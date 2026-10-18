---
title: Model Assumptions and Diagnostics
description: The LINE assumptions of the simple linear normal error regression model and how to check them, by examining the predictor (location, spread, skewness, kurtosis, box plots, histograms, Q–Q plots) and the residuals (linearity, constant variance, normality, independence, outliers), with graphical methods and formal tests.
---

A typical regression analysis has four steps: formulating a model, estimating it, evaluating it and using it. The inference of [3.3.3](/3.3.3) and [3.3.4](/3.3.4) (the $t$- and $F$-tests, confidence and prediction intervals) belongs to the last step, and every one of its $p$-values and coverage probabilities is computed under the model assumptions. This chapter is about the third step: which assumptions the **simple linear regression model** makes, what can go wrong, and how to detect it, both with graphs and with formal tests. We first look at the predictor $X$, whose "distribution" or design matters although the model assumes nothing about it, and then at the **residuals**, which stand in for the unobservable errors. The remedies for the problems found here are the subject of [3.3.6](/3.3.6); the matrix form of the same tools and their multiple regression versions follow in [3.3.7](/3.3.7) and [3.3.11](/3.3.11).

## 5.1. The Model and Its Assumptions

### 5.1.1. The Simple Linear Normal Error Regression Model

We observe $n$ cases $(X_i, Y_i)$, where $Y_i$ is the $i$-th response (outcome) and $X_i$ the $i$-th explanatory (predictor) variable, and assume

$$
Y_i = \beta_0 + \beta_1 X_i + \varepsilon_i, \qquad i = 1, \dots, n,
$$
where $\beta_0$ is the intercept, $\beta_1$ the slope, and the random errors $\varepsilon_1, \dots, \varepsilon_n$ are independent and normally distributed with $\mathbb{E}(\varepsilon_i) = 0$ and constant variance $\operatorname{Var}(\varepsilon_i) = \sigma^2$ ([3.3.2](/3.3.2)). For each $X_i$, the response therefore has the normal distribution $\mathcal{N}(\beta_0 + \beta_1 X_i, \sigma^2)$ centered on the regression line.

With the **least squares** estimates $b_0$ (intercept) and $b_1$ (slope), the **fitted values** and **residuals** are

$$
\hat Y_i = b_0 + b_1 X_i, \qquad e_i = Y_i - \hat Y_i = Y_i - (b_0 + b_1 X_i).
$$

### 5.1.2. The LINE Assumptions

The model consists of four assumptions, remembered by the acronym LINE:

| Assumption | Statement | Name |
|---|---|---|
| L | the mean of $Y_i$ is a linear function of $X_i$: $\mathbb{E}(Y_i) = \beta_0 + \beta_1 X_i$ | linearity |
| I | $\varepsilon_1, \dots, \varepsilon_n$ are independent | independence |
| N | $\varepsilon_1, \dots, \varepsilon_n \sim \mathcal{N}(0, \sigma^2)$ | normality |
| E | $\operatorname{Var}(Y_i) = \sigma^2$ does not depend on $X_i$ | equal (constant) variance |

The three probabilistic assumptions (I, N, E) are statements about the errors, equivalently about the conditional distribution of $Y$ given $X$. It is therefore not appropriate to check them on the observed $Y_1, \dots, Y_n$ as one sample: the $Y_i$ have different means $\beta_0 + \beta_1 X_i$, so their histogram mixes normal distributions with different centers and need not look normal even when the model is correct. The assumptions are checked on the residuals, which have mean zero and approximate the errors.

### 5.1.3. Diagnostics and Remedial Measures

**Definition 5.1.1 (Regression Diagnostics)** **Regression diagnostics** are graphical tools and formal procedures that check whether the assumptions of a regression model are violated. **Remedial measures** are the methods used when they are: transformations and other adjustments that fix the problem, or different models and analytic strategies that accommodate the violation.

If the assumptions are violated, the inference cannot be trusted: the $t$- and $F$-tests and their $p$-values are not correct, and confidence intervals do not have the nominal coverage. Diagnostics should therefore precede inference, and their results decide which remedy, if any, is needed ([3.3.6](/3.3.6)).

