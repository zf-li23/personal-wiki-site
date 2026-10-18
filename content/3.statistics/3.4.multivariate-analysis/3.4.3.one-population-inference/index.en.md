---
title: Inference for a Single Mean Vector
description: Sampling distribution of the sample mean vector and sample covariance matrix of a normal sample and the Wishart distribution; Hotelling's T² statistic, its F distribution, the test for a mean vector and its invariance; confidence ellipsoids; individual, Bonferroni and T² simultaneous confidence intervals for linear combinations; the relation between T² and the likelihood ratio test.
---

This chapter carries the inference for the mean of a normal population ([3.2.4](/3.2.4), [3.2.5](/3.2.5)) over to a mean vector, when the covariance matrix is unknown. Each one-dimensional object has a $p$-dimensional analogue: the sample variance becomes the sample covariance matrix, whose distribution is the Wishart distribution (a matrix version of the scaled chi-square distribution); the square of the $t$ statistic becomes Hotelling's $T^2$ statistic, which again has an $F$ distribution after scaling; the confidence interval becomes a confidence ellipsoid. One idea, however, has no counterpart in one dimension: with several means, or several linear combinations of them, we usually want intervals that are correct simultaneously, and the chapter compares the Bonferroni intervals with the $T^2$ intervals obtained from the confidence ellipsoid. The tools are the properties of the multivariate normal distribution ([3.4.2](/3.4.2)) and the maximization lemma ([3.4.1](/3.4.1)). The comparison of two or more mean vectors and large-sample inference follow in [3.4.4](/3.4.4).

## 3.1. The Setting and the Sampling Distributions

### 3.1.1. A Motivating Example and the Model

