---
title: Linear Regression Models
description: The classical linear regression model from the multivariate point of view, least squares and its geometry as an orthogonal projection, properties under the Gauss–Markov and normal assumptions with t- and F-inference and prediction intervals, and regularization by ridge regression, principal component regression and the Lasso.
---

Many questions in statistics and machine learning ask how a response depends on several covariates: how next year's earnings depend on age, education and past earnings, or how a child's height depends on the parents' heights. The linear regression model is the simplest non-trivial answer, and it is a natural part of a multivariate course because everything about it is matrix algebra: the least squares fit is an **orthogonal projection** onto the column space of the **design matrix**, its distribution follows from the **multivariate normal distribution** of [3.4.2](/3.4.2), and the tests for groups of coefficients are quadratic forms of the same kind as Hotelling's $T^2$ in [3.4.3](/3.4.3). The chapter first sets up the model and the least squares estimator, then studies its properties under three increasingly strong sets of assumptions (none, the Gauss–Markov model, normal errors), and finally turns to the case of many covariates, where ridge regression, principal component regression (built on the **principal component analysis** of [3.4.5](/3.4.5)) and the **Lasso** trade a little bias for much less variance. The estimation theory overlaps with [3.2.3](/3.2.3) and the tests with [3.2.5](/3.2.5); model diagnostics, variable selection and the general linear model are developed in the linear regression course [3.3](/3.3).

## 7.1. The Classical Linear Regression Model

### 7.1.1. Responses and Covariates

The data consist of $n$ units, each with a response and $p$ covariates. The *response* (outcome) is $Y$; the *covariates* (predictors) are $X_1,\dots,X_p$, collected in $\boldsymbol{X}=(X_1,\dots,X_p)^{\mathsf T}$. Two questions are asked of such data:

- *description*: how is $Y$ associated with $\boldsymbol{X}$ (how is height related to weight, or income to education and experience)?
- *prediction*: given a new covariate vector $\boldsymbol{x}^*$, what response $Y^*$ should we expect?

We assume that the $n$ observations $(\boldsymbol{x}_i,y_i)$ are iid, that $p$ is fixed, and that the covariates are treated as given (conditioning on them is not crucial for what follows). Every response can be decomposed as its conditional mean plus an error,

$$
Y=\mathbb{E}(Y\mid\boldsymbol{X}=\boldsymbol{x})+\varepsilon=g(\boldsymbol{x})+\varepsilon,\qquad\mathbb{E}(\varepsilon\mid\boldsymbol{X}=\boldsymbol{x})=0,
$$

where $g$ is the regression function; the **conditional expectation** is the **best predictor** of $Y$ from $\boldsymbol{X}$ in mean square ([3.1.9](/3.1.9)). A linear model restricts $g$ to a linear function, $g(x)=a+bx$ for one covariate.

Linear models are a good starting point for several reasons: they are simple but not trivial; explicit formulas, based on elegant algebra and geometry, give insight; they can capture nonlinearity by including nonlinear transformations of the covariates; they are often good approximations of nonlinear data-generating processes; and, although simpler, they do not necessarily predict worse than complicated nonlinear models.

**Example 7.1.1 (One Covariate)** To predict next year's earnings $y$ of a person of age $x$ from data $(x_i,y_i)$, $i=1,\dots,n$, take

$$
y_i=a+bx_i+\varepsilon_i,\quad i=1,\dots,n,\qquad\text{or}\qquad\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},\qquad\boldsymbol{Y}=\begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix},\quad X=\begin{bmatrix}1&x_1\\\vdots&\vdots\\1&x_n\end{bmatrix},\quad\boldsymbol{\beta}=\begin{bmatrix}a\\b\end{bmatrix}.
$$

**Example 7.1.2 (Two Populations)** Let $x_i=1$ if person $i$ took a job-training program and $x_i=0$ otherwise, and fit the same model $y_i=a+bx_i+\varepsilon_i$. With $\mathbb{E}\varepsilon_i=0$, the mean earnings are $\mu_1=a$ without training and $\mu_2=a+b$ with training, so testing $H_0\colon\mu_1=\mu_2$ is the same as testing $H_0\colon b=0$. Sorting the units by group, the design matrix has a first column of ones and a second column of $n_1$ zeros followed by $n_2$ ones; the $t$-test of $b=0$ in this regression is exactly the pooled two-sample $t$-test of [3.2.5](/3.2.5).

**Example 7.1.3 (A Quadratic Trend)** If earnings first rise and then fall with age, take $y_i=a+bx_i+cx_i^2+\varepsilon_i$, which is again $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ with rows $(1,x_i,x_i^2)$ in $X$ and $\boldsymbol{\beta}=(a,b,c)^{\mathsf T}$. The design matrix may contain polynomials or any other nonlinear transformations of the original covariates: in statistics, "linear" means linear in the parameters, not linear in the covariates.

### 7.1.2. Least Squares Estimation

Which line fits the data best? Gauss proposed to minimize the sum of squared vertical deviations. For one covariate, the *ordinary least squares* (OLS) estimator is

$$
(\hat\alpha,\hat\beta)=\arg\min_{a,b}\frac1n\sum_{i=1}^n(y_i-a-bx_i)^2.
$$

Setting the two partial derivatives to zero gives

