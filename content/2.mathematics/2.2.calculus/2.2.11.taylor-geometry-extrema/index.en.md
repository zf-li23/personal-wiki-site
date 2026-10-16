---
title: Taylor's Formula, Geometric Applications and Extrema
source_hash: d78e7356dda0
---

The total differential of the previous chapter is the first-order approximation of a function of several variables. This chapter puts it to work in two directions. Geometrically, the first-order approximation gives tangent lines to space curves and tangent planes to surfaces. Analytically, the second-order approximation (Taylor's formula) gives tests for extrema: the second-order term is a quadratic form, and the type of an extremum is decided by the definiteness of the Hessian matrix. Finally we treat extremum problems with constraints; the method of Lagrange multipliers rests on the implicit function theorem of [2.2.10](/2.2.10), and its geometric meaning is that the level curve of the objective function is tangent to the constraint curve.

The chapter is closely tied to linear algebra: for the Hessian matrix, **quadratic forms** and **positive definite matrices** see [2.1.7](/2.1.7) (whose Examples 7.2.1 and 7.3.1 discuss the same problem from the matrix point of view), and for least squares fitting and the **normal equations** see [2.1.4](/2.1.4). **Taylor's formula** and extrema in one variable are covered in [2.2.5](/2.2.5).

## 11.1. Preliminaries: Cross Products, Planes and Lines

Before discussing space curves and surfaces, we briefly review solid analytic geometry. A vector in $\mathbb{R}^3$ is written $\boldsymbol{a}=(a_1,a_2,a_3)$, the coordinate unit vectors are $\boldsymbol{i},\boldsymbol{j},\boldsymbol{k}$, and the dot product $\boldsymbol{a}\cdot\boldsymbol{b}$ is the standard **inner product**.

**Definition 11.1.1 (Cross Product)** The **cross product** (vector product) of vectors $\boldsymbol{a},\boldsymbol{b}\in\mathbb{R}^3$ is

$$
\boldsymbol{a}\times\boldsymbol{b}=\begin{vmatrix}\boldsymbol{i}&\boldsymbol{j}&\boldsymbol{k}\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix}=(a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1).
$$

The determinant here is only a formal device (expanded along the first row). The cross product has the following properties: $\boldsymbol{a}\times\boldsymbol{b}$ is perpendicular to both $\boldsymbol{a}$ and $\boldsymbol{b}$, and $\boldsymbol{a},\boldsymbol{b},\boldsymbol{a}\times\boldsymbol{b}$ form a right-handed system; $\|\boldsymbol{a}\times\boldsymbol{b}\|=\|\boldsymbol{a}\|\|\boldsymbol{b}\|\sin\theta$ is the area of the parallelogram spanned by $\boldsymbol{a}$ and $\boldsymbol{b}$; $\boldsymbol{b}\times\boldsymbol{a}=-\boldsymbol{a}\times\boldsymbol{b}$, and $\boldsymbol{a}\times\boldsymbol{b}=\boldsymbol{0}$ if and only if the two vectors are collinear; for fixed $\boldsymbol{a}$, the map $\boldsymbol{b}\mapsto\boldsymbol{a}\times\boldsymbol{b}$ is a **linear transformation** (its matrix is given in [2.1.1](/2.1.1)). The scalar triple product $(\boldsymbol{a}\times\boldsymbol{b})\cdot\boldsymbol{c}=\det[\boldsymbol{a}\ \boldsymbol{b}\ \boldsymbol{c}]$ (with the three vectors as rows or columns) has absolute value equal to the volume of the parallelepiped they span; this is the geometric meaning of the **determinant** ([2.1.5](/2.1.5)).

- Planes: the plane through $M_0(x_0,y_0,z_0)$ with normal vector $\boldsymbol{n}=(A,B,C)\ne\boldsymbol{0}$ (point-normal form) is $A(x-x_0)+B(y-y_0)+C(z-z_0)=0$, and its general form is $Ax+By+Cz+D=0$. The distance from a point $(x_1,y_1,z_1)$ to it is $\dfrac{|Ax_1+By_1+Cz_1+D|}{\sqrt{A^2+B^2+C^2}}$ (derived in Example 11.6.6 by Lagrange multipliers).
- Lines: the line through $M_0$ with direction vector $\boldsymbol{s}=(l,m,n)$ has parametric form $(x,y,z)=(x_0,y_0,z_0)+t(l,m,n)$ and symmetric (standard) form $\dfrac{x-x_0}{l}=\dfrac{y-y_0}{m}=\dfrac{z-z_0}{n}$ (a zero denominator means that the numerator is zero). The intersection of two planes is a line, whose direction vector is the cross product of the two normal vectors.
- The angle between two lines (two planes) is given by the angle between their direction vectors (normal vectors): $\cos\theta=\dfrac{|\boldsymbol{s}_1\cdot\boldsymbol{s}_2|}{\|\boldsymbol{s}_1\|\|\boldsymbol{s}_2\|}$.

## 11.2. Taylor's Formula in Several Variables

### 11.2.1. Taylor's Formula with Lagrange Remainder

To write the higher-order terms compactly, we introduce the notation

$$
\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)f(x_0,y_0)=hf_x(x_0,y_0)+kf_y(x_0,y_0),
$$

$$
\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^lf(x_0,y_0)=\sum_{i=0}^{l}\binom{l}{i}\frac{\partial^lf}{\partial x^i\,\partial y^{l-i}}(x_0,y_0)\,h^ik^{l-i}.
$$

This is just the $l$-th order total differential $\mathrm{d}^lf$ of [2.2.10](/2.2.10) (with $\mathrm{d}x=h$, $\mathrm{d}y=k$).

