---
title: Multidimensional Scaling and Kernel PCA
description: Three equivalent formulations of PCA; computing PCA by the singular value decomposition and the accuracy trade-off with eigendecomposition; proximity and Euclidean distance matrices; classical multidimensional scaling (principal coordinates analysis) and its characterization theorem; kernel PCA and positive definite kernels; t-SNE for visualization.
---

The previous chapter ([3.4.5](/3.4.5)) defined principal components through the eigenvectors of a $p \times p$ covariance matrix. This chapter looks at PCA from three further angles. Theoretically, the one-at-a-time construction is equivalent to fitting the best $r$-dimensional subspace as a whole. Computationally, PCA is obtained from the **singular value decomposition** of the centered data matrix, which is both more accurate and, through the $n \times n$ matrix of inner products between observations, the key to two extensions. The first, multidimensional scaling, reconstructs a configuration of points when only the distances between observations are known. The second, kernel PCA, applies PCA after a nonlinear map into a high-dimensional feature space without ever computing that map. We end with t-SNE, a nonlinear visualization method that borrows the idea of similarities between observations. These tools reappear in cluster analysis ([3.4.11](/3.4.11)) and in statistical computing ([3.5](/3.5)).

## 6.1. PCA Revisited

### 6.1.1. Three Formulations

The principal components of [3.4.5](/3.4.5) can be derived in three equivalent ways:

| | one direction at a time | $r$-dimensional subspace: small distance | $r$-dimensional subspace: large spread |
|---|---|---|---|
| motivation | keep information, i.e. large spread | the projection is close to the data | the projection is spread out |
| model | $\boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ | location $C$, directions $U$, coefficients $\boldsymbol{b}$ | directions $U$ |
| objective | $\max_{\boldsymbol{a}}\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \max_{\boldsymbol{a}}\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}$ | $\min_{U, C, \boldsymbol{b}}\mathbb{E}d^2 = \operatorname{tr}\Sigma - \max_U\operatorname{tr}(U^{\mathsf T}\Sigma U)$ | $\max_U\sum_{i=1}^p\operatorname{Var}(\tilde X_i) = \max_U\operatorname{tr}(U^{\mathsf T}\Sigma U)$ |
| solution | $\boldsymbol{a}_i = \boldsymbol{e}_i$ | $U = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_r]$ for every $r$ | $U = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_r]$ for every $r$ |

Here $U$ has orthonormal columns and $\tilde{\boldsymbol{X}} = UU^{\mathsf T}(\boldsymbol{X} - \boldsymbol{\mu})$ is the projection (see Section 5.6 of [3.4.5](/3.4.5)). The second and third formulations show that the first $r$ components are optimal as a whole, not only one by one.

### 6.1.2. The Data Matrix and the Centering Matrix

Let $X$ be the $n \times p$ **data matrix** with rows $\boldsymbol{x}_1^{\mathsf T}, \dots, \boldsymbol{x}_n^{\mathsf T}$. The sample mean is $\bar{\boldsymbol{x}} = \frac1nX^{\mathsf T}\boldsymbol{1}_n$; for example,

$$
X = \begin{bmatrix} 4 & 1 \\ 5 & 2 \\ 3 & 5 \end{bmatrix}, \qquad \bar{\boldsymbol{x}} = \frac13\begin{bmatrix} 4 & 5 & 3 \\ 1 & 2 & 5 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 \\ 8/3 \end{bmatrix}.
$$

The matrix whose rows all equal $\bar{\boldsymbol{x}}^{\mathsf T}$ is $\boldsymbol{1}_n\bar{\boldsymbol{x}}^{\mathsf T} = \frac1n\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}X$, so subtracting the column means, which removes the influence of location, is multiplication by the **centering matrix** $H = I_n - \frac1n\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$ ([3.4.2](/3.4.2)):

$$
\tilde X = HX = X - \boldsymbol{1}_n\bar{\boldsymbol{x}}^{\mathsf T}, \qquad \tilde x_{ij} = x_{ij} - \bar x_j.
$$

$H$ is symmetric and idempotent ($H^2 = H$): it is the **orthogonal projection matrix** onto the orthogonal complement of $\boldsymbol{1}_n$. Hence

$$
(n-1)S = \tilde X^{\mathsf T}\tilde X = (HX)^{\mathsf T}(HX) = X^{\mathsf T}HX.
$$

### 6.1.3. PCA via the Singular Value Decomposition

