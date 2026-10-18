---
title: Prediction and Analysis of Variance
description: Using a fitted simple linear regression; confidence intervals for the mean response, prediction intervals for new observations and their means, the Working–Hotelling confidence band for the whole line; the analysis of variance (partition of sums of squares, degrees of freedom, expected mean squares, F-test, ANOVA table), the general linear test, and the coefficient of determination and its relation to the correlation coefficient.
---

A typical regression analysis involves four steps: model formulation, model estimation, model evaluation and model use. The previous chapters formulated the simple linear regression model ([3.3.2](/3.3.2)) and made inference about its parameters ([3.3.3](/3.3.3)). This chapter is about using and evaluating it. The first half answers the questions a fitted line is usually asked: what is the mean response at a given level of $X$, where will a new observation fall, and how well is the whole line determined. The difference between estimating a mean and predicting an observation, and between a single interval and a simultaneous band, recurs throughout the course. The second half looks at the fit from the point of view of the **analysis of variance**: the total variation of the responses is split into a part explained by the regression and a part left to the errors. This leads to the $F$-test, to the general linear test, which compares a full and a reduced model and is the main testing tool for multiple regression ([3.3.9](/3.3.9)), and to the coefficient of determination $R^2$.

## 4.1. Estimating the Mean Response

### 4.1.1. The Estimator and Its Distribution

At a level $X=X_h$ of the predictor (within the scope of the model, but not necessarily one of the observed $X_i$), the mean response is

$$
\mathbb{E}(Y_h)=\mu_h=\beta_0+\beta_1X_h,
$$
a parameter induced by $\beta_0$ and $\beta_1$. We estimate it by the fitted value

$$
\hat Y_h=\hat\mu_h=b_0+b_1X_h.
$$

**Theorem 4.1.1** Under the simple linear regression model, $\hat Y_h$ is unbiased for $\mathbb{E}(Y_h)$, with

$$
\sigma^2(\hat Y_h)=\operatorname{Var}(\hat Y_h)=\sigma^2\left[\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right],
$$
and among all linear unbiased estimators of $\beta_0+\beta_1X_h$ it has the smallest variance. Under normal errors, $\hat Y_h\sim\mathcal{N}\big(\mathbb{E}(Y_h),\sigma^2(\hat Y_h)\big)$.

**Proof** Since $b_0=\bar Y-b_1\bar X$,

$$
\hat Y_h=\bar Y+b_1(X_h-\bar X).
$$
Unbiasedness follows from $\mathbb{E}(\bar Y)=\beta_0+\beta_1\bar X$ and $\mathbb{E}(b_1)=\beta_1$. Since $\operatorname{Cov}(\bar Y,b_1)=0$ ([3.3.2](/3.3.2)), $\operatorname{Var}(\hat Y_h)=\sigma^2/n+(X_h-\bar X)^2\sigma^2/S_{XX}$. The minimum variance property is proved as the **Gauss–Markov theorem** ([3.3.3](/3.3.3)), with the constraints $\sum_ic_i=1$ and $\sum_ic_iX_i=X_h$. Under normal errors $\hat Y_h$ is a linear combination of independent normal variables. $\square$

Replacing $\sigma^2$ by $\mathrm{MSE}$ gives the estimated variance and the standard error,

$$
s^2(\hat Y_h)=\mathrm{MSE}\left[\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right],\qquad\frac{\hat Y_h-\mathbb{E}(Y_h)}{s(\hat Y_h)}\sim t_{n-2},
$$
by the same argument as for $b_1$ in [3.3.3](/3.3.3). Tests and **confidence intervals** for $\mathbb{E}(Y_h)$ follow; the $100(1-\alpha)\%$ confidence interval is

$$
\hat Y_h\pm t_{n-2,\alpha/2}\,s(\hat Y_h).
$$

The standard error grows with the distance of $X_h$ from $\bar X$: the mean response is estimated most precisely at the center of the data. The reason is the uncertainty in the slope. The estimated line always passes through $(\bar X,\bar Y)$, and like a teeter-totter pivoting at its middle, a change of the slope has a bigger impact the farther we move from $\bar X$. At $X_h=0$ the formula reduces to $s^2(b_0)=\mathrm{MSE}\,(1/n+\bar X^2/S_{XX})$ of [3.3.3](/3.3.3).

### 4.1.2. Example: The Toluca Company

The Toluca Company of Example 3.6.1 in [3.3.3](/3.3.3) manufactures a replacement part for refrigeration equipment in lots of varying size. To determine the optimum lot size, it first needs the relationship between the labor hours $Y$ and the lot size $X$. The $n=25$ observed lots have sizes from $20$ to $120$ units with $\bar X=70$ and $S_{XX}=19800$. The least squares fit is

