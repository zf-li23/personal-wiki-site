---
title: Posterior Simulation and Large-Sample Theory
description: Learning about a posterior from simulation draws (functions of parameters, joint and marginal sampling), discrete-grid sampling, the normal approximation at the posterior mode, posterior consistency and the Bernstein–von Mises theorem, Bayesian versus frequentist asymptotics, situations in which the asymptotic theory fails, and the many-normal-means problem with Stein's inadmissibility result, the James–Stein estimator and its empirical Bayes interpretation.
---

Once a model and a prior are fixed, the posterior distribution is determined, but it is rarely of use as a formula alone. We want its mean and quantiles, the posterior of functions of the parameters, predictions, and probabilities of statements such as $\theta>3$. The conjugate models of [3.7.1](/3.7.1)–[3.7.3](/3.7.3) give some of these in closed form; most do not. This chapter develops two complementary tools. The first is simulation: a sample of draws from the posterior answers every such question by averaging (§5.1), and in one or two dimensions draws can be produced from any computable density on a grid (§5.2). The second is asymptotics: with many data the posterior is approximately normal (§5.3), concentrates at the true parameter value (§5.4), and agrees with frequentist large-sample theory, except in a list of situations that recur in practice (§5.5). The chapter closes with the problem of estimating many normal means (§5.6), where the obvious estimator fails in high dimensions and a shrinkage estimator, interpreted as an empirical Bayes rule, leads directly to the hierarchical models of [3.7.6](/3.7.6).

The simulation methods here produce independent draws and need no iteration. Iterative methods, **Markov chain Monte Carlo** and the **Gibbs sampler**, are treated in [3.5.9](/3.5.9) and will be needed for models whose posterior cannot be reduced to one or two dimensions. As before, $\Gamma(\alpha,\beta)$ has shape $\alpha$ and rate $\beta$.

## 5.1. Learning About the Posterior by Simulation

Suppose we can draw $\theta^1,\dots,\theta^S$ independently from $p(\theta\mid y)$. Every posterior summary is then estimated by the corresponding summary of the draws: $\mathbb{E}(\theta\mid y)$ by the average, $\mathbb{P}(\theta\in A\mid y)$ by the proportion of draws in $A$, quantiles and central posterior intervals by empirical quantiles. This is the **Monte Carlo method** ([3.1.12](/3.1.12)) applied to the posterior: by the **law of large numbers** the estimates converge as $S\to\infty$, with Monte Carlo error of order $S^{-1/2}$, so a few thousand draws suffice for most summaries. The real advantage of simulation is that questions which are awkward analytically become trivial.

### 5.1.1. Example: Air Conditioning Failures

**Example 5.1.1 (Air Conditioning Failures)** Proschan (1963) recorded the times between successive failures of the air conditioning system in 13 Boeing 720 aircraft. For the plane numbered 7910 the $n=15$ intervals, in hours, are

$$
74,\ 57,\ 48,\ 29,\ 502,\ 12,\ 70,\ 21,\ 29,\ 386,\ 59,\ 27,\ 153,\ 26,\ 326,
$$
with total $n\bar y=1819$ and mean $\bar y=121.27$. Model them as $y_i\mid\theta\overset{\text{iid}}{\sim}\mathrm{Exp}(\theta)$, where $\theta=1/\mathbb{E}(y\mid\theta)$ is the failure rate (failures per hour). The likelihood is

$$
p(y\mid\theta)=\prod_{i=1}^n\theta\mathrm{e}^{-\theta y_i}=\theta^n\mathrm{e}^{-n\bar y\theta},
$$
and the **maximum likelihood estimator** is $\hat\theta=1/\bar y=0.00825$, about 8 failures per 1000 hours of operation. The gamma family is conjugate ([3.7.2](/3.7.2), §2.1): with $\theta\sim\Gamma(\alpha,\beta)$,

$$
p(\theta\mid y)\propto\theta^n\mathrm{e}^{-n\bar y\theta}\,\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}=\theta^{\alpha+n-1}\mathrm{e}^{-(\beta+n\bar y)\theta},\qquad\theta\mid y\sim\Gamma(\alpha+n,\,\beta+n\bar y).
$$
The update adds the number of intervals to the shape and their total length to the rate. Relative to the flat prior $\Gamma(1,0)$ the prior $\Gamma(\alpha,\beta)$ is therefore worth $\alpha-1$ exponential observations with total $\beta$ hours; relative to the scale-invariant prior $p(\theta)\propto1/\theta$, which is $\Gamma(0,0)$, it is worth $\alpha$ observations.

The other planes supply prior information. The maximum likelihood estimates of $\theta$ for four of them have average about $0.009$ and standard deviation $0.003$. Matching the gamma mean $\alpha/\beta$ and variance $\alpha/\beta^2$ gives $\alpha=(0.009/0.003)^2=9$ and $\beta=0.009/0.003^2=1000$, a prior worth 8 failure intervals totaling $1000$ hours. To see how much the answer depends on this choice, we also use a weaker prior worth half as many intervals in half the time, $\alpha=5$, $\beta=500$:

| prior | prior mean | prior sd | posterior | posterior mean | posterior sd |
|---|---|---|---|---|---|
| strong, $\Gamma(9,1000)$ | 0.0090 | 0.0030 | $\Gamma(24,2819)$ | 0.00851 | 0.00174 |
| weak, $\Gamma(5,500)$ | 0.0100 | 0.0045 | $\Gamma(20,2319)$ | 0.00862 | 0.00193 |

Both posterior means lie between the prior mean and $\hat\theta=0.00825$, close to the latter, and the two analyses agree to within a small fraction of a posterior standard deviation: fifteen observations already outweigh either prior.

![Air conditioning failures of plane 7910. Left and middle: prior, normalized likelihood and posterior of the failure rate under the strong prior Gamma(9, 1000) and the weak prior Gamma(5, 500). Right: 10000 simulated values of the mean time between failures 1/θ under the strong prior, with the exact inverse-gamma density.](./plots/ac_failures.py)

### 5.1.2. Functions of Parameters

**Proposition 5.1.1** If $\theta^1,\dots,\theta^S\overset{\text{iid}}{\sim}p(\theta\mid y)$ and $\lambda=h(\theta)$ for a function $h$, then $\lambda^s=h(\theta^s)$, $s=1,\dots,S$, are independent draws from the posterior $p(\lambda\mid y)$.

**Proof** The $\lambda^s$ are functions of independent random variables, hence independent, and each has the distribution of $h(\theta)$ when $\theta\sim p(\theta\mid y)$, which is by definition $p(\lambda\mid y)$. $\square$

No change-of-variables formula is needed: we simply transform each draw. In particular $\bar\lambda=\frac1S\sum_sh(\theta^s)$ is an unbiased and, by the law of large numbers, consistent estimate of $\mathbb{E}[h(\theta)\mid y]$.

In Example 5.1.1 the quantity of practical interest is the mean time between failures $\lambda=1/\theta=\mathbb{E}(y\mid\theta)$, which for the exponential model is also the standard deviation of the time between failures. Here the exact answer is available: $1/\theta$ has an **inverse-gamma distribution** ([3.7.2](/3.7.2), Definition 2.4.1), and under the strong prior $\lambda\mid y\sim\mathrm{Inv}\text{-}\Gamma(24,2819)$, with mean $2819/23=122.6$ hours, median $119.1$ and $95\%$ central posterior interval $[81.7,183.3]$. Ten thousand gamma draws, inverted, give mean $122.3$ and interval $[81.6,183.6]$, and the proportion of draws with $\lambda>100$ estimates $\mathbb{P}(\lambda>100\mid y)=0.81$. Note that $\mathbb{E}(1/\theta\mid y)=122.6$ differs from $1/\mathbb{E}(\theta\mid y)=117.5$: posterior summaries do not commute with nonlinear functions, and simulation handles this automatically. Simulation also answers questions with no simple closed form, such as the posterior distribution of the probability that the next interval exceeds $200$ hours, $h(\theta)=\mathrm{e}^{-200\theta}$.

### 5.1.3. Sampling from Joint and Marginal Distributions

Multiparameter posteriors are usually known through a factorization, $p(\theta_1,\theta_2\mid y)=p(\theta_2\mid y)\,p(\theta_1\mid\theta_2,y)$, in which both factors are standard distributions although the marginal $p(\theta_1\mid y)$ may not be ([3.7.3](/3.7.3)). Simulation exploits this directly. Write $(X,Y)$ for a generic pair with joint density $p(x,y)=p(x)p(y\mid x)$.

**Proposition 5.1.2** Draw $x_i\sim p(x)$ and then $y_i\sim p(y\mid x_i)$, independently for $i=1,\dots,m$. Then the pairs $(x_i,y_i)$ are independent draws from $p(x,y)$, and $y_1,\dots,y_m$ alone are independent draws from the **marginal distribution** $p(y)=\int p(x,y)\,\mathrm{d}x$.