**Example 3.1.1 (Ratings for Occupations)** The O*NET database rates occupations on six work values: Achievement (the occupation lets workers use their best abilities and gives a feeling of accomplishment), Working Conditions (job security and good working conditions), Recognition (advancement, potential for leadership, prestige), Relationships (service to others in a friendly, noncompetitive environment), Support (supportive management that stands behind its employees) and Independence (working independently and making one's own decisions). For $n = 55$ occupations in architecture, engineering and related fields (architects, landscape architects, cartographers, surveyors, aerospace engineers, …), the sample means of the six ratings are

| Achievement | Independence | Recognition | Relationships | Support | Working Conditions |
|---|---|---|---|---|---|
| 5.118 | 5.021 | 4.717 | 3.668 | 4.592 | 5.101 |

Natural questions are: Is the mean vector equal to a hypothesized value? How confident are we about the mean vector as a whole? How confident are we about an integrated value such as $\frac{1}{2}\mu_{\text{Achievement}} + \frac{1}{2}\mu_{\text{Independence}}$? And what if several such integrated values are of interest at once?

Throughout the chapter we assume that $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ is a random sample from $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ with both $\boldsymbol{\mu}$ and $\Sigma$ unknown: the $\boldsymbol{X}_j$ are mutually independent and each $\boldsymbol{X}_j \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$. The point estimators are $\bar{\boldsymbol{X}}$ and $S = \frac{1}{n-1}\sum_j(\boldsymbol{X}_j - \bar{\boldsymbol{X}})(\boldsymbol{X}_j - \bar{\boldsymbol{X}})^{\mathsf T}$, which are unbiased (Theorem 2.2.1), are the maximum likelihood estimators up to the factor $\frac{n-1}{n}$ (Theorem 2.5.1), and are sufficient (Theorem 2.5.2). Inference needs their joint distribution.

The two probabilistic tools are Theorem 2.4.7, which says that $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_p$ for $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$, and Theorem 2.4.8 on linear combinations $\sum_jc_j\boldsymbol{X}_j$ of independent normal vectors. A linear combination of vectors is written like a scalar one with identity blocks: $\bar{\boldsymbol{X}} = \frac{1}{n}\boldsymbol{X}_1 + \cdots + \frac{1}{n}\boldsymbol{X}_n = \frac{1}{n}[I_p, \dots, I_p](\boldsymbol{X}_1^{\mathsf T}, \dots, \boldsymbol{X}_n^{\mathsf T})^{\mathsf T}$, just as $\bar X = \frac{1}{n}(1, \dots, 1)(X_1, \dots, X_n)^{\mathsf T}$ in one dimension. For $p = 2$, $n = 2$, for instance, $\begin{bmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{bmatrix}(X_{11}, X_{12}, X_{21}, X_{22})^{\mathsf T} = \boldsymbol{X}_1 + \boldsymbol{X}_2$. Two such combinations $\sum_jc_j\boldsymbol{X}_j$ and $\sum_jb_j\boldsymbol{X}_j$ have $\operatorname{Cov} = \sum_jc_jb_j\Sigma$ and are independent when $\sum_jb_jc_j = 0$.

### 3.1.2. The Wishart Distribution

In one dimension, if $z_1, \dots, z_m$ are iid $\mathcal{N}(0, \sigma^2)$, then $\sum_iz_i^2 \sim \sigma^2\chi^2_m$. The multivariate analogue replaces squares by outer products.

**Definition 3.1.1 (Wishart Distribution)** Let $\boldsymbol{Z}_1, \dots, \boldsymbol{Z}_m$ be iid $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$. The distribution of the $p \times p$ random matrix

$$
\sum_{j=1}^{m}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}
$$
is called the **Wishart distribution** with $m$ degrees of freedom and scale matrix $\Sigma$, written $W_p(m, \Sigma)$.

The distribution is named after John Wishart, who derived it in 1928. It is the multivariate analogue of a scaled chi-square distribution: $W_1(m, \sigma^2) = \sigma^2\chi^2_m$, and the diagonal entries of $A \sim W_p(m, \Sigma)$ are $\sigma_{kk}\chi^2_m$. Its mean is $\mathbb{E}A = m\Sigma$. When $m \ge p$ and $\Sigma$ is positive definite, $A$ is positive definite with probability one and has a density, which we shall not need; some authors write $W_m(\cdot \mid \Sigma)$ for the same distribution. Besides testing problems in multivariate analysis, it is the conjugate prior for the precision matrix in Bayesian statistics.

**Property 3.1.1** Let $A_1 \sim W_p(m_1, \Sigma)$ and $A_2 \sim W_p(m_2, \Sigma)$ be independent, and $A \sim W_p(m, \Sigma)$. Then

1. $A_1 + A_2 \sim W_p(m_1 + m_2, \Sigma)$;
2. $CAC^{\mathsf T} \sim W_q(m, C\Sigma C^{\mathsf T})$ for every constant $q \times p$ matrix $C$ (in particular for an invertible $p \times p$ matrix $C$).

Both follow from the definition: concatenate the two sets of $\boldsymbol{Z}_j$ for the first, and note that $CAC^{\mathsf T} = \sum_j(C\boldsymbol{Z}_j)(C\boldsymbol{Z}_j)^{\mathsf T}$ with $C\boldsymbol{Z}_j$ iid $\mathcal{N}_q(\boldsymbol{0}, C\Sigma C^{\mathsf T})$ for the second.

### 3.1.3. The Joint Distribution of the Sample Mean Vector and the Sample Covariance Matrix

**Theorem 3.1.1** Let $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ be a random sample from $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$. Then

1. $\bar{\boldsymbol{X}} \sim \mathcal{N}_p\left(\boldsymbol{\mu}, \frac{1}{n}\Sigma\right)$;
2. $(n-1)S \sim W_p(n-1, \Sigma)$;
3. $\bar{\boldsymbol{X}}$ and $S$ are independent.

**Proof** Let $Q = (q_{jl})$ be the $n \times n$ Helmert matrix

$$
Q = \begin{bmatrix} \frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \cdots & \frac{1}{\sqrt{n}} \\ \frac{1}{\sqrt{2 \cdot 1}} & \frac{-1}{\sqrt{2 \cdot 1}} & 0 & \cdots & 0 \\ \frac{1}{\sqrt{3 \cdot 2}} & \frac{1}{\sqrt{3 \cdot 2}} & \frac{-2}{\sqrt{3 \cdot 2}} & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ \frac{1}{\sqrt{n(n-1)}} & \frac{1}{\sqrt{n(n-1)}} & \frac{1}{\sqrt{n(n-1)}} & \cdots & \frac{-(n-1)}{\sqrt{n(n-1)}} \end{bmatrix},
$$
an orthogonal matrix whose first row is $\boldsymbol{1}_n^{\mathsf T}/\sqrt{n}$; the other rows are orthogonal to it, so their entries sum to zero. Define $\boldsymbol{Z}_l = \sum_{j=1}^{n}q_{lj}(\boldsymbol{X}_j - \boldsymbol{\mu})$ for $l = 1, \dots, n$. By Theorem 2.4.8, the $\boldsymbol{Z}_l$ are jointly normal with $\operatorname{Cov}(\boldsymbol{Z}_l, \boldsymbol{Z}_{l'}) = \left(\sum_jq_{lj}q_{l'j}\right)\Sigma$, which is $\Sigma$ for $l = l'$ and $O$ otherwise, because the rows of $Q$ are orthonormal. Hence $\boldsymbol{Z}_1, \dots, \boldsymbol{Z}_n$ are iid $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$. Now $\boldsymbol{Z}_1 = \sqrt{n}(\bar{\boldsymbol{X}} - \boldsymbol{\mu})$, which gives part 1, and since $Q$ is orthogonal,

$$
\sum_{l=1}^{n}\boldsymbol{Z}_l\boldsymbol{Z}_l^{\mathsf T} = \sum_{j=1}^{n}(\boldsymbol{X}_j - \boldsymbol{\mu})(\boldsymbol{X}_j - \boldsymbol{\mu})^{\mathsf T} = (n-1)S + n(\bar{\boldsymbol{X}} - \boldsymbol{\mu})(\bar{\boldsymbol{X}} - \boldsymbol{\mu})^{\mathsf T},
$$
so $(n-1)S = \sum_{l=2}^{n}\boldsymbol{Z}_l\boldsymbol{Z}_l^{\mathsf T} \sim W_p(n-1, \Sigma)$, which is part 2. Part 3 holds because $\bar{\boldsymbol{X}}$ depends only on $\boldsymbol{Z}_1$ and $S$ only on $\boldsymbol{Z}_2, \dots, \boldsymbol{Z}_n$. $\square$

In summary, with $\boldsymbol{Z}_j$ iid $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$,

$$
\bar{\boldsymbol{X}} = \boldsymbol{\mu} + \frac{1}{\sqrt{n}}\boldsymbol{Z}_1, \qquad (n-1)S = \sum_{j=2}^{n}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}. \tag{3.1}
$$
This is the multivariate version of the independence of $\bar X$ and $S^2$ for a normal sample ([3.2.2](/3.2.2)).

