---
title: Model Selection and Diagnostics
description: Model building and validation, best subsets and stepwise selection, the criteria R², adjusted R², Mallows' Cp, AIC, BIC, PRESS and predicted R² with the leave-one-out identities, and the diagnostics of multiple regression, namely added-variable plots, studentized deleted residuals, leverage, DFFITS, Cook's distance, DFBETAS and variance inflation factors.
---

Faced with many candidate explanatory variables, how do we decide which to include? And once a model is chosen, how do we check it? This chapter answers both questions for multiple regression. The first half treats model selection: the overall strategy of model building and validation, the search over subsets of variables, and the criteria for comparing models, from $R^2$ and adjusted $R^2$ to Mallows' $C_p$, the information criteria AIC and BIC, and the PRESS statistic, all of which balance underfitting against overfitting. The second half extends the diagnostics of [3.3.5](/3.3.5) and [3.3.6](/3.3.6) to several explanatory variables: added-variable plots for the form of each variable, studentized deleted residuals for outlying responses, leverages for outlying values of the explanatory variables, DFFITS, Cook's distance and DFBETAS for influence, and variance inflation factors for the multicollinearity of [3.3.10](/3.3.10). The formulas for deleted residuals and Cook's distance used earlier are derived here from one identity for leaving out a single case. Remedial measures follow in [3.3.12](/3.3.12); shrinkage methods such as the **Lasso** are treated in [3.2.3](/3.2.3) and [3.4.7](/3.4.7).

## 11.1. What Is Model Selection

### 11.1.1. Building and Validating a Model

A regression model is usually built in four stages:

1. data collection and preparation;
2. reduction of the explanatory variables, using exploratory analysis and subject-matter knowledge;
3. model refinement and selection, including diagnostics and the possible addition of curvature and interaction terms;
4. model validation.

Validation evaluates the performance of the model and gives an unbiased estimate of its ability to generalize. The data used to fit the model and to estimate its parameters are the *training data*; ideally a separate data set (test or new data) is used to check the fitted model, for instance its predictive ability. When new data are not available, **cross-validation** ([3.4.10](/3.4.10)) splits the data into training and test parts: a single split, leave-one-out, or $K$-fold cross-validation, in which the data are divided into $K$ parts (say $K=5$ or $10$), each part serves once as the test set for the model fitted on the other $K-1$ parts, and the $K$ prediction errors are averaged.

**Definition 11.1.1 (Overfitting and Underfitting)** A model shows **overfitting** when it fits the training data much better than it predicts new data, because its many parameters adapt to the noise of the particular sample. A model shows **underfitting** when it is too simple to capture the systematic structure, for instance because it omits relevant explanatory variables, so that its predictions are biased.

A basic rule follows from [3.3.10](/3.3.10): the list of candidate explanatory variables must include all the variables that actually predict the response. Otherwise every selected model is underspecified, its coefficients are biased, and the analysis is misleading. Within that list, the aim is a reasonable and useful model, neither underfitted nor overfitted.

### 11.1.2. Routine Approaches

Selecting a "best" model that uses a subset of the available explanatory variables involves two decisions: how many explanatory variables to use (the subset size), and, given the size, which ones. There are three families of methods:

| family | idea | key methods |
|---|---|---|
| subset selection | keep or delete each variable entirely, searching for the best subset | best subsets regression; forward, backward and stepwise selection |
| regularization and shrinkage | penalize the size of the coefficients; selection happens indirectly when coefficients shrink to $0$ | **ridge regression** (shrinks only, suits multicollinearity); the Lasso (shrinks some coefficients exactly to $0$) |
| cross-validation | evaluate candidate models (or tuning parameters $\lambda$) by their prediction error on held-out data | **leave-one-out cross-validation** (small samples); $K$-fold cross-validation ($K=5$ or $10$) |

Subset selection and shrinkage propose candidates; criteria such as AIC, BIC and adjusted $R^2$, or cross-validation, act as the referee that chooses among them.

**Definition 11.1.2 (Best Subsets and Stepwise Regression)** With $P-1$ candidate explanatory variables there are $2^{P-1}$ models containing the intercept ($1024$ for $P-1=10$). **Best subsets regression** fits all of them (or uses an algorithm that finds the best ones without fitting all) and compares them by a criterion, reporting several good models of each size. **Stepwise regression** searches greedily instead: **forward selection** starts from the model with no variables and adds, at each step, the variable that improves the fit most, as long as its $t$- or $F$-test is significant at a preset level $\alpha_{\mathrm{enter}}$; **backward elimination** starts from the full model and deletes the least significant variable as long as its $p$-value exceeds $\alpha_{\mathrm{remove}}$; forward stepwise selection adds variables like forward selection but after each addition checks whether a variable already in the model has become redundant and removes it.

Best subsets regression is feasible for up to about $30$ or $40$ candidates and identifies several good models for final consideration; for larger numbers, automatic search ends with a single model. Stepwise results should not be overused or overstated:

- the final model is not guaranteed to be optimal in any specified sense;
- the procedure yields a single model, although there are often several equally good ones;
- without the researcher's knowledge it may be necessary to force important predictors into the model;
- the order in which variables enter should not be over-interpreted;
- many $t$-tests are performed, so the probability is high that some unimportant predictors are included or some important ones excluded.

