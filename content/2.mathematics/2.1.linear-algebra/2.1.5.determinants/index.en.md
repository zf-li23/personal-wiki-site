---
title: Determinants
source_hash: 72b943932395
---

The determinant assigns a number to a square matrix. It has two equally important interpretations: the signed volume of the parallelepiped whose edges are the columns of the matrix, and the factor by which the corresponding linear transformation scales volumes. Rather than starting from an expansion formula, this chapter abstracts three axioms from signed area (multilinearity in the columns, antisymmetry in the columns, normalization), derives all properties of the determinant and its uniqueness from the axioms, and then uses an expansion formula to prove that a function satisfying the axioms actually exists.

The main results are: $\det A \ne 0$ if and only if $A$ is invertible; $\det(AB) = \det A\det B$; and the determinant can be computed by Gaussian elimination in $O(n^3)$ operations. Cofactors give a formula for the inverse matrix and Cramer's rule, which are useful in theory but unsuitable for numerical computation. This chapter relies on the **elementary matrix**, the **invertible matrix** and elimination from Chapter 2, and on the orthogonal matrices and QR decomposition of Chapter 4; Chapter 6 uses the determinant to define the characteristic polynomial. The permutations in the complete expansion are exactly the **permutations** of 1.3.2.

## 5.1. Signed Volume and the Definition of the Determinant

### 5.1.1. Signed Area

We want to define the signed volume of the parallelepiped in $\mathbb{R}^n$ spanned by $n$ vectors. Start with the plane: the signed area $\delta(\boldsymbol{a}_1, \boldsymbol{a}_2)$ of the parallelogram with sides $\boldsymbol{a}_1 = \begin{bmatrix} a_{11} \\ a_{21} \end{bmatrix}$ and $\boldsymbol{a}_2 = \begin{bmatrix} a_{12} \\ a_{22} \end{bmatrix}$ should satisfy:

- bilinearity: $\delta(k\boldsymbol{a}_1 + k'\boldsymbol{a}_1', \boldsymbol{a}_2) = k\delta(\boldsymbol{a}_1, \boldsymbol{a}_2) + k'\delta(\boldsymbol{a}_1', \boldsymbol{a}_2)$, and likewise in the second argument (stretching a side by a factor $k$ multiplies the area by $k$; adding bases adds areas);
- vanishing on collinear vectors, or equivalently antisymmetry: $\delta(\boldsymbol{a}, \boldsymbol{a}) = 0$, which is equivalent to $\delta(\boldsymbol{a}_1, \boldsymbol{a}_2) = -\delta(\boldsymbol{a}_2, \boldsymbol{a}_1)$ (swapping the two sides reverses the orientation);
- normalization: $\delta(\boldsymbol{e}_1, \boldsymbol{e}_2) = 1$ (the unit square has area $1$).

These three properties determine $\delta$ uniquely:

$$
\begin{aligned}
\delta(\boldsymbol{a}_1, \boldsymbol{a}_2) &= \delta(a_{11}\boldsymbol{e}_1 + a_{21}\boldsymbol{e}_2,\ a_{12}\boldsymbol{e}_1 + a_{22}\boldsymbol{e}_2) \\
&= a_{11}a_{12}\delta(\boldsymbol{e}_1, \boldsymbol{e}_1) + a_{11}a_{22}\delta(\boldsymbol{e}_1, \boldsymbol{e}_2) + a_{21}a_{12}\delta(\boldsymbol{e}_2, \boldsymbol{e}_1) + a_{21}a_{22}\delta(\boldsymbol{e}_2, \boldsymbol{e}_2) \\
&= a_{11}a_{22} - a_{12}a_{21}.
\end{aligned}
$$

### 5.1.2. The Axiomatic Definition of the Determinant

Regarding a function $\delta(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n)$ of $n$ column vectors as a function $\delta(A)$ of the square matrix $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$, we arrive at the following definition.

**Definition 5.1.1 (Determinant)** A function $\delta\colon \mathbb{R}^{n \times n} \to \mathbb{R}$ on all square matrices of order $n$ satisfying

1. multilinearity in the columns: it is linear in each column, that is, for $i = 1, \dots, n$,
   $$
   \delta(\dots, k\boldsymbol{a}_i + k'\boldsymbol{a}_i', \dots) = k\delta(\dots, \boldsymbol{a}_i, \dots) + k'\delta(\dots, \boldsymbol{a}_i', \dots);
   $$
2. antisymmetry in the columns: interchanging any two columns changes the sign, that is, for $i < j$, $\delta(\dots, \boldsymbol{a}_i, \dots, \boldsymbol{a}_j, \dots) = -\delta(\dots, \boldsymbol{a}_j, \dots, \boldsymbol{a}_i, \dots)$;
3. normalization: $\delta(I_n) = 1$,

is called a determinant function of order $n$. The value of the determinant function at a square matrix $A$ is called the **determinant** of $A$, written $\det(A)$, $\det A$ or $|A|$.

We will prove that a determinant function of order $n$ exists and is unique (Theorem 5.3.1, Theorem 5.5.1), so "the determinant of $A$" is well defined. The notation $|A|$ is normally used only when $A$ is written out as an array of $n$ rows and $n$ columns ($n > 1$); it should not be confused with the absolute value.

**Example 5.1.1** The determinant of order one is $\det[a_{11}] = a_{11}$; the determinant of order two is the signed area:

$$
\begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}.
$$

By multilinearity in the columns, $\det(kA) = k^n\det A$, in agreement with how volumes scale. Hence for $n > 1$ the determinant is not a linear function: in general $\det(A + B) \ne \det A + \det B$.

**Property 5.1.1 (Vanishing on Dependent Columns)** Let $A$ be a square matrix of order $n$.

1. If $A$ has two equal columns, then $\det A = 0$;
2. if $A$ does not have full rank (that is, is not invertible), then $\det A = 0$;
3. if $A$ has a zero column or a zero row, then $\det A = 0$.

