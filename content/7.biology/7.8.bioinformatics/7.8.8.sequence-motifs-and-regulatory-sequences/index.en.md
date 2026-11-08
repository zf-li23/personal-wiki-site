---
title: Sequence Motifs and Regulatory Sequences
description: "Short sequence patterns recognized by proteins and RNAs: consensus sequences and IUPAC codes; position frequency and weight matrices with pseudocounts, sequence logos and information content (with the small-sample correction), the expected PWM score as relative entropy; scanning genomes, exact p-values by convolution, thresholds and false positives (the CTCF matrix), and the lactase-persistence enhancer scanned with the Oct-1 matrix; de novo motif discovery by word enrichment, expectation maximization (MEME's OOPS, ZOOPS and TCM models) and Gibbs sampling; motif databases (JASPAR, HOCOMOCO, CIS-BP) and comparison; phylogenetic footprinting, phastCons and phyloP; splice sites, polyadenylation and translation signals; practice with the MEME suite and HOMER."
---

Transcription factors, splicing factors, RNA-binding proteins and ribosomes find their targets by reading short stretches of sequence. These targets are not fixed words: the sites of one transcription factor differ from each other at many positions, they are short (often $6$ to $20$ bp) and they occur, in weaker versions, everywhere in a genome. A sequence motif is the statistical description of such a family of sites. This chapter describes how motifs are represented (consensus sequences, matrices and logos), how a known motif is used to search genomes and what the scores mean statistically, how unknown motifs are discovered in sets of sequences that share a regulator, and how evolutionary conservation, the second great source of evidence for functional sequence, is measured. The biophysics of recognition was treated in biophysics: the energy-matrix model of protein–DNA binding in [7.6.17](/7.6.17#sec-17.7.3), and the selection theory that relates the frequencies of bases in sites to their binding energies (the Berg–von Hippel relation) and the problem of finding sites among decoys in [7.6.41](/7.6.41#sec-41.3). Here we take the statistical view, with the methods used in practice. The data on which motifs are discovered today, ChIP-seq and ATAC-seq peaks, and the analysis of motif accessibility across cells belong to systems biology ([7.9](/7.9)); deep-learning models that read regulatory sequence and discover motifs from their internal representations are in [7.8.15](/7.8.15). The running example is the lactase-persistence variant rs4988235 of the course, which lies in an enhancer of *LCT* inside *MCM6*: we scan its neighborhood with the matrix of the transcription factor Oct-1.

## 8.1. Motifs and Consensus Sequences

**Definition 8.1.1 (Sequence Motif)** A **sequence motif** is a short pattern of nucleotides or amino acids shared by a family of functionally equivalent sites, such as the binding sites of a transcription factor, the splice sites of introns or the phosphorylation sites of a kinase, described by a rule or a probability model that assigns each candidate sequence a degree of match.

In molecular biology "motif" also denotes a recurring structural element of proteins (a supersecondary structure, [7.1](/7.1)) and, in systems biology, a recurring pattern of interactions in networks ([7.9](/7.9)); this chapter concerns sequence motifs only. The simplest representation is the **consensus sequence** ([7.1.4](/7.1.4#sec-4.4.2)), the most frequent base at each position, written with the IUPAC codes for degenerate positions:

| Code | Bases | Code | Bases | Code | Bases |
|---|---|---|---|---|---|
| R | A or G (purine) | K | G or T | B | not A |
| Y | C or T (pyrimidine) | M | A or C | D | not C |
| S | C or G (strong) | W | A or T (weak) | H | not G |
| N | any base | | | V | not T |

A consensus with degeneracy rules (for example "at most one mismatch") is easy to search and to communicate: TATAAT for the $-10$ element of bacterial σ70 promoters, TGANTCA for the AP-1 site. But it discards information in two ways. It treats all matches equally, although sites differ in strength, and it treats all mismatches equally, although at some positions a substitution reduces binding slightly and at others it abolishes it. Real sites rarely match the consensus exactly: most functional σ70 promoters have two or more mismatches in their $-10$ and $-35$ elements, because a perfect promoter would bind RNA polymerase too strongly to be regulated or escaped ([7.2](/7.2)). A probabilistic representation is needed.

## 8.2. Matrices and Logos

### 8.2.1. Position Frequency and Weight Matrices

**Definition 8.2.1 (Position Frequency Matrix)** For a set of $N$ aligned sites of length $L$, the **position frequency matrix** (PFM) is the $L \times 4$ matrix of counts $n_{jb}$ of base $b$ at position $j$ (or of the frequencies $n_{jb}/N$). Treated as a probability model, it assumes that positions are independent, with base $b$ at position $j$ having probability $p_{jb}$.

The matrix becomes a scoring rule by comparing the motif model with a background model $q$ (the base frequencies of the genome, or a higher-order Markov model as in [7.8.7](/7.8.7#sec-7.1.3)).

**Formula 8.2.1 (Position Weight Matrix)** With a pseudocount $\beta$ distributed in proportion to the background, the probabilities and weights are

$$
p_{jb} = \frac{n_{jb} + \beta q_b}{N + \beta}, \qquad W_{jb} = \log_2\frac{p_{jb}}{q_b}, \tag{8.1}
$$
and the score of a candidate site $x_1 \cdots x_L$ is $S(x) = \sum_jW_{jx_j}$, the log-likelihood ratio (in bits) of the motif model against the background.

This is the **position weight matrix** (PWM) of [7.6.17](/7.6.17#sec-17.7.3), estimated from sites; it is the DNA analogue of the position-specific scoring matrix of protein families ([7.8.5](/7.8.5#sec-5.4.1)). Under the Berg–von Hippel relation ([7.6.41](/7.6.41#sec-41.3.2)), $W_{jb}$ is proportional to minus the binding energy of base $b$ at position $j$ relative to the consensus, so the score of a site estimates its affinity up to a scale factor. The pseudocount prevents $\log 0$: a base never seen among $10$ sites is unlikely but not impossible. JASPAR recommends $\beta = 0.8$, a choice that is reasonable for tens to hundreds of sites; with thousands of sites its effect is negligible.

**Example 8.2.1** Eight invented sites of a $6$-bp motif, TATAAT, TATGAT, TACAAT, TATAAT, GATAAT, TATACT, TATAAT and TAAAAT, give the counts (rows A, C, G, T; columns positions 1 to 6) A $(0, 8, 1, 7, 7, 0)$, C $(0, 0, 1, 0, 1, 0)$, G $(1, 0, 0, 1, 0, 0)$, T $(7, 0, 6, 0, 0, 8)$. With a uniform background ($q_b = 0.25$) and $\beta = 0.5$, a base seen $8$ times gets $p = 8.125/8.5 = 0.956$ and weight $\log_2(0.956/0.25) = 1.93$ bits, a base seen $7$ times $1.75$, once $-0.92$ and never $-4.09$. The consensus TATAAT scores $10.63$ bits, the maximum; TAGAAT, with the never-seen G at position 3, scores $5.02$; TATGTT, with a G at position 4 (seen once) and a T at position 5 (never seen), $2.14$. The consensus representation would treat TAGAAT and the observed site TACAAT alike (one mismatch each), while the matrix distinguishes an unseen substitution (G, $5.02$ bits) from a tolerated one (C, seen once, $8.19$ bits).

### 8.2.2. Sequence Logos and Information Content

A **sequence logo** (Schneider and Stephens 1990; introduced in [7.1.4](/7.1.4)) displays a matrix as stacks of letters, one stack per position, whose total height is the information content of the position and whose letters are scaled by their frequencies.

**Definition 8.2.2 (Information Content of a Motif Position)** The **information content** of position $j$ of a DNA motif estimated from $N$ sites with frequencies $f_{jb}$ is

$$
R_j = 2 - (H_j + e_N), \qquad H_j = -\sum_bf_{jb}\log_2f_{jb}, \qquad e_N = \frac{3}{2N\ln2}, \tag{8.2}
$$
in bits, where $H_j$ is the Shannon entropy of the position and $e_N$ corrects for the downward bias of entropy estimated from $N$ sequences (Schneider and colleagues 1986). The information content of the motif is $R = \sum_jR_j$. For proteins, $2$ is replaced by $\log_220 = 4.32$ bits and the correction by $19/(2N\ln2)$.

The maximum, $2$ bits for DNA, is reached by a position at which one base always occurs; a position with uniform frequencies has $0$ bits. The correction term is the leading term of the bias of the plug-in entropy, $(s - 1)/(2N\ln2)$ for $s$ letters, and matters for small sets: for $N = 8$ it is $0.27$ bits per position. The conservation of a protein position is likewise at most $4.32$ bits, the height of a fully conserved column of a protein logo ([7.1.4](/7.1.4#sec-4.4.2)). A variant of the definition measures the relative entropy $\sum_bf_{jb}\log_2(f_{jb}/q_b)$ to a nonuniform background, which is larger for positions conserved for a base that is rare in the genome.

**Example 8.2.2** In Example 8.2.1, positions 2 and 6 are invariant ($H = 0$, $R = 2 - 0.27 = 1.73$ bits), positions 1, 4 and 5 have frequencies $7/8$ and $1/8$ ($H = 0.54$, $R = 1.19$), and position 3 has $6/8, 1/8, 1/8$ ($H = 1.06$, $R = 0.67$); the motif carries $R = 7.68$ bits. The JASPAR matrix of CTCF (MA0139.1), estimated from $913$ sites in ChIP-seq peaks of human cells, has $19$ positions with $0.14$ to $1.92$ bits each and $17.2$ bits in total ($e_N = 0.002$).

![The binding motif of the insulator protein CTCF as a logo and a weight matrix (JASPAR MA0139.1, 913 sites from ChIP-seq peaks in human cells). A: sequence logo; the height of each stack is the information content R = 2 − (H + e_N) of the position, letters are scaled by their frequencies, and the motif carries 17.2 bits. B: the position weight matrix log₂[(n + 0.8q)/(N + 0.8)/q] in bits, with the human background q = (0.295, 0.205, 0.205, 0.295) for A, C, G, T; the consensus base of each position has the largest weight, and bases never observed (C at positions 10 and 13, G at position 5) receive large negative weights that the pseudocount keeps finite](./plots/ctcf-logo-pwm.py)

**Theorem 8.2.1 (Expected PWM Scores)** For a PWM $W_{jb} = \log_2(p_{jb}/q_b)$ with motif model $p$ and background $q$, the expected score of a site drawn from the motif model is the relative entropy

$$
\mathbb{E}_p[S] = \sum_j\sum_bp_{jb}\log_2\frac{p_{jb}}{q_b} = \sum_jD(p_j \Vert q) \ge 0,
$$
and the expected score of a background window is $\mathbb{E}_q[S] = -\sum_jD(q \Vert p_j) \le 0$.

**Proof** By linearity of expectation over independent positions, $\mathbb{E}_p[S] = \sum_j\mathbb{E}_p[W_{jx_j}] = \sum_j\sum_bp_{jb}W_{jb}$, which is the sum of **Kullback–Leibler divergences** $D(p_j \Vert q)$; similarly $\mathbb{E}_q[S] = \sum_j\sum_bq_b\log_2(p_{jb}/q_b) = -\sum_jD(q \Vert p_j)$. Both divergences are nonnegative by Gibbs' inequality. $\square$

The information content of a motif therefore measures how well its sites can be distinguished from background: for the CTCF matrix with the human background, the expected score of a site is $19.1$ bits and that of a random window $-32.6$ bits. Schneider and colleagues (1986) observed that for many bacterial factors the information content of the sites, $R_{\mathrm{sequence}}$, is close to $R_{\mathrm{frequency}} = \log_2(G/\gamma)$, the information needed to pick $\gamma$ sites out of $G$ possible positions ([7.6.41](/7.6.41#sec-41.3.2)). For CTCF, with $2 \times 3.1\times10^9$ positions on both strands of the human genome and of the order of $5\times10^4$ sites, $\log_2(6.2\times10^9/5\times10^4) = 16.9$ bits, close to the $17.2$ bits of its motif; for most eukaryotic factors, with motifs of $8$ to $12$ bits, the sites are far less specific than this argument requires, and chromatin, cooperativity and clustering supply the rest.

## 8.3. Scanning Genomes

### 8.3.1. Scores and p-Values

To find candidate sites, each window of length $L$ on both strands is scored with the PWM, and windows above a threshold are reported. The threshold should be set by the probability that a background window scores as high, which the score itself does not show: $10$ bits is a strong match for a $6$-bp motif and a weak one for a $19$-bp motif. Because positions are independent under both models, the exact distribution of the score of a random window can be computed.

**Algorithm 8.3.1 (Exact Score Distribution of a PWM)** Round the weights to integers on a fine grid, $\tilde W_{jb} = \operatorname{round}(cW_{jb})$ (for example $c = 100$ per bit). Let $P_0$ be the distribution concentrated at $0$; for $j = 1, \dots, L$,

$$
P_j(s) = \sum_bq_b\,P_{j-1}\left(s - \tilde W_{jb}\right),
$$
a convolution over the four bases. $P_L$ is the distribution of the score of a background window; its upper tail gives the p-value of every score, and the same recursion with $p_{jb}$ in place of $q_b$ gives the score distribution of sites drawn from the motif model. The time is $O(L \cdot 4 \cdot c\,\Delta)$, with $\Delta$ the range of the scores in bits.

This is the method of Staden (1989), used by FIMO of the MEME suite (Grant, Bailey and Noble 2011) with a background estimated from the sequences, and refined by algorithms that compute p-values without fixing the grid (Touzet and Varré 2007). Since scores of overlapping windows are dependent, the expected number of matches above a threshold is still $p$ times the number of windows, but their count is not binomial.

**Example 8.3.1 (Scanning a Genome with the CTCF Matrix)** For the CTCF PWM of the logo figure and the human background, the exact background distribution gives the thresholds $7.26$, $12.43$ and $16.67$ bits for p-values $10^{-4}$, $10^{-5}$ and $10^{-6}$. A genome of $3.1$ Gb scanned on both strands contains $6.2\times10^9$ windows, so the expected numbers of chance matches above these thresholds are $6.2\times10^5$, $6.2\times10^4$ and $6.2\times10^3$, while sites drawn from the motif model exceed them with probabilities $0.98$, $0.91$ and $0.72$. Even the strictest threshold leaves thousands of chance matches, of the order of the number of real sites, and costs more than a quarter of the real ones. A genome-wide scan with a PWM predicts where a factor *could* bind; in any cell, only a small fraction of matches is bound, depending on chromatin accessibility, cooperating factors and DNA methylation (CTCF does not bind sites whose central CpG is methylated).

![Scanning with a position weight matrix. A: the exact distribution of the CTCF PWM score of a random 19-bp window (gray, human background) and of a site drawn from the motif model (blue), computed by convolution over positions (Algorithm 8.3.1), on a logarithmic scale; dashed lines are the thresholds with background p-values 10⁻⁴, 10⁻⁵ and 10⁻⁶ (7.3, 12.4 and 16.7 bits). B: as the threshold rises, the expected number of chance matches in a 3.1-Gb genome scanned on both strands (red, logarithmic left axis) falls by a factor of 10 for every 4 to 5 bits, while the fraction of motif-model sites above the threshold (green, right axis) falls slowly at first and then steeply: no threshold separates real sites from chance matches in a whole genome](./plots/score-threshold.py)

When thousands of sequences are scanned, p-values are converted into q-values with the **false discovery rate** procedures (the **Benjamini–Hochberg procedure**, or Storey's q-values, as FIMO reports), but the FDR controls only the statistical error of declaring a background window a match, not the biological error of declaring an unbound match a binding site.

### 8.3.2. The Lactase-Persistence Enhancer

The derived allele of rs4988235, $-13910\mathrm{T}$ on the strand of *LCT*, lies in an enhancer within intron 13 of *MCM6*, $13.9$ kb upstream of *LCT* ([7.8.2](/7.8.2)). In reporter assays the T allele increases the activity of the *LCT* promoter, and DNA-binding experiments have identified the transcription factor Oct-1 (POU2F1) as binding to this region, more strongly to the T allele. What does a PWM scan say?

**Example 8.3.2** We scanned the $101$ bp of GRCh38 chromosome 2 centered on rs4988235 with the JASPAR matrix of POU2F1 (MA0785.1, $12$ bp, octamer-like consensus AATATGCAAATT; maximum score $16.0$ bits with the human background and $\beta = 0.8$). The best window containing the variant is read on the minus strand, ATAATGTAG(C/T)CC: it scores $-5.35$ bits with the ancestral C and $-3.79$ bits with the derived T, an increase of $1.56$ bits, because at position $10$, where the matrix strongly prefers A, a T is less disfavored than a C. Both scores are low (p-values about $0.04$ in random sequence); the strongest Oct-1 match of the region, ATTATACAAATG ($9.42$ bits), lies $46$ bp upstream and is not affected by the variant. A single-matrix scan thus captures the direction of the effect but not its magnitude: binding in the cell depends on the flanking sequence, on cooperating factors at the enhancer, and on the protein preparation and context of the experiment; variant-effect predictors trained on chromatin data ([7.8.15](/7.8.15)) and direct measurements of allele-specific binding are the better tools for regulatory variants ([7.8.12](/7.8.12)).

![Scanning the lactase-persistence enhancer with a PWM. A: the score of every 12-bp window of the 101 bp around rs4988235 (GRCh38 chr2:135,851,026–135,851,126) under the JASPAR POU2F1 (Oct-1) matrix MA0785.1, maximum over the two strands, for the ancestral (G on the forward strand, −13910C on the strand of *LCT*) and derived sequences; only the windows containing the variant (shaded) change. B: the best window covering the variant, read on the minus strand, under the logo of the matrix; the derived T at position 10, where A is preferred, raises the score by 1.6 bits, but both alleles score far below the strongest site of the region (ATTATACAAATG, 46 bp away, 9.4 bits) and the matrix maximum (16.0 bits)](./plots/lactase-enhancer.py)

## 8.4. De Novo Motif Discovery

### 8.4.1. The Problem

Given a set of sequences believed to share a regulator (the promoters of coregulated genes, the $100$ bp at the summits of ChIP-seq peaks, sequences selected in vitro), find the motif they share. This is *motif discovery*: in its combinatorial form, finding a word of length $L$ that occurs in every sequence with at most $d$ mismatches (the planted motif problem) is NP-hard, and the statistical versions are solved heuristically. Three families of methods are used.

### 8.4.2. Word Enrichment

The simplest approach counts words. For every $k$-mer (or every degenerate word over IUPAC codes), compare the number of target sequences that contain it with the number of background sequences that do, and test the excess with the **hypergeometric distribution** (Fisher's exact test). Exhaustive counting of all $4^k$ words is fast for $k \le 12$ and finds strong motifs reliably; the best words are then extended and turned into matrices.

**Example 8.4.1** An $8$-mer occurs in $300$ of $1000$ ChIP-seq peak sequences and in $200$ of $5000$ background sequences with matched GC content. The odds ratio is $(300 \times 4800)/(700 \times 200) = 10.3$, and the hypergeometric probability of at least $300$ occurrences among $1000$ sequences drawn from $6000$ of which $500$ contain the word is $1.7\times10^{-119}$. Since about $4^8/2 = 32\,768$ distinct words (up to reverse complement) were tested, a Bonferroni correction multiplies this by $3\times10^4$, without changing the conclusion.

HOMER (Heinz and colleagues 2010) and STREME (Bailey 2021) work this way, with refinements: STREME builds its candidate words with a suffix tree, tests them on held-out sequences and refines them into PWMs, and both use background sequences matched in GC content, without which GC-rich peaks would make every GC-rich word look enriched.

### 8.4.3. Expectation Maximization

If we knew where the site is in each sequence, the matrix would be estimated by counting; if we knew the matrix, we could compute where the sites probably are. The **EM algorithm** ([3.5.6](/3.5.6)) alternates the two, treating the site positions as missing data (Lawrence and Reilly 1990; MEME, Bailey and Elkan 1994).

**Algorithm 8.4.1 (EM for One Occurrence per Sequence)** Given $N$ sequences of length $M$, a motif length $L$, a background $q$, and an initial matrix $p$:

1. *E step.* For each sequence $i$ and each start position $k = 1, \dots, M - L + 1$, compute the likelihood ratio of a site at $k$, $\mathrm{LR}_{ik} = \prod_{j=1}^{L}p_{j,x_{i,k+j-1}}/q_{x_{i,k+j-1}}$, and the posterior probability $z_{ik} = \mathrm{LR}_{ik}/\sum_{k'}\mathrm{LR}_{ik'}$ that the site of sequence $i$ starts at $k$ (assuming a uniform prior over positions).
2. *M step.* Re-estimate the matrix from the expected counts: $n_{jb} = \sum_i\sum_kz_{ik}\boldsymbol{1}[x_{i,k+j-1} = b]$, and $p_{jb} = (n_{jb} + \beta q_b)/(N + \beta)$.
3. Repeat until the log-likelihood $\sum_i\log\frac{1}{M - L + 1}\sum_k\mathrm{LR}_{ik}$ (relative to the background) stops increasing.

Each iteration takes $O(NML)$ time and cannot decrease the likelihood, but EM converges to a local maximum that depends on the start. MEME therefore starts from many matrices derived from substrings of the data, runs a single iteration from each, and continues only from the best. Three models of how sites are distributed are offered: OOPS (one occurrence per sequence), ZOOPS (zero or one, with an additional parameter $\gamma$ for the fraction of sequences that contain a site) and TCM or ANR (any number of repetitions, a two-component mixture over all positions). Once a motif is found, its sites are down-weighted (erased) and the search is repeated for further motifs.

**Example 8.4.2** We simulated $25$ random sequences of $150$ bp with human base frequencies, each with one site of length $19$ drawn from the CTCF matrix at a random position, and ran OOPS EM starting from each $19$-mer of the first sequence (initial matrix: probability $0.3$ for the base of the $19$-mer and $0.233$ for each other base). After one iteration from every start, the five best were iterated to convergence. The best run converged in $6$ iterations, with the log-likelihood ratio rising from $10.3$ to $330.8$ bits, and the most probable position in each sequence was the planted site for all $25$ sequences; the estimated logo matches the planted one. With a sharper initial matrix (probability $0.5$ on the start word), the best start was a word overlapping the site in sequence 1 shifted by one base, and EM converged to the motif shifted by one position, a local optimum that MEME escapes by trying shifted versions of each matrix.

![De novo motif discovery by expectation maximization (OOPS model) on simulated data: 25 random sequences of 150 bp (human base frequencies), each with one 19-bp site drawn from the CTCF matrix. EM was started from every 19-mer of the first sequence, run for one iteration from each, and the five best starts were iterated to convergence. A: the log-likelihood ratio of the data under the motif model against the background over the iterations of the best run. B: the posterior probability of the site position in sequence 1 at the start, after one and three iterations and at convergence (dashed line: the planted site). C: the logo of the 25 planted sites. D: the logo of the expected counts at convergence; all 25 sites are recovered](./plots/em-motif.py)

### 8.4.4. Gibbs Sampling

The **Gibbs sampler** ([3.5.9](/3.5.9)) replaces the expected positions by sampled ones (Lawrence and colleagues 1993).

**Algorithm 8.4.2 (Gibbs Sampling for Motif Discovery)** Choose a random start position $a_i$ in every sequence. Repeat:

1. Choose one sequence $i$ (in turn or at random) and estimate the matrix $p$ with pseudocounts from the sites $a_{i'}$ of all other sequences.
2. For every position $k$ of sequence $i$, compute the likelihood ratio $\mathrm{LR}_{ik}$ of a site at $k$ under $p$ against the background.
3. Draw a new $a_i$ with probability proportional to $\mathrm{LR}_{ik}$.

The positions $(a_1, \dots, a_N)$ form a Markov chain whose stationary distribution is the posterior distribution of the site positions (under a Dirichlet prior on the matrix, with the matrix integrated out); the chain wanders until it finds a few true sites, after which the matrix sharpens and the other sites are found quickly. Random restarts and occasional shifts of all positions by a few bases help to escape local optima. The sampler's randomness makes it less dependent on the starting point than EM, at the cost of many iterations.

### 8.4.5. Backgrounds and Controls

All these methods measure enrichment relative to a background, and the background decides what counts as a motif. Order-$0$ backgrounds make CpG-rich or AT-rich words look like motifs in promoters and peaks; higher-order Markov backgrounds estimated from the sequences themselves ([7.8.7](/7.8.7#sec-7.1.3)), or control sequences generated by shuffling each target while preserving its dinucleotide composition (Altschul and Erickson 1985), remove these artifacts. Repeats also produce strong spurious motifs and are masked before discovery. The statistical significance of a discovered motif (MEME's E-value) is computed against shuffled versions of the same sequences.

## 8.5. Motif Databases and Comparison

Matrices are collected in databases: JASPAR (open access, curated, nonredundant; the 2024 release has thousands of matrices across taxa), HOCOMOCO (human and mouse matrices from ChIP-seq and HT-SELEX, with quality grades), CIS-BP (inferred motifs for thousands of factors, including predictions from DNA-binding domain similarity) and, for RNA-binding proteins, ATtRACT and the RNAcompete collection. Most current matrices come from high-throughput binding assays: ChIP-seq peaks in cells; protein-binding microarrays, which measure the binding of a factor to all $10$-mers; and HT-SELEX, rounds of **in vitro selection** from random DNA libraries followed by sequencing, which also reveal preferences for pairs of sites and for spacing.

A newly discovered matrix is compared with the databases to identify the factor. Tomtom (Gupta and colleagues 2007) aligns two matrices column by column, scoring columns by Pearson correlation or Euclidean distance of their frequencies, and computes the significance of the best alignment over offsets and strands against a null distribution of column scores. Because many factors of one structural family (homeodomains, bHLH, C2H2 zinc fingers) recognize similar sequences, a match identifies a family rather than a factor; additional evidence, such as the expression of the candidate factors and ChIP-seq, decides. Enrichment of known motifs in a set of sequences relative to controls is tested by AME (MEME suite) or HOMER's known-motif mode, the most common analysis of ChIP-seq and ATAC-seq peaks ([7.9](/7.9)).

## 8.6. Conservation

### 8.6.1. Phylogenetic Footprinting

Functional sequence changes more slowly than nonfunctional sequence, because most mutations in it are deleterious and removed by purifying selection. Comparing orthologous regions of several species therefore reveals functional elements without knowing what they do, the computational analogue of **DNase I footprinting**.

**Definition 8.6.1 (Phylogenetic Footprinting)** **Phylogenetic footprinting** is the identification of functional elements, such as transcription factor binding sites, as segments of an alignment of orthologous noncoding sequences from several species that have changed less than expected under neutral evolution (Tagle and colleagues 1988).

The choice of species matters. Closely related species (human and chimpanzee) are too similar: almost everything is conserved by chance. Very distant species (human and fish) have lost most regulatory sequence alignment, leaving only the most constrained elements. Many moderately divergent species give the most power, because the total branch length of their tree, the number of opportunities for neutral change, is large while each pairwise alignment remains reliable; the alignments of $100$ vertebrates and of $241$ placental mammals (the Zoonomia project) serve this purpose. Conservation is also how genes were first found by comparing transcripts with other species ([7.8.7](/7.8.7#sec-7.4.3)), and it is a strong predictor of the pathogenicity of variants ([7.8.12](/7.8.12)).

### 8.6.2. Conservation Scores

**Definition 8.6.2 (Conservation Score)** A **conservation score** assigns each position of a reference genome a measure of evolutionary constraint, computed from a multiple alignment of orthologous genomes and a phylogenetic tree with neutral branch lengths, usually estimated from presumably neutral sites such as fourfold degenerate codon positions or ancient repeats.

Two scores are shown in genome browsers.

- *phastCons* (Siepel and colleagues 2005) is a *phylo-HMM*: a two-state hidden Markov model, conserved and nonconserved, whose emission at each alignment column is the likelihood of the column under a phylogenetic model ([7.8.6](/7.8.6#sec-6.5.1)), with branch lengths scaled down by a factor $\rho < 1$ in the conserved state. The posterior probability of the conserved state, computed by the forward–backward algorithm exactly as for CpG islands ([7.8.7](/7.8.7#sec-7.2.2)), is the score; Viterbi segments give conserved elements. Because it uses neighboring positions, phastCons finds conserved elements of tens to hundreds of base pairs.
- *phyloP* (Pollard and colleagues 2010) tests each position separately: the substitutions in its column are compared with the neutral model by a likelihood ratio or score test, and the score is $-\log_{10}$ of the p-value, positive for conservation (fewer substitutions than expected) and negative for acceleration (more). Its single-base resolution suits the interpretation of individual variants.

GERP (Cooper and colleagues 2005) reports "rejected substitutions", the difference between the neutral and observed numbers of substitutions at a position. Estimates of the fraction of the human genome under constraint range between about $3$ and $10\,\%$ depending on method and data, several times the fraction that codes for protein; most constrained bases are noncoding. The most extreme examples are the $481$ ultraconserved elements of at least $200$ bp that are identical between human, mouse and rat (Bejerano and colleagues 2004), many of them enhancers of developmental regulators. Conversely, regions conserved across mammals but rapidly changed in the human lineage (human accelerated regions) are candidates for human-specific traits.

## 8.7. Other Sequence Signals

### 8.7.1. Splice Sites

The splice sites are the best-studied motifs of eukaryotic genes. The **5′ splice site** (donor) spans the last three exonic and the first six intronic positions, with consensus MAG|GURAGU; the **3′ splice site** (acceptor) spans about $20$ intronic positions, with the **branch point** and a polypyrimidine tract upstream of the invariant AG, and one or two exonic positions.

**Example 8.7.1** From the $1883$ introns of the curated protein-coding genes on human chromosome 21 (one transcript per gene), the donor logo has $8.2$ bits, $3.9$ of them in the invariant GT, and peaks of about $1$ bit at the G of position $-1$ and of $0.6$ to $1.0$ bits at positions $+3$ to $+5$; the acceptor logo has $9.3$ bits, $4.0$ of them in the AG, $0.8$ bits at the C or T of position $-3$ and $0.1$ to $0.5$ bits per position spread over the polypyrimidine tract.

![Splice-site signals of human introns: counts at the 1883 introns of the longest RefSeq transcript of each of the 228 curated protein-coding genes on chromosome 21 (GRCh38), read on the strand of the gene. A: 5′ splice site (donor), exon positions −3 to −1 and intron positions +1 to +6; 98.9 % of introns begin with GT and 0.8 % with GC. B: 3′ splice site (acceptor), intron positions −20 to −1 and exon positions +1 to +3: the invariant AG is preceded by a pyrimidine-rich tract. Dashed lines mark the exon–intron boundaries; stack heights are information contents in bits](./plots/splice-sites.py)

The positions of the donor site are not independent (base pairing with U1 snRNA can be made up by stronger pairing elsewhere in the site), so the PWM is improved by models with dependencies: MaxEntScan (Yeo and Burge 2004) fits the maximum entropy distribution consistent with low-order marginal frequencies, an application of the **maximum entropy principle**, and is the standard for scoring the effect of variants on splice sites. Splice sites alone, however, are not enough: their information content is far below what is needed to find introns in a genome, and the decision depends on exonic and intronic splicing enhancers and silencers and on the exon–intron architecture. Deep networks that read $10$ kb of context (SpliceAI, Jaganathan and colleagues 2019) predict splice sites from sequence with high accuracy and are used to interpret variants that create or destroy them ([7.8.15](/7.8.15)).

### 8.7.2. Signals of Transcription and Translation

Other well-known motifs are the **TATA box** (TATAWAWR, about $30$ bp upstream of the transcription start of a minority of eukaryotic promoters), the initiator and downstream core promoter elements ([7.2](/7.2)); the **polyadenylation signal** AAUAAA, or its variant AUUAAA, $10$–$30$ nucleotides upstream of the cleavage site, together with downstream GU-rich elements; the **Kozak sequence** gccRccAUGG around the start codon of eukaryotic mRNAs and the **Shine–Dalgarno sequence** AGGAGG upstream of bacterial start codons, which pairs with the 3′ end of 16S rRNA ([7.8.7](/7.8.7#sec-7.3.3)). RNA-binding proteins recognize motifs that are short ($4$–$7$ nucleotides), often in a particular structural context (single-stranded loops), which makes them weaker as sequence signals than transcription factor sites; their models combine sequence and structure ([7.8.16](/7.8.16)).

## 8.8. Practice

```bash
# De novo discovery in ChIP-seq peak summits (100 bp), with a shuffled control preserving dinucleotides
streme --p peaks.fa --dna --nmotifs 10 --oc streme_out
meme-chip -oc memechip_out -meme-nmotifs 5 -db JASPAR2024_CORE_vertebrates.meme peaks.fa
findMotifsGenome.pl peaks.bed hg38 homer_out -size 200 -p 8    # HOMER: known and de novo motifs

# Known motifs: compare a discovered motif with a database, and test enrichment in peaks
tomtom -oc tomtom_out streme_out/streme.txt JASPAR2024_CORE_vertebrates.meme
sea --p peaks.fa --m JASPAR2024_CORE_vertebrates.meme --oc sea_out

# Scan sequences with a PWM: exact p-values and q-values
fimo --thresh 1e-4 --oc fimo_out MA0139.1.meme promoters.fa
```

```python
# Building a PWM, computing information content and scanning with Biopython
from Bio import motifs
from Bio.Seq import Seq
sites = [Seq(s) for s in ["TATAAT", "TATGAT", "TACAAT", "TATAAT", "GATAAT", "TATACT", "TATAAT", "TAAAAT"]]
m = motifs.create(sites)
pwm = m.counts.normalize(pseudocounts=0.125)               # 0.125 per base, beta = 0.5 in total
pssm = pwm.log_odds()                                       # log2 ratios against a uniform background
print(m.consensus, pssm.max)                                # TATAAT, 10.63 bits
seq = Seq("GGCTATAATGCCATGATAATCGG")
for pos, score in pssm.search(seq, threshold=5.0, both=True):
    print(pos, round(float(score), 2))                     # negative positions are on the minus strand
```

The interpretation of motif results needs care. A discovered motif may reflect sequence bias of the assay (GC content, the cutting preference of a nuclease), repeats or a cofactor rather than the immunoprecipitated factor; centrality of the motif at peak summits and comparison with matched controls are the usual checks. A known motif with significant enrichment shows that sites are over-represented, not that each predicted site is bound, and its absence does not prove that the factor binds indirectly.

## Summary

| Topic | Key points |
|---|---|
| Motifs | families of functionally equivalent short sites (Definition 8.1.1); consensus and IUPAC codes lose the strengths of sites and mismatches |
| Matrices | PFM of counts (Definition 8.2.1); PWM $\log_2[(n + \beta q)/(N + \beta)/q]$, score = log-likelihood ratio, ∝ binding energy (Formula 8.2.1, Example 8.2.1) |
| Logos | information content $R_j = 2 - (H_j + e_N)$, small-sample correction $3/(2N\ln2)$; $4.32$ bits for proteins (Definition 8.2.2, Example 8.2.2: CTCF $17.2$ bits) |
| Expected scores | relative entropy for sites, minus the reverse divergence for background (Theorem 8.2.1); $R_{\mathrm{sequence}} \approx \log_2(G/\gamma)$ |
| Scanning | exact score distribution by convolution (Algorithm 8.3.1); CTCF at $p = 10^{-6}$: $6200$ chance matches in the genome and $72\,\%$ sensitivity (Example 8.3.1); FDR for many sequences |
| Lactase enhancer | −13910T raises the best Oct-1 PWM score covering the variant from $-5.35$ to $-3.79$ bits; a scan shows direction, not magnitude (Example 8.3.2) |
| Discovery | word enrichment with hypergeometric tests (Example 8.4.1); EM with OOPS, ZOOPS, TCM (Algorithm 8.4.1, Example 8.4.2: 25/25 sites, local optima by shifts); Gibbs sampling (Algorithm 8.4.2); dinucleotide-preserving backgrounds |
| Databases | JASPAR, HOCOMOCO, CIS-BP; PBM, HT-SELEX; Tomtom; family-level identification |
| Conservation | phylogenetic footprinting (Definition 8.6.1); conservation scores on a neutral tree (Definition 8.6.2): phastCons (phylo-HMM, elements), phyloP (per base, conservation and acceleration), GERP; ultraconserved elements |
| Other signals | donor and acceptor sites ($8.2$ and $9.3$ bits, Example 8.7.1), MaxEntScan, SpliceAI; TATA box, poly(A) signal, Kozak and Shine–Dalgarno sequences; RNA-binding motifs |

## Questions

1. Write the consensus sequence of the sites of Example 8.2.1 using IUPAC codes for positions where more than one base was observed, and explain what information is lost.

   **Answer** Position 1: T (7) or G (1), K; position 2: A; position 3: T (6), A (1), C (1), H; position 4: A or G, R; position 5: A or C, M; position 6: T. Consensus KAHRMT. This degenerate word matches $2 \times 3 \times 2 \times 2 = 24$ sequences equally, including GACGCT, which differs from the best site at four positions, each time with a base observed only once; the matrix gives it $2 \times 1.93 - 4 \times 0.92 = 0.18$ bits against $10.63$ for TATAAT. Frequencies, and hence the strength of sites, are lost; the reduced alphabet also cannot express "T usually, G rarely".

2. Compute the information content of a DNA motif position with frequencies $(0.5, 0, 0.5, 0)$ estimated from $20$ sites, and of a protein column in which $10$ sequences all have tryptophan.

   **Answer** DNA: $H = 1$ bit, $e_{20} = 3/(2 \times 20 \times 0.693) = 0.108$, $R = 2 - 1 - 0.108 = 0.89$ bits. Protein: $H = 0$, correction $19/(2 \times 10 \times 0.693) = 1.37$ bits, $R = 4.32 - 1.37 = 2.95$ bits. The small-sample correction is large for proteins because $20$ letters cannot be represented reliably by $10$ sequences: even an invariant column might be less conserved in a larger sample.

3. Show that for a motif position with frequencies $p$ and a uniform background, the information content without correction equals the expected weight of the position under the motif model.

   **Answer** With $q_b = 1/4$, the expected weight is $\sum_bp_b\log_2(p_b/0.25) = \sum_bp_b\log_2p_b + \sum_bp_b\log_24 = -H + 2 = R$. This is Theorem 8.2.1 for one position: the information content of a logo is the average score that a real site gains at that position over a random base; logos of motifs with a nonuniform background should use the relative entropy, which is what the PWM actually rewards.

4. Using the score distribution of a PWM, explain why a threshold of "$80\,\%$ of the maximum score", common in older tools, is unsuitable for comparing motifs of different lengths and information contents.

   **Answer** The background distribution of the score depends on the matrix: its mean is $-\sum_jD(q \Vert p_j)$ and its spread grows with the number and contrast of positions. For a short, low-information motif, $80\,\%$ of the maximum may correspond to a p-value of $10^{-2}$, giving a match every $100$ bp; for a long, high-information motif such as CTCF, the same fraction may correspond to $10^{-7}$ and miss many real sites. A threshold on the p-value computed exactly (Algorithm 8.3.1) gives the same expected number of chance matches per base for every motif, so results are comparable; an additional FDR control is needed when many sequences or motifs are scanned.

5. A motif has information content $12$ bits. Approximately how often do you expect a background window to score as high as a typical site? How many such windows does the human genome contain?

   **Answer** A typical site scores about its expected score, the relative entropy $\approx 12$ bits (Theorem 8.2.1 with a near-uniform background). The probability that a background window reaches a log-likelihood ratio of $S$ bits is at most $2^{-S}$ (by Markov's inequality applied to the likelihood ratio, whose expectation under the background is $1$), here $2^{-12} = 2.4\times10^{-4}$, and in practice somewhat less. With $6.2\times10^9$ windows on both strands, up to about $1.5\times10^6$ windows score like a typical site, far more than the thousands of sites a factor binds: most eukaryotic motifs are not specific enough to be found by sequence alone.

6. In Algorithm 8.4.1 the E step uses the likelihood ratio relative to the background. Why does the background cancel in the posterior $z_{ik}$ only if every position of a sequence is assigned the same background model, and what goes wrong with a background of uniform frequencies on GC-rich peaks?

   **Answer** The probability of a sequence with a site at $k$ is the product of motif probabilities in the site and background probabilities elsewhere; dividing by the background probability of the whole sequence gives the likelihood ratio of the window, and the common factor cancels in $z_{ik}$ because every hypothesis $k$ shares it. The background still enters through the ratio $p/q$ in the window: with uniform $q$ in GC-rich sequences, every GC-rich window has a high ratio under any matrix that has drifted toward G and C, so EM converges to a "motif" describing composition (CCGCCC-like) rather than binding. A background estimated from the sequences, preferably a higher-order Markov model that captures CpG and GC content, removes this.

7. MEME found a motif of $15$ bp in $500$ ChIP-seq peaks, but Tomtom matches it to the forkhead family rather than to the immunoprecipitated factor, a nuclear receptor. Give three explanations and an analysis to distinguish them.

   **Answer** (a) The receptor binds DNA through a forkhead pioneer factor at many sites (indirect or cooperative binding), common for nuclear receptors in liver and breast cells, where FOXA1 opens chromatin. (b) The antibody cross-reacts or the peaks are dominated by highly accessible regions bound by many factors (hyper-ChIPable regions). (c) The receptor motif is present but weaker or more variable, and MEME's first motif is the most frequent signal, not the primary one. Analyses: search for further motifs after erasing the first, and test the known receptor motif for enrichment and centrality at peak summits (CentriMo); compare peaks with forkhead ChIP-seq from the same cells; examine whether the strongest peaks contain the receptor motif; and check the peaks in a control for antibody specificity (a knockout or knockdown of the receptor, an input or IgG control).

8. Why do phastCons and phyloP need a neutral tree, and what happens to a conservation score if the alignment at a position contains only primates?

   **Answer** Conservation is an excess of similarity relative to what neutral evolution would produce on the same tree; the neutral branch lengths, estimated from fourfold degenerate sites or ancient repeats, set the expected number of substitutions. Primates are closely related: the total neutral branch length among them is small, so even a neutral position is expected to show few substitutions, and the absence of substitutions has a high probability under neutrality. phyloP then gives scores near zero (no significant conservation can be shown), and phastCons cannot separate the two states; constraint is detectable only with enough total branch length, which is why alignments of hundreds of mammals were assembled. Gaps in an alignment (species without an aligned base) similarly reduce the power of the scores locally.

9. (Design) A variant associated with a disease lies $30$ kb from the nearest gene, in a region with an ATAC-seq peak in the relevant cell type. Propose an analysis, using the methods of this chapter and evidence from other chapters, to decide whether it changes a transcription factor binding site.

   **Answer** Score both alleles with all relevant matrices (JASPAR, HOCOMOCO) and compute the change in PWM score and the p-values of the best windows (Example 8.3.2); prefer factors expressed in the cell type. Check conservation of the site (phyloP at the variant, phastCons elements), since conserved sites are more often functional. Look for direct evidence: ChIP-seq of candidate factors in the cell type, allele-specific binding or accessibility in heterozygous samples (more reads from one allele), and chromatin-trained deep models that predict the variant's effect on accessibility from sequence ([7.8.15](/7.8.15)). Fine-map the association to see whether this variant or one in linkage disequilibrium is likely causal ([7.4.25](/7.4.25)). Finally test experimentally: reporter assays of both alleles, electrophoretic mobility shift assays with the candidate factor, and genome editing of the site with measurement of the target gene's expression, identified by chromatin conformation data ([7.9](/7.9)).

10. (Open) Explain why de novo motif discovery is easier in sequences from ChIP-seq peaks than in the promoters of coregulated genes found by expression analysis, and why both are easier for bacteria than for mammals.

    **Answer** ChIP-seq peaks localize the bound DNA to about $100$ bp around the summit, so the site occupies a large fraction of each sequence and most sequences contain it; promoters of coexpressed genes are long (often $1$–$2$ kb are taken), many coexpressed genes are regulated indirectly or by different factors, and the regulatory site may be in a distant enhancer rather than the promoter, so the signal is diluted among much background sequence and absent from many sequences (the ZOOPS case). Bacterial factors bind longer, more informative sites (often $15$–$20$ bp with $15$–$20$ bits, palindromic for dimeric factors), close to the genes they regulate in compact intergenic regions; mammalian factors often have short motifs of $8$–$12$ bits, act from enhancers tens of kilobases away, bind cooperatively in combinations, and their sites are embedded in genomes with strong composition heterogeneity (CpG islands, repeats), all of which reduce the contrast between sites and background.
