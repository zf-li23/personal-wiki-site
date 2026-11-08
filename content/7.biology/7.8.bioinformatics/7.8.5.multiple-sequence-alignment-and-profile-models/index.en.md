---
title: Multiple Sequence Alignment and Profile Models
description: "Multiple sequence alignment: the sum-of-pairs objective, the cost of exact dynamic programming and NP-hardness; the center-star 2-approximation; progressive alignment along a guide tree and its refinements (iteration, consistency, MAFFT, Clustal Omega, FAMSA) and their evaluation. Profiles: position-specific scoring matrices with sequence weights and pseudocounts, PSI-BLAST and profile drift. Probabilistic models: pair HMMs and posterior alignment, profile HMMs (match, insert and delete states, parameter estimation, Viterbi and forward scoring), HMMER and Pfam, HMM–HMM comparison with HHpred and HHblits, and a simulation of why profiles detect remote homologs. Column conservation by entropy and Jensen–Shannon divergence; practice with MAFFT, HMMER and jackhmmer. Running example: the MCM2–7 helicase family."
---

A pairwise alignment compares two sequences; a family of homologous sequences is understood only by comparing all of them at once. A multiple sequence alignment (MSA) arranges many homologous sequences in columns, and what it shows cannot be seen in any pair: which positions never change (the residues of an active site), which change only among similar residues, where insertions are tolerated, and which positions change together. MSAs are the input of most of the rest of the course: phylogenetic trees are inferred from them ([7.8.6](/7.8.6)), conservation scores identify functional sites and regulatory elements ([7.8.8](/7.8.8)), and the coevolution of columns in deep alignments is the signal from which protein contacts and structures are predicted ([7.6.15](/7.6.15#sec-15.5.4), [7.8.17](/7.8.17)). The chapter has two parts. The first treats the construction of MSAs: the objective, why it cannot be optimized exactly, and the progressive methods that are used instead. The second treats *profiles*, models of a family estimated from its MSA, from position-specific scoring matrices to profile **hidden Markov models**, which turn the alignment of a sequence to a family into a probabilistic inference and detect homologs far beyond the reach of pairwise comparison ([7.8.4](/7.8.4)). The theory of hidden Markov models, with the **forward algorithm** and the **Viterbi algorithm**, was given in [4.6.8](/4.6.8); the **consensus sequence** and the sequence logo were introduced in [7.1.4](/7.1.4#sec-4.4.2). The example is again the MCM family: the six paralogous subunits MCM2–7 of the eukaryotic replicative helicase and their orthologs, AAA+ ATPases whose Walker A motif binds ATP.

## 5.1. The Multiple Alignment Problem

**Definition 5.1.1 (Multiple Sequence Alignment)** A **multiple sequence alignment** of $k$ sequences $x^{(1)}, \dots, x^{(k)}$ is a matrix of $k$ rows and $L$ columns over $\mathcal{A} \cup \{-\}$ such that row $r$ with the gap symbols deleted is $x^{(r)}$ and no column consists of gaps only. Each MSA induces a pairwise alignment of every two rows, obtained by deleting the columns in which both have gaps.

To find the best MSA we need an objective. The most common one adds up the pairwise scores.

**Definition 5.1.2 (Sum-of-Pairs Score)** The **sum-of-pairs score** (SP score) of an MSA is the sum over all pairs of rows $r < t$ of the score of the pairwise alignment they induce,

$$
\operatorname{SP} = \sum_{r < t}S\left(x^{(r)}, x^{(t)}\right),
$$
with a substitution matrix and gap penalties as in [7.8.3](/7.8.3); in a *weighted* SP score each pair is multiplied by a weight $w_rw_t$ that down-weights redundant sequences.

The SP score is a convenient but imperfect model. A column in which all $k$ sequences have a leucine except one isoleucine scores $\binom{k-1}{2}s(\mathrm{L},\mathrm{L}) + (k-1)s(\mathrm{L},\mathrm{I})$, counting the same evolutionary event, one substitution on one branch, $k - 1$ times; the evolutionary model behind an MSA is a tree, not a set of independent pairs. Tree-based objectives (the cost of the alignment on a phylogeny) are more faithful but harder still.

**Theorem 5.1.1** The SP-optimal alignment of $k$ sequences of length $n$ can be computed by dynamic programming in a $k$-dimensional lattice in $O(2^kk^2n^k)$ time; the problem of finding it is NP-hard when $k$ is part of the input (Wang and Jiang 1994).

The recursion generalizes Needleman–Wunsch ([7.8.3](/7.8.3#sec-3.5.2)): a cell $(i_1, \dots, i_k)$ has $2^k - 1$ predecessors, one for each nonempty subset of rows that advance by one residue (the others receive gaps), and the score of each move is a sum over $\binom{k}{2}$ pairs. For three sequences of $300$ residues the lattice has $2.7\times10^7$ cells and $2^3 \cdot 300^3 = 2.2\times10^8$ moves, feasible; for ten sequences, $2^{10} \cdot 300^{10} = 6\times10^{27}$ moves, impossible. Bounds that prune the lattice (the program MSA of Lipman, Altschul and Kececioglu, 1989) extend exact alignment to about ten short sequences. Practical methods are therefore heuristics, and the quality of an MSA is judged by comparison with reference alignments rather than by its score (Section 5.3.4).

## 5.2. Center-Star Alignment

The simplest heuristic with a guarantee chooses one sequence as the center and aligns every other sequence to it.

**Algorithm 5.2.1 (Center-Star Alignment)** For sequences $x^{(1)}, \dots, x^{(k)}$ and a distance $d$ (an optimal pairwise alignment cost, such as the edit distance of [7.8.3](/7.8.3#sec-3.5.1)):

1. Compute $d(x^{(r)}, x^{(t)})$ for all pairs.
2. Choose the center $c$ minimizing $\sum_td(x^{(c)}, x^{(t)})$.
3. Align each $x^{(t)}$ optimally to $x^{(c)}$, and merge these $k - 1$ pairwise alignments into one MSA, inserting into all rows the gaps that any of them introduces into the center ("once a gap, always a gap").

**Theorem 5.2.1** If the cost of an alignment column pair satisfies the triangle inequality and gaps against gaps cost $0$, the SP cost of the center-star alignment is at most $2 - 2/k$ times the minimum SP cost.

**Proof** Let $D(r, t)$ be the cost of the pairwise alignment of rows $r$ and $t$ induced by the star alignment. Rows aligned to the center keep their optimal alignment with it, $D(c, t) = d(c, t)$, and by the triangle inequality, column by column, $D(r, t) \le D(r, c) + D(c, t) = d(r, c) + d(c, t)$. Summing over ordered pairs $r \ne t$,

$$
2\operatorname{SP}_{\mathrm{star}} = \sum_{r \ne t}D(r, t) \le \sum_{r \ne t}[d(r, c) + d(c, t)] = 2(k - 1)\sum_td(c, t).
$$
For the optimal MSA, every induced pairwise alignment costs at least the optimal pairwise cost, so $2\operatorname{SP}_{\mathrm{opt}} \ge \sum_r\sum_td(r, t) \ge k\sum_td(c, t)$ by the choice of $c$. Hence $\operatorname{SP}_{\mathrm{star}}/\operatorname{SP}_{\mathrm{opt}} \le (k - 1)/(k/2) = 2 - 2/k$. $\square$

**Example 5.2.1** For the five DNA sequences ATTGCCATT, ATGGCCATT, ATCCAATTTT, ATCTTCTT and ACTGACC (a textbook example of Gusfield), the edit distances from the first sequence to the others are $1, 5, 4, 5$, total $15$, the smallest row sum (the others are $15$, $21$, $17$ and $22$), so it is the center. The star alignment has SP cost at most $(k - 1) \times 15 = 60$, while any alignment costs at least half the sum of all pairwise distances, $45$; the star alignment is therefore within a factor $60/45 = 1.33$ of the optimum, better than the worst-case bound $1.6$.

The guarantee is weak in practice, because the center may be far from distant members, but the merge step is the one used by all progressive methods.

## 5.3. Progressive Alignment

### 5.3.1. Profiles and the Guide Tree

Progressive alignment (Feng and Doolittle 1987; Higgins and Sharp 1988) builds the MSA by repeated pairwise alignment of groups, joining first the most similar sequences, whose alignment is reliable, and adding more distant ones later.

**Definition 5.3.1 (Profile)** A **profile** of an aligned group of sequences is the description of its columns: for each column $j$, the frequencies $f_j(a)$ of the residues and of gaps. Two profiles, or a profile and a sequence, are aligned by dynamic programming with a column-to-column score, for example the average pair score $\sum_{a,b}f_j(a)f'_l(b)s(a, b)$.

**Definition 5.3.2 (Guide Tree)** A **guide tree** is a rooted binary tree on the sequences, computed from their pairwise distances by a clustering method (UPGMA, neighbor joining, single linkage), which fixes the order in which progressive alignment merges groups.

**Algorithm 5.3.1 (Progressive Alignment)**

1. Compute the pairwise distances (from pairwise alignments, or quickly from shared $k$-mers).
2. Build the guide tree from the distances.
3. Visit the internal nodes from the leaves to the root; at each node, align the profiles of its two child groups by dynamic programming and keep the result as the profile of the node, without changing the alignments within the groups.
4. The profile at the root is the MSA.

The time is dominated by $k - 1$ profile alignments of length about $n$, $O(kn^2)$ beyond the distance computation. ClustalW (Thompson, Higgins and Gibson 1994), the standard program for two decades, added sequence weights from the tree, position-specific gap penalties (lower in hydrophilic stretches, likely loops) and a switch of substitution matrix according to the divergence of the groups.

![Progressive alignment of the MCM family: 15 sequences (human MCM2–7, MCM6 of eight further eukaryotes, the single MCM of the archaeon *Saccharolobus solfataricus*) aligned with FAMSA. Left: the UPGMA guide tree of the distances 1 − identity from the alignment, which sets the order of merging. Right: 40 columns around the Walker A motif GDPxxxKS (boxed), with residues colored where they agree with the consensus of their column in at least half of the sequences; the MCM6 proteins have S in GDP(S/G) where the other paralogs have G. The guide tree groups sequences by similarity only and is not a reliable phylogeny: the archaeal protein, which is an outgroup to all eukaryotic paralogs, is placed next to MCM5](./plots/guide-tree.py)

### 5.3.2. Weaknesses and Remedies

Progressive alignment is greedy: an error made early, when two groups are aligned, is frozen into all later steps ("once a gap, always a gap"). Errors arise when the guide tree is wrong, when distant groups are joined with little information, and when the scoring of a pair of groups is misled by a few unusual sequences. Each successful program attacks this differently.

- *Iterative refinement* (MUSCLE, Edgar 2004): after a progressive alignment, repeatedly cut an edge of the guide tree, realign the two resulting groups as profiles, and keep the change if the SP score improves. MUSCLE also computes the initial distances from $k$-mer counts, without alignments, to scale to large sets.
- *Consistency* (T-Coffee, Notredame, Higgins and Heringa 2000): first build a library of pairwise alignments of all pairs, then re-weight each residue pair $(x_i, y_j)$ by the support of intermediate sequences, $W'(x_i, y_j) = W(x_i, y_j) + \sum_z\sum_l\min[W(x_i, z_l), W(z_l, y_j)]$; progressive alignment with these weights prefers alignments on which the other sequences agree. Consistency is the most effective single idea for accuracy, at a cost cubic in the number of sequences.
- *Fast homology detection* (MAFFT, Katoh and colleagues 2002): convert sequences to numerical signals of residue volume and polarity and find homologous segments by the **fast Fourier transform** of their correlation; the variants range from FFT-NS-2 (two rounds of progressive alignment, fast) to L-INS-i (iterative refinement with consistency from local pairwise alignments, accurate for up to a few hundred sequences).
- *Profile HMMs* (Clustal Omega, Sievers and colleagues 2011): compute guide trees for hundreds of thousands of sequences by embedding them in a low-dimensional space (mBed), and align groups as profile HMMs (Section 5.5) with HHalign.
- *Scale* (FAMSA, Deorowicz and colleagues 2016; MAFFT PartTree): distances from the length of the **longest common subsequence**, single-linkage guide trees and bit-parallel computation align millions of sequences in hours.

### 5.3.3. Aligning Coding Sequences and Large Sets

Coding DNA should be aligned as protein and then back-translated codon by codon (tools such as PAL2NAL, or `tranalign` of EMBOSS); otherwise gaps that break codons appear and synonymous differences obscure homology ([7.8.3](/7.8.3#sec-3.1.2)). For tens of thousands of sequences one builds an MSA of a representative subset (after sequence clustering, [7.8.4](/7.8.4#sec-4.7.2)) and adds the others to it (`mafft --add`, `hmmalign` against a profile of the subset). The alignments of $10^5$ to $10^6$ SARS-CoV-2 genomes used for phylogenetics are built differently: each genome is aligned pairwise to the reference, which is enough when all sequences are $99.9\,\%$ identical.

### 5.3.4. Evaluating Alignments

Since the optimum of the objective is not computable and the objective is only a proxy, programs are compared on reference alignments, often derived from superpositions of known structures, in benchmarks such as BAliBASE (Thompson and colleagues 1999), PREFAB and HomFam.

**Definition 5.3.3 (SP and TC Accuracy)** Relative to a reference alignment, the *SP accuracy* (sum-of-pairs, or developer's score) of a test alignment is the fraction of residue pairs aligned in the reference columns that are also aligned in the test alignment, and the *TC accuracy* (total column score) is the fraction of reference columns that appear identically in the test alignment.

**Example 5.3.1** Let the reference align three sequences as `AC-GT`, `ACAGT`, `A-AGT` and the test as `ACG-T`, `ACAGT`, `A-AGT`. The reference has $11$ aligned residue pairs ($3$ in the first column, $1$ in the second, $1$ in the third, $3$ in the fourth, $3$ in the fifth); the test differs only in row $1$, where G is now aligned with the A of rows $2$ and $3$ instead of with their G. The reference pairs lost are (G of row $1$, G of row $2$) and (G of row $1$, G of row $3$), so the SP accuracy is $9/11 = 0.82$; the reference columns $1$, $2$ and $5$ are reproduced and columns $3$ and $4$ are not, so the TC accuracy is $3/5 = 0.6$.

On BAliBASE, the accuracy of all methods falls steeply below about $25\,\%$ identity, and the differences between methods are largest there. For alignments used in phylogenetics, columns that are unreliable (with many gaps or low agreement) are often removed before tree inference, with programs such as trimAl ([7.8.6](/7.8.6)).

## 5.4. Position-Specific Scoring Matrices

### 5.4.1. From an MSA to a PSSM

A single substitution matrix treats every position of a protein alike; an MSA of the family shows that position $j$ tolerates only small hydrophobic residues while position $j'$ accepts anything. A **position weight matrix**, introduced for DNA binding sites in [7.6.17](/7.6.17#sec-17.7.3), captures this for proteins as well.

**Definition 5.4.1 (Position-Specific Scoring Matrix)** A **position-specific scoring matrix** (PSSM) of a family aligned in $L$ columns is the $L \times 20$ matrix of log-odds scores

$$
s_j(a) = \log_2\frac{p_j(a)}{q_a},
$$
where $p_j(a)$ is the estimated probability of residue $a$ at column $j$ and $q_a$ its background frequency. The score of a sequence $y_1 \cdots y_L$ aligned without gaps to the columns is $\sum_js_j(y_j)$, the log-likelihood ratio of the family model against the background.

Two problems arise in estimating $p_j(a)$ from a few sequences. Families are sampled unevenly (many mammalian sequences, few from protists), so close relatives must be down-weighted; and a residue not seen in a column of ten sequences is not impossible there, so the estimate needs pseudocounts.

**Formula 5.4.1 (Position-Based Sequence Weights)** In the method of Henikoff and Henikoff (1994), sequence $r$ receives the weight

$$
w_r = \sum_j\frac{1}{c_j\,n_j(x^{(r)}_j)},
$$
where $c_j$ is the number of distinct residues in column $j$ and $n_j(a)$ the number of sequences with residue $a$ there; the weights are then normalized to sum to $1$.

**Example 5.4.1** For the four aligned sequences GYVGS, GFDGF, GYDGF and GYQGG: column $1$ (all G) gives each sequence $1/4$; column $2$ (Y, F, Y, Y) gives the F sequence $1/2$ and each Y sequence $1/6$; column $3$ (V, D, D, Q) gives $1/3$ to V and Q and $1/6$ to each D; column $4$ gives $1/4$ each; column $5$ (S, F, F, G) gives $1/3$ to S and G and $1/6$ to each F. The totals are $4/3$, $4/3$, $1$ and $4/3$, normalized $0.267$, $0.267$, $0.200$ and $0.267$: GYDGF, which agrees with another sequence at every variable column, counts least.

**Formula 5.4.2 (Pseudocounts from a Substitution Matrix)** With weighted counts $n_j(a)$ summing to $N_j$ (the effective number of sequences), the estimate

$$
p_j(a) = \frac{n_j(a) + B\,g_j(a)}{N_j + B}, \qquad g_j(a) = \sum_b\frac{n_j(b)}{N_j}\,\mathbb{P}(a \mid b),
$$
adds $B$ pseudocounts distributed like the residues that would arise from those observed by substitution, with $\mathbb{P}(a \mid b) = p_{ab}/q_b$ the conditional target frequencies of a matrix such as BLOSUM62. Few sequences (small $N_j$) leave the estimate close to the substitution-matrix prediction; many sequences let the data dominate.

The pseudocount is a **Laplace smoothing** informed by biology. Its Bayesian form is a prior: mixtures of **Dirichlet distributions** (Sjölander and colleagues 1996), each component representing a kind of column (hydrophobic, aromatic, small, charged), are fitted to large sets of alignments and give posterior mean estimates that are the best available for small families; HMMER uses them.

### 5.4.2. PSI-BLAST

**Definition 5.4.2 (PSI-BLAST)** **PSI-BLAST** (Position-Specific Iterated BLAST; Altschul and colleagues 1997) searches a database iteratively: a BLASTP search with the query gives an MSA of the significant hits, from which a PSSM is computed; the PSSM, in place of the query and BLOSUM62, is used in the next search, and so on until no new sequences are found.

**Algorithm 5.4.1 (PSI-BLAST)**

1. Search with the query and BLOSUM62; collect the hits with E-value below the inclusion threshold ($0.002$ by default in current versions).
2. Build an MSA of the hits on the query (master–slave: columns are the query positions, insertions in hits are ignored), weight the sequences, add pseudocounts and compute the PSSM, rescaled so that its $\lambda$ matches that of the BLAST statistics.
3. Search the database with the PSSM; the E-values of [7.8.4](/7.8.4#sec-4.4.3) apply unchanged.
4. Repeat steps 2 and 3 until convergence or a fixed number of iterations (usually $3$ to $5$).

Each iteration adds homologs that are similar to the family, if not to the query, and their inclusion widens the profile. The danger is *profile drift*: a single false positive admitted into the profile (an unrelated protein with a shared low-complexity or coiled-coil segment, or a multidomain protein that shares a different domain) attracts its own relatives, and after a few iterations the profile describes another family. Masking low-complexity regions ([7.8.4](/7.8.4#sec-4.5)), a strict inclusion threshold, and inspection of the newly added sequences at each iteration limit it.

**Definition 5.4.3 (Remote Homology)** **Remote homology** is homology between proteins whose sequences have diverged so far (typically below about $25\,\%$ identity, the twilight zone of [7.8.3](/7.8.3#sec-3.1.2)) that pairwise comparison fails to detect it significantly, although structure and often function are conserved.

## 5.5. Hidden Markov Models of Alignments

### 5.5.1. Pair HMMs

The scores of [7.8.3](/7.8.3) can be read as probabilities. A *pair HMM* has three emitting states: $M$ emits an aligned pair $(a, b)$ with probability $p_{ab}$, $X$ emits a residue $a$ of $x$ against a gap with probability $q_a$, and $Y$ emits a residue of $y$. From $M$ a gap is opened with probability $\delta$ (to $X$ or to $Y$), and a gap state is left with probability $1 - \varepsilon$. A path through the model is an alignment, and its probability divided by that of the two sequences under the background is

$$
\prod_{\text{pairs}}\frac{p_{ab}}{q_aq_b} \times \prod_{\text{gaps}}\delta\varepsilon^{\,k-1} \times (\text{terms from } 1 - 2\delta \text{ and } 1 - \varepsilon),
$$
whose logarithm is the score of the alignment with substitution scores $\log[p_{ab}/(q_aq_b)]$ and an affine gap penalty with $d \approx -\log\delta$, $e \approx -\log\varepsilon$ (Durbin and colleagues 1998). The **Viterbi algorithm** on the pair HMM is therefore Gotoh's algorithm ([7.8.3](/7.8.3#sec-3.5.4)), with the three matrices as the three states.

What the probabilistic view adds is the sum over alignments. The **forward algorithm** computes $\mathbb{P}(x, y)$ summed over all alignments, a measure of relatedness that does not depend on a single alignment, and the forward and backward algorithms together give the *posterior probability* that $x_i$ is aligned to $y_j$, $\mathbb{P}(x_i \diamond y_j \mid x, y)$. These posteriors measure the reliability of each column ([7.8.3](/7.8.3#sec-3.5.6)); maximum-expected-accuracy alignment, which maximizes their sum, and consistency built from them are the basis of the accurate aligners ProbCons and MAFFT L-INS-i.

### 5.5.2. Profile HMMs

**Definition 5.5.1 (Profile Hidden Markov Model)** A **profile hidden Markov model** of a family with $K$ consensus columns (Krogh and colleagues 1994) is a hidden Markov model with, for each column $k = 1, \dots, K$, a *match* state $M_k$ that emits residues with column-specific probabilities $e_{M_k}(a)$, an *insert* state $I_k$ that emits residues with background-like probabilities and can repeat, modeling residues inserted after column $k$, and a silent *delete* state $D_k$ that skips column $k$. The transitions run from left to right: $M_k \to M_{k+1}, I_k, D_{k+1}$; $I_k \to I_k, M_{k+1}$; $D_k \to D_{k+1}, M_{k+1}$ (in the Plan7 architecture of HMMER).

A profile HMM is a PSSM (the match emissions) with position-specific, probabilistic gap penalties (the transitions): a column where many family members have deletions has a high probability $M_{k-1} \to D_k$, so deleting it costs little, while deletions in a conserved core are expensive. The model is estimated from an MSA:

1. Columns in which at least half of the (weighted) sequences have a residue become match columns; the others are insertions.
2. Each sequence of the MSA defines a path through the model; the weighted counts of emissions and transitions along the paths, plus Dirichlet-mixture pseudocounts, give the probabilities.
3. The effective number of sequences is reduced (HMMER's entropy weighting) so that the model is not more confident than the diversity of the family justifies.

![The architecture of a profile hidden Markov model with four match columns, in the Plan7 form of HMMER. Match states M1–M4 (squares) emit residues with the probabilities of their alignment columns; insert states I0–I3 (diamonds) emit residues with background-like probabilities and can repeat (self-loops); delete states D1–D4 (circles) are silent and skip a column. Arrows are the allowed transitions (no direct transitions between insert and delete states). The red path aligns a sequence with two inserted residues after column 2 and without column 4: Begin → M1 → M2 → I2 → I2 → M3 → D4 → End](./plots/profile-hmm.py)

**Algorithm 5.5.1 (Viterbi Alignment of a Sequence to a Profile HMM)** For a sequence $y_1 \cdots y_n$ and a model with background frequencies $q$, transition probabilities $a$ and emission probabilities $e$, let $V^M_k(i)$, $V^I_k(i)$ and $V^D_k(i)$ be the best log-odds scores of a path that has generated $y_1 \cdots y_i$ and ends in $M_k$, $I_k$ or $D_k$. Then

$$
\begin{aligned}
V^M_k(i) &= \log\frac{e_{M_k}(y_i)}{q_{y_i}} + \max\{V^M_{k-1}(i-1) + \log a_{M_{k-1}M_k},\ V^I_{k-1}(i-1) + \log a_{I_{k-1}M_k},\ V^D_{k-1}(i-1) + \log a_{D_{k-1}M_k}\},\\
V^I_k(i) &= \log\frac{e_{I_k}(y_i)}{q_{y_i}} + \max\{V^M_k(i-1) + \log a_{M_kI_k},\ V^I_k(i-1) + \log a_{I_kI_k}\},\\
V^D_k(i) &= \max\{V^M_{k-1}(i) + \log a_{M_{k-1}D_k},\ V^D_{k-1}(i) + \log a_{D_{k-1}D_k}\},
\end{aligned}
$$
with the begin state as $V^M_0(0) = 0$. The best path, found by traceback, aligns $y$ to the model, in $O(Kn)$ time. Replacing every $\max$ by a sum of probabilities (a log-sum-exp) gives the forward score, the log-odds of $y$ under the model summed over all alignments.

For database search the model is made *local*: paths may enter at any match state and leave from any match state, as in Smith–Waterman, and flanking states emit unaligned residues of the target. Aligning many sequences to the model (`hmmalign`) produces an MSA in which every sequence is aligned to the family, not to the other sequences, in linear time per sequence.

### 5.5.3. HMMER and Pfam

HMMER3 (Eddy 2011) made profile HMM search as fast as BLAST. Each target passes a pipeline of filters: an ungapped *multiple segment Viterbi* (MSV) score computed with striped SIMD instructions, which removes about $98\,\%$ of targets; a gapped Viterbi filter; and finally the full forward score with domain identification. The scores are bit scores, log-odds against a background model, and E-values come from their null distributions: Viterbi and MSV scores of random sequences follow a Gumbel distribution with $\lambda \approx \ln 2$ per bit, and forward scores an exponential tail with the same $\lambda$ (Eddy 2008), so only the location must be calibrated per model.

Pfam (now part of InterPro) is a database of about $20\,000$ protein families, each represented by a curated *seed* alignment of representative members, a profile HMM built from it, and a *full* alignment of all UniProtKB sequences that score above a manually set gathering threshold. InterPro integrates Pfam with other signature databases (PROSITE patterns, SMART, PANTHER, CATH-Gene3D) and annotates every UniProtKB protein with its domains. Searching a new protein against Pfam (`hmmscan`, or InterProScan) is the standard way to find its domains.

**Example 5.5.1 (Profile versus Pairwise)** We built a profile HMM (HMMER's default parameters, $822$ match states) from a FAMSA alignment of nine MCM6 orthologs, from human to yeast, and scored the human paralogs, the archaeal MCM and $2000$ shuffled paralog sequences. The paralogs scored $441$ to $500$ bits (MCM7 $499.8$, MCM4 $494.3$, MCM2 $464.5$, MCM3 $444.0$, MCM5 $441.3$) and the archaeal MCM $514.5$ bits, with E-values below $10^{-130}$; no shuffled sequence reached the reporting threshold. The local pairwise alignments of human MCM6 alone with the same targets give $291$ to $347$ bits ([7.8.4](/7.8.4#sec-4.4.3)): the profile adds $40$ to $50\,\%$ to the score of the same homologs, because it knows which positions are conserved throughout the family and which vary. For homologs as close as these both methods succeed; the gain decides the outcome for remote homologs near the threshold.

### 5.5.4. Comparing Profiles

If profiles of the query family are better than the query alone, profiles of the target families should help too. HHsearch and HHpred (Söding 2005) align two profile HMMs by dynamic programming, scoring a pair of match states by the log of $\sum_ap_k(a)p'_l(a)/q_a$, the probability that the two columns emit the same residue relative to chance, and transitions by the combined probabilities of both models. HHblits (Remmert and colleagues 2012) makes this fast enough to iterate over databases of profiles of all UniProtKB clusters (UniRef30): it first discretizes each profile column into one of $219$ letters of a profile alphabet and prefilters with a sequence-like comparison of these strings, then runs the full HMM–HMM alignment on the survivors. HHblits and the iterated profile search jackhmmer (HMMER) are the tools used to build the deep MSAs given to AlphaFold ([7.8.17](/7.8.17)).

The sensitivity of these methods for remote homologs follows a ladder: BLAST < PSI-BLAST < HMMER (jackhmmer) < HHblits, each step adding information about the families of the query and then of the targets. The simulation below isolates the effect of the scoring, by removing insertions and deletions so that every method uses the correct alignment.

![Why profiles detect remote homologs, in a simulation without insertions and deletions, so that the correct alignment is known and only the scoring differs. Sequences of 50 residues evolve under the PAM Markov chain (reconstructed from Dayhoff's PAM250 as in 7.8.3). For each distance D between the compared sequences, 400 homologous pairs of families are generated, each family of 10 sequences descending independently from a common root D/2 PAM away, and 2000 unrelated families serve as negatives. Scores: pairwise log-odds of the first members with the PAM matrix of the true distance (gray); the first member of the target against the position-specific scoring matrix of the query family, with pseudocounts (blue); profile against profile, the sum over columns of log2 Σ p(a)p′(a)/f(a) (purple). Plotted is the fraction of homologs scoring above the 99th percentile of the negatives (sensitivity at 1 % false positives). Information about the family of the query extends detection by roughly 150 PAM, and information about both families much further](./plots/profile-sensitivity.py)

## 5.6. Conservation

The simplest use of an MSA is to ask how variable each column is. Positions under strong functional constraint (catalytic residues, ligand-binding residues, residues buried in the core or at an interface) are conserved, and conservation is the most widely used predictor of functional importance and of the pathogenicity of missense variants ([7.8.12](/7.8.12)).

**Formula 5.6.1 (Column Conservation Scores)** For column $j$ with weighted residue frequencies $p_j(a)$:

- the Shannon entropy $H_j = -\sum_ap_j(a)\log_2p_j(a)$, between $0$ (invariant) and $\log_220 = 4.32$ bits; the information content $\log_220 - H_j$ is the height of a stack in a sequence logo ([7.1.4](/7.1.4#sec-4.4.2));
- the relative entropy $\sum_ap_j(a)\log_2[p_j(a)/q_a]$ with respect to the background $q$, which also rewards columns conserved for rare residues;
- the Jensen–Shannon divergence $\operatorname{JSD}(p_j, q) = \frac{1}{2}D(p_j \Vert m) + \frac{1}{2}D(q \Vert m)$ with $m = \frac{1}{2}(p_j + q)$ and $D$ the **Kullback–Leibler divergence**, which is bounded by $1$ bit and was found to predict catalytic and binding residues best among simple scores (Capra and Singh 2007).

Scores that account for the phylogeny of the sequences, such as the evolutionary rate of each site estimated on a tree (Rate4Site, used by ConSurf), are better still, because a column can look variable only because the alignment contains very distant sequences, or conserved only because all sequences are close relatives. The same holds for DNA: the conservation scores of genome browsers (phyloP, phastCons) are computed on a phylogeny of many species ([7.8.8](/7.8.8)).

![Conservation of the 40 columns around the Walker A motif of the MCM family (the alignment of the guide-tree figure: 15 sequences). A: sequence logo; stack height is the information content log₂20 − H in bits (with the small-sample correction), letters are scaled by their frequency. B: Shannon entropy of each column; the invariant residues G, D and P of GDP and K and S of the Walker A lysine and serine (columns 11–13, 17 and 18, stars) have entropy 0. C: Jensen–Shannon divergence between each column (pseudocount 0.1 per residue) and the background frequencies of Robinson and Robinson; it is high for conserved columns and highest where the conserved residue is rare in proteins. Column 14 separates the MCM6 proteins (S) from the other paralogs (G)](./plots/conservation.py)

**Example 5.6.1** In the Walker A region of the MCM family, the columns of G, D, P (GDP), K and S are invariant across all six eukaryotic paralogs and the archaeal protein, which diverged before the last common ancestor of eukaryotes, more than $1.5$ billion years of evolution; these residues bind the phosphates of ATP, and mutation of the lysine abolishes the ATPase activity of MCM subunits. Column $14$, where all MCM6 orthologs have S and all other paralogs G, is a *specificity-determining* position: conserved within each paralog group but different between groups, a pattern that distinguishes subfamily function from general function and that entropy computed over the whole family misses. Conservation is a property of single columns; the correlated change of two columns, which reveals residues in contact, is **coevolution**, analyzed with **Potts models** in [7.6.15](/7.6.15#sec-15.5.4).

## 5.7. Practice

```bash
# Multiple alignment: automatic choice of strategy, and the accurate iterative mode for small sets
mafft --auto mcm_family.fa > mcm_family.afa
mafft --localpair --maxiterate 1000 mcm_family.fa > mcm_family.linsi.afa
clustalo -i mcm_family.fa -o mcm_family.clustalo.afa --threads 8
famsa mcm_huge.fa mcm_huge.afa                       # millions of sequences

# Add new sequences to an existing alignment without realigning it
mafft --add new_sequences.fa --keeplength mcm_family.afa > mcm_family_plus.afa

# Coding sequences: align the proteins, then thread the codons onto the protein alignment
pal2nal.pl mcm6_proteins.afa mcm6_cds.fa -output fasta > mcm6_codon.afa

# Profile HMMs with HMMER
hmmbuild mcm6.hmm mcm6_orthologs.afa                 # build a model from an MSA
hmmsearch --tblout mcm6_hits.tbl -E 1e-5 mcm6.hmm uniprot_sprot.fasta
hmmscan --domtblout domains.tbl Pfam-A.hmm query.fa  # domains of a query (after hmmpress)
jackhmmer -N 3 --tblout iter.tbl MCM6_HUMAN.fa uniref50.fasta   # iterated search, like PSI-BLAST

# Iterated profile-profile search, as used to build MSAs for structure prediction
hhblits -i MCM6_HUMAN.fa -d UniRef30_2023_02 -n 3 -oa3m mcm6.a3m
```

```python
# The same model search from Python with pyhmmer (bindings to HMMER3)
import pyhmmer
alphabet = pyhmmer.easel.Alphabet.amino()
with pyhmmer.easel.MSAFile("mcm6_orthologs.afa", digital=True, alphabet=alphabet) as f:
    msa = f.read()
msa.name = b"MCM6"
builder = pyhmmer.plan7.Builder(alphabet)
hmm, _, _ = builder.build_msa(msa, pyhmmer.plan7.Background(alphabet))
with pyhmmer.easel.SequenceFile("targets.fa", digital=True, alphabet=alphabet) as f:
    targets = f.read_block()
for hits in pyhmmer.hmmsearch([hmm], targets):
    for hit in hits:
        print(hit.name, round(hit.score, 1), hit.evalue)   # bit score and E-value per target
```

Two practical cautions. An MSA is a hypothesis about homology at every column, and regions that are not homologous (different domains, low-complexity linkers, the ends of sequences of different length) are aligned anyway; such regions should be trimmed or masked before a tree or a conservation score is computed. And the choice of sequences matters as much as the program: fragments, misannotated genes and near-identical copies distort both the alignment and every statistic computed from it, so the input is usually filtered by length and clustered at a high identity first.

## Summary

| Topic | Key points |
|---|---|
| Objective | MSA (Definition 5.1.1); sum-of-pairs score, weighted (Definition 5.1.2), overcounts events on a tree |
| Complexity | $k$-dimensional DP, $O(2^kk^2n^k)$; NP-hard (Theorem 5.1.1); feasible for about $3$ to $10$ short sequences |
| Center star | align all to the center (Algorithm 5.2.1); SP within $2 - 2/k$ of optimal (Theorem 5.2.1, Example 5.2.1) |
| Progressive | profiles (Definition 5.3.1) merged along a guide tree (Definition 5.3.2, Algorithm 5.3.1); "once a gap, always a gap"; remedies: iteration (MUSCLE), consistency (T-Coffee), FFT and L-INS-i (MAFFT), HMM profiles (Clustal Omega), scale (FAMSA) |
| Evaluation | reference benchmarks, SP and TC accuracy (Definition 5.3.3, Example 5.3.1) |
| PSSM | log-odds $\log_2[p_j(a)/q_a]$ (Definition 5.4.1); Henikoff weights (Formula 5.4.1, Example 5.4.1); substitution-matrix or Dirichlet-mixture pseudocounts (Formula 5.4.2) |
| PSI-BLAST | iterated PSSM search (Definition 5.4.2, Algorithm 5.4.1); profile drift; remote homology (Definition 5.4.3) |
| HMMs | pair HMM: Viterbi = Gotoh, forward = sum over alignments, posteriors; profile HMM with M/I/D states (Definition 5.5.1), Viterbi in $O(Kn)$ (Algorithm 5.5.1), local mode; HMMER3 filters and E-values ($\lambda = \ln 2$); Pfam, InterPro; the MCM6 profile scores paralogs $40$–$50\,\%$ higher than the pairwise query (Example 5.5.1) |
| Profile–profile | HHpred, HHblits (profile alphabet of $219$ letters); sensitivity ladder BLAST < PSI-BLAST < HMMER < HHblits; simulation of the gain |
| Conservation | entropy, relative entropy, Jensen–Shannon divergence (Formula 5.6.1); phylogeny-aware rates; specificity-determining positions; conservation versus coevolution (Example 5.6.1) |

## Questions

1. Compute the number of cells and moves of the exact dynamic program for aligning $4$ sequences of $200$ residues, and explain why the number of moves per cell is $2^k - 1$.

   **Answer** The lattice has $201^4 \approx 1.6\times10^9$ cells. In each move every row either advances by one residue or receives a gap, and at least one row must advance (an all-gap column is forbidden): $2^4 - 1 = 15$ moves per cell, so about $2.4\times10^{10}$ moves, each scoring $\binom{4}{2} = 6$ pairs. This is feasible on a computer for four sequences, but every further sequence multiplies the work by about $400$ ($2 \times 200$), so the method stops at a handful of sequences.

2. A column of an MSA of $10$ sequences has L in nine sequences and I in one. With BLOSUM62 ($s(\mathrm{L},\mathrm{L}) = 4$, $s(\mathrm{L},\mathrm{I}) = 2$), compute its SP score, and explain what is unsatisfactory about it as a model of evolution.

   **Answer** $\binom{9}{2} \times 4 + 9 \times 2 = 36 \times 4 + 18 = 162$. If the ten sequences are related by a tree, the column is explained by a single L → I substitution on one branch; the SP score instead counts the nine L–I pairs as nine separate substitutions and the $36$ L–L pairs as independent observations of conservation. The SP score therefore over-weights sequences that are close relatives and does not correspond to any evolutionary event count; weighted SP scores and tree-based or probabilistic objectives (profile HMMs) are attempts to correct this.

3. Prove that in the center-star method every induced pairwise alignment between a sequence and the center is optimal, and explain why the induced alignment between two non-center sequences need not be.

   **Answer** Each sequence $t$ was aligned optimally to the center, and merging only inserts columns in which both $t$ and the center have gaps (the gaps that other sequences introduced into the center); deleting such all-gap columns from the induced pair restores the optimal alignment of $t$ with $c$, at the same cost because gap–gap columns cost $0$. Two non-center sequences $r$ and $t$ are aligned only through the center: residues of $r$ and $t$ aligned to the same center residue are aligned to each other, whether or not that is optimal for $r$ and $t$; when both are far from the center, their direct optimal alignment can be much better. The triangle inequality bounds the loss: $D(r, t) \le d(r, c) + d(c, t)$.

4. Compute the Henikoff weights of the three sequences ACDE, ACDF and GCHF, and say which sequence is down-weighted and why.

   **Answer** Column $1$ (A, A, G; $c = 2$): A sequences $1/(2 \times 2) = 1/4$ each, G $1/2$. Column $2$ (all C): $1/3$ each. Column $3$ (D, D, H): $1/4$, $1/4$, $1/2$. Column $4$ (E, F, F): E $1/2$, each F $1/4$. Totals: ACDE $1/4 + 1/3 + 1/4 + 1/2 = 4/3$; ACDF $1/4 + 1/3 + 1/4 + 1/4 = 13/12$; GCHF $1/2 + 1/3 + 1/2 + 1/4 = 19/12$. Normalized: $0.33$, $0.27$, $0.40$. ACDF is down-weighted most because it shares its residue with another sequence at every variable column (A and D with ACDE, F with GCHF): its information is largely duplicated. GCHF, the most distinct, receives the largest weight.

5. A column of a PSSM is estimated from $N = 4$ (effective) sequences, all with W. Using Formula 5.4.2 with $B = 5$, and assuming that under BLOSUM62's target frequencies $\mathbb{P}(\mathrm{W} \mid \mathrm{W}) = 0.49$, $\mathbb{P}(\mathrm{Y} \mid \mathrm{W}) = 0.07$, compute $p(\mathrm{W})$ and $p(\mathrm{Y})$, and the PSSM scores for $q_{\mathrm{W}} = 0.013$, $q_{\mathrm{Y}} = 0.032$.

   **Answer** $g(\mathrm{W}) = 0.49$, $g(\mathrm{Y}) = 0.07$. $p(\mathrm{W}) = (4 + 5 \times 0.49)/9 = 6.45/9 = 0.717$; $p(\mathrm{Y}) = (0 + 5 \times 0.07)/9 = 0.039$. Scores: $\log_2(0.717/0.013) = \log_255.2 = 5.8$ bits for W; $\log_2(0.039/0.032) = 0.28$ bits for Y. Without pseudocounts Y would be impossible ($-\infty$), although tyrosine replaces tryptophan in many families; with them, a Y at this position is mildly favorable and a W strongly so. With $N = 40$ the data would dominate: $p(\mathrm{W}) = (40 + 2.45)/45 = 0.94$.

6. Explain profile drift in PSI-BLAST with an example, and name three ways to reduce it.

   **Answer** Suppose a query contains a domain A and a coiled coil. In the first iteration a protein with domain B and a coiled coil is included because of a significant coiled-coil alignment. The PSSM now contains columns describing the coiled coil strongly, and the second iteration includes many coiled-coil proteins of unrelated families; after a few iterations the profile represents coiled coils rather than domain A, and the reported homologs are false. Remedies: mask low-complexity and coiled-coil regions in the query (SEG, COILS); use a strict inclusion threshold ($E \le 0.001$) and few iterations; inspect the sequences added at each iteration and exclude suspicious ones; restrict the profile to the domain of interest; or use methods with better statistics for profiles (jackhmmer, HHblits).

7. Show how the Viterbi recursion of a pair HMM with gap-opening probability $\delta$ and extension probability $\varepsilon$ yields an affine gap penalty, and compute the penalties for $\delta = 0.02$, $\varepsilon = 0.4$ in bits.

   **Answer** A gap of length $k$ along a Viterbi path consists of one transition $M \to X$ (probability $\delta$), $k - 1$ transitions $X \to X$ (probability $\varepsilon$ each) and one transition back $X \to M$ (probability $1 - \varepsilon$), and the emitted residues are scored against the background, contributing nothing to the log-odds. The log-probability is $\log\delta + (k-1)\log\varepsilon + \log(1 - \varepsilon)$, compared with $\log(1 - 2\delta)$ per step for staying in $M$: affine in $k$, with opening cost $d = -\log_2[\delta(1 - \varepsilon)/(1 - 2\delta)]$ and extension cost $e = -\log_2\varepsilon$. Numerically $d = -\log_2(0.02 \times 0.6/0.96) = -\log_2(0.0125) = 6.3$ bits and $e = -\log_20.4 = 1.3$ bits, about $12.6$ and $2.6$ in half-bit units, the same order as the gap costs used with BLOSUM62 ($11 + k$ in units of about half a bit).

8. In Example 5.5.1 the profile HMM of MCM6 orthologs scores the human paralogs $40$ to $50\,\%$ higher in bits than a pairwise alignment of human MCM6 with the same targets. Give two reasons, and explain why scores of close homologs are not the right test of a remote-homology method.

   **Answer** First, the match emissions are position specific: at the many columns invariant across the family (the Walker A and B motifs, the arginine finger, structural glycines), the profile gives large scores to the conserved residue and does not reward chance identities at variable columns, so true homologs gain more score than random sequences. Second, the transitions are position specific: insertions and deletions are cheap where the orthologs themselves vary in length and expensive in the conserved core, which keeps the alignment of the paralogs on the right register. The paralogs and the archaeal MCM are far above any threshold under both methods; what matters for remote homology is the separation of true and false hits near the threshold, measured as sensitivity at a fixed false-positive rate on benchmarks of structurally verified remote homologs (as in the simulation of Section 5.5.4).

9. For a column with frequencies $p = (1, 0, \dots, 0)$ (all residues the same, say W) and another with all residues A, compute the Shannon entropy and the relative entropy to the background ($q_{\mathrm{W}} = 0.013$, $q_{\mathrm{A}} = 0.078$). Why do some conservation scores prefer the second measure?

   **Answer** Both columns have entropy $0$ bits: entropy does not distinguish which residue is conserved. The relative entropies are $\log_2(1/0.013) = 6.3$ bits for W and $\log_2(1/0.078) = 3.7$ bits for A. A conserved alanine is less surprising, because alanine is common and is also found in unconstrained columns of a few sequences by chance, while a conserved tryptophan in a deep alignment is rarely an accident. Relative entropy and the Jensen–Shannon divergence take this into account; in a small alignment, however, a column of rare residues can look extremely conserved by chance, so these scores need enough sequences and pseudocounts.

10. (Design) You have a protein of unknown function from an archaeal metagenome. BLASTP against nr finds no hit with $E < 10$. Plan a sequence of analyses to find homologs and possible functions, and say what each step adds.

    **Answer** (1) Check the sequence: complete open reading frame, no frame shifts, low-complexity or transmembrane segments (SEG, a topology predictor), which explain or confound failures. (2) Search with profiles of the query: jackhmmer or PSI-BLAST against UniRef50 or a metagenomic protein database, iterating with a strict inclusion threshold; more diverse homologs, even without known function, build a deeper profile. (3) Search the resulting profile against family databases: hmmscan against Pfam, and HHpred (profile–profile) against Pfam, PDB and other family HMMs, the most sensitive sequence-based step, which often detects homology at $10$–$20\,\%$ identity. (4) If still nothing is found, predict the structure ([7.8.17](/7.8.17)) from the MSA and search structure databases with Foldseek ([7.8.4](/7.8.4#sec-4.7.3)), since structure is conserved longer than sequence. (5) Interpret cautiously: a remote homolog suggests a fold and perhaps a general biochemical activity; specific function requires the conservation of active-site residues in the alignment (Section 5.6), genomic context (neighboring genes, operons) and ultimately experiment.