## 5.2. Diagnostics for the Predictor

### 5.2.1. Why Look at the Predictor

Before describing the relationship between a response $Y$ and a predictor $X$, we look at the distributions of the variables. The predictor should always be examined. The response alone is much less informative: if $Y$ depends on $X$, its marginal distribution mixes the conditional distributions at different $X$ values, and looking only at the marginal distribution of $Y$ is a common mistake.

No distributional assumption is imposed on $X$; it may follow any distribution, or simply be regarded as fixed (not random). Still, the "distribution" of the $X_i$, that is, the design, is important:

- The spread of the $X_i$ determines the precision of the slope, $\operatorname{Var}(b_1) = \sigma^2 / \sum_{i}(X_i - \bar X)^2$ ([3.3.3](/3.3.3)). A good design gives more power in inference and ensures the validity of the whole analysis; a bad design does the opposite.
- Skewness of the $X_i$ and extreme values among them can inflate the variance of the estimates or dominate the fitted trend (the leverage of [3.3.6](/3.3.6)).

If $X$ takes many values, numerical summaries (mean, median, quartiles; R `summary`) describe it; if it takes only a few values, a frequency table (R `table`) is enough.

A *sequence plot* plots the observations against the order in which they were collected. A trend in such a plot is a warning about independence and suggests that time, or another ordering variable, may act as a confounding factor that alters the relation between $X$ and $Y$. A classic example: ice cream sales and shark attacks rise and fall together over the months of a year, because both are driven by the temperature, not because one causes the other. Likewise one should ask whether important predictors have been left out of the model; confounding is treated systematically in causal inference ([3.9](/3.9)).

```r
plot(lotsize)                         # sequence plot of the predictor
lines(lowess(lotsize), col = "red")   # smoothed trend over the order of collection
```

### 5.2.2. Location, Spread, Skewness and Kurtosis

Four kinds of numerical summaries describe a distribution:

| Statistic | Measures |
|---|---|
| mean | location |
| standard deviation; range $X_{(n)} - X_{(1)}$ | variability, spread |
| skewness | lack of symmetry |
| kurtosis | heavy or light tails relative to a normal distribution |

With the sample central moments $m_k = \frac1n\sum_{i=1}^n (X_i - \bar X)^k$, the **sample skewness** and **sample kurtosis** ([3.2.1](/3.2.1)) are

$$
g_1 = \frac{m_3}{m_2^{3/2}} = \frac{\frac1n\sum_{i=1}^n(X_i - \bar X)^3}{\Big(\frac1n\sum_{i=1}^n(X_i - \bar X)^2\Big)^{3/2}}, \qquad g_2 = \frac{m_4}{m_2^2} - 3 = \frac{\frac1n\sum_{i=1}^n(X_i - \bar X)^4}{\Big(\frac1n\sum_{i=1}^n(X_i - \bar X)^2\Big)^2} - 3,
$$
the sample versions of the **skewness** and **kurtosis** of [3.1.8](/3.1.8).

Skewness. If $g_1 < 0$ the distribution is skewed to the left: the left tail is long relative to the right tail (for example, the age at death). If $g_1 > 0$ it is skewed to the right (for example, the scores on a difficult exam, or incomes). The sign gives the direction of the skewness, which can be present to varying degrees; the magnitude compares the sample with a symmetric (normal) distribution, and values far from zero suggest a non-normal, skewed population. In the normal and other symmetric distributions the mean, the median and the mode coincide; generally (though not always) a right-skewed distribution has mode < median < mean and a left-skewed one the reverse order. If the data are multimodal, the modes can affect the sign of the skewness, and a single number no longer describes the shape well.

Kurtosis. $g_2$ measures how far the rare observations scatter from the mean, and $g_2 = 0$ for a normal distribution. It is sometimes called the excess kurtosis, the term kurtosis being reserved for $G_2 = m_4 / m_2^2 = g_2 + 3$; when software reports a sample kurtosis, one must check which convention it follows.