| | Estimate | Std. Error | $t$ value | $\mathbb{P}(>\lvert t\rvert)$ |
|---|---|---|---|---|
| (Intercept) | $62.366$ | $26.177$ | $2.382$ | $0.0259$ |
| lotsize | $3.570$ | $0.347$ | $10.290$ | $4.45\times10^{-10}$ |

with residual standard error $s=48.82$ on $23$ degrees of freedom: each additional unit in a lot requires about $3.57$ more labor hours. The confidence intervals for the mean response at all observed lot sizes and at the new sizes $65$ and $100$ are obtained with `predict`:

```r
toluca <- read.table("CH01TA01.txt", col.names = c("lotsize", "hours"))
reg <- lm(hours ~ lotsize, data = toluca)
predict(reg, newdata = data.frame(lotsize = c(65, 100)),
        interval = "confidence", level = 0.95)
```

or directly from the formula:

```r
n <- nrow(toluca); x <- toluca$lotsize; xnew <- 100; alpha <- 0.05
s2 <- sum(residuals(reg)^2) / (n - 2)                 # MSE
ssx <- sum((x - mean(x))^2)
muh <- coef(reg)[1] + coef(reg)[2] * xnew             # fitted mean response
wid <- qt(1 - alpha / 2, df = n - 2) * sqrt((1 / n + (xnew - mean(x))^2 / ssx) * s2)
c(muh - wid, muh + wid)
```

| $X_h$ | $\hat Y_h$ | $95\%$ confidence interval | width |
|---|---|---|---|
| $80$ | $347.98$ | $(326.54,\ 369.42)$ | $43$ |
| $30$ | $169.47$ | $(134.37,\ 204.58)$ | $70$ |
| $65$ | $294.43$ | $(273.91,\ 314.95)$ | $41$ |
| $100$ | $419.39$ | $(389.86,\ 448.91)$ | $59$ |

The widths confirm the pattern: the intervals are narrowest near $\bar X=70$ and widen toward the ends of the data, the interval at $X_h=30$ (distance $40$ from $\bar X$) being wider than that at $X_h=100$ (distance $30$).

## 4.2. Predicting a New Observation

### 4.2.1. The Prediction Interval

Now we want to predict the value of a single new observation at $X=X_h$,

$$
Y_{h(\mathrm{new})}=\beta_0+\beta_1X_h+\varepsilon_{h(\mathrm{new})},
$$
where the new error is independent of the $n$ observations used for the fit. Since $\mathbb{E}(\varepsilon_{h(\mathrm{new})})=0$, the predicted value is the same as the estimated mean, $\hat Y_h=b_0+b_1X_h$; this is also how a missing response is filled in (in the Pisa data of [3.3.2](/3.3.2), the year with a missing lean). The interval, however, must be wider, because two sources of variation are involved:

1. variation in the possible location of the distribution of $Y$, that is, the uncertainty of $\hat Y_h$ as an estimate of the mean;
2. variation within the probability distribution of $Y$, the new error itself.

Formally, the *prediction error* is

$$
Y_{h(\mathrm{new})}-\hat Y_h=\big[\mathbb{E}(Y_h)-\hat Y_h\big]+\varepsilon_{h(\mathrm{new})},
$$
with mean $0$ and, the two terms being independent,

$$
\sigma^2(\mathrm{pred})=\operatorname{Var}\big(Y_{h(\mathrm{new})}-\hat Y_h\big)=\sigma^2+\sigma^2(\hat Y_h)=\sigma^2\left[1+\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right].
$$
Under normal errors the prediction error is $\mathcal{N}\big(0,\sigma^2(\mathrm{pred})\big)$, and with

$$
s^2(\mathrm{pred})=\mathrm{MSE}\left[1+\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right],\qquad\frac{Y_{h(\mathrm{new})}-\hat Y_h}{s(\mathrm{pred})}\sim t_{n-2}.
$$
Hence $\mathbb{P}\big(\lvert Y_{h(\mathrm{new})}-\hat Y_h\rvert<t_{n-2,\alpha/2}\,s(\mathrm{pred})\big)=1-\alpha$.

**Definition 4.2.1** The random interval

$$
\hat Y_h\pm t_{n-2,\alpha/2}\,s(\mathrm{pred})
$$
which contains the new observation $Y_{h(\mathrm{new})}$ with probability $1-\alpha$ is the $100(1-\alpha)\%$ **prediction interval** for $Y_{h(\mathrm{new})}$.

A prediction interval is a kind of confidence interval for a random quantity: we choose a range of the distribution of $Y$ in which most observations fall and declare that the next observation will fall in it. Its usefulness depends, as always, on its width and on the precision the user needs. Two differences from the confidence interval for the mean are essential.

