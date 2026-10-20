---
title: The Bootstrap
description: Bootstrap samples and the bootstrap principle; when resampling works (Hadamard differentiability); bootstrap estimates of standard error and bias; normal, basic, percentile and BCa confidence intervals; bootstrap hypothesis tests; the parametric bootstrap.
---

The **bootstrap** quantifies the uncertainty of an estimator when its **sampling distribution** cannot be derived. Its three main uses are to estimate the bias and the **standard error** of an estimator, to construct a **confidence interval** for a parameter, and to test a hypothesis about it. The idea is simple: treat the observed sample as if it were the population, resample from it with replacement, and recompute the statistic on each resample. Formally, the unknown distribution function $F$ is replaced by the **empirical distribution function** $F_n$, and the sampling distribution of the statistic under $F$ is approximated by its distribution under $F_n$, which is computed by **Monte Carlo methods** ([3.1.12](/3.1.12)). The bootstrap of regression models (resampling cases or residuals) appeared in [3.3.12](/3.3.12); this chapter develops the general method and its theory. It uses the inverse transform view of resampling ([3.1.7](/3.1.7)) and the interval estimation of [3.2.4](/3.2.4); the random number generators behind every resample are the subject of [3.5.8](/3.5.8), and resampling tests are continued in nonparametric statistics ([3.6](/3.6)).

## 7.1. Preliminaries: Sampling Variability

Statistical inference uses the information in a sample to learn about the whole population, and asks how accurate the conclusions are. A frequentist regards a parameter as a fixed, usually unknown, number, whereas a sample statistic varies from sample to sample. How well a statistic estimates the parameter depends on this variation: the closer the values of the statistic are from sample to sample, the more accurate the estimate.

**Example 7.1.1** The US Census states that $27.5\%$ of US adults aged at least 25 have a bachelor's degree or higher. In a random sample of $200$ such residents, $58$ have a degree. The population parameter is $p=0.275$ and the sample statistic is $\hat p=58/200=0.29$. Drawing $10\,000$ samples of size $200$ from the population and computing $\hat p$ for each gives an approximation of the **sampling distribution** of $\hat p$: the distribution of the statistic over samples of the same size from the same population.

The **standard error** $\operatorname{se}(\hat\theta)$ of a statistic is the standard deviation of its sampling distribution, a typical distance between the statistic and the parameter. A small standard error means that the statistic varies little from sample to sample. The sample size matters: as $n$ grows the variability decreases and the statistic tends to be closer to the parameter.

An interval estimate has the form "point estimate $\pm$ margin of error"; the margin of error reflects the precision of the point estimate. A **confidence interval** is computed from the data by a method that captures the parameter for a specified proportion of all samples, the **confidence level**. The parameter is fixed; it is the interval that varies. If the sampling distribution is roughly symmetric and bell-shaped, a $95\%$ interval is approximately

$$
\text{statistic}\pm 2\operatorname{se}.
$$
For a normal sampling distribution the factor $2$ comes from the 68–95–99.7 rule (more precisely $z_{0.025}=1.96$). Without normality, **Chebyshev's inequality** $\mathbb{P}(\lvert X-\mu\rvert\ge k\sigma)\le 1/k^2$ only guarantees $95\%$ coverage for $k=\sqrt{20}\approx4.47$.

| Term | Meaning |
|---|---|
| margin of error | the amount added to and subtracted from the estimate in an interval |
| standard error | the standard deviation of the statistic over repeated samples of the same size |
| sample standard deviation | the standard deviation of the individual values in one sample |

In simple cases the sampling distribution and the standard error can be derived mathematically: the mean of a normal sample is normal. In most real problems the distribution is too complicated, and we cannot take thousands of samples when only one is available. The bootstrap approximates the sampling distribution and the standard error using only the information in the one sample; bootstrap methods are a class of nonparametric Monte Carlo methods that estimate distributional characteristics of a statistic by resampling.

## 7.2. Bootstrap Basics

The name comes from the phrase "to pull oneself up by one's bootstraps", traced to Raspe's *The Surprising Adventures of Baron Munchausen*, in which the Baron, at the bottom of a deep lake, saves himself by pulling on his own bootstraps. Ideally we would sample repeatedly from the population; the key idea is to pretend, for the moment, that the population consists of many copies of the observed sample. Sampling from this hypothetical population is the same as sampling with replacement from the sample itself.

