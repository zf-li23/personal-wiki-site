---
title: Matrix Functions
source_hash: 0ab5431b4579
---

This chapter answers two questions. First, a complex number has the polar form $z = r\mathrm{e}^{\mathrm{i}\theta}$; can a matrix likewise be written as "a stretch times a rotation", $A = R\mathrm{e}^{\mathrm{i}M}$? This requires a definition of $\mathrm{e}^{\mathrm{i}M}$, and the answer is the polar decomposition of [Chapter 13](/2.1.13). Second, the solution of the scalar equation $x'(t) = kx(t)$ is $x(t) = x(0)\mathrm{e}^{kt}$; can the solution of the system $\boldsymbol{X}'(t) = A\boldsymbol{X}(t)$ be written as $\boldsymbol{X}(t) = \mathrm{e}^{At}\boldsymbol{X}(0)$? Both questions require extending a complex function $f\colon \mathbb{C} \to \mathbb{C}$ to a map $f\colon \mathbb{C}^{n\times n} \to \mathbb{C}^{n\times n}$ on matrices.

Discrete mathematics has already defined the **matrix exponential** by a power series and discussed its relation to Lie groups ([1.3.5](/1.3.5)). This chapter gives three equivalent definitions of $f(A)$ (the spectral definition via the Jordan canonical form, interpolation polynomials, and power series) together with the corresponding three algorithms, and compares their costs. The preparation consists of carrying limits, derivatives and series from calculus ([2.2](/2.2)) over to matrices; the main tools are the Jordan canonical form and the minimal polynomial of the [previous chapter](/2.1.10), and the **Lagrange interpolation polynomial** of [Chapter 9](/2.1.9). The central result is that $f(A)$ depends only on finitely many values of $f$ and its derivatives at the eigenvalues of $A$, so computing $f(A)$ reduces to solving a linear system. The last section uses the matrix exponential to solve systems of linear differential equations with constant coefficients, the starting point of ordinary differential equations ([2.4](/2.4)).

## 11.1. Matrix-Valued Functions

**Definition 11.1.1** A matrix $A(x) = (a_{ij}(x))_{m \times n}$ whose entries are real functions $a_{ij}(x)$ on an interval $[a, b]$ is called a **matrix-valued function**.

For example, $A(x) = \begin{bmatrix} \sin x & \mathrm{e}^x & 1 \\ 3x^2 & 0 & x - 1 \end{bmatrix}$. Constant matrices are special cases of matrix-valued functions. Addition, multiplication by a function $k(x)$, multiplication $A(x)B(x) = \left(\sum_k a_{ik}(x)b_{kj}(x)\right)$ and transposition are defined as for constant matrices.

**Definition 11.1.2** Let $A(x)$ be a matrix-valued function of order $n$. If there is a matrix-valued function $B(x)$ of order $n$ with $A(x)B(x) = B(x)A(x) = I$ for every $x \in [a, b]$, then $A(x)$ is called invertible on $[a, b]$, and we write $B(x) = A^{-1}(x)$. The largest order of a minor of $A(x)$ that does not vanish identically is called the rank of $A(x)$; a matrix-valued function of order $n$ and rank $n$ is said to have full rank.

**Theorem 11.1.1** A matrix-valued function $A(x)$ of order $n$ is invertible on $[a, b]$ $\Leftrightarrow$ $\det A(x)$ vanishes nowhere on $[a, b]$. In that case $A^{-1}(x) = \dfrac{1}{\det A(x)}\operatorname{adj}A(x)$, where $\operatorname{adj}A(x)$ is the **adjugate matrix**.

Unlike for constant matrices, full rank does not imply invertibility: for $A(x) = \begin{bmatrix} x & 0 \\ 0 & 1 \end{bmatrix}$ on $[-1, 1]$, $\det A(x) = x$ does not vanish identically, so the rank is $2$; but $\det A(0) = 0$, so $A(x)$ is not invertible on $[-1, 1]$. Full rank only requires that the determinant not vanish identically; invertibility requires that it vanish nowhere.

**Definition 11.1.3** If every entry of $A(x)$ has a limit at $x_0$ (is continuous, differentiable), then $A(x)$ is said to have a limit at $x_0$ (be continuous, differentiable), and we define entrywise

$$
\lim_{x \to x_0} A(x) = \left(\lim_{x \to x_0} a_{ij}(x)\right), \qquad A'(x) = \frac{\mathrm{d}A}{\mathrm{d}x} = \left(a_{ij}'(x)\right), \qquad \int_a^b A(x)\,\mathrm{d}x = \left(\int_a^b a_{ij}(x)\,\mathrm{d}x\right).
$$

**Property 11.1.1** Let $A(x)$ and $B(x)$ be differentiable, with sizes for which the operations make sense.

