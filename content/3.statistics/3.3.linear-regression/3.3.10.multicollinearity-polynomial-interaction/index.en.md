---
title: Multicollinearity, Polynomial Regression and Interaction Models
description: Venn diagrams for regression, the three cases of collinearity (orthogonal, degenerate and general designs) and their consequences, the bias from omitting a relevant variable and Simpson's paradox, polynomial regression with centering and orthogonal polynomials, and interaction models with a group indicator or two continuous variables.
---

The difficulties met in [3.3.8](/3.3.8) and [3.3.9](/3.3.9), coefficients that change sign when a variable is added, a significant overall $F$-test with no significant $t$-test, sequential sums of squares that depend on the order, all have one source: correlation among the explanatory variables. This chapter analyzes it systematically. Venn diagrams give an intuitive picture of which information least squares uses for each coefficient. The three cases of zero, perfect and partial collinearity show what correlation does to the estimates, their variances and the sums of squares. Remedies follow: deleting variables, where omitting a relevant variable causes bias (Simpson's paradox is the famous instance), and transforming variables, with polynomial regression as the main example, where centering removes much of the collinearity between a variable and its powers. Finally, interaction models describe effects of one variable that depend on the value of another, in particular when one of them is a group indicator. Numerical diagnostics of collinearity (variance inflation factors) are in [3.3.11](/3.3.11), and remedies that change the estimator, such as **ridge regression**, in [3.3.12](/3.3.12) and [3.4.7](/3.4.7).

## 10.1. Multicollinearity

### 10.1.1. Venn Diagrams

A Venn diagram represents the variation of each variable by a circle and shared variation by overlaps. In simple regression, the overlap of the circles of $y$ and $X$ is the information that least squares uses to estimate $\beta_X$. If this information is variation in $y$ explained uniquely by variation in $X$, the estimate $b_X$ is unbiased; the larger the overlap, the more information is used and the smaller the variance of $b_X$. The rest of the $y$ circle is the variation that $X$ cannot explain; it is attributed to the error term, and the larger it is, the larger the estimate of $\sigma^2$.

With two explanatory variables $X$ and $W$, the $y$ circle splits into four parts: a part shared only with $X$, a part shared only with $W$, a part shared with both, and the unexplained rest. The partial regression coefficient of $X$ ([3.3.8](/3.3.8)) is estimated from the variation in $y$ uniquely attributable to $X$, and that of $W$ from the part unique to $W$; this is the variable-added-last logic of the $t$-tests. The part shared by $X$ and $W$ is not used for either coefficient, since we cannot tell whether the movements of $y$ there are due to $X$ or to $W$. It still counts for the fit, and the rest of the $y$ circle estimates $\sigma^2$.

![Venn diagrams for regression. Left: simple regression, where the overlap of y and X is the information used to estimate beta_X and the rest of y is error. Right: two explanatory variables X and W, where the parts of y unique to X and to W estimate b_X and b_W, the part shared by X and W is used for neither coefficient, and the unexplained part of y estimates sigma^2](./plots/venn-regression.py)

The diagram is a heuristic. It fails in the presence of **suppressor variables** ([3.3.9](/3.3.9)), where the "shared" area would have to be negative.

**Definition 10.1.1 (Multicollinearity)** The explanatory variables of a regression model exhibit **multicollinearity** when they are strongly correlated with each other, that is, when some column of the design matrix is close to a linear combination of the other columns.

Multicollinearity is a property of the explanatory variables, not of the response. Pairwise correlations reveal pairwise collinearity, but a variable can be nearly a linear combination of several others while all its pairwise correlations are moderate.

**Example 10.1.1 (Body Fat, Revisited)** In the body fat model of [3.3.9](/3.3.9) the overall $F$-test is highly significant ($F^*=21.52$, $p=7.3\times10^{-6}$) while none of the three $t$-tests is. The correlations among the explanatory variables are

| | skinfold | thigh | midarm |
|---|---|---|---|
| skinfold | $1$ | $0.924$ | $0.458$ |
| thigh | | $1$ | $0.085$ |

Skinfold and thigh are strongly correlated, and although midarm is only moderately correlated with each of them, its correlation with the best linear combination of skinfold and thigh is $0.995$. The coefficients of skinfold ($X_1$) and thigh ($X_2$) change with the other variables in the model:

| variables in the model | $b_1$ | $b_2$ |
|---|---|---|
| $X_1$ | $0.857$ | |
| $X_2$ | | $0.857$ |
| $X_1,X_2$ | $0.222$ | $0.659$ |
| $X_1,X_2,X_3$ | $4.334$ | $-2.857$ |

### 10.1.2. Zero Collinearity

Recall that $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}\sim\mathcal{N}_p\big(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1}\big)$. The first extreme case is an *orthogonal design*: the explanatory variables are uncorrelated, $r_{jk}=0$ for $j\ne k$.

