---
title: Descriptive Statistics and the Multivariate Normal Distribution
description: Sample mean vector, sample covariance and correlation matrices in matrix form, their geometry and the generalized sample variance; unbiasedness and linear combinations; the multivariate normal density, its contour ellipsoids and its construction from independent normals; linear transformations, marginals, independence, conditional distributions and the chi-square property; maximum likelihood estimation and sufficiency under normality.
---

This chapter connects samples with populations in the multivariate setting. It begins with the descriptive statistics of a data matrix (the sample mean vector, the sample covariance matrix and the sample correlation matrix), written in matrix form and interpreted geometrically, together with a one-number summary of variability, the generalized sample variance. Without any distributional assumption these statistics are unbiased for the corresponding population quantities. The second half develops the multivariate normal distribution, which serves as the building block and benchmark of multivariate analysis. Its definition and basic properties were derived in probability ([3.1.15](/3.1.15)); here we restate them in the form used by the course, add the geometry of its density, and derive the maximum likelihood estimators and the sufficient statistics of a normal sample. The tools are those of [3.4.1](/3.4.1); the sampling distributions of these estimators and the inference built on them follow in [3.4.3](/3.4.3).

## 2.1. Descriptive Statistics

### 2.1.1. Sample Means, Variances, Covariances and Correlations

Let $X = (x_{jk})$ be an $n \times p$ data matrix (Definition 1.2.1), with rows $\boldsymbol{x}_j^{\mathsf T}$ for items $j = 1, \dots, n$ and columns for variables $k = 1, \dots, p$. For each variable separately we have the **sample mean** $\bar x_k$ (center, location) and the **sample variance** $s_{kk} = s_k^2$ (spread, dispersion); for each pair of variables the **sample covariance** $s_{ik}$ measures their linear association:

$$
\bar x_k = \frac{1}{n}\sum_{j=1}^{n}x_{jk}, \qquad s_{ik} = \frac{1}{n-1}\sum_{j=1}^{n}(x_{ji} - \bar x_i)(x_{jk} - \bar x_k), \qquad i, k = 1, \dots, p.
$$
The covariance depends on the units of the variables. Dividing by the standard deviations removes them.

**Definition 2.1.1 (Sample Mean Vector, Sample Covariance Matrix, Sample Correlation Matrix)** The **sample mean vector**, the **sample covariance matrix** and the **sample correlation matrix** of the data matrix $X$ are

$$
\bar{\boldsymbol{x}} = \begin{bmatrix} \bar x_1 \\ \vdots \\ \bar x_p \end{bmatrix}, \qquad S = \begin{bmatrix} s_{11} & \cdots & s_{1p} \\ \vdots & \ddots & \vdots \\ s_{p1} & \cdots & s_{pp} \end{bmatrix} = \frac{1}{n-1}\sum_{j=1}^{n}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}, \qquad R = \begin{bmatrix} 1 & r_{12} & \cdots & r_{1p} \\ r_{21} & 1 & \cdots & r_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ r_{p1} & r_{p2} & \cdots & 1 \end{bmatrix},
$$
where the sample correlation coefficient is

$$
r_{ik} = \frac{s_{ik}}{\sqrt{s_{ii}}\sqrt{s_{kk}}} = \frac{\sum_{j=1}^{n}(x_{ji} - \bar x_i)(x_{jk} - \bar x_k)}{\sqrt{\sum_{j=1}^{n}(x_{ji} - \bar x_i)^2}\sqrt{\sum_{j=1}^{n}(x_{jk} - \bar x_k)^2}}.
$$
The matrix with divisor $n$ instead of $n - 1$ is written $S_n = \frac{n-1}{n}S$.

Both divisors are in use; $S$ is unbiased (Theorem 2.2.1) and $S_n$ is the maximum likelihood estimator under normality (Theorem 2.5.1). The matrices $S$, $S_n$ and $R$ are symmetric and nonnegative definite, since $\boldsymbol{a}^{\mathsf T}S\boldsymbol{a} = \frac{1}{n-1}\sum_j[\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})]^2 \ge 0$.

**Remark 2.1.1** The sample correlation $r_{ik}$ is the sample covariance of the standardized variables, so it is free of units and scale. It satisfies $\lvert r_{ik}\rvert \le 1$ and measures only linear association: $r = 0$ means no linear association, not no association. Under the linear transformations $y_{ji} = ax_{ji} + b$, $y_{jk} = cx_{jk} + d$ the correlation becomes $\operatorname{sgn}(ac)\,r_{ik}$; it is unchanged when $a$ and $c$ have the same sign and changes sign otherwise.

**Example 2.1.1** For the data matrix $X = \begin{bmatrix} 4 & 1 \\ 5 & 2 \\ 3 & 5 \end{bmatrix}$ ($n = 3$, $p = 2$; sales and number of books of three bookstores),

$$
\bar x_1 = \frac{4 + 5 + 3}{3} = 4, \qquad \bar x_2 = \frac{1 + 2 + 5}{3} = \frac{8}{3},
$$

$$
s_{11} = \frac{0^2 + 1^2 + (-1)^2}{2} = 1, \qquad s_{22} = \frac{(-\frac{5}{3})^2 + (-\frac{2}{3})^2 + (\frac{7}{3})^2}{2} = \frac{13}{3}, \qquad s_{12} = \frac{0 \cdot (-\frac{5}{3}) + 1 \cdot (-\frac{2}{3}) + (-1)\cdot\frac{7}{3}}{2} = -\frac{3}{2},
$$
so

$$
\bar{\boldsymbol{x}} = \begin{bmatrix} 4 \\ \frac{8}{3} \end{bmatrix}, \qquad S = \begin{bmatrix} 1 & -\frac{3}{2} \\ -\frac{3}{2} & \frac{13}{3} \end{bmatrix}, \qquad r_{12} = \frac{-3/2}{\sqrt{1}\sqrt{13/3}} \approx -0.72, \qquad R = \begin{bmatrix} 1 & -0.72 \\ -0.72 & 1 \end{bmatrix}.
$$
In the scatter plot of the three points, $\bar{\boldsymbol{x}}$ is the center of gravity, $s_{11}$ and $s_{22}$ describe the horizontal and vertical spread, and the negative correlation says that the cloud runs from upper left to lower right.

### 2.1.2. Matrix Form

Write $\boldsymbol{1}_n$ for the $n \times 1$ vector of ones and $\boldsymbol{y}_k = (x_{1k}, \dots, x_{nk})^{\mathsf T}$ for the $k$-th column of $X$. Then $\bar x_k = \frac{1}{n}\boldsymbol{y}_k^{\mathsf T}\boldsymbol{1}_n$, and stacking these,

$$
\bar{\boldsymbol{x}} = \frac{1}{n}\begin{bmatrix} x_{11} & \cdots & x_{n1} \\ \vdots & \ddots & \vdots \\ x_{1p} & \cdots & x_{np} \end{bmatrix}\begin{bmatrix} 1 \\ \vdots \\ 1 \end{bmatrix} = \frac{1}{n}X^{\mathsf T}\boldsymbol{1}_n.
$$
The $n \times p$ matrix whose every row is $\bar{\boldsymbol{x}}^{\mathsf T}$ is $\boldsymbol{1}_n\bar{\boldsymbol{x}}^{\mathsf T} = \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}X$, so the matrix of deviations from the means is

$$
B = X - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}X = \left(I_n - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}\right)X.
$$

**Definition 2.1.2 (Centering Matrix)** The $n \times n$ matrix $H = I_n - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$ is called the **centering matrix**.

$H$ is symmetric and idempotent, $H^2 = I_n - \frac{2}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T} + \frac{1}{n^2}\boldsymbol{1}_n(\boldsymbol{1}_n^{\mathsf T}\boldsymbol{1}_n)\boldsymbol{1}_n^{\mathsf T} = H$; it is the **orthogonal projection matrix** onto the orthogonal complement of $\boldsymbol{1}_n$. Since $(n-1)s_{ik}$ is the inner product of the $i$-th and $k$-th columns of $B$,

$$
(n-1)S = nS_n = B^{\mathsf T}B = X^{\mathsf T}H^{\mathsf T}HX = X^{\mathsf T}HX = X^{\mathsf T}\left(I_n - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}\right)X.
$$
With $D^{1/2} = \operatorname{diag}(\sqrt{s_{11}}, \dots, \sqrt{s_{pp}})$, the correlation matrix is