1. $(A + B)' = A' + B'$, $(A^{\mathsf T})' = (A')^{\mathsf T}$, $(\operatorname{tr}(A))' = \operatorname{tr}(A')$;
2. $(AB)' = A'B + AB'$; the order of the factors cannot be changed, so $(A^2)' = A'A + AA'$, which in general differs from $2AA'$;
3. if $A(x)$ is invertible, then $(A^{-1})' = -A^{-1}A'A^{-1}$ (differentiate $AA^{-1} = I$);
4. if $x = u(t)$ is differentiable, then $\dfrac{\mathrm{d}}{\mathrm{d}t}A(u(t)) = A'(u(t))\,u'(t)$.

## 11.2. Linear Dependence of Vector-Valued Functions

**Definition 11.2.1** Let $\boldsymbol{\alpha}_1(x), \dots, \boldsymbol{\alpha}_m(x)$ be continuous $n$-dimensional vector-valued functions on $[a, b]$. If there are real numbers $k_1, \dots, k_m$, not all zero, such that $k_1\boldsymbol{\alpha}_1(x) + \cdots + k_m\boldsymbol{\alpha}_m(x) = \boldsymbol{0}$ for all $x \in [a, b]$, they are called linearly dependent on $[a, b]$; otherwise they are called linearly independent.

The coefficients must be constants. Checking the definition directly requires the identity to hold for infinitely many $x$ at once; the following two methods reduce it to the rank of a single constant matrix.

**Definition 11.2.2** The matrix $G = (g_{ij})$ of order $m$ with $g_{ij} = \displaystyle\int_a^b \boldsymbol{\alpha}_i^{\mathsf T}(x)\boldsymbol{\alpha}_j(x)\,\mathrm{d}x$ is called the **Gram matrix** of $\boldsymbol{\alpha}_1(x), \dots, \boldsymbol{\alpha}_m(x)$, and $\det G$ is called the Gram determinant.

**Theorem 11.2.1** Continuous vector-valued functions $\boldsymbol{\alpha}_1(x), \dots, \boldsymbol{\alpha}_m(x)$ on $[a, b]$ are linearly independent $\Leftrightarrow$ their Gram matrix has full rank.

**Proof** Suppose $\sum_j k_j\boldsymbol{\alpha}_j(x) = \boldsymbol{0}$ (\*). Multiplying on the left by $\boldsymbol{\alpha}_i^{\mathsf T}(x)$ and integrating gives $\sum_j g_{ij}k_j = 0$, that is, $G\boldsymbol{k} = \boldsymbol{0}$ with $\boldsymbol{k} = (k_1, \dots, k_m)^{\mathsf T}$. If $G$ has full rank, then $\boldsymbol{k} = \boldsymbol{0}$ and the functions are linearly independent. If $G$ does not have full rank, take a nonzero solution of $G\boldsymbol{k} = \boldsymbol{0}$ and let $\boldsymbol{\alpha}(x) = \sum_i k_i\boldsymbol{\alpha}_i(x)$; then

$$
\int_a^b \boldsymbol{\alpha}^{\mathsf T}(x)\boldsymbol{\alpha}(x)\,\mathrm{d}x = \boldsymbol{k}^{\mathsf T}G\boldsymbol{k} = 0.
$$

The integrand $\|\boldsymbol{\alpha}(x)\|^2$ is continuous and nonnegative, so $\boldsymbol{\alpha}(x) \equiv \boldsymbol{0}$: (\*) has a nonzero solution and the functions are linearly dependent. $\square$

The entry $g_{ij}$ is the inner product of $\boldsymbol{\alpha}_i$ and $\boldsymbol{\alpha}_j$ with respect to the integral inner product; the [next chapter](/2.1.12) shows that the Gram matrix is the metric matrix of a set of vectors in a general inner product space. If the functions are smooth enough, derivatives provide another criterion.

**Definition 11.2.3** Let $\boldsymbol{\alpha}_1(x), \dots, \boldsymbol{\alpha}_m(x)$ have derivatives of order $m - 1$ on $[a, b]$, and let $A(x)$ be the $m \times n$ matrix-valued function whose $i$-th row is $\boldsymbol{\alpha}_i^{\mathsf T}(x)$. The $m \times mn$ matrix $W(x) = \left(A(x), A'(x), \dots, A^{(m-1)}(x)\right)$ is called the **Wronskian matrix** of $\boldsymbol{\alpha}_1(x), \dots, \boldsymbol{\alpha}_m(x)$.

**Theorem 11.2.2** If there is $x_0 \in [a, b]$ such that the constant matrix $W(x_0)$ has rank $m$, then $\boldsymbol{\alpha}_1(x), \dots, \boldsymbol{\alpha}_m(x)$ are linearly independent on $[a, b]$.

**Proof** Suppose not. If $\sum_j k_j\boldsymbol{\alpha}_j(x) = \boldsymbol{0}$ has a nonzero solution $\boldsymbol{k}$, differentiating repeatedly gives $\sum_j k_j\boldsymbol{\alpha}_j^{(l)}(x) = \boldsymbol{0}$ ($l = 0, \dots, m - 1$); at $x_0$ this reads $W^{\mathsf T}(x_0)\boldsymbol{k} = \boldsymbol{0}$ in matrix form, so $\operatorname{rank}(W(x_0)) < m$, a contradiction. $\square$

This condition is only sufficient. Take $n = 1$, $\boldsymbol{\alpha}_1(x) = x^2$ and $\boldsymbol{\alpha}_2(x) = x|x|$. They are linearly independent on $[-1, 1]$ (equal on $[0, 1]$, opposite on $[-1, 0]$), but the determinant $2x^2|x| - 2x^2|x|$ of $W(x) = \begin{bmatrix} x^2 & 2x \\ x|x| & 2|x| \end{bmatrix}$ vanishes identically.

## 11.3. Sequences and Series of Matrices

**Definition 11.3.1** Let $A_k = (a_{ij}^{(k)}) \in \mathbb{C}^{n\times n}$. If each of the $n^2$ sequences $\{a_{ij}^{(k)}\}$ converges to $a_{ij}$, the sequence of matrices $\{A_k\}$ is said to converge with limit $A = (a_{ij})$, written $\lim_{k \to \infty}A_k = A$; otherwise it diverges.

**Property 11.3.1** If $A_k \to A$ and $B_k \to B$, then

1. $aA_k + bB_k \to aA + bB$ ($a, b \in \mathbb{C}$);
2. $A_kB_k \to AB$;
3. $PA_kQ \to PAQ$ ($P, Q$ fixed matrices);
4. if $A$ and all $A_k$ are invertible, then $A_k^{-1} \to A^{-1}$ (by the adjugate formula, the entries of the inverse are continuous functions of the entries).

Convergence of the powers $A^k$ depends only on the eigenvalues.

**Definition 11.3.2** The **spectral radius** of $A \in \mathbb{C}^{n\times n}$ is $\rho(A) = \max\{|\lambda| : \lambda \text{ is an eigenvalue of } A\}$.

**Theorem 11.3.1** $\lim_{k \to \infty}A^k = O$ $\Leftrightarrow$ $\rho(A) < 1$.

**Proof** By the Jordan canonical form $A = PJP^{-1}$ we have $A^k = PJ^kP^{-1}$, so it suffices to consider a single Jordan block. Write $J_{\lambda,m} = \lambda I + N$ with $N^m = O$; since $\lambda I$ and $N$ commute, the binomial theorem gives

$$
J_{\lambda,m}^k = \sum_{j=0}^{m-1} \binom{k}{j}\lambda^{k-j}N^j,
$$

whose entries are $\binom{k}{j}\lambda^{k-j}$ ($0 \le j \le m - 1$). If $|\lambda| < 1$, a polynomial in $k$ times $|\lambda|^k$ tends to zero; if $|\lambda| \ge 1$, the diagonal entry $\lambda^k$ does not tend to zero. $\square$

The spectral radius and norms are related as follows. For any eigenvalue $\lambda$ with unit eigenvector $\boldsymbol{x}$, $|\lambda| = \|A\boldsymbol{x}\| \le \|A\|_2$, so $\rho(A)$ never exceeds the **spectral norm**; one can show that $\rho(A) = \lim_{k\to\infty}\|A^k\|_2^{1/k}$. The spectral radius determines the eventual exponential rate of growth of $A^k$, but the behavior over the first steps also depends on how far $A$ is from being "normal": in the figure below, two matrices both have spectral radius $0.9$, but for the upper triangular one $\|A^k\|_2$ first grows to about $6$ before it starts to decay. This phenomenon is related to the normal matrices of the [next chapter](/2.1.12).

![Spectral norm of the powers of three 2 x 2 matrices as a function of k: the spectral radius determines the limiting behavior, while the non-normal matrix shows transient growth](./plots/matrix-powers-spectral-radius.py)

**Definition 11.3.3** The expression $A_1 + A_2 + \cdots$ is called a **matrix series**, and $S_k = A_1 + \cdots + A_k$ is its partial sum. If $\lim_{k \to \infty}S_k = S$, the series converges with sum $S = \sum_{k=1}^\infty A_k$; otherwise it diverges. If all $n^2$ numerical series $\sum_k a_{ij}^{(k)}$ converge absolutely, the matrix series is said to converge absolutely.

Clearly, a matrix series converges if and only if all $n^2$ numerical series converge, and the entries of the sum are their sums.

**Theorem 11.3.2** Let $A \in \mathbb{C}^{n\times n}$. Then $\sum_{k=0}^\infty A^k$ converges $\Leftrightarrow$ $\rho(A) < 1$, and in that case $\sum_{k=0}^\infty A^k = (I - A)^{-1}$.

**Proof** If the series converges, its general term $A^k \to O$, so $\rho(A) < 1$ by Theorem 11.3.1. Conversely, if $\rho(A) < 1$, then $1$ is not an eigenvalue of $A$ and $I - A$ is invertible. From $(I - A)(I + A + \cdots + A^k) = I - A^{k+1} \to I$, the partial sums tend to $(I - A)^{-1}$. $\square$

**Theorem 11.3.3** Write $|A| = \max_{i,j}|a_{ij}|$.

1. $\sum_k A_k$ converges absolutely $\Leftrightarrow$ the numerical series $\sum_k |A_k|$ converges;
2. if $\sum_k A_k$ converges absolutely and $P, Q$ are fixed matrices, then $\sum_k PA_kQ$ also converges absolutely and $\sum_k PA_kQ = P\left(\sum_k A_k\right)Q$;
3. (comparison test) if $B_k = (b_{ij}^{(k)})$ has nonnegative entries, $|a_{ij}^{(k)}| \le b_{ij}^{(k)}$, and $\sum_k B_k$ converges, then $\sum_k A_k$ converges absolutely.

**Proof** 1: $|a_{ij}^{(k)}| \le |A_k| \le \sum_{i,j}|a_{ij}^{(k)}|$; now use the comparison test for numerical series. 2: every entry of $PA_kQ$ has modulus at most $n^2|P||A_k||Q|$. 3: compare entry by entry. $\square$

## 11.4. Polynomials in a Matrix

We begin with the simplest case: $f(x) = a_kx^k + \cdots + a_1x + a_0$ is a polynomial and $f(A) = a_kA^k + \cdots + a_1A + a_0I$. By Lemma 10.5.1 of the [previous chapter](/2.1.10), $f(P^{-1}AP) = P^{-1}f(A)P$, and a polynomial in a block diagonal matrix is the block diagonal matrix of the polynomials in the blocks. So if $P^{-1}AP = J = \operatorname{diag}(J_{\mu_1, m_{11}}, \dots)$ is the Jordan canonical form, then

$$
f(A) = Pf(J)P^{-1} = P\operatorname{diag}\left(f(J_{\mu_1, m_{11}}), \dots\right)P^{-1},
$$

and the problem reduces to evaluating a polynomial at a single Jordan block.

**Theorem 11.4.1** Let $f$ be a polynomial and $J_{\lambda,m}$ a Jordan block of order $m$. Then

$$
f(J_{\lambda,m}) = \begin{bmatrix} f(\lambda) & f'(\lambda) & \frac{1}{2!}f''(\lambda) & \cdots & \frac{1}{(m-1)!}f^{(m-1)}(\lambda) \\ & f(\lambda) & f'(\lambda) & \ddots & \vdots \\ & & \ddots & \ddots & \frac{1}{2!}f''(\lambda) \\ & & & f(\lambda) & f'(\lambda) \\ & & & & f(\lambda) \end{bmatrix} = \sum_{j=0}^{m-1} \frac{f^{(j)}(\lambda)}{j!}N^j. \tag{11.1}
$$

**Proof** By **Taylor's formula**, the expansion $f(x) = \sum_{j \ge 0} \frac{f^{(j)}(\lambda)}{j!}(x - \lambda)^j$ of the polynomial $f$ about $\lambda$ is a finite sum and holds exactly. Substitute $x = J_{\lambda,m} = \lambda I + N$, where $N = J_{0,m}$ satisfies $N^m = O$ and $N^j$ is the matrix with ones on the $j$-th superdiagonal and zeros elsewhere. $\square$

**Example 11.4.1** Let $J_{2,3} = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}$ and $f(x) = x^3$. Then $f(2) = 8$, $f'(2) = 12$ and $\frac{1}{2}f''(2) = 6$, so $J_{2,3}^3 = \begin{bmatrix} 8 & 12 & 6 \\ 0 & 8 & 12 \\ 0 & 0 & 8 \end{bmatrix}$.

Hence computing $f(A)$ only requires the derivatives of $f$ of order up to $m_i - 1$ at each eigenvalue $\mu_i$, where $m_i$ is the order of the largest Jordan block for $\mu_i$, that is, the multiplicity of $\mu_i$ in the minimal polynomial. This observation yields the definition for general functions.

## 11.5. The Spectral Definition of a Matrix Function

**Definition 11.5.1 (Spectrum of a Matrix)** Let the minimal polynomial of $A \in \mathbb{C}^{n\times n}$ be $m_A(\lambda) = (\lambda - \mu_1)^{m_1}\cdots(\lambda - \mu_s)^{m_s}$, the $\mu_i$ distinct. The set $\sigma(A) = \{\mu_1, \dots, \mu_s\}$ is called the **spectrum** of $A$. Let $f$ be a complex function. If

$$
f(\mu_i), f'(\mu_i), \dots, f^{(m_i - 1)}(\mu_i), \qquad i = 1, \dots, s
$$

are all defined, $f$ is said to be defined on the spectrum of $A$, and these $m = \deg m_A$ numbers are called the values of $f$ on the spectrum of $A$.

**Definition 11.5.2** Let $f$ be defined on the spectrum of $A$ and let $P^{-1}AP = J$ be the Jordan canonical form. Define $f(J_{\lambda,k})$ for Jordan blocks by Eq. (11.1); the following $f(A)$ is called a **matrix function**:

$$
f(A) = Pf(J)P^{-1} = P\operatorname{diag}\left(f(J_{\mu_1, m_{11}}), \dots, f(J_{\mu_s, m_{st_s}})\right)P^{-1}.
$$

Theorem 11.6.1 will show that $f(A)$ does not depend on the choice of the Jordan basis $P$. For multivalued functions (such as $\ln z$ or $\sqrt{z}$) a branch must be fixed near each eigenvalue, and different branches give different $f(A)$.

**Property 11.5.1** Let $f$ and $g$ be defined on the spectrum of $A$, and $\det(\lambda I - A) = \prod_i(\lambda - \mu_i)^{n_i}$.

1. $P^{-1}f(A)P = f(P^{-1}AP)$, and $f(A)$ commutes with $A$;
2. $(f + g)(A) = f(A) + g(A)$ and $(fg)(A) = f(A)g(A)$ (apply the Leibniz rule to Eq. (11.1));
3. $\det(\lambda I - f(A)) = \prod_i (\lambda - f(\mu_i))^{n_i}$, that is, the eigenvalues of $f(A)$ are the $f(\mu_i)$, with the same multiplicities ($f(J)$ is upper triangular);
4. $\mathrm{e}^A$ is always invertible, with $(\mathrm{e}^A)^{-1} = \mathrm{e}^{-A}$ (by 2 and $\mathrm{e}^z\mathrm{e}^{-z} = 1$; alternatively, 3 gives $\det \mathrm{e}^A = \prod \mathrm{e}^{n_i\mu_i} \ne 0$);
5. if $A$ is diagonalizable, $P^{-1}AP = \operatorname{diag}(\mu_1I_{n_1}, \dots, \mu_sI_{n_s})$, then $f(A) = P\operatorname{diag}(f(\mu_1)I_{n_1}, \dots, f(\mu_s)I_{n_s})P^{-1}$ is also diagonalizable.

**Example 11.5.1** Let $J = J_{0,3}$ and $f(z) = \sin z$. Then $m_J = \lambda^3$, $f(0) = 0$, $f'(0) = 1$ and $f''(0) = 0$, so $\sin J = J$.

**Example 11.5.2** Let $A = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 2 & 0 & 1 & 0 \\ 0 & -2 & 0 & 0 \\ 4 & 0 & 2 & 0 \end{bmatrix}$; we compute $\mathrm{e}^A$. We have $\det(\lambda I_4 - A) = \lambda^4$, $\operatorname{rank}(A) = 2$, $\operatorname{rank}(A^2) = 1$ and $A^3 = O$, so $J = \operatorname{diag}(J_{0,3}, J_{0,1})$ and $m_A = \lambda^3$. Take the Jordan basis $P = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ -2 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 \end{bmatrix}$ (columns 1, 2, 3 form a Jordan chain and column 4 is another eigenvector). For $f(z) = \mathrm{e}^z$ we have $f(0) = f'(0) = f''(0) = 1$, so

$$
\mathrm{e}^J = \operatorname{diag}\left(\begin{bmatrix} 1 & 1 & \frac12 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}, 1\right), \qquad \mathrm{e}^A = P\mathrm{e}^JP^{-1} = \begin{bmatrix} 2 & 1 & \frac12 & 0 \\ 2 & 1 & 1 & 0 \\ -2 & -2 & 0 & 0 \\ 4 & 0 & 2 & 1 \end{bmatrix}.
$$

**Example 11.5.3** If $A \ne O$ and $A^2 = O$, then $m_A = \lambda^2$, and the only Jordan blocks are $J_{0,2}$ and $J_{0,1}$. Since $\mathrm{e}^{J_{0,2}} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = I + J_{0,2}$ and $\mathrm{e}^{J_{0,1}} = 1$, we get $\mathrm{e}^J = I + J$ and $\mathrm{e}^A = P(I + J)P^{-1} = I + A$.

## 11.6. The Interpolation Method

In Example 11.5.2, $A^3 = O$, and it seems quicker to observe directly that $\mathrm{e}^A = I + A + \frac{1}{2}A^2$: the right-hand side is exactly the Taylor polynomial of degree $2$ of $f(z) = \mathrm{e}^z$ at $0$. In general, $f(A)$ always equals the value at $A$ of some polynomial of low degree.

**Theorem 11.6.1** Let $m_A(\lambda) = \prod_{i=1}^s(\lambda - \mu_i)^{m_i}$, $m = \deg m_A$, and let $f$ be defined on the spectrum of $A$. Then there is a unique polynomial $r(z)$ of degree less than $m$ with

$$
r^{(j)}(\mu_i) = f^{(j)}(\mu_i), \qquad i = 1, \dots, s, \quad j = 0, 1, \dots, m_i - 1,
$$

and $f(A) = r(A)$. The polynomial $r(z)$ is called the *Hermite interpolation polynomial* of $f$ on the spectrum of $A$; it is also called the Hermite–Lagrange interpolation polynomial.

**Proof** The polynomials of degree less than $m$ form an $m$-dimensional space, and the map $r \mapsto \left(r^{(j)}(\mu_i)\right)_{i,j} \in \mathbb{C}^m$ is linear. It is injective: if all these values vanish, then $(z - \mu_i)^{m_i} \mid r$ for every $i$, hence $m_A \mid r$, and since $\deg r < m$, $r = 0$. As the dimensions agree, the map is also surjective, so $r$ exists and is unique. For each Jordan block $J_{\mu_i, k}$ of $A$ ($k \le m_i$), Eq. (11.1) uses only $f^{(j)}(\mu_i)$ with $j < k$, so $f(J_{\mu_i,k}) = r(J_{\mu_i,k})$ and $f(A) = Pr(J)P^{-1} = r(A)$. The right-hand side does not involve $P$, so Definition 11.5.2 does not depend on the choice of the Jordan basis. $\square$

When all $m_i = 1$ ($A$ diagonalizable), $r$ is the Lagrange interpolation polynomial through the points $(\mu_i, f(\mu_i))$, and so

$$
f(A) = \sum_{i=1}^s f(\mu_i)\prod_{j \ne i}\frac{A - \mu_jI}{\mu_i - \mu_j}.
$$

Theorem 11.6.1 turns the computation of $f(A)$ into solving a linear system of order $m$ (a Vandermonde system with derivative conditions); no Jordan basis is needed.

**Algorithm 11.6.1 (Method of Undetermined Coefficients)** Input: $A$ and a function $f$ defined on the spectrum of $A$.

1. Find the minimal polynomial $m_A(\lambda) = \prod_{i=1}^s(\lambda - \mu_i)^{m_i}$ of $A$, $m = \sum_i m_i$. If the minimal polynomial is not known, the characteristic polynomial can be used instead (it is also an annihilating polynomial; only the system is larger).
2. Set $r(z) = a_0 + a_1z + \cdots + a_{m-1}z^{m-1}$.
3. Write down the $m$ linear equations $r^{(j)}(\mu_i) = f^{(j)}(\mu_i)$ and solve for $a_0, \dots, a_{m-1}$.
4. $f(A) = r(A) = a_0I + a_1A + \cdots + a_{m-1}A^{m-1}$.

**Example 11.6.1** Let $A = \begin{bmatrix} -4 & 2 & 10 \\ -4 & 3 & 7 \\ -3 & 1 & 7 \end{bmatrix}$; we compute $\cos A$. Here $\det(\lambda I - A) = (\lambda - 2)^3$ and $\operatorname{rank}(2I - A) = 2$, so there is a single Jordan block and $m_A = (\lambda - 2)^3$. Set $r(z) = a_0 + a_1z + a_2z^2$. From $r(2) = \cos 2$, $r'(2) = -\sin 2$ and $r''(2) = -\cos 2$:

$$
\begin{cases} a_0 + 2a_1 + 4a_2 = \cos 2, \\ a_1 + 4a_2 = -\sin 2, \\ 2a_2 = -\cos 2, \end{cases} \qquad a_0 = 2\sin 2 - \cos 2, \quad a_1 = 2\cos 2 - \sin 2, \quad a_2 = -\tfrac12\cos 2.
$$

Therefore

$$
\cos A = a_0I + a_1A + a_2A^2 = \begin{bmatrix} 2\cos 2 + 6\sin 2 & -2\sin 2 & -2\cos 2 - 10\sin 2 \\ \frac12\cos 2 + 4\sin 2 & \cos 2 - \sin 2 & -\cos 2 - 7\sin 2 \\ \frac12\cos 2 + 3\sin 2 & -\sin 2 & -5\sin 2 \end{bmatrix}.
$$

**Example 11.6.2** Let $A = \begin{bmatrix} 3 & -3 & 2 \\ -1 & 5 & -2 \\ -1 & 3 & 0 \end{bmatrix}$; we compute $\ln A$, $\sin\frac{\pi}{4}A$ and $\mathrm{e}^A$. Here $\det(\lambda I - A) = (\lambda - 2)^2(\lambda - 4)$, so the minimal polynomial is $(\lambda - 2)^2(\lambda - 4)$ or $(\lambda - 2)(\lambda - 4)$; since $\operatorname{rank}(A - 2I) = 1$, the eigenvalue $2$ has two Jordan blocks and $m_A = (\lambda - 2)(\lambda - 4)$. Set $r(z) = a_0 + a_1z$.

- $\ln$: $a_0 + 2a_1 = \ln 2$ and $a_0 + 4a_1 = 2\ln 2$ give $a_0 = 0$, $a_1 = \frac12\ln 2$, so $\ln A = \frac{\ln 2}{2}A$.
- $\sin\frac{\pi}{4}z$: $a_0 + 2a_1 = 1$ and $a_0 + 4a_1 = 0$ give $a_0 = 2$, $a_1 = -\frac12$, so $\sin\frac{\pi}{4}A = 2I - \frac12A = \begin{bmatrix} \frac12 & \frac32 & -1 \\ \frac12 & -\frac12 & 1 \\ \frac12 & -\frac32 & 2 \end{bmatrix}$.
- $\mathrm{e}^z$: $a_0 + 2a_1 = \mathrm{e}^2$ and $a_0 + 4a_1 = \mathrm{e}^4$, so $\mathrm{e}^A = (2\mathrm{e}^2 - \mathrm{e}^4)I + \frac12(\mathrm{e}^4 - \mathrm{e}^2)A$.

The code below solves the Vandermonde system with derivative conditions of Algorithm 11.6.1 to compute $\mathrm{e}^A$, and compares the result with SciPy's `expm`.

```python
import numpy as np
from math import factorial
from scipy.linalg import expm

def matrix_function(A, spectrum, derivs):
    """f(A) by Hermite interpolation on the spectrum.

    spectrum: list of (eigenvalue, multiplicity in the minimal polynomial)
    derivs:   derivs(mu, j) returns the j-th derivative of f at mu
    """
    m = sum(k for _, k in spectrum)              # degree of m_A
    V = np.zeros((m, m), dtype=complex)          # confluent Vandermonde matrix
    b = np.zeros(m, dtype=complex)
    row = 0
    for mu, k in spectrum:
        for j in range(k):                       # condition r^{(j)}(mu) = f^{(j)}(mu)
            for p in range(j, m):
                V[row, p] = factorial(p) / factorial(p - j) * mu ** (p - j)
            b[row] = derivs(mu, j)
            row += 1
    a = np.linalg.solve(V, b)                    # coefficients of r(z)
    R, P = np.zeros_like(A, dtype=complex), np.eye(len(A))
    for coef in a:                               # accumulate a_0 I + a_1 A + ...
        R += coef * P
        P = P @ A
    return R

A = np.array([[-4., 2, 10], [-4, 3, 7], [-3, 1, 7]])     # m_A = (z - 2)^3
E = matrix_function(A, [(2, 3)], lambda mu, j: np.exp(mu))
print(np.abs(E - expm(A)).max())                         # ~1e-13
B = np.array([[3., -3, 2], [-1, 5, -2], [-1, 3, 0]])     # m_B = (z - 2)(z - 4)
E = matrix_function(B, [(2, 1), (4, 1)], lambda mu, j: np.exp(mu))
print(np.abs(E - expm(B)).max())
```

The interpolation method is convenient for small matrices and exact computation, but it needs accurate eigenvalues and multiplicities, and the Vandermonde system with derivative conditions is ill-conditioned when eigenvalues are close together. The `expm` of numerical software uses "scaling and squaring" combined with rational approximation: it first computes $\mathrm{e}^{A/2^s}$ (with $\|A/2^s\|$ small, by Padé approximation) and then squares the result $s$ times.

## 11.7. The Power Series Definition

The third definition simply replaces $z$ by $A$ in a power series; it agrees with the definition of the matrix exponential in [1.3.5](/1.3.5). Let $S(z) = \sum_{p=0}^\infty a_pz^p$ have radius of convergence $R$: it converges absolutely for $|z| < R$ and diverges for $|z| > R$, and the series differentiated term by term has the same radius of convergence ([2.2.8](/2.2.8)). Common expansions are

$$
\mathrm{e}^z = \sum_{p=0}^\infty \frac{z^p}{p!}, \quad \sin z = \sum_{p=0}^\infty \frac{(-1)^pz^{2p+1}}{(2p+1)!}, \quad \cos z = \sum_{p=0}^\infty \frac{(-1)^pz^{2p}}{(2p)!} \quad (R = +\infty), \qquad \ln(1 + z) = \sum_{p=1}^\infty \frac{(-1)^{p-1}z^p}{p} \quad (R = 1).
$$

**Definition 11.7.1** For $A \in \mathbb{C}^{n\times n}$, let $S(A) = \sum_{p=0}^\infty a_pA^p$; if the partial sums $S_p(A) = a_0I + \cdots + a_pA^p$ converge, $S(A)$ is said to converge.

**Theorem 11.7.1** Let the power series $S(z)$ have radius of convergence $R$ and sum $f(z)$ for $|z| < R$. If all eigenvalues of $A$ satisfy $|\mu_i| < R$ (that is, $\rho(A) < R$), then $S(A)$ converges absolutely and $S(A) = f(A)$, where $f(A)$ is computed by the spectral definition. If some $|\mu_i| > R$, then $S(A)$ diverges.

**Proof** $S_p(A) = PS_p(J)P^{-1}$. By Eq. (11.1), the entries of $S_p(J_{\lambda,k})$ are $\frac{1}{j!}S_p^{(j)}(\lambda)$, the partial sums of the $j$-th derived series of $S$. For $|\lambda| < R$ these converge absolutely to $\frac{1}{j!}f^{(j)}(\lambda)$, so $S_p(J) \to f(J)$; for $|\lambda| > R$ the diagonal entries $S_p(\lambda)$ diverge. $\square$

Note the direction of the statement: it is not that "if $S(z)$ has radius of convergence $R$, then $|\mu_i| < R$"; rather, as in the theorem above, the series converges when all eigenvalues lie inside the disk of convergence.

By Theorem 11.7.1, $\mathrm{e}^A$, $\sin A$ and $\cos A$ converge for every $A$; for $\rho(A) < 1$, $\ln(I + A) = A - \frac12A^2 + \frac13A^3 - \cdots$, and $\sum_k A^k = (I - A)^{-1}$ (Theorem 11.3.2) is exactly the case $f(z) = \frac{1}{1 - z}$. For matrices satisfying special relations, power series can be summed directly:

**Example 11.7.1** If $A^2 = O$, then $\mathrm{e}^A = I + A$, $\sin A = A$ and $\cos A = I$ (in agreement with Example 11.5.3). If $A^2 = A$, then $A^k = A$ ($k \ge 1$), and

$$
\mathrm{e}^A = I + \left(1 + \frac{1}{2!} + \frac{1}{3!} + \cdots\right)A = I + (\mathrm{e} - 1)A.
$$

## 11.8. The Matrix Exponential

**Definition 11.8.1 (Matrix Exponential)** For $A \in \mathbb{C}^{n\times n}$ and $t \in \mathbb{R}$ (or $\mathbb{C}$),

$$
\mathrm{e}^{At} = \sum_{k=0}^\infty \frac{t^k}{k!}A^k = I + tA + \frac{t^2}{2!}A^2 + \cdots.
$$

By Theorem 11.7.1, the series converges absolutely for all $A$ and $t$ and equals the matrix function of $f(z) = \mathrm{e}^{tz}$ at $A$.

**Theorem 11.8.1** Let $A, B \in \mathbb{C}^{n\times n}$ and let $P$ be invertible.

1. If $AB = BA$, then $\mathrm{e}^{A+B} = \mathrm{e}^A\mathrm{e}^B$;
2. $\mathrm{e}^{P^{-1}AP} = P^{-1}\mathrm{e}^AP$;
3. $\det \mathrm{e}^A = \mathrm{e}^{\operatorname{tr}(A)}$;
4. $\dfrac{\mathrm{d}}{\mathrm{d}t}\mathrm{e}^{At} = A\mathrm{e}^{At} = \mathrm{e}^{At}A$.

**Proof** 1: When $A$ and $B$ commute, the binomial theorem holds, and the Cauchy product of the two absolutely convergent series can be rearranged exactly as in the proof of $\mathrm{e}^{x+y} = \mathrm{e}^x\mathrm{e}^y$. 2: Property 11.5.1. 3: By part 3 of Property 11.5.1, the eigenvalues of $\mathrm{e}^A$ are $\mathrm{e}^{\lambda_1}, \dots, \mathrm{e}^{\lambda_n}$ (with multiplicity), whose product is $\mathrm{e}^{\lambda_1 + \cdots + \lambda_n}$. 4: Differentiate the power series term by term. $\square$

The commutativity hypothesis cannot be dropped: for $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ and $B = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}$ we have $\mathrm{e}^A\mathrm{e}^B = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$, whereas $A + B$ has eigenvalues $\pm 1$ and $\mathrm{e}^{A+B} = \begin{bmatrix} \cosh 1 & \sinh 1 \\ \sinh 1 & \cosh 1 \end{bmatrix}$.