$$
\frac1n\sum_{i=1}^n(y_i-\hat\alpha-\hat\beta x_i)=0\ \Longrightarrow\ \bar y=\hat\alpha+\hat\beta\bar x,\qquad\frac1n\sum_{i=1}^nx_i(y_i-\hat\alpha-\hat\beta x_i)=0\ \Longrightarrow\ \overline{xy}=\hat\alpha\bar x+\hat\beta\,\overline{x^2},
$$

and eliminating $\hat\alpha$ yields $\overline{xy}-\bar x\bar y=\hat\beta(\overline{x^2}-\bar x^2)$, that is, $\hat\sigma_{xy}=\hat\beta\hat\sigma_x^2$. Hence

$$
\hat\beta=\frac{\hat\sigma_{xy}}{\hat\sigma_x^2},\qquad\hat\alpha=\bar y-\hat\beta\bar x,
$$

where $\hat\sigma_{xy}=\frac1n\sum_i(x_i-\bar x)(y_i-\bar y)$ and $\hat\sigma_x^2=\frac1n\sum_i(x_i-\bar x)^2$.

The fitted line has a revealing form in terms of the sample **correlation coefficient** $\hat\rho_{xy}=\hat\sigma_{xy}/(\hat\sigma_x\hat\sigma_y)$:

$$
\hat y_i-\bar y=\frac{\hat\sigma_{xy}}{\hat\sigma_x^2}(x_i-\bar x)=\frac{\hat\rho_{xy}\hat\sigma_x\hat\sigma_y}{\hat\sigma_x^2}(x_i-\bar x)\quad\Longrightarrow\quad\frac{\hat y_i-\bar y}{\hat\sigma_y}=\hat\rho_{xy}\,\frac{x_i-\bar x}{\hat\sigma_x}.
$$

In standard units the slope is the correlation, and since $\lvert\hat\rho_{xy}\rvert\le1$ the prediction is closer to the mean than the covariate ("regression toward the mean", Galton's original observation). This is the sample version of the **best linear predictor** of [3.1.10](/3.1.10): the slope $\rho\sqrt{\operatorname{Var}(Y)}/\sqrt{\operatorname{Var}(X)}$ minimizes $\mathbb{E}[(Y-\mathbb{E}Y)-b(X-\mathbb{E}X)]^2$ over $b\in\mathbb{R}$. Regression therefore reflects correlation, not causation.

For several covariates we let the first covariate be the constant $1$ (an intercept) and keep writing $p$ for the total number of columns. The data are

$$
\boldsymbol{Y}=\begin{bmatrix}y_1\\y_2\\\vdots\\y_n\end{bmatrix},\qquad X=\begin{bmatrix}x_{11}&x_{12}&\cdots&x_{1p}\\x_{21}&x_{22}&\cdots&x_{2p}\\\vdots&\vdots&&\vdots\\x_{n1}&x_{n2}&\cdots&x_{np}\end{bmatrix}=\begin{bmatrix}\boldsymbol{x}_1^{\mathsf T}\\\boldsymbol{x}_2^{\mathsf T}\\\vdots\\\boldsymbol{x}_n^{\mathsf T}\end{bmatrix}=(X_1,\dots,X_p),
$$

so $\boldsymbol{x}_i\in\mathbb{R}^p$ is the covariate vector of unit $i$ and $X_j\in\mathbb{R}^n$ is the $j$-th column. (In [3.2.3](/3.2.3) the intercept is counted separately, so $p+1$ there corresponds to $p$ here.) The OLS estimator is

$$
\hat{\boldsymbol{\beta}}=\arg\min_{\boldsymbol{\beta}}\frac1n\sum_{i=1}^n(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})^2=\arg\min_{\boldsymbol{\beta}}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2.
$$

The first-order condition is $\sum_{i=1}^n\boldsymbol{x}_i(y_i-\boldsymbol{x}_i^{\mathsf T}\hat{\boldsymbol{\beta}})=\boldsymbol{0}$, i.e. the normal equations $X^{\mathsf T}(\boldsymbol{Y}-X\hat{\boldsymbol{\beta}})=\boldsymbol{0}$, and if $X^{\mathsf T}X=\sum_i\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}$ is nonsingular (equivalently, $X$ has full column rank $p$),

$$
\hat{\boldsymbol{\beta}}=\Big(\sum_{i=1}^n\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}\Big)^{-1}\Big(\sum_{i=1}^n\boldsymbol{x}_iy_i\Big)=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$

For $p=2$ with $X=(\boldsymbol{1},\boldsymbol{x})$ this reduces to the formulas for $(\hat\alpha,\hat\beta)$ above.

### 7.1.3. The Geometry of Least Squares

Regard $\boldsymbol{Y}$ and the columns $X_1,\dots,X_p$ as vectors in $\mathbb{R}^n$. The vectors $X\boldsymbol{b}$, $\boldsymbol{b}\in\mathbb{R}^p$, fill the column space $\mathcal{R}(X)=\{b_1X_1+\cdots+b_pX_p\colon b_j\in\mathbb{R}\}$, so minimizing $\|\boldsymbol{Y}-X\boldsymbol{b}\|^2$ means finding the point of $\mathcal{R}(X)$ closest to $\boldsymbol{Y}$:

$$
X\hat{\boldsymbol{\beta}}=\arg\min_{\boldsymbol{v}\in\mathcal{R}(X)}\|\boldsymbol{Y}-\boldsymbol{v}\|^2.
$$

This is the **least squares** problem of linear algebra ([2.1](/2.1)), and the answer is the **orthogonal projection** of $\boldsymbol{Y}$ onto $\mathcal{R}(X)$: the residual $\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}$ is orthogonal to every column, which is exactly what the normal equations say.