**Proposition 10.1.1** If the explanatory variables are pairwise uncorrelated, then for every $k$

$$
b_k=\frac{\sum_i(X_{ik}-\bar X_k)(Y_i-\bar Y)}{\sum_i(X_{ik}-\bar X_k)^2}=\frac{s_Y}{s_k}r_{Yk},\qquad\operatorname{Var}(b_k)=\frac{\sigma^2}{\sum_i(X_{ik}-\bar X_k)^2},
$$
the same as in the simple regression of $Y$ on $X_k$ alone.

**Proof** Replacing each $X_k$ by $X_k-\bar X_k$ changes only the intercept, not the slopes or their variances, since the column space and the parametrization of the slopes are unchanged. After centering, the columns are orthogonal to the intercept column and, being uncorrelated, to each other, so $X^{\mathsf T}X=\operatorname{diag}\big(n,S_{11},\dots,S_{p-1,p-1}\big)$ with $S_{kk}=\sum_i(X_{ik}-\bar X_k)^2$. Hence $b_k=\sum_i(X_{ik}-\bar X_k)Y_i/S_{kk}$ and $\operatorname{Var}(b_k)=\sigma^2/S_{kk}$; equivalently, in the standardized model of [3.3.9](/3.3.9), $r_{XX}=I_{p-1}$ and $b_k^*=r_{Yk}$. $\square$

Consequently, with zero collinearity:

- $b_k$ does not depend on which other explanatory variables are in the model;
- the contribution of $X_k$ to $\mathrm{SSTO}$ is clear-cut: $\mathrm{SSR}(X_k\mid\text{others})=\mathrm{SSR}(X_k)$, and the Type I, II and III sums of squares of $X_k$ are the same;
- if the linear model is true, the orthogonal design is optimal: there is no ambiguity between the explanatory variables, and for given spreads $\sum_i(X_{ik}-\bar X_k)^2$ the variances of the $b_k$ are the smallest possible, which gives high power;
- the $p$-values for testing $\beta_k$ still change with the model, because they depend on $\mathrm{MSE}$, which depends on which variables are included.

### 10.1.3. Perfect Collinearity

The other extreme is a *degenerate design*: some explanatory variables (columns of $X$) are linearly dependent, as in $X_1=2X_2$, $X_2-3X_3+X_4=5$, or generally $c_1X_{j_1}+\cdots+c_kX_{j_k}=\text{constant}$. Then $\operatorname{rank}(X^{\mathsf T}X)=\operatorname{rank}(X)<p$, so $(X^{\mathsf T}X)^{-1}$ does not exist and $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ cannot be computed: the normal equations have infinitely many solutions, and the full model with all the explanatory variables cannot be fitted. Geometrically, when $aX_1+bX_2=c$ the data lie in a vertical plane over a line in the $(X_1,X_2)$ plane, and every response plane through the same line in that vertical plane fits equally well.

For each exact linear relation the variables involved are confounded and at least one of them is redundant. The redundancy can be removed mathematically by deleting one of the variables, after which the reduced model can be fitted. But the confounding remains: if $X_1+X_2+X_3=0$, the models with $(X_1,X_2)$, $(X_1,X_3)$ and $(X_2,X_3)$ give identical fits, and their coefficients cannot be interpreted separately.

**Example 10.1.2** Add to the student data of [3.3.8](/3.3.8) the average high school grade $\mathrm{hs}=(\mathrm{hsm}+\mathrm{hss}+\mathrm{hse})/3$ and fit gpa $\sim$ hsm + hss + hse + hs. R reports "1 not defined because of singularities": the coefficient of hs is NA and the other estimates are those of the model without hs. Here $X$ is not of full rank and the least squares solution is not unique, so some statistics are misleading. `Anova()` of the package car gives Type II sums of squares equal to $0$ for all four variables, and refuses to compute Type III sums of squares ("there are aliased coefficients in the model").

