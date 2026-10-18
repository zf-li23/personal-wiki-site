---
title: Remedial Measures and Single-Factor Analysis of Variance
description: Weighted and generalized least squares for unequal error variances; ridge regression, the Lasso and the elastic net for multicollinearity; robust and nonparametric regression; the bootstrap; and the cell means and factor effects models of one-way analysis of variance.
---

This chapter has two parts. The first completes the toolbox of remedial measures begun in [3.3.6](/3.3.6): when the diagnostics of [3.3.5](/3.3.5) and [3.3.11](/3.3.11) show unequal error variances, **multicollinearity**, influential cases or a nonlinear relation, we can change the estimator instead of the model. Weighted least squares restores efficiency under **heteroscedasticity**; ridge regression and its relatives trade a little bias for a large reduction in variance; robust and nonparametric regression weaken the assumptions; and the bootstrap assesses the precision of estimators whose sampling distribution is hard to derive. The second part begins the analysis of variance with one categorical explanatory variable. It is still a linear model, with **design matrix** built from indicator variables, so everything we know about regression applies; it also prepares the experimental design of [3.8](/3.8). The inference for these models follows in [3.3.13](/3.3.13), and two factors in [3.3.14](/3.3.14).

## 12.1. Remedial Measures

The diagnostics of the previous chapters can be summarized as a checklist. Check the normality of the **residuals** with a **normal Q–Q plot** or a histogram; plot the residuals against the fitted values, against each predictor and, when appropriate, against time or space, looking for curvature and for a changing spread; examine the partial regression plots. Then look for cases that are extreme on the influence measures (studentized deleted residuals, the diagonal elements of the **hat matrix**, DFFITS, **Cook's distance** and DFBETAS), and examine the tolerance (or the **variance inflation factor**) of each predictor: predictors with low tolerance call for recoding or for variable selection. This section collects the remedies for the problems found in this way.

### 12.1.1. Unequal Error Variances: Weighted Least Squares

Consider the model $Y_i=\beta_0+\beta_1X_{i,1}+\cdots+\beta_{p-1}X_{i,p-1}+\varepsilon_i$ with independent $\varepsilon_i\sim\mathcal{N}(0,\sigma_i^2)$. If $\sigma_i^2=\sigma^2$ for all $i$, maximizing the **likelihood function** $L=f_1f_2\cdots f_n$ is ordinary least squares. If the variances differ but are known, the density of $Y_i$ is

$$
f_i=\frac{1}{\sqrt{2\pi}\,\sigma_i}\exp\left[-\frac12\left(\frac{Y_i-\beta_0-\beta_1X_{i,1}-\cdots-\beta_{p-1}X_{i,p-1}}{\sigma_i}\right)^2\right],
$$
and maximizing $L$ over the $\beta$'s is equivalent to minimizing

$$
\sum_{i=1}^n\left(\frac{Y_i-\beta_0-\beta_1X_{i,1}-\cdots-\beta_{p-1}X_{i,p-1}}{\sigma_i}\right)^2.
$$
Each case is weighted by the inverse of its variance: precise observations count more.

**Remark 12.1.1** What happens if we ignore the heteroscedasticity and use the OLS estimator $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ anyway? Write $\operatorname{Cov}(\boldsymbol{Y})=\Sigma\ne\sigma^2I_n$. The estimator is still unbiased, since $\mathbb{E}\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}X\boldsymbol{\beta}=\boldsymbol{\beta}$ uses only $\mathbb{E}\boldsymbol{\varepsilon}=\boldsymbol{0}$; but its covariance matrix becomes

$$
\operatorname{Cov}(\boldsymbol{b})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\Sigma X(X^{\mathsf T}X)^{-1},
$$
which is no longer $\sigma^2(X^{\mathsf T}X)^{-1}$. The usual standard errors are therefore wrong, and the **Gauss–Markov theorem**, whose proof needs $\Sigma=\sigma^2I_n$, no longer applies: $\boldsymbol{b}$ is unbiased but in general not of minimum variance (Proposition 12.1.1 exhibits the best linear unbiased estimator). In practice the prediction intervals of OLS then have coverage below or above the nominal level, depending on where the new case lies.

**Definition 12.1.1 (White Estimator)** The **White estimator** (also called the heteroscedasticity-consistent or sandwich estimator) of $\operatorname{Cov}(\boldsymbol{b})$ replaces the unknown $\Sigma$ by the diagonal matrix of squared residuals:

$$
\widehat{\operatorname{Cov}}(\boldsymbol{b})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\hat\Sigma X(X^{\mathsf T}X)^{-1},\qquad \hat\Sigma=\operatorname{diag}(e_1^2,\dots,e_n^2).
$$

The White estimator keeps the OLS coefficients and only corrects their standard errors; it is consistent under heteroscedasticity of unknown form. It does not help with prediction intervals: $\operatorname{Var}(Y_h-\hat Y_h)=\boldsymbol{X}_h^{\mathsf T}\operatorname{Cov}(\boldsymbol{b})\boldsymbol{X}_h+\sigma_h^2$ requires an estimate of the error variance $\sigma_h^2$ at the new case $\boldsymbol{X}_h$, that is, a model for how the variance depends on the predictors. This is what weighted least squares provides.

**Definition 12.1.2 (Weighted Least Squares)** Given weights $w_i>0$, the **weighted least squares** (WLS) estimator $\boldsymbol{b}_{\mathrm{w}}$ minimizes the weighted residual sum of squares