**Definition 5.2.1 (Leptokurtic and Platykurtic Distributions)** A distribution with kurtosis greater than $0$ (heavier tails than the normal) is called a **leptokurtic distribution** ("lepto-" means slender); a distribution with kurtosis less than $0$ (lighter tails) is called a **platykurtic distribution** ("platy-" means broad). Distributions with kurtosis $0$ are called mesokurtic.

Three misconceptions about kurtosis are common. First, kurtosis is not only peakedness: tailedness and peakedness are both components of it, and the tails dominate. Second, positive kurtosis goes with a sharper peak and heavy tails, negative kurtosis with a flatter top and light tails. Third, kurtosis is not the variance: it is computed from standardized data and is scale-free, so it describes the shape of a distribution apart from its variance; a leptokurtic distribution can have a smaller or a larger variance than a platykurtic one.

| Distribution (standardized) | Kurtosis |
|---|---|
| Laplace (double exponential) | $3$ |
| hyperbolic secant | $2$ |
| logistic | $1.2$ |
| normal | $0$ |
| raised cosine | $-0.594$ |
| Wigner semicircle | $-1$ |
| uniform | $-1.2$ |

Leptokurtic ("super-Gaussian") distributions include Student's $t$, the Laplace, exponential, Poisson and logistic distributions; platykurtic ("sub-Gaussian") ones include the continuous and discrete uniform distributions and the raised cosine. The most platykurtic distribution of all is $\mathrm{Ber}(1/2)$, a fair coin toss, with kurtosis $-2$; no distribution has smaller kurtosis, since $\mathbb{E}Z^4 \ge (\mathbb{E}Z^2)^2 = 1$ for a standardized $Z$. In finance, kurtosis risk refers to this: for two assets with the same mean and variance of returns, the one with the leptokurtic return distribution has a higher chance of extreme gains and losses.

In short, skewness distinguishes extreme values in one tail from those in the other, while kurtosis measures extreme values in either tail: leptokurtic data have tails more extreme than the normal distribution, platykurtic data a lower likelihood of extreme events.

Why compare with the normal distribution at all? The regression model does not assume that $X$ comes from a normal distribution (it may have any distribution, or be fixed), nor that $Y$ comes from a single normal distribution; it assumes that $Y$ given $X_i$ is normal. In some cases, however, $X$ or $Y$ may themselves be normal, and it can be useful to know this.

**Example 5.2.1 (Toluca Lot Sizes)** In the Toluca Company data, $n = 25$ production runs record the lot size $X$ and the work hours $Y$. For the lot sizes,

| Min | $Q_1$ | Median | Mean | $Q_3$ | Max |
|---|---|---|---|---|---|
| $20$ | $50$ | $70$ | $70$ | $90$ | $120$ |

with standard deviation $28.72$ (variance $825$, $\sum(X_i - \bar X)^2 = 19800$), mode $90$, range $100$ and interquartile range $\mathrm{IQR} = Q_3 - Q_1 = 40$; the quartiles divide the ordered data into four equal parts. The sample skewness is $g_1 = -0.097$ and the sample kurtosis $g_2 = -1.106$. The lot sizes are nearly symmetric with light tails, as one expects from a planned design whose values are multiples of $10$ spread evenly between $20$ and $120$.

### 5.2.3. Graphical Summaries

Stem-and-leaf plots (R `stem`) list the data compactly by leading digits; they show the shape of the distribution while keeping the individual values.

The **boxplot** ([3.4.1](/3.4.1)) shows the median, the quartiles and the whiskers, which extend to the most extreme observations within $1.5\,\mathrm{IQR}$ of the box; points beyond them are plotted individually as potential outliers (R `boxplot`; `range = 0` extends the whiskers to the extremes). The spacings between the parts of the box indicate the spread and the skewness. For a normal distribution, $Q_1$ and $Q_3$ are $\mu \mp 0.6745\sigma$, the whisker limits $Q_1 - 1.5\,\mathrm{IQR}$ and $Q_3 + 1.5\,\mathrm{IQR}$ are $\mu \mp 2.698\sigma$, and only $0.7\%$ of the observations fall outside them. A boxplot cannot show everything: very different distributions, for example a unimodal and a bimodal one with the same quartiles, can have identical boxplots.

