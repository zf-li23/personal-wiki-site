---
title: The Physics of Sequences, Specificity and Evolution
description: "Biological information in sequences: genomes and mutation rates by the numbers. Comparing sequences as statistical mechanics: HP-model scores, log-odds scoring matrices as interaction energies, the extreme-value statistics of chance similarity, the Jukes–Cantor model, the molecular clock and the dating of HIV. Sequence and specificity: binding sites in a genome of decoys, the minimal length of a unique site, the selection theory of Berg and von Hippel and the stationary distribution of Sella and Hirsh. Evolution on fitness landscapes: epistasis, accessible mutational paths, biophysical landscapes from folding stability and marginal stability. Drug resistance: pre-existing mutants, combination therapy, the mutant selection window, viruses at the error threshold. Fidelity across the central dogma."
---

The macromolecules of the previous chapters are specified by sequences, and sequences are what evolution changes. This chapter looks at sequences with the tools of statistical physics. Three questions organize it. How much information does a sequence carry, and how can two sequences be compared so that their similarity can be trusted? How does the sequence of a binding site determine which proteins bind it, and how does selection on binding shape the sequences we observe? And how do populations move through the space of sequences, on **fitness** landscapes whose shape is set by the physics of folding and binding, in the cases where we can watch it happen: the evolution of resistance to drugs in bacteria and viruses?