$$
Q_{\mathrm{w}}(\boldsymbol{\beta})=\sum_{i=1}^nw_i\,(Y_i-\boldsymbol{X}_i^{\mathsf T}\boldsymbol{\beta})^2=(\boldsymbol{Y}-X\boldsymbol{\beta})^{\mathsf T}W(\boldsymbol{Y}-X\boldsymbol{\beta}),\qquad W=\operatorname{diag}(w_1,\dots,w_n),
$$
where $\boldsymbol{X}_i^{\mathsf T}$ is the $i$-th row of $X$. The weights need not sum to $1$.

**Proposition 12.1.1** Suppose $\operatorname{Cov}(\boldsymbol{\varepsilon})=\Sigma=\operatorname{diag}(\sigma_1^2,\dots,\sigma_n^2)$ with known $\sigma_i^2$, and take $w_i=1/\sigma_i^2$, that is, $W=\Sigma^{-1}$. Then

$$
\boldsymbol{b}_{\mathrm{w}}=(X^{\mathsf T}WX)^{-1}X^{\mathsf T}W\boldsymbol{Y},\qquad \operatorname{Cov}(\boldsymbol{b}_{\mathrm{w}})=(X^{\mathsf T}WX)^{-1},
$$
and $\boldsymbol{b}_{\mathrm{w}}$ is the best linear unbiased estimator of $\boldsymbol{\beta}$.

**Proof** Multiply the model by $W^{1/2}=\operatorname{diag}(1/\sigma_1,\dots,1/\sigma_n)$:

$$
\underbrace{W^{1/2}\boldsymbol{Y}}_{\boldsymbol{Y}^*}=\underbrace{W^{1/2}X}_{X^*}\boldsymbol{\beta}+\underbrace{W^{1/2}\boldsymbol{\varepsilon}}_{\boldsymbol{\varepsilon}^*},\qquad \operatorname{Cov}(\boldsymbol{\varepsilon}^*)=W^{1/2}\Sigma W^{1/2}=I_n.
$$
The transformed model satisfies the Gauss–Markov assumptions with $\sigma^2=1$, and $Q_{\mathrm{w}}(\boldsymbol{\beta})=\|\boldsymbol{Y}^*-X^*\boldsymbol{\beta}\|^2$. Hence its OLS estimator $(X^{*\mathsf T}X^*)^{-1}X^{*\mathsf T}\boldsymbol{Y}^*=(X^{\mathsf T}WX)^{-1}X^{\mathsf T}W\boldsymbol{Y}$ is the best linear unbiased estimator, with covariance matrix $(X^{*\mathsf T}X^*)^{-1}=(X^{\mathsf T}WX)^{-1}$. A linear estimator of $\boldsymbol\beta$ based on $\boldsymbol{Y}$ is also linear in $\boldsymbol{Y}^*$, so the optimality carries over. $\square$

In words: the optimal weights are inversely proportional to the variances, $w_i=k/\sigma_i^2$, and then $\operatorname{Var}(\sqrt{w_i}\,Y_i)=k$ for every case. Computing $\boldsymbol{b}_{\mathrm{w}}$ is easy (the `weights` argument of `lm()`); the practical problem is to determine the weights. Three situations arise.

1. Variances known: use $w_i=1/\sigma_i^2$ as in Proposition 12.1.1.
2. Only relative magnitudes known: if the ratios $\sigma_i^2/\sigma_j^2$ are known, for example $\sigma_i^2$ proportional to $X_i$ or to $X_i^2$, write $\sigma_i^2=k/w_i$ with known $w_i$ and unknown proportionality constant $k$. Then $\operatorname{Cov}(W^{1/2}\boldsymbol{Y})=kI_n$, the estimator $\boldsymbol{b}_{\mathrm{w}}$ is unchanged, $\operatorname{Cov}(\boldsymbol{b}_{\mathrm{w}})=k(X^{\mathsf T}WX)^{-1}$, and $k$ is estimated by the error mean square of the transformed model,

$$
\hat k=\mathrm{MSE}_{\mathrm{w}}=\frac{\sum_i(Y_i^*-\hat Y_i^*)^2}{n-p}=\frac{\sum_iw_i(Y_i-\hat Y_i)^2}{n-p}=\frac{\sum_iw_ie_i^2}{n-p}.
$$
3. Variances completely unknown: (a) if there are replicates or near replicates (cases with equal or similar predictor values), estimate the variance within each group by the **sample variance** $s_i^2$ and use $w_i=1/s_i^2$ for all cases in the group. (b) Otherwise use two-stage estimation: fit OLS, then regress the absolute residuals $\lvert e_i\rvert$ on the predictors to model the standard deviation (or the squared residuals $e_i^2$ to model the variance); the fitted values $\hat\sigma_i$ (or $\hat\sigma_i^2$) give the weights $w_i=1/\hat\sigma_i^2$, and WLS is fitted with them. If the coefficients change substantially, the two steps can be iterated with the residuals of the WLS fit until $\boldsymbol{b}_{\mathrm{w}}$ stabilizes; this is a form of *iteratively reweighted least squares*.

The absolute residuals are usually preferred to the squared ones in step (b): they are less affected by outlying cases, and their regression on the predictors estimates the standard deviation, whose dependence on $X$ is often closer to linear.

