---
title: Separation of Variables in Cylindrical and Spherical Coordinates
---

Drums, pipes, cylindrical rods, planets and atoms are not rectangles, and a problem posed on a disk, a cylinder or a ball should be solved in coordinates adapted to its boundary. In such coordinates **separation of variables** works exactly as on an interval ([2.5.4](/2.5.4)), but the separated ordinary differential equations are no longer $X''+\lambda X=0$: in polar and cylindrical coordinates the radial equation is the **Bessel equation**, and in spherical coordinates the angular equation is the **Legendre equation**. The eigenfunctions are therefore Bessel functions and Legendre polynomials instead of sines and cosines, and solutions are expanded in Fourier–Bessel and Legendre series instead of Fourier series. The special functions and their orthogonality were prepared in [2.4.10](/2.4.10); Sturm–Liouville theory ([2.4.12](/2.4.12)) explains why the expansions exist. This chapter puts these pieces together. The next chapter treats unbounded regions, where series give way to integral transforms.

## 5.1. The Laplace Operator in Curvilinear Coordinates

### 5.1.1. Polar, Cylindrical and Spherical Coordinates

The **Laplace operator** in orthogonal curvilinear coordinates was computed in [2.2.14](/2.2.14#sec-14.6). In this course we write **cylindrical coordinates** as $(r,\theta,z)$ and **spherical coordinates** as $(r,\theta,\varphi)$, where $r$ is the distance from the origin, $\theta\in[0,\pi]$ is the polar angle measured from the positive $z$-axis and $\varphi\in[0,2\pi)$ is the azimuthal angle:

$$
x=r\sin\theta\cos\varphi,\qquad y=r\sin\theta\sin\varphi,\qquad z=r\cos\theta.
$$
This is the convention of physics and of most PDE texts, and it matches the notation $P_n(\cos\theta)\mathrm{e}^{\mathrm{i}m\varphi}$ of [2.4.10](/2.4.10); note that the roles of the letters $\theta$ and $\varphi$ are interchanged compared with [2.2.12](/2.2.12). The Laplacian reads

$$
\begin{aligned}
\text{polar:}\quad&\Delta u=u_{rr}+\frac1ru_r+\frac1{r^2}u_{\theta\theta},\\
\text{cylindrical:}\quad&\Delta u=u_{rr}+\frac1ru_r+\frac1{r^2}u_{\theta\theta}+u_{zz},\\
\text{spherical:}\quad&\Delta u=\frac1{r^2}\big(r^2u_r\big)_r+\frac1{r^2\sin\theta}\big(\sin\theta\,u_\theta\big)_\theta+\frac1{r^2\sin^2\theta}u_{\varphi\varphi}.
\end{aligned}\tag{5.1}
$$
The angular part of the spherical Laplacian, $\Delta_SY=\frac1{\sin\theta}(\sin\theta\,Y_\theta)_\theta+\frac1{\sin^2\theta}Y_{\varphi\varphi}$, is the Laplacian on the unit sphere, so that $\Delta u=\frac1{r^2}(r^2u_r)_r+\frac1{r^2}\Delta_Su$.

The coordinate singularities ($r=0$, and $\theta=0,\pi$ in spherical coordinates) are not boundaries of the physical region. At these points the separated equations have singular points, and in place of a boundary condition we require the solution to be bounded there. This "natural" condition is what selects $J_m$ rather than $Y_m$, and $P_n$ rather than $Q_n$.

### 5.1.2. The Helmholtz Equation

Separating time from space in the **wave equation** $u_{tt}=c^2\Delta u$ or the **heat equation** $u_t=k\Delta u$ on a region $\Omega$, we set $u=T(t)v(x)$ and obtain $T''/(c^2T)=\Delta v/v=-\lambda$ or $T'/(k T)=\Delta v/v=-\lambda$. In both cases the spatial factor satisfies the same equation.

**Definition 5.1.1 (Helmholtz Equation)** The equation

$$
\Delta v+\lambda v=0\quad\text{in }\Omega\tag{5.2}
$$
is called the **Helmholtz equation**. Together with a homogeneous boundary condition on $\partial\Omega$ it is an **eigenvalue problem** for the operator $-\Delta$: a number $\lambda$ for which (5.2) has a nontrivial solution satisfying the boundary condition is an eigenvalue, and the solution is an **eigenfunction**.

The time factor is then $\cos(c\sqrt\lambda\,t)$, $\sin(c\sqrt\lambda\,t)$ for the wave equation and $\mathrm{e}^{-k\lambda t}$ for the heat equation, so the eigenvalues determine the natural frequencies and the decay rates. Their basic properties follow from **Green's first identity** in the same way as for the one-dimensional **Sturm–Liouville problem**.

**Theorem 5.1.1** Let $\Omega\subset\mathbb{R}^n$ ($n=2,3$) be a bounded region with piecewise smooth boundary, and consider $-\Delta v=\lambda v$ in $\Omega$ with the **Dirichlet boundary condition** $v=0$ on $\partial\Omega$, for $v\in C^2(\Omega)\cap C^1(\bar\Omega)$ (complex values allowed).

1. Every eigenvalue is real and positive, and
$$
\lambda=\frac{\displaystyle\int_\Omega\lvert\nabla v\rvert^2\,\mathrm{d}V}{\displaystyle\int_\Omega\lvert v\rvert^2\,\mathrm{d}V}.
$$
2. Eigenfunctions belonging to different eigenvalues are orthogonal: $\int_\Omega v\bar w\,\mathrm{d}V=0$.

For the **Neumann boundary condition** $\frac{\partial v}{\partial\boldsymbol{n}}=0$ the same holds, except that $\lambda=0$ is an eigenvalue with constant eigenfunctions.

**Proof** Green's first identity holds for complex functions by linearity. Applied to $\bar v$ and $v$, it gives

$$
\int_\Omega\bar v\,\Delta v\,\mathrm{d}V=\oint_{\partial\Omega}\bar v\frac{\partial v}{\partial\boldsymbol{n}}\,\mathrm{d}S-\int_\Omega\lvert\nabla v\rvert^2\,\mathrm{d}V=-\int_\Omega\lvert\nabla v\rvert^2\,\mathrm{d}V,
$$
since $v=0$ on $\partial\Omega$. Substituting $\Delta v=-\lambda v$ gives the quotient formula, so $\lambda$ is real and $\lambda\ge0$. If $\lambda=0$, then $\nabla v\equiv\boldsymbol{0}$, so $v$ is constant on each connected component of $\Omega$ and vanishes by the boundary condition, which is impossible for an eigenfunction. Hence $\lambda>0$.

For 2, let $-\Delta v=\lambda v$ and $-\Delta w=\mu w$ with $\lambda\ne\mu$; $\mu$ is real by 1. Applying Green's first identity twice and subtracting,

$$
(\lambda-\mu)\int_\Omega v\bar w\,\mathrm{d}V=\int_\Omega\big(v\Delta\bar w-\bar w\Delta v\big)\,\mathrm{d}V=\oint_{\partial\Omega}\Big(v\frac{\partial\bar w}{\partial\boldsymbol{n}}-\bar w\frac{\partial v}{\partial\boldsymbol{n}}\Big)\mathrm{d}S=0.
$$
For the Neumann condition the boundary terms vanish for the same reason. $\square$

As for regular Sturm–Liouville problems one can prove more (we state it without proof): for a connected region the Dirichlet eigenvalues form a sequence $0<\lambda_1<\lambda_2\le\lambda_3\le\cdots\to+\infty$ (repeated according to multiplicity), the first eigenfunction does not change sign, and the eigenfunctions form a complete orthogonal system, so that every reasonable function on $\Omega$ has an **eigenfunction expansion**. The eigenvalues encode geometry: by Weyl's law, $\lambda_j\sim4\pi j/\lvert\Omega\rvert$ in the plane, so the area of a drum can be heard from its high overtones. In general the eigenvalues cannot be computed in closed form. For the disk and the ball they can, because the Helmholtz equation separates.

## 5.2. Vibrations of a Circular Membrane

### 5.2.1. Separation of Variables

A membrane of radius $a$ is fixed along its rim. Its displacement $u(r,\theta,t)$ satisfies

$$
\begin{cases}
u_{tt}=c^2\Big(u_{rr}+\dfrac1ru_r+\dfrac1{r^2}u_{\theta\theta}\Big),&0\le r<a,\ t>0,\\[2mm]
u(a,\theta,t)=0,\\
u(r,\theta,0)=f(r,\theta),\quad u_t(r,\theta,0)=g(r,\theta).
\end{cases}\tag{5.3}
$$
By §5.1.2 we first solve the Helmholtz equation $v_{rr}+\frac1rv_r+\frac1{r^2}v_{\theta\theta}+\lambda v=0$ with $v(a,\theta)=0$; by Theorem 5.1.1, $\lambda>0$. Setting $v=R(r)\Theta(\theta)$ and multiplying by $r^2/(R\Theta)$,

$$
\frac{r^2R''+rR'+\lambda r^2R}{R}=-\frac{\Theta''}{\Theta}=\mu.
$$

1. The angular equation $\Theta''+\mu\Theta=0$ with the periodicity condition $\Theta(\theta+2\pi)=\Theta(\theta)$, because $\theta$ and $\theta+2\pi$ describe the same point. By the periodic case of the table in [2.4.12](/2.4.12#sec-12.4.1), $\mu=m^2$ with $m=0,1,2,\dots$ and $\Theta=A\cos m\theta+B\sin m\theta$.
2. The radial equation $r^2R''+rR'+(\lambda r^2-m^2)R=0$. With $s=\sqrt\lambda\,r$ this is the Bessel equation of order $m$, with general solution $R=CJ_m(\sqrt\lambda\,r)+DY_m(\sqrt\lambda\,r)$. The **Bessel function of the second kind** $Y_m$ is unbounded at $r=0$, so $D=0$.
3. The boundary condition $R(a)=J_m(\sqrt\lambda\,a)=0$, so $\sqrt\lambda\,a$ is a positive zero $j_{m,k}$ of $J_m$:
$$
\lambda_{mk}=\Big(\frac{j_{m,k}}{a}\Big)^2,\qquad v_{mk}=J_m\Big(\frac{j_{m,k}r}{a}\Big)\cos m\theta,\ J_m\Big(\frac{j_{m,k}r}{a}\Big)\sin m\theta,\qquad k=1,2,\dots
$$

The Dirichlet eigenvalues of the disk are thus the squares of the zeros of Bessel functions, divided by $a^2$; for $m\ge1$ each has two independent eigenfunctions (a rotation of the pattern). Each product

$$
u_{mk}=J_m\Big(\frac{j_{m,k}r}{a}\Big)\big(A\cos m\theta+B\sin m\theta\big)\cos(\omega_{mk}t-\delta),\qquad\omega_{mk}=\frac{c\,j_{m,k}}{a},
$$
is a standing wave, a normal mode of the drum. Its nodal lines (where $u_{mk}\equiv0$) consist of $m$ diameters and of the $k-1$ circles $r=a\,j_{m,i}/j_{m,k}$, $i<k$.

![Six normal modes of a circular membrane with their nodal lines; the titles give the frequency ratio omega_mk / omega_01 = j_mk / j_01](./plots/membrane-modes.py)

The frequencies relative to the fundamental $\omega_{01}$ are

| Mode $(m,k)$ | $(0,1)$ | $(1,1)$ | $(2,1)$ | $(0,2)$ | $(3,1)$ | $(1,2)$ | $(2,2)$ | $(0,3)$ |
|---|---|---|---|---|---|---|---|---|
| $j_{m,k}$ | $2.4048$ | $3.8317$ | $5.1356$ | $5.5201$ | $6.3802$ | $7.0156$ | $8.4172$ | $8.6537$ |
| $\omega_{mk}/\omega_{01}$ | $1$ | $1.593$ | $2.136$ | $2.295$ | $2.653$ | $2.917$ | $3.500$ | $3.598$ |

For a string the overtones are the integer multiples $n\omega_1$ of the fundamental, which the ear hears as a single pitch with a definite timbre. The overtones of a drum are not integer multiples and are spaced irregularly, which is why a drum sounds percussive rather than tuned. Timpani are tuned by loading the membrane with air so that the modes $(1,1),(2,1),(3,1)$ approach the ratios $2:3:4$.

![Natural frequencies of a string (integer multiples of the fundamental) and of a circular membrane (ratios of Bessel zeros j_mk / j_01), colored by the angular number m](./plots/drum-spectrum.py)

### 5.2.2. Fourier–Bessel Series

To satisfy the initial conditions we superpose all the modes by the **superposition principle** and must expand $f$ and $g$ in the eigenfunctions. For the radial factor this is the following expansion, whose orthogonality relation was proved in [Theorem 10.4.2](/2.4.10#thm-10.4.2).

**Definition 5.2.1 (Fourier–Bessel Series)** Let $\nu\ge0$, let $j_{\nu,k}$ be the positive zeros of $J_\nu$, and let $f$ be integrable on $[0,a]$ with respect to the weight $r$. The series

$$
f(r)\sim\sum_{k=1}^\infty c_kJ_\nu\Big(\frac{j_{\nu,k}r}{a}\Big),\qquad c_k=\frac{2}{a^2J_{\nu+1}(j_{\nu,k})^2}\int_0^arf(r)J_\nu\Big(\frac{j_{\nu,k}r}{a}\Big)\mathrm{d}r\tag{5.4}
$$
is called the **Fourier–Bessel series** of $f$ (of order $\nu$).

The coefficient formula is the usual "coordinate equals inner product divided by norm squared": substituting $x=r/a$ in Theorem 10.4.2 gives $\int_0^arJ_\nu(j_{\nu,k}r/a)^2\,\mathrm{d}r=\frac{a^2}2J_{\nu+1}(j_{\nu,k})^2$. For piecewise smooth $f$ the series converges to $\frac12\big(f(r^+)+f(r^-)\big)$ for $0<r<a$, like a **Fourier series** (stated without proof). At $r=a$ every term vanishes, so the convergence is nonuniform near $a$ unless $f(a)=0$.

Expanding the initial data in the double system $J_m(j_{m,k}r/a)\cos m\theta$, $J_m(j_{m,k}r/a)\sin m\theta$ (a Fourier series in $\theta$ whose coefficients are expanded in Fourier–Bessel series in $r$), the solution of (5.3) is

$$
u=\sum_{m=0}^\infty\sum_{k=1}^\infty J_m\Big(\frac{j_{m,k}r}{a}\Big)\Big[\big(A_{mk}\cos m\theta+B_{mk}\sin m\theta\big)\cos\omega_{mk}t+\big(C_{mk}\cos m\theta+D_{mk}\sin m\theta\big)\sin\omega_{mk}t\Big],
$$
where, for example,

$$
A_{mk}=\frac{\displaystyle\int_0^{2\pi}\!\!\int_0^af(r,\theta)J_m\Big(\frac{j_{m,k}r}{a}\Big)\cos m\theta\,r\,\mathrm{d}r\,\mathrm{d}\theta}{\varepsilon_m\pi\cdot\frac{a^2}{2}J_{m+1}(j_{m,k})^2},\qquad\varepsilon_0=2,\ \varepsilon_m=1\ (m\ge1),
$$
and $C_{mk}$ is obtained from $g$ in the same way with an extra factor $1/\omega_{mk}$.

**Example 5.2.1** A membrane with $a=c=1$ is released from rest from the paraboloid $f=1-r^2$. Find the motion.

**Solution** The data do not depend on $\theta$, so only $m=0$ appears, and $g=0$ gives $C_{0k}=0$. Write $j_k=j_{0,k}$. Using $(xJ_1)'=xJ_0$ and $(x^2J_2)'=x^2J_1$ from the recurrence relations,

$$
\int_0^1rJ_0(j_kr)\,\mathrm{d}r=\frac{J_1(j_k)}{j_k},\qquad\int_0^1r(1-r^2)J_0(j_kr)\,\mathrm{d}r=\frac{2J_2(j_k)}{j_k^2}=\frac{4J_1(j_k)}{j_k^3},
$$
where the second integral follows by integrating by parts once ($1-r^2$ vanishes at $r=1$) and the last step uses $J_2(j_k)=\frac{2}{j_k}J_1(j_k)-J_0(j_k)$ with $J_0(j_k)=0$. Hence $c_k=\frac{2}{J_1(j_k)^2}\cdot\frac{4J_1(j_k)}{j_k^3}$, and

$$
u(r,t)=\sum_{k=1}^\infty\frac{8}{j_k^3J_1(j_k)}J_0(j_kr)\cos(j_kt).
$$
Numerically the coefficients are $1.108$, $-0.140$, $0.045,\dots$: the motion is almost a pure fundamental mode, because the initial shape already resembles $J_0(j_1r)$.

## 5.3. Problems in a Cylinder

### 5.3.1. Cooling of a Long Cylinder

An infinitely long cylinder of radius $a$, initially at temperature $f(r)$, has its surface held at temperature $0$. The temperature depends only on $r$ and $t$:

$$
u_t=k\Big(u_{rr}+\frac1ru_r\Big),\quad0\le r<a,\qquad u(a,t)=0,\qquad u(r,0)=f(r).
$$
This is the case $m=0$ of §5.2 with the time factor $\mathrm{e}^{-k\lambda t}$:

$$
u(r,t)=\sum_{n=1}^\infty c_n\,\mathrm{e}^{-k j_{0,n}^2t/a^2}J_0\Big(\frac{j_{0,n}r}{a}\Big),\qquad c_n\text{ from (5.4) with }\nu=0.
$$
For a uniform initial temperature $f\equiv u_0$, the first integral of Example 5.2.1 gives $c_n=\frac{2u_0}{j_{0,n}J_1(j_{0,n})}$. All terms decay, and for large $t$ the first one dominates: $u\approx1.602\,u_0\,\mathrm{e}^{-k j_{0,1}^2t/a^2}J_0(j_{0,1}r/a)$. The time constant $a^2/(k j_{0,1}^2)$ is the same for any initial temperature, and comparing the three basic shapes of the same "radius" $a$ shows the effect of geometry:

| Body | First Dirichlet eigenvalue | Time constant $1/(k\lambda_1)$ |
|---|---|---|
| Slab $\lvert x\rvert<a$ | $(\pi/2a)^2\approx2.47/a^2$ | $0.405\,a^2/k$ |
| Infinite cylinder $r<a$ | $j_{0,1}^2/a^2\approx5.78/a^2$ | $0.173\,a^2/k$ |
| Ball $r<a$ | $\pi^2/a^2\approx9.87/a^2$ | $0.101\,a^2/k$ |

The more surface a body has per unit volume, the faster it cools. (The value for the ball comes from the radial eigenfunction $\frac{\sin(\pi r/a)}{r}$ of §5.4.3.)

### 5.3.2. Steady State in a Finite Cylinder

Consider a cylinder $0\le r<a$, $0<z<h$ whose lateral surface and bottom are held at temperature $0$ and whose top is held at an axisymmetric temperature $f(r)$. The steady temperature solves the **Laplace equation**

$$
u_{rr}+\frac1ru_r+u_{zz}=0,\qquad u(a,z)=0,\quad u(r,0)=0,\quad u(r,h)=f(r).
$$
The homogeneous conditions are on the lateral surface, so the eigenvalue problem is in $r$: $u=R(r)Z(z)$ gives $(rR')'+\lambda rR=0$, $R(a)=0$, $R$ bounded, hence $R=J_0(j_{0,k}r/a)$ with $\lambda=(j_{0,k}/a)^2$. Then $Z''-\lambda Z=0$ with $Z(0)=0$ gives $Z=\sinh(j_{0,k}z/a)$, and the condition at the top determines the coefficients:

$$
u(r,z)=\sum_{k=1}^\infty c_k\frac{\sinh(j_{0,k}z/a)}{\sinh(j_{0,k}h/a)}J_0\Big(\frac{j_{0,k}r}{a}\Big),\qquad c_k\text{ the Fourier–Bessel coefficients of }f.
$$

If instead the top and bottom are held at $0$ and the lateral surface at $u(a,z)=g(z)$, the eigenvalue problem is in $z$: $Z=\sin\frac{n\pi z}{h}$, and the radial equation becomes $R''+\frac1rR'-\big(\frac{n\pi}h\big)^2R=0$, the modified Bessel equation, whose bounded solution is $I_0\big(\frac{n\pi r}{h}\big)$ ([2.4.10](/2.4.10#sec-10.4.4)). Then

$$
u(r,z)=\sum_{n=1}^\infty b_n\frac{I_0(n\pi r/h)}{I_0(n\pi a/h)}\sin\frac{n\pi z}{h},\qquad b_n=\frac2h\int_0^hg(z)\sin\frac{n\pi z}{h}\,\mathrm{d}z.
$$
The general rule is the same as on a rectangle: the direction carrying the homogeneous boundary conditions supplies the oscillating eigenfunctions, and the other direction is solved by non-oscillating functions ($\sinh$, $I_0$) fitted to the remaining boundary data.

## 5.4. Problems in a Ball

### 5.4.1. Axisymmetric Solutions and Legendre Polynomials

We solve the Dirichlet problem for the Laplace equation in the ball $r<a$ with boundary values that do not depend on $\varphi$:

$$
\Delta u=0\ \ (r<a),\qquad u(a,\theta)=f(\theta),\quad0\le\theta\le\pi.
$$
The solution is then independent of $\varphi$. Setting $u=R(r)\Theta(\theta)$ in (5.1) and multiplying by $r^2/(R\Theta)$,

$$
\frac{(r^2R')'}{R}=-\frac{(\sin\theta\,\Theta')'}{\sin\theta\,\Theta}=\mu.
$$
With $x=\cos\theta$ we have $\frac{\mathrm{d}}{\mathrm{d}\theta}=-\sin\theta\frac{\mathrm{d}}{\mathrm{d}x}$, and the angular equation becomes

$$
\big((1-x^2)\Theta_x\big)_x+\mu\Theta=0,\qquad-1<x<1,
$$
the Legendre equation with $\mu=\nu(\nu+1)$. The poles $\theta=0,\pi$ are interior points of the ball, so $\Theta$ must be bounded at $x=\pm1$; by [2.4.10](/2.4.10#sec-10.2.3) this happens exactly for $\mu=n(n+1)$, $n=0,1,2,\dots$, with $\Theta=P_n(\cos\theta)$. The radial equation $r^2R''+2rR'-n(n+1)R=0$ is a Cauchy–Euler equation ([2.4.9](/2.4.9)) with solutions $r^n$ and $r^{-(n+1)}$; boundedness at the center selects $r^n$. Therefore

$$
u(r,\theta)=\sum_{n=0}^\infty A_n\Big(\frac ra\Big)^nP_n(\cos\theta),\qquad A_n=\frac{2n+1}{2}\int_0^\pi f(\theta)P_n(\cos\theta)\sin\theta\,\mathrm{d}\theta,\tag{5.5}
$$
where $A_n$ are the coefficients of the Legendre series of $f$ in the variable $x=\cos\theta$ (the factor $\sin\theta\,\mathrm{d}\theta=-\mathrm{d}x$ is the change of variable). For the exterior problem ($r>a$, $u\to0$ as $r\to\infty$) we keep $r^{-(n+1)}$ instead and obtain $u=\sum A_n(a/r)^{n+1}P_n(\cos\theta)$.

**Example 5.4.1** Solve $\Delta u=0$ in $r<a$ with $u(a,\theta)=\cos^2\theta$.

**Solution** No integration is needed: since $P_2(x)=\frac{3x^2-1}2$, we have $x^2=\frac13P_0(x)+\frac23P_2(x)$. By (5.5),

$$
u=\frac13+\frac23\Big(\frac ra\Big)^2P_2(\cos\theta)=\frac13+\frac{3z^2-r^2}{3a^2}.
$$
In Cartesian coordinates $u=\frac13+\frac{2z^2-x^2-y^2}{3a^2}$, and one checks directly that $\Delta u=\frac{4-2-2}{3a^2}=0$. The value at the center is $\frac13$, the average of $\cos^2\theta$ over the sphere, as the mean value property of harmonic functions ([2.5.8](/2.5.8)) predicts.

**Example 5.4.2 (Conducting Sphere in a Uniform Field)** A grounded conducting sphere $r=a$ is placed in a uniform electric field $E_0$ along the $z$-axis. The potential satisfies $\Delta u=0$ for $r>a$, $u=0$ on $r=a$, and $u\approx-E_0z=-E_0r\cos\theta$ for large $r$. Find $u$.

**Solution** The boundary data involve only $P_1(\cos\theta)=\cos\theta$, so we try $u=\big(Ar+Br^{-2}\big)\cos\theta$, a combination of the two radial solutions for $n=1$. The condition at infinity gives $A=-E_0$, and $u(a,\theta)=0$ gives $B=E_0a^3$:

$$
u=-E_0\Big(r-\frac{a^3}{r^2}\Big)\cos\theta.
$$
The term $E_0a^3\cos\theta/r^2$ is the potential of a dipole, the field of the charges induced on the sphere. The field at the surface is $-u_r(a,\theta)=3E_0\cos\theta$: at the poles it is three times the applied field.

### 5.4.2. Spherical Harmonics

Without axial symmetry we separate $u=R(r)Y(\theta,\varphi)$, obtaining $(r^2R')'=\mu R$ and $\Delta_SY+\mu Y=0$, and then $Y=\Theta(\theta)\Phi(\varphi)$. As for the disk, periodicity in $\varphi$ gives $\Phi=\mathrm{e}^{\mathrm{i}m\varphi}$ with $m\in\mathbb{Z}$, and $\Theta$ satisfies, with $x=\cos\theta$, the associated Legendre equation

$$
(1-x^2)\Theta''-2x\Theta'+\Big(\mu-\frac{m^2}{1-x^2}\Big)\Theta=0.
$$
It has a solution bounded at $x=\pm1$ if and only if $\mu=n(n+1)$ with $n\ge\lvert m\rvert$ (stated without proof), and the solution is then a multiple of $P_n^{\lvert m\rvert}(x)$ below.

**Definition 5.4.1 (Spherical Harmonics)** For integers $0\le m\le n$, the functions

$$
P_n^m(x)=(1-x^2)^{m/2}\frac{\mathrm{d}^m}{\mathrm{d}x^m}P_n(x)
$$
are called the **associated Legendre functions**. For integers $n\ge0$ and $\lvert m\rvert\le n$, the functions

$$
Y_n^m(\theta,\varphi)=P_n^{\lvert m\rvert}(\cos\theta)\,\mathrm{e}^{\mathrm{i}m\varphi}
$$
on the unit sphere are called the **spherical harmonics** of degree $n$ (often multiplied by normalizing constants, which we omit).

**Theorem 5.4.1** Spherical harmonics have the following properties (stated without proof).

1. $\Delta_SY_n^m=-n(n+1)Y_n^m$: the spherical harmonics of degree $n$ are eigenfunctions of $-\Delta_S$ with eigenvalue $n(n+1)$, which has multiplicity $2n+1$;
2. They are orthogonal on the sphere with respect to the area element $\mathrm{d}S=\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$, and the system $\{Y_n^m\}$ is complete, so every square-integrable function on the sphere has a Laplace series $f=\sum_{n,m}a_{nm}Y_n^m$;
3. $r^nY_n^m(\theta,\varphi)$ is a homogeneous harmonic polynomial of degree $n$ in $x,y,z$, and the restrictions of such polynomials to the sphere are exactly the spherical harmonics of degree $n$.

For example, for $n=1$: $rP_1(\cos\theta)=z$ and $rP_1^1(\cos\theta)\mathrm{e}^{\pm\mathrm{i}\varphi}=r\sin\theta\,\mathrm{e}^{\pm\mathrm{i}\varphi}=x\pm\mathrm{i}y$, three harmonic polynomials of degree 1. The general Dirichlet problem in the ball is solved by $u=\sum_{n,m}a_{nm}(r/a)^nY_n^m$, where $a_{nm}$ are the Laplace series coefficients of the boundary values.

![Real parts P_n^m(cos theta) cos(m phi) of spherical harmonics for n = 0, …, 3: its zero set consists of m great circles through the poles and n - m parallels](./plots/spherical-harmonics.py)

Spherical harmonics appear wherever a problem has spherical symmetry: the multipole expansion of a potential, the gravitational field of the Earth, the angular distribution of the cosmic microwave background, and the angular part of atomic orbitals. In the hydrogen atom, separating the Schrödinger equation with a central potential produces exactly the eigenvalue problem $\Delta_SY=-\ell(\ell+1)Y$; the orbitals labeled s, p, d, f correspond to $\ell=0,1,2,3$, and the $2\ell+1$ values of $m$ account for the degeneracy of each level.

### 5.4.3. The Radial Equation for the Helmholtz Equation

For the wave or heat equation in a ball, the Helmholtz equation $\Delta v+\lambda v=0$ separates into $Y_n^m$ and the radial equation

$$
r^2R''+2rR'+\big(\lambda r^2-n(n+1)\big)R=0.
$$
The substitution $R=r^{-1/2}S$ turns it into the Bessel equation of order $n+\frac12$ for $S$, so the bounded solutions are the spherical Bessel functions $j_n(\sqrt\lambda\,r)$, where $j_n(x)=\sqrt{\frac{\pi}{2x}}J_{n+1/2}(x)$. By [Theorem 10.4.1](/2.4.10#thm-10.4.1), $J_{1/2}$ is elementary, and $j_0(x)=\frac{\sin x}{x}$. For radially symmetric problems ($n=0$) we can therefore write the eigenfunctions explicitly: the Dirichlet eigenfunctions of the ball are $\frac{\sin(k\pi r/a)}{r}$ with $\lambda=(k\pi/a)^2$, which gave the last row of the table in §5.3.1.

## Summary

| Region | Separated equations | Eigenfunctions | Eigenvalue condition |
|---|---|---|---|
| Disk $r<a$ (Helmholtz) | $\Theta''+m^2\Theta=0$; Bessel equation of order $m$ in $\sqrt\lambda\,r$ | $J_m(j_{m,k}r/a)\cos m\theta$, $J_m(j_{m,k}r/a)\sin m\theta$ | $\sqrt\lambda\,a=j_{m,k}$ |
| Cylinder, homogeneous on the side | Bessel in $r$; $Z''=\lambda Z$ | $J_0(j_{0,k}r/a)$, times $\sinh$ or $\cosh$ in $z$ | $J_0(\sqrt\lambda\,a)=0$ |
| Cylinder, homogeneous top and bottom | $Z''+\lambda Z=0$; modified Bessel in $r$ | $\sin(n\pi z/h)$, times $I_0(n\pi r/h)$ | $\lambda=(n\pi/h)^2$ |
| Ball, Laplace equation | Cauchy–Euler in $r$; associated Legendre in $\cos\theta$; $\Phi''+m^2\Phi=0$ | $r^nY_n^m(\theta,\varphi)$ | $\mu=n(n+1)$, boundedness at the poles |
| Ball, Helmholtz equation | Spherical Bessel in $r$ | $j_n(\sqrt\lambda\,r)Y_n^m$ | $j_n(\sqrt\lambda\,a)=0$ |

The method in every case: write $\Delta$ in coordinates adapted to the boundary, separate, impose periodicity in angles and boundedness at coordinate singularities, solve the eigenvalue problem in the directions with homogeneous conditions, and expand the remaining data in the resulting orthogonal system (Fourier, Fourier–Bessel, Legendre or Laplace series).