## 3.2. Hotelling's T² Test

### 3.2.1. From the t Statistic to the T² Statistic

Testing a hypothesis follows a fixed pipeline: state the null hypothesis $H_0$; choose a **test statistic** $T$; derive its null distribution; for a given **level of significance** $\alpha$, construct the rejection region, which can be done before seeing the data; finally compute the observed statistic $t$ from the data and its **p-value**, and decide whether to reject $H_0$.

Recall the one-dimensional case ([3.2.5](/3.2.5)). For $H_0\colon \mu = \mu_0$ versus $H_1\colon \mu \ne \mu_0$ with $x_1, \dots, x_n$ iid $\mathcal{N}(\mu, \sigma^2)$, under $H_0$ we have $\sqrt{n}(\bar x - \mu_0)/\sigma \sim \mathcal{N}(0, 1)$ and $(n-1)s^2/\sigma^2 \sim \chi^2_{n-1}$, independent, and the estimated standard error is $\widehat{\mathrm{se}}(\hat\mu) = s/\sqrt{n}$, so

$$
t = \frac{\bar x - \mu_0}{s/\sqrt{n}} \sim t_{n-1}, \qquad t^2 = \sqrt{n}(\bar x - \mu_0)(s^2)^{-1}\sqrt{n}(\bar x - \mu_0) \sim F_{1,n-1}.
$$
The squared statistic has the structure (normal random variable) $\times$ (scaled $\chi^2$ random variable / degrees of freedom)$^{-1}$ $\times$ (normal random variable), and it generalizes directly.

**Definition 3.2.1 (Hotelling's T² Statistic)** For testing $H_0\colon \boldsymbol{\mu} = \boldsymbol{\mu}_0$ against $H_1\colon \boldsymbol{\mu} \ne \boldsymbol{\mu}_0$, the statistic

$$
T^2 = \sqrt{n}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}\sqrt{n}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0) = n(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)
$$
is called **Hotelling's T² statistic**.

$T^2$ is $n$ times the squared Mahalanobis distance of $\bar{\boldsymbol{X}}$ from $\boldsymbol{\mu}_0$ measured with $S$. By Eq. (3.1), under $H_0$ it has the structure

$$
T^2 = (\text{multivariate normal random vector})^{\mathsf T}\left(\frac{\text{Wishart random matrix}}{\text{degrees of freedom}}\right)^{-1}(\text{multivariate normal random vector}) = \boldsymbol{Z}_1^{\mathsf T}\left[\frac{1}{n-1}\sum_{j=2}^{n}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}\right]^{-1}\boldsymbol{Z}_1,
$$
a $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$ vector against an independent $W_p(n-1, \Sigma)/(n-1)$ matrix. For $p = 1$, $T^2 = t^2$.

### 3.2.2. The Distribution of T²

**Theorem 3.2.1** Let $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ be a random sample from $\mathcal{N}_p(\boldsymbol{\mu}_0, \Sigma)$ with $n > p$. Then

$$
\frac{n-p}{p}\cdot\frac{T^2}{n-1} \sim F_{p,n-p}, \qquad \text{that is,} \qquad T^2 \sim \frac{p(n-1)}{n-p}F_{p,n-p}.
$$

**Proof** By Eq. (3.1), $T^2/(n-1) = \boldsymbol{Z}_1^{\mathsf T}A^{-1}\boldsymbol{Z}_1$ with $A = \sum_{j=2}^{n}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}$ and $\boldsymbol{Z}_1, \dots, \boldsymbol{Z}_n$ iid $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$. We may assume $\Sigma = I_p$: replacing every $\boldsymbol{Z}_j$ by $\Sigma^{-1/2}\boldsymbol{Z}_j$ does not change $\boldsymbol{Z}_1^{\mathsf T}A^{-1}\boldsymbol{Z}_1$. Write

$$
\frac{T^2}{n-1} = \boldsymbol{Z}_1^{\mathsf T}A^{-1}\boldsymbol{Z}_1 = \frac{\boldsymbol{Z}_1^{\mathsf T}\boldsymbol{Z}_1}{1/(\boldsymbol{L}^{\mathsf T}A^{-1}\boldsymbol{L})}, \qquad \boldsymbol{L} = \frac{\boldsymbol{Z}_1}{\|\boldsymbol{Z}_1\|}.
$$
We show that (a) the numerator is $\chi^2_p$; (b) the denominator is $\chi^2_{n-p}$; (c) they are independent. Then $\frac{T^2}{n-1} = \frac{\chi^2_p}{\chi^2_{n-p}}$, i.e. $\frac{n-p}{p}\cdot\frac{T^2}{n-1} \sim F_{p,n-p}$, by the definition of the **F-distribution**. Part (a) is clear.

(b), special case $\boldsymbol{L} = \boldsymbol{e}_p = (0, \dots, 0, 1)^{\mathsf T}$. Write the $(n-1) \times p$ matrix with rows $\boldsymbol{Z}_2^{\mathsf T}, \dots, \boldsymbol{Z}_n^{\mathsf T}$ as $[B, \boldsymbol{y}]$, with $B$ of size $(n-1) \times (p-1)$ and $\boldsymbol{y}$ of size $(n-1) \times 1$. Then

