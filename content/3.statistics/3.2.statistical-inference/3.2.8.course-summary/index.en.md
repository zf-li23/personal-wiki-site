---
title: Course Summary
description: A compact review of the whole course — sampling distributions and data reduction, point estimation, confidence intervals, parametric and nonparametric tests, and Bayesian inference — organized in comparison tables, with the standard recipes for constructing estimators, intervals and tests.
---

Probability theory deduces the behavior of data from a known model; statistical inference reasons in the opposite direction, from a sample to the population that produced it. Because the sample is random, every conclusion is uncertain, and the central task of the subject is to quantify that uncertainty: by the bias, variance and mean squared error of an estimator, the confidence level of an interval, the significance level and power of a test, or, in the Bayesian approach, by the posterior distribution itself. This page reviews the course in that light: the framework and the tools of data reduction ([3.2.1](/3.2.1), [3.2.2](/3.2.2)), the three problems of point estimation ([3.2.3](/3.2.3)), interval estimation ([3.2.4](/3.2.4)) and hypothesis testing ([3.2.5](/3.2.5), [3.2.6](/3.2.6)), and the Bayesian alternative ([3.2.7](/3.2.7)).

## 8.1. The Framework

A sample $\boldsymbol{X}=(X_1,\dots,X_n)$ from a population $F$ is modeled by a family of distributions; in a parametric model $\{f(x;\theta)\colon\theta\in\Theta\}$, $\Theta$ is finite-dimensional, while in a nonparametric model the form of $F$ is unknown. A statistic $T(\boldsymbol{X})$ is a function of the sample free of unknown quantities; its distribution is its sampling distribution. Inference about $\theta$ (or $F$) takes three forms:

| Problem | Output | Frequentist quality measure | Chapter |
|---|---|---|---|
| point estimation | a value $\hat\theta(\boldsymbol{x})$ | bias, variance, MSE, consistency, efficiency | [3.2.3](/3.2.3) |
| interval estimation | a set $C(\boldsymbol{x})\subseteq\Theta$ | coverage $\mathbb{P}_\theta(\theta\in C(\boldsymbol{X}))\ge1-\alpha$, length | [3.2.4](/3.2.4) |
| hypothesis testing | reject or accept $H_0$ | type I error $\le\alpha$, power | [3.2.5](/3.2.5), [3.2.6](/3.2.6) |

In the frequentist view $\theta$ is a fixed constant and probability statements refer to repetitions of the sampling; in the Bayesian view $\theta$ has a prior distribution and all statements are conditional on the observed data ([3.2.7](/3.2.7)).

## 8.2. Sampling Distributions and Data Reduction

### 8.2.1. Sampling Distributions

| Distribution | Construction ($Z,Z_i\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$, independent pieces) | Facts |
|---|---|---|
| $\chi^2_r$ | $Z_1^2+\cdots+Z_r^2$ | mean $r$, variance $2r$; $\chi^2_r=\Gamma(\frac r2,\frac12)$; additive in $r$ |
| $t_r$ | $Z/\sqrt{Y/r}$, $Y\sim\chi^2_r$ | symmetric, heavier tails than $\mathcal{N}(0,1)$; $t_1$ is Cauchy; $t_r\xrightarrow{d}\mathcal{N}(0,1)$ |
| $F_{r_1,r_2}$ | $(Y_1/r_1)/(Y_2/r_2)$, $Y_i\sim\chi^2_{r_i}$ | $1/F\sim F_{r_2,r_1}$; $t_r^2\sim F_{1,r}$; $F_{r_1,r_2,1-\alpha}=1/F_{r_2,r_1,\alpha}$ |

For a normal sample $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ with sample mean $\bar X$ and sample variance $S^2=\frac{1}{n-1}\sum_i(X_i-\bar X)^2$ (Theorem 2.1.3):

$$
\bar X\sim\mathcal{N}\Big(\mu,\frac{\sigma^2}{n}\Big),\qquad \frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1},\qquad \bar X\ \text{and}\ S^2\ \text{independent},\qquad \frac{\sqrt n(\bar X-\mu)}{S}\sim t_{n-1}.
$$
For non-normal populations, the **central limit theorem** and Slutsky's theorem (Theorem 2.1.4) give $\sqrt n(\bar X-\mu)/S\xrightarrow{d}\mathcal{N}(0,1)$ whenever the variance is finite, which underlies all large-sample procedures.