To compute $\mathrm{e}^{At}$, use $P^{-1}AP = J$ to get $\mathrm{e}^{At} = P\mathrm{e}^{Jt}P^{-1}$. For a Jordan block, the two terms of $J_{\lambda,m}t = \lambda tI + tN$ commute, so

$$
\mathrm{e}^{J_{\lambda,m}t} = \mathrm{e}^{\lambda t}\mathrm{e}^{tN} = \mathrm{e}^{\lambda t}\left(I + tN + \frac{t^2}{2!}N^2 + \cdots + \frac{t^{m-1}}{(m-1)!}N^{m-1}\right). \tag{11.2}
$$

This is also what Eq. (11.1) gives for $f(z) = \mathrm{e}^{tz}$ ($f^{(j)}(\lambda) = t^j\mathrm{e}^{\lambda t}$). Note that the superdiagonal of $tJ_{\lambda,m}$ consists of $t$'s; it is not itself a Jordan block, and Eq. (11.1) must not be applied to it as if it were.

**Example 11.8.1** Let $A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$, so $m_A = \lambda^2 + 1$ and the spectrum is $\{\mathrm{i}, -\mathrm{i}\}$. By interpolation, set $r(z) = a_0 + a_1z$; from $a_0 + \mathrm{i}a_1 = \mathrm{e}^{\mathrm{i}t}$ and $a_0 - \mathrm{i}a_1 = \mathrm{e}^{-\mathrm{i}t}$ we get $a_0 = \cos t$ and $a_1 = \sin t$, so