![The geometry of least squares for n = 3 and two covariates: the fitted vector X b_hat is the orthogonal projection of Y onto the plane C(X) spanned by X_1 and X_2, the residual is perpendicular to that plane, and any other X b is farther from Y](./plots/ols-geometry.py)

**Definition 7.1.1** The vector of **fitted values** is $\hat{\boldsymbol{Y}}=X\hat{\boldsymbol{\beta}}$ and the vector of **residuals** is $\hat{\boldsymbol{\varepsilon}}=\boldsymbol{Y}-\hat{\boldsymbol{Y}}$. Since

$$
\hat{\boldsymbol{Y}}=X\hat{\boldsymbol{\beta}}=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}=H\boldsymbol{Y},\qquad H=X(X^{\mathsf T}X)^{-1}X^{\mathsf T},
$$
the $n\times n$ matrix $H$ is called the **hat matrix** ("it puts the hat on $\boldsymbol{Y}$").

$H$ is symmetric and idempotent, $H=H^{\mathsf T}$ and $H^2=H$, so it is the **orthogonal projection matrix** onto $\mathcal{R}(X)$, with $\operatorname{tr}(H)=\operatorname{tr}\big((X^{\mathsf T}X)^{-1}X^{\mathsf T}X\big)=p=\operatorname{rank}(H)$; $I_n-H$ projects onto the orthogonal complement and has rank $n-p$. Componentwise, $\hat y_i=\sum_{j=1}^nh_{ij}y_j$: each fitted value is a weighted average of all responses, and the diagonal entry $h_{ii}$ (the leverage of unit $i$) measures how much $y_i$ influences its own fit.

**Proposition 7.1.1 (Property I)** Without any probabilistic assumption, $\hat{\boldsymbol{Y}}\perp\hat{\boldsymbol{\varepsilon}}$, that is, $\hat{\boldsymbol{Y}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}=0$; consequently $\|\boldsymbol{Y}\|^2=\|\hat{\boldsymbol{Y}}\|^2+\|\hat{\boldsymbol{\varepsilon}}\|^2$.

**Proof** $\hat{\boldsymbol{Y}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}=\boldsymbol{Y}^{\mathsf T}H(I_n-H)\boldsymbol{Y}=\boldsymbol{Y}^{\mathsf T}(H-H^2)\boldsymbol{Y}=0$. $\square$

This is a purely geometric property of OLS; the next section adds probability.

## 7.2. Properties of the Least Squares Estimator

### 7.2.1. The Gauss–Markov Model

**Definition 7.2.1 (Gauss–Markov Model)** The **Gauss–Markov model** is

$$
\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},\qquad\mathbb{E}(\boldsymbol{\varepsilon})=\boldsymbol{0},\qquad\operatorname{Cov}(\boldsymbol{\varepsilon})=\sigma^2I_n,
$$
where the design matrix $X$ is fixed with linearly independent columns. Equivalently, $y_i=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}+\varepsilon_i$ with $\mathbb{E}\varepsilon_i=0$, $\operatorname{Var}(\varepsilon_i)=\sigma^2$ and $\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$ for $i\ne j$. The unknown parameters are $(\boldsymbol{\beta},\sigma^2)$.

Only the first two moments of the errors are specified. That suffices for the mean and covariance of every linear function of $\boldsymbol{Y}$.

**Theorem 7.2.1** Under the Gauss–Markov model,

$$
\mathbb{E}(\hat{\boldsymbol{\beta}})=\boldsymbol{\beta},\qquad\operatorname{Cov}(\hat{\boldsymbol{\beta}})=\sigma^2(X^{\mathsf T}X)^{-1},
$$
and for the fitted values and residuals

$$
\mathbb{E}\begin{bmatrix}\hat{\boldsymbol{Y}}\\\hat{\boldsymbol{\varepsilon}}\end{bmatrix}=\begin{bmatrix}X\boldsymbol{\beta}\\\boldsymbol{0}\end{bmatrix},\qquad\operatorname{Cov}\begin{bmatrix}\hat{\boldsymbol{Y}}\\\hat{\boldsymbol{\varepsilon}}\end{bmatrix}=\sigma^2\begin{bmatrix}H&O\\O&I_n-H\end{bmatrix}.
$$

**Proof** Since $\mathbb{E}(\boldsymbol{Y})=X\boldsymbol{\beta}$ and $\operatorname{Cov}(\boldsymbol{Y})=\sigma^2I_n$,

$$
\mathbb{E}(\hat{\boldsymbol{\beta}})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\mathbb{E}(\boldsymbol{Y})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}X\boldsymbol{\beta}=\boldsymbol{\beta},
$$

$$
\operatorname{Cov}(\hat{\boldsymbol{\beta}})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\operatorname{Cov}(\boldsymbol{Y})X(X^{\mathsf T}X)^{-1}=\sigma^2(X^{\mathsf T}X)^{-1}X^{\mathsf T}X(X^{\mathsf T}X)^{-1}=\sigma^2(X^{\mathsf T}X)^{-1}.
$$

For the second statement the key is that both vectors are linear in $\boldsymbol{Y}$:

$$
\begin{bmatrix}\hat{\boldsymbol{Y}}\\\hat{\boldsymbol{\varepsilon}}\end{bmatrix}=\begin{bmatrix}H\boldsymbol{Y}\\(I_n-H)\boldsymbol{Y}\end{bmatrix}=\begin{bmatrix}H\\I_n-H\end{bmatrix}\boldsymbol{Y}.
$$