Could we instead fit the full model with all candidates and keep the variables with significant coefficients? Not in general. The $t$-tests are variable-added-last tests, so correlated variables can all appear insignificant although together they matter (the body fat data of [3.3.9](/3.3.9)), and many tests are performed at once.

## 11.2. Selection Criteria

Throughout this section a candidate model has $p-1$ explanatory variables and $p$ parameters ($1\le p\le P$), with error sum of squares $\mathrm{SSE}_p$ and mean square $\mathrm{MSE}_p=\mathrm{SSE}_p/(n-p)$; the full model has all $P-1$ candidates.

### 11.2.1. R² and Adjusted R²

The **coefficient of determination** of [3.3.4](/3.3.4) and its adjusted version are

$$
R_p^2=1-\frac{\mathrm{SSE}_p}{\mathrm{SSTO}},\qquad R_{a,p}^2=1-\frac{n-1}{n-p}\cdot\frac{\mathrm{SSE}_p}{\mathrm{SSTO}}=1-\frac{\mathrm{MSE}_p}{\mathrm{SSTO}/(n-1)}.
$$
The full model always maximizes $R_p^2$ (minimizes $\mathrm{SSE}_p$), so $R_p^2$ cannot choose the size; one looks instead for the point where its increase slows down, which indicates that the further variables are unimportant. The adjusted $R_{a,p}^2$ accounts for the number of parameters: we may choose the model that maximizes $R_{a,p}^2$, equivalently minimizes $\mathrm{MSE}_p$.

### 11.2.2. Mallows' Cp

Let $\boldsymbol{\mu}=(\mu_1,\dots,\mu_n)^{\mathsf T}=\mathbb{E}(\boldsymbol{Y})$ be the true mean responses at the observed $X$ values. A candidate model with design matrix $X_p$ and hat matrix $H_p$ gives $\hat{\boldsymbol{Y}}_p=H_p\boldsymbol{Y}$, with $\mathbb{E}(\hat{\boldsymbol{Y}}_p)=H_p\boldsymbol{\mu}$ and $\operatorname{Cov}(\hat{\boldsymbol{Y}}_p)=\sigma^2H_p$. Its total mean squared error decomposes into squared bias and variance:

$$
\sum_{i=1}^n\mathbb{E}(\hat Y_{i,p}-\mu_i)^2=\sum_{i=1}^n\big(\mathbb{E}(\hat Y_{i,p})-\mu_i\big)^2+\sum_{i=1}^n\operatorname{Var}(\hat Y_{i,p}).
$$
Few variables give a large bias, many variables a large variance; the best model complexity minimizes the sum, the **bias–variance trade-off**.

**Theorem 11.2.1** Assume $\operatorname{Cov}(\boldsymbol{Y})=\sigma^2I_n$. The standardized total mean squared error of the candidate model is

$$
\Gamma_p=\frac{1}{\sigma^2}\sum_{i=1}^n\mathbb{E}(\hat Y_{i,p}-\mu_i)^2=\frac{\mathbb{E}(\mathrm{SSE}_p)}{\sigma^2}-(n-2p),
$$
and $\Gamma_p\ge p$, with equality if and only if the model is unbiased, $H_p\boldsymbol{\mu}=\boldsymbol{\mu}$.

**Proof** The variance part is $\operatorname{tr}\operatorname{Cov}(\hat{\boldsymbol{Y}}_p)=\sigma^2\operatorname{tr}(H_p)=p\sigma^2$. The bias part is $\|H_p\boldsymbol{\mu}-\boldsymbol{\mu}\|^2=\boldsymbol{\mu}^{\mathsf T}(I_n-H_p)\boldsymbol{\mu}$. For any random vector with mean $\boldsymbol{\mu}$ and covariance $\Sigma$, $\mathbb{E}(\boldsymbol{Y}^{\mathsf T}A\boldsymbol{Y})=\operatorname{tr}(A\Sigma)+\boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}$; with $A=I_n-H_p$ this gives $\mathbb{E}(\mathrm{SSE}_p)=(n-p)\sigma^2+\boldsymbol{\mu}^{\mathsf T}(I_n-H_p)\boldsymbol{\mu}$. Hence the bias part is $\mathbb{E}(\mathrm{SSE}_p)-(n-p)\sigma^2\ge0$, and $\sigma^2\Gamma_p=p\sigma^2+\mathbb{E}(\mathrm{SSE}_p)-(n-p)\sigma^2$. $\square$

If the full model contains all relevant variables, $\mathrm{MSE}_P$ is an unbiased estimator of $\sigma^2$, and replacing the unknowns by estimates gives a criterion.

