---
title: Principal Component Analysis
description: Population and sample principal components as the eigenvectors of a covariance or correlation matrix; variance explained and the correlations between components and variables; standardization; principal components under normality; choosing the number of components, scree plots, interpretation and diagnostics; PCA as best low-rank approximation; large-sample inference for eigenvalues and eigenvectors.
---

When $p$ variables are strongly correlated, the data occupy only a few directions of $\mathbb{R}^p$ and much of the description is redundant. Principal component analysis replaces the original variables by a small number of uncorrelated linear combinations that retain most of their variation. Mathematically it is nothing but the **spectral decomposition** of a covariance matrix ([2.1.7](/2.1.7)): the components are the coordinates of the data in the orthonormal basis of eigenvectors, ordered by eigenvalue, and the optimality of this choice is the extremal property of the **Rayleigh quotient**. This chapter develops the population theory, its sample version, and the practical questions of how many components to keep and how to interpret them. The next chapter ([3.4.6](/3.4.6)) computes PCA through the **singular value decomposition** and extends it to distance data (multidimensional scaling) and to nonlinear structure (kernel PCA); factor analysis ([3.4.8](/3.4.8)) builds a statistical model on the same covariance structure.

## 5.1. Motivation and Basic Idea

The `decathlon2` data record the results of $27$ athletes in the ten events of two decathlon competitions. How can we understand the structure of ten correlated features? Plotting two of them, say shot put against discus, shows a strong positive correlation: the points scatter around a line. In the extreme case where all points lie exactly on a line, one coordinate along that line describes them completely. In general we look for the direction along which the data have the largest variance; projecting onto it loses the least information. In higher dimensions we keep the few directions of largest spread, for example the plane that best fits a curved cloud in $\mathbb{R}^3$.

Choosing these directions amounts to changing the coordinate system. Geometrically, *principal component analysis* (PCA) rotates the original axes; algebraically, it forms linear combinations of the $p$ random variables,

$$
Y_j = \boldsymbol{a}_j^{\mathsf T}\boldsymbol{X} = a_{j1}X_1 + \cdots + a_{jp}X_p,
$$

so that an $n \times p$ **data matrix** $X$ (rows $\boldsymbol{x}_1^{\mathsf T}, \dots, \boldsymbol{x}_n^{\mathsf T}$, one per observation) is rotated into a matrix of new coordinates $(y_{jk})$ whose last columns carry little variation. PCA explains the variance–covariance structure of a set of variables through a few linear combinations of them; its two general objectives are data reduction and interpretation. It was introduced by Karl Pearson in 1901 and developed independently, and named, by Harold Hotelling in the 1930s; it is now one of the most widely used statistical techniques in almost every field.

![A correlated bivariate sample with its principal axes: the first principal direction e_1 follows the long axis of the constant-distance ellipse (left); in the rotated coordinates (y_1, y_2) the scores are uncorrelated and most of the spread lies along y_1 (right)](./plots/pca-axes.py)

## 5.2. Population Principal Components

### 5.2.1. Definition

Let the random vector $\boldsymbol{X} = (X_1, \dots, X_p)^{\mathsf T}$ have **covariance matrix** $\Sigma$ with eigenvalues $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_p \ge 0$. The first component should be the linear combination $Y_1 = \boldsymbol{a}_1^{\mathsf T}\boldsymbol{X}$ that maximizes $\operatorname{Var}(Y_1) = \boldsymbol{a}_1^{\mathsf T}\Sigma\boldsymbol{a}_1$. Since replacing $\boldsymbol{a}_1$ by $c\boldsymbol{a}_1$ multiplies the variance by $c^2$, the problem only makes sense for coefficient vectors of unit length, or equivalently for the ratio $\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}/\boldsymbol{a}^{\mathsf T}\boldsymbol{a}$.

**Definition 5.2.1 (Principal Component)** The first **principal component** of $\boldsymbol{X}$ is the linear combination $Y_1 = \boldsymbol{a}_1^{\mathsf T}\boldsymbol{X}$ that maximizes $\operatorname{Var}(\boldsymbol{a}_1^{\mathsf T}\boldsymbol{X})$ subject to $\boldsymbol{a}_1^{\mathsf T}\boldsymbol{a}_1 = 1$. For $i = 2, \dots, p$, the $i$-th principal component is the linear combination $Y_i = \boldsymbol{a}_i^{\mathsf T}\boldsymbol{X}$ that maximizes $\operatorname{Var}(\boldsymbol{a}_i^{\mathsf T}\boldsymbol{X})$ subject to $\boldsymbol{a}_i^{\mathsf T}\boldsymbol{a}_i = 1$ and $\operatorname{Cov}(\boldsymbol{a}_i^{\mathsf T}\boldsymbol{X}, \boldsymbol{a}_k^{\mathsf T}\boldsymbol{X}) = \boldsymbol{a}_k^{\mathsf T}\Sigma\boldsymbol{a}_i = 0$ for all $k < i$.

The solution uses the extremal characterization of eigenvalues of a symmetric matrix, the Rayleigh quotient of [2.1.7](/2.1.7).

**Lemma 5.2.1 (Maximization of Quadratic Forms on the Unit Sphere)** Let $\Sigma$ be a symmetric $p \times p$ matrix with eigenvalues $\lambda_1 \ge \cdots \ge \lambda_p$ and associated orthonormal eigenvectors $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$. Then

