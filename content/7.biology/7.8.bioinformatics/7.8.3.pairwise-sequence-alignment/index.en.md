---
title: Pairwise Sequence Alignment
description: "Homology, identity and similarity; dot plots; substitution matrices as log-odds scores, with the construction of PAM (powers of a Markov transition matrix, reconstructed from Dayhoff's data) and BLOSUM, their relative entropies and the choice of a matrix; nucleotide scores and their target identities; linear and affine gap penalties. Alignment as a path in the edit graph and the number of alignments; the Needleman–Wunsch, Smith–Waterman and Gotoh algorithms with worked examples, semi-global alignment, edit distance and the longest common subsequence; linear-space (Hirschberg), banded, SIMD and wavefront alignment; significance by shuffling, with human and yeast MCM6 as the running example."
---

To decide whether two genes or proteins are related, and to transfer what is known about one to the other, we must first decide which residues correspond. A pairwise sequence alignment does this: it writes the two sequences one above the other, inserting gaps so that residues descended from the same ancestral residue stand in the same column. Alignment is the most used operation of bioinformatics. Database searches ([7.8.4](/7.8.4)) are alignments made fast, multiple alignments and profiles ([7.8.5](/7.8.5)) are built from pairwise ones, phylogenetic trees ([7.8.6](/7.8.6)) are inferred from them, and mapping sequencing reads to a genome ([7.8.10](/7.8.10)) is pairwise alignment on a vast scale. This chapter treats the two halves of the problem. The model is the scoring system: a substitution matrix, derived from the frequencies of substitutions in related proteins as a **log-odds score** ([7.6.41](/7.6.41#def-41.2.1)), and a penalty for gaps. The algorithm finds the best alignment under that model by **dynamic programming**, whose general principle was introduced with the **longest common subsequence** in [4.3.1](/4.3.1#sec-1.6); here we give the alignment algorithms themselves, their variants and the techniques that make them practical for long sequences. The biochemical background, homologous proteins and the use of alignments to trace evolution, was given in [7.1.4](/7.1.4#sec-4.4). The running example is the protein MCM6, a subunit of the replicative helicase, whose gene *MCM6* contains in one of its introns the lactase persistence variant rs4988235 followed through this course ([7.8.1](/7.8.1)).

## 3.1. Homology and Similarity

### 3.1.1. Homology, Identity and Similarity

Two sequences are homologous if they descend from a common ancestral sequence: **homologs** that diverged by speciation are **orthologs**, those that diverged by gene duplication within a lineage are **paralogs** ([7.1.4](/7.1.4#sec-4.4.1)), and homologs acquired by horizontal transfer are sometimes called *xenologs*. Human MCM6 and yeast Mcm6 are orthologs; human MCM2, MCM3, MCM4, MCM5, MCM6 and MCM7, the six subunits of the MCM2–7 helicase, are paralogs that arose by duplications before the last common ancestor of eukaryotes, from a single MCM protein still found, as a homohexamer, in archaea. Homology is a statement about history and is either true or false; similarity is a measurable property of an alignment, and we infer homology from similarity that is too great to be explained by chance.

**Definition 3.1.1 (Sequence Alignment)** A (pairwise) **sequence alignment** of strings $x = x_1 \cdots x_m$ and $y = y_1 \cdots y_n$ over an alphabet $\mathcal{A}$ is a pair of strings $x^*$, $y^*$ of equal length over $\mathcal{A} \cup \{-\}$ such that deleting the gap symbols $-$ from $x^*$ gives $x$, deleting them from $y^*$ gives $y$, and no column contains two gaps. A column $(a, b)$ with $a, b \in \mathcal{A}$ is a *match* if $a = b$ and a *mismatch* (substitution) otherwise; a column with a gap represents an insertion or deletion (indel) in one of the lineages. An alignment is a **global alignment** if it covers both sequences entirely and a **local alignment** if it aligns a substring of $x$ with a substring of $y$.

**Definition 3.1.2 (Sequence Identity)** The **sequence identity** of an alignment is the number of identical columns divided by a length; the length must be stated, since three conventions are in use: the number of columns of the alignment (including gaps), the number of aligned residue pairs (excluding gaps), or the length of the shorter sequence. *Similarity* (positives) counts in addition the columns whose substitution score is positive.

**Example 3.1.1 (Human and Yeast MCM6)** The best local alignment of human MCM6 ($821$ residues) with *Saccharomyces cerevisiae* Mcm6 ($1017$ residues), under the scoring system of BLAST (BLOSUM62, gaps scored $-(11 + k)$ for length $k$), covers residues $17$–$816$ of the human and $102$–$1004$ of the yeast protein in $906$ columns, of which $385$ are identities, $412$ mismatches and $109$ gap columns in $13$ gaps. The identity is $385/906 = 42.5\,\%$ of the columns, $385/797 = 48.3\,\%$ of the aligned pairs and $385/821 = 46.9\,\%$ of the shorter sequence; $537$ columns ($59.3\,\%$) have a positive score. For comparison, human and mouse MCM6 are $95.9\,\%$ identical over their full length without a single gap, and human MCM6 and its paralog MCM2 are $31.8\,\%$ identical over a local alignment of $654$ columns.

### 3.1.2. The Twilight Zone

Unrelated proteins also share identities. Two random residues drawn from the background frequencies are identical with probability $\sum_a q_a^2 \approx 0.058$; but an optimal alignment of two unrelated proteins, which chooses where to put gaps to maximize the score, typically shows $15$ to $25\,\%$ identity. Rost (1999), from structurally verified pairs, found that above about $40\,\%$ identity over more than $100$ aligned residues proteins are almost always homologous, while between about $20$ and $35\,\%$ homologs and unrelated pairs overlap. This range is called the *twilight zone*: an identity there is neither evidence for nor against homology, and a statistical measure of significance ([7.8.4](/7.8.4)) or a more sensitive profile method ([7.8.5](/7.8.5)) is needed. The human MCM paralogs, at $30$–$40\,\%$ identity over $650$ columns, are on the safe side of the zone because the alignments are long.

For coding sequences, the protein sequence is the better object to align. DNA has only four letters, so unrelated DNA is $25\,\%$ identical by chance, and synonymous changes at third codon positions saturate quickly; protein alignments detect homology five to ten times further back in evolutionary time than DNA alignments of the same genes (Pearson 2013). DNA alignment is used for non-coding sequence, for closely related sequences (reads against a reference genome, strains of a virus) and for finding genes in the first place.

## 3.2. Dot Plots

The simplest comparison of two sequences shows all their similarities at once, without choosing an alignment.

**Definition 3.2.1 (Dot Plot)** The **dot plot** of $x$ and $y$ with window $w$ and mismatch threshold $k$ is the set of points $(i, j)$ such that the substrings $x_i \cdots x_{i+w-1}$ and $y_j \cdots y_{j+w-1}$ differ in at most $k$ positions. For DNA, points are also drawn where $x_i \cdots x_{i+w-1}$ matches the reverse complement of a window of $y$.

A run of points along a diagonal is a similar segment; an alignment is a path that connects such runs. Two parallel diagonals over the same range of $x$ reveal a duplicated segment, an anti-diagonal of reverse-complement matches an inversion, and a sideways jump of the diagonal an insertion or deletion. The window filters chance matches: for random DNA, a single position matches with probability $1/4$, so a quarter of all cells are dots, whereas an exact match of $w = 11$ positions has probability $4^{-11} = 2.4\times10^{-7}$, about $0.02$ chance points in a $300 \times 300$ plot.

![Dot plots of a random 300-nt sequence x against a rearranged copy y, in which the segment 40–60 is duplicated in tandem, the segment 120–180 is inverted (reverse complemented), the segment 210–240 is deleted, and 3 % of positions are substituted. A: single-base identities; a quarter of all cells are dots and the structure is invisible. B: windows of 11 bases with at most one mismatch, forward matches in blue and reverse-complement matches in orange. The main diagonal is interrupted by the duplication (two diagonals over x = 40–60), the inversion (an anti-diagonal) and the deletion (a horizontal jump of 30 positions in x)](./plots/dot-plot.py)

Dot plots remain the standard first look at the comparison of two long sequences, such as two assemblies of a chromosome, where whole-genome aligners draw them from their alignments (as "synteny plots"). They need no scoring matrix and no gap penalty, but give no score and no statement of significance; for those we need a scoring model.

## 3.3. Scoring Substitutions

### 3.3.1. Scores as Log-Odds

The score of a gap-free alignment is the sum of scores $s(a, b)$ of its columns. Following [7.6.41](/7.6.41#def-41.2.1), the natural choice is the **log-odds score** $s(a, b) = \lambda^{-1}\ln[p_{ab}/(q_aq_b)]$: the log-ratio of the probability of the column under a model of related sequences, in which pairs occur with *target frequencies* $p_{ab}$, to that under a model of independent sequences with background frequencies $q_a$. The total score is then a log-likelihood ratio, which by the Neyman–Pearson lemma is the most powerful statistic for deciding between the two models. Conversely, every scoring matrix with a negative expected score and some positive entries implies target frequencies: there is a unique $\lambda > 0$ with $\sum_{a,b}q_aq_b\mathrm{e}^{\lambda s(a,b)} = 1$ ([7.6.41](/7.6.41#thm-41.2.1)), and $p_{ab} = q_aq_b\mathrm{e}^{\lambda s(a,b)}$ are the frequencies for which the matrix is optimal.

**Definition 3.3.1 (Substitution Matrix)** A **substitution matrix** is a symmetric function $s\colon \mathcal{A} \times \mathcal{A} \to \mathbb{R}$ (in practice integer-valued) assigning a score to each aligned pair of residues. Its *relative entropy* with respect to background frequencies $q$ is the **Kullback–Leibler divergence** of the implied target frequencies from the background,

$$
H = \sum_{a,b}p_{ab}\log_2\frac{p_{ab}}{q_aq_b} = \frac{\lambda}{\ln 2}\sum_{a,b}p_{ab}\,s(a,b)
$$
bits per aligned pair, the expected score per column of a true alignment in bits.

$H$ measures how much a column of an alignment tells us: a matrix for closely related sequences has high $H$ (few columns suffice to recognize a homolog) and one for distant sequences low $H$. With the background frequencies used by BLAST (Robinson and Robinson 1991), BLOSUM62 has $\lambda = 0.3176$ (the scores are in units of $1/\lambda = 3.15$ nats, close to half-bits), expected score $-0.95$ per random pair, $H = 0.58$ bits and implied target identity $\sum_a p_{aa} = 30\,\%$.

### 3.3.2. PAM Matrices

Dayhoff and colleagues (1978) derived the first substitution matrices from evolution observed directly. They aligned $71$ families of closely related proteins (at least $85\,\%$ identity, so that each site had changed at most once), reconstructed the ancestral sequences on trees and counted $1572$ *accepted point mutations*, substitutions that had been fixed in the population and so had passed through natural selection.

**Definition 3.3.2 (PAM Matrix)** One **PAM** (point accepted mutation) is the evolutionary distance over which $1\,\%$ of residues are substituted. The 1-PAM *mutation probability matrix* $M$ has entries $M_{ab}$, the probability that residue $b$ is replaced by residue $a$ in one PAM; the **PAM matrix** of distance $n$ is the log-odds matrix

$$
\mathrm{PAM}n(a, b) = c\log\frac{(M^n)_{ab}}{q_a},
$$
with $c$ a scale factor (Dayhoff used $10\log_{10}$), rounded to integers.

**Algorithm 3.3.1 (Dayhoff's Construction)** From the counts $A_{ab} = A_{ba}$ of accepted substitutions between $a$ and $b$ on the trees, and the frequencies $q_a$:

1. Compute the relative mutability $m_b$ of each residue: the number of times $b$ was substituted divided by the number of occurrences of $b$ exposed to change.
2. Set $M_{ab} = \kappa\, m_bA_{ab}/\sum_{c \ne b}A_{cb}$ for $a \ne b$ and $M_{bb} = 1 - \kappa m_b$, with $\kappa$ chosen so that the expected change $\sum_b q_b(1 - M_{bb})$ equals $0.01$.
3. Take the matrix power $M^n$ and the log-odds of Definition 3.3.2.

The construction is a **Markov chain** on the twenty amino acids: $M$ is the one-step transition matrix (columns sum to $1$), $M^n$ the $n$-step one, and the background $q$ its stationary distribution, with $q_bM_{ab} = q_aM_{ba}$ (the chain is reversible, as for nucleotide models in [7.6.41](/7.6.41#sec-41.2.3)). The matrix power extrapolates the substitutions observed at short distance to long distances, accounting for multiple and back substitutions at the same site.

**Example 3.3.1 (Reconstructing 1 PAM)** The published PAM250 log-odds matrix and the Dayhoff frequencies determine $M^{250}_{ab} = q_a10^{\mathrm{PAM250}(a,b)/10}$. Because the chain is reversible, $D^{-1/2}M^{250}D^{1/2}$ with $D = \operatorname{diag}(q)$ is symmetric, and its eigendecomposition gives the 250th root, which after rescaling to exactly $1\,\%$ change is the 1-PAM matrix (the rescaling factor is $1/250.1$, so the rounded matrix is almost exactly consistent). Powers of this matrix reproduce Dayhoff's table of the correspondence between distance and observed difference: $50\,\%$ difference at $80$ PAM, $80\,\%$ at $250$ PAM. At $250$ PAM a tryptophan is still a tryptophan with probability $0.55$, an alanine only with probability $0.13$: rare, structurally special residues are conserved. The naive estimate $0.99^{250} = 8.1\,\%$ of unchanged sites is far below the actual $19.6\,\%$, because back substitutions occur and because slowly mutating residues stay unchanged. Two unrelated sequences differ at $1 - \sum_a q_a^2 = 94\,\%$ of positions, the limit as $n \to \infty$.

![PAM matrices as powers of one Markov transition matrix, reconstructed from Dayhoff's PAM250 log-odds matrix and amino acid frequencies (Example 3.3.1). A: the expected percent difference between two sequences n PAM apart (line) and Dayhoff's tabulated correspondence (points); the dashed line is the difference between unrelated sequences, 94 %. B: the relative entropy of the PAM n log-odds matrix, the information per aligned pair, falls from 4 bits at short distances to 0.35 bits at PAM250; the dashed lines mark BLOSUM80, BLOSUM62 and BLOSUM45 (with BLAST background frequencies), which correspond in information to about PAM128, PAM183 and PAM246](./plots/pam-divergence.py)

### 3.3.3. BLOSUM Matrices

PAM matrices extrapolate from close relatives, and errors in the short-distance counts are amplified by the matrix power. Henikoff and Henikoff (1992) instead counted substitutions directly in alignments of distantly related proteins: about $2000$ ungapped *blocks*, the most conserved segments of about $500$ protein families of the BLOCKS database.

**Definition 3.3.3 (BLOSUM Matrix)** The **BLOSUM matrix** (BLOcks SUbstitution Matrix) with threshold $L$, BLOSUM$L$, is the log-odds matrix computed from pairs of residues in the same column of ungapped blocks, after the sequences of each block that are at least $L\,\%$ identical have been clustered and each cluster counted with total weight one.

**Algorithm 3.3.2 (BLOSUM Construction)**

1. In each block, cluster sequences with at least $L\,\%$ identity (single linkage) and give each sequence weight $1/(\text{cluster size})$.
2. Count, over all columns, the weighted pairs of residues from different clusters, $f_{ab}$ (unordered pairs), and normalize: $q_{ab} = f_{ab}/\sum_{c \le d}f_{cd}$.
3. Compute the residue frequencies $p_a = q_{aa} + \frac{1}{2}\sum_{b \ne a}q_{ab}$ and the expected pair frequencies $e_{aa} = p_a^2$, $e_{ab} = 2p_ap_b$ for $a \ne b$.
4. Set $s(a, b) = \operatorname{round}[2\log_2(q_{ab}/e_{ab})]$, a score in half-bits.

**Example 3.3.2** A block of five sequences and two columns, `AAAAS` and `SSSTT` (one sequence per position, no clustering), gives $10$ pairs per column: AA $6$, AS $4$ in the first; SS $3$, ST $6$, TT $1$ in the second. Thus $q_{\mathrm{AA}} = 0.30$, $q_{\mathrm{AS}} = 0.20$, $q_{\mathrm{SS}} = 0.15$, $q_{\mathrm{ST}} = 0.30$, $q_{\mathrm{TT}} = 0.05$; $p_{\mathrm{A}} = 0.30 + 0.10 = 0.40$, $p_{\mathrm{S}} = 0.40$, $p_{\mathrm{T}} = 0.20$. The scores are $2\log_2(0.30/0.16) = 1.81 \to 2$ for AA, $2\log_2(0.20/0.32) = -1.36 \to -1$ for AS, $-0.19 \to 0$ for SS, $1.81 \to 2$ for ST and $0.64 \to 1$ for TT. Identity is not automatically rewarded: S paired with itself scores $0$ because S is common and its pairing with T is the frequent event.

The threshold $L$ sets the distance: a high $L$ removes only near-identical redundancy and keeps the substitutions between close relatives, giving matrices for close sequences (BLOSUM80, $H = 0.91$ bits with the BLAST background); a low $L$ merges close relatives into clusters and leaves only distant comparisons (BLOSUM45, $0.36$ bits). The numbering therefore runs opposite to that of PAM. BLOSUM62 is the default of BLAST and of most aligners; it outperformed PAM matrices of the same relative entropy in detecting distant homologs (Henikoff and Henikoff 1993), presumably because it is estimated from the distant comparisons for which it is used rather than extrapolated to them. In 2008 Styczynski and colleagues found that the BLOSUM62 used everywhere differs from the intended one because of a bug in the original program; the "correct" matrix performs slightly worse, a reminder that the matrices are empirical tools, judged by their performance.

![BLOSUM62 and PAM250 with residues ordered by Dayhoff's physicochemical groups: cysteine; small residues S, T, P, A, G; acids and amides N, D, E, Q; bases H, R, K; hydrophobic M, I, L, V; aromatic F, Y, W (lines separate the groups). Blue cells are positive scores (pairs seen in related proteins more often than by chance), red cells negative. Both matrices have positive blocks within groups (I–V, F–Y, D–E, K–R); BLOSUM62 gives large identity scores to rare residues (W 11, C 9), and PAM250, extrapolated to a large distance, has more positive off-diagonal entries within groups](./plots/substitution-matrices.py)

### 3.3.4. Choosing a Matrix

| Matrix | $\lambda$ (per score unit) | Expected score | $H$ (bits) | Target identity | Typical use |
|---|---|---|---|---|---|
| PAM30 | $0.340$ | $-4.96$ | $2.53$ | $74\,\%$ | short queries (< $35$ residues), near-identical |
| PAM70 | $0.335$ | $-2.70$ | $1.49$ | $51\,\%$ | queries of $35$–$50$ residues |
| BLOSUM80 | $0.226$ | $-2.09$ | $0.91$ | $39\,\%$ | queries of $50$–$85$ residues, close homologs |
| BLOSUM62 | $0.318$ | $-0.95$ | $0.58$ | $30\,\%$ | default for proteins |
| BLOSUM45 | $0.229$ | $-0.81$ | $0.36$ | $24\,\%$ | long queries, distant homologs |
| PAM250 | $0.225$ | $-0.80$ | $0.32$ | $19\,\%$ | historical; very distant homologs |

(All values computed with the Robinson–Robinson background frequencies; the query-length ranges are those recommended by NCBI.) The relative entropy also sets a minimum length: to reach a significant score of about $40$ bits ([7.8.4](/7.8.4)), an alignment needs about $40/H$ columns, $16$ with PAM30 but $70$ with BLOSUM62. Short queries therefore need high-information matrices, and a matrix whose target identity matches the true divergence of the sequences is the most sensitive one (Altschul 1991). For the same reason no single matrix is optimal for all searches; profile methods ([7.8.5](/7.8.5)) replace the fixed matrix by position-specific scores estimated from the family.

### 3.3.5. Nucleotide Scores

DNA is usually scored by a match reward $r$ and a mismatch penalty $-p$. With uniform bases, $\lambda$ solves $\frac{1}{4}\mathrm{e}^{\lambda r} + \frac{3}{4}\mathrm{e}^{-\lambda p} = 1$ and the implied target identity is $\frac{1}{4}\mathrm{e}^{\lambda r}$:

| $r/{-p}$ | $\lambda$ | Target identity | $H$ (bits) | Use |
|---|---|---|---|---|
| $1/{-3}$ | $1.374$ | $98.8\,\%$ | $1.89$ | near-identical sequences (old megablast default) |
| $1/{-2}$ | $1.333$ | $94.8\,\%$ | $1.62$ | megablast default, reads to genome |
| $2/{-3}$ | $0.634$ | $88.8\,\%$ | $1.32$ | blastn default |
| $1/{-1}$ | $1.099$ | $75.0\,\%$ | $0.79$ | divergent sequences |
| $5/{-4}$ | $0.192$ | $65.1\,\%$ | $0.52$ | EMBOSS default (EDNAFULL) |

A scheme suited to $95\,\%$ identity penalizes the mismatches of a $75\,\%$-identical pair so heavily that the alignment breaks into short pieces. Matrices that distinguish **transitions** (purine–purine, pyrimidine–pyrimidine), which occur about twice as often as **transversions** in most genomes, are also used, for example the $4\times4$ matrix with scores $2$, $-5$ (transition) and $-7$ (transversion) in Question 2.

## 3.4. Gap Penalties

An insertion or deletion of $k$ residues is usually a single mutational event: slippage during replication, unequal crossing over, insertion of a transposable element. Indels are rarer than substitutions, roughly one indel per ten substitutions in proteins, and are tolerated mainly in surface loops, not in the cores of secondary structures. A gap penalty should therefore charge mainly for the existence of a gap and less for its length.

**Definition 3.4.1 (Gap Penalty)** A **gap penalty** is a function $g(k) \ge 0$ subtracted from the score of an alignment for each maximal run of $k$ gap symbols in one row. It is *linear* if $g(k) = dk$ and an **affine gap penalty** if

$$
g(k) = d + (k - 1)e \qquad (d \ge e > 0),
$$
where $d$ is the cost of opening a gap and $e$ the cost of each further position.

BLAST writes the same affine penalty as $a + bk$ ("existence" $a = 11$, "extension" $b = 1$ for BLOSUM62), so that $d = a + b = 12$, $e = b = 1$; programs differ in this convention, which must be checked when parameters are transferred. In a probabilistic alignment model ([7.8.5](/7.8.5)) an affine penalty corresponds to a geometric distribution of gap lengths: if a gap is opened with probability $\delta$ and extended with probability $\varepsilon$, a gap of length $k$ has probability $\delta\varepsilon^{k-1}$, whose negative logarithm is affine in $k$. Observed indel lengths have a heavier tail than geometric (roughly a power law), and concave penalties such as $d + e\ln k$ fit better but cost more to optimize; affine penalties are the universal compromise.

**Example 3.4.1** Let $x = $ `TACCTGTGCTGTTC` and $y = $ `TACCGGTGTTC`, where $y$ arose from $x$ by deleting `TGT` after position $4$ and substituting one base. With match $+1$, mismatch $-1$ and the linear penalty $g(k) = 2k$, the optimal alignment is

```text
TACCTGTGCTGTTC
TACC-G-G-TGTTC
```
with three separate one-base gaps and score $11 - 6 = 5$. With the affine penalty $g(k) = 5 + (k - 1)$, the optimal alignment is

```text
TACCTGTGCTGTTC
TACC---GGTGTTC
```
with one gap of length $3$ and one mismatch, score $10 - 1 - 7 = 2$, the alignment that reflects the history. Under the linear scheme this alignment scores $3$, and under the affine scheme the first one scores $-4$: the gap model, not the algorithm, decides which history is reconstructed.

## 3.5. Dynamic Programming

### 3.5.1. Alignments as Paths

Write $x$ down the rows and $y$ across the columns of a grid with nodes $(i, j)$, $0 \le i \le m$, $0 \le j \le n$, the *edit graph*. A diagonal step from $(i-1, j-1)$ to $(i, j)$ aligns $x_i$ with $y_j$, a vertical step aligns $x_i$ with a gap and a horizontal step aligns $y_j$ with a gap. Global alignments are exactly the paths from $(0, 0)$ to $(m, n)$, and the score of an alignment with linear gap penalty is the sum of the weights of the edges of its path.

**Formula 3.5.1 (Number of Alignments)** The number of global alignments of sequences of lengths $m$ and $n$ is the Delannoy number

$$
D(m, n) = D(m-1, n-1) + D(m-1, n) + D(m, n-1), \qquad D(i, 0) = D(0, j) = 1;
$$
the number of distinct sets of aligned pairs, which ignores the order of adjacent gaps in the two rows, is $\binom{m+n}{n} = \sum_k\binom{m}{k}\binom{n}{k}$.

For $m = n = 300$, $\binom{600}{300} = 1.35\times10^{179}$ and $D(300, 300) \approx 1.5\times10^{228}$; enumeration is out of the question. For $m = n = 3$, $D = 63$ and $\binom{6}{3} = 20$.

The edit graph makes the problem a longest-path problem in a directed acyclic graph, solvable by **dynamic programming**: the best path to $(i, j)$ ends with one of three steps, and its remainder is a best path to the predecessor node (optimal substructure).

**Definition 3.5.1 (Edit Distance)** The **edit distance** (Levenshtein distance) between two strings is the minimum number of single-character substitutions, insertions and deletions that transform one into the other.

The edit distance is the negative of the optimal global alignment score with match $0$, mismatch $-1$ and linear gap penalty $1$. The length of the **longest common subsequence** ([4.3.1](/4.3.1#def-1.6.1)) is the optimal global score with match $1$, mismatch $-\infty$ (forbidden) and gap $0$. Sequence alignment generalizes both by weighting the operations with biologically estimated scores.

### 3.5.2. Global Alignment: Needleman–Wunsch

**Algorithm 3.5.1 (Needleman–Wunsch Algorithm)** Input: sequences $x_1 \cdots x_m$, $y_1 \cdots y_n$, a substitution matrix $s$ and a linear gap penalty $d$. Let $F(i, j)$ be the best score of an alignment of $x_1 \cdots x_i$ with $y_1 \cdots y_j$.

1. Initialization: $F(0, 0) = 0$, $F(i, 0) = -id$, $F(0, j) = -jd$.
2. Recursion, for $i = 1, \dots, m$ and $j = 1, \dots, n$:

$$
F(i, j) = \max\begin{cases}F(i-1, j-1) + s(x_i, y_j) & x_i \text{ aligned with } y_j,\\ F(i-1, j) - d & x_i \text{ aligned with a gap},\\ F(i, j-1) - d & y_j \text{ aligned with a gap}.\end{cases}
$$
3. Termination: the optimal score is $F(m, n)$.
4. Traceback: from $(m, n)$, repeatedly move to a predecessor cell that attains the maximum, writing the corresponding column, until $(0, 0)$.

The Needleman–Wunsch algorithm (1970; this form with explicit gap costs is due to Sellers and Gotoh) takes $O(mn)$ time and $O(mn)$ space; the traceback takes $O(m + n)$ time. It returns one optimal alignment; when several predecessors attain the maximum, there are several, and the choice among them (a fixed preference for diagonal steps, say) is arbitrary.

**Theorem 3.5.1** $F(i, j)$ computed by the recursion of Algorithm 3.5.1 is the maximum score over all alignments of $x_1 \cdots x_i$ and $y_1 \cdots y_j$.

**Proof** By induction on $i + j$. For $i = 0$ or $j = 0$ there is only one alignment (all gaps), with the stated score. For $i, j \ge 1$, the last column of any alignment of the prefixes is $(x_i, y_j)$, $(x_i, -)$ or $(-, y_j)$, and removing it leaves an alignment of $(x_1 \cdots x_{i-1}, y_1 \cdots y_{j-1})$, $(x_1 \cdots x_{i-1}, y_1 \cdots y_j)$ or $(x_1 \cdots x_i, y_1 \cdots y_{j-1})$ respectively. Since the score is additive over columns, the best alignment with a given last column consists of that column and a best alignment of the remaining prefixes, whose score is $F$ of the predecessor by the induction hypothesis. The maximum over the three cases is $F(i, j)$. $\square$

**Example 3.5.1** Align $x = $ `AAG` (columns) with $y = $ `AGC` (rows), with the nucleotide matrix of Question 2 (match $2$; transition $-5$; transversion $-7$) and $d = 5$. The matrix $F$ is

| | $-$ | A | A | G |
|---|---|---|---|---|
| $-$ | $0$ | $-5$ | $-10$ | $-15$ |
| A | $-5$ | $2$ | $-3$ | $-8$ |
| G | $-10$ | $-3$ | $-3$ | $-1$ |
| C | $-15$ | $-8$ | $-8$ | $-6$ |

For instance $F(\mathrm{G}, \mathrm{G}_3) = \max(-3 + 2, -8 - 5, -3 - 5) = -1$. The optimal score is $-6$, attained by two alignments, `AAG-` over `-AGC` and `AAG-` over `A-GC`, which differ in which A is aligned: the cell $F(\mathrm{A}, \mathrm{A}_2) = -3$ is reached both diagonally (from $-5$, plus $2$) and horizontally (from $2$, minus $5$).

### 3.5.3. Local Alignment: Smith–Waterman

Two proteins often share only a domain, and a gene is found in a genome as a short stretch of a long sequence. A local alignment finds the best-scoring pair of substrings.

**Algorithm 3.5.2 (Smith–Waterman Algorithm)** As Algorithm 3.5.1, with three changes:

1. Initialization: $F(i, 0) = F(0, j) = 0$.
2. Recursion: $F(i, j) = \max\{0,\ F(i-1, j-1) + s(x_i, y_j),\ F(i-1, j) - d,\ F(i, j-1) - d\}$.
3. Termination and traceback: the optimal score is $\max_{i,j}F(i, j)$; the traceback starts at a cell attaining it and stops at the first cell with value $0$.

The option $0$ in the Smith–Waterman algorithm (1981) means "start a new alignment here": $F(i, j)$ is the best score of an alignment of a suffix of $x_1 \cdots x_i$ with a suffix of $y_1 \cdots y_j$, the empty alignment scoring $0$. The algorithm finds a meaningful local alignment only if the expected score of a random column is negative; otherwise long random alignments accumulate positive scores, the best local alignment extends over most of both sequences, and its score grows linearly with length instead of logarithmically. This is the phase transition of Arratia and Waterman (1994), and the reason why the condition of [7.6.41](/7.6.41#thm-41.2.1) appears in the statistics of [7.8.4](/7.8.4).

**Example 3.5.2** For the sequences of Example 3.5.1 the local matrix has rows $(0, 0, 0, 0)$, $(0, 2, 2, 0)$, $(0, 0, 0, 4)$, $(0, 0, 0, 0)$ (row $-$, A, G, C); the maximum $4$ at (G, $\mathrm{G}_3$) traces back through either $2$, giving the local alignment `AG` over `AG` with score $4$, starting at the first or the second A of $x$.

**Example 3.5.3 (A Protein Pair)** The classic textbook pair $x = $ `HEAGAWGHEE` and $y = $ `PAWHEAE` (Durbin and colleagues 1998), scored with BLOSUM50 and $d = 8$, has optimal global score $1$ but optimal local score $28$, attained by `AWGHE` over `AW-HE`. The global alignment is forced to align the unrelated flanks, whose negative scores almost cancel the conserved core.

![Dynamic-programming matrices for x = HEAGAWGHEE (columns) and y = PAWHEAE (rows), BLOSUM50 and a linear gap penalty of 8. Shaded cells are the traceback, arrows point to the predecessor that attains the maximum. A: Needleman–Wunsch; the traceback runs from the bottom-right cell, score 1, to the top-left corner and gives HEAGAWGHE-E over --P-AW-HEAE. B: Smith–Waterman; negative values are replaced by 0, and the traceback runs from the maximum, 28, to the first zero and gives AWGHE over AW-HE](./plots/dp-matrices.py)

The two algorithms in Python, in a direct transcription of the recursions:

```python
import numpy as np

def needleman_wunsch(x, y, s, d):
    """Global alignment with linear gap penalty d (> 0); s(a, b) is the substitution score."""
    m, n = len(x), len(y)
    F = np.zeros((m + 1, n + 1))
    F[:, 0] = -d * np.arange(m + 1)
    F[0, :] = -d * np.arange(n + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            F[i, j] = max(F[i - 1, j - 1] + s(x[i - 1], y[j - 1]),
                          F[i - 1, j] - d, F[i, j - 1] - d)
    # traceback from the bottom-right corner (diagonal preferred on ties)
    a, b, i, j = [], [], m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and F[i, j] == F[i - 1, j - 1] + s(x[i - 1], y[j - 1]):
            a.append(x[i - 1]); b.append(y[j - 1]); i -= 1; j -= 1
        elif i > 0 and F[i, j] == F[i - 1, j] - d:
            a.append(x[i - 1]); b.append("-"); i -= 1
        else:
            a.append("-"); b.append(y[j - 1]); j -= 1
    return F[m, n], "".join(reversed(a)), "".join(reversed(b))

def smith_waterman(x, y, s, d):
    """Local alignment: the same recursion with a floor at 0, traced back from the maximum."""
    m, n = len(x), len(y)
    F = np.zeros((m + 1, n + 1))
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            F[i, j] = max(0.0, F[i - 1, j - 1] + s(x[i - 1], y[j - 1]),
                          F[i - 1, j] - d, F[i, j - 1] - d)
    i, j = np.unravel_index(np.argmax(F), F.shape)
    best, a, b = F[i, j], [], []
    while F[i, j] > 0:
        if F[i, j] == F[i - 1, j - 1] + s(x[i - 1], y[j - 1]):
            a.append(x[i - 1]); b.append(y[j - 1]); i -= 1; j -= 1
        elif F[i, j] == F[i - 1, j] - d:
            a.append(x[i - 1]); b.append("-"); i -= 1
        else:
            a.append("-"); b.append(y[j - 1]); j -= 1
    return best, "".join(reversed(a)), "".join(reversed(b))

# needleman_wunsch("HEAGAWGHEE", "PAWHEAE", blosum50, 8) -> (1.0, 'HEAGAWGHE-E', '--P-AW-HEAE')
# smith_waterman("HEAGAWGHEE", "PAWHEAE", blosum50, 8)   -> (28.0, 'AWGHE', 'AW-HE')
```

### 3.5.4. Affine Gaps: Gotoh's Algorithm

With an affine penalty the score of a column depends on whether the previous column was already a gap in the same row, so one matrix is no longer enough: the state of the path (in a match, or in a gap in $x$ or in $y$) must be remembered.

**Algorithm 3.5.3 (Gotoh's Algorithm)** For the affine penalty $g(k) = d + (k-1)e$ keep three matrices: $M(i, j)$, the best score of an alignment of the prefixes ending with $x_i$ aligned to $y_j$; $I_x(i, j)$, ending with $x_i$ aligned to a gap; $I_y(i, j)$, ending with $y_j$ aligned to a gap. Initialize $M(0, 0) = 0$, $I_x(i, 0) = -d - (i-1)e$, $I_y(0, j) = -d - (j-1)e$ and all other boundary cells to $-\infty$. Then

$$
\begin{aligned}
M(i, j) &= s(x_i, y_j) + \max\{M(i-1, j-1),\ I_x(i-1, j-1),\ I_y(i-1, j-1)\},\\
I_x(i, j) &= \max\{M(i-1, j) - d,\ I_x(i-1, j) - e,\ I_y(i-1, j) - d\},\\
I_y(i, j) &= \max\{M(i, j-1) - d,\ I_y(i, j-1) - e,\ I_x(i, j-1) - d\}.
\end{aligned}
$$
The optimal global score is $\max\{M(m, n), I_x(m, n), I_y(m, n)\}$; the traceback moves between the three matrices. For local alignment, add the option $0$ to $M$ and take the maximum over all cells.

Gotoh (1982) thus keeps $O(mn)$ time with a constant factor of about three, whereas a general gap function $g(k)$ requires $O(mn(m + n))$ time because every gap length must be tried. The three matrices are the three states of a finite automaton, and of the pair hidden Markov model of [7.8.5](/7.8.5), whose Viterbi path is an optimal alignment. The transition from $I_x$ directly to $I_y$ allows a gap in one sequence to be followed immediately by a gap in the other; some implementations forbid it, which rarely matters: one residue gapped in each row costs $2d$, more than aligning the two residues as a mismatch under any usual matrix.

The library implementations are what one uses in practice; Biopython's aligner implements Gotoh's algorithm in C:

```python
from Bio import Align
from Bio.Align import substitution_matrices

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -12      # first position of a gap: existence 11 + extension 1
aligner.extend_gap_score = -1     # each further position
aligner.mode = "local"            # or "global"
alignment = aligner.align(human_mcm6, yeast_mcm6)[0]
print(alignment.score)            # 1711.0
print(alignment.counts())         # identities=385, mismatches=412, gaps=109
```

```bash
# The same with EMBOSS: water (Smith-Waterman) and needle (Needleman-Wunsch), affine gaps
water  -asequence MCM6_HUMAN.fa -bsequence MCM6_YEAST.fa -datafile EBLOSUM62 \
       -gapopen 10 -gapextend 0.5 -outfile mcm6.water
needle -asequence MCM6_HUMAN.fa -bsequence MCM6_YEAST.fa -gapopen 10 -gapextend 0.5 -outfile mcm6.needle
```

### 3.5.5. Semi-Global Alignment

Many problems lie between global and local alignment: a read should be aligned completely, but to any part of a chromosome; two overlapping reads share a suffix of one and a prefix of the other; a gene sequence should be matched completely to a slightly longer genomic region.

**Definition 3.5.2 (Semi-Global Alignment)** A **semi-global alignment** (end-gap-free or overlap alignment) is a global alignment in which gaps at the beginning or end of one or both sequences are not penalized.

All variants use the same recursion and differ only in boundary conditions and in where the traceback starts:

| Variant | Initialization | Optimal score at | Use |
|---|---|---|---|
| Global | $F(i, 0) = -id$, $F(0, j) = -jd$ | $F(m, n)$ | two complete homologous sequences |
| Local | $F(i, 0) = F(0, j) = 0$, floor at $0$ | $\max_{i,j}F(i, j)$ | shared domains, unknown extent |
| $x$ inside $y$ ("glocal") | $F(i, 0) = -id$, $F(0, j) = 0$ | $\max_jF(m, j)$ | a read or a gene inside a genome |
| Overlap | $F(i, 0) = F(0, j) = 0$ | $\max\{\max_jF(m, j), \max_iF(i, n)\}$ | overlapping reads in assembly ([7.8.11](/7.8.11)) |

Free end gaps matter. In a global alignment of human MCM6 ($821$ residues) to yeast Mcm6 ($1017$), the yeast-specific N-terminal extension of about $100$ residues is charged as a terminal gap; the global score is $1608$, and the alignment has $202$ gap columns and $38.7\,\%$ identity, against the local score $1711$ over $906$ columns with $42.5\,\%$ identity. The alignment of the conserved part is nearly the same; what differs is how the unalignable ends are charged.

### 3.5.6. Ties, Suboptimal Alignments and Reliability

An optimal alignment is a point estimate. Different scoring parameters can give different optimal alignments, near-optimal alignments may differ from the optimum in large regions, and positions of gaps in poorly conserved regions are often arbitrary. Two tools quantify this. Parametric alignment computes how the optimal alignment changes as the gap penalties vary. Probabilistic alignment computes, with the forward and backward algorithms of a pair hidden Markov model ([7.8.5](/7.8.5)), the posterior probability that $x_i$ is aligned to $y_j$, summed over all alignments; columns with high posterior probability are reliable, and the *maximum expected accuracy* alignment, which maximizes the sum of posterior probabilities of its columns, is often more accurate than the Viterbi (highest-scoring) alignment. Downstream analyses that are sensitive to alignment errors, such as the detection of positive selection, mask unreliable columns.

## 3.6. Alignment at Scale

### 3.6.1. Linear Space: Hirschberg's Algorithm

The full matrix of two $100$-kb sequences has $10^{10}$ cells, $40$ GB at four bytes per cell. The score alone needs only two rows at a time, but the traceback seems to need the whole matrix. Hirschberg (1975) showed that it does not.

**Algorithm 3.6.1 (Hirschberg's Algorithm)** To align $x_1 \cdots x_m$ with $y_1 \cdots y_n$ globally:

1. If $m \le 1$, align directly.
2. Let $h = \lfloor m/2\rfloor$. Compute the last row $f(j)$ of the forward matrix of $x_1 \cdots x_h$ against $y$, and the last row $r(j)$ of the matrix of the reversed sequences $x_m \cdots x_{h+1}$ against $y_n \cdots y_1$, read backwards, so that $r(j)$ is the best score of aligning $x_{h+1} \cdots x_m$ with $y_{j+1} \cdots y_n$. Both need only $O(n)$ space.
3. Let $j^* = \arg\max_j[f(j) + r(j)]$: an optimal path crosses row $h$ at column $j^*$.
4. Recursively align $x_1 \cdots x_h$ with $y_1 \cdots y_{j^*}$ and $x_{h+1} \cdots x_m$ with $y_{j^*+1} \cdots y_n$, and concatenate.

**Theorem 3.6.1** Hirschberg's algorithm computes an optimal global alignment in $O(mn)$ time and $O(m + n)$ space.

**Proof** Correctness: every global path crosses row $h$ at some column $j$, and the best path through $(h, j)$ has score $f(j) + r(j)$ (best prefix part plus best suffix part, by additivity), so $j^*$ lies on an optimal path, and optimal alignments of the two parts concatenate to an optimal alignment. Time: the work at the top level is about $mn$ cells; the two subproblems have sizes $h \times j^*$ and $(m - h) \times (n - j^*)$, with total area $\frac{m}{2}j^* + \frac{m}{2}(n - j^*) = mn/2$, and in general level $k$ costs $mn/2^k$, so the total is less than $2mn$. Space: each level stores two rows and the recursion depth is $\log_2 m$. $\square$

![Hirschberg's linear-space alignment of two DNA sequences of 30 and 28 bases (match +1, mismatch −1, gap −2; the second sequence lacks five bases of the first and carries three substitutions and a 3-base insertion). A: each subproblem (rectangle, darker for earlier levels of the recursion) is split at its middle row (dashed); the column where the optimal path crosses that row is found from the forward and reverse score rows, and the crossing points (dots) chain into the optimal path (line). B: the cells evaluated at each level of the recursion halve from level to level (bars), as mn/2^level (points), for a total of less than 2mn](./plots/hirschberg.py)

Myers and Miller (1988) extended the method to affine gaps; it is used whenever long sequences are aligned with traceback, for example in the final alignment step of genome-to-genome aligners.

### 3.6.2. Banded and Bounded Alignment

If two sequences are known to be similar, their optimal path stays near the main diagonal. *Banded alignment* fills only the cells with $\lvert i - j\rvert \le w$, in $O(w(m + n))$ time; the result is optimal if the optimal path never leaves the band, which is guaranteed when the number of indels, or more precisely their net offset at every point, is at most $w$. Read aligners extend a seed match ([7.8.10](/7.8.10)) by banded alignment, and *X-drop* alignment ([7.8.4](/7.8.4)) instead prunes the cells whose score has fallen more than $X$ below the best score seen so far, adapting the band to the data. For two sequences at edit distance $s$, the *wavefront algorithm* (WFA, Marco-Sola and colleagues 2021) computes, for increasing score $s$, the furthest-reaching diagonal points with that score; it runs in $O(ns)$ time and is extremely fast for similar sequences such as long reads against a reference.

### 3.6.3. Hardware

The cells of one anti-diagonal of the matrix are independent and can be computed in parallel. Single-instruction multiple-data (SIMD) instructions of modern processors compute $16$ to $64$ cells at once; Farrar's (2007) *striped* layout arranges the query in segments so that the dependence along a column is handled by a rarely needed correction loop. Libraries such as parasail and SSW reach $10^{10}$ to $10^{11}$ cell updates per second on one processor, and graphics processors more. At $10^{10}$ cells per second, a full Smith–Waterman comparison of an $821$-residue query with a database of $10^{11}$ residues takes about $8000$ seconds, more than two hours, which is why database searches use the heuristics of [7.8.4](/7.8.4).

```python
# Striped SIMD Smith-Waterman with parasail (gap open and extension penalties; check the convention)
import parasail
result = parasail.sw_trace_striped_16(human_mcm6, yeast_mcm6, 11, 1, parasail.blosum62)
print(result.score, result.cigar.decode)
```

## 3.7. How High Is a Good Score?

An alignment algorithm always returns an optimal alignment, even of unrelated sequences. To judge a score we must compare it with the scores of sequences that are not related. The simplest empirical test shuffles one sequence many times, which keeps its length and composition but destroys any homology, and aligns the query to each shuffle.

**Formula 3.7.1 (Shuffle Z-Score)** If the shuffled sequences give scores with mean $\bar S$ and standard deviation $\hat\sigma$, the z-score of the observed score $S$ is $Z = (S - \bar S)/\hat\sigma$.

**Example 3.7.1** Aligning human MCM6 to $300$ shuffles of yeast Mcm6 gives global scores with mean $-242.6$ and standard deviation $22.9$ (the real score $1608$ has $Z = 81$), and local scores with mean $42.8$, standard deviation $4.7$ and maximum $62$ (the real score $1711$ has $Z = 355$). The orthologs are related far beyond doubt; for the twilight zone the question is decided in the tail of the null distribution.

![Significance by shuffling: human MCM6 aligned with BLOSUM62 and affine gaps (11 + k) to 300 shuffles of yeast Mcm6, which keep its length and composition. A: global scores; B: local scores. The real scores, 1608 and 1711, lie 81 and 355 standard deviations above the mean of the shuffles (dashed), far off scale. The local scores of shuffled pairs are small and skewed to the right, the shape of the extreme-value distribution of 7.8.4](./plots/shuffle-test.py)

The z-score assumes a normal null distribution, but the scores of optimal local alignments of random sequences are maxima over many possible alignments and follow an extreme-value distribution with a long right tail, so normal tail probabilities are much too small. For local alignments the theory of Karlin and Altschul gives the exact form of the tail, and with it the E-value used by every database search; this is the subject of [7.8.4](/7.8.4).

## Summary

| Topic | Key points |
|---|---|
| Alignment | columns of homologous residues with gaps (Definition 3.1.1); identity depends on the denominator (Definition 3.1.2, Example 3.1.1); twilight zone at $20$–$35\,\%$ identity; align coding sequences as proteins |
| Dot plots | windowed matches (Definition 3.2.1) reveal repeats, inversions and indels without a scoring model |
| Substitution scores | log-odds $s = \lambda^{-1}\ln[p_{ab}/(q_aq_b)]$; every matrix implies target frequencies; relative entropy $H$ in bits per pair (Definition 3.3.1) |
| PAM | 1 PAM = $1\,\%$ accepted change; PAM$n$ from $M^n$ of a reversible Markov chain (Definition 3.3.2, Algorithm 3.3.1); $80\,\%$ difference at PAM250; reconstruction in Example 3.3.1 |
| BLOSUM | log-odds from ungapped blocks, clustered at $L\,\%$ identity, half-bit units (Definition 3.3.3, Algorithm 3.3.2); BLOSUM62 default, $H = 0.58$ bits (BLAST background) $\approx$ PAM183 |
| Choice | high-$H$ matrices for short or close sequences, low-$H$ for distant; DNA $r/{-p}$ sets the target identity (Section 3.3.5) |
| Gaps | linear $dk$ or affine $d + (k-1)e$ (Definition 3.4.1); affine = geometric gap lengths; the gap model decides the reconstructed history (Example 3.4.1) |
| Algorithms | alignments are paths in the edit graph, Delannoy-many (Formula 3.5.1); Needleman–Wunsch (Algorithm 3.5.1, Theorem 3.5.1), Smith–Waterman with floor $0$ (Algorithm 3.5.2), Gotoh's three matrices (Algorithm 3.5.3), semi-global variants; all $O(mn)$ |
| Relatives | edit distance (Definition 3.5.1) and LCS are special scoring schemes |
| Scale | Hirschberg linear space, $< 2mn$ time (Algorithm 3.6.1, Theorem 3.6.1); banded, X-drop, wavefront; SIMD at $10^{10}$ cells/s |
| Significance | shuffle z-scores (Formula 3.7.1, Example 3.7.1); local scores are extreme-value distributed ([7.8.4](/7.8.4)) |

## Questions

1. The local alignment of human and yeast MCM6 in Example 3.1.1 has $385$ identities, $412$ mismatches and $109$ gap columns. Compute its identity in the three conventions of Definition 3.1.2, and explain why identities reported by different programs for the same pair can differ by several percentage points.

   **Answer** Columns: $385 + 412 + 109 = 906$, so $385/906 = 42.5\,\%$; aligned pairs: $385/797 = 48.3\,\%$; shorter sequence ($821$ residues): $385/821 = 46.9\,\%$. Programs also differ in the alignment itself (global or local, matrix and gap parameters, whether terminal gaps are counted), so the global alignment of the same pair, with $395$ identities over $1020$ columns, gives only $38.7\,\%$. An identity is meaningful only with its alignment method and denominator.

2. With the nucleotide matrix (match $2$, transition $-5$, transversion $-7$) and a linear gap penalty of $5$, score the three alignments `GAATC`/`CATAC`, `GAAT-C`/`C-ATAC` and `GAATC-`/`CA-TAC`. Which is best?

   **Answer** `GAATC`/`CATAC`: G–C transversion $-7$, A–A $2$, A–T $-7$, T–A $-7$, C–C $2$, total $-17$. `GAAT-C`/`C-ATAC`: G–C $-7$, A–gap $-5$, A–A $2$, T–T $2$, gap–A $-5$, C–C $2$, total $-11$. `GAATC-`/`CA-TAC`: G–C $-7$, A–A $2$, A–gap $-5$, T–T $2$, C–A $-7$, gap–C $-5$, total $-20$. The second is the best of the three; the gaps buy two extra matches, which pays because a gap ($-5$) costs less than a transversion ($-7$).

3. Fill the Needleman–Wunsch matrix for $x = $ `ACG` and $y = $ `AG` with match $+1$, mismatch $-1$ and $d = 2$, and give the optimal alignment.

   **Answer** With $x$ down the rows and $y$ across: row $0$: $0, -2, -4$; row A: $-2, 1, -1$; row C: $-4, -1, 0$; row G: $-6, -3, 0$. For example $F(\mathrm{C}, \mathrm{G}) = \max(1 - 1, -1 - 2, -1 - 2) = 0$ and $F(\mathrm{G}, \mathrm{G}) = \max(-1 + 1, 0 - 2, -3 - 2) = 0$. The optimal score is $0$, from `ACG` over `A-G` (two matches, one gap: $2 - 2$).

4. For DNA scored $+1/{-1}$ and $+1/{-3}$, compute $\lambda$ and the implied target identity, and say which scheme you would use to find a $70\,\%$-identical homolog.

   **Answer** For $+1/{-1}$: $\frac{1}{4}\mathrm{e}^{\lambda} + \frac{3}{4}\mathrm{e}^{-\lambda} = 1$ gives $\mathrm{e}^\lambda = 3$, $\lambda = \ln 3 = 1.099$, target identity $3/4 = 75\,\%$. For $+1/{-3}$: solving numerically gives $\lambda = 1.374$, $\mathrm{e}^{\lambda} = 3.95$, target identity $98.8\,\%$. A $70\,\%$-identical homolog has $0.7 - 3 \times 0.3 = -0.2$ expected score per column under $+1/{-3}$, so its alignment breaks up; under $+1/{-1}$ it gains $0.4$ per column. Use $+1/{-1}$, whose target identity is close to the true one.

5. Why does the Smith–Waterman algorithm require the expected score of a random pair to be negative? What happens to local alignments of unrelated proteins scored with BLOSUM62 plus $1$ on every entry?

   **Answer** If the expected score is positive, a random alignment gains score on average with every column, so the best local alignment extends over essentially the whole length and its score grows linearly with the lengths; local alignment degenerates into global alignment, and high scores no longer indicate homology. BLOSUM62 has expected score $-0.95$ per random pair (Section 3.3.1); adding $1$ to every entry makes it $+0.05$, just positive, so unrelated proteins would produce long alignments with large scores. This is the linear phase of Arratia and Waterman; the logarithmic phase, needed for the statistics of [7.8.4](/7.8.4), requires a negative expected score.

6. One PAM changes $1\,\%$ of residues. Why do sequences $250$ PAM apart still share about $20\,\%$ of residues rather than $0.99^{250} = 8.1\,\%$, and what is the limit for very large distances?

   **Answer** $0.99^{250}$ is the probability that a site never changes. But a site that has changed can return to its original residue (or change several times and end at the same one), so the observed identity exceeds the fraction of unchanged sites; moreover mutability varies, and slowly changing residues such as tryptophan and cysteine are retained with probability above $0.5$ at PAM250 (Example 3.3.1), raising the average. As $n \to \infty$, $M^n$ converges to the stationary distribution, every column of $M^n$ becomes $q$, and the identity tends to $\sum_a q_a^2 \approx 6\,\%$: the sequences become effectively unrelated.

7. Example 3.4.1 compares a linear and an affine gap penalty. Verify the four scores ($5$ and $3$ under the linear scheme, $-4$ and $2$ under the affine scheme) and explain in terms of the mutational process why the affine alignment is preferable.

   **Answer** The first alignment has $11$ matches and three gaps of length $1$: linear $11 - 3 \times 2 = 5$, affine $11 - 3 \times 5 = -4$. The second has $10$ matches, one mismatch and one gap of length $3$: linear $10 - 1 - 6 = 3$, affine $10 - 1 - (5 + 2) = 2$. The linear scheme charges a $3$-base gap the same as three $1$-base gaps, so it prefers to scatter them to gain a match; but three separate deletions are three mutational events and one deletion of $3$ bases is one, so the affine scheme, which charges mainly for events, prefers the parsimonious history.

8. Two bacterial chromosomes of $5\,\mathrm{Mb}$ each are to be aligned globally. Estimate the memory of a full dynamic-programming matrix at one byte per cell, of Hirschberg's algorithm and of a banded alignment with $w = 1000$, and the time at $10^{10}$ cells per second.

   **Answer** Full matrix: $(5\times10^6)^2 = 2.5\times10^{13}$ cells, $25\,\mathrm{TB}$; time $2500$ s. Hirschberg: two rows of $5\times10^6$ scores, a few tens of megabytes, time at most twice as long, about $5000$ s. Banded: $(2w + 1) \times 5\times10^6 \approx 10^{10}$ cells, $10\,\mathrm{GB}$ with traceback (or linear space with Hirschberg inside the band), time about $1$ s. In practice whole-genome aligners first find anchors (exact or seed matches, [7.8.4](/7.8.4)), chain them, and align only the gaps between anchors, since large rearrangements (Section 3.2) violate any band.

9. Show that the number of global alignments of two sequences of length $3$ is $63$, and that there are $20$ distinct sets of aligned pairs. Why does the second count matter more for alignment algorithms?

   **Answer** The Delannoy recursion gives $D(1,1) = 3$, $D(2,1) = 5$, $D(2,2) = D(1,1) + D(1,2) + D(2,1) = 13$, $D(3,1) = 7$, $D(3,2) = D(2,1) + D(2,2) + D(3,1) = 25$, $D(3,3) = D(2,2) + D(2,3) + D(3,2) = 13 + 25 + 25 = 63$. A set of $k$ aligned pairs is chosen as $k$ positions of each sequence matched in order, in $\binom{3}{k}^2$ ways: $1 + 9 + 9 + 1 = 20 = \binom{6}{3}$. Alignments with the same aligned pairs differ only in the order of adjacent gaps in the two rows (`A-`/`-C` versus `-A`/`C-`), which have the same score under any gap penalty that charges gaps per row; dynamic programming effectively optimizes over the sets of aligned pairs, and the order of adjacent gaps is a convention of the traceback.

10. (Design) You want to (a) find whether a $300$-nt human non-coding element is conserved in the mouse genome, (b) compare the protein products of two bacterial genes that share one of three domains, and (c) align a $150$-nt read to a $1$-kb amplicon reference. For each, choose the alignment mode, the scoring system and the algorithm.

    **Answer** (a) Search the human element against the mouse genome: a local alignment (it may be partially conserved) with a DNA scheme suited to the divergence of non-coding sequence between human and mouse (about $70\,\%$ identity where conserved, so $+1/{-1}$ or a blastn-like $2/{-3}$ with affine gaps), using a fast seeded search ([7.8.4](/7.8.4)) since the genome is $2.7\,\mathrm{Gb}$; confirm with Smith–Waterman on the region found. (b) Local alignment of the proteins (Smith–Waterman–Gotoh with BLOSUM62, gaps $11 + k$), which reports the shared domain instead of forcing the unrelated domains into a global alignment; judge the score with the E-value of [7.8.4](/7.8.4). (c) Semi-global ("glocal") alignment: the read must be aligned end to end but may lie anywhere in the reference, so end gaps in the reference are free and in the read are penalized; a nucleotide scheme for near-identical sequences ($+1/{-2}$ or $+1/{-4}$ with affine gaps) and banded or full Gotoh alignment, cheap for $150 \times 1000$ cells.