$$
A = \begin{bmatrix} B^{\mathsf T} \\ \boldsymbol{y}^{\mathsf T} \end{bmatrix}[B, \boldsymbol{y}] = \begin{bmatrix} B^{\mathsf T}B & B^{\mathsf T}\boldsymbol{y} \\ \boldsymbol{y}^{\mathsf T}B & \boldsymbol{y}^{\mathsf T}\boldsymbol{y} \end{bmatrix}.
$$
Now $\boldsymbol{e}_p^{\mathsf T}A^{-1}\boldsymbol{e}_p$ is the $(p, p)$ entry of $A^{-1}$, which equals $\det(B^{\mathsf T}B)/\det A$ (cofactor formula), and by the determinant formula for block matrices (the **Schur complement**), $\det A = \det(B^{\mathsf T}B)\cdot[\boldsymbol{y}^{\mathsf T}\boldsymbol{y} - \boldsymbol{y}^{\mathsf T}B(B^{\mathsf T}B)^{-1}B^{\mathsf T}\boldsymbol{y}]$. Hence

$$
\frac{1}{\boldsymbol{e}_p^{\mathsf T}A^{-1}\boldsymbol{e}_p} = \boldsymbol{y}^{\mathsf T}[I_{n-1} - B(B^{\mathsf T}B)^{-1}B^{\mathsf T}]\boldsymbol{y} = \boldsymbol{y}^{\mathsf T}C\boldsymbol{y}.
$$
$C$ is symmetric and idempotent, the **orthogonal projection matrix** onto the orthogonal complement of the column space of $B$, with rank $(n-1) - (p-1) = n - p$. So there is an orthogonal $\Gamma$ with $\Gamma C\Gamma^{\mathsf T} = \operatorname{diag}(I_{n-p}, O)$. The vector $\boldsymbol{y}$ (the last coordinates of $\boldsymbol{Z}_2, \dots, \boldsymbol{Z}_n$) is $\mathcal{N}_{n-1}(\boldsymbol{0}, I)$ and independent of $B$; conditionally on $B$, $\tilde{\boldsymbol{y}} = \Gamma\boldsymbol{y} \sim \mathcal{N}_{n-1}(\boldsymbol{0}, I)$ and $\boldsymbol{y}^{\mathsf T}C\boldsymbol{y} = \tilde{\boldsymbol{y}}^{\mathsf T}\operatorname{diag}(I_{n-p}, O)\tilde{\boldsymbol{y}} = \sum_{i=1}^{n-p}\tilde y_i^2 \sim \chi^2_{n-p}$. Since this conditional distribution does not depend on $B$, $1/(\boldsymbol{e}_p^{\mathsf T}A^{-1}\boldsymbol{e}_p) \sim \chi^2_{n-p}$.

(b), general case. For a fixed unit vector $\boldsymbol{l}$, choose an orthogonal $\Gamma$ whose last row is $\boldsymbol{l}^{\mathsf T}$, so that $\Gamma^{\mathsf T}\boldsymbol{e}_p = \boldsymbol{l}$. Then $\boldsymbol{l}^{\mathsf T}A^{-1}\boldsymbol{l} = \boldsymbol{e}_p^{\mathsf T}(\Gamma A\Gamma^{\mathsf T})^{-1}\boldsymbol{e}_p$ and $\Gamma A\Gamma^{\mathsf T} = \sum_{j=2}^{n}\tilde{\boldsymbol{Z}}_j\tilde{\boldsymbol{Z}}_j^{\mathsf T}$ with $\tilde{\boldsymbol{Z}}_j = \Gamma\boldsymbol{Z}_j$ again iid $\mathcal{N}_p(\boldsymbol{0}, I_p)$. By the special case, $1/(\boldsymbol{l}^{\mathsf T}A^{-1}\boldsymbol{l}) \sim \chi^2_{n-p}$ for every fixed unit vector $\boldsymbol{l}$. The random $\boldsymbol{L} = \boldsymbol{Z}_1/\|\boldsymbol{Z}_1\|$ is independent of $A$, so conditionally on $\boldsymbol{Z}_1$, $1/(\boldsymbol{L}^{\mathsf T}A^{-1}\boldsymbol{L}) \sim \chi^2_{n-p}$.

(c) This conditional distribution given $\boldsymbol{Z}_1$ does not depend on $\boldsymbol{Z}_1$. Hence the denominator is independent of $\boldsymbol{Z}_1$, and in particular of the numerator $\boldsymbol{Z}_1^{\mathsf T}\boldsymbol{Z}_1$, and its unconditional distribution is $\chi^2_{n-p}$. $\square$

The proof has three noteworthy features. It first studies the algebra with all random quantities held fixed, and only then their randomness. It makes two reductions without loss of generality: $\Sigma = I_p$ (multiplying every $\boldsymbol{Z}_j$ by $\Sigma^{-1/2}$) and $\boldsymbol{L} = \boldsymbol{e}_p$ (multiplying every $\boldsymbol{Z}_j$ by an orthogonal matrix); both leave the denominator unchanged. And it separates the sources of randomness of the denominator ($\boldsymbol{L}$, $B$ and $\boldsymbol{y}$): with $\boldsymbol{L}$ and $B$ held fixed, the conditional distribution is $\chi^2_{n-p}$ regardless of their values, which yields both the unconditional distribution and the independence. The degrees of freedom $n - p = (n-1) - (p-1)$ are those of the Wishart matrix minus the $p - 1$ dimensions used up by $B$.

### 3.2.3. The Test

By Theorem 3.2.1, the level-$\alpha$ test of $H_0\colon \boldsymbol{\mu} = \boldsymbol{\mu}_0$ against $H_1\colon \boldsymbol{\mu} \ne \boldsymbol{\mu}_0$ rejects $H_0$ when