**Proof** By construction the pair $(x_i,y_i)$ has density $p(x)p(y\mid x)=p(x,y)$. To see this in terms of what the draws are used for, consider the joint **empirical distribution function**

$$
\hat F(x,y)=\frac1m\sum_{i=1}^m\boldsymbol{1}\{x_i\le x\}\boldsymbol{1}\{y_i\le y\}.
$$
Each summand has expectation

$$
\mathbb{E}\big[\boldsymbol{1}\{x_i\le x\}\boldsymbol{1}\{y_i\le y\}\big]=\int_{-\infty}^x\int_{-\infty}^yp(y'\mid x')\,p(x')\,\mathrm{d}y'\,\mathrm{d}x'=\mathbb{P}(X\le x,Y\le y)=F(x,y),
$$
so $\hat F(x,y)$ is an unbiased estimate of the joint distribution function $F(x,y)$, with variance $F(x,y)[1-F(x,y)]/m\to0$, and $\hat F(x,y)\to F(x,y)$ as $m\to\infty$ by the law of large numbers. For the $y_i$ alone take $\hat F(y)=\frac1m\sum_i\boldsymbol{1}\{y_i\le y\}$: each summand has expectation $\mathbb{P}(y_i\le y)=\int p(x)\int_{-\infty}^yp(y'\mid x)\,\mathrm{d}y'\,\mathrm{d}x=F(y)$, the marginal distribution function, and the same argument applies. $\square$

Discarding a component of joint draws is therefore the simulation counterpart of integrating it out. Because the marginal is never computed, this works even when the integral has no closed form.

**Example 5.1.2 (Normal Model with a Conjugate Prior)** For $y_i\mid\mu,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ with the conjugate prior $\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$, $\mu\mid\sigma^2\sim\mathcal{N}(\mu_0,\sigma^2/\kappa_0)$, the joint posterior is of the same form with updated parameters $(\mu_n,\kappa_n,\nu_n,\sigma_n^2)$ ([3.7.3](/3.7.3)):

$$
\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(\nu_n,\sigma_n^2),\qquad\mu\mid\sigma^2,y\sim\mathcal{N}(\mu_n,\sigma^2/\kappa_n).
$$
To simulate, draw $(\sigma^2)^s$ from the **scaled inverse-chi-square distribution** (as $\nu_n\sigma_n^2/Z$ with $Z\sim\chi^2_{\nu_n}$), then $\mu^s$ from $\mathcal{N}(\mu_n,(\sigma^2)^s/\kappa_n)$. The pairs are draws from the joint posterior; the $\mu^s$ alone are draws from the marginal posterior $t_{\nu_n}(\mu_n,\sigma_n^2/\kappa_n)$, obtained without integrating. One more step, $\tilde y^s\sim\mathcal{N}(\mu^s,(\sigma^2)^s)$, gives draws from the **posterior predictive distribution** of a new observation.

## 5.2. Discrete-Grid Sampling

When the prior is not conjugate, the posterior can still be evaluated up to a constant, $q(\theta)=p(\theta)p(y\mid\theta)\propto p(\theta\mid y)$, but it no longer belongs to a family we can sample from. A simple example is the normal model with the semi-conjugate prior in which $\mu$ and $\sigma^2$ are independent a priori,

$$
\mu\sim\mathcal{N}(\mu_0,\tau_0^2),\qquad\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2),
$$
whose joint posterior is not of normal–inverse-chi-square form because the prior variance of $\mu$ no longer scales with $\sigma^2$. In one or two dimensions the simplest general method is to replace the continuous distribution by a discrete one on a grid.

**Algorithm 5.2.1 (Grid Sampling)** To draw $S$ values from a posterior $p(\alpha,\beta\mid y)\propto q(\alpha,\beta)$:

1. After some experimentation (for example around the mode, several approximate posterior standard deviations in each direction), choose a rectangular range that contains almost all the posterior mass.
2. Compute $q$ at the points $(\alpha_i,\beta_k)$ of a grid with spacings $\Delta_\alpha$, $\Delta_\beta$ covering this range.
3. Normalize: $p_{ik}=q(\alpha_i,\beta_k)/\sum_{i',k'}q(\alpha_{i'},\beta_{k'})$, a discrete distribution on the grid.
4. Compute the marginal of $\alpha$ by summing over $\beta$: $p(\alpha_i\mid y)=\sum_kp_{ik}$.
5. For $s=1,\dots,S$:
   1. draw $\alpha^s$ from the discrete distribution $p(\alpha_i\mid y)$, a discrete version of **inverse transform sampling**;
   2. draw $\beta^s$ from the discrete conditional distribution $p(\beta_k\mid\alpha^s,y)=p_{ik}/p(\alpha_i\mid y)$ given the value just drawn;
   3. add to $\alpha^s$ and $\beta^s$ independent uniform jitters on $(-\Delta_\alpha/2,\Delta_\alpha/2)$ and $(-\Delta_\beta/2,\Delta_\beta/2)$, so that the draws have a continuous distribution.

Steps 4 and 5 are Proposition 5.1.2 applied to the discrete approximation. In practice $\log q$ is computed and its maximum subtracted before exponentiating, since $q$ itself may underflow. The grid is best laid out on a scale where the posterior is roughly symmetric and unbounded, such as $\log\sigma$ or $\operatorname{logit}\theta$; then the density on the new scale, including the Jacobian of the transformation, is what must be evaluated ([3.7.6](/3.7.6), §6.5).

**Example 5.2.1** Take a grid with $\alpha\in\{0,0.2,0.4,0.6,0.8,1\}$ and $\beta\in\{0.3,0.6,0.9\}$, and suppose the $18$ unnormalized values $q(\alpha_i,\beta_k)$ sum to $200$, with $q(0.4,0.9)=4$, $q(0.8,0.6)=8$, $q(0.6,0.3)=6$. After normalization $p(0.4,0.9\mid y)=4/200=0.02$, $p(0.8,0.6\mid y)=0.04$ and $p(0.6,0.3\mid y)=0.03$. Suppose that summing each column gives the marginal $p(\alpha\mid y)=(0.1,0.2,0.2,0.1,0.3,0.1)$ for the six values of $\alpha$. A draw then first picks a column with these probabilities; if $\alpha=0.4$ is picked, $\beta=0.9$ is chosen with conditional probability $0.02/0.2=0.1$.

![Grid sampling for the normal model with independent priors μ ~ N(5, 2²) and σ² ~ Inv-χ²(3, 4), and 12 observations simulated from N(10, 2²). Left: contours of the posterior density of (μ, σ) computed on a 201 × 217 grid. Right: 1000 draws obtained by Algorithm 5.2.1.](./plots/grid_sampling.py)

:::

The cost of a grid grows exponentially with the dimension: $K$ points per parameter means $K^d$ evaluations. Grid sampling is therefore useful only after the problem has been reduced to one or two dimensions, which is often possible. If the conditional posterior $p(\theta_1\mid\theta_2,y)$ is a standard distribution, then for any value of $\theta_1$

$$
p(\theta_2\mid y)=\frac{p(\theta_1,\theta_2\mid y)}{p(\theta_1\mid\theta_2,y)},
$$
so the marginal of $\theta_2$ can be evaluated pointwise and only $\theta_2$ needs a grid; $\theta_1$ is then drawn exactly from its conditional distribution. For the semi-conjugate normal model, given $\sigma^2$ the problem is the normal mean with known variance ([3.7.2](/3.7.2), §2.3), so $\mu\mid\sigma^2,y\sim\mathcal{N}(\mu_n,\tau_n^2)$ with

$$
\frac1{\tau_n^2}=\frac1{\tau_0^2}+\frac n{\sigma^2},\qquad\mu_n=\tau_n^2\Big(\frac{\mu_0}{\tau_0^2}+\frac{n\bar y}{\sigma^2}\Big),
$$
both depending on $\sigma^2$. Evaluating the ratio at $\mu=\mu_n$, where the normal density in the denominator equals $(2\pi\tau_n^2)^{-1/2}$, gives the one-dimensional marginal

$$
p(\sigma^2\mid y)\propto p(\sigma^2)\,\tau_n\,(\sigma^2)^{-n/2}\exp\Big(-\frac{(\mu_n-\mu_0)^2}{2\tau_0^2}-\frac{\sum_{i=1}^n(y_i-\mu_n)^2}{2\sigma^2}\Big),
$$
which is sampled on a one-dimensional grid; each draw of $\sigma^2$ is followed by an exact normal draw of $\mu$. The same device, with the hyperparameters in the role of $\sigma^2$, is the basis of the computations for hierarchical models in [3.7.6](/3.7.6).

## 5.3. Normal Approximation to the Posterior

### 5.3.1. The Approximation

If the posterior is unimodal and roughly symmetric, it is natural to approximate it by a normal distribution. Expand $\log p(\theta\mid y)$ in a Taylor series around the posterior mode $\hat\theta$:

$$
\log p(\theta\mid y)=\log p(\hat\theta\mid y)+\Big[\frac{\mathrm{d}}{\mathrm{d}\theta}\log p(\theta\mid y)\Big]^{\mathsf T}_{\theta=\hat\theta}(\theta-\hat\theta)+\frac12(\theta-\hat\theta)^{\mathsf T}\Big[\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(\theta\mid y)\Big]_{\theta=\hat\theta}(\theta-\hat\theta)+\cdots.
$$
At an interior mode the linear term vanishes. The constant term only normalizes, and the quadratic term is the logarithm of a normal kernel.

**Definition 5.3.1 (Normal Approximation)** Let $\hat\theta$ be the posterior mode and

$$
I(\theta)=-\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(\theta\mid y)
$$
the observed information (a matrix when $\theta$ is a vector). The **normal approximation** to the posterior is

$$
p(\theta\mid y)\approx\mathcal{N}\big(\hat\theta,\,[I(\hat\theta)]^{-1}\big).
$$

With a flat prior, $\hat\theta$ is the maximum likelihood estimate and $I(\hat\theta)$ is the **observed information** of the likelihood ([3.5.5](/3.5.5)). In this course $J(\theta)$ denotes the expected **Fisher information** of one observation, as in [3.7.2](/3.7.2), and $I(\theta)$ the observed information of the whole posterior. The mode and $I(\hat\theta)$ can be found by the optimization methods of [3.5.4](/3.5.4)–[3.5.5](/3.5.5); for a one-parameter model they are usually available by hand.

### 5.3.2. Examples

**Example 5.3.1 (Binomial Model)** With $y\mid\theta\sim\mathrm{Bin}(n,\theta)$ and the prior $\mathrm{Beta}(\alpha,\beta)$, the posterior is $\mathrm{Beta}(\alpha+y,\beta+n-y)$ and

$$
\begin{aligned}
\log p(\theta\mid y)&=\text{const}+(\alpha+y-1)\log\theta+(\beta+n-y-1)\log(1-\theta),\\
\frac{\mathrm{d}}{\mathrm{d}\theta}\log p(\theta\mid y)&=\frac{\alpha+y-1}{\theta}-\frac{\beta+n-y-1}{1-\theta},\\
\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(\theta\mid y)&=-\frac{\alpha+y-1}{\theta^2}-\frac{\beta+n-y-1}{(1-\theta)^2}.
\end{aligned}
$$
The mode is $\hat\theta=\frac{\alpha+y-1}{\alpha+\beta+n-2}$. Since $\alpha+y-1=(\alpha+\beta+n-2)\hat\theta$ and $\beta+n-y-1=(\alpha+\beta+n-2)(1-\hat\theta)$, the observed information at the mode is

$$
I(\hat\theta)=\frac{\alpha+\beta+n-2}{\hat\theta}+\frac{\alpha+\beta+n-2}{1-\hat\theta}=\frac{\alpha+\beta+n-2}{\hat\theta(1-\hat\theta)},\qquad p(\theta\mid y)\approx\mathcal{N}\Big(\hat\theta,\frac{\hat\theta(1-\hat\theta)}{\alpha+\beta+n-2}\Big).
$$
With the uniform prior this is $\mathcal{N}\big(\frac yn,\frac{(y/n)(1-y/n)}{n}\big)$, the familiar large-sample distribution of a sample proportion, now read as a statement about $\theta$.

Consider $n=41$ trials with $y=37$ successes.

- *Prior $\mathrm{Beta}(3,3)$.* The posterior is $\mathrm{Beta}(40,7)$, $\hat\theta=39/45=0.8667$, $I(\hat\theta)=45^3/(39\cdot6)=389.42$ and $[I(\hat\theta)]^{-1/2}=0.0507$. The approximate $95\%$ interval $[0.767,0.966]$ is shifted to the right of the exact central interval $[0.737,0.937]$: the exact posterior is skewed to the left, toward the interior, and the normal approximation even puts probability $0.004$ above $\theta=1$.
- *Mixture prior $\frac12\mathrm{Beta}(8,2)+\frac12\mathrm{Beta}(2,8)$.* This bimodal prior expresses the belief that $\theta$ is either large or small. By the update rule for mixtures of conjugate priors ([3.7.1](/3.7.1), Proposition 1.6.1) the posterior is a mixture of $\mathrm{Beta}(45,6)$ and $\mathrm{Beta}(39,12)$ with weights proportional to $\mathrm{B}(45,6)/\mathrm{B}(8,2)$ and $\mathrm{B}(39,12)/\mathrm{B}(2,8)$, which are in the ratio $15279:1$. The data have chosen the first component: the posterior is unimodal and practically $\mathrm{Beta}(45,6)$, with $\hat\theta=44/49=0.8980$, $I(\hat\theta)=534.8$ and $[I(\hat\theta)]^{-1/2}=0.0432$, and the normal approximation is as good as before.
- *The same mixture prior with ambiguous data*, $y=5$ in $n=10$. Now both components keep weight $\frac12$ by symmetry, the posterior is bimodal with modes near $0.34$ and $0.66$, and a normal approximation centered at either mode misses half of the posterior mass.

![Exact posteriors (solid) and normal approximations at the mode (dashed) for binomial data. Left: Beta(3, 3) prior, y = 37, n = 41. Middle: the mixture prior ½Beta(8, 2) + ½Beta(2, 8) with the same data; the posterior is essentially Beta(45, 6). Right: the mixture prior with y = 5, n = 10; the posterior is bimodal and the approximation fails.](./plots/normal_approximation.py)

:::

The requirement "unimodal and roughly symmetric" is therefore essential. It is usually met when the number of observations is large, as the next example shows: with the prior $\mathrm{Beta}(10,10)$ and a fixed observed proportion $y/n=0.1$, the exact and approximate posteriors are visibly different at $n=50$ (posterior standard deviation $0.0487$ exact against $0.0490$ approximate, but with a skewed shape) and practically indistinguishable at $n=400$, where the posterior is $\mathrm{Beta}(50,370)$ with standard deviation $0.0158$.

**Example 5.3.2 (Normal Model, Mean and Variance Unknown)** Let $y_i\mid\mu,\sigma\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ with the non-informative prior that is uniform on $(\mu,\log\sigma)$, equivalent to $p(\mu,\sigma^2)\propto\sigma^{-2}$ ([3.7.3](/3.7.3)). With $s^2=\frac1{n-1}\sum_i(y_i-\bar y)^2$,

$$
\log p(\mu,\log\sigma\mid y)=\text{const}-n\log\sigma-\frac{1}{2\sigma^2}\big[(n-1)s^2+n(\bar y-\mu)^2\big].
$$
The first derivatives are

$$
\frac{\partial}{\partial\mu}\log p=\frac{n(\bar y-\mu)}{\sigma^2},\qquad\frac{\partial}{\partial(\log\sigma)}\log p=-n+\frac{(n-1)s^2+n(\bar y-\mu)^2}{\sigma^2},
$$
so the mode is $(\hat\mu,\log\hat\sigma)=\big(\bar y,\log\big(\sqrt{(n-1)/n}\,s\big)\big)$. The second derivatives are

$$
\frac{\partial^2}{\partial\mu^2}\log p=-\frac n{\sigma^2},\qquad\frac{\partial^2}{\partial\mu\,\partial(\log\sigma)}\log p=-\frac{2n(\bar y-\mu)}{\sigma^2},\qquad\frac{\partial^2}{\partial(\log\sigma)^2}\log p=-\frac{2}{\sigma^2}\big[(n-1)s^2+n(\bar y-\mu)^2\big].
$$
At the mode the mixed derivative vanishes and $(n-1)s^2=n\hat\sigma^2$, so

$$
I(\hat\mu,\log\hat\sigma)=\begin{bmatrix}n/\hat\sigma^2&0\\0&2n\end{bmatrix},\qquad
\begin{bmatrix}\mu\\\log\sigma\end{bmatrix}\Bigm|y\approx\mathcal{N}_2\left(\begin{bmatrix}\bar y\\\log\hat\sigma\end{bmatrix},\begin{bmatrix}\hat\sigma^2/n&0\\0&1/(2n)\end{bmatrix}\right).
$$
The approximation for $\mu$ replaces the exact marginal $t_{n-1}(\bar y,s^2/n)$ by a normal distribution, which is accurate once $n$ is moderately large; the approximation for $\log\sigma$ is much better than a normal approximation for $\sigma$ or $\sigma^2$ would be, because $\log\sigma$ ranges over the whole line and its posterior is nearly symmetric.

### 5.3.3. Uses and Cautions

The normal approximation is useful in several ways.

- It summarizes a posterior by a point estimate and a standard error, the form in which results are usually reported, and it gives a benchmark for interpreting a posterior density relative to its mode: in a contour plot, the contour at height $\mathrm{e}^{-2}$ times the maximum contains about $86\%$ of the mass of a two-dimensional normal distribution.
- It reduces the data to a few summaries: approximately, the posterior depends on the data only through $\hat\theta$ and $I(\hat\theta)$, in the spirit of **sufficient statistics**.
- It is a check for more elaborate computations: a simulation program whose output disagrees grossly with the normal approximation in a large-sample problem probably has a bug. It also provides starting points and proposal distributions for the iterative methods of [3.5.9](/3.5.9).

Two remarks govern its accuracy. First, the approximation is more accurate in lower dimensions: a joint normal distribution has normal marginals, but normal marginals do not imply a normal joint distribution, so a marginal posterior of one parameter is often close to normal when the joint posterior is not. Second, the approximation can be improved dramatically by transforming parameters: positive parameters on the log scale, probabilities on the logit scale. For finite $n$, the closeness of the approximation can differ substantially between parametrizations of the same model (Question 1).

## 5.4. Large-Sample Theory

### 5.4.1. The Setting

Why should a posterior become normal, and normal around what? Consider a sequence of experiments with $y_1,\dots,y_n$ independent draws from a true distribution $f$, analyzed with a model $p(y\mid\theta)$ and a prior $p(\theta)$, and let $n\to\infty$. Two situations must be distinguished: the true distribution belongs to the parametric family, $f=p(\cdot\mid\theta_0)$ for some $\theta_0$, or it does not. In the second case there is no true parameter value, and we need a substitute: the member of the family closest to $f$. Closeness is measured by the Kullback–Leibler information

$$
H(\theta)=\mathbb{E}_f\Big[\log\frac{f(y)}{p(y\mid\theta)}\Big]=\int\log\Big(\frac{f(y)}{p(y\mid\theta)}\Big)f(y)\,\mathrm{d}y,
$$
the **Kullback–Leibler divergence** from $f$ to $p(\cdot\mid\theta)$. It is nonnegative and zero only if the two distributions coincide. We assume that $H$ has a unique minimizer and denote it $\theta_0$. If $f=p(\cdot\mid\theta_0)$, then $H(\theta_0)=0$ and this minimizer is the true value, so the notation covers both situations.

### 5.4.2. Consistency

**Definition 5.4.1 (Posterior Consistency)** The posterior distribution is consistent at $\theta_0$ if for every neighborhood $A$ of $\theta_0$, $\mathbb{P}(\theta\in A\mid y_1,\dots,y_n)\to1$ as $n\to\infty$, with probability one when the $y_i$ are drawn from $f$. This property is called **posterior consistency**.

**Theorem 5.4.1 (Consistency in a Finite Parameter Space)** Let the parameter space $\Theta$ be finite, let $\theta_0$ be the unique minimizer of $H$, and suppose $\mathbb{P}(\theta=\theta_0)>0$ and that the expectations $\mathbb{E}_f\lvert\log p(y\mid\theta)\rvert$ are finite. Then

$$
\mathbb{P}(\theta=\theta_0\mid y_1,\dots,y_n)\to1\qquad(n\to\infty).
$$

**Proof** For $\theta\neq\theta_0$ consider the log posterior odds

$$
\log\frac{p(\theta\mid y)}{p(\theta_0\mid y)}=\log\frac{p(\theta)}{p(\theta_0)}+\sum_{i=1}^n\log\frac{p(y_i\mid\theta)}{p(y_i\mid\theta_0)}.
$$
If $p(\theta)=0$ the odds are $0$ for every $n$. Otherwise the first term is a finite constant, because $p(\theta_0)>0$. With $\theta$ and $\theta_0$ fixed, the sum consists of $n$ independent identically distributed terms with mean

$$
\mathbb{E}_f\Big[\log\frac{p(y_i\mid\theta)}{p(y_i\mid\theta_0)}\Big]=\mathbb{E}_f\Big[\log\frac{f(y_i)}{p(y_i\mid\theta_0)}\Big]-\mathbb{E}_f\Big[\log\frac{f(y_i)}{p(y_i\mid\theta)}\Big]=H(\theta_0)-H(\theta)<0,
$$
strictly negative because $\theta_0$ is the unique minimizer. By the **strong law of large numbers** the sum tends to $-\infty$ with probability one, hence so do the log posterior odds, and $p(\theta\mid y)/p(\theta_0\mid y)\to0$. Since there are finitely many $\theta\ne\theta_0$ and the posterior probabilities add to one,

$$
p(\theta_0\mid y)=\Big(1+\sum_{\theta\ne\theta_0}\frac{p(\theta\mid y)}{p(\theta_0\mid y)}\Big)^{-1}\to1.\qquad\square
$$

The proof shows what drives consistency: each observation contributes on average $H(\theta_0)-H(\theta)<0$ to the log odds against $\theta_0$, a fixed amount, while the prior contributes once. The likelihood eventually dominates any prior that gives $\theta_0$ positive probability. The result extends to a countably infinite parameter space under additional conditions, and to continuous parameters as follows.

**Theorem 5.4.2 (Consistency in a Continuous Parameter Space)** Suppose $\theta$ is defined on a compact set $\Theta$, $\theta_0$ is the unique minimizer of $H$, and $A$ is a neighborhood of $\theta_0$ with prior probability $\mathbb{P}(\theta\in A)>0$. Then, under regularity conditions on the model, $\mathbb{P}(\theta\in A\mid y)\to1$ as $n\to\infty$.

The proof follows the idea of the discrete case: compactness allows $\Theta\setminus A$ to be covered by finitely many small sets, on each of which the posterior odds against $A$ tend to zero. For many models $\Theta$ is not compact (a normal mean ranges over $\mathbb{R}$), but for most problems the compactness assumption can be relaxed.

### 5.4.3. Asymptotic Normality

Consistency says where the posterior concentrates; the normal approximation of §5.3 says what shape it takes. The log posterior is

$$
\log p(\theta\mid y)=\text{const}+\log p(\theta)+\sum_{i=1}^n\log p(y_i\mid\theta).
$$
The prior term stays fixed while the log-likelihood grows linearly in $n$: the likelihood dominates the prior. Consequently the posterior mode $\hat\theta$ converges to $\theta_0$, and the curvature at the mode is

$$
I(\hat\theta)\approx-\sum_{i=1}^n\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(y_i\mid\theta)\Big|_{\theta=\hat\theta}\approx n\cdot\mathbb{E}_f\Big[-\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(y\mid\theta)\Big]_{\theta=\theta_0}=nJ(\theta_0),
$$
by the law of large numbers. When $f=p(\cdot\mid\theta_0)$, $J(\theta_0)$ is the Fisher information of one observation; in general it is defined by this expectation under $f$.

**Theorem 5.4.3 (Bernstein–von Mises Theorem)** Suppose the model is identifiable, $\theta_0$ is an interior point of $\Theta$, the log-likelihood is twice continuously differentiable near $\theta_0$ with $J(\theta_0)$ positive definite, and the prior density is continuous and positive at $\theta_0$. Then as $n\to\infty$ the posterior distribution of $\theta$ approaches normality with mean $\theta_0$ and variance $[nJ(\theta_0)]^{-1}$; more precisely, the posterior distribution of $\sqrt n(\theta-\hat\theta)$, with $\hat\theta$ the posterior mode or the maximum likelihood estimate, converges in total variation to $\mathcal{N}\big(0,J(\theta_0)^{-1}\big)$.

In practice $\theta_0$ and $J(\theta_0)$ are unknown, and one uses the approximation $\mathcal{N}(\hat\theta,[I(\hat\theta)]^{-1})$ of Definition 5.3.1, which is asymptotically equivalent. The theorem also explains why, in large samples, the choice among reasonable priors hardly matters ([3.7.1](/3.7.1), Example 1.6.1): the prior enters only through its value near $\theta_0$, which affects the posterior at order $1/n$.

### 5.4.4. Bayesian and Frequentist Asymptotics

The Bayesian statement and the classical large-sample theory of maximum likelihood look almost identical:

$$
\text{Bayesian: }[I(\hat\theta)]^{1/2}(\theta-\hat\theta)\mid y\;\overset{\cdot}{\sim}\;\mathcal{N}(0,I_d),\qquad
\text{frequentist: }[I(\hat\theta)]^{1/2}(\hat\theta-\theta)\mid\theta\;\overset{\cdot}{\sim}\;\mathcal{N}(0,I_d),
$$
where $I_d$ is the identity matrix. In the Bayesian statement $\theta$ is random and $\hat\theta$, the posterior mode, is fixed given the data (asymptotically it can be replaced by $\theta_0$). In the frequentist statement $\theta$ is fixed at its true value $\theta_0$ and $\hat\theta$, the maximum likelihood estimate, is random over repetitions of the experiment. The two estimates differ by $O(1/n)$, and the approximating distributions coincide.

The practical consequence concerns intervals. The interval $\hat\theta\pm z_{\alpha/2}[I(\hat\theta)]^{-1/2}$ is both an approximate $100(1-\alpha)\%$ **credible interval** and an approximate $100(1-\alpha)\%$ **confidence interval** (the Wald interval). In large samples a Bayesian credible interval therefore has approximately its nominal frequentist coverage, and a confidence interval can be read approximately as a posterior probability statement under a flat prior, although the two interpretations remain different. In small samples, or when the conditions of Theorem 5.4.3 fail, they can differ substantially. If the model is misspecified, the posterior still concentrates at $\theta_0$ with variance $[nJ(\theta_0)]^{-1}$, while the sampling variance of the maximum likelihood estimate is then a different, "sandwich" expression, so credible intervals need not have the nominal coverage.

## 5.5. When the Asymptotic Theory Fails

The theorems of §5.4 rest on assumptions that are easy to violate: the data are informative about every parameter, the number of parameters stays fixed, the posterior is proper, the prior gives positive density near $\theta_0$, $\theta_0$ lies in the interior, and the questions asked concern the center of the distribution. Each failure has a typical example.

### 5.5.1. Underidentified Models and Nonidentified Parameters

**Definition 5.5.1 (Identifiability)** A model is underidentified, given data $y$, if the likelihood $p(y\mid\theta)$ is equal for a range of values of $\theta$. A parameter is **identifiable** if distinct values of it give distinct distributions of the data; a parameter about which the data supply no information at all is called nonidentified.

**Example 5.5.1** Let the pairs $(u,v)$ be bivariate normal,

$$
\begin{bmatrix}u\\v\end{bmatrix}\sim\mathcal{N}_2\left(\begin{bmatrix}0\\0\end{bmatrix},\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}\right),
$$
and suppose that in every pair only one of the two components is observed, $u_1,\dots,u_m$ from some pairs and $v_1,\dots,v_k$ from others. Each observed component is $\mathcal{N}(0,1)$ whatever $\rho$ is, so with $\phi$ the standard normal density

