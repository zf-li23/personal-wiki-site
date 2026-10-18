---
title: The Matrix Approach and Multiple Linear Regression
description: Simple linear regression in matrix form, least squares by calculus and by orthogonal projection onto the column space, the sampling distribution of the estimates; the multiple linear regression model, its parameters and special cases, the Gauss–Markov theorem, the hat matrix and leverage, and the analysis of variance with the overall F-test, R² and adjusted R².
---

With one predictor, every formula of the previous chapters could be written with sums. With several predictors this becomes unmanageable, and the natural language is that of vectors and matrices: the data form a response vector and a design matrix, least squares becomes an orthogonal projection, and all sums of squares become quadratic forms. This chapter first rewrites simple linear regression ([3.3.2](/3.3.2)–[3.3.4](/3.3.4)) in this language, so that nothing new happens except the notation, and then lets the design matrix have more columns: the multiple linear regression model. We derive the least squares estimates analytically and geometrically, their sampling distribution, the Gauss–Markov theorem, the properties of the hat matrix (which explain the leverages and residual variances used in [3.3.5](/3.3.5) and [3.3.6](/3.3.6)), and the analysis of variance for the whole model with $R^2$ and adjusted $R^2$. Inference on individual coefficients and on groups of them follows in [3.3.8](/3.3.8) and [3.3.9](/3.3.9). The linear algebra comes from [2.1](/2.1), the distribution theory from [3.1.15](/3.1.15); the same model is treated from the multivariate point of view in [3.4.7](/3.4.7).

## 7.1. Simple Linear Regression in Matrix Form

### 7.1.1. Tools: the Multivariate Normal Distribution and Quadratic Forms

We collect the facts used in this chapter. For a random vector $\boldsymbol{Z}$ with mean vector $\boldsymbol{\mu}$, the **covariance matrix** $\operatorname{Cov}(\boldsymbol{Z}) = \mathbb{E}\big[(\boldsymbol{Z} - \boldsymbol{\mu})(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\big]$ ([3.1.10](/3.1.10)) has the blocks $\operatorname{Cov}(\boldsymbol{Z}_1)$, $\operatorname{Cov}(\boldsymbol{Z}_1, \boldsymbol{Z}_2)$, … for a partitioned $\boldsymbol{Z}$, and for constant $A$, $\boldsymbol{c}$,

$$
\mathbb{E}(A\boldsymbol{Z} + \boldsymbol{c}) = A\boldsymbol{\mu} + \boldsymbol{c}, \qquad \operatorname{Cov}(A\boldsymbol{Z} + \boldsymbol{c}) = \mathbb{E}\big[A(\boldsymbol{Z} - \boldsymbol{\mu})(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}A^{\mathsf T}\big] = A\operatorname{Cov}(\boldsymbol{Z})A^{\mathsf T}.
$$

**Theorem 7.1.1 (Properties of the Multivariate Normal Distribution)** Let $\boldsymbol{Z}$ be an $n \times 1$ random vector with the **multivariate normal distribution** $\mathcal{N}_n(\boldsymbol{\mu}, \Sigma)$ ([3.1.15](/3.1.15)).

1. (N1) A linear transformation of a normal vector is normal: $A\boldsymbol{Z} + \boldsymbol{c} \sim \mathcal{N}(A\boldsymbol{\mu} + \boldsymbol{c}, A\Sigma A^{\mathsf T})$ for every constant $d \times n$ matrix $A$ and $\boldsymbol{c} \in \mathbb{R}^d$.
2. (N2) A normal distribution is specified by its first and second moments, the mean vector and the covariance matrix.
3. (N3) If $\boldsymbol{Z} = \begin{bmatrix}\boldsymbol{Z}_1\\\boldsymbol{Z}_2\end{bmatrix}$ is normal and $\boldsymbol{Z}_1, \boldsymbol{Z}_2$ are uncorrelated, $\operatorname{Cov}(\boldsymbol{Z}_1, \boldsymbol{Z}_2) = O$, then $\boldsymbol{Z}_1$ and $\boldsymbol{Z}_2$ are independent; the same holds for $k$ blocks.
4. (N4) $\boldsymbol{W}_1 = A_1\boldsymbol{Z}$ and $\boldsymbol{W}_2 = A_2\boldsymbol{Z}$ are independent if and only if $A_1\Sigma A_2^{\mathsf T} = O$. If $\Sigma = \sigma^2I_n$, the condition is $A_1A_2^{\mathsf T} = O$.
5. (N5) If $\boldsymbol{W}_i = A_i\boldsymbol{Z}$, $i = 1, \dots, k$, with $\operatorname{Cov}(\boldsymbol{W}_i, \boldsymbol{W}_j) = O$ for $1 \le i < j \le k$, then the squared lengths $\boldsymbol{W}_1^{\mathsf T}\boldsymbol{W}_1, \dots, \boldsymbol{W}_k^{\mathsf T}\boldsymbol{W}_k$ are mutually independent.
6. (N6) If $\Sigma$ is nonsingular, $(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{Z} - \boldsymbol{\mu}) \sim \chi^2_n$. If $\Sigma$ is singular with rank $r < n$ and $\Sigma^-$ is a generalized inverse of $\Sigma$ (any matrix with $\Sigma\Sigma^-\Sigma = \Sigma$; it is not unique), then $(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\Sigma^-(\boldsymbol{Z} - \boldsymbol{\mu}) \sim \chi^2_r$.

(N1)–(N4) are proved in [3.1.15](/3.1.15) (the stacked vector $(\boldsymbol{W}_1, \boldsymbol{W}_2) = \begin{bmatrix}A_1\\A_2\end{bmatrix}\boldsymbol{Z}$ is normal by (N1), with off-diagonal covariance block $A_1\Sigma A_2^{\mathsf T}$, so (N4) follows from (N3)); (N5) follows from (N3), since functions of independent vectors are independent, and is what makes sums of squares independent. For (N6), $\Sigma^{-1/2}(\boldsymbol{Z} - \boldsymbol{\mu}) \sim \mathcal{N}(\boldsymbol{0}, I_n)$ is the standardization of $\boldsymbol{Z}$, and the quadratic form is its squared length; in the singular case the possible values of $\boldsymbol{Z} - \boldsymbol{\mu}$ only occupy an $r$-dimensional subspace of $\mathbb{R}^n$.

**Lemma 7.1.1** A square matrix $A$ of order $n$ is idempotent ($A^2 = A$) if and only if $\operatorname{rank}(A) + \operatorname{rank}(I_n - A) = n$.

**Proof** Every $\boldsymbol{x} \in \mathbb{R}^n$ is $\boldsymbol{x} = A\boldsymbol{x} + (I_n - A)\boldsymbol{x}$, so $\mathbb{R}^n = \mathcal{R}(A) + \mathcal{R}(I_n - A)$ and the ranks always add up to at least $n$. If $A^2 = A$, then $A(I_n - A) = O$, so $\mathcal{R}(I_n - A) \subseteq \mathcal{N}(A)$; conversely $A\boldsymbol{x} = \boldsymbol{0}$ implies $\boldsymbol{x} = (I_n - A)\boldsymbol{x}$. Hence $\mathcal{R}(I_n - A) = \mathcal{N}(A)$, whose dimension is $n - \operatorname{rank}(A)$. If the ranks add up to $n$, the sum $\mathcal{R}(A) + \mathcal{R}(I_n - A)$ is direct, so $\mathcal{R}(A) \cap \mathcal{R}(I_n - A) = \{\boldsymbol{0}\}$; the vector $(A - A^2)\boldsymbol{x} = A(I_n - A)\boldsymbol{x} = (I_n - A)A\boldsymbol{x}$ lies in both, hence is $\boldsymbol{0}$ for every $\boldsymbol{x}$, and $A^2 = A$. $\square$

**Theorem 7.1.2 (Expectation of a Quadratic Form)** Let $\boldsymbol{Z}$ be a random vector with mean $\boldsymbol{\mu}$ and covariance matrix $\Sigma$, and $A$ a constant square matrix. Then

$$
\mathbb{E}(\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}) = \operatorname{tr}(A\Sigma) + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}.
$$

**Proof** (The trace trick.) Expanding around $\boldsymbol{\mu}$, the linear terms have expectation zero, and a number equals its own trace, $\operatorname{tr}(\boldsymbol{u}^{\mathsf T}A\boldsymbol{u}) = \operatorname{tr}(A\boldsymbol{u}\boldsymbol{u}^{\mathsf T})$:

$$
\begin{aligned}
\mathbb{E}(\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}) &= \mathbb{E}\big[(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}A(\boldsymbol{Z} - \boldsymbol{\mu})\big] + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu} = \operatorname{tr}\big\{\mathbb{E}\big[A(\boldsymbol{Z} - \boldsymbol{\mu})(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\big]\big\} + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu} \\
&= \operatorname{tr}\big\{A\,\mathbb{E}\big[(\boldsymbol{Z} - \boldsymbol{\mu})(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\big]\big\} + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu} = \operatorname{tr}(A\Sigma) + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}. \qquad \square
\end{aligned}
$$
The theorem needs only the first two moments; normality is not required.

**Example 7.1.1 (Equicorrelated Variables)** Let $X_1, \dots, X_n$ have mean $0$, variance $1$ and pairwise correlation $\rho$, and $Y = a_1X_1 + \cdots + a_nX_n = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$. Then $\mathbb{E}(Y) = \boldsymbol{a}^{\mathsf T}\mathbb{E}(\boldsymbol{X}) = 0$ and $\operatorname{Var}(Y) = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}$ with $\Sigma = (1 - \rho)I_n + \rho\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$, where $\boldsymbol{1}_n$ is the vector of ones. How negative can $\rho$ be? A covariance matrix is positive semidefinite, and the eigenvalues of $\Sigma$ are $1 + (n - 1)\rho$ (eigenvector $\boldsymbol{1}_n$) and $1 - \rho$ (on the orthogonal complement of $\boldsymbol{1}_n$, multiplicity $n - 1$). Hence $\rho \ge -1/(n - 1)$, and the minimum $\rho = -1/(n - 1)$ is attained, for instance, by $X_i = \sqrt{n/(n - 1)}\,(U_i - \bar U)$ with $U_1, \dots, U_n$ iid of variance $1$; then $Y = \boldsymbol{1}_n^{\mathsf T}\boldsymbol{X}$ has variance $0$.

### 7.1.2. The Model in Matrix Form

The simple linear regression model $Y_i = \beta_0 + \beta_1X_i + \varepsilon_i$, with independent normal errors of mean $0$ and variance $\sigma^2$, consists of the $n$ equations

$$
Y_1 = \beta_0 + \beta_1X_1 + \varepsilon_1, \quad Y_2 = \beta_0 + \beta_1X_2 + \varepsilon_2, \quad \dots, \quad Y_n = \beta_0 + \beta_1X_n + \varepsilon_n,
$$
that is,

$$
\begin{bmatrix}Y_1\\Y_2\\\vdots\\Y_n\end{bmatrix} = \begin{bmatrix}\beta_0 + \beta_1X_1\\\beta_0 + \beta_1X_2\\\vdots\\\beta_0 + \beta_1X_n\end{bmatrix} + \begin{bmatrix}\varepsilon_1\\\varepsilon_2\\\vdots\\\varepsilon_n\end{bmatrix} = \begin{bmatrix}1 & X_1\\1 & X_2\\\vdots & \vdots\\1 & X_n\end{bmatrix}\begin{bmatrix}\beta_0\\\beta_1\end{bmatrix} + \begin{bmatrix}\varepsilon_1\\\varepsilon_2\\\vdots\\\varepsilon_n\end{bmatrix}.
$$
In matrix form,

$$
\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon},
$$
with the vector of responses $\boldsymbol{Y} = (Y_1, \dots, Y_n)^{\mathsf T}$, the $n \times 2$ **design matrix** $X$ with rows $(1, X_i)$, the vector of parameters (coefficients) $\boldsymbol{\beta} = (\beta_0, \beta_1)^{\mathsf T}$ and the vector of error terms $\boldsymbol{\varepsilon} = (\varepsilon_1, \dots, \varepsilon_n)^{\mathsf T}$.

Since the errors are independent with common variance, their covariance matrix is

$$
\operatorname{Cov}(\boldsymbol{\varepsilon}) = \operatorname{Cov}\begin{bmatrix}\varepsilon_1\\\vdots\\\varepsilon_n\end{bmatrix} = \sigma^2I_n:
$$
the covariance between any two error terms is zero, and the diagonal entries all equal $\sigma^2$. Because the design matrix is fixed, $X\boldsymbol{\beta}$ is a constant vector, so $\boldsymbol{Y}$ and $\boldsymbol{\varepsilon}$ have the same covariance matrix, $\operatorname{Cov}(\boldsymbol{Y}) = \sigma^2I_n$. The distributional model is

$$
\boldsymbol{Y} \sim \mathcal{N}_n(X\boldsymbol{\beta}, \sigma^2I_n).
$$

### 7.1.3. Least Squares: The Analytic Approach

The least squares criterion is

$$
Q(\boldsymbol{\beta}) = \|\boldsymbol{Y} - X\boldsymbol{\beta}\|^2 = (\boldsymbol{Y} - X\boldsymbol{\beta})^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{\beta}), \qquad \hat{\boldsymbol{\beta}} = \arg\min_{\boldsymbol{\beta} \in \mathbb{R}^2}Q(\boldsymbol{\beta}).
$$
Its gradient and Hessian are

$$
\frac{\partial Q}{\partial\boldsymbol{\beta}} = -2X^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{\beta}), \qquad \frac{\partial^2Q}{\partial\boldsymbol{\beta}\,\partial\boldsymbol{\beta}^{\mathsf T}} = 2X^{\mathsf T}X.
$$
Setting the gradient to zero gives the **normal equations** $X^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{\beta}) = \boldsymbol{0}$, i.e. $X^{\mathsf T}X\boldsymbol{\beta} = X^{\mathsf T}\boldsymbol{Y}$. The Hessian is positive semidefinite, and positive definite exactly when $\operatorname{rank}(X) = 2$ (the $X_i$ are not all equal). Under this condition the minimizer of $Q$ exists and is unique:

$$
\boldsymbol{b} = \hat{\boldsymbol{\beta}} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$
Explicitly,

$$
X^{\mathsf T}X = \begin{bmatrix}n & \sum X_i\\\sum X_i & \sum X_i^2\end{bmatrix}, \qquad (X^{\mathsf T}X)^{-1} = \frac{1}{n\sum X_i^2 - (\sum X_i)^2}\begin{bmatrix}\sum X_i^2 & -\sum X_i\\-\sum X_i & n\end{bmatrix}, \qquad X^{\mathsf T}\boldsymbol{Y} = \begin{bmatrix}\sum Y_i\\\sum X_iY_i\end{bmatrix},
$$
and multiplying out recovers $b_1 = \sum(X_i - \bar X)(Y_i - \bar Y)/\sum(X_i - \bar X)^2$ and $b_0 = \bar Y - b_1\bar X$ of [3.3.2](/3.3.2), since $n\sum X_i^2 - (\sum X_i)^2 = n\sum(X_i - \bar X)^2$.

The vector of fitted (predicted) responses and the vector of residuals are

$$
\hat{\boldsymbol{Y}} = X\boldsymbol{b} = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y} = H\boldsymbol{Y}, \qquad \boldsymbol{e} = \boldsymbol{Y} - \hat{\boldsymbol{Y}} = \boldsymbol{Y} - H\boldsymbol{Y} = (I_n - H)\boldsymbol{Y},
$$
where $H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$ is the hat matrix (projection matrix) of Section 7.3.

### 7.1.4. Least Squares: The Geometric Approach

Write the design matrix by columns, $X = [\boldsymbol{1}_n \mid \boldsymbol{x}]$ with $\boldsymbol{x} = (X_1, \dots, X_n)^{\mathsf T}$. Then

$$
\hat{\boldsymbol{Y}} = X\boldsymbol{b} = b_0\boldsymbol{1}_n + b_1\boldsymbol{x}
$$
is a linear combination of the columns of $X$: it lies in the **column space** $\mathcal{R}(X)$ (also written $C(X)$ or $\operatorname{Im}X$), the subspace of $\mathbb{R}^n$ spanned by the columns. An $n \times p$ matrix maps $\mathbb{R}^p$ to $\mathbb{R}^n$, $\boldsymbol{\beta} \mapsto X\boldsymbol{\beta}$; with $n = 3$ observations and $p = 2$ columns, $X$ maps the plane $\mathbb{R}^2$ of coefficient vectors onto a plane through the origin inside $\mathbb{R}^3$.

