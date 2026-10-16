---
title: Higher-Order Equations and Dependence on Initial Values
source_hash: f978f39ca19e
---

This chapter moves from first-order equations to higher-order equations and systems. We first present several classes of higher-order equations whose order can be reduced, supplementing §15.5 of [2.2.15](/2.2.15). We then show that every higher-order equation or system in normal form is equivalent to a first-order system $\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y})$; once a norm is introduced on $\mathbb{R}^n$, the existence and uniqueness theorems and the extension theorem of [2.4.4](/2.4.4) and [2.4.5](/2.4.5) carry over word for word. Finally we discuss how solutions depend on initial values and parameters: under a Lipschitz condition the solution depends continuously on initial values and parameters (the error grows at most exponentially, as controlled by Grönwall's inequality), and when the right-hand side is smooth the solution is differentiable, its derivatives satisfying the variational equation. This is a prerequisite for a differential equation to describe physical phenomena, and it is the starting point of the stability theory of [2.4.11](/2.4.11). The systematic theory of linear systems and higher-order linear equations is given in [2.4.8](/2.4.8) and [2.4.9](/2.4.9).

## 7.1. Higher-Order Equations Reducible in Order

The idea of reduction of order is to change the unknown function or the independent variable so that an $n$th-order equation becomes an equation of lower order, solve the lower-order equation, and then integrate. [2.2.15](/2.2.15) has already treated the three classes $y^{(n)}=f(x)$, $y''=f(x,y')$ and $y''=f(y,y')$; here we give their general forms and further types.

### 7.1.1. Cauchy's Formula for Repeated Integration

**Proposition 7.1.1 (Cauchy's Formula)** Let $f$ be continuous on an interval $I$ and $x_0\in I$. Then the solution of $y^{(n)}=f(x)$ satisfying $y(x_0)=y'(x_0)=\cdots=y^{(n-1)}(x_0)=0$ is

$$
y(x)=\frac{1}{(n-1)!}\int_{x_0}^x(x-t)^{n-1}f(t)\,\mathrm{d}t, \tag{7.1}
$$
and the general solution is

$$
y(x)=\frac{1}{(n-1)!}\int_{x_0}^x(x-t)^{n-1}f(t)\,\mathrm{d}t+\sum_{k=0}^{n-1}c_k(x-x_0)^k.
$$

**Proof** Denote the right-hand side of (7.1) by $y_n(x)$. By **differentiation under the integral sign** (the upper limit also contains $x$, but for $k<n-1$ the integrand vanishes at $t=x$),

$$
y_n^{(k)}(x)=\frac{1}{(n-1-k)!}\int_{x_0}^x(x-t)^{n-1-k}f(t)\,\mathrm{d}t,\qquad k=0,1,\dots,n-1,
$$
so $y_n^{(k)}(x_0)=0$, $y_n^{(n-1)}(x)=\int_{x_0}^xf(t)\,\mathrm{d}t$, and $y_n^{(n)}=f$. The solutions of the homogeneous equation $y^{(n)}=0$ are the polynomials of degree less than $n$. $\square$

Formula (7.1) turns the $n$-fold integral $\int_{x_0}^x\int_{x_0}^{t_{n-1}}\cdots\int_{x_0}^{t_1}f(t)\,\mathrm{d}t\,\mathrm{d}t_1\cdots\mathrm{d}t_{n-1}$ into a single integral; for $n=2$ it reads $y=\int_{x_0}^x(x-t)f(t)\,\mathrm{d}t+c_1(x-x_0)+c_0$.

### 7.1.2. Equations Not Containing the Unknown Function

The equation $F(x,y^{(k)},y^{(k+1)},\dots,y^{(n)})=0$ does not contain $y,y',\dots,y^{(k-1)}$. Putting $z=y^{(k)}$ turns it into the equation $F(x,z,z',\dots,z^{(n-k)})=0$ of order $n-k$; once $z=\omega(x,c_1,\dots,c_{n-k})$ is found, $k$ integrations by Cauchy's formula give $y$.

In particular, for $y''=f(y')$ the substitution $z=y'$ gives the separable equation $z'=f(z)$, so $x=\displaystyle\int_{z_0}^z\frac{\mathrm{d}t}{f(t)}+c$; we solve for $z$ and integrate once more.

### 7.1.3. Equations Not Containing the Independent Variable; the Energy Integral

The equation $y''=f(y,y')$ does not contain $x$. Taking $y$ as the independent variable and putting $y'=z(y)$, we have $y''=z\dfrac{\mathrm{d}z}{\mathrm{d}y}$, and the equation becomes the first-order equation $z\dfrac{\mathrm{d}z}{\mathrm{d}y}=f(y,z)$. The most important special case is an equation whose right-hand side contains only $y$.

**Proposition 7.1.2 (Energy Integral)** Let $f$ be continuous and $\mathcal{V}(y)=-\displaystyle\int_{y_0}^yf(s)\,\mathrm{d}s$. Then every solution of $y''=f(y)$ satisfies

$$
\frac12(y')^2+\mathcal{V}(y)=E \tag{7.2}
$$
for some constant $E$, and on an interval where $y'\ne0$,

$$
x=\pm\int\frac{\mathrm{d}y}{\sqrt{2\big(E-\mathcal{V}(y)\big)}}+c.
$$

**Proof** Multiply both sides by $y'$: $y''y'=f(y)y'$, that is, $\dfrac{\mathrm{d}}{\mathrm{d}x}\Big(\dfrac12(y')^2\Big)=-\dfrac{\mathrm{d}}{\mathrm{d}x}\mathcal{V}(y)$, and integration gives (7.2). Solving for $y'=\pm\sqrt{2(E-\mathcal{V}(y))}$ and separating variables gives the second formula. $\square$

Physically, $y''=f(y)$ is the equation of motion of a particle of unit mass under a conservative force $f(y)$; $\frac12(y')^2$ is the kinetic energy, $\mathcal{V}$ the potential energy, and (7.2) expresses conservation of energy. Such a quantity $E$ is called a first integral of the equation ([2.4.14](/2.4.14)).

**Example 7.1.1** Solve $y''=2y^3$, $y(0)=1$, $y'(0)=1$. By (7.2), $(y')^2=y^4+c_1$, and the initial values give $c_1=0$; since $y'(0)>0$, we have $y'=y^2$, so $-\dfrac1y=x-1$ and

$$
y=\frac{1}{1-x},\qquad x<1.
$$
The solution blows up as $x\to1^-$, and its maximal interval of existence is $(-\infty,1)$.

**Example 7.1.2 (The Pendulum)** The angle of an undamped pendulum satisfies $\theta''+\omega^2\sin\theta=0$. The energy integral is $\dfrac12(\theta')^2-\omega^2\cos\theta=E$. For $E<\omega^2$, $\theta$ oscillates back and forth in $\lvert\theta\rvert\le\theta_{\max}$ (where $\cos\theta_{\max}=-E/\omega^2$), with period

$$
T=4\int_0^{\theta_{\max}}\frac{\mathrm{d}\theta}{\sqrt{2\omega^2(\cos\theta-\cos\theta_{\max})}},
$$
an elliptic integral; the larger the amplitude, the longer the period. For $E>\omega^2$ the pendulum passes over the top and rotates indefinitely; the borderline case $E=\omega^2$ corresponds to motions that approach the inverted position. In the $(\theta,\theta')$-plane, the level curves of the energy integral are the trajectories of the solutions.

![Energy level curves (theta')^2/2 - cos theta = E of the pendulum theta'' + sin theta = 0: the closed curves are oscillations, the curves above and below are rotations, and the separatrix through (±pi, 0) (E = 1) separates the two](./plots/pendulum-energy.py)

The equation $y''=f(ax+by)$ ($b\ne0$) can also be reduced to this type: with $z=ax+by$ we get $z''=by''=bf(z)$.

### 7.1.4. Equations Containing Only Two Derivatives Whose Orders Differ by One or Two

(1) $F(y^{(n-1)},y^{(n)})=0$. Putting $z=y^{(n-1)}$ gives the first-order equation $F(z,z')=0$. If it can be solved as $z'=f(z)$, it is separable and $\int\frac{\mathrm{d}z}{f(z)}=x+c_1$; otherwise we use the parametric method ([2.4.6](/2.4.6)). Once $z=\omega(x,c_1)$ is found, Cauchy's formula gives

$$
y(x)=\frac{1}{(n-2)!}\int_{x_0}^x(x-t)^{n-2}\omega(t,c_1)\,\mathrm{d}t+\sum_{k=0}^{n-2}c_{k+2}(x-x_0)^k.
$$

(2) $F(y^{(n-2)},y^{(n)})=0$. Putting $z=y^{(n-2)}$ gives $F(z,z'')=0$. If it can be solved as $z''=f(z)$, we are in the case of the energy integral: $(z')^2=2\int f(z)\,\mathrm{d}z+c_1$; separating variables gives $z=\omega(x,c_1,c_2)$, and we then integrate $n-2$ times.

**Example 7.1.3** Solve $a^2y^{(4)}=y''$ ($a>0$). Put $z=y''$, so that $a^2z''=z$. Multiplying by $2z'$ and integrating gives $a^2(z')^2=z^2+c_1$; separating variables, $\dfrac{\mathrm{d}z}{\sqrt{z^2+c_1}}=\pm\dfrac{\mathrm{d}x}{a}$, and integrating and simplifying gives $z=c_2\mathrm{e}^{x/a}+c_3\mathrm{e}^{-x/a}$. Integrating twice more,

$$
y=A\mathrm{e}^{x/a}+B\mathrm{e}^{-x/a}+Cx+D,
$$
with $A,B,C,D$ arbitrary constants. This equation is also linear with constant coefficients, and its **characteristic equation** $a^2\lambda^4=\lambda^2$ (with roots $0,0,\pm1/a$) gives the same general solution directly ([2.2.16](/2.2.16)).

### 7.1.5. Equations Homogeneous in the Unknown Function and Its Derivatives

Suppose $F(x,ty,ty',\dots,ty^{(n)})=t^mF(x,y,y',\dots,y^{(n)})$ for $t\ne0$. Put $y=\mathrm{e}^{\int z\,\mathrm{d}x}$, i.e. $z=y'/y$. Then $y'=yz$, $y''=y(z'+z^2)$, and so on: each $y^{(k)}$ is $y$ times a polynomial in $z,z',\dots,z^{(k-1)}$, and after the factor $y^m$ is removed, the order of the equation drops by one. This substitution turns a second-order homogeneous linear equation into a Riccati equation ([2.4.3](/2.4.3)).

**Example 7.1.4** Solve $x^2yy''=(y-xy')^2$ ($x>0$). The equation is homogeneous of degree two in $y,y',y''$. Put $y'=yz$, $y''=y(z'+z^2)$ and divide by $y^2$:

$$
x^2(z'+z^2)=(1-xz)^2,\qquad\text{i.e.}\qquad x^2z'+2xz=1,\quad(x^2z)'=1.
$$
Hence $z=\dfrac1x+\dfrac{c_1}{x^2}$, $\ln\lvert y\rvert=\ln x-\dfrac{c_1}{x}+c$, and the general solution is $y=c_2x\mathrm{e}^{-c_1/x}$ ($c_2=0$ gives the solution $y=0$).

## 7.2. Reduction to First-Order Systems

Suppose an $n$th-order equation has been solved for the highest derivative:

$$
y^{(n)}=F\big(x,y,y',\dots,y^{(n-1)}\big). \tag{7.3}
$$
Putting $y_1=y$, $y_2=y'$, …, $y_n=y^{(n-1)}$, Eq. (7.3) is equivalent to the system

$$
y_1'=y_2,\quad y_2'=y_3,\quad\dots,\quad y_{n-1}'=y_n,\quad y_n'=F(x,y_1,\dots,y_n): \tag{7.4}
$$
if $y$ is a solution of (7.3), then $(y,y',\dots,y^{(n-1)})$ is a solution of (7.4); conversely, if $(y_1,\dots,y_n)$ is a solution of (7.4), the first $n-1$ equations give $y_k=y_1^{(k-1)}$, and the last equation says that $y_1$ is a solution of (7.3). The initial conditions $y^{(k)}(x_0)=\eta_k$ ($k=0,\dots,n-1$) correspond to $y_{k+1}(x_0)=\eta_k$.

A higher-order system in several unknown functions can be reduced to a first-order system in the same way; the number of new unknown functions equals the sum of the highest orders of the original unknowns.

**Definition 7.2.1** The system

$$
y_i'=f_i(x,y_1,\dots,y_n),\qquad i=1,\dots,n
$$
is called a **system in normal form**, and $n$ is called its order. With the column vectors $\boldsymbol{y}=(y_1,\dots,y_n)^{\mathsf T}$ and $\boldsymbol{f}=(f_1,\dots,f_n)^{\mathsf T}$, it takes the vector form

$$
\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y}), \tag{7.5}
$$
and its initial value problem consists of (7.5) together with $\boldsymbol{y}(x_0)=\boldsymbol{\eta}$, $(x_0,\boldsymbol{\eta})\in\mathbb{R}^{n+1}$.

A solution $\boldsymbol{y}(x)$ of (7.5) takes values in $\mathbb{R}^n$, and its graph is an integral curve in $\mathbb{R}^{n+1}$. Regarding $x$ as time, the curve traced by $\boldsymbol{y}(x)$ in $\mathbb{R}^n$ is called a trajectory, and $\mathbb{R}^n$ is called the phase space. In Example 7.1.2 the pendulum equation becomes $\theta'=\omega_1$, $\omega_1'=-\omega^2\sin\theta$, and the curves in the figure are trajectories in the phase plane.

## 7.3. Existence, Uniqueness and Extension in $\mathbb{R}^n$

The theory of first-order equations used only a few properties of the absolute value. Replacing the absolute value by a norm on $\mathbb{R}^n$, all of the proofs carry over unchanged.

**Definition 7.3.1** A function $\boldsymbol{y}\mapsto\|\boldsymbol{y}\|$ on $\mathbb{R}^n$ is called a **norm** if it satisfies the following three conditions:

1. $\|\boldsymbol{y}\|\ge0$, and $\|\boldsymbol{y}\|=0$ if and only if $\boldsymbol{y}=\boldsymbol{0}$;
2. $\|\lambda\boldsymbol{y}\|=\lvert\lambda\rvert\|\boldsymbol{y}\|$ ($\lambda\in\mathbb{R}$);
3. $\|\boldsymbol{y}+\boldsymbol{z}\|\le\|\boldsymbol{y}\|+\|\boldsymbol{z}\|$ (the triangle inequality).

Commonly used norms are the **Euclidean norm** $\|\boldsymbol{y}\|_2=\sqrt{y_1^2+\cdots+y_n^2}$ (the length of $\boldsymbol{y}$), $\|\boldsymbol{y}\|_1=\lvert y_1\rvert+\cdots+\lvert y_n\rvert$, and $\|\boldsymbol{y}\|_\infty=\max_i\lvert y_i\rvert$, the last being the most convenient for estimates. They are equivalent to one another:

$$
\|\boldsymbol{y}\|_\infty\le\|\boldsymbol{y}\|_2\le\|\boldsymbol{y}\|_1\le n\|\boldsymbol{y}\|_\infty,
$$
so notions such as convergence, boundedness and the Lipschitz condition do not depend on the choice of norm (in fact any two norms on $\mathbb{R}^n$ are equivalent). The integral of a vector-valued function is defined componentwise, and by Riemann sums and the triangle inequality,

$$
\Big\|\int_{x_0}^x\boldsymbol{g}(t)\,\mathrm{d}t\Big\|\le\Big\lvert\int_{x_0}^x\|\boldsymbol{g}(t)\|\,\mathrm{d}t\Big\rvert.
$$

Let $\boldsymbol{f}$ be continuous on $R=\{(x,\boldsymbol{y})\mid\lvert x-x_0\rvert\le a,\ \|\boldsymbol{y}-\boldsymbol{\eta}\|\le b\}$. If $\|\boldsymbol{f}(x,\boldsymbol{y}_1)-\boldsymbol{f}(x,\boldsymbol{y}_2)\|\le L\|\boldsymbol{y}_1-\boldsymbol{y}_2\|$, we say that $\boldsymbol{f}$ satisfies a Lipschitz condition with respect to $\boldsymbol{y}$. If the **Jacobian matrix** $\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}=\Big(\dfrac{\partial f_i}{\partial y_j}\Big)$ is continuous on $R$, then from

$$
\boldsymbol{f}(x,\boldsymbol{y}_1)-\boldsymbol{f}(x,\boldsymbol{y}_2)=\int_0^1\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}\big(x,\boldsymbol{y}_2+s(\boldsymbol{y}_1-\boldsymbol{y}_2)\big)\,\mathrm{d}s\,(\boldsymbol{y}_1-\boldsymbol{y}_2)
$$
(note that $R$ is convex in $\boldsymbol{y}$), the Lipschitz condition holds, and $L$ may be taken to be the maximum of the **matrix norm** of the Jacobian matrix.

**Theorem 7.3.1** Let $\boldsymbol{f}$ be continuous on $R$, $M=\max_R\|\boldsymbol{f}\|$ and $h=\min\{a,b/M\}$.

1. (Peano) The initial value problem $\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y})$, $\boldsymbol{y}(x_0)=\boldsymbol{\eta}$ has at least one solution on $[x_0-h,x_0+h]$.
2. (Picard) If, in addition, $\boldsymbol{f}$ satisfies a Lipschitz condition with respect to $\boldsymbol{y}$, then the solution is unique, and the Picard iterates $\boldsymbol{\varphi}_{n+1}(x)=\boldsymbol{\eta}+\int_{x_0}^x\boldsymbol{f}(t,\boldsymbol{\varphi}_n(t))\,\mathrm{d}t$ converge to it uniformly on $[x_0-h,x_0+h]$.

**Proof** Replace $\lvert\cdot\rvert$ by $\|\cdot\|$ in the proofs of Theorems 4.2.1 and 4.4.1. The only properties used are the triangle inequality, the integral inequality above, the Weierstrass M-test and the Cauchy criterion in $\mathbb{R}^n$ (applied componentwise), and the Arzelà–Ascoli theorem (extracting subsequences one component at a time). $\square$

**Theorem 7.3.2** Let $\boldsymbol{f}$ be continuous in a region $G$ of $\mathbb{R}^{n+1}$.

1. (Extension) Every solution of (7.5) can be extended to a noncontinuable solution whose maximal interval of existence is an open interval $(\alpha,\beta)$; as $x\to\beta^-$, the point $(x,\boldsymbol{y}(x))$ eventually leaves every bounded closed subset of $G$, and likewise as $x\to\alpha^+$. If, in addition, $\boldsymbol{f}$ satisfies a local Lipschitz condition with respect to $\boldsymbol{y}$, the noncontinuable solution is uniquely determined by its initial value.
2. (Global existence) If $G=(\alpha,\beta)\times\mathbb{R}^n$ and $\|\boldsymbol{f}(x,\boldsymbol{y})\|\le A(x)\|\boldsymbol{y}\|+B(x)$ with $A,B\ge0$ continuous on $(\alpha,\beta)$, then the maximal interval of existence of every noncontinuable solution is $(\alpha,\beta)$.

**Proof** The same as the proofs of Theorem 5.1.1, Corollary 5.1.2 and Theorem 5.1.2. $\square$

In particular, a linear system $\boldsymbol{y}'=A(x)\boldsymbol{y}+\boldsymbol{b}(x)$ (with $A,\boldsymbol{b}$ continuous on $(\alpha,\beta)$) satisfies $\|\boldsymbol{f}\|\le\|A(x)\|\|\boldsymbol{y}\|+\|\boldsymbol{b}(x)\|$, so its solutions exist and are unique on the whole of $(\alpha,\beta)$. This is the starting point of [2.4.8](/2.4.8).

**Corollary 7.3.1** Let $F(x,u_1,\dots,u_n)$ be continuous in a region $G$ of $\mathbb{R}^{n+1}$ with continuous partial derivatives with respect to $u_1,\dots,u_n$. Then for any $(x_0,\eta_0,\dots,\eta_{n-1})\in G$, the solution of the $n$th-order equation (7.3) satisfying $y^{(k)}(x_0)=\eta_k$ ($k=0,\dots,n-1$) exists and is unique near $x_0$, and it can be extended to the boundary of $G$.

**Proof** Apply Theorems 7.3.1 and 7.3.2 to the equivalent system (7.4): the Jacobian matrix of its right-hand side $(y_2,\dots,y_n,F)^{\mathsf T}$ is continuous. $\square$

## 7.4. Dependence of Solutions on Initial Values and Parameters

Initial values and the parameters in an equation usually come from measurements and are only approximate. If a small change in the initial value could cause a huge change in the solution, the equation would have no predictive power. In this section we prove that, under a Lipschitz condition, solutions depend continuously on initial values and parameters on finite intervals, and that solutions are moreover differentiable when the right-hand side is smooth.

Denote the solution of (7.5) satisfying $\boldsymbol{y}(x_0)=\boldsymbol{\eta}$ by $\boldsymbol{y}=\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta})$. When the equation contains a parameter $\boldsymbol{\lambda}\in\Lambda\subset\mathbb{R}^m$, we write it as $\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y},\boldsymbol{\lambda})$ and denote the solution by $\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$.

### 7.4.1. Grönwall's Inequality

**Lemma 7.4.1 (Grönwall's Inequality)** Let $u(x)$ and $L(x)$ be continuous and nonnegative on $[x_0,x_1]$, and let $K\ge0$ be a constant. If

$$
u(x)\le K+\int_{x_0}^xL(t)u(t)\,\mathrm{d}t,\qquad x_0\le x\le x_1,
$$
then

$$
u(x)\le K\exp\Big(\int_{x_0}^xL(t)\,\mathrm{d}t\Big),\qquad x_0\le x\le x_1.
$$

**Proof** Let $v(x)=K+\int_{x_0}^xL(t)u(t)\,\mathrm{d}t$. Then $u\le v$ and $v'=Lu\le Lv$. With $\Lambda(x)=\int_{x_0}^xL$, we have $\big(v\mathrm{e}^{-\Lambda}\big)'=(v'-Lv)\mathrm{e}^{-\Lambda}\le0$, so $v(x)\mathrm{e}^{-\Lambda(x)}\le v(x_0)=K$ and $u\le v\le K\mathrm{e}^{\Lambda}$. $\square$

For $x<x_0$ there is a symmetric form: $u(x)\le K+\Big\lvert\int_{x_0}^xLu\,\mathrm{d}t\Big\rvert$ implies $u(x)\le K\exp\Big\lvert\int_{x_0}^xL\,\mathrm{d}t\Big\rvert$. Taking $K=0$ gives $u\equiv0$; applied to the norm of the difference of two solutions, this is yet another proof of uniqueness under a Lipschitz condition. It is exactly the argument used in the proof of Theorem 5.1.2.

**Theorem 7.4.1 (Error Estimate for Solutions)** Let $\boldsymbol{f},\boldsymbol{g}$ be continuous in a region $G\subset\mathbb{R}^{n+1}$, let $\boldsymbol{f}$ satisfy a Lipschitz condition with respect to $\boldsymbol{y}$ (with constant $L$), and let $\|\boldsymbol{f}-\boldsymbol{g}\|\le\varepsilon$ in $G$. Suppose $\boldsymbol{\varphi}$ and $\boldsymbol{\psi}$ are solutions on an interval $J\ni x_0$ of $\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y})$ and $\boldsymbol{y}'=\boldsymbol{g}(x,\boldsymbol{y})$ respectively, with $\boldsymbol{\varphi}(x_0)=\boldsymbol{\eta}$ and $\boldsymbol{\psi}(x_0)=\boldsymbol{\zeta}$. Then for $x\in J$,

$$
\|\boldsymbol{\varphi}(x)-\boldsymbol{\psi}(x)\|\le\big(\|\boldsymbol{\eta}-\boldsymbol{\zeta}\|+\varepsilon\lvert x-x_0\rvert\big)\mathrm{e}^{L\lvert x-x_0\rvert}.
$$

**Proof** Let $x>x_0$. From the integral equations,

$$
\boldsymbol{\varphi}(s)-\boldsymbol{\psi}(s)=\boldsymbol{\eta}-\boldsymbol{\zeta}+\int_{x_0}^s\Big(\big(\boldsymbol{f}(t,\boldsymbol{\varphi})-\boldsymbol{f}(t,\boldsymbol{\psi})\big)+\big(\boldsymbol{f}(t,\boldsymbol{\psi})-\boldsymbol{g}(t,\boldsymbol{\psi})\big)\Big)\,\mathrm{d}t,
$$
so $u(s)=\|\boldsymbol{\varphi}(s)-\boldsymbol{\psi}(s)\|$ satisfies $u(s)\le\|\boldsymbol{\eta}-\boldsymbol{\zeta}\|+\varepsilon(x-x_0)+\int_{x_0}^sLu\,\mathrm{d}t$ on $[x_0,x]$. Grönwall's inequality (with the constant $K=\|\boldsymbol{\eta}-\boldsymbol{\zeta}\|+\varepsilon(x-x_0)$), evaluated at $s=x$, gives the result. The case $x<x_0$ is similar. $\square$

The factor $\mathrm{e}^{L\lvert x-x_0\rvert}$ in the estimate shows that errors in the initial value are controlled on a finite interval but may grow exponentially with the length of the interval. In chaotic systems such exponential growth really occurs, which makes long-term prediction impossible; this does not contradict continuous dependence on finite intervals.

![The difference (log scale) between the solutions of y' = y - y^3 starting from y(0) = 0.01 and y(0) = 0.011: near the unstable equilibrium y = 0 the difference grows like e^x, always staying below the Grönwall bound 0.001 e^{2x} (L = max |1 - 3y^2| = 2), and it decays again once both solutions approach y = 1](./plots/initial-value-sensitivity.py)

### 7.4.2. Continuous Dependence

**Theorem 7.4.2 (Continuous Dependence on Initial Conditions and Parameters)** Let $\boldsymbol{f}(x,\boldsymbol{y},\boldsymbol{\lambda})$ be continuous on $G\times\Lambda$ (where $G\subset\mathbb{R}^{n+1}$ is a region and $\Lambda\subset\mathbb{R}^m$ is open) and satisfy a local Lipschitz condition with respect to $\boldsymbol{y}$. Suppose $\boldsymbol{\varphi}(x;x_0^*,\boldsymbol{\eta}^*,\boldsymbol{\lambda}^*)$ exists on a bounded closed interval $[a,b]\ni x_0^*$. Then there is $\delta>0$ such that, whenever

$$
\lvert x_0-x_0^*\rvert+\|\boldsymbol{\eta}-\boldsymbol{\eta}^*\|+\|\boldsymbol{\lambda}-\boldsymbol{\lambda}^*\|<\delta,
$$
the noncontinuable solution $\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$ exists on $[a,b]$, and $\boldsymbol{\varphi}$ is continuous as a function of $(x,x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$ on this set.

Sketch of proof: take a tubular neighborhood $K=\{(x,\boldsymbol{y})\mid a\le x\le b,\ \|\boldsymbol{y}-\boldsymbol{\varphi}^*(x)\|\le d\}\subset G$ of the graph of $\boldsymbol{\varphi}^*=\boldsymbol{\varphi}(x;x_0^*,\boldsymbol{\eta}^*,\boldsymbol{\lambda}^*)$. It is a bounded closed set; on $K\times\bar B(\boldsymbol{\lambda}^*,r)$ the function $\boldsymbol{f}$ is bounded (by $M$), satisfies a Lipschitz condition with respect to $\boldsymbol{y}$ (with constant $L$, obtained from the local Lipschitz condition by compactness), and is uniformly continuous in $\boldsymbol{\lambda}$, so that $\|\boldsymbol{f}(\cdot,\cdot,\boldsymbol{\lambda})-\boldsymbol{f}(\cdot,\cdot,\boldsymbol{\lambda}^*)\|\le\varepsilon$ on $K$ when $\|\boldsymbol{\lambda}-\boldsymbol{\lambda}^*\|$ is small. The value of the new solution at $x_0^*$ differs from $\boldsymbol{\eta}^*$ by at most $\|\boldsymbol{\eta}-\boldsymbol{\eta}^*\|+M\lvert x_0-x_0^*\rvert$. By Theorem 7.4.1, as long as it stays in $K$,

$$
\|\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})-\boldsymbol{\varphi}^*(x)\|\le\big(\|\boldsymbol{\eta}-\boldsymbol{\eta}^*\|+M\lvert x_0-x_0^*\rvert+\varepsilon(b-a)\big)\mathrm{e}^{L(b-a)}.
$$
For $\delta$ small enough the right-hand side is less than $d/2$; by the extension theorem, the new solution cannot leave $K$ before reaching $x=b$ (or $x=a$), so it exists on all of $[a,b]$, and the inequality shows that it is uniformly close to $\boldsymbol{\varphi}^*$. Joint continuity in $(x,x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$ then follows by adding $\|\boldsymbol{\varphi}(x)-\boldsymbol{\varphi}(x')\|\le M\lvert x-x'\rvert$.

Without the Lipschitz condition (and hence without uniqueness), "the solution" is no longer a function of the initial value, and the result must be reformulated as continuity of the solution set; we do not discuss this here.

### 7.4.3. Differentiability and the Variational Equation

**Theorem 7.4.3 (Differentiability with Respect to Initial Values and Parameters)** Suppose $\boldsymbol{f}(x,\boldsymbol{y},\boldsymbol{\lambda})$ and its partial derivatives $\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}$, $\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{\lambda}}$ are continuous on $G\times\Lambda$. Then $\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$ is continuously differentiable on its domain, and along the solution $\boldsymbol{\varphi}(x)=\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$, writing $A(x)=\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}\big(x,\boldsymbol{\varphi}(x),\boldsymbol{\lambda}\big)$:

1. the $n\times n$ matrix $Y(x)=\dfrac{\partial\boldsymbol{\varphi}}{\partial\boldsymbol{\eta}}$ is the solution of the initial value problem for the linear system

$$
Y'=A(x)Y,\qquad Y(x_0)=I_n; \tag{7.6}
$$
2. $\dfrac{\partial\boldsymbol{\varphi}}{\partial x_0}=-Y(x)\,\boldsymbol{f}(x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$;
3. the $n\times m$ matrix $Z(x)=\dfrac{\partial\boldsymbol{\varphi}}{\partial\boldsymbol{\lambda}}$ is the solution of $Z'=A(x)Z+\dfrac{\partial\boldsymbol{f}}{\partial\boldsymbol{\lambda}}\big(x,\boldsymbol{\varphi}(x),\boldsymbol{\lambda}\big)$, $Z(x_0)=O$.

**Definition 7.4.1** The linear system (7.6) is called the **variational equation** of Eq. (7.5) along the solution $\boldsymbol{\varphi}$.

The variational equation is the linearization of the equation about a known solution: if $\boldsymbol{\varphi}+\boldsymbol{\xi}$ is a nearby solution, then $\boldsymbol{\xi}'=\boldsymbol{f}(x,\boldsymbol{\varphi}+\boldsymbol{\xi})-\boldsymbol{f}(x,\boldsymbol{\varphi})=A(x)\boldsymbol{\xi}+o(\|\boldsymbol{\xi}\|)$, and dropping the higher-order term gives $\boldsymbol{\xi}'=A(x)\boldsymbol{\xi}$. The matrix $Y(x)$ is a **fundamental matrix** of this system, and $\boldsymbol{\xi}(x)\approx Y(x)\,\delta\boldsymbol{\eta}$ gives the first-order effect of a perturbation $\delta\boldsymbol{\eta}$ of the initial value.

Sketch of proof: formally, differentiating the integral equation $\boldsymbol{\varphi}(x)=\boldsymbol{\eta}+\int_{x_0}^x\boldsymbol{f}(t,\boldsymbol{\varphi}(t),\boldsymbol{\lambda})\,\mathrm{d}t$ with respect to $\boldsymbol{\eta}$ gives $Y=I_n+\int_{x_0}^xA(t)Y\,\mathrm{d}t$, which is (7.6). Differentiating with respect to $x_0$ gives $\dfrac{\partial\boldsymbol{\varphi}}{\partial x_0}=-\boldsymbol{f}(x_0,\boldsymbol{\eta},\boldsymbol{\lambda})+\int_{x_0}^xA\dfrac{\partial\boldsymbol{\varphi}}{\partial x_0}\,\mathrm{d}t$; this satisfies the same linear equation with initial value $-\boldsymbol{f}(x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$, and therefore equals $-Y(x)\boldsymbol{f}(x_0,\boldsymbol{\eta},\boldsymbol{\lambda})$. Differentiation with respect to $\boldsymbol{\lambda}$ is similar. Rigorously, consider the difference quotient $\boldsymbol{q}_h(x)=\dfrac1h\big(\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta}+h\boldsymbol{e}_j,\boldsymbol{\lambda})-\boldsymbol{\varphi}(x;x_0,\boldsymbol{\eta},\boldsymbol{\lambda})\big)$. By the integral form of the mean value theorem it satisfies the linear equation

