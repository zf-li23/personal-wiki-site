---
title: The Multivariate Normal Distribution
source_hash: 914bfffed48e
---

The normal distribution is important for two reasons: the central limit theorem ([3.1.13](/3.1.13)), and the fact that it is closed under linear operations and easy to compute with. This chapter extends it to random vectors. [3.1.6](/3.1.6) defined the bivariate normal distribution through its joint density; in general dimension a more convenient definition is "a linear transformation of independent standard normal random variables". From it we derive, in a unified way, the joint density, the characteristic function, the marginal distributions, linear transformations, criteria for independence and the conditional distributions; the main tools are characteristic functions ([3.1.11](/3.1.11)) and matrix algebra ([2.1](/2.1)). These properties of the multivariate normal distribution underlie the sampling distributions of normal populations in statistical inference ([3.2.2](/3.2.2)), linear regression and multivariate statistical analysis. The chapter ends with the law of large numbers and the central limit theorem for random vectors.

## 15.1. Mean Vector and Covariance Matrix of a Random Vector

This section agrees with the treatment of covariance matrices in [3.1.10](/3.1.10); here we collect the rules of calculation in matrix form. All vectors are column vectors.

Let $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ be a random vector. If $\mu_i = \mathbb{E}X_i$ exists for every $i$, we say that the expectation of $\boldsymbol{X}$ exists and define

$$
\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X} = (\mathbb{E}X_1, \dots, \mathbb{E}X_n)^{\mathsf T} = (\mu_1, \dots, \mu_n)^{\mathsf T}.
$$
Similarly, for a matrix $Y = (X_{ij})_{m \times n}$ whose entries are random variables, we define $\mathbb{E}Y = (\mathbb{E}X_{ij})_{m \times n}$.

**Property 15.1.1** Suppose the expectations of the random vector $\boldsymbol{X}$ and the random matrix $Y$ exist, $\boldsymbol{a} = (a_1, \dots, a_n)^{\mathsf T}$ is a constant vector, and $A_{k \times m}$, $B_{n \times j}$ are constant matrices (with dimensions making the operations meaningful). Then

1. $\mathbb{E}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{a}^{\mathsf T}\mathbb{E}\boldsymbol{X}$;
2. $(\mathbb{E}Y)^{\mathsf T} = \mathbb{E}(Y^{\mathsf T})$;
3. $\mathbb{E}(AY) = A\,\mathbb{E}Y$;
4. $\mathbb{E}(YB) = (\mathbb{E}Y)B$;
5. $\mathbb{E}(AYB) = A(\mathbb{E}Y)B$.

All of these are essentially the linearity of expectation: for instance, the $(i, l)$ entry of $AY$ is $\sum_s a_{is}X_{sl}$, whose expectation is $\sum_s a_{is}\mathbb{E}X_{sl}$.

The covariance matrix of $\boldsymbol{X}$ (Definition 10.5.1) is

$$
\Sigma = \operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}] = (\sigma_{ij})_{n \times n}, \quad \sigma_{ij} = \operatorname{Cov}(X_i, X_j).
$$
It is a symmetric positive semidefinite matrix, and $\det\Sigma = 0$ (in which case $\Sigma$ is called degenerate) if and only if there are constants $a_1, \dots, a_n$, not all zero, with $\sum_{i=1}^{n} a_i(X_i - \mathbb{E}X_i) = 0$ a.s. (Theorem 10.5.1). The key to the proof is $\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} = \operatorname{Var}\left(\sum_i a_i(X_i - \mathbb{E}X_i)\right) \ge 0$.

**Property 15.1.2** Let $\boldsymbol{X}$ have covariance matrix $\Sigma$, let $A$ be a constant matrix and $\boldsymbol{b}$ a constant vector. Then

$$
\mathbb{E}(\boldsymbol{b} + A\boldsymbol{X}) = \boldsymbol{b} + A\boldsymbol{\mu}, \qquad \operatorname{Cov}(\boldsymbol{b} + A\boldsymbol{X}) = A\Sigma A^{\mathsf T}.
$$

**Proof** By Property 15.1.1, $\operatorname{Cov}(\boldsymbol{b} + A\boldsymbol{X}) = \mathbb{E}[A(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}A^{\mathsf T}] = A\,\mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}]\,A^{\mathsf T} = A\Sigma A^{\mathsf T}$. $\square$

In particular, $\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}$.

## 15.2. Definition of the Multivariate Normal Distribution

**Definition 15.2.1 (Multivariate Normal Distribution)** Let $\boldsymbol{\mu} = (\mu_1, \dots, \mu_n)^{\mathsf T}$ be an $n$-dimensional constant column vector, $B$ an $n \times m$ constant matrix, and $\varepsilon_1, \dots, \varepsilon_m$ mutually independent standard normal random variables, $\boldsymbol{\varepsilon} = (\varepsilon_1, \dots, \varepsilon_m)^{\mathsf T}$. If