The thermodynamics of molecular recognition and the energy-matrix model of DNA binding were developed in [7.6.17](/7.6.17#sec-17.7.3), kinetic **proofreading** in [7.6.17](/7.6.17#sec-17.9) and [7.6.38](/7.6.38#sec-38.5.2), protein folding and the **designability** of folds in [7.6.16](/7.6.16), and **robustness** and neutral networks in [7.6.40](/7.6.40). The algorithms of sequence alignment (dynamic programming, BLAST, multiple alignment and the construction of phylogenetic trees) belong to bioinformatics ([7.8](/7.8)), and the systematic theory of **population genetics** to genetics ([7.4.23](/7.4.23)) and evolutionary biology ([7.10](/7.10)); here we use their results where the physics of sequences needs them. The chapter follows chapter 21 of *Physical Biology of the Cell*.

## 41.1. Biological Information

### 41.1.1. Why Sequences?

Information in a cell is stored and transmitted in many forms: the conformation of a protein, the frequency of action potentials, the inherited structure of a membrane, the pattern of chromatin marks. Sequence information is privileged for two reasons. First, it is copied with the highest fidelity over the most generations, by a machinery (replication, transcription, translation with a nearly universal **genetic code**) that has been conserved for more than three billion years. Second, it is to a good approximation context independent: a codon UUU means phenylalanine wherever it occurs in a **reading frame**, a binding site for RNA polymerase is a binding site wherever it lies. Context independence is what makes sequences comparable letter by letter and makes quantitative measures of similarity meaningful; it is also an approximation that fails in interesting ways (codon context, the structural context of a residue, **epistasis** between sites, 41.4).

Each position of a DNA sequence carries at most $\log_24 = 2$ bits; a protein position at most $\log_220 = 4.3$ bits. The genome of *E. coli*, $4.6\times10^6\,\mathrm{bp}$, holds at most $9.2\times10^6$ bits, a little over a megabyte, the size of a book of a thousand pages; the **haploid** human genome, $3.1\times10^9\,\mathrm{bp}$, about $780$ megabytes. These are upper bounds: real sequences are not random (base composition, repeats, codon bias), and the information that matters biologically, the sequence that is constrained by selection, is a fraction of the total (about $5$–$10\,\%$ of the human genome by comparative estimates).

### 41.1.2. Genomes and Mutations by the Numbers

Information is copied with errors, and the errors are the raw material of evolution.

| Quantity | *E. coli* | Human | RNA viruses (HIV) |
|---|---|---|---|
| genome size | $4.6\,\mathrm{Mb}$ | $3.1\,\mathrm{Gb}$ (haploid) | $10^4$ nt (HIV: $9.7\,\mathrm{kb}$) |
| genes | $\sim4300$ | $\sim20\,000$ protein-coding | $9$ |
| mutation rate per site per replication | $\sim2\times10^{-10}$ | $\sim1.2\times10^{-8}$ per generation ($\sim10^{-10}$ per cell division) | $10^{-6}$–$10^{-4}$ (HIV: $3\times10^{-5}$) |
| mutations per genome per replication | $\sim10^{-3}$ | $\sim70$ new mutations per child | $\sim0.3$ (HIV) |
| population size (per host or species) | $10^8$–$10^{10}$ per culture | $N_e \approx 10^4$ | $10^{10}$ virions produced per day in a patient |

Two regularities stand out. For DNA-based microbes, the mutation rate per genome per replication is roughly constant, about $0.003$, although genome sizes vary a hundredfold (Drake's rule, 1991); RNA viruses copy with error rates near the inverse of their genome length, close to the **error threshold** of 41.5.4. And across organisms, the mutation rate per site falls as the **effective population size** rises. Lynch's drift-barrier hypothesis explains this by the limited power of selection: selection can lower the mutation rate only until the fitness benefit of a further reduction is smaller than $1/N_e$, below which drift dominates ([7.4.23](/7.4.23#sec-23.6)); large populations can refine their polymerases further. The fidelity of the copying machinery itself and the free energy it costs are summarized in 41.6.

Reading sequences is a physical measurement. Sanger sequencing exploits the fact that DNA polymerase incorporates dideoxynucleotides, which terminate the chain, and separates the terminated products by length; sequencing by synthesis detects each incorporated nucleotide by a flash of light (pyrosequencing) or a cleavable fluorescent terminator on amplified clusters; single-molecule methods read the current through a **nanopore** as the strand is pulled through ([7.6.12](/7.6.12)) or the fluorescence of a single polymerase in a zero-mode waveguide. The first bacterial genome was sequenced in 1995; the cost of sequencing a human genome has since fallen by about six orders of magnitude.

## 41.2. Comparing Sequences

### 41.2.1. Scores as Energies

To ask whether two sequences are related by descent, we align them and score the alignment. In the two-letter **HP model** of [7.6.16](/7.6.16), where each residue is hydrophobic ($\sigma_i = 1$) or polar ($\sigma_i = 0$), the score of an ungapped alignment of sequences $\sigma$ and $\sigma'$ is a sum over positions,

$$
S = \sum_i\left[\varepsilon_{HH}\sigma_i\sigma_i' + \varepsilon_{PP}(1 - \sigma_i)(1 - \sigma_i') + \varepsilon_{HP}\left(\sigma_i(1 - \sigma_i') + (1 - \sigma_i)\sigma_i'\right)\right], \tag{41.1}
$$
with positive scores for matches and a negative score for mismatches; an insertion or deletion is charged a gap penalty. The form of Eq. (41.1) is that of an energy of a lattice model with site-wise interactions, and the analogy can be made precise.

**Definition 41.2.1 (Log-Odds Score)** The **log-odds score** for aligning residue $a$ with residue $b$ is

$$
s_{ab} = \frac{1}{\lambda}\ln\frac{p_{ab}}{q_aq_b},
$$
where $p_{ab}$ is the frequency with which $a$ and $b$ are found aligned in pairs of truly related sequences, $q_a$ and $q_b$ are the background frequencies of the residues, and $\lambda$ sets the unit (BLOSUM matrices are given in half-bits, $\lambda = \frac{1}{2}\ln 2$). The score of an alignment is the sum of the $s_{ab}$ over aligned pairs.

The log-odds score is the log-likelihood ratio of two hypotheses: that the aligned pairs were generated by a model of related sequences, $\prod p_{ab}$, or independently, $\prod q_aq_b$. By the Neyman–Pearson lemma it is the most powerful statistic to distinguish them. In the language of statistical mechanics, write $q_a \propto \mathrm{e}^{-\beta\varepsilon_a}$ and $p_{ab} \propto \mathrm{e}^{-\beta(\varepsilon_a + \varepsilon_b + \varepsilon_{ab})}$: the score is minus an interaction energy $\varepsilon_{ab}$ between residues at the same position, and a high score means that the pair is found together more often than chance, as if attracted. The empirical matrices (PAM from closely related proteins, Dayhoff 1978; BLOSUM from conserved blocks of distant ones, Henikoff and Henikoff 1992) encode the physics of substitutions: high scores between residues of similar size and polarity (isoleucine and valine), large positive diagonal entries for rare and structurally special residues (tryptophan, cysteine).

### 41.2.2. The Statistics of Chance Similarity

A score means something only if we know how high it would be by chance. Two random sequences always have some similar stretch, and its best score grows with the size of the search.

**Theorem 41.2.1 (Karlin–Altschul Statistics)** For two random sequences of lengths $m$ and $n$ with independent letters, and a scoring system whose expected score per aligned pair is negative and in which a positive score is possible, the number of distinct ungapped local alignments with score at least $S$ is asymptotically Poisson with mean

$$
E(S) = Kmn\,\mathrm{e}^{-\lambda S}, \tag{41.2}
$$
where $\lambda > 0$ is the unique positive solution of $\sum_{a,b}q_aq_b\mathrm{e}^{\lambda s_{ab}} = 1$ and $K$ is a constant. Consequently the maximal score $S_{\max}$ follows an extreme-value (Gumbel) distribution, $\mathbb{P}(S_{\max} < x) \approx \exp(-Kmn\mathrm{e}^{-\lambda x})$, with mean growing as $\ln(Kmn)/\lambda$ (Karlin and Altschul 1990).

The mean of the best score grows only logarithmically with the search space; this is why database searches work: a real homologue of a hundred residues scores far above the chance level even in a database of $10^9$ residues. The $E$ value that BLAST reports is Eq. (41.2) for the observed score, the expected number of equally good hits by chance. The condition $\sum q_aq_b\mathrm{e}^{\lambda s_{ab}} = 1$ also shows that $\lambda$ makes $q_aq_b\mathrm{e}^{\lambda s_{ab}}$ a probability distribution, the "target frequencies" $p_{ab}$ for which the scoring system is optimal: every scoring matrix implicitly assumes a model of related sequences. For DNA with match score $+1$, mismatch $-1$ and uniform bases, $\frac{1}{4}\mathrm{e}^{\lambda} + \frac{3}{4}\mathrm{e}^{-\lambda} = 1$ gives $\mathrm{e}^\lambda = 3$, $\lambda = \ln 3$, which the simulation in the figure reproduces.

![Statistics of sequence comparison. A: best ungapped local alignment scores (match +1, mismatch −1, found by a maximum-subarray scan of all diagonals) for 1000 pairs of random DNA sequences of 200 bases (gray) with the moment-fitted Gumbel distribution (red), and for 1000 pairs of related sequences, each descended from a common random ancestor with 20 % of sites mutated in each copy (blue): related pairs score far beyond the chance tail. B: mean best score of random pairs against ln(mn): a straight line with slope close to 1/λ = 1/ln 3 = 0.91, the logarithmic growth predicted by Theorem 41.2.1](./plots/alignment-statistics.py)

### 41.2.3. Divergence and the Molecular Clock

The fraction of differing sites between two sequences underestimates the number of substitutions that separate them, because a site can change more than once. A Markov model of substitution corrects for this.

**Formula 41.2.1 (Jukes–Cantor Distance)** If every base changes to each of the three others at rate $\alpha$ (total rate $3\alpha$ per site), the probability that a site differs between two sequences separated by time $t$ along each of two lineages, i.e. by $d = 6\alpha t$ expected substitutions per site, is

$$
p = \frac{3}{4}\left(1 - \mathrm{e}^{-4d/3}\right), \qquad\text{so}\qquad d = -\frac{3}{4}\ln\left(1 - \frac{4}{3}p\right). \tag{41.3}
$$

**Proof** Along a path of total length $2t$ between the two sequences, a site is a continuous-time **Markov chain** on four states with rate $\alpha$ to each other state. The probability $P(\tau)$ of being in the initial state obeys $\dot P = -3\alpha P + \alpha(1 - P)$, so $P(\tau) = \frac{1}{4} + \frac{3}{4}\mathrm{e}^{-4\alpha\tau}$. With $\tau = 2t$ and $d = 3\alpha\cdot2t$, the probability of a difference is $1 - P = \frac{3}{4}(1 - \mathrm{e}^{-4d/3})$. $\square$

For small $d$, $p \approx d$; as $d$ grows, $p$ saturates at $3/4$, the difference between two random sequences, and the correction diverges. More realistic models allow different rates for transitions and **transversions**, unequal base frequencies and rate variation among sites; they are the basis of phylogenetic inference ([7.8](/7.8)).

If substitutions accumulate at a roughly constant rate, divergence measures time: the **molecular clock** of Zuckerkandl and Pauling (1965), explained by the neutral theory as the rate of **neutral mutation** ([7.4.23](/7.4.23#sec-23.7)). Different proteins tick at different rates, fast for fibrinopeptides, which are cut off and discarded, slow for histones and cytochrome *c*, whose sequences are constrained; the rate is set by the fraction of positions at which changes are neutral. Two applications show the power of the idea.

**Example 41.2.1 (When HIV Entered Humans)** HIV-1 evolves so fast that sequences from patients sampled over a few decades differ measurably. Korber and colleagues (2000) regressed the genetic distance of envelope sequences from their reconstructed common ancestor against the year of sampling; extrapolating the line to zero distance dated the ancestor of the pandemic group M to about 1931 (95 % interval 1915–1941). A sequence from a blood sample taken in Kinshasa in 1959 fell on the line, a test of the method. Later analyses with more sequences and models allowing rate variation placed the origin near 1908 (Worobey and colleagues 2008); the jump from chimpanzees to humans happened in west-central Africa early in the twentieth century.

**Example 41.2.2 (What a Dinosaur Saw)** The rod pigment rhodopsin of vertebrates absorbs maximally at wavelengths from about $480$ to $510\,\mathrm{nm}$, depending on a few residues near the retinal ([7.6.18](/7.6.18)). Chang and colleagues (2002) inferred the most probable sequence of the rhodopsin of the common ancestor of birds and crocodilians, an archosaur of about $240$ million years ago, synthesized the gene, expressed the protein and measured its absorption maximum: $508\,\mathrm{nm}$, slightly red-shifted like the rhodopsins of modern birds. Ancestral sequence reconstruction turns phylogenies into experiments on extinct proteins.

![Divergence and the molecular clock. A: the fraction of differing sites between two sequences against the true number of substitutions per site separating them, under the Jukes–Cantor model (line, Formula 41.2.1) and for simulated sequences of 1000 sites (circles); the observed difference saturates at 3/4, and the Jukes–Cantor correction (squares) recovers the true distance with increasing scatter as saturation is approached. B: root-to-tip regression with simulated sequences, in the manner of the dating of HIV-1: 60 sequences of 2500 sites sampled between 1983 and 1997 from lineages that left a common ancestor in 1930 and accumulate substitutions at 2.4 × 10⁻³ per site per year with lineage-to-lineage rate variation, and one sample from 1959 (diamond); the regression line extrapolated to zero distance estimates the date of the ancestor, with a bootstrap 95 % interval (shaded) of a few decades](./plots/divergence.py)

## 41.3. Sequence and Specificity

### 41.3.1. Binding Sites in a Genome of Decoys

A transcription factor must find its sites among millions of others. In the energy-matrix model of [7.6.17](/7.6.17#sec-17.7.3), the binding free energy of a site is a sum of contributions of its positions; in the simplest version, a site of length $L$ with $k$ mismatches to the consensus has energy $E_k = E_0 + k\varepsilon$, with $\varepsilon \approx 1$–$3\,k_{\mathrm{B}}T$ per mismatch for typical bacterial factors. The probability that the site is occupied is a Fermi function of its energy,

$$
p(k) = \frac{1}{1 + \mathrm{e}^{(E_k - \mu)/k_{\mathrm{B}}T}}, \tag{41.4}
$$
where $\mu$ is the chemical potential of the free protein, set by its concentration. In a random genome of $G$ base pairs (both strands), the expected number of sites with $k$ mismatches is $N_k = 2G\binom{L}{k}3^k/4^L$, which grows rapidly with $k$ up to $k \approx 3L/4$.

The two factors pull in opposite directions. The number of decoys at distance $k$ grows roughly as $(3L)^k/k!$, the occupancy falls as $\mathrm{e}^{-k\varepsilon/k_{\mathrm{B}}T}$; if $\varepsilon$ is too small, the protein is spread over thousands of near-consensus sites and the specific site is occupied only if the protein is abundant. Two simple consequences follow. First, a site is unique in a random genome only if $4^L > 2G$, that is $L > \log_4(2G)$: $12$ bp for *E. coli*, $16$ bp for the human genome. Real bacterial sites are of this length; eukaryotic factors often recognize only $6$–$10$ bp and rely on cooperativity, clustering and chromatin to be specific. Second, the useful range of $\varepsilon$ is bounded above as well: a protein that discriminates too strongly binds nonspecific DNA so weakly that it cannot use facilitated diffusion, and one whose specific binding energy exceeds $L\varepsilon$ too much stays bound too long; Gerland, Moroz and Hwa (2002) showed that these constraints place the optimal mismatch energy at about $2$–$3\,k_{\mathrm{B}}T$, as measured.

![Sequence and specificity of a DNA-binding protein recognizing 12 bp. A: occupancy of a site against its number of mismatches to the consensus (Eq. (41.4)) for mismatch energies of 1, 2 and 3 kBT, the consensus being 99 % occupied. B: expected number of occupied sites with k mismatches in a random genome of 4.6 Mb (both strands): the number of sites at each distance (dashed) times their occupancy; with weak discrimination the protein is mostly bound to hundreds of thousands of decoys. C: selection on binding sites produces Boltzmann statistics. Binding sites evolving under selection for occupancy with a random position- and base-specific energy matrix (weak-mutation dynamics, population size 200, stationary distribution sampled by Monte Carlo, Theorem 41.3.1): the logarithm of the frequency of each base relative to the consensus at each position falls linearly with its mismatch energy, as Berg and von Hippel's theory predicts (Corollary 41.3.1)](./plots/specificity.py)

### 41.3.2. Selection Theory of Binding Sites

The sites of a transcription factor in a genome are not identical: they are a collection of sequences that bind well enough. Berg and von Hippel (1987) proposed that their statistics reflect selection on binding energy: positions at which a mismatch costs little are variable, positions at which it costs much are conserved. The idea can be derived from population genetics in the regime of weak mutation, where a population is almost always **monomorphic** and moves from one sequence to another by the fixation of single mutants.

**Theorem 41.3.1 (Stationary Distribution under Weak Mutation)** Consider a haploid population of constant size $N$ evolving by the Moran process, in which each genotype $g$ has fitness $F(g)$, mutations arise rarely ($N\mu \ll 1$) and the mutation rates between any two genotypes are symmetric. Then the population performs a Markov chain on genotypes whose stationary distribution is

$$
\pi(g) \propto F(g)^{N-1}. \tag{41.5}
$$
With $F(g) = \mathrm{e}^{-\phi(g)}$ for a "fitness potential" $\phi$, $\pi(g) \propto \mathrm{e}^{-(N-1)\phi(g)}$: a Boltzmann distribution with energy $\phi$ and inverse temperature $N - 1$ (Sella and Hirsh 2005).

**Proof** A mutant $h$ arising in a population fixed for $g$ is fixed with the Moran fixation probability $\Pi(g \to h) = (1 - r^{-1})/(1 - r^{-N})$, $r = F(h)/F(g)$ (the analogue for the Moran model of Kimura's formula, [Theorem 23.6.1](/7.4.23#thm-23.6.1) of 7.4.23). The rate of transitions $g \to h$ of the monomorphic population is $N\mu_{gh}\Pi(g \to h)$. With $\mu_{gh} = \mu_{hg}$,

$$
\frac{N\mu_{gh}\Pi(g \to h)}{N\mu_{hg}\Pi(h \to g)} = \frac{(1 - r^{-1})(1 - r^{N})}{(1 - r^{-N})(1 - r)} = r^{N-1},
$$
using $(1 - r^{-1})/(1 - r) = -r^{-1}$ and $(1 - r^N)/(1 - r^{-N}) = -r^N$. The ratio of forward to backward rates equals $\pi(h)/\pi(g)$ with $\pi \propto F^{N-1}$, so this distribution satisfies detailed balance (Theorem 38.1.1 of [7.6.38](/7.6.38#sec-38.1.1)) and is stationary. $\square$

The analogy with statistical mechanics is exact in this regime: fitness plays the role of a Boltzmann factor, the population size that of inverse temperature, and the number of genotypes with a given fitness that of entropy. In small populations ("high temperature") sequences spread over many genotypes of lower fitness, in large ones they concentrate on the fittest; the competition between the number of sequences and their fitness is a free-energy minimization, $\ln\pi = -(N - 1)\phi + \ln\Omega$ for classes of $\Omega$ genotypes.

**Corollary 41.3.1 (Berg–von Hippel Relation)** If fitness depends on a binding energy that is a sum of independent position contributions, $E(s) = \sum_i\varepsilon_i(s_i)$, and fitness is locally exponential in the energy, $F \propto \mathrm{e}^{-\beta_{\mathrm{s}}E}$ over the range of energies that occur, then the bases at each position of selected sites are independently distributed with

$$
\ln\frac{f_i(b)}{f_i(b_{\mathrm{cons}})} = -\lambda\,\varepsilon_i(b), \qquad \lambda = (N - 1)\beta_{\mathrm{s}}, \tag{41.6}
$$
where $f_i(b)$ is the frequency of base $b$ at position $i$ and $\varepsilon_i(b)$ its energy relative to the consensus base.

The corollary justifies the use of position weight matrices built from collections of sites as estimates of binding energies, up to a scale factor $\lambda$; the simulation in panel C of the figure checks it with a sigmoidal (occupancy) fitness, which is locally exponential near the selected energies. It also gives a meaning to the information content of a collection of sites, $R_{\mathrm{seq}} = \sum_i[2 + \sum_bf_i(b)\log_2f_i(b)]$ bits, the quantity displayed by a sequence logo ([7.8](/7.8)): Schneider and colleagues (1986) found that for many bacterial factors $R_{\mathrm{seq}}$ is close to $\log_2(G/\gamma)$, the information needed to pick $\gamma$ sites out of a genome of $G$ positions, as if sites had evolved to be just specific enough. The relation fails for factors whose sites are bound cooperatively or whose fitness depends on more than binding, and the energy matrices measured directly by high-throughput binding assays ([7.6.17](/7.6.17#sec-17.7.3)) are the better estimates when available.

### 41.3.3. Sequence and Nucleosome Positioning

Sequence also determines where **nucleosomes** prefer to sit. Wrapping $147$ bp around the histone octamer bends the DNA by about $0.5\,k_{\mathrm{B}}T$ per base pair ([7.6.21](/7.6.21#sec-21.7)), and sequences with AA, TT and TA steps repeated every $10$ bp in phase with the helical turn, where the minor groove faces the octamer, bend more easily ([7.2.4](/7.2.4#sec-4.4)). Segal and colleagues (2006) built a probabilistic model of nucleosome sequence preferences from sequences of isolated nucleosomes and predicted a substantial part of the nucleosome organization of yeast; the remainder comes from statistical positioning next to barriers (the excluded-volume packing of nucleosomes next to a bound factor, a one-dimensional hard-rod gas) and from remodelers. The genome thus contains, superimposed on the code for proteins, a weaker code for its own packaging, written in the same four letters and read through the physics of DNA bending.

## 41.4. Evolution on Fitness Landscapes

### 41.4.1. Fitness Landscapes and Epistasis

**Definition 41.4.1 (Fitness Landscape)** A **fitness landscape** is a function $F\colon\mathcal{S} \to \mathbb{R}$ assigning a fitness (a growth rate, a resistance level, a binding affinity used as a proxy) to each genotype in a sequence space $\mathcal{S}$, where genotypes differing by one mutation are neighbours (Wright 1932; for sequences, Maynard Smith 1970). For $L$ biallelic sites the space is the hypercube $\{0, 1\}^L$; for proteins of length $L$, a graph of $20^L$ vertices of degree $19L$.

A landscape is additive (in logarithm) if every mutation has the same effect in every background; otherwise the sites interact, which is **epistasis** in the sense of evolutionary genetics: the deviation of the effect of a combination of mutations from the sum of their individual effects. Epistasis comes in degrees. In *magnitude epistasis* the size but not the sign of a mutation's effect depends on the background; in *sign epistasis* a mutation that is beneficial in one background is deleterious in another; in *reciprocal sign epistasis* two mutations are each deleterious alone and beneficial together. Only the last can create separate peaks: a landscape without reciprocal sign epistasis has a single fitness maximum (Poelwijk and colleagues 2011), and multiple peaks, on which populations can be trapped, require it.

### 41.4.2. Adaptive Walks and Accessible Paths

In a population with small $N\mu$ and strong selection, beneficial mutations fix one at a time and deleterious ones are lost; the population performs an adaptive walk, moving at each step to a fitter neighbour. Which of the many possible orders of mutations can such a walk take?

**Example 41.4.1 (Five Mutations to Antibiotic Resistance)** Five point mutations in the β-lactamase TEM-1 of *E. coli*, together with a promoter mutation, increase resistance to the antibiotic cefotaxime about $10^5$-fold. Weinreich, Delaney, DePristo and Hartl (2006) constructed all $2^5 = 32$ combinations of the five mutations in the coding sequence and measured the resistance of each. Of the $5! = 120$ orders in which the mutations could be acquired one by one, $102$ contain at least one step that lowers resistance (or leaves it unchanged), and are inaccessible to an adaptive walk; most of the probability of reaching the quintuple mutant is concentrated on a handful of paths. Sign epistasis, mostly through effects on stability and on the balance between activity and folding, makes evolution far more predictable than the number of possible orders suggests.

The rough Mount Fuji model (Aita and colleagues 2000) captures this: an additive trend plus an independent random contribution of size $\sigma$ for each genotype. With $\sigma = 0$ all paths are accessible; as $\sigma$ grows, sign epistasis becomes common and the fraction of accessible paths falls, reaching the value observed for TEM-1 when the random part is comparable to the mean effect of a mutation.

![Accessible mutational paths on rugged fitness landscapes (rough Mount Fuji model: five mutations with additive effects between 0.5 and 1.5 plus a random contribution of standard deviation σ for each of the 32 genotypes). A: an example landscape with σ = 1.5, genotypes plotted by number of mutations and fitness, single-mutation steps as gray lines; only 3 of the 120 orders in which the five mutations can be added increase fitness at every step (red). B: mean fraction of accessible paths among landscapes in which the quintuple mutant is the fitter end, against σ (400 landscapes per value): all paths are open without epistasis, and the fraction falls to the value measured for the five resistance mutations of TEM-1 β-lactamase (18 of 120, dashed) when the random part equals the mean additive effect](./plots/landscape.py)

### 41.4.3. Biophysical Fitness Landscapes

For many proteins, the dominant physical determinant of fitness is folding stability: a protein that is unfolded does not work and may aggregate. If fitness is proportional to the fraction of molecules folded, the two-state model of folding ([7.6.16](/7.6.16)) gives a landscape with a simple shape.

**Formula 41.4.1 (Stability Fitness Landscape)** With folding free energy $\Delta G$ (negative for a stable protein) and mutational effects $\Delta\Delta G_i$ that add,

$$
F = \frac{1}{1 + \mathrm{e}^{\Delta G/RT}}, \qquad \Delta G = \Delta G_{\mathrm{wt}} + \sum_i\Delta\Delta G_i. \tag{41.7}
$$
The landscape is additive in the biophysical variable $\Delta G$ and epistatic in fitness: a mutation's effect on fitness depends on the stability of the background.

Equation (41.7) explains several observations at once. Most random mutations destabilize, by about $1\,\mathrm{kcal\,mol^{-1}}$ on average with a broad spread (Tokuriki and colleagues 2007). A stable protein absorbs several of them with no change of fitness, because $F$ is flat for $\Delta G \ll -RT$; once its stability is used up, one more mutation inactivates it. Bershtein, Segal, Bekerman, Tokuriki and Tawfik (2006) observed this threshold robustness in TEM-1 drifting under purifying selection: the fraction of active variants fell faster than exponentially with the number of mutations, a signature of negative epistasis through stability. Bloom, Labthavikul, Otey and Arnold (2006) showed that a stabilized cytochrome P450 tolerated more of the destabilizing mutations needed for a new activity, so that stability promotes evolvability, the connection to robustness discussed in [7.6.40](/7.6.40#sec-40.5).

Combined with Theorem 41.3.1, the landscape predicts the stability of natural proteins. The number of sequences with stability $\Delta G$ increases steeply towards instability (there are far more ways to be unstable than to be stable), while fitness increases with stability only until it saturates. The stationary distribution, proportional to the number of sequences times $F^{N-1}$, therefore peaks where the last increments of stability no longer pay for the sequence entropy they cost: natural proteins are marginally stable, with $\Delta G$ of a few kilocalories per mole, not because marginal stability is optimal but because more stability is not worth the constraint (Taverna and Goldstein 2002; Zeldovich, Chen and Shakhnovich 2007). The same argument predicts that proteins of species with smaller effective populations are less stable, and that proteins expressed at high levels, where misfolding costs more, are more stable.

![A biophysical fitness landscape from folding stability. A: the fraction folded as a function of the folding free energy (Formula 41.4.1, RT = 0.6 kcal/mol): flat for stable proteins and steep near ΔG = 0. B: threshold robustness: fraction of 5000 simulated lineages still folded after accumulating random mutations with destabilizing effects drawn from a normal distribution (mean +1.0, standard deviation 1.7 kcal/mol), for proteins starting at ΔG = −3 and −8 kcal/mol; the stable protein tolerates several mutations before any are lost. C: stationary distributions of stability under mutation and selection (Theorem 41.3.1) for a protein of 100 sites, each either optimal or one of 19 suboptimal residues costing 1 kcal/mol, in populations of 10, 10³ and 10⁵: the entropy of sequence space pushes towards instability, selection towards stability, and the balance leaves proteins marginally stable, less so in larger populations](./plots/stability-fitness.py)

### 41.4.4. Regimes of Evolutionary Dynamics

The adaptive-walk picture assumes that beneficial mutations arise one at a time and fix before the next appears, which requires $N\mu_{\mathrm{b}}\ln(Ns) \ll 1$ for beneficial mutation rate $\mu_{\mathrm{b}}$ and **selection coefficient** $s$ (the time to fixation is about $\ln(Ns)/s$ generations, [7.4.23](/7.4.23#sec-23.3.1)). Large asexual populations of microbes violate it: several beneficial mutations arise in different lineages and compete, and only one can win (clonal interference, Gerrish and Lenski 1998). The rate of adaptation then grows only logarithmically with population size and mutation rate, and the mutations that fix have larger effects than those that would fix one at a time. In Lenski's long-term evolution experiment, the fitness of *E. coli* relative to its ancestor has increased for more than $75\,000$ generations, following a power law in time rather than approaching a plateau, a trajectory that models with clonal interference and diminishing-returns epistasis reproduce (Wiser, Ribeck and Lenski 2013). The quantitative theory of these regimes belongs to [7.10](/7.10).

## 41.5. Drug Resistance and Viral Evolution

### 41.5.1. Resistance Exists Before the Drug

Resistance to antibiotics and antivirals is evolution observed in the clinic and the laboratory. The Luria–Delbrück **fluctuation test** showed that resistant mutants arise spontaneously before the selective agent is applied, with a characteristic jackpot distribution ([7.4.12](/7.4.12#sec-12.4), [7.6.32](/7.6.32#sec-32.8.2)); resistance to an antibiotic typically appears at a rate of $10^{-6}$ to $10^{-9}$ per cell per generation, depending on how many mutations in the target confer it. Resistance then usually increases in steps. Selection of *Mycobacterium tuberculosis* on a low concentration of a fluoroquinolone gave mutants with one of three substitutions near the active site of DNA gyrase (A90V, S91P, D94H in GyrA) and two- to tenfold higher resistance; challenging these at higher concentrations selected secondary mutations with more than a hundredfold resistance. In a patient treated for a *Staphylococcus aureus* infection with a series of antibiotics, whole-genome sequencing of successive isolates over three months revealed $35$ mutations, including stepwise changes in genes associated with resistance to vancomycin and the other drugs used (Mwangi and colleagues 2007).

**Formula 41.5.1 (Pre-Existing Multiple Mutants)** In a population of $N$ replicating genomes in which each of $k$ specific mutations arises independently at rate $\mu$ per replication, the expected number of genomes carrying all $k$, generated in one round of replication, is approximately $N\mu^k$, and the probability that at least one exists is $1 - \mathrm{e}^{-N\mu^k}$.

### 41.5.2. Why Combination Therapy Works

**Example 41.5.1 (HIV and Triple Therapy)** An untreated HIV patient produces about $10^{10}$ virions per day ([7.6.1](/7.6.1#sec-1.6.5)), and reverse transcription makes about $3\times10^{-5}$ errors per base. Every possible single point mutation is therefore made about $10^{10}\times3\times10^{-5}/3 = 10^5$ times per day, and resistance to any single drug that one mutation confers exists before treatment begins: monotherapy with AZT or a protease inhibitor failed within weeks to months. A specific double mutant is made about $10^{10}\times(10^{-5})^2 = 1$ time per day, a specific triple mutant about $10^{-5}$ times per day. Combining three drugs, each requiring a different mutation, makes pre-existing resistance unlikely, and if the combination suppresses replication completely, new mutants cannot arise. This arithmetic, worked out by Perelson, Ho, Coffin and others in the 1990s, is why highly active antiretroviral therapy turned HIV infection into a chronic disease. The same logic applies to tuberculosis, treated with four drugs, and to cancer, where tumors of $10^9$–$10^{11}$ cells contain resistant variants to most single targeted drugs.

### 41.5.3. The Mutant Selection Window

A drug at a concentration that inhibits the sensitive strain but not a resistant mutant selects for the mutant. If resistance carries a fitness cost, as it often does, the mutant grows more slowly than the wild type without drug; above some concentration it grows faster, and above its own minimal inhibitory concentration it does not grow at all. Between the two lies the mutant selection window (Drlica and Zhao 2007), and treatments that keep the drug concentration within it for long periods favour resistance. In spatially varying drug concentrations, resistance can evolve stepwise through neighbouring regions of increasing concentration: Baym and colleagues (2016) filmed *E. coli* spreading across a large agar plate with bands of increasing antibiotic concentration, acquiring resistance to a thousandfold higher concentration within about ten days by a succession of mutations, each population colonizing the next band. Spatial gradients and fluctuating dosing open accessible paths on the landscape of resistance that would be closed in a uniform environment.

![The numbers of drug resistance. A: probability that a population already contains a variant with k specific mutations (Formula 41.5.1), for HIV (3 × 10⁻⁵ per base per replication; one, two or three mutations, solid) and for a bacterium with a target-specific resistance mutation rate of 10⁻⁸ (one or two mutations, dashed); shaded, the 10¹⁰ virions produced per day in an untreated patient and the 10⁹–10¹¹ bacteria of a large infection: single resistance mutations always pre-exist, combinations of three almost never. B: the mutant selection window: net growth rates against drug concentration for a sensitive strain and for a resistant mutant with an eightfold higher IC50 and a 10 % fitness cost (Hill coefficient 2, death rate 0.1 per hour); in the shaded range the drug favours the mutant](./plots/resistance.py)

### 41.5.4. Viruses at the Error Threshold

RNA viruses replicate with error rates near the inverse of their genome length: for HIV, about $0.3$ errors per genome per replication; for poliovirus, about one. Eigen's **error threshold** ([7.2.23](/7.2.23#thm-23.6.1)) states that a sequence of length $L$ copied with per-site error rate $\mu$ can be maintained by selection with superiority $\sigma$ only if $\mu L \lesssim \ln\sigma$; above it, the population loses the fittest sequence and spreads over sequence space. Viruses seem to live near this limit, which gives them maximal variability and, in principle, a vulnerability: raising their mutation rate further with a mutagenic nucleoside analogue should push them over the threshold. Crotty, Cameron and Andino (2001) showed that ribavirin increases the mutation rate of poliovirus and that its antiviral effect correlates with the extra mutations, a result called lethal mutagenesis; molnupiravir, used against SARS-CoV-2, acts by the same principle. The quantitative relation between mutation rate, population size and the loss of fitness (in finite populations, the gradual accumulation of deleterious mutations by drift, Muller's ratchet) is part of the theory of [7.10](/7.10).

The phylogenetic analysis of sequences from many hosts and times reconstructs the spread of epidemics and the evolution of viruses within patients: HIV diversifies within each patient under immune pressure, and the envelope sequences of a patient's virus a decade after infection differ from the founder by several percent. Phylogenies of all organisms, built from ribosomal RNA (Woese and Fox 1977) and from many genes, revealed the three domains of life and the extent of **horizontal gene transfer** among bacteria; their methods and results belong to [7.8](/7.8) and [7.10](/7.10).

## 41.6. Fidelity Across the Central Dogma

The rate at which sequences change is set by the fidelity of the machines that copy them, and that fidelity is a physical quantity, bought with free energy as discussed in [7.6.17](/7.6.17#sec-17.9) and [7.6.38](/7.6.38#sec-38.5.2).

| Process | Equilibrium discrimination (one step) | Observed error rate | Mechanisms beyond equilibrium |
|---|---|---|---|
| DNA replication (*E. coli*) | $\sim10^{-4}$–$10^{-5}$ (base pairing and geometric selection) | $\sim10^{-10}$ per bp | $3'\to5'$ exonuclease proofreading ($\sim10^{-2}$), mismatch repair ($\sim10^{-2}$–$10^{-3}$) |
| transcription | $\sim10^{-4}$ | $\sim10^{-5}$–$10^{-6}$ per nt | backtracking and cleavage |
| translation | $\sim10^{-2}$ (codon–anticodon) | $\sim10^{-4}$ per codon | kinetic proofreading by EF-Tu GTP hydrolysis, induced fit |
| tRNA charging | $\sim10^{-2}$–$10^{-3}$ for similar amino acids | $\sim10^{-4}$–$10^{-5}$ | editing sites (double sieve) |
| reverse transcription (HIV) | — | $\sim3\times10^{-5}$ per base | none (no proofreading) |

The pattern is that every error rate far below the equilibrium limit is achieved by an additional driven step, and that each step improves accuracy by roughly the equilibrium factor, in agreement with the theory of proofreading ([7.6.38](/7.6.38#sec-38.5.2)). The rates are not as low as physics would allow: they are compromises between the costs of errors, of time and of free energy, and, by the drift-barrier argument of 41.1.2, they are as low as selection in a population of a given size can make them. The rate of evolution, in turn, is set by these rates, so that the physics of molecular recognition in the copying machines reaches up to the tempo of evolution.

## Summary

- Sequences carry at most 2 bits per base; genomes, mutation rates and population sizes span many orders of magnitude (table in 41.1.2), with about $0.003$ mutations per genome per replication in DNA microbes (Drake's rule) and near one in RNA viruses.
- Comparing sequences: scores are log-likelihood ratios, minus interaction energies (Definition 41.2.1); the best score between random sequences grows as $\ln(mn)/\lambda$ with Gumbel statistics and $E = Kmn\mathrm{e}^{-\lambda S}$ (Theorem 41.2.1); divergence corrected for multiple hits, $d = -\frac{3}{4}\ln(1 - \frac{4}{3}p)$ (Formula 41.2.1), dates events by the **molecular clock** (HIV origin, Example 41.2.1) and reconstructs ancestral proteins (Example 41.2.2).
- Specificity: occupancy is a Fermi function of the site energy (Eq. (41.4)); the genome is a sea of decoys, a unique site needs $L > \log_4(2G)$, and mismatch energies of $2$–$3\,k_{\mathrm{B}}T$ are a compromise. Under weak mutation the stationary distribution of genotypes is $F^{N-1}$, a Boltzmann distribution with population size as inverse temperature (Theorem 41.3.1), which gives the Berg–von Hippel relation $\ln(f_b/f_{\mathrm{cons}}) = -\lambda\varepsilon_b$ (Corollary 41.3.1).
- Landscapes: epistasis of magnitude, sign and reciprocal sign; only the last creates multiple peaks (Definition 41.4.1); sign epistasis closes most mutational paths (Example 41.4.1, 102 of 120 for TEM-1); stability gives an additive-in-$\Delta G$, epistatic-in-fitness landscape (Formula 41.4.1), threshold robustness and marginal stability.
- Resistance: mutants pre-exist (Luria–Delbrück); the expected number of $k$-fold mutants is $N\mu^k$ (Formula 41.5.1), which explains combination therapy (Example 41.5.1); the mutant selection window and spatial gradients favour stepwise resistance; RNA viruses live near the error threshold, the basis of lethal mutagenesis.
- Fidelity of the copying machines (table in 41.6) is bought by driven proofreading steps and limited by the drift barrier.

## Questions

1. How many bits does the binding-site collection of a bacterial transcription factor need to specify $10$ sites in the *E. coli* genome, and how many base pairs is that at most?

   **Answer** The information needed is $\log_2(G/\gamma) = \log_2(4.6\times10^6/10) = \log_2(4.6\times10^5) = 18.8$ bits (Schneider's $R_{\mathrm{frequency}}$; counting both strands adds one bit). A perfectly conserved base carries $2$ bits, so at least about $9.4$–$10$ fully conserved positions are needed; real sites spread the information over more positions, typically $15$–$20$ bp, with partial conservation.

2. Two DNA sequences of $600$ sites differ at $210$. Estimate the number of substitutions per site that separate them. If the substitution rate is $10^{-9}$ per site per year in each lineage, when did they diverge?

   **Answer** $p = 0.35$; $d = -\frac{3}{4}\ln(1 - 4\times0.35/3) = -0.75\ln(0.5333) = 0.471$ substitutions per site (versus $0.35$ uncorrected). The divergence time is $t = d/(2\times10^{-9}) = 2.4\times10^8$ years, $235$ million years. The uncorrected estimate would have given $175$ million years.

3. Using Theorem 41.2.1 with $\lambda = \ln 3$ and $K \approx 0.1$, what score must an ungapped local alignment between a $300$-base query and a database of $10^9$ bases reach to have $E = 10^{-3}$?

   **Answer** $E = Kmn\mathrm{e}^{-\lambda S}$ gives $S = \ln(Kmn/E)/\lambda = \ln(0.1\times300\times10^9/10^{-3})/\ln 3 = \ln(3\times10^{13})/1.0986 = 31.0/1.0986 = 28.2$. A score of about $28$, for example $28$ more matches than mismatches in an ungapped stretch, is needed; the corresponding stretch at $70\,\%$ identity would be about $70$ bases long.

4. Show that the Moran fixation probability $\Pi = (1 - 1/r)/(1 - 1/r^N)$ reduces to $1/N$ for a neutral mutant and to about $1 - 1/r$ for a strongly beneficial one in a large population, and compute the stationary probability ratio, Eq. (41.5), between two genotypes differing in fitness by $1\,\%$ in populations of $100$ and $10^4$.

   **Answer** As $r \to 1$, write $r = 1 + s$: $1 - 1/r \approx s$ and $1 - 1/r^N \approx 1 - \mathrm{e}^{-Ns} \to Ns$ for small $Ns$, so $\Pi \to 1/N$. For $r > 1$ and $N \to \infty$, $r^{-N} \to 0$ and $\Pi \to 1 - 1/r \approx s$. The stationary ratio is $1.01^{N-1}$: $1.01^{99} = 2.7$ for $N = 100$ and $1.01^{9999} = \mathrm{e}^{99.5} \approx 10^{43}$ for $N = 10^4$. In small populations nearly neutral differences are tolerated; in large ones, the fitter genotype dominates absolutely.

5. Explain why a landscape of $L$ mutations without any sign epistasis has all $L!$ paths from the wild type to the full mutant accessible when the full mutant is fittest and each mutation is beneficial alone.

   **Answer** Without sign epistasis, every mutation has the same sign of effect in all backgrounds. If each mutation is beneficial alone, it is beneficial in every background, so adding any mutation at any step increases fitness, and every order of addition is an increasing path. Magnitude epistasis changes the step sizes, and hence the probabilities of the paths, but not their accessibility. This is the case $\sigma = 0$ of the rough Mount Fuji figure.

6. A protein has $\Delta G = -6\,\mathrm{kcal\,mol^{-1}}$. Mutations destabilize by $\Delta\Delta G \sim \mathcal{N}(1, 1.7^2)\,\mathrm{kcal\,mol^{-1}}$. Estimate how many random mutations it can accumulate before the probability of being unfolded ($\Delta G > 0$) exceeds one half, and explain why the effect of each mutation on fitness depends on the previous ones.

   **Answer** After $n$ mutations $\Delta G \sim \mathcal{N}(-6 + n, 1.7^2n)$; the probability that $\Delta G > 0$ is one half when the mean is zero, $n = 6$ (more precisely, the first-passage problem gives a similar number). The first few mutations barely change fitness because $F$ is flat for $\Delta G \ll 0$; later ones, from a background near $\Delta G = 0$, change it strongly. The same mutation is neutral in a stable background and deleterious in a marginal one: epistasis through the common biophysical variable, although $\Delta G$ itself is additive.

7. A bacterial infection contains $10^{10}$ cells. Resistance to drug A arises by any of $5$ point mutations, to drug B by any of $2$, each at $10^{-9}$ per cell per division. What is the probability that a cell resistant to both exists before treatment, if double mutants arise only by two independent mutations in the same lineage, and what does this imply for treatment with A and B together versus in sequence?

   **Answer** Rates: resistance to A $5\times10^{-9}$, to B $2\times10^{-9}$ per division. The expected number of doubly resistant cells made directly is about $N\mu_A\mu_B = 10^{10}\times10^{-17} = 10^{-7}$, plus the contribution of growing single-mutant clones (a Luria–Delbrück-type enhancement of order $\ln N$, still far below one): the probability is about $10^{-6}$. Given together, the drugs are very unlikely to meet pre-existing double resistance. Given in sequence, drug A selects one of the roughly $50$ A-resistant cells already present ($N\mu_A = 50$), which grows into a population of $10^{10}$ A-resistant cells, among which about $20$ will be B-resistant when drug B is started: sequential therapy turns a $10^{-6}$ risk into near certainty.

8. Why do RNA viruses not simply lower their mutation rate to escape the error threshold? Give two reasons, one physical and one evolutionary.

   **Answer** Physically, fidelity costs time and free energy and requires proofreading machinery: RNA-dependent RNA polymerases and **reverse transcriptases** lack an exonuclease domain, and adding one (as coronaviruses, with genomes of $30\,\mathrm{kb}$, have done with nsp14) requires a larger genome and slows replication. Evolutionarily, a high mutation rate supplies the variation that lets viruses escape immune responses and adapt to new hosts, and in large populations the deleterious load is partly compensated by the speed of replication; experiments with high-fidelity poliovirus mutants showed that they are attenuated in animals, losing the population diversity that helps them spread between tissues (Vignuzzi, Stone, Arnold, Cameron and Andino 2006).

9. (Design) You want to infer the energy matrix of a transcription factor from the sequences of its natural binding sites, using Corollary 41.3.1. Which assumptions might fail, and how would you test the inferred matrix?

   **Answer** Assumptions: sites evolved under selection on binding only (but some sites are under selection for weak binding, for regulation at a particular threshold, or for cooperative binding with other factors); positions are independent (but adjacent positions interact through DNA shape); fitness is exponential in energy over the relevant range (it may saturate at high occupancy, which flattens the matrix); the sites are a stationary sample (but they share ancestry, so their frequencies are not independent). Tests: measure binding of designed variants in vitro (gel shift, **fluorescence anisotropy**, SPR) or in high-throughput assays (Sort-Seq, protein-binding microarrays, SELEX) and compare energies with $-\ln(f_b/f_{\mathrm{cons}})$; check whether the proportionality constant is the same for all positions; predict occupancy of new sites in vivo with the **thermodynamic model** ([7.2.11](/7.2.11)) and compare with expression.

10. (Open question) Antibiotic resistance often carries a fitness cost, yet resistant strains persist long after an antibiotic is withdrawn. Using the concepts of this chapter, explain why.

    **Answer** Compensatory mutations: after resistance is acquired, second-site mutations that restore fitness without loss of resistance are often available (more targets than for reversion, which requires a specific back mutation), so the population climbs a new peak of the landscape rather than returning to the old one; reciprocal sign epistasis between the resistance mutation and its compensator then makes reversion deleterious in the compensated background. Linkage: resistance genes on plasmids are linked to other selected genes or to addiction systems that kill plasmid-free cells. Residual selection: low antibiotic concentrations in the environment, below the minimal inhibitory concentration of the sensitive strain, can still favour resistant cells (a minimal selective concentration far below the MIC). Population size and drift: once the resistant genotype is common, the cost must act over many generations to purge it, and the rate $\approx s$ per generation may be slow for costs of a percent.
