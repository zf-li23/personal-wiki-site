---
title: Codon Models and Adaptive Protein Evolution
description: "Estimating synonymous and nonsynonymous rates from protein-coding sequences: counting methods (Nei–Gojobori, the transition–transversion bias and codon usage), the Goldman–Yang and Muse–Gaut codon substitution models, definitions of dS and dN within a model and their maximum likelihood estimation, the interpretation of ω; branch models, random-site models (M1a/M2a, M7/M8) with likelihood ratio tests on the boundary of the parameter space, empirical Bayes identification of selected sites, the branch-site test; assumptions, sources of false positives and the classes of genes under positive selection."
---

The ratio $\omega = d_{\mathrm{N}}/d_{\mathrm{S}}$ of nonsynonymous to synonymous substitution rates is the most direct molecular signature of selection on proteins ([Definition 8.1.2](/7.10.8#def-8.1.2)): a value below 1 shows that amino acid changes are removed by **purifying selection**, a value above 1 that they have been fixed faster than neutral changes, which only **positive selection** explains. [7.10.8](/7.10.8#sec-8.1) introduced the idea and the simplest counting method. This chapter gives the statistical machinery behind it. It starts from the counting methods and why they disagree, replaces them by Markov models of codon substitution in which $\omega$ is a parameter ([7.10.20](/7.10.20) for Markov substitution models in general), and then lets $\omega$ vary among lineages and among sites, so that a few sites under positive selection along a few branches can be detected against the background of almost universal purifying selection. The models are fitted to alignments on a **phylogenetic tree** by the likelihood methods of [7.8.6](/7.8.6#sec-6.5) and [7.10.21](/7.10.21), and compared by **likelihood ratio tests** whose null distributions need care because the null value often lies on the boundary of the parameter space.

The results connect to several other chapters: positive selection in genes for immunity, reproduction and conflict with pathogens ([7.10.17](/7.10.17)), new functions after **gene duplication** ([7.10.18](/7.10.18)), the population-genetic tests of [7.10.8](/7.10.8#sec-8.2), which detect selection on a different time scale, and the $d_{\mathrm{N}}/d_{\mathrm{S}}$ of somatic mutations in tumors ([7.9.13](/7.9.13#sec-13.4.2)).

## 23.1. Counting Synonymous and Nonsynonymous Change

### 23.1.1. The Problem

Because of the redundancy of the **genetic code** ([7.2.19](/7.2.19)), a **synonymous substitution** at a codon leaves the protein unchanged, while a **nonsynonymous substitution** changes it ([Definition 8.1.1](/7.10.8#def-8.1.1)). If synonymous changes are taken as the benchmark of what would happen without selection on the protein, comparing the two kinds of change measures that selection. The comparison must be made per opportunity: a typical protein-coding sequence offers about three times as many nonsynonymous as synonymous mutations, so raw counts of differences are meaningless. The distances $d_{\mathrm{S}}$ and $d_{\mathrm{N}}$ are therefore defined as numbers of substitutions per synonymous site and per nonsynonymous site, and all methods for estimating them have to solve three problems: how many sites of each kind a sequence has, how the observed differences divide into the two kinds, and how to correct for multiple substitutions at the same site.

### 23.1.2. The Nei–Gojobori Method

**Definition 23.1.1 (Nei–Gojobori Method)** The **Nei–Gojobori method** (NG86; Nei and Gojobori 1986, a simplification of Miyata and Yasunaga 1980) estimates $d_{\mathrm{S}}$ and $d_{\mathrm{N}}$ between two aligned protein-coding sequences of $L_{\mathrm{c}}$ codons in three steps.

1. *Sites.* Each codon has three nucleotide sites. For each codon position, a fraction $f$ of the site is counted as synonymous if a fraction $f$ of the three possible point mutations at that position is synonymous (mutations to stop codons are ignored). Summing over codons and averaging over the two sequences gives $S$ synonymous and $N$ nonsynonymous sites, $S + N = 3L_{\mathrm{c}}$.
2. *Differences.* Codons that differ at one position contribute one synonymous or one nonsynonymous difference. Codons that differ at two or three positions are connected by two or six mutational pathways through intermediate codons (pathways through stop codons excluded), and their differences are averaged over the pathways with equal weights. Summing gives $S_{\mathrm{d}}$ synonymous and $N_{\mathrm{d}}$ nonsynonymous differences.
3. *Correction.* The proportions $p_{\mathrm{S}} = S_{\mathrm{d}}/S$ and $p_{\mathrm{N}} = N_{\mathrm{d}}/N$ are corrected for multiple hits with the Jukes–Cantor formula,

$$
d_{\mathrm{S}} = -\frac34\ln\Bigl(1 - \frac43p_{\mathrm{S}}\Bigr), \qquad d_{\mathrm{N}} = -\frac34\ln\Bigl(1 - \frac43p_{\mathrm{N}}\Bigr). \tag{23.1}
$$

**Example 23.1.1** The codon TTT (Phe) has nine single-mutation neighbors: TTC (Phe), TTA and TTG (Leu), TCT (Ser), TAT (Tyr), TGT (Cys), CTT (Leu), ATT (Ile) and GTT (Val). Only TTC is synonymous, so TTT has $3 \times 1/9 = 1/3$ synonymous and $8/3$ nonsynonymous sites. The codons CCT (Pro) and CAG (Gln) differ at two positions; the pathway through CAT (His) involves two nonsynonymous changes, the pathway through CCG (Pro) one synonymous and one nonsynonymous change, so with equal weights the pair contributes $0.5$ synonymous and $1.5$ nonsynonymous differences.

**Example 23.1.2 (The *rbcL* Genes of Cucumber and Tobacco)** The chloroplast gene *rbcL*, encoding the large subunit of rubisco, was compared between cucumber (*Cucumis sativus*) and tobacco (*Nicotiana tabacum*); after removal of gaps, 472 codons remain. Of these, 345 are identical, 115 differ at one position (95 synonymously, 20 nonsynonymously), 10 at two positions and 2 at all three. NG86 partitions the 1416 sites into $S = 343.5$ and $N = 1072.5$ and the 141 differences into $S_{\mathrm{d}} = 103.0$ and $N_{\mathrm{d}} = 38.0$. Then $p_{\mathrm{S}} = 0.300$, $p_{\mathrm{N}} = 0.035$, and Eq. (23.1) gives $d_{\mathrm{S}} = 0.383$, $d_{\mathrm{N}} = 0.036$ and $\omega = 0.095$: a nonsynonymous mutation has had less than a tenth of the chance of a synonymous one of being fixed, the strong constraint expected for an essential enzyme (data and estimates from Yang 2014).

The JC69 correction is logically imperfect, since a synonymous site cannot change to three other nucleotides synonymously, but at low divergence the correction is small and so is its error.

### 23.1.3. Transition Bias and Codon Usage

NG86 assumes, in effect, that all point mutations are equally likely. Two features of real sequences violate this and bias the counts of sites.

- *Transition–transversion bias.* Transitions occur at a higher rate than transversions (the **transition/transversion rate ratio** $\kappa$ is often 2–10 per site), and at third codon positions transitions are much more often synonymous than transversions. Counting sites as if $\kappa = 1$ underestimates $S$, overestimates $d_{\mathrm{S}}$ and underestimates $\omega$ (Li, Wu and Luo 1985).
- *Unequal codon usage.* Codon frequencies are unequal (**codon usage bias**, [7.10.8](/7.10.8#sec-8.1.2)), which means that substitution rates are not symmetric: rates towards common codons are higher. Ignoring it usually has the opposite effect, overestimating $S$ and $\omega$ (Yang and Nielsen 2000).

The method of Li, Wu and Luo (LWL85) classifies each codon position as nondegenerate (all changes nonsynonymous), twofold degenerate (one change, a transition, synonymous) or fourfold degenerate (all changes synonymous; the third position of the isoleucine codons, which is threefold degenerate, is treated as twofold), with $L_0$, $L_2$ and $L_4$ sites in the three classes, and estimates the transitional and transversional distances $A_i$ and $B_i$ in each class with the K80 formula ([Formula 6.2.1](/7.8.6#fml-6.2.1)). Counting a twofold site as $1/3$ synonymous,

$$
d_{\mathrm{S}} = \frac{L_2A_2 + L_4(A_4 + B_4)}{L_2/3 + L_4}, \qquad d_{\mathrm{N}} = \frac{L_2B_2 + L_0(A_0 + B_0)}{2L_2/3 + L_0}. \tag{23.2}
$$

Later refinements replace the fraction $1/3$ by an estimate from the fourfold sites (Li 1993; Pamilo and Bianchi 1993, LPB93), or weight each of the nine mutations of a codon by its rate when counting sites (Ina 1995): with $\kappa = 2$, the three transitions from TTT (to TTC, TCT and CTT) each count twice, so TTT has $3 \times 2/12 = 1/2$ synonymous sites instead of $1/3$. Yang and Nielsen (2000; YN00) accommodate both the transition bias and unequal codon frequencies by an iterative counting procedure that approximates the likelihood method of §23.2.

![Synonymous sites and estimates of ω for the *rbcL* genes of cucumber and tobacco. A: proportion of synonymous sites S/(S + N) in the universal genetic code with equal codon frequencies, as a function of the transition/transversion rate ratio κ, computed by weighting each mutation of each codon by its rate; it rises from 0.255 at κ = 1 to 0.287 at κ = 2.59, so ignoring transition bias undercounts synonymous sites. B: the estimate of ω from the same pair of genes by six counting methods (orange) and by maximum likelihood under codon models with different assumptions about κ and codon frequencies (blue), from Yang (2014), Table 2.8. The estimates differ almost twofold, more because of their assumptions than because of the estimation method](./plots/sites.py)

The *rbcL* comparison shows how much the assumptions matter (figure above). LWL85 gives $S = 321.2$, $d_{\mathrm{S}} = 0.385$, $d_{\mathrm{N}} = 0.039$ and $\omega = 0.101$; LPB93 gives $\omega = 0.129$; YN00, which also allows for the strongly AT-rich third positions of this chloroplast gene, gives $S = 308.4$, $d_{\mathrm{S}} = 0.498$ and $\omega = 0.071$. Codon bias here counteracts the transition bias, and the method that ignores both (NG86) is closer to YN00 than the methods that correct for only one. Two general conclusions follow (Yang 2014): different methods give very different estimates even for similar sequences, because they count sites differently, unlike nucleotide distances, which agree at low divergence; and the assumptions matter more than the method, since counting and likelihood methods under the same assumptions give similar results.

## 23.2. Codon Substitution Models

### 23.2.1. The Rate Matrix

Instead of correcting counts, one can model substitution between codons directly as a **continuous-time Markov chain** whose states are the 61 sense codons of the universal code (60 in the vertebrate mitochondrial code); stop codons are excluded because they do not occur inside functional genes.

**Definition 23.2.1 (Codon Model)** A **codon model** (Goldman and Yang 1994; Muse and Gaut 1994) is a **substitution model** whose states are the sense codons. In the form in common use (Goldman and Yang 1994, simplified by Nielsen and Yang 1998), the instantaneous rate from codon $I$ to codon $J \neq I$ is

$$
q_{IJ} = \begin{cases}
0, & I \text{ and } J \text{ differ at two or three positions},\\
\pi_J, & \text{synonymous transversion},\\
\kappa\pi_J, & \text{synonymous transition},\\
\omega\pi_J, & \text{nonsynonymous transversion},\\
\omega\kappa\pi_J, & \text{nonsynonymous transition},
\end{cases} \tag{23.3}
$$

where $\pi_J$ is the equilibrium frequency of codon $J$, $\kappa$ the transition/transversion rate ratio and $\omega$ the nonsynonymous/synonymous rate ratio. The codon frequencies are equal (Fequal), products of four nucleotide frequencies (F1×4, 3 free parameters), products of position-specific nucleotide frequencies (F3×4, 9 parameters), or free (F61, 60 parameters).

The parameters $\kappa$ and $\pi_J$ describe processes at the DNA level (mutation bias and any selection on the DNA), while $\omega$ describes selection on the protein: $\omega = 1$ means that nonsynonymous mutations are fixed at the same rate as synonymous ones, $\omega < 1$ that most are removed by purifying selection, $\omega > 1$ that they are fixed faster, by positive selection. Because $q_{IJ}$ is a symmetric factor times $\pi_J$, the chain satisfies detailed balance, $\pi_Iq_{IJ} = \pi_Jq_{JI}$, and has **time reversibility** ([7.10.20](/7.10.20)). Changes at two or three positions have rate zero instantaneously but positive probability over any finite time, $P(t) = \mathrm{e}^{Qt}$, computed numerically for the $61 \times 61$ matrix.

In the Muse–Gaut model the rate to the target codon is proportional to the frequency $\pi^*_{j_k}$ of the target nucleotide at the changed position $k$, rather than to the codon frequency; it is also reversible, with $\pi_J \propto \pi^*_{j_1}\pi^*_{j_2}\pi^*_{j_3}$. A mutation–selection version (FMutSel; Yang and Nielsen 2008) writes the rate as a mutation rate times a **fixation probability** ([Theorem 6.3.1](/7.10.6#thm-6.3.1)): if codon $I$ has scaled fitness $F_I = 2N_{\mathrm{e}}f_I$, then $2N_{\mathrm{e}}s_{IJ} = F_J - F_I$ and

$$
q_{IJ} = a_{i_kj_k}\pi^*_{j_k}\,\frac{F_J - F_I}{1 - \mathrm{e}^{F_I - F_J}} \quad (\times\,\omega \text{ if nonsynonymous}), \tag{23.4}
$$

with $a_{ij}$ symmetric (for example $\kappa$ for transitions and 1 for transversions); its stationary distribution $\pi_J \propto \pi^*_{j_1}\pi^*_{j_2}\pi^*_{j_3}\mathrm{e}^{F_J}$ separates mutation bias from selection on codon usage, the same balance as Eq. (8.1). Further extensions let $\omega$ depend on the physicochemical distance between amino acids, or estimate empirical codon matrices from many alignments; they fit better but are harder to interpret.

### 23.2.2. Synonymous and Nonsynonymous Rates within the Model

The model has no "sites" or "differences"; $d_{\mathrm{S}}$ and $d_{\mathrm{N}}$ are defined from its rates.

**Definition 23.2.2 (Synonymous and Nonsynonymous Substitution Rates)** Let $Q$ be scaled so that one nucleotide substitution is expected per codon per time unit, $-\sum_I\pi_Iq_{II} = 1$, and let $t$ be the distance between two sequences in substitutions per codon. Let $\rho_{\mathrm{S}} = \sum_{I \neq J,\ \text{syn}}\pi_Iq_{IJ}$ and $\rho_{\mathrm{N}} = \sum_{I \neq J,\ \text{nonsyn}}\pi_Iq_{IJ}$ be the proportions of synonymous and nonsynonymous substitutions ($\rho_{\mathrm{S}} + \rho_{\mathrm{N}} = 1$), and $\rho^{(1)}_{\mathrm{S}}$, $\rho^{(1)}_{\mathrm{N}}$ the same proportions computed with $\omega = 1$ (normalized to sum to 1), the proportions of synonymous and nonsynonymous mutations. The numbers of synonymous and nonsynonymous sites per codon are $S = 3\rho^{(1)}_{\mathrm{S}}$ and $N = 3\rho^{(1)}_{\mathrm{N}}$, and the **synonymous substitution rate** and **nonsynonymous substitution rate** (distances) are

$$
d_{\mathrm{S}} = \frac{t\rho_{\mathrm{S}}}{3\rho^{(1)}_{\mathrm{S}}}, \qquad d_{\mathrm{N}} = \frac{t\rho_{\mathrm{N}}}{3\rho^{(1)}_{\mathrm{N}}}. \tag{23.5}
$$

Sites are thus counted as mutational opportunities under the DNA-level process (transition bias and codon frequencies included), before selection on the protein acts.

**Theorem 23.2.1 (The Ratio of the Distances Is ω)** Under the model of Eq. (23.3), $d_{\mathrm{N}}/d_{\mathrm{S}} = \omega$, and $t = Sd_{\mathrm{S}} + Nd_{\mathrm{N}}$.

**Proof** Let $q^{(1)}_{IJ}$ be the rates with $\omega = 1$. Every nonsynonymous rate equals $\omega q^{(1)}_{IJ}$ and every synonymous rate equals $q^{(1)}_{IJ}$, so with $A = \sum_{\text{nonsyn}}\pi_Iq^{(1)}_{IJ}$ and $B = \sum_{\text{syn}}\pi_Iq^{(1)}_{IJ}$ we have $\rho_{\mathrm{N}}/\rho_{\mathrm{S}} = \omega A/B$ and $\rho^{(1)}_{\mathrm{N}}/\rho^{(1)}_{\mathrm{S}} = A/B$. Dividing the two expressions of Eq. (23.5), $d_{\mathrm{N}}/d_{\mathrm{S}} = (\rho_{\mathrm{N}}/\rho_{\mathrm{S}})/(\rho^{(1)}_{\mathrm{N}}/\rho^{(1)}_{\mathrm{S}}) = \omega$. Finally $Sd_{\mathrm{S}} + Nd_{\mathrm{N}} = t\rho_{\mathrm{S}} + t\rho_{\mathrm{N}} = t$. $\square$

The theorem shows what $\omega$ measures: a ratio of two ratios, the proportion of nonsynonymous among the substitutions that occurred relative to the proportion expected if the protein were under no selection. In particular, $d_{\mathrm{S}}$ is the average substitution rate of the three codon positions before selection on the protein, whatever drives evolution at synonymous sites. The common belief that the test requires neutral synonymous sites is mistaken: if selection on codon usage slows synonymous change, it slows the "before selection" rate of nonsynonymous change in the same way, and $\omega$ still measures selection on the amino acid sequence (Yang 2014).

### 23.2.3. Maximum Likelihood Estimation

For two sequences, the probability of a pair of codons $(x, y)$ at a site is $\pi_xp_{xy}(t)$ (by reversibility the root can be placed at either sequence), and the log likelihood is the sum over codon sites,

$$
\ell(t, \kappa, \omega) = \sum_{h = 1}^{L_{\mathrm{c}}}\ln\bigl[\pi_{x_h}p_{x_hy_h}(t; \kappa, \omega)\bigr], \tag{23.6}
$$

with codon frequencies usually set to their observed values. It is maximized numerically, and the estimates of $d_{\mathrm{S}}$ and $d_{\mathrm{N}}$ follow from Eq. (23.5) by the invariance of maximum likelihood estimates; their variances follow from the **delta method**. For many sequences, the same rate matrix is used on every branch of the tree and the likelihood is computed by **Felsenstein's pruning algorithm** ([7.8.6](/7.8.6#sec-6.5.1)).

![Maximum likelihood estimation from two coding sequences under the codon model of Eq. (23.3) (simulation). Two sequences of 400 codons descend from a common ancestor drawn from the stationary distribution (F3×4 frequencies of an AT-rich gene), separated by a total distance t = 0.6 substitutions per codon, with κ = 2.5 and ω = 0.2. A: the log likelihood surface in (t, ω) with κ fixed at its true value; contours 2, 5, 10, 20 and 50 units below the maximum; cross: maximum likelihood estimate; dot: true values. The two parameters are nearly uncorrelated because t is determined mostly by the synonymous and ω by the nonsynonymous differences. B: the profile log likelihood of ω (t and κ maximized); the approximate 95 % interval, where the curve lies within 1.92 of the maximum, contains the true value 0.2](./plots/likelihood.py)

**Example 23.2.1** For the *rbcL* genes of Example 23.1.2 (Yang 2014, Table 2.8):

| model | $\hat\kappa$ | $S$ | $\hat d_{\mathrm{S}}$ | $\hat d_{\mathrm{N}}$ | $\hat\omega$ | $\ell$ |
|---|---|---|---|---|---|---|
| Fequal, $\kappa = 1$ | 1 | 360.7 | 0.371 | 0.036 | 0.096 | $-2466.33$ |
| Fequal, $\kappa$ estimated | 2.59 | 407.1 | 0.322 | 0.037 | 0.117 | $-2454.26$ |
| F3×4, $\kappa$ estimated | 3.13 | 331.0 | 0.455 | 0.036 | 0.078 | $-2371.86$ |
| F61, $\kappa$ estimated | 2.86 | 307.4 | 0.473 | 0.035 | 0.074 | $-2304.47$ |

The first model is the model underlying NG86, and its estimates are close to those of NG86 ($\hat t = 0.363$ substitutions per codon, or 171.4 over the gene, against 141 observed differences). Estimating $\kappa$ improves the log likelihood by 12.07, so $2\Delta\ell = 24.1$ against $\chi^2_1$ rejects $\kappa = 1$ decisively; it changes $S$ much more than the numbers of substitutions, and because $S$ is the smaller count, $d_{\mathrm{S}}$ and $\omega$ change most. Allowing unequal codon frequencies improves the fit far more and moves $\omega$ in the other direction.

:::

The likelihood approach has two advantages over counting. Conceptually, only the instantaneous rates have to be specified; at that level there are no multiple changes in a codon, every change is clearly synonymous or not, and the weighting of pathways, the correction for multiple hits and the irregularities of the code are handled by the probability calculus. Practically, more realistic models (a GTR mutation process, variable $\omega$) are easy to add.

### 23.2.4. Interpreting ω in Comparative Genomics

In 857 orthologous genes, the median estimates of $d_{\mathrm{N}}$, $d_{\mathrm{S}}$ and $\omega$ are 0.005, 0.030 and 0.149 between human and orangutan and 0.019, 0.195 and 0.101 between mouse and rat (dos Reis and colleagues 2012). The two pairs diverged at similar times, so the rodent genes evolve much faster per year, as the generation-time effect predicts ([7.10.6](/7.10.6#sec-6.6.2)), and their lower $\omega$ fits the **nearly neutral theory**: rodents have larger effective sizes, so purifying selection removes slightly deleterious amino acid changes more efficiently.

Two limits of divergence restrict the use of $\omega$. When sequences are too divergent, synonymous sites are saturated and $d_{\mathrm{S}}$ cannot be estimated (estimates above about 3 are unreliable); the remedy is to add species and estimate many short branches on a tree. When sequences are too similar, as for individuals of one species or closely related bacterial strains, there is little information, and the ratio changes meaning: slightly deleterious nonsynonymous mutations segregate for some time before they are lost, so $\omega$ estimated from polymorphism or from recently separated sequences is inflated relative to that of fixed differences, and it decreases with the time since divergence (Rocha and colleagues 2006; Kryazhimskiy and Plotkin 2008). Within a population, $\omega$ is therefore not a test of positive selection; the population-genetic methods of [7.10.8](/7.10.8#sec-8.2) are needed. The ratio of somatic mutations in tumors ([7.9.13](/7.9.13#sec-13.4.2)) uses mutations rather than substitutions and is interpreted in the same spirit, as the excess or deficit of nonsynonymous mutations among those retained in the tumor.

## 23.3. Lineages under Positive Selection: Branch Models

An $\omega$ averaged over the whole history of two sequences is dominated by the long periods of purifying selection; adaptive episodes are more visible if attention is restricted to particular branches. The classical study is of lysozyme in primates (Messier and Stewart 1997): reconstructing the ancestral sequences ([7.10.21](/7.10.21)) and counting changes branch by branch, they found $d_{\mathrm{N}} > d_{\mathrm{S}}$ on the branch ancestral to the leaf-eating colobine monkeys, in which lysozyme acquired a digestive function in the foregut ([7.10.8](/7.10.8#sec-8.1.1)). Such methods treat inferred ancestral sequences as data and do not correct properly for multiple hits; the likelihood approach averages over ancestral states instead.

**Definition 23.3.1 (Branch Model)** A **branch model** (Yang 1998) is a codon model on a phylogeny in which the ratio $\omega$ differs among branches according to a specification made in advance: one ratio for all branches (model M0), a separate ratio for each branch (free-ratio model), or a few ratios, typically $\omega_1$ for the *foreground* branches of interest and $\omega_0$ for all other (*background*) branches. Nested branch models are compared by likelihood ratio tests; positive selection on the foreground is tested by comparing the model with $\omega_1$ free against the same model with $\omega_1 = 1$.

The likelihood is computed exactly as for M0, except that the transition probabilities of each branch are computed from the rate matrix with that branch's $\omega$. In the gene *ASPM*, a determinant of brain size, a model with separate ratios for the human, chimpanzee and orangutan branches gave $\hat\omega_{\mathrm{H}} = 1.03$, $\hat\omega_{\mathrm{C}} = 0.66$ and $\hat\omega_{\mathrm{O}} = 0.43$ (Zhang 2003), compared with M0 by a test with 2 degrees of freedom.

Two cautions apply. The foreground must be chosen before looking at the data: choosing the branches with the highest estimated ratios and then testing them is a hidden **multiple comparisons** problem, which invalidates the null distribution. And variation of $\omega$ among branches, or $\omega_1 > \omega_0$ without $\omega_1 > 1$, violates strict neutrality but is not evidence of adaptation: relaxation of purifying selection after loss of function, or less efficient purifying selection in a lineage with a small **effective population size**, produce the same pattern. The requirement that $\omega$ averaged over all sites exceed 1 is stringent, and branch tests have little power when most sites are constrained.

## 23.4. Sites under Positive Selection: Site Models

### 23.4.1. Random-Site Models

Most proteins have a core of highly conserved residues with $\omega$ near zero and a few positions that change freely. Positive selection should therefore be sought at individual sites. When structural information identifies candidate sites in advance, they can be analyzed separately: in the human major histocompatibility complex (MHC) class I genes, $\omega$ for the whole gene is below 1, but for the 57 residues that form the antigen recognition site, identified from the crystal structure, it is significantly above 1 (Hughes and Nei 1988). Estimating a separate $\omega$ for every site is possible but has as many parameters as sites. The standard solution treats $\omega$ as a random variable across sites.

**Definition 23.4.1 (Site Model)** A **site model** (random-site model; Nielsen and Yang 1998; Yang and colleagues 2000) is a codon model in which the synonymous rate is the same at all sites while the ratio $\omega$ of each site is drawn independently from a distribution $f(\omega)$ with a few parameters, the same on all branches. The probability of the data $x_h$ at codon site $h$ is the mixture

$$
f(x_h) = \int_0^\infty f(\omega)f(x_h \mid \omega)\,\mathrm{d}\omega \approx \sum_{k = 1}^Kp_kf(x_h \mid \omega_k), \tag{23.7}
$$

a **finite mixture model** over site classes $k$ with proportions $p_k$ and ratios $\omega_k$; continuous distributions are approximated by $K = 10$ equally probable classes, as in the **discrete gamma model** of rate variation.

The models in common use are:

| model | parameters of $f(\omega)$ | $\omega > 1$ allowed |
|---|---|---|
| M0 (one ratio) | $\omega$ | yes, at all sites |
| M1a (nearly neutral) | $p_0$; $0 < \omega_0 < 1$, $\omega_1 = 1$ | no |
| M2a (positive selection) | $p_0, p_1$; $0 < \omega_0 < 1$, $\omega_1 = 1$, $\omega_2 > 1$ | yes |
| M3 (discrete) | $p_0, p_1$; $\omega_0, \omega_1, \omega_2$ free | yes |
| M7 (beta) | $\omega \sim \mathrm{Beta}(p, q)$ on $(0, 1)$ | no |
| M8 (beta & $\omega$) | $p_0$; $\mathrm{Beta}(p, q)$; $\omega_s > 1$ | yes |

The rate matrices of all classes are scaled by one common factor, so that the synonymous rate is the same in all classes and only the nonsynonymous rate varies. Two pairs of nested models are used to test for positive selection: M1a against M2a and M7 against M8. Comparing M0 with M3 tests variation of $\omega$ among sites, not positive selection. The class with $\omega_1 = 1$ in M1a, which absorbs sites under weak constraint, is what keeps the M1a–M2a test from mistaking relaxed constraint for selection.

### 23.4.2. Likelihood Ratio Tests on the Boundary

Wilks' theorem ([Theorem 5.3.1](/3.2.5#thm-5.3.1)), which gives $2\Delta\ell \xrightarrow{d} \chi^2_k$, requires the null value to lie in the interior of the parameter space. In the tests of positive selection it does not: M1a is M2a with $p_2 = 0$, a boundary value, and when $p_2 = 0$ the parameter $\omega_2$ does not appear in the likelihood at all.

**Theorem 23.4.1 (Likelihood Ratio Test on a Boundary)** Suppose that under the alternative a single parameter $\psi$ is restricted to $\psi \ge \psi_0$, the null hypothesis is $\psi = \psi_0$, all other parameters are interior and identifiable, and the usual regularity conditions hold. Then under the null hypothesis

$$
2\Delta\ell \xrightarrow{d} \tfrac12\chi^2_0 + \tfrac12\chi^2_1,
$$

the 1:1 mixture of a point mass at 0 and $\chi^2_1$ (Chernoff 1954; Self and Liang 1987). The 5 % and 1 % critical values are 2.71 and 5.41, instead of 3.84 and 6.63.

**Proof** (sketch, for a normal mean.) Locally the log likelihood is quadratic, so the problem is asymptotically that of a single observation $Z \sim \mathcal{N}(\psi - \psi_0, 1)$ (after standardization) with $\psi \ge \psi_0$. Under the null, $Z \sim \mathcal{N}(0, 1)$; the constrained estimate is $\max(Z, 0)$ and $2\Delta\ell = \max(Z, 0)^2$. This is 0 with probability $1/2$ and equals $Z^2 \sim \chi^2_1$ on the event $Z > 0$, which has probability $1/2$. $\square$

![The likelihood ratio test when the null value lies on the boundary of the parameter space. Data: 50 observations from N(μ, 1); H₀: μ = 0 against H₁: μ ≥ 0, so that 2Δℓ = 50 max(x̄, 0)². A: distribution of 2Δℓ over 20 000 data sets simulated under H₀: half are exactly 0 (orange bar, its height is the probability), the rest follow the density of ½χ²₁ (line). B: tail probabilities P(2Δℓ > c) from the simulation (dots) compared with the 1:1 mixture of 0 and χ²₁, with χ²₁ and with χ²₂; the 5 % critical values are 2.71, 3.84 and 5.99. Using χ²₁ or χ²₂ in place of the mixture gives a conservative test](./plots/boundary.py)

For M1a against M2a and for M7 against M8 the situation is worse than in the theorem, because $\omega_2$ (or $\omega_s$) is not identifiable under the null, and the exact null distribution is unknown. In practice $\chi^2_2$ is used; simulations show that it is conservative (Anisimova and colleagues 2001), which is acceptable for a test whose false positives are more damaging than its false negatives.

### 23.4.3. Which Sites? Empirical Bayes

When the test indicates sites with $\omega > 1$, the posterior probability that site $h$ belongs to class $k$ follows from Bayes' theorem,

$$
\mathbb{P}(\omega_h = \omega_k \mid x_h) = \frac{p_kf(x_h \mid \omega_k)}{\sum_jp_jf(x_h \mid \omega_j)}, \tag{23.8}
$$

the same calculation as for the rate class of a site under the gamma model. Sites with a high posterior probability (say above 0.95) for the class $\omega > 1$ are inferred to be under positive selection. Replacing the parameters by their maximum likelihood estimates is naive **empirical Bayes** (NEB), which ignores their sampling error and can be unreliable in small data sets; Bayes empirical Bayes (BEB; Yang, Wong and Nielsen 2005) integrates over the uncertainty in the parameters of $f(\omega)$ with a prior, keeping branch lengths at their estimates, and a fully Bayesian version averages over everything by MCMC (Huelsenbeck and Dyer 2004). The approach can detect selected sites even when $\omega$ averaged over the protein is far below 1.

![Empirical Bayes identification of sites under positive selection, Eq. (23.8), in a simplified model in which the data at codon site h are the number of nonsynonymous changes over the tree, Poisson with mean ω_h λ_N, where λ_N is the expected number of nonsynonymous changes per site at ω = 1; synonymous changes do not depend on the class and cancel from the posterior. Sites belong to three classes: ω = 0.05 (75 %), ω = 1 (15 %) and ω = 4 (10 %). A: the posterior probability of the class ω = 4 at each of 200 simulated sites with λ_N = 1.5 (bars), computed with the true parameters; red ticks mark the sites truly in that class; dashed: the cutoff 0.95. Many truly selected sites do not reach the cutoff, but almost all sites that do are truly selected. B: as the tree becomes longer (more sequences or more divergence), the proportion of selected sites detected at P > 0.95 increases, while the proportion of detections that are false stays low (means over 200 simulated proteins)](./plots/empirical-bayes.py)

**Example 23.4.1 (Class I MHC)** An alignment of 192 alleles of the human class I MHC loci A, B and C, 270 codons long, was analyzed with branch lengths fixed at their M0 estimates (Yang and Swanson 2002; Yang and colleagues 2005):

| model | $\ell$ | estimates |
|---|---|---|
| M0 | $-8225.15$ | $\hat\omega = 0.612$ |
| M1a | $-7490.99$ | $\hat p_0 = 0.830$, $\hat\omega_0 = 0.041$ ($\omega_1 = 1$) |
| M2a | $-7231.15$ | $\hat p_0 = 0.776$, $\hat p_1 = 0.140$, $\hat p_2 = 0.084$; $\hat\omega_0 = 0.058$, $\hat\omega_2 = 5.39$ |
| M7 | $-7502.79$ | $\hat p = 0.087$, $\hat q = 0.360$ |
| M8 | $-7238.01$ | $\hat p_0 = 0.915$, $\hat p = 0.167$, $\hat q = 0.717$; $\hat\omega_s = 5.08$ |

The whole-gene ratio is below 1, but M2a puts about $8\,\%$ of the sites in a class with $\omega \approx 5.4$; $2\Delta\ell = 2(7490.99 - 7231.15) = 519.7$ for M1a against M2a and $529.6$ for M7 against M8, far beyond any critical value. The 24 sites with posterior probability above $0.95$ under M2a are scattered along the primary sequence but clustered in the three-dimensional structure: most are among the 57 residues of the antigen recognition site identified independently from the crystal structure, and the others lie in the same region; M8 identifies nearly the same sites. The cleft that binds **antigen** peptides is where selection to recognize a diversity of foreign peptides acts.

## 23.5. Sites and Lineages Together: the Branch-Site Test

Branch tests average $\omega$ over sites, site tests average it over branches. The site test works well for genes in perpetual arms races, where the same sites are under selection throughout the tree, but most adaptive episodes are expected to affect a few sites on a few branches.

**Definition 23.5.1 (Branch-Site Test)** In the **branch-site test** (Yang and Nielsen 2002, modified by Zhang, Nielsen and Yang 2005), the branches are divided in advance into foreground and background, and the sites into four classes:

| site class | proportion | background $\omega$ | foreground $\omega$ |
|---|---|---|---|
| 0 | $p_0$ | $0 < \omega_0 < 1$ | $\omega_0$ |
| 1 | $p_1$ | $\omega_1 = 1$ | $1$ |
| 2a | $(1 - p_0 - p_1)p_0/(p_0 + p_1)$ | $\omega_0$ | $\omega_2 \ge 1$ |
| 2b | $(1 - p_0 - p_1)p_1/(p_0 + p_1)$ | $1$ | $\omega_2 \ge 1$ |

The alternative hypothesis (branch-site model A) estimates $p_0, p_1, \omega_0, \omega_2$; the null hypothesis is the same model with $\omega_2 = 1$. Because $\omega_2 = 1$ is on the boundary, the null distribution of $2\Delta\ell$ is the 1:1 mixture of 0 and $\chi^2_1$ (Theorem 23.4.1); $\chi^2_1$ is often used to be conservative.

The probability of the data at a site is again a mixture, Eq. (23.7), over the four classes; classes 0 and 1 evolve under M0 with the corresponding ratio, classes 2a and 2b under a branch model. In simulations the modified test has acceptable false positive rates and more power than the branch test (Zhang, Nielsen and Yang 2005; Yang and dos Reis 2011). Sites under selection on the foreground branches can be identified by BEB, but their posterior probabilities rarely reach high values. Related models divide the tree into clades with different $\omega$ for one class of sites (clade models), or let the $\omega$ of each site switch among values along the tree as a hidden Markov process (switching models), which needs no foreground but is less powerful when a foreground hypothesis exists.

**Example 23.5.1 (Phytochromes after Gene Duplication)** The **phytochrome** photoreceptors of flowering plants are encoded by a small gene family. In an alignment of 16 sequences of the A and C/F subfamilies, the foreground was the branch separating the subfamilies, which follows a gene duplication. Under M0, $\hat\omega = 0.089$: purifying selection dominates. A branch model with separate ratios for foreground and background gives $\hat\omega_1 = 0.016$ for the foreground, and $2\Delta\ell = 1.28$ ($p = 0.26$): no evidence of selection. The branch-site test gives $\ell_0 = -29\,704.74$ under the null and $\ell_1 = -29\,694.80$ under the alternative, $2\Delta\ell = 19.88$, with $p = 8.2 \times 10^{-6}$ from $\chi^2_1$ or $4.1 \times 10^{-6}$ from the mixture: about $11\,\%$ of sites were under positive selection along the foreground branch, and BEB identified 27 of them (Yang 2014, analyzing data of Alba and colleagues 2000). The estimate $\hat\omega_2 = 131$ is not meaningful by itself: with a short foreground branch and few changes, $\omega_2$ is poorly determined and only its being above 1 is informative.

## 23.6. Assumptions, Pitfalls and Results

### 23.6.1. Assumptions and False Positives

Codon models describe substitution, not the population genetics of mutation and selection, and their assumptions can mislead in specific ways:

- *One ratio for all amino acid pairs.* Exchanges between similar amino acids are more frequent than between dissimilar ones; models using physicochemical distances fit better but only moderately. Comparisons of "radical" and "conservative" replacements as evidence of selection are much more sensitive to model assumptions than $\omega$.
- *Conservativeness.* Branch models average over sites, site models over branches; recurrent diversifying selection is detected well, while a single adaptive substitution that sweeps quickly to fixation leaves almost no signal in $\omega$.
- *Constant synonymous rate.* Variation of $d_{\mathrm{S}}$ among sites is significant in most data sets; its effect on site detection appears to be modest when M2a or M8 and BEB are used.
- *One tree for all sites.* Recombination within the gene, frequent in some viruses, gives different sites different genealogies and can produce false positives; methods for detecting recombination often assume neutrality and may themselves mistake selection for recombination.
- *Alignment errors.* Placing nonsynonymous codons from different positions in the same column creates apparent nonsynonymous substitutions at that site, and such sites are readily called positively selected; alignment quality is critical.
- *Divergence.* Too little divergence leaves no information, too much saturates synonymous sites and makes alignment and codon usage difficult.
- *Simultaneous changes.* The models allow only one nucleotide change at a time; multinucleotide mutations, which change adjacent bases in one event, are interpreted as several substitutions at a site and can inflate the branch-site test (Venkat, Hahn and Thornton 2018).

### 23.6.2. Comparison with Population-Genetic Tests

The tests of this chapter and the neutrality tests of [7.10.8](/7.10.8#sec-8.2) are designed for different data and detect different things. Codon models need divergent sequences and have almost no power on samples from a single population; neutrality tests are designed for population samples and closely related species. An excess of amino acid replacements has hardly any explanation other than positive selection, while a rejected neutrality test may reflect any violation of a composite null hypothesis: growth or structure as well as selection at the locus or linked loci. In simulations with repeated selective sweeps on a neutral background, tests based on $\omega$ between species are usually more powerful than tests based on polymorphism, because each sweep leaves its trace in polymorphism only briefly, while its fixed differences accumulate (Zhai and colleagues 2009). The **McDonald–Kreitman test** combines the two kinds of data.

### 23.6.3. Which Genes Evolve Adaptively

The genes in which positive selection has been detected from $\omega$ fall mostly into three overlapping categories (Yang 2014):

- *Host defense and pathogen evasion.* Host genes for immunity (the MHC; the retroviral restriction factor TRIM5α of primates; plant resistance genes that recognize pathogens) and pathogen genes for evading it (viral surface and capsid proteins; membrane antigens of *Plasmodium*; enzymes of plant enemies that attack cell walls). Each side selects for change in the other, an **evolutionary arms race** ([7.10.17](/7.10.17#sec-17.2.1)) with the dynamics of the **Red Queen hypothesis**; in phage coevolving with bacteria, the phage evolved much faster than against a fixed host (Paterson and colleagues 2010). Toxins in the venoms of snakes and scorpions, which subdue prey, also evolve fast.
- *Reproduction.* Proteins of sperm–egg recognition and other reproductive proteins, such as the abalone sperm lysin of [7.10.8](/7.10.8#sec-8.1.1), evolve rapidly, perhaps through **sexual conflict** over the speed of fertilization and the risk of polyspermy, and may contribute to reproductive isolation ([7.10.11](/7.10.11)).
- *New functions after duplication.* Accelerated, sometimes adaptive, protein evolution follows many gene duplications ([7.10.18](/7.10.18#sec-18.2)): the *DAZ* gene family and chorionic gonadotropin of primates, the pancreatic ribonuclease duplicated in leaf-eating colobine monkeys, the phytochromes of Example 23.5.1.

Detections are statistical hypotheses about the past. Their strongest confirmation comes from experiments: reconstructing and expressing ancestral proteins ([7.10.26](/7.10.26), [7.10.21](/7.10.21)) and testing the effect of the inferred substitutions.

## Summary

| Topic | Result |
|---|---|
| distances | $d_{\mathrm{S}}$, $d_{\mathrm{N}}$ per synonymous and nonsynonymous site; counting needs sites, differences and a multiple-hit correction |
| counting methods | NG86 (Definition 23.1.1, Eq. (23.1)); LWL85 by degeneracy classes (Eq. (23.2)), LPB93, Ina, YN00; transition bias lowers and codon bias raises $\hat\omega$; methods disagree almost twofold (*rbcL*, Example 23.1.2) |
| codon model | 61 sense codons, rates $\pi_J$, $\kappa$, $\omega$ (Definition 23.2.1, Eq. (23.3)); Muse–Gaut; FMutSel with fixation probabilities (Eq. (23.4)); reversible, $P(t) = \mathrm{e}^{Qt}$ |
| $d_{\mathrm{S}}$, $d_{\mathrm{N}}$ in the model | sites as mutational opportunities with $\omega = 1$ (Definition 23.2.2, Eq. (23.5)); $d_{\mathrm{N}}/d_{\mathrm{S}} = \omega$ exactly, $t = Sd_{\mathrm{S}} + Nd_{\mathrm{N}}$ (Theorem 23.2.1); synonymous sites need not be neutral |
| estimation | likelihood Eq. (23.6), pruning on trees; assumptions matter more than method (Example 23.2.1); saturation and within-population inflation of $\omega$ |
| branch models | $\omega$ by branch, foreground chosen a priori (Definition 23.3.1); $\omega_1 > \omega_0$ is not evidence of adaptation unless $\omega_1 > 1$ |
| site models | mixtures over site classes (Definition 23.4.1, Eq. (23.7)); M1a–M2a and M7–M8; MHC: $8\,\%$ of sites at $\omega \approx 5.4$ (Example 23.4.1) |
| boundary | $2\Delta\ell \to \frac12\chi^2_0 + \frac12\chi^2_1$, critical value 2.71 (Theorem 23.4.1); $\chi^2_2$ conservative for M1a–M2a |
| selected sites | posterior class probabilities, Eq. (23.8); NEB, BEB |
| branch-site test | four site classes, null $\omega_2 = 1$ (Definition 23.5.1); phytochromes after duplication (Example 23.5.1) |
| pitfalls | alignment errors, recombination, multinucleotide mutations, saturation; immunity, reproduction and duplicated genes dominate the detections |

## Questions

1. Show that the codon CCT has $S = 1$ and $N = 2$ both with equal mutation rates and with $\kappa = 2$.

   **Answer** All three changes at the third position are synonymous (CCN is Pro), all six at the first two positions nonsynonymous: $S = 1$. With $\kappa = 2$ each position has weight $2 + 1 + 1 = 4$, so $S = 3 \times 4/12 = 1$ again; the count changes only where transitions and transversions differ in synonymy, as at the third position of TTT.

2. NG86 gives $S = 200$, $N = 600$, $S_{\mathrm{d}} = 40$, $N_{\mathrm{d}} = 12$. Compute $d_{\mathrm{S}}$, $d_{\mathrm{N}}$ and $\omega$.

   **Answer** $p_{\mathrm{S}} = 0.2$, $p_{\mathrm{N}} = 0.02$; Eq. (23.1) gives $d_{\mathrm{S}} = 0.233$, $d_{\mathrm{N}} = 0.0203$, $\omega = 0.087$. With strong transition bias, $S$ is undercounted, so $\hat\omega$ is probably too small.

3. Why can a gene with average $\omega = 0.6$ still contain sites under positive selection?

   **Answer** The average mixes site classes: in the MHC, $78\,\%$ of sites at $\omega \approx 0.06$, $14\,\%$ at 1 and $8\,\%$ at about 5.4 average to about 0.6. Site models (Eq. (23.7)) detect the class with $\omega > 1$ by the M1a–M2a test ($\Delta\ell \approx 260$) and Eq. (23.8) locates the sites.

4. A branch-site test gives $2\Delta\ell = 3.2$. Compute the $p$-value from the mixture and from $\chi^2_1$.

   **Answer** $\mathbb{P}(\chi^2_1 > 3.2) = 0.074$; the 1:1 mixture gives $0.037$ (Theorem 23.4.1). The mixture is correct asymptotically; $\chi^2_1$ is a conservative safeguard against model violations such as alignment errors.

5. Why is $\omega$ between individuals of one species not a test of positive selection?

   **Answer** Their differences are mostly polymorphisms, including slightly deleterious nonsynonymous mutations not yet removed, so $\omega$ is inflated at short divergence and falls with time; it reflects the time scale, not adaptation. Polymorphism calls for the tests of [7.10.8](/7.10.8#sec-8.2).