Recall that every real $m \times k$ matrix $A$ has a singular value decomposition $A = U\Gamma V^{\mathsf T}$, where $U$ ($m \times m$) and $V$ ($k \times k$) are orthogonal and $\Gamma$ is $m \times k$ with diagonal entries $\gamma_1 \ge \gamma_2 \ge \cdots \ge \gamma_{\min(m,k)} \ge 0$ and zeros elsewhere; the positive $\gamma_i$ are the **singular values** of $A$. Then

$$
AA^{\mathsf T} = U\Gamma\Gamma^{\mathsf T}U^{\mathsf T}, \qquad A^{\mathsf T}A = V\Gamma^{\mathsf T}\Gamma V^{\mathsf T},
$$

so the columns of $U$ and $V$ are eigenvectors of $AA^{\mathsf T}$ and $A^{\mathsf T}A$, with the common nonzero eigenvalues $\gamma_i^2$.

Apply this to the centered data matrix:

$$
S = \frac{1}{n-1}\tilde X^{\mathsf T}\tilde X, \qquad \tilde X = U\Gamma V^{\mathsf T} \ \Longrightarrow\ \tilde X^{\mathsf T}\tilde X = V(\Gamma^{\mathsf T}\Gamma)V^{\mathsf T}.
$$

The right singular vectors are the eigenvectors of $S$: $\hat P = V$, with $\hat\lambda_i = \gamma_i^2/(n-1)$. All principal component scores at once are

$$
Y = \tilde X\hat P = \tilde XV = U\Gamma V^{\mathsf T}V = U\Gamma,
$$

whose $(i, j)$ entry is $\hat y_{ij} = \hat{\boldsymbol{e}}_j^{\mathsf T}(\boldsymbol{x}_i - \bar{\boldsymbol{x}})$, the $j$-th component of the $i$-th unit. The spectral decompositions of $S$ and of $\tilde X^{\mathsf T}\tilde X$ have the same eigenvectors; their eigenvalues differ only by the factor $n - 1$. For the turtle data of [3.4.5](/3.4.5), the first column of $U\Gamma$ coincides with the first principal component score computed from the spectral decomposition of $S$.

### 6.1.4. SVD versus Eigendecomposition

The spectral decomposition is often called the eigenvalue decomposition (EVD). An SVD can be computed through the EVD of $A^{\mathsf T}A$, but the standard algorithms (in LAPACK, used by R and Matlab, a refinement of the Golub–Kahan method in Golub and Van Loan) work on $A$ directly. For PCA there is a trade-off:

- speed: when $n \gg p$, forming the $p \times p$ matrix $S$ and computing its EVD is cheap; when $n \ll p$, it is cheaper to work with the thin SVD of $\tilde X$, or equivalently with the $n \times n$ matrix $\tilde X\tilde X^{\mathsf T}$, which is the idea behind kernel PCA (Section 6.3);
- accuracy: the SVD is better, because forming $\tilde X^{\mathsf T}\tilde X$ squares the condition number and can destroy small singular values in floating-point arithmetic.

**Example 6.1.1 (Läuchli Matrix)** Let

$$
L = \begin{bmatrix} 1 & 1 & 1 \\ \varepsilon & 0 & 0 \\ 0 & \varepsilon & 0 \\ 0 & 0 & \varepsilon \end{bmatrix}, \qquad L^{\mathsf T}L = \begin{bmatrix} 1 + \varepsilon^2 & 1 & 1 \\ 1 & 1 + \varepsilon^2 & 1 \\ 1 & 1 & 1 + \varepsilon^2 \end{bmatrix}.
$$

The singular values of $L$ are $\sqrt{3 + \varepsilon^2}, \varepsilon, \varepsilon$. For $\varepsilon = 0.01$, both the SVD ($1.73208, 0.01, 0.01$) and the EVD of $L^{\mathsf T}L$ ($3.0001, 0.0001, 0.0001$) are accurate. For $\varepsilon = 10^{-10}$, the SVD still returns $1.7320508, 10^{-10}, 10^{-10}$, but in double precision $1 + \varepsilon^2$ rounds to $1$, so $L^{\mathsf T}L$ is computed as a rank-one matrix and its eigenvalues come out as $3, 8.9 \times 10^{-16}, 0$: the small singular values are lost.

## 6.2. Multidimensional Scaling

### 6.2.1. Proximity Matrices

PCA starts from an $n \times p$ data matrix and produces an $n \times k$ matrix of coordinates. In *multidimensional scaling* (MDS) the observed data are only an $n \times n$ matrix $D = (d_{ij})$ of proximities between the $n$ units; a data matrix $X$ may or may not exist. The aim is to represent the proximities by a simple geometric model or map: points $\boldsymbol{z}_1, \dots, \boldsymbol{z}_n$ in a low-dimensional space whose distances reproduce the $d_{ij}$ as well as possible.