**Proof** 1. Interchanging the two columns leaves the matrix unchanged, so by antisymmetry $\det A = -\det A$. 2. If $A$ does not have full rank, its columns are **linearly dependent**, so some column is a **linear combination** of the others, $\boldsymbol{a}_j = \sum_{i \ne j} k_i\boldsymbol{a}_i$. By multilinearity,

$$
\det A = \sum_{i \ne j} k_i\,\delta(\boldsymbol{a}_1, \dots, \boldsymbol{a}_{j-1}, \boldsymbol{a}_i, \boldsymbol{a}_{j+1}, \dots, \boldsymbol{a}_n) = 0,
$$

since every term has two equal columns. 3. A matrix with a zero row or column does not have full rank, so this follows from 2. $\square$

Given multilinearity in the columns, antisymmetry is equivalent to "two equal columns give zero": one direction was shown above; conversely, if the value is always zero when two columns are equal, then

$$
0 = \delta(\dots, \boldsymbol{a}_i + \boldsymbol{a}_j, \dots, \boldsymbol{a}_i + \boldsymbol{a}_j, \dots) = \delta(\dots, \boldsymbol{a}_i, \dots, \boldsymbol{a}_j, \dots) + \delta(\dots, \boldsymbol{a}_j, \dots, \boldsymbol{a}_i, \dots).
$$

Geometrically, part 2 of Property 5.1.1 says that a parallelepiped whose edges lie in a lower-dimensional subspace is "flat" and has volume zero. Only invertible matrices can have a nonzero determinant; the next section proves that their determinant is indeed nonzero.

## 5.2. Properties of the Determinant

### 5.2.1. Determinants of Elementary Matrices

Denote the three kinds of elementary matrices of Chapter 2 as follows: the interchange matrix $P_{ij}$ (swaps columns $i$ and $j$); the scaling matrix $E_{ii;k}$ (multiplies column $i$ by $k \ne 0$); and the row-addition matrix $E_{ji;k} = I_n + k\boldsymbol{e}_j\boldsymbol{e}_i^{\mathsf T}$ (multiplication on the right adds $k$ times column $j$ to column $i$).

**Proposition 5.2.1 (Determinants of Elementary Matrices)** $\det P_{ij} = -1$, $\det E_{ii;k} = k$ and $\det E_{ji;k} = 1$. An elementary matrix and its transpose have the same determinant.

**Proof** Each of the three kinds of elementary matrices is obtained from $I_n$ by one elementary column operation. $P_{ij}$ interchanges two columns of $I_n$, so by antisymmetry $\det P_{ij} = -\det I_n = -1$; $E_{ii;k}$ multiplies column $i$ by $k$, so by multilinearity $\det E_{ii;k} = k$; for $E_{ji;k}$,

$$
\det E_{ji;k} = \delta(\dots, \boldsymbol{e}_i + k\boldsymbol{e}_j, \dots, \boldsymbol{e}_j, \dots) = \delta(\dots, \boldsymbol{e}_i, \dots, \boldsymbol{e}_j, \dots) + k\,\delta(\dots, \boldsymbol{e}_j, \dots, \boldsymbol{e}_j, \dots) = 1.
$$

Moreover $P_{ij}^{\mathsf T} = P_{ij}$, $E_{ii;k}^{\mathsf T} = E_{ii;k}$ and $E_{ji;k}^{\mathsf T} = E_{ij;k}$, so transposition does not change the determinant. $\square$

**Proposition 5.2.2 (Determinants under Elementary Column Operations)** In the same way:

1. interchanging columns $i$ and $j$ of $A$: $\det(AP_{ij}) = -\det A = \det A\det P_{ij}$;
2. multiplying column $i$ of $A$ by $k \ne 0$: $\det(AE_{ii;k}) = k\det A = \det A\det E_{ii;k}$;
3. adding $k$ times column $j$ of $A$ to column $i$: $\det(AE_{ji;k}) = \det A = \det A\det E_{ji;k}$.

That is, $\det(AE) = \det A\det E$ for every elementary matrix $E$.

### 5.2.2. Rules for Determinants

**Theorem 5.2.1** Let $A, B$ be square matrices of order $n$.

1. If the invertible matrix $A = E_1E_2\cdots E_m$ is a product of elementary matrices $E_i$, then $\det A = \det E_1\det E_2\cdots\det E_m$;
2. $\det A \ne 0$ if and only if $A$ is invertible;
3. $\det(AB) = \det A\det B = \det(BA)$;
4. $\det A^{\mathsf T} = \det A$.

**Proof** 1. Apply Proposition 5.2.2 repeatedly: $\det A = \det(E_1\cdots E_{m-1})\det E_m = \cdots = \det E_1\cdots\det E_m$.

2. An invertible matrix is a product of elementary matrices (Chapter 2), so by 1 and Proposition 5.2.1 its determinant is a product of nonzero numbers, hence nonzero; a matrix that is not invertible has determinant zero (Property 5.1.1).

3. If $B$ is invertible, $B = E_1\cdots E_m$, then $\det(AB) = \det(AE_1\cdots E_m) = \det A\det E_1\cdots\det E_m = \det A\det B$. If $B$ is not invertible, then neither is $AB$ ($\operatorname{rank}(AB) \le \operatorname{rank}(B) < n$), and both sides are $0$. Interchanging $A$ and $B$ gives the second equality.

4. If $A = E_1\cdots E_m$ is invertible, then $A^{\mathsf T} = E_m^{\mathsf T}\cdots E_1^{\mathsf T}$, and by Proposition 5.2.1 and part 1, $\det A^{\mathsf T} = \det E_m\cdots\det E_1 = \det A$. If $A$ is not invertible, then neither is $A^{\mathsf T}$, and both sides are $0$. $\square$