$$
\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}
$$
and the matrix $BB^{\mathsf T}$ has full rank, then $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ is said to have the $n$-dimensional normal distribution, or **multivariate normal distribution** (MVN), written $\boldsymbol{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, BB^{\mathsf T})$, or simply $\mathcal{N}(\boldsymbol{\mu}, BB^{\mathsf T})$ when the dimension is clear.

The components of $\boldsymbol{\varepsilon}$ are independent with variance $1$, so $\mathbb{E}\boldsymbol{\varepsilon} = \boldsymbol{0}$ and $\operatorname{Cov}(\boldsymbol{\varepsilon}) = \mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^{\mathsf T}) = I_m$. By Property 15.1.2,

$$
\mathbb{E}\boldsymbol{X} = \boldsymbol{\mu} + B\,\mathbb{E}\boldsymbol{\varepsilon} = \boldsymbol{\mu}, \qquad \Sigma := \operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[(B\boldsymbol{\varepsilon})(B\boldsymbol{\varepsilon})^{\mathsf T}] = B\,\mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^{\mathsf T})\,B^{\mathsf T} = BI_mB^{\mathsf T} = BB^{\mathsf T}.
$$
So the two parameters in the notation $\mathcal{N}(\boldsymbol{\mu}, \Sigma)$ are exactly the mean vector and the covariance matrix. Full rank of $BB^{\mathsf T}$ means that $\Sigma$ is positive definite, which requires $m \ge n$. Conversely, for any positive definite matrix $\Sigma$, taking $B = \Sigma^{1/2}$ (or the lower triangular factor of the Cholesky decomposition) makes $\boldsymbol{\mu} + B\boldsymbol{\varepsilon}$ distributed as $\mathcal{N}(\boldsymbol{\mu}, \Sigma)$, so every positive definite matrix is the covariance matrix of some multivariate normal distribution.

**Example 15.2.1** Let $\varepsilon_1, \varepsilon_2$ be iid $\mathcal{N}(0, 1)$ and

$$
\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix} + \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} \varepsilon_1 \\ \varepsilon_2 \end{pmatrix}.
$$
Then $(X_1, X_2)^{\mathsf T} \sim \mathcal{N}\left(\begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}\right)$. By Theorem 15.4.2 below, $X_1 = \mu_1 + \varepsilon_1 + \varepsilon_2$ and $X_2 = \mu_2 + \varepsilon_1 - \varepsilon_2$ are independent.

**Theorem 15.2.1 (Density Function)** When $\Sigma$ is positive definite, $\boldsymbol{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \Sigma)$ has the joint density

$$
f(\boldsymbol{x}) = \frac{1}{(\sqrt{2\pi})^n\sqrt{\det\Sigma}}\exp\left[-\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\right], \quad \boldsymbol{x} \in \mathbb{R}^n. \tag{15.1}
$$

**Proof** We show below that the distribution of $\boldsymbol{X}$ depends only on $\boldsymbol{\mu}$ and $\Sigma$ (Theorem 15.2.2), so we may choose an invertible square matrix $B$ with $\Sigma = BB^{\mathsf T}$ and set $\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}$ with $\boldsymbol{\varepsilon} \sim \mathcal{N}_n(\boldsymbol{0}, I_n)$. The components of $\boldsymbol{\varepsilon}$ are independent, with density

$$
f_{\boldsymbol{\varepsilon}}(\boldsymbol{y}) = \prod_{i=1}^{n}\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-y_i^2/2} = \frac{1}{(\sqrt{2\pi})^n}\exp\left(-\frac{1}{2}\boldsymbol{y}^{\mathsf T}\boldsymbol{y}\right).
$$
The map $\boldsymbol{y} = B^{-1}(\boldsymbol{x} - \boldsymbol{\mu})$ is invertible, $\{\boldsymbol{X} = \boldsymbol{x}\} = \{\boldsymbol{\varepsilon} = B^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\}$, and the absolute value of the Jacobian determinant is $\lvert \det B^{-1} \rvert = 1/\sqrt{\det\Sigma}$ (since $\det\Sigma = (\det B)^2$). By the change-of-variables formula for densities of functions of random vectors ([3.1.7](/3.1.7)),

$$
f(\boldsymbol{x}) = \frac{1}{(\sqrt{2\pi})^n}\exp\left\{-\frac{1}{2}[B^{-1}(\boldsymbol{x} - \boldsymbol{\mu})]^{\mathsf T}[B^{-1}(\boldsymbol{x} - \boldsymbol{\mu})]\right\}\frac{1}{\sqrt{\det\Sigma}},
$$
and since $(B^{-1})^{\mathsf T}B^{-1} = (BB^{\mathsf T})^{-1} = \Sigma^{-1}$, Eq. (15.1) follows. $\square$

