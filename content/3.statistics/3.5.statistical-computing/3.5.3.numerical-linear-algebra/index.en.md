---
title: Numerical Linear Algebra
description: How linear systems, least squares problems and eigenvalue problems are solved on a computer — LU and Cholesky factorizations with pivoting, projectors, QR by Gram–Schmidt, Householder and Givens, the SVD and its applications, the power method and the Schur form — with operation counts and stability.
---

Almost every statistical computation ends in linear algebra: a regression fit solves a **least squares** problem, a Gaussian likelihood needs a determinant and a quadratic form in an inverse covariance matrix, principal components are eigenvectors, and every Newton step of [3.5.5](/3.5.5) solves a linear system. The theory of these problems was developed in linear algebra ([2.1](/2.1)): the **LU decomposition** in [2.1.2](/2.1.2), orthogonality and the **QR decomposition** in [2.1.4](/2.1.4), eigenvalues in [2.1.6](/2.1.6), the **Cholesky decomposition** and the **singular value decomposition** in [2.1.7](/2.1.7), the Jordan and Schur forms in [2.1.10](/2.1.10) and [2.1.12](/2.1.12). This chapter looks at the same factorizations as algorithms: how they are computed, how many floating-point operations they cost, and how rounding errors ([3.5.1](/3.5.1)) propagate through them. It has three parts, following the three basic problems: linear systems $A\boldsymbol{x}=\boldsymbol{b}$ (Gaussian elimination, pivoting, Cholesky), least squares problems $A\boldsymbol{x}\approx\boldsymbol{b}$ (projectors, three ways to compute a QR decomposition, the SVD) and eigenvalue problems $A\boldsymbol{x}=\lambda\boldsymbol{x}$ (the power method and the eigenvalue-revealing factorizations). The guiding principle is that there is no best algorithm, only the most suitable one for the problem at hand: speed, stability and generality pull in different directions. The R functions `solve`, `chol`, `qr`, `svd` and `eigen` used throughout call LINPACK and LAPACK routines that implement the algorithms below.

## 3.1. Linear Systems

### 3.1.1. Matrix Multiplication

Let $A\in\mathbb{C}^{m\times n}$ have columns $\boldsymbol{a}_1,\dots,\boldsymbol{a}_n$. The product with a vector is a linear combination of the columns:

$$
\boldsymbol{b}=A\boldsymbol{x}=\sum_{j=1}^n x_j\boldsymbol{a}_j .
$$
Likewise $\boldsymbol{x}^{\mathsf T}A$ is a linear combination of the rows of $A$. For $B\in\mathbb{C}^{n\times p}$ with rows $\boldsymbol{b}_{(1)}^{\mathsf T},\dots,\boldsymbol{b}_{(n)}^{\mathsf T}$, the product is a sum of outer products,

$$
AB=\begin{bmatrix}\boldsymbol{a}_1&\cdots&\boldsymbol{a}_n\end{bmatrix}\begin{bmatrix}\boldsymbol{b}_{(1)}^{\mathsf T}\\ \vdots\\ \boldsymbol{b}_{(n)}^{\mathsf T}\end{bmatrix}=\sum_{j=1}^n\boldsymbol{a}_j\boldsymbol{b}_{(j)}^{\mathsf T},
$$
and each term $\boldsymbol{a}_j\boldsymbol{b}_{(j)}^{\mathsf T}$ is an $m\times p$ matrix of rank one. This view underlies the vectorized implementations below, where a whole submatrix is updated by one outer product.

If $A$ is square and nonsingular, $\boldsymbol{x}=A^{-1}\boldsymbol{b}$ is the unique vector with $A\boldsymbol{x}=\boldsymbol{b}$: it is the vector of coefficients of the expansion of $\boldsymbol{b}$ in the basis of columns of $A$. Multiplication by $A^{-1}$ is therefore a change of basis: it converts the coefficients of $\boldsymbol{b}$ in the standard basis into its coefficients in the basis $\boldsymbol{a}_1,\dots,\boldsymbol{a}_n$, and multiplication by $A$ converts back.

The best-behaved change of basis is the one by a **unitary matrix** $Q$, $Q^{\mathsf H}=Q^{-1}$ (in the real case an **orthogonal matrix**, $Q^{\mathsf T}=Q^{-1}$). Its eigenvalues have modulus $1$, eigenvectors for different eigenvalues are orthogonal, and multiplication by $Q$ or $Q^{\mathsf H}$ preserves inner products, hence lengths and angles: in the real case it is a rigid rotation ($\det Q=1$) or a reflection ($\det Q=-1$).

**Theorem 3.1.1 (Unitary Invariance)** For any $A\in\mathbb{C}^{m\times n}$ and unitary $Q\in\mathbb{C}^{m\times m}$,

$$
\|QA\|_2=\|A\|_2\triangleq\sup_{\boldsymbol{x}\ne\boldsymbol{0}}\frac{\|A\boldsymbol{x}\|_2}{\|\boldsymbol{x}\|_2},\qquad \|QA\|_{\mathrm{F}}=\|A\|_{\mathrm{F}}\triangleq\Bigl(\sum_{i=1}^m\sum_{j=1}^n\lvert a_{ij}\rvert^2\Bigr)^{1/2}.
$$

**Proof** $\|QA\boldsymbol{x}\|_2=\|A\boldsymbol{x}\|_2$ for every $\boldsymbol{x}$, which gives the first identity. For the second, $\|A\|_{\mathrm{F}}^2=\operatorname{tr}(A^{\mathsf H}A)=\sum_j\boldsymbol{a}_j^{\mathsf H}\boldsymbol{a}_j$, and $(QA)^{\mathsf H}(QA)=A^{\mathsf H}A$. $\square$

This invariance is why algorithms built from orthogonal transformations (QR, SVD) do not amplify rounding errors, while algorithms built from general triangular transformations may.

### 3.1.2. Triangular Systems

Assume $A\in\mathbb{C}^{m\times m}$ is nonsingular, so that $A\boldsymbol{x}=\boldsymbol{b}$ has the unique solution $\boldsymbol{x}=A^{-1}\boldsymbol{b}$. Computing $A^{-1}$ explicitly and multiplying is wasteful (about three times the work of the method below) and less accurate; Cramer's rule $x_j=\det A_j/\det A$ is even more expensive. The key observation is that triangular systems are trivial. If $L$ is lower triangular, $L\boldsymbol{x}=\boldsymbol{b}$ is solved by *forward substitution*, computing $x_1,x_2,\dots$ in turn; if $U$ is upper triangular, $U\boldsymbol{x}=\boldsymbol{b}$ is solved by *back substitution*, from $x_m$ upwards:

$$
x_i=\frac1{l_{ii}}\Bigl(b_i-\sum_{j<i}l_{ij}x_j\Bigr),\qquad x_i=\frac1{u_{ii}}\Bigl(b_i-\sum_{j>i}u_{ij}x_j\Bigr).
$$

```r
for_sub <- function(L, b) {
  n <- length(b)
  x <- rep(0, n)
  x[1] <- b[1] / L[1, 1]
  for (i in 2:n) {
    tmp <- b[i]
    for (j in 1:(i - 1)) tmp <- tmp - L[i, j] * x[j]
    x[i] <- tmp / L[i, i]
  }
  return(x)
}

back_sub <- function(U, b) {
  n <- length(b)
  x <- rep(0, n)
  for (i in n:1) {
    tmp <- b[i]
    for (j in i:n) tmp <- tmp - U[i, j] * x[j]   # x[i] is still 0 here
    x[i] <- tmp / U[i, i]
  }
  return(x)
}
```

Row $k$ costs about $2k$ operations, so each triangular solve takes $\sum_{k=1}^m2k\sim m^2$ flops (base R has the compiled versions `forwardsolve` and `backsolve`). The strategy for a general $A$ is to factor it into triangular matrices.

### 3.1.3. Gaussian Elimination and the LU Decomposition

**Definition 3.1.1 (Gaussian Elimination)** **Gaussian elimination** transforms a square system into an upper triangular one by applying simple linear transformations on the left: at step $k$, for each $j>k$, a multiple $l_{jk}=x_{jk}/x_{kk}$ of row $k$ is subtracted from row $j$, where $x_{jk}$ denote the entries of the matrix at the beginning of step $k$ and $x_{kk}$ is the **pivot**. In matrix form, $L_{m-1}\cdots L_2L_1A=U$ with

$$
L_k=I-\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T},\qquad \boldsymbol{\ell}_k=(0,\dots,0,l_{k+1,k},\dots,l_{mk})^{\mathsf T}.
$$
Setting $L=L_1^{-1}L_2^{-1}\cdots L_{m-1}^{-1}$ gives the **LU decomposition** $A=LU$ with $L$ unit lower triangular and $U$ upper triangular.

**Example 3.1.1** For

$$
A=\begin{bmatrix}2&1&1&0\\4&3&3&1\\8&7&9&5\\6&7&9&8\end{bmatrix},\qquad L_1A=\begin{bmatrix}1&&&\\-2&1&&\\-4&&1&\\-3&&&1\end{bmatrix}A=\begin{bmatrix}2&1&1&0\\&1&1&1\\&3&5&5\\&4&6&8\end{bmatrix},
$$
then $L_2=\begin{bmatrix}1&&&\\&1&&\\&-3&1&\\&-4&&1\end{bmatrix}$ and $L_3=\begin{bmatrix}1&&&\\&1&&\\&&1&\\&&-1&1\end{bmatrix}$ finish the elimination:

$$
A=\begin{bmatrix}1&&&\\2&1&&\\4&3&1&\\3&4&1&1\end{bmatrix}\begin{bmatrix}2&1&1&0\\&1&1&1\\&&2&2\\&&&2\end{bmatrix}=LU .
$$

The factor $L$ is obtained without any computation, thanks to two "strokes of luck".

**Proposition 3.1.1 (Two Strokes of Luck)** (a) $L_k^{-1}=I+\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T}$ is obtained from $L_k$ by negating its subdiagonal entries. (b) $L=L_1^{-1}\cdots L_{m-1}^{-1}$ is the unit lower triangular matrix with the multipliers $l_{jk}$ inserted in the appropriate places.

**Proof** (a) $(I-\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T})(I+\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T})=I-\boldsymbol{\ell}_k(\boldsymbol{e}_k^{\mathsf T}\boldsymbol{\ell}_k)\boldsymbol{e}_k^{\mathsf T}=I$, since the $k$-th entry of $\boldsymbol{\ell}_k$ is zero. (b) Similarly $\boldsymbol{e}_k^{\mathsf T}\boldsymbol{\ell}_{k'}=0$ for $k<k'$, so all cross terms in the product vanish and $L=I+\sum_k\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T}$. $\square$

**Algorithm 3.1.1 (Gaussian Elimination without Pivoting)** Set $U=A$, $L=I$. For $k=1,\dots,m-1$: for $j=k+1,\dots,m$, set $l_{jk}=u_{jk}/u_{kk}$ and $u_{j,k:m}=u_{j,k:m}-l_{jk}u_{k,k:m}$. In vectorized form, step $k$ computes the column of multipliers $\boldsymbol{l}=u_{(k+1):m,k}/u_{kk}$ and updates the trailing submatrix by one outer product, $u_{(k+1):m,k:m}\leftarrow u_{(k+1):m,k:m}-\boldsymbol{l}\,u_{k,k:m}$.

```r
# Input: a square matrix A whose leading principal minors are nonzero
# Output: unit lower triangular L and upper triangular U with A = LU
lu <- function(A) {
  m <- nrow(A)
  if (ncol(A) != m) stop("A must be square")
  L <- diag(m)
  U <- as.matrix(A)
  for (k in 1:(m - 1)) {
    multiplier <- U[(k + 1):m, k] / U[k, k]          # (m-k) x 1
    L[(k + 1):m, k] <- multiplier
    # outer product update: (m-k) x 1 times 1 x (m-k+1)
    U[(k + 1):m, k:m] <- U[(k + 1):m, k:m] - multiplier %*% U[k, k:m, drop = FALSE]
  }
  return(list(L = L, U = U))
}

A <- matrix(c(2, 1, 1, 0,
              4, 3, 3, 1,
              8, 7, 9, 5,
              6, 7, 9, 8), nrow = 4, byrow = TRUE)
out <- lu(A)
out$L %*% out$U    # equals A
```

How long does an algorithm take? No answer is both easy and comprehensive; the classical measure counts floating-point operations.

**Definition 3.1.2 (Flop)** A **flop** (floating-point operation) is one addition, subtraction, multiplication, division or square root of floating-point numbers. Flop counts make no distinction between real and complex arithmetic and ignore memory access and other aspects of performance; they are reported by their leading term, where $f\sim g$ means $f/g\to1$ as the dimensions tend to infinity.

Most of the work of Algorithm 3.1.1 is the update $u_{j,k:m}=u_{j,k:m}-l_{jk}u_{k,k:m}$: one multiplication and one subtraction for each of $m-k+1$ entries. Hence the total is

$$
\sum_{k=1}^{m-1}\sum_{j=k+1}^m2(m-k+1)=\sum_{k=1}^{m-1}2(m-k+1)(m-k)\sim\frac23m^3\ \text{flops}.
$$
Once $A=LU$ is known, $A\boldsymbol{x}=\boldsymbol{b}$ becomes $LU\boldsymbol{x}=\boldsymbol{b}$: solve $L\boldsymbol{y}=\boldsymbol{b}$ by forward substitution and then $U\boldsymbol{x}=\boldsymbol{y}$ by back substitution, $\sim2m^2$ flops in all. The total work is dominated by the factorization, $\sim\frac23m^3$ flops, and the factorization can be reused for many right-hand sides.

**Remark 3.1.1** A nonsingular $A$ has an LU decomposition with unit lower triangular $L$ (and then a unique one) if and only if all its **leading principal minors** of orders $1,\dots,m-1$ are nonzero ([2.1.2](/2.1.2)); otherwise some pivot $u_{kk}$ vanishes. This is the motivation for pivoting.

### 3.1.4. Pivoting

Gaussian elimination without pivoting is not only inapplicable for some matrices; it is unstable. The matrix

$$
A=\begin{bmatrix}0&1\\1&1\end{bmatrix}
$$
has full rank and is well-conditioned (its singular values, `svd(A)$d`, are $1.618$ and $0.618$), yet elimination fails at the first step. A slight perturbation reveals the general problem:

$$
A=\begin{bmatrix}10^{-20}&1\\1&1\end{bmatrix}\ \Longrightarrow\ L=\begin{bmatrix}1&0\\10^{20}&1\end{bmatrix},\quad U=\begin{bmatrix}10^{-20}&1\\0&1-10^{20}\end{bmatrix}.
$$
In double precision $1-10^{20}$ rounds to $-10^{20}$ (in R, `1 - 10^20 == -10^20` is `TRUE`, while `1 - 10^10 == -10^10` is `FALSE`), so the computer stores

