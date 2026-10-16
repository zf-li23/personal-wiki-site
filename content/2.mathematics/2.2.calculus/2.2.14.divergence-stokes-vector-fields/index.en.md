---
title: The Divergence Theorem, Stokes' Theorem and Vector Fields
source_hash: 79df51f9a207
---

Green's theorem in [2.2.13](/2.2.13) relates a double integral over a plane region to a **line integral of a vector field** around its boundary. This chapter extends it to space: the divergence theorem relates a triple integral over a spatial region to a **surface integral of a vector field** over its closed boundary surface, and Stokes' theorem relates a surface integral of a vector field over a surface to a line integral around its boundary curve. The three theorems share a common form, "the integral of a certain derivative over a region equals an integral over its boundary", in direct line of descent from the one-variable **fundamental theorem of calculus**; in modern mathematics they are unified in the general Stokes theorem for differential forms, $\int_M\mathrm{d}\omega=\int_{\partial M}\omega$.

The "certain derivatives" in these formulas are the divergence and the curl of a vector field. The divergence is the outward **flux** per unit volume and measures the "sources" of the field; the components of the curl are **circulations** per unit area and measure the "vortices" of the field. The three operations gradient, divergence and curl let us classify vector fields: conservative fields, whose line integrals are independent of the path (gravitational and electrostatic fields); solenoidal fields, which have no sources (the velocity field of an incompressible fluid, the magnetic field); and harmonic fields, which are both. Conservative fields recast the "antiderivatives of differential forms" of [2.2.10](/2.2.10) in the language of vector fields, and they are the mathematical basis of potential energy and conservation of energy in physics. The formulas of this chapter are basic tools of electromagnetism (Maxwell's equations in integral and differential form), fluid mechanics and partial differential equations (the Laplace equation, the heat equation).

## 14.1. Gradient, Divergence and Curl

### 14.1.1. The Nabla Operator and the Gradient

Throughout this section $f,g$ are **scalar fields** and $\boldsymbol{u},\boldsymbol{v}$ are **vector fields** (Definition 13.3.1), with $\boldsymbol{v}=(X,Y,Z)=X\boldsymbol{i}+Y\boldsymbol{j}+Z\boldsymbol{k}$; all partial derivatives involved are assumed to be continuous.

**Definition 14.1.1 (Nabla Operator)** The formal vector

$$
\nabla=\frac{\partial}{\partial x}\boldsymbol{i}+\frac{\partial}{\partial y}\boldsymbol{j}+\frac{\partial}{\partial z}\boldsymbol{k}
$$
is called the **nabla operator** (also the del operator or Hamilton operator). Applied to a scalar field it gives the **gradient** $\operatorname{grad}f=\nabla f=(f_x,f_y,f_z)$ (Definition 10.6.2), an operation taking scalar fields to vector fields.

The gradient obeys the same rules as the derivative in one variable: $\nabla(\alpha f+\beta g)=\alpha\nabla f+\beta\nabla g$, $\nabla(fg)=f\nabla g+g\nabla f$, $\nabla\big(\frac fg\big)=\frac{g\nabla f-f\nabla g}{g^2}$ and $\nabla\varphi(f)=\varphi'(f)\nabla f$. If $\boldsymbol{v}=\nabla f$, then $f$ is called a potential function of $\boldsymbol{v}$ (Section 14.4).

### 14.1.2. Divergence

**Definition 14.1.2 (Divergence)** The **divergence** of a vector field $\boldsymbol{v}=(X,Y,Z)$ is the scalar field

$$
\operatorname{div}\boldsymbol{v}=\nabla\cdot\boldsymbol{v}=\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}.
$$
The divergence of a plane vector field $\boldsymbol{v}=(X,Y)$ is $\operatorname{div}\boldsymbol{v}=\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}$.

The notation "$\nabla\cdot$" is purely formal: it treats $\nabla$ as a vector and takes its **inner product** with $\boldsymbol{v}$. The physical meaning of the divergence (flux per unit volume) is derived from the divergence theorem in 14.2.3.

**Property 14.1.1** $\nabla\cdot(\alpha\boldsymbol{u}+\beta\boldsymbol{v})=\alpha\nabla\cdot\boldsymbol{u}+\beta\nabla\cdot\boldsymbol{v}$ and $\nabla\cdot(f\boldsymbol{v})=f\,\nabla\cdot\boldsymbol{v}+\nabla f\cdot\boldsymbol{v}$.

**Proof** Write $\boldsymbol{v}=(v_1,v_2,v_3)$. By the product rule, $\frac{\partial(fv_1)}{\partial x}+\frac{\partial(fv_2)}{\partial y}+\frac{\partial(fv_3)}{\partial z}=f\Big(\frac{\partial v_1}{\partial x}+\frac{\partial v_2}{\partial y}+\frac{\partial v_3}{\partial z}\Big)+\Big(v_1\frac{\partial f}{\partial x}+v_2\frac{\partial f}{\partial y}+v_3\frac{\partial f}{\partial z}\Big)$. $\square$

### 14.1.3. Curl

**Definition 14.1.3 (Curl)** The **curl** of a vector field $\boldsymbol{v}=(X,Y,Z)$ is the vector field

$$
\operatorname{curl}\boldsymbol{v}=\nabla\times\boldsymbol{v}=\begin{vmatrix}\boldsymbol{i}&\boldsymbol{j}&\boldsymbol{k}\\ \dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\ X&Y&Z\end{vmatrix}=\Big(\frac{\partial Z}{\partial y}-\frac{\partial Y}{\partial z},\ \frac{\partial X}{\partial z}-\frac{\partial Z}{\partial x},\ \frac{\partial Y}{\partial x}-\frac{\partial X}{\partial y}\Big).
$$
A plane vector field $\boldsymbol{v}=(X(x,y),Y(x,y))$ is regarded as $(X,Y,0)$, and its curl is $\operatorname{curl}\boldsymbol{v}=\Big(\dfrac{\partial Y}{\partial x}-\dfrac{\partial X}{\partial y}\Big)\boldsymbol{k}$.

The determinant is expanded along the first row, with "multiplying" an entry of the second row by one of the third row understood as taking a partial derivative (a formal extension of the cross product formula, Definition 11.1.1). Many texts, particularly in the Continental European tradition, write $\operatorname{rot}\boldsymbol{v}$ instead.

**Property 14.1.2**

- $\nabla\times(\alpha\boldsymbol{u}+\beta\boldsymbol{v})=\alpha\nabla\times\boldsymbol{u}+\beta\nabla\times\boldsymbol{v}$;
- $\nabla\times(f\boldsymbol{v})=f\,\nabla\times\boldsymbol{v}+\nabla f\times\boldsymbol{v}$;
- $\nabla\cdot(\boldsymbol{u}\times\boldsymbol{v})=\boldsymbol{v}\cdot(\nabla\times\boldsymbol{u})-\boldsymbol{u}\cdot(\nabla\times\boldsymbol{v})$.

**Proof** The first component of the second identity is $\frac{\partial(fv_3)}{\partial y}-\frac{\partial(fv_2)}{\partial z}=f\big(\frac{\partial v_3}{\partial y}-\frac{\partial v_2}{\partial z}\big)+\big(\frac{\partial f}{\partial y}v_3-\frac{\partial f}{\partial z}v_2\big)$, and the last term is exactly the first component of $\nabla f\times\boldsymbol{v}$; the other components are similar. Third identity: $\boldsymbol{u}\times\boldsymbol{v}=(u_2v_3-u_3v_2,\,u_3v_1-u_1v_3,\,u_1v_2-u_2v_1)$; take the divergence and expand by the product rule. Collecting the terms containing derivatives of $\boldsymbol{u}$ gives $v_1\big(\frac{\partial u_3}{\partial y}-\frac{\partial u_2}{\partial z}\big)+v_2\big(\frac{\partial u_1}{\partial z}-\frac{\partial u_3}{\partial x}\big)+v_3\big(\frac{\partial u_2}{\partial x}-\frac{\partial u_1}{\partial y}\big)=\boldsymbol{v}\cdot(\nabla\times\boldsymbol{u})$, and collecting those containing derivatives of $\boldsymbol{v}$ gives $-\boldsymbol{u}\cdot(\nabla\times\boldsymbol{v})$. $\square$

**Example 14.1.1** For $\boldsymbol{v}=(y,z,x)$: $\operatorname{div}\boldsymbol{v}=0$ and $\operatorname{curl}\boldsymbol{v}=(0-1,\,0-1,\,0-1)=(-1,-1,-1)$. For $\boldsymbol{v}=(y^2,z^2,x^2)$: $\operatorname{div}\boldsymbol{v}=0$ and $\operatorname{curl}\boldsymbol{v}=(-2z,-2x,-2y)$. For a rigid body rotating about the $z$-axis with angular velocity $\omega$, the velocity field $\boldsymbol{v}=\omega(-y,x,0)$ has curl $(0,0,2\omega)$: the curl points along the axis of rotation, and its magnitude is twice the angular velocity.