The mean is $(HX\boldsymbol{\beta},(I_n-H)X\boldsymbol{\beta})=(X\boldsymbol{\beta},\boldsymbol{0})$ because $HX=X$, and the covariance is $\sigma^2\begin{bmatrix}H\\I_n-H\end{bmatrix}\begin{bmatrix}H&I_n-H\end{bmatrix}$, whose blocks are $H^2=H$, $H(I_n-H)=O$ and $(I_n-H)^2=I_n-H$. $\square$

So under the Gauss–Markov model the geometric orthogonality $\hat{\boldsymbol{Y}}\perp\hat{\boldsymbol{\varepsilon}}$ becomes $\operatorname{Cov}(\hat{\boldsymbol{Y}},\hat{\boldsymbol{\varepsilon}})=O$.

To estimate $\sigma^2$, write $\hat y_i=\boldsymbol{x}_i^{\mathsf T}\hat{\boldsymbol{\beta}}$ and $\hat\varepsilon_i=y_i-\hat y_i$; the residual $\hat\varepsilon_i$ is the vertical distance from the point to the fitted line, and $\sigma$ is the spread of $y$ around the population line. A natural choice is $\tilde\sigma^2=\operatorname{RSS}/n$ with the residual sum of squares

$$
\operatorname{RSS}=\sum_{i=1}^n\hat\varepsilon_i^2=\hat{\boldsymbol{\varepsilon}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}.
$$
However, $\mathbb{E}\hat\varepsilon_i=0$ and $\operatorname{Var}(\hat\varepsilon_i)=\sigma^2(1-h_{ii})$ by Theorem 7.2.1, so

$$
\mathbb{E}(\operatorname{RSS})=\sigma^2\sum_{i=1}^n(1-h_{ii})=\sigma^2\big(n-\operatorname{tr}(H)\big)=\sigma^2(n-p).
$$
Therefore we use

$$
\hat\sigma^2=\frac{\operatorname{RSS}}{n-p}=\frac{1}{n-p}\sum_{i=1}^n\hat\varepsilon_i^2,
$$
which is an **unbiased estimator** of $\sigma^2$: fitting $p$ coefficients uses up $p$ degrees of freedom.

The Gauss–Markov model also gives OLS an optimality property. For symmetric matrices write $A\succeq B$ if $A-B$ is positive semidefinite; $\operatorname{Cov}(\tilde{\boldsymbol{\beta}})\succeq\operatorname{Cov}(\hat{\boldsymbol{\beta}})$ means that $\operatorname{Var}(\boldsymbol{c}^{\mathsf T}\tilde{\boldsymbol{\beta}})\ge\operatorname{Var}(\boldsymbol{c}^{\mathsf T}\hat{\boldsymbol{\beta}})$ for every $\boldsymbol{c}\in\mathbb{R}^p$.

**Theorem 7.2.2 (Gauss–Markov Theorem)** Under the Gauss–Markov model, the OLS estimator $\hat{\boldsymbol{\beta}}$ is the best linear unbiased estimator (BLUE) of $\boldsymbol{\beta}$: $\operatorname{Cov}(\tilde{\boldsymbol{\beta}})\succeq\operatorname{Cov}(\hat{\boldsymbol{\beta}})$ for every estimator $\tilde{\boldsymbol{\beta}}$ such that

1. $\tilde{\boldsymbol{\beta}}=A\boldsymbol{Y}$ for some $A\in\mathbb{R}^{p\times n}$ not depending on $\boldsymbol{Y}$, and
2. $\mathbb{E}(\tilde{\boldsymbol{\beta}})=\boldsymbol{\beta}$ for every $\boldsymbol{\beta}$.

**Proof** Condition 2 means $AX\boldsymbol{\beta}=\boldsymbol{\beta}$ for all $\boldsymbol{\beta}$, i.e. $AX=I_p$. Write $A=(X^{\mathsf T}X)^{-1}X^{\mathsf T}+D$; then $DX=O$, and

$$
\operatorname{Cov}(\tilde{\boldsymbol{\beta}})=\sigma^2AA^{\mathsf T}=\sigma^2(X^{\mathsf T}X)^{-1}+\sigma^2DD^{\mathsf T}\succeq\sigma^2(X^{\mathsf T}X)^{-1}=\operatorname{Cov}(\hat{\boldsymbol{\beta}}),
$$
since the cross terms $(X^{\mathsf T}X)^{-1}X^{\mathsf T}D^{\mathsf T}$ vanish. $\square$

### 7.2.2. The Normal Linear Model

For exact confidence intervals and tests we strengthen the assumptions on the errors.

**Definition 7.2.2 (Normal Linear Model)** The **normal linear model** is

$$
\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},\qquad\boldsymbol{\varepsilon}\sim\mathcal{N}_n(\boldsymbol{0},\sigma^2I_n),
$$
with a fixed design matrix $X$ of full column rank; equivalently $y_i=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}+\varepsilon_i$ with $\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$, $i=1,\dots,n$.

Since uncorrelated errors with common variance are implied, the normal linear model is a special case of the Gauss–Markov model, and all results of Section 7.2.1 remain valid. Recall $\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$, $\hat{\boldsymbol{Y}}=X\hat{\boldsymbol{\beta}}$, $\hat{\boldsymbol{\varepsilon}}=\boldsymbol{Y}-\hat{\boldsymbol{Y}}$ and $\hat\sigma^2=\hat{\boldsymbol{\varepsilon}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}/(n-p)$.