$$
R = D^{-1/2}SD^{-1/2}, \qquad S = D^{1/2}RD^{1/2}.
$$
Multiplying by a diagonal matrix on the left scales the rows, on the right the columns, so $(D^{-1/2}SD^{-1/2})_{ik} = s_{ik}/(\sqrt{s_{ii}}\sqrt{s_{kk}})$.

For Example 2.1.1, $\bar{\boldsymbol{x}} = \frac{1}{3}\begin{bmatrix} 4 & 5 & 3 \\ 1 & 2 & 5 \end{bmatrix}\boldsymbol{1}_3 = (4, \frac{8}{3})^{\mathsf T}$ and $X^{\mathsf T}HX = \begin{bmatrix} 2 & -3 \\ -3 & \frac{26}{3} \end{bmatrix} = 2S$.

### 2.1.3. Geometry of the Sample

Besides $n$ points in $\mathbb{R}^p$, the data matrix can be read as $p$ vectors $\boldsymbol{y}_1, \dots, \boldsymbol{y}_p$ in $\mathbb{R}^n$ ([3.4.1](/3.4.1), Section 1.2.3). We cannot draw $n$-dimensional space for large $n$, but lengths, angles and volumes still make sense, and the descriptive statistics are exactly such quantities.

- Mean = projection on $\boldsymbol{1}_n$. The unit vector along $\boldsymbol{1}_n$ is $\boldsymbol{1}_n/\sqrt{n}$, and the projection of $\boldsymbol{y}_k$ on it is $\left(\boldsymbol{y}_k^{\mathsf T}\frac{\boldsymbol{1}_n}{\sqrt{n}}\right)\frac{\boldsymbol{1}_n}{\sqrt{n}} = \bar x_k\boldsymbol{1}_n$.
- Variance = squared length of the deviation vector. The deviation vector $\boldsymbol{d}_k = \boldsymbol{y}_k - \bar x_k\boldsymbol{1}_n$ is perpendicular to $\boldsymbol{1}_n$, and $L_{\boldsymbol{d}_k}^2 = \boldsymbol{d}_k^{\mathsf T}\boldsymbol{d}_k = \sum_j(x_{jk} - \bar x_k)^2 = (n-1)s_{kk}$. The closer $\boldsymbol{y}_k$ is to the line of $\boldsymbol{1}_n$, the smaller the variance.
- Correlation = cosine of the angle. $\boldsymbol{d}_i^{\mathsf T}\boldsymbol{d}_k = (n-1)s_{ik} = L_{\boldsymbol{d}_i}L_{\boldsymbol{d}_k}\cos\theta_{ik}$, hence $r_{ik} = \cos\theta_{ik}$. The smaller the angle between two deviation vectors, the larger the correlation.

**Example 2.1.2** For $X = \begin{bmatrix} 4 & 1 \\ -1 & 3 \\ 3 & 5 \end{bmatrix}$, $\bar{\boldsymbol{x}} = (2, 3)^{\mathsf T}$, the projections of the columns on $\boldsymbol{1}_3$ are $2\boldsymbol{1}_3$ and $3\boldsymbol{1}_3$, and the deviation vectors are $\boldsymbol{d}_1 = (2, -3, 1)^{\mathsf T}$, $\boldsymbol{d}_2 = (-2, 0, 2)^{\mathsf T}$. Hence $s_{11} = 14/2 = 7$, $s_{22} = 8/2 = 4$, $s_{12} = -2/2 = -1$ and $r_{12} = \cos\theta_{12} = -2/\sqrt{14 \cdot 8} \approx -0.19$: the two deviation vectors are almost perpendicular.

### 2.1.4. Generalized Sample Variance

How can the information in the $p \times p$ matrix $S$ be summarized by a single number? Two common choices are the total sample variance $\operatorname{tr}S = s_{11} + \cdots + s_{pp}$ and the following.

**Definition 2.1.3 (Generalized Sample Variance)** The determinant $\det S$ of the sample covariance matrix is called the **generalized sample variance**.

Both pictures of the sample explain what it measures.

In the picture of $p$ vectors in $\mathbb{R}^n$, for $p = 2$, the deviation vectors $\boldsymbol{d}_1, \boldsymbol{d}_2$ span a parallelogram of area $L_{\boldsymbol{d}_1}L_{\boldsymbol{d}_2}\sin\theta = L_{\boldsymbol{d}_1}L_{\boldsymbol{d}_2}\sqrt{1 - \cos^2\theta}$. With $L_{\boldsymbol{d}_k} = \sqrt{(n-1)s_{kk}}$ and $\cos\theta = r_{12}$,

$$
\text{area} = (n-1)\sqrt{s_{11}s_{22}(1 - r_{12}^2)}, \qquad \det S = \det\begin{bmatrix} s_{11} & \sqrt{s_{11}s_{22}}\,r_{12} \\ \sqrt{s_{11}s_{22}}\,r_{12} & s_{22} \end{bmatrix} = s_{11}s_{22}(1 - r_{12}^2),
$$
so $\det S = (\text{area})^2/(n-1)^2$. In general $\det S = (n-1)^{-p}(\text{volume})^2$, where the volume is that of the parallelotope spanned by $\boldsymbol{d}_1, \dots, \boldsymbol{d}_p$ (it equals $\sqrt{\det(B^{\mathsf T}B)}$). The generalized variance is large when the deviation vectors are long and far from collinear.

In the picture of $n$ points in $\mathbb{R}^p$, if $\det S > 0$, the solid ellipsoid $\{\boldsymbol{x}\colon (\boldsymbol{x} - \bar{\boldsymbol{x}})^{\mathsf T}S^{-1}(\boldsymbol{x} - \bar{\boldsymbol{x}}) \le c^2\}$ (all points within Mahalanobis distance $c$ of $\bar{\boldsymbol{x}}$) has volume

$$
\operatorname{vol}\{\boldsymbol{x}\colon (\boldsymbol{x} - \bar{\boldsymbol{x}})^{\mathsf T}S^{-1}(\boldsymbol{x} - \bar{\boldsymbol{x}}) \le c^2\} = k_p(\det S)^{1/2}c^p, \qquad k_p = \frac{2\pi^{p/2}}{p\,\Gamma(p/2)},
$$
because its semi-axes are $c\sqrt{\lambda_i}$, where $\lambda_1, \dots, \lambda_p$ are the eigenvalues of $S$, and $\det S = \lambda_1\lambda_2\cdots\lambda_p$. Thus $\det S$ measures the volume occupied by the bulk of the data cloud.

**Theorem 2.1.1** The following are equivalent for a sample $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$:

1. $\det S = 0$;
2. $S\boldsymbol{a} = \boldsymbol{0}$ for some $\boldsymbol{a} \ne \boldsymbol{0}$ (that is, $\boldsymbol{a}$ is an eigenvector of $S$ with eigenvalue $0$);
3. $\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}}) = 0$ for all $j$: the linear combination of the mean-corrected data with coefficients $\boldsymbol{a}$ vanishes, i.e. the deviation vectors $\boldsymbol{d}_1, \dots, \boldsymbol{d}_p$ are linearly dependent;
4. $\boldsymbol{a}^{\mathsf T}\boldsymbol{x}_j = c$ for all $j$, with $c = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}$: the linear combination of the original data is constant.

In particular $\det S = 0$ whenever $n \le p$.

**Proof** (1)⇔(2) since $\det S = \lambda_1\cdots\lambda_p$. (2)⇒(3): $0 = \boldsymbol{a}^{\mathsf T}S\boldsymbol{a} = \frac{1}{n-1}\sum_j[\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})]^2$. (3)⇒(2): $(n-1)S\boldsymbol{a} = \sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}\boldsymbol{a} = \boldsymbol{0}$. (3)⇔(4) is immediate, and (3) says $B\boldsymbol{a} = a_1\boldsymbol{d}_1 + \cdots + a_p\boldsymbol{d}_p = \boldsymbol{0}$. Finally $\operatorname{rank}(S) = \operatorname{rank}(B) = \operatorname{rank}(HX) \le \operatorname{rank}(H) = n - 1$, so $S$ is singular when $n - 1 < p$. $\square$