Proximity matrices (similarity, dissimilarity or distance matrices) arise either directly, from experiments in which subjects assess the similarity of pairs of stimuli, or indirectly, as correlations, covariances or distances computed from raw profile data. For instance, in a classic study two subjects rated the dissimilarity of every pair of ten brands of cola on a visual analogue scale from $0$ ("same") to $100$ ("different"); the resulting matrix is symmetric and distance-like but need not satisfy the triangle inequality. The airline distances between ten US cities, by contrast, are symmetric, metric (they satisfy the triangle inequality) and nearly Euclidean.

**Definition 6.2.1 (Proximity Matrix)** An $n \times n$ matrix $D = (d_{ij})$ is called a **proximity matrix** if

1. $D = D^{\mathsf T}$, and
2. $d_{ij} \ge 0$ and $d_{ii} = 0$ for all $i, j = 1, \dots, n$.

There are two families of methods. *Metric multidimensional scaling* treats the $d_{ij}$ as distances; its basic form, classical MDS, is the subject of this section. *Nonmetric multidimensional scaling* (for example the Shepard–Kruskal algorithm) uses only the rank order of the proximities, and suits judgments such as the cola data.

### 6.2.2. Euclidean Distance Matrices

Classical MDS assumes that $D$ consists of Euclidean distances computed from an unobserved $n \times p$ data matrix $X$.

**Definition 6.2.2 (Euclidean Distance Matrix)** An $n \times n$ matrix $D = (d_{ij})$ is called a **Euclidean distance matrix** if there exist a positive integer $p$ and $n$ points $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n \in \mathbb{R}^p$ such that

$$
d_{ij}^2 = (\boldsymbol{x}_i - \boldsymbol{x}_j)^{\mathsf T}(\boldsymbol{x}_i - \boldsymbol{x}_j), \qquad i, j = 1, \dots, n.
$$

Given $D$, the configuration is not unique: if $\boldsymbol{z}_i = Q\boldsymbol{x}_i + \boldsymbol{a}$ with $Q$ an **orthogonal matrix** and $\boldsymbol{a}$ a constant vector, the distances are unchanged. A proximity matrix cannot detect shifts, rotations or reflections, so $X$ can be recovered at best up to these transformations. The natural object to recover is therefore one that is invariant under them. In PCA we used the $p \times p$ matrix $(HX)^{\mathsf T}(HX)$, which measures similarity between variables; for similarity between units we use the $n \times n$ matrix

$$
B = (HX)(HX)^{\mathsf T}, \qquad b_{ij} = (\boldsymbol{x}_i - \bar{\boldsymbol{x}})^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}}).
$$

$B$ is unchanged by shifts, rotations and reflections. If $\boldsymbol{y}_i = Q\boldsymbol{x}_i + \boldsymbol{a}$ for all units, then $Y = XQ^{\mathsf T} + \boldsymbol{1}_n\boldsymbol{a}^{\mathsf T}$; since $H\boldsymbol{1}_n = \boldsymbol{0}$, $HY = HXQ^{\mathsf T}$ and

$$
(HY)(HY)^{\mathsf T} = HXQ^{\mathsf T}QX^{\mathsf T}H = (HX)(HX)^{\mathsf T}.
$$

### 6.2.3. Classical Multidimensional Scaling

Write $\tilde x_{ik} = x_{ik} - \bar x_k$, so that $\sum_{i=1}^n\tilde x_{ik} = 0$ for every $k$. The known and the unknown quantities are connected by

$$
d_{ij}^2 = \sum_{k=1}^p(\tilde x_{ik} - \tilde x_{jk})^2 = \sum_k\tilde x_{ik}^2 + \sum_k\tilde x_{jk}^2 - 2\sum_k\tilde x_{ik}\tilde x_{jk} = b_{ii} + b_{jj} - 2b_{ij}.
$$

The task has two steps: recover $B$ from $D$, then decompose $B$.

Step 1 ($D \to B$). The centering constraint gives zero row sums, $\sum_{j=1}^n b_{ij} = \sum_{k=1}^p\tilde x_{ik}\sum_{j=1}^n\tilde x_{jk} = 0$ for every $i$, and by symmetry zero column sums. Let $T = \operatorname{tr}B = \sum_i b_{ii}$. Summing the connection formula,

$$
\sum_{i=1}^n d_{ij}^2 = T + nb_{jj}, \qquad \sum_{j=1}^n d_{ij}^2 = T + nb_{ii}, \qquad \sum_{i=1}^n\sum_{j=1}^n d_{ij}^2 = 2nT.
$$