For $n = 2$ and $\Sigma = \begin{pmatrix} \sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}$, Eq. (15.1) is exactly the density of the bivariate normal distribution $\mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$ of [3.1.6](/3.1.6) (Definition 6.4.1). The contours $(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) = c$ of the density are ellipsoids centered at $\boldsymbol{\mu}$, with principal axes along the eigenvectors of $\Sigma$ and semi-axes proportional to the square roots of the eigenvalues.

![Density contours of the bivariate normal distribution N(0, 0, 1, 1, rho) and the conditional expectation line E(Y | X = x) = rho x (rho = -0.7, 0, 0.7)](./plots/bivariate-normal-contours.py)

**Theorem 15.2.2 (Characteristic Function)** The characteristic function of $\boldsymbol{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \Sigma)$ is

$$
\varphi_{\boldsymbol{X}}(\boldsymbol{t}) = \mathbb{E}\exp(\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{X}) = \exp\left[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}\Sigma\boldsymbol{t}\right], \quad \boldsymbol{t} \in \mathbb{R}^n.
$$

**Proof** First the characteristic function of $\boldsymbol{\varepsilon}$: by the independence of the components and Example 11.3.6, for $\boldsymbol{s} \in \mathbb{R}^m$,

$$
\varphi_{\boldsymbol{\varepsilon}}(\boldsymbol{s}) = \mathbb{E}\left[\prod_{j=1}^{m}\exp(\mathrm{i}s_j\varepsilon_j)\right] = \prod_{j=1}^{m}\mathbb{E}\exp(\mathrm{i}s_j\varepsilon_j) = \prod_{j=1}^{m}\exp\left(-\frac{s_j^2}{2}\right) = \exp\left(-\frac{\boldsymbol{s}^{\mathsf T}\boldsymbol{s}}{2}\right).
$$
Hence

$$
\varphi_{\boldsymbol{X}}(\boldsymbol{t}) = \mathbb{E}\exp[\mathrm{i}(\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} + \boldsymbol{t}^{\mathsf T}B\boldsymbol{\varepsilon})] = \exp(\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu})\,\varphi_{\boldsymbol{\varepsilon}}(B^{\mathsf T}\boldsymbol{t}) = \exp\left[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}BB^{\mathsf T}\boldsymbol{t}\right]. \quad \square
$$

Thus the mean vector and covariance matrix of $\boldsymbol{X}$ uniquely determine its characteristic function; since the characteristic function and the distribution function of a random vector determine each other, the multivariate normal distribution is uniquely determined by $\boldsymbol{\mu}$ and $\Sigma$, regardless of the choice of $B$ in the representation $\Sigma = BB^{\mathsf T}$. Both the joint density (Theorem 15.2.1) and the characteristic function (Theorem 15.2.2) can serve as equivalent definitions of the multivariate normal distribution.

## 15.3. Marginal Distributions and Linear Transformations

**Theorem 15.3.1** If $\boldsymbol{X}$ has a multivariate normal distribution, then any subvector $(X_{j_1}, \dots, X_{j_k})^{\mathsf T}$ of $\boldsymbol{X}$ is also (multivariate) normal, with mean vector and covariance matrix given by the corresponding components of $\boldsymbol{\mu}$ and the corresponding submatrix of $\Sigma$.

**Proof** Write $\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}$ and let $B_1$ consist of rows $j_1, \dots, j_k$ of $B$. Then $(X_{j_1}, \dots, X_{j_k})^{\mathsf T} = (\mu_{j_1}, \dots, \mu_{j_k})^{\mathsf T} + B_1\boldsymbol{\varepsilon}$. The matrix $B_1B_1^{\mathsf T}$ is a principal submatrix of the positive definite matrix $BB^{\mathsf T}$ and is therefore positive definite, and the claim follows from the definition. $\square$

For example, in Example 15.2.1, $X_1 = \mu_1 + \varepsilon_1 + \varepsilon_2 \sim \mathcal{N}(\mu_1, 2)$.

**Theorem 15.3.2** If $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$, then for any constant matrix $A$ and constant vector $\boldsymbol{b}$ such that $\boldsymbol{b} + A\boldsymbol{X}$ is defined and $A\Sigma A^{\mathsf T}$ has full rank,

$$
\boldsymbol{Y} = \boldsymbol{b} + A\boldsymbol{X} \sim \mathcal{N}\left(\boldsymbol{b} + A\boldsymbol{\mu}, A\Sigma A^{\mathsf T}\right).
$$