$$
\max_{\boldsymbol{a} \ne \boldsymbol{0}} \frac{\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \lambda_1 \ (\text{attained at } \boldsymbol{a} = \boldsymbol{e}_1), \qquad \min_{\boldsymbol{a} \ne \boldsymbol{0}} \frac{\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \lambda_p \ (\text{attained at } \boldsymbol{a} = \boldsymbol{e}_p),
$$

and, for $k = 1, \dots, p-1$,

$$
\max_{\boldsymbol{a} \perp \boldsymbol{e}_1, \dots, \boldsymbol{e}_k,\ \boldsymbol{a} \ne \boldsymbol{0}} \frac{\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \lambda_{k+1} \ (\text{attained at } \boldsymbol{a} = \boldsymbol{e}_{k+1}).
$$

**Proof** Write $\Sigma = P\Lambda P^{\mathsf T}$ with $P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_p]$ orthogonal and $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_p)$, and put $\boldsymbol{b} = P^{\mathsf T}\boldsymbol{a}$. Then $\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}/\boldsymbol{a}^{\mathsf T}\boldsymbol{a} = \sum_i\lambda_i b_i^2/\sum_i b_i^2$ is a weighted average of the eigenvalues, which lies between $\lambda_p$ and $\lambda_1$. The constraint $\boldsymbol{a} \perp \boldsymbol{e}_1, \dots, \boldsymbol{e}_k$ means $b_1 = \cdots = b_k = 0$, so the average is then at most $\lambda_{k+1}$. $\square$

### 5.2.2. Finding the Principal Components

**Theorem 5.2.1** Let $\Sigma$ be the covariance matrix of $\boldsymbol{X} = (X_1, \dots, X_p)^{\mathsf T}$, with eigenvalue–eigenvector pairs $(\lambda_1, \boldsymbol{e}_1), \dots, (\lambda_p, \boldsymbol{e}_p)$, $\lambda_1 \ge \cdots \ge \lambda_p \ge 0$, the eigenvectors being orthonormal. Then the $i$-th principal component is

$$
Y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{X} = e_{i1}X_1 + e_{i2}X_2 + \cdots + e_{ip}X_p, \qquad i = 1, \dots, p,
$$

and

$$
\operatorname{Var}(Y_i) = \boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{e}_i = \lambda_i, \qquad \operatorname{Cov}(Y_i, Y_k) = \boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{e}_k = 0 \quad (i \ne k).
$$

If some eigenvalues are equal, the corresponding coefficient vectors, and hence the principal components, are not unique.

**Proof** By Lemma 5.2.1, $\boldsymbol{e}_1$ maximizes the variance among unit vectors. For $Y_i$, the constraint $\operatorname{Cov}(\boldsymbol{e}_k^{\mathsf T}\boldsymbol{X}, \boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{e}_k^{\mathsf T}\Sigma\boldsymbol{a} = \lambda_k\boldsymbol{e}_k^{\mathsf T}\boldsymbol{a} = 0$ means $\boldsymbol{a} \perp \boldsymbol{e}_k$ whenever $\lambda_k > 0$, so again by Lemma 5.2.1 the maximum is $\lambda_i$, attained at $\boldsymbol{e}_i$. Finally $\operatorname{Cov}(\boldsymbol{e}_i^{\mathsf T}\boldsymbol{X}, \boldsymbol{e}_k^{\mathsf T}\boldsymbol{X}) = \boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{e}_k = \lambda_k\boldsymbol{e}_i^{\mathsf T}\boldsymbol{e}_k = 0$ for $i \ne k$. $\square$

In matrix form, with $P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_p]$ and $\boldsymbol{Y} = (Y_1, \dots, Y_p)^{\mathsf T}$,

$$
\boldsymbol{Y} = P^{\mathsf T}\boldsymbol{X}, \qquad \boldsymbol{X} = P\boldsymbol{Y}, \qquad \operatorname{Cov}(\boldsymbol{Y}) = P^{\mathsf T}\Sigma P = \Lambda.
$$

The eigenvectors form the new coordinate system and the principal components are the coordinates of $\boldsymbol{X}$ in it.

**Example 5.2.1** Let

$$
\Sigma = \begin{bmatrix} 1 & -2 & 0 \\ -2 & 5 & 0 \\ 0 & 0 & 2 \end{bmatrix}.
$$

The eigenvalue–eigenvector pairs are $\lambda_1 = 5.83$, $\boldsymbol{e}_1 = (0.383, -0.924, 0)^{\mathsf T}$; $\lambda_2 = 2.00$, $\boldsymbol{e}_2 = (0, 0, 1)^{\mathsf T}$; $\lambda_3 = 0.17$, $\boldsymbol{e}_3 = (0.924, 0.383, 0)^{\mathsf T}$, so $\Sigma = P\Lambda P^{\mathsf T}$ with $P = [\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}_3]$, and the principal components are

$$
Y_1 = 0.383X_1 - 0.924X_2, \qquad Y_2 = X_3, \qquad Y_3 = 0.924X_1 + 0.383X_2.
$$

The variable $X_3$, uncorrelated with the others, is itself a principal component.

### 5.2.3. Interpreting the Principal Components

**Theorem 5.2.2** Under the assumptions of Theorem 5.2.1,