$$
T^2 = n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0) > \frac{p(n-1)}{n-p}F_{p,n-p,\alpha}, \tag{3.2}
$$
where $F_{p,n-p,\alpha}$ is the upper $\alpha$ quantile of $F_{p,n-p}$; the right side is the critical value, written $T^2_\alpha$ below. The statistic and its distribution are named after Harold Hotelling (1895–1973), who introduced them in 1931 as the generalization of Student's $t$.

**Example 3.2.1** In Example 3.1.1 ($n = 55$, $p = 6$, $\alpha = 0.05$), the critical value is $\frac{6 \cdot 54}{49}F_{6,49,0.05} = 15.145$.

- For $H_{01}\colon \boldsymbol{\mu} = (5.0, 5.0, 4.7, 3.6, 4.6, 5.0)^{\mathsf T}$, $T^2 = 9.053 < 15.145$: $H_{01}$ is not rejected.
- For $H_{02}\colon \boldsymbol{\mu} = (5.0, 5.0, 4.8, 3.6, 4.6, 5.0)^{\mathsf T}$, $T^2 = 20.840 > 15.145$: $H_{02}$ is rejected.

The two hypotheses differ only in the Recognition component (sample mean $4.717$), by $0.1$. The first is compatible with the data and the second is not, although each component of both is within about $0.12$ of the sample mean; whether a deviation is large depends on the variances and correlations of the components, which $T^2$ takes into account through $S^{-1}$.

**Property 3.2.1 (Invariance)** $T^2$ is invariant under changes of the units of measurement and, more generally, under nonsingular affine transformations: if $\boldsymbol{y}_j = C\boldsymbol{x}_j + \boldsymbol{d}$ with $C$ a $p \times p$ invertible matrix, and the hypothesis is transformed accordingly to $\boldsymbol{\mu}_{Y,0} = C\boldsymbol{\mu}_0 + \boldsymbol{d}$, then the $T^2$ computed from the $\boldsymbol{y}_j$ equals the $T^2$ computed from the $\boldsymbol{x}_j$.

**Proof** By Theorem 2.2.2, $\bar{\boldsymbol{y}} = C\bar{\boldsymbol{x}} + \boldsymbol{d}$ and $S_Y = CSC^{\mathsf T}$. Hence

$$
\begin{aligned}
T^2_Y &= n(\bar{\boldsymbol{y}} - \boldsymbol{\mu}_{Y,0})^{\mathsf T}S_Y^{-1}(\bar{\boldsymbol{y}} - \boldsymbol{\mu}_{Y,0}) = n[C(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)]^{\mathsf T}(CSC^{\mathsf T})^{-1}C(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0) \\
&= n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}C^{\mathsf T}(C^{\mathsf T})^{-1}S^{-1}C^{-1}C(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0) = n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0). \quad \square
\end{aligned}
$$

## 3.3. Confidence Regions

In one dimension, with $z_1, \dots, z_n$ iid $\mathcal{N}(\psi, \sigma_\psi^2)$, the pivot $\left(\frac{\bar z - \psi}{s/\sqrt{n}}\right)^2 \sim F_{1,n-1}$ gives the confidence interval

$$
I(\boldsymbol{z}) = \bar z \pm t_{n-1,\alpha/2}\frac{s}{\sqrt{n}} = \{\psi\colon n(\bar z - \psi)(s^2)^{-1}(\bar z - \psi) \le c^2\}, \qquad c^2 = t_{n-1,\alpha/2}^2 = F_{1,n-1,\alpha},
$$
with coverage $\mathbb{P}_\psi(I(\boldsymbol{z}) \ni \psi) = \mathbb{P}(\lvert t_{n-1}\rvert \le t_{n-1,\alpha/2}) = 1 - \alpha$. The statistic is the same as for the test; the difference is that the test fixes $\mu_0$ and looks at the data, while the interval fixes the data and collects all parameter values that would not be rejected. The same inversion works for a mean vector.

**Theorem 3.3.1 (Confidence Region for a Mean Vector)** Let $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ be a random sample from $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ with $n > p$. The set

$$
R(X) = \{\boldsymbol{\mu}\colon n(\bar{\boldsymbol{X}} - \boldsymbol{\mu})^{\mathsf T}S^{-1}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}) \le c^2\}, \qquad c^2 = T^2_\alpha = \frac{p(n-1)}{n-p}F_{p,n-p,\alpha},
$$
is a $100(1 - \alpha)\%$ **confidence region** for $\boldsymbol{\mu}$: $\mathbb{P}_{\boldsymbol{\mu}}(R(X) \ni \boldsymbol{\mu}) = 1 - \alpha$.

The coverage is Theorem 3.2.1 with $\boldsymbol{\mu}_0$ replaced by the true $\boldsymbol{\mu}$. The region consists of exactly those $\boldsymbol{\mu}_0$ for which the test (3.2) does not reject. To decide whether a given $\boldsymbol{\mu}_0$ lies in it, compute $T^2$ for $\boldsymbol{\mu}_0$ and compare it with $c^2$.

Geometrically, $R(X)$ is a solid ellipsoid centered at $\bar{\boldsymbol{x}}$. If $S$ has eigenvalues $\lambda_1 \ge \cdots \ge \lambda_p > 0$ and eigenvectors $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$, then by Theorem 2.3.1 (with $\Sigma$ replaced by $S/n$) its axes are