With the averages $d_{i\cdot}^2 = \frac1n\sum_j d_{ij}^2$, $d_{\cdot j}^2 = \frac1n\sum_i d_{ij}^2$, $d_{\cdot\cdot}^2 = \frac{1}{n^2}\sum_i\sum_j d_{ij}^2$, solving for $b_{ij}$ gives

$$
b_{ij} = -\frac12\big(d_{ij}^2 - d_{i\cdot}^2 - d_{\cdot j}^2 + d_{\cdot\cdot}^2\big), \qquad\text{that is,}\qquad B = HAH, \quad A = (a_{ij}), \ a_{ij} = -\frac12d_{ij}^2.
$$

Step 2 ($B \to$ coordinates). Suppose $\operatorname{rank}(B) = p$ and write the spectral decomposition $B = P_1\Lambda_1P_1^{\mathsf T}$ with $P_1 = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_p]$ ($n \times p$) and $\Lambda_1 = \operatorname{diag}(\lambda_1, \dots, \lambda_p)$, $\lambda_1 \ge \cdots \ge \lambda_p > 0$. Then $Z = P_1\Lambda_1^{1/2}$ satisfies $ZZ^{\mathsf T} = B$, so its rows reproduce the distances exactly. For dimension reduction keep the $k$ largest eigenvalues:

**Algorithm 6.2.1 (Classical Multidimensional Scaling)** Given a proximity matrix $D$ and a target dimension $k$:

1. form $A = (-\frac12d_{ij}^2)$ and $B = HAH$;
2. compute the eigenvalues $\lambda_1 \ge \lambda_2 \ge \cdots$ of $B$ and orthonormal eigenvectors $\boldsymbol{e}_1, \boldsymbol{e}_2, \dots$;
3. return the $n \times k$ configuration $\tilde Z = P_k\Lambda_k^{1/2}$, where $P_k = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_k]$ and $\Lambda_k = \operatorname{diag}(\lambda_1, \dots, \lambda_k)$; its $i$-th row gives the coordinates of unit $i$.

The number $k$ is chosen as in PCA, for example from the proportion $\sum_{i \le k}\lambda_i/\sum_i\lvert\lambda_i\rvert$ (or over the positive eigenvalues) or from a scree plot of the eigenvalues of $B$.

The method is called *classical multidimensional scaling* (CMDS), also *principal coordinates analysis* (PCoA, Gower, 1966), because of its connection with PCA. If $D$ consists of the Euclidean distances between the rows of $X$, then $B = \tilde X\tilde X^{\mathsf T}$, and with $\tilde X = U\Gamma V^{\mathsf T}$,

$$
B = \tilde X\tilde X^{\mathsf T} = U(\Gamma\Gamma^{\mathsf T})U^{\mathsf T}.
$$

So the eigenvectors of $B$ are the left singular vectors of $\tilde X$, its eigenvalues are $\gamma_i^2$, and $P_k\Lambda_k^{1/2}$ consists of the first $k$ columns of $U\Gamma = \tilde X\hat P$: the CMDS configuration is exactly the matrix of the first $k$ principal component scores (up to the sign of each column). PCA reaches $U\Gamma$ from the $p \times p$ matrix of similarities between variables; CMDS reaches it from the $n \times n$ matrix of similarities between units. Writing $W = \tilde X^{\mathsf T}$ for the $p \times n$ matrix that treats the units as "variables", $B = W^{\mathsf T}W$ is the corresponding cross-product matrix.

**Remark 6.2.1** Every row and column of $B$ sums to zero, while a sample covariance matrix $S$ in general does not. The reason is that $B$ was defined from the data matrix with column means removed, which amounts to removing the row means of the $p \times n$ matrix $\tilde X^{\mathsf T}$ before forming cross-products; a sample covariance matrix of the variables is computed without removing the means across variables.

### 6.2.4. When Is a Proximity Matrix Euclidean?

**Theorem 6.2.1** Let $D = (d_{ij})$ be an $n \times n$ proximity matrix, $A = (-\frac12d_{ij}^2)$ and $B = HAH$. Then $D$ is a Euclidean distance matrix if and only if $B$ is positive semidefinite. In that case $D$ is the matrix of distances of a configuration in $\mathbb{R}^p$ with $p = \operatorname{rank}(B)$.

**Proof** ($\Rightarrow$) If $D$ is Euclidean with points $\boldsymbol{x}_i$, the derivation of Step 1 shows $B = (HX)(HX)^{\mathsf T}$, which is positive semidefinite.

