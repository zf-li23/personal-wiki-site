---
title: Real Symmetric Matrices
source_hash: 3e28167632ce
---

A general square matrix need not be diagonalizable, and even when it is, the eigenvectors used need not be orthogonal. Real symmetric matrices have both properties at once: they can always be diagonalized by an **orthogonal matrix**. Starting from this fact, the chapter treats in turn the spectral decomposition of real symmetric matrices, quadratic forms and the Rayleigh quotient, positive definite matrices and congruence; finally it extends "orthogonal diagonalization of symmetric matrices" to arbitrary $m\times n$ matrices, obtaining the singular value decomposition, and uses it to define the pseudoinverse and the spectral norm.

The chapter uses from [Chapter 4](/2.1.4) the **inner product**, the notions of **orthonormal basis** and **orthogonal matrix**, and the **QR decomposition**; from [Chapter 2](/2.1.2) the LDU decomposition and the **Schur complement**; and from [Chapter 6](/2.1.6) **eigenvalues**, **similar matrices** and the **eigendecomposition**. Its results are basic tools in later courses: covariance matrices are symmetric positive semidefinite (Probability, 3.1); principal component analysis is the spectral decomposition of a covariance matrix (Multivariate Statistics, 3.4); least squares and the pseudoinverse are the backbone of linear regression (3.3); and the Cholesky decomposition and the SVD are standard algorithms in statistical computing (3.9). The extensions to the complex field (normal matrices, Hermitian matrices, the complex SVD) appear in [Chapter 12](/2.1.12) and [Chapter 13](/2.1.13).

## 7.1. Spectral Decomposition of Real Symmetric Matrices

**Proposition 7.1.1** The eigenvalues of a real symmetric matrix are all real.

**Proof** Let the real symmetric matrix $A$ of order $n$ have an eigenvalue $\lambda\in\mathbb{C}$ with eigenvector $\boldsymbol{x}=[x_i]\in\mathbb{C}^n$, $A\boldsymbol{x}=\lambda\boldsymbol{x}$. Taking the conjugate transpose of both sides and using $\bar A=A$, $A^{\mathsf T}=A$, we get $\boldsymbol{x}^{\mathsf H}A=\bar\lambda\,\boldsymbol{x}^{\mathsf H}$. Hence

$$
\lambda\,\boldsymbol{x}^{\mathsf H}\boldsymbol{x}=\boldsymbol{x}^{\mathsf H}A\boldsymbol{x}=\bar\lambda\,\boldsymbol{x}^{\mathsf H}\boldsymbol{x},
$$

and since $\boldsymbol{x}^{\mathsf H}\boldsymbol{x}=\sum_{i=1}^n|x_i|^2>0$, we have $\lambda=\bar\lambda$. $\square$

Because $\lambda$ is real, $\lambda I-A$ is a real matrix, and the homogeneous system $(\lambda I-A)\boldsymbol{x}=\boldsymbol{0}$ has a nonzero real solution; so the eigenvectors of a real symmetric matrix can always be chosen real. From now on, "eigenvector" means a real eigenvector.

**Proposition 7.1.2** Eigenvectors of a real symmetric matrix belonging to distinct eigenvalues are orthogonal.

**Proof** Let $\lambda_1\neq\lambda_2$, $A\boldsymbol{x}_1=\lambda_1\boldsymbol{x}_1$ and $A\boldsymbol{x}_2=\lambda_2\boldsymbol{x}_2$. Transposing the second equation gives $\boldsymbol{x}_2^{\mathsf T}A=\lambda_2\boldsymbol{x}_2^{\mathsf T}$, so $\lambda_1\boldsymbol{x}_2^{\mathsf T}\boldsymbol{x}_1=\boldsymbol{x}_2^{\mathsf T}A\boldsymbol{x}_1=\lambda_2\boldsymbol{x}_2^{\mathsf T}\boldsymbol{x}_1$. Since $\lambda_1\neq\lambda_2$, $\boldsymbol{x}_2^{\mathsf T}\boldsymbol{x}_1=0$. $\square$

**Theorem 7.1.1 (Spectral Decomposition of a Real Symmetric Matrix)** For every real symmetric matrix $A$ of order $n$ there exist an orthogonal matrix $Q$ of order $n$ and a real diagonal matrix $\Lambda$ such that $A=Q\Lambda Q^{\mathsf T}$.

**Proof** We use induction on $n$. The case $n=1$ is trivial. Suppose the statement holds for real symmetric matrices of order $n-1$. Take any real eigenpair $(\lambda_1,\boldsymbol{q}_1)$ of $A$ with $\|\boldsymbol{q}_1\|=1$, extend $\boldsymbol{q}_1$ to an orthonormal basis $\boldsymbol{q}_1,\dots,\boldsymbol{q}_n$ of $\mathbb{R}^n$, and write $Q_1=[\boldsymbol{q}_1\ Q_{12}]$. From $A\boldsymbol{q}_1=\lambda_1\boldsymbol{q}_1$ and $Q_{12}^{\mathsf T}\boldsymbol{q}_1=\boldsymbol{0}$ we obtain

$$
Q_1^{\mathsf T}AQ_1=\begin{bmatrix}\boldsymbol{q}_1^{\mathsf T}A\boldsymbol{q}_1 & \boldsymbol{q}_1^{\mathsf T}AQ_{12}\\ Q_{12}^{\mathsf T}A\boldsymbol{q}_1 & Q_{12}^{\mathsf T}AQ_{12}\end{bmatrix}=\begin{bmatrix}\lambda_1 & \boldsymbol{0}^{\mathsf T}\\ \boldsymbol{0} & Q_{12}^{\mathsf T}AQ_{12}\end{bmatrix},
$$

where the upper right block vanishes because $\boldsymbol{q}_1^{\mathsf T}AQ_{12}=(Q_{12}^{\mathsf T}A\boldsymbol{q}_1)^{\mathsf T}$. The matrix $Q_{12}^{\mathsf T}AQ_{12}$ is real symmetric of order $n-1$, so by the induction hypothesis $Q_{12}^{\mathsf T}AQ_{12}=Q_2\Lambda_2Q_2^{\mathsf T}$. Let

$$
Q=Q_1\begin{bmatrix}1&\\&Q_2\end{bmatrix},\qquad \Lambda=\begin{bmatrix}\lambda_1&\\&\Lambda_2\end{bmatrix}.
$$

Then $Q$ is orthogonal (a product of orthogonal matrices), $\Lambda$ is real diagonal, and $A=Q\Lambda Q^{\mathsf T}$. $\square$

The factorization $A=Q\Lambda Q^{\mathsf T}$ is called the *spectral decomposition* of the real symmetric matrix $A$. It is a special case of the **eigendecomposition** $A=X\Lambda X^{-1}$ of [Chapter 6](/2.1.6), with $X$ chosen orthogonal so that $X^{-1}=X^{\mathsf T}$. Some textbooks also call $X\Lambda X^{-1}$ a "spectral decomposition" for any diagonalizable matrix; this text reserves the name for orthogonal (or unitary) diagonalization. Some remarks:

- Writing $Q=[\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$ and $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$, we have
  $$
  A=Q\Lambda Q^{\mathsf T}=\lambda_1\boldsymbol{q}_1\boldsymbol{q}_1^{\mathsf T}+\cdots+\lambda_n\boldsymbol{q}_n\boldsymbol{q}_n^{\mathsf T}.
  $$
  Each $\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf T}$ is the **orthogonal projection matrix** onto the line $\operatorname{span}(\boldsymbol{q}_i)$. Thus applying $A$ to a vector means first decomposing the vector along $n$ mutually perpendicular directions and then stretching the component in each direction by the factor $\lambda_i$.
- By permuting the columns of $Q$ we can make the diagonal of $\Lambda$ any ordering of the eigenvalues of $A$.
- A real symmetric matrix is always diagonalizable, so the **geometric multiplicity** of each eigenvalue equals its **algebraic multiplicity**.

**Algorithm 7.1.1 (Spectral Decomposition of a Real Symmetric Matrix)** Input: a real symmetric matrix $A$ of order $n$.

1. Compute all roots of the characteristic polynomial $p_A(\lambda)=\det(\lambda I-A)$, obtaining the distinct eigenvalues $\mu_1,\dots,\mu_s$;
2. for each $\mu_j$, find a basis of the solution space of $(\mu_jI-A)\boldsymbol{x}=\boldsymbol{0}$ and turn it into an orthonormal basis by the **Gram–Schmidt process**;
3. put the orthonormal bases of all eigenspaces together as the columns of $Q$, and the corresponding eigenvalues on the diagonal of $\Lambda$.

By Proposition 7.1.2, different eigenspaces are automatically orthogonal, so in step 2 we only need to orthogonalize within each eigenspace.

**Example 7.1.1** Find the spectral decomposition of $A=\begin{bmatrix}4&2&2\\2&4&2\\2&2&4\end{bmatrix}$. Since $A=2I+2\boldsymbol{1}\boldsymbol{1}^{\mathsf T}$ with $\boldsymbol{1}=[1\ 1\ 1]^{\mathsf T}$, the eigenvalues are $8$ (eigenvector $\boldsymbol{1}$) and the double eigenvalue $2$ (eigenspace $x_1+x_2+x_3=0$). Taking the basis $[-1\ 1\ 0]^{\mathsf T},[-1\ 0\ 1]^{\mathsf T}$ of the latter, orthogonalizing and normalizing, we get

$$
Q=\begin{bmatrix}\frac{1}{\sqrt3}&-\frac{1}{\sqrt2}&-\frac{1}{\sqrt6}\\ \frac{1}{\sqrt3}&\frac{1}{\sqrt2}&-\frac{1}{\sqrt6}\\ \frac{1}{\sqrt3}&0&\frac{2}{\sqrt6}\end{bmatrix},\qquad \Lambda=\operatorname{diag}(8,2,2),\qquad A=Q\Lambda Q^{\mathsf T}.
$$