### 10.1.4. The General Case

Between the two extremes, the design is neither orthogonal nor degenerate. A small amount of correlation is harmless. As the correlation grows, the part of the variation of $y$ unique to each variable shrinks, less information is used to estimate each coefficient, and the variances of the estimates grow. Higher collinearity increases variance but does not cause bias.

When the correlation becomes large, problems appear on two levels.

- Numerically, $X^{\mathsf T}X$ is close to singular and hard to invert accurately, so $(X^{\mathsf T}X)^{-1}$ becomes unstable.
- Statistically, the ambiguity between the variables increases and the coefficients become hard to interpret; $\operatorname{Cov}(\boldsymbol{b})=\sigma^2(X^{\mathsf T}X)^{-1}$ has large diagonal entries, so $\operatorname{Var}(b_k)$ inflates; the Type I and Type II sums of squares differ, and the ANOVA $F$-tests and the $t$-tests disagree.

Solving the statistical problem also solves the numerical one.

![Sampling distributions of the least squares estimates (b1, b2) over 2000 simulated data sets with the same true coefficients (1, 1): with uncorrelated explanatory variables the estimates form a small round cloud; with correlation 0.95 the cloud is a long thin ellipse along b1 + b2 = 2, so each coefficient is very uncertain while their sum is well determined](./plots/collinearity-sampling.py)

**Example 10.1.3** Break the exact relation of Example 10.1.2 with a little noise, $\mathrm{hs1}=\mathrm{hs}+0.05\,Z$ with $Z$ standard normal, and fit gpa $\sim$ hsm + hss + hse + hs1.

| | without hs1: estimate (s.e.) | with hs1: estimate (s.e.) |
|---|---|---|
| hsm | $0.169$ $(0.035)$ | $-0.308$ $(0.316)$ |
| hss | $0.034$ $(0.038)$ | $-0.429$ $(0.308)$ |
| hse | $0.045$ $(0.039)$ | $-0.425$ $(0.312)$ |
| hs1 | | $1.410$ $(0.930)$ |
| $R^2$, $R_a^2$ | $0.2046$, $0.1937$ | $0.2128$, $0.1985$ |

The standard errors of the grade coefficients grow about ninefold, all three change sign, and hsm is no longer significant. The sequential sums of squares of hsm, hss and hse are unchanged ($25.81$, $1.24$, $0.67$) and hs1 adds $1.12$, but the Type II sums of squares of hsm, hss and hse drop to $0.46$, $0.95$, $0.90$. Meanwhile $R^2$ and the fitted values hardly change; $R^2$ always increases when a variable is added, and here even $R_a^2$ does.

The effects of multicollinearity can be summarized as follows. The regression coefficients are poorly estimated and may be meaningless, and so are their standard errors; the Type I and Type II sums of squares differ; $R^2$ and the predicted values are usually fine; and there is a risk of overfitting ([3.3.11](/3.3.11)). Ask what the purpose of the analysis is. For prediction within the range of the data, collinearity matters little, and a larger sample is a viable remedy. For explanation, collinearity is a real problem.

**Example 10.1.4** For the body fat data, the three two-variable models are

| model | coefficients ($t$) | $R_a^2$ |
|---|---|---|
| skinfold + thigh | $0.222$ $(0.73)$, $0.659$ $(2.27)$ | $0.752$ |
| skinfold + midarm | $1.001$ $(7.80)$, $-0.431$ $(-2.44)$ | $0.761$ |
| thigh + midarm | $0.851$ $(7.57)$, $0.096$ $(0.60)$ | $0.749$ |

For interpretation, skinfold + midarm is preferable: both coefficients are significant and $R_a^2$ is the largest. Skinfold and thigh, correlated at $0.92$, should not be in the same model.

## 10.2. Remedies

### 10.2.1. Deleting Variables

