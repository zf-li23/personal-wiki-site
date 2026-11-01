---
title: Probabilistic Models of Sequences and Gene Prediction
description: "Statistics of genome sequences and the models built on them: base composition, GC skew and the replication origin of E. coli; dinucleotide statistics and CpG depletion; Markov chain models of sequence and their estimation; classifying CpG islands with log-likelihood ratios and segmenting a genome with a two-state hidden Markov model (forward–backward posteriors on the LCT–MCM6 locus); the 5' splice site HMM; open reading frames, codon usage and three-base periodicity; prokaryotic gene finders (GeneMark, Glimmer, Prodigal) and a periodic Markov coding model trained on E. coli; eukaryotic gene structure, exon and intron lengths and generalized HMMs (GENSCAN, AUGUSTUS); evidence-based annotation (BRAKER, MAKER, long reads); evaluation at nucleotide, exon and gene level; numerical representations of sequences."
---

A genome sequence is not a random string. Its composition varies along the chromosome, some short words are avoided and others favored, protein-coding regions carry a three-base rhythm, and functional elements such as promoters, splice sites and CpG islands have statistical signatures of their own. This chapter turns such regularities into probabilistic models and uses them for the first task of every genome project: finding the genes. The models are **Markov models** of sequence, in which each base depends on the few bases before it, and **hidden Markov models**, in which the dependence changes according to an unobserved state (island or not, exon or intron); their general theory, with the **forward algorithm**, the **Viterbi algorithm** and the **Baum–Welch algorithm**, was given in [4.6.8](/4.6.8), and this chapter treats the biological modeling. The chapter follows the path from statistics of whole genomes (Section 7.1) through classification and segmentation (Section 7.2) to prokaryotic and eukaryotic gene prediction (Sections 7.3 and 7.4), its evaluation (Section 7.5) and the numerical encodings of sequences used by learning methods (Section 7.6). The examples use two real genomes: *Escherichia coli* K-12 for bacterial genes, and human chromosome 21 and the *LCT*–*MCM6* locus of chromosome 2, the running example of the course, for CpG islands and exons. Motifs and conservation, the other sources of evidence for functional elements, are the subject of [7.8.8](/7.8.8); assembly and the full annotation pipeline of a new genome are in [7.8.11](/7.8.11).

## 7.1. The Statistics of Genome Sequences

### 7.1.1. Composition and Skew