**Example 7.1.2 (Spectral Decomposition of an Orthogonal Projection Matrix)** An orthogonal projection matrix $P$ satisfies $P^2=P^{\mathsf T}=P$, so it is real symmetric. If $P\boldsymbol{x}=\lambda\boldsymbol{x}$, then $P\boldsymbol{x}=P^2\boldsymbol{x}$ gives $\lambda\boldsymbol{x}=\lambda^2\boldsymbol{x}$, hence $\lambda\in\{0,1\}$. Take orthonormal bases $\boldsymbol{q}_1,\dots,\boldsymbol{q}_r$ of $\mathcal{R}(P)$ and $\boldsymbol{q}_{r+1},\dots,\boldsymbol{q}_n$ of $\mathcal{N}(P)$; they are eigenvectors for $1$ and $0$ respectively, and together form an orthonormal basis of $\mathbb{R}^n$ (since $\mathcal{N}(P)=\mathcal{R}(P)^\perp$). With $Q=[\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$,

$$
P=Q\begin{bmatrix}I_r&\\&O\end{bmatrix}Q^{\mathsf T}=\boldsymbol{q}_1\boldsymbol{q}_1^{\mathsf T}+\cdots+\boldsymbol{q}_r\boldsymbol{q}_r^{\mathsf T}.
$$

The spectral decomposition $A=Q\Lambda Q^{\mathsf T}$ can also be written $Q^{\mathsf T}AQ=\Lambda$, which leads to the following equivalence relation.

**Definition 7.1.1 (Orthogonal Similarity)** Real square matrices $A,B$ are said to be **orthogonally similar** if there is an orthogonal matrix $Q$ such that $Q^{\mathsf T}AQ=B$.

**Proposition 7.1.3** Orthogonal similarity of real square matrices is an **equivalence relation**.

**Proof** Reflexivity: $A=I^{\mathsf T}AI$. Symmetry: $Q^{\mathsf T}AQ=B$ gives $Q BQ^{\mathsf T}=A$, and $Q^{\mathsf T}$ is also orthogonal. Transitivity: $Q^{\mathsf T}AQ=B$ and $R^{\mathsf T}BR=C$ give $(QR)^{\mathsf T}A(QR)=C$. $\square$

The corresponding transformation $A\mapsto Q^{\mathsf T}AQ$ is called an orthogonal similarity transformation. Orthogonal similarity is a special case of **matrix similarity** ($Q^{\mathsf T}=Q^{-1}$), so the similarity invariants (rank, characteristic polynomial, eigenvalues with their algebraic and geometric multiplicities, determinant, trace) are invariants of orthogonal similarity as well; in addition it preserves symmetry: $Q^{\mathsf T}AQ$ is symmetric (skew-symmetric) if and only if $A$ is. Theorem 7.1.1 says that the canonical form of a real symmetric matrix under orthogonal similarity is a real diagonal matrix; in other words, a real square matrix is orthogonally similar to a diagonal matrix if and only if it is symmetric (necessity: $Q\Lambda Q^{\mathsf T}$ is obviously symmetric). Orthogonal similarity is not used only for symmetric matrices: the canonical form of nonsymmetric real matrices under orthogonal similarity (the real Schur form) and unitary similarity of complex matrices are treated in [Chapter 12](/2.1.12).

## 7.2. Quadratic Forms and the Rayleigh Quotient

**Definition 7.2.1 (Quadratic Form)** A homogeneous quadratic function of the variables $x_1,\dots,x_n$ with real coefficients,

$$
f(x_1,\dots,x_n)=\sum_{i=1}^n\sum_{j=1}^n a_{ij}x_ix_j,
$$

is called a **quadratic form**. Writing $\boldsymbol{x}=[x_i]$ and $A=[a_{ij}]_{n\times n}$, we have $f(\boldsymbol{x})=\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$.

From $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=(\boldsymbol{x}^{\mathsf T}A\boldsymbol{x})^{\mathsf T}=\boldsymbol{x}^{\mathsf T}A^{\mathsf T}\boldsymbol{x}$ we get

$$
\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{x}^{\mathsf T}\frac{A+A^{\mathsf T}}{2}\boldsymbol{x},
$$

that is, a quadratic form depends only on the **symmetric matrix** part $\frac12(A+A^{\mathsf T})$ of $A$ (every square matrix splits uniquely into a symmetric part and a **skew-symmetric matrix** part). From now on we therefore always assume the matrix of a quadratic form to be real symmetric; then $A$ is uniquely determined by the form: $a_{ii}$ is the coefficient of $x_i^2$, and $a_{ij}=a_{ji}$ is half the coefficient of $x_ix_j$. The energy of many physical systems is a quadratic form, for instance the energy of a harmonic oscillator,

$$
\tfrac12kx^2+\tfrac12mv^2=\begin{bmatrix}x&v\end{bmatrix}\begin{bmatrix}\frac12k&\\&\frac12m\end{bmatrix}\begin{bmatrix}x\\v\end{bmatrix},
$$

which is why $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$ is often called an energy function.

**Example 7.2.1 (Hessian Matrix)** Let $f\colon \mathbb{R}^n\to\mathbb{R}$ be three times continuously differentiable near $\boldsymbol{x}_0$. By the multivariate **Taylor's formula**, in a small neighborhood of $\boldsymbol{x}_0$ of radius $\rho$,

$$
f(\boldsymbol{x})=f(\boldsymbol{x}_0)+\nabla f(\boldsymbol{x}_0)^{\mathsf T}(\boldsymbol{x}-\boldsymbol{x}_0)+\tfrac12(\boldsymbol{x}-\boldsymbol{x}_0)^{\mathsf T}H(\boldsymbol{x}_0)(\boldsymbol{x}-\boldsymbol{x}_0)+o(\rho^2),
$$

where $\nabla f(\boldsymbol{x}_0)=\Big[\frac{\partial f}{\partial x_i}(\boldsymbol{x}_0)\Big]_{n\times1}$ is the gradient and $H(\boldsymbol{x}_0)=\Big[\frac{\partial^2 f}{\partial x_i\partial x_j}(\boldsymbol{x}_0)\Big]_{n\times n}$ is called the *Hessian matrix* of $f$ at $\boldsymbol{x}_0$. When the second partial derivatives are continuous, mixed partials do not depend on the order of differentiation, so the Hessian matrix is real symmetric and the second-order term of the Taylor expansion is a quadratic form.

The spectral decomposition removes the cross terms of a quadratic form. Let $A=Q\Lambda Q^{\mathsf T}$ and make the orthogonal change of variables $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{x}$; then

$$
\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{y}^{\mathsf T}\Lambda\boldsymbol{y}=\lambda_1y_1^2+\cdots+\lambda_ny_n^2.
$$

Geometrically, this rotates the coordinate axes onto the $n$ mutually orthogonal eigenvector directions of $A$, called the principal axes. For example, the matrix $\begin{bmatrix}5&2\\2&5\end{bmatrix}$ of $5x_1^2+4x_1x_2+5x_2^2=1$ has eigenvalues $7,3$ with eigenvectors $\frac{1}{\sqrt2}[1\ 1]^{\mathsf T},\frac{1}{\sqrt2}[-1\ 1]^{\mathsf T}$, so the curve is $7y_1^2+3y_2^2=1$: an ellipse whose principal axes lie along the $45^\circ$ directions, with semi-axes $1/\sqrt7$ and $1/\sqrt3$.

To study how the form depends only on the direction of $\boldsymbol{x}$, we divide it by $\|\boldsymbol{x}\|^2$:

**Definition 7.2.2 (Rayleigh Quotient)** Given a real square matrix $A$ and a nonzero vector $\boldsymbol{x}\in\mathbb{R}^n$, the real number $\dfrac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$ is called the **Rayleigh quotient** of $\boldsymbol{x}$ with respect to $A$.

If $A=QBQ^{\mathsf T}$ with $Q$ orthogonal and $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{x}$, then $\dfrac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}=\dfrac{\boldsymbol{y}^{\mathsf T}B\boldsymbol{y}}{\boldsymbol{y}^{\mathsf T}\boldsymbol{y}}$: an orthogonal similarity turns a Rayleigh quotient into the Rayleigh quotient of another matrix, with the argument transformed orthogonally. Taking $B=\Lambda$ yields the following extremal characterization.

**Theorem 7.2.1 (Extremal Characterization of Eigenvalues)** Let the eigenvalues of the real symmetric matrix $A$ be $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n$, with corresponding eigenvectors $\boldsymbol{q}_1,\dots,\boldsymbol{q}_n$ forming an orthonormal basis of $\mathbb{R}^n$. Then

$$
\lambda_i=\max_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_i,\dots,\boldsymbol{q}_n)}}\frac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}=\min_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_1,\dots,\boldsymbol{q}_i)}}\frac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}.
$$

In particular, $\lambda_1=\max\limits_{\boldsymbol{x}\neq\boldsymbol{0}}\dfrac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$ and $\lambda_n=\min\limits_{\boldsymbol{x}\neq\boldsymbol{0}}\dfrac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$.

The condition $\boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_i,\dots,\boldsymbol{q}_n)$ is equivalent to $\boldsymbol{x}\perp\operatorname{span}(\boldsymbol{q}_1,\dots,\boldsymbol{q}_{i-1})$, so we maximize over the directions orthogonal to the first $i-1$ eigenvectors.