**Proof** By definition there are an $n \times m$ constant matrix $B$ and independent standard normal $\varepsilon_1, \dots, \varepsilon_m$ with $\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}$. Then $\boldsymbol{Y} = (\boldsymbol{b} + A\boldsymbol{\mu}) + (AB)\boldsymbol{\varepsilon}$, and $(AB)(AB)^{\mathsf T} = A\Sigma A^{\mathsf T}$ has full rank, so by the definition again $\boldsymbol{Y}$ is multivariate normal, with mean vector and covariance matrix given by Property 15.1.2. $\square$

**Example 15.3.1** Let

$$
\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} 1 \\ -5 \end{pmatrix}, \begin{pmatrix} 4 & -2 \\ -2 & 9 \end{pmatrix}\right), \qquad \begin{pmatrix} Y_1 \\ Y_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} X_1 \\ X_2 \end{pmatrix}.
$$
Then $\boldsymbol{b} + A\boldsymbol{\mu} = (2, -4)^{\mathsf T}$ and

$$
A\Sigma A^{\mathsf T} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 4 & -2 \\ -2 & 9 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 2 & 9 \end{pmatrix},
$$
so $(Y_1, Y_2)^{\mathsf T} = (1 + X_1, X_1 + X_2)^{\mathsf T} \sim \mathcal{N}\left(\begin{pmatrix} 2 \\ -4 \end{pmatrix}, \begin{pmatrix} 4 & 2 \\ 2 & 9 \end{pmatrix}\right)$.

Taking $A$ to be a row vector $\boldsymbol{a}^{\mathsf T}$ gives the one-dimensional case. Its converse also holds, and this is the most practical tool for recognizing a multivariate normal distribution.

**Theorem 15.3.3 (Characterization by Linear Combinations)** $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ if and only if, for every $\boldsymbol{a} = (a_1, \dots, a_n)^{\mathsf T} \in \mathbb{R}^n$,

$$
Y := \boldsymbol{a}^{\mathsf T}\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}).
$$
(For $\boldsymbol{a} = \boldsymbol{0}$ this is read as the "normal distribution" $\mathcal{N}(0, 0)$ degenerate at a constant.)

**Proof** Necessity: the characteristic function of $Y$ is

$$
\varphi_Y(t) = \mathbb{E}\exp(\mathrm{i}tY) = \mathbb{E}\exp[\mathrm{i}(t\boldsymbol{a})^{\mathsf T}\boldsymbol{X}] = \exp\left[\mathrm{i}t(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}) - \frac{1}{2}t^2\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}\right], \tag{15.2}
$$
so $Y \sim \mathcal{N}(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a})$. Sufficiency: setting $t = 1$ in Eq. (15.2),

$$
\mathbb{E}\exp(\mathrm{i}\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \varphi_Y(1) = \exp\left[\mathrm{i}\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}\right]
$$
holds for every $\boldsymbol{a}$; this is precisely the characteristic function of $\mathcal{N}(\boldsymbol{\mu}, \Sigma)$, so by uniqueness $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$. $\square$

For example, $(X_1, X_2)^{\mathsf T} \sim \mathcal{N}\left(\begin{pmatrix} 1 \\ -5 \end{pmatrix}, \begin{pmatrix} 4 & -2 \\ -2 & 9 \end{pmatrix}\right)$ if and only if $a_1X_1 + a_2X_2 \sim \mathcal{N}(a_1 - 5a_2, 4a_1^2 - 4a_1a_2 + 9a_2^2)$ for all $a_1, a_2$.

**Remark 15.3.1** Theorem 15.3.3 requires every linear combination to be normal; normality of each component is not enough. Let $X \sim \mathcal{N}(0, 1)$, let $S$ be independent of $X$ with $\mathbb{P}(S = 1) = \mathbb{P}(S = -1) = \frac{1}{2}$, and let $Y = SX$. By symmetry $Y \sim \mathcal{N}(0, 1)$, but $\mathbb{P}(X + Y = 0) = \mathbb{P}(S = -1) = \frac{1}{2}$, so $X + Y$ is not normal and $(X, Y)$ is not bivariate normal. Moreover $\operatorname{Cov}(X, Y) = \mathbb{E}(SX^2) = \mathbb{E}S \cdot \mathbb{E}X^2 = 0$, yet $\lvert Y \rvert = \lvert X \rvert$, so $X$ and $Y$ are not independent.

![The counterexample of Remark 15.3.1: X and Y are both standard normal and uncorrelated, but the sample of (X, Y) concentrates on the two diagonals, so (X, Y) is not bivariate normal](./plots/normal-marginals-not-joint.py)

## 15.4. Criteria for Independence

For a multivariate normal distribution, independence can be read off directly from the covariance matrix.

**Theorem 15.4.1** Let $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ be partitioned as

