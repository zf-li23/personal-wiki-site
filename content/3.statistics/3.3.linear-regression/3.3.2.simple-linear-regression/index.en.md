---
title: Simple Linear Regression
description: The simple linear regression model with general and with normal errors, its assumptions (LINE) and the meaning of its parameters; least squares estimation, fitted values and residuals, the error mean square as estimator of the error variance, and maximum likelihood estimation, illustrated by the Leaning Tower of Pisa in R.
---

The previous chapter ended with the regression function $\mathbb{E}(Y\mid X=x)$ of a bivariate normal distribution. In most applications, however, $X$ is not random in the same way as $Y$: it is a dose chosen by the experimenter, a year, a lot size. This chapter sets up the **simple linear regression model**, in which the mean of the response is a linear function of one predictor and the deviations from that line are random errors, and studies its two classical estimation methods. **Least squares** needs only assumptions about the means and variances of the errors; **maximum likelihood estimation** needs their distribution, and under normal errors the two give the same line. The model was met briefly in [3.2.3](/3.2.3); here it is developed in full, with the residuals that will serve for model checking in [3.3.5](/3.3.5). Inference for the parameters follows in [3.3.3](/3.3.3), and the matrix form for several predictors in [3.3.7](/3.3.7).

## 2.1. The Simple Linear Regression Model

### 2.1.1. Data and Model

We observe $n$ pairs $(X_1,Y_1),\dots,(X_n,Y_n)$; each pair $(X_i,Y_i)$ is called a *case*, $X_i$ is the $i$-th observed value of the explanatory variable and $Y_i$ the $i$-th observed response, and $n$ is the **sample size**. A *deterministic* (functional) relationship $Y=f(X)$ would put all points exactly on a curve; a *statistical* relationship allows the observations to scatter around it.

**Definition 2.1.1 (Simple Linear Regression Model)** The **simple linear regression model** is

$$
Y_i=\beta_0+\beta_1X_i+\varepsilon_i,\qquad i=1,\dots,n,
$$
where the $X_i$ are known constants, $\beta_0$ (the **intercept**) and $\beta_1$ (the **slope**) are unknown parameters, and the **random error terms** $\varepsilon_i$ satisfy $\mathbb{E}(\varepsilon_i)=0$, $\operatorname{Var}(\varepsilon_i)=\sigma^2$, and $\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$ for $i\ne j$.

The model is "simple" because there is one predictor, and "linear" because it is linear in the parameters $\beta_0,\beta_1$ (and here also in the predictor). The error term represents the intrinsic variability of the response: the part not determined by $X$, whether it comes from measurement error, from omitted variables, or from genuine randomness. The parameters $\beta_0$, $\beta_1$ and $\sigma^2$ are unknown constants and the targets of **statistical inference**, the process of deducing properties of the parameters from the data.

### 2.1.2. The Model with Normal Errors

For exact tests and intervals we add a distributional assumption.

**Definition 2.1.2 (Normal Error Regression Model)** The **normal error regression model** is the simple linear regression model with

$$
\varepsilon_1,\dots,\varepsilon_n\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2).
$$

Uncorrelated normal errors are independent (their joint distribution is multivariate normal with diagonal covariance matrix), so the model is equivalent to: $Y_1,\dots,Y_n$ are independent, and

$$
Y_i\sim\mathcal{N}(\beta_0+\beta_1X_i,\ \sigma^2),\qquad i=1,\dots,n.
$$
At each level of $X$ the responses follow a normal distribution with mean on the line $\beta_0+\beta_1X$ and with the same spread.

### 2.1.3. Assumptions and the Meaning of the Parameters

Both models share the following features. Since $\mathbb{E}(\varepsilon_i)=0$,

$$
\mathbb{E}(Y_i)=\beta_0+\beta_1X_i+\mathbb{E}(\varepsilon_i)=\beta_0+\beta_1X_i,\qquad\operatorname{Var}(Y_i)=\operatorname{Var}(\varepsilon_i)=\sigma^2.
$$
The mean of $Y_i$ is determined by the value of $X_i$; all possible means fall on the line

