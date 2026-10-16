---
title: Classical Equations and Well-Posed Problems
---

A **partial differential equation** relates an unknown function of several variables to its partial derivatives. Almost every continuum model in physics, chemistry and biology takes this form: the displacement of a string, the temperature in a rod, the concentration of a chemical, the electric potential in a region. This chapter introduces the vocabulary of the subject and the three classical second-order equations that the rest of the course studies: the wave equation, the heat equation and the Laplace equation. We derive each from a conservation law, explain which initial and boundary conditions make up a sensible problem, and state Hadamard's notion of a well-posed problem. Finally we classify second-order linear equations into hyperbolic, parabolic and elliptic types. The classification is not just bookkeeping: each type has its own qualitative behavior (finite propagation speed, smoothing, equilibrium), and its own methods, which the later chapters develop: first-order equations in [2.5.2](/2.5.2), the wave equation in [2.5.3](/2.5.3), separation of variables in [2.5.4](/2.5.4) and [2.5.5](/2.5.5), integral transforms in [2.5.6](/2.5.6), the heat equation in [2.5.7](/2.5.7) and the Laplace equation in [2.5.8](/2.5.8). The tools come from calculus (the **divergence theorem**, [2.2.14](/2.2.14#thm-14.2.1); **Fourier series**, [2.2.9](/2.2.9)) and from ordinary differential equations (characteristics, [2.4.14](/2.4.14); Sturm–Liouville problems, [2.4.12](/2.4.12)).

## 1.1. Basic Concepts

### 1.1.1. Order, Solutions and Linearity

We write $u_x=\frac{\partial u}{\partial x}$, $u_{xy}=\frac{\partial^2u}{\partial y\,\partial x}$, and so on; the time variable is $t$, and $\Omega\subset\mathbb{R}^n$ denotes a region with boundary $\partial\Omega$.

**Definition 1.1.1 (Order and Classical Solution)** A partial differential equation for an unknown function $u(x_1,\dots,x_n)$ is a relation

$$
F\big(x,u,Du,D^2u,\dots,D^mu\big)=0,\qquad x\in\Omega,\tag{1.1}
$$
where $D^ku$ stands for the collection of all partial derivatives of $u$ of order $k$, and $D^mu$ actually occurs. The number $m$ is called the **order** of the equation. A function $u\in C^m(\Omega)$ that satisfies Eq. (1.1) at every point of $\Omega$ is called a **classical solution**.

Later we shall meet solutions that are not differentiable enough to satisfy the equation pointwise (the shock waves of [2.5.2](/2.5.2), the "plucked string" of [2.5.3](/2.5.3)); for now "solution" means classical solution.

**Definition 1.1.2 (Linear and Nonlinear Equations)** Write Eq. (1.1) as $\mathcal{L}u=f$ after moving all terms that do not contain $u$ to the right-hand side.

1. If $\mathcal{L}(\alpha u+\beta v)=\alpha\mathcal{L}u+\beta\mathcal{L}v$ for all functions $u,v$ and constants $\alpha,\beta$, the equation is **linear**; it is **homogeneous** if $f\equiv0$ and nonhomogeneous otherwise.
2. If the equation is linear in the derivatives of the highest order $m$, with coefficients that depend only on $x$, while the lower-order terms may depend nonlinearly on $u$ and its derivatives of order less than $m$, it is a **semilinear equation**.
3. If it is linear in the derivatives of order $m$, with coefficients that may depend on $x$ and on derivatives of $u$ of order less than $m$, it is a **quasilinear equation**.
4. Otherwise the equation is a **fully nonlinear equation**.

Each class contains the previous one. The following table lists equations that appear in this course or in its applications (here $c,k,D>0$ are constants).

| Equation | Name | Order | Type |
|---|---|---|---|
| $u_t+cu_x=0$ | transport equation | 1 | linear, homogeneous |
| $u_t+uu_x=0$ | inviscid Burgers equation | 1 | quasilinear |
| $u_x^2+u_y^2=1$ | eikonal equation | 1 | fully nonlinear |
| $u_{tt}=c^2\Delta u$ | wave equation | 2 | linear, homogeneous |
| $u_t=k\Delta u+f(x,t)$ | heat equation with a source | 2 | linear, nonhomogeneous |
| $\Delta u=0$, $\Delta u=f$ | Laplace and Poisson equations | 2 | linear |
| $u_t=D\Delta u+u(1-u)$ | Fisher–KPP equation | 2 | semilinear |
| $\operatorname{div}\Big(\dfrac{\nabla u}{\sqrt{1+\lvert\nabla u\rvert^2}}\Big)=0$ | minimal surface equation | 2 | quasilinear |
| $u_t+6uu_x+u_{xxx}=0$ | Korteweg–de Vries equation | 3 | semilinear |

