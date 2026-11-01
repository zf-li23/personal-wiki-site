---
title: "Beyond Gene Levels: Isoforms, Splicing, Translation and RNA Modification"
description: "What sequencing measures beyond the abundance of each gene: splicing events and the percent spliced in with its uncertainty and a replicate model for differential splicing, splicing in single cells, full-length isoforms and circular RNAs from long reads, ribosome profiling (P sites, translation efficiency, differential translation, the detection of translated ORFs, and a data-driven discovery about rocaglamide A), nascent transcription and RNA turnover from metabolic labeling, RNA modifications, RNA–protein crosslinking and structure probing, alternative polyadenylation, RNA editing and fusion transcripts."
---

A gene-level count, the subject of [7.9.2](/7.9.2), compresses the life of a transcript into one number. Between transcription and the finished protein, the RNA is spliced in one of several ways, cleaved and polyadenylated at one of several sites, chemically modified and edited, bound by proteins, translated at a rate set by its own sequence and finally degraded; each step is regulated ([7.2.16](/7.2.16)–[7.2.20](/7.2.20)), and each can be measured genome-wide by a variant of sequencing. This chapter treats these measurements as one family. In every case the experiment converts a molecular event into a feature of reads (a split read across a junction, the length and phase of a ribosome footprint, a T-to-C mismatch, a truncation at a crosslink), and the analysis turns counts of such features into a ratio with its uncertainty: the fraction of transcripts that include an exon (4.1–4.3), the number of ribosomes per mRNA (4.4), the fraction of molecules made in the last hours (4.5), the fraction of a site that is modified, bound or edited (4.6–4.7). The statistics are those of [biostatistics](/7.7) applied to ratios of counts; the molecular mechanisms are those of molecular biology, which we link rather than repeat; and the results add layers to the networks of the later chapters, because a regulator may act on splicing or translation without changing the level of any transcript.

## 4.1. Quantifying Alternative Splicing

### 4.1.1. Events and the Reads That Measure Them

