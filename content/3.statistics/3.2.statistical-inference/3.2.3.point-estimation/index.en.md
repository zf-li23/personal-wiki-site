---
title: Point Estimation
description: Criteria for estimators (unbiasedness, efficiency, mean squared error, consistency, asymptotic normality), the method of moments, maximum likelihood, UMVUE theory with the Rao–Blackwell and Lehmann–Scheffé theorems and the Cramér–Rao inequality, estimation in linear regression, kernel density estimation and an outlook on high-dimensional sparse estimation.
---

Point estimation uses a single statistic to estimate an unknown parameter, such as the mean income of a population or the success probability of a Bernoulli trial. Since an estimator is a function of a random sample, its value changes from sample to sample, and the question is not whether one estimate is right but how the estimator behaves over repeated sampling. This chapter first sets up the criteria for comparing estimators (unbiasedness, efficiency, mean squared error, consistency and asymptotic normality), then develops the two general construction methods, the method of moments and maximum likelihood, and finally asks for optimal estimators: the uniformly minimum variance unbiased estimator, found through the **sufficient statistics** and **complete statistics** of [3.2.2](/3.2.2), and the Cramér–Rao lower bound that measures how good an unbiased estimator can be. Two applications close the chapter: estimation in the linear regression model, studied in depth in the course [3.3](/3.3), and kernel density estimation, a first nonparametric method (see [3.6](/3.6)); an optional section sketches estimation when the number of parameters exceeds the sample size. The probabilistic tools are the **law of large numbers**, the **central limit theorem** and the convergence concepts of [3.1.14](/3.1.14). Interval estimation, which attaches a measure of precision to a point estimate, follows in [3.2.4](/3.2.4).

## 3.1. Optimality Criteria for Estimators

### 3.1.1. Point Estimators

**Statistical inference** draws conclusions about a population from a random sample $\boldsymbol{X}=(X_1,\dots,X_n)$. In a parametric problem the population belongs to a **distribution family** $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ with **parameter space** $\Theta$, where $\theta$ may be a $k$-dimensional vector, and the goal is to estimate $\theta$ or a function $g(\theta)$; for a sample from $\mathcal{N}(\mu,\sigma^2)$ we may want $\theta=(\mu,\sigma^2)$ itself or $g(\theta)=\mu/\sigma^2$. Once $\theta$ is replaced by a good estimate, every characteristic of the population (its mean, variance, quantiles) can be estimated as well. In a nonparametric problem the form of the population distribution $F$ is unknown, and we estimate characteristics $g(F)$ such as the population mean or variance of annual income, which are also called parameters. Parameter estimation comes in two forms: point estimation, treated here, and interval estimation ([3.2.4](/3.2.4)).

**Definition 3.1.1 (Point Estimator)** A statistic $\hat g(\boldsymbol{X})=\hat g(X_1,\dots,X_n)$ used to estimate an unknown parameter $g(\theta)$ is called a **point estimator** (or simply an estimator) of $g(\theta)$. Its observed value $\hat g(\boldsymbol{x})$ for a realized sample $\boldsymbol{x}=(x_1,\dots,x_n)$ is called an **estimate** of $g(\theta)$.

Estimators of $\theta$ are written $\hat\theta(\boldsymbol{X})$ or simply $\hat\theta$. The typical estimators of the population mean $\mu$ and variance $\sigma^2$ are the **sample mean** and the **sample variance**,

$$
\bar X=\frac1n\sum_{i=1}^nX_i,\qquad S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2,
$$

and the corresponding estimates are $\bar x$ and $s^2$. Because an estimator is a function of the random sample, it is itself a random variable, and its behavior is described by its **sampling distribution** ([3.2.2](/3.2.2)). For one parameter there are usually many candidate estimators: the population mean $\mu$ can be estimated by the sample mean, the sample median, the sample mode, or even by a constant such as $10$. To select a reasonable one we impose properties: unbiasedness, efficiency, small mean squared error, consistency and asymptotic normality.

### 3.1.2. Unbiasedness

An estimator should be close to the parameter on average, that is, $\mathbb{E}(\hat\theta-\theta)$ should be as small as possible, ideally zero for every value of the parameter.

**Definition 3.1.2 (Unbiased Estimator)** Let $\boldsymbol{X}=(X_1,\dots,X_n)$ be a random sample from $\{f(x;\theta)\colon\theta\in\Theta\}$ and let $g(\theta)$ be a function on $\Theta$. An estimator $\hat g(\boldsymbol{X})$ of $g(\theta)$ is called an **unbiased estimator** if

$$
\mathbb{E}_\theta[\hat g(\boldsymbol{X})]=g(\theta)\qquad\text{for all }\theta\in\Theta;
$$
otherwise it is **biased**, and $\operatorname{Bias}_\theta(\hat g)=\mathbb{E}_\theta[\hat g(\boldsymbol{X})]-g(\theta)$ is its **bias**. A sequence of estimators $\hat g_n(\boldsymbol{X})$, one for each sample size $n$, is called **asymptotically unbiased** if $\lim_{n\to\infty}\mathbb{E}_\theta[\hat g_n(\boldsymbol{X})]=g(\theta)$ for all $\theta\in\Theta$.

Unbiasedness has two interpretations.

- *No systematic error.* The value of $\hat g(\boldsymbol{X})$ is larger than $g(\theta)$ for some samples and smaller for others; unbiasedness means that over- and underestimates balance, so the estimator is right on average.
- *Repeated use.* Suppose a store buys $N$ products every day from a factory whose long-run rate of scrap is $p_0$, at price $a$ each, and agrees to pay $N(1-\hat p)a$, where $\hat p$ is the scrap rate estimated from that day's sample. Each day $\hat p$ may be above or below $p_0$, but if $\hat p$ is unbiased the arrangement is fair to both sides in the long run: by the strong **law of large numbers**, the average of the estimates over $m$ days, $\frac1m\sum_{i=1}^m\hat g(\boldsymbol{X}^{(i)})$, converges to $g(\theta)$ almost surely as $m\to\infty$.

Unbiasedness involves only the first moment, which makes it mathematically simple, and in the absence of other criteria an unbiased estimator seems preferable to a biased one. It is, however, not invariant under nonlinear transformations: if $\hat\theta$ is unbiased for $\theta$, then $g(\hat\theta)$ is in general biased for $g(\theta)$.

**Theorem 3.1.1** Let $X_1,\dots,X_n$ be a random sample from a population with mean $\mu$ and variance $\sigma^2$. Then $\bar X$ and $S^2$ are unbiased estimators of $\mu$ and $\sigma^2$, respectively.

**Proof** $\mathbb{E}\bar X=\frac1n\sum_{i=1}^n\mathbb{E}X_i=\mu$. Since $\sum_{i=1}^n(X_i-\bar X)^2=\sum_{i=1}^nX_i^2-n\bar X^2$, $\mathbb{E}X_i^2=\sigma^2+\mu^2$ and $\mathbb{E}\bar X^2=\operatorname{Var}(\bar X)+\mu^2=\sigma^2/n+\mu^2$,

$$
\mathbb{E}S^2=\frac1{n-1}\left[\sum_{i=1}^n\mathbb{E}X_i^2-n\,\mathbb{E}\bar X^2\right]=\frac n{n-1}\left[(\sigma^2+\mu^2)-\left(\frac{\sigma^2}n+\mu^2\right)\right]=\sigma^2.\qquad\square
$$

This is why the sample variance divides by $n-1$ rather than $n$: the estimator $S_n^2=\frac1n\sum_{i=1}^n(X_i-\bar X)^2=\frac{n-1}nS^2$ has $\mathbb{E}S_n^2=\frac{n-1}n\sigma^2$, so it is biased but asymptotically unbiased.

### 3.1.3. Efficiency

Unbiased estimators are not unique: for the population mean, $\bar X$, $X_1$ and $(X_1+X_n)/2$ are all unbiased. Among unbiased estimators, the one whose sampling distribution is more concentrated around the parameter is better.

**Definition 3.1.3 (Relative Efficiency)** Let $\hat g_1(\boldsymbol{X})$ and $\hat g_2(\boldsymbol{X})$ be two unbiased estimators of $g(\theta)$. If

$$
\operatorname{Var}_\theta[\hat g_1(\boldsymbol{X})]\le\operatorname{Var}_\theta[\hat g_2(\boldsymbol{X})]\qquad\text{for all }\theta\in\Theta,
$$
with strict inequality for at least one $\theta\in\Theta$, then $\hat g_1$ is said to be **more efficient** than $\hat g_2$.

**Example 3.1.1** Let $X_1,\dots,X_n$ be a random sample from a population with mean $\theta$ and variance $\sigma^2$, and let $\hat\theta_1=X_1$, $\hat\theta_2=\bar X$. Both are unbiased, with $\operatorname{Var}(\hat\theta_1)=\sigma^2$ and $\operatorname{Var}(\hat\theta_2)=\sigma^2/n$. Hence $\bar X$ is more efficient than $X_1$ for $n\ge2$, and it becomes more efficient as $n$ grows.

### 3.1.4. Mean Squared Error

The goodness of an estimator can be measured by its distance $|\hat\theta-\theta|$ from the parameter. Averaging this distance gives the mean absolute error $\mathbb{E}|\hat\theta-\theta|$; any increasing function of $|\hat\theta-\theta|$ would serve, and the square is the most convenient.

**Definition 3.1.4 (Mean Squared Error)** The **mean squared error** (MSE) of an estimator $\hat\theta$ of $\theta$ is the function of $\theta$

$$
\operatorname{MSE}_\theta(\hat\theta)=\mathbb{E}_\theta(\hat\theta-\theta)^2.
$$

The MSE is analytically tractable, and it has a transparent interpretation: expanding the square around $\mathbb{E}_\theta\hat\theta$, the cross term vanishes, and

$$
\operatorname{MSE}_\theta(\hat\theta)=\operatorname{Var}_\theta(\hat\theta)+(\mathbb{E}_\theta\hat\theta-\theta)^2=\operatorname{Var}_\theta(\hat\theta)+[\operatorname{Bias}_\theta(\hat\theta)]^2.
$$

The MSE thus combines the variability of the estimator (its precision) and its bias (its accuracy), and an estimator with small MSE has a small combined variance and bias. For an unbiased estimator the MSE equals the variance; looking for the unbiased estimator with smallest variance leads to the uniformly minimum variance unbiased estimators of §3.4. But the decomposition also explains the *bias–variance trade-off*: some estimators accept a small bias in exchange for a large reduction in variance, and then have a smaller MSE than any unbiased estimator. For estimating $g(\theta)$ the criterion reads: $\hat g_1$ is better than $\hat g_2$ in MSE if $\mathbb{E}_\theta[\hat g_1-g(\theta)]^2\le\mathbb{E}_\theta[\hat g_2-g(\theta)]^2$ for all $\theta$, with strict inequality for some $\theta$. An estimator $\hat g^*$ that is at least as good as every other estimator for every $\theta$ would be called a uniformly minimum MSE estimator, but it does not exist in general: the constant estimator $\hat g\equiv g(\theta_0)$ has MSE $0$ at $\theta=\theta_0$, so $\hat g^*$ would need MSE zero everywhere.

**Example 3.1.2** Let $X_1,\dots,X_n$ be a random sample from $\mathcal{N}(\mu,\sigma^2)$. By Theorem 3.1.1, $\bar X$ and $S^2$ are unbiased, so their MSEs are their variances:

$$
\mathbb{E}(\bar X-\mu)^2=\operatorname{Var}(\bar X)=\frac{\sigma^2}n,\qquad\mathbb{E}(S^2-\sigma^2)^2=\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1},
$$

the latter because $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$ ([3.2.2](/3.2.2)) has variance $2(n-1)=(n-1)^2\operatorname{Var}(S^2)/\sigma^4$. An alternative estimator of $\sigma^2$ is $\hat\sigma^2=S_n^2=\frac{n-1}nS^2$, which will turn out to be the maximum likelihood estimator. It is biased, $\mathbb{E}\hat\sigma^2=\frac{n-1}n\sigma^2$, with variance $\operatorname{Var}(\hat\sigma^2)=\left(\frac{n-1}n\right)^2\frac{2\sigma^4}{n-1}=\frac{2(n-1)\sigma^4}{n^2}$, so

$$
\mathbb{E}(\hat\sigma^2-\sigma^2)^2=\frac{2(n-1)\sigma^4}{n^2}+\left(\frac{n-1}n\sigma^2-\sigma^2\right)^2=\frac{2n-1}{n^2}\sigma^4<\frac2{n-1}\sigma^4=\mathbb{E}(S^2-\sigma^2)^2.
$$

**Remark 3.1.1** Example 3.1.2 does not mean that $S^2$ should be abandoned. In MSE, $\hat\sigma^2$ is on average closer to $\sigma^2$, but it systematically underestimates $\sigma^2$. No absolute answer is obtained; rather, we learn more about the estimators so that a good one can be chosen for the situation at hand. Since the MSE is a function of the parameter, there is in general no single best estimator: the MSE curves of two estimators often cross, each being better on part of the parameter space.