Histograms (R `hist`) show the shape of the density, including multimodality; with `freq = FALSE` they are on the density scale and can be overlaid with a smooth density estimate (R `density`). Their appearance depends on the choice of bins.

Quantile–quantile (Q–Q) plots compare two distributions through their quantiles. Let $F$ and $G$ be two distribution functions and

$$
F^{-1}(q) = \inf\{y \colon F(y) \ge q\}, \qquad 0 < q < 1,
$$
the corresponding **quantile** functions. The Q–Q plot plots $F^{-1}(q)$ against $G^{-1}(q)$ for $0 < q < 1$: each point pairs the two values below which the same fraction $q$ (say $10\%$, $50\%$, $80\%$) of the respective distributions lies. If $F$ and $G$ differ only in location and scale, the points lie on a straight line.

The **normal Q–Q plot** (normal probability plot) compares a sample with the normal distribution. For a sample $X_1, \dots, X_n$ with **order statistics** $X_{(1)} \le X_{(2)} \le \cdots \le X_{(n)}$, the $i$-th order statistic is the realized quantile of order about $i/n$; the corresponding normal scores are

$$
Z_i = \Phi^{-1}(p_i), \qquad p_i = \frac{i - 0.5}{n}, \qquad i = 1, \dots, n,
$$
and the plot shows $X_{(i)}$ against $Z_i$. If the sample comes from a normal distribution, the points roughly follow the straight line

$$
X_{(i)} = \mu + \sigma Z_i,
$$
and departures from a line indicate departures from normality. Some texts plot $X_{(i)}$ against $sZ_i$ instead, or use slightly different $p_i$; this does not alter the nature of the plot. The shape of the departure also reveals the shape of the underlying distribution:

| Pattern of the points | Distribution |
|---|---|
| close to the line | normal |
| S-shaped: flat in the middle, ends bending towards the horizontal | light tails (platykurtic) |
| inverted S: lower end below, upper end above the line | heavy tails (leptokurtic) |
| convex curve, above the line at both ends | right skew |
| concave curve, below the line at both ends | left skew |
| two clusters with a jump between them | bimodal |

![Normal Q-Q plots of samples of size 60 from a normal, a uniform (light-tailed), a t distribution with 2 degrees of freedom (heavy-tailed), an exponential (right-skewed), a negative exponential (left-skewed) and a bimodal normal mixture distribution; the reference line passes through the quartiles](./plots/qq-patterns.py)

For the Toluca lot sizes the stem-and-leaf plot, the boxplot (box from $50$ to $90$, whiskers to $20$ and $120$, no outliers), the histogram and the normal Q–Q plot all agree with the numerical summaries: symmetric, flat, without extreme values.

```r
summary(lotsize)                     # five-number summary and mean
stem(lotsize)                        # stem-and-leaf plot
boxplot(lotsize)
hist(lotsize, freq = FALSE)          # histogram on the density scale
lines(density(lotsize), col = "red") # kernel density estimate
qqnorm(lotsize)                      # normal Q-Q plot
qqline(lotsize, col = "red")         # line through the quartiles
```

## 5.3. Diagnostics Using Residuals

Recall that the residuals $e_i = Y_i - \hat Y_i = Y_i - (b_0 + b_1 X_i)$ show how well the model fits and approximate the error terms $\varepsilon_i$. They can be used for several diagnostic purposes:

- Is the linear model appropriate?
- Is the error variance constant?
- Are the errors normal?
- Are the errors independent?
- Are there outliers?

**Definition 5.3.1 (Residual Plot)** A **residual plot** is a plot of the residuals $e_i$ against the predictor $X_i$, against the fitted values $\hat Y_i$, or against another variable such as the time order of the observations.

If the model is adequate, the residual plot shows a horizontal band of points around zero without any systematic pattern. The typical patterns of the four kinds of violation are shown below and discussed in the following subsections.

![Four residual plots: (a) a horizontal band without pattern, (b) a U-shaped curve when a quadratic relation is fitted by a straight line, (c) a funnel when the error standard deviation grows with X, (d) long runs of positive and negative residuals in time order when the errors are autocorrelated](./plots/residual-patterns.py)

