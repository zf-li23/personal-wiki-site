---
title: Power Series Solutions
source_hash: ff44977df870
---

Linear equations with variable coefficients generally cannot be solved in terms of elementary functions. The most important variable-coefficient equations of physics (the Legendre, Bessel, Hermite and Airy equations, among others) arise from solving partial differential equations by separation of variables: separating Laplace's equation in spherical coordinates gives the Legendre equation, and separating Laplace's equation, the wave equation or the heat equation in cylindrical or polar coordinates gives the Bessel equation. Their solutions define new "special functions", and the most direct way to study them is to write the solutions as **power series**.

This chapter first treats the case in which the coefficients can be expanded in power series near a point (an ordinary point): the solutions are then power series as well, with coefficients determined by a recurrence relation. We then turn to regular singular points, where the coefficients have only a "weak" singularity; the Frobenius method gives solutions of the form $x^\rho\sum a_kx^k$, possibly with logarithmic terms, and the Cauchy–Euler equation of the previous chapter is the prototype. Finally we use both methods to study Legendre polynomials and Bessel functions and derive the basic properties needed for separation of variables in partial differential equations ([2.5](/2.5)): orthogonality, recurrence relations, zeros and asymptotic behavior. The zeros and orthogonality of these functions receive a unified explanation in Sturm–Liouville theory ([2.4.12](/2.4.12)).

## 10.1. Power Series Solutions at Ordinary Points

### 10.1.1. Ordinary Points and Cauchy's Theorem

Consider the second-order homogeneous linear equation

$$
y''+p(x)y'+q(x)y=0.\tag{10.1}
$$

**Definition 10.1.1** If $p(x)$ and $q(x)$ can both be expanded in convergent power series $\sum_kc_k(x-x_0)^k$ in some neighborhood of $x_0$, then $x_0$ is called an **ordinary point** of Eq. (10.1); otherwise $x_0$ is called a singular point of the equation.

For an equation with rational coefficients, for example, $x_0$ is an ordinary point if and only if it is not a zero of the denominators of $p$ and $q$ (in lowest terms).

**Theorem 10.1.1 (Cauchy)** Suppose $p$ and $q$ can be expanded in convergent power series in $\lvert x-x_0\rvert<R$. Then every solution of Eq. (10.1) can be expanded in a power series $y=\sum_{k=0}^\infty a_k(x-x_0)^k$ convergent in $\lvert x-x_0\rvert<R$, where $a_0=y(x_0)$ and $a_1=y'(x_0)$ are arbitrary and the remaining coefficients are uniquely determined by the recurrence relation obtained by substituting into the equation and comparing coefficients.

**Proof** (Sketch.) We may assume $x_0=0$. Substituting $y=\sum a_kx^k$ and multiplying power series (the **Cauchy product**), comparison of the coefficients of $x^k$ gives

$$
(k+2)(k+1)a_{k+2}=-\sum_{j=0}^{k}\big((j+1)a_{j+1}p_{k-j}+a_jq_{k-j}\big),
$$
so once $a_0,a_1$ are fixed all the $a_k$ are uniquely determined, and the only question is whether the resulting series converges. Take any $0<r<R$. The series $\sum p_kr^k$ and $\sum q_kr^k$ converge, so $\lvert p_k\rvert,\lvert q_k\rvert\le M/r^k$. Replacing $\lvert p_k\rvert,\lvert q_k\rvert$ by $M/r^k$ and using $\lvert a_0\rvert,\lvert a_1\rvert$ as initial values, we obtain a comparison equation whose solution can be written explicitly; its power series coefficients satisfy $A_k\ge\lvert a_k\rvert$, and its radius of convergence is $r$ (the method of majorants). By the comparison test $\sum a_kx^k$ converges in $\lvert x\rvert<r$, and $r<R$ is arbitrary. A convergent power series can be differentiated term by term, so it is indeed a solution; by uniqueness, the solution with the same initial values coincides with it. $\square$

The radius of convergence is at least the distance from $x_0$ to the nearest (complex) singularity of $p$ and $q$. For example, the coefficient of $y''+\frac{1}{1+x^2}y=0$ is smooth on the whole real line, yet the power series solution at $x_0=0$ is only guaranteed to converge in $\lvert x\rvert<1$, because $\frac1{1+x^2}$ has singularities at $\pm\mathrm{i}$. This is a typical phenomenon of complex analysis ([2.3](/2.3)).

**Algorithm 10.1.1 (Power Series Method)** To solve Eq. (10.1) near an ordinary point $x_0$:

1. Set $y=\sum_{k\ge0}a_k(x-x_0)^k$ and expand the coefficients in powers of $x-x_0$ as well (for polynomial coefficients one usually multiplies the equation by a common denominator and works with the polynomial coefficients directly);
2. Substitute into the equation, collect like powers and set the coefficient of each power to zero; this gives the recurrence relation;
3. Take $(a_0,a_1)=(1,0)$ and $(0,1)$ in turn to obtain two linearly independent solutions (their Wronskian at $x_0$ equals 1).