$$
\sigma_{11} + \sigma_{22} + \cdots + \sigma_{pp} = \sum_{i=1}^p\operatorname{Var}(X_i) = \lambda_1 + \lambda_2 + \cdots + \lambda_p = \sum_{i=1}^p\operatorname{Var}(Y_i).
$$

**Proof** $\sum_i\sigma_{ii} = \operatorname{tr}(\Sigma) = \operatorname{tr}(P\Lambda P^{\mathsf T}) = \operatorname{tr}(\Lambda P^{\mathsf T}P) = \operatorname{tr}(\Lambda)$. $\square$

The common value is the *total population variance*, and the rotation redistributes it among the components without changing it. Hence

$$
\text{proportion of total population variance due to the } k\text{-th principal component} = \frac{\lambda_k}{\lambda_1 + \lambda_2 + \cdots + \lambda_p}.
$$

If the first one, two or three components account for, say, $80\%$–$90\%$ of the total variance for large $p$, they can replace the original $p$ variables with little loss of information. In Example 5.2.1 the total variance is $1 + 5 + 2 = 8$; the first component accounts for $5.83/8 = 73\%$ and the first two for $(5.83 + 2)/8 = 98\%$.

The coefficient vector $\boldsymbol{e}_i = (e_{i1}, \dots, e_{ip})^{\mathsf T}$ describes the component as a whole: $e_{ik}$ measures the importance of the $k$-th variable to the $i$-th component in the presence of the other variables. The importance of a single variable on its own is measured by a correlation.

**Theorem 5.2.3** If $Y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{X}$ are the principal components obtained from $\Sigma$, then the correlation coefficients between the components and the variables are

$$
\rho_{Y_i, X_k} = \frac{e_{ik}\sqrt{\lambda_i}}{\sqrt{\sigma_{kk}}}, \qquad i, k = 1, \dots, p,
$$

and $\sum_{i=1}^p\rho_{Y_i, X_k}^2 = 1$ for each $k$.

**Proof** Let $\boldsymbol{c}_k$ be the $k$-th coordinate vector, so that $X_k = \boldsymbol{c}_k^{\mathsf T}\boldsymbol{X}$. Then $\operatorname{Cov}(Y_i, X_k) = \boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{c}_k = \lambda_i\boldsymbol{e}_i^{\mathsf T}\boldsymbol{c}_k = \lambda_i e_{ik}$, and dividing by $\sqrt{\operatorname{Var}(Y_i)\operatorname{Var}(X_k)} = \sqrt{\lambda_i\sigma_{kk}}$ gives the formula. Since $\Sigma = \sum_i\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$, the $(k,k)$ entry gives $\sum_i\lambda_ie_{ik}^2 = \sigma_{kk}$, which is the second claim. $\square$

So $\rho_{Y_i, X_k}^2$ is the proportion of the variance of $X_k$ explained by its correlation with $Y_i$. Geometrically, if all variables are scaled to unit length, $\rho_{Y_i, X_k}$ is the cosine of the angle between $X_k$ and the axis of $Y_i$, and $\sum_i\rho_{Y_i, X_k}^2 = 1$ is the Pythagorean theorem in the rotated coordinates.

**Example 5.2.2** In Example 5.2.1,

$$
\rho_{Y_1, X_1} = \frac{0.383\sqrt{5.83}}{\sqrt1} = 0.925, \qquad \rho_{Y_1, X_2} = \frac{-0.924\sqrt{5.83}}{\sqrt5} = -0.998.
$$

The coefficient of $X_2$ in $Y_1$ is about $2.4$ times that of $X_1$ in absolute value, yet both variables are almost equally (and strongly) correlated with $Y_1$; the coefficients and the correlations answer different questions.

### 5.2.4. Principal Components of Standardized Variables

What happens if one variable is measured on a much larger scale than the others, for example the 1500 m time (in seconds) against the 100 m time in the decathlon, or homework, quizzes and exams scored out of very different totals? The first component is then dominated by the variable with the largest variance.

**Example 5.2.3** For

$$
\Sigma = \begin{bmatrix} 1 & 4 \\ 4 & 100 \end{bmatrix}
$$

the eigenvalues are $100.16$ and $0.84$, with $\boldsymbol{e}_1 = (0.040, 0.999)^{\mathsf T}$: the first component, which explains $99.2\%$ of the total variance, is essentially the second variable alone, simply because its variance is so much larger.

The remedy is to standardize: let $Z_k = (X_k - \mu_k)/\sqrt{\sigma_{kk}}$, $k = 1, \dots, p$, or in matrix form

$$
\boldsymbol{Z} = (V^{1/2})^{-1}(\boldsymbol{X} - \boldsymbol{\mu}), \qquad V^{1/2} = \operatorname{diag}(\sqrt{\sigma_{11}}, \dots, \sqrt{\sigma_{pp}}).
$$

Then $\operatorname{Cov}(\boldsymbol{Z}) = (V^{1/2})^{-1}\Sigma(V^{1/2})^{-1} = \rho$, the population correlation matrix of $\boldsymbol{X}$, with entries $\rho_{ik} = \sigma_{ik}/\sqrt{\sigma_{ii}\sigma_{kk}}$.

**Theorem 5.2.4** The $i$-th principal component of the standardized variables $\boldsymbol{Z} = (Z_1, \dots, Z_p)^{\mathsf T}$, with $\operatorname{Cov}(\boldsymbol{Z}) = \rho$, is

