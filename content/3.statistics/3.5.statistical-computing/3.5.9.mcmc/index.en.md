---
title: Markov Chain Monte Carlo
description: Monte Carlo integration (hit-or-miss and mean-value methods), importance sampling and its variance, rare events and self-normalized weights; Markov chains, stationary distributions, detailed balance and the basic limit theorem; the Metropolis–Hastings algorithm, the Gibbs sampler and convergence diagnostics.
---

*Markov chain Monte Carlo* (MCMC) estimates by simulation the expectation of a statistic in a complex model. Successive random draws form a Markov chain whose stationary distribution is the target distribution. It is particularly useful for evaluating posterior distributions in complex Bayesian models. In the Metropolis–Hastings algorithm, candidates are drawn from an arbitrary proposal distribution and kept or not according to an acceptance rule; the Gibbs sampler is the special case in which the proposals are the conditional distributions of single components of a vector. This chapter, the last of the course, joins two lines. The first part continues the **Monte Carlo method** of [3.1.12](/3.1.12) and the samplers of [3.5.8](/3.5.8): two ways of Monte Carlo integration and importance sampling, a mirror image of rejection sampling that fails in high dimensions in a different way. The second part introduces Markov chains, their stationary distributions and the basic limit theorem, and combines both into MCMC. The Bayesian background (**prior distribution**, **posterior distribution**, **credible intervals**) is in [3.2.7](/3.2.7); Bayesian statistics ([3.7](/3.7)) relies on these samplers throughout.

MCMC is applied to integration and optimization problems in high-dimensional spaces, in three classes of problems: integration, generating samples from a probability distribution, and optimization. Typical examples:

- Bayesian inference and learning: the normalization $p(x\mid y)=\dfrac{p(y\mid x)p(x)}{\int_{\mathcal{X}}p(y\mid t)p(t)\,\mathrm{d}t}$, the marginalization $p(x\mid y)=\int_{\mathcal{Z}}p(x,z\mid y)\,\mathrm{d}z$, and expectations $\mathbb{E}_{X\mid Y}[f(X)]=\int_{\mathcal{X}}f(x)p(x\mid y)\,\mathrm{d}x$;
- statistical mechanics: the partition function $Z=\sum_s\exp(-H(s)/(kT))$ of a system with states $s$, Hamiltonian (energy) $H(s)$, Boltzmann's constant $k$ and temperature $T$, where summing over the huge number of configurations is prohibitively expensive;
- penalized likelihood model selection, and simulation of physical systems in nuclear physics and computer graphics.

MCMC is not one technique but a large class of sampling algorithms, including the Metropolis algorithm, Gibbs sampling and slice sampling.

## 9.1. Monte Carlo Integration

### 9.1.1. Numerical Integration by Simulation

Consider $\int_0^\pi\sin x\,\mathrm{d}x=2$. A Riemann sum, the Monte Carlo hit-or-miss method and R's adaptive quadrature give:

```r
n <- 100; h <- pi/n
x <- seq(from = 0, to = pi, length = n)
rect <- sin(x) * h
sum(rect)                                  # 1.979834

# Monte Carlo method: the hit-or-miss method
n <- 1e+5
xran <- runif(n, min = 0, max = pi)
yran <- runif(n, min = 0, max = 1)
sum(yran <= sin(xran))/n * pi              # 1.997

integrate(sin, lower = 0, upper = pi)      # 2 with absolute error < 2.2e-14
```

Despite a few uses of random simulation before computers, practical widespread use had to wait for them. Stanislaw Ulam conceived the method in 1946 while playing solitaire; the name, after the casino of Monte Carlo, started as a joke at a time when gambling was illegal in most places, and soon became a technical term for the simulation of random processes.

### 9.1.2. The Mean-Value Method

Let $X\sim p(x)$ and $\mathbb{E}f=I(f)=\int_{\mathcal{X}}f(x)p(x)\,\mathrm{d}x$. By the strong **law of large numbers**,

$$
\hat I_n(f)=\frac1n\sum_{i=1}^nf(X_i)\xrightarrow{\text{a.s.}}I(f),\qquad n\to\infty.
$$
If the $f(X_i)$ are i.i.d. with $0<\operatorname{Var}(f(X))<\infty$, the **central limit theorem** gives

$$
\frac{\hat I_n(f)-\mathbb{E}f}{\sqrt{\operatorname{Var}(f)/n}}\xrightarrow{d}\mathcal{N}(0,1).
$$
An unbiased estimator of $\operatorname{Var}(f)$ is $s^2=\frac1{n-1}\sum_{i=1}^n\bigl(f(X_i)-\hat I_n(f)\bigr)^2$, so an approximate $100(1-\alpha)\%$ confidence interval for $\mathbb{E}f$ is $\hat I_n(f)\pm z_{\alpha/2}s/\sqrt n$. The error is of order $n^{-1/2}$ whatever the dimension.

**Example 9.1.1** Let $X\sim\mathcal{N}(0,1)$ and $a=\mathbb{P}(\sin(\pi X)>0.5)$. Then $a=\mathbb{E}\bigl[\boldsymbol{1}\{\sin(\pi X)>0.5\}\bigr]=\mathbb{E}f$, so draw $X_i\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$ and form $\hat a=\frac1n\sum_{i=1}^n\boldsymbol{1}\{\sin(\pi X_i)>0.5\}$. The summands are i.i.d. $\mathrm{Ber}(a)$, so $\hat a$ satisfies a central limit theorem with variance $a(1-a)/n$.

### 9.1.3. Hit-or-Miss and Mean-Value: Variance Comparison

Suppose $0\le f(x)\le M$ for $a\le x\le b$, and we want $\theta=\int_a^bf(x)\,\mathrm{d}x$.

**Definition 9.1.1 (Two Monte Carlo Methods)** In the **hit-or-miss method**, drop $n$ points uniformly in the box $[a,b]\times[0,M]$ and let $\hat p$ be the proportion that falls under the graph of $f$; the estimate is

$$
\hat\theta_H=M(b-a)\hat p.
$$
In the **mean-value method** (crude Monte Carlo), write $\theta=(b-a)\int_a^bf(x)\frac{1}{b-a}\,\mathrm{d}x=(b-a)\mathbb{E}[f(X)]$ with $X\sim\mathrm{U}(a,b)$, and estimate

$$
\hat\theta_M=(b-a)\hat I_n(f)=\frac{b-a}{n}\sum_{i=1}^nf(X_i),\qquad X_i\overset{\text{iid}}{\sim}\mathrm{U}(a,b).
$$

**Theorem 9.1.1** With the same number $n$ of uniform points, $\operatorname{Var}(\hat\theta_M)\le\operatorname{Var}(\hat\theta_H)$.

**Proof** $\hat p=\frac1n\sum_iY_i$ with $Y_i\sim\mathrm{Ber}\bigl(\theta/(M(b-a))\bigr)$, so

$$
\operatorname{Var}(\hat\theta_H)=\frac{\theta\bigl(M(b-a)-\theta\bigr)}{n},\qquad\operatorname{Var}(\hat\theta_M)=\frac{(b-a)^2}{n}\operatorname{Var}(f(X)).
$$
Since $\mathbb{E}f=\theta/(b-a)$,

