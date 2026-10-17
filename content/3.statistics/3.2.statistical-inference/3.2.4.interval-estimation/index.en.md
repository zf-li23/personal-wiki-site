---
title: Interval Estimation and Confidence Intervals
description: Confidence intervals, confidence limits and confidence regions; reliability versus precision; the pivotal quantity method for normal, uniform and exponential populations and for two normal samples; large-sample approximate intervals, the Behrens–Fisher problem and Welch's interval; joint regions by Bonferroni and Šidák corrections.
---

A point estimate is a single number and says nothing about its own uncertainty: the observed sample is one of many possible samples, and the estimate is one of many plausible values. Interval estimation reports instead a range of values together with a guarantee, stated as a probability over repeated sampling, that the range contains the parameter. This chapter defines confidence intervals, confidence limits and confidence regions and the two competing requirements of reliability and precision (§4.1), develops the main construction, the pivotal quantity method, for normal, uniform and exponential populations and for comparing two normal populations (§4.2), turns to large-sample intervals based on the **central limit theorem**, including the Behrens–Fisher problem (§4.3), and ends with joint confidence regions for several parameters (§4.4). The pivots are built from the good point estimators of [3.2.3](/3.2.3), usually functions of a **sufficient statistic**, and their distributions are the normal, $\chi^2$, $t$ and $F$ **sampling distributions** of [3.2.2](/3.2.2). Confidence intervals and hypothesis tests are two sides of the same coin; the duality is taken up in [3.2.5](/3.2.5), and the Bayesian alternative, the credible interval, in [3.2.7](/3.2.7).

## 4.1. Basic Concepts

### 4.1.1. Interval Estimates and Confidence Intervals

Let $\boldsymbol{X}=(X_1,\dots,X_n)$ be a random sample from $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ and suppose we want to estimate a one-dimensional parameter $g(\theta)$. A point estimate $\hat g(\boldsymbol{X})$ does not show its own precision (or uncertainty, or risk), and the MSE is not a direct evaluation of a single estimate. An *interval estimate* of $g(\theta)$ is a pair of statistics $\hat g_1(\boldsymbol{X})\le\hat g_2(\boldsymbol{X})$, giving the random interval $[\hat g_1(\boldsymbol{X}),\hat g_2(\boldsymbol{X})]$, together with the probability that $g(\theta)\in[\hat g_1(\boldsymbol{X}),\hat g_2(\boldsymbol{X})]$. Any such pair of statistics gives an interval estimate; the question is how to evaluate and construct good ones.

**Example 4.1.1** For the heights of eighteen-year-old Hong Kong children, consider samples of size $n=100$ and the interval $[\bar X-1.96S/\sqrt n,\ \bar X+1.96S/\sqrt n]$ for the mean height $\mu$. The interval is random: it moves from sample to sample. In $1000$ repeated samples from a population with mean $68$ in, $94.7\%$ of these intervals covered the true mean. The narrower interval $[\bar X-0.5S/\sqrt n,\ \bar X+0.5S/\sqrt n]$ covered it only $38.2\%$ of the time. A good interval must be judged by both its coverage and its length.

Two criteria evaluate an interval estimate:

- *reliability*, the probability $\mathbb{P}_\theta(g(\theta)\in[\hat g_1(\boldsymbol{X}),\hat g_2(\boldsymbol{X})])$ that it covers the parameter;
- *precision*, measured by the expected length $\mathbb{E}_\theta[\hat g_2(\boldsymbol{X})-\hat g_1(\boldsymbol{X})]$, which usually depends on the sample size.

For a fixed sample size the two cannot be obtained simultaneously: a longer interval is more reliable and less precise. J. Neyman's principle resolves the conflict by fixing a level of reliability and, among intervals reaching it, seeking the one with the highest precision.

For the rest of this section let $g(\theta)=\theta$ with $\theta\in\Theta\subseteq\mathbb{R}$; the general case only changes notation.