The four fundamental subspaces of an $n \times p$ matrix $A$ of rank $r$ ([2.1.3](/2.1.3), [2.1.4](/2.1.4)) organize this picture:

| Subspace | Lies in | Dimension | Orthogonal complement |
|---|---|---|---|
| column space $\mathcal{R}(A)$ | $\mathbb{R}^n$ | $r$ | left null space $\mathcal{N}(A^{\mathsf T})$, dimension $n - r$ |
| row space $\mathcal{R}(A^{\mathsf T})$ | $\mathbb{R}^p$ | $r$ | null space $\mathcal{N}(A)$, dimension $p - r$ |

$A$ maps $\mathbb{R}^p$ onto $\mathcal{R}(A)$ and $A^{\mathsf T}$ maps $\mathbb{R}^n$ onto $\mathcal{R}(A^{\mathsf T})$; every vector of $\mathbb{R}^n$ is the sum of a vector in $\mathcal{R}(A)$ and an orthogonal vector in $\mathcal{N}(A^{\mathsf T})$.

The least squares problem can therefore be reformulated as

$$
\min_{\boldsymbol{\beta} \in \mathbb{R}^2}\|\boldsymbol{Y} - X\boldsymbol{\beta}\|^2 = \min_{\boldsymbol{v} = X\boldsymbol{\beta}}\|\boldsymbol{Y} - \boldsymbol{v}\|^2 = \min_{\boldsymbol{v} \in \mathcal{R}(X)}\|\boldsymbol{Y} - \boldsymbol{v}\|^2,
$$
the problem of finding the point of the column space closest to $\boldsymbol{Y}$. By the best approximation theorem ([2.1.4](/2.1.4)), the minimizer is the **orthogonal projection** of $\boldsymbol{Y}$ onto $\mathcal{R}(X)$, $\hat{\boldsymbol{Y}} = P\boldsymbol{Y}$, where $P$ is the **orthogonal projection matrix** onto $\mathcal{R}(X)$; by the Pythagorean theorem every other $\boldsymbol{v} \in \mathcal{R}(X)$ is farther from $\boldsymbol{Y}$. The residual is orthogonal to the column space, $\boldsymbol{e} \in \mathcal{N}(X^{\mathsf T})$:

$$
X^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{b}) = X^{\mathsf T}\boldsymbol{e} = \boldsymbol{0}, \qquad\text{that is,}\qquad \boldsymbol{1}_n^{\mathsf T}\boldsymbol{e} = 0, \quad \boldsymbol{x}^{\mathsf T}\boldsymbol{e} = 0.
$$
These are the normal equations again, one for each column, and they give $\boldsymbol{b} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ and

$$
P\boldsymbol{Y} = X\boldsymbol{b} = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}, \qquad P = H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}.
$$
The projection matrix is symmetric and idempotent ($P^2 = P$), the residuals and the fitted values are orthogonal, $\boldsymbol{e}^{\mathsf T}\hat{\boldsymbol{Y}} = 0$, and $\boldsymbol{1}_n^{\mathsf T}\boldsymbol{e} = 0$ says that the residuals sum to zero. (A picture of the projection for $n = 3$ is in [3.4.7](/3.4.7).)

### 7.1.5. Sampling Distribution

**Theorem 7.1.3** In the simple linear regression model, $\boldsymbol{b} \sim \mathcal{N}_2\big(\boldsymbol{\beta}, \sigma^2(X^{\mathsf T}X)^{-1}\big)$. The estimated covariance matrix of $\boldsymbol{b}$ is

$$
s^2\{\boldsymbol{b}\} = s^2(X^{\mathsf T}X)^{-1}, \qquad s^2 = \frac{\boldsymbol{e}^{\mathsf T}\boldsymbol{e}}{n - 2} = \frac{\boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}}{n - 2}.
$$

**Proof** $\boldsymbol{Y} \sim \mathcal{N}_n(X\boldsymbol{\beta}, \sigma^2I_n)$ and $\boldsymbol{b} = D\boldsymbol{Y}$ with $D = (X^{\mathsf T}X)^{-1}X^{\mathsf T}$. By (N1), $\boldsymbol{b}$ is normal with mean $DX\boldsymbol{\beta} = \boldsymbol{\beta}$ and covariance $\sigma^2DD^{\mathsf T} = \sigma^2(X^{\mathsf T}X)^{-1}X^{\mathsf T}X(X^{\mathsf T}X)^{-1} = \sigma^2(X^{\mathsf T}X)^{-1}$. That $\boldsymbol{e}^{\mathsf T}\boldsymbol{e} = \boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}$ follows from $(I_n - H)^{\mathsf T}(I_n - H) = I_n - H$. $\square$

With the inverse computed above, the entries of $\sigma^2(X^{\mathsf T}X)^{-1}$ are the familiar formulas of [3.3.3](/3.3.3):

$$
\operatorname{Var}(b_0) = \sigma^2\left[\frac1n + \frac{\bar X^2}{\sum(X_i - \bar X)^2}\right], \qquad \operatorname{Var}(b_1) = \frac{\sigma^2}{\sum(X_i - \bar X)^2}, \qquad \operatorname{Cov}(b_0, b_1) = -\frac{\bar X\sigma^2}{\sum(X_i - \bar X)^2}.
$$

This framework carries over to multiple regression without change: adding another explanatory variable is adding another column to the design matrix $X$.

## 7.2. The Multiple Linear Regression Model

### 7.2.1. Data and Notation

The cases are still denoted by $i = 1, \dots, n$; the data are

$$
\{(Y_i;\ X_{i1}, X_{i2}, \dots, X_{i,p-1})\}_{1 \le i \le n},
$$
where $Y_i$ is the response and $X_{i1}, \dots, X_{i,p-1}$ are the values of the $p - 1$ explanatory (predictor) variables for the $i$-th case. Throughout the course, $p$ denotes the number of regression parameters including the intercept, so there are $p - 1$ predictors, and for simple linear regression $p = 2$. (This agrees with [3.4.7](/3.4.7); in [3.2.3](/3.2.3) $p$ counts the predictors only.) The design matrix

$$
X = \begin{bmatrix}1 & X_{11} & X_{12} & \cdots & X_{1,p-1}\\1 & X_{21} & X_{22} & \cdots & X_{2,p-1}\\\vdots & \vdots & \vdots & & \vdots\\1 & X_{n1} & X_{n2} & \cdots & X_{n,p-1}\end{bmatrix} = \big[\boldsymbol{1}_n \mid \boldsymbol{x}_1 \mid \cdots \mid \boldsymbol{x}_{p-1}\big] = \begin{bmatrix}\boldsymbol{x}_{(1)}^{\mathsf T}\\\boldsymbol{x}_{(2)}^{\mathsf T}\\\vdots\\\boldsymbol{x}_{(n)}^{\mathsf T}\end{bmatrix}
$$
can be read by columns, $\boldsymbol{x}_k = (X_{1k}, \dots, X_{nk})^{\mathsf T}$ being the values of the $k$-th predictor, or by rows, $\boldsymbol{x}_{(i)}^{\mathsf T} = (1, X_{i1}, \dots, X_{i,p-1})$ being the $i$-th case.

### 7.2.2. The Model and Its Parameters

**Definition 7.2.1 (Multiple Linear Regression Model)** The **multiple linear regression model** is

$$
Y_i = \beta_0 + \beta_1X_{i1} + \beta_2X_{i2} + \cdots + \beta_{p-1}X_{i,p-1} + \varepsilon_i, \qquad i = 1, \dots, n,
$$
where $\varepsilon_1, \dots, \varepsilon_n$ are independent normal random errors with mean $0$ and variance $\sigma^2$. In matrix form, with $\boldsymbol{Y} = (Y_1, \dots, Y_n)^{\mathsf T}$, the $n \times p$ design matrix $X$, $\boldsymbol{\beta} = (\beta_0, \beta_1, \dots, \beta_{p-1})^{\mathsf T}$ and $\boldsymbol{\varepsilon} = (\varepsilon_1, \dots, \varepsilon_n)^{\mathsf T}$,

$$
\boldsymbol{Y}_{n\times1} = X_{n\times p}\boldsymbol{\beta}_{p\times1} + \boldsymbol{\varepsilon}_{n\times1}, \qquad \boldsymbol{\varepsilon} \sim \mathcal{N}_n(\boldsymbol{0}, \sigma^2I_n), \qquad \boldsymbol{Y} \sim \mathcal{N}_n(X\boldsymbol{\beta}, \sigma^2I_n).
$$