- The extra $1$ under the square root does not vanish as $n\to\infty$: as the sample grows the confidence interval shrinks to the point $\mathbb{E}(Y_h)$, but the prediction interval tends to $\mathbb{E}(Y_h)\pm z_{\alpha/2}\sigma$.
- The prediction interval depends strongly on the normality of the error terms, because it covers a single error $\varepsilon_{h(\mathrm{new})}$ and no averaging takes place. The confidence interval for the mean response concerns $\hat Y_h$, a linear combination of all the $Y_i$, which is approximately normal for large $n$ by the **central limit theorem** even if the errors are not.

### 4.2.2. Example: Prediction for the Toluca Company

In R, `interval = "prediction"` replaces the confidence interval by the prediction interval; in the formula code above, `(1 / n + ...)` becomes `(1 + 1 / n + ...)`.

```r
predict(reg, newdata = data.frame(lotsize = c(65, 100)),
        interval = "prediction", level = 0.95)
```

| $X_h$ | $\hat Y_h$ | $95\%$ prediction interval | width | width of the confidence interval |
|---|---|---|---|---|
| $80$ | $347.98$ | $(244.73,\ 451.23)$ | $206$ | $43$ |
| $30$ | $169.47$ | $(62.55,\ 276.40)$ | $214$ | $70$ |
| $65$ | $294.43$ | $(191.37,\ 397.49)$ | $206$ | $41$ |
| $100$ | $419.39$ | $(314.16,\ 524.61)$ | $210$ | $59$ |

The prediction intervals are about five times as wide as the confidence intervals, and they vary much less with $X_h$, since the dominant term is the error variance $\mathrm{MSE}=2384$.

### 4.2.3. The Mean of Several New Observations

Consider the heights of Tsinghua students. "What is the average height of sophomores?" asks for a mean response; "a sophomore is picked at random: what will his height be?" asks for a single new observation. "A class of $30$ sophomores is picked at random: what will their average height be?" lies between these two extremes: it asks for the mean $\bar Y_{h(\mathrm{new})}$ of $m$ new observations, all at $X=X_h$. The estimator is again $\hat Y_h$, and since the average of $m$ independent new errors has variance $\sigma^2/m$, the $100(1-\alpha)\%$ prediction interval becomes

$$
\hat Y_h\pm t_{n-2,\alpha/2}\,s(\mathrm{predmean}),\qquad s^2(\mathrm{predmean})=\mathrm{MSE}\left[\frac1m+\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right].
$$
For $m=1$ this is the prediction interval, and as $m\to\infty$ it becomes the confidence interval for the mean response.

## 4.3. Confidence Band for the Regression Line

For each fixed $x$ the confidence interval $\big(l(x),u(x)\big)$ satisfies $\mathbb{P}\big[l(x)<\beta_0+\beta_1x<u(x)\big]=1-\alpha$. Does it follow that $\mathbb{P}\big[l(x)<\beta_0+\beta_1x<u(x)\text{ for all }x\big]=1-\alpha$? No: the probability that all the intervals cover simultaneously is smaller, and the pointwise intervals do not form a proper confidence band.

**Definition 4.3.1** Lower and upper functions $L(x)$, $U(x)$ computed from the sample with

$$
\mathbb{P}\big[L(x)<\beta_0+\beta_1x<U(x)\text{ for all }x\in\mathbb{R}\big]=1-\alpha
$$
define the $100(1-\alpha)\%$ **confidence band** $\{(x,y)\colon L(x)<y<U(x),\ x\in\mathbb{R}\}$ for the regression line $y=\beta_0+\beta_1x$.

Instead of the sampling distribution of $(\hat Y_x-\mu_x)/s(\hat Y_x)$ at one $x$, where $\mu_x=\beta_0+\beta_1x$ and $\hat Y_x=b_0+b_1x$, we use that of its maximum over all $x$.

**Theorem 4.3.1 (Working–Hotelling Confidence Band)** Under the normal error regression model, with

$$
W^2=2F_{2,n-2,\alpha},
$$
the band $\hat Y_x\pm W\,s(\hat Y_x)$, $x\in\mathbb{R}$, has simultaneous confidence level exactly $1-\alpha$:

$$
\mathbb{P}\big[\lvert\hat Y_x-\mu_x\rvert\le W\,s(\hat Y_x)\text{ for all }x\big]=1-\alpha.
$$

**Proof** Let $\boldsymbol{\theta}=(b_0-\beta_0,\ b_1-\beta_1)^{\mathsf T}$ and $\boldsymbol{a}_x=(1,x)^{\mathsf T}$, so that $\hat Y_x-\mu_x=\boldsymbol{a}_x^{\mathsf T}\boldsymbol{\theta}$. The vector $\boldsymbol{\theta}$ is bivariate normal with mean $\boldsymbol{0}$ and covariance matrix $\sigma^2M^{-1}$, where $M=\begin{bmatrix}n&\sum_iX_i\\\sum_iX_i&\sum_iX_i^2\end{bmatrix}$ (one checks that $\sigma^2\boldsymbol{a}_x^{\mathsf T}M^{-1}\boldsymbol{a}_x$ is the variance $\sigma^2(\hat Y_x)$ of Theorem 4.1.1). By the Cauchy–Schwarz inequality applied to $M^{-1/2}\boldsymbol{a}$ and $M^{1/2}\boldsymbol{\theta}$,