**Theorem 7.2.3** Under the normal linear model,

$$
\begin{bmatrix}\hat{\boldsymbol{\beta}}\\\hat{\boldsymbol{\varepsilon}}\end{bmatrix}\sim\mathcal{N}_{p+n}\left(\begin{bmatrix}\boldsymbol{\beta}\\\boldsymbol{0}\end{bmatrix},\ \sigma^2\begin{bmatrix}(X^{\mathsf T}X)^{-1}&O\\O&I_n-H\end{bmatrix}\right),\qquad\frac{\hat\sigma^2}{\sigma^2}\sim\frac{\chi^2_{n-p}}{n-p},
$$
so $\hat{\boldsymbol{\beta}}\perp\!\!\!\perp\hat{\boldsymbol{\varepsilon}}$ and $\hat{\boldsymbol{\beta}}\perp\!\!\!\perp\hat\sigma^2$. Likewise $(\hat{\boldsymbol{Y}},\hat{\boldsymbol{\varepsilon}})$ is jointly normal with the moments of Theorem 7.2.1, so $\hat{\boldsymbol{Y}}\perp\!\!\!\perp\hat{\boldsymbol{\varepsilon}}$.

**Proof** The vector $(\hat{\boldsymbol{\beta}},\hat{\boldsymbol{\varepsilon}})$ equals $\begin{bmatrix}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\\I_n-H\end{bmatrix}\boldsymbol{Y}$, a linear transformation of the normal vector $\boldsymbol{Y}$, so it is (singular) multivariate normal. Its mean is $(\boldsymbol{\beta},\boldsymbol{0})$, and the off-diagonal covariance block is $\sigma^2(X^{\mathsf T}X)^{-1}X^{\mathsf T}(I_n-H)=O$ because $X^{\mathsf T}H=X^{\mathsf T}$. For jointly normal vectors, zero covariance means independence, so $\hat{\boldsymbol{\beta}}$ is independent of $\hat{\boldsymbol{\varepsilon}}$ and of every function of it, in particular of $\hat\sigma^2$. Finally $\hat{\boldsymbol{\varepsilon}}=(I_n-H)\boldsymbol{\varepsilon}$, so $\hat{\boldsymbol{\varepsilon}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}=\boldsymbol{\varepsilon}^{\mathsf T}(I_n-H)\boldsymbol{\varepsilon}$; writing the projection $I_n-H=QQ^{\mathsf T}$ with $Q\in\mathbb{R}^{n\times(n-p)}$ having orthonormal columns, $Q^{\mathsf T}\boldsymbol{\varepsilon}/\sigma\sim\mathcal{N}_{n-p}(\boldsymbol{0},I_{n-p})$, hence $\hat{\boldsymbol{\varepsilon}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}/\sigma^2=\|Q^{\mathsf T}\boldsymbol{\varepsilon}/\sigma\|^2\sim\chi^2_{n-p}$. The statement for $\hat{\boldsymbol{Y}}=X\hat{\boldsymbol{\beta}}$ follows in the same way. $\square$

The theorem is the source of all exact inference in the linear model. The three typical applications are a single linear combination, several linear combinations, and prediction.

**Corollary 7.2.1** Under the normal linear model, for every $\boldsymbol{c}\in\mathbb{R}^p$,

$$
\boldsymbol{c}^{\mathsf T}\hat{\boldsymbol{\beta}}\sim\mathcal{N}\big(\boldsymbol{c}^{\mathsf T}\boldsymbol{\beta},\ \sigma^2\boldsymbol{c}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{c}\big),\qquad T_{\boldsymbol{c}}=\frac{\boldsymbol{c}^{\mathsf T}\hat{\boldsymbol{\beta}}-\boldsymbol{c}^{\mathsf T}\boldsymbol{\beta}}{\sqrt{\hat\sigma^2\boldsymbol{c}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{c}}}\sim t_{n-p}.
$$

Taking $\boldsymbol{c}$ to be the $j$-th standard basis vector gives the usual $t$-test and confidence interval for a single coefficient $\beta_j$ ([3.2.5](/3.2.5)).

**Corollary 7.2.2** Let $C$ be an $l\times p$ matrix of rank $l$ with rows $\boldsymbol{c}_1^{\mathsf T},\dots,\boldsymbol{c}_l^{\mathsf T}$, so that $C\boldsymbol{\beta}=(\boldsymbol{c}_1^{\mathsf T}\boldsymbol{\beta},\dots,\boldsymbol{c}_l^{\mathsf T}\boldsymbol{\beta})^{\mathsf T}$. Under the normal linear model, $C\hat{\boldsymbol{\beta}}-C\boldsymbol{\beta}\sim\mathcal{N}_l\big(\boldsymbol{0},\sigma^2C(X^{\mathsf T}X)^{-1}C^{\mathsf T}\big)$, and

$$
F_C=\frac{(C\hat{\boldsymbol{\beta}}-C\boldsymbol{\beta})^{\mathsf T}\{C(X^{\mathsf T}X)^{-1}C^{\mathsf T}\}^{-1}(C\hat{\boldsymbol{\beta}}-C\boldsymbol{\beta})}{l\,\hat\sigma^2}\sim F_{l,n-p}.
$$