Bias, variance and MSE all depend on the sample size, and increasing $n$ usually decreases all three. A simulation makes this concrete. Drawing $10\,000$ samples from $\mathcal{N}(0,1)$ for each $n=10,20,\dots,100$, the bias of $S_n^2$ is about $-1/n$ while that of $S^2$ is zero, and the variance and MSE of $S_n^2$ are slightly smaller than those of $S^2$, the differences vanishing as $n$ grows. For a location parameter one can similarly compare the sample mean $\bar X$, the **sample median** $m_{0.5}$ and the trimmed mean $\bar X_\alpha$, which discards the fraction $\alpha$ of the smallest and of the largest observations before averaging. The trimmed mean is less sensitive to outliers than the mean but still estimates the center reasonably for many models; it is a *robust* estimator. Resampling from the heights of $25\,000$ eighteen-year-old Hong Kong children (a nearly symmetric population with mean $68$ in, about $172.7$ cm), the three estimators have negligible bias and the median has the largest variance. Resampling from the sale prices of about $2000$ houses in Ames, Iowa (a right-skewed population with mean about 180 thousand dollars and median about 160 thousand dollars), the median and trimmed means estimate the mean with a clear negative bias, yet a lightly trimmed mean has a smaller MSE than the sample mean: a small bias bought a larger reduction in variance.

### 3.1.5. Consistency

Unbiasedness and efficiency are properties for a fixed sample size. Consistency requires that, as information accumulates, the estimator converges to the parameter.

**Definition 3.1.5 (Consistent Estimator)** For each sample size $n$ let $\hat g_n(\boldsymbol{X})=\hat g_n(X_1,\dots,X_n)$ be an estimator of $g(\theta)$.

1. If $\hat g_n(\boldsymbol{X})\xrightarrow{p}g(\theta)$, that is, $\lim_{n\to\infty}\mathbb{P}_\theta(|\hat g_n(\boldsymbol{X})-g(\theta)|\ge\varepsilon)=0$ for all $\theta\in\Theta$ and all $\varepsilon>0$, then $\hat g_n$ is called a (weakly) **consistent estimator** of $g(\theta)$.
2. If $\mathbb{P}_\theta\left(\lim_{n\to\infty}\hat g_n(\boldsymbol{X})=g(\theta)\right)=1$ for all $\theta\in\Theta$, then $\hat g_n$ is called a **strongly consistent** estimator of $g(\theta)$.
3. If for some $r>0$, $\lim_{n\to\infty}\mathbb{E}_\theta|\hat g_n(\boldsymbol{X})-g(\theta)|^r=0$ for all $\theta\in\Theta$, then $\hat g_n$ is said to be **consistent in $r$-th mean**; for $r=2$, **consistent in quadratic mean**.

These are **convergence in probability**, **almost sure convergence** and convergence in $r$-th mean of [3.1.14](/3.1.14): strong consistency and consistency in $r$-th mean both imply weak consistency. Consistency in quadratic mean is equivalent to $\operatorname{MSE}\to0$, that is, bias and variance both tending to zero, which is often the easiest way to check consistency. By the strong law of large numbers, $\bar X$ is strongly consistent for $\mu$, and more generally the sample moments are strongly consistent for the population moments; by the continuous mapping theorem ([3.1.14](/3.1.14)), continuous functions of strongly consistent estimators are strongly consistent.

**Example 3.1.3** Let $X_1,\dots,X_n$ be a random sample from $\mathrm{U}(0,\theta)$. Then the geometric mean $T(\boldsymbol{X})=\left(\prod_{i=1}^nX_i\right)^{1/n}$ is a strongly consistent estimator of $g(\theta)=\theta\mathrm{e}^{-1}$.

**Proof** Let $Y_i=\log X_i$. Then $Y_1,\dots,Y_n$ are iid with density $f(y;\theta)=\frac1\theta\mathrm{e}^y\boldsymbol{1}_{(-\infty,\log\theta)}(y)$, and integrating by parts,

$$
\mathbb{E}Y_1=\frac1\theta\int_{-\infty}^{\log\theta}y\mathrm{e}^y\,\mathrm{d}y=\frac1\theta\left[y\mathrm{e}^y\Big|_{-\infty}^{\log\theta}-\int_{-\infty}^{\log\theta}\mathrm{e}^y\,\mathrm{d}y\right]=\log\theta-1.
$$

By the strong law of large numbers, $\log T(\boldsymbol{X})=\frac1n\sum_{i=1}^n\log X_i=\bar Y\to\log\theta-1$ almost surely, hence $T(\boldsymbol{X})=\mathrm{e}^{\bar Y}\to\mathrm{e}^{\log\theta-1}=\theta\mathrm{e}^{-1}$ almost surely. $\square$

### 3.1.6. Asymptotic Normality

Consistency says that $\hat g_n-g(\theta)\to0$; asymptotic normality describes the size and shape of the remaining error, which is what large-sample confidence intervals and tests need.

**Definition 3.1.6 (Consistent Asymptotically Normal Estimator)** A sequence of estimators $\hat g_n$ of $g(\theta)$ is called a **consistent asymptotically normal estimator** if there is a function $\sigma^2(\theta)>0$ such that

$$
\sqrt n\,[\hat g_n(\boldsymbol{X})-g(\theta)]\xrightarrow{d}\mathcal{N}(0,\sigma^2(\theta))\qquad\text{for all }\theta\in\Theta;
$$
$\sigma^2(\theta)$ is called the **asymptotic variance** of $\hat g_n$.

Loosely, $\hat g_n\overset{\cdot}{\sim}\mathcal{N}(g(\theta),\sigma^2(\theta)/n)$ for large $n$, and the error is of order $1/\sqrt n$. By the central limit theorem, $\sqrt n(\bar X-\mu)\xrightarrow{d}\mathcal{N}(0,\sigma^2)$ whenever $\sigma^2<\infty$. Between two consistent asymptotically normal estimators of the same parameter, the one with the smaller asymptotic variance is preferred.

## 3.2. The Method of Moments

### 3.2.1. Motivation

**Example 3.2.1** Suppose the talk time of a mobile phone on one battery charge is measured on a random sample of $100$ phones (simulated data), and we want the mean and the variance of the talk time. Let the random variable $X$ denote the population; the targets are $\mu=\mathbb{E}X$ and $\sigma^2=\operatorname{Var}(X)=\mathbb{E}(X-\mathbb{E}X)^2$. Without assuming any statistical model we can estimate them by the corresponding sample quantities,

$$
\hat\mu=\bar X=\frac1n\sum_{i=1}^nX_i\colon\ \bar x=24.5,\qquad\hat\sigma^2=S_n^2=\frac1n\sum_{i=1}^n(X_i-\bar X)^2\colon\ s_n^2=0.15.
$$

Inference beyond the point estimate (a confidence interval, say) then requires resampling methods such as the bootstrap. If the population can be approximated by $\mathcal{N}(\mu,\sigma^2)$, then still $\mathbb{E}X=\mu$ and $\operatorname{Var}(X)=\sigma^2$, the same estimators are used, and inference can draw on normal theory or the central limit theorem.

**Example 3.2.2** For $n=500$ eighteen-year-old children let $(X,Y)$ be weight (lb) and height (in), with $\mu_1=\mathbb{E}X$, $\mu_2=\mathbb{E}Y$, $\sigma_1^2=\operatorname{Var}(X)$, $\sigma_2^2=\operatorname{Var}(Y)$ and correlation $\rho=\operatorname{Corr}(X,Y)$. The corresponding sample quantities give, without any model,

$$
\hat\mu_1=\bar X=126.7,\quad\hat\mu_2=\bar Y=67.9,\quad\hat\sigma_1^2=S_{nX}^2=143.3,\quad\hat\sigma_2^2=S_{nY}^2=3.9,\quad\hat\rho=\frac{S_{nXY}}{S_{nX}S_{nY}}=\frac{\frac1n\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y)}{S_{nX}S_{nY}}=0.48,
$$

that is, a mean weight of $57.5$ kg and a mean height of $172.5$ cm. The same estimators arise if $(X,Y)$ is assumed bivariate normal; the model then also supports confidence intervals.

### 3.2.2. Definition and Examples

The idea, due to K. Pearson (1894), is to express the parameter through population moments and replace them by sample moments. For a population $X$ the $k$-th origin moment and the $k$-th central moment are $\alpha_k=\mathbb{E}X^k$ and $\mu_k=\mathbb{E}(X-\mathbb{E}X)^k$; the sample counterparts are the sample origin moments $a_{n,k}=\frac1n\sum_{i=1}^nX_i^k$ ($k=1,2,\dots$) and the sample central moments $m_{n,k}=\frac1n\sum_{i=1}^n(X_i-\bar X)^k$ ($k=2,3,\dots$) of [3.2.1](/3.2.1).

**Definition 3.2.1 (Method of Moments)** Let $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ be a distribution family, and let $g(\theta)$ be a function of the parameter that can be written as a function of population moments,

$$
g(\theta)=G(\alpha_1,\dots,\alpha_k;\mu_2,\dots,\mu_s).
$$
For a random sample $\boldsymbol{X}=(X_1,\dots,X_n)$, replacing the population moments by the sample moments gives

$$
\hat g(\boldsymbol{X})=G(a_{n,1},\dots,a_{n,k};m_{n,2},\dots,m_{n,s}),
$$
which is called the **moment estimator** of $g(\theta)$. This way of constructing estimators is the **method of moments**.

For instance, the coefficient of variation $\nu=\sigma/\mu$ and the skewness $\beta_1=\mu_3/\mu_2^{3/2}$ have the moment estimators

$$
\hat\nu=\frac S{\bar X}\ \ (\text{or }S_n/\bar X),\qquad\hat\beta_1=\frac{m_{n,3}}{m_{n,2}^{3/2}}=\frac{\sqrt n\sum_{i=1}^n(X_i-\bar X)^3}{\left[\sum_{i=1}^n(X_i-\bar X)^2\right]^{3/2}}.
$$

In many cases the moment estimator does not require the form of the density, that is, no statistical model is needed, only the existence of the moments involved. For a parametric family with $\boldsymbol{\theta}=(\theta_1,\dots,\theta_r)$, one writes $\mathbb{E}_{\boldsymbol{\theta}}X^k=m_k(\theta_1,\dots,\theta_r)$ for $k=1,\dots,r$ and solves the system

$$
\frac1n\sum_{i=1}^nX_i^k=m_k(\theta_1,\dots,\theta_r),\qquad k=1,\dots,r,
$$

for $\boldsymbol{\theta}$; this system may have no closed-form solution, in which case it is solved numerically.

**Example 3.2.3** For a random sample from $\mathrm{Ber}(\theta)$, $0<\theta<1$, we have $\mathbb{E}_\theta X_1=\theta$, so $\bar X$ is the moment estimator of $\theta$ and $\bar X(1-\bar X)$ is the moment estimator of $g(\theta)=\theta(1-\theta)$.

**Example 3.2.4** For a random sample from $\mathcal{N}(\mu,\sigma^2)$ with both parameters unknown, $\mathbb{E}X_1=\mu$ and $\mathbb{E}X_1^2=\sigma^2+\mu^2$. Solving $\bar X=\mu$ and $\frac1n\sum X_i^2=\sigma^2+\mu^2$ gives

$$
\tilde\mu=\bar X,\qquad\tilde\sigma^2=\frac1n\sum_{i=1}^nX_i^2-\bar X^2=\frac1n\sum_{i=1}^n(X_i-\bar X)^2=S_n^2.
$$

**Example 3.2.5** For a random sample from $\mathrm{U}(\alpha,\beta)$ with both endpoints unknown, $\mathbb{E}X_1=\frac{\alpha+\beta}2$ and $\operatorname{Var}(X_1)=\frac{(\beta-\alpha)^2}{12}$. Solving $\bar X=\frac{\alpha+\beta}2$ and $S_n^2=\frac{(\beta-\alpha)^2}{12}$ gives

$$
\hat\alpha=\bar X-\sqrt3\,S_n,\qquad\hat\beta=\bar X+\sqrt3\,S_n.
$$

Note that $\hat\alpha$ may exceed the smallest observation, so the moment estimator can be incompatible with the data; the maximum likelihood estimator of Example 3.3.10 does not have this defect.

**Example 3.2.6** For a random sample $(X_i,Y_i)$, $i=1,\dots,n$, from a two-dimensional population, the moment estimator of the covariance $\sigma_{12}=\mathbb{E}[(X-\mathbb{E}X)(Y-\mathbb{E}Y)]$ is the **sample covariance** $m_{12}=\frac1n\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y)$, and that of the correlation $\rho=\sigma_{12}/(\sigma_1\sigma_2)$ is the sample correlation coefficient

$$
r=\frac{\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y)}{\sqrt{\sum_{i=1}^n(X_i-\bar X)^2\sum_{i=1}^n(Y_i-\bar Y)^2}}.
$$

**Example 3.2.7 (Non-Uniqueness)** A moment estimator need not be unique. For $\mathrm{Exp}(\theta)$ with density $\theta\mathrm{e}^{-\theta x}$, $x>0$, both $\mathbb{E}X=\theta^{-1}$ and $\operatorname{Var}(X)=\theta^{-2}$ determine $\theta$, giving the moment estimators

$$
\hat\theta_1=\bar X^{-1},\qquad\hat\theta_2=S_n^{-1}.
$$

A simulation with $\theta=2$ and $10\,000$ replications for $n=10,30,50,\dots$ shows that $\hat\theta_1$ has smaller bias, variance and MSE than $\hat\theta_2$ for every $n$. The general lesson is to use low-order moments, which are estimated more precisely; we shall see in Example 3.3.4 that $\hat\theta_1$ is also the maximum likelihood estimator.

### 3.2.3. Properties