$$
\operatorname{Var}(\hat\theta_M)\le\operatorname{Var}(\hat\theta_H)\iff\mathbb{E}[f^2]-(\mathbb{E}f)^2\le M\frac{\theta}{b-a}-\Bigl(\frac{\theta}{b-a}\Bigr)^2=M\,\mathbb{E}f-(\mathbb{E}f)^2\iff\mathbb{E}[f^2]\le M\,\mathbb{E}f,
$$
which holds because $0\le f\le M$ implies $f^2\le Mf$. $\square$

Both estimators converge by the law of large numbers and allow confidence intervals by the central limit theorem; the mean-value method has the smaller variance and is the standard choice. (The hit-or-miss method throws away information: it only records whether a point is under the graph, not by how much.)

The same estimators apply in Bayesian inference. For a posterior $p(\theta\mid y)=L(\theta;y)p(\theta)/m(y)$ with likelihood $L(\theta;y)$, prior $p(\theta)$ and $m(y)=\int L(\theta;y)p(\theta)\,\mathrm{d}\theta$, the posterior mean of $f(\theta)$,

$$
\mu_f=\mathbb{E}(f(\theta)\mid y)=\int f(\theta)\frac{L(\theta;y)p(\theta)}{m(y)}\,\mathrm{d}\theta,
$$
is usually hopelessly intractable. If we can sample $\theta^{(i)}\sim p(\cdot\mid y)$, $i=1,\dots,n$, then $\hat\mu_f=\frac1n\sum_if(\theta^{(i)})=\bar f_n$ with $\operatorname{Var}(\bar f_n)=\operatorname{Var}(f(\theta))/n$. We are interested in methods that do not require the evaluation of $m(y)$.

## 9.2. Importance Sampling

### 9.2.1. The Importance Sampling Estimator

Recall rejection sampling ([3.5.8](/3.5.8)): to simulate $X\sim p$ from $Y\sim q$ on the same space $\Omega$, find $c$ with $cq(x)\ge p(x)$ for all $x$, simulate $y\sim q$ and $u\sim\mathrm{U}(0,1)$, and accept $y$ if $u<p(y)/(cq(y))$. It works because $(y,ucq(y))$ is uniform under $cq$, and the accepted points are uniform under $p$. Importance sampling tells a slightly different story: instead of producing samples of $p$, it estimates an expectation under $p$ directly from samples of $q$.

**Definition 9.2.1 (Importance Sampling)** Let $X\sim p$ on $\Omega$, let $\phi\colon\Omega\to\mathbb{R}$ be a given function, and suppose we want $\theta=\mathbb{E}_p[\phi(X)]$ but can only sample $Y\sim q$, where $q(x)>0$ wherever $\phi(x)p(x)\ne0$. Since

$$
\theta=\int\phi(x)p(x)\,\mathrm{d}x=\int\phi(x)\frac{p(x)}{q(x)}q(x)\,\mathrm{d}x=\mathbb{E}_q\bigl[\phi(Y)w(Y)\bigr],
$$
simulate $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}q$ and form the weighted average with **importance weights** $w(Y_i)=p(Y_i)/q(Y_i)$:

$$
\hat\theta_n^{\mathrm{IS}}=\frac1n\sum_{i=1}^n\phi(Y_i)w(Y_i).
$$
This is **importance sampling** (IS) with **proposal distribution** $q$.

With $\phi\equiv1$, $\frac1n\sum_iw(Y_i)$ is the IS estimator of $\mathbb{E}_p[1]=1$; this is a useful check on the weights.

**Proposition 9.2.1** If $\mathbb{E}_p[\phi(X)]$ and $\mathbb{E}_p[\phi^2(X)w(X)]$ are finite, then $\hat\theta_n^{\mathrm{IS}}$ is unbiased and consistent.

**Proof** Unbiasedness:

$$
\mathbb{E}_q\hat\theta_n^{\mathrm{IS}}=\frac1n\sum_{i=1}^n\mathbb{E}_q\Bigl[\phi(Y_i)\frac{p(Y_i)}{q(Y_i)}\Bigr]=\frac1n\sum_{i=1}^n\int_\Omega\phi(y)\frac{p(y)}{q(y)}q(y)\,\mathrm{d}y=\frac1n\sum_{i=1}^n\mathbb{E}_p[\phi(X)]=\theta.
$$
Consistency: by **Markov's inequality** $\mathbb{P}(Z\ge a)\le\mathbb{E}(Z)/a$ for $Z\ge0$, for any $\varepsilon>0$,

$$
\mathbb{P}\bigl(\lvert\hat\theta_n^{\mathrm{IS}}-\theta\rvert\ge\varepsilon\bigr)=\mathbb{P}\bigl(\lvert\hat\theta_n^{\mathrm{IS}}-\theta\rvert^2\ge\varepsilon^2\bigr)\le\frac{\mathbb{E}_q\lvert\hat\theta_n^{\mathrm{IS}}-\theta\rvert^2}{\varepsilon^2}=\frac{\operatorname{Var}_q\bigl(\phi(Y)w(Y)\bigr)}{n\varepsilon^2}\to0,
$$
because $\operatorname{Var}_q(\phi(Y)w(Y))\le\mathbb{E}_q[\phi^2w^2]=\mathbb{E}_p[\phi^2w]<\infty$. $\square$

**Example 9.2.1** We can simulate $Y\sim\Gamma(a,b)$ for $a=1,2,3,\dots$ and $b>0$ by summing exponentials (the transformation method). Suppose $Y_i\overset{\text{iid}}{\sim}\Gamma(a,b)$, and we want $\mathbb{E}_p[\phi(X)]$ for $X\sim\Gamma(\alpha,\beta)$ with arbitrary $\alpha,\beta>0$. The $\Gamma(\alpha,\beta)$ density is $p(x;\alpha,\beta)=\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-\beta x}$, so

$$
w(y)=\frac{p(y)}{q(y)}=\frac{\Gamma(a)\beta^\alpha}{\Gamma(\alpha)b^a}y^{\alpha-a}\mathrm{e}^{-(\beta-b)y},\qquad\hat\theta_n^{\mathrm{IS}}=\frac{\Gamma(a)\beta^\alpha}{\Gamma(\alpha)b^a}\cdot\frac1n\sum_{i=1}^n\phi(Y_i)Y_i^{\alpha-a}\mathrm{e}^{-(\beta-b)Y_i}
$$
is an unbiased and consistent estimate of $\mathbb{E}_p[\phi(X)]$. The same $Y$'s can be "recycled" to compute $\mathbb{E}_{\alpha,\beta}[\phi(X)]$ for many values of $\alpha$ and $\beta$.

### 9.2.2. The Variance of the Importance Sampling Estimator

**Proposition 9.2.2** If $\theta=\mathbb{E}_p[\phi(X)]$ and $\mathbb{E}_p[w(X)\phi^2(X)]$ are finite, then

$$
\operatorname{Var}_q\bigl(\hat\theta_n^{\mathrm{IS}}\bigr)=\frac1n\Bigl(\mathbb{E}_p\bigl[w(X)\phi^2(X)\bigr]-\theta^2\Bigr).
$$

**Proof**