$$
p(\rho\mid y)\propto p(\rho)\prod_{i=1}^m\phi(u_i)\prod_{j=1}^k\phi(v_j)\propto p(\rho).
$$
The posterior equals the prior however many observations are made: $\rho$ is nonidentified. In such problems no amount of data of the same kind helps; better data collection (here, pairs with both components observed) or genuine prior information about the parameter is needed.

### 5.5.2. Label Switching

A special case of underidentification occurs when different parameter values give the same likelihood for every data set. It is typical of mixture models. For the two-component normal **mixture model**

$$
p(y_i\mid\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\lambda)=\lambda\frac{1}{\sigma_1\sqrt{2\pi}}\exp\Big(-\frac{(y_i-\mu_1)^2}{2\sigma_1^2}\Big)+(1-\lambda)\frac{1}{\sigma_2\sqrt{2\pi}}\exp\Big(-\frac{(y_i-\mu_2)^2}{2\sigma_2^2}\Big),
$$
exchanging $(\mu_1,\sigma_1^2)$ with $(\mu_2,\sigma_2^2)$ and replacing $\lambda$ by $1-\lambda$ gives the same likelihood for any data. With a prior that is symmetric in the two components, the posterior is a $50\%$–$50\%$ mixture of two mirror images. It cannot be normal (it is bimodal) and cannot converge to a single point. This phenomenon, in which the labels of the components are not determined by the data, is called *label switching* (also aliasing). The usual remedy is to reparametrize so that the duplication disappears, for instance by restricting $\mu_1\le\mu_2$. In multidimensional problems this can be difficult, since vectors have no natural order: one may order the components by one coordinate, which may or may not separate them.