**Definition 4.1.1 (Confidence Interval)** Let $\hat\theta_1(\boldsymbol{X})\le\hat\theta_2(\boldsymbol{X})$ be statistics, so that $[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ is a **random interval** (an interval whose endpoints are random variables). Given $0<\alpha<1$, if

$$
\mathbb{P}_\theta\left(\hat\theta_1(\boldsymbol{X})\le\theta\le\hat\theta_2(\boldsymbol{X})\right)\ge1-\alpha\qquad\text{for all }\theta\in\Theta,
$$
then $[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ is called a **confidence interval** for $\theta$ with **confidence level** $1-\alpha$. The infimum

$$
\inf_{\theta\in\Theta}\mathbb{P}_\theta\left(\hat\theta_1(\boldsymbol{X})\le\theta\le\hat\theta_2(\boldsymbol{X})\right)
$$
is called the **confidence coefficient** of the interval, and $\mathbb{E}_\theta(\hat\theta_2-\hat\theta_1)$ its precision (other measures of precision are also used).

The probability $\mathbb{P}_\theta(\hat\theta_1\le\theta\le\hat\theta_2)$ is the coverage probability at $\theta$. A confidence interval with level $1-\alpha$ has coverage at least $1-\alpha$ everywhere, and its confidence coefficient is the largest such level. Neyman's principle asks for the most precise interval whose confidence coefficient is at least $1-\alpha$; when the coverage probability does not depend on $\theta$, confidence level and coefficient coincide.

**Example 4.1.2** Let $X_1,\dots,X_n$ be a random sample from $\mathcal{N}(\mu,\sigma^2)$, $\mu\in\mathbb{R}$, $\sigma^2>0$, with **sample mean** $\bar X$ and **sample variance** $S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2$, and consider the interval estimate $[\bar X-kS/\sqrt n,\ \bar X+kS/\sqrt n]$ of $\mu$. With $\theta=(\mu,\sigma^2)$, the coverage probability is

$$
\mathbb{P}_\theta\left(\bar X-\frac{kS}{\sqrt n}\le\mu\le\bar X+\frac{kS}{\sqrt n}\right)=\mathbb{P}_\theta\left(\left\lvert\frac{\sqrt n(\bar X-\mu)}S\right\rvert\le k\right)=\mathbb{P}(|T|\le k),\qquad T\sim t_{n-1},
$$

since $T=\sqrt n(\bar X-\mu)/S\sim t_{n-1}$ (Corollary 2.1.4). It does not depend on $\theta$, so it is the confidence coefficient, and it increases with $k$. Since $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$, the expected length is

$$
l_k=\frac{2k\,\mathbb{E}S}{\sqrt n}=\frac{2\sqrt2\,k\sigma\,\Gamma(n/2)}{\sqrt{n(n-1)}\,\Gamma((n-1)/2)},
$$

which also increases with $k$. For a given $n$, increasing the reliability requires a larger $k$, and increasing the precision requires a smaller $k$: this is the trade-off between reliability and precision.

### 4.1.2. Interpretation

Let $\alpha=0.05$, and suppose that after sampling we obtain the $95\%$ confidence interval $[0.5,1.5]$ for $\mu$. Can we say that the probability that $0.5\le\mu\le1.5$ is at least $0.95$? No. Before sampling, $[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ is a random interval; after sampling, $[\hat\theta_1(\boldsymbol{x}),\hat\theta_2(\boldsymbol{x})]$ is an observed interval, which is not random, and the fixed parameter either lies in it or does not. The probability refers to the procedure, in the frequency interpretation of probability: if the experiment is repeated $N$ times with samples $\boldsymbol{x}^{(1)},\dots,\boldsymbol{x}^{(N)}$, producing intervals $[\hat\theta_1(\boldsymbol{x}^{(j)}),\hat\theta_2(\boldsymbol{x}^{(j)})]$, then in the long run at least about $0.95N$ of these intervals contain $\theta$.

![One hundred simulated 95% intervals [x_bar - k s / sqrt(n), x_bar + k s / sqrt(n)] for the mean of N(68, 3.6) with n = 100. Left, k = 1.96: almost all intervals (gray) cover the true mean (vertical line); those that miss are drawn in color. Right, k = 0.5: the intervals are shorter but most of them miss.](./plots/ci-coverage.py)

### 4.1.3. Confidence Limits

Often only one side matters: the strength of a new material should be at least some value, and a rate of spoiled products should be at most $1\%$.

**Definition 4.1.2 (Confidence Limits)** Let $\hat\theta_U(\boldsymbol{X})$ and $\hat\theta_L(\boldsymbol{X})$ be statistics and $0<\alpha<1$. If

$$
\mathbb{P}_\theta\left(\theta\le\hat\theta_U(\boldsymbol{X})\right)\ge1-\alpha\quad\text{for all }\theta\in\Theta,\qquad\text{respectively}\qquad\mathbb{P}_\theta\left(\hat\theta_L(\boldsymbol{X})\le\theta\right)\ge1-\alpha\quad\text{for all }\theta\in\Theta,
$$
then $\hat\theta_U$ is called an **upper confidence limit** and $\hat\theta_L$ a **lower confidence limit** for $\theta$ with confidence level $1-\alpha$.

For a given level, an upper confidence limit is more precise the smaller $\mathbb{E}_\theta\hat\theta_U$, and a lower confidence limit the larger $\mathbb{E}_\theta\hat\theta_L$. Two one-sided limits combine into an interval.

**Lemma 4.1.1** Let $\hat\theta_L(\boldsymbol{X})$ be a lower confidence limit for $\theta$ with confidence level $1-\alpha_1$ and $\hat\theta_U(\boldsymbol{X})$ an upper confidence limit with confidence level $1-\alpha_2$, and suppose $\hat\theta_L(\boldsymbol{X})\le\hat\theta_U(\boldsymbol{X})$. Then $[\hat\theta_L(\boldsymbol{X}),\hat\theta_U(\boldsymbol{X})]$ is a confidence interval for $\theta$ with confidence level $1-(\alpha_1+\alpha_2)$.

**Proof** The interval misses $\theta$ exactly when $\theta<\hat\theta_L$ or $\theta>\hat\theta_U$. Hence

$$
\mathbb{P}_\theta(\hat\theta_L\le\theta\le\hat\theta_U)=1-\mathbb{P}_\theta(\theta<\hat\theta_L)-\mathbb{P}_\theta(\theta>\hat\theta_U)\ge1-\alpha_1-\alpha_2,
$$

the two events being disjoint because $\hat\theta_L\le\hat\theta_U$. $\square$

### 4.1.4. Confidence Regions

For a parameter of dimension $k\ge2$, such as the mean height and mean weight of a population of children, the interval is replaced by a region.

**Definition 4.1.3 (Confidence Region)** Let $\mathcal{F}=\{f(x;\boldsymbol{\theta})\colon\boldsymbol{\theta}\in\Theta\}$ with $\boldsymbol{\theta}=(\theta_1,\dots,\theta_k)\in\Theta\subseteq\mathbb{R}^k$, $k\ge2$, let $\boldsymbol{X}$ be a random sample from $f(x;\boldsymbol{\theta})$, and let $S(\boldsymbol{X})$ be a statistic. Then $S(\boldsymbol{X})$ is called a **confidence region** for $\boldsymbol{\theta}$ with confidence level $1-\alpha$, and $\inf_{\boldsymbol{\theta}\in\Theta}\mathbb{P}_{\boldsymbol{\theta}}(\boldsymbol{\theta}\in S(\boldsymbol{X}))$ its confidence coefficient, if

1. for each $\boldsymbol{X}$, $S(\boldsymbol{X})$ is a subset of $\Theta$;
2. for a given $0<\alpha<1$, $\mathbb{P}_{\boldsymbol{\theta}}(\boldsymbol{\theta}\in S(\boldsymbol{X}))\ge1-\alpha$ for all $\boldsymbol{\theta}\in\Theta$.

A confidence region may be an ellipse, a disk or any other set. A rectangle $[\hat\theta_{1L},\hat\theta_{1U}]\times[\hat\theta_{2L},\hat\theta_{2U}]$ is called a *joint confidence interval*, or simultaneous confidence intervals; it is the easiest to report, and §4.4 constructs such rectangles.

## 4.2. The Pivotal Quantity Method

### 4.2.1. The Method

**Example 4.2.1** Let $X_1,\dots,X_n$ be a random sample from $\mathcal{N}(\mu,\sigma^2)$ where $\mu$ is unknown and $\sigma^2$ is known. We want a confidence interval for $\mu$ with confidence coefficient $1-\alpha$, for instance a $95\%$ interval for the mean height of eighteen-year-old Hong Kong children. The natural point estimate of $\mu$ is $\bar X$, whose distribution is $\mathcal{N}(\mu,\sigma^2/n)$. Its standardization

$$
Z=\frac{\sqrt n(\bar X-\mu)}\sigma\sim\mathcal{N}(0,1)
$$

has a distribution that does not depend on $\mu$. With $z_{\alpha/2}$ the upper $\alpha/2$ quantile of $\mathcal{N}(0,1)$,

$$
\mathbb{P}_\mu\left(\left\lvert\frac{\sqrt n(\bar X-\mu)}\sigma\right\rvert\le z_{\alpha/2}\right)=1-\alpha,\qquad\text{that is,}\qquad\mathbb{P}_\mu\left(\bar X-\frac\sigma{\sqrt n}z_{\alpha/2}\le\mu\le\bar X+\frac\sigma{\sqrt n}z_{\alpha/2}\right)=1-\alpha.
$$

Therefore $\left[\bar X-\frac{\sigma}{\sqrt n}z_{\alpha/2},\ \bar X+\frac{\sigma}{\sqrt n}z_{\alpha/2}\right]$ is a confidence interval for $\mu$ with confidence level (and coefficient) $1-\alpha$. Its length $l_n=2\sigma z_{\alpha/2}/\sqrt n$ is not random, and:

1. the larger the sample size, the shorter $l_n$ and the higher the precision;
2. the larger $\sigma$, the longer $l_n$;
3. the smaller $\alpha$, that is, the larger the level $1-\alpha$, the larger $z_{\alpha/2}$ and the lower the precision.

For given $\sigma$ and $\alpha$, the precision can only be increased by increasing the sample size. For example, to guarantee a length $l_n\le0.5$ when $\sigma=1$ and $\alpha=0.05$, we need $2\sigma z_{\alpha/2}/\sqrt n\le0.5$, that is, $n\ge(2\cdot1.96/0.5)^2=61.5$, so $n=62$.

Why a symmetric interval? Any $a<b$ with $\mathbb{P}(a\le Z\le b)=1-\alpha$ gives an interval of length $(b-a)\sigma/\sqrt n$, and since the $\mathcal{N}(0,1)$ density is symmetric and unimodal, $b-a$ is minimized by $b=-a=z_{\alpha/2}$. The same principle, putting the interval where the density of the pivot is highest, gives shortest intervals for other unimodal pivots, and equal tails are a convenient approximation when the pivot is skewed.

The method of Example 4.2.1 consists of four steps.

1. Find a random variable that contains the parameter $\theta$ and the sample $X_1,\dots,X_n$, preferably through a sufficient statistic, and whose distribution is known exactly or at least approximately.
2. Determine constants $a<b$ such that this random variable lies in $[a,b]$ with $\mathbb{P}_\theta$-probability at least $1-\alpha$.
3. Rearrange the inequality of step 2 into an interval whose endpoints are statistics and which contains $\theta$.
4. The interval of step 3 is the required confidence interval.

**Definition 4.2.1 (Pivotal Quantity)** A random variable $G(\boldsymbol{X};\theta)$ that depends on the sample and on the parameter $\theta$, and whose distribution does not depend on $\theta$, is called a **pivotal quantity** (pivot) for $\theta$. The construction of confidence intervals by steps 1–4 is the **pivotal quantity method**.

How do we find a pivot? It depends on the problem, but the usual route is: take a good estimator $\hat\theta$ of $\theta$, often a function of a sufficient statistic; determine its distribution, exact or limiting, which depends on $\theta$; and transform $\hat\theta$ so that the distribution of the transformed variable no longer depends on the parameters.

The pivot is not unique. In Example 4.2.1, even when $\sigma^2$ is known, $T=\frac{\sqrt n(\bar X-\mu)}S\sim t_{n-1}$ is also a pivot, leading to the interval $\left[\bar X-\frac{S}{\sqrt n}t_{n-1,\alpha/2},\ \bar X+\frac{S}{\sqrt n}t_{n-1,\alpha/2}\right]$. Which one is better? In a simulation from $\mathcal{N}(1,2)$ with $n=100$, where $z_{0.025}=1.96$ and $t_{99,0.025}=1.98$, the two $95\%$ intervals are $[\bar X\pm0.277]$ and $[\bar X\pm0.198S]$; over $1000$ replications their empirical coverage probabilities, the fractions of intervals covering $\mu$, were $0.952$ and $0.948$, both close to $0.95$. Repeating for $n$ from $20$ to $500$, the coverages of both fluctuate around $0.95$, but the $t$ interval is slightly longer on average, especially for small $n$. When $\sigma$ is known, the $z$ interval uses the information and is preferred.

The same pivot also gives one-sided limits: with confidence level $1-\alpha$, $\bar X+\sigma z_\alpha/\sqrt n$ is an upper confidence limit and $\bar X-\sigma z_\alpha/\sqrt n$ a lower confidence limit for $\mu$.

### 4.2.2. One Normal Population

**Example 4.2.2** Let $X_1,\dots,X_n$ be a random sample from $\mathcal{N}(\mu,\sigma^2)$ with $\mu$ known and $\sigma^2$ unknown. Let $S_\mu^2=\frac1n\sum_{i=1}^n(X_i-\mu)^2$; then

$$
\frac{nS_\mu^2}{\sigma^2}=\sum_{i=1}^n\left(\frac{X_i-\mu}\sigma\right)^2\sim\chi^2_n
$$

is a pivot. For any $0<a<b$ with $\mathbb{P}(a\le\chi^2_n\le b)=1-\alpha$,

$$
\mathbb{P}_{\sigma^2}\left(a\le\frac{nS_\mu^2}{\sigma^2}\le b\right)=\mathbb{P}_{\sigma^2}\left(\frac{nS_\mu^2}b\le\sigma^2\le\frac{nS_\mu^2}a\right)=1-\alpha\qquad\text{for all }\sigma^2.
$$

Choosing equal tails, $a=\chi^2_{n,1-\alpha/2}$ and $b=\chi^2_{n,\alpha/2}$ (simple, though not the shortest), gives the interval

$$
\left[\frac{nS_\mu^2}{\chi^2_{n,\alpha/2}},\ \frac{nS_\mu^2}{\chi^2_{n,1-\alpha/2}}\right].
$$

Why not use $S^2$ here? With $\mu$ known, $S_\mu^2$ is sufficient and is the UMVUE of $\sigma^2$ (Example 3.4.9); $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$ is also a pivot but wastes one degree of freedom, giving a longer interval on average.

**Example 4.2.3** Let $X_1,\dots,X_n$ be a random sample from $\mathcal{N}(\mu,\sigma^2)$ with both parameters unknown, and $\boldsymbol{\theta}=(\mu,\sigma^2)$. We have

$$
\frac{\sqrt n(\bar X-\mu)}\sigma\sim\mathcal{N}(0,1),\qquad\frac{(n-1)S^2}{\sigma^2}=\sum_{i=1}^n\left(\frac{X_i-\bar X}\sigma\right)^2\sim\chi^2_{n-1},
$$

and the two are independent (Theorem 2.1.3), so

$$
\frac{\sqrt n(\bar X-\mu)/\sigma}{\sqrt{(n-1)S^2/[\sigma^2(n-1)]}}=\frac{\sqrt n(\bar X-\mu)}S\sim t_{n-1},
$$

a pivot for $\mu$ free of the nuisance parameter $\sigma^2$. For $a<b$ with $\mathbb{P}(a\le t_{n-1}\le b)=1-\alpha$, $\mathbb{P}_{\boldsymbol{\theta}}\left(\bar X-b\frac S{\sqrt n}\le\mu\le\bar X-a\frac S{\sqrt n}\right)=1-\alpha$ for all $\boldsymbol{\theta}$; the symmetric choice $b=-a=t_{n-1,\alpha/2}$ gives the shortest interval

$$
\left[\bar X-t_{n-1,\alpha/2}\frac S{\sqrt n},\ \bar X+t_{n-1,\alpha/2}\frac S{\sqrt n}\right]=\bar X\pm t_{n-1,\alpha/2}\frac S{\sqrt n}.
$$

For $\sigma^2$, repeating Example 4.2.2 with the pivot $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$ gives

$$
\left[\frac{(n-1)S^2}{\chi^2_{n-1,\alpha/2}},\ \frac{(n-1)S^2}{\chi^2_{n-1,1-\alpha/2}}\right].
$$

For the children's heights, a sample of size $n=100$ from a population with $(\mu,\sigma^2)=(68,3.6)$ gave $\bar x=67.8$ and $s^2=4.13$. With $t_{99,0.025}=1.984$, $\chi^2_{99,0.025}=128.4$ and $\chi^2_{99,0.975}=73.4$, the $95\%$ confidence intervals are $[67.4,68.2]$ for $\mu$ and $[3.18,5.57]$ for $\sigma^2$; both contain the true values.

The four intervals for a normal population are:

| Target | Condition | Pivot | Confidence interval with level $1-\alpha$ |
|---|---|---|---|
| $\mu$ | $\sigma^2$ known | $\frac{\sqrt n(\bar X-\mu)}\sigma\sim\mathcal{N}(0,1)$ | $\bar X\pm z_{\alpha/2}\frac\sigma{\sqrt n}$ |
| $\mu$ | $\sigma^2$ unknown | $\frac{\sqrt n(\bar X-\mu)}S\sim t_{n-1}$ | $\bar X\pm t_{n-1,\alpha/2}\frac S{\sqrt n}$ |
| $\sigma^2$ | $\mu$ known | $\frac{nS_\mu^2}{\sigma^2}\sim\chi^2_n$ | $\left[\frac{nS_\mu^2}{\chi^2_{n,\alpha/2}},\frac{nS_\mu^2}{\chi^2_{n,1-\alpha/2}}\right]$ |
| $\sigma^2$ | $\mu$ unknown | $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ | $\left[\frac{(n-1)S^2}{\chi^2_{n-1,\alpha/2}},\frac{(n-1)S^2}{\chi^2_{n-1,1-\alpha/2}}\right]$ |

### 4.2.3. Uniform and Exponential Populations

**Example 4.2.4** Let $X_1,\dots,X_n$ be a random sample from $\mathrm{U}(0,\theta)$, $\theta>0$. The **order statistic** $X=X_{(n)}$ is sufficient for $\theta$, with density $f_X(x;\theta)=\frac n{\theta^n}x^{n-1}$ for $0\le x\le\theta$. The variable $Y=X_{(n)}/\theta$ has density $f_Y(y)=ny^{n-1}$, $0\le y\le1$, free of $\theta$, so it is a pivot. For any $0\le a<b\le1$ with $\int_a^bny^{n-1}\,\mathrm{d}y=b^n-a^n=1-\alpha$,

$$
\mathbb{P}_\theta(a\le Y\le b)=\mathbb{P}_\theta\left(a\le\frac{X_{(n)}}\theta\le b\right)=\mathbb{P}_\theta\left(\frac{X_{(n)}}b\le\theta\le\frac{X_{(n)}}a\right)=1-\alpha\qquad\text{for all }\theta,
$$

and $[X_{(n)}/b,\ X_{(n)}/a]$ is a confidence interval with level $1-\alpha$. Its length $X_{(n)}\left(\frac1a-\frac1b\right)$, with $a=a(b)=(b^n-1+\alpha)^{1/n}$, is minimized at $b=1$, $a=\alpha^{1/n}$, since $\frac{\mathrm{d}}{\mathrm{d}b}\left(\frac1a-\frac1b\right)=\frac{1}{b^2}-\frac{b^{n-1}}{a^{n+1}}<0$ for $a<b$. The shortest interval is

$$
\left[X_{(n)},\ \frac{X_{(n)}}{\alpha^{1/n}}\right].
$$

Here the density of the pivot is increasing, so the shortest interval puts all of $\alpha$ in the left tail of $Y$.

**Example 4.2.5** In a test of the lifetimes of $5$ light bulbs of one brand, the lifetimes were $2,3,1,3$ and $4$ years. By the method of moments and by maximum likelihood under an exponential model ([3.2.3](/3.2.3)), the mean lifetime is estimated by $\bar x=2.6$ years. What is a confidence interval?

Let $X_1,\dots,X_n$ be a random sample from $\mathrm{Exp}(\lambda)$ with density $\lambda\mathrm{e}^{-\lambda x}\boldsymbol{1}_{(0,\infty)}(x)$, $\lambda>0$. Since $\bar X$ is unbiased for $1/\lambda$ (it is the UMVUE), we build the interval on $\bar X$. Because $2\lambda X_i\sim\mathrm{Exp}(1/2)=\chi^2_2$ independently,

$$
2\lambda n\bar X=2\lambda\sum_{i=1}^nX_i\sim\chi^2_{2n}
$$

(Corollary 2.1.7) is a pivot. From $\mathbb{P}\left(\chi^2_{2n,1-\alpha/2}\le2\lambda n\bar X\le\chi^2_{2n,\alpha/2}\right)=1-\alpha$, the interval for $\lambda$ is

$$
\left[\frac{\chi^2_{2n,1-\alpha/2}}{2n\bar X},\ \frac{\chi^2_{2n,\alpha/2}}{2n\bar X}\right],
$$

and, inverting, $\left[\frac{2n\bar X}{\chi^2_{2n,\alpha/2}},\frac{2n\bar X}{\chi^2_{2n,1-\alpha/2}}\right]$ is the interval for the mean lifetime $1/\lambda$. For the light bulbs, $n=5$, $\bar x=2.6$, $\chi^2_{10,0.025}=20.48$ and $\chi^2_{10,0.975}=3.25$, so the $95\%$ confidence interval for the mean lifetime is

$$
\left[\frac{26}{20.48},\ \frac{26}{3.25}\right]=[1.27,\ 8.01]\ \text{years},
$$

very wide because the sample is tiny.

### 4.2.4. Two Normal Populations

Comparisons of two populations are among the most common problems in practice: the yields of two kinds of wheat, the yields of a process at two temperatures, the heights of men and women, the average treatment effect of a drug. Let $X_1,\dots,X_m$ and $Y_1,\dots,Y_n$ be independent random samples from $\mathcal{N}(\mu_1,\sigma_1^2)$ and $\mathcal{N}(\mu_2,\sigma_2^2)$ with all four parameters unknown, and let

$$
S_X^2=\frac1{m-1}\sum_{i=1}^m(X_i-\bar X)^2,\qquad S_Y^2=\frac1{n-1}\sum_{j=1}^n(Y_j-\bar Y)^2.
$$

We want confidence intervals for $\mu_1-\mu_2$ and for $\sigma_1^2/\sigma_2^2$.

**Example 4.2.6 (Difference of Means, Equal Variances)** To find a pivot for $\mu_1-\mu_2$ we assume that the variances, although unknown, are equal, $\sigma_1^2=\sigma_2^2=\sigma^2$. Since $\bar X-\mu_1\sim\mathcal{N}(0,\sigma^2/m)$ and $\bar Y-\mu_2\sim\mathcal{N}(0,\sigma^2/n)$ are independent,

$$
\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sigma\sqrt{\frac1m+\frac1n}}\sim\mathcal{N}(0,1).
$$

Also $(m-1)S_X^2/\sigma^2\sim\chi^2_{m-1}$ and $(n-1)S_Y^2/\sigma^2\sim\chi^2_{n-1}$ are independent, so $[(m-1)S_X^2+(n-1)S_Y^2]/\sigma^2\sim\chi^2_{m+n-2}$, independent of the means. With the pooled variance $S_w^2=\frac{(m-1)S_X^2+(n-1)S_Y^2}{m+n-2}$ it follows that

$$
\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_w\sqrt{\frac1m+\frac1n}}\sim t_{m+n-2}
$$

(Corollary 2.1.5), and, as in Example 4.2.3,

$$
(\bar X-\bar Y)\pm t_{m+n-2,\alpha/2}\,S_w\sqrt{\frac1m+\frac1n}
$$

is a confidence interval for $\mu_1-\mu_2$ with level $1-\alpha$.

**Example 4.2.7 (Ratio of Variances)** Since $(m-1)S_X^2/\sigma_1^2\sim\chi^2_{m-1}$ and $(n-1)S_Y^2/\sigma_2^2\sim\chi^2_{n-1}$ are independent,

$$
\frac{S_Y^2/\sigma_2^2}{S_X^2/\sigma_1^2}=\frac{\sigma_1^2}{\sigma_2^2}\cdot\frac{S_Y^2}{S_X^2}\sim F_{n-1,m-1}
$$

(the reciprocal of the statistic in Corollary 2.1.6) is a pivot for $\sigma_1^2/\sigma_2^2$, with no assumption on the means. For $0<a<b$ with $\mathbb{P}(a\le F_{n-1,m-1}\le b)=1-\alpha$, we get $\mathbb{P}_{\boldsymbol{\theta}}\left(a\frac{S_X^2}{S_Y^2}\le\frac{\sigma_1^2}{\sigma_2^2}\le b\frac{S_X^2}{S_Y^2}\right)=1-\alpha$ for all $\boldsymbol{\theta}=(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2)$, and with equal tails the interval

$$
\left[\frac{S_X^2}{S_Y^2}F_{n-1,m-1,1-\alpha/2},\ \frac{S_X^2}{S_Y^2}F_{n-1,m-1,\alpha/2}\right].
$$

**Example 4.2.8 (Professor Salaries)** The nine-month salaries of $397$ faculty members (assistant professors, associate professors and professors) of a college in the U.S. in 2008–09 were collected to monitor salary differences, together with rank, discipline, years since the PhD, years of service and sex (the data set `Salaries` of the R package `carData`). Is there a difference in salary between professors and assistant professors, and between men and women? The summary statistics, in dollars, are:

| Comparison | $m$ | $n$ | $\bar X$ | $\bar Y$ | $S_X$ | $S_Y$ |
|---|---|---|---|---|---|---|
| professors ($X$) vs assistant professors ($Y$) | $266$ | $67$ | $126\,772$ | $80\,776$ | $27\,719$ | $8\,174$ |
| men ($X$) vs women ($Y$) | $358$ | $39$ | $115\,090$ | $101\,002$ | $30\,437$ | $25\,922$ |

For professors versus assistant professors, $t_{331,0.025}=1.967$ and the equal-variance $95\%$ interval for $\mu_1-\mu_2$ is $[39\,255,\ 52\,737]$. But with $F_{66,265,0.975}=0.666$ and $F_{66,265,0.025}=1.436$, the $95\%$ interval for $\sigma_1^2/\sigma_2^2$ is $[7.66,\ 16.51]$, far from $1$: the equal-variance assumption is untenable, and the interval for the means is not appropriate. For men versus women, $t_{395,0.025}=1.966$ gives $[4\,131,\ 24\,045]$ for the difference of means, and the variance ratio interval $[0.81,\ 2.12]$ (from $F_{38,357,0.975}=0.591$ and $F_{38,357,0.025}=1.541$) contains $1$, so here the equal-variance interval is acceptable. The case of unequal variances is treated in §4.3.3.

## 4.3. Approximate Confidence Intervals

### 4.3.1. Large-Sample Intervals

Often the exact distribution of a natural pivot is complicated or unknown. Large-sample theory, above all the central limit theorem, then provides a limiting distribution that does not depend on the parameter. These approximate intervals are used in many data problems, and they are often nonparametric, not assuming the form of the population distribution.

**Definition 4.3.1 (Asymptotically Valid Confidence Interval)** A sequence of intervals $[\hat\theta_1(\boldsymbol{X}_n),\hat\theta_2(\boldsymbol{X}_n)]$, $\boldsymbol{X}_n=(X_1,\dots,X_n)$, is called an **asymptotically valid confidence interval** for $\theta$ with confidence level $1-\alpha$ if

$$
\liminf_{n\to\infty}\mathbb{P}_\theta\left(\hat\theta_1(\boldsymbol{X}_n)\le\theta\le\hat\theta_2(\boldsymbol{X}_n)\right)\ge1-\alpha\qquad\text{for all }\theta\in\Theta.
$$

The confidence level is then only approximately $1-\alpha$ for a finite sample, and the quality of the approximation, which usually depends on $\theta$, must be checked, for instance by simulation. The tools are the central limit theorem, the weak **law of large numbers** and Slutsky's theorem (Theorem 2.1.4), with $n$ assumed large enough for them to apply.

### 4.3.2. Bernoulli, Poisson and Exponential Populations

**Example 4.3.1 (Bernoulli Proportion)** The long-run scrap rate of a product is $\theta$, and a store will buy the products only if $\theta<0.01$. A random sample of $100$ products contains $3$ scraps, so the point estimate is $\hat\theta=\bar x=0.03$. What is a confidence interval?

Let $X_1,\dots,X_n$ be a random sample from $\mathrm{Ber}(\theta)$. Since $\mathbb{E}_\theta X_1=\theta$ and $\operatorname{Var}_\theta(X_1)=\theta(1-\theta)$, the central limit theorem gives

$$
T=\frac{\sqrt n(\bar X_n-\theta)}{\sqrt{\theta(1-\theta)}}\xrightarrow{d}\mathcal{N}(0,1),
$$

a limiting distribution free of $\theta$, so $T$ serves as an approximate pivot, and $\mathbb{P}_\theta(|T|\le z_{\alpha/2})\approx1-\alpha$ for large $n$.

*Method 1: solving the quadratic inequality.* The inequality $|T|\le z_{\alpha/2}$ is equivalent to $n(\bar X_n-\theta)^2\le z_{\alpha/2}^2\theta(1-\theta)$, that is,

$$
\theta^2(n+z_{\alpha/2}^2)-\theta(2n\bar X_n+z_{\alpha/2}^2)+n\bar X_n^2\le0,
$$

which holds exactly for $c_1\le\theta\le c_2$ with

$$
c_{1,2}=\frac n{n+z_{\alpha/2}^2}\left[\bar X_n+\frac{z_{\alpha/2}^2}{2n}\mp z_{\alpha/2}\sqrt{\frac{\bar X_n(1-\bar X_n)}n+\frac{z_{\alpha/2}^2}{4n^2}}\right].
$$

So $[c_1(\boldsymbol{X}),c_2(\boldsymbol{X})]$ is a confidence interval with level approximately $1-\alpha$; it is known as the Wilson score interval.

*Method 2: replacing the variance.* The interval of Method 1 is somewhat complicated, and in other problems the inequality $|T|\le z_{\alpha/2}$ may have no closed-form solution. By the weak law of large numbers, the denominator can be replaced by a consistent estimate. Here

$$
S_n^2=\frac1n\sum_{i=1}^n(X_i-\bar X_n)^2=\frac1n\sum_{i=1}^nX_i^2-\bar X_n^2=\bar X_n-\bar X_n^2=\bar X_n(1-\bar X_n)\xrightarrow{p}\theta(1-\theta),
$$

using $X_i^2=X_i$, so by Slutsky's theorem

$$
\frac{\sqrt n(\bar X_n-\theta)}{\sqrt{\bar X_n(1-\bar X_n)}}\xrightarrow{d}\mathcal{N}(0,1),\qquad\mathbb{P}_\theta\left(-z_{\alpha/2}\le\frac{\sqrt n(\bar X_n-\theta)}{\sqrt{\bar X_n(1-\bar X_n)}}\le z_{\alpha/2}\right)\approx1-\alpha.
$$

This leads to the confidence interval, with confidence coefficient approximately $1-\alpha$,

$$
\left[\bar X_n-z_{\alpha/2}\sqrt{\frac{\bar X_n(1-\bar X_n)}n},\ \bar X_n+z_{\alpha/2}\sqrt{\frac{\bar X_n(1-\bar X_n)}n}\right]=\bar X_n\pm z_{\alpha/2}\sqrt{\frac{\bar X_n(1-\bar X_n)}n},
$$

called the Wald interval, and to the approximate lower and upper confidence limits $\bar X_n-z_\alpha\sqrt{\bar X_n(1-\bar X_n)/n}$ and $\bar X_n+z_\alpha\sqrt{\bar X_n(1-\bar X_n)/n}$.

For the scrap rate, the $95\%$ Wald interval is $[-0.34\%,\ 6.34\%]$, the $95\%$ lower confidence limit is $0.19\%$ and the $95\%$ upper confidence limit is $5.81\%$. The upper limit is far above $1\%$, so the data do not show that $\theta<0.01$. The Wald interval also extends below $0$: with $\theta$ near $0$ and only $3$ scraps, the normal approximation with an estimated variance is poor. The Wilson interval of Method 1 avoids this; it is $[1.03\%,\ 8.45\%]$ here and its coverage is much closer to the nominal level for small $n\theta$, as the figure below shows.

**Example 4.3.2 (Poisson Mean)** For a random sample from $\mathrm{Poi}(\theta)$, $\mathbb{E}_\theta X_1=\operatorname{Var}_\theta(X_1)=\theta$. As in the previous example,

$$
\frac{\sqrt n(\bar X_n-\theta)}{\sqrt\theta}\xrightarrow{d}\mathcal{N}(0,1)\qquad\text{and}\qquad\frac{\sqrt n(\bar X_n-\theta)}{\sqrt{\bar X_n}}\xrightarrow{d}\mathcal{N}(0,1),
$$

and the second leads to the interval $\bar X_n\pm z_{\alpha/2}\sqrt{\bar X_n/n}$ with confidence coefficient approximately $1-\alpha$.

**Example 4.3.3 (Exponential Mean)** Let $X_1,\dots,X_n$ be a random sample from the exponential distribution with mean $\theta$, density $f(x;\theta)=\frac1\theta\mathrm{e}^{-x/\theta}$, $x>0$, that is, $\mathrm{Exp}(1/\theta)$. Then $\mathbb{E}_\theta X_1=\theta$ and $\operatorname{Var}_\theta(X_1)=\theta^2$, so

$$
\frac{\sqrt n(\bar X_n-\theta)}\theta\xrightarrow{d}\mathcal{N}(0,1)\qquad\text{and}\qquad\frac{\sqrt n(\bar X_n-\theta)}{\bar X_n}\xrightarrow{d}\mathcal{N}(0,1),
$$

and the approximate interval is $\bar X_n\pm z_{\alpha/2}\bar X_n/\sqrt n$. In a simulation with $\theta=1$, $\alpha=0.05$ and $n=100$, $93.8\%$ of $1000$ such intervals covered $\theta$, close to $0.95$, and the coverage approaches $0.95$ as $n$ grows. Compared with the exact interval of Example 4.2.5, $\left[\frac{2n\bar X_n}{\chi^2_{2n,\alpha/2}},\frac{2n\bar X_n}{\chi^2_{2n,1-\alpha/2}}\right]$, the approximate interval is symmetric about $\bar X_n$ although the sampling distribution of $\bar X_n$ is right-skewed, and its coverage falls short of the nominal level for small $n$. When an exact pivot is available it is preferable; the approximate interval is the fallback when it is not.

![Coverage probabilities of nominal 95% intervals. Left: Bernoulli proportion with theta = 0.03, exact coverage of the Wald and Wilson intervals as functions of n; the Wald interval undercovers badly and erratically. Right: exponential mean, simulated coverage (4000 samples per n) of the approximate interval x_bar +- 1.96 x_bar / sqrt(n) and the exact chi-square interval.](./plots/approximate-coverage.py)

### 4.3.3. The Behrens–Fisher Problem

**Example 4.3.4 (Difference of Means, Unequal Variances)** Return to two independent normal samples, now with $\sigma_1^2\ne\sigma_2^2$, both unknown. We have

$$
\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sqrt{\sigma_1^2/m+\sigma_2^2/n}}\sim\mathcal{N}(0,1),\qquad\frac{(m-1)S_X^2}{\sigma_1^2}+\frac{(n-1)S_Y^2}{\sigma_2^2}\sim\chi^2_{m+n-2},
$$