About $95\,\%$ of human multi-exon genes produce more than one isoform by **alternative splicing** ([7.2.16](/7.2.16#sec-16.7)). Short reads rarely span a whole transcript, so the usual analysis does not estimate the abundance of each full isoform (the approach of [7.9.2](/7.9.2), which depends on the annotation and is uncertain when isoforms differ in a few exons) but decomposes the variation into local events, each a choice between two paths through a small part of the gene. Five classes cover most events (figure, panel A).

| Event | Choice | Reads supporting the longer (inclusion) form | Reads supporting the shorter form |
|---|---|---|---|
| Skipped exon (SE) | a cassette exon is included or skipped | junctions upstream exon–cassette and cassette–downstream exon; reads inside the cassette | the junction joining the flanking exons |
| Mutually exclusive exons (MXE) | exactly one of two exons is used | junctions to and from the first exon | junctions to and from the second |
| Alternative 5′ splice site (A5SS) | two donor sites in the upstream exon | the junction from the downstream donor; reads in the extension | the junction from the upstream donor |
| Alternative 3′ splice site (A3SS) | two acceptor sites in the downstream exon | the junction to the upstream acceptor; reads in the extension | the junction to the downstream acceptor |
| Retained intron (RI) | an intron is kept or removed | reads across the exon–intron boundaries and inside the intron | the exon–exon junction |

Alternative first and last exons, which follow from alternative promoters and polyadenylation sites, are usually treated with transcription start sites and 3′ ends (4.7.1). The key reads are *split* reads: a read whose two parts map to two exons, with the intron in between reported as a gap in the alignment by a splice-aware aligner ([7.8.10](/7.8.10)). A junction is called *annotated* if it joins sites of a known transcript and *novel* otherwise; methods based on intron clusters, such as LeafCutter (Li and colleagues, 2018), use only split reads, need no annotation, and represent complex events with more than two choices.

![The five basic classes of alternative splicing events and how reads measure them. A: skipped exon (SE), mutually exclusive exons (MXE), alternative 5′ splice site (A5SS), alternative 3′ splice site (A3SS) and retained intron (RI); constitutive exons in blue, alternative regions in orange, one form joined above and the other below. B: a sashimi plot of a skipped exon in two conditions: read coverage over the three exons, and arcs for the junctions labeled with the numbers of junction reads. The inclusion counts I (the two arcs through the middle exon) and the skipping count S (the long arc) give the percent spliced in by Formula 4.1.1, 0.78 in the control and 0.27 after treatment](./plots/splicing_events.py)

### 4.1.2. Percent Spliced In

**Definition 4.1.1 (Percent Spliced In)** For an alternative splicing event in a sample, the **percent spliced in** $\psi$ is the fraction of the transcripts that pass through the event and use its inclusion form:
$$
\psi = \frac{n_{\mathrm{inc}}}{n_{\mathrm{inc}} + n_{\mathrm{exc}}},
$$
where $n_{\mathrm{inc}}$ and $n_{\mathrm{exc}}$ are the numbers of molecules of the two forms. It is reported as a fraction in $[0, 1]$ or as a percentage; the difference between two conditions is $\Delta\psi$.

$\psi$ is a ratio within one gene, so it does not depend on the expression level of the gene, on the library size, or on a normalization between samples. Its estimate depends on how many reads each form can produce. A junction can be covered by a read of length $L$ only if the read overlaps each exon by at least an anchor of $a$ nucleotides, so a junction offers $L - 2a + 1$ start positions; the inclusion form of a skipped exon has two junctions and the skipping form one.

**Formula 4.1.1 (PSI from junction reads)** Let $I$ and $S$ be the numbers of reads on the inclusion and skipping junctions of an event, and $l_I$, $l_S$ the numbers of positions at which a read supports each form (*effective lengths*; for a skipped exon counted by junction reads, $l_S = L - 2a + 1$ and $l_I = 2l_S$). Then
$$
\hat\psi = \frac{I/l_I}{I/l_I + S/l_S}. \tag{4.1}
$$
If exon-body reads are counted as well, $l_I$ includes the positions inside the cassette exon.

**Example 4.1.1** In the control of panel B, $I = 45 + 39 = 84$ inclusion reads and $S = 12$ skipping reads with $L = 100$, $a = 8$, so $l_S = 85$, $l_I = 170$ and $\hat\psi = (84/170)/(84/170 + 12/85) = 0.78$; the naive ratio $I/(I + S) = 0.875$ overestimates $\psi$ because the inclusion form offers twice as many positions. After treatment, $I = 30$ and $S = 40$ give $\hat\psi = 0.27$.

How precise is $\hat\psi$? Each junction read is, given $\psi$, an independent trial whose probability of supporting inclusion is $p = \psi l_I/(\psi l_I + (1 - \psi)l_S)$, so $I$ given $I + S$ has a **binomial distribution**. With a uniform prior on $p$, the posterior of $p$ is the **beta distribution** $\mathrm{Beta}(I + 1, S + 1)$ ([3.7](/3.7)), and since the map $p \mapsto \psi = pl_S/(pl_S + (1 - p)l_I)$ is increasing, the quantiles of $p$ map to quantiles of $\psi$. For $I : S = 3 : 1$ the posterior $95\,\%$ interval of $\psi$ is $[0.25, 0.86]$ with $8$ junction reads, $[0.48, 0.71]$ with $80$ and $[0.56, 0.64]$ with $800$ (figure below, panel A). Most events in a typical library have tens of junction reads, so a single sample determines $\psi$ only to about $\pm 0.1$, and events with fewer than about $10$–$20$ reads are usually filtered out before testing.

### 4.1.3. Differential Splicing with Replicates

Pooling the reads of the replicates of each condition and comparing the two pooled proportions by a Fisher exact test ignores the variation of $\psi$ between biological replicates, which is often larger than the binomial sampling error: the situation of overdispersed counts in differential expression ([7.7.20](/7.7.20)), now for proportions. The replicate multivariate analysis of transcript splicing (rMATS; Shen and colleagues, 2014) puts the two sources of variation into a hierarchical model.

**Algorithm 4.1.1 (Replicate Model for Differential Splicing)** For one event, let $I_{kj}$ and $S_{kj}$ be the junction counts of replicate $j$ in group $k \in \{1, 2\}$.

1. Model: $\operatorname{logit}\psi_{kj} \sim \mathcal{N}(\mu_k, \sigma^2)$ independently, with group means $\mu_k$ and a variance $\sigma^2$ shared by the groups, and $I_{kj} \mid \psi_{kj} \sim \mathrm{Bin}\bigl(I_{kj} + S_{kj},\ p(\psi_{kj})\bigr)$ with $p(\psi) = \psi l_I/(\psi l_I + (1 - \psi)l_S)$.
2. Likelihood: integrate each replicate's binomial probability over the normal distribution of $\operatorname{logit}\psi_{kj}$ (numerically, by quadrature), and multiply over replicates.
3. Test: maximize the likelihood with $\mu_1$ and $\mu_2$ free and with $\mu_1 = \mu_2$; twice the difference of the maximized log-likelihoods is the statistic of a **likelihood ratio test**, compared with $\chi^2_1$. rMATS tests the composite null hypothesis $\lvert\psi_1 - \psi_2\rvert \le c$ for a user-chosen $c$ (by default almost $0$; $c = 0.05$ asks for a change of at least five percentage points).
4. Multiple testing: convert the p-values of all events to **false discovery rates** ([7.7.20](/7.7.20)) and report events with an FDR below a threshold and a $\lvert\Delta\psi\rvert$ above a minimum.

The cost is a few low-dimensional optimizations per event, linear in the number of events and replicates. rMATS reports the results twice, with junction counts only (JC) and with junction and exon-body counts (JCEC); the second has more reads but depends more on uniform coverage.

**Example 4.1.2** Panel B below shows three control and three treated replicates, each with about $96$ junction reads, whose estimates agree within their binomial intervals; the model gives $\Delta\psi = 0.47$ and a likelihood ratio of $13.3$, $p = 3\times10^{-4}$. In panel C the replicates of each condition scatter widely ($\psi$ from $0.45$ to $0.95$ in the controls). The estimated variance between replicates is large, and the likelihood ratio is only $3.4$ ($p = 0.07$), although the means differ by about as much. A Fisher test on the pooled counts reports $p \approx 10^{-21}$ for both data sets: it counts reads as if they were independent biological replicates, the error called pseudoreplication in single-cell analysis ([7.9.5](/7.9.5#sec-5.6)).

![How certain is a percent spliced in? A: the posterior distribution of PSI for one skipped exon with the same ratio of inclusion to skipping reads (I : S = 3 : 1, PSI = 0.60) at three depths (uniform prior on the probability that a junction read supports inclusion, transformed with the effective lengths for 100-nt reads and an 8-nt anchor). B, C: differential splicing with three replicates per condition in a model like that of rMATS (Algorithm 4.1.1): points, PSI of each replicate with its 95% interval; lines, fitted group means. In B the replicates agree and the likelihood ratio test is significant; in C they disagree and the evidence is weak, although a Fisher test on the pooled counts still reports a tiny p-value](./plots/psi_uncertainty.py)

Other tools differ in the unit of analysis and the model:

| Tool | Unit | Model | Note |
|---|---|---|---|
| rMATS | the five event classes | binomial with logit-normal replicate variation (Algorithm 4.1.1) | annotated and novel junctions; JC and JCEC |
| SUPPA2 | events from annotated transcripts | $\psi$ from transcript abundances (pseudo-alignment) | fast; depends on the annotation |
| LeafCutter | clusters of introns sharing splice sites | Dirichlet-multinomial generalized linear model | annotation-free; also used for splicing QTLs |
| MAJIQ | local splicing variations (all junctions from one exon) | Bayesian, posterior of $\Delta\psi$ | complex events |

Results are visualized as a *sashimi plot* (as in panel B of the first figure: coverage tracks with arcs for junctions, available in genome browsers such as IGV and from `rmats2sashimiplot`) and confirmed for individual events by RT-PCR with primers in the flanking exons, which separates the two products by size.

```bash
# Differential splicing of treated (b1) against control (b2) samples from aligned reads
# (b1.txt, b2.txt: comma-separated BAM files of the replicates; paired-end 150-nt reads)
rmats.py --b1 b1.txt --b2 b2.txt --gtf genes.gtf -t paired --readLength 150 \
         --cstat 0.05 --nthread 8 --od rmats_out --tmp rmats_tmp
# Events with FDR < 0.05 and |dPSI| > 0.1, skipped exons counted by junction reads only
awk -F'\t' 'NR == 1 || ($20 < 0.05 && ($23 > 0.1 || $23 < -0.1))' rmats_out/SE.MATS.JC.txt > SE.sig.txt
```

Splicing changes are common in disease. In infection, inflammation and cancer, hundreds of events change together, often through a change in the level or activity of a few splicing regulators (SR proteins, hnRNPs, RBFOX, MBNL, ESRP; [7.2.16](/7.2.16#sec-16.7.2)); a global analysis of blood samples from patients with COVID-19 (Wang and colleagues, 2022) is one example. A set of co-regulated events with a known regulator is a module of the regulatory network that a gene-level analysis does not see ([7.9.11](/7.9.11)).

### 4.1.4. Splicing as a Drug Target

Splicing is also a target for drugs, and the first case shows how precisely a single event can be manipulated. Spinal muscular atrophy (SMA), the most common genetic cause of death in infancy, is caused by homozygous loss of *SMN1*, which encodes the survival motor neuron protein. A nearly identical paralog, *SMN2*, differs from it at a position in exon 7 (a C-to-T change, c.840C>T) that weakens an exonic splicing enhancer and strengthens a silencer, so that only about $10\,\%$ of *SMN2* transcripts include exon 7; the rest encode an unstable protein. The number of *SMN2* copies (one to four or more) therefore modifies the severity of the disease. Nusinersen, an $18$-nucleotide antisense oligonucleotide with $2'$-O-methoxyethyl sugars and a phosphorothioate backbone, which resists nucleases and does not recruit RNase H, binds an intronic splicing silencer just downstream of exon 7 (ISS-N1), displaces the hnRNP A1/A2 proteins that bind there and raises the inclusion of exon 7. Developed by Adrian Krainer and colleagues with Ionis Pharmaceuticals and approved in 2016, it is given by intrathecal injection; risdiplam (2020), an oral small molecule, achieves the same by stabilizing the interaction of the U1 snRNP with the $5'$ splice site of exon 7. The quantity that these therapies change is exactly the $\psi$ of one skipped exon. Splicing also controls cell identity: an embryonic-stem-cell-specific exon of the transcription factor gene *FOXP1* changes its DNA-binding specificity and is required for pluripotency (Gabut and colleagues, 2011).

## 4.2. Splicing in Single Cells

Single-cell RNA sequencing ([7.9.5](/7.9.5)) shows that cell types differ in splicing as well as in expression, but measuring $\psi$ in single cells meets three obstacles.

1. Coverage. Droplet methods sequence only the $3'$ ends of transcripts and see few junctions; full-length plate-based protocols (Smart-seq2, Smart-seq3) are needed, at a cost of tens to hundreds of times more per cell.
2. Sparsity. A single cell holds a few copies of a typical mRNA, of which a fraction is captured. For most events in most cells there are no junction reads at all: $80$–$90\,\%$ of the entries of a cell-by-event matrix of $\psi$ are missing.
3. Discreteness. With one or two captured molecules, the observed $\psi$ of a cell is $0$, $1$ or $1/2$; the distribution across cells is polarized, and it is hard to tell a cell that uses both isoforms from a mixture of cells each using one.

The missing values cannot be set to zero, as for unobserved gene counts, because $\psi = 0$ is a definite biological statement (all skipping). Methods therefore impute them from similar cells, an operation like the smoothing of gene expression over a neighbor graph ([7.9.5](/7.9.5#sec-5.4)), or model the counts directly. SCASL (single-cell clustering based on alternative splicing landscapes) extracts junctions from split reads without annotation, groups junctions sharing a splice site into events, imputes missing ratios from the nearest cells in an iterative way, and clusters cells by their splicing profiles. Applied to tumors, such splicing-based clusters subdivide cells that look alike by expression and identify intermediate states; in triple-negative breast cancer, epithelial cells with a splicing profile between normal and malignant cells were interpreted as a precancerous state, in which a shift in the isoforms of a few genes precedes malignancy. The general point is that ratios of isoforms, unlike levels, are insensitive to the cell-to-cell fluctuations in total mRNA content and capture efficiency, so they can reveal states that expression levels blur.

## 4.3. Long Reads: Full-Length Isoforms and Circular RNAs

Long reads, from PacBio circular consensus sequencing of full-length cDNA (Iso-Seq) or from **nanopore sequencing** of cDNA or of native RNA ([7.8.9](/7.8.9)), cover a whole transcript in one read and so remove the ambiguity of assembling isoforms from fragments. The analysis maps each read to the genome with a spliced long-read aligner (minimap2), collapses reads with the same intron chain into transcript models, and classifies each model against the annotation. The SQANTI categories are standard: full splice match (the same intron chain as a known transcript), incomplete splice match (a $5'$-truncated version of one, often a degradation product), novel in catalog (new combinations of known splice sites) and novel not in catalog (at least one new site). Quantification assigns reads to models by the same **EM algorithm** as for short reads ([7.9.2](/7.9.2)), with far less ambiguity. The main artifacts are truncated reads, template switching and internal priming of oligo(dT) on A-rich stretches, which create false $3'$ ends; the community benchmark LRGASP (2024) found that long reads identify many new isoforms reliably when the reads are accurate and deep, but that quantification is still more precise with short reads for well-annotated genes.

A **circular RNA** is made by back-splicing, in which a downstream $5'$ splice site joins an upstream $3'$ splice site ([7.2.16](/7.2.16#sec-16.7.5)). In short reads its only signature is the back-splice junction: a split read whose two parts map in reversed order (the $3'$ part upstream of the $5'$ part on the genome). Detectors (CIRI2, CIRCexplorer, find_circ) look for such chimeric alignments, and treatment with RNase R, which degrades linear RNA, enriches circles for validation. The internal structure of a circle cannot be read from the junction alone; long reads of circles, made by rolling-circle reverse transcription so that one read covers the circle several times, showed that circular RNAs of human and mouse brain often contain exons, retained introns and microexons that their linear counterparts lack (Rahimi and colleagues, 2021). Whether a circle is translated is a question for ribosome profiling (4.4.3): footprints spanning the back-splice junction can only come from ribosomes on the circle, and a few circular RNAs (for example circ-ZNF609) are translated into proteins from internal ribosome entry sites.

## 4.4. The Translatome

### 4.4.1. Footprints and the P Site

**Ribosome profiling** sequences the mRNA fragments protected by ribosomes from nuclease digestion ([7.2.6](/7.2.6#sec-6.6); the codon-level view is in [7.2.20](/7.2.20#sec-20.8)).

**Definition 4.4.1 (Translatome)** The **translatome** of a cell is the set of RNAs that are being translated, together with the positions and densities of the ribosomes on them; ribosome profiling measures it as ribosome-protected fragments (RPFs, footprints).

The footprints of elongating eukaryotic ribosomes are $28$–$30$ nt long (a shorter class of $20$–$22$ nt comes from ribosomes with an empty A site). To place each ribosome at a codon, each read is reduced to the position of the P site, which lies at a fixed distance from the $5'$ end for a given read length; the distance is estimated from the data.

**Algorithm 4.4.1 (P-Site Offset)** For each read length $\ell$:

1. Over all annotated coding sequences, histogram the positions of the read $5'$ ends relative to the first nucleotide of the start codon (a metagene).
2. Take the offset $\delta_\ell$ as the distance of the peak just upstream of the start codon: ribosomes that have just initiated have the start codon in the P site, so their $5'$ ends lie $\delta_\ell$ nucleotides upstream (typically $\delta = 12$ for $28$- and $29$-nt reads, $13$ for $30$ nt).
3. Shift every read of length $\ell$ by $\delta_\ell$, compute the reading frame of its P site in the coding sequence, and keep the lengths whose P sites lie mostly in frame $0$.

The cost is one pass over the reads. The result, a P-site track along each transcript, is the input of all later steps. Three features of a good library follow from the steps (figure): reads are enriched in coding sequences and depleted from $3'$ UTRs, there is a peak at the start codon and a smaller one at the stop codon, and the counts repeat with a period of three nucleotides, with $60$–$80\,\%$ of P sites in frame $0$. The periodicity, which reflects the movement of the ribosome one codon at a time, is what distinguishes genuine translation from other protected fragments (complexes of RNA with other proteins, or rRNA fragments).

![Ribosome profiling reads and the three-nucleotide periodicity (simulated reads). A: positions of the 5′ ends of 29-nt footprints relative to the A of the annotated start codon, summed over genes: the peak 12 nt upstream marks ribosomes with the start codon in the P site, and downstream the counts repeat every three nucleotides (dark: frame of the coding sequence). B: after shifting each read length by its P-site offset (Algorithm 4.4.1), the fraction of P sites in each reading frame; poorly phased lengths (here 30 nt) are often discarded. C: a test of active translation for candidate ORFs as in Algorithm 4.4.2: P-site counts of each codon in frames 0, +1 and +2, compared by one-sided Wilcoxon signed-rank tests and combined by Stouffer's method, for a translated ORF (top, combined p = 9e-21) and for coverage without phase (bottom, p = 0.5)](./plots/ribo_periodicity.py)

### 4.4.2. Translation Efficiency and Differential Translation

The number of footprints on a coding sequence is proportional to the number of mRNA molecules times the number of ribosomes on each. Dividing by the mRNA abundance from RNA-seq of the same sample gives a per-molecule measure.

**Definition 4.4.2 (Translation Efficiency)** The **translation efficiency** (TE) of a gene in a sample is the ratio of its ribosome-footprint density on the coding sequence to its mRNA density, each normalized for library size:
$$
\mathrm{TE} = \frac{\text{RPF per kilobase of CDS per million footprints}}{\text{RNA-seq reads per kilobase per million reads}}.
$$
Since the CDS length cancels, $\log\mathrm{TE} = \log(\text{normalized RPF count}) - \log(\text{normalized mRNA count})$.

When elongation is uniform and initiation limits the rate, TE is proportional to the initiation rate ([Formula 20.8.1](/7.2.20#fml-20.8.1)); in general it measures ribosome density, which rises also when elongation slows (4.4.5). A ratio of two noisy counts is noisy, and it is better not to test ratios directly but to model both assays together.

**Formula 4.4.1 (Differential translation as an interaction)** For gene $g$, assay $a \in \{0, 1\}$ (RNA-seq, ribosome profiling) and condition $c \in \{0, 1\}$, model the counts as negative binomial with mean
$$
\log\mu_{gac} = \log s_{ac} + \beta_{g0} + \beta_{g1}a + \beta_{g2}c + \beta_{g3}\,ac, \tag{4.2}
$$
with size factors $s_{ac}$ estimated separately for each assay. Then $\beta_{g2}$ is the change of mRNA level, $\beta_{g2} + \beta_{g3}$ the change of footprints, and the interaction coefficient $\beta_{g3}$ is the change of $\log\mathrm{TE}$. In a formula interface the design is `~ assay + condition + assay:condition`, and differential translation is a test of the interaction (Wald or likelihood ratio, [7.7.20](/7.7.20)).

This is the approach of deltaTE (Chothani and colleagues, 2019), implemented with the **generalized linear model** of DESeq2; Xtail, RiboDiff, riborex and anota2seq are variants. Comparing the tests for $\beta_{g2}$ and $\beta_{g3}$ sorts genes into four classes (figure below, panel A): *forwarded* genes change mRNA and footprints together (transcriptional regulation, TE unchanged); *exclusive* genes change TE without a change of mRNA (pure translational regulation); *buffered* genes change TE in the direction opposite to an mRNA change, which keeps protein synthesis constant; *intensified* genes change both in the same direction. Buffering is common in comparisons of cell lines with different chromosome copy numbers, where translation compensates part of the dosage change.

**Example 4.4.1** A gene has $1000$ mRNA reads and $500$ footprints in the control and $2000$ mRNA reads and $4000$ footprints after treatment, with equal library sizes. The mRNA rises $2$-fold, the footprints $8$-fold, so $\mathrm{TE}$ rises $4$-fold: $\beta_3 = \log_2 4 = 2$ on the $\log_2$ scale, an intensified gene. With $2000$ footprints after treatment instead, footprints and mRNA would both double and the gene would be forwarded; with $500$, TE would halve and the gene would be buffered.

In the simulation of panel A, with $3000$ genes, three replicates per assay and condition and the interaction tested at a BH-adjusted $p < 0.05$, $97.5\,\%$ of the genes were assigned to their true class. Two practical points matter. The two libraries should come from the same lysate, because TE compares them gene by gene; and drugs that arrest elongation before lysis (cycloheximide) distort the positions of footprints near the start codon, so that flash freezing without drugs is now preferred.

### 4.4.3. Which RNAs Are Translated

Ribosome profiling also shows where translation happens, including in RNAs annotated as noncoding, in $5'$ leaders (**upstream open reading frames**, [7.2.20](/7.2.20#sec-20.5.2)), in $3'$ UTRs, and on circular RNAs. Coverage alone is not evidence, because other complexes protect RNA too; the test is the phase of the P sites within a candidate **open reading frame**.

**Algorithm 4.4.2 (Detecting Translated ORFs by Their Phase)** (after RiboCode; Xiao and colleagues, 2018)

1. Candidates: in each transcript, list the ORFs from a start codon (AUG, optionally near-cognate codons such as CUG or GUG) to the first in-frame stop codon, longer than a minimum length.
2. Counts: for each codon $i$ of an ORF, let $x_i$, $y_i$, $z_i$ be the numbers of P sites at its first, second and third nucleotide (frames $0$, $+1$, $+2$).
3. Tests: test $x_i > y_i$ and $x_i > z_i$ across the codons by one-sided **Wilcoxon signed-rank tests**, which use only the sign and rank of the paired differences and so tolerate the very uneven coverage along an ORF.
4. Combination: combine the two p-values by Stouffer's method, $Z = (\Phi^{-1}(1 - p_1) + \Phi^{-1}(1 - p_2))/\sqrt2$ and $p = 1 - \Phi(Z)$, where $\Phi$ is the standard normal distribution function; among overlapping candidates in the same frame choose the start codon with the best support, and control the false discovery rate over all candidates.

The work is linear in the number of codons of all candidates.

**Example 4.4.2** For an ORF with $p_1 = 10^{-4}$ and $p_2 = 0.02$, $Z = (3.719 + 2.054)/\sqrt2 = 4.08$ and the combined $p = 2.2\times10^{-5}$: stronger than either test alone, because both point the same way. In panel C of the figure, $60$ codons of a translated ORF give $p = 9\times10^{-21}$, while coverage of the same depth without phase gives $p = 0.5$.

Applied to many tissues and tumors, such methods find thousands of translated uORFs and small ORFs, some encoding peptides with demonstrated functions (in muscle, for example, myoregulin and other micropeptides that regulate the calcium pump SERCA). Most translated uORFs act by regulating the translation of the main ORF downstream rather than through their peptides ([7.2.20](/7.2.20#sec-20.5.2)), and tumors often differ from normal tissue in the use of uORFs, a reflection of the stress signaling that controls reinitiation. The translatome is also context-dependent: the set of translated ORFs changes with stress, differentiation and the cell cycle, so annotation from one condition is incomplete.

### 4.4.4. mRNA and Protein Levels

Why measure translation at all, when RNA-seq is cheap? Because the level of an mRNA explains only part of the level of its protein. In a genome-wide study of mouse fibroblasts (Schwanhäusser and colleagues, 2011), mRNA levels explained about $40\,\%$ of the variance of protein levels across genes, and translation rate constants were the strongest single predictor. Later analyses that corrected for measurement error raised the share explained by mRNA to more than half (Li, Bickel and Biggin, 2014), and across conditions within one gene the correlation is usually higher than across genes. The steady state $p^* = k_{\mathrm{tl}}m^*/k_{\mathrm{deg},p}$ shows why ([7.2.22](/7.2.22)): protein level is the product of mRNA level, translation rate and protein lifetime, and the last two vary between genes by about as much as the first. Translation is also where most of the energy of gene expression is spent, about four ATP equivalents per peptide bond. Measuring the **proteome** directly is the subject of [7.9.9](/7.9.9); ribosome profiling measures one factor of the product.

### 4.4.5. A Data-Driven Discovery: Rocaglamide A

Methods for TE rest on two assumptions: that initiation limits the rate of translation, so that ribosome density measures the initiation rate; and that the pattern of ribosomes along a transcript (its elongation profile) is the same in the conditions compared, so that only the total changes. Testing the second assumption requires a measure of where on a coding sequence the ribosomes are.

**Formula 4.4.2 (Polarity score)** For a coding sequence of $L$ codons with ribosome densities $d_1, \dots, d_L$, let $p_i = d_i/\sum_jd_j$ and $w_i = (2i - L - 1)/(L - 1)$, which runs from $-1$ at the first codon to $+1$ at the last. The polarity of the profile is
$$
\rho = \sum_{i=1}^{L}p_iw_i \in [-1, 1]. \tag{4.3}
$$
A uniform profile has $\rho = 0$; ribosomes piled up near the start give $\rho < 0$, near the stop $\rho > 0$; the change $\Delta\rho$ between conditions detects a change of the elongation profile independently of the total.

**Example 4.4.3** In a $300$-codon coding sequence, a fivefold excess of density over the first $30$ codons gives $\rho = -0.26$; uniform density gives $0$.

A reanalysis of $49$ published ribosome profiling studies (Li and colleagues, 2023) computed $\Delta\rho$ for every gene and treatment and found that some perturbations shift ribosomes along coding sequences, contrary to the second assumption. The clearest was rocaglamide A (RocA), a natural product of plants of the genus *Aglaia* and a candidate anticancer drug, known to inhibit translation initiation by clamping the RNA helicase eIF4A (an **initiation factor** of the cap-binding complex, [7.2.20](/7.2.20#sec-20.4)) onto polypurine sequences in $5'$ leaders, which blocks the scanning small subunit (Iwasaki, Floor and Ingolia, 2016). Reanalyzing those data with a dose series of RocA, the study divided the significantly changed genes into two groups: $643$ genes with fewer footprints on the coding sequence and ribosomes accumulating in the $5'$ leader, as expected for an initiation block (initiation-responsive genes), and $374$ genes with more footprints, concentrated over roughly the first hundred codons (elongation-responsive genes). The second group had been missed because a TE analysis that assumes a constant profile reads more footprints as more translation. The proposed explanation is that RocA-bound eIF4A on polypurine motifs within coding sequences also blocks elongating ribosomes, whose collisions activate the ribotoxic stress kinase ZAKα and the p38 and JNK pathways. The figure models the two patterns: an initiation block lowers the density uniformly and leaves $\rho$ unchanged, an elongation block piles ribosomes near the start and makes $\rho$ negative.

![Changes of translation measured by ribosome profiling. A: log2 fold changes of mRNA and of footprints for 3000 simulated genes (three replicates per condition and assay), analysed with the interaction model of Formula 4.4.1 (here as a linear model on log counts) and classified as forwarded, exclusive, buffered or intensified, with gray for genes without significant change (BH-adjusted p < 0.05). B, C: model profiles of ribosome density along a 300-codon coding sequence with a 50-codon leader: B, a scanning block in the leader lowers the density on the coding sequence uniformly and accumulates ribosomes upstream (an initiation-responsive pattern, polarity unchanged); C, a block of early elongation piles ribosomes over the first 100 codons (an elongation-responsive pattern, polarity −0.29)](./plots/te_polarity.py)

The case illustrates data-driven discovery ([7.9.1](/7.9.1#sec-1.2)) at its best: no new experiment, a systematic reanalysis of public data with a statistic designed to test an assumption, a surprising result in one condition, and a mechanism that can then be tested directly. It also illustrates why the assumptions of a quantification method deserve to be checked in each data set.

## 4.5. Nascent Transcription and RNA Turnover

An mRNA level is the ratio of synthesis to degradation ($m^* = k_{\mathrm{syn}}/k_{\mathrm{deg}}$, [Formula 18.1.1](/7.2.18#fml-18.1.1)), and a change in level may come from either. Two kinds of methods separate them. The first sequences nascent RNA still attached to RNA polymerase II: NET-seq (Churchman and Weissman, 2011) immunoprecipitates the polymerase complex and sequences the $3'$ ends of the RNA inside it, giving the position of every engaged polymerase at single-nucleotide resolution; PRO-seq (Kwak and colleagues, 2013) lets engaged polymerases incorporate one biotinylated nucleotide in isolated nuclei and sequences the run-on products (a genome-wide version of the run-on assay, [7.2.6](/7.2.6#sec-6.3.2)). Both show promoter-proximal pausing, divergent transcription from promoters and enhancers, and the speed of elongation; they measure transcription directly, before processing and decay.

The second kind labels new RNA metabolically. Cells take up $4$-thiouridine (4sU) for a time $t$; in SLAM-seq (Herzog and colleagues, 2017) alkylation of the thiol makes the reverse transcriptase read 4sU as C, so reads from new RNA carry T-to-C mismatches, without any biochemical separation ([7.2.18](/7.2.18#sec-18.1.2)). The difficulty is quantitative: only a few percent of the uridines of new RNA are replaced, so many reads of new molecules contain no conversion, while sequencing errors put a few conversions into reads of old molecules. A mixture model separates the two.

**Formula 4.5.1 (Binomial mixture for labeled reads)** Let read $r$ of a gene contain $n_r$ uridine positions and $k_r$ T-to-C conversions. With $\theta$ the fraction of the gene's molecules made during labeling, $p_{\mathrm{c}}$ the conversion probability per uridine in new RNA and $p_{\mathrm{e}}$ the background rate,
$$
\mathbb{P}(k_r \mid n_r) = \theta\binom{n_r}{k_r}p_{\mathrm{c}}^{k_r}(1 - p_{\mathrm{c}})^{n_r - k_r} + (1 - \theta)\binom{n_r}{k_r}p_{\mathrm{e}}^{k_r}(1 - p_{\mathrm{e}})^{n_r - k_r}. \tag{4.4}
$$
$p_{\mathrm{e}}$ is estimated from unlabeled samples and $p_{\mathrm{c}}$ from all genes together; $\theta$ is estimated for each gene by the EM algorithm, alternating the posterior probability that each read is new with the mean of these probabilities. For a gene in steady state in cells growing at rate $\mu$, $\theta = 1 - \mathrm{e}^{-(k_{\mathrm{deg}} + \mu)t}$, so
$$
k_{\mathrm{deg}} = -\frac{\ln(1 - \theta)}{t} - \mu, \qquad t_{1/2} = \frac{\ln 2}{k_{\mathrm{deg}}}. \tag{4.5}
$$

**Example 4.5.1** Take reads with $n = 30$ uridines, $p_{\mathrm{c}} = 0.04$ and $p_{\mathrm{e}} = 0.001$. A read of new RNA has no conversion with probability $0.96^{30} = 0.29$, a read of old RNA has at least one with probability $1 - 0.999^{30} = 0.03$. If $\theta = 0.3$, the fraction of reads with a conversion is $0.3 \times 0.71 + 0.7 \times 0.03 = 0.23$. After $t = 2\,\mathrm{h}$ of labeling in cells doubling every $24\,\mathrm{h}$, the true $\theta = 0.3$ gives $k_{\mathrm{deg}} = 0.149\,\mathrm{h^{-1}}$ and $t_{1/2} = 4.6\,\mathrm{h}$; taking the share of converted reads, $0.23$, as $\theta$ would give $t_{1/2} = 6.7\,\mathrm{h}$, a $45\,\%$ overestimate. In the simulation of the figure, the naive estimate is about $0.65$ times the true $\theta$ for every gene, while the mixture recovers $\theta$ with a root-mean-square error of $0.04$ from $300$ reads per gene.

![Estimating the new fraction of each mRNA from metabolic labeling (simulated reads). A: T-to-C conversions per read for one gene (400 reads with about 28 uridines; 30% new RNA, conversion rate 0.04 per uridine in new RNA, error rate 0.001 in old RNA), with the two components of the binomial mixture of Formula 4.5.1 fitted by EM. B: new fractions of 300 genes estimated by the mixture (dark) and by the share of reads with at least one conversion (light), which misses the new molecules whose reads carry no conversion. C: half-life from the new fraction after 2 h of labeling in cells doubling every 24 h, Eq. (4.5)](./plots/slam_mixture.py)

Time courses of labeling (and of chasing the label) give synthesis, processing and degradation rates of every transcript; combined with a perturbation, they show whether a regulator acts on transcription or on stability. The same mixture idea applies to single cells (scSLAM-seq, NASC-seq), where the new and old RNA of one cell give a direct estimate of the recent change of its state, the experimental counterpart of RNA velocity ([7.9.7](/7.9.7)).

## 4.6. The Epitranscriptome and RNA–Protein Interactions

### 4.6.1. RNA Modifications

More than $150$ chemical modifications of RNA nucleosides are known, most of them in tRNA and rRNA. In mRNA the most abundant internal modification is $N^6$-methyladenosine (m6A), at about $0.1$–$0.4\,\%$ of adenosines, mostly within the consensus DRACH ($\mathrm{D} = $ A, G or U; $\mathrm{R} = $ A or G; $\mathrm{H} = $ A, C or U) and enriched near stop codons and in $3'$ UTRs. It is written co-transcriptionally by the METTL3–METTL14 methyltransferase complex, can be removed by the demethylases FTO and ALKBH5, and is read by YTH-domain proteins (YTHDF1–3 in the cytoplasm, YTHDC1 in the nucleus) that promote decay, translation or splicing. Other mRNA modifications include pseudouridine, $N^1$-methyladenosine, $5$-methylcytidine and inosine.

**Definition 4.6.1 (Epitranscriptome)** The **epitranscriptome** is the set of chemical modifications of the RNAs of a cell, with their positions and the fraction of molecules modified at each position (the stoichiometry).

The mapping methods trade resolution against bias:

| Method | Principle | Resolution | Stoichiometry |
|---|---|---|---|
| MeRIP-seq / m6A-seq (2012) | immunoprecipitation of fragmented RNA with an anti-m6A antibody; peaks compared with input | $100$–$200$ nt | no |
| miCLIP | antibody crosslinked to RNA by UV; mutations and truncations at the crosslink | single nucleotide | no |
| GLORI (2023) | chemical deamination of unmethylated A to I, read as G; m6A resists | single nucleotide | yes |
| Direct RNA nanopore sequencing | modified bases change the ionic current and the base caller's errors | single nucleotide, per molecule | yes |

In nanopore sequencing of native RNA ([7.6.12](/7.6.12)), the RNA itself passes through the pore, so modifications are not erased by reverse transcription. Each modification shifts the current of the $k$-mers containing it, and classifiers trained on synthetic RNAs with and without the modification detect it: EpiNano (2019) used the systematic errors of base calling with a **support vector machine**, later tools model the current signal directly, and the current base callers report modification probabilities for each base. Because each read is one molecule, the method also shows whether two modifications occur on the same molecule and on which isoform. Dinopore (2022) applies the approach to inosine, which reverse transcription reads as G, and so distinguishes an edited adenosine (A-to-I, 4.7.2) from a genomic A/G variant, which short reads cannot.

### 4.6.2. Crosslinking and Immunoprecipitation

Which RNAs, and which positions on them, does an RNA-binding protein contact? Immunoprecipitating the protein from a lysate collects RNAs that bound to it, or to its partners, or re-associated after lysis. Covalent crosslinking in living cells removes the last two problems.

**Definition 4.6.2 (CLIP)** **Crosslinking and immunoprecipitation** (CLIP) is the genome-wide mapping of the binding sites of an RNA-binding protein in which protein–RNA contacts are crosslinked covalently in living cells, usually by ultraviolet light, the RNA is partially digested, the protein–RNA complexes are purified by immunoprecipitation and denaturing gel electrophoresis, and the RNA fragments are sequenced (Ule and colleagues, 2003).

The variants differ in how the exact contact is read from the sequence. HITS-CLIP (2008) uses crosslink-induced deletions; PAR-CLIP (Hafner and colleagues, 2010) incorporates the photoreactive nucleoside 4-thiouridine into RNA, crosslinks at $365\,\mathrm{nm}$, and reads the contact as a T-to-C transition, which separates crosslinked from background reads; iCLIP and eCLIP (2016) use the fact that reverse transcription stops at the crosslinked nucleotide, so the $5'$ ends of reads mark it. The ENCODE project mapped about $150$ RNA-binding proteins by eCLIP in two cell lines, with size-matched input controls. Analysis calls peaks of crosslink sites against the input and the RNA abundance (a sparse count problem like peak calling in [7.9.8](/7.9.8)) and finds sequence motifs in them ([7.8.8](/7.8.8)). Combined with splicing changes after depleting the same protein, CLIP gives an RNA map: binding upstream of a cassette exon tends to repress it and binding downstream to enhance it, for regulators such as NOVA and RBFOX.

### 4.6.3. RNA Structure Probing

The structure of an RNA in cells can be probed with reagents that modify flexible or unpaired nucleotides: SHAPE reagents acylate the $2'$-hydroxyl of flexible nucleotides, dimethyl sulfate (DMS) methylates unpaired A and C. In mutational profiling (SHAPE-MaP, 2014; DMS-MaPseq, 2017) the reverse transcriptase is run under conditions in which it reads through modified nucleotides and incorporates mismatches, so the mutation rate at each position, compared with an untreated control, measures its reactivity. Reactivities enter structure prediction as pseudo-energy constraints in the dynamic programming of [7.8.16](/7.8.16), and the comparison of reactivities in cells and in vitro shows where proteins or other RNAs bind. Long-read versions (PORE-cupine, 2021, with nanopore detection of the modifications) determine structures separately for each isoform.

## 4.7. Other Layers of RNA Processing

### 4.7.1. Alternative Polyadenylation

About $70\,\%$ of human genes have more than one polyadenylation site, mostly within the $3'$ UTR, so that one gene makes mRNAs with short and long $3'$ UTRs that differ in their sites for microRNAs and RNA-binding proteins ([7.2.17](/7.2.17#sec-17.2.4), [7.2.18](/7.2.18)). Dedicated $3'$-end sequencing (PAS-seq, 3′READS, QuantSeq REV) maps the cleavage sites directly; from ordinary RNA-seq, the use of a distal site is inferred from the drop in coverage at the proximal site.

**Formula 4.7.1 (Distal polyadenylation usage)** If the $3'$ UTR of a transcript has a proximal and a distal polyadenylation site and the read coverage is $W_{\mathrm{S}} + W_{\mathrm{L}}$ upstream of the proximal site and $W_{\mathrm{L}}$ between the two sites, the percentage of distal polyadenylation site usage is
$$
\mathrm{PDUI} = \frac{W_{\mathrm{L}}}{W_{\mathrm{L}} + W_{\mathrm{S}}}. \tag{4.6}
$$
DaPars (Xia and colleagues, 2014) finds the proximal site without annotation as the change point of the coverage that minimizes the squared deviation of a two-level step function.

**Example 4.7.1** Coverage $100$ upstream of the proximal site and $30$ between the sites gives $W_{\mathrm{L}} = 30$, $W_{\mathrm{S}} = 70$ and $\mathrm{PDUI} = 0.3$: $30\,\%$ of the transcripts have the long $3'$ UTR. A tumor in which the same gene has coverage $100$ and $10$ has $\mathrm{PDUI} = 0.1$, a shortening.

Shorter $3'$ UTRs are a widespread feature of proliferating cells (Sandberg and colleagues, 2008) and of many cancers (Mayr and Bartel, 2009), in which oncogenes escape repression by microRNAs. Since PDUI is a ratio within one transcript, like $\psi$, it is analysed with the same replicate models.

### 4.7.2. RNA Editing

**RNA editing** by deamination of adenosine to inosine, by the ADAR enzymes acting on double-stranded RNA ([7.2.17](/7.2.17#sec-17.6.3)), is detected in RNA-seq as A-to-G mismatches, because inosine pairs with C. The detection is a variant call ([7.8.12](/7.8.12)) with different sources of error: a site must be absent from the DNA of the same individual (or at least from databases of genomic variants), must not lie near a splice junction or at the end of reads, where alignment errors cluster, and on stranded libraries must show A-to-G on the transcribed strand. In humans most of the more than a million known sites lie in Alu repeats, which form double-stranded hairpins in introns and UTRs; a few hundred recode proteins, the classic example being the glutamine-to-arginine site of the glutamate receptor subunit GluA2, edited in nearly all transcripts in the brain, which makes the channel impermeable to calcium. Editing levels, again ratios ($G/(A + G)$ at a site), vary between tissues and are reduced in some diseases; databases such as REDIportal collect the sites.

### 4.7.3. Fusion Transcripts

Chromosomal rearrangements in tumors join parts of two genes and create fusion transcripts, some of which drive the cancer: *BCR*–*ABL1* in chronic myeloid leukemia, *TMPRSS2*–*ERG* in about half of prostate cancers, *EML4*–*ALK* in a subset of lung cancers, all targets of specific drugs or of diagnosis ([7.9.13](/7.9.13)). In RNA-seq a fusion appears as split reads with parts in two genes and as read pairs whose mates map to the two genes. Detectors (STAR-Fusion, Arriba) collect such chimeric alignments, require support from several independent reads at a consistent breakpoint, preferably at exon boundaries, and filter the frequent artifacts: read-through transcripts of adjacent genes, chimeras formed during library preparation, and alignments between paralogs. Fusions found in RNA reflect genomic rearrangements that can be confirmed in DNA; trans-splicing between transcripts without a rearrangement exists but is rare in mammals.

## Summary

| Layer | Readout in the reads | Quantity | Model | Main tools |
|---|---|---|---|---|
| Splicing events | inclusion and skipping junction reads | $\psi$ (Definition 4.1.1, Formula 4.1.1), $\Delta\psi$ | binomial with logit-normal replicate variation, LRT (Algorithm 4.1.1) | rMATS, LeafCutter, SUPPA2, MAJIQ |
| Splicing in single cells | sparse junction reads from full-length protocols | per-cell ratios, mostly missing | imputation over similar cells, clustering | SCASL and others |
| Isoforms and circles | full-length reads; back-splice junctions | isoform models and abundances | classification against the annotation, EM | Iso-Seq, IsoQuant, CIRI2 |
| Translation | footprints, P sites, 3-nt phase | TE (Definition 4.4.2), $\Delta\log\mathrm{TE}$, polarity (Formula 4.4.2) | NB GLM with an assay × condition interaction (Formula 4.4.1); Wilcoxon and Stouffer (Algorithm 4.4.2) | deltaTE, Xtail, RiboCode |
| Nascent RNA and turnover | 3′ ends of polymerase-bound RNA; T-to-C conversions | polymerase density; new fraction $\theta$, half-life | binomial mixture fitted by EM (Formula 4.5.1) | NET-seq, PRO-seq, SLAM-seq, GRAND-SLAM |
| Modifications | antibody enrichment, chemical conversion, nanopore current | sites and stoichiometry (Definition 4.6.1) | peak calling; classifiers of the current | MeRIP-seq, GLORI, nanopore tools |
| Protein binding | crosslink mutations or truncations | binding sites (Definition 4.6.2) | peaks against size-matched input | PAR-CLIP, eCLIP |
| 3′ ends, editing, fusions | coverage drop; A-to-G; chimeric reads | PDUI (Formula 4.7.1); editing level; breakpoints | change point; variant calling; read support | DaPars, REDIportal, STAR-Fusion |

- Every measurement of this chapter is a ratio of counts within one gene or one site. Its precision is set by the number of informative reads, not by the total depth (Example 4.1.1), and its comparison between conditions must model the variation between biological replicates (Example 4.1.2), as for gene counts.
- Methods carry assumptions that can fail: uniform coverage for exon-body counts, uniform elongation for translation efficiency (4.4.5), complete conversion for labeling (Example 4.5.1). Systematic reanalysis of public data can test them.
- mRNA level, translation and protein lifetime contribute comparably to protein level (4.4.4), and regulators of splicing, translation and RNA stability change the output of genes without changing their transcript counts; these layers are part of the regulatory network.

## Questions

1. Why does the naive ratio $I/(I + S)$ overestimate the percent spliced in of a skipped exon counted by junction reads, and when would it underestimate it?

   **Answer** The inclusion form has two junctions and the skipping form one, so at equal numbers of molecules the inclusion form produces about twice as many junction reads: $I/S \approx 2\psi/(1 - \psi)$, and $I/(I + S) = 2\psi/(1 + \psi) > \psi$ for $0 < \psi < 1$ (for $\psi = 0.6$ it is $0.75$). If exon-body reads of a long cassette exon are added to $I$, the inclusion form offers even more positions, and ignoring them would overestimate more. The naive ratio would underestimate $\psi$ only if the skipping form offered more positions than the inclusion form, as for a retained intron counted by reads inside a short intron against a junction, or for an alternative $3'$ site whose extension is shorter than the read positions lost.

2. An exon has $I = 6$, $S = 2$ junction reads in one sample and $I = 600$, $S = 200$ in another. Both give $\hat\psi = 0.60$. Give the $95\,\%$ posterior intervals and explain why most splicing analyses filter events by read count.

   **Answer** With effective lengths $l_I = 170$, $l_S = 85$ and a uniform prior, the posterior of $p$ is $\mathrm{Beta}(7, 3)$ and $\mathrm{Beta}(601, 201)$; mapping the quantiles to $\psi$ gives $[0.25, 0.86]$ and $[0.56, 0.64]$. With $8$ reads almost every $\psi$ between a quarter and nine tenths is plausible, so an apparent $\Delta\psi$ of $0.3$ between two such samples means nothing; events with few reads add tests without power and increase the multiple-testing burden, so they are removed before testing (independent filtering, [7.7.20](/7.7.20)).

3. In Example 4.1.2 the pooled Fisher test gives $p \approx 10^{-21}$ for data set C, while the replicate model gives $p = 0.07$. Which is right, and what does the difference show?

   **Answer** The replicate model is the appropriate one for the question "does the treatment change splicing in this kind of sample?". The Fisher test treats every read as an independent replicate and asks only whether the pooled reads of the two groups could come from one proportion, which they clearly cannot; but the replicates of each group also differ among themselves by as much as the groups differ, so the group difference is not distinguishable from the variation between individual samples. The difference is the same as between a test with cells as replicates and a pseudobulk test in single-cell analysis (7.9.5): the unit of replication must be the biological sample.

4. A gene has $800$ mRNA reads and $400$ footprints in the control, $400$ mRNA reads and $380$ footprints after a drug, with equal library sizes and three replicates each. Compute the fold changes and the change of TE, classify the gene, and explain why the interaction model is preferred to a test of the TE ratios.

   **Answer** mRNA changes $0.5$-fold ($\log_2 = -1$), footprints $0.95$-fold ($\log_2 = -0.074$), so TE rises $1.9$-fold ($\beta_3 = 0.926$ on the $\log_2$ scale). If both the mRNA change and the interaction are significant, the TE change opposes the mRNA change: the gene is buffered, and protein synthesis is nearly constant despite halved mRNA. The interaction model uses the counts of both assays with their own negative binomial variances and size factors, so the uncertainty of each count enters correctly; a ratio of two noisy counts per sample has a skewed, heavy-tailed distribution, especially at low counts, and a t-test on such ratios is poorly calibrated.

5. Why does a three-nucleotide periodicity of P sites distinguish translation from other sources of protected RNA fragments? A candidate ORF lies in a $5'$ leader and overlaps the main ORF in a different frame. How can its translation be detected?

   **Answer** Ribosomes advance one codon at a time, so their P sites fall predominantly on the first nucleotide of codons of the frame being translated; other ribonucleoprotein complexes protect fragments without any relation to the codon frame. For an overlapping uORF in frame $+1$ relative to the main ORF, the P sites in the overlap come from both; the part of the uORF upstream of the main start codon can be tested alone (Algorithm 4.4.2 restricted to those codons), and in the overlap one can compare the excess of frame $+1$ over the level expected from the main ORF's phase distribution, estimated on non-overlapping main ORF codons. Initiation-specific footprints obtained with harringtonine or lactimidomycin give independent evidence of a start codon at the uORF.

6. A labeling experiment ($t = 1\,\mathrm{h}$, cells doubling every $20\,\mathrm{h}$) gives a new fraction $\theta = 0.1$ for gene A and $\theta = 0.6$ for gene B. Compute their half-lives. Which estimate is less precise, and why?

   **Answer** $\mu = \ln 2/20 = 0.0347\,\mathrm{h^{-1}}$. For A, $k_{\mathrm{deg}} = -\ln 0.9 - 0.0347 = 0.1054 - 0.0347 = 0.0707\,\mathrm{h^{-1}}$, $t_{1/2} = 9.8\,\mathrm{h}$. For B, $k_{\mathrm{deg}} = -\ln 0.4 - 0.0347 = 0.916 - 0.0347 = 0.882\,\mathrm{h^{-1}}$, $t_{1/2} = 0.79\,\mathrm{h}$. For A the estimate depends on a small $\theta$ and on the subtraction of the dilution rate, which is about a third of $-\ln(1 - \theta)$; an error of $0.02$ in $\theta$ changes $t_{1/2}$ by about $30\,\%$. For B, $\mathrm{d}k/\mathrm{d}\theta = 1/(1 - \theta) = 2.5$ is moderate, and an error of $0.02$ changes $t_{1/2}$ by about $6\,\%$. The best precision is obtained when the labeling time is comparable to the half-life; a time course covers a range of stabilities.

7. Why does m6A mapping with an antibody (MeRIP-seq) not give the stoichiometry of a site, while GLORI and nanopore sequencing do?

   **Answer** Immunoprecipitation enriches fragments containing at least one modified base relative to input; the enrichment depends on the antibody's affinity, on the number of modified sites in a fragment and on the background binding, so a peak height cannot be converted into the fraction of molecules modified at a given adenosine, and the resolution is that of the fragment. GLORI converts every unmethylated adenosine to a base read as G, so at each site the fraction of reads still showing A is the methylated fraction (after correcting for incomplete conversion). In nanopore sequencing each read is a molecule, and classifying each molecule at a site as modified or not gives the fraction directly, with an error set by the classifier's accuracy.

8. (Design) Design an experiment and an analysis to decide whether a drug that lowers the protein level of a set of genes acts on transcription, on mRNA stability or on translation.

   **Answer** Treat cells with drug or vehicle (at least three biological replicates each) and collect, from the same cultures: RNA-seq (mRNA levels); a short pulse of 4sU before harvest for SLAM-seq (new fraction and hence synthesis and degradation rates by Formula 4.5.1 and Eq. (4.5)), or a time course; and ribosome profiling from the same lysates as the RNA-seq. Transcriptional action shows as a lower synthesis rate with unchanged half-life and unchanged TE (footprints forwarded); stability as a shorter half-life with unchanged synthesis; translation as a TE change in the interaction model (Formula 4.4.1) with unchanged mRNA (exclusive). The polarity of footprint profiles (Formula 4.4.2) distinguishes an initiation from an elongation effect. Check the protein change and its timing by targeted proteomics ([7.9.9](/7.9.9)), and confirm the mechanism for a few genes by reporters (a $5'$ leader fused to luciferase) and by drugs with known targets.

9. Coverage over a $3'$ UTR is $200$ upstream of the proximal polyadenylation site and $150$ between the proximal and distal sites in normal tissue, and $200$ and $40$ in a tumor. Compute PDUI and interpret.

   **Answer** Normal: $W_{\mathrm{L}} = 150$, $W_{\mathrm{S}} = 50$, $\mathrm{PDUI} = 0.75$. Tumor: $W_{\mathrm{L}} = 40$, $W_{\mathrm{S}} = 160$, $\mathrm{PDUI} = 0.20$. Most transcripts in the tumor end at the proximal site, so the $3'$ UTR is shortened. If the lost region contains microRNA sites, the tumor mRNA escapes repression and may be more stable and more translated, a common mechanism of oncogene activation in cancers with shortened UTRs. The interpretation assumes uniform coverage along the UTR; a $3'$ bias of the library would lower $W_{\mathrm{S}}$ artificially, so the comparison is valid only between libraries of the same protocol.