**Theorem 11.2.1 (Taylor's Formula in Two Variables)** Let $f(x,y)$ have continuous partial derivatives of order $q+1$ in a neighborhood of $M_0(x_0,y_0)$, and let $(x_0+h,y_0+k)$ lie in this neighborhood. Then there is $\theta\in(0,1)$ such that

$$
f(x_0+h,y_0+k)=f(x_0,y_0)+\sum_{l=1}^{q}\frac1{l!}\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^lf(x_0,y_0)+\frac{1}{(q+1)!}\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^{q+1}f(x_0+\theta h,y_0+\theta k).
$$

**Proof** Restrict the function to the segment joining the two points, which reduces it to a function of one variable. Let $g(t)=f(x_0+th,y_0+tk)$, $t\in[0,1]$. By the chain rule $g'(t)=hf_x+kf_y=\big(h\partial_x+k\partial_y\big)f(x_0+th,y_0+tk)$, and by induction

$$
g^{(l)}(t)=\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^lf(x_0+th,y_0+tk)\qquad(l\le q+1)
$$

(this uses the independence of mixed partial derivatives from the order of differentiation). Applying the one-variable Taylor formula with **Lagrange form of the remainder** to $g$ at $t=0$ and setting $t=1$ gives $g(1)=\sum_{l=0}^q\frac{g^{(l)}(0)}{l!}+\frac{g^{(q+1)}(\theta)}{(q+1)!}$, which is the claim. $\square$

For $q=0$ we obtain the mean value theorem in two variables: $f(x_0+h,y_0+k)-f(x_0,y_0)=hf_x(x_0+\theta h,y_0+\theta k)+kf_y(x_0+\theta h,y_0+\theta k)$. It follows that if $\nabla f\equiv\boldsymbol{0}$ on a region $D$, then $f$ is constant on $D$ (any two points of $D$ can be joined by a polygonal path in $D$; apply the mean value theorem on each segment).

### 11.2.2. Peano Remainder and Uniqueness

**Theorem 11.2.2 (Peano Remainder)** Let $f$ have continuous partial derivatives of order $q$ in a neighborhood of $M_0(x_0,y_0)$, and let $\rho=\sqrt{h^2+k^2}$. Then

$$
f(x_0+h,y_0+k)=f(x_0,y_0)+\sum_{l=1}^{q}\frac1{l!}\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^lf(x_0,y_0)+o(\rho^q)\qquad(\rho\to0).
$$

**Proof** By Theorem 11.2.1 (of order $q-1$, so that the remainder involves the $q$-th order derivatives at an intermediate point), the difference between the remainder and $\frac1{q!}\big(h\partial_x+k\partial_y\big)^qf(x_0,y_0)$ is a sum of terms $\binom{q}{i}h^ik^{q-i}$ multiplied by the difference between a $q$-th order partial derivative at the intermediate point and at $M_0$; the latter tends to $0$ by continuity, while $|h^ik^{q-i}|\le\rho^q$. $\square$

**Theorem 11.2.3 (Uniqueness of the Taylor Expansion)** If

$$
f(x_0+h,y_0+k)=P(h,k)+o(\rho^q),
$$

where $P$ is a polynomial in $h,k$ of degree at most $q$, then $P$ is the Taylor polynomial of order $q$ of $f$ at $M_0$.

**Proof** Subtracting the two expansions gives a polynomial $Q(h,k)$ of degree at most $q$ with $Q=o(\rho^q)$. Split $Q$ into homogeneous parts by degree, $Q=Q_0+Q_1+\cdots+Q_q$. Letting $(h,k)\to0$ gives $Q_0=0$. Suppose $Q_0=\cdots=Q_{j-1}=0$. For fixed $(h,k)\ne(0,0)$ we have $Q_j(th,tk)=t^jQ_j(h,k)$ while $Q(th,tk)=o(t^j)$ as $t\to0^+$; dividing by $t^j$ and letting $t\to0^+$ gives $Q_j(h,k)=0$. By induction $Q\equiv0$. $\square$

The point of uniqueness is that Taylor expansions of functions of several variables can be obtained indirectly from known expansions of functions of one variable, without computing the partial derivatives one by one.

**Example 11.2.1** Find the third-order Taylor expansion of $f(x,y)=\mathrm{e}^x\ln(1+y)$ at the origin. From $\mathrm{e}^x=1+x+\frac{x^2}2+O(x^3)$ and $\ln(1+y)=y-\frac{y^2}2+\frac{y^3}3+O(y^4)$, multiplying and keeping terms of degree at most three gives

$$
\mathrm{e}^x\ln(1+y)=y+xy-\frac{y^2}{2}+\frac{x^2y}{2}-\frac{xy^2}{2}+\frac{y^3}{3}+o(\rho^3).
$$

By uniqueness this is the third-order Taylor formula, and we can read off $f_{xy}(0,0)=1$, $\frac{1}{3!}\cdot3f_{xxy}(0,0)=\frac12$, that is, $f_{xxy}(0,0)=1$, and so on. The Taylor expansion of a polynomial is simply its rearrangement in powers of $x-x_0$ and $y-y_0$.

### 11.2.3. Second-Order Taylor Formula in $n$ Variables and the Hessian Matrix

The case of $n$ variables is entirely analogous. Write the increment as $\boldsymbol{h}=(h_1,\dots,h_n)^{\mathsf T}$ and differentiate $g(t)=f(x_0+t\boldsymbol{h})$ twice: $g''(t)=\sum_{i,j}f_{x_ix_j}(x_0+t\boldsymbol{h})h_ih_j$.

**Theorem 11.2.4** Let $f$ have continuous second-order partial derivatives in a neighborhood of $x_0$. Then

$$
f(x_0+\boldsymbol{h})=f(x_0)+\nabla f(x_0)\cdot\boldsymbol{h}+\frac12\boldsymbol{h}^{\mathsf T}H_f(x_0+\theta\boldsymbol{h})\boldsymbol{h},\qquad\theta\in(0,1),
$$

$$
f(x_0+\boldsymbol{h})=f(x_0)+\nabla f(x_0)\cdot\boldsymbol{h}+\frac12\boldsymbol{h}^{\mathsf T}H_f(x_0)\boldsymbol{h}+o(\|\boldsymbol{h}\|^2),
$$

where $H_f=\Big[\dfrac{\partial^2f}{\partial x_i\,\partial x_j}\Big]_{n\times n}$ is the **Hessian matrix** of $f$.

Since the second-order partial derivatives are continuous, $H_f$ is a real symmetric matrix, and the second-order term is a **quadratic form** in $\boldsymbol{h}$. Compare the one-variable formula $f(x_0+h)=f(x_0)+f'(x_0)h+\frac12f''(x_0)h^2+o(h^2)$: the gradient plays the role of the first derivative and the Hessian matrix that of the second derivative (it is also the Jacobian matrix of the gradient map $x\mapsto\nabla f(x)$). [Example 7.2.1](/2.1.7#ex-7.2.1) of linear algebra states the same formula.

**Example 11.2.2** Let $f$ have continuous third-order partial derivatives. Use Taylor's formula to estimate the error of the five-point difference quotient, widely used in numerical computation,

$$
\Delta_hf(x,y)=\frac{f(x+h,y)+f(x-h,y)+f(x,y+h)+f(x,y-h)-4f(x,y)}{h^2}
$$

as an approximation of $f_{xx}+f_{yy}$. Expanding $f(x\pm h,y)$ to second order with third-order Lagrange remainders and adding, the first-order terms cancel: $f(x+h,y)+f(x-h,y)=2f+h^2f_{xx}+\frac{h^3}{6}\big[f_{xxx}(x+\theta_1h,y)-f_{xxx}(x-\theta_2h,y)\big]$, and similarly in the $y$-direction. Hence

$$
\Delta_hf-(f_{xx}+f_{yy})=\frac{h}{6}\big[f_{xxx}(x+\theta_1h,y)-f_{xxx}(x-\theta_2h,y)+f_{yyy}(x,y+\theta_3h)-f_{yyy}(x,y-\theta_4h)\big],
$$

and the error is at most $\frac{2h}{3}M$, where $M$ bounds the absolute values of the third-order partial derivatives (if the fourth-order partial derivatives are continuous, one can show that the error is in fact $O(h^2)$).

## 11.3. Vector-Valued Functions

**Definition 11.3.1 (Vector-Valued Function)** A map $\boldsymbol{r}(t)=(x(t),y(t),z(t))$ from an interval $I\subset\mathbb{R}$ to $\mathbb{R}^3$ (or $\mathbb{R}^n$) is called a **vector-valued function** of one variable. If $\lim\limits_{\Delta t\to0}\dfrac{\boldsymbol{r}(t+\Delta t)-\boldsymbol{r}(t)}{\Delta t}$ exists, it is called the derivative of $\boldsymbol{r}$ at $t$, denoted $\boldsymbol{r}'(t)$.

As in Theorem 10.3.4 of [2.2.10](/2.2.10), limits, continuity and differentiability of vector-valued functions can all be checked component by component: $\boldsymbol{r}$ is continuous if and only if $x,y,z$ are, and $\boldsymbol{r}'(t)=(x'(t),y'(t),z'(t))$. If $\boldsymbol{r}(t)$ is the position of a particle, then $\boldsymbol{r}'(t)$ is its velocity and $\boldsymbol{r}''(t)$ its acceleration.