$$
\boldsymbol{q}_h'=A_h(x)\boldsymbol{q}_h,\qquad\boldsymbol{q}_h(x_0)=\boldsymbol{e}_j,\qquad A_h(x)=\int_0^1\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}\big(x,\boldsymbol{\varphi}+s(\boldsymbol{\varphi}_h-\boldsymbol{\varphi}),\boldsymbol{\lambda}\big)\,\mathrm{d}s.
$$
By continuous dependence (Theorem 7.4.2), $A_h\to A$ uniformly as $h\to0$; applying Theorem 7.4.1 to this linear equation then shows that $\boldsymbol{q}_h$ converges uniformly to the $j$th column of the solution of (7.6). Continuity of the partial derivatives follows by applying Theorem 7.4.2 to the system formed by the original equation together with the variational equation.

The case with parameters can also be reduced to the case of initial values: regard $\boldsymbol{\lambda}$ as a new unknown function and add the equation $\boldsymbol{\lambda}'=\boldsymbol{0}$ with the initial value $\boldsymbol{\lambda}(x_0)=\boldsymbol{\lambda}$; the parameter then becomes part of the initial value of the enlarged system. If $\boldsymbol{f}$ is of class $C^k$, repeated application of Theorem 7.4.3 to the variational equation shows that $\boldsymbol{\varphi}$ is also of class $C^k$.

