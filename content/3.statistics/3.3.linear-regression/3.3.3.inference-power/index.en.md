---
title: Statistical Inference and Power
description: Inference in simple linear regression with normal errors; sampling distributions of the slope and intercept estimators, t-tests and confidence intervals, the test of zero correlation, the Gauss–Markov theorem (BLUE), joint inference with the Bonferroni correction, and the power of the slope test computed from the noncentral t-distribution, with power curves and sample size determination.
---

Least squares gives one line, but a different sample would give a different line. How far can the estimated slope $b_1$ be from the true slope $\beta_1$, and is the evidence for $\beta_1\ne0$ convincing? This chapter answers these questions under the normal error regression model of [3.3.2](/3.3.2). It first reviews the three basic tools of [3.2.2](/3.2.2)–[3.2.5](/3.2.5) (**sampling distributions**, tests and confidence intervals) on the normal mean, then applies them to $\beta_1$ and $\beta_0$, establishes the optimality of least squares (the **Gauss–Markov theorem**), and treats two questions that arise as soon as more than one statement is made or a study is planned: joint confidence statements for $(\beta_0,\beta_1)$, and the power of a test, which decides how large a study must be. Estimation of the mean response, prediction and the analysis of variance follow in [3.3.4](/3.3.4).

## 3.1. Review: Basics of Statistical Inference

### 3.1.1. Sampling Distributions

We use the normal mean as the example. Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$. The **sample mean** and the **sample variance**,

$$
\hat\mu=\bar X=\frac1n\sum_{i=1}^nX_i,\qquad\hat\sigma^2=s^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2,
$$
estimate the center (location) and the spread (variability, dispersion); $s^2$ has $n-1$ **degrees of freedom**, and $\hat\sigma=s=\sqrt{s^2}$. As an estimator, $\bar X$ varies from sample to sample and is therefore a random variable. Its distribution, the probability distribution of all possible values of the statistic for a given sample size, is its **sampling distribution**: $\bar X\sim\mathcal{N}(\mu,\sigma^2/n)$, normal with the same mean but a much smaller variance $\sigma^2(\bar X)=\mathbb{E}(\bar X-\mu)^2=\sigma^2/n$. The sample size in the sampling distribution of $\bar X$ is the size $n$ of each sample, not the number of samples drawn.

**Definition 3.1.1** The **standard error** of an estimator $\hat\theta$ is the estimated standard deviation of its sampling distribution. For the sample mean, $\hat\sigma^2(\bar X)=s^2/n$ and

$$
\operatorname{SE}(\bar X)=s(\bar X)=\frac{s}{\sqrt n}.
$$

The standard error is the typical deviation of $\bar X$ from its target $\mu$ and tells us how accurate $\bar X$ is. Two derived distributions describe $s^2$ and the standardized mean. If $Z_1,\dots,Z_k\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$, then $U=Z_1^2+\cdots+Z_k^2$ has the **chi-square distribution** $\chi^2_k$ with $k$ degrees of freedom, with $\mathbb{E}(U)=k$ and $\operatorname{Var}(U)=2k$. If moreover $Z_0\sim\mathcal{N}(0,1)$ is independent of $U$, then $T=Z_0/\sqrt{U/k}$ has the **t-distribution** $t_k$ with $k$ degrees of freedom.

**Theorem 3.1.1** Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$. Then