### 14.1.4. Second-Order Operations and the Laplace Operator

**Theorem 14.1.1** If $f$ and the components of $\boldsymbol{v}$ have continuous second-order partial derivatives, then

$$
\operatorname{curl}\operatorname{grad}f=\nabla\times\nabla f=\boldsymbol{0},\qquad\operatorname{div}\operatorname{curl}\boldsymbol{v}=\nabla\cdot(\nabla\times\boldsymbol{v})=0.
$$

**Proof** The first component of $\nabla\times\nabla f$ is $f_{zy}-f_{yz}=0$ (Theorem 10.4.1: continuous mixed partial derivatives are equal), and similarly for the others. Also $\nabla\cdot(\nabla\times\boldsymbol{v})=(Z_{yx}-Y_{zx})+(X_{zy}-Z_{xy})+(Y_{xz}-X_{yz})=0$. $\square$

Formally, these correspond to the identities $\boldsymbol{a}\times\boldsymbol{a}=\boldsymbol{0}$ and $\boldsymbol{a}\cdot(\boldsymbol{a}\times\boldsymbol{b})=0$ of vector algebra. Sections 14.4 and 14.5 discuss the converses: is an irrotational field a gradient field, and is a solenoidal field a curl? The answers depend on the shape of the region.

**Definition 14.1.4 (Laplace Operator)** The expression

$$
\Delta f=\nabla\cdot\nabla f=\operatorname{div}\operatorname{grad}f=\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}+\frac{\partial^2f}{\partial z^2}
$$
is called the Laplacian of $f$, and $\Delta=\nabla^2$ is called the **Laplace operator**.

In the language of curl and divergence, the two forms of Green's theorem (Theorems 13.4.1 and 13.4.2) read

$$
\oint_{\partial D}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_D(\operatorname{curl}\boldsymbol{v})\cdot\boldsymbol{k}\,\mathrm{d}\sigma,\qquad\oint_{\partial D}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}l=\iint_D\operatorname{div}\boldsymbol{v}\,\mathrm{d}\sigma.
$$
The next two sections extend them to space: the latter becomes the divergence theorem and the former becomes Stokes' theorem.

## 14.2. The Divergence Theorem

### 14.2.1. The Divergence Theorem

**Theorem 14.2.1 (Divergence Theorem)** Let $\Omega\subset\mathbb{R}^3$ be a bounded closed region whose boundary $\partial\Omega$ consists of finitely many smooth surfaces, oriented by the outer side, and let $\boldsymbol{v}=(X,Y,Z)$ be continuously differentiable on $\Omega$. Then

$$
\oiint_{\partial\Omega}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iiint_\Omega\operatorname{div}\boldsymbol{v}\,\mathrm{d}V,
$$
that is,

$$
\oiint_{\partial\Omega}X\,\mathrm{d}y\wedge\mathrm{d}z+Y\,\mathrm{d}z\wedge\mathrm{d}x+Z\,\mathrm{d}x\wedge\mathrm{d}y=\iiint_\Omega\Big(\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}\Big)\mathrm{d}V.
$$

**Proof** It suffices to prove $\oiint_{\partial\Omega}Z\,\mathrm{d}x\wedge\mathrm{d}y=\iiint_\Omega\frac{\partial Z}{\partial z}\,\mathrm{d}V$; the other two are similar. First let $\Omega=\{(x,y,z)\mid(x,y)\in D_{xy},\ z_1(x,y)\le z\le z_2(x,y)\}$. By the projection method for **triple integrals** (Theorem 12.3.1),

$$
\iiint_\Omega\frac{\partial Z}{\partial z}\,\mathrm{d}V=\iint_{D_{xy}}\Big(\int_{z_1}^{z_2}\frac{\partial Z}{\partial z}\,\mathrm{d}z\Big)\mathrm{d}x\,\mathrm{d}y=\iint_{D_{xy}}\big[Z(x,y,z_2(x,y))-Z(x,y,z_1(x,y))\big]\mathrm{d}x\,\mathrm{d}y.
$$
On the other hand, $\partial\Omega$ consists of the top $z=z_2$ (whose outer side is the upper side), the bottom $z=z_1$ (whose outer side is the lower side) and the lateral surface (perpendicular to the $xy$-plane, so $\mathrm{d}x\wedge\mathrm{d}y=0$); by Theorem 13.5.1, $\oiint_{\partial\Omega}Z\,\mathrm{d}x\wedge\mathrm{d}y$ equals exactly the right side above. A general region is divided by auxiliary surfaces into finitely many pieces of this type; each auxiliary surface carries opposite orientations in the two adjacent pieces, so the integrals over it cancel. $\square$

The divergence theorem is also called Gauss's theorem (or the Gauss–Ostrogradsky theorem). In the plane it is the flux form of Green's theorem. When using it, note that $\partial\Omega$ is oriented by the outer side (if $\Omega$ has cavities, the inner boundary surfaces are oriented by their inner sides, which still point out of $\Omega$), and that $\boldsymbol{v}$ must be continuously differentiable at every point of $\Omega$. Taking $\boldsymbol{v}=\frac13(x,y,z)$ expresses volume as a surface integral: $V(\Omega)=\frac13\oiint_{\partial\Omega}x\,\mathrm{d}y\wedge\mathrm{d}z+y\,\mathrm{d}z\wedge\mathrm{d}x+z\,\mathrm{d}x\wedge\mathrm{d}y$. For a ball of radius $R$, for instance, $\boldsymbol{v}\cdot\boldsymbol{n}=\frac R3$ and $V=\frac R3\cdot4\pi R^2=\frac43\pi R^3$.

### 14.2.2. Applications

**Example 14.2.1** Let $\Omega=\{x^2+y^2\le1,\ 0\le z\le1\}$. Evaluate $\oiint_{\partial\Omega}(x^3+\sin yz)\,\mathrm{d}y\wedge\mathrm{d}z+(y^3+\mathrm{e}^{xz})\,\mathrm{d}z\wedge\mathrm{d}x+\big[3z+\ln(x^2+y^2+1)\big]\,\mathrm{d}x\wedge\mathrm{d}y$ (outer side). A direct computation is hopeless, but the divergence is $3x^2+3y^2+3$, and in **cylindrical coordinates**

$$
\iiint_\Omega3(x^2+y^2+1)\,\mathrm{d}V=3\int_0^{2\pi}\mathrm{d}\theta\int_0^1(r^2+1)r\,\mathrm{d}r\int_0^1\mathrm{d}z=\frac{9\pi}2.
$$

**Example 14.2.2** We redo Example 13.5.2 with the divergence theorem: $\oiint_Sy^2z\,\mathrm{d}x\wedge\mathrm{d}y=\iiint_{x^2+y^2+z^2\le R^2}y^2\,\mathrm{d}V=\frac13\iiint\rho^2\,\mathrm{d}V=\frac13\cdot\frac{4\pi R^5}5=\frac{4\pi R^5}{15}$ (by symmetry under interchange of variables, $\iiint x^2=\iiint y^2=\iiint z^2$).

**Example 14.2.3 (Closing the Surface)** We redo Example 13.5.4 (the cone $S\colon z=\sqrt{x^2+y^2}$, $0\le z\le h$, outer side) with the divergence theorem. Add the disk $S_1\colon z=h$, $x^2+y^2\le h^2$, with its upper side; $S+S_1$ is the outward-oriented boundary of the solid cone $\Omega$. The field $\boldsymbol{v}=(y-z,z-x,x-y)$ has divergence $0$, so

$$
\iint_S=\oiint_{S+S_1}-\iint_{S_1}=0-\iint_{x^2+y^2\le h^2}(x-y)\,\mathrm{d}x\,\mathrm{d}y=0.
$$
Likewise, closing Example 13.5.3 with the top and bottom disks gives $\oiint=\iiint_\Omega(y-z)\,\mathrm{d}V=-\iiint_\Omega z\,\mathrm{d}V=-2\pi$; on the two disks $\iint(x-y)\,\mathrm{d}x\,\mathrm{d}y=0$ and $\mathrm{d}y\wedge\mathrm{d}z=0$, so the integral is $-2\pi$, in agreement with the direct computation.

**Example 14.2.4** Evaluate $I=\iint_S(y^2-x)\,\mathrm{d}y\wedge\mathrm{d}z+(z^2-y)\,\mathrm{d}z\wedge\mathrm{d}x+(x^2-z)\,\mathrm{d}x\wedge\mathrm{d}y$, where $S\colon z=1-x^2-y^2$, $z\ge0$, with its upper side. Add $S_1\colon z=0$, $x^2+y^2\le1$, with its lower side, and let $\Omega$ be the solid bounded by the paraboloid and the plane. The divergence is $-3$ and $V(\Omega)=\int_0^{2\pi}\mathrm{d}\theta\int_0^1(1-r^2)r\,\mathrm{d}r=\frac\pi2$, so $\oiint_{S+S_1}=-\frac{3\pi}2$. On $S_1$ we have $z=0$ and $\mathrm{d}y\wedge\mathrm{d}z=\mathrm{d}z\wedge\mathrm{d}x=0$, so