$$
\mathrm{e}^{At} = \cos t\,I + \sin t\,A = \begin{bmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{bmatrix}.
$$

Since $A^2 = -I$, the matrix $A$ plays the role of the imaginary unit here, and this identity is the matrix version of **Euler's formula** $\mathrm{e}^{\mathrm{i}t} = \cos t + \mathrm{i}\sin t$; $\{\mathrm{e}^{At}\}$ is the **one-parameter subgroup** of plane rotations.

**Example 11.8.2** If $P^{-1}AP = J = \operatorname{diag}(J_{2,1}, J_{4,2})$, then by Eq. (11.2)

$$
\mathrm{e}^{At} = P\begin{bmatrix} \mathrm{e}^{2t} & 0 & 0 \\ 0 & \mathrm{e}^{4t} & t\mathrm{e}^{4t} \\ 0 & 0 & \mathrm{e}^{4t} \end{bmatrix}P^{-1}.
$$

**Theorem 11.8.2** Let $B \in \mathbb{C}^{n\times n}$. There is an $X$ with $\mathrm{e}^X = B$ $\Leftrightarrow$ $B$ is invertible.

**Proof** Necessity: $\det \mathrm{e}^X = \mathrm{e}^{\operatorname{tr}(X)} \ne 0$. Sufficiency: by part 2 of Theorem 11.8.1, it suffices to find $X$ for each Jordan block $J_{\lambda,k}$ ($\lambda \ne 0$) of $B$. Write $J_{\lambda,k} = \lambda(I + M)$ with $M = \lambda^{-1}N$ nilpotent. Choose a logarithm $\ell$ of $\lambda$ ($\mathrm{e}^\ell = \lambda$) and let

$$
X = \ell I + L, \qquad L = \ln(I + M) = M - \frac{M^2}{2} + \cdots + \frac{(-1)^kM^{k-1}}{k-1},
$$

a finite series because $M^k = O$. The formal power series identity $\exp(\ln(1 + z)) = 1 + z$ remains valid when a nilpotent matrix is substituted, so $\mathrm{e}^L = I + M$; since $\ell I$ and $L$ commute, $\mathrm{e}^X = \mathrm{e}^\ell \mathrm{e}^L = \lambda(I + M) = J_{\lambda,k}$. $\square$

Logarithms are not unique: $\mathrm{e}^{2\pi \mathrm{i} I} = I = \mathrm{e}^O$. A real matrix need not have a real logarithm either; for example, $\operatorname{diag}(-1, 2)$ has none: for a real matrix $X$, the Jordan blocks of $\mathrm{e}^X$ for negative eigenvalues always occur in pairs (they come from a pair of complex conjugate eigenvalues $\ell, \bar\ell$ of $X$).

## 11.9. Systems of Linear Differential Equations with Constant Coefficients

Let $\boldsymbol{X}(t) = (x_1(t), \dots, x_n(t))^{\mathsf T}$ and let $A \in \mathbb{C}^{n\times n}$ be a constant matrix; we solve $\boldsymbol{X}'(t) = A\boldsymbol{X}(t)$. Imitating the scalar case: $\mathrm{e}^{-At}$ commutes with $A$, so by Property 11.1.1 and Theorem 11.8.1,

$$
\left(\mathrm{e}^{-At}\boldsymbol{X}(t)\right)' = -A\mathrm{e}^{-At}\boldsymbol{X}(t) + \mathrm{e}^{-At}\boldsymbol{X}'(t) = \mathrm{e}^{-At}\left(\boldsymbol{X}'(t) - A\boldsymbol{X}(t)\right).
$$

**Theorem 11.9.1** The system $\boldsymbol{X}'(t) = A\boldsymbol{X}(t)$ with initial value $\boldsymbol{X}(0) = \boldsymbol{x}_0$ has a unique solution, namely $\boldsymbol{X}(t) = \mathrm{e}^{At}\boldsymbol{x}_0$. Consequently the general solution is $\boldsymbol{X}(t) = \mathrm{e}^{At}\boldsymbol{c}$, an arbitrary linear combination of the columns of $\mathrm{e}^{At}$.

**Proof** By part 4 of Theorem 11.8.1, $\mathrm{e}^{At}\boldsymbol{x}_0$ is a solution. Conversely, if $\boldsymbol{X}(t)$ is a solution, the right-hand side above vanishes, so $\mathrm{e}^{-At}\boldsymbol{X}(t)$ is a constant vector, equal to $\boldsymbol{X}(0) = \boldsymbol{x}_0$; hence $\boldsymbol{X}(t) = \mathrm{e}^{At}\boldsymbol{x}_0$. $\square$

**Corollary 11.9.1** Let $P^{-1}AP = J$. The general solution of $\boldsymbol{X}'(t) = A\boldsymbol{X}(t)$ is $\boldsymbol{X}(t) = P\mathrm{e}^{Jt}\boldsymbol{c}$ (with $\boldsymbol{c} = P^{-1}\boldsymbol{x}_0$ an arbitrary constant vector). Explicitly, if $\boldsymbol{p}_1, \dots, \boldsymbol{p}_k$ is a Jordan chain for the eigenvalue $\lambda$ ($\boldsymbol{p}_1$ an eigenvector), it yields $k$ linearly independent solutions

$$
\mathrm{e}^{\lambda t}\boldsymbol{p}_1, \quad \mathrm{e}^{\lambda t}(t\boldsymbol{p}_1 + \boldsymbol{p}_2), \quad \mathrm{e}^{\lambda t}\left(\frac{t^2}{2!}\boldsymbol{p}_1 + t\boldsymbol{p}_2 + \boldsymbol{p}_3\right), \quad \dots, \quad \mathrm{e}^{\lambda t}\sum_{j=1}^{k}\frac{t^{k-j}}{(k-j)!}\boldsymbol{p}_j.
$$

**Proof** $P\mathrm{e}^{Jt}\boldsymbol{c} = \mathrm{e}^{At}P\boldsymbol{c}$ is a solution, and $P\boldsymbol{c}$ ranges over all of $\mathbb{C}^n$. The columns of $P\mathrm{e}^{Jt}$ can be read off from Eq. (11.2). $\square$

One can check that a function of the form $\mathrm{e}^{\lambda t}\left(\frac{t^{k-1}}{(k-1)!}\boldsymbol{\alpha}_1 + \cdots + t\boldsymbol{\alpha}_{k-1} + \boldsymbol{\alpha}_k\right)$ ($\boldsymbol{\alpha}_1 \ne \boldsymbol{0}$) is a solution if and only if $\boldsymbol{\alpha}_1, \dots, \boldsymbol{\alpha}_k$ is a Jordan chain for $\lambda$. So solving the system amounts to finding Jordan chains.

For a real matrix of order $2$, the eigenvalues and the Jordan structure of $A$ determine the shape of the trajectories $\boldsymbol{X}(t) = \mathrm{e}^{At}\boldsymbol{x}_0$ (see the figure below): when the two real eigenvalues have the same sign, the trajectories enter or leave the origin (a node), and when they have opposite signs the origin is a saddle; a pair of complex conjugate eigenvalues $a \pm b\mathrm{i}$ produces spirals, and for $a = 0$ the trajectories are closed curves (a center, the rotation of Example 11.8.1). The two Jordan forms with a double eigenvalue give different pictures: for $A = \lambda I$ every vector is an eigenvector and the trajectories are rays; when $A$ is similar to $J_{\lambda,2}$, the term $t\mathrm{e}^{\lambda t}$ appears in the solutions and all trajectories approach the origin along the single eigenvector direction.

![Phase portraits of six 2 x 2 matrices: each curve is a trajectory exp(tA)x_0, arrows point in the direction of increasing t, and dashed lines are the lines of real eigenvectors. The middle and right matrices of the bottom row have the same eigenvalues (the double eigenvalue -1) and differ only in their Jordan block structure](./plots/phase-portraits.py)

**Example 11.9.1** Solve

$$
\begin{cases} x_1' = 6x_1 + 2x_2 + 2x_3, \\ x_2' = -2x_1 + 2x_2, \\ x_3' = 2x_3, \end{cases} \qquad A = \begin{bmatrix} 6 & 2 & 2 \\ -2 & 2 & 0 \\ 0 & 0 & 2 \end{bmatrix}.
$$

Here $\det(\lambda I - A) = (\lambda - 2)(\lambda - 4)^2$ and $\operatorname{rank}(A - 4I) = 2$, so there is only one block for $4$ and $J = \operatorname{diag}(2, J_{4,2})$. Solving $(A - 2I)\boldsymbol{x} = \boldsymbol{0}$ gives $\boldsymbol{p}_1 = (0, -1, 1)^{\mathsf T}$; $(A - 4I)\boldsymbol{x} = \boldsymbol{0}$ gives $\boldsymbol{p}_2 = (2, -2, 0)^{\mathsf T}$; and $(A - 4I)\boldsymbol{x} = \boldsymbol{p}_2$ gives $\boldsymbol{p}_3 = (1, 0, 0)^{\mathsf T}$. The general solution is

$$
\boldsymbol{X}(t) = c_1\mathrm{e}^{2t}\begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix} + c_2\mathrm{e}^{4t}\begin{bmatrix} 2 \\ -2 \\ 0 \end{bmatrix} + c_3\mathrm{e}^{4t}\left(t\begin{bmatrix} 2 \\ -2 \\ 0 \end{bmatrix} + \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}\right).
$$