$$
\mathbb{E}(Y)=\beta_0+\beta_1X,
$$
the *population regression line* (the regression function of the model), and the $Y_i$ vary about this line with constant variance. The **normal distribution** of the errors is an additional feature of the second model. The four conditions that make up the simple linear regression model with normal errors are summarized by the acronym LINE.

- Linear function (L): the mean of the response at each value of the predictor is a linear function of the predictor.
- Independent (I): the errors are independent.
- Normally distributed (N): the errors at each value of the predictor are normally distributed.
- Equal variances (E): the errors at each value of the predictor have the same variance $\sigma^2$.

The population regression line is a fixed, unknown line; the *estimated regression line* $\hat Y=b_0+b_1X$ computed below is a random line that changes from sample to sample.

The slope $\beta_1$ is the change in the mean of the probability distribution of $Y$ per unit increase in $X$. The intercept $\beta_0$ is the mean of $Y$ at $X=0$, and it has this interpretation only when the scope of the model includes $X=0$. If the data cover, say, lot sizes from $20$ to $120$ units, $\beta_0$ is merely the height of the line extended far outside the data, and it should not be interpreted.

## 2.2. Least Squares Estimation

### 2.2.1. The Least Squares Principle

How should we estimate the response at a given level $X=x$? If $X$ is ignored (or has no effect on $Y$), the natural estimate is a single number $c$ that is close to all the responses, and the minimizer of $\sum_{i=1}^n(Y_i-c)^2$ is $c=\bar Y$. If $X$ is taken into account, we choose a line instead of a number. For each case, the observed response is $Y_i=\beta_0+\beta_1X_i+\varepsilon_i$, the response predicted by a candidate line is $b_0+b_1X_i$, and the difference is $Y_i-b_0-b_1X_i$. The least squares principle chooses the line that minimizes the sum of the squared differences over all cases,

$$
Q(b_0,b_1)=\sum_{i=1}^n(Y_i-b_0-b_1X_i)^2,\qquad(b_0,b_1)=\arg\min_{b_0,b_1}Q(b_0,b_1).
$$

Write $\bar X=\frac1n\sum_iX_i$, $\bar Y=\frac1n\sum_iY_i$ and

$$
S_{XX}=\sum_{i=1}^n(X_i-\bar X)^2,\qquad S_{XY}=\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y).
$$

**Theorem 2.2.1** If the $X_i$ are not all equal ($S_{XX}>0$), the least squares estimates are

$$
b_1=\hat\beta_1=\frac{S_{XY}}{S_{XX}}=\frac{\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y)}{\sum_{i=1}^n(X_i-\bar X)^2},\qquad b_0=\hat\beta_0=\bar Y-b_1\bar X.
$$

**Proof** $Q$ is a convex quadratic function of $(b_0,b_1)$, so its minimizers are the solutions of the **normal equations**

$$
\frac{\partial Q}{\partial b_0}=-2\sum_{i=1}^n(Y_i-b_0-b_1X_i)=0,\qquad\frac{\partial Q}{\partial b_1}=-2\sum_{i=1}^nX_i(Y_i-b_0-b_1X_i)=0.
$$
The first gives $b_0=\bar Y-b_1\bar X$. Substituting into the second, $\sum_iX_i\big[(Y_i-\bar Y)-b_1(X_i-\bar X)\big]=0$, and since $\sum_i\bar X(Y_i-\bar Y)=\sum_i\bar X(X_i-\bar X)=0$ this is $S_{XY}-b_1S_{XX}=0$. The Hessian $2\begin{bmatrix}n&\sum X_i\\\sum X_i&\sum X_i^2\end{bmatrix}$ has determinant $4nS_{XX}>0$, so the solution is the unique minimizer. $\square$

Here $b_1$ is the estimated slope (an estimator of $\beta_1$) and $b_0$ the estimated intercept. Dividing numerator and denominator by $n-1$ shows $b_1=r\,s_Y/s_X$, where $r$ is the sample correlation and $s_X,s_Y$ the sample standard deviations: Galton's adjusted slope of [3.3.1](/3.3.1).