**Definition 11.2.1 (Mallows' Cp)** **Mallows' Cp** of a candidate model is

$$
C_p=\hat\Gamma_p=\frac{\mathrm{SSE}_p}{\mathrm{MSE}_P}-(n-2p),
$$
where $\mathrm{MSE}_P$ is the mean squared error of the full model.

For the full model $C_P=P$ exactly. An unbiased model has $C_p\approx p$; among such models we prefer those with small $C_p$. A value $C_p\gg p$ indicates substantial bias, that is, missing relevant predictors; $C_p\ll p$ (possible because of sampling variability) may indicate overfitting. One plots $C_p$ against $p$ together with the line $C_p=p$ and looks for models near or below the line with small $C_p$.

![Mallows' Cp against the number of parameters p for all subsets of six simulated candidate predictors, of which three are relevant: models missing a relevant predictor lie far above the line Cp = p, models containing all three relevant predictors lie near the line, and the smallest Cp is attained by the true three-predictor model](./plots/mallows-cp.py)

### 11.2.3. AIC and BIC

The **Akaike information criterion** and the **Bayesian information criterion** (also called Schwarz's Bayesian criterion, SBC) were defined in [3.4.11](/3.4.11) for any likelihood model: $\mathrm{AIC}=-2\ln\hat L+2m$ and $\mathrm{BIC}=-2\ln\hat L+m\ln n$, where $\hat L$ is the maximized likelihood and $m$ the number of parameters. Both are to be minimized.

**Proposition 11.2.1** For the normal linear model with $p$ regression coefficients, up to an additive constant that is the same for all candidate models,

$$
\mathrm{AIC}_p=n\ln\frac{\mathrm{SSE}_p}{n}+2p,\qquad\mathrm{BIC}_p=n\ln\frac{\mathrm{SSE}_p}{n}+p\ln n.
$$

**Proof** The maximum likelihood estimate of $\sigma^2$ is $\hat\sigma^2=\mathrm{SSE}_p/n$, so $-2\ln\hat L=n\ln(2\pi)+n\ln\hat\sigma^2+\mathrm{SSE}_p/\hat\sigma^2=n\ln(2\pi)+n\ln(\mathrm{SSE}_p/n)+n$. The terms $n\ln(2\pi)+n$, and the penalty of the parameter $\sigma^2$ that every model has, do not depend on the model. $\square$

The first term rewards fit and the second penalizes complexity. Since $\ln n>2$ for $n\ge8$, BIC penalizes additional parameters more heavily than AIC and tends to choose smaller models. With $\sigma^2$ known, $-2\ln\hat L=\mathrm{SSE}_p/\sigma^2+\text{constant}$, so AIC and $C_p$ (with $\sigma^2$ in place of $\mathrm{MSE}_P$) differ only by a constant: for normal linear regression the two criteria are equivalent, and with $\sigma^2$ estimated they are close.

### 11.2.4. PRESS and Predicted R²

The criteria so far evaluate a model on the data used to fit it. The PRESS criterion instead predicts each case from the other cases, a form of leave-one-out cross-validation. Let $\boldsymbol{b}_{(-i)}$ be the least squares estimate computed without case $i$, from the design matrix $X_{(-i)}$ and response $\boldsymbol{Y}_{(-i)}$ with the $i$-th row deleted, and $\hat Y_{i(-i)}=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{b}_{(-i)}$ the resulting prediction of $Y_i$.

**Definition 11.2.2 (PRESS and Predicted R²)** The *prediction sum of squares* (**PRESS**) of a model is

$$
\mathrm{PRESS}_p=\sum_{i=1}^n\big(Y_i-\hat Y_{i(-i)}\big)^2,
$$
and the **predicted R²** is $R_{\mathrm{pred}}^2=1-\mathrm{PRESS}_p/\mathrm{SSTO}$. Models with small $\mathrm{PRESS}_p$ (large $R_{\mathrm{pred}}^2$) are preferred.

PRESS does not require $n$ refits. The key is the effect of deleting one case, which follows from the **Sherman–Morrison formula**: if $A$ and $A+B$ are invertible and $B$ has rank $1$, then with $g=\operatorname{tr}(BA^{-1})\ne-1$,

$$
(A+B)^{-1}=A^{-1}-\frac{1}{1+g}A^{-1}BA^{-1}.
$$

**Theorem 11.2.2 (Leave-One-Out Formulas)** Let $h_{ii}=\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i<1$ be the $i$-th diagonal entry of the hat matrix and $e_i=Y_i-\hat Y_i$ the $i$-th residual. Then

$$
\boldsymbol{b}-\boldsymbol{b}_{(-i)}=\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_ie_i}{1-h_{ii}},\qquad Y_i-\hat Y_{i(-i)}=\frac{e_i}{1-h_{ii}}.
$$
Consequently $\mathrm{PRESS}_p=\sum_{i=1}^n\big(e_i/(1-h_{ii})\big)^2$ is computed from a single fit.

**Proof** Deleting row $i$ gives $X_{(-i)}^{\mathsf T}X_{(-i)}=X^{\mathsf T}X-\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}$ and $X_{(-i)}^{\mathsf T}\boldsymbol{Y}_{(-i)}=X^{\mathsf T}\boldsymbol{Y}-\boldsymbol{x}_iY_i$. The Sherman–Morrison formula with $A=X^{\mathsf T}X$, $B=-\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}$ and $g=-h_{ii}$ gives

$$
\big(X_{(-i)}^{\mathsf T}X_{(-i)}\big)^{-1}=(X^{\mathsf T}X)^{-1}+\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}}{1-h_{ii}}.
$$
Multiplying by $X^{\mathsf T}\boldsymbol{Y}-\boldsymbol{x}_iY_i$ and using $\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}=\hat Y_i$,

