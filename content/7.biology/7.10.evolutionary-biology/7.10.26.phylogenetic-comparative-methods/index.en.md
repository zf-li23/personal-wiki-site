---
title: Phylogenetic Comparative Methods
description: "Comparative data and the phylogeny: why species are not independent; Brownian motion on a tree and the phylogenetic covariance matrix; Felsenstein's independent contrasts and phylogenetic generalized least squares, and their equivalence; phylogenetic signal (Pagel's λ, Blomberg's K) and phylogenetic niche conservatism; the Ornstein–Uhlenbeck model of stabilizing selection towards optima; the Mk model, ancestral state reconstruction and tests of correlated evolution of discrete characters; rates of phenotypic evolution in darwins and haldanes and their dependence on the time interval."
---

Many questions in evolutionary biology are answered by comparing species: whether a trait is an adaptation to an environment, whether two traits evolve together, how fast phenotypes change, what an extinct ancestor was like. The **comparative method** ([Definition 3.5.1](/7.10.3#def-3.5.1)) infers adaptation from repeated, independent evolution of a feature in lineages exposed to the same selective factor. Its central difficulty was noted there: species are not independent data points, because related species share features by descent. This chapter gives the statistical models that turn a phylogeny into the covariance structure of comparative data, and the methods built on them.

The models are stochastic processes on trees. Continuous characters are modeled by **Brownian motion** (§26.2; the physics is in [7.6.5](/7.6.5)) and by the Ornstein–Uhlenbeck process (§26.5), which adds stabilizing selection towards an optimum ([7.10.9](/7.10.9#sec-9.2)); discrete characters by continuous-time Markov chains (§26.6), the same mathematics as the substitution models of [7.10.20](/7.10.20). The phylogeny with branch lengths, usually a dated tree from [7.10.24](/7.10.24), is taken as known; in practice the uncertainty in it can be propagated by repeating the analysis over a posterior sample of trees ([7.10.22](/7.10.22)). The methods of this chapter are the basis of the analyses of diversification and macroevolution in [7.10.31](/7.10.31) and [7.10.32](/7.10.32).

## 26.1. Species Are Not Independent

Most birds fly and all lay eggs; most mammals do not fly and most give birth to live young. Across species, flight and egg-laying are strongly correlated, but this hardly suggests a functional link: the ancestor of birds flew and laid eggs, the ancestor of therian mammals did neither, and their thousands of descendants inherited both conditions (Futuyma and Kirkpatrick 2017). The correlation rests on essentially one evolutionary event in each lineage, not on thousands of independent observations.

Felsenstein (1985) made the statistical point with a worst case. Suppose two traits evolve independently on a tree made of two clades that separated early and then radiated. Each clade drifts to its own region of trait space, so a scatter plot of species values shows two clouds, and an ordinary regression across species finds a strong correlation with an apparently tiny $p$-value; yet the data contain only one independent comparison at the deepest level, plus comparisons within clades that show nothing. Treating species as independent inflates the effective sample size and the rate of false positives (figure below). The remedy is to model the covariance that the phylogeny induces, which requires a model of trait evolution.

![Why species are not independent data (after Felsenstein 1985). Two traits X and Y evolve by independent Brownian motions on a tree of 20 species consisting of two clades of 10 that separated at the root and radiated in the last fifth of the tree's height. A: one simulated data set; within each clade there is no association, but because the clades drifted apart early, ordinary least squares across species finds a strong and highly significant correlation. B: over 2000 data sets simulated with no correlation, the proportion of tests rejecting a zero slope at the 5 % level: ordinary least squares on species values, independent contrasts (Algorithm 26.3.1, regression through the origin of the 19 contrasts) and phylogenetic generalized least squares (Definition 26.3.1) with the Brownian covariance matrix. The last two give identical slopes (Theorem 26.3.2) and hold the nominal error rate](./plots/pic.py)

## 26.2. Brownian Motion on a Phylogeny

**Definition 26.2.1 (Brownian Motion Model)** In the **Brownian motion model** of a continuous character, the character value $X(t)$ along each lineage changes by independent normal increments, $X(t + h) - X(t) \sim \mathcal{N}(0, \sigma^2h)$, with *rate* $\sigma^2$ (variance per unit time); at a speciation event both daughter lineages start from the value of the ancestor and evolve independently thereafter (Edwards and Cavalli-Sforza 1964; Felsenstein 1973, 1985).

The model describes random drift of the mean of a polygenic trait in a population of constant size ([7.10.6](/7.10.6)), for which $\sigma^2 = h^2V_P/N_{\mathrm{e}}$ per generation (Lande 1976), but also selection whose direction changes randomly and frequently; in comparative studies it is used as a neutral baseline, not as a statement that the trait is neutral.

**Theorem 26.2.1 (Tip Values under Brownian Motion)** Let a rooted tree with $n$ tips have branch lengths in units of time, and let the character start at value $a$ at the root. Under the Brownian motion model the vector $\boldsymbol{X}$ of tip values is multivariate normal,

$$
\boldsymbol{X} \sim \mathcal{N}_n(a\boldsymbol{1}, \sigma^2C), \qquad C_{ij} = \text{length of the path shared by tips } i \text{ and } j \text{ from the root}, \tag{26.1}
$$

so $C_{ii}$ is the distance from the root to tip $i$ and $C_{ij}$ the distance from the root to the most recent common ancestor of $i$ and $j$.

**Proof** $X_i - a$ is the sum of the increments along the branches from the root to tip $i$; these increments are independent normals with variances $\sigma^2$ times the branch lengths, so $X_i$ is normal with mean $a$ and variance $\sigma^2C_{ii}$, and any linear combination of tip values is also a sum of independent normal increments, so $\boldsymbol{X}$ is multivariate normal. For $i \neq j$, the increments on the shared path enter both $X_i$ and $X_j$, while those on the separate paths are independent of everything else, so $\operatorname{Cov}(X_i, X_j) = \sigma^2C_{ij}$. $\square$

The matrix $C$ is the *phylogenetic covariance matrix* of the tree. The log likelihood is that of a multivariate normal, and its maximizers are

$$
\hat a = \frac{\boldsymbol{1}^{\mathsf T}C^{-1}\boldsymbol{x}}{\boldsymbol{1}^{\mathsf T}C^{-1}\boldsymbol{1}}, \qquad \hat\sigma^2 = \frac{(\boldsymbol{x} - \hat a\boldsymbol{1})^{\mathsf T}C^{-1}(\boldsymbol{x} - \hat a\boldsymbol{1})}{n}, \tag{26.2}
$$

the generalized least squares estimate of the root state and the weighted residual variance (with $n - 1$ in the denominator for the restricted maximum likelihood estimate). The root estimate $\hat a$ is the ancestral state reconstruction of a continuous character at the root; its variance $\sigma^2/(\boldsymbol{1}^{\mathsf T}C^{-1}\boldsymbol{1})$ is usually large, since ancestral values of continuous characters are poorly determined by living species alone.

![Brownian motion on a phylogeny. A: a trait evolving by Brownian motion (σ² = 1 per unit time, starting at 0) along a dated tree of eight species, drawn as a traitgram (trait value against time): lineages share their path until they split and wander independently afterwards (grey: internal branches; blue: terminal branches). B: the phylogenetic covariance matrix C of the eight tips (Theorem 26.2.1): C_ij is the length of the path from the root shared by tips i and j; the root-to-tip length is 1. C: over 5000 simulations, the empirical covariance of each pair of tip values against the shared path length, with the prediction σ²C_ij (line)](./plots/bm.py)

## 26.3. Independent Contrasts and Phylogenetic Regression

### 26.3.1. Felsenstein's Contrasts

The differences between sister species are independent of the history before their split. Felsenstein (1985) turned this into an algorithm that transforms $n$ correlated tip values into $n - 1$ independent contrasts.

**Algorithm 26.3.1 (Phylogenetically Independent Contrasts)** Given a rooted binary tree with branch lengths and a value $x_i$ at every tip, repeat until only the root remains:

1. choose two tips $i$ and $j$ that are sisters, with branch lengths $v_i$ and $v_j$ to their common ancestor $k$;
2. compute the standardized contrast $u_k = (x_i - x_j)/\sqrt{v_i + v_j}$;
3. assign to $k$ the value $x_k = (x_i/v_i + x_j/v_j)/(1/v_i + 1/v_j)$ and lengthen the branch above $k$ by $v_iv_j/(v_i + v_j)$; remove $i$ and $j$, so that $k$ becomes a tip.

The output is the set of $n - 1$ **phylogenetically independent contrasts** $u_k$, one per internal node.

**Theorem 26.3.1 (Contrasts Are Independent)** Under the Brownian motion model with rate $\sigma^2$, the $n - 1$ standardized contrasts are independent, each distributed as $\mathcal{N}(0, \sigma^2)$, whatever the value at the root.

**Proof** Consider the first step. Given the value $y_k$ at node $k$, $x_i$ and $x_j$ are independent with variances $\sigma^2v_i$ and $\sigma^2v_j$ and both have mean $y_k$, so $x_i - x_j \sim \mathcal{N}(0, \sigma^2(v_i + v_j))$, and $u_k \sim \mathcal{N}(0, \sigma^2)$ independently of $y_k$, hence of everything outside the clade. The weighted mean $x_k$ equals $y_k$ plus an error with variance $\sigma^2v_iv_j/(v_i + v_j)$, and the error is uncorrelated with $x_i - x_j$: with weights $w_i = v_j/(v_i + v_j)$ and $w_j = v_i/(v_i + v_j)$, $\operatorname{Cov}(w_ix_i + w_jx_j, x_i - x_j \mid y_k) = \sigma^2(w_iv_i - w_jv_j) = 0$, and uncorrelated jointly normal variables are independent. So after the step, node $k$ behaves as a tip with a value that has evolved by Brownian motion along a branch lengthened by $v_iv_j/(v_i + v_j)$, independent of $u_k$, and the argument repeats. $\square$

Because contrasts are differences, a regression of the contrasts of $Y$ on those of $X$ is fitted through the origin; their sign is arbitrary, provided the same order is used for both traits. The slope estimates the evolutionary regression of $Y$ on $X$, and $\sum_ku_k^2/(n - 1)$ is an unbiased estimate of $\sigma^2$. Contrasts also serve as diagnostics: if the model fits, their absolute values should not depend on the length of the branches from which they were computed or on the estimated node values.

### 26.3.2. Phylogenetic Generalized Least Squares

**Definition 26.3.1 (Phylogenetic Generalized Least Squares)** **Phylogenetic generalized least squares** (PGLS; Grafen 1989) fits the linear model $\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ for species values, with residuals $\boldsymbol{\varepsilon} \sim \mathcal{N}_n(\boldsymbol{0}, \sigma^2V)$ whose covariance $V$ is derived from the phylogeny and a model of evolution ($V = C$ under Brownian motion, or the matrices of Eqs. (26.3) and (26.7)), by **generalized least squares** ([Definition 12.1.3](/3.3.12#def-12.1.3)):

$$
\hat{\boldsymbol{\beta}} = (X^{\mathsf T}V^{-1}X)^{-1}X^{\mathsf T}V^{-1}\boldsymbol{y}, \qquad \operatorname{Cov}(\hat{\boldsymbol{\beta}}) = \sigma^2(X^{\mathsf T}V^{-1}X)^{-1}.
$$

PGLS is a general linear model, so it accommodates several predictors, categorical predictors and interactions; the residuals, not the traits themselves, are assumed to evolve along the tree. It is the phylogenetic counterpart of the models for correlated errors in repeated measures and the animal model of quantitative genetics ([7.7.17](/7.7.17)), with the tree in place of a pedigree or a grouping structure.

**Theorem 26.3.2 (Contrasts and PGLS Agree)** For a single predictor, the slope of the regression through the origin of the contrasts of $Y$ on those of $X$ equals the PGLS slope of $Y$ on $X$ (with an intercept) under the Brownian covariance $C$.

**Proof** Contrasts are linear in the tip values, $\boldsymbol{u} = A\boldsymbol{x}$ for an $(n - 1) \times n$ matrix $A$ determined by the tree. They do not depend on the root value, so $A\boldsymbol{1} = \boldsymbol{0}$, and by Theorem 26.3.1 $ACA^{\mathsf T} = I_{n - 1}$. The PGLS slope with an intercept is $\boldsymbol{x}^{\mathsf T}M\boldsymbol{y}/\boldsymbol{x}^{\mathsf T}M\boldsymbol{x}$ with $M = C^{-1} - C^{-1}\boldsymbol{1}\boldsymbol{1}^{\mathsf T}C^{-1}/(\boldsymbol{1}^{\mathsf T}C^{-1}\boldsymbol{1})$, the matrix that removes the generalized least squares mean. Let $\boldsymbol{w} = C^{-1/2}\boldsymbol{1}$. Then $C^{1/2}MC^{1/2} = I - \boldsymbol{w}\boldsymbol{w}^{\mathsf T}/(\boldsymbol{w}^{\mathsf T}\boldsymbol{w})$ is the orthogonal projection onto the complement of $\boldsymbol{w}$. The rows of $AC^{1/2}$ are orthonormal ($ACA^{\mathsf T} = I$) and orthogonal to $\boldsymbol{w}$ ($AC^{1/2}\boldsymbol{w} = A\boldsymbol{1} = \boldsymbol{0}$), so they are an orthonormal basis of that $(n - 1)$-dimensional complement, and $C^{1/2}A^{\mathsf T}AC^{1/2}$ is the same projection. Hence $A^{\mathsf T}A = M$, and the contrast slope $(A\boldsymbol{x})^{\mathsf T}(A\boldsymbol{y})/(A\boldsymbol{x})^{\mathsf T}(A\boldsymbol{x})$ equals the PGLS slope. $\square$

The simulation in the figure of §26.1 confirms the identity numerically and shows that both methods hold the nominal type I error rate, while ordinary regression across species rejected a true null hypothesis in more than half of the data sets.

## 26.4. Phylogenetic Signal

**Definition 26.4.1 (Phylogenetic Signal)** **Phylogenetic signal** is the tendency of related species to resemble one another more than species drawn at random from the same tree (Blomberg and Garland 2002). It is measured relative to the expectation under Brownian motion.

Two measures are standard. *Pagel's λ* (Pagel 1999) multiplies the off-diagonal elements of $C$ by a factor $\lambda$,

$$
C(\lambda)_{ij} = \begin{cases} C_{ii}, & i = j,\\ \lambda C_{ij}, & i \neq j, \end{cases} \tag{26.3}
$$

which shortens the internal branches relative to the terminal ones: $\lambda = 1$ is Brownian motion, $\lambda = 0$ a star tree, under which species are independent; $\lambda$ is estimated by maximum likelihood (with $a$ and $\sigma^2$ maximized analytically as in Eq. (26.2)) and tested against 0 and 1 by likelihood ratio tests. It is also used in PGLS to let the residual covariance depart from Brownian motion. *Blomberg's K* (Blomberg, Garland and Ives 2003) compares the observed ratio of the mean squared error of the tip values about $\hat a$ to the mean squared error computed with the phylogenetic covariance with its expectation under Brownian motion:

$$
K = \frac{(\boldsymbol{x} - \hat a\boldsymbol{1})^{\mathsf T}(\boldsymbol{x} - \hat a\boldsymbol{1})\big/(\boldsymbol{x} - \hat a\boldsymbol{1})^{\mathsf T}C^{-1}(\boldsymbol{x} - \hat a\boldsymbol{1})}{\bigl[\operatorname{tr}C - n/(\boldsymbol{1}^{\mathsf T}C^{-1}\boldsymbol{1})\bigr]/(n - 1)}. \tag{26.4}
$$

$K \approx 1$ indicates the signal expected under Brownian motion, $K < 1$ less (related species more different than expected), $K > 1$ more; its significance is assessed by permuting the tip values.

![Measuring phylogenetic signal. Traits were simulated on a random ultrametric tree of 50 species under Pagel's λ model, Eq. (26.3). A: the profile log likelihood of λ for one data set simulated with each of λ = 0, 0.5 and 1 (true values dotted; dashed: 1.92 below the maximum, the approximate 95 % interval); 50 species locate λ only roughly. B: Blomberg's K, Eq. (26.4), over 500 data sets simulated under each λ: near 1 and variable under Brownian motion, much smaller when the species are nearly independent](./plots/signal.py)

High signal is often interpreted as evidence of constraint or of "phylogenetic inertia", and low signal as evidence of adaptation, but neither inference is safe: under Brownian motion signal is high however fast the trait evolves, and strong stabilizing selection towards a common optimum (§26.5) erases signal while keeping the trait nearly constant. Signal describes a pattern; the process requires explicit models.

In ecological traits, high signal is the expression of phylogenetic niche conservatism:

**Definition 26.4.2 (Phylogenetic Niche Conservatism)** **Phylogenetic niche conservatism** is the retention over long periods of evolutionary time, by related species, of much the same resources and environmental conditions, so that their ecological niches are more similar than expected from their divergence (Futuyma and Kirkpatrick 2017; Wiens and Graham 2005).

It shows in habitat tracking, the shift of geographic distributions with the habitats to which species are adapted, as in molluscs that kept the same temperature regime through the climatic changes of the last 3 million years, and in conservative diets: the larvae of all butterflies of the tribe Heliconiini feed on plants of the passionflower family, apparently since the tribe originated in the Oligocene. Gene flow between populations in the ancestral and in a new niche, with a trade-off between adaptations to the two, keeps selection in favor of the ancestral state, and the loss of unused genes can make a reversal unlikely ([7.10.32](/7.10.32)). Niche conservatism shapes geographic patterns of diversity ([7.10.30](/7.10.30)).

## 26.5. Stabilizing Selection: the Ornstein–Uhlenbeck Model

**Definition 26.5.1 (Ornstein–Uhlenbeck Model)** In the **Ornstein–Uhlenbeck model** of trait evolution (Felsenstein 1988; Hansen 1997), the trait follows the **Ornstein–Uhlenbeck process** ([Definition 5.4.3](/7.6.5#def-5.4.3))

$$
\mathrm{d}X = \alpha(\theta - X)\,\mathrm{d}t + \sigma\,\mathrm{d}B \tag{26.5}
$$

along each lineage, where $B$ is standard Brownian motion, $\theta$ the optimum, $\alpha \ge 0$ the strength of the pull towards it and $\sigma^2$ the rate of stochastic change. Given $X(0) = x_0$,

$$
\mathbb{E}[X(t)] = \theta + (x_0 - \theta)\mathrm{e}^{-\alpha t}, \qquad \operatorname{Var}(X(t)) = \frac{\sigma^2}{2\alpha}\bigl(1 - \mathrm{e}^{-2\alpha t}\bigr). \tag{26.6}
$$

The mean approaches the optimum with *phylogenetic half-life* $\ln 2/\alpha$, and the variance approaches the stationary value $\sigma^2/(2\alpha)$ instead of growing without bound. With $\alpha = 0$ the model reduces to Brownian motion.

The biological interpretation comes from quantitative genetics. A population under Gaussian stabilizing selection with width $\omega^2$ ([Formula 9.2.1](/7.10.9#fml-9.2.1)) and phenotypic variance $V_P$ has its mean moved towards the optimum by a fraction $h^2V_P/(\omega^2 + V_P)$ of its distance per generation, by the **breeder's equation**, while drift adds variance $h^2V_P/N_{\mathrm{e}}$ per generation (Lande 1976). The mean then follows Eq. (26.5) with $\alpha = h^2V_P/(\omega^2 + V_P)$ and $\sigma^2 = h^2V_P/N_{\mathrm{e}}$ per generation. Applied to species over millions of years, however, $\theta$ is better read as the optimum of an adaptive zone, which may itself fluctuate, and $\alpha$ as a phenomenological measure of how quickly species return to it (Hansen 1997).

On a tree, the tip covariances follow from Eq. (26.6). For an ultrametric tree of height $T$ with the root state fixed, two species whose shared path has length $s$ have

$$
\operatorname{Cov}(X_i, X_j) = \frac{\sigma^2}{2\alpha}\mathrm{e}^{-2\alpha(T - s)}\bigl(1 - \mathrm{e}^{-2\alpha s}\bigr), \tag{26.7}
$$

because the value at the common ancestor, with variance $\sigma^2(1 - \mathrm{e}^{-2\alpha s})/(2\alpha)$, is carried to each tip multiplied by $\mathrm{e}^{-\alpha(T - s)}$, and the rest of the change is independent. Covariance thus decays with the time since divergence: species separated by much more than the half-life are nearly independent, whatever their relationship, and phylogenetic signal is weak.

![Brownian motion and the Ornstein–Uhlenbeck model. A: sample paths of a trait starting at 0 under Brownian motion (α = 0) and under OU models pulled towards the optimum θ = 1 (dashed) with α = 1 and α = 5 (σ² = 1, time in units of the tree height), simulated with the exact transition distributions of Eq. (26.6); dotted lines: the stationary band θ ± 2σ/√(2α) for α = 5. B: the correlation between two species that share a path of length s from the root of a tree of height 1, from Eq. (26.7): equal to s under Brownian motion, decaying with the time since divergence under OU](./plots/ou.py)

The model becomes a tool for testing adaptive hypotheses when the optimum differs among parts of the tree (Hansen 1997; Butler and King 2004): branches are assigned *a priori* to selective regimes (for example, the habitat or diet inferred for the lineage), each with its own $\theta$, and models with one or several optima, or Brownian motion, are compared by likelihood ratio tests or the **Akaike information criterion**. A shared optimum for lineages that independently entered the same regime is the model-based form of the argument from convergence. Caution is needed: with small trees, measurement error in species means or a misspecified tree, OU models are often preferred over Brownian motion even when the data were generated without stabilizing selection, and $\alpha$ is poorly estimated (Cooper and colleagues 2016); simulation of the fitted models (parametric bootstrap) is a necessary check.

## 26.6. Discrete Characters

### 26.6.1. The Mk Model and Ancestral States

**Definition 26.6.1 (Mk Model)** The **Mk model** (Lewis 2001) describes the evolution of a discrete character with $k$ unordered states as a **continuous-time Markov chain** along each branch with rate matrix $Q$; in the symmetric version, every change occurs at rate $q$, so that

$$
P_{ii}(t) = \frac1k + \frac{k - 1}{k}\mathrm{e}^{-kqt}, \qquad P_{ij}(t) = \frac1k - \frac1k\mathrm{e}^{-kqt} \quad (i \neq j), \tag{26.8}
$$

the analog of the Jukes–Cantor model for $k$ states. Asymmetric versions allow different rates between each pair of states (for a binary character, a gain rate $q_{01}$ and a loss rate $q_{10}$).

The likelihood of the tip states is computed by **Felsenstein's pruning algorithm** and maximized over the rates. Because morphological data sets usually include only characters that vary among the species, the likelihood should be conditioned on variability (the Mkv model; Lewis 2001), otherwise rates are underestimated. The Mk model is also the morphological model of the tip-dating analyses of [7.10.24](/7.10.24#sec-24.5).

**Ancestral state reconstruction**, introduced with parsimony in [7.10.2](/7.10.2#sec-2.6.1) and treated for sequences in [7.10.21](/7.10.21), assigns to each internal node the probabilities of its states given the data: the *marginal* reconstruction computes, for each node separately, the likelihood with the node fixed to each state, which gives posterior probabilities when the root distribution is used as a prior (an **empirical Bayes** calculation when the rate is replaced by its estimate). Unlike parsimony, it reports uncertainty, which is large for old nodes and for characters that change often.

![The Mk model for a binary character and ancestral state reconstruction. A binary character (filled: state 1, open: state 0) was simulated on a dated tree of 12 species (root age 1) under the symmetric Mk model with rate q = 1.5. A: the tree with the observed tip states and, at each internal node, the marginal posterior probability of state 1 (blue sector), computed by the pruning algorithm at the maximum likelihood rate with equal root probabilities; nodes close to tips that agree are reconstructed confidently, deep nodes are uncertain. B: the log likelihood of q (dotted: estimate; shaded: approximate 95 % interval, unbounded above within the range shown); a single character on a small tree determines its rate of change only roughly](./plots/mk.py)

Reconstructions are hypotheses that can be tested experimentally. Vertebrate rhodopsins differ in the wavelength $\lambda_{\max}$ to which they are most sensitive, and fishes of dim, deep water have repeatedly evolved pigments shifted towards blue. Yokoyama and colleagues reconstructed and synthesized the ancestral pigment of the conger eel lineage ($\lambda_{\max} = 501$ nm) and found that the conger's pigment ($486$ nm) could be recreated only by combining the substitution A292S with two other substitutions that by themselves had no effect: the adaptation depended on epistasis among them (Futuyma and Kirkpatrick 2017). Geographic location treated as a character traces the spread of epidemics: the gene tree of Ebola virus showed that most cases of the 2014 West African epidemic, which caused more than 11,000 deaths among more than 26,000 cases, descended from a single introduction into Sierra Leone from Guinea ([7.8.6](/7.8.6#sec-6.8.3)). And any system with inheritance and variation can be analyzed: on a phylogeny of 84 Austronesian societies built from their languages, political organization was inferred to increase in complexity by small steps but to decrease by small or large ones (Currie and colleagues 2010).

### 26.6.2. Correlated Evolution of Discrete Characters

**Definition 26.6.2 (Correlated Evolution)** Two characters show **correlated evolution** when the rate or direction of change of one depends on the state of the other, so that their changes are associated along the branches of the phylogeny beyond what shared ancestry alone produces.

For two binary characters, Pagel (1994) modeled the pair as one Markov chain on the four combined states $00, 01, 10, 11$, in which only one character changes at a time. In the *independent* model, each character has its own gain and loss rates, the same whatever the state of the other (4 parameters); in the *dependent* model, all 8 rates between combined states that differ in one character are free. The likelihood ratio statistic, $2\Delta\ell$, is compared with $\chi^2_4$ (or its null distribution is obtained by simulation), and the estimated rates of the dependent model show which change tends to precede which: for example, whether the transition to a mating system is followed by a change in testis size, or the reverse.

In primates, analyses of this kind showed that shifts between polygamous and monogamous mating systems were repeatedly accompanied by changes in relative testis size, as the hypothesis of sperm competition predicts (Harvey and Harcourt 1984; [7.10.3](/7.10.3#sec-3.5)). Among 344 tetrapod species, where sex determination switched many times between XY and ZW systems in lizards and amphibians, analyses accounting for the phylogeny showed that XY species tend to have female-biased and ZW species male-biased adult sex ratios; the cause, perhaps the degeneration of the Y and W chromosomes raising mortality in the heterogametic sex, is uncertain (Futuyma and Kirkpatrick 2017). A single change in each character, however strongly correlated across species, is one event: such tests have power only when the characters have changed repeatedly. Stochastic character mapping (Nielsen 2002; Huelsenbeck, Nielsen and Bollback 2003) samples complete histories of changes along the branches from their posterior distribution, which gives the expected number and timing of transitions and the time spent in each state.

## 26.7. Rates of Phenotypic Evolution

**Definition 26.7.1 (Darwin and Haldane)** Rates of evolution of a quantitative trait are measured in *darwins*, the change of the natural logarithm of the trait mean per million years (Haldane 1949), $r = (\ln\bar z_2 - \ln\bar z_1)/\Delta t$, or in *haldanes*, the change of the mean in units of the within-population standard deviation per generation (Gingerich 1993), $h = [(\bar z_2 - \bar z_1)/s_p]/\Delta t_{\mathrm{gen}}$.

Measured rates vary greatly among characters and lineages, and above all with the interval over which they are measured: rates observed over a few generations in living populations are hundreds to millions of times higher than those computed from fossil series over millions of years, and rates decline steadily as the interval lengthens (Gingerich 1993; Futuyma and Kirkpatrick 2017). At the short-term rates, a 20 g mouse could evolve into a 2-million-gram elephant in fewer than 100,000 generations. Body mass of terrestrial vertebrates fluctuates without cumulative net change over intervals up to about a million years and accumulates large changes only over longer intervals (Uyeda and colleagues 2011); the largest species of the horse family increased about tenfold in mass over 25 million years.

The models of this chapter explain the scaling. If the trait mean changes as Brownian motion, the expected magnitude of change over an interval $t$ is proportional to $\sigma\sqrt{t}$, so a rate computed as change divided by time scales as $t^{-1/2}$. If change is bounded, as under an OU process near stationarity or for a mean fluctuating within an adaptive zone, the magnitude of change does not grow with $t$ and the rate scales as $t^{-1}$. Only sustained directional change gives a rate independent of the interval. The observed steep decline of rates with interval therefore reflects mostly fluctuating, reversing change averaged over long periods, not slower evolution in the past. Long-term rates of morphological evolution are usually so low that they could be explained by mutation and drift alone (Lynch 1990); the problem is not how evolution can be so fast, but why it is so often slow, which raises the questions of stasis, constraint and niche conservatism taken up in [7.10.32](/7.10.32).

## Summary

| Topic | Result |
|---|---|
| nonindependence | shared ancestry inflates the effective number of observations; Felsenstein's worst case (§26.1) |
| Brownian motion | independent normal increments, rate $\sigma^2$ (Definition 26.2.1); tips $\mathcal{N}_n(a\boldsymbol{1}, \sigma^2C)$, $C_{ij}$ = shared path (Theorem 26.2.1, Eq. (26.1)); GLS estimates of root and rate, Eq. (26.2) |
| contrasts | Algorithm 26.3.1; $n - 1$ independent $\mathcal{N}(0, \sigma^2)$ contrasts (Theorem 26.3.1); regression through the origin |
| PGLS | GLS with phylogenetic residual covariance (Definition 26.3.1); same slope as contrasts under BM (Theorem 26.3.2) |
| phylogenetic signal | Definition 26.4.1; Pagel's $\lambda$, Eq. (26.3); Blomberg's $K$, Eq. (26.4); signal is a pattern, not a process; niche conservatism (Definition 26.4.2) |
| OU model | $\mathrm{d}X = \alpha(\theta - X)\mathrm{d}t + \sigma\mathrm{d}B$ (Definition 26.5.1, Eqs. (26.5)–(26.6)); Lande's interpretation; covariance decays with divergence time, Eq. (26.7); multiple optima; spurious support in small trees |
| discrete characters | Mk model, Eq. (26.8) (Definition 26.6.1); marginal ancestral reconstruction; opsins, Ebola, Austronesian societies |
| correlated evolution | dependent vs independent four-state models, $\chi^2_4$ (Pagel 1994; Definition 26.6.2); needs repeated changes; stochastic character mapping |
| rates | darwins and haldanes (Definition 26.7.1); rates fall with interval: $t^{-1/2}$ under BM, $t^{-1}$ under bounded change |

## Questions

1. For sister tips with values $x_i = 3.0$ and $x_j = 1.0$ on branches of length $v_i = 1$ and $v_j = 3$, compute the standardized contrast, the value assigned to their ancestor and the length added to its branch.

   **Answer** $u = (3.0 - 1.0)/\sqrt{1 + 3} = 1.0$; $x_k = (3.0/1 + 1.0/3)/(1 + 1/3) = 2.5$; added length $1 \times 3/(1 + 3) = 0.75$. The ancestor is pulled towards the tip on the shorter branch, which carries more information about it.

2. Why does ordinary regression across species give too many false positives in Felsenstein's two-clade example, and why do contrasts not?

   **Answer** Most of the variation in both traits comes from the single early divergence of the two clades, which ordinary regression counts as many independent observations. Contrasts weight that divergence as one comparison (the root contrast) among $n - 1$ independent ones, all of which have mean zero under the null hypothesis, so the test has the correct size (Theorem 26.3.1).

3. Under an OU model with $\alpha = 2$ per unit time on a tree of height 1, what is the correlation between two species whose common ancestor lived at $s = 0.5$? Compare with Brownian motion.

   **Answer** From Eq. (26.7) divided by the tip variance $\sigma^2(1 - \mathrm{e}^{-4})/4$: $\mathrm{e}^{-2}(1 - \mathrm{e}^{-2})/(1 - \mathrm{e}^{-4}) = 0.135 \times 0.865/0.982 = 0.119$, against $s = 0.5$ under Brownian motion: half a tree height is several half-lives ($\ln 2/2 = 0.35$), so the species are nearly independent.

4. A trait has $K = 0.3$ in a clade. Give two different evolutionary explanations, and say how they might be distinguished.

   **Answer** Strong stabilizing selection towards a common optimum (OU with large $\alpha$), which erases resemblance among relatives; or adaptation to environments that are not phylogenetically structured (convergence), or simply large measurement error. Fitting OU models with one or several optima defined by the environments, and estimating measurement error, distinguishes them better than $K$ alone.

5. A trait changed by 0.2 standard deviations in 10 generations in a field study, and by 2 standard deviations over $10^6$ generations in a fossil lineage. Compute both rates in haldanes. Is the fossil lineage evolving more slowly?

   **Answer** $0.2/10 = 0.02$ haldanes and $2/10^6 = 2 \times 10^{-6}$ haldanes. Not necessarily: over long intervals rapid changes in alternating directions cancel, so rates decline with interval even if populations always evolve as fast as living ones; the rates are comparable only at the same time scale.
