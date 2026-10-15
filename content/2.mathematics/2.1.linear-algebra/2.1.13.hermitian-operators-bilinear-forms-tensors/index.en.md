---
title: Hermitian Operators, Bilinear Forms and Tensors
source_hash: 45d95f7f1934
---

The [previous chapter](/2.1.12) proved that the normal operators are exactly the operators that can be diagonalized in an orthonormal basis. There is a clear correspondence between normal matrices and complex numbers: the normal matrices whose eigenvalues are all real (the Hermitian matrices) play the role of real numbers, and those whose eigenvalues have modulus $1$ (the unitary matrices) play the role of unit complex numbers. Following this analogy, the first half of the chapter generalizes the polar form $z = r\mathrm{e}^{\mathrm{i}\theta}$ of a complex number to the polar decomposition $A = R\mathrm{e}^{\mathrm{i}M}$ of a matrix; it then carries the real **quadratic forms**, **congruence of matrices**, **Sylvester's law of inertia** and positive definite matrices of [Chapter 7](/2.1.7) over to the complex field, obtaining Hermitian forms and \*-congruence; finally it states the **singular value decomposition** of complex matrices and explains its relation to the polar decomposition. Most proofs are the same as in the real case and are only sketched.

The second half takes a different point of view. The inner product $(a, b), (c, d) \mapsto ac + bd$ and the oriented area $(a, b), (c, d) \mapsto ad - bc$ in the plane (a $2 \times 2$ **determinant**) are both maps "two vectors $\mapsto$ one number" that are linear in each argument. This chapter studies such maps, the bilinear forms, on general vector spaces; under a change of basis they transform as $P^{\mathsf T}GP$, which is the origin of congruence. Symmetric nondegenerate bilinear forms give "generalized inner products" (such as the Lorentz form of special relativity), and skew-symmetric ones give symplectic spaces; the transformations preserving them form the orthogonal and symplectic groups. Finally, the **dual space** of [Chapter 8](/2.1.8) is used to introduce tensors: from numbers (order $0$) to linear functionals (order $1$), bilinear forms (order $2$) and multilinear forms.

The chapter again follows the approach of "reducing to standard problems": bringing a Hermitian form to normal form is unitary diagonalization; testing positive definiteness reduces to eigenvalues, leading principal minors or a single Cholesky decomposition, at very different costs; classifying bilinear forms means finding the normal form of the representing matrix under congruence, and a change of basis only requires computing $P^{\mathsf T}GP$.

## 13.1. Self-Adjoint Operators and Hermitian Matrices

**Definition 13.1.1** Let $V$ be an inner product space and $T\colon V \to V$ a linear transformation. If the adjoint $T^*$ of $T$ exists and $T = T^*$, that is, $\langle T\alpha, \beta \rangle = \langle \alpha, T\beta \rangle$ for all $\alpha, \beta$, then $T$ is called a **self-adjoint operator**. A self-adjoint operator on a Euclidean space is called a symmetric transformation, and a self-adjoint operator on a unitary space is called a **Hermitian operator**.

**Definition 13.1.2** Let $A \in \mathbb{C}^{n\times n}$. If $A^{\mathsf H} = A$, then $A$ is called a **Hermitian matrix**; if $A^{\mathsf H} = -A$, then $A$ is called a **skew-Hermitian matrix**.

By Theorem 12.6.2, $T$ is a Hermitian operator (symmetric transformation) if and only if its matrix with respect to an orthonormal basis is a Hermitian matrix (real symmetric matrix). The diagonal entries of a Hermitian matrix satisfy $a_{ii} = \bar a_{ii}$, so they are all real. Hermitian operators are obviously normal.

**Example 13.1.1** On $\mathbb{R}^n$, $\boldsymbol{x} \mapsto A\boldsymbol{x}$ with $A$ real symmetric is a symmetric transformation. On $\mathbb{C}^2$, $\boldsymbol{x} \mapsto \begin{bmatrix} 2 & 1 + \mathrm{i} \\ 1 - \mathrm{i} & 3 \end{bmatrix}\boldsymbol{x}$ is a Hermitian operator: its matrix with respect to the orthonormal basis $\boldsymbol{e}_1, \boldsymbol{e}_2$ is $A$, and $A^{\mathsf H} = A$.

**Theorem 13.1.1** Let $A$ be a Hermitian matrix.

1. The eigenvalues of $A$ are all real;
2. there is a unitary matrix $U$ with $U^{\mathsf H}AU = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$, $\lambda_i \in \mathbb{R}$;
3. conversely, a normal matrix whose eigenvalues are all real is Hermitian;
4. the eigenvalues of a skew-Hermitian matrix are purely imaginary or zero; $A$ is Hermitian $\Leftrightarrow$ $\mathrm{i}A$ is skew-Hermitian.

**Proof** 1: Let $A\boldsymbol{\alpha} = \lambda\boldsymbol{\alpha}$ with $\boldsymbol{\alpha} \ne \boldsymbol{0}$. Then $\lambda\langle \boldsymbol{\alpha}, \boldsymbol{\alpha} \rangle = \langle A\boldsymbol{\alpha}, \boldsymbol{\alpha} \rangle = \langle \boldsymbol{\alpha}, A\boldsymbol{\alpha} \rangle = \bar\lambda\langle \boldsymbol{\alpha}, \boldsymbol{\alpha} \rangle$, so $\lambda = \bar\lambda$. 2: $A$ is normal; apply the **spectral theorem** and 1. 3: $A = U\Lambda U^{\mathsf H}$ with $\Lambda$ real gives $A^{\mathsf H} = U\bar\Lambda U^{\mathsf H} = A$. 4: As in 1, $\lambda = -\bar\lambda$. $\square$

**Example 13.1.2** Orthogonal projections are self-adjoint operators. Let $V = W \oplus W^\perp$, $v = v_1 + v_2$ and $w = w_1 + w_2$ ($v_1, w_1 \in W$, $v_2, w_2 \in W^\perp$), and $Tv = v_1$. Then

$$
\langle Tv, w \rangle = \langle v_1, w_1 + w_2 \rangle = \langle v_1, w_1 \rangle = \langle v_1 + v_2, w_1 \rangle = \langle v, Tw \rangle.
$$

**Example 13.1.3** Let $V = \operatorname{span}\{1, \cos x, \sin x\}$ with $\langle f, g \rangle = \int_0^{2\pi}f(x)g(x)\,\mathrm{d}x$, and $D\colon f \mapsto f'$. The functions $e_1 = \frac{1}{\sqrt{2\pi}}$, $e_2 = \frac{\cos x}{\sqrt\pi}$, $e_3 = \frac{\sin x}{\sqrt\pi}$ form an orthonormal basis, and $De_1 = 0$, $De_2 = -e_3$, $De_3 = e_2$, so