**Proof** The numerator times $l/\sigma^2$ is a quadratic form $\boldsymbol{Z}^{\mathsf T}\Sigma_Z^{-1}\boldsymbol{Z}$ of a normal vector $\boldsymbol{Z}\sim\mathcal{N}_l(\boldsymbol{0},\Sigma_Z)$, hence $\chi^2_l$; it is a function of $\hat{\boldsymbol{\beta}}$ and so independent of $(n-p)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p}$. The ratio of the two chi-square variables divided by their degrees of freedom is $F_{l,n-p}$. $\square$

For example, with $C=\begin{bmatrix}\boldsymbol{0}&I_{p-1}\end{bmatrix}$ we get $C\boldsymbol{\beta}=(\beta_2,\dots,\beta_p)^{\mathsf T}$, and $F_C$ with $C\boldsymbol{\beta}=\boldsymbol{0}$ tests whether any covariate besides the intercept matters. The statistic has the same structure as Hotelling's $T^2$ in [3.4.3](/3.4.3): a squared distance in the metric of the inverse covariance matrix.

For prediction at a new covariate vector $\boldsymbol{x}^*$ there are two targets. The mean response $\boldsymbol{x}^{*\mathsf T}\boldsymbol{\beta}$ is estimated by $\hat y^*=\boldsymbol{x}^{*\mathsf T}\hat{\boldsymbol{\beta}}$, and Corollary 7.2.1 with $\boldsymbol{c}=\boldsymbol{x}^*$ gives the confidence interval

$$
\hat y^*\pm t_{n-p,\alpha/2}\,\hat\sigma\sqrt{\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*}.
$$
A new response $y^*=\boldsymbol{x}^{*\mathsf T}\boldsymbol{\beta}+\varepsilon^*$, with $\varepsilon^*\sim\mathcal{N}(0,\sigma^2)$ independent of the data, satisfies $y^*-\hat y^*\sim\mathcal{N}\big(0,\sigma^2(1+\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*)\big)$, which gives the prediction interval

$$
\hat y^*\pm t_{n-p,\alpha/2}\,\hat\sigma\sqrt{1+\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*}.
$$
The extra $1$ accounts for the noise of the new observation; it does not vanish as $n\to\infty$, while the confidence interval shrinks to a point.

### 7.2.3. Examples

**Example 7.2.1 (Galton's Height Data)** Galton's family data record the heights (in inches) of $934$ adult children together with the mid-parent height, the average of the two parents' heights. Regressing the child's height on the mid-parent height gives

| | estimate | std. error | $t$ value | $p$-value |
|---|---|---|---|---|
| intercept | $22.64$ | $4.27$ | $5.31$ | $1.4\times10^{-7}$ |
| mid-parent height | $0.637$ | $0.0616$ | $10.35$ | $8.1\times10^{-24}$ |

The slope is clearly positive but smaller than $1$: children of tall parents are tall, but on average less extreme than their parents, which is the regression toward the mean of Section 7.1.2. At a mid-parent height of $60$ inches the fitted value is $60.88$, with $95\%$ confidence interval $[59.74,62.01]$ for the mean height. The prediction intervals are much wider than the confidence intervals, and both widen as $\boldsymbol{x}^*$ moves away from the center of the data, because $\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*$ grows.

**Example 7.2.2 (Job Training)** In the Lalonde data ($n=445$), the 1978 earnings re78 of participants in a job-training experiment are regressed on the treatment indicator and ten pretreatment covariates (age, years of education, indicators for black, Hispanic, married and no degree, the 1974 and 1975 earnings and the indicators of zero earnings in those years), so $p=12$ and $n-p=433$. The treatment coefficient is $1671$ (std. error $641$, $t=2.61$, $p=0.0095$), a significant positive effect, whereas none of the covariates is individually significant at level $0.05$. Are they jointly significant? Corollary 7.2.2 with the $10\times12$ matrix $C$ selecting the ten covariate coefficients gives $F_C=1.857$ on $(10,433)$ degrees of freedom, $p=0.049$: only weakly significant at level $0.05$. Individual $t$-tests and a joint $F$-test answer different questions, and neither can replace the other.

### 7.2.4. Comparison of the Assumptions

| Assumptions | Key property |
|---|---|
| none | $\hat{\boldsymbol{Y}}\perp\hat{\boldsymbol{\varepsilon}}$ (geometric property of OLS) |
| Gauss–Markov model: $\mathbb{E}\varepsilon_i=0$, $\operatorname{Var}(\varepsilon_i)=\sigma^2$, $\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$ ($i\ne j$) | $\operatorname{Cov}(\hat{\boldsymbol{Y}},\hat{\boldsymbol{\varepsilon}})=O$; $\hat{\boldsymbol{\beta}}$ unbiased and BLUE; $\hat\sigma^2$ unbiased |
| normal linear model: $\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$ | $\hat{\boldsymbol{Y}}$ independent of $\hat{\boldsymbol{\varepsilon}}$ (probabilistic property); exact $t$ and $F$ inference |

Although normality is a strong assumption, the procedures derived from it are robust to many violations: by the **central limit theorem**, $\hat{\boldsymbol{\beta}}$ is approximately normal for large $n$ under the Gauss–Markov model, and the $t$- and $F$-procedures remain approximately valid.

## 7.3. Overfitting, Regularization and Model Selection

### 7.3.1. Many Covariates

Including useless covariates makes the estimators less precise. This is harmless when the number of covariates is small compared with the sample size, but in many modern applications it is not: DNA sequencing, for instance, produces millions of covariates for a few hundred subjects. The theory above then breaks down. When the columns of $X$ are highly correlated (multicollinearity), $X^{\mathsf T}X$ is nearly singular and $\operatorname{Cov}(\hat{\boldsymbol{\beta}})=\sigma^2(X^{\mathsf T}X)^{-1}$ is huge; when $p>n$, $X^{\mathsf T}X$ is singular and the OLS estimator is not even unique. A model with many parameters can fit the training data very well and still predict new data poorly, which is called overfitting.

Remedies include diagnostic indices such as the variance inflation factor; model selection criteria such as the RSS, $R^2$ and adjusted $R^2$, information criteria (AIC, BIC) and cross-validation; and variable selection procedures such as forward and backward selection. These are developed in [3.3](/3.3). Here we discuss three methods that modify the estimator itself. Most of them minimize a penalized objective

$$
Q(\boldsymbol{\beta})=\frac{1}{2n}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\sum_{j=1}^pp_\lambda(\lvert\beta_j\rvert),
$$
where $p_\lambda(\cdot)$ is a *penalty function* and $\lambda\ge0$ is a *tuning parameter* that controls the strength of the penalty and is usually chosen by cross-validation. Throughout this section we assume that the columns of $X$ are centered (each has mean zero) and $\boldsymbol{Y}$ is centered, so that the intercept is estimated by $\bar y$ and is not penalized.

### 7.3.2. Ridge Regression

**Definition 7.3.1 (Ridge Regression)** For $\lambda>0$, the **ridge regression** estimator is

$$
\hat{\boldsymbol{\beta}}^{\mathrm{Ridge}}(\lambda)=\arg\min_{\boldsymbol{\beta}}\big\{\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\lambda\|\boldsymbol{\beta}\|^2\big\}=(X^{\mathsf T}X+\lambda I_p)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$

The closed form follows from setting the gradient $-2X^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol{\beta})+2\lambda\boldsymbol{\beta}$ to zero. Since $X^{\mathsf T}X$ is a **positive semidefinite matrix**, $X^{\mathsf T}X+\lambda I_p$ is positive definite and hence invertible for every $\lambda>0$, even when $p>n$.