### 2.2.2. Fitted Values and Residuals

**Definition 2.2.1** The *estimated regression function* is $\hat Y=b_0+b_1X$. For case $i$, the **fitted value** is $\hat Y_i=b_0+b_1X_i$ and the **residual** is

$$
e_i=Y_i-\hat Y_i=Y_i-(b_0+b_1X_i).
$$

The residual is not the error term. Since $Y_i=\beta_0+\beta_1X_i+\varepsilon_i$,

$$
e_i=(\beta_0-b_0)+(\beta_1-b_1)X_i+\varepsilon_i,
$$
so $e_i\approx\varepsilon_i$ only when the fitted line is close to the true line: $\varepsilon_i$ is the vertical deviation of $Y_i$ from the unknown population line, $e_i$ its deviation from the estimated line. When the model is adequate the residuals reflect the error terms, which makes them highly useful for studying whether a given regression model is appropriate for the data at hand ([3.3.5](/3.3.5)).

**Proposition 2.2.1** The least squares fit has the following properties.

1. $\sum_{i=1}^ne_i=0$ and $\sum_{i=1}^nX_ie_i=0$.
2. $\sum_{i=1}^n\hat Y_ie_i=0$ and $\sum_{i=1}^n\hat Y_i=\sum_{i=1}^nY_i$.
3. $\sum_{i=1}^ne_i^2=Q(b_0,b_1)$ is the minimum of $Q$.
4. The estimated regression line passes through the point $(\bar X,\bar Y)$.

**Proof** Item 1 is the pair of normal equations with $(b_0,b_1)$ inserted. Then $\sum_i\hat Y_ie_i=b_0\sum_ie_i+b_1\sum_iX_ie_i=0$ and $\sum_i(Y_i-\hat Y_i)=\sum_ie_i=0$. Item 3 is the definition of $(b_0,b_1)$, and item 4 is $b_0+b_1\bar X=\bar Y$. $\square$

In particular the $n$ residuals are not free: they satisfy two linear constraints.

### 2.2.3. Estimating the Error Variance

For a single sample from one population, $\sigma^2=\operatorname{Var}(Y)$ is estimated by the sample variance $\sum_i(Y_i-\bar Y)^2/(n-1)$. In regression this is wrong: the $Y_i$ come from different probability distributions whose means $\beta_0+\beta_1X_i$ depend on the level $X_i$, and $\sum_i(Y_i-\bar Y)^2$ also contains the variation of these means. Each deviation must be calculated around its own estimated mean $\hat Y_i$, and these deviations are the residuals. Since $e_i\approx\varepsilon_i$ and $\sigma^2=\operatorname{Var}(\varepsilon_i)=\mathbb{E}(\varepsilon_i^2)$, a natural first guess is $\frac1n\sum_ie_i^2$. But by Proposition 2.2.1 the residuals satisfy two linear constraints, so they carry only $n-2$ **degrees of freedom**, and the right divisor is $n-2$.

**Definition 2.2.2** The **error sum of squares** and the **error mean square** are

$$
\mathrm{SSE}=\sum_{i=1}^n(Y_i-\hat Y_i)^2=\sum_{i=1}^ne_i^2,\qquad\mathrm{MSE}=\frac{\mathrm{SSE}}{n-2}.
$$
The estimator of $\sigma^2$ is $s^2=\hat\sigma^2=\mathrm{MSE}$, and $s=\sqrt{\mathrm{MSE}}$ (the *residual standard error*) estimates $\sigma$.

**Theorem 2.2.2** Under the simple linear regression model, $\mathbb{E}(\mathrm{SSE})=(n-2)\sigma^2$, so $\mathbb{E}(\mathrm{MSE})=\sigma^2$.

**Proof** Write $Y_i-\bar Y=\beta_1(X_i-\bar X)+(\varepsilon_i-\bar\varepsilon)$. By Proposition 2.2.1,

