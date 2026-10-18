---
title: "Multiple Linear Regression: Example and Inference"
description: A complete multiple regression analysis of student data (exploration, transformations, competing models, nested-model F-tests), followed by the distribution theory of the normal linear model and the matrix forms of the t-tests, confidence intervals for coefficients and mean responses, and prediction intervals.
---

Building a simple linear regression model is a short routine: plot the data, fit a line, test the slope, check the residuals. With several explanatory variables each step becomes harder. There are many candidate models, the explanatory variables are correlated with each other, and the coefficient of a variable, its standard error and its significance all change with the other variables in the model. This chapter first works through a complete analysis of a real data set to show these difficulties and the usual ways of handling them. It then states the fundamental distribution theorem of the normal linear model and uses it to restate, in matrix form, the inference of [3.3.3](/3.3.3) and [3.3.4](/3.3.4): tests and confidence intervals for single coefficients, confidence intervals for the mean response and prediction intervals for new observations. The matrix notation and the least squares estimator come from [3.3.7](/3.3.7); the comparison of nested models by **general linear tests**, used informally here, is developed in [3.3.9](/3.3.9), and correlated explanatory variables are the subject of [3.3.10](/3.3.10).

## 8.1. A Multiple Regression Example

### 8.1.1. The Problem and the Data

**Example 8.1.1 (Computer Science Students)** Too many computer science majors at a university drop out of the program. Can we find predictors of success that are available when a student enters the program? For $n=224$ students the data record

| variable | meaning | values |
|---|---|---|
| gpa | grade point average after three semesters (the response $Y$) | $0.12$ to $4.00$ |
| hsm, hss, hse | high school grades in mathematics, science and English | integers $2$ to $10$ |
| satm, satv | SAT scores in mathematics and verbal | integers $200$ to $800$ |
| sex | gender (of interest for other questions) | $1$, $2$ |

For now we ignore gender, so there are five explanatory variables: three high school grades and two SAT scores.

### 8.1.2. Exploration and Transformations

Before fitting any model we look at the variables one at a time (summaries and histograms) and then in pairs (correlations and a scatter plot matrix, `pairs()` in R). Two questions arise at this stage: whether the response or the explanatory variables should be transformed, and what the configuration of the explanatory variables implies for the analysis.

Highly skewed distributions are difficult to examine: apparently outlying values appear in the direction of the skew, while unusual values in the opposite direction can be hidden. The mean of a skewed distribution is a poor summary of its center, and the variance is very sensitive to outliers and skewness. Power transformations make a skewed distribution more symmetric: roots, logarithms or reciprocals reduce right skewness, and squares, cubes or higher powers reduce left skewness. The logarithm is especially common, because

$$
\log Y_1-\log Y_2=\log\Big(1+\frac{Y_1-Y_2}{Y_2}\Big)\approx\frac{Y_1-Y_2}{Y_2}
$$
turns absolute changes into relative changes; moreover a positive response cannot be described exactly by $Y=X\boldsymbol{\beta}+\varepsilon$ with normal errors, while its logarithm can take any real value. The price is interpretation. If $\log Y=X\boldsymbol{\beta}+\varepsilon$ and the coefficient of $X_k$ is estimated by $b_k$, then a one-unit increase in $X_k$, the other variables fixed, multiplies the fitted value $\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\boldsymbol{b}}$ by $\mathrm{e}^{b_k}$, a change of $(\mathrm{e}^{b_k}-1)\times100\%$. Note that $\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\boldsymbol{b}}$ estimates the median of $Y$, not its mean: with normal errors $\mathbb{E}(Y)=\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}+\sigma^2/2}$.

One should think twice before transforming. A transformation can destroy the interpretation (awkward exponents chosen by the **Box–Cox transformation** are the extreme case); it changes the null hypothesis and the error distribution; it does not guarantee normality or constant variance; back-transformed confidence intervals may be biased; and the transformed scale often does not answer the question of interest (a physician wants a result in mg/dL, not in standard deviations). Alternatives are generalized linear models, resampling methods and nonparametric methods.

### 8.1.3. The Explanatory Variables