$$
\pm\sqrt{\lambda_i}\,\frac{c}{\sqrt{n}}\,\boldsymbol{e}_i = \pm\sqrt{\lambda_i}\sqrt{\frac{p(n-1)}{n(n-p)}F_{p,n-p,\alpha}}\,\boldsymbol{e}_i, \qquad i = 1, \dots, p.
$$
The ellipsoid is long in the directions in which the data vary most and shrinks at the rate $1/\sqrt{n}$. For $p = 2$ it can be drawn: for the Achievement and Recognition ratings of Example 3.1.1 ($n = 55$), whose sample correlation is strongly positive, the $95\%$ confidence ellipse is a thin ellipse tilted along the diagonal around $(5.12, 4.72)$, small compared with the scatter of the data. For $p \ge 4$ the ellipsoid cannot be visualized, and one reports intervals instead.

## 3.4. Simultaneous Confidence Intervals

### 3.4.1. Intervals for a Single Linear Combination

An integrated value such as $\frac{1}{2}\mu_1 + \frac{1}{2}\mu_2 = (\frac{1}{2}, \frac{1}{2}, 0, 0, 0, 0)\boldsymbol{\mu}$ is a linear combination $\psi = \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$. For a fixed $\boldsymbol{a}$, the values $z_j = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}_j$ are iid $\mathcal{N}(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a})$ (Theorem 2.4.1), with sample mean $\bar z = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}}$ and sample variance $s_z^2 = \boldsymbol{a}^{\mathsf T}S\boldsymbol{a}$ (Theorem 2.2.2). The one-dimensional $t$ interval applies to them: $\hat\psi = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}}$, $\widehat{\mathrm{se}}(\hat\psi) = s_z/\sqrt{n}$, and a $100(1 - \beta)\%$ confidence interval for $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ is

$$
I_{\boldsymbol{a}} = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}} \pm t_{n-1,\beta/2}\sqrt{\frac{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}}{n}}. \tag{3.3}
$$
With $\boldsymbol{a} = \boldsymbol{e}_k$ this is the usual interval for the component mean $\mu_k$. For the two-variable sub-data set (Achievement, Recognition) with $n = 55$ and $\beta = 0.05$, the multiplier is $t_{54,0.025} = 2.005$.

### 3.4.2. Simultaneous Coverage and Bonferroni Intervals

Each interval (3.3) is correct with probability $1 - \beta$: $\mathbb{P}(I_{\boldsymbol{a}_k} \ni \boldsymbol{a}_k^{\mathsf T}\boldsymbol{\mu}) = 1 - \beta$. When $m$ such intervals are reported together, the probability that all of them are correct is smaller, and it is this probability that matters if conclusions are drawn from all of them at once.

**Definition 3.4.1 (Simultaneous Confidence Intervals)** Intervals $I_1, \dots, I_m$ for $\psi_k = \boldsymbol{a}_k^{\mathsf T}\boldsymbol{\mu}$, $k = 1, \dots, m$, are **simultaneous confidence intervals** with confidence level $1 - \alpha$ if

$$
\mathbb{P}(I_k \ni \psi_k \text{ for all } k = 1, \dots, m) \ge 1 - \alpha.
$$
In contrast, an individual confidence interval only satisfies $\mathbb{P}(I_k \ni \psi_k) \ge 1 - \alpha$ for each $k$ separately.

Simultaneous coverage is a requirement, not a method; the course presents two common ways to meet it. Let $C_k$ be the event that $I_{\boldsymbol{a}_k}$ covers $\psi_k$, each interval having level $1 - \beta$. By Bonferroni's inequality,

$$
\mathbb{P}(\text{some } C_k \text{ false}) \le \sum_{k=1}^{m}\mathbb{P}(C_k \text{ false}) = m\beta, \qquad \text{so} \qquad \mathbb{P}(\text{all } C_k \text{ true}) \ge 1 - m\beta.
$$
Choosing $\beta = \alpha/m$ (the **Bonferroni correction** of [3.2.4](/3.2.4)) gives the Bonferroni intervals

$$
\boldsymbol{a}_k^{\mathsf T}\bar{\boldsymbol{X}} \pm t_{n-1,\alpha/(2m)}\sqrt{\frac{\boldsymbol{a}_k^{\mathsf T}S\boldsymbol{a}_k}{n}}, \qquad k = 1, \dots, m, \tag{3.4}
$$
with simultaneous level at least $1 - \alpha$, whatever the dependence between the intervals. They are conservative. Bonferroni's method lets every linear combination bear the error rate equally: with $m = 5$ and $\alpha = 0.05$, every interval is computed at level $99\%$, rather than some at $98.5\%$ and others at $99.5\%$ (an unequal split is also valid but must be fixed in advance).

### 3.4.3. T² Intervals

Can a single multiplier $c$ make the intervals $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}} \pm c\sqrt{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}/n}$ cover $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ for all $\boldsymbol{a} \ne \boldsymbol{0}$ simultaneously? The interval for $\boldsymbol{a}$ covers if and only if $t_{\boldsymbol{a}}^2 \le c^2$, where

$$
t_{\boldsymbol{a}}^2 = \frac{n[\boldsymbol{a}^{\mathsf T}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})]^2}{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}},
$$
so all of them cover if and only if $\max_{\boldsymbol{a}}t_{\boldsymbol{a}}^2 \le c^2$. By the maximization lemma (Lemma 1.7.2, with $B = S$ and $\boldsymbol{d} = \bar{\boldsymbol{x}} - \boldsymbol{\mu}$),