($\Leftarrow$) Let $B$ be positive semidefinite with rank $p$, positive eigenvalues $\lambda_1 \ge \cdots \ge \lambda_p > 0$ and orthonormal eigenvectors $\tilde{\boldsymbol{e}}_1, \dots, \tilde{\boldsymbol{e}}_p$; put $\tilde P = [\tilde{\boldsymbol{e}}_1, \dots, \tilde{\boldsymbol{e}}_p]$ ($n \times p$) and $\tilde\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_p)$, so $B = \tilde P\tilde\Lambda\tilde P^{\mathsf T}$. Let $\tilde X = \tilde P\tilde\Lambda^{1/2}$ with rows $\tilde{\boldsymbol{x}}_i^{\mathsf T}$. Then $B = \tilde X\tilde X^{\mathsf T}$, $b_{ij} = \tilde{\boldsymbol{x}}_i^{\mathsf T}\tilde{\boldsymbol{x}}_j$, and

$$
(\tilde{\boldsymbol{x}}_i - \tilde{\boldsymbol{x}}_j)^{\mathsf T}(\tilde{\boldsymbol{x}}_i - \tilde{\boldsymbol{x}}_j) = b_{ii} + b_{jj} - 2b_{ij}. \tag{6.1}
$$

On the other hand, $B = HAH$ means $b_{ij} = a_{ij} - \bar a_{i\cdot} - \bar a_{\cdot j} + \bar a_{\cdot\cdot}$, with $\bar a_{i\cdot}, \bar a_{\cdot j}, \bar a_{\cdot\cdot}$ the row, column and overall means of $A$. Since $d_{ii} = 0$ and $d_{ij} = d_{ji}$, we have $a_{ii} = 0$ and $\bar a_{i\cdot} = \bar a_{\cdot i}$. Substituting into Eq. (6.1), all the means cancel and

$$
(\tilde{\boldsymbol{x}}_i - \tilde{\boldsymbol{x}}_j)^{\mathsf T}(\tilde{\boldsymbol{x}}_i - \tilde{\boldsymbol{x}}_j) = a_{ii} + a_{jj} - 2a_{ij} = -2a_{ij} = d_{ij}^2.
$$

Hence $D$ is the Euclidean distance matrix of $\tilde{\boldsymbol{x}}_1, \dots, \tilde{\boldsymbol{x}}_n \in \mathbb{R}^p$. $\square$

If $B$ has negative eigenvalues, $D$ is not Euclidean; CMDS then uses only the positive part, and the size of the negative eigenvalues measures the departure from a Euclidean configuration.

### 6.2.5. Implementation and an Example

In R, `cmdscale()` (package `stats`) performs classical MDS and can return the eigenvalues of $B$, which helps in choosing $k$; `isoMDS()` (package `MASS`) performs nonmetric MDS, based on the order of the proximities rather than their values. Software results may differ from the theory above because a function called "MDS" may implement a nonmetric method that does not require $D$ to be a distance matrix.

**Example 6.2.1** The road distances (in km) between eight cities in eastern China are

| | Beijing | Tianjin | Jinan | Qingdao | Zhengzhou | Shanghai | Hangzhou | Nanjing |
|---|---|---|---|---|---|---|---|---|
| Beijing | 0 | | | | | | | |
| Tianjin | 118 | 0 | | | | | | |
| Jinan | 439 | 363 | 0 | | | | | |
| Qingdao | 668 | 571 | 362 | 0 | | | | |
| Zhengzhou | 714 | 729 | 443 | 772 | 0 | | | |
| Shanghai | 1259 | 1145 | 886 | 776 | 984 | 0 | | |
| Hangzhou | 1328 | 1191 | 872 | 828 | 962 | 203 | 0 | |
| Nanjing | 1065 | 936 | 626 | 617 | 710 | 322 | 305 | 0 |

The eigenvalues of $B$ (in units of $10^3\,\mathrm{km}^2$) are $1756, 337, 79, 38, 13, 0, -14, -33$. Road distances are not exactly Euclidean, so two eigenvalues are negative, but they are small, and the first two eigenvalues account for $92\%$ of $\sum_i\lvert\lambda_i\rvert$. The two-dimensional CMDS configuration reproduces the geography up to an orthogonal transformation: after a suitable rotation, so that north points up, Beijing and Tianjin lie in the north, Shanghai, Hangzhou and Nanjing in the south-east, Zhengzhou in the west and Qingdao in the east, with Jinan in between, much as on a map.

![Classical MDS of the road distances between eight cities: eigenvalues of B (left; two are slightly negative) and the two-dimensional configuration (right), rotated so that the layout matches the orientation of a map](./plots/cmds-cities.py)

