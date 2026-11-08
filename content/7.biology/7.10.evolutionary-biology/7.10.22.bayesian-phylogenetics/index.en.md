---
title: Bayesian Phylogenetics
description: "What is specific to Bayesian inference of trees: the posterior over topologies, branch lengths and substitution parameters; a complete one-parameter example (the JC69 distance of the human–orangutan 12S rRNA, its marginal likelihood by quadrature, sensitivity to the prior and a prior–likelihood conflict); priors on branch lengths (the tree-length problem of i.i.d. priors and the gamma-Dirichlet prior), on substitution parameters and on topologies (uniform topologies, labeled histories, the Yule and birth–death priors); MCMC proposals and their proposal ratios (sliding windows, proportional scaling with its Jacobian, NNI, SPR, TBR, node slider), mixing, convergence diagnostics and Metropolis-coupled MCMC; summarizing the posterior (MAP tree, credible sets, clade probabilities, consensus); spuriously high posterior probabilities and the star tree paradox; marginal likelihoods by thermodynamic integration and stepping-stone sampling, the failure of the harmonic mean, and reversible-jump MCMC."
---

Bayesian phylogenetics was introduced in [7.8.6](/7.8.6#sec-6.6.2) as a practical alternative to maximum likelihood with the bootstrap: a **prior distribution** on trees and parameters, a **posterior distribution** computed by **Markov chain Monte Carlo** with the **Metropolis–Hastings algorithm**, and clade probabilities as the measure of support. The general theory, Bayes' rule and the choice of priors ([3.2.7](/3.2.7), [3.7.1](/3.7.1), [3.7.2](/3.7.2)), MCMC and its convergence ([3.5.9](/3.5.9)), hierarchical models ([3.7.6](/3.7.6)) and Bayes factors ([3.7.8](/3.7.8#sec-8.8)), is not repeated here. This chapter treats what is specific to trees. The parameter space is unusual: a discrete set of topologies, astronomically large, each carrying its own continuous branch lengths. Priors that look harmless on each branch can be strongly informative about the tree as a whole. The proposals of the chain must move between topologies, and their proposal ratios must be computed correctly. And when the data are many and the models are equally wrong, posterior probabilities can be extreme for no good reason.

The chapter starts with a model simple enough to compute every quantity exactly, the JC69 distance between two sequences of [7.10.20](/7.10.20), and then moves to trees. The statistical properties of the likelihood on which everything rests are those of [7.10.21](/7.10.21); Bayesian dating with relaxed clocks and fossil calibrations is the subject of [7.10.24](/7.10.24), and the multispecies coalescent of [7.10.25](/7.10.25).

## 22.1. The Posterior Distribution of Trees

### 22.1.1. Structure of the Problem

For an alignment $X$, a topology $\tau_k$ with branch lengths $\boldsymbol{t}_k$, and substitution parameters $\boldsymbol{\theta}$ (exchangeabilities, frequencies, the gamma shape), the posterior is

$$
f(\tau_k, \boldsymbol{t}_k, \boldsymbol{\theta} \mid X) = \frac{f(\tau_k)\,f(\boldsymbol{t}_k \mid \tau_k)\,f(\boldsymbol{\theta})\,f(X \mid \tau_k, \boldsymbol{t}_k, \boldsymbol{\theta})}{\sum_j\iint f(\tau_j)\,f(\boldsymbol{t}_j \mid \tau_j)\,f(\boldsymbol{\theta})\,f(X \mid \tau_j, \boldsymbol{t}_j, \boldsymbol{\theta})\,\mathrm{d}\boldsymbol{t}_j\,\mathrm{d}\boldsymbol{\theta}}, \tag{22.1}
$$
where the likelihood $f(X \mid \tau, \boldsymbol{t}, \boldsymbol{\theta})$ is computed by the pruning algorithm. The posterior probability of a topology integrates over its branch lengths and the substitution parameters:

$$
\mathbb{P}(\tau_k \mid X) = \frac{f(\tau_k)\,f(X \mid \tau_k)}{\sum_jf(\tau_j)\,f(X \mid \tau_j)}, \qquad f(X \mid \tau_k) = \iint f(\boldsymbol{t}_k \mid \tau_k)\,f(\boldsymbol{\theta})\,f(X \mid \tau_k, \boldsymbol{t}_k, \boldsymbol{\theta})\,\mathrm{d}\boldsymbol{t}_k\,\mathrm{d}\boldsymbol{\theta}. \tag{22.2}
$$
Each topology is a model, as in [7.10.21](/7.10.21#sec-21.1.2), and its posterior probability is that of a model, with $f(X \mid \tau_k)$ its **marginal likelihood**. The denominator, a sum over $(2s - 5)!!$ unrooted topologies of integrals of dimension $2s - 3$ plus the number of substitution parameters, cannot be computed. MCMC avoids it, because the Metropolis–Hastings acceptance ratio involves only ratios of the numerator: a chain whose states are $(\tau, \boldsymbol{t}, \boldsymbol{\theta})$ visits each topology in proportion to its posterior probability.

All binary topologies of $s$ taxa have the same number of branch lengths, so a move between topologies does not change the dimension of the parameter space; the parameters with the same meaning on both trees (the substitution parameters, the external branches, the branches defining a shared split) can be matched, which keeps the acceptance rates of cross-tree moves reasonable. Only when trees with polytomies or models of different dimension are compared is a trans-dimensional algorithm (Section 22.6.3) needed.

### 22.1.2. A Complete Example: The JC69 Distance

With one parameter everything can be computed by numerical integration, which shows the Bayesian machinery without the complications of trees.

**Example 22.1.1** For the human and orangutan mitochondrial 12S rRNA genes ($x = 90$ differences at $n = 948$ sites, [Example 20.3.1](/7.10.20#sec-20.3.1)), take an exponential prior on the distance with mean $0.2$, $f(d) = 5\,\mathrm{e}^{-5d}$. The likelihood is binomial in the probability $p(d) = \frac{3}{4}(1 - \mathrm{e}^{-4d/3})$ of a difference, $f(x \mid d) = p^x(1 - p)^{n - x}$ up to a constant. The marginal likelihood $f(x) = \int_0^\infty f(d)f(x \mid d)\,\mathrm{d}d = 5.168\times10^{-131}$ is a one-dimensional integral over an infinite range of an integrand that is a sharp spike near $d = 0.1$. Its value is easy to obtain with Gaussian quadrature after a transformation that spreads the spike over the interval, and hard to obtain without one: with the naive transform $y = (d - 1)/(d + 1)$, even $32$ quadrature points give a wrong answer (Yang 2014). The posterior has mean $0.1021$ and $95\,\%$ equal-tail **credible interval** $(0.0819, 0.1246)$, almost identical to the likelihood interval $(0.0817, 0.1245)$: with $948$ sites the likelihood dominates a diffuse prior. Exponential priors with mean $10$ or a uniform prior on $(0, 10)$ give the same posterior to two decimal places.

Two lessons of this simple example carry over to trees. First, priors matter when they are informative relative to the likelihood: the gamma prior $\mathrm{G}(100, 10)$, with mean $10$ and standard deviation $1$, moves the posterior of the 12S distance to a mean of $0.222$ and an interval $(0.190, 0.256)$, which excludes the MLE. Second, when the prior and the likelihood conflict, the posterior can be multimodal. For the human and chimpanzee 12S genes ($x = 11$ at $n = 946$, MLE $0.0117$) under the same prior, the posterior has its main mode at $0.121$, ten times the MLE, and a second local mode at $9.9$, near the prior mean, lower by more than $800$ log units but surrounded by a flat likelihood (Yang 2014). A chain started there may stay for a long time, and no convergence diagnostic computed from a single chain would reveal it.

![Bayesian estimation of a JC69 distance. A: for the human and orangutan 12S rRNA genes (90 differences at 948 sites), the exponential prior with mean 0.2 (dashed), the likelihood scaled to the height of the posterior (dotted, nearly hidden by the posterior) and the posterior, with its mean and 95 % equal-tail credible interval (shaded). B: the posterior under four priors: the exponential priors with means 0.2 and 10 and the uniform prior on (0, 10) give the same posterior, while the informative gamma prior G(100, 10), with mean 10, drags it to about 0.22. C: the human and chimpanzee 12S genes (11 differences at 946 sites, MLE 0.0117) under the same gamma prior, on a log scale: the log posterior (solid) is the sum of the log likelihood (dotted), which is flat beyond saturation, and the log prior (dashed); its highest mode lies at 0.121, and a second local mode at 9.9, near the prior mean, can trap an MCMC chain although it is hundreds of log units lower](./plots/jc-posterior.py)

## 22.2. Priors

### 22.2.1. Priors on Branch Lengths

**Definition 22.2.1 (Tree Prior)** A **tree prior** is the joint prior distribution of the topology and the branch lengths of a phylogeny. Without a clock it is usually specified as a prior on unrooted topologies with a prior on branch lengths given the topology; with a clock, as a prior on rooted trees with node ages, often generated by a model of diversification (Section 22.2.3) or by the **coalescent**.

The first Bayesian programs gave each branch an independent exponential prior (the MrBayes default has mean $0.1$) or a uniform prior on $(0, A)$. Each looks innocent, but jointly they make a strong statement about the tree length $T = \sum_it_i$. With $2s - 3$ independent exponential branch lengths of rate $\lambda$, $T$ has the **gamma distribution** $\Gamma(2s - 3, \lambda)$, with mean $(2s - 3)/\lambda$ and coefficient of variation $1/\sqrt{2s - 3}$. For $s = 100$ taxa and mean branch length $0.1$, the prior $99\,\%$ interval of $T$ is $(16.3, 23.5)$ substitutions per site: an extremely informative prior, centered far above the tree lengths of closely related sequences. Analyses of shallow data sets with many taxa under this default produced trees an order of magnitude too long, with credible intervals of the tree length that excluded its MLE. For a data set of $123$ lizard mitochondrial sequences, the default prior has mean tree length $24.3$ against an MLE of $2.48$ (Brown and colleagues 2010; Zhang and colleagues 2012). The uniform prior is worse: with $A = 100$ it centers the tree length near $10^4$.

**Formula 22.2.1 (Gamma–Dirichlet Prior)** The *gamma–Dirichlet* prior on branch lengths (Rannala, Zhu and Yang 2012) assigns the tree length $T$ a gamma prior $\Gamma(\alpha_T, \beta_T)$ and the proportions $x_i = t_i/T$ a symmetric **Dirichlet distribution** $\mathrm{Dir}(1, \dots, 1)$ on the $K = 2s - 3$ branches. Transforming $(T, x_1, \dots, x_{K-1})$ to $(t_1, \dots, t_K)$, with Jacobian determinant $T^{-(K-1)}$, gives the density

$$
f(\boldsymbol{t}) = \frac{\beta_T^{\alpha_T}}{\Gamma(\alpha_T)}\,\mathrm{e}^{-\beta_TT}\,T^{\alpha_T - 1 - (K - 1)}\,(K - 1)!, \qquad T = \sum_{i=1}^Kt_i. \tag{22.3}
$$

The prior on the tree length is now set directly, with $\alpha_T = 1$ for a diffuse prior and $\beta_T$ chosen to give a reasonable mean, and the posterior tree length is much less sensitive to it: varying the prior mean over several orders of magnitude changed the posterior little in the lizard data. An inverse-gamma prior on $T$ gives a heavier tail. The topology is usually far less sensitive to branch-length priors than the branch lengths are.

### 22.2.2. Priors on Substitution Parameters

Base frequencies and the six GTR exchangeabilities (normalized to sum to $1$) are proportions and receive Dirichlet priors, usually $\mathrm{Dir}(1, \dots, 1)$; the gamma shape $\alpha$ and the ratio $\kappa$ receive exponential or gamma priors, or a uniform prior on a transformed scale. Because priors, unlike MLEs, are not invariant under reparametrization, the choice of scale matters: a uniform prior on $\kappa$ over $(0, 100)$ puts half of its mass above $50$, while a uniform prior on $\kappa/(1 + \kappa)$ treats ratios below and above $1$ symmetrically. With alignments of thousands of sites these parameters are well estimated and the prior has little influence; it matters for small data sets and for parameter-rich models, for which hierarchical priors ([3.7.6](/3.7.6)) that let the data set the spread are an option.

### 22.2.3. Priors on Topologies

Without a clock the usual prior is uniform on unrooted topologies. With rooted trees, a uniform prior on topologies differs from the prior implied by models of diversification. A *labeled history* is a rooted topology together with the order in time of its internal vertices; a rooted tree of $n$ tips has $n!(n - 1)!/2^{n-1}$ labeled histories, while the number of rooted topologies is $(2n - 3)!!$. A symmetric topology has more labeled histories than an asymmetric one: for $n = 4$ there are $15$ topologies and $18$ labeled histories, the balanced topology $((a, b), (c, d))$ has $2$ (either pair may split first), each of the $12$ pectinate topologies $1$.

**Definition 22.2.2 (Yule Process)** The **Yule process** is the pure-birth model of diversification: every lineage splits into two at the same constant rate $\lambda$, independently of the others, and no lineage goes extinct. It is the special case of the **birth–death process** with death rate $0$.

Under the Yule process, at each splitting event each of the current lineages is equally likely to be the one that splits; looking backward in time, each pair of the $k$ lineages is equally likely to be the next to join. Every labeled history therefore has the same probability, and so it does under the coalescent and the constant-rate birth–death process with complete sampling. The induced prior on rooted topologies favors balanced trees, relative to the uniform prior (for $n = 4$, $\frac{2}{18}$ for each balanced topology instead of $\frac{1}{15}$). The node ages follow the process: under the Yule model the waiting time while there are $k$ lineages is exponential with rate $k\lambda$. These priors are the basis of the clock models of [7.10.24](/7.10.24), where the times matter.

The prior on topologies induces a prior on clades. Under the uniform prior on rooted topologies, small and very large clades are relatively probable and clades of intermediate size improbable (Pickett and Randle 2005), whereas under the Yule prior the expected number of clades of size $k$ among $n$ tips is $2n/(k(k + 1))$ for $k < n$, falling steadily with $k$. A uniform prior on trees is thus not uninformative about clades, and the prior influence can persist in the posterior for clades that the data say little about.

![Priors on branch lengths and topologies. A: the prior on the tree length T induced for s = 123 sequences by independent exponential priors with mean 0.1 on each of the 243 branches (a gamma distribution with mean 24.3 and little spread), and by the gamma-Dirichlet prior with tree length T ~ G(1, 1); the dotted line marks the maximum likelihood tree length 2.48 of the lizard data quoted in the text. Densities are drawn for log T. B: the corresponding priors on a single branch: under the gamma-Dirichlet prior each branch is a share of the tree length and is expected to be short. C: the expected number of clades of each size k in a rooted tree of n = 10 tips, under the uniform prior on rooted topologies (squares) and under the Yule prior (line; circles, 20 000 simulated Yule trees): the uniform prior favors very small and very large clades](./plots/priors.py)

## 22.3. MCMC Proposals

### 22.3.1. Proposal Ratios

In the Metropolis–Hastings algorithm ([Algorithm 9.4.1](/3.5.9#alg-9.4.1) of 3.5.9), a proposal $x \to x'$ drawn from $q(x' \mid x)$ is accepted with probability

$$
\alpha = \min\Bigl\{1,\ \frac{f(x')}{f(x)}\cdot\frac{f(X \mid x')}{f(X \mid x)}\cdot\frac{q(x \mid x')}{q(x' \mid x)}\Bigr\}, \tag{22.4}
$$
the product of the prior ratio, the likelihood ratio and the *proposal ratio*. Getting the proposal ratio wrong does not stop the chain from running; it makes it converge to the wrong distribution, which is why every new move must be derived carefully and checked, for instance by running the chain without data and verifying that it reproduces the prior.

The simplest moves change one continuous parameter:

- *Sliding window*: $x' \sim \mathrm{U}(x - w/2, x + w/2)$, reflected at a boundary ($x' = -x'$ if $x' < 0$). The proposal density is symmetric, also after reflection, and the proposal ratio is $1$. A normal proposal $x' \sim \mathcal{N}(x, \sigma^2)$ is equivalent; *Bactrian* proposals, a mixture of two normals centered away from $x$, avoid tiny steps and mix better.
- *Proportional scaling*: $x' = cx$ with $c = \mathrm{e}^{\varepsilon(u - 1/2)}$, $u \sim \mathrm{U}(0, 1)$. On the logarithmic scale this is a sliding window, $y' = y + \varepsilon(u - \frac{1}{2})$ with $y = \ln x$, which is symmetric; transforming back, the density of $x'$ carries the Jacobian $\lvert\mathrm{d}y'/\mathrm{d}x'\rvert = 1/x'$, so

$$
\frac{q(x \mid x')}{q(x' \mid x)} = \frac{1/x}{1/x'} = \frac{x'}{x} = c. \tag{22.5}
$$
If $m$ parameters are multiplied by the same $c$ (all branch lengths of a tree, to rescale the tree), the proposal ratio is $c^m$. Scaling moves are natural for positive parameters spanning orders of magnitude, such as branch lengths and rates.

### 22.3.2. Moves between Trees

Proposals that change the topology are of two kinds: local moves that rearrange the tree near a branch and adjust branch lengths, and global moves that cut and regraft subtrees.

- *Nearest-neighbor interchange* (NNI): choose an internal branch, swap two of the four subtrees around it, and possibly rescale the branch lengths in the neighborhood. On unrooted binary trees every tree has the same number $2(s - 3)$ of NNI neighbors, so choosing the branch and the swap uniformly gives a symmetric proposal; the branch-length adjustments contribute their own Jacobians.
- *Subtree pruning and regrafting* (SPR) and *tree bisection and reconnection* (TBR) are the moves of the heuristic searches of [7.8.6](/7.8.6#sec-6.5.2). They move further in tree space, but most of their proposals are poor trees that are rejected, so they are combined with local moves, and the proposal ratio must count the number of possible regraftings in the forward and backward directions when it differs between trees.
- *Node slider* (for rooted trees under a clock): move an internal vertex up or down in time; if it passes another vertex, the topology changes. The proposal ratio is a ratio of the Jacobians of the age changes.

Mixing over topologies is the bottleneck of Bayesian phylogenetics. The likelihood surface over trees is rugged, and a chain can be trapped in a group of good trees separated from another by trees of low posterior probability, the Bayesian counterpart of the islands of [7.10.21](/7.10.21#sec-21.4.6).

### 22.3.3. Mixing, Convergence and Coupled Chains

The step size of each move trades the acceptance rate against the size of the accepted steps. Steps that are too small are almost always accepted but explore slowly; steps that are too large are mostly rejected and the chain sticks. The efficiency of the estimate of a posterior mean, the inverse of the factor $1 + 2\sum_k\rho_k$ by which autocorrelation inflates its variance (the **effective sample size** of [3.5.9](/3.5.9#sec-9.6)), is highest at intermediate steps, with acceptance proportions of about $30$ to $40\,\%$ for one-dimensional moves. Programs tune the step sizes automatically during the burn-in.

![MCMC proposals for the JC69 distance of the human and orangutan 12S rRNA genes, with the exponential prior of mean 0.2. A: the first 1000 iterations of sliding-window chains started far from the posterior (d = 0.25), with a window that is too small (w = 0.005, nearly all proposals accepted, the chain drifts slowly), about right (w = 0.04) and too large (w = 0.5, most proposals rejected, long flat stretches). B: for sliding windows and proportional-scaling moves of increasing size (relative to the posterior standard deviation), the proportion of proposals accepted (dashed) and the efficiency, the variance of the posterior mean under independent sampling relative to that of the chain (solid), from 10 000 iterations each. For this nearly normal one-dimensional posterior the two moves behave alike; efficiency is low for small steps, highest for steps of several standard deviations with about 40 % of proposals accepted, and falls again for very large steps](./plots/mcmc-moves.py)

Convergence is assessed with several independent chains from dispersed starting trees. For continuous parameters, trace plots, effective sample sizes and the potential scale reduction factor $\hat R$ of Gelman and Rubin ([3.5.9](/3.5.9#sec-9.6)) are used. For the topology, which has no mean or variance, the chains are compared by their clade probabilities; MrBayes reports the average standard deviation of split frequencies across runs, and values below about $0.01$ are taken to indicate agreement. Agreement between chains is necessary but not sufficient: all chains may be stuck in the same region.

Metropolis-coupled MCMC ($\mathrm{MC}^3$), the **parallel tempering** of physics, runs $m$ chains in parallel, chain $i$ sampling the "heated" distribution $\pi(x)^{\beta_i}$ with $\beta_1 = 1$ for the cold chain and, in MrBayes, $\beta_i = 1/(1 + \lambda(i - 1))$ with a heating parameter $\lambda$. Heated chains see a flatter surface and cross valleys easily. At intervals, two chains $i$ and $j$ propose to swap states, which is accepted with probability

$$
\min\Bigl\{1,\ \frac{\pi(x_j)^{\beta_i}\,\pi(x_i)^{\beta_j}}{\pi(x_i)^{\beta_i}\,\pi(x_j)^{\beta_j}}\Bigr\},
$$
and only the cold chain is sampled. The swaps carry good states found by the heated chains to the cold one, at the cost of $m$ times the computation.

## 22.4. Summarizing the Posterior

The output of the chain is a sample of trees with branch lengths and parameters. It is summarized as follows:

- The *maximum a posteriori* (MAP) tree is the topology sampled most often, the counterpart of the ML tree. With many taxa, even the best tree may have a small posterior probability, so a single tree is a poor summary.
- The $95\,\%$ *credible set of trees* collects the most probable topologies until their probabilities sum to $95\,\%$ (Rannala and Yang 1996; a **credible set** in the sense of [3.7.1](/3.7.1)). It is small when the data are informative and can contain thousands of trees when they are not.
- Clades are summarized individually.

**Definition 22.4.1 (Posterior Clade Probability)** The **posterior clade probability** of a clade (or of a split, for unrooted trees) is the posterior probability that the true tree contains it, the sum of the posterior probabilities of all topologies that contain it, estimated by the proportion of sampled trees containing it.

The usual display is the **majority-rule consensus tree** of the sample ([7.8.6](/7.8.6#sec-6.6.1)), with each clade labeled by its posterior probability, or the MAP tree with its clades labeled. A clade probability averages over all trees that contain the clade, a form of model averaging over the uncertain parts of the tree. Posterior means of branch lengths on the consensus tree are averages over different sets of sampled trees for different branches and are best not reported; when branch lengths matter, a second chain on the fixed topology gives them.

Unlike the bootstrap percentage, a posterior clade probability has a direct interpretation: the probability that the clade is true given the data, the model and the prior. In real and simulated data alike, posterior clade probabilities are usually higher than bootstrap percentages for the same clades; it is often remarked that bootstrap values are reported only when they exceed $50\,\%$, and posterior probabilities only when they fall below $100\,\%$. This is not in itself evidence that either is wrong, since they measure different things. But posterior probabilities are sometimes very high for clades that are decidedly wrong, or different analyses of the same data give conflicting clades, each with posterior probability near $1$. The next section examines why.

## 22.5. High Posterior Probabilities and the Star Tree Paradox

The very first Bayesian analysis of a molecular phylogeny, of $739$ bp of mitochondrial tRNA genes from five apes, gave the best tree a posterior probability of $0.9999$ (Rannala and Yang 1996), although the human–chimpanzee–gorilla relationship was then considered difficult. Spuriously high posterior probabilities can have three causes: computational errors (a wrong proposal ratio, a chain that has not converged or mixes poorly, so that it overrepresents the region it visited); misspecification of the substitution model, which simulations show inflates posterior probabilities; and the behavior of Bayesian model selection itself, which can produce extreme probabilities even under the correct model. The third is the subject of this section.

Bayesian model selection is consistent: as the data grow, the model closest to the truth in **Kullback–Leibler divergence** has posterior probability tending to $1$, and among equally close models the one with fewer parameters wins. The case not covered is that of several models of the same dimension that are equally close to the truth. Binary trees of the same taxa are such models when the true tree is a star.

**Definition 22.5.1 (Star Tree Paradox)** The **star tree paradox** is the behavior of posterior probabilities of binary trees when the data are generated on a star tree (without internal branches): as the number of sites tends to infinity, the posterior probabilities of the binary trees do not converge to equal values but continue to fluctuate among data sets, so that one binary tree frequently receives a posterior probability close to $1$ (Suzuki, Glazko and Nei 2002; Lewis, Holder and Holsinger 2005; Yang and Rannala 2005).

For three species and binary characters under a clock, with rooted binary trees $\tau_1, \tau_2, \tau_3$, the limiting distribution is known (Susko 2008): with $z_1, z_2, z_3$ standard normal variables with correlations $-\frac{1}{2}$,

$$
\mathbb{P}(\tau_i \mid X) \to \frac{\mathrm{e}^{z_i^2/2}\,\Phi(z_i)}{\sum_j\mathrm{e}^{z_j^2/2}\,\Phi(z_j)}. \tag{22.6}
$$
The form explains the paradox. The $z_i$ are the standardized estimates of the internal branch of each binary tree, which fluctuate at the scale $n^{-1/2}$ around the true value $0$; integrating the likelihood over a branch length constrained to be positive gives a factor $\int_0^\infty\mathrm{e}^{zu - u^2/2}\,\mathrm{d}u = \sqrt{2\pi}\,\mathrm{e}^{z^2/2}\Phi(z)$ that depends on $z$ exponentially, and more data only reduce the scale on which the $z_i$ are measured, not their randomness. In the limit, one binary tree has posterior probability above $0.95$ in $4.3\,\%$ of data sets and above $0.99$ in $0.8\,\%$, and one has a probability below $0.05$ in $17\,\%$ (Yang 2014 reports $4.2$, $0.8$ and $17.3\,\%$). Real radiations are rarely exact stars, but a very short internal branch behaves like one until the data are large enough to resolve it, and the same mechanism inflates posterior probabilities of clades separated by short branches.

![The star tree paradox. Binary characters evolve under a molecular clock on a star tree of three species (each branch 0.2), and the three rooted binary trees are compared by Bayesian inference, with exponential priors of mean 0.1 on their two branch lengths and marginal likelihoods computed by two-dimensional numerical integration. A: the posterior probabilities of the three trees for 300 data sets of 3000 sites, plotted in a triangle whose corners are probability 1 for one tree and whose center (cross) is 1/3 for each. The points do not cluster at the center: they spread over the whole triangle, and many lie near its edges and corners, where one tree is strongly favored. B: the distribution of the largest of the three posterior probabilities in the simulated data sets (histogram) and in the limit of infinitely many sites (line), computed from 200 000 draws of Susko's formula, Eq. (22.6); the proportions of data sets in which one tree receives more than 0.95 are given in the panel](./plots/star-tree.py)

Two remedies have been proposed. One adds the star tree and other multifurcating trees to the model, with positive prior probability, and moves between trees of different dimension by reversible-jump MCMC (Lewis and colleagues 2005); when the data contain no information on a branch, the posterior then favors the polytomy. The other gives internal branches a prior whose mean shrinks with the size of the data (Yang and Rannala 2005; Yang 2008), which makes clade probabilities less extreme and closer to bootstrap percentages. Neither is standard; the practical lesson is that clade probabilities near $1$ supported by very short branches deserve the same suspicion as bootstrap support of $100\,\%$ in large data sets ([7.10.21](/7.10.21#sec-21.7.1)).

## 22.6. Comparing Models

### 22.6.1. Marginal Likelihoods and the Harmonic Mean

The **Bayes factor** of two models, the ratio of their marginal likelihoods ([3.7.8](/3.7.8#sec-8.8)), compares substitution models, clock models, partitionings or constrained topologies. Marginal likelihoods are integrals over all parameters of the model and are much harder to compute than posterior expectations. The harmonic mean estimator,

$$
\hat f(X) = \Bigl[\frac{1}{N}\sum_{k=1}^N\frac{1}{f(X \mid \theta^{(k)})}\Bigr]^{-1}, \qquad \theta^{(k)} \sim f(\theta \mid X), \tag{22.7}
$$
uses only the posterior sample and was for years the default in phylogenetic programs. It is consistent, since $\mathbb{E}[1/f(X \mid \theta) \mid X] = 1/f(X)$, but its variance is usually infinite: the terms are dominated by rare draws from the tails of the posterior, where the likelihood is small, which a finite chain almost never visits. In practice it overestimates the marginal likelihood, does not improve noticeably with longer runs, and is insensitive to the prior, which the true marginal likelihood is not. Its use is no longer recommended.

### 22.6.2. Thermodynamic Integration and Stepping-Stone Sampling

Both methods connect the prior to the posterior through the *power posteriors* $p_b(\theta) = f(\theta)f(X \mid \theta)^b/z(b)$, $0 \le b \le 1$, with normalizing constants $z(0) = 1$ and $z(1) = f(X)$.

**Definition 22.6.1 (Thermodynamic Integration)** **Thermodynamic integration** (path sampling; Lartillot and Philippe 2006 in phylogenetics) computes

$$
\ln f(X) = \int_0^1\mathbb{E}_b\bigl[\ln f(X \mid \theta)\bigr]\,\mathrm{d}b, \tag{22.8}
$$
where $\mathbb{E}_b$ is the expectation under $p_b$, estimated by MCMC at a grid of values of $b$ and integrated numerically.

Eq. (22.8) follows from $\frac{\mathrm{d}}{\mathrm{d}b}\ln z(b) = \frac{1}{z(b)}\int f(\theta)f(X \mid \theta)^b\ln f(X \mid \theta)\,\mathrm{d}\theta = \mathbb{E}_b[\ln f(X \mid \theta)]$, integrated from $0$ to $1$.

**Definition 22.6.2 (Stepping-Stone Sampling)** **Stepping-stone sampling** (Xie and colleagues 2011) writes $f(X) = \prod_{k=0}^{K-1}z(b_{k+1})/z(b_k)$ for $0 = b_0 < b_1 < \dots < b_K = 1$ and estimates each ratio by **importance sampling** from the power posterior at $b_k$,

$$
\frac{z(b_{k+1})}{z(b_k)} = \mathbb{E}_{b_k}\bigl[f(X \mid \theta)^{b_{k+1} - b_k}\bigr] \approx \frac{1}{N}\sum_{j=1}^Nf(X \mid \theta_{k,j})^{b_{k+1} - b_k}. \tag{22.9}
$$

Because successive power posteriors are close, each importance-sampling step is well behaved, which the single giant step of the harmonic mean, from posterior to prior, is not. The values of $b$ are concentrated near $0$, where the power posterior changes fastest; a common choice is the quantiles $b_k = (k/K)^{1/0.3}$ of a $\mathrm{Beta}(0.3, 1)$ distribution. Both methods cost $K$ separate MCMC runs; they are implemented in MrBayes, BEAST 2 and RevBayes, and are the standard ways of computing Bayes factors between substitution or clock models.

![Estimating a marginal likelihood, for the JC69 model of the human and orangutan 12S rRNA genes with the exponential prior of mean 0.2, whose exact log marginal likelihood (−299.996, from the integral of Example 22.1.1) is obtained by quadrature. A: power posteriors for several values of b, from the prior (b = 0) to the posterior (b = 1), on a log scale; small values of b already move most of the mass toward the region favored by the likelihood. B: estimates from 40 independent replicates of each method, all using exact draws from the target distributions so that only the estimators differ: the harmonic mean of the likelihood over 1000 or 10 000 posterior draws is biased upward by more than a log unit and barely improves with ten times more draws, while stepping-stone sampling with 16 power posteriors and 200 draws each is close to the exact value (line)](./plots/marginal-likelihood.py)

### 22.6.3. Reversible-Jump MCMC

When the models differ in dimension (substitution models from JC69 to GTR, numbers of rate categories, trees with and without polytomies), a single chain can move between them by *reversible-jump MCMC* (Green 1995). A jump from a model with parameters $\theta$ to one with more parameters $\theta'$ draws auxiliary random variables $u$ to fill the extra dimensions and maps $(\theta, u)$ to $\theta'$ by a one-to-one transformation; the acceptance ratio of Eq. (22.4) then includes the ratio of the probabilities of choosing the two moves and the Jacobian of the transformation. The posterior probability of each model is the proportion of time the chain spends in it, and averaging over the models (for instance over all time-reversible nucleotide models, Huelsenbeck and colleagues 2004) accounts for the uncertainty in the model instead of conditioning on one chosen model. Constructing efficient jumps is difficult, which is why marginal likelihoods computed separately for each model remain common.

## Summary

| Topic | Key points |
|---|---|
| Posterior of trees | Eq. (22.1); topology posterior from marginal likelihoods, Eq. (22.2); each topology is a model; MCMC avoids the sum over trees; binary trees share dimension, so parameters are matched across trees |
| One-parameter example | JC69 distance of 12S rRNA: $f(x) = 5.168\times10^{-131}$ by quadrature (transform matters), posterior mean $0.1021$, CI $(0.0819, 0.1246)$; informative prior $\mathrm{G}(100, 10)$ moves it to $0.22$; prior–likelihood conflict gives a second mode (Example 22.1.1) |
| Branch-length priors | tree prior (Definition 22.2.1); i.i.d. exponential induces $T \sim \Gamma(2s - 3, \lambda)$, strongly informative (mean $24.3$ vs MLE $2.48$); gamma–Dirichlet prior, Eq. (22.3) |
| Other priors | Dirichlet for frequencies and exchangeabilities, scale matters; uniform topologies vs labeled histories ($n!(n - 1)!/2^{n-1}$); Yule process (Definition 22.2.2) uniform on labeled histories, favors balanced trees; clade-size effects ($2n/(k(k+1))$ under Yule) |
| Proposals | acceptance with prior, likelihood and proposal ratios, Eq. (22.4); sliding window (ratio $1$), proportional scaling (ratio $c$, or $c^m$), Eq. (22.5); NNI, SPR, TBR, node slider; tuning to about 30–40 % acceptance |
| Convergence | several chains, ESS, $\hat R$, split-frequency agreement; $\mathrm{MC}^3$ with heated chains and swaps |
| Summaries | MAP tree, 95 % credible set, posterior clade probability (Definition 22.4.1), majority-rule consensus; avoid consensus branch lengths |
| High probabilities | errors, model misspecification, and the star tree paradox (Definition 22.5.1): limit Eq. (22.6), $4.3\,\%$ of data sets give $> 0.95$; remedies: polytomy priors with rjMCMC, data-size-dependent branch priors |
| Model comparison | harmonic mean, Eq. (22.7), has infinite variance and is biased; thermodynamic integration, Eq. (22.8); stepping-stone, Eq. (22.9); reversible-jump MCMC for model averaging |

## Questions

1. For the scaling move that multiplies all $2s - 3$ branch lengths of a tree by $c = \mathrm{e}^{\varepsilon(u - 1/2)}$, give the proposal ratio and the full acceptance ratio under i.i.d. exponential branch-length priors with rate $\lambda$.

   **Answer** On the log scale the move adds the same $\varepsilon(u - \frac{1}{2})$ to every $\ln t_i$, symmetric; the Jacobian of each coordinate contributes $c$, so the proposal ratio is $c^{2s - 3}$. The prior ratio is $\prod_i\mathrm{e}^{-\lambda(ct_i - t_i)} = \mathrm{e}^{-\lambda(c - 1)T}$. The acceptance probability is $\min\{1, \mathrm{e}^{-\lambda(c - 1)T}\,c^{2s - 3}\,f(X \mid c\boldsymbol{t})/f(X \mid \boldsymbol{t})\}$.

2. Show that i.i.d. exponential priors with mean $0.1$ on the branches of an unrooted tree of $s = 50$ taxa imply a prior mean and standard deviation of the tree length, and why this matters for a data set of closely related sequences with an ML tree length of $0.5$.

   **Answer** $T \sim \Gamma(97, 10)$: mean $9.7$, standard deviation $\sqrt{97}/10 = 0.98$. The prior puts essentially no mass near $0.5$ (it is about nine standard deviations away), so it competes with the likelihood, and with weakly informative data it pulls the posterior tree length far above the MLE. A gamma–Dirichlet prior with a diffuse prior on $T$ removes the problem.

3. For rooted trees of $4$ taxa, compare the prior probability of the topology $((a, b), (c, d))$ under the uniform prior on topologies and under the Yule prior, and the prior probability that $a$ and $b$ form a clade under each.

   **Answer** Uniform: $1/15$ for the topology. Yule: the topology has $2$ of the $18$ labeled histories, probability $1/9$. The clade $(a, b)$ occurs in the balanced tree $((a, b), (c, d))$ and in the pectinate trees in which $a$ and $b$ join first, $(((a, b), c), d)$ and $(((a, b), d), c)$, $3$ topologies: $3/15 = 0.2$ under the uniform prior, and $(2 + 1 + 1)/18 = 2/9 \approx 0.22$ under the Yule prior. Check backward in time: $(a, b)$ is the first of the $6$ pairs to join with probability $1/6$, or $(c, d)$ joins first ($1/6$) and then $(a, b)$ is the first of the $3$ remaining pairs ($1/3$): $1/6 + 1/18 = 2/9$.

4. Why does the harmonic mean estimator of the marginal likelihood barely change when the chain is run ten times longer, while the stepping-stone estimate improves?

   **Answer** The harmonic mean is an importance-sampling estimate of $1/f(X)$ with the posterior as the sampling distribution for a target that is the prior; the weights $1/f(X \mid \theta)$ are enormous in the tails of the posterior, which are almost never sampled, so its variance is typically infinite and its error is dominated by rare unseen draws, not by the number of samples. Stepping-stone sampling breaks the move from prior to posterior into many small steps, each an importance-sampling problem with well-behaved weights, so its error falls with the sample size.

5. In a Bayesian analysis of a rapid radiation, a clade defined by a branch of estimated length $0.001$ substitutions per site has posterior probability $0.98$, and its bootstrap support is $55\,\%$. How should it be reported?

   **Answer** The conflict is typical of short branches: as in the star tree paradox, posterior probabilities of resolutions of a near-polytomy fluctuate widely and can be near $1$ without strong evidence, while the bootstrap reflects the few informative sites on the branch. Report both measures; check robustness to the internal-branch prior (a data-size-dependent or polytomy prior), to the substitution model, and across independent chains; and present the relationship as unresolved unless more data (more genes) increase both supports.