$$
\max_{\boldsymbol{a} \ne \boldsymbol{0}}t_{\boldsymbol{a}}^2 = n\max_{\boldsymbol{a} \ne \boldsymbol{0}}\frac{[\boldsymbol{a}^{\mathsf T}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})]^2}{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}} = n(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}) = T^2,
$$
attained at $\boldsymbol{a} \propto S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})$. The event that all intervals cover is therefore exactly the event $T^2 \le c^2$ that the confidence region of Theorem 3.3.1 covers $\boldsymbol{\mu}$.

**Theorem 3.4.1 (T² Simultaneous Confidence Intervals)** Let $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ be a random sample from $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ with $n > p$. Then

$$
\mathbb{P}\left(\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}} - c\sqrt{\frac{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}}{n}} \le \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu} \le \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}} + c\sqrt{\frac{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}}{n}} \text{ for all } \boldsymbol{a}\right) = 1 - \alpha, \qquad c^2 = \frac{p(n-1)}{n-p}F_{p,n-p,\alpha}. \tag{3.5}
$$

For $\boldsymbol{a} = \boldsymbol{e}_1, \dots, \boldsymbol{e}_p$, the $T^2$ intervals for the component means are $\bar x_k \pm c\sqrt{s_{kk}/n}$. Geometrically, the $T^2$ interval for $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ is the projection of the confidence ellipsoid onto the direction $\boldsymbol{a}$: the maximum and minimum of $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ over $R(X)$ are $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}} \pm c\sqrt{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}/n}$, again by the maximization lemma. In the plane, the $T^2$ intervals for $\mu_1$ and $\mu_2$ are the shadows of the confidence ellipse on the two axes, which is not a coincidence.

**Remark 3.4.1** The vector $\boldsymbol{a}$ need not have unit length, either in the derivation or in the result. The ratio $t_{\boldsymbol{a}}^2$ does not change when $\boldsymbol{a}$ is rescaled, and the multiplier $c$, obtained once from the confidence region, is shared by the intervals for all $\boldsymbol{a}$; there is no need to repeat the maximization for a particular $\boldsymbol{a}$. On the other hand, the interval for a given $\boldsymbol{a}$ keeps the scale of $\boldsymbol{a}$: the interval for $100\,\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ is $100$ times that for $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$, as it should be.

**Remark 3.4.2** All three kinds of intervals (individual $t$, Bonferroni, $T^2$) are one-dimensional intervals for one-dimensional quantities $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$; only the confidence region is a $p$-dimensional set. When the intervals for $\mu_1$ and $\mu_2$ are drawn as a rectangle, this is only to compare their lengths with one another and with the confidence ellipse. The three kinds of intervals have the same form $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}} \pm c\sqrt{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}/n}$ and differ only in the multiplier $c$.

![Simulated data resembling the Achievement and Recognition ratings (n = 55): the 95% confidence ellipse for the mean vector and, as rectangles, the individual t intervals, the Bonferroni intervals (m = 2) and the T^2 intervals for the two component means. The T^2 rectangle is the shadow of the ellipse on the axes.](./plots/t2-confidence-ellipse.py)

### 3.4.4. Comparing the Intervals

| Intervals | Multiplier $c$ | Coverage |
|---|---|---|
| Individual $t$ | $t_{n-1,\alpha/2}$ | $1 - \alpha$ for each interval separately |
| Bonferroni | $t_{n-1,\alpha/(2m)}$ | at least $1 - \alpha$ for $m$ prespecified combinations |
| $T^2$ | $\sqrt{\frac{p(n-1)}{n-p}F_{p,n-p,\alpha}}$ | exactly $1 - \alpha$ for all combinations, including those chosen after seeing the data |

For the two-variable example ($n = 55$, $p = 2$, $\alpha = 0.05$), the multipliers are $2.005$ (individual), $2.306$ (Bonferroni, $m = 2$), $2.670$ (Bonferroni, $m = 5$) and $2.542$ ($T^2$). Only the Bonferroni multiplier depends on the number $m$ of linear combinations: for the $p$ component means ($m = p$) the Bonferroni intervals are shorter than the $T^2$ intervals, but as $m$ grows they become longer, and the $T^2$ intervals remain valid for any number of combinations, even those suggested by the data. Both multipliers grow with the dimension $p$; the $T^2$ multiplier grows much faster, since it protects infinitely many combinations.

![Multipliers c of the three kinds of 95% intervals as functions of the dimension p, for n = 200: individual t intervals (constant), Bonferroni intervals for m = p combinations, and T^2 intervals.](./plots/critical-values.py)

In practice: use individual intervals only for a single quantity of prior interest; use Bonferroni intervals for a small number of combinations fixed in advance, typically the $p$ component means; use $T^2$ intervals when many combinations are examined or when they are chosen after looking at the data.

## 3.5. Hotelling's T² and the Likelihood Ratio Test

The $T^2$ test was constructed by analogy with the $t$ test. It is also the **likelihood ratio test** ([3.2.5](/3.2.5)) for $H_0\colon \boldsymbol{\mu} = \boldsymbol{\mu}_0$, which confirms that it is the natural choice.

**Theorem 3.5.1** Let $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ be a random sample from $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ with $n > p$, and let