$$
\frac{(\boldsymbol{a}^{\mathsf T}\boldsymbol{\theta})^2}{\boldsymbol{a}^{\mathsf T}M^{-1}\boldsymbol{a}}\le\boldsymbol{\theta}^{\mathsf T}M\boldsymbol{\theta}\quad\text{for all }\boldsymbol{a}\ne\boldsymbol{0},
$$
with equality for $\boldsymbol{a}$ proportional to $M\boldsymbol{\theta}$. The left side does not change when $\boldsymbol{a}$ is rescaled, and the directions of the vectors $\boldsymbol{a}_x$, $x\in\mathbb{R}$, are all directions except that of $(0,1)^{\mathsf T}$, which is their limit as $x\to\pm\infty$; hence

$$
\sup_{x\in\mathbb{R}}\frac{(\hat Y_x-\mu_x)^2}{\sigma^2(\hat Y_x)}=\frac{\boldsymbol{\theta}^{\mathsf T}M\boldsymbol{\theta}}{\sigma^2}\sim\chi^2_2.
$$
This variable is independent of $\mathrm{SSE}/\sigma^2\sim\chi^2_{n-2}$ ([3.3.3](/3.3.3)), so $\sup_x(\hat Y_x-\mu_x)^2/s^2(\hat Y_x)=\boldsymbol{\theta}^{\mathsf T}M\boldsymbol{\theta}/\mathrm{MSE}\sim2F_{2,n-2}$, and the band covers the whole line if and only if this supremum is at most $W^2$. $\square$

Since a simultaneous statement is stronger, $W>t_{n-2,\alpha/2}$: the band is wider than the individual confidence intervals. It uses the same $F_{2,n-2,\alpha}$ as the elliptical confidence region for $(\beta_0,\beta_1)$ in [3.3.3](/3.3.3); indeed, the band is the set of all lines whose coefficients lie in that ellipse.

**Example 4.3.1** For the Toluca data, $t_{23,0.025}=2.069$ is used for an individual $95\%$ interval and $W=\sqrt{2F_{2,23,0.05}}=2.616$ for the $95\%$ confidence band. At $X_h=100$ the band is

$$
419.39\pm2.616\times14.27=(382.05,\ 456.72),
$$
wider than the individual interval $(389.86,\ 448.91)$. To obtain the band with `predict`, which only knows $t$-intervals, find the level $1-\alpha'$ with $t_{n-2,\alpha'/2}=W$:

```r
W <- sqrt(2 * qf(0.95, df1 = 2, df2 = n - 2))   # 2.6162
adjalpha <- 2 * (1 - pt(W, df = n - 2))         # 0.0154
predict(reg, newdata = data.frame(lotsize = 100),
        interval = "confidence", level = 1 - adjalpha)
```

| $n$ | $\alpha$ | df | $t_{23,0.025}$ (individual interval) | $W$ (band) | adjusted $\alpha'$ |
|---|---|---|---|---|---|
| $25$ | $0.05$ | $(2,23)$ | $2.0687$ | $2.6162$ | $0.0154$ |

so the band at each point is an individual interval of level $98.46\%$.

![The Toluca data with the fitted line, the 95 percent pointwise confidence intervals for the mean response, the wider 95 percent Working-Hotelling confidence band, and the much wider 95 percent prediction intervals; all are narrowest at the mean lot size 70](./plots/toluca-intervals.py)

A confidence band is useful to

- evaluate the reliability of the model: it shows the range of uncertainty of the fitted line, a narrow band meaning high precision and a wide band high uncertainty;
- make several interval estimates of mean responses at once, with a guaranteed simultaneous level, for instance for risk assessment and decisions;
- assess the fit: if the regression function is seriously misspecified, a smooth curve through the data (such as `lowess`) leaves the band; the individual observations, in contrast, are not expected to lie inside it, since the band is for the mean, and their spread is described by the prediction intervals.

The four kinds of statements met so far are:

| Question | Interval | Standard error |
|---|---|---|
| the mean response $\mathbb{E}(Y_h)$ at one level $X_h$ | confidence interval, $t_{n-2,\alpha/2}$ | $s(\hat Y_h)$ |
| a new observation $Y_{h(\mathrm{new})}$ at $X_h$ | prediction interval, $t_{n-2,\alpha/2}$ | $s(\mathrm{pred})$ |
| the mean of $m$ new observations at $X_h$ | prediction interval, $t_{n-2,\alpha/2}$ | $s(\mathrm{predmean})$ |
| the regression line at several or all levels | confidence band, $W=\sqrt{2F_{2,n-2,\alpha}}$ | $s(\hat Y_x)$ |