$$
\iint_{S_1}x^2\,\mathrm{d}x\wedge\mathrm{d}y=-\iint_{x^2+y^2\le1}x^2\,\mathrm{d}x\,\mathrm{d}y=-\frac\pi4,\qquad I=-\frac{3\pi}2+\frac\pi4=-\frac{5\pi}4.
$$
A direct computation (projecting front and back pieces onto the $yz$-plane, and so on) also gives $-\frac{5\pi}4$, but requires three different double integrals.

**Example 14.2.5** Let $\Omega$ be bounded by the cylinder $x^2+y^2=1$ and the planes $z=0$ and $x+z=1$. Evaluate $I=\oiint_{\partial\Omega}2xz\,\mathrm{d}y\wedge\mathrm{d}z+xz\cos y\,\mathrm{d}z\wedge\mathrm{d}x+3yz\sin x\,\mathrm{d}x\wedge\mathrm{d}y$ (outer side). By the divergence theorem,

$$
I=\iiint_\Omega(2z-xz\sin y+3y\sin x)\,\mathrm{d}V.
$$
$\Omega$ is symmetric about the $zx$-plane, and $xz\sin y$ and $y\sin x$ are odd in $y$, so their integrals vanish. Hence

$$
I=\iint_{x^2+y^2\le1}\mathrm{d}x\,\mathrm{d}y\int_0^{1-x}2z\,\mathrm{d}z=\iint_{x^2+y^2\le1}(1-x)^2\,\mathrm{d}x\,\mathrm{d}y=\pi+\frac\pi4=\frac{5\pi}4.
$$
Computing directly: the bottom contributes $0$; on the slanted face $\boldsymbol{n}=\frac{(1,0,1)}{\sqrt2}$ and $\mathrm{d}S=\sqrt2\,\mathrm{d}x\,\mathrm{d}y$, contributing $\iint[2x(1-x)+3y(1-x)\sin x]\,\mathrm{d}x\,\mathrm{d}y=-\frac\pi2$; on the lateral surface $\boldsymbol{n}=(x,y,0)$, and with $\mathrm{d}S=\mathrm{d}\theta\,\mathrm{d}z$ it contributes $\int_0^{2\pi}\mathrm{d}\theta\int_0^{1-\cos\theta}2\cos^2\theta\,z\,\mathrm{d}z=\frac{7\pi}4$ (the term $xyz\cos y$ vanishes by symmetry). The total is $\frac{5\pi}4$. The comparison shows how the divergence theorem replaces three surface integrals by one simple triple integral.

**Example 14.2.6 (Excising a Singularity)** Let $S$ be a smooth closed surface not passing through the origin, with its outer side. Evaluate $I=\oiint_S\dfrac{x\,\mathrm{d}y\wedge\mathrm{d}z+y\,\mathrm{d}z\wedge\mathrm{d}x+z\,\mathrm{d}x\wedge\mathrm{d}y}{(x^2+y^2+z^2)^{3/2}}$. Write $\rho=\sqrt{x^2+y^2+z^2}$ and $\boldsymbol{v}=\frac{(x,y,z)}{\rho^3}$. Away from the origin, $\frac{\partial}{\partial x}\frac x{\rho^3}=\frac{\rho^2-3x^2}{\rho^5}$, and adding the three terms gives $\operatorname{div}\boldsymbol{v}=\frac{3\rho^2-3\rho^2}{\rho^5}=0$.

- If $S$ does not enclose the origin, the divergence theorem gives $I=0$.
- If $S$ encloses the origin, choose a small sphere $S_\varepsilon\colon\rho=\varepsilon$ inside $S$ and apply the divergence theorem to the region between $S$ and $S_\varepsilon$ (with $S_\varepsilon$ oriented by its inner side); this gives $I=\oiint_{S_\varepsilon}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$ (with $S_\varepsilon$ oriented by its outer side). On $S_\varepsilon$ we have $\boldsymbol{v}\cdot\boldsymbol{n}=\frac1{\varepsilon^2}$, so $I=\frac1{\varepsilon^2}\cdot4\pi\varepsilon^2=4\pi$.

This is the three-dimensional version of Example 13.4.6. Physically, the electric field $\boldsymbol{E}=\frac{q}{4\pi\varepsilon_0}\frac{(x,y,z)}{\rho^3}$ of a point charge $q$ has flux $\frac q{\varepsilon_0}$ through every closed surface enclosing the charge and flux $0$ through every closed surface not enclosing it: this is Gauss's law.

### 14.2.3. Physical Meaning of the Divergence

**Theorem 14.2.2** Let $\boldsymbol{v}$ be continuously differentiable in a neighborhood of $M_0$, and let $\Omega$ be a small region containing $M_0$ (such as a ball centered at $M_0$) with volume $V(\Omega)$. Then

$$
\operatorname{div}\boldsymbol{v}(M_0)=\lim_{\Omega\to M_0}\frac1{V(\Omega)}\oiint_{\partial\Omega}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S},
$$
where $\Omega\to M_0$ means that the diameter of $\Omega$ tends to zero.

**Proof** By the divergence theorem and the **mean value theorem for integrals** applied to the triple integral, $\oiint_{\partial\Omega}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iiint_\Omega\operatorname{div}\boldsymbol{v}\,\mathrm{d}V=\operatorname{div}\boldsymbol{v}(M)\,V(\Omega)$ for some $M\in\Omega$. As $\Omega\to M_0$ we have $M\to M_0$, and the continuity of $\operatorname{div}\boldsymbol{v}$ gives the result. $\square$

Thus the divergence is the volume density of flux: regarding $\boldsymbol{v}$ as a velocity, $\operatorname{div}\boldsymbol{v}(M_0)$ is the amount of fluid flowing out of a unit volume near $M_0$ per unit time. Points with $\operatorname{div}\boldsymbol{v}>0$ are "sources", points with $\operatorname{div}\boldsymbol{v}<0$ are "sinks", and where $\operatorname{div}\boldsymbol{v}=0$ fluid is neither produced nor absorbed. This limit does not refer to a coordinate system, so the divergence is independent of the choice of coordinates; taking it as the definition of the divergence and then deriving the coordinate formula from the divergence theorem is another common approach.

![Left: a source (positive divergence) and a sink (negative divergence), with the outward normal vectors on small circles and the outward flux; right: the divergence-free field (x, -y), for which the inflow through any closed curve equals the outflow](./plots/divergence-flux.py)

## 14.3. Stokes' Theorem

### 14.3.1. Stokes' Theorem

Recall the orientation of the boundary of an oriented surface (the section on oriented surfaces in [2.2.13](/2.2.13)): a person standing on the positive side of a surface $S$ and walking along the boundary $\partial S$ always has $S$ on the left. Equivalently, when the fingers of the right hand curl in the direction of $\partial S$, the thumb points along the normal vector on the positive side of $S$ (the right-hand rule).