**Theorem 11.3.1 (Differentiation Rules)** Let $\boldsymbol{u}(t),\boldsymbol{v}(t)$ be differentiable vector-valued functions, $\varphi(t)$ a differentiable scalar function and $c$ a constant. Then

1. $(c\boldsymbol{u})'=c\boldsymbol{u}'$ and $(\boldsymbol{u}\pm\boldsymbol{v})'=\boldsymbol{u}'\pm\boldsymbol{v}'$;
2. $(\varphi\boldsymbol{u})'=\varphi'\boldsymbol{u}+\varphi\boldsymbol{u}'$;
3. $(\boldsymbol{u}\cdot\boldsymbol{v})'=\boldsymbol{u}'\cdot\boldsymbol{v}+\boldsymbol{u}\cdot\boldsymbol{v}'$;
4. $(\boldsymbol{u}\times\boldsymbol{v})'=\boldsymbol{u}'\times\boldsymbol{v}+\boldsymbol{u}\times\boldsymbol{v}'$ (the order of the factors must not be changed).

**Proof** Apply the product rule of one variable componentwise. For 3: $(\sum_ku_kv_k)'=\sum_ku_k'v_k+\sum_ku_kv_k'$. For 4, the first component is $(u_2v_3-u_3v_2)'=(u_2'v_3-u_3'v_2)+(u_2v_3'-u_3v_2')$, and the others are similar. $\square$

**Theorem 11.3.2** A differentiable vector-valued function $\boldsymbol{r}(t)$ has constant length if and only if $\boldsymbol{r}(t)\cdot\boldsymbol{r}'(t)\equiv0$.

**Proof** $\|\boldsymbol{r}\|^2=\boldsymbol{r}\cdot\boldsymbol{r}$ is constant if and only if $(\boldsymbol{r}\cdot\boldsymbol{r})'=2\boldsymbol{r}\cdot\boldsymbol{r}'\equiv0$. $\square$

For instance, for a particle in uniform circular motion, the position vector (measured from the center) is perpendicular to the velocity; and in any motion at constant speed, the acceleration is perpendicular to the velocity.

Integrals of vector-valued functions are also defined componentwise: $\displaystyle\int_a^b\boldsymbol{r}(t)\,\mathrm{d}t=\Big(\int_a^bx(t)\,\mathrm{d}t,\int_a^by(t)\,\mathrm{d}t,\int_a^bz(t)\,\mathrm{d}t\Big)$, and the **fundamental theorem of calculus** continues to hold.

**Example 11.3.1** A particle has velocity $\boldsymbol{v}(t)=(\cos t,\sin t,1)$ at time $t$ and is at $\boldsymbol{s}(0)=(1,0,2)$ at $t=0$. Find its position at $t=\pi$.

$$
\boldsymbol{s}(\pi)=\boldsymbol{s}(0)+\int_0^\pi\boldsymbol{v}(t)\,\mathrm{d}t=(1,0,2)+\big(\sin t,-\cos t,t\big)\Big|_0^\pi=(1,2,2+\pi).
$$

The trajectory of the particle is a helix.

## 11.4. Tangent Lines to Curves and Tangent Planes to Surfaces

### 11.4.1. Tangent Lines and Normal Planes of Parametric Curves

Let a space curve $L$ have parametric equation $\boldsymbol{r}(t)=(x(t),y(t),z(t))$, $t\in[\alpha,\beta]$, with the point $M_0$ corresponding to $t_0$. The limit of the secant direction $\dfrac{\boldsymbol{r}(t_0+\Delta t)-\boldsymbol{r}(t_0)}{\Delta t}$ as $\Delta t\to0$ is exactly $\boldsymbol{r}'(t_0)$.