For example, "how much does a household with disposable income $23\,500$ dollars spend on dining out, on average?" asks for a confidence interval for a mean response; "what will the temperature in this room be tomorrow, with the thermostat set to $31\,^\circ\mathrm{C}$?" asks for a prediction interval; questions about the mean response over a whole range of conditions at once call for the band.

## 4.4. Analysis of Variance

### 4.4.1. Partitioning the Total Sum of Squares

The total variation of the responses is measured by the total sum of squares; it is $0$ if all observations are equal and positive otherwise. The analysis of variance partitions it, quantifying and classifying the variation by its sources. Each deviation from the mean splits into two parts:

$$
Y_i-\bar Y=(Y_i-\hat Y_i)+(\hat Y_i-\bar Y),
$$
the deviation of the observation around the fitted line and the deviation of the fitted value around the mean.

![The partition of a deviation for two lots of the Toluca data: (a) total deviations Y_i - Y_bar from the mean, (b) deviations Y_i - Y_hat_i around the fitted line, (c) deviations Y_hat_i - Y_bar of the fitted values from the mean](./plots/anova-decomposition.py)

**Definition 4.4.1** The **total sum of squares** and the **regression sum of squares** are

$$
\mathrm{SSTO}=\sum_{i=1}^n(Y_i-\bar Y)^2,\qquad\mathrm{SSR}=\sum_{i=1}^n(\hat Y_i-\bar Y)^2;
$$
together with $\mathrm{SSE}=\sum_i(Y_i-\hat Y_i)^2$ of [3.3.2](/3.3.2), SSR is the variation due to the model (explained by the regression line) and SSE the variation due to the error terms.

**Theorem 4.4.1** $\mathrm{SSTO}=\mathrm{SSR}+\mathrm{SSE}$, and $\mathrm{SSR}=b_1^2\sum_i(X_i-\bar X)^2$.

**Proof** Squaring and summing the partition of $Y_i-\bar Y$,

$$
\sum_i(Y_i-\bar Y)^2=\sum_i(Y_i-\hat Y_i)^2+2\sum_i(Y_i-\hat Y_i)(\hat Y_i-\bar Y)+\sum_i(\hat Y_i-\bar Y)^2,
$$
and the cross term is $\sum_ie_i(b_0+b_1X_i)-\bar Y\sum_ie_i=0$ because $\sum_ie_i=\sum_iX_ie_i=0$ ([3.3.2](/3.3.2)). Since $\hat Y_i-\bar Y=b_1(X_i-\bar X)$, $\mathrm{SSR}=b_1^2S_{XX}$. $\square$

The total sum of squares is often written SST, as in some software output.

### 4.4.2. Degrees of Freedom and Mean Squares

The degrees of freedom split in the same way, $n-1=1+(n-2)$:

- $\mathrm{SSTO}$ has $\mathrm{df}_{\mathrm{T}}=n-1$: the $n$ deviations $Y_i-\bar Y$ sum to $0$;
- $\mathrm{SSR}$ has $\mathrm{df}_{\mathrm{R}}=1$, because $\mathrm{SSR}=b_1^2S_{XX}$ depends on the data through the single quantity $b_1$;
- $\mathrm{SSE}$ has $\mathrm{df}_{\mathrm{E}}=n-2$, adjusting for the estimated intercept and slope.

**Definition 4.4.2** A **mean square** is a sum of squares divided by its degrees of freedom. The regression mean square and the error mean square are

$$
\mathrm{MSR}=\frac{\mathrm{SSR}}{\mathrm{df}_{\mathrm{R}}}=\mathrm{SSR},\qquad\mathrm{MSE}=\frac{\mathrm{SSE}}{\mathrm{df}_{\mathrm{E}}}=\frac{\mathrm{SSE}}{n-2}.
$$

$\mathrm{MSE}=s^2$ is the estimator of $\sigma^2=\operatorname{Var}(Y\mid X)=\operatorname{Var}(\varepsilon)$ obtained in [3.3.2](/3.3.2), whereas $\mathrm{SSTO}/(n-1)$ is the sample variance of the $Y_i$, which ignores $X$. Because $\hat Y_i=b_0+b_1X_i$ estimates $\mathbb{E}(Y_i)$ better than $\bar Y$ does, we expect SSE to be smaller than SSTO, and by Theorem 4.4.1 it is: $\mathrm{SSE}=\mathrm{SSTO}-\mathrm{SSR}\le\mathrm{SSTO}$.

### 4.4.3. Expected Mean Squares

Before the observations are obtained, MSR and MSE are random variables.

**Theorem 4.4.2** Under the simple linear regression model,