$$
\boldsymbol{b}_{(-i)}=\boldsymbol{b}+\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i\hat Y_i}{1-h_{ii}}-(X^{\mathsf T}X)^{-1}\boldsymbol{x}_iY_i-\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_ih_{ii}Y_i}{1-h_{ii}}=\boldsymbol{b}+\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i}{1-h_{ii}}(\hat Y_i-Y_i).
$$
Finally $Y_i-\hat Y_{i(-i)}=\boldsymbol{x}_i^{\mathsf T}(\boldsymbol{b}-\boldsymbol{b}_{(-i)})+e_i=h_{ii}e_i/(1-h_{ii})+e_i=e_i/(1-h_{ii})$. $\square$

Since $0<1-h_{ii}\le1$, every leave-one-out error is at least as large in absolute value as the residual, so $\mathrm{PRESS}_p\ge\mathrm{SSE}_p$. With much noise in the model, $\mathrm{PRESS}_p>\mathrm{SSTO}$ is possible and $R_{\mathrm{pred}}^2$ is negative; the adjusted $R^2$ can also be negative, when $\mathrm{SSE}\approx\mathrm{SSTO}$. If $R_{\mathrm{pred}}^2\ll R^2$, the model is probably overfitted even if its variables are statistically significant. For instance, a cubic polynomial fitted to $12$ points with $R^2=0.66$ and $R_a^2=0.54$, every term significant at level $0.05$, had $R_{\mathrm{pred}}^2\approx0$: its curve passed close to a few extreme points and predicted them badly once they were left out.

### 11.2.5. Example: Surgical Unit

**Example 11.2.1 (Surgical Unit)** For $n=54$ patients undergoing a liver operation, the response is the survival time, and the candidate explanatory variables include the blood clotting score, a prognostic index, an enzyme function test score and a liver function test score (four further variables, age, gender and two indicators of alcohol use, are set aside here). Survival times are heavily right-skewed, and the logarithm lsurv reduces the long right tail and stabilizes the variance of the residuals, so it is used as the response. The correlations of lsurv with the four scores are $0.25$, $0.47$, $0.65$ and $0.65$; among the scores the largest correlation is $0.50$ (blood clotting and liver function).

Alcohol use has three categories (none, moderate, heavy). It enters the model through two indicator variables, alcmod and alcheavy, with "none" as the baseline. A single variable coded $-1,0,1$ or $1,2,3$ would force the three categories onto equally spaced positions and the effect to be linear in the code, while the indicators allow arbitrary differences between the categories.

```r
library(leaps)
predictors <- a1[, c("blood", "prog", "enz", "liver")]
leapSet <- leaps(x = predictors, y = a1$lsurv, nbest = 3, method = "Cp")
leapSet$which[which.min(leapSet$Cp), ]           # TRUE TRUE TRUE FALSE
fit <- lm(lsurv ~ blood + prog + enz, data = a1)
extractAIC(fit)                                  # n log(SSE/n) + 2p
extractAIC(fit, k = log(nrow(a1)))               # BIC
regsubsets(x = predictors, y = a1$lsurv, nbest = 3)   # also forward/backward
```

The three best models of each size are

| $p-1$ | variables | $R_p^2$ | $C_p$ | $\mathrm{AIC}_p$ | $\mathrm{BIC}_p$ |
|---|---|---|---|---|---|
| $1$ | enz | $0.428$ | $66.5$ | $-103.8$ | $-99.8$ |
| $1$ | liver | $0.422$ | $67.7$ | $-103.3$ | $-99.3$ |
| $1$ | prog | $0.221$ | $108.6$ | $-87.2$ | $-83.2$ |
| $2$ | prog, enz | $0.663$ | $20.5$ | $-130.5$ | $-124.5$ |
| $2$ | enz, liver | $0.600$ | $33.5$ | $-121.1$ | $-115.1$ |
| $2$ | blood, enz | $0.549$ | $43.9$ | $-114.7$ | $-108.7$ |
| $3$ | blood, prog, enz | $0.757$ | $3.4$ | $-146.2$ | $-138.2$ |
| $3$ | prog, enz, liver | $0.718$ | $11.4$ | $-138.0$ | $-130.1$ |
| $3$ | blood, enz, liver | $0.612$ | $32.9$ | $-120.8$ | $-112.9$ |
| $4$ | all four | $0.759$ | $5.0$ | $-144.6$ | $-134.6$ |

All three criteria choose blood, prog and enz: $C_p=3.4$ is close to $p=4$, and AIC and BIC are smallest; adding liver raises $R^2$ only from $0.757$ to $0.759$. (The `plot()` method of `regsubsets` with `scale = "Cp"` merely orders the models by $C_p$, whether the values are good or not.) When several models of the same size give approximately the same predictions, subject-matter knowledge should decide; if prediction is the key goal, the choice matters little. Different criteria often prefer different sets of predictors, so best subsets regression is best used as a screening tool.

## 11.3. Diagnostics for Multiple Regression

"When the effects of all known causes are estimated with exactness and subducted, the residual facts are constantly appearing in the form of phenomena altogether new" (John Herschel). The residual plots of [3.3.8](/3.3.8) remain the first check; multiple regression adds tools for the form of each explanatory variable, for outlying responses and explanatory values, for influential cases and for multicollinearity.