A zero generalized variance indicates that some variables are redundant (exact linear functions of the others) and should be removed before further computations, for example before inverting $S$.

**Remark 2.1.2** A single number cannot capture a matrix. The three covariance matrices

$$
S = \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix}\ (r = 0.8), \qquad S = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}\ (r = 0), \qquad S = \begin{bmatrix} 5 & -4 \\ -4 & 5 \end{bmatrix}\ (r = -0.8)
$$
all have $\det S = 9$, yet they describe clouds of very different shape and orientation. The generalized variance loses the information on the direction of the correlation and on the variability in each direction; the eigenvalues and eigenvectors of $S$ retain it, which leads to principal component analysis ([3.4.5](/3.4.5)).

![Three simulated samples with mean (2, 1) whose covariance matrices have correlation 0.8, 0 and -0.8 but the same generalized variance det S = 9. The ellipses are the 95% contours (x - mean)^T S^(-1) (x - mean) = 5.99 of the true covariance; they have the same area, and the arrows are the semi-axes along the eigenvectors.](./plots/generalized-variance.py)

## 2.2. Sample Statistics and Population Parameters

Now let the rows of the data matrix be a **random sample** $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ (Definition 1.2.2), so that $\bar{\boldsymbol{X}}$, $S$ and $S_n$ are random. How are these statistics related to the population mean vector $\boldsymbol{\mu}$ and covariance matrix $\Sigma$? The following results need no assumption on the form of $f(\boldsymbol{x})$ beyond finite second moments.

**Theorem 2.2.1** Let $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ be a random sample from a joint distribution with mean vector $\boldsymbol{\mu}$ and covariance matrix $\Sigma$. Then

$$
\mathbb{E}\bar{\boldsymbol{X}} = \boldsymbol{\mu}, \qquad \operatorname{Cov}(\bar{\boldsymbol{X}}) = \frac{1}{n}\Sigma, \qquad \mathbb{E}S_n = \frac{n-1}{n}\Sigma, \qquad \mathbb{E}S = \Sigma.
$$
Hence $\bar{\boldsymbol{X}}$ and $S$ are **unbiased estimators** of $\boldsymbol{\mu}$ and $\Sigma$, while $S_n$ is biased.

**Proof** Linearity gives $\mathbb{E}\bar{\boldsymbol{X}} = \frac{1}{n}\sum_j\mathbb{E}\boldsymbol{X}_j = \boldsymbol{\mu}$. By independence the cross covariances vanish, so

$$
\operatorname{Cov}(\bar{\boldsymbol{X}}) = \mathbb{E}\left[\frac{1}{n}\sum_j(\boldsymbol{X}_j - \boldsymbol{\mu})\cdot\frac{1}{n}\sum_l(\boldsymbol{X}_l - \boldsymbol{\mu})^{\mathsf T}\right] = \frac{1}{n^2}\sum_{j=1}^{n}\mathbb{E}[(\boldsymbol{X}_j - \boldsymbol{\mu})(\boldsymbol{X}_j - \boldsymbol{\mu})^{\mathsf T}] = \frac{1}{n}\Sigma.
$$
For $S_n$, expand $\sum_j(\boldsymbol{X}_j - \bar{\boldsymbol{X}})(\boldsymbol{X}_j - \bar{\boldsymbol{X}})^{\mathsf T} = \sum_j\boldsymbol{X}_j\boldsymbol{X}_j^{\mathsf T} - n\bar{\boldsymbol{X}}\bar{\boldsymbol{X}}^{\mathsf T}$ and use $\mathbb{E}[\boldsymbol{X}_j\boldsymbol{X}_j^{\mathsf T}] = \Sigma + \boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf T}$ and $\mathbb{E}[\bar{\boldsymbol{X}}\bar{\boldsymbol{X}}^{\mathsf T}] = \frac{1}{n}\Sigma + \boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf T}$:

$$
\mathbb{E}\left[\sum_j(\boldsymbol{X}_j - \bar{\boldsymbol{X}})(\boldsymbol{X}_j - \bar{\boldsymbol{X}})^{\mathsf T}\right] = n(\Sigma + \boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf T}) - n\left(\frac{1}{n}\Sigma + \boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf T}\right) = (n-1)\Sigma.
$$
Dividing by $n$ and by $n - 1$ gives the last two statements. $\square$

