---
title: Harmonic Functions and the Laplace Equation
---

The **Laplace equation** $\Delta u=0$ and the **Poisson equation** $-\Delta u=f$ ([2.5.1](/2.5.1)) describe equilibria: steady temperatures, electrostatic and gravitational potentials, the velocity potential of an ideal fluid, the shape of a stretched membrane under a load, the stationary states of diffusion. Their solutions, the **harmonic functions** ([2.2.14](/2.2.14#sec-14.5.2)), are the most rigid functions of analysis. A harmonic function equals its own average over every sphere; it is infinitely differentiable; it attains no maximum or minimum inside its domain; it is determined in a region by its boundary values through an explicit integral formula; and in the plane it is the real part of an **analytic function**.

This chapter develops these properties in the order in which they depend on one another. Green's identities and the fundamental solution (§8.1) give a representation of any function in terms of its Laplacian and boundary values. The mean value property and the maximum principle (§8.2) give uniqueness and stability. Green's functions (§8.3), constructed for the half-space and the ball by the method of images, turn the representation into a solution formula, the Poisson integral. In two dimensions complex analysis supplies a much larger supply of explicit solutions through conformal mapping (§8.4, using [2.3.8](/2.3.8)). Finally, Dirichlet's principle (§8.5) characterizes the solution as the minimizer of an energy, connecting the Laplace equation with the **calculus of variations** ([2.4.13](/2.4.13)). Throughout, $\Omega\subset\mathbb{R}^n$ ($n\ge2$) is a bounded region with piecewise smooth boundary $\partial\Omega$ and outward unit normal $\boldsymbol{n}$, and $\omega_n$ denotes the area of the unit sphere in $\mathbb{R}^n$ ($\omega_2=2\pi$, $\omega_3=4\pi$).

## 8.1. Green's Identities and the Fundamental Solution

### 8.1.1. Green's Identities

**Green's first identity** ([2.2.14](/2.2.14#thm-14.5.2)) states that for $u,v\in C^2(\bar\Omega)$

$$
\int_\Omega v\,\Delta u\,\mathrm{d}V=\oint_{\partial\Omega}v\frac{\partial u}{\partial\boldsymbol{n}}\,\mathrm{d}S-\int_\Omega\nabla u\cdot\nabla v\,\mathrm{d}V.\tag{8.1}
$$
(The proof via the **divergence theorem** works in every dimension.) Interchanging $u$ and $v$ and subtracting, the gradient terms cancel.

**Theorem 8.1.1 (Green's Second Identity)** For $u,v\in C^2(\bar\Omega)$,

$$
\int_\Omega\big(u\,\Delta v-v\,\Delta u\big)\,\mathrm{d}V=\oint_{\partial\Omega}\Big(u\frac{\partial v}{\partial\boldsymbol{n}}-v\frac{\partial u}{\partial\boldsymbol{n}}\Big)\mathrm{d}S.\tag{8.2}
$$

The identity is the multidimensional analogue of Lagrange's identity for Sturm–Liouville operators ([2.4.12](/2.4.12#sec-12.5.1)): it says that $\Delta$ is symmetric on functions satisfying homogeneous Dirichlet or Neumann conditions. Two immediate consequences concern the boundary value problems.

**Theorem 8.1.2** Let $u\in C^2(\bar\Omega)$.

1. (Compatibility condition) If $-\Delta u=f$ in $\Omega$ and $\frac{\partial u}{\partial\boldsymbol{n}}=g$ on $\partial\Omega$, then
$$
\int_\Omega f\,\mathrm{d}V+\oint_{\partial\Omega}g\,\mathrm{d}S=0.
$$
2. (Uniqueness) Two solutions of the Dirichlet problem $-\Delta u=f$ in $\Omega$, $u=g$ on $\partial\Omega$ coincide; two solutions of the Neumann problem differ by a constant when $\Omega$ is connected.

**Proof** 1: Take $v\equiv1$ in (8.1). 2: The difference $w$ of two solutions satisfies $\Delta w=0$ and $w=0$ (or $\frac{\partial w}{\partial\boldsymbol{n}}=0$) on $\partial\Omega$. Taking $u=v=w$ in (8.1) gives $\int_\Omega\lvert\nabla w\rvert^2\,\mathrm{d}V=0$, so $w$ is constant; in the Dirichlet case the constant is $0$. $\square$

The compatibility condition has a clear meaning: in a steady state, the heat produced inside ($\int f$) must leave through the boundary ($-\oint g$ is the outward flux). If it fails, the Neumann problem has no solution; the temperature keeps rising or falling. This is the Fredholm alternative of [2.4.12](/2.4.12#sec-12.4.3) in higher dimensions: the homogeneous Neumann problem has the nontrivial solution $1$, and the data must be orthogonal to it.

### 8.1.2. The Fundamental Solution

The Laplace equation is invariant under translations and rotations, so we first look for radial solutions $u=v(r)$, $r=\lvert x\rvert$. In polar or spherical coordinates ([2.5.5](/2.5.5#sec-5.1.1)), $\Delta u=v''+\frac{n-1}rv'=r^{1-n}(r^{n-1}v')'$, so $r^{n-1}v'=$ const, which gives $v=a\ln r+b$ for $n=2$ and $v=ar^{2-n}+b$ for $n\ge3$ (as in [2.2.14](/2.2.14#sec-14.6)).

**Definition 8.1.1 (Fundamental Solution of the Laplace Equation)** The function

$$
\Gamma(x)=\begin{cases}-\dfrac{1}{2\pi}\ln\lvert x\rvert,&n=2,\\[3mm]\dfrac{1}{(n-2)\,\omega_n\lvert x\rvert^{n-2}},&n\ge3,\end{cases}\qquad x\ne0,\tag{8.3}
$$
is called the **fundamental solution** of the Laplace equation. For $n=3$, $\Gamma(x)=\frac1{4\pi\lvert x\rvert}$.

The constants are chosen so that $\nabla\Gamma=-\frac{x}{\omega_n\lvert x\rvert^n}$ has unit flux outward through every sphere centered at $0$: $-\oint_{\lvert x\rvert=r}\frac{\partial\Gamma}{\partial r}\,\mathrm{d}S=\frac{1}{\omega_nr^{n-1}}\cdot\omega_nr^{n-1}=1$. Physically, $\Gamma(x-y)$ is the potential at $x$ of a unit point charge (or point source of heat, in a steady state) located at $y$, in units in which $-\Delta(\text{potential})=$ charge density. Formally, $-\Delta\Gamma=\delta$ (the **Dirac delta function**), and the next theorem makes this precise.

**Theorem 8.1.3 (Green's Representation Formula)** For $u\in C^2(\bar\Omega)$ and $x\in\Omega$,

$$
u(x)=\oint_{\partial\Omega}\Big(\Gamma(y-x)\frac{\partial u}{\partial\boldsymbol{n}}(y)-u(y)\frac{\partial\Gamma(y-x)}{\partial\boldsymbol{n}_y}\Big)\mathrm{d}S_y-\int_\Omega\Gamma(y-x)\,\Delta u(y)\,\mathrm{d}V_y.\tag{8.4}
$$

**Proof** The function $v(y)=\Gamma(y-x)$ is harmonic in $\Omega$ except at $y=x$. Remove a small ball $B_\varepsilon=B(x,\varepsilon)$ and apply (8.2) on $\Omega_\varepsilon=\Omega\setminus\bar B_\varepsilon$, where $\Delta v=0$:

$$
-\int_{\Omega_\varepsilon}v\,\Delta u\,\mathrm{d}V=\oint_{\partial\Omega}\Big(u\frac{\partial v}{\partial\boldsymbol{n}}-v\frac{\partial u}{\partial\boldsymbol{n}}\Big)\mathrm{d}S+\oint_{\partial B_\varepsilon}\Big(u\frac{\partial v}{\partial\boldsymbol{n}}-v\frac{\partial u}{\partial\boldsymbol{n}}\Big)\mathrm{d}S.
$$
On $\partial B_\varepsilon$ the outward normal of $\Omega_\varepsilon$ points toward $x$, so $\frac{\partial v}{\partial\boldsymbol{n}}=-\Gamma'(\varepsilon)=\frac{1}{\omega_n\varepsilon^{n-1}}$, writing $\Gamma$ as a function of $r$. Hence $\oint_{\partial B_\varepsilon}u\frac{\partial v}{\partial\boldsymbol{n}}\,\mathrm{d}S$ is the average of $u$ over $\partial B_\varepsilon$, which tends to $u(x)$. The other term is bounded by $\lvert\Gamma(\varepsilon)\rvert\,\omega_n\varepsilon^{n-1}\max\lvert\nabla u\rvert$, which is of order $\varepsilon\lvert\ln\varepsilon\rvert$ for $n=2$ and $\varepsilon$ for $n\ge3$, and tends to $0$. Since $\Gamma(y-x)$ is integrable near $y=x$, the left side tends to $-\int_\Omega v\Delta u$. Letting $\varepsilon\to0$ and rearranging gives (8.4). $\square$

If $u$ vanishes near $\partial\Omega$, (8.4) reads $u(x)=\int\Gamma(y-x)(-\Delta u)(y)\,\mathrm{d}y$: $\Gamma*(-\Delta u)=u$, which is the precise meaning of $-\Delta\Gamma=\delta$. Correspondingly, for a reasonable $f$ (for instance $f\in C^2$ with compact support) the Newtonian potential $u=\Gamma*f$ solves $-\Delta u=f$ in $\mathbb{R}^n$: the potential of a charge distribution is the superposition of the potentials of its point charges.

**Corollary 8.1.1** Every harmonic function in a region $\Omega$ is infinitely differentiable there.

**Proof** Let $x_0\in\Omega$ and take a ball $\bar B\subset\Omega$ around $x_0$. Apply (8.4) on $B$ with $\Delta u=0$: for $x$ near $x_0$, $u(x)$ is an integral over $\partial B$ of functions $\Gamma(y-x)$, $\frac{\partial\Gamma(y-x)}{\partial\boldsymbol{n}_y}$ that are infinitely differentiable in $x$ (since $y-x$ stays away from $0$), so **differentiation under the integral sign** is allowed to all orders. $\square$

In fact harmonic functions are real analytic (locally given by convergent power series in $x_1,\dots,x_n$), a statement we do not prove. The analogous statement for the heat equation is the smoothing effect of [2.5.7](/2.5.7#sec-7.1.3); for the wave equation it is false.

## 8.2. The Mean Value Property and the Maximum Principle

### 8.2.1. The Mean Value Property

**Theorem 8.2.1 (Mean Value Property)** Let $u$ be harmonic in $\Omega$ and let the closed ball $\bar B(x,r)$ lie in $\Omega$. Then

$$
u(x)=\frac{1}{\omega_nr^{n-1}}\oint_{\partial B(x,r)}u\,\mathrm{d}S=\frac{n}{\omega_nr^n}\int_{B(x,r)}u\,\mathrm{d}V:
$$
the value at the center equals the average over the sphere and the average over the ball.

**Proof** Let $\phi(\rho)=\frac{1}{\omega_n}\oint_{\lvert\boldsymbol{e}\rvert=1}u(x+\rho\boldsymbol{e})\,\mathrm{d}S_{\boldsymbol{e}}$ be the average of $u$ over $\partial B(x,\rho)$, written as an integral over the unit sphere, for $0<\rho\le r$. Differentiating under the integral sign and changing back to $\partial B(x,\rho)$,

$$
\phi'(\rho)=\frac{1}{\omega_n}\oint_{\lvert\boldsymbol{e}\rvert=1}\nabla u(x+\rho\boldsymbol{e})\cdot\boldsymbol{e}\,\mathrm{d}S_{\boldsymbol{e}}=\frac{1}{\omega_n\rho^{n-1}}\oint_{\partial B(x,\rho)}\frac{\partial u}{\partial\boldsymbol{n}}\,\mathrm{d}S=\frac{1}{\omega_n\rho^{n-1}}\int_{B(x,\rho)}\Delta u\,\mathrm{d}V=0,
$$
by the divergence theorem. So $\phi$ is constant, and by continuity $\phi(\rho)\to u(x)$ as $\rho\to0^+$; this proves the first equality. Multiplying $u(x)=\phi(\rho)$ by $\omega_n\rho^{n-1}$ and integrating over $0<\rho<r$ gives $\frac{\omega_nr^n}{n}u(x)=\int_{B(x,r)}u\,\mathrm{d}V$, the second. $\square$

In the plane, the mean value property also follows from **Cauchy's integral formula** ([2.3.4](/2.3.4)): if $u=\operatorname{Re}F$ with $F$ analytic, then $F(z_0)=\frac1{2\pi}\int_0^{2\pi}F(z_0+r\mathrm{e}^{\mathrm{i}\theta})\,\mathrm{d}\theta$, and taking real parts gives the theorem for $n=2$. The converse holds as well (stated without proof): a continuous function that satisfies the mean value property for every ball in $\Omega$ is harmonic. Thus "harmonic" can be defined without derivatives, as "equal to its local averages". This is also the discrete picture: on a square grid of spacing $h$, $\Delta u\approx\frac{1}{h^2}\big(\sum_{\text{4 neighbors}}u-4u\big)$, so the discrete Laplace equation says that each value is the average of its four neighbors, which is the basis of iterative numerical methods.

### 8.2.2. The Maximum Principle

**Theorem 8.2.2 (Strong Maximum Principle)** Let $\Omega$ be connected and $u$ harmonic in $\Omega$. If $u$ attains its maximum over $\Omega$ at an interior point, then $u$ is constant in $\Omega$. The same holds for the minimum.

**Proof** Let $M=\max_\Omega u$ and $S=\{x\in\Omega:u(x)=M\}$, which is nonempty by hypothesis and closed in $\Omega$ by continuity. If $x\in S$ and $\bar B(x,r)\subset\Omega$, then by the mean value property $M=u(x)=\frac{n}{\omega_nr^n}\int_{B(x,r)}u\,\mathrm{d}V$. Since $u\le M$ and $u$ is continuous, the average equals $M$ only if $u\equiv M$ on $B(x,r)$; hence $S$ is open. A connected set has no subsets that are both open and closed other than itself and the empty set, so $S=\Omega$. For the minimum apply this to $-u$. $\square$

**Corollary 8.2.1 (Weak Maximum Principle)** Let $u\in C^2(\Omega)\cap C(\bar\Omega)$ be harmonic in the bounded region $\Omega$. Then

$$
\min_{\partial\Omega}u\le u(x)\le\max_{\partial\Omega}u\qquad\text{for all }x\in\Omega.
$$

**Proof** The continuous function $u$ attains its maximum over the compact set $\bar\Omega$. If it is attained only at interior points, $u$ is constant by Theorem 8.2.2 and the maximum is also attained on $\partial\Omega$, a contradiction. $\square$

The interpretation is the same as for the heat equation ([2.5.7](/2.5.7#sec-7.2)): a steady temperature without sources has no hot or cold spots inside. The proof via the strict inequality given there also works here and yields more: if $\Delta u\ge0$ in $\Omega$ ($u$ is subharmonic), then $\max_{\bar\Omega}u=\max_{\partial\Omega}u$ (apply the argument to $u+\varepsilon\lvert x\rvert^2$, which has $\Delta>0$ and so no interior maximum).

![A harmonic function on the unit disk, u = Re(z^3 + z^2 / 2): its maximum and minimum lie on the boundary circle, and its value at the center is the average of its boundary values](./plots/maximum-principle.py)

**Corollary 8.2.2 (Uniqueness and Stability of the Dirichlet Problem)** Let $u_1,u_2\in C^2(\Omega)\cap C(\bar\Omega)$ solve $-\Delta u_i=f$ in $\Omega$ with $u_i=g_i$ on $\partial\Omega$. Then

$$
\max_{\bar\Omega}\lvert u_1-u_2\rvert\le\max_{\partial\Omega}\lvert g_1-g_2\rvert.
$$
In particular, the Dirichlet problem has at most one solution, and it depends continuously on the boundary data in the maximum norm.

**Proof** Apply Corollary 8.2.1 to the harmonic functions $\pm(u_1-u_2)$. $\square$

Unlike Theorem 8.1.2, this requires no differentiability up to the boundary, only continuity. Together with existence (§8.3 for the ball, and in general by more advanced methods), the Dirichlet problem for the Poisson equation is well-posed.

### 8.2.3. Liouville's Theorem

**Theorem 8.2.3 (Liouville's Theorem for Harmonic Functions)** A harmonic function on all of $\mathbb{R}^n$ that is bounded is constant.

**Proof** Let $\lvert u\rvert\le M$ and $x,y\in\mathbb{R}^n$ with $d=\lvert x-y\rvert$. By the mean value property for balls of radius $R>d$, writing $V_R=\frac{\omega_nR^n}{n}$ for their volume,

$$
\lvert u(x)-u(y)\rvert=\frac1{V_R}\Big\lvert\int_{B(x,R)}u\,\mathrm{d}V-\int_{B(y,R)}u\,\mathrm{d}V\Big\rvert\le\frac{M}{V_R}\big\lvert B(x,R)\,\triangle\,B(y,R)\big\rvert,
$$
where $\triangle$ denotes the symmetric difference. Every point of the symmetric difference lies at distance between $R-d$ and $R+d$ from $x$, so its volume is at most $V_{R+d}-V_{R-d}$, and the right side is at most $M\frac{(R+d)^n-(R-d)^n}{R^n}\to0$ as $R\to\infty$. Hence $u(x)=u(y)$. $\square$

In the plane this implies Liouville's theorem of complex analysis ([2.3.4](/2.3.4)): if $F$ is a bounded entire function, its real and imaginary parts are bounded harmonic functions on $\mathbb{R}^2$, hence constant.

## 8.3. Green's Functions

### 8.3.1. Definition and Properties

The representation formula (8.4) expresses $u$ through $\Delta u$, the boundary values of $u$, and the normal derivative $\frac{\partial u}{\partial\boldsymbol{n}}$. For the Dirichlet problem the last one is not given. We remove it by adding to $\Gamma(y-x)$ a harmonic function chosen so that the sum vanishes on the boundary.

**Definition 8.3.1 (Green's Function of the Dirichlet Problem)** For $x\in\Omega$, let $h^x\in C^2(\Omega)\cap C^1(\bar\Omega)$ be the solution of

$$
\Delta_yh^x(y)=0\ \ (y\in\Omega),\qquad h^x(y)=\Gamma(y-x)\ \ (y\in\partial\Omega).
$$
The function $G(x,y)=\Gamma(y-x)-h^x(y)$, $x,y\in\Omega$, $x\ne y$, is called the **Green's function** of the Dirichlet problem for the Laplace operator in $\Omega$.

For fixed $x$, $G(x,\cdot)$ is harmonic in $\Omega\setminus\{x\}$, vanishes on $\partial\Omega$, and has the singularity of the fundamental solution at $y=x$: it is the potential of a unit point charge at $x$ inside a grounded conducting surface $\partial\Omega$, and $h^x$ is the potential of the charges induced on the conductor. This is the PDE counterpart of the Green's function of a two-point boundary value problem ([2.4.12](/2.4.12#def-12.4.2)), which is the response to a unit point load.

**Theorem 8.3.1** Suppose the Green's function exists and is $C^1$ in $y$ up to $\partial\Omega$, and let $u\in C^2(\bar\Omega)$ solve

$$
-\Delta u=f\ \text{ in }\Omega,\qquad u=g\ \text{ on }\partial\Omega.
$$
Then for $x\in\Omega$

$$
u(x)=\int_\Omega G(x,y)f(y)\,\mathrm{d}V_y-\oint_{\partial\Omega}g(y)\frac{\partial G}{\partial\boldsymbol{n}_y}(x,y)\,\mathrm{d}S_y.\tag{8.5}
$$

**Proof** Apply (8.2) to $u$ and $h^x$, which is harmonic in all of $\Omega$: $-\int_\Omega h^x\Delta u=\oint_{\partial\Omega}\big(u\frac{\partial h^x}{\partial\boldsymbol{n}}-h^x\frac{\partial u}{\partial\boldsymbol{n}}\big)$. Add this identity, written as $0=\oint_{\partial\Omega}\big(u\frac{\partial h^x}{\partial\boldsymbol{n}}-h^x\frac{\partial u}{\partial\boldsymbol{n}}\big)\mathrm{d}S+\int_\Omega h^x\Delta u\,\mathrm{d}V$, to (8.4). Since $h^x=\Gamma(\cdot-x)$ on $\partial\Omega$, the terms with $\frac{\partial u}{\partial\boldsymbol{n}}$ cancel, and what remains is $u(x)=-\oint u\frac{\partial G}{\partial\boldsymbol{n}_y}-\int G\Delta u$, which is (8.5). $\square$

The function $K(x,y)=-\frac{\partial G}{\partial\boldsymbol{n}_y}(x,y)$, $x\in\Omega$, $y\in\partial\Omega$, is called the *Poisson kernel* of $\Omega$; with it, the solution of the Dirichlet problem for the Laplace equation is $u(x)=\oint_{\partial\Omega}K(x,y)g(y)\,\mathrm{d}S_y$. Theorem 8.3.1 assumes that a solution exists; for the half-space and the ball we will verify directly that (8.5) does produce one.

**Theorem 8.3.2** The Green's function has the following properties.

1. (Symmetry) $G(x,y)=G(y,x)$ for $x\ne y$;
2. (Positivity) $G(x,y)>0$ for $x\ne y$, and for $n\ge3$ also $G(x,y)<\Gamma(y-x)$;
3. $K(x,y)\ge0$ and $\displaystyle\oint_{\partial\Omega}K(x,y)\,\mathrm{d}S_y=1$ for every $x\in\Omega$.

**Proof** 1: Fix $x\ne z$ in $\Omega$ and let $v=G(x,\cdot)$, $w=G(z,\cdot)$. Apply (8.2) to $v,w$ on $\Omega$ with small balls $B(x,\varepsilon)$, $B(z,\varepsilon)$ removed. Both functions are harmonic there and vanish on $\partial\Omega$, so the boundary integrals over the two small spheres add up to $0$. Near $x$, $w$ is smooth and $v$ has the singularity of $\Gamma$; the computation in the proof of Theorem 8.1.3 shows that the integral over $\partial B(x,\varepsilon)$ tends to $-w(x)=-G(z,x)$, and likewise the integral over $\partial B(z,\varepsilon)$ tends to $v(z)=G(x,z)$. Hence $G(x,z)=G(z,x)$.

2: $G(x,y)\to+\infty$ as $y\to x$, because $h^x$ is bounded near $x$. Choose $\varepsilon$ so small that $G(x,\cdot)>0$ on $\bar B(x,\varepsilon)$. On $\Omega\setminus\bar B(x,\varepsilon)$, $G(x,\cdot)$ is harmonic, positive on $\partial B(x,\varepsilon)$ and zero on $\partial\Omega$, so by the strong minimum principle it is positive inside. For $n\ge3$, $h^x$ is harmonic with positive boundary values $\Gamma(y-x)$, so $h^x>0$.

3: $G(x,\cdot)\ge0$ in $\Omega$ and $=0$ on $\partial\Omega$, so its outward normal derivative is $\le0$. Formula (8.5) with $u\equiv1$ ($f=0$, $g=1$) gives $\oint K\,\mathrm{d}S=1$. $\square$

Symmetry is the reciprocity principle: the potential at $y$ due to a charge at $x$ equals the potential at $x$ due to the same charge at $y$. Finding $G$ requires solving a Dirichlet problem, so Green's functions are explicitly known only for special regions. The *method of images* finds them for regions with symmetry: we place a fictitious charge outside $\Omega$ whose potential cancels that of the real charge on $\partial\Omega$.

### 8.3.2. The Half-Space

Let $\Omega=\mathbb{R}^n_+=\{x:x_n>0\}$ and let $x^*=(x_1,\dots,x_{n-1},-x_n)$ be the reflection of $x$ in the plane $x_n=0$. For $y$ on that plane, $\lvert y-x\rvert=\lvert y-x^*\rvert$, so

$$
G(x,y)=\Gamma(y-x)-\Gamma(y-x^*)
$$
vanishes on the boundary, and $\Gamma(\cdot-x^*)$ is harmonic in $\Omega$ because $x^*\notin\Omega$. The outward normal is $-\boldsymbol{e}_n$. From $\nabla\Gamma(z)=-\frac{z}{\omega_n\lvert z\rvert^n}$, at $y_n=0$

$$
\frac{\partial G}{\partial y_n}=-\frac{y_n-x_n}{\omega_n\lvert y-x\rvert^n}+\frac{y_n+x_n}{\omega_n\lvert y-x^*\rvert^n}=\frac{2x_n}{\omega_n\lvert y-x\rvert^n},
$$
so the Poisson kernel of the half-space is $K(x,y)=\frac{\partial G}{\partial y_n}=\frac{2x_n}{\omega_n\lvert x-y\rvert^n}$, and

$$
u(x)=\frac{2x_n}{\omega_n}\int_{\mathbb{R}^{n-1}}\frac{g(y)}{\lvert x-y\rvert^n}\,\mathrm{d}y\tag{8.6}
$$
is the bounded harmonic function in the half-space with boundary values $g$ (for bounded continuous $g$; stated without proof). For $n=2$, writing the point as $(x,y)$ with $y>0$ and the boundary point as $(s,0)$, this is $u(x,y)=\frac y\pi\int\frac{g(s)}{(x-s)^2+y^2}\,\mathrm{d}s$, the formula obtained with the Fourier transform in [2.5.6](/2.5.6#sec-6.4.3).

### 8.3.3. The Ball and Poisson's Formula

Let $\Omega=B(0,R)$. For $x\ne0$ let $x^*=\frac{R^2}{\lvert x\rvert^2}x$ be the inverse point of $x$ with respect to the sphere $\lvert y\rvert=R$; it lies on the same ray outside the ball. For $\lvert y\rvert=R$,

$$
\lvert y-x^*\rvert^2=R^2-\frac{2R^2\,x\cdot y}{\lvert x\rvert^2}+\frac{R^4}{\lvert x\rvert^2}=\frac{R^2}{\lvert x\rvert^2}\big(\lvert x\rvert^2-2x\cdot y+R^2\big)=\frac{R^2}{\lvert x\rvert^2}\lvert y-x\rvert^2,
$$
that is, $\lvert y-x\rvert=\frac{\lvert x\rvert}{R}\lvert y-x^*\rvert$: the sphere is a level set of the ratio of the distances to $x$ and $x^*$ (a sphere of Apollonius). Since $\Gamma$ depends only on the distance, the function

$$
G(x,y)=\Gamma(y-x)-\Gamma\Big(\frac{\lvert x\rvert}{R}(y-x^*)\Big)
$$
vanishes for $\lvert y\rvert=R$ and is harmonic in $y\in B(0,R)\setminus\{x\}$: it is the Green's function of the ball (for $x=0$ take $G(0,y)=\Gamma(y)-\Gamma(R\boldsymbol{e})$ with any unit vector $\boldsymbol{e}$). For $n=3$, $G(x,y)=\frac1{4\pi}\big(\frac1{\lvert y-x\rvert}-\frac{R}{\lvert x\rvert\,\lvert y-x^*\rvert}\big)$: the image charge has strength $-R/\lvert x\rvert$.

![Method of images in two dimensions: level curves of the Green's function with the source x (filled) and the image x* (open), which has the opposite sign. Left: the half-plane, image reflected in the boundary line. Right: the unit disk, image at the inverse point x / |x|^2; the boundary circle is a level curve](./plots/method-of-images.py)

Computing the normal derivative on $\lvert y\rvert=R$ with $\boldsymbol{n}=y/R$ and the gradient of $\Gamma$, the two terms combine (using $\lvert y-x^*\rvert=\frac{R}{\lvert x\rvert}\lvert y-x\rvert$ and $x^*\cdot y=\frac{R^2}{\lvert x\rvert^2}x\cdot y$) into

$$
\frac{\partial G}{\partial\boldsymbol{n}_y}=-\frac{(R^2-x\cdot y)-(\lvert x\rvert^2-x\cdot y)}{R\,\omega_n\lvert x-y\rvert^n}=-\frac{R^2-\lvert x\rvert^2}{R\,\omega_n\lvert x-y\rvert^n}.
$$

**Theorem 8.3.3 (Poisson's Integral Formula)** Let $g$ be continuous on the sphere $\lvert y\rvert=R$, and define

$$
u(x)=\frac{R^2-\lvert x\rvert^2}{\omega_nR}\oint_{\lvert y\rvert=R}\frac{g(y)}{\lvert x-y\rvert^n}\,\mathrm{d}S_y\quad(\lvert x\rvert<R),\qquad u(x)=g(x)\quad(\lvert x\rvert=R).\tag{8.7}
$$
Then $u$ is harmonic in the ball and continuous on the closed ball: it is the solution of the Dirichlet problem.

**Proof** (Sketch.) The Poisson kernel $K(x,y)=\frac{R^2-\lvert x\rvert^2}{\omega_nR\lvert x-y\rvert^n}$ is harmonic in $x$ for $\lvert x\rvert<R$ (a direct computation, or: $K=-\frac{\partial G}{\partial\boldsymbol{n}_y}$ and $G$ is harmonic in $x$ by symmetry), so $u$ is harmonic by differentiation under the integral sign. By Theorem 8.3.2, $K>0$ and $\oint K\,\mathrm{d}S_y=1$. Fix $y_0$ on the sphere and $\delta>0$. For $\lvert y-y_0\rvert\ge\delta$ and $\lvert x-y_0\rvert<\delta/2$ we have $\lvert x-y\rvert\ge\delta/2$, so $K(x,y)\le\frac{2^n(R^2-\lvert x\rvert^2)}{\omega_nR\delta^n}\to0$ as $x\to y_0$. Thus $K(x,\cdot)$ concentrates at $y_0$, and the approximate identity argument of [Theorem 7.1.2](/2.5.7#thm-7.1.2) (part 2) shows $u(x)\to g(y_0)$. $\square$

At $x=0$ formula (8.7) is the mean value property. In the plane, with $x=r\mathrm{e}^{\mathrm{i}\theta}$ and $y=R\mathrm{e}^{\mathrm{i}\varphi}$, $\lvert x-y\rvert^2=R^2-2Rr\cos(\theta-\varphi)+r^2$ and $\mathrm{d}S=R\,\mathrm{d}\varphi$, so

$$
u(r,\theta)=\frac1{2\pi}\int_0^{2\pi}\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\varphi)+r^2}\,g(\varphi)\,\mathrm{d}\varphi.\tag{8.8}
$$
Summing the geometric series $\sum_{m\in\mathbb{Z}}(r/R)^{\lvert m\rvert}\mathrm{e}^{\mathrm{i}m(\theta-\varphi)}$ shows that the kernel equals $1+2\sum_{m\ge1}(r/R)^m\cos m(\theta-\varphi)$, so (8.8) is the closed form of the Fourier series solution of the Dirichlet problem in the disk obtained by **separation of variables** in [2.5.4](/2.5.4).

![Left: the Poisson kernel of the unit disk as a function of theta - phi; as r → 1 it concentrates at theta = phi. Right: the harmonic function with boundary values 1 on the upper and 0 on the lower half circle (Example 8.4.1)](./plots/poisson-kernel-disk.py)

The explicit kernel gives quantitative control of positive harmonic functions.

**Theorem 8.3.4 (Harnack's Inequality)** Let $u\ge0$ be harmonic in $B(0,R)$ and continuous on its closure. Then for $\lvert x\rvert=r<R$

$$
\frac{R^{n-2}(R-r)}{(R+r)^{n-1}}\,u(0)\le u(x)\le\frac{R^{n-2}(R+r)}{(R-r)^{n-1}}\,u(0).
$$

**Proof** For $\lvert y\rvert=R$, $R-r\le\lvert x-y\rvert\le R+r$, so $\frac{R^2-r^2}{\omega_nR(R+r)^n}\le K(x,y)\le\frac{R^2-r^2}{\omega_nR(R-r)^n}$. Multiply by $u(y)\ge0$, integrate over the sphere, and use $\oint u\,\mathrm{d}S=\omega_nR^{n-1}u(0)$ (mean value property) and $R^2-r^2=(R-r)(R+r)$. $\square$

For $n=2$ the bounds are $\frac{R-r}{R+r}u(0)\le u(x)\le\frac{R+r}{R-r}u(0)$. Harnack's inequality says that a positive harmonic function cannot be large at one point and tiny at a nearby one; letting $R\to\infty$ gives another proof of Liouville's theorem for positive harmonic functions.

## 8.4. Harmonic Functions in the Plane and Conformal Mapping

In two dimensions harmonic functions and analytic functions are two sides of the same object.

**Theorem 8.4.1** Let $D\subset\mathbb{C}$ be a region and identify $z=x+\mathrm{i}y$ with $(x,y)$.

1. If $F=u+\mathrm{i}v$ is analytic in $D$, then $u$ and $v$ are harmonic in $D$;
2. If $D$ is simply connected and $u$ is harmonic in $D$, then $u=\operatorname{Re}F$ for an analytic function $F$ in $D$, unique up to an additive imaginary constant.

**Proof** 1: Analytic functions are infinitely differentiable ([2.3.4](/2.3.4)), and differentiating the **Cauchy–Riemann equations** $u_x=v_y$, $u_y=-v_x$ gives $u_{xx}+u_{yy}=v_{yx}-v_{xy}=0$, and similarly for $v$. 2: The function $F'$ should be $u_x-\mathrm{i}u_y$. This function satisfies the Cauchy–Riemann equations because $u$ is harmonic and $C^2$, so it is analytic; on a simply connected region it has a primitive $F$ (by Cauchy's integral theorem), and adjusting the constant gives $\operatorname{Re}F=u$. The construction of the harmonic conjugate $v=\operatorname{Im}F$ is carried out in [2.3.2](/2.3.2). $\square$

The key to applications is that harmonicity survives a change of variables by an analytic map.

**Theorem 8.4.2** Let $f$ be analytic in $D$ and map $D$ into a region $D'$, and let $U$ be harmonic in $D'$. Then $u=U\circ f$ is harmonic in $D$, and

$$
\Delta u(z)=\lvert f'(z)\rvert^2\,(\Delta U)(f(z)).
$$

**Proof** Harmonicity is a local property. Near $w_0=f(z_0)$, $U=\operatorname{Re}H$ for an analytic $H$ on a small disk (Theorem 8.4.1, part 2), so near $z_0$, $u=\operatorname{Re}(H\circ f)$ is the real part of an analytic function and is harmonic by part 1. The formula follows from the chain rule and the Cauchy–Riemann equations for $f$, which say that the Jacobian matrix of $f$ is $\lvert f'\rvert$ times a rotation. $\square$

This yields a method for the Dirichlet problem in a plane region $D$: find a **conformal mapping** $w=f(z)$ of $D$ onto a region $D'$ where the problem is easy (the unit disk with formula (8.8), or the upper half-plane with formula (8.6)), transfer the boundary values, solve in $D'$, and compose with $f$. The Riemann mapping theorem ([2.3.8](/2.3.8)) guarantees that every simply connected proper subregion of $\mathbb{C}$ can be mapped conformally onto the disk, and the catalog of explicit maps in [2.3.8](/2.3.8) covers many regions of practical interest.

**Example 8.4.1** Find the harmonic function in the unit disk with boundary values $1$ on the upper half of the circle and $0$ on the lower half.

**Solution** In the upper half-plane, $U(w)=\frac1\pi\operatorname{Arg}w$ is harmonic (it is $\frac1\pi\operatorname{Im}\operatorname{Log}w$), equal to $1$ on the negative real axis and $0$ on the positive real axis. The Möbius transformation $w=f(z)=\mathrm{i}\frac{1+z}{1-z}$ maps the unit disk onto the upper half-plane, with $f(1)=\infty$, $f(\mathrm{i})=-1$ and $f(-1)=0$; hence it maps the upper half circle onto the negative real axis and the lower half circle onto the positive real axis. Therefore

$$
u(z)=\frac1\pi\operatorname{Arg}\Big(\mathrm{i}\frac{1+z}{1-z}\Big)=\frac12+\frac1\pi\arctan\frac{2r\sin\theta}{1-r^2},\qquad z=r\mathrm{e}^{\mathrm{i}\theta},
$$
where the second form follows from $\mathrm{i}\frac{1+z}{1-z}=\frac{-2r\sin\theta+\mathrm{i}(1-r^2)}{\lvert1-z\rvert^2}$, whose imaginary part is positive. At the center $u(0)=\frac12$, the average of the boundary values. The same function is obtained by evaluating Poisson's formula (8.8), with much more effort; its level curves are the circular arcs through $\pm1$, the images of the rays from $0$ in the $w$-plane.

The interplay works in both directions: complex analysis gives explicit harmonic functions, and harmonic functions model physical fields in the plane. For a two-dimensional ideal fluid flow or electrostatic field, a potential $\phi$ and a stream function (or flux function) $\psi$ combine into the complex potential $\phi+\mathrm{i}\psi$, an analytic function; the curves $\phi=\text{const}$ and $\psi=\text{const}$ are orthogonal families of equipotentials and streamlines ([2.3.8](/2.3.8)).

## 8.5. Dirichlet's Principle

The steady state of a membrane or a temperature field minimizes an energy. For the Poisson equation the energy is

$$
E[w]=\int_\Omega\Big(\frac12\lvert\nabla w\rvert^2-fw\Big)\mathrm{d}V,
$$
defined on the class $\mathcal{A}=\{w\in C^2(\bar\Omega):w=g\text{ on }\partial\Omega\}$ of admissible functions.

**Theorem 8.5.1 (Dirichlet's Principle)** A function $u\in\mathcal{A}$ solves $-\Delta u=f$ in $\Omega$ if and only if $E[u]=\min_{w\in\mathcal{A}}E[w]$.

**Proof** Every $w\in\mathcal{A}$ can be written $w=u+v$ with $v\in C^2(\bar\Omega)$ and $v=0$ on $\partial\Omega$. Expanding,

$$
E[u+v]=E[u]+\int_\Omega\big(\nabla u\cdot\nabla v-fv\big)\,\mathrm{d}V+\frac12\int_\Omega\lvert\nabla v\rvert^2\,\mathrm{d}V.
$$
By (8.1) and $v=0$ on $\partial\Omega$, the middle term equals $\int_\Omega(-\Delta u-f)v\,\mathrm{d}V$.

If $-\Delta u=f$, the middle term vanishes and $E[w]=E[u]+\frac12\int\lvert\nabla v\rvert^2\ge E[u]$: $u$ is a minimizer (and the unique one, since equality forces $\nabla v\equiv\boldsymbol{0}$, hence $v\equiv0$).

Conversely, if $u$ minimizes $E$, then for every such $v$ the function $i(\varepsilon)=E[u+\varepsilon v]=E[u]+\varepsilon\int(-\Delta u-f)v+\frac{\varepsilon^2}2\int\lvert\nabla v\rvert^2$ has a minimum at $\varepsilon=0$, so $i'(0)=\int_\Omega(-\Delta u-f)v\,\mathrm{d}V=0$. Since $v$ is an arbitrary $C^2$ function vanishing on $\partial\Omega$, the multidimensional version of the **fundamental lemma of the calculus of variations** gives $-\Delta u-f\equiv0$. $\square$

The equation $-\Delta u=f$ is thus the **Euler–Lagrange equation** of the functional $E$, exactly as in [2.4.13](/2.4.13) but with a function of several variables: a stationary energy gives the equilibrium equation, and the natural boundary condition of a free boundary would be $\frac{\partial u}{\partial\boldsymbol{n}}=0$. Riemann used Dirichlet's principle around 1850 to assert the existence of solutions, taking for granted that the minimum is attained. Weierstrass objected that a functional bounded below need not attain its infimum in a given class, and the gap was only closed around 1900 by Hilbert, whose work led to the modern approach: minimize over a larger space of functions with square-integrable derivatives (a Sobolev space), where a minimizer exists, and then prove that it is smooth. The same variational formulation is the starting point of the finite element method, which minimizes $E$ over piecewise polynomial functions on a mesh.

## Summary

| Topic | Statement |
|---|---|
| Green's identities | $\int(v\Delta u+\nabla u\cdot\nabla v)=\oint v\partial_{\boldsymbol{n}}u$; $\int(u\Delta v-v\Delta u)=\oint(u\partial_{\boldsymbol{n}}v-v\partial_{\boldsymbol{n}}u)$ |
| Neumann problem | Solvable only if $\int_\Omega f+\oint_{\partial\Omega}g=0$; solution unique up to a constant |
| Fundamental solution | $-\frac1{2\pi}\ln\lvert x\rvert$ ($n=2$), $\frac1{4\pi\lvert x\rvert}$ ($n=3$); $-\Delta\Gamma=\delta$ |
| Mean value property | $u(x)$ is the average of $u$ over every sphere and ball centered at $x$ |
| Maximum principle | No interior extremum unless constant; $\min_{\partial\Omega}u\le u\le\max_{\partial\Omega}u$; uniqueness and stability |
| Liouville, Harnack | Bounded harmonic functions on $\mathbb{R}^n$ are constant; $\frac{R-r}{R+r}u(0)\le u(x)\le\frac{R+r}{R-r}u(0)$ in the disk |
| Green's function | $G(x,y)=\Gamma(y-x)-h^x(y)$, zero on $\partial\Omega$, symmetric, positive; $u=\int Gf-\oint g\,\partial_{\boldsymbol{n}_y}G$ |
| Method of images | Half-space: reflect $x$; ball: inverse point $x^*=R^2x/\lvert x\rvert^2$ with strength $(R/\lvert x\rvert)^{n-2}$ |
| Poisson's formula | Ball: $u=\frac{R^2-\lvert x\rvert^2}{\omega_nR}\oint\frac{g}{\lvert x-y\rvert^n}$; disk: kernel $\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\varphi)+r^2}$ |
| Plane | Real parts of analytic functions; invariance under conformal maps |
| Dirichlet's principle | $-\Delta u=f$, $u=g$ $\iff$ $u$ minimizes $\int(\frac12\lvert\nabla w\rvert^2-fw)$ among $w=g$ on $\partial\Omega$ |
