---
title: Statistical Properties of Phylogenetic Methods and Tests of Trees
description: "Phylogenetic methods as statistical estimators: why trees are hard to estimate (homoplasy, long branches, incomplete lineage sorting, horizontal transfer); trees as models rather than parameters; criteria of performance; least squares and minimum evolution, neighbor joining as balanced minimum evolution; weighted parsimony, its assumptions and the Tuffley–Steel equivalence with a no-common-mechanism likelihood; consistency, efficiency and robustness of maximum likelihood, the Felsenstein and Farris zones; reversibility, the root and the clock; the ape mitochondrial proteins; local optima; ancestral state reconstruction by empirical Bayes, marginal and joint, and its biases; goodness of fit by parametric bootstrap; interpreting bootstrap support, the interior-branch test, the KH, SH and AU tests; consistency and retention indices."
---

[7.8.6](/7.8.6) presented the methods of tree inference as algorithms: the number of trees ([Theorem 6.1.1](/7.8.6#thm-6.1.1) of 7.8.6), distance methods with UPGMA and **neighbor joining** ([Section 6.3](/7.8.6#sec-6.3)), **maximum parsimony** with the Fitch and Sankoff algorithms ([Section 6.4](/7.8.6#sec-6.4)), maximum likelihood with **Felsenstein's pruning algorithm**, tree search by NNI, SPR and TBR, and model choice by AIC and BIC ([Section 6.5](/7.8.6#sec-6.5)), and **bootstrap support** ([Section 6.6](/7.8.6#sec-6.6)). This chapter treats the same methods as statistical estimators and asks what statisticians ask of any estimator. Does it converge to the truth as data accumulate (consistency)? How fast (efficiency)? How badly does it fail when its assumptions are wrong (robustness)? And how uncertain is the answer, which leads to tests of trees. The answers differ from those of ordinary parameter estimation, because the object estimated, the tree topology, is discrete and changes the meaning of every other parameter. The chapter also treats the reconstruction of ancestral states, which uses the same machinery for a different end, and closes with the indices reported in parsimony analyses.

The substitution models and their likelihood for two sequences are in [7.10.20](/7.10.20); the Bayesian alternative to the bootstrap and to tree tests is in [7.10.22](/7.10.22); gene-tree discordance caused by population processes is in [7.10.25](/7.10.25).

## 21.1. Phylogeny Estimation as a Statistical Problem

### 21.1.1. Why Phylogenies Are Hard to Estimate

Shared derived characters are evidence of common ancestry only if they arose once. Four evolutionary phenomena break this, and they are the sources of error that the statistical methods of this chapter try to control.

- **Homoplasy**: the same state evolves more than once, by **convergent evolution**, parallelism or reversal. For a nucleotide, which has only four states, homoplasy is unavoidable: repeated changes at a site are the multiple hits of [7.10.20](/7.10.20).
- Unequal rates among lineages and among sites. Fast lineages accumulate homoplasies on their long branches, and methods that underestimate multiple hits group them together: **long-branch attraction**. Rate variation among sites makes the fast sites saturate and the slow ones uninformative.
- **Incomplete lineage sorting**: when speciation events follow each other closely, ancestral polymorphism persists across them and gene trees differ from the species tree ([7.10.25](/7.10.25)).
- **Horizontal gene transfer** and hybridization, which give parts of a genome a history different from the rest.

Two properties of the true tree govern how hard it is. *Easy* trees have long internal branches: every reasonable method recovers them. *Hard* trees have short internal branches and long external branches scattered across the tree; on them, methods that model the process poorly fail, and even good methods need much data. The information in the data is greatest at intermediate divergence: very similar sequences contain few changes, very divergent ones are saturated. This is why fast-evolving genes are chosen for recent radiations and slowly evolving proteins for deep ones.

### 21.1.2. Trees Are Models, Not Parameters

In ordinary estimation, a single model $f(X \mid \theta)$ is fully specified except for the parameter $\theta$. In phylogenetics, each topology $\tau$ defines a different model $f_\tau(X \mid \theta_\tau)$, with its own parameters: the branch lengths of one tree are not those of another, since a branch is defined by the split of the taxa that it separates. Choosing the tree is therefore a problem of *model selection* among models of equal dimension, not of parameter estimation (Yang, Goldman and Friday 1995). The distinction matters because the classical theorems on the consistency and efficiency of maximum likelihood estimators ([3.2.3](/3.2.3)) are proved for parameter estimation; some hold for tree estimation (consistency, Section 21.4.1) and some do not (efficiency, Section 21.4.2).

The performance of a tree-building method is judged by several criteria:

| Criterion | Meaning |
|---|---|
| Consistency | the probability of recovering the true tree tends to $1$ as the number of sites tends to infinity, the analog of a **consistent estimator** |
| Efficiency | the probability of recovering the true tree with a given finite number of sites, relative to other methods |
| Robustness | the method still performs well when its assumptions are violated |
| Computation | the time needed, which decides what is feasible with thousands of taxa |
| Falsifiability | whether the method's assumptions can be tested on the data |

Because the probability of recovering the true tree can rarely be computed analytically, almost everything known about these properties comes from simulation, with sequences generated on known trees by the algorithms of [7.10.20](/7.10.20#sec-20.6).

## 21.2. Distance Criteria

### 21.2.1. Least Squares

A distance method takes the matrix of estimated pairwise distances $d_{ij}$ as data and fits a tree whose path lengths $\delta_{ij}(\boldsymbol{b})$, sums of branch lengths $\boldsymbol{b}$, match them. The **least squares** score of a tree is

$$
S(\tau) = \min_{\boldsymbol{b}}\sum_{i<j}w_{ij}\bigl(d_{ij} - \delta_{ij}(\boldsymbol{b})\bigr)^2, \tag{21.1}
$$
and the least-squares tree minimizes it (Cavalli-Sforza and Edwards 1967). For a fixed topology $\delta = A\boldsymbol{b}$ with a $0/1$ design matrix $A$ (row $ij$ marks the branches on the path from $i$ to $j$), so fitting branch lengths is a linear regression; with nonnegativity constraints it is a constrained one. Ordinary least squares takes $w_{ij} = 1$; but the variance of a distance grows with its size ([7.10.20](/7.10.20#sec-20.3.3)), and distances that share branches are correlated, which suggests **weighted least squares** with $w_{ij} = 1/\operatorname{Var}(d_{ij})$ (Fitch and Margoliash 1967 used $1/d_{ij}^2$) or **generalized least squares** with the full covariance matrix of the distances.

**Example 21.2.1** For mitochondrial sequences of human (H), chimpanzee (C), gorilla (G) and orangutan (O) with K80 distances $d_{\mathrm{HC}} = 0.0965$, $d_{\mathrm{HG}} = 0.1140$, $d_{\mathrm{CG}} = 0.1180$, $d_{\mathrm{HO}} = 0.1849$, $d_{\mathrm{CO}} = 0.2009$, $d_{\mathrm{GO}} = 0.1947$ (data of Brown and colleagues 1982, as tabulated by Yang 2014), the tree ((H, C), G, O) fits with internal branch $0.0088$, external branches $0.0433$ (H), $0.0533$ (C), $0.0589$ (G) and $0.1358$ (O), and $S = 3.6\times10^{-5}$. On the other two topologies the internal branch shrinks to zero under the nonnegativity constraint and $S = 1.4\times10^{-4}$: the data support (H, C), and the alternatives collapse to the star tree.

### 21.2.2. Minimum Evolution and Neighbor Joining

**Definition 21.2.1 (Minimum Evolution)** The **minimum evolution** criterion fits branch lengths to the distances on each topology (usually by least squares) and chooses the topology with the smallest tree length, the sum of its branch lengths (Kidd and Sgaramella-Zonta 1971; Rzhetsky and Nei 1993).

The criterion, an idea of Edwards and Cavalli-Sforza (1963), applies to distances the same principle that parsimony applies to discrete characters. Its statistical properties depend on details that look technical. Minimum evolution with ordinary least-squares branch lengths is consistent: as the distances converge to additive ones, the true tree becomes the shortest. With weighted or generalized least-squares branch lengths it can be inconsistent (Gascuel and colleagues 2001), a surprising case where the better estimator of branch lengths gives the worse criterion for topology.

Neighbor joining fits here. Saitou and Nei (1987) argued that its pair selection minimizes the OLS tree length, which holds only at the first step. Gascuel and Steel (2006) showed that it is a greedy algorithm for the *balanced* minimum evolution criterion, which uses Pauplin's (2000) estimate of tree length,

$$
\hat L(\tau) = \sum_{i<j}2^{-n_{ij}}d_{ij}, \tag{21.2}
$$
where $n_{ij}$ is the number of internal vertices on the path from $i$ to $j$ in the binary tree $\tau$. For four taxa with split $ab \mid cd$, $\hat L = \frac{1}{2}(d_{ab} + d_{cd}) + \frac{1}{4}(d_{ac} + d_{ad} + d_{bc} + d_{bd})$, which equals the true tree length for additive distances. The weights $2^{-n_{ij}}$ down-weight long, noisy distances, as weighted least squares intends, while the criterion stays consistent (Desper and Gascuel 2004). A search of tree space under this criterion (FastME) is more accurate than neighbor joining's single greedy pass. The consistency of neighbor joining itself is [Theorem 6.3.2](/7.8.6#thm-6.3.2) of 7.8.6.

## 21.3. Parsimony Revisited

### 21.3.1. Weighted Parsimony and Its Assumptions

Unweighted parsimony counts every change as one step. Weighted parsimony assigns costs $c(a, b)$ to changes, computed by Sankoff's algorithm ([Algorithm 6.4.1](/7.8.6#alg-6.4.1) of 7.8.6 and the text after it): transversions may cost more than transitions, changes at third codon positions less, and in *transversion parsimony* transitions cost nothing. *Successive weighting* down-weights characters that show much homoplasy on a first tree. All of these are attempts to make the cost of a change reflect its improbability, which is what a likelihood model does with branch lengths and rate matrices.

What parsimony assumes has been argued for decades. It does not assume that evolution is parsimonious, but it treats a change on a long branch as just as unlikely as one on a short branch, and it ignores multiple changes that it cannot see. The method works well when changes are rare on every branch, which is when the expected number of homoplasies is small; it fails, inconsistently, when two long branches are separated by a short one, in the **Felsenstein zone** of [Definition 6.4.2](/7.8.6#def-6.4.2) of 7.8.6. Parsimony is also not falsifiable in the statistical sense: it has no model whose fit to the data could be tested.

### 21.3.2. Parsimony as a Likelihood Method

When do parsimony and likelihood give the same tree on every data set?

**Theorem 21.3.1 (Tuffley–Steel Equivalence)** Under the symmetric $c$-state model (JC69 for $c = 4$), the likelihood of a single character on a tree, maximized over the branch lengths, is $c^{-(1 + l)}$, where $l$ is the parsimony length of the character on the tree. Consequently, under the *no-common-mechanism* model, in which every character has its own set of branch lengths, the maximum likelihood tree is the most parsimonious tree (Tuffley and Steel 1997).

**Proof** (sketch) Let $l$ be the parsimony length. Taking a most parsimonious reconstruction, set each branch that carries a change to infinite length (its end state is then a uniform random draw, probability $1/c$) and every other branch to length $0$ (no change, probability $1$); with the root state probability $1/c$, the likelihood is $c^{-(1 + l)}$. Tuffley and Steel showed that no assignment of branch lengths does better. With a separate set of branch lengths for each character, the maximized log-likelihood of the data is $-\sum_h(1 + l_h)\ln c$, a decreasing function of the total parsimony length. $\square$

The theorem is of philosophical rather than practical interest. The no-common-mechanism model has a number of parameters that grows with the number of sites, so the usual asymptotic properties of likelihood do not apply, and statisticians regard such models as ill-posed; compared by Bayes factors with ordinary models, it fits real data far worse (Huelsenbeck and colleagues 2011). A connection with well-behaved models exists in the opposite limit: as all branch lengths become small, the likelihood of a site is dominated by the reconstructions with the fewest changes (Question 5 of [7.8.6](/7.8.6)), and ML and parsimony choose the same tree. Parsimony is thus an approximation to likelihood that is good when change is rare, and poor exactly where the trees are hard.

## 21.4. Statistical Properties of Maximum Likelihood

### 21.4.1. Consistency

**Theorem 21.4.1 (Consistency of Maximum Likelihood Trees)** Suppose sites evolve independently under a substitution model for which different trees, with any branch lengths, give different distributions of site patterns (the model is identifiable). If the model is correct, the probability that the maximum likelihood tree is the true tree tends to $1$ as the number of sites tends to infinity.

**Proof** (sketch, after Yang 1994) Let $f_i = n_i/n$ be the observed frequency of site pattern $i$. For any tree $\tau$ with branch lengths $\theta$, the log-likelihood is $\ell_\tau = n\sum_if_i\ln p^{(\tau)}_i(\theta)$, and

$$
\frac{\ell_{\max} - \ell_\tau}{n} = \sum_if_i\ln\frac{f_i}{p^{(\tau)}_i(\theta)} \ge 0, \qquad \ell_{\max} = n\sum_if_i\ln f_i, \tag{21.3}
$$
the **Kullback–Leibler divergence** from the model to the observed pattern distribution. As $n \to \infty$, $f_i$ converges to the pattern probabilities $p^{(\tau_0)}_i(\theta_0)$ of the true tree, and its maximized likelihood approaches $\ell_{\max}$. Any other tree can approach it only if it can reproduce the same pattern probabilities, which identifiability excludes; its divergence stays bounded away from zero, and its log-likelihood falls behind by an amount proportional to $n$. $\square$

The standard models (JC69 to GTR, with gamma rates) are identifiable (Chang 1996; Allman and Rhodes 2006 and later work), so ML is consistent when the model is right. Under a wrong model it may be inconsistent: likelihood under JC69 applied to data with strong rate variation behaves like parsimony and attracts long branches.

### 21.4.2. Efficiency

For conventional parameters, the MLE is asymptotically efficient: no regular estimator has a smaller asymptotic variance (the **Cramér–Rao inequality**). For tree topology there is no such guarantee. Simulations found that, on some trees, likelihood under the true model recovers the true tree less often than parsimony or than likelihood under a wrong, simpler model, and that the gap persists as the number of sites grows (Yang 1996, 1997). The explanation is a bias in favor of the truth. Parsimony and simplistic likelihood tend to group long branches; on a tree in which the long branches really are sisters (the *Farris zone*), this bias helps, and the biased method beats the unbiased one. In the Felsenstein zone the same bias makes it fail.

The figure shows both zones on one axis. Recovering a tree whose internal branch is very short is hard for likelihood, which needs informative changes on that branch; parsimony recovers the Farris-zone tree even when the branch is so short that no change on it is expected, because the patterns that support it arise from parallel changes on the long branches. The lesson is not that parsimony is preferable, since nobody knows in advance in which zone the truth lies: a method that is consistent everywhere is preferable to one that is excellent in one region and inconsistent in another. It is that efficiency for topology depends on the tree, and a method can be asymptotically more efficient than ML over a whole region of parameter space, which cannot happen in conventional estimation.

![The relative performance of methods depends on the shape of the tree, after Swofford and colleagues (2001). Alignments of 1000 sites are simulated under JC69 on four-taxon trees with two long external branches (0.5 substitutions per site), two short ones (0.05) and an internal branch t₀, and each is analyzed by maximum parsimony and by maximum likelihood under JC69, with the branch lengths optimized on each of the three topologies (50 data sets per point). Left of the center (Farris zone), the long branches are sisters; right (Felsenstein zone), they are not, and the internal branch grows outward from the center in both directions; the dashed line marks 1/3, a random choice among the three trees. Parsimony recovers the Farris-zone tree in every data set and the Felsenstein-zone tree in almost none: it is inconsistent there. Likelihood is consistent in both zones, more accurate as the internal branch grows, but in the Farris zone less accurate than the biased method](./plots/zones.py)

### 21.4.3. Robustness

Simulations have examined how ML behaves when its assumptions are violated, with a fairly consistent picture (summarized by Yang 2014). Some violations have a large effect on the fit of the model but little on the tree: ignoring the transition/transversion rate difference or unequal base frequencies rarely changes the inferred topology. Others matter much more: ignoring rate variation among sites underestimates long branches and produces long-branch attraction; changes of composition among lineages group taxa of similar composition ([7.10.20](/7.10.20#sec-20.3.4)); and changes of rates across the tree at individual sites (heterotachy) can mislead all methods. Model-based methods using adequate models of rate variation are, overall, more robust than distance methods and parsimony, which is why they are the standard.

### 21.4.4. Reversibility, the Root and the Clock

Under a reversible model, the likelihood of a rooted tree does not change when the root is moved along any branch (the pulley principle, Eq. (20.4) of 7.10.20), so only unrooted trees are identifiable, with $2s - 3$ branch lengths for $s$ species. Under a **molecular clock**, every tip is equidistant from the root and the parameters are the $s - 1$ ages of the internal vertices; the root is then identifiable from the sequence data. The clock is a constraint on the unrooted tree, and a likelihood ratio test with $s - 2$ degrees of freedom compares the two. Real data usually reject the strict clock, which motivates the relaxed clocks of [7.10.24](/7.10.24). Nonreversible and nonstationary models can also identify the root, but the signal is weak.

### 21.4.5. Example: The Phylogeny of Apes

**Example 21.4.1** The $12$ mitochondrial proteins encoded by the heavy strand of seven apes (human, common chimpanzee, bonobo, gorilla, Bornean and Sumatran orangutans, gibbon), concatenated into $3331$ amino acids, allow an exhaustive evaluation of all $945$ unrooted binary trees under the empirical MTMAM model (analysis of Yang 2014). The ML tree groups humans with the two chimpanzees, then gorilla, the two orangutans and the gibbon, with $\ell = -14\,558.59$; the worst binary tree has $-15\,769.00$ and the star tree $-15\,777.60$. The same tree has the shortest parsimony length and the shortest sum of ML branch lengths, so likelihood, parsimony and minimum evolution agree, and so does likelihood under the Poisson model ($\ell = -16\,566.60$, much worse in fit). Adding discrete gamma rates with five categories raises the log-likelihood to $-14\,411.90$ with $\hat\alpha = 0.333$ (and $-14\,413.38$ with $\alpha = 0.4$ fixed); $2\Delta\ell = 293.4$ against the one-rate model, a boundary test (Section 20.5.2 of 7.10.20) rejected beyond doubt. The best alternative trees are ((human, gorilla), chimpanzees), $35.0$ log-likelihood units worse, and ((chimpanzees, gorilla), human), $38.2$ units worse. These are the three resolutions of the human–chimpanzee–gorilla trichotomy, the classic case of a short internal branch, which the tests of Section 21.7 examine.

### 21.4.6. The Likelihood Surface

Two kinds of multiple optima complicate the computation. On a fixed tree, the likelihood as a function of the branch lengths is usually unimodal in practice, but multiple local maxima have been constructed for small data sets (Steel 1994) and occur occasionally in real ones, so programs optimize from several starting points when it matters. In the space of trees, the local search of [Section 6.5.2](/7.8.6#sec-6.5.2) of 7.8.6 can be trapped on *islands*, groups of good trees separated by trees that are worse than all of them under the rearrangements used; larger moves (SPR, TBR), several random starting trees and stochastic perturbation of the current best tree are the remedies, and their success is checked by comparing the best likelihoods found by independent searches.

## 21.5. Ancestral State Reconstruction

**Definition 21.5.1 (Ancestral State Reconstruction)** **Ancestral state reconstruction** is the inference of the character states (nucleotides, amino acids, morphological states) at the internal vertices of a phylogeny from the states at its tips. A *marginal* reconstruction assigns a state to one vertex; a *joint* reconstruction assigns states to all internal vertices at once.

Reconstructed ancestors are used to count changes on branches, to study the evolution of characters (the comparative method of [7.10.26](/7.10.26)), and to resurrect ancient proteins in the laboratory, an idea of Pauling and Zuckerkandl (1963) that is now routine. Parsimony gives reconstructions directly (the downward pass of the Fitch algorithm). In a Markov model, the ancestral states are not parameters: they are unobserved random variables, summed over in the likelihood. The correct inference is therefore their conditional distribution given the data, computed with the parameters (branch lengths, rate matrix) set to their MLEs, an **empirical Bayes** procedure (Yang and colleagues 1995). For the root,

$$
\mathbb{P}(x_0 = a \mid \text{site}) = \frac{\pi_aL_0(a)}{\sum_b\pi_bL_0(b)}, \tag{21.4}
$$
with $L_0$ the partial likelihoods of the pruning algorithm; any other vertex is treated by moving the root there, which reversibility allows. The probability of a joint reconstruction is the product of the transition probabilities along all branches divided by the likelihood of the site, and the best one is found by a dynamic program like Sankoff's algorithm with branch-specific costs $-\ln p_{ab}(t)$ (Pupko and colleagues 2000). Marginal probabilities must not be multiplied to obtain joint ones, because the states at neighboring vertices are dependent.

Compared with parsimony, empirical Bayes takes branch lengths and unequal rates into account and, above all, quantifies uncertainty. Under JC69 with equal branch lengths the two rank joint reconstructions identically; otherwise they usually agree on the best reconstruction, and the main determinant of accuracy for both is the divergence of the sequences. Two refinements address the parameters treated as known: a hierarchical Bayesian analysis integrates over branch lengths and rates, which matters for small data sets and for single morphological characters, where the rates cannot be estimated reliably; and *stochastic mapping* samples whole histories of changes on the tree from their posterior distribution.

Reconstructed states are inferred pseudo-data, and using only the best reconstruction at each site biases the conclusions systematically. On a star tree of three sequences with branches of $0.2$ evolving under F81 with the base frequencies of the human mitochondrial D-loop (T $0.2263$, C $0.3282$, A $0.3393$, G $0.1062$), a site with pattern AAG has posterior probability $0.903$ for A and $0.083$ for G at the root. Choosing the best state at every site over-counts common nucleotides and under-counts rare ones: the reconstructed root has composition $0.212$, $0.324$, $0.369$, $0.095$, more extreme than the stationary process that generated the data, and a spurious gain of G toward the present follows (example of Yang 2014). Averaging over the posterior probabilities removes the bias. The same artifact has produced apparent trends in amino acid composition and overestimated the thermostability of resurrected proteins.

![Ancestral state reconstruction by empirical Bayes. A and B: marginal posterior probabilities of T, C, A and G (bars, left to right in each group) at the four internal vertices of a rooted five-taxon tree, for one site with tip states T, C, A, C, C under K80 with κ = 2, with short branches (A) and with all branch lengths multiplied by four (B); the label below each group gives the most probable state and its probability, and the line at the bottom the best joint reconstruction and its posterior probability. With short branches the reconstruction CCCC is fairly certain; with long branches every vertex is uncertain. C: the systematic bias of using only the best reconstruction, for three sequences on a star tree with branches of 0.2 under F81 with the base frequencies of the human mitochondrial D-loop (example of Yang 2014): the expected root composition from the most probable state at each site exaggerates the common A and depletes the rare G, while the average of the posterior probabilities reproduces the true composition](./plots/ancestral.py)

## 21.6. Model Adequacy

Likelihood ratio tests and information criteria compare models with each other; they do not say whether the best is adequate. A test of absolute fit uses the fact that the site-pattern counts of an alignment of $s$ sequences are a multinomial sample with $4^s$ categories. The saturated multinomial model, with one free probability per pattern, has maximized log-likelihood $\ell_{\max} = \sum_in_i\ln(n_i/n)$, and every substitution model is a special case of it. The statistic $\Delta = \ell_{\max} - \ell_{\text{model}}$ would be compared with a $\chi^2$ distribution, but most of the $4^s$ patterns have expected counts near zero and the asymptotic theory fails. The **parametric bootstrap** ([3.5.7](/3.5.7#alg-7.4.1)) supplies the null distribution instead (Goldman 1993): simulate many alignments under the fitted model and tree, refit each in the same way, and compare the observed $\Delta$ with the simulated values.

**Example 21.6.1** For the plastid *rbcL* genes of $12$ plant species ($1312$ sites without gaps), $\ell_{\max} = -4025.03$ and HKY85 + Γ gives $\ell = -5242.35$, so $\Delta = 1217.32$. In $1000$ data sets simulated under the fitted model, $38.7\,\%$ of the $\Delta$ values exceed the observed one: HKY85 + Γ is adequate by this test, while JC69 is strongly rejected by the same procedure (analysis of Yang 2014). Model choice by AIC and BIC is described in [Section 6.5.3](/7.8.6#sec-6.5.3) of 7.8.6 and [3.4.11](/3.4.11). The Bayesian counterpart of this test is the posterior predictive check of [3.7.7](/3.7.7).

## 21.7. Testing Trees

### 21.7.1. What the Bootstrap Measures

Felsenstein's bootstrap support ([Definition 6.6.1](/7.8.6#def-6.6.1) of 7.8.6) is the most widely reported measure of confidence, and its interpretation has been debated since it was introduced. It is not the probability that a clade is true (that is a Bayesian quantity, [7.10.22](/7.10.22)). It can be read as an approximate measure of repeatability, the probability that the clade would be recovered from a new data set of the same size, or, following Felsenstein and Kishino (1993), as approximately one minus a p-value for the hypothesis that the clade is absent; but this p-value is not correct even to first order (Susko 2009), and the corrections proposed by Efron, Halloran and Holmes (1996) and others are rarely used. Empirically, in the simulations of Hillis and Bull (1993), clades with $70\,\%$ support were true in $95\,\%$ of cases, but other studies have found the bootstrap too liberal in some conditions. It measures sampling error only: it is blind to the systematic errors of an inconsistent method or a wrong model. A faster approximation, *RELL* (resampling estimated log-likelihoods, Kishino and Hasegawa 1989), resamples the site log-likelihoods computed at the original MLEs instead of reoptimizing each tree on each replicate. In the ape example, the full bootstrap gives the ML tree $99.4\,\%$, the two alternatives $0.3\,\%$ each; RELL gives $98.7\,\%$, $1.0\,\%$ and $0.3\,\%$.

### 21.7.2. The Interior-Branch Test

A second approach asks whether an internal branch is significantly longer than zero, by a likelihood ratio test of the tree with and without that branch constrained to zero. The null value lies on the boundary, so the statistic has a $50:50$ mixture of $0$ and $\chi^2_1$ as its null distribution. The test has three difficulties: the tree whose branch is tested is chosen from the same data; testing every branch raises the issue of **multiple comparisons**; and branches of wrong trees can be estimated to be significantly positive (Tateno and colleagues 1994), so a positive branch does not establish that the split is right. The SH-like approximate likelihood ratio test of [7.8.6](/7.8.6#sec-6.6.1) is a descendant that corrects for the alternative resolutions around a branch.

### 21.7.3. The KH, SH and AU Tests

To compare whole trees, the likelihood ratio test is not available: two topologies are not nested, and the null hypothesis is not of the form "a parameter is zero". Kishino and Hasegawa used the variation among sites instead.

**Definition 21.7.1 (Kishino–Hasegawa Test)** For two trees $\tau_1$ and $\tau_2$ specified before the data are seen, with site log-likelihoods $\ell_{1h}$ and $\ell_{2h}$ at their MLEs, the **Kishino–Hasegawa test** (KH test) takes $\delta = \ell_1 - \ell_2 = \sum_hd_h$, $d_h = \ell_{1h} - \ell_{2h}$, and estimates its variance by treating the $d_h$ as independent and identically distributed,

$$
\widehat{\operatorname{Var}}(\delta) = \frac{n}{n - 1}\sum_{h=1}^n(d_h - \bar d)^2; \tag{21.5}
$$
the trees differ significantly if $\lvert\delta\rvert$ exceeds about $1.96$ standard errors (or its RELL distribution is used).

The test is valid only if the two trees are chosen in advance. In practice, the ML tree is found from the data and every other tree is tested against it; the ML tree is then favored by construction, and the test rejects good trees far too often (Shimodaira and Hasegawa 1999; Goldman, Anderson and Rodrigo 2000).

**Definition 21.7.2 (Shimodaira–Hasegawa Test)** The **Shimodaira–Hasegawa test** (SH test) compares a set of candidate trees $\tau_1, \dots, \tau_m$ chosen in advance (it may include the ML tree) and tests, for each $\tau_i$, the statistic $T_i = \max_j\ell_j - \ell_i$. Its null distribution is computed under the least favorable hypothesis that all trees in the set have equal expected log-likelihood:

1. Draw $B$ RELL replicates of the site log-likelihoods, giving $\ell_i^{(b)}$ for every tree.
2. Center each tree's replicates: $\tilde\ell_i^{(b)} = \ell_i^{(b)} - \bar\ell_i$, with $\bar\ell_i$ the mean over replicates.
3. Compute $T_i^{(b)} = \max_j\tilde\ell_j^{(b)} - \tilde\ell_i^{(b)}$; the p-value of $\tau_i$ is the fraction of replicates with $T_i^{(b)} \ge T_i$.

The SH test controls the probability of rejecting the true tree, whatever it is, but by assuming the worst case it is very conservative, and the more trees in the candidate set, the fewer it rejects.

**Definition 21.7.3 (Approximately Unbiased Test)** The **approximately unbiased test** (AU test, Shimodaira 2002) computes p-values for trees (or clades) from a *multiscale bootstrap*: the bootstrap proportion of the hypothesis is computed for replicates of several lengths $n' = rn$ ($r$ from about $0.5$ to $1.4$), the normal quantile of the proportion is fitted as a function of the scale $\sigma^2 = n/n'$ by a model of the boundary of the hypothesis region, and the fit is extrapolated to $\sigma^2 = -1$, which corrects the bias of the ordinary bootstrap proportion to second order.

The AU test is less conservative than the SH test while controlling the type I error in most situations, and is the recommended test of tree topologies in programs such as CONSEL and IQ-TREE.

**Example 21.7.1** For the ape mitochondrial proteins, the KH test (against the ML tree) rejects all trees at the $1\,\%$ level except ((human, gorilla), chimpanzees), with $p = 0.014$; ((chimpanzees, gorilla), human) has $p = 0.007$. The SH test gives $p = 0.781$ and $0.754$ for these two trees and fails to reject $27$ trees at the $1\,\%$ level. The data favor ((human, chimpanzees), gorilla) by about $35$ log-likelihood units, roughly two standard errors ($16.0$); the KH test overstates and the SH test understates the strength of this evidence.

![The selection bias of the KH test, in the large-sample normal approximation. The log-likelihoods of m candidate trees are treated as correlated normal variables (correlation 0.5, so that each difference between two trees has standard deviation 1), with the true tree as good as the others in expectation (the least favorable case, solid lines) or better by one standard deviation (dashed). The proportion of 100 000 simulated data sets in which the true tree is rejected at the one-sided 5 % level: the KH test applied against the tree with the highest likelihood rejects the true tree in 5 % of data sets when there are two trees but in more than half when there are 100, because the best of many trees beats the true one by chance; the SH test, which refers the observed difference to the distribution of the maximum, keeps the rate at or below 5 %, and is conservative when the true tree is in fact better](./plots/tree-tests.py)

### 21.7.4. Indices of Parsimony Analysis

Parsimony analyses report descriptive indices of the fit of characters to the tree, which have no statistical interpretation but appear in much of the literature.

**Definition 21.7.4 (Consistency Index)** For a character with minimum possible number of changes $m$ on any tree (the number of its states minus one) and $s$ changes on the given tree, the **consistency index** is $m/s$ (Kluge and Farris 1969); for a data set it is $\sum_im_i/\sum_is_i$. It equals $1$ when there is no homoplasy and decreases toward $0$ as homoplasy increases.

The *retention index*, $\sum_i(M_i - s_i)/\sum_i(M_i - m_i)$ with $M_i$ the maximum number of changes of character $i$ on any tree (Farris 1989), corrects the consistency index for uninformative characters, and the decay index (Bremer support) of a clade is the number of extra steps needed by the shortest tree without it. For molecular data the consistency index is a poor guide: it depends on the number of taxa and the divergence of the sequences, and it says little about whether the tree is right.

![The consistency index does not measure accuracy (after Yang 2014). Alignments of 500 sites are simulated under JC69 on the unrooted tree ((a:0.5, b:0.5):0.1, c:0.6, d:1.4) with all branches multiplied by a constant, so that the tree length varies along the x-axis; for 200 data sets per point, the probability that maximum parsimony recovers the true tree and the mean consistency index of the most parsimonious tree. The accuracy rises steeply, peaks at a tree length of about 0.2 to 1 and then declines as homoplasy accumulates; the consistency index stays near 0.95 throughout, because with four taxa most sites cannot show much homoplasy, and gives no indication of how often the tree is right](./plots/consistency-index.py)

## Summary

| Topic | Key points |
|---|---|
| Difficulties | homoplasy, long branches and rate variation, incomplete lineage sorting, horizontal transfer; hard trees have short internal and long scattered external branches; information peaks at intermediate divergence |
| Statistical framing | each topology is a model with its own parameters, so tree estimation is model selection; criteria: consistency, efficiency, robustness, speed, falsifiability |
| Distance criteria | least squares, Eq. (21.1), OLS/WLS/GLS (Example 21.2.1); minimum evolution (Definition 21.2.1) consistent with OLS branch lengths, not always with WLS/GLS; NJ is greedy balanced minimum evolution with Pauplin's tree length, Eq. (21.2) |
| Parsimony | weighted costs; inconsistent in the Felsenstein zone; ML = MP under the no-common-mechanism model (Theorem 21.3.1), ML → MP for short branches |
| Likelihood | consistent under an identifiable correct model via the KL divergence (Theorem 21.4.1); not asymptotically efficient for topology (Farris vs Felsenstein zone); robust to ts/tv and composition, sensitive to rate variation and heterotachy; root identifiable only with a clock or a nonreversible model; ape proteins: ML = MP = ME tree (Example 21.4.1); local optima and tree islands |
| Ancestral states | Definition 21.5.1; empirical Bayes marginal, Eq. (21.4), and joint reconstruction; agrees with parsimony for short equal branches; best-state reconstruction biases composition, posterior averaging does not |
| Model adequacy | multinomial $\ell_{\max}$ vs model, null by parametric bootstrap (Example 21.6.1) |
| Tests of trees | bootstrap = repeatability or approximate p-value, blind to bias; RELL; interior-branch test with boundary mixture; KH (Definition 21.7.1) valid only for trees fixed in advance; SH (Definition 21.7.2) conservative; AU (Definition 21.7.3) by multiscale bootstrap (Example 21.7.1) |
| Parsimony indices | consistency index (Definition 21.7.4), retention index, Bremer support: descriptive, not measures of accuracy |

## Questions

1. Why is the KH test invalid when one of the two trees is the ML tree estimated from the same data?

   **Answer** Under the null hypothesis of equal fit, $\delta = \ell_1 - \ell_2$ is symmetric about zero; but if $\tau_1$ is chosen because it has the highest likelihood, $\delta \ge 0$ by construction. The KH test ignores this selection and rejects other trees, including the true one, too often, the more so the more trees were searched (Figure). The SH test refers $\delta$ to the distribution of the maximum over the candidate set and keeps the error rate at or below the nominal level.

2. For four taxa with additive distances on $((a, b), (c, d))$, show that Pauplin's tree length, Eq. (21.2), equals the true tree length and is smaller than for the other two topologies.

   **Answer** With external branches summing to $X$ and internal branch $y$: $d_{ab} + d_{cd} = X$ and $d_{ac} + d_{ad} + d_{bc} + d_{bd} = 2X + 4y$, so $\hat L = \frac{1}{2}X + \frac{1}{4}(2X + 4y) = X + y$. For $((a, c), (b, d))$, $\hat L' = \frac{1}{2}(X + 2y) + \frac{1}{4}(2X + 2y) = X + \frac{3}{2}y$, larger by $y/2$; likewise for the third topology.

3. An ancestral protein reconstructed by taking the most probable amino acid at each site is richer in common amino acids than any living protein. Is this evidence of a compositional trend?

   **Answer** No. At ambiguous sites the common state wins more often than its posterior probability warrants, so best-state reconstructions exaggerate the stationary composition even under a stationary process (Section 21.5). Use the posterior expected composition, or sample ancestors from the posterior; only a trend that survives this (and a nonstationary model that fits better) is credible.

4. In the ape example the ML tree is better than the next tree by $35.0$ log-likelihood units with standard error $16.0$. Why are a bootstrap support of $99.4\,\%$ and an SH p-value of $0.78$ both possible?

   **Answer** The bootstrap (and the KH test) ask whether the winner, ahead by about $2.2$ standard errors, would win again in similar data: almost always. The SH test asks whether any tree of the candidate set could be true under the least favorable hypothesis that all fit equally well, and compares each with the maximum over the whole set, which is large when the set is large. The AU test is the appropriate test of whether a specific alternative is excluded.

5. (Open question) A clade with $100\,\%$ bootstrap support from $200$ nuclear genes conflicts with a well-established morphological clade. How would you investigate?

   **Answer** Full support from genome-scale data reflects only sampling variance, so look for systematic error: long branches joined in the clade, poor model fit (parametric bootstrap or posterior predictive tests, compositional heterogeneity), and robustness to richer models (partitions, profile mixtures, nonstationary models). Test the morphological topology with the AU test, and inspect per-gene log-likelihood differences: a conflict driven by a few genes or fast sites suggests artifact or hidden paralogy; one spread over many genes suggests real signal, possibly from incomplete lineage sorting or introgression ([7.10.25](/7.10.25)).