### 5.5.3. Number of Parameters Increasing with the Sample Size

The theorems assume that the information about each parameter grows with $n$. In the model

$$
y_i\mid\pi_i\sim\mathrm{Bin}(n_i,\pi_i),\qquad\pi_i\sim p(\pi_i),\qquad i=1,2,\dots,
$$
with independent priors, each new group brings a new parameter, and

$$
p(\pi_i\mid y)\propto p(\pi_i)\,\pi_i^{y_i}(1-\pi_i)^{n_i-y_i}
$$
regardless of how many groups are observed. Additional groups give information only about their own $\pi_j$, and the posterior of $\pi_i$ does not converge to a point; for that, more Bernoulli trials under the same $\pi_i$ would be needed. Hierarchical models ([3.7.6](/3.7.6)) change this picture by tying the $\pi_i$ together through a common distribution, whose parameters are then estimated with increasing precision as groups accumulate.

### 5.5.4. Improper Posterior Distributions

The asymptotic results presuppose a proper posterior; the proof of Theorem 5.4.1 used $\sum_kp(\theta_k\mid y)=1$. An **improper prior** can produce an improper posterior ([3.7.2](/3.7.2), §2.6), and then the theory does not apply at all. The remedy is easy: a proper prior always gives a proper posterior. An improper posterior is usually a symptom of a badly behaved likelihood, which flattens out in some direction, and a likelihood analysis will break down too ([3.7.6](/3.7.6), §6.5, gives an example).