1. *Unbiasedness.* The sample origin moments are unbiased, $\mathbb{E}a_{n,k}=\alpha_k$; the sample central moments are in general biased (for instance $\mathbb{E}m_{n,2}=\frac{n-1}n\mu_2$); and a moment estimator $\hat g(\boldsymbol{X})=G(a_{n,1},\dots;m_{n,2},\dots)$ is in general biased for $g(\theta)$. Many moment estimators are asymptotically unbiased.
2. *Consistency.* By the strong law of large numbers, the sample origin and central moments are strongly consistent. If $G$ is continuous, the moment estimator $\hat g(\boldsymbol{X})$ is strongly consistent for $g(\theta)=G(\alpha_1,\dots,\alpha_k;\mu_2,\dots,\mu_s)$.
3. *Asymptotic normality.* Under regularity conditions (finite moments of order $2\max(k,s)$ and $G$ differentiable), $\hat g(\boldsymbol{X})$ is a consistent asymptotically normal estimator; this follows from the multivariate central limit theorem and the delta method ([3.1.14](/3.1.14)). For example, $\sqrt n(\bar X-\mu)\xrightarrow{d}\mathcal{N}(0,\sigma^2)$ and $\sqrt n(S_n^2-\sigma^2)\xrightarrow{d}\mathcal{N}(0,\mu_4-\sigma^4)$.

## 3.3. Maximum Likelihood Estimation

### 3.3.1. The Likelihood Function

For a distribution family $\mathcal{F}=\{f(\boldsymbol{x};\theta)\colon\theta\in\Theta\}$ (with $\theta$ possibly a vector), the joint density of the sample is also written $f_\theta(\boldsymbol{x})$ or $f(\boldsymbol{x}\mid\theta)$. Regarded as a function of $\theta$ for the observed $\boldsymbol{x}$, it is the likelihood $L(\theta;\boldsymbol{x})=f(\boldsymbol{x};\theta)$, also written $L(\theta\mid\boldsymbol{x})$ or $L(\theta,\boldsymbol{x})$; its logarithm $l(\theta;\boldsymbol{x})=\log L(\theta;\boldsymbol{x})$ is the log-likelihood.

**Example 3.3.1** Let $X_1,\dots,X_{10}$ be a random sample from $\mathrm{Ber}(\theta)$, $0<\theta<1$, with observed values $x_1,\dots,x_{10}$ and $t=x_1+\cdots+x_{10}$. Suppose six of the ten trials are successes, so $t=6$. The probability of observing exactly these outcomes is

$$
L(\theta;\boldsymbol{x})=\theta^6(1-\theta)^4,\qquad0<\theta<1,
$$

a function of the unknown $\theta$. For $\theta=0.1,0.2,\dots,0.9$:

| $\theta$ | $0.1$ | $0.2$ | $0.3$ | $0.4$ | $0.5$ | $0.6$ | $0.7$ | $0.8$ | $0.9$ |
|---|---|---|---|---|---|---|---|---|---|
| $L(\theta;\boldsymbol{x})\times10^{4}$ | $0.0066$ | $0.262$ | $1.75$ | $5.31$ | $9.77$ | $11.94$ | $9.53$ | $4.19$ | $0.53$ |

If these nine values were the only possible values of $\theta$, one would choose $\theta=0.6$, the value that makes the observed six successes most probable. Observe that $0.6=6/10=t/n$; in fact $t/n$ maximizes the likelihood over all $0<\theta<1$ (Example 3.3.2), and $\hat\theta=t/n$ is the maximum likelihood estimate.

![Left: the likelihood of Example 3.3.1 for t = 6 successes in n = 10 trials, maximized at t/n = 0.6, and the same for n = 100 with t = 60, both rescaled to maximum 1; the larger sample gives a sharper peak. Right: the likelihood of the capture–recapture model of Example 3.3.12, maximized at N = 49 and N = 50.](./plots/likelihood-functions.py)

**Definition 3.3.1 (Likelihood Function)** Let $\boldsymbol{X}=(X_1,\dots,X_n)$ be a random sample from $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$, where $f(x;\theta)$ is a density (or probability mass function), and let $\boldsymbol{x}=(x_1,\dots,x_n)$ be the observed values. The **likelihood function** is

$$
L(\theta;\boldsymbol{x})=\prod_{i=1}^nf(x_i;\theta),\qquad\theta\in\Theta,
$$
and $l(\theta;\boldsymbol{x})=\log L(\theta;\boldsymbol{x})=\sum_{i=1}^n\log f(x_i;\theta)$ is the **log-likelihood function**.

**Definition 3.3.2 (Maximum Likelihood Estimation)** In the setting of Definition 3.3.1, let $\hat\theta=\hat\theta(\boldsymbol{X})$ be a statistic satisfying

$$
L(\hat\theta(\boldsymbol{x});\boldsymbol{x})=\sup_{\theta\in\Theta}L(\theta;\boldsymbol{x})\qquad\text{for all }\boldsymbol{x}\in\mathcal{X},
$$
or equivalently $l(\hat\theta(\boldsymbol{x});\boldsymbol{x})=\sup_{\theta\in\Theta}l(\theta;\boldsymbol{x})$, where $\mathcal{X}$ is the sample space. Then $\hat\theta(\boldsymbol{X})$ is called a **maximum likelihood estimator** (MLE) of $\theta$ and $\hat\theta(\boldsymbol{x})$ a maximum likelihood estimate of $\theta$. Estimating parameters in this way is called **maximum likelihood estimation**.

The definition covers discrete and continuous families alike, and it does not require an iid sample: for any model with joint density $f(\boldsymbol{x};\theta)$ we maximize $L(\theta;\boldsymbol{x})=f(\boldsymbol{x};\theta)$. The maximum likelihood principle is to choose the parameter value under which the observed data are most probable. Once the likelihood is written down, finding the MLE is a purely mathematical problem, solved in one of three ways:

- *by differentiation*: a stationary point of $l(\theta;\boldsymbol{x})$ with negative second derivative is a local maximum, and one must check that it is the global maximum;
- *by direct inspection* of the likelihood, when it is not differentiable in $\theta$ (for instance when the support depends on $\theta$);
- *numerically*, by maximizing $L(\theta;\boldsymbol{x})$ on a computer.

### 3.3.2. Computing the MLE by Differentiation

When $l(\theta;\boldsymbol{x})$ is differentiable and the maximum lies in the interior of $\Theta$, the MLE solves the *likelihood equation*

$$
\frac{\partial l(\theta;\boldsymbol{x})}{\partial\theta_i}=0,\qquad i=1,\dots,k.
$$

For one parameter, a solution $\theta_0$ with $l''(\theta_0)<0$ is a local maximum. For $k$ parameters, a solution $\boldsymbol{\theta}_0$ is a local maximum if the **Hessian matrix** $\left(\frac{\partial^2l}{\partial\theta_i\partial\theta_j}\right)$ at $\boldsymbol{\theta}_0$ is a **negative definite matrix**, that is, $\boldsymbol{\lambda}^{\mathsf T}\left(\frac{\partial^2l}{\partial\theta_i\partial\theta_j}\Big|_{\boldsymbol{\theta}_0}\right)\boldsymbol{\lambda}<0$ for every nonzero $\boldsymbol{\lambda}\in\mathbb{R}^k$ ([2.2](/2.2)).

**Example 3.3.2** Let $X_1,\dots,X_n$ be a random sample from $\mathrm{Ber}(\theta)$, $\theta\in(0,1)$. Since $f(x_i;\theta)=\theta^{x_i}(1-\theta)^{1-x_i}$ with $x_i\in\{0,1\}$,

$$
L(\theta;\boldsymbol{x})=\theta^t(1-\theta)^{n-t},\qquad l(\theta;\boldsymbol{x})=t\log\theta+(n-t)\log(1-\theta),\qquad t=x_1+\cdots+x_n.
$$

The likelihood equation $\frac{t}{\theta}-\frac{n-t}{1-\theta}=0$ gives $\theta=t/n$, and $l''(\theta)=-\frac t{\theta^2}-\frac{n-t}{(1-\theta)^2}<0$ for all $\theta$. Hence $\hat\theta=t/n=\bar x$ for $0<t<n$; for $t=0$ or $t=n$ the likelihood is monotone and the supremum is approached at the boundary, consistent with $\hat\theta=\bar x$ if $\Theta$ is taken as $[0,1]$.

**Example 3.3.3** For a random sample from $\mathrm{Poi}(\theta)$, $\theta\in(0,\infty)$, $f(x_i;\theta)=\mathrm{e}^{-\theta}\theta^{x_i}/x_i!$ and

$$
l(\theta;\boldsymbol{x})=-n\theta+(n\bar x)\log\theta-\log\prod_{i=1}^nx_i!.
$$

Then $l'(\theta)=-n+n\bar x/\theta=0$ gives $\theta=\bar x$, and $l''(\theta)=-n\bar x/\theta^2<0$, so $\hat\theta=\bar x$.

**Example 3.3.4** For a random sample from $\mathrm{Exp}(\theta)$ with density $f(x;\theta)=\theta\mathrm{e}^{-\theta x}$, $x>0$, we have $l(\theta;\boldsymbol{x})=n\log\theta-n\bar x\theta$, $l'(\theta)=n/\theta-n\bar x=0$ and $l''(\theta)=-n/\theta^2<0$, so $\hat\theta=1/\bar x$.

**Example 3.3.5** Let $X_1,\dots,X_n$ be a random sample from $\mathcal{N}(\mu,\sigma^2)$.