The parameters are the intercept $\beta_0$, the regression coefficients $\beta_1, \dots, \beta_{p-1}$ of the explanatory variables, and the error variance $\sigma^2$. Notice the switch of terminology from "slope" to "regression coefficient".

**Definition 7.2.2 (Partial Regression Coefficient)** In the multiple linear regression model, $\beta_k$ ($1 \le k \le p - 1$) is the change in the mean response $\mathbb{E}(Y)$ per unit increase in $X_k$ when the other predictors $X_1, \dots, X_{k-1}, X_{k+1}, \dots, X_{p-1}$ are held constant. The $\beta_k$ are therefore also called **partial regression coefficients**: they reflect the partial effect of one predictor when the other predictors are included in the model and held constant.

A partial regression coefficient generally differs from the slope of the simple regression of $Y$ on $X_k$ alone, which also absorbs the effects of predictors correlated with $X_k$; and it changes when predictors are added to or removed from the model. Its interpretation also requires that the combination of predictor values considered lies within the scope of the model, the region of predictor values jointly covered by the data: when predictors are correlated, holding one fixed while changing another may lead outside that region.

### 7.2.3. Special Cases

The model is linear in the parameters, and the predictors may be functions of the original variables. Several important models are special cases.

- The polynomial model of order $p - 1$, $Y_i = \beta_0 + \beta_1X_i + \beta_2X_i^2 + \cdots + \beta_{p-1}X_i^{p-1} + \varepsilon_i$, takes the powers of one variable as predictors.
- Interactions between explanatory variables can be represented by their products (crossed terms) and included in the model.
- Some explanatory variables can be indicator variables. A *dummy variable* is a predictor that takes the values $0$ and $1$ (or other distinct numbers) to code the categories of a qualitative variable.

These models are developed in [3.3.10](/3.3.10); one example shows how much a single linear model can express.

**Example 7.2.1 (Children's Height)** The response is height $Y$, and the two explanatory variables are age in months $X_1$ and gender $X_2$, a dummy variable with $X_2 = 0$ for a girl and $X_2 = 1$ for a boy. Consider

$$
Y_i = \beta_0 + \beta_1X_{i1} + \beta_2X_{i2} + \beta_3X_{i1}X_{i2} + \varepsilon_i.
$$
If child $i$ is a girl ($X_{i2} = 0$), $Y_i = \beta_0 + \beta_1X_{i1} + \varepsilon_i$; if child $i$ is a boy ($X_{i2} = 1$), $Y_i = (\beta_0 + \beta_2) + (\beta_1 + \beta_3)X_{i1} + \varepsilon_i$. One model represents two different regression lines of $Y$ against $X_1$, for girls and for boys: $\beta_2$ is the difference of the intercepts and $\beta_3$, the coefficient of the interaction, the difference of the slopes.

![Simulated heights of 40 girls and 40 boys against age in months, with the two regression lines given by a single model with a gender dummy variable and an age-by-gender interaction](./plots/dummy-interaction.py)

## 7.3. Estimation

### 7.3.1. Least Squares

The analytic approach is the same as in Section 7.1: minimizing $Q(\boldsymbol{\beta}) = \|\boldsymbol{Y} - X\boldsymbol{\beta}\|^2$ over $\boldsymbol{\beta} \in \mathbb{R}^p$ leads to the normal equations $X^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{\beta}) = \boldsymbol{0}$ and Hessian $2X^{\mathsf T}X$. Under the condition $\operatorname{rank}(X) = p$ (the columns of $X$ are linearly independent), the minimizer exists and is unique,

$$
\boldsymbol{b} = \hat{\boldsymbol{\beta}} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$
Geometrically, $\hat{\boldsymbol{Y}} = X\boldsymbol{b} = b_0\boldsymbol{1}_n + b_1\boldsymbol{x}_1 + \cdots + b_{p-1}\boldsymbol{x}_{p-1}$ is the orthogonal projection of $\boldsymbol{Y}$ onto the $p$-dimensional column space $\mathcal{R}(X) \subseteq \mathbb{R}^n$, and the residual $\boldsymbol{e}$ is orthogonal to every column.

**Definition 7.3.1 (Hat Matrix)** The $n \times n$ matrix

$$
H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}
$$
is called the **hat matrix** (also the projection matrix or influence matrix), because it maps the responses to the fitted values, $\hat{\boldsymbol{Y}} = X\boldsymbol{b} = H\boldsymbol{Y}$; the residuals are $\boldsymbol{e} = \boldsymbol{Y} - \hat{\boldsymbol{Y}} = (I_n - H)\boldsymbol{Y}$.

It can be shown directly that $H$ is symmetric and idempotent, $H^{\mathsf T} = H = H^2$, and $HX = X$, $(I_n - H)X = O$; so $H$ is the orthogonal projection matrix onto $\mathcal{R}(X)$ and $I_n - H$ the one onto its orthogonal complement. Consequently the residuals and the fitted values are orthogonal, $\boldsymbol{e}^{\mathsf T}\hat{\boldsymbol{Y}} = \boldsymbol{Y}^{\mathsf T}(I_n - H)H\boldsymbol{Y} = 0$, and the degrees of freedom of the residuals are $\mathrm{df}_E = \operatorname{rank}(I_n - H) = n - p$ (Section 7.3.3).

The error sum of squares, its degrees of freedom and the mean squared error are

$$
\mathrm{SSE} = \boldsymbol{e}^{\mathsf T}\boldsymbol{e} = (\boldsymbol{Y} - X\boldsymbol{b})^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{b}) = \boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}, \qquad \mathrm{df}_E = n - p, \qquad \mathrm{MSE} = \frac{\mathrm{SSE}}{\mathrm{df}_E} = \frac{\boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}}{n - p},
$$
and the estimators of $\sigma^2$ and $\sigma$ are $s^2 = \mathrm{MSE}$ and $s = \sqrt{\mathrm{MSE}}$.

**Theorem 7.3.1 (Sampling Distributions)** In the multiple linear regression model with $\operatorname{rank}(X) = p$:

1. $\boldsymbol{b} \sim \mathcal{N}_p\big(\boldsymbol{\beta}, \sigma^2(X^{\mathsf T}X)^{-1}\big)$: $\boldsymbol{b}$ is unbiased, $\mathbb{E}(\boldsymbol{b}) = \boldsymbol{\beta}$, with covariance matrix $\operatorname{Cov}(\boldsymbol{b}) = \sigma^2(X^{\mathsf T}X)^{-1}$, estimated by $s^2\{\boldsymbol{b}\} = \mathrm{MSE}\,(X^{\mathsf T}X)^{-1}$;
2. $\boldsymbol{e} \sim \mathcal{N}_n\big(\boldsymbol{0}, \sigma^2(I_n - H)\big)$, and $\boldsymbol{e}$ is independent of $\boldsymbol{b}$;
3. $\mathrm{SSE}/\sigma^2 \sim \chi^2_{n-p}$, independent of $\boldsymbol{b}$; in particular $\mathbb{E}(\mathrm{MSE}) = \sigma^2$.

**Proof** (1) is proved exactly as Theorem 7.1.3. For (2), $\boldsymbol{e} = (I_n - H)\boldsymbol{Y} = (I_n - H)\boldsymbol{\varepsilon}$ because $(I_n - H)X = O$, so by (N1) it is normal with mean $\boldsymbol{0}$ and covariance $\sigma^2(I_n - H)(I_n - H)^{\mathsf T} = \sigma^2(I_n - H)$. With $\boldsymbol{b} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$, condition (N4) holds: $(X^{\mathsf T}X)^{-1}X^{\mathsf T}(I_n - H) = O$ since $X^{\mathsf T}H = X^{\mathsf T}$. For (3), write the symmetric idempotent matrix of rank $n - p$ as $I_n - H = QQ^{\mathsf T}$ with $Q \in \mathbb{R}^{n\times(n-p)}$ having orthonormal columns. Then $Q^{\mathsf T}\boldsymbol{\varepsilon}/\sigma \sim \mathcal{N}_{n-p}(\boldsymbol{0}, I_{n-p})$ and $\mathrm{SSE}/\sigma^2 = \boldsymbol{\varepsilon}^{\mathsf T}(I_n - H)\boldsymbol{\varepsilon}/\sigma^2 = \|Q^{\mathsf T}\boldsymbol{\varepsilon}/\sigma\|^2 \sim \chi^2_{n-p}$; it is a function of $\boldsymbol{e}$, hence independent of $\boldsymbol{b}$. $\square$