In Example 2.1.1 the population is $\boldsymbol{X} = (X_1, X_2)^{\mathsf T}$ with $\boldsymbol{\mu} = (\mu_1, \mu_2)^{\mathsf T}$ and $\Sigma = \begin{bmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{bmatrix}$; the sample gives the estimates $\bar{\boldsymbol{x}} = (4, \frac{8}{3})^{\mathsf T}$ of $\boldsymbol{\mu}$ and $S$ of $\Sigma$. Each entry of the sample matrices estimates the corresponding entry of the population matrices.

Linear combinations of the variables behave in the same way. For constant vectors $\boldsymbol{b}, \boldsymbol{c}$ and a constant $q \times p$ matrix $A$, the population results are those of [3.1.15](/3.1.15):

$$
\mathbb{E}(\boldsymbol{c}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{c}^{\mathsf T}\boldsymbol{\mu}, \quad \operatorname{Var}(\boldsymbol{c}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{c}^{\mathsf T}\Sigma\boldsymbol{c}, \quad \operatorname{Cov}(\boldsymbol{b}^{\mathsf T}\boldsymbol{X}, \boldsymbol{c}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{b}^{\mathsf T}\Sigma\boldsymbol{c}, \quad \mathbb{E}(A\boldsymbol{X}) = A\boldsymbol{\mu}, \quad \operatorname{Cov}(A\boldsymbol{X}) = A\Sigma A^{\mathsf T}.
$$
For instance $\operatorname{Cov}(\boldsymbol{b}^{\mathsf T}\boldsymbol{X}, \boldsymbol{c}^{\mathsf T}\boldsymbol{X}) = \mathbb{E}[\boldsymbol{b}^{\mathsf T}(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\boldsymbol{c}] = \boldsymbol{b}^{\mathsf T}\Sigma\boldsymbol{c}$, and more generally $\operatorname{Cov}(B\boldsymbol{X}, C\boldsymbol{X}) = B\Sigma C^{\mathsf T}$; these are the matrix versions of $\mathbb{E}(aX) = a\,\mathbb{E}X$ and $\operatorname{Var}(aX) = a^2\operatorname{Var}(X)$. The sample versions have exactly the same form.

**Theorem 2.2.2** Let $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ have sample mean vector $\bar{\boldsymbol{x}}$ and sample covariance matrix $S$. The values $\boldsymbol{b}^{\mathsf T}\boldsymbol{x}_j$ and $\boldsymbol{c}^{\mathsf T}\boldsymbol{x}_j$ ($j = 1, \dots, n$) of two linear combinations have

$$
\text{sample means } \boldsymbol{b}^{\mathsf T}\bar{\boldsymbol{x}},\ \boldsymbol{c}^{\mathsf T}\bar{\boldsymbol{x}}, \qquad \text{sample variances } \boldsymbol{b}^{\mathsf T}S\boldsymbol{b},\ \boldsymbol{c}^{\mathsf T}S\boldsymbol{c}, \qquad \text{sample covariance } \boldsymbol{b}^{\mathsf T}S\boldsymbol{c}.
$$
More generally, the $q$ linear combinations $A\boldsymbol{x}_j$ have sample mean vector $A\bar{\boldsymbol{x}}$ and sample covariance matrix $ASA^{\mathsf T}$.

**Proof** The mean of $A\boldsymbol{x}_j$ is $\frac{1}{n}\sum_jA\boldsymbol{x}_j = A\bar{\boldsymbol{x}}$, and its sample covariance matrix is $\frac{1}{n-1}\sum_jA(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}A^{\mathsf T} = ASA^{\mathsf T}$. The other statements are the special cases $A = \boldsymbol{c}^{\mathsf T}$ and $A = \begin{bmatrix} \boldsymbol{b}^{\mathsf T} \\ \boldsymbol{c}^{\mathsf T} \end{bmatrix}$. $\square$

**Example 2.2.1** In Example 2.1.1, the linear combination $c_1x_1 + c_2x_2$ takes the values $\boldsymbol{c}^{\mathsf T}(4, 1)^{\mathsf T}$, $\boldsymbol{c}^{\mathsf T}(5, 2)^{\mathsf T}$, $\boldsymbol{c}^{\mathsf T}(3, 5)^{\mathsf T}$, with sample mean $4c_1 + \frac{8}{3}c_2$ and sample variance

$$
\boldsymbol{c}^{\mathsf T}S\boldsymbol{c} = \begin{bmatrix} c_1 & c_2 \end{bmatrix}\begin{bmatrix} 1 & -\frac{3}{2} \\ -\frac{3}{2} & \frac{13}{3} \end{bmatrix}\begin{bmatrix} c_1 \\ c_2 \end{bmatrix} = c_1^2 - 3c_1c_2 + \frac{13}{3}c_2^2.
$$
For $\boldsymbol{c} = (1, 1)^{\mathsf T}$ the values are $5, 7, 8$, with mean $\frac{20}{3}$ and variance $\frac{7}{3}$, as the formula gives.

## 2.3. The Multivariate Normal Distribution

### 2.3.1. Why the Multivariate Normal Distribution

The multivariate normal distribution plays four roles. It is a building block for constructing more complex distributions (Gaussian mixture models) and the benchmark on which new methods are tested. It provides a coordinate system: its mean vector and covariance matrix define "normal" linear dependence, against which anomalies, nonlinearity and other departures are measured. It is the mathematical core of many modern methods: latent spaces of generative models, conjugate Bayesian analysis, Gaussian processes. And it trains statistical intuition: thinking in vectors, distinguishing joint from marginal distributions, and updating beliefs by conditioning.

### 2.3.2. Density and Contours

In one dimension $X \sim \mathcal{N}(\mu, \sigma^2)$ has density $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left\{-\frac{(x - \mu)^2}{2\sigma^2}\right\}$; the exponent is minus one half of the squared standardized distance from $\mu$. Replacing it by the squared **Mahalanobis distance** gives the multivariate density.

**Definition 2.3.1 (Multivariate Normal Distribution)** A $p$-dimensional random vector $\boldsymbol{X}$ has the multivariate normal distribution $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$, where $\boldsymbol{\mu} \in \mathbb{R}^p$ and $\Sigma$ is a $p \times p$ positive definite matrix, if its density is

$$
f(\boldsymbol{x}) = \frac{1}{(2\pi)^{p/2}(\det\Sigma)^{1/2}}\exp\left\{-\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\right\}, \qquad \boldsymbol{x} \in \mathbb{R}^p. \tag{2.1}
$$

In [3.1.15](/3.1.15) the distribution was defined as $\boldsymbol{\mu} + B\boldsymbol{\varepsilon}$ with independent standard normal components of $\boldsymbol{\varepsilon}$ ([Definition 15.2.1](/3.1.15#def-15.2.1)), and Eq. (2.1) was derived as its density; the two definitions are equivalent, and so is the characterization by linear combinations (Theorem 2.4.1 below). The distribution is continuous and completely characterized by its first two moments: $\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X}$ and $\Sigma = \operatorname{Cov}(\boldsymbol{X})$.

**Example 2.3.1 (Bivariate Normal Density)** For $p = 2$ there are five free parameters, two for location and three for scale:

$$
\boldsymbol{\mu} = \begin{bmatrix} \mu_1 \\ \mu_2 \end{bmatrix} = \begin{bmatrix} \mathbb{E}X_1 \\ \mathbb{E}X_2 \end{bmatrix}, \qquad \Sigma = \begin{bmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{bmatrix} = \begin{bmatrix} \sigma_{11} & \rho_{12}\sqrt{\sigma_{11}\sigma_{22}} \\ \rho_{12}\sqrt{\sigma_{11}\sigma_{22}} & \sigma_{22} \end{bmatrix},
$$
and Eq. (2.1) reduces to the **bivariate normal distribution** of [3.1.6](/3.1.6). With $\sigma_{11} = \sigma_{22}$ and $\rho_{12} = 0$ the density surface is a rotationally symmetric bell; with $\rho_{12} = 0.75$ it is a ridge along the diagonal. As $\rho_{12}$ increases from $0$ towards $1$ the contours change from circles to ever thinner ellipses along the line $x_2 = x_1$, and for negative $\rho_{12}$ along $x_2 = -x_1$.

The density depends on $\boldsymbol{x}$ only through the squared distance $(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})$, so its contours are the sets of constant Mahalanobis distance from $\boldsymbol{\mu}$.

**Theorem 2.3.1 (Contours of Constant Density)** Let $\Sigma$ have eigenvalues $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_p > 0$ with normalized eigenvectors $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$, $\Sigma\boldsymbol{e}_i = \lambda_i\boldsymbol{e}_i$. The contours of constant density of $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$,

$$
\{\boldsymbol{x}\colon (\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) = c^2\},
$$
are ellipsoids centered at $\boldsymbol{\mu}$ with axes $\pm c\sqrt{\lambda_i}\,\boldsymbol{e}_i$, $i = 1, \dots, p$.

**Proof** $\Sigma^{-1} = \sum_i\lambda_i^{-1}\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$ (Property 1.6.1), so with $y_i = \boldsymbol{e}_i^{\mathsf T}(\boldsymbol{x} - \boldsymbol{\mu})$, the coordinates of $\boldsymbol{x} - \boldsymbol{\mu}$ along the eigenvectors, the equation reads $\sum_i y_i^2/\lambda_i = c^2$: an ellipsoid with semi-axis $c\sqrt{\lambda_i}$ along $\boldsymbol{e}_i$. $\square$

The longest axis points along the eigenvector of the largest eigenvalue of $\Sigma$, the direction of greatest variance. Theorem 2.4.7 below gives the probability content of these ellipsoids.

![Left: a sample of 400 points from a bivariate normal distribution with the contours of constant density containing 50%, 90% and 99% of the probability; the arrows are the semi-axes c sqrt(lambda_i) e_i of the 90% ellipse. Right: the fraction of the sample inside the ellipse of level 1 - alpha against 1 - alpha, close to the diagonal as Theorem 2.4.7 predicts.](./plots/mvn-contours.py)

### 2.3.3. Construction from Independent Standard Normals

**Theorem 2.3.2** Let $Z_1, \dots, Z_p$ be iid $\mathcal{N}(0, 1)$, $\boldsymbol{Z} = (Z_1, \dots, Z_p)^{\mathsf T}$, let $\Sigma$ be a symmetric positive definite matrix and $\boldsymbol{\mu} \in \mathbb{R}^p$. Then

$$
\boldsymbol{X} = \boldsymbol{\mu} + \Sigma^{1/2}\boldsymbol{Z} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma).
$$

**Proof** By independence $\boldsymbol{Z}$ has density $f_{\boldsymbol{Z}}(\boldsymbol{z}) = \prod_jf_j(z_j) = (2\pi)^{-p/2}\exp(-\boldsymbol{z}^{\mathsf T}\boldsymbol{z}/2)$. The transformation $\boldsymbol{x} = \boldsymbol{\mu} + \Sigma^{1/2}\boldsymbol{z}$ is invertible with $\boldsymbol{z} = \Sigma^{-1/2}(\boldsymbol{x} - \boldsymbol{\mu})$; since $\partial\boldsymbol{z}/\partial\boldsymbol{x} = \Sigma^{-1/2}$, the absolute value of the **Jacobian determinant** is $\det\Sigma^{-1/2} = (\det\Sigma)^{-1/2}$. Hence

$$
f(\boldsymbol{x}) = (\det\Sigma)^{-1/2}(2\pi)^{-p/2}\exp\left\{-\frac{1}{2}[\Sigma^{-1/2}(\boldsymbol{x} - \boldsymbol{\mu})]^{\mathsf T}[\Sigma^{-1/2}(\boldsymbol{x} - \boldsymbol{\mu})]\right\} = \frac{1}{(2\pi)^{p/2}(\det\Sigma)^{1/2}}\exp\left\{-\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\right\},
$$
using $\Sigma^{-1/2}\Sigma^{-1/2} = \Sigma^{-1}$. $\square$

The one-dimensional case is $X = \mu + \sigma Z$. A second proof uses the **characteristic function**, as in [3.1.15](/3.1.15). In a fundamental sense the multivariate normal distribution is the distribution of affine transformations of independent Gaussians, and Theorem 2.3.2 (or its variant with the **Cholesky decomposition** $\Sigma = LL^{\mathsf T}$ in place of $\Sigma^{1/2}$) is how multivariate normal samples are simulated. Conversely, $\boldsymbol{Z} = \Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu})$ standardizes a normal vector, the probabilistic counterpart of the whitening in [3.4.1](/3.4.1), Section 1.6.4: it rotates onto the axes of the contour ellipsoids and rescales them to unit length.

## 2.4. Properties of the Multivariate Normal Distribution

The properties below were proved in [3.1.15](/3.1.15), mostly via characteristic functions; we restate them in the form used throughout the course. Two of them are the key tools for everything that follows: closure under linear transformations (Theorem 2.4.2) and the equivalence of independence and zero covariance (Theorem 2.4.4). Theorem 2.4.1 serves as an equivalent definition and as the quickest way to recognize multivariate normality; the marginal and conditional distributions (Theorems 2.4.3 and 2.4.5) are used more in other courses and serve here mainly as exercises in applying the two key tools; Theorems 2.4.7 and 2.4.8 are the basis of the inference in [3.4.3](/3.4.3).

### 2.4.1. Linear Combinations and Linear Transformations

**Theorem 2.4.1** A random vector $\boldsymbol{X}$ is distributed as $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ if and only if $\boldsymbol{a}^{\mathsf T}\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a})$ for every $\boldsymbol{a} \in \mathbb{R}^p$.

This is [Theorem 15.3.3](/3.1.15#thm-15.3.3): the characteristic function of $Y = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ at $t$ is that of $\boldsymbol{X}$ at $t\boldsymbol{a}$, so the one-dimensional characteristic functions for all $\boldsymbol{a}$ determine the multivariate one. For example,

$$
\begin{bmatrix} X_1 \\ X_2 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 1 \\ -5 \end{bmatrix}, \begin{bmatrix} 4 & -2 \\ -2 & 9 \end{bmatrix}\right) \iff a_1X_1 + a_2X_2 \sim \mathcal{N}\left(a_1 - 5a_2,\ 4a_1^2 - 4a_1a_2 + 9a_2^2\right) \text{ for all } a_1, a_2.
$$

**Theorem 2.4.2 (Linear Transformations)** If $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ and $A$ is a $q \times p$ constant matrix ($q \le p$) such that $A\Sigma A^{\mathsf T}$ is invertible, then

$$
A\boldsymbol{X} = \begin{bmatrix} a_{11}X_1 + \cdots + a_{1p}X_p \\ \vdots \\ a_{q1}X_1 + \cdots + a_{qp}X_p \end{bmatrix} \sim \mathcal{N}_q(A\boldsymbol{\mu}, A\Sigma A^{\mathsf T}).
$$
Also $\boldsymbol{X} + \boldsymbol{d} \sim \mathcal{N}_p(\boldsymbol{\mu} + \boldsymbol{d}, \Sigma)$ for every constant vector $\boldsymbol{d}$.

**Proof** For $\boldsymbol{b} \in \mathbb{R}^q$, $\boldsymbol{b}^{\mathsf T}(A\boldsymbol{X}) = (A^{\mathsf T}\boldsymbol{b})^{\mathsf T}\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{b}^{\mathsf T}A\boldsymbol{\mu}, \boldsymbol{b}^{\mathsf T}A\Sigma A^{\mathsf T}\boldsymbol{b})$ by Theorem 2.4.1, and Theorem 2.4.1 again gives the claim. The second statement is the same argument with $\boldsymbol{b}^{\mathsf T}(\boldsymbol{X} + \boldsymbol{d})$. $\square$

**Example 2.4.1** With $\boldsymbol{X}$ as above and $\boldsymbol{Y} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\boldsymbol{X}$,

$$
\boldsymbol{Y} \sim \mathcal{N}\left(\begin{bmatrix} 1 \\ 0 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ -5 \end{bmatrix},\ \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 4 & -2 \\ -2 & 9 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}^{\mathsf T}\right) = \mathcal{N}\left(\begin{bmatrix} 2 \\ -4 \end{bmatrix}, \begin{bmatrix} 4 & 2 \\ 2 & 9 \end{bmatrix}\right).
$$