$$
\mathrm{SSE}=\sum_i\big[(Y_i-\bar Y)-b_1(X_i-\bar X)\big]^2=\sum_i(Y_i-\bar Y)^2-b_1^2S_{XX}.
$$
Now $\mathbb{E}\sum_i(Y_i-\bar Y)^2=\beta_1^2S_{XX}+\mathbb{E}\sum_i(\varepsilon_i-\bar\varepsilon)^2=\beta_1^2S_{XX}+(n-1)\sigma^2$, and by Theorem 2.2.3 below $\mathbb{E}(b_1^2)=\operatorname{Var}(b_1)+\beta_1^2=\sigma^2/S_{XX}+\beta_1^2$. Hence $\mathbb{E}(\mathrm{SSE})=(n-1)\sigma^2-\sigma^2=(n-2)\sigma^2$. $\square$

### 2.2.4. Properties of the Least Squares Estimators

The estimators are linear in the responses. Since $\sum_i(X_i-\bar X)=0$,

$$
b_1=\sum_{i=1}^nk_iY_i,\qquad k_i=\frac{X_i-\bar X}{S_{XX}},\qquad\sum_ik_i=0,\quad\sum_ik_iX_i=1,\quad\sum_ik_i^2=\frac1{S_{XX}},
$$
and $b_0=\bar Y-b_1\bar X=\sum_i\big(\frac1n-\bar Xk_i\big)Y_i$.

**Theorem 2.2.3** Under the simple linear regression model,

$$
\mathbb{E}(b_1)=\beta_1,\quad\operatorname{Var}(b_1)=\frac{\sigma^2}{S_{XX}},\qquad\mathbb{E}(b_0)=\beta_0,\quad\operatorname{Var}(b_0)=\sigma^2\left(\frac1n+\frac{\bar X^2}{S_{XX}}\right),\qquad\operatorname{Cov}(\bar Y,b_1)=0.
$$

**Proof** $\mathbb{E}(b_1)=\sum_ik_i(\beta_0+\beta_1X_i)=\beta_0\sum_ik_i+\beta_1\sum_ik_iX_i=\beta_1$, and since the $Y_i$ are uncorrelated with variance $\sigma^2$, $\operatorname{Var}(b_1)=\sigma^2\sum_ik_i^2=\sigma^2/S_{XX}$. Next $\operatorname{Cov}(\bar Y,b_1)=\sum_i\frac1nk_i\sigma^2=0$, so $\mathbb{E}(b_0)=\beta_0+\beta_1\bar X-\beta_1\bar X=\beta_0$ and $\operatorname{Var}(b_0)=\operatorname{Var}(\bar Y)+\bar X^2\operatorname{Var}(b_1)=\sigma^2/n+\bar X^2\sigma^2/S_{XX}$. $\square$

Thus $b_0$, $b_1$ and $s^2$ are **unbiased estimators**. They are also optimal: among all unbiased estimators that are linear in $Y_1,\dots,Y_n$, $b_0$ and $b_1$ have the smallest variance (the **Gauss–Markov theorem**, [3.3.3](/3.3.3)), and under normal errors $s^2$ is the minimum-variance unbiased estimator of $\sigma^2$ ([3.2.3](/3.2.3)).

### 2.2.5. Example: The Leaning Tower of Pisa

Construction of the bell tower of Pisa began in 1173, and by 1178, when the second floor was built, it had begun to sink. Construction resumed in 1272; to compensate for the tilt, the engineers built the upper levels with one side taller. The seventh floor was completed in 1319 and the bell chamber added in 1372. The tilt continued to grow and was monitored; the tower was closed in 1990, and stabilization, by removing soil from under the taller side, was completed in 2008. The monitoring data below give the lean $Y$ (in tenths of a millimeter in excess of $2.9$ meters) for the years $X=75,\dots,87$ (that is, 1975–1987).

| year $X$ | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| lean $Y$ | 642 | 644 | 656 | 667 | 673 | 688 | 696 | 698 | 713 | 717 | 725 | 742 | 757 |