**Example 10.1.1** Solve the Airy equation $y''=xy$. Setting $y=\sum a_kx^k$ gives $\sum_k(k+2)(k+1)a_{k+2}x^k=\sum_ka_{k-1}x^k$, so $a_2=0$ and

$$
a_{k+2}=\frac{a_{k-1}}{(k+2)(k+1)}\qquad(k\ge1).
$$
The coefficients split into three classes modulo 3: $a_2=a_5=a_8=\cdots=0$, and the other two classes are determined by $a_0$ and $a_1$ respectively. A fundamental set of solutions is

$$
y_1=1+\frac{x^3}{3\cdot2}+\frac{x^6}{6\cdot5\cdot3\cdot2}+\cdots,\qquad y_2=x+\frac{x^4}{4\cdot3}+\frac{x^7}{7\cdot6\cdot4\cdot3}+\cdots.
$$
The coefficients are reciprocals of products of integers and decay very quickly, so both series converge on all of $\mathbb{R}$ (in agreement with Theorem 10.1.1, since the coefficient $x$ is an entire function). The Airy equation describes the light intensity near a caustic in optics and the wave function near a turning point in quantum mechanics: the solutions oscillate for $x<0$ and grow or decay exponentially for $x>0$.

## 10.2. The Legendre Equation and Legendre Polynomials

### 10.2.1. Series Solutions of the Legendre Equation

**Definition 10.2.1 (Legendre Equation)** The equation

$$
(1-x^2)y''-2xy'+\nu(\nu+1)y=0\tag{10.2}
$$
is called the **Legendre equation** of order $\nu$ ($\nu$ a constant).

This equation arises from separating variables in Laplace's equation $\Delta u=0$ in spherical coordinates and setting $x=\cos\theta$ (in the axisymmetric case). The points $x=\pm1$ are singular points and $x=0$ is an ordinary point, so by Theorem 10.1.1 the power series solutions converge in $\lvert x\rvert<1$. Substituting $y=\sum a_kx^k$ gives

$$
\sum_k\Big((k+2)(k+1)a_{k+2}-\big(k(k-1)+2k-\nu(\nu+1)\big)a_k\Big)x^k=0,
$$
that is,

$$
a_{k+2}=\frac{(k-\nu)(k+\nu+1)}{(k+2)(k+1)}a_k.\tag{10.3}
$$
Taking $(a_0,a_1)=(1,0)$ gives the even solution $y_1=1-\frac{\nu(\nu+1)}{2!}x^2+\frac{(\nu-2)\nu(\nu+1)(\nu+3)}{4!}x^4-\cdots$, and taking $(0,1)$ gives the odd solution $y_2=x-\frac{(\nu-1)(\nu+2)}{3!}x^3+\cdots$.

When $\nu=n$ is a nonnegative integer, the term $k=n$ in Eq. (10.3) makes $a_{n+2}=0$, so whichever of $y_1$, $y_2$ has the same parity as $n$ terminates at $x^n$ and becomes a polynomial of degree $n$.

### 10.2.2. Legendre Polynomials

**Definition 10.2.2 (Legendre Polynomials)** For each $n$, the polynomial solution of degree $n$ of the Legendre equation of order $n$ satisfying $P_n(1)=1$ is denoted $P_n(x)$; the polynomials $P_n$ are called the **Legendre polynomials**.

The first few are

$$
P_0=1,\quad P_1=x,\quad P_2=\frac{3x^2-1}{2},\quad P_3=\frac{5x^3-3x}{2},\quad P_4=\frac{35x^4-30x^2+3}{8},\quad P_5=\frac{63x^5-70x^3+15x}{8}.
$$
They can also be obtained by applying Gram–Schmidt orthogonalization on $[-1,1]$ to $1,x,x^2,\dots$ ([2.1.12](/2.1.12)); the orthogonality below explains why.