**Remark 6.2.2** MDS can be useful even when a data matrix $X$ is available. One may compute a proximity matrix that better reflects the information of interest, for example from the sample correlations between the observations. If this $D$ is a Euclidean distance matrix, it can be regarded as computed from some data matrix $\tilde X$ with the same number of units (but not necessarily the same number of variables); we never need $\tilde X$ itself, because CMDS gives its low-dimensional representation directly.

### 6.2.6. A Related Method: Latent Semantic Indexing

In the "bag-of-words" model a collection of $C$ documents over a dictionary of $W$ words is summarized by a $C \times W$ matrix of word counts $n_w^{(c)}$. *Latent semantic indexing* (LSI, Deerwester et al., 1990) applies a singular value decomposition to this matrix and keeps the leading singular vectors, which span a low-dimensional subspace of the word–document space capturing most of the variation in the collection. Documents and words are then compared in this latent space, which also achieves substantial compression of large collections.

## 6.3. Kernel PCA

### 6.3.1. Nonlinear Extensions

PCA is a linear projection; it is often used as a preprocessing step, for example before classification, keeping the most important linear features. But data that are not linearly separable may be separable after a nonlinear transformation. Points of two classes arranged as a disk inside a ring in the plane cannot be separated by a line, but after the map

$$
\phi\big((x_1, x_2)^{\mathsf T}\big) = (x_1^2, x_2^2, \sqrt2x_1x_2)^{\mathsf T}
$$

they are separated by a plane in $\mathbb{R}^3$, since $x_1^2 + x_2^2$ is small for the inner class and large for the outer one. Equivalently, we may add more features and then use linear methods.

Suppose we have observations $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n \in \mathbb{R}^{p_0}$ and map them into a feature space of dimension $p > p_0$,

$$
\phi\colon \mathbb{R}^{p_0} \to \mathbb{R}^p, \qquad \boldsymbol{x} \mapsto \tilde{\boldsymbol{x}} = \phi(\boldsymbol{x}),
$$

usually with $p \gg n$ (a high-dimensional problem). Applying PCA to the new features requires the EVD of the $p \times p$ matrix $\tilde S_n = \frac1n(H\Phi)^{\mathsf T}(H\Phi)$, where $\Phi = [\phi(\boldsymbol{x}_1), \dots, \phi(\boldsymbol{x}_n)]^{\mathsf T}$ is $n \times p$. When $p$ is large, or infinite, this is impossible. The remedy is what we learned from PCA and MDS: work with the $n \times n$ matrix of inner products between units instead.

### 6.3.2. The Kernel Trick

Assume first that $\Phi$ is already centered. Instead of $\tilde S_n = \frac1n\Phi^{\mathsf T}\Phi$, we decompose

$$
B = \Phi\Phi^{\mathsf T}, \qquad b_{ij} = \langle\phi(\boldsymbol{x}_i), \phi(\boldsymbol{x}_j)\rangle,
$$

the matrix $B$ of classical MDS for the feature vectors. Its entries are similarities between units, which motivates a new name.

**Definition 6.3.1 (Positive Definite Kernel)** A function $K\colon \mathbb{R}^{p_0} \times \mathbb{R}^{p_0} \to \mathbb{R}$ is called a **positive definite kernel** if it is symmetric, $K(\boldsymbol{x}, \boldsymbol{y}) = K(\boldsymbol{y}, \boldsymbol{x})$, and for every $n$ and every $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ the kernel matrix $K = [K(\boldsymbol{x}_i, \boldsymbol{x}_j)]_{n \times n}$ is positive semidefinite.