$$
(De_1, De_2, De_3) = (e_1, e_2, e_3)A, \qquad A = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{bmatrix}, \qquad A^{\mathsf T} = -A.
$$

Hence $D^* = -D$: $D$ is not self-adjoint but skew-adjoint, with eigenvalues $0, \pm \mathrm{i}$ (corresponding to the complex functions $1, \mathrm{e}^{\pm \mathrm{i}x}$). The underlying reason is integration by parts: for periodic functions, $\langle f', g \rangle = -\langle f, g' \rangle$. Correspondingly, $-D^2 = -\frac{\mathrm{d}^2}{\mathrm{d}x^2}$ is self-adjoint, which is the starting point of the Fourier series method in partial differential equations.

Every complex square matrix can be written uniquely as $A = H + K$, where $H = \frac12(A + A^{\mathsf H})$ is Hermitian and $K = \frac12(A - A^{\mathsf H})$ is skew-Hermitian; this is the analogue of splitting $z = a + b\mathrm{i}$ into real and imaginary parts. Expanding $AA^{\mathsf H}$ and $A^{\mathsf H}A$ shows that $A$ is normal $\Leftrightarrow$ $HK = KH$.

## 13.2. The Polar Decomposition

The correspondence between complex numbers and matrices is summarized in the table below (the complex number $z = a + b\mathrm{i}$ itself corresponds to the real normal matrix $\begin{bmatrix} a & -b \\ b & a \end{bmatrix}$ of order 2, [Chapter 9](/2.1.9)).

| Complex numbers | Matrices |
|---|---|
| **Complex conjugate** $\bar z$ | **Conjugate transpose** $A^{\mathsf H}$ |
| $z\bar z = \bar zz$ | Normal: $AA^{\mathsf H} = A^{\mathsf H}A$ |
| Real number $z = \bar z$ | Hermitian matrix $A = A^{\mathsf H}$ |
| Purely imaginary number $z = -\bar z$ | Skew-Hermitian matrix $A = -A^{\mathsf H}$ |
| $\lvert z\rvert = 1$, i.e., $\bar zz = 1$ | Unitary matrix $A^{\mathsf H}A = I$ |
| $r \ge 0$ | Positive semidefinite Hermitian matrix (eigenvalues $\ge 0$) |
| $\mathrm{e}^{\mathrm{i}\theta}$, $\theta$ real | $\mathrm{e}^{\mathrm{i}M}$, $M$ Hermitian (Example 12.3.3) |
| Polar form $z = r\mathrm{e}^{\mathrm{i}\theta}$ | $A = R\mathrm{e}^{\mathrm{i}M}$ |

**Theorem 13.2.1** Let $A$ be a normal matrix of order $n$. Then there are a positive semidefinite Hermitian matrix $R$ and a Hermitian matrix $M$ with $A = R\mathrm{e}^{\mathrm{i}M}$ and $RM = MR$.

**Proof** By the spectral theorem there is a unitary matrix $U$ with $U^{\mathsf H}AU = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$. Write each eigenvalue in **polar form** $\lambda_j = r_j\mathrm{e}^{\mathrm{i}\theta_j}$ with $r_j \ge 0$ and $\theta_j \in \mathbb{R}$, and let

$$
R = U\operatorname{diag}(r_1, \dots, r_n)U^{\mathsf H}, \qquad M = U\operatorname{diag}(\theta_1, \dots, \theta_n)U^{\mathsf H}.
$$

$R$ is a Hermitian matrix with nonnegative eigenvalues and $M$ is Hermitian; both are diagonalized by the same $U$, so they commute. By the properties of matrix functions, $\mathrm{e}^{\mathrm{i}M} = U\operatorname{diag}(\mathrm{e}^{\mathrm{i}\theta_1}, \dots, \mathrm{e}^{\mathrm{i}\theta_n})U^{\mathsf H}$, and therefore $R\mathrm{e}^{\mathrm{i}M} = U\operatorname{diag}(r_j\mathrm{e}^{\mathrm{i}\theta_j})U^{\mathsf H} = A$. $\square$

The factorization $A = R\mathrm{e}^{\mathrm{i}M}$ is called the *polar decomposition* of the normal matrix $A$. Since $A^{\mathsf H}A = \mathrm{e}^{-\mathrm{i}M}R^2\mathrm{e}^{\mathrm{i}M} = R^2$, the factor $R = (A^{\mathsf H}A)^{1/2}$ is uniquely determined by $A$ (taking the positive semidefinite square root); $M$ is not unique: each $\theta_j$ may be changed by an integer multiple of $2\pi$, and when $A$ is singular the arguments of the zero eigenvalues are arbitrary. This answers the question raised at the beginning of [Chapter 11](/2.1.11).

**Example 13.2.1** The matrix $A = \begin{bmatrix} r\cos\theta & -r\sin\theta \\ r\sin\theta & r\cos\theta \end{bmatrix}$ corresponding to the complex number $z = r\mathrm{e}^{\mathrm{i}\theta}$ has the polar decomposition $R = rI$, $M = \begin{bmatrix} 0 & \mathrm{i}\theta \\ -\mathrm{i}\theta & 0 \end{bmatrix}$: $M$ is Hermitian, $\mathrm{i}M = \theta\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$, and $\mathrm{e}^{\mathrm{i}M}$ is the rotation matrix through the angle $\theta$ (Example 11.8.1). Here the polar decomposition of the matrix and the polar form of the complex number coincide completely.

A general square matrix (not necessarily normal) also has a polar decomposition $A = UP$ ($U$ unitary, $P$ positive semidefinite Hermitian), but $U$ and $P$ need not commute; see Section 13.5.

## 13.3. Hermitian Forms

**Definition 13.3.1** Let $a_{ij} = \bar a_{ji}$ ($1 \le i, j \le n$). The function $f(x_1, \dots, x_n) = \sum_{i,j=1}^n a_{ij}\bar x_ix_j$ of $n$ complex variables is called a **Hermitian form** in $n$ variables. Writing $A = (a_{ij})$, the matrix $A$ is Hermitian and $f = \boldsymbol{x}^{\mathsf H}A\boldsymbol{x}$; $A$ is called the matrix of $f$.

**Example 13.3.1** The matrix of $f(x_1, x_2) = \mathrm{i}\bar x_1x_2 - \mathrm{i}\bar x_2x_1$ is $\begin{bmatrix} 0 & \mathrm{i} \\ -\mathrm{i} & 0 \end{bmatrix}$. For $\boldsymbol{x} = (1, \mathrm{i})^{\mathsf T}$, $f = \mathrm{i} \cdot \mathrm{i} - \mathrm{i} \cdot (-\mathrm{i}) \cdot 1 = -2$.