For a given initial value $\boldsymbol{X}(0) = \boldsymbol{x}_0$, $\boldsymbol{c} = P^{-1}\boldsymbol{x}_0$ with $P = (\boldsymbol{p}_1, \boldsymbol{p}_2, \boldsymbol{p}_3)$. For example, for $\boldsymbol{x}_0 = (1, 0, 0)^{\mathsf T} = \boldsymbol{p}_3$ we get $\boldsymbol{c} = (0, 0, 1)^{\mathsf T}$ and $\boldsymbol{X}(t) = \mathrm{e}^{4t}(1 + 2t, -2t, 0)^{\mathsf T}$.

The solution of an inhomogeneous system consists of a homogeneous solution plus the "accumulated response" to the input.

**Theorem 11.9.2** Let $B \in \mathbb{C}^{n \times m}$ and let $\boldsymbol{u}(t)$ be a continuous $m$-dimensional vector-valued function. The system $\boldsymbol{X}'(t) = A\boldsymbol{X}(t) + B\boldsymbol{u}(t)$ with $\boldsymbol{X}(0) = \boldsymbol{x}_0$ has a unique solution, namely

$$
\boldsymbol{X}(t) = \mathrm{e}^{At}\boldsymbol{x}_0 + \int_0^t \mathrm{e}^{A(t-\tau)}B\boldsymbol{u}(\tau)\,\mathrm{d}\tau. \tag{11.3}
$$

