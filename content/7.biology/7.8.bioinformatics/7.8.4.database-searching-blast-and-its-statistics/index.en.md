---
title: "Database Searching: BLAST and Its Statistics"
description: "Why exhaustive Smith–Waterman search is too slow for modern databases; FASTA and the BLAST algorithm (neighborhood words, two-hit seeding, X-drop ungapped and gapped extension) with the speed–sensitivity trade-off computed for BLOSUM62; the statistics of local alignment scores (Erdős–Rényi law, Gumbel distribution, Karlin–Altschul E-values, bit scores, effective lengths, composition-based statistics) checked against simulation; low-complexity filtering; the BLAST family, BLAT and spaced seeds; DIAMOND, MMseqs2 and sequence clustering; running and reading a search, with human MCM6 as the example."
---

A new sequence becomes interesting when it can be related to sequences already studied. The first step of almost every analysis of a gene or protein is therefore a search of a database for similar sequences: to guess the function of an unknown protein, to find the orthologs of a gene in other species, to identify the organism a read comes from, or to check whether a primer matches anything besides its target. The previous chapter ([7.8.3](/7.8.3)) gave the optimal algorithm for comparing two sequences; applied to every sequence of a database it is too slow by orders of magnitude. This chapter describes how BLAST and its successors make the search fast, by first finding short word matches ("seeds") and extending only those, and how a score is turned into a statement of significance, the E-value. The statistical theory, the extreme-value distribution of the best score of random sequences due to Karlin and Altschul, was stated in [7.6.41](/7.6.41#thm-41.2.1) and used for genome annotation in [7.4.14](/7.4.14#sec-14.5); here we explain its practical use, verify it by simulation and show where it needs corrections. Multiple alignments and profiles, which make searches more sensitive, follow in [7.8.5](/7.8.5); the mapping of millions of reads to one genome, a search problem of a different shape, in [7.8.10](/7.8.10).

## 4.1. The Scale of the Problem

UniProtKB contained about $2.5\times10^8$ protein sequences in 2024, and the NCBI non-redundant protein database (nr) is of the same order; at an average length of about $350$ residues this is of the order of $10^{11}$ residues. A Smith–Waterman comparison of a query of $m = 821$ residues (human MCM6) against $n = 10^{11}$ residues fills $mn \approx 8\times10^{13}$ cells; at $10^{10}$ cells per second, the speed of a well-vectorized implementation on one processor ([7.8.3](/7.8.3#sec-3.6.3)), this takes about $8000$ seconds, more than two hours, for a single query. Analyses that compare a whole proteome or a metagenome of $10^6$ to $10^8$ sequences against such a database are out of reach.

Two observations make the problem tractable. First, a database contains very few true homologs of a given query, and the alignments of unrelated pairs need not be computed exactly: it suffices to recognize quickly that they score poorly. Second, alignments of real homologs almost always contain short segments of high similarity. A heuristic search finds such segments with an index or a lookup table and computes alignments only around them. It may miss a homolog that a full search would find; the fraction found is its sensitivity, and the price paid for it is time. The art of search algorithms is to place this trade-off well.

## 4.2. FASTA

The first widely used heuristic, FASTA (Lipman and Pearson 1985; Pearson and Lipman 1988), already contains the main ideas.

**Algorithm 4.2.1 (FASTA)** For a query $x$ and each database sequence $y$:

1. Find all exact matches of words of length $k$ (*ktup*, $2$ for proteins, $6$ for DNA) between $x$ and $y$ with a lookup table of the query words.
2. For each diagonal $i - j$, combine the word matches into the ten best ungapped regions and rescore them with a substitution matrix.
3. Join compatible regions on neighboring diagonals, allowing gaps, into an approximate alignment.
4. For the best-scoring database sequences, compute an optimal alignment by dynamic programming in a band around the best diagonals.

FASTA established the pattern of *filter, then align*. Its statistics were empirical: the scores of all database sequences form a distribution dominated by unrelated sequences, against which a high score is judged. The FASTA program (now FASTA36) is still maintained and remains one of the most sensitive heuristic tools; the FASTA file format ([7.8.1](/7.8.1#sec-1.4.1)) was introduced with it.

## 4.3. BLAST

### 4.3.1. Neighborhood Words and Seeds

**Definition 4.3.1 (BLAST)** **BLAST** (Basic Local Alignment Search Tool; Altschul, Gish, Miller, Myers and Lipman 1990) is a family of programs that find local alignments between a query and the sequences of a database by locating short high-scoring word pairs, extending them into alignments, and reporting each alignment with an E-value computed from the statistics of local alignment scores.

BLAST differs from FASTA in what counts as a seed. Instead of exact word matches it uses words that score highly with the substitution matrix, so that conservative substitutions also produce hits.

**Definition 4.3.2 (Neighborhood and Seed Match)** For a query word $u$ of length $W$, its neighborhood with threshold $T$ is the set of words $v$ of length $W$ with $\sum_{k=1}^W s(u_k, v_k) \ge T$. A **seed match** (word hit) is a pair of positions $(i, j)$ at which the database word $y_j \cdots y_{j+W-1}$ lies in the neighborhood of the query word $x_i \cdots x_{i+W-1}$.

**Example 4.3.1** With BLOSUM62 and $W = 3$, the query word PQG scores $7 + 5 + 6 = 18$ with itself. Its neighborhood for $T = 13$ consists of $9$ words: PQG ($18$), PEG ($15$), PRG and PKG ($14$), and PNG, PDG, PHG, PMG and PSG ($13$). For $T = 11$ it contains $21$ words, adding for example PAG, PQA, PQN and PQS ($12$) and PGG, PLG and PVG ($11$). Averaged over query words drawn from the background frequencies, the neighborhood for $W = 3$, $T = 11$ (the default of BLASTP) contains $19$ words, and that for $T = 13$ contains $6.6$.

:::

BLAST builds a lookup table, or a deterministic finite automaton, from the neighborhood words of every position of the query, and scans each database sequence once, reporting all seed matches in time proportional to the database length plus the number of hits. The neighborhood is computed for the query only, which is why the method is efficient when one query is compared with a large database.

The threshold $T$ sets the trade-off. For two unrelated sequences a given pair of word positions is a hit with probability $2.1\times10^{-3}$ at $T = 11$; for a pair of related sequences with the target frequencies of BLOSUM62 (about $30\,\%$ identity) the probability is $0.119$. A true alignment of $100$ residues thus contains about $98 \times 0.119 \approx 12$ hits on average, but a search of $m = 300$ query positions against $n = 10^{11}$ database positions produces about $mn \times 2.1\times10^{-3} \approx 6\times10^{10}$ chance hits. Raising $T$ to $13$ reduces both rates by about the same factor ($6.3\times10^{-4}$ and $0.064$). Exact word matches are no better: their chance rate ($2.0\times10^{-4}$) is that of $T = 15$, and their sensitivity per word ($0.028$) is lower.

![The neighborhood threshold T of BLASTP for BLOSUM62 and background frequencies of Robinson and Robinson, computed exactly by convolving the score distributions of single positions. A: the mean number of words in the neighborhood of a query word, for word lengths W = 2, 3 and 4 (dashed line: the default T = 11). B: the probability that an aligned pair of 3-residue words is a hit, for unrelated sequences (horizontal) and for related sequences with the target frequencies of BLOSUM62, about 30 % identity (vertical), as T varies. Lowering T increases the sensitivity per word and the number of chance hits in nearly fixed proportion; exact word matches (open circle) have the chance rate of T = 15 but a lower sensitivity](./plots/neighborhood.py)

### 4.3.2. Two Hits and X-Drop Extension

The original BLAST extended every seed match. The 1997 version (Gapped BLAST; Altschul and colleagues) reduced the number of extensions with the *two-hit method*: an extension is started only when two non-overlapping hits lie on the same diagonal within a distance $A$ ($A = 40$ by default). A true alignment usually contains several hits close together, whereas a chance hit is followed by another on its diagonal within $40$ positions only with probability about $40 \times 2.1\times10^{-3} \approx 0.08$. Requiring two hits allows a lower $T$ (higher sensitivity per word) for the same number of extensions, which are the expensive step.

**Definition 4.3.3 (X-Drop Extension)** An *X-drop extension* of a seed extends an alignment from the seed in one direction, keeping the running score and the best score seen so far, and stops as soon as the running score falls more than $X$ below the best; the extended alignment ends at the position of the best score.

**Algorithm 4.3.1 (BLASTP)** Input: a query, a database, BLOSUM62, gap costs $11 + k$, and the thresholds $W = 3$, $T = 11$, $A = 40$.

1. List the neighborhood words of all query words and build the lookup table.
2. Scan the database; for each sequence, record the seed matches on each diagonal.
3. For each pair of non-overlapping hits on one diagonal at distance at most $A$, extend the second hit without gaps in both directions by X-drop ($X$ equivalent to about $7$ bits); the result is a *high-scoring segment pair* (HSP).
4. If the HSP scores above a trigger (about $22$ bits), run a gapped X-drop extension (dynamic programming restricted to the cells whose score stays within about $15$ bits of the best) in both directions from a central position of the HSP.
5. For alignments that reach the reporting threshold, recompute the alignment with traceback (with a larger $X$, about $25$ bits), apply composition-based score adjustment (Section 4.4.5) and compute the E-value.
6. Report the alignments sorted by E-value.

The gapped extension explores only a narrow region that adapts to the alignment, so its cost is roughly proportional to the length of the alignment, not to $mn$. Most of the work is in steps 2 and 3, and most HSPs from chance two-hit pairs die after a few residues.

**Example 4.3.2** In a $120$-residue segment of human MCM6 around the Walker A motif (residues $356$–$475$), compared with the corresponding segment of yeast Mcm6 (residues $535$–$654$), there are $109$ hits with $W = 3$, $T = 11$, of which $79$ lie on the homologous diagonal. They form $7$ two-hit pairs, $6$ on the homologous diagonal and one by chance. The ungapped extension from the first pair on the homologous diagonal climbs steadily to a score of $441$ at the end of the segment; the extension from the chance pair reaches a maximum of $16$ and is abandoned after $13$ further residues, when its running score has fallen more than $X = 16$ below that maximum.

![Seeds and extensions of BLASTP on human MCM6 residues 356–475 (horizontal) against yeast Mcm6 residues 535–654 (vertical), the region containing the Walker A motif GDPSTAKSQ. A: hits of 3-residue words scoring at least T = 11 (dots); pairs of hits on one diagonal within 40 positions (rings) trigger ungapped extensions (shaded lines). B: running score of the ungapped extension to the right from the first two-hit pair on the homologous diagonal (top), which rises to 441 at the end of the segment, and from a chance two-hit pair (bottom), which reaches 16 and stops when the score falls more than X = 16 below this maximum](./plots/seed-and-extend.py)

## 4.4. The Statistics of Local Alignment Scores

### 4.4.1. The Longest Match

How long a similarity do unrelated sequences share by chance? The simplest case is an exact match.

**Theorem 4.4.1 (Erdős–Rényi Law)** In $n$ independent trials with success probability $p$, the length $R_n$ of the longest run of successes satisfies $R_n/\log_{1/p}n \to 1$ almost surely. For two random sequences of lengths $m$ and $n$ in which aligned letters agree with probability $p$, the longest exact match (common substring) has length close to $\log_{1/p}(mn)$; more precisely its mean is approximately $\log_{1/p}[mn(1 - p)] + \gamma/\ln(1/p) - \frac{1}{2}$, with $\gamma = 0.5772$ the Euler constant (Arratia and Waterman 1985).

For two random DNA sequences of $10^4$ bases ($p = \frac{1}{4}$) the formula predicts $13.0$; in $60$ simulated pairs the longest common substring had mean length $12.7$ (standard deviation $0.9$), and for $10^3$ bases $9.7$ against a prediction of $9.7$. A $1$-kb query compared with both strands of a $3.1$-Gb genome shares by chance an exact match of about $\log_4(6.2\times10^{12}) = 21$ bases: a $21$-mer match proves nothing about homology in a genome-wide search, while a $28$-mer, the seed of megablast, is expected by chance $10^{-4}$ times.

The law says that the best chance score grows logarithmically with the search space. The same holds for scored local alignments, and the theory of Karlin and Altschul describes the distribution around this logarithmic mean.

### 4.4.2. The Extreme-Value Distribution

**Definition 4.4.1 (Gumbel Distribution)** A random variable $S$ has a **Gumbel distribution** (type I extreme-value distribution) with location $u$ and scale $1/\lambda$ if

$$
\mathbb{P}(S \le x) = \exp\left(-\mathrm{e}^{-\lambda(x - u)}\right),
$$
with density $\lambda\,\mathrm{e}^{-\lambda(x-u)}\exp(-\mathrm{e}^{-\lambda(x-u)})$, mode $u$, mean $u + \gamma/\lambda$ and variance $\pi^2/(6\lambda^2)$. Its right tail is exponential: $\mathbb{P}(S > x) \approx \mathrm{e}^{-\lambda(x - u)}$ for large $x$.

The maximum of many independent variables with exponential-type tails has, after centering, a Gumbel distribution; the best local alignment score is such a maximum, over the many possible starting points of alignments. **Karlin–Altschul statistics** ([7.6.41](/7.6.41#thm-41.2.1)) make this exact for ungapped alignments: for random sequences of lengths $m$ and $n$, the number of distinct local alignments with score at least $x$ is approximately Poisson with mean $Kmn\,\mathrm{e}^{-\lambda x}$, so the best score $S$ has

$$
\mathbb{P}(S \ge x) \approx 1 - \exp\left(-Kmn\,\mathrm{e}^{-\lambda x}\right), \tag{4.1}
$$
a Gumbel distribution with $u = \ln(Kmn)/\lambda$. The parameter $\lambda$ is the positive root of $\sum q_aq_b\mathrm{e}^{\lambda s(a,b)} = 1$, which for BLOSUM62 with the background of Robinson and Robinson gives $\lambda = 0.3176$ ([7.8.3](/7.8.3#sec-3.3.1)); $K$ (here $0.134$) is given by a more complicated series. For gapped alignments no formula is known, but simulations show that Eq. (4.1) holds with parameters that depend on the gap costs; for BLOSUM62 with gaps $11 + k$ BLAST uses $\lambda = 0.267$, $K = 0.041$, estimated by aligning large numbers of random sequences (Altschul and Gish 1996).

**Example 4.4.1** We aligned $4000$ pairs of random protein sequences of $300$ residues with BLOSUM62. Without gaps, the best local scores had mean $30.4$, and the maximum-likelihood Gumbel fit gave $\lambda = 0.322$ and $K = 0.11$, close to the asymptotic $0.3176$ and $0.134$. With gaps $11 + k$, the mean was $31.9$, and the fit gave $\lambda = 0.283$, $K = 0.051$, against $0.267$ and $0.041$. Repeating the gapped simulation with lengths $100$ to $800$, the mean best score grew from $23.5$ to $39.5$ while $\ln(mn)$ grew from $9.21$ to $13.37$, a slope of $3.83 = 1/0.261$, close to $1/\lambda$. The differences from the asymptotic values are *edge effects*: an alignment that starts near the end of a sequence of $300$ residues cannot grow long, so short sequences behave as if they were shorter.

![Scores of optimal local alignments of unrelated proteins: 4000 pairs of random sequences of 300 residues with background frequencies of Robinson and Robinson, aligned with BLOSUM62 with gaps 11 + k (purple) and without gaps (blue). A: histograms and maximum-likelihood Gumbel fits. B: the empirical probability of a score at least x on a logarithmic scale, linear in the tail with slope −λ (fitted λ = 0.28 and 0.32 against the asymptotic 0.267 and 0.3176). C: the mean gapped score grows linearly with ln(mn) (600 pairs per length), with slope close to 1/λ = 1/0.267 (dashed)](./plots/gumbel-scores.py)

### 4.4.3. Bit Scores and E-Values

A raw score depends on the scale of the substitution matrix and on $K$; it is converted into a quantity that can be compared across scoring systems.

**Definition 4.4.2 (Bit Score)** The **bit score** of an alignment with raw score $S$ under a scoring system with parameters $\lambda$ and $K$ is

$$
S' = \frac{\lambda S - \ln K}{\ln 2}.
$$

**Definition 4.4.3 (E-Value)** The **E-value** of an alignment with bit score $S'$ found in a search of a query of length $m$ against a database of total length $n$ is the expected number of distinct alignments with at least this score between the query and unrelated sequences of the same total length:

$$
E = mn\,2^{-S'} = Kmn\,\mathrm{e}^{-\lambda S}.
$$

**Formula 4.4.1 (P-Value of a Search)** Since the number of chance alignments with score at least $S$ is approximately Poisson with mean $E$, the probability that the search finds at least one is

$$
P = 1 - \mathrm{e}^{-E},
$$
which is close to $E$ when $E < 0.01$.

The E-value is the expected number of false positives at least as good as the hit, for this search; it already accounts for the size of the database, like a **Bonferroni correction** over all database positions, and can exceed $1$. A hit with $E = 10$ is entirely compatible with chance; one with $E = 10^{-10}$ is not. The same raw score is less significant in a larger database: the bit score is independent of the database, and the score needed for a given E-value grows as $\log_2(mn/E)$ bits. This is the expected number of chance hits of [7.4.14](/7.4.14#sec-14.5) in another notation, and answers the question raised in [7.1.4](/7.1.4#sec-4.4.3) of how probable a similarity is by chance.

**Example 4.4.2 (Human MCM6 against Yeast)** The local alignment of human MCM6 ($m = 821$) with yeast Mcm6 has raw score $1711$ ([7.8.3](/7.8.3#sec-3.1.1)), so $S' = (0.267 \times 1711 + 3.19)/0.693 = 663.7$ bits. Against UniProtKB/Swiss-Prot ($n \approx 2.1\times10^8$ residues), $E = 821 \times 2.1\times10^8 \times 2^{-663.7} \approx 10^{-189}$; BLAST prints such values as $0.0$. The archaeal MCM of *Saccharolobus solfataricus* aligns with score $890$, $347$ bits, $E \approx 10^{-93}$, and the human paralog MCM2 with $824$, $322$ bits, $E \approx 10^{-86}$: all three relationships are certain.

**Example 4.4.3 (The Significance Threshold)** For a query of $300$ residues against Swiss-Prot, $E = 0.01$ requires $S' = \log_2(300 \times 2.1\times10^8/0.01) = 42.5$ bits, a raw score of $(42.5 \times 0.693 + \ln 0.041)/0.267 = 98$. For $m = 100$ the threshold is $40.9$ bits, for $m = 821$ it is $44.0$ bits. As a rule, a protein alignment of about $40$ to $50$ bits is significant in a search of a large database; with BLOSUM62, which carries $0.58$ bits per column ([7.8.3](/7.8.3#sec-3.3.4)), this is a well-conserved stretch of $70$ to $90$ residues.

### 4.4.4. Effective Lengths

Equation (4.1) is asymptotic. In a finite sequence an alignment cannot start within its expected length of the end, so the effective lengths of the query and the database are smaller than the true ones.

**Formula 4.4.2 (Effective Lengths)** The expected length of an alignment with score near the threshold is $\ell \approx \ln(Kmn)/H$, where $H$ is the relative entropy of the scoring system in nats per aligned pair. The E-value is computed with the effective lengths

$$
m' = m - \ell, \qquad n' = n - N\ell,
$$
where $N$ is the number of sequences in the database.

**Example 4.4.4** For BLOSUM62 with gaps $11 + k$, $H = 0.14$ nats. For $m = 300$ against Swiss-Prot ($n = 2.07\times10^8$ residues in $N = 5.7\times10^5$ sequences), $\ell = \ln(0.041 \times 300 \times 2.07\times10^8)/0.14 = 155$, so $m' = 145$ and $n' = 1.19\times10^8$. The alignment of raw score $98$ of Example 4.4.3 then has $E = 0.0031$ instead of $0.011$. Current versions of BLAST use a refined finite-size correction (Park and colleagues 2012) with additional parameters estimated by simulation, which changes E-values of short alignments by a similar factor.

### 4.4.5. Composition and Other Corrections

The theory assumes that both sequences have the background composition. Proteins of biased composition (rich in cysteine, proline or charged residues, or the hydrophobic sequences of membrane proteins) produce high scores with each other without being related. BLAST therefore adjusts the scores for each pair of sequences. In *composition-based statistics* (Schäffer and colleagues 2001) $\lambda$ is recomputed for the actual compositions; in *compositional score matrix adjustment* (Yu and Altschul 2005), the default of current versions, the substitution matrix itself is modified so that its implied target frequencies are consistent with the two compositions. The adjusted scores, not the raw BLOSUM62 scores, are those reported. When several HSPs between the same pair of sequences are consistent with one alignment (in BLASTN and BLASTX, for example), *sum statistics* assess them jointly, which gives a smaller E-value than any single HSP.

## 4.5. Low-Complexity Regions and Repeats

Many proteins contain segments of very biased composition: runs of glutamine (polyglutamine tracts, expanded in Huntington's disease), proline-rich linkers, serine–arginine repeats, coiled coils. Such segments align with each other in thousands of unrelated proteins with scores far above what the statistics expect, because the statistics assume that letters are independent.

**Definition 4.5.1 (Low-Complexity Region)** A **low-complexity region** of a sequence is a segment whose composition is strongly biased toward a few letters, quantified by the Shannon entropy $-\sum_a f_a\log_2f_a$ of its letter frequencies $f_a$ in windows of fixed length, or by the compositional complexity $\frac{1}{L}\log_N[L!/\prod_an_a!]$ of a window of length $L$ with letter counts $n_a$ over an alphabet of $N$ letters (Wootton and Federhen 1993).

**Example 4.5.1** In windows of $12$ residues the entropy is $0$ bits for QQQQQQQQQQQQ, $0.65$ bits for QQQQPQQQQPQQ, $2.69$ bits for the signal-peptide-like MKVLAAGIVGLL and $\log_212 = 3.58$ bits, the maximum, for twelve different residues. The program SEG flags windows of $12$ residues whose entropy is below $2.2$ bits, extends them while it stays below $2.5$ bits, and masks the result, by default for BLASTP query sequences in the seeding step only.

:::

Masking replaces the residues by X (or N for DNA) in *hard masking*, or marks them as lowercase letters that are not used to start seeds but are used in extensions (*soft masking*). For DNA, the program DUST masks low-complexity sequence by the over-representation of triplets, and genomes are masked for interspersed repeats (Alu, L1 and other transposable elements, which make up nearly half of the human genome) with RepeatMasker before they are used as search targets, since an *Alu* element in a query would otherwise hit about a million places. Low-complexity hits are the most common source of false positives with small E-values; an alignment dominated by one or two residue types should be examined before it is believed.

## 4.6. The BLAST Family and DNA Seeds

### 4.6.1. Programs

| Program | Query | Database | Comparison |
|---|---|---|---|
| BLASTN (megablast, dc-megablast, blastn) | nucleotide | nucleotide | DNA against DNA; word size $28$, $11$ discontiguous, $11$ |
| BLASTP | protein | protein | protein against protein, $W = 3$, BLOSUM62 |
| BLASTX | nucleotide | protein | query translated in six frames |
| TBLASTN | protein | nucleotide | database translated in six frames |
| TBLASTX | nucleotide | nucleotide | both translated (slow; for distant coding DNA) |
| PSI-BLAST, DELTA-BLAST | protein | protein | iterated profile searches ([7.8.5](/7.8.5)) |

Translated searches compare coding sequences at the protein level, which is more sensitive for divergent genes ([7.8.3](/7.8.3#sec-3.1.2)); BLASTX is the standard tool to find what proteins a read, a contig or a transcript might encode, and TBLASTN to find a protein's gene in an unannotated genome. Megablast, with exact seeds of $28$ bases and scores $+1/{-2}$, is designed for sequences of over $95\,\%$ identity, such as a read against its own species or a primer against a genome.

BLAT (BLAST-Like Alignment Tool; Kent 2002) inverts the strategy of BLAST: it indexes the genome instead of the query, storing the positions of all non-overlapping $11$-mers of the human genome (about $2.8\times10^8$ of them) in memory, and looks up each query word. It is built to align an mRNA or a protein to a genome quickly, joining the HSPs of the exons of one gene into a spliced alignment; it is the search behind the UCSC Genome Browser.

### 4.6.2. Spaced Seeds

The seed of BLASTN must match exactly in $W$ consecutive positions, and in a region of moderate identity such runs are rare. Ma, Tromp and Li (2002) observed that seeds that require matches only at some positions within a longer window, *spaced seeds*, are more sensitive for the same number of chance hits.

**Definition 4.6.1 (Spaced Seed)** A *spaced seed* is a binary pattern such as $111010010100110111$: a hit at position $(i, j)$ requires matches at the positions marked $1$ and allows anything at those marked $0$. Its *weight* is the number of $1$s.

A seed of weight $W$ has the same chance-hit probability, $4^{-W}$ per pair of positions, whether contiguous or spaced. But the hits of a contiguous seed in a homologous region are strongly correlated: when $11$ consecutive positions match, the next window is likely to match too, so hits come in clumps and the probability of at least one hit is lower than for a seed whose overlapping placements share fewer positions.

**Example 4.6.1** In a homologous region of $64$ bases whose positions are identical independently with probability $0.7$, the contiguous seed of weight $11$ hits with probability $0.30$, the spaced seed $111010010100110111$ of PatternHunter with probability $0.47$ (simulation of $4\times10^4$ regions); at $0.8$ identity the probabilities are $0.71$ and $0.88$. The expected number of chance hits for a $1$-kb query against both strands of a $3.1$-Gb genome is $mn4^{-W} = 6.2\times10^{12} \times 4^{-11} = 1.5\times10^6$ for either seed of weight $11$, and $8.6\times10^{-5}$ for the contiguous seed of weight $28$.

![Seeds for DNA search. A: probability that a seed hits a homologous region of 64 bases whose positions are identical independently with probability p (Monte Carlo, 40 000 regions per point), for contiguous seeds of weight 8, 11 and 28 and the spaced seed 111010010100110111 of PatternHunter (weight 11, length 18); at p = 0.7 (dashed) the spaced seed hits with probability 0.47 and the contiguous seed of the same weight with 0.30. B: expected number of chance hits of a seed of weight W for a 1-kb query against both strands of a 3.1-Gb genome, mn·4^−W](./plots/spaced-seeds.py)

:::

Spaced seeds are used in discontiguous megablast, in PatternHunter, in DIAMOND, and, generalized to sets of several seeds and to minimizers, in the read aligners of [7.8.10](/7.8.10).

## 4.7. Fast Search and Clustering at Scale

### 4.7.1. DIAMOND and MMseqs2

Metagenomics ([7.8.14](/7.8.14)) and the annotation of thousands of genomes require comparisons of $10^7$ to $10^9$ sequences with large databases, which even BLAST cannot do. Two programs dominate.

- DIAMOND (Buchfink, Xie and Huson 2015; version 2, 2021) indexes both the queries and the database (*double indexing*), so that the seed matches of all query–target pairs are found by sorting and merging two lists, a cache-friendly operation; it uses spaced seeds over a reduced alphabet of $11$ letters (grouping similar amino acids) to gain sensitivity per seed. In its fast modes it is thousands of times faster than BLASTX on short reads; in its most sensitive modes it approaches the sensitivity of BLASTP at about $80$ times the speed.
- MMseqs2 (Steinegger and Söding 2017) requires two consecutive *similar* $k$-mer matches ($k = 6$ or $7$, with neighborhoods as in BLAST) on the same diagonal, then an ungapped alignment on that diagonal, and finally a vectorized Smith–Waterman alignment only for the survivors. A sensitivity parameter (from $1$ to $7.5$) sets the size of the $k$-mer neighborhoods; at high sensitivity it exceeds BLAST in detecting remote homologs at a fraction of its time, and it can also search with profiles ([7.8.5](/7.8.5)).

Both report BLAST-like E-values and the same tabular output, so they can replace BLAST in pipelines.

### 4.7.2. Sequence Clustering

Databases are highly redundant: thousands of near-identical sequences of the same protein from different strains. Clustering them reduces the search space and the bias of statistics toward over-represented families.

**Definition 4.7.1 (Sequence Clustering)** **Sequence clustering** partitions a set of sequences into groups (clusters) such that every member of a cluster is similar to its representative sequence above a threshold, typically of identity and alignment coverage.

**Algorithm 4.7.1 (Greedy Incremental Clustering)** Used by CD-HIT (Li and Godzik 2006) and UCLUST:

1. Sort the sequences by decreasing length.
2. The first sequence becomes the representative of the first cluster.
3. For each next sequence, compare it with the existing representatives (filtering most comparisons by counting shared short words); if it matches one at or above the threshold (say $90\,\%$ identity over $80\,\%$ of its length), add it to that cluster; otherwise make it the representative of a new cluster.

The method needs at most one comparison per sequence and representative, but the number of representatives grows with the data, so the cost is quadratic in the worst case. Linclust (Steinegger and Söding 2018), part of MMseqs2, clusters in time linear in the number of sequences: it selects for each sequence a few $k$-mers, groups sequences sharing a $k$-mer, and compares each to the longest member of its group only. The UniRef databases cluster UniProtKB at $100$, $90$ and $50\,\%$ identity (UniRef100, UniRef90, UniRef50); UniRef50 has several times fewer sequences than UniProtKB and is the usual target for sensitive searches and for building the multiple alignments used in structure prediction ([7.8.17](/7.8.17)).

### 4.7.3. Beyond Sequence

Below about $20\,\%$ identity sequence searches lose most homologs, while protein structures, which change more slowly, remain similar. With the hundreds of millions of predicted structures of the AlphaFold database, structural search became a third kind of database search. Foldseek (van Kempen and colleagues 2024) encodes each residue's local structural environment as a letter of a $20$-letter *structural alphabet* and then searches with the machinery of this chapter (prefilter on $k$-mers, local alignment, E-values); it is treated with structure comparison in [7.8.17](/7.8.17).

## 4.8. Running and Reading a Search

A local search with BLAST+ against a custom database:

```bash
# Build a protein database from a FASTA file (creates the index files used by blastp)
makeblastdb -in uniprot_sprot.fasta -dbtype prot -out sprot -parse_seqids

# Search: BLOSUM62, gaps 11 + k, E-value cutoff 1e-5, tabular output with standard columns
blastp -query MCM6_HUMAN.fa -db sprot -evalue 1e-5 -num_threads 8 \
       -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore" \
       -out mcm6_vs_sprot.tsv

# Six-frame translated search of contigs against proteins, then the same with DIAMOND
blastx  -query contigs.fa -db sprot -evalue 1e-5 -outfmt 6 -out contigs_blastx.tsv
diamond makedb --in uniprot_sprot.fasta -d sprot
diamond blastx -q contigs.fa -d sprot --sensitive -e 1e-5 -o contigs_diamond.tsv

# Cluster at 90 % identity with MMseqs2 (linclust) or CD-HIT
mmseqs easy-linclust proteins.fa clusters tmp --min-seq-id 0.9 -c 0.8
cd-hit -i proteins.fa -o proteins90.fa -c 0.9 -aS 0.8
```

The tabular format (`-outfmt 6`) has one line per HSP with $12$ standard columns: query and subject identifiers, percent identity, alignment length, mismatches, gap openings, start and end in the query and the subject, E-value and bit score. For the human–yeast MCM6 alignment of [7.8.3](/7.8.3#sec-3.1.1), the corresponding line would read

```text
MCM6_HUMAN  MCM6_YEAST  42.5  906  412  13  17  816  102  1004  1e-189  664
```
(identity over all columns including gaps, as BLAST reports it; BLAST itself would report slightly different numbers because of the composition adjustment and would print the E-value as $0.0$).

```python
# Parsing tabular BLAST output and keeping the best hit per query
import pandas as pd
cols = "qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore".split()
hits = pd.read_csv("mcm6_vs_sprot.tsv", sep="\t", names=cols)
best = hits.sort_values("bitscore", ascending=False).drop_duplicates("qseqid")
print(best.head())
```

Some rules for reading the output:

- Judge hits by E-value and bit score, not by percent identity: $40\,\%$ identity over $30$ residues is often insignificant, $25\,\%$ over $400$ residues highly significant.
- An E-value is valid for the search that produced it. Comparing E-values across searches of different databases requires the bit scores, which do not depend on the database.
- Check the coverage: a hit to one domain of a multidomain protein does not transfer the function of the whole protein. Annotation by the best hit propagates errors from database entries that were themselves annotated by sequence similarity; experimentally characterized entries (Swiss-Prot with evidence codes) are more reliable.
- Look at alignments dominated by low-complexity or compositionally biased segments, and at hits whose E-values are near the threshold, before drawing conclusions.
- Reciprocal best hits (gene $a$ of species 1 has $b$ as its best hit in species 2, and vice versa) are a simple operational criterion for **orthologs**; gene families with lineage-specific duplications need tree-based methods ([7.8.6](/7.8.6)).

## Summary

| Topic | Key points |
|---|---|
| Problem | databases of $10^{11}$ residues; full Smith–Waterman of one query takes hours; heuristics trade sensitivity for speed |
| FASTA | exact $k$-tuple matches, diagonals, banded DP (Algorithm 4.2.1) |
| BLAST seeds | neighborhood words scoring $\ge T$ (Definition 4.3.2); PQG has $9$ neighbors at $T = 13$, $21$ at $T = 11$ (Example 4.3.1); $T$ moves sensitivity and chance hits together |
| BLAST extension | two hits within $A = 40$ on one diagonal; ungapped X-drop (Definition 4.3.3) to an HSP; gapped X-drop above a trigger (Algorithm 4.3.1); chance seeds die quickly (Example 4.3.2) |
| Longest match | Erdős–Rényi law: $\log_{1/p}(mn)$ (Theorem 4.4.1); $21$ bases by chance in a genome search |
| Score distribution | Gumbel (Definition 4.4.1); $\mathbb{P}(S \ge x) \approx 1 - \exp(-Kmn\mathrm{e}^{-\lambda x})$ (Eq. (4.1)); BLOSUM62: $\lambda = 0.3176$ ungapped, $0.267$ gapped; confirmed by simulation (Example 4.4.1) |
| Significance | bit score $S' = (\lambda S - \ln K)/\ln 2$ (Definition 4.4.2); $E = mn2^{-S'}$ (Definition 4.4.3); $P = 1 - \mathrm{e}^{-E}$ (Formula 4.4.1); about $40$–$50$ bits needed in a large database (Example 4.4.3); effective lengths (Formula 4.4.2); composition adjustment |
| Filtering | low-complexity regions (Definition 4.5.1), SEG, DUST, repeat masking; soft versus hard masking |
| Family | BLASTN/P/X, TBLASTN/X, PSI-BLAST; BLAT indexes the genome; spaced seeds (Definition 4.6.1) raise sensitivity at equal chance rate (Example 4.6.1) |
| Scale | DIAMOND (double indexing, reduced alphabet), MMseqs2 (similar $k$-mers, prefilters); clustering by greedy incremental methods and Linclust (Definition 4.7.1, Algorithm 4.7.1); UniRef; structural search with Foldseek |

## Questions

1. With BLOSUM62 ($\mathrm{P}\mathrm{P} = 7$, $\mathrm{Q}\mathrm{Q} = 5$, $\mathrm{Q}\mathrm{E} = 2$, $\mathrm{Q}\mathrm{R} = \mathrm{Q}\mathrm{K} = 1$, $\mathrm{G}\mathrm{G} = 6$), verify the scores of PQG against PEG, PRG and PKG, and explain why lowering $T$ from $13$ to $11$ more than doubles the neighborhood of PQG.

   **Answer** PEG: $7 + 2 + 6 = 15$; PRG and PKG: $7 + 1 + 6 = 14$. A word's neighbors are obtained by replacing one or more letters with substitutions costing little: at $T = 13$ only single substitutions at the middle position costing at most $5$ ($18 - 13$) qualify, giving $9$ words; at $T = 11$ the budget is $7$, which admits substitutions at the last position too (PQA, PQN, PQS with $12$, PQD with $11$) and more at the middle (PAG, PPG, PTG, PYG, PGG, PLG, PWG, PVG), giving $21$; no substitution of the first P qualifies, since every P–X score is at most $-1$, a loss of at least $8$. Since the number of words within a score budget grows roughly exponentially with the budget, the neighborhood size grows exponentially as $T$ decreases (Section 4.3.1: $6.6$ words on average at $T = 13$, $19$ at $T = 11$).

2. Why does BLAST compute the neighborhood words of the query and not of the database, and why does BLAT do the opposite?

   **Answer** BLAST is designed for one (or a few) queries against a large, changing database: the neighborhood of a query of length $m$ has about $19m$ words, a small table built in milliseconds, and the database is scanned once sequentially; indexing the neighborhoods of $10^{11}$ database positions would be impossible. BLAT is designed for many queries (mRNAs, reads, proteins) against one fixed genome: it builds once an index of the genome's non-overlapping $11$-mers, which fits in memory, and each query then needs only a lookup per word, without scanning the $3$-Gb genome. The choice depends on which side is large and fixed.

3. A BLASTP hit has raw score $60$ with BLOSUM62 and gaps $11 + k$ ($\lambda = 0.267$, $K = 0.041$). Compute the bit score and the E-value for a $250$-residue query against a database of $5\times10^{10}$ residues. Is the hit significant? What score is needed for $E = 10^{-3}$?

   **Answer** $S' = (0.267 \times 60 - \ln 0.041)/\ln 2 = (16.02 + 3.19)/0.693 = 27.7$ bits. $E = 250 \times 5\times10^{10} \times 2^{-27.7} = 1.25\times10^{13} \times 4.6\times10^{-9} \approx 5.8\times10^4$: tens of thousands of chance alignments this good are expected, so the hit means nothing. For $E = 10^{-3}$: $S' = \log_2(1.25\times10^{13}/10^{-3}) = 53.5$ bits, raw score $(53.5 \times 0.693 + \ln 0.041)/0.267 = (37.1 - 3.19)/0.267 = 127$.

4. Why can an E-value be larger than $1$ while a P-value cannot? Compute $P$ for $E = 0.01$, $1$ and $5$, and say which quantity you would use to decide which hits to accept.

   **Answer** The E-value is an expected count of chance alignments, which can be any non-negative number; the P-value is the probability of at least one, $P = 1 - \mathrm{e}^{-E}$: $0.00995$ for $E = 0.01$, $0.632$ for $E = 1$, $0.993$ for $E = 5$. For small values they are equal, and BLAST reports $E$ because it is more informative for weak hits (it distinguishes $E = 5$ from $E = 50$, while $P \approx 1$ for both) and because it can be read as the expected number of false positives among the hits at least as good, which is what one wants to control when accepting a list of hits.

5. In Example 4.4.1 the fitted gapped $\lambda$ was $0.283$ for sequences of $300$ residues, while BLAST uses $0.267$. Explain the difference, and say how it affects E-values of short sequences if uncorrected.

   **Answer** Equation (4.1) is the limit for long sequences. In short sequences an alignment cannot start near the end and still grow to the length of a typical high-scoring alignment, so fewer high scores occur than the asymptotic formula predicts; the tail falls off faster (apparently larger $\lambda$) and the location is lower (apparently smaller $Kmn$). If the asymptotic parameters were used with the true lengths, E-values for short sequences would be too large, that is, conservative. BLAST corrects this by effective lengths (Formula 4.4.2) or by a finite-size correction with additional parameters estimated from the same kind of simulation.

6. Show that the Erdős–Rényi law predicts that the longest exact match between a random $150$-nt read and a random $3.1$-Gb genome (both strands) is about $19$ bases. What does this imply for the minimum length of an exact seed in read mapping?

   **Answer** $\log_4(150 \times 6.2\times10^9) = \log_4(9.3\times10^{11}) = \ln(9.3\times10^{11})/\ln 4 = 27.6/1.386 = 19.9$; the refined formula gives $\log_4(0.75 \times 9.3\times10^{11}) + 0.42 - 0.5 \approx 19.6$. A read therefore shares an exact match of about $19$–$20$ bases with random places of the genome; seeds shorter than about $20$ bases have many chance occurrences in a human genome and are useful only when combined (several seeds, chaining) or verified by alignment. Read mappers use seeds of $19$–$32$ bases (BWA-MEM's default minimum seed is $19$), close to this bound ([7.8.10](/7.8.10)).

7. Compute the Shannon entropy of the windows QQQQQQQQQQQQ, QQQQPQQQQPQQ and MKVLAAGIVGLL, and decide which would be masked by SEG with the thresholds $2.2$ and $2.5$ bits. Why are such segments a problem for the statistics of BLAST?

   **Answer** The first has entropy $0$, the second $-\frac{5}{6}\log_2\frac{5}{6} - \frac{1}{6}\log_2\frac{1}{6} = 0.219 + 0.431 = 0.65$ bits, the third (counts L $3$; V, A, G $2$ each; M, K, I $1$ each) $\frac{1}{4}\log_24 + 3\cdot\frac{1}{6}\log_26 + 3\cdot\frac{1}{12}\log_212 = 0.5 + 1.29 + 0.90 = 2.69$ bits. The first two are below $2.2$ and masked; the third is not. Karlin–Altschul statistics assume that letters are independent and have the background frequencies; a polyglutamine tract aligned to another polyglutamine tract scores $5$ per column for every column, a score the theory considers astronomically improbable, but such tracts occur in many unrelated proteins. Their alignments receive tiny E-values that do not reflect homology.

8. Explain why a spaced seed of weight $11$ is more sensitive than a contiguous seed of weight $11$ although both have the same probability of a chance hit at a given position pair.

   **Answer** The chance rate depends only on the weight: $4^{-11}$ per position pair for either seed. Sensitivity is the probability of at least one hit in a homologous region, which depends on how the hits at overlapping placements are correlated. For a contiguous seed two placements shifted by one share $10$ of their $11$ positions, so hits come in runs: the expected number of hits in a region is the same as for the spaced seed, but they are concentrated in fewer regions, and more regions have none. The spaced pattern was chosen so that its shifted copies overlap in few positions, making its hits closer to independent and the probability of at least one hit larger ($0.47$ against $0.30$ at $70\,\%$ identity over $64$ bases, Example 4.6.1).

9. A BLASTX search of an unknown $1.2$-kb contig from a soil metagenome gives its best hit, $E = 10^{-30}$ over residues $50$–$250$ of a $600$-residue protein annotated as "putative transporter" in an unreviewed database entry. What can you conclude, and what would you check?

   **Answer** The contig very probably encodes a protein homologous to the hit over about $200$ residues (one or two domains), but not necessarily to the whole protein, and the annotation of the target is itself likely inferred by similarity, possibly from a chain of such inferences. Check: the coverage of the contig and of the target, the frame and whether the coding region is intact (no stop codons, consistent strand); the domains of both (InterPro or Pfam, [7.8.5](/7.8.5)); the best hits among reviewed (Swiss-Prot) entries with experimental evidence; whether the alignment is dominated by low-complexity or transmembrane segments, which in transporters can give spurious similarity; and, for an ecological interpretation, the taxonomy of the top hits. The safe conclusion is "homologous to transporters of family X", with the specific substrate unknown.

10. (Design) You must annotate $5\times10^7$ predicted proteins from a metagenome against UniRef90 (about $1.5\times10^8$ sequences) within a day on a $64$-core server. Estimate whether BLASTP is feasible, and design a strategy.

    **Answer** BLASTP of a $300$-residue protein against a database of $\sim5\times10^{10}$ residues takes on the order of a minute on one core, so $5\times10^7$ queries need about $5\times10^7$ core-minutes, $95$ core-years, or about a year and a half on $64$ cores: infeasible. Strategy: (1) cluster the queries at $90$–$95\,\%$ identity with Linclust ([Section 4.7.2](/7.8.4#sec-4.7.2)), which for metagenomes often reduces the number by a factor of several; (2) search the representatives with DIAMOND in a sensitive mode or MMseqs2, which are $100$ to $10^4$ times faster than BLASTP; (3) transfer annotations within clusters; (4) for proteins without significant hits, run a more sensitive profile search against Pfam with HMMER or HH-suite ([7.8.5](/7.8.5)), or structure-based search. With a speedup of $10^3$ and a reduction of the queries by a factor of $3$, the search takes about $95/(3 \times 1000)$ core-years $\approx 12$ core-days, about $4.5$ hours on $64$ cores.