**Property 13.3.1**

1. Hermitian forms take real values: $\bar{f} = \overline{\boldsymbol{x}^{\mathsf H}A\boldsymbol{x}} = (\boldsymbol{x}^{\mathsf H}A\boldsymbol{x})^{\mathsf H} = \boldsymbol{x}^{\mathsf H}A^{\mathsf H}\boldsymbol{x} = f$.
2. Hermitian matrices of order $n$ correspond one-to-one to Hermitian forms in $n$ variables: if $\boldsymbol{x}^{\mathsf H}C\boldsymbol{x} = 0$ for all $\boldsymbol{x} \in \mathbb{C}^n$, then $C = O$. Taking $\boldsymbol{x} = \boldsymbol{e}_j$ gives $c_{jj} = 0$; taking $\boldsymbol{x} = \boldsymbol{e}_j + \boldsymbol{e}_k$ and $\boldsymbol{x} = \boldsymbol{e}_j + \mathrm{i}\boldsymbol{e}_k$ gives $c_{jk} + c_{kj} = 0$ and $\mathrm{i}(c_{jk} - c_{kj}) = 0$, so $c_{jk} = 0$.

Under an invertible change of variables $\boldsymbol{x} = P\boldsymbol{y}$, $f = \boldsymbol{x}^{\mathsf H}A\boldsymbol{x} = \boldsymbol{y}^{\mathsf H}(P^{\mathsf H}AP)\boldsymbol{y}$, so the matrix changes according to the following relation.

**Definition 13.3.2** Let $A, B \in \mathbb{C}^{n\times n}$. If there is an invertible matrix $P$ with $P^{\mathsf H}AP = B$, then $A$ and $B$ are said to be related by **\*-congruence**.

\*-congruence is an equivalence relation; it is the complex version of the congruence $P^{\mathsf T}AP$ of real matrices. Since unitary matrices satisfy $P^{\mathsf H} = P^{-1}$, unitary similarity is both a similarity and a \*-congruence, so the standard way to reduce a Hermitian form is unitary diagonalization.