**Example 12.1.1** In a study of 54 healthy adult women aged 20 to 60, $Y$ is the diastolic blood pressure and $X$ the age. The scatter plot shows a strong linear relation without skewness, but the spread of $Y$ grows with age.

```r
a1 <- read.table("CH11TA01.txt")
colnames(a1) <- c("age", "diast")
fit <- lm(diast ~ age, data = a1)            # OLS
a1$absr <- abs(fit$residuals)
fit2 <- lm(absr ~ age, data = a1)            # model the standard deviation
a1$shat <- predict(fit2)                     # estimated sigma_i
a1$wt <- 1 / a1$shat^2                       # weights w_i = 1 / sigma_i^2
fit3 <- lm(diast ~ age, weights = wt, data = a1)   # WLS
summary(fit3)
```

| | OLS | WLS |
|---|---|---|
| intercept (s.e.) | $56.157\ (3.994)$ | $55.566\ (2.521)$ |
| slope for age (s.e.) | $0.580\ (0.0970)$ | $0.596\ (0.0792)$ |
| $t$ for the slope | $5.98$ | $7.53$ |
| residual standard error on 52 d.f. | $8.146$ | $1.213$ |
| $R^2$ | $0.408$ | $0.521$ |

The estimates barely change, as expected of two unbiased estimators, but the standard error of the age coefficient drops from $0.097$ to $0.079$.

![Left: the OLS and WLS lines for simulated data whose spread grows with X. Right: the absolute OLS residuals against X with the fitted line used to estimate the standard deviation of each case.](./plots/weighted-least-squares.py)

**Remark 12.1.2** Two numbers in the WLS output must not be read as in OLS. The residual standard error $1.213$ is $\sqrt{\mathrm{MSE}_{\mathrm{w}}}$, an estimate of $\sqrt{k}$ on the weighted scale, not of the error standard deviation of $Y$; it is smaller here only because of how the weights happen to be scaled (multiplying all weights by $c$ multiplies it by $\sqrt c$), so it is not an advantage of WLS. Likewise $R^2$ has no clear-cut meaning for weighted least squares. The gain of WLS is the smaller standard error of the coefficients and correct prediction intervals.

WLS handles a diagonal $\Sigma$. When the errors are also correlated (for example in time series or in clustered data, see [3.3.5](/3.3.5)), the same idea uses the full covariance matrix.

**Definition 12.1.3 (Generalized Least Squares)** In the model $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ with $\mathbb{E}[\boldsymbol{\varepsilon}\mid X]=\boldsymbol{0}$ and $\operatorname{Cov}(\boldsymbol{\varepsilon}\mid X)=\Omega$ positive definite, the **generalized least squares** (GLS) estimator minimizes the squared Mahalanobis length of the residual vector:

$$
\hat{\boldsymbol{\beta}}_{\mathrm{GLS}}=\arg\min_{\boldsymbol{\beta}}(\boldsymbol{Y}-X\boldsymbol{\beta})^{\mathsf T}\Omega^{-1}(\boldsymbol{Y}-X\boldsymbol{\beta})=(X^{\mathsf T}\Omega^{-1}X)^{-1}X^{\mathsf T}\Omega^{-1}\boldsymbol{Y}.
$$

GLS is OLS applied to linearly transformed data: with the **Cholesky decomposition** $\Omega=CC^{\mathsf T}$, the model $C^{-1}\boldsymbol{Y}=C^{-1}X\boldsymbol{\beta}+C^{-1}\boldsymbol{\varepsilon}$ has $\operatorname{Cov}(C^{-1}\boldsymbol{\varepsilon})=I_n$, so the proof of Proposition 12.1.1 shows that GLS is the best linear unbiased estimator. WLS is the special case of a diagonal $\Omega$.

### 12.1.2. Multicollinearity: Ridge Regression

When the predictors are nearly linearly dependent (**multicollinearity**, [3.3.10](/3.3.10)), $X^{\mathsf T}X$ is close to singular and $(X^{\mathsf T}X)^{-1}$ has huge entries, so the OLS coefficients have huge variances. A natural fix is to invert $X^{\mathsf T}X+\lambda I$ instead, for some $\lambda>0$. This is Tikhonov regularization of an ill-posed problem; in statistics it was proposed by A. E. Hoerl (1962) and developed by Hoerl and Kennard (1970) as ridge regression, and in machine learning it is called weight decay. The estimators become biased but much more stable, and the method works even when $p\gg n$.

**Definition 12.1.4 (Ridge Regression)** For $\lambda>0$, the **ridge regression** estimator is the minimizer of the penalized residual sum of squares

$$
Q(\boldsymbol{\beta})=(\boldsymbol{Y}-X\boldsymbol{\beta})^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol{\beta})+\lambda\sum_j\beta_j^2,\qquad \boldsymbol{b}^{R}(\lambda)=(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$
The predictors are standardized first, and the intercept is not penalized.

The closed form follows from $\partial Q/\partial\boldsymbol{\beta}=-2X^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol{\beta})+2\lambda\boldsymbol{\beta}=\boldsymbol{0}$, that is, $(X^{\mathsf T}X+\lambda I)\boldsymbol{\beta}=X^{\mathsf T}\boldsymbol{Y}$; the matrix $X^{\mathsf T}X+\lambda I$ is a **positive definite matrix** for every $\lambda>0$. Standardization matters because the penalty treats all coefficients alike, so they must be on a common scale.