### 5.5.5. A Prior That Excludes the Point of Convergence

If $p(\theta)=0$ then $p(\theta\mid y)=0$. If the prior excludes $\theta_0$, the posterior cannot converge to it and, if it converges at all, converges to the nearest point where the prior is positive. The remedy is the principle of [3.7.1](/3.7.1) §1.6.1: the prior must be positive at every remotely plausible value.

### 5.5.6. Tails and Boundaries

Asymptotic normality is a statement about the center of the posterior, derived from a Taylor expansion at the mode (which is close to the posterior mean and median), not about its tails. A normal density decays like $\mathrm{e}^{-c\theta^2}$, while posteriors can have much heavier tails, like a **Cauchy distribution** ($p(\theta)\propto\theta^{-2}$ for large $\lvert\theta\rvert$) or a **Laplace distribution** ($p(\theta)\propto\mathrm{e}^{-c\lvert\theta\rvert}$). Tail probabilities and extreme quantiles computed from a normal approximation can be badly wrong even when the center is well approximated.

A related problem appears for finite samples. The normal distribution takes values on the whole line, while many parameters, such as binomial probabilities, have a bounded range. Near the boundary the posterior is skewed and the approximation puts mass outside the parameter space (Example 5.3.1). As $n$ increases the posterior concentrates and the boundary usually ceases to matter, since $\theta_0$ is then many posterior standard deviations away from it. The exception is $\theta_0$ on the boundary itself, such as a variance component equal to $0$ ([3.7.6](/3.7.6), §6.6), where asymptotic normality fails for every $n$.

## 5.6. The Many-Normal-Means Problem and Empirical Bayes

Asymptotic arguments let $n$ grow with the number of parameters fixed. Many modern problems have the opposite structure: many parameters, few observations for each. The simplest such problem shows that the usual estimator can be poor, and how pooling information across parameters repairs it.

Let $x_1,\dots,x_p$ be independent with $x_j\sim\mathcal{N}(\theta_j,\sigma^2)$, $\sigma^2$ known, that is $\boldsymbol{x}\sim\mathcal{N}_p(\boldsymbol{\theta},\sigma^2I_p)$, and suppose the goal is to estimate $\boldsymbol{\theta}=(\theta_1,\dots,\theta_p)^{\mathsf T}$. From the frequentist point of view $\boldsymbol{x}$ is the maximum likelihood estimate and an **unbiased estimator** of $\boldsymbol{\theta}$. When $p$ is large this apparently obvious solution becomes problematic in two ways.

### 5.6.1. The Length of the Estimate

From the frequentist view, $\boldsymbol{x}\mid\boldsymbol{\theta}\sim\mathcal{N}_p(\boldsymbol{\theta},\sigma^2I_p)$ and

$$
\mathbb{E}\big(\|\boldsymbol{x}\|^2\mid\boldsymbol{\theta}\big)=\|\boldsymbol{\theta}\|^2+p\sigma^2.
$$
Geometrically, the noise vector $\boldsymbol{x}-\boldsymbol{\theta}$ has squared length about $p\sigma^2$ and is nearly orthogonal to $\boldsymbol{\theta}$ in high dimensions, so $\boldsymbol{x}$ is longer than $\boldsymbol{\theta}$. The probability $\mathbb{P}(\|\boldsymbol{x}\|>\|\boldsymbol{\theta}\|\mid\boldsymbol{\theta})$ is high and tends to $1$ as $p$ increases with $\|\boldsymbol{\theta}\|^2/p$ bounded (Question 6).