1. *$\mu$ unknown, $\sigma^2$ known.* From $l(\mu)=-n\log(\sqrt{2\pi}\sigma)-\frac1{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2$ we get $l'(\mu)=n(\bar x-\mu)/\sigma^2=0$ and $l''(\mu)=-n/\sigma^2<0$, so $\hat\mu=\bar x$.
2. *$\sigma^2$ unknown, $\mu$ known.* From $l(\sigma^2)=-\frac n2\log(2\pi)-\frac n2\log\sigma^2-\frac1{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2$,

   $$
   \frac{\partial l}{\partial\sigma^2}=-\frac n{2\sigma^2}+\frac1{2\sigma^4}\sum_{i=1}^n(x_i-\mu)^2=0\quad\Longrightarrow\quad\sigma^2=\frac1n\sum_{i=1}^n(x_i-\mu)^2=:s_\mu^2,
   $$
   and $\frac{\partial^2l}{\partial(\sigma^2)^2}\Big|_{\sigma^2=s_\mu^2}=\frac n{2s_\mu^4}-\frac{2ns_\mu^2}{2s_\mu^6}=-\frac n{2s_\mu^4}<0$. Hence $\hat\sigma^2=\frac1n\sum_{i=1}^n(x_i-\mu)^2$, which is unbiased.
3. *Both unknown.* The two likelihood equations have the unique solution $\mu=\bar x$, $\sigma^2=\frac1n\sum_{i=1}^n(x_i-\bar x)^2=s_n^2$, where the Hessian is $\operatorname{diag}\left(-\frac n{s_n^2},-\frac n{2s_n^4}\right)$, which is negative definite. Hence $\hat\mu=\bar x$ and $\hat\sigma^2=s_n^2$, the latter now biased (Example 3.1.2).

**Example 3.3.6** A multinomial experiment with $r$ outcomes is carried out independently $n$ times. With counts $x_1,\dots,x_r\ge0$, $x_1+\cdots+x_r=n$, the likelihood is

$$
L(p_1,\dots,p_r;\boldsymbol{x})=\frac{n!}{x_1!\cdots x_r!}p_1^{x_1}\cdots p_r^{x_r},\qquad0<p_i<1,\quad p_1+\cdots+p_r=1.
$$

There are $r-1$ free parameters, since $p_r=1-p_1-\cdots-p_{r-1}$. Differentiating $\log L$ with respect to $p_i$, $i=1,\dots,r-1$, gives $\frac{x_i}{p_i}-\frac{x_r}{p_r}=0$, whose unique solution is $p_i=x_i/n$, $i=1,\dots,r$. The $(r-1)\times(r-1)$ Hessian at this point has entries $-\frac{n^2}{x_i}\delta_{ij}-\frac{n^2}{x_r}$, the negative of a sum of a positive diagonal matrix and a positive multiple of the all-ones matrix, so it is negative definite. Hence $\hat p_i=x_i/n$.

**Example 3.3.7 (Hardy–Weinberg Equilibrium)** A gene occurs as one of two alleles $A$ and $a$, with $A$ having frequency $\theta$ in the population. A diploid genotype consists of two genes, so under random mating the genotypes have probabilities

| genotype | $AA$ | $Aa$ | $aa$ |
|---|---|---|---|
| probability | $\theta^2$ | $2\theta(1-\theta)$ | $(1-\theta)^2$ |

In a random sample of people, $k_1=13$ are $AA$, $k_2=24$ are $Aa$ and $k_3=19$ are $aa$. The likelihood is

$$
\mathbb{P}(k_1,k_2,k_3\mid\theta)=\binom{k_1+k_2+k_3}{k_1}\binom{k_2+k_3}{k_2}\theta^{2k_1}[2\theta(1-\theta)]^{k_2}(1-\theta)^{2k_3},
$$

so $l(\theta)=\text{const}+(2k_1+k_2)\log\theta+(k_2+2k_3)\log(1-\theta)$. Setting $\frac{2k_1+k_2}\theta-\frac{k_2+2k_3}{1-\theta}=0$ gives

$$
\hat\theta=\frac{2k_1+k_2}{2(k_1+k_2+k_3)}=\frac{50}{112}\approx0.446,
$$

the fraction of $A$ alleles among all the genes in the sample.

### 3.3.3. Computing the MLE from the Definition

**Example 3.3.8** For a single observation $X\sim\mathrm{U}(0,\theta)$, $\theta>0$, the likelihood is $L(\theta;x)=\theta^{-1}\boldsymbol{1}_{[x,\infty)}(\theta)$: it is $0$ for $\theta<x$ and $1/\theta$ for $\theta\ge x$, jumping up at $\theta=x$ and decreasing afterwards. The likelihood equation has no solution; the maximum is attained at the jump, $\hat\theta=x$.

**Example 3.3.9** Let $X_1,\dots,X_n$ be a random sample from $\mathrm{U}(\alpha,\beta)$, $\alpha<\beta$, where only one endpoint is unknown. Since $f(x_i)=\frac1{\beta-\alpha}\boldsymbol{1}_{[\alpha,\beta]}(x_i)$,

$$
L(\alpha,\beta;\boldsymbol{x})=\frac1{(\beta-\alpha)^n}\boldsymbol{1}_{[\alpha,\infty)}(x_{(1)})\,\boldsymbol{1}_{(-\infty,\beta]}(x_{(n)}),
$$

where $x_{(1)}=\min_ix_i$ and $x_{(n)}=\max_ix_i$ are the extreme **order statistics**. If $\alpha$ is unknown, maximizing $L$ means making the indicator equal to $1$, which requires $\alpha\le x_{(1)}$, and making $(\beta-\alpha)^{-n}$ as large as possible, which requires $\alpha$ as close to $\beta$ as possible; hence $\hat\alpha=x_{(1)}$. If $\beta$ is unknown, the same argument gives $\hat\beta=x_{(n)}$.

**Example 3.3.10** If both $\alpha$ and $\beta$ are unknown, $L(\alpha,\beta;\boldsymbol{x})$ is maximized when $\alpha\le x_{(1)}$, $x_{(n)}\le\beta$ and $\beta-\alpha$ is as small as possible, that is, $\hat\alpha=x_{(1)}$ and $\hat\beta=x_{(n)}$.

The MLE need not be unique, and it need not have a closed form; in the latter case $L(\theta;\boldsymbol{x})$ is maximized numerically, with care to find the global rather than a local maximum.

**Example 3.3.11 (Non-Uniqueness)** Let $X_1,\dots,X_n$ be a random sample from $\mathrm{U}(\theta,\theta+1)$, $\theta\in\mathbb{R}$. The likelihood equals $1$ if $\theta\le x_{(1)}$ and $x_{(n)}\le\theta+1$, and $0$ otherwise, that is, $L(\theta;\boldsymbol{x})=\boldsymbol{1}\{x_{(n)}-1\le\theta\le x_{(1)}\}$. Every point of the interval $[x_{(n)}-1,x_{(1)}]$ maximizes it, so for every $0\le\lambda\le1$,

$$
\hat\theta_\lambda=\lambda X_{(1)}+(1-\lambda)(X_{(n)}-1)
$$

is an MLE of $\theta$; the choice among them must be made on other grounds (by symmetry, $\lambda=\frac12$ is natural).

**Example 3.3.12 (Capture–Recapture)** To estimate the size $N$ of a wild animal population, $10$ animals are captured, tagged and released. A few months later $20$ animals are captured, of which $4$ are found to be tagged. Assuming every animal is equally likely to be captured, the intuitive estimate solves $10/N=4/20$, giving $N=50$. For the MLE, let $X_i=1$ if the $i$-th recaptured animal is tagged and $0$ otherwise, and $t=\sum_{i=1}^{20}x_i=4$. The number of tagged animals among the $20$ is hypergeometric, so

$$
L(N;x_1,\dots,x_{20})=\frac{\binom{N-10}{16}\binom{10}{4}}{\binom N{20}},\qquad N\ge26.
$$

Since $N$ is an integer, we compare consecutive values: $L(N)/L(N-1)=\frac{(N-10)(N-20)}{N(N-26)}\ge1$ if and only if $N\le\frac{10\cdot20}4=50$, with equality at $N=50$. Hence $L$ increases up to $N=49$, $L(49)=L(50)$, and $L$ decreases afterwards: both $\hat N=49$ and $\hat N=50$ are MLEs, the latter agreeing with the intuitive estimate. In general the MLE is $\lfloor Mn/t\rfloor$ for $M$ tagged animals, a recapture of size $n$ and $t$ tagged recaptures, with a tie when $Mn/t$ is an integer.

### 3.3.4. MLE in an Exponential Family

For an **exponential family** in natural form ([3.2.2](/3.2.2)) the likelihood equations can be written down once and for all. Let $\boldsymbol{X}$ be a random sample from

$$
f(x;\boldsymbol{\theta})=C(\boldsymbol{\theta})\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x),\qquad\boldsymbol{\theta}\in\Theta,
$$

where $\Theta$ is the natural parameter space, and let $\Theta_0$ be the set of interior points of $\Theta$. Then

$$
L(\boldsymbol{\theta};\boldsymbol{x})=C^n(\boldsymbol{\theta})\exp\left\{\sum_{i=1}^k\theta_i\sum_{j=1}^nT_i(x_j)\right\}h(\boldsymbol{x}),\qquad l(\boldsymbol{\theta};\boldsymbol{x})=n\log C(\boldsymbol{\theta})+\sum_{i=1}^k\theta_i\sum_{j=1}^nT_i(x_j)+\log h(\boldsymbol{x}),
$$

with $h(\boldsymbol{x})=\prod_{j=1}^nh(x_j)$.

**Theorem 3.3.1** Suppose the representation is of full rank, that is, $T_1(X),\dots,T_k(X)$ satisfy no affine relation with probability one. If for a sample $\boldsymbol{x}$ the likelihood equations

$$
\frac n{C(\boldsymbol{\theta})}\frac{\partial C(\boldsymbol{\theta})}{\partial\theta_i}=-\sum_{j=1}^nT_i(x_j),\qquad i=1,\dots,k,
$$

have a solution in $\Theta_0$, then the solution is unique and it is the MLE of $\boldsymbol{\theta}$.

**Proof** By Corollary 2.2.1, with $D=\log C$, the left side equals $n\,\partial D/\partial\theta_i=-n\,\mathbb{E}_{\boldsymbol{\theta}}T_i(X)$, so the equations say $\mathbb{E}_{\boldsymbol{\theta}}T_i(X)=\frac1n\sum_jT_i(x_j)$: the population means of the sufficient statistics are matched to the sample means. Moreover the Hessian of $l$ is $n\,\partial^2D/\partial\theta_i\partial\theta_j=-n\operatorname{Cov}_{\boldsymbol{\theta}}(T_i(X),T_j(X))$, which is negative definite under the full-rank assumption. Hence $l$ is strictly concave on the convex set $\Theta$, a stationary point in $\Theta_0$ is the unique global maximum, and there is at most one. $\square$

In an exponential family there is therefore no need to examine second derivatives. For example, for two independent samples $X_1,\dots,X_m\overset{\text{iid}}{\sim}\mathcal{N}(\mu_1,\sigma^2)$ and $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu_2,\sigma^2)$ with a common variance, the joint density is a three-parameter exponential family with sufficient and complete statistic $\left(\sum X_i,\sum Y_j,\sum X_i^2+\sum Y_j^2\right)$, and the likelihood equations give

$$
\hat\mu_1=\bar X,\qquad\hat\mu_2=\bar Y,\qquad\hat\sigma^2=\frac1{m+n}\left[\sum_{i=1}^m(X_i-\bar X)^2+\sum_{j=1}^n(Y_j-\bar Y)^2\right].
$$

### 3.3.5. Unbiasedness and Invariance

Whether the MLE is unbiased depends on the problem. In Example 3.3.5 the MLE of $\sigma^2$ is unbiased when $\mu$ is known and biased when $\mu$ is unknown.

**Example 3.3.13** Let $X_1,\dots,X_n$ be a random sample from $\mathrm{U}(0,\beta)$. The MLE $\hat\beta=X_{(n)}$ (Example 3.3.9) has density $\frac{nx^{n-1}}{\beta^n}\boldsymbol{1}_{[0,\beta]}(x)$, so

$$
\mathbb{E}X_{(n)}=\int_0^\beta x\frac{nx^{n-1}}{\beta^n}\,\mathrm{d}x=\frac n{n+1}\beta,
$$

and $\hat\beta$ is biased; the bias-corrected $\hat\beta^*=\frac{n+1}nX_{(n)}$ is unbiased. The moment estimator $\hat\beta_1=2\bar X$ is unbiased as well, and

$$
\operatorname{Var}(\hat\beta^*)=\frac{\beta^2}{n(n+2)},\qquad\operatorname{Var}(\hat\beta_1)=\frac{4}{n}\cdot\frac{\beta^2}{12}=\frac{\beta^2}{3n},
$$

so $\hat\beta^*$ is more efficient than $\hat\beta_1$ for $n\ge2$; its variance decreases at the rate $n^{-2}$ instead of $n^{-1}$. The MLE itself is weakly consistent: for $0<\varepsilon<\beta$,

$$
\mathbb{P}(|\hat\beta-\beta|<\varepsilon)=\mathbb{P}(\beta-\varepsilon<X_{(n)}\le\beta)=\int_{\beta-\varepsilon}^\beta\frac{nx^{n-1}}{\beta^n}\,\mathrm{d}x=1-\left(1-\frac\varepsilon\beta\right)^n\to1.
$$

![Bias, variance and mean squared error of the moment estimator 2 times the sample mean, the MLE X_(n) and the bias-corrected MLE (n+1)/n X_(n) for U(0, 2), estimated from 5000 simulated samples for each sample size. The MLE is biased downward, but its MSE is far below that of the unbiased moment estimator.](./plots/uniform-estimators.py)

The second property concerns reparametrization. In Example 3.3.3 we may want the probability $\mathbb{P}_\theta(X=0)=\mathrm{e}^{-\theta}$ rather than $\theta$; in Example 3.3.4, where $\mathbb{E}_\theta X=1/\theta$, it may be more natural to estimate the mean $1/\theta$. How is the MLE of $g(\theta)$ determined? If $g$ is not one-to-one, several $\theta$ give the same value $\theta^*=g(\theta)$, and we define the induced likelihood

$$
L^*(\theta^*;\boldsymbol{x})=\sup_{\{\theta\colon g(\theta)=\theta^*\}}L(\theta;\boldsymbol{x}),
$$

calling a maximizer of $L^*$ the MLE of $g(\theta)$.

**Theorem 3.3.2 (Invariance of the MLE)** If $\hat\theta$ is the MLE of $\theta$, then for any function $g(\theta)$, the MLE of $g(\theta)$ is $g(\hat\theta)$.

**Proof** If $g$ is one-to-one from $\Theta$ onto $\Theta^*$, then $L(\theta;\boldsymbol{x})=L(g^{-1}(\theta^*);\boldsymbol{x})=L^*(\theta^*;\boldsymbol{x})$, so $\max_{\theta\in\Theta}L(\theta;\boldsymbol{x})=\max_{\theta^*\in\Theta^*}L^*(\theta^*;\boldsymbol{x})$, and $\hat\theta^*=g(\hat\theta)$ attains it because $L^*(g(\hat\theta);\boldsymbol{x})=L(\hat\theta;\boldsymbol{x})$. In general, let $\hat\theta^*=g(\hat\theta)$. Then $L^*(\hat\theta^*;\boldsymbol{x})=\sup_{\{\theta\colon g(\theta)=g(\hat\theta)\}}L(\theta;\boldsymbol{x})=L(\hat\theta;\boldsymbol{x})$, since $\hat\theta$ belongs to this set and maximizes $L$ overall. For every $\theta^*\in\Theta^*$,

$$
L^*(\theta^*;\boldsymbol{x})=\sup_{\{\theta\colon g(\theta)=\theta^*\}}L(\theta;\boldsymbol{x})\le\max_{\theta\in\Theta}L(\theta;\boldsymbol{x})=L(\hat\theta;\boldsymbol{x})=L^*(\hat\theta^*;\boldsymbol{x}).
$$

Therefore $g(\hat\theta)$ is the MLE of $g(\theta)$. $\square$

The theorem is due to P. W. Zehna (*Annals of Mathematical Statistics* 37, 1966), and the argument does not depend on the dimension of $\theta$. Thus the MLE of $\mathrm{e}^{-\theta}$ in the Poisson model is $\mathrm{e}^{-\bar x}$; the MLE of the mean $1/\theta$ of $\mathrm{Exp}(\theta)$ is $\bar x$; and the MLE of $\sigma$ is $\left[\frac1n\sum(x_i-\mu)^2\right]^{1/2}$ when $\mu$ is known and $\left[\frac1n\sum(x_i-\bar x)^2\right]^{1/2}$ when $\mu$ is unknown. Unbiasedness, by contrast, is not invariant: $S^2$ is unbiased for $\sigma^2$ but $S$ is biased for $\sigma$.

### 3.3.6. Sufficiency, Consistency and Asymptotic Normality

**Theorem 3.3.3** Let $\boldsymbol{X}$ be a random sample from $\{f(x;\theta)\colon\theta\in\Theta\}$ and $T=T(\boldsymbol{X})$ a sufficient statistic for $\theta$. If the MLE of $\theta$ exists, then it can be chosen as a function of $T$; if it is unique, it is a function of $T$.

**Proof** By the factorization theorem (Theorem 2.3.1), $L(\theta;\boldsymbol{x})=g(T(\boldsymbol{x});\theta)h(\boldsymbol{x})$ with $h\ge0$ free of $\theta$. For $\boldsymbol{x}$ with $h(\boldsymbol{x})>0$, maximizing $L(\theta;\boldsymbol{x})$ over $\theta$ is the same as maximizing $g(T(\boldsymbol{x});\theta)$, which depends on $\boldsymbol{x}$ only through $T(\boldsymbol{x})$. $\square$

Example 3.3.11 shows why the qualification is needed: with $\lambda$ chosen depending on the sample beyond $(X_{(1)},X_{(n)})$, a non-unique MLE need not be a function of the sufficient statistic.

Proving the consistency of the MLE in general is not easy. H. Cramér (1946) showed that, under regularity conditions, some root of the likelihood equation is weakly consistent; A. Wald (1949) first proved the strong consistency of the MLE, under rather complicated conditions.

