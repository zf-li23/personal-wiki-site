---
title: Goodness-of-Fit Tests
description: The one-sample Kolmogorov–Smirnov test and its one-sided versions; its distribution-free null distribution and exact computation; the asymptotic theory behind it (Glivenko–Cantelli, the empirical process, Donsker's theorem, the Brownian bridge and the Kolmogorov distribution); applications to a uniform model, random number generators and confidence bands; testing normality with estimated parameters (the Lilliefors test, Shapiro–Wilk, Q–Q plots); Pearson's chi-squared test for discrete distributions, grouping of cells and estimated parameters.
---

The location problems of [3.6.3](/3.6.3)–[3.6.5](/3.6.5) asked about one feature of a distribution, its center. A **goodness-of-fit test** asks about the whole distribution: is it plausible that the sample came from a specified distribution $F_0$? The question arises whenever a model is proposed (are break points of threads uniform, are accident counts Poisson, are these residuals normal?) and before choosing between parametric and nonparametric methods. [3.2.6](/3.2.6) introduced the two standard tools, the **Kolmogorov–Smirnov test** for continuous distributions and Pearson's $\chi^2$ test for grouped data. This chapter explains why the Kolmogorov–Smirnov test works, from the **Glivenko–Cantelli theorem** to Donsker's theorem and the Brownian bridge; applies it, with exact and asymptotic $p$-values and confidence bands; shows what goes wrong when the parameters of $F_0$ are estimated from the same data and how the Lilliefors test repairs it; and returns to the $\chi^2$ test for discrete distributions, with grouping and estimated parameters. The two-sample version, the Smirnov test, follows in [3.6.10](/3.6.10).

Throughout, $X_1,\dots,X_n$ are i.i.d. with continuous distribution function $F$, $X_{(1)}\le\cdots\le X_{(n)}$ are the order statistics, and $F_n(x)=\frac1n\sum_{i=1}^n\boldsymbol{1}\{X_i\le x\}$ is the **empirical distribution function**. For each $x$, $F_n(x)$ is a random variable; as $x$ varies, $F_n$ is a random function, a random element of the space of distribution functions.

## 6.1. The Kolmogorov–Smirnov Test Revisited

**Example 6.1.1 (Thread Breaks)** Twenty threads, each $6\,\mathrm{cm}$ long, are subjected to strain, and the distance from one end at which each breaks is recorded:

$$
0.6,\ 0.8,\ 1.1,\ 1.2,\ 1.4,\ 1.7,\ 1.8,\ 1.9,\ 2.2,\ 2.4,\ 2.5,\ 2.9,\ 3.1,\ 3.4,\ 3.4,\ 3.9,\ 4.4,\ 4.9,\ 5.2,\ 5.9 .
$$
Is the break point equally likely to be anywhere along the thread, that is, is $X\sim\mathrm{U}(0,6)$ with $F_0(x)=x/6$ on $[0,6]$?

:::

The idea of the test is that $F_n$ is a consistent estimator of the true $F$; for a sample from $F_0$, $F_n$ should not depart violently from $F_0$ anywhere. The test measures the largest departure, the **Kolmogorov distance** of [3.6.2](/3.6.2) between $F_n$ and $F_0$.

**Definition 6.1.1 (Kolmogorov–Smirnov Test)** To test $H_0\colon F=F_0$ for a continuous, completely specified $F_0$, the one-sample **Kolmogorov–Smirnov test** uses

$$
D_n=\sup_{x\in\mathbb{R}}\lvert F_n(x)-F_0(x)\rvert,\qquad D_n^+=\sup_{x\in\mathbb{R}}\big(F_n(x)-F_0(x)\big),\qquad D_n^-=\sup_{x\in\mathbb{R}}\big(F_0(x)-F_n(x)\big),
$$
and rejects $H_0$ for large values of $D_n$ against the two-sided alternative $H_1\colon F\ne F_0$, of $D_n^+$ against $H_1\colon F>F_0$ (the observations tend to be smaller than under $F_0$), and of $D_n^-$ against $H_1\colon F<F_0$ (they tend to be larger).

Because $F_n$ is a step function and $F_0$ is nondecreasing, the suprema are attained at the jumps, just after or just before an order statistic:

$$
D_n^+=\max_{1\le i\le n}\Big\{\frac in-F_0(X_{(i)})\Big\},\qquad D_n^-=\max_{1\le i\le n}\Big\{F_0(X_{(i)})-\frac{i-1}{n}\Big\},\qquad D_n=\max\{D_n^+,D_n^-\}.
$$
The test of $F\ne F_0$ is two-sided although it rejects only for large $D_n$: large values of $D_n$ arise from departures in either direction, and small values of $D_n$ are never evidence against $H_0$. (The alternatives $F>F_0$ and $F<F_0$ are meant in the sense "$\ge$ everywhere, $>$ somewhere".)

**Example 6.1.2 (Thread Breaks, Continued)** With $F_0(x)=x/6$, the largest value of $i/n-X_{(i)}/6$ occurs at $X_{(15)}=3.4$, where $F_{20}(3.4)=15/20=0.75$ and $F_0(3.4)=0.567$; thus $D_{20}^+=0.183$. The largest value of $X_{(i)}/6-(i-1)/n$ is $0.100$, at $X_{(1)}=0.6$, so $D_{20}^-=0.100$ and $D_{20}=0.183$. The empirical distribution lies above $F_0$ in the middle of the range: breaks between $2$ and $4\,\mathrm{cm}$ are somewhat more frequent than uniformity predicts. Whether this is more than chance is the question of §6.3.

:::

![The break points of 20 threads: the empirical distribution function with the 95% Kolmogorov band (F_n plus or minus 0.294), the uniform distribution function on (0, 6) and an alternative piecewise-linear distribution function. The Kolmogorov distance to the uniform, 0.183, is attained just after the jump at x = 3.4. Both hypothesized functions stay inside the band.](./plots/thread-edf.py)

The key property of the statistic is that its null distribution does not depend on $F_0$.

**Theorem 6.1.1** If $F_0$ is continuous, then under $H_0$ the distributions of $D_n$, $D_n^+$ and $D_n^-$ do not depend on $F_0$: they are those obtained for a sample from $\mathrm{U}(0,1)$ tested against the uniform distribution.

**Proof** By the **probability integral transform**, $U_i=F_0(X_i)$ are i.i.d. $\mathrm{U}(0,1)$ under $H_0$. Since $F_0$ is nondecreasing, $X_i\le x$ implies $U_i\le F_0(x)$, and for continuous $F_0$ the converse holds except on a null set, so $F_n(x)=G_n(F_0(x))$ almost surely, where $G_n$ is the empirical distribution function of the $U_i$. Hence $\sup_x\lvert F_n(x)-F_0(x)\rvert=\sup_x\lvert G_n(F_0(x))-F_0(x)\rvert=\sup_{0<u<1}\lvert G_n(u)-u\rvert$, because $F_0$ takes every value in $(0,1)$; the one-sided statistics are handled in the same way. $\square$

So $D_n$ is a **distribution-free statistic**: one table of critical values serves every continuous $F_0$. The exact distribution is a statement about uniform order statistics $U_{(1)}<\cdots<U_{(n)}$, whose joint density is $n!$ on $\{0<u_1<\cdots<u_n<1\}$. Since $D_n<t$ if and only if $\lvert i/n-U_{(i)}\rvert<t$ and $\lvert U_{(i)}-(i-1)/n\rvert<t$ for every $i$, each order statistic must lie in a "safety band" around the midpoint $\frac{2i-1}{2n}$ of the $i$-th step of the empirical distribution function. Writing $t=\frac1{2n}+v$, Kolmogorov's formula is

$$
\mathbb{P}\left(D_n<\frac1{2n}+v\right)=\begin{cases}0, & v\le0,\\[4pt] \displaystyle\int_{\frac1{2n}-v}^{\frac1{2n}+v}\int_{\frac3{2n}-v}^{\frac3{2n}+v}\cdots\int_{\frac{2n-1}{2n}-v}^{\frac{2n-1}{2n}+v}n!\ \mathrm{d}u_n\cdots\mathrm{d}u_1, & 0<v<\frac{2n-1}{2n},\\[10pt] 1, & v\ge\frac{2n-1}{2n},\end{cases}
$$
with the integrand restricted to $0<u_1<\cdots<u_n<1$. The smallest possible value of $D_n$ is $\frac1{2n}$, attained when every $U_{(i)}$ sits exactly at the midpoint $\frac{2i-1}{2n}$, and $D_n\le1$ always. The $n$-fold integral is evaluated numerically by recursive algorithms; R's `ks.test(..., exact = TRUE)` uses the method of Marsaglia, Tsang and Wang (2003).

## 6.2. Asymptotic Theory

Exact computation becomes expensive for large $n$, and in any case we want to understand how $D_n$ behaves. Three limit theorems, each stronger than the last, answer the question.

### 6.2.1. The Uniform Law of Large Numbers

For fixed $x$, $nF_n(x)\sim\mathrm{Bin}(n,F(x))$ is a count and $F_n(x)$ a sample proportion, so the ordinary law of large numbers gives $F_n(x)\to F(x)$ almost surely. Much more is true: the convergence is uniform in $x$. This is the Glivenko–Cantelli theorem ([Theorem 1.5.2](/3.2.1#thm-1.5.2) of 3.2.1, from 1933),

$$
D_n=\sup_{x\in\mathbb{R}}\lvert F_n(x)-F(x)\rvert\xrightarrow{\text{a.s.}}0 .
$$
For the test it means consistency: under $H_0$, $D_n\to0$, while if the true $F$ differs from $F_0$, then $\sup_x\lvert F_n-F_0\rvert\to\sup_x\lvert F-F_0\rvert>0$, so $\sqrt nD_n\to\infty$ and the test rejects with probability tending to $1$ against every fixed alternative.

### 6.2.2. The Empirical Process and Donsker's Theorem

For fixed $x$, the **central limit theorem** gives the rate of this convergence:

$$
\sqrt n\big(F_n(x)-F(x)\big)\xrightarrow{d}\mathcal{N}\big(0,F(x)(1-F(x))\big).
$$
But $D_n$ is a supremum over all $x$, and the distribution of a supremum is not determined by the distributions at single points. We need the joint behavior of the whole random curve.

**Definition 6.2.1 (Empirical Process)** The **empirical process** of the sample is the random function

$$
G_n(x)=\sqrt n\big(F_n(x)-F(x)\big)=\frac{1}{\sqrt n}\sum_{i=1}^nZ_i(x),\qquad Z_i(x)=\boldsymbol{1}\{X_i\le x\}-F(x),\qquad x\in\mathbb{R}.
$$

For each $x$, the $Z_i(x)$ are i.i.d. with mean $0$ and variance $F(x)(1-F(x))$, and for $x\le y$

$$
\operatorname{Cov}\big(G_n(x),G_n(y)\big)=\operatorname{Cov}\big(\boldsymbol{1}\{X\le x\},\boldsymbol{1}\{X\le y\}\big)=F(x)-F(x)F(y)=\min\{F(x),F(y)\}-F(x)F(y).
$$
By the multivariate central limit theorem, the finite-dimensional distributions of $G_n$ converge to those of a Gaussian process with this covariance. That process has a name.

**Definition 6.2.2 (Brownian Bridge)** Let $W$ be a standard Brownian motion on $[0,1]$: a Gaussian process with continuous paths, $W(0)=0$, mean $0$ and $\operatorname{Cov}(W(s),W(t))=\min\{s,t\}$. The process

$$
B(t)=W(t)-tW(1),\qquad 0\le t\le1,
$$
is the (standard) **Brownian bridge**. It is a Gaussian process with continuous paths, $B(0)=B(1)=0$, mean $0$ and

$$
\operatorname{Cov}\big(B(s),B(t)\big)=\min\{s,t\}-st,\qquad\text{in particular}\quad\operatorname{Var}B(t)=t(1-t).
$$

The Brownian bridge has the same law as **Brownian motion** conditioned on $W(1)=0$, a random walk path "pinned down" at both ends; for a bridge over $[0,T]$ the variance is $t(T-t)/T$. Comparing covariances, the limit of the empirical process is $B\big(F(x)\big)$, the Brownian bridge run on the time scale $t=F(x)$. Donsker's insight was that the convergence holds for the whole process, not only for finitely many points at a time.

The prototype is the random walk. Let $X_1,X_2,\dots$ be i.i.d. with mean $0$ and variance $\sigma^2$ (for example, fair $\pm1$ coin flips), with partial sums $S_k=X_1+\cdots+X_k$, and let $X^{(n)}_t$, $t\in[0,1]$, be the polygonal path through the points $\big(k/n,\,S_k/(\sigma\sqrt n)\big)$, $k=0,\dots,n$. Donsker's theorem (1951), also called the invariance principle, states that $X^{(n)}\xrightarrow{d}W$ as random continuous functions: the rescaled random walk converges in distribution to standard Brownian motion. "Convergence in distribution" here means **weak convergence** of the laws on the function space, so that $\mathbb{E}\,h(X^{(n)})\to\mathbb{E}\,h(W)$ for every bounded continuous functional $h$, such as a maximum or an integral of the path. The version for distribution functions is the one we need.

**Theorem 6.2.1 (Donsker's Theorem)** For i.i.d. observations from a continuous distribution function $F$, the empirical process converges in distribution, as a random function, to a Brownian bridge on the time scale $F$:

$$
G_n=\sqrt n\,(F_n-F)\xrightarrow{d}B\circ F,\qquad n\to\infty .
$$
Consequently, for every functional $h$ that is continuous (in the supremum norm), $h(G_n)\xrightarrow{d}h(B\circ F)$.

We do not prove the theorem; the technical points are the choice of topology (the empirical process has jumps, so it lives in a space of functions with jumps) and the tightness of the sequence. Its role relative to the central limit theorem is easy to state:

| | Central limit theorem | Donsker's theorem (functional CLT) |
|---|---|---|
| object | one random variable, at a fixed point | a whole random curve (empirical process, random walk) |
| limit | a normal distribution | a Brownian bridge (or Brownian motion) |
| what it yields | asymptotic distribution of a single statistic | asymptotic distribution of any continuous functional of the curve: maximum, supremum, integral |

![Left: five sample paths of the uniform empirical process, the square root of n times (F_n(t) minus t), for n = 1000; they look like Brownian bridges, tied to zero at both ends. Right: the simulated null distribution of the square root of n times D_n for n = 20 (20000 samples) and the Kolmogorov density; the dashed line is the asymptotic 5% critical value 1.358.](./plots/brownian-bridge.py)

### 6.2.3. Suprema of the Brownian Bridge

By Theorem 6.1.1 we may take $F$ uniform, so that $F(x)=t$ and the limit is $B$ itself. Since the supremum of the absolute value is a continuous functional, Donsker's theorem gives

$$
\sqrt nD_n=\sup_t\lvert G_n(t)\rvert\xrightarrow{d}\sup_{0\le t\le1}\lvert B(t)\rvert,\qquad \sqrt nD_n^+\xrightarrow{d}\sup_{0\le t\le1}B(t),
$$
and the distributions of these suprema of the Brownian bridge are known in closed form.

**Definition 6.2.3 (Kolmogorov Distribution)** The **Kolmogorov distribution** is the distribution of $\sup_{0\le t\le1}\lvert B(t)\rvert$; its distribution function is

$$
K(x)=1-2\sum_{k=1}^\infty(-1)^{k-1}\mathrm{e}^{-2k^2x^2}=\sum_{k=-\infty}^{\infty}(-1)^k\mathrm{e}^{-2k^2x^2},\qquad x>0 .
$$

**Theorem 6.2.2 (Kolmogorov, Smirnov)** If $F_0$ is continuous, then under $H_0$, for every $x>0$,

$$
\lim_{n\to\infty}\mathbb{P}\big(\sqrt nD_n\le x\big)=K(x),\qquad \lim_{n\to\infty}\mathbb{P}\big(\sqrt nD_n^+\le x\big)=\lim_{n\to\infty}\mathbb{P}\big(\sqrt nD_n^-\le x\big)=1-\mathrm{e}^{-2x^2}.
$$

The one-sided limits agree because the Brownian bridge is symmetric under turning it upside down: $-B$ is again a Brownian bridge, and $\sup(-B)=-\inf B$. The series for $K$ converges extremely fast, and a few terms give high accuracy; for the tail, $1-K(x)\approx2\mathrm{e}^{-2x^2}$, twice the one-sided tail, because large values of $\sup\lvert B\rvert$ come almost always from one side only. The asymptotic two-sided $5\%$ critical value of $\sqrt nD_n$ is $1.358$. Note that $D_n^+$ and $D_n$ do not have the same distribution: $D_n\ge D_n^+$ always, and $D_n$ is stochastically larger.

**Corollary 6.2.1** If $F_0$ is continuous, then under $H_0$ the statistic $V=4n\big(D_n^+\big)^2$ has the limiting distribution $\chi^2_2$.

**Proof** For $x>0$, $V\le4x^2$ if and only if $\sqrt nD_n^+\le x$. Hence $\lim_n\mathbb{P}(V\le4x^2)=1-\mathrm{e}^{-2x^2}=1-\mathrm{e}^{-4x^2/2}$, that is, $\lim_n\mathbb{P}(V\le y)=1-\mathrm{e}^{-y/2}$ for all $y>0$, which is the distribution function of $\chi^2_2$ (the exponential distribution with mean $2$). $\square$

## 6.3. Applications

**Example 6.3.1 (Thread Breaks, Continued)** For $D_{20}=0.1833$:

```r
x <- c(0.6, 0.8, 1.1, 1.2, 1.4, 1.7, 1.8, 1.9, 2.2, 2.4, 2.5, 2.9, 3.1, 3.4, 3.4, 3.9, 4.4, 4.9, 5.2, 5.9)
ks.test(x, "punif", min = 0, max = 6)                # asymptotic p-value, because of the tie at 3.4
ks.test(x, "punif", min = 0, max = 6, exact = TRUE)  # exact p-value
n <- length(x); d <- 0.1833
2 * sum((-1)^(0:29) * exp(-2 * (1:30)^2 * n * d^2))  # the series 1 - K(sqrt(n) d)
```

```text
	One-sample Kolmogorov-Smirnov test
data:  x
D = 0.18333, p-value = 0.5121
alternative hypothesis: two-sided
Warning message: ties should not be present for the Kolmogorov-Smirnov test

	One-sample Kolmogorov-Smirnov test
data:  x
D = 0.18333, p-value = 0.4583
alternative hypothesis: two-sided
```

The exact $p$-value is $0.458$ and the asymptotic one $1-K(\sqrt{20}\times0.1833)=0.512$; there is no evidence against uniformity. (The warning concerns the two breaks recorded at $3.4$: rounding produces ties that a continuous model excludes. Their effect on the $p$-value is negligible here.) For the one-sided statistics, the asymptotic $p$-values are $\mathrm{e}^{-2\cdot20\cdot0.1833^2}=0.261$ for $D_{20}^+=0.183$ and $\mathrm{e}^{-2\cdot20\cdot0.1^2}=0.670$ for $D_{20}^-=0.100$, and Corollary 6.2.1 gives the same numbers: `1 - pchisq(4 * n * 0.1^2, df = 2)` is $0.670$.

The two-sided $5\%$ critical value for $n=20$ is $0.294$ from the exact distribution. The asymptotic one is $1.358/\sqrt{20}=0.304$; solving the one-sided equation $\mathrm{e}^{-2nd^2}=0.025$ gives $d=\sqrt{-\log(0.025)/(2n)}=0.3037$ as well, which is also $\sqrt{\chi^2_{2,0.025}/n}/2$ by Corollary 6.2.1. That the two-sided critical value can be computed from the one-sided tail at level $\alpha/2$ reflects the tail approximation $1-K(x)\approx2\mathrm{e}^{-2x^2}$.

:::

**Example 6.3.2 (Testing a Random Number Generator)** Five numbers produced by a generator of supposedly $\mathrm{U}(0,1)$ variates are $0.44,0.81,0.14,0.05,0.93$. Sorted, $R_{(1)},\dots,R_{(5)}=0.05,0.14,0.44,0.81,0.93$, and with $i/N=0.2,0.4,0.6,0.8,1.0$:

$$
\begin{aligned}
D^+&=\max_i\Big\{\frac iN-R_{(i)}\Big\}=\max\{0.15,0.26,0.16,-0.01,0.07\}=0.26,\\
D^-&=\max_i\Big\{R_{(i)}-\frac{i-1}{N}\Big\}=\max\{0.05,-0.06,0.04,0.21,0.13\}=0.21,
\end{aligned}
$$
so $D=0.26$. The exact $5\%$ critical value for $N=5$ is $0.563$, and $0.26<0.563$: no evidence against the generator. The exact $p$-value is $0.81$; the asymptotic one, $1-K(\sqrt5\times0.26)=1-K(0.581)=0.89$, is rough for so small a sample. A real generator is of course tested with millions of numbers and with a battery of tests for uniformity and independence ([3.5.8](/3.5.8)).

:::

### 6.3.1. Confidence Bands

Inverting the test gives a **confidence band** for the whole distribution function. If $d_\alpha$ is the $1-\alpha$ quantile of $D_n$ under $H_0$, then for any continuous $F$

$$
\mathbb{P}\Big(F_n(x)-d_\alpha\le F(x)\le F_n(x)+d_\alpha\ \text{for all }x\Big)=\mathbb{P}(D_n\le d_\alpha)=1-\alpha,
$$
so the band $\big[\max\{F_n-d_\alpha,0\},\min\{F_n+d_\alpha,1\}\big]$ covers the entire unknown $F$ with probability $1-\alpha$. A fully specified $F_0$ is rejected by the Kolmogorov–Smirnov test at level $\alpha$ exactly when its graph leaves the band somewhere. This duality makes the band a convenient tool for comparing several candidate distributions at once. (The band from the **DKW inequality** of [3.6.2](/3.6.2), with half-width $\sqrt{\log(2/\alpha)/(2n)}$, is slightly wider and valid for every $n$; for $n=20$ and $\alpha=0.05$ its half-width is $0.304$, against the exact $0.294$.)

**Example 6.3.3 (Two Candidate Distributions)** For the thread data, compare (i) $\mathrm{U}(0,6)$ with (ii) the distribution function

$$
F(x)=\frac x5,\quad 0<x\le3;\qquad F(x)=0.2+\frac{4x}{30},\quad 3<x\le6,
$$
which puts probability $0.6$ on the first half of the thread. Both are completely specified, and the Kolmogorov distances are $0.183$ for (i) and $0.120$ for (ii), both below $0.294$. Both distribution functions stay inside the $95\%$ band in the figure of §6.1; equivalently, a plot of $F(x)-F_n(x)$ against $x$ for both candidates stays within $\pm0.294$. There is no strong evidence against either hypothesis: twenty observations cannot distinguish them.

:::

## 6.4. Testing Normality with Estimated Parameters

Many statistical methods assume that the data come from a normal distribution, or at least from one that is approximately normal, and checking this is often part of deciding whether to use a nonparametric method. If $\mu$ and $\sigma^2$ are specified, the Kolmogorov–Smirnov test applies directly. Usually, though, the null hypothesis says only that the distribution is normal with some $\mu$ and $\sigma^2$, and the parameters must be estimated from the data. The tempting procedure is to standardize, $z_i=(x_i-\bar x)/s$, and compare the empirical distribution function of the $z_i$ with $\Phi$ using the ordinary Kolmogorov tables.

The statistic is fine; the tables are not. The estimated $\hat\mu=\bar x$ and $\hat\sigma=s$ are fitted to the same data, so the fitted normal distribution function is pulled toward $F_n$, and $D_n$ is systematically smaller than when the true parameters are used. With the ordinary critical values the test is far too conservative: it rarely rejects, even when normality is false.

**Definition 6.4.1 (Lilliefors Test)** The **Lilliefors test** of the composite hypothesis that the data are normal with unknown $\mu,\sigma^2$ computes

$$
D_n=\sup_z\big\lvert S_n(z)-\Phi(z)\big\rvert,
$$
where $S_n$ is the empirical distribution function of $z_i=(x_i-\bar x)/s$, and refers it to the null distribution of this statistic when $\mu,\sigma^2$ are estimated, obtained by simulation from normal samples (it does not depend on the true $\mu$ and $\sigma$).

The statistic is exactly the Kolmogorov–Smirnov statistic; only the reference distribution changes. Lilliefors (1967) tabulated it by Monte Carlo simulation. For computation, Dallal and Wilkinson (1986) gave the approximation, for $p<0.1$ and $5\le n\le100$,

$$
p\approx\exp\Big(-7.01256\,D_n^2(n+2.78019)+2.99587\,D_n\sqrt{n+2.78019}-0.122119+\frac{0.974598}{\sqrt n}+\frac{1.67997}{n}\Big),
$$
and for larger $p$-values one uses Stephens's (1974) modified statistic $D^*=D_n\big(\sqrt n-0.01+0.85/\sqrt n\big)$, whose distribution is nearly free of $n$. R's `nortest::lillie.test` implements both.

![Null distribution of the Kolmogorov–Smirnov statistic for normal samples of size 30, simulated 20000 times, when the mean and standard deviation are known and when they are estimated from the same sample (the Lilliefors statistic). Estimation shifts the distribution to the left; the 95% quantiles (dashed) are 0.242 and 0.159. The observed value 0.192 of Example 6.4.1 is unremarkable under the first distribution and extreme under the second.](./plots/lilliefors-null.py)

**Example 6.4.1** A sample of $30$ observations:

$$
11,13,14,22,29,30,41,41,52,55,56,59,65,65,66,74,74,75,77,81,82,82,82,82,83,85,85,87,87,88 .
$$
The estimates are $\bar x=61.43$ and $s=25.04$. For the smallest value, $z_1=(11-61.43)/25.04=-2.014$ and $\Phi(z_1)=0.022$, against $S_n(z_1)=1/30=0.033$; continuing, the largest difference is $0.192$, where the fitted normal distribution function exceeds the empirical one just below $x=74$ (the long left tail of the data makes the normal curve rise too early). The ordinary Kolmogorov $p$-value would be $0.218$ (asymptotic; the exact value is $0.19$), suggesting no departure from normality. The Lilliefors $p$-value is $0.0062$ (the simulation in the figure gives $0.0056$), and the $1\%$ critical value for $n=30$, $0.183$, is exceeded: the sample is clearly not normal.

```r
x <- c(11, 13, 14, 22, 29, 30, 41, 41, 52, 55, 56, 59, 65, 65, 66,
       74, 74, 75, 77, 81, 82, 82, 82, 82, 83, 85, 85, 87, 87, 88)
n <- length(x)
z <- (x - mean(x)) / sd(x)
ks.test(z, "pnorm")                    # D = 0.1921, p-value = 0.2182 (wrong reference distribution)
dn <- 0.1921
exp(-7.01256 * dn^2 * (n + 2.78019) + 2.99587 * dn * sqrt(n + 2.78019) -
      0.122119 + 0.974598 / sqrt(n) + 1.67997 / n)   # 0.006245726
nortest::lillie.test(x)                # D = 0.1921, p-value = 0.006246
shapiro.test(x)                        # W = 0.86294, p-value = 0.001171
```

:::

Calling `ks.test(x, "pnorm", mean = mean(x), sd = sd(x))` gives the same wrong $p$-value as the standardized version: the problem is not how the data are standardized but that the parameters came from the data.

The **Shapiro–Wilk test** of [3.2.6](/3.2.6) is built for exactly this composite hypothesis. Its statistic $W$ is, up to the use of generalized least squares weights, the squared correlation between the ordered data and the expected order statistics of a standard normal sample; $W\le1$, values close to $1$ support normality, and normality is rejected when $W$ is too small. (Under non-normality $W$ is noticeably below $1$, not near $0$: for the data above $W=0.863$.) Simulation studies consistently find it among the most powerful normality tests against a wide range of alternatives, more powerful than the Lilliefors and Kolmogorov tests, especially for small and moderate samples; the **Anderson–Darling test**, which weights the tails more heavily than $D_n$, is a strong competitor. For Example 6.4.1, `shapiro.test` gives $p=0.0012$.

No test replaces a plot. A **normal Q–Q plot** (R: `qqnorm(x); qqline(x)`, or `plot(qnorm(((1:n) - 0.5) / n), sort(x))`) shows how the data depart from normality, which no $p$-value does: for Example 6.4.1 the points bend away from the line in the left tail. Moreover, $p$-values depend heavily on the sample size. With a small sample, a normality test has little power, and "not rejected" means little; with a very large sample, it rejects for departures far too small to matter, and a significance test for non-normality is then essentially useless. What matters is whether the departure is large enough to affect the method that will be used.

## 6.5. Discrete Distributions: Pearson's Chi-Squared Test

For a discrete $F_0$ the Kolmogorov–Smirnov test is still valid but conservative: the probability integral transform no longer yields uniform variables, the null distribution of $D_n$ is stochastically smaller than in the continuous case, and the continuous tables give too few significant results. Goodness of fit to a discrete distribution, typically for counts, is usually tested with Pearson's $\chi^2$ statistic ([Theorem 6.3.1](/3.2.6#thm-6.3.1) of 3.2.6): with $O_j$ the observed and $E_j$ the expected frequencies of $r$ cells under $H_0$,

$$
\chi^2=\sum_{j=1}^r\frac{(O_j-E_j)^2}{E_j}\ \overset{\cdot}{\sim}\ \chi^2_{r-1-s},
$$
where $s$ is the number of parameters estimated from the data. Each estimated parameter (the $p$ of a **binomial distribution**, the $\lambda$ of a **Poisson distribution**) costs one degree of freedom: fitting makes the expected counts closer to the observed ones, so the statistic is smaller than it would be with known parameters. Two practical rules accompany the test. The approximation needs large expected counts, traditionally $E_j\ge5$ in every cell; sparse cells, usually in the tails, are merged with neighbors before computing $\chi^2$. And the degrees-of-freedom rule holds when the parameters are estimated efficiently from the grouped counts (by maximum likelihood on the grouped data or by minimum $\chi^2$); if they are estimated from the ungrouped data, the null distribution lies between $\chi^2_{r-1-s}$ and $\chi^2_{r-1}$ (Chernoff and Lehmann, 1954), and using $\chi^2_{r-1-s}$ is slightly liberal. The continuity correction $\sum_j(\lvert O_j-E_j\rvert-0.5)^2/E_j$ is sometimes suggested, but it matters only for very few cells and is rarely used beyond the $1$-degree-of-freedom case.

**Example 6.5.1 (Recorded Ages at Death)** It is often suggested that recorded ages at death are influenced by two factors: people strive to reach a "round" age, a new decade, before dying; and elderly people misstate their age, tending to round it (a person aged $73$ to $77$ may say $75$). Both would distort the distribution of the last digit of recorded ages. For $117$ males whose deaths are recorded at Badenscallie, a burial ground in Scotland, the last digits of the ages are:

| last digit | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
|---|---|---|---|---|---|---|---|---|---|---|
| frequency | $7$ | $11$ | $17$ | $19$ | $9$ | $13$ | $9$ | $11$ | $13$ | $8$ |

Under $H_0$ every digit is equally likely, with expected frequency $117/10=11.7$. The differences are $-4.7,-0.7,5.3,7.3,-2.7,1.3,-2.7,-0.7,1.3,-3.7$, and

$$
\chi^2=\sum_{j}\frac{(O_j-11.7)^2}{11.7}=\frac{136.1}{11.7}=11.63
$$
on $9$ degrees of freedom. The upper $5\%$ point is $\chi^2_{9,0.05}=16.92>11.63$, and $p=0.235$: there is no real evidence against $H_0$.

The test, however, answers a question somewhat different from the one posed. Both suggested mechanisms concern old people, but the records include all ages: $41$ of the $117$ deaths occurred before age $60$, several of them of very young children, and for these neither striving for a decade nor misstating age is plausible. Mixing them in dilutes any effect among the elderly. Moreover, survival until a notable family event (the birth of a grandchild, say) may be a stronger incentive than the completion of a decade, and misstatement of age occurs for many reasons and across a wide range of ages. A sharper analysis would restrict attention to deaths at advanced ages, accepting the smaller sample.

:::

**Example 6.5.2 (Accidents and the Poisson Distribution)** A factory employs $220$ people. The numbers of people experiencing $0,1,2,\dots$ accidents in a year are:

| accidents $r$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $\ge6$ |
|---|---|---|---|---|---|---|---|
| people $n_r$ | $181$ | $9$ | $4$ | $10$ | $7$ | $4$ | $5$ |

Are the data consistent with a Poisson distribution? The mean $\lambda$ is unknown. The log-likelihood is $\ell(\lambda)=\sum_rn_r\big(r\log\lambda-\lambda-\log r!\big)$, so $\partial\ell/\partial\lambda=\sum_rn_r(r/\lambda-1)=0$ gives the **maximum likelihood estimation** formula $\hat\lambda=\sum_rrn_r/\sum_rn_r=125/220=0.568$, treating the $5$ people in the last cell as having exactly $6$ accidents (a small approximation; the grouped-data MLE would treat the cell as "$\ge6$"). The expected numbers $E_r=220\,\hat\lambda^r\mathrm{e}^{-\hat\lambda}/r!$ are

| accidents $r$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $\ge6$ |
|---|---|---|---|---|---|---|---|
| expected $E_r$ | $124.6$ | $70.8$ | $20.1$ | $3.8$ | $0.5$ | $0.06$ | $0.01$ |

The cells from $3$ accidents upward have tiny expected counts, so they are merged into one cell "$\ge3$" with $E=4.4$ (close enough to $5$) and $O=26$:

$$
\chi^2=\frac{(181-124.6)^2}{124.6}+\frac{(9-70.8)^2}{70.8}+\frac{(4-20.1)^2}{20.1}+\frac{(26-4.4)^2}{4.4}=197.7,
$$
with $4-1-1=2$ degrees of freedom ($\chi^2_{2,0.05}=5.99$). The $p$-value is below $10^{-40}$: the Poisson model is decisively rejected. (Rounding the expected counts to one decimal gives $198.3$.)

The rejection is not surprising. Accident counts would be Poisson if accidents occurred entirely at random, if every person had the same accident rate and if having one accident did not change the chance of another. The data show the typical pattern of heterogeneity: too many people with no accident and too many with several, compared with the fitted Poisson. The sample variance, about $1.98$, is more than three times the mean $0.568$; this **overdispersion** points to differences in accident proneness between people, which a mixture such as the **negative binomial distribution** can model.

:::

## Summary

| Test | Null hypothesis | Statistic | Null distribution | Notes |
|---|---|---|---|---|
| Kolmogorov–Smirnov (Definition 6.1.1) | $F=F_0$, continuous and fully specified | $D_n$, $D_n^\pm$ | distribution-free (Theorem 6.1.1); exact, or $\sqrt nD_n\to$ Kolmogorov, $4n(D_n^+)^2\to\chi^2_2$ | consistent; duality with confidence bands |
| Lilliefors (Definition 6.4.1) | normal, $\mu,\sigma^2$ unknown | $D_n$ of standardized data | simulated; Dallal–Wilkinson formula | ordinary KS tables far too conservative here |
| Shapiro–Wilk | normal, $\mu,\sigma^2$ unknown | $W$ (correlation with normal scores) | tabulated or computed | high power for small and moderate $n$ |
| Pearson $\chi^2$ | discrete $F_0$, $s$ parameters estimated | $\sum(O-E)^2/E$ | $\chi^2_{r-1-s}$ | merge cells to $E\ge5$; estimate from grouped data |

- The asymptotic theory rests on three layers: Glivenko–Cantelli (uniform convergence of $F_n$, hence consistency), the pointwise central limit theorem, and Donsker's theorem (Theorem 6.2.1): the empirical process $\sqrt n(F_n-F)$ converges to the Brownian bridge $B\circ F$ (Definition 6.2.2), so suprema of $\sqrt n\lvert F_n-F\rvert$ converge to the Kolmogorov distribution (Definition 6.2.3, Theorem 6.2.2).
- Examples: thread breaks ($D=0.183$, exact $p=0.458$, uniform not rejected); random numbers ($D=0.26<0.563$); a non-normal sample (KS tables $p=0.22$, Lilliefors $p=0.006$, Shapiro–Wilk $p=0.001$); digits of ages ($\chi^2_9=11.63$, $p=0.235$); accidents (Poisson rejected, $\chi^2_2\approx198$, overdispersion).
- Formal tests of fit should always be read together with a plot (EDF with band, Q–Q plot) and with the sample size in mind.

## Questions

1. Why is the test based on $D_n=\sup_x\lvert F_n(x)-F_0(x)\rvert$ called two-sided, although it rejects only when $D_n$ is large?

   **Answer** "Two-sided" refers to the alternative, $F\ne F_0$, which includes departures in both directions ($F_n$ above $F_0$ somewhere or below it). Both kinds make $D_n$ large, because of the absolute value; a small $D_n$ means that $F_n$ is close to $F_0$ everywhere, which is never evidence against $H_0$. The rejection region is therefore one-tailed in the statistic and two-sided in the alternative, like the $\chi^2$ test or the $F$ test of an analysis of variance.

2. For the five failure times $2.5,3.8,4.1,5.5,6.0$ (hours), construct the $95\%$ Kolmogorov confidence band for $F(4.0)$, given the exact critical value $D_{5,0.05}\approx0.563$.

   **Answer** Two of the five observations are at most $4.0$, so $F_5(4.0)=0.4$. The band at $x=4.0$ is $[\max\{0.4-0.563,0\},\min\{0.4+0.563,1\}]=[0,0.963]$. The band covers the whole curve $F$ simultaneously with probability $0.95$; for a single point, the pointwise binomial interval (Clopper–Pearson for $2$ out of $5$ is $[0.053,0.853]$) is narrower, which is the price of simultaneity, and with only five observations both are very wide.

3. Explain why the Kolmogorov–Smirnov test is consistent against every fixed alternative $F\ne F_0$, and what Donsker's theorem adds.

   **Answer** By the Glivenko–Cantelli theorem, $\sup_x\lvert F_n-F\rvert\to0$ almost surely, so $D_n=\sup_x\lvert F_n-F_0\rvert\to\sup_x\lvert F-F_0\rvert=\delta>0$, and $\sqrt nD_n\approx\sqrt n\,\delta\to\infty$, exceeding any fixed critical value with probability tending to $1$. Glivenko–Cantelli gives consistency but no critical values. Donsker's theorem gives the rate and the shape of the fluctuations under $H_0$: $\sqrt n(F_n-F_0)$ converges to the Brownian bridge $B\circ F_0$, and the supremum is a continuous functional, so $\sqrt nD_n$ converges to $\sup\lvert B\rvert$, whose Kolmogorov distribution supplies asymptotic critical values and $p$-values.

4. Someone tests normality with `ks.test(x, "pnorm", mean = mean(x), sd = sd(x))` and obtains $p=0.22$. Does this support normality?

   **Answer** No. The parameters were estimated from the same data, which pulls the fitted distribution toward $F_n$ and makes $D_n$ smaller than the ordinary null distribution assumes; the $p$-value is far too large. The Lilliefors test, with the correct null distribution, gives $p=0.006$ for the same data (Example 6.4.1). In addition, a nonsignificant result from a test of modest power would not establish normality in any case; a Q–Q plot is needed.

5. In Example 6.5.2, how many degrees of freedom would the test have if the mean number of accidents were known to be $0.5$ in advance? And if the cells $\ge3$ had not been merged?

   **Answer** With a known $\lambda$ no parameter is estimated, and the four cells give $4-1=3$ degrees of freedom. Without merging, there would be $7$ cells and, with $\lambda$ estimated, $7-1-1=5$ degrees of freedom; but the expected counts $3.8,0.5,0.06,0.01$ are far too small for the $\chi^2$ approximation (the cell "$\ge6$" alone would contribute about $(5-0.01)^2/0.01\approx2500$), so the merged test is the appropriate one. The conclusion, a decisive rejection, is the same.