$$
\tilde L=\begin{bmatrix}1&0\\10^{20}&1\end{bmatrix},\quad \tilde U=\begin{bmatrix}10^{-20}&1\\0&-10^{20}\end{bmatrix},\qquad \tilde L\tilde U=\begin{bmatrix}10^{-20}&1\\1&0\end{bmatrix}.
$$
Both factors were computed with tiny relative errors, but their product has lost the $(2,2)$ entry of $A$ completely: the tiny pivot produced huge entries in $L$ and $U$, and the rounding error in a huge entry is as large as an entry of $A$. The algorithm is not backward stable.

**Definition 3.1.3 (Partial Pivoting)** In Gaussian elimination with **partial pivoting**, at step $k$ the entry of largest modulus in column $k$ on or below the diagonal, $\lvert u_{ik}\rvert=\max_{j\ge k}\lvert u_{jk}\rvert$, is chosen as the pivot, and rows $i$ and $k$ are interchanged before the elimination. Only rows are interchanged; with permutation matrices $P_k$,

$$
L_{m-1}P_{m-1}\cdots L_2P_2L_1P_1A=U .
$$
In **complete pivoting** the pivot is the entry of largest modulus in the whole trailing submatrix, and rows and columns are both permuted, $L_{m-1}P_{m-1}\cdots L_1P_1AC_1\cdots C_{m-1}=U$, that is, $PAC=LU$.

With partial pivoting all multipliers satisfy $\lvert l_{jk}\rvert\le1$. The permutations can be moved to the right, which is the third stroke of luck:

$$
L_{m-1}P_{m-1}\cdots L_2P_2L_1P_1=L'_{m-1}\cdots L'_2L'_1\,P_{m-1}\cdots P_2P_1,\qquad L'_k=P_{m-1}\cdots P_{k+1}L_kP_{k+1}^{-1}\cdots P_{m-1}^{-1}.
$$
For example, $L_3P_3L_2P_2L_1P_1=L'_3L'_2L'_1P_3P_2P_1$ with $L'_3=L_3$, $L'_2=P_3L_2P_3^{-1}$, $L'_1=P_3P_2L_1P_2^{-1}P_3^{-1}$. Since $P_{k+1},\dots,P_{m-1}$ only permute rows and columns with indices greater than $k$, each $L'_k$ has the same structure as $L_k$, with its subdiagonal entries permuted. Writing $L^{-1}=L'_{m-1}\cdots L'_1$ and $P=P_{m-1}\cdots P_1$ we obtain the factorization

$$
PA=LU .
$$

**Algorithm 3.1.2 (Gaussian Elimination with Partial Pivoting)** Set $U=A$, $L=I$, $P=I$. For $k=1,\dots,m-1$: select $i\ge k$ to maximize $\lvert u_{ik}\rvert$; if $u_{ik}=0$ continue with the next $k$; otherwise interchange $u_{k,k:m}\leftrightarrow u_{i,k:m}$, $l_{k,1:k-1}\leftrightarrow l_{i,1:k-1}$ and $p_{k,:}\leftrightarrow p_{i,:}$, and for $j=k+1,\dots,m$ set $l_{jk}=u_{jk}/u_{kk}$ and $u_{j,k:m}=u_{j,k:m}-l_{jk}u_{k,k:m}$.

Every square matrix, singular or not, has such a decomposition. In practice $P$ is not stored as a matrix: the rows are swapped at each step and only the permutation is recorded. The search for the pivot costs $O(m^2)$ comparisons, negligible against the $\sim\frac23m^3$ flops of the elimination. Complete pivoting needs $O(m^3)$ comparisons, and since the improvement in stability is marginal it is rarely used. R's `solve(A, b)` calls the LAPACK routine `dgesv`, which is Gaussian elimination with partial pivoting; `Matrix::lu()` returns the factors.

### 3.1.5. The Cholesky Decomposition

**Theorem 3.1.2 (Cholesky Decomposition)** Every Hermitian **positive definite matrix** $A$ has a unique decomposition

$$
A=R^{\mathsf H}R,\qquad r_{jj}>0,
$$
where $R$ is upper triangular.

In statistics the data are usually real, and "Hermitian" becomes "symmetric", $A=R^{\mathsf T}R$. Recall the relevant facts: a **symmetric matrix** has real eigenvalues and orthogonal eigenvectors; a symmetric positive definite (SPD) matrix moreover has positive eigenvalues, positive diagonal entries and positive pivots in elimination, satisfies $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$ for $\boldsymbol{x}\ne\boldsymbol{0}$, its principal submatrices are positive definite, $X^{\mathsf T}AX$ is SPD for every $X$ of full column rank, and its leading principal minors are positive (Sylvester's criterion).

The Cholesky decomposition is a variant of Gaussian elimination that operates on the left and the right of the matrix at once, preserving and exploiting symmetry. Write

$$
A=\begin{bmatrix}a_{11}&\boldsymbol{w}^{\mathsf H}\\\boldsymbol{w}&K\end{bmatrix},\qquad \alpha=\sqrt{a_{11}} .
$$
One step of elimination on both sides gives

$$
A=\begin{bmatrix}\alpha&0\\\boldsymbol{w}/\alpha&I\end{bmatrix}\begin{bmatrix}1&0\\0&K-\boldsymbol{w}\boldsymbol{w}^{\mathsf H}/a_{11}\end{bmatrix}\begin{bmatrix}\alpha&\boldsymbol{w}^{\mathsf H}/\alpha\\0&I\end{bmatrix}=R_1^{\mathsf H}A_1R_1 .
$$
The submatrix $K-\boldsymbol{w}\boldsymbol{w}^{\mathsf H}/a_{11}$, the **Schur complement** of $a_{11}$, is again positive definite (it is a principal submatrix of $A_1=R_1^{-\mathsf H}AR_1^{-1}$), so the process can be continued down to the bottom-right corner, giving $A=R_1^{\mathsf H}R_2^{\mathsf H}\cdots R_m^{\mathsf H}\,R_m\cdots R_2R_1=R^{\mathsf H}R$.

**Algorithm 3.1.3 (Cholesky Decomposition)** Set $R$ equal to the upper triangle of $A$. For $k=1,\dots,m$: for $j=k+1,\dots,m$, set $R_{j,j:m}=R_{j,j:m}-R_{k,j:m}\bar R_{kj}/R_{kk}$; then $R_{k,k:m}=R_{k,k:m}/\sqrt{R_{kk}}$.

The inner update touches $m-j+1$ entries with two flops each, so the work is

$$
\sum_{k=1}^m\sum_{j=k+1}^m2(m-j+1)\sim2\sum_{k=1}^m\sum_{j=1}^{m-k}j\sim\sum_{k=1}^mk^2\sim\frac13m^3\ \text{flops},
$$
half the cost of Gaussian elimination. The algorithm is always stable: since $\|R\|_2=\|R^{\mathsf H}\|_2=\|A\|_2^{1/2}$, entries much larger than those of $A$ can never arise, and because most of the weight of a positive definite matrix is on the diagonal, no pivoting is needed. To solve $A\boldsymbol{x}=\boldsymbol{b}$ for SPD $A$, the standard method is to reduce the system to $R^{\mathsf H}R\boldsymbol{x}=\boldsymbol{b}$ and solve $R^{\mathsf H}\boldsymbol{y}=\boldsymbol{b}$ and then $R\boldsymbol{x}=\boldsymbol{y}$; each triangular solve costs $\sim m^2$ flops, so the total is again $\sim\frac13m^3$ flops, and the whole process is backward stable.

**Example 3.1.2 (Likelihood of a Moving-Average Process)** Let $\varepsilon_t$, $t\in\mathbb{Z}$, be independent $\mathcal{N}(0,\delta)$ variables (Gaussian white noise with variance $\delta>0$) and $0<b<1$. The process $X_t=\varepsilon_t+b\varepsilon_{t-1}$ is a moving-average process of order one, MA(1). For $\boldsymbol{X}=(X_1,\dots,X_n)^{\mathsf T}$ we have $\mathbb{E}\boldsymbol{X}=\boldsymbol{0}$ and the tridiagonal covariance matrix

$$
\Sigma=\operatorname{Cov}(\boldsymbol{X})=\delta\begin{bmatrix}1+b^2&b&&\\b&1+b^2&\ddots&\\&\ddots&\ddots&b\\&&b&1+b^2\end{bmatrix},
$$
so the log-likelihood of the observation $\boldsymbol{X}=\boldsymbol{x}$ is

$$
\log L(b,\delta)=-\frac n2\log(2\pi)-\frac12\log\det\Sigma-\frac12\boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}.
$$
To maximize it numerically we must evaluate it at many $(b,\delta)$, and neither the determinant nor the inverse should be computed directly. With the Cholesky decomposition $\Sigma=LL^{\mathsf T}$ ($L=R^{\mathsf T}$ lower triangular),

$$
\det\Sigma=(\det L)^2=(l_{11}\cdots l_{nn})^2,\qquad \boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}=(L^{-1}\boldsymbol{x})^{\mathsf T}(L^{-1}\boldsymbol{x})=\boldsymbol{y}^{\mathsf T}\boldsymbol{y},
$$
where $\boldsymbol{y}=L^{-1}\boldsymbol{x}$ is obtained by forward substitution.

```r
ma1_loglik <- function(b, delta, x) {
  n <- length(x)
  Sigma <- diag(delta * (1 + b^2), n)
  Sigma[cbind(1:(n - 1), 2:n)] <- delta * b
  Sigma[cbind(2:n, 1:(n - 1))] <- delta * b
  R <- chol(Sigma)                          # Sigma = t(R) %*% R, R upper triangular
  y <- backsolve(R, x, transpose = TRUE)    # solves t(R) y = x
  -n / 2 * log(2 * pi) - sum(log(diag(R))) - sum(y^2) / 2
}
```

**Example 3.1.3** For which $\rho$ is

$$
C=\begin{bmatrix}1&0.6&-0.3\\0.6&1&\rho\\-0.3&\rho&1\end{bmatrix}
$$
a correlation matrix? It must be symmetric positive semidefinite. By Sylvester's criterion, the leading minors $1$ and $1-0.36$ are positive, and $\det C=-\rho^2-0.36\rho+0.55\ge0$ gives $-0.9432\le\rho\le0.5832$. Alternatively, the first step of the Cholesky decomposition leaves the Schur complement

$$
\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}-\begin{bmatrix}0.6\\-0.3\end{bmatrix}\begin{bmatrix}0.6&-0.3\end{bmatrix}=\begin{bmatrix}0.64&\rho+0.18\\\rho+0.18&0.91\end{bmatrix},
$$
which is positive semidefinite if and only if $0.5824-(\rho+0.18)^2\ge0$, that is, $\lvert\rho+0.18\rvert\le0.7632$: the same interval. For semidefinite matrices R offers the pivoted version `chol(A, pivot = TRUE)`.

## 3.2. Least Squares Problems

### 3.2.1. The Least Squares Problem

A matrix $A\in\mathbb{R}^{m\times n}$ of rank $r$ maps $\mathbb{R}^n$ to $\mathbb{R}^m$, and its four fundamental subspaces describe this map: in $\mathbb{R}^n$, the row space $\mathcal{R}(A^{\mathsf T})$ of dimension $r$ and the null space $\mathcal{N}(A)$ of dimension $n-r$; in $\mathbb{R}^m$, the **column space** $\mathcal{R}(A)$ of dimension $r$ and the left null space $\mathcal{N}(A^{\mathsf T})$ of dimension $m-r$. Each pair is orthogonal and complementary. Every $\boldsymbol{x}=\boldsymbol{x}_r+\boldsymbol{x}_n$ splits into a row-space part and a null-space part, and $A\boldsymbol{x}=A\boldsymbol{x}_r$; the system $A\boldsymbol{x}=\boldsymbol{b}$ is solvable only if $\boldsymbol{b}\in\mathcal{R}(A)$.

An overdetermined system, with more equations than unknowns ($m>n$), usually has no solution. The least squares idea, due to Gauss and Legendre around 1800, is to "solve" it by

$$
\min_{\boldsymbol{x}}\|\boldsymbol{b}-A\boldsymbol{x}\|_2 .
$$

**Theorem 3.2.1 (Least Squares and the Normal Equations)** Let $A\in\mathbb{C}^{m\times n}$ ($m\ge n$) and $\boldsymbol{b}\in\mathbb{C}^m$. A vector $\boldsymbol{x}\in\mathbb{C}^n$ minimizes the residual norm $\|\boldsymbol{r}\|_2=\|\boldsymbol{b}-A\boldsymbol{x}\|_2$ if and only if $\boldsymbol{r}\perp\mathcal{R}(A)$, that is, $A^{\mathsf H}\boldsymbol{r}=\boldsymbol{0}$, or equivalently

$$
A^{\mathsf H}A\boldsymbol{x}=A^{\mathsf H}\boldsymbol{b},
$$
or again equivalently $P\boldsymbol{b}=A\boldsymbol{x}$, where $P\in\mathbb{C}^{m\times m}$ is the orthogonal projector onto $\mathcal{R}(A)$. The system $A^{\mathsf H}A\boldsymbol{x}=A^{\mathsf H}\boldsymbol{b}$ is nonsingular if and only if $A$ has **full rank**, and then the solution is unique.

**Proof** If $A^{\mathsf H}\boldsymbol{r}=\boldsymbol{0}$, then for any $\boldsymbol{y}$, $\boldsymbol{b}-A\boldsymbol{y}=\boldsymbol{r}+A(\boldsymbol{x}-\boldsymbol{y})$ with orthogonal summands, so $\|\boldsymbol{b}-A\boldsymbol{y}\|_2^2=\|\boldsymbol{r}\|_2^2+\|A(\boldsymbol{x}-\boldsymbol{y})\|_2^2\ge\|\boldsymbol{r}\|_2^2$. Conversely, if $A^{\mathsf H}\boldsymbol{r}=\boldsymbol{z}\ne\boldsymbol{0}$, then $\boldsymbol{y}=\boldsymbol{x}+t\boldsymbol{z}$ with small $t>0$ gives $\|\boldsymbol{b}-A\boldsymbol{y}\|_2^2=\|\boldsymbol{r}\|_2^2-2t\|\boldsymbol{z}\|_2^2+t^2\|A\boldsymbol{z}\|_2^2<\|\boldsymbol{r}\|_2^2$. Finally $A^{\mathsf H}A$ is nonsingular if and only if $A\boldsymbol{z}=\boldsymbol{0}$ only for $\boldsymbol{z}=\boldsymbol{0}$. $\square$

Geometrically, $\boldsymbol{y}=A\boldsymbol{x}=P\boldsymbol{b}$ is the point of $\mathcal{R}(A)$ closest to $\boldsymbol{b}$. This is the matrix form of least squares regression in [3.3.7](/3.3.7). To understand $P$ we study projectors.

### 3.2.2. Projectors

Shine a light onto a subspace from a suitable direction: the shadow of a vector $\boldsymbol{v}$ is its projection $P\boldsymbol{v}$. Projecting the shadow again changes nothing.