**Theorem 13.3.1 (Sylvester's Law of Inertia)** Every Hermitian form $f = \boldsymbol{x}^{\mathsf H}A\boldsymbol{x}$ can be brought by an invertible linear substitution $\boldsymbol{x} = C\boldsymbol{z}$ to the normal form

$$
f = \bar z_1z_1 + \cdots + \bar z_pz_p - \bar z_{p+1}z_{p+1} - \cdots - \bar z_rz_r,
$$

where $r = \operatorname{rank}(A)$, the positive index of inertia $p$ equals the number of positive eigenvalues of $A$, and $p$ and $r$ are uniquely determined by $f$. In matrix form: a Hermitian matrix is \*-congruent to $\operatorname{diag}(I_p, -I_{r-p}, O)$, and two Hermitian matrices are \*-congruent if and only if they have the same rank and the same positive index of inertia.

**Proof** Existence: by Theorem 13.1.1 there is a unitary $U$ with $U^{\mathsf H}AU = \operatorname{diag}(d_1, \dots, d_r, 0, \dots, 0)$, $d_1, \dots, d_p > 0 > d_{p+1}, \dots, d_r$. Let $D = \operatorname{diag}(|d_1|^{-1/2}, \dots, |d_r|^{-1/2}, 1, \dots, 1)$ and $C = UD$. The proof of uniqueness is the same as for real symmetric matrices (Theorem 7.3.3): if $f$ had two normal forms with different positive indices of inertia, the dimension formula would produce a nonzero vector at which $f > 0$ in one normal form and $f \le 0$ in the other, a contradiction. $\square$

The numbers $p$ and $r - p$ are called the positive and negative indices of inertia of $f$; together they form the **inertia** of $f$.

**Example 13.3.2** Let $A = \begin{bmatrix} 1 & \mathrm{i} & 1 \\ -\mathrm{i} & 0 & 0 \\ 1 & 0 & 0 \end{bmatrix}$; find an invertible $C$ that brings $f = \boldsymbol{x}^{\mathsf H}A\boldsymbol{x}$ to normal form.

1. $\det(\lambda I - A) = (\lambda - 2)(\lambda + 1)\lambda$, with eigenvalues $2, -1, 0$. The corresponding eigenvectors are $(2, -\mathrm{i}, 1)^{\mathsf T}$, $(-1, -\mathrm{i}, 1)^{\mathsf T}$, $(0, \mathrm{i}, 1)^{\mathsf T}$; they belong to distinct eigenvalues and are automatically orthogonal, and normalizing gives
$$
\boldsymbol{q}_1 = \tfrac{1}{\sqrt6}(2, -\mathrm{i}, 1)^{\mathsf T}, \qquad \boldsymbol{q}_2 = \tfrac{1}{\sqrt3}(-1, -\mathrm{i}, 1)^{\mathsf T}, \qquad \boldsymbol{q}_3 = \tfrac{1}{\sqrt2}(0, \mathrm{i}, 1)^{\mathsf T}.
$$
2. $P = (\boldsymbol{q}_1, \boldsymbol{q}_2, \boldsymbol{q}_3)$ is unitary and $P^{\mathsf H}AP = \operatorname{diag}(2, -1, 0)$. Setting $\boldsymbol{x} = P\boldsymbol{y}$ gives $f = 2\bar y_1y_1 - \bar y_2y_2$.
3. Setting $\boldsymbol{y} = D\boldsymbol{z}$ with $D = \operatorname{diag}(\frac{1}{\sqrt2}, 1, 1)$ gives $f = \bar z_1z_1 - \bar z_2z_2$. Thus $C = PD$, $p = 1$ and $r = 2$.

## 13.4. Positive Definite Hermitian Matrices

**Definition 13.4.1 (Positive Definite Matrix)** Let $A$ be a Hermitian matrix of order $n$. If $\boldsymbol{x}^{\mathsf H}A\boldsymbol{x} > 0$ for all $\boldsymbol{x} \ne \boldsymbol{0}$, then $A$ is called a positive definite Hermitian matrix and $f = \boldsymbol{x}^{\mathsf H}A\boldsymbol{x}$ a positive definite Hermitian form; if $\boldsymbol{x}^{\mathsf H}A\boldsymbol{x} \ge 0$, then $A$ is called a positive semidefinite Hermitian matrix.

By the metric matrices of the [previous chapter](/2.1.12), inner products on $\mathbb{C}^n$ correspond one-to-one to positive definite Hermitian matrices $G$ of order $n$: $\langle \boldsymbol{\alpha}, \boldsymbol{\beta} \rangle = \boldsymbol{\alpha}^{\mathsf T}G\bar{\boldsymbol{\beta}}$. $G = I$ gives the standard inner product.

**Property 13.4.1** For every $A \in \mathbb{C}^{m \times n}$, $A^{\mathsf H}A$ and $AA^{\mathsf H}$ are positive semidefinite Hermitian matrices; if $A$ has full column rank, $A^{\mathsf H}A$ is positive definite, and if $A$ has full row rank, $AA^{\mathsf H}$ is positive definite.

**Proof** $\boldsymbol{x}^{\mathsf H}A^{\mathsf H}A\boldsymbol{x} = \|A\boldsymbol{x}\|^2 \ge 0$; if $A$ has full column rank, $\boldsymbol{x} \ne \boldsymbol{0} \Rightarrow A\boldsymbol{x} \ne \boldsymbol{0}$, and the inequality is strict. $\square$

**Theorem 13.4.1** Let $A$ be a Hermitian matrix of order $n$. The following are equivalent:

1. $A$ is positive definite;
2. all eigenvalues of $A$ are positive;
3. there is an invertible matrix $P$ with $A = P^{\mathsf H}P$;
4. $A$ is \*-congruent to $I_n$;
5. all **leading principal minors** of $A$ are positive;
6. there is a unique upper triangular matrix $R$ with positive real diagonal entries such that $A = R^{\mathsf H}R$ (the complex **Cholesky decomposition**).

**Proof** 1 $\Rightarrow$ 2: if $A\boldsymbol{\alpha} = \lambda\boldsymbol{\alpha}$, then $0 < \boldsymbol{\alpha}^{\mathsf H}A\boldsymbol{\alpha} = \lambda\|\boldsymbol{\alpha}\|^2$. 2 $\Rightarrow$ 3: $A = U\Lambda U^{\mathsf H} = (\Lambda^{1/2}U^{\mathsf H})^{\mathsf H}(\Lambda^{1/2}U^{\mathsf H})$. 3 $\Rightarrow$ 1: $\boldsymbol{x}^{\mathsf H}A\boldsymbol{x} = \|P\boldsymbol{x}\|^2 > 0$ ($\boldsymbol{x} \ne \boldsymbol{0}$). 3 $\Leftrightarrow$ 4: $A = P^{\mathsf H}IP$. 1 $\Rightarrow$ 5: the upper left submatrix $A_k$ of order $k$ is also positive definite (take $\boldsymbol{x}$ with its last $n - k$ components zero), so by 2, $\det A_k$ is a product of positive eigenvalues. 5 $\Rightarrow$ 6: nonzero leading principal minors guarantee that the **LU decomposition** exists and is unique, and the Hermitian property gives $A = LDL^{\mathsf H}$, where the diagonal entries of $D$ are ratios of consecutive leading principal minors and hence positive; let $R = D^{1/2}L^{\mathsf H}$. 6 $\Rightarrow$ 3 is clear. $\square$

The real Cholesky decomposition of [Chapter 7](/2.1.7) is written $A = LL^{\mathsf T}$, where $L = R^{\mathsf T}$ is lower triangular; the two are the same thing. The costs of these tests differ greatly: computing eigenvalues requires an iterative algorithm, and even for a Hermitian matrix it takes about $\frac43n^3$ operations just to find the eigenvalues; computing leading principal minors one by one via cofactor expansion is extremely expensive, whereas a single run of **Gaussian elimination** yields all of them as products of pivots; the Cholesky decomposition takes about $\frac13n^3$ operations (half of an LU decomposition), and it fails (a nonpositive pivot appears) if and only if $A$ is not positive definite. In practice, therefore, the standard way to test positive definiteness is to attempt a Cholesky decomposition.

The positive semidefinite case has similar results: $A$ is positive semidefinite $\Leftrightarrow$ all eigenvalues are nonnegative $\Leftrightarrow$ $A = C^{\mathsf H}C$ ($C$ not necessarily invertible) $\Leftrightarrow$ $A$ is \*-congruent to $\operatorname{diag}(I_r, O)$. However, nonnegative leading principal minors do not imply positive semidefiniteness: the leading principal minors of $\operatorname{diag}(0, -1)$ are $0, 0$, yet it is not positive semidefinite; the correct condition is that all principal minors (not just the leading ones) be nonnegative.

**Example 13.4.1** Let $A = \begin{bmatrix} 2 & 1 + \mathrm{i} \\ 1 - \mathrm{i} & 3 \end{bmatrix}$. Its leading principal minors are $2 > 0$ and $\det A = 6 - |1 + \mathrm{i}|^2 = 4 > 0$, so $A$ is positive definite (its eigenvalues are $1$ and $4$). Cholesky decomposition: $r_{11} = \sqrt2$, $r_{11}r_{12} = 1 + \mathrm{i} \Rightarrow r_{12} = \frac{1 + \mathrm{i}}{\sqrt2}$, $r_{22} = \sqrt{3 - |r_{12}|^2} = \sqrt2$, so

$$
A = R^{\mathsf H}R, \qquad R = \begin{bmatrix} \sqrt2 & \frac{1 + \mathrm{i}}{\sqrt2} \\ 0 & \sqrt2 \end{bmatrix}.
$$

## 13.5. The Singular Value Decomposition of Complex Matrices

[Chapter 7](/2.1.7) proved the singular value decomposition for real matrices (Theorem 7.4.1) and discussed the **Moore–Penrose pseudoinverse** and low-rank approximation. Replacing the transpose by the conjugate transpose, the proof carries over word for word.

**Theorem 13.5.1 (Singular Value Decomposition)** Let $A \in \mathbb{C}^{m \times n}$ with $\operatorname{rank}(A) = r$. Then there are a unitary matrix $U$ of order $m$ and a unitary matrix $V$ of order $n$ with

$$
A = U\Sigma V^{\mathsf H}, \qquad \Sigma = \begin{bmatrix} \operatorname{diag}(\sigma_1, \dots, \sigma_r) & O \\ O & O \end{bmatrix}_{m \times n}, \qquad \sigma_1 \ge \cdots \ge \sigma_r > 0.
$$

The $\sigma_i$ are the arithmetic square roots of the positive eigenvalues of $A^{\mathsf H}A$ and are called the **singular values** of $A$.

**Proof** $A^{\mathsf H}A$ is a positive semidefinite Hermitian matrix (Property 13.4.1), so by Theorem 13.1.1 there is a unitary $V = (\boldsymbol{v}_1, \dots, \boldsymbol{v}_n)$ with $V^{\mathsf H}A^{\mathsf H}AV = \operatorname{diag}(\sigma_1^2, \dots, \sigma_r^2, 0, \dots, 0)$. For $i > r$, $\|A\boldsymbol{v}_i\|^2 = 0$. Let $\boldsymbol{u}_i = \frac{1}{\sigma_i}A\boldsymbol{v}_i$ ($i \le r$); then $\langle \boldsymbol{u}_j, \boldsymbol{u}_i \rangle = \frac{1}{\sigma_i\sigma_j}\boldsymbol{v}_i^{\mathsf H}A^{\mathsf H}A\boldsymbol{v}_j = \frac{\sigma_j^2}{\sigma_i\sigma_j}\delta_{ij} = \delta_{ij}$. Extending $\boldsymbol{u}_1, \dots, \boldsymbol{u}_r$ to an orthonormal basis of $\mathbb{C}^m$ gives a unitary $U$ with $AV = U\Sigma$. $\square$

**Example 13.5.1** A matrix $A = u\boldsymbol{v}^{\mathsf H}$ of rank $1$ (with nonzero $\boldsymbol{u} \in \mathbb{C}^m$, $\boldsymbol{v} \in \mathbb{C}^n$) has the single singular value $\sigma_1 = \|\boldsymbol{u}\|\,\|\boldsymbol{v}\|$, with $\boldsymbol{u}_1 = \boldsymbol{u} / \|\boldsymbol{u}\|$, $\boldsymbol{v}_1 = \boldsymbol{v} / \|\boldsymbol{v}\|$ and $A = \sigma_1\boldsymbol{u}_1\boldsymbol{v}_1^{\mathsf H}$; the remaining columns are arbitrary extensions. For example, for the $3 \times 2$ all-ones matrix $A = (1, 1, 1)^{\mathsf T}(1, 1)$, $\sigma_1 = \sqrt3 \cdot \sqrt2 = \sqrt6$, $\boldsymbol{u}_1 = \frac{1}{\sqrt3}(1, 1, 1)^{\mathsf T}$ and $\boldsymbol{v}_1 = \frac{1}{\sqrt2}(1, 1)^{\mathsf T}$.

The singular value decomposition extends the spectral decomposition of normal matrices to arbitrary matrices, at the price of using two different unitary matrices on the left and on the right. It immediately yields the polar decomposition of a general square matrix.

**Theorem 13.5.2 (Polar Decomposition)** Let $A \in \mathbb{C}^{n\times n}$. Then there are a unitary matrix $U$ and a positive semidefinite Hermitian matrix $P$ with $A = UP$. The factor $P = (A^{\mathsf H}A)^{1/2}$ is unique; if $A$ is invertible, $U$ is unique as well. $A$ is normal $\Leftrightarrow$ $U$ can be chosen with $UP = PU$, and in that case this is the factorization $A = R\mathrm{e}^{\mathrm{i}M}$ of Theorem 13.2.1 ($R = P$, $\mathrm{e}^{\mathrm{i}M} = U$).

**Proof** From $A = W\Sigma V^{\mathsf H}$ ($W, V$ unitary, $\Sigma$ nonnegative diagonal), $A = (WV^{\mathsf H})(V\Sigma V^{\mathsf H})$; let $U = WV^{\mathsf H}$ and $P = V\Sigma V^{\mathsf H}$. From $A^{\mathsf H}A = P^2$ and the uniqueness of the positive semidefinite square root, $P$ is unique ($(A^{\mathsf H}A)^{1/2}$ is the matrix function $\sqrt z$ in the sense of [Chapter 11](/2.1.11), with the nonnegative branch); if $A$ is invertible, so is $P$, and $U = AP^{-1}$ is unique. If $UP = PU$, then $AA^{\mathsf H} = UP^2U^{\mathsf H} = P^2 = A^{\mathsf H}A$; the converse follows from Theorem 13.2.1. $\square$

Similarly, $A = (W\Sigma W^{\mathsf H})(WV^{\mathsf H}) = P'U$ with $P' = (AA^{\mathsf H})^{1/2}$. Geometrically, the polar decomposition splits an arbitrary linear transformation into "stretching along orthogonal directions" ($P$) and "a length-preserving rotation or reflection" ($U$); it is the full generalization of the complex number $z = r \cdot \mathrm{e}^{\mathrm{i}\theta}$. The code below computes the polar decomposition from the SVD and compares it with SciPy's result.

```python
import numpy as np
from scipy.linalg import polar

rng = np.random.default_rng(0)
A = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
W, s, Vh = np.linalg.svd(A)                      # A = W diag(s) V^H
U = W @ Vh                                       # unitary factor
P = Vh.conj().T @ np.diag(s) @ Vh                # positive semidefinite factor
U2, P2 = polar(A)                                # SciPy: A = U2 @ P2
print(np.allclose(U, U2), np.allclose(P, P2))    # True True
print(np.allclose(U.conj().T @ U, np.eye(4)))    # True
```

![Polar decomposition A = UP of a real 2 x 2 matrix: P first stretches by factors σ_1 and σ_2 along its two orthogonal eigenvectors v_1 and v_2, turning the unit circle into an ellipse, and U then rotates the ellipse as a whole, giving the image of the unit circle under A; the green polyline tracks the same figure through both steps](./plots/polar-decomposition.py)

The singular value decomposition and the polar decomposition have many applications; we list only a few kinds. Low-rank approximation: truncating $A = \sum\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf H}$ after the first $k$ terms gives the best rank-$k$ approximation in both the spectral norm and the Frobenius norm (the Eckart–Young theorem, Theorem 7.6.2), the basis of data compression and principal component analysis; the right singular vectors of a centered data matrix are the principal directions. Least squares and pseudoinverses: $A^+ = V\Sigma^+U^{\mathsf H}$ gives the least squares solution of minimal length, and $\sigma_1 / \sigma_r$ measures how ill-conditioned the problem is; very small singular values indicate that the matrix is "numerically" rank-deficient. Polar decomposition: $U$ is the unitary matrix closest to $A$ in the Frobenius norm, which is used to "orthogonalize" a rotation matrix contaminated by errors (the orthogonal Procrustes problem); continuum mechanics decomposes the deformation gradient into a rotation and a stretch in the same way. In quantum information, the Schmidt decomposition of a bipartite pure state is the singular value decomposition of its coefficient matrix.