**Definition 11.4.1 (Tangent Vector, Tangent Line and Normal Plane)** Let $x,y,z$ be differentiable at $t_0$ with $\boldsymbol{r}'(t_0)\ne\boldsymbol{0}$. The vector $\boldsymbol{r}'(t_0)=(x'(t_0),y'(t_0),z'(t_0))$ is called the **tangent vector** of the curve at $M_0$; the line through $M_0$ with this direction vector is the tangent line, and the plane through $M_0$ with this normal vector is the **normal plane**:

$$
\frac{x-x_0}{x'(t_0)}=\frac{y-y_0}{y'(t_0)}=\frac{z-z_0}{z'(t_0)},\qquad x'(t_0)(x-x_0)+y'(t_0)(y-y_0)+z'(t_0)(z-z_0)=0.
$$

The tangent vector $\boldsymbol{r}'(t_0)$ points in the direction of increasing parameter. If $\boldsymbol{r}\in C^1$ and $\boldsymbol{r}'\ne\boldsymbol{0}$ everywhere, the curve is called a **smooth curve**, and its **arc length** is $\displaystyle\int_\alpha^\beta\|\boldsymbol{r}'(t)\|\,\mathrm{d}t$. When the curve is given as $y=y(x)$, $z=z(x)$, we use $x$ as the parameter, and the tangent vector is $(1,y'(x),z'(x))$.

**Example 11.4.1** Find the tangent line to the helix $x=a\cos t$, $y=a\sin t$, $z=bt$ at $t=\frac\pi4$. The point of tangency is $\Big(\dfrac{a}{\sqrt2},\dfrac{a}{\sqrt2},\dfrac{b\pi}4\Big)$ and the tangent vector is $(-a\sin t,a\cos t,b)=\Big(-\dfrac{a}{\sqrt2},\dfrac{a}{\sqrt2},b\Big)$, so the tangent line is

$$
\frac{x-a/\sqrt2}{-a/\sqrt2}=\frac{y-a/\sqrt2}{a/\sqrt2}=\frac{z-b\pi/4}{b}.
$$

The angle $\gamma$ between the tangent vector of the helix and the $z$-axis satisfies $\cos\gamma=\dfrac{b}{\sqrt{a^2+b^2}}$, a constant.

### 11.4.2. Tangent Planes and Normal Vectors of Surfaces

**Definition 11.4.2 (Tangent Plane and Normal Vector)** Let $M_0$ be a point of a surface $S$. If the tangent lines at $M_0$ of all smooth curves on the surface through $M_0$ lie in one plane, this plane is called the **tangent plane** of $S$ at $M_0$; a normal vector of the tangent plane is called a **normal vector** of the surface at $M_0$, and the line through $M_0$ in the direction of the normal vector is called the normal line of the surface.

For an implicit surface $F(x,y,z)=0$, suppose $F$ has continuous partial derivatives, $F(M_0)=0$ and $\nabla F(M_0)\ne\boldsymbol{0}$. For any smooth curve $\boldsymbol{r}(t)$ on the surface through $M_0$, differentiating $F(\boldsymbol{r}(t))\equiv0$ by the chain rule gives $\nabla F(M_0)\cdot\boldsymbol{r}'(t_0)=0$. So all tangent lines are perpendicular to $\nabla F(M_0)$, the tangent plane exists, and its normal vector is $\boldsymbol{n}=\nabla F(M_0)$:

$$
F_x(M_0)(x-x_0)+F_y(M_0)(y-y_0)+F_z(M_0)(z-z_0)=0.
$$

This is precisely the statement that "the gradient is perpendicular to the level surfaces": the surface $F=0$ is a level surface of $F$.

For an explicit surface $z=f(x,y)$, put $F=f(x,y)-z$; the normal vector is $\boldsymbol{n}=(f_x,f_y,-1)$ and the tangent plane is $z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$, which is the plane obtained from the "geometric meaning of the differential" in [2.2.10](/2.2.10). The normal line is $\dfrac{x-x_0}{f_x}=\dfrac{y-y_0}{f_y}=\dfrac{z-z_0}{-1}$.

**Example 11.4.2** Find the tangent plane and normal line of the surface $z=1-x^2-y^2$ at $(1,2,-4)$. Here $z_x=-2x=-2$ and $z_y=-2y=-4$, so the tangent plane is $z+4=-2(x-1)-4(y-2)$, that is, $2x+4y+z=6$, and the normal line is $\dfrac{x-1}{2}=\dfrac{y-2}{4}=\dfrac{z+4}{1}$.

![Tangent plane (translucent) and normal line of a paraboloid of revolution at a point: near the point of tangency, the height difference between the surface and the tangent plane is an infinitesimal of higher order than the distance](./plots/tangent-plane.py)

**Example 11.4.3** Show that the sphere $x^2+y^2+z^2=R^2$ and the cone $x^2+y^2=a^2z^2$ are orthogonal (their normal vectors are perpendicular at the points of intersection). Their normal vectors are $(2x,2y,2z)$ and $(2x,2y,-2a^2z)$, whose inner product $4(x^2+y^2-a^2z^2)$ vanishes at the points of intersection.

### 11.4.3. Intersection Curves of Two Surfaces

Let a curve $L$ be given by $F(x,y,z)=0$, $G(x,y,z)=0$. Since it lies on both surfaces, its tangent vector at $M_0$ is perpendicular to both $\nabla F(M_0)$ and $\nabla G(M_0)$. When these are not collinear, the tangent vector is

$$
\boldsymbol{\tau}=\nabla F(M_0)\times\nabla G(M_0)=\Big(\det\frac{\partial(F,G)}{\partial(y,z)},\ \det\frac{\partial(F,G)}{\partial(z,x)},\ \det\frac{\partial(F,G)}{\partial(x,y)}\Big)\Big|_{M_0},
$$

and the tangent line is the intersection of the two tangent planes. The condition $\nabla F\times\nabla G\ne\boldsymbol{0}$ is exactly the condition in Theorem 10.8.3 of [2.2.10](/2.2.10) that some $2\times2$ Jacobian determinant be nonzero; in that case the curve can be represented near $M_0$ as a parametric curve.

**Example 11.4.4** Find the tangent line to the curve $x^2+y^2+z^2=6$, $z=x^2+y^2$ at $M_0(1,1,2)$. The two normal vectors are $(2,2,4)\parallel(1,1,2)$ and $(2x,2y,-1)=(2,2,-1)$, so

$$
\boldsymbol{\tau}=(1,1,2)\times(2,2,-1)=(-5,5,0)\parallel(1,-1,0),
$$

and the tangent line is $\dfrac{x-1}{1}=\dfrac{y-1}{-1}$, $z=2$.

### 11.4.4. Parametric Surfaces

Let a surface be given by $\boldsymbol{r}(u,v)=(x(u,v),y(u,v),z(u,v))$, with $M_0$ corresponding to $(u_0,v_0)$. Fixing $v=v_0$ gives a $u$-curve on the surface with tangent vector $\boldsymbol{r}_u=(x_u,y_u,z_u)$; likewise the tangent vector of the $v$-curve is $\boldsymbol{r}_v$. If the two are not collinear, they span the tangent plane, and the normal vector is

$$
\boldsymbol{n}=\boldsymbol{r}_u\times\boldsymbol{r}_v=\begin{vmatrix}\boldsymbol{i}&\boldsymbol{j}&\boldsymbol{k}\\ x_u&y_u&z_u\\ x_v&y_v&z_v\end{vmatrix}=\Big(\det\frac{\partial(y,z)}{\partial(u,v)},\ \det\frac{\partial(z,x)}{\partial(u,v)},\ \det\frac{\partial(x,y)}{\partial(u,v)}\Big).
$$

The condition $\boldsymbol{r}_u\times\boldsymbol{r}_v\ne\boldsymbol{0}$ is equivalent to the $3\times2$ Jacobian matrix of the map $(u,v)\mapsto\boldsymbol{r}(u,v)$ having rank $2$. In [2.2.13](/2.2.13) the area element of a surface will be exactly $\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\,\mathrm{d}u\,\mathrm{d}v$.

**Example 11.4.5** Find the tangent plane of the helicoid $x=u\cos v$, $y=u\sin v$, $z=v$ at the point corresponding to $(u_0,v_0)$. We have $\boldsymbol{r}_u=(\cos v,\sin v,0)$ and $\boldsymbol{r}_v=(-u\sin v,u\cos v,1)$, so

$$
\boldsymbol{n}=\boldsymbol{r}_u\times\boldsymbol{r}_v=(\sin v,-\cos v,u),
$$

and the tangent plane is $(x-x_0)\sin v_0-(y-y_0)\cos v_0+u_0(z-z_0)=0$, where $(x_0,y_0,z_0)=(u_0\cos v_0,u_0\sin v_0,v_0)$.

The cases are summarized below:

| Given as | Tangent vector or normal vector |
|---|---|
| Curve $\boldsymbol{r}(t)$ | Tangent vector $\boldsymbol{r}'(t_0)$ |
| Curve $F=G=0$ | Tangent vector $\nabla F\times\nabla G$ |
| Surface $z=f(x,y)$ | Normal vector $(f_x,f_y,-1)$ |
| Surface $F(x,y,z)=0$ | Normal vector $\nabla F$ |
| Surface $\boldsymbol{r}(u,v)$ | Normal vector $\boldsymbol{r}_u\times\boldsymbol{r}_v$ |

## 11.5. Extrema

### 11.5.1. Definition and Necessary Condition

**Definition 11.5.1 (Local Extremum)** Let $f$ be defined in a neighborhood $N(x_0,\delta)$ of $x_0$. If $f(x)\le f(x_0)$ ($f(x)\ge f(x_0)$) for all $x\in N(x_0,\delta)$, then $f(x_0)$ is called a **local maximum** (**local minimum**) of $f$, and $x_0$ a local maximum point (local minimum point); collectively these are called a **local extremum** and an extreme point.

A local extremum is a local property, and an extreme point must be an interior point of the domain.

**Theorem 11.5.1 (Necessary Condition for an Extremum)** If $f$ has a local extremum at $x_0$ and all partial derivatives of $f$ at $x_0$ exist, then $\nabla f(x_0)=\boldsymbol{0}$, that is, $f_{x_1}(x_0)=\cdots=f_{x_n}(x_0)=0$.

**Proof** With the other variables fixed, the one-variable function $x_i\mapsto f(x_1^0,\dots,x_i,\dots,x_n^0)$ has a local extremum at $x_i^0$, so by **Fermat's theorem on stationary points** in one variable its derivative $f_{x_i}(x_0)$ is $0$. $\square$

A point where the gradient vanishes is called a **stationary point** of $f$. As in one variable, a differentiable extreme point must be a stationary point, but a stationary point need not be an extreme point, and a point where partial derivatives fail to exist may also be an extreme point: $f=\sqrt{x^2+y^2}$ has a local minimum at the origin, where its partial derivatives do not exist.

**Definition 11.5.2 (Saddle Point)** If $x_0$ is a stationary point of $f$ but not an extreme point, $x_0$ is called a **saddle point** of $f$.

The origin is a saddle point of both $z=x^2-y^2$ and $z=xy$: the function increases in some directions and decreases in others, and the surface is shaped like a saddle.

### 11.5.2. Sufficient Conditions for Extrema

At a stationary point the first-order term vanishes, so by Theorem 11.2.4, $f(x_0+\boldsymbol{h})-f(x_0)\approx\frac12\boldsymbol{h}^{\mathsf T}H_f(x_0)\boldsymbol{h}$, and the type of extremum is determined by the sign of this quadratic form.

**Theorem 11.5.2 (Sufficient Conditions for an Extremum)** Let $f$ have continuous second-order partial derivatives in a neighborhood of $x_0$, with $\nabla f(x_0)=\boldsymbol{0}$.

1. If $H_f(x_0)$ is a **positive definite matrix**, then $x_0$ is a strict local minimum point;
2. if $H_f(x_0)$ is a **negative definite matrix**, then $x_0$ is a strict local maximum point;
3. if $H_f(x_0)$ is an **indefinite matrix**, then $x_0$ is a saddle point.

**Proof** 1: Since $H_f(x_0)$ is positive definite, the continuous function $\boldsymbol{e}\mapsto\boldsymbol{e}^{\mathsf T}H_f(x_0)\boldsymbol{e}$ on the unit sphere has a minimum $m>0$ (equal to the smallest eigenvalue of $H_f(x_0)$). By the Peano form in Theorem 11.2.4,

$$
f(x_0+\boldsymbol{h})-f(x_0)=\frac12\boldsymbol{h}^{\mathsf T}H_f(x_0)\boldsymbol{h}+o(\|\boldsymbol{h}\|^2)\ge\Big(\frac m2+o(1)\Big)\|\boldsymbol{h}\|^2,
$$

and the right side is positive for sufficiently small $\|\boldsymbol{h}\|$ with $\boldsymbol{h}\ne\boldsymbol{0}$. Case 2 is similar. 3: Choose $\boldsymbol{e}_1,\boldsymbol{e}_2$ with $\boldsymbol{e}_1^{\mathsf T}H\boldsymbol{e}_1>0>\boldsymbol{e}_2^{\mathsf T}H\boldsymbol{e}_2$. Then $f(x_0+t\boldsymbol{e}_1)-f(x_0)=\frac{t^2}2\boldsymbol{e}_1^{\mathsf T}H\boldsymbol{e}_1+o(t^2)>0$ and $f(x_0+t\boldsymbol{e}_2)-f(x_0)<0$ for sufficiently small $t$, so $x_0$ is not an extreme point. $\square$

Positive and negative definiteness can be tested by leading principal minors or by eigenvalues ([2.1.7](/2.1.7)). In two variables, write $A=f_{xx}(x_0,y_0)$, $B=f_{xy}(x_0,y_0)$, $C=f_{yy}(x_0,y_0)$, $H=\begin{bmatrix}A&B\\ B&C\end{bmatrix}$ and $\det H=AC-B^2$; we obtain:

**Corollary 11.5.1** Let a function $f$ of two variables have continuous second-order partial derivatives in a neighborhood of a stationary point $(x_0,y_0)$.

1. $AC-B^2>0$ and $A>0$: local minimum point; $AC-B^2>0$ and $A<0$: local maximum point;
2. $AC-B^2<0$: saddle point;
3. $AC-B^2=0$: no conclusion.

Theorem 11.5.2 does not cover the case where $H_f(x_0)$ is positive or negative semidefinite and singular ($\det H_f(x_0)=0$). Then the second-order term vanishes in some directions, the nature of the point is decided by higher-order terms, and anything can happen:

**Example 11.5.1** Each of the following functions has a stationary point at the origin, where its Hessian matrix is a singular semidefinite matrix ($\operatorname{diag}(2,0)$, $\operatorname{diag}(0,2)$ or $O$):

1. $f=x^2+y^4$: the origin is a local minimum point; $f=x^2-y^4$: the origin is a saddle point; $f=-(x^4+y^4)$: the origin is a local maximum point.
2. $f=2x^4-3x^2y+y^2=(y-x^2)(y-2x^2)$. Restricted to any line through the origin, the origin is a local minimum point: on the coordinate axes $f=2x^4$ or $y^2$, and on $y=kx$ ($k\ne0$) we have $g(x)=f(x,kx)=2x^4-3kx^3+k^2x^2$ with $g''(0)=2k^2>0$. But $f<0$ between the two parabolas $y=x^2$ and $y=2x^2$ and $f>0$ outside them, so the origin is not an extreme point.

The second example shows that a point at which the function has a local minimum along every line may fail to be a local minimum point, yet another difference between several variables and one.

**Algorithm 11.5.1 (Finding Extrema of a Function of Two Variables)** Let $f$ have continuous second-order partial derivatives.

1. Solve the system $f_x=0$, $f_y=0$ to find all stationary points; also list the points where the partial derivatives do not exist;
2. at each stationary point compute $A,B,C$ and apply Corollary 11.5.1;
3. for stationary points with $AC-B^2=0$ and for points where the partial derivatives do not exist, decide by the definition (examine the sign of $f(x)-f(x_0)$).

**Example 11.5.2** Find the extrema of $f(x,y)=x^3+y^3-3xy$. From $f_x=3x^2-3y=0$ and $f_y=3y^2-3x=0$ we get the stationary points $(0,0)$ and $(1,1)$. Here $f_{xx}=6x$, $f_{xy}=-3$ and $f_{yy}=6y$. At $(0,0)$, $AC-B^2=-9<0$, so it is a saddle point (along $y=x$, $f=2x^3-3x^2<0$; along $y=-x$, $f=3x^2>0$); at $(1,1)$, $AC-B^2=27>0$ and $A=6>0$, giving the local minimum $f(1,1)=-1$.

![Surface and level curves of z = x³ + y³ − 3xy: (1, 1) is a local minimum point and the origin is a saddle point, near which the level curves cross in an "×" shape](./plots/stationary-points.py)

**Example 11.5.3** Find the extrema of $f(x,y)=2x^4+y^4-2x^2-2y^2$. We have $f_x=8x^3-4x$ and $f_y=4y^3-4y$, so the stationary points are the $9$ combinations of $x\in\{0,\pm\frac1{\sqrt2}\}$ and $y\in\{0,\pm1\}$. With $f_{xx}=24x^2-4$, $f_{xy}=0$ and $f_{yy}=12y^2-4$, we get $AC-B^2=16(6x^2-1)(3y^2-1)$.

| Stationary point | $AC-B^2$ | $A$ | Conclusion |
|---|---|---|---|
| $(0,0)$ | $16$ | $-4$ | local maximum $0$ |
| $\big(\pm\frac1{\sqrt2},\pm1\big)$ (4 points) | $64$ | $8$ | local minimum $-\frac32$ |
| $(0,\pm1)$, $\big(\pm\frac1{\sqrt2},0\big)$ (4 points) | $-32$ | | saddle point |

**Example 11.5.4** Find the extrema of the implicit function $z=z(x,y)$ determined by $x^2-6xy+10y^2-2yz-z^2+18=0$. Differentiating with respect to $x$ and $y$:

$$
2x-6y-2yz_x-2zz_x=0,\qquad-6x+20y-2z-2yz_y-2zz_y=0.
$$

Setting $z_x=z_y=0$ gives $x=3y$ and $z=y$; substituting into the equation gives $y^2=9$, so the stationary points are $(9,3)$ (with $z=3$) and $(-9,-3)$ (with $z=-3$). Differentiating once more and substituting $z_x=z_y=0$:

$$
2-2(y+z)z_{xx}=0,\qquad-6-2(y+z)z_{xy}=0,\qquad20-2(y+z)z_{yy}=0
$$

(all terms containing $z_x$ or $z_y$ drop out). At $(9,3,3)$ we have $A=\frac16$, $B=-\frac12$, $C=\frac53$, $AC-B^2=\frac1{36}>0$ and $A>0$, so $z(9,3)=3$ is a local minimum; at $(-9,-3,-3)$ we have $A=-\frac16$, $B=\frac12$, $C=-\frac53$, so $z(-9,-3)=-3$ is a local maximum.

### 11.5.3. Least Squares Fitting

**Example 11.5.5 (Least Squares Line)** Given observations $(x_1,y_1),\dots,(x_n,y_n)$ (with the $x_i$ not all equal), find $a,b$ minimizing $Q(a,b)=\sum\limits_{i=1}^n\big(y_i-(ax_i+b)\big)^2$. This is the simplest instance of the method of **least squares**. From

$$
Q_a=-2\sum_i\big(y_i-ax_i-b\big)x_i=0,\qquad Q_b=-2\sum_i\big(y_i-ax_i-b\big)=0
$$

we obtain the **normal equations**

$$
\begin{bmatrix}\sum x_i^2&\sum x_i\\ \sum x_i&n\end{bmatrix}\begin{bmatrix}a\\ b\end{bmatrix}=\begin{bmatrix}\sum x_iy_i\\ \sum y_i\end{bmatrix},\qquad
a=\frac{n\sum x_iy_i-\sum x_i\sum y_i}{n\sum x_i^2-(\sum x_i)^2},\quad b=\frac{\sum x_i^2\sum y_i-\sum x_i\sum x_iy_i}{n\sum x_i^2-(\sum x_i)^2}.
$$

The Hessian matrix of $Q$ is twice the coefficient matrix above. By the **Cauchy–Schwarz inequality**, $n\sum x_i^2-(\sum x_i)^2>0$ (the $x_i$ are not all equal), so it is a positive definite constant matrix. By Taylor's formula, $Q(a+h,b+k)-Q(a,b)=\frac12(h,k)H(h,k)^{\mathsf T}>0$ for all $(h,k)\ne\boldsymbol{0}$, so the unique stationary point is the minimum point. This agrees with the conclusion obtained from orthogonal projection in [2.1.4](/2.1.4). Fitting an exponential curve $y=a\mathrm{e}^{bx}$ reduces to fitting a line by taking logarithms: $\ln y=\ln a+bx$.

## 11.6. Constrained Extrema and Lagrange Multipliers

### 11.6.1. The Problem and Its Geometric Meaning

Many problems ask for extrema of a function subject to conditions, for example extrema of $f(x,y,z)$ on a surface $g(x,y,z)=0$ or on a curve $g=h=0$.

**Definition 11.6.1 (Constrained Extremum)** Let $M_0$ satisfy the constraint $g(M_0)=0$. If there is a neighborhood of $M_0$ such that $f(M)\le f(M_0)$ (or $\ge$) for all points $M$ in it satisfying $g(M)=0$, then $f(M_0)$ is called a **constrained extremum** of $f$ subject to $g=0$, and $f$ is called the objective function. Several constraints are treated in the same way.

If some of the variables can be solved for from the constraints and substituted into the objective function, the problem becomes an unconstrained one (the direct method). For example, to find the extreme values of $f=y^2-x^2$ on the ellipse $\frac{x^2}4+y^2=1$, substitute $y^2=1-\frac{x^2}4$ to get $g(x)=1-\frac54x^2$, $x\in[-2,2]$, with maximum $g(0)=1$ and minimum $g(\pm2)=-4$. In general, however, the constraints cannot be solved explicitly, and we use the following method.

**Lemma 11.6.1** Let $f$ be differentiable at $M_0$.

1. If $M_0$ lies on a smooth curve $L$ and $f$ restricted to $L$ has a local extremum at $M_0$, then $\nabla f(M_0)$ is perpendicular to the tangent line of $L$ at $M_0$;
2. if $M_0$ lies on a surface $S$ that has a tangent plane at $M_0$, and $f$ restricted to $S$ has a local extremum at $M_0$, then $\nabla f(M_0)$ is perpendicular to the tangent plane.

**Proof** 1: Let $L$ be $\boldsymbol{r}(t)$ with $\boldsymbol{r}(t_0)=M_0$. The one-variable function $f(\boldsymbol{r}(t))$ has a local extremum at $t_0$, so its derivative $\nabla f(M_0)\cdot\boldsymbol{r}'(t_0)$ is $0$. 2: Apply 1 to every smooth curve on $S$ through $M_0$; the tangent lines of these curves span the tangent plane. $\square$

### 11.6.2. One Constraint

**Theorem 11.6.1 (Method of Lagrange Multipliers)** Let $f,g$ have continuous partial derivatives in a neighborhood of $M_0$, let $f$ have a constrained extremum at $M_0$ subject to $g=0$, and let $\nabla g(M_0)\ne\boldsymbol{0}$. Then there is a real number $\lambda$ such that

$$
\nabla f(M_0)=\lambda\nabla g(M_0).
$$

**Proof** We treat functions of three variables. Assume $g_z(M_0)\ne0$. By the implicit function theorem the constraint determines $z=z(x,y)$ near $M_0$, so the surface $g=0$ has a tangent plane at $M_0$ with normal vector $\nabla g(M_0)$. By Lemma 11.6.1, $\nabla f(M_0)$ is also perpendicular to this tangent plane, hence parallel to $\nabla g(M_0)$. $\square$

Geometrically, at a constrained extreme point the level surface (curve) of the objective function is tangent to the constraint surface (curve). If the two crossed transversally at $M_0$, moving along the constraint would cross the level surfaces of $f$, so $f$ could be both increased and decreased and $M_0$ would not be an extreme point. The number $\lambda$ is called a Lagrange multiplier. Introducing the Lagrange function

$$
L(x,y,z,\lambda)=f(x,y,z)-\lambda g(x,y,z),
$$

the conclusion of the theorem together with the constraint itself is exactly the system of stationarity equations $L_x=L_y=L_z=0$, $L_\lambda=-g=0$ of $L$ in all $4$ variables: the constrained extremum problem becomes an unconstrained stationary point problem.

**Algorithm 11.6.1 (Method of Lagrange Multipliers)** To find the extrema (extreme values) of $f$ subject to $g=0$:

1. write $L=f-\lambda g$ and solve the system $L_x=L_y=L_z=0$, $g=0$ to obtain the candidate constrained extreme points (also check the points where $\nabla g=\boldsymbol{0}$);
2. decide which of these points are the required extreme points. In applied problems, if the nature of the problem guarantees that the extreme value exists (for example, the constraint set is bounded and closed, or the extreme value is clearly attained in the interior) and there are only finitely many candidates, it suffices to compare function values.

**Example 11.6.1** Find the extreme values of $f(x,y)=xy$ on the circle $(x-1)^2+y^2=1$. From $\nabla f=(y,x)$ and $\nabla g=(2(x-1),2y)$ we get

$$
y=2\lambda(x-1),\qquad x=2\lambda y,\qquad(x-1)^2+y^2=1.
$$

Eliminating $\lambda$ from the first two equations gives $y^2=x(x-1)$, and substituting into the constraint gives $2x^2-3x=0$. For $x=0$: $y=0$ and $f=0$; for $x=\frac32$: $y=\pm\frac{\sqrt3}2$ and $f=\pm\frac{3\sqrt3}{4}$. The circle is a bounded closed set, so the extreme values exist: the maximum is $\frac{3\sqrt3}4$ and the minimum is $-\frac{3\sqrt3}4$. The point $(0,0)$ also satisfies the system but is not a constrained extreme point: near it the circle can be written $x=1+\cos t$, $y=\sin t$ ($t$ close to $\pi$), and $f\approx-\frac12(t-\pi)^3$ changes sign.

![Level curves of f = xy and the constraint circle (x − 1)² + y² = 1: at the maximum and minimum points the level curves are tangent to the circle and ∇f is parallel to ∇g](./plots/lagrange-tangency.py)

**Example 11.6.2** The box requiring the least material: when is the surface area $S=2(xy+yz+zx)$ of a rectangular box of volume $a$ smallest? From $\nabla S=\lambda\nabla(xyz)$ we get $2(y+z)=\lambda yz$, $2(x+z)=\lambda xz$ and $2(x+y)=\lambda xy$. Subtracting the first two gives $2(y-x)=\lambda z(y-x)$; if $x\ne y$ then $\lambda z=2$, and substituting back into the first equation gives $2y=0$, a contradiction. So $x=y$, and likewise $y=z$; that is, $x=y=z=\sqrt[3]{a}$, and the cube uses the least material (the surface area tends to infinity as any of $x,y,z\to0^+$ or $\to+\infty$, so the minimum exists).

**Example 11.6.3** Let $a>0$. Find the maximum of the product $\prod x_i$ of positive numbers $x_1,\dots,x_n$ with $\sum x_i=a$. Let $L=\prod x_i-\lambda(\sum x_i-a)$. Then $L_{x_i}=\prod_{j\ne i}x_j-\lambda=0$; multiplying each equation by $x_i$ gives $\prod_jx_j=\lambda x_i$, so $x_1=\cdots=x_n=\frac an$ and the maximum is $\big(\frac an\big)^n$ (the product tends to $0$ at the boundary $x_i\to0$). Hence $\sqrt[n]{x_1\cdots x_n}\le\frac{x_1+\cdots+x_n}{n}$ for any positive numbers $x_i$, which is the **AM–GM inequality**.

**Example 11.6.4 (Law of Refraction)** Light travels with speeds $v_1$ in air and $v_2$ in water. It goes from a point $A$ in the air through a point $C$ on the water surface to a point $B$ in the water. Let $a$ and $b$ be the distances from $A$ and $B$ to the surface, $c$ the horizontal distance between the two points, $\alpha$ the angle of incidence and $\beta$ the angle of refraction. Assuming that light follows the path of least time, we minimize $T=\dfrac{a}{v_1\cos\alpha}+\dfrac{b}{v_2\cos\beta}$ subject to $a\tan\alpha+b\tan\beta=c$. From

$$
\frac{a\sin\alpha}{v_1\cos^2\alpha}=\lambda\frac{a}{\cos^2\alpha},\qquad\frac{b\sin\beta}{v_2\cos^2\beta}=\lambda\frac{b}{\cos^2\beta}
$$

we get $\dfrac{\sin\alpha}{v_1}=\dfrac{\sin\beta}{v_2}$, which is Snell's law of refraction.

### 11.6.3. Several Constraints

**Theorem 11.6.2** Let $f,g,h$ have continuous partial derivatives near $M_0$, let $f$ have a constrained extremum at $M_0$ subject to $g=0$ and $h=0$, and let $\nabla g(M_0)$ and $\nabla h(M_0)$ be non-collinear. Then there are $\lambda,\mu$ such that

$$
\nabla f(M_0)=\lambda\nabla g(M_0)+\mu\nabla h(M_0).
$$

**Proof** The tangent vector of the constraint curve $g=h=0$ at $M_0$ is $\boldsymbol{\tau}=\nabla g\times\nabla h\ne\boldsymbol{0}$. By Lemma 11.6.1, $\nabla f\cdot\boldsymbol{\tau}=0$, so $\nabla f$ lies in the plane perpendicular to $\boldsymbol{\tau}$, which is spanned by $\nabla g$ and $\nabla h$. $\square$

In general, at a constrained extreme point $M_0$ of a function of $n$ variables subject to $m$ constraints $g_1=\cdots=g_m=0$ ($m<n$), if the $m\times n$ Jacobian matrix $\dfrac{\partial(g_1,\dots,g_m)}{\partial(x_1,\dots,x_n)}$ of the constraints has **full rank** (the $\nabla g_i$ are linearly independent), then there are $\lambda_1,\dots,\lambda_m$ with $\nabla f=\sum\lambda_i\nabla g_i$. The idea of the proof: use the implicit function theorem to express $m$ of the variables in terms of the remaining $n-m$, apply the necessary condition to the resulting unconstrained composite function, and then solve for the multipliers. The Lagrange function is $L=f-\sum_i\lambda_ig_i$.

**Example 11.6.5** Find the maximum of $f=xyz$ on the line $x+y+z=30$, $x+y-z=0$. From $\nabla f=\lambda(1,1,1)+\mu(1,1,-1)$ we get $yz=xz=\lambda+\mu$, so $z(x-y)=0$. If $z=0$, the constraints give $x+y=30$ and $x+y=0$, a contradiction; hence $x=y$, and solving gives $z=15$, $x=y=\frac{15}2$ and $f_{\max}=\frac{3375}4$. (One can also check this by parametrizing the line directly: $f=15x(15-x)$.)

**Example 11.6.6 (Distance from a Point to a Plane)** Find the distance from $P_0(x_0,y_0,z_0)$ to the plane $Ax+By+Cz+D=0$. Minimize $d^2=(x-x_0)^2+(y-y_0)^2+(z-z_0)^2$ subject to the constraint:

$$
2(x-x_0)=\lambda A,\qquad 2(y-y_0)=\lambda B,\qquad 2(z-z_0)=\lambda C.
$$

Multiplying the three equations by $A,B,C$ respectively, adding, and using $Ax+By+Cz=-D$ gives $\lambda=-\dfrac{2(Ax_0+By_0+Cz_0+D)}{A^2+B^2+C^2}$, and therefore

$$
d=\frac{|\lambda|}{2}\sqrt{A^2+B^2+C^2}=\frac{|Ax_0+By_0+Cz_0+D|}{\sqrt{A^2+B^2+C^2}}.
$$

**Example 11.6.7** The plane $x+y+z=1$ cuts the paraboloid $z=x^2+y^2$ in an ellipse. Find the largest and smallest distances from points of the ellipse to the origin. Let

$$
L=x^2+y^2+z^2-\lambda_1(z-x^2-y^2)-\lambda_2(x+y+z-1).
$$

Then $L_x=2x+2\lambda_1x-\lambda_2=0$ and $L_y=2y+2\lambda_1y-\lambda_2=0$; subtracting gives $(1+\lambda_1)(x-y)=0$. If $\lambda_1=-1$, then $\lambda_2=0$, and $L_z=2z+1=0$ gives $z=-\frac12<0$, contradicting $z=x^2+y^2$. So $x=y$, and substituting into the two constraints gives $2x^2+2x-1=0$, $x=y=\frac{-1\pm\sqrt3}2$ and $z=2\mp\sqrt3$. The squared distance is $d^2=x^2+y^2+z^2=z+z^2=9\mp5\sqrt3$, so the largest distance is $\sqrt{9+5\sqrt3}$ and the smallest is $\sqrt{9-5\sqrt3}$.

## 11.7. Extreme Values on Bounded Closed Regions

By the extreme value theorem, a continuous function on a bounded closed region $D$ attains a maximum and a minimum. An extreme value attained in the interior must occur at an extreme point; one attained on the boundary occurs at a constrained extreme point of $f$ restricted to the boundary.

**Algorithm 11.7.1 (Extreme Values on a Bounded Closed Region)** Let $f$ be continuous on a bounded closed region $D$.

1. Find the stationary points in the interior of $D$ and the points where the partial derivatives do not exist;
2. find the candidate extreme points of $f$ on the boundary $\partial D$: when the boundary is given by an equation, use Lagrange multipliers or a parametrization; when the boundary consists of several pieces, also include the endpoints (corners) of the pieces;
3. compare the values of $f$ at all these points: the largest is the maximum and the smallest is the minimum. There is no need to decide whether these points are extreme points.

**Example 11.7.1** Find the extreme values of $z=x^2+y^2-12x+16y$ on $x^2+y^2\le25$. The stationary point $(6,-8)$ lies outside the region. On the boundary, let $L=z-\lambda(x^2+y^2-25)$; from $2x-12=2\lambda x$ and $2y+16=2\lambda y$ we get $y=-\frac43x$, and substituting into the constraint gives $(3,-4)$ and $(-3,4)$. Since $z(3,-4)=-75$ and $z(-3,4)=125$, the maximum is $125$ and the minimum is $-75$. Alternatively, on the boundary $z=25-12x+16y$ is a linear function, and the Cauchy–Schwarz inequality gives the result directly.

**Example 11.7.2** On the closed triangle with vertices $P_1(0,0)$, $P_2(1,0)$, $P_3(0,1)$, find the points at which the sum of squared distances to the three vertices is largest and smallest. The objective function is $z=3x^2+3y^2-2x-2y+2$. The interior stationary point is the centroid $M_0\big(\frac13,\frac13\big)$; on the side $P_1P_2$ ($y=0$), $z=3x^2-2x+2$ with stationary point $\big(\frac13,0\big)$; on the side $P_1P_3$ the stationary point is $\big(0,\frac13\big)$; on the side $P_2P_3$ ($y=1-x$), $z=6x^2-6x+3$ with stationary point $\big(\frac12,\frac12\big)$. Comparing these with the three vertices:

| Point | $P_1$ | $P_2$, $P_3$ | $M_0$ | $\big(\frac13,0\big)$, $\big(0,\frac13\big)$ | $\big(\frac12,\frac12\big)$ |
|---|---|---|---|---|---|
| $z$ | $2$ | $3$ | $\frac43$ | $\frac53$ | $\frac32$ |

The maximum $3$ is attained at $P_2$ and $P_3$, and the minimum $\frac43$ at the centroid.

For a function of one variable on an interval, a unique extreme point must be a point of global extremum (otherwise the function would be smaller somewhere else, and there would have to be another extreme point in between). Functions of several variables have no such property:

**Example 11.7.3** The function $f(x,y)=3(x^2+y^2)-x^3$ has stationary points $(0,0)$ and $(2,0)$. At $(0,0)$, $A=C=6$ and $B=0$, so it is a local minimum point; at $(2,0)$, $A=-6$ and $C=6$, so it is a saddle point. Thus $(0,0)$ is the only extreme point of $f$, and it is a local minimum point. But on the boundary of $D=\{x^2+y^2\le16\}$ we have $f=48-x^3$, and $f(4,0)=-16<f(0,0)=0$. Comparing $f(0,0)=0$, $f(2,0)=4$ and the boundary values $f(4,0)=-16$ and $f(-4,0)=112$, the maximum is $112$ and the minimum is $-16$, both attained on the boundary. Intuitively, starting from the local minimum point the function can "go around" the saddle point and descend elsewhere; the plane offers more paths than a line.

## Summary

| Problem | Method | Key points |
|---|---|---|
| Tangent line to a curve | $\boldsymbol{r}'(t_0)$, or $\nabla F\times\nabla G$ | Tangent vector nonzero |
| Tangent plane to a surface | $\nabla F$, $(f_x,f_y,-1)$, $\boldsymbol{r}_u\times\boldsymbol{r}_v$ | The gradient is perpendicular to level surfaces |
| Taylor's formula | Reduce to one variable via $g(t)=f(x_0+t\boldsymbol{h})$ | Second-order term $\frac12\boldsymbol{h}^{\mathsf T}H_f\boldsymbol{h}$; the expansion is unique |
| Unconstrained extrema | $\nabla f=\boldsymbol{0}$, then examine $H_f$ | Positive definite: minimum; negative definite: maximum; indefinite: saddle point; semidefinite and singular: inconclusive |
| Constrained extrema | $\nabla f=\sum\lambda_i\nabla g_i$, $g_i=0$ | Jacobian matrix of the constraints of full rank; level surface tangent to the constraint |
| Extreme values on a closed region | Interior stationary points, nondifferentiable points, constrained stationary points on the boundary, corners | Compare function values; a unique extreme point need not give an extreme value |

| Two-variable test (at a stationary point) | $AC-B^2>0$ | $AC-B^2<0$ | $AC-B^2=0$ |
|---|---|---|---|
| Conclusion | $A>0$ minimum, $A<0$ maximum | saddle point | further analysis needed |