1. $\bar X\sim\mathcal{N}(\mu,\sigma^2/n)$;
2. $(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$;
3. $\bar X$ and $s^2$ are independent.

Consequently

$$
T=\frac{\bar X-\mu}{\operatorname{SE}(\bar X)}=\frac{\bar X-\mu}{s/\sqrt n}=\frac{(\bar X-\mu)/(\sigma/\sqrt n)}{\sqrt{\dfrac{(n-1)s^2}{\sigma^2(n-1)}}}\sim t_{n-1}.
$$

This is [Theorem 2.1.3](/3.2.2#thm-2.1.3) of 3.2.2, where it is proved; the independence in item 3 is a special property of the normal distribution. The statistic $T$ measures how far $\bar X$ is from its target in units of its standard error.

### 3.1.2. Hypothesis Tests

A test decides between a **null hypothesis** $H_0$ and an **alternative hypothesis** $H_1$ and can make two kinds of mistakes: a **type I error** (rejecting $H_0$ when it is true), with probability $\alpha=\mathbb{P}(\text{reject }H_0\mid H_0\text{ true})$, and a **type II error** (failing to reject $H_0$ when $H_1$ is true). The classical principle is to choose a decision rule that first controls $\alpha$ at a prescribed **level of significance** and then makes the probability of a type II error as small as possible. The power of the test, $1-\mathbb{P}(\text{type II error})$, depends on which value of the parameter in $H_1$ is true (Section 3.6). Many texts write $\beta$ for the probability of a type II error; we avoid this because $\beta_0,\beta_1$ denote the regression coefficients.

**Example 3.1.1** Are Tsinghua male students taller than $174$ cm on average? A census would be costly and is unnecessary; instead we sample and test. The heights (cm) of $15$ randomly sampled male students are

$$
174,\ 171,\ 175,\ 174,\ 176,\ 177,\ 175,\ 171,\ 178,\ 177,\ 175,\ 179,\ 176,\ 174,\ 177,
$$
modeled as a sample from $\mathcal{N}(\mu,\sigma^2)$, with $\bar x=175.27$, $s^2=5.21$, $s=2.28$. We test $H_0\colon\mu=174$ against $H_1\colon\mu>174$ at $\alpha=0.05$. The observed statistic is

$$
t_0=\frac{175.27-174}{2.28/\sqrt{15}}=2.15.
$$
Critical value approach: the upper $0.05$ quantile is $t_{14,0.05}=1.761$, and $t_0>1.761$, so $H_0$ is rejected. $p$-value approach: $\mathbb{P}(T>t_0)=0.025$ for $T\sim t_{14}$, which is below $0.05$, so $H_0$ is rejected. The test is significant: the data support that Tsinghua male students are taller than $174$ cm on average.

For the two-sided problem $H_0\colon\mu=\mu_0$ against $H_1\colon\mu\ne\mu_0$, the test statistic is $T=(\bar X-\mu_0)/(s/\sqrt n)\overset{H_0}{\sim}t_{n-1}$. With $t_0$ its observed value,

- critical value approach: reject $H_0$ if $\lvert t_0\rvert>t_{n-1,\alpha/2}$;
- **p-value** approach: reject $H_0$ if $\mathbb{P}(T\ge\lvert t_0\rvert)+\mathbb{P}(T\le-\lvert t_0\rvert)<\alpha$.

### 3.1.3. Confidence Intervals

An interval estimator $(\bar X-c,\bar X+c)$ with $\mathbb{P}\big(\mu\in(\bar X-c,\bar X+c)\big)=1-\alpha$ is a **confidence interval** for $\mu$ with **confidence level** $1-\alpha$. The confidence is placed on the procedure and describes its long-run behavior: over many samples, a proportion $1-\alpha$ of the intervals cover $\mu$, while any particular interval either covers $\mu$ or does not. If the data are not normal, the procedure is only approximate (by the **central limit theorem**), and the actual coverage probability may differ from the nominal level.

From $(\bar X-\mu)/(s/\sqrt n)\sim t_{n-1}$,

$$
\mathbb{P}\left(-t_{n-1,\alpha/2}<\frac{\bar X-\mu}{s/\sqrt n}<t_{n-1,\alpha/2}\right)=1-\alpha
\ \Longrightarrow\ 
\mathbb{P}\left(\bar X-t_{n-1,\alpha/2}\frac{s}{\sqrt n}<\mu<\bar X+t_{n-1,\alpha/2}\frac{s}{\sqrt n}\right)=1-\alpha,
$$
so the $100(1-\alpha)\%$ confidence interval for $\mu$ is

$$
\left(\bar X-t_{n-1,\alpha/2}\frac{s}{\sqrt n},\ \bar X+t_{n-1,\alpha/2}\frac{s}{\sqrt n}\right).
$$
Its center is the point estimate $\bar X$, its half-width $t_{n-1,\alpha/2}\operatorname{SE}(\bar X)$ is the *margin of error*, and its confidence level is $1-\alpha$.

**Example 3.1.2** For the heights of Example 3.1.1, $t_{14,0.025}=2.145$, and the $95\%$ confidence interval for the mean height is

$$
175.27\pm2.145\times\frac{2.28}{\sqrt{15}}=(174.00,\ 176.53).
$$
We are $95\%$ confident that the average height of Tsinghua male students lies between $174.00$ and $176.53$ cm.

Tests and intervals are two sides of the same coin ([3.2.5](/3.2.5)). For $H_0\colon\mu=\mu_0$ against $H_1\colon\mu\ne\mu_0$, construct the $100(1-\alpha)\%$ confidence interval: if it contains $\mu_0$, do not reject $H_0$; if not, reject. This is equivalent to the critical value and $p$-value approaches for the two-sided hypothesis. For a one-sided hypothesis at level $\alpha$, the same cutoff is obtained from a $100(1-2\alpha)\%$ two-sided interval: in Example 3.1.1 the $90\%$ interval has lower limit $175.27-1.761\times2.28/\sqrt{15}=174.23>174$, so $H_0\colon\mu=174$ is rejected against $\mu>174$, in agreement with Example 3.1.1, while the $95\%$ interval excludes $174$ only barely (its two-sided $p$-value is $0.0496$).

## 3.2. Inference for the Slope

The slope is usually the parameter of interest. When $\beta_1=0$ the regression line is horizontal, $\mathbb{E}(Y)=\beta_0$ for every $X$, and there is no linear association between $Y$ and $X$; under normal errors with equal variances, the distributions of $Y$ at all levels of $X$ are then identical.

### 3.2.1. Sampling Distribution of $b_1$

By [3.3.2](/3.3.2), the least squares estimator $b_1=S_{XY}/S_{XX}$ is unbiased and linear in the responses:

$$
b_1=\sum_{i=1}^n\frac{X_i-\bar X}{S_{XX}}Y_i=\sum_{i=1}^n\frac{X_i-\bar X}{S_{XX}}(\beta_0+\beta_1X_i+\varepsilon_i)=\beta_1+\sum_{i=1}^n\frac{X_i-\bar X}{S_{XX}}\varepsilon_i.
$$

**Theorem 3.2.1** Under the normal error regression model,

1. $b_1\sim\mathcal{N}\big(\beta_1,\sigma^2(b_1)\big)$ with $\sigma^2(b_1)=\operatorname{Var}(b_1)=\sigma^2/S_{XX}$;
2. $(n-2)s^2/\sigma^2=\mathrm{SSE}/\sigma^2\sim\chi^2_{n-2}$, and $s^2$ is independent of $(b_0,b_1)$;
3. with the standard error $s(b_1)=s/\sqrt{S_{XX}}$, where $s=\sqrt{\mathrm{MSE}}$,

$$
\frac{b_1-\beta_1}{s(b_1)}\sim t_{n-2}.
$$

**Proof** Item 1 holds because $b_1$ is a linear combination of the independent normal errors, with the mean and variance computed in [3.3.2](/3.3.2). Item 2 is the special case $p=2$ of the distribution theory of the normal linear model, proved with the matrix approach in [3.3.7](/3.3.7) (see also [3.4.7](/3.4.7)). For item 3,

$$
\frac{b_1-\beta_1}{s(b_1)}=\frac{(b_1-\beta_1)/\sigma(b_1)}{s(b_1)/\sigma(b_1)}=\frac{(b_1-\beta_1)/\sigma(b_1)}{\sqrt{\mathrm{SSE}/[\sigma^2(n-2)]}},
$$
a standard normal variable divided by the square root of an independent $\chi^2_{n-2}$ variable over its degrees of freedom. $\square$

Compared with the normal mean, two degrees of freedom are lost instead of one, because two parameters are estimated before the residuals can be formed.

### 3.2.2. The t-Test for the Slope

To test $H_0\colon\beta_1=0$ against $H_1\colon\beta_1\ne0$, the evidence about $\beta_1$ is summarized by $b_1$ and its uncertainty by $\sigma(b_1)=\sigma/\sqrt{S_{XX}}$, estimated by $s(b_1)=s/\sqrt{S_{XX}}$ with $s=\sqrt{\sum_i(Y_i-\hat Y_i)^2/(n-2)}$. The evidence concerning $H_0$ is summarized by the test statistic

$$
T=\frac{b_1-0}{s(b_1)}\overset{H_0}{\sim}t_{n-2}.
$$
At level $\alpha$, reject $H_0$ if the observed value satisfies $\lvert t_0\rvert>t_{n-2,\alpha/2}$; equivalently, if the two-sided $p$-value is below $\alpha$. For one-sided alternatives, or for $H_0\colon\beta_1=c$ (use $T=(b_1-c)/s(b_1)$), the statistic and the decision rule are modified accordingly. In the R output of `summary(lm(...))`, the column `t value` is $b_1/s(b_1)$ and `Pr(>|t|)` is the two-sided $p$-value; for the Pisa data of [3.3.2](/3.3.2), $t_0=9.3187/0.3099=30.07$ on $11$ degrees of freedom, $p=6.5\times10^{-12}$.

The conclusion of the test must be read with care. If we do not reject $H_0$, any of three realities is possible:

1. we committed a type II error: in reality $\beta_1\ne0$, and the sample just did not provide enough evidence;
2. there really is not much of a linear relationship between $X$ and $Y$;
3. there is a relationship between $X$ and $Y$, but it is not linear.

If we do reject $H_0$, any of three realities is possible:

1. we committed a type I error: in reality $\beta_1=0$, but we have an unusual sample;
2. the relationship between $X$ and $Y$ is indeed linear;
3. a linear function fits the data reasonably well, but a curved ("curvilinear") function would fit even better.

A significant slope is therefore not a proof that the linear model is right; the diagnostics of [3.3.5](/3.3.5) address the remaining possibilities.

### 3.2.3. Confidence Interval for the Slope

By Theorem 3.2.1, $\mathbb{P}\big(\lvert b_1-\beta_1\rvert/s(b_1)<t_{n-2,\alpha/2}\big)=1-\alpha$, so the $100(1-\alpha)\%$ confidence interval for $\beta_1$ is

$$
\big(b_1-t_{n-2,\alpha/2}\,s(b_1),\ b_1+t_{n-2,\alpha/2}\,s(b_1)\big).
$$

### 3.2.4. Testing Zero Correlation

Suppose now that $(X_i,Y_i)$, $i=1,\dots,n$, is a random sample from a **bivariate normal distribution**, so that $X$ is random as well. Then

$$
\mathbb{E}(Y\mid X=x)=\left(\mu_Y-\rho\frac{\sigma_Y}{\sigma_X}\mu_X\right)+\rho\frac{\sigma_Y}{\sigma_X}x=\beta_0+\beta_1x,\qquad\beta_1=\rho\frac{\sigma_Y}{\sigma_X},
$$
and conditionally on the $X_i$ the normal error regression model holds. Since $\sigma_X,\sigma_Y>0$, testing $H_0\colon\rho=0$ is equivalent to testing $H_0\colon\beta_1=0$, and correspondingly $b_1=r\,s_Y/s_X$ with the sample **correlation coefficient** $r$. In terms of $r$ the $t$-statistic becomes

$$
t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}\overset{H_0}{\sim}t_{n-2},
$$
which is shown in [3.3.4](/3.3.4). In R the test is `cor.test(x, y)`. It is the more natural formulation when it is not obvious which variable is the response, because it treats $X$ and $Y$ symmetrically.

## 3.3. Inference for the Intercept

Similarly, $b_0=\bar Y-b_1\bar X$ is a linear combination of the $Y_i$, and since $\operatorname{Cov}(\bar Y,b_1)=0$ ([3.3.2](/3.3.2)),

$$
b_0\sim\mathcal{N}\big(\beta_0,\sigma^2(b_0)\big),\qquad\sigma^2(b_0)=\sigma^2\left(\frac1n+\frac{\bar X^2}{S_{XX}}\right),\qquad s(b_0)=s\sqrt{\frac1n+\frac{\bar X^2}{S_{XX}}},
$$
and $(b_0-\beta_0)/s(b_0)\sim t_{n-2}$. Hence:

- significance test of $H_0\colon\beta_0=0$ against $H_1\colon\beta_0\ne0$: reject $H_0$ if $\lvert b_0\rvert/s(b_0)>t_{n-2,\alpha/2}$; one-sided tests and tests of $H_0\colon\beta_0=c$ are derived accordingly;
- the $100(1-\alpha)\%$ confidence interval for $\beta_0$ is $\big(b_0-t_{n-2,\alpha/2}\,s(b_0),\ b_0+t_{n-2,\alpha/2}\,s(b_0)\big)$.

**Remark 3.3.1** Several practical points follow from these formulas.

1. Design, that is, where to collect the data, matters. The *scope* of the model is the range of the explanatory variable covered by the data. The variance $\sigma^2(b_1)=\sigma^2/\sum_i(X_i-\bar X)^2$ is smallest when the $X_i$ are spread out as much as possible, which guides the allocation of $X_1,\dots,X_n$ and the choice of the sample size; but a design with all points at the two ends of the range cannot reveal a curvature, so in practice some intermediate levels are kept.
2. Inference about $\beta_0$ is usually not of interest: a shift of the origin of $X$ changes $\beta_0$, and $X=0$ may not be in the scope of the model.
3. If the errors are not normal but their distribution is roughly symmetric, the tests and intervals are reasonable approximations, and they improve as the sample size increases.

**Example 3.3.1** For the Pisa data of [3.3.2](/3.3.2), `confint(bc)` gives the $95\%$ confidence limits (labeled `2.5 %` and `97.5 %`):

| | 2.5 % | 97.5 % |
|---|---|---|
| (Intercept) | $-116.43$ | $-5.81$ |
| year | $8.637$ | $10.001$ |

The lean increases by between $0.86$ and $1.00$ mm per year, with $95\%$ confidence. The interval for the intercept is uninteresting: it would tell us the lean in the year 1900, which lies far outside the scope of the data.

## 3.4. The Gauss–Markov Theorem

We now establish the fundamental optimality property of the least squares estimators. For an independent random sample $Y_1,\dots,Y_n$ from a population with mean $\mu=\mathbb{E}(Y)$ and finite variance, the sample mean $\bar Y$ has the smallest variance among all linear unbiased estimators $\sum_ic_iY_i$ of $\mu$ (unbiasedness forces $\sum_ic_i=1$, and $\sum_ic_i^2$ is minimized by $c_i=1/n$).

**Definition 3.4.1** An estimator of a parameter is a **best linear unbiased estimator** (BLUE) if it is linear in the observations $Y_1,\dots,Y_n$, unbiased, and has the smallest variance among all linear unbiased estimators.

The class of linear unbiased estimators is a subclass of the unbiased estimators, so a BLUE need not be the minimum-variance unbiased estimator among all unbiased estimators; under normal errors, however, the least squares estimators are even that ([3.2.3](/3.2.3)).

**Theorem 3.4.1 (Gauss–Markov Theorem)** Under the simple linear regression model (uncorrelated errors with mean $0$ and common variance $\sigma^2$, no normality required), the least squares estimators $b_0$ and $b_1$ are the best linear unbiased estimators of $\beta_0$ and $\beta_1$.

**Proof** We prove the statement for $b_1$. Let $\tilde\beta_1=\sum_ic_iY_i$ be linear. Then $\mathbb{E}(\tilde\beta_1)=\beta_0\sum_ic_i+\beta_1\sum_ic_iX_i$, so $\tilde\beta_1$ is unbiased for all $\beta_0,\beta_1$ if and only if

$$
\sum_{i=1}^nc_i=0,\qquad\sum_{i=1}^nc_iX_i=1,
$$
and its variance is $\sigma^2\sum_ic_i^2$. The least squares coefficients $k_i=(X_i-\bar X)/S_{XX}$ satisfy both constraints. Write $c_i=k_i+d_i$; then $\sum_id_i=0$ and $\sum_id_iX_i=0$, hence $\sum_ik_id_i=\big(\sum_id_iX_i-\bar X\sum_id_i\big)/S_{XX}=0$ and

$$
\operatorname{Var}(\tilde\beta_1)=\sigma^2\sum_ic_i^2=\sigma^2\sum_ik_i^2+\sigma^2\sum_id_i^2\ge\sigma^2\sum_ik_i^2=\operatorname{Var}(b_1),
$$
with equality only if all $d_i=0$, that is, $\tilde\beta_1=b_1$. The proof for $b_0$ is the same, with the constraints $\sum_ic_i=1$ and $\sum_ic_iX_i=0$. $\square$

Geometrically, the coefficient vectors $\boldsymbol{c}=(c_1,\dots,c_n)^{\mathsf T}$ of the linear unbiased estimators of $\beta_1$ form the intersection of the two hyperplanes $\sum_ic_i=0$ and $\sum_ic_iX_i=1$ in $\mathbb{R}^n$, and the variance is $\sigma^2\|\boldsymbol{c}\|^2$. The BLUE corresponds to the point of this affine subspace closest to the origin, the foot of the perpendicular, which is $\boldsymbol{k}$ with $k_i=(X_i-\bar X)/\sum_j(X_j-\bar X)^2$. The theorem is the single strongest justification of least squares; its matrix version for several predictors is [Theorem 3.5.1](/3.2.3#thm-3.5.1) of 3.2.3.

## 3.5. Joint Inference for the Intercept and the Slope

A confidence interval is a statement about a single parameter. For two or more parameters we want a **confidence region** $S\subset\mathbb{R}^2$ with $\mathbb{P}\big((\beta_0,\beta_1)\in S\big)=1-\alpha$. Since $(b_0,b_1)^{\mathsf T}$ is bivariate normal with mean $(\beta_0,\beta_1)^{\mathsf T}$ and covariance matrix proportional to $\sigma^2$, the natural (smallest) confidence region is an ellipse,

$$
\begin{bmatrix}b_0-\beta_0\\b_1-\beta_1\end{bmatrix}^{\mathsf T}\begin{bmatrix}n&\sum_iX_i\\\sum_iX_i&\sum_iX_i^2\end{bmatrix}\begin{bmatrix}b_0-\beta_0\\b_1-\beta_1\end{bmatrix}\le2\,\mathrm{MSE}\,F_{2,n-2,\alpha},
$$
whose matrix form is developed in [3.3.7](/3.3.7). A simpler alternative is a rectangle, the product of two separate confidence intervals,

$$
S=\mathrm{CI}_0\times\mathrm{CI}_1=\{(\beta_0,\beta_1)\colon\beta_0\in\mathrm{CI}_0\text{ and }\beta_1\in\mathrm{CI}_1\}.
$$
If each interval has level $1-\alpha$, the rectangle does not: with $A_j=\{\beta_j\in\mathrm{CI}_j\}$,

$$
\mathbb{P}(A_0\cap A_1)=1-\mathbb{P}(A_0^{\mathsf c}\cup A_1^{\mathsf c})\le1-\mathbb{P}(A_0^{\mathsf c})=1-\alpha,
$$
with strict inequality in general. The confidence level of each interval has to be adjusted. By the Bonferroni inequality,

$$
\mathbb{P}(A_0\cap A_1)\ge1-\mathbb{P}(A_0^{\mathsf c})-\mathbb{P}(A_1^{\mathsf c}),
$$
so if each interval has level $1-\alpha/2$, the rectangle has level at least $1-\alpha$. This is the **Bonferroni correction** ([3.2.4](/3.2.4)): the joint intervals

$$
b_0\pm t_{n-2,\alpha/4}\,s(b_0),\qquad b_1\pm t_{n-2,\alpha/4}\,s(b_1)
$$
replace the individual intervals $b_j\pm t_{n-2,\alpha/2}\,s(b_j)$, and their product is a confidence region for $(\beta_0,\beta_1)$ with level at least $1-\alpha$. With $g$ parameters, each interval uses $\alpha/g$.

**Example 3.5.1** For the Pisa data, $t_{11,0.0125}=2.593$ instead of $t_{11,0.025}=2.201$, and the Bonferroni $95\%$ joint confidence intervals are $-126.3<\beta_0<4.0$ and $8.515<\beta_1<10.122$. Both are wider than the individual intervals of Example 3.3.1; the price of a joint statement is a loss of precision.

## 3.6. Power

### 3.6.1. Definition

The *power* of a significance test is the probability that the null hypothesis is rejected when the alternative hypothesis $H_1$ is in fact true,

$$
\text{power}=1-\mathbb{P}(\text{type II error}).
$$
This probability depends on the particular value of the parameter in $H_1$, and as a function of that value it is the **power function** of the test ([3.2.5](/3.2.5)), usually displayed as a curve. The guiding principle is that, once the significance level is set, the test should also be properly powered for the value of the parameter in $H_1$ that is of primary interest: neither under-powered (a real effect is likely to be missed) nor over-powered (resources are wasted, and negligible effects become significant).

### 3.6.2. Power of the Slope Test and the Noncentral t-Distribution

For the test of $H_0\colon\beta_1=0$ against $H_1\colon\beta_1\ne0$ that rejects when $\lvert b_1\rvert/s(b_1)>t_{n-2,\alpha/2}$,

$$
\operatorname{Power}(\beta_1)=\mathbb{P}\left(\frac{\lvert b_1\rvert}{s(b_1)}>t_{n-2,\alpha/2}\ \Big|\ \beta_1\right).
$$
At $\beta_1=0$, $\operatorname{Power}(0)=\alpha$, the probability of a type I error. For $\beta_1\ne0$ a difficulty arises: $b_1\sim\mathcal{N}(\beta_1,\sigma^2(b_1))$ is not centered at $0$, and $T=b_1/s(b_1)$ does not follow $t_{n-2}$.

**Definition 3.6.1** Let $Z\sim\mathcal{N}(0,1)$ and $U\sim\chi^2_k$ be independent, and $\delta\in\mathbb{R}$. The distribution of

$$
T=\frac{Z+\delta}{\sqrt{U/k}}
$$
is the **noncentral t-distribution** $t_k(\delta)$ with $k$ degrees of freedom and **noncentrality parameter** $\delta$. For $\delta=0$ it is the ordinary $t_k$.

For $\delta>0$ the density is shifted to the right and is skewed, its right tail being heavier.

**Theorem 3.6.1** Under the normal error regression model,

$$
T=\frac{b_1}{s(b_1)}\sim t_{n-2}(\delta),\qquad\delta=\frac{\beta_1}{\sigma(b_1)}=\frac{\beta_1\sqrt{S_{XX}}}{\sigma}.
$$

**Proof** Write

$$
T=\frac{(b_1-\beta_1)+\beta_1}{s(b_1)}=\frac{\big[(b_1-\beta_1)+\beta_1\big]/\sigma(b_1)}{s(b_1)/\sigma(b_1)}=\frac{Z+\delta}{\sqrt{\mathrm{SSE}/[\sigma^2(n-2)]}},
$$
where $Z=(b_1-\beta_1)/\sigma(b_1)\sim\mathcal{N}(0,1)$ is independent of $\mathrm{SSE}/\sigma^2\sim\chi^2_{n-2}$ by Theorem 3.2.1. $\square$

Hence

$$
\operatorname{Power}(\beta_1)=\mathbb{P}(T>t_{n-2,\alpha/2})+\mathbb{P}(T<-t_{n-2,\alpha/2}),\qquad T\sim t_{n-2}\big(\beta_1/\sigma(b_1)\big).
$$
To compute it for various values of $\beta_1$ we need to know or assume $\sigma^2(b_1)=\sigma^2/\sum_i(X_i-\bar X)^2$, that is, the design $X_1,\dots,X_n$ and the error variance $\sigma^2$, from prior knowledge or a pilot study; then tables or software give the probability (in R, `pt(q, df, ncp)` is the distribution function of $t_{df}(\mathrm{ncp})$).

Why is a new distribution needed, rather than a shifted $t$? It is true that $T-\beta_1/s(b_1)=(b_1-\beta_1)/s(b_1)\sim t_{n-2}$, so that

$$
\operatorname{Power}(\beta_1)=\mathbb{P}\left(T-\frac{\beta_1}{s(b_1)}>t_{n-2,\alpha/2}-\frac{\beta_1}{s(b_1)}\right)+\mathbb{P}\left(T-\frac{\beta_1}{s(b_1)}<-t_{n-2,\alpha/2}-\frac{\beta_1}{s(b_1)}\right).
$$
But the shift $\beta_1/s(b_1)$ contains the random $s$, so these are not probabilities of fixed events under $t_{n-2}$. Plugging in an estimate, as in $\beta_1/s(b_1)=1.5\sqrt{19800}/48.82=4.32$ for the example below, only approximates the exact noncentral computation, which uses the fixed $\delta=\beta_1/\sigma(b_1)$.

**Example 3.6.1 (Toluca Company)** A manufacturer of refrigeration equipment produces a replacement part in lots of varying size and wants to study the relationship between the lot size $X$ and the labor hours $Y$. The lot sizes range from $20$ to $120$ units, $n=25$, $S_{XX}=\sum_i(X_i-\bar X)^2=19800$, and the error standard deviation is estimated as $s=48.82$; for planning we assume $\sigma^2=50^2=2500$. Then

$$
\sigma^2(b_1)=\frac{2500}{19800}=0.1263,\qquad\sigma(b_1)=0.355.
$$
Suppose the slope of interest is $\beta_1=1.5$ (hours per unit). Then $\delta=1.5/0.355=4.22$, the critical value is $t_{23,0.025}=2.069$, and

```r
c <- qt(1 - 0.025, df = 23)                                  # 2.0687
pt(-c, df = 23, ncp = 4.225) + 1 - pt(c, df = 23, ncp = 4.225)   # 0.981
```

so $\operatorname{Power}(1.5)=0.981$. In summary:

| $n$ | $\sigma^2$ | $S_{XX}$ | $\alpha$ | $\sigma^2(b_1)$ | df | $\beta_1$ | $\delta$ | $t_{23,0.025}$ | power |
|---|---|---|---|---|---|---|---|---|---|
| $25$ | $2500$ | $19800$ | $0.05$ | $0.1263$ | $23$ | $1.5$ | $4.22$ | $2.0687$ | $0.981$ |

![Left: densities of the central t-distribution with 23 degrees of freedom and of the noncentral t-distribution with noncentrality 4.22; the shaded area beyond the critical values plus or minus 2.069 under the noncentral density is the power 0.981; right: densities of noncentral t-distributions for several degrees of freedom and noncentrality parameters](./plots/noncentral-t-power.py)

### 3.6.3. The Power Curve

To see the power over a range of slopes, choose a range (say from $-2$ to $2$), vary $\beta_1$ over equally spaced values, compute $\operatorname{Power}(\beta_1)$ for each, and plot it against $\beta_1$: this is the *power curve* of the test.

```r
find_power <- function(n, sig2, ssx, beta1, alpha) {
  sig2b1 <- sig2 / ssx                     # variance of b1
  df <- n - 2
  delta <- beta1 / sqrt(sig2b1)            # noncentrality parameter
  c <- qt(1 - alpha / 2, df)               # critical value
  1 - pt(c, df, delta) + pt(-c, df, delta)
}
beta1 <- seq(-2, 2, by = 0.05)
power <- sapply(beta1, function(b) find_power(25, 2500, 19800, b, 0.05))
plot(power ~ beta1, type = "l", ylab = "Power",
     main = "Power for the slope in simple linear regression")
```

The curve is symmetric about $0$, equals $\alpha=0.05$ at $\beta_1=0$, and increases to $1$ as $\lvert\beta_1\rvert$ grows.

![Power curves of the two-sided t-test of beta_1 = 0 at level 0.05 in the Toluca setting (sigma^2 = 2500): with n = 25 and S_XX = 19800 the power at beta_1 = 1 is 0.77, with n = 45 and S_XX = 35800 it is 0.96; both curves equal 0.05 at beta_1 = 0](./plots/power-curve-slope.py)

### 3.6.4. Sample Size Determination

In the Toluca example, $n=25$ gives $\operatorname{Power}(1.5)=0.98$, high enough for practice. If the slope of interest is $\beta_1=1.0$ instead, the same computation gives $\operatorname{Power}(1.0)=0.77$: the study is under-powered. Suppose we want $\operatorname{Power}(1)=0.95$. The primary way to increase the power is to increase the sample size $n$ together with a good design $X_1,\dots,X_n$: both enlarge $S_{XX}=\sum_i(X_i-\bar X)^2$, hence $\delta=\beta_1\sqrt{S_{XX}}/\sigma$. Adding lots with the same spread of sizes, each extra lot adding $800$ to $S_{XX}$:

| sample size | $S_{XX}$ | $\sigma^2$ | $\operatorname{Power}(1)$ |
|---|---|---|---|
| $30$ | $23800$ | $2500$ | $0.846$ |
| $35$ | $27800$ | $2500$ | $0.899$ |
| $40$ | $31800$ | $2500$ | $0.935$ |
| $45$ | $35800$ | $2500$ | $0.959$ |

The proper sample size is therefore $45$, with a design such that $S_{XX}=35800$.

**Example 3.6.2** For a single sample from a normal population with known variance $1$, test $H_0\colon\mu=0$ against $H_1\colon\mu=1$ at level $0.05$ with power $0.90$. The **Z-test** based on $n$ observations rejects when $\sqrt n\bar X\ge z_{0.05}=1.645$. Its power at $\mu=1$ is

$$
0.90=\mathbb{P}\big(\sqrt n\bar X\ge1.645\mid\mu=1\big)=\mathbb{P}\big(\sqrt n(\bar X-1)\ge1.645-\sqrt n\big)=1-\Phi(1.645-\sqrt n),
$$
so $1.645-\sqrt n=-z_{0.10}=-1.282$, $\sqrt n=2.927$ and $n=8.56$: take $n=9$. In general, to detect a mean shift $\Delta$ with a one-sided level-$\alpha$ Z-test and power $1-\gamma$, one needs $n\ge\big[(z_\alpha+z_\gamma)\sigma/\Delta\big]^2$.

### 3.6.5. Remarks

- The formulas, procedures and R code for the two-sided $t$-test are easily modified for one-sided tests and for tests about $\beta_0$.
- Power calculation and sample size determination are part of the design of a study or experiment and must be done carefully before it is carried out. When the study is important, consult an experienced applied statistician on the power calculation, the sample size and the design.
- Statistical significance is not practical significance. A model is usually only an approximation of reality, and in many cases we know without looking at the data that a point null hypothesis is false; failing to reject it may simply mean that we did not have enough data, and in this view the test becomes a test of the sample size. The larger the sample, the smaller the $p$-values and the greater the power, and the more easily statistically significant results are obtained, even when the actual effect is unimportant.
- Confidence intervals are useful even when the null hypothesis is not rejected, because they show how close to the null value the true effect is likely to be. For these reasons confidence intervals are generally preferable to bare tests.

## Summary

- Review: for a normal sample, $\bar X\sim\mathcal{N}(\mu,\sigma^2/n)$ and $(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$ are independent, so $(\bar X-\mu)/\operatorname{SE}(\bar X)\sim t_{n-1}$; this gives the $t$-test, the $p$-value and the confidence interval $\bar X\pm t_{n-1,\alpha/2}s/\sqrt n$.
- Slope: $b_1\sim\mathcal{N}(\beta_1,\sigma^2/S_{XX})$, $s(b_1)=s/\sqrt{S_{XX}}$, $(b_1-\beta_1)/s(b_1)\sim t_{n-2}$; test $H_0\colon\beta_1=0$ by $\lvert b_1\rvert/s(b_1)>t_{n-2,\alpha/2}$, interval $b_1\pm t_{n-2,\alpha/2}s(b_1)$. For bivariate normal data this is also the test of $\rho=0$.
- Intercept: $b_0\sim\mathcal{N}\big(\beta_0,\sigma^2(1/n+\bar X^2/S_{XX})\big)$, with the same kind of test and interval; usually of less interest.
- Gauss–Markov theorem: $b_0,b_1$ are the BLUEs under uncorrelated, homoscedastic errors with mean zero.
- Joint inference: the product of two individual $1-\alpha$ intervals has level below $1-\alpha$; the Bonferroni correction uses $t_{n-2,\alpha/4}$ for each.
- Power: $b_1/s(b_1)\sim t_{n-2}(\delta)$ with $\delta=\beta_1\sqrt{S_{XX}}/\sigma$; the power grows with $\lvert\beta_1\rvert$, with $n$ and with the spread of the $X_i$. Plan the sample size before the study, and prefer confidence intervals to bare significance statements.