**Proof** Let $Q=[\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$ and $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$, so that $A=Q\Lambda Q^{\mathsf T}$. Put $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{x}$. Since $Q^{\mathsf T}\boldsymbol{q}_j=\boldsymbol{e}_j$, we have $\boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_i,\dots,\boldsymbol{q}_n)$ if and only if $\boldsymbol{y}\in\operatorname{span}(\boldsymbol{e}_i,\dots,\boldsymbol{e}_n)$, that is, $y_1=\cdots=y_{i-1}=0$. Therefore

$$
\max_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_i,\dots,\boldsymbol{q}_n)}}\frac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}=\max_{\substack{\boldsymbol{y}\neq\boldsymbol{0}\\ y_1=\cdots=y_{i-1}=0}}\frac{\lambda_iy_i^2+\cdots+\lambda_ny_n^2}{y_i^2+\cdots+y_n^2}=\lambda_i,
$$

because the numerator is at most $\lambda_i(y_i^2+\cdots+y_n^2)$, with equality for $\boldsymbol{y}=\boldsymbol{e}_i$. Applying this to $-A$, whose eigenvalues $-\lambda_n\ge\cdots\ge-\lambda_1$ have eigenvectors $\boldsymbol{q}_n,\dots,\boldsymbol{q}_1$, gives $-\lambda_i=\max\limits_{\boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_1,\dots,\boldsymbol{q}_i)}\frac{\boldsymbol{x}^{\mathsf T}(-A)\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$, which is the second equality. $\square$

Theorem 7.2.1 turns an eigenvalue problem into a constrained optimization problem: $\lambda_1$ is the maximum of the quadratic form on the unit sphere $\|\boldsymbol{x}\|=1$, attained at $\boldsymbol{q}_1$. This is exactly how principal component analysis finds the direction of maximal variance of a covariance matrix. The more general Courant–Fischer minimax principle does not require the eigenvectors in advance: $\lambda_i$ is the maximum, over all $i$-dimensional subspaces, of the minimum of the Rayleigh quotient on the subspace.

Take the earlier form $5x_1^2+4x_1x_2+5x_2^2$ as an example. The left panel of the figure below shows its level curves, all of them ellipses whose principal axes are the two eigenvectors; the right panel shows the Rayleigh quotient along the unit circle, whose maximum $7$ is attained in the direction of $\boldsymbol{q}_1$ ($45^\circ$) and whose minimum $3$ is attained in the orthogonal direction $\boldsymbol{q}_2$ ($135^\circ$).

![Left: the level curves of the quadratic form 5x_1^2+4x_1x_2+5x_2^2 are ellipses whose principal axes are the eigenvectors; the arrows are the two semi-axes q_i/√λ_i of the curve x^T A x = 1. Right: the Rayleigh quotient on the unit circle, whose maximum and minimum are exactly the eigenvalues 7 and 3](./plots/principal-axes-rayleigh.py)

For a nonsymmetric real square matrix $A$, the Rayleigh quotient depends only on the symmetric part of $A$, so its extreme values are the largest and smallest eigenvalues of $\frac12(A+A^{\mathsf T})$, not eigenvalues of $A$. For example, $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ has both eigenvalues equal to $0$, but its Rayleigh quotient $x_1x_2/(x_1^2+x_2^2)$ takes every value in $[-\frac12,\frac12]$.

## 7.3. Positive Definite Matrices and Congruence

### 7.3.1. Classification of Quadratic Forms

**Definition 7.3.1 (Classification of Quadratic Forms)** Let $A$ be a real square matrix of order $n$. If for every nonzero vector $\boldsymbol{x}\in\mathbb{R}^n$

1. $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$, then $A$ is called a **positive definite matrix**, and the quadratic form is called positive definite;
2. $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}\ge0$, then $A$ is called a **positive semidefinite matrix**, and the quadratic form is called positive semidefinite;
3. $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}<0$, then $A$ is called a **negative definite matrix**;
4. $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}\le0$, then $A$ is called a **negative semidefinite matrix**;
5. if $A$ satisfies none of the above, that is, there exist $\boldsymbol{x},\boldsymbol{y}$ with $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0>\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}$, then $A$ is called an **indefinite matrix**, and the quadratic form is called indefinite.

$A$ is negative (semi)definite if and only if $-A$ is positive (semi)definite, so it suffices to study the positive definite and positive semidefinite cases. Following the convention of §7.2, we always assume $A$ to be real symmetric when discussing definiteness.

**Proposition 7.3.1** Let $T$ be an invertible matrix of order $n$. Then $T^{\mathsf T}AT$ is positive (semi)definite, negative (semi)definite or indefinite exactly when $A$ is.

**Proof** We treat positive definiteness. If $A$ is positive definite and $\boldsymbol{x}\neq\boldsymbol{0}$, then $T\boldsymbol{x}\neq\boldsymbol{0}$, so $\boldsymbol{x}^{\mathsf T}T^{\mathsf T}AT\boldsymbol{x}=(T\boldsymbol{x})^{\mathsf T}A(T\boldsymbol{x})>0$. Conversely, if $T^{\mathsf T}AT$ is positive definite and $\boldsymbol{x}\neq\boldsymbol{0}$, let $\boldsymbol{y}=T^{-1}\boldsymbol{x}\neq\boldsymbol{0}$; then $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{y}^{\mathsf T}T^{\mathsf T}AT\boldsymbol{y}>0$. $\square$

**Example 7.3.1 (The Hessian Matrix and Extrema)** Return to Example 7.2.1. If $\boldsymbol{x}_0$ is a stationary point, $\nabla f(\boldsymbol{x}_0)=\boldsymbol{0}$, then $f(\boldsymbol{x})-f(\boldsymbol{x}_0)=\frac12(\boldsymbol{x}-\boldsymbol{x}_0)^{\mathsf T}H(\boldsymbol{x}_0)(\boldsymbol{x}-\boldsymbol{x}_0)+o(\rho^2)$. Hence: if $H(\boldsymbol{x}_0)$ is positive definite, $\boldsymbol{x}_0$ is a local minimum; if it is negative definite, a local maximum; if it is indefinite, not an extremum; if it is positive or negative semidefinite (and singular), higher-order Taylor terms are needed to decide.

### 7.3.2. Positive Definite Matrices

A positive definite matrix is invertible (otherwise take a nonzero $\boldsymbol{x}\in\mathcal{N}(A)$, for which $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=0$). A real diagonal matrix is positive definite if and only if its diagonal entries are positive; in particular the identity matrix is positive definite, which is just the positivity $\boldsymbol{x}^{\mathsf T}\boldsymbol{x}>0$ of the **inner product**.

**Definition 7.3.2 (Leading Principal Minor)** The determinant $\det A_i$ of the $i$-th leading principal submatrix $A_i$ (the upper left $i\times i$ submatrix) of a square matrix $A$ is called the $i$-th **leading principal minor** of $A$.

**Theorem 7.3.1 (Equivalent Conditions for Positive Definiteness)** For a real symmetric matrix $A$ the following are equivalent:

1. $A$ is positive definite, that is, $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$ for every nonzero vector $\boldsymbol{x}$;
2. all eigenvalues of $A$ are positive;
3. there is an invertible matrix $T$ such that $A=T^{\mathsf T}T$;
4. $A$ has an $LDL^{\mathsf T}$ decomposition ($L$ unit lower triangular, $D$ diagonal) in which the diagonal entries of $D$ are all positive;
5. all leading principal minors of $A$ are positive;
6. all leading principal submatrices of $A$ are positive definite.

**Proof** (cyclic) $1\Rightarrow2$: if $(\lambda,\boldsymbol{x})$ is an eigenpair, then $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\lambda\boldsymbol{x}^{\mathsf T}\boldsymbol{x}>0$, so $\lambda>0$.

$2\Rightarrow3$: in the spectral decomposition $A=Q\Lambda Q^{\mathsf T}$ the diagonal entries of $\Lambda$ are positive; take the diagonal matrix $\Lambda^{1/2}$ with $(\Lambda^{1/2})^2=\Lambda$ and let $T=\Lambda^{1/2}Q^{\mathsf T}$. Then $T$ is invertible and $A=T^{\mathsf T}T$.

$3\Rightarrow4$: take the **QR decomposition** $T=QR$, where $R$ is upper triangular with positive diagonal; then $A=R^{\mathsf T}Q^{\mathsf T}QR=R^{\mathsf T}R$. Write $R^{\mathsf T}=L\tilde D$ ($L$ unit lower triangular, $\tilde D$ the diagonal part of $R$, with positive diagonal); then $A=L\tilde D^2L^{\mathsf T}$, and we take $D=\tilde D^2$.

$4\Rightarrow5$: partition according to the $i$-th leading principal submatrix,

$$
\begin{bmatrix}A_i&A_{21}^{\mathsf T}\\A_{21}&A_{22}\end{bmatrix}=\begin{bmatrix}L_i&\\L_{21}&L_{22}\end{bmatrix}\begin{bmatrix}D_i&\\&D_{22}\end{bmatrix}\begin{bmatrix}L_i&\\L_{21}&L_{22}\end{bmatrix}^{\mathsf T}.
$$

Comparing the upper left blocks gives $A_i=L_iD_iL_i^{\mathsf T}$, so $\det A_i=\det D_i>0$.

$5\Rightarrow6$: induction on $n$; the case $n=1$ is clear. Suppose the claim holds in order $n-1$. The leading principal submatrices $A_1,\dots,A_{n-1}$ of $A$ are also those of $A_{n-1}$, so by the induction hypothesis they are all positive definite, and it remains to show that $A=A_n$ is positive definite. $A_{n-1}$ is invertible and $A_{n-1}^{-1}$ is symmetric. Write $A=\begin{bmatrix}A_{n-1}&\boldsymbol{a}\\\boldsymbol{a}^{\mathsf T}&a_{nn}\end{bmatrix}$ and perform block elimination:

$$
A=\begin{bmatrix}I_{n-1}&\\\boldsymbol{a}^{\mathsf T}A_{n-1}^{-1}&1\end{bmatrix}\begin{bmatrix}A_{n-1}&\\&a_{nn}-\boldsymbol{a}^{\mathsf T}A_{n-1}^{-1}\boldsymbol{a}\end{bmatrix}\begin{bmatrix}I_{n-1}&A_{n-1}^{-1}\boldsymbol{a}\\&1\end{bmatrix}=TBT^{\mathsf T}.
$$

By Proposition 7.3.1, $A$ is positive definite if and only if $B$ is. The lower right entry of $B$ is the **Schur complement** of $A_{n-1}$; taking determinants gives $a_{nn}-\boldsymbol{a}^{\mathsf T}A_{n-1}^{-1}\boldsymbol{a}=\det A/\det A_{n-1}>0$, and $A_{n-1}$ is positive definite, so the block diagonal matrix $B$ is positive definite.

$6\Rightarrow1$: $A=A_n$ is itself a leading principal submatrix. $\square$

Conditions 2 and 5 are two practical tests: the former requires the eigenvalues, the latter only $n$ determinants. Condition 4 says that if Gaussian elimination on a symmetric matrix produces only positive pivots, it has at the same time proved the matrix positive definite; this is the cheapest test computationally. Theorem 7.3.1 also yields several properties of positive definite matrices:

- if $A$ is positive definite, then so are $A^{-1}$ (its eigenvalues are $\lambda_i^{-1}>0$) and $A^k$ ($k\in\mathbb{N}$);
- if $A,B$ are positive definite and $k>0$, then $A+B$ and $kA$ are positive definite (directly from the definition);
- the diagonal entries of a positive definite matrix satisfy $a_{ii}=\boldsymbol{e}_i^{\mathsf T}A\boldsymbol{e}_i>0$;
- if $C$ is an $m\times n$ matrix of full column rank, then $C^{\mathsf T}C$ is positive definite ($\boldsymbol{x}^{\mathsf T}C^{\mathsf T}C\boldsymbol{x}=\|C\boldsymbol{x}\|^2>0$).

### 7.3.3. The Cholesky Decomposition

Setting $\tilde L=LD^{1/2}$ in condition 4 writes $A$ as a lower triangular matrix times its transpose.

**Theorem 7.3.2 (Cholesky Decomposition)** A real symmetric matrix $A$ is positive definite if and only if there is a lower triangular matrix $L$ with positive diagonal entries such that $A=LL^{\mathsf T}$; such an $L$ is unique.

**Proof** Existence: by condition 4 of Theorem 7.3.1, $A=L_0DL_0^{\mathsf T}$; take $L=L_0D^{1/2}$. Conversely, if $A=LL^{\mathsf T}$ with $L$ invertible, then $A$ is positive definite by condition 3. Uniqueness: if $L_1L_1^{\mathsf T}=L_2L_2^{\mathsf T}$, then $L_2^{-1}L_1=L_2^{\mathsf T}L_1^{-\mathsf T}$. The left side is lower triangular and the right side upper triangular, so both equal a diagonal matrix $D$ with positive diagonal; moreover $D=L_2^{-1}L_1$ and $D^{-1}=(L_2^{\mathsf T}L_1^{-\mathsf T})^{-1}=L_1^{\mathsf T}L_2^{-\mathsf T}=D^{\mathsf T}=D$, hence $D^2=I$, $D=I$ and $L_1=L_2$. $\square$

Comparing the $(i,j)$ entries ($i\ge j$) of $A=LL^{\mathsf T}$ gives $a_{ij}=\sum_{k=1}^{j}l_{ik}l_{jk}$, from which the entries of $L$ are solved column by column:

**Algorithm 7.3.1 (Cholesky Decomposition)** Input: a real symmetric matrix $A$ of order $n$. For $j=1,2,\dots,n$:

1. compute $d=a_{jj}-\sum_{k=1}^{j-1}l_{jk}^2$. If $d\le0$, then $A$ is not positive definite; stop. Otherwise set $l_{jj}=\sqrt d$;
2. for $i=j+1,\dots,n$, compute $l_{ij}=\Big(a_{ij}-\sum_{k=1}^{j-1}l_{ik}l_{jk}\Big)\Big/l_{jj}$.

The algorithm uses only the lower triangular part of $A$ and takes about $\frac13n^3$ multiply–adds, half of the LU decomposition (about $\frac23n^3$), with half the storage; it needs no pivoting and is numerically stable; and whether it runs to completion is itself a test of positive definiteness. To solve a positive definite system $A\boldsymbol{x}=\boldsymbol{b}$, first factor $A=LL^{\mathsf T}$, then solve $L\boldsymbol{y}=\boldsymbol{b}$ by forward substitution and $L^{\mathsf T}\boldsymbol{x}=\boldsymbol{y}$ by **back substitution**. This is the standard method for the normal equations $A^{\mathsf T}A\boldsymbol{x}=A^{\mathsf T}\boldsymbol{b}$ ($A$ of full column rank) and for sampling from a multivariate normal distribution.

**Example 7.3.2** For $A=\begin{bmatrix}4&2&2\\2&5&3\\2&3&6\end{bmatrix}$: $l_{11}=2$, $l_{21}=l_{31}=1$; $l_{22}=\sqrt{5-1}=2$, $l_{32}=(3-1)/2=1$; $l_{33}=\sqrt{6-1-1}=2$. So $A$ is positive definite, and

$$
A=\begin{bmatrix}2&&\\1&2&\\1&1&2\end{bmatrix}\begin{bmatrix}2&1&1\\&2&1\\&&2\end{bmatrix}.
$$

Over the complex field, a positive definite Hermitian matrix likewise has a unique factorization $A=R^{\mathsf H}R$ with $R$ upper triangular with positive real diagonal; see [Chapter 13](/2.1.13).

### 7.3.4. Positive Semidefinite and Indefinite Matrices

**Proposition 7.3.2 (Equivalent Conditions for Positive Semidefiniteness)** For a real symmetric matrix $A$ the following are equivalent:

1. $A$ is positive semidefinite;
2. all eigenvalues of $A$ are nonnegative;
3. there is a matrix $T$ such that $A=T^{\mathsf T}T$;
4. $A$ has an $LDL^{\mathsf T}$ decomposition in which the diagonal entries of $D$ are all nonnegative.

**Proof** $1\Rightarrow2$ and $2\Rightarrow3$ are as in Theorem 7.3.1 (now $\Lambda^{1/2}$ may have zero diagonal entries). $3\Rightarrow1$: $\boldsymbol{x}^{\mathsf T}T^{\mathsf T}T\boldsymbol{x}=\|T\boldsymbol{x}\|^2\ge0$. $4\Rightarrow1$: with $\boldsymbol{y}=L^{\mathsf T}\boldsymbol{x}$, $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{y}^{\mathsf T}D\boldsymbol{y}\ge0$. $1\Rightarrow4$: induction on $n$; write $A=\begin{bmatrix}a_{11}&\boldsymbol{a}^{\mathsf T}\\\boldsymbol{a}&A'\end{bmatrix}$. If $a_{11}>0$, eliminate the first column: $A=\begin{bmatrix}1&\\\boldsymbol{a}/a_{11}&I\end{bmatrix}\begin{bmatrix}a_{11}&\\&A'-\boldsymbol{a}\boldsymbol{a}^{\mathsf T}/a_{11}\end{bmatrix}\begin{bmatrix}1&\\\boldsymbol{a}/a_{11}&I\end{bmatrix}^{\mathsf T}$; by Proposition 7.3.1 the middle matrix is positive semidefinite, and we apply the induction hypothesis to its lower right block. If $a_{11}=0$, then $\boldsymbol{a}=\boldsymbol{0}$: otherwise, taking $\boldsymbol{x}=[t\ \ \boldsymbol{a}^{\mathsf T}]^{\mathsf T}$, the value $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=2t\|\boldsymbol{a}\|^2+\boldsymbol{a}^{\mathsf T}A'\boldsymbol{a}$ becomes negative as $t\to-\infty$; so $A=\operatorname{diag}(0,A')$, and we apply the induction hypothesis to $A'$. $\square$

- For a real symmetric positive semidefinite matrix $A$, $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=0$ if and only if $\boldsymbol{x}\in\mathcal{N}(A)$: writing $A=T^{\mathsf T}T$, $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\|T\boldsymbol{x}\|^2=0$ implies $T\boldsymbol{x}=\boldsymbol{0}$, hence $A\boldsymbol{x}=\boldsymbol{0}$.
- The leading principal minors of a positive semidefinite matrix are nonnegative, but the converse fails: $A=\begin{bmatrix}0&0\\0&-1\end{bmatrix}$ has leading principal minors $0,0$, yet $\boldsymbol{e}_2^{\mathsf T}A\boldsymbol{e}_2=-1$. The correct test is: a real symmetric matrix is positive semidefinite if and only if all of its principal minors (determinants of submatrices formed by choosing the same set of rows and columns) are nonnegative.
- For every real matrix $C$, both $C^{\mathsf T}C$ and $CC^{\mathsf T}$ are positive semidefinite (condition 3); the singular value decomposition of §7.4 starts from here.

**Proposition 7.3.3** If the real symmetric matrix $A$ of order $n$ is indefinite, that is, there exist $\boldsymbol{x},\boldsymbol{y}$ with $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$ and $\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}<0$, then there is a nonzero vector $\boldsymbol{z}$ with $\boldsymbol{z}^{\mathsf T}A\boldsymbol{z}=0$.