**Proposition 12.1.2** Let $X^{\mathsf T}X$ be invertible, with **spectral decomposition** $X^{\mathsf T}X=V\operatorname{diag}(d_1,\dots,d_p)V^{\mathsf T}$, $d_j>0$, and let $\boldsymbol{b}$ be the OLS estimator. Then for $\lambda>0$:

1. (Constrained form) $\boldsymbol{b}^R(\lambda)$ minimizes $(\boldsymbol{Y}-X\boldsymbol{\beta})^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol{\beta})$ subject to $\sum_j\beta_j^2\le c$, where $c=\|\boldsymbol{b}^R(\lambda)\|^2$.
2. (Shrinkage) $\boldsymbol{b}^R(\lambda)=(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}X\,\boldsymbol{b}$, so in the coordinates $V^{\mathsf T}\boldsymbol\beta$ each component of $\boldsymbol{b}$ is multiplied by $d_j/(d_j+\lambda)<1$; in particular $\|\boldsymbol{b}^R(\lambda)\|$ decreases in $\lambda$ and tends to $0$ as $\lambda\to\infty$.
3. (Bias and variance) $\mathbb{E}\boldsymbol{b}^R(\lambda)=(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}X\boldsymbol{\beta}\ne\boldsymbol{\beta}$ in general, and

$$
\operatorname{Cov}(\boldsymbol{b}^R(\lambda))=\sigma^2(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}X(X^{\mathsf T}X+\lambda I)^{-1}=\sigma^2V\operatorname{diag}\Big(\frac{d_j}{(d_j+\lambda)^2}\Big)V^{\mathsf T},
$$
which is smaller than $\operatorname{Cov}(\boldsymbol{b})=\sigma^2V\operatorname{diag}(1/d_j)V^{\mathsf T}$ in the sense that the difference is positive definite.

**Proof** 1. If $\sum_j\beta_j^2\le c$, then $Q(\boldsymbol\beta)\ge Q(\boldsymbol{b}^R)$ gives $\|\boldsymbol{Y}-X\boldsymbol\beta\|^2\ge\|\boldsymbol{Y}-X\boldsymbol{b}^R\|^2+\lambda(c-\|\boldsymbol\beta\|^2)\ge\|\boldsymbol{Y}-X\boldsymbol{b}^R\|^2$. This is the Lagrange multiplier argument: $\lambda$ is the multiplier of the constraint. 2. Substitute $X^{\mathsf T}\boldsymbol{Y}=X^{\mathsf T}X\boldsymbol{b}$ and diagonalize. 3. Take expectations and covariances in 2; the eigenvalues of the difference are $\sigma^2\big[1/d_j-d_j/(d_j+\lambda)^2\big]=\sigma^2\lambda(2d_j+\lambda)/[d_j(d_j+\lambda)^2]>0$. $\square$

So both the length and the variance of the coefficient vector shrink as $\lambda$ grows, and the directions with small $d_j$, in which the data carry little information and OLS is most unstable, are shrunk the most. The price is a bias that grows with $\lambda$. Hoerl and Kennard showed that there is always some $\lambda>0$ for which the total **mean squared error** $\mathbb{E}\|\boldsymbol{b}^R(\lambda)-\boldsymbol{\beta}\|^2$ is smaller than that of OLS: a **bias–variance trade-off**. In practice $\lambda$ is chosen by **cross-validation** (or generalized cross-validation) or by inspecting the *ridge trace*, the plot of the coefficients against $\lambda$, and taking the smallest $\lambda$ at which they stabilize.

![Left: ridge trace of three standardized coefficients for simulated collinear predictors. Right: squared bias, variance and their sum, the mean squared error of the ridge estimator, as functions of lambda; the dashed line is the mean squared error of OLS.](./plots/ridge-trace-bias-variance.py)

**Example 12.1.2** For the body fat data of [3.3.9](/3.3.9) and [3.3.10](/3.3.10), with three highly correlated predictors, `lm.ridge` in the package `MASS` standardizes the predictors and computes the ridge path.

```r
library(MASS)
fits <- lm.ridge(fat ~ skinfold + thigh + midarm,
                 lambda = seq(0, 0.1, 0.001), data = b1)
plot(fits)                                 # ridge trace
whichIsBest <- which.min(fits$GCV)         # generalized cross-validation
coef(fits)[whichIsBest, ]
```

| $\lambda$ | intercept | skinfold | thigh | midarm |
|---|---|---|---|---|
| $0$ (OLS) | $117.08$ | $4.334$ | $-2.857$ | $-2.186$ |
| $0.019$ | $43.84$ | $2.117$ | $-0.960$ | $-1.018$ |

The coefficients chosen by generalized cross-validation are much smaller and of more plausible size; the least efficiently estimated coefficients shrink the fastest.

Why penalize the size of the coefficients? A large coefficient puts much emphasis on one feature. When a polynomial of increasing degree is fitted to a fixed set of points, the residual sum of squares keeps decreasing while the coefficients explode in size and alternate in sign: the fit models intricate relations that belong to the particular training data, which is **overfitting**. Bounding $\sum_j\beta_j^2$ rules such fits out.