but unlike the equal-variance case the unknown variances do not cancel, and there is no simple exact pivot. Finding an exact confidence interval for $\mu_1-\mu_2$ in this situation, especially when $m$ and $n$ are not large, is the *Behrens–Fisher problem*, posed by W. Behrens (1929) and studied by R. A. Fisher, H. Scheffé, B. L. Welch and many others.

If both $m$ and $n$ are large, replacing the variances by their estimates and applying the central limit theorem and Slutsky's theorem gives

$$
Z=\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sqrt{S_X^2/m+S_Y^2/n}}\xrightarrow{d}\mathcal{N}(0,1)\qquad(m,n\to\infty),
$$

and the approximate interval with level $1-\alpha$,

$$
(\bar X-\bar Y)\pm z_{\alpha/2}\sqrt{\frac{S_X^2}m+\frac{S_Y^2}n}.
$$

This argument does not use normality: it requires only finite variances, so the interval is valid for large samples from any two populations.

For moderate sample sizes, Welch (1938, 1947) proposed approximating the distribution of

$$
T_*=\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sqrt{S_X^2/m+S_Y^2/n}}
$$

under normality by a $t_r$ distribution. The variance estimate $S_X^2/m+S_Y^2/n$ is matched to a scaled $\chi^2_r$ by its first two moments, which gives the degrees of freedom