**Theorem 3.3.4** Let $\hat\theta_n=\hat\theta_n(X_1,\dots,X_n)$ be the MLE of $\theta\in\Theta\subseteq\mathbb{R}$ based on a random sample with density $f(\cdot;\theta)$. Under suitable regularity conditions, $\hat\theta_n\xrightarrow{p}\theta$ under $\mathbb{P}_\theta$ as $n\to\infty$.

The idea of the proof: by the weak law of large numbers, $\frac1n[l(\theta';\boldsymbol{X})-l(\theta;\boldsymbol{X})]\xrightarrow{p}\mathbb{E}_\theta\log\frac{f(X;\theta')}{f(X;\theta)}$, which by Jensen's inequality is negative for $\theta'\ne\theta$ when the family is identifiable, so for large $n$ the likelihood at the true value exceeds that at any fixed other value.

The precision of the MLE in large samples is governed by the Fisher information $I(\theta)$ of Definition 3.4.3 below.

**Theorem 3.3.5** In the setting of Theorem 3.3.4 and under suitable regularity conditions, the MLE is asymptotically normal: under $\mathbb{P}_\theta$,

$$
\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}\mathcal{N}(0,\sigma_\theta^2),\qquad\sigma_\theta^2=\frac1{I(\theta)},\qquad I(\theta)=\mathbb{E}_\theta\left[\frac\partial{\partial\theta}\log f(X;\theta)\right]^2,\quad X\sim f(\cdot;\theta).
$$

Loosely, $\hat\theta_n\overset{\cdot}{\sim}\mathcal{N}(\theta,\sigma_\theta^2/n)$ for large $n$, and probabilities involving $\hat\theta_n$ can be approximated accordingly. The idea of the proof is to expand the score $l'(\theta;\boldsymbol{X})$ around the true $\theta$ by **Taylor's formula**, use $l'(\hat\theta_n;\boldsymbol{X})=0$, so that $\sqrt n(\hat\theta_n-\theta)\approx\frac{n^{-1/2}l'(\theta)}{-n^{-1}l''(\theta)}$, and apply the central limit theorem to the numerator (a sum of iid terms with mean $0$ and variance $I(\theta)$) and the weak law of large numbers to the denominator (which tends to $I(\theta)$), together with Slutsky's theorem (Theorem 2.1.4). Combining with the delta method ([3.1.14](/3.1.14)) gives, for differentiable $g$,

