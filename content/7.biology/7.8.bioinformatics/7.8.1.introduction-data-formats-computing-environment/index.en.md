---
title: "Introduction: Data, Formats and the Computing Environment"
description: "What bioinformatics is and what this course covers: linear and semi-linear structures (sequences, intervals, alignments, base pairings, trees and sequence graphs). The growth of sequence data. Sequences as strings and IUPAC codes. The file formats of the field (FASTA and its index, BED, GFF3/GTF, SAM/BAM/CRAM, VCF, Newick, mmCIF) and their coordinate systems, zero-based half-open versus one-based closed, with conversions and the representation of indels. Block compression (BGZF) and the binning index used by tabix and BAM. The computing environment: shell idioms, Python, software environments, containers, clusters and workflow managers. Reproducibility, checksums and the FAIR principles."
---

Bioinformatics studies biological questions through the data of molecular biology, above all the sequences of DNA, RNA and protein, by means of algorithms, statistical models and software. This chapter sets out what the course is about and prepares the ground that every later chapter stands on: what the data look like, how they are written in files, how positions on a genome are counted, and the computing environment in which analyses are run. Two kinds of tools recur throughout and are worth distinguishing at the start: an **algorithm** is a procedure that computes a well-defined answer (the best-scoring alignment of two sequences, every occurrence of a word in a genome), whereas a *model* states how the data are thought to arise (substitutions along a tree, errors in a sequencing read), so that the answer is an estimate with an uncertainty. Most methods of the field combine the two: a model defines what is optimal, and an algorithm, often **dynamic programming**, finds it.

The course follows a small number of examples from chapter to chapter. The lactase persistence variant rs4988235 ($-13910\mathrm{C{>}T}$ upstream of *LCT*, inside an intron of *MCM6*), whose history under selection was told in [7.4.23](/7.4.23), is looked up in databases (7.8.2), aligned and searched (7.8.3–7.8.4), seen in reads (7.8.10), called and annotated (7.8.12) and compared between populations (7.8.13). The genome of one person, the public reference sample HG002 of the Genome in a Bottle consortium, carries the analysis from raw reads (7.8.9) to variants. The genome of SARS-CoV-2 is retrieved from its database record, aligned, placed on a tree and followed in wastewater (7.8.2, 7.8.5, 7.8.6, 7.8.14). The diagnosis of a rare disease, NGLY1 deficiency, found by exome sequencing in 2012, shows how these pieces serve a patient (7.8.12). The statistics behind many methods are those of [3.1](/3.1), [3.2](/3.2) and [biostatistics](/7.7); the algorithms and data structures are those of [4.3](/4.3); the analysis of omics data and of biological networks belongs to [systems biology](/7.9).

## 1.1. What Bioinformatics Is

### 1.1.1. Definition and Kinds of Questions

**Definition 1.1.1 (Bioinformatics)** **Bioinformatics** is the science of acquiring, storing, retrieving, analyzing and interpreting biological data, chiefly the sequences, structures and measured activities of nucleic acids and proteins, by computational and statistical methods, with the aim of answering biological questions.

The neighboring term *computational biology* is often used for the same field, with an emphasis on models and theory rather than data and tools; the distinction is not sharp. The questions take a few recurring forms:

| Form | Example | Typical method | Chapter |
|---|---|---|---|
| Comparison | Is this protein related to one of known function? | alignment, database search | 7.8.3–7.8.5 |
| History | How are SARS-CoV-2 lineages related? | phylogenetic inference | 7.8.6 |
| Annotation | Where are the genes and regulatory sites in a new genome? | probabilistic sequence models | 7.8.7–7.8.8, 7.8.11 |
| Reconstruction | What is the genome of this person, or of a new species? | read mapping, assembly | 7.8.9–7.8.11 |
| Variation | Which differences from the reference does a person carry, and which matter? | variant calling, annotation | 7.8.12–7.8.13 |
| Prediction | What structure does this sequence fold into; what does a mutation do? | dynamic programming, deep learning | 7.8.15–7.8.17 |

Research in the field is both *hypothesis-driven*, testing a specific idea with data collected for the purpose, and *data-driven*, mining large public data sets collected for other purposes. The second mode is characteristic: most sequences analyzed in a typical study were produced by someone else and deposited in a public database ([7.8.2](/7.8.2)).

### 1.1.2. The Growth of the Data