The goal is to refine a model that has redundancy in its explanatory variables. Possible actions are: collect additional data under different experimental or observational conditions, so that the variables are less correlated; replace the variables by uncorrelated combinations of them (**principal component analysis**, [3.4.5](/3.4.5), and **principal component regression**, [3.4.7](/3.4.7)); select variables, removing some predictors ([3.3.11](/3.3.11)); or transform variables (Section 10.2.2). Before deleting variables we must ask: what happens if we omit a relevant one?

**Theorem 10.2.1 (Omitted Variable Bias)** Suppose the true model is $\boldsymbol{Y}=X\boldsymbol{\beta}+W\boldsymbol{\gamma}+\boldsymbol{\varepsilon}$ with $\mathbb{E}(\boldsymbol{\varepsilon})=\boldsymbol{0}$, $\operatorname{Cov}(\boldsymbol{\varepsilon})=\sigma^2I_n$, where $X$ ($n\times p$, containing the intercept) and $W$ ($n\times q$) are fixed and $(X,W)$ has full column rank, but we fit $\boldsymbol{Y}$ on $X$ alone, obtaining $\boldsymbol{b}_X=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ and $\mathrm{MSE}_X$. Then

1. $\mathbb{E}(\boldsymbol{b}_X)=\boldsymbol{\beta}+(X^{\mathsf T}X)^{-1}X^{\mathsf T}W\boldsymbol{\gamma}$;
2. $\operatorname{Cov}(\boldsymbol{b}_X)=\sigma^2(X^{\mathsf T}X)^{-1}$, which is smaller (in the positive semidefinite order) than the covariance matrix $\sigma^2\big(X^{\mathsf T}(I_n-H_W)X\big)^{-1}$ of the coefficients of $X$ in the full model, where $H_W$ is the hat matrix of $W$;
3. $\mathbb{E}(\mathrm{MSE}_X)=\sigma^2+\dfrac{\boldsymbol{\gamma}^{\mathsf T}W^{\mathsf T}(I_n-H_X)W\boldsymbol{\gamma}}{n-p}\ge\sigma^2$.

**Proof** (1) $\mathbb{E}(\boldsymbol{b}_X)=(X^{\mathsf T}X)^{-1}X^{\mathsf T}(X\boldsymbol{\beta}+W\boldsymbol{\gamma})$. (2) The covariance follows as in [3.3.8](/3.3.8); by Theorem 9.3.1 of [3.3.9](/3.3.9), the full-model coefficients of $X$ are $(X^{\mathsf T}M_WX)^{-1}X^{\mathsf T}M_W\boldsymbol{Y}$ with $M_W=I_n-H_W$, whose covariance is $\sigma^2(X^{\mathsf T}M_WX)^{-1}$, and $X^{\mathsf T}M_WX\preceq X^{\mathsf T}X$ because $X^{\mathsf T}H_WX$ is positive semidefinite. (3) $\mathbb{E}(\boldsymbol{Y}^{\mathsf T}A\boldsymbol{Y})=\operatorname{tr}(A\Sigma)+\boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}$ with $A=I_n-H_X$ and $\boldsymbol{\mu}=X\boldsymbol{\beta}+W\boldsymbol{\gamma}$ gives $\mathbb{E}(\mathrm{SSE}_X)=(n-p)\sigma^2+\boldsymbol{\gamma}^{\mathsf T}W^{\mathsf T}(I_n-H_X)W\boldsymbol{\gamma}$. $\square$

So omitting a relevant variable biases the coefficients of the remaining variables, unless the omitted variable is orthogonal to them ($X^{\mathsf T}W=O$), and it biases the estimate of $\sigma^2$ upwards. If $W$ is orthogonal to $X$, then $\boldsymbol{b}_X$ is unbiased and its variance is unchanged, but $\sigma^2$ is still overestimated, so the estimated standard errors are too large. In the other direction, omitting a variable highly collinear with $X$ can reduce the variance considerably. The relevant criterion is then the **mean squared error** $\mathbb{E}\|\boldsymbol{b}_X-\boldsymbol{\beta}\|^2$, bias squared plus variance: omitting a highly collinear variable *may* reduce it, an instance of the **bias–variance trade-off**. As an illustration of the bias, if the true model is $Y=X^2-10X+30+\varepsilon$ and $X$ takes values well above $5$, the regression of $Y$ on $X$ alone has a positive slope (for instance $21.3$), although the coefficient of $X$ in the true model is $-10$.