By 3, if $A$ is invertible then $\det A\det A^{-1} = \det I_n = 1$, that is, $\det A^{-1} = 1/\det A$. Note that although the product formula holds, there is no corresponding formula for sums.

**Corollary 5.2.1 (The Determinant as a Function of the Rows)** Since $\det A^{\mathsf T} = \det A$:

1. the determinant is also multilinear and antisymmetric in the rows; elementary row operations affect the determinant in the same way as elementary column operations;
2. if a function $\delta\colon \mathbb{R}^{n \times n} \to \mathbb{R}$ is multilinear and antisymmetric in the rows and normalized, then $\delta$ is the determinant function of order $n$ (because $A \mapsto \delta(A^{\mathsf T})$ satisfies Definition 5.1.1).

## 5.3. Geometric Meaning and Uniqueness

### 5.3.1. The Volume Scaling Factor

Consider $\det(AB) = \det A\det B$ from the point of view of linear transformations: let $A$ correspond to the linear transformation $\boldsymbol{x} \mapsto A\boldsymbol{x}$ and $B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_n]$. Then

$$
\det(AB) = \delta(A\boldsymbol{b}_1, \dots, A\boldsymbol{b}_n) = \det A \cdot \delta(\boldsymbol{b}_1, \dots, \boldsymbol{b}_n),
$$

that is, under $A$ the signed volume of the parallelepiped with edges $\boldsymbol{b}_1, \dots, \boldsymbol{b}_n$ is multiplied by $\det A$. For this reason $\det A$ is called the volume scaling factor of the linear transformation $A$; the scaling factor of a composition is the product of the individual factors. The sign of $\det A$ tells whether the transformation preserves orientation, and $|\det A|$ is the factor by which volumes are enlarged. This viewpoint reappears in the change of variables for multiple integrals (the Jacobian determinant).

In the plane, the three kinds of elementary transformations correspond exactly to three basic geometric operations:

| Elementary matrix | Example | Geometric meaning | Determinant | Corresponding elimination step |
|---|---|---|---|---|
| interchange matrix $P_{12}$ | $(x_1, x_2) \mapsto (x_2, x_1)$ | reflection across the line $x_1 = x_2$ | $-1$ | interchanging two rows: the determinant changes sign |
| scaling matrix $E_{11;k}$ | $(x_1, x_2) \mapsto (kx_1, x_2)$ | stretch along the $x_1$ direction | $k$ | multiplying a row by $k$: the determinant is multiplied by $k$ |
| row-addition matrix $E_{21;k}$ | $(x_1, x_2) \mapsto (x_1, kx_1 + x_2)$ | shear (same base, same height) | $1$ | adding a multiple of one row to another: unchanged |

The figure below shows the images of the unit square, and of the letter F inside it, under several transformations: the area of the image equals $|\det A|$, and the interchange (a reflection) turns F into its mirror image, corresponding to $\det A < 0$.

![Images of the unit square under a shear, a stretch, an interchange and a general linear transformation: the area of the parallelogram is |det A|, and when det A is negative the letter F is mirrored (the orientation is reversed)](./plots/determinant-area.py)

In general, the interchange matrix of order $n$, $P_{ij} = I_n - (\boldsymbol{e}_i - \boldsymbol{e}_j)(\boldsymbol{e}_i - \boldsymbol{e}_j)^{\mathsf T} = I_n - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}$ with $\boldsymbol{v} = (\boldsymbol{e}_i - \boldsymbol{e}_j)/\sqrt{2}$, is a **Householder reflection**.

### 5.3.2. Uniqueness

**Theorem 5.3.1** If a determinant function of order $n$ exists, it is unique.

**Proof** Let $\delta_1, \delta_2$ be determinant functions. If $A$ does not have full rank, $\delta_1(A) = \delta_2(A) = 0$; if $A$ is an elementary matrix, Proposition 5.2.1 used only the axioms, so $\delta_1(A) = \delta_2(A)$; if $A$ is invertible, $A = E_1\cdots E_m$, then $\delta_1(A) = \delta_1(E_1)\cdots\delta_1(E_m) = \delta_2(E_1)\cdots\delta_2(E_m) = \delta_2(A)$. $\square$

The proof shows that the determinant is determined by its values on elementary matrices together with the product rule:

**Proposition 5.3.1** If a function $\delta$ on all square matrices of order $n$ satisfies the following five conditions, then $\delta$ is the determinant function:

1. $\delta(AB) = \delta(A)\delta(B)$;
2. $\delta(A) = 0$ if $A$ is not invertible;
3. interchange matrices satisfy $\delta(P_{ij}) = -1$;
4. scaling matrices satisfy $\delta(E_{ii;k}) = k$ ($k \ne 0$);
5. row-addition matrices satisfy $\delta(E_{ji;k}) = 1$.

These five conditions are exactly the properties that "the volume scaling factor of a linear transformation of $\mathbb{R}^n$" ought to have.

## 5.4. Computing Determinants

### 5.4.1. Determinants of Special Matrices

**Example 5.4.1**

1. **Diagonal matrix**: by multilinearity in the columns, the determinant is the product of the diagonal entries; geometrically, it is the signed volume of a box whose edges point along the standard basis directions.
2. **Triangular matrix**: the determinant is the product of the diagonal entries. If some diagonal entry is zero, the matrix does not have full rank and the determinant is zero; otherwise, row-addition operations eliminate the off-diagonal entries without changing the determinant. Geometrically, a sequence of shears with the same base and height turns the parallelepiped into a box of the same volume.
3. Orthogonal matrix $Q$: taking determinants in $Q^{\mathsf T}Q = I_n$ gives $(\det Q)^2 = 1$, so $\det Q = \pm 1$. Orthogonal transformations preserve lengths and angles and do not change the size of volumes.
4. Invertible matrix $X$: $\det X^{-1} = 1/\det X$, and furthermore $\det(X^{-1}AX) = \det A$.
5. Block diagonal and block triangular matrices: for square matrices $A, B$,
   $$
   \det\begin{bmatrix} A & O \\ O & B \end{bmatrix} = \det\begin{bmatrix} A & C \\ O & B \end{bmatrix} = \det\begin{bmatrix} A & O \\ D & B \end{bmatrix} = \det A\det B.
   $$