$$
\boldsymbol{X} = \begin{pmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{pmatrix}, \qquad \boldsymbol{\mu} = \begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix}, \qquad \Sigma = \begin{pmatrix} \Sigma_{11} & O \\ O & \Sigma_{22} \end{pmatrix},
$$
where $\boldsymbol{X}_1$, $\boldsymbol{\mu}_1$ and the square matrix $\Sigma_{11}$ have the same number of rows. Then $\boldsymbol{X}_1$ and $\boldsymbol{X}_2$ are independent, with $\boldsymbol{X}_1 \sim \mathcal{N}(\boldsymbol{\mu}_1, \Sigma_{11})$ and $\boldsymbol{X}_2 \sim \mathcal{N}(\boldsymbol{\mu}_2, \Sigma_{22})$.

**Proof** Partition $\boldsymbol{t}$ accordingly as $(\boldsymbol{t}_1^{\mathsf T}, \boldsymbol{t}_2^{\mathsf T})^{\mathsf T}$. By Theorem 15.2.2,

$$
\begin{aligned}
\varphi(\boldsymbol{t}) = \varphi(\boldsymbol{t}_1, \boldsymbol{t}_2) &= \exp\left[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}\Sigma\boldsymbol{t}\right] = \exp\left[\mathrm{i}\boldsymbol{t}_1^{\mathsf T}\boldsymbol{\mu}_1 - \frac{1}{2}\boldsymbol{t}_1^{\mathsf T}\Sigma_{11}\boldsymbol{t}_1 + \mathrm{i}\boldsymbol{t}_2^{\mathsf T}\boldsymbol{\mu}_2 - \frac{1}{2}\boldsymbol{t}_2^{\mathsf T}\Sigma_{22}\boldsymbol{t}_2\right] \\
&= \exp\left[\mathrm{i}\boldsymbol{t}_1^{\mathsf T}\boldsymbol{\mu}_1 - \frac{1}{2}\boldsymbol{t}_1^{\mathsf T}\Sigma_{11}\boldsymbol{t}_1\right] \times \exp\left[\mathrm{i}\boldsymbol{t}_2^{\mathsf T}\boldsymbol{\mu}_2 - \frac{1}{2}\boldsymbol{t}_2^{\mathsf T}\Sigma_{22}\boldsymbol{t}_2\right] = \varphi_1(\boldsymbol{t}_1)\varphi_2(\boldsymbol{t}_2),
\end{aligned}
$$
where $\varphi_1$ and $\varphi_2$ are the characteristic functions of $\mathcal{N}(\boldsymbol{\mu}_1, \Sigma_{11})$ and $\mathcal{N}(\boldsymbol{\mu}_2, \Sigma_{22})$ (by Theorem 15.3.1, these are the characteristic functions of $\boldsymbol{X}_1$ and $\boldsymbol{X}_2$). The criterion for independence via characteristic functions (Corollary 11.3.2) gives the result. $\square$

**Example 15.4.1**

$$
\begin{pmatrix} X_1 \\ X_2 \\ X_3 \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} 2 \\ 7 \\ 3 \end{pmatrix}, \begin{pmatrix} 4 & 0 & 0 \\ 0 & 9 & -3 \\ 0 & -3 & 8 \end{pmatrix}\right) \iff \begin{cases} X_1 \sim \mathcal{N}(2, 4), \\ (X_2, X_3)^{\mathsf T} \sim \mathcal{N}\left(\begin{pmatrix} 7 \\ 3 \end{pmatrix}, \begin{pmatrix} 9 & -3 \\ -3 & 8 \end{pmatrix}\right), \\ X_1 \text{ and } (X_2, X_3) \text{ are independent}. \end{cases}
$$
("$\Leftarrow$": stacking independent normal vectors, the joint characteristic function is the product, which is exactly the characteristic function on the left.)

**Theorem 15.4.2** If $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$, then $X_1, X_2, \dots, X_n$ are mutually independent if and only if

$$
\Sigma = \operatorname{diag}(\sigma_1^2, \sigma_2^2, \dots, \sigma_n^2).
$$

Sufficiency follows by applying Theorem 15.4.1 repeatedly (or by factoring the characteristic function directly into $n$ factors); necessity holds because independence implies uncorrelatedness. For example, if $\Sigma = \operatorname{diag}(4, 9, 8)$, then $X_1, X_2, X_3$ are mutually independent.

Thus for a multivariate normal random vector, "uncorrelated" and "independent" are equivalent for its components. Note that joint normality is essential: the $X$ and $Y$ of Remark 15.3.1 are each normal and uncorrelated, yet not independent.

## 15.5. Conditional Distributions

**Theorem 15.5.1 (Conditional Distribution)** Let $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ with $\det\Sigma > 0$, partitioned as

