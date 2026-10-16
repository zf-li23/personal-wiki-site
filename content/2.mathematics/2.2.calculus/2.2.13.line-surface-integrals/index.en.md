---
title: Line and Surface Integrals
source_hash: 0872c5890666
---

The **multiple integrals** of [2.2.12](/2.2.12) integrate over plane and spatial regions. Physics also deals with many quantities distributed along curves or over surfaces. The mass of a curved wire, and the mass and moment of inertia of a thin shell, are integrals of scalar functions along curves and over surfaces; they do not depend on orientation. The work done by a variable force along a path, and the flux of a fluid through a surface, are integrals of vector fields along oriented curves and over oriented surfaces; they change sign when the orientation is reversed. All four kinds of integrals are defined by the familiar "partition, approximate, sum, take the limit", and the basic method of computing all of them is parametrization: line integrals reduce to **definite integrals** and surface integrals to **double integrals**, the key points being the expressions for the arc length element $\mathrm{d}l$ and the area element $\mathrm{d}S$ and the handling of orientation.

The other theme of the chapter is Green's theorem: a double integral over a plane region equals a line integral of a vector field around its boundary. It is the two-dimensional generalization of the **fundamental theorem of calculus** $\int_a^bf'(x)\,\mathrm{d}x=f(b)-f(a)$: "the integral of a derivative over a region equals an integral over its boundary". [2.2.14](/2.2.14) extends it to the divergence theorem and Stokes' theorem in space and explains these formulas systematically in the language of divergence, curl and conservative fields; Cauchy's integral theorem in complex analysis also rests on Green's theorem. This chapter uses the tangent vectors, normal vectors and cross products of [2.2.11](/2.2.11), and the evaluation and change of variables of multiple integrals from [2.2.12](/2.2.12).

## 13.1. Line Integrals of Scalar Functions

### 13.1.1. Definition and Properties

Let a curved wire $L$ have linear density $\rho(x,y,z)$; we want its mass. Divide $L$ into small pieces $L_1,\dots,L_n$, the $i$-th of length $\Delta l_i$, and choose a point $P_i$ on each; the mass of a piece is approximately $\rho(P_i)\Delta l_i$, and summing and letting the partition become infinitely fine gives the mass.

**Definition 13.1.1 (Line Integral of a Scalar Function)** Let $L\subset\mathbb{R}^3$ be a rectifiable curve and $f$ a function defined on $L$. Divide $L$ arbitrarily into $n$ small arcs $L_1,\dots,L_n$, let $\Delta l_i$ be the arc length of $L_i$ and $\lambda=\max_i\Delta l_i$, and choose arbitrary $P_i\in L_i$. If the limit $\lim\limits_{\lambda\to0}\sum_{i=1}^nf(P_i)\Delta l_i$ exists and does not depend on the partition or the sample points, it is called the **line integral of a scalar function** $f$ along $L$ (or the line integral with respect to arc length), written

$$
\int_Lf(x,y,z)\,\mathrm{d}l.
$$
When $L$ is a closed curve we write $\oint_Lf\,\mathrm{d}l$; integrals $\int_Lf(x,y)\,\mathrm{d}l$ along plane curves are defined in the same way.

For $f\equiv1$ the integral is the **arc length** of $L$; for $f=\rho$ it is the mass; if $L$ lies in the $xy$-plane and $f\ge0$, then $\int_Lf\,\mathrm{d}l$ is the area of the piece of cylinder with directrix $L$, generators parallel to the $z$-axis and height $f(x,y)$.

**Property 13.1.1** Suppose the line integrals of $f$ and $g$ along $L$ exist.

- Linearity: $\int_L(\alpha f+\beta g)\,\mathrm{d}l=\alpha\int_Lf\,\mathrm{d}l+\beta\int_Lg\,\mathrm{d}l$.
- Additivity: if $L$ consists of $L_1$ and $L_2$ joined end to end, then $\int_L=\int_{L_1}+\int_{L_2}$.
- Monotonicity: if $f\le g$ on $L$, then $\int_Lf\,\mathrm{d}l\le\int_Lg\,\mathrm{d}l$.
- Independence of orientation: the integral does not depend on the direction in which $L$ is traversed, because the $\Delta l_i$ are always positive.

As with **multiple integrals**, symmetry can be exploited: if $L$ is symmetric about the $y$-axis and $f$ is odd in $x$, then $\int_Lf\,\mathrm{d}l=0$; if the equation of $L$ is symmetric under interchanging $x$ and $y$, then $\int_Lf(x,y)\,\mathrm{d}l=\int_Lf(y,x)\,\mathrm{d}l$.

### 13.1.2. Evaluation

**Theorem 13.1.1** Let $L$ be a **smooth curve** $\boldsymbol{r}(t)=(x(t),y(t),z(t))$, $\alpha\le t\le\beta$ (with $x,y,z$ continuously differentiable and $\boldsymbol{r}'(t)\ne\boldsymbol{0}$), and let $f$ be continuous on $L$. Then

$$
\int_Lf\,\mathrm{d}l=\int_\alpha^\beta f(x(t),y(t),z(t))\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}\,\mathrm{d}t.
$$

**Proof** A partition $\alpha=t_0<t_1<\cdots<t_n=\beta$ of $[\alpha,\beta]$ induces a partition of $L$. By the arc length formula and the **mean value theorem for integrals**, $\Delta l_i=\int_{t_{i-1}}^{t_i}\|\boldsymbol{r}'(t)\|\,\mathrm{d}t=\|\boldsymbol{r}'(\tau_i)\|\Delta t_i$ with $\tau_i\in[t_{i-1},t_i]$. Taking $P_i=\boldsymbol{r}(\tau_i)$, the sum $\sum f(P_i)\Delta l_i=\sum f(\boldsymbol{r}(\tau_i))\|\boldsymbol{r}'(\tau_i)\|\Delta t_i$ is a **Riemann sum** for the definite integral on the right. Since $\|\boldsymbol{r}'\|$ has a positive lower bound, $\max\Delta t_i\to0$ is equivalent to $\lambda\to0$, and passing to the limit gives the result. $\square$

In this formula $\mathrm{d}l=\|\boldsymbol{r}'(t)\|\,\mathrm{d}t$ is the arc length element. Since $\mathrm{d}l>0$, the lower limit of the definite integral must be less than the upper limit; this differs from the integrals of vector fields below. Common arc length elements:

| Representation of the curve | Arc length element $\mathrm{d}l$ |
|---|---|
| Parametric space curve $\boldsymbol{r}(t)$ | $\sqrt{x'^2+y'^2+z'^2}\,\mathrm{d}t$ |
| Plane curve $y=y(x)$ | $\sqrt{1+y'(x)^2}\,\mathrm{d}x$ |
| **Polar coordinates** $r=r(\theta)$ | $\sqrt{r^2+r'(\theta)^2}\,\mathrm{d}\theta$ |

**Example 13.1.1** Mass is distributed on the circle $x^2+y^2=2y$ with linear density $\sqrt{x^2+y^2}$ at $(x,y)$. Find the total mass $M$.

First solution: with the parametrization $x=\cos t$, $y=1+\sin t$, $0\le t\le2\pi$, we have $\mathrm{d}l=\mathrm{d}t$ and

$$
M=\int_0^{2\pi}\sqrt{2+2\sin t}\,\mathrm{d}t=\int_0^{2\pi}\sqrt{2}\sqrt{1+\sin t}\,\mathrm{d}t=8.
$$
(Put $t=s-\frac\pi2$; then $1+\sin t=1-\cos s=2\sin^2\frac s2$, and the integral is $2\int_0^{2\pi}\sin\frac s2\,\mathrm{d}s=8$.)

Second solution: in polar coordinates the circle is $r=2\sin\theta$, $0\le\theta\le\pi$, with $\mathrm{d}l=\sqrt{r^2+r'^2}\,\mathrm{d}\theta=2\,\mathrm{d}\theta$, and the integrand is $\sqrt{x^2+y^2}=r$, so $M=\int_0^\pi2\sin\theta\cdot2\,\mathrm{d}\theta=8$. A well-chosen coordinate system can simplify the computation considerably.

**Example 13.1.2** Find the area of the part of the cylinder $x^2+y^2=ax$ ($a>0$) lying inside the sphere $x^2+y^2+z^2=a^2$. The directrix of the cylinder is the circle $L\colon r=a\cos\theta$ ($|\theta|\le\frac\pi2$) in the $xy$-plane, with $\mathrm{d}l=a\,\mathrm{d}\theta$; above and below the point $(x,y)$ the cylinder has height $\sqrt{a^2-x^2-y^2}$. By the geometric meaning of the line integral,

$$
S=2\int_L\sqrt{a^2-x^2-y^2}\,\mathrm{d}l=2\int_{-\pi/2}^{\pi/2}\sqrt{a^2-a^2\cos^2\theta}\,a\,\mathrm{d}\theta=2a^2\int_{-\pi/2}^{\pi/2}|\sin\theta|\,\mathrm{d}\theta=4a^2.
$$

**Example 13.1.3** The curve $L\colon x^2+y^2+z^2=4$, $x^2+y^2=2x$, $z\ge0$ has linear density $|xyz|$ at $(x,y,z)$. Find the mass of $L$. A parametrization is $x=1+\cos t$, $y=\sin t$, $z=\sqrt{4-2x}=2\sin\frac t2$ ($0\le t\le2\pi$), with $\mathrm{d}l=\sqrt{1+\cos^2\frac t2}\,\mathrm{d}t$. Using half angles, $x=2\cos^2\frac t2$ and $y=2\sin\frac t2\cos\frac t2$; with $u=\frac t2$,

$$
m=\int_0^{\pi}8\,|\cos^3u|\sin^2u\sqrt{1+\cos^2u}\cdot2\,\mathrm{d}u=32\int_0^{\pi/2}\cos^3u\sin^2u\sqrt{1+\cos^2u}\,\mathrm{d}u.
$$
The substitution $s=\sin u$ turns this into $32\int_0^1(1-s^2)s^2\sqrt{2-s^2}\,\mathrm{d}s$; with $s=\sqrt2\sin\varphi$ the integrand becomes $\cos2\varphi\sin^22\varphi\,\mathrm{d}\varphi$, so

$$
m=32\int_0^{\pi/4}\cos2\varphi\sin^22\varphi\,\mathrm{d}\varphi=32\cdot\frac16=\frac{16}3.
$$

**Example 13.1.4** Let $L$ be the ellipse $x^2+4y^2=4$. Evaluate $\oint_L\sqrt{1+3y^2}\,\mathrm{d}l$. With $x=2\cos t$, $y=\sin t$ we get $\mathrm{d}l=\sqrt{4\sin^2t+\cos^2t}\,\mathrm{d}t=\sqrt{1+3\sin^2t}\,\mathrm{d}t$, which coincides with the integrand, so the integral is $\int_0^{2\pi}(1+3\sin^2t)\,\mathrm{d}t=2\pi+3\pi=5\pi$.

## 13.2. Surface Area and Surface Integrals of Scalar Functions

### 13.2.1. Surface Area

In one variable, arc length is defined as a limit of inscribed polygonal paths. The area of a surface cannot be defined as a limit of inscribed polyhedra (Schwarz gave an example in which the areas of inscribed polyhedra tend to infinity); instead we approximate by tangent planes. Divide the surface $S$ into small pieces $\Delta S_i$ and replace each piece by a small piece of its **tangent plane** at some point. If the projection of the piece onto the $xy$-plane has area $\Delta\sigma_i$ and the tangent plane makes an angle $\gamma_i$ with the $xy$-plane (that is, the **normal vector** makes the angle $\gamma_i$ with the $z$-axis), then $\Delta S_i\approx\Delta\sigma_i/|\cos\gamma_i|$.

**Definition 13.2.1 (Surface Area)** Let a smooth surface $S$ be given by $z=z(x,y)$, $(x,y)\in D_{xy}$, where $z$ has continuous partial derivatives on the bounded closed region $D_{xy}$. The quantity

$$
\iint_{D_{xy}}\frac{\mathrm{d}\sigma}{|\cos\gamma|}=\iint_{D_{xy}}\sqrt{1+z_x^2+z_y^2}\,\mathrm{d}x\,\mathrm{d}y
$$
is called the **surface area** of $S$, and $\mathrm{d}S=\sqrt{1+z_x^2+z_y^2}\,\mathrm{d}x\,\mathrm{d}y$ is called the area element.

Here the normal vector is $(-z_x,-z_y,1)$ and $|\cos\gamma|=1/\sqrt{1+z_x^2+z_y^2}$. When the surface is written as $x=x(y,z)$ or $y=y(z,x)$, we project onto the corresponding coordinate plane, and the formulas are analogous.

**Theorem 13.2.1 (Area Element of a Parametric Surface)** Let a smooth surface $S$ be given one-to-one by $\boldsymbol{r}(u,v)=(x(u,v),y(u,v),z(u,v))$, $(u,v)\in D_{uv}$, with components having continuous partial derivatives and $\boldsymbol{r}_u\times\boldsymbol{r}_v\ne\boldsymbol{0}$. Then the area of $S$ is

$$
\iint_{D_{uv}}\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\,\mathrm{d}u\,\mathrm{d}v=\iint_{D_{uv}}\sqrt{A^2+B^2+C^2}\,\mathrm{d}u\,\mathrm{d}v=\iint_{D_{uv}}\sqrt{EG-F^2}\,\mathrm{d}u\,\mathrm{d}v,
$$
where $A=\det\dfrac{\partial(y,z)}{\partial(u,v)}$, $B=\det\dfrac{\partial(z,x)}{\partial(u,v)}$, $C=\det\dfrac{\partial(x,y)}{\partial(u,v)}$ are the components of $\boldsymbol{r}_u\times\boldsymbol{r}_v$ (Definition 11.1.1 and the section on parametric surfaces in [2.2.11](/2.2.11)), and $E=\|\boldsymbol{r}_u\|^2$, $F=\boldsymbol{r}_u\cdot\boldsymbol{r}_v$, $G=\|\boldsymbol{r}_v\|^2$.

**Proof** A small rectangle $[u,u+\Delta u]\times[v,v+\Delta v]$ in the parameter domain is mapped to a small piece of the surface, which is approximately the parallelogram with sides $\boldsymbol{r}_u\Delta u$ and $\boldsymbol{r}_v\Delta v$ and area $\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\Delta u\Delta v$. This agrees with Definition 13.2.1: if $C\ne0$ on some piece, the **implicit function theorem** lets us write the surface as $z=z(x,y)$, with $z_x=-A/C$ and $z_y=-B/C$, and by the change of variables formula for **double integrals** (Theorem 12.4.1), $\mathrm{d}x\,\mathrm{d}y=|C|\,\mathrm{d}u\,\mathrm{d}v$, so

$$
\sqrt{1+z_x^2+z_y^2}\,\mathrm{d}x\,\mathrm{d}y=\frac{\sqrt{A^2+B^2+C^2}}{|C|}\,|C|\,\mathrm{d}u\,\mathrm{d}v.
$$
The identity $\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|^2=\|\boldsymbol{r}_u\|^2\|\boldsymbol{r}_v\|^2-(\boldsymbol{r}_u\cdot\boldsymbol{r}_v)^2$ is verified directly from the definition of the cross product. $\square$

For the sphere $\boldsymbol{r}(\varphi,\theta)=(R\sin\varphi\cos\theta,R\sin\varphi\sin\theta,R\cos\varphi)$ ($\rho=R$ in **spherical coordinates**), the area element is $\mathrm{d}S=R^2\sin\varphi\,\mathrm{d}\varphi\,\mathrm{d}\theta$, and the area of the sphere is $\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi R^2\sin\varphi\,\mathrm{d}\varphi=4\pi R^2$. If we instead project using $z=\sqrt{R^2-x^2-y^2}$, the area element $\frac{R}{\sqrt{R^2-x^2-y^2}}\,\mathrm{d}x\,\mathrm{d}y$ is unbounded at the equator and the double integral is an **improper integral**; the parametric approach avoids this problem.

**Example 13.2.1** Consider the sphere $x^2+y^2+z^2=a^2$ and the cylinder $x^2+y^2=ax$ ($a>0$).

(1) The area of the part of the sphere inside the cylinder. On the upper hemisphere $z_x=-\frac xz$ and $z_y=-\frac yz$, so $\sqrt{1+z_x^2+z_y^2}=\frac{a}{z}$; the projected region is $D\colon r\le a\cos\theta$, and

$$
S_1=2\iint_D\frac{a}{\sqrt{a^2-x^2-y^2}}\,\mathrm{d}\sigma=2\int_{-\pi/2}^{\pi/2}\mathrm{d}\theta\int_0^{a\cos\theta}\frac{ar}{\sqrt{a^2-r^2}}\,\mathrm{d}r=4a^2\int_0^{\pi/2}(1-\sin\theta)\,\mathrm{d}\theta=2a^2(\pi-2).
$$

(2) The area of the part of the cylinder inside the sphere was computed in Example 13.1.2 to be $4a^2$. To use projection instead: the cylinder is perpendicular to the $xy$-plane, onto which it projects to a curve, so it cannot be projected onto the $xy$-plane; write the cylinder as $y=\pm\sqrt{ax-x^2}$ and project onto the $zx$-plane, where eliminating $y$ from the intersection curve gives the projected region $z^2\le a(a-x)$, $0\le x\le a$. The result is the same.

**Example 13.2.2** The area of the part of the paraboloid of revolution $z=x^2+y^2$ cut off by $z=2$ (that is, over $(x,y)\in\{x^2+y^2\le2\}$) is

$$
\iint_{x^2+y^2\le2}\sqrt{1+4x^2+4y^2}\,\mathrm{d}x\,\mathrm{d}y=2\pi\int_0^{\sqrt2}\sqrt{1+4r^2}\,r\,\mathrm{d}r=\frac{\pi}{6}(1+4r^2)^{3/2}\Big|_0^{\sqrt2}=\frac{13\pi}3.
$$

### 13.2.2. Surface Integrals of Scalar Functions

**Definition 13.2.2 (Surface Integral of a Scalar Function)** Let $S\subset\mathbb{R}^3$ be a bounded smooth (or piecewise smooth) surface and $f$ a function defined on $S$. Divide $S$ arbitrarily into small pieces $S_1,\dots,S_n$, let $\Delta S_i$ be the area of $S_i$ and $\lambda$ the largest diameter of the pieces, and choose arbitrary $P_i\in S_i$. If $\lim\limits_{\lambda\to0}\sum_{i=1}^nf(P_i)\Delta S_i$ exists and does not depend on the partition or the sample points, it is called the **surface integral of a scalar function** $f$ over $S$, written $\iint_Sf(x,y,z)\,\mathrm{d}S$; when $S$ is a closed surface we write $\oiint_Sf\,\mathrm{d}S$.

For $f\equiv1$ the integral is the surface area, and when $f$ is a surface density it is the mass of the shell. The properties are the same as for line integrals of scalar functions: linearity, additivity over (pieces of) surfaces, monotonicity, independence of orientation, and symmetry, including symmetry under interchange of variables.

**Theorem 13.2.2** Let $f$ be continuous on $S$.

- If $S\colon z=z(x,y)$, $(x,y)\in D_{xy}$, then $\iint_Sf\,\mathrm{d}S=\iint_{D_{xy}}f(x,y,z(x,y))\sqrt{1+z_x^2+z_y^2}\,\mathrm{d}x\,\mathrm{d}y$.
- If $S\colon\boldsymbol{r}(u,v)$, $(u,v)\in D_{uv}$, then $\iint_Sf\,\mathrm{d}S=\iint_{D_{uv}}f(\boldsymbol{r}(u,v))\,\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\,\mathrm{d}u\,\mathrm{d}v$.

The proof is the same as for Theorem 13.1.1: the formula for the area element plus the mean value theorem for integrals. When projecting onto a coordinate plane, the projection must be one-to-one. If the surface has "two layers" in the direction of projection (as the sphere does over the $xy$-plane), it must be split into upper and lower pieces computed separately; if part of the surface is perpendicular to the plane of projection, that part cannot be projected onto it.

**Example 13.2.3** Let $S$ be the boundary of the tetrahedron $x+y+z\le1$, $x,y,z\ge0$. Evaluate $\oiint_S\dfrac{\mathrm{d}S}{(1+x+y)^2}$. We compute over the four faces. Bottom face $z=0$: $\mathrm{d}S=\mathrm{d}x\,\mathrm{d}y$, and

$$
\int_0^1\mathrm{d}x\int_0^{1-x}\frac{\mathrm{d}y}{(1+x+y)^2}=\int_0^1\Big(\frac1{1+x}-\frac12\Big)\mathrm{d}x=\ln2-\frac12.
$$
Slanted face $z=1-x-y$: $\mathrm{d}S=\sqrt3\,\mathrm{d}x\,\mathrm{d}y$, and the integral is $\sqrt3(\ln2-\frac12)$. Side face $x=0$: projecting onto the $yz$-plane, $\int_0^1\mathrm{d}y\int_0^{1-y}\frac{\mathrm{d}z}{(1+y)^2}=\int_0^1\frac{1-y}{(1+y)^2}\,\mathrm{d}y=1-\ln2$; likewise the side face $y=0$ gives $1-\ln2$. Hence

$$
\oiint_S\frac{\mathrm{d}S}{(1+x+y)^2}=(1+\sqrt3)\Big(\ln2-\frac12\Big)+2(1-\ln2)=(\sqrt3-1)\ln2+\frac{3-\sqrt3}2.
$$

**Example 13.2.4** Let $S$ be the part of the sphere $x^2+y^2+z^2=R^2$ with $z\ge0$. Evaluate $\iint_S(x+y+z)\,\mathrm{d}S$. $S$ is symmetric about the $yz$-plane and the $zx$-plane, and $x$, $y$ are odd in the respective variables, so $\iint_Sx\,\mathrm{d}S=\iint_Sy\,\mathrm{d}S=0$.

First solution (projection): $\mathrm{d}S=\frac Rz\,\mathrm{d}x\,\mathrm{d}y$, so $\iint_Sz\,\mathrm{d}S=\iint_{x^2+y^2\le R^2}R\,\mathrm{d}x\,\mathrm{d}y=\pi R^3$.

Second solution (parametrization): $\mathrm{d}S=R^2\sin\varphi\,\mathrm{d}\varphi\,\mathrm{d}\theta$, so $\iint_Sz\,\mathrm{d}S=\int_0^{2\pi}\mathrm{d}\theta\int_0^{\pi/2}R\cos\varphi\cdot R^2\sin\varphi\,\mathrm{d}\varphi=\pi R^3$.

The integral is therefore $\pi R^3$.

**Example 13.2.5** Find the centroid (the **center of mass** of a uniform shell) of the part of the cone $z=\sqrt{x^2+y^2}$ cut out by the cylinder $x^2+y^2=ax$ ($a>0$). Here $z_x^2+z_y^2=1$ and $\mathrm{d}S=\sqrt2\,\mathrm{d}x\,\mathrm{d}y$; the projected region $D\colon r\le a\cos\theta$ is a disk of radius $\frac a2$.

$$
\iint_S\mathrm{d}S=\frac{\sqrt2\pi a^2}4,\qquad\iint_Sx\,\mathrm{d}S=\sqrt2\iint_Dx\,\mathrm{d}\sigma=\sqrt2\cdot\frac{\pi a^2}4\cdot\frac a2,
$$

$$
\iint_Sz\,\mathrm{d}S=\sqrt2\int_{-\pi/2}^{\pi/2}\mathrm{d}\theta\int_0^{a\cos\theta}r^2\,\mathrm{d}r=\frac{\sqrt2a^3}3\int_{-\pi/2}^{\pi/2}\cos^3\theta\,\mathrm{d}\theta=\frac{4\sqrt2a^3}9.
$$
By symmetry $\bar y=0$, so the centroid is $\big(\frac a2,0,\frac{16a}{9\pi}\big)$.

**Example 13.2.6** Let $S$ be the boundary of the solid cylinder $x^2+y^2\le R^2$, $0\le z\le H$. Find $\oiint_S(x^2+y^2+z^2)\,\mathrm{d}S$ (the **moment of inertia** of a uniform shell about the origin). Bottom $z=0$: $\iint(x^2+y^2)\,\mathrm{d}x\,\mathrm{d}y=\frac{\pi R^4}2$; top $z=H$: $\frac{\pi R^4}2+\pi R^2H^2$; on the lateral surface use the cylindrical parametrization $x=R\cos\theta$, $y=R\sin\theta$, $z=z$, with $\mathrm{d}S=R\,\mathrm{d}\theta\,\mathrm{d}z$:

$$
\int_0^{2\pi}\mathrm{d}\theta\int_0^H(R^2+z^2)R\,\mathrm{d}z=2\pi R\Big(R^2H+\frac{H^3}3\Big).
$$
The total is $\pi R^4+2\pi R^3H+\pi R^2H^2+\frac23\pi RH^3$. The lateral surface can also be written as $x=\pm\sqrt{R^2-y^2}$ and projected onto the $yz$-plane (in front and back pieces); the result is the same, but the computation is more laborious.

## 13.3. Oriented Curves and Line Integrals of Vector Fields

### 13.3.1. Vector Fields and Oriented Curves

In physics, a region of space in which some physical phenomenon takes place is called a field. Temperature, density and electric potential take a number at each point; velocity, force and electric field strength take a vector at each point.

**Definition 13.3.1 (Scalar Field and Vector Field)** Let $\Omega\subset\mathbb{R}^3$ be a region. A function $f\colon\Omega\to\mathbb{R}$ defined on $\Omega$ is called a **scalar field** on $\Omega$; a map $\boldsymbol{v}\colon\Omega\to\mathbb{R}^3$,

$$
\boldsymbol{v}(x,y,z)=X(x,y,z)\boldsymbol{i}+Y(x,y,z)\boldsymbol{j}+Z(x,y,z)\boldsymbol{k}=(X,Y,Z),
$$
is called a **vector field** on $\Omega$. If $X,Y,Z$ are all continuous, $\boldsymbol{v}$ is called a continuous vector field; if $X,Y,Z$ all have continuous partial derivatives, $\boldsymbol{v}$ is called a continuously differentiable vector field. Plane vector fields $\boldsymbol{v}=(X(x,y),Y(x,y))$ are defined in the same way.

For example, the gravitational force exerted by a particle of mass $M$ at $P_0(x_0,y_0,z_0)$ on a particle of mass $m$ at $P(x,y,z)$ is

$$
\boldsymbol{F}(x,y,z)=-\frac{GMm}{\|\boldsymbol{r}\|^3}\boldsymbol{r},\qquad\boldsymbol{r}=(x-x_0,y-y_0,z-z_0),
$$
with magnitude $\frac{GMm}{\|\boldsymbol{r}\|^2}$, pointing toward $P_0$. It is a continuously differentiable vector field away from $P_0$.

**Definition 13.3.2 (Oriented Curve)** A curve with a designated initial point and terminal point (that is, with a designated direction of traversal) is called an **oriented curve**. The oriented curve traversed in the direction opposite to $L$ is denoted $L^-$. Unless stated otherwise, a curve given parametrically is oriented in the direction of increasing parameter, and a closed curve in the plane is oriented counterclockwise.

At each point of an oriented smooth curve $L$ there is a unit tangent vector $\boldsymbol{\tau}=(\cos\alpha,\cos\beta,\cos\gamma)$ pointing in the direction of traversal. If $L$ is given by a parametrization $\boldsymbol{r}(t)$ oriented in the direction of increasing parameter, then $\boldsymbol{\tau}=\boldsymbol{r}'(t)/\|\boldsymbol{r}'(t)\|$.

### 13.3.2. Definition and Properties

A constant force $\boldsymbol{F}$ that moves a particle through a straight displacement $\boldsymbol{s}$ does work $W=\boldsymbol{F}\cdot\boldsymbol{s}$. When a variable force $\boldsymbol{F}(x,y,z)$ moves a particle along an oriented curve $L$ from $A$ to $B$, divide $L$ into small pieces in the direction of traversal; the $i$-th piece is approximately the displacement $\Delta\boldsymbol{l}_i=(\Delta x_i,\Delta y_i,\Delta z_i)$, and the force is approximately the constant force $\boldsymbol{F}(P_i)$, so

$$
W=\lim_{\lambda\to0}\sum_{i=1}^n\boldsymbol{F}(P_i)\cdot\Delta\boldsymbol{l}_i=\lim_{\lambda\to0}\sum_{i=1}^n\boldsymbol{F}(P_i)\cdot\boldsymbol{\tau}(P_i)\Delta l_i.
$$
The limit of the last sum is precisely the line integral of the scalar function $\boldsymbol{F}\cdot\boldsymbol{\tau}$.

**Definition 13.3.3 (Line Integral of a Vector Field)** Let $\boldsymbol{v}=(X,Y,Z)$ be a continuous vector field on a region $\Omega\subset\mathbb{R}^3$, $L$ a piecewise smooth oriented curve in $\Omega$, and $\boldsymbol{\tau}$ the positively directed unit tangent vector of $L$. If the line integral $\int_L\boldsymbol{v}\cdot\boldsymbol{\tau}\,\mathrm{d}l$ of the scalar function $\boldsymbol{v}\cdot\boldsymbol{\tau}$ exists, it is called the **line integral of a vector field** $\boldsymbol{v}$ along the oriented curve $L$, written

$$
\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z,
$$
where $\mathrm{d}\boldsymbol{l}=\boldsymbol{\tau}\,\mathrm{d}l=(\mathrm{d}x,\mathrm{d}y,\mathrm{d}z)$ is called the oriented arc element. $\int_LX\,\mathrm{d}x$ is called the line integral of $X$ along $L$ with respect to $x$, and similarly for the others. When $L$ is a closed curve, $\oint_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$ is called the **circulation** of $\boldsymbol{v}$ around $L$.

Physically, when $\boldsymbol{F}$ is a force, the line integral is the work done; when $\boldsymbol{v}$ is the velocity of a fluid, the circulation measures how strongly the fluid rotates along $L$. The definition and the properties of line integrals of scalar functions immediately give:

**Property 13.3.1**

- Orientation: $\int_{L^-}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=-\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$ (reversing the orientation changes the sign of $\boldsymbol{\tau}$).
- Linearity, and additivity over paths: if $L$ consists of $L_1$ and $L_2$ joined end to end (with consistent orientations), then $\int_L=\int_{L_1}+\int_{L_2}$.
- Relation to line integrals of scalar functions: $\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z=\int_L(X\cos\alpha+Y\cos\beta+Z\cos\gamma)\,\mathrm{d}l$.

### 13.3.3. Evaluation

**Theorem 13.3.1** Let $L\colon\boldsymbol{r}(t)=(x(t),y(t),z(t))$ be an oriented smooth curve whose initial point corresponds to $t=\alpha$ and terminal point to $t=\beta$ ($\alpha$ may exceed $\beta$), and let $\boldsymbol{v}=(X,Y,Z)$ be continuous on $L$. Then

$$
\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z=\int_\alpha^\beta\big[X(\boldsymbol{r}(t))x'(t)+Y(\boldsymbol{r}(t))y'(t)+Z(\boldsymbol{r}(t))z'(t)\big]\,\mathrm{d}t.
$$

**Proof** Suppose $\alpha<\beta$. By Theorem 13.1.1 and $\boldsymbol{\tau}=\boldsymbol{r}'/\|\boldsymbol{r}'\|$,

$$
\int_L\boldsymbol{v}\cdot\boldsymbol{\tau}\,\mathrm{d}l=\int_\alpha^\beta\boldsymbol{v}(\boldsymbol{r}(t))\cdot\frac{\boldsymbol{r}'(t)}{\|\boldsymbol{r}'(t)\|}\,\|\boldsymbol{r}'(t)\|\,\mathrm{d}t=\int_\alpha^\beta\boldsymbol{v}(\boldsymbol{r}(t))\cdot\boldsymbol{r}'(t)\,\mathrm{d}t.
$$
If $\alpha>\beta$, then $\boldsymbol{\tau}=-\boldsymbol{r}'/\|\boldsymbol{r}'\|$, and replacing $\int_\beta^\alpha$ by $\int_\alpha^\beta$ changes the sign once more. $\square$

The method of computation is simply "substitution": substitute the equations of the curve into the integrand, with $\mathrm{d}x=x'(t)\,\mathrm{d}t$ and so on; the lower limit of the definite integral corresponds to the initial point and the upper limit to the terminal point. For a plane curve $y=y(x)$ from $x=a$ to $x=b$, $\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y=\int_a^b[X(x,y(x))+Y(x,y(x))y'(x)]\,\mathrm{d}x$.

**Example 13.3.1** (1) For $L\colon y=x^2$ from $x=0$ to $x=2$, $\int_L(x^2-y^2)\,\mathrm{d}x=\int_0^2(x^2-x^4)\,\mathrm{d}x=\frac83-\frac{32}5=-\frac{56}{15}$.

(2) Let $L$ be the upper half of the ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$, oriented counterclockwise (from $(a,0)$ to $(-a,0)$). With $x=a\cos t$, $y=b\sin t$, $t$ from $0$ to $\pi$:

$$
\int_L(x^2+2xy)\,\mathrm{d}y=\int_0^\pi(a^2\cos^2t+2ab\cos t\sin t)\,b\cos t\,\mathrm{d}t=0+2ab^2\int_0^\pi\cos^2t\sin t\,\mathrm{d}t=\frac43ab^2.
$$

**Example 13.3.2** Let $\boldsymbol{v}=y\boldsymbol{i}-x\boldsymbol{j}+(x+y+z)\boldsymbol{k}$, $A(a,0,0)$ and $B(a,0,c)$. Let $L_1$ be the helix $x=a\cos t$, $y=a\sin t$, $z=\frac{ct}{2\pi}$ from $A$ ($t=0$) to $B$ ($t=2\pi$), and $L_2$ the line segment from $A$ to $B$.

$$
\int_{L_1}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^{2\pi}\Big[-a^2\sin^2t-a^2\cos^2t+\Big(a\cos t+a\sin t+\frac{ct}{2\pi}\Big)\frac{c}{2\pi}\Big]\mathrm{d}t=-2\pi a^2+\frac{c^2}2,
$$
whereas on $L_2\colon x=a$, $y=0$, $z$ from $0$ to $c$, we get $\int_{L_2}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^c(a+z)\,\mathrm{d}z=ac+\frac{c^2}2$. The two paths have the same initial and terminal points, yet the integrals differ: in general, line integrals of vector fields depend on the path.

**Example 13.3.3** Let $\boldsymbol{u}=(2xy,x^2)$, $\boldsymbol{v}=(xy,y-x)$, and let $L_1,L_2,L_3$ be the curves from $(0,0)$ to $(1,1)$ along $y=x$, $y=x^2$ and $y=x^3$ respectively.

$$
\int_{L_1}\boldsymbol{u}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(2x^2+x^2)\,\mathrm{d}x=1,\quad\int_{L_2}\boldsymbol{u}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(2x^3+2x^3)\,\mathrm{d}x=1,\quad\int_{L_3}\boldsymbol{u}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(2x^4+3x^4)\,\mathrm{d}x=1;
$$

$$
\int_{L_1}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1x^2\,\mathrm{d}x=\frac13,\quad\int_{L_2}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(3x^3-2x^2)\,\mathrm{d}x=\frac1{12},\quad\int_{L_3}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_0^1(3x^5+x^4-3x^3)\,\mathrm{d}x=-\frac1{20}.
$$
The work done by $\boldsymbol{u}$ is the same along all three paths, while that done by $\boldsymbol{v}$ is not. The reason is that $\boldsymbol{u}$ is the **gradient** of the function $x^2y$: $\boldsymbol{u}\cdot\mathrm{d}\boldsymbol{l}=\mathrm{d}(x^2y)$, and the integral equals the difference of the values of $x^2y$ at the terminal and initial points. When a line integral is independent of the path is the subject of the section on conservative fields in [2.2.14](/2.2.14).

![Work done by two plane vector fields along three paths from (0,0) to (1,1): for the gradient field on the left it is independent of the path, for the field on the right it depends on the path](./plots/work-path-dependence.py)

**Example 13.3.4** Evaluate $\oint_L(x^2-2xy)\,\mathrm{d}x+(y^2-2xy)\,\mathrm{d}y$, where $L$ runs along straight segments from $(-1,1)$ to $(1,-1)$, then to $(1,1)$, and finally back to $(-1,1)$. On the first segment $y=-x$, $x$ from $-1$ to $1$: $\int_{-1}^1[(x^2+2x^2)-(x^2+2x^2)]\,\mathrm{d}x=0$; on the second $x=1$, $y$ from $-1$ to $1$: $\int_{-1}^1(y^2-2y)\,\mathrm{d}y=\frac23$; on the third $y=1$, $x$ from $1$ to $-1$: $\int_1^{-1}(x^2-2x)\,\mathrm{d}x=-\frac23$. The integral is therefore $0$.

**Example 13.3.5** Evaluate $\oint_Lx\,\mathrm{d}y-y\,\mathrm{d}x+(x+y)\,\mathrm{d}z$, where $L$ is the intersection of the hemisphere $z=\sqrt{1-x^2-y^2}$ with the cylinder $x^2+y^2=x$, oriented counterclockwise as seen from the positive $z$-axis. A parametrization is

$$
x=\frac12+\frac12\cos\theta,\quad y=\frac12\sin\theta,\quad z=\sqrt{1-x}=\sin\frac\theta2,\qquad0\le\theta\le2\pi,
$$
whose projection runs counterclockwise as $\theta$ increases. We have $x\,\mathrm{d}y-y\,\mathrm{d}x=\frac14(1+\cos\theta)\,\mathrm{d}\theta$ and $(x+y)\,\mathrm{d}z=\frac14(1+\cos\theta+\sin\theta)\cos\frac\theta2\,\mathrm{d}\theta=\frac14\big(2\cos^3\frac\theta2+2\sin\frac\theta2\cos^2\frac\theta2\big)\mathrm{d}\theta$, so

$$
\oint_L=\frac14\int_0^{2\pi}\Big(1+\cos\theta+2\cos^3\frac\theta2+2\sin\frac\theta2\cos^2\frac\theta2\Big)\mathrm{d}\theta=\frac14\Big(2\pi+0+\frac83\Big)=\frac\pi2+\frac23.
$$

**Example 13.3.6** A particle of mass $m$ sits at the origin, and a unit-mass particle moves under its attraction from $A(0,2)$ to $B(1,1)$: along $L_1$, the polygonal path $A\to C(1,2)\to B$, and along $L_2$, the minor arc of the circle $x^2+y^2=2y$ from $A$ to $B$. The gravitational force is $\boldsymbol{F}=-Gm\dfrac{(x,y)}{(x^2+y^2)^{3/2}}$, and the work is $W=-Gm\int_L\dfrac{x\,\mathrm{d}x+y\,\mathrm{d}y}{(x^2+y^2)^{3/2}}$. Along $L_1$:

$$
W_1=-Gm\int_0^1\frac{x\,\mathrm{d}x}{(x^2+4)^{3/2}}-Gm\int_2^1\frac{y\,\mathrm{d}y}{(1+y^2)^{3/2}}=Gm\Big[\Big(\frac1{\sqrt5}-\frac12\Big)+\Big(\frac1{\sqrt2}-\frac1{\sqrt5}\Big)\Big]=\frac{Gm}2(\sqrt2-1).
$$
Along $L_2$ ($x=\cos t$, $y=1+\sin t$, $t$ from $\frac\pi2$ to $0$): $W_2=Gm\int_0^{\pi/2}\frac{\cos t\,\mathrm{d}t}{(2+2\sin t)^{3/2}}=\frac{Gm}2(\sqrt2-1)=W_1$. In fact $\boldsymbol{F}=\nabla\frac{Gm}{\sqrt{x^2+y^2}}$, so the work equals $Gm\big(\frac1{|OB|}-\frac1{|OA|}\big)$ and depends only on the initial and terminal points: the gravitational field is a conservative field.

## 13.4. Green's Theorem

### 13.4.1. Simply Connected Domains and Orientation of the Boundary

**Definition 13.4.1 (Simply and Multiply Connected Domains)** Let $D\subset\mathbb{R}^2$ be a plane **region**. If for every simple closed curve in $D$ the bounded region it encloses is contained in $D$, then $D$ is called a **simply connected domain**; otherwise $D$ is called a **multiply connected domain**.

Intuitively, a simply connected domain has no "holes": disks and half-planes are simply connected, while the annulus $1<x^2+y^2<4$ and the punctured plane $\mathbb{R}^2\setminus\{0\}$ are multiply connected.

**Definition 13.4.2 (Positive Orientation of the Boundary)** Let $D$ be a bounded closed region whose boundary $\partial D$ consists of finitely many piecewise smooth simple closed curves. The positive orientation of $\partial D$ is the direction in which $D$ always lies to the left as one travels along it: the outer boundary is traversed counterclockwise and the inner boundaries clockwise.

![Positively oriented boundary of a multiply connected region: the outer boundary runs counterclockwise and the inner boundary clockwise, so that the region always lies to the left](./plots/green-region.py)

### 13.4.2. Green's Theorem

**Theorem 13.4.1 (Green's Theorem)** Let $D\subset\mathbb{R}^2$ be a bounded closed region whose boundary $\partial D$ consists of finitely many piecewise smooth simple closed curves, positively oriented, and let $X(x,y),Y(x,y)$ have continuous partial derivatives on $D$ (that is, on some open set containing $D$). Then

$$
\oint_{\partial D}X\,\mathrm{d}x+Y\,\mathrm{d}y=\iint_D\Big(\frac{\partial Y}{\partial x}-\frac{\partial X}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y.
$$

**Proof** (1) Let $D=\{(x,y)\mid a\le x\le b,\ y_1(x)\le y\le y_2(x)\}$. Reducing to an **iterated integral**,

$$
\iint_D\frac{\partial X}{\partial y}\,\mathrm{d}x\,\mathrm{d}y=\int_a^b\mathrm{d}x\int_{y_1(x)}^{y_2(x)}\frac{\partial X}{\partial y}\,\mathrm{d}y=\int_a^b\big[X(x,y_2(x))-X(x,y_1(x))\big]\mathrm{d}x.
$$
On the other hand, $\partial D$ consists of the lower edge $y=y_1(x)$ ($x$ from $a$ to $b$), the upper edge $y=y_2(x)$ ($x$ from $b$ to $a$) and two vertical segments, on which $\mathrm{d}x=0$; so $\oint_{\partial D}X\,\mathrm{d}x=\int_a^bX(x,y_1(x))\,\mathrm{d}x-\int_a^bX(x,y_2(x))\,\mathrm{d}x$. Hence $\oint_{\partial D}X\,\mathrm{d}x=-\iint_D\frac{\partial X}{\partial y}\,\mathrm{d}x\,\mathrm{d}y$.

(2) If $D$ can also be written as $\{c\le y\le d,\ x_1(y)\le x\le x_2(y)\}$, then similarly $\oint_{\partial D}Y\,\mathrm{d}y=\iint_D\frac{\partial Y}{\partial x}\,\mathrm{d}x\,\mathrm{d}y$, and adding the two identities gives the result.

(3) A general region is divided by finitely many auxiliary lines into pieces each of the type in (1) and (2). Apply Green's theorem to each piece and add: the double integrals add up to the integral over $D$; each auxiliary line appears once in the positively oriented boundaries of the two adjacent pieces, with opposite orientations, so the line integrals over it cancel, and what remains is exactly $\partial D$ with its positive orientation. Multiply connected regions are handled in the same way: auxiliary lines connecting the holes to the outer boundary cut the region into simply connected pieces. $\square$

Green's theorem relates a double integral over a region to a line integral over its boundary; like the Newton–Leibniz formula, it says "derivative inside = values on the boundary". Three points need attention when using it: the boundary must be positively oriented; $X,Y$ must have continuous partial derivatives at every point of $D$ (if $D$ contains a singularity, the theorem cannot be applied directly; see Example 13.4.6); and a curve that is not closed can be closed by adding a segment.

**Corollary 13.4.1 (Area Formula)** Under the hypotheses of Theorem 13.4.1, the area of $D$ is

$$
\sigma(D)=\oint_{\partial D}x\,\mathrm{d}y=-\oint_{\partial D}y\,\mathrm{d}x=\frac12\oint_{\partial D}x\,\mathrm{d}y-y\,\mathrm{d}x.
$$

For example, the area enclosed by the astroid $x=a\cos^3t$, $y=b\sin^3t$ ($0\le t\le2\pi$) is

$$
\frac12\int_0^{2\pi}(3ab\cos^4t\sin^2t+3ab\sin^4t\cos^2t)\,\mathrm{d}t=\frac{3ab}2\int_0^{2\pi}\sin^2t\cos^2t\,\mathrm{d}t=\frac{3\pi ab}8.
$$
The area of the ellipse $x=a\cos t$, $y=b\sin t$ is $\frac12\int_0^{2\pi}ab\,\mathrm{d}t=\pi ab$.

### 13.4.3. Applications

**Example 13.4.1** Let $L$ be the counterclockwise closed curve formed by the upper semicircle $y=\sqrt{a^2-x^2}$ and the diameter, and $D$ the half-disk. Then

$$
\oint_L(y^2+x)\,\mathrm{d}x+x^2\,\mathrm{d}y=\iint_D(2x-2y)\,\mathrm{d}x\,\mathrm{d}y=-2\iint_Dy\,\mathrm{d}x\,\mathrm{d}y=-\int_{-a}^a(a^2-x^2)\,\mathrm{d}x=-\frac43a^3,
$$
where $\iint_Dx\,\mathrm{d}x\,\mathrm{d}y=0$ by symmetry.

**Example 13.4.2** The polygonal path in Example 13.3.4 is the positively oriented boundary of the triangle $D$ with vertices $(-1,1),(1,-1),(1,1)$, so by Green's theorem

$$
\oint_L(x^2-2xy)\,\mathrm{d}x+(y^2-2xy)\,\mathrm{d}y=\iint_D(-2y+2x)\,\mathrm{d}x\,\mathrm{d}y=\int_{-1}^1\mathrm{d}x\int_{-x}^1(2x-2y)\,\mathrm{d}y=\int_{-1}^1(3x^2+2x-1)\,\mathrm{d}x=0,
$$
in agreement with the direct computation. Since $D$ is symmetric about the line $y=x$, symmetry under interchange of variables also shows directly that $\iint_D(x-y)\,\mathrm{d}x\,\mathrm{d}y=0$.

**Example 13.4.3 (Closing the Curve)** We redo Example 13.3.1 (2) by Green's theorem. Add $L_1$, the segment of the $x$-axis from $(-a,0)$ to $(a,0)$; together $L$ and $L_1$ form the positively oriented boundary of the upper half of the elliptical disk, $D$. Since $\mathrm{d}y=0$ on $L_1$,

$$
\int_L(x^2+2xy)\,\mathrm{d}y=\oint_{L+L_1}(x^2+2xy)\,\mathrm{d}y=\iint_D(2x+2y)\,\mathrm{d}x\,\mathrm{d}y=\iint_D2y\,\mathrm{d}x\,\mathrm{d}y.
$$
In **generalized polar coordinates** $x=ar\cos\theta$, $y=br\sin\theta$, $\mathrm{d}x\,\mathrm{d}y=abr\,\mathrm{d}r\,\mathrm{d}\theta$, the integral is $\int_0^\pi\mathrm{d}\theta\int_0^12br\sin\theta\cdot abr\,\mathrm{d}r=\frac43ab^2$.

**Example 13.4.4** Evaluate $I=\int_L(\mathrm{e}^x\sin y-3y+x^2)\,\mathrm{d}x+(\mathrm{e}^x\cos y-x)\,\mathrm{d}y$, where $L$ is the arc of the upper semicircle $x^2+y^2=a^2$ from $A(a,0)$ to $B(-a,0)$. Direct parametrization is laborious; add the diameter $L_1$ from $B$ to $A$, and let $D$ be the upper half-disk:

$$
I=\oint_{L+L_1}-\int_{L_1}=\iint_D\big[(\mathrm{e}^x\cos y-1)-(\mathrm{e}^x\cos y-3)\big]\mathrm{d}\sigma-\int_{-a}^ax^2\,\mathrm{d}x=\pi a^2-\frac23a^3.
$$
The part $\mathrm{e}^x\sin y\,\mathrm{d}x+\mathrm{e}^x\cos y\,\mathrm{d}y=\mathrm{d}(\mathrm{e}^x\sin y)$ of the integrand cancels in the difference of partial derivatives; this is a typical use of closing the curve.

**Example 13.4.5** Let $L\colon y=\sqrt{\pi^2-x^2}$ be oriented from $(\pi,0)$ to $(-\pi,0)$. Evaluate $I=\int_L(\sin x-x^2y)\,\mathrm{d}x+(\sin y+xy^2)\,\mathrm{d}y$. Add the segment $L_1$ from $(-\pi,0)$ to $(\pi,0)$ (on which $y=0$ and the integral is $\int_{-\pi}^\pi\sin x\,\mathrm{d}x=0$); then

$$
I=\iint_D(y^2+x^2)\,\mathrm{d}x\,\mathrm{d}y=\int_0^\pi\mathrm{d}\theta\int_0^\pi r^3\,\mathrm{d}r=\frac{\pi^5}4.
$$

**Example 13.4.6 (Excising a Singularity)** Let $L$ be a piecewise smooth simple closed curve not passing through the origin, oriented counterclockwise. Evaluate $I=\oint_L\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}$. Write $X=\frac{-y}{x^2+y^2}$ and $Y=\frac{x}{x^2+y^2}$; away from the origin,

$$
\frac{\partial Y}{\partial x}=\frac{y^2-x^2}{(x^2+y^2)^2}=\frac{\partial X}{\partial y}.
$$

- If $L$ does not enclose the origin, $X,Y$ are continuously differentiable on the closed region bounded by $L$, and Green's theorem gives $I=0$.
- If $L$ encloses the origin, Green's theorem cannot be applied directly. Choose $\varepsilon>0$ small enough that the circle $C_\varepsilon\colon x^2+y^2=\varepsilon^2$ lies inside the region bounded by $L$, and apply Green's theorem to the multiply connected region $D$ between $L$ and $C_\varepsilon$ (with $C_\varepsilon$ traversed clockwise): $\oint_L+\oint_{C_\varepsilon^-}=\iint_D0\,\mathrm{d}\sigma=0$. Therefore

$$
I=\oint_{C_\varepsilon}\frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}=\frac1{\varepsilon^2}\oint_{C_\varepsilon}x\,\mathrm{d}y-y\,\mathrm{d}x=\frac1{\varepsilon^2}\cdot2\pi\varepsilon^2=2\pi.
$$

For example, if $L$ is the ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ traversed clockwise, then $I=-2\pi$; computing directly with $x=a\cos t$, $y=b\sin t$ requires $-\int_0^{2\pi}\frac{ab\,\mathrm{d}t}{a^2\cos^2t+b^2\sin^2t}$, which also gives $-2\pi$ by the substitution $\tan t$, but with much more work. The value of the integral depends only on whether $L$ winds around the origin, not on the shape of $L$; geometrically it is the total angle swept out by $L$ around the origin ($\frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}$ is locally the differential $\mathrm{d}\theta$ of the polar angle).

**Example 13.4.7** For which smooth simple closed curve $L$ (oriented counterclockwise) is $I=\oint_L(y^3-y)\,\mathrm{d}x-2x^3\,\mathrm{d}y$ largest? By Green's theorem, $I=\iint_D(1-6x^2-3y^2)\,\mathrm{d}x\,\mathrm{d}y$, where $D$ is the region enclosed by $L$. The integrand is positive inside the ellipse $6x^2+3y^2<1$ and negative outside, so $I$ is largest when $D$ is exactly this elliptical disk, that is, when $L$ is the ellipse $6x^2+3y^2=1$.

### 13.4.4. The Flux Form of Green's Theorem

Let $\boldsymbol{v}=(X,Y)$ be the velocity of a plane fluid and $\boldsymbol{n}$ the outward unit normal vector of $\partial D$. The area of fluid leaving $D$ per unit time through a small piece $\mathrm{d}l$ of the boundary is $\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l$, so $\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l$ is the total outflow from $D$ per unit time.

**Theorem 13.4.2 (Flux Form of Green's Theorem)** Under the hypotheses of Theorem 13.4.1, let $\boldsymbol{v}=(X,Y)$ and let $\boldsymbol{n}$ be the outward unit normal vector of $\partial D$. Then

$$
\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l=\iint_D\Big(\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y.
$$

**Proof** Rotating the positively directed unit tangent vector $\boldsymbol{\tau}=(\cos\alpha,\sin\alpha)$ clockwise by $\frac\pi2$ gives the outward normal (the region lies to the left): $\boldsymbol{n}=(\sin\alpha,-\cos\alpha)$, so $\boldsymbol{n}\,\mathrm{d}l=(\mathrm{d}y,-\mathrm{d}x)$. Hence $\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l=\oint_{\partial D}-Y\,\mathrm{d}x+X\,\mathrm{d}y$, and Green's theorem applied to this gives the result. $\square$

The two forms say respectively that the circulation around the boundary equals the integral of $\frac{\partial Y}{\partial x}-\frac{\partial X}{\partial y}$ over the region, and that the outward flow equals the integral of $\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}$ over the region. These two integrands are the curl and the divergence of a plane vector field in [2.2.14](/2.2.14).

**Example 13.4.8** Let $f$ have continuous second-order partial derivatives on a bounded closed region $D$, and let $\frac{\partial f}{\partial\boldsymbol{n}}$ be the **directional derivative** of $f$ in the direction of the outward normal of $\partial D$. Then

$$
\oint_{\partial D}\frac{\partial f}{\partial\boldsymbol{n}}\,\mathrm{d}l=\iint_D\Big(\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}\Big)\mathrm{d}x\,\mathrm{d}y.
$$
Indeed $\frac{\partial f}{\partial\boldsymbol{n}}=\nabla f\cdot\boldsymbol{n}$; apply Theorem 13.4.2 to $\boldsymbol{v}=\nabla f=(f_x,f_y)$. In particular, for a function satisfying $f_{xx}+f_{yy}=0$, the integral of the normal derivative around any closed curve vanishes.

## 13.5. Oriented Surfaces and Surface Integrals of Vector Fields

### 13.5.1. Oriented Surfaces

A surface $S$ is called smooth if it has a nonzero normal vector $\boldsymbol{n}$ at every point and $\boldsymbol{n}$ varies continuously with the point. A smooth surface has two opposite unit normal vectors at each point; to discuss fluid flowing from one side of the surface to the other, we must be able to choose one of them continuously over the whole surface.

**Definition 13.5.1 (Oriented Surface)** Let $S$ be a smooth surface. If, for any point $M_0$ of $S$ and any unit normal vector at $M_0$, moving the point continuously from $M_0$ around any closed curve on $S$ that does not cross the boundary of $S$ and back to $M_0$, with the normal vector varying continuously along the way, always brings the normal vector back to the original one, then $S$ is called a two-sided surface. A two-sided surface with one side chosen (that is, with a continuous unit normal vector field $\boldsymbol{n}$ chosen) is called an **oriented surface**, and the side to which $\boldsymbol{n}$ points is called its positive side. The oriented surface with the orientation opposite to $S$ is denoted $S^-$.

Everyday surfaces (spheres, cylinders, graphs $z=f(x,y)$) are two-sided. The *Möbius strip* (a long strip of paper given a half twist and glued end to end) is a one-sided surface: after one trip around the center line, the normal vector has become its opposite, so the surface cannot be oriented; such surfaces are not considered in this course. Common conventions: a graph $z=z(x,y)$ has an upper side ($\cos\gamma>0$) and a lower side; a closed surface is oriented by its outer side; for a solid between two closed surfaces, the boundary is oriented by the outer side of the outer surface and the inner side of the inner surface (both pointing out of the solid).

The boundary curve of an oriented surface $S$ is oriented by the right-hand rule: a person standing on the positive side of the surface (head pointing along $\boldsymbol{n}$) walks along the boundary with the surface always on the left. This convention is used in Stokes' theorem in [2.2.14](/2.2.14); when $S$ is a region in the $xy$-plane with its upper side, it is the positive orientation of Definition 13.4.2.

### 13.5.2. Definition and Properties

Let an incompressible fluid have a time-independent velocity $\boldsymbol{v}(x,y,z)$; we want the volume of fluid flowing through an oriented surface $S$ (from the negative side to the positive side) per unit time. Divide $S$ into small pieces $\Delta S_i$, each approximately a flat piece with unit normal vector $\boldsymbol{n}(P_i)$, and approximate the velocity by the constant $\boldsymbol{v}(P_i)$. The fluid passing through the piece per unit time then fills an oblique prism of volume $\boldsymbol{v}(P_i)\cdot\boldsymbol{n}(P_i)\Delta S_i$, and the total flow is $\lim\sum\boldsymbol{v}\cdot\boldsymbol{n}\,\Delta S_i$.

**Definition 13.5.2 (Surface Integral of a Vector Field and Flux)** Let $\boldsymbol{v}=(X,Y,Z)$ be a continuous vector field on a region $\Omega\subset\mathbb{R}^3$, $S$ an oriented smooth (or piecewise smooth) surface in $\Omega$, and $\boldsymbol{n}$ its unit normal vector on the positive side. The surface integral $\iint_S\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}S$ of the scalar function $\boldsymbol{v}\cdot\boldsymbol{n}$ is called the **surface integral of a vector field** $\boldsymbol{v}$ over the oriented surface $S$, also called the **flux** of $\boldsymbol{v}$ through $S$, written

$$
\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iint_SX\,\mathrm{d}y\wedge\mathrm{d}z+Y\,\mathrm{d}z\wedge\mathrm{d}x+Z\,\mathrm{d}x\wedge\mathrm{d}y,
$$
where $\mathrm{d}\boldsymbol{S}=\boldsymbol{n}\,\mathrm{d}S$ is called the oriented area element. Writing $\boldsymbol{n}=(\cos\alpha,\cos\beta,\cos\gamma)$, we have $\mathrm{d}y\wedge\mathrm{d}z=\cos\alpha\,\mathrm{d}S$, $\mathrm{d}z\wedge\mathrm{d}x=\cos\beta\,\mathrm{d}S$ and $\mathrm{d}x\wedge\mathrm{d}y=\cos\gamma\,\mathrm{d}S$. An integral over a closed surface is written $\oiint_S$.

$\mathrm{d}x\wedge\mathrm{d}y$ is the oriented projection of the oriented area element onto the $xy$-plane: it equals the projected area element $\mathrm{d}x\,\mathrm{d}y$ when $\cos\gamma>0$, equals $-\mathrm{d}x\,\mathrm{d}y$ when $\cos\gamma<0$, and is zero when $\cos\gamma=0$ (the surface is perpendicular to the $xy$-plane). This differs from the always positive $\mathrm{d}x\,\mathrm{d}y$ of multiple integrals and is the most common source of errors in computation.

**Property 13.5.1**

- Orientation: $\iint_{S^-}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=-\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$.
- Linearity, and additivity over surfaces (when $S$ is split into pieces, each piece is oriented consistently with $S$).
- If $S$ is perpendicular to the $xy$-plane (for example, a cylinder with generators parallel to the $z$-axis), then $\iint_SZ\,\mathrm{d}x\wedge\mathrm{d}y=0$; similarly for the other coordinate planes.

### 13.5.3. Evaluation

**Theorem 13.5.1** Let $\boldsymbol{v}=(X,Y,Z)$ be continuous on an oriented smooth surface $S$.

(1) If $S\colon z=z(x,y)$, $(x,y)\in D_{xy}$, oriented by its upper side, then

$$
\iint_SZ\,\mathrm{d}x\wedge\mathrm{d}y=\iint_{D_{xy}}Z(x,y,z(x,y))\,\mathrm{d}x\,\mathrm{d}y,\qquad\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iint_{D_{xy}}\big(-Xz_x-Yz_y+Z\big)\,\mathrm{d}x\,\mathrm{d}y;
$$
for the lower side, both right-hand sides change sign. The cases $x=x(y,z)$ (front side positive) and $y=y(z,x)$ (right side positive) are similar.

(2) If $S\colon\boldsymbol{r}(u,v)$, $(u,v)\in D_{uv}$, then

$$
\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\pm\iint_{D_{uv}}\boldsymbol{v}(\boldsymbol{r}(u,v))\cdot(\boldsymbol{r}_u\times\boldsymbol{r}_v)\,\mathrm{d}u\,\mathrm{d}v=\pm\iint_{D_{uv}}(XA+YB+ZC)\,\mathrm{d}u\,\mathrm{d}v,
$$
with the plus sign if $\boldsymbol{r}_u\times\boldsymbol{r}_v=(A,B,C)$ points to the positive side and the minus sign otherwise.

**Proof** (2) By the definition and Theorem 13.2.2: the unit normal vector on the positive side is $\boldsymbol{n}=\pm\frac{\boldsymbol{r}_u\times\boldsymbol{r}_v}{\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|}$ and $\mathrm{d}S=\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\,\mathrm{d}u\,\mathrm{d}v$; multiply. (1) is the special case $u=x$, $v=y$ of (2): $\boldsymbol{r}_x\times\boldsymbol{r}_y=(-z_x,-z_y,1)$ points to the upper side. $\square$

Formula (1) shows that on an explicit surface, all three components of the flux can be computed by a single projection onto the $xy$-plane, with no need to project separately onto three coordinate planes.

**Algorithm 13.5.1 (Evaluating Surface Integrals of Vector Fields)** To compute $\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$:

1. First look for simplifications: if $S$ is closed, or becomes closed after adding a simple surface, consider the divergence theorem of [2.2.14](/2.2.14); use symmetry and the fact from Property 13.5.1 that "parts perpendicular to a coordinate plane contribute zero" to eliminate some terms.
2. Project term by term: for $\iint Z\,\mathrm{d}x\wedge\mathrm{d}y$, split $S$ into pieces each of which can be written $z=z(x,y)$ and projects one-to-one onto the $xy$-plane; convert each to a double integral with a plus or minus sign according to whether the positive normal of the piece makes an acute or obtuse angle with the $z$-axis. The other two terms are treated likewise.
3. Or project once: if $S$ is $z=z(x,y)$, use Theorem 13.5.1 (1), projecting only once.
4. Or parametrize: use Theorem 13.5.1 (2), with the sign determined by the direction of $\boldsymbol{r}_u\times\boldsymbol{r}_v$.
5. Or convert to a surface integral of a scalar function: find the unit normal vector $\boldsymbol{n}$ on the positive side and compute $\iint_S\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}S$; this is most efficient when $\boldsymbol{v}\cdot\boldsymbol{n}$ is simple on $S$ (for example, $\boldsymbol{n}=\frac{(x,y,z)}R$ on a sphere).

**Example 13.5.1** Let $f,g,h$ be continuous and let $S$ be the outer side of the boundary of the box $[0,a]\times[0,b]\times[0,c]$. Evaluate $\oiint_Sf(x)\,\mathrm{d}y\wedge\mathrm{d}z+g(y)\,\mathrm{d}z\wedge\mathrm{d}x+h(z)\,\mathrm{d}x\wedge\mathrm{d}y$. The term $\iint h(z)\,\mathrm{d}x\wedge\mathrm{d}y$ is nonzero only on the top and bottom faces: the top $z=c$, with its upper side, gives $abh(c)$; the bottom $z=0$, with its lower side, gives $-abh(0)$. The other two terms are similar, so

$$
\oiint_S=bc\big[f(a)-f(0)\big]+ca\big[g(b)-g(0)\big]+ab\big[h(c)-h(0)\big].
$$

**Example 13.5.2** Evaluate $\oiint_Sy^2z\,\mathrm{d}x\wedge\mathrm{d}y$, where $S$ is the outer side of the sphere $x^2+y^2+z^2=R^2$.

First solution (projection piece by piece): the upper hemisphere $z=\sqrt{R^2-x^2-y^2}$ has its upper side and the lower hemisphere $z=-\sqrt{R^2-x^2-y^2}$ its lower side. On the lower hemisphere $z<0$, and the lower side contributes another minus sign, so the two pieces give equal values (they do not cancel):

$$
\oiint_S=2\iint_{x^2+y^2\le R^2}y^2\sqrt{R^2-x^2-y^2}\,\mathrm{d}x\,\mathrm{d}y=2\int_0^{2\pi}\sin^2\theta\,\mathrm{d}\theta\int_0^Rr^3\sqrt{R^2-r^2}\,\mathrm{d}r=2\pi\cdot\frac{2R^5}{15}=\frac{4\pi R^5}{15}.
$$

Second solution (conversion to a scalar surface integral): the outward normal is $\boldsymbol{n}=\frac{(x,y,z)}R$ and $\boldsymbol{v}\cdot\boldsymbol{n}=\frac{y^2z^2}R$. With the spherical parametrization, $\mathrm{d}S=R^2\sin\varphi\,\mathrm{d}\varphi\,\mathrm{d}\theta$, and

$$
\oiint_S\frac{y^2z^2}R\,\mathrm{d}S=R^5\int_0^{2\pi}\sin^2\theta\,\mathrm{d}\theta\int_0^\pi\sin^3\varphi\cos^2\varphi\,\mathrm{d}\varphi=R^5\cdot\pi\cdot\frac4{15}=\frac{4\pi R^5}{15}.
$$

**Example 13.5.3** Evaluate $I=\iint_Sx(y-z)\,\mathrm{d}y\wedge\mathrm{d}z+(x-y)\,\mathrm{d}x\wedge\mathrm{d}y$, where $S$ is the outer side of the cylinder $x^2+y^2=1$ ($0\le z\le2$). Since $S$ is perpendicular to the $xy$-plane, $\iint_S(x-y)\,\mathrm{d}x\wedge\mathrm{d}y=0$.

First solution (projection piece by piece): the front half $x=\sqrt{1-y^2}$ has its front side (normal making an acute angle with the $x$-axis) and the back half $x=-\sqrt{1-y^2}$ its back side; both project onto $D\colon-1\le y\le1$, $0\le z\le2$:

$$
I=\iint_D\sqrt{1-y^2}(y-z)\,\mathrm{d}y\,\mathrm{d}z-\iint_D\big(-\sqrt{1-y^2}\big)(y-z)\,\mathrm{d}y\,\mathrm{d}z=2\int_{-1}^1\sqrt{1-y^2}\,\mathrm{d}y\int_0^2(y-z)\,\mathrm{d}z=2\int_{-1}^1\sqrt{1-y^2}(2y-2)\,\mathrm{d}y=-2\pi.
$$

Second solution (conversion to a scalar surface integral): $\boldsymbol{n}=(x,y,0)$ and $\boldsymbol{v}\cdot\boldsymbol{n}=x^2(y-z)$; on the lateral surface $x=\cos\theta$, $y=\sin\theta$, $\mathrm{d}S=\mathrm{d}\theta\,\mathrm{d}z$:

$$
I=\int_0^2\mathrm{d}z\int_0^{2\pi}\cos^2\theta(\sin\theta-z)\,\mathrm{d}\theta=\int_0^2(-\pi z)\,\mathrm{d}z=-2\pi.
$$

**Example 13.5.4** Evaluate $I=\iint_S(y-z)\,\mathrm{d}y\wedge\mathrm{d}z+(z-x)\,\mathrm{d}z\wedge\mathrm{d}x+(x-y)\,\mathrm{d}x\wedge\mathrm{d}y$, where $S$ is the outer (lower) side of the cone $z=\sqrt{x^2+y^2}$ ($0\le z\le h$). By Theorem 13.5.1 (1), with $z_x=\frac xz$, $z_y=\frac yz$ and the lower side:

$$
I=-\iint_{x^2+y^2\le h^2}\Big[-(y-z)\frac xz-(z-x)\frac yz+(x-y)\Big]\mathrm{d}x\,\mathrm{d}y=-\iint_{x^2+y^2\le h^2}2(x-y)\,\mathrm{d}x\,\mathrm{d}y=0,
$$
since the bracket equals $\frac{-xy+xz-yz+xy}{z}+(x-y)=2(x-y)$, whose integral vanishes by symmetry. This can also be seen term by term: for $\iint(y-z)\,\mathrm{d}y\wedge\mathrm{d}z$, the front and back pieces have the same projected region and the same integrand but opposite signs, so they cancel; the other two terms are similar.

**Example 13.5.5** A unit point charge at the origin produces the electric field $\boldsymbol{E}=k\dfrac{(x,y,z)}{(x^2+y^2+z^2)^{3/2}}$ at $(x,y,z)$. Its electric flux through the sphere $x^2+y^2+z^2=R^2$ (outer side) is

$$
\oiint_S\boldsymbol{E}\cdot\boldsymbol{n}\,\mathrm{d}S=\oiint_Sk\frac{(x,y,z)}{R^3}\cdot\frac{(x,y,z)}R\,\mathrm{d}S=\frac k{R^2}\oiint_S\mathrm{d}S=4\pi k,
$$
independent of the radius. This is the simplest case of Gauss's law in electromagnetism; [2.2.14](/2.2.14) shows that it holds for every closed surface enclosing the charge.

**Example 13.5.6** Evaluate $\oiint_S\dfrac{\mathrm{d}y\wedge\mathrm{d}z}x+\dfrac{\mathrm{d}z\wedge\mathrm{d}x}y+\dfrac{\mathrm{d}x\wedge\mathrm{d}y}z$, where $S$ is the outer side of the ellipsoid $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$. With the parametrization $x=a\sin\varphi\cos\theta$, $y=b\sin\varphi\sin\theta$, $z=c\cos\varphi$,

$$
\boldsymbol{r}_\varphi\times\boldsymbol{r}_\theta=(bc\sin^2\varphi\cos\theta,\ ca\sin^2\varphi\sin\theta,\ ab\sin\varphi\cos\varphi)=abc\sin\varphi\Big(\frac x{a^2},\frac y{b^2},\frac z{c^2}\Big),
$$
which points outward. With $\boldsymbol{v}=\big(\frac1x,\frac1y,\frac1z\big)$ we get $\boldsymbol{v}\cdot(\boldsymbol{r}_\varphi\times\boldsymbol{r}_\theta)=abc\sin\varphi\big(\frac1{a^2}+\frac1{b^2}+\frac1{c^2}\big)$, so the integral is

$$
abc\Big(\frac1{a^2}+\frac1{b^2}+\frac1{c^2}\Big)\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\sin\varphi\,\mathrm{d}\varphi=4\pi abc\Big(\frac1{a^2}+\frac1{b^2}+\frac1{c^2}\Big).
$$
The integrand is undefined on the coordinate planes, but the surface integral converges as an improper integral; after parametrization the singularities disappear automatically.

**Example 13.5.7** Let $S\colon z=xy$, $|x|\le1$, $|y|\le1$, with its upper side. Evaluate $I=\iint_S\mathrm{e}^y\,\mathrm{d}y\wedge\mathrm{d}z+\mathrm{e}^x\,\mathrm{d}z\wedge\mathrm{d}x+\mathrm{d}x\wedge\mathrm{d}y$. By Theorem 13.5.1 (1), with $z_x=y$ and $z_y=x$,

$$
I=\iint_{[-1,1]^2}\big(-y\mathrm{e}^y-x\mathrm{e}^x+1\big)\,\mathrm{d}x\,\mathrm{d}y=-2\int_{-1}^1y\mathrm{e}^y\,\mathrm{d}y-2\int_{-1}^1x\mathrm{e}^x\,\mathrm{d}x+4=4-\frac8{\mathrm{e}},
$$
where $\int_{-1}^1x\mathrm{e}^x\,\mathrm{d}x=(x-1)\mathrm{e}^x\big|_{-1}^1=\frac2{\mathrm{e}}$.

![The surface z = xy and its unit normal vector field on the upper side: the normal varies continuously, and choosing a side makes the surface an oriented surface](./plots/oriented-surface.py)

## Summary

Comparison of the four kinds of line and surface integrals:

| | Line integral of a scalar function | Line integral of a vector field | Surface integral of a scalar function | Surface integral of a vector field |
|---|---|---|---|---|
| Integrand | Scalar function $f$ | Vector field $\boldsymbol{v}$ | Scalar function $f$ | Vector field $\boldsymbol{v}$ |
| Notation | $\int_Lf\,\mathrm{d}l$ | $\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_LX\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z$ | $\iint_Sf\,\mathrm{d}S$ | $\iint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iint_SX\,\mathrm{d}y\wedge\mathrm{d}z+\cdots$ |
| Orientation | None | Sign changes when reversed | None | Sign changes with the side |
| Physical meaning | Mass, arc length | Work, circulation | Mass, area | Flux (rate of flow) |
| Element | $\mathrm{d}l=\Vert\boldsymbol{r}'(t)\Vert\,\mathrm{d}t$ | $\mathrm{d}\boldsymbol{l}=\boldsymbol{r}'(t)\,\mathrm{d}t$ | $\mathrm{d}S=\Vert\boldsymbol{r}_u\times\boldsymbol{r}_v\Vert\,\mathrm{d}u\,\mathrm{d}v$ | $\mathrm{d}\boldsymbol{S}=\pm\boldsymbol{r}_u\times\boldsymbol{r}_v\,\mathrm{d}u\,\mathrm{d}v$ |
| Reduces to | Definite integral, lower limit $<$ upper limit | Definite integral, lower limit at the initial point | Double integral | Double integral, sign by the side |
| Relation between the two kinds | | $\int_L\boldsymbol{v}\cdot\boldsymbol{\tau}\,\mathrm{d}l$ | | $\iint_S\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}S$ |

The two forms of Green's theorem ($\boldsymbol{v}=(X,Y)$, $\partial D$ positively oriented, $\boldsymbol{n}$ the outward normal):

| Form | Formula | Physical meaning |
|---|---|---|
| Circulation form | $\oint_{\partial D}X\,\mathrm{d}x+Y\,\mathrm{d}y=\iint_D(Y_x-X_y)\,\mathrm{d}\sigma$ | Circulation around the boundary = total rotation inside |
| Flux form | $\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l=\iint_D(X_x+Y_y)\,\mathrm{d}\sigma$ | Outward flow = total source strength inside |
| Area | $\sigma(D)=\frac12\oint_{\partial D}x\,\mathrm{d}y-y\,\mathrm{d}x$ | |

Common methods for plane line integrals of vector fields: parametrize directly; for closed curves use Green's theorem, and for curves that are not closed add a segment; excise a small disk around a singularity; when the integral is independent of the path, switch to a simpler path or use a potential ([2.2.14](/2.2.14)).