For the block upper triangular matrix in item 5 the proof goes as follows (the other cases are similar). If $A$ is not invertible, the first few columns are linearly dependent and both sides are zero. If $A$ is invertible,

$$
\begin{bmatrix} A & C \\ O & B \end{bmatrix} = \begin{bmatrix} A & O \\ O & I \end{bmatrix}\begin{bmatrix} I & A^{-1}C \\ O & B \end{bmatrix}.
$$

The function $X \mapsto \det\begin{bmatrix} X & O \\ O & I \end{bmatrix}$ satisfies the three axioms of Definition 5.1.1, so it equals $\det X$; in the second factor, column additions using the earlier columns eliminate $A^{-1}C$ without changing the determinant, and the same argument gives $\det\begin{bmatrix} I & O \\ O & B \end{bmatrix} = \det B$.

Item 3 and the QR decomposition give an intuitive interpretation of the determinant: if $A = QR$ (Chapter 4), then $\det A = \det Q\det R$, where $\det Q = \pm 1$ is the sign of the signed volume and $\det R = \prod_i r_{ii} = \prod_i \|\tilde{\boldsymbol{q}}_i\| \ge 0$ is its size. Here $\|\tilde{\boldsymbol{q}}_i\|$ is the distance from $\boldsymbol{a}_i$ to the subspace spanned by the first $i-1$ edges, that is, the successive "heights" of the parallelepiped, so $|\det A|$ is the $n$-dimensional generalization of "base times height".

![The case of order 2: the parallelogram with sides a1, a2 and the rectangle with base a1 and height q2 (from Gram–Schmidt) have the same area, |det A| = ||a1|| · ||q2||](./plots/base-times-height.py)

### 5.4.2. Computing Determinants by Elimination

For a general matrix, the basic method for computing the determinant is to simplify the matrix by elementary operations while recording the effect of each step on the determinant:

- adding a multiple of one row (column) to another: the determinant is unchanged;
- interchanging two rows (columns): the determinant changes sign;
- multiplying a row (column) by $k$: the determinant is multiplied by $k$.

**Algorithm 5.4.1 (Determinant by Gaussian Elimination)** Input: a square matrix $A$ of order $n$.

1. Perform Gaussian elimination on $A$ (interchanging rows to choose pivots when necessary), using only row additions and interchanges, to reduce it to an upper triangular matrix $U$, and record the number $s$ of interchanges; if at some step no nonzero pivot can be found, then $\det A = 0$;
2. $\det A = (-1)^s u_{11}u_{22}\cdots u_{nn}$.

In matrix language, this computes the **PLU decomposition** $PA = LU$, so $\det A = \det P^{-1}\det L\det U = \pm\prod_i u_{ii}$. The cost is about $\frac{2}{3}n^3$ floating-point operations, comparable to solving one linear system.

**Example 5.4.2** Compute $\det A = \begin{vmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \\ 3 & 7 & 10 \end{vmatrix}$.

Eliminate the first column by row additions, then interchange the last two rows:

$$
\begin{vmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \\ 3 & 7 & 10 \end{vmatrix} = \begin{vmatrix} 1 & 2 & 3 \\ 0 & 0 & 1 \\ 0 & 1 & 1 \end{vmatrix} = -\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{vmatrix} = -1.
$$

Alternatively, at the second step one can view the matrix as block upper triangular: $\begin{vmatrix} 1 & 2 & 3 \\ 0 & 0 & 1 \\ 0 & 1 & 1 \end{vmatrix} = 1 \cdot \begin{vmatrix} 0 & 1 \\ 1 & 1 \end{vmatrix} = -1$.

### 5.4.3. Vandermonde Determinants and Polynomial Interpolation

**Example 5.4.3** Suppose a quadratic polynomial $p(x) = k_2x^2 + k_1x + k_0$ passes through three points $(\lambda_i, \mu_i)$ ($i = 1, 2, 3$) with pairwise distinct abscissas. Does such a polynomial exist? Is it unique?

The conditions $p(\lambda_i) = \mu_i$ form a linear system in the coefficients:

$$
\begin{bmatrix} 1 & \lambda_1 & \lambda_1^2 \\ 1 & \lambda_2 & \lambda_2^2 \\ 1 & \lambda_3 & \lambda_3^2 \end{bmatrix}\begin{bmatrix} k_0 \\ k_1 \\ k_2 \end{bmatrix} = \begin{bmatrix} \mu_1 \\ \mu_2 \\ \mu_3 \end{bmatrix}.
$$

The polynomial exists and is unique if and only if the coefficient matrix is invertible, that is, its determinant is nonzero. Working from right to left, add $-\lambda_1$ times each column to the column on its right:

$$
\begin{vmatrix} 1 & \lambda_1 & \lambda_1^2 \\ 1 & \lambda_2 & \lambda_2^2 \\ 1 & \lambda_3 & \lambda_3^2 \end{vmatrix}
= \begin{vmatrix} 1 & 0 & 0 \\ 1 & \lambda_2 - \lambda_1 & \lambda_2^2 - \lambda_2\lambda_1 \\ 1 & \lambda_3 - \lambda_1 & \lambda_3^2 - \lambda_3\lambda_1 \end{vmatrix}
= (\lambda_2 - \lambda_1)(\lambda_3 - \lambda_1)\begin{vmatrix} 1 & \lambda_2 \\ 1 & \lambda_3 \end{vmatrix}
= \prod_{1 \le j < i \le 3}(\lambda_i - \lambda_j).
$$

This is nonzero when the $\lambda_i$ are pairwise distinct, so three points determine a unique polynomial of degree at most $2$.

**Definition 5.4.1 (Vandermonde Matrix)** A matrix of the form

$$
V = \begin{bmatrix} 1 & \lambda_1 & \lambda_1^2 & \cdots & \lambda_1^{n-1} \\ 1 & \lambda_2 & \lambda_2^2 & \cdots & \lambda_2^{n-1} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & \lambda_n & \lambda_n^2 & \cdots & \lambda_n^{n-1} \end{bmatrix}
$$

is called a **Vandermonde matrix**.

**Theorem 5.4.1** $\det V = \displaystyle\prod_{1 \le j < i \le n}(\lambda_i - \lambda_j)$. In particular, $V$ is invertible when $\lambda_1, \dots, \lambda_n$ are pairwise distinct.

**Proof** We use induction on $n$; for $n = 2$, $\det V = \lambda_2 - \lambda_1$. As in Example 5.4.3, starting from the last column, add $-\lambda_1$ times column $k$ to column $k+1$ in turn ($k = n-1, \dots, 1$). Row $i$ becomes $[1,\ \lambda_i - \lambda_1,\ \lambda_i(\lambda_i - \lambda_1),\ \dots,\ \lambda_i^{n-2}(\lambda_i - \lambda_1)]$ and the first row becomes $[1, 0, \dots, 0]$. Computing the determinant as that of a block lower triangular matrix and factoring $\lambda_i - \lambda_1$ out of row $i$ ($i \ge 2$) gives

$$
\det V = \prod_{i=2}^n(\lambda_i - \lambda_1) \cdot \det V(\lambda_2, \dots, \lambda_n),
$$

where $V(\lambda_2, \dots, \lambda_n)$ is a Vandermonde matrix of order $n-1$. The claim follows from the induction hypothesis. $\square$

**Definition 5.4.2 (Polynomial Interpolation)** Finding a curve through given points in the plane is called interpolation; when the interpolating function is a polynomial, it is called **polynomial interpolation**.

By Theorem 5.4.1, for $n$ points with pairwise distinct abscissas there is a unique interpolating polynomial of degree at most $n-1$. Solving the Vandermonde system directly is not a good way to compute the interpolating polynomial ($V$ is often very ill-conditioned); the Lagrange interpolation formula is given in [Chapter 9](/2.1.9).

## 5.5. Expansion of the Determinant

### 5.5.1. Minors and Cofactors

**Example 5.5.1** Splitting the first column by multilinearity and then moving the nonzero entries to the first row by antisymmetry in the rows, we can express a determinant of order three through determinants of order two:

$$
\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix}
= a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix}
- a_{21}\begin{vmatrix} a_{12} & a_{13} \\ a_{32} & a_{33} \end{vmatrix}
+ a_{31}\begin{vmatrix} a_{12} & a_{13} \\ a_{22} & a_{23} \end{vmatrix}.
$$