$$
\boldsymbol{X} = \begin{pmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{pmatrix}, \qquad \boldsymbol{\mu} = \begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix}, \qquad \Sigma = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix},
$$
where $\boldsymbol{X}_1$, $\boldsymbol{\mu}_1$ and the square matrix $\Sigma_{11}$ have the same number of rows. Then, given $\boldsymbol{X}_1 = \boldsymbol{x}_1$, $\boldsymbol{X}_2$ has the multivariate normal distribution

$$
\mathcal{N}\left(\boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1),\ \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\right).
$$

**Proof** Let

$$
\begin{pmatrix} \boldsymbol{Y}_1 \\ \boldsymbol{Y}_2 \end{pmatrix} = \begin{pmatrix} I & O \\ -\Sigma_{21}\Sigma_{11}^{-1} & I \end{pmatrix}\begin{pmatrix} \boldsymbol{X}_1 - \boldsymbol{\mu}_1 \\ \boldsymbol{X}_2 - \boldsymbol{\mu}_2 \end{pmatrix}.
$$
By Theorem 15.3.2 and a direct computation of $A\Sigma A^{\mathsf T}$ (using $\Sigma_{12} = \Sigma_{21}^{\mathsf T}$),

$$
\begin{pmatrix} \boldsymbol{Y}_1 \\ \boldsymbol{Y}_2 \end{pmatrix} \sim \mathcal{N}\left(\boldsymbol{0}, \begin{pmatrix} \Sigma_{11} & O \\ O & \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12} \end{pmatrix}\right)
$$
(the transformation matrix is invertible, so the covariance matrix is still positive definite). By Theorem 15.4.1, $\boldsymbol{Y}_1 = \boldsymbol{X}_1 - \boldsymbol{\mu}_1$ and $\boldsymbol{Y}_2 = \boldsymbol{X}_2 - \boldsymbol{\mu}_2 - \Sigma_{21}\Sigma_{11}^{-1}\boldsymbol{Y}_1$ are independent, and $\boldsymbol{Y}_2 \sim \mathcal{N}(\boldsymbol{0}, \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})$. Therefore

$$
\boldsymbol{X}_2 = \boldsymbol{Y}_2 + \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{X}_1 - \boldsymbol{\mu}_1),
$$
and hence

$$
\begin{aligned}
\mathbb{P}(\boldsymbol{X}_2 \le \boldsymbol{x}_2 \mid \boldsymbol{X}_1 = \boldsymbol{x}_1) &= \mathbb{P}(\boldsymbol{Y}_2 + \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1) \le \boldsymbol{x}_2 \mid \boldsymbol{Y}_1 = \boldsymbol{x}_1 - \boldsymbol{\mu}_1) \\
&= \mathbb{P}(\boldsymbol{Y}_2 + \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1) \le \boldsymbol{x}_2),
\end{aligned}
$$
where the last step uses the independence of $\boldsymbol{Y}_2$ and $\boldsymbol{Y}_1$ (inequalities between vectors are componentwise). That is, given $\boldsymbol{X}_1 = \boldsymbol{x}_1$, $\boldsymbol{X}_2$ has the same distribution as $\boldsymbol{Y}_2 + \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1)$, which proves the theorem. $\square$

The conditional expectation $\mathbb{E}(\boldsymbol{X}_2 \mid \boldsymbol{X}_1 = \boldsymbol{x}_1) = \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1)$ is a linear function of $\boldsymbol{x}_1$, and the conditional covariance matrix $\Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}$ (the Schur complement of $\Sigma_{11}$) does not depend on $\boldsymbol{x}_1$. Hence, for the multivariate normal distribution, the best predictor (the **conditional expectation**, [3.1.9](/3.1.9)) coincides with the best linear predictor ([3.1.10](/3.1.10)). For the bivariate normal $\mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$:

$$
X_2 \mid X_1 = x_1 \sim \mathcal{N}\left(\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x_1 - \mu_1),\ \sigma_2^2(1 - \rho^2)\right).
$$

## 15.6. Standard Applications

**Example 15.6.1** Let $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ with $\Sigma$ positive definite. Then $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_n$.

**Proof** By the spectral decomposition, $\Sigma^{-1} = P\Lambda P^{\mathsf T}$ with $P$ orthogonal and $\Lambda$ a positive diagonal matrix; let $\Sigma^{-1/2} = P\Lambda^{1/2}P^{\mathsf T}$ (symmetric, with $\Sigma^{-1/2}\Sigma\Sigma^{-1/2} = I_n$). By Theorem 15.3.2,

$$
\boldsymbol{Y} = \Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \mathcal{N}(\boldsymbol{0}, I_n),
$$
and by Theorem 15.4.2, $Y_1, \dots, Y_n$ are iid $\mathcal{N}(0, 1)$. Hence $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) = \boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} = Y_1^2 + \cdots + Y_n^2 \sim \chi^2_n$ (the **chi-square distribution**, Definition 7.1.1). $\square$

