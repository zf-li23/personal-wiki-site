---
title: Basics of Bayesian Computation
description: Why Bayesian inference reduces to sampling and Monte Carlo integration; non-iterative methods for drawing from a posterior known only up to a constant (grid approach, inverse transform, relationships between distributions, rejection sampling and adaptive rejection sampling for log-concave densities); importance sampling with the choice of proposal, the optimal proposal, tail conditions, the effective sample size, self-normalized weights, a censored-data example and sampling importance resampling.
---

The posterior distribution $p(\theta\mid y)\propto p(\theta)p(y\mid\theta)$ is fully determined by the model and the data, but outside the conjugate families of [3.7.1](/3.7.1)–[3.7.4](/3.7.4) neither its normalizing constant nor its summaries are available in closed form. [3.7.5](/3.7.5) showed that a sample of draws from the posterior answers every question about it, and drew samples on a grid; this chapter develops the general non-iterative methods for producing such draws, or weighted versions of them, from a density that can only be evaluated up to a constant. After the reason why sampling is the central computational task (§9.1), we review three elementary methods: the grid approach, inverse transform sampling and transformations between distributions (§9.2). Rejection sampling turns draws from a simple proposal into exact draws from the target (§9.3); importance sampling keeps every proposal draw and corrects it by a weight (§9.4). Both depend critically on how well the proposal matches the target, above all in its tails, and both deteriorate in high dimensions. That is the reason for the iterative methods of [3.7.10](/3.7.10), the **Metropolis–Hastings algorithm** and the **Gibbs sampler**, for which the methods of this chapter remain the building blocks (starting points, proposals, one-dimensional updates).

The general theory of the samplers, with full proofs, is in the statistical computing course: random number generation, the inverse transform and rejection sampling in [3.5.8](/3.5.8), Monte Carlo integration and importance sampling in [3.5.9](/3.5.9). Here we concentrate on what changes when the target is a posterior: the density is known only up to a constant, the natural proposals are derived from the prior, from a partial posterior or from a normal approximation, and the quality of the result must be judged from the simulation itself. Throughout, $f$ denotes a normalized target density, $q=bf$ an unnormalized version of it with unknown $b>0$, and $g$ a proposal density that we can both sample and evaluate.

## 9.1. Why Sampling?

### 9.1.1. The Computational Problem

Bayesian inference poses two computational tasks: computing the **posterior distribution** $p(\theta\mid y)$, and computing the **posterior predictive distribution**

$$
p(\tilde y\mid y)=\int p(\tilde y\mid\theta)\,p(\theta\mid y)\,\mathrm{d}\theta.
$$
Both are usually impossible in closed form. The difficulty is already visible in **Bayes' theorem**,

$$
p(\theta\mid y)=\frac{p(\theta,y)}{p(y)}=\frac{p(\theta)p(y\mid\theta)}{p(y)}\propto p(\theta)p(y\mid\theta):
$$
the numerator is a product of known functions, while the denominator $p(y)=\int p(\theta)p(y\mid\theta)\,\mathrm{d}\theta$, the **marginal likelihood**, is an integral over the whole parameter space.