$$
Y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{Z} = \boldsymbol{e}_i^{\mathsf T}(V^{1/2})^{-1}(\boldsymbol{X} - \boldsymbol{\mu}), \qquad i = 1, \dots, p,
$$

where $(\lambda_i, \boldsymbol{e}_i)$ are now the eigenvalue–eigenvector pairs of $\rho$. Moreover,

$$
\sum_{i=1}^p\operatorname{Var}(Y_i) = \sum_{i=1}^p\operatorname{Var}(Z_i) = p, \qquad \rho_{Y_i, Z_k} = e_{ik}\sqrt{\lambda_i}, \quad i, k = 1, \dots, p.
$$

This is Theorems 5.2.1–5.2.3 applied to $\boldsymbol{Z}$, whose variances are all $1$; the proportion of total standardized variance due to the $k$-th component is $\lambda_k/p$. The principal components obtained from $\Sigma$ and from $\rho$ are in general different, and neither is a simple function of the other: standardization is a substantive choice, appropriate when the variables are on incommensurable scales.

**Example 5.2.4** In Example 5.2.3 the correlation matrix is $\rho = \begin{bmatrix} 1 & 0.4 \\ 0.4 & 1 \end{bmatrix}$, with eigenvalues $1.4$ and $0.6$ and $\boldsymbol{e}_1 = (0.707, 0.707)^{\mathsf T}$, $\boldsymbol{e}_2 = (-0.707, 0.707)^{\mathsf T}$. Now that both variables have unit variance, the first component weights them equally and explains $1.4/2 = 70\%$ of the total standardized variance.

### 5.2.5. Principal Components under Normality

Suppose now that $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ with $\Sigma$ positive definite. Two additional facts follow.

1. The principal component scores are independent normal variables: $\boldsymbol{Y} = P^{\mathsf T}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \mathcal{N}_p(\boldsymbol{0}, \Lambda)$, so $Y_1, \dots, Y_p$ are independent with $Y_i \sim \mathcal{N}(0, \lambda_i)$.
2. The density of $\boldsymbol{X}$ is constant on the ellipsoids $(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) = c^2$. Since $\Sigma^{-1} = \sum_i\lambda_i^{-1}\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$, in the coordinates $y_i = \boldsymbol{e}_i^{\mathsf T}(\boldsymbol{x} - \boldsymbol{\mu})$ the ellipsoid is

   $$
   \frac{y_1^2}{\lambda_1} + \frac{y_2^2}{\lambda_2} + \cdots + \frac{y_p^2}{\lambda_p} = c^2,
   $$

   whose axes point along $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$ with half-lengths $c\sqrt{\lambda_1}, \dots, c\sqrt{\lambda_p}$. The principal components are the axes of the constant-density ellipsoids, the first being the longest.

## 5.3. Sample Principal Components

### 5.3.1. Definition and Properties

Let $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ be $n$ independent observations from a $p$-dimensional population with mean $\boldsymbol{\mu}$ and covariance matrix $\Sigma$, with sample mean $\bar{\boldsymbol{x}}$, **sample covariance matrix** $S$ and **sample correlation matrix** $R$ ([3.4.2](/3.4.2)). We seek linear combinations of the measured variables that account for much of the variation in the sample and are uncorrelated with each other. The recipe is to replace the population distribution by the empirical one: $\Sigma$ by $S$, $\rho$ by $R$, and to proceed as before.

**Definition 5.3.1 (Sample Principal Component)** Let $S$ have eigenvalue–eigenvector pairs $(\hat\lambda_1, \hat{\boldsymbol{e}}_1), \dots, (\hat\lambda_p, \hat{\boldsymbol{e}}_p)$ with $\hat\lambda_1 \ge \cdots \ge \hat\lambda_p \ge 0$ and orthonormal $\hat{\boldsymbol{e}}_i$. The $i$-th **sample principal component** is

$$
\hat y_i = \hat{\boldsymbol{e}}_i^{\mathsf T}\boldsymbol{x} = \hat e_{i1}x_1 + \hat e_{i2}x_2 + \cdots + \hat e_{ip}x_p, \qquad i = 1, \dots, p,
$$

and its value $\hat y_{ji} = \hat{\boldsymbol{e}}_i^{\mathsf T}\boldsymbol{x}_j$ at the $j$-th observation is the $i$-th principal component score of that observation. Usually the observations are centered first, $\hat y_{ji} = \hat{\boldsymbol{e}}_i^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})$, which changes only the location of the scores.

**Theorem 5.3.1** The sample principal components satisfy

| quantity | value |
|---|---|
| sample variance of $\hat y_k$ | $\hat\lambda_k$, $k = 1, \dots, p$ |
| sample covariance of $\hat y_i, \hat y_k$ | $0$, $i \ne k$ |
| total sample variance | $\sum_{i=1}^p s_{ii} = \hat\lambda_1 + \hat\lambda_2 + \cdots + \hat\lambda_p$ |
| sample correlation of $\hat y_i$ and $x_k$ | $r_{\hat y_i, x_k} = \dfrac{\hat e_{ik}\sqrt{\hat\lambda_i}}{\sqrt{s_{kk}}}$ |

**Proof** For the first line,