$$
\hat\Sigma = \frac{1}{n}\sum_{j=1}^{n}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}, \qquad \hat\Sigma_0 = \frac{1}{n}\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu}_0)(\boldsymbol{x}_j - \boldsymbol{\mu}_0)^{\mathsf T}.
$$
The likelihood ratio for $H_0\colon \boldsymbol{\mu} = \boldsymbol{\mu}_0$ against $H_1\colon \boldsymbol{\mu} \ne \boldsymbol{\mu}_0$ is

$$
\Lambda = \frac{\max_{\Sigma}L(\boldsymbol{\mu}_0, \Sigma)}{\max_{\boldsymbol{\mu}, \Sigma}L(\boldsymbol{\mu}, \Sigma)} = \left(\frac{\det\hat\Sigma}{\det\hat\Sigma_0}\right)^{n/2} = \left(1 + \frac{T^2}{n-1}\right)^{-n/2}.
$$
Hence the likelihood ratio test, which rejects for small $\Lambda$, is equivalent to the $T^2$ test, which rejects for large $T^2$.

**Proof** The denominator is $(2\pi)^{-np/2}\mathrm{e}^{-np/2}(\det\hat\Sigma)^{-n/2}$ (Theorem 2.5.1 and the value of the maximized likelihood in [3.4.2](/3.4.2)). With $\boldsymbol{\mu} = \boldsymbol{\mu}_0$ fixed, the same argument as in the proof of Theorem 2.5.1 shows that $L(\boldsymbol{\mu}_0, \Sigma)$ is maximized at $\Sigma = \hat\Sigma_0$, with maximum $(2\pi)^{-np/2}\mathrm{e}^{-np/2}(\det\hat\Sigma_0)^{-n/2}$. This gives the first expression.

For the second, consider the $(p + 1) \times (p + 1)$ block matrix

$$
A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} = \begin{bmatrix} n\hat\Sigma & \sqrt{n}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0) \\ \sqrt{n}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T} & -1 \end{bmatrix}
$$
and compute its determinant in two ways using $\det A = \det A_{22}\det(A_{11} - A_{12}A_{22}^{-1}A_{21}) = \det A_{11}\det(A_{22} - A_{21}A_{11}^{-1}A_{12})$. The first gives

$$
\det A = (-1)\det\left(n\hat\Sigma + n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}\right) = (-1)\det(n\hat\Sigma_0),
$$
since $\sum_j(\boldsymbol{x}_j - \boldsymbol{\mu}_0)(\boldsymbol{x}_j - \boldsymbol{\mu}_0)^{\mathsf T} = \sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T} + n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}$. The second, with $n\hat\Sigma = (n-1)S$, gives

$$
\det A = \det(n\hat\Sigma)\left(-1 - n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}[(n-1)S]^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)\right) = (-1)\det(n\hat\Sigma)\left(1 + \frac{T^2}{n-1}\right).
$$
Comparing, $\det\hat\Sigma_0 = \det\hat\Sigma\,(1 + T^2/(n-1))$. $\square$

In one dimension the identity is the familiar decomposition $\sum_j(x_j - \mu_0)^2 = \sum_j(x_j - \bar x)^2 + n(\bar x - \mu_0)^2$, which gives $\hat\sigma_0^2/\hat\sigma^2 = 1 + t^2/(n-1)$. Theorem 3.5.1 also yields a formula for $T^2$ that avoids inverting $S$:

$$
T^2 = \frac{(n-1)\det\hat\Sigma_0}{\det\hat\Sigma} - (n-1) = (n-1)\frac{\det\left(\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu}_0)(\boldsymbol{x}_j - \boldsymbol{\mu}_0)^{\mathsf T}\right)}{\det\left(\sum_{j=1}^{n}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}\right)} - (n-1).
$$
The likelihood ratio approach extends to hypotheses for which no $T^2$ analogue is apparent, and for large $n$, $-2\log\Lambda = n\log(1 + T^2/(n-1))$ is approximately $\chi^2_p$ under $H_0$ ([3.4.4](/3.4.4)).

## Summary

- Normal sample: $\bar{\boldsymbol{X}} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma/n)$, $(n-1)S \sim W_p(n-1, \Sigma)$, independent; the Wishart distribution $W_p(m, \Sigma)$ is the distribution of $\sum_{j=1}^{m}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}$ with $\boldsymbol{Z}_j$ iid $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$, the analogue of $\sigma^2\chi^2_m$.
- Hotelling's $T^2 = n(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)$ generalizes $t^2$; under $H_0$, $\frac{n-p}{p(n-1)}T^2 \sim F_{p,n-p}$; reject when $T^2 > \frac{p(n-1)}{n-p}F_{p,n-p,\alpha}$. $T^2$ is invariant under nonsingular affine transformations and is equivalent to the likelihood ratio test, $\Lambda = (1 + T^2/(n-1))^{-n/2}$.
- Confidence region: the ellipsoid $\{\boldsymbol{\mu}\colon n(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}) \le c^2\}$ with axes $\pm\sqrt{\lambda_i}\,c\,\boldsymbol{e}_i/\sqrt{n}$.
- Intervals for $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ have the form $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}} \pm c\sqrt{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}/n}$: $c = t_{n-1,\alpha/2}$ (individual), $t_{n-1,\alpha/(2m)}$ (Bonferroni, $m$ combinations), $\sqrt{p(n-1)F_{p,n-p,\alpha}/(n-p)}$ ($T^2$, all combinations, the projections of the confidence ellipsoid). Simultaneous coverage is the new idea of the chapter.