The configuration of the $X$'s matters as much as the distribution of $Y$. A good design gives more power and makes the whole analysis valid; one should ask whether there are possible confounders and extreme cases. In particular, beware of *hidden extrapolation*: with correlated explanatory variables, a point can lie within the range of every single variable and still be far from the region covered by the data jointly, so that the fitted model is used where it was never checked. A good fit to the data is not the same as usefulness for prediction.

![Hidden extrapolation: the data cover an elongated elliptical region in the (X1, X2) plane; the marked new point lies inside the range of X1 and inside the range of X2 but far outside the joint region of the data](./plots/hidden-extrapolation.py)

In the student data the histograms show no obvious problems, so no transformation is used. The sample **correlation coefficients** are

| | gpa | hsm | hss | hse | satm | satv |
|---|---|---|---|---|---|---|
| gpa | $1$ | $0.437$ | $0.329$ | $0.289$ | $0.252$ | $0.114$ |
| hsm | | $1$ | $0.576$ | $0.447$ | $0.454$ | $0.221$ |
| hss | | | $1$ | $0.579$ | $0.240$ | $0.262$ |
| hse | | | | $1$ | $0.108$ | $0.244$ |
| satm | | | | | $1$ | $0.464$ |

All correlations with gpa are significant at level $0.05$ (`cor.test()`) except that with satv ($p=0.087$); among the explanatory variables only hse and satm are not significantly correlated ($p=0.106$). The high school grades are clearly related to gpa, but the trends are not evident in the scatter plots, and the explanatory variables are correlated with each other. Should we simply drop satv? The answer depends on the other variables in the model, as the next step shows.

### 8.1.4. Comparing Models

We fit several models with `lm()` and compare them.

```r
fit1 <- lm(gpa ~ hsm + hss + hse, data = csdata)
summary(fit1)   # coefficients, t-tests, R^2, overall F-test
anova(fit1)     # sequential sums of squares
plot(fit1)      # diagnostic plots
fit2 <- lm(gpa ~ hsm + hse, data = csdata)
fit3 <- lm(gpa ~ hsm, data = csdata)
fit4 <- lm(gpa ~ satm + satv, data = csdata)
fit5 <- lm(gpa ~ hsm + hss + hse + satm + satv, data = csdata)
```

| model | explanatory variables | $R^2$ | $R_a^2$ | $s=\sqrt{\mathrm{MSE}}$ | overall $F$ (df) | $p$-value |
|---|---|---|---|---|---|---|
| 1 | hsm, hss, hse | $0.2046$ | $0.1937$ | $0.6998$ | $18.86$ $(3,220)$ | $6.4\times10^{-11}$ |
| 2 | hsm, hse | $0.2016$ | $0.1943$ | $0.6996$ | $27.89$ $(2,221)$ | $1.6\times10^{-11}$ |
| 3 | hsm | $0.1905$ | $0.1869$ | $0.7028$ | $52.25$ $(1,222)$ | $7.8\times10^{-12}$ |
| 4 | satm, satv | $0.0634$ | $0.0549$ | $0.7577$ | $7.48$ $(2,221)$ | $7.2\times10^{-4}$ |
| 5 | all five | $0.2115$ | $0.1934$ | $0.7000$ | $11.69$ $(5,218)$ | $5.1\times10^{-10}$ |

Here $R_a^2=1-\frac{n-1}{n-p}\cdot\frac{\mathrm{SSE}}{\mathrm{SSTO}}$ is the adjusted $R^2$, which penalizes the number of parameters ([3.3.11](/3.3.11)). The individual results are instructive.

- Model 1: the overall $F$-test is highly significant, but only hsm has a significant $t$-test ($b=0.169$, $t=4.75$); for hss $t=0.91$ ($p=0.36$) and for hse $t=1.17$ ($p=0.25$). A significant $F$-test with insignificant individual $t$-tests is a typical symptom of correlated explanatory variables. The intercept ($0.590$, $p=0.046$) has no meaning here, since no student has all grades equal to $0$.
- Model 2 (hss removed): hsm is highly significant and hse borderline ($t=1.75$, $p=0.082$); $R_a^2$ even increases slightly.
- Model 3 (hsm only): $b=0.208$, $t=7.23$; the MSE and $R_a^2$ are slightly worse than for model 2. With fewer variables the fitted values take fewer distinct values; with hsm alone, an integer from $2$ to $10$, there are at most nine.
- Model 4 (SAT scores only): satm is significant ($t=3.44$) and satv is not ($t=-0.04$); the MSE and $R_a^2$ are much worse.
- Model 5 (all five): only hsm is significant ($t=3.72$, $p=0.0003$), although every variable except satv was significant on its own.

