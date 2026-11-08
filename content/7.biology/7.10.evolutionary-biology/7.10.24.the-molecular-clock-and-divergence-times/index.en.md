---
title: The Molecular Clock and Divergence Times
description: "The molecular clock hypothesis and its history; why rates differ among proteins and lineages; tests of the clock: relative rate tests, the likelihood ratio test with s − 2 degrees of freedom, the index of dispersion and their limits; likelihood dating under global and local clocks, rate smoothing and penalized likelihood, the problems of uncertain calibrations; dating with sampled tips and root-to-tip regression; Bayesian dating with autocorrelated and independent relaxed clocks, birth–death priors on times, soft-bound fossil calibrations and effective priors; the infinite-sites theory and plot; the fossilized birth–death process and tip dating."
---

A phylogeny tells the order of branching; dating it tells when. Times are needed to connect evolutionary history with the geological record ([7.10.29](/7.10.29)), with biogeography ([7.10.30](/7.10.30)), with rates of diversification ([7.10.31](/7.10.31)) and phenotypic change ([7.10.26](/7.10.26)), and with the epidemiology of viruses ([7.8.6](/7.8.6#sec-6.8.3)). Sequences do not measure time; they measure the amount of change, the product of rate and time. Dating therefore needs two ingredients beyond the data: a model of how rates vary across the tree, and external information, usually fossils, that fixes the absolute time scale. The simplest model, a constant rate, is the **molecular clock** ([Definition 23.7.1](/7.4.23#def-23.7.1)), introduced in [7.10.2](/7.10.2#sec-2.6.2) and explained by the neutral theory in [7.10.6](/7.10.6#sec-6.6).

This chapter treats the clock as a statistical hypothesis: how to test it, how to estimate times when it holds, how to relax it when it does not, and how to represent the uncertainty of fossil calibrations, which, as the infinite-sites theory shows, limits the precision of molecular dates however much sequence is available. The Bayesian machinery of [7.10.22](/7.10.22) and the coalescent of [7.10.7](/7.10.7) are used throughout.

## 24.1. The Molecular Clock Hypothesis

### 24.1.1. Origins

In the early 1960s, the first protein sequences from different species showed that the number of differences between species in hemoglobin (Zuckerkandl and Pauling 1962), cytochrome c (Margoliash 1963) and fibrinopeptides (Doolittle and Blombäck 1964) grew roughly in proportion to the time since their divergence. Zuckerkandl and Pauling (1965) proposed that proteins evolve at a roughly constant rate, an "evolutionary clock", and used it to date the duplications of the globin family. Three qualifications were understood from the start. The clock is stochastic: substitutions occur at random times, as a **Poisson process**, not at regular intervals. Each protein has its own clock: rates differ by orders of magnitude, from histones to fibrinopeptides ([7.10.6](/7.10.6#sec-6.6.1)), because functional constraint determines what fraction of mutations is neutral. And rate constancy may hold within a group, such as primates, but fail across distant groups.

**Example 24.1.1 (The α-Globin Clock)** The classic data are the α-globin chains of hemoglobin. Human α-globin differs from that of the shark at $74$ of $139$ comparable sites, $p = 0.532$. If substitutions at a site occur as a Poisson process and every substitution produces a new amino acid, the probability that a site shows no difference is $\mathrm{e}^{-K}$, where $K$ is the mean number of substitutions per site along the two lineages, so

$$
K = -\ln(1 - p), \qquad k = \frac{K}{2T},
$$
with $T$ the time since divergence and the factor 2 for the two lineages; this is the Poisson correction distance, the infinite-states limit of the Poisson model of [7.10.20](/7.10.20#sec-20.5.1). For human against shark $K = 0.759$, against carp ($p = 0.486$) $0.666$, newt $0.580$, chicken $0.286$, echidna $0.304$, kangaroo $0.212$ and dog $0.178$. Plotted against approximate fossil dates of the branch points (450 Mya for shark, 405 for carp, 350 for newt, 300 for chicken, 220 for echidna, 130 for kangaroo, 80 for dog), the distances fall close to a line through the origin, with $k \approx 0.8 \times 10^{-9}$ per site per year (figure, panel A); averaging all comparisons that span each branch point (shark against the seven others, carp against the six others, and so on) uses all the data and gives $k \approx 0.9 \times 10^{-9}$ (panel B). Only the chicken lies well below the line. The comparisons are always made with the human sequence not because humans are special but because every pair has evolved for the same time since its common ancestor: the human and the shark α-globin have both been evolving for 450 million years.

The same rate dates a gene duplication. The α and β chains, which form the $\alpha_2\beta_2$ tetramer of the hemoglobin of jawed vertebrates, descend from one duplication, and α and β of the same species differ at $p = 0.58$ in humans and $0.59$ in carp, $K \approx 0.87$–$0.89$. With $k \approx 0.87 \times 10^{-9}$, $T = K/(2k) \approx 500$ Mya, earlier than the split between sharks and bony vertebrates, consistent with the presence of both chains in all jawed vertebrates. (The shark's α and β differ more, $p = 0.67$, which would give about 640 Mya: rates and dates scatter by tens of percent, and such estimates are only approximate. The hemoglobins of lampreys and hagfishes, which function as monomers and dimers, evolved independently from another globin lineage.) Zuckerkandl and Pauling made calculations of exactly this kind to date the globin duplications.

![The α-globin clock (Example 24.1.1). Percent amino acid differences in α-globin among eight vertebrates (the classic table reproduced in Barton et al. (2007), Fig. 13.26), converted to Poisson distances K = −ln(1 − p) and plotted against approximate fossil dates of the branch points. A: human against each other species. B: each branch point, averaging all comparisons that span it, which uses every sequence. The dashed lines through the origin have slope 2k; the estimated rate k is about 0.8 to 0.9 × 10⁻⁹ substitutions per site per year. The chicken lies below the line; modern estimates of some branch points also differ from the classic ones (for example about 180 Mya for monotremes and 160 Mya for marsupials against placentals), but the approximate linearity remains](./plots/alpha-globin-clock.py)

:::

Clocklike evolution seemed incompatible with a selection-dominated view, since species as different as elephants and mice live under very different selective regimes; when the neutral theory was proposed, the clock became "perhaps the strongest evidence for the theory" (Kimura and Ohta 1971). If a fraction $f_0$ of mutations, at rate $\mu$, is neutral and the rest strongly deleterious, the substitution rate is the neutral mutation rate $\mu f_0$, independent of population size and environment ([Theorem 23.7.1](/7.4.23#thm-23.7.1)). The neutral theory, however, neither is the only explanation of a clock nor always predicts one: it predicts constancy per generation, and for nearly neutral mutations the rate depends on the effective population size ([7.10.6](/7.10.6#sec-6.6.2)).

### 24.1.2. Why Rates Differ among Lineages

Sequence comparisons since the 1980s have shown systematic differences among lineages: rodents evolve faster than primates, and apes, including humans, more slowly than monkeys (the primate and hominoid slowdowns). Proposed causes are generation time (more germ-line cell divisions per year in species with short generations), the efficiency of DNA repair, and metabolic rate; substitution rates in nuclear and mitochondrial genes decline with body size, from rodents through primates to whales (Martin and Palumbi 1993). Because small mammals tend to have short generations, high metabolic rates, short lives and large populations all at once, correlational analyses cannot separate these factors well (Bromham 2011). In plants, which lack a sequestered germ line, mutations may accumulate with somatic cell divisions, and trees and shrubs evolve more slowly than herbs. The evolutionary stopwatch of rates per generation in [7.6.20](/7.6.20#sec-20.4.2) gives the orders of magnitude.

These patterns define the models used below.

**Definition 24.1.1 (Strict Molecular Clock)** A **strict molecular clock** (global clock) is the model in which the substitution rate of a sequence, in substitutions per site per unit time, is the same on every branch of the tree. Under it the tree with branch lengths in expected substitutions is ultrametric: all tips are equally distant from the root, and the age of each node is its distance from the tips divided by the rate.

## 24.2. Testing the Clock

### 24.2.1. Relative Rate Tests

**Definition 24.2.1 (Relative Rate Test)** The **relative rate test** (Sarich and Wilson 1973) tests whether two species $A$ and $B$ have evolved at the same rate since their common ancestor $O$, using an outgroup $C$: under the clock the distances from $O$ to $A$ and to $B$ are equal, $a = b$, equivalently $d_{AC} = d_{BC}$. With distances counted as numbers of differences (Fitch 1976),

$$
a = \frac{d_{AB} + d_{AC} - d_{BC}}{2}, \qquad b = \frac{d_{AB} + d_{BC} - d_{AC}}{2}, \qquad X^2 = \frac{(a - b)^2}{a + b} \overset{H_0}{\approx} \chi^2_1. \tag{24.1}
$$

The statistic is equivalent to testing whether $a/(a + b)$ deviates from $1/2$ under a binomial model. It does not correct for multiple hits; Wu and Li (1985) used $d_{AC} - d_{BC}$ under the K80 model with its standard error, Tajima (1993) compared the counts $m_1$ and $m_2$ of the site patterns $xyy$ and $xyx$ (nucleotides of $A$, $B$, $C$) with $(m_1 - m_2)^2/(m_1 + m_2)$, which needs no substitution model, and Muse and Weir (1992) formulated it as a likelihood ratio test with one degree of freedom. If species 1 and 3 differ at 15 sites and species 2 and 3 at only 5, the lineage of species 1 has accumulated 10 more changes since it separated from species 2, and the clock is rejected for this gene in these species.

### 24.2.2. The Likelihood Ratio Test

For a rooted tree of $s$ species, the clock model has $s - 1$ parameters, the ages of the internal nodes measured in expected substitutions per site; the model without a clock has $2s - 3$, the branch lengths of the unrooted tree, because rate and time are confounded on each branch. The clock model is obtained by $s - 2$ equality constraints (each internal node equidistant from all its descendant tips), so (Felsenstein 1981)

$$
2\Delta\ell = 2(\ell_1 - \ell_0) \overset{H_0}{\approx} \chi^2_{s - 2}. \tag{24.2}
$$

No absolute dates are needed to test the clock.

**Example 24.2.1** The mitochondrial 12S rRNA genes of human, common chimpanzee, bonobo, gorilla, orangutan and gibbon (957 sites; Horai and colleagues 1995) were analyzed under K80: $\ell_0 = -2345.10$ with the clock (5 node ages), $\ell_1 = -2335.80$ without it (9 branch lengths). Then $2\Delta\ell = 18.60$ with $4$ degrees of freedom, $p < 0.001$: the clock is rejected (Yang 2014).

### 24.2.3. Limits of Clock Tests and the Index of Dispersion

The null hypothesis of these tests is not quite rate constancy but equidistance of the tips from the root. If the rate accelerated or slowed down in all lineages simultaneously, the tree would still be clocklike. Rate differences between the ingroup and the outgroup are not detected, and a constant rate cannot be distinguished from a variable rate with the same average along each lineage. Failure to reject may reflect lack of power, which is low for three species; with many species, on the other hand, the likelihood ratio test rejects the clock before the violation matters much for tree inference.

Earlier tests used the *index of dispersion* $R$, the ratio of the variance to the mean of the number of substitutions among lineages, which is 1 for a Poisson process on a star tree; values above 1, an overdispersed clock, were found for many mammalian proteins ([7.10.6](/7.10.6#sec-6.6.2)). The index was used mostly as a test of the neutral theory; it is sensitive to the assumed phylogeny (a star tree inflates $R$) and has been superseded by likelihood ratio tests with explicit models.

## 24.3. Likelihood Dating

### 24.3.1. The Global Clock

Under a strict clock with $c$ nodes of known age, the parameters are the rate $r$ and the ages of the other $s - 1 - c$ internal nodes; each branch length is $r$ times the duration of the branch, the likelihood is computed with **Felsenstein's pruning algorithm**, and it is maximized subject to the constraint that every node is older than its daughters. Uncertainty in the tree topology also affects dates; a well-supported binary tree is preferable to a consensus tree with polytomies, which represent ignorance rather than an estimate.

**Example 24.3.1 (Apes and Old World Monkeys)** Five genomic contigs (12–64 kb each) from human, chimpanzee, baboon (*Papio anubis*) and rhesus macaque (*Macaca mulatta*) (Steiper and colleagues 2004) do not reject the clock. Fixing the human–chimpanzee divergence at 7 Myr and the baboon–macaque divergence at 6 Myr, the likelihood estimates under HKY85+Γ are an age of $33.8$ Myr for the divergence of apes and Old World monkeys (95 % interval 32.4–35.2) and a rate of $6.6 \times 10^{-10}$ substitutions per site per year (Yang 2014, Table 10.1). The interval is far too narrow, because it treats the calibration ages as known exactly.

### 24.3.2. Local Clocks and Rate Smoothing

**Definition 24.3.1 (Local Clock)** A **local clock** model (Kishino and Hasegawa 1990; Rambaut and Bromham 1998; Yoder and Yang 2000) assigns the branches of a dated tree to a small number $k$ of rate classes specified in advance, with a strict clock within each class; it has $k - 1$ more parameters than the global clock.

With separate rates for apes and monkeys in Example 24.3.1, the root age hardly changes (33.3 Myr), while the ape rate ($5.4 \times 10^{-10}$) is lower than the monkey rate ($8.0 \times 10^{-10}$), the hominoid slowdown. Local clocks work when biology suggests which lineages differ; otherwise the assignment of branches to rates is arbitrary, and some assignments make the model unidentifiable.

Rate smoothing avoids prior assignment by assuming, following Gillespie (1991), that rates themselves evolve and are autocorrelated across the tree. Sanderson's penalized likelihood (2002) maximizes

$$
\ell(\boldsymbol{t}, \boldsymbol{r}) - \lambda\sum_k\bigl(r_k - r_{\mathrm{anc}(k)}\bigr)^2, \tag{24.3}
$$

the log likelihood of the data given times and branch rates minus a penalty on rate changes between each branch $k$ and its parent branch; the smoothing parameter $\lambda$ is chosen by cross-validation ($\lambda \to \infty$ gives the clock, $\lambda \to 0$ free rates). Such objective functions are not likelihoods in the usual sense, since the rates are unobserved random variables that should be integrated out, and their statistical properties are uncertain.

### 24.3.3. The Problem of Calibrations

Fossils rarely give the age of a node. The age of a fossil has measurement error, its placement on the tree may be wrong, and the oldest known fossil of a clade postdates its origin by an unknown amount: fossils give good minimum ages and seldom good maximum ages. Treating minimum ages as true ages biases all estimates, and using several of them together makes them inconsistent: if two nodes are truly 100 and 200 Myr old and fossils give minimum ages of 50 and 130 Myr, both constraints are correct, but treated as point calibrations they imply a ratio $1 : 2.6$ of the distances of the two nodes from the present instead of $1 : 2$. Allowing a calibrated age to vary between bounds in a likelihood analysis is not a remedy, because the model becomes unidentifiable: doubling all times and halving all rates fits the sequences equally well. Bootstrap intervals computed with fixed calibrations are equally misleading; with very long sequences their width tends to zero, although the uncertainty of the fossils remains. Uncertain calibrations need a probabilistic description, which the Bayesian approach provides (§24.4).

Geological events can also calibrate trees, for example the rise of the Isthmus of Panama about 2.7–3.5 Myr ago for marine species separated by it, but the timing of barriers and the possibility that populations separated before the barrier was complete raise similar problems. Volcanic archipelagos that form in sequence provide a natural test. The Hawaiian Islands arose one by one over a hot spot, from Kauai, about 5 Myr old, to the island of Hawaii, less than 0.5 Myr old; species endemic to a young island cannot be older than the island, and in *Drosophila*, honeycreepers and other Hawaiian groups the molecular dates of splits between species on different islands agree broadly with the ages of the islands, supporting the use of the clock, while the island ages themselves serve as calibrations for these groups.

### 24.3.4. Dating with Sampled Tips

Rapidly evolving viruses accumulate measurable change within years, so the dates at which sequences were sampled can calibrate the clock. Under a clock, sequences sampled later have had longer to diverge from the root. In the simplest case, if $a$ and $b$ are sampled at times $t_a < t_b$ and $c$ is an outgroup, the rate is estimated by $(d_{bc} - d_{ac})/(t_b - t_a)$.

**Definition 24.3.2 (Root-to-Tip Regression)** **Root-to-tip regression** is the regression of the distance from the root to each tip of a tree with estimated branch lengths (substitutions per site, the tree rooted, for example, at the position that maximizes the fit) on the sampling dates of the tips. Under a clock the relationship is linear: the slope estimates the substitution rate and the intercept with zero divergence estimates the date of the root; a weak correlation indicates a poor temporal signal or a violation of the clock.

The regression is an exploratory diagnostic, not a valid statistical test: the points share branches and are not independent, so its standard errors are wrong. Formal estimation uses likelihood (Rambaut 2000) or Bayesian methods with priors on genealogies of serially sampled sequences, such as the coalescent with dated tips (Rodrigo and Felsenstein 1999) or birth–death models with sampling through time (§24.5). Extrapolation is dangerous: samples spanning 50 years say little about events hundreds of years earlier, especially if the clock does not hold.

![Dating with sampling times (simulation). A: a genealogy of 40 virus sequences sampled between 1990 and 2020 under a serially sampled coalescent (constant population size), drawn on a time axis; substitutions accumulate along the branches under a strict clock of 2 × 10⁻³ substitutions per site per year in 1500 sites. B: root-to-tip regression: the number of substitutions per site from the root to each tip against its sampling date, with the least-squares line; its slope estimates the rate and its intercept with zero divergence the date of the root (dotted: true root date). The estimates are close but not exact, and the points are not independent, because tips share the branches near the root](./plots/root-to-tip.py)

## 24.4. Bayesian Dating

### 24.4.1. The Model

Bayesian dating (Thorne, Kishino and Painter 1998; Kishino, Thorne and Bruno 2001; Yang and Rannala 2006; Drummond and colleagues 2006) treats times $\boldsymbol{t}$ and branch rates $\boldsymbol{r}$ as unknowns with prior distributions. With substitution and prior parameters $\boldsymbol{\theta}$, the joint posterior is

$$
f(\boldsymbol{t}, \boldsymbol{r}, \boldsymbol{\theta} \mid X) \propto f(\boldsymbol{\theta})\,f(\boldsymbol{t} \mid \boldsymbol{\theta})\,f(\boldsymbol{r} \mid \boldsymbol{t}, \boldsymbol{\theta})\,f(X \mid \boldsymbol{t}, \boldsymbol{r}, \boldsymbol{\theta}), \tag{24.4}
$$

the product of the prior on times (which carries the fossil calibrations), the prior on rates (the clock model) and the sequence likelihood. It is sampled by **Markov chain Monte Carlo** ([3.5.9](/3.5.9), [7.10.22](/7.10.22)): node ages are updated one at a time within the limits set by parent and daughter nodes, rates and substitution parameters are updated, and a move that multiplies all times by a random factor near 1 and divides all rates by it lets the chain travel along the ridge of the likelihood, which is flat in that direction. For large data sets, the exact likelihood can be replaced by a multivariate normal approximation around the maximum likelihood branch lengths of the tree without a clock (Thorne and colleagues 1998), with a gradient term when some estimates are zero and preferably on transformed branch lengths (dos Reis and Yang 2011); the alignment is then not needed during the MCMC, and genome-scale dating becomes feasible.

### 24.4.2. Priors on Rates: Relaxed Clocks

**Definition 24.4.1 (Relaxed Molecular Clock)** A **relaxed molecular clock** is a prior distribution on the substitution rates of the branches of a dated tree that allows them to differ. In the *autocorrelated* (geometric Brownian motion) model, the logarithm of the rate drifts along the tree as **Brownian motion**: given the rate $r_{\mathrm{A}}$ at the ancestral node and a time $t$ to the descendant node,

$$
\ln r \sim \mathcal{N}\bigl(\ln r_{\mathrm{A}} - \tfrac12\nu t,\ \nu t\bigr), \tag{24.5}
$$

the correction $-\frac12\nu t$ making $\mathbb{E}[r] = r_{\mathrm{A}}$, with $\nu$ measuring how fast rates drift (Thorne and colleagues 1998). In the *independent-rates* model, the rate of each branch is drawn independently from a common distribution, for example the **log-normal distribution** with mean $\mu$,

$$
\ln r \sim \mathcal{N}\bigl(\ln\mu - \tfrac12\sigma^2,\ \sigma^2\bigr), \tag{24.6}
$$

with $\sigma^2$ measuring the departure from a clock (Drummond and colleagues 2006; Rannala and Yang 2007).

![Relaxed clocks: rates drawn on a dated tree of 12 species (root age 100 Myr). Top: autocorrelated rates (geometric Brownian motion, Eq. (24.5), ν = 0.006 per Myr, root rate 1, rate taken at the midpoint of each branch); bottom: independent log-normal rates (Eq. (24.6), σ² = 0.3). Left: the chronogram, with branch lengths in time and branches colored by rate. Right: the corresponding phylogram, with branch lengths equal to rate times time, which is what the sequences estimate. Under autocorrelation related lineages share slow or fast rates, so whole clades are compressed or stretched; under independent rates neighboring branches vary independently and the phylogram is ragged](./plots/rates.py)

Autocorrelation fits the idea that rates depend on heritable traits such as generation time, which change gradually; independence fits episodic changes. Bayes factors comparing the two have given conflicting results, and since the two models differ only in the prior, the more relevant question is how sensitive the time estimates are to the choice. Because the rates of different loci are modeled as independent trajectories while their divergence times are shared, analyzing many loci jointly lets them "borrow information": a branch that is long at one locus and short at others is more probably fast at that locus than old.

### 24.4.3. Priors on Times and Fossil Calibrations

**Definition 24.4.2 (Fossil Calibration)** A **fossil calibration** is a prior probability distribution for the age of a node of the tree, derived from the fossil record (or from dated geological events), which converts relative times into absolute times. It usually combines a minimum age, the age of the oldest fossil securely assigned to the clade, with a less certain maximum age; *hard* bounds give zero density outside an interval, while *soft* bounds leave a small probability (often 2.5 %) beyond each bound (Yang and Rannala 2006).

The prior on the ages of the other nodes is specified conditionally on the calibrated ones. A convenient family is the **birth–death process** with species sampling (Rannala and Yang 1996): with birth rate $\lambda$, death rate $\mu$ and sampling fraction $\rho$, the ages of the $s - 2$ non-root internal nodes, given the root age $t_1$, are distributed as the order statistics of $s - 2$ independent draws from a kernel density on $(0, t_1)$; for $\lambda = \mu$,

$$
g(t) = \frac{1 + \rho\lambda t_1}{t_1(1 + \rho\lambda t)^2}, \qquad 0 < t < t_1, \tag{24.7}
$$

which is uniform when $\rho = 0$. Changing the parameters changes the shape of the tree, from star-like (nodes near the root) to trees with long internal branches, so the sensitivity of the dates to the time prior can be explored. The prior of all times is then $f(\boldsymbol{t}) = f_{\mathrm{BD}}(\boldsymbol{t}_{-C} \mid \boldsymbol{t}_C)f(\boldsymbol{t}_C)$, the calibration densities of the calibrated ages $\boldsymbol{t}_C$ times the conditional density of the rest; simply multiplying calibration densities by a Yule density of all ages does not follow the rules of probability (Heled and Drummond 2012).

![Calibration densities. A: four ways of turning fossil information into a prior on the age t of a node: a soft minimum (t > 50 Myr, with 2.5 % below and a heavy-tailed decline above), soft minimum and maximum bounds (flat between 50 and 70 Myr with 2.5 % in each tail), a gamma density with 95 % of its probability between 50 and 70 Myr, and a soft maximum (t < 70 Myr, 2.5 % above). B: the effective prior: independent gamma calibrations specified for a node (mean 60, sd 8 Myr) and its daughter node (mean 55, sd 8 Myr); because a node must be older than its daughter, only the region t₁ > t₂ is sampled, and the marginal priors actually used (solid) differ from the specified ones (dashed): the two ages are pushed apart](./plots/calibrations.py)

Calibration densities specified for individual nodes are not the priors actually used: the constraint that each node be older than its descendants truncates their joint distribution, and the resulting *effective prior* can differ markedly from the intended one (Inoue, Donoghue and Yang 2010; figure above). The effective prior should always be examined by running the analysis without sequence data.

### 24.4.4. The Limit of Precision: the Infinite-Sites Theory

In conventional estimation, more data shrink the posterior to a point. In dating they do not: sequences determine distances (rate × time), not times and rates separately, and the posterior remains sensitive to the prior however long the alignment.

**Theorem 24.4.1 (Infinite-Sites Limit under a Clock)** Under a strict clock with rate $r$ and node ages $t_1, \dots, t_{s - 1}$, let the sequence length tend to infinity, so that the distances $d_j = rt_j$ from the nodes to the present are known exactly. Then the posterior of $r$ is

$$
f(r \mid d_1, \dots, d_{s - 1}) \propto g(r)\,f_t\Bigl(\frac{d_1}{r}, \dots, \frac{d_{s - 1}}{r}\Bigr)r^{1 - s}, \tag{24.8}
$$

where $g$ is the prior on the rate and $f_t$ the prior on times, and every node age is a fixed multiple of any other, $t_j = (d_j/d_k)t_k$. The posterior of the times is concentrated on a line, so posterior means, quantiles and credible-interval widths of all nodes are proportional to the distances $d_j$ (Yang and Rannala 2006; Rannala and Yang 2007).

**Proof** Change variables from $(r, t_1, \dots, t_{s - 1})$ to $(r, d_1, \dots, d_{s - 1})$ with $d_j = rt_j$; the **Jacobian determinant** of the inverse map $t_j = d_j/r$ is $r^{1 - s}$, so the joint density of $(r, \boldsymbol{d})$ is $g(r)f_t(\boldsymbol{d}/r)r^{1 - s}$. Conditioning on the known $\boldsymbol{d}$ gives Eq. (24.8), and $t_j = d_j/r$ is then a deterministic function of the single random variable $r$, proportional to $d_j$. $\square$

Thus with infinite data the uncertainty is that of a single scale factor, determined by the calibrations. With a single calibration and a vague rate prior, the posterior of the calibrated age is essentially its prior; several calibrations pool information and are each sharpened by the others.

**Definition 24.4.3 (Infinite-Sites Plot)** The **infinite-sites plot** (Inoue, Donoghue and Yang 2010; dos Reis and Yang 2013) is the plot of the width $w$ of the 95 % credible interval of each node age against its posterior mean $t$. A line through the origin with $R^2$ near 1 indicates that the sequence data are effectively infinite and the remaining uncertainty is due to the calibrations, quantified by the slope (Myr of interval width per Myr of age); scatter about the line indicates that more sequence data would still sharpen the estimates.

![The infinite-sites plot (simulation of Theorem 24.4.1). Five nodes evolving under a strict clock have true ages 5, 10, 20, 40 and 80 Myr; the 20 Myr node carries a uniform calibration on (16, 26) Myr. Data on n sites give Poisson numbers of substitutions from each node to the present (rate 10⁻⁹ per site per year); with vague priors the posterior of each distance is gamma, the posterior of the calibrated age equals its prior, and each age is obtained by scaling. A: credible-interval width against posterior mean for 10⁴, 10⁵ and 10⁷ sites, with lines through the origin; as n grows the points fall exactly on a line whose slope is set by the calibration alone. B: the credible-interval width of the 80 Myr node against n approaches the infinite-data limit (dashed) and hardly changes beyond about 10⁵ sites](./plots/infinite-sites.py)

For six primates with an alignment of 8.7 million sites (first and second codon positions of 14,631 genes), the infinite-sites plot is a perfect line, $w = 0.322t$ with $R^2 = 1.000$: each million years of divergence adds 0.32 Myr to the interval, and more sequence would not help. For 36 mammals with the mitochondrial protein-coding genes (7260 sites), $w = 0.204t$ but $R^2 = 0.516$: these data are far from the limit (dos Reis and Yang 2013). With finite data, the posterior variance consists of a calibration part and a part that decreases as $1/n$, so the interval width approaches its limit at rate $1/n$. Under relaxed clocks, the limit is reached only when both the number of loci and their lengths grow; the number of loci matters most, so partitioned analyses are important.

### 24.4.5. Molecular Dates and the Fossil Record

The Bayesian analysis of the ape–monkey data of Example 24.3.1, with soft bounds of 5–8 Myr on both calibrated nodes, gives root ages of 32–34 Myr under the global clock and both relaxed clocks, but with credible intervals of about 24–46 Myr under independent rates, far wider than the likelihood intervals and honest about the fossil uncertainty (Yang 2014, Table 10.1). For 36 mammals with mitochondrial genes and 24 minimum and 14 maximum fossil bounds, the clock is rejected and the autocorrelated model estimates a mean rate of 0.16 (0.091–0.28) substitutions per site per $10^8$ years and $\nu = 0.61$ (0.37–0.97), indicating substantial rate variation among lineages. For the great apes, an analysis of about 60 kb of sequence calibrated by four fossil dates placed the human–chimpanzee split at about 6.6 (6.0–7.0) Myr and the divergence from gorilla at 8.6 (7.7–9.2) Myr; estimates from whole genomes calibrated by human mutation rates gave about 6 and 10 Myr (Futuyma and Kirkpatrick 2017). Pedigree-based mutation rates, lower than those inferred from fossils, imply older dates, a discrepancy that is not fully resolved (Yang 2014; see also Example 25.2.1).

Molecular dates have repeatedly been older than the fossil record: for the animal phyla, which appear in a burst in the early Cambrian about 500–540 Myr ago but whose molecular divergences were estimated much earlier ([7.10.29](/7.10.29)), and for the orders of placental mammals and birds, which radiated after the end-Cretaceous extinction 66 Myr ago. Part of the gap is expected, because fossils record when a lineage became morphologically recognizable and preserved, after it became genetically separate; part came from early methods with strict clocks and point calibrations. Analyses that integrate many genes, relaxed clocks and carefully justified calibrations (Meredith and colleagues 2011; dos Reis and colleagues 2012) agree much better with the fossil record, and the interaction has improved both the interpretation of fossils and the methods.

## 24.5. Fossils as Data: Tip Dating and the Fossilized Birth–Death Process

Node calibrations use fossils indirectly, through the judgment of the researcher who turns them into densities, and use only the oldest fossil of each clade. The alternative is to model the fossils themselves.

**Definition 24.5.1 (Fossilized Birth–Death Process)** The **fossilized birth–death process** (Stadler 2010; Heath, Huelsenbeck and Stadler 2014) is a model of a phylogeny in which lineages speciate at rate $\lambda$ and go extinct at rate $\mu$, each lineage leaves fossils at rate $\psi$ while it exists, and living species are sampled with probability $\rho$. Fossils appear in the tree as dated tips or as sampled ancestors on branches, so the prior on the tree and divergence times is derived from the same process that produced the fossils.

Combined with a model of morphological evolution (the Mk model of [7.10.26](/7.10.26)) for characters scored on fossil and living species, the process allows *tip dating* (total-evidence dating; Pyron 2011; Ronquist and colleagues 2012): fossils are placed in the tree by their characters and dated by their stratigraphic ages, with uncertainty in both, and molecular data from living species are analyzed together with them. The same idea with sampling through time, in birth–death–sampling models for viral sequences (Stadler 2010; Stadler and colleagues 2012), links the dated phylogeny to epidemiological parameters such as the **basic reproduction number** of an epidemic. These approaches make explicit what node calibrations hide in their priors, but they depend on models of fossil preservation and morphological evolution that are themselves simple.

## Summary

| Topic | Result |
|---|---|
| clock hypothesis | rates of proteins roughly constant in time (Zuckerkandl and Pauling 1965); stochastic, gene-specific, locally valid; neutral explanation ([Theorem 23.7.1](/7.4.23#thm-23.7.1)) |
| lineage effects | generation time, repair, metabolic rate, body size; primate and hominoid slowdowns; strict clock: ultrametric tree (Definition 24.1.1) |
| tests | relative rate test, Eq. (24.1) (Definition 24.2.1); likelihood ratio test with $s - 2$ df, Eq. (24.2) (Example 24.2.1); index of dispersion; tests check equidistance of tips only |
| likelihood dating | global clock (Example 24.3.1); local clocks (Definition 24.3.1); penalized likelihood, Eq. (24.3); point or bounded calibrations ignore or cannot handle fossil uncertainty |
| tip dates | root-to-tip regression: slope = rate, intercept = root date (Definition 24.3.2); diagnostic only |
| Bayesian dating | posterior Eq. (24.4); relaxed clocks, autocorrelated Eq. (24.5) or independent Eq. (24.6) (Definition 24.4.1); birth–death time prior Eq. (24.7); soft-bound calibrations (Definition 24.4.2); effective priors |
| precision | infinite data fix only distances; times lie on a line (Theorem 24.4.1, Eq. (24.8)); infinite-sites plot $w \propto t$ (Definition 24.4.3); primates $w = 0.322t$, $R^2 = 1$ |
| fossils and molecules | molecular dates older than fossils (Cambrian, K–Pg radiations), partly expected, partly methodological |
| fossils as data | fossilized birth–death process, tip dating (Definition 24.5.1); birth–death–sampling models for viruses |

## Questions

1. With $d_{AB} = 130$, $d_{AC} = 150$ and $d_{BC} = 100$ differences ($C$ the outgroup), apply Fitch's relative rate test.

   **Answer** Eq. (24.1): $a = 90$, $b = 40$, $X^2 = 50^2/130 = 19.2 > 3.84$: the lineage of $A$ evolved faster.

2. How many degrees of freedom has the likelihood ratio test of the clock for 10 species, and what does a non-significant result show?

   **Answer** $s - 2 = 8$ ($9$ node ages against $17$ branch lengths). It shows only that the tips are not detectably unequal in distance from the root; simultaneous rate changes in all lineages, or lack of power, are not excluded.

3. Why do two correct fossil minima used as fixed calibrations bias the dates?

   **Answer** They fix the ratio of the two node distances at the ratio of the minima (for true ages 100 and 200 and minima 50 and 130, $1 : 2.6$ instead of $1 : 2$), so rates and all other ages are fitted to contradictory constraints. Bayesian dating uses calibration densities instead and propagates their uncertainty.

4. Under a strict clock with infinite data, the human–chimpanzee node has a $\mathrm{U}(6, 8)$ calibration and the gorilla node is 1.3 times farther from the present. What is the posterior of the gorilla node?

   **Answer** By Theorem 24.4.1 its age is $1.3$ times the calibrated age, whose posterior is about its prior: roughly $\mathrm{U}(7.8, 10.4)$ Myr, a width of 2.6 Myr that no amount of sequence reduces.

5. Sequences sampled in 2000 and 2020 lie 0.010 and 0.050 substitutions per site from the root. Estimate the rate and root date.

   **Answer** Rate $0.040/20 = 0.002$ per site per year; root $0.010/0.002 = 5$ years before 2000, about 1995. The estimate is doubtful if root-to-tip points scatter widely or if it extrapolates far beyond the sampling window.