$$
\begin{aligned}
\operatorname{Var}_q\bigl(\hat\theta_n^{\mathrm{IS}}\bigr)&=\frac1n\operatorname{Var}_q\bigl(\phi(Y)w(Y)\bigr)=\frac1n\Bigl(\mathbb{E}_q\bigl[w^2(Y)\phi^2(Y)\bigr]-\bigl(\mathbb{E}_q[w(Y)\phi(Y)]\bigr)^2\Bigr)\\
&=\frac1n\Bigl(\int_\Omega\frac{p^2(y)}{q^2(y)}\phi^2(y)q(y)\,\mathrm{d}y-\theta^2\Bigr)=\frac1n\Bigl(\int_\Omega\frac{p(y)}{q(y)}\phi^2(y)p(y)\,\mathrm{d}y-\theta^2\Bigr)=\frac1n\Bigl(\mathbb{E}_p[w\phi^2]-\theta^2\Bigr). \qquad\square
\end{aligned}
$$

For the crude estimator $\hat\theta_n^{\mathrm{MC}}=\frac1n\sum_i\phi(X_i)$, $X_i\sim p$, we have $\operatorname{Var}(\hat\theta_n^{\mathrm{MC}})=\frac1n\bigl(\mathbb{E}_p[\phi^2]-\theta^2\bigr)$, hence

$$
\operatorname{Var}_q\bigl(\hat\theta_n^{\mathrm{IS}}\bigr)=\operatorname{Var}\bigl(\hat\theta_n^{\mathrm{MC}}\bigr)-\frac1n\mathbb{E}_p\bigl[(1-w(X))\phi^2(X)\bigr].
$$
IS reduces the variance when $w<1$ (that is, $q>p$) where $\phi^2p$ is large: a good proposal puts more mass where $\lvert\phi\rvert p$ is large. Variance reduction is the main purpose of importance sampling.

Each time we use IS we should check that this variance is finite, and ideally small, that is, that $\mathbb{E}_p[w\phi^2]<\infty$. If $\phi(X)$ has finite mean and variance, then $\mathbb{E}_p[\phi^2]<\infty$; if in addition the weights are bounded, $w(x)\le M$ for all $x\in\Omega$, then

$$
\mathbb{E}_p[w\phi^2]\le M\,\mathbb{E}_p[\phi^2]<\infty.
$$
This is the same condition as for rejection, $p(x)/q(x)\le M$, except that now we only need the existence of $M$, not its value. The condition is only sufficient: $w$ may be unbounded while $\mathbb{E}_p[w\phi^2]$ is still finite. Importance sampling therefore has a wider domain of application than rejection, and it is statistically more efficient because no sample is wasted. The essential requirement is that the tails of $q$ are not lighter than those of $p$.

**Example 9.2.2** For the gamma example, $\mathbb{E}_p[w\phi^2]\propto\int_0^\infty p(x)x^{\alpha-a}\mathrm{e}^{-(\beta-b)x}\phi^2(x)\,\mathrm{d}x$. The factor $x^{\alpha-a}\mathrm{e}^{-(\beta-b)x}$ is bounded if $\alpha\ge a$ and $\beta>b$, which is sufficient for a finite variance. For $\phi(x)=1$,

$$
p(x)x^{\alpha-a}\mathrm{e}^{-(\beta-b)x}\propto x^{2\alpha-a-1}\mathrm{e}^{-(2\beta-b)x},
$$
which is integrable on $(0,\infty)$ if and only if $a<2\alpha$ and $b<2\beta$; this is necessary and sufficient. Take $a=b=2$, $\alpha=0.5$ and $\beta=2.5$, so that $2\alpha<a$. Monitoring the weights $w(y_i)$ and the running estimates $\hat\theta_m^{\mathrm{IS}}$, $m=1,\dots,n$, shows that the estimator is hit by occasional huge weights and never settles down.

### 9.2.3. Rare Events

Suppose $X\sim p$ and we want $\mathbb{P}(X>x_0)=\mathbb{E}_p[\boldsymbol{1}\{X>x_0\}]$ with $x_0$ far in the upper tail of $p$. A crude sample may contain no $X_i>x_0$ at all, and then $\hat\theta_n=\frac1n\sum_i\boldsymbol{1}\{X_i>x_0\}$ is simply zero. IS takes a $q$ that puts more probability on large values and reweights to get expectations under $p$, which can reduce the variance dramatically. Estimating the probability of a rare event is one of the most important applications of importance sampling; in finance, for example, it gives the probability that a loss exceeds the $99.9\%$ quantile.

**Example 9.2.3** Let $p(x)=\mathcal{N}(x;\mu,\sigma^2)$ and $\theta=\mathbb{P}(X>x_0)$ with $x_0\gg\mu+3\sigma$. A natural proposal sits over $x_0$: $q(y)=\mathcal{N}(y;x_0,\sigma^2)$. The weights are

$$
w(y)=\frac{\mathcal{N}(y;\mu,\sigma^2)}{\mathcal{N}(y;x_0,\sigma^2)}=\exp\Bigl(-\frac{(y-\mu)^2}{2\sigma^2}+\frac{(y-x_0)^2}{2\sigma^2}\Bigr),\qquad\hat\theta_n^{\mathrm{IS}}=\frac1n\sum_{i=1}^nw(Y_i)\boldsymbol{1}\{Y_i>x_0\}.
$$
For $\mathbb{P}(X>4)=3.17\times10^{-5}$ with $X\sim\mathcal{N}(0,1)$ and $q=\mathcal{N}(4,1)$, $100$ estimates with $n=1000$ each have a standard deviation about $100$ times smaller than those of crude Monte Carlo, most of which are exactly $0$.

![Importance sampling. Left: running estimates of E_p[1] = 1 for the target Gamma(0.5, 2.5); the proposal Gamma(2, 2) violates a < 2 alpha and is hit by huge weights, while Gamma(0.5, 1) converges. Right: 100 estimates of P(X > 4) for X ~ N(0, 1) with n = 1000: crude Monte Carlo mostly returns 0, importance sampling from N(4, 1) is accurate.](./plots/importance-sampling.py)

In the tail $p$ is tiny; a rejection envelope $cq$ covering it would reject almost every proposal, and a hundred million crude draws may not hit the event once. Importance sampling deliberately chooses a heavy-tailed or shifted proposal that samples the rare region often, and then pulls the samples back to reality with small weights. It is essentially the only classical non-Markov-chain method for rare event probabilities.

### 9.2.4. Unnormalized Densities

Normalizing constants are hard to compute, so we prefer algorithms that simulate $X\sim p$ without evaluating $p$ itself. Suppose $p(x)=\tilde p(x)/Z_p$ and $q(x)=\tilde q(x)/Z_q$, where we can evaluate $\tilde p$ and $\tilde q$ but not $Z_p$, $Z_q$. Rejection still works: find $M$ with $M\ge\tilde p(x)/\tilde q(x)$ for all $x$; simulate $y\sim q$ (which only requires $\tilde q$ in a rejection or MCMC sampler) and $u\sim\mathrm{U}(0,1)$; return $X=y$ if $u<\tilde p(y)/(M\tilde q(y))$, otherwise repeat.

**Example 9.2.4** Let $p(x)\propto\sin^2x/x^2$, $-\infty<x<\infty$, and $q(y)\propto(1+y^2)^{-1}$, the Cauchy distribution. Then

$$
\frac{\tilde p(x)}{\tilde q(x)}=\frac{(1+x^2)\sin^2x}{x^2}=\frac{\sin^2x}{x^2}+\sin^2x\le2=:M.
$$
Simulate $y\sim t_1$ and $u\sim\mathrm{U}(0,1)$; if $u<\dfrac{(1+y^2)\sin^2y}{2y^2}$, return $X=y$; otherwise repeat.