What is the effect of the penalty? Take the **singular value decomposition** $X=UDV^{\mathsf T}$ ([2.1](/2.1)), with $\boldsymbol{u}_j$ the columns of $U$ and singular values $d_1\ge\cdots\ge d_p\ge0$. Then

$$
X\hat{\boldsymbol{\beta}}^{\mathrm{OLS}}=\sum_{j=1}^p\boldsymbol{u}_j\,\boldsymbol{u}_j^{\mathsf T}\boldsymbol{Y},\qquad X\hat{\boldsymbol{\beta}}^{\mathrm{Ridge}}(\lambda)=UD(D^2+\lambda I_p)^{-1}DU^{\mathsf T}\boldsymbol{Y}=\sum_{j=1}^p\boldsymbol{u}_j\,\frac{d_j^2}{d_j^2+\lambda}\,\boldsymbol{u}_j^{\mathsf T}\boldsymbol{Y}
$$
(the first formula when $X$ has full column rank). Because the columns of $X$ are centered, $X\boldsymbol{v}_j=d_j\boldsymbol{u}_j$ is the $j$-th sample principal component of the covariates and $d_j^2/n$ its variance. OLS projects $\boldsymbol{Y}$ onto all principal component directions with weight $1$; ridge regression shrinks the coordinate along the $j$-th direction by the factor $d_j^2/(d_j^2+\lambda)$, so the directions of small variance, where the data carry little information and OLS is most unstable, are shrunk the most. The price is bias, $\mathbb{E}\hat{\boldsymbol{\beta}}^{\mathrm{Ridge}}=(X^{\mathsf T}X+\lambda I_p)^{-1}X^{\mathsf T}X\boldsymbol{\beta}\ne\boldsymbol{\beta}$; the gain is a smaller variance, and for a suitable $\lambda$ a smaller **mean squared error** than OLS, an instance of the **bias–variance trade-off**.

### 7.3.3. Principal Component Regression

**Definition 7.3.2 (Principal Component Regression)** **Principal component regression** (PCR) computes the principal components of the covariates (the columns of $XV$, [3.4.5](/3.4.5)), selects some of them, and regresses $\boldsymbol{Y}$ by OLS on the selected components instead of the original covariates.

Since the components are uncorrelated, the regression on them decouples; in the notation above, PCR keeping the set $J$ of components fits $\sum_{j\in J}\boldsymbol{u}_j\boldsymbol{u}_j^{\mathsf T}\boldsymbol{Y}$, so it shrinks with factor $1$ or $0$ where ridge regression shrinks smoothly. The usual choice keeps the first $k$ components, which amounts to discarding the low-variance directions. This is not necessarily the best choice: the components with the largest variances need not be the most informative about $Y$, and the response may depend mainly on a component of small variance (I. Jolliffe, 1982). One should select the components that are most predictive of $Y$, for example by their correlation with $Y$ or by cross-validation, rather than by their variances.

### 7.3.4. The Lasso

Ridge regression predicts well, but its many small, nonzero coefficients are difficult to interpret. R. Tibshirani (1996) proposed the **Lasso** (least absolute shrinkage and selection operator) to achieve the ambitious goal of estimating the parameters and selecting the important variables simultaneously:

$$
\hat{\boldsymbol{\beta}}^{\mathrm{Lasso}}(\lambda)=\arg\min_{\boldsymbol{\beta}}\Big\{\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\lambda\sum_{j=1}^p\lvert\beta_j\rvert\Big\}.
$$
The objective is convex but not differentiable, and there is no closed-form solution; it is computed by algorithms such as coordinate descent or LARS ([3.2.3](/3.2.3) surveys its theory).

To compare the two penalties, first rewrite both as constrained problems. By Lagrangian duality, for each $\lambda\ge0$ there is a $t\ge0$ such that the Lasso solves

$$
\min_{\boldsymbol{\beta}}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2\quad\text{subject to}\quad\sum_{j=1}^p\lvert\beta_j\rvert\le t,
$$
and ridge regression solves the same problem with the constraint $\sum_j\beta_j^2\le t$. Second, the objective has elliptical level sets centered at the OLS estimator: since $X^{\mathsf T}(\boldsymbol{Y}-X\hat{\boldsymbol{\beta}})=\boldsymbol{0}$, the cross term vanishes in

$$
\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2=(\boldsymbol{Y}-X\hat{\boldsymbol{\beta}})^{\mathsf T}(\boldsymbol{Y}-X\hat{\boldsymbol{\beta}})+(\boldsymbol{\beta}-\hat{\boldsymbol{\beta}})^{\mathsf T}X^{\mathsf T}X(\boldsymbol{\beta}-\hat{\boldsymbol{\beta}}),
$$
which is the Pythagorean decomposition of Section 7.1.3. The constrained solution is the point where the smallest ellipse $(\boldsymbol{b}-\hat{\boldsymbol{\beta}})^{\mathsf T}X^{\mathsf T}X(\boldsymbol{b}-\hat{\boldsymbol{\beta}})=c$ first touches the constraint region. The $\ell_1$ ball is a diamond (a cross-polytope in higher dimensions) whose corners lie on the coordinate axes, and the ellipse typically touches it at a corner, where some coefficients are exactly zero; the $\ell_2$ ball is round, and the contact point generically has all coordinates nonzero.

![Lasso and ridge regression in two dimensions: elliptical contours of the residual sum of squares centered at the OLS estimate first touch the l1 diamond at a corner, giving a sparse Lasso solution with b_2 = 0, and touch the l2 disk at a point with both coordinates nonzero](./plots/ridge-lasso-geometry.py)

## 7.4. Model Checking

Model checking is an essential part of regression analysis, and its tools (residual plots, leverage and influence measures, tests of the assumptions) belong to [3.3](/3.3). One classical example shows why it cannot be skipped.

**Example 7.4.1 (Anscombe's Quartet)** F. Anscombe (1973) constructed four data sets of $11$ points each for which the least squares fits are almost identical: in all four the fitted line is $\hat y=3.00+0.500x$, with the same $R^2\approx0.67$, the same residual standard error and the same $t$-statistics. Yet the scatter plots reveal fundamental differences: the first looks like a linear relation with noise, the second is a smooth curve, in the third a single outlier tilts an otherwise exact line, and in the fourth one high-leverage point alone determines the slope. The numerical summaries of a regression are meaningful only when the model is adequate, and plotting the data is the first check.

![Anscombe's quartet: four data sets with practically the same least squares line y = 3 + 0.5 x and the same R^2, but completely different scatter plots](./plots/anscombe-quartet.py)

## Summary

The OLS estimator $\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ of the model $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ ("linear" meaning linear in the parameters) makes $\hat{\boldsymbol{Y}}=H\boldsymbol{Y}$ the orthogonal projection of $\boldsymbol{Y}$ onto $\mathcal{R}(X)$; with one covariate, the standardized slope is the correlation. Its properties depend on the assumptions:

| | geometry only | Gauss–Markov model | normal linear model |
|---|---|---|---|
| $\hat{\boldsymbol{Y}}$ and $\hat{\boldsymbol{\varepsilon}}$ | orthogonal | uncorrelated | independent |
| $\hat{\boldsymbol{\beta}}$ | solves the normal equations | unbiased, $\operatorname{Cov}=\sigma^2(X^{\mathsf T}X)^{-1}$, BLUE | $\mathcal{N}_p(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1})$ |
| $\hat\sigma^2=\operatorname{RSS}/(n-p)$ | — | unbiased | $\sigma^2\chi^2_{n-p}/(n-p)$, independent of $\hat{\boldsymbol{\beta}}$ |

- Inference and prediction: $T_{\boldsymbol{c}}\sim t_{n-p}$ for one linear combination, $F_C\sim F_{l,n-p}$ for several; confidence intervals for the mean response use $\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*$, prediction intervals add $1$ under the square root.
- Many covariates: ridge regression shrinks along the principal component directions by $d_j^2/(d_j^2+\lambda)$; principal component regression keeps or drops whole components (to be chosen by relevance to $Y$, not by variance); the $\ell_1$ penalty of the Lasso sets coefficients exactly to zero and selects variables.
- Model checking: identical regression output can come from completely different data (Anscombe's quartet); always look at the data.
- Connections: the projection and spectral tools come from [2.1](/2.1) and [3.4.1](/3.4.1), the distribution theory from [3.4.2](/3.4.2); the $F$-statistic parallels Hotelling's $T^2$ ([3.4.3](/3.4.3)); the factor scores of [3.4.8](/3.4.8) and the multiple correlation of [3.4.9](/3.4.9) reuse the least squares ideas of this chapter.