**Example 11.3.1 (Life Insurance)** For $n=18$ managers, $Y$ is the amount of life insurance carried, $X_1$ the average annual income and $X_2$ a risk aversion score. The first-order model gives $\hat Y=-205.72+6.288X_1+4.738X_2$, with $t=30.8$ and $3.44$, $R^2=0.986$ and $s=12.66$ on $15$ degrees of freedom. The usual residual plots show no gross problem at first sight; the tools below reveal more.

### 11.3.1. Added-Variable Plots

**Definition 11.3.1 (Added-Variable Plot)** The **added-variable plot** (partial regression plot) of $X_k$ plots the residuals $Y\mid X_{-k}$ of the regression of $Y$ on the other explanatory variables against the residuals $X_k\mid X_{-k}$ of the regression of $X_k$ on the other explanatory variables. There is one plot for each $X_k$ (`avPlots()` in the package car).

By the Frisch–Waugh–Lovell theorem of [3.3.9](/3.3.9), the least squares line through the plot has slope $b_k$ and residuals equal to those of the full model, and its $R^2$ is the coefficient of partial determination. The plot therefore shows the strength of the marginal relationship between $Y$ and $X_k$ in the full model, and it can reveal a nonlinear relationship, nonconstant variance and outliers, all after adjustment for the other variables. Residual plots against each $X_k$ are also useful, but they do not adjust the response for the other variables.

![Added-variable plots for simulated life-insurance data in which the true effect of income is quadratic: the plot for income shows clear curvature around the fitted line, while the plot for risk aversion shows a linear trend with scatter](./plots/added-variable-plots.py)

In Example 11.3.1 the added-variable plot of income shows a curvilinear relationship, and so does the plot of the residuals against income. Adding the term $X_1^2$ reduces $\mathrm{SSE}$ from $2405.15$ to $75.06$ ($F^*=434.6$ on $(1,14)$ degrees of freedom): the model needs curvature in income.

### 11.3.2. Outlying Responses: Studentized Deleted Residuals

The residuals $\boldsymbol{e}=(I_n-H)\boldsymbol{Y}$ have $\operatorname{Cov}(\boldsymbol{e})=\sigma^2(I_n-H)$, so $\operatorname{Var}(e_i)=\sigma^2(1-h_{ii})$: residuals have unequal variances, smaller at cases with large $h_{ii}$.

**Definition 11.3.2 (Studentized and Deleted Residuals)** The internally **studentized residual** is $e_i^*=e_i/\sqrt{\mathrm{MSE}(1-h_{ii})}$. The **deleted residual** is $d_i=Y_i-\hat Y_{i(-i)}$, the error in predicting $Y_i$ from the fit without case $i$, and the **studentized deleted residual** (externally studentized residual) is

$$
t_i=\frac{d_i}{s(d_i)}=\frac{e_i}{\sqrt{\mathrm{MSE}_{(-i)}(1-h_{ii})}},
$$
where $\mathrm{MSE}_{(-i)}$ is the mean squared error of the fit without case $i$ and $s^2(d_i)=\mathrm{MSE}_{(-i)}/(1-h_{ii})$.

By Theorem 11.2.2, $d_i=e_i/(1-h_{ii})$, so $\operatorname{Var}(d_i)=\sigma^2/(1-h_{ii})$, which gives the second expression for $t_i$. Equivalently $1/(1-h_{ii})=1+\boldsymbol{x}_i^{\mathsf T}\big(X_{(-i)}^{\mathsf T}X_{(-i)}\big)^{-1}\boldsymbol{x}_i$ (multiply the Sherman–Morrison expression of $\big(X_{(-i)}^{\mathsf T}X_{(-i)}\big)^{-1}$ by $\boldsymbol{x}_i$ on both sides), so $t_i=\big(Y_i-\hat Y_{i(-i)}\big)\big/\sqrt{\mathrm{MSE}_{(-i)}\big(1+\boldsymbol{x}_i^{\mathsf T}(X_{(-i)}^{\mathsf T}X_{(-i)})^{-1}\boldsymbol{x}_i\big)}$ is the standardized error of predicting a new observation at $\boldsymbol{x}_i$ from the other $n-1$ cases ([3.3.8](/3.3.8)).

**Theorem 11.3.1** Under the normal linear model,

$$
(n-p)\,\mathrm{MSE}=(n-p-1)\,\mathrm{MSE}_{(-i)}+\frac{e_i^2}{1-h_{ii}},
$$
so $t_i=e_i\Big(\dfrac{n-p-1}{\mathrm{SSE}(1-h_{ii})-e_i^2}\Big)^{1/2}$ can be computed from a single fit, and $t_i\sim t_{n-p-1}$.