A scatterplot, with a locally weighted smoother (`lowess`) as a nonparametric guide, shows an almost perfectly linear increase. The line is fitted with `lm`:

```r
towerpisa <- read.table("pisa.txt", header = TRUE)   # columns: year, lean
plot(lean ~ year, data = towerpisa, xlab = "Year", ylab = "Lean", las = 1)
lines(lowess(towerpisa$year, towerpisa$lean), col = 2)   # locally weighted smoother
bc <- lm(lean ~ year, data = towerpisa)
summary(bc)
abline(bc, col = 3, lty = 2)
```

The output contains:

| | Estimate | Std. Error | $t$ value | $\mathbb{P}(>\lvert t\rvert)$ |
|---|---|---|---|---|
| (Intercept) | $-61.1209$ | $25.1298$ | $-2.432$ | $0.0333$ |
| year | $9.3187$ | $0.3099$ | $30.069$ | $6.5\times10^{-12}$ |

with residual standard error $4.181$ on $11$ degrees of freedom, multiple $R^2=0.988$, and $F=904.1$ on $1$ and $11$ degrees of freedom. The estimated regression line is

$$
\hat Y=-61.12+9.3187X:
$$
the lean grew by about $9.3$ tenths of a millimeter, almost $1$ mm, per year. The intercept would be the lean in the year 1900, far outside the data, and has no physical meaning. With $n=13$ cases the error degrees of freedom are $13-2=11$, and

$$
\mathrm{SSE}=\sum_ie_i^2=192.29,\qquad\mathrm{MSE}=\frac{192.29}{11}=17.48,\qquad s=\sqrt{17.48}=4.181,
$$
which is the residual standard error reported by R (`sum(bc$residuals^2)` gives the SSE). For 1982 the fitted value is $\hat Y_{82}=b_0+82\,b_1=703.0$ and the residual is $e_{82}=698-703.0=-5.0$.

![The Pisa data with the least squares line Y_hat = -61.12 + 9.32 X; the vertical segments are the residuals, whose squares sum to SSE = 192.3, and the residual at 1982 is e = -5.0](./plots/pisa-least-squares.py)

The residuals tell us not only about the errors but also how well the model fits the data. A *residual plot* plots the residuals against the predictor (or against the fitted values); if the model is adequate it shows a structureless horizontal band around $0$. A **normal Q–Q plot** of the residuals ([3.2.6](/3.2.6)) plots the ordered residuals against the standard normal quantiles $\Phi^{-1}\big((i-0.5)/n\big)$ and checks the normality assumption. Both are the basic tools of the diagnostics in [3.3.5](/3.3.5).

```r
plot(towerpisa$year, residuals(bc), las = 1, xlab = "Year", ylab = "Residual")
abline(h = 0)
qqnorm(residuals(bc), datax = TRUE)
qqline(residuals(bc), datax = TRUE)
```

![Left: residual plot of the Pisa fit against the year, a band around zero with no clear trend; right: normal Q-Q plot of the residuals, which lie close to a straight line](./plots/pisa-residual-diagnostics.py)

The residuals range from $-5.97$ to $7.40$ and show no clear pattern. Two cautions apply. First, the observations are consecutive years of one tower, so the data form a time series, and the independence of the errors cannot be taken for granted; it has to be checked ([3.3.5](/3.3.5)). Second, predicting the lean far outside the observed years (the data file also contains the year $116$, i.e. 2016, with a missing lean, which `lm` drops) is an extrapolation that the model cannot support, all the more because the stabilization work changed the process itself.

## 2.3. Maximum Likelihood Estimation

The **likelihood function** measures how "likely" each value of the parameters is in light of the observed data; given a statistical model, all the evidence in the sample about the parameters is contained in it. Under normal errors the density of $Y_i$ is

$$
f(Y_i\mid\beta_0,\beta_1,\sigma^2)=\frac1{\sqrt{2\pi\sigma^2}}\exp\left\{-\frac{(Y_i-\beta_0-\beta_1X_i)^2}{2\sigma^2}\right\},
$$
and by independence the likelihood is the product