### 7.3.2. The Gauss–Markov Theorem

Theorem 7.3.1 gives the covariance matrix of $\boldsymbol{b}$; in which sense is it optimal? The answer requires only assumptions on the first two moments. The Gauss–Markov conditions are:

1. Linearity: the model is linear in the parameters, $\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$.
2. Randomness: the data have been randomly sampled from the population, so that the errors of different cases are uncorrelated.
3. Non-collinearity: the regressors are not perfectly correlated with each other, $\operatorname{rank}(X) = p$.
4. Exogeneity: the regressors are not correlated with the error term, $\mathbb{E}(\boldsymbol{\varepsilon} \mid X) = \boldsymbol{0}$.
5. Homoscedasticity: whatever the values of the regressors, the variance of the error is constant.

Together, conditions 2, 4 and 5 say $\mathbb{E}(\boldsymbol{\varepsilon}) = \boldsymbol{0}$ and $\operatorname{Cov}(\boldsymbol{\varepsilon}) = \sigma^2I_n$ (given $X$). Normality is not needed.

**Theorem 7.3.2 (Gauss–Markov Theorem)** Under the Gauss–Markov conditions, the ordinary least squares estimator $\boldsymbol{b}$ is the best linear unbiased estimator (BLUE) of $\boldsymbol{\beta}$: for every estimator $\tilde{\boldsymbol{\beta}} = A\boldsymbol{Y}$, with $A$ a constant $p \times n$ matrix, that is unbiased for every $\boldsymbol{\beta}$, the matrix $\operatorname{Cov}(\tilde{\boldsymbol{\beta}}) - \operatorname{Cov}(\boldsymbol{b})$ is positive semidefinite. In particular $\operatorname{Var}(\boldsymbol{c}^{\mathsf T}\tilde{\boldsymbol{\beta}}) \ge \operatorname{Var}(\boldsymbol{c}^{\mathsf T}\boldsymbol{b})$ for every $\boldsymbol{c} \in \mathbb{R}^p$, and each $\tilde\beta_k$ has variance at least $\operatorname{Var}(b_k)$.

**Proof** Write $A = (X^{\mathsf T}X)^{-1}X^{\mathsf T} + D$, so that $\tilde{\boldsymbol{\beta}} = D\boldsymbol{Y} + \boldsymbol{b}$. Unbiasedness for every $\boldsymbol{\beta}$ means

$$
\mathbb{E}(\tilde{\boldsymbol{\beta}}) = \mathbb{E}(D\boldsymbol{Y} + \boldsymbol{b}) = DX\boldsymbol{\beta} + \boldsymbol{\beta} = \boldsymbol{\beta} \quad\text{for all }\boldsymbol{\beta}, \qquad\text{so}\qquad DX = O.
$$
Then