### 2.4.2. Marginal Distributions and Independence

Partition $\boldsymbol{X}$, its mean vector and its covariance matrix conformably as

$$
\boldsymbol{X} = \begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix}, \qquad \boldsymbol{\mu} = \begin{bmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{bmatrix}, \qquad \Sigma = \begin{bmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{bmatrix}, \tag{2.2}
$$
with $\boldsymbol{X}_1$ and $\boldsymbol{\mu}_1$ of size $q \times 1$, $\boldsymbol{X}_2$ and $\boldsymbol{\mu}_2$ of size $(p - q) \times 1$, and $\Sigma_{11}$ of size $q \times q$. Here $\Sigma_{11} = \operatorname{Cov}(\boldsymbol{X}_1)$, $\Sigma_{22} = \operatorname{Cov}(\boldsymbol{X}_2)$ and $\Sigma_{12} = \operatorname{Cov}(\boldsymbol{X}_1, \boldsymbol{X}_2) = \Sigma_{21}^{\mathsf T}$, the $q \times (p - q)$ matrix of covariances between the components of $\boldsymbol{X}_1$ and those of $\boldsymbol{X}_2$. (If the block notation is unfamiliar, it helps to read every argument below first with $\boldsymbol{X}_1$ and $\boldsymbol{X}_2$ scalars, where $\Sigma = \begin{bmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{bmatrix}$.)

**Theorem 2.4.3 (Marginal Distributions)** All subsets of the components of $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ are normally distributed: with the partition (2.2), $\boldsymbol{X}_1 \sim \mathcal{N}_q(\boldsymbol{\mu}_1, \Sigma_{11})$.

This is Theorem 2.4.2 with $A = [I_q, O]$. For example,

$$
\begin{bmatrix} X_1 \\ X_2 \\ X_3 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 2 \\ 7 \\ 3 \end{bmatrix}, \begin{bmatrix} 4 & -1 & 2 \\ -1 & 9 & -3 \\ 2 & -3 & 8 \end{bmatrix}\right) \implies X_1 \sim \mathcal{N}(2, 4), \quad \begin{bmatrix} X_2 \\ X_3 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 7 \\ 3 \end{bmatrix}, \begin{bmatrix} 9 & -3 \\ -3 & 8 \end{bmatrix}\right).
$$
The converse fails: normal marginals do not imply a jointly normal vector.

**Theorem 2.4.4 (Independence and Zero Covariance)**

1. If $\boldsymbol{X}_1$ ($q_1 \times 1$) and $\boldsymbol{X}_2$ ($q_2 \times 1$) are independent, then $\operatorname{Cov}(\boldsymbol{X}_1, \boldsymbol{X}_2) = O$, a $q_1 \times q_2$ matrix of zeros.
2. If $\begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix} \sim \mathcal{N}_{q_1+q_2}\left(\begin{bmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{bmatrix}, \begin{bmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{bmatrix}\right)$, then $\boldsymbol{X}_1$ and $\boldsymbol{X}_2$ are independent if and only if $\Sigma_{12} = O$.
3. If $\boldsymbol{X}_1 \sim \mathcal{N}_{q_1}(\boldsymbol{\mu}_1, \Sigma_{11})$ and $\boldsymbol{X}_2 \sim \mathcal{N}_{q_2}(\boldsymbol{\mu}_2, \Sigma_{22})$ are independent, then

$$
\begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix} \sim \mathcal{N}_{q_1+q_2}\left(\begin{bmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{bmatrix}, \begin{bmatrix} \Sigma_{11} & O \\ O & \Sigma_{22} \end{bmatrix}\right).
$$

Part 1 holds for any distribution; part 2 is [Theorem 15.4.1](/3.1.15#thm-15.4.1) (the characteristic function factorizes when $\Sigma_{12} = O$); part 3 follows because the joint characteristic function of independent vectors is the product of the two normal characteristic functions. For example,

$$
\begin{bmatrix} X_1 \\ X_2 \\ X_3 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 2 \\ 7 \\ 3 \end{bmatrix}, \begin{bmatrix} 4 & 0 & 0 \\ 0 & 9 & -3 \\ 0 & -3 & 8 \end{bmatrix}\right) \iff X_1 \sim \mathcal{N}(2, 4),\ \begin{bmatrix} X_2 \\ X_3 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 7 \\ 3 \end{bmatrix}, \begin{bmatrix} 9 & -3 \\ -3 & 8 \end{bmatrix}\right),\ X_1 \text{ independent of } (X_2, X_3).
$$

**Remark 2.4.1** Joint normality is essential in part 2. If $\boldsymbol{X}_1$ and $\boldsymbol{X}_2$ are independent and each is normal, the stacked vector is normal (part 3). If they are dependent, the stacked vector may or may not be normal. For a counterexample let $X_1 \sim \mathcal{N}(0, 1)$, let $S$ be independent of $X_1$ with $\mathbb{P}(S = 1) = \mathbb{P}(S = -1) = \frac{1}{2}$, and $X_2 = SX_1$. Then $X_2 \sim \mathcal{N}(0, 1)$ and $\operatorname{Cov}(X_1, X_2) = 0$, but $X_1$ and $X_2$ are not independent ([Remark 15.3.1](/3.1.15#rem-15.3.1)). Theorem 2.4.1 shows at once that $(X_1, X_2)^{\mathsf T}$ is not bivariate normal: the linear combination $X_1 + X_2$ equals $0$ with probability $\frac{1}{2}$ (and $2X_1$ otherwise), which is not a normal distribution. So "zero covariance is equivalent to independence" holds only under joint normality.

### 2.4.3. Conditional Distributions

**Theorem 2.4.5 (Conditional Distributions)** Let $\boldsymbol{X} = \begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix} \sim \mathcal{N}_{q_1+q_2}(\boldsymbol{\mu}, \Sigma)$ be partitioned as in (2.2), with $\det\Sigma_{22} > 0$. Then the conditional distribution of $\boldsymbol{X}_1$ given $\boldsymbol{X}_2 = \boldsymbol{x}_2$ is normal with

$$
\text{mean} = \boldsymbol{\mu}_1 + \Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{x}_2 - \boldsymbol{\mu}_2), \qquad \text{covariance} = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}.
$$