**Proof** Let $\boldsymbol{X}(t)$ be a solution. Then $\left(\mathrm{e}^{-At}\boldsymbol{X}(t)\right)' = \mathrm{e}^{-At}\left(\boldsymbol{X}' - A\boldsymbol{X}\right) = \mathrm{e}^{-At}B\boldsymbol{u}(t)$. Integrating from $0$ to $t$ gives $\mathrm{e}^{-At}\boldsymbol{X}(t) - \boldsymbol{x}_0 = \int_0^t \mathrm{e}^{-A\tau}B\boldsymbol{u}(\tau)\,\mathrm{d}\tau$, and multiplying both sides on the left by $\mathrm{e}^{At}$ yields Eq. (11.3); this also proves uniqueness. Differentiating directly verifies that Eq. (11.3) is indeed a solution. $\square$

Eq. (11.3) is called the *variation of constants formula*: replacing the constant vector $\boldsymbol{c}$ in the homogeneous solution $\mathrm{e}^{At}\boldsymbol{c}$ by a function $\boldsymbol{c}(t)$ and substituting into the equation gives $\boldsymbol{c}'(t) = \mathrm{e}^{-At}B\boldsymbol{u}(t)$. It is the basic formula for the response of a linear system in control theory.

A system $\boldsymbol{X}'(t) = A(t)\boldsymbol{X}(t)$ with time-dependent coefficients generally cannot be solved by a matrix exponential: $\mathrm{e}^{\int_0^tA(s)\mathrm{d}s}$ is a solution only when $A(t)$ commutes with $\int_0^tA(s)\,\mathrm{d}s$. In general, $\mathrm{e}^{At}$ is replaced by the fundamental matrix $\Phi(t)$ ($\Phi' = A\Phi$, $\Phi(0) = I$), which satisfies $\det\Phi(t) = \mathrm{e}^{\int_0^t\operatorname{tr}(A(s))\,\mathrm{d}s}$, and the solution of the inhomogeneous system is $\boldsymbol{X}(t) = \Phi(t)\boldsymbol{x}_0 + \Phi(t)\int_0^t\Phi^{-1}(\tau)B(\tau)\boldsymbol{u}(\tau)\,\mathrm{d}\tau$. These topics belong to the course on ordinary differential equations.