$$
\begin{aligned}
\operatorname{Cov}(\tilde{\boldsymbol{\beta}}) &= \operatorname{Cov}\big(D\boldsymbol{\varepsilon} + (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{\varepsilon}\big) = \sigma^2\big\{D + (X^{\mathsf T}X)^{-1}X^{\mathsf T}\big\}\big\{D + (X^{\mathsf T}X)^{-1}X^{\mathsf T}\big\}^{\mathsf T} \\
&= \sigma^2\big\{DD^{\mathsf T} + (X^{\mathsf T}X)^{-1} + DX(X^{\mathsf T}X)^{-1} + (X^{\mathsf T}X)^{-1}X^{\mathsf T}D^{\mathsf T}\big\} = \sigma^2\big\{DD^{\mathsf T} + (X^{\mathsf T}X)^{-1}\big\},
\end{aligned}
$$
because the two cross terms vanish by $DX = O$. Since $DD^{\mathsf T}$ is positive semidefinite, $\operatorname{Cov}(\tilde{\boldsymbol{\beta}}) \succeq \sigma^2(X^{\mathsf T}X)^{-1} = \operatorname{Cov}(\boldsymbol{b})$. $\square$

This is the **Gauss–Markov theorem** of [3.2.3](/3.2.3) in the present notation. It explains the remark of [3.3.5](/3.3.5): under heteroscedasticity (condition 5 fails) least squares remains unbiased but is no longer best. It also has a limitation. "Best" refers only to linear unbiased estimators, and the natural criterion for comparing estimators is the **mean squared error** $\mathbb{E}\big[(\tilde\beta - \beta)^2\big] = \operatorname{Var}(\tilde\beta) + (\text{bias})^2$, the **bias–variance trade-off** ([3.2.3](/3.2.3)). A biased estimator with a much smaller variance can be preferable in practice, which is the idea behind **ridge regression** ([3.4.7](/3.4.7)); an unbiased estimator with a larger variance than OLS never is.

![Sampling densities of three rival estimators of beta: a biased estimator with small variance, the OLS estimator (unbiased with the smallest variance among linear unbiased estimators) and an unbiased estimator with larger variance; the legend gives their mean squared errors](./plots/rival-estimators.py)

### 7.3.3. The Hat Matrix and Leverage

The hat matrix $H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$, the projection matrix or influence matrix, maps the vector of responses to the vector of fitted values, $\hat{\boldsymbol{Y}} = H\boldsymbol{Y}$. Its entries describe the influence that each response value has on each fitted value,

$$
\hat Y_i = \sum_{j=1}^n h_{ij}Y_j, \qquad h_{ij} = \frac{\partial\hat Y_i}{\partial Y_j} = \boldsymbol{x}_{(i)}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_{(j)},
$$
and its diagonal elements $h_{ii} = \partial\hat Y_i/\partial Y_i = \boldsymbol{x}_{(i)}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_{(i)}$ are the **leverages** of [3.3.6](/3.3.6): the influence of each response value on the fitted value for that same observation.

**Proposition 7.3.1** $0 \le h_{ii} \le 1$ and $\sum_{i=1}^n h_{ii} = \operatorname{tr}(H) = p$. If the model contains an intercept, $h_{ii} \ge 1/n$.

**Proof** Since $H$ is symmetric and idempotent, $h_{ii} = (H^2)_{ii} = \sum_jh_{ij}^2 = h_{ii}^2 + \sum_{j\ne i}h_{ij}^2 \ge 0$, and then $h_{ii} \ge h_{ii}^2$ gives $h_{ii} \le 1$. By the cyclic property of the trace, $\operatorname{tr}(H) = \operatorname{tr}\big((X^{\mathsf T}X)^{-1}X^{\mathsf T}X\big) = \operatorname{tr}(I_p) = p$. If $\boldsymbol{1}_n \in \mathcal{R}(X)$, then $H\boldsymbol{1}_n = \boldsymbol{1}_n$, so $H - \frac1nJ$ with $J = \boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$ is again symmetric and idempotent, hence positive semidefinite, and its diagonal entries $h_{ii} - 1/n$ are nonnegative. $\square$

The average leverage is $p/n$. For simple linear regression, $\boldsymbol{x}_{(i)}^{\mathsf T} = (1, X_i)$ and the inverse of Section 7.1.3 give

$$
h_{ii} = \frac{\sum_jX_j^2 + nX_i^2 - 2X_i\sum_jX_j}{n\sum_jX_j^2 - (\sum_jX_j)^2} = \frac{\big(\sum_jX_j^2 - n\bar X^2\big) + n(X_i - \bar X)^2}{n\big(\sum_jX_j^2 - n\bar X^2\big)} = \frac1n + \frac{(X_i - \bar X)^2}{\sum_{j=1}^n(X_j - \bar X)^2},
$$
in agreement with Proposition 6.1.1. Why is the leverage a distance? In general it measures the distance between $\boldsymbol{x}_{(i)}$ and the center of the predictor values in terms of the shape (the density) of the sample: all points on the same contour of the scatter of the predictors have the same leverage.

**Proposition 7.3.2 (Leverage and Mahalanobis Distance)** Suppose the model has an intercept, write $\boldsymbol{x}_{(i)}^{\mathsf T} = (1, \boldsymbol{z}_i^{\mathsf T})$ with $\boldsymbol{z}_i \in \mathbb{R}^{p-1}$ the predictor values of case $i$, and let $\bar{\boldsymbol{z}}$ and $S$ be the sample mean vector and sample covariance matrix of $\boldsymbol{z}_1, \dots, \boldsymbol{z}_n$. Then

$$
h_{ii} = \frac1n + \frac{D^2(\boldsymbol{z}_i, \bar{\boldsymbol{z}})}{n - 1}, \qquad\text{i.e.}\qquad D^2(\boldsymbol{z}_i, \bar{\boldsymbol{z}}) = (n - 1)\Big(h_{ii} - \frac1n\Big),
$$
where $D^2(\boldsymbol{z}, \bar{\boldsymbol{z}}) = (\boldsymbol{z} - \bar{\boldsymbol{z}})^{\mathsf T}S^{-1}(\boldsymbol{z} - \bar{\boldsymbol{z}})$ is the squared **Mahalanobis distance** ([3.4.1](/3.4.1)).

**Proof** Let $Z_c$ be the $n \times (p - 1)$ matrix with rows $(\boldsymbol{z}_i - \bar{\boldsymbol{z}})^{\mathsf T}$. Subtracting multiples of the column $\boldsymbol{1}_n$ does not change the column space, so $\mathcal{R}(X) = \mathcal{R}([\boldsymbol{1}_n \mid Z_c])$, and the two blocks are orthogonal, $\boldsymbol{1}_n^{\mathsf T}Z_c = \boldsymbol{0}^{\mathsf T}$. The projection onto the sum of two orthogonal subspaces is the sum of the projections, so

$$
H = \frac1nJ + Z_c(Z_c^{\mathsf T}Z_c)^{-1}Z_c^{\mathsf T}, \qquad h_{ii} = \frac1n + (\boldsymbol{z}_i - \bar{\boldsymbol{z}})^{\mathsf T}(Z_c^{\mathsf T}Z_c)^{-1}(\boldsymbol{z}_i - \bar{\boldsymbol{z}}),
$$
and $Z_c^{\mathsf T}Z_c = (n - 1)S$. $\square$

With several predictors, a case can thus have high leverage although none of its predictor values is extreme on its own: what counts is the distance in the metric of the predictors' covariance, so a case that breaks their correlation pattern is far from the center.

![Leverage contours for a regression on two correlated predictors: the curves of constant h_ii are ellipses following the shape of the scatter, and a point that is not extreme in either predictor separately but lies against the correlation has the largest leverage](./plots/leverage-contours.py)

The degrees of freedom of a sum of squares are the rank of the matrix of its quadratic form: the degrees of freedom of $\boldsymbol{Y}^{\mathsf T}A\boldsymbol{Y}$ are $\operatorname{rank}(A)$. For an idempotent matrix $A$ the eigenvalues are only $0$ or $1$, so $\operatorname{rank}(A) = \operatorname{tr}(A) = \sum\lambda_i$. With $H$ idempotent, $I_n - H$ is also idempotent, $(I_n - H)^2 = I_n - H$, and by Lemma 7.1.1 or directly,

$$
\mathrm{df}(\mathrm{SSE}) = \operatorname{rank}(I_n - H) = \operatorname{tr}(I_n - H) = n - \operatorname{tr}(H) = n - p.
$$

**Proposition 7.3.3 (Covariance Matrix of the Residuals)** The eigenvalues of $I_n - H$ are $1$ or $0$, and

$$
\operatorname{Cov}(\boldsymbol{e}) = \operatorname{Cov}\big((I_n - H)\boldsymbol{Y}\big) = (I_n - H)\,\sigma^2I_n\,(I_n - H)^{\mathsf T} = \sigma^2(I_n - H), \qquad\text{so}\qquad \operatorname{Var}(e_i) = \sigma^2(1 - h_{ii}), \quad \operatorname{Cov}(e_i, e_j) = -\sigma^2h_{ij}\ (i \ne j).
$$

The random errors $\boldsymbol{\varepsilon}$ are not the residuals $\boldsymbol{e}$! Even when the errors satisfy the equal variance assumption, the residuals do not have equal variances: a residual is smaller in variance the larger the leverage of its case. In simple linear regression the cases with $X_i$ at either end of the range have the largest $h_{ii}$, so the fitted line follows the data there most closely and their residuals have the smallest variances; the residuals in the middle vary most. This is the reason for the standardized and studentized residuals of [3.3.6](/3.3.6).

Does this dependence among the residuals affect a normality test, which treats $e_1, \dots, e_n$ as an iid sample? With an intercept, $\sum_ie_i = 0$, so

$$
0 = \operatorname{Var}\Big(\sum_{i=1}^ne_i\Big) = \sum_{i=1}^n\operatorname{Var}(e_i) + \sum_{i\ne j}\operatorname{Cov}(e_i, e_j) = \sigma^2\big(n - \operatorname{tr}(H)\big) + n(n - 1)\,\overline{\operatorname{Cov}(e_i, e_j)},
$$
where the bars denote averages over $i$ and over the pairs $i \ne j$. Hence

$$
\overline{\operatorname{Var}(e_i)} = \sigma^2\Big(1 - \frac pn\Big), \qquad \overline{\operatorname{Cov}(e_i, e_j)} = -\frac{\sigma^2(1 - p/n)}{n - 1}, \qquad \overline{\operatorname{Corr}(e_i, e_j)} \approx -\frac{1}{n - 1} \approx 0.
$$
In practice this makes little difference as long as $p/n$ is small. A test that is often applied to residuals, especially in econometrics, is the *Jarque–Bera test*, a Lagrange multiplier (score) test that uses the sample skewness $S$ and the sample kurtosis $K = m_4/m_2^2$ of the residuals:

$$
\mathrm{JB} = \frac n6\left(S^2 + \frac14(K - 3)^2\right) \overset{\cdot}{\sim} \chi^2_2
$$
under normality, for large $n$. For small samples or dependent data its $\chi^2$ approximation is poor, and bootstrap versions are used.

## 7.4. Analysis of Variance

### 7.4.1. Sums of Squares and Degrees of Freedom

The sources of variation are the same as in [3.3.4](/3.3.4): regression (called model in SAS), error (called residual in R) and total, and the sums of squares and degrees of freedom add up as before. With $\boldsymbol{1}_n$ the vector of ones,

$$
\mathrm{SSR} = \sum_{i=1}^n(\hat Y_i - \bar Y)^2 = (\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n), \qquad \mathrm{SSE} = \sum_{i=1}^n(Y_i - \hat Y_i)^2 = (\boldsymbol{Y} - \hat{\boldsymbol{Y}})^{\mathsf T}(\boldsymbol{Y} - \hat{\boldsymbol{Y}}),
$$

$$
\mathrm{SSTO} = \sum_{i=1}^n(Y_i - \bar Y)^2 = (\boldsymbol{Y} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\boldsymbol{Y} - \bar Y\boldsymbol{1}_n).
$$
(Some texts and software write SSM for $\mathrm{SSR}$, SST for $\mathrm{SSTO}$, and RSS for $\mathrm{SSE}$.)

**Proposition 7.4.1** Let $J = \boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$ be the $n \times n$ matrix of ones. If the model contains an intercept,

$$
\mathrm{SSTO} = \boldsymbol{Y}^{\mathsf T}\Big(I_n - \frac1nJ\Big)\boldsymbol{Y}, \qquad \mathrm{SSR} = \boldsymbol{Y}^{\mathsf T}\Big(H - \frac1nJ\Big)\boldsymbol{Y}, \qquad \mathrm{SSE} = \boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y},
$$
the three matrices are symmetric and idempotent with ranks $n - 1$, $p - 1$ and $n - p$, and

$$
\mathrm{SSTO} = \mathrm{SSR} + \mathrm{SSE}, \qquad \mathrm{df}_T = n - 1 = \mathrm{df}_R + \mathrm{df}_E = (p - 1) + (n - p).
$$

**Proof** Since $\bar Y = \frac1n\boldsymbol{1}_n^{\mathsf T}\boldsymbol{Y} = \frac1n\boldsymbol{Y}^{\mathsf T}\boldsymbol{1}_n$,

$$
\mathrm{SSTO} = \boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} - 2\bar Y\boldsymbol{Y}^{\mathsf T}\boldsymbol{1}_n + \boldsymbol{1}_n^{\mathsf T}\boldsymbol{1}_n\bar Y^2 = \boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} - \frac2n\boldsymbol{Y}^{\mathsf T}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}\boldsymbol{Y} + \frac1n\boldsymbol{Y}^{\mathsf T}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}\boldsymbol{Y} = \boldsymbol{Y}^{\mathsf T}\Big(I_n - \frac1nJ\Big)\boldsymbol{Y}.
$$
$\frac1nJ$ is idempotent of rank $1$ (the projection onto $\operatorname{span}(\boldsymbol{1}_n)$), so $I_n - \frac1nJ$ is idempotent of rank $n - 1$. Next, $\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n = (H - \frac1nJ)\boldsymbol{Y}$, and because $\boldsymbol{1}_n \in \mathcal{R}(X)$ we have $HJ = JH = J$, so $(H - \frac1nJ)^2 = H - \frac1nJ$ with rank $\operatorname{tr}(H) - \operatorname{tr}(\frac1nJ) = p - 1$. Finally,