$$
\sqrt n[g(\hat\theta_n)-g(\theta)]\xrightarrow{d}\mathcal{N}\left(0,\frac{[g'(\theta)]^2}{I(\theta)}\right).
$$

By the Cramér–Rao inequality of §3.4.5, $[g'(\theta)]^2/(nI(\theta))$ is the smallest variance an unbiased estimator of $g(\theta)$ can have, so the MLE is asymptotically efficient. For Example 3.3.13 the regularity conditions fail (the support depends on $\beta$), and indeed $X_{(n)}$ converges at the faster rate $1/n$.

### 3.3.7. Comparison with the Method of Moments

**Example 3.3.14** For the heights of a sample of $n=500$ Hong Kong children, the moment estimate of the mean height is $\bar x=67.9$ in ($172.5$ cm); assuming $\mathcal{N}(\mu,\sigma^2)$, the MLE is the same. In a test of $5$ light bulbs of one brand, the lifetimes are $2,3,1,3$ and $4$ years. The moment estimate of the mean lifetime is $\bar x=2.6$ years; assuming $\mathrm{Exp}(\theta)$ with $\mathbb{E}X=\theta^{-1}=g(\theta)$, the MLE of $g(\theta)$ is also $\bar x=2.6$ by invariance. Simulating samples from $\mathrm{Exp}(2.6)$, whose mean is $1/2.6\approx0.385$, the empirical variances of the MLE $\bar X$ of the mean for $n=5,50,100,500$ are $0.0307$, $0.00293$, $0.00149$, $0.000301$, close to the exact values $\frac{1}{2.6^2n}=0.0296$, $0.00296$, $0.00148$, $0.000296$.

| | Method of moments | Maximum likelihood |
|---|---|---|
| Model | only moments needed; no distributional form | the form of the density must be known |
| Computation | usually explicit | may need numerical optimization |
| Unbiasedness | origin moments unbiased, otherwise in general biased | depends on the problem |
| Large samples | consistent, asymptotically normal | consistent, asymptotically normal and asymptotically efficient |
| Invariance | not invariant (e.g. Example 3.2.7) | invariant (Theorem 3.3.2) |
| Robustness | often more robust to model error | can be very bad if the model is wrong |

If the statistical model is a good approximation, the MLE is often more efficient than the moment estimator; if it is not, the MLE can be very bad, and the moment estimator is often more robust.

## 3.4. Uniformly Minimum Variance Unbiased Estimation

### 3.4.1. Definition and Existence

Within the class of unbiased estimators, MSE equals variance, so the natural optimality criterion is to have the smallest variance for every value of the parameter.

**Definition 3.4.1 (Uniformly Minimum Variance Unbiased Estimator)** Let $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ be a parametric family and $\boldsymbol{X}=(X_1,\dots,X_n)$ a random sample. An unbiased estimator $U(\boldsymbol{X})$ of $g(\theta)$ is called a **uniformly minimum variance unbiased estimator** (UMVUE) of $g(\theta)$ if for every unbiased estimator $V(\boldsymbol{X})$ of $g(\theta)$,

$$
\operatorname{Var}_\theta(U)\le\operatorname{Var}_\theta(V)\qquad\text{for all }\theta\in\Theta.
$$

An unbiased estimator need not exist. A function $g(\theta)$ that has an unbiased estimator is called *estimable*.

**Example 3.4.1** Let $X\sim\mathrm{Bin}(n,p)$, $0<p<1$. Then $g(p)=1/p$ has no unbiased estimator. Indeed, if $\delta(X)$ were unbiased, then $\sum_{i=0}^n\delta(i)\binom ni p^i(1-p)^{n-i}=\frac1p$ for all $p\in(0,1)$, that is,

$$
\sum_{i=0}^n\delta(i)\binom nip^{i+1}(1-p)^{n-i}-1=0\qquad\text{for all }p\in(0,1).
$$

The left side is a polynomial in $p$ of degree at most $n+1$ which is not identically zero (its value at $p=0$ is $-1$), so it has at most $n+1$ roots, a contradiction.

There are three methods for finding a UMVUE: the zero-unbiased-estimator criterion, the sufficient and complete statistic method (Lehmann–Scheffé), and the Cramér–Rao inequality. All rest on the Rao–Blackwell theorem.

### 3.4.2. The Rao–Blackwell Theorem

**Theorem 3.4.1 (Rao–Blackwell Theorem)** Let $T=T(\boldsymbol{X})$ be a sufficient statistic for $\theta$ and $\hat g(\boldsymbol{X})$ an unbiased estimator of $g(\theta)$. Then $h(T)=\mathbb{E}_\theta[\hat g(\boldsymbol{X})\mid T]$ is an unbiased estimator of $g(\theta)$ and

$$
\operatorname{Var}_\theta(h(T))\le\operatorname{Var}_\theta(\hat g(\boldsymbol{X}))\qquad\text{for all }\theta\in\Theta,
$$

with equality for a given $\theta$ if and only if $\mathbb{P}_\theta(\hat g(\boldsymbol{X})=h(T))=1$.

**Proof** Because $T$ is sufficient, the conditional distribution of $\boldsymbol{X}$ given $T$ does not depend on $\theta$, so $h(T)$ does not depend on $\theta$ and is a statistic. By the law of iterated expectations ([3.1.9](/3.1.9)), $\mathbb{E}_\theta h(T)=\mathbb{E}_\theta\{\mathbb{E}[\hat g\mid T]\}=\mathbb{E}_\theta\hat g=g(\theta)$. Moreover

$$
\operatorname{Var}_\theta(\hat g)=\mathbb{E}_\theta[\hat g-h(T)+h(T)-g(\theta)]^2=\mathbb{E}_\theta[\hat g-h(T)]^2+\operatorname{Var}_\theta(h(T))+2\,\mathbb{E}_\theta\{[\hat g-h(T)][h(T)-g(\theta)]\}.
$$

Conditioning on $T$, the cross term is $2\,\mathbb{E}_\theta\{[h(T)-g(\theta)]\,\mathbb{E}[\hat g-h(T)\mid T]\}=0$. Hence $\operatorname{Var}_\theta(\hat g)=\operatorname{Var}_\theta(h(T))+\mathbb{E}_\theta[\hat g-h(T)]^2\ge\operatorname{Var}_\theta(h(T))$, with equality if and only if $\hat g=h(T)$ with probability one. $\square$

Conditioning an unbiased estimator on a sufficient statistic thus never increases its variance, and strictly improves it unless the estimator is already a function of $T$. Consequently, if a UMVUE exists, it can be taken to be a function of a sufficient statistic.

**Example 3.4.2** Let $X_1,\dots,X_n$ be a random sample from $\mathrm{Ber}(p)$. The estimator $X_1$ is unbiased for $p$, and $T=\sum_{i=1}^nX_i$ is sufficient. For $t\ge1$,

$$
h(t)=\mathbb{E}(X_1\mid T=t)=\frac{\mathbb{P}(X_1=1,\ X_2+\cdots+X_n=t-1)}{\mathbb{P}(T=t)}=\frac{p\binom{n-1}{t-1}p^{t-1}(1-p)^{n-t}}{\binom ntp^t(1-p)^{n-t}}=\frac tn,
$$

and $h(0)=0$. So Rao–Blackwellization turns $X_1$ into $\bar X$, reducing the variance from $p(1-p)$ to $p(1-p)/n$. Is $\bar X$ the UMVUE? The next two subsections answer yes.

### 3.4.3. The Zero-Unbiased-Estimator Criterion

A statistic $l(\boldsymbol{X})$ with $\mathbb{E}_\theta l(\boldsymbol{X})=0$ for all $\theta$ is an unbiased estimator of zero. Adding it to an unbiased estimator keeps unbiasedness, so an unbiased estimator is optimal exactly when it cannot be improved in this way.

**Theorem 3.4.2** Let $\hat g(\boldsymbol{X})$ be an unbiased estimator of $g(\theta)$ with $\operatorname{Var}_\theta(\hat g)<\infty$ for all $\theta\in\Theta$. If for every statistic $l(\boldsymbol{X})$ with $\mathbb{E}_\theta l(\boldsymbol{X})=0$ and $\operatorname{Var}_\theta(l)<\infty$ for all $\theta$,

$$
\operatorname{Cov}_\theta(\hat g,l)=\mathbb{E}_\theta[\hat g(\boldsymbol{X})l(\boldsymbol{X})]=0\qquad\text{for all }\theta\in\Theta,
$$

then $\hat g(\boldsymbol{X})$ is a UMVUE of $g(\theta)$.

**Proof** Let $\hat g_1$ be any unbiased estimator of $g(\theta)$ with finite variance (otherwise there is nothing to prove), and $l=\hat g_1-\hat g$. Then $\mathbb{E}_\theta l=0$, and

$$
\operatorname{Var}_\theta(\hat g_1)=\operatorname{Var}_\theta(\hat g+l)=\operatorname{Var}_\theta(\hat g)+\operatorname{Var}_\theta(l)+2\operatorname{Cov}_\theta(\hat g,l)=\operatorname{Var}_\theta(\hat g)+\operatorname{Var}_\theta(l)\ge\operatorname{Var}_\theta(\hat g).\qquad\square
$$

The condition is also necessary: if $\operatorname{Cov}_{\theta_0}(\hat g,l)\ne0$ for some $l$ and $\theta_0$, then $\hat g-cl$ with $c=\operatorname{Cov}_{\theta_0}(\hat g,l)/\operatorname{Var}_{\theta_0}(l)$ has smaller variance at $\theta_0$. The criterion verifies that a candidate is a UMVUE but does not construct one. Combining it with Rao–Blackwell, it suffices to check functions of a sufficient statistic.

**Corollary 3.4.1** Let $T$ be a sufficient statistic and $h(T)$ an unbiased estimator of $g(\theta)$ with finite variance. If $\operatorname{Cov}_\theta(h(T),\delta(T))=0$ for all $\theta$ and every $\delta(T)$ with $\mathbb{E}_\theta\delta(T)=0$ for all $\theta$, then $h(T)$ is a UMVUE of $g(\theta)$.

**Example 3.4.3** In Example 3.4.2, let $\delta(T)$ satisfy $\mathbb{E}_p\delta(T)=0$ for all $p$, and write $a_i=\delta(i)$. Then $\sum_{i=0}^na_i\binom nip^i(1-p)^{n-i}=0$; dividing by $(1-p)^n$ and setting $\varphi=p/(1-p)\in(0,\infty)$ gives $\sum_{i=0}^na_i\binom ni\varphi^i=0$ for all $\varphi>0$, so all $a_i=0$ and $\delta\equiv0$. Hence $\operatorname{Cov}_p(\bar X,\delta(T))=0$ and $\bar X$ is the UMVUE of $p$.

**Example 3.4.4** Let $X_1,\dots,X_n$ be a random sample from $\mathrm{U}(0,\theta)$. The MLE $T=X_{(n)}$ is sufficient and biased, while $h(T)=\frac{n+1}nT$ is unbiased with variance $\frac{\theta^2}{n(n+2)}$ (Example 3.3.13). If $\mathbb{E}_\theta\delta(T)=\int_0^\theta\delta(t)\frac{nt^{n-1}}{\theta^n}\,\mathrm{d}t=0$ for all $\theta>0$, then $\int_0^\theta\delta(t)t^{n-1}\,\mathrm{d}t=0$ for all $\theta$, and differentiating gives $\delta(\theta)\theta^{n-1}=0$, so $\delta=0$ (almost everywhere). Hence $\frac{n+1}nX_{(n)}$ is the UMVUE of $\theta$, and $\frac{n+1}{2n}X_{(n)}$ is the UMVUE of the mean $\theta/2$, better than the unbiased $\bar X$. Which estimator is optimal thus depends on the model: for a normal population, $\bar X$ is the UMVUE of the mean (Example 3.4.7).

In both examples the zero-unbiased estimators of $T$ were forced to vanish, which is precisely the completeness of $T$ (Definition 2.3.3). This leads to the general method.

### 3.4.4. The Lehmann–Scheffé Theorem

**Theorem 3.4.3 (Lehmann–Scheffé Theorem)** Let $T(\boldsymbol{X})$ be a sufficient and complete statistic for $\theta$. If $\hat g(T)$ is an unbiased estimator of $g(\theta)$, then $\hat g(T)$ is the unique (with probability one) UMVUE of $g(\theta)$. In particular, for any unbiased estimator $U$ of $g(\theta)$, $\mathbb{E}(U\mid T)$ is the UMVUE.

**Proof** *Uniqueness among functions of $T$.* If $\hat g_1(T)$ is another unbiased estimator, then $\delta(T)=\hat g(T)-\hat g_1(T)$ has $\mathbb{E}_\theta\delta(T)=0$ for all $\theta$, and completeness gives $\mathbb{P}_\theta(\delta(T)=0)=1$.

*Optimality.* Let $U$ be any unbiased estimator. By the Rao–Blackwell theorem, $h(T)=\mathbb{E}(U\mid T)$ is unbiased with $\operatorname{Var}_\theta(h(T))\le\operatorname{Var}_\theta(U)$. By uniqueness $\hat g(T)=h(T)$ with probability one, so $\operatorname{Var}_\theta(\hat g(T))\le\operatorname{Var}_\theta(U)$ for all $\theta$. $\square$

The theorem (E. L. Lehmann and H. Scheffé, 1950) holds for multidimensional $\theta$ as well. It gives two recipes: find a function of a sufficient and complete statistic that is unbiased, often by computing $\mathbb{E}_\theta$ of simple functions of $T$ and adjusting; or condition any simple unbiased estimator on $T$. For full-rank exponential families the natural sufficient statistic is complete (Theorem 2.3.2).

**Example 3.4.5** For $\mathrm{Ber}(\theta)$, $T=\sum_{i=1}^nX_i\sim\mathrm{Bin}(n,\theta)$ is sufficient and complete (Example 2.3.7), so $\bar X=T/n$ is the UMVUE of $\theta$. For $g(\theta)=\theta(1-\theta)$: $\mathbb{E}T=n\theta$ and $\mathbb{E}T^2=n\theta(1-\theta)+n^2\theta^2=\mathbb{E}T+n(n-1)\theta^2$, so $\theta^2=\mathbb{E}\left[\frac{T^2-T}{n(n-1)}\right]$ and

$$
\frac Tn-\frac{T^2-T}{n(n-1)}=\frac{T(n-T)}{n(n-1)}
$$

is unbiased for $\theta(1-\theta)$; being a function of $T$, it is the UMVUE. Note that it equals $\frac n{n-1}\bar X(1-\bar X)$, a bias-corrected version of the moment estimator of Example 3.2.3.

**Example 3.4.6** Let $X_1,\dots,X_n$ be a random sample from $\mathrm{Poi}(\theta)$; $T=\sum X_i\sim\mathrm{Poi}(n\theta)$ is sufficient and complete.

1. $\bar X$ is the UMVUE of $\theta$.
2. For $g(\theta)=\theta^r$ ($r$ a positive integer), an unbiased $\delta(T)$ must satisfy $\sum_{t=0}^\infty\delta(t)\frac{(n\theta)^t}{t!}\mathrm{e}^{-n\theta}=\theta^r$, that is,

   $$
   \sum_{t=0}^\infty\delta(t)\frac{n^t\theta^t}{t!}=\theta^r\mathrm{e}^{n\theta}=\sum_{t=r}^\infty\frac{n^{t-r}\theta^t}{(t-r)!}.
   $$
   Comparing coefficients, $\delta(t)=0$ for $t<r$ and $\delta(t)=\frac{n^{t-r}/(t-r)!}{n^t/t!}=\frac{t(t-1)\cdots(t-r+1)}{n^r}$ for $t\ge r$, which is the UMVUE of $\theta^r$.
3. For $g(\theta)=\mathbb{P}_\theta(X_1=x)=\mathrm{e}^{-\theta}\theta^x/x!$, the indicator $U=\boldsymbol{1}\{X_1=x\}$ is unbiased, and since $X_1$ and $X_2+\cdots+X_n\sim\mathrm{Poi}((n-1)\theta)$ are independent,

   $$
   \mathbb{E}(U\mid T=t)=\frac{\mathbb{P}(X_1=x)\,\mathbb{P}(X_2+\cdots+X_n=t-x)}{\mathbb{P}(T=t)}=\binom tx\frac{(n-1)^{t-x}}{n^t}=\binom tx\left(\frac1n\right)^x\left(1-\frac1n\right)^{t-x}
   $$
   for $t\ge x$ (and $0$ for $t<x$) is the UMVUE. Compare the MLE $\mathrm{e}^{-\bar X}\bar X^x/x!$, which is biased.

**Example 3.4.7** Let $X_1,\dots,X_n$ be a random sample from $\mathcal{N}(\mu,\sigma^2)$. Then $T_1=\bar X$ and $T_2=\sum_{i=1}^n(X_i-\bar X)^2$ are independent, $T_1\sim\mathcal{N}(\mu,\sigma^2/n)$, $T_2/\sigma^2\sim\chi^2_{n-1}$, and $(T_1,T_2)$ is sufficient and complete (Example 2.3.10).

1. $\bar X$ is the UMVUE of $\mu$ and $S^2=T_2/(n-1)$ is the UMVUE of $\sigma^2$.
2. For $g=\sigma^r$ with $r>-(n-1)$, using $\mathbb{E}(\chi^2_{n-1})^{r/2}=2^{r/2}\Gamma\left(\frac{n-1+r}2\right)/\Gamma\left(\frac{n-1}2\right)$,

   $$
   \mathbb{E}\left[K_{n-1,r}T_2^{r/2}\right]=\sigma^r,\qquad K_{n-1,r}=\frac{\Gamma\left(\frac{n-1}2\right)}{2^{r/2}\Gamma\left(\frac{n-1+r}2\right)},
   $$
   so $K_{n-1,r}T_2^{r/2}$ is the UMVUE of $\sigma^r$; for $r=1$ this corrects the bias of $S$ as an estimator of $\sigma$.
3. For $g=\mu/\sigma^2$ and $n>3$: $\mathbb{E}(1/T_2)=\frac1{(n-3)\sigma^2}$, so by independence $\mathbb{E}\left[\frac{(n-3)T_1}{T_2}\right]=\frac{\mu}{\sigma^2}$, and $(n-3)\bar X/T_2$ is the UMVUE of $\mu/\sigma^2$.

### 3.4.5. The Cramér–Rao Inequality

The Cramér–Rao inequality (C. R. Rao, 1945; H. Cramér, 1946) gives a lower bound for the variance of unbiased estimators. If an unbiased estimator attains it, that estimator is a UMVUE. The bound may, however, not be attained even by the UMVUE, so the method does not always succeed; its wider importance is that it defines the efficiency of estimators and the Fisher information, central to large-sample theory. Throughout, $\theta$ is one-dimensional unless stated otherwise.

**Definition 3.4.2 (Cramér–Rao Regular Family)** A family $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ is called a **Cramér–Rao regular family** if

1. $\Theta$ is an open interval of $\mathbb{R}$;
2. the support $\{x\colon f(x;\theta)>0\}$ does not depend on $\theta$;
3. $\frac{\partial f(x;\theta)}{\partial\theta}$ exists for all $x$ in the support and all $\theta\in\Theta$;
4. integration and differentiation can be interchanged: $\frac\partial{\partial\theta}\int f(x;\theta)\,\mathrm{d}x=\int\frac{\partial f(x;\theta)}{\partial\theta}\,\mathrm{d}x$;
5. $0<I(\theta)<\infty$ for all $\theta\in\Theta$, where $I(\theta)$ is defined below.

**Definition 3.4.3 (Fisher Information)** For a family satisfying conditions 1–3 of Definition 3.4.2, the **score function** of one observation is $s(x;\theta)=\frac{\partial}{\partial\theta}\log f(x;\theta)$, and

$$
I(\theta)=\mathbb{E}_\theta\left[\frac{\partial\log f(X;\theta)}{\partial\theta}\right]^2
$$
is the **Fisher information** in one observation.

$I(\theta)$ measures how much information one observation carries about $\theta$: the more sharply the density changes with $\theta$, the larger $I(\theta)$. For a random sample, the scores add up, and the information in $(X_1,\dots,X_n)$ is $nI(\theta)$. The Fisher information is also the asymptotic precision of the MLE (Theorem 3.3.5). If moreover $f$ is twice differentiable in $\theta$ and the second derivative can also be taken under the integral sign, then $I(\theta)=-\mathbb{E}_\theta\left[\frac{\partial^2\log f(X;\theta)}{\partial\theta^2}\right]$, which is often easier to compute.

**Theorem 3.4.4 (Cramér–Rao Inequality)** Let $\mathcal{F}$ be a Cramér–Rao regular family, $g(\theta)$ a differentiable function on $\Theta$, and $\hat g(\boldsymbol{X})$ an unbiased estimator of $g(\theta)$ based on a random sample of size $n$ such that $\int\hat g(\boldsymbol{x})f(\boldsymbol{x};\theta)\,\mathrm{d}\boldsymbol{x}$ can be differentiated under the integral sign. Then

$$
\operatorname{Var}_\theta(\hat g(\boldsymbol{X}))\ge\frac{[g'(\theta)]^2}{nI(\theta)}\qquad\text{for all }\theta\in\Theta.
$$

In particular, for an unbiased estimator of $\theta$, $\operatorname{Var}_\theta(\hat\theta)\ge\frac1{nI(\theta)}$.

**Proof** Let $S(\boldsymbol{x};\theta)=\frac\partial{\partial\theta}\log f(\boldsymbol{x};\theta)=\sum_{i=1}^n\frac\partial{\partial\theta}\log f(x_i;\theta)$ be the score of the sample. By conditions 3 and 4,

$$
\mathbb{E}_\theta\left[\frac\partial{\partial\theta}\log f(X_i;\theta)\right]=\int\frac{\partial f(x;\theta)}{\partial\theta}\,\mathrm{d}x=\frac\partial{\partial\theta}\int f(x;\theta)\,\mathrm{d}x=0,
$$

so $\mathbb{E}_\theta S=0$ and, by independence, $\operatorname{Var}_\theta(S)=nI(\theta)$. Differentiating $g(\theta)=\int\hat g(\boldsymbol{x})f(\boldsymbol{x};\theta)\,\mathrm{d}\boldsymbol{x}$ under the integral sign,

$$
g'(\theta)=\int\hat g(\boldsymbol{x})\frac{\partial f(\boldsymbol{x};\theta)}{\partial\theta}\,\mathrm{d}\boldsymbol{x}=\mathbb{E}_\theta[\hat g(\boldsymbol{X})S(\boldsymbol{X};\theta)]=\operatorname{Cov}_\theta(\hat g,S).
$$

By the Cauchy–Schwarz inequality ([3.1.8](/3.1.8)), $[g'(\theta)]^2\le\operatorname{Var}_\theta(\hat g)\operatorname{Var}_\theta(S)=nI(\theta)\operatorname{Var}_\theta(\hat g)$. $\square$

**Remark 3.4.1** Equality holds for a given $\theta$ if and only if $\hat g-g(\theta)$ and $S$ are linearly related with probability one, $S(\boldsymbol{X};\theta)=a(\theta)[\hat g(\boldsymbol{X})-g(\theta)]$. Requiring this for every $\theta$ and integrating in $\theta$ shows that $f(\boldsymbol{x};\theta)$ must be of exponential family form with $\hat g$ as its sufficient statistic. Hence:

- an unbiased estimator whose variance attains the bound for every $\theta$ is a UMVUE;
- exponential families (in their usual parameter spaces) satisfy the regularity conditions;
- the bound can be attained only in exponential families, and even there only by the unbiased estimators of the particular functions $g(\theta)=\mathbb{E}_\theta T$ of the natural sufficient statistic $T$ (and their affine transformations);
- the variance of a UMVUE may therefore exceed the bound, for instance for $\sigma^2$ in Example 3.4.10.

**Example 3.4.8** For $\mathrm{Ber}(\theta)$, $\log f=x\log\theta+(1-x)\log(1-\theta)$, and $\frac{\partial\log f}{\partial\theta}=\frac x\theta-\frac{1-x}{1-\theta}=\frac{x-\theta}{\theta(1-\theta)}$, so $I(\theta)=\frac{\operatorname{Var}(X)}{\theta^2(1-\theta)^2}=\frac1{\theta(1-\theta)}$. The bound for unbiased estimators of $\theta$ is $\frac{\theta(1-\theta)}n=\operatorname{Var}(\bar X)$.

**Example 3.4.9** For $\mathrm{Poi}(\theta)$, $\frac{\partial\log f}{\partial\theta}=\frac x\theta-1$ and $I(\theta)=\frac1\theta$; the bound $\frac\theta n$ equals $\operatorname{Var}(\bar X)$. For $\mathrm{Exp}(\theta)$ with density $\theta\mathrm{e}^{-\theta x}$, $\frac{\partial\log f}{\partial\theta}=\frac1\theta-x$ and $I(\theta)=\operatorname{Var}(X)=\frac1{\theta^2}$; for $g(\theta)=1/\theta$, the bound is $\frac{(1/\theta^2)^2}{n/\theta^2}=\frac1{n\theta^2}=\operatorname{Var}(\bar X)$, so $\bar X$ is the UMVUE of the mean $1/\theta$. For $\mathcal{N}(\mu,\sigma^2)$ with $\sigma^2$ known, $I(\mu)=1/\sigma^2$ and the bound $\sigma^2/n$ is attained by $\bar X$. With $\mu$ known, $I(\sigma^2)=\frac1{2\sigma^4}$ and the bound $\frac{2\sigma^4}n$ is attained by $S_\mu^2=\frac1n\sum_{i=1}^n(X_i-\mu)^2$, which is therefore the UMVUE of $\sigma^2$.

For a $k$-dimensional parameter $\boldsymbol{\theta}=(\theta_1,\dots,\theta_k)^{\mathsf T}$, write $A\succeq B$ if $A-B$ is a **positive semidefinite matrix**. Under the analogous regularity conditions, every unbiased estimator $\hat{\boldsymbol{\theta}}$ of $\boldsymbol{\theta}$ satisfies

$$
\operatorname{Cov}_{\boldsymbol{\theta}}(\hat{\boldsymbol{\theta}})\succeq[nI(\boldsymbol{\theta})]^{-1},\qquad I_{ij}(\boldsymbol{\theta})=\mathbb{E}_{\boldsymbol{\theta}}\left[\frac{\partial\log f(X;\boldsymbol{\theta})}{\partial\theta_i}\frac{\partial\log f(X;\boldsymbol{\theta})}{\partial\theta_j}\right],
$$

where $I(\boldsymbol{\theta})=(I_{ij}(\boldsymbol{\theta}))$ is the *Fisher information matrix*. In particular, each diagonal entry gives $\operatorname{Var}(\hat\theta_i)\ge\{[nI(\boldsymbol{\theta})]^{-1}\}_{ii}$.

**Example 3.4.10** For $\mathcal{N}(\mu,\sigma^2)$ with $\boldsymbol{\theta}=(\theta_1,\theta_2)=(\mu,\sigma^2)$,

$$
\frac{\partial\log f}{\partial\theta_1}=\frac{x-\theta_1}{\theta_2},\qquad\frac{\partial\log f}{\partial\theta_2}=\frac{(x-\theta_1)^2-\theta_2}{2\theta_2^2},
$$

so $I_{11}=\frac1{\sigma^2}$, $I_{22}=\frac{\mathbb{E}[(X-\mu)^2-\sigma^2]^2}{4\sigma^8}=\frac1{2\sigma^4}$ and $I_{12}=\frac{\mathbb{E}(X-\mu)^3-\sigma^2\mathbb{E}(X-\mu)}{2\sigma^6}=0$. Hence

$$
[nI(\boldsymbol{\theta})]^{-1}=\begin{bmatrix}\sigma^2/n&0\\0&2\sigma^4/n\end{bmatrix}.
$$

$\bar X$ attains the bound for $\mu$, while the UMVUE $S^2$ has $\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1}>\frac{2\sigma^4}n$.

### 3.4.6. Efficiency

**Definition 3.4.4 (Efficiency)** Under the conditions of Theorem 3.4.4, the **efficiency** of an unbiased estimator $\hat g(\boldsymbol{X})$ of $g(\theta)$ is

$$
e_{\hat g}(\theta)=\frac{[g'(\theta)]^2/(nI(\theta))}{\operatorname{Var}_\theta(\hat g(\boldsymbol{X}))},\qquad0<e_{\hat g}(\theta)\le1.
$$
If $e_{\hat g}(\theta)=1$ for all $\theta$, $\hat g$ is called an **efficient estimator**; if $\lim_{n\to\infty}e_{\hat g}(\theta)=1$ for all $\theta$, it is called **asymptotically efficient**.

By Examples 3.4.8–3.4.10, $\bar X$ is efficient for $\theta$ in the Bernoulli and Poisson models, for the mean $1/\theta$ of $\mathrm{Exp}(\theta)$, and for $\mu$ in the normal model. In the normal model with $\mu$ unknown, $S^2$ has efficiency $\frac{2\sigma^4/n}{2\sigma^4/(n-1)}=\frac{n-1}n<1$: it is the UMVUE but not efficient, only asymptotically efficient. Efficiency is defined relative to the Cramér–Rao bound and is meaningful only when the regularity conditions of Theorem 3.4.4 hold; for $\mathrm{U}(0,\theta)$ they fail, and the UMVUE $\frac{n+1}nX_{(n)}$ has variance of order $n^{-2}$, below any bound of the form $c/n$.

## 3.5. The Method of Moments and MLE in Linear Regression

### 3.5.1. The Simple Linear Regression Model

The Ames Housing data record about $2000$ house sales in Ames, Iowa (2006–2010) with $82$ variables. To predict the sale price $y$ (the dependent variable) from the above-ground living area $x$ (the independent variable), consider the *simple linear regression model*

$$
y_i=\beta_0+\beta_1x_i+\varepsilon_i,\qquad i=1,\dots,n,
$$

where the $x_i$ are treated as fixed, $\beta_0,\beta_1$ are unknown coefficients, and the unobserved random errors satisfy $\mathbb{E}\varepsilon_i=0$, $\operatorname{Var}(\varepsilon_i)=\sigma^2$ and are iid. The line $y=\beta_0+\beta_1x$ is the population regression line; for estimates $\hat\beta_0,\hat\beta_1$, the sample regression line $\hat y=\hat\beta_0+\hat\beta_1x$ gives the fitted values $\hat y_i=\hat\beta_0+\hat\beta_1x_i$ and the residuals $\hat\varepsilon_i=y_i-\hat y_i$.

### 3.5.2. Least Squares, Moments and Likelihood

The ordinary **least squares** estimator minimizes the residual sum of squares,

$$
(\hat\beta_0,\hat\beta_1)=\arg\min_{\beta_0,\beta_1}\operatorname{RSS}(\beta_0,\beta_1),\qquad\operatorname{RSS}(\beta_0,\beta_1)=\sum_{i=1}^n(y_i-\beta_0-\beta_1x_i)^2,
$$

and setting the partial derivatives to zero gives

$$
\hat\beta_1=\frac{S_{xy}}{S_{xx}}=\frac{\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)}{\sum_{i=1}^n(x_i-\bar x)^2},\qquad\hat\beta_0=\bar y-\hat\beta_1\bar x.
$$

The square is used because it yields an explicit formula; an alternative is least absolute deviations, which minimizes $\sum|y_i-\hat y_i|$ and is more robust to outliers. The error variance is estimated by $\hat\sigma_n^2=\frac1n\sum_{i=1}^n\hat\varepsilon_i^2$, or by the bias-corrected $\hat\sigma^2=\frac1{n-2}\sum_{i=1}^n\hat\varepsilon_i^2$, which is unbiased. For the Ames data, the fitted line is $\widehat{\text{SalePrice}}=6759.9+115.79\times\text{LivingArea}$ (in dollars and square feet), with $\hat\sigma_n=54\,387$ and $\hat\sigma=54\,414$.

For a moment estimator, note that the assumption $\mathbb{E}(\varepsilon\mid x)=0$ implies the moment conditions $\mathbb{E}\varepsilon=0$ and $\mathbb{E}(x\varepsilon)=0$. Their sample versions,

$$
\frac1n\sum_{i=1}^n(y_i-\beta_0-\beta_1x_i)=0,\qquad\frac1n\sum_{i=1}^nx_i(y_i-\beta_0-\beta_1x_i)=0,
$$

are exactly the least squares normal equations, so the moment estimators coincide with the least squares estimators; the moment estimator of $\sigma^2$ is $\hat\sigma_n^2$, and $\hat\sigma^2$ is its bias correction.

For the MLE, assume in addition $\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$, equivalently $y_i\mid x_i\sim\mathcal{N}(\beta_0+\beta_1x_i,\sigma^2)$ independently. The likelihood is

$$
L(\beta_0,\beta_1,\sigma^2)=(2\pi\sigma^2)^{-n/2}\exp\left\{-\frac1{2\sigma^2}\sum_{i=1}^n(y_i-\beta_0-\beta_1x_i)^2\right\},
$$

so $l=-\frac n2\log(2\pi\sigma^2)-\frac{\operatorname{RSS}(\beta_0,\beta_1)}{2\sigma^2}$. For every $\sigma^2$, $l$ is maximized in $(\beta_0,\beta_1)$ by minimizing the RSS, so the MLEs of the coefficients are the least squares estimators, and then $\partial l/\partial\sigma^2=0$ gives $\hat\sigma^2_{\mathrm{MLE}}=\frac1n\operatorname{RSS}(\hat\beta_0,\hat\beta_1)=\hat\sigma_n^2$.

### 3.5.3. Multiple Linear Regression

With $p$ predictors, the model is $y_i=\beta_0+\beta_1x_{i1}+\cdots+\beta_px_{ip}+\varepsilon_i$. For the Ames data, using living area, lot area and the presence of central air conditioning (a $0/1$ variable) gives $\widehat{\text{SalePrice}}=-39\,570+107.7\times\text{LivingArea}+1.03\times\text{LotArea}+51\,710\times\text{CentralAir}$, with residual standard error $52\,420$. Writing $\boldsymbol{\beta}=(\beta_0,\beta_1,\dots,\beta_p)^{\mathsf T}$ and $\boldsymbol{x}_i=(1,x_{i1},\dots,x_{ip})^{\mathsf T}$, the model is $y_i=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}+\varepsilon_i$, or in matrix form

$$
\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},
$$

where $\boldsymbol{Y}=(y_1,\dots,y_n)^{\mathsf T}$, $\boldsymbol{\varepsilon}=(\varepsilon_1,\dots,\varepsilon_n)^{\mathsf T}$, and the $n\times(p+1)$ *design matrix* $X$ has rows $\boldsymbol{x}_i^{\mathsf T}$. The questions are how to estimate $\boldsymbol{\beta}$, how to predict, how to make inference on $\boldsymbol{\beta}$, and how to check the model.

The Gauss–Markov assumptions are:

1. *zero mean*: $\mathbb{E}(\varepsilon_i\mid\boldsymbol{x}_i)=0$, so that $\mathbb{E}(y_i\mid\boldsymbol{x}_i)=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}$;
2. *homoscedasticity*: $\operatorname{Var}(\varepsilon_i)=\sigma^2$ for all $i$;
3. *uncorrelated errors*: $\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$ for $i\ne j$.

The least squares estimator minimizes $\operatorname{RSS}(\boldsymbol{\beta})=\sum_{i=1}^n(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})^2=\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2$. If $\operatorname{rank}(X)=p+1$, the minimizer is unique and is given by the **normal equations** $X^{\mathsf T}X\boldsymbol{\beta}=X^{\mathsf T}\boldsymbol{Y}$ ([2.1](/2.1)):

$$
\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y},\qquad\hat\sigma_n^2=\frac1n\operatorname{RSS}(\hat{\boldsymbol{\beta}}),\qquad\hat\sigma^2=\frac1{n-p-1}\operatorname{RSS}(\hat{\boldsymbol{\beta}}).
$$

As in the simple case, the moment conditions $\mathbb{E}(\boldsymbol{x}_i\varepsilon_i)=\boldsymbol{0}$ lead to the same estimator. Under normal errors, the conditional likelihood of $\boldsymbol{Y}$ given the $\boldsymbol{x}_i$ is

$$
L(\boldsymbol{\beta},\sigma^2)=\prod_{i=1}^n\frac1{\sqrt{2\pi}\sigma}\exp\left\{-\frac{(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})^2}{2\sigma^2}\right\},
$$

and the likelihood equations give $\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}=\left(\sum_i\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}\right)^{-1}\sum_i\boldsymbol{x}_iy_i=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ and $\hat\sigma^2_{\mathrm{MLE}}=\frac1n\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}\|^2$.