The simplest statistic is the base composition. Because of base pairing, the two strands together contain equal amounts of A and T and of G and C, and genomes are described by their GC content, which ranges from below $20\,\%$ in some bacteria to above $70\,\%$ in others and varies along mammalian chromosomes in regions of hundreds of kilobases (isochores). Within one strand, however, the complementary bases need not be equal (Chargaff's second parity rule holds only approximately), and the deviations carry information.

**Definition 7.1.1 (GC Skew)** The *GC skew* of a window of one strand is $(G - C)/(G + C)$, with $G$ and $C$ the numbers of the two bases in the window; the cumulative skew is its running sum along the genome.

In many bacteria the leading strand of replication is enriched in G and depleted in C, probably because the lagging-strand template, exposed as single strand during replication, suffers more cytosine deamination ([7.2](/7.2)), and because genes, which are G-rich on their coding strand, are preferentially oriented in the direction of replication. The skew therefore changes sign at the replication origin and the terminus, and the cumulative skew has its minimum at the origin and its maximum at the terminus (Lobry 1996). This is the standard first step in finding the origin of a newly sequenced bacterial genome.

**Example 7.1.1** The genome of *E. coli* K-12 MG1655 (RefSeq NC_000913.3) has $4\,641\,652$ bp and a GC content of $50.8\,\%$. In $10$-kb windows of the forward strand, the GC skew averages $-0.033$ between $1.6$ and $3.9$ Mb and $+0.031$ elsewhere; the cumulative skew is lowest at position $3\,925\,596$, within a few hundred base pairs of *oriC* (annotated at $3\,925\,744$–$3\,925\,975$), and highest near $1.55$ Mb, in the terminus region opposite the origin. The two replication forks move from *oriC* in opposite directions, so the forward strand is the lagging-strand template on one arm and the leading-strand template on the other.

![GC skew of the *E. coli* K-12 MG1655 genome. A: the skew (G − C)/(G + C) of the forward strand in 10-kb windows, positive (green) on one replication arm and negative (red) on the other. B: the cumulative skew, with its minimum at 3.93 Mb, the replication origin *oriC*, and its maximum near 1.55 Mb, in the terminus region. Computed from the RefSeq sequence NC_000913.3](./plots/gc-skew.py)

### 7.1.2. Word Statistics

The frequency of a short word, a **k-mer**, is compared with its expectation from the frequencies of its letters. For dinucleotides the ratio

$$
\rho_{xy} = \frac{f_{xy}}{f_xf_y}
$$
of observed to expected frequency is a stable signature of a genome, similar between distant regions of the same genome and different between species (Karlin and colleagues), which is used to assign metagenomic fragments to genomes and to detect recently transferred genes ([7.8.6](/7.8.6#sec-6.8.2)).

**Example 7.1.2** On human chromosome 21 (GRCh38, $40.9\,\%$ GC), $\rho_{\mathrm{CG}} = 0.275$, $\rho_{\mathrm{TA}} = 0.733$ and all other dinucleotides lie between $0.84$ and $1.22$. In *E. coli*, $\rho_{\mathrm{CG}} = 1.16$ and $\rho_{\mathrm{TA}} = 0.76$. The depletion of TA is shared (TpA steps are flexible and part of stop codons and degradation signals in RNA), but the fourfold depletion of CpG is specific to vertebrates: most CpGs in vertebrate genomes are methylated at the cytosine, and **deamination** of 5-methylcytosine gives thymine, a mutation that escapes the repair of uracil, so CpG decays to TpG and CpA over evolutionary time ([7.2.15](/7.2.15)). The exceptions are the **CpG islands**, stretches of hundreds of base pairs that keep the expected CpG frequency because they are unmethylated in the germline ([Definition 15.7.1](/7.2.15#def-15.7.1) of 7.2.15); they mark most promoters of housekeeping genes, and finding them is a classical problem of sequence modeling.

### 7.1.3. Markov Chain Models of Sequence

**Definition 7.1.2 (Markov Chain Model of a Sequence)** A *Markov chain model of order $k$* for sequences over an alphabet $\mathcal{A}$ specifies, for every context $w \in \mathcal{A}^k$ and letter $b$, the transition probability $a_{wb} = \mathbb{P}(x_i = b \mid x_{i-k} \cdots x_{i-1} = w)$; the probability of a sequence is

$$
\mathbb{P}(x_1 \cdots x_L) = \mathbb{P}(x_1 \cdots x_k)\prod_{i=k+1}^{L}a_{x_{i-k}\cdots x_{i-1},\,x_i}.
$$
The order-$0$ model treats bases as independent with fixed frequencies.

The **maximum likelihood estimation** of the transition probabilities from training sequences is the ratio of counts, $\hat a_{wb} = n_{wb}/\sum_cn_{wc}$, in practice with a pseudocount for words never seen. The number of free parameters is $3 \cdot 4^k$ for DNA: $12$ for order $1$, $3072$ for order $5$, $786\,432$ for order $9$. The order is chosen by a compromise between context and data: higher orders capture codon structure and short motifs, but need much training data. GeneMark uses order $5$ for coding regions, enough to see two adjacent codons; Glimmer avoids a fixed order with *interpolated Markov models*, which combine the predictions of all orders up to $8$, weighting each context by how often it was seen in training (Salzberg and colleagues 1998).

## 7.2. Classifying and Segmenting Sequences

### 7.2.1. Log-Likelihood Ratios

Two Markov models, one trained on a class of sequences (CpG islands, coding regions) and one on the background, classify a new sequence by the log-likelihood ratio

$$
S(x) = \log_2\frac{\mathbb{P}(x \mid +)}{\mathbb{P}(x \mid -)} = \sum_{i}\log_2\frac{a^+_{x_{i-1}x_i}}{a^-_{x_{i-1}x_i}}, \tag{7.1}
$$
a sum of position scores, positive in favor of the class model; divided by the length, it is a score per base. This is the Neyman–Pearson test of [3.2.5](/3.2.5), and the per-base score is a **log-odds score** as in sequence alignment ([7.8.3](/7.8.3#sec-3.3.1)).

**Example 7.2.1 (CpG Island Models)** We estimated first-order transition matrices from human chromosome 21 inside the $446$ CpG islands of the UCSC Genome Browser (mean length $781$ bp) and outside them:

| + (islands) | A | C | G | T | | − (background) | A | C | G | T |
|---|---|---|---|---|---|---|---|---|---|---|
| A | $0.174$ | $0.295$ | $0.411$ | $0.119$ | | A | $0.332$ | $0.172$ | $0.234$ | $0.262$ |
| C | $0.156$ | $0.368$ | $0.294$ | $0.182$ | | C | $0.360$ | $0.248$ | $0.053$ | $0.339$ |
| G | $0.155$ | $0.347$ | $0.360$ | $0.138$ | | G | $0.296$ | $0.205$ | $0.249$ | $0.249$ |
| T | $0.075$ | $0.364$ | $0.363$ | $0.198$ | | T | $0.217$ | $0.201$ | $0.246$ | $0.335$ |

Rows are the preceding base. The decisive entry is C → G: $0.294$ in islands, $0.053$ outside, a log ratio of $\log_2(0.294/0.053) = 2.48$ bits, the largest of the sixteen; all transitions to C and G score positively, those to A and T negatively. The tables are close to the ones that Durbin and colleagues (1998) estimated from a much smaller set of human sequences. With Eq. (7.1) per base, $99.8\,\%$ of the islands score above $0$ and $94.8\,\%$ of random non-island segments of the same lengths score below $0$, with medians of $+0.31$ and $-0.31$ bits per base.

### 7.2.2. Segmentation with a Hidden Markov Model

Classification needs the boundaries of the candidate regions. In a genome we do not know where islands begin and end; we want to segment the sequence. A hidden Markov model does both at once: hidden states $\pi_i \in \{+, -\}$ follow a Markov chain with switching probabilities, and each state emits the next base according to its own transition matrix.

**Definition 7.2.1 (CpG Island HMM)** The two-state *CpG island hidden Markov model* has hidden states $+$ (island) and $-$ (background) with transition probabilities $\mathbb{P}(\pi_{i+1} = - \mid \pi_i = +) = \tau_+$ and $\mathbb{P}(\pi_{i+1} = + \mid \pi_i = -) = \tau_-$, and emission probabilities $\mathbb{P}(x_i \mid x_{i-1}, \pi_i = \pm) = a^{\pm}_{x_{i-1}x_i}$. The expected lengths of island and background segments are $1/\tau_+$ and $1/\tau_-$, and their length distributions are geometric.

The emissions depend on the previous base, a slight extension of the HMMs of [4.6.8](/4.6.8) in which an emission depends only on the current state; the forward, backward and Viterbi recursions are unchanged, with the emission probability $e_k(x_i)$ replaced by $a^k_{x_{i-1}x_i}$. Durbin and colleagues used an equivalent model with eight states (A+, C+, G+, T+, A−, …), each emitting its own base. Two decodings are useful.

- The **Viterbi algorithm** gives the single most probable state path, a segmentation into islands and background.
- *Posterior decoding* uses the forward variables $f_k(i) = \mathbb{P}(x_1 \cdots x_i, \pi_i = k)$ and backward variables $b_k(i) = \mathbb{P}(x_{i+1} \cdots x_L \mid \pi_i = k)$ to compute, at each position, $\mathbb{P}(\pi_i = + \mid x) = f_+(i)b_+(i)/\mathbb{P}(x)$, a confidence for every base.

The parameters can be estimated from annotated sequences by counting, as here, or from unannotated sequence by the Baum–Welch algorithm, an **EM algorithm** ([3.5.6](/3.5.6)) that alternates posterior decoding with re-estimation of the transition and emission probabilities from the expected counts.

**Example 7.2.2 (CpG Islands of the LCT–MCM6 Locus)** With the matrices of Example 7.2.1, $\tau_+ = 1/780$ and $\tau_- = 1/90\,000$ (the mean length of islands and the mean distance between them on chromosome 21), we computed posterior probabilities over the $200$ kb of chromosome 2 from $135.70$ to $135.90$ Mb (GRCh38), which contains *UBXN4*, *LCT* and *MCM6*. The two islands of the UCSC track, at the promoters of *UBXN4* and *MCM6*, are recovered over their whole lengths with posterior close to $1$. The promoter of *LCT*, a gene expressed only in the intestine, has no island; its regulation by an enhancer within *MCM6* is the subject of the lactase-persistence story ([7.8.8](/7.8.8)). Of the other $45$ segments with posterior above $0.5$, most are shorter than $200$ bp, and two of about $0.7$ kb within *LCT* are GC-rich ($62\,\%$) but have a CpG observed/expected ratio of only $0.28$–$0.39$: the first-order model rewards GC content as well as CpG. On $10$ Mb of chromosome 21 ($30$–$40$ Mb), the model touches all $78$ annotated islands and covers $95\,\%$ of their bases, but only $20\,\%$ of the bases it calls are in annotated islands; with a stricter switching probability $\tau_- = 10^{-7}$ and a minimum length of $200$ bp, the precision rises to $32\,\%$ while $95\,\%$ of island bases are still found. The annotation itself is a rule (GC content above $50\,\%$, observed/expected CpG ratio above $0.6$ over at least $200$ bp, after masking repeats), so "false positives" partly measure the difference between two definitions.

![Finding CpG islands with a two-state HMM in 200 kb of human chromosome 2 around *LCT* and *MCM6* (GRCh38 chr2:135.70–135.90 Mb). A: RefSeq genes (*UBXN4* on the plus strand, *LCT* and *MCM6* on the minus strand) and the CpG islands of the UCSC track (boxes). B: CpG observed/expected ratio in 500-bp windows (dashed line: 0.6). C: the posterior probability of the island state from the forward–backward algorithm, with first-order emission matrices estimated on chromosome 21 and switching probabilities 1/780 and 1/90 000. The islands at the promoters of *UBXN4* and *MCM6* have posterior close to 1 over their whole length; *LCT*, a tissue-specific gene, has no promoter island; the many short peaks and two GC-rich segments within *LCT* show the limits of a model that sees only adjacent bases](./plots/cpg-hmm.py)

### 7.2.3. A Hidden Markov Model of a Splice Site

The same machinery locates signals. A toy model of Eddy (2004), used in many courses, describes a stretch of DNA that starts in an exon and ends in an intron, with a 5′ splice site in between: an exon state E emits all bases with probability $0.25$, a one-base splice-site state 5 emits G with probability $0.95$ and A with $0.05$, and an intron state I emits A and T with $0.4$ each and C and G with $0.1$; E stays with probability $0.9$ and moves to 5 with $0.1$, 5 always moves to I, and I stays with $0.9$ and ends with $0.1$.

**Example 7.2.3** For the $26$-base sequence CTTCATGTGAAAGCAGACGTAAGTCA, every state path is EE…E5II…I, determined by the position of the splice-site state, which must be on a G or an A. The path with the splice site at the G in position $19$ has log-probability $\ln\mathbb{P}(x, \pi) = -41.22$, the largest. Summing over all $14$ admissible positions gives $\ln\mathbb{P}(x) = -40.45$, so the posterior probability of the splice site at position $19$ is $\mathrm{e}^{-41.22 + 40.45} = 0.46$, and at the G in position $23$ it is $0.28$. The Viterbi path is the best single answer, but the posterior says that the evidence is split between two candidates, information that the Viterbi path alone hides. For two bases AT with all of them from the exon or all from the intron (a common first exercise), the joint probabilities are $\ln(0.25 \times 0.9 \times 0.25) = -2.88$ and $\ln(0.4 \times 0.8 \times 0.4) = -2.06$ when the intron stays with probability $0.8$: AT is more probable as intron.

Real splice-site models use the position-specific base frequencies of thousands of sites ([7.8.8](/7.8.8)) rather than a single G.

## 7.3. Prokaryotic Gene Prediction

### 7.3.1. Open Reading Frames

Bacterial and archaeal genes are uninterrupted, and about $88\,\%$ of a typical bacterial genome codes for protein. A gene is an **open reading frame**: a run of **codons** from a **start codon** (mostly ATG, also GTG and TTG) to a **stop codon**, in one of the three **reading frames** of either strand. In random sequence, stops occur every $64/3 \approx 21$ codons on average, and long ORFs are improbable ([7.4.14](/7.4.14#fml-14.3.1)); real genes, a median of about $300$ codons long, stand out.

**Example 7.3.1 (ORFs in *E. coli*)** We listed, for every stop codon in all six frames of the *E. coli* genome, the ORF from the first ATG after the preceding in-frame stop, keeping those of at least $30$ codons, and did the same for the genome with its bases randomly permuted (same composition, no genes). The two genomes have similar numbers of short ORFs ($26\,147$ and $27\,378$ of at least $30$ codons), but the real genome has $5983$ ORFs of at least $100$ codons against $1074$ in the shuffled one, $3175$ against $19$ of at least $200$, and $2030$ against none of at least $300$. With the base frequencies of *E. coli*, the probability that a random codon is a stop is $0.0456$, a mean of $21.9$ codons between stops, and the shuffled ORFs fall off geometrically as expected. Of the real ORFs of at least $300$ codons, $93.6\,\%$ end at the stop codon of one of the $4297$ annotated protein-coding genes (median $274$ codons); of those of at least $100$ codons, only $62.6\,\%$ do. Length alone finds most long genes and fails for short ones, where coding statistics are needed.

![Open reading frames in the *E. coli* K-12 genome (blue), in the same genome with its bases randomly permuted (gray), and the lengths of the 4297 annotated protein-coding genes (orange), in 25-codon bins on a logarithmic scale. In the shuffled genome the number of ORFs falls off geometrically with length, as for random sequence, and no ORF reaches 300 codons; in the real genome, ORFs longer than about 200 codons are almost all annotated genes, while short ORFs are dominated by chance](./plots/orf-lengths.py)

### 7.3.2. Coding Statistics

Protein-coding sequence differs from noncoding sequence in ways that a Markov model can learn.

- Codon usage: synonymous codons are used unequally, and the preference varies between genomes and between highly and weakly expressed genes, which tend to use the codons read by abundant tRNAs.
- Amino acid composition and dipeptide frequencies, which make adjacent codons dependent.
- Three-base periodicity: base frequencies differ at the three codon positions, so the sequence repeats statistically with period $3$.

**Definition 7.3.1 (Codon Usage Bias)** **Codon usage bias** is the unequal use of the **synonymous codons** of an amino acid in a genome or gene. It is measured, for codon $c$ of an amino acid with $m$ synonymous codons, by the *relative synonymous codon usage* $\mathrm{RSCU}_c = m\,n_c/\sum_{c'}n_{c'}$, which is $1$ for uniform use, or for a whole gene by indices such as the codon adaptation index, the geometric mean of the RSCU of its codons relative to the most used codon of each amino acid in highly expressed reference genes (Sharp and Li 1987).

**Example 7.3.2** In the annotated genes of *E. coli* K-12, the six leucine codons are used with frequencies CTG $0.50$, TTG $0.13$, TTA $0.13$, CTC $0.10$, CTT $0.10$ and CTA $0.04$ (RSCU of CTG $2.99$, of CTA $0.22$), and the arginine codons CGC $0.40$, CGT $0.38$, CGG $0.10$, CGA $0.06$, AGA $0.035$ and AGG $0.020$. The rare arginine codons AGA and AGG correspond to rare tRNAs; human genes expressed in *E. coli* often stall at clusters of them, which is why expression strains carrying extra copies of these tRNA genes are used ([7.2](/7.2)). Base frequencies at the three codon positions of all genes are, for (A, C, G, T): position 1 $(0.25, 0.24, 0.35, 0.16)$, position 2 $(0.29, 0.23, 0.18, 0.30)$, position 3 $(0.18, 0.27, 0.29, 0.26)$; the excess of G at the first position reflects the frequency of amino acids encoded by G-starting codons (Gly, Ala, Val, Asp, Glu).

![The three-base periodicity of protein-coding DNA in *E. coli* K-12. A: base frequencies at the three codon positions of the 4297 annotated genes. B: power spectrum of the four base indicator sequences, averaged over 360-bp windows from every fourth gene (2252 windows) and from intergenic regions longer than 360 bp (746 windows), normalized by its median; coding windows have a sharp peak at frequency 1/3 (period 3 bp), 4.7 times the background level, intergenic windows a weaker one (2.3), contributed by unannotated or overlapping coding fragments](./plots/codon-periodicity.py)

The periodicity is the basis of a class of gene-detection methods that use the **discrete Fourier transform** of sequences; the Markov models below capture it directly, by using a different transition matrix at each codon position.

**Definition 7.3.2 (Periodic Markov Model)** A *three-periodic* (inhomogeneous) Markov model of order $k$ for coding sequence has three transition matrices $a^{(1)}, a^{(2)}, a^{(3)}$, one for each codon position; base $x_i$ at codon position $c(i)$ is drawn from $a^{(c(i))}_{x_{i-k}\cdots x_{i-1},\,x_i}$.

**Example 7.3.3 (A Coding Model for *E. coli*)** We trained three-periodic Markov models of orders $0$, $2$ and $5$ on a random half of the annotated *E. coli* genes and homogeneous models of the same order on the intergenic regions (both strands), and scored, by the log-likelihood ratio per codon, the $1891$ held-out genes of at least $100$ codons against the $2236$ unannotated ORFs of at least $100$ codons. The area under the ROC curve was $0.68$ for order $0$, $0.93$ for order $2$ and $0.95$ for order $5$. The unannotated ORFs are hard negatives: most lie on the opposite strand or in another frame of real genes, and inherit part of their statistics; $38\,\%$ of them still score above $0$ with the order-$5$ model. Gene finders reduce this by comparing all six frames at once and assigning each region to the frame with the best coding score.

### 7.3.3. Gene Finders for Prokaryotes

**Definition 7.3.3 (Gene Prediction)** **Gene prediction** is the identification of the positions and exon–intron structures of genes, above all protein-coding genes, in a genome sequence; *ab initio* prediction uses only the statistics of the sequence itself, *evidence-based* prediction also alignments of transcripts and proteins.

The main prokaryotic programs differ in how they model coding sequence and starts.

- *GeneMark* (Borodovsky and McIninch 1993) scores each frame with fifth-order periodic Markov models; *GeneMarkS* trains them on the genome itself by iteration (self-training), and *GeneMarkS-2* adds models for atypical genes acquired by horizontal transfer.
- *Glimmer* (Delcher, Salzberg and colleagues 1999) uses interpolated Markov models trained on long ORFs of the genome, which are almost all genes (Example 7.3.1).
- *Prodigal* (Hyatt and colleagues 2010) builds a dynamic program over all candidate starts and stops that maximizes a score combining coding statistics, GC frame bias, the ribosome binding site (**Shine–Dalgarno sequence**, about $8$ bp upstream of the start) and start-codon type, with all parameters learned from the genome; it is the standard in annotation pipelines (Prokka, Bakta, NCBI PGAP uses GeneMarkS-2) and in metagenomics.

Prokaryotic gene finders recover almost all genes of well-studied bacteria. The remaining problems are the exact start codons, the most frequent error, short genes of fewer than about $50$ codons, which are underpredicted, and genes with unusual composition.

```bash
# Prokaryotic gene prediction and annotation
prodigal -i genome.fa -a proteins.faa -d genes.fna -f gff -o genes.gff -p single
prodigal -i contigs.fa -a proteins.faa -p meta          # metagenome mode: no self-training
bakta --db bakta_db --output annot --prefix strain1 genome.fa   # genes, RNAs, functions
```

## 7.4. Eukaryotic Gene Structure and Generalized HMMs

### 7.4.1. The Problem

In eukaryotes, coding sequence is split into **exons** separated by **introns** (a median of $6.5$ exons per gene among the chromosome 21 genes of Example 7.4.1); coding sequence is only about $1.5\,\%$ of the human genome. A gene model must find the transcription start, the start codon, every **5′ splice site** and **3′ splice site**, the stop codon and the **polyadenylation signal**, and keep the reading frame across introns, where the intron phase (between codons or after the first or second base of a codon) must be consistent on both sides. The signals are weak: a splice site is defined by GT…AG and a few degenerate positions around them, which occur by chance thousands of times per gene.

**Example 7.4.1** In the $228$ curated protein-coding genes of RefSeq on human chromosome 21 (one transcript per gene, the longest), the $1711$ internal exons have a median length of $126$ bp (mean $143$; $80\,\%$ between $63$ and $217$ bp), and the $1883$ introns a median of $1.9$ kb, a mean of $6.1$ kb and a maximum of $339$ kb. Of the introns, $98.9\,\%$ begin with GT, $0.8\,\%$ with GC, and $99.8\,\%$ end with AG.

### 7.4.2. Generalized Hidden Markov Models

An HMM state with a self-transition generates segments with a geometric length distribution, whose mode is $1$. Exon lengths are not geometric: very short exons are rare (the spliceosome needs a minimal exon to assemble across it, [7.2](/7.2)) and the distribution peaks near $100$–$150$ bp. A model of genes therefore needs explicit length distributions.

**Definition 7.4.1 (Generalized Hidden Markov Model)** A **generalized hidden Markov model** (GHMM, or hidden semi-Markov model) is an HMM in which each visit to a state emits a whole segment: the state $k$ draws a duration $d$ from a length distribution $\phi_k(d)$ and then emits $d$ symbols from a segment model (for example a periodic Markov chain for coding states, a position weight matrix for a signal state), before moving to the next state by the transition probabilities.

**Algorithm 7.4.1 (Viterbi Decoding of a GHMM)** Let $V_k(i)$ be the probability of the best parse of $x_1 \cdots x_i$ whose last segment, of state $k$, ends at $i$. Then

$$
V_k(i) = \max_{d \le D}\ \max_{l}\ V_l(i - d)\,a_{lk}\,\phi_k(d)\,\mathbb{P}(x_{i-d+1} \cdots x_i \mid k),
$$
with traceback of the maximizing $(l, d)$; the time is $O(LDK^2)$ for $L$ positions, maximal duration $D$ and $K$ states.

The factor $D$ is prohibitive for introns of hundreds of kilobases. GENSCAN (Burge and Karlin 1997) made the GHMM practical: noncoding states (introns, intergenic regions) have geometric lengths and are handled like ordinary HMM states, while explicit length distributions are used only for exons, whose candidates are limited to segments between plausible signals (start, splice sites, stop) in an open frame. Its states are the exon types (initial, internal in three phases, terminal, single-exon), the introns in three phases, the promoter, the untranslated regions and the poly(A) signal, on both strands; exons are scored with fifth-order periodic Markov models and signals with position weight matrices and models of dependencies between splice-site positions. AUGUSTUS (Stanke and Waack 2003) extended the approach with better intron and splice-site models, species-specific training and, above all, the integration of external evidence as hints that modify the probabilities of the states.

![Length distributions of human internal exons (A) and introns (B), from the longest RefSeq transcript of each of the 228 curated protein-coding genes on chromosome 21 (GRCh38): 1711 internal exons with median 126 bp, and 1883 introns with median 1.9 kb on a logarithmic length axis. The geometric distribution of the same mean as the exons (red), which an ordinary HMM state with a self-transition would impose, has its mode at length 1 and misses the shape of the observed distribution, the reason for explicit length distributions in generalized HMMs](./plots/exon-intron-lengths.py)

### 7.4.3. Evidence and Pipelines

Ab initio predictors get most exons of a human gene right but whole genes much less often: the probability of predicting every exon and splice site of a ten-exon gene exactly is a product of many probabilities below $1$. Current annotation therefore combines several kinds of evidence.

- Transcripts: RNA-seq reads aligned to the genome with a spliced aligner ([7.8.10](/7.8.10)) show which regions are transcribed, and reads spanning exon junctions fix the splice sites to the base; full-length transcripts from long-read sequencing (PacBio Iso-Seq, Nanopore cDNA) give complete exon chains, including alternative isoforms and untranslated regions.
- Proteins: spliced alignment of known proteins from related species (Exonerate, GenomeThreader, miniprot) gives gene structures that are conserved.
- Conservation: protein-coding exons are conserved between species with a characteristic pattern (substitutions concentrated at third codon positions, insertions and deletions in multiples of three), which comparative gene finders such as TWINSCAN and CESAR exploit; conservation of noncoding elements is treated in [7.8.8](/7.8.8#sec-8.6).

Pipelines train the ab initio models on genes supported by evidence and then predict genome-wide with the evidence as hints: BRAKER (BRAKER3 uses both RNA-seq and proteins to train GeneMark-ETP and AUGUSTUS) and MAKER, which also integrates repeat masking and evidence alignment. For human and mouse, the reference annotations (GENCODE and RefSeq) are built mostly from transcript evidence with manual curation; they list about $20\,000$ protein-coding genes and a larger number of noncoding RNA genes, and still change with every release. Deep-learning predictors trained on many annotated genomes (Helixer, Tiberius) now reach the accuracy of evidence-based pipelines for some species from sequence alone; sequence models of this kind are treated in [7.8.15](/7.8.15). The complete annotation of a new genome is described in [7.8.11](/7.8.11).

```bash
# Ab initio prediction with a pre-trained species model, and evidence-based annotation
augustus --species=human --gff3=on genome.fa > augustus.gff3
braker.pl --genome=genome.masked.fa --prot_seq=orthodb_proteins.fa --bam=rnaseq.bam --threads 16
```

## 7.5. Evaluating Predictions

Predictions are compared with a reference annotation at three levels (Burset and Guigó 1996).

**Definition 7.5.1 (Accuracy of Gene Prediction)** With TP, FP and FN the numbers of true positives, false positives and false negatives at a given level (coding nucleotides; exons, counted as correct only if both boundaries are exact; or whole genes, correct only if all exons are), the sensitivity of a gene predictor is $\mathrm{TP}/(\mathrm{TP} + \mathrm{FN})$, the fraction of real features predicted, and its specificity is $\mathrm{TP}/(\mathrm{TP} + \mathrm{FP})$, the fraction of predictions that are real.

The "specificity" of gene prediction is what statistics calls the positive predictive value or precision, not the specificity of a diagnostic test (the fraction of negatives classified negative), because true negatives, all non-genic positions, are too numerous to be informative. Accuracy falls steeply from the nucleotide to the exon to the gene level, as the following example and Question 7 show. Completeness can also be measured without a reference annotation, by the fraction of near-universal single-copy orthologs (BUSCO) found in the predicted proteins ([7.8.11](/7.8.11)).

**Example 7.5.1** A predictor applied to a region with $40$ annotated exons predicts $45$ exons, of which $30$ match an annotated exon exactly. Exon sensitivity is $30/40 = 0.75$ and exon specificity $30/45 = 0.67$. If the region contains $5$ genes and only $1$ is predicted with all exons correct, gene sensitivity is $0.2$, although three quarters of the exons are right.

## 7.6. Numerical Representations of Sequences

Statistical and learning methods need sequences as numbers. The main encodings are:

- One-hot encoding: a sequence of length $L$ becomes an $L \times 4$ binary matrix (a **one-hot vector** per position), lossless and position-specific; it is the input of convolutional networks for regulatory sequence ([7.8.15](/7.8.15)).
- $k$-mer counts: the vector of the $4^k$ word frequencies, independent of position and of sequence length, used for composition signatures (Section 7.1.2), alignment-free comparison and metagenomic classification ([7.8.14](/7.8.14)).
- Indicator sequences and their Fourier transforms, as in the periodicity analysis above.
- Geometric representations, which map a sequence to a walk. The Z curve (Zhang and Zhang 1994) maps the prefix $x_1 \cdots x_n$ to the point with coordinates $x_n = (A_n + G_n) - (C_n + T_n)$, $y_n = (A_n + C_n) - (G_n + T_n)$, $z_n = (A_n + T_n) - (G_n + C_n)$, where $A_n, \dots$ are the base counts in the prefix: the three coordinates track purine–pyrimidine, amino–keto and weak–strong (AT–GC) imbalance, the curve determines the sequence uniquely, and its slopes show composition changes such as the GC skew of Section 7.1.1 (which is the slope of a related walk, $G_n - C_n$).
- Learned embeddings of $k$-mers or positions from language models of DNA and protein, in which similar contexts give similar vectors ([7.8.15](/7.8.15)).

The choice is a modeling decision: one-hot preserves everything but has no notion of similarity between positions; $k$-mer counts discard order beyond $k$ but are robust to insertions and to the absence of an alignment.

## Summary

| Topic | Key points |
|---|---|
| Composition | GC skew and its cumulative sum locate the origin and terminus of bacterial replication (Definition 7.1.1, Example 7.1.1: *E. coli* minimum at *oriC*, 3.926 Mb) |
| Words | dinucleotide ratio $\rho_{xy}$; CpG depleted fourfold in human ($0.28$ on chr21) by deamination of methylcytosine, not in *E. coli* (Example 7.1.2) |
| Markov models | order $k$, $3 \cdot 4^k$ parameters, counts as MLE (Definition 7.1.2); interpolated models |
| Classification | log-likelihood ratio of two models, Eq. (7.1); CpG island tables, C→G $2.5$ bits (Example 7.2.1) |
| Segmentation | two-state HMM with Markov emissions (Definition 7.2.1); Viterbi and posterior decoding; *UBXN4* and *MCM6* promoter islands found, none at *LCT*; precision limited by GC-rich segments (Example 7.2.2); splice-site HMM, posterior $0.46$ versus Viterbi (Example 7.2.3) |
| Prokaryotic genes | ORFs: real versus shuffled *E. coli* $2030$ versus $0$ of ≥ 300 codons (Example 7.3.1); codon usage bias, RSCU (Definition 7.3.1, Example 7.3.2); three-base periodicity; periodic Markov models (Definition 7.3.2), AUC $0.68 \to 0.95$ from order 0 to 5 (Example 7.3.3); GeneMark, Glimmer, Prodigal (Definition 7.3.3) |
| Eukaryotic genes | split genes, weak signals, intron phases; human exons median $126$ bp, introns $1.9$ kb, GT–AG $99\,\%$ (Example 7.4.1); GHMM with explicit durations (Definition 7.4.1, Algorithm 7.4.1); GENSCAN, AUGUSTUS; evidence from RNA-seq, long reads, proteins and conservation; BRAKER, MAKER; deep-learning predictors |
| Evaluation | sensitivity and "specificity" (= precision) at nucleotide, exon and gene levels (Definition 7.5.1, Example 7.5.1); BUSCO completeness |
| Representations | one-hot, $k$-mer counts, Fourier, Z curve, embeddings |

## Questions

1. Under an order-$0$ model with base frequencies $0.3$ (A, T) and $0.2$ (C, G), compute the expected number of occurrences of the $6$-mer GAATTC (the *Eco*RI site) in a genome of $4.6$ Mb, counting both strands, and the expected distance between sites.

   **Answer** $\mathbb{P}(\mathrm{GAATTC}) = 0.2 \times 0.3^4 \times 0.2 = 0.2^2 \times 0.3^4 = 0.04 \times 0.0081 = 3.24\times10^{-4}$. The site is its own reverse complement (a palindrome), so occurrences on the two strands coincide: the expected number is $4.6\times10^6 \times 3.24\times10^{-4} = 1490$, one every $3.1$ kb on average (with equal base frequencies, $4^{-6}$ gives one every $4.1$ kb). Observed counts in bacterial genomes deviate from such expectations because restriction sites are selected against in genomes of bacteria and phages exposed to the corresponding enzymes.

2. Why is a fifth-order Markov model natural for coding sequence, and how many parameters does a three-periodic fifth-order model have? What problem appears for a ninth-order model trained on a bacterial genome?

   **Answer** Five preceding bases span the previous codon and part of the current one, so the model captures codon usage and dependencies between adjacent codons (dipeptide preferences). Each of the three position-specific matrices has $4^5 = 1024$ contexts with $3$ free probabilities: $3 \times 3072 = 9216$ parameters. A bacterial genome has about $4\times10^6$ coding bases, roughly $430$ per parameter. A ninth-order model has $3 \times 3 \times 4^9 = 2.4\times10^6$ parameters, about $1.7$ coding bases per parameter: most contexts are seen a few times or never, and the estimates overfit. Interpolated Markov models solve this by using long contexts only where they have been observed often enough.

3. In Example 7.2.1, compute the log-likelihood ratio (bits) of the dinucleotide sequence CGCG (three transitions) under the island and background models, and of TGCA.

   **Answer** CGCG has transitions C→G, G→C, C→G: $\log_2(0.294/0.053) + \log_2(0.347/0.205) + \log_2(0.294/0.053) = 2.47 + 0.76 + 2.47 = 5.70$ bits in favor of the island model. TGCA: T→G $\log_2(0.363/0.246) = 0.56$, G→C $0.76$, C→A $\log_2(0.156/0.360) = -1.21$, total $0.11$ bits, almost neutral. A single CpG contributes as much as four or five other favorable steps, which is why the model is dominated by CpG density.

4. In the CpG island HMM, what expected segment lengths correspond to $\tau_+ = 1/780$ and $\tau_- = 1/90\,000$? Explain why making $\tau_-$ smaller reduced the number of called segments in Example 7.2.2.

   **Answer** Geometric lengths with means $1/\tau_+ = 780$ bp for islands and $1/\tau_- = 90\,000$ bp between islands. Entering an island costs $\log_2\tau_-$ bits and leaving it $\log_2\tau_+$ bits; a short CpG-rich stretch is called an island only if its emission log-likelihood ratio exceeds this cost. With $\tau_- = 1/90\,000$ the entry costs $16.5$ bits, with $10^{-7}$ it costs $23.3$ bits, so a stretch must gain about $7$ more bits from its bases, equivalent to three more CpGs; short and weakly enriched stretches no longer qualify, and the number of segments on $10$ Mb fell from $1714$ to $741$.

5. In Example 7.2.3, verify the log-probability of the path with the splice-site state at position 19, given that the first $18$ bases are emitted by E, the G at $19$ by 5, and the last $7$ bases (TAAGTCA) by I.

   **Answer** Exon part: $18$ emissions of $0.25$ and $17$ transitions E→E of $0.9$: $18\ln0.25 + 17\ln0.9 = -24.953 - 1.791 = -26.744$. Transition E→5 ($0.1$): $-2.303$; emission of G by 5 ($0.95$): $-0.051$; transition 5→I ($1$): $0$. Intron: emissions T, A, A, G, T, C, A with probabilities $0.4, 0.4, 0.4, 0.1, 0.4, 0.1, 0.4$: $5\ln0.4 + 2\ln0.1 = -4.581 - 4.605 = -9.187$; six transitions I→I ($0.9$): $-0.632$; the end transition ($0.1$): $-2.303$. Total $-26.744 - 2.303 - 0.051 - 9.187 - 0.632 - 2.303 = -41.22$.

6. Why are the unannotated long ORFs of Example 7.3.3 "hard negatives", and how does a gene finder that compares frames avoid them?

   **Answer** An ORF overlapping a real gene in another frame or on the opposite strand consists of the same bases, read with a shift; since codon positions have different composition (position 1 G-rich, position 2 T-rich), the shifted reading still deviates from noncoding statistics, and a reverse-complement reading inherits a complementary codon structure, so it can resemble coding sequence more than intergenic DNA does. Comparing it with a noncoding model is the wrong test; the right one compares the six frames with each other. GeneMark computes, at each position, the posterior probability of coding in each frame and of noncoding, and the real frame wins clearly over its shadows; Prodigal similarly chooses non-overlapping genes by dynamic programming over all frames, allowing only small overlaps.

7. A gene has $12$ exons. If an ab initio predictor finds each exon exactly with probability $0.8$, independently, what is the probability that the whole gene is correct? What does this imply for the use of evidence?

   **Answer** $0.8^{12} = 0.069$: only about $7\,\%$ of such genes would be fully correct, although $80\,\%$ of exons are. Errors are not independent in reality (a missed exon shifts the frame and corrupts neighbors), but the product shows why gene-level accuracy is low. Each piece of external evidence that fixes splice sites (spliced RNA-seq reads, full-length transcripts, protein alignments) raises the per-exon accuracy close to $1$, and the gene-level accuracy rises much faster, which is why annotation pipelines rely on evidence.

8. Compute the relative synonymous codon usage of the six leucine codons in Example 7.3.2. Which codon would you avoid when designing a synthetic gene for high expression in *E. coli*, and why is codon optimization not simply "use the most frequent codon everywhere"?

   **Answer** $\mathrm{RSCU} = 6 \times$ frequency: CTG $2.99$, TTG $0.77$, TTA $0.77$, CTC $0.63$, CTT $0.62$, CTA $0.22$. CTA, the rarest, should be avoided (as should the arginine codons AGA and AGG). Using only the most frequent codon can deplete its charged tRNA when the protein is highly expressed, removes the slower codons that help co-translational folding at domain boundaries, creates repetitive sequence that recombines or forms secondary structure (especially near the start codon, where mRNA folding strongly affects initiation), and may introduce unwanted motifs; design tools therefore match the codon distribution of highly expressed genes and optimize mRNA structure near the ribosome binding site.

9. A new bacterial genome has a cumulative GC skew without a clear minimum and maximum. Give two biological reasons, and an alternative way to locate the origin.

   **Answer** Reasons: the skew is weak in some lineages (for example where replication-associated mutational asymmetry is small or genes are not strongly oriented), and large inversions or recent rearrangements spanning the origin or terminus flip the strand of part of a replication arm, producing several minima; a genome with multiple origins (as in archaea such as *Sulfolobus*) or an assembly that is fragmented or wrongly joined also breaks the pattern. Alternatives: search for DnaA boxes (the 9-bp binding sites of the initiator protein, clustered at *oriC*) near the *dnaA* gene, look for the conserved gene order around the origin (*dnaA*, *dnaN*, *recF*, *gyrB*), or measure it experimentally by marker frequency analysis, sequencing a growing culture and finding the region of highest coverage, since regions near the origin are replicated first.

10. (Design) You have assembled the genome of a non-model insect and have RNA-seq from three tissues but no close relative with a curated annotation. Describe how you would annotate its protein-coding genes and how you would assess the result.

    **Answer** First identify and soft-mask repeats (RepeatModeler and RepeatMasker), since transposable elements contain ORFs that would be predicted as genes ([7.8.11](/7.8.11)). Align the RNA-seq reads with a spliced aligner and the proteins of a broad database of arthropod orthologs (OrthoDB) with a spliced protein aligner. Run an evidence-based pipeline (BRAKER3 with both kinds of evidence) that trains GeneMark and AUGUSTUS on genes supported by evidence and predicts genome-wide with hints; optionally add long-read transcripts to define complete isoforms and untranslated regions. Assess completeness with BUSCO on the predicted proteins (fraction of single-copy insect orthologs complete, fragmented, duplicated or missing), the fraction of RNA-seq reads and junctions explained by the models, the agreement of predicted proteins with homologs over their full length, the distributions of exon and intron lengths and exon numbers compared with related species (Example 7.4.1), and the proportion of genes without any evidence, which should be small and inspected for repeats or pseudogenes.