$$
\mathbb{E}(\mathrm{MSE})=\sigma^2,\qquad\mathbb{E}(\mathrm{MSR})=\sigma^2+\beta_1^2\sum_{i=1}^n(X_i-\bar X)^2.
$$

**Proof** The first is Theorem 2.2.2 of [3.3.2](/3.3.2). For the second, $\mathbb{E}(\mathrm{MSR})=S_{XX}\,\mathbb{E}(b_1^2)=S_{XX}\big[\operatorname{Var}(b_1)+\beta_1^2\big]=S_{XX}\big(\sigma^2/S_{XX}+\beta_1^2\big)$. $\square$

When $H_0\colon\beta_1=0$ is true, $\mathbb{E}(\mathrm{MSR})=\mathbb{E}(\mathrm{MSE})=\sigma^2$, and both are unbiased estimators of $\sigma^2$. When $H_1\colon\beta_1\ne0$ holds, $\mathbb{E}(\mathrm{MSR})>\mathbb{E}(\mathrm{MSE})$, and MSR tends to be larger than MSE. Comparing the two mean squares therefore tests $\beta_1=0$.

### 4.4.4. The F-Test

The test statistic is

$$
F^*=\frac{\mathrm{MSR}}{\mathrm{MSE}}.
$$
Under the normal error model and $H_0\colon\beta_1=0$, $\mathrm{SSR}/\sigma^2=\big(b_1/\sigma(b_1)\big)^2\sim\chi^2_1$ is independent of $\mathrm{SSE}/\sigma^2\sim\chi^2_{n-2}$ ([3.3.3](/3.3.3)), so

$$
F^*=\frac{\chi^2_{\mathrm{df}_{\mathrm{R}}}/\mathrm{df}_{\mathrm{R}}}{\chi^2_{\mathrm{df}_{\mathrm{E}}}/\mathrm{df}_{\mathrm{E}}}\sim F_{\mathrm{df}_{\mathrm{R}},\mathrm{df}_{\mathrm{E}}}=F_{1,n-2}.
$$
Large values of $F^*$ support $H_1$, so the level-$\alpha$ test rejects $H_0$ if $F^*>F_{1,n-2,\alpha}$; equivalently, by the $p$-value approach, if $\mathbb{P}(F>F^*)<\alpha$ for $F\sim F_{1,n-2}$.

**Remark 4.4.1** Two facts connect the $F$-test with what we already know.

1. Under $H_1\colon\beta_1\ne0$, $F^*$ follows a noncentral $F$-distribution with $(1,n-2)$ degrees of freedom and noncentrality parameter $\beta_1^2S_{XX}/\sigma^2$, and $\operatorname{Power}(\beta_1)=\mathbb{P}(F^*>F_{1,n-2,\alpha})$ can be computed from it, as in [3.3.3](/3.3.3).
2. The **t-test** of [3.3.3](/3.3.3) uses $T=b_1/s(b_1)$, and

$$
T^2=\frac{b_1^2}{\mathrm{MSE}/S_{XX}}=\frac{b_1^2S_{XX}}{\mathrm{MSE}}=\frac{\mathrm{MSR}}{\mathrm{MSE}}=F^*.
$$
Since also $F_{1,n-2,\alpha}=t_{n-2,\alpha/2}^2$, the two-sided $t$-test and the $F$-test are equivalent and give the same $p$-value in simple linear regression. The key is $\mathrm{df}_{\mathrm{R}}=1$; with several predictors the $F$-test tests several coefficients at once and has no $t$ counterpart.

### 4.4.5. The ANOVA Table

The computations are arranged in the *ANOVA table*:

| Source | df | SS | MS | $F$ value | $\mathbb{P}(>F)$ |
|---|---|---|---|---|---|
| Regression | $1$ | $\mathrm{SSR}=\sum_i(\hat Y_i-\bar Y)^2$ | $\mathrm{MSR}=\mathrm{SSR}/1$ | $\mathrm{MSR}/\mathrm{MSE}$ | $p$-value |
| Error | $n-2$ | $\mathrm{SSE}=\sum_i(Y_i-\hat Y_i)^2$ | $\mathrm{MSE}=\mathrm{SSE}/(n-2)$ | | |
| Total | $n-1$ | $\mathrm{SSTO}=\sum_i(Y_i-\bar Y)^2$ | | | |

In R, `anova(lm(...))` prints the first two rows, the error row being labeled `Residuals`.

**Example 4.4.1** For the Pisa data ($n=13$), `anova(lm(lean ~ year, data = pisa))` gives

| | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
|---|---|---|---|---|---|
| year | $1$ | $15804.5$ | $15804.5$ | $904.12$ | $6.5\times10^{-12}$ |
| Residuals | $11$ | $192.3$ | $17.5$ | | |