**Definition 3.2.1 (Projector)** A **projector** is a square matrix $P$ that is idempotent, $P^2=P$. The matrix $I-P$ is the **complementary projector** to $P$. A projector is an **orthogonal projector** if $\mathcal{R}(P)$ and $\mathcal{N}(P)$ are orthogonal; otherwise it is oblique.

The direction of the light is $P\boldsymbol{v}-\boldsymbol{v}$, which lies in $\mathcal{N}(P)$ because $\mathbb{P}(P\boldsymbol{v}-\boldsymbol{v})=(P^2-P)\boldsymbol{v}=\boldsymbol{0}$. Oblique and orthogonal projectors differ in whether the projection lines are orthogonal to the projection plane. Note that an orthogonal projector is not an orthogonal matrix (unless $P=I$).

**Proposition 3.2.1** Let $P\in\mathbb{C}^{m\times m}$ be a projector.

1. Its eigenvalues are $0$ and $1$, and it is diagonalizable, since $P^2-P=\mathbb{P}(P-I)=O$ and the polynomial $z(z-1)$ has distinct roots; hence $\operatorname{tr}(P)=\operatorname{rank}(P)$.
2. $P$ is singular unless $P=I$: if $P^{-1}$ exists, $P=P^{-1}P^2=I$.
3. $I-P$ is also a projector, $\mathcal{R}(I-P)=\mathcal{N}(P)$, $\mathcal{N}(I-P)=\mathcal{R}(P)$, and $\mathcal{R}(P)\cap\mathcal{N}(P)=\{\boldsymbol{0}\}$. Hence $\mathbb{C}^m=\mathcal{R}(P)\oplus\mathcal{N}(P)$: $P$ projects onto $\mathcal{R}(P)$ along $\mathcal{N}(P)$, and every $\boldsymbol{v}$ decomposes uniquely as $\boldsymbol{v}=P\boldsymbol{v}+(I-P)\boldsymbol{v}$.

**Theorem 3.2.2** A projector $P$ is orthogonal if and only if $P=P^{\mathsf H}$.

**Proof** If $P=P^{\mathsf H}$, then $(P\boldsymbol{x})^{\mathsf H}(I-P)\boldsymbol{y}=\boldsymbol{x}^{\mathsf H}(P-P^2)\boldsymbol{y}=0$, so $\mathcal{R}(P)\perp\mathcal{R}(I-P)=\mathcal{N}(P)$. Conversely, if $P$ is orthogonal, then for all $\boldsymbol{x},\boldsymbol{y}$, $\langle P\boldsymbol{x},\boldsymbol{y}-P\boldsymbol{y}\rangle=\langle\boldsymbol{x}-P\boldsymbol{x},P\boldsymbol{y}\rangle=0$; thus $\langle P\boldsymbol{x},\boldsymbol{y}\rangle=\langle P\boldsymbol{x},P\boldsymbol{y}\rangle=\langle\boldsymbol{x},P\boldsymbol{y}\rangle=\langle P^{\mathsf H}\boldsymbol{x},\boldsymbol{y}\rangle$, and $P=P^{\mathsf H}$. $\square$

An orthogonal projector is thus a Hermitian (in the real case, symmetric) idempotent matrix. Since a real symmetric matrix has a spectral decomposition $A=Q\Lambda Q^{\mathsf T}$ with orthogonal $Q$, and the eigenvalues of $P$ are $0$ and $1$, every orthogonal projector of rank $n$ has the form

$$
P=\hat Q\hat Q^{\mathsf T}=\sum_{j=1}^n\boldsymbol{q}_j\boldsymbol{q}_j^{\mathsf T},
$$
where the columns $\boldsymbol{q}_1,\dots,\boldsymbol{q}_n$ of $\hat Q\in\mathbb{R}^{m\times n}$ are orthonormal. In particular:

- for a unit vector $\boldsymbol{q}$, the rank-one orthogonal projector $P_{\boldsymbol{q}}=\boldsymbol{q}\boldsymbol{q}^{\mathsf T}$ isolates the component $P\boldsymbol{v}=\boldsymbol{q}(\boldsymbol{q}^{\mathsf T}\boldsymbol{v})$ in the direction of $\boldsymbol{q}$, and its complement $P_{\perp\boldsymbol{q}}=I-\boldsymbol{q}\boldsymbol{q}^{\mathsf T}$, of rank $m-1$, eliminates it;
- for an arbitrary nonzero vector $\boldsymbol{a}$, $P_{\boldsymbol{a}}=\dfrac{\boldsymbol{a}\boldsymbol{a}^{\mathsf T}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}$ and $P_{\perp\boldsymbol{a}}=I-\dfrac{\boldsymbol{a}\boldsymbol{a}^{\mathsf T}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}$.

For the subspace spanned by linearly independent $\boldsymbol{a}_1,\dots,\boldsymbol{a}_n$, the columns of $A=[\boldsymbol{a}_1|\cdots|\boldsymbol{a}_n]$, let $\boldsymbol{y}=A\boldsymbol{x}$ be the orthogonal projection of $\boldsymbol{v}$ onto $\mathcal{R}(A)$. Then $\boldsymbol{v}-\boldsymbol{y}\perp\mathcal{R}(A)$, that is, $\boldsymbol{a}_j^{\mathsf T}(\boldsymbol{v}-A\boldsymbol{x})=0$ for every $j$, or $A^{\mathsf T}(\boldsymbol{v}-A\boldsymbol{x})=\boldsymbol{0}$. Hence $\boldsymbol{x}=(A^{\mathsf T}A)^{-1}A^{\mathsf T}\boldsymbol{v}$, $P\boldsymbol{v}=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}\boldsymbol{v}$, and

$$
P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T},
$$
which reduces to $\boldsymbol{a}\boldsymbol{a}^{\mathsf T}/(\boldsymbol{a}^{\mathsf T}\boldsymbol{a})$ for $n=1$. In linear regression $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ this is the **hat matrix** $H=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$ ([3.3.7](/3.3.7)).

### 3.2.3. The QR Decomposition

In many applications we are interested in the successive spaces spanned by the columns of $A$, $\langle\boldsymbol{a}_1\rangle\subseteq\langle\boldsymbol{a}_1,\boldsymbol{a}_2\rangle\subseteq\cdots$. The idea of the QR decomposition is to construct orthonormal vectors $\boldsymbol{q}_1,\boldsymbol{q}_2,\dots$ that span these successive spaces.

**Definition 3.2.2 (Reduced and Full QR Decomposition)** Let $A\in\mathbb{C}^{m\times n}$, $m\ge n$. A **reduced QR decomposition** is a factorization

$$
A=\hat Q\hat R,\qquad \begin{bmatrix}\boldsymbol{a}_1&\cdots&\boldsymbol{a}_n\end{bmatrix}=\begin{bmatrix}\boldsymbol{q}_1&\cdots&\boldsymbol{q}_n\end{bmatrix}\begin{bmatrix}r_{11}&r_{12}&\cdots&r_{1n}\\&r_{22}&\cdots&r_{2n}\\&&\ddots&\vdots\\&&&r_{nn}\end{bmatrix},
$$
where $\hat Q\in\mathbb{C}^{m\times n}$ has orthonormal columns and $\hat R\in\mathbb{C}^{n\times n}$ is upper triangular. A **full QR decomposition** $A=QR$ appends $m-n$ further orthonormal columns to $\hat Q$, making it a unitary $Q\in\mathbb{C}^{m\times m}$, and $m-n$ rows of zeros to $\hat R$, so that $R\in\mathbb{C}^{m\times n}$ is still upper triangular.

If $A$ has full rank $n$, then $r_{jj}\ne0$ and $\langle\boldsymbol{a}_1,\dots,\boldsymbol{a}_j\rangle=\langle\boldsymbol{q}_1,\dots,\boldsymbol{q}_j\rangle$ for every $j$. Comparing columns gives the **Gram–Schmidt process**:

$$
\boldsymbol{q}_1=\frac{\boldsymbol{a}_1}{r_{11}},\quad \boldsymbol{q}_2=\frac{\boldsymbol{a}_2-r_{12}\boldsymbol{q}_1}{r_{22}},\quad\dots,\quad \boldsymbol{q}_n=\frac{\boldsymbol{a}_n-\sum_{i=1}^{n-1}r_{in}\boldsymbol{q}_i}{r_{nn}},
$$
with $r_{ij}=\boldsymbol{q}_i^{\mathsf H}\boldsymbol{a}_j$ ($i<j$) and $r_{jj}=\bigl\|\boldsymbol{a}_j-\sum_{i=1}^{j-1}r_{ij}\boldsymbol{q}_i\bigr\|_2$. The columns $\boldsymbol{q}_{n+1},\dots,\boldsymbol{q}_m$ added in the full QR decomposition form an orthonormal basis of $\mathcal{N}(A^{\mathsf H})$, the orthogonal complement of $\mathcal{R}(A)$.

**Theorem 3.2.3 (Existence and Uniqueness)** (a) Every $A\in\mathbb{C}^{m\times n}$ ($m\ge n$) has a full QR decomposition, hence also a reduced one. (b) Each $A\in\mathbb{C}^{m\times n}$ ($m\ge n$) of full rank has a unique reduced QR decomposition $A=\hat Q\hat R$ with $r_{jj}>0$.

A proof of existence is provided by the Gram–Schmidt algorithm itself (when some $r_{jj}=0$, pick any unit vector orthogonal to the previous $\boldsymbol{q}_i$). For $m<n$ a QR decomposition also exists, $A=Q\begin{bmatrix}R_1&R_2\end{bmatrix}$ with an upper triangular $m\times m$ block $R_1$ followed by the columns $Q^{-1}\boldsymbol{a}_{m+1},Q^{-1}\boldsymbol{a}_{m+2},\dots$.

Another quick existence proof uses the Cholesky decomposition: if $A$ has full rank and $A^{\mathsf T}A=R^{\mathsf T}R$, then $A=(AR^{-1})R$ is a reduced QR decomposition, because

$$
(AR^{-1})^{\mathsf T}(AR^{-1})=R^{-\mathsf T}A^{\mathsf T}AR^{-1}=R^{-\mathsf T}R^{\mathsf T}RR^{-1}=I .
$$
(The other product $(AR^{-1})(AR^{-1})^{\mathsf T}$ is the projector onto $\mathcal{R}(A)$, not $I$, unless $A$ is square.) The triangular factors agree up to the signs of the rows:

```r
A <- matrix(c(10, 1,  1,
               1, 20, 2,
               1, 2, 30), ncol = 3)
qr.R(qr(A))
chol(t(A) %*% A)
```

```text
> qr.R(qr(A))
         [,1]       [,2]      [,3]
[1,] -10.0995  -3.168472 -4.158620
[2,]   0.0000 -19.873620 -4.419101
[3,]   0.0000   0.000000 29.464851
> chol(t(A) %*% A)
        [,1]      [,2]      [,3]
[1,] 10.0995  3.168472  4.158620
[2,]  0.0000 19.873620  4.419101
[3,]  0.0000  0.000000 29.464851
```

*Solving with QR.* If $A=QR$, then $A\boldsymbol{x}=\boldsymbol{b}$ becomes $QR\boldsymbol{x}=\boldsymbol{b}$, or $R\boldsymbol{x}=Q^{\mathsf T}\boldsymbol{b}$. The method is: (1) compute a QR decomposition $A=QR$; (2) compute $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{b}$; (3) solve the triangular system $R\boldsymbol{x}=\boldsymbol{y}$. This is what `lm` does: the component `effects` of an `lm` fit is the vector $Q^{\mathsf T}\boldsymbol{y}$, and the component `qr` stores the decomposition.

For the least squares problem $\min_{\boldsymbol{x}}\|A\boldsymbol{x}-\boldsymbol{b}\|_2^2$ with $m\ge n$ and full rank, write the full $Q=\bigl[\tilde Q\ \big|\ \tilde Q_\perp\bigr]$ with $\tilde Q\in\mathbb{R}^{m\times n}$, $\tilde Q_\perp\in\mathbb{R}^{m\times(m-n)}$, so that $Q^{\mathsf T}A=\begin{bmatrix}\hat R\\O\end{bmatrix}$. By unitary invariance,

$$
\|A\boldsymbol{x}-\boldsymbol{b}\|_2^2=\|Q^{\mathsf T}(A\boldsymbol{x}-\boldsymbol{b})\|_2^2=\left\|\begin{bmatrix}\hat R\boldsymbol{x}-\tilde Q^{\mathsf T}\boldsymbol{b}\\-\tilde Q_\perp^{\mathsf T}\boldsymbol{b}\end{bmatrix}\right\|_2^2=\|\hat R\boldsymbol{x}-\tilde Q^{\mathsf T}\boldsymbol{b}\|_2^2+\|\tilde Q_\perp^{\mathsf T}\boldsymbol{b}\|_2^2 .
$$
The minimum is attained by solving $\hat R\boldsymbol{x}=\tilde Q^{\mathsf T}\boldsymbol{b}$, $\boldsymbol{x}=\hat R^{-1}\tilde Q^{\mathsf T}\boldsymbol{b}$, and the residual norm is $\|\tilde Q_\perp^{\mathsf T}\boldsymbol{b}\|_2$. The reduced decomposition suffices for the solution; the extra columns of the full one only give the residual.

*The advantage over the normal equations.* If we solve the normal equations $A^{\mathsf T}A\boldsymbol{x}=A^{\mathsf T}\boldsymbol{b}$ by elimination, the matrix is $B=A^{\mathsf T}A$ with $\kappa(B)=\kappa(A)^2$ (the **condition number** in the 2-norm, see [3.5.1](/3.5.1)). With QR we solve $R\boldsymbol{x}=Q^{\mathsf T}\boldsymbol{b}$, and since $\kappa(Q)=1$, $\kappa(R)=\kappa(QR)=\kappa(A)$.

**Example 3.2.1** For a tiny $\delta$ consider

$$
A=\begin{bmatrix}1&1\\\delta&0\\0&\delta\end{bmatrix},\qquad B=A^{\mathsf T}A=\begin{bmatrix}1+\delta^2&1\\1&1+\delta^2\end{bmatrix}.
$$
The eigenvalues of $B$ are $2+\delta^2$ and $\delta^2$, so $\kappa(B)=\frac{2+\delta^2}{\delta^2}\approx\frac2{\delta^2}$ while $\kappa(R)=\kappa(A)=\sqrt{\frac{2+\delta^2}{\delta^2}}\approx\frac{\sqrt2}{\delta}$. With $\delta=10^{-5}$, $1+\delta^2$ already loses half of its significant digits relative to $\delta^2$, and $\kappa(B)\approx2\times10^{10}$:

```r
d <- 1e-2
A <- matrix(c(1, d, 0, 1, 0, d), ncol = 2)
kappa(A, exact = TRUE)               # 141.4249
kappa(t(A) %*% A, exact = TRUE)      # 20001
kappa(A, exact = TRUE)^2             # 20001
d <- 1e-5
A <- matrix(c(1, d, 0, 1, 0, d), ncol = 2)
kappa(A)                             # 141422.4 (an estimate)
kappa(t(A) %*% A)                    # 19999989553
```