**Definition 9.1.1 (Unnormalized Density)** A nonnegative function $q$ with $0<\int q(x)\,\mathrm{d}x<\infty$ is an **unnormalized density** of the distribution with density $f(x)=q(x)/\int q(x')\,\mathrm{d}x'$. In Bayesian computation the target distribution is the posterior, and its unnormalized density is

$$
q(\theta\mid y)=p(\theta)\,p(y\mid\theta)\propto p(\theta\mid y).
$$

A useful computational method must therefore work with $q(\theta\mid y)$ alone. All the methods of this chapter do, possibly after a modification (§9.3.3, §9.4.5). In practice $\log q(\theta\mid y)$ is computed rather than $q$ itself, since products of many likelihood terms underflow.

### 9.1.2. Inference by Monte Carlo Simulation

A distribution is well represented by a large sample from it: the histogram of draws approximates the density, the scatter plot of joint draws approximates the contours of a joint density, and every summary of the distribution has a sample counterpart. With draws from the posterior, any posterior inference can therefore be carried out numerically ([3.7.5](/3.7.5), §5.1).

Most quantities of interest are expectations. If $\theta^1,\dots,\theta^S$ are independent draws from $p(\theta\mid y)$, then

$$
\mathbb{E}[h(\theta)\mid y]=\int h(\theta)\,p(\theta\mid y)\,\mathrm{d}\theta\approx\frac1S\sum_{s=1}^Sh(\theta^s). \tag{9.1}
$$
This is the **Monte Carlo method** ([3.1.12](/3.1.12)): an expectation is approximated by the sample mean of a function of simulated random variables. The estimate is unbiased; by the **law of large numbers** it converges as $S\to\infty$, and by the **central limit theorem** its error is approximately normal with standard deviation $\sqrt{\operatorname{Var}(h(\theta)\mid y)/S}$. The convergence rate $O(S^{-1/2})$ does not depend on the dimension of $\theta$, which is what makes simulation preferable to numerical quadrature in more than a few dimensions.

Many quantities that do not look like expectations can be written as one:

- *probabilities:* $\mathbb{P}(Y\in A)=\mathbb{E}[\boldsymbol{1}_A(Y)]$;
- *integrals:* with $U\sim\mathrm{U}(a,b)$, whose density is $f_U(x)=\frac1{b-a}$ on $(a,b)$,
  $$
  \int_a^bq(x)\,\mathrm{d}x=(b-a)\int_a^bq(x)\frac1{b-a}\,\mathrm{d}x=(b-a)\,\mathbb{E}[q(U)];
  $$
- *finite sums:* with $W$ uniform on a finite set $A$, so that each element has probability $p=1/\lvert A\rvert$,
  $$
  \sum_{x\in A}q(x)=\frac1p\sum_{x\in A}q(x)\,p=\frac1p\,\mathbb{E}[q(W)].
  $$

Each is then estimated by an average over simulated values, as in Eq. (9.1). The comparison of the hit-or-miss and mean-value estimators of an integral is in [3.5.9](/3.5.9), §9.1.

### 9.1.3. Sampling a Univariate Distribution

All simulation starts from uniform pseudorandom numbers. They are produced by deterministic recursions such as the **linear congruential generator**

$$
X_{n+1}=(aX_n+c)\bmod m,
$$
whose outputs divided by $m$ behave like independent $\mathrm{U}(0,1)$ draws; modern software uses longer-period generators such as the Mersenne Twister ([3.5.8](/3.5.8), §8.1; Ripley's *Stochastic Simulation* (1987) is a classical reference). We take such a generator for granted. To turn uniform numbers into draws from a general distribution there are five basic approaches, treated in the rest of this chapter:

1. the grid approach (already used in [3.7.5](/3.7.5));
2. inverse transform sampling;
3. relationships with other distributions;
4. rejection sampling;
5. importance sampling, which produces weighted rather than plain draws.

## 9.2. Some Simple Sampling Methods

### 9.2.1. The Grid Approach

Suppose $X$ has a density $p(x)$, possibly unnormalized, that can be evaluated at any point. The grid approach replaces the continuous distribution by a discrete one.

**Algorithm 9.2.1 (Grid Approach)**

1. Choose an equally spaced grid of values $x_{1:n}=(x_1,\dots,x_n)$ covering the region where the density is not negligible.
2. Evaluate the density at each grid point, $p_i=p(x_i)$, and set $p_0=0$.
3. Normalize, $\tilde p_i=p_i/\sum_{j=0}^np_j$, which gives a valid discrete probability distribution on $x_{1:n}$.
4. Compute its distribution function, $\tilde P_i=\sum_{j=1}^i\tilde p_j\approx\mathbb{P}(X\le x_i)$, with $\tilde P_0=0$.
5. To generate a draw, sample $u\sim\mathrm{U}(0,1)$ and set $x=x_i$ for the index $i$ with $\tilde P_{i-1}<u\le\tilde P_i$.

Step 5 is a mechanism for drawing from any discrete distribution; it is the discrete case of the inverse transform of §9.2.2. In R it is implemented by `sample()`, which normalizes the weights itself:

```r
x <- seq(-4, 4, length.out = 1000)        # grid
p <- exp(-x^2 / 2) * (1 + sin(3 * x)^2)    # any unnormalized density
draws <- sample(x, size = 5000, replace = TRUE, prob = p)
```

The grid approach is quick and easy, works for any density that can be evaluated, and extends to several dimensions: **grid sampling** in two dimensions, with a marginal and a conditional step, is Algorithm 5.2.1 of [3.7.5](/3.7.5). Its drawbacks are that the draws come from an approximation to the true distribution, whose quality depends on the number and range of the grid points (too few points give a poor approximation; a range that is too narrow cuts off mass), and that only the $n$ grid values can be generated, so that most values of the random variable never occur. Adding a uniform jitter within each grid cell ([3.7.5](/3.7.5), §5.2) removes the second problem but not the first. Since the cost grows like $n^d$ in $d$ dimensions, the method is restricted to one or two dimensions, and other schemes are needed in general.

### 9.2.2. Inverse Transform Sampling

Let $F(x)=\mathbb{P}(X\le x)$ be the distribution function of $X$. Its generalized inverse, the **quantile function**, is

$$
F^{-1}(u)=\inf\{x\colon F(x)\ge u\},\qquad0<u<1.
$$
Because $F$ is nondecreasing and right-continuous, $F^{-1}(u)\le x$ if and only if $u\le F(x)$.

**Proposition 9.2.1** If $U\sim\mathrm{U}(0,1)$, then $F^{-1}(U)$ has distribution function $F$. If $F$ is continuous, then conversely $F(X)\sim\mathrm{U}(0,1)$.

**Proof** By the equivalence above, $\mathbb{P}(F^{-1}(U)\le x)=\mathbb{P}(U\le F(x))=F(x)$. If $F$ is continuous, then $F(F^{-1}(u))=u$, and $\mathbb{P}(F(X)\le u)=\mathbb{P}(X\le F^{-1}(u))=F(F^{-1}(u))=u$ for $0<u<1$ (the event $F(X)\le u$ differs from $X\le F^{-1}(u)$ only on a set of probability zero). $\square$

Hence an i.i.d. sample $u_1,\dots,u_m$ from $\mathrm{U}(0,1)$ gives an i.i.d. sample $x_i=F^{-1}(u_i)$ from $F$. This is **inverse transform sampling**; its general form and further examples are in [3.5.8](/3.5.8), §8.2.

**Example 9.2.1** (a) The **Cauchy distribution** with location $\mu$ and scale $\sigma$ has

$$
F(x;\mu,\sigma)=\frac12+\frac1\pi\arctan\frac{x-\mu}{\sigma},\qquad F^{-1}(u;\mu,\sigma)=\mu+\sigma\tan\Big[\pi\Big(u-\frac12\Big)\Big].
$$

(b) The **exponential distribution** $\mathrm{Exp}(\lambda)$, with mean $\mu=1/\lambda$, has

$$
F(x)=1-\mathrm{e}^{-\lambda x},\qquad F^{-1}(u)=-\frac{\log(1-u)}{\lambda}=-\mu\log(1-u).
$$

(c) For a discrete distribution, the grid approach of §9.2.1 is precisely the inversion of the discrete distribution function.

:::

It is sometimes easier to work with the **survival function** $S(x)=1-F(x)$. Since $U$ and $1-U$ are both uniform, $S^{-1}(U)$ is also a draw from $F$; for the exponential distribution, $S^{-1}(u)=-\mu\log u$ saves one subtraction.

The method gives draws from the exact distribution, with no grid to choose. Its drawbacks are of a practical kind:

- Although the density may be simple, the distribution function and its inverse often have no closed form (normal, gamma, beta). They must then be computed numerically. For the normal distribution there are rational approximations accurate to machine precision (R's default normal generator is inversion with such an approximation), but for gamma and beta distributions the quantile function requires iterative root finding, which is too slow for large simulations and loses accuracy far in the tails.
- For a discrete distribution with many classes, finding the index $i$ in step 5 may require many comparisons. For this reason R draws binomial variates by inversion only when the mean $np$ is below $30$, and uses a rejection algorithm otherwise.
- The method is intrinsically one-dimensional, because a multivariate distribution has no single quantile function. Multivariate targets need a factorization into conditional distributions, each inverted in turn.

### 9.2.3. Relationships with Other Distributions

Many distributions can be generated as functions of variables that are easy to draw. For example:

$$
\begin{aligned}
&X\sim\mathcal{N}(\mu,\sigma^2)\ \Rightarrow\ \mathrm{e}^X\sim\mathrm{LN}(\mu,\sigma^2);\qquad X\sim\mathcal{N}(0,1)\ \Rightarrow\ X^2\sim\chi^2_1;\qquad U\sim\mathrm{U}(0,1)\ \Rightarrow\ -\log U\sim\mathrm{Exp}(1);\\
&X_\alpha\sim\Gamma(\alpha,1),\ X_\beta\sim\Gamma(\beta,1)\text{ independent}\ \Rightarrow\ \frac{X_\alpha}{X_\alpha+X_\beta}\sim\mathrm{Beta}(\alpha,\beta).
\end{aligned}
$$
The **log-normal distribution**, the **chi-square distribution** and the **beta distribution** are thus reduced to normal, uniform and **gamma distribution** draws. Further examples used in this course: a scaled inverse-$\chi^2$ draw is $\nu s^2/Z$ with $Z\sim\chi^2_\nu$ ([3.7.3](/3.7.3)); a **Dirichlet distribution** draw is a vector of independent $\Gamma(\alpha_j,1)$ variables divided by their sum; a $t_\nu(\mu,\sigma^2)$ draw is $\mu+\sigma Z/\sqrt{V/\nu}$ with $Z\sim\mathcal{N}(0,1)$ and $V\sim\chi^2_\nu$ independent; and the **Box–Muller transform** turns two uniforms into two independent standard normals ([3.5.8](/3.5.8), §8.4). The inverse transform method is the special case $X=F^{-1}(U)$ of this idea.

Such constructions give draws from the correct distribution. On the other hand, many distributions, and in particular most posteriors, have no useful relationship with standard ones, and the constructions can be inefficient, since functions such as $\log$, $\sin$ and $\cos$ are relatively expensive to evaluate.

## 9.3. Rejection Sampling

### 9.3.1. The Algorithm

Rejection sampling, due to von Neumann (1951), simulates from a density $f(x)$ that is not easy to sample directly. The idea is to find a dominating, or majorizing, distribution: a density $g$ that is easy to sample from, and a constant $c$ such that

$$
f(x)\le c\,g(x)\qquad\text{for all }x.
$$
The function $cg$ is called the envelope. Integrating both sides shows $c\ge1$, with equality only if $f=g$.

**Algorithm 9.3.1 (Rejection Sampling)**

1. Sample $x$ from $g$ and compute the acceptance ratio $r(x)=\dfrac{f(x)}{cg(x)}\le1$.
2. Sample $u\sim\mathrm{U}(0,1)$. If $u\le r(x)$, accept and return $x$; if $u>r(x)$, reject and go back to step 1.

Step 2 amounts to flipping a biased coin with success probability $r(x)$.

**Theorem 9.3.1** The values returned by Algorithm 9.3.1 are draws from $f$. Each proposal is accepted with probability $1/c$, so the number of proposals per returned value is geometric with mean $c$.

**Proof** Let $I$ be the indicator that a proposal $X\sim g$ is accepted. Given $X=x$, $I=1$ with probability $r(x)$, so

$$
\mathbb{P}(I=1)=\int\mathbb{P}(I=1\mid X=x)\,g(x)\,\mathrm{d}x=\int\frac{f(x)}{cg(x)}g(x)\,\mathrm{d}x=\frac1c.
$$
By **Bayes' theorem** the density of an accepted value is

$$
p(x\mid I=1)=\frac{\mathbb{P}(I=1\mid X=x)\,g(x)}{\mathbb{P}(I=1)}=\frac{f(x)}{cg(x)}g(x)\cdot c=f(x).
$$
Successive proposals are independent, so the returned values are independent, and the waiting time for the first acceptance is geometric with success probability $1/c$. $\square$

A more formal proof, which also covers the independence of successive outputs in detail, is [Theorem 8.3.1](/3.5.8#thm-8.3.1) of 3.5.8.

The geometric picture explains the algorithm (Flury, 1990). Given $x\sim g$, the point $(x,\,u\,cg(x))$ is uniformly distributed under the graph of the envelope $cg$, and it is accepted exactly when it also lies under the graph of $f$. Accepted points are therefore uniform under $f$, and their first coordinates have density $f$. The acceptance probability is a ratio of areas,

$$
\frac1c=\frac{\int f(x)\,\mathrm{d}x}{\int cg(x)\,\mathrm{d}x}=\frac{\text{area under }f}{\text{area under }cg}.
$$

Since the expected number of proposals per draw is $c$, the constant should be as small as possible. For a given $g$ the optimal choice is

$$
c=\sup_x\frac{f(x)}{g(x)}.
$$
It need not be determined exactly: any $c$ with $f\le cg$ everywhere gives a correct algorithm, only a less efficient one.

**Example 9.3.1 (Half-Normal Distribution)** The half-normal density is

$$
f(x)=2\phi(x)\boldsymbol{1}\{x\ge0\}=\sqrt{\frac2\pi}\exp\Big(-\frac{x^2}{2}\Big)\boldsymbol{1}\{x\ge0\},
$$
where $\phi$ is the standard normal density. Use $\mathrm{Exp}(1)$, $g(x)=\mathrm{e}^{-x}\boldsymbol{1}\{x\ge0\}$, as the dominating density. Then

$$
\frac{f(x)}{g(x)}=\sqrt{\frac2\pi}\exp\Big(x-\frac{x^2}{2}\Big)=\sqrt{\frac2\pi}\,\mathrm{e}^{1/2}\exp\Big(-\frac{(x-1)^2}{2}\Big),
$$
which is maximal at $x=1$. The optimal constant is $c=\sqrt{2/\pi}\,\mathrm{e}^{1/2}\approx1.315$, so the acceptance rate is $1/c\approx76\%$, and the acceptance ratio is $r(x)=\exp(-\frac12(x-1)^2)$. The scheme is: sample $x\sim\mathrm{Exp}(1)$ and $u\sim\mathrm{U}(0,1)$; accept $x$ if $u\le\exp(-\frac12(x-1)^2)$, otherwise repeat. A QQ plot of the accepted values against the absolute values of $\mathcal{N}(0,1)$ draws lies along the diagonal. In this special case the scheme is not needed, since the half-normal distribution is that of $\lvert Z\rvert$ for $Z\sim\mathcal{N}(0,1)$; [Example 8.3.2](/3.5.8#ex-8.3.2) of 3.5.8 shows the envelope and the samples, and the optimization over the rate of the exponential proposal.

:::

### 9.3.2. Unnormalized Densities

A posterior is usually known only up to a constant, $p(\theta\mid y)\propto p(\theta)p(y\mid\theta)$, and the normalizing constant is hard to compute. Rejection sampling does not need it. Suppose $f$ is known only through $q(x)=bf(x)$ with $b$ unknown, and find $\tilde c$ such that

$$
q(x)\le\tilde c\,g(x)\qquad\text{for all }x.
$$

**Algorithm 9.3.2 (Rejection Sampling with an Unnormalized Density)**

1. Sample $x$ from $g$ and compute $r(x)=\dfrac{q(x)}{\tilde cg(x)}\le1$.
2. Sample $u\sim\mathrm{U}(0,1)$. If $u\le r(x)$, accept and return $x$; otherwise go back to step 1.

Since $q/(\tilde cg)=f/(cg)$ with $c=\tilde c/b$, this is Algorithm 9.3.1 with a valid envelope, and its output is a sample from $f$. Everything is the same except that the unnormalized density is used in place of the normalized one. The acceptance probability is

$$
\int\frac{q(x)}{\tilde cg(x)}g(x)\,\mathrm{d}x=\frac{1}{\tilde c}\int q(x)\,\mathrm{d}x=\frac{b}{\tilde c},
$$
which is unknown in general, but can be estimated by the observed proportion of acceptances; that proportion, times $\tilde c$, is in turn an estimate of the normalizing constant $b$.

**Example 9.3.2 (The Prior as Proposal)** Take as proposal the **prior distribution**, $g(\theta)=p(\theta)$, and as unnormalized target $q(\theta\mid y)=p(\theta)p(y\mid\theta)$. Then $q/g=p(y\mid\theta)$ is the **likelihood function**, and the smallest valid constant is its maximum, $\tilde c=p(y\mid\hat\theta)$ with $\hat\theta$ the **maximum likelihood estimator**. A draw $\theta\sim p(\theta)$ is accepted with probability $p(y\mid\theta)/p(y\mid\hat\theta)$, the likelihood relative to its maximum. The overall acceptance probability is

$$
\frac{\int p(\theta)p(y\mid\theta)\,\mathrm{d}\theta}{p(y\mid\hat\theta)}=\frac{p(y)}{p(y\mid\hat\theta)},
$$
the marginal likelihood relative to the maximized likelihood. This scheme needs nothing but the ability to simulate from the prior and evaluate the likelihood, but it is efficient only when the prior and the posterior are similar. With informative data the posterior occupies a small fraction of the prior's range, and the acceptance rate becomes tiny; for $n$ observations of a regular $d$-parameter model it decreases roughly like $n^{-d/2}$.

:::

### 9.3.3. Choosing the Proposal

*Discrete and multivariate targets.* The argument of Theorem 9.3.1 goes through for discrete random variables and for vectors, with integrals over a density replaced by integrals over a general measure; for a discrete problem they become sums over the probability mass function. In higher dimensions, however, the majorizing constants tend to be much larger: if the target and the proposal are products of $d$ independent components, the constant is the product of the $d$ one-dimensional constants, so the acceptance rate decreases exponentially in $d$.

*Tails.* The condition $cg(\theta)\ge p(\theta\mid y)$ requires the proposal to have tails at least as heavy as those of the target. Suppose the target is the standard Cauchy and the proposal is the standard normal. Then

$$
\frac{p(\theta\mid y)}{g(\theta)}=\frac{1/[\pi(1+\theta^2)]}{(2\pi)^{-1/2}\mathrm{e}^{-\theta^2/2}}=\sqrt{\frac2\pi}\,\frac{\mathrm{e}^{\theta^2/2}}{1+\theta^2}\to\infty\qquad(\lvert\theta\rvert\to\infty),
$$
since $\mathrm{e}^{-a}$ converges to zero faster than $1/(1+a)$. There is no constant $c$ with $cg(\theta)\ge p(\theta\mid y)$ for all $\theta$. The reverse choice, a Cauchy proposal for a normal target, works with $c\approx1.52$ (Question 3).

*Shape.* For a given $g$, the constant is determined by $c=\sup f/g$; the choice of $g$ therefore also determines the acceptance rate. A good proposal is "close" to $f$ in shape, so that the ratio $f/g$ is nearly constant. In practice one often chooses a parametric family (normal or $t$ distributions with various locations and scales, for instance centered at the posterior mode with the scale of the normal approximation of [3.7.5](/3.7.5)) and uses the member with the smallest $c$.

To summarize: rejection sampling gives draws from the exact distribution, it is extremely flexible and works for a wide range of problems, and for many problems there are good majorizing distributions, in particular for log-concave densities (§9.3.4). Its disadvantages are that it may be inefficient when $c$ is large, as it typically is in high dimensions, and that it is not always clear how to pick the majorizing distribution.

### 9.3.4. Adaptive Rejection Sampling

For one important class of densities, a good envelope can be constructed automatically and improved while the sampler runs.

**Definition 9.3.1 (Log-Concave Density)** A density $f$ is a **log-concave density** if $h(x)=\log f(x)$ is a concave function on an interval (the support of $f$).

Normal densities, gamma densities with shape $\alpha\ge1$, beta densities with $\alpha,\beta\ge1$ and the logistic density are log-concave; $t$ and Cauchy densities are not. Since a sum of concave functions is concave, a posterior with a log-concave prior and a log-concave likelihood is log-concave. This holds, for instance, for **logistic regression** with normal priors, and for many of the one-dimensional full conditional distributions encountered in a Gibbs sampler.

For a concave $h$, every tangent line lies above the graph, and every chord between two points of the graph lies below it. Given abscissae $x_1<\dots<x_k$ at which $h$ and $h'$ have been evaluated, define the upper hull $u_k$ and the lower hull $l_k$:

$$
u_k(x)=\min_{1\le j\le k}\big[h(x_j)+h'(x_j)(x-x_j)\big],\qquad
l_k(x)=\frac{(x_{j+1}-x)h(x_j)+(x-x_j)h(x_{j+1})}{x_{j+1}-x_j}\quad\text{for }x_j\le x\le x_{j+1},
$$
with $l_k(x)=-\infty$ outside $[x_1,x_k]$. Then $l_k\le h\le u_k$. The function $\exp u_k$ is piecewise exponential, so the normalized envelope $s_k(x)=\exp u_k(x)/\int\exp u_k(x')\,\mathrm{d}x'$ can be sampled exactly by inverting the distribution function piece by piece; $\exp l_k$ is a squeezing function below the target. If the support is unbounded, the tangents at $x_1$ and $x_k$ must slope up and down respectively, $h'(x_1)>0>h'(x_k)$, so that the envelope is integrable.

**Algorithm 9.3.3 (Adaptive Rejection Sampling)** Gilks and Wild (1992). Start with a few abscissae $x_1<\dots<x_k$ satisfying the condition above. To produce each draw:

1. Sample $x^*\sim s_k$ and $w\sim\mathrm{U}(0,1)$.
2. *Squeezing test.* If $w\le\exp[l_k(x^*)-u_k(x^*)]$, accept $x^*$; $h$ need not be evaluated.
3. *Rejection test.* Otherwise evaluate $h(x^*)$ and $h'(x^*)$. If $w\le\exp[h(x^*)-u_k(x^*)]$, accept $x^*$, otherwise reject it. In either case add $x^*$ to the abscissae and update $u_k$ and $l_k$.

Step 3 is ordinary rejection sampling with the envelope $\exp u_k$ for the unnormalized target $\exp h$ (Algorithm 9.3.2), and step 2 is a shortcut that accepts without evaluating $h$ when the point lies under the squeeze, which is below the target. Every evaluation of $h$ refines both hulls exactly where the envelope was loose, so the acceptance rate and the squeeze rate increase toward $1$ as sampling proceeds, and the number of evaluations of the possibly expensive log density grows only slowly with the number of draws. A derivative-free variant builds the upper hull from extended chords instead of tangents, and adaptive rejection Metropolis sampling (Gilks, Best and Tan, 1995) adds a Metropolis–Hastings correction for densities that are not log-concave. Adaptive rejection sampling was the workhorse for one-dimensional updates in early general-purpose Gibbs samplers such as BUGS ([Remark 8.3.1](/3.5.8#rem-8.3.1) of 3.5.8).

![Adaptive rejection sampling for the log-concave density Gamma(4, 1). Left: on the log scale, the tangents at three abscissae form the upper hull and the chords form the lower hull. Middle: on the density scale, the piecewise exponential envelope and the squeeze, with the approximate proportion of proposals accepted and the proportion accepted already by the squeezing test. Right: after three more abscissae have been added, both are close to 1.](./plots/ars_envelope.py)

## 9.4. Importance Sampling

### 9.4.1. Motivation

Recall from §9.1.2 that probabilities, integrals and sums can be written as expectations, $\mathbb{E}[\boldsymbol{1}_A(Y)]$, $(b-a)\mathbb{E}[q(U)]$ or $\mathbb{E}[q(W)]/p$. Nothing requires $U$ or $W$ to be uniformly distributed: for most problems several Monte Carlo estimators can be proposed, and a better one has a smaller variance for the same computational effort.

**Example 9.4.1 (A Rare Event)** In quality control we may need the probability $\mathbb{P}(X-\mu>5\sigma)$ for $X\sim\mathcal{N}(\mu,\sigma^2)$, equivalently $\mathbb{P}(X>5)$ for $X\sim\mathcal{N}(0,1)$. The direct estimate is

$$
\mathbb{P}(X>5)=\mathbb{E}[\boldsymbol{1}\{X>5\}]\approx\frac1n\sum_{i=1}^n\boldsymbol{1}\{x_i>5\},\qquad x_i\overset{\text{iid}}{\sim}\mathcal{N}(0,1).
$$
The true value is $\mathbb{P}(X>5)\approx2.866516\times10^{-7}$, so on average only $3$ of $10^7$ draws exceed $5$: almost all the computation is spent on draws that contribute nothing, and the estimate is very inefficient.

:::

The opposite situation shows what goes wrong. Suppose we want $\int_0^1f(x)\,\mathrm{d}x$ for a function with $f(x)=0$ outside $[0,1]$. With $U\sim\mathrm{U}(0,1)$ and $W\sim\mathrm{U}(0,5)$,

$$
\int_0^1f(x)\,\mathrm{d}x=\mathbb{E}[f(U)]\approx\frac1n\sum_{i=1}^nf(u_i),\qquad\int_0^1f(x)\,\mathrm{d}x=5\,\mathbb{E}[f(W)]\approx\frac5n\sum_{i=1}^nf(w_i).
$$
Both are unbiased, but the second is "barely relevant sampling": four fifths of the draws fall where $f=0$, and the variance per draw is $5\int_0^1f^2-I^2$ instead of $\int_0^1f^2-I^2$, with $I=\int_0^1f$. The lesson is to choose a good distribution from which to simulate, and to multiply the integrand by $1$, in the form of a ratio of densities, so as to obtain the expectation of a quantity that varies less than the original integrand over the region of integration.

### 9.4.2. Weighted Samples

Let $f$ be the target density and $g$ a proposal density that is easy to sample, with $g(x)>0$ wherever $f(x)>0$. If $x\sim g$, its **importance weight** is

$$
w_x=w(x)=\frac{f(x)}{g(x)},
$$
and the pair $(x,w_x)$ is a weighted sample of $f$. The basic property of weighted samples is

$$
\mathbb{E}_f[h(X)]=\int h(x)f(x)\,\mathrm{d}x=\int h(x)\,w(x)\,g(x)\,\mathrm{d}x=\mathbb{E}_g[h(X)w(X)].
$$

**Proposition 9.4.1** Let $x_1,\dots,x_n\overset{\text{iid}}{\sim}g$ and

$$
\hat h=\frac1n\sum_{i=1}^nh(x_i)\,w(x_i). \tag{9.2}
$$
If $\mathbb{E}_f\lvert h(X)\rvert<\infty$, then $\hat h$ is an **unbiased estimator** of $\mathbb{E}_f[h(X)]$ and, by the **strong law of large numbers**, a **consistent estimator**: $\hat h\to\mathbb{E}_f[h(X)]$ with probability one as $n\to\infty$. Its variance is finite if and only if $\mathbb{E}_f[h^2(X)w(X)]<\infty$.

**Proof** Each term $h(x_i)w(x_i)$ has expectation $\mathbb{E}_g[hw]=\mathbb{E}_f[h]$ by the identity above, which gives unbiasedness; the terms are i.i.d. with finite mean, which gives consistency. Finally $\mathbb{E}_g[h^2w^2]=\int h^2\frac{f^2}{g^2}g=\mathbb{E}_f[h^2w]$. $\square$

This is **importance sampling**, studied in general in [3.5.9](/3.5.9) (§9.2). Strictly, the support condition is only needed where $h(x)f(x)\ne0$. The estimator does not produce draws from $f$; it estimates expectations under $f$ from draws from $g$, and no draw is discarded.

**Example 9.4.2 (Mean of a Truncated Normal Distribution)** We want the mean of a standard normal distribution truncated to $[0,1]$, whose density is

$$
f(x)=\frac{\phi(x)}{\int_0^1\phi(z)\,\mathrm{d}z},\qquad0\le x\le1.
$$
*Brute force simulation* takes draws $x_i$ from $\mathcal{N}(0,1)$ and keeps only those in $[0,1]$, estimating the mean by

$$
\frac{\sum_{i=1}^nx_i\boldsymbol{1}\{x_i\in[0,1]\}}{\sum_{i=1}^n\boldsymbol{1}\{x_i\in[0,1]\}}.
$$
This is rejection sampling with the proposal $\mathcal{N}(0,1)$, and it is inefficient when $\sum_i\boldsymbol{1}\{x_i\in[0,1]\}\ll n$: here only $34\%$ of the draws are kept. Importance sampling instead draws from $\mathrm{U}(0,1)$, so that $g(x)=1$ on $[0,1]$ and the weights are $w_i=f(x_i)=\phi(x_i)/\int_0^1\phi(z)\,\mathrm{d}z$; the estimate is $\frac1n\sum_ix_iw_i$, and no draw is rejected. The exact value is $\frac{\phi(0)-\phi(1)}{\Phi(1)-\Phi(0)}=0.4599$.

:::

**Example 9.4.3 (A Rare Event, Continued)** For $\mathbb{P}(X>5)$ in Example 9.4.1, a natural proposal puts all its mass beyond $5$ and decreases at an exponential rate: $5+\mathrm{Exp}(1)$, that is $g(x)=\mathrm{e}^{5-x}$ for $x>5$. The function $h(x)f(x)=\boldsymbol{1}\{x>5\}\phi(x)$ vanishes outside the support of $g$, so the estimate is the average of the weights $w(x_i)=\phi(x_i)\mathrm{e}^{x_i-5}$. In R:

```r
n <- 10000
x <- rexp(n) + 5                 # draws from g(x) = exp(5 - x), x > 5
w <- dnorm(x) * exp(x - 5)       # weights f(x) / g(x); h(x) = 1 on the support of g
mean(w)                          # importance sampling estimate of P(X > 5)
sum(rnorm(n) > 5) / n            # direct Monte Carlo estimate
```

Two runs gave

```text
[1] 2.920778e-07
[1] 0
```
and

```text
[1] 2.92517e-07
[1] 0
```
With $10^4$ draws, importance sampling estimates the probability with a relative standard error of about $1.4\%$, while the direct estimate is $0$. The direct method would need about $2\times10^{10}$ draws for the same precision.

:::

### 9.4.3. Choosing the Proposal

The variance of the estimator Eq. (9.2) is

$$
\operatorname{Var}(\hat h)=\frac1n\operatorname{Var}_g[h(X)w(X)]=\frac1n\Big(\int\frac{h^2(x)f^2(x)}{g(x)}\,\mathrm{d}x-\big(\mathbb{E}_f[h(X)]\big)^2\Big),
$$
and the proposal should make it small.

**Theorem 9.4.1 (Optimal Proposal)** Among all proposal densities, the variance of $\hat h$ is minimized by

$$
g^*(x)=\frac{\lvert h(x)\rvert f(x)}{\int\lvert h(x')\rvert f(x')\,\mathrm{d}x'},
$$
and the minimal variance is $\frac1n\big[\big(\mathbb{E}_f\lvert h(X)\rvert\big)^2-\big(\mathbb{E}_f[h(X)]\big)^2\big]$. In particular, if $h\ge0$ (or $h\le0$), the optimal estimator has variance zero.

**Proof** Only the first term of the variance depends on $g$. By the **Cauchy–Schwarz inequality**, for any density $g$,

$$
\Big(\int\lvert h\rvert f\,\mathrm{d}x\Big)^2=\Big(\int\frac{\lvert h\rvert f}{\sqrt g}\sqrt g\,\mathrm{d}x\Big)^2\le\int\frac{h^2f^2}{g}\,\mathrm{d}x\cdot\int g\,\mathrm{d}x=\int\frac{h^2f^2}{g}\,\mathrm{d}x,
$$
with equality if and only if $\lvert h\rvert f/\sqrt g$ is proportional to $\sqrt g$, that is $g\propto\lvert h\rvert f$. If $h\ge0$ then $\mathbb{E}_f\lvert h\rvert=\mathbb{E}_f h$ and the minimum is $0$: every weighted term $h(x)w(x)$ equals the constant $\int hf$. $\square$

The zero-variance proposal is not usable, since its normalizing constant $\int\lvert h\rvert f$ is (for $h\ge0$) the very quantity we want to compute. Its value is as a guide: a good proposal is roughly proportional to $\lvert h\rvert f$. In the simplest case $h=1$, which is relevant when the same draws are used for many functions $h$, a good proposal is as close as possible to being proportional to $f$. What matters is the shape, not the height: the importance weights are allowed to be large or small, but they should be nearly constant.

The second requirement is about the tails. The variance is finite only if $\int h^2f^2/g<\infty$, which fails, or is practically infinite, when $g$ decreases much faster than $\lvert h\rvert f$ in the tails. Then the weights are usually small and occasionally enormous: most estimates are too low, and a few are far too high.

**Example 9.4.4 (Shape and Tails of the Proposal)** We estimate the area under the standard normal density between $-50$ and $50$, which is $1$ to many digits, with $n=1000$ draws from three proposals: $\mathrm{U}(-50,50)$, $t_1$ and $t_{30}$. The estimate is the average of the weights $\phi(x_i)/g(x_i)$ over the draws in $(-50,50)$, and the experiment is repeated $5000$ times. All three estimators are unbiased, but their standard deviations are $0.16$, $0.018$ and $0.0017$: the uniform proposal has the right tails but the wrong shape, the $t_1$ proposal is closer in shape, and $t_{30}$ is almost proportional to the target. Conversely, take as target the Cauchy ($t_1$) density truncated to $(-50,50)$ and renormalized so that the exact area is $1$, and as proposal the standard normal, whose tails are much lighter. The estimates are mostly near $0.85$, below the true value, because the normal draws almost never reach the Cauchy tails; when they do, the weight is huge, and a few dozen of the $5000$ estimates exceed $1.5$. The tails of the distributions matter.

![Importance sampling estimates of an area equal to 1. Top: target densities (solid) and proposal densities (dashed). Bottom: histograms of 5000 estimates, each from n = 1000 draws, with their standard deviation; estimates beyond the range are counted in the last bin. The three proposals for the normal target differ in shape; the normal proposal for the Cauchy target has too light tails.](./plots/importance_proposals.py)

:::

In summary, a good importance sampling proposal $g$ should satisfy the following:

1. $g(x)>0$ whenever $h(x)f(x)\ne0$;
2. $g$ is close to being proportional to $\lvert h\rvert f$ (to $f$ if many functions $h$ are of interest);
3. $g$ has the same or heavier tails than $f$, so that the weights are bounded or at least have finite variance;
4. it is easy to simulate values from $g$;
5. it is easy to compute the density $g(x)$ at any value $x$ that might be realized.

Fulfilling this wish list in high-dimensional spaces, where Monte Carlo methods are most useful, is often a tough task. Standard choices are a $t$ distribution with few degrees of freedom centered at the posterior mode with the scale of the normal approximation ([3.7.5](/3.7.5), §5.3), mixtures of such distributions for multimodal targets, and posteriors based on part of the data (Example 9.4.5).

### 9.4.4. The Effective Sample Size

How much is a weighted sample worth? We compare the variance of the importance sampling estimate Eq. (9.2) with that of an average of $n_{\mathrm{eff}}$ independent draws from $f$ itself. Write $h_x=h(x)$. As in §9.4.3,

$$
\begin{aligned}
\operatorname{Var}(\hat h)&=\frac1n\operatorname{Var}_g[h_xw_x]=\frac1n\Big[\mathbb{E}_g(h_x^2w_x^2)-\big(\mathbb{E}_gh_xw_x\big)^2\Big]=\frac1n\Big[\mathbb{E}_f(h_x^2w_x)-\big(\mathbb{E}_fh_x\big)^2\Big].
\end{aligned}
$$
To separate the effect of the weights from that of $h$, assume that $h_x^2$ and $w_x$ are uncorrelated under $f$. Since $\mathbb{E}_f(w_x)=\int\frac{f^2}{g}=\mathbb{E}_g(w_x^2)$,

$$
\operatorname{Var}(\hat h)\approx\frac1n\Big[\mathbb{E}_f(h_x^2)\,\mathbb{E}_f(w_x)-\big(\mathbb{E}_fh_x\big)^2\Big]=\frac1n\Big[\mathbb{E}_f(h_x^2)\,\mathbb{E}_g(w_x^2)-\big(\mathbb{E}_fh_x\big)^2\Big].
$$
An average of $n_{\mathrm{eff}}$ independent draws from $f$ has variance

$$
\operatorname{Var}_f\Big[\frac1{n_{\mathrm{eff}}}\sum_{i=1}^{n_{\mathrm{eff}}}h(x_i)\Big]=\frac1{n_{\mathrm{eff}}}\operatorname{Var}_f[h(x)]=\frac1{n_{\mathrm{eff}}}\Big[\mathbb{E}_fh_x^2-\big(\mathbb{E}_fh_x\big)^2\Big].
$$
Equating the two variances, and then taking $\mathbb{E}_fh_x\approx0$ in this step (after centering $h$), gives

$$
n_{\mathrm{eff}}=n\cdot\frac{\mathbb{E}_fh_x^2-(\mathbb{E}_fh_x)^2}{\mathbb{E}_f(h_x^2)\,\mathbb{E}_g(w_x^2)-(\mathbb{E}_fh_x)^2}\approx\frac{n}{\mathbb{E}_g(w_x^2)}\approx\frac{n}{\frac1n\sum_{i=1}^nw^2(x_i)}. \tag{9.3}
$$
Since $\mathbb{E}_gw_x=1$, we have $\mathbb{E}_g(w_x^2)=1+\operatorname{Var}_g(w_x)\ge1$, so $n_{\mathrm{eff}}\le n$, with equality only for constant weights ($g=f$). A large value of $\frac1n\sum_iw^2(x_i)$, that is, highly variable weights, means poor performance.

**Definition 9.4.1 (Effective Sample Size of Importance Sampling)** Let $\tilde w_i=w(x_i)/\sum_{j=1}^nw(x_j)$ be the normalized importance weights, which sum to one. The effective sample size of the weighted sample is

$$
S_{\mathrm{eff}}=\frac{1}{\sum_{i=1}^n\tilde w_i^2}=\frac{\big(\sum_{i=1}^nw(x_i)\big)^2}{\sum_{i=1}^nw^2(x_i)}.
$$

This is Eq. (9.3) with the factor $\frac1n\sum_iw(x_i)\approx1$ written out, so that it does not depend on the scale of the weights and can be used with unnormalized weights (§9.4.5). It ranges from $1$, when one draw carries all the weight, to $n$, when all weights are equal. The **effective sample size** is a rough guide only: the derivation assumed that $h^2$ and the weights are uncorrelated, and the estimate is itself noisy. In particular, when the variance of the weights is infinite, $S_{\mathrm{eff}}$ can look acceptable in a given run while the estimates are unreliable (Example 9.4.4 with the Cauchy target gives a median $S_{\mathrm{eff}}$ of about $500$ out of $1000$). A small $S_{\mathrm{eff}}$ is a reliable warning; a large one is not a guarantee. A more robust diagnostic, the shape of the Pareto distribution fitted to the largest weights, underlies Pareto-smoothed importance sampling, which is used in practice to compute **leave-one-out cross-validation** from a single posterior sample ([3.7.8](/3.7.8), §8.5).

### 9.4.5. Unnormalized Densities

In Bayesian computation the target is known only through an unnormalized density, $q(\theta\mid y)$, written $q(x)$ for short. The weights $f/g$ are then not computable, but the ratios

$$
w_u(x)=\frac{q(x)}{g(x)}
$$
are, and the unknown constant cancels in a ratio:

$$
\mathbb{E}_f[h(X)]=\int h(x)\frac{q(x)}{\int q(x')\,\mathrm{d}x'}\,\mathrm{d}x=\frac{\int h(x)q(x)\,\mathrm{d}x}{\int q(x)\,\mathrm{d}x}=\frac{\mathbb{E}_g[h(X)w_u(X)]}{\mathbb{E}_g[w_u(X)]}.
$$
With $x_1,\dots,x_n\overset{\text{iid}}{\sim}g$, both expectations are estimated by sample means:

$$
\mathbb{E}_f[h(X)]\approx\frac{\frac1n\sum_{i=1}^nh(x_i)w_u(x_i)}{\frac1n\sum_{i=1}^nw_u(x_i)}=\sum_{i=1}^n\tilde w_i\,h(x_i),\qquad\tilde w_i=\frac{w_u(x_i)}{\sum_{j=1}^nw_u(x_j)}. \tag{9.4}
$$

This is **self-normalized importance sampling** ([Proposition 9.2.3](/3.5.9#prop-9.2.3) of 3.5.9). Unlike Eq. (9.2), the estimator Eq. (9.4) is not unbiased, because it is a ratio of two random quantities, but its bias is of order $1/n$. It is consistent: by the strong law of large numbers the numerator converges to $\mathbb{E}_g[hw_u]$ and the denominator to $\mathbb{E}_g[w_u]>0$, so the ratio converges to $\mathbb{E}_f[h(X)]$ with probability one. Its approximate variance follows from the **delta method**. The effective sample size is that of Definition 9.4.1, computed from the normalized weights $\tilde w_i$; the unknown constant does not matter. As a by-product, $\frac1n\sum_iw_u(x_i)$ is an unbiased estimate of $\int q(x)\,\mathrm{d}x$; with $q=p(\theta)p(y\mid\theta)$, this is an estimate of the marginal likelihood $p(y)$.

**Example 9.4.5 (Normal Data with Censored Observations)** Suppose we have observed $x_1,\dots,x_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$, and $m$ more "imprecise" observations $x_{n+1},\dots,x_{n+m}$ from the same distribution whose exact values were not recorded, but which are known to be positive: they are censored at $0$ (**censoring**). How do we infer $(\mu,\sigma^2)$ with the **non-informative prior** $p(\mu,\sigma^2)\propto\sigma^{-2}$?

The extra information enters through its likelihood,

$$
\prod_{k=1}^m\mathbb{P}(x_{n+k}>0\mid\mu,\sigma)=\Phi^m\Big(\frac\mu\sigma\Big),
$$
where $\Phi$ is the standard normal distribution function. The posterior is therefore

$$
p(\mu,\sigma^2\mid x_1,\dots,x_n,\,x_{n+1}>0,\dots,x_{n+m}>0)\propto p(\mu,\sigma^2\mid x_1,\dots,x_n)\,\Phi^m\Big(\frac\mu\sigma\Big),
$$
where the first factor is the posterior based on the exact observations alone. By [3.7.3](/3.7.3) (§3.3) it is the **normal-inverse-chi-square distribution**

$$
\sigma^2\mid x_{1:n}\sim\mathrm{Inv}\text{-}\chi^2(n-1,s^2),\qquad\mu\mid\sigma^2,x_{1:n}\sim\mathcal{N}(\bar x,\sigma^2/n),
$$
with $\bar x$ and $s^2$ the mean and variance of the exact observations. The full posterior is not of a standard form, but this factorization suggests an importance sampler: take the partial posterior as the proposal $g$, which is easy to sample (draw $\sigma^2$, then $\mu$) and evaluate. With the unnormalized target $q=g\cdot\Phi^m(\mu/\sigma)$, the weights are simply

$$
w_u(\mu,\sigma^2)=\Phi^m\Big(\frac\mu\sigma\Big),
$$
the likelihood of the censored observations. No normalizing constant is needed, and the weights are bounded by $1$, so the variance of the estimator is always finite: the proposal automatically has heavier tails than the target, because the target is the proposal multiplied by a bounded likelihood.

For illustration, we simulated $n=10$ exact observations from $\mathcal{N}(0.5,1)$, giving $\bar x=0.585$ and $s^2=0.610$, and assumed $m=10$ further observations known to be positive. From $S=20\,000$ draws of the proposal, the effective sample size is $S_{\mathrm{eff}}=9174$. The censored observations shift the posterior: the posterior mean of $\mu$ moves from $0.58$ under the proposal to $0.80$ after weighting (a grid computation of the exact posterior gives $0.80$), the posterior mean of $\sigma$ decreases from $0.85$ to $0.76$, and $\mathbb{P}(\mu>0\mid\text{all data})$ rises from $0.978$ to $0.9999$. The importance weights favor large values of $\mu/\sigma$, as they should, since ten positive values have been observed in addition to the exact ones.

![Normal data with ten observations censored at 0 (simulated data). Left: draws from the proposal, the posterior given the exact observations only (gray), and draws obtained by sampling importance resampling (red), with contours of the exact posterior. Middle: marginal posterior of μ from the proposal draws, from the resampled draws, and computed exactly on a grid. Right: the normalized importance weights in decreasing order, multiplied by the number of draws.](./plots/censored_normal_sir.py)

:::

### 9.4.6. Sampling Importance Resampling

Importance sampling yields weighted draws, which suffice for expectations, but some uses require an unweighted sample from $f$: a histogram, a sample passed on to another computation, or posterior predictive simulation. Resampling converts the weighted sample into an approximately unweighted one.

**Algorithm 9.4.1 (Sampling Importance Resampling)** Suppose $x_1,\dots,x_n$ have been drawn from $g$ and their importance weights $w(x_i)$ computed (with $f$ or with an unnormalized $q$).

1. Sample a value $\tilde x_1$ from the set $\{x_1,\dots,x_n\}$, where the probability of sampling each $x_i$ is proportional to its weight $w(x_i)$.
2. Repeat, sampling $k-1$ more values $\tilde x_2,\dots,\tilde x_k$ in the same way.

The result $\{\tilde x_1,\dots,\tilde x_k\}$ is a sample of size $k$ from (approximately) $f$.

The resampled values all have equal weights, and the weights may be computed from an unnormalized density, since only their relative sizes enter. The resampled values are only approximately distributed according to $f$: conditionally on the original draws, they come from the weighted empirical distribution $\sum_i\tilde w_i\delta_{x_i}$, which converges to $f$ as $n\to\infty$ by the consistency of Eq. (9.4). Resampling cannot create information: the result contains at most as many distinct values as the original draws, and when a few weights dominate it contains many copies of the same few points, so the effective sample size of §9.4.4 should be checked before resampling.

The algorithm as stated samples with replacement. A common recommendation is to sample without replacement (once a value is selected, it is removed and the remaining weights renormalized), with $k$ much smaller than $n$, for instance $n=5000$ proposal draws and $k=1000$ resampled ones. Without replacement, a few draws with very large weights cannot be repeated many times, which guards against the degenerate case in which the resample consists of copies of a few points; in the limit of a very large $n$ relative to $k$ the two versions agree. In Example 9.4.5 we resampled $k=2000$ of the $20\,000$ draws without replacement; the histogram of the resampled $\mu$ values agrees with the exact marginal posterior (figure above), and their mean is $0.79$.

## Summary

| Method | Requires | Output | Advantages | Disadvantages |
|---|---|---|---|---|
| grid approach (Algorithm 9.2.1) | $q$ evaluable on a grid | draws from a discrete approximation | quick, any density, few dimensions | approximate; grid size and range; cost $n^d$ |
| inverse transform (Proposition 9.2.1) | $F^{-1}$ | exact draws | exact, no tuning | $F^{-1}$ often unavailable or slow; one-dimensional |
| relationships between distributions (§9.2.3) | a known representation | exact draws | exact | few distributions have one; cost of $\log$, $\sin$, $\cos$ |
| rejection sampling (Algorithms 9.3.1–9.3.2) | $g$ and $c$ with $q\le cg$ | exact draws | exact, flexible, $q$ unnormalized | acceptance rate $b/c$ may be tiny; $g$ needs tails at least as heavy as $f$ |
| adaptive rejection sampling (Algorithm 9.3.3) | log-concave target, $h=\log q$ and $h'$ | exact draws | automatic envelope; acceptance rate $\to1$ | one-dimensional; log-concavity |
| importance sampling, Eq. (9.2) and Eq. (9.4) | $g$ with $g>0$ where $hf\ne0$ | weighted draws | no rejection; rare events; $q$ unnormalized (self-normalized) | variance may be infinite if $g$ has lighter tails; weights degenerate in high dimensions |
| sampling importance resampling (Algorithm 9.4.1) | importance weights | approximate equally weighted draws | unweighted sample from a weighted one | approximate; duplicates when weights are uneven |

- Bayesian computation reduces to Monte Carlo integration, Eq. (9.1), with draws from a posterior known only through $q(\theta\mid y)=p(\theta)p(y\mid\theta)$ (Definition 9.1.1); the error is $O(S^{-1/2})$ in any dimension.
- Rejection sampling: accept $x\sim g$ with probability $f(x)/[cg(x)]$; acceptance rate $1/c$, optimal $c=\sup f/g$ (Theorem 9.3.1); with $q=bf$ the rate is $b/\tilde c$. A normal proposal cannot dominate a Cauchy target; the prior as proposal accepts with probability $p(y)/p(y\mid\hat\theta)$ (Example 9.3.2).
- Importance sampling: $\mathbb{E}_f h=\mathbb{E}_g[hw]$, $w=f/g$; the estimator is unbiased and consistent (Proposition 9.4.1), optimal with $g\propto\lvert h\rvert f$ (Theorem 9.4.1); shape and tails of $g$ matter (Example 9.4.4).
- Effective sample size $S_{\mathrm{eff}}=1/\sum_i\tilde w_i^2\approx n/\mathbb{E}_g(w^2)$ (Eq. (9.3), Definition 9.4.1): a rough guide, reliable as a warning only.
- With an unnormalized target, use normalized weights, Eq. (9.4): biased but consistent. Proposals built from part of the data or the prior give weights equal to the remaining likelihood (Example 9.4.5).

## Questions

1. Find the acceptance probability of rejection sampling with an unnormalized density $q=bf$ and constant $\tilde c$ (Algorithm 9.3.2), and explain how a run of the algorithm can be used to estimate $b$. For the prior as proposal (Example 9.3.2), what does this estimate?

   **Answer** A proposal is accepted with probability $\int\frac{q(x)}{\tilde cg(x)}g(x)\,\mathrm{d}x=\frac{1}{\tilde c}\int q=\frac b{\tilde c}$. If $N$ proposals yield $A$ acceptances, $A/N$ estimates $b/\tilde c$ (it is a binomial proportion), so $\tilde cA/N$ is an unbiased estimate of $b=\int q$. With $g=p(\theta)$, $q=p(\theta)p(y\mid\theta)$ and $\tilde c=p(y\mid\hat\theta)$, the quantity estimated is $b=p(y)$, the marginal likelihood: $p(y)\approx p(y\mid\hat\theta)\cdot A/N$.
2. In Example 9.3.1 use the proposal $\mathrm{Exp}(\lambda)$ instead of $\mathrm{Exp}(1)$. Find the optimal constant $c(\lambda)$, the rate $\lambda$ that minimizes it, and the acceptance ratio.

   **Answer** $\frac{f(x)}{g(x)}=\frac1\lambda\sqrt{\frac2\pi}\exp(\lambda x-\frac{x^2}2)$, maximal at $x=\lambda$, so $c(\lambda)=\frac1\lambda\sqrt{\frac2\pi}\mathrm{e}^{\lambda^2/2}$. Then $\frac{\mathrm{d}}{\mathrm{d}\lambda}\log c(\lambda)=-\frac1\lambda+\lambda=0$ gives $\lambda=1$ and $c=\sqrt{2\mathrm{e}/\pi}\approx1.315$, as in the example. The acceptance ratio is $r(x)=\frac{f(x)}{c(\lambda)g(x)}=\exp\big(-\frac12(x-\lambda)^2\big)$.
3. Use the standard Cauchy density $g(x)=\frac1{\pi(1+x^2)}$ as a proposal for the standard normal target. Find the optimal $c$ and the acceptance rate. Why can the roles not be exchanged?

   **Answer** $\frac{\phi(x)}{g(x)}=\sqrt{\frac\pi2}(1+x^2)\mathrm{e}^{-x^2/2}$. The derivative of $(1+x^2)\mathrm{e}^{-x^2/2}$ is $x(1-x^2)\mathrm{e}^{-x^2/2}$, so the maximum is at $x=\pm1$ with value $2\mathrm{e}^{-1/2}$, and $c=\sqrt{2\pi}\,\mathrm{e}^{-1/2}\approx1.520$, an acceptance rate of $1/c\approx0.658$. The reverse ratio $g/\phi$ tends to infinity in the tails (§9.3.3), so no envelope exists: a proposal must have tails at least as heavy as the target.
4. Use rejection sampling with the proposal $\mathrm{U}(0,1)$ for the posterior $\mathrm{Beta}(3,3)$, pretending that its normalizing constant is unknown, $q(\theta)=\theta^2(1-\theta)^2$. Find the smallest $\tilde c$, the acceptance rate, and explain how the acceptance rate changes for the posterior $\mathrm{Beta}(y+1,n-y+1)$ when $n$ grows with $y/n=\frac12$.

   **Answer** $q$ is maximal at $\theta=\frac12$, so $\tilde c=q(\frac12)=\frac1{16}$. The acceptance rate is $\frac{\int q}{\tilde c}=16\,\mathrm{B}(3,3)=16\cdot\frac{2!\,2!}{5!}=\frac{16}{30}\approx0.533$. For $\mathrm{Beta}(y+1,n-y+1)$ with $y=n/2$, the acceptance rate is $\mathrm{B}(y+1,y+1)/\big(\frac12\big)^{n}$, the ratio of the area under the density to that of its enclosing rectangle; by Stirling's formula it is approximately $\sqrt{\pi/(2n)}$, since the posterior concentrates in an interval of width $O(n^{-1/2})$ while the uniform proposal keeps spreading over $[0,1]$. This is Example 9.3.2 in miniature: the prior (here uniform) becomes an ever poorer proposal as the data become informative.
5. Show that for estimating $\int_0^1f(x)\,\mathrm{d}x$ the estimator based on $W\sim\mathrm{U}(0,5)$ in §9.4.1 has a larger variance than the one based on $U\sim\mathrm{U}(0,1)$, and interpret this in terms of Theorem 9.4.1.

   **Answer** With $I=\int_0^1f$, $\operatorname{Var}(f(U))=\int_0^1f^2-I^2$, and $\operatorname{Var}(5f(W))=25\,\mathbb{E}[f(W)^2]-I^2=25\cdot\frac15\int_0^1f^2-I^2=5\int_0^1f^2-I^2$, larger by $4\int_0^1f^2$. Both are importance sampling estimators of $\int_0^1f=\mathbb{E}_g[f/g]$, in which the integrand $f$ plays the role of $hf$ in Theorem 9.4.1; the optimal proposal is therefore proportional to $\lvert f\rvert$, which is zero outside $[0,1]$. $\mathrm{U}(0,5)$ wastes $80\%$ of its draws where the integrand vanishes, and $\mathrm{U}(0,1)$ is closer to the optimal shape.
6. A run of importance sampling with $n=5$ draws gives unnormalized weights $(1,1,1,1,6)$. Compute the normalized weights and the effective sample size. With the values $h(x_i)=(0,1,2,3,4)$, compute the self-normalized estimate of $\mathbb{E}_fh$. What would you conclude in practice?

   **Answer** The weights sum to $10$, so $\tilde w=(0.1,0.1,0.1,0.1,0.6)$, and $S_{\mathrm{eff}}=1/(4\cdot0.01+0.36)=1/0.40=2.5$, or equivalently $(\sum w)^2/\sum w^2=100/40$. The estimate is $\sum_i\tilde w_ih(x_i)=0.1(0+1+2+3)+0.6\cdot4=3.0$. Half the nominal sample size is lost and one draw dominates the estimate, so the proposal is poorly matched to the target in the region of the fifth draw; in practice one would increase $n$ substantially, check whether the largest weights keep growing as $n$ increases (a sign of infinite variance), and move or widen the proposal, for instance with heavier tails.
7. Derive the effective sample size formula Eq. (9.3) and state the two approximations used. Show that $n/\mathbb{E}_g(w^2)\le n$ and that $S_{\mathrm{eff}}=n$ only if all weights are equal.

   **Answer** See §9.4.4: equate $\operatorname{Var}(\hat h)=\frac1n[\mathbb{E}_f(h^2w)-(\mathbb{E}_fh)^2]$ with $\frac1{n_{\mathrm{eff}}}\operatorname{Var}_f(h)$. The approximations are (i) $h^2$ and $w$ uncorrelated under $f$, so that $\mathbb{E}_f(h^2w)\approx\mathbb{E}_f(h^2)\mathbb{E}_f(w)$ with $\mathbb{E}_f(w)=\int f^2/g=\mathbb{E}_g(w^2)$, and (ii) $\mathbb{E}_fh\approx0$, giving $n_{\mathrm{eff}}\approx n/\mathbb{E}_g(w^2)$; finally $\mathbb{E}_g(w^2)$ is replaced by its sample mean. Since $\mathbb{E}_gw=\int f=1$, $\mathbb{E}_g(w^2)=1+\operatorname{Var}_g(w)\ge1$. For the sample version, by the Cauchy–Schwarz inequality $(\sum_iw_i)^2\le n\sum_iw_i^2$, so $S_{\mathrm{eff}}\le n$, with equality if and only if all $w_i$ are equal.
8. In Example 9.4.5, why are the weights bounded, and why does this matter? Would the prior $p(\mu,\sigma^2)\propto\sigma^{-2}$ itself be a usable proposal? What happens to the effective sample size when the number $m$ of censored observations grows while $n$ stays fixed?

   **Answer** The weights are the likelihood $\Phi^m(\mu/\sigma)\le1$ of the censored observations, because the proposal is the posterior given the remaining data; bounded weights imply $\mathbb{E}_f(h^2w)\le\mathbb{E}_fh^2$, so the variance is finite for every $h$ with finite posterior variance. The prior is improper and cannot be sampled, so it is not a proposal; even a proper vague prior would be a very poor proposal, since the posterior occupies a small part of its range (Example 9.3.2). As $m$ grows, the censored observations carry more and more information, $\Phi^m(\mu/\sigma)$ becomes a sharply increasing function of $\mu/\sigma$, the target moves away from the proposal (toward large $\mu/\sigma$), and the weights concentrate on the few proposal draws in the upper tail of $\mu/\sigma$; the effective sample size decreases. A proposal that already includes an approximation to the censored likelihood, such as a $t$ approximation at the mode of the full posterior, is then preferable.