**Proof** When $\boldsymbol{X}_1$ and $\boldsymbol{X}_2$ are dependent, we try to remove from $\boldsymbol{X}_1$ the part related to $\boldsymbol{X}_2$, so that $\boldsymbol{X}_1 - g(\boldsymbol{X}_2)$ is independent of $\boldsymbol{X}_2$. For a normal vector the dependence is linear, so it suffices to try $g(\boldsymbol{X}_2) = A\boldsymbol{X}_2$. Let $\boldsymbol{Z} = \boldsymbol{X}_1 - \boldsymbol{\mu}_1 - A(\boldsymbol{X}_2 - \boldsymbol{\mu}_2)$. The vector

$$
\begin{bmatrix} \boldsymbol{Z} \\ \boldsymbol{X}_2 - \boldsymbol{\mu}_2 \end{bmatrix} = \begin{bmatrix} I & -A \\ O & I \end{bmatrix}\begin{bmatrix} \boldsymbol{X}_1 - \boldsymbol{\mu}_1 \\ \boldsymbol{X}_2 - \boldsymbol{\mu}_2 \end{bmatrix}
$$
is a linear transformation of a normal vector, hence normal (Theorem 2.4.2). By Theorem 2.4.4, $\boldsymbol{Z}$ is independent of $\boldsymbol{X}_2$ if and only if

$$
\operatorname{Cov}(\boldsymbol{Z}, \boldsymbol{X}_2) = \Sigma_{12} - A\Sigma_{22} = O, \qquad \text{i.e. } A = \Sigma_{12}\Sigma_{22}^{-1}.
$$
With this $A$, $\boldsymbol{Z}$ has mean $\boldsymbol{0}$ and covariance matrix

$$
\operatorname{Cov}(\boldsymbol{Z}) = \Sigma_{11} - A\Sigma_{21} - \Sigma_{12}A^{\mathsf T} + A\Sigma_{22}A^{\mathsf T} = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}.
$$
Given $\boldsymbol{X}_2 = \boldsymbol{x}_2$, we have $\boldsymbol{X}_1 = \boldsymbol{\mu}_1 + \Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{x}_2 - \boldsymbol{\mu}_2) + \boldsymbol{Z}$ with $\boldsymbol{Z}$ independent of $\boldsymbol{X}_2$, so the conditional distribution is that of $\boldsymbol{Z}$ shifted by the stated mean. $\square$

**Example 2.4.2** For the three-dimensional example of Theorem 2.4.3, find the distribution of $X_1$ given $X_2 = 1$, $X_3 = 0$. Here $\Sigma_{12} = (-1, 2)$, $\Sigma_{22} = \begin{bmatrix} 9 & -3 \\ -3 & 8 \end{bmatrix}$, $\Sigma_{22}^{-1} = \frac{1}{63}\begin{bmatrix} 8 & 3 \\ 3 & 9 \end{bmatrix}$, so $\Sigma_{12}\Sigma_{22}^{-1} = \frac{1}{63}(-2, 15)$ and

$$
\text{mean} = 2 + \frac{1}{63}(-2, 15)\begin{bmatrix} 1 - 7 \\ 0 - 3 \end{bmatrix} = 2 - \frac{33}{63} = \frac{31}{21}, \qquad \text{variance} = 4 - \frac{1}{63}(-2, 15)\begin{bmatrix} -1 \\ 2 \end{bmatrix} = 4 - \frac{32}{63} = \frac{220}{63}.
$$
Thus $X_1 \mid X_2 = 1, X_3 = 0 \sim \mathcal{N}\left(\frac{31}{21}, \frac{220}{63}\right)$; the conditional variance is smaller than the marginal variance $4$.

**Remark 2.4.2** The conditional covariance $\Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$, the **Schur complement** of $\Sigma_{22}$, does not depend on the value $\boldsymbol{x}_2$, and the conditional mean is linear in $\boldsymbol{x}_2$. Since the **conditional expectation** is the best predictor in mean square ([3.1.9](/3.1.9)), under normality the best predictor equals the best linear predictor; this is the link with linear regression ([3.3](/3.3), [3.4.7](/3.4.7)). The Schur complement also appears in the inverse of $\Sigma$: by the block inversion formula ([2.1.2](/2.1.2)),

$$
\begin{bmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{bmatrix}^{-1} = \begin{bmatrix} (\Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21})^{-1} & * \\ * & * \end{bmatrix},
$$
so the upper left block of the precision matrix $\Sigma^{-1}$ is the inverse of the conditional covariance matrix. In particular, if $\boldsymbol{X}_1 = (X_i, X_k)^{\mathsf T}$ and $\boldsymbol{X}_2$ consists of the other components, $(\Sigma^{-1})_{ik} = 0$ if and only if $X_i$ and $X_k$ are conditionally independent given the rest. This is the basis of Gaussian graphical models.

**Theorem 2.4.6** Suppose $\boldsymbol{X}_1 \mid \boldsymbol{X}_2 = \boldsymbol{x}_2 \sim \mathcal{N}(A\boldsymbol{x}_2, \Omega)$, where $A$ is a constant matrix and $\Omega$ a constant positive definite matrix, and $\boldsymbol{X}_2 \sim \mathcal{N}(\boldsymbol{\mu}_2, \Sigma_{22})$. Then $\begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix}$ is multivariate normal, and

$$
\boldsymbol{X}_1 \sim \mathcal{N}(A\boldsymbol{\mu}_2, \Omega + A\Sigma_{22}A^{\mathsf T}).
$$