$$
r=\frac{\left(\frac{S_X^2}m+\frac{S_Y^2}n\right)^2}{\frac{S_X^4}{m^2(m-1)}+\frac{S_Y^4}{n^2(n-1)}}
$$

(the Welch–Satterthwaite formula; $\min(m,n)-1\le r\le m+n-2$), rounded to the nearest integer in tables or used as it is in software. The approximate interval is

$$
(\bar X-\bar Y)\pm t_{r,\alpha/2}\sqrt{\frac{S_X^2}m+\frac{S_Y^2}n}.
$$

This Welch interval is what R's `t.test` reports by default (`var.equal = FALSE`), and it is recommended over the pooled interval unless the variances are known to be equal.

For the professor salaries (Example 4.2.8), professors versus assistant professors give: equal-variance interval $[39\,255,\ 52\,737]$; normal approximation $[42\,133,\ 49\,860]$; and Welch's interval with $r=324.3$, $[42\,118,\ 49\,874]$. The last two agree, and both differ markedly from the equal-variance interval, which was shown inappropriate. For men versus women, the normal approximation gives about $[5\,354,\ 22\,822]$, close to the equal-variance interval $[4\,131,\ 24\,045]$, as expected when the variance ratio is compatible with $1$.

## 4.4. Confidence Regions