Here $F^*=15804.5/17.48=904.1=30.069^2=T^2$, and $\sqrt{17.48}=4.181$ is the residual standard error of `summary`. For the Toluca data ($n=25$), the table has $\mathrm{SSR}=252378$ on $1$ degree of freedom and $\mathrm{SSE}=54825$ on $23$ degrees of freedom, so $\mathrm{MSE}=2384$, $F^*=105.88=10.290^2$, and $p=4.45\times10^{-10}$, in agreement with the $t$-test.

## 4.5. The General Linear Test

The analysis of variance can be viewed in a different way that generalizes. The test of $H_0\colon\beta_1=0$ against $H_1\colon\beta_1\ne0$ compares two models:

$$
Y_i=\beta_0+\beta_1X_i+\varepsilon_i\quad\text{(full model)},\qquad Y_i=\beta_0+\varepsilon_i\quad\text{(reduced model, }H_0\text{ true)}.
$$
The principle of the extra sum of squares is to compare the two models through their error sums of squares: the reduced model can never fit better, and the increase of the error sum of squares when we pass from the full to the reduced model measures how much the excluded terms contribute.

**Definition 4.5.1** Let a **full model** and a **reduced model** be given, the reduced model being the special case of the full model specified by $H_0$, and let $\mathrm{SSE}(F)$ with $\mathrm{df}(F)$ degrees of freedom and $\mathrm{SSE}(R)$ with $\mathrm{df}(R)$ degrees of freedom be their error sums of squares. The **general linear test** of $H_0$ uses the statistic

$$
F^*=\frac{\big[\mathrm{SSE}(R)-\mathrm{SSE}(F)\big]/\big(\mathrm{df}(R)-\mathrm{df}(F)\big)}{\mathrm{SSE}(F)/\mathrm{df}(F)}
$$
and rejects $H_0$ for large values of $F^*$.

Under the normal error model, if $H_0$ holds (there is no difference between the models), $F^*\sim F_{\mathrm{df}(R)-\mathrm{df}(F),\,\mathrm{df}(F)}$; both the critical value and the $p$-value approaches can be used. The distribution theory is proved for the general case with the matrix approach in [3.3.9](/3.3.9).

For simple linear regression, the full model has $\mathrm{SSE}(F)=\mathrm{SSE}$ with $\mathrm{df}(F)=n-2$. In the reduced model the least squares estimate of $\beta_0$ is $\bar Y$, so $\mathrm{SSE}(R)=\sum_i(Y_i-\bar Y)^2=\mathrm{SSTO}$ with $\mathrm{df}(R)=n-1$. Hence

$$
F^*=\frac{(\mathrm{SSTO}-\mathrm{SSE})/\big((n-1)-(n-2)\big)}{\mathrm{SSE}/(n-2)}=\frac{\mathrm{SSR}}{\mathrm{MSE}}=\frac{\mathrm{MSR}}{\mathrm{MSE}},
$$
exactly the ANOVA $F$-test. Here the general linear test brings nothing new, but it applies to any pair of nested linear models and is the standard way of testing groups of coefficients in multiple regression.

## 4.6. Correlation and the Coefficient of Determination

The usual (Pearson) sample **correlation coefficient**

$$
r=\frac{\sum_i(X_i-\bar X)(Y_i-\bar Y)}{\sqrt{\sum_i(X_i-\bar X)^2\sum_i(Y_i-\bar Y)^2}}=\frac{S_{XY}}{\sqrt{S_{XX}\,\mathrm{SSTO}}}
$$
is a number between $-1$ and $1$ that measures the strength of the linear relationship between two variables. The analysis of variance gives a second measure.

**Definition 4.6.1** The **coefficient of determination** is the proportion of the total variation that is explained by the model (by the predictor variable):

$$
R^2=\frac{\mathrm{SSR}}{\mathrm{SSTO}}=1-\frac{\mathrm{SSE}}{\mathrm{SSTO}}.
$$

By Theorem 4.4.1, $0\le R^2\le1$; $R^2=1$ if all points lie on the fitted line, and $R^2=0$ if $b_1=0$.

**Proposition 4.6.1** In simple linear regression, $R^2=r^2$, and $b_1=r\sqrt{\mathrm{SSTO}/S_{XX}}$.

**Proof** $b_1=S_{XY}/S_{XX}=r\sqrt{S_{XX}\mathrm{SSTO}}/S_{XX}=r\sqrt{\mathrm{SSTO}/S_{XX}}$, hence $\mathrm{SSR}=b_1^2S_{XX}=r^2\,\mathrm{SSTO}$. $\square$

So $r=\pm\sqrt{R^2}$, with the sign of $b_1$. For the Pisa data, $R^2=15804.5/(15804.5+192.3)=0.988$ and $r=0.994$; for the Toluca data, $R^2=252378/(252378+54825)=0.8215$ and $r=0.906$. R reports $R^2$ as `Multiple R-squared`; the adjusted $R^2$ printed next to it penalizes the number of predictors and is discussed with multiple regression ([3.3.8](/3.3.8)).