**Theorem 10.2.1 (Rodrigues' Formula)**

$$
P_n(x)=\frac{1}{2^nn!}\frac{\mathrm{d}^n}{\mathrm{d}x^n}(x^2-1)^n.
$$

**Proof** Let $u=(x^2-1)^n$. Then $(x^2-1)u'=2nxu$. Differentiating both sides $n+1$ times with the Leibniz rule gives

$$
(x^2-1)u^{(n+2)}+2(n+1)xu^{(n+1)}+n(n+1)u^{(n)}=2nxu^{(n+1)}+2n(n+1)u^{(n)},
$$
which simplifies to $(1-x^2)v''-2xv'+n(n+1)v=0$ with $v=u^{(n)}$. Hence $v$ is a polynomial solution of degree $n$. Writing $u=(x-1)^n(x+1)^n$, the Leibniz rule gives $v(1)=n!\,2^n$ (only the term in which $(x-1)^n$ is differentiated $n$ times lacks a factor $x-1$), so after division by $2^nn!$ the value at $x=1$ is 1. $\square$

**Theorem 10.2.2** Legendre polynomials have the following properties.

1. $P_n(-x)=(-1)^nP_n(x)$, $P_n(1)=1$, $P_n(-1)=(-1)^n$, and $\lvert P_n(x)\rvert\le1$ for $\lvert x\rvert\le1$;
2. (Orthogonality) $\displaystyle\int_{-1}^1P_m(x)P_n(x)\,\mathrm{d}x=\begin{cases}0,&m\ne n,\\\dfrac{2}{2n+1},&m=n;\end{cases}$
3. (Generating function) For $\lvert x\rvert\le1$ and $\lvert t\rvert<1$, $\displaystyle\frac{1}{\sqrt{1-2xt+t^2}}=\sum_{n=0}^\infty P_n(x)t^n$;
4. (Recurrence relations) $(n+1)P_{n+1}(x)=(2n+1)xP_n(x)-nP_{n-1}(x)$ and $(x^2-1)P_n'(x)=n\big(xP_n(x)-P_{n-1}(x)\big)$;
5. $P_n$ has exactly $n$ distinct zeros in $(-1,1)$.

**Proof** First part of 2: the Legendre equation can be written in the self-adjoint form $\big((1-x^2)y'\big)'+\nu(\nu+1)y=0$. Hence

$$
\big((1-x^2)P_n'\big)'P_m-\big((1-x^2)P_m'\big)'P_n=\big(m(m+1)-n(n+1)\big)P_mP_n,
$$
and the left-hand side equals $\big((1-x^2)(P_n'P_m-P_m'P_n)\big)'$. Integrating over $[-1,1]$, the boundary terms on the left contain the factor $1-x^2$ and vanish; for $m\ne n$ we have $m(m+1)\ne n(n+1)$, so $\int_{-1}^1P_mP_n=0$. For $m=n$, integrating by parts $n$ times using Rodrigues' formula gives $\int_{-1}^1P_n^2=\frac{(2n)!}{2^{2n}(n!)^2}\int_{-1}^1(1-x^2)^n\,\mathrm{d}x=\frac{2}{2n+1}$.

5: $P_n$ is orthogonal to every polynomial of degree less than $n$ (such polynomials are linear combinations of $P_0,\dots,P_{n-1}$). Suppose $P_n$ changes sign in $(-1,1)$ only at $x_1,\dots,x_k$ with $k<n$. Then $P_n(x)\prod_i(x-x_i)$ does not change sign in $(-1,1)$ and is not identically zero, so its integral is nonzero, contradicting orthogonality. Therefore $P_n$ has at least $n$ sign changes, while a polynomial of degree $n$ has at most $n$ zeros.

1 follows from the definition and the parity in Eq. (10.3) (the bound $\lvert P_n\rvert\le1$ can be obtained from Laplace's integral representation $P_n(x)=\frac1\pi\int_0^\pi(x+\sqrt{x^2-1}\cos\varphi)^n\,\mathrm{d}\varphi$, which we omit); 3 and 4 can be obtained by differentiating the generating function with respect to $t$ and $x$ and comparing coefficients, which we also omit. $\square$

Thus $\{P_n\}$ is an **orthogonal system of functions** on $[-1,1]$, and it is complete: for a piecewise smooth function $f$ on $[-1,1]$, the Legendre series

$$
f(x)\sim\sum_{n=0}^\infty c_nP_n(x),\qquad c_n=\frac{2n+1}{2}\int_{-1}^1f(x)P_n(x)\,\mathrm{d}x
$$
converges to $f(x)$ at points of continuity of $f$ and to the average of the one-sided limits at jump points (stated without proof). The generating function has a direct meaning in electrostatics: $\frac{1}{\lvert\boldsymbol{r}-\boldsymbol{r}'\rvert}=\sum_n\frac{r'^n}{r^{n+1}}P_n(\cos\gamma)$ for $r'<r$, where $\gamma$ is the angle between the two vectors; this is the multipole expansion.

![Legendre polynomials P_0, …, P_5 on [-1, 1]: P_n has exactly n zeros, P_n(1) = 1, |P_n| ≤ 1, and P_n has the parity of n](./plots/legendre-polynomials.py)

### 10.2.3. Bounded Solutions and Legendre Functions of the Second Kind

For $\nu=n$ the other series solution does not terminate; suitably normalized, it is denoted $Q_n(x)$ (the Legendre function of the second kind). For example,

$$
Q_0(x)=\frac12\ln\frac{1+x}{1-x},\qquad Q_1(x)=\frac x2\ln\frac{1+x}{1-x}-1,
$$
which tend to infinity logarithmically as $x\to\pm1$. More generally, we state the following fact: the Legendre equation has a bounded solution on $[-1,1]$ that is not identically zero if and only if $\nu(\nu+1)=n(n+1)$ for some nonnegative integer $n$, and the bounded solutions are then the constant multiples of $P_n$. In spherical coordinates $x=\cos\theta=\pm1$ corresponds to the poles, and the physical requirement that the solution be bounded at the poles restricts the separation constant to $n(n+1)$. This is an example of a singular Sturm–Liouville problem ([2.4.12](/2.4.12)): the eigenvalues are $n(n+1)$ and the eigenfunctions are $P_n$.

Without axial symmetry, separation of variables in spherical coordinates gives the associated Legendre equation

$$
(1-x^2)y''-2xy'+\Big(n(n+1)-\frac{m^2}{1-x^2}\Big)y=0,
$$
whose bounded solutions are the associated Legendre functions $P_n^m(x)=(1-x^2)^{m/2}\dfrac{\mathrm{d}^m}{\mathrm{d}x^m}P_n(x)$ ($0\le m\le n$). The functions $P_n^m(\cos\theta)\mathrm{e}^{\mathrm{i}m\varphi}$ are the spherical harmonics.

## 10.3. Regular Singular Points and the Frobenius Method

### 10.3.1. Regular Singular Points and the Indicial Equation

Near a singular point the solutions are in general not power series. The simplest example is the Cauchy–Euler equation $x^2y''+axy'+by=0$: $x=0$ is a singular point, and the solutions are $x^\rho$ or $x^\rho\ln x$, where $\rho$ is a root of $\rho(\rho-1)+a\rho+b=0$ (Theorem 9.5.1). If the singularity is no worse than that of the Cauchy–Euler equation, we may expect solutions of the form "$x^\rho$ times a power series".

**Definition 10.3.1** Let $x_0$ be a singular point of Eq. (10.1). If $(x-x_0)p(x)$ and $(x-x_0)^2q(x)$ can both be expanded in convergent power series in some neighborhood of $x_0$, then $x_0$ is called a **regular singular point**; otherwise it is called an irregular singular point.

For example, $x=0$ is a regular singular point of the Cauchy–Euler equation and of the Bessel equation $x^2y''+xy'+(x^2-\nu^2)y=0$, and $x=\pm1$ are regular singular points of the Legendre equation; $x=0$ is an irregular singular point of $x^3y''+y=0$.

Let $x_0=0$ be a regular singular point. Multiplying the equation by $x^2$, we write it as

$$
x^2y''+xP(x)y'+Q(x)y=0,\qquad P(x)=\sum_{k\ge0}p_kx^k,\quad Q(x)=\sum_{k\ge0}q_kx^k,\tag{10.4}
$$
where both series converge in $\lvert x\rvert<R$. Substituting $y=x^\rho\sum_{k\ge0}a_kx^k$ ($a_0\ne0$) on $x>0$ and comparing the coefficients of $x^{\rho+k}$ gives

$$
F(\rho+k)a_k=-\sum_{j=0}^{k-1}\big((\rho+j)p_{k-j}+q_{k-j}\big)a_j,\qquad F(\rho)=\rho(\rho-1)+p_0\rho+q_0.\tag{10.5}
$$
For $k=0$ this reads $F(\rho)a_0=0$, so $\rho$ must be a root of $F$.

**Definition 10.3.2** The equation $F(\rho)=\rho(\rho-1)+p_0\rho+q_0=0$ is called the **indicial equation** of Eq. (10.4) at the regular singular point $x=0$, and its roots are called the indices (or exponents).

Since $p_0=\lim_{x\to0}xp(x)$ and $q_0=\lim_{x\to0}x^2q(x)$, the indicial equation is just the characteristic equation of the Cauchy–Euler equation obtained by replacing the coefficients with their lowest-order approximations.

### 10.3.2. The Frobenius Theorem

**Theorem 10.3.1 (Frobenius)** Let $x=0$ be a regular singular point of Eq. (10.4), let the series $P$ and $Q$ converge in $\lvert x\rvert<R$, and let the indices be $\rho_1,\rho_2$ with $\operatorname{Re}\rho_1\ge\operatorname{Re}\rho_2$. Then on $0<x<R$:

1. The equation has a solution $y_1=x^{\rho_1}\sum_{k\ge0}a_kx^k$ with $a_0=1$;
2. If $\rho_1-\rho_2\notin\mathbb{Z}$, there is a second, linearly independent solution $y_2=x^{\rho_2}\sum_{k\ge0}b_kx^k$ with $b_0=1$;
3. If $\rho_1=\rho_2$, there is a second, linearly independent solution $y_2=y_1\ln x+x^{\rho_1}\sum_{k\ge1}b_kx^k$;
4. If $\rho_1-\rho_2=N$ is a positive integer, there is a second, linearly independent solution $y_2=cy_1\ln x+x^{\rho_2}\sum_{k\ge0}b_kx^k$ with $b_0=1$, where the constant $c$ may be zero.

All the power series above converge in $\lvert x\rvert<R$. On $-R<x<0$, replace $x^\rho$ and $\ln x$ by $\lvert x\rvert^\rho$ and $\ln\lvert x\rvert$.

**Proof** (Sketch.) We have $F(\rho)=(\rho-\rho_1)(\rho-\rho_2)$. For $\rho=\rho_1$, $F(\rho_1+k)=k(k+\rho_1-\rho_2)\ne0$ for $k\ge1$ (because $\operatorname{Re}(\rho_1-\rho_2)\ge0$), so Eq. (10.5) determines the $a_k$ one by one. Convergence is proved with majorants as in Theorem 10.1.1; the key point is that $\lvert F(\rho_1+k)\rvert$ grows like $k^2$. For $\rho=\rho_2$, as long as $F(\rho_2+k)=k(k-N)$ is nonzero for all $k\ge1$, that is, as long as $\rho_1-\rho_2$ is not a positive integer, we likewise obtain $y_2$; when $\rho_1\ne\rho_2$ the leading terms $x^{\rho_1}$ and $x^{\rho_2}$ of the two solutions differ, so they are linearly independent.

In cases 3 and 4 the recurrence meets $F(\rho_2+N)=0$ at $k=N$. If the right-hand side of Eq. (10.5) happens to vanish there, $b_N$ is arbitrary and we are in the case $c=0$; otherwise there is no solution of this form and a logarithmic term is needed. The form of the logarithmic term follows from the reduction-of-order formula (9.6): $y_2=y_1\int\frac{\mathrm{e}^{-\int p}}{y_1^2}$, where $\mathrm{e}^{-\int p}=x^{-p_0}\cdot(\text{power series})$ and $y_1^{-2}=x^{-2\rho_1}\cdot(\text{power series})$. Since $p_0=1-\rho_1-\rho_2$, the integrand is $x^{-1-N}\cdot(\text{power series})$; on integration the $x^{-1}$ term produces $\ln x$ and the remaining terms give $x^{-N}\cdot(\text{power series})$. $\square$

**Algorithm 10.3.1 (Frobenius Method)** To solve near a regular singular point $x=0$:

1. Write the equation in the form (10.4) and find $p_0,q_0$ and the roots $\rho_1,\rho_2$ of the indicial equation;
2. For $\rho_1$, compute $y_1$ from the recurrence (10.5);
3. Depending on whether $\rho_1-\rho_2$ is an integer, substitute $y_2$ in the form given by Theorem 10.3.1, or find $y_2$ by the reduction-of-order formula (9.6).

**Example 10.3.1** Solve $2xy''+y'+y=0$ ($x>0$). Multiplying by $\frac x2$ gives $x^2y''+\frac x2y'+\frac x2y=0$, so $p_0=\frac12$ and $q_0=0$; the indicial equation $\rho(\rho-1)+\frac\rho2=0$ has roots $\rho_1=\frac12$ and $\rho_2=0$, whose difference is not an integer. Substituting directly into the original equation, the coefficient of $x^{\rho+k-1}$ gives

$$
(\rho+k)(2\rho+2k-1)a_k=-a_{k-1}.
$$
For $\rho=0$: $a_k=-\frac{a_{k-1}}{k(2k-1)}$, and $y_2=1-x+\frac{x^2}{6}-\frac{x^3}{90}+\cdots=\sum_k\frac{(-1)^k(2x)^k}{(2k)!}=\cos\sqrt{2x}$. For $\rho=\frac12$: $a_k=-\frac{a_{k-1}}{k(2k+1)}$, and $y_1=\sqrt x\big(1-\frac x3+\frac{x^2}{30}-\cdots\big)=\frac{1}{\sqrt2}\sin\sqrt{2x}$. The general solution is $y=C_1\cos\sqrt{2x}+C_2\sin\sqrt{2x}$ (as a check, the substitution $x=s^2/2$ turns the equation into $y_{ss}+y=0$).

**Remark 10.3.1** The Gauss hypergeometric equation $x(1-x)y''+\big(c-(a+b+1)x\big)y'-aby=0$ has three regular singular points $0,1,\infty$. At $x=0$ the indices are $0$ and $1-c$, and the Frobenius solution with $\rho=0$ is the hypergeometric series

$$
F(a,b;c;x)=\sum_{k\ge0}\frac{(a)_k(b)_k}{(c)_k\,k!}x^k,\qquad(a)_k=a(a+1)\cdots(a+k-1).
$$
Many special functions are special cases of it; for example $P_n(x)=F\big(-n,n+1;1;\frac{1-x}{2}\big)$: the Legendre equation has regular singular points at $x=\pm1,\infty$, and the substitution $t=\frac{1-x}{2}$ turns it into the hypergeometric equation.

## 10.4. The Bessel Equation and Bessel Functions

### 10.4.1. Bessel Functions of the First Kind

**Definition 10.4.1 (Bessel Equation)** The equation

$$
x^2y''+xy'+(x^2-\nu^2)y=0\qquad(\nu\ge0)\tag{10.6}
$$
is called the **Bessel equation** of order $\nu$.

Separating variables $u=R(r)\mathrm{e}^{\mathrm{i}\nu\theta}$ in the Helmholtz equation $\Delta u+k^2u=0$ in polar coordinates and setting $x=kr$, the function $R$ satisfies Eq. (10.6); vibrations of a circular membrane and heat conduction in a cylinder both reduce to it ([2.5](/2.5)).

The point $x=0$ is a regular singular point with $p_0=1$ and $q_0=-\nu^2$; the indicial equation is $\rho^2-\nu^2=0$, so $\rho=\pm\nu$. For $\rho=\nu$, Eq. (10.5) becomes

$$
k(k+2\nu)a_k=-a_{k-2},\qquad a_1=0,
$$
so the odd coefficients vanish and $a_{2m}=\dfrac{(-1)^ma_0}{2^{2m}m!\,(\nu+1)(\nu+2)\cdots(\nu+m)}$. Taking $a_0=\dfrac{1}{2^\nu\Gamma(\nu+1)}$ and simplifying with the property $\Gamma(\nu+m+1)=(\nu+m)\cdots(\nu+1)\Gamma(\nu+1)$ of the **gamma function**, we arrive at the following definition.

**Definition 10.4.2 (Bessel Function of the First Kind)** The function

$$
J_\nu(x)=\sum_{m=0}^\infty\frac{(-1)^m}{m!\,\Gamma(m+\nu+1)}\Big(\frac x2\Big)^{2m+\nu}\tag{10.7}
$$
is called the **Bessel function of the first kind** of order $\nu$. Replacing $\nu$ by $-\nu$ in Eq. (10.7) (with the convention that $1/\Gamma$ vanishes at the nonpositive integers) defines $J_{-\nu}$.

By the ratio test, the series in Eq. (10.7) converges for all $x$. For example,

$$
J_0(x)=1-\frac{x^2}{2^2}+\frac{x^4}{2^2\cdot4^2}-\frac{x^6}{2^2\cdot4^2\cdot6^2}+\cdots,\qquad J_1(x)=\frac x2-\frac{x^3}{2^2\cdot4}+\frac{x^5}{2^2\cdot4^2\cdot6}-\cdots.
$$

**Theorem 10.4.1** 

1. If $\nu\notin\mathbb{Z}$, then $J_\nu$ and $J_{-\nu}$ are two linearly independent solutions of Eq. (10.6), and $W[J_\nu,J_{-\nu}](x)=-\dfrac{2\sin\nu\pi}{\pi x}$;
2. If $\nu=n$ is an integer, then $J_{-n}=(-1)^nJ_n$, and the two are linearly dependent;
3. $J_{1/2}(x)=\sqrt{\dfrac{2}{\pi x}}\sin x$ and $J_{-1/2}(x)=\sqrt{\dfrac{2}{\pi x}}\cos x$.

**Proof** 1: As $x\to0^+$, $J_{\pm\nu}\sim\frac{(x/2)^{\pm\nu}}{\Gamma(1\pm\nu)}$; the two behave differently, so they are linearly independent (here $2\nu$ may be odd, so that the indices differ by an integer, but then $c=0$ and there is no logarithmic term). By Liouville's formula (Theorem 9.1.2, with $p_1=\frac1x$ in the standard form), $W=\frac{C}{x}$, and the constant $C$ is computed from the leading terms using the reflection formula $\Gamma(\nu)\Gamma(1-\nu)=\frac{\pi}{\sin\nu\pi}$. 2: $1/\Gamma(m-n+1)=0$ for $m<n$; start the sum at $m=n$ and set $m=n+j$. 3: Substitute $\Gamma(\frac32)=\frac{\sqrt\pi}2$ and so on, and compare with the series for $\sin x$ and $\cos x$. $\square$

### 10.4.2. Bessel Functions of the Second Kind

For integer order a second solution is needed, and by parts 3 and 4 of Theorem 10.3.1 it contains a logarithmic term. The uniform construction is as follows.

**Definition 10.4.3 (Bessel Function of the Second Kind)** For $\nu\notin\mathbb{Z}$ let

$$
Y_\nu(x)=\frac{J_\nu(x)\cos\nu\pi-J_{-\nu}(x)}{\sin\nu\pi},
$$
and for an integer $n$ let $Y_n(x)=\lim_{\nu\to n}Y_\nu(x)$. The function $Y_\nu$ is called the **Bessel function of the second kind** of order $\nu$ (or Neumann function).

For every $\nu\ge0$, $J_\nu$ and $Y_\nu$ are linearly independent with $W[J_\nu,Y_\nu]=\frac{2}{\pi x}$, and the general solution of the Bessel equation is $y=C_1J_\nu(x)+C_2Y_\nu(x)$. As $x\to0^+$, $Y_\nu$ is unbounded:

$$
Y_0(x)=\frac2\pi\Big(\ln\frac x2+\gamma\Big)J_0(x)+(\text{a power series with zero constant term}),\qquad Y_\nu(x)\sim-\frac{\Gamma(\nu)}{\pi}\Big(\frac2x\Big)^\nu\quad(\nu>0),
$$
where $\gamma$ is the **Euler–Mascheroni constant**. When solving in a region containing the center, we require the solution to be bounded at $r=0$, and only $J_\nu$ is kept.

### 10.4.3. Basic Properties

**Theorem 10.4.2** For $\nu\ge0$ and $x>0$:

1. (Recurrence relations) $\big(x^\nu J_\nu\big)'=x^\nu J_{\nu-1}$ and $\big(x^{-\nu}J_\nu\big)'=-x^{-\nu}J_{\nu+1}$; consequently

$$
J_{\nu-1}+J_{\nu+1}=\frac{2\nu}{x}J_\nu,\qquad J_{\nu-1}-J_{\nu+1}=2J_\nu',\qquad J_0'=-J_1;
$$
$Y_\nu$ satisfies the same recurrence relations.

2. (Asymptotic behavior) As $x\to+\infty$,

$$
J_\nu(x)=\sqrt{\frac{2}{\pi x}}\cos\Big(x-\frac{\nu\pi}{2}-\frac\pi4\Big)+O(x^{-3/2}),\qquad Y_\nu(x)=\sqrt{\frac{2}{\pi x}}\sin\Big(x-\frac{\nu\pi}{2}-\frac\pi4\Big)+O(x^{-3/2}).
$$

3. (Zeros) $J_\nu$ has infinitely many positive zeros $0<j_{\nu,1}<j_{\nu,2}<\cdots$, all of them simple, and $j_{\nu,k+1}-j_{\nu,k}\to\pi$; the positive zeros of $J_\nu$ and $J_{\nu+1}$ interlace.

4. (Orthogonality) If $\alpha$ and $\beta$ are positive zeros of $J_\nu$, then

$$
\int_0^1xJ_\nu(\alpha x)J_\nu(\beta x)\,\mathrm{d}x=\begin{cases}0,&\alpha\ne\beta,\\\dfrac12J_{\nu+1}(\alpha)^2,&\alpha=\beta.\end{cases}
$$

**Proof** 1: By Eq. (10.7), $x^\nu J_\nu=\sum_m\frac{(-1)^mx^{2m+2\nu}}{2^{2m+\nu}m!\,\Gamma(m+\nu+1)}$. Differentiating term by term and using $\frac{2m+2\nu}{\Gamma(m+\nu+1)}=\frac{2}{\Gamma(m+\nu)}$, we get $x^\nu\sum_m\frac{(-1)^m}{m!\,\Gamma(m+\nu)}(\frac x2)^{2m+\nu-1}=x^\nu J_{\nu-1}$. The second identity is proved in the same way. Expanding both identities ($\nu x^{\nu-1}J_\nu+x^\nu J_\nu'=x^\nu J_{\nu-1}$, and so on) and adding and subtracting gives the remaining formulas.

2: (Sketch.) The substitution $u=\sqrt xy$ transforms Eq. (10.6) into

$$
u''+\Big(1-\frac{\nu^2-\frac14}{x^2}\Big)u=0.
$$
For large $x$ this is close to $u''+u=0$, whose solutions are approximately $A\cos(x-\delta)$; the exact amplitude and phase require an integral representation, which we omit. For $\nu=\frac12$ the correction term vanishes and $u$ is exactly $\sin x$ or $\cos x$, in agreement with part 3 of Theorem 10.4.1.

3: The existence of the zeros and the fact that their spacing tends to $\pi$ follow from the above equation for $u$ and the Sturm comparison theorem ([2.4.12](/2.4.12)). Simplicity: if $J_\nu(x_0)=J_\nu'(x_0)=0$ (with $x_0>0$ an ordinary point), then $J_\nu\equiv0$ by uniqueness. Interlacing: by 1, between consecutive zeros of $x^{-\nu}J_\nu$ there is a zero of its derivative $-x^{-\nu}J_{\nu+1}$ (by Rolle's theorem), and between consecutive zeros of $x^{\nu+1}J_{\nu+1}$ there is a zero of $x^{\nu+1}J_\nu$.

4: The function $u(x)=J_\nu(\alpha x)$ satisfies $(xu')'+\big(\alpha^2x-\frac{\nu^2}{x}\big)u=0$, and $v(x)=J_\nu(\beta x)$ satisfies the same equation with $\alpha$ replaced by $\beta$. Multiplying the two equations by $v$ and $u$ respectively and subtracting gives

$$
\big(x(u'v-uv')\big)'=(\beta^2-\alpha^2)xuv.
$$
Integrate over $[0,1]$: at $x=1$ we have $u(1)=v(1)=0$, and at $x=0$, $x(u'v-uv')\to0$ (since $u,v\sim x^\nu$); hence $\int_0^1xuv=0$ for $\alpha\ne\beta$. The value for $\alpha=\beta$ is obtained by letting $\beta\to\alpha$ and applying L'Hôpital's rule, then replacing $J_\nu'(\alpha)$ by $-J_{\nu+1}(\alpha)$ using 1. $\square$

The first few zeros of $J_0$ are $j_{0,1}\approx2.4048$, $j_{0,2}\approx5.5201$ and $j_{0,3}\approx8.6537$; those of $J_1$ are $3.8317$, $7.0156$ and $10.1735$. The natural frequencies of a vibrating circular membrane are proportional to these zeros, and since their spacing is not constant, a drum does not produce overtones at integer multiples of the fundamental as a string does.

By orthogonality, $\{J_\nu(j_{\nu,k}x)\}_{k\ge1}$ is orthogonal on $[0,1]$ with respect to the weight function $x$, and a function on $[0,1]$ can be expanded in a Fourier–Bessel series

$$
f(x)\sim\sum_{k=1}^\infty c_kJ_\nu(j_{\nu,k}x),\qquad c_k=\frac{2}{J_{\nu+1}(j_{\nu,k})^2}\int_0^1xf(x)J_\nu(j_{\nu,k}x)\,\mathrm{d}x,
$$
which converges for piecewise smooth $f$ (stated without proof). This is exactly the expansion needed when solving partial differential equations on a disk by separation of variables.

![Left: Bessel functions of the first kind J_0, J_1, J_2, whose amplitude decays like x^{-1/2}; the dashed curve is the asymptotic form √(2/(πx)) cos(x - π/4) of J_0. Right: Bessel functions of the second kind Y_0, Y_1, which tend to -∞ as x → 0](./plots/bessel-functions.py)

### 10.4.4. Other Representations and Related Equations

1. (Generating function and integral representation) For integer $n$, $\exp\big(\frac x2(t-\frac1t)\big)=\sum_{n\in\mathbb{Z}}J_n(x)t^n$ and $J_n(x)=\frac1\pi\int_0^\pi\cos(n\theta-x\sin\theta)\,\mathrm{d}\theta$ (stated without proof).
2. For $\lambda>0$, the general solution of $x^2y''+xy'+(\lambda^2x^2-\nu^2)y=0$ is $C_1J_\nu(\lambda x)+C_2Y_\nu(\lambda x)$ (set $s=\lambda x$). This is the form that usually appears in separation of variables, and $\lambda$ is determined by the boundary condition $J_\nu(\lambda a)=0$ to be $j_{\nu,k}/a$.
3. The solutions of the modified Bessel equation $x^2y''+xy'-(x^2+\nu^2)y=0$ (obtained by replacing $x$ with $\mathrm{i}x$) are the modified Bessel functions $I_\nu(x)=\mathrm{i}^{-\nu}J_\nu(\mathrm{i}x)=\sum_m\frac{1}{m!\,\Gamma(m+\nu+1)}(\frac x2)^{2m+\nu}$ and $K_\nu$. They do not oscillate: $I_\nu$ grows exponentially and $K_\nu$ decays exponentially. They appear in steady-state heat conduction problems in cylinders.
4. The general solution of the Airy equation $y''+xy=0$ on $x>0$ is $\sqrt x\big(C_1J_{1/3}(\frac23x^{3/2})+C_2J_{-1/3}(\frac23x^{3/2})\big)$ (the solutions of $y''=xy$ in Example 10.1.1 correspond to modified Bessel functions).

## Summary

| Case | Form of the solutions | Key point |
|---|---|---|
| Ordinary point | $\sum a_k(x-x_0)^k$, radius of convergence at least that of the coefficients | Substitute and compare coefficients to get a recurrence; $a_0,a_1$ arbitrary |
| Regular singular point | $x^\rho\sum a_kx^k$ | Indicial equation $\rho(\rho-1)+p_0\rho+q_0=0$ |
| Index difference $\notin\mathbb{Z}$ | Two Frobenius series | — |
| Index difference $=0$ | $y_1\ln x+x^{\rho_1}\sum b_kx^k$ | A logarithmic term is always present |
| Index difference a positive integer $N$ | $cy_1\ln x+x^{\rho_2}\sum b_kx^k$ | Consistency of the recurrence at $k=N$ decides whether $c=0$ |

| Function | Equation | Main properties |
|---|---|---|
| $P_n(x)$ | $(1-x^2)y''-2xy'+n(n+1)y=0$ | Rodrigues' formula; $\int_{-1}^1P_mP_n=\frac{2}{2n+1}\delta_{mn}$; the only solution bounded on $[-1,1]$ (up to a constant factor) |
| $J_\nu(x)$ | $x^2y''+xy'+(x^2-\nu^2)y=0$ | Series (10.7); bounded at $0$; infinitely many zeros; $\int_0^1xJ_\nu(\alpha x)J_\nu(\beta x)=0$ |
| $Y_\nu(x)$ | Same as above | Unbounded at $0$ (logarithmic term for integer order); $W[J_\nu,Y_\nu]=\frac2{\pi x}$ |
