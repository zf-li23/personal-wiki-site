---
title: Systems of Linear Differential Equations
source_hash: 799b4933554f
---

This chapter studies first-order **systems of linear differential equations** $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)$. Such a system is the vector form of the first-order linear equation $x'=a(t)x+f(t)$, and the resemblance is more than formal: global existence of solutions, the structure "particular solution plus general solution of the homogeneous equation", and the variation of constants formula all carry over unchanged, except that the number $\mathrm{e}^{\int a}$ is replaced by a matrix $\Phi(t)$. Linear systems are also the foundation of the nonlinear theory: the behavior of a nonlinear equation near an equilibrium point is determined by its linearization ([2.4.11](/2.4.11)), and the derivatives of solutions with respect to initial values satisfy the linear variational equation ([2.4.7](/2.4.7)). The next chapter treats $n$th-order linear equations as a special case of this one.

These results and the common methods of solution were introduced in calculus ([Section 16.6 of 2.2.16](/2.2.16#sec-16.6)), and systems with constant coefficients were solved with matrix functions in linear algebra ([Section 11.9 of 2.1.11](/2.1.11#sec-11.9)). This chapter gives the rigorous theory: the proof of global existence and uniqueness, the solution space and fundamental matrices, Liouville's formula, the general variation of constants formula, the convergence and properties of the matrix exponential, and the structure of solutions obtained from the Jordan canonical form. Routine computations are kept brief, with references to the two chapters above.

## 8.1. Global Existence and Uniqueness

### 8.1.1. Systems and Norms

**Definition 8.1.1 (System of Linear Differential Equations)** Let $A(t)=(a_{ij}(t))$ be an $n\times n$ matrix-valued function and $\boldsymbol{f}(t)$ an $n$-dimensional vector-valued function on an interval $I$. The system

$$
\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)\tag{8.1}
$$
is called a **system of linear differential equations**. When $\boldsymbol{f}\equiv\boldsymbol{0}$ it is called a homogeneous system,

$$
\boldsymbol{x}'=A(t)\boldsymbol{x},\tag{8.2}
$$
and otherwise a nonhomogeneous system; when $A$ is a constant matrix, it is called a system with constant coefficients. Throughout, $A(t)$ and $\boldsymbol{f}(t)$ are assumed continuous on $I$, and they may be complex-valued.

Continuity, differentiation and integration of matrix-valued functions are defined entrywise ([Section 11.1 of 2.1.11](/2.1.11#sec-11.1)). The product rule $(AB)'=A'B+AB'$ holds, but the order of the matrix factors matters.

Estimates require norms. Fix a norm $\|\boldsymbol{x}\|$ on $\mathbb{C}^n$ (for example $\sum_i\lvert x_i\rvert$ or the Euclidean norm; all norms on a finite-dimensional space are equivalent), and give matrices the corresponding operator norm $\|A\|=\max_{\|\boldsymbol{x}\|=1}\|A\boldsymbol{x}\|$. This is a **matrix norm**, and it satisfies

$$
\|A\boldsymbol{x}\|\le\|A\|\,\|\boldsymbol{x}\|,\qquad\|A+B\|\le\|A\|+\|B\|,\qquad\|AB\|\le\|A\|\,\|B\|;
$$
moreover, for vector-valued functions, $\big\|\int_a^b\boldsymbol{g}(s)\,\mathrm{d}s\big\|\le\int_a^b\|\boldsymbol{g}(s)\|\,\mathrm{d}s$. The quantity $\sum_{i,j}\lvert a_{ij}\rvert$, which is also often used, is not an operator norm, but it satisfies the last two inequalities as well, and the arguments below remain valid for it.

### 8.1.2. The Existence and Uniqueness Theorem

The general **existence and uniqueness theorem** ([2.4.4](/2.4.4), [2.4.7](/2.4.7)) gives only local solutions. The special feature of linear systems is that their solutions exist on the whole interval on which the coefficients are continuous: the right-hand side grows at most linearly in $\boldsymbol{x}$, so solutions cannot become infinite in finite time.

**Theorem 8.1.1** Let $A(t)$ and $\boldsymbol{f}(t)$ be continuous on an interval $I$. Then for any $t_0\in I$ and $\boldsymbol{\eta}\in\mathbb{C}^n$, the **initial value problem**

$$
\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t),\qquad\boldsymbol{x}(t_0)=\boldsymbol{\eta}
$$
has a unique solution on the whole of $I$.

**Proof** The initial value problem is equivalent to the integral equation $\boldsymbol{x}(t)=\boldsymbol{\eta}+\int_{t_0}^t\big(A(s)\boldsymbol{x}(s)+\boldsymbol{f}(s)\big)\,\mathrm{d}s$. Take any bounded closed interval $J\subset I$ containing $t_0$, and let $L=\max_J\|A(t)\|$. Form the Picard iterates

$$
\boldsymbol{x}_0(t)=\boldsymbol{\eta},\qquad\boldsymbol{x}_{k+1}(t)=\boldsymbol{\eta}+\int_{t_0}^t\big(A(s)\boldsymbol{x}_k(s)+\boldsymbol{f}(s)\big)\,\mathrm{d}s.
$$
They are all defined and continuous on the whole of $J$ (unlike the nonlinear case, where one has to restrict to a small interval to keep $\boldsymbol{x}_k$ within the domain). With $M=\max_J\|\boldsymbol{x}_1(t)-\boldsymbol{x}_0(t)\|$, induction gives

$$
\|\boldsymbol{x}_{k+1}(t)-\boldsymbol{x}_k(t)\|\le\Big\lvert\int_{t_0}^tL\|\boldsymbol{x}_k(s)-\boldsymbol{x}_{k-1}(s)\|\,\mathrm{d}s\Big\rvert\le\frac{ML^k\lvert t-t_0\rvert^k}{k!},\qquad t\in J.
$$
The sum of the right-hand sides, $M\mathrm{e}^{L\lvert J\rvert}$, is finite, so by the Weierstrass M-test the sequence $\boldsymbol{x}_k$ is **uniformly convergent** on $J$ to a continuous function $\boldsymbol{x}(t)$; passing to the limit in the integral equation shows that $\boldsymbol{x}$ is a solution.

Uniqueness: let $\boldsymbol{x},\boldsymbol{y}$ be two solutions on $J$. Then $\boldsymbol{z}=\boldsymbol{x}-\boldsymbol{y}$ satisfies $\boldsymbol{z}(t)=\int_{t_0}^tA(s)\boldsymbol{z}(s)\,\mathrm{d}s$. With $K=\max_J\|\boldsymbol{z}\|$, substituting into the right-hand side repeatedly gives $\|\boldsymbol{z}(t)\|\le K L^k\lvert t-t_0\rvert^k/k!\to0$, so $\boldsymbol{z}\equiv\boldsymbol{0}$.

Finally, $J$ is an arbitrary bounded closed subinterval of $I$ containing $t_0$; by uniqueness, the solutions on different intervals $J$ agree on their common part, and together they form the unique solution on $I$. $\square$

The proof also yields an estimate for the solution (which can also be obtained from Grönwall's inequality, [2.4.7](/2.4.7)):

$$
\|\boldsymbol{x}(t)\|\le\Big(\|\boldsymbol{\eta}\|+\Big\lvert\int_{t_0}^t\|\boldsymbol{f}(s)\|\,\mathrm{d}s\Big\rvert\Big)\mathrm{e}^{L\lvert t-t_0\rvert},\qquad t\in J.
$$

**Remark 8.1.1** Linearity is essential. The right-hand side of $x'=x^2$ is smooth on the whole plane, but the solution $x=\frac1{1-t}$ with $x(0)=1$ exists only for $t<1$. Solutions of linear systems, by contrast, exist everywhere in $I$; singularities can occur only at singular points of the coefficients (for example, the coefficients of $t^2y''-2ty'+2y=0$, written in normal form, are discontinuous at $t=0$).

The real and imaginary parts of a solution of a system with complex coefficients satisfy a system with real coefficients. Conversely, if $A$ and $\boldsymbol{f}$ are real-valued and $\boldsymbol{\eta}$ is a real vector, then by uniqueness the solution is real-valued (its complex conjugate is also a solution).

## 8.2. The Solution Space of a Homogeneous System

### 8.2.1. Dimension of the Solution Space

**Theorem 8.2.1 (Superposition Principle)** Let $\mathcal{L}\boldsymbol{x}=\boldsymbol{x}'-A(t)\boldsymbol{x}$; this is a linear map from $C^1(I)$ to $C(I)$ (spaces of vector-valued functions). Consequently:

1. linear combinations of solutions of the homogeneous system (8.2) are again solutions;
2. the difference of two solutions of the nonhomogeneous system (8.1) is a solution of the homogeneous system (8.2); if $\boldsymbol{x}^*$ is one solution of (8.1), then all solutions of (8.1) are $\boldsymbol{x}^*+\boldsymbol{x}$, where $\boldsymbol{x}$ ranges over the solutions of (8.2).

**Theorem 8.2.2** The solutions of the homogeneous system (8.2) form an $n$-dimensional vector space $S$. For any $t_0\in I$, the map

$$
\boldsymbol{x}\mapsto\boldsymbol{x}(t_0),\qquad S\to\mathbb{C}^n
$$
is a linear isomorphism (for real coefficients and real solutions only, it is a map $S\to\mathbb{R}^n$).

**Proof** By the superposition principle, $S$ is a vector space, and the map is clearly linear. It is surjective by the existence part of Theorem 8.1.1 and injective by the uniqueness part. $\square$

This isomorphism turns questions about solutions into linear algebra questions about initial vectors. In particular:

- $m$ solutions $\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_m$ are linearly independent if and only if their values $\boldsymbol{\varphi}_1(t_0),\dots,\boldsymbol{\varphi}_m(t_0)$ at some point (and hence at every point) are linearly independent;
- a solution that vanishes at one point vanishes identically.

### 8.2.2. Fundamental Matrices and Liouville's Formula

**Definition 8.2.1 (Fundamental Matrix)** A set of $n$ linearly independent solutions $\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_n$ of the homogeneous system (8.2) is called a **fundamental set of solutions**; the matrix $\Phi(t)=(\boldsymbol{\varphi}_1(t),\dots,\boldsymbol{\varphi}_n(t))$ with these solutions as columns is called a **fundamental matrix**, and a fundamental matrix with $\Phi(t_0)=I$ is called the **principal fundamental matrix** (at $t_0$). The **Wronskian** of the $n$ solutions is $W(t)=\det\Phi(t)$.

A matrix $Y(t)$ whose columns are $n$ solutions satisfies the matrix equation $Y'=A(t)Y$ (look at it column by column) and is called a solution matrix; conversely, every column of a solution of the matrix equation is a solution of (8.2).

**Theorem 8.2.3** Let $Y(t)$ be a solution matrix of (8.2). The following conditions are equivalent:

1. the columns of $Y$ are linearly independent, i.e. $Y$ is a fundamental matrix;
2. $\det Y(t)\ne0$ for all $t\in I$;
3. $\det Y(t_0)\ne0$ for some $t_0\in I$.

Hence the Wronskian of a solution matrix either vanishes identically or vanishes nowhere.

**Proof** By Theorem 8.2.2, the columns are linearly independent if and only if their values at any one point are linearly independent, i.e. $\det Y(t)\ne0$; and if this holds at one point, it holds at every point. $\square$

This conclusion fails for arbitrary vector-valued functions: $(t,1)^{\mathsf T}$ and $(t^2,t)^{\mathsf T}$ are linearly independent on $\mathbb{R}$, but $\det\begin{bmatrix}t&t^2\\1&t\end{bmatrix}\equiv0$. They cannot both be solutions of the same homogeneous system with continuous coefficients.

The Wronskian satisfies a first-order linear equation and therefore has an explicit expression.

**Theorem 8.2.4 (Liouville's Formula)** Let $Y(t)$ be a solution matrix of (8.2) and $t_0\in I$. Then

$$
\det Y(t)=\det Y(t_0)\exp\Big(\int_{t_0}^t\operatorname{tr}(A(s))\,\mathrm{d}s\Big).\tag{8.3}
$$

**Proof** The determinant is linear in each row, so by the product rule $\frac{\mathrm{d}}{\mathrm{d}t}\det Y$ is the sum of the $n$ determinants obtained from $\det Y$ by replacing the $i$th row with its derivative. Since $Y'=AY$, the $i$th row of $Y'$ is $\sum_ja_{ij}\cdot(\text{row }j\text{ of }Y)$; subtracting multiples of the other rows in the $i$th determinant leaves only $a_{ii}\cdot(\text{row }i)$, so that determinant equals $a_{ii}\det Y$. Therefore

$$
(\det Y)'=\big(a_{11}+\cdots+a_{nn}\big)\det Y=\operatorname{tr}(A(t))\det Y,
$$
and solving this first-order linear equation gives (8.3). $\square$

Liouville's formula gives a second proof that $\det Y$ either vanishes identically or vanishes nowhere. Geometrically, $\lvert\det Y(t)\rvert$ is the volume at time $t$ of the image, under the flow of solutions, of a set of initial values of unit volume, and $\operatorname{tr}(A)$ is the instantaneous rate of expansion of volume (the divergence of the vector field $A\boldsymbol{x}$).

**Theorem 8.2.5** Let $\Phi(t)$ be a fundamental matrix of (8.2).

1. For any invertible constant matrix $C$, $\Phi(t)C$ is also a fundamental matrix; conversely, every fundamental matrix $\Psi(t)$ can be written as $\Psi=\Phi C$, where $C=\Phi^{-1}(t_0)\Psi(t_0)$ is an invertible constant matrix.
2. The general solution of (8.2) is $\boldsymbol{x}=\Phi(t)\boldsymbol{c}$ with $\boldsymbol{c}$ an arbitrary constant vector; the solution satisfying $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ is $\boldsymbol{x}(t)=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{\eta}$.

**Proof** 1: $(\Phi C)'=A\Phi C$ and $\det(\Phi C)=\det\Phi\det C\ne0$. Conversely, differentiating $\Phi\Phi^{-1}=I$ gives $(\Phi^{-1})'=-\Phi^{-1}\Phi'\Phi^{-1}=-\Phi^{-1}A$, hence

$$
(\Phi^{-1}\Psi)'=-\Phi^{-1}A\Psi+\Phi^{-1}A\Psi=O,
$$
and $\Phi^{-1}\Psi$ is a constant matrix. 2: $\Phi\boldsymbol{c}$ is a solution; any solution $\boldsymbol{x}$ and $\Phi(t)\Phi^{-1}(t_0)\boldsymbol{x}(t_0)$ have the same value at $t_0$, so they are equal by uniqueness. $\square$

The function of two variables $R(t,s)=\Phi(t)\Phi^{-1}(s)$ does not depend on the choice of fundamental matrix (since $\Phi C(\Phi C)^{-1}=\Phi\Phi^{-1}$). It is the principal fundamental matrix at $s$; it maps the state at time $s$ to the state at time $t$, and in control theory it is called the state transition matrix. By definition,

$$
R(t,t)=I,\qquad R(t,s)R(s,r)=R(t,r),\qquad R(t,s)^{-1}=R(s,t).
$$

**Example 8.2.1** The system

$$
\boldsymbol{x}'=\begin{bmatrix}0&1\\-\dfrac{2}{t^2}&\dfrac{2}{t}\end{bmatrix}\boldsymbol{x},\qquad t>0
$$
comes from the Cauchy–Euler equation $t^2y''-2ty'+2y=0$ (with $\boldsymbol{x}=(y,y')^{\mathsf T}$), which has the solutions $t$ and $t^2$. Hence

$$
\Phi(t)=\begin{bmatrix}t&t^2\\1&2t\end{bmatrix},\qquad\det\Phi(t)=t^2,
$$
in agreement with Liouville's formula: $\operatorname{tr}(A)=\frac2t$ and $\det\Phi(1)\exp\big(\int_1^t\frac2s\,\mathrm{d}s\big)=t^2$. The principal fundamental matrix at $t_0=1$ is $\Phi(t)\Phi^{-1}(1)=\begin{bmatrix}2t-t^2&t^2-t\\2-2t&2t-1\end{bmatrix}$.

For systems with variable coefficients there is in general no method for finding a fundamental matrix. A tempting but often wrong "formula" is $\exp\big(\int_{t_0}^tA(s)\,\mathrm{d}s\big)$: it is a fundamental matrix only when $A(t)$ commutes with $\int_{t_0}^tA(s)\,\mathrm{d}s$ (for example, when $A(t)=a(t)B$ with $B$ a constant matrix). In the example above, $A(1)$ does not commute with $\int_1^2A(s)\,\mathrm{d}s$.

## 8.3. Nonhomogeneous Systems and the Variation of Constants Formula

**Theorem 8.3.1 (Variation of Constants Formula)** Let $\Phi(t)$ be a fundamental matrix of (8.2). Then the solution of the nonhomogeneous system (8.1) satisfying $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ is

$$
\boldsymbol{x}(t)=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{\eta}+\int_{t_0}^t\Phi(t)\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s,\tag{8.4}
$$
and the general solution of (8.1) is $\boldsymbol{x}(t)=\Phi(t)\boldsymbol{c}+\Phi(t)\int_{t_0}^t\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s$ with $\boldsymbol{c}$ an arbitrary constant vector.

**Proof** Derivation: as for first-order linear equations, replace the constant vector in the general homogeneous solution $\Phi(t)\boldsymbol{c}$ by a function $\boldsymbol{c}(t)$. Substituting into (8.1) gives $\Phi'\boldsymbol{c}+\Phi\boldsymbol{c}'=A\Phi\boldsymbol{c}+\boldsymbol{f}$, and since $\Phi'=A\Phi$, we get $\Phi\boldsymbol{c}'=\boldsymbol{f}$. As $\Phi(s)$ is invertible everywhere, $\boldsymbol{c}'(s)=\Phi^{-1}(s)\boldsymbol{f}(s)$; integrating and using $\boldsymbol{c}(t_0)=\Phi^{-1}(t_0)\boldsymbol{\eta}$ gives (8.4).

Verification: write the right-hand side of (8.4) as $\boldsymbol{x}(t)=\Phi(t)\boldsymbol{c}(t)$ with $\boldsymbol{c}(t)=\Phi^{-1}(t_0)\boldsymbol{\eta}+\int_{t_0}^t\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s$. Then $\boldsymbol{x}'=A\Phi\boldsymbol{c}+\Phi\Phi^{-1}(t)\boldsymbol{f}(t)=A\boldsymbol{x}+\boldsymbol{f}$ and $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$. By the uniqueness in Theorem 8.1.1, this is the required solution. The form of the general solution follows from Theorem 8.2.1. $\square$

The general solution is sometimes misquoted as $\Phi(t)\big(\boldsymbol{c}+\Phi(t)\int_{t_0}^t\Phi^{-1}\boldsymbol{f}\big)$, with a superfluous factor $\Phi(t)$ inside the parentheses; the correct formula is (8.4).

Formula (8.4) has a clear meaning: the solution is the evolution of the initial value under the homogeneous system, plus the sum over all times $s$ of the input $\boldsymbol{f}(s)\,\mathrm{d}s$ evolved from time $s$ to time $t$. The matrix $R(t,s)=\Phi(t)\Phi^{-1}(s)$ is the response of the system to a unit "impulse" applied at time $s$; in physics this superposition principle is known as Duhamel's principle. Formula (8.4) also shows that the solution of a nonhomogeneous system is linear in both inputs $\boldsymbol{\eta}$ and $\boldsymbol{f}$.

**Example 8.3.1** The second-order equation $y''+\omega^2y=g(t)$ ($\omega>0$) becomes, with $\boldsymbol{x}=(y,y')^{\mathsf T}$, the system

$$
\boldsymbol{x}'=\begin{bmatrix}0&1\\-\omega^2&0\end{bmatrix}\boldsymbol{x}+\begin{bmatrix}0\\g(t)\end{bmatrix},\qquad\Phi(t)=\begin{bmatrix}\cos\omega t&\sin\omega t\\-\omega\sin\omega t&\omega\cos\omega t\end{bmatrix}.
$$
Here $\det\Phi=\omega$, and the upper right entry of $\Phi(t)\Phi^{-1}(s)$ is $\frac{1}{\omega}\sin\omega(t-s)$. Taking the first component of (8.4), the solution with $y(0)=y'(0)=0$ is

$$
y(t)=\frac1\omega\int_0^t\sin\omega(t-s)\,g(s)\,\mathrm{d}s.
$$
The next chapter extends this way of writing solutions with a "kernel" to general $n$th-order linear equations (Definition 9.2.1). For a concrete numerical example, see [Example 16.6.2 of 2.2.16](/2.2.16#ex-16.6.2).

## 8.4. The Matrix Exponential

### 8.4.1. Definition and Convergence

For $n=1$ the solution of $x'=ax$ is $\mathrm{e}^{at}x_0$. For a system with constant coefficients $\boldsymbol{x}'=A\boldsymbol{x}$ it is natural to guess that the solution is $\mathrm{e}^{tA}\boldsymbol{x}_0$, and for this we need to define the exponential of a matrix.

**Definition 8.4.1 (Matrix Exponential)** For $A\in\mathbb{C}^{n\times n}$, define

$$
\mathrm{e}^{A}=\exp A=\sum_{k=0}^\infty\frac{A^k}{k!}=I+A+\frac{A^2}{2!}+\cdots+\frac{A^k}{k!}+\cdots.
$$

**Theorem 8.4.1** For every $A$, the series $\sum_k\frac{t^kA^k}{k!}$ converges uniformly and absolutely on every bounded interval $\lvert t\rvert\le T$; its sum $\mathrm{e}^{tA}$ is differentiable in $t$, and

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathrm{e}^{tA}=A\mathrm{e}^{tA}=\mathrm{e}^{tA}A.
$$

**Proof** We have $\big\|\frac{t^kA^k}{k!}\big\|\le\frac{(T\|A\|)^k}{k!}$, and $\sum_k\frac{(T\|A\|)^k}{k!}=\mathrm{e}^{T\|A\|}$ converges. By the Weierstrass M-test (which also applies entrywise, since the modulus of each entry is at most a constant times the matrix norm), the series converges uniformly and absolutely on $\lvert t\rvert\le T$. The termwise differentiated series $\sum_{k\ge1}\frac{t^{k-1}A^k}{(k-1)!}=A\sum_{j\ge0}\frac{t^jA^j}{j!}$ also converges uniformly, so termwise differentiation is permitted and the derivative is $A\mathrm{e}^{tA}$; factoring $A$ out on the right is similar. $\square$

In [2.1.11](/2.1.11#sec-11.8) the matrix exponential is a special case of a matrix function, defined via the spectrum or computed by interpolation; the series definition given here agrees with it.

### 8.4.2. Properties

**Theorem 8.4.2** Let $A,B\in\mathbb{C}^{n\times n}$, $P$ invertible, and $s,t\in\mathbb{R}$.

1. If $AB=BA$, then $\mathrm{e}^{A+B}=\mathrm{e}^A\mathrm{e}^B$;
2. $\mathrm{e}^{(s+t)A}=\mathrm{e}^{sA}\mathrm{e}^{tA}$; $\mathrm{e}^{A}$ is invertible and $(\mathrm{e}^A)^{-1}=\mathrm{e}^{-A}$;
3. $\mathrm{e}^{PAP^{-1}}=P\mathrm{e}^AP^{-1}$;
4. $\det\mathrm{e}^{tA}=\mathrm{e}^{t\operatorname{tr}(A)}$.

**Proof** We use uniqueness for differential equations, which avoids rearranging series.

1: $B$ commutes with every power of $A$, hence with $\mathrm{e}^{tA}$. Let $Z(t)=\mathrm{e}^{tA}\mathrm{e}^{tB}$. Then

$$
Z'=A\mathrm{e}^{tA}\mathrm{e}^{tB}+\mathrm{e}^{tA}B\mathrm{e}^{tB}=(A+B)Z,\qquad Z(0)=I.
$$
The function $\mathrm{e}^{t(A+B)}$ satisfies the same matrix initial value problem (column by column, it is the initial value problem for $\boldsymbol{x}'=(A+B)\boldsymbol{x}$), so by uniqueness $Z(t)=\mathrm{e}^{t(A+B)}$; now take $t=1$.

2: $sA$ and $tA$ commute, so the first identity follows from 1; taking $s=-t$ gives $\mathrm{e}^{tA}\mathrm{e}^{-tA}=\mathrm{e}^{O}=I$.

3: $(PAP^{-1})^k=PA^kP^{-1}$, so the series agree term by term.

4: $\mathrm{e}^{tA}$ is a solution matrix of $\boldsymbol{x}'=A\boldsymbol{x}$ (Theorem 8.4.1), so by Liouville's formula $\det\mathrm{e}^{tA}=\det I\cdot\mathrm{e}^{\int_0^t\operatorname{tr}(A)\,\mathrm{d}s}$. $\square$

The commutativity condition cannot be dropped; a counterexample follows [Theorem 11.8.1 of 2.1.11](/2.1.11#thm-11.8.1). Property 2 says that $t\mapsto\mathrm{e}^{tA}$ is a homomorphism from the additive group $(\mathbb{R},+)$ to the multiplicative group of invertible matrices; $\{\mathrm{e}^{tA}\}_{t\in\mathbb{R}}$ is called a one-parameter subgroup.

### 8.4.3. Solutions of Systems with Constant Coefficients

**Theorem 8.4.3** $\mathrm{e}^{tA}$ is the principal fundamental matrix at $t=0$ of the system with constant coefficients $\boldsymbol{x}'=A\boldsymbol{x}$. Consequently:

1. the solution satisfying $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ is $\boldsymbol{x}(t)=\mathrm{e}^{(t-t_0)A}\boldsymbol{\eta}$;
2. every fundamental matrix $\Phi$ satisfies $\Phi(t)\Phi^{-1}(s)=\mathrm{e}^{(t-s)A}$, and in particular $\mathrm{e}^{tA}=\Phi(t)\Phi^{-1}(0)$;
3. the solution of $\boldsymbol{x}'=A\boldsymbol{x}+\boldsymbol{f}(t)$ satisfying $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ is

$$
\boldsymbol{x}(t)=\mathrm{e}^{(t-t_0)A}\boldsymbol{\eta}+\int_{t_0}^t\mathrm{e}^{(t-s)A}\boldsymbol{f}(s)\,\mathrm{d}s.\tag{8.5}
$$

**Proof** By Theorem 8.4.1, $(\mathrm{e}^{tA})'=A\mathrm{e}^{tA}$, and $\mathrm{e}^{0A}=I$. The matrix $\mathrm{e}^{tA}\mathrm{e}^{-sA}=\mathrm{e}^{(t-s)A}$ is the principal fundamental matrix at $s$, and $\Phi(t)\Phi^{-1}(s)$ does not depend on the choice of fundamental matrix, so the two are equal. Statements 1 and 3 follow from Theorems 8.2.5 and 8.3.1. $\square$

That $R(t,s)$ depends only on $t-s$ reflects the time-translation invariance of systems with constant coefficients: if $\boldsymbol{x}(t)$ is a solution, so is $\boldsymbol{x}(t+c)$. Formula (8.5) is [Eq. (11.3) of 2.1.11](/2.1.11#eq-11.3).

Statement 2 gives one way to compute $\mathrm{e}^{tA}$: first find any fundamental matrix $\Phi$ (by eigenvectors or otherwise), then compute $\Phi(t)\Phi^{-1}(0)$.

## 8.5. Computing $\mathrm{e}^{tA}$ via the Jordan Canonical Form

### 8.5.1. The Exponential of a Jordan Block

By the **Jordan canonical form**, there is an invertible matrix $P$ with $P^{-1}AP=J=\operatorname{diag}(J_1,\dots,J_s)$, where $J_i=J_{\lambda_i,m_i}$ is an $m_i\times m_i$ **Jordan block** ([2.1.10](/2.1.10)). By property 3 of Theorem 8.4.2,

$$
\mathrm{e}^{tA}=P\mathrm{e}^{tJ}P^{-1},\qquad\mathrm{e}^{tJ}=\operatorname{diag}\big(\mathrm{e}^{tJ_1},\dots,\mathrm{e}^{tJ_s}\big)
$$
(powers of a block diagonal matrix are computed block by block).

**Theorem 8.5.1** Let $J_{\lambda,m}=\lambda I+N$, where $N$ is the $m\times m$ matrix with ones on the superdiagonal and zeros elsewhere. Then

$$
\mathrm{e}^{tJ_{\lambda,m}}=\mathrm{e}^{\lambda t}\sum_{k=0}^{m-1}\frac{t^k}{k!}N^k=\mathrm{e}^{\lambda t}\begin{bmatrix}1&t&\dfrac{t^2}{2!}&\cdots&\dfrac{t^{m-1}}{(m-1)!}\\&1&t&\cdots&\dfrac{t^{m-2}}{(m-2)!}\\&&\ddots&\ddots&\vdots\\&&&1&t\\&&&&1\end{bmatrix}.
$$

**Proof** $\lambda I$ commutes with $N$, so by property 1 of Theorem 8.4.2, $\mathrm{e}^{tJ}=\mathrm{e}^{\lambda t}\mathrm{e}^{tN}$. The matrix $N^k$ has ones on the $k$th superdiagonal, and $N^m=O$, so the series for $\mathrm{e}^{tN}$ has only its first $m$ terms. $\square$

The matrix $P\mathrm{e}^{tJ}$ is also a fundamental matrix (Theorem 8.2.5), and its columns can be written down directly: the columns $\boldsymbol{p}_1,\dots,\boldsymbol{p}_m$ of $P$ corresponding to $J_{\lambda,m}$ form a **Jordan chain** ($(A-\lambda I)\boldsymbol{p}_1=\boldsymbol{0}$, $(A-\lambda I)\boldsymbol{p}_{k+1}=\boldsymbol{p}_k$), which gives the $m$ solutions

$$
\mathrm{e}^{\lambda t}\boldsymbol{p}_1,\quad\mathrm{e}^{\lambda t}(t\boldsymbol{p}_1+\boldsymbol{p}_2),\quad\dots,\quad\mathrm{e}^{\lambda t}\sum_{j=1}^m\frac{t^{m-j}}{(m-j)!}\boldsymbol{p}_j.
$$
This is [Corollary 11.9.1 of 2.1.11](/2.1.11#cor-11.9.1). When $A$ is a **diagonalizable matrix**, all blocks are $1\times1$, and a fundamental set of solutions is $\mathrm{e}^{\lambda_kt}\boldsymbol{r}_k$ (the eigenvector method, [Theorem 16.6.5 of 2.2.16](/2.2.16#thm-16.6.5)); for a complex eigenvalue of a real matrix, the real and imaginary parts of $\mathrm{e}^{\lambda t}\boldsymbol{r}$ give real solutions.

### 8.5.2. Structure of Solutions and Growth Estimates

The following corollary is the foundation of the theory of equations with constant coefficients in the next chapter and of the stability theory in Chapter 11.

**Corollary 8.5.1** Let $\lambda_1,\dots,\lambda_r$ be the distinct eigenvalues of $A$, and let $m_j$ be the size of the largest Jordan block for $\lambda_j$ (that is, the multiplicity of $\lambda_j$ as a root of the minimal polynomial).

1. Every entry of $\mathrm{e}^{tA}$ (and hence every component of every solution of $\boldsymbol{x}'=A\boldsymbol{x}$) has the form $\sum_{j=1}^rp_j(t)\mathrm{e}^{\lambda_jt}$, where $p_j$ is a polynomial of degree less than $m_j$;
2. let $\mu=\max_j\operatorname{Re}\lambda_j$. For every $\varepsilon>0$ there is a constant $C$ such that

$$
\|\mathrm{e}^{tA}\|\le C\mathrm{e}^{(\mu+\varepsilon)t},\qquad t\ge0;
$$
if all eigenvalues with real part $\mu$ are **semisimple eigenvalues** (all of their Jordan blocks are $1\times1$), one may take $\varepsilon=0$.

**Proof** 1: $\mathrm{e}^{tA}=P\mathrm{e}^{tJ}P^{-1}$, and by Theorem 8.5.1 the entries of $\mathrm{e}^{tJ}$ are $\frac{t^k}{k!}\mathrm{e}^{\lambda_jt}$ ($k<m_j$) or $0$; multiplying by constant matrices on the left and right produces linear combinations of them. 2: $\lvert t^k\mathrm{e}^{\lambda_jt}\rvert=t^k\mathrm{e}^{t\operatorname{Re}\lambda_j}\le C_\varepsilon\mathrm{e}^{(\mu+\varepsilon)t}$, because $t^k\mathrm{e}^{-\varepsilon t}$ is bounded for $t\ge0$; if the eigenvalues with real part $\mu$ have only $1\times1$ blocks, the corresponding terms have $k=0$ and no $\varepsilon$ is needed. Boundedness of the entries implies boundedness of the norm. $\square$

The eigenvalues determine the exponential growth rate as $t\to+\infty$, but not everything: Jordan blocks contribute polynomial factors $t^k$, and a nonnormal matrix ([2.1.12](/2.1.12)) may make $\|\mathrm{e}^{tA}\|$ undergo considerable transient growth before it decays (right panel of the figure).

![Left: the three entries e^{-t/2}, t e^{-t/2}, (t^2/2) e^{-t/2} of the first row of e^{tA} for the Jordan block A = J_{-0.5,3}; the polynomial factors make the last two first grow and then decay. Right: ‖e^{tA}‖ (spectral norm) for A = [[-1, a], [0, -2]]; both eigenvalues are negative, the transient growth becomes more pronounced as a increases, and for the normal matrix a = 0 the norm decays monotonically](./plots/matrix-exponential-growth.py)

### 8.5.3. The Method of Generalized Eigenspaces

Finding $P$ and $P^{-1}$ is often laborious. When only the solution $\mathrm{e}^{tA}\boldsymbol{\eta}$ is needed, a decomposition into **generalized eigenspaces** can replace the Jordan basis.

**Theorem 8.5.2** Let $\lambda_1,\dots,\lambda_r$ be the distinct eigenvalues of $A$ with algebraic multiplicities $n_1,\dots,n_r$, and let $V_j=\mathcal{N}\big((A-\lambda_jI)^{n_j}\big)$ be the generalized eigenspaces. Decompose the initial value as $\boldsymbol{\eta}=\boldsymbol{\eta}_1+\cdots+\boldsymbol{\eta}_r$ with $\boldsymbol{\eta}_j\in V_j$. Then

$$
\mathrm{e}^{tA}\boldsymbol{\eta}=\sum_{j=1}^r\mathrm{e}^{\lambda_jt}\sum_{k=0}^{n_j-1}\frac{t^k}{k!}(A-\lambda_jI)^k\boldsymbol{\eta}_j.\tag{8.6}
$$

**Proof** Since $\mathbb{C}^n=V_1\oplus\cdots\oplus V_r$ ([2.1.10](/2.1.10)), the decomposition exists and is unique. As $\lambda_jI$ commutes with $A-\lambda_jI$,

$$
\mathrm{e}^{tA}\boldsymbol{\eta}_j=\mathrm{e}^{\lambda_jt}\mathrm{e}^{t(A-\lambda_jI)}\boldsymbol{\eta}_j=\mathrm{e}^{\lambda_jt}\sum_{k=0}^\infty\frac{t^k}{k!}(A-\lambda_jI)^k\boldsymbol{\eta}_j,
$$
and $(A-\lambda_jI)^k\boldsymbol{\eta}_j=\boldsymbol{0}$ for $k\ge n_j$, so the series is a finite sum. Summing over $j$ gives the result. $\square$

Taking $\boldsymbol{\eta}$ to be the standard basis vectors $\boldsymbol{e}_1,\dots,\boldsymbol{e}_n$ gives the columns of $\mathrm{e}^{tA}$. This method requires only solving linear systems to find bases of the $V_j$ and decomposing vectors; no Jordan chains are needed.

**Example 8.5.1** Let $A=\begin{bmatrix}3&-1\\1&1\end{bmatrix}$. The characteristic polynomial is $(\lambda-2)^2$, so there is only one eigenvalue, $V_1=\mathbb{C}^2$, and $(A-2I)^2=O$ (Cayley–Hamilton). By (8.6),

$$
\mathrm{e}^{tA}=\mathrm{e}^{2t}\big(I+t(A-2I)\big)=\mathrm{e}^{2t}\begin{bmatrix}1+t&-t\\t&1-t\end{bmatrix}.
$$
This agrees with the general solution obtained by elimination in [Example 16.6.5 of 2.2.16](/2.2.16#ex-16.6.5).

**Example 8.5.2** Find $\mathrm{e}^{tA}$ for $A=\begin{bmatrix}2&1&1\\0&2&1\\0&0&3\end{bmatrix}$. The eigenvalues are $2$ (double) and $3$ (simple). With $N=A-2I=\begin{bmatrix}0&1&1\\0&0&1\\0&0&1\end{bmatrix}$ we have $N^2=\begin{bmatrix}0&0&2\\0&0&1\\0&0&1\end{bmatrix}$, $V_1=\mathcal{N}(N^2)=\operatorname{span}\{\boldsymbol{e}_1,\boldsymbol{e}_2\}$, and $V_2=\mathcal{N}(A-3I)=\operatorname{span}\{(2,1,1)^{\mathsf T}\}$.

- $\boldsymbol{e}_1,\boldsymbol{e}_2\in V_1$: $\mathrm{e}^{tA}\boldsymbol{e}_1=\mathrm{e}^{2t}(\boldsymbol{e}_1+tN\boldsymbol{e}_1)=\mathrm{e}^{2t}\boldsymbol{e}_1$ and $\mathrm{e}^{tA}\boldsymbol{e}_2=\mathrm{e}^{2t}(\boldsymbol{e}_2+t\boldsymbol{e}_1)$;
- $\boldsymbol{e}_3=(2,1,1)^{\mathsf T}+(-2,-1,0)^{\mathsf T}$, where the second vector lies in $V_1$ and $N(-2,-1,0)^{\mathsf T}=(-1,0,0)^{\mathsf T}$. Hence $\mathrm{e}^{tA}\boldsymbol{e}_3=\mathrm{e}^{3t}(2,1,1)^{\mathsf T}+\mathrm{e}^{2t}(-2-t,-1,0)^{\mathsf T}$.

Altogether,

$$
\mathrm{e}^{tA}=\begin{bmatrix}\mathrm{e}^{2t}&t\mathrm{e}^{2t}&2\mathrm{e}^{3t}-(2+t)\mathrm{e}^{2t}\\0&\mathrm{e}^{2t}&\mathrm{e}^{3t}-\mathrm{e}^{2t}\\0&0&\mathrm{e}^{3t}\end{bmatrix}.
$$
One can check that $\det\mathrm{e}^{tA}=\mathrm{e}^{7t}=\mathrm{e}^{t\operatorname{tr}(A)}$.

Computing $\mathrm{e}^{tA}$ by interpolation ([Section 11.6 of 2.1.11](/2.1.11#sec-11.6)) is a third approach: $\mathrm{e}^{tA}=r(A)$, where $r$ is the polynomial that agrees with $\mathrm{e}^{tz}$, together with sufficiently many derivatives, on the spectrum of $A$. All three methods give the same matrix.

## Summary

| Topic | Result |
|---|---|
| Existence and uniqueness | Coefficients continuous on $I$ $\Rightarrow$ the solution of the initial value problem exists and is unique on all of $I$ (Theorem 8.1.1) |
| Solution space | Homogeneous solutions form an $n$-dimensional space; $\boldsymbol{x}\mapsto\boldsymbol{x}(t_0)$ is an isomorphism (Theorem 8.2.2) |
| Fundamental matrix | $\Phi'=A\Phi$ and $\det\Phi\ne0$; two fundamental matrices differ by an invertible constant matrix factor; $\det\Phi$ satisfies Liouville's formula (8.3) |
| Nonhomogeneous systems | $\boldsymbol{x}=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{\eta}+\int_{t_0}^t\Phi(t)\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s$ (Eq. (8.4)) |
| Matrix exponential | The series converges uniformly and absolutely on bounded intervals; $\mathrm{e}^{A+B}=\mathrm{e}^A\mathrm{e}^B$ for commuting $A,B$; $\det\mathrm{e}^{tA}=\mathrm{e}^{t\operatorname{tr}(A)}$ |
| Constant coefficients | $\mathrm{e}^{tA}$ is the principal fundamental matrix; $\mathrm{e}^{tA}=P\mathrm{e}^{tJ}P^{-1}$, and Jordan blocks give $t^k\mathrm{e}^{\lambda t}$ |
| Growth estimate | $\Vert\mathrm{e}^{tA}\Vert\le C\mathrm{e}^{(\mu+\varepsilon)t}$, $\mu=\max\operatorname{Re}\lambda$ (Corollary 8.5.1) |
| Methods of computation | Jordan basis; generalized eigenspace decomposition (8.6); interpolation; find any $\Phi$, then compute $\Phi(t)\Phi^{-1}(0)$ |