### 5.3.1. Is the Relationship Linear?

There are two plots for this question: $Y_i$ against $X_i$ (the scatter plot), and $e_i$ against $X_i$ or $\hat Y_i$ (the residual plot). The residual plot emphasizes the deviations from the linear pattern better, because the linear trend that dominates the scatter plot has been removed.

**Example 5.3.1 (A Quadratic Relation)** We generate data from $Y = X^2 - 10X + 30 + \varepsilon$ with normal errors, $\sigma = 25$, and fit a straight line.

```r
x <- seq(1, 30, by = 1)
n <- length(x)
y <- x^2 - 10 * x + 30 + 25 * rnorm(n)
a100 <- data.frame(x, y)
fit1 <- lm(y ~ x, data = a100)
anova(fit1)
summary(fit1)
```

One run gave the following output:

| Source | df | SS | MS | $F$ | $p$-value |
|---|---|---|---|---|---|
| x | $1$ | $1016230$ | $1016230$ | $182.52$ | $8.7 \times 10^{-14}$ |
| Residuals | $28$ | $155898$ | $5568$ | | |

| | Estimate | Std. error | $t$ value | $p$-value |
|---|---|---|---|---|
| (Intercept) | $-138.179$ | $27.942$ | $-4.945$ | $3.2 \times 10^{-5}$ |
| x | $21.264$ | $1.574$ | $13.510$ | $8.7 \times 10^{-14}$ |

Everything looks highly significant, and $R^2 = 1016230 / 1172128 = 0.867$ is large. Yet the scatter plot with the fitted line (`plot(y ~ x); abline(fit1)`) shows points above the line at both ends and below it in the middle, the smoothed curve (`scatter.smooth(x, y)`) is clearly a parabola, and the residual plot (`scatter.smooth(x, fit1$residuals); abline(h = 0)`) shows the U shape of panel (b) above. The significance of the slope and a large $R^2$ do not show that the relation is linear.

### 5.3.2. Is the Error Variance Constant?

Again we plot $Y_i$ against $X_i$, and $e_i$ against $X_i$ or $\hat Y_i$. The residual plot against $X_i$ emphasizes problems with the variance assumption: a funnel or megaphone shape means that the spread of the errors changes with $X$.

**Definition 5.3.2 (Homoscedasticity and Heteroscedasticity)** The errors of a regression model are homoscedastic if they all have the same variance, $\operatorname{Var}(\varepsilon_i) = \sigma^2$ for all $i$; this property is called **homoscedasticity**. Otherwise, if the variance depends on $i$ (typically on $X_i$), the errors are heteroscedastic, and the property is called **heteroscedasticity**.

**Example 5.3.2 (Variance Growing with $X$)** We generate data from $Y = 30 + 100X + 10X\varepsilon$, so that the error standard deviation $10X$ grows with $X$:

```r
x <- seq(1, 100, by = 1)
n <- length(x)
y <- 30 + 100 * x + 10 * x * rnorm(n)
a100a <- data.frame(x, y)
fit2 <- lm(y ~ x, data = a100a)
anova(fit2)
summary(fit2)
```

| Source | df | SS | MS | $F$ | $p$-value |
|---|---|---|---|---|---|
| x | $1$ | $845726258$ | $845726258$ | $2431.1$ | $< 2.2 \times 10^{-16}$ |
| Residuals | $98$ | $34091704$ | $347875$ | | |

| | Estimate | Std. error | $t$ value | $p$-value |
|---|---|---|---|---|
| (Intercept) | $71.299$ | $118.852$ | $0.60$ | $0.55$ |
| x | $100.746$ | $2.043$ | $49.31$ | $< 2 \times 10^{-16}$ |

The trend appears linear and the slope estimate is close to the truth, but the residual plot fans out as in panel (c) above. Why is the nonconstant variance a concern? Least squares remains unbiased, since unbiasedness uses only $\mathbb{E}(\varepsilon_i) = 0$; but the **Gauss–Markov theorem** ([3.2.3](/3.2.3)) requires a common variance, so least squares is no longer the minimum variance linear unbiased estimator. Estimation is not the most efficient, and the inference (tests, confidence intervals, prediction intervals) can be off, wrong or difficult to carry out, because the reported standard errors are computed as if the variance were constant.