### 4.4.1. Mean and Variance of a Normal Population

**Example 4.4.1** Let $X_1,\dots,X_n$ be a random sample from $\mathcal{N}(\mu,\sigma^2)$. We construct a confidence region for $\boldsymbol{\theta}=(\mu,\sigma^2)$ with confidence coefficient $1-\alpha$. With $S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2$,

$$
\frac{\sqrt n(\bar X-\mu)}\sigma\sim\mathcal{N}(0,1),\qquad\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1},
$$

and the two are independent. Choose $c>0$ with $\mathbb{P}(-c\le Z\le c)=\sqrt{1-\alpha}$ for $Z\sim\mathcal{N}(0,1)$, which determines $c$ uniquely, and $0<a<b$ with $\mathbb{P}(a\le\chi^2_{n-1}\le b)=\sqrt{1-\alpha}$. Then for all $\boldsymbol{\theta}$,

$$
\mathbb{P}_{\boldsymbol{\theta}}\left(-c\le\frac{\sqrt n(\bar X-\mu)}\sigma\le c\right)=\mathbb{P}_{\boldsymbol{\theta}}\left((\mu-\bar X)^2\le\frac{c^2\sigma^2}n\right)=\sqrt{1-\alpha},
$$

$$
\mathbb{P}_{\boldsymbol{\theta}}\left(a\le\frac{(n-1)S^2}{\sigma^2}\le b\right)=\mathbb{P}_{\boldsymbol{\theta}}\left(\frac{(n-1)S^2}b\le\sigma^2\le\frac{(n-1)S^2}a\right)=\sqrt{1-\alpha},
$$