There are three main ways to compute a QR decomposition: Gram–Schmidt orthogonalization, Householder triangularization and Givens rotations.

### 3.2.4. Gram–Schmidt Orthogonalization

**Algorithm 3.2.1 (Classical Gram–Schmidt)** For $j=1,\dots,n$: set $\boldsymbol{v}_j=\boldsymbol{a}_j$; for $i=1,\dots,j-1$, set $r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$ and $\boldsymbol{v}_j=\boldsymbol{v}_j-r_{ij}\boldsymbol{q}_i$; then $r_{jj}=\|\boldsymbol{v}_j\|_2$ and $\boldsymbol{q}_j=\boldsymbol{v}_j/r_{jj}$.

In exact arithmetic it produces $\hat Q$ and $\hat R$. In floating-point arithmetic it can produce vectors that are far from orthogonal.

**Example 3.2.2** Orthogonalize

$$
\boldsymbol{a}_1=(1,\varepsilon,0,0)^{\mathsf T},\quad \boldsymbol{a}_2=(1,0,\varepsilon,0)^{\mathsf T},\quad \boldsymbol{a}_3=(1,0,0,\varepsilon)^{\mathsf T},
$$
where $\varepsilon$ is so tiny that $1+\varepsilon^2$ rounds to $1$ (for example $\varepsilon=10^{-10}$ in double precision). Classical Gram–Schmidt gives: $r_{11}=\sqrt{1+\varepsilon^2}\approx1$, $\boldsymbol{q}_1=(1,\varepsilon,0,0)^{\mathsf T}$; $r_{12}=\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_2=1$, $\boldsymbol{v}_2=\boldsymbol{a}_2-\boldsymbol{q}_1=(0,-\varepsilon,\varepsilon,0)^{\mathsf T}$, $r_{22}=\sqrt2\varepsilon$, $\boldsymbol{q}_2=(0,-1,1,0)^{\mathsf T}/\sqrt2$; $r_{13}=\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3=1$, $r_{23}=\boldsymbol{q}_2^{\mathsf T}\boldsymbol{a}_3=0$, $\boldsymbol{v}_3=(0,-\varepsilon,0,\varepsilon)^{\mathsf T}$, $r_{33}=\sqrt2\varepsilon$, and

$$
\boldsymbol{q}_3=(0,-1,0,1)^{\mathsf T}/\sqrt2 .
$$
Here $\boldsymbol{q}_1^{\mathsf T}\boldsymbol{q}_2=-\varepsilon/\sqrt2\approx0$, but $\boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_3=1/2$: orthogonality is completely lost.

The cure comes from the view of orthogonal projectors. Gram–Schmidt computes $\boldsymbol{q}_j=P_j\boldsymbol{a}_j/\|P_j\boldsymbol{a}_j\|$, where $P_1=I$ and, for $j\ge2$,

$$
P_j\boldsymbol{v}=\boldsymbol{v}-(\boldsymbol{q}_1^{\mathsf H}\boldsymbol{v})\boldsymbol{q}_1-\cdots-(\boldsymbol{q}_{j-1}^{\mathsf H}\boldsymbol{v})\boldsymbol{q}_{j-1}=\Bigl(I-\sum_{i=1}^{j-1}\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf H}\Bigr)\boldsymbol{v}.
$$
Because the $\boldsymbol{q}_i$ are orthonormal, $P_j=I-\sum_{i<j}\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf H}=\prod_{i<j}(I-\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf H})=P_{\perp\boldsymbol{q}_{j-1}}\cdots P_{\perp\boldsymbol{q}_2}P_{\perp\boldsymbol{q}_1}$: a single projection of rank $m-j+1$ equals a sequence of $j-1$ projections of rank $m-1$. Classical Gram–Schmidt applies the left form, computing all coefficients from the original column $\boldsymbol{a}_j$; the modified version applies the right form, projecting the current, already partially orthogonalized vector one direction at a time.

**Algorithm 3.2.2 (Modified Gram–Schmidt)** For $i=1,\dots,n$, set $\boldsymbol{v}_i=\boldsymbol{a}_i$. For $i=1,\dots,n$: set $r_{ii}=\|\boldsymbol{v}_i\|_2$ and $\boldsymbol{q}_i=\boldsymbol{v}_i/r_{ii}$; for $j=i+1,\dots,n$, set $r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{v}_j$ and $\boldsymbol{v}_j=\boldsymbol{v}_j-r_{ij}\boldsymbol{q}_i$.

The only difference from Algorithm 3.2.1 is $r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{v}_j$ (MGS) instead of $r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$ (CGS); in exact arithmetic the two are equivalent, but modified Gram–Schmidt is much less sensitive to rounding errors. In Example 3.2.2 it computes $r_{13}=\boldsymbol{q}_1^{\mathsf T}\boldsymbol{v}_3=1$, $\boldsymbol{v}_3=(0,-\varepsilon,0,\varepsilon)^{\mathsf T}$, then $r_{23}=\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3=\varepsilon/\sqrt2$, $\boldsymbol{v}_3\leftarrow(0,-\varepsilon/2,-\varepsilon/2,\varepsilon)^{\mathsf T}$, $r_{33}=\sqrt6\varepsilon/2$, and

$$
\boldsymbol{q}_3=(0,-1,-1,2)^{\mathsf T}/\sqrt6,\qquad \boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_3=0 .
$$

Why? In MGS, $\boldsymbol{v}_3^{(1)}=\boldsymbol{a}_3-(\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3)\boldsymbol{q}_1$ and $\boldsymbol{v}_3=\boldsymbol{v}_3^{(1)}-(\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3^{(1)})\boldsymbol{q}_2$, so $\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3=\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3^{(1)}-(\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3^{(1)})\boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_2=0$ whatever errors $\boldsymbol{v}_3^{(1)}$ contains. In CGS, $\boldsymbol{v}_3=\boldsymbol{a}_3-(\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3)\boldsymbol{q}_1-(\boldsymbol{q}_2^{\mathsf T}\boldsymbol{a}_3)\boldsymbol{q}_2$ gives $\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3=-(\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3)\,\boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_1$: if an error is made in computing $\boldsymbol{q}_2$, so that $\boldsymbol{q}_1^{\mathsf T}\boldsymbol{q}_2=\delta$ is small but nonzero, it is not corrected in any of the computations that follow, and it is multiplied by the possibly large coefficient $\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3$.

```r
CGS <- function(A) {
  m <- nrow(A); n <- ncol(A)
  Q <- matrix(0, m, n); R <- matrix(0, n, n)
  for (j in 1:n) {
    v <- A[, j]
    if (j > 1) for (i in 1:(j - 1)) {
      R[i, j] <- sum(Q[, i] * A[, j])      # coefficient from the original column
      v <- v - R[i, j] * Q[, i]
    }
    R[j, j] <- sqrt(sum(v^2))
    Q[, j] <- v / R[j, j]
  }
  list(Q, R)
}

MGS <- function(A) {
  m <- nrow(A); n <- ncol(A)
  V <- A; Q <- matrix(0, m, n); R <- matrix(0, n, n)
  for (i in 1:n) {
    R[i, i] <- sqrt(sum(V[, i]^2))
    Q[, i] <- V[, i] / R[i, i]
    if (i < n) for (j in (i + 1):n) {
      R[i, j] <- sum(Q[, i] * V[, j])      # coefficient from the updated column
      V[, j] <- V[, j] - R[i, j] * Q[, i]
    }
  }
  list(Q, R)
}
```

**Example 3.2.3** The singular matrix with columns $(1,2,3)^{\mathsf T},(4,5,6)^{\mathsf T},(7,8,9)^{\mathsf T}$ has rank $2$. Run through `MGS`, the third column $\boldsymbol{v}_3$ becomes exactly $\boldsymbol{0}$, so $r_{33}=0$ and $\boldsymbol{q}_3$ is `NaN`: the method exposes the rank deficiency. `CGS` instead returns $r_{33}=5.6\times10^{-15}$ and a third column that agrees with $\boldsymbol{q}_2$ to about $15$ digits, so that $\tilde Q^{\mathsf T}\tilde Q$ has entries $1$ off the diagonal, and the problem goes unnoticed.

*Operation count.* In Algorithm 3.2.2 most of the work is the inner loop, $r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{v}_j$ ($m$ multiplications and $m-1$ additions) and $\boldsymbol{v}_j=\boldsymbol{v}_j-r_{ij}\boldsymbol{q}_i$ ($m$ multiplications and $m$ subtractions), about $4m$ flops per iteration:

$$
\sum_{i=1}^n\sum_{j=i+1}^n4m=4m\sum_{i=1}^n(n-i)\sim2mn^2\ \text{flops}.
$$
Counting exactly, with $m$ divisions and $2m-1$ flops for each norm, the additions total $\frac12n(n+1)(m-1)$, the subtractions $\frac12mn(n-1)$, the multiplications $mn^2$ and the divisions $mn$, so the total is $2mn^2+mn-\frac12n^2-\frac12n\sim2mn^2$ flops (the square roots add $n$ more). Classical Gram–Schmidt has the same count.

### 3.2.5. Householder Triangularization

Gram–Schmidt multiplies $A$ on the right by triangular matrices to make its columns orthonormal. At step 1,

$$
\begin{bmatrix}\boldsymbol{a}_1&\boldsymbol{a}_2&\cdots&\boldsymbol{a}_n\end{bmatrix}\begin{bmatrix}\frac1{r_{11}}&\frac{-r_{12}}{r_{11}}&\cdots&\frac{-r_{1n}}{r_{11}}\\&1&&\\&&\ddots&\\&&&1\end{bmatrix}=\begin{bmatrix}\boldsymbol{q}_1&\boldsymbol{a}_2^{(2)}&\cdots&\boldsymbol{a}_n^{(2)}\end{bmatrix},
$$
and after all the steps $AR_1R_2\cdots R_n=\hat Q$ with $R_1R_2\cdots R_n=\hat R^{-1}$: Gram–Schmidt is *triangular orthogonalization*. The Householder method is *orthogonal triangularization*: it multiplies $A$ on the left by unitary matrices $Q_k$ to make it triangular,

$$
Q_n\cdots Q_2Q_1A=R,\qquad Q_n\cdots Q_2Q_1=Q^{-1}.
$$
(In this language, Gaussian elimination $L_{m-1}\cdots L_1A=U$ is triangular triangularization.) Step $k$ introduces zeros below the diagonal in column $k$ and preserves all the zeros introduced before:

$$
\begin{bmatrix}\times&\times&\times\\\times&\times&\times\\\times&\times&\times\\\times&\times&\times\\\times&\times&\times\end{bmatrix}\xrightarrow{Q_1}\begin{bmatrix}\times&\times&\times\\0&\times&\times\\0&\times&\times\\0&\times&\times\\0&\times&\times\end{bmatrix}\xrightarrow{Q_2}\begin{bmatrix}\times&\times&\times\\0&\times&\times\\0&0&\times\\0&0&\times\\0&0&\times\end{bmatrix}\xrightarrow{Q_3}\begin{bmatrix}\times&\times&\times\\0&\times&\times\\0&0&\times\\0&0&0\\0&0&0\end{bmatrix}.
$$
To leave the first $k-1$ rows and the first $k-1$ columns alone, $Q_k$ must have the form

$$
Q_k=\begin{bmatrix}I_{k-1}&O\\O&F\end{bmatrix},
$$
where $F$ maps the vector $\boldsymbol{x}\in\mathbb{R}^{m-k+1}$ formed by the entries $k,\dots,m$ of column $k$ to a multiple of $\boldsymbol{e}_1$. Since $Q_kQ_k^{\mathsf T}=\begin{bmatrix}I&O\\O&FF^{\mathsf T}\end{bmatrix}=I$, $F$ must be orthogonal, so $\|F\boldsymbol{x}\|=\|\boldsymbol{x}\|$ and the target is $F\boldsymbol{x}=\pm\|\boldsymbol{x}\|\boldsymbol{e}_1$.

**Definition 3.2.3 (Householder Reflector)** For a nonzero $\boldsymbol{v}\in\mathbb{R}^p$, the matrix

$$
F=I-2\frac{\boldsymbol{v}\boldsymbol{v}^{\mathsf T}}{\boldsymbol{v}^{\mathsf T}\boldsymbol{v}}
$$
is the **Householder reflection** across the hyperplane $\operatorname{span}(\boldsymbol{v})^\perp$. With $\boldsymbol{v}=\|\boldsymbol{x}\|\boldsymbol{e}_1-\boldsymbol{x}$ it maps $\boldsymbol{x}$ to $\|\boldsymbol{x}\|\boldsymbol{e}_1$.

Compare with the projector $P_{\perp\boldsymbol{v}}=I-\boldsymbol{v}\boldsymbol{v}^{\mathsf T}/(\boldsymbol{v}^{\mathsf T}\boldsymbol{v})$ of rank $p-1$: the projector goes halfway to the hyperplane, the reflector goes twice as far, to the mirror image. $F$ is symmetric and orthogonal, $F=F^{\mathsf T}=F^{-1}$, of full rank, and so is $Q_k$. (Matrices that are both symmetric and orthogonal are not limited to entries $0,\pm1$: $\boldsymbol{v}=(1,2)^{\mathsf T}$ gives $F=\frac15\begin{bmatrix}3&-4\\-4&-3\end{bmatrix}$.)

The reflector is not unique: $\boldsymbol{x}$ can be reflected to $+\|\boldsymbol{x}\|\boldsymbol{e}_1$ or to $-\|\boldsymbol{x}\|\boldsymbol{e}_1$, and from the computational point of view the choice matters. If $\boldsymbol{x}$ is close to $+\|\boldsymbol{x}\|\boldsymbol{e}_1$, then $\boldsymbol{v}=\|\boldsymbol{x}\|\boldsymbol{e}_1-\boldsymbol{x}$ is computed with catastrophic cancellation, and $\boldsymbol{v}\boldsymbol{v}^{\mathsf T}/(\boldsymbol{v}^{\mathsf T}\boldsymbol{v})$ is inaccurate. The stable choice reflects $\boldsymbol{x}$ to the point farther away, $-\operatorname{sgn}(x_1)\|\boldsymbol{x}\|\boldsymbol{e}_1$, that is, $\boldsymbol{v}=\operatorname{sgn}(x_1)\|\boldsymbol{x}\|\boldsymbol{e}_1+\boldsymbol{x}$, so that the first entry is a sum of two numbers of the same sign (take $\operatorname{sgn}(0)=1$).

**Algorithm 3.2.3 (Householder QR Decomposition)** For $k=1,\dots,n$: set $\boldsymbol{x}=A_{k:m,k}$, $\boldsymbol{v}_k=\operatorname{sgn}(x_1)\|\boldsymbol{x}\|_2\boldsymbol{e}_1+\boldsymbol{x}$, $\boldsymbol{v}_k=\boldsymbol{v}_k/\|\boldsymbol{v}_k\|_2$, and $A_{k:m,k:n}=A_{k:m,k:n}-2\boldsymbol{v}_k(\boldsymbol{v}_k^{\mathsf T}A_{k:m,k:n})$.