Both $R^2$ and $r$ measure linear association only, and they are easily misread.

- They can be $0$ even if there is a perfect nonlinear relationship (points on a parabola symmetric about $\bar X$).
- A high $R^2$ does not mean that the linear model is appropriate (a curved relationship can have a high $R^2$) or that predictions are precise enough: prediction intervals depend on $\mathrm{MSE}$, not on $R^2$.
- A low $R^2$ with a significant slope means that $X$ explains little of the variability of $Y$, however small the $p$-value; conversely, a regression line through a cloud with $R^2$ near $0$ describes almost nothing, whatever pattern the eye may want to see in it.
- $R^2$ depends on the spread of the $X_i$ in the sample: the same model gives a larger $R^2$ when the $X_i$ are more spread out.

Finally, we prove the formula for the test of zero correlation used in [3.3.3](/3.3.3).

**Theorem 4.6.1** Let $(X_i,Y_i)$, $i=1,\dots,n$, be a random sample from a bivariate normal distribution with correlation $\rho$. Under $H_0\colon\rho=0$,

$$
t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}\sim t_{n-2}.
$$

**Proof** Conditionally on $X_1,\dots,X_n$ the normal error regression model holds with $\beta_1=\rho\sigma_Y/\sigma_X$, so $H_0\colon\rho=0$ is $H_0\colon\beta_1=0$, under which $T=b_1/s(b_1)\sim t_{n-2}$. Now

$$
T=\frac{b_1\sqrt{S_{XX}}}{\sqrt{\mathrm{SSE}/(n-2)}}=\frac{b_1\sqrt{S_{XX}}\sqrt{n-2}}{\sqrt{\mathrm{SSTO}-\mathrm{SSR}}}=\frac{r\sqrt{\mathrm{SSTO}}\sqrt{n-2}}{\sqrt{\mathrm{SSTO}(1-r^2)}}=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}},
$$
using $b_1\sqrt{S_{XX}}=r\sqrt{\mathrm{SSTO}}$ and $\mathrm{SSR}=r^2\mathrm{SSTO}$ (Proposition 4.6.1). The conditional distribution $t_{n-2}$ does not depend on the $X_i$, so it is also the unconditional distribution. $\square$

For $H_0\colon\beta_1=0$ in simple linear regression we now have four equivalent tests, all giving the same $p$-value:

1. the individual parameter $t$-test, $T=b_1/s(b_1)$;
2. the $t$-test of the population correlation coefficient, $H_0\colon\rho=0$ (for bivariate normal data);
3. the overall ANOVA $F$-test, $F^*=\mathrm{MSR}/\mathrm{MSE}=T^2$;
4. the general linear test, which here coincides with the ANOVA $F$-test; with several predictors it becomes the partial $F$-test of [3.3.9](/3.3.9).

## Summary

- Mean response at $X_h$: $\hat Y_h=b_0+b_1X_h$, $s^2(\hat Y_h)=\mathrm{MSE}\,[1/n+(X_h-\bar X)^2/S_{XX}]$, confidence interval $\hat Y_h\pm t_{n-2,\alpha/2}s(\hat Y_h)$; most precise at $\bar X$.
- New observation at $X_h$: prediction interval $\hat Y_h\pm t_{n-2,\alpha/2}s(\mathrm{pred})$ with $s^2(\mathrm{pred})=\mathrm{MSE}+s^2(\hat Y_h)$; it does not shrink to a point as $n\to\infty$ and relies on normal errors. For the mean of $m$ new observations, $1$ is replaced by $1/m$.
- Whole line: the Working–Hotelling band $\hat Y_x\pm W s(\hat Y_x)$ with $W^2=2F_{2,n-2,\alpha}$ has exact simultaneous level $1-\alpha$ and is wider than the pointwise intervals.
- ANOVA: $\mathrm{SSTO}=\mathrm{SSR}+\mathrm{SSE}$ with $n-1=1+(n-2)$ degrees of freedom; $\mathbb{E}(\mathrm{MSE})=\sigma^2$, $\mathbb{E}(\mathrm{MSR})=\sigma^2+\beta_1^2S_{XX}$; $F^*=\mathrm{MSR}/\mathrm{MSE}\sim F_{1,n-2}$ under $H_0\colon\beta_1=0$, and $F^*=T^2$.
- General linear test: compare $\mathrm{SSE}(R)$ and $\mathrm{SSE}(F)$ of a reduced and a full model; in simple regression it is the ANOVA $F$-test.
- $R^2=\mathrm{SSR}/\mathrm{SSTO}=r^2$ measures the proportion of variation explained by the linear fit, and only that.
