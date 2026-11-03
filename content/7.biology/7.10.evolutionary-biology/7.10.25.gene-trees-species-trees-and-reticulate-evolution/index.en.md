---
title: Gene Trees, Species Trees and Reticulate Evolution
description: "Why gene trees differ from the species tree: incomplete lineage sorting, duplication and loss, introgression and horizontal transfer; the multispecies coalescent, coalescent units, the density of a gene tree within a species tree, the three-species mismatch probability, anomalous gene trees and the anomaly zone; estimating species trees by concatenation, summary methods and full-likelihood Bayesian methods; gene flow: the isolation-with-migration model, the ABBA–BABA D statistic, phylogenetic networks; Bayesian species delimitation and what it delimits."
---

A phylogeny built from one gene is the history of that gene. Since [7.8.6](/7.8.6#sec-6.1.3) and [7.10.2](/7.10.2#sec-2.5.2) we have distinguished the **gene tree** from the **species tree**, and [7.10.7](/7.10.7#sec-7.9) showed with Eq. (7.14) that the coalescent alone makes them differ when speciation events follow each other quickly. With genome-scale data this is no longer a nuisance at the margins: in great apes, cichlid fishes, birds and many other groups, a large fraction of loci have gene trees that disagree with the species tree, and the disagreement itself carries information about ancestral population sizes, the timing of speciation and gene flow.

This chapter develops the theory and methods. It explains where discordance comes from (§25.1), models it by the multispecies coalescent (§25.2), uses the model to estimate species trees (§25.3), extends it to gene flow between species and to networks (§25.4), and applies it to the question of how many species a sample contains (§25.5). The coalescent results are those of [7.10.7](/7.10.7); the Bayesian computation is that of [7.10.22](/7.10.22); the computation of $f$-statistics from genotype data is in [7.8.13](/7.8.13#sec-13.3.3).

## 25.1. Why Gene Trees Differ from Species Trees

### 25.1.1. Three Sources of Discordance

When a species splits, the gene copies of the ancestral population are divided between the daughters. A gene tree follows these copies backward until they coalesce, and three processes make its branching differ from that of the species (Maddison 1997; Nichols 2001):

- **Incomplete lineage sorting** ([7.8.6](/7.8.6#sec-6.1.3)). Ancestral polymorphism persists through a speciation event, so the copies from the two most closely related species can find their common ancestor further back than a copy from a more distant species. It needs no special event, only short intervals between speciations relative to the effective population size.
- *Gene duplication and loss.* If a gene was duplicated before a speciation and different copies were lost in different lineages, the surviving genes compared as **orthologs** are in fact **paralogs**, and their tree reflects the duplication rather than the speciation (hidden paralogy; [7.10.18](/7.10.18#sec-18.1.1)).
- *Gene flow.* **Introgression** after hybridization ([7.10.12](/7.10.12)) and **horizontal gene transfer** ([7.8.6](/7.8.6#sec-6.8.2)) give parts of a genome the history of another species.

The first is the null expectation of population genetics and is modeled in §25.2; the third is modeled in §25.4; the second is handled by gene-tree reconciliation and orthology assignment, and is usually excluded by analyzing single-copy genes.

![Gene trees inside a species tree. The species tree ((A, B), C) is drawn as tubes, whose width stands for population size, with one gene copy sampled from each species and time running upward. A: the lineages of A and B coalesce within their common ancestral population AB, and the gene tree matches the species tree. B: they fail to coalesce within AB; in the ancestral population ABC the first coalescence happens to join A and B, and the gene tree again matches. C: they fail to coalesce within AB and the first coalescence in ABC joins B and C, producing the discordant gene tree (A, (B, C)): incomplete lineage sorting. Under the coalescent the three pairs are equally likely to coalesce first in ABC, so each discordant tree has probability (1/3)e^{−T} for an internal branch of T coalescent units](./plots/embedded.py)

### 25.1.2. Discordance in Real Genomes

Discordance is common in rapid radiations (Futuyma and Kirkpatrick 2017). Six loci sequenced from four closely related species of *Melanoplus* grasshoppers each show gene lineages persisting through one or more speciation events, yet together they yield a good estimate of the species tree. Among placental mammals, a phylogeny based on about 20 million bases from 14,632 genes confirms most relationships but leaves several unresolved, such as which two of bats, carnivores and perissodactyls are closest relatives, because these lineages diverged within a short time. The cichlids of Lake Victoria, which produced more than 450 species in about the last 15,000 years, have such rampant incomplete lineage sorting that their relationships could be resolved only with several million bases of sequence.

Introgression adds discordance of a different kind. In three *Anopheles* mosquitoes that transmit malaria, *A. gambiae*, *A. arabiensis* and *A. melas*, gene trees of 10 kb windows conflict along the whole genome: on the left arm of chromosome 3, $92\,\%$ of windows group *A. gambiae* with *A. arabiensis*. Gene trees on the X chromosome are deeper, and they are taken to reflect the history of speciation, which makes *A. melas* and *A. arabiensis* sister species; the autosomal majority reflects later hybridization (Futuyma and Kirkpatrick 2017). The lesson is general: the most common gene tree is not necessarily the species tree, and the regions of the genome that resist gene flow can be more informative about speciation than the genome-wide majority.

## 25.2. The Multispecies Coalescent

### 25.2.1. The Model

**Definition 25.2.1 (Multispecies Coalescent)** The **multispecies coalescent** (Takahata 1989; Rannala and Yang 2003) is the probability model for the genealogy of gene copies sampled from several species related by a species tree with divergence times $\tau$ and a population size for every extant and ancestral species. Within each branch of the species tree, the lineages present coalesce backward in time according to the **coalescent** with the population size of that branch; lineages from different species can coalesce only in a common ancestral population; after a split there is complete isolation. Gene trees at unlinked, nonrecombining loci are independent given the species tree.

**Definition 25.2.2 (Coalescent Unit)** A **coalescent unit** is a length of time equal to $2N_{\mathrm{e}}$ generations of the population concerned, so a branch of $t$ generations has length $T = t/(2N_{\mathrm{e}})$, the scale on which two lineages coalesce at rate 1 ([Definition 7.2.1](/7.10.7#def-7.2.1)). If times and population sizes are measured in expected mutations per site, $\tau = \mu t$ and $\theta = 4N_{\mathrm{e}}\mu$, then $T = 2\tau/\theta$.

Coalescent units are the natural measure of the length of species-tree branches for discordance: a branch is "short" when it lasts a fraction of $2N_{\mathrm{e}}$ generations, however many years that is. Measuring time in mutations per site, two lineages in a population with parameter $\theta$ coalesce at rate $2/\theta$. If $m$ lineages enter a population of duration $\tau$ and $n$ leave it, with waiting times $t_j$ while there are $j$ lineages, the contribution of that population to the density of the gene tree is

$$
\prod_{j = n + 1}^{m}\frac{2}{\theta}\exp\Bigl(-\frac{j(j - 1)}{\theta}t_j\Bigr) \times \exp\Bigl(-\frac{n(n - 1)}{\theta}\Bigl[\tau - \sum_{j = n + 1}^{m}t_j\Bigr]\Bigr), \tag{25.1}
$$

the rate of each coalescence times the probability of no further coalescence before the population ends; the factor $j(j - 1)/2$ of the waiting-time density cancels with the probability $2/(j(j - 1))$ of the particular pair that coalesces. The density $f(G_i, \boldsymbol{t}_i \mid \Theta)$ of the gene tree $G_i$ with coalescence times $\boldsymbol{t}_i$ at locus $i$ is the product of Eq. (25.1) over all populations of the species tree (Rannala and Yang 2003). Because the coalescent process of a population may stop before all its lineages have coalesced, it is also called the censored coalescent. With alignments $X_i$ at $L$ loci,

$$
f(X \mid \Theta) = \prod_{i = 1}^{L}\sum_{G_i}\int f(G_i, \boldsymbol{t}_i \mid \Theta)\,f(X_i \mid G_i, \boldsymbol{t}_i)\,\mathrm{d}\boldsymbol{t}_i, \tag{25.2}
$$

where $f(X_i \mid G_i, \boldsymbol{t}_i)$ is the phylogenetic likelihood computed by **Felsenstein's pruning algorithm**. The sum and integral over gene trees are intractable except for very few sequences per locus, so Eq. (25.2) is used in a Bayesian framework with MCMC over the gene trees of all loci, as in the program BPP (Rannala and Yang 2003; Yang and Rannala 2010).

### 25.2.2. Three Species

For species tree $((A, B), C)$ with one sequence from each species, the probability that the gene tree differs from the species tree is (Hudson 1983; Nei 1987)

$$
P_{\mathrm{SG}} = \frac23\mathrm{e}^{-T} = \frac23\exp\Bigl(-\frac{t_{ABC} - t_{AB}}{2N_{AB}}\Bigr), \tag{25.3}
$$

the probability $\mathrm{e}^{-T}$ that $A$ and $B$ fail to coalesce in their ancestral population times the probability $2/3$ that the first coalescence in the common ancestor of all three joins a wrong pair (Eq. (7.14)). It depends only on the internal branch in coalescent units, not on the age of the speciation events: if two splits are separated by $N_{AB}$ generations ($T = 1/2$), $40\,\%$ of the genome has a discordant gene tree, even if the species diverged hundreds of millions of years ago (Edwards and colleagues 2005). Incomplete lineage sorting in deep, rapid radiations leaves permanent marks in genomes instead of "sorting out" with time, and sampling more individuals per species does not help, since their lineages coalesce long before they reach the short deep branch; only more loci help.

![Gene trees under the multispecies coalescent. A: three species with species tree ((A, B), C): the probability that the rooted gene tree of one sequence per species matches the species tree, 1 − (2/3)e^{−T}, and the probability of each of the two discordant gene trees, (1/3)e^{−T}, against the internal branch length T in coalescent units (lines), with simulated frequencies (dots). B: the anomaly zone for four species with the asymmetric species tree (((A, B), C), D), whose two internal branches have lengths x (the younger) and y (the older) in coalescent units. In the shaded region, the symmetric gene tree ((A, B), (C, D)) is more probable than the gene tree matching the species tree (exact probabilities computed by enumerating the coalescent histories); the line is the boundary y = a(x) derived by Degnan and Rosenberg (2006)](./plots/msc.py)

Equating $P_{\mathrm{SG}}$ with the observed proportion of discordant loci gives an estimate of the ancestral population size (the mismatch method), but errors in the estimated gene trees inflate the apparent discordance and hence the estimate; full-likelihood methods avoid this (Yang 2002).

**Example 25.2.1 (Hominoid Ancestral Populations)** BPP was applied to 14,663 autosomal loci (mean length 508 bp) from human (H), chimpanzee (C), gorilla (G) and orangutan (O), one sequence per species, under a clock (Burgess and Yang 2008; Yang 2014, Table 9.1). The posterior means, in mutations per kb, were $\theta_{\mathrm{HC}} = 6.0$, $\theta_{\mathrm{HCG}} = 3.5$ and $\theta_{\mathrm{HCGO}} = 8.1$ for the ancestral populations, and $\tau_{\mathrm{HC}} = 4.1$, $\tau_{\mathrm{HCG}} = 6.6$ and $\tau_{\mathrm{HCGO}} = 13.8$ for the divergences. The ancestral populations were much larger than that of modern humans ($\theta \approx 0.6$ per kb). The internal branch of the human–chimpanzee ancestor lasts $T = 2(6.6 - 4.1)/6.0 = 0.83$ coalescent units, so Eq. (25.3) predicts $P_{\mathrm{SG}} = \frac23\mathrm{e}^{-0.83} = 0.29$: close to the $30\,\%$ of the genome in which humans are not closest to chimpanzees. With a mutation rate of $10^{-9}$ per site per year, the divergence times are about 4.1 Myr (human–chimpanzee) and 6.6 Myr (with gorilla); the lower rates measured in pedigrees, $0.5$–$0.6 \times 10^{-9}$ per year, would make them much older, a conflict with the fossil-calibrated dates of [7.10.24](/7.10.24#sec-24.4.5) that is not yet resolved.

### 25.2.3. Anomalous Gene Trees

With three species, the gene tree that matches the species tree is always the most probable. With four or more, this can fail.

**Definition 25.2.3 (Anomaly Zone)** A rooted gene tree topology is *anomalous* for a species tree with given branch lengths if it differs from the species tree topology and has a higher probability under the multispecies coalescent than the topology that matches the species tree. The **anomaly zone** is the set of species-tree branch lengths for which anomalous gene trees exist (Degnan and Rosenberg 2006).

Consider the asymmetric species tree $(((A, B), C), D)$ with three speciation events so close in time that all coalescences of one sequence per species happen in the common ancestor of all four. The coalescent then makes all 18 **labeled histories** (rooted trees with the order of their internal nodes) equally probable. The asymmetric topology $(((A, B), C), D)$ corresponds to one labeled history, but the symmetric topology $((A, B), (C, D))$ to two (the pairs can coalesce in either order), so the symmetric gene tree has probability about $2/18$ against $1/18$ for the matching tree: the most frequent gene tree is wrong. For four species, anomalous gene trees occur only for the asymmetric species tree; for five or more, for every species tree topology with suitable branch lengths (Degnan and Rosenberg 2006). In practice, gene trees estimated in the anomaly zone are more often unresolved than resolved wrongly, because such short branches carry few mutations (Huang and Knowles 2009), but the theory shows that "majority vote" of gene trees is not a consistent estimator of the species tree.

## 25.3. Estimating Species Trees

### 25.3.1. Concatenation

**Definition 25.3.1 (Concatenation)** **Concatenation** (supermatrix analysis) estimates a species tree by joining the alignments of many loci into one alignment and analyzing it with a single tree, possibly with partition-specific substitution models, as if all loci shared one genealogy.

Concatenation uses all the sequence information and is usually accurate when internal branches are long in coalescent units. But it models discordance as rate heterogeneity, which it is not, and it can be statistically inconsistent, converging to a wrong tree as loci are added, in and near the anomaly zone (Kubatko and Degnan 2007); because the data set is large, the wrong tree can receive very high bootstrap or posterior support. In simulations with incomplete lineage sorting, coalescent-based methods outperformed concatenation (Leaché and Rannala 2011).

### 25.3.2. Summary Methods

Summary methods first estimate a gene tree for every locus and then combine them. Some use only topologies: minimizing deep coalescences (Maddison 1997), gene-tree parsimony, pseudo-likelihood on rooted triplets (MP-EST), and methods based on quartets. The quartet approach has a convenient property: for unrooted gene trees of four species, the topology matching the species tree is always the most probable, so there are no anomalous unrooted quartets, and the species tree that agrees with the largest number of quartets induced by the gene trees is a consistent estimator under the multispecies coalescent. This is the principle of ASTRAL (Mirarab and colleagues 2014), widely used for phylogenomic data ([7.8.6](/7.8.6#sec-6.1.3)). Others also use branch lengths: if all populations have the same size, the maximum likelihood species tree given rooted gene trees with node ages is the tree with the largest divergence times compatible with all gene trees (Liu and colleagues 2010).

Summary methods are fast and scale to thousands of loci and taxa, but they treat estimated gene trees as known. Loci from closely related species carry few informative sites, their gene trees are poorly resolved, and gene-tree estimation error becomes the main source of error; methods using topologies alone also cannot estimate all parameters of the model (with three species, only $(\tau_{ABC} - \tau_{AB})/\theta_{AB}$ is identifiable).

### 25.3.3. Full-Likelihood Methods

Bayesian methods compute the posterior of the species tree $S$ and its parameters from the alignments directly,

$$
f(S, \Theta \mid X) \propto f(S, \Theta)\prod_{i = 1}^{L}\sum_{G_i}\int f(G_i, \boldsymbol{t}_i \mid S, \Theta)\,f(X_i \mid G_i, \boldsymbol{t}_i)\,\mathrm{d}\boldsymbol{t}_i, \tag{25.4}
$$

with MCMC over species trees, gene trees and parameters (BEST, Liu and Pearl 2007; \*BEAST, Heled and Drummond 2010; BPP). They account for uncertainty in the gene trees and use branch lengths as well as topologies, so they are consistent in the anomaly zone and efficient with weakly informative loci, but they are computationally demanding: proposals for species divergence times are constrained by all gene trees (genes must split before species), which slows mixing, and is eased by moves that change species and gene trees together. For unlinked SNPs, gene trees can be integrated out analytically (SNAPP; Bryant and colleagues 2012). A different approach, Bayesian concordance analysis, estimates for each clade its *concordance factor*, the proportion of the genome for which it is true; in great apes the clade (human, chimpanzee) has a concordance factor of about $70\,\%$, the two alternatives about $15\,\%$ each.

**Example 25.3.1 (Fence Lizards)** The *Sceloporus undulatus* species group of North American fence lizards is a recent radiation. A mitochondrial gene and 29 nuclear loci from 21 specimens of nine species (Leaché 2009) showed weakly resolved and conflicting gene trees and four events of mitochondrial introgression at contact zones between species. After removing the specimens with introgressed mitochondria, coalescent-based Bayesian analyses of eight nuclear loci still recovered many clades of the species tree with high posterior probability, and BPP estimated population sizes of about 2–4 mutations per kb and a root age of about 4.6 mutations per kb (95 % interval 3.5–5.5), the latter robust and the former sensitive to their priors (Yang 2014).

## 25.4. Gene Flow between Species

### 25.4.1. The Isolation-with-Migration Model

**Definition 25.4.1 (Isolation-with-Migration Model)** The **isolation-with-migration model** (IM model; Nielsen and Wakeley 2001; Hey and Nielsen 2004) is a multispecies coalescent model in which species, after splitting, continue to exchange migrants at constant rates. For two species it has six parameters: the population sizes $\theta_1$, $\theta_2$ of the two species and $\theta_{\mathrm{A}}$ of their ancestor, the divergence time $\tau$, and the scaled migration rates $M_{12} = N_2m_{12}$ and $M_{21} = N_1m_{21}$, where $m_{ij}$ is the proportion of individuals in population $j$ that are immigrants from $i$ per generation, so $M_{ij}$ is the expected number of immigrants into $j$ per generation.

Backward in time, lineages switch between populations by migration and coalesce within them, the **structured coalescent** of [Definition 7.6.1](/7.10.7#def-7.6.1) confined to the period after the split. For two sequences the history is a Markov chain with states $S_{11}$, $S_{12}$, $S_{22}$ (both lineages in population 1, one in each, both in 2) and $S_1$, $S_2$ (coalesced, ancestor in population 1 or 2). With time in mutations per site and $m_1 = 4M_{21}/\theta_1$, $m_2 = 4M_{12}/\theta_2$ the per-lineage backward migration rates into the other population, its rate matrix is (Hobolth and colleagues 2011)

$$
Q = \begin{pmatrix}
-2(m_1 + 1/\theta_1) & 2m_1 & 0 & 2/\theta_1 & 0\\
m_2 & -(m_1 + m_2) & m_1 & 0 & 0\\
0 & 2m_2 & -2(m_2 + 1/\theta_2) & 0 & 2/\theta_2\\
0 & 0 & 0 & -m_1 & m_1\\
0 & 0 & 0 & m_2 & -m_2
\end{pmatrix}, \tag{25.5}
$$

and with $P(t) = \mathrm{e}^{Qt}$ and initial state $a$, the density of the coalescence time of the two sequences is

$$
f(t) = \begin{cases}
P_{aS_{11}}(t)\dfrac{2}{\theta_1} + P_{aS_{22}}(t)\dfrac{2}{\theta_2}, & t < \tau,\\[2ex]
\bigl[P_{aS_{11}}(\tau) + P_{aS_{12}}(\tau) + P_{aS_{22}}(\tau)\bigr]\dfrac{2}{\theta_{\mathrm{A}}}\mathrm{e}^{-2(t - \tau)/\theta_{\mathrm{A}}}, & t \ge \tau,
\end{cases} \tag{25.6}
$$

which integrates out the migration history; the likelihood of a pair of sequences depends only on $t$. Such calculations make maximum likelihood feasible for thousands of loci from two or three genomes (Zhu and Yang 2012). With many sequences per locus, MCMC must average over the number, times and directions of migration events, which is very slow; heuristic implementations use migration bands (Gronau and colleagues 2011), and introgression as discrete pulses can be modeled with hybridization nodes in the species tree (the multispecies coalescent with introgression; Flouri and colleagues 2020).

![Coalescence times under the isolation-with-migration model, Eqs. (25.5) and (25.6): two species with θ₁ = θ₂ = 0.005, ancestral θ_A = 0.003 and divergence time τ = 0.005 (mutations per site), exchanging M = 0.01, 0.1, 1 or 10 migrants per generation in each direction. A: two sequences from the same species. B: one sequence from each species; without migration they cannot coalesce before τ (dotted line), while with frequent migration (M = 10) the density approaches that of a single population and the divergence time leaves little trace](./plots/im.py)

### 25.4.2. The D Statistic

**Definition 25.4.2 (D Statistic)** For four populations or species related by the tree $(((P_1, P_2), P_3), O)$, with the outgroup $O$ carrying the ancestral allele A at biallelic sites, let $n_{\mathrm{ABBA}}$ be the number of sites at which $P_2$ and $P_3$ share the derived allele B (pattern ABBA for $P_1 P_2 P_3 O$) and $n_{\mathrm{BABA}}$ the number at which $P_1$ and $P_3$ share it. The **D statistic** (ABBA–BABA test; Green and colleagues 2010; Durand and colleagues 2011) is

$$
D = \frac{n_{\mathrm{ABBA}} - n_{\mathrm{BABA}}}{n_{\mathrm{ABBA}} + n_{\mathrm{BABA}}}, \tag{25.7}
$$

its standard error being computed by a block jackknife over large genomic blocks.

Under the multispecies coalescent without gene flow, ABBA and BABA patterns arise only from the two discordant gene trees $((P_2, P_3), P_1)$ and $((P_1, P_3), P_2)$, which are equally probable (Eq. (25.3)), so $\mathbb{E}[D] = 0$ however much incomplete lineage sorting there is. Gene flow between $P_3$ and $P_2$ makes $((P_2, P_3), P_1)$ more common and $D > 0$; gene flow between $P_3$ and $P_1$ makes $D < 0$. With population allele frequencies $p_i$ of B and the outgroup fixed for A, the expected difference per site is proportional to $\mathbb{E}[(1 - p_1)p_2p_3 - p_1(1 - p_2)p_3] = \mathbb{E}[(p_2 - p_1)p_3]$, which equals $-f_4(P_1, P_2; P_3, O)$ when $p_O = 0$: the numerator of $D$ is the $f_4$-statistic of [7.8.13](/7.8.13#sec-13.3.3) in site-pattern form. The test detected the contribution of Neanderthals to the genomes of non-Africans ($D > 0$ for $P_1$ African, $P_2$ non-African, $P_3$ Neanderthal; [7.10.33](/7.10.33)).

![The D statistic (simulation). Species tree (((P1, P2), P3), O) with P1 and P2 splitting 0.5 and P3 1.0 coalescent units ago; at time 0.2 a fraction f of the genome of P2 is replaced by genes from P3. For each of 20 000 unlinked loci a gene tree is simulated under the multispecies coalescent and mutations fall on its branches as a Poisson process; a derived allele on the branch ancestral to P2 and P3 alone gives the pattern ABBA, on the branch ancestral to P1 and P3 alone BABA. A: the numbers of ABBA and BABA sites against f; without introgression they are equal, because incomplete lineage sorting produces the two discordant gene trees equally often. B: D with 95 % intervals from a block jackknife over 20 blocks of 1000 loci; D departs from zero as soon as f > 0](./plots/dstat.py)

The test has limits. Structure in the ancestral population (subdivision persisting through the splits) can also make $D \neq 0$ without gene flow after speciation; $D$ does not tell the direction or timing of gene flow; and as an estimator of the proportion of introgression it is biased, since it depends on the amount of incomplete lineage sorting, which is why related statistics such as the admixture fraction estimated from $f_4$ ratios are used for quantification ([7.8.13](/7.8.13#sec-13.3.3)).

### 25.4.3. Networks

**Definition 25.4.3 (Reticulate Evolution)** **Reticulate evolution** is evolution in which lineages that have diverged exchange genes or merge, by hybridization and introgression, **hybrid speciation**, allopolyploidy or horizontal gene transfer, so that the history of the organisms is not a tree.

**Definition 25.4.4 (Phylogenetic Network)** A **phylogenetic network** is a rooted directed acyclic graph whose leaves are the taxa, in which ordinary internal nodes have one parent and *reticulation* (hybrid) nodes have two; each reticulation node carries an inheritance probability $\gamma$, the proportion of the genome inherited from one of its parents. Under the multispecies network coalescent, each locus follows one of the parents of each reticulation node with probabilities $\gamma$ and $1 - \gamma$ and then coalesces as in a species tree.

Networks combine incomplete lineage sorting and hybridization in one model, and the inheritance probabilities and the placement of reticulations are estimated by likelihood or Bayesian methods from gene trees or sequences (implemented in programs such as PhyloNet and SNaQ); identifiability is a serious problem, since different networks can predict the same distribution of gene trees. The three hybrid species of sunflowers of [7.10.2](/7.10.2#sec-2.5.1) are reticulation nodes in such a network. In prokaryotes, horizontal transfer is so frequent that a network, or a tree of the most stably inherited genes with transfers mapped onto it, is a better description than any single tree ([7.10.27](/7.10.27)).

## 25.5. Species Delimitation

**Definition 25.5.1 (Species Delimitation)** **Species delimitation** is the inference, from data on a sample of individuals, of how many species the sample contains and which individuals belong to each; it differs from species identification, the assignment of a specimen to one of several known species.

Delimitation depends on what species are taken to be ([7.10.11](/7.10.11#sec-11.1)). Under the **biological species concept** species are groups of interbreeding populations reproductively isolated from others; under genealogical versions of the **phylogenetic species concept** they are basal exclusive groups, recognized in practice when gene trees show reciprocal monophyly at most loci. Genetic data are used because they are numerous and track divergence faithfully, and because they can reveal **cryptic species**.

Simple methods use thresholds on divergence (the "10× rule", requiring mitochondrial divergence between species at least ten times the polymorphism within them), reciprocal monophyly of a mitochondrial gene tree, or the generalized mixed Yule–coalescent (GMYC), which locates on a single dated gene tree the time at which branching switches from a speciation (Yule) pattern to a coalescent pattern. All ignore errors in gene-tree estimation, and reciprocal monophyly also ignores incomplete lineage sorting, which is expected even between good species; in simulations it has low power.

Bayesian species delimitation under the multispecies coalescent (Yang and Rannala 2010) compares delimitation models by reversible-jump MCMC on Eq. (25.4). The user assigns individuals to populations and gives a guide tree for the populations; the algorithm splits and joins internal nodes of the guide tree, each model having its own divergence times and population sizes, and estimates the posterior probability of each delimitation. The results depend on the guide tree (a wrong guide tree can cause over-splitting), on the priors for $\theta$ and $\tau$, and on gene flow. When two species exchange migrants, the posterior probability of two species changes rapidly around $M = Nm \approx 1$: below about $0.1$ migrants per generation two species are inferred with good power, above about 10 a single species (Zhang and colleagues 2011), the same threshold that separates differentiated from homogenized populations in [7.10.10](/7.10.10).

The method infers population divergence with no or little gene flow, which is a necessary but not a sufficient condition for species status: it may split allopatric populations that have diverged neutrally but are not reproductively isolated, and it cannot distinguish isolation by geography from intrinsic isolation. It therefore delimits genetic structure, which may or may not correspond to species; integrating ecological, morphological and reproductive evidence remains necessary (Sukumaran and Knowles 2017).

## Summary

| Topic | Result |
|---|---|
| discordance | incomplete lineage sorting, duplication and loss, introgression and horizontal transfer; common in radiations (grasshoppers, mammals, cichlids), introgression in *Anopheles* |
| multispecies coalescent | coalescent within each species-tree branch, complete isolation after splits (Definition 25.2.1); coalescent units $T = t/2N_{\mathrm{e}} = 2\tau/\theta$ (Definition 25.2.2); gene-tree density Eq. (25.1), likelihood Eq. (25.2) |
| three species | $P_{\mathrm{SG}} = \frac23\mathrm{e}^{-T}$, Eq. (25.3); depends on the internal branch only; hominoids $\approx 0.3$ (Example 25.2.1) |
| anomaly zone | wrong gene tree most probable (Definition 25.2.3); four asymmetric species: symmetric gene tree $2/18$ vs $1/18$; any shape for five or more |
| species-tree estimation | concatenation can be inconsistent (Definition 25.3.1); quartet summary methods (ASTRAL) consistent but ignore gene-tree error; full-likelihood Bayesian methods, Eq. (25.4) (Example 25.3.1) |
| gene flow | IM model (Definition 25.4.1), Markov chain of two lineages, Eqs. (25.5)–(25.6); $D$ statistic, Eq. (25.7) (Definition 25.4.2), numerator $\propto -f_4$ |
| networks | reticulate evolution (Definition 25.4.3), phylogenetic networks with inheritance probabilities (Definition 25.4.4) |
| species delimitation | Definition 25.5.1; thresholds and monophyly are unreliable; Bayesian delimitation on a guide tree; transition near $Nm \approx 1$; delimits structure, not necessarily species |

## Questions

1. Using the estimates of Example 25.2.1, compute the length of the internal branch of the human–chimpanzee ancestor in coalescent units and the expected proportion of loci with a discordant gene tree.

   **Answer** $T = 2(\tau_{\mathrm{HCG}} - \tau_{\mathrm{HC}})/\theta_{\mathrm{HC}} = 2(6.6 - 4.1)/6.0 = 0.83$; by Eq. (25.3), $P_{\mathrm{SG}} = \frac23\mathrm{e}^{-0.83} = 0.29$, split equally between the two discordant trees.

2. Why is the most frequent rooted gene tree an inconsistent estimator of the species tree for four or more species, while the quartet method is consistent?

   **Answer** In the anomaly zone a discordant rooted topology (for four asymmetric species, the symmetric one, with two labeled histories against one) is more probable than the matching topology, so majority vote converges to it. For unrooted four-taxon gene trees the matching quartet is always the most probable, so choosing the species tree that agrees with most quartets converges to the truth.

3. A genome comparison finds 1200 ABBA and 1000 BABA sites. Compute $D$. What else is needed before concluding that gene flow occurred, and between which species?

   **Answer** $D = 200/2200 = 0.091$. A block-jackknife standard error is needed (sites are linked); if $D$ is significantly positive, the excess points to gene flow between $P_3$ and $P_2$, although ancestral population structure is an alternative explanation, and $D$ alone does not give the direction or timing.

4. Why can concatenating hundreds of loci give a wrong species tree with 100 % bootstrap support?

   **Answer** Concatenation assumes one genealogy for all loci. When incomplete lineage sorting is extensive (short internal branches in coalescent units), the combined data can favor a tree that differs from the species tree, and the bootstrap measures only sampling variation of sites under this misspecified model, which shrinks as data are added; the support therefore grows while the error remains.

5. Two populations exchange about 1 migrant per generation. What does Bayesian species delimitation tend to infer, and why does the answer not settle whether they are species?

   **Answer** Near $Nm \approx 1$ the posterior of the two-species model is intermediate and sensitive to the data and priors; with fewer migrants it favors two species, with many it favors one. The model detects reduced gene flow and population divergence, not reproductive isolation, so the result must be combined with evidence on isolation, ecology and morphology.