The result $R$ is left in place of $A$, and the reflection vectors $\boldsymbol{v}_k$ are stored for later use; $Q$ is never formed. To solve $A\boldsymbol{x}=\boldsymbol{b}$ (or the least squares problem), compute $Q^{-1}\boldsymbol{b}=Q^{\mathsf T}\boldsymbol{b}=Q_n\cdots Q_1\boldsymbol{b}$ implicitly, by $\boldsymbol{b}_{k:m}=\boldsymbol{b}_{k:m}-2\boldsymbol{v}_k(\boldsymbol{v}_k^{\mathsf T}\boldsymbol{b}_{k:m})$ for $k=1,\dots,n$, and then solve the upper triangular system $R\boldsymbol{x}=Q^{\mathsf T}\boldsymbol{b}$ by back substitution. Since each $Q_k$ is symmetric, $Q=Q_1^{\mathsf T}\cdots Q_n^{\mathsf T}=Q_1Q_2\cdots Q_n$, so $Q\boldsymbol{x}$ is computed by $\boldsymbol{x}_{k:m}=\boldsymbol{x}_{k:m}-2\boldsymbol{v}_k(\boldsymbol{v}_k^{\mathsf T}\boldsymbol{x}_{k:m})$ for $k=n$ down to $1$. If $Q$ is required explicitly, apply this to $\boldsymbol{x}=\boldsymbol{e}_1,\dots,\boldsymbol{e}_m$ (or only $\boldsymbol{e}_1,\dots,\boldsymbol{e}_n$ for $\hat Q$).

*Operation count.* In iteration $k$, the dot products $\boldsymbol{v}_k^{\mathsf T}A_{k:m,k:n}$ cost about $2(m-k)(n-k)$ flops, the outer product $2\boldsymbol{v}_k(\cdots)$ about $(m-k)(n-k)$ and the subtraction another $(m-k)(n-k)$. Including the outer loop, the total is

$$
\sum_{k=1}^n4(m-k)(n-k)=4\sum_{k=1}^n\bigl(mn-k(m+n)+k^2\bigr)\sim4mn^2-4(m+n)\frac{n^2}2+\frac43n^3=2mn^2-\frac23n^3\ \text{flops},
$$
slightly less than the $2mn^2$ of Gram–Schmidt. For a square nonsingular $A$ ($m=n$) this is $\frac43m^3$, twice the $\frac23m^3$ of Gaussian elimination: if the least operation count is the goal, a square system is solved by Gaussian elimination.

*Stability.* Because of rounding errors, the computed factors satisfy $A=\tilde Q\tilde R+E$. The residual $E$ is not usually the problem: for both Householder and Gram–Schmidt, $\|E\|\le c\,\varepsilon_{\mathrm{mach}}\|A\|$, where $c$ depends only on the dimensions, and both compute $\tilde R$ accurately in a columnwise sense. The main difference is in the orthogonality of the computed factor:

$$
\text{Householder: }\|I-\tilde Q^{\mathsf T}\tilde Q\|\le c\,\varepsilon_{\mathrm{mach}},\qquad \text{MGS: }\|I-\tilde Q^{\mathsf T}\tilde Q\|\le c\,\varepsilon_{\mathrm{mach}}\kappa(A),\qquad \text{CGS: }\|I-\tilde Q^{\mathsf T}\tilde Q\|\le c\,\varepsilon_{\mathrm{mach}}\kappa(A)^2,
$$
the last bound holding as long as $\varepsilon_{\mathrm{mach}}\kappa(A)^2$ is well below $1$. Householder computes $\tilde Q$ as a product of accurate reflectors, which are orthogonal up to rounding, while there is nothing in Gram–Schmidt that forces $\tilde Q$ to be orthonormal in the face of roundoff. Householder triangularization is therefore the principal method for computing QR factorizations.

![Loss of orthogonality of the computed Q for 50 x 12 test matrices with prescribed condition numbers. Householder QR stays at the level of machine precision; modified Gram-Schmidt loses orthogonality in proportion to kappa(A), classical Gram-Schmidt in proportion to kappa(A)^2 until the columns are no longer independent at all.](./plots/qr-orthogonality-loss.py)

**Remark 3.2.1 (Least Squares by MGS)** The weakness of MGS concerns $\tilde Q$, not the least squares solution, provided the method is used correctly. To solve $\min\|A\boldsymbol{x}-\boldsymbol{b}\|_2$ we must not compute $\boldsymbol{x}=R^{-1}(Q^{\mathsf T}\boldsymbol{b})$ from the computed $Q$. Instead, apply MGS to the augmented matrix,

$$
\begin{bmatrix}A&\boldsymbol{b}\end{bmatrix}=\begin{bmatrix}Q&\boldsymbol{q}_{n+1}\end{bmatrix}\begin{bmatrix}R&\boldsymbol{z}\\\boldsymbol{0}^{\mathsf T}&\rho\end{bmatrix}.
$$
Then $A\boldsymbol{x}-\boldsymbol{b}=\begin{bmatrix}A&\boldsymbol{b}\end{bmatrix}\begin{bmatrix}\boldsymbol{x}\\-1\end{bmatrix}=Q(R\boldsymbol{x}-\boldsymbol{z})-\rho\boldsymbol{q}_{n+1}$, and since $\boldsymbol{q}_{n+1}$ is orthogonal to the columns of $Q$, $\|A\boldsymbol{x}-\boldsymbol{b}\|_2^2=\|R\boldsymbol{x}-\boldsymbol{z}\|_2^2+\rho^2$. The solution is $\boldsymbol{x}=R^{-1}\boldsymbol{z}$, where $\boldsymbol{z}$ is computed as part of the MGS procedure instead of as the product $Q^{\mathsf T}\boldsymbol{b}$. Used this way MGS is stable for least squares, although it can give poor results when used to compute an orthonormal basis: the stability of an algorithm depends on the problem.

**Example 3.2.4** For the singular matrix of Example 3.2.3, a Householder implementation returns a $\tilde Q$ with $\|\tilde Q^{\mathsf T}\tilde Q-I\|$ of order $10^{-16}$ and an $\tilde R$ whose last diagonal entry is $-4.4\times10^{-16}$, a clear signal of rank deficiency; the CGS factor has $\tilde Q^{\mathsf T}\tilde Q$ with off-diagonal entries equal to $1$.

*QR in R.* The function `qr` computes a Householder QR decomposition (by the LINPACK routine `dqrdc2`, or by LAPACK with `LAPACK = TRUE`) and returns it in compact form:

```r
A <- rbind(c(2, -2, 18), c(2, 1, 0), c(1, 2, 0))
A.qr <- qr(A)
A.qr.out <- list(Q = qr.Q(A.qr), R = qr.R(A.qr))
A.qr
```

```text
$qr
          [,1] [,2] [,3]
[1,] -3.0000000  0.0  -12
[2,]  0.6666667 -3.0   12
[3,]  0.3333333  0.8    6

$rank
[1] 3

$qraux
[1] 1.666667 1.600000 6.000000

$pivot
[1] 1 2 3
```

The upper triangle of `$qr` is $R$. The Householder vectors are stored below the diagonal and in `$qraux`: the reflection is $H_i=I-\boldsymbol{v}_i\boldsymbol{v}_i^{\mathsf T}/p_i$, where $p_i$ is the $i$-th entry of `$qraux` and $\boldsymbol{v}_i$ has entries $\boldsymbol{v}_i[1{:}(i-1)]=0$, $\boldsymbol{v}_i[i]=p_i$ $(=\boldsymbol{v}_i^{\mathsf T}\boldsymbol{v}_i/2)$ and $\boldsymbol{v}_i[(i+1){:}m]=$ `A.qr$qr[(i+1):m, i]`. This is the reflector $F=I-2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}/(\boldsymbol{v}^{\mathsf T}\boldsymbol{v})$ with a different scaling of $\boldsymbol{v}$. One can check it directly:

```r
p <- A.qr$qraux
v1 <- matrix(c(p[1], A.qr$qr[2:3, 1]))
p[1] == t(v1) %*% v1 / 2
v2 <- matrix(c(0, p[2], A.qr$qr[3, 2]))
I <- diag(3)
H1 <- I - v1 %*% t(v1) / p[1]
H2 <- I - v2 %*% t(v2) / p[2]
Q <- H1 %*% H2    # equals qr.Q(A.qr)

B <- cbind(c(2, -2, 18), c(2, -2, 18), c(2, 1, 0))
qr(B)$pivot       # 1 3 2: A P = Q R
```

The default `qr` uses a limited form of column pivoting: a column that is (numerically) a linear combination of the previous ones is moved to the end, so that the decomposition is $AP=QR$ and `$rank` reports the numerical rank. In `B` the second column repeats the first, and the pivot vector is $(1,3,2)$.

### 3.2.6. Givens Rotations

A **Givens rotation**

$$
G=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}
$$
rotates $\boldsymbol{x}\in\mathbb{R}^2$ counterclockwise by $\theta$ (its columns are the images of $\boldsymbol{e}_1$ and $\boldsymbol{e}_2$). Applied to two rows $i,j$ of a matrix (and the identity elsewhere), it can set an element to zero: choosing

$$
\cos\theta=\frac{x_i}{\sqrt{x_i^2+x_j^2}},\qquad \sin\theta=\frac{-x_j}{\sqrt{x_i^2+x_j^2}}
$$
gives $G\begin{bmatrix}x_i\\x_j\end{bmatrix}=\begin{bmatrix}\sqrt{x_i^2+x_j^2}\\0\end{bmatrix}$ (or $-\sqrt{x_i^2+x_j^2}$ with the opposite signs). Givens QR introduces the zeros of each column from the bottom up, one rotation per zero:

$$
\begin{bmatrix}\times&\times&\times\\\times&\times&\times\\\times&\times&\times\\\times&\times&\times\end{bmatrix}\xrightarrow{(3,4)}\begin{bmatrix}\times&\times&\times\\\times&\times&\times\\\times&\times&\times\\0&\times&\times\end{bmatrix}\xrightarrow{(2,3)}\begin{bmatrix}\times&\times&\times\\\times&\times&\times\\0&\times&\times\\0&\times&\times\end{bmatrix}\xrightarrow{(1,2)}\begin{bmatrix}\times&\times&\times\\0&\times&\times\\0&\times&\times\\0&\times&\times\end{bmatrix}\to\cdots\to R .
$$
The flop count is $3mn^2-n^3$, 50% more than Householder QR. Givens rotations are therefore used mainly on structured matrices, where only a few entries need to be zeroed (a tridiagonal or upper Hessenberg matrix needs only one rotation per column), and for the delicate zeroing needed when a factorization is updated or downdated after adding or deleting a row.

The QR decomposition is a versatile computational tool for linear systems, least squares and eigenvalue problems (Section 3.3). Of the three methods: Gram–Schmidt, which sequentially orthogonalizes the columns of $A$, is the oldest method and the one in most linear algebra textbooks; its advantage is that it can be stopped part-way, leaving a reduced QR of the first columns. Householder transformations provide the most generally useful way to compute the QR decomposition. Givens transformations are preferred when $A$ has a special sparsity structure, such as band or Hessenberg structure. Gram–Schmidt produces $Q$ explicitly, whereas Householder and Givens hold $Q$ in factored form.

### 3.2.7. The Singular Value Decomposition

We want to transform between orthonormal bases $\{\boldsymbol{v}_i\}$ of $\mathbb{C}^n$ and $\{\boldsymbol{u}_i\}$ of $\mathbb{C}^m$ such that $A\boldsymbol{v}_i=\sigma_i\boldsymbol{u}_i$:

$$
AV=A\begin{bmatrix}\boldsymbol{v}_1&\cdots&\boldsymbol{v}_n\end{bmatrix}=\begin{bmatrix}\boldsymbol{u}_1&\cdots&\boldsymbol{u}_m\end{bmatrix}\begin{bmatrix}\sigma_1&&\\&\ddots&\\&&\sigma_r\\&&&\end{bmatrix}=U\Sigma\ \Longrightarrow\ A=U\Sigma V^{\mathsf H}.
$$

**Definition 3.2.4** A singular value decomposition (SVD) of $A\in\mathbb{C}^{m\times n}$ is a factorization $A=U\Sigma V^{\mathsf H}$ with unitary $U\in\mathbb{C}^{m\times m}$, $V\in\mathbb{C}^{n\times n}$ and diagonal $\Sigma\in\mathbb{R}^{m\times n}$ with entries $\sigma_1\ge\sigma_2\ge\cdots\ge\sigma_{\min(m,n)}\ge0$. The $\sigma_j$ are the **singular values** of $A$, the columns $\boldsymbol{u}_j$ of $U$ its **left singular vectors** and the columns $\boldsymbol{v}_j$ of $V$ its **right singular vectors**, numbered so that $A\boldsymbol{v}_j=\sigma_j\boldsymbol{u}_j$. For $m\ge n$, the **reduced SVD** $A=\hat U\hat\Sigma V^{\mathsf H}$ keeps only the first $n$ columns of $U$ ($\hat U\in\mathbb{C}^{m\times n}$ with orthonormal columns, $\hat\Sigma\in\mathbb{R}^{n\times n}$); the full SVD extends $\hat U$ to a unitary $U$ by $m-n$ "silent" columns and adds zero rows to $\Sigma$.

The $\boldsymbol{v}_i$ are eigenvectors of $A^{\mathsf H}A$, the $\boldsymbol{u}_i$ eigenvectors of $AA^{\mathsf H}$, and the nonzero singular values are the square roots of their nonzero eigenvalues. Geometrically, $A$ maps the unit sphere of $\mathbb{R}^n$ to a hyperellipse in $\mathbb{R}^m$, stretching it by the factors $\sigma_1,\dots,\sigma_m$ (possibly zero) in the orthogonal directions $\boldsymbol{u}_1,\dots,\boldsymbol{u}_m$; the vectors $\sigma_j\boldsymbol{u}_j$ are the principal semiaxes of the hyperellipse, with lengths $\sigma_j$. The factorization $A=U\Sigma V^{\mathsf H}$ decomposes the transformation into a rotation (or reflection) $V^{\mathsf H}$, a scaling $\Sigma$ along the coordinate axes and another rotation $U$. If $\operatorname{rank}(A)=r<n$, the reduced SVD can be shrunk further to $A=\hat U_{m\times r}\hat\Sigma_{r\times r}\hat V_{n\times r}^{\mathsf H}$, and in the full SVD both $U$ and $V$ are extended to unitary matrices; the silent columns satisfy $\boldsymbol{v}_i\in\mathcal{N}(A)=\mathcal{N}(A^{\mathsf H}A)$ and $\boldsymbol{u}_i\in\mathcal{N}(A^{\mathsf H})=\mathcal{N}(AA^{\mathsf H})$ for $i>r$.