**Proof** $\boldsymbol{x},\boldsymbol{y}$ are linearly independent (otherwise their quadratic forms would have the same sign), so $\boldsymbol{z}=\boldsymbol{x}+k\boldsymbol{y}\neq\boldsymbol{0}$. The value $\boldsymbol{z}^{\mathsf T}A\boldsymbol{z}=\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}+2k\,\boldsymbol{x}^{\mathsf T}A\boldsymbol{y}+k^2\,\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}$ is a quadratic function of $k$ with negative leading coefficient and positive constant term; its discriminant $4(\boldsymbol{x}^{\mathsf T}A\boldsymbol{y})^2-4(\boldsymbol{x}^{\mathsf T}A\boldsymbol{x})(\boldsymbol{y}^{\mathsf T}A\boldsymbol{y})>0$, so it has a real root. $\square$

### 7.3.5. Congruence and the Law of Inertia

The transformation $A\mapsto T^{\mathsf T}AT$ in Proposition 7.3.1 comes from the change of variables $\boldsymbol{x}=T\boldsymbol{y}$: $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{y}^{\mathsf T}(T^{\mathsf T}AT)\boldsymbol{y}$. This motivates the following definition.

**Definition 7.3.3 (Congruence)** Square matrices $A,B$ are called **congruent matrices** if there is an invertible matrix $X$ such that $X^{\mathsf T}AX=B$.

**Proposition 7.3.4** Congruence of square matrices is an equivalence relation.

**Proof** Reflexivity: $A=I^{\mathsf T}AI$. Symmetry: $X^{\mathsf T}AX=B$ gives $(X^{-1})^{\mathsf T}BX^{-1}=A$. Transitivity: $X^{\mathsf T}AX=B$ and $Y^{\mathsf T}BY=C$ give $(XY)^{\mathsf T}A(XY)=C$. $\square$

The corresponding transformation $A\mapsto X^{\mathsf T}AX$ ($X$ invertible) is called a congruence transformation. Its invariants include rank, positive (semi)definiteness, negative (semi)definiteness and indefiniteness (Proposition 7.3.1), and symmetry. Orthogonal similarity is a special congruence ($X^{\mathsf T}=X^{-1}$ when $X$ is orthogonal), but congruence in general does not preserve eigenvalues; for example, $\operatorname{diag}(1,4)$ is congruent to $I_2$. By condition 3 of Theorem 7.3.1, a real symmetric matrix is positive definite if and only if it is congruent to the identity matrix.

**Proposition 7.3.5 (Congruence Canonical Form)** For a real symmetric matrix $A$ there is an invertible matrix $X$ such that

$$
X^{\mathsf T}AX=J=\begin{bmatrix}I_p&&\\&-I_{r-p}&\\&&O\end{bmatrix},
$$

where $r=\operatorname{rank}(A)$ and $0\le p\le r$. $J$ is called the congruence canonical form of $A$.

**Proof** By the spectral decomposition there is an orthogonal matrix $Q$ with $Q^{\mathsf T}AQ=\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$, where we order the eigenvalues so that $\lambda_1,\dots,\lambda_p>0$, $\lambda_{p+1},\dots,\lambda_r<0$ and $\lambda_{r+1}=\cdots=\lambda_n=0$. Let $Y=\operatorname{diag}\big(|\lambda_1|^{-1/2},\dots,|\lambda_r|^{-1/2},1,\dots,1\big)$; then $Y^{\mathsf T}\Lambda Y=J$. Take $X=QY$. $\square$

**Theorem 7.3.3 (Sylvester's Law of Inertia)** The congruence canonical form of a real symmetric matrix is unique, and its numbers of positive, negative and zero diagonal entries equal the numbers of positive, negative and zero eigenvalues of the matrix (counted with multiplicity).

**Proof** By the proof of Proposition 7.3.5, it suffices to show that the canonical form is unique. Let $J_1=X^{\mathsf T}AX$ and $J_2=Y^{\mathsf T}AY$ be two congruence canonical forms of $A$ with $p$ and $q$ positive diagonal entries respectively; both have rank $r$, so we need only show $p=q$. Partition $X=[X_1\ X_2]$ and $Y=[Y_1\ Y_2]$ with $X_1$ having $p$ columns and $Y_1$ having $q$ columns; then $X_1^{\mathsf T}AX_1=I_p$ and $Y_2^{\mathsf T}AY_2=\operatorname{diag}(-I_{r-q},O)$. Let $M=\mathcal{R}(X_1)$ and $N=\mathcal{R}(Y_2)$, so $\dim M=p$ and $\dim N=n-q$; for nonzero $\boldsymbol{x}\in M$ we have $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$, and for $\boldsymbol{x}\in N$ we have $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}\le0$, hence $M\cap N=\{\boldsymbol{0}\}$. From $\dim(M+N)=\dim M+\dim N\le n$ we get $p\le q$. Exchanging the roles of $J_1,J_2$ gives $q\le p$. $\square$

**Definition 7.3.4 (Inertia)** For a real symmetric matrix $A$, the number $p$ of diagonal entries $1$ in its congruence canonical form is called the **positive index of inertia** of $A$, and the number $r-p$ of diagonal entries $-1$ the **negative index of inertia**; the triple $(p,\,r-p,\,n-r)$ is called the **inertia** of $A$.

Inertia is a complete invariant under congruence: two real symmetric matrices of order $n$ are congruent if and only if they have the same inertia (both are then congruent to the same $J$). Hence the real symmetric matrices of order $n$ fall into $\sum_{r=0}^n(r+1)=\frac{(n+1)(n+2)}{2}$ congruence classes. A real symmetric matrix is positive definite if and only if $p=n$, and positive semidefinite if and only if $p=r$.

**Example 7.3.3 (Completing the Square)** The congruence canonical form gives a "sum of squares" form of a quadratic form: if $A=T^{\mathsf T}JT$ and $\boldsymbol{y}=T\boldsymbol{x}$, then

$$
\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=y_1^2+\cdots+y_p^2-y_{p+1}^2-\cdots-y_r^2,
$$

called the canonical form of the quadratic form. In practice there is no need to compute eigenvalues: complete the square one variable at a time (each step removes one variable from the remainder). For example,

$$
x_1^2+x_1x_2+2x_3^2=\Big(x_1+\tfrac12x_2\Big)^2-\tfrac14x_2^2+2x_3^2,
$$

and with $y_1=x_1+\frac12x_2$, $y_2=\frac12x_2$, $y_3=\sqrt2\,x_3$ we get $y_1^2-y_2^2+y_3^2$, so the inertia is $(2,1,0)$. The substitution used for completing squares is not unique, nor are the resulting coefficients, but by the law of inertia the numbers of positive and negative squares are fixed. With an orthogonal substitution (the spectral decomposition) the coefficients of the squares are the eigenvalues; a general invertible substitution preserves only their signs.

**Example 7.3.4 (Stationary Points of Quadratic Functions of Two Variables)** For $f(\boldsymbol{x})=\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$ with $A$ a real symmetric matrix of order 2, $\boldsymbol{0}$ is a stationary point and the Hessian matrix is $2A$. There are 6 congruence canonical forms of $A$: $\operatorname{diag}(1,1)$ (minimum, elliptic paraboloid), $\operatorname{diag}(-1,-1)$ (maximum), $\operatorname{diag}(1,-1)$ (saddle point, hyperbolic paraboloid), $\operatorname{diag}(1,0)$ and $\operatorname{diag}(-1,0)$ (parabolic cylinder, with a degenerate line of stationary points), and $\operatorname{diag}(0,0)$ (constant function). The graphs of the first five in the new coordinates $\boldsymbol{y}$ are shown below.

![The quadric surfaces z = y^T J y for the five nonzero congruence canonical forms](./plots/quadratic-forms-2d.py)

## 7.4. Singular Value Decomposition

An $m\times n$ matrix has no eigenvalues, but $A^{\mathsf T}A$ (of order $n$) and $AA^{\mathsf T}$ (of order $m$) are symmetric positive semidefinite and have spectral decompositions. Since $\mathcal{N}(A^{\mathsf T}A)=\mathcal{N}(A)$, we have $\operatorname{rank}(A)=\operatorname{rank}(A^{\mathsf T}A)=\operatorname{rank}(AA^{\mathsf T})$, which we denote by $r$; so the eigenvalues of both are nonnegative, and each has $r$ positive eigenvalues (counted with multiplicity).

**Proposition 7.4.1** $A^{\mathsf T}A$ and $AA^{\mathsf T}$ have the same positive eigenvalues (with multiplicity), and their eigenvectors can be obtained from each other.

**Proof** Let $A^{\mathsf T}A\boldsymbol{x}=\lambda\boldsymbol{x}$ with $\lambda>0$ and $\boldsymbol{x}\neq\boldsymbol{0}$. Put $\boldsymbol{y}=A\boldsymbol{x}$; then $\boldsymbol{y}\neq\boldsymbol{0}$ (otherwise $\lambda\boldsymbol{x}=\boldsymbol{0}$), and $AA^{\mathsf T}\boldsymbol{y}=A(\lambda\boldsymbol{x})=\lambda\boldsymbol{y}$. Conversely, from $AA^{\mathsf T}\boldsymbol{y}=\lambda\boldsymbol{y}$ put $\boldsymbol{x}=A^{\mathsf T}\boldsymbol{y}$. The map $\boldsymbol{x}\mapsto A\boldsymbol{x}$ sends the **eigenspace** of $A^{\mathsf T}A$ for $\lambda$ injectively into the eigenspace of $AA^{\mathsf T}$ for $\lambda$, and vice versa, so the two eigenspaces have the same dimension; for symmetric matrices algebraic multiplicity equals geometric multiplicity, so the multiplicities agree too. $\square$

We extend eigenvalues and eigenvectors to rectangular matrices:

**Definition 7.4.1 (Singular Value)** Let $A$ be a real $m\times n$ matrix and $\sigma\ge0$. If there are nonzero vectors $\boldsymbol{x}\in\mathbb{R}^n$ and $\boldsymbol{y}\in\mathbb{R}^m$ such that $A\boldsymbol{x}=\sigma\boldsymbol{y}$ and $A^{\mathsf T}\boldsymbol{y}=\sigma\boldsymbol{x}$, then $\sigma$ is called a **singular value** of $A$, and $\boldsymbol{x}$ and $\boldsymbol{y}$ are called a **right singular vector** and a **left singular vector** of $A$ for $\sigma$.

In this case $A^{\mathsf T}A\boldsymbol{x}=\sigma^2\boldsymbol{x}$ and $AA^{\mathsf T}\boldsymbol{y}=\sigma^2\boldsymbol{y}$: right singular vectors are eigenvectors of $A^{\mathsf T}A$, left singular vectors are eigenvectors of $AA^{\mathsf T}$, and singular values are the nonnegative square roots of the corresponding eigenvalues.

**Theorem 7.4.1 (Singular Value Decomposition)** Let $A$ be a real $m\times n$ matrix with $\operatorname{rank}(A)=r$. Then there exist an orthogonal matrix $U$ of order $m$ and an orthogonal matrix $V$ of order $n$ such that $A=U\Sigma V^{\mathsf T}$, where

$$
\Sigma=\begin{bmatrix}\Sigma_r&O\\O&O\end{bmatrix}_{m\times n},\qquad \Sigma_r=\operatorname{diag}(\sigma_1,\dots,\sigma_r),\qquad \sigma_1\ge\sigma_2\ge\cdots\ge\sigma_r>0.
$$

The factorization $A=U\Sigma V^{\mathsf T}$ is called the singular value decomposition of $A$, or SVD for short.

**Proof** $A^{\mathsf T}A$ is symmetric positive semidefinite and has a spectral decomposition $A^{\mathsf T}A=V\Lambda V^{\mathsf T}$ with the eigenvalues in decreasing order; write $\Lambda=\operatorname{diag}(\Sigma_r^2,O)$, where $\Sigma_r$ has positive diagonal. Partition $V=[V_1\ V_2]$ with $V_1$ of size $n\times r$. Then

$$
V_1^{\mathsf T}A^{\mathsf T}AV_1=\Sigma_r^2,\qquad V_2^{\mathsf T}A^{\mathsf T}AV_2=O,
$$

and the latter says $\|AV_2\boldsymbol{z}\|^2=0$ for all $\boldsymbol{z}$, so $AV_2=O$. Let $U_1=AV_1\Sigma_r^{-1}$ ($m\times r$); then $U_1^{\mathsf T}U_1=\Sigma_r^{-1}V_1^{\mathsf T}A^{\mathsf T}AV_1\Sigma_r^{-1}=I_r$, that is, the columns of $U_1$ are orthonormal. Extend it to an orthogonal matrix $U=[U_1\ U_2]$; then

$$
U^{\mathsf T}AV=\begin{bmatrix}U_1^{\mathsf T}AV_1&U_1^{\mathsf T}AV_2\\U_2^{\mathsf T}AV_1&U_2^{\mathsf T}AV_2\end{bmatrix}=\begin{bmatrix}\Sigma_r&O\\O&O\end{bmatrix}=\Sigma,
$$

where $U_1^{\mathsf T}AV_1=\Sigma_r^{-1}V_1^{\mathsf T}A^{\mathsf T}AV_1=\Sigma_r$ and $U_2^{\mathsf T}AV_1=U_2^{\mathsf T}U_1\Sigma_r=O$. Hence $A=U\Sigma V^{\mathsf T}$. $\square$

Write $U=[\boldsymbol{u}_1\ \cdots\ \boldsymbol{u}_m]=[U_1\ U_2]$ and $V=[\boldsymbol{v}_1\ \cdots\ \boldsymbol{v}_n]=[V_1\ V_2]$. From the SVD we can read off:

- From $AV=U\Sigma$ and $A^{\mathsf T}U=V\Sigma^{\mathsf T}$ we get $A\boldsymbol{v}_i=\sigma_i\boldsymbol{u}_i$ and $A^{\mathsf T}\boldsymbol{u}_i=\sigma_i\boldsymbol{v}_i$: $\sigma_i$ are the singular values and $\boldsymbol{u}_i,\boldsymbol{v}_i$ the corresponding left and right singular vectors.
- The reduced singular value decomposition and the rank-one expansion:
  $$
  A=U_1\Sigma_rV_1^{\mathsf T}=\sigma_1\boldsymbol{u}_1\boldsymbol{v}_1^{\mathsf T}+\cdots+\sigma_r\boldsymbol{u}_r\boldsymbol{v}_r^{\mathsf T},
  $$
  where the left and right singular vectors determine each other: $U_1=AV_1\Sigma_r^{-1}$ and $V_1=A^{\mathsf T}U_1\Sigma_r^{-1}$.
- The four fundamental subspaces: $\boldsymbol{u}_1,\dots,\boldsymbol{u}_r$ is an orthonormal basis of the **column space** $\mathcal{R}(A)$, $\boldsymbol{v}_1,\dots,\boldsymbol{v}_r$ of the **row space** $\mathcal{R}(A^{\mathsf T})$, $\boldsymbol{u}_{r+1},\dots,\boldsymbol{u}_m$ of the **left null space** $\mathcal{N}(A^{\mathsf T})$, and $\boldsymbol{v}_{r+1},\dots,\boldsymbol{v}_n$ of the **null space** $\mathcal{N}(A)$. The SVD gives the best bases of all four subspaces at once, and $A$ maps the basis vectors $\boldsymbol{v}_i$ of the row space one by one to multiples $\sigma_i\boldsymbol{u}_i$ of the basis vectors of the column space.
- $A^{\mathsf T}A=V\Sigma^{\mathsf T}\Sigma V^{\mathsf T}$ and $AA^{\mathsf T}=U\Sigma\Sigma^{\mathsf T}U^{\mathsf T}$ are their spectral decompositions; the nonzero singular values of $A$ are the square roots of the nonzero eigenvalues of $A^{\mathsf T}A$ (or $AA^{\mathsf T}$).
- The singular values of a real symmetric matrix are the absolute values of its eigenvalues (in $A=Q\Lambda Q^{\mathsf T}$, move the signs of the negative eigenvalues onto columns of $U$), and those of a symmetric positive semidefinite matrix are its eigenvalues; orthogonally similar matrices have the same eigenvalues and the same singular values. If $A$ is invertible, then $A^{-1}=V\Sigma^{-1}U^{\mathsf T}$, and the singular values of $A^{-1}$ are the reciprocals of those of $A$.

Geometrically, $A=U\Sigma V^{\mathsf T}$ says that every linear map is the composition of a rotation (or reflection), a scaling along the coordinate axes, and another rotation: $A$ maps the unit sphere onto a (possibly degenerate) ellipsoid with semi-axes $\sigma_i\boldsymbol{u}_i$. The figure below uses the $2\times2$ matrix $\begin{bmatrix}3&0\\4&5\end{bmatrix}$ from Example 7.4.1 and applies $V^{\mathsf T}$, $\Sigma$, $U$ to the unit circle in turn: $V^{\mathsf T}$ rotates the right singular vectors $\boldsymbol{v}_1,\boldsymbol{v}_2$ onto the coordinate axes, $\Sigma$ stretches the axes by $\sigma_1,\sigma_2$, and $U$ rotates the axes onto the directions $\boldsymbol{u}_1,\boldsymbol{u}_2$.

![The geometry of the SVD: the unit circle undergoes the rotation V^T, the axis scaling Σ and the rotation U, yielding its image under A; the red and green arrows track v_1 and v_2, which end up as the semi-axes σ_1 u_1 and σ_2 u_2 of the ellipse (the first two panels are zoomed in)](./plots/svd-rotate-stretch-rotate.py)

**Algorithm 7.4.1 (Computing the Singular Value Decomposition)** Input: a real $m\times n$ matrix $A$.

1. Compute the spectral decomposition $A^{\mathsf T}A=V\Lambda V^{\mathsf T}$ with the eigenvalues in decreasing order, $\Lambda=\operatorname{diag}(\Sigma_r^2,O)$;
2. take $\Sigma_r$ to be the square roots of the positive eigenvalues, and $\Sigma=\begin{bmatrix}\Sigma_r&O\\O&O\end{bmatrix}_{m\times n}$;
3. partition $V=[V_1\ V_2]$ with $V_1$ of size $n\times r$;
4. let $U_1=AV_1\Sigma_r^{-1}$;
5. extend $U_1$ to an orthogonal matrix $U=[U_1\ U_2]$ (the columns of $U_2$ form an orthonormal basis of $\mathcal{N}(A^{\mathsf T})$).

If $m<n$, the same computation can be done with $AA^{\mathsf T}$ to reduce the size. This algorithm suits hand computation; numerically one should not form $A^{\mathsf T}A$ explicitly, since that squares the condition number and loses accuracy in the small singular values. Practical algorithms (Golub–Kahan bidiagonalization) apply orthogonal transformations directly to $A$, at a cost of $O(mn^2)$ ($m\ge n$).

**Example 7.4.1** Find the singular value decomposition of $A=\begin{bmatrix}3&0\\4&5\\0&0\end{bmatrix}$. We have $A^{\mathsf T}A=\begin{bmatrix}25&20\\20&25\end{bmatrix}$ with eigenvalues $45,5$ and eigenvectors $\boldsymbol{v}_1=\frac1{\sqrt2}[1\ 1]^{\mathsf T}$, $\boldsymbol{v}_2=\frac1{\sqrt2}[-1\ 1]^{\mathsf T}$. So $\sigma_1=3\sqrt5$, $\sigma_2=\sqrt5$, and