and by independence

$$
\mathbb{P}_{\boldsymbol{\theta}}\left((\mu-\bar X)^2\le\frac{c^2}n\sigma^2,\ \frac{(n-1)S^2}b\le\sigma^2\le\frac{(n-1)S^2}a\right)=\sqrt{1-\alpha}\cdot\sqrt{1-\alpha}=1-\alpha.
$$

In fact $c=z_\gamma$ with $\gamma=(1-\sqrt{1-\alpha})/2$, and splitting the probability $1-\sqrt{1-\alpha}$ equally between the two tails of the $\chi^2$ distribution gives $b=\chi^2_{n-1,\gamma}$ and $a=\chi^2_{n-1,1-\gamma}$. The confidence region is

$$
(\mu-\bar X)^2\le\frac{z_\gamma^2}n\sigma^2,\qquad\frac1{\chi^2_{n-1,\gamma}}\sum_{i=1}^n(X_i-\bar X)^2\le\sigma^2\le\frac1{\chi^2_{n-1,1-\gamma}}\sum_{i=1}^n(X_i-\bar X)^2,\qquad\gamma=\frac{1-\sqrt{1-\alpha}}2.
$$

In the $(\mu,\sigma^2)$ plane it is the part of the interior of the parabola $(\mu-\bar x)^2=c^2\sigma^2/n$ between two horizontal lines.