### 8.2.2. Sufficiency, Completeness and Exponential Families

| Concept | Definition or criterion | Role |
|---|---|---|
| sufficient statistic $T$ | conditional distribution of $\boldsymbol{X}$ given $T$ free of $\theta$; factorization $f(\boldsymbol{x};\theta)=g(T(\boldsymbol{x});\theta)h(\boldsymbol{x})$ | no information about $\theta$ is lost; MLEs and Bayes procedures depend on $\boldsymbol{x}$ only through $T$ |
| minimal sufficient | a function of every sufficient statistic | maximal reduction |
| complete statistic | $\mathbb{E}_\theta\varphi(T)=0$ for all $\theta$ implies $\varphi(T)=0$ a.s. | uniqueness of unbiased estimators based on $T$ |
| exponential family | $f(x;\theta)=C(\theta)\exp\{\sum_jQ_j(\theta)T_j(x)\}h(x)$ | $(\sum_iT_1(X_i),\dots,\sum_iT_k(X_i))$ is sufficient, and complete if the natural parameter space has an interior point |
| Basu's theorem | bounded complete sufficient $T$ is independent of every ancillary statistic | e.g. independence of $\bar X$ and $S^2$ |

## 8.3. Point Estimation

### 8.3.1. Criteria

| Criterion | Definition | Remarks |
|---|---|---|
| unbiasedness | $\mathbb{E}_\theta\hat\theta=\theta$ for all $\theta$ | $S^2$ is unbiased for $\sigma^2$, the MLE $\frac{n-1}{n}S^2$ is not |
| mean squared error | $\operatorname{MSE}(\hat\theta)=\mathbb{E}_\theta(\hat\theta-\theta)^2=\operatorname{Var}(\hat\theta)+\operatorname{Bias}(\hat\theta)^2$ | trades bias against variance |
| consistency | $\hat\theta_n\xrightarrow{p}\theta$ (strong: $\xrightarrow{\text{a.s.}}$) | a large-sample minimum requirement |
| asymptotic normality | $\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}\mathcal{N}(0,v(\theta))$ | basis of approximate intervals and tests |
| efficiency | variance attains the Cramér–Rao bound $\frac{[g'(\theta)]^2}{nI(\theta)}$ | $I(\theta)=\mathbb{E}_\theta\big[(\partial_\theta\log f(X;\theta))^2\big]$, the Fisher information |
| UMVUE | unbiased with minimal variance for every $\theta$ | may exist without attaining the Cramér–Rao bound |

### 8.3.2. Methods

| Method | Recipe | Properties |
|---|---|---|
| method of moments | equate sample moments $\frac1n\sum X_i^k$ to population moments $\mathbb{E}_\theta X^k$ and solve | simple, consistent, asymptotically normal; not always efficient |
| **maximum likelihood estimation** | maximize $L(\theta;\boldsymbol{x})=\prod f(x_i;\theta)$, usually via the likelihood equation $\partial_\theta\log L=0$; check boundaries when the support depends on $\theta$ | invariant ($g(\hat\theta)$ is the MLE of $g(\theta)$); a function of a sufficient statistic; under regularity consistent with $\sqrt n(\hat\theta-\theta)\xrightarrow{d}\mathcal{N}(0,1/I(\theta))$, hence asymptotically efficient |
| UMVUE via sufficiency | Rao–Blackwell: $\mathbb{E}[\hat\theta\mid T]$ improves any unbiased $\hat\theta$; Lehmann–Scheffé: an unbiased function of a complete sufficient $T$ is the UMVUE | also: the zero-unbiased-estimator criterion |
| Bayes estimators | posterior mean, median or mode | optimal for squared, absolute and $0$–$1$ type losses |
| least squares, kernel density | OLS in linear regression (coincides with MLE under normal errors); kernel density estimate $\frac{1}{nh}\sum K\big(\frac{x-X_i}{h}\big)$ | the bandwidth $h$ controls the bias–variance trade-off |

## 8.4. Interval Estimation

The pivot method: find $G(\boldsymbol{X};\theta)$ whose distribution does not depend on $\theta$, choose $a,b$ with $\mathbb{P}(a\le G\le b)=1-\alpha$, and solve $a\le G(\boldsymbol{X};\theta)\le b$ for $\theta$. For normal populations:

| Parameter | Pivot | $1-\alpha$ confidence interval |
|---|---|---|
| $\mu$, $\sigma^2$ known | $\frac{\sqrt n(\bar X-\mu)}{\sigma}\sim\mathcal{N}(0,1)$ | $\bar X\pm z_{\alpha/2}\,\sigma/\sqrt n$ |
| $\mu$, $\sigma^2$ unknown | $\frac{\sqrt n(\bar X-\mu)}{S}\sim t_{n-1}$ | $\bar X\pm t_{n-1,\alpha/2}\,S/\sqrt n$ |
| $\sigma^2$, $\mu$ unknown | $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ | $\Big[\frac{(n-1)S^2}{\chi^2_{n-1,\alpha/2}},\ \frac{(n-1)S^2}{\chi^2_{n-1,1-\alpha/2}}\Big]$ |
| $\mu_1-\mu_2$, $\sigma_1^2=\sigma_2^2$ unknown | $\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_w\sqrt{1/m+1/n}}\sim t_{m+n-2}$ | $\bar X-\bar Y\pm t_{m+n-2,\alpha/2}\,S_w\sqrt{1/m+1/n}$ |
| $\sigma_1^2/\sigma_2^2$ | $\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}\sim F_{m-1,n-1}$ | $\Big[\frac{S_1^2/S_2^2}{F_{m-1,n-1,\alpha/2}},\ \frac{S_1^2/S_2^2}{F_{m-1,n-1,1-\alpha/2}}\Big]$ |