**Example 12.1.3** Suppose software can only compute OLS, $(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$. To obtain the ridge estimator, augment the data with $p$ pseudo-observations:

$$
X^*=\begin{bmatrix}X\\ \sqrt\lambda\,I_p\end{bmatrix},\qquad \boldsymbol{Y}^*=\begin{bmatrix}\boldsymbol{Y}\\ \boldsymbol{0}_p\end{bmatrix}.
$$
Then $(\boldsymbol{Y}^*-X^*\boldsymbol\beta)^{\mathsf T}(\boldsymbol{Y}^*-X^*\boldsymbol\beta)=(\boldsymbol{Y}-X\boldsymbol\beta)^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol\beta)+\lambda\boldsymbol\beta^{\mathsf T}\boldsymbol\beta$, and $X^*$ has full column **rank**, so OLS on $(X^*,\boldsymbol{Y}^*)$ is well defined and equals $(X^{*\mathsf T}X^*)^{-1}X^{*\mathsf T}\boldsymbol{Y}^*=(X^{\mathsf T}X+\lambda I_p)^{-1}X^{\mathsf T}\boldsymbol{Y}$.

### 12.1.3. The Lasso and the Elastic Net

Ridge regression shrinks all coefficients but sets none of them to zero, so it does not select variables. Replacing the squared penalty by the absolute value changes this.

**Definition 12.1.5 (Lasso)** Let $Z$ be the matrix of standardized predictors. The **Lasso** (least absolute shrinkage and selection operator, R. Tibshirani, 1996) minimizes

$$
(\boldsymbol{Y}-Z\boldsymbol{\beta})^{\mathsf T}(\boldsymbol{Y}-Z\boldsymbol{\beta})+\lambda\sum_j\lvert\beta_j\rvert,\qquad\lambda>0;
$$
ridge regression is the same problem with $\lambda\sum_j\beta_j^2$.

In the constrained form the Lasso minimizes the residual sum of squares over the diamond $\sum_j\lvert\beta_j\rvert\le c$ instead of the ball $\sum_j\beta_j^2\le c$. The elliptical contours of the residual sum of squares typically first touch the diamond at a corner, where some coordinates are exactly zero, so the Lasso performs shrinkage and variable selection at the same time. There is no closed form; the solution path is computed by coordinate descent or by the LARS algorithm.

![Elliptical contours of the residual sum of squares around the OLS estimate and the constraint regions of ridge regression (disk) and the Lasso (diamond); the Lasso solution lies on a corner, where one coefficient is exactly zero.](./plots/ridge-lasso-geometry.py)

**Definition 12.1.6 (Elastic Net)** The **elastic net** (H. Zou and T. Hastie, 2005) combines both penalties:

$$
\hat{\boldsymbol{\beta}}=\arg\min_{\boldsymbol{\beta}}\Big\{\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\lambda_1\|\boldsymbol{\beta}\|_1+\lambda_2\|\boldsymbol{\beta}\|_2^2\Big\},\qquad\lambda_1,\lambda_2\ge0.
$$

The elastic net deals simultaneously with **multicollinearity** (through the $\ell_2$ part, which makes it keep or drop groups of correlated predictors together) and with variable selection (through the $\ell_1$ part). The two tuning parameters are chosen by cross-validation over a grid of combinations. The package `glmnet` parametrizes the penalty by an overall strength $\lambda$ and a mixing parameter $\alpha\in[0,1]$ and minimizes

$$
\frac{1}{2n}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\lambda\Big[\alpha\|\boldsymbol{\beta}\|_1+\frac{1-\alpha}{2}\|\boldsymbol{\beta}\|_2^2\Big],
$$
so that $\alpha=1$ is the Lasso, $\alpha=0$ ridge regression and $\alpha\in(0,1)$ the elastic net.

```r
library(glmnet)
# x: matrix of predictors, y: response; glmnet standardizes x by default
fit <- glmnet(x, y, alpha = 1)             # Lasso path over a grid of lambda
cvfit <- cv.glmnet(x, y, alpha = 0.5)      # elastic net, lambda chosen by 10-fold CV
coef(cvfit, s = "lambda.min")
```

**Remark 12.1.3** The penalties have a Bayesian interpretation ([3.2.7](/3.2.7)). With normal errors, OLS is the maximum likelihood estimator: $\hat{\boldsymbol\beta}_{\mathrm{OLS}}=\arg\min_{\boldsymbol\beta}\|\boldsymbol{Y}-X\boldsymbol\beta\|^2$ maximizes the density of $\boldsymbol{Y}$ given $(\boldsymbol\beta,\sigma^2)$. A frequentist treats $\boldsymbol\beta$ as an unknown constant, so point estimation is an optimization problem; a Bayesian treats $\boldsymbol\beta$ as random with a **prior distribution** $\pi(\boldsymbol\beta)$, and the **posterior distribution** is $\pi(\boldsymbol\beta\mid\boldsymbol{Y})\propto f(\boldsymbol{Y}\mid\boldsymbol\beta)\,\pi(\boldsymbol\beta)$. The **maximum a posteriori estimate** is its mode,

$$
\hat{\boldsymbol\beta}_{\mathrm{MAP}}=\arg\max_{\boldsymbol\beta}\pi(\boldsymbol\beta\mid\boldsymbol{Y})=\arg\min_{\boldsymbol\beta}\Big\{\frac{1}{2\sigma^2}\|\boldsymbol{Y}-X\boldsymbol\beta\|^2-\log\pi(\boldsymbol\beta)\Big\}.
$$
If the $\beta_j$ are independent $\mathcal{N}(0,\tau^2)$, then $-\log\pi(\boldsymbol\beta)=\|\boldsymbol\beta\|^2/(2\tau^2)+\text{const}$ and the MAP estimate is the ridge estimator with $\lambda=\sigma^2/\tau^2$; if they are independent Laplace (double exponential) with density $\frac{1}{2s}\mathrm{e}^{-\lvert\beta\rvert/s}$, it is the Lasso with $\lambda=2\sigma^2/s$.