The Fisher–KPP equation is the simplest **reaction-diffusion equation**; such equations model spreading populations and chemical patterns ([7.4](/7.4)).

### 1.1.2. The Superposition Principle

For linear homogeneous equations the solution set is a vector space: this is the **superposition principle**, the basis of almost every method for linear equations in this course.

**Theorem 1.1.1 (Superposition Principle)** Let $\mathcal{L}$ be a linear differential operator of order $m$.

1. If $u_1,\dots,u_N$ solve $\mathcal{L}u=0$, so does every linear combination $\sum_{j=1}^Nc_ju_j$; if $u_p$ solves $\mathcal{L}u=f$, every solution of $\mathcal{L}u=f$ has the form $u_p+v$ with $\mathcal{L}v=0$.
2. If $u_1,u_2,\dots$ solve $\mathcal{L}u=0$, the series $u=\sum_{j=1}^\infty c_ju_j$ converges, and the series of all derivatives of order at most $m$ are **uniformly convergent** on compact subsets of $\Omega$, then $u$ also solves $\mathcal{L}u=0$.

**Proof** Part 1 is linearity. In part 2, uniform convergence of the differentiated series allows termwise differentiation ([2.2.9](/2.2.9#thm-9.1.6)), so $\mathcal{L}u=\sum c_j\mathcal{L}u_j=0$. $\square$

Part 2 is what separation of variables needs ([2.5.4](/2.5.4)): there the solution is an infinite series of simple solutions, and the convergence hypothesis must be checked. Without it the conclusion can fail, because a series of smooth functions may converge to a function that is not differentiable.

Unlike an ordinary differential equation, whose general solution contains arbitrary constants, a partial differential equation has a general solution containing arbitrary functions. For example, $u_{xy}=0$ means that $u_x$ does not depend on $y$, so $u_x=f(x)$, and integrating in $x$ gives

$$
u(x,y)=F(x)+G(y)
$$
with $F,G$ arbitrary $C^1$ functions. The solution space of a linear homogeneous partial differential equation is therefore infinite-dimensional, and singling out one solution requires conditions on whole curves or surfaces, not at a single point.

## 1.2. Derivation of the Classical Equations

Each of the three classical equations expresses a balance law: Newton's second law for a small piece of string, conservation of energy for a small piece of a body. The pattern is always the same: write the balance for an arbitrary small region, convert boundary terms into volume integrals, and use the arbitrariness of the region to obtain a pointwise equation.

### 1.2.1. The Vibrating String

Consider a perfectly flexible elastic string stretched along the $x$-axis, vibrating in a plane, and let $u(x,t)$ be its transverse displacement. We assume that the motion is purely transverse, that the slope is small ($\lvert u_x\rvert\ll1$), that the string has constant linear density $\rho$, and that the tension acts along the tangent. Let $\theta$ be the angle between the tangent and the $x$-axis; then $\sin\theta\approx\tan\theta=u_x$ and $\cos\theta\approx1$ up to terms of order $u_x^2$.

Take the piece of string over $[x,x+\Delta x]$. Since there is no horizontal motion, the horizontal components $T\cos\theta$ of the tension at the two ends balance, so to first order the tension $T$ is the same at both ends and constant in $x$; small vibrations do not stretch the string appreciably, so $T$ is also constant in time. The vertical components are $T\sin\theta\approx Tu_x$, so with an external force density $F(x,t)$ per unit length, Newton's second law gives

$$
\rho\,\Delta x\,u_{tt}(\bar x,t)=T\big[u_x(x+\Delta x,t)-u_x(x,t)\big]+F(\hat x,t)\,\Delta x
$$
for some $\bar x,\hat x$ in the interval. Dividing by $\Delta x$ and letting $\Delta x\to0$,

$$
u_{tt}=c^2u_{xx}+f(x,t),\qquad c=\sqrt{T/\rho},\quad f=F/\rho.\tag{1.2}
$$
The constant $c$ has the dimension of a velocity; [2.5.3](/2.5.3) shows that it is the speed at which disturbances travel along the string. The same argument for a stretched membrane gives $u_{tt}=c^2(u_{xx}+u_{yy})$, and the equations of acoustics (small pressure perturbations in a gas) or electromagnetism (each component of the field in a vacuum) give the three-dimensional version.

**Definition 1.2.1 (Wave Equation)** The equation

$$
u_{tt}=c^2\Delta u,\qquad x\in\mathbb{R}^n,\ t\in\mathbb{R},\tag{1.3}
$$
where $\Delta=\partial_{x_1}^2+\cdots+\partial_{x_n}^2$ is the **Laplace operator** in the space variables and $c>0$, is called the **wave equation**; with a right-hand side $f(x,t)$ it is the nonhomogeneous wave equation.

### 1.2.2. Heat Conduction and Diffusion

Let $u(x,t)$ be the temperature at the point $x\in\mathbb{R}^3$ of a body with density $\rho$, specific heat $c_{\mathrm{p}}$ and thermal conductivity $\kappa$, all assumed constant. Two physical laws are needed.

1. The thermal energy in a region $V$ is $\iiint_Vc_{\mathrm{p}}\rho u\,\mathrm{d}V$.
2. *Fourier's law*: heat flows from hot to cold at a rate proportional to the temperature gradient; the heat flux vector is $\boldsymbol{q}=-\kappa\nabla u$.

Let $V$ be any region with piecewise smooth boundary $\partial V$ and outward unit normal $\boldsymbol{n}$, and let $F(x,t)$ be the rate of heat production per unit volume by internal sources. Conservation of energy says that the rate of change of heat in $V$ equals the inward flux through $\partial V$ plus the heat produced inside:

$$
\frac{\mathrm{d}}{\mathrm{d}t}\iiint_Vc_{\mathrm{p}}\rho u\,\mathrm{d}V=-\iint_{\partial V}\boldsymbol{q}\cdot\boldsymbol{n}\,\mathrm{d}S+\iiint_VF\,\mathrm{d}V.
$$
By the divergence theorem the flux term equals $\iiint_V\nabla\cdot(\kappa\nabla u)\,\mathrm{d}V$, and differentiating under the integral sign,

$$
\iiint_V\big(c_{\mathrm{p}}\rho u_t-\kappa\Delta u-F\big)\,\mathrm{d}V=0.
$$
The integrand is continuous and its integral over every region $V$ vanishes, so it vanishes identically (if it were positive at a point, it would be positive on a small ball around that point). Hence

$$
u_t=k\Delta u+f,\qquad k=\frac{\kappa}{c_{\mathrm{p}}\rho},\quad f=\frac{F}{c_{\mathrm{p}}\rho}.\tag{1.4}
$$
The constant $k$ is the thermal diffusivity. Exactly the same derivation applies to the concentration $u$ of a substance diffusing in a medium: *Fick's law* $\boldsymbol{q}=-D\nabla u$ replaces Fourier's law, and $D$ is the diffusion coefficient. If the conductivity varies in space, the derivation gives $c_{\mathrm{p}}\rho u_t=\nabla\cdot(\kappa(x)\nabla u)+F$ instead.

**Definition 1.2.2 (Heat Equation)** The equation

$$
u_t=k\Delta u,\qquad k>0,\tag{1.5}
$$
is called the **heat equation** (also the diffusion equation); with a right-hand side $f(x,t)$ it is the nonhomogeneous heat equation.

The wave equation is second order in time, the heat equation first order. This difference has deep consequences: the wave equation is reversible in time (if $u(x,t)$ is a solution, so is $u(x,-t)$), whereas the heat equation describes an irreversible process that smooths out irregularities and can only be solved forward in time (§1.4).

### 1.2.3. Steady States: the Laplace and Poisson Equations

If the sources and the boundary temperatures do not depend on time, the temperature tends to a steady state with $u_t=0$, which by Eq. (1.4) satisfies $k\Delta u+f=0$. The same equations arise for steady vibrations of a membrane under a time-independent load, for the electrostatic potential ($\Delta\varphi=-\rho_{\mathrm{e}}/\varepsilon_0$, with charge density $\rho_{\mathrm{e}}$), for the gravitational potential, and for the velocity potential of an incompressible irrotational flow (the velocity $\boldsymbol{v}=\nabla\varphi$ satisfies $\nabla\cdot\boldsymbol{v}=0$, so $\Delta\varphi=0$).

**Definition 1.2.3 (Laplace and Poisson Equations)** The equation

$$
\Delta u=0\tag{1.6}
$$
is called the **Laplace equation**, and its $C^2$ solutions are the **harmonic functions** ([2.2.14](/2.2.14#sec-14.5.2)). The nonhomogeneous equation $\Delta u=f$ is called the **Poisson equation**.

Physicists often write the Poisson equation as $-\Delta u=f$, so that a positive source produces a positive solution; the sign is a matter of convention. In two variables, harmonic functions are exactly the real parts of analytic functions, which links this equation with complex analysis ([2.3](/2.3), [2.5.8](/2.5.8)).

The three equations in one picture: the wave equation describes oscillation and propagation, the heat equation describes relaxation toward equilibrium, and the Laplace equation describes the equilibrium itself.

## 1.3. Initial and Boundary Conditions

### 1.3.1. Initial Conditions

A partial differential equation alone has infinitely many solutions; additional conditions single out the one that describes a particular physical situation. Conditions at the initial time $t=0$ are called initial conditions. Since the heat equation is first order in $t$, it needs one initial condition, the initial temperature

$$
u(x,0)=\varphi(x).
$$
The wave equation is second order in $t$ and, like Newton's equation for a particle, needs the initial position and the initial velocity:

$$
u(x,0)=\varphi(x),\qquad u_t(x,0)=\psi(x).
$$
The Laplace equation describes a state that does not evolve and has no initial conditions.

### 1.3.2. Boundary Conditions

If the body occupies a bounded region $\Omega$, conditions are also needed on the boundary $\partial\Omega$. Let $\boldsymbol{n}$ be the outward unit normal and $\frac{\partial u}{\partial\boldsymbol{n}}=\nabla u\cdot\boldsymbol{n}$ the normal derivative.

**Definition 1.3.1 (Boundary Conditions)** Let $g$ be a given function on $\partial\Omega$ (for evolution equations, also depending on $t$).

1. $u=g$ on $\partial\Omega$ is a **Dirichlet boundary condition** (boundary condition of the first kind);
2. $\dfrac{\partial u}{\partial\boldsymbol{n}}=g$ on $\partial\Omega$ is a **Neumann boundary condition** (of the second kind);
3. $\dfrac{\partial u}{\partial\boldsymbol{n}}+\alpha u=g$ on $\partial\Omega$, with a function $\alpha>0$, is a **Robin boundary condition** (of the third kind).

A boundary condition is called homogeneous if $g\equiv0$.

These are the multidimensional forms of the boundary conditions for ordinary differential equations in [2.4.12](/2.4.12#sec-12.4.1). Their physical meanings:

| Condition | Heat conduction | Vibrating string ($x=l$ an endpoint) |
|---|---|---|
| Dirichlet | the boundary temperature is prescribed (a heat bath) | the end moves in a prescribed way; $u(l,t)=0$ is a fixed end |
| Neumann | the heat flux $-\kappa\frac{\partial u}{\partial\boldsymbol{n}}$ is prescribed; $g=0$ is an insulated boundary | the end slides freely on a vertical rail: $u_x(l,t)=0$ (no vertical force) |
| Robin | Newton's law of cooling: $-\kappa\frac{\partial u}{\partial\boldsymbol{n}}=H(u-u_{\mathrm{env}})$, heat exchange with surroundings at temperature $u_{\mathrm{env}}$ | the end is attached to a spring of stiffness $K$: $Tu_x(l,t)=-Ku(l,t)$ |

The sign $\alpha>0$ in the Robin condition is the physical one: heat leaves the body when it is hotter than its surroundings. Mixed conditions (different kinds on different parts of $\partial\Omega$) are also common. For problems on an unbounded region one imposes instead growth or decay conditions at infinity, such as boundedness of $u$.

### 1.3.3. Types of Problems

An equation together with its initial and boundary conditions is called a problem for the equation (in Chinese textbooks, a "problem with definite conditions"). There are three kinds:

- an **initial value problem** (Cauchy problem): the equation on all of space, with initial conditions only;
- a **boundary value problem**: the equation in $\Omega$ with boundary conditions only (typical for the Laplace equation); with a Dirichlet condition it is the Dirichlet problem, with a Neumann condition the Neumann problem;
- an initial-boundary value problem, with both.

**Definition 1.3.2 (Initial-Boundary Value Problem)** A problem for an evolution equation on $\Omega\times(0,T)$ with initial conditions at $t=0$ and boundary conditions on $\partial\Omega\times(0,T)$ is called an **initial-boundary value problem** (a mixed problem).

For example, heat conduction in a rod of length $l$ whose left end is kept at temperature $0$ and whose right end is insulated is the initial-boundary value problem

$$
\begin{cases}u_t=ku_{xx},&0<x<l,\ t>0,\\u(0,t)=0,\quad u_x(l,t)=0,&t>0,\\u(x,0)=\varphi(x),&0\le x\le l.\end{cases}\tag{1.7}
$$
A classical solution of such a problem is required to be $C^2$ in $x$ and $C^1$ in $t$ inside the region and continuous up to the boundary (with $u_x$ continuous up to the boundary where a Neumann or Robin condition is imposed), so that the conditions make sense. Continuity at the corners $(0,0)$ and $(l,0)$ forces compatibility conditions on the data: in (1.7) we need $\varphi(0)=0$. When the data are incompatible (an initially warm rod plunged into ice water), the solution is discontinuous at the corner; the formulas of [2.5.4](/2.5.4) still make sense, and the solution is classical for $t>0$.

## 1.4. Well-Posedness

Problems for partial differential equations come from models whose data are measured, hence known only approximately. A useful problem should therefore have a solution, only one, and the solution should not change much when the data change a little.

**Definition 1.4.1 (Well-Posed Problem)** A problem for a partial differential equation is called **well-posed** (in the sense of Hadamard) if

1. (existence) it has a solution for every admissible data;
2. (uniqueness) the solution is unique;
3. (stability) the solution depends continuously on the data: small changes of the data, measured in a suitable norm, cause small changes of the solution.

A problem that is not well-posed is called ill-posed.

Condition 3 is the analogue of **continuous dependence** for ordinary differential equations ([2.4.7](/2.4.7)). The norms are part of the definition: for the wave equation, for example, one measures data and solutions by their maximum or their energy. The classical problems of this course are well-posed: the initial value problem for the wave equation ([2.5.3](/2.5.3)), the initial and initial-boundary value problems for the heat equation ([2.5.7](/2.5.7)) and the Dirichlet problem for the Laplace equation ([2.5.8](/2.5.8)). The point of the definition is that well-posedness depends on matching the type of conditions to the type of equation, as the following classical example shows.

**Example 1.4.1 (Hadamard's Example)** Consider the initial value problem for the Laplace equation in the half-plane $y>0$:

$$
u_{xx}+u_{yy}=0,\qquad u(x,0)=0,\qquad u_y(x,0)=\frac{\sin nx}{n},
$$
where $n$ is a positive integer. Its solution (unique, by Holmgren's uniqueness theorem) is

$$
u_n(x,y)=\frac{1}{n^2}\sinh ny\,\sin nx,
$$
as one checks directly. As $n\to\infty$, the data tend to $0$ uniformly: $\sup_x\lvert u_y(x,0)\rvert=\frac1n\to0$. For the zero data the solution is $u\equiv0$. But for every fixed $y>0$,

$$
\sup_x\lvert u_n(x,y)\rvert=\frac{\sinh ny}{n^2}\to+\infty.
$$
Arbitrarily small data produce arbitrarily large solutions at any positive height: the problem is not stable, hence ill-posed.

![Hadamard's example: the Cauchy data sin(nx)/n shrink to zero (left), while the amplitude sinh(ny)/n² of the solution at heights y = 0.5, 1, 2 grows exponentially with n (right)](./plots/hadamard-example.py)

The same initial data are perfectly reasonable for the wave equation $u_{yy}=u_{xx}$ (with $y$ as time): the solution is $\frac1{n^2}\sin ny\sin nx$, which stays small. The Laplace equation describes equilibrium, which is determined by boundary values on a closed curve, not by "position and velocity" on a line. A second example of the same phenomenon is the heat equation run backward in time.

**Example 1.4.2 (The Backward Heat Equation)** On $0<x<\pi$ with $u(0,t)=u(\pi,t)=0$, the function $u_n=\mathrm{e}^{-n^2t}\sin nx$ solves $u_t=u_{xx}$. Suppose we want to recover the initial temperature from the temperature at time $T>0$. Final data $u(x,T)=\varepsilon\sin nx$ lead to the initial state $u(x,0)=\varepsilon\mathrm{e}^{n^2T}\sin nx$: a change of size $\varepsilon$ in the final data changes the initial state by $\varepsilon\mathrm{e}^{n^2T}$, which is unbounded in $n$. Heat conduction destroys information about fine details (high frequencies) exponentially fast, so reconstructing the past from the present is unstable.

Ill-posed problems are not meaningless: deblurring an image, computed tomography and other inverse problems are of this kind. They require extra a priori information about the solution (regularization), which is a subject of its own.

## 1.5. Classification of Second-Order Linear Equations

### 1.5.1. Two Independent Variables

The general second-order linear equation in two variables is

$$
Au_{xx}+2Bu_{xy}+Cu_{yy}+Du_x+Eu_y+Fu=G,\tag{1.8}
$$
where the coefficients are functions of $(x,y)$ and $A,B,C$ do not vanish simultaneously. The second-order terms (the principal part) determine the character of the equation. They correspond to the **quadratic form** $A\xi^2+2B\xi\eta+C\eta^2$ with matrix $M=\begin{bmatrix}A&B\\B&C\end{bmatrix}$, in the same way that a quadratic curve $Ax^2+2Bxy+Cy^2=1$ is a hyperbola, a parabola or an ellipse according to the sign of $B^2-AC$.

**Definition 1.5.1 (Hyperbolic, Parabolic and Elliptic Equations)** At a point $(x_0,y_0)$, Eq. (1.8) is called

1. a **hyperbolic equation** if $B^2-AC>0$;
2. a **parabolic equation** if $B^2-AC=0$;
3. an **elliptic equation** if $B^2-AC<0$.

The equation is of a given type in a region if it is of that type at every point of the region.

Writing the wave equation as $u_{tt}-c^2u_{xx}=0$ (variables $(t,x)$, $A=1$, $B=0$, $C=-c^2$) gives $B^2-AC=c^2>0$: hyperbolic. The heat equation $ku_{xx}-u_t=0$ has $A=k$, $B=C=0$: parabolic. The Laplace equation $u_{xx}+u_{yy}=0$ has $B^2-AC=-1$: elliptic. The type can change from point to point: the Tricomi equation $yu_{xx}+u_{yy}=0$ from transonic gas dynamics has $B^2-AC=-y$, so it is elliptic for $y>0$ (subsonic flow), hyperbolic for $y<0$ (supersonic flow) and parabolic on the line $y=0$.

The type is a genuine property of the equation, not of the coordinates. Let

$$
\xi=\xi(x,y),\qquad\eta=\eta(x,y)
$$
be a $C^2$ change of variables with nonzero **Jacobian determinant** $J=\xi_x\eta_y-\xi_y\eta_x$, and write $u(x,y)=w(\xi,\eta)$. By the **chain rule**, $u_x=w_\xi\xi_x+w_\eta\eta_x$ and

$$
u_{xx}=w_{\xi\xi}\xi_x^2+2w_{\xi\eta}\xi_x\eta_x+w_{\eta\eta}\eta_x^2+w_\xi\xi_{xx}+w_\eta\eta_{xx},
$$
and similarly for $u_{xy}$ and $u_{yy}$. Substituting into Eq. (1.8) gives an equation of the same form,

$$
\bar Aw_{\xi\xi}+2\bar Bw_{\xi\eta}+\bar Cw_{\eta\eta}+(\text{terms with }w_\xi,w_\eta,w)=G,
$$
with

$$
\begin{aligned}
\bar A&=A\xi_x^2+2B\xi_x\xi_y+C\xi_y^2,\\
\bar B&=A\xi_x\eta_x+B(\xi_x\eta_y+\xi_y\eta_x)+C\xi_y\eta_y,\\
\bar C&=A\eta_x^2+2B\eta_x\eta_y+C\eta_y^2.
\end{aligned}\tag{1.9}
$$

**Theorem 1.5.1** Under a change of variables with Jacobian determinant $J\ne0$, the new coefficients (1.9) satisfy

$$
\bar B^2-\bar A\bar C=J^2\,(B^2-AC).
$$
In particular, the type of Eq. (1.8) at a point does not depend on the choice of coordinates.

**Proof** Let $P=\begin{bmatrix}\xi_x&\xi_y\\\eta_x&\eta_y\end{bmatrix}$ be the **Jacobian matrix** of the change of variables. Formulas (1.9) say exactly that

$$
\begin{bmatrix}\bar A&\bar B\\\bar B&\bar C\end{bmatrix}=P\begin{bmatrix}A&B\\B&C\end{bmatrix}P^{\mathsf T},
$$
as one verifies by multiplying out. Taking determinants, $\bar A\bar C-\bar B^2=(\det P)^2(AC-B^2)=J^2(AC-B^2)$. $\square$

### 1.5.2. Characteristics and Canonical Forms

The idea of the classification is to choose new coordinates in which the principal part is as simple as possible, like bringing a quadratic form to principal axes. By Eq. (1.9), the coefficient $\bar A$ vanishes exactly when $\xi$ satisfies the first-order equation

$$
A\xi_x^2+2B\xi_x\xi_y+C\xi_y^2=0.\tag{1.10}
$$
If $\xi_y\ne0$, the level curves $\xi(x,y)=\text{const}$ have slope $\frac{\mathrm{d}y}{\mathrm{d}x}=-\frac{\xi_x}{\xi_y}$; substituting $\xi_x=-\xi_y\frac{\mathrm{d}y}{\mathrm{d}x}$ into Eq. (1.10) and dividing by $\xi_y^2$ shows that Eq. (1.10) is equivalent to an ordinary differential equation for the level curves.

**Definition 1.5.2 (Characteristic Equation and Characteristic Curves)** The ordinary differential equation

$$
A\Big(\frac{\mathrm{d}y}{\mathrm{d}x}\Big)^2-2B\frac{\mathrm{d}y}{\mathrm{d}x}+C=0,\qquad\text{that is,}\qquad A\,(\mathrm{d}y)^2-2B\,\mathrm{d}x\,\mathrm{d}y+C\,(\mathrm{d}x)^2=0,\tag{1.11}
$$
is called the **characteristic equation** of Eq. (1.8), and its integral curves are called the **characteristic curves** of Eq. (1.8).

When $A\ne0$, Eq. (1.11) factors as

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{B\pm\sqrt{B^2-AC}}{A},
$$
so a hyperbolic equation has two real families of characteristic curves, a parabolic equation one family, and an elliptic equation none (the roots are complex). The characteristics are the curves along which the equation cannot determine all second derivatives of $u$ from the values of $u$ and its first derivatives on the curve; [2.5.3](/2.5.3) shows that for the wave equation they are the paths along which signals travel. For the Tricomi equation, Eq. (1.11) reads $y(\mathrm{d}y)^2+(\mathrm{d}x)^2=0$, which has real solutions only for $y<0$: there $\frac{\mathrm{d}x}{\mathrm{d}y}=\pm\sqrt{-y}$, and the characteristics are the curves $x\pm\frac23(-y)^{3/2}=\text{const}$.

![Type regions and characteristic curves of the Tricomi equation y u_xx + u_yy = 0: elliptic for y > 0, hyperbolic for y < 0 with the two families x ± (2/3)(-y)^(3/2) = const, which meet the parabolic line y = 0 in cusps](./plots/tricomi-characteristics.py)

**Theorem 1.5.2 (Canonical Forms)** Suppose the coefficients of Eq. (1.8) are sufficiently smooth (for the elliptic case, analytic) and the equation has a fixed type in a neighborhood of a point. Then near that point there are coordinates $(\xi,\eta)$ in which the equation takes one of the following *canonical forms*, where the dots denote terms of order at most one:

1. hyperbolic: $w_{\xi\eta}+\cdots=0$, or equivalently (with $\alpha=\xi+\eta$, $\beta=\xi-\eta$) $w_{\alpha\alpha}-w_{\beta\beta}+\cdots=0$;
2. parabolic: $w_{\eta\eta}+\cdots=0$;
3. elliptic: $w_{\xi\xi}+w_{\eta\eta}+\cdots=0$.

**Proof** (Hyperbolic case.) Let $\varphi_1(x,y)=C_1$ and $\varphi_2(x,y)=C_2$ be general integrals of the two factors of Eq. (1.11), with $\nabla\varphi_1,\nabla\varphi_2\ne\boldsymbol{0}$. Both $\varphi_1$ and $\varphi_2$ satisfy Eq. (1.10), and they are independent because the two families of characteristics have different slopes. Taking $\xi=\varphi_1$, $\eta=\varphi_2$ gives $J\ne0$ and $\bar A=\bar C=0$ by Eq. (1.9); by Theorem 1.5.1, $\bar B^2=J^2(B^2-AC)>0$, so we can divide by $2\bar B$.

(Parabolic case.) There is one family $\varphi(x,y)=C$; take $\xi=\varphi$ and any $\eta$ with $J\ne0$. Then $\bar A=0$, and Theorem 1.5.1 gives $\bar B^2=\bar A\bar C=0$, so $\bar B=0$; $\bar C\ne0$ because the principal part cannot vanish identically, and we divide by $\bar C$.

(Elliptic case.) The characteristic equation has a complex solution $\varphi=\alpha+\mathrm{i}\beta$ of Eq. (1.10) (this is where analyticity is used). Separating the real and imaginary parts of $A\varphi_x^2+2B\varphi_x\varphi_y+C\varphi_y^2=0$ gives exactly $\bar A=\bar C$ and $\bar B=0$ for the coordinates $\xi=\alpha$, $\eta=\beta$. $\square$

For constant coefficients the characteristics are straight lines and the canonical form can be found by hand, as in the following examples; the reduction to canonical form is often the first step toward a general solution.

**Example 1.5.1** Find the general solution of $u_{xx}+2u_{xy}-3u_{yy}=0$.

**Solution** Here $A=1$, $B=1$, $C=-3$, $B^2-AC=4>0$: hyperbolic. The characteristic equation $(y')^2-2y'-3=0$ gives $y'=3$ and $y'=-1$, so the characteristics are the lines $y-3x=C_1$ and $y+x=C_2$. With $\xi=y-3x$ and $\eta=y+x$, Eq. (1.9) gives $\bar A=\bar C=0$ and $\bar B=1\cdot(-3)\cdot1+1\cdot(-3\cdot1+1\cdot1)+(-3)\cdot1\cdot1=-8$, so the equation becomes $-16w_{\xi\eta}=0$, that is, $w_{\xi\eta}=0$. As in §1.1.2, $w=F(\xi)+G(\eta)$, and

$$
u(x,y)=F(y-3x)+G(y+x)
$$
with $F,G$ arbitrary $C^2$ functions.

**Example 1.5.2** Find the general solution of $u_{xx}+2u_{xy}+u_{yy}=0$.

**Solution** $A=B=C=1$ and $B^2-AC=0$: parabolic. The characteristic equation $(y'-1)^2=0$ has the single family $y-x=C$. Take $\xi=y-x$ and $\eta=x$. Then $\bar A=0$, $\bar B=0$ and $\bar C=1$, so the equation becomes $w_{\eta\eta}=0$, whence $w=F(\xi)+\eta\,G(\xi)$ and

$$
u(x,y)=F(y-x)+x\,G(y-x).
$$
(Indeed, the equation is $(\partial_x+\partial_y)^2u=0$.)

**Example 1.5.3** Reduce $u_{xx}+2u_{xy}+5u_{yy}=0$ to canonical form.

**Solution** $B^2-AC=1-5=-4<0$: elliptic. The characteristic equation $(y')^2-2y'+5=0$ has the complex roots $y'=1\pm2\mathrm{i}$, with complex characteristics $y-x\mp2\mathrm{i}x=C$. Take the real and imaginary parts $\xi=y-x$, $\eta=2x$. Then $P=\begin{bmatrix}-1&1\\2&0\end{bmatrix}$ and

$$
P\begin{bmatrix}1&1\\1&5\end{bmatrix}P^{\mathsf T}=\begin{bmatrix}4&0\\0&4\end{bmatrix},
$$
so the equation becomes $w_{\xi\xi}+w_{\eta\eta}=0$: in the coordinates $(\xi,\eta)$ it is the Laplace equation.

### 1.5.3. More Independent Variables

The second-order linear equation in $n$ variables is

$$
\sum_{i,j=1}^na_{ij}(x)u_{x_ix_j}+\sum_{i=1}^nb_i(x)u_{x_i}+c(x)u=f(x),\qquad a_{ij}=a_{ji}.\tag{1.12}
$$
At each point the symmetric matrix $(a_{ij})$ has $n$ real **eigenvalues**. Eq. (1.12) is called elliptic at the point if all eigenvalues are nonzero and have the same sign; hyperbolic if all are nonzero and exactly one has the sign opposite to the others; and parabolic if exactly one eigenvalue is zero and the others have the same sign. (Other sign patterns, such as two positive and two negative eigenvalues, are possible when $n\ge4$, but they rarely occur in applications.) Under a change of variables $y=y(x)$ the matrix transforms as in Theorem 1.5.1, $(a_{ij})\mapsto P(a_{ij})P^{\mathsf T}$ with $P$ the Jacobian matrix, and by **Sylvester's law of inertia** the numbers of positive, negative and zero eigenvalues do not change; so the type is again independent of the coordinates.

When the $a_{ij}$ are constant, an orthogonal change of variables diagonalizes the matrix (principal axes), and a rescaling of each variable brings the principal part to $\pm u_{y_1y_1}\pm\cdots\pm u_{y_ny_n}$. Unlike the case $n=2$, an equation with variable coefficients and $n\ge3$ cannot in general be brought to canonical form in a whole neighborhood; only the classification at each point survives.

In the variables $(x_1,\dots,x_n,t)$, the wave equation $u_{tt}-c^2\Delta u=0$ has the matrix $\operatorname{diag}(-c^2,\dots,-c^2,1)$: hyperbolic. The heat equation has $\operatorname{diag}(k,\dots,k,0)$: parabolic. The Laplace equation has the identity matrix: elliptic. The table summarizes the characteristic features of the three types, which the following chapters establish.

| Type | Prototype | Typical problem | Characteristic behavior |
|---|---|---|---|
| Hyperbolic | wave equation $u_{tt}=c^2\Delta u$ | initial value or initial-boundary value problem (two initial conditions) | finite speed of propagation, singularities propagate along characteristics, energy conserved, reversible in time |
| Parabolic | heat equation $u_t=k\Delta u$ | initial value or initial-boundary value problem (one initial condition) | infinite speed of propagation, instant smoothing, maximum principle, irreversible |
| Elliptic | Laplace equation $\Delta u=0$ | boundary value problem | equilibrium; solutions smooth, determined by boundary values; mean value property and maximum principle |

## Summary

- A partial differential equation is classified by its order and by its degree of nonlinearity (linear, semilinear, quasilinear, fully nonlinear). For linear homogeneous equations, solutions can be superposed; infinite superpositions require uniform convergence of the differentiated series.
- The wave equation (Newton's law for a string, $c^2=T/\rho$), the heat equation (energy conservation and Fourier's law, $k=\kappa/(c_{\mathrm{p}}\rho)$) and the Laplace and Poisson equations (steady states) are the three classical equations.
- A problem consists of the equation together with initial conditions (one for the heat equation, two for the wave equation) and boundary conditions (Dirichlet, Neumann, Robin). It is well-posed if a solution exists, is unique and depends continuously on the data. The Cauchy problem for the Laplace equation (Hadamard's example) and the backward heat equation are ill-posed.
- The second-order equation $Au_{xx}+2Bu_{xy}+Cu_{yy}+\cdots=0$ is hyperbolic, parabolic or elliptic according as $B^2-AC>0$, $=0$ or $<0$; the type is invariant under changes of variables. The characteristic equation $A(\mathrm{d}y)^2-2B\,\mathrm{d}x\,\mathrm{d}y+C(\mathrm{d}x)^2=0$ gives the coordinates that reduce the equation to its canonical form.