## 13.6. Bilinear Forms

**Definition 13.6.1** Let $V$ be a vector space over a field $\mathbb{F}$. A map $g\colon V \times V \to \mathbb{F}$ that is linear in each argument, that is, $g(c_1\alpha_1 + c_2\alpha_2, \beta) = c_1g(\alpha_1, \beta) + c_2g(\alpha_2, \beta)$ and $g(\beta, c_1\alpha_1 + c_2\alpha_2) = c_1g(\beta, \alpha_1) + c_2g(\beta, \alpha_2)$, is called a **bilinear form** on $V$. If $g(\alpha, \beta) = g(\beta, \alpha)$ for all $\alpha, \beta$, $g$ is called a **symmetric bilinear form**; if $g(\alpha, \beta) = -g(\beta, \alpha)$, $g$ is called a **skew-symmetric bilinear form**.

In the skew-symmetric case $g(\alpha, \alpha) = -g(\alpha, \alpha)$, so $g(\alpha, \alpha) = 0$. Every bilinear form can be written uniquely as the sum of a symmetric and a skew-symmetric form: $g(\alpha, \beta) = \frac12[g(\alpha, \beta) + g(\beta, \alpha)] + \frac12[g(\alpha, \beta) - g(\beta, \alpha)]$. A complex inner product is conjugate linear in the second argument, so it is not a bilinear form; its generalization is the Hermitian form above. In what follows we mainly consider bilinear forms on real spaces.