$$
\frac{1}{n-1}\sum_{j=1}^n(\hat y_{jk} - \bar{\hat y}_k)^2 = \frac{1}{n-1}\sum_{j=1}^n\big[\hat{\boldsymbol{e}}_k^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})\big]^2 = \hat{\boldsymbol{e}}_k^{\mathsf T}\Big[\frac{1}{n-1}\sum_{j=1}^n(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}\Big]\hat{\boldsymbol{e}}_k = \hat{\boldsymbol{e}}_k^{\mathsf T}S\hat{\boldsymbol{e}}_k = \hat\lambda_k.
$$

The other lines follow in the same way from the population proofs with $\Sigma$ replaced by $S$. $\square$

These are sample variances and correlations, descriptive statistics of the observed data; they estimate, but are not, the population quantities $\lambda_k$ and $\rho_{Y_i, X_k}$.

The data-matrix form clarifies which side the orthogonal matrix multiplies. For one observation the scores are $\hat{\boldsymbol{y}}_j = \hat P^{\mathsf T}\boldsymbol{x}_j$, a $p \times 1$ vector, where $\hat P = [\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_p]$. The data matrix $X$ stacks the observations as rows $\boldsymbol{x}_j^{\mathsf T}$, so the score matrix is

$$
Y = X\hat P \quad (n \times p), \qquad \text{row } j \text{ of } Y = \hat{\boldsymbol{y}}_j^{\mathsf T} = \boldsymbol{x}_j^{\mathsf T}\hat P.
$$

The sample principal components are coordinates; the eigenvectors form the coordinate system.

### 5.3.2. Principal Components of the Sample Correlation Matrix

If the observations are standardized, $z_{jk} = (x_{jk} - \bar x_k)/\sqrt{s_{kk}}$, the sample covariance matrix of $\boldsymbol{z}_1, \dots, \boldsymbol{z}_n$ is $R$. With $(\hat\lambda_i, \hat{\boldsymbol{e}}_i)$ now the eigenpairs of $R$, the $i$-th sample principal component is

$$
\hat y_i = \hat{\boldsymbol{e}}_i^{\mathsf T}\boldsymbol{z} = \hat e_{i1}z_1 + \hat e_{i2}z_2 + \cdots + \hat e_{ip}z_p, \qquad i = 1, \dots, p.
$$

Its sample variance is $\hat\lambda_i$, the sample covariance of two different components is $0$, the total standardized sample variance is $\operatorname{tr}(R) = p = \hat\lambda_1 + \cdots + \hat\lambda_p$, and $r_{\hat y_i, z_k} = \hat e_{ik}\sqrt{\hat\lambda_i}$.

### 5.3.3. Geometric Interpretation

For a bivariate sample, the ellipses $(\boldsymbol{x} - \bar{\boldsymbol{x}})^{\mathsf T}S^{-1}(\boldsymbol{x} - \bar{\boldsymbol{x}}) = c^2$ of constant **Mahalanobis distance** have their axes along $\hat{\boldsymbol{e}}_1$ and $\hat{\boldsymbol{e}}_2$ and are centered at $\bar{\boldsymbol{x}}$; the sample principal components are the coordinates along these axes. When $\hat\lambda_1 > \hat\lambda_2$ the ellipse is elongated and the principal directions are well defined. When $\hat\lambda_1 \approx \hat\lambda_2$ the ellipse is nearly a circle, every direction has about the same spread, and the principal directions are not determined by the data: in that case PCA cannot reduce dimension, and the computed directions are essentially arbitrary.

### 5.3.4. Dimension Reduction and Reconstruction

Keeping $k < p$ components means keeping the first $k$ columns of $Y = \tilde X\hat P$, where $\tilde X$ is the centered data matrix, and setting the rest to zero:

$$
Y = [\hat{\boldsymbol{y}}_{(1)}, \dots, \hat{\boldsymbol{y}}_{(k)}, \hat{\boldsymbol{y}}_{(k+1)}, \dots, \hat{\boldsymbol{y}}_{(p)}] \ \longrightarrow\ \tilde Y = [\hat{\boldsymbol{y}}_{(1)}, \dots, \hat{\boldsymbol{y}}_{(k)}, \boldsymbol{0}, \dots, \boldsymbol{0}],
$$

where $\hat{\boldsymbol{y}}_{(i)}$ is the column of scores of the $i$-th component. Rotating back gives the approximation $\hat X = \tilde Y\hat P^{\mathsf T}$ of $\tilde X$, still $n \times p$: each observation is replaced by its projection onto the span of $\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_k$ (plus $\bar{\boldsymbol{x}}$ if we add the mean back). For a single point in the plane with coordinates $(2, 1)$ and scores $(2.5, 0.3)$, keeping one component replaces the scores by $(2.5, 0)$, and rotating back gives the foot of the perpendicular from the point to the first axis.

Why does this save storage? Since the last $p - k$ columns of $\tilde Y$ are zero, only its first $k$ columns ($nk$ numbers) and the first $k$ columns of $\hat P$ ($kp$ numbers) need to be stored, instead of the $np$ entries of $X$. For a $1440 \times 1080$ image (one color channel treated as $n = 1440$ observations of $p = 1080$ variables) and $k = 100$, the ratio is

$$
\frac{nk + kp}{np} = \frac{1440 \cdot 100 + 100 \cdot 1080}{1440 \cdot 1080} \approx 16\%.
$$

For a photograph, the first component of each color channel explains more than $85\%$ of the variance and $20$ components more than $95\%$; $5$ or $10$ components give a blurred, blocky picture, while $100$ or $200$ components are visually close to the original.