For importance sampling the same issue arises, because $w=p/q$ needs normalized densities. Let $\tilde w=\tilde p/\tilde q$. Then

$$
\mathbb{E}_q\Bigl[\frac1n\sum_{i=1}^n\frac{\tilde p(Y_i)}{\tilde q(Y_i)}\phi(Y_i)\Bigr]=\frac{Z_p}{Z_q}\mathbb{E}_p[\phi(X)],\qquad\mathbb{E}_q\Bigl[\frac1n\sum_{i=1}^n\frac{\tilde p(Y_i)}{\tilde q(Y_i)}\Bigr]=\frac{Z_p}{Z_q}.
$$

**Proposition 9.2.3 (Self-Normalized Importance Sampling)** The ratio

$$
\hat\theta_n^{\mathrm{IS}}=\frac{\frac1n\sum_{i=1}^n\tilde w(Y_i)\phi(Y_i)}{\frac1n\sum_{i=1}^n\tilde w(Y_i)}=\frac{\sum_{i=1}^n\tilde w(Y_i)\phi(Y_i)}{\sum_{i=1}^n\tilde w(Y_i)}
$$
is consistent for $\mathbb{E}_p[\phi(X)]$: by the law of large numbers the numerator converges to $\frac{Z_p}{Z_q}\mathbb{E}_p[\phi(X)]$ and the denominator to $\frac{Z_p}{Z_q}$.

This *self-normalized importance sampling* estimator is biased for finite $n$ but consistent, and it also satisfies a central limit theorem whose variance can be estimated by the **delta method**. Since it never needs $Z_p$, it is a key tool for posterior expectations in Bayesian computation.

**Example 9.2.5** Recall Example 9.2.1, with $Y_i\sim\Gamma(a,b)$ and target $\Gamma(\alpha,\beta)$. Dropping the constants, $\tilde w(y)=y^{\alpha-a}\mathrm{e}^{-(\beta-b)y}$, and $\sum_i\tilde w(Y_i)\phi(Y_i)/\sum_i\tilde w(Y_i)$ is consistent for $\mathbb{E}_p[\phi(X)]$. To estimate $\mathbb{E}_pX$ for $p=\Gamma(2,4)$ (true value $\alpha/\beta=0.5$), take $a=b=1$, so that $Y\sim\mathrm{Exp}(1)$:

```r
phi <- function(x) {x}
theta.est <- function(n, alpha, beta) {
  # IS estimate of E_p(phi(X)), X ~ Gamma(alpha, beta)
  y <- rexp(n)
  w <- y^(alpha-1) * exp(-(beta-1)*y)
  theta.hat <- sum(phi(y)*w)/sum(w)
  return(theta.hat)
}
theta.est(1000, alpha = 2, beta = 4)   # [1] 0.5043166
```

### 9.2.5. Rejection Sampling versus Importance Sampling

Both methods address the same difficulty, that we cannot sample the target $p$ directly, by opposite routes.

| Aspect | Rejection sampling | Importance sampling |
|---|---|---|
| treatment of samples | hard selection: unsuitable proposals are discarded, wasting computation | keeps every sample and adjusts it softly by its weight |
| requirement on the proposal | an envelope from above: $cq(x)\ge p(x)$ everywhere | cover from below: the tails of $q$ must not be lighter than those of $p$ ($p/q$ bounded suffices) |
| what matters | a small $c$ (high acceptance rate $1/c$) | a small variance of $p/q$ (under $\phi^2p$) |
| output | genuine i.i.d. samples from $p$ | weighted samples; only expectations |
| variance | controlled by the acceptance rate, always finite | may be infinite if the weights explode |
| rare events | hopeless: almost no proposal is accepted | the method of choice: tilt $q$ toward the event |
| high dimensions | $c$ grows exponentially with $d$ ($c\propto\kappa^d$), acceptance rate $\to0$ | weight degeneracy: almost all weight on one sample |

Rejection sampling has not been made obsolete by importance sampling, for two reasons. It produces genuine, independent samples from $p$, which are needed whenever the task is not just an expectation but a histogram, a density estimate, or the input of another random process. And its variance has an absolute safety bound: there is no catastrophic instability caused by a single extreme weight.

In high dimensions both methods fail, in different ways. For rejection, even if $q$ and $p$ are very similar in each coordinate, the global bound $c$ of a product over $d$ coordinates grows exponentially, and the acceptance rate $1/c$ tends to zero. For importance sampling, the overlap of $p$ and $q$ becomes very thin and the weight is a product of many ratios: of $100\,000$ samples, one may carry $99.99\%$ of the total weight. The *effective sample size*

$$
\mathrm{ESS}=\frac{\bigl(\sum_{i=1}^nw_i\bigr)^2}{\sum_{i=1}^nw_i^2}\in[1,n]
$$
then collapses to about $1$, and the estimate has a huge, practically infinite, variance.

In summary: in low dimensions, when pure samples are needed and a tight bound $c$ can be found, use rejection sampling; for expectations, integrals, tail behavior and rare events in low to moderate dimensions, use importance sampling; in high dimensions (say $d>10$, as in many Bayesian posteriors) both fail, and we turn to MCMC.

## 9.3. Markov Chains

### 9.3.1. Definition

A Markov chain is a process that moves from one state to another, randomly, and each step is "memoryless": the future depends only on the current state, not on the past. Simulation naturally leads us to discrete-time processes.

**Definition 9.3.1 (Markov Chain)** A sequence of random variables $X_0,X_1,\dots$ with values in a countable set $S$, the state space, is a **Markov chain** if it has the **Markov property**

$$
\mathbb{P}(X_{n+1}=x\mid X_0=x_0,X_1=x_1,\dots,X_n=x_n)=\mathbb{P}(X_{n+1}=x\mid X_n=x_n)
$$
for all $n$ and all states. It is time-homogeneous if $\mathbb{P}(X_{t+1}=j\mid X_t=i)=p_{ij}$ does not depend on $t$; the matrix $P=(p_{ij})\in\mathbb{R}^{\lvert S\rvert\times\lvert S\rvert}$ is the **transition matrix**, with $p_{ij}\ge0$ and row sums $\sum_jp_{ij}=1$.

A Markov chain thus requires three elements: a sequence of random variables (the chain), a state space (the values they take) and a transition matrix (the rules for the transitions). All chains below are time-homogeneous.

**Example 9.3.1** Let $X_t$ be the last number seen at time $t$ when drawing numbers from $\{1,2,3\}$. Drawing with replacement, the $X_t$ are i.i.d., which is a (trivial) Markov chain. Drawing without replacement, $X_t$ is not a Markov chain: the distribution of $X_3$ given $X_2$ depends on $X_1$, since the numbers already drawn cannot reappear.

A Markov chain is essentially a random walk on a graph. In a directed graph $G=(V,E)$ each vertex is a state and each edge carries the probability of moving from one state to the other; for each vertex $x$ the outgoing edges form a distribution, $\sum_jp_{xj}=1$. Starting at a vertex $x_0$, pick an outgoing edge at random according to these probabilities, move to $x_1$, and repeat. For example, on $S=\{1,2,3\}$,

$$
P=\begin{bmatrix}0.6&0.2&0.2\\0.3&0.4&0.3\\0&0.3&0.7\end{bmatrix}.
$$