The estimator has the following properties.

1. *Unbiasedness.* Under the zero-mean assumption, $\mathbb{E}\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}X\boldsymbol{\beta}=\boldsymbol{\beta}$, and $\operatorname{Cov}(\hat{\boldsymbol{\beta}})=\sigma^2(X^{\mathsf T}X)^{-1}$ under homoscedastic uncorrelated errors.
2. *Optimality.* By the Gauss–Markov theorem below, $\hat{\boldsymbol{\beta}}$ is the best linear unbiased estimator (BLUE).
3. *Normality.* Under normal errors, $\hat{\boldsymbol{\beta}}\sim\mathcal{N}_{p+1}(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1})$, a **multivariate normal distribution**, and $(n-p-1)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p-1}$.
4. *Independence.* Under normal errors, $\hat{\boldsymbol{\beta}}$ and $\hat\sigma^2$ (equivalently $\hat\sigma_n^2$) are independent.

**Theorem 3.5.1 (Gauss–Markov Theorem)** Under the Gauss–Markov assumptions with $\operatorname{rank}(X)=p+1$, for every linear unbiased estimator $\tilde{\boldsymbol{\beta}}=C\boldsymbol{Y}$ of $\boldsymbol{\beta}$ (with $C$ a constant $(p+1)\times n$ matrix and $\mathbb{E}\tilde{\boldsymbol{\beta}}=\boldsymbol{\beta}$ for all $\boldsymbol{\beta}$), $\operatorname{Cov}(\tilde{\boldsymbol{\beta}})-\operatorname{Cov}(\hat{\boldsymbol{\beta}})$ is positive semidefinite.