$$
(\boldsymbol{Y} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\boldsymbol{Y} - \bar Y\boldsymbol{1}_n) = (\boldsymbol{Y} - \hat{\boldsymbol{Y}} + \hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\boldsymbol{Y} - \hat{\boldsymbol{Y}} + \hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n) = (\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n) + (\boldsymbol{Y} - \hat{\boldsymbol{Y}})^{\mathsf T}(\boldsymbol{Y} - \hat{\boldsymbol{Y}}),
$$
because the cross term is $\boldsymbol{e}^{\mathsf T}(\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n) = 0$ by $\boldsymbol{e}^{\mathsf T}\hat{\boldsymbol{Y}} = 0$ and $\boldsymbol{e}^{\mathsf T}\boldsymbol{1}_n = 0$. $\square$

The mean squares are $\mathrm{MSTO} = \mathrm{SSTO}/\mathrm{df}_T$, $\mathrm{MSR} = \mathrm{SSR}/\mathrm{df}_R$ and $\mathrm{MSE} = \mathrm{SSE}/\mathrm{df}_E$.

| Source | SS | df | MS | $F$ |
|---|---|---|---|---|
| Regression | $\mathrm{SSR} = \sum(\hat Y_i - \bar Y)^2$ | $p - 1$ | $\mathrm{MSR} = \mathrm{SSR}/(p - 1)$ | $\mathrm{MSR}/\mathrm{MSE}$ |
| Error | $\mathrm{SSE} = \sum(Y_i - \hat Y_i)^2$ | $n - p$ | $\mathrm{MSE} = \mathrm{SSE}/(n - p)$ | |
| Total | $\mathrm{SSTO} = \sum(Y_i - \bar Y)^2$ | $n - 1$ | $\mathrm{MSTO} = \mathrm{SSTO}/(n - 1)$ | |

### 7.4.2. Expected Mean Squares and the F-Test

**Proposition 7.4.2 (Expected Mean Squares)** In the multiple linear regression model,

$$
\mathbb{E}(\mathrm{MSE}) = \sigma^2, \qquad \mathbb{E}(\mathrm{MSR}) = \sigma^2 + \frac{1}{p - 1}(X\boldsymbol{\beta})^{\mathsf T}\Big(I_n - \frac1nJ\Big)X\boldsymbol{\beta}.
$$
Under the good design $\operatorname{rank}(X) = p$, the quadratic form $(X\boldsymbol{\beta})^{\mathsf T}(I_n - \frac1nJ)X\boldsymbol{\beta}$ is $0$ if and only if $\beta_1 = \beta_2 = \cdots = \beta_{p-1} = 0$, and positive when at least one $\beta_k \ne 0$.

**Proof** Since $(I_n - H)X = O$, $\mathrm{MSE} = \boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}/(n - p) = \boldsymbol{\varepsilon}^{\mathsf T}(I_n - H)\boldsymbol{\varepsilon}/(n - p)$, and by Theorem 7.1.2

$$
\mathbb{E}(\mathrm{MSE}) = \frac{\mathbb{E}\big(\boldsymbol{\varepsilon}^{\mathsf T}(I_n - H)\boldsymbol{\varepsilon}\big)}{n - p} = \frac{\operatorname{tr}\big[(I_n - H)(\sigma^2I_n)\big]}{n - p} = \sigma^2.
$$
For $\mathrm{SSR} = \boldsymbol{Y}^{\mathsf T}(H - \frac1nJ)\boldsymbol{Y}$ with $\boldsymbol{Y} \sim \mathcal{N}(X\boldsymbol{\beta}, \sigma^2I_n)$, Theorem 7.1.2 gives

$$
\mathbb{E}\Big[\boldsymbol{Y}^{\mathsf T}\Big(H - \frac1nJ\Big)\boldsymbol{Y}\Big] = (X\boldsymbol{\beta})^{\mathsf T}\Big(H - \frac1nJ\Big)(X\boldsymbol{\beta}) + \sigma^2\operatorname{tr}\Big(H - \frac1nJ\Big),
$$
where $\operatorname{tr}(H - \frac1nJ) = \operatorname{rank}(H) - \operatorname{rank}(\frac1nJ) = p - 1$, and, since $HX = X$,

$$
(X\boldsymbol{\beta})^{\mathsf T}\Big(H - \frac1nJ\Big)(X\boldsymbol{\beta}) = \boldsymbol{\beta}^{\mathsf T}\Big(X^{\mathsf T}HX - \frac1nX^{\mathsf T}JX\Big)\boldsymbol{\beta} = \boldsymbol{\beta}^{\mathsf T}\Big(X^{\mathsf T}X - \frac1nX^{\mathsf T}JX\Big)\boldsymbol{\beta} = (X\boldsymbol{\beta})^{\mathsf T}\Big(I_n - \frac1nJ\Big)X\boldsymbol{\beta}.
$$
Dividing by $p - 1$ gives $\mathbb{E}(\mathrm{MSR})$. Since $I_n - \frac1nJ$ is idempotent, it is positive semidefinite, and the quadratic form equals $\|(I_n - \frac1nJ)X\boldsymbol{\beta}\|^2$, which vanishes exactly when $X\boldsymbol{\beta}$ is a multiple of $\boldsymbol{1}_n$; as the columns of $X$ are linearly independent, this happens exactly when $\beta_1 = \cdots = \beta_{p-1} = 0$. $\square$

So $\mathrm{MSR}$ and $\mathrm{MSE}$ estimate the same $\sigma^2$ when no predictor matters, and $\mathrm{MSR}$ tends to be larger otherwise: their ratio is the natural test statistic.

**Theorem 7.4.1 (ANOVA F-Test)** For the hypotheses

$$
H_0\colon \beta_1 = \beta_2 = \cdots = \beta_{p-1} = 0 \qquad\text{vs}\qquad H_1\colon \beta_k \ne 0 \text{ for at least one } k \in \{1, 2, \dots, p - 1\},
$$
the test statistic $F^* = \mathrm{MSR}/\mathrm{MSE}$ has the sampling distribution $F^* \sim F_{p-1,n-p}$ under $H_0$. At level $\alpha$, $H_0$ is rejected if the calculated value $F_0$ exceeds $F_{p-1,n-p,\alpha}$, equivalently if the $p$-value $\mathbb{P}(F^* > F_0 \mid H_0)$ is less than $\alpha$.

**Proof** Under $H_0$, $X\boldsymbol{\beta} = \beta_0\boldsymbol{1}_n$ and $(H - \frac1nJ)\boldsymbol{1}_n = \boldsymbol{0}$, so $\mathrm{SSR} = \boldsymbol{\varepsilon}^{\mathsf T}(H - \frac1nJ)\boldsymbol{\varepsilon}$; also $\mathrm{SSE} = \boldsymbol{\varepsilon}^{\mathsf T}(I_n - H)\boldsymbol{\varepsilon}$. The two matrices are symmetric idempotent of ranks $p - 1$ and $n - p$, so, as in the proof of Theorem 7.3.1, $\mathrm{SSR}/\sigma^2 \sim \chi^2_{p-1}$ and $\mathrm{SSE}/\sigma^2 \sim \chi^2_{n-p}$. Moreover $\mathrm{SSR} = \|\boldsymbol{W}_1\|^2$ and $\mathrm{SSE} = \|\boldsymbol{W}_2\|^2$ with $\boldsymbol{W}_1 = (H - \frac1nJ)\boldsymbol{\varepsilon}$, $\boldsymbol{W}_2 = (I_n - H)\boldsymbol{\varepsilon}$, and $(H - \frac1nJ)(I_n - H) = O$ because $H(I_n - H) = O$ and $J(I_n - H) = J - JH = O$; by (N4) and (N5) the two sums of squares are independent. The ratio of independent chi-square variables divided by their degrees of freedom has the $F_{p-1,n-p}$ distribution. $\square$