Two $F$-tests comparing nested models (`anova(reduced, full)`) settle the role of the two groups of variables:

| reduced model | full model | extra df | $F$ | $p$-value | conclusion |
|---|---|---|---|---|---|
| hsm, hss, hse | all five | $2$ | $0.950$ | $0.388$ | the SAT scores add nothing |
| satm, satv | all five | $3$ | $13.65$ | $3.4\times10^{-8}$ | the high school grades are needed |

For the first test the residual sums of squares are $107.75$ on $220$ degrees of freedom and $106.82$ on $218$, so $F=\big((107.75-106.82)/2\big)/(106.82/218)=0.950$. Similarly, the three variables hss, satm and satv as a group add nothing to a model containing hsm and hse ($p=0.436$), and with $n=224$ the test has enough power for this to mean that no important information is lost.

Which model is best? hsm is clearly important. Among the models with hsm alone and with hsm and hse, hsm explains $19\%$ of the variation of gpa and hsm with hse $20\%$, and $R_a^2$ slightly favors the two-variable model. The choice depends on the purpose: to interpret the coefficients, the one-variable model avoids the ambiguity caused by correlated explanatory variables; to predict gpa, some correlation among the explanatory variables is harmless and the two-variable model may be preferred. Systematic methods of model selection are the subject of [3.3.11](/3.3.11).

### 8.1.5. Lessons from the Example

1. Look at graphical and numerical summaries one variable at a time, then use plots and correlations to understand the relationships between pairs of variables.
2. A variable can be a significant predictor alone and not significant when other explanatory variables are in the model. Regression coefficients, their standard errors and the results of significance tests depend on which other explanatory variables are in the model.
3. The $t$-test of $\beta_k$ is a *variable-added-last* test: it asks whether $X_k$ helps once all the other variables are already in the model. There is a total amount $\mathrm{SSTO}$ of variation in the response to explain; correlated explanatory variables overlap in the part of this variation that they explain, so they compete with each other, and none of them may look significant although together they are ([3.3.10](/3.3.10)).
4. Significance tests do not tell the whole story. In practice one has to understand how the data were collected, the nature of the variables and how they relate to each other.

A related distinction is between location and variability. Regression coefficients and fitted values describe means; $R^2$ and prediction intervals describe variability. A coefficient can therefore be highly significant while $R^2$ is small: regressing gpa on satm alone gives $b=0.00227$ with $p=0.00014$, but $R^2=0.063$. The two are linked by

$$
F^*=\frac{\mathrm{MSR}}{\mathrm{MSE}}=\frac{R^2}{1-R^2}\cdot\frac{n-p}{p-1},
$$
so with large $n$ even a small $R^2$ gives a large $F^*$. Significance says that the mean response changes with $X$; a small $R^2$ says that individual responses scatter widely around that mean.

![Two data sets with the same regression line and highly significant slopes: in the left panel the points lie close to the line and R^2 is large; in the right panel the noise is much larger and R^2 is small](./plots/significance-vs-r2.py)

**Remark 8.1.1** If every case of the data set is duplicated, the least squares estimates do not change, but the residual sum of squares doubles while the error degrees of freedom grow from $n-p$ to $2n-p$. The estimated standard errors therefore shrink by the factor $\sqrt{(n-p)/(2n-p)}\approx1/\sqrt{2}$, the $t$-statistics grow by about $\sqrt{2}$ and the $p$-values become smaller, although no new information has been added. Standard errors are valid only when the cases are independent.

## 8.2. Inference in Multiple Regression

### 8.2.1. The Model and Least Squares