**Example 15.6.2** Let $\begin{pmatrix} X \\ Y \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \Sigma\right)$ with $\Sigma = \begin{pmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{pmatrix}$ positive definite. Find a necessary and sufficient condition for $X + Y$ and $X - Y$ to be independent.

**Solution** Let $\begin{pmatrix} Z_1 \\ Z_2 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} X \\ Y \end{pmatrix}$. The transformation matrix is invertible, so by Theorem 15.3.2, $(Z_1, Z_2)^{\mathsf T}$ is bivariate normal with covariance matrix

$$
\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\Sigma\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}^{\mathsf T} = \begin{pmatrix} \sigma_{11} + 2\sigma_{12} + \sigma_{22} & \sigma_{11} - \sigma_{22} \\ \sigma_{11} - \sigma_{22} & \sigma_{11} - 2\sigma_{12} + \sigma_{22} \end{pmatrix}.
$$
By Theorem 15.4.2, $Z_1$ and $Z_2$ are independent if and only if the off-diagonal entry vanishes, that is, $\sigma_{11} = \sigma_{22}$ ($X$ and $Y$ have equal variances), regardless of $\sigma_{12}$.

**Example 15.6.3 (Sample Mean and Sample Variance of a Normal Sample)** Let $X_1, \dots, X_n$ be independent, each distributed as $\mathcal{N}(\mu, \sigma^2)$, let $\bar X = \frac{1}{n}\sum_{i=1}^{n} X_i$ be the **sample mean** and $S_n^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar X)^2$ the **sample variance**. Then

1. $\bar X$ and $S_n^2$ are independent;
2. $\bar X \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$;
3. $\frac{(n-1)S_n^2}{\sigma^2} \sim \chi^2_{n-1}$.

**Proof** We may assume $\mu = 0$ and $\sigma = 1$ (otherwise consider $(X_i - \mu)/\sigma$), so that $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T} \sim \mathcal{N}(\boldsymbol{0}, I_n)$. Take an orthogonal matrix $Q$ whose first row is $\left(\frac{1}{\sqrt{n}}, \dots, \frac{1}{\sqrt{n}}\right)$ (extend this unit vector to an orthonormal basis of $\mathbb{R}^n$), and let $\boldsymbol{Y} = Q\boldsymbol{X}$. By Theorem 15.3.2, $\boldsymbol{Y} \sim \mathcal{N}(\boldsymbol{0}, QQ^{\mathsf T}) = \mathcal{N}(\boldsymbol{0}, I_n)$, and by Theorem 15.4.2, $Y_1, \dots, Y_n$ are iid $\mathcal{N}(0, 1)$. Now $Y_1 = \sqrt{n}\,\bar X$, and since orthogonal transformations preserve length,

$$
(n-1)S_n^2 = \sum_{i=1}^{n} X_i^2 - n\bar X^2 = \boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} - Y_1^2 = Y_2^2 + \cdots + Y_n^2.
$$
Hence $\bar X = Y_1/\sqrt{n} \sim \mathcal{N}(0, 1/n)$ and $(n-1)S_n^2 \sim \chi^2_{n-1}$; the former depends only on $Y_1$ and the latter only on $Y_2, \dots, Y_n$, so they are independent. $\square$

This theorem is the cornerstone of statistical inference for normal populations (the $t$-test, the $\chi^2$-test and the $F$-test; see [3.2](/3.2)); in higher dimensions there is an analogous result (the Wishart distribution).

## 15.7. Limit Theorems for Random Vectors

Reducing questions about random vectors to one dimension (the Cramér–Wold device, Theorem 14.4.5) extends the one-dimensional law of large numbers and central limit theorem to random vectors.

**Theorem 15.7.1** Let $\boldsymbol{X}_1, \boldsymbol{X}_2, \dots$ be iid $k$-dimensional random vectors such that $\mathbb{E}\boldsymbol{X}_1$ exists. Then

$$
\frac{\boldsymbol{X}_1 + \cdots + \boldsymbol{X}_n}{n} \xrightarrow{\text{a.s.}} \mathbb{E}\boldsymbol{X}_1 \quad (\text{hence also in probability}).
$$

**Proof** For each component $j$, the variables $X_{1j}, X_{2j}, \dots$ are iid with finite mean, so by the strong law of large numbers (Theorem 12.3.4), $\frac{1}{n}\sum_{i=1}^{n} X_{ij} \xrightarrow{\text{a.s.}} \mathbb{E}X_{1j}$. The intersection of $k$ events of probability $1$ still has probability $1$, which gives almost sure convergence of the vector. $\square$

