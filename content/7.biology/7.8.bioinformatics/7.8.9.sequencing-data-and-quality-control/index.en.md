---
title: Sequencing Data and Quality Control
description: "What sequencing data look like before analysis. Error profiles of the platforms (short-read sequencing by synthesis and DNA nanoballs, PacBio HiFi consensus, nanopore reads), read length and accuracy. Reads and the FASTQ format, Phred quality scores and their ASCII encodings, expected errors per read, binned scores and the calibration of quality values. Library and read structure: single-end and paired-end reads, insert size and adapter read-through, sample barcodes and demultiplexing with error-tolerant indexes, index hopping, unique molecular identifiers and their collisions, amplicon libraries. Quality control with FastQC and MultiQC, trimming of adapters and low-quality ends (the running-sum algorithm), PCR and optical duplicates, library complexity. k-mer spectra: error, heterozygous and homozygous peaks, genome size and heterozygosity by a GenomeScope-style fit. Designing an experiment: coverage, uniformity and read length."
---

A sequencing run ends with files of reads, and every later analysis (mapping, assembly, variant calling, expression) inherits their errors. This chapter is about the data themselves: what kinds of errors each platform makes, how base-by-base confidence is recorded, how the structure of a library shows up in the reads, how quality is checked and improved before analysis, and how the counts of short words in the reads already reveal the size and heterozygosity of a genome. The chemistry of sequencing (chain termination, **sequencing by synthesis** with **reversible terminators**, **single-molecule real-time sequencing** and **nanopore sequencing**) and the construction of libraries are described in [7.2.6](/7.2.6#sec-6.7), and the statistics of coverage in [7.2.6](/7.2.6#sec-6.9) and [7.4.14](/7.4.14#sec-14.2.1); we use them without repeating them. The running example is the genome of HG002, an Ashkenazi Jewish man (Coriell NA24385) whose genome and those of his parents (HG003 and HG004) have been sequenced on every major platform by the Genome in a Bottle consortium, giving public data and a benchmark set of variants against which methods are tested; a second example is the small amplicon panel of single-nucleotide polymorphisms (including rs4988235) sequenced as $50$-nt single-end reads on a DNBSEQ benchtop instrument, typical of teaching and clinical panels. The files and formats of the field were introduced in [7.8.1](/7.8.1); the reads are mapped to a reference in [7.8.10](/7.8.10) and assembled in [7.8.11](/7.8.11).

## 9.1. From Signal to Bases

### 9.1.1. Reads and Base Calling

**Definition 9.1.1 (Read)** A **read** is the sequence of bases inferred by a sequencing instrument from one template molecule (or one cluster of copies of it), together with a quality score for each base; in paired-end sequencing the two reads from the two ends of a fragment are called *mates*.

Instruments do not observe bases but signals: images of fluorescent clusters, light pulses in a nanometre well, or the ionic current through a pore. *Base calling* converts signals into bases and quality scores. For short-read instruments it is a classification of the intensities in each cycle, corrected for the cross-talk between dye channels and for phasing ([7.2.6](/7.2.6#sec-6.7.2)); for nanopore reads it is the translation of a current trace, in which several nucleotides influence the current at once, into a sequence of unknown length, done by neural networks (recurrent or transformer models trained with a connectionist temporal classification loss) in the programs Dorado and its predecessors. Each generation of base-calling models has improved the accuracy of the same raw data, so raw signal files are kept when possible and old data can be re-called.

### 9.1.2. Error Profiles of the Platforms

The platforms differ less in their average accuracy than in the *kind* of errors they make, and the kind of error determines which analyses suffer.

| Platform | Reads | Dominant errors | Consequences |
|---|---|---|---|
| Illumina (bridge-amplified clusters, four- or two-color SBS) | $2\times 50$ to $2\times 300$ nt; typically $2\times 150$ | substitutions, increasing towards the $3'$ end with phasing; in two-color chemistry a run of G (no signal) when a cluster fades, so reads end in poly-G; errors after GGC motifs | quality trimming; poly-G trimming; repeats longer than the fragment cannot be resolved |
| DNBSEQ (DNA nanoballs by rolling-circle amplification, combinatorial probe-anchor synthesis) | $50$ to $2\times 150$ nt | substitutions; few duplicates from amplification on the chip, because each nanoball is a linear copy of one circle and errors do not propagate between copies | similar to Illumina |
| PacBio HiFi (circular consensus of a single molecule) | $10$–$25$ kb, accuracy above Q20 by definition, typically about Q30 | residual insertions and deletions in homopolymers | assembly, phasing, structural variants, methylation from kinetics |
| Oxford Nanopore (R10.4.1 pores) | $10$ kb to over $1$ Mb; about Q20 for single reads, higher for duplex reads that read both strands | insertions and deletions, especially in homopolymers, and systematic errors at some motifs and modified bases | ultra-long reads span centromeres and segmental duplications; direct RNA and modification calling |
| Sanger | up to about $1000$ nt, about Q40 | low-quality ends of the trace | validation of individual variants |

The short-read error rate rises with cycle number because of phasing: in each cycle a small fraction of the strands in a cluster falls out of step, so the signal of the correct base declines and that of its neighbours grows. In single-molecule reads errors are largely random in position, so they can be removed by consensus. PacBio HiFi reads exploit this within one molecule: a circularized template is read many times by the same polymerase, and the consensus of the passes is far more accurate than any single pass.

![Read length and accuracy of the main sequencing platforms. A: representative ranges of read length and per-base accuracy (as a Phred score and as percent correct) for current chemistries (2025; they vary with instrument, kit and base-calling model); hollow markers are older or alternative modes. B: why repeated passes over a circular template help: with an independent error probability of 0.1 per pass at a base, a majority vote of n passes errs with probability P(Bin(n, 0.1) ≥ (n+1)/2); five passes reach about Q21 and nine about Q31. The real HiFi consensus uses a probabilistic model of all passes and corrects insertions and deletions as well](./plots/platforms.py)

**Example 9.1.1** If each pass has an error probability $e = 0.1$ at a base, independently, a majority vote over $n = 5$ passes is wrong when at least $3$ passes are wrong, with probability $\binom{5}{3}\mathrm{e}^3(1-e)^2 + \binom{5}{4}\mathrm{e}^4(1-e) + \mathrm{e}^5 = 0.00856$, that is Q$20.7$. With $n = 9$ the probability is $8.9\times10^{-4}$ (Q$30.5$), with $n = 15$, $3.4\times10^{-5}$ (Q$44.7$). Accuracy therefore grows exponentially in the number of passes, which is the number of times the polymerase goes round the circle; for a fixed read length, it falls as the insert gets longer. This is why HiFi libraries are size-selected to $15$–$20$ kb, a compromise between length and accuracy.

## 9.2. Quality Scores and the FASTQ Format

### 9.2.1. FASTQ

**Definition 9.2.1 (FASTQ Format)** The **FASTQ format** stores reads as records of four lines: a header beginning with `@` followed by the read identifier and an optional description; the sequence; a separator line beginning with `+` (optionally repeating the identifier); and a string of quality characters of the same length as the sequence, one per base, each encoding a Phred quality score $Q$ as the character with code $Q + 33$.

```text
@A00123:45:HXXXXXXXX:2:1101:10221:1000 1:N:0:ACGTACGT+TGCATGCA
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTTAT
+
FFFFFFFFF:FFFFFFFFFFFFFFFFF,FFFFFFFFFFF:FFFFFFFFF:FFFFFFFFF#F:F
```

The Illumina header encodes the instrument, run, flow cell, lane, tile and the $x$ and $y$ coordinates of the cluster, then the mate number, whether the read failed the chastity filter (`Y`/`N`), a control bit and the index sequences of the sample. DNBSEQ headers (`@E100012345L1C001R00100000123/1`) encode the flow cell, lane, column, row and mate. The position on the flow cell is used to recognize optical duplicates (§9.4.3).

The base-by-base quality is the **Phred quality score** $Q = -10\log_{10}p_{\mathrm{err}}$ of [7.2.6](/7.2.6#sec-6.7.2): Q$20$ means one error in $100$ bases, Q$30$ one in $1000$, Q$40$ one in $10^4$. Sequencing reports summarize a run by the fraction of bases at or above Q$30$, typically $85$–$95\,\%$ for short-read runs.

**Formula 9.2.1 (Expected Errors in a Read)** If the bases of a read have qualities $Q_1, \dots, Q_L$ and their errors are independent, the expected number of errors and the probability that the read is error-free are

$$
\mathbb{E}[\text{errors}] = \sum_{i=1}^{L} 10^{-Q_i/10}, \qquad \mathbb{P}(\text{no error}) = \prod_{i=1}^{L}\bigl(1 - 10^{-Q_i/10}\bigr).
$$

**Example 9.2.1** A $150$-nt read whose first $100$ bases have Q$30$ and last $50$ bases Q$20$ has $100 \times 0.001 + 50 \times 0.01 = 0.6$ expected errors, and is error-free with probability $0.999^{100} \times 0.99^{50} = 0.547$. The last third of the read contributes five sixths of the expected errors. Filtering reads by expected errors (as in amplicon pipelines, [7.8.14](/7.8.14)) rather than by mean quality accounts for this, since the mean quality of the read ($26.7$) hides where the errors are.

### 9.2.2. Encodings and Binning

The quality characters are printable ASCII codes. The current standard, *Phred+33* (Sanger encoding, used by all Illumina software since version 1.8 in 2011), adds $33$ to $Q$: `!` ($33$) is Q$0$, `+` ($43$) Q$10$, `5` ($53$) Q$20$, `?` ($63$) Q$30$ and `I` ($73$) Q$40$. Older Illumina data used *Phred+64* (`@` for Q$0$, `h` for Q$40$), and the earliest Solexa data a different score, $Q_{\mathrm{Sol}} = -10\log_{10}[p/(1-p)]$, also offset by $64$, which can be negative. An encoding can be recognized from the characters present: codes below $59$ (`;`) occur only in Phred+33 files, and lowercase letters, above `J` ($74$, Q$41$ in Phred+33), almost only in Phred+64 files (some long-read data use higher Phred+33 scores). Programs that assume the wrong encoding shift every quality by $31$ and silently trim everything or nothing.

Modern instruments *bin* qualities into a few values to make files smaller: NovaSeq data use only Q$2$, Q$12$, Q$23$ and Q$37$, written `#`, `-`, `8` and `F` (the read above contains `F`, `:` for Q$25$ and `,` for Q$11$ from a four-level scheme of another instrument). Binning loses little information for variant calling, because the scores were not calibrated to more than a few levels anyway, and it lets compression reduce the qualities, the least compressible part of a FASTQ file, by half or more.

### 9.2.3. Calibration

A quality score is a claim about a probability, and it can be checked: among all bases reported at Q$30$, one in a thousand should be wrong. At positions of the genome known not to vary in a sample (sites absent from dbSNP and from the sample's high-confidence variants), every mismatch between read and reference is an error, so the empirical quality of a set of $n$ bases with $m$ mismatches is $-10\log_{10}[(m + 1)/(n + 2)]$ (the $+1$ and $+2$ give a sensible value when $m = 0$). Base callers are often miscalibrated, overconfident at high scores, and the error rate depends on the cycle and on the neighbouring bases in ways the base caller did not model. *Base quality score recalibration* (BQSR, part of the GATK workflow of [7.8.12](/7.8.12)) groups bases by reported quality, cycle and dinucleotide context, computes the empirical quality of each group from the mismatches at known non-variant sites, and replaces each base's quality by that value. Calibrated qualities matter because a variant caller multiplies the error probabilities of the reads ([7.8.12](/7.8.12)), so a systematic overestimate of quality inflates the confidence of false variants.

![Calibration of base quality scores (simulated). A: reported against empirical quality for three contexts (early cycles after A; late cycles after A; late cycles after G); the base caller is overconfident above Q25, and more so late in the read and after G, so the curves fall below the diagonal. B: after recalibration each base carries the empirical quality of its group, and the qualities agree with the error rates measured on new data](./plots/quality-calibration.py)

![Quality by position for simulated 2 × 150 Illumina-style reads, as in the FastQC module "per base sequence quality": boxes are quartiles, whiskers the 10th and 90th percentiles, red lines medians and the purple line the mean. A: read 1, with quality slowly declining towards the 3′ end. B: read 2, lower throughout and with more low-quality outliers at the end. Background bands mark the FastQC zones: good above Q28, reasonable from Q20 to Q28, poor below Q20](./plots/quality-by-position.py)

## 9.3. Library and Read Structure

### 9.3.1. Single-End and Paired-End Reads

**Definition 9.3.1 (Paired-End Sequencing)** In **paired-end sequencing** each library fragment is read from both ends, giving two reads (mates) that point towards each other and are separated on the genome by the *insert size*, the length of the fragment between the adapters; in single-end sequencing only one end is read.

Mates are stored in two FASTQ files (`_R1` and `_R2`, in the same order) or interleaved in one. The pair constrains mapping (the mates must align on opposite strands at about the expected distance, [7.8.10](/7.8.10)), detects structural variants as pairs with wrong orientation or distance ([7.8.12](/7.8.12)) and scaffolds contigs ([7.8.11](/7.8.11)). Single-end reads, cheaper and faster, suffice for counting applications such as amplicon genotyping and some expression assays.

**Definition 9.3.2 (Adapter)** An **adapter** in a sequencing library is a synthetic oligonucleotide joined to both ends of each fragment that contains the sequences needed for capture on the flow cell, for priming the sequencing reactions and for the sample index.

The insert size is distributed around a value set by fragmentation and size selection. If the insert is shorter than twice the read length, the mates overlap, and the overlap can be used to merge them into one longer, more accurate sequence; if it is shorter than the read length, the sequencer reads through the insert into the adapter at the $3'$ end, and the read ends in adapter sequence that must be removed before mapping or assembly. Libraries of naturally short DNA, such as cell-free DNA in plasma (fragments of about $167$ bp, protected by a **nucleosome** and its linker), ancient DNA or small RNA, contain many such inserts.

![Insert size and adapter read-through for 2 × 150 reads. A: insert-size distributions of a whole-genome library (normal, mean 350, standard deviation 90 nt) and of cell-free DNA (mononucleosomal peak at 167 nt, 10 % dinucleosomal fragments at 334 nt). In the first, 1.3 % of fragments are shorter than 150 nt and are read through into the adapter and 29 % give overlapping mates; in cell-free DNA the figures are 11.6 % and 91 %. B: the three cases for one fragment: no overlap, overlapping mates, and read-through into the adapters](./plots/insert-size.py)

Adapter read-through is detected in two ways: by searching the $3'$ end of each read for the adapter sequence, allowing mismatches and partial matches at the very end (cutadapt, Trimmomatic), or, for paired reads, by aligning read 1 to the reverse complement of read 2: if they overlap with their $5'$ ends offset past each other, the insert is shorter than the reads and both can be cut at the end of the overlap without knowing the adapter sequence (fastp, AdapterRemoval).

### 9.3.2. Sample Barcodes and Demultiplexing

A run of a modern instrument produces far more reads than one sample needs, so many libraries are pooled. Each library carries one or two short *index* sequences (sample barcodes, typically $8$ or $10$ nt) in its adapters, read in separate index reads.

**Definition 9.3.3 (Demultiplexing)** **Demultiplexing** is the assignment of the reads of a pooled sequencing run to their samples by their index sequences, usually allowing a small number of mismatches to the expected index.

Tolerating mismatches requires that the indexes of a pool be far apart: if every pair differs at three or more positions (**Hamming distance** at least $3$), a read index with one error is still closer to its true index than to any other, and the assignment is unambiguous. With a per-base error rate $\varepsilon = 0.005$ in the index read, $1 - 0.995^8 = 3.9\,\%$ of $8$-nt indexes contain at least one error, which exact matching would discard; a dual index of $2\times 8$ nt has an error in $7.7\,\%$ of reads.

On patterned flow cells, free adapter molecules can prime the copying of another library's molecules, so that a read receives an index of a different sample (*index hopping*). With a single index per sample, such reads are silently assigned to the wrong sample, at rates of a fraction of a percent to a few percent depending on library preparation. *Unique dual indexing*, in which every sample has its own pair of indexes and no index is shared, makes a hopped read carry an unexpected combination, so it is discarded rather than misassigned. Index hopping matters most when rare variants or low-abundance sequences are compared between pooled samples, as in tumour and liquid-biopsy sequencing.

```bash
# Demultiplex a run with the Illumina converter (sample sheet lists the index pairs)
bcl-convert --bcl-input-directory run/ --output-directory fastq/ --sample-sheet SampleSheet.csv
# Check checksums of the delivered files before anything else (7.8.1)
md5sum -c md5.txt
```

### 9.3.3. Unique Molecular Identifiers

**Definition 9.3.4 (Unique Molecular Identifier)** A **unique molecular identifier** (UMI) is a short random sequence attached to each original molecule before amplification, so that reads sharing both a UMI and a mapping position are taken to be copies of one molecule.

With UMIs, molecules rather than reads are counted ([7.2.6](/7.2.6#sec-6.8.1)), and in duplex sequencing, where both strands of each molecule carry identifiers, a consensus of all copies of both strands removes amplification and sequencing errors to below $10^{-7}$ per base, enough to detect mutations present in a tiny fraction of cells. Two complications arise. First, different molecules may receive the same UMI by chance, a **birthday problem**: with $n$ molecules at the same position and $4^\ell$ possible UMIs of length $\ell$, the probability that some two share a UMI is about $1 - \exp[-n(n - 1)/(2\cdot4^\ell)]$. Second, errors in the UMI create apparent new molecules. The directional method of UMI-tools handles the second:

**Algorithm 9.3.1 (Directional UMI Clustering)** For the reads at one mapping position, with distinct UMIs $u$ observed $c(u)$ times:

1. Build a directed graph on the UMIs with an edge $u \to v$ whenever $u$ and $v$ differ at one position and $c(u) \ge 2c(v) - 1$: an error-derived UMI is one substitution away from its source and much rarer.
2. Each connected component of the graph, taken from its most abundant UMI along the directed edges, is one molecule; count the components.

Building the graph by comparing all pairs takes $O(U^2\ell)$ time for $U$ distinct UMIs at a position, which is small because $U$ is rarely more than a few thousand; generating the $3\ell$ single-substitution neighbours of each UMI and looking them up in a **hash table** reduces it to $O(U\ell)$.

**Example 9.3.1** With $\ell = 10$ ($4^{10} \approx 1.05\times10^6$ UMIs) and $n = 100$ molecules starting at the same position, the collision probability is $1 - \mathrm{e}^{-4950/1\,048\,576} = 0.47\,\%$; with $\ell = 8$ it is $7.3\,\%$. For $n = 1000$ molecules, as for a highly expressed gene in one cell, $\ell = 10$ gives $38\,\%$ and $\ell = 12$ gives $2.9\,\%$. This is why single-cell protocols use UMIs of $10$–$12$ nt.

### 9.3.4. Amplicon Libraries

In an *amplicon* library the targets are amplified by PCR with specific primers, and the products are indexed in a second PCR ([7.2.6](/7.2.6#sec-6.8.2)). All reads of one amplicon begin at the same position (the primer), so duplicate marking by position (§9.4.3), which assumes random fragmentation, must not be applied; the primer sequences, which come from the oligonucleotides rather than the sample, must be trimmed or masked before variant calling, or a variant under a primer is invisible; and the samples of a pool must be mixed in equal amounts so that each receives a similar number of reads. A panel of a few hundred SNPs sequenced at $50$ nt on a benchtop instrument, as in teaching laboratories and forensic or pharmacogenetic tests, needs only tens of thousands of reads per sample.

## 9.4. Quality Control and Filtering

### 9.4.1. Quality Reports

FastQC computes a set of summaries for one FASTQ (or BAM) file and flags each as pass, warning or failure; MultiQC collects the reports of all samples and tools of a project into one page, where outlying samples stand out.

| Module | Expected for a good genomic library | Common problems |
|---|---|---|
| Per-base sequence quality | high, declining slowly towards the $3'$ end | a sharp drop (instrument problem); low quality in read 2 |
| Per-tile sequence quality | uniform over the flow cell | bubbles, dirt or edge effects in some tiles |
| Per-sequence quality | one peak at high quality | a subpopulation of poor reads |
| Per-base sequence content | four nearly flat, parallel lines | bias in the first $10$–$15$ bases from random priming or transposase insertion (normal); amplicons and bisulfite libraries are unbalanced by design |
| Per-sequence GC content | close to the theoretical distribution for the species | a second peak (contamination, adapter dimers); a shoulder from PCR bias |
| Per-base N content | near zero | a cycle where base calling failed |
| Sequence length distribution | one length (before trimming) | expected after trimming |
| Sequence duplication levels | mostly unique for genomes | high duplication: low input or over-amplification (expected for RNA-seq of highly expressed genes and for amplicons) |
| Overrepresented sequences | none above $0.1\,\%$ | adapter dimers, rRNA, contaminants |
| Adapter content | near zero | read-through in short inserts |

The thresholds of FastQC were chosen for random whole-genome libraries, so a "failure" is often an expected property of the assay (RNA-seq duplication, amplicon base composition); interpreting the report requires knowing what the library should look like.

### 9.4.2. Trimming and Filtering

Reads are trimmed (adapter sequence, low-quality $3'$ ends, poly-G tails of two-color chemistry) and filtered (reads that become too short, reads with too many Ns or low-quality bases). Quality trimming should remove a low-quality tail without cutting at the first isolated low base.

**Algorithm 9.4.1 (Running-Sum Quality Trimming)** Given qualities $q_1, \dots, q_L$ of a read and a threshold $T$:

1. Set $s = 0$, $s^* = 0$, $k = L + 1$. For $i = L, L - 1, \dots, 1$: add $T - q_i$ to $s$; if $s < 0$, stop; if $s > s^*$, set $s^* = s$ and $k = i$.
2. Keep bases $1, \dots, k - 1$.

The algorithm finds the suffix with the largest total deficit $\sum_{i \ge k}(T - q_i)$ before a stretch of good bases makes the running sum negative; the cut falls where the tail is poor *on balance*, so an isolated good base inside a bad tail, or an isolated bad base among good ones, does not decide it. It runs in $O(L)$ time and is the method of BWA (option `-q`) and cutadapt; sliding-window trimming (cut where the mean quality of a window of $4$ bases first falls below $T$, as in Trimmomatic and fastp) is an alternative.

**Example 9.4.1** For the $15$ qualities $38, 38, 37, 36, 35, 34, 30, 22, 18, 25, 12, 8, 15, 5, 2$ and $T = 20$, the running sum from the end is $18, 36, 41, 53, 61$ (after the bases with $2, 5, 15, 8, 12$), then $56$, $58$, $56$, $46$, $32$, $17$, $1$ and $-16$. Its maximum, $61$, is reached after base $11$ (Q$12$), so bases $11$–$15$ are removed and the first $10$ kept, including Q$18$ at position $9$, which is followed by the better Q$25$.

```bash
# Paired-end trimming and filtering with fastp: adapters detected by overlap, poly-G tails removed,
# 3' ends cut where a 4-base window falls below Q20, reads shorter than 36 nt dropped
fastp -i HG002_R1.fq.gz -I HG002_R2.fq.gz -o trim_R1.fq.gz -O trim_R2.fq.gz \
      --detect_adapter_for_pe --trim_poly_g --cut_right --cut_window_size 4 --cut_mean_quality 20 \
      --length_required 36 --thread 8 --html HG002.fastp.html --json HG002.fastp.json
fastqc -t 4 -o qc/ trim_R1.fq.gz trim_R2.fq.gz
multiqc qc/ .
```

Aggressive trimming is not always better. Modern aligners and variant callers use base qualities and *soft-clip* adapter remnants and poor ends themselves ([7.8.10](/7.8.10)), so for whole-genome resequencing only adapter removal is essential; for assembly ([7.8.11](/7.8.11)), $k$-mer counting and amplicon analysis, where every error creates false sequence, trimming and filtering matter more.

### 9.4.3. Duplicates and Library Complexity

**Definition 9.4.1 (PCR and Optical Duplicate)** A **PCR duplicate** is a read or read pair derived from the same original library molecule as another read, through amplification during library preparation; it is recognized after mapping as a pair with the same chromosome, start positions of both mates and orientations as another pair. An *optical duplicate* is a duplicate whose two clusters lie close together on the same tile of the flow cell (within $100$ pixels on unpatterned and about $2500$ on patterned flow cells), arising from one cluster called twice or from seeding of a neighbouring well.

Duplicates carry no independent information: a polymerase error in an early PCR cycle appears in all copies and looks like a well-supported variant. Variant-calling pipelines therefore mark them (Picard MarkDuplicates, samtools markdup, [7.8.10](/7.8.10)) so that only one read of each set is counted. The fraction of duplicates depends on the number of distinct molecules in the library, its *complexity*.

**Formula 9.4.1 (Library Complexity)** If a library contains $C$ distinct molecules, equally likely to be sequenced, and $n$ reads are drawn, the number of distinct molecules observed is, in expectation,

$$
D(n) = C\bigl(1 - \mathrm{e}^{-n/C}\bigr),
$$
since each molecule is missed with probability $(1 - 1/C)^n \approx \mathrm{e}^{-n/C}$; the duplicate fraction is $1 - D(n)/n$. Given the observed $n$ and $D$, the equation can be solved for $C$ (Picard EstimateLibraryComplexity), and $D$ predicted for deeper sequencing of the same library.

**Example 9.4.2** A run gives $n = 4\times10^8$ read pairs, of which $D = 3\times10^8$ are distinct ($25\,\%$ duplicates). Solving $C(1 - \mathrm{e}^{-n/C}) = D$ gives $C = 6.6\times10^8$ molecules. Sequencing the same library to $8\times10^8$ pairs would yield $4.6\times10^8$ distinct pairs ($42\,\%$ duplicates), and to $1.6\times10^9$, only $6.0\times10^8$ ($62\,\%$ duplicates): doubling the reads would add only $55\,\%$ more information. A new library with more input DNA, not more sequencing, is the remedy. In practice molecules are not equally likely to be sequenced (amplification favours some), so the model underestimates duplication at depth; the extrapolation methods of the program preseq, which fit the observed frequencies of duplicate counts, are more accurate.

![Library complexity and duplicates. A: distinct molecules observed against reads sequenced for libraries of 1.0 × 10⁸, 6.6 × 10⁸ and 3.0 × 10⁹ distinct molecules, from D(n) = C(1 − e^(−n/C)) (Formula 9.4.1); the dashed line is the limit of no duplicates. The point is a run of 400 million read pairs with 300 million distinct, which implies C = 6.6 × 10⁸. B: the duplicate fraction 1 − D(n)/n for the same libraries; it grows with depth and falls with complexity](./plots/library-complexity.py)

## 9.5. k-mer Spectra

**Definition 9.5.1 (k-mer and k-mer Spectrum)** A **k-mer** is a substring of length $k$ of a sequence; a read of length $L$ contains $L - k + 1$ of them. The **k-mer spectrum** of a set of reads is the histogram giving, for each $c = 1, 2, \dots$, the number of distinct $k$-mers (usually canonical, [7.8.1](/7.8.1#sec-1.3)) that occur exactly $c$ times in the reads.

Counting $k$-mers needs no reference genome, and for $k$ around $21$–$31$ most $k$-mers of a large genome occur only once in it ($4^{21} \approx 4.4\times10^{12}$, a thousand times the size of the human genome), so the spectrum reflects the genome directly. Counting is done with a **hash table** keyed by the $k$-mer encoded in $2k$ bits, with memory-saving variants in Jellyfish (a lock-free hash table) and KMC (disk-based partitioning by minimizers).

**Formula 9.5.1 (k-mer Coverage)** With base coverage $c$ and reads of length $L$, a $k$-mer present once in the genome is contained in about

$$
c_k = c\,\frac{L - k + 1}{L}
$$
reads, because a read covering a base contains a given $k$-mer starting there only if the read starts at most $L - k$ bases before it. A $k$-mer is free of sequencing errors with probability $(1 - \varepsilon)^k$ for per-base error rate $\varepsilon$.

The spectrum of a diploid genome has three parts. Errors produce $k$-mers that occur once or twice: with $\varepsilon = 0.002$ and $k = 21$, $1 - 0.998^{21} = 4.1\,\%$ of $k$-mer instances contain an error, and nearly every such $k$-mer is new. Homozygous sequence, identical on both haplotypes, produces a peak at the $k$-mer coverage $c_k$. At heterozygous sites, the $k$-mers that overlap a difference exist on only one haplotype and form a second peak at $c_k/2$. Repeats add smaller peaks at multiples of $c_k$. The counts in each peak are approximately Poisson, with extra variance from uneven coverage, so they are modeled by **negative binomial distributions**.

**Formula 9.5.2 (Diploid k-mer Model)** For a diploid genome of haploid length $G$ with per-base heterozygosity $r$, a position starts a $k$-mer shared by both haplotypes with probability $(1 - r)^k$, and otherwise starts two distinct haplotype-specific $k$-mers. With $\lambda$ the $k$-mer coverage per haplotype, the expected number of distinct genomic $k$-mers occurring $x$ times is

$$
h(x) = G\Bigl[\,2\bigl(1 - (1 - r)^k\bigr)\,f(x; \lambda) + (1 - r)^k f(x; 2\lambda)\Bigr],
$$
with $f(\cdot\,; \mu)$ a negative binomial distribution of mean $\mu$. The total number of genomic $k$-mer instances is $2\lambda G$, so $G$ is estimated as the number of $k$-mer instances outside the error peak divided by $2\lambda$, and $r$ from the relative heights of the two peaks.

This is the model of GenomeScope (which also includes duplicated sequence at $3\lambda$ and $4\lambda$), fitted to the spectrum by nonlinear **least squares**. It estimates the size, heterozygosity and repeat content of a genome before any assembly, and its error peak gives the error rate of the reads. It also detects contamination (an unexpected peak at another coverage) and, for polyploids, the ploidy.

**Example 9.5.1** The figure shows the spectrum of a simulated diploid genome of $G = 100\,\mathrm{Mb}$ with heterozygosity $r = 1\,\%$, sequenced to $30\times$ with $150$-nt reads and error rate $0.2\,\%$, counted with $k = 21$. By Formula 9.5.1 the homozygous peak is at $c_k = 30 \times 130/150 = 26$ and the heterozygous peak at $13$. The fraction of haploid positions starting a shared $k$-mer is $0.99^{21} = 0.81$, so there are $0.81G$ homozygous and $2 \times 0.19G = 0.38G$ heterozygous distinct $k$-mers; although heterozygosity is only $1\,\%$, almost a fifth of the positions are within $k$ bases of a heterozygous site, which is why the heterozygous peak is prominent. Fitting Formula 9.5.2 to the counts at $x \ge 6$ gives $G = 100.0\,\mathrm{Mb}$, $r = 1.00\,\%$ and $\lambda = 13.0$; dividing the $k$-mer instances at $x \ge 6$ by $2\lambda$ gives $99.9\,\mathrm{Mb}$. For a human genome at $30\times$, the same calculation gives about $3\,\mathrm{Gb}$ and a heterozygosity of about $0.1\,\%$.

![The 21-mer spectrum of a simulated diploid genome (haploid size 100 Mb, heterozygosity 1 %, 30× coverage with 150-nt reads, base error rate 0.2 %) and a GenomeScope-style fit. Error k-mers form the peak at counts 1–3; k-mers on one haplotype only form the heterozygous peak at 13, k-mers shared by both haplotypes the homozygous peak at 26. The red line is the fitted mixture of two negative binomials (Formula 9.5.2) at counts of 6 or more; dashed lines are its components. The fit recovers the simulated genome size and heterozygosity](./plots/kmer-spectrum.py)

```bash
# 21-mer spectrum of trimmed reads and a GenomeScope fit
jellyfish count -C -m 21 -s 5G -t 16 -o reads.jf <(zcat trim_R1.fq.gz trim_R2.fq.gz)
jellyfish histo -t 16 reads.jf > reads.histo
genomescope2 -i reads.histo -o genomescope/ -k 21 -p 2
```

## 9.6. Designing a Sequencing Experiment

The first design question is the depth. The **sequencing coverage** $c = N\ell/G$ of [7.2.6](/7.2.6#sec-6.9) and the Lander–Waterman model of [7.4.14](/7.4.14#sec-14.2.1) give the fraction of the genome covered and, by the **binomial distribution** of reads between the two alleles, the depth needed to call heterozygous variants. Typical choices:

| Application | Depth or reads | Reason |
|---|---|---|
| Human germline genome | $30\times$ mean | each allele of a heterozygote seen several times at almost every site |
| **Exome sequencing** | $100\times$ mean over targets | capture is uneven, so a high mean is needed for $20\times$ at most targets |
| Tumour genome | $60$–$100\times$ tumour, $30\times$ normal | variants present in a fraction of cells (subclones, impure samples) |
| Low-pass genome with imputation | $0.5$–$4\times$ | genotypes inferred from reference panels of haplotypes ([7.8.13](/7.8.13)) |
| De novo assembly | $30$–$60\times$ long reads, plus Hi-C | contiguity requires spanning repeats ([7.8.11](/7.8.11)) |
| Bulk RNA-seq | $20$–$40$ million reads per sample | depends on the expression level of the genes of interest ([7.9](/7.9)) |
| Amplicon panel | $10^4$–$10^5$ reads per sample | a few hundred targets at hundreds of reads each |

Real coverage is less uniform than the Poisson model, because fragmentation, amplification and capture favour some sequences (GC-rich and AT-rich regions are underrepresented in PCR-amplified libraries). Uniformity is summarized by the fraction of the target above a threshold and, for capture data, by the *fold-80 base penalty*: the factor by which the mean depth would have to be raised for $80\,\%$ of the target bases to reach the current mean, equal to the mean divided by the 20th percentile of depth.

**Example 9.6.1** Suppose the mean depth of the exome targets is $100\times$ but their depths vary across targets as a gamma distribution with shape $4$ (coefficient of variation $0.5$). The fraction of targets below $20\times$ is $0.91\,\%$, the 20th percentile of depth is $57\times$, and the fold-80 penalty is $100/57 = 1.74$. With perfectly uniform coverage, $20\times$ everywhere would need a mean of only about $20\times$; non-uniformity, not the Poisson variance, sets the $100\times$ standard.

Read length and type matter as much as depth. Short reads cannot be placed uniquely in repeats longer than the fragment: several percent of the human genome, including many segmental duplications and genes with pseudogenes (*SMN1* and *SMN2*, *CYP2D6*, *PMS2*), is *difficult* for short reads, and long reads or linked approaches are needed there. Paired reads with longer inserts resolve more. For a fixed budget, the choice is between more samples at lower depth and fewer at higher depth, a statistical design question of the kind treated in [7.7.18](/7.7.18).

## Summary

| Topic | Key points |
|---|---|
| Platforms | short reads (SBS on clusters or nanoballs): substitutions rising along the read, poly-G in two-color chemistry; HiFi: consensus of passes, accuracy exponential in passes (Example 9.1.1); nanopore: indels in homopolymers, ultra-long reads, direct modification calls; base calling by neural networks |
| Reads and FASTQ | a read with per-base qualities (Definition 9.1.1); four-line records (Definition 9.2.1); headers encode flow-cell position and index |
| Qualities | **Phred quality score** $Q = -10\log_{10}p$; Phred+33 (`?` = Q30, `I` = Q40), historical Phred+64 and Solexa; binning; expected errors $\sum 10^{-Q_i/10}$ (Formula 9.2.1); calibration and BQSR from mismatches at non-variant sites |
| Library structure | paired-end reads and insert size (Definition 9.3.1); adapters (Definition 9.3.2) and read-through below the read length; demultiplexing (Definition 9.3.3) with indexes at Hamming distance $\ge 3$; unique dual indexes against index hopping; UMIs (Definition 9.3.4), birthday collisions and directional clustering (Algorithm 9.3.1); amplicons: no positional deduplication, primer trimming |
| QC | FastQC modules and their expected deviations by assay; MultiQC; running-sum trimming (Algorithm 9.4.1); trimming matters most for assembly, $k$-mer and amplicon analyses |
| Duplicates | PCR and optical duplicates (Definition 9.4.1); complexity $D(n) = C(1 - \mathrm{e}^{-n/C})$ (Formula 9.4.1) predicts the return on deeper sequencing |
| k-mer spectra | spectrum of $k$-mer counts (Definition 9.5.1); $c_k = c(L - k + 1)/L$ (Formula 9.5.1); error, heterozygous ($\lambda$) and homozygous ($2\lambda$) peaks; GenomeScope model (Formula 9.5.2) gives $G = $ instances$/2\lambda$ and $r$ |
| Design | depth by application; uniformity and fold-80 penalty (Example 9.6.1); repeats and difficult regions set the need for long reads |

## Questions

1. Decode the quality string `?5+!I` (Phred+33) into Phred scores and error probabilities, and compute the expected number of errors in these five bases.

   **Answer** Codes $63, 53, 43, 33, 73$ minus $33$ give Q$30$, Q$20$, Q$10$, Q$0$, Q$40$, with error probabilities $0.001$, $0.01$, $0.1$, $1$ and $0.0001$. By Formula 9.2.1 the expected number of errors is $1.1111$; a Q$0$ base (often an N) is essentially uninformative.

2. A FASTQ file contains the characters `h`, `f` and `B` but none below `@`. Which encoding does it use, and what are the scores of these characters?

   **Answer** Characters from `@` ($64$) upwards with lowercase letters such as `h` ($104$) indicate Phred+64 (Illumina 1.3–1.7): `h` is Q$40$, `f` ($102$) Q$38$ and `B` ($66$) Q$2$, which Illumina 1.5–1.7 used as a marker for an unreliable read end. Read as Phred+33 the same characters would give impossible values of $71$, $69$ and $33$. Convert with `seqtk seq -Q64 -V` before using modern tools.

3. Why do short-read errors increase along the read, while the errors of single-molecule reads do not, and how does this difference shape the strategies for removing errors?

   **Answer** On a cluster, phasing accumulates: each cycle a small fraction of strands falls out of step, so the signal becomes a growing mixture of neighbouring positions and the base call less certain towards the $3'$ end ([7.2.6](/7.2.6#sec-6.7.2)); errors are mostly substitutions concentrated in the tail, so trimming tails and recalibrating qualities by cycle help. In single-molecule reads each base is observed once by a single enzyme or pore, with error probability roughly constant along the read and largely random, so errors are removed by consensus: of passes over one molecule (HiFi), of both strands (duplex nanopore), or of many reads at a site after alignment or in assembly.

4. A pool of $96$ samples is demultiplexed allowing one mismatch per index. Why must the index set have minimum Hamming distance at least $3$, and what goes wrong with distance $2$?

   **Answer** With one mismatch allowed, a read index is assigned to any expected index within distance $1$. If two expected indexes differ at only $2$ positions, there are sequences at distance $1$ from both (change one of the two differing positions), so a read with one error may be assigned to the wrong sample or must be discarded as ambiguous. With minimum distance $3$, the balls of radius $1$ around the indexes are disjoint, the same argument as for single-error-correcting codes, so one error is always corrected correctly.

5. Compute the probability of a UMI collision among $n = 300$ molecules at the same position for $\ell = 10$ and $\ell = 12$, and explain how collisions bias counts.

   **Answer** $n(n - 1)/2 = 44\,850$. For $\ell = 10$: $1 - \exp(-44\,850/1\,048\,576) = 4.2\,\%$; for $\ell = 12$ ($4^{12} = 16\,777\,216$): $1 - \exp(-44\,850/16\,777\,216) = 0.27\,\%$. A collision merges two molecules into one, so counts are underestimated, more for highly expressed genes where many molecules share a position: the bias is nonlinear and compresses the high end of the expression range. Counts can be corrected by the expected number of distinct UMIs, $4^\ell[1 - (1 - 4^{-\ell})^n]$, solved for $n$, analogous to Formula 9.4.1.

6. Apply Algorithm 9.4.1 with $T = 20$ to the qualities $35, 35, 10, 35, 35, 15, 12, 30, 8, 5$. Where is the read cut, and why does the isolated Q$10$ at position $3$ survive?

   **Answer** From the end: $T - q$ gives $15, 12, -10, 8, 5, -15, -15, 10, \dots$; the running sum is $15, 27, 17, 25, 30, 15, 0, 10, -5$. It becomes negative at position $2$ (after adding $-15$ for position $2$: $10 - 15 = -5$), so the scan stops. The maximum, $30$, is reached after position $6$ (Q$15$), so positions $6$–$10$ are removed and $1$–$5$ kept. The Q$10$ at position $3$ lies inside a region whose sum is dominated by the good bases at positions $1$, $2$, $4$ and $5$; cutting there would discard good bases to remove one poor one.

7. A library gave $5\times10^7$ read pairs with $20\,\%$ duplicates. Estimate its complexity and the number of distinct pairs that $2\times10^8$ reads would give. Would you sequence deeper or make a new library, if the goal is $1.5\times10^8$ distinct pairs?

   **Answer** $D = 4\times10^7$. Solving $C(1 - \mathrm{e}^{-5\times10^7/C}) = 4\times10^7$ numerically gives $C = 1.08\times10^8$ (at $C = 10^8$, $10^8(1 - \mathrm{e}^{-0.5}) = 3.93\times10^7$, slightly too few). With $2\times10^8$ reads, $D = 1.08\times10^8(1 - \mathrm{e}^{-1.86}) = 9.1\times10^7$, $55\,\%$ duplicates. Since $D$ can never exceed $C \approx 1.1\times10^8$, the goal of $1.5\times10^8$ distinct pairs is unreachable with this library; a new library from more input DNA, or with fewer PCR cycles, is needed.

8. In a $k$-mer spectrum ($k = 21$) of $150$-nt reads, the homozygous peak is at $40$ and the number of $k$-mer instances outside the error peak is $1.2\times10^{11}$. Estimate the base coverage and the haploid genome size.

   **Answer** The homozygous peak is the diploid $k$-mer coverage $2\lambda = 40$, so by Formula 9.5.1 the base coverage is $c = 40 \times 150/130 = 46\times$. The haploid genome size is $1.2\times10^{11}/40 = 3.0\times10^9$ bases, a human-sized genome.

9. Why does a spectrum with only one large peak indicate either a homozygous (inbred) genome or very low heterozygosity, and how would a triploid genome appear?

   **Answer** In Formula 9.5.2 the heterozygous peak at $\lambda$ has weight $2[1 - (1 - r)^k] \approx 2kr$ relative to the homozygous peak at $2\lambda$; when $r \to 0$ it vanishes and only the peak at the full coverage remains (inbred lines, haploid organisms, or CHM13). In a triploid, a $k$-mer can be present on one, two or three of the haplotypes, so peaks appear at $\lambda$, $2\lambda$ and $3\lambda$ (the per-haplotype coverage and its multiples), with relative heights depending on the pattern of differences among the three; the positions of the peaks, at ratios $1:2:3$, reveal the ploidy (GenomeScope 2 fits such models, and Smudgeplot uses pairs of $k$-mers to the same end).

10. (Design) You are planning to sequence HG002 to call germline variants, and also to obtain its complete diploid assembly. Choose platforms, depths and quality-control steps for each goal, and say what you would check in the data before analysis.

    **Answer** For variant calling: $2\times150$ paired-end short reads at $30$–$40\times$ (about $3.5$–$4.5\times10^8$ pairs), PCR-free library to avoid duplicates and GC bias; QC by FastQC/MultiQC (quality by cycle, adapter content, GC), duplicate rate and insert size after mapping, and concordance with the Genome in a Bottle benchmark as a check of the whole pipeline. For the assembly: PacBio HiFi at about $30$–$40\times$ (accurate long reads for contigs), ultra-long nanopore reads (over $100$ kb, $\ge 20\times$) to span centromeres and segmental duplications, and Hi-C or parental short reads (HG003, HG004) to phase the haplotypes ([7.8.11](/7.8.11)); QC by the read-length distribution and HiFi quality, and a $k$-mer spectrum of the short reads, which should show the expected human size, about $0.1\,\%$ heterozygosity and no contaminant peak. In both cases check the checksums of the files and the sample identity (for example, the sex chromosomes and known genotypes) before analysis.