The intercept estimate $71.3$ looks far from $\beta_0 = 30$ even though $b_0$ is unbiased. It is not surprising: the intercept is an extrapolation to $X = 0$, $b_0 = \bar Y - b_1 \bar X$ with $\bar X = 50.5$, so the large errors of the observations with large $X$ enter it through $b_1$, and its standard deviation is large (about $75$ in a simulation of this design; the reported $118.9$ is itself distorted by the heteroscedasticity). The deviation $41.3$ is well within one standard deviation. Weighted least squares ([3.3.6](/3.3.6)) gives far more precise estimates here.

Several formal tests of equal variances exist. The first three test whether $k$ samples come from populations with equal variances; in regression they are applied to groups of observations formed by the values of $X$ (for example, the cases with small and with large $X$).

- *Bartlett's test* is the **likelihood ratio test** for equal variances of normal populations, with an approximate $\chi^2$ distribution; it is sensitive to departures from normality.
- *Levene's test* computes the absolute deviations $Z_{ij} = \lvert Y_{ij} - \bar Y_i\rvert$ of the observations from their group means and compares the groups by a two-sample $t$-test or an **analysis of variance** of the $Z_{ij}$: a group with greater dispersion has larger absolute deviations from its center.
- The *Brown–Forsythe test* is Levene's test with deviations from the group medians, $Z_{ij} = \lvert Y_{ij} - \tilde Y_i\rvert$, which makes it more robust. Versions of Levene's test with trimmed means work better for symmetric heavy-tailed distributions, the median version for skewed ones.
- The *Breusch–Pagan test* models the error variance as $\sigma_i^2 = h(\boldsymbol{z}_i^{\mathsf T}\boldsymbol{\alpha})$, $\boldsymbol{z}_i^{\mathsf T}\boldsymbol{\alpha} = \alpha_0 + \alpha_1 Z_{i1} + \cdots + \alpha_q Z_{iq}$, for some function $h$ with first and second derivatives. Under $H_0\colon \alpha_1 = \cdots = \alpha_q = 0$ the variance $\sigma_i^2 = h(\alpha_0) = \sigma^2$ is constant. With $\mathrm{SSR}^*$ the regression sum of squares of the regression of $e_i^2$ on $Z_{i1}, \dots, Z_{iq}$, the test statistic is

  $$
  \chi^2_{\mathrm{BP}} = \frac{\mathrm{SSR}^*/2}{(\mathrm{SSE}/n)^2} \overset{H_0}{\approx} \chi^2_q.
  $$
  In simple linear regression one usually takes $Z = X$ and $h = \exp$ ($q = 1$), that is, $\log\sigma_i^2 = \alpha_0 + \alpha_1 X_i$. The test assumes normal errors and a large sample.

### 5.3.3. Are the Errors Normal?

We look at the distribution of the residuals. Unlike the $Y_i$, the residuals can be examined together as one sample, because they all estimate errors with $\mathbb{E}(\varepsilon) = 0$. The common "eye tests" are the scatter in the residual plot, the boxplot, the histogram and the normal Q–Q plot of the residuals.

**Example 5.3.3 (Toluca Residuals)** For the regression of work hours on lot size,

```r
reg <- lm(hours ~ lotsize, data = toluca)
resid <- resid(reg)
hist(resid, freq = FALSE)   # compare with the normal density N(0, MSE)
qqp <- qqnorm(resid)
qqline(resid)
cor(qqp$x, qqp$y)           # correlation between residuals and normal scores
shapiro.test(resid)
```

The histogram is roughly bell-shaped and symmetric, and a normal curve with mean $0$ and variance $\mathrm{MSE}$ fitted on top of it agrees reasonably with a smooth density estimate; the normal Q–Q plot is close to a straight line. The Shapiro–Wilk test gives $W = 0.9789$, $p = 0.8626$: no obvious deviation from normality, since the $p$-value is greater than $0.05$.