**Example 13.6.1** Let $A \in \mathbb{F}^{n\times n}$. Then $g(\boldsymbol{\alpha}, \boldsymbol{\beta}) = \boldsymbol{\alpha}^{\mathsf T}A\boldsymbol{\beta}$ is a bilinear form on $\mathbb{F}^n$.

1. If $A$ is symmetric, $g$ is symmetric: $\boldsymbol{\alpha}^{\mathsf T}A\boldsymbol{\beta} = (\boldsymbol{\alpha}^{\mathsf T}A\boldsymbol{\beta})^{\mathsf T} = \boldsymbol{\beta}^{\mathsf T}A\boldsymbol{\alpha}$; if $A$ is skew-symmetric, $g$ is skew-symmetric.
2. If $A$ is real symmetric positive definite, $g$ is an inner product on $\mathbb{R}^n$; $A = I$ gives the standard inner product.
3. On $\mathbb{R}^4$ take $A = \operatorname{diag}(1, 1, 1, -c^2)$ and $\boldsymbol{\alpha}_k = (x_k, y_k, z_k, t_k)^{\mathsf T}$. This gives the Lorentz form $g(\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2) = x_1x_2 + y_1y_2 + z_1z_2 - c^2t_1t_2$, the "metric" of spacetime in special relativity; $g(\boldsymbol{\alpha}, \boldsymbol{\alpha})$ can be positive, negative or zero.
4. On $\mathbb{R}^2$, $g\left((a, b)^{\mathsf T}, (c, d)^{\mathsf T}\right) = ad - bc$ is a skew-symmetric form with $A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$.

**Definition 13.6.2** Let $v_1, \dots, v_n$ be a basis of $V$ and $g$ a bilinear form. The matrix $G = (g(v_i, v_j))_{n \times n}$ is called the matrix (metric matrix) of $g$ with respect to this basis. If $G$ is invertible, $g$ is called a **nondegenerate bilinear form**.

**Theorem 13.6.1** Let $\alpha = \sum x_iv_i$ and $\beta = \sum y_jv_j$. Then $g(\alpha, \beta) = \sum_{i,j}x_iy_jg(v_i, v_j) = \boldsymbol{x}^{\mathsf T}G\boldsymbol{y}$. If $(w_1, \dots, w_n) = (v_1, \dots, v_n)P$ and $G_1$, $G_2$ are the matrices of $g$ with respect to the two bases, then

$$
G_2 = P^{\mathsf T}G_1P.
$$

**Proof** The first formula follows by bilinear expansion. If $\boldsymbol{x}$ and $\boldsymbol{x}'$ are the coordinates of $\alpha$ in the two bases, then $\boldsymbol{x} = P\boldsymbol{x}'$, and likewise $\boldsymbol{y} = P\boldsymbol{y}'$, so $g(\alpha, \beta) = \boldsymbol{x}^{\mathsf T}G_1\boldsymbol{y} = \boldsymbol{x}'^{\mathsf T}(P^{\mathsf T}G_1P)\boldsymbol{y}'$; comparing with $\boldsymbol{x}'^{\mathsf T}G_2\boldsymbol{y}'$ for all $\boldsymbol{x}', \boldsymbol{y}'$ gives the result. $\square$

So the matrices of a bilinear form with respect to different bases are congruent, just as the matrices of a linear transformation with respect to different bases are similar (the comparison table in the summary of [Chapter 8](/2.1.8)). Since $\det G_2 = (\det P)^2\det G_1$, nondegeneracy does not depend on the choice of basis. Nondegeneracy is equivalent to: if $g(\alpha, \beta) = 0$ for all $\beta$, then $\alpha = 0$; it is also equivalent to the map $\alpha \mapsto g(\alpha, \cdot)$ being an isomorphism from $V$ onto the dual space $V^*$.

An inner product is a nondegenerate symmetric form, and this isomorphism is the map $\Phi\colon u \mapsto \langle \cdot, u \rangle$ of the Riesz representation theorem (Theorem 12.6.1). It clarifies the relation between the adjoint operator and the **dual map** $T^{\mathsf t}\colon V^* \to V^*$ ($T^{\mathsf t}f = f \circ T$): $T^{\mathsf t}(\Phi u) = \langle T\cdot, u \rangle = \langle \cdot, T^*u \rangle = \Phi(T^*u)$, that is, $T^* = \Phi^{-1}T^{\mathsf t}\Phi$. In an orthonormal basis of a Euclidean space both have matrix $A^{\mathsf T}$; in a unitary space $\Phi$ is conjugate linear, so the matrix of the adjoint becomes $A^{\mathsf H}$, while the matrix of the dual map is still $A^{\mathsf T}$.

**Example 13.6.2** The matrix of $g(f, h) = \int_0^1 f(x)h(x)\,\mathrm{d}x$ on $\mathcal{P}_2(\mathbb{R})$ with respect to the basis $1, x, x^2$ is

$$
G = \begin{bmatrix} 1 & \frac12 & \frac13 \\ \frac12 & \frac13 & \frac14 \\ \frac13 & \frac14 & \frac15 \end{bmatrix}, \qquad g_{ij} = \int_0^1 x^{i+j-2}\,\mathrm{d}x = \frac{1}{i + j - 1}.
$$

This is the Hilbert matrix. The Hilbert matrix of order $n$ is a notoriously ill-conditioned matrix, with condition number about $1.6 \times 10^{13}$ for $n = 10$: the monomial basis $1, x, \dots, x^{n-1}$ is "almost linearly dependent" on $[0, 1]$. If instead the polynomials obtained by orthogonalization on $[0, 1]$ (the shifted Legendre polynomials; compare Example 12.4.2) are used as a basis, the metric matrix is $I$. Choosing a good basis often does more for numerical stability than improving the algorithm.

## 13.7. Normal Forms of Symmetric and Skew-Symmetric Forms

In this section $\mathbb{F} = \mathbb{R}$. By Theorem 13.6.1, finding a basis in which the matrix of $g$ is as simple as possible means simplifying $G$ under congruence.