**Remark 9.3.1** The Markov property is a property of a stochastic process (the future depends on the past only through the present); the memorylessness $\mathbb{P}(X>s+t\mid X>s)=\mathbb{P}(X>t)$ of the **exponential distribution** is a property of the distribution of a single random variable. The two should not be confused.

### 9.3.2. Stationary Distributions

Let $\{X_t\}_{t=0}^\infty$ be a homogeneous Markov chain on $S$ with initial distribution $X_0\sim\pi_0$ (a row vector) and transition probabilities $p_{ij}$. The $n$-step transition probabilities are $p_{ij}^{(n)}=\mathbb{P}(X_{t+n}=j\mid X_t=i)$, the entries of $P^n$. With $\pi_t(j)=\mathbb{P}(X_t=j)$, the **law of total probability** gives

$$
\pi_t(j)=\sum_{i\in S}\pi_{t-1}(i)p_{ij}=(\pi_{t-1}P)(j)=(\pi_0P^t)(j).
$$
In principle, any question about the probabilistic behavior of a Markov chain can be answered by matrix algebra.

**Definition 9.3.2 (Stationary Distribution)** A distribution $\pi$ on $S$ is a **stationary distribution** of the chain if $\pi=\pi P$, that is, $\pi(j)=\sum_i\pi(i)p_{ij}$ for all $j$. A distribution $\pi$ with $\lim_{n\to\infty}p_{ij}^{(n)}=\pi(j)$ for all $i,j$ is a limiting distribution of the chain.

The condition $\pi^{\mathsf T}=P^{\mathsf T}\pi^{\mathsf T}$ says that $\pi^{\mathsf T}$ is an eigenvector of $P^{\mathsf T}$ for the eigenvalue $1$. Since $P\boldsymbol{1}=\boldsymbol{1}$, the eigenvalue $1$ always exists, and since $P^n$ is again stochastic for all $n$, no eigenvalue has modulus larger than $1$.

**Theorem 9.3.1 (Detailed Balance)** Let $S$ be a discrete state space and $\pi$ a distribution on $S$. If for all $i,j\in S$

$$
\pi(i)p_{ij}=\pi(j)p_{ji},
$$
then $\pi$ is a stationary distribution of $P$.

**Proof** $(\pi P)(i)=\sum_j\pi(j)p_{ji}=\sum_j\pi(i)p_{ij}=\pi(i)\sum_jp_{ij}=\pi(i)$. $\square$

The equation is the *detailed balance condition*; a chain satisfying it is called a *reversible Markov chain*, because in equilibrium every transition $i\to j$ occurs as often as the reverse transition $j\to i$. Detailed balance is sufficient, not necessary, for stationarity, and it is much easier to check than $\pi=\pi P$; every MCMC algorithm below is built on it.

**Corollary 9.3.1** If $S$ is finite and $P$ is symmetric, $P=P^{\mathsf T}$, the uniform distribution $\pi(i)=1/\lvert S\rvert$ is stationary; the chain is reversible, since any transition occurs with equal probability in the forward and reverse directions. More generally, the uniform distribution is stationary whenever $P$ is doubly stochastic, that is, its column sums are also $1$, as for

$$
P=\begin{bmatrix}0.2&0.3&0.5\\0.4&0.3&0.3\\0.4&0.4&0.2\end{bmatrix},\qquad\pi=\bigl(\tfrac13,\tfrac13,\tfrac13\bigr).
$$

**Example 9.3.2** Consider the two-state chain on $S=\{0,1\}$ with

$$
P=\begin{bmatrix}1-a&a\\b&1-b\end{bmatrix},\qquad a,b\in[0,1],\ 0<a+b<2,
$$
started in state $0$ with probability $\alpha$, $\pi_0=(\alpha,1-\alpha)$. The eigenvalues of $P$ are $1$ and $1-a-b$, and

$$
P^n=\frac{1}{a+b}\begin{bmatrix}b&a\\b&a\end{bmatrix}+\frac{(1-a-b)^n}{a+b}\begin{bmatrix}a&-a\\-b&b\end{bmatrix}
$$
(write $P=E_1+(1-a-b)E_2$, where $E_1,E_2$ are the two matrices above including the factor $1/(a+b)$; then $E_1^2=E_1$, $E_2^2=E_2$ and $E_1E_2=E_2E_1=O$, so $P^n=E_1+(1-a-b)^nE_2$). Since $\lvert1-a-b\rvert<1$,

$$
\lim_{n\to\infty}P^n=\frac{1}{a+b}\begin{bmatrix}b&a\\b&a\end{bmatrix},\qquad\pi=\lim_{n\to\infty}\pi_n=\Bigl(\frac{b}{a+b},\frac{a}{a+b}\Bigr)
$$
for every $\alpha$. The same $\pi$ follows from $\pi=\pi P$: the first coordinate gives $\pi(0)(1-a)+\pi(1)b=\pi(0)$, i.e. $a\pi(0)=b\pi(1)$, which is also the detailed balance condition.

The stationary probabilities have a second meaning. Let $R$ be the first return time to state $0$ and $r_0=\mathbb{E}(R\mid X_0=0)$ the *mean return time*. Conditioning on the first step, if $X_1=0$ then $R=1$, and if $X_1=1$ then $R=1+G$ with $G\sim\mathrm{Geo}(b)$ the time to leave state $1$, so $\mathbb{E}(R\mid X_1=1)=1+1/b$ and

$$
r_0=(1-a)\cdot1+a\Bigl(1+\frac1b\Bigr)=\frac{a+b}{b}=\frac1{\pi(0)}.
$$
Similarly $r_1=(a+b)/a=1/\pi(1)$. In general, for an irreducible positive recurrent chain (defined below), $r_i=1/\pi(i)$: if $\pi(i)=1/4$, the chain is in state $i$ one quarter of the time and needs on average four steps to return to it.

A stationary distribution need not be a limiting distribution. With $a=b=1$, $P=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has the stationary distribution $\pi=(\frac12,\frac12)$, since $\pi P=\pi$. But $X_{n+2}=X_n$: the chain alternates, $X_n=X_0$ for even $n$ and $X_n=X_1$ for odd $n$, so $P^n$ has no limit, the distribution of $X_n$ does not converge, and it depends on the initial distribution. Sometimes no limiting distribution exists.

### 9.3.3. The Basic Limit Theorem

Three properties of a chain control its long-run behavior: it should move freely through the state space, it should not cycle deterministically, and it should come back.

**Definition 9.3.3 (Irreducibility)** State $j$ is accessible from $i$ ($i\to j$) if $p_{ij}^{(n)}>0$ for some $n\ge0$; $i$ and $j$ communicate ($i\leftrightarrow j$) if $i\to j$ and $j\to i$. The chain, or its transition matrix $P$, is **irreducible** if every pair of states communicates, that is, $S$ consists of one communicating class; equivalently, the transition graph is strongly connected.

**Definition 9.3.4 (Period)** The **period** of state $i$ is $d_i=\gcd\{n\ge1\colon p_{ii}^{(n)}>0\}$. State $i$ is **aperiodic** if $d_i=1$, so that returns to $i$ can occur at irregular times; for a state with $d_i=1$ there is $n'$ such that $p_{ii}^{(n)}>0$ for all $n\ge n'$. The chain is aperiodic if all its states are.