**Theorem 3.2.4 (Existence and Uniqueness of the SVD)** Every matrix $A\in\mathbb{C}^{m\times n}$ has a singular value decomposition. The singular values are uniquely determined, and if $A$ is square and the $\sigma_j$ are distinct, the left and right singular vectors are uniquely determined up to complex signs (factors of modulus one). The singular values are real; if $A$ is real, $U$ and $V$ can be chosen real.

Since $A^{\mathsf H}A=V\Sigma^{\mathsf H}U^{\mathsf H}U\Sigma V^{\mathsf H}=V\Sigma^{\mathsf H}\Sigma V^{\mathsf H}$ and $AA^{\mathsf H}=U\Sigma\Sigma^{\mathsf H}U^{\mathsf H}$, an SVD can in principle be obtained in two steps: (1) find $\{\boldsymbol{v}_j,\sigma_j\}$ from the eigendecomposition of $A^{\mathsf H}A$; (2) set $\boldsymbol{u}_j=A\boldsymbol{v}_j/\sigma_j$ for $j\le r$ and complete with an orthonormal basis of $\mathcal{N}(A^{\mathsf H})$. This shows that $\kappa(A^{\mathsf T}A)=\sigma_1^2/\sigma_n^2=\kappa(A)^2$. Numerically this route is not used, precisely because forming $A^{\mathsf H}A$ squares the condition number and destroys small singular values; library routines (LAPACK, called by `svd`) first reduce $A$ to bidiagonal form by Householder reflections and then iterate on the bidiagonal matrix.

**Proposition 3.2.2 (Matrix Properties via the SVD)** Let $A=U\Sigma V^{\mathsf H}$ have $r$ nonzero singular values.

1. $\operatorname{rank}(A)=r$.
2. $\mathcal{R}(A)=\langle\boldsymbol{u}_1,\dots,\boldsymbol{u}_r\rangle$ and $\mathcal{N}(A)=\langle\boldsymbol{v}_{r+1},\dots,\boldsymbol{v}_n\rangle$.
3. $\|A\|_2=\sigma_1$ and $\|A\|_{\mathrm{F}}=\sqrt{\operatorname{tr}(A^{\mathsf H}A)}=\sqrt{\sigma_1^2+\cdots+\sigma_r^2}$ (both norms are unitarily invariant, so they equal those of $\Sigma$).
4. The nonzero singular values are $\sigma_j=\sqrt{\lambda_j(A^{\mathsf H}A)}=\sqrt{\lambda_j(AA^{\mathsf H})}$.
5. If $A=A^{\mathsf H}$, then $\sigma_j=\lvert\lambda_j(A)\rvert$.
6. For square $A$, $\lvert\det A\rvert=\prod_j\sigma_j$ (whereas $\det A=\prod_j\lambda_j$ and $\operatorname{tr}(A)=\sum_j\lambda_j$).

The sum $\|A\|_*=\sum_i\sigma_i$ is the nuclear norm. These properties are also the best computational tools: the best method for determining the rank of a matrix is to count the singular values greater than a judiciously chosen tolerance (property 1); the most accurate method for an orthonormal basis of a range or a null space is property 2 (QR provides faster but not always as accurate alternatives); property 3 is the standard method for computing $\|A\|_2$. Beyond these, the SVD is an ingredient of robust algorithms for least squares fitting, intersection of subspaces, regularization and numerous other problems.

*Solving $A\boldsymbol{x}=\boldsymbol{b}$: a change of bases.* With $\tilde{\boldsymbol{b}}=U^{\mathsf H}\boldsymbol{b}$ and $\tilde{\boldsymbol{x}}=V^{\mathsf H}\boldsymbol{x}$,

$$
\boldsymbol{b}=A\boldsymbol{x}\iff U^{\mathsf H}\boldsymbol{b}=\Sigma V^{\mathsf H}\boldsymbol{x}\iff\tilde{\boldsymbol{b}}=\Sigma\tilde{\boldsymbol{x}} .
$$
$A$ reduces to the diagonal matrix $\Sigma$ when the range is expressed in the basis of columns of $U$ and the domain in the basis of columns of $V$: every matrix is diagonal, if only one uses the proper bases for the domain and range spaces. In particular, for nonsingular $A$, $A^{-1}=V\Sigma^{-1}U^{\mathsf H}$.

*The condition number revisited.* For an invertible $A\in\mathbb{R}^{m\times m}$ with $\sigma_1\ge\cdots\ge\sigma_m>0$, the condition numbers of $\boldsymbol{x}\mapsto A\boldsymbol{x}$ and of $\boldsymbol{b}\mapsto A^{-1}\boldsymbol{b}$ ([3.5.1](/3.5.1)) are bounded by

$$
\kappa(\boldsymbol{x})=\|A\|\frac{\|\boldsymbol{x}\|}{\|A\boldsymbol{x}\|}\le\|A\|\,\|A^{-1}\|,\qquad \kappa(\boldsymbol{b})=\|A^{-1}\|\frac{\|\boldsymbol{b}\|}{\|\boldsymbol{x}\|}\le\|A^{-1}\|\,\|A\|,
$$
and $\kappa(A)=\|A\|_2\|A^{-1}\|_2=\sigma_1/\sigma_m$. Writing $A=\sum_{i=1}^m\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$, a sum of $m$ rank-one matrices, the equality holds in the first bound if $\boldsymbol{x}=k\boldsymbol{v}_m$ is a multiple of the right singular vector for $\sigma_m$, since then $\|\boldsymbol{x}\|/\|A\boldsymbol{x}\|=\|k\boldsymbol{v}_m\|/\|k\sigma_m\boldsymbol{u}_m\|=1/\sigma_m=\|A^{-1}\|$; and in the second if $\boldsymbol{b}=k\boldsymbol{u}_1$, since $A^{-1}=\sum_i\boldsymbol{v}_i\boldsymbol{u}_i^{\mathsf T}/\sigma_i$ gives $\|\boldsymbol{b}\|/\|\boldsymbol{x}\|=\|k\boldsymbol{u}_1\|/\|k\boldsymbol{v}_1/\sigma_1\|=\sigma_1=\|A\|$. Singular values themselves are perfectly conditioned: if $\tilde\sigma_i$ are the singular values of $A+E$, then $\lvert\tilde\sigma_i-\sigma_i\rvert\le\|E\|_2$ for each $i$ (Weyl) and $\sqrt{\sum_i(\tilde\sigma_i-\sigma_i)^2}\le\|E\|_{\mathrm{F}}$ (Mirsky).

**Theorem 3.2.5 (Low-Rank Approximation)** Let $A=U\Sigma V^{\mathsf T}\in\mathbb{R}^{m\times n}$, $r=\operatorname{rank}(A)$, and for $k<r$ let

$$
A_k=\sum_{i=1}^k\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}.
$$
Then

$$
\min_{\operatorname{rank}(B)\le k}\|A-B\|_2=\|A-A_k\|_2=\sigma_{k+1},\qquad \min_{\operatorname{rank}(B)\le k}\|A-B\|_{\mathrm{F}}=\|A-A_k\|_{\mathrm{F}}=\sqrt{\sigma_{k+1}^2+\cdots+\sigma_r^2}.
$$

This is the **Eckart–Young theorem** (in the 2-norm and the Frobenius norm, also called the Eckart–Young–Mirsky theorem; a proof is in [2.1.7](/2.1.7)). The value of the error follows from $U^{\mathsf T}A_kV=\operatorname{diag}(\sigma_1,\dots,\sigma_k,0,\dots,0)$, so $U^{\mathsf T}(A-A_k)V=\operatorname{diag}(0,\dots,0,\sigma_{k+1},\dots,\sigma_r)$. For example, the closest rank-2 matrix to $\operatorname{diag}(4,2,1,3)$ is $\operatorname{diag}(4,0,0,3)$: the two largest singular values are kept, wherever they stand on the diagonal.

**Example 3.2.5 (Image Compression)** A digital image is a matrix of pixels; a color image is three such matrices, the red, green and blue intensities (on a scale of $0$ to $255$, rescaled to $[0,1]$ in R). Image compression keeps only a low-rank approximation of each matrix, which retains the essential information of the image. For a $400\times286$ photograph (full rank $286$), the rank-$20$ approximation of each channel is already recognizable and needs $20(400+286+1)$ instead of $400\times286$ numbers per channel; the more singular values we keep, the more accurate the approximation.

```r
library(jpeg)
x <- readJPEG("photo.jpg")      # convert the image into an array
dim(x)                          # 400 286 3
# each matrix holds one color channel of the RGB scale
r <- x[, , 1]; r.svd <- svd(r)
g <- x[, , 2]; g.svd <- svd(g)
b <- x[, , 3]; b.svd <- svd(b)
# collect the results into a list used to reconstruct the image
rgb.svds <- list(r.svd, g.svd, b.svd)

for (j in c(3, 5, 10, 20, 30)) {
  a <- sapply(rgb.svds, function(i) {
    i$u[, 1:j] %*% diag(i$d[1:j]) %*% t(i$v[, 1:j])
  }, simplify = "array")
  writeJPEG(pmin(pmax(a, 0), 1), paste0("compressed_svd_rank_", j, ".jpg"))
}
```

*Principal component analysis.* High-dimensional data matrices are hard to use. As the number $p$ of variables grows with the sample size $n$ fixed, the number of samples needed for good prediction grows exponentially, and algorithms tend to overfit, so that their performance first increases and then decreases with $p$ (the Hughes phenomenon). This is part of the curse of dimensionality: the volume of the space increases so fast that the data become sparse, most of the data lie in a thin "shell", all points become nearly equidistant so that distance-based methods perform poorly, and the data can no longer be visualized. Reducing the dimension of a data matrix $X_{n\times p}$ means reducing $p$, the number of variables, while retaining as much of the variance as possible. **Principal component analysis** ([3.4.5](/3.4.5)) does this with the SVD.

Let the rows $\boldsymbol{X}_{(i)}^{\mathsf T}$ of $X$ be the data points, and assume that the columns of $X$ are centered (and, if desired, scaled). The projection of a data point onto a unit vector $\boldsymbol{v}_1$ is $\boldsymbol{v}_1\boldsymbol{v}_1^{\mathsf T}\boldsymbol{X}_{(i)}$, with coefficient $\boldsymbol{v}_1^{\mathsf T}\boldsymbol{X}_{(i)}=\boldsymbol{X}_{(i)}^{\mathsf T}\boldsymbol{v}_1$; for all points at once, $\boldsymbol{Y}_1=X\boldsymbol{v}_1\in\mathbb{R}^n$. With the sample covariance matrix $\frac1{n-1}X^{\mathsf T}X$,

$$
\operatorname{Var}(\boldsymbol{Y}_1)=\frac1{n-1}\boldsymbol{Y}_1^{\mathsf T}\boldsymbol{Y}_1=\frac1{n-1}\boldsymbol{v}_1^{\mathsf T}X^{\mathsf T}X\boldsymbol{v}_1,\qquad \max_{\|\boldsymbol{v}_1\|_2=1}\boldsymbol{v}_1^{\mathsf T}X^{\mathsf T}X\boldsymbol{v}_1=\max_{\|\boldsymbol{v}_1\|_2=1}\|X\boldsymbol{v}_1\|_2^2=\|X\|_2^2 .
$$
Hence, with the SVD $X=U\Sigma V^{\mathsf T}$, $\sigma_1\ge\cdots\ge\sigma_p$, the direction of maximal variance, the first principal direction, is the first right singular vector $\boldsymbol{v}_1$, equivalently the eigenvector of $X^{\mathsf T}X$ with the largest eigenvalue $\lambda_1=\sigma_1^2$; $\boldsymbol{Y}_1=X\boldsymbol{v}_1=\sigma_1\boldsymbol{u}_1$ is the vector of first principal component scores, with variance $\sigma_1^2/(n-1)$. Keeping the first $k<p$ principal components fits a $k$-dimensional ellipsoid to the data, or projects the data onto a $k$-dimensional plane, and the proportion of variance explained is

$$
\frac{\sum_{i=1}^k\boldsymbol{v}_i^{\mathsf T}X^{\mathsf T}X\boldsymbol{v}_i}{\sum_{i=1}^p\boldsymbol{v}_i^{\mathsf T}X^{\mathsf T}X\boldsymbol{v}_i}=\frac{\sum_{i=1}^k\sigma_i^2}{\sum_{i=1}^p\sigma_i^2}=\frac{\sum_{i=1}^k\lambda_i}{\sum_{i=1}^p\lambda_i}.
$$
The scree plot of these proportions is used to choose $k$, by looking for the "knee". PCA with and without standardization gives different results: variables with the largest variances dominate the first component, so standardizing is usual when the variables are measured in different or incomparable units; it amounts to giving all variables equal importance, and it is sensitive to outliers (robust scaling by the median and the interquartile range is an alternative). But standardizing is not appropriate when all variables measure the same quantity in the same units: if many neurons are recorded simultaneously, their differences in activity are important, and dividing the activity of an almost silent neuron by its tiny standard deviation would greatly amplify what is probably noise.

### 3.2.8. Three Algorithms for Least Squares

Let $A\in\mathbb{C}^{m\times n}$, $m\ge n$, have full rank. Three algorithms solve $\min_{\boldsymbol{x}}\|A\boldsymbol{x}-\boldsymbol{b}\|_2$.

**Algorithm 3.2.4 (Least Squares via the Normal Equations)** (1) Form the matrix $A^{\mathsf H}A$ and the vector $A^{\mathsf H}\boldsymbol{b}$. (2) Compute the Cholesky decomposition $A^{\mathsf H}A=R^{\mathsf H}R$. (3) Solve the lower triangular system $R^{\mathsf H}\boldsymbol{w}=A^{\mathsf H}\boldsymbol{b}$ for $\boldsymbol{w}$. (4) Solve the upper triangular system $R\boldsymbol{x}=\boldsymbol{w}$ for $\boldsymbol{x}$.

This is the classical way: for full-rank $A$ the normal equations form a square Hermitian positive definite system of dimension $n$, and the standard method for such systems is the Cholesky decomposition. Forming $A^{\mathsf H}A$ requires $\sim\sum_{i=1}^n\sum_{j=1}^i2m\sim mn^2$ flops (by symmetry only half of it is needed), the Cholesky decomposition $\sim n^3/3$; the total is $\sim mn^2+n^3/3$ flops.

**Algorithm 3.2.5 (Least Squares via QR)** (1) Compute the reduced QR decomposition $A=\hat Q\hat R$. (2) Compute the vector $\hat Q^{\mathsf H}\boldsymbol{b}$. (3) Solve the upper triangular system $\hat R\boldsymbol{x}=\hat Q^{\mathsf H}\boldsymbol{b}$ for $\boldsymbol{x}$.