## Summary

| Topic | Result |
|---|---|
| Matrix-valued functions | Operations and calculus are defined entrywise; invertible $\Leftrightarrow$ determinant nonzero everywhere; $(AB)' = A'B + AB'$, $(A^{-1})' = -A^{-1}A'A^{-1}$ |
| Dependence of vector-valued functions | Gram matrix of full rank $\Leftrightarrow$ independent (Theorem 11.2.1); Wronskian matrix of full rank at one point $\Rightarrow$ independent (Theorem 11.2.2) |
| Sequences and series of matrices | $A^k \to O \Leftrightarrow \rho(A) < 1$; $\sum A^k = (I - A)^{-1} \Leftrightarrow \rho(A) < 1$; absolute convergence via $\sum \lvert A_k\rvert$ |
| Matrix functions | Depend only on $f^{(j)}(\mu_i)$, $j < m_i$; the three definitions agree (Theorems 11.6.1, 11.7.1) |
| Matrix exponential | $\mathrm{e}^{A+B} = \mathrm{e}^A\mathrm{e}^B$ for commuting $A, B$; $\det \mathrm{e}^A = \mathrm{e}^{\operatorname{tr}(A)}$; $\mathrm{e}^X = B$ is solvable $\Leftrightarrow$ $B$ invertible |
| Systems of differential equations | $\boldsymbol{X}' = A\boldsymbol{X}$: $\boldsymbol{X} = \mathrm{e}^{At}\boldsymbol{x}_0$, fundamental solutions from Jordan chains; inhomogeneous case: variation of constants formula (11.3) |

The three methods for computing $f(A)$ compare as follows.

| Method | What is needed | Main computation | When to use |
|---|---|---|---|
| Jordan representation $f(A) = Pf(J)P^{-1}$ | Jordan form and Jordan basis $P$ | Solve systems chain by chain, compute $P^{-1}$ | Theoretical arguments; when the structure of $f(A)$ is also needed (e.g., fundamental solutions of differential systems) |
| Interpolation (Algorithm 11.6.1) | Minimal (or characteristic) polynomial and the values of $f$ on the spectrum | Solve a linear system of order $m$, compute powers up to $A^{m-1}$ | Small matrices, exact computation; no $P$ needed |
| Power series | $\rho(A)$ smaller than the radius of convergence | Truncate the series | Direct summation when $A$ satisfies relations such as $A^k = O$ or $A^2 = A$; numerically combined with scaling and rational approximation |

The three methods reduce "functions of a matrix" to three standard problems: computing a Jordan form, solving one linear system, and summing a numerical series. The interpolation method best reflects the approach of this course: a problem that seems to require infinitely much information is broken down into finitely many numbers and one linear system.