$$
U_1=AV\Sigma_r^{-1}=\begin{bmatrix}3&0\\4&5\\0&0\end{bmatrix}\begin{bmatrix}\frac1{\sqrt2}&-\frac1{\sqrt2}\\\frac1{\sqrt2}&\frac1{\sqrt2}\end{bmatrix}\begin{bmatrix}\frac{1}{3\sqrt5}&\\&\frac1{\sqrt5}\end{bmatrix}=\begin{bmatrix}\frac1{\sqrt{10}}&-\frac3{\sqrt{10}}\\\frac3{\sqrt{10}}&\frac1{\sqrt{10}}\\0&0\end{bmatrix}.
$$

Adding $\boldsymbol{u}_3=\boldsymbol{e}_3$ gives $U=[U_1\ \boldsymbol{e}_3]$, $\Sigma=\begin{bmatrix}3\sqrt5&0\\0&\sqrt5\\0&0\end{bmatrix}$ and $A=U\Sigma V^{\mathsf T}$. The left panel of the figure below shows the $2\times2$ matrix formed by the first two rows of $A$ (which has the same singular values and singular vectors) mapping the unit circle onto an ellipse.

![Left: A maps the unit circle onto an ellipse with semi-axes σ_i u_i. Right: the relative error of the truncated SVD of an 80×60 matrix as a function of the rank k](./plots/svd-geometry-low-rank.py)

The SVD is the most widely used matrix factorization in data analysis. The terms of the rank-one expansion are ordered by decreasing $\sigma_i$, and truncating after $k$ terms gives the best rank-$k$ approximation of $A$ (Theorem 7.6.2), the basis of "low-rank models" in image compression, denoising and recommender systems. For a centered data matrix, the right singular vectors are the principal component directions; the number of singular values that are not negligible compared with the others measures the numerical rank; and the pseudoinverse of the next section handles all kinds of linear systems and least squares problems in a unified way.

## 7.5. The Moore–Penrose Pseudoinverse

**Definition 7.5.1 (Moore–Penrose Pseudoinverse)** Let $A\in\mathbb{R}^{m\times n}$ with $\operatorname{rank}(A)=r$ have the reduced singular value decomposition $A=U_r\Sigma_rV_r^{\mathsf T}$. The matrix

$$
A^+=V_r\Sigma_r^{-1}U_r^{\mathsf T}\in\mathbb{R}^{n\times m}
$$

is called the **Moore–Penrose pseudoinverse** of $A$, or simply its pseudoinverse (or generalized inverse). (For $A=O$ we set $A^+=O$.)

From $U_r^{\mathsf T}U_r=V_r^{\mathsf T}V_r=I_r$ we obtain at once:

- $AA^+=U_rU_r^{\mathsf T}$ is the matrix of the **orthogonal projection** onto $\mathcal{R}(A)$, and $I-AA^+$ that of the orthogonal projection onto $\mathcal{N}(A^{\mathsf T})$;
- $A^+A=V_rV_r^{\mathsf T}$ is the matrix of the orthogonal projection onto $\mathcal{R}(A^{\mathsf T})$, and $I-A^+A$ that of the orthogonal projection onto $\mathcal{N}(A)$;
- if $A$ is invertible, $A^+=A^{-1}$; if $A$ has full column rank, $A^+=(A^{\mathsf T}A)^{-1}A^{\mathsf T}$; if $A$ has full row rank, $A^+=A^{\mathsf T}(AA^{\mathsf T})^{-1}$.

$A^+$ does not depend on the choice of SVD: it is the unique matrix $X$ satisfying the Penrose conditions

$$
AXA=A,\qquad XAX=X,\qquad (AX)^{\mathsf T}=AX,\qquad (XA)^{\mathsf T}=XA
$$

(that $A^+$ satisfies them follows directly from the projection properties above; if $X_1,X_2$ both satisfy them, then $AX_1=AX_2$ are both the orthogonal projection onto $\mathcal{R}(A)$ and $X_1A=X_2A$ are both the orthogonal projection onto $\mathcal{R}(A^{\mathsf T})$, whence $X_1=X_1AX_1=X_2AX_1=X_2AX_2=X_2$).

**Theorem 7.5.1** For the linear system $A\boldsymbol{x}=\boldsymbol{b}$, $\boldsymbol{x}^+=A^+\boldsymbol{b}$ is the **least squares** solution of minimum length: the set of all least squares solutions is $\{A^+\boldsymbol{b}+\boldsymbol{x}_0\mid\boldsymbol{x}_0\in\mathcal{N}(A)\}$, and $\|A^+\boldsymbol{b}+\boldsymbol{x}_0\|^2=\|A^+\boldsymbol{b}\|^2+\|\boldsymbol{x}_0\|^2$. In particular, if the system is consistent, $A^+\boldsymbol{b}$ is its solution of minimum length; if $A$ is invertible, it is the unique solution.

**Proof** $AA^+\boldsymbol{b}$ is the orthogonal projection of $\boldsymbol{b}$ onto $\mathcal{R}(A)$, so $A^+\boldsymbol{b}$ is a least squares solution. Equivalently, $(I-AA^+)\boldsymbol{b}\in\mathcal{N}(A^{\mathsf T})$ gives $A^{\mathsf T}A(A^+\boldsymbol{b})=A^{\mathsf T}\boldsymbol{b}$, that is, $A^+\boldsymbol{b}$ satisfies the **normal equations** (some textbooks call solving the normal equations the "regularization method"; this has nothing to do with regularization in statistics). The solution set of the normal equations is a particular solution plus $\mathcal{N}(A^{\mathsf T}A)=\mathcal{N}(A)$. Finally $A^+\boldsymbol{b}=V_r(\cdots)\in\mathcal{R}(A^{\mathsf T})\perp\mathcal{N}(A)$, and the Pythagorean theorem gives the length formula. If the system is consistent, its least squares solutions are exactly its solutions. $\square$

## 7.6. The Spectral Norm and Stability of Singular Values

The Rayleigh quotient of $A^{\mathsf T}A$ is $\dfrac{\boldsymbol{x}^{\mathsf T}A^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}=\dfrac{\|A\boldsymbol{x}\|^2}{\|\boldsymbol{x}\|^2}$, which measures the factor by which $A$ stretches a vector. By Theorem 7.2.1, its extreme values are squares of singular values.

**Definition 7.6.1 (Spectral Norm)** For a real $m\times n$ matrix $A$, the nonnegative number

$$
\|A\|=\max_{\boldsymbol{x}\neq\boldsymbol{0}}\frac{\|A\boldsymbol{x}\|}{\|\boldsymbol{x}\|}=\max_{\|\boldsymbol{x}\|=1}\|A\boldsymbol{x}\|
$$

is called the **spectral norm** of $A$.

By definition, $\|A\boldsymbol{x}\|\le\|A\|\|\boldsymbol{x}\|$ for every $\boldsymbol{x}$ (compatibility), and there is a unit vector $\boldsymbol{x}_0$ with $\|A\|=\|A\boldsymbol{x}_0\|$ (the unit sphere is closed and bounded); an orthogonal matrix $Q$ has $\|Q\|=1$.

**Proposition 7.6.1** Let the singular values of $A$ (padded with zeros to $n$ values) be $\sigma_1\ge\cdots\ge\sigma_n\ge0$, with corresponding right singular vectors $\boldsymbol{v}_1,\dots,\boldsymbol{v}_n$ forming an orthonormal basis of $\mathbb{R}^n$. Then

$$
\sigma_i=\max_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{v}_i,\dots,\boldsymbol{v}_n)}}\frac{\|A\boldsymbol{x}\|}{\|\boldsymbol{x}\|}=\min_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{v}_1,\dots,\boldsymbol{v}_i)}}\frac{\|A\boldsymbol{x}\|}{\|\boldsymbol{x}\|}.
$$

In particular, the spectral norm equals the largest singular value, $\|A\|=\sigma_1$, the square root of the largest eigenvalue of $A^{\mathsf T}A$; and $\sigma_n=\min\limits_{\boldsymbol{x}\neq\boldsymbol{0}}\|A\boldsymbol{x}\|/\|\boldsymbol{x}\|$.

**Proof** Apply Theorem 7.2.1 to $A^{\mathsf T}A$ (eigenvalues $\sigma_1^2\ge\cdots\ge\sigma_n^2$, eigenvectors $\boldsymbol{v}_i$) and take square roots. $\square$

For an invertible matrix $A$ of order $n$, the largest singular value of $A^{-1}$ is $1/\sigma_n$, so $\|A^{-1}\|=1/\sigma_n$. The number $\kappa(A)=\|A\|\|A^{-1}\|=\sigma_1/\sigma_n\ge1$ is called the *condition number* of $A$. It measures error amplification in solving linear systems: if $A\boldsymbol{x}=\boldsymbol{b}$ and $A(\boldsymbol{x}+\delta\boldsymbol{x})=\boldsymbol{b}+\delta\boldsymbol{b}$, then $\|\boldsymbol{b}\|\le\|A\|\|\boldsymbol{x}\|$ and $\|\delta\boldsymbol{x}\|\le\|A^{-1}\|\|\delta\boldsymbol{b}\|$ give

$$
\frac{\|\delta\boldsymbol{x}\|}{\|\boldsymbol{x}\|}\le\kappa(A)\frac{\|\delta\boldsymbol{b}\|}{\|\boldsymbol{b}\|}.
$$