This "modern classical" method, popular since the 1960s, uses Gram–Schmidt or, more usually, Householder triangularization. Its justification: $P=\hat Q\hat Q^{\mathsf H}$ is the orthogonal projector onto $\mathcal{R}(A)$, so $A\boldsymbol{x}=P\boldsymbol{b}$ becomes $\hat Q\hat R\boldsymbol{x}=\hat Q\hat Q^{\mathsf H}\boldsymbol{b}$, that is, $\hat R\boldsymbol{x}=\hat Q^{\mathsf H}\boldsymbol{b}$; equivalently the normal equations $\hat R^{\mathsf H}\hat Q^{\mathsf H}\hat Q\hat R\boldsymbol{x}=\hat R^{\mathsf H}\hat Q^{\mathsf H}\boldsymbol{b}$ reduce to it. The work is dominated by the QR decomposition, $\sim2mn^2-\frac23n^3$ flops with Householder reflections.

**Algorithm 3.2.6 (Least Squares via the SVD)** (1) Compute the reduced SVD $A=\hat U\hat\Sigma V^{\mathsf H}$. (2) Compute the vector $\hat U^{\mathsf H}\boldsymbol{b}$. (3) Solve the diagonal system $\hat\Sigma\boldsymbol{w}=\hat U^{\mathsf H}\boldsymbol{b}$ for $\boldsymbol{w}$. (4) Set $\boldsymbol{x}=V\boldsymbol{w}$.

Now $P=\hat U\hat U^{\mathsf H}$, and $A^{\mathsf H}A\boldsymbol{x}=A^{\mathsf H}\boldsymbol{b}$ becomes $V\hat\Sigma\hat U^{\mathsf H}\hat U\hat\Sigma V^{\mathsf H}\boldsymbol{x}=V\hat\Sigma\hat U^{\mathsf H}\boldsymbol{b}$, that is, $\hat\Sigma V^{\mathsf H}\boldsymbol{x}=\hat U^{\mathsf H}\boldsymbol{b}$. The work is dominated by the SVD, $\sim2mn^2+11n^3$ flops. For rank-deficient $A$ the same steps with only the nonzero (or not negligible) singular values give the minimum-norm solution $\boldsymbol{x}=A^+\boldsymbol{b}$, where $A^+=V\Sigma^+U^{\mathsf H}$ is the **Moore–Penrose pseudoinverse**; for full rank $A^+=(A^{\mathsf H}A)^{-1}A^{\mathsf H}$.

| Algorithm | Flops | Stability | Use |
|---|---|---|---|
| Normal equations + Cholesky | $\sim mn^2+n^3/3$ | errors grow like $\kappa(A)^2$ | speed is the only concern, well-conditioned $A$ |
| Householder QR | $\sim2mn^2-\frac23n^3$ | backward stable | the standard choice (`lm`, `qr.solve`) |
| SVD | $\sim2mn^2+11n^3$ | most robust | $A$ close to rank-deficient |

Each of these methods is advantageous in certain situations. When speed is the only consideration, Algorithm 3.2.4 may be the best, and for $m\gg n$ it costs about half as much as the others. But solving the normal equations is not always stable in the presence of rounding errors, since $\kappa(A^{\mathsf T}A)=\kappa(A)^2$; numerical analysts therefore recommend Algorithm 3.2.5 instead. If $A$ is close to rank-deficient, Algorithm 3.2.5 itself has less than ideal stability properties, and Algorithm 3.2.6 is preferred. The figure compares the three on consistent systems ($\boldsymbol{b}=A\boldsymbol{x}$) with prescribed condition numbers.

![Relative error of the least squares solution for 100 x 10 matrices with prescribed condition numbers and b = A x. Householder QR and the SVD lose accuracy in proportion to kappa(A); the normal equations lose it in proportion to kappa(A)^2 and break down (the Cholesky factorization of A^T A fails) once kappa(A) exceeds about 10^8.](./plots/least-squares-accuracy.py)

## 3.3. Eigenvalue Problems

### 3.3.1. Basic Definitions

**Definition 3.3.1 (Eigenvalues and Eigenvectors)** Let $A\in\mathbb{C}^{m\times m}$ be square. A nonzero vector $\boldsymbol{x}\in\mathbb{C}^m$ is an **eigenvector** of $A$, and $\lambda\in\mathbb{C}$ its corresponding **eigenvalue**, if $A\boldsymbol{x}=\lambda\boldsymbol{x}$. The set of all eigenvalues of $A$ is the **spectrum** of $A$, a subset of $\mathbb{C}$ denoted by $\Lambda(A)$.

The idea is that the action of a matrix on a subspace $S$ of $\mathbb{C}^m$ may mimic scalar multiplication. The subspace $E_\lambda=\mathcal{N}(A-\lambda I)$ is the eigenspace of $\lambda$; any nonzero $\boldsymbol{x}\in E_\lambda$ is an eigenvector, and since $AE_\lambda\subseteq E_\lambda$, the eigenspace is invariant under $A$. Eigenvalue problems make sense only when the range and the domain of the map are the same space, and

$$
\det A=\prod_{j=1}^m\lambda_j,\qquad \operatorname{tr}(A)=\sum_{j=1}^m\lambda_j .
$$
A linear combination of eigenvectors for different eigenvalues is not an eigenvector. Over $\mathbb{C}$, every square matrix has at least one eigenvalue and eigenvector, by the fundamental theorem of algebra.

The **geometric multiplicity** of $\lambda$ is $\dim E_\lambda=\dim\mathcal{N}(A-\lambda I)$. The **characteristic polynomial** $p_A(z)=\det(zI-A)=(z-\lambda_1)(z-\lambda_2)\cdots(z-\lambda_m)$ has degree $m$; grouping equal roots, $p_A(z)=(z-\lambda_1)^{k_1}\cdots(z-\lambda_r)^{k_r}$, $r\le m$, and the **algebraic multiplicity** of $\lambda_j$ is its multiplicity $k_j$ as a root of $p_A$. The geometric multiplicity can never exceed the algebraic multiplicity. For

$$
A=\begin{bmatrix}1&2\\0&1\end{bmatrix},\qquad \det(A-\lambda I)=(1-\lambda)^2,\qquad A-I=\begin{bmatrix}0&2\\0&0\end{bmatrix},
$$
the eigenvalue $1$ has algebraic multiplicity $2$ but geometric multiplicity $1$.

The **minimal polynomial** $\mu_A$ of $A$ is the monic polynomial $P$ of least degree with $\mathbb{P}(A)=O$; any polynomial $Q$ with $Q(A)=O$ is a multiple of $\mu_A$. By the **Cayley–Hamilton theorem** a matrix satisfies its own characteristic equation, $p_A(A)=O$, so $\mu_A\mid p_A$: if $p_A(z)=\prod_j(z-\lambda_j)^{k_j}$, then $\mu_A(z)=\prod_j(z-\lambda_j)^{s_j}$ with $1\le s_j\le k_j$. In the **Jordan canonical form** of $A$ ([2.1.10](/2.1.10)), the geometric multiplicity of $\lambda$ is the number of Jordan blocks for $\lambda$, its algebraic multiplicity is the sum of their sizes, and its multiplicity $s_j$ in $\mu_A$ is the size of the largest one; $A$ is diagonalizable if and only if every Jordan block has size $1$, that is, if and only if $\mu_A$ has only simple roots.

The rank of a matrix is the number of its nonzero singular values, but it is not the number of its nonzero eigenvalues: $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ has rank $1$, $\sigma_1=1$, $\sigma_2=0$, but $\lambda_1=\lambda_2=0$. The two counts agree for diagonalizable matrices, where $\mathcal{N}(A)=E_0(A)$ and $\mathcal{R}(A)$ is the sum of the eigenspaces for $\lambda\ne0$.

**Example 3.3.1** Find a real matrix $A$ with $A^7=A^4$ and $A^2\ne A$. The minimal polynomial must satisfy $\mu_A(x)\mid x^7-x^4=x^4(x-1)(x^2+x+1)$ and $\mu_A(x)\nmid x^2-x=x(x-1)$. So we can simply take $\mu_A(x)=x^2$, $x^3$ or $x^4$, making $A$ nilpotent, for example

$$
A=\begin{bmatrix}0&1\\0&0\end{bmatrix},\quad A=\begin{bmatrix}0&1&\\&0&1\\&&0\end{bmatrix}\quad\text{or}\quad A=\begin{bmatrix}0&1&&\\&0&1&\\&&0&1\\&&&0\end{bmatrix}.
$$
Or let $\mu_A(x)=x^2+x+1$, whose roots are $\lambda=\frac{-1\pm\sqrt3\,\mathrm{i}}2$. Since $\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ has eigenvalues $a\pm b\mathrm{i}$, we can take the rotation by $120°$,

$$
A=\begin{bmatrix}-1/2&-\sqrt3/2\\\sqrt3/2&-1/2\end{bmatrix},
$$
for which $A^3=I$, hence $A^7=A=A^4$, while $A^2\ne A$.

**Example 3.3.2** Show that $A^4=5A+6I$ for $A=\begin{bmatrix}4&-2\\5&-3\end{bmatrix}$. The characteristic polynomial is $p_A(\lambda)=(4-\lambda)(-3-\lambda)+10=\lambda^2-\lambda-2$, with roots $\lambda_1=-1$, $\lambda_2=2$. By the Cayley–Hamilton theorem $A^2-A-2I=O$, so $A^2=A+2I$, $A^3=A^2+2A=3A+2I$ and $A^4=3A^2+2A=3(A+2I)+2A=5A+6I$. Alternatively, $f(x)=x^4-5x-6$ satisfies $f(\lambda_1)=f(\lambda_2)=0$, so $p_A\mid f$, and $p_A(A)=O$ implies $f(A)=O$.

The eigenvalues of a real matrix are real or occur in complex conjugate pairs; a real symmetric matrix has real eigenvalues and orthogonal eigenvectors. A quick way to check that a matrix is positive definite uses diagonal dominance.

**Definition 3.3.2 (Strict Diagonal Dominance)** $A$ is strictly (row) diagonally dominant if $\lvert a_{ii}\rvert>\sum_{j\ne i}\lvert a_{ij}\rvert$ for all $i$, and strictly column diagonally dominant if $\lvert a_{ii}\rvert>\sum_{j\ne i}\lvert a_{ji}\rvert$ for all $i$.

**Theorem 3.3.1 (Gershgorin Circle Theorem)** Every eigenvalue of $A$ lies within at least one of the Gershgorin discs $D\bigl(a_{ii},\sum_{j\ne i}\lvert a_{ij}\rvert\bigr)$, $i=1,\dots,m$.

**Proof** For an eigenvalue $\lambda$, scale the eigenvector $\boldsymbol{x}$ so that its largest component is $x_i=1$ and $\lvert x_j\rvert\le1$ for $j\ne i$. Row $i$ of $A\boldsymbol{x}=\lambda\boldsymbol{x}$ reads $\sum_{j\ne i}a_{ij}x_j+a_{ii}=\lambda$, so $\lvert\lambda-a_{ii}\rvert=\bigl\lvert\sum_{j\ne i}a_{ij}x_j\bigr\rvert\le\sum_{j\ne i}\lvert a_{ij}\rvert$. $\square$

**Corollary 3.3.1** A symmetric matrix with $a_{ii}>\sum_{j\ne i}\lvert a_{ij}\rvert$ for all $i$ is positive definite.

Indeed its eigenvalues are real and lie in discs contained in the right half-plane. The converse is false; a positive definite matrix only satisfies $\lvert a_{ij}\rvert<\sqrt{a_{ii}a_{jj}}\le(a_{ii}+a_{jj})/2$.

Eigenvalues are particularly useful for analyzing the behavior of systems governed by linear equations as they evolve, in terms of $A^t$ or $\mathrm{e}^{tA}=\sum_{n=0}^\infty\frac{(tA)^n}{n!}$ as $t\to\infty$: the study of resonance (for example of musical instruments or of bridges) and of stability (for example of fluid flows subjected to small perturbations). If $A$ has $m$ linearly independent eigenvectors, $A\boldsymbol{x}_j=\lambda_j\boldsymbol{x}_j$ is equivalent to $AX=X\Lambda$ with $X=[\boldsymbol{x}_1|\cdots|\boldsymbol{x}_m]$, $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_m)$, that is, $A=X\Lambda X^{-1}$. Then $X^{-1}A=\Lambda X^{-1}$ is a change of basis to "eigenvector coordinates", and $A^n=X\Lambda^nX^{-1}$.

### 3.3.2. The Power Method

To find the dominant eigenvalue of $A$ (the one of largest modulus, $\lvert\lambda_1\rvert>\lvert\lambda_i\rvert$ for $i\ne1$) and its eigenvector, we repeatedly multiply a vector by $A$.

**Algorithm 3.3.1 (Power Method)** Choose a random vector $\boldsymbol{q}_0\in\mathbb{R}^n$ with $\|\boldsymbol{q}_0\|=1$. For $k=1,2,\dots$, while $\|\boldsymbol{q}_{k-1}-\boldsymbol{q}_{k-2}\|>\varepsilon$: set $\boldsymbol{z}_k=A\boldsymbol{q}_{k-1}$, $\boldsymbol{q}_k=\boldsymbol{z}_k/\|\boldsymbol{z}_k\|$ and $\lambda^{(k)}=\boldsymbol{q}_k^{\mathsf T}A\boldsymbol{q}_k$.

**Theorem 3.3.2** Let $A\in\mathbb{R}^{n\times n}$ be diagonalizable with eigenvalues $\lvert\lambda_1\rvert>\lvert\lambda_2\rvert\ge\cdots\ge\lvert\lambda_n\rvert$ and unit eigenvectors $\boldsymbol{x}_1,\dots,\boldsymbol{x}_n$, and let $\boldsymbol{q}_0=\sum_ic_i\boldsymbol{x}_i$ with $c_1\ne0$. Then $\boldsymbol{q}_k$ converges, up to sign, to $\boldsymbol{x}_1$ with error $O(\lvert\lambda_2/\lambda_1\rvert^k)$, and $\lambda^{(k)}\to\lambda_1$.

**Proof** The $n$ independent eigenvectors form a basis of $\mathbb{R}^n$, and $c_1\ne0$ means that $\boldsymbol{q}_0$ has a component in the direction of $\boldsymbol{x}_1$. Then

$$
A^k\boldsymbol{q}_0=\sum_{i=1}^nc_iA^k\boldsymbol{x}_i=\sum_{i=1}^nc_i\lambda_i^k\boldsymbol{x}_i=c_1\lambda_1^k\Bigl(\boldsymbol{x}_1+\sum_{i=2}^n\frac{c_i}{c_1}\Bigl(\frac{\lambda_i}{\lambda_1}\Bigr)^k\boldsymbol{x}_i\Bigr).
$$
Since $\lambda_1$ is dominant, $(\lambda_i/\lambda_1)^k\to0$ and $A^k\boldsymbol{q}_0$ approaches the direction $c_1\lambda_1^k\boldsymbol{x}_1$. The power method only normalizes the products $A\boldsymbol{q}_{k-1}$ to avoid overflow or underflow, $\boldsymbol{q}_k=A^k\boldsymbol{q}_0/\|A^k\boldsymbol{q}_0\|$, so it converges to $\pm\boldsymbol{x}_1$, and the eigenvalue estimate satisfies $\boldsymbol{q}_k^{\mathsf T}A\boldsymbol{q}_k\approx\boldsymbol{q}_k^{\mathsf T}\lambda_1\boldsymbol{q}_k=\lambda_1$. $\square$