The first human genome sequence (2001) cost about $10^8$ US dollars and took a decade. With massively parallel short-read sequencing ([7.2.6](/7.2.6#sec-6.7.2)) the cost of a human genome at $30\times$ fell to about $10^3$ dollars by 2015 and to a few hundred dollars in the 2020s. Over 2001–2022 the cost fell by a factor of about $2\times10^5$, that is, $\log_2(2\times10^5) \approx 17.6$ halvings in $21$ years, one halving every $1.2$ years on average and every few months in 2008–2011. The cost of computing, by Moore's law, halved about every two years. Sequencing has therefore become cheap relative to the storage and analysis of its output, and public archives grew accordingly: the NCBI Sequence Read Archive held about $90\,\mathrm{PB}$ of raw data in 2024.

![The cost of sequencing one human genome, 2001–2024, on a logarithmic scale (rounded values after the NHGRI Genome Sequencing Program cost table and vendor list prices for the most recent point), compared with a cost that halves every two years from the 2001 value (Moore's law). The steep fall after 2007 marks the arrival of massively parallel sequencing; the dashed arrow marks the factor of about 600 by which sequencing had outpaced computing by 2015](./plots/sequencing-cost.py)

**Formula 1.1.1 (Halving Time)** If a cost falls from $C_0$ to $C_1$ in time $t$ with a constant rate, its halving time is

$$
t_{1/2} = \frac{t\ln 2}{\ln(C_0/C_1)}.
$$

**Example 1.1.1** From $10^8$ dollars (2001) to $1.5\times10^3$ dollars (2015), $t_{1/2} = 14 \times 0.693/\ln(6.7\times10^4) = 9.70/11.1 \approx 0.87$ years. At Moore's rate the cost in 2015 would have been $10^8 \times 2^{-7} \approx 7.8\times10^5$ dollars, about $500$ times the actual figure.

### 1.1.3. Milestones

| Year | Event |
|---|---|
| 1965 | Margaret Dayhoff's *Atlas of Protein Sequence and Structure*, the first sequence collection |
| 1970 | Needleman–Wunsch global alignment by dynamic programming |
| 1977 | Sanger sequencing; the first DNA genome ($\varphi$X174, 5386 nt) |
| 1978 | Dayhoff's PAM substitution matrices |
| 1981 | Smith–Waterman local alignment |
| 1982 | GenBank founded; with the European (EMBL) and Japanese (DDBJ) archives it later formed the International Nucleotide Sequence Database Collaboration |
| 1990 | BLAST |
| 1995 | first genome of a free-living organism (*Haemophilus influenzae*, by whole-genome shotgun) |
| 2001–2004 | draft and finished human genome |
| 2005–2008 | massively parallel short-read sequencing |
| 2010–2011 | single-molecule real-time sequencing; nanopore sequencing (2014) |
| 2020–2021 | AlphaFold2 predicts protein structures at near-experimental accuracy |
| 2022–2023 | the complete telomere-to-telomere human genome; the first human pangenome reference |

## 1.2. Linear and Semi-Linear Structures

The objects of this course are *linear* (a sequence is a string read in one direction) or *semi-linear*: a sequence carries additional structure that is still organized along it or derived from a few sequences. Six kinds recur:

| Structure | What it adds to a sequence | Chapter |
|---|---|---|
| Annotated sequence | intervals with labels (genes, **exons**, binding sites) | 7.8.1–7.8.2, 7.8.7–7.8.8 |
| Alignment | a correspondence between positions of two or more sequences | 7.8.3–7.8.5, 7.8.10 |
| Nested pairing | a set of non-crossing pairs of positions (RNA **secondary structure**) | 7.8.16 |
| Tree | the history that generated several sequences | 7.8.6 |
| Sequence graph | overlaps between reads (assembly graphs) or alternative paths through a genome (**pangenome** graphs) | 7.8.11 |
| Profile | a position-by-position distribution over residues (motifs, protein families) | 7.8.5, 7.8.8 |

What these have in common is that the important relations are local along a sequence or are determined by a small number of sequences, so that algorithms can sweep along the sequence (dynamic programming, **hidden Markov models**, string indexes). General networks of interacting molecules, whose relations have no such order, are treated in [systems biology](/7.9) and their mathematics in [1.4.7](/1.4.7).

![Six kinds of semi-linear structure on a DNA or RNA sequence. A: an annotated sequence, with labeled intervals (a gene with two exons, a binding site). B: a pairwise alignment, a correspondence between positions with one mismatch and one gap. C: an RNA secondary structure drawn as an arc diagram; arcs are nested and never cross. D: a rooted tree relating four sequences. E: a de Bruijn graph of the 3-mers of a short sequence, whose path spells it. F: a profile, a distribution over bases at each position, drawn as a sequence logo](./plots/semilinear-structures.py)

## 1.3. Sequences as Strings

A DNA sequence is a string over the alphabet $\{\mathrm{A}, \mathrm{C}, \mathrm{G}, \mathrm{T}\}$, an RNA sequence over $\{\mathrm{A}, \mathrm{C}, \mathrm{G}, \mathrm{U}\}$ and a protein sequence over the twenty amino-acid letters. Ambiguity is written with the IUPAC codes: $\mathrm{R} = \{\mathrm{A}, \mathrm{G}\}$ (purine), $\mathrm{Y} = \{\mathrm{C}, \mathrm{T}\}$ (pyrimidine), $\mathrm{S} = \{\mathrm{C}, \mathrm{G}\}$, $\mathrm{W} = \{\mathrm{A}, \mathrm{T}\}$, $\mathrm{K} = \{\mathrm{G}, \mathrm{T}\}$, $\mathrm{M} = \{\mathrm{A}, \mathrm{C}\}$, $\mathrm{B}$, $\mathrm{D}$, $\mathrm{H}$, $\mathrm{V}$ for "not A", "not C", "not G", "not T" respectively, and $\mathrm{N}$ for any base. In reference genomes, runs of $\mathrm{N}$ mark gaps of unknown sequence, and lower-case letters mark repeats that have been *soft-masked*.

**Definition 1.3.1 (Reverse Complement)** For a DNA string $s = s_1 s_2 \cdots s_n$, the **reverse complement** is $\bar s = \bar s_n \bar s_{n-1} \cdots \bar s_1$, where $\bar{\mathrm{A}} = \mathrm{T}$, $\bar{\mathrm{C}} = \mathrm{G}$, $\bar{\mathrm{G}} = \mathrm{C}$, $\bar{\mathrm{T}} = \mathrm{A}$ (and $\bar{\mathrm{R}} = \mathrm{Y}$, $\bar{\mathrm{N}} = \mathrm{N}$, and so on). It is the sequence of the opposite strand read in its own $5' \to 3'$ direction.

A reference genome stores one strand, the *forward* or *plus* strand of each chromosome; a gene on the minus strand is transcribed from the reverse complement. Both *LCT* and *MCM6* lie on the minus strand of chromosome 2, which is why rs4988235, named $-13910\mathrm{C{>}T}$ in the orientation of *LCT*, appears as G>A in genome coordinates and in databases that report alleles on the forward strand.

**Example 1.3.1** The reverse complement of $\mathrm{ATGCGTTA}$ is $\mathrm{TAACGCAT}$. Its GC content, the fraction of G and C, is $3/8 = 37.5\%$, the same on both strands. A $k$-mer and its reverse complement come from the same double-stranded site, so programs that count $k$-mers in reads of unknown strand count the *canonical* $k$-mer, the lexicographically smaller of the two ([7.8.9](/7.8.9#sec-9.5)).

## 1.4. File Formats

Bioinformatics exchanges data mostly as plain-text files, often compressed, with one record per line or per small group of lines. Text formats can be read by people and processed with the standard Unix tools; their binary counterparts (BAM, BCF) are smaller and faster. The formats below are the ones used in this course.

### 1.4.1. Sequences: FASTA and Its Index

**Definition 1.4.1 (FASTA Format)** The **FASTA format** stores sequences as records, each consisting of a header line beginning with `>`, whose first word is the sequence identifier and the rest a free description, followed by one or more lines of sequence in IUPAC letters, usually wrapped at 60 to 80 characters.

```text
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC
```

To read a region of a 3-Gb genome without scanning the whole file, `samtools faidx` writes an index, `genome.fa.fai`, with one line per sequence: its name, length, the byte offset of its first base, the number of bases per line and the number of bytes per line (bases plus the newline). Every line except the last of a record must have the same length.

**Formula 1.4.1 (FASTA Offset)** In a record whose first base is at byte $O$, with $b$ bases and $w$ bytes per line, the base at zero-based position $p$ is at byte

$$
O + \lfloor p/b \rfloor\, w + (p \bmod b).
$$

**Example 1.4.1** In a file whose first record is chromosome 2, with header `>chr2` ($6$ bytes including the newline, so $O = 6$) and $60$ bases per line ($b = 60$, $w = 61$), the base at one-based position $135\,851\,076$, the site of rs4988235, has zero-based position $p = 135\,851\,075 = 2\,264\,184 \times 60 + 35$ and lies at byte $6 + 2\,264\,184 \times 61 + 35 = 138\,115\,265$. Reading one base costs one seek, $O(1)$ time, whatever the size of the file.

### 1.4.2. Intervals and Annotations: BED and GFF

**Definition 1.4.2 (BED Format)** The **BED format** (Browser Extensible Data) describes genomic intervals, one per line, by tab-separated fields: chromosome, start and end in zero-based half-open coordinates (Definition 1.4.4), and optionally a name, a score, a strand and further fields for display and for blocks (exons).

```text
chr2	135851075	135851076	rs4988235	0	-
```

**Definition 1.4.3 (GFF Format)** The **GFF format** (General Feature Format, version 3, GFF3) describes features of a sequence in nine tab-separated columns: sequence identifier, source, feature type (a term of the Sequence Ontology such as `gene`, `mRNA`, `exon`, `CDS`), start and end in one-based closed coordinates, score, strand, phase (for coding segments, the number of bases to skip to reach the next codon: 0, 1 or 2) and attributes as `key=value` pairs, among them `ID` and `Parent`, which link exons to transcripts and transcripts to genes.

GTF (GFF2 with fixed attributes `gene_id` and `transcript_id`) is the older dialect still used by RNA-seq tools; GENCODE and Ensembl distribute both. Because features refer to their parents, a GFF3 file describes a forest: genes with transcripts, transcripts with exons and coding segments. The part of the SARS-CoV-2 annotation for the spike gene reads

```text
NC_045512.2	RefSeq	gene	21563	25384	.	+	.	ID=gene-GU280_gp02;Name=S
NC_045512.2	RefSeq	CDS	21563	25384	.	+	0	ID=cds-YP_009724390.1;Parent=gene-GU280_gp02;product=surface glycoprotein
```

The interval contains $25384 - 21563 + 1 = 3822$ nucleotides, $1274$ codons: $1273$ amino acids and a stop codon.

### 1.4.3. Alignments, Variants, Trees and Structures

| Format | Content | Coordinates | Chapter |
|---|---|---|---|
| FASTQ | reads with per-base quality scores | (none) | [7.8.9](/7.8.9) |
| SAM / BAM / CRAM | reads aligned to a reference: position, mapping quality, CIGAR string of matches and gaps; BAM is compressed binary, CRAM stores differences from the reference | SAM text one-based; BAM binary zero-based | [7.8.10](/7.8.10) |
| VCF / BCF | variant sites with reference and alternative alleles, genotypes and likelihoods per sample | one-based | [7.8.12](/7.8.12) |
| Newick | a tree as nested parentheses with branch lengths: `((A:0.1,B:0.2):0.05,C:0.3);` | (none) | [7.8.6](/7.8.6) |
| PDB / mmCIF | atomic coordinates of macromolecular structures; mmCIF replaced the fixed-column PDB format as the archive standard in 2014 | residue numbers | [7.8.17](/7.8.17) |

### 1.4.4. Coordinate Systems

Two conventions for numbering positions are in use, and confusing them is the most common error in genomic data analysis.

**Definition 1.4.4 (Zero-Based Half-Open and One-Based Closed Coordinates)** In **zero-based half-open coordinates** the positions of a sequence are numbered $0, 1, 2, \dots$ and an interval is written $[s, e)$, containing the positions $s, s + 1, \dots, e - 1$. In **one-based closed coordinates** the positions are numbered $1, 2, 3, \dots$ and an interval is written $[s', e']$, containing $s', \dots, e'$.

**Formula 1.4.2 (Conversion)** The same set of bases is written $[s, e)$ in zero-based half-open and $[s + 1, e]$ in one-based closed coordinates: the start increases by one and the end is unchanged. The length is $e - s$ in the first system and $e' - s' + 1$ in the second.

BED, BAM (internally), the UCSC databases and most programming libraries (Python slices `seq[s:e]`) use zero-based half-open coordinates; GFF, SAM text, VCF, HGVS names, the UCSC and Ensembl browser displays and most biologists use one-based closed coordinates. The half-open system has arithmetic advantages: the length is $e - s$, adjacent intervals $[s, m)$ and $[m, e)$ share an endpoint without overlapping, and an empty interval, the position *between* two bases where an insertion occurs, is $[s, s)$. In the closed system an insertion has no interval of its own, which is why VCF and HGVS represent it relative to a neighboring base.

**Example 1.4.2 (One Site in Five Notations)** rs4988235 lies at one-based position $135\,851\,076$ of chromosome 2 in GRCh38. It is written

| System | Notation |
|---|---|
| BED (zero-based half-open) | `chr2  135851075  135851076` |
| VCF (one-based) | `2  135851076  rs4988235  G  A` |
| HGVS, genomic | `NC_000002.12:g.135851076G>A` |
| HGVS, relative to the *LCT* transcript | `c.-13910C>T` (upstream of the start codon, minus strand) |
| UCSC browser position | `chr2:135,851,076` |

:::

In VCF, a deletion of the bases $\mathrm{CT}$ after a $\mathrm{G}$ at position $1000$ is written `POS=1000 REF=GCT ALT=G`: the record starts at the base preceding the event (the *anchor* or *padding* base), so that both alleles are non-empty. An insertion of $\mathrm{AA}$ after the same base is `POS=1000 REF=G ALT=GAA`. Inside a repeat, the same deletion can be placed at several positions with identical resulting sequences; VCF tools *normalize* such variants by shifting them as far left as possible and removing shared bases (`bcftools norm`), so that the same event always has the same record.

![The same interval and the same variants in the two coordinate systems. Top: a reference sequence with zero-based positions (between bases, as fence posts) and one-based positions (on bases); the highlighted interval of four bases is start 3, end 7 (half-open) in BED and 4–7 in GFF and VCF, and its length is 7 − 3 = 7 − 4 + 1 = 4. Bottom: a substitution, a deletion and an insertion as VCF records, the latter two anchored on the preceding base; in half-open coordinates the deleted bases are start 8, end 10 and the insertion point is the empty interval at 6](./plots/coordinate-systems.py)

### 1.4.5. Compression and Indexing

Large text files are compressed with BGZF (blocked gzip), a variant of gzip that compresses the file in independent blocks of at most $64\,\mathrm{KiB}$ of input; each block is a valid gzip member, so the file can be decompressed by `gzip`, but a reader can also start at the beginning of any block. A position in the file is a *virtual offset*: the byte offset of the compressed block times $2^{16}$ plus the offset within the uncompressed block. `bgzip` writes such files; `tabix` and the BAM and BCF indexes record, for each region, the virtual offsets where its records begin. The indexes use a hierarchy of bins.

**Algorithm 1.4.1 (Hierarchical Binning)** The genome is divided into bins at six levels, of sizes $2^{29}, 2^{26}, 2^{23}, 2^{20}, 2^{17}$ and $2^{14}$ bases ($512\,\mathrm{Mb}$ down to $16\,\mathrm{kb}$); level $\ell$ has $8^\ell$ bins, numbered consecutively from $(8^\ell - 1)/7$, so there are $37\,449$ bins in all.

1. To index a record covering the zero-based half-open interval $[s, e)$: assign it to the smallest bin that contains it entirely. With $e' = e - 1$ (the last base of the record), for the levels $\ell = 5, 4, \dots, 1$ (shifts $k = 14, 17, 20, 23, 26$): if $\lfloor s/2^k\rfloor = \lfloor e'/2^k\rfloor$, the bin is $(8^\ell - 1)/7 + \lfloor s/2^k\rfloor$; otherwise go up a level. A record that fits no smaller bin goes into bin $0$.
2. To query a region $[a, b)$: at each level, list the bins whose span intersects $[a, b)$ (at most one or a few per level for a short region), read the records stored in them, and keep those that overlap $[a, b)$.

A separate *linear index* stores, for each $16$-kb window, the smallest file offset of any record overlapping it, which lets the reader skip records that end before the region.

The binning scheme is a simplified **interval tree**: every interval is stored in exactly one node, and a query visits one root-to-leaf path plus the bins that the query itself spans. For a short query, at most six bins (one per level) are examined, and the time is proportional to the number of records in them rather than to the size of the file. Bin $0$ holds the few records longer than $64\,\mathrm{Mb}$, so even they are found.

**Example 1.4.3** For rs4988235, $[s, e) = [135\,851\,075, 135\,851\,076)$ and $\lfloor s/2^{14}\rfloor = 8291$, so the record lies in the $16$-kb bin $4681 + 8291 = 12\,972$. A query for the same base examines bins $0, 3, 25, 202, 1621$ and $12\,972$, one per level. A $50$-kb record covering $[135\,830\,000, 135\,880\,000)$ crosses a $16$-kb boundary but not a $128$-kb one, and is stored in bin $585 + \lfloor 135\,830\,000/2^{17}\rfloor = 585 + 1036 = 1621$.

:::

![Hierarchical binning for indexing genomic intervals. Bins at successive levels are 8 times smaller (only the top three of the six levels drawn); each record is stored in the smallest bin that contains it, so a short record crossing the boundary at 3/8 of the genome ends up in bin 0. A query (dashed line) examines one bin per level (shaded), the bins on the path from the root to the finest bin containing the queried position, and tests only the records stored there for overlap](./plots/binning-index.py)

```bash
bgzip variants.vcf                      # writes variants.vcf.gz (BGZF)
tabix -p vcf variants.vcf.gz            # writes the index variants.vcf.gz.tbi
tabix variants.vcf.gz 2:135851076-135851076
samtools faidx GRCh38.fa chr2:135851026-135851126   # 101 bases around the site
```

## 1.5. The Computing Environment

The tools of the field run mostly on Linux servers and clusters, from the command line. The operating-system background is in [4.11](/4.11): the shell, pipes and text processing in [4.11.10](/4.11.10), containers in [4.11.9](/4.11.9), and clusters, batch jobs and workflow managers in [4.11.11](/4.11.11); scientific Python in [4.4](/4.4). This section collects only what is specific to sequence data.

### 1.5.1. Stream Processing of Text Formats

Line-oriented formats are processed in pipelines that read a file once and keep little in memory:

```bash
# Number of sequences and total length in a FASTA file
grep -c '>' genome.fa
grep -v '>' genome.fa | tr -d '\n' | wc -c

# Sequence lengths from the index (name and length columns)
cut -f1,2 genome.fa.fai | sort -k2,2nr | head

# Number of reads in a gzipped FASTQ file (4 lines per record)
echo $(( $(zcat reads.fq.gz | wc -l) / 4 ))

# Total length of the intervals in a BED file (half-open: end - start)
awk '{s += $3 - $2} END {print s}' targets.bed

# Feature types in a GFF3 file and their counts
grep -v '^#' annotation.gff3 | cut -f3 | sort | uniq -c | sort -k1,1nr

# Sort a BED file by chromosome, then numerically by start, and merge overlapping intervals
sort -k1,1 -k2,2n peaks.bed | bedtools merge -i - > merged.bed
```

Two habits avoid many errors. Genomic files are sorted by chromosome and then numerically by position (`sort -k1,1 -k2,2n`), and tools that combine files (`bedtools`, `bcftools`) require the same sort order and the same chromosome names in all inputs: `chr2` (UCSC) and `2` (Ensembl, NCBI) denote the same chromosome but do not match as strings. And files are best inspected with `less -S` and `head` rather than opened in a spreadsheet: Excel silently converts gene symbols such as SEPT2 and MARCH1 to dates, an error found in about a fifth of the papers with gene lists in Excel supplementary files surveyed in 2016, which led the HGNC to rename these genes (SEPTIN2, MARCHF1) in 2020.

### 1.5.2. Programming Languages

Python is the general language of the field: Biopython reads and writes sequence formats and accesses databases, pysam wraps the samtools and htslib libraries for SAM/BAM/CRAM, VCF and tabix files, and NumPy and pandas handle the numerical and tabular parts ([4.4](/4.4)). R with the Bioconductor project is the main environment for statistical analysis of genomic data (differential expression, [7.9](/7.9)). Performance-critical tools (aligners, assemblers, variant callers) are written in C, C++ or Rust and called from the shell or from Python.

```python
# GC content in windows along a sequence, and the reverse complement
from Bio import SeqIO

rec = next(SeqIO.parse("NC_045512.2.fasta", "fasta"))
seq = str(rec.seq).upper()
print(rec.id, len(seq))                      # NC_045512.2 29903
window = 500
gc = [(s, (seq[s:s + window].count("G") + seq[s:s + window].count("C")) / window)
      for s in range(0, len(seq) - window + 1, window)]
spike = rec.seq[21562:25384]                 # BED-style [21562, 25384): the S gene
print(len(spike), spike.translate()[:10])    # 3822 MFVFLVLLPL
```

The slice `seq[21562:25384]` is the one-based interval $21563$–$25384$ of the annotation (Formula 1.4.2), and its translation begins with the signal peptide of the spike protein, MFVFLVLLPL.

### 1.5.3. Software Environments, Containers and Clusters

A bioinformatics analysis typically uses tens of programs, each in a specific version. They are installed with a **package manager**: conda (or its faster implementations mamba and pixi) with the Bioconda channel, which packages over ten thousand bioinformatics tools, into isolated environments whose exact contents are recorded in a **lock file**. Alternatively a program and all its dependencies are packaged as a container image (Docker on a workstation, Apptainer on a cluster; [4.11.9](/4.11.9)), which also fixes the operating-system libraries; the BioContainers project builds an image for every Bioconda package. Large jobs run as batch jobs on a cluster under a workload manager such as Slurm ([4.11.11](/4.11.11#sec-11.3)).

### 1.5.4. Workflows

An analysis such as "trim the reads, align them, call variants" is a chain of programs whose outputs are the inputs of the next. A **workflow management system** ([4.11.11](/4.11.11#sec-11.6)) describes the steps by their inputs and outputs, derives the **directed acyclic graph** of tasks, runs them in parallel where possible, reruns only what is out of date, and gives each step its own software environment. Snakemake and Nextflow are the two most used in bioinformatics; the nf-core project maintains reviewed Nextflow pipelines for common analyses.

```python
# Snakefile: quality control, alignment and variant calling for one sample
SAMPLES = ["HG002"]
REF = "ref/GRCh38.fa"

rule all:
    input: expand("vcf/{s}.vcf.gz", s=SAMPLES)

rule trim:
    input: r1="fastq/{s}_R1.fq.gz", r2="fastq/{s}_R2.fq.gz"
    output: r1="trim/{s}_R1.fq.gz", r2="trim/{s}_R2.fq.gz", html="qc/{s}.fastp.html"
    conda: "envs/fastp.yaml"
    threads: 8
    shell: "fastp -i {input.r1} -I {input.r2} -o {output.r1} -O {output.r2} -h {output.html} -w {threads}"

rule align:
    input: r1="trim/{s}_R1.fq.gz", r2="trim/{s}_R2.fq.gz", ref=REF
    output: "bam/{s}.bam"
    conda: "envs/align.yaml"
    threads: 16
    shell: "bwa-mem2 mem -t {threads} -R '@RG\\tID:{wildcards.s}\\tSM:{wildcards.s}' {input.ref} {input.r1} {input.r2}"
           " | samtools sort -@ 4 -o {output} - && samtools index {output}"

rule call:
    input: bam="bam/{s}.bam", ref=REF
    output: "vcf/{s}.vcf.gz"
    conda: "envs/bcftools.yaml"
    shell: "bcftools mpileup -f {input.ref} {input.bam} | bcftools call -mv -Oz -o {output} && tabix -p vcf {output}"
```

## 1.6. Reproducibility and Data Management

A computational result is reproducible if another person, given the same data, can obtain it again. This requires recording, for every result, the input files, the exact versions of the reference genome and annotation (for example GRCh38 with GENCODE release 47), the software versions and parameters, and the code. The usual practice is code under a **version control system** ([4.14](/4.14)), environments pinned in lock files or container images identified by digest, analyses run by a workflow manager that logs every command, and random seeds fixed.

Large data files are not kept under version control; their integrity is checked with a cryptographic **hash function**, usually MD5 or SHA-256. Sequencing providers and archives publish the checksum of every file, and `md5sum -c` compares the checksums of downloaded or copied files with the published list ([4.11.11](/4.11.11#sec-11.5)):

```bash
md5sum HG002_R1.fq.gz HG002_R2.fq.gz > checksums.md5    # at the source
md5sum -c checksums.md5                                  # after copying: "HG002_R1.fq.gz: OK"
```

**Definition 1.6.1 (FAIR Principles)** The **FAIR principles** (Wilkinson et al., 2016) state that scientific data should be *findable* (with persistent identifiers and rich metadata in a searchable resource), *accessible* (retrievable by their identifiers through a standard protocol, with the metadata available even if the data are not), *interoperable* (in formal, shared formats and vocabularies) and *reusable* (with clear licenses, provenance and community standards).

Public archives implement these principles: a sequencing study deposited in the Sequence Read Archive receives accession numbers for the project, the samples, the experiments and the runs, with metadata in controlled vocabularies ([7.8.2](/7.8.2)). Human data add a constraint: genotypes identify a person and their relatives, so individual-level human sequence data are held in controlled-access archives (dbGaP, EGA, the human section of GSA) and released only to approved researchers, while summary statistics are usually public.

## Summary

| Topic | Key points |
|---|---|
| The field | Bioinformatics (Definition 1.1.1) combines models of how data arise with algorithms that compute optimal answers; questions of comparison, history, annotation, reconstruction, variation and prediction |
| Data growth | sequencing cost halved about every $1.2$ years on average since 2001 (Formula 1.1.1), far faster than computing |
| Scope | linear and semi-linear structures: annotated sequences, alignments, nested pairings, trees, sequence graphs, profiles; networks belong to 7.9 |
| Strings | IUPAC codes, soft-masking, reverse complement (Definition 1.3.1); reference genomes store the plus strand |
| Formats | FASTA (Definition 1.4.1) with byte-offset index (Formula 1.4.1), BED (Definition 1.4.2), GFF3/GTF (Definition 1.4.3), FASTQ, SAM/BAM/CRAM, VCF, Newick, mmCIF |
| Coordinates | zero-based half-open $[s, e)$ versus one-based closed $[s + 1, e]$ (Definition 1.4.4, Formula 1.4.2); VCF anchors indels on the preceding base and normalizes left |
| Indexing | BGZF blocks with virtual offsets; hierarchical bins (Algorithm 1.4.1) find all records overlapping a region by examining about one bin per level |
| Environment | shell pipelines, Python (Biopython, pysam), conda/Bioconda, containers, Slurm, workflow managers (Snakemake, Nextflow) |
| Reproducibility | versions of references, software and parameters; checksums; FAIR principles (Definition 1.6.1); controlled access for human data |

## Questions

1. A gene annotation in GFF3 gives an exon as `chr7 117559590 117559700`. Write the same exon in BED, and give its length.

   **Answer** BED uses zero-based half-open coordinates, so the start decreases by one and the end stays (Formula 1.4.2): `chr7 117559589 117559700`. The length is $117\,559\,700 - 117\,559\,589 = 111$ bases, equal to $117\,559\,700 - 117\,559\,590 + 1$ in the closed system.

2. Why do the two coordinate systems both survive, instead of one replacing the other?

   **Answer** Each is natural for different users. One-based closed numbering matches how biologists count bases and how positions are cited in papers, clinical reports and HGVS names. Zero-based half-open intervals make computation simple: lengths are differences, adjacent intervals meet without overlap, insertion points are empty intervals, and they coincide with array indexing and slicing in C and Python. Formats designed for display and annotation (GFF, VCF) took the first, formats designed by programmers for storage and computation (BED, BAM) the second. The practical rule is to convert once, at input, and to know which convention every file uses.

3. A FASTA index line reads `chr1 248956422 6 60 61`. At which byte does the base at one-based position $1\,000\,001$ start?

   **Answer** Zero-based $p = 1\,000\,000 = 16\,666 \times 60 + 40$. By Formula 1.4.1 the byte is $6 + 16\,666 \times 61 + 40 = 1\,016\,672$.

4. Write a deletion of the two bases $\mathrm{TG}$ at one-based positions $201$–$202$ of a reference whose base $200$ is $\mathrm{A}$, as a VCF record, and the same event in BED.

   **Answer** VCF anchors on the preceding base: `POS=200 REF=ATG ALT=A`. In BED the deleted bases are $[200, 202)$, positions $200$ and $201$ in zero-based numbering, that is, one-based $201$ and $202$; length $2$.

5. The reference reads $\cdots\mathrm{GCACACACAT}\cdots$, with the $\mathrm{CA}$ repeat starting at one-based position $101$ (so the $\mathrm{G}$ is at $100$). A read lacks one copy of $\mathrm{CA}$. Give two VCF records that describe this read, and the normalized one.

   **Answer** The read is $\mathrm{GCACACAT}$: any one of the four $\mathrm{CA}$ (or $\mathrm{AC}$) units can be considered deleted. Deleting the first gives `POS=100 REF=GCA ALT=G`; deleting the last gives `POS=106 REF=ACA ALT=A` (the $\mathrm{A}$ at $106$ anchors the deletion of $\mathrm{CA}$ at $107$–$108$). Both produce the same sequence. Normalization shifts the deletion to the leftmost possible position, giving `POS=100 REF=GCA ALT=G`, so that two callers report the same record.

6. Using Algorithm 1.4.1, in which bin is a record covering the zero-based half-open interval $[16\,380, 16\,390)$ stored? Why is it not in bin $4681$?

   **Answer** $e' = 16\,389$. At the $16$-kb level, $\lfloor 16\,380/16\,384\rfloor = 0$ but $\lfloor 16\,389/16\,384\rfloor = 1$: the record crosses the boundary at $16\,384$, so it does not fit in bin $4681$ (the first $16$-kb bin) or $4682$. At the $128$-kb level both ends give $0$, so the record is stored in bin $585 + 0 = 585$. A query for any position in $[0, 131\,072)$ examines bin $585$, so it is still found.

7. (Design) A collaborator sends a table of variants with columns "chromosome, position, gene" but no information on the genome version or coordinate system. What would you check before using it?

   **Answer** First, the genome version: look up a few positions of known variants (for example a gene's well-known variant, or rs IDs if present) in GRCh37 and GRCh38; positions differ by up to megabases (rs4988235 is at $136\,608\,646$ in GRCh37 and $135\,851\,076$ in GRCh38). Second, the coordinate convention: compare the reference base at the given position with the reported allele, at both $p$ and $p + 1$; the convention under which the reference alleles match is the one used. Third, the strand: alleles may be reported on the gene's strand (C/T for rs4988235) rather than the forward strand (G/A). Fourth, chromosome naming (`chr2` or `2`) and, if it came from a spreadsheet, gene symbols converted to dates. Ask for the source file in a standard format such as VCF, which states the reference in its header.

8. Estimate the size of the raw data for one human genome sequenced to $30\times$ with $150$-nt reads, if gzipped FASTQ needs about $0.7$ bytes per base including the quality scores. How many reads are there?

   **Answer** Bases: $3.1\times10^9 \times 30 = 9.3\times10^{10}$. File size: about $6.5\times10^{10}$ bytes, $65\,\mathrm{GB}$. Reads: $9.3\times10^{10}/150 = 6.2\times10^8$ reads, $3.1\times10^8$ pairs. Aligned and stored as CRAM against the reference, with quality scores binned, the same data occupy a few times less.

9. Explain why a workflow manager reruns only some steps after a parameter of the variant caller is changed, and why this depends on declaring inputs and outputs.

   **Answer** The workflow manager builds a directed acyclic graph in which each task is connected to the tasks that produce its inputs. When the parameters or code of a task change (Snakemake tracks them as part of each job's metadata), that task and every task downstream of it in the graph are out of date; tasks upstream (trimming, alignment) are not, and their outputs are reused. The manager can only know these dependencies if every step declares its inputs and outputs; a step that reads or writes undeclared files breaks the graph, so a change may not trigger a needed rerun.

10. Why must individual human genomes be kept under controlled access, even after the names of the participants are removed?

    **Answer** A genome is itself an identifier: it matches a person's DNA, and through shared segments it also identifies relatives; combined with public genealogical databases, surnames and demographic information, de-identified genotypes can be re-identified, as several studies have shown. Genotypes also reveal health risks of the person and their family. Controlled access limits use to approved research under agreements, while aggregate data such as allele frequencies and summary statistics, which carry much less individual information, can be released openly.