![Low-rank reconstruction of a synthetic 120 x 160 grayscale image from its first k principal components (k = 1, 5, 20) compared with the original, and the cumulative proportion of variance explained](./plots/image-reconstruction.py)

## 5.4. Practical Issues

### 5.4.1. How Many Components to Retain

There is no definitive rule; the usual aids are:

- the *scree plot*, the plot of $\hat\lambda_i$ against $i$ (also called an elbow plot): look for the bend after which the remaining eigenvalues are small and roughly equal, and keep the components before it;
- the cumulative proportion of total sample variance explained, $(\hat\lambda_1 + \cdots + \hat\lambda_k)/(\hat\lambda_1 + \cdots + \hat\lambda_p)$, compared with a target such as $80\%$ or $90\%$;
- for PCA based on the correlation matrix $R$, the cutoff $1$ (Kaiser's rule): keep the components with $\hat\lambda_i > 1$, that is, those that explain more than the variance of a single standardized variable.

The interpretability of the retained components and the purpose of the analysis matter as much as these rules.

![Scree plot of the eigenvalues of the sample correlation matrix (left) and cumulative proportion of variance explained (right) for a simulated sample of n = 200 observations of p = 8 variables driven by two latent factors: the elbow after the second eigenvalue suggests keeping two components](./plots/scree-plot.py)

**Example 5.4.1** Jolicoeur and Mosimann measured the length, width and height of the carapaces (shells) of $24$ female and $24$ male painted turtles. For the male turtles the data are right-skewed, so we first take logarithms. PCA of the covariance matrix of the log-measurements (`prcomp` in R, which returns the square roots of the eigenvalues as `sdev`) gives component standard deviations $0.1527, 0.0245, 0.0190$, so the first component explains $96.05\%$ of the total variance and clearly one component captures essentially all the variation. Its coefficient vector is $(0.683, 0.510, 0.523)^{\mathsf T}$, so very approximately

$$
\hat y_1 \approx 0.5\big[\log(\text{length}) + \log(\text{width}) + \log(\text{height})\big] = 0.5\log(\text{volume}),
$$

and the first component measures the logarithm of the shell's volume, that is, its overall size.

### 5.4.2. Software

In R, `princomp()` uses the spectral decomposition of the covariance (or correlation) matrix, and `prcomp()` uses the singular value decomposition of the centered data matrix ([3.4.6](/3.4.6)). Simplified calls are `prcomp(x, scale = FALSE)` and `princomp(x, cor = FALSE, scores = TRUE)`; `scale = TRUE` or `cor = TRUE` standardizes the variables first, that is, analyzes the correlation matrix. The outputs correspond to the quantities above as follows.

| `prcomp()` | `princomp()` | meaning |
|---|---|---|
| `sdev` | `sdev` | standard deviations $\sqrt{\hat\lambda_j}$ of the components |
| `rotation` | `loadings` | matrix whose columns are the eigenvectors $\hat{\boldsymbol{e}}_j$ |
| `center` | `center` | variable means that were subtracted |
| `scale` | `scale` | scaling applied to each variable |
| `x` | `scores` | score vectors $\hat{\boldsymbol{y}}_{(j)} = (\hat y_{1j}, \dots, \hat y_{nj})^{\mathsf T}$ |

### 5.4.3. Checking Normality and Detecting Outliers

Plots of the principal components $\hat y_1, \hat y_2, \dots, \hat y_k$ serve two diagnostic purposes.

- The first few components are linear combinations with large variance; under multivariate normality they are normal, so their Q–Q plots and pairwise scatter plots check the normality assumption ([3.4.4](/3.4.4)).
- The last few components have small variance; an observation with a large value on them violates the near-linear relations satisfied by the rest of the data, so they help to identify suspect observations that may not stand out in any original variable.

In the turtle data, the scatter plot of $\hat y_1$ against $\hat y_2$ and the Q–Q plot of $\hat y_2$ both single out one turtle, whose second-component score is far larger than the others.

### 5.4.4. Interpreting a Component

To interpret the practical meaning of a component (rather than its theoretical meaning as a variance-maximizing direction), proceed in three steps.

1. Use the magnitudes of the coefficients to decide which original variables to keep for the interpretation. For $\hat y_1 = -0.7x_1 + 0.5x_2 - 0.1x_3$ we keep $x_1$ and $x_2$; the cutoff (for example $0.4$) is somewhat subjective.
2. Use the signs to decide whether the component is a sum (all signs equal) or a contrast (opposite signs) of the retained variables.
3. Combine this with the meanings of the variables. If $x_1$ is a Chinese-language score and $x_2$ a mathematics score, then $\hat y_1 = -0.7x_1 + 0.5x_2 - 0.1x_3$ is the difference between mathematics and language performance: values near $0$ mean balanced performance, positive values a science-oriented student, negative values a humanities-oriented one. A component $0.7x_1 + 0.5x_2 - 0.1x_3$ would instead measure overall ability in the two subjects.

## 5.5. Discussion

### 5.5.1. When Is PCA Useful?

PCA is usually an intermediate step in a data analysis, for example to reduce dimension before regression or classification. Two situations deserve attention.

- Eigenvalues $\hat\lambda_i \approx 0$ indicate (near) linear dependencies among the variables; the corresponding $\hat{\boldsymbol{e}}_i$ describe them.
- Equal or nearly equal eigenvalues make the corresponding components ill-defined, as in Section 5.3.3; if all eigenvalues are close, the variables are nearly uncorrelated and PCA is of little use.

PCA is implemented in practice through the singular value decomposition, discussed in [3.4.6](/3.4.6).

### 5.5.2. Covariance Matrices with Special Structure

**Example 5.5.1** If $\Sigma = \operatorname{diag}(\sigma_{11}, \sigma_{22}, \dots, \sigma_{pp})$, then $(\sigma_{ii}, \boldsymbol{c}_i)$ are the eigenpairs, where $\boldsymbol{c}_i$ is the $i$-th coordinate vector: the variables are already uncorrelated, the principal components are the variables themselves (ordered by variance), and PCA gains nothing.

**Example 5.5.2** For the equicorrelation matrix

$$
\Sigma = \sigma^2\begin{bmatrix} 1 & \rho & \cdots & \rho \\ \rho & 1 & \cdots & \rho \\ \vdots & \vdots & \ddots & \vdots \\ \rho & \rho & \cdots & 1 \end{bmatrix} = \sigma^2\big[(1 - \rho)I_p + \rho\boldsymbol{1}\boldsymbol{1}^{\mathsf T}\big], \qquad \rho > 0,
$$

the largest eigenvalue is $\lambda_1 = \sigma^2[1 + (p-1)\rho]$ with $\boldsymbol{e}_1 = \frac{1}{\sqrt p}(1, 1, \dots, 1)^{\mathsf T}$, and the remaining eigenvalues are $\lambda_2 = \cdots = \lambda_p = \sigma^2(1 - \rho)$, with eigenvectors that may be chosen as

$$
\boldsymbol{e}_k = \frac{1}{\sqrt{(k-1)k}}\big(\underbrace{1, \dots, 1}_{k-1}, -(k-1), 0, \dots, 0\big)^{\mathsf T}, \qquad k = 2, \dots, p.
$$

Indeed $\Sigma\boldsymbol{1} = \sigma^2(1 - \rho + p\rho)\boldsymbol{1}$, and every $\boldsymbol{v} \perp \boldsymbol{1}$ satisfies $\Sigma\boldsymbol{v} = \sigma^2(1 - \rho)\boldsymbol{v}$. The first component is proportional to the sum (or average) of the variables and explains the proportion $\lambda_1/(p\sigma^2) = \rho + (1 - \rho)/p$ of the total variance; the other components are not unique. A positively correlated set of test scores thus has a first "general ability" component.

### 5.5.3. Limitations

- PCA uses only the covariance matrix (second moments); higher-order structure is ignored.
- It only captures linear structure; curved or clustered data may need nonlinear methods ([3.4.6](/3.4.6)).
- Linear combinations of many variables may be hard to interpret.
- It is sensitive to outliers and to the scales of the variables.

## 5.6. PCA as Best Low-Dimensional Approximation

The derivation in Section 5.2 builds the components one at a time, maximizing variance. An equivalent view treats the $r$-dimensional approximation as a whole. Approximating the data by the first $r$ principal components means projecting them onto the $r$-dimensional plane through $\bar{\boldsymbol{x}}$ spanned by $\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_r$; among all $r$-dimensional planes, this one minimizes the sum of squared distances $\sum_{j=1}^n d_j^2$ from the observations to the plane, and among all planes through $\bar{\boldsymbol{x}}$ it maximizes the spread of the projected observations.

**Theorem 5.6.1** Let $A = [\boldsymbol{a}_1, \dots, \boldsymbol{a}_n]^{\mathsf T}$ be any $n \times p$ matrix with $\operatorname{rank}(A) \le r < \min(p, n)$, used to approximate the mean-corrected data matrix $[\boldsymbol{x}_1 - \bar{\boldsymbol{x}}, \dots, \boldsymbol{x}_n - \bar{\boldsymbol{x}}]^{\mathsf T}$, and measure the error by the sum of the $np$ squared errors $\sum_{j=1}^n(\boldsymbol{x}_j - \bar{\boldsymbol{x}} - \boldsymbol{a}_j)^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}} - \boldsymbol{a}_j)$. Let $\hat E_r = [\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_r]$. The error is minimized by $\hat A = [\hat{\boldsymbol{y}}_{(1)}, \dots, \hat{\boldsymbol{y}}_{(r)}]\hat E_r^{\mathsf T}$, the projection of each centered observation onto the span of $\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_r$, and the minimal error is