In practice the usefulness of the power method depends on the ratio $\lvert\lambda_2\rvert/\lvert\lambda_1\rvert$, which dictates the rate of convergence. The danger that $\boldsymbol{q}_0$ is deficient in $\boldsymbol{x}_1$ ($c_1=0$) is a less worrisome matter: if $\boldsymbol{q}_0$ is chosen randomly, the probability of $c_1=0$ is $0$, and rounding errors typically ensure that some $\boldsymbol{q}_k$ acquire a component in $\boldsymbol{x}_1$. Each iteration computes a single matrix-vector product, $O(n^2)$ flops, and if $A$ is sparse much less: even for very large $n$ the method is efficient, as in Google's PageRank algorithm. The method fails when the dominant eigenvalue is not unique in modulus, for example for a rotation matrix, whose eigenvalues $\mathrm{e}^{\pm\mathrm{i}\theta}$ have the same modulus: $\boldsymbol{q}_k$ just keeps rotating.

For a Hermitian matrix $A$ and a nonzero vector $\boldsymbol{q}$, the **Rayleigh quotient** $R(A,\boldsymbol{q})=\boldsymbol{q}^{\mathsf H}A\boldsymbol{q}/(\boldsymbol{q}^{\mathsf H}\boldsymbol{q})$ satisfies $\lambda_n\le R(A,\boldsymbol{q})\le\lambda_1$ (eigenvalues in decreasing order); $\lambda^{(k)}$ is the Rayleigh quotient of $\boldsymbol{q}_k$. For symmetric $A$ the Rayleigh quotient is stationary at eigenvectors, so the eigenvalue error is quadratic in the eigenvector error, $O(\lvert\lambda_2/\lambda_1\rvert^{2k})$.

![Power method for 50 x 50 symmetric matrices with lambda_1 = 1 and |lambda_2/lambda_1| = 0.5, 0.8, 0.95. The eigenvector error decreases like ratio^k (dashed lines), the eigenvalue error of the Rayleigh quotient like ratio^(2k), until both reach the level of rounding errors.](./plots/power-method-convergence.py)

**Example 3.3.3 (PageRank)** A search engine must crawl the web and locate all pages with public access, index the data so that it can be searched efficiently for keywords, and rate the importance of each page, so that when a user searches, the more important pages among those with the desired information are presented first. PageRank assigns to each page a numerical weight measuring its relative importance within the hyperlinked set of documents. For a web of four pages in which page $j$ distributes its importance equally among the pages it links to, the link matrix is

$$
A=\begin{bmatrix}0&0&1&\frac12\\\frac13&0&0&0\\\frac13&\frac12&0&\frac12\\\frac13&\frac12&0&0\end{bmatrix},
$$
and the importance scores solve $A\boldsymbol{x}=\boldsymbol{x}$: $\boldsymbol{x}$ is the eigenvector for the dominant eigenvalue $1$ of this column-stochastic matrix, here $\boldsymbol{x}\propto(12,4,9,6)^{\mathsf T}$. For the real web, with billions of pages, it is computed by the power method.

### 3.3.3. Eigenvalue-Revealing Factorizations

**Definition 3.3.3 (Eigenvalue Decomposition)** An **eigendecomposition** (spectral decomposition) of a square matrix $A$ is a factorization

$$
A=X\Lambda X^{-1}
$$
with nonsingular $X$ and diagonal $\Lambda$. An eigenvalue whose algebraic multiplicity exceeds its geometric multiplicity is a **defective eigenvalue**, and a matrix that has one or more defective eigenvalues is a **defective matrix**.

**Theorem 3.3.3** A square matrix $A$ has an eigenvalue decomposition $A=X\Lambda X^{-1}$ if and only if it is nondefective, that is, diagonalizable.

Such a decomposition does not always exist, and R does not warn about it:

```r
A <- matrix(c(1, 0, 2, 1), 2)    # rows (1, 2) and (0, 1)
eigen(A)
```

```text
eigen() decomposition
$values
[1] 1 1

$vectors
     [,1]          [,2]
[1,]    1 -1.000000e+00
[2,]    0  1.110223e-16
```

The two computed eigenvectors are parallel up to rounding, so the matrix $X$ is numerically singular. When the decomposition exists it is not unique (eigenvectors can be rescaled and reordered, and any basis of a multidimensional eigenspace will do). Even then, if $X$ is highly ill-conditioned, a great deal of information may be discarded in passing from $A$ to $\Lambda$.

*Unitary diagonalization.* $A$ is unitarily diagonalizable if there is a unitary $Q$ with $A=Q\Lambda Q^{\mathsf H}$: the $m$ linearly independent eigenvectors can be chosen to be orthonormal.

**Theorem 3.3.4** A matrix is unitarily diagonalizable if and only if it is normal, $A^{\mathsf H}A=AA^{\mathsf H}$.

Examples of a **normal matrix** are Hermitian ($A=A^{\mathsf H}$), skew-Hermitian ($A=-A^{\mathsf H}$), unitary ($A^{-1}=A^{\mathsf H}$) and circulant matrices, and any of these plus $kI$. Symmetry explains $\|A\|_2=\sigma_1$ and $\|A^{-1}\|_2=1/\sigma_m$: since $B=A^{\mathsf H}A$ is Hermitian, $\mathbb{C}^n$ has an orthonormal basis $\boldsymbol{e}_1,\dots,\boldsymbol{e}_n$ of eigenvectors of $B$, with eigenvalues $\lambda_1,\dots,\lambda_n\ge0$. For $\boldsymbol{x}=a_1\boldsymbol{e}_1+\cdots+a_n\boldsymbol{e}_n$,

$$
\|A\boldsymbol{x}\|_2^2=\boldsymbol{x}^{\mathsf H}A^{\mathsf H}A\boldsymbol{x}=\langle\boldsymbol{x},B\boldsymbol{x}\rangle=\langle\boldsymbol{x},a_1\lambda_1\boldsymbol{e}_1+\cdots+a_n\lambda_n\boldsymbol{e}_n\rangle=\sum_j\lambda_j\lvert a_j\rvert^2\le\max_j\lambda_j\,\|\boldsymbol{x}\|_2^2,
$$
so $\|A\|_2\le\sqrt{\max_j\lambda_j}=\sigma_1$, with equality for $\boldsymbol{x}=\boldsymbol{e}_{j_0}$, the eigenvector of the largest eigenvalue; applied to $A^{-1}$ this gives $\|A^{-1}\|_2=1/\sigma_m$.

Normal matrices are also those whose eigenvalues are perfectly conditioned. For a general diagonalizable matrix the sensitivity depends on the eigenvector matrix.

**Theorem 3.3.5 (Bauer–Fike Theorem)** Let $A\in\mathbb{C}^{n\times n}$ be diagonalizable, $A=X\Lambda X^{-1}$, and let $\mu$ be an eigenvalue of $A+\delta A$. Then for any $p$-norm

$$
\min_{\lambda\in\Lambda(A)}\lvert\lambda-\mu\rvert\le\kappa_p(X)\,\|\delta A\|_p .
$$

For normal $A$, $X$ can be taken unitary, $\kappa_2(X)=1$: if $\lambda$ and $\lambda+\delta\lambda$ are corresponding eigenvalues of $A$ and $A+\delta A$, then $\lvert\delta\lambda\rvert\le\|\delta A\|_2$. Thus the absolute condition number of the symmetric (indeed of the normal) eigenvalue problem is $\hat\kappa=1$.

**Definition 3.3.4 (Schur Decomposition)** A **Schur decomposition** (unitary triangularization) of a square matrix $A$ is a factorization $A=QTQ^{\mathsf H}$ with unitary $Q$ and upper triangular $T$. A real Schur decomposition of a real matrix $A$ is $A=QTQ^{\mathsf T}$ with orthogonal $Q$ and quasi-upper-triangular $T$ (block upper triangular with $1\times1$ and $2\times2$ blocks on the diagonal, the $2\times2$ blocks carrying complex conjugate pairs of eigenvalues).

Since $A$ and $T$ are similar, the eigenvalues of $A$ appear on the diagonal of $T$. By the **Schur triangularization theorem** ([2.1.12](/2.1.12)), every square matrix has a Schur decomposition.

**Example 3.3.4** The matrix

$$
A=\begin{bmatrix}-2&4&0&-1\\8&-1&0&4\\-2&1&1&9\\7&7&-1&-1\end{bmatrix}
$$
has eigenvalues $\lambda_1=6.1429$, $\lambda_{2,3}=-0.6175\pm1.7365\mathrm{i}$, $\lambda_4=-7.9078$. Its real Schur decomposition $A=QTQ^{\mathsf T}$ has

$$
T=Q^{\mathsf T}AQ=\begin{bmatrix}6.1429&7.1693&-2.3027&-2.8451\\0&-0.6175&-11.0418&0.4232\\0&0.2731&-0.6175&-0.9995\\0&0&0&-7.9078\end{bmatrix},
$$
with a $2\times2$ diagonal block whose eigenvalues are $-0.6175\pm\mathrm{i}\sqrt{11.0418\times0.2731}=-0.6175\pm1.7365\mathrm{i}$.

**Algorithm 3.3.2 (QR Algorithm)** Let $A$ be a real matrix whose eigenvalues we want. Set $A_0=A$. For $k=0,1,2,\dots$: compute the QR decomposition $A_k=Q_kR_k$ and set $A_{k+1}=R_kQ_k$.

Since $A_{k+1}=R_kQ_k=Q_k^{-1}Q_kR_kQ_k=Q_k^{-1}A_kQ_k$, all the $A_k$ are similar and have the same eigenvalues. If $\lvert\lambda_1\rvert>\lvert\lambda_2\rvert>\cdots>\lvert\lambda_n\rvert$, the $A_k$ converge to an upper triangular matrix $T$, a Schur form of $A$, whose diagonal lists the eigenvalues. Practical versions first reduce $A$ to upper Hessenberg form by Householder reflections and use shifts to accelerate convergence; `eigen` calls such LAPACK routines (with a specialized one for symmetric matrices).

The three eigenvalue-revealing factorizations, which reduce a matrix to a form in which the eigenvalues are explicitly displayed, are nested:

- a diagonalization $A=X\Lambda X^{-1}$ exists if and only if $A$ is nondefective;
- a unitary diagonalization $A=Q\Lambda Q^{\mathsf H}$ exists if and only if $A$ is normal;
- a unitary triangularization (Schur decomposition) $A=QTQ^{\mathsf H}$ always exists.

So Schur (all square matrices) $\supset$ eigendecomposition (diagonalizable matrices) $\supset$ unitary diagonalization (normal matrices), in terms of the matrices they apply to; the Schur form is the general basis of numerical eigenvalue computations.

### 3.3.4. SVD versus Eigendecomposition

For a unitarily diagonalizable $A=Q\Lambda Q^{\mathsf H}$, this is an eigendecomposition, and $A=Q\lvert\Lambda\rvert\bigl(\operatorname{sgn}(\Lambda)Q^{\mathsf H}\bigr)=U\Sigma V^{\mathsf H}$ with $U=Q$, $\Sigma=\lvert\Lambda\rvert$ and $V=Q\,\overline{\operatorname{sgn}(\Lambda)}$, where $\operatorname{sgn}(\Lambda)=\operatorname{diag}(\lambda_j/\lvert\lambda_j\rvert)$ (and $1$ for $\lambda_j=0$), gives an SVD (after reordering by decreasing $\lvert\lambda_j\rvert$). Hence a singular value is also an eigenvalue when $A$ is symmetric positive semidefinite (more generally, Hermitian positive semidefinite), and then the SVD and the eigendecomposition coincide. In general $\sigma_1=\|A\|_2\ge\|A\boldsymbol{x}\|/\|\boldsymbol{x}\|=\lvert\lambda\rvert$ for every eigenpair, so $\sigma_1\ge\lvert\lambda_1\rvert$.

The two factorizations share the theme of diagonalizing a matrix, but:

| | Eigendecomposition $A=X\Lambda X^{-1}$ | SVD $A=U\Sigma V^{\mathsf H}$ |
|---|---|---|
| Applies to | square, nondefective matrices | all matrices, even rectangular |
| Bases | one basis (the eigenvectors), generally not orthogonal | two orthonormal bases (left and right singular vectors) |
| Diagonal entries | complex in general | real, nonnegative |
| Relevant to | behavior of $A^k$ or $\mathrm{e}^{tA}$ | behavior of $A$ itself or of $A^{-1}$ |

## Summary

There is no best algorithm, only the most suitable one for the problem.

| Problem | Tool | Stability and cost |
|---|---|---|
| Linear system $A\boldsymbol{x}=\boldsymbol{b}$ | LU with partial pivoting, $PA=LU$; for SPD $A$, Cholesky $A=R^{\mathsf T}R$ | pivoting is needed for LU; Cholesky is stable without it and costs half |
| Least squares $A\boldsymbol{x}\approx\boldsymbol{b}$ | Householder QR, the standard; SVD for singular or nearly singular $A$ | normal equations amplify errors by $\kappa(A)^2$; QR is stable; SVD most robust and most expensive |
| Matrix structure (rank, compression, PCA) | SVD, for any matrix | singular values order the directions by importance; best low-rank approximation |
| Eigenvalues, powers, long-term behavior | eigendecomposition for $A^k$; Schur form for any square matrix; power method for the dominant eigenvalue of large sparse matrices | normal matrices have perfectly conditioned eigenvalues |

| Operation | Flops (leading term) |
|---|---|
| Triangular solve | $m^2$ |
| LU decomposition (Gaussian elimination) | $\frac23m^3$ |
| Cholesky decomposition | $\frac13m^3$ |
| Gram–Schmidt QR (classical or modified) | $2mn^2$ |
| Householder QR | $2mn^2-\frac23n^3$ |
| Givens QR | $3mn^2-n^3$ |
| Least squares via normal equations / QR / SVD | $mn^2+\frac13n^3$ / $2mn^2-\frac23n^3$ / $2mn^2+11n^3$ |

The key facts: orthogonal transformations do not amplify errors ($\|QA\|_2=\|A\|_2$), which is the basis of the stability of QR and the SVD; solving the normal equations $A^{\mathsf T}A\boldsymbol{x}=A^{\mathsf T}\boldsymbol{b}$ squares the condition number; modified Gram–Schmidt and classical Gram–Schmidt are equivalent in exact arithmetic but not in floating point; a matrix is diagonalizable if and only if geometric and algebraic multiplicities agree, unitarily diagonalizable if and only if it is normal, and always triangularizable by a unitary similarity; the SVD exists for every matrix, with $\sigma_i=\sqrt{\lambda_i(A^{\mathsf H}A)}$; and the power method converges to the eigenvector of the eigenvalue of largest modulus at the rate $\lvert\lambda_2/\lambda_1\rvert$.