**Proof** Add to the model the indicator $\boldsymbol{u}_i$ of case $i$ (the $i$-th standard basis vector of $\mathbb{R}^n$), $\boldsymbol{Y}=X\boldsymbol{\beta}+\gamma\boldsymbol{u}_i+\boldsymbol{\varepsilon}$. This mean-shift model fits case $i$ exactly, so its error sum of squares is that of the other $n-1$ cases, $(n-p-1)\mathrm{MSE}_{(-i)}$, and $\hat\gamma=Y_i-\hat Y_{i(-i)}=d_i$. As in the proof of Proposition 9.2.1 of [3.3.9](/3.3.9), with $\tilde{\boldsymbol{u}}=(I_n-H)\boldsymbol{u}_i$ we have $\tilde{\boldsymbol{u}}^{\mathsf T}\tilde{\boldsymbol{u}}=1-h_{ii}$ and $\tilde{\boldsymbol{u}}^{\mathsf T}\boldsymbol{Y}=e_i$, so the extra sum of squares of $\boldsymbol{u}_i$ is $e_i^2/(1-h_{ii})$, which is the identity. Moreover $t_i$ is exactly the $t$-statistic of $\hat\gamma$ in the mean-shift model, which has $n-p-1$ error degrees of freedom; if case $i$ follows the model, $\gamma=0$ and $t_i\sim t_{n-p-1}$ by Theorem 8.2.2 of [3.3.8](/3.3.8). $\square$

Adding a case increases $\mathrm{SSE}$, unlike adding a variable, which decreases it. To test for outliers, declare case $i$ to have an outlying $Y$ value if $\lvert t_i\rvert>t_{n-p-1,\alpha/(2n)}$. Since all $n$ cases are tested, this uses the **Bonferroni correction**.

In Example 11.3.1, `rstudent()` gives the largest value $t_7=2.75$ (and `stdres()` of MASS $e_7^*=2.29$). The Bonferroni critical value is $t_{14,0.05/36}=3.62$; `outlierTest()` of car reports the unadjusted $p$-value $0.016$ and the Bonferroni $p$-value $0.28$: no case is a significant outlier in $Y$.

Outliers are not necessarily bad observations. If they are correct, they may be the most informative points in the data: in exponential growth data, the last two observations may look like outliers from a straight line while in fact they reveal the true form of the growth. Deleting inconvenient points to protect a theory, or defining outliers as the responses one does not like, is bad practice.

### 11.3.3. Outlying Explanatory Values: Leverage

**Definition 11.3.3 (Leverage)** The **leverage** of case $i$ is the diagonal entry $h_{ii}=\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i$ of the **hat matrix**; since $\hat Y_i=h_{i1}Y_1+\cdots+h_{ii}Y_i+\cdots+h_{in}Y_n$, it is the weight of $Y_i$ in its own fitted value.

The leverages satisfy $0\le h_{ii}\le1$ and $\sum_{i=1}^nh_{ii}=\operatorname{tr}(H)=\operatorname{rank}(H)=p$, so their mean is $\bar h=p/n$. With an intercept in the model,

$$
h_{ii}=\frac1n+(\tilde{\boldsymbol{x}}_i)^{\mathsf T}(\tilde X^{\mathsf T}\tilde X)^{-1}\tilde{\boldsymbol{x}}_i,
$$
where $\tilde X$ is the matrix of centered explanatory variables and $\tilde{\boldsymbol{x}}_i^{\mathsf T}$ its $i$-th row: $h_{ii}$ measures the distance of the $X$ values of case $i$ from their means, in the metric of their sample covariance matrix. A case is usually declared to have extreme $X$ values when $h_{ii}>2p/n$; leverages between $0.2$ and $0.5$ are moderate and leverages above $0.5$ high. The same quantity $\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h$ at a new point detects hidden extrapolation ([3.3.8](/3.3.8)): if it is well beyond the range of the leverages of the data, the prediction at $\boldsymbol{x}_h$ is an extrapolation.

In Example 11.3.1, $2p/n=6/18=0.33$; `hatvalues()` gives $h_{77}=0.62$, a high leverage, and $h_{66}=0.35$, just above the cutoff. All other leverages are below $0.30$.

### 11.3.4. Influential Cases

A case is *influential* if its removal causes a major change in the fitted regression. An outlier in $Y$ with small leverage, or a high-leverage case that follows the pattern of the others, need not be influential; a case with both a large residual and a high leverage usually is. Three measures quantify influence on different parts of the fit.