Formal tests of normality test

$$
H_0\colon \text{the data are an iid sample from a normal population} \quad\text{vs}\quad H_1\colon \text{they are not}.
$$

- A correlation test uses the correlation between the ordered residuals and their expected values under normality (the normal scores of the Q–Q plot); $H_0$ is rejected when the correlation is smaller than a tabulated critical value.
- The **Shapiro–Wilk test** ([3.2.6](/3.2.6)) is likewise based on the correlation between the order statistics and normal scores. It has the best power among the common tests and is the most common choice. Like every test, it becomes sensitive to small, practically irrelevant departures when $n$ is large.
- The **Kolmogorov–Smirnov test** uses the largest distance between the **empirical distribution function** $F_n$ and the hypothesized $F$, $D_n = \sup_x\lvert F_n(x) - F(x)\rvert$.
- The *Cramér–von Mises test* uses the integrated squared distance $T = n\int_{-\infty}^{\infty}\big(F_n(x) - F(x)\big)^2\,\mathrm{d}F(x)$.
- The *Anderson–Darling test* weights the squared distance by $w(x) = 1/\big(F(x)(1 - F(x))\big)$, $A^2 = n\int_{-\infty}^{\infty}\big(F_n(x) - F(x)\big)^2 w(x)\,\mathrm{d}F(x)$, which gives more weight to the tails.

When the mean and variance of the normal distribution are estimated from the data, as they always are for residuals, the null distributions of the last three statistics change, and corrected critical values must be used. The residuals are moreover slightly correlated; [3.3.7](/3.3.7) shows that this hardly matters when $n$ is large compared with the number of parameters.

To sum up: the real question is whether the distribution of the errors is far enough from normal to invalidate our confidence intervals, significance tests and so on. Look at the distribution of the residuals, use a normal Q–Q plot, and be wary of tests of normality, which reject trivial departures in large samples and miss important ones in small samples.

### 5.3.4. Are the Errors Independent?

Dependence is usually seen in a plot of the residuals against the time order of the observations. The typical pattern is a linear or quadratic trend, or a cyclical pattern; such patterns mean that the observations are not independent. For instance, when the shear strength of welds ($Y$) is regressed on the weld diameter ($X$), the residuals plotted in the order in which the welds were made may drift steadily upward, or rise and fall in waves.

- The *Durbin–Watson test* tests for serially correlated errors. It assumes the first-order autoregressive model $\varepsilon_i = \rho\varepsilon_{i-1} + u_i$ with $-1 < \rho < 1$ and $u_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma_u^2)$, tests $H_0\colon \rho = 0$, and uses

  $$
  d = \frac{\sum_{i=2}^n (e_i - e_{i-1})^2}{\sum_{i=1}^n e_i^2} \approx 2(1 - \hat\rho) \in [0, 4],
  $$
  where $\hat\rho$ is the lag-one sample autocorrelation of the residuals. Exact critical values require tables. As a rule of thumb, $d \in (1.5, 2.5)$ is relatively fine, while $d < 1$ or $d > 3$ is a definite cause for concern.
- The *Ljung–Box test*, from time series analysis, tests the randomness of a series "overall", over a number of lags at once instead of at each distinct lag:

  $$
  Q = n(n + 2)\sum_{k=1}^{h}\frac{\hat\rho_k^2}{n - k} \overset{H_0}{\approx} \chi^2_h,
  $$
  where $\hat\rho_k$ is the sample autocorrelation at lag $k$ and $h$ the number of lags tested.

### 5.3.5. Are There Outliers?

The least squares estimates are based on means and sums of squares, and these numerical summaries are not robust to outliers: a single observation that does not follow the pattern of the others can change the fit considerably. Outliers are seen in the plot of $Y_i$ against $X_i$ and in the residual plot of $e_i$ against $X_i$ or $\hat Y_i$; the residual plot against $X_i$ shows them most clearly. Their precise classification (outliers, high-leverage points, influential observations) is given in [3.3.6](/3.3.6).