$$
(n-1)(\hat\lambda_{r+1} + \cdots + \hat\lambda_p).
$$

This is the **Eckart–Young theorem** for the centered data matrix. The population version explains why: for a random vector $\boldsymbol{X}$ with mean $\boldsymbol{\mu}$ and covariance $\Sigma$, approximate $\boldsymbol{X}$ by a point $C + U\boldsymbol{b}$ of an $r$-dimensional plane with location $C$, orthonormal direction matrix $U = [\boldsymbol{u}_1, \dots, \boldsymbol{u}_r]$ and coefficients $\boldsymbol{b}$, minimizing $\mathbb{E}(\boldsymbol{X} - C - U\boldsymbol{b})^{\mathsf T}(\boldsymbol{X} - C - U\boldsymbol{b})$. Optimize in the order $\boldsymbol{b}$, $C$, $U$:

1. given the plane, the closest point is the orthogonal projection, $\hat{\boldsymbol{b}} = U^{\mathsf T}(\boldsymbol{X} - C)$, which leaves the residual $(I - UU^{\mathsf T})(\boldsymbol{X} - C)$;
2. given the directions, the best location is the mean, $\hat C = \boldsymbol{\mu}$ (the mean is the point closest to the distribution in mean square);
3. the objective becomes $\mathbb{E}\|(I - UU^{\mathsf T})(\boldsymbol{X} - \boldsymbol{\mu})\|^2 = \operatorname{tr}\Sigma - \operatorname{tr}(U^{\mathsf T}\Sigma U)$, so we maximize $\operatorname{tr}(U^{\mathsf T}\Sigma U)$.