**Definition 10.2.1 (Simpson's Paradox)** **Simpson's paradox** is the phenomenon that an association between two variables that holds within each of several groups disappears or is reversed when the groups are combined.

In regression terms, the regression of $Y$ on $X$ omits the group variable. If the groups differ in both $X$ and $Y$, the pooled slope can have the opposite sign of the common within-group slope (left panel of the figure below). The paradox is often encountered in social-science and medical statistics, and it is particularly problematic when frequency data are given causal interpretations.

![A continuous X and a group indicator. Left: Simpson's paradox, where the regression line within each group has a positive slope but the pooled line ignoring the groups has a negative slope. Middle: an additive model, two parallel lines with different intercepts. Right: an interaction model, two lines with different slopes](./plots/groups-and-interaction.py)

### 10.2.2. Polynomial Regression

Transformations can reduce collinearity, but they can also create it. The most common transformation of the explanatory variables is to add their powers.

**Definition 10.2.2 (Polynomial Regression Model)** A **polynomial regression** model contains powers of the explanatory variables as additional explanatory variables, for instance the quadratic model $Y_i=\beta_0+\beta_1X_i+\beta_2X_i^2+\varepsilon_i$ in one variable, or the second-order model

$$
Y_i=\beta_0+\beta_1X_{i1}+\beta_2X_{i2}+\beta_{11}X_{i1}^2+\beta_{22}X_{i2}^2+\beta_{12}X_{i1}X_{i2}+\varepsilon_i
$$
in two variables.

The model is still linear in the parameters, so all the theory of [3.3.7](/3.3.7)–[3.3.9](/3.3.9) applies. The issue is that a variable and its powers are generally highly correlated, so polynomial regression creates a multicollinearity problem.

**Example 10.2.1 (Power Cells)** In a designed experiment, the life $Y$ (number of charge–discharge cycles until failure) of a power cell is studied as a function of the charge rate $X_1$ (three levels $0.6$, $1.0$, $1.4$) and the temperature $X_2$ (three levels $10$, $20$, $30$), with $n=11$ cells: the four corner points and the four edge midpoints of the $3\times3$ grid once each, and the center point $(1.0,20)$ three times. Design of experiments is regression analysis behind the scenes; what is not simple are the choices made when planning: which $X$'s to test, which ranges, how many replicates, whether center points are needed ([3.8](/3.8)). We fit the second-order model:

```r
b1$chrate2 <- b1$chrate^2
b1$temp2 <- b1$temp^2
b1$ct <- b1$chrate * b1$temp
reg5 <- lm(cycles ~ chrate + temp + chrate2 + temp2 + ct, data = b1)
```

The overall $F$-test is significant ($F^*=10.57$ on $(5,5)$ degrees of freedom, $p=0.011$, $R^2=0.914$), but none of the individual $t$-tests is (the $p$-values range from $0.10$ to $0.62$): a multicollinearity problem. Indeed $r(X_1,X_1^2)=0.991$ and $r(X_2,X_2^2)=0.986$; high correlations between powers of a variable are common.

The remedy is *centering*: subtract the mean before squaring. The centered variable takes positive and negative values, and for a design symmetric about its mean, as here, the centered variable and its square are exactly uncorrelated. The procedure is: center the explanatory variables (`scale()` in R; standardizing is also fine, but the subtraction of the mean is the key), recompute the squares and cross products from the centered variables, and rerun the regression.

```r
b1$schrate <- scale(b1$chrate)
b1$stemp <- scale(b1$temp)
reg6 <- lm(cycles ~ schrate + stemp + I(schrate^2) + I(stemp^2) + I(schrate * stemp), data = b1)
```

| term | estimate | std. error | $t$ | $p$-value |
|---|---|---|---|---|
| intercept | $162.84$ | $16.61$ | $9.81$ | $0.0002$ |
| charge rate | $-43.25$ | $10.24$ | $-4.22$ | $0.008$ |
| temperature | $58.48$ | $10.24$ | $5.71$ | $0.002$ |
| charge rate squared | $16.44$ | $12.20$ | $1.35$ | $0.236$ |
| temperature squared | $-6.36$ | $12.20$ | $-0.52$ | $0.624$ |
| product | $6.90$ | $9.71$ | $0.71$ | $0.509$ |

Now the linear terms are clearly significant and the second-order terms are not. The general linear test of the three second-order terms gives $F^*=0.78$ on $(3,5)$ degrees of freedom, $p=0.553$, so the first-order model $\hat Y=160.58-139.58X_1+7.55X_2$ ($R^2=0.873$) suffices.

The sequential ANOVA table of the centered model is *exactly* the same as before ($18704$, $34201$, $1646$, $285$, $529$, residual $5240$). This is no coincidence: the sequence of column spaces is the same. For example, $\{1,X_1\}$ and $\{1,X_1-\bar X_1\}$ span the same space, and $(X_1-\bar X_1)^2=X_1^2-2\bar X_1X_1+\bar X_1^2$ lies in the span of $\{1,X_1,X_1^2\}$, so each sequential extra sum of squares, and the fitted values, are unchanged. The $t$-test of the highest-order term is also unchanged; what centering changes are the coefficients and $t$-tests of the lower-order terms.

That observation explains a rule from the design of experiments: it is usually a bad idea to eliminate lower-order terms from a model before the higher-order terms, even if they are not significant (the *hierarchy principle*). An additive change of scale of $X$ changes the $t$-statistics of all but the highest-order term, so the significance of a lower-order term depends on an arbitrary origin. Removing a lower-order term imposes a special structure: just as setting the intercept to zero forces the regression through the origin, setting $a_1=0$ in $y=a_0+a_1x+a_2x^2$ gives $y=a_0+a_2(x-0)^2$, whose extremum is at $x=0$.

Centering is not enough for higher powers: $r(X_1,X_1^3)=0.969$, and for the centered variable with three symmetric levels $-a,0,a$ we even have $(X_1-\bar X_1)^3=a^2(X_1-\bar X_1)$, an exact collinearity (with three levels at most a quadratic can be fitted in each variable). In general, `poly(x, degree)` or `polym(x1, x2, degree = 2)` in R produces *orthogonal polynomials*, polynomials in $X$ whose columns are orthogonal to each other, which avoids collinearity among the powers altogether; the fitted values and sequential sums of squares are again the same.

## 10.3. Interaction Models

### 10.3.1. Interaction

The first-order model assumes that the effects of the explanatory variables on the mean response are additive: the change of $\mathbb{E}(Y)$ per unit of $X_1$ is the same at every value of $X_2$. With several explanatory variables we must consider the possibility that the effect of one variable depends on the value of another.

**Definition 10.3.1 (Interaction Effect)** Two explanatory variables $X_1$ and $X_2$ have an **interaction effect** on $Y$ if the effect of $X_1$ on the mean response depends on the value of $X_2$. In a regression model it is represented by the product term in

$$
Y_i=\beta_0+\beta_1X_{i1}+\beta_2X_{i2}+\beta_3X_{i1}X_{i2}+\varepsilon_i;
$$
the model without the product term is called additive.

We consider two cases: one continuous variable and one binary (yes/no) variable, and two continuous variables.

### 10.3.2. A Continuous Variable and a Group Indicator

Let $X_1$ be continuous and let $X_2$ take the value $0$ for group 1 and $1$ for group 2. The interaction model gives one line per group:

$$
X_2=0\colon\ \mathbb{E}(Y)=\beta_0+\beta_1X_1,\qquad X_2=1\colon\ \mathbb{E}(Y)=(\beta_0+\beta_2)+(\beta_1+\beta_3)X_1.
$$
Hence

- $H_0\colon\beta_2=\beta_3=0$ tests whether the two groups have the same regression line;
- $H_0\colon\beta_3=0$ tests whether the slopes are the same, that is, whether the lines are parallel (no interaction);
- $H_0\colon\beta_2=0$ tests whether the intercepts are the same, given possibly different slopes.

Each is a general linear test of [3.3.9](/3.3.9), and the test of $\beta_3=0$ is the $t$-test of the product term. Interaction thus means non-parallel lines: the slope of the line depends on the group (middle and right panels of the figure in Section 10.2.1).

**Example 10.3.1 (Adoption of an Innovation)** For $20$ insurance companies, $Y$ is the number of months it took the company to adopt an innovation, $X_1$ is the size of the firm (continuous) and $X_2$ the type of firm ($0$ for a mutual company, $1$ for a stock company). Do stock firms adopt the innovation more slowly or faster than mutual firms, across all firm sizes? A scatter plot colored by type (`ggplot()` with `geom_smooth()`) suggests two lines with different intercepts and similar slopes.

```r
a1$sizestock <- a1$size * a1$stock
reg1 <- lm(months ~ size + stock + sizestock, data = a1)
reg2 <- lm(months ~ size, data = a1)
anova(reg2, reg1)    # H0: beta_2 = beta_3 = 0 (same line)
summary(reg1)        # t-test of sizestock: H0: beta_3 = 0 (parallel lines)
```

The test of a common line has $\mathrm{SSE}=492.63$ on $18$ degrees of freedom against $176.38$ on $16$, $F^*=14.34$ and $p=0.0003$: the linear relationship differs between the groups. In the interaction model the product term has $b_3=-0.0004$ with $t=-0.02$ ($p=0.98$): no evidence against parallel lines. The coefficient of stock, $8.13$ ($t=2.23$, $p=0.041$), estimates the difference of the intercepts at size $0$, which is outside the range of the data; centering size changes it to the difference at the mean size, $8.06$ with standard error $1.50$ ($t=5.36$) instead of $3.65$, a much more precise and meaningful comparison.

The additive model gives $\hat Y=33.87-0.1017X_1+8.06X_2$: the common slope is $-0.10$ months per unit of size ($t=-11.4$), and stock firms take on average $8.06$ months longer ($t=5.52$, $p=3.7\times10^{-5}$), with intercept $33.87+8.06=41.93$.

```r
reg5 <- lm(months ~ size + stock, data = a1)
beta <- coef(reg5)
ggplot(a1, aes(size, months, color = as.factor(stock))) +
  geom_point() +
  geom_abline(intercept = beta[1], slope = beta[2]) +              # mutual firms
  geom_abline(intercept = beta[1] + beta[3], slope = beta[2])      # stock firms
```

### 10.3.3. Two Continuous Variables

With two continuous variables the interaction model can be rewritten in two ways:

$$
Y=\beta_0+(\beta_1+\beta_3X_2)X_1+\beta_2X_2+\varepsilon=\beta_0+\beta_1X_1+(\beta_2+\beta_3X_1)X_2+\varepsilon.
$$
The coefficient of $X_1$ is a linear function of $X_2$ and vice versa: the response surface is no longer a plane but a twisted surface, whose sections at fixed $X_2$ are lines with slopes $\beta_1+\beta_3X_2$. In particular $\beta_1$ is the effect of $X_1$ only at $X_2=0$, which is another reason to center the variables before forming products, as in Example 10.2.1. Interactions of a group indicator with several continuous variables, and of several factors, lead to the analysis of variance of [3.3.12](/3.3.12)–[3.3.14](/3.3.14).

## Summary

| design | estimates | sums of squares | consequences |
|---|---|---|---|
| orthogonal ($r_{jk}=0$) | $b_k=(s_Y/s_k)r_{Yk}$, independent of the other variables; smallest variances | Types I, II, III equal | optimal; only the $p$-values depend on the model (through $\mathrm{MSE}$) |
| degenerate (exact linear relation) | $(X^{\mathsf T}X)^{-1}$ does not exist; not unique | not defined (aliased) | delete a redundant variable; confounding remains |
| general (strong correlation) | unbiased but with inflated variances, unstable, may change sign | Types I and II differ | $F$- and $t$-tests disagree; prediction fine, interpretation hard |

- Omitting a relevant variable $W$ biases $\boldsymbol{b}_X$ by $(X^{\mathsf T}X)^{-1}X^{\mathsf T}W\boldsymbol{\gamma}$ and inflates $\mathrm{MSE}$, but may reduce variance; Simpson's paradox is the extreme case of a reversed association.
- Polynomial terms are highly correlated with the original variables; centering removes much of the correlation without changing fitted values or sequential sums of squares; keep lower-order terms with higher-order ones; orthogonal polynomials avoid the problem.
- An interaction effect is represented by a product term; with a group indicator it means non-parallel lines, and the hypotheses "same line", "parallel lines" and "same intercept" are general linear tests.