$$
L(\beta_0,\beta_1,\sigma^2)=\prod_{i=1}^nf(Y_i\mid\beta_0,\beta_1,\sigma^2)=(2\pi\sigma^2)^{-n/2}\exp\left\{-\frac{1}{2\sigma^2}\sum_{i=1}^n(Y_i-\beta_0-\beta_1X_i)^2\right\}.
$$

**Theorem 2.3.1** Under the normal error regression model, the maximum likelihood estimators are

$$
\hat\beta_0=b_0,\qquad\hat\beta_1=b_1,\qquad\hat\sigma^2=\frac{1}{n}\sum_{i=1}^n(Y_i-\hat Y_i)^2=\frac{\mathrm{SSE}}{n}=\frac{n-2}{n}\,\mathrm{MSE}.
$$

**Proof** Maximizing $L$ is equivalent to minimizing

$$
-\log L=\frac n2\log(2\pi\sigma^2)+\frac{Q(\beta_0,\beta_1)}{2\sigma^2}.
$$
For every fixed $\sigma^2$ this is minimized in $(\beta_0,\beta_1)$ by minimizing $Q$, that is, by the least squares estimates. Setting the derivative with respect to $\sigma^2$ at $(b_0,b_1)$ to zero, $\frac{n}{2\sigma^2}-\frac{\mathrm{SSE}}{2\sigma^4}=0$, gives $\hat\sigma^2=\mathrm{SSE}/n$. $\square$

The two methods differ in what they assume and, in general, in what they give.

| | Least squares | Maximum likelihood |
|---|---|---|
| assumptions | means and variances of the errors (Definition 2.1.1) | full distribution of the errors (Definition 2.1.2) |
| $\beta_0,\beta_1$ | $b_0,b_1$ | $b_0,b_1$ (under normal errors) |
| $\sigma^2$ | $\mathrm{MSE}=\mathrm{SSE}/(n-2)$, unbiased | $\mathrm{SSE}/n$, biased downward |

Maximum likelihood estimates rely on distributional assumptions and least squares estimates do not; in general the MLEs and the LSEs are different, and they coincide for the coefficients here only because the normal log-likelihood is a decreasing function of the sum of squares. With other error distributions, such as the Laplace distribution, maximum likelihood leads to other criteria, such as least absolute deviations. The same comparison, including the method of moments, is made in [3.2.3](/3.2.3).

## Summary

- Simple linear regression model: $Y_i=\beta_0+\beta_1X_i+\varepsilon_i$ with $\mathbb{E}(\varepsilon_i)=0$, $\operatorname{Var}(\varepsilon_i)=\sigma^2$, uncorrelated errors; the normal error model adds $\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$, i.e. $Y_i\sim\mathcal{N}(\beta_0+\beta_1X_i,\sigma^2)$ independently. Assumptions: LINE (linear mean, independent, normal, equal variances).
- $\beta_1$ is the change in the mean response per unit of $X$; $\beta_0$ is interpretable only if $X=0$ lies in the scope of the model.
- Least squares: $b_1=S_{XY}/S_{XX}$, $b_0=\bar Y-b_1\bar X$; the residuals $e_i=Y_i-\hat Y_i$ satisfy $\sum e_i=0$, $\sum X_ie_i=0$, and the fitted line passes through $(\bar X,\bar Y)$.
- Error variance: $s^2=\mathrm{MSE}=\mathrm{SSE}/(n-2)$ is unbiased; the $n-2$ reflects the two estimated parameters.
- $b_0,b_1$ are linear in $Y$ and unbiased, with $\operatorname{Var}(b_1)=\sigma^2/S_{XX}$ and $\operatorname{Var}(b_0)=\sigma^2(1/n+\bar X^2/S_{XX})$.
- Maximum likelihood under normal errors gives the same $b_0,b_1$ and $\hat\sigma^2=\mathrm{SSE}/n$.
- In R: `lm(y ~ x)`, `summary()`, `residuals()`; residual plots and normal Q–Q plots of the residuals are the first checks of the model.