**Theorem 13.7.1** Let $g$ be a nondegenerate symmetric bilinear form on an $n$-dimensional real space $V$. Then there is a basis in which the matrix of $g$ is $\operatorname{diag}(I_p, -I_q)$, $p + q = n$, and the pair $(p, q)$ is uniquely determined by $g$.

**Proof** The matrix $G$ of $g$ with respect to any basis is an invertible real symmetric matrix. By **Sylvester's law of inertia** (Theorem 7.3.3), $G$ is congruent to $\operatorname{diag}(I_p, -I_q)$ with $p$ and $q$ unique; if $P^{\mathsf T}GP = \operatorname{diag}(I_p, -I_q)$, changing the basis by $P$ does the job. $\square$

The pair $(p, q)$ is called the *signature* of $g$. The Lorentz form of Example 13.6.1 has signature $(3, 1)$.

**Theorem 13.7.2** Let $g$ be a nondegenerate skew-symmetric bilinear form on an $n$-dimensional real space $V$. Then $n = 2m$ is even, and there is a basis $e_1, f_1, \dots, e_m, f_m$ with $g(e_i, f_i) = 1 = -g(f_i, e_i)$ and with $g$ vanishing on all other pairs of basis vectors. That is, the matrix of $g$ is

$$
\operatorname{diag}(J, \dots, J), \qquad J = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}.
$$

Such a basis is called a symplectic basis.