The data consist of a response $Y$ and $p-1$ explanatory variables $X_1,\dots,X_{p-1}$ observed on $n$ cases, with values $(Y_i,X_{i1},\dots,X_{i,p-1})$ for case $i$. The model is

$$
Y_i=\beta_0+\beta_1X_{i1}+\cdots+\beta_{p-1}X_{i,p-1}+\varepsilon_i,\qquad\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),\quad i=1,\dots,n,
$$
or $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ with $\boldsymbol{\varepsilon}\sim\mathcal{N}_n(\boldsymbol{0},\sigma^2I_n)$, where the $n\times p$ **design matrix** $X$ has rows $\boldsymbol{x}_i^{\mathsf T}=(1,X_{i1},\dots,X_{i,p-1})$ and $p$ counts the parameters including the intercept.

The regression function $\mathbb{E}(Y)=\beta_0+\beta_1X_1+\cdots+\beta_{p-1}X_{p-1}$ is called a *regression surface* or *response surface*; with two explanatory variables it is a plane, for instance $\mathbb{E}(Y)=10+2X_1+5X_2$, and each $Y_i$ deviates from the plane by its error $\varepsilon_i$. This *first-order model* is designed for explanatory variables whose effects on the mean response are additive, that is, do not interact ([3.3.10](/3.3.10)).

**Definition 8.2.1 (Partial Regression Coefficient)** In the first-order model, $\beta_1,\dots,\beta_{p-1}$ are called **partial regression coefficients**: $\beta_k$ is the change in the mean response $\mathbb{E}(Y)$ per unit increase in $X_k$ when all the other explanatory variables are held constant.

The word *partial* is essential: $\beta_k$ describes the effect of $X_k$ given the other variables, which is why its estimate changes when the set of other variables changes (Example 8.1.1).

The least squares results of [3.3.7](/3.3.7) are, with $H=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$ the **hat matrix**,

$$
\boldsymbol{b}=\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y},\qquad\hat{\boldsymbol{Y}}=X\boldsymbol{b}=H\boldsymbol{Y},\qquad\boldsymbol{e}=\boldsymbol{Y}-\hat{\boldsymbol{Y}}=(I_n-H)\boldsymbol{Y},
$$

$$
s^2=\mathrm{MSE}=\frac{\boldsymbol{e}^{\mathsf T}\boldsymbol{e}}{n-p}=\frac{\boldsymbol{Y}^{\mathsf T}(I_n-H)\boldsymbol{Y}}{n-p}.
$$
Geometrically, $\hat{\boldsymbol{Y}}$ is the **orthogonal projection** of $\boldsymbol{Y}$ onto the column space $\mathcal{R}(X)$ and $\boldsymbol{e}$ lies in its orthogonal complement $\mathcal{N}(X^{\mathsf T})$; the coefficient vector $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ is a linear function of $\boldsymbol{Y}$ through $X^{\mathsf T}$. That $\boldsymbol{b}$ and $\boldsymbol{e}$ (hence $s^2$) are independent under normal errors is part of the theorem below.

### 8.2.2. The Fundamental Theorem

Two facts about **quadratic forms** in normal vectors are needed. Let $\chi^2_r(\delta)$ denote the noncentral chi-square distribution with $r$ degrees of freedom and noncentrality parameter $\delta$, the distribution of $\|\boldsymbol{Z}\|^2$ for $\boldsymbol{Z}\sim\mathcal{N}_r(\boldsymbol{\mu},I_r)$ with $\|\boldsymbol{\mu}\|^2=\delta$; for $\delta=0$ it is the central **chi-square distribution** $\chi^2_r$.

**Lemma 8.2.1** Let $\boldsymbol{Z}\sim\mathcal{N}_n(\boldsymbol{\mu},I_n)$ and let $A$ be a symmetric $n\times n$ matrix. Then $\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}\sim\chi^2_r(\boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu})$ if and only if $A$ is idempotent with $\operatorname{rank}(A)=r$.