From the Bayesian view with independent priors $\theta_j\sim\mathcal{N}(\mu_{0j},\tau_{0j}^2)$, the normal-mean result of [3.7.2](/3.7.2) gives

$$
\theta_j\mid\boldsymbol{x}\sim\mathcal{N}\Big(\frac{\tau_{0j}^2x_j+\sigma^2\mu_{0j}}{\tau_{0j}^2+\sigma^2},\;\frac{\sigma^2\tau_{0j}^2}{\tau_{0j}^2+\sigma^2}\Big).
$$
Letting $\tau_{0j}^2\to\infty$, the flat-prior limit, gives $\boldsymbol{\theta}\mid\boldsymbol{x}\sim\mathcal{N}_p(\boldsymbol{x},\sigma^2I_p)$, and now

$$
\mathbb{E}\big(\|\boldsymbol{\theta}\|^2\mid\boldsymbol{x}\big)=\|\boldsymbol{x}\|^2+p\sigma^2,
$$
so the posterior asserts that $\|\boldsymbol{\theta}\|>\|\boldsymbol{x}\|$ with high probability. The two views contradict each other: having observed $\boldsymbol{x}$, the sampling argument says the truth is probably shorter than $\boldsymbol{x}$, the flat-prior posterior says it is probably longer. The culprit is the flat prior. Independent flat priors on many parameters are not non-informative about every function of them: they make large values of $\|\boldsymbol{\theta}\|$ overwhelmingly probable. In high dimensions a prior that is harmless coordinate by coordinate can be strongly informative jointly.

### 5.6.2. Inadmissibility and the James–Stein Estimator

To compare estimators $\tilde{\boldsymbol{\theta}}=\tilde{\boldsymbol{\theta}}(\boldsymbol{x})$ we need a criterion.

**Definition 5.6.1 (Risk Function and Admissibility)** Under squared-error loss, the **risk function** of an estimator $\tilde{\boldsymbol{\theta}}$ is

$$
R(\tilde{\boldsymbol{\theta}},\boldsymbol{\theta})=\mathbb{E}_{\boldsymbol{\theta}}\|\tilde{\boldsymbol{\theta}}-\boldsymbol{\theta}\|^2=\mathbb{E}_{\boldsymbol{\theta}}\sum_{j=1}^p(\tilde\theta_j-\theta_j)^2,
$$
the total mean squared error as a function of the true $\boldsymbol{\theta}$. An estimator $\tilde{\boldsymbol{\theta}}_1$ dominates $\tilde{\boldsymbol{\theta}}_2$ if $R(\tilde{\boldsymbol{\theta}}_1,\boldsymbol{\theta})\le R(\tilde{\boldsymbol{\theta}}_2,\boldsymbol{\theta})$ for all $\boldsymbol{\theta}$, with strict inequality for some $\boldsymbol{\theta}$. An estimator that is dominated by no other estimator is an **admissible estimator**; a dominated one is inadmissible.

An inadmissible estimator should not be used, since another estimator is at least as good whatever the truth. The risk of $\hat{\boldsymbol{\theta}}_{\mathrm{MLE}}=\boldsymbol{x}$ is constant, $R(\boldsymbol{x},\boldsymbol{\theta})=\mathbb{E}_{\boldsymbol{\theta}}\|\boldsymbol{x}-\boldsymbol{\theta}\|^2=p\sigma^2$, and it seemed self-evident that nothing could beat it uniformly. Stein (1956) showed that for $p\ge3$ it is inadmissible, and James and Stein (1961) gave an explicit dominating estimator. Without loss of generality let $\sigma^2=1$ (otherwise divide by $\sigma$); then $R(\boldsymbol{x},\boldsymbol{\theta})=p$.

**Definition 5.6.2 (James–Stein Estimator)** Let $p\ge3$ and let $\boldsymbol{\mu}\in\mathbb{R}^p$ be an arbitrary fixed vector. The **James–Stein estimator** is

$$
\tilde{\boldsymbol{\theta}}_{\mathrm{JS}}=\boldsymbol{\mu}+\Big(1-\frac{p-2}{\|\boldsymbol{x}-\boldsymbol{\mu}\|^2}\Big)(\boldsymbol{x}-\boldsymbol{\mu})=\boldsymbol{x}-\frac{p-2}{\|\boldsymbol{x}-\boldsymbol{\mu}\|^2}(\boldsymbol{x}-\boldsymbol{\mu}).
$$

For $\boldsymbol{\mu}=\boldsymbol{0}$ it is $\big(1-\frac{p-2}{\|\boldsymbol{x}\|^2}\big)\boldsymbol{x}$, which shrinks every coordinate toward $0$ by the same data-dependent fraction. An estimator of this kind, which pulls the individual estimates toward a common point, is a *shrinkage estimator*.

**Theorem 5.6.1 (Stein)** For $p\ge3$ and every $\boldsymbol{\theta}$,