If $H_0$ is rejected, there is evidence that one or more of the explanatory variables in the linear model is potentially useful for predicting (explaining) the response. If $H_0$ is not rejected, there is no evidence that any of the explanatory variables helps to model, predict or explain the response through the linear model. The overall test does not say which predictors matter; that is the role of the $t$-tests and partial $F$-tests of [3.3.8](/3.3.8) and [3.3.9](/3.3.9). For $p = 2$ it reduces to the $F$-test of $H_0\colon \beta_1 = 0$ in [3.3.4](/3.3.4).

### 7.4.3. R² and Adjusted R²

**Definition 7.4.1 (Coefficient of Multiple Determination)** The **coefficient of multiple determination** is

$$
R^2 = \frac{\mathrm{SSR}}{\mathrm{SSTO}} = \frac{\sum(\hat Y_i - \bar Y)^2}{\sum(Y_i - \bar Y)^2} = 1 - \frac{\mathrm{SSE}}{\mathrm{SSTO}}.
$$
It gives the proportion of the variation in the response that is explained by the model, that is, by all the explanatory variables in the model; $1 - R^2$ is the proportion not explained.

**Proposition 7.4.3** If the model contains an intercept:

1. $R^2 = r^2$, where $r$ is the sample correlation between the responses $Y_i$ and the fitted values $\hat Y_i$; $R = \sqrt{R^2} = r$ is the sample **multiple correlation coefficient**.
2. $F^* = \dfrac{R^2}{1 - R^2}\cdot\dfrac{n - p}{p - 1}$.
3. Adding an explanatory variable never increases $\mathrm{SSE}$ and never decreases $R^2$.

**Proof** (1) The mean of the $\hat Y_i$ is $\bar Y$, since $\sum e_i = 0$. As in the proof of Proposition 7.4.1, $\sum(Y_i - \bar Y)(\hat Y_i - \bar Y) = (\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n + \boldsymbol{e})^{\mathsf T}(\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n) = \mathrm{SSR}$, so

$$
r = \frac{\sum(Y_i - \bar Y)(\hat Y_i - \bar Y)}{\sqrt{\sum(Y_i - \bar Y)^2}\sqrt{\sum(\hat Y_i - \bar Y)^2}} = \frac{\mathrm{SSR}}{\sqrt{\mathrm{SSTO}\cdot\mathrm{SSR}}} = \sqrt{\frac{\sum(\hat Y_i - \bar Y)^2}{\sum(Y_i - \bar Y)^2}}.
$$
(2) $F^* = \dfrac{\mathrm{SSR}/(p - 1)}{\mathrm{SSE}/(n - p)}$; divide numerator and denominator by $\mathrm{SSTO}$. (3) If a column $\boldsymbol{z}$ is added, the column space can only grow, $\mathcal{R}(X_{\mathrm{old}}) \subseteq \mathcal{R}(X_{\mathrm{new}})$, and $\mathrm{SSE}$ is the squared distance from $\boldsymbol{Y}$ to the column space, which cannot increase when the subspace grows; $\mathrm{SSTO}$ does not change. $\square$

More precisely, if $\boldsymbol{z}$ is not a linear combination of the old columns, let $\tilde{\boldsymbol{z}} = (I_n - H_{\mathrm{old}})\boldsymbol{z} \ne \boldsymbol{0}$ be its part orthogonal to $\mathcal{R}(X_{\mathrm{old}})$. Then $\mathcal{R}(X_{\mathrm{new}})$ is the orthogonal sum of $\mathcal{R}(X_{\mathrm{old}})$ and $\operatorname{span}(\tilde{\boldsymbol{z}})$, the new residual is the old residual minus its projection on $\tilde{\boldsymbol{z}}$, and

$$
\mathrm{SSE}_{\mathrm{new}} = \mathrm{SSE}_{\mathrm{old}} - \frac{(\tilde{\boldsymbol{z}}^{\mathsf T}\boldsymbol{e}_{\mathrm{old}})^2}{\tilde{\boldsymbol{z}}^{\mathsf T}\tilde{\boldsymbol{z}}}.
$$
So $\mathrm{SSE}$ strictly decreases unless the new variable, adjusted for the old ones, is exactly uncorrelated with the old residuals. In practice it almost always decreases, even when the new variable is pure noise. This is why $R^2$ alone cannot be used to choose among models with different numbers of predictors.

**Definition 7.4.2 (Adjusted Coefficient of Determination)** The **adjusted coefficient of determination** is

$$
R_a^2 = 1 - \frac{\mathrm{MSE}}{\mathrm{MSTO}} = 1 - \frac{n - 1}{n - p}\cdot\frac{\mathrm{SSE}}{\mathrm{SSTO}},
$$
which replaces the sums of squares in $1 - R^2$ by mean squares, using $\hat\sigma^2 = \mathrm{MSE} = \mathrm{SSE}/(n - p)$ as the estimate of the error variance.

When more explanatory variables are added, $R^2$ always increases (or stays the same), but $R_a^2$ can decrease: the decrease of $\mathrm{SSE}$ must outweigh the loss of a degree of freedom. One always has $R_a^2 \le R^2$, and $R_a^2$ can be negative. Model selection criteria built on this idea are discussed in [3.3.11](/3.3.11). The limitations of $R^2$ listed in [3.3.6](/3.3.6) apply equally to $R_a^2$.

## Summary

| Quantity | Matrix form | Distribution or property |
|---|---|---|
| model | $\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, $X$ of size $n \times p$, rank $p$ | $\boldsymbol{Y} \sim \mathcal{N}_n(X\boldsymbol{\beta}, \sigma^2I_n)$ |
| estimates | $\boldsymbol{b} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ | $\mathcal{N}_p\big(\boldsymbol{\beta}, \sigma^2(X^{\mathsf T}X)^{-1}\big)$; BLUE |
| fitted values, residuals | $\hat{\boldsymbol{Y}} = H\boldsymbol{Y}$, $\boldsymbol{e} = (I_n - H)\boldsymbol{Y}$, $H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$ | $\boldsymbol{e}^{\mathsf T}\hat{\boldsymbol{Y}} = 0$; $\operatorname{Cov}(\boldsymbol{e}) = \sigma^2(I_n - H)$ |
| leverage | $h_{ii} = \boldsymbol{x}_{(i)}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_{(i)}$ | $\frac1n \le h_{ii} \le 1$, $\sum h_{ii} = p$, $h_{ii} = \frac1n + \frac{D^2}{n - 1}$ |
| $\mathrm{SSE}$, $\mathrm{SSR}$, $\mathrm{SSTO}$ | $\boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}$, $\boldsymbol{Y}^{\mathsf T}(H - \frac1nJ)\boldsymbol{Y}$, $\boldsymbol{Y}^{\mathsf T}(I_n - \frac1nJ)\boldsymbol{Y}$ | df $n - p$, $p - 1$, $n - 1$ |
| overall $F$-test | $F^* = \mathrm{MSR}/\mathrm{MSE}$ | $F_{p-1,n-p}$ under $H_0\colon \beta_1 = \cdots = \beta_{p-1} = 0$ |
| $R^2$, $R_a^2$ | $1 - \mathrm{SSE}/\mathrm{SSTO}$, $1 - \mathrm{MSE}/\mathrm{MSTO}$ | $R^2 = r^2(\boldsymbol{Y}, \hat{\boldsymbol{Y}})$; $R_a^2$ penalizes extra predictors |

- Least squares has two derivations: setting the gradient of $\|\boldsymbol{Y} - X\boldsymbol{\beta}\|^2$ to zero, and projecting $\boldsymbol{Y}$ orthogonally onto the column space $\mathcal{R}(X)$; both give the normal equations $X^{\mathsf T}\boldsymbol{e} = \boldsymbol{0}$.
- Every distributional result follows from a few facts about the multivariate normal distribution (linear transformations, zero covariance means independence, quadratic forms in projections are chi-square) and from $\mathbb{E}(\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}) = \operatorname{tr}(A\Sigma) + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}$.
- The Gauss–Markov theorem needs only $\mathbb{E}(\boldsymbol{\varepsilon}) = \boldsymbol{0}$, $\operatorname{Cov}(\boldsymbol{\varepsilon}) = \sigma^2I_n$ and full rank; it compares OLS only with linear unbiased estimators.
- Partial regression coefficients measure the effect of one predictor with the others held constant; polynomial terms, interactions and dummy variables keep the model linear in the parameters.