**Example 5.3.4 (An Outlier Near the Center)** We generate $20$ observations from $Y = 30 + 50X + \varepsilon$, $\sigma = 200$, at $X = 1, 6, \dots, 96$, and add one outlier at $X = 50$:

```r
x <- seq(1, 100, by = 5)
n <- length(x)
y <- 30 + 50 * x + 200 * rnorm(n)
x <- c(x, 50)
y <- c(y, 30 + 50 * 50 + 10000)       # the last pair is the outlier
a100b1 <- data.frame(x, y)
fit3 <- lm(y ~ x, data = a100b1)              # with the outlier
fit4 <- lm(y ~ x, data = a100b1[-(n + 1), ])  # without the outlier
```

**Example 5.3.5 (An Outlier at an Extreme $X$)** Same data, but the added outlier is $(100,\ 30 + 50 \cdot 100 - 10000)$; `fit5` and `fit6` are the fits with and without it.

| Fit | $b_0$ (std. error) | $b_1$ (std. error) | $s = \sqrt{\mathrm{MSE}}$ | $F$ ($p$-value) |
|---|---|---|---|---|
| without outlier | $26.2$ ($81.3$) | $50.86$ ($1.44$) | $185.8$ | $1245.7$ ($< 10^{-15}$) |
| outlier at $X = 50$ | $459.0$ ($973.9$) | $51.72$ ($17.35$) | $2237$ | $8.89$ ($0.0077$) |
| outlier at $X = 100$ | $861.8$ ($903.5$) | $25.04$ ($15.25$) | $2111$ | $2.69$ ($0.117$) |

The outlier at $X = 50$, close to $\bar X = 48.5$, shifts the whole line upward and so changes the intercept, but hardly the slope; it inflates $s$ more than tenfold and with it all standard errors. The outlier at the extreme value $X = 100$ also tilts the line: the slope is halved, and it is no longer significant at the $0.05$ level. In the residual plot of the first fit the outlier stands out with a residual of about $9500$; in the second the line has been pulled towards the outlier, so the remaining residuals show a spurious increasing trend. An outlier has a large effect on the slope when its $X$ value is far from $\bar X$, and a small one when it is near $\bar X$: this is the leverage of [3.3.6](/3.3.6).

![Two regressions with one outlier each, fitted with and without the outlier: an outlier near the mean of X shifts the line but leaves the slope almost unchanged, while an outlier at an extreme X value tilts the line and halves the slope](./plots/outlier-influence.py)

## Summary

| Assumption | Graphical check | Formal tests |
|---|---|---|
| linearity | scatter plot with smoother; residuals against $X$ or $\hat Y$ | lack-of-fit test ([3.3.6](/3.3.6)) |
| constant variance | residuals against $X$ or $\hat Y$ (funnel shape) | Bartlett, Levene, Brown–Forsythe, Breusch–Pagan |
| normality | histogram, boxplot and normal Q–Q plot of the residuals | correlation test, Shapiro–Wilk, Kolmogorov–Smirnov, Cramér–von Mises, Anderson–Darling |
| independence | residuals against time order | Durbin–Watson, Ljung–Box |
| no outliers | scatter plot, residual plot | studentized residuals, Cook's distance ([3.3.6](/3.3.6)) |

- The model assumes nothing about the distribution of $X$, but the design matters; examine $X$ with numerical summaries (location, spread, skewness $g_1$, kurtosis $g_2$) and plots (sequence plot, stem-and-leaf plot, boxplot, histogram, Q–Q plot). Positive kurtosis means heavier tails than the normal (leptokurtic), negative lighter tails (platykurtic); kurtosis is scale-free and is not the variance.
- The probabilistic assumptions concern the conditional distribution of $Y$ given $X$, so they are checked on the residuals, not on the marginal distribution of $Y$.
- A large $R^2$ and significant tests do not validate the model: a missed curvature (Example 5.3.1) and heteroscedasticity (Example 5.3.2) can coexist with impressive output. Under heteroscedasticity least squares stays unbiased but loses efficiency, and its standard errors are wrong.
- Least squares is not robust: an outlier near $\bar X$ mostly shifts the line, an outlier at an extreme $X$ tilts it.