For example, $S=\{0,1\}$ with $P=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has $d_0=d_1=2$. Likewise, on $S=\{1,2,3,4\}$ with $\pi_0=(1,0,0,0)$ and

$$
P=\begin{bmatrix}0&1/2&0&1/2\\1/2&0&1/2&0\\0&1/2&0&1/2\\1/2&0&1/2&0\end{bmatrix},
$$
$p_{11}^{(n)}=0$ for all odd $n$, and every state has period $2$.

**Theorem 9.3.2** If states $i,j\in S$ communicate, then $d_i=d_j$. In particular, all states of an irreducible chain have the same period.

**Proof** Since $j$ is accessible from $i$, there is $n_1$ with $p_{ij}^{(n_1)}>0$; since $i$ is accessible from $j$, there is $n_2$ with $p_{ji}^{(n_2)}>0$. Then $p_{ii}^{(n_1+n_2)}\ge p_{ij}^{(n_1)}p_{ji}^{(n_2)}>0$, so $d_i\mid(n_1+n_2)$. Let $n$ be any integer with $p_{jj}^{(n)}>0$. Then $p_{ii}^{(n_1+n+n_2)}>0$, so $d_i\mid(n_1+n+n_2)$, hence $d_i\mid n$. Thus $d_i$ divides every element of $\{n\colon p_{jj}^{(n)}>0\}$, and $d_j\ge d_i$. Interchanging $i$ and $j$ gives $d_i\ge d_j$. $\square$

A simple trick makes an irreducible chain aperiodic: add a self-loop, $p_{ii}>0$ for some state $i$.

**Definition 9.3.5 (Recurrence)** A state is **transient** if, after leaving it, there is a positive probability of never returning; it is **recurrent** if the chain returns to it with probability $1$. A recurrent state is **positive recurrent** if its mean return time is finite and **null recurrent** if it is infinite (a return with probability $1$ does not imply a finite expected return time).

On a finite state space every state of an irreducible chain is positive recurrent.

**Theorem 9.3.3 (Basic Limit Theorem)** Let the Markov chain $X_0,X_1,\dots$ be irreducible, aperiodic and positive recurrent (for a finite state space: irreducible and aperiodic). Then there is a unique stationary distribution $\pi$, and for any initial distribution $\pi_0$,

$$
\lim_{n\to\infty}\pi_n(i)=\pi(i)\quad\text{for all states } i;
$$
equivalently, $\lim_{n\to\infty}P^n$ is the matrix whose rows all equal $\pi$.

We say that the chain targets $\pi$: wherever it starts, after some time it is in state $i$ with probability about $\pi(i)$. A chain with these three properties is called *ergodic*: ergodicity = irreducibility + aperiodicity + positive recurrence. For simulation, the most important consequence is the ergodic theorem: for an irreducible positive recurrent chain with stationary distribution $\pi$ and any $\phi$ with $\mathbb{E}_\pi\lvert\phi\rvert<\infty$,

$$
\frac1n\sum_{t=0}^{n-1}\phi(X_t)\xrightarrow{\text{a.s.}}\mathbb{E}_\pi[\phi(X)],
$$
from any starting state. This is the law of large numbers for Markov chains; averages along one path replace averages over independent samples.

Putting the two parts together gives MCMC. We want $\mathbb{E}_p[\phi(X)]$ for a probability mass function or density $p$ on $S$. By the Monte Carlo method the problem is to generate random elements of $S$ with distribution $p$; MCMC does this by constructing a Markov chain with stationary distribution $\pi=p$. Simulate a correlated sequence $X_0,X_1,X_2,\dots$ with $X_t\sim\pi$ (or at least $X_t\xrightarrow{d}\pi$), and use the usual estimate

$$
\hat\phi_n=\frac1n\sum_{t=0}^{n-1}\phi(X_t).
$$
For example, a random walk on $\{0,1\}^m$: pick $j\in\{1,\dots,m\}$ uniformly at random and flip the $j$-th coordinate of $X_{t-1}=(z_1,\dots,z_m)$, $X_t=(z_1,\dots,1-z_j,\dots,z_m)$; the transition matrix is symmetric, so the chain targets the uniform distribution. MCMC methods also apply to countably infinite and continuous state spaces, and they are among the most versatile Monte Carlo algorithms we have.

## 9.4. The Metropolis–Hastings Algorithm

### 9.4.1. The Algorithm

Suppose we need samples from a probability mass function $\pi(x)=\tilde\pi(x)/Z_\pi$ on $S=\{1,\dots,m\}$, known only up to the constant $Z_\pi$. It is enough to give a rule for simulating $X_{t+1}$ given $X_t$. In all Metropolis–Hastings (MH) algorithms, a candidate $Y$ is generated from a proposal distribution $q(\cdot\mid X_t)$, where $Y\sim q(\cdot\mid x)$ means $\mathbb{P}(Y=y\mid X=x)=q(y\mid x)$. If the candidate is accepted, the chain moves to $X_{t+1}=Y$; otherwise it stays, $X_{t+1}=X_t$. The proposal may depend on the current state; its choice is very flexible, but the resulting chain must converge to the target $\pi$.

**Algorithm 9.4.1 (Metropolis–Hastings Algorithm)**

1. Choose a proposal distribution $q(\cdot\mid X_t)$, subject to regularity conditions (the chain must be irreducible and aperiodic).
2. Generate $X_0$, for example from $q$.
3. Repeat until the chain has converged to its stationary distribution according to some criterion:
   1. generate $Y$ from $q(\cdot\mid X_t)$ and $U$ from $\mathrm{U}(0,1)$;
   2. if
      $$
      U\le\alpha(Y\mid X_t)=\min\Bigl\{1,\frac{\tilde\pi(Y)\,q(X_t\mid Y)}{\tilde\pi(X_t)\,q(Y\mid X_t)}\Bigr\},
      $$
      accept $Y$ and set $X_{t+1}=Y$; otherwise set $X_{t+1}=X_t$;
   3. increment $t$.

The candidate is accepted with probability $\alpha(Y\mid X_t)$, the acceptance probability; since only the ratio $\tilde\pi(Y)/\tilde\pi(X_t)$ appears, it suffices to know the target up to a constant.

**Theorem 9.4.1** The Markov chain generated by the Metropolis–Hastings algorithm satisfies detailed balance with respect to $\pi$; hence $\pi$ is a stationary distribution, and if the chain is irreducible and aperiodic, $\pi$ is its limiting distribution.

**Proof** By the basic limit theorem it suffices to show that $\pi$ is stationary, and by Theorem 9.3.1 that $\pi(x)p_{xy}=\pi(y)p_{yx}$. For $x=y$ this is clear. For $y\ne x$, the chain moves from $X_t=x$ to $X_{t+1}=y$ if $y$ is proposed and then accepted, so $p_{xy}=q(y\mid x)\alpha(y\mid x)$ and

$$
\begin{aligned}
\pi(x)p_{xy}&=\pi(x)q(y\mid x)\min\Bigl\{1,\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)}\Bigr\}=\min\bigl\{\pi(x)q(y\mid x),\ \pi(y)q(x\mid y)\bigr\}\\
&=\pi(y)q(x\mid y)\min\Bigl\{1,\frac{\pi(x)q(y\mid x)}{\pi(y)q(x\mid y)}\Bigr\}=\pi(y)q(x\mid y)\alpha(x\mid y)=\pi(y)p_{yx}. \qquad\square
\end{aligned}
$$