$$
R(\tilde{\boldsymbol{\theta}}_{\mathrm{JS}},\boldsymbol{\theta})=p-(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac{1}{\|\boldsymbol{x}-\boldsymbol{\mu}\|^2}<p=R(\boldsymbol{x},\boldsymbol{\theta}).
$$
Hence $\boldsymbol{x}$ is inadmissible under squared-error loss.

**Proof** We use Stein's identity: if $z\sim\mathcal{N}(\theta,1)$ and $g$ is absolutely continuous with $\mathbb{E}\lvert g'(z)\rvert<\infty$, then $\mathbb{E}[(z-\theta)g(z)]=\mathbb{E}[g'(z)]$. It follows by integrating by parts, since $(z-\theta)\phi(z-\theta)=-\frac{\mathrm{d}}{\mathrm{d}z}\phi(z-\theta)$. Write $S=\|\boldsymbol{x}-\boldsymbol{\mu}\|^2$. Expanding the square,

$$
R(\tilde{\boldsymbol{\theta}}_{\mathrm{JS}},\boldsymbol{\theta})=\mathbb{E}_{\boldsymbol{\theta}}\Big\|\boldsymbol{x}-\boldsymbol{\theta}-\frac{p-2}{S}(\boldsymbol{x}-\boldsymbol{\mu})\Big\|^2
=\mathbb{E}_{\boldsymbol{\theta}}\|\boldsymbol{x}-\boldsymbol{\theta}\|^2+(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac{1}{S}-2(p-2)\sum_{i=1}^p\mathbb{E}_{\boldsymbol{\theta}}\frac{(x_i-\mu_i)(x_i-\theta_i)}{S}.
$$
The first term is $p$. For the last, apply Stein's identity to $x_i$ with the other coordinates held fixed and $g_i(\boldsymbol{x})=(x_i-\mu_i)/S$:

$$
\frac{\partial g_i}{\partial x_i}=\frac{1}{S}-\frac{2(x_i-\mu_i)^2}{S^2},\qquad\sum_{i=1}^p\frac{\partial g_i}{\partial x_i}=\frac pS-\frac2S=\frac{p-2}{S},
$$
so the sum equals $(p-2)\,\mathbb{E}_{\boldsymbol{\theta}}(1/S)$. For $p\ge3$, $S$ is a noncentral chi-square variable with $p$ degrees of freedom, $\mathbb{E}_{\boldsymbol{\theta}}(1/S)$ is finite and positive, and the integrability conditions hold. Altogether

$$
R(\tilde{\boldsymbol{\theta}}_{\mathrm{JS}},\boldsymbol{\theta})=p+(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac1S-2(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac1S=p-(p-2)^2\,\mathbb{E}_{\boldsymbol{\theta}}\frac1S<p.\qquad\square
$$

The gain is largest when $\boldsymbol{\theta}$ is near $\boldsymbol{\mu}$. At $\boldsymbol{\theta}=\boldsymbol{\mu}$, $S\sim\chi^2_p$ and $\mathbb{E}(1/S)=1/(p-2)$, so the risk is $2$ instead of $p$; as $\|\boldsymbol{\theta}-\boldsymbol{\mu}\|\to\infty$ the risk increases to $p$ but never reaches it. The choice of $\boldsymbol{\mu}$ is arbitrary: shrinking toward any fixed point helps, although the help is negligible far from it. The result is surprising because the coordinates are independent and may concern unrelated quantities, yet combining them in one estimate reduces the total risk; it does not claim that each coordinate is better estimated. The James–Stein estimator is itself inadmissible: when $S<p-2$ its shrinkage factor is negative and it overshoots $\boldsymbol{\mu}$, and the positive-part estimator, which replaces the factor by $\max\big(0,1-\frac{p-2}{S}\big)$, dominates it. Shrinkage toward zero is also the idea of **ridge regression** ([3.3.12](/3.3.12)).

![Risk of three estimators of p = 10 normal means with unit variance, as a function of the distance of θ from the shrinkage point 0: the maximum likelihood estimate x (constant risk 10), the James–Stein estimator (exact formula of Theorem 5.6.1) and its positive-part version (20000 simulations per point).](./plots/james_stein_risk.py)

### 5.6.3. An Empirical Bayes Interpretation

The James–Stein estimator looks like a trick; a Bayesian argument explains where it comes from. Keep $\sigma^2=1$ and assume the prior

$$
\theta_j\overset{\text{iid}}{\sim}\mathcal{N}(\mu_j,\tau_0^2),\qquad j=1,\dots,p,
$$
with $\boldsymbol{\mu}$ known and a common variance $\tau_0^2$. Then

$$
\theta_j\mid\boldsymbol{x}\sim\mathcal{N}\Big(\frac{\tau_0^2x_j+\mu_j}{\tau_0^2+1},\frac{\tau_0^2}{\tau_0^2+1}\Big),\qquad
\mathbb{E}(\theta_j\mid\boldsymbol{x})=\frac{\mu_j/\tau_0^2+x_j}{1/\tau_0^2+1}=\mu_j+\frac{\tau_0^2}{1+\tau_0^2}(x_j-\mu_j),
$$
and the posterior mean, the Bayes estimator under squared-error loss, is

$$
\hat{\boldsymbol{\theta}}_{\mathrm{Bayes}}=\boldsymbol{\mu}+\Big(1-\frac{1}{1+\tau_0^2}\Big)(\boldsymbol{x}-\boldsymbol{\mu}).
$$
This has exactly the form of $\tilde{\boldsymbol{\theta}}_{\mathrm{JS}}$, with the shrinkage fraction $\frac{1}{1+\tau_0^2}$ in place of $\frac{p-2}{\|\boldsymbol{x}-\boldsymbol{\mu}\|^2}$. If $\tau_0^2$ is unknown, the data can estimate it. Integrating out $\theta_j$, the $x_j$ are marginally independent with $x_j\sim\mathcal{N}(\mu_j,\tau_0^2+1)$, so $S=\|\boldsymbol{x}-\boldsymbol{\mu}\|^2\sim(1+\tau_0^2)\chi^2_p$ and

$$
\mathbb{E}\Big[\sum_{j=1}^p(x_j-\mu_j)^2\Big]=p(1+\tau_0^2),\qquad\mathbb{E}\frac{p-2}{S}=\frac{p-2}{1+\tau_0^2}\,\mathbb{E}\frac{1}{\chi^2_p}=\frac{1}{1+\tau_0^2}.
$$
Thus $\hat\tau_0^2=S/p-1$ is an unbiased estimate of $\tau_0^2$, and $(p-2)/S$ is an unbiased (and, as $p\to\infty$, consistent) estimate of the shrinkage fraction $1/(1+\tau_0^2)$. Substituting it into the Bayes estimator gives the James–Stein estimator. The James–Stein estimator is therefore an "empirical" version of a Bayes rule, which is where the name of the following method comes from.

**Definition 5.6.3 (Empirical Bayes)** Consider a model in which parameters $\theta_1,\dots,\theta_p$ are drawn independently from a prior $p(\theta\mid\phi)$ with an unknown hyperparameter $\phi$, and data $x_j\mid\theta_j\sim p(x_j\mid\theta_j)$. The **empirical Bayes** method estimates $\phi$ from the marginal distribution of all the data, $p(\boldsymbol{x}\mid\phi)=\prod_j\int p(x_j\mid\theta_j)p(\theta_j\mid\phi)\,\mathrm{d}\theta_j$, for instance by the method of moments or by maximizing it, and then bases inference about each $\theta_j$ on the posterior $p(\theta_j\mid\hat\phi,x_j)$, treating $\hat\phi$ as known.

Empirical Bayes borrows strength: the estimate of each $\theta_j$ uses all the data through $\hat\phi$, and the James–Stein theorem shows that this pays off in frequentist risk. Its weakness is that it treats the estimated hyperparameter as if it were known, ignoring the uncertainty in $\hat\phi$, and it uses the data both to choose the prior and to update it. The fully Bayesian alternative gives $\phi$ its own prior and integrates over it; this is the **hierarchical model** of [3.7.6](/3.7.6), where the same normal problem returns as the eight schools example. Large-scale applications of empirical Bayes, such as estimating thousands of effects in genomics, are discussed in [7.7.20](/7.7.20).

## Summary

| Topic | Key facts |
|---|---|
| posterior simulation | draws $\theta^s\sim p(\theta\mid y)$ estimate any summary; $h(\theta^s)\sim p(h(\theta)\mid y)$ (Proposition 5.1.1); $\mathbb{E}(1/\theta\mid y)\ne1/\mathbb{E}(\theta\mid y)$ |
| joint and marginal | $x_i\sim p(x)$, $y_i\sim p(y\mid x_i)$ gives joint draws, and the $y_i$ alone marginal draws; justified by the unbiased and consistent ECDF (Proposition 5.1.2) |
| exponential–gamma | $\Gamma(\alpha,\beta)\to\Gamma(\alpha+n,\beta+n\bar y)$; $1/\theta\mid y\sim\mathrm{Inv}\text{-}\Gamma(\alpha+n,\beta+n\bar y)$ (Example 5.1.1) |
| grid sampling | range, unnormalized density on a grid, normalize, marginal, discrete inverse CDF, conditional, jitter (Algorithm 5.2.1); reduce to one dimension with $p(\theta_2\mid y)=p(\theta_1,\theta_2\mid y)/p(\theta_1\mid\theta_2,y)$ |
| normal approximation | $p(\theta\mid y)\approx\mathcal{N}(\hat\theta,[I(\hat\theta)]^{-1})$, $I=-\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(\theta\mid y)$ at the mode (Definition 5.3.1); binomial: $\mathcal{N}\big(\hat\theta,\frac{\hat\theta(1-\hat\theta)}{\alpha+\beta+n-2}\big)$; normal: $(\mu,\log\sigma)\approx\mathcal{N}_2\big((\bar y,\log\hat\sigma),\operatorname{diag}(\hat\sigma^2/n,1/(2n))\big)$ |
| when it works | unimodal, roughly symmetric, low dimension, suitable parametrization (log, logit) |
| consistency | $\theta_0$ minimizes the Kullback–Leibler information $H(\theta)$; $\mathbb{P}(\theta=\theta_0\mid y)\to1$ for finite $\Theta$ (Theorem 5.4.1), neighborhoods for compact $\Theta$ (Theorem 5.4.2) |
| asymptotic normality | likelihood dominates prior; $\theta\mid y\approx\mathcal{N}(\theta_0,[nJ(\theta_0)]^{-1})$ (Theorem 5.4.3) |
| Bayes vs frequentist | same normal form, $\theta$ random vs $\hat\theta$ random; credible and confidence intervals agree asymptotically |
| failures | nonidentified parameters, label switching, parameters growing with $n$, improper posterior, prior excluding $\theta_0$, heavy tails, boundary (§5.5) |
| many normal means | $\mathbb{E}\|\boldsymbol{x}\|^2=\|\boldsymbol{\theta}\|^2+p\sigma^2$; $\boldsymbol{x}$ inadmissible for $p\ge3$; $R(\tilde{\boldsymbol{\theta}}_{\mathrm{JS}},\boldsymbol{\theta})=p-(p-2)^2\mathbb{E}(1/S)$ (Theorem 5.6.1) |
| empirical Bayes | Bayes rule $\boldsymbol{\mu}+\big(1-\frac1{1+\tau_0^2}\big)(\boldsymbol{x}-\boldsymbol{\mu})$ with $\frac{p-2}{S}$ unbiased for $\frac1{1+\tau_0^2}$ gives James–Stein (Definition 5.6.3) |

## Questions

1. In Example 5.1.1 with the strong prior, the posterior is $\Gamma(24,2819)$. Find the normal approximation for $\theta$ and for $\phi=\log\theta$, and compare the resulting $95\%$ intervals for $\theta$ with the exact central interval $[0.00545,0.01224]$.

   **Answer** For $\theta$: $\log p=23\log\theta-2819\theta$, so $\hat\theta=23/2819=0.008159$ and $I(\hat\theta)=23/\hat\theta^2$, giving $\mathcal{N}(0.008159,\,0.001701^2)$ and the interval $[0.00482,0.01149]$, too far to the left at both ends. For $\phi=\log\theta$ the density includes the Jacobian $\theta$: $\log p(\phi\mid y)=24\phi-2819\mathrm{e}^\phi$, with mode $\mathrm{e}^{\hat\phi}=24/2819$ and $I(\hat\phi)=2819\mathrm{e}^{\hat\phi}=24$. The approximation $\phi\mid y\approx\mathcal{N}(\log0.008514,1/24)$ gives, after exponentiating, $[0.00571,0.01270]$, whose endpoints are about half as far from the exact ones. The log scale removes most of the skewness of the gamma posterior.
2. For $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathrm{Poi}(\theta)$ and the prior $\Gamma(\alpha,\beta)$, derive the normal approximation to the posterior and show that it agrees asymptotically with Theorem 5.4.3.

   **Answer** The posterior is $\Gamma(\alpha+n\bar y,\beta+n)$ with $\log p=(\alpha+n\bar y-1)\log\theta-(\beta+n)\theta+\text{const}$. The mode is $\hat\theta=\frac{\alpha+n\bar y-1}{\beta+n}$ and $I(\hat\theta)=\frac{\alpha+n\bar y-1}{\hat\theta^2}=\frac{(\beta+n)^2}{\alpha+n\bar y-1}$, so $\theta\mid y\approx\mathcal{N}\big(\hat\theta,\frac{\alpha+n\bar y-1}{(\beta+n)^2}\big)$. As $n\to\infty$, $\hat\theta\to\theta_0$ and the variance is $\approx\bar y/n\approx\theta_0/n$. The Fisher information of one Poisson observation is $J(\theta)=1/\theta$, so $[nJ(\theta_0)]^{-1}=\theta_0/n$, as the theorem states; the prior parameters $\alpha,\beta$ affect only terms of relative order $1/n$.
3. The parameter space is $\Theta=\{0.3,0.6\}$ for Bernoulli trials with success probability $\theta$, the prior gives each value probability $\frac12$, and the data actually come from $\mathrm{Ber}(0.5)$. To which value does the posterior converge? About how many trials make the posterior odds of the other value roughly $1:100$?

   **Answer** $H(\theta)=\mathbb{E}_f\log f(y)-[0.5\log\theta+0.5\log(1-\theta)]$. The bracket is $-0.7803$ for $\theta=0.3$ and $-0.7136$ for $\theta=0.6$, so $H$ is smaller at $0.6$ and $\theta_0=0.6$, the model value closest to the truth in Kullback–Leibler divergence (although $0.5$ is about equally far from both in absolute distance). By Theorem 5.4.1 the posterior concentrates on $0.6$. Each trial changes the log odds of $0.3$ against $0.6$ by $H(0.6)-H(0.3)=-0.0668$ on average, so the expected log odds reach $\log0.01=-4.61$ after about $4.61/0.0668\approx69$ trials. The per-trial standard deviation of the increment is $0.63$, so for a particular sequence the actual number varies considerably.
4. Show that if $S\sim c\,\chi^2_p$ with $p\ge3$ then $\mathbb{E}(1/S)=\frac{1}{c(p-2)}$, and deduce that the risk of the James–Stein estimator at $\boldsymbol{\theta}=\boldsymbol{\mu}$ is $2$. Why must $p\ge3$?

   **Answer** With the $\chi^2_p$ density, $\mathbb{E}(1/Z)=\int_0^\infty\frac{z^{p/2-2}\mathrm{e}^{-z/2}}{2^{p/2}\Gamma(p/2)}\,\mathrm{d}z=\frac{2^{p/2-1}\Gamma(p/2-1)}{2^{p/2}\Gamma(p/2)}=\frac{1}{2(p/2-1)}=\frac1{p-2}$, and $\mathbb{E}(1/S)=\mathbb{E}(1/Z)/c$. At $\boldsymbol{\theta}=\boldsymbol{\mu}$ (with $\sigma^2=1$), $S\sim\chi^2_p$, so $R=p-(p-2)^2/(p-2)=2$. For $p\le2$ the integral $\int_0z^{p/2-2}\,\mathrm{d}z$ diverges, $\mathbb{E}(1/S)=\infty$, and the risk formula breaks down; indeed $\boldsymbol{x}$ is admissible for $p=1,2$.
5. For each model, say which assumption of the asymptotic theory fails and what happens to the posterior as more data of the same kind arrive. (a) $y_i\mid\theta_1,\theta_2\sim\mathcal{N}(\theta_1+\theta_2,1)$ with independent proper priors. (b) A two-component Poisson mixture with a symmetric prior. (c) Binomial data with the prior $\theta\sim\mathrm{U}(0,0.5)$ when the true value is $0.6$. (d) The success rate of each of many surgeons, each observed in one operation.

   **Answer** (a) Only $\theta_1+\theta_2$ is identified: its posterior concentrates at the true sum, while the posterior of $\theta_1-\theta_2$ given the sum stays equal to what the prior implies (nonidentified parameter, §5.5.1). (b) Label switching: the posterior stays bimodal with two mirror-image modes; an order constraint on the two means restores a unimodal posterior (§5.5.2). (c) The prior excludes the point of convergence: the posterior piles up at the boundary $0.5$ (§5.5.5), and the normal approximation fails there (§5.5.6). (d) The number of parameters grows with the sample size: each surgeon's posterior is based on one operation and never concentrates; a hierarchical model sharing information among surgeons is needed (§5.5.3).
6. Let $\boldsymbol{x}\sim\mathcal{N}_p(\boldsymbol{\theta},I_p)$. Show that $\mathbb{P}(\|\boldsymbol{x}\|>\|\boldsymbol{\theta}\|\mid\boldsymbol{\theta})\to1$ as $p\to\infty$ if $\|\boldsymbol{\theta}\|^2\le cp$ for a constant $c$, and evaluate it for $p=10$, $\|\boldsymbol{\theta}\|^2=10$.

   **Answer** Write $\boldsymbol{x}=\boldsymbol{\theta}+\boldsymbol{z}$. Then $D=\|\boldsymbol{x}\|^2-\|\boldsymbol{\theta}\|^2=2\boldsymbol{\theta}^{\mathsf T}\boldsymbol{z}+\|\boldsymbol{z}\|^2$ has mean $p$ and variance $4\|\boldsymbol{\theta}\|^2+2p\le(4c+2)p$ (the two terms are uncorrelated because odd moments of $\boldsymbol{z}$ vanish). By Chebyshev's inequality $\mathbb{P}(D\le0)\le\mathbb{P}(\lvert D-p\rvert\ge p)\le(4c+2)/p\to0$. For $p=10$, $\|\boldsymbol{x}\|^2$ is noncentral $\chi^2_{10}$ with noncentrality $10$, and $\mathbb{P}(\|\boldsymbol{x}\|^2>10)=0.92$: even in ten dimensions the observed vector is longer than the truth in more than nine cases out of ten.
7. In grid sampling (Algorithm 5.2.1), why is the jitter added, and how should the grid spacing and range be checked? What limits the method?

   **Answer** Without jitter every draw lies exactly on a grid point, so the draws have a discrete distribution with ties; uniform jitter within one grid cell spreads each draw over the cell and yields a continuous distribution that approximates the posterior to within the grid resolution. The range is adequate if the normalized density is negligible along the boundary of the grid (otherwise mass is cut off, as in [3.7.6](/3.7.6) §6.5 with a truncated prior), and the spacing is adequate if refining the grid does not change the summaries of interest. The method is limited by dimension: $K$ points per coordinate need $K^d$ evaluations, so it is practical for $d\le2$ or $3$, unless the problem can be reduced to fewer dimensions by drawing some parameters exactly from conditional distributions.
8. In the empirical Bayes setting of §5.6.3, the plug-in estimate $\hat\tau_0^2=S/p-1$ can be negative. Show that replacing $1/(1+\tau_0^2)$ by $\min\{1,p/S\}$ in the Bayes rule gives an estimator close to the positive-part James–Stein estimator, and explain why truncation is sensible.

   **Answer** With $\hat\tau_0^2=\max(0,S/p-1)$, the shrinkage fraction is $\frac{1}{1+\hat\tau_0^2}=\min\{1,p/S\}$, and the estimator is $\boldsymbol{\mu}+\big(1-\min\{1,p/S\}\big)(\boldsymbol{x}-\boldsymbol{\mu})=\boldsymbol{\mu}+\max\big(0,1-\frac pS\big)(\boldsymbol{x}-\boldsymbol{\mu})$. This is the positive-part James–Stein estimator with $p$ in place of $p-2$, a difference that matters only when $p$ is small. Truncation is sensible because a variance cannot be negative: when $S<p$ the data are consistent with $\tau_0^2=0$, all $\theta_j$ equal to $\mu_j$, and the best estimate is complete shrinkage, never shrinkage past $\boldsymbol{\mu}$.