An orthogonal matrix has condition number $1$, which is why the orthogonal transformations of [Chapter 4](/2.1.4) are numerically stable; and $\kappa(A^{\mathsf T}A)=\kappa(A)^2$, so solving the normal equations directly loses accuracy more easily than using the QR decomposition.

**Proposition 7.6.2** The spectral norm satisfies:

1. positivity: $\|A\|\ge0$, with $\|A\|=0$ if and only if $A=O$;
2. homogeneity: $\|kA\|=|k|\|A\|$;
3. the triangle inequality: $\|A+B\|\le\|A\|+\|B\|$;
4. submultiplicativity: $\|AB\|\le\|A\|\|B\|$;
5. orthogonal invariance: if $U,V$ are orthogonal matrices, then $\|UAV^{\mathsf T}\|=\|A\|$.

**Proof** 1 and 2 follow directly from the definition. 3: take a unit vector $\boldsymbol{x}_0$ with $\|A+B\|=\|(A+B)\boldsymbol{x}_0\|$; then $\|A+B\|\le\|A\boldsymbol{x}_0\|+\|B\boldsymbol{x}_0\|\le\|A\|+\|B\|$. 4: take a unit vector $\boldsymbol{x}_0$ with $\|AB\|=\|AB\boldsymbol{x}_0\|$; then $\|AB\|\le\|A\|\|B\boldsymbol{x}_0\|\le\|A\|\|B\|$. 5: by 4, $\|UAV^{\mathsf T}\|\le\|U\|\|A\|\|V^{\mathsf T}\|=\|A\|$; and since $A=U^{\mathsf T}(UAV^{\mathsf T})V$, likewise $\|A\|\le\|UAV^{\mathsf T}\|$. $\square$

**Definition 7.6.2 (Matrix Norm)** A function $\|\cdot\|\colon \mathbb{R}^{m\times n}\to\mathbb{R}$ satisfying conditions 1–4 of Proposition 7.6.2 (condition 4 for every pair of conformable matrices) is called a **matrix norm**.

Another commonly used matrix norm is the *Frobenius norm* $\|A\|_{\mathrm{F}}=\sqrt{\operatorname{tr}(A^{\mathsf T}A)}=\sqrt{\sum_{i,j}a_{ij}^2}$. By the orthogonal invariance of the **trace**, $\|A\|_{\mathrm{F}}^2=\operatorname{tr}(\Sigma^{\mathsf T}\Sigma)=\sigma_1^2+\cdots+\sigma_r^2$, so $\|A\|\le\|A\|_{\mathrm{F}}\le\sqrt r\,\|A\|$.

**Theorem 7.6.1 (Stability of Singular Values)** Let $A,\tilde A$ be real matrices of the same size with singular values $\sigma_1\ge\sigma_2\ge\cdots$ and $\tilde\sigma_1\ge\tilde\sigma_2\ge\cdots$ respectively. Then $|\tilde\sigma_i-\sigma_i|\le\|\tilde A-A\|$.

The proof of this inequality (Weyl's inequality) requires the Courant–Fischer minimax principle and is omitted here. It says that singular values are well-conditioned: they change by at most as much as the matrix does. Eigenvalues behave differently.

**Example 7.6.1 (Singular Values Versus Eigenvalues)** Let $J_n(0)$ be the Jordan block of order $n$ (zero diagonal, ones on the superdiagonal). Then $J_n(0)^{\mathsf T}J_n(0)=\operatorname{diag}(0,1,\dots,1)$, so $J_n(0)$ has the $n$-fold eigenvalue $0$ and singular values $1$ ($n-1$ times) and $0$ (once). Changing the $(n,1)$ entry of $J_n(0)$ to $10^{-n}$ gives $\tilde J$ with $\|\tilde J-J_n(0)\|=10^{-n}$. Now $\tilde J^{\mathsf T}\tilde J=\operatorname{diag}(10^{-2n},1,\dots,1)$, so the singular values are $1$ ($n-1$ times) and $10^{-n}$, a change of exactly $10^{-n}$; but the characteristic polynomial is $\lambda^n-10^{-n}$, with eigenvalues $10^{-1}\mathrm{e}^{2\pi\mathrm{i}j/n}$ ($j=1,\dots,n$), a change of $10^{-1}$, which is $10^{n-1}$ times the perturbation. In general the change of the eigenvalues can only be bounded as $|\tilde\lambda_i-\lambda_i|\le C_A\|\tilde A-A\|^{1/n}$, where $C_A$ is a constant depending on $A,\tilde A$; this is why eigenvalues are said to be ill-conditioned. Symmetric matrices are the exception: if $A,\tilde A$ are both real symmetric with eigenvalues in decreasing order, then likewise $|\tilde\lambda_i-\lambda_i|\le\|\tilde A-A\|$ (also a consequence of the minimax principle), so the eigenvalue problem for real symmetric matrices is well-conditioned.

The extremal characterization of singular values also answers the question "how well can $A$ be approximated by a matrix of low rank?"

**Theorem 7.6.2 (Eckart–Young Theorem)** Let $A$ have the SVD $A=\sum_{i=1}^r\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$, let $0\le k<r$, and let $A_k=\sum_{i=1}^k\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$. Then

$$
\min_{\operatorname{rank}(B)\le k}\|A-B\|=\|A-A_k\|=\sigma_{k+1}.
$$

**Proof** The largest singular value of $A-A_k=\sum_{i=k+1}^r\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$ is $\sigma_{k+1}$. On the other hand, if $\operatorname{rank}(B)\le k$, then $\dim\mathcal{N}(B)\ge n-k$, and its dimension plus that of the $(k+1)$-dimensional subspace $\operatorname{span}(\boldsymbol{v}_1,\dots,\boldsymbol{v}_{k+1})$ exceeds $n$, so they share a unit vector $\boldsymbol{x}$. By Proposition 7.6.1, $\|A-B\|\ge\|(A-B)\boldsymbol{x}\|=\|A\boldsymbol{x}\|\ge\sigma_{k+1}$. $\square$

The same conclusion holds for the Frobenius norm, with error $\sqrt{\sigma_{k+1}^2+\cdots+\sigma_r^2}$. The right panel of the figure in §7.4 plots the truncation error for an $80\times60$ matrix whose singular values decay geometrically: storing $A_k$ takes only $k(m+n+1)$ numbers, while the error decreases rapidly with $k$. This is the principle of low-rank compression.

## Summary

The thread of this chapter is "simplification by orthogonal matrices": a real symmetric matrix reduces to a diagonal matrix under orthogonal similarity, a quadratic form reduces to a sum of squares under congruence, and an arbitrary matrix reduces to a diagonal matrix under two orthogonal transformations, one on each side.

| Topic | Core results | Computation |
|---|---|---|
| Spectral decomposition | Real symmetric $A=Q\Lambda Q^{\mathsf T}=\sum\lambda_i\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf T}$; a real square matrix is orthogonally similar to a diagonal matrix ⇔ it is symmetric | Algorithm 7.1.1: eigenvalues + Gram–Schmidt within each eigenspace |
| Rayleigh quotient | $\lambda_1=\max\frac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$, $\lambda_n=\min$; $\lambda_i$ is the extreme value on an orthogonal complement | Orthogonal substitution $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{x}$ |
| Positive definite matrices | Six equivalent conditions: definition, eigenvalues, $T^{\mathsf T}T$, $LDL^{\mathsf T}$, leading principal minors, leading principal submatrices | Cholesky (Algorithm 7.3.1), $\frac13n^3$, doubles as a test |
| Semidefinite, indefinite | Nonnegative eigenvalues ⇔ $T^{\mathsf T}T$ ⇔ $D\ge0$; nonnegative leading principal minors are not enough; indefinite ⇒ some nonzero $\boldsymbol{z}$ has $\boldsymbol{z}^{\mathsf T}A\boldsymbol{z}=0$ | — |
| Congruence | $X^{\mathsf T}AX$; canonical form $\operatorname{diag}(I_p,-I_{r-p},O)$; law of inertia: $(p,r-p,n-r)$ is a complete invariant | Completing squares or spectral decomposition |
| Singular value decomposition | $A=U\Sigma V^{\mathsf T}=\sum\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$; singular vectors are orthonormal bases of the four fundamental subspaces | Algorithm 7.4.1: spectral decomposition of $A^{\mathsf T}A$ + $U_1=AV_1\Sigma_r^{-1}$ |
| Pseudoinverse | $A^+=V_r\Sigma_r^{-1}U_r^{\mathsf T}$; $AA^+$, $A^+A$ are orthogonal projections; $A^+\boldsymbol{b}$ is the minimum-length least squares solution | From the SVD |
| Spectral norm | $\Vert A\Vert=\sigma_1$; orthogonally invariant; singular values are well-conditioned ($\vert\tilde\sigma_i-\sigma_i\vert\le\Vert\tilde A-A\Vert$), eigenvalues in general ill-conditioned | — |
| Low-rank approximation | $\min_{\operatorname{rank}(B)\le k}\Vert A-B\Vert=\sigma_{k+1}$, attained by the truncated SVD | Truncated SVD |

A comparison of the equivalence relations:

| Relation | Definition | Canonical form | Complete invariant |
|---|---|---|---|
| Equivalence | $PAQ=B$, $P,Q$ invertible | $\operatorname{diag}(I_r,O)$ | Rank |
| Similarity | $P^{-1}AP=B$, $P$ invertible | Jordan canonical form ([Chapter 10](/2.1.10)) | Eigenvalues and Jordan block structure |
| Orthogonal similarity (real symmetric) | $Q^{\mathsf T}AQ=B$, $Q$ orthogonal | $\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ | Eigenvalues |
| Congruence (real symmetric) | $X^{\mathsf T}AX=B$, $X$ invertible | $\operatorname{diag}(I_p,-I_{r-p},O)$ | Inertia |