![The 95% confidence region for (mu, sigma^2) of Example 4.4.1 from a simulated sample of size 30 from N(0, 1): the shaded set inside the parabola (mu - x_bar)^2 = c^2 sigma^2 / n and between the two horizontal lines; the cross marks the true parameter.](./plots/normal-confidence-region.py)

### 4.4.2. Several Means: Šidák and Bonferroni Corrections

**Example 4.4.2 (Independent Samples)** Consider the mean salaries $(\mu_1,\mu_2)$ of professors and assistant professors in Example 4.2.8. Let $X_1,\dots,X_m$ be the professors' salaries and $Y_1,\dots,Y_n$ the assistant professors' salaries, with $X_i\sim\mathcal{N}(\mu_1,\sigma_1^2)$ and $Y_j\sim\mathcal{N}(\mu_2,\sigma_2^2)$, the two samples being independent. The *Šidák correction* constructs confidence intervals for $\mu_1$ and $\mu_2$ separately, each with confidence level $\sqrt{1-\alpha}$; with $\gamma=(1-\sqrt{1-\alpha})/2$,

$$
\left[\bar X-t_{m-1,\gamma}\frac{S_X}{\sqrt m},\ \bar X+t_{m-1,\gamma}\frac{S_X}{\sqrt m}\right]\times\left[\bar Y-t_{n-1,\gamma}\frac{S_Y}{\sqrt n},\ \bar Y+t_{n-1,\gamma}\frac{S_Y}{\sqrt n}\right]
$$