**Proof** Induction on $n$. Take $e_1 \ne 0$. By nondegeneracy there is $\beta$ with $g(e_1, \beta) \ne 0$, and rescaling gives $f_1$ with $g(e_1, f_1) = 1$. The vectors $e_1, f_1$ are linearly independent (otherwise $g(e_1, f_1) = 0$). Let $W = \operatorname{span}\{e_1, f_1\}$ and $W' = \{v \mid g(v, e_1) = g(v, f_1) = 0\}$. For every $v$, $v - g(v, f_1)e_1 + g(v, e_1)f_1 \in W'$, so $V = W + W'$; and $W \cap W' = \{0\}$ (if $ae_1 + bf_1 \in W'$, then $g(ae_1 + bf_1, f_1) = a = 0$ and $g(ae_1 + bf_1, e_1) = -b = 0$). Hence $V = W \oplus W'$, and $g$ restricted to $W'$ is still nondegenerate and skew-symmetric; apply the induction hypothesis to $W'$. For $n = 1$ a skew-symmetric form satisfies $g(\alpha, \alpha) = 0$ and is identically zero, so it cannot be nondegenerate; therefore the dimension must be even. $\square$

The evenness of the dimension can also be seen directly: $G^{\mathsf T} = -G$ gives $\det G = \det G^{\mathsf T} = (-1)^n\det G$, so $\det G \ne 0$ forces $n$ to be even.

**Definition 13.7.1** Let $g$ be a nondegenerate bilinear form on $V$. If $g$ is symmetric, $(V, g)$ is called an orthogonal space; if $g$ is skew-symmetric, $(V, g)$ is called a **symplectic space**. The set $\operatorname{Isom}(V, g) = \{T \mid g(T\alpha, T\beta) = g(\alpha, \beta), \forall \alpha, \beta\}$ of linear isomorphisms preserving $g$ is called the isometry group of $(V, g)$; the isometry group of an orthogonal space is called an **orthogonal group**, and that of a symplectic space a **symplectic group**.

$\operatorname{Isom}(V, g)$ is a group under composition: compositions and inverses of isometries are isometries. If $T$ has matrix $M$ and $g$ has matrix $G$ with respect to some basis, then $T \in \operatorname{Isom}(V, g) \Leftrightarrow M^{\mathsf T}GM = G$. In a basis giving the normal form:

| Matrix $G$ of $g$ | Isometry group | Condition |
|---|---|---|
| $I_n$ (inner product) | Orthogonal group $O(n)$ | $M^{\mathsf T}M = I$, the orthogonal transformations of the [previous chapter](/2.1.12) |
| $\operatorname{diag}(I_p, -I_q)$ | Indefinite orthogonal group $O(p, q)$ | $M^{\mathsf T}\operatorname{diag}(I_p, -I_q)M = \operatorname{diag}(I_p, -I_q)$ |
| $\operatorname{diag}(J, \dots, J)$ | Symplectic group $\operatorname{Sp}(2m, \mathbb{R})$ | $M^{\mathsf T}GM = G$ |

**Example 13.7.1** Give $\mathbb{R}^4$ the Lorentz form of Example 13.6.1. Let $0 < v < c$, $E_0 = \sqrt{1 - v^2/c^2}$, and

$$
T\colon (x, y, z, t)^{\mathsf T} \mapsto (x', y', z', t')^{\mathsf T}, \qquad x' = \frac{x - vt}{E_0}, \quad y' = y, \quad z' = z, \quad t' = \frac{t - vx/c^2}{E_0}.
$$

A direct computation gives $(x - vt)^2 - c^2\left(t - \frac{vx}{c^2}\right)^2 = \left(1 - \frac{v^2}{c^2}\right)(x^2 - c^2t^2)$, and dividing by $E_0^2$ yields $x'^2 - c^2t'^2 = x^2 - c^2t^2$, so $g(T\alpha, T\alpha) = g(\alpha, \alpha)$; by polarization of the symmetric bilinear form, $g(T\alpha_1, T\alpha_2) = g(\alpha_1, \alpha_2)$. $T$ is a Lorentz transformation, and the isometry group $O(3, 1)$ of the Lorentz form is called the *Lorentz group*.

**Example 13.7.2** The oriented area $g(\boldsymbol{\alpha}, \boldsymbol{\beta}) = \det(\boldsymbol{\alpha}, \boldsymbol{\beta})$ on $\mathbb{R}^2$ is a symplectic form. Real $2 \times 2$ matrices satisfy the identity $M^{\mathsf T}JM = (\det M)J$, so $M \in \operatorname{Sp}(2, \mathbb{R})$ $\Leftrightarrow$ $\det M = 1$: in two dimensions the symplectic transformations are exactly the linear transformations preserving oriented area. In higher dimensions the symplectic condition is much stronger than volume preservation. The phase space of Hamiltonian mechanics carries a natural symplectic form, and the time evolution of the system preserves it.

![Isometries of three bilinear forms in the plane. Left: rotations preserve x^2 + y^2, and points move along circles. Middle: Lorentz transformations (with c = 1) preserve x^2 - t^2, points move along hyperbolas, and the light cone x = ±t is invariant. Right: matrices of determinant 1 preserve oriented area; after a shear and a squeeze the unit disk still has area π](./plots/isometry-groups.py)

Taking a one-parameter subgroup $\mathrm{e}^{tX}$ in an isometry group and differentiating at $t = 0$, the condition $M^{\mathsf T}GM = G$ becomes $X^{\mathsf T}G + GX = O$. For $G = I$ this gives the skew-symmetric matrices $\mathfrak{so}(n)$, and for the symplectic matrix $G$ it gives $\mathfrak{sp}(2m)$; both are **classical Lie algebras** of [1.3.5](/1.3.5).

## 13.8. Tensors

The set $\mathcal{L}(V, V; \mathbb{F})$ of all bilinear forms on $V$ is a vector space over $\mathbb{F}$ under addition and scalar multiplication of functions. By Theorem 13.6.1, once a basis is fixed, $g \mapsto G$ is a linear isomorphism from $\mathcal{L}(V, V; \mathbb{F})$ onto $\mathbb{F}^{n\times n}$, so $\dim \mathcal{L}(V, V; \mathbb{F}) = n^2$. A natural basis of it can be built from the dual space.

**Definition 13.8.1** Let $\varphi_1, \varphi_2 \in V^*$. The bilinear form $(v_1, v_2) \mapsto \varphi_1(v_1)\varphi_2(v_2)$ is called the **tensor product** of $\varphi_1$ and $\varphi_2$ and is denoted $\varphi_1 \otimes \varphi_2$.

**Theorem 13.8.1** Let $v_1, \dots, v_n$ be a basis of $V$ and $v_1^*, \dots, v_n^*$ the **dual basis**. Then $\{v_i^* \otimes v_j^* \mid 1 \le i, j \le n\}$ is a basis of $\mathcal{L}(V, V; \mathbb{F})$, and every bilinear form satisfies

$$
g = \sum_{i,j=1}^n g(v_i, v_j)\,v_i^* \otimes v_j^*.
$$

**Proof** $(v_i^* \otimes v_j^*)(v_k, v_l) = \delta_{ik}\delta_{jl}$, so the matrix of $v_i^* \otimes v_j^*$ with respect to the basis $v_1, \dots, v_n$ is the matrix unit $E_{ij}$ (with $1$ in position $(i, j)$ and $0$ elsewhere). Since $\{E_{ij}\}$ is a basis of $\mathbb{F}^{n\times n}$, the isomorphism $g \mapsto G$ gives the result; both sides of the expansion take the same value at every $(v_k, v_l)$. $\square$

More generally, a map $g\colon V \times \cdots \times V \to \mathbb{F}$ ($k$ copies of $V$) that is linear in each argument is called a $k$-linear form.

**Definition 13.8.2** Let $k \ge 1$. A map $g\colon V^k \to \mathbb{F}$ that is linear in each argument is called a **multilinear form** of order $k$ on $V$ (a tensor of order $k$).

As in the case $k = 2$, $\{v_{i_1}^* \otimes \cdots \otimes v_{i_k}^*\}$ is a basis of the space of all $k$-linear forms, whose dimension is $n^k$, and the coordinates of $g$ form the $k$-dimensional array $g_{i_1\cdots i_k} = g(v_{i_1}, \dots, v_{i_k})$. Under a change of basis $(w_1, \dots, w_n) = (v_1, \dots, v_n)P$, every index transforms by $P$:

$$
g'_{j_1\cdots j_k} = \sum_{i_1, \dots, i_k} g_{i_1\cdots i_k}\,p_{i_1j_1}\cdots p_{i_kj_k},
$$

which for $k = 2$ is $G' = P^{\mathsf T}GP$. This gives a unified interpretation of "number $\to$ vector $\to$ matrix $\to$ tensor": numbers have order $0$, linear functionals order $1$, bilinear forms order $2$, and $k$-linear forms order $k$. The determinant $\det(\boldsymbol{\alpha}_1, \dots, \boldsymbol{\alpha}_n)$ on an $n$-dimensional space is an $n$-linear form, and it is alternating (interchanging two arguments changes the sign); this is exactly what the axiomatic definition of [Chapter 5](/2.1.5) says. The "tensors" of machine learning are usually such multidimensional arrays, that is, the coordinates of multilinear objects once a basis is fixed.

## Summary

| Topic | Result |
|---|---|
| Hermitian matrices | Real eigenvalues, unitarily diagonalizable to a real diagonal matrix; normal + real eigenvalues $\Leftrightarrow$ Hermitian (Theorem 13.1.1) |
| Polar decomposition | Normal matrices: $A = R\mathrm{e}^{\mathrm{i}M}$ with $R$ positive semidefinite, $M$ Hermitian, commuting (Theorem 13.2.1); general square matrices: $A = UP$, $P = (A^{\mathsf H}A)^{1/2}$ (Theorem 13.5.2) |
| Hermitian forms | $f = \boldsymbol{x}^{\mathsf H}A\boldsymbol{x}$ is real-valued; under $\boldsymbol{x} = P\boldsymbol{y}$ the matrix changes by \*-congruence $P^{\mathsf H}AP$; normal form and law of inertia (Theorem 13.3.1) |
| Positive definite Hermitian matrices | All eigenvalues positive $\Leftrightarrow$ $A = P^{\mathsf H}P$ $\Leftrightarrow$ all leading principal minors positive $\Leftrightarrow$ $A = R^{\mathsf H}R$ (Theorem 13.4.1) |
| Complex SVD | $A = U\Sigma V^{\mathsf H}$ (Theorem 13.5.1); applications to low-rank approximation, pseudoinverses and principal component analysis |
| Bilinear forms | $g(\alpha, \beta) = \boldsymbol{x}^{\mathsf T}G\boldsymbol{y}$, change of basis $G_2 = P^{\mathsf T}G_1P$ (Theorem 13.6.1); nondegenerate $\Leftrightarrow$ $\det G \ne 0$ |
| Normal forms | Symmetric: $\operatorname{diag}(I_p, -I_q)$; skew-symmetric: symplectic basis, even dimension (Theorems 13.7.1, 13.7.2) |
| Isometry groups | $M^{\mathsf T}GM = G$: orthogonal groups, the Lorentz group, symplectic groups |
| Tensors | $\{v_i^* \otimes v_j^*\}$ is a basis of the space of bilinear forms, of dimension $n^2$ (Theorem 13.8.1); $k$-linear forms form a space of dimension $n^k$ |

Each of the three equivalence relations belongs to one kind of object: similarity $P^{-1}AP$ to linear transformations, congruence $P^{\mathsf T}GP$ to bilinear forms, and \*-congruence $P^{\mathsf H}GP$ to Hermitian forms. When the change-of-basis matrix is orthogonal (unitary), as it is between orthonormal bases, the three coincide; this is why the spectral theorem simplifies linear transformations and quadratic forms at the same time. With this the course, which started from matrix computations and passed through vector spaces and linear maps, has arrived at the threshold of multilinear algebra.