For example, $\frac{1}{n}\sum_{i=1}^{n}(a\boldsymbol{X}_i + \boldsymbol{b}) \xrightarrow{\text{a.s.}} a\,\mathbb{E}\boldsymbol{X}_1 + \boldsymbol{b}$.

**Theorem 15.7.2 (Multivariate Central Limit Theorem)** Let $\boldsymbol{X}_1, \boldsymbol{X}_2, \dots$ be iid $k$-dimensional random vectors with $\mathbb{E}\boldsymbol{X}_1 = \boldsymbol{\mu}$ and positive definite covariance matrix $\operatorname{Cov}(\boldsymbol{X}_1) = \Sigma$, and let $\boldsymbol{S}_n = \boldsymbol{X}_1 + \cdots + \boldsymbol{X}_n$. Then

$$
\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}_k(\boldsymbol{0}, \Sigma), \qquad \Sigma^{-1/2} \cdot \frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}_k(\boldsymbol{0}, I_k).
$$

**Proof** Take any constant vector $\boldsymbol{a} \ne \boldsymbol{0}$. Then $\boldsymbol{a}^{\mathsf T}\boldsymbol{S}_n = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}_1 + \cdots + \boldsymbol{a}^{\mathsf T}\boldsymbol{X}_n$ is a sum of iid random variables with $\mathbb{E}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_1) = \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ and $\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_1) = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} > 0$. By the one-dimensional central limit theorem (Theorem 13.1.1),

$$
\frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{S}_n - \mathbb{E}(\boldsymbol{a}^{\mathsf T}\boldsymbol{S}_n)}{\sqrt{\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{S}_n)}} = \frac{\boldsymbol{a}^{\mathsf T}(\boldsymbol{S}_n - n\boldsymbol{\mu})/\sqrt{n}}{\sqrt{\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}}} \xrightarrow{d} \mathcal{N}(0, 1),
$$
that is, $\boldsymbol{a}^{\mathsf T}\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a})$, which is exactly the distribution of $\boldsymbol{a}^{\mathsf T}\boldsymbol{Z}$ for $\boldsymbol{Z} \sim \mathcal{N}_k(\boldsymbol{0}, \Sigma)$ (Theorem 15.3.3). For $\boldsymbol{a} = \boldsymbol{0}$ the statement is trivial. Theorem 14.4.5 gives the first conclusion; the second follows from the continuous mapping theorem (Theorem 14.4.1, with the linear map $\boldsymbol{x} \mapsto \Sigma^{-1/2}\boldsymbol{x}$) and Theorem 15.3.2. $\square$

**Example 15.7.1 (Theoretical Basis of the Chi-Square Test)** Combine Example 15.6.1 with Theorem 15.7.2. Writing $\boldsymbol{M}_n = \boldsymbol{S}_n/n$, the continuous mapping theorem (with $g(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}$) gives

$$
\left(\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}}\right)^{\mathsf T}\Sigma^{-1}\left(\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}}\right) = n(\boldsymbol{M}_n - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{M}_n - \boldsymbol{\mu}) \xrightarrow{d} \chi^2_k.
$$
This is the theoretical basis of Pearson's $\chi^2$ goodness-of-fit test and other large-sample tests ([3.2.6](/3.2.6)).

## Summary

- Three equivalent definitions of the multivariate normal distribution: the linear transformation $\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}$ (with $BB^{\mathsf T}$ of full rank); the joint density Eq. (15.1); the characteristic function $\exp[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}\Sigma\boldsymbol{t}]$. The distribution is uniquely determined by the mean vector $\boldsymbol{\mu}$ and the covariance matrix $\Sigma$.
- Closure under linear transformations: $\boldsymbol{b} + A\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{b} + A\boldsymbol{\mu}, A\Sigma A^{\mathsf T})$; marginal distributions are again normal. Characterization: $\boldsymbol{X}$ is multivariate normal if and only if every linear combination $\boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ is univariate normal (normal components alone are not enough).
- Independence: a zero off-diagonal covariance block ($\Sigma_{12} = O$) $\Leftrightarrow$ the two blocks are independent; for jointly normal components, uncorrelated and independent are equivalent.
- Conditional distributions: $\boldsymbol{X}_2 \mid \boldsymbol{X}_1 = \boldsymbol{x}_1 \sim \mathcal{N}(\boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1), \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})$; the conditional mean is linear and the conditional covariance does not depend on $\boldsymbol{x}_1$.
- Applications: $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_n$; for a normal sample, $\bar X$ and $S_n^2$ are independent and $(n-1)S_n^2/\sigma^2 \sim \chi^2_{n-1}$.
- Law of large numbers and central limit theorem for random vectors: componentwise, or via the Cramér–Wold device reduced to one dimension, $\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}_k(\boldsymbol{0}, \Sigma)$.