### 12.1.4. Influential Cases: Robust Regression

Least squares is very sensitive to outlying cases, because the squared residuals give them large influence. The basic idea of *robust regression* is a fitting procedure that is not sensitive to outlying cases. Instead of minimizing the sum of squared residuals, one can minimize

- the sum of absolute residuals $\sum_i\lvert Y_i-\boldsymbol{X}_i^{\mathsf T}\boldsymbol\beta\rvert$: *least absolute deviations* (LAD, also called least absolute residuals, LAR), which is median regression;
- the median of the squared residuals: *least median of squares* (LMS), which tolerates almost half of the cases being outliers.

A third approach is iteratively reweighted least squares (IRLS): a weighted regression whose weights are computed from the residuals of the previous fit, so that cases with large scaled residuals receive small weights (for example Huber or bisquare weights), repeated until the coefficients converge. The price of robustness is extensive computation, and robust fits should be compared with the least squares fit rather than replacing the study of the outlying cases.

### 12.1.5. Nonlinearity: Nonparametric Regression and Regression Trees

When no simple parametric form fits the regression function, *nonparametric regression* estimates $\mathbb{E}[Y\mid X=x]$ directly; there are several versions, with an interesting theory ([3.6](/3.6)), and all of them have a smoothing or penalty parameter that balances bias and variance.

- Local polynomial regression fits a low-degree polynomial by weighted least squares in a moving neighborhood of each $x$. In R, `lowess` (locally weighted scatterplot smoother) handles simple regression and `loess` (local regression) the general case; the smooth curves added to the residual plots of the earlier chapters are of this kind.
- Smoothing splines minimize $\sum_i(Y_i-f(X_i))^2+\lambda\int f''(x)^2\,\mathrm{d}x$ over all smooth $f$; in R, `smooth.spline` handles simple regression.
- *Regression trees*, the standard approach in machine learning, partition the predictor space into rectangles by repeatedly splitting the data into nodes according to a single predictor; the predicted value in each rectangle is the mean of the responses in it.

### 12.1.6. Evaluating Estimators: The Bootstrap

For complex estimators (the ridge coefficients for a $\lambda$ chosen from the data, a robust fit, a ratio of coefficients) the sampling distribution is difficult to derive. The *bootstrap* (B. Efron, 1979) approximates it by resampling: sample with replacement from the data, refit the model to each resample, and use the resulting distribution of the quantity of interest to estimate its precision. Resampling from the observations amounts to replacing the unknown distribution by the **empirical distribution function** ([3.1.7](/3.1.7)). For regression models there are two versions.

**Algorithm 12.1.1 (Case Resampling)** 1. Draw $n$ cases $(\boldsymbol{X}_i,Y_i)$ with replacement from the original sample to obtain a bootstrap sample. 2. Fit OLS to it to obtain $\hat{\boldsymbol\beta}^*_b$. 3. Repeat for $b=1,\dots,B$ and use the $\hat{\boldsymbol\beta}^*_b$ in the usual manner to construct bootstrap standard errors and confidence intervals for the coefficients (for example the sample standard deviation of the $\hat\beta^*_{b,j}$, or their $\alpha/2$ and $1-\alpha/2$ quantiles).

**Algorithm 12.1.2 (Residual Resampling)** 1. Fit OLS to the original sample to obtain the fitted values $\hat Y_i$ and residuals $e_i$. 2. Draw residuals $e_{b1}^{*},\dots,e_{bn}^{*}$ with replacement from $e_1,\dots,e_n$ and form $Y^*_{bi}=\hat Y_i+e_{bi}^{*}$. 3. Regress the $Y^*_{bi}$ on the fixed $\boldsymbol{X}_i$ to obtain $\hat{\boldsymbol\beta}^*_b$. 4. Repeat for $b=1,\dots,B$ and proceed as in Algorithm 12.1.1.

**Remark 12.1.4** Which version is more reasonable depends on the situation. Residual resampling keeps the design fixed and assumes that the errors are exchangeable, so it is appropriate when the predictors are fixed by design and the model, including constant variance, is adequate; it is also the natural choice when there are few cases. Case resampling treats $(\boldsymbol{X}_i,Y_i)$ as a random sample from a joint distribution; it remains valid under heteroscedasticity and when the regression function is misspecified, at the cost of a varying design. Both are developed further in statistical computing ([3.5](/3.5)).

## 12.2. Single-Factor Analysis of Variance

### 12.2.1. Concepts

In the **analysis of variance** (ANOVA) the response variable $Y$ is continuous, as in regression, but the explanatory variable is categorical (qualitative or discrete).

**Definition 12.2.1 (Factor)** A categorical explanatory variable is called a **factor**, and its $r$ possible values are the **factor levels**. The levels are often called groups or treatments; in a single-factor (one-way) study each level defines a population of responses.

We write $Y_{ij}$ for the $j$-th observation at level $i$ of the factor, $i=1,\dots,r$, $j=1,\dots,n_i$; the sample sizes $n_i$ need not be equal, and $n_T=\sum_in_i$ is the total number of observations. ANOVA focuses on the mean responses at the different factor levels, and the analysis usually proceeds in two steps:

1. determine whether or not the factor level means are all the same;
2. if they differ, examine how they differ and what the implications of the differences are.

With $r=2$ levels, step 1 is the pooled two-sample **t-test** ([3.2.5](/3.2.5)); one-way ANOVA generalizes it to $r$ groups.

ANOVA is regression. The difference is in what the models attend to: regression models are concerned with the statistical relation between one or more quantitative predictors and the response, $\mathbb{E}Y=f(X)$, whereas ANOVA does not consider the quantitative differences between the levels of $X$ (the levels may have no natural order at all) or their statistical relation to $\mathbb{E}Y$; it only compares the means. Coding the levels by indicator variables turns an ANOVA model into a linear regression model, which is how we fit it.

### 12.2.2. The Cell Means Model

The ANOVA model assumes that:

1. the response has a mean that may depend on the level of the factor;
2. the responses at each factor level are a random sample from the corresponding probability distribution, independent of the responses at the other levels;
3. each of these distributions is normal;
4. all of them have the same variance.

**Definition 12.2.2 (Cell Means Model)** A "cell" is a level of the factor. The **cell means model** is

$$
Y_{ij}=\mu_i+\varepsilon_{ij},\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),\qquad i=1,\dots,r,\quad j=1,\dots,n_i,
$$
where $\mu_i$ is the theoretical mean (expected value) of all observations at level $i$. Equivalently, the $Y_{ij}\sim\mathcal{N}(\mu_i,\sigma^2)$ are independent.

The parameters are $\mu_1,\dots,\mu_r$ and $\sigma^2$. The question "does the explanatory variable help explain $Y$?" becomes "do the $\mu_i$ vary?", that is,

$$
H_0\colon\mu_1=\mu_2=\cdots=\mu_r\ (=\mu,\text{ a constant})\qquad\text{versus}\qquad H_1\colon\text{not all }\mu_i\text{ are equal}.
$$

**Theorem 12.2.1** Write $\bar Y_{i\cdot}=\sum_{j=1}^{n_i}Y_{ij}/n_i$ for the sample mean at level $i$ and $s_i^2=\sum_{j=1}^{n_i}(Y_{ij}-\bar Y_{i\cdot})^2/(n_i-1)$ for the sample variance. In the cell means model the least squares (and maximum likelihood) estimator of $\mu_i$ is $\hat\mu_i=\bar Y_{i\cdot}$, and the unbiased pooled estimator of $\sigma^2$ is

$$
s^2=\frac{\sum_i(n_i-1)s_i^2}{\sum_i(n_i-1)}=\frac{\sum_i(n_i-1)s_i^2}{n_T-r}=\mathrm{MSE}.
$$

**Proof** The sum of squares $\sum_i\sum_j(Y_{ij}-\mu_i)^2$ separates into $r$ sums, the $i$-th of which involves only $\mu_i$ and is minimized by the sample mean. Each $s_i^2$ is unbiased for $\sigma^2$, so any weighted average of them is; the weights $n_i-1$ give $s^2=\sum_i\sum_j(Y_{ij}-\bar Y_{i\cdot})^2/(n_T-r)$, the error mean square of the fitted regression. $\square$

As in the pooled $t$-test, the $s_i^2$ are pooled with weights proportional to their degrees of freedom $n_i-1$; they are not simply averaged unless all $n_i$ are equal.

Let $\bar Y_{\cdot\cdot}=\sum_i\sum_jY_{ij}/n_T$ be the overall sample mean; when all $n_i=n$, $\bar Y_{\cdot\cdot}=\sum_i\bar Y_{i\cdot}/r$. The total variation splits as in regression ([3.3.4](/3.3.4)):

$$
\underbrace{\sum_{i,j}(Y_{ij}-\bar Y_{\cdot\cdot})^2}_{\mathrm{SSTO}}=\underbrace{\sum_in_i(\bar Y_{i\cdot}-\bar Y_{\cdot\cdot})^2}_{\mathrm{SSTR}}+\underbrace{\sum_{i,j}(Y_{ij}-\bar Y_{i\cdot})^2}_{\mathrm{SSE}},
$$
because the cross term $2\sum_i(\bar Y_{i\cdot}-\bar Y_{\cdot\cdot})\sum_j(Y_{ij}-\bar Y_{i\cdot})$ vanishes. $\mathrm{SSTR}$ is the *treatment sum of squares* (the regression or model sum of squares $\mathrm{SSR}$ of the regression formulation), the variation of the level means around the overall mean; $\mathrm{SSE}$ is the error (residual) sum of squares, the variation within the levels.

| Source | df | SS | MS |
|---|---|---|---|
| Treatments (model) | $r-1$ | $\mathrm{SSTR}=\sum_in_i(\bar Y_{i\cdot}-\bar Y_{\cdot\cdot})^2$ | $\mathrm{MSTR}=\mathrm{SSTR}/(r-1)$ |
| Error | $n_T-r$ | $\mathrm{SSE}=\sum_{i,j}(Y_{ij}-\bar Y_{i\cdot})^2$ | $\mathrm{MSE}=\mathrm{SSE}/(n_T-r)$ |
| Total | $n_T-1$ | $\mathrm{SSTO}=\sum_{i,j}(Y_{ij}-\bar Y_{\cdot\cdot})^2$ | |