**Proof** We prove the direction used below. If $A$ is symmetric and idempotent of rank $r$, its eigenvalues are $0$ and $1$, so $A=QQ^{\mathsf T}$ with $Q\in\mathbb{R}^{n\times r}$ having orthonormal columns. Then $\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}=\|Q^{\mathsf T}\boldsymbol{Z}\|^2$ with $Q^{\mathsf T}\boldsymbol{Z}\sim\mathcal{N}_r(Q^{\mathsf T}\boldsymbol{\mu},I_r)$ and $\|Q^{\mathsf T}\boldsymbol{\mu}\|^2=\boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}$. (Conversely, comparing moment generating functions shows that the nonzero eigenvalues of $A$ must all equal $1$.) $\square$

**Lemma 8.2.2** Let $\boldsymbol{y}\sim\mathcal{N}_n(\boldsymbol{\mu},\Sigma)$, let $B$ be a $k\times n$ matrix of constants and $A$ a symmetric idempotent $n\times n$ matrix of constants. If $B\Sigma A=O$, then $B\boldsymbol{y}$ and $\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}$ are independent.

**Proof** Since $A$ is symmetric and idempotent, $\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}=\boldsymbol{y}^{\mathsf T}A^{\mathsf T}A\boldsymbol{y}=(A\boldsymbol{y})^{\mathsf T}(A\boldsymbol{y})$ is a function of $A\boldsymbol{y}$. The vector $(B\boldsymbol{y},A\boldsymbol{y})$ is jointly normal with $\operatorname{Cov}(B\boldsymbol{y},A\boldsymbol{y})=B\Sigma A^{\mathsf T}=B\Sigma A=O$, so $B\boldsymbol{y}$ and $A\boldsymbol{y}$ are independent ([3.1.15](/3.1.15)), and so are $B\boldsymbol{y}$ and any function of $A\boldsymbol{y}$. $\square$

**Theorem 8.2.1 (Fundamental Theorem of the Normal Linear Model)** Suppose that $\boldsymbol{Y}\sim\mathcal{N}_n(X\boldsymbol{\beta},\sigma^2I_n)$, where $X$ is $n\times p$ of rank $p<n$. Then

1. $\boldsymbol{b}\sim\mathcal{N}_p\big(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1}\big)$;
2. $\dfrac{\boldsymbol{e}^{\mathsf T}\boldsymbol{e}}{\sigma^2}=\dfrac{(n-p)s^2}{\sigma^2}\sim\chi^2_{n-p}$;
3. $\boldsymbol{b}$ and $s^2$ are independent.

**Proof** (1) $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ is a linear transformation of a normal vector, with mean $(X^{\mathsf T}X)^{-1}X^{\mathsf T}X\boldsymbol{\beta}=\boldsymbol{\beta}$ and covariance matrix $(X^{\mathsf T}X)^{-1}X^{\mathsf T}(\sigma^2I_n)X(X^{\mathsf T}X)^{-1}=\sigma^2(X^{\mathsf T}X)^{-1}$.

(2) $\boldsymbol{Y}/\sigma\sim\mathcal{N}_n(X\boldsymbol{\beta}/\sigma,I_n)$ and $\boldsymbol{e}^{\mathsf T}\boldsymbol{e}/\sigma^2=(\boldsymbol{Y}/\sigma)^{\mathsf T}(I_n-H)(\boldsymbol{Y}/\sigma)$. The matrix $I_n-H$ is symmetric and idempotent with $\operatorname{rank}(I_n-H)=\operatorname{tr}(I_n-H)=n-p$, and the noncentrality parameter is $\boldsymbol{\beta}^{\mathsf T}X^{\mathsf T}(I_n-H)X\boldsymbol{\beta}/\sigma^2=0$ because $(I_n-H)X=O$. Lemma 8.2.1 gives $\chi^2_{n-p}$.

(3) $\boldsymbol{b}=B\boldsymbol{Y}$ with $B=(X^{\mathsf T}X)^{-1}X^{\mathsf T}$ and $(n-p)s^2=\boldsymbol{Y}^{\mathsf T}A\boldsymbol{Y}$ with $A=I_n-H$, and $B(\sigma^2I_n)A=\sigma^2(X^{\mathsf T}X)^{-1}X^{\mathsf T}(I_n-H)=O$ because $X^{\mathsf T}H=X^{\mathsf T}$. Lemma 8.2.2 gives independence. $\square$