**Proof** Let $\boldsymbol{E} = \boldsymbol{X}_1 - A\boldsymbol{X}_2$. Given $\boldsymbol{X}_2 = \boldsymbol{x}_2$, $\boldsymbol{E} \sim \mathcal{N}(\boldsymbol{0}, \Omega)$, a distribution that does not depend on $\boldsymbol{x}_2$; hence $\boldsymbol{E}$ is independent of $\boldsymbol{X}_2$ and $\boldsymbol{E} \sim \mathcal{N}(\boldsymbol{0}, \Omega)$. By Theorem 2.4.4 (part 3), $(\boldsymbol{E}^{\mathsf T}, \boldsymbol{X}_2^{\mathsf T})^{\mathsf T}$ is normal, and $\begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix} = \begin{bmatrix} I & A \\ O & I \end{bmatrix}\begin{bmatrix} \boldsymbol{E} \\ \boldsymbol{X}_2 \end{bmatrix}$ is normal by Theorem 2.4.2, with $\boldsymbol{X}_1 = \boldsymbol{E} + A\boldsymbol{X}_2$ having mean $A\boldsymbol{\mu}_2$ and covariance $\Omega + A\Sigma_{22}A^{\mathsf T}$. $\square$

Hierarchical models of this kind (a normal observation whose mean is itself normal) are the basic computation of Bayesian statistics with normal priors.

### 2.4.4. The Chi-Square Property and Linear Combinations of Normal Vectors

**Theorem 2.4.7** Let $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ with $\Sigma$ positive definite. Then

1. $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_p$, the **chi-square distribution** with $p$ degrees of freedom;
2. the distribution $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ assigns probability $1 - \alpha$ to the solid ellipsoid $\{\boldsymbol{x}\colon (\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) \le \chi^2_{p,\alpha}\}$, where $\chi^2_{p,\alpha}$ is the upper $\alpha$ quantile of $\chi^2_p$.

**Proof** By Theorem 2.4.2, $\boldsymbol{Z} = \Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \mathcal{N}_p(\boldsymbol{0}, I_p)$, so $Z_1, \dots, Z_p$ are iid $\mathcal{N}(0, 1)$ by Theorem 2.4.4, and

$$
(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) = [\Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu})]^{\mathsf T}[\Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu})] = \boldsymbol{Z}^{\mathsf T}\boldsymbol{Z} = Z_1^2 + \cdots + Z_p^2 \sim \chi^2_p.
$$
Part 2 follows from part 1. $\square$

The squared Mahalanobis distance of a normal vector from its mean is thus $\chi^2_p$, with mean $p$ in agreement with Corollary 1.3.2. For $p = 2$, the $\chi^2_2$ distribution is the exponential distribution with mean $2$, and $\chi^2_{2,0.05} \approx 5.99$. Replacing $\boldsymbol{\mu}$ and $\Sigma$ by estimates gives an ellipse $\{\boldsymbol{x}\colon (\boldsymbol{x} - \hat{\boldsymbol{\mu}})^{\mathsf T}\hat\Sigma^{-1}(\boldsymbol{x} - \hat{\boldsymbol{\mu}}) \le \chi^2_{2,\alpha}\}$ that should contain about $100(1 - \alpha)\%$ of the observations if the data are normal, a simple graphical check of normality.

**Theorem 2.4.8 (Linear Combinations of Independent Normal Vectors)** Let $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ be mutually independent with $\boldsymbol{X}_j \sim \mathcal{N}_p(\boldsymbol{\mu}_j, \Sigma)$ (all with the same covariance matrix $\Sigma$). Then

1. $\boldsymbol{V}_1 = c_1\boldsymbol{X}_1 + c_2\boldsymbol{X}_2 + \cdots + c_n\boldsymbol{X}_n \sim \mathcal{N}_p\left(\sum_{j=1}^{n}c_j\boldsymbol{\mu}_j,\ \left(\sum_{j=1}^{n}c_j^2\right)\Sigma\right)$;
2. $\boldsymbol{V}_1$ and $\boldsymbol{V}_2 = b_1\boldsymbol{X}_1 + \cdots + b_n\boldsymbol{X}_n$ are jointly multivariate normal with covariance matrix

$$
\begin{bmatrix} \left(\sum_{j}c_j^2\right)\Sigma & (\boldsymbol{b}^{\mathsf T}\boldsymbol{c})\Sigma \\ (\boldsymbol{b}^{\mathsf T}\boldsymbol{c})\Sigma & \left(\sum_{j}b_j^2\right)\Sigma \end{bmatrix};
$$
3. consequently, $\boldsymbol{V}_1$ and $\boldsymbol{V}_2$ are independent if $\boldsymbol{b}^{\mathsf T}\boldsymbol{c} = \sum_{j=1}^{n}b_jc_j = 0$.

**Proof** By Theorem 2.4.4 (part 3), the stacked $np$-vector $\tilde{\boldsymbol{X}} = (\boldsymbol{X}_1^{\mathsf T}, \dots, \boldsymbol{X}_n^{\mathsf T})^{\mathsf T}$ is normal with block diagonal covariance $\operatorname{diag}(\Sigma, \dots, \Sigma)$. Now $\boldsymbol{V}_1 = [c_1I_p, \dots, c_nI_p]\tilde{\boldsymbol{X}}$ and similarly for $\boldsymbol{V}_2$, so $(\boldsymbol{V}_1^{\mathsf T}, \boldsymbol{V}_2^{\mathsf T})^{\mathsf T}$ is a linear transformation of $\tilde{\boldsymbol{X}}$ and is normal by Theorem 2.4.2 (when $\boldsymbol{b}$ and $\boldsymbol{c}$ are linearly dependent the covariance matrix is singular, and the statement is read as a normal distribution with singular covariance). The covariances follow from bilinearity and independence:

$$
\operatorname{Cov}(\boldsymbol{V}_1, \boldsymbol{V}_2) = \operatorname{Cov}\left(\sum_jc_j\boldsymbol{X}_j, \sum_lb_l\boldsymbol{X}_l\right) = \sum_jc_jb_j\operatorname{Cov}(\boldsymbol{X}_j) = (\boldsymbol{b}^{\mathsf T}\boldsymbol{c})\Sigma.
$$
Part 3 follows from Theorem 2.4.4. $\square$

For example, the sample mean $\bar{\boldsymbol{X}} = \frac{1}{n}\boldsymbol{X}_1 + \cdots + \frac{1}{n}\boldsymbol{X}_n$ of a normal sample is $\mathcal{N}_p(\boldsymbol{\mu}, \frac{1}{n}\Sigma)$, and any combination $\sum_jb_j\boldsymbol{X}_j$ with $\sum_jb_j = 0$ is independent of it. This is the key to the sampling distribution of $(\bar{\boldsymbol{X}}, S)$ in [3.4.3](/3.4.3).

## 2.5. Estimation Under Normality

### 2.5.1. Maximum Likelihood Estimation

Assume that $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ is a random sample from $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$: the $\boldsymbol{X}_j$ are mutually independent and each $\boldsymbol{X}_j \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$. The joint density, regarded as a function of $(\boldsymbol{\mu}, \Sigma)$ for the observed $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$, is the **likelihood function**

$$
L(\boldsymbol{\mu}, \Sigma) = \prod_{j=1}^{n}\frac{1}{(2\pi)^{p/2}(\det\Sigma)^{1/2}}\mathrm{e}^{-(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu})/2} = \frac{1}{(2\pi)^{np/2}(\det\Sigma)^{n/2}}\exp\left\{-\frac{1}{2}\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu})\right\},
$$
with **log-likelihood function**

$$
\ell(\boldsymbol{\mu}, \Sigma) = -\frac{np}{2}\log(2\pi) - \frac{n}{2}\log\det\Sigma - \frac{1}{2}\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu}).
$$

**Theorem 2.5.1 (Maximum Likelihood Estimators)** Let $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ be a random sample from $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ with $n > p$. Then

$$
\hat{\boldsymbol{\mu}} = \bar{\boldsymbol{X}}, \qquad \hat\Sigma = \frac{1}{n}\sum_{j=1}^{n}(\boldsymbol{X}_j - \bar{\boldsymbol{X}})(\boldsymbol{X}_j - \bar{\boldsymbol{X}})^{\mathsf T} = \frac{n-1}{n}S
$$
are the maximum likelihood estimators of $\boldsymbol{\mu}$ and $\Sigma$. Their observed values $\bar{\boldsymbol{x}}$ and $\frac{1}{n}\sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}$ are the maximum likelihood estimates.