### 9.4.2. Examples

**Example 9.4.1** Let $\pi(x)=x/Z_\pi$ with $Z_\pi=\sum_{x=1}^mx$, $x=1,\dots,m$. As proposal take $Y\sim\mathrm{U}\{1,\dots,m\}$, $q(y\mid x)=1/m$, which is irreducible (any state is reachable in a single step). If $X_t=x$: simulate $y\sim\mathrm{U}\{1,\dots,m\}$ and $u\sim\mathrm{U}(0,1)$; if

$$
u\le\min\Bigl\{1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\Bigr\}=\min\Bigl\{1,\frac yx\Bigr\},
$$
set $X_{t+1}=y$, otherwise $X_{t+1}=x$. The trace of the chain (state $X_t$ against $t$) jumps around $\{1,\dots,30\}$, and the histogram of $X_t$ grows linearly in $x$:

```r
m <- 30
n <- 10000; X <- rep(NA, n)
X[1] <- 1
for (t in 1:(n-1)) {
  x <- X[t]
  y <- ceiling(m*runif(1))     # uniform proposal on 1, ..., m
  a <- min(1, y/x)             # acceptance probability
  U <- runif(1)
  if (U <= a) {
    X[t+1] <- y
  } else {
    X[t+1] <- x
  }
}
plot(X[1:200], type = "l"); hist(X)
```

**Example 9.4.2** To simulate the **Poisson distribution** $\pi(x)=\mathrm{e}^{-\lambda}\lambda^x/x!\propto\lambda^x/x!$, use the simple proposal $q(y\mid x)=1/2$ for $y=x\pm1$: toss a coin and add or subtract $1$. If $X_t=x$, simulate $y\sim\mathrm{U}\{x-1,x+1\}$ and $u\sim\mathrm{U}(0,1)$. If $y=-1$ then $\alpha=0$; otherwise

$$
\alpha(y\mid x)=\min\Bigl\{1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\Bigr\}=\begin{cases}\min\Bigl\{1,\dfrac{\lambda}{x+1}\Bigr\},&y=x+1,\\[2ex]\min\Bigl\{1,\dfrac{x}{\lambda}\Bigr\},&y=x-1.\end{cases}
$$
If $u\le\alpha(y\mid x)$, set $X_{t+1}=y$; otherwise $X_{t+1}=x$.

For continuous random variables the same algorithm applies with densities: computers represent the reals by a fine finite grid, the target and proposal probabilities of a grid cell are approximately density times cell length, and the cell lengths cancel in the Hastings ratio $\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}$. So the theory of chains on finite spaces carries over; a rigorous treatment uses transition kernels on general state spaces.

**Example 9.4.3** To simulate $X\sim\mathcal{N}(0,1)$, with target $\tilde\pi(x)\propto\exp(-x^2/2)$, we need a simple irreducible proposal. Fix $a>0$ and choose a new point uniformly in a window of length $2a$ centered at $x$, $q(y\mid x)=\frac{1}{2a}\boldsymbol{1}\{x-a<y<x+a\}$. Then $q(y\mid x)=q(x\mid y)$, and the algorithm is: if $X_t=x$, simulate $y\sim\mathrm{U}(x-a,x+a)$ and $u\sim\mathrm{U}(0,1)$; if $u\le\alpha(y\mid x)$, set $X_{t+1}=y$, otherwise $X_{t+1}=x$, where

$$
\alpha(y\mid x)=\min\Bigl\{1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\Bigr\}=\min\Bigl\{1,\exp\Bigl(-\frac{y^2}2+\frac{x^2}2\Bigr)\Bigr\}.
$$

```r
a <- 3; n <- 2000
X <- numeric(n); X[1] <- 0
for (t in 1:(n-1)) {
  x <- X[t]
  y <- x + (2*runif(1) - 1)*a          # uniform proposal on (x - a, x + a)
  if (runif(1) < exp((x^2 - y^2)/2)) {
    X[t+1] <- y
  } else {
    X[t+1] <- x
  }
}
```

### 9.4.3. Special Cases

- The *Metropolis algorithm*: the proposal is symmetric, $q(x\mid y)=q(y\mid x)$, and the acceptance probability reduces to $\min\{1,\tilde\pi(Y)/\tilde\pi(X_t)\}$; moves uphill are always accepted, moves downhill sometimes. Examples 9.4.1–9.4.3 are of this type.
- The *random walk Metropolis* algorithm: $q(y\mid x)=g(y-x)$ for a symmetric density $g$. At each iteration an increment $Z\sim g$ is generated and $Y=X_t+Z$.
- The *independence sampler*: the proposal does not depend on the current state, $q(y\mid x)=q(y)$. The acceptance probability is $\min\{1,w(Y)/w(X_t)\}$ with the importance weight $w=\tilde\pi/q$, which links MH to importance sampling; the sampler works well when $q$ is close to $\pi$ with heavier tails.
- The Gibbs sampler, treated next.

## 9.5. The Gibbs Sampler

The Gibbs sampler is often applied when the target is a multivariate distribution $\pi(\boldsymbol{x})$, $\boldsymbol{x}=(x_1,\dots,x_d)$. Write $\boldsymbol{x}_{(-j)}=(x_1,\dots,x_{j-1},x_{j+1},\dots,x_d)$; the distribution of $X_j$ given $\boldsymbol{X}_{(-j)}=\boldsymbol{x}_{(-j)}$ is the *full conditional distribution* $\pi(x_j\mid\boldsymbol{x}_{(-j)})$. Denote $X_t$ by $\boldsymbol{X}(t)$.

**Algorithm 9.5.1 (Gibbs Sampler)**

1. Initialize $\boldsymbol{X}(0)$ at time $t=0$.
2. For each iteration $t=1,2,\dots$:
   1. set $\boldsymbol{x}=\boldsymbol{X}(t-1)$;
   2. for each coordinate $j=1,\dots,d$, generate $X_j^*(t)$ from $\pi(x_j\mid\boldsymbol{x}_{(-j)})$ and update $x_j=X_j^*(t)$;
   3. set $\boldsymbol{X}(t)=(X_1^*(t),\dots,X_d^*(t))$; every candidate is accepted.

The Gibbs sampler is particularly natural, and it works well if the conditional distributions are easy to sample. Consider a bivariate density $\pi(\theta_1,\theta_2)$, and suppose $(\theta_1,\theta_2)\sim\pi$. Simulate $\theta_1'\sim\pi(\theta_1'\mid\theta_2)$, then $\theta_2'\sim\pi(\theta_2'\mid\theta_1')$ using the new $\theta_1'$. The distribution of $(\theta_1',\theta_2')$ is