The "largest spread" formulation gives the same problem:

$$
\max_U\operatorname{tr}\operatorname{Cov}\big(UU^{\mathsf T}(\boldsymbol{X} - \boldsymbol{\mu})\big) = \max_U\operatorname{tr}(UU^{\mathsf T}\Sigma UU^{\mathsf T}) = \max_U\operatorname{tr}(U^{\mathsf T}\Sigma UU^{\mathsf T}U) = \max_U\operatorname{tr}(U^{\mathsf T}\Sigma U) = \sum_{i=1}^r\boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{e}_i = \sum_{i=1}^r\lambda_i,
$$

the maximum being attained at $\hat{\boldsymbol{u}}_i = \boldsymbol{e}_i$ (Ky Fan's maximum principle, the $r$-dimensional extension of Lemma 5.2.1). Thus the one-at-a-time and the whole-subspace views lead to the same components for every $r$.

## 5.7. Large-Sample Inference

The sample eigenvalues and eigenvectors are random; how variable are they? Assume that $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ is a random sample from a multivariate normal population and that the eigenvalues of $\Sigma$ are distinct and positive, $\lambda_1 > \lambda_2 > \cdots > \lambda_p > 0$. Let $\boldsymbol{\lambda} = (\lambda_1, \dots, \lambda_p)^{\mathsf T}$, $\hat{\boldsymbol{\lambda}}$ the vector of sample eigenvalues, and $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_p)$. For large $n$, the following results (due to Anderson and Girshick) hold.

**Theorem 5.7.1** Under these assumptions:

1. $\sqrt{n}(\hat{\boldsymbol{\lambda}} - \boldsymbol{\lambda})$ is approximately $\mathcal{N}_p(\boldsymbol{0}, 2\Lambda^2)$; in particular the $\hat\lambda_i$ are approximately independent with $\hat\lambda_i \overset{\cdot}{\sim} \mathcal{N}(\lambda_i, 2\lambda_i^2/n)$;
2. with $E_i = \lambda_i\sum_{k \ne i}\frac{\lambda_k}{(\lambda_k - \lambda_i)^2}\boldsymbol{e}_k\boldsymbol{e}_k^{\mathsf T}$, $\sqrt{n}(\hat{\boldsymbol{e}}_i - \boldsymbol{e}_i)$ is approximately $\mathcal{N}_p(\boldsymbol{0}, E_i)$;
3. each $\hat\lambda_i$ is approximately independent of the elements of the associated $\hat{\boldsymbol{e}}_i$.

From part 1, $\mathbb{P}(\lvert\hat\lambda_i - \lambda_i\rvert \le z_{\alpha/2}\lambda_i\sqrt{2/n}) \approx 1 - \alpha$, which gives the large-sample $100(1-\alpha)\%$ confidence interval

$$
\frac{\hat\lambda_i}{1 + z_{\alpha/2}\sqrt{2/n}} \le \lambda_i \le \frac{\hat\lambda_i}{1 - z_{\alpha/2}\sqrt{2/n}}.
$$

Part 2 shows that the $\hat{\boldsymbol{e}}_i$ are approximately normal around the $\boldsymbol{e}_i$, that their elements are correlated, and that their variability depends strongly on the separation of the eigenvalues: if $\lambda_i$ is close to another eigenvalue, $E_i$ is large and the direction $\hat{\boldsymbol{e}}_i$ is poorly determined, the quantitative version of the remark in Section 5.3.3.

## Summary

- The principal components of $\boldsymbol{X}$ are $Y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{X}$, where $(\lambda_i, \boldsymbol{e}_i)$ are the eigenpairs of $\Sigma$ in decreasing order; they are uncorrelated with $\operatorname{Var}(Y_i) = \lambda_i$, and $\sum_i\lambda_i = \operatorname{tr}\Sigma$ is the total variance, so $\lambda_k/\sum_i\lambda_i$ is the proportion explained by the $k$-th component.
- The coefficients $e_{ik}$ describe a component jointly; the correlations $\rho_{Y_i, X_k} = e_{ik}\sqrt{\lambda_i}/\sqrt{\sigma_{kk}}$ describe each variable separately.
- PCA is not scale invariant; with incommensurable variables use the correlation matrix, whose components differ from those of $\Sigma$.
- Under normality the components are independent and are the axes of the constant-density ellipsoids.
- Sample principal components replace $\Sigma, \rho$ by $S, R$; the number of components is chosen by scree plots, cumulative variance, or eigenvalues above $1$ for $R$; the first components check normality, the last ones flag outliers.
- Keeping $r$ components gives the best rank-$r$ approximation of the centered data, with error $(n-1)\sum_{i > r}\hat\lambda_i$.
