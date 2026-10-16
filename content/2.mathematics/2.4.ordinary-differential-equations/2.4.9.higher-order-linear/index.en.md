---
title: Higher-Order Linear Differential Equations
source_hash: 2a681439ae54
---

The $n$th-order linear equation $y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_n(x)y=f(x)$ is the most common type of equation in physics and engineering: vibrations, electric circuits, the bending of beams and the stationary equations of quantum mechanics all belong to it. With $\boldsymbol{x}=(y,y',\dots,y^{(n-1)})^{\mathsf T}$ it becomes a first-order **system of linear differential equations** whose coefficient matrix is a **companion matrix**. Hence the whole theory of the previous chapter applies directly: global existence and uniqueness, the solution space, the Wronskian and Liouville's formula, and the variation of constants formula. This chapter translates these results into the language of $n$th-order equations, with emphasis on two formulas that are very useful in applications: the variation of constants formula written in terms of cofactors, and the Cauchy function $K(x,t)$ derived from it, which expresses a particular solution of the nonhomogeneous equation as $\int K(x,t)f(t)\,\mathrm{d}t$.

When some solutions of the homogeneous equation are known, the order can be reduced. Equations with constant coefficients and Cauchy–Euler equations can be solved completely; the concrete methods were discussed in detail in calculus ([2.2.16](/2.2.16)), and here we add only theoretical explanations. Finally we discuss periodic solutions of $y''+M^2y=f$, which give a precise formulation of the phenomenon of "resonance". The qualitative theory of zeros of second-order equations and boundary value problems are treated in [2.4.12](/2.4.12), and series solutions of equations with variable coefficients in the next chapter.

## 9.1. A Special Case of Linear Systems

### 9.1.1. Reduction to a System; Existence and Uniqueness

Throughout this chapter, $p_1(x),\dots,p_n(x),f(x)$ are assumed continuous on an interval $I$. Write

$$
L(y)=y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_{n-1}(x)y'+p_n(x)y,
$$
and consider the nonhomogeneous and homogeneous equations

$$
L(y)=f(x),\tag{9.1}
$$

$$
L(y)=0.\tag{9.2}
$$
A function $y$ is a solution of (9.1) if and only if $\boldsymbol{x}=(y,y',\dots,y^{(n-1)})^{\mathsf T}$ is a solution of the system

$$
\boldsymbol{x}'=C(x)\boldsymbol{x}+f(x)\boldsymbol{e}_n,\qquad C(x)=\begin{bmatrix}0&1&&\\&\ddots&\ddots&\\&&0&1\\-p_n&-p_{n-1}&\cdots&-p_1\end{bmatrix},\tag{9.3}
$$
where $\boldsymbol{e}_n=(0,\dots,0,1)^{\mathsf T}$. Theorem 8.1.1 therefore gives:

**Theorem 9.1.1** For any $x_0\in I$ and $\eta_0,\dots,\eta_{n-1}\in\mathbb{C}$, the solution of Eq. (9.1) satisfying $y^{(k)}(x_0)=\eta_k$ ($k=0,\dots,n-1$) exists and is unique on the whole of $I$.

### 9.1.2. Fundamental Sets of Solutions and the Wronskian

The functions $y_1,\dots,y_n$ are solutions of (9.2) if and only if the vectors $(y_k,y_k',\dots,y_k^{(n-1)})^{\mathsf T}$ are solutions of the homogeneous system associated with (9.3). Linear dependence of the scalar functions is the same as linear dependence of the corresponding vector-valued functions (a linear relation among the first components, once differentiated, holds for the remaining components as well). The determinant of the corresponding solution matrix is the **Wronskian** of the functions,

$$
W(x)=W[y_1,\dots,y_n](x)=\begin{vmatrix}y_1&y_2&\cdots&y_n\\y_1'&y_2'&\cdots&y_n'\\\vdots&\vdots&&\vdots\\y_1^{(n-1)}&y_2^{(n-1)}&\cdots&y_n^{(n-1)}\end{vmatrix}.
$$
The trace of the companion matrix is $-p_1$, so Theorems 8.2.2–8.2.4 give:

**Theorem 9.1.2** 

1. The solutions of the homogeneous equation (9.2) form an $n$-dimensional vector space, and $y\mapsto(y(x_0),\dots,y^{(n-1)}(x_0))$ is an isomorphism of it onto $\mathbb{C}^n$;
2. $n$ solutions $y_1,\dots,y_n$ of (9.2) are linearly independent (form a **fundamental set of solutions**) $\Leftrightarrow$ $W\ne0$ at some point $\Leftrightarrow$ $W\ne0$ at every point;
3. (**Liouville's formula**) $W(x)=W(x_0)\exp\Big(-\displaystyle\int_{x_0}^xp_1(t)\,\mathrm{d}t\Big)$;
4. if $y_1,\dots,y_n$ is a fundamental set of solutions and $y^*$ is one solution of (9.1), then all solutions of (9.1) are $y=y^*+C_1y_1+\cdots+C_ny_n$.

For general functions, $W\equiv0$ does not imply linear dependence (see the example after [Proposition 16.1.1 of 2.2.16](/2.2.16#prop-16.1.1)); statement 2 shows that solutions behave differently. For second-order equations, Liouville's formula can also be verified directly: $W'=y_1y_2''-y_1''y_2=-p_1(y_1y_2'-y_1'y_2)$.

### 9.1.3. Determining the Equation from a Fundamental Set of Solutions

Conversely, a linearly independent set of functions determines a unique homogeneous linear equation.

**Proposition 9.1.1** Let $y_1,\dots,y_n\in C^n(I)$ with $W[y_1,\dots,y_n]$ nonzero everywhere on $I$. Then there is a unique $n$th-order linear equation with leading coefficient 1 having $y_1,\dots,y_n$ as a fundamental set of solutions, namely

$$
\frac{W[y_1,\dots,y_n,y](x)}{W[y_1,\dots,y_n](x)}=0,
$$
where $W[y_1,\dots,y_n,y]$ is the Wronskian of the $n+1$ functions. In particular, $p_1=-W'/W$.

**Proof** Expanding along the last column, $W[y_1,\dots,y_n,y]=W\cdot y^{(n)}+(\text{a linear combination of lower derivatives})$, so the left-hand side is an $n$th-order linear differential operator with leading coefficient 1 applied to $y$, with continuous coefficients. For $y=y_k$ the determinant has two equal columns and vanishes, so every $y_k$ is a solution. Uniqueness: if two such equations $L_1(y)=0$ and $L_2(y)=0$ have the same fundamental set of solutions, then $L_1-L_2$ is an operator of order at most $n-1$ with $n$ linearly independent solutions. If it were not the zero operator, let its order be $m<n$ and its leading coefficient be nonzero at some point $x_1$; near $x_1$ its solution space is only $m$-dimensional, a contradiction. The formula $p_1=-W'/W$ follows from Liouville's formula. $\square$

**Example 9.1.1** The equation with fundamental set of solutions $x$ and $\mathrm{e}^x$ (on an interval not containing $x=1$, where $W=(x-1)\mathrm{e}^x\ne0$) is

$$
\frac{1}{(x-1)\mathrm{e}^x}\begin{vmatrix}x&\mathrm{e}^x&y\\1&\mathrm{e}^x&y'\\0&\mathrm{e}^x&y''\end{vmatrix}=0,\qquad\text{i.e.}\qquad y''-\frac{x}{x-1}y'+\frac{1}{x-1}y=0,
$$
that is, $(x-1)y''-xy'+y=0$ ([Example 16.1.2 of 2.2.16](/2.2.16#ex-16.1.2)).

## 9.2. The Variation of Constants Formula and the Cauchy Function

### 9.2.1. The Variation of Constants Formula in Terms of Cofactors

Applying Theorem 8.3.1 to the system (9.3) and taking the first component gives a formula for a particular solution of the $n$th-order equation.

**Theorem 9.2.1** Let $y_1,\dots,y_n$ be a fundamental set of solutions of (9.2), $W(x)$ their Wronskian, and $W_k(x)$ the determinant obtained from $W(x)$ by replacing its $k$th column with $(0,\dots,0,1)^{\mathsf T}$ (that is, the cofactor of the entry in row $n$, column $k$ of $W$). Then

$$
y^*(x)=\int_{x_0}^x\sum_{k=1}^n\frac{y_k(x)W_k(t)}{W(t)}f(t)\,\mathrm{d}t\tag{9.4}
$$
is a solution of (9.1) satisfying $y^*(x_0)=(y^*)'(x_0)=\cdots=(y^*)^{(n-1)}(x_0)=0$. The general solution of (9.1) is $y=C_1y_1+\cdots+C_ny_n+y^*$.

**Proof** The matrix $\Phi(x)$ with columns $(y_k,\dots,y_k^{(n-1)})^{\mathsf T}$ is a fundamental matrix of the homogeneous system associated with (9.3), and $\det\Phi=W$. By Theorem 8.3.1, the solution of the system (9.3) with $\boldsymbol{x}(x_0)=\boldsymbol{0}$ is

$$
\boldsymbol{x}(x)=\int_{x_0}^x\Phi(x)\Phi^{-1}(t)\boldsymbol{e}_nf(t)\,\mathrm{d}t.
$$
By the formula $\Phi^{-1}=\frac{1}{W}\operatorname{adj}\Phi$ for the **adjugate matrix**, $\Phi^{-1}(t)\boldsymbol{e}_n$ is the $n$th column of $\operatorname{adj}\Phi(t)$ divided by $W(t)$; its $k$th component is the cofactor of the $(n,k)$ entry of $\Phi(t)$ divided by $W(t)$, that is, $W_k(t)/W(t)$. The first component of $\boldsymbol{x}(x)$ is the first row $(y_1(x),\dots,y_n(x))$ of $\Phi(x)$ times this vector, which gives (9.4). The condition $\boldsymbol{x}(x_0)=\boldsymbol{0}$ is exactly the stated initial condition on $y^*$ and its derivatives. $\square$

This is the general form of [Algorithm 16.2.1 of 2.2.16](/2.2.16#alg-16.2.1): the $C_k'$ obtained there by Cramer's rule are exactly $W_kf/W$. For $n=3$,

$$
W_1=\begin{vmatrix}0&y_2&y_3\\0&y_2'&y_3'\\1&y_2''&y_3''\end{vmatrix},\qquad W_2=\begin{vmatrix}y_1&0&y_3\\y_1'&0&y_3'\\y_1''&1&y_3''\end{vmatrix},\qquad W_3=\begin{vmatrix}y_1&y_2&0\\y_1'&y_2'&0\\y_1''&y_2''&1\end{vmatrix}.
$$

### 9.2.2. The Cauchy Function

**Definition 9.2.1 (Cauchy Function)** Let $y_1,\dots,y_n$ be a fundamental set of solutions of (9.2). The function

$$
K(x,t)=\sum_{k=1}^n\frac{y_k(x)W_k(t)}{W(t)}=\frac{1}{W(t)}\begin{vmatrix}y_1(t)&\cdots&y_n(t)\\\vdots&&\vdots\\y_1^{(n-2)}(t)&\cdots&y_n^{(n-2)}(t)\\y_1(x)&\cdots&y_n(x)\end{vmatrix}\qquad(x,t\in I)
$$
is called the **Cauchy function** of Eq. (9.2).

The second equality: replace the last row of $W(t)$ by $(y_1(x),\dots,y_n(x))$ and expand along the last row; the coefficients are exactly the $W_k(t)$.

**Theorem 9.2.2** 

1. For fixed $t\in I$, $K(x,t)$ as a function of $x$ is the solution of (9.2) satisfying the initial conditions

$$
K(t,t)=\partial_xK(t,t)=\cdots=\partial_x^{n-2}K(t,t)=0,\qquad\partial_x^{n-1}K(t,t)=1.
$$
Consequently, $K$ does not depend on the choice of fundamental set of solutions.

2. The solution of (9.1) satisfying $y(x_0)=\cdots=y^{(n-1)}(x_0)=0$ is

$$
y^*(x)=\int_{x_0}^xK(x,t)f(t)\,\mathrm{d}t.\tag{9.5}
$$

**Proof** 1: $K(x,t)$ is a linear combination of $y_1(x),\dots,y_n(x)$ with coefficients constant in $x$ (depending on $t$), so it is a solution. The value of $\partial_x^jK(x,t)$ at $x=t$ is obtained by replacing the last row of the determinant with $(y_1^{(j)}(t),\dots,y_n^{(j)}(t))$: for $j\le n-2$ this row coincides with an earlier row, giving $0$; for $j=n-1$ the determinant is $W(t)$, and the quotient is $1$. By uniqueness, only one solution satisfies these initial conditions. Statement 2 is (9.4). $\square$

Thus $K(x,t)$ is the response produced by "a unit impulse given to the $(n-1)$th derivative at time $t$", and (9.5) regards the nonhomogeneous term as a superposition of such impulses. It is the same object as $R(t,s)=\Phi(t)\Phi^{-1}(s)$ of the previous chapter: $K(x,t)$ is precisely the $(1,n)$ entry of $R(x,t)$.

For $n=2$,

$$
K(x,t)=\frac{1}{W(t)}\begin{vmatrix}y_1(t)&y_2(t)\\y_1(x)&y_2(x)\end{vmatrix}=\frac{y_1(t)y_2(x)-y_1(x)y_2(t)}{y_1(t)y_2'(t)-y_1'(t)y_2(t)},
$$
and by Liouville's formula the denominator may be replaced by $W(x_0)\exp\big(-\int_{x_0}^tp_1\big)$, so the Wronskian needs to be computed at only one point:

$$
y^*(x)=\frac{1}{W(x_0)}\int_{x_0}^x\big(y_1(t)y_2(x)-y_1(x)y_2(t)\big)\,\mathrm{e}^{\int_{x_0}^tp_1(s)\,\mathrm{d}s}f(t)\,\mathrm{d}t.
$$

**Example 9.2.1** Solve $x^2y''-2xy'+2y=x^3$ ($x>0$). In normal form the equation is $y''-\frac2xy'+\frac2{x^2}y=x$. The homogeneous equation is a Cauchy–Euler equation with solutions $y_1=x$, $y_2=x^2$, and $W(t)=t^2$, so

$$
K(x,t)=\frac{tx^2-t^2x}{t^2}=\frac{x^2}{t}-x,\qquad y^*=\int_1^x\Big(\frac{x^2}{t}-x\Big)t\,\mathrm{d}t=\frac{x^3}{2}-x^2+\frac{x}{2}.
$$
Discarding the homogeneous part, we may take the particular solution $\frac{x^3}{2}$; the general solution is $y=C_1x+C_2x^2+\frac{x^3}{2}$.

### 9.2.3. The Cauchy Function of an Equation with Constant Coefficients

An equation with constant coefficients is invariant under translations in time, so $K(x,t)$ depends only on $x-t$: $K(x,t)=k(x-t)$, where $k$ is the solution of the homogeneous equation with $k(0)=\cdots=k^{(n-2)}(0)=0$ and $k^{(n-1)}(0)=1$ (as a function of $x$, $k(x-t)$ satisfies the conditions in statement 1 of Theorem 9.2.2). Formula (9.5) then becomes a convolution,

$$
y^*(x)=\int_{x_0}^xk(x-t)f(t)\,\mathrm{d}t.
$$
For a second-order equation $y''+ay'+by=f$ with characteristic roots $\lambda_1,\lambda_2$:

| Characteristic roots | $k(s)$ | Particular solution $y^*(x)$ |
|---|---|---|
| Real roots $\lambda_1\ne\lambda_2$ | $\dfrac{\mathrm{e}^{\lambda_2s}-\mathrm{e}^{\lambda_1s}}{\lambda_2-\lambda_1}$ | $\displaystyle\int_{x_0}^x\frac{\mathrm{e}^{\lambda_2(x-t)}-\mathrm{e}^{\lambda_1(x-t)}}{\lambda_2-\lambda_1}f(t)\,\mathrm{d}t$ |
| Double root $\lambda$ | $s\,\mathrm{e}^{\lambda s}$ | $\displaystyle\int_{x_0}^x(x-t)\mathrm{e}^{\lambda(x-t)}f(t)\,\mathrm{d}t$ |
| Complex roots $\alpha\pm\mathrm{i}\beta$ | $\dfrac{\mathrm{e}^{\alpha s}\sin\beta s}{\beta}$ | $\displaystyle\int_{x_0}^x\frac{\mathrm{e}^{\alpha(x-t)}\sin\beta(x-t)}{\beta}f(t)\,\mathrm{d}t$ |

In particular, a particular solution of $y''+n^2y=f$ ($n>0$) is

$$
y^*(x)=\frac1n\int_{x_0}^x\sin n(x-t)f(t)\,\mathrm{d}t=\frac{\sin nx}{n}\int_{x_0}^x\cos nt\,f(t)\,\mathrm{d}t-\frac{\cos nx}{n}\int_{x_0}^x\sin nt\,f(t)\,\mathrm{d}t.
$$

**Example 9.2.2** Solve $y''-2y'+y=\dfrac{\mathrm{e}^x}{x}$ ($x>0$). Here $1$ is a double root and $k(s)=s\mathrm{e}^s$, so

$$
y^*=\int_1^x(x-t)\mathrm{e}^{x-t}\frac{\mathrm{e}^t}{t}\,\mathrm{d}t=\mathrm{e}^x\int_1^x\Big(\frac xt-1\Big)\mathrm{d}t=\mathrm{e}^x(x\ln x-x+1).
$$
Discarding the homogeneous part $(1-x)\mathrm{e}^x$, the general solution is $y=(C_1+C_2x)\mathrm{e}^x+x\mathrm{e}^x\ln x$. The method of undetermined coefficients does not apply to this right-hand side, whereas the kernel formula has no such restriction.

## 9.3. Reduction of Order When Some Solutions Are Known

### 9.3.1. Second-Order Equations

Let $\varphi$ be a nonzero solution of $y''+p(x)y'+q(x)y=0$ on $I$ (with $\varphi\ne0$ on the interval under consideration). A solution $y$ linearly independent of $\varphi$ can be found directly from Liouville's formula: $W[\varphi,y]=\varphi y'-\varphi'y=W(x_0)\mathrm{e}^{-\int_{x_0}^xp}$ is a first-order linear equation for $y$, and dividing both sides by $\varphi^2$ gives

$$
\Big(\frac{y}{\varphi}\Big)'=\frac{W(x_0)}{\varphi^2(x)}\mathrm{e}^{-\int_{x_0}^xp(t)\,\mathrm{d}t}.
$$
Integrating, $y=\varphi\Big(\dfrac{y(x_0)}{\varphi(x_0)}+W(x_0)\displaystyle\int_{x_0}^x\frac{\mathrm{e}^{-\int_{x_0}^tp(s)\,\mathrm{d}s}}{\varphi^2(t)}\,\mathrm{d}t\Big)$, which gives all solutions. Taking $y(x_0)=0$ and $W(x_0)=1$:

**Proposition 9.3.1** If $\varphi$ is a nowhere-vanishing solution of $y''+py'+qy=0$, then

$$
\psi(x)=\varphi(x)\int_{x_0}^x\frac{1}{\varphi^2(t)}\exp\Big(-\int_{x_0}^tp(s)\,\mathrm{d}s\Big)\mathrm{d}t\tag{9.6}
$$
is a solution linearly independent of $\varphi$, the general solution is $y=C_1\varphi+C_2\psi$, and $W[\varphi,\psi](x_0)=1$.

This agrees with the result of reduction of order by $y=\varphi z$ in [Section 16.2.1 of 2.2.16](/2.2.16#sec-16.2.1). Once $\varphi$ and $\psi$ are known, a particular solution of the nonhomogeneous equation is given by the kernel of Definition 9.2.1; so knowing one homogeneous solution suffices to solve the nonhomogeneous equation.

**Example 9.3.1** (1) $y''+py'+\frac{p^2}{4}y=0$ ($p$ a real constant): $\varphi=\mathrm{e}^{\lambda x}$ with $\lambda=-\frac p2$. In (9.6) (with $x_0=0$) the integrand is $\mathrm{e}^{-2\lambda t}\mathrm{e}^{-pt}=1$, so $\psi=x\mathrm{e}^{\lambda x}$. This is where the solution $x\mathrm{e}^{\lambda x}$ for a double root of an equation with constant coefficients comes from.

(2) The Cauchy–Euler equation $x^2y''+pxy'+\frac{(p-1)^2}{4}y=0$ ($x>0$): substituting $y=x^\lambda$ gives $\lambda^2+(p-1)\lambda+\frac{(p-1)^2}{4}=0$, with the double root $\lambda=\frac{1-p}{2}$. In normal form the coefficient is $p(x)=\frac px$; taking $x_0=1$ and using $2\lambda+p=1$,

$$
\psi=x^\lambda\int_1^x\frac{t^{-p}}{t^{2\lambda}}\,\mathrm{d}t=x^\lambda\int_1^x\frac{\mathrm{d}t}{t}=x^\lambda\ln x.
$$
This is where the solution $x^\lambda\ln x$ for a double root of a Cauchy–Euler equation comes from.

### 9.3.2. Equations of Order $n$

Let $\varphi$ be a nowhere-vanishing solution of (9.2). Put $y=\varphi z$ and substitute into (9.2), using the Leibniz formula $y^{(k)}=\sum_{j=0}^k\binom kj\varphi^{(j)}z^{(k-j)}$. The coefficient of $z$ itself is $L(\varphi)=0$, so $z$ does not appear, and dividing by $\varphi$ gives

$$
z^{(n)}+P_1(x)z^{(n-1)}+\cdots+P_{n-1}(x)z'=0,\qquad P_1=p_1+n\frac{\varphi'}{\varphi},\quad P_2=p_2+(n-1)p_1\frac{\varphi'}{\varphi}+\binom n2\frac{\varphi''}{\varphi},\quad\dots
$$
Putting $u=z'$ then gives a homogeneous linear equation of order $n-1$ for $u$. If $u_1,\dots,u_{n-1}$ is a fundamental set of solutions of it, then $\varphi,\ \varphi\int u_1,\ \dots,\ \varphi\int u_{n-1}$ is a fundamental set of solutions of (9.2). In general, knowing $k$ linearly independent solutions allows the order of the equation to be reduced by $k$ (each reduction uses up one known solution: $y_j=\varphi z_j$ gives the solution $(y_j/\varphi)'$ of the $u$-equation).

For the third-order equation $y'''+py''+qy'+ry=0$:

$$
u''+\Big(\frac{3\varphi'}{\varphi}+p\Big)u'+\Big(\frac{3\varphi''}{\varphi}+\frac{2p\varphi'}{\varphi}+q\Big)u=0.
$$

**Example 9.3.2** The equation $x^3y'''-3x^2y''+6xy'-6y=0$ ($x>0$) has the solution $\varphi=x$. In normal form $p=-\frac3x$ and $q=\frac{6}{x^2}$; substituting into the equation above, the coefficient of $u'$ is $\frac3x-\frac3x=0$, and the coefficient of $u$ is $0+2\cdot(-\frac3x)\cdot\frac1x+\frac{6}{x^2}=0$. Hence $u''=0$, $u=c_1+c_2x$, $z=c_1x+\frac{c_2}2x^2+c_3$, and

$$
y=\varphi z=C_1x+C_2x^2+C_3x^3.
$$
(This is a Cauchy–Euler equation with indicial equation $(\lambda-1)(\lambda-2)(\lambda-3)=0$; see Section 9.5.)

## 9.4. Equations with Constant Coefficients

For the equation with constant coefficients $y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=0$, the corresponding system (9.3) has constant coefficients; its coefficient matrix is the companion matrix $C$, whose **characteristic polynomial** is exactly $P(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$ ([2.1.6](/2.1.6)). Corollary 8.5.1 of the previous chapter shows that solutions are sums of terms $p_j(x)\mathrm{e}^{\lambda_jx}$, where the degree of the polynomial $p_j$ is controlled by the sizes of the Jordan blocks for $\lambda_j$. For a companion matrix, this size equals exactly the algebraic multiplicity:

**Proposition 9.4.1** Every **eigenvalue** of a companion matrix has geometric multiplicity 1; hence each eigenvalue corresponds to a single Jordan block, whose size equals the multiplicity of the eigenvalue as a **characteristic root**.

**Proof** Deleting the first column and the last row of $C-\lambda I$ leaves an $(n-1)\times(n-1)$ minor that is lower triangular with ones on the diagonal (the ones of the superdiagonal move onto the diagonal), so it equals $1$. Hence $\operatorname{rank}(C-\lambda I)\ge n-1$, and the eigenspace is at most one-dimensional. $\square$

Therefore a characteristic root $\lambda$ of multiplicity $m$ contributes exactly $\mathrm{e}^{\lambda x},x\mathrm{e}^{\lambda x},\dots,x^{m-1}\mathrm{e}^{\lambda x}$; this is the structural reason behind [Theorem 16.3.1 of 2.2.16](/2.2.16#thm-16.3.1). The eigenvector of the companion matrix for $\lambda$ is $(1,\lambda,\dots,\lambda^{n-1})^{\mathsf T}$, which corresponds to the solution $\mathrm{e}^{\lambda x}$.

For the concrete methods of solution (the **characteristic equation**, the method of undetermined coefficients, the **operator method**), see [Sections 16.3 and 16.4 of 2.2.16](/2.2.16#sec-16.3); when the nonhomogeneous term is not of exponential type, use the kernel formula of Section 9.2.3. Conditions for solutions to be bounded or to tend to zero as $x\to+\infty$ are given in [2.4.11](/2.4.11).

## 9.5. Cauchy–Euler Equations

**Definition 9.5.1 (Cauchy–Euler Equation)** An equation of the form

$$
x^ny^{(n)}+a_1x^{n-1}y^{(n-1)}+\cdots+a_{n-1}xy'+a_ny=f(x)\qquad(a_k\text{ real constants})\tag{9.7}
$$
is called a **Cauchy–Euler equation**.

The point $x=0$ is a singular point of the coefficients, so we work on $x>0$ (for $x<0$, put $x=-\mathrm{e}^t$; the results are the same with $x$ replaced by $\lvert x\rvert$). Putting $x=\mathrm{e}^t$ and $\mathrm{D}=\frac{\mathrm{d}}{\mathrm{d}t}$, we have

$$
x\frac{\mathrm{d}y}{\mathrm{d}x}=\mathrm{D}y,\qquad x^2\frac{\mathrm{d}^2y}{\mathrm{d}x^2}=\mathrm{D}(\mathrm{D}-1)y,\qquad\dots,\qquad x^k\frac{\mathrm{d}^ky}{\mathrm{d}x^k}=\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)y
$$
(for the proof by induction see [Proposition 16.4.2 of 2.2.16](/2.2.16#prop-16.4.2)), and (9.7) becomes an equation with constant coefficients. Consequently, the homogeneous Cauchy–Euler equation has solutions of the form $y=\mathrm{e}^{\lambda t}=x^\lambda$, which can be substituted directly: $x^ky^{(k)}=\lambda(\lambda-1)\cdots(\lambda-k+1)x^\lambda$, which gives

$$
F(\lambda)=\lambda(\lambda-1)\cdots(\lambda-n+1)+a_1\lambda(\lambda-1)\cdots(\lambda-n+2)+\cdots+a_{n-1}\lambda+a_n=0.\tag{9.8}
$$

**Theorem 9.5.1** Suppose a real root $\lambda_0$ of $F(\lambda)=0$ has multiplicity $m$, and a pair of complex roots $\alpha\pm\mathrm{i}\beta$ ($\beta>0$) has multiplicity $m$. They correspond, respectively, to the $m$ and $2m$ real solutions of the homogeneous Cauchy–Euler equation on $x>0$

$$
x^{\lambda_0},\ x^{\lambda_0}\ln x,\ \dots,\ x^{\lambda_0}\ln^{m-1}x;
$$

$$
x^\alpha\ln^jx\cos(\beta\ln x),\quad x^\alpha\ln^jx\sin(\beta\ln x),\qquad j=0,1,\dots,m-1,
$$
and the $n$ functions corresponding to all the roots form a fundamental set of solutions.

**Proof** The substitution $x=\mathrm{e}^t$ gives an equation with constant coefficients whose characteristic polynomial is $F$. By [Theorem 16.3.1 of 2.2.16](/2.2.16#thm-16.3.1), the functions $t^j\mathrm{e}^{\lambda_0t}$ and $t^j\mathrm{e}^{\alpha t}\cos\beta t$, $t^j\mathrm{e}^{\alpha t}\sin\beta t$ form a fundamental set of solutions of it; now substitute back $t=\ln x$. $\square$

**Example 9.5.1** (1) $x^2y''-xy'+y=0$: $F(\lambda)=\lambda(\lambda-1)-\lambda+1=(\lambda-1)^2$, and the general solution is $y=(C_1+C_2\ln x)x$.

(2) $x^2y''+3xy'+5y=0$: $F(\lambda)=\lambda^2+2\lambda+5$ with roots $-1\pm2\mathrm{i}$, and the general solution is $y=\dfrac1x\big(C_1\cos(2\ln x)+C_2\sin(2\ln x)\big)$.

A nonhomogeneous Cauchy–Euler equation is transformed into an equation with constant coefficients and then solved by the kernel formula of Section 9.2.3 or by undetermined coefficients ([Example 16.4.10 of 2.2.16](/2.2.16#ex-16.4.10)). The Cauchy–Euler equation is the prototype of the theory of regular singular points in the next chapter: the indicial equation is the second-order case of (9.8).

## 9.6. Periodic Solutions of $y''+M^2y=f$

Let $f$ be a continuous $T$-periodic function on $\mathbb{R}$ ($T>0$), and let $M>0$. Consider

$$
y''+M^2y=f(x),\qquad x\in\mathbb{R}.\tag{9.9}
$$
This equation describes an undamped oscillator driven by a periodic external force. The question is: when does it have a solution of period $T$?

**Theorem 9.6.1** A solution $y$ of Eq. (9.9) is $T$-periodic if and only if $y(0)=y(T)$ and $y'(0)=y'(T)$.

**Proof** Necessity is obvious. Sufficiency: since $f(x+T)=f(x)$, the function $y(x+T)$ is also a solution of (9.9). Let $z(x)=y(x+T)-y(x)$. Then $z''+M^2z=f(x+T)-f(x)=0$ and $z(0)=z'(0)=0$, so $z\equiv0$ by the uniqueness in Theorem 9.1.1, that is, $y(x+T)\equiv y(x)$. $\square$

The proof uses only the linearity of the equation and the periodicity of its coefficients, so the same holds for any linear system with $T$-periodic coefficients: a solution is $T$-periodic if and only if $\boldsymbol{x}(0)=\boldsymbol{x}(T)$.

**Theorem 9.6.2** 

1. (Nonresonance) If $MT\notin2\pi\mathbb{Z}$, then (9.9) has a unique $T$-periodic solution;
2. (Resonance) If $MT=2\pi k$ ($k$ a positive integer), then (9.9) has a $T$-periodic solution if and only if

$$
\int_0^Tf(t)\cos Mt\,\mathrm{d}t=\int_0^Tf(t)\sin Mt\,\mathrm{d}t=0,
$$
in which case all solutions of (9.9) are $T$-periodic; otherwise all solutions are unbounded.

**Proof** The general solution is $y=c_1\cos Mx+c_2\sin Mx+y^*(x)$ with $y^*(x)=\frac1M\int_0^x\sin M(x-t)f(t)\,\mathrm{d}t$, so that $y^*(0)=(y^*)'(0)=0$. By Theorem 9.6.1, $y$ is $T$-periodic if and only if

$$
\begin{cases}c_1(\cos MT-1)+c_2\sin MT=-y^*(T),\\-c_1M\sin MT+c_2M(\cos MT-1)=-(y^*)'(T).\end{cases}
$$
The determinant of the coefficients is $M\big((\cos MT-1)^2+\sin^2MT\big)=2M(1-\cos MT)$.

1: If $MT\notin2\pi\mathbb{Z}$, the determinant is nonzero, and $(c_1,c_2)$ exists and is unique.

2: If $MT=2\pi k$, all coefficients vanish, and the system is solvable if and only if $y^*(T)=(y^*)'(T)=0$. Since $\sin M(T-t)=-\sin Mt$ and $\cos M(T-t)=\cos Mt$,

$$
y^*(T)=-\frac1M\int_0^T\sin Mt\,f(t)\,\mathrm{d}t,\qquad(y^*)'(T)=\int_0^T\cos M(T-t)f(t)\,\mathrm{d}t=\int_0^T\cos Mt\,f(t)\,\mathrm{d}t,
$$
which gives the stated condition; in that case every pair $(c_1,c_2)$ satisfies the system. If the condition fails, let $\boldsymbol{d}=(y(T)-y(0),y'(T)-y'(0))$; it does not depend on $c_1,c_2$ and is nonzero. The function $z(x)=y(x+T)-y(x)$ is a solution of the homogeneous equation with $(z(0),z'(0))=\boldsymbol{d}$, so it is a nonzero $T$-periodic function, and therefore $y(x+jT)=y(x)+\sum_{i<j}z(x+iT)=y(x)+jz(x)$ is unbounded. $\square$

The meaning of condition 2: when $f$ is expanded in a Fourier series, $\cos Mt$ and $\sin Mt$ are exactly the terms whose frequency equals the natural frequency $M$. **Resonance** occurs when the external force contains a component at the natural frequency ([Section 16.5.2 of 2.2.16](/2.2.16#sec-16.5.2)), and the amplitude then grows linearly; when it contains no such component, there is no resonance even if $MT\in2\pi\mathbb{Z}$.

**Example 9.6.1** (1) $y''+2y=\cos x$, $T=2\pi$, $M=\sqrt2$, so $MT\notin2\pi\mathbb{Z}$: the unique $2\pi$-periodic solution is $\cos x$. The other solutions are $\cos x$ plus $c_1\cos\sqrt2x+c_2\sin\sqrt2x$; they are almost periodic but not periodic.

(2) $y''+y=\cos x$, $T=2\pi$, $M=1$: $\int_0^{2\pi}\cos^2t\,\mathrm{d}t=\pi\ne0$, so there is no periodic solution. The general solution is $y=c_1\cos x+c_2\sin x+\frac x2\sin x$, whose amplitude grows linearly.

(3) $y''+4y=\sin x$, $T=2\pi$, $M=2$: $\int_0^{2\pi}\sin t\cos2t\,\mathrm{d}t=\int_0^{2\pi}\sin t\sin2t\,\mathrm{d}t=0$, so all solutions $y=c_1\cos2x+c_2\sin2x+\frac13\sin x$ are $2\pi$-periodic.

![Solutions of y'' + M^2 y = f (with initial values y(0) = y'(0) = 0 and one other set of initial values). Left: nonresonant y'' + 2y = cos x; the solutions oscillate around the unique 2π-periodic solution cos x (thick line) without being periodic. Middle: resonant y'' + y = cos x; the amplitude grows linearly. Right: y'' + 4y = sin x; although MT ∈ 2πZ, the forcing contains no component at the natural frequency, and all solutions are 2π-periodic](./plots/periodic-forcing.py)

## Summary

| Topic | Result |
|---|---|
| Reduction to a system | $\boldsymbol{x}=(y,\dots,y^{(n-1)})^{\mathsf T}$; the coefficient matrix is a companion matrix with $\operatorname{tr}=-p_1$ |
| Structure of solutions | The solution space is $n$-dimensional; $n$ solutions are independent $\Leftrightarrow$ $W$ is nonzero at one point; $W(x)=W(x_0)\mathrm{e}^{-\int_{x_0}^xp_1}$ |
| Equation determined by solutions | $W[y_1,\dots,y_n,y]/W[y_1,\dots,y_n]=0$ (Proposition 9.1.1) |
| Variation of constants formula | $y^*=\int_{x_0}^x\sum_ky_k(x)W_k(t)f(t)/W(t)\,\mathrm{d}t$, where $W_k$ is a cofactor of the $n$th row |
| Cauchy function | $K(\cdot,t)$ is the homogeneous solution with $\partial_x^jK(t,t)=\delta_{j,n-1}$; for constant coefficients $K=k(x-t)$ and the particular solution is a convolution |
| Reduction of order | Second order: $\psi=\varphi\int\varphi^{-2}\mathrm{e}^{-\int p}$; order $n$: $y=\varphi z$, $u=z'$ lowers the order by one |
| Constant coefficients | Each eigenvalue of a companion matrix has a single Jordan block; a root of multiplicity $m$ gives $x^j\mathrm{e}^{\lambda x}$ ($j<m$) |
| Cauchy–Euler equations | $y=x^\lambda$, $F(\lambda)=0$; a root of multiplicity $m$ gives $x^\lambda\ln^jx$ |
| Periodic solutions | $T$-periodic $\Leftrightarrow$ $\boldsymbol{x}(0)=\boldsymbol{x}(T)$; unique when $MT\notin2\pi\mathbb{Z}$; under resonance $f$ must be orthogonal to $\cos Mt$ and $\sin Mt$ |