**Proof** Unbiasedness for all $\boldsymbol{\beta}$ means $CX=I_{p+1}$. Write $C=(X^{\mathsf T}X)^{-1}X^{\mathsf T}+D$; then $DX=O$. Hence $\operatorname{Cov}(\tilde{\boldsymbol{\beta}})=\sigma^2CC^{\mathsf T}=\sigma^2(X^{\mathsf T}X)^{-1}+\sigma^2DD^{\mathsf T}$, the cross terms vanishing because $DX=O$, and $\sigma^2DD^{\mathsf T}$ is positive semidefinite. $\square$

Unlike the Cramér–Rao bound, this optimality needs no distributional assumption, but it is restricted to estimators that are linear in $\boldsymbol{Y}$. Under normal errors, $\hat{\boldsymbol{\beta}}$ is even the UMVUE, since the model is then an exponential family with complete sufficient statistic $(X^{\mathsf T}\boldsymbol{Y},\boldsymbol{Y}^{\mathsf T}\boldsymbol{Y})$.

## 3.6. Kernel Density Estimation

### 3.6.1. From the Histogram to the Kernel Estimator

The estimators so far target finitely many parameters. Kernel density estimation estimates an entire unknown density $f$ from a sample, without assuming a parametric family. The familiar estimator is the histogram, but it depends on the choice of bins (too many bins overfit, too few oversmooth), it is discontinuous although the density usually is not, and its overall error can be large. The kernel estimator replaces the bins by a smooth bump placed at each observation.

For a continuous distribution, the density is the derivative of the distribution function,

$$
f(x)=F'(x)=\lim_{h\to0}\frac{F(x+h)-F(x-h)}{2h}.
$$

Replacing $F$ by the **empirical distribution function** $F_n$ and $h$ by a small $h_n>0$ gives the natural estimator

$$
f_n(x)=\frac{F_n(x+h_n)-F_n(x-h_n)}{2h_n}=\frac1{nh_n}\sum_{i=1}^nK_0\left(\frac{x-X_i}{h_n}\right),\qquad K_0(u)=\frac12\boldsymbol{1}_{[-1,1)}(u),
$$

since $F_n(x+h_n)-F_n(x-h_n)$ is the fraction of observations in $(x-h_n,x+h_n]$. Replacing the box $K_0$ by a smooth function $K$ gives a smooth estimate.

**Definition 3.6.1 (Kernel Density Estimation)** Let $X_1,\dots,X_n$ be a random sample from a distribution with density $f$. The estimator

$$
f_n(x)=\frac1{nh_n}\sum_{i=1}^nK\left(\frac{x-X_i}{h_n}\right)
$$
is called a **kernel density estimator** of $f$; the function $K$ is the **kernel function** and the constant $h_n>0$, with $h_n\to0$ as $n\to\infty$, is the **bandwidth**. Estimating a density in this way is called **kernel density estimation**.

Usually $K$ is itself a density, in which case $f_n$ is a density too: it is the average of $n$ copies of $K$ rescaled to width $h_n$ and centered at the observations. Typical conditions on $K$ are:

1. $K(x)\ge0$, $\sup_xK(x)\le M<\infty$ and $\lim_{|x|\to\infty}|x|K(x)=0$;
2. $K(-x)=K(x)$, $\int_{-\infty}^\infty K(x)\,\mathrm{d}x=1$ and $\int_{-\infty}^\infty x^2K(x)\,\mathrm{d}x<\infty$;
3. (for some results) the Fourier transform of $K$, that is, the **characteristic function** of the density $K$, is absolutely integrable.

| Kernel | $K(u)$ |
|---|---|
| uniform | $\frac12\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| triangular | $(1-\lvert u\rvert)\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| Epanechnikov | $\frac34(1-u^2)\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| quartic (biweight) | $\frac{15}{16}(1-u^2)^2\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| triweight | $\frac{35}{32}(1-u^2)^3\boldsymbol{1}\{\lvert u\rvert\le1\}$ |
| Gaussian | $\frac1{\sqrt{2\pi}}\mathrm{e}^{-u^2/2}$ |
| cosine | $\frac\pi4\cos\left(\frac{\pi u}2\right)\boldsymbol{1}\{\lvert u\rvert\le1\}$ |

The Epanechnikov kernel is optimal in the sense of asymptotic mean integrated squared error, but the loss in efficiency from using another common kernel is small; the Gaussian kernel is often used for its convenient mathematical properties. The choice of bandwidth matters far more than the choice of kernel.

### 3.6.2. Bandwidth Selection

The bandwidth controls the bias–variance trade-off. A small $h$ follows the data closely: the estimate is noisy, with small bias and large variance. A large $h$ oversmooths: the variance is small but the bias is large and features such as modes are lost. With $\operatorname{MSE}=\operatorname{Bias}^2+\operatorname{Var}$ at each point, a global criterion is the mean integrated squared error

$$
\operatorname{MISE}(h)=\mathbb{E}\int[f_n(x)-f(x)]^2\,\mathrm{d}x.
$$

For a twice differentiable $f$ and a kernel satisfying conditions 1–2, a Taylor expansion gives $\mathbb{E}f_n(x)-f(x)\approx\frac{h^2}2m_2(K)f''(x)$ and $\operatorname{Var}(f_n(x))\approx\frac{f(x)R(K)}{nh}$, where $R(g)=\int g(x)^2\,\mathrm{d}x$ and $m_2(K)=\int x^2K(x)\,\mathrm{d}x$. Integrating, $\operatorname{MISE}(h)=\operatorname{AMISE}(h)+o\left(\frac1{nh}+h^4\right)$ with the asymptotic MISE

$$
\operatorname{AMISE}(h)=\frac{R(K)}{nh}+\frac14m_2(K)^2h^4R(f''),
$$

which is minimized by

$$
h_{\mathrm{AMISE}}=\left[\frac{R(K)}{m_2(K)^2R(f'')\,n}\right]^{1/5}.
$$

The optimal bandwidth is of order $n^{-1/5}$ and the optimal MISE of order $n^{-4/5}$, slower than the $n^{-1}$ of parametric estimation. The formula cannot be used directly because $R(f'')$ involves the unknown density. Practical selectors either plug in an estimate of $R(f'')$ (plug-in methods; replacing $f$ by a normal density gives the rule of thumb $h=0.9\min(\hat\sigma,\widehat{\mathrm{IQR}}/1.34)\,n^{-1/5}$, the default `bw.nrd0` of R's `density`) or minimize an unbiased estimate of the MISE (cross-validation). Adaptive (variable) bandwidths, such as balloon and sample-point estimators, let $h$ vary with $x$ or with the observation.

![Kernel density estimates with a Gaussian kernel from 100 observations of N(0, 1), drawn as a rug, for three bandwidths: h = 0.05 undersmooths, h = 0.35 (the normal-reference choice) is close to the true density (dashed), h = 2 oversmooths.](./plots/kde-bandwidth.py)

In R, `density(x, bw = "nrd0", adjust = 1, kernel = "gaussian")` computes the estimate; `bw` selects the bandwidth rule (for example `"nrd0"` or the plug-in `"SJ"`), `kernel` the kernel (such as `"epanechnikov"` or `"rectangular"`), and the bandwidth actually used is `adjust * bw`.

### 3.6.3. Asymptotic Properties

If $f$ is continuous at $x$, $K$ satisfies conditions 1–2, $h_n\to0$ and $nh_n\to\infty$, then the kernel estimator is:

1. *asymptotically unbiased*: $\lim_{n\to\infty}\mathbb{E}f_n(x)=f(x)$;
2. *consistent in quadratic mean*: $\lim_{n\to\infty}\mathbb{E}[f_n(x)-f(x)]^2=0$, hence weakly consistent, $f_n(x)\xrightarrow{p}f(x)$;
3. *strongly consistent*, $f_n(x)\xrightarrow{\text{a.s.}}f(x)$, under the stronger condition $nh_n/\log n\to\infty$;
4. *asymptotically normal*: if $f(x)>0$,

   $$
   \frac{f_n(x)-\mathbb{E}f_n(x)}{\sqrt{\operatorname{Var}(f_n(x))}}\xrightarrow{d}\mathcal{N}(0,1).
   $$

## 3.7. High-Dimensional Data and Sparse Estimation (Optional)

### 3.7.1. High-Dimensional Problems

High-dimensional statistics and sparse modeling have been among the most active areas of statistics for two decades. In high-dimensional data the number of variables $p$ is comparable to or much larger than the sample size $n$. In genomics, a study may have a few hundred patients and tens of thousands of gene expression levels, and the questions are to classify patients, to identify the driver genes and to estimate their effects. In functional MRI studies of the visual cortex, the response of a single voxel was modeled on $10\,921$ wavelet (Gabor) features of the image with $n=1750$ training images. The key structural assumption is *sparsity*: only a few predictors are relevant, so most coefficients $\beta_j$ are zero. Sparsity is plausible in genomics and imaging but may fail in other areas, such as economics and finance, where many small effects can matter.

Consider the linear model $\boldsymbol{Y}=X\boldsymbol{\beta}^*+\boldsymbol{\varepsilon}$ with a deterministic $X\in\mathbb{R}^{n\times p}$, $p\gg n$, iid noise, and a sparse $\boldsymbol{\beta}^*$ with at most $s<p$ nonzero entries on the support $\mathcal{S}=\{j\colon\beta_j^*\ne0\}$. Least squares is ill-posed: for $p>n$ the matrix $X^{\mathsf T}X$ is singular and infinitely many $\boldsymbol{\beta}$ fit the data exactly. Best subset selection,

$$
\min_{\boldsymbol{\beta}}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|_2^2\quad\text{subject to}\quad\|\boldsymbol{\beta}\|_0\le k,
$$

where $\|\boldsymbol{\beta}\|_0$ counts the nonzero entries, enforces sparsity directly but is a combinatorial (NP-hard) problem.

### 3.7.2. The Lasso

Replacing the $\ell_0$ constraint by the $\ell_1$ norm $\|\boldsymbol{\beta}\|_1=\sum_j|\beta_j|$ leads to basis pursuit (S. Chen and D. Donoho, 1994), the nonnegative garrote (L. Breiman, 1995) and the *Lasso* (R. Tibshirani, 1996):

$$
\hat{\boldsymbol{\beta}}=\arg\min_{\boldsymbol{\beta}}\left\{\|\boldsymbol{Y}-X\boldsymbol{\beta}\|_2^2+\lambda\|\boldsymbol{\beta}\|_1\right\},\qquad\lambda\ge0.
$$

The $\ell_1$ penalty has two key properties. Because the $\ell_1$ ball has corners on the coordinate axes, many entries of $\hat{\boldsymbol{\beta}}$ are exactly zero, so the Lasso performs variable selection; and the problem is convex, a convex relaxation of the $\ell_0$ problem, so it can be solved efficiently even for very large $p$. The tuning parameter $\lambda$ trades fit against sparsity and is usually chosen by cross-validation.

The theory of the Lasso studies three kinds of guarantees under conditions on $X$ (such as restricted eigenvalue or irrepresentable conditions) and for $\lambda$ of order $\sigma\sqrt{n\log p}$:

- *estimation error* $\|\hat{\boldsymbol{\beta}}-\boldsymbol{\beta}^*\|_2^2$, of order $s\log p/n$ (P. Bickel, Y. Ritov and A. Tsybakov, 2009; S. Negahban et al., 2009);
- *prediction error* $\|X\hat{\boldsymbol{\beta}}-X\boldsymbol{\beta}^*\|_2^2$ (F. Bunea et al., 2006);
- *model selection consistency*: the estimated support $\hat{\mathcal{S}}=\{j\colon\hat\beta_j\ne0\}$ satisfies $\mathbb{P}(\hat{\mathcal{S}}=\mathcal{S})\to1$ (P. Zhao and B. Yu, 2006).

A current frontier is uncertainty quantification after variable selection, that is, valid confidence intervals and $p$-values in high dimensions, through data splitting, the bootstrap, de-biased (de-sparsified) Lasso estimators, post-selection inference and knockoffs.

## Summary

| Method | Advantages | Drawbacks | Typical use |
|---|---|---|---|
| Method of moments | simple; needs only moments, no model | may be non-unique, inefficient or outside the parameter space | first estimates, complex models, starting values |
| Maximum likelihood | invariant; consistent, asymptotically normal and efficient | needs the model; may lack closed form; sensitive to model error | parametric models, large samples |
| UMVUE | optimal among unbiased estimators for every $n$ | may not exist; construction needs sufficient complete statistics | exact small-sample inference in exponential families |
| Kernel density estimation | no parametric assumption; flexible | slow rate $n^{-4/5}$; sensitive to bandwidth | exploratory analysis, nonparametric density estimation |

- Estimators are compared by bias, variance and MSE for fixed $n$, and by consistency and asymptotic variance for large $n$. MSE $=$ variance $+$ bias$^2$, and a small bias can buy a large reduction in variance.
- The MLE maximizes the likelihood; it is a function of any sufficient statistic, invariant under reparametrization, and under regularity conditions asymptotically $\mathcal{N}(\theta,1/(nI(\theta)))$.
- The Rao–Blackwell theorem improves unbiased estimators by conditioning on a sufficient statistic, and the Lehmann–Scheffé theorem shows that an unbiased function of a sufficient and complete statistic is the unique UMVUE.
- The Cramér–Rao inequality bounds the variance of unbiased estimators by $[g'(\theta)]^2/(nI(\theta))$; the bound is attained only in exponential families, and it defines the efficiency of an estimator.
- In linear regression with normal errors, least squares, the method of moments and maximum likelihood give the same coefficient estimates, which are BLUE under the Gauss–Markov assumptions.