Expanding completely gives

$$
\det A = a_{11}a_{22}a_{33} - a_{11}a_{32}a_{23} + a_{21}a_{32}a_{13} - a_{21}a_{12}a_{33} + a_{31}a_{12}a_{23} - a_{31}a_{22}a_{13}.
$$

We now generalize this to order $n$: we express a determinant of order $n$ recursively through determinants of order $n-1$, which at the same time proves that a determinant function exists.

**Definition 5.5.1 (Minors and Cofactors)** Let $A$ be a square matrix of order $n$, $n \ge 2$. Denote by $A\binom{i}{j}$ the matrix of order $n-1$ obtained from $A$ by deleting row $i$ and column $j$. Then $M_{ij} = \det A\binom{i}{j}$ is called the **minor** of the entry $a_{ij}$, and $C_{ij} = (-1)^{i+j}M_{ij}$ is called the **cofactor** of $a_{ij}$.

The sign $(-1)^{i+j}$ comes from the antisymmetry of the determinant: moving row $i$ and column $j$ to the upper left corner takes $(i-1) + (j-1)$ interchanges of adjacent rows or columns. For example, for order two $\det A = a_{11}C_{11} + a_{21}C_{21}$, and for order three Example 5.5.1 is $\det A = a_{11}C_{11} + a_{21}C_{21} + a_{31}C_{31}$.

**Theorem 5.5.1 (Expansion along the First Column)** Let $A = [a_{ij}]$ be a square matrix of order $n$, $n \ge 2$. Then

$$
\delta(A) = a_{11}C_{11} + a_{21}C_{21} + \cdots + a_{n1}C_{n1} = \sum_{i=1}^n a_{i1}C_{i1}
$$

is a determinant function of order $n$. Hence a determinant function exists, and $\det A = \sum_i a_{i1}C_{i1}$, called the expansion of the determinant along the first column.

**Proof** We use induction on $n$; the case $n = 2$ has been verified. Suppose a determinant function of order $n-1$ exists (so that the cofactors are meaningful and have all the properties of determinants). By Corollary 5.2.1, it suffices to verify that $\delta$ is multilinear and antisymmetric in the rows and normalized.