**Proof** We follow the one-dimensional route: set the derivatives of $\ell$ to zero, using [3.4.1](/3.4.1), Section 1.8 (denominator layout). For $\boldsymbol{\mu}$, write $(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu}) = \boldsymbol{z}^{\mathsf T}\Sigma^{-1}\boldsymbol{z}$ with $\boldsymbol{z} = \boldsymbol{\mu} - \boldsymbol{x}_j$. By the chain rule and Property 1.8.1, $\frac{\partial}{\partial\boldsymbol{\mu}}\boldsymbol{z}^{\mathsf T}\Sigma^{-1}\boldsymbol{z} = \frac{\partial\boldsymbol{z}}{\partial\boldsymbol{\mu}}\cdot 2\Sigma^{-1}\boldsymbol{z} = 2\Sigma^{-1}(\boldsymbol{\mu} - \boldsymbol{x}_j)$, so

$$
\frac{\partial\ell}{\partial\boldsymbol{\mu}} = -\Sigma^{-1}\sum_{j=1}^{n}(\boldsymbol{\mu} - \boldsymbol{x}_j) = \boldsymbol{0} \iff \hat{\boldsymbol{\mu}} = \frac{1}{n}\sum_{j=1}^{n}\boldsymbol{x}_j = \bar{\boldsymbol{x}},
$$
whatever $\Sigma$ is. For $\Sigma$, write each quadratic form as a trace, $(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu}) = \operatorname{tr}(\Sigma^{-1}B_j)$ with $B_j = (\boldsymbol{x}_j - \boldsymbol{\mu})(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}$, and apply Property 1.8.2:

$$
\frac{\partial\ell}{\partial\Sigma} = -\frac{n}{2}\Sigma^{-1} + \frac{1}{2}\Sigma^{-1}\left(\sum_{j=1}^{n}B_j\right)\Sigma^{-1} = O \iff n\Sigma = \sum_{j=1}^{n}B_j.
$$
Substituting $\hat{\boldsymbol{\mu}} = \bar{\boldsymbol{x}}$ gives $\hat\Sigma = \frac{1}{n}\sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}$, which is positive definite with probability one when $n > p$. That this stationary point is the global maximum follows, for instance, from the inequality $\operatorname{tr}(\Sigma^{-1}B) + n\log\det\Sigma \ge np + n\log\det(B/n)$ for positive definite $B$, with equality only at $\Sigma = B/n$, applied with $B = \sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}$. $\square$

Substituting the estimates, $\sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}\hat\Sigma^{-1}(\boldsymbol{x}_j - \bar{\boldsymbol{x}}) = \operatorname{tr}(\hat\Sigma^{-1} \cdot n\hat\Sigma) = np$, so the maximum of the likelihood is

$$
L(\hat{\boldsymbol{\mu}}, \hat\Sigma) = \frac{1}{(2\pi)^{np/2}}\mathrm{e}^{-np/2}\frac{1}{(\det\hat\Sigma)^{n/2}} \propto (\text{generalized sample variance})^{-n/2}.
$$
This value reappears in the likelihood ratio test of [3.4.3](/3.4.3). By the invariance property of maximum likelihood estimators, the MLE of a function $h(\boldsymbol{\mu}, \Sigma)$ is $h(\hat{\boldsymbol{\mu}}, \hat\Sigma)$: for example, the MLE of $\boldsymbol{\mu}^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}$ is $\hat{\boldsymbol{\mu}}^{\mathsf T}\hat\Sigma^{-1}\hat{\boldsymbol{\mu}}$, and the MLE of $\sqrt{\sigma_{kk}}$ is $\sqrt{\hat\sigma_{kk}}$ with $\hat\sigma_{kk} = \frac{1}{n}\sum_j(x_{jk} - \bar x_k)^2$.

The MLE $\hat\Sigma = S_n$ is biased, and $S$ is its unbiased correction (Theorem 2.2.1); for large $n$ the difference is negligible.

### 2.5.2. Sufficient Statistics

**Theorem 2.5.2** Let $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ be a random sample from $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$. Then $(\bar{\boldsymbol{X}}, S)$ is a **sufficient statistic** for $(\boldsymbol{\mu}, \Sigma)$.

**Proof** As in the proof of Theorem 2.5.1, write the exponent of the likelihood as a trace and decompose around $\bar{\boldsymbol{x}}$:

$$
\begin{aligned}
\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu}) &= \operatorname{tr}\left(\Sigma^{-1}\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu})(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\right) \\
&= \operatorname{tr}\left(\Sigma^{-1}\left[\sum_{j=1}^{n}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T} + n(\bar{\boldsymbol{x}} - \boldsymbol{\mu})(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}\right]\right) \\
&= (n-1)\operatorname{tr}(\Sigma^{-1}S) + n(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}),
\end{aligned}
$$
where the cross terms vanish because $\sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}}) = \boldsymbol{0}$. Hence

$$
L(\boldsymbol{\mu}, \Sigma) = \frac{1}{(2\pi)^{np/2}(\det\Sigma)^{n/2}}\exp\left\{-\frac{n-1}{2}\operatorname{tr}(\Sigma^{-1}S) - \frac{n}{2}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})\right\}
$$
depends on the data only through $\bar{\boldsymbol{x}}$ and $S$, and the **factorization theorem** gives sufficiency. $\square$

For normal populations, therefore, all the information about the parameters contained in the sample is carried by $\bar{\boldsymbol{X}}$ and $S$, whatever the sample size: the data matrix can be reduced to $p + p(p+1)/2$ numbers. This is not true for nonnormal populations, where $\bar{\boldsymbol{X}}$ and $S$ may miss important information; checking the normality assumption is therefore part of every analysis based on these statistics. The sampling distribution of the sufficient statistics is the subject of [3.4.3](/3.4.3).

## Summary

- Descriptive statistics in matrix form: $\bar{\boldsymbol{x}} = \frac{1}{n}X^{\mathsf T}\boldsymbol{1}_n$, $(n-1)S = X^{\mathsf T}HX$ with the centering matrix $H = I_n - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$, $R = D^{-1/2}SD^{-1/2}$. Geometrically (columns as vectors in $\mathbb{R}^n$): mean = projection on $\boldsymbol{1}_n$, variance $\propto$ squared length of the deviation vector, correlation = cosine of the angle.
- Generalized sample variance $\det S = \lambda_1\cdots\lambda_p = (n-1)^{-p}(\text{volume})^2$; it vanishes exactly when some linear combination of the variables is constant (always when $n \le p$), and it ignores orientation.
- Without distributional assumptions: $\mathbb{E}\bar{\boldsymbol{X}} = \boldsymbol{\mu}$, $\operatorname{Cov}(\bar{\boldsymbol{X}}) = \Sigma/n$, $\mathbb{E}S = \Sigma$; linear combinations $A\boldsymbol{x}_j$ have sample mean $A\bar{\boldsymbol{x}}$ and sample covariance $ASA^{\mathsf T}$, mirroring $A\boldsymbol{\mu}$ and $A\Sigma A^{\mathsf T}$.
- $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$: density with the squared Mahalanobis distance in the exponent; contours are ellipsoids centered at $\boldsymbol{\mu}$ with axes $\pm c\sqrt{\lambda_i}\boldsymbol{e}_i$; $\boldsymbol{\mu} + \Sigma^{1/2}\boldsymbol{Z}$ with iid standard normal $\boldsymbol{Z}$.
- Properties: $\boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ normal for all $\boldsymbol{a}$ (equivalent definition); $A\boldsymbol{X} \sim \mathcal{N}(A\boldsymbol{\mu}, A\Sigma A^{\mathsf T})$; marginals normal; under joint normality, independence $\iff \Sigma_{12} = O$; $\boldsymbol{X}_1 \mid \boldsymbol{x}_2 \sim \mathcal{N}(\boldsymbol{\mu}_1 + \Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{x}_2 - \boldsymbol{\mu}_2), \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21})$; $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_p$; $\sum c_j\boldsymbol{X}_j$ and $\sum b_j\boldsymbol{X}_j$ are independent when $\boldsymbol{b}^{\mathsf T}\boldsymbol{c} = 0$.
- Under normality: the MLEs are $\bar{\boldsymbol{X}}$ and $\frac{n-1}{n}S$, the maximized likelihood is proportional to $(\det\hat\Sigma)^{-n/2}$, and $(\bar{\boldsymbol{X}}, S)$ is sufficient.