$$
\begin{aligned}
p(\theta_1',\theta_2')&=\int\!\!\int\pi(\theta_1,\theta_2)\,\pi(\theta_1'\mid\theta_2)\,\pi(\theta_2'\mid\theta_1')\,\mathrm{d}\theta_1\,\mathrm{d}\theta_2
=\int\!\!\int\pi(\theta_1,\theta_2)\frac{\pi(\theta_1',\theta_2)}{\pi(\theta_2)}\cdot\frac{\pi(\theta_1',\theta_2')}{\pi(\theta_1')}\,\mathrm{d}\theta_1\,\mathrm{d}\theta_2\\
&=\pi(\theta_1',\theta_2')\int\pi(\theta_1\mid\theta_2)\,\mathrm{d}\theta_1\int\pi(\theta_2\mid\theta_1')\,\mathrm{d}\theta_2=\pi(\theta_1',\theta_2'),
\end{aligned}
$$
since each integral equals $1$ (in the second step, $\pi(\theta_1,\theta_2)/\pi(\theta_2)=\pi(\theta_1\mid\theta_2)$ and $\pi(\theta_1',\theta_2)/\pi(\theta_1')=\pi(\theta_2\mid\theta_1')$). So if $\theta^{(0)}=(\theta_1,\theta_2)\sim\pi$, then after these two steps $\theta^{(1)}=(\theta_1',\theta_2')\sim\pi$ is a new, correlated, sample, and iterating gives $\theta^{(2)},\theta^{(3)},\dots$: $\pi$ is stationary. The Gibbs sampler comes in several flavors. In the multivariate case $\theta=(\theta_1,\dots,\theta_K)$ we may sample $\pi(\theta_i\mid\theta_{(-i)})$ for $i=1,\dots,K$ in turn (systematic scan), or select $i\sim\mathrm{U}\{1,\dots,K\}$ at each step (random scan). The ergodicity conditions must be checked whenever a new sampler is constructed.

**Proposition 9.5.1** Consider an MH algorithm targeting $\pi(\theta_1,\theta_2)$ with the proposal $q(\theta_1'\mid\theta)=\pi(\theta_1'\mid\theta_2)$ that updates only $\theta_1$. Its acceptance probability equals $1$; hence the Gibbs sampler is a Metropolis–Hastings sampler.

**Proof** With $X_t=(\theta_1,\theta_2)$ and $Y=(\theta_1',\theta_2)$, $\tilde\pi=\pi$, $q(Y\mid X_t)=\pi(\theta_1'\mid\theta_2)$ and $q(X_t\mid Y)=\pi(\theta_1\mid\theta_2)$,

$$
\alpha(Y\mid X_t)=\min\Bigl\{1,\frac{\pi(\theta_1',\theta_2)\,\pi(\theta_1\mid\theta_2)}{\pi(\theta_1,\theta_2)\,\pi(\theta_1'\mid\theta_2)}\Bigr\}=\min\Bigl\{1,\frac{\pi(\theta_2)}{\pi(\theta_2)}\Bigr\}=1,
$$
because $\pi(\theta_1',\theta_2)/\pi(\theta_1'\mid\theta_2)=\pi(\theta_2)=\pi(\theta_1,\theta_2)/\pi(\theta_1\mid\theta_2)$. $\square$

**Example 9.5.1** For the standard **bivariate normal distribution** with correlation $\rho$, the full conditionals are $X\mid Y=y\sim\mathcal{N}(\rho y,1-\rho^2)$ and $Y\mid X=x\sim\mathcal{N}(\rho x,1-\rho^2)$ ([3.1.15](/3.1.15)). The Gibbs sampler alternates these two draws. Each move is parallel to a coordinate axis; when $\lvert\rho\rvert$ is close to $1$ the density is a narrow ridge along the diagonal, the moves are short, and the chain explores the distribution slowly. Indeed the sequence $X_t$ is an AR(1) process with coefficient $\rho^2$, so its lag-$k$ autocorrelation is $\rho^{2k}$.

![Gibbs sampler for the standard bivariate normal. Left: the first 15 sweeps from (-3, 3) for rho = 0.9 move parallel to the axes along the ridge of the density. Right: the trace of the first coordinate for rho = 0.5 mixes fast, for rho = 0.99 it wanders slowly.](./plots/gibbs-bivariate-normal.py)

## 9.6. Convergence Diagnostics

The basic limit theorem guarantees convergence only as $n\to\infty$; in practice we must decide how long to run the chain and how much of it to use. Standard practice:

- *Burn-in*: discard an initial segment of the chain, during which it moves from the starting point to the region where $\pi$ has its mass; only the remaining states are averaged.
- Trace plots of $X_t$ against $t$: a well-mixing chain looks like stationary noise without trends or long flat stretches. Several chains from dispersed starting points should overlap.
- Autocorrelations: successive states are correlated, which inflates the variance of $\hat\phi_n$. With lag-$k$ autocorrelations $\rho_k$ of $\phi(X_t)$, $\operatorname{Var}(\hat\phi_n)\approx\frac{\operatorname{Var}_\pi(\phi)}{n}\bigl(1+2\sum_{k\ge1}\rho_k\bigr)$, so the chain is worth $n/(1+2\sum_k\rho_k)$ independent draws (its effective sample size).
- The Gelman–Rubin statistic $\hat R$ compares the variance between several parallel chains with the variance within them; values close to $1$ (say below $1.01$–$1.1$) indicate convergence.

The scale of the proposal governs the mixing of random walk Metropolis. Small steps are almost always accepted but move slowly; large steps are rarely accepted, so the chain sticks. Both produce high autocorrelation. A theoretical guideline (Roberts, Gelman and Gilks, 1997) is an acceptance rate of about $0.44$ in one dimension and $0.234$ in high dimensions.

![Random walk Metropolis for N(0, 1) with uniform proposals on (x - a, x + a), started at 10. With a = 0.1 nearly every move is accepted but the chain drifts slowly toward the target; with a = 30 almost every proposal is rejected and the trace is flat for long stretches; a = 2.5 mixes well, with the fastest decay of the autocorrelation after the burn-in of 200 iterations.](./plots/rw-metropolis-mixing.py)

## Summary

- Classical Monte Carlo: the hit-or-miss and the mean-value methods both rest on the law of large numbers; the mean-value method has the smaller variance.
- Two mirror-image routes when $p$ cannot be sampled directly. Rejection sampling (hard selection) bounds $p$ from above by $cq$; it gives genuine i.i.d. samples with a safe variance, but $c$ explodes in high dimensions. Importance sampling (soft weighting) needs no $c$ and wastes no samples, with $w=p/q$; it is the tool for rare events and, self-normalized, for unnormalized posteriors, but its weights degenerate in high dimensions.
- Markov chains: the Markov property and the transition matrix; a stationary distribution solves $\pi=\pi P$, detailed balance $\pi_ip_{ij}=\pi_jp_{ji}$ is sufficient but not necessary; a periodic chain can have a stationary but no limiting distribution. Basic limit theorem: irreducible + aperiodic + positive recurrent (ergodic) $\Rightarrow$ a unique stationary distribution, which is the limit from any start.
- MCMC joins the two Monte Carlo ideas: construct a chain whose stationary distribution is the target, let it converge, and replace the average of independent samples by the average along the correlated chain. Metropolis–Hastings accepts $Y\sim q(\cdot\mid x)$ with probability $\min\bigl\{1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\bigr\}$; the Gibbs sampler draws each coordinate from its full conditional distribution and accepts always. In practice, discard a burn-in, inspect trace plots and autocorrelations, and tune the proposal.

| Method | Independence of samples | Target | Goal | High dimensions |
|---|---|---|---|---|
| crude Monte Carlo | independent | easy to sample | expectations, integrals | fine, if we can sample |
| importance sampling | weighted, independent | any, with a proposal | expectations, integrals | weights degenerate |
| rejection sampling | independent | any, with an envelope | samples | acceptance rate decays exponentially |
| MCMC | dependent | any, unnormalized | expectations, samples | the standard tool |