**Theorem 14.3.1 (Stokes' Theorem)** Let $S$ be a bounded piecewise smooth oriented surface whose boundary $\partial S$ is a piecewise smooth closed curve oriented by the right-hand rule, and let $\boldsymbol{v}=(X,Y,Z)$ be continuously differentiable on some region containing $S$. Then

$$
\oint_{\partial S}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_S(\operatorname{curl}\boldsymbol{v})\cdot\mathrm{d}\boldsymbol{S},
$$
that is,

$$
\oint_{\partial S}X\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z=\iint_S\begin{vmatrix}\mathrm{d}y\wedge\mathrm{d}z&\mathrm{d}z\wedge\mathrm{d}x&\mathrm{d}x\wedge\mathrm{d}y\\ \dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\ X&Y&Z\end{vmatrix}.
$$

**Proof** Let $S$ be the graph of $z=z(x,y)$ over $D_{xy}$ ($z$ with continuous second-order partial derivatives), with its upper side; a general surface is split into such pieces and the results added, the line integrals over common boundaries cancelling. We prove only $\oint_{\partial S}X\,\mathrm{d}x=\iint_S\frac{\partial X}{\partial z}\,\mathrm{d}z\wedge\mathrm{d}x-\frac{\partial X}{\partial y}\,\mathrm{d}x\wedge\mathrm{d}y$; the terms in $Y$ and $Z$ are similar. The projection of $\partial S$ onto the $xy$-plane is $\partial D_{xy}$ (positively oriented), and $z=z(x,y)$ along $\partial S$, so

$$
\oint_{\partial S}X(x,y,z)\,\mathrm{d}x=\oint_{\partial D_{xy}}X(x,y,z(x,y))\,\mathrm{d}x=-\iint_{D_{xy}}\Big(\frac{\partial X}{\partial y}+\frac{\partial X}{\partial z}z_y\Big)\mathrm{d}x\,\mathrm{d}y,
$$
where the last step uses Green's theorem and the **chain rule**. On the other hand, Theorem 13.5.1 (1) applied to the vector field $\big(0,\frac{\partial X}{\partial z},-\frac{\partial X}{\partial y}\big)$ gives

$$
\iint_S\frac{\partial X}{\partial z}\,\mathrm{d}z\wedge\mathrm{d}x-\frac{\partial X}{\partial y}\,\mathrm{d}x\wedge\mathrm{d}y=\iint_{D_{xy}}\Big(-\frac{\partial X}{\partial z}z_y-\frac{\partial X}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y.
$$
The two expressions are equal. $\square$

Some remarks:

- When $S$ is a region in the $xy$-plane (with its upper side) and $\boldsymbol{v}=(X(x,y),Y(x,y),0)$, Stokes' theorem is Green's theorem.
- As long as the boundary is the same and the orientations are compatible, $\iint_S\operatorname{curl}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$ does not depend on the choice of the surface $S$. If $S_1$ and $S_2$ have the same boundary and $S_1$ together with $S_2^-$ forms a closed surface (enclosing a region $\Omega$ on which $\boldsymbol{v}$ is continuously differentiable), this can also be seen from the divergence theorem and $\operatorname{div}\operatorname{curl}\boldsymbol{v}=0$. Hence, to compute a line integral, we may choose the simplest available surface, usually a piece of a plane.
- A closed surface has no boundary, so $\oiint_S\operatorname{curl}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=0$ (cut the closed surface into two pieces; they have the same boundary with opposite orientations).

### 14.3.2. Applications

**Example 14.3.1** Evaluate $I=\oint_L(y-z)\,\mathrm{d}x+(z-x)\,\mathrm{d}y+(x-y)\,\mathrm{d}z$, where $L$ is the intersection of the cylinder $x^2+y^2=R^2$ with the plane $\frac xa+\frac zb=1$ ($a,b>0$), oriented counterclockwise as seen from the positive $z$-axis. Here $\operatorname{curl}\boldsymbol{v}=(-2,-2,-2)$. Take $S$ to be the elliptical piece of the plane enclosed by $L$, with its upper side (compatible with the orientation of $L$ by the right-hand rule). With $S\colon z=b\big(1-\frac xa\big)$, $z_x=-\frac ba$ and $z_y=0$, Theorem 13.5.1 (1) gives

$$
I=\iint_{x^2+y^2\le R^2}\Big[(-2)\frac ba+0+(-2)\Big]\mathrm{d}x\,\mathrm{d}y=-2\pi R^2\Big(1+\frac ba\Big).
$$
A direct computation with the parametrization $x=R\cos t$, $y=R\sin t$, $z=b\big(1-\frac Ra\cos t\big)$ gives the same result.

![Stokes' theorem: the elliptical piece S of the plane x/a + z/b = 1 cut out by the cylinder; with S oriented by its upper side, the induced orientation of the boundary L is counterclockwise as seen from above](./plots/stokes-surface.py)

**Example 14.3.2** Evaluate $I=\oint_Ly\,\mathrm{d}x+z\,\mathrm{d}y+x\,\mathrm{d}z$, where $L$ is the intersection of the sphere $x^2+y^2+z^2=a^2$ with the plane $x+z=a$, oriented counterclockwise as seen from above. Here $\operatorname{curl}\boldsymbol{v}=(-1,-1,-1)$. $L$ is a circle in the plane: the distance from the center of the sphere to the plane is $\frac a{\sqrt2}$, so its radius is $\frac a{\sqrt2}$. Take $S$ to be the disk in the plane, with upper unit normal $\boldsymbol{n}=\frac{(1,0,1)}{\sqrt2}$, and convert to a surface integral of a scalar function:

$$
I=\iint_S(-1,-1,-1)\cdot\frac{(1,0,1)}{\sqrt2}\,\mathrm{d}S=-\sqrt2\cdot\pi\Big(\frac a{\sqrt2}\Big)^2=-\frac{\pi a^2}{\sqrt2}.
$$
It can also be computed directly: $L$ has the parametrization $x=a\cos^2t$, $y=\sqrt2a\sin t\cos t$, $z=a\sin^2t$ ($0\le t\le\pi$), and substitution gives $a^2\int_0^\pi(-2\sqrt2\sin^2t\cos^2t+\sqrt2\sin^2t\cos2t+2\sin t\cos^3t)\,\mathrm{d}t=-\frac{\pi a^2}{\sqrt2}$; this parametrization is easy to use but not easy to find.

**Example 14.3.3** Evaluate $I=\oint_L(y^2-z^2)\,\mathrm{d}x+(z^2-x^2)\,\mathrm{d}y+(x^2-y^2)\,\mathrm{d}z$, where $L$ is the trace cut on the surface of the cube $[0,a]^3$ by the plane $x+y+z=\frac32a$, oriented counterclockwise as seen from above. The trace is a regular hexagon whose vertices are the midpoints of six edges of the cube, with side $\frac a{\sqrt2}$ and area $\frac{3\sqrt3}2\cdot\frac{a^2}2=\frac{3\sqrt3}4a^2$. We have $\operatorname{curl}\boldsymbol{v}=-2(y+z,\,z+x,\,x+y)$, the upper unit normal of the plane is $\boldsymbol{n}=\frac{(1,1,1)}{\sqrt3}$, and on $S$

$$
\operatorname{curl}\boldsymbol{v}\cdot\boldsymbol{n}=-\frac{4(x+y+z)}{\sqrt3}=-\frac{6a}{\sqrt3}=-2\sqrt3a,\qquad I=-2\sqrt3a\cdot\frac{3\sqrt3}4a^2=-\frac92a^3.
$$
A direct computation would require six segments; by symmetry under interchange of variables only two need to be computed, with the same result.

**Example 14.3.4** Let $L$ be the intersection of the cylinder $x^2+y^2=1$ with the plane $x+2y+z=3$, oriented counterclockwise as seen from the positive $z$-axis. Then $\oint_Lx^2\,\mathrm{d}x+y^2\,\mathrm{d}y+z^2\,\mathrm{d}z=0$, because the integrand is $\frac13\mathrm{d}(x^2+y^2+z^2)$ (its curl is zero); for $\oint_Lz\,\mathrm{d}x+x\,\mathrm{d}y+y\,\mathrm{d}z$ we have $\operatorname{curl}\boldsymbol{v}=(1,1,1)$, and taking the upper side of the plane piece $z=3-x-2y$, with $-z_x=1$ and $-z_y=2$, the integral is $\iint_{x^2+y^2\le1}(1+2+1)\,\mathrm{d}x\,\mathrm{d}y=4\pi$.

### 14.3.3. Physical Meaning of the Curl

**Theorem 14.3.2** Let $\boldsymbol{v}$ be continuously differentiable in a neighborhood of $M_0$, let $\boldsymbol{n}_0$ be a unit vector, and let $S$ be a small surface through $M_0$ with normal vector $\boldsymbol{n}_0$ at $M_0$ (such as a small disk perpendicular to $\boldsymbol{n}_0$), with area $A(S)$ and boundary oriented by the right-hand rule. Then

$$
\lim_{S\to M_0}\frac1{A(S)}\oint_{\partial S}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\operatorname{curl}\boldsymbol{v}(M_0)\cdot\boldsymbol{n}_0.
$$

**Proof** By Stokes' theorem and the mean value theorem for integrals, $\oint_{\partial S}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\operatorname{curl}\boldsymbol{v}\cdot\boldsymbol{n}\,\mathrm{d}S=(\operatorname{curl}\boldsymbol{v}\cdot\boldsymbol{n})(M)\,A(S)$ for some $M\in S$; let $S\to M_0$. $\square$

The left side is called the circulation density of $\boldsymbol{v}$ at $M_0$ about $\boldsymbol{n}_0$. Thus the projection of the curl onto any direction is the circulation density about that direction; by the **Cauchy–Schwarz inequality**, the circulation density is largest when $\boldsymbol{n}_0$ points in the direction of $\operatorname{curl}\boldsymbol{v}(M_0)$, with maximum value $\|\operatorname{curl}\boldsymbol{v}(M_0)\|$. This gives a coordinate-free description of the curl: its direction is the axis about which the field rotates most strongly near the point (by the right-hand rule), and its length is the maximal circulation density. For plane fields, the divergence and the curl can likewise be regarded as flux and circulation per unit area (the two forms of Green's theorem).

![Left: the rigid rotation field (-y, x) has curl 2k everywhere, and the circulation grows with the area enclosed by the circle; right: the vortex field (-y, x)/(x^2+y^2) is irrotational away from the origin, but its circulation around the origin is always 2π](./plots/curl-circulation.py)

## 14.4. Conservative Fields and Potential Functions

### 14.4.1. Basic Concepts

Examples 13.3.3 and 13.3.6 show that for some vector fields the integral between two points is the same along every path. In this section $\Omega$ is a **region** (connected open set) in $\mathbb{R}^2$ or $\mathbb{R}^3$, and all curves are piecewise smooth oriented curves in $\Omega$. The planar and spatial cases run entirely in parallel and are treated together.

**Definition 14.4.1 (Conservative Vector Field)** Let $\boldsymbol{v}$ be a continuous vector field on $\Omega$. If for any two points $A,B$ of $\Omega$ the integral $\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$ is the same for all curves $L$ in $\Omega$ from $A$ to $B$ (that is, the integral is independent of the path), then $\boldsymbol{v}$ is called a **conservative vector field** on $\Omega$, and the integral is written $\int_A^B\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$.

**Definition 14.4.2 (Gradient Field and Potential Function)** If there is a differentiable function $f$ on $\Omega$ with $\nabla f=\boldsymbol{v}$, that is, $\mathrm{d}f=X\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z$, then $\boldsymbol{v}$ is called a **gradient field** on $\Omega$, and $f$ a **potential function** of $\boldsymbol{v}$.

$f$ is a potential function of $\boldsymbol{v}$ if and only if $f$ is an **antiderivative** of the differential form $X\,\mathrm{d}x+Y\,\mathrm{d}y+Z\,\mathrm{d}z$ (Definition 10.5.2); the differential form is then called exact. Two potential functions on a region differ by a constant (a function with zero gradient on a region is constant). In physics one usually takes the potential energy $U=-f$, so that $\boldsymbol{F}=-\nabla U$.

**Definition 14.4.3 (Irrotational Vector Field)** If a continuously differentiable vector field $\boldsymbol{v}$ satisfies $\operatorname{curl}\boldsymbol{v}=\boldsymbol{0}$ everywhere on $\Omega$, then $\boldsymbol{v}$ is called an **irrotational vector field** on $\Omega$. A plane field is irrotational when $\dfrac{\partial Y}{\partial x}=\dfrac{\partial X}{\partial y}$.

### 14.4.2. Criteria for Conservative Fields

**Theorem 14.4.1** Let $\boldsymbol{v}$ be a continuous vector field on a region $\Omega$. The following are equivalent:

1. $\boldsymbol{v}$ is a conservative field on $\Omega$;
2. $\oint_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=0$ for every piecewise smooth closed curve $L$ in $\Omega$;
3. $\boldsymbol{v}$ is a gradient field on $\Omega$.

In this case, for a potential function $f$, $\int_A^B\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=f(B)-f(A)$ (the Newton–Leibniz formula for line integrals). If $\boldsymbol{v}$ is moreover continuously differentiable, it is irrotational.

**Proof** (1) $\Rightarrow$ (2): choose two points $A,B$ on the closed curve $L$ and split $L$ into $L_1$ from $A$ to $B$ and $L_2$ from $B$ to $A$. Then $\oint_L=\int_{L_1}+\int_{L_2}=\int_{L_1}-\int_{L_2^-}=0$, because $L_1$ and $L_2^-$ both run from $A$ to $B$. (2) $\Rightarrow$ (1): if $L_1,L_2$ both run from $A$ to $B$, then $L_1+L_2^-$ is a closed curve, and $\int_{L_1}-\int_{L_2}=\oint_{L_1+L_2^-}=0$.

(1) $\Rightarrow$ (3): fix $A\in\Omega$ and let $f(P)=\int_A^P\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}$ (well defined because the integral is independent of the path). Let $P=(x,y,z)$. Since $\Omega$ is open, for small $|h|$ the segment from $P$ to $(x+h,y,z)$ lies in $\Omega$, and along it $\mathrm{d}y=\mathrm{d}z=0$, so

$$
\frac{f(x+h,y,z)-f(x,y,z)}{h}=\frac1h\int_x^{x+h}X(t,y,z)\,\mathrm{d}t=X(x+\theta h,y,z)\to X(x,y,z)\quad(h\to0),
$$
by the mean value theorem for integrals ($0<\theta<1$) and the continuity of $X$. Similarly $f_y=Y$ and $f_z=Z$. The partial derivatives are continuous, so $f$ is differentiable and $\nabla f=\boldsymbol{v}$.

(3) $\Rightarrow$ (1): let $L\colon\boldsymbol{r}(t)$, $t$ from $\alpha$ to $\beta$. By Theorem 13.3.1 and the chain rule,

$$
\int_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\int_\alpha^\beta\nabla f(\boldsymbol{r}(t))\cdot\boldsymbol{r}'(t)\,\mathrm{d}t=\int_\alpha^\beta\frac{\mathrm{d}}{\mathrm{d}t}f(\boldsymbol{r}(t))\,\mathrm{d}t=f(B)-f(A)
$$
(adding over the pieces of a piecewise smooth curve), which is independent of the path. Finally, if $\boldsymbol{v}=\nabla f$ is continuously differentiable, then $f$ has continuous second-order partial derivatives, and by Theorem 14.1.1, $\operatorname{curl}\boldsymbol{v}=\boldsymbol{0}$. $\square$

The physical meaning of a conservative field is conservation of energy. Let a particle of mass $m$ move under the force $\boldsymbol{F}=\nabla f$ alone, along the trajectory $\boldsymbol{r}(t)$. By Newton's second law $m\boldsymbol{r}''=\nabla f(\boldsymbol{r})$,

$$
\frac{\mathrm{d}}{\mathrm{d}t}\Big(\frac12m\|\boldsymbol{r}'\|^2-f(\boldsymbol{r})\Big)=m\boldsymbol{r}''\cdot\boldsymbol{r}'-\nabla f(\boldsymbol{r})\cdot\boldsymbol{r}'=0,
$$
that is, the sum of the kinetic energy and the potential energy $-f$ is conserved.

Condition (2) of Theorem 14.4.1 must be checked for all closed curves, which is impractical. For continuously differentiable fields, being irrotational is a necessary condition, but in general not a sufficient one:

**Example 14.4.1** The plane field $\boldsymbol{v}=\Big(\dfrac{-y}{x^2+y^2},\dfrac{x}{x^2+y^2}\Big)$ is irrotational on $\mathbb{R}^2\setminus\{0\}$ (Example 13.4.6), but its circulation around the unit circle is $2\pi\ne0$, so it is not a conservative field on $\mathbb{R}^2\setminus\{0\}$. On any simply connected region not containing the origin (such as the right half-plane) it has a potential function, namely the polar angle $\theta$, for instance $\theta=\arctan\frac yx$ on the right half-plane; but the polar angle cannot be defined continuously on all of $\mathbb{R}^2\setminus\{0\}$. Similarly, the spatial field $\Big(\dfrac{-y}{x^2+y^2},\dfrac{x}{x^2+y^2},z\Big)$ is irrotational but not conservative on space with the $z$-axis removed.

The trouble is that the region has a "hole": a closed curve going once around the hole cannot be shrunk to a point within the region, and Green's theorem or Stokes' theorem cannot be applied to a surface it bounds. This calls for a notion of simple connectivity for spatial regions.

**Definition 14.4.4 (Surface-Simply-Connected Domain)** Let $\Omega\subset\mathbb{R}^3$ be a region. If for every piecewise smooth closed curve $L$ in $\Omega$ there is a piecewise smooth surface in $\Omega$ with boundary $L$, then $\Omega$ is called a **surface-simply-connected domain**.

Balls, the whole space and spherical shells $a^2<x^2+y^2+z^2<b^2$ are surface-simply-connected; solid tori (doughnut shapes) and space with a line removed are not. Surface-simple-connectedness is what is usually meant by a (spatial) **simply connected domain**; when a plane region is simply connected in the sense of Definition 13.4.1, the plane region enclosed by a closed curve is a surface with that curve as its boundary.

**Theorem 14.4.2** Let $\Omega$ be a simply connected plane region or a surface-simply-connected spatial region, and let $\boldsymbol{v}$ be continuously differentiable on $\Omega$. Then $\boldsymbol{v}$ is conservative if and only if $\boldsymbol{v}$ is irrotational. In the planar case: $X\,\mathrm{d}x+Y\,\mathrm{d}y$ is exact on a simply connected region if and only if $\frac{\partial Y}{\partial x}=\frac{\partial X}{\partial y}$.

**Proof** Necessity was proved in Theorem 14.4.1. Sufficiency: let $L$ be a closed curve in $\Omega$ and $S$ a surface in $\Omega$ with boundary $L$; by Stokes' theorem $\oint_L\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\operatorname{curl}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=0$, and in the planar case we use Green's theorem. Theorem 14.4.1 then gives the result. (Strictly speaking, a self-intersecting closed curve must first be decomposed into simple closed curves, or one verifies condition (2) only for simple closed curves and then shows that this suffices for path independence; we do not go into this here.) $\square$

### 14.4.3. Computing Potential Functions

**Algorithm 14.4.1 (Testing for a Conservative Field and Finding a Potential)** Given a continuously differentiable field $\boldsymbol{v}=(X,Y,Z)$ on $\Omega$:

1. Test: check whether $\Omega$ is (surface-)simply connected, and compute $\operatorname{curl}\boldsymbol{v}$. If $\Omega$ is simply connected and $\boldsymbol{v}$ is irrotational, then $\boldsymbol{v}$ is conservative; if $\Omega$ is not simply connected, one must also check that the circulation around each "hole" vanishes (as in Example 14.4.1).
2. Line integral method: fix $(x_0,y_0,z_0)\in\Omega$ and integrate along a broken line parallel to the coordinate axes (the broken line must lie in $\Omega$):
   $$
   f(x,y,z)=\int_{x_0}^xX(t,y_0,z_0)\,\mathrm{d}t+\int_{y_0}^yY(x,t,z_0)\,\mathrm{d}t+\int_{z_0}^zZ(x,y,t)\,\mathrm{d}t.
   $$
3. Or the indefinite integral method: from $f_x=X$ get $f=\int X\,\mathrm{d}x+g(y,z)$; substituting into $f_y=Y$ determines $g_y$, and integrating gives $g$ up to a function $h(z)$; finally $f_z=Z$ determines $h$.
4. Or grouping into differentials: when the integrand can be recognized directly as a sum of total differentials (such as $y\,\mathrm{d}x+x\,\mathrm{d}y=\mathrm{d}(xy)$), this is fastest.
5. Evaluate the integral: $\int_A^B\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=f(B)-f(A)$; alternatively, integrate directly along a simpler path (a broken line).

**Example 14.4.2** For $2xy^3\,\mathrm{d}x+3x^2y^2\,\mathrm{d}y$: $\frac{\partial}{\partial y}(2xy^3)=6xy^2=\frac{\partial}{\partial x}(3x^2y^2)$, and $\mathbb{R}^2$ is simply connected. Integrating along $(0,0)\to(x,0)\to(x,y)$: $f=\int_0^x0\,\mathrm{d}t+\int_0^y3x^2t^2\,\mathrm{d}t=x^2y^3$, so the antiderivatives are $x^2y^3+C$.

**Example 14.4.3** Find an antiderivative of $\big(\frac yx+\frac{2x}y\big)\mathrm{d}x+\big(\ln x-\frac{x^2}{y^2}\big)\mathrm{d}y$ on $\{x>0,y>0\}$. Both cross partial derivatives equal $\frac1x-\frac{2x}{y^2}$, and the region is simply connected. By the indefinite integral method, $f=\int\big(\frac yx+\frac{2x}y\big)\mathrm{d}x=y\ln x+\frac{x^2}y+g(y)$; then $f_y=\ln x-\frac{x^2}{y^2}+g'(y)$, and comparison with $Y$ gives $g'=0$. Hence the antiderivatives are $y\ln x+\frac{x^2}y+C$.

**Example 14.4.4** For $(\mathrm{e}^x\sin y+y)\,\mathrm{d}x+(\mathrm{e}^x\cos y+x+2)\,\mathrm{d}y$, both cross partial derivatives equal $\mathrm{e}^x\cos y+1$. By the line integral method, $f=\int_0^x0\,\mathrm{d}t+\int_0^y(\mathrm{e}^x\cos t+x+2)\,\mathrm{d}t=\mathrm{e}^x\sin y+xy+2y$. Grouping into differentials shows this at a glance: $\mathrm{d}(\mathrm{e}^x\sin y)+\mathrm{d}(xy)+\mathrm{d}(2y)$.

**Example 14.4.5** Let $f$ be continuously differentiable with $f(0)=0$. Determine $f$ so that $(x\mathrm{e}^x+f(x))y\,\mathrm{d}x+f(x)\,\mathrm{d}y$ is exact, and find an antiderivative. The condition $\frac{\partial}{\partial y}[(x\mathrm{e}^x+f)y]=\frac{\partial}{\partial x}f$ reads $f'(x)-f(x)=x\mathrm{e}^x$. Multiplying by $\mathrm{e}^{-x}$ gives $(\mathrm{e}^{-x}f)'=x$, so $\mathrm{e}^{-x}f=\frac{x^2}2+C$, and $f(0)=0$ gives $f(x)=\frac{x^2\mathrm{e}^x}2$. Antiderivative: $\frac{\partial}{\partial y}F=f(x)$ gives $F=\frac{x^2\mathrm{e}^x}2y+g(x)$, and then $F_x=(x\mathrm{e}^x+\frac{x^2\mathrm{e}^x}2)y+g'(x)$ gives $g'=0$, so the antiderivatives are $\frac12x^2\mathrm{e}^xy+C$.

**Example 14.4.6** Let $f(t)$ be continuously differentiable for $t\ne0$ with $f(1)=0$. Determine $f$ such that $\oint_Ly\big(2-f(x^2-y^2)\big)\,\mathrm{d}x+xf(x^2-y^2)\,\mathrm{d}y=0$ for every closed curve $L$ not meeting the lines $y=\pm x$. The lines $y=\pm x$ divide the plane into four angular regions, each simply connected and containing no point with $x^2-y^2=0$; a closed curve not meeting the two lines must lie in one of these regions. By Theorem 14.4.2, the condition is equivalent to $\frac{\partial}{\partial x}\big[xf(x^2-y^2)\big]=\frac{\partial}{\partial y}\big[y(2-f(x^2-y^2))\big]$ on these regions, that is,

$$
f+2x^2f'=2-f+2y^2f',\qquad\text{that is,}\qquad tf'(t)+f(t)=1\quad(t=x^2-y^2).
$$
Hence $(tf(t))'=1$ and $tf(t)=t+C$; $f(1)=0$ gives $C=-1$, so $f(t)=1-\frac1t$.

**Example 14.4.7** (1) $\int_{(0,2)}^{(2,3)}x\,\mathrm{d}y+y\,\mathrm{d}x=xy\big|_{(0,2)}^{(2,3)}=6$. (2) $\int_{(0,0)}^{(a,b)}\mathrm{e}^x(\cos y\,\mathrm{d}x-\sin y\,\mathrm{d}y)=\mathrm{e}^x\cos y\big|_{(0,0)}^{(a,b)}=\mathrm{e}^a\cos b-1$. (3) Along paths avoiding the origin, $\int_{A}^{B}\dfrac{x\,\mathrm{d}x+y\,\mathrm{d}y+z\,\mathrm{d}z}{x^2+y^2+z^2}=\frac12\ln(x^2+y^2+z^2)\Big|_A^B=\ln\dfrac{\|B\|}{\|A\|}$, where $\|A\|$ is the distance from the point $A$ to the origin.

**Example 14.4.8** For $\boldsymbol{v}=(x+yz,\,y+zx,\,z+xy)$: $\operatorname{curl}\boldsymbol{v}=(x-x,\,y-y,\,z-z)=\boldsymbol{0}$, $\mathbb{R}^3$ is simply connected, and a potential function is $f=\frac12(x^2+y^2+z^2)+xyz$. Hence along any curve from the origin to $(1,1,1)$, $\int\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=f(1,1,1)-f(0,0,0)=\frac52$.

**Example 14.4.9** Decide whether $z^2\,\mathrm{d}x+2yz\,\mathrm{d}y+(y^2+2xz+z^2)\,\mathrm{d}z$ is exact. Since $\operatorname{curl}\boldsymbol{v}=(2y-2y,\,2z-2z,\,0)=\boldsymbol{0}$, it is. Integrating along $(0,0,0)\to(x,0,0)\to(x,y,0)\to(x,y,z)$, the integrands on the first two segments vanish, and

$$
f=\int_0^z(y^2+2xt+t^2)\,\mathrm{d}t=y^2z+xz^2+\frac{z^3}3.
$$

**Example 14.4.10** Unit point masses are placed at $A(1,0)$ and $B(0,1)$, and another unit point mass moves from the origin $O$ along the upper semicircle with center $A$ and radius $1$ to $D(2,0)$. Find the work done by gravity. The gravitational field is conservative: the field at a unit mass at $Q$ is $\nabla\frac{G}{\|Q-P\|}$, with potential function $\frac{G}{\|Q-P\|}$ ($P$ being the attracting mass), so the work depends only on the initial and terminal points. $O$ and $D$ are both at distance $1$ from $A$, so the work done by the attraction of $A$ is zero (in fact, along this circle the attraction of $A$ is everywhere perpendicular to the displacement); the work done by the attraction of $B$ is $G\big(\frac1{\|DB\|}-\frac1{\|OB\|}\big)=G\big(\frac1{\sqrt5}-1\big)$. The total work is $G\big(\frac1{\sqrt5}-1\big)$, which is negative: the particle moves away from $B$.

## 14.5. Solenoidal and Harmonic Fields

### 14.5.1. Solenoidal Fields

**Definition 14.5.1 (Solenoidal Vector Field)** If a continuously differentiable vector field $\boldsymbol{v}$ satisfies $\operatorname{div}\boldsymbol{v}=0$ everywhere on a region $\Omega$, then $\boldsymbol{v}$ is called a **solenoidal vector field** on $\Omega$.

The velocity field of an incompressible fluid and the magnetic field are solenoidal. By Theorem 14.1.1, the curl $\boldsymbol{v}=\nabla\times\boldsymbol{u}$ of a continuously differentiable field is always solenoidal.

**Example 14.5.1** Particles of masses $m_i$ are located at $P_i$ ($i=1,\dots,k$). Their gravitational attraction on a unit mass at $P=(x,y,z)$ is

$$
\boldsymbol{F}=\sum_{i=1}^k\boldsymbol{F}_i=-G\sum_{i=1}^km_i\frac{\boldsymbol{r}_i}{\|\boldsymbol{r}_i\|^3},\qquad\boldsymbol{r}_i=P-P_i.
$$
By the computation in Example 14.2.6, each term has zero divergence away from $P_i$, so $\boldsymbol{F}$ is solenoidal on the region with the masses removed. But if a closed surface $S$ (outer side) encloses the masses $m_{i_1},\dots,m_{i_s}$, excising small balls around these points and applying the divergence theorem gives

$$
\oiint_S\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=-4\pi G\,(m_{i_1}+\cdots+m_{i_s}),
$$
which is Gauss's law for gravitation: the flux depends only on the total mass enclosed by the surface. From the point of view of Theorem 14.2.2, the point masses are "sinks" of the gravitational field, with strength proportional to the mass.

Can a solenoidal field be written as a curl? As for irrotational fields, the answer depends on whether the region has "cavities".

**Definition 14.5.2 (Volume-Simply-Connected Domain)** Let $\Omega\subset\mathbb{R}^3$ be a region. If the bounded region enclosed by every piecewise smooth closed surface in $\Omega$ is contained in $\Omega$, then $\Omega$ is called a volume-simply-connected domain.

Balls, the whole space and solid tori are volume-simply-connected; spherical shells and space with a point removed are not. Volume-simple-connectedness and surface-simple-connectedness are independent conditions: a solid torus satisfies only the former, a spherical shell only the latter.

**Theorem 14.5.1** Let $\Omega$ be a volume-simply-connected domain and $\boldsymbol{v}$ continuously differentiable on $\Omega$.

1. $\boldsymbol{v}$ is solenoidal if and only if $\oiint_S\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=0$ for every piecewise smooth closed surface $S$ in $\Omega$.
2. If $\boldsymbol{v}$ is solenoidal, then there is a vector field $\boldsymbol{u}$ with $\boldsymbol{v}=\nabla\times\boldsymbol{u}$ ($\boldsymbol{u}$ is called a vector potential).

**Proof** (1) Necessity: the region enclosed by $S$ lies in $\Omega$, so by the divergence theorem the flux is $\iiint\operatorname{div}\boldsymbol{v}\,\mathrm{d}V=0$. Sufficiency: if $\operatorname{div}\boldsymbol{v}(M_0)\ne0$, then by Theorem 14.2.2 the flux through a small sphere centered at $M_0$ is nonzero, a contradiction. (2) The proof is omitted. $\square$

When the region is not volume-simply-connected, conclusion (2) may fail: the field $\frac{(x,y,z)}{\rho^3}$ of Example 14.2.6 is solenoidal on $\mathbb{R}^3\setminus\{0\}$, but its flux through the unit sphere is $4\pi$; since the flux of a curl through a closed surface is always zero (the remark after Theorem 14.3.1), it is not the curl of any continuously differentiable field.

### 14.5.2. Harmonic Fields and Harmonic Functions

**Definition 14.5.3 (Harmonic Vector Field and Harmonic Function)** A vector field that is both a gradient field and solenoidal is called a **harmonic vector field**. If $\boldsymbol{v}=\nabla f$ is a harmonic field, then $\Delta f=\nabla\cdot\nabla f=0$. A function on a region that has continuous second-order partial derivatives and satisfies the Laplace equation $\Delta f=0$ is called a **harmonic function**.

For example, $\frac1{\sqrt{x^2+y^2+z^2}}$ is harmonic on $\mathbb{R}^3\setminus\{0\}$ (its gradient is exactly $-1$ times the field of Example 14.2.6); in the plane, $x^2-y^2$, $\mathrm{e}^x\sin y$ and $\ln(x^2+y^2)$ are harmonic functions. The electric potential in a charge-free region of an electrostatic field and the temperature in a steady-state temperature field are harmonic functions.

**Theorem 14.5.2 (Green's First Identity)** Let $\Omega$ be a bounded closed region with piecewise smooth boundary $\partial\Omega$ and outward normal $\boldsymbol{n}$, and let $f,g$ have continuous second-order partial derivatives on $\Omega$. Then

$$
\oiint_{\partial\Omega}f\frac{\partial g}{\partial\boldsymbol{n}}\,\mathrm{d}S=\iiint_\Omega\big(f\Delta g+\nabla f\cdot\nabla g\big)\,\mathrm{d}V.
$$

**Proof** The **directional derivative** is $\frac{\partial g}{\partial\boldsymbol{n}}=\nabla g\cdot\boldsymbol{n}$, so the left side is the flux of $f\nabla g$. By the divergence theorem and Property 14.1.1, it equals $\iiint_\Omega\nabla\cdot(f\nabla g)\,\mathrm{d}V=\iiint_\Omega(f\Delta g+\nabla f\cdot\nabla g)\,\mathrm{d}V$. $\square$

**Theorem 14.5.3** Let $\Omega$ be a bounded region and let $f$ have continuous second-order partial derivatives on the closed region $\bar\Omega$ and be harmonic in $\Omega$. If $f=0$ on the boundary, then $f\equiv0$ in $\Omega$.

**Proof** Take $g=f$ in Theorem 14.5.2. The left side vanishes because $f|_{\partial\Omega}=0$, and $\Delta f=0$ on the right, so $\iiint_\Omega\|\nabla f\|^2\,\mathrm{d}V=0$. The integrand is continuous and nonnegative, so $\nabla f\equiv\boldsymbol{0}$ and $f$ is constant on the connected set $\Omega$; continuity and the zero boundary values then give $f\equiv0$. $\square$

Corollary: if two harmonic functions take the same values on the boundary, they are equal (apply Theorem 14.5.3 to their difference). In other words, the Dirichlet problem for the Laplace equation (find a harmonic function with given boundary values) has at most one solution: the steady-state temperature distribution is uniquely determined by the boundary temperature. Green's first identity in the plane follows in the same way from the flux form of Green's theorem (Example 13.4.8 is the case $f\equiv1$).

## 14.6. Vector Operators in Orthogonal Curvilinear Coordinates

Physical problems often have cylindrical or spherical symmetry, and it is then more convenient to write the gradient, divergence and curl in cylindrical or spherical coordinates. Let the position of a point be determined by $(q_1,q_2,q_3)$, $\boldsymbol{r}=\boldsymbol{r}(q_1,q_2,q_3)$. If the three families of coordinate curves (obtained by letting only one $q_i$ vary) are mutually orthogonal at each point, $(q_1,q_2,q_3)$ are called orthogonal curvilinear coordinates. Let $\boldsymbol{e}_i$ denote the unit tangent vector in the direction of increasing $q_i$, and assume that $\boldsymbol{e}_1,\boldsymbol{e}_2,\boldsymbol{e}_3$ form a right-handed system.

**Definition 14.6.1 (Lamé Coefficients)** The numbers $H_i=\Big\|\dfrac{\partial\boldsymbol{r}}{\partial q_i}\Big\|=\sqrt{\Big(\dfrac{\partial x}{\partial q_i}\Big)^2+\Big(\dfrac{\partial y}{\partial q_i}\Big)^2+\Big(\dfrac{\partial z}{\partial q_i}\Big)^2}$ ($i=1,2,3$) are called the **Lamé coefficients** (or scale factors) of the orthogonal curvilinear coordinates.

The arc length element along a $q_i$ coordinate curve is $\mathrm{d}l_i=H_i\,\mathrm{d}q_i$, the area elements on the coordinate surfaces are $\mathrm{d}S_1=H_2H_3\,\mathrm{d}q_2\,\mathrm{d}q_3$ and so on, and the volume element is $\mathrm{d}V=H_1H_2H_3\,\mathrm{d}q_1\,\mathrm{d}q_2\,\mathrm{d}q_3$ ($H_1H_2H_3$ is exactly the **Jacobian determinant** of the coordinate transformation). The Lamé coefficients of cylindrical coordinates $(r,\theta,z)$ are $1,r,1$; those of spherical coordinates $(\rho,\varphi,\theta)$ ($x=\rho\sin\varphi\cos\theta$, $y=\rho\sin\varphi\sin\theta$, $z=\rho\cos\varphi$, as in [2.2.12](/2.2.12)) are $1,\rho,\rho\sin\varphi$.

Let $\boldsymbol{v}=v_1\boldsymbol{e}_1+v_2\boldsymbol{e}_2+v_3\boldsymbol{e}_3$. The components of the gradient are the directional derivatives $\frac1{H_i}\frac{\partial f}{\partial q_i}$ along the $\boldsymbol{e}_i$; the divergence is computed, following Theorem 14.2.2, as the flux through a small curvilinear box with edges $\mathrm{d}l_1,\mathrm{d}l_2,\mathrm{d}l_3$ divided by its volume (for example, the difference of the fluxes through the two $q_3$ coordinate faces is approximately $\frac{\partial(v_3H_1H_2)}{\partial q_3}\Delta q_1\Delta q_2\Delta q_3$); and the curl is computed, following Theorem 14.3.2, from the circulation around small curvilinear rectangles on the coordinate surfaces. The results are

$$
\begin{aligned}
\nabla f&=\sum_{i=1}^3\frac1{H_i}\frac{\partial f}{\partial q_i}\boldsymbol{e}_i,\qquad
\nabla\cdot\boldsymbol{v}=\frac1{H_1H_2H_3}\Big[\frac{\partial(v_1H_2H_3)}{\partial q_1}+\frac{\partial(v_2H_3H_1)}{\partial q_2}+\frac{\partial(v_3H_1H_2)}{\partial q_3}\Big],\\
\nabla\times\boldsymbol{v}&=\frac1{H_1H_2H_3}\begin{vmatrix}H_1\boldsymbol{e}_1&H_2\boldsymbol{e}_2&H_3\boldsymbol{e}_3\\ \dfrac{\partial}{\partial q_1}&\dfrac{\partial}{\partial q_2}&\dfrac{\partial}{\partial q_3}\\ H_1v_1&H_2v_2&H_3v_3\end{vmatrix},\qquad
\Delta f=\frac1{H_1H_2H_3}\sum_{i=1}^3\frac{\partial}{\partial q_i}\Big(\frac{H_1H_2H_3}{H_i^2}\frac{\partial f}{\partial q_i}\Big).
\end{aligned}
$$

**Cylindrical coordinates** $(r,\theta,z)$, $\boldsymbol{v}=v_r\boldsymbol{e}_r+v_\theta\boldsymbol{e}_\theta+v_z\boldsymbol{e}_z$:

$$
\begin{aligned}
\nabla f&=\frac{\partial f}{\partial r}\boldsymbol{e}_r+\frac1r\frac{\partial f}{\partial\theta}\boldsymbol{e}_\theta+\frac{\partial f}{\partial z}\boldsymbol{e}_z,\qquad
\nabla\cdot\boldsymbol{v}=\frac1r\frac{\partial(rv_r)}{\partial r}+\frac1r\frac{\partial v_\theta}{\partial\theta}+\frac{\partial v_z}{\partial z},\\
\nabla\times\boldsymbol{v}&=\Big(\frac1r\frac{\partial v_z}{\partial\theta}-\frac{\partial v_\theta}{\partial z}\Big)\boldsymbol{e}_r+\Big(\frac{\partial v_r}{\partial z}-\frac{\partial v_z}{\partial r}\Big)\boldsymbol{e}_\theta+\frac1r\Big(\frac{\partial(rv_\theta)}{\partial r}-\frac{\partial v_r}{\partial\theta}\Big)\boldsymbol{e}_z,\\
\Delta f&=\frac1r\frac{\partial}{\partial r}\Big(r\frac{\partial f}{\partial r}\Big)+\frac1{r^2}\frac{\partial^2f}{\partial\theta^2}+\frac{\partial^2f}{\partial z^2}.
\end{aligned}
$$

**Spherical coordinates** $(\rho,\varphi,\theta)$, $\boldsymbol{v}=v_\rho\boldsymbol{e}_\rho+v_\varphi\boldsymbol{e}_\varphi+v_\theta\boldsymbol{e}_\theta$:

$$
\begin{aligned}
\nabla f&=\frac{\partial f}{\partial\rho}\boldsymbol{e}_\rho+\frac1\rho\frac{\partial f}{\partial\varphi}\boldsymbol{e}_\varphi+\frac1{\rho\sin\varphi}\frac{\partial f}{\partial\theta}\boldsymbol{e}_\theta,\qquad
\nabla\cdot\boldsymbol{v}=\frac1{\rho^2}\frac{\partial(\rho^2v_\rho)}{\partial\rho}+\frac1{\rho\sin\varphi}\frac{\partial(\sin\varphi\,v_\varphi)}{\partial\varphi}+\frac1{\rho\sin\varphi}\frac{\partial v_\theta}{\partial\theta},\\
\nabla\times\boldsymbol{v}&=\frac1{\rho\sin\varphi}\Big(\frac{\partial(\sin\varphi\,v_\theta)}{\partial\varphi}-\frac{\partial v_\varphi}{\partial\theta}\Big)\boldsymbol{e}_\rho+\frac1\rho\Big(\frac1{\sin\varphi}\frac{\partial v_\rho}{\partial\theta}-\frac{\partial(\rho v_\theta)}{\partial\rho}\Big)\boldsymbol{e}_\varphi+\frac1\rho\Big(\frac{\partial(\rho v_\varphi)}{\partial\rho}-\frac{\partial v_\rho}{\partial\varphi}\Big)\boldsymbol{e}_\theta,\\
\Delta f&=\frac1{\rho^2}\frac{\partial}{\partial\rho}\Big(\rho^2\frac{\partial f}{\partial\rho}\Big)+\frac1{\rho^2\sin\varphi}\frac{\partial}{\partial\varphi}\Big(\sin\varphi\frac{\partial f}{\partial\varphi}\Big)+\frac1{\rho^2\sin^2\varphi}\frac{\partial^2f}{\partial\theta^2}.
\end{aligned}
$$

For example, the radial field $\boldsymbol{v}=\frac1{\rho^2}\boldsymbol{e}_\rho$ (the field of Example 14.2.6) has divergence $\frac1{\rho^2}\frac{\partial}{\partial\rho}(1)=0$; a harmonic function depending only on $\rho$ satisfies $(\rho^2f')'=0$, so $f=\frac{C_1}\rho+C_2$. In the plane, a harmonic function depending only on $r$ satisfies $(rf')'=0$, so $f=C_1\ln r+C_2$. Verifying these facts in Cartesian coordinates is much more laborious.

## Summary

The main integral theorems ($\boldsymbol{v}=(X,Y,Z)$ continuously differentiable, boundaries with the induced positive orientation):

| Theorem | Formula | Integrals related | "Derivative" over the region |
|---|---|---|---|
| Newton–Leibniz | $\int_a^bf'(x)\,\mathrm{d}x=f(b)-f(a)$ | Interval ↔ endpoints | $f'$ |
| Green | $\oint_{\partial D}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_D(Y_x-X_y)\,\mathrm{d}\sigma$ | Plane region ↔ boundary curve | Plane curl |
| Divergence (Gauss) | $\oiint_{\partial\Omega}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}=\iiint_\Omega\operatorname{div}\boldsymbol{v}\,\mathrm{d}V$ | Spatial region ↔ boundary surface | Divergence |
| Stokes | $\oint_{\partial S}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\operatorname{curl}\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{S}$ | Surface ↔ boundary curve | Curl |
| Newton–Leibniz for line integrals | $\int_A^B\nabla f\cdot\mathrm{d}\boldsymbol{l}=f(B)-f(A)$ | Curve ↔ endpoints | Gradient |

Basic operations of vector analysis:

| Operation | Definition | Physical meaning | Identity |
|---|---|---|---|
| Gradient $\nabla f$ | $(f_x,f_y,f_z)$ | Direction and rate of fastest increase | $\nabla\times\nabla f=\boldsymbol{0}$ |
| Divergence $\nabla\cdot\boldsymbol{v}$ | $X_x+Y_y+Z_z$ | Volume density of flux (source strength) | $\nabla\cdot(\nabla\times\boldsymbol{v})=0$ |
| Curl $\nabla\times\boldsymbol{v}$ | $(Z_y-Y_z,\,X_z-Z_x,\,Y_x-X_y)$ | Maximal circulation density and its axis | |
| Laplacian $\Delta f$ | $f_{xx}+f_{yy}+f_{zz}$ | $\nabla\cdot\nabla f$ | |

Special classes of fields:

| Field | Definition | Equivalent conditions or properties |
|---|---|---|
| Conservative | Line integrals independent of the path | $\Leftrightarrow$ zero integral around closed curves $\Leftrightarrow$ gradient field; on simply connected (surface-simply-connected) regions $\Leftrightarrow$ irrotational |
| Solenoidal | $\operatorname{div}\boldsymbol{v}=0$ | On volume-simply-connected regions $\Leftrightarrow$ zero flux through closed surfaces, and a curl |
| Harmonic | Gradient field and solenoidal | The potential satisfies $\Delta f=0$; a harmonic function is determined by its boundary values |

When computing line and surface integrals of vector fields, first see whether the main theorems or path independence simplify the problem: for closed surfaces use the divergence theorem (closing the surface if necessary, and excising small balls around singularities); for closed space curves use Stokes' theorem (choosing the simplest surface); for irrotational fields change the path or use a potential function.
