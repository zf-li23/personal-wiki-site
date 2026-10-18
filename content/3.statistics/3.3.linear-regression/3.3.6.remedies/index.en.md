---
title: Remedial Measures and Miscellaneous Topics
description: More residual diagnostics (the four diagnostic plots of R, leverage, outliers and influential observations, standardized and studentized deleted residuals, Cook's distance, the F-test for lack of fit), remedial measures for nonlinearity, nonconstant variance and non-normal errors (nonlinear and weighted regression, generalized linear models, variance-stabilizing and Box–Cox transformations), regression through the origin, inverse prediction, the two regression lines and the limitations of R².
---

[3.3.5](/3.3.5) listed what can go wrong with a simple linear regression and how to see it. This chapter completes the diagnostics and turns to the cure. The first part refines the residual analysis: R's built-in diagnostic plots lead to the distinction between outliers, high-leverage points and influential observations, to residuals scaled by their own standard deviations, and to Cook's distance; with repeated observations at the same $X$ values, the **general linear test** of [3.3.4](/3.3.4) becomes a formal test for lack of fit. The second part discusses remedies: nonlinear regression, weighting, generalized linear models and, above all, transformations, with the Box–Cox procedure for choosing one. The last part collects several topics about simple regression: regression through the origin, inverse prediction, the relation between the two regression lines and the correlation coefficient, and the limitations of $R^2$. The matrix approach of [3.3.7](/3.3.7) will extend all of this to several predictors.

## 6.1. More Diagnostics for Residuals

### 6.1.1. Residual Plots Revisited

**Residuals** are what is left over of the response after a model has been fitted to the data, and they reveal patterns in the data that the fitted model does not explain. We look at them to find serious or obvious violations of the model assumptions:

- a nonlinear relationship;
- nonconstant variance;
- non-normal errors;
- dependence;

and also for the presence of outliers and for a strongly skewed distribution. The recommended procedure is:

1. Plot $Y$ against $X$: is the relationship linear? Use `scatter.smooth` to add a smoothed curve.
2. If a straight line is reasonable, fit the model and obtain the residuals.
3. Look at the distribution of the residuals.
4. Plot the residuals against the time (run) order, against $X$ or any other potential explanatory variable, and against the fitted values $\hat Y = b_0 + b_1 X$.
5. In all cases look for nonrandom patterns and for outliers (unusual observations).

### 6.1.2. Built-in Diagnostic Plots in R

Applying `plot` to an `lm` object after a fit shows four diagnostic plots; points with numbers next to them are the most extreme cases of each plot.

1. *Residuals vs Fitted* shows whether the residuals have nonlinear patterns. It is good if the residuals spread equally around a horizontal line without distinct patterns; a curved smoother indicates nonlinearity.
2. *Normal Q–Q* is the **normal Q–Q plot** of the standardized residuals (Section 6.1.3). It is good if the points lie well on the straight dashed line.
3. *Scale–Location* (spread–location) plots $\sqrt{\lvert r_i\rvert}$, the square roots of the absolute standardized residuals, against the fitted values, and checks the assumption of equal variance (**homoscedasticity**). It is good if the smoother is horizontal and the points are spread equally (randomly); an increasing smoother indicates a variance that grows with the mean. Standardized residuals are used because even under homoscedastic errors the raw residuals have unequal variances $\sigma^2(1 - h_{ii})$.
4. *Residuals vs Leverage* helps to find influential cases. Here patterns are not relevant; we watch out for outlying values at the upper right or lower right corner, outside the dashed contours of Cook's distance.

```r
reg <- lm(hours ~ lotsize, data = toluca)
par(mfrow = c(2, 2))   # four plots in one window
plot(reg)
par(mfrow = c(1, 1))
```

For the Toluca data ([3.3.5](/3.3.5)) none of the four plots shows a serious problem; the plots provide rule-of-thumb limits, and the case most often flagged, observation 21 with lot size $30$ and $273$ work hours, is worth a second look but is not influential. The quantities in plots 2–4 are defined next; they will be discussed again for multiple regression in [3.3.11](/3.3.11).

### 6.1.3. Leverage, Outliers and Influence

In simple linear regression every fitted value is a linear combination of the responses. Since $\hat Y_i = \bar Y + b_1(X_i - \bar X)$ and $b_1 = \sum_j (X_j - \bar X)Y_j / \sum_k (X_k - \bar X)^2$,

$$
\hat Y_i = \sum_{j=1}^n h_{ij}Y_j, \qquad h_{ij} = \frac1n + \frac{(X_i - \bar X)(X_j - \bar X)}{\sum_{k=1}^n (X_k - \bar X)^2}.
$$
The $n \times n$ matrix $H = [h_{ij}]$ satisfies $\hat{\boldsymbol{Y}} = H\boldsymbol{Y}$; it is the **hat matrix** of [3.3.7](/3.3.7).

**Definition 6.1.1 (Leverage)** The **leverage** of the $i$-th observation is

$$
h_{ii} = \frac{\partial \hat Y_i}{\partial Y_i},
$$
the $i$-th diagonal element of the hat matrix. It is also called the self-sensitivity or self-influence of the observation.

**Proposition 6.1.1** In simple linear regression,

$$
h_{ii} = \frac1n + \frac{(X_i - \bar X)^2}{\sum_{j=1}^n (X_j - \bar X)^2}.
$$

**Proof** Since $b_0 = \bar Y - b_1\bar X$,

$$
\begin{aligned}
h_{ii} = \frac{\partial \hat Y_i}{\partial Y_i} &= \frac{\partial}{\partial Y_i}(b_0 + b_1X_i) = \frac{\partial}{\partial Y_i}\big[\bar Y + b_1(X_i - \bar X)\big] \\
&= \frac1n + \frac{\partial}{\partial Y_i}\left[(X_i - \bar X)\frac{\sum_{j=1}^n (X_j - \bar X)Y_j}{\sum_{j=1}^n (X_j - \bar X)^2}\right] = \frac1n + \frac{(X_i - \bar X)^2}{\sum_{j=1}^n (X_j - \bar X)^2}. \qquad \square
\end{aligned}
$$

Leverage is a measure of how far the predictor value of an observation is from those of the other observations; it depends only on the $X$ values, not on the responses. (It is a common error to call any case that "does not get along with the trend of the majority" a high-leverage case; that describes an outlier.) Its main properties:

- $h_{ii} \in [0, 1]$, and here $h_{ii} \ge 1/n$ with $\sum_i h_{ii} = 2$, the number of regression parameters (Proposition 7.3.1).
- The smaller $h_{ii}$, the less $Y_i$ affects its own fitted value. If $h_{ii} = 1$, then $\hat Y_i = Y_i$: the line must follow the point perfectly.
- $h_{ii}$ measures the distance of $X_i$ from the center $\bar X$. With several predictors it is the tool for detecting outlying $X$ values, which may be influential, since then no single predictor need look extreme ([3.3.7](/3.3.7)).

**Definition 6.1.2 (Outliers, High-Leverage Points and Influential Observations)** Two types of extreme values are distinguished. An **outlier** is an observation whose response $Y_i$ does not follow the general trend of the rest of the data: it has a high discrepancy, that is, a large residual. An observation is a **high-leverage point** if its predictor value $X_i$ is extreme, that is, if $h_{ii}$ is large; a small change in such a point has the potential to change the fit. An observation is an **influential observation** if it unduly influences any part of the regression analysis: removing it substantially changes the estimated coefficients or fitted values.

The three notions are different. A high-leverage point that lies on the trend of the other points is harmless; an outlier with low leverage mainly shifts the line and inflates $s$ (Example 5.3.4); an outlier with high leverage is typically influential (Example 5.3.5).

**Example 6.1.1** In each panel below, nine points follow a line and a tenth point (the triangle) is added. In panel A the triangle has $X = 20$, far from the others, but lies on the trend: high leverage, not an outlier, little influence. In panel B it has an ordinary $X$ but a response far below the line: an outlier with low leverage, which moves the line only slightly. In panel C it is both far out in $X$ and far from the trend: it pulls the line towards itself and is influential.

![Three regressions with one added observation (triangle), fitted with all data (solid) and without the triangle (dashed): A, a high-leverage point on the trend; B, an outlier with low leverage; C, a high-leverage outlier that changes the slope; the titles give its leverage h, studentized deleted residual t and Cook's distance D](./plots/leverage-influence.py)

Panel C also shows why raw residuals are a poor guide to outliers: an influential point drags the line towards itself, so its own residual is smaller than its discrepancy. The same happens in a well-known small data set of the number of pubs and the number of deaths in eight cities, where one city with five times as many pubs as the others lies far off the line through the other seven points but has a modest raw residual, while its studentized residual is enormous. The remedy is to scale each residual by its standard deviation, and to compare $Y_i$ with a fit that does not use $Y_i$.

**Definition 6.1.3 (Standardized and Studentized Residuals)** Since $\operatorname{Var}(e_i) = \sigma^2(1 - h_{ii})$ ([Section 7.3.3](/3.3.7#sec-7.3.3)), the estimated standard deviation of $e_i$ is $s\{e_i\} = \sqrt{\mathrm{MSE}(1 - h_{ii})}$.

1. The *semistudentized residual* is $e_i^* = e_i / \sqrt{\mathrm{MSE}}$.
2. The **standardized residual** (internally studentized residual) is $r_i = \dfrac{e_i}{s\{e_i\}} = \dfrac{e_i}{\sqrt{\mathrm{MSE}(1 - h_{ii})}}$. Under the model, almost all of them should lie between $-2$ and $2$.
3. The **deleted residual** is $d_i = Y_i - \hat Y_{i(i)}$, where $\hat Y_{i(i)}$ is the predicted response for the $i$-th observation from the model fitted with the $i$-th observation deleted.
4. The **studentized deleted residual** (externally studentized residual) is the standardized deleted residual,

   $$
   t_i = \frac{d_i}{s\{d_i\}} = \frac{e_i}{\sqrt{\mathrm{MSE}_{(i)}(1 - h_{ii})}},
   $$
   where $\mathrm{MSE}_{(i)}$ is the mean squared error of the fit without the $i$-th observation.

In R, `rstandard` returns the $r_i$ and `rstudent` the $t_i$ (which R calls studentized residuals). Studentized deleted residuals offer the better criterion for identifying outliers: under the model with normal errors, $t_i \sim t_{n-p-1}$, where $p$ is the number of regression parameters ($p = 2$ here), so each $t_i$ can be compared with $t$ quantiles (with a Bonferroni adjustment when all $n$ cases are screened). They do not require $n$ refits: as shown below, $d_i = e_i / (1 - h_{ii})$ and $(n - p - 1)\mathrm{MSE}_{(i)} = \mathrm{SSE} - e_i^2/(1 - h_{ii})$, so

$$
t_i = e_i\sqrt{\frac{n - p - 1}{\mathrm{SSE}(1 - h_{ii}) - e_i^2}}.
$$

**Definition 6.1.4 (Cook's Distance)** **Cook's distance** of the $i$-th observation measures its influence on all $n$ fitted values:

$$
D_i = \frac{\sum_{j=1}^n \big(\hat Y_j - \hat Y_{j(i)}\big)^2}{p\,\mathrm{MSE}},
$$
where $\hat Y_{j(i)}$ is the fitted value of the $j$-th case obtained when the $i$-th case is excluded, $p$ is the number of regression parameters and $\mathrm{MSE} = s^2 = \boldsymbol{e}^{\mathsf T}\boldsymbol{e}/(n - p)$.

**Proposition 6.1.2** With $X$ the $n \times p$ design matrix of full column rank,

$$
D_i = \frac{e_i^2}{p\,\mathrm{MSE}}\left[\frac{h_{ii}}{(1 - h_{ii})^2}\right], \qquad d_i = \frac{e_i}{1 - h_{ii}}.
$$

**Proof** Write $A = X^{\mathsf T}X$, let $\boldsymbol{x}_{(i)}^{\mathsf T}$ be the $i$-th row of $X$, so that $h_{ii} = \boldsymbol{x}_{(i)}^{\mathsf T}A^{-1}\boldsymbol{x}_{(i)}$, and let $\boldsymbol{b}_{(i)}$ be the estimate without case $i$. Deleting the case changes $A$ to $A - \boldsymbol{x}_{(i)}\boldsymbol{x}_{(i)}^{\mathsf T}$ and $X^{\mathsf T}\boldsymbol{Y}$ to $X^{\mathsf T}\boldsymbol{Y} - \boldsymbol{x}_{(i)}Y_i$. By the Sherman–Morrison formula $(A - \boldsymbol{x}\boldsymbol{x}^{\mathsf T})^{-1} = A^{-1} + A^{-1}\boldsymbol{x}\boldsymbol{x}^{\mathsf T}A^{-1}/(1 - \boldsymbol{x}^{\mathsf T}A^{-1}\boldsymbol{x})$, and since $\boldsymbol{x}_{(i)}^{\mathsf T}\boldsymbol{b} = \hat Y_i$,

$$
\boldsymbol{b}_{(i)} = \boldsymbol{b} - A^{-1}\boldsymbol{x}_{(i)}Y_i + A^{-1}\boldsymbol{x}_{(i)}\frac{\hat Y_i - h_{ii}Y_i}{1 - h_{ii}} = \boldsymbol{b} - A^{-1}\boldsymbol{x}_{(i)}\frac{e_i}{1 - h_{ii}}.
$$
Hence $d_i = Y_i - \boldsymbol{x}_{(i)}^{\mathsf T}\boldsymbol{b}_{(i)} = e_i + h_{ii}e_i/(1 - h_{ii}) = e_i/(1 - h_{ii})$, and

$$
\sum_{j=1}^n\big(\hat Y_j - \hat Y_{j(i)}\big)^2 = \big\|X(\boldsymbol{b} - \boldsymbol{b}_{(i)})\big\|^2 = \frac{e_i^2}{(1 - h_{ii})^2}\,\boldsymbol{x}_{(i)}^{\mathsf T}A^{-1}X^{\mathsf T}XA^{-1}\boldsymbol{x}_{(i)} = \frac{e_i^2h_{ii}}{(1 - h_{ii})^2}.
$$
Dividing by $p\,\mathrm{MSE}$ gives $D_i$. $\square$

Cook's distance thus combines the size of the residual and the leverage: an observation is influential when both are sizable. $D_i$ is usually compared with the $F_{p,n-p}$ distribution; as a rule of thumb, cases with $D_i > 0.5$ deserve attention and cases with $D_i > 1$ are likely influential. These are the dashed contours in R's residuals-vs-leverage plot; points beyond them, in the upper or lower right corner, are the influential ones.

To recap the new concepts: the standardized residual scales $e_i$ by its own standard deviation, and the studentized deleted residual uses in addition the fit without case $i$; the leverage $h_{ii} = \partial\hat Y_i/\partial Y_i \in [0, 1]$ measures the distance of $X_i$ from the center of the predictor values; Cook's $D_i$ measures the influence of the $i$-th case on all fitted values.

### 6.1.4. The F-Test for Lack of Fit

A residual plot suggests nonlinearity; a formal test of whether the linear model is adequate (a goodness-of-fit test) needs a prerequisite: replicates, that is, repeated observations at the same values of $X$. With replicates the error sum of squares can be split into a pure error part (variation within replicates) and a lack-of-fit part, and the two hypotheses

$$
H_0\colon \text{there is no lack of fit in the linear regression model} \quad\text{vs}\quad H_1\colon \text{there is a lack of fit}
$$
can be compared with the general linear test, by comparing two models.

Suppose there are $c$ distinct predictor levels $X_1, \dots, X_c$ with $n_i$ observations $Y_{i1}, \dots, Y_{in_i}$ at level $X_i$, $\sum_{i=1}^c n_i = n$. In the general linear test of $H_0\colon \beta_1 = 0$ ([3.3.4](/3.3.4)) the full model was $Y_i = \beta_0 + \beta_1X_i + \varepsilon_i$ and the reduced model $Y_i = \beta_0 + \varepsilon_i$. For the lack-of-fit test of $H_0\colon \mu_i = \beta_0 + \beta_1X_i$ against $H_1\colon \mu_i \ne \beta_0 + \beta_1X_i$, the full model allows an arbitrary mean at each level, and the linear model is the reduced one:

$$
\text{full: } Y_{ij} = \mu_i + \varepsilon_{ij}, \qquad \text{reduced: } Y_{ij} = \beta_0 + \beta_1X_i + \varepsilon_{ij}, \qquad i = 1, \dots, c,\ j = 1, \dots, n_i.
$$
The least squares fit of the full model is the level mean $\bar Y_i$, and the error deviation of each observation from the regression line splits as

$$
Y_{ij} - \hat Y_{ij} = (Y_{ij} - \bar Y_i) + (\bar Y_i - \hat Y_{ij}).
$$
For example, if at the third level an observation $Y_{31} = 160$ has level mean $\bar Y_3 = 155$ and fitted value $\hat Y_{31} = 112$, the error deviation $48$ is the pure error deviation $5$ plus the lack-of-fit deviation $43$.

**Definition 6.1.5 (Pure Error and Lack-of-Fit Sums of Squares)** The **pure error sum of squares** and the **lack-of-fit sum of squares** are

$$
\mathrm{SSPE} = \sum_{i=1}^c\sum_{j=1}^{n_i}(Y_{ij} - \bar Y_i)^2, \qquad \mathrm{SSLF} = \sum_{i=1}^c\sum_{j=1}^{n_i}(\bar Y_i - \hat Y_{ij})^2 = \sum_{i=1}^c n_i\big(\bar Y_i - (b_0 + b_1X_i)\big)^2.
$$

**Proposition 6.1.3** $\mathrm{SSE} = \mathrm{SSPE} + \mathrm{SSLF}$, with degrees of freedom $n - 2 = (n - c) + (c - 2)$.

**Proof** Squaring the decomposition and summing, the cross term vanishes because $\bar Y_i - \hat Y_{ij}$ does not depend on $j$ (the fitted value $\hat Y_{ij} = b_0 + b_1X_i$ is the same for all replicates at level $i$):

$$
\sum_{i,j}(Y_{ij} - \bar Y_i)(\bar Y_i - \hat Y_{ij}) = \sum_i(\bar Y_i - \hat Y_{ij})\sum_j(Y_{ij} - \bar Y_i) = 0. \qquad \square
$$

| Source of variation | SS | df | MS |
|---|---|---|---|
| Regression | $\mathrm{SSR} = \sum\sum(\hat Y_{ij} - \bar Y)^2$ | $1$ | $\mathrm{MSR} = \mathrm{SSR}/1$ |
| Error | $\mathrm{SSE} = \sum\sum(Y_{ij} - \hat Y_{ij})^2$ | $n - 2$ | $\mathrm{MSE} = \mathrm{SSE}/(n - 2)$ |
| $\quad$ Lack of fit | $\mathrm{SSLF} = \sum\sum(\bar Y_i - \hat Y_{ij})^2$ | $c - 2$ | $\mathrm{MSLF} = \mathrm{SSLF}/(c - 2)$ |
| $\quad$ Pure error | $\mathrm{SSPE} = \sum\sum(Y_{ij} - \bar Y_i)^2$ | $n - c$ | $\mathrm{MSPE} = \mathrm{SSPE}/(n - c)$ |
| Total | $\mathrm{SSTO} = \sum\sum(Y_{ij} - \bar Y)^2$ | $n - 1$ | |

The error sum of squares of the reduced (linear) model is $\mathrm{SSE}$, that of the full model is $\mathrm{SSPE}$, and their difference is $\mathrm{SSLF}$. The expected mean squares are

$$
\mathbb{E}(\mathrm{MSPE}) = \sigma^2, \qquad \mathbb{E}(\mathrm{MSLF}) = \sigma^2 + \frac{\sum_{i=1}^c n_i\big(\mu_i - (\beta_0 + \beta_1X_i)\big)^2}{c - 2},
$$
so $\mathrm{MSPE}$ estimates $\sigma^2$ whether or not the linear model holds, while $\mathrm{MSLF}$ estimates $\sigma^2$ only if it holds and is larger otherwise. This is why replicates are needed: they provide an estimate of $\sigma^2$ that does not depend on the form of the regression function.

**Theorem 6.1.1 (F-Test for Lack of Fit)** Under the normal error model with $c > 2$ levels and $n > c$,

$$
F^* = \frac{(\mathrm{SSE} - \mathrm{SSPE})/\big((n - 2) - (n - c)\big)}{\mathrm{SSPE}/(n - c)} = \frac{\mathrm{MSLF}}{\mathrm{MSPE}} \overset{H_0}{\sim} F_{c-2,n-c},
$$
and $H_0$ (no lack of fit) is rejected at level $\alpha$ when $F^* > F_{c-2,n-c,\alpha}$.

This is the general linear test statistic of the full model against the reduced one. The test only gives evidence against linearity: if the null hypothesis is rejected, we conclude that a linear regression function does not fit, but the test does not tell us which (nonlinear) regression function would work.

**Example 6.1.2 (Toluca Data)** The $n = 25$ runs have $c = 11$ distinct lot sizes. In R the full model is fitted by treating the lot size as a factor without an intercept, and `anova` compares the two models:

```r
reg  <- lm(hours ~ lotsize, data = toluca)                   # reduced model
Full <- lm(hours ~ 0 + as.factor(lotsize), data = toluca)    # full model: one mean per level
anova(reg, Full)
```

| Model | Res. df | RSS | df | Sum of Sq | $F$ | $p$-value |
|---|---|---|---|---|---|---|
| hours ~ lotsize | $23$ | $54825$ | | | | |
| hours ~ 0 + as.factor(lotsize) | $14$ | $37581$ | $9$ | $17245$ | $0.7138$ | $0.6893$ |

Here $\mathrm{SSE} = 54825$, $\mathrm{SSPE} = 37581$ and $\mathrm{SSLF} = 17245$, so $F^* = (17245/9)/(37581/14) = 0.714$ with $p = 0.689$: there is no evidence of lack of fit, and the linear regression function is adequate for these data.

## 6.2. Remedial Measures

### 6.2.1. Nonlinear Relationships

Many nonlinear relationships can be modeled with linear models: "linear" refers to the parameters, not to the predictor. Both

$$
Y = \beta_0 + \beta_1\log X + \varepsilon \quad\text{(log-linear)}, \qquad Y = \beta_0 + \beta_1X + \beta_2X^2 + \varepsilon \quad\text{(quadratic)}
$$
are linear regression models, the second one with two explanatory variables $X$ and $X^2$, which leads to multiple linear regression ([3.3.7](/3.3.7), [3.3.10](/3.3.10)). Sometimes a nonlinear equation can be transformed into a linear one: the model

$$
Y = \beta_0\exp(\beta_1X + \varepsilon)
$$
becomes, after taking logarithms, the linear model $\log Y = \log\beta_0 + \beta_1X + \varepsilon$. Note that the error enters this model multiplicatively; the transformation is appropriate exactly because it makes the error additive.

**Example 6.2.1 (Michaelis–Menten Model)** In enzyme kinetics the velocity $V$ of a reaction depends on the substrate concentration $C$ through $V = \theta_1C/(\theta_2 + C)$, where $\theta_1$ is the maximum velocity and $\theta_2$ describes how quickly, in terms of increasing concentration, the reaction approaches it. Taking reciprocals gives a linear model in the explanatory variable $1/C$:

$$
\frac1V = \frac1{\theta_1} + \frac{\theta_2}{\theta_1}\cdot\frac1C = \beta_0 + \beta_1\frac1C.
$$
Whether this transformation gives a good fit must be checked like any other model: the reciprocal also transforms the errors, small velocities at low concentrations become large values of $1/V$ with large variability, and the observations with the smallest $C$ (largest $1/C$) have high leverage.

Many other times such transformations do not exist. If we do not want to alter the assumptions on the errors, we can instead perform a *nonlinear regression* analysis: the mean response varies with $X$ in a nonlinear manner, and the observations deviate about these means just as in linear regression, $Y_i = f(X_i; \boldsymbol{\theta}) + \varepsilon_i$ with $f$ nonlinear in the parameters $\boldsymbol{\theta}$. The least squares estimates then have no closed form and are computed iteratively (R `nls`, nonlinear least squares).

### 6.2.2. Nonconstant Variance

Sometimes we need to model the way in which the error variance changes. It may be functionally related to $X$, or, in other words, change with the mean. In this case we use a weighted analysis: weighted least squares minimizes $\sum_i w_i(Y_i - b_0 - b_1X_i)^2$ with weights $w_i$ proportional to $1/\sigma_i^2$, so that the observations with large error variance count less (R: the argument `weights` of `lm`). Weighted least squares is developed in [3.3.12](/3.3.12). Alternatively, a transformation of $Y$ can stabilize the variance (Section 6.2.4).

**Example 6.2.2** In Example 5.3.2 the error standard deviation is $10X$, so the weights $w_i = 1/X_i^2$ are appropriate. A simulation of the same design shows that ordinary and weighted least squares are both unbiased, but the weighted estimates are far more precise: the standard deviation of the intercept estimate drops from about $75$ to about $9$, and that of the slope is halved.

![Histograms of the OLS and WLS estimates of the intercept and slope over 4000 simulated data sets from Y = 30 + 100 X + 10 X eps, X = 1, ..., 100: both are centered at the true values 30 and 100, but the WLS estimates with weights 1/X^2 are much less variable](./plots/wls-vs-ols.py)

### 6.2.3. Non-Normal Errors

Transformations of $Y$ often allow us to keep using linear regression. If not, we use a procedure that allows other distributions for the error term. A *generalized linear model* lets $Y$ follow a distribution from an **exponential family** ([3.2.2](/3.2.2)), for example

- the binomial distribution (yes/no or percentage data),
- the Poisson distribution (count data),
- the gamma distribution (including the exponential),
- the inverse Gaussian (Wald) distribution,
- the negative binomial and the multinomial distributions,

and models the mean as $\mathbb{E}(Y) = g(\beta_0 + \beta_1X_1 + \cdots)$, where $g$ is a monotonic, generally nonlinear transformation; its inverse $g^{-1}$, which maps the mean to the linear predictor, is called the *link function*. **Logistic regression** ([3.4.12](/3.4.12)) is the binomial case with the logit link. In R these models are fitted with `glm`.

### 6.2.4. Transformations

Large values of a response are often more variable than smaller values. Transformations are typically performed to

- stabilize the variance, so as to achieve equal variances;
- improve normality, which is often violated because it is easy to have an outlier when the variance is large, and a transformation can rein it in;
- simplify the model.

Sometimes one transformation solves several of these problems at once.

**Definition 6.2.1 (Variance-Stabilizing Transformation)** Suppose $\mathbb{E}(Y) = \mu$ and $\operatorname{Var}(Y) = h(\mu)$, so that the variance changes with the mean. A transformation $f$ for which $\operatorname{Var}\big(f(Y)\big)$ is approximately constant is called a **variance-stabilizing transformation**.

By the **delta method** ([3.1.14](/3.1.14)), $f(Y) \approx f(\mu) + f'(\mu)(Y - \mu)$, so

$$
\operatorname{Var}\big(f(Y)\big) \approx \big(f'(\mu)\big)^2h(\mu).
$$
Requiring $\big(f'(\mu)\big)^2h(\mu)$ to be constant gives $f'(\mu) = c/\sqrt{h(\mu)}$, that is,

$$
f(\mu) = \int\frac{c\,\mathrm{d}\mu}{\sqrt{h(\mu)}}.
$$
For example, if $h(\mu) = \mu^2$ (constant coefficient of variation), $f(\mu) = \log\mu$; if $h(\mu) = \mu^{2\nu}$ with $\nu \ne 1$, $f(\mu) = c\mu^{1-\nu}$, in particular $f(\mu) = \sqrt\mu$ for Poisson-type variance $h(\mu) = \mu$.

The power transformations generalize these examples. The **Box–Cox transformation** ([3.4.4](/3.4.4)) of a strictly positive response is $Y^* = Y^\lambda$, or, rescaled, $Y^* = (Y^\lambda - 1)/\lambda$; in the second form the limit as $\lambda \to 0$ is the natural logarithm. It adjusts for non-normality and for nonconstant variance (variance stabilization), and $\lambda$ is chosen to give the best fit to the data. If the variance is small at the low end and large at the high end, so that the residual plot fans out, consider the family

| $\lambda$ | $Y^*$ | Name |
|---|---|---|
| $1$ | $Y$ | no transformation |
| $0.5$ | $Y^{1/2}$ | square root |
| $0$ | $\log Y$ | (natural) logarithm |
| $-0.5$ | $Y^{-1/2}$ | reciprocal square root |
| $-1$ | $Y^{-1} = 1/Y$ | reciprocal |

Transformations further down the list are stronger: they shrink large values more than small values. The square root already compresses the higher values, so that the lower values become more spread out; the logarithm compresses high values more aggressively still. A right-skewed distribution can therefore be made more symmetric by a suitable choice.

In regression, $\lambda$ is estimated by including it as a parameter in the nonlinear model

$$
\frac{Y_i^\lambda - 1}{\lambda} = \beta_0 + \beta_1X_i + \varepsilon_i, \qquad \varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2),
$$
and using maximum likelihood. Let $K_2 = \big(\prod_{i=1}^n Y_i\big)^{1/n}$ be the geometric mean of the responses and define the standardized transformed response

$$
h(Y_i, \lambda) = \begin{cases} K_1(Y_i^\lambda - 1), & \lambda \ne 0,\\ K_2\log Y_i, & \lambda = 0,\end{cases} \qquad K_1 = \frac{1}{\lambda K_2^{\lambda-1}},
$$
and let $\mathrm{SSE}(\lambda)$ be the error sum of squares of the least squares regression of $h(Y_i, \lambda)$ on $X_i$.

**Theorem 6.2.1 (Box–Cox Procedure)** The maximum likelihood estimate of $\lambda$ minimizes $\mathrm{SSE}(\lambda)$, and the profile log-likelihood of $\lambda$ is

$$
\ell(\lambda) = \max_{\beta_0,\beta_1,\sigma^2}\log L(\lambda, \beta_0, \beta_1, \sigma^2) = -\frac n2\log\frac{\mathrm{SSE}(\lambda)}{n} + \text{const}.
$$

**Proof** The transformed responses are independent $\mathcal{N}(\beta_0 + \beta_1X_i, \sigma^2)$, so the density of $Y_1, \dots, Y_n$ contains the Jacobian of the transformation:

$$
L(\lambda, \boldsymbol{\beta}, \sigma^2) = \frac{1}{(2\pi)^{n/2}\sigma^n}\exp\left\{-\frac{\sum_{i=1}^n\big((Y_i^\lambda - 1)/\lambda - \beta_0 - \beta_1X_i\big)^2}{2\sigma^2}\right\}J(\lambda; \boldsymbol{Y}), \qquad J(\lambda; \boldsymbol{Y}) = \prod_{i=1}^n\left\lvert\frac{\mathrm{d}}{\mathrm{d}Y_i}\frac{Y_i^\lambda - 1}{\lambda}\right\rvert = \prod_{i=1}^nY_i^{\lambda-1}
$$
(for $\lambda = 0$ the factor is $\prod 1/Y_i$, the same formula). Since $J(\lambda; \boldsymbol{Y}) = K_2^{n(\lambda-1)}$,

$$
\log L = -\frac n2\log(2\pi\sigma^2) - \frac{\sum_i\big((Y_i^\lambda - 1)/\lambda - \beta_0 - \beta_1X_i\big)^2}{2\sigma^2} + n(\lambda - 1)\log K_2 = -\frac n2\log(2\pi\tilde\sigma^2) - \frac{\sum_i\big(h(Y_i, \lambda) - \tilde\beta_0 - \tilde\beta_1X_i\big)^2}{2\tilde\sigma^2},
$$
with $\tilde\sigma^2 = \sigma^2/K_2^{2(\lambda-1)}$ and $\tilde\beta_k = \beta_k/K_2^{\lambda-1}$, a one-to-one reparametrization for fixed $\lambda$. For fixed $\lambda$ this is the normal log-likelihood of the regression of $h(Y_i, \lambda)$ on $X_i$, maximized by the least squares estimates and $\tilde\sigma^2 = \mathrm{SSE}(\lambda)/n$, with maximum $-\frac n2\log\big(2\pi\,\mathrm{SSE}(\lambda)/n\big) - \frac n2$. Hence maximizing over $\lambda$ is the same as minimizing $\mathrm{SSE}(\lambda)$. $\square$

The scaling by the geometric mean makes the error sums of squares comparable across $\lambda$; without it, $\mathrm{SSE}$ would change with the units of the transformed response. In practice one computes $\mathrm{SSE}(\lambda)$ on a grid of $\lambda$ values and takes the minimizer $\hat\lambda$ (the MLE). By **Wilks' theorem** ([3.2.5](/3.2.5)), $-2\log\big(L(\lambda)/L(\hat\lambda)\big) \overset{\cdot}{\sim} \chi^2_1$, which gives the approximate $1 - \alpha$ confidence interval

$$
(\lambda_l, \lambda_u) = \left\{\lambda\colon \ell(\lambda) \ge \ell(\hat\lambda) - \frac12\chi^2_{1,\alpha}\right\}.
$$
The interval matters because $\lambda$ is a tool, not the goal: the goal is a regression model with simple structure and well-behaved errors. Any value inside the interval is compatible with the data, so one usually takes a convenient, interpretable value close to $\hat\lambda$ (such as $0$, $\pm 0.5$ or $\pm 1$) rather than $\hat\lambda$ itself, and then estimates $\boldsymbol{\beta}$ and $\sigma^2$ for the chosen transformation.

**Example 6.2.3 (Plasma Levels)** In a study of $25$ healthy children aged $0$ to $4$ years (five at each age), the plasma level $Y$ of a polyamine decreases with age $X$, and its variability is large at age $0$ and gets smaller with age; the histogram of $Y$ is right-skewed. The untransformed regression has $\mathrm{SSE} = 77.98$ on $23$ degrees of freedom, which is also $\mathrm{SSE}(1)$, since $h(Y_i, 1) = Y_i - 1$. The Box–Cox procedure gives

| $\lambda$ | $-1.0$ | $-0.9$ | $-0.8$ | $-0.7$ | $-0.6$ | $-0.5$ | $-0.4$ | $-0.3$ | $-0.2$ | $-0.1$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $\mathrm{SSE}(\lambda)$ | $33.91$ | $32.70$ | $31.76$ | $31.09$ | $30.69$ | $30.56$ | $30.72$ | $31.18$ | $31.95$ | $33.06$ |

so $\hat\lambda = -0.5$, and the $95\%$ confidence interval is about $(-1.1, 0.1)$. Based on the plot of the profile log-likelihood, either the reciprocal square root or the logarithm is a reasonable choice. After either transformation the spread is roughly constant across ages and the histogram of the transformed response is roughly symmetric; the relation remains monotone (increasing for $Y^{-1/2}$, decreasing for $\log Y$) and close to linear.

```r
library(MASS)
boxcox(plasma ~ age, data = a1, lambda = seq(-1.5, 0.5, length = 10))  # profile log-likelihood
# the same by hand: SSE(lambda) of the standardized transformed response
n <- nrow(a1)
k2 <- exp(mean(log(a1$plasma)))           # geometric mean
lambda <- seq(-1, 1, by = 0.1)
sse <- sapply(lambda, function(l) {
  h <- if (l == 0) k2 * log(a1$plasma) else (a1$plasma^l - 1) / (l * k2^(l - 1))
  deviance(lm(h ~ a1$age))                # error sum of squares
})
lambda[which.min(sse)]
a1$tplasma <- a1$plasma^(-0.5)            # apply the chosen transformation
```

![Box-Cox procedure on simulated data with five observations at each of five predictor values: the spread of Y shrinks as X grows, Y^(-1/2) has nearly constant spread, and the profile log-likelihood of lambda is maximized near -0.5 with a 95% confidence interval that excludes both 1 and 0](./plots/box-cox-profile.py)

When the error variance is constant but the relation is curved, one transforms $X$ instead, which leaves the error distribution unchanged; when the error variance also changes with $X$, one transforms $Y$, possibly combined with a transformation of $X$. The prototype patterns are:

| Pattern of the scatter plot | Transformation |
|---|---|
| constant spread; increasing, concave | $X' = \log_{10}X$ or $X' = \sqrt X$ |
| constant spread; increasing, convex | $X' = X^2$ or $X' = \exp(X)$ |
| constant spread; decreasing, convex | $X' = 1/X$ or $X' = \exp(-X)$ |
| spread increasing with the mean | $Y' = \sqrt Y$, $Y' = \log_{10}Y$ or $Y' = 1/Y$ |

## 6.3. Additional Topics

### 6.3.1. Regression Through the Origin

**Definition 6.3.1 (Regression Through the Origin)** The model $Y_i = \beta_1X_i + \varepsilon_i$, that is, the simple linear regression model with $\beta_0 = 0$ assumed, is called **regression through the origin**. Its least squares estimate is

$$
b_1 = \frac{\sum_{i=1}^n X_iY_i}{\sum_{i=1}^n X_i^2},
$$
and $\mathrm{MSE} = \sum_i e_i^2/(n - 1)$. In R it is fitted by `lm(Y ~ 0 + X)`.

Even when theory says that the line should pass through the origin, fitting this model is generally not a good idea. A wrong model is easily specified, and chance variation in the data can be mistaken for structure; forcing the line through $(0, 0)$ may force the model to behave in a certain way in a region where there are no data. The usual statistics also lose their properties:

- the residuals no longer sum to zero, $\sum_i e_i \ne 0$, because the normal equation for the intercept is missing;
- the decomposition $\sum(Y_i - \bar Y)^2 = \sum(Y_i - \hat Y_i)^2 + \sum(\hat Y_i - \bar Y)^2$ fails, because the cross term $2\sum(Y_i - \hat Y_i)(\hat Y_i - \bar Y)$ no longer vanishes, so $\mathrm{SSTO} \ne \mathrm{SSE} + \mathrm{SSR}$, and the degrees of freedom do not add up as $n - 1 = (n - 2) + 1$;
- $R^2$ computed by software is then based on the uncentered sums $\sum Y_i^2 = \sum\hat Y_i^2 + \sum e_i^2$ (with $n = (n - 1) + 1$ degrees of freedom) and cannot be compared with the $R^2$ of the model with an intercept;
- $b_1$ and $\bar Y$ are correlated, $\operatorname{Cov}(b_1, \bar Y) = \sigma^2\sum_iX_i/(n\sum_iX_i^2) \ne 0$, whereas in the model with intercept $\operatorname{Cov}(b_1, \bar Y) = 0$.

A safer approach is to fit the model with an intercept and test whether $\beta_0 = 0$.

### 6.3.2. Inverse Prediction

The model is the same, $Y_i = \beta_0 + \beta_1X_i + \varepsilon_i$, with fitted regression function $\hat Y = b_0 + b_1X$. Instead of predicting a new $Y_h$ at a given $X_h$, we now observe a new response $Y_{h(\mathrm{new})}$ and want to estimate the $X_h$ that produced it.

**Definition 6.3.2 (Inverse Prediction)** **Inverse prediction** (calibration) estimates the predictor value $X_h$ corresponding to a new observation $Y_{h(\mathrm{new})}$ by solving the fitted equation for $X$:

$$
\hat X_h = \frac{Y_{h(\mathrm{new})} - b_0}{b_1}, \qquad b_1 \ne 0.
$$

An approximate $1 - \alpha$ confidence interval is $\hat X_h \pm t_{n-2,\alpha/2}\,s\{\mathrm{pred}X\}$ with

$$
s^2\{\mathrm{pred}X\} = \frac{\mathrm{MSE}}{b_1^2}\left[1 + \frac1n + \frac{(\hat X_h - \bar X)^2}{\sum_{i=1}^n(X_i - \bar X)^2}\right],
$$
which is adequate when $t_{n-2,\alpha/2}^2\,\mathrm{MSE}/\big(b_1^2\sum(X_i - \bar X)^2\big)$ is small (say below $0.1$), that is, when the slope is estimated precisely. Typical technical applications are the validation of new instruments and the assessment of "unknown" samples against a set of standard values. For example, when measured galactose concentrations $Y$ are calibrated against known actual concentrations $X$ with the fitted line $\hat Y = -0.100 + 1.017X$, a new measurement is converted into an estimated actual concentration by $\hat X_h = (Y_{h(\mathrm{new})} + 0.100)/1.017$.

Inverse prediction is not the same as regressing $X$ on $Y$. The regression of $Y$ on $X$ minimizes the vertical distances of the points from the line, the regression of $X$ on $Y$ the horizontal ones, and the two lines differ unless the points lie exactly on a line.

### 6.3.3. The Two Regression Lines

Let

$$
r = \frac{\sum(X_i - \bar X)(Y_i - \bar Y)}{\sqrt{\sum(X_i - \bar X)^2}\sqrt{\sum(Y_i - \bar Y)^2}}
$$
be the sample **correlation coefficient**, and $s_X$, $s_Y$ the sample standard deviations. The regression of $Y$ on $X$ and the regression of $X$ on $Y$,

$$
Y = b_0 + b_1X, \qquad X = a_0 + a_1Y, \qquad b_1 = r\frac{s_Y}{s_X}, \qquad a_1 = r\frac{s_X}{s_Y},
$$
both pass through $(\bar X, \bar Y)$, and $a_1b_1 = r^2$. Drawn in the same $(X, Y)$-plane, the second line is $Y = -a_0/a_1 + X/a_1$. Since $0 \le a_1b_1 \le 1$, we have $\lvert b_1\rvert \le 1/\lvert a_1\rvert$ (for $r \ne 0$): the regression of $Y$ on $X$ is always the flatter one, and both are systematically pulled away from the major axis of the data towards the mean of the predicted variable.

**Proposition 6.3.1** Let $\theta$ be the angle between the two regression lines, $r \ne 0$. Then

$$
\tan\theta = \frac{1/a_1 - b_1}{1 + b_1/a_1} = \frac{1 - a_1b_1}{a_1 + b_1} = \frac{1 - r^2}{r\left(\dfrac{s_X}{s_Y} + \dfrac{s_Y}{s_X}\right)}.
$$
In particular, if $s_X = s_Y$ and $r > 0$, then $\tan\theta = (1 - r^2)/(2r)$, equivalently

$$
r = \frac{1 - \sin\theta}{\cos\theta} = \tan\Big(\frac\pi4 - \frac\theta2\Big).
$$

**Proof** The first formula is the angle between two lines with slopes $1/a_1$ and $b_1$; multiplying numerator and denominator by $a_1$ gives the second, and $a_1 + b_1 = r(s_X/s_Y + s_Y/s_X)$ with $a_1b_1 = r^2$ gives the third. For $s_X = s_Y$, solving $r^2 + 2r\tan\theta - 1 = 0$ for $r > 0$ gives $r = \sec\theta - \tan\theta = (1 - \sin\theta)/\cos\theta$. $\square$

This is the geometric meaning of $r$: the smaller the angle between the two regression lines, the larger $\lvert r\rvert$. If $s_X = s_Y$ and $r = 1$, the two lines coincide with the line $Y - \bar Y = X - \bar X$; if $r = -1$, they coincide with the line of slope $-1$; if $r = 0$, they are perpendicular, the horizontal line $Y = \bar Y$ and the vertical line $X = \bar X$.

### 6.3.4. Limitations of R²

Recall the **coefficient of determination** ([3.3.4](/3.3.4))

$$
R^2 = \frac{\mathrm{SSR}}{\mathrm{SSTO}} = \frac{b_1^2\sum(X_i - \bar X)^2}{\sum(Y_i - \bar Y)^2}
$$
(in R, `summary(fit)$r.squared`). It is often misread; always plot the data, because very different data sets can share the same fit and the same $R^2$ (Anscombe's quartet, [Example 7.4.1 of 3.4.7](/3.4.7#ex-7.4.1)). In particular:

- $R^2$ does not measure goodness of fit. With a large $\sigma^2$, $R^2$ can be tiny even when the model is completely correct; it can be high when an obvious nonlinear term is missing (Example 5.3.1, $R^2 = 0.87$); and since $R^2$ grows with $\sum(X_i - \bar X)^2$, it can be made anywhere between $0$ and $1$ just by changing the range of $X$.
- $R^2$ says nothing about predictive ability; the $\mathrm{MSE}$ is a better measure of the prediction error.
- $R^2$ cannot be used to compare models with transformed responses, since the total sum of squares changes with the scale of $Y$; $R^2$ can easily go down when the model assumptions are better fulfilled.
- $R^2$ does not measure how one variable explains another: regressing $X$ on $Y$ gives exactly the same $R^2 = r^2$.

The adjusted $R^2$ of [3.3.7](/3.3.7) does nothing to address any of these issues.

## Summary

| Quantity | Formula | Use |
|---|---|---|
| leverage | $h_{ii} = \partial\hat Y_i/\partial Y_i = \frac1n + \frac{(X_i - \bar X)^2}{\sum(X_j - \bar X)^2}$ | outlying $X$ values |
| standardized residual | $r_i = e_i/\sqrt{\mathrm{MSE}(1 - h_{ii})}$ | Q–Q and scale–location plots |
| studentized deleted residual | $t_i = e_i/\sqrt{\mathrm{MSE}_{(i)}(1 - h_{ii})} \sim t_{n-p-1}$ | outlying $Y$ values |
| Cook's distance | $D_i = \frac{e_i^2}{p\,\mathrm{MSE}}\frac{h_{ii}}{(1 - h_{ii})^2}$ | influence on all fitted values |
| lack-of-fit test | $F^* = \mathrm{MSLF}/\mathrm{MSPE} \sim F_{c-2,n-c}$ | linearity, with replicates |

- Outliers have large residuals, high-leverage points extreme predictor values; influential observations change the fit when removed, and high-leverage outliers usually are influential.
- Remedies: nonlinear relations by transforming $X$, adding terms, or nonlinear regression; nonconstant variance by weighted least squares or variance-stabilizing transformations of $Y$; non-normal errors by transformations or generalized linear models.
- A variance-stabilizing transformation solves $f'(\mu) \propto 1/\sqrt{h(\mu)}$. The Box–Cox procedure chooses $\lambda$ by minimizing $\mathrm{SSE}(\lambda)$ of the geometric-mean-standardized response; a convenient $\lambda$ inside the Wilks confidence interval is preferred to $\hat\lambda$ itself.
- Regression through the origin destroys $\sum e_i = 0$ and the ANOVA decomposition; inverse prediction solves the fitted line for $X$; the two regression lines satisfy $a_1b_1 = r^2$, and their angle measures $r$; $R^2$ is not a measure of fit, prediction or explanation.