**Theorem 12.2.2 (Expected Mean Squares)** In the cell means model,

$$
\mathbb{E}[\mathrm{MSE}]=\sigma^2,\qquad \mathbb{E}[\mathrm{MSTR}]=\sigma^2+\frac{\sum_in_i(\mu_i-\mu_\cdot)^2}{r-1},\qquad \mu_\cdot=\frac{\sum_in_i\mu_i}{n_T}.
$$

**Proof** The first identity is Theorem 12.2.1. For the second, $\bar Y_{i\cdot}-\bar Y_{\cdot\cdot}$ has mean $\mu_i-\mu_\cdot$, and $\mathbb{E}[\mathrm{SSTR}]=\sum_in_i(\mu_i-\mu_\cdot)^2+\mathbb{E}\big[\sum_in_i(\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot\cdot})^2\big]$. The last expectation is $\sum_in_i\mathbb{E}\bar\varepsilon_{i\cdot}^2-n_T\mathbb{E}\bar\varepsilon_{\cdot\cdot}^2=\sum_in_i\frac{\sigma^2}{n_i}-n_T\frac{\sigma^2}{n_T}=(r-1)\sigma^2$. $\square$

So $\mathbb{E}[\mathrm{MSTR}]>\mathbb{E}[\mathrm{MSE}]$ exactly when the level means differ, which suggests comparing the two mean squares. In more complicated models the expected mean squares tell us which ratio to use for each **F-test**.

**Theorem 12.2.3 (ANOVA F-Test)** Under $H_0\colon\mu_1=\cdots=\mu_r$,

$$
F^*=\frac{\mathrm{MSTR}}{\mathrm{MSE}}\sim F_{r-1,\,n_T-r}.
$$
The level-$\alpha$ test rejects $H_0$ when $F^*>F_{r-1,n_T-r,\alpha}$; one usually reports the **p-value** $\mathbb{P}(F_{r-1,n_T-r}>F^*)$.

**Proof** This is the overall $F$-test of the regression formulation below: $\mathrm{SSE}/\sigma^2\sim\chi^2_{n_T-r}$ always, and under $H_0$, $\mathrm{SSTR}/\sigma^2\sim\chi^2_{r-1}$ independently of $\mathrm{SSE}$, since the $\bar Y_{i\cdot}$ are independent of the $s_i^2$ ([3.2.2](/3.2.2)). $\square$

To fit the cell means model by regression, use one indicator variable per level: the $i$-th explanatory variable equals $1$ if the observation is from group $i$ and $0$ otherwise. Each row of the design matrix then has a single $1$, in the column of its group,

$$
X=\begin{bmatrix}1&0&\cdots&0\\0&1&\cdots&0\\\vdots&&\ddots&\vdots\\0&0&\cdots&1\end{bmatrix}\ \begin{matrix}\text{group }1\\\text{group }2\\\vdots\\\text{group }r\end{matrix},\qquad \boldsymbol\beta=(\mu_1,\dots,\mu_r)^{\mathsf T},
$$
with no intercept column: the $r$ indicators already sum to the column of ones. The design matrices and their estimates are worked out in [3.3.13](/3.3.13).

### 12.2.3. The Factor Effects Model

**Definition 12.2.3 (Factor Effects Model)** The **factor effects model** is the reparametrization of the cell means model

$$
Y_{ij}=\mu+\tau_i+\varepsilon_{ij},\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
where $\mu$ is a constant common to all observations, defined to fit the purpose of the study, and $\tau_i=\mu_i-\mu$ is the $i$-th **factor level effect**, or **treatment effect**, a constant for each factor level.

The two models describe the same family of distributions, $\mu_i=\mu+\tau_i$, but the factor effects form is the more useful way of looking at more complicated models (two factors and their interaction in [3.3.14](/3.3.14)), and the null hypotheses are easier to state: "no factor effect" is $\tau_1=\cdots=\tau_r=0$. Because it has one parameter more than there are means, the factor effects model needs a constraint on the $\tau_i$; this, and the choice of $\mu$, are the subject of the next chapter.

## Summary {#summary}

- Under unequal error variances OLS remains unbiased but loses efficiency and gives wrong standard errors. The White estimator corrects the standard errors; weighted least squares with $w_i\propto1/\sigma_i^2$ is the best linear unbiased estimator, and in practice the weights are estimated from replicates or by regressing the absolute residuals on the predictors. Generalized least squares extends this to correlated errors.
- Ridge regression, $(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}\boldsymbol{Y}$, shrinks the coefficients and their variances at the price of bias; the Lasso also sets coefficients to zero, and the elastic net combines both. They are MAP estimates under normal and Laplace priors.
- Robust regression (LAD, LMS, IRLS) limits the influence of outlying cases; nonparametric regression and regression trees relax the form of the regression function; the bootstrap estimates precision by resampling cases or residuals.
- One-way ANOVA compares the means of $r$ factor levels in the cell means model $Y_{ij}=\mu_i+\varepsilon_{ij}$ or the factor effects model $Y_{ij}=\mu+\tau_i+\varepsilon_{ij}$; $\hat\mu_i=\bar Y_{i\cdot}$, $\mathrm{SSTO}=\mathrm{SSTR}+\mathrm{SSE}$, and $H_0\colon\mu_1=\cdots=\mu_r$ is tested by $F^*=\mathrm{MSTR}/\mathrm{MSE}\sim F_{r-1,n_T-r}$.