**Definition 11.3.4 (DFFITS, Cook's Distance, DFBETAS)** For case $i$,

1. the **DFFITS** is the studentized difference of the fitted value of case $i$ with and without case $i$,

$$
(\mathrm{DFFITS})_i=\frac{\hat Y_i-\hat Y_{i(-i)}}{\sqrt{\mathrm{MSE}_{(-i)}h_{ii}}};
$$
2. **Cook's distance** is the aggregate change of all $n$ fitted values,

$$
D_i=\frac{\big\|X(\boldsymbol{b}-\boldsymbol{b}_{(-i)})\big\|^2}{p\,\mathrm{MSE}}=\frac{\sum_{j=1}^n\big(\hat Y_j-\hat Y_{j(-i)}\big)^2}{p\,\mathrm{MSE}};
$$
3. the **DFBETAS** measure the change of each coefficient, $(\mathrm{DFBETAS})_{k(-i)}=\dfrac{b_k-b_{k(-i)}}{\sqrt{\mathrm{MSE}_{(-i)}c_{kk}}}$, $k=0,1,\dots,p-1$, where $c_{kk}=[(X^{\mathsf T}X)^{-1}]_{kk}$, so that $\operatorname{Var}(b_k)=\sigma^2c_{kk}$.

The name Cook's distance comes from the confidence region for $\boldsymbol{\beta}$. Since $(\boldsymbol{b}-\boldsymbol{\beta})^{\mathsf T}X^{\mathsf T}X(\boldsymbol{b}-\boldsymbol{\beta})/\sigma^2\sim\chi^2_p$, a $100(1-\alpha)\%$ confidence ellipsoid ([3.2.4](/3.2.4)) is $\big\{\boldsymbol{\beta}\in\mathbb{R}^p\colon\|X(\boldsymbol{\beta}-\boldsymbol{b})\|^2/(p\,\mathrm{MSE})\le F_{p,n-p,\alpha}\big\}$, centered at $\boldsymbol{b}$ with axes given by the eigenvectors and eigenvalues of $X^{\mathsf T}X$. Cook (1977) measures the influence of case $i$ by the same distance between $\boldsymbol{b}$ and $\boldsymbol{b}_{(-i)}$.

**Proposition 11.3.1** In terms of the residual, the leverage and $t_i$,

$$
(\mathrm{DFFITS})_i=t_i\sqrt{\frac{h_{ii}}{1-h_{ii}}},\qquad D_i=\frac{e_i^2}{p\,\mathrm{MSE}}\cdot\frac{h_{ii}}{(1-h_{ii})^2}=\frac{(e_i^*)^2}{p}\cdot\frac{h_{ii}}{1-h_{ii}}.
$$

**Proof** By Theorem 11.2.2, $\hat Y_i-\hat Y_{i(-i)}=\boldsymbol{x}_i^{\mathsf T}(\boldsymbol{b}-\boldsymbol{b}_{(-i)})=h_{ii}e_i/(1-h_{ii})$; dividing by $\sqrt{\mathrm{MSE}_{(-i)}h_{ii}}$ gives $\frac{e_i}{\sqrt{\mathrm{MSE}_{(-i)}(1-h_{ii})}}\sqrt{\frac{h_{ii}}{1-h_{ii}}}$. For Cook's distance, $\|X(\boldsymbol{b}-\boldsymbol{b}_{(-i)})\|^2=\frac{e_i^2}{(1-h_{ii})^2}\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}X(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i=\frac{e_i^2h_{ii}}{(1-h_{ii})^2}$. $\square$

The formulas show that influence combines a large residual with a high leverage. The usual guidelines are:

| measure | what it measures | case considered influential if |
|---|---|---|
| $(\mathrm{DFFITS})_i$ | change of its own fitted value | $\lvert\mathrm{DFFITS}\rvert>1$ (small to medium data), $>2\sqrt{p/n}$ (large data) |
| $D_i$ | change of all fitted values | $D_i>4/n$; or by the percentile $\nu=\mathbb{P}(F_{p,n-p}<D_i)$: little influence if $\nu<20\%$, substantial if $\nu\ge50\%$ |
| $(\mathrm{DFBETAS})_{k(-i)}$ | change of each coefficient | $\lvert\mathrm{DFBETAS}\rvert>1$ (small to medium data), $>2/\sqrt{n}$ (large data) |

![Influence diagnostics for simulated data with one case that has both an extreme X value and a large residual: the scatter plot shows that the fitted line changes markedly when this case is deleted, and the index plot of Cook's distances singles it out far above the cutoff 4/n](./plots/influence-diagnostics.py)

```r
round(hatvalues(lmfit1), 4)          # leverages h_ii
round(rstudent(lmfit1), 4)           # studentized deleted residuals t_i
round(cooks.distance(lmfit1), 4)     # Cook's distances D_i
dfbetas(lmfit1)                      # DFBETAS for every case and coefficient
plot(lmfit1, which = 4)              # index plot of Cook's distances
plot(lmfit1, which = 5)              # residuals against leverage with Cook contours
```

In Example 11.3.1, case 7 has $D_7=2.89$, at the $93$rd percentile of $F_{3,15}$, far above all other cases (the next largest are $0.35$ and $0.20$); its DFFITS is $2.75\sqrt{0.62/0.38}=3.53$, and its DFBETAS are $2.66$ for income and $-2.68$ for risk aversion. Case 7 is highly influential, although it is not an outlier by the Bonferroni test.

What should be done with outlying and influential cases once they are identified? They should be examined to determine *why* they are outlying or influential. Based on this examination, appropriate actions include correcting errors in the data, deleting or down-weighting the cases (robust regression, [3.3.12](/3.3.12)), transforming the data, considering a different model (here, adding curvature in income), and redesigning the experiment or the sample survey to collect more data.

### 11.3.5. Multicollinearity: Variance Inflation Factors

The pairwise correlations of [3.3.10](/3.3.10) can miss multicollinearity that involves several variables. A direct measure is how well each explanatory variable is explained by the others.

**Definition 11.3.5 (Variance Inflation Factor)** Let $R_k^2$ be the coefficient of determination of the regression of $X_k$ on the other $p-2$ explanatory variables. The **variance inflation factor** of $X_k$ is $(\mathrm{VIF})_k=(1-R_k^2)^{-1}$ and its **tolerance** is $\mathrm{TOL}_k=1-R_k^2=1/(\mathrm{VIF})_k$.

**Theorem 11.3.2** In the standardized regression model of [3.3.9](/3.3.9), $\operatorname{Var}(b_k^*)=\sigma^{*2}(\mathrm{VIF})_k$, where $\sigma^{*2}$ is the error variance of that model; in the original model,

$$
\operatorname{Var}(b_k)=\frac{\sigma^2}{\sum_i(X_{ik}-\bar X_k)^2}\cdot(\mathrm{VIF})_k.
$$

**Proof** $\operatorname{Cov}(\boldsymbol{b}^*)=\sigma^{*2}r_{XX}^{-1}$, so we need $[r_{XX}^{-1}]_{kk}$; take $k=1$ and partition $r_{XX}=\begin{bmatrix}1&\boldsymbol{r}_{1,-1}^{\mathsf T}\\\boldsymbol{r}_{1,-1}&r_{-1,-1}\end{bmatrix}$, where $r_{-1,-1}$ is the correlation matrix of $X_2,\dots,X_{p-1}$ and $\boldsymbol{r}_{1,-1}$ their correlations with $X_1$. By the block inversion formula with the **Schur complement**,

$$
[r_{XX}^{-1}]_{11}=\big(1-\boldsymbol{r}_{1,-1}^{\mathsf T}r_{-1,-1}^{-1}\boldsymbol{r}_{1,-1}\big)^{-1}.
$$
In the standardized regression of $X_1^*$ on $X_2^*,\dots,X_{p-1}^*$ the coefficients are $\boldsymbol{\beta}_{1,-1}=r_{-1,-1}^{-1}\boldsymbol{r}_{1,-1}$, the total sum of squares is $1$ and the regression sum of squares is $\boldsymbol{\beta}_{1,-1}^{\mathsf T}r_{-1,-1}\boldsymbol{\beta}_{1,-1}=\boldsymbol{r}_{1,-1}^{\mathsf T}r_{-1,-1}^{-1}\boldsymbol{r}_{1,-1}$, which is therefore $R_1^2$. Hence $[r_{XX}^{-1}]_{11}=(1-R_1^2)^{-1}$. The second formula follows by $b_k=(s_Y/s_k)b_k^*$ and $\sigma^{*2}=\sigma^2/\big((n-1)s_Y^2\big)$. $\square$

So $(\mathrm{VIF})_k$ is exactly the factor by which collinearity inflates the variance of $b_k$ compared with an orthogonal design (Proposition 10.1.1 of [3.3.10](/3.3.10)). With $\overline{\mathrm{VIF}}=\sum_{k=1}^{p-1}(\mathrm{VIF})_k/(p-1)$, multicollinearity is considered excessive when the largest $\mathrm{VIF}$ exceeds $10$ or the average $\mathrm{VIF}$ is considerably larger than $1$. In Example 11.3.1, `vif()` of car gives $1.07$ for both income and risk aversion: no problem. For the body fat data the VIFs are $709$ (skinfold), $564$ (thigh) and $105$ (midarm), confirming the severe multicollinearity of [3.3.10](/3.3.10) ($R^2=0.990$ for midarm on the other two).

## Summary

| criterion | formula | choose |
|---|---|---|
| $R_p^2$ | $1-\mathrm{SSE}_p/\mathrm{SSTO}$ | where its increase levels off |
| $R_{a,p}^2$ | $1-\frac{n-1}{n-p}\cdot\frac{\mathrm{SSE}_p}{\mathrm{SSTO}}$ | maximum (minimum $\mathrm{MSE}_p$) |
| Mallows' $C_p$ | $\mathrm{SSE}_p/\mathrm{MSE}_P-(n-2p)$ | small, with $C_p\approx p$ |
| $\mathrm{AIC}_p$, $\mathrm{BIC}_p$ | $n\ln(\mathrm{SSE}_p/n)+2p$, $+p\ln n$ | minimum |
| $\mathrm{PRESS}_p$, $R_{\mathrm{pred}}^2$ | $\sum_i\big(e_i/(1-h_{ii})\big)^2$, $1-\mathrm{PRESS}_p/\mathrm{SSTO}$ | minimum PRESS; beware $R_{\mathrm{pred}}^2\ll R^2$ |

| problem | diagnostic | rule of thumb |
|---|---|---|
| form of $X_k$ | added-variable plot | curvature, unequal spread, outliers |
| outlying $Y$ | $t_i=e_i/\sqrt{\mathrm{MSE}_{(-i)}(1-h_{ii})}\sim t_{n-p-1}$ | $\lvert t_i\rvert>t_{n-p-1,\alpha/(2n)}$ |
| outlying $X$ | $h_{ii}$ | $h_{ii}>2p/n$; $>0.5$ high |
| influence | DFFITS, Cook's $D_i$, DFBETAS | $>1$ (or $2\sqrt{p/n}$), $>4/n$, $>1$ (or $2/\sqrt n$) |
| multicollinearity | $(\mathrm{VIF})_k=(1-R_k^2)^{-1}$ | largest $>10$ |

- Model building: include all relevant candidates, select by best subsets or stepwise search, judge with criteria or cross-validation, validate on new or held-out data; avoid both underfitting (bias) and overfitting (variance).
- One identity drives the leave-one-out diagnostics: $\boldsymbol{b}-\boldsymbol{b}_{(-i)}=(X^{\mathsf T}X)^{-1}\boldsymbol{x}_ie_i/(1-h_{ii})$ and $Y_i-\hat Y_{i(-i)}=e_i/(1-h_{ii})$.