is, by independence, a confidence region with level $\sqrt{1-\alpha}\cdot\sqrt{1-\alpha}=1-\alpha$. For $k$ independent samples, intervals of level $(1-\alpha)^{1/k}$ each give a joint level $1-\alpha$.

For $\alpha=0.05$, $\gamma=0.0127$ and each interval has level $1-2\gamma=0.9747$. The separate $95\%$ intervals are $[123\,426,\ 130\,118]$ for $\mu_1$ and $[78\,782,\ 82\,770]$ for $\mu_2$, but their product has joint level only $0.95^2\approx0.90$; the Šidák $95\%$ region is

$$
[122\,950,\ 130\,595]\times[78\,491,\ 83\,061].
$$

**Example 4.4.3 (Dependent Samples)** For a random sample of $n=500$ eighteen-year-old Hong Kong children, let $(X_i,Y_i)$ be weight and height, and suppose $(X,Y)$ follows a bivariate normal distribution with means $(\mu_1,\mu_2)$, variances $\sigma_1^2,\sigma_2^2$ and correlation $\rho$; now $X$ and $Y$ are dependent. The point estimates are $\hat\mu_1=\bar X=126.7$, $\hat\mu_2=\bar Y=67.9$ (that is, $57.5$ kg and $172.5$ cm), $\hat\sigma_1^2=S_{nX}^2=143.3$, $\hat\sigma_2^2=S_{nY}^2=3.9$ and $\hat\rho=0.48$ (Example 3.2.2). To construct a $95\%$ confidence region for $(\mu_1,\mu_2)$, the *Bonferroni correction* constructs intervals for $\mu_1$ and $\mu_2$ separately with confidence level $1-\alpha/2$ each. Since

$$
\frac{\sqrt n(\bar X-\mu_1)}{S_X}\sim t_{n-1},\qquad\frac{\sqrt n(\bar Y-\mu_2)}{S_Y}\sim t_{n-1},
$$

we have $\mathbb{P}\left(\left\lvert\frac{\sqrt n(\bar X-\mu_1)}{S_X}\right\rvert\le t_{n-1,\alpha/4}\right)=1-\frac\alpha2$, and the same for $Y$. By the union bound,

$$
1-\mathbb{P}\left(\left\lvert\frac{\sqrt n(\bar X-\mu_1)}{S_X}\right\rvert\le t_{n-1,\alpha/4},\ \left\lvert\frac{\sqrt n(\bar Y-\mu_2)}{S_Y}\right\rvert\le t_{n-1,\alpha/4}\right)\le\mathbb{P}\left(\left\lvert\frac{\sqrt n(\bar X-\mu_1)}{S_X}\right\rvert>t_{n-1,\alpha/4}\right)+\mathbb{P}\left(\left\lvert\frac{\sqrt n(\bar Y-\mu_2)}{S_Y}\right\rvert>t_{n-1,\alpha/4}\right)=\frac\alpha2+\frac\alpha2=\alpha,
$$

whatever the dependence between $X$ and $Y$. Hence the (conservative) $1-\alpha$ confidence region for $(\mu_1,\mu_2)$ is

$$
\left[\bar X-t_{n-1,\alpha/4}\frac{S_X}{\sqrt n},\ \bar X+t_{n-1,\alpha/4}\frac{S_X}{\sqrt n}\right]\times\left[\bar Y-t_{n-1,\alpha/4}\frac{S_Y}{\sqrt n},\ \bar Y+t_{n-1,\alpha/4}\frac{S_Y}{\sqrt n}\right].
$$

For the children, the $95\%$ region is $[125.5,\ 127.9]$ lb for the mean weight times $[67.75,\ 68.15]$ in for the mean height. The Bonferroni correction generalizes immediately to $(\mu_1,\dots,\mu_k)$, using level $1-\alpha/k$ for each interval, and it handles different sample sizes with no extra effort. A less conservative refinement, used in multiple testing, is the Holm–Bonferroni method.

For the professor salaries, the Bonferroni $95\%$ region is $[122\,941,\ 130\,603]\times[78\,485,\ 83\,067]$, slightly larger than the Šidák region $[122\,950,\ 130\,595]\times[78\,491,\ 83\,061]$. The comparison is general: the Šidák correction requires independence (more generally, positive dependence of a suitable kind) and is slightly less conservative, since $(1-\alpha)^{1/k}<1-\alpha/k$; the Bonferroni correction is valid for both independent and dependent estimators.

## Summary

- A confidence interval with level $1-\alpha$ covers the parameter with probability at least $1-\alpha$ for every parameter value; the probability refers to the random interval before sampling, not to the observed interval. Reliability (the confidence coefficient) and precision (the expected length) compete, and Neyman's principle fixes the first and optimizes the second.
- The pivotal quantity method transforms a good estimator into a variable whose distribution is free of the parameter, then inverts a probability statement about it. The standard pivots are:

| Model | Target | Pivot |
|---|---|---|
| $\mathcal{N}(\mu,\sigma^2)$ | $\mu$ | $\sqrt n(\bar X-\mu)/\sigma\sim\mathcal{N}(0,1)$ or $\sqrt n(\bar X-\mu)/S\sim t_{n-1}$ |
| $\mathcal{N}(\mu,\sigma^2)$ | $\sigma^2$ | $nS_\mu^2/\sigma^2\sim\chi^2_n$ or $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$ |
| $\mathrm{U}(0,\theta)$ | $\theta$ | $X_{(n)}/\theta$, density $ny^{n-1}$ on $[0,1]$ |
| $\mathrm{Exp}(\lambda)$ | $\lambda$ | $2\lambda n\bar X\sim\chi^2_{2n}$ |
| two normal samples, $\sigma_1^2=\sigma_2^2$ | $\mu_1-\mu_2$ | $\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_w\sqrt{1/m+1/n}}\sim t_{m+n-2}$ |
| two normal samples | $\sigma_1^2/\sigma_2^2$ | $\frac{S_Y^2/\sigma_2^2}{S_X^2/\sigma_1^2}\sim F_{n-1,m-1}$ |

- Approximate intervals come from the central limit theorem with the variance either kept in the pivot (Wilson) or replaced by a consistent estimate (Wald); their coverage must be checked, and exact pivots are preferable when available. For unequal variances, Welch's interval is the standard solution of the Behrens–Fisher problem.
- Joint regions for several parameters can be built as rectangles: Šidák's correction for independent estimators, Bonferroni's for arbitrary dependence.