Every inner product of features, $K(\boldsymbol{x}_i, \boldsymbol{x}_j) = \langle\phi(\boldsymbol{x}_i), \phi(\boldsymbol{x}_j)\rangle$, is a positive definite kernel, and conversely every positive definite kernel is such an inner product for some feature map into a (possibly infinite-dimensional) Hilbert space (Mercer's theorem, or the Moore–Aronszajn construction of the reproducing kernel Hilbert space). A kernel thus quantifies the similarity of two observations. The connection between PCA and MDS shows that we never need $\phi$ explicitly — sometimes it is not even available, as when the feature space is infinite-dimensional. All we need is to specify $K$. Common choices for $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{p_0}$ are:

- the *polynomial kernel* $K(\boldsymbol{x}, \boldsymbol{y}) = (a\boldsymbol{x}^{\mathsf T}\boldsymbol{y} + c)^d$, $d \in \mathbb{N}_+$, $a > 0$, $c \ge 0$; with $a = 1$, $c = 0$, $d = 2$ in the plane it is exactly the inner product of the features $(x_1^2, x_2^2, \sqrt2x_1x_2)$ above;
- the *Gaussian kernel*, or radial basis function (RBF) kernel, $K(\boldsymbol{x}, \boldsymbol{y}) = \exp\big(-\|\boldsymbol{x} - \boldsymbol{y}\|^2/(2\sigma^2)\big)$, whose feature space is infinite-dimensional;
- the sigmoid kernel $K(\boldsymbol{x}, \boldsymbol{y}) = \tanh(a\boldsymbol{x}^{\mathsf T}\boldsymbol{y} + r)$, popular in practice although it is not positive semidefinite for all parameter values, so it is not a positive definite kernel in general.

### 6.3.3. The Algorithm

**Algorithm 6.3.1 (Kernel PCA)** Given observations $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$, a positive definite kernel $K$ and a dimension $k$:

1. compute the kernel matrix $K = [K(\boldsymbol{x}_i, \boldsymbol{x}_j)]_{n \times n}$;
2. center it: $\tilde K = HKH$;
3. compute the $k$ largest eigenvalues $\lambda_1 \ge \cdots \ge \lambda_k > 0$ of $\tilde K$ and orthonormal eigenvectors $\boldsymbol{\alpha}_1, \dots, \boldsymbol{\alpha}_k$;
4. return the $n \times k$ matrix of kernel principal component scores $[\sqrt{\lambda_1}\boldsymbol{\alpha}_1, \dots, \sqrt{\lambda_k}\boldsymbol{\alpha}_k]$.

The scores are those of ordinary PCA of the centered feature vectors $\phi(\boldsymbol{x}_i) - \bar\phi$, and the variance of the $j$-th component in feature space is $\lambda_j/n$. A new point $\boldsymbol{x}$ is projected through the kernel values $K(\boldsymbol{x}, \boldsymbol{x}_i)$, centered in the same way, as $\lambda_j^{-1/2}\boldsymbol{\alpha}_j^{\mathsf T}\tilde{\boldsymbol{k}}(\boldsymbol{x})$. In R the method is implemented in `kernlab::kpca()`.

*Kernel principal component analysis* (kernel PCA) is linear PCA in the feature space and nonlinear in the original space. Three common questions clarify the construction.

**Remark 6.3.1** Why is kernel PCA nonlinear, when it still performs PCA? The data are first mapped into the high-dimensional feature space and PCA is performed there. The second step is linear, but the map $\phi$ can be nonlinear, so the components are nonlinear functions of the original variables.

**Remark 6.3.2** Both $B$ and $D$ express similarity between units, but in opposite directions. $D$ is a distance: the larger $d_{ij}$, the less similar the units. $B$ imitates a covariance matrix: the closer $b_{ij}$ is to $0$, the weaker the association. The connecting formula $d_{ij}^2 = b_{ii} + b_{jj} - 2b_{ij}$ shows this reverse relation.

**Remark 6.3.3** Why does the algorithm center the kernel matrix as $HKH$ before the spectral decomposition? We want the matrix $B$ of the centered features, which has zero row and column sums: if $\Phi$ were the uncentered feature matrix, then $B = (H\Phi)(H\Phi)^{\mathsf T} = H\Phi\Phi^{\mathsf T}H$. The kernel matrix $K$ corresponds to the uncentered $\Phi\Phi^{\mathsf T}$ and does not have zero row and column sums in general, so $HKH$ is exactly the $B$ we need.

![Two concentric rings in the plane (left): linear PCA only rotates the data and the first component does not separate the rings (middle), whereas kernel PCA with a Gaussian kernel separates them along its first component (right)](./plots/kernel-pca-rings.py)

## 6.4. t-SNE

### 6.4.1. Projection and Manifold Learning

Linear projections such as PCA can fail to display structure that lies on a curved low-dimensional surface (a manifold) in high dimension: projecting a "Swiss roll" onto a plane superimposes its layers, whereas unrolling it would show its true two-dimensional structure. Methods that try to unroll the data are called manifold learning. For visualizing high-dimensional data in two or three dimensions, the most popular of them is *t-distributed stochastic neighbor embedding* (t-SNE, van der Maaten and Hinton, 2008). On the MNIST handwritten digits, for example, the first two principal components show heavily overlapping digit classes, while t-SNE separates most of them into clusters.

The basic idea: place the points in the low-dimensional space so that the neighborhoods (clusters) of the high-dimensional space are preserved. Starting from a random configuration, t-SNE moves the points a little at a time; each point is attracted by points that are similar to it in the original space and repelled by the others.

### 6.4.2. The Method

1. Similarities in the original space. For a point $\boldsymbol{x}_i$, measure its distance to every other point and evaluate it under a normal density centered at $\boldsymbol{x}_i$; normalizing so that the similarities add to $1$ gives

   $$
   p_{j\mid i} = \frac{\exp\big(-\|\boldsymbol{x}_i - \boldsymbol{x}_j\|^2/(2\sigma_i^2)\big)}{\sum_{k \ne i}\exp\big(-\|\boldsymbol{x}_i - \boldsymbol{x}_k\|^2/(2\sigma_i^2)\big)}.
   $$

   Distant points get very small similarities and close points large ones. The width $\sigma_i$ adapts to the density of the data around $\boldsymbol{x}_i$ and is set through a user-chosen *perplexity*, roughly the effective number of neighbors; normalization makes points in dense and sparse regions comparable. The two directions are then averaged, $p_{ij} = \frac{p_{j\mid i} + p_{i\mid j}}{2n}$.
2. Similarities in the low-dimensional space. For the low-dimensional points $\boldsymbol{y}_1, \dots, \boldsymbol{y}_n$, the similarities are computed in the same way but with a Student $t$ distribution with one degree of freedom (hence the name):

   $$
   q_{ij} = \frac{(1 + \|\boldsymbol{y}_i - \boldsymbol{y}_j\|^2)^{-1}}{\sum_{k \ne l}(1 + \|\boldsymbol{y}_k - \boldsymbol{y}_l\|^2)^{-1}}.
   $$

   The heavy tails of the $t$ distribution let moderately dissimilar points be placed far apart in the low-dimensional map, which relieves the "crowding" of points that a normal kernel would cause and separates clusters clearly.
3. Matching. The points $\boldsymbol{y}_i$ are moved by gradient descent so that the matrix $(q_{ij})$ looks more and more like $(p_{ij})$, minimizing the *Kullback–Leibler divergence*

   $$
   \mathrm{KL}(P\,\|\,Q) = \sum_{i \ne j}p_{ij}\log\frac{p_{ij}}{q_{ij}}.
   $$

In short, t-SNE converts Euclidean distances into probabilities that express similarity, builds one probability distribution over pairs of objects in the high-dimensional space and another in the low-dimensional space, and makes the two as close as possible.

**Remark 6.4.1** t-SNE borrows only the idea of similarities between units: it describes the similarities in both spaces (fixed in the high-dimensional space, to be found in the low-dimensional one) and matches them to find a good low-dimensional display. It does not use the proximity matrix $D$, the matrix $B$, or the principal component scores of MDS.

![The 1797 handwritten digit images (8 x 8 pixels, p = 64) displayed by their first two principal components (left) and by t-SNE (right), colored by digit: t-SNE separates most digit classes into clusters](./plots/pca-vs-tsne.py)

### 6.4.3. Strengths and Limitations

t-SNE is designed for the visualization of high-dimensional data in low dimension and is widely available (for example the R package `tsne`). Its limitations are:

- it gives no explicit map, so it cannot be applied directly to new data;
- it tends to preserve local structure; distances between clusters and cluster sizes in the map are not meaningful, and data of intrinsically high dimension cannot be represented well in two or three dimensions;
- it is slow; when the original dimension is very high, PCA is usually applied first and t-SNE afterwards.

A more recent method with similar aims is UMAP (Uniform Manifold Approximation and Projection, McInnes et al., 2018; R package `umap`), which is faster and preserves more of the global structure.

## Summary

- PCA can be formulated one direction at a time or for a whole subspace (smallest distance or largest spread); all three give the same components. It is computed from the SVD $\tilde X = U\Gamma V^{\mathsf T}$ of the centered data matrix: the eigenvectors are $V$, the scores $U\Gamma$; the SVD is more accurate than the EVD of $\tilde X^{\mathsf T}\tilde X$.
- Multidimensional scaling represents an $n \times n$ proximity matrix $D$ by a low-dimensional configuration. Classical MDS forms $B = HAH$ with $a_{ij} = -\frac12d_{ij}^2$ and takes $P_k\Lambda_k^{1/2}$; $D$ is Euclidean exactly when $B$ is positive semidefinite, and for Euclidean distances CMDS reproduces the principal component scores (principal coordinates analysis).
- Kernel PCA replaces the inner products of the data by a positive definite kernel, centers the kernel matrix as $HKH$ and decomposes it: PCA in a feature space that is never computed, nonlinear in the original variables.
- t-SNE matches neighborhood probabilities in the original space (normal kernel) and in the map ($t$ kernel) by minimizing a Kullback–Leibler divergence; it is a tool for visualization, not a general-purpose projection.