### 7.2.1. Bootstrap Samples and the Bootstrap Principle

**Definition 7.2.1 (Bootstrap Sample)** Let $\boldsymbol{x}=(x_1,\dots,x_n)$ be an observed random sample from a distribution with distribution function $F$. If $X^*$ is selected at random from $\boldsymbol{x}$, then

$$
\mathbb{P}(X^*=x_i)=\frac1n,\qquad i=1,\dots,n.
$$
Sampling $n$ times with replacement from $\boldsymbol{x}$ gives i.i.d. random variables $X_1^*,\dots,X_n^*$, uniformly distributed on the set $\boldsymbol{x}$; $\boldsymbol{x}^*=(x_1^*,\dots,x_n^*)$ is called a **bootstrap sample**. It has the same size as the original sample.

The distribution function of $X^*$ is the **empirical distribution function** $F_n(x)=\frac1n\sum_{i=1}^n\boldsymbol{1}\{x_i\le x\}$, an estimator of $F$ (by the **Glivenko–Cantelli theorem** it converges to $F$ uniformly, almost surely). This justifies the *bootstrap principle*: since $F_n\approx F$, it is reasonable to assume that $X^*\overset{d}{\approx}X$ and that a statistic satisfies $T(\boldsymbol{X}^*)\overset{d}{\approx}T(\boldsymbol{X})$. In other words, the relation between $F_n$ and the bootstrap world mimics the relation between $F$ and the real world. Sampling from $F_n$ is exactly **inverse transform sampling** from a step function (see [the last example of §7.3 in 3.1.7](/3.1.7#ex-7.3.1)).

### 7.2.2. The Bootstrap Distribution

**Algorithm 7.2.1 (Nonparametric Bootstrap)** Let $\theta$ be the parameter of interest and $\hat\theta=T(\boldsymbol{x})$ an estimator of it.

1. For $b=1,\dots,B$: draw the $b$-th bootstrap sample $\boldsymbol{x}^{*(b)}=(x_1^*,\dots,x_n^*)$ by sampling with replacement from $x_1,\dots,x_n$, and compute the $b$-th replicate $\hat\theta^{(b)}=T(\boldsymbol{x}^{*(b)})$.
2. The empirical distribution of $\hat\theta^{(1)},\dots,\hat\theta^{(B)}$ is the bootstrap estimate of the distribution of $\hat\theta$.

**Definition 7.2.2 (Bootstrap Distribution)** The statistic computed from a bootstrap sample is a bootstrap statistic, or bootstrap replicate $\hat\theta^*$; the distribution of the replicates over many bootstrap samples is the **bootstrap distribution** of $\hat\theta$.

If the original sample is a random sample from the population, the bootstrap distribution generally approximates the sampling distribution well in shape and spread. It is, however, centered at the sample statistic $\hat\theta$, not at the parameter $\theta$, so it estimates how far $\hat\theta$ typically is from $\theta$ but cannot move $\hat\theta$ closer to $\theta$. For example, the means of $1000$ bootstrap samples of $500$ commute times spread over about $\pm3$ minutes around the sample mean, so we are confident that the sample mean is within about three minutes of the population mean.

In R, the loop is a few lines; the package `boot` wraps it, requiring a statistic of the form `function(data, indices)`:

```r
# generic bootstrap of a statistic theta_hat = stat(x)
B <- 2000; n <- length(x)
theta_star <- numeric(B)
for (b in 1:B) {
  xb <- sample(x, size = n, replace = TRUE)   # bootstrap sample
  theta_star[b] <- stat(xb)                   # bootstrap replicate
}
hist(theta_star)                              # always look at the bootstrap distribution

library(boot)
obj <- boot(data = x, statistic = function(x, i) stat(x[i]), R = B)
```

### 7.2.3. When Does the Bootstrap Work?

A larger sample makes the bootstrap more accurate, but the bootstrap does not always work. One should always look at a plot of the bootstrap distribution: if it is poorly behaved, for example heavily skewed or broken into isolated clumps of values, the intervals it produces deserve little confidence. For most statistics in common use the bootstrap distribution behaves well. The theory below (optional) explains when and why.

Resampling works when the statistic is "well behaved" as $F_n$ fluctuates slightly around $F$. Write the statistic as a functional, $T(\boldsymbol{X})=\phi(F_n)$, and the parameter as $\phi(F)$; the bootstrap needs a derivative of $\phi$ with respect to a function. Of the possible notions on an infinite-dimensional space, the Fréchet derivative (uniform over all bounded directions) is too strong: the median and other quantiles are not Fréchet differentiable. The Gâteaux derivative (along fixed straight lines) is too weak to carry a central limit theorem through $\phi$. The right compromise is the following.

**Definition 7.2.3 (Hadamard Differentiability)** Let $\mathcal{D}$ be a normed space of functions (for distribution functions, bounded functions with the supremum norm). A map $\phi\colon\mathcal{D}_\phi\subseteq\mathcal{D}\to\mathbb{R}$ is **Hadamard differentiable** at $F$ if there is a continuous linear map $\phi'_F\colon\mathcal{D}\to\mathbb{R}$ such that

$$
\frac{\phi(F+t h_t)-\phi(F)}{t}\to\phi'_F(h)\qquad\text{for all } t\to0,\ h_t\to h \text{ with } F+th_t\in\mathcal{D}_\phi.
$$
Equivalently, the Fréchet approximation holds uniformly on compact sets of directions $h$.

Compact sets are enough because the random fluctuation of the empirical distribution function is itself "compact" in the limit. By Donsker's theorem $\sqrt n(F_n-F)$ converges in distribution to a Brownian bridge $G_F$. The limit is tight (Prohorov's theorem): for every $\varepsilon>0$ its sample paths lie in a fixed compact set of continuous functions with probability at least $1-\varepsilon$. A derivative that controls only such well-behaved directions therefore suffices.

**Theorem 7.2.1 (Functional Delta Method)** If $\phi$ is Hadamard differentiable at $F$ (tangentially to the continuous functions), then

$$
\sqrt n\bigl(\phi(F_n)-\phi(F)\bigr)\xrightarrow{d}\phi'_F(G_F),
$$
a normal distribution $\mathcal{N}(0,\sigma^2)$ with $\sigma^2=\operatorname{Var}(\phi'_F(G_F))$. Moreover the nonparametric bootstrap is consistent: conditionally on the data, $\sqrt n(\phi(F_n^*)-\phi(F_n))$ converges in distribution to the same limit in probability, where $F_n^*$ is the empirical distribution function of a bootstrap sample.

This is the infinite-dimensional analogue of the **delta method**. Hadamard differentiability is a sufficient condition for the bootstrap, not a necessary one, but it explains the three typical situations.

| Situation | Examples | Behavior of the standard bootstrap |
|---|---|---|
| smooth (essentially linear) functionals, Fréchet differentiable | sample mean $\bar X$, least squares coefficients $\hat{\boldsymbol\beta}$ | works well |
| functionals with a kink at the sample level, Hadamard differentiable when $F$ is continuous with positive density at the target | **sample median**, other quantiles, quantile regression coefficients | works for large $n$ if $F$ has a density with $f(M)=F'(M)>0$ at the median $M$; for small $n$ the bootstrap distribution is lumpy |
| not Hadamard differentiable at all | extremes $\max X_i$, $\min X_i$; **Lasso** coefficients whose true value is $0$ | fails; the limit distribution is not normal |

For the median, the indicator $\boldsymbol{1}\{X\le x\}$ makes the sample functional non-smooth; integration against a continuous $F$ with $f(M)>0$ smooths the kink at the population level. For the maximum, the statistic is driven by a single boundary point, and for the Lasso the penalty $\lambda\lvert\beta\rvert$ has a corner at $0$ that the data cannot smooth out.

**Example 7.2.1** Let $X_1,\dots,X_n$ be i.i.d. $\mathrm{U}(0,\theta)$ and $\hat\theta=X_{(n)}$. A bootstrap sample reproduces the sample maximum whenever it contains $x_{(n)}$, so

$$
\mathbb{P}^*\bigl(\hat\theta^*=\hat\theta\bigr)=1-\Bigl(1-\frac1n\Bigr)^n\to1-\mathrm{e}^{-1}\approx0.632,
$$
whereas $\mathbb{P}(\hat\theta=\theta)=0$ and $n(\theta-X_{(n)})/\theta$ converges to $\mathrm{Exp}(1)$. The bootstrap distribution has an atom of mass about $0.63$ and cannot approximate the continuous sampling distribution.

![Bootstrap distributions for one sample of size 50 from U(0, 1). The bootstrap means (left) form a smooth bell-shaped histogram; the bootstrap maxima (right) take only the few largest observed values, with about 63% of the mass at the sample maximum itself.](./plots/bootstrap-mean-vs-max.py)

How to diagnose a clumpy bootstrap plot: a large $n$ does not automatically fix the standard bootstrap.

- First ask whether the functional is Hadamard differentiable at the population level. If not (maximum, minimum, Lasso), the standard bootstrap fails at the root.
- For functionals that are differentiable only when $F$ is continuous (median), ask whether the data come from a discrete population or have many ties. If yes, the differentiability fails by discreteness; if no, $n$ is too small to smooth the sample-level kinks, and more data help.

Two remedies exist for non-smooth statistics.

- The *smoothed bootstrap* adds to every resampled point a small continuous noise, for example $\mathcal{N}(0,h^2)$ with bandwidth $h$. This is sampling from a **kernel density estimator** $\tilde f_n$ instead of the step function $F_n$; the continuous density $\tilde f_n>0$ restores differentiability.
- The *m-out-of-n bootstrap* draws resamples of size $m$ instead of $n$, with $m\to\infty$ and $m/n\to0$. It does not rely on a first-order expansion of the functional; the slower rate of convergence absorbs the discrete jumps. It is consistent under much weaker conditions, including for the maximum.

## 7.3. Applications

### 7.3.1. Standard Error

**Definition 7.3.1 (Bootstrap Standard Error)** The bootstrap estimate of the **standard error** of an estimator $\hat\theta$ is the sample standard deviation of the bootstrap replicates $\hat\theta^{(1)},\dots,\hat\theta^{(B)}$:

$$
\widehat{\operatorname{se}}(\hat\theta^*)=\sqrt{\frac{1}{B-1}\sum_{b=1}^B\bigl(\hat\theta^{(b)}-\bar\theta^*\bigr)^2},\qquad \bar\theta^*=\frac1B\sum_{b=1}^B\hat\theta^{(b)}.
$$

According to Efron and Tibshirani, the number of replicates needed for a good estimate of the standard error is not large: $B=50$ is usually enough and $B>200$ is rarely necessary. Much larger $B$ (at least $1000$) is needed for confidence intervals, which depend on the tails of the bootstrap distribution.

**Example 7.3.1** The data set `law` in the R package `bootstrap` contains the average LSAT score and average GPA of $15$ law schools, a random sample from the $82$ schools in `law82`. The sample correlation is $r=0.776$ (the population value over all $82$ schools is $0.76$). Resampling the $15$ pairs (not the two variables separately, which would destroy the correlation) gives a bootstrap standard error of about $0.13$; its exact value varies with the random seed.

```r
library(bootstrap)   # data sets law and law82
B <- 200; n <- nrow(law)
R <- numeric(B)
for (b in 1:B) {
  i <- sample(1:n, size = n, replace = TRUE)   # resample whole cases
  R[b] <- cor(law$LSAT[i], law$GPA[i])
}
cor(law$LSAT, law$GPA)   # theta_hat = 0.776
sd(R)                    # bootstrap standard error, about 0.13

library(boot)
r <- function(x, i) cor(x[i, 1], x[i, 2])
boot(data = law, statistic = r, R = 2000)   # reports original, bias and std. error
```

### 7.3.2. Bias

**Definition 7.3.2 (Bias)** The **bias** of an estimator $\hat\theta$ of $\theta$ is $\operatorname{Bias}(\hat\theta)=\mathbb{E}[\hat\theta]-\theta$; if it is zero, $\hat\theta$ is an **unbiased estimator**. For example, the maximum likelihood estimator $\frac1n\sum_i(X_i-\bar X)^2$ of a variance is biased. The bootstrap estimate of bias replaces $\mathbb{E}[\hat\theta]$ by the mean of the replicates and $\theta$ by $\hat\theta$:

$$
\widehat{\operatorname{Bias}}(\hat\theta)=\frac1B\sum_{b=1}^B\hat\theta^{(b)}-\hat\theta=\bar\theta^*-\hat\theta.
$$

The bias-corrected estimate is $\hat\theta-\widehat{\operatorname{Bias}}(\hat\theta)=2\hat\theta-\bar\theta^*$. The correction adds variability, so it is worthwhile only when the bias is large compared with the standard error; a common rule of thumb ignores a bias smaller than $0.25\,\widehat{\operatorname{se}}$. Any of the intervals below can likewise be shifted by $\widehat{\operatorname{Bias}}(\hat\theta)$.

**Example 7.3.2** For the law school data the bootstrap bias of $r$ is small (about $-0.005$ to $-0.01$, depending on the run), negligible against the standard error $0.13$.

The data `patch` (package `bootstrap`) contain measurements of a hormone in the blood of $8$ subjects after wearing a placebo patch, an old patch and a new patch. The parameter of interest is

$$
\theta=\frac{\mathbb{E}(\text{new})-\mathbb{E}(\text{old})}{\mathbb{E}(\text{old})-\mathbb{E}(\text{placebo})}.
$$
The new and the old patch are considered bioequivalent if $\lvert\theta\rvert\le0.2$. With $y_i=\text{new}_i-\text{old}_i$ and $z_i=\text{old}_i-\text{placebo}_i$, the statistic is $\hat\theta=\bar y/\bar z=-0.0713$. Resampling the subjects gives a bias of about $0.007$ and a standard error of about $0.10$; the bias is small, $\lvert\widehat{\operatorname{Bias}}\rvert/\widehat{\operatorname{se}}<0.1$.

```r
library(bootstrap)
n <- nrow(patch); B <- 2000
theta_hat <- mean(patch$y) / mean(patch$z)
theta_b <- numeric(B)
for (b in 1:B) {
  i <- sample(1:n, size = n, replace = TRUE)   # resample subjects: keep (y, z) pairs
  theta_b[b] <- mean(patch$y[i]) / mean(patch$z[i])
}
bias <- mean(theta_b) - theta_hat
se <- sd(theta_b)
c(theta_hat = theta_hat, bias = bias, se = se, ratio = bias / se)
```

### 7.3.3. Bootstrap Confidence Intervals

Denote by $\hat\theta^*_q$ the (lower) $q$ quantile of the bootstrap distribution, $\mathbb{P}^*(\hat\theta^*\le\hat\theta^*_q)=q$, estimated by the corresponding sample quantile of the replicates, and by $z_{\alpha/2}=\Phi^{-1}(1-\alpha/2)$ the upper $\alpha/2$ quantile of $\mathcal{N}(0,1)$.

**Definition 7.3.3 (Normal Bootstrap Interval)** If $\hat\theta$ is (approximately) unbiased and normal, $\hat\theta\overset{\cdot}{\sim}\mathcal{N}(\theta,\operatorname{se}(\hat\theta)^2)$, the approximate $100(1-\alpha)\%$ **normal bootstrap interval** is

$$
\hat\theta\pm z_{\alpha/2}\,\widehat{\operatorname{se}}(\hat\theta^*).
$$

Typical cases are the sample mean (by the **central limit theorem**) and the coefficient $\hat\beta$ of a linear regression with i.i.d. normal errors. The function `boot.ci` centers this interval at the bias-corrected estimate $\hat\theta-\widehat{\operatorname{Bias}}$.

**Definition 7.3.4 (Basic Bootstrap Interval)** Let $a_q$ be the $q$ quantile of $\hat\theta-\theta$, so that $\mathbb{P}(\hat\theta-\theta\le a_q)=q$. Then $\mathbb{P}(\hat\theta-\theta>a_\alpha)=1-\alpha$, that is $\mathbb{P}(\theta<\hat\theta-a_\alpha)=1-\alpha$, and $(\hat\theta-a_{1-\alpha/2},\hat\theta-a_{\alpha/2})$ is an exact $100(1-\alpha)\%$ interval. The distribution of $\hat\theta-\theta$ is unknown; by the bootstrap principle it is approximated by that of $\hat\theta^*-\hat\theta$, whose $q$ quantile is $\hat\theta^*_q-\hat\theta$ because $q=\mathbb{P}^*(\hat\theta^*\le\hat\theta^*_q)=\mathbb{P}^*(\hat\theta^*-\hat\theta\le\hat\theta^*_q-\hat\theta)$. Substituting gives the **basic bootstrap interval** (also called the empirical bootstrap interval)

$$
\bigl(2\hat\theta-\hat\theta^*_{1-\alpha/2},\ 2\hat\theta-\hat\theta^*_{\alpha/2}\bigr).
$$

**Definition 7.3.5 (Percentile Interval)** The **percentile interval** takes the quantiles of the bootstrap distribution directly:

$$
\bigl(\hat\theta^*_{\alpha/2},\ \hat\theta^*_{1-\alpha/2}\bigr).
$$

The percentile interval is appealing for its simplicity, but it relies on the bootstrap distribution, based on one particular sample, being a good approximation of the true distribution of $\hat\theta$. It is transformation invariant: for a monotone $g$, the percentile interval for $g(\theta)$ is the image of that for $\theta$. Its weakness is median bias: if $\hat\theta$ is not median-unbiased, the interval is wrong with confidence.

**Definition 7.3.6 (BCa Interval)** The $100(1-\alpha)\%$ **bias-corrected and accelerated interval** (BCa interval) is $(\hat\theta^*_{\alpha_1},\hat\theta^*_{\alpha_2})$, with adjusted levels

$$
\alpha_1=\Phi\Bigl(\hat z_0+\frac{\hat z_0-z_{\alpha/2}}{1-\hat a(\hat z_0-z_{\alpha/2})}\Bigr),\qquad
\alpha_2=\Phi\Bigl(\hat z_0+\frac{\hat z_0+z_{\alpha/2}}{1-\hat a(\hat z_0+z_{\alpha/2})}\Bigr).
$$
Here the bias-correction factor $\hat z_0$ measures the median bias of the replicates, and the acceleration $\hat a$ measures the rate of change of the standard error with the parameter (a skewness), estimated from the jackknife replicates:

$$
\hat z_0=\Phi^{-1}\Bigl(\frac1B\sum_{b=1}^B\boldsymbol{1}\{\hat\theta^{(b)}<\hat\theta\}\Bigr),\qquad
\hat a=\frac{\sum_{i=1}^n(\hat\theta_{(\cdot)}-\hat\theta_{(i)})^3}{6\Bigl(\sum_{i=1}^n(\hat\theta_{(\cdot)}-\hat\theta_{(i)})^2\Bigr)^{3/2}},
$$
where $\hat\theta_{(i)}$ is the leave-one-out estimate computed without $x_i$ and $\hat\theta_{(\cdot)}=\frac1n\sum_{i=1}^n\hat\theta_{(i)}$.

The leave-one-out estimates $\hat\theta_{(1)},\dots,\hat\theta_{(n)}$ are the replicates of the *jackknife*, the older resampling method (Quenouille, Tukey) that recomputes the statistic $n$ times, each time deleting one observation. With $\hat z_0=\hat a=0$ we get $\alpha_1=\alpha/2$, $\alpha_2=1-\alpha/2$, and the BCa interval reduces to the percentile interval. The BCa interval keeps the transformation invariance of the percentile interval and corrects both the bias and the skewness: its coverage error is $O(n^{-1})$ (second-order accurate), against $O(n^{-1/2})$ for the normal, basic and percentile intervals. It is the method recommended for routine use, and one of the types computed by `boot.ci`; it needs a larger $B$ (say $B\ge1000$) because $\alpha_1,\alpha_2$ may lie far in the tails.

| Interval | Formula | When to use | Weakness |
|---|---|---|---|
| normal | $\hat\theta\pm z_{\alpha/2}\widehat{\operatorname{se}}$ | $n$ large and the limit distribution clearly normal (sample mean) | wrong if the distribution is asymmetric or $\hat\theta$ is biased |
| basic | $(2\hat\theta-\hat\theta^*_{1-\alpha/2},2\hat\theta-\hat\theta^*_{\alpha/2})$ | assumes the fluctuation of $\hat\theta-\theta$ is mirrored by that of $\hat\theta^*-\hat\theta$, no normality | reverses the quantiles, so under strong skewness it overcorrects in the wrong direction and may leave the parameter space |
| percentile | $(\hat\theta^*_{\alpha/2},\hat\theta^*_{1-\alpha/2})$ | skewed data but nearly unbiased estimator; transformation invariant | wrong with confidence under large median bias |
| BCa | $(\hat\theta^*_{\alpha_1},\hat\theta^*_{\alpha_2})$ | default in practice; corrects bias $\hat z_0$ and acceleration $\hat a$ | more computation (jackknife, large $B$) |

![Bootstrap distribution of the law school correlation (B = 2000) and four 95% intervals. The distribution is skewed to the left; the normal and basic intervals extend beyond the upper bound 1 of a correlation, whereas the percentile and BCa intervals respect it, and BCa shifts the interval further toward the long left tail.](./plots/law-correlation-bootstrap.py)

```r
library(boot)
r <- function(x, i) cor(x[i, 1], x[i, 2])
obj <- boot(data = law, statistic = r, R = 2000)
boot.ci(obj, type = c("norm", "basic", "perc", "bca"))

# bootstrap intervals for regression coefficients: cat heart weight on body weight
library(MASS); data(cats)
coefs <- function(d, i) coef(lm(Hwt ~ Bwt, data = d[i, ]))   # resample cases
obj2 <- boot(data = cats, statistic = coefs, R = 2000)
boot.ci(obj2, type = "bca", index = 2)                       # slope
```

### 7.3.4. Bootstrap Hypothesis Testing

Consider the one-sample problem: we observe $\boldsymbol{z}=(z_1,\dots,z_n)$ and test whether the population mean equals a given $\mu_0$, $H_0\colon\mu=\mu_0$ against $H_a\colon\mu\ne\mu_0$ (two-sided), with the test statistic

$$
T(\boldsymbol{z})=\frac{\bar z-\mu_0}{\widehat{\operatorname{se}}}=\frac{\bar z-\mu_0}{\hat\sigma/\sqrt n}.
$$
The **p-value** is the probability, under the null hypothesis, of a value at least as extreme as the observed one, $\mathbb{P}_{H_0}(\lvert T\rvert\ge\lvert T_{\mathrm{obs}}\rvert)$. The question is how to obtain the null distribution of $T$ from the observed sample. There are two ways.

1. Through a confidence interval: compute a bootstrap interval for $\mu$ and reject $H_0$ at level $\alpha$ if $\mu_0$ is outside the $100(1-\alpha)\%$ interval (the duality of tests and confidence intervals). For instance, when a drug is given to $8$ patients and the change in their condition is measured, the drug is declared ineffective at level $0.05$ if the $95\%$ bootstrap interval of the mean change covers $0$.
2. Through a p-value: shift the data so that the null hypothesis holds, and resample from the shifted data.

**Algorithm 7.3.1 (Bootstrap Test for One Mean)**

1. Shift the data: $\tilde z_i=z_i-\bar z+\mu_0$, $i=1,\dots,n$, so that $\tilde{\boldsymbol{z}}$ has mean $\mu_0$.
2. For $b=1,\dots,B$, draw a bootstrap sample from $\tilde{\boldsymbol{z}}$ and compute $\tilde T^{(b)}=\dfrac{\bar{\tilde z}^{(b)}-\mu_0}{\hat{\tilde\sigma}^{(b)}/\sqrt n}$.
3. The p-value is $\#\{b\colon\lvert\tilde T^{(b)}\rvert\ge\lvert T_{\mathrm{obs}}\rvert\}/B$.

The statistic must be recomputed from each resample with its own standard deviation $\hat{\tilde\sigma}^{(b)}$; resampling the studentized statistic is more accurate than resampling $\bar z$ alone. A common refinement reports $(1+\#\{\cdot\})/(B+1)$, which is never zero.

**Algorithm 7.3.2 (Bootstrap Test for Two Means)** Observe $\boldsymbol{z}=(z_1,\dots,z_n)$ and $\boldsymbol{y}=(y_1,\dots,y_m)$ from two populations with a common variance, and test $H_0\colon\mu_z=\mu_y$ against $H_a\colon\mu_z\ne\mu_y$ with

$$
T(\boldsymbol{z},\boldsymbol{y})=\frac{\bar z-\bar y}{\hat\sigma\sqrt{n^{-1}+m^{-1}}},
$$
where $\hat\sigma$ is the pooled standard deviation.

1. Let $\bar x$ be the mean of the combined sample $\boldsymbol{x}$, and shift both samples to it: $\tilde z_i=z_i-\bar z+\bar x$, $\tilde y_j=y_j-\bar y+\bar x$.
2. For $b=1,\dots,B$, resample $n$ values with replacement from $\tilde{\boldsymbol{z}}$ and $m$ values from $\tilde{\boldsymbol{y}}$, and compute $\tilde T^{(b)}=\dfrac{\bar{\tilde z}^{(b)}-\bar{\tilde y}^{(b)}}{\hat{\tilde\sigma}^{(b)}\sqrt{n^{-1}+m^{-1}}}$.
3. The p-value is $\#\{b\colon\lvert\tilde T^{(b)}\rvert\ge\lvert T_{\mathrm{obs}}\rvert\}/B$.

**Remark 7.3.1** The permutation test for the same problem (developed in nonparametric statistics, [3.6](/3.6)) pools the combined sample $\boldsymbol{x}$, randomly assigns $n$ of its values to the first group and the remaining $m$ to the second, that is, samples group labels without replacement, and repeats this $M$ times. The bootstrap test samples with replacement from the shifted samples. The permutation test is exact under the stronger null hypothesis that the two distributions are equal; the bootstrap test only approximates the null distribution but targets the hypothesis of equal means.

## 7.4. The Parametric Bootstrap

There is also a parametric version. Assume that the data come from a known family $P_{\boldsymbol\theta}$ with unknown parameters $\boldsymbol\theta$. Our best guess of $P_{\boldsymbol\theta}$ is $P_{\hat{\boldsymbol\theta}}$, with the estimate $\hat{\boldsymbol\theta}$.

**Algorithm 7.4.1 (Parametric Bootstrap)**

1. Estimate $\hat{\boldsymbol\theta}$ from the data $\boldsymbol{X}$.
2. For $b=1,\dots,B$: simulate a data set $\boldsymbol{X}^{*(b)}$ of the same size and shape as the real data from $P_{\hat{\boldsymbol\theta}}$, and compute $T^{*(b)}=T(\boldsymbol{X}^{*(b)})$, treating the simulated data exactly like the real data.
3. Use the empirical distribution of $T^{*(1)},\dots,T^{*(B)}$ as the estimate of the sampling distribution of $T$.

**Example 7.4.1** Suppose a sample of size $n$ is believed to come from a normal population. Compute $\bar x$ and $s^2$, generate $1000$ samples of size $n$ from $\mathcal{N}(\bar x,s^2)$ and compute their means. These $1000$ means estimate the sampling distribution of $\bar X$; sorting them and dropping the smallest and largest $2.5\%$ gives a $95\%$ (percentile) interval for the population mean.

```r
n <- length(x); B <- 1000
means <- replicate(B, mean(rnorm(n, mean = mean(x), sd = sd(x))))   # simulate from N(xbar, s^2)
quantile(means, c(0.025, 0.975))
```

Knowing the family $P_{\boldsymbol\theta}$ is a strong assumption and rarely justified in practice, so the most common form is the nonparametric bootstrap. The parametric bootstrap is useful when the model is trusted, for small samples, and when the statistic has a discrete or degenerate nonparametric bootstrap distribution.

## Summary

Though remarkably simple to implement, the bootstrap would not be feasible without modern computing power. Its key idea is to perform computations on the data themselves to estimate the variation of statistics that are computed from the same data: the data "pull themselves up by their own bootstraps". Resampling ideas existed before 1979, but Bradley Efron widened their applicability, showed how to implement them effectively on computers and coined the term.

| Task | Bootstrap estimate |
|---|---|
| sampling distribution of $\hat\theta$ | empirical distribution of $\hat\theta^{(1)},\dots,\hat\theta^{(B)}$; nonparametric (resample the data, assumes i.i.d. data) or parametric (simulate from $P_{\hat\theta}$, assumes the model) |
| standard error | $\widehat{\operatorname{se}}=\bigl(\frac1{B-1}\sum_b(\hat\theta^{(b)}-\bar\theta^*)^2\bigr)^{1/2}$, $B=50$–$200$ |
| bias | $\widehat{\operatorname{Bias}}=\bar\theta^*-\hat\theta$ |
| confidence interval | normal $\hat\theta\pm z_{\alpha/2}\widehat{\operatorname{se}}$; basic $(2\hat\theta-\hat\theta^*_{1-\alpha/2},2\hat\theta-\hat\theta^*_{\alpha/2})$, using $\hat\theta^*-\hat\theta$ for $\hat\theta-\theta$; percentile $(\hat\theta^*_{\alpha/2},\hat\theta^*_{1-\alpha/2})$; BCa; $B\ge1000$ |
| hypothesis test | reject if $\theta_0$ is outside the interval, or shift the data to $H_0$ and resample the test statistic for a p-value |

The bootstrap is justified for Hadamard differentiable functionals (functional delta method); it fails for extremes and for non-smooth estimators at boundary points, where the smoothed or the $m$-out-of-$n$ bootstrap can help. Always look at the bootstrap distribution before trusting an interval.