This theorem, also used without proof in [3.2.5](/3.2.5) ([Theorem 5.6.1](/3.2.5#thm-5.6.1) there), is the source of every exact $t$- and $F$-procedure in this course.

### 8.2.3. Inference for Regression Coefficients

The overall $F$-test of [3.3.4](/3.3.4) carries over: to test $H_0\colon\beta_1=\cdots=\beta_{p-1}=0$ against $H_1$: $\beta_k\ne0$ for at least one $k$, use

$$
F^*=\frac{\mathrm{MSR}}{\mathrm{MSE}}=\frac{\mathrm{SSR}/(p-1)}{\mathrm{SSE}/(n-p)}\overset{H_0}{\sim}F_{p-1,n-p},
$$
and reject $H_0$ at level $\alpha$ if $F^*>F_{p-1,n-p,\alpha}$, equivalently if the $p$-value $\mathbb{P}(F_{p-1,n-p}>F^*)$ is less than $\alpha$.

For a single coefficient, Theorem 8.2.1 gives $b_k\sim\mathcal{N}\big(\beta_k,\sigma^2[(X^{\mathsf T}X)^{-1}]_{kk}\big)$, where $[(X^{\mathsf T}X)^{-1}]_{kk}$ is the diagonal entry belonging to $\beta_k$ ($k=0,1,\dots,p-1$). The estimated covariance matrix of $\boldsymbol{b}$ and the estimated variance of $b_k$ are

$$
s^2(\boldsymbol{b})=\mathrm{MSE}\,(X^{\mathsf T}X)^{-1},\qquad s^2(b_k)=\mathrm{MSE}\,[(X^{\mathsf T}X)^{-1}]_{kk}.
$$

**Theorem 8.2.2** Under the normal linear model, $(b_k-\beta_k)/s(b_k)\sim t_{n-p}$. Consequently:

1. the level-$\alpha$ test of $H_0\colon\beta_k=0$ against $H_1\colon\beta_k\ne0$ rejects when $\lvert t^*\rvert>t_{n-p,\alpha/2}$, where $t^*=b_k/s(b_k)$;
2. a $100(1-\alpha)\%$ confidence interval for $\beta_k$ is $b_k\pm t_{n-p,\alpha/2}\,s(b_k)$.

**Proof** $(b_k-\beta_k)/\big(\sigma\sqrt{[(X^{\mathsf T}X)^{-1}]_{kk}}\big)\sim\mathcal{N}(0,1)$ is independent of $(n-p)s^2/\sigma^2\sim\chi^2_{n-p}$ by Theorem 8.2.1, and the ratio of the first to the square root of the second divided by $n-p$ is $(b_k-\beta_k)/s(b_k)$. $\square$

The $t$-test assesses $X_k$ given the other variables in the model, again a variable-added-last test. As a general linear test it compares the full model with the reduced model obtained by deleting $X_k$ only,

$$
Y_i=\beta_0+\beta_1X_{i1}+\cdots+\beta_{k-1}X_{i,k-1}+\beta_{k+1}X_{i,k+1}+\cdots+\beta_{p-1}X_{i,p-1}+\varepsilon_i,
$$
and the two tests are equivalent ([3.3.9](/3.3.9)).

**Example 8.2.1 (Dwaine Studios)** A company operates portrait studios in $21$ medium-sized cities. In each city we observe the sales $Y$, the population aged $16$ and under $X_1$ (thousands) and the per capita disposable income $X_2$ (thousands), and fit $Y_i=\beta_0+\beta_1X_{i1}+\beta_2X_{i2}+\varepsilon_i$.

```r
reg1 <- lm(Sales ~ Targtpop + Dispoinc, data = a1)
summary(reg1)
confint(reg1, level = 0.95)   # t-intervals for each coefficient
```

| | estimate | std. error | $t$ | $p$-value | $95\%$ confidence interval |
|---|---|---|---|---|---|
| intercept | $-68.857$ | $60.017$ | $-1.15$ | $0.266$ | $[-194.95,\ 57.23]$ |
| $X_1$ (Targtpop) | $1.4546$ | $0.2118$ | $6.87$ | $2\times10^{-6}$ | $[1.010,\ 1.899]$ |
| $X_2$ (Dispoinc) | $9.3655$ | $4.0640$ | $2.30$ | $0.033$ | $[0.827,\ 17.904]$ |

Here $s=11.01$ on $18$ degrees of freedom, $R^2=0.9167$, $R_a^2=0.9075$ and $F^*=99.1$ on $(2,18)$ degrees of freedom ($p=1.9\times10^{-10}$). Both variables help to explain sales when the other is already in the model. If $X_1$ alone is used, the fit is $\hat Y=68.05+1.836X_1$ with confidence intervals $[48.24,87.85]$ for the intercept and $[1.529,2.142]$ for the slope: both change dramatically, because the coefficients depend on the other variables in the model.

### 8.2.4. Estimating the Mean Response

At a set of values $\boldsymbol{x}_h=(1,X_{h1},\dots,X_{h,p-1})^{\mathsf T}$ of the explanatory variables, the mean response $\mathbb{E}(Y_h)=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{\beta}$ is estimated by

$$
\hat Y_h=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{b}=\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}\sim\mathcal{N}\big(\boldsymbol{x}_h^{\mathsf T}\boldsymbol{\beta},\ \sigma^2\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h\big),
$$
with estimated variance $s^2(\hat Y_h)=\mathrm{MSE}\,\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h=\boldsymbol{x}_h^{\mathsf T}s^2(\boldsymbol{b})\boldsymbol{x}_h$. As in Theorem 8.2.2, a $100(1-\alpha)\%$ **confidence interval** for $\mathbb{E}(Y_h)$ is

$$
\hat Y_h\pm t_{n-p,\alpha/2}\,s(\hat Y_h).
$$
Its width grows with $\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h$, that is, as $\boldsymbol{x}_h$ moves away from the center of the data in the metric given by $X^{\mathsf T}X$; it also grows with $\mathrm{MSE}$ and with the confidence level, and shrinks as $n$ grows. For large samples the interval remains approximately valid without normal errors.

### 8.2.5. Predicting a New Observation

A new observation $Y_{h(\mathrm{new})}=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{\beta}+\varepsilon_h$ at $\boldsymbol{x}_h$, with $\varepsilon_h\sim\mathcal{N}(0,\sigma^2)$ independent of the data, is predicted by the same $\hat Y_h=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{b}$. Now the uncertainty has two sources, the sampling variability of $\boldsymbol{b}$ and the new error term.

**Theorem 8.2.3** Under the normal linear model,

$$
Y_{h(\mathrm{new})}-\hat Y_h\sim\mathcal{N}\Big(0,\ \sigma^2\big(1+\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h\big)\Big),
$$
and a $100(1-\alpha)\%$ **prediction interval** for $Y_{h(\mathrm{new})}$ is $\hat Y_h\pm t_{n-p,\alpha/2}\,s(\mathrm{pred})$, where $s^2(\mathrm{pred})=\mathrm{MSE}\big(1+\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h\big)$.

**Proof** Substituting $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}(X\boldsymbol{\beta}+\boldsymbol{\varepsilon})=\boldsymbol{\beta}+(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{\varepsilon}$,

$$
Y_{h(\mathrm{new})}-\hat Y_h=\big(\boldsymbol{x}_h^{\mathsf T}\boldsymbol{\beta}+\varepsilon_h\big)-\boldsymbol{x}_h^{\mathsf T}\boldsymbol{b}=\varepsilon_h-\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{\varepsilon}.
$$
The two terms are independent normal variables with mean $0$, so the difference is normal with variance $\operatorname{Var}(\varepsilon_h)+\operatorname{Var}\big(\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{\varepsilon}\big)=\sigma^2+\sigma^2\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h$. Since $\hat Y_h$ depends on the data only through $\boldsymbol{b}$, the difference is independent of $s^2$, and the interval follows as in Theorem 8.2.2. $\square$

Unlike the confidence interval for the mean, the prediction interval depends strongly on the normality of the errors: the term $\sigma^2$ of the new error does not shrink with $n$, so the interval relies on the shape of the error distribution even in large samples.

**Example 8.2.2 (Dwaine Studios, Continued)** `predict(reg1, se.fit = TRUE, interval = "confidence")` and `interval = "prediction"` give, at the observed cities,

| city | $X_1$ | $X_2$ | $Y$ | $\hat Y_h$ | $s(\hat Y_h)$ | $95\%$ CI for $\mathbb{E}(Y_h)$ | $95\%$ prediction interval |
|---|---|---|---|---|---|---|---|
| 1 | $68.5$ | $16.7$ | $174.4$ | $187.18$ | $3.84$ | $[179.11,\ 195.25]$ | $[162.69,\ 211.68]$ |
| 2 | $45.2$ | $16.8$ | $164.4$ | $154.23$ | $3.56$ | $[146.76,\ 161.70]$ | $[129.93,\ 178.53]$ |
| 3 | $91.3$ | $18.2$ | $244.2$ | $234.40$ | $4.59$ | $[224.76,\ 244.04]$ | $[209.34,\ 259.45]$ |
| 21 | $52.3$ | $16.0$ | $166.5$ | $157.06$ | $4.08$ | $[148.49,\ 165.63]$ | $[132.40,\ 181.73]$ |

For city 1, $s^2(\mathrm{pred})=s^2+s^2(\hat Y_h)=11.01^2+3.84^2$, so $s(\mathrm{pred})=11.66$ and the prediction interval $187.18\pm2.101\times11.66$ is about three times as wide as the confidence interval: most of the uncertainty about a single city comes from the new error term, not from the estimation of $\boldsymbol{\beta}$.

### 8.2.6. Diagnostics and Remedies

The diagnostics of [3.3.5](/3.3.5) carry over to multiple regression:

- look at the distribution of each variable and at the relationships between pairs of variables;
- plot the residuals against the fitted values, against each explanatory variable, and against time or order if available;
- check normality with a histogram and a **normal Q–Q plot** of the residuals;
- check constant variance by plotting the residuals against anything that might be related to the variance, such as the fitted values or each $X_k$.

The remedies are also similar: transformations such as the Box–Cox transformation ([3.3.6](/3.3.6)), and analyses with and without possible outliers. Diagnostics specific to multiple regression (added-variable plots, leverage, influence and multicollinearity measures) follow in [3.3.11](/3.3.11), and further remedies in [3.3.12](/3.3.12).

## Summary

- A multiple regression analysis starts with variable-by-variable and pairwise exploration; transformations make skewed variables more symmetric but cost interpretability; correlated explanatory variables can create hidden extrapolation.
- Coefficients, standard errors and $t$-tests depend on the other variables in the model. Each $t$-test is a variable-added-last test; a significant overall $F$-test with insignificant $t$-tests signals correlated explanatory variables; nested models are compared by $F$-tests on the difference of residual sums of squares.
- Significance concerns means, $R^2$ and prediction intervals concern variability: $F^*=\frac{R^2}{1-R^2}\cdot\frac{n-p}{p-1}$.
- The fundamental theorem: $\boldsymbol{b}\sim\mathcal{N}_p(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1})$, $(n-p)s^2/\sigma^2\sim\chi^2_{n-p}$, and the two are independent.

| target | estimate | estimated variance | $100(1-\alpha)\%$ interval |
|---|---|---|---|
| $\beta_k$ | $b_k$ | $\mathrm{MSE}\,[(X^{\mathsf T}X)^{-1}]_{kk}$ | $b_k\pm t_{n-p,\alpha/2}\,s(b_k)$ |
| $\mathbb{E}(Y_h)$ | $\hat Y_h=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{b}$ | $\mathrm{MSE}\,\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h$ | $\hat Y_h\pm t_{n-p,\alpha/2}\,s(\hat Y_h)$ |
| $Y_{h(\mathrm{new})}$ | $\hat Y_h$ | $\mathrm{MSE}\,\big(1+\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h\big)$ | $\hat Y_h\pm t_{n-p,\alpha/2}\,s(\mathrm{pred})$ |