Here $S_w^2=\frac{(m-1)S_1^2+(n-1)S_2^2}{m+n-2}$ is the pooled variance. Without normality, approximate intervals come from asymptotic normality, $\hat\theta\pm z_{\alpha/2}\widehat{\mathrm{se}}$ (for example $\hat p\pm z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$ for a proportion), or from the bootstrap. One-sided confidence limits use one tail of the pivot; confidence regions for several parameters combine pivots (or use Bonferroni's inequality). A Bayesian credible interval instead takes posterior quantiles and is interpreted conditionally on the data.

## 8.5. Parametric Hypothesis Testing

### 8.5.1. Concepts and Optimal Tests

A test of $H_0\colon\theta\in\Theta_0$ against $H_1\colon\theta\in\Theta_1$ is a rejection region $W$ (or a test function $\varphi(\boldsymbol{x})\in[0,1]$). The power function is $\beta_\varphi(\theta)=\mathbb{E}_\theta\varphi(\boldsymbol{X})$; the type I error is $\beta_\varphi(\theta)$ for $\theta\in\Theta_0$ and the type II error is $1-\beta_\varphi(\theta)$ for $\theta\in\Theta_1$. The Neyman–Pearson principle fixes the level, $\sup_{\Theta_0}\beta_\varphi\le\alpha$, and then maximizes the power. The $p$-value is the smallest level at which the observed data would lead to rejection.

| Result | Statement |
|---|---|
| Neyman–Pearson lemma | for simple $H_0\colon\theta=\theta_0$ against $H_1\colon\theta=\theta_1$, the most powerful level-$\alpha$ test rejects when $f(\boldsymbol{x};\theta_1)/f(\boldsymbol{x};\theta_0)>k$ (randomizing on the boundary if necessary) |
| UMP tests in exponential families | for a one-parameter exponential family with $Q(\theta)$ monotone, one-sided hypotheses have UMP tests based on $T=\sum T(X_i)$; two-sided hypotheses generally have no UMP test |
| likelihood ratio test | reject when $\lambda(\boldsymbol{x})=\frac{\sup_{\Theta_0}L(\theta;\boldsymbol{x})}{\sup_{\Theta}L(\theta;\boldsymbol{x})}\le c$; under regularity $-2\log\lambda\xrightarrow{d}\chi^2_k$, $k=\dim\Theta-\dim\Theta_0$ (Wilks) |
| duality with intervals | $\{\theta_0\colon H_0\colon\theta=\theta_0\ \text{is accepted at level}\ \alpha\}$ is a $1-\alpha$ confidence set, and conversely |

### 8.5.2. Tests for Normal Populations

| Hypothesis | Statistic | Null distribution |
|---|---|---|
| $\mu=\mu_0$, $\sigma^2$ known | $Z=\frac{\sqrt n(\bar X-\mu_0)}{\sigma}$ | $\mathcal{N}(0,1)$ |
| $\mu=\mu_0$, $\sigma^2$ unknown | $T=\frac{\sqrt n(\bar X-\mu_0)}{S}$ | $t_{n-1}$ |
| $\sigma^2=\sigma_0^2$, $\mu$ unknown | $\chi^2=\frac{(n-1)S^2}{\sigma_0^2}$ | $\chi^2_{n-1}$ |
| $\mu_1-\mu_2=\delta$, equal unknown variances | $T=\frac{(\bar X-\bar Y)-\delta}{S_w\sqrt{1/m+1/n}}$ | $t_{m+n-2}$ |
| $\sigma_1^2=\sigma_2^2$ | $F=S_1^2/S_2^2$ | $F_{m-1,n-1}$ |
| paired data, $\mathbb{E}(Y-X)=0$ | one-sample $t$ on $Z_i=Y_i-X_i$ | $t_{n-1}$ |

For two-sided alternatives reject when $\lvert Z\rvert>z_{\alpha/2}$, $\lvert T\rvert>t_{\cdot,\alpha/2}$, or the $\chi^2$, $F$ statistic falls outside its $\alpha/2$ and $1-\alpha/2$ quantiles; for one-sided alternatives use one tail at level $\alpha$. For Bernoulli and Poisson parameters and for two means with unequal unknown variances, large-sample $Z$ statistics replace the exact pivots.

## 8.6. Nonparametric Tests

| Question | Test | Statistic and null distribution |
|---|---|---|
| median or paired difference $=0$ | sign test | $n_+\sim\mathrm{Bin}(n_0,\frac12)$ |
| symmetric center $=0$ | Wilcoxon signed-rank | $W^+$; mean $\frac{n_0(n_0+1)}{4}$, variance $\frac{n_0(n_0+1)(2n_0+1)}{24}$ |
| two samples, location shift | Wilcoxon rank-sum (Mann–Whitney) | $W$; mean $\frac{n(N+1)}{2}$, variance $\frac{mn(N+1)}{12}$ |
| given discrete or grouped distribution | Pearson $\chi^2$ | $\sum\frac{(\text{obs}-\text{exp})^2}{\text{exp}}\approx\chi^2_{r-1-s}$ |
| independence or homogeneity in an $r\times s$ table | contingency-table $\chi^2$ | $n\big(\sum\frac{n_{ij}^2}{n_{i\cdot}n_{\cdot j}}-1\big)\approx\chi^2_{(r-1)(s-1)}$ |
| fully specified continuous $F_0$ | Kolmogorov–Smirnov | $D_n=\sup\lvert F_n-F_0\rvert$, distribution-free |
| normality with unknown parameters | Shapiro–Wilk; Q–Q plot | $W$ close to $1$ under normality |

Rank tests lose little power under normality (asymptotic relative efficiency $3/\pi\approx0.955$ for the Wilcoxon tests) and can gain a great deal under heavy tails or outliers.

## 8.7. Bayesian Inference

$$
\pi(\theta\mid\boldsymbol{x})=\frac{f(\boldsymbol{x}\mid\theta)\pi(\theta)}{\int f(\boldsymbol{x}\mid\theta)\pi(\theta)\,\mathrm{d}\theta}\propto\text{likelihood}\times\text{prior}.
$$

| Task | Bayesian answer |
|---|---|
| choice of prior | subjective; conjugate (Beta–binomial, Gamma–Poisson, normal–normal, normal–gamma); non-informative: uniform (possibly improper), Jeffreys $\propto\sqrt{I(\theta)}$ (invariant), maximum entropy; hierarchical |
| point estimate | posterior mean (minimizes PMSE; squared loss), posterior median (absolute loss), MAP (equals the MLE under a flat prior) |
| uncertainty | posterior variance $=$ PMSE of the posterior mean |
| interval | credible interval $\mathbb{P}(\theta\in C\mid\boldsymbol{x})\ge1-\alpha$; HPD interval is the shortest |
| test | compare $\alpha_0=\mathbb{P}(\Theta_0\mid\boldsymbol{x})$ and $\alpha_1=\mathbb{P}(\Theta_1\mid\boldsymbol{x})$; Bayes factor $m_1(\boldsymbol{x})/m_0(\boldsymbol{x})$ |
| prediction | posterior predictive $p(z\mid\boldsymbol{x})=\int g(z\mid\theta)\pi(\theta\mid\boldsymbol{x})\,\mathrm{d}\theta$ |
| decision | minimize the posterior expected loss $\mathbb{E}[L(a,\theta)\mid\boldsymbol{x}]$ |

The Bayesian approach respects the likelihood principle, which $p$-values violate, and its interval and test statements have a direct conditional meaning; its price is the need to specify a prior, whose influence vanishes as the sample grows.

## 8.8. Recipes

1. Estimators. For the method of moments, express the parameters in terms of moments and substitute sample moments. For the MLE, write $L(\theta)$, take $\log L$, solve the likelihood equation, and check that it is a maximum; if the support depends on $\theta$ (as for $\mathrm{U}(0,\theta)$), maximize directly, which often gives an order statistic. For a UMVUE, find a complete sufficient statistic $T$ and an unbiased function of $T$, or condition any unbiased estimator on $T$.
2. Confidence intervals. Find a pivot from the distribution theory of §8.2, fix its two quantiles, and solve for $\theta$; for large samples, standardize an asymptotically normal estimator.
3. Tests. For simple hypotheses use the Neyman–Pearson likelihood ratio; for one-sided hypotheses in a monotone exponential family, the corresponding one-sided test in $T$ is UMP; in general use the likelihood ratio test with Wilks' $\chi^2$ approximation. Determine the critical value from the null distribution at level $\alpha$, or report the $p$-value.
4. Without a parametric model, use signs and ranks for location problems, Pearson's $\chi^2$ for counts and tables, and the Kolmogorov–Smirnov or Shapiro–Wilk test for distributional hypotheses.
5. Bayesian analysis. Write likelihood $\times$ prior, recognize the kernel of a known distribution (conjugacy), and read off posterior means, quantiles and probabilities.

## Summary

The course rests on a small number of results; each problem above is solved by one of them.

| Question | Key results |
|---|---|
| What do the statistics look like under normality? | Theorem 2.1.3 ($\bar X$ and $S^2$ independent, with normal and $\chi^2$ distributions); Theorem 2.1.4 (Slutsky) for large samples |
| How far can the data be reduced? | Theorem 2.3.1 (factorization), Theorem 2.3.2 (completeness in exponential families), Theorem 2.3.3 (Basu) |
| How good can an estimator be? | Theorem 3.4.4 (Cramér–Rao lower bound); Theorems 3.4.1 and 3.4.3 (Rao–Blackwell, Lehmann–Scheffé) for the UMVUE; Theorem 3.3.5 (asymptotic normality and efficiency of the MLE) |
| How is an interval built? | A pivot (Definition 4.2.1), or an asymptotically normal estimator; duality with tests |
| Which test is best? | Theorem 5.4.1 (Neyman–Pearson lemma), Theorem 5.4.4 (Karlin–Rubin) for one-sided UMP tests; Theorem 5.3.1 (Wilks) for likelihood ratio tests |
| What if there is no parametric model? | Signs and ranks; Theorem 6.3.1 (Pearson's $\chi^2$) for counts; Kolmogorov–Smirnov and Shapiro–Wilk for distributions |
| How does the Bayesian answer differ? | Posterior $\propto$ likelihood $\times$ prior; Theorem 7.3.1 (conjugate priors in exponential families); Bayes estimators and HPD intervals from the posterior |