Multilinearity in the rows: take the first row as an example (the other rows are similar). Let the first row be $a_{1j} = ka_{1j}' + \ell a_{1j}''$ ($j = 1, \dots, n$), and let $A', A''$ be the matrices obtained by replacing the first row with $[a_{1j}']$ and $[a_{1j}'']$ respectively. For $i \ne 1$, the submatrix belonging to $C_{i1}$ contains the first row (without its first entry), so by the induction hypothesis $C_{i1} = kC_{i1}' + \ell C_{i1}''$; and $C_{11} = C_{11}' = C_{11}''$. Hence

$$
\delta(A) = (ka_{11}' + \ell a_{11}'')C_{11} + \sum_{i=2}^n a_{i1}(kC_{i1}' + \ell C_{i1}'') = k\delta(A') + \ell\delta(A'').
$$

Antisymmetry in the rows: given multilinearity in the rows, this is equivalent to "two equal rows give zero". Suppose rows $p$ and $q$ of $A$ are equal ($p < q$). For $i \ne p, q$, $A\binom{i}{1}$ has two equal rows, so $C_{i1} = 0$. Moreover $a_{p1} = a_{q1}$, and $A\binom{p}{1}$ and $A\binom{q}{1}$ differ only by moving one row past $q - p - 1$ rows, so $M_{p1} = (-1)^{q-p-1}M_{q1}$. Hence

$$
a_{p1}C_{p1} + a_{q1}C_{q1} = a_{p1}\left((-1)^{p+1}(-1)^{q-p-1} + (-1)^{q+1}\right)M_{q1} = a_{p1}\left((-1)^{q} + (-1)^{q+1}\right)M_{q1} = 0.
$$

Normalization: $\delta(I_n) = 1 \cdot C_{11} = \det I_{n-1} = 1$. $\square$

### 5.5.2. Expansion along Any Row or Column

**Theorem 5.5.2** A determinant can be expanded along any column or any row:

1. expansion along column $j$: $\det A = a_{1j}C_{1j} + a_{2j}C_{2j} + \cdots + a_{nj}C_{nj} = \sum_{i=1}^n a_{ij}C_{ij}$;
2. expansion along row $i$: $\det A = a_{i1}C_{i1} + a_{i2}C_{i2} + \cdots + a_{in}C_{in} = \sum_{j=1}^n a_{ij}C_{ij}$.

**Proof** 1. Moving column $j$ to the far left by $j-1$ interchanges of adjacent columns gives $A' = [\boldsymbol{a}_j\ \boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_{j-1}\ \boldsymbol{a}_{j+1}\ \cdots\ \boldsymbol{a}_n]$ with $\det A = (-1)^{j-1}\det A'$. $A'$ and $A$ satisfy $a_{i1}' = a_{ij}$, $M_{i1}' = M_{ij}$ and $C_{i1}' = (-1)^{1-j}C_{ij}$, and expanding $A'$ along its first column gives the result. 2. Expand $A^{\mathsf T}$ along column $i$ and use $\det A^{\mathsf T} = \det A$. $\square$

An expansion turns one determinant of order $n$ into $n$ determinants of order $n-1$; when some row or column contains many zeros, expanding along it simplifies the computation considerably.

**Example 5.5.2** Compute the determinant of the orthogonal matrix $Q = \begin{bmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & -\frac{2}{\sqrt{6}} & 0 \end{bmatrix}$ from Example 4.3.2.

The third column contains a zero, so we expand along it:

$$
\det Q = \frac{1}{\sqrt{2}}\begin{vmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & -\frac{2}{\sqrt{6}} \end{vmatrix} + \frac{1}{\sqrt{2}}\begin{vmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & -\frac{2}{\sqrt{6}} \end{vmatrix} = \sqrt{2}\cdot\left(-\frac{3}{\sqrt{18}}\right) = -1.
$$

(The sign of the first term is $(-1)^{1+3} = 1$, and the coefficient of the second is $(-1)^{2+3}\cdot\left(-\frac{1}{\sqrt{2}}\right) = \frac{1}{\sqrt{2}}$.) $\det Q = -1$ shows that this orthogonal transformation reverses orientation, consistent with $\det Q = \pm 1$.

## 5.6. Applications of Cofactors

### 5.6.1. Cofactor Vectors

**Proposition 5.6.1** Let $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$, and let $\boldsymbol{c}_j = [C_{1j}\ C_{2j}\ \cdots\ C_{nj}]^{\mathsf T}$ be the vector of cofactors of the entries in column $j$. Then

$$
\boldsymbol{a}_{j'}^{\mathsf T}\boldsymbol{c}_j = \begin{cases} \det A, & j' = j, \\ 0, & j' \ne j. \end{cases}
$$

The analogous statement holds for the vector of cofactors of a row.

**Proof** For $j' = j$, $\boldsymbol{a}_j^{\mathsf T}\boldsymbol{c}_j$ is the expansion of $\det A$ along column $j$. For $j' \ne j$, replace column $j$ of $A$ by $\boldsymbol{a}_{j'}$; the cofactors of column $j$ of the new matrix are still $\boldsymbol{c}_j$, so its expansion along column $j$ is $\boldsymbol{a}_{j'}^{\mathsf T}\boldsymbol{c}_j$; but the new matrix has two equal columns, so its determinant is zero. $\square$

Geometric meaning: $\boldsymbol{a}_{j'} \perp \boldsymbol{c}_j$ for $j' \ne j$, so $\boldsymbol{c}_j$ is a normal vector to the "base" spanned by the other $n-1$ columns. The signed length $\boldsymbol{a}_j^{\mathsf T}\boldsymbol{c}_j/\|\boldsymbol{c}_j\|$ of the projection of $\boldsymbol{a}_j$ onto the direction $\boldsymbol{c}_j$ is the height of the parallelepiped, and

$$
\det A = \boldsymbol{a}_j^{\mathsf T}\boldsymbol{c}_j = \frac{\boldsymbol{a}_j^{\mathsf T}\boldsymbol{c}_j}{\|\boldsymbol{c}_j\|} \cdot \|\boldsymbol{c}_j\|,
$$

that is, "volume = height × base area", so $\|\boldsymbol{c}_j\|$ is the area of the base. For $n = 3$, $\boldsymbol{c}_3$ is exactly the cross product of $\boldsymbol{a}_1$ and $\boldsymbol{a}_2$.

### 5.6.2. The Adjugate Matrix and the Inverse Formula

**Definition 5.6.1 (Adjugate Matrix)** For a square matrix $A = [a_{ij}]$ of order $n$, the matrix $C = [C_{ij}]$ whose $(i, j)$ entry is the cofactor $C_{ij}$ of $a_{ij}$ is called the cofactor matrix of $A$, and its transpose $C^{\mathsf T}$ is called the **adjugate matrix** of $A$, written $\operatorname{adj}A$.

$C^{\mathsf T}$ is also called the complementary matrix. Note that it is a different concept from the adjoint (conjugate transpose) of a linear transformation in [Chapter 12](/2.1.12).

**Theorem 5.6.1 (Inverse Formula)** For every square matrix $A$ of order $n$, $C^{\mathsf T}A = AC^{\mathsf T} = \det(A)I_n$. In particular, if $A$ is invertible, then

$$
A^{-1} = \frac{1}{\det A}C^{\mathsf T} = \frac{1}{\det A}\operatorname{adj}A.
$$

**Proof** The $(i, j)$ entry of $C^{\mathsf T}A$ is $\boldsymbol{c}_i^{\mathsf T}\boldsymbol{a}_j$, which by Proposition 5.6.1 is $\det A$ for $i = j$ and $0$ for $i \ne j$. The same argument with rows gives $AC^{\mathsf T} = \det(A)I_n$. $\square$

For example, in order two, $\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \dfrac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$. The inverse formula shows that every entry of $A^{-1}$ is a rational function of the entries of $A$ and hence depends continuously on $A$; but it requires $n^2$ determinants of order $n-1$, and in practice inverses should be computed by the Gauss–Jordan elimination of Chapter 2.

### 5.6.3. Cramer's Rule

**Theorem 5.6.2 (Cramer's Rule)** Let $A$ be a square matrix of order $n$. The linear system $A\boldsymbol{x} = \boldsymbol{b}$ has a unique solution if and only if $\det A \ne 0$, and in that case the solution is

$$
x_1 = \frac{\det B_1}{\det A}, \quad x_2 = \frac{\det B_2}{\det A}, \quad \dots, \quad x_n = \frac{\det B_n}{\det A},
$$

where $B_j$ is the matrix obtained from $A$ by replacing column $j$ with $\boldsymbol{b}$.

**Proof** $A\boldsymbol{x} = \boldsymbol{b}$ has a unique solution if and only if $A$ is invertible, that is, $\det A \ne 0$. Write the system as $x_1\boldsymbol{a}_1 + \cdots + x_n\boldsymbol{a}_n = \boldsymbol{b}$ and take the inner product of both sides with $\boldsymbol{c}_i$; by Proposition 5.6.1, $x_i\boldsymbol{c}_i^{\mathsf T}\boldsymbol{a}_i = \boldsymbol{c}_i^{\mathsf T}\boldsymbol{b}$. Here $\boldsymbol{c}_i^{\mathsf T}\boldsymbol{a}_i$ and $\boldsymbol{c}_i^{\mathsf T}\boldsymbol{b}$ are the expansions of $\det A$ and $\det B_i$ along column $i$, so $x_i = \det B_i/\det A$. $\square$

Geometric meaning: $x_i$ is the ratio of the signed volume of the parallelepiped with edges $\boldsymbol{b}$ and $\boldsymbol{a}_j$ ($j \ne i$) to that of the parallelepiped with edges $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$. The two parallelepipeds share the same base (with edges $\boldsymbol{a}_j$, $j \ne i$); since $\boldsymbol{b} - x_i\boldsymbol{a}_i = \sum_{j \ne i}x_j\boldsymbol{a}_j$ lies in the base, $\boldsymbol{b}$ and $x_i\boldsymbol{a}_i$ have the same projection onto the normal vector $\boldsymbol{c}_i$ of the base, so $x_i$ is the ratio of the two heights.

Like the inverse formula, Cramer's rule is a theoretical tool (for instance, it shows that the solution depends continuously on the data, and it is handy for hand computation in orders two and three); it should not be used to solve linear systems numerically.

## 5.7. Permutations and the Complete Expansion

### 5.7.1. The Complete Expansion

**Example 5.7.1** Expand a determinant of order three by multilinearity in every column:

$$
\det A = \delta\left(\sum_{i} a_{i1}\boldsymbol{e}_i,\ \sum_{i} a_{i2}\boldsymbol{e}_i,\ \sum_{i} a_{i3}\boldsymbol{e}_i\right) = \sum_{\sigma_1, \sigma_2, \sigma_3} a_{\sigma_11}a_{\sigma_22}a_{\sigma_33}\,\delta(\boldsymbol{e}_{\sigma_1}, \boldsymbol{e}_{\sigma_2}, \boldsymbol{e}_{\sigma_3}).
$$

This is a sum of $3^3 = 27$ terms, but only the $3! = 6$ terms with $\sigma_1, \sigma_2, \sigma_3$ pairwise distinct are nonzero. Each corresponding matrix $[\boldsymbol{e}_{\sigma_1}\ \boldsymbol{e}_{\sigma_2}\ \boldsymbol{e}_{\sigma_3}]$ is a **permutation matrix** with determinant $\pm 1$, and the result agrees with Example 5.5.1.

### 5.7.2. Permutations and Their Signs

**Definition 5.7.1 (Permutation)** An arrangement $\sigma_1, \sigma_2, \dots, \sigma_n$ of $1, 2, \dots, n$ in some order is called a permutation of $n$ elements, written $\sigma$. Swapping the positions of two numbers in a permutation is called a transposition. If $\sigma$ can be turned into $1, 2, \dots, n$ by an odd number of transpositions, it is called an odd permutation and its sign is defined as $\operatorname{sgn}(\sigma) = -1$; if it can be turned into $1, 2, \dots, n$ by an even number of transpositions, it is called an even permutation and $\operatorname{sgn}(\sigma) = 1$.

A permutation $\sigma$ is the map $i \mapsto \sigma_i$, that is, a **permutation** in the sense of 1.3.2; odd and even permutations correspond to **odd permutations** and **even permutations** there. Permutations correspond one-to-one to permutation matrices via $\sigma \mapsto P_\sigma = [\boldsymbol{e}_{\sigma_1}\ \cdots\ \boldsymbol{e}_{\sigma_n}]$; a transposition corresponds to interchanging two columns, so $\det P_\sigma = \operatorname{sgn}(\sigma)$.

This also answers the question of whether a permutation can be both odd and even: it cannot. If $\sigma$ becomes the identity permutation after $s$ transpositions, then $P_\sigma$ becomes $I_n$ after $s$ column interchanges, so $\det P_\sigma = (-1)^s$; since $\det P_\sigma$ is uniquely determined (Theorem 5.3.1), the parity of $s$ is determined by $\sigma$. For $n \ge 2$, fixing a transposition $\tau$, the map $\sigma \mapsto \tau\sigma$ is a bijection between odd and even permutations, so there are $n!/2$ of each.

### 5.7.3. The Complete Expansion Theorem

**Theorem 5.7.1 (Complete Expansion of the Determinant)** For a square matrix $A = [a_{ij}]$ of order $n$,

$$
\det A = \sum_{\sigma} \operatorname{sgn}(\sigma)\,a_{\sigma_11}a_{\sigma_22}\cdots a_{\sigma_nn} = \sum_{\sigma} \operatorname{sgn}(\sigma)\,a_{1\sigma_1}a_{2\sigma_2}\cdots a_{n\sigma_n},
$$

where the sum runs over all $n!$ permutations of $n$ elements.

**Proof** As in Example 5.7.1, expand by multilinearity in every column:

$$
\det A = \sum_{\sigma_1, \dots, \sigma_n = 1}^n a_{\sigma_11}\cdots a_{\sigma_nn}\,\delta(\boldsymbol{e}_{\sigma_1}, \dots, \boldsymbol{e}_{\sigma_n}).
$$

If two of $\sigma_1, \dots, \sigma_n$ coincide, $\delta(\boldsymbol{e}_{\sigma_1}, \dots, \boldsymbol{e}_{\sigma_n})$ has two equal columns and vanishes; otherwise $\sigma$ is a permutation and $\delta(\boldsymbol{e}_{\sigma_1}, \dots, \boldsymbol{e}_{\sigma_n}) = \det P_\sigma = \operatorname{sgn}(\sigma)$. This gives the first equality. Applying the first equality to $\det A^{\mathsf T} = \det A$ gives the second. $\square$

This proof uses only the axioms, so it gives an independent proof of uniqueness; conversely, verifying directly that the right-hand side satisfies the three axioms also proves existence.

The complete expansion has $n!$ terms, each requiring $n-1$ multiplications, for a total of $(n-1)\cdot n!$; the recursive algorithm of expansion along rows or columns also needs about $(\mathrm{e}-1)\cdot n!$ multiplications. Both grow faster than any exponential in $n$, whereas Gaussian elimination (Algorithm 5.4.1) needs only about $n^3/3$ multiplications. For $n = 20$, the complete expansion takes about $5 \times 10^{19}$ multiplications and elimination only about $3000$. Determinants should therefore generally not be computed by the complete expansion or by expansion along rows or columns; the value of the complete expansion lies in theory, for example in showing that $\det A$ is a polynomial in the entries of the matrix (hence a continuous function), and in deriving the degree and coefficients of the characteristic polynomial in Chapter 6.

![Number of multiplications needed to compute a determinant of order n (logarithmic vertical axis): the complete expansion and expansion along rows or columns grow like n!, Gaussian elimination only like n³](./plots/determinant-cost.py)

## Summary {#summary}

The theory of determinants can be summarized as: "three axioms → properties and uniqueness → expansion gives existence → elimination gives computation".

| Concept or result | Content | Location |
|---|---|---|
| Determinant | the function that is multilinear and antisymmetric in the columns and normalized; exists and is unique | Definition 5.1.1, Theorem 5.3.1, Theorem 5.5.1 |
| Vanishing on dependent columns | two equal columns, not of full rank, a zero row or column ⇒ $\det A = 0$ | Property 5.1.1 |
| Elementary matrices | $\det P_{ij} = -1$, $\det E_{ii;k} = k$, $\det E_{ji;k} = 1$ | Proposition 5.2.1 |
| Rules | $\det A \ne 0 \iff A$ invertible; $\det(AB) = \det A\det B$; $\det A^{\mathsf T} = \det A$; $\det A^{-1} = 1/\det A$ | Theorem 5.2.1 |
| Geometric meaning | signed volume; volume scaling factor of a linear transformation | Section 5.3 |
| Special matrices | diagonal, triangular: product of the diagonal entries; orthogonal: $\pm 1$; block triangular: $\det A\det B$ | Example 5.4.1 |
| Vandermonde determinant | $\prod_{j<i}(\lambda_i - \lambda_j)$; the interpolating polynomial exists and is unique | Theorem 5.4.1 |
| Expansion along a row or column | $\det A = \sum_i a_{ij}C_{ij} = \sum_j a_{ij}C_{ij}$ | Theorem 5.5.2 |
| Cofactor vectors | $\boldsymbol{a}_{j'}^{\mathsf T}\boldsymbol{c}_j = \delta_{jj'}\det A$; normal to the base, with length equal to the base area | Proposition 5.6.1 |
| Inverse formula and Cramer's rule | $A^{-1} = C^{\mathsf T}/\det A$; $x_j = \det B_j/\det A$ | Theorem 5.6.1, Theorem 5.6.2 |
| Complete expansion | $\det A = \sum_\sigma \operatorname{sgn}(\sigma)\prod_i a_{\sigma_ii}$ | Theorem 5.7.1 |

| Method | Cost | When to use |
|---|---|---|
| Gaussian elimination (Algorithm 5.4.1) | about $\frac{2}{3}n^3$ floating-point operations | the standard method for general matrices |
| Expansion along a row or column | about $(\mathrm{e}-1)\cdot n!$ multiplications | hand computation when a row or column has many zeros |
| Complete expansion | $(n-1)\cdot n!$ multiplications | theoretical derivations; hand computation in orders two and three |