**Example 7.4.1** The solution of $y'=y^2$, $y(0)=\eta$ is $\varphi(x;\eta)=\dfrac{\eta}{1-\eta x}$, and direct differentiation gives $\dfrac{\partial\varphi}{\partial\eta}=\dfrac{1}{(1-\eta x)^2}$. Using the variational equation instead: $A(x)=2\varphi(x)=\dfrac{2\eta}{1-\eta x}$, and the solution of $Y'=A(x)Y$, $Y(0)=1$ is

$$
Y(x)=\exp\int_0^x\frac{2\eta}{1-\eta t}\,\mathrm{d}t=\exp\big(-2\ln(1-\eta x)\big)=\frac{1}{(1-\eta x)^2},
$$
in agreement. Moreover, $\dfrac{\partial\varphi}{\partial x_0}$ at $x_0=0$ should be $-Y(x)\eta^2=-\dfrac{\eta^2}{(1-\eta x)^2}$. Indeed, the solution with $y(x_0)=\eta$ is $\dfrac{\eta}{1-\eta(x-x_0)}$, and differentiating with respect to $x_0$ and setting $x_0=0$ gives exactly this.

**Example 7.4.2** For the equation $y'=\lambda y$ with a parameter and $y(0)=\eta$, we have $\varphi=\eta\mathrm{e}^{\lambda x}$. The derivative $Z=\dfrac{\partial\varphi}{\partial\lambda}$ satisfies $Z'=\lambda Z+\varphi=\lambda Z+\eta\mathrm{e}^{\lambda x}$, $Z(0)=0$, whose solution is $Z=\eta x\mathrm{e}^{\lambda x}$, in agreement with direct differentiation. The effect on the solution of a measurement error in the growth rate $\lambda$ is amplified linearly in $x$ (the relative error is $x\,\delta\lambda$).

## Summary

| Topic | Key points |
|---|---|
| Reduction of order | Cauchy's formula (7.1); without $y$, put $z=y^{(k)}$; without $x$, put $y'=z(y)$; energy integral (7.2) for $y''=f(y)$; for homogeneous equations, put $y'=yz$ |
| Systems | An $n$th-order equation is equivalent to a system (7.4) of $n$ first-order equations in normal form |
| Existence, uniqueness, extension | With a norm in place of the absolute value, the Picard, Peano and extension theorems hold verbatim; global existence under linear growth |
| Continuous dependence | Grönwall's inequality: the error is at most $(\Vert\delta\boldsymbol{\eta}\Vert+\varepsilon\lvert x-x_0\rvert)\mathrm{e}^{L\lvert x-x_0\rvert}$ |
| Differentiability | $\partial\boldsymbol{\varphi}/\partial\boldsymbol{\eta}$ satisfies the variational equation $Y'=\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{y}}Y$, $Y(x_0)=I_n$ |
