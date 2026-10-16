---
title: Multiple Integrals and Integrals Depending on a Parameter
source_hash: 2cf595dd7dc2
---

The definite integral is the quantity obtained on an interval by "partition, approximate, sum, take the limit". Replacing the interval by a plane or spatial region, the same four steps give double and triple integrals, collectively called multiple integrals: the volume of a solid under a curved top, the mass of a nonuniform plate or body, centers of mass and moments of inertia are all expressed by them. The definition and properties of multiple integrals are copied almost verbatim from those of the definite integral; the difficulty lies in computation. There are two basic strategies. One is to reduce the integral to iterated integrals, that is, to compute definite integrals one after another, the key being to read off the limits of integration from the shape of the region. The other is a change of variables that transforms the region into a simple shape, at the cost of multiplying the area or volume element by the absolute value of the **Jacobian determinant**; this is the local manifestation of the meaning of the **determinant** in linear algebra as a [volume scaling factor](/2.1.5#sec-5.3.1).

This chapter relies on the one-variable **definite integral** and **improper integral** ([2.2.7](/2.2.7)) and on the Jacobian matrix of [2.2.10](/2.2.10). The last section discusses integrals depending on a parameter, which are formally one-dimensional but whose proofs use multiple integrals and continuity in several variables. The results of this chapter are the computational tools for joint distributions, marginal distributions and distributions of functions of random vectors in probability theory (3.1); in particular, the Gaussian integral $\int_{-\infty}^{+\infty}\mathrm{e}^{-x^2}\,\mathrm{d}x=\sqrt\pi$ underlies the normal distribution. Integrals over curves and surfaces are treated in [2.2.13](/2.2.13).

## 12.1. Concept and Properties of Multiple Integrals

### 12.1.1. Definition of Double and Triple Integrals

Two motivating examples. Let $z=f(x,y)\ge0$ be continuous on a bounded closed region $D$, and consider the volume $V$ of the solid with base $D$ and top the surface $z=f(x,y)$. Divide $D$ into small regions $D_1,\dots,D_k$ of areas $\Delta\sigma_i$ and choose a point $P_i$ in each; approximating each small solid by a flat-topped cylinder gives $V\approx\sum f(P_i)\Delta\sigma_i$. The mass of a plate with surface density $\mu(x,y)$ is likewise approximately $\sum\mu(P_i)\Delta\sigma_i$. As the partition becomes finer, the limit of the approximations is the required quantity.

**Definition 12.1.1 (Double Integral)** Let $D\subset\mathbb{R}^2$ be a bounded closed region and $f$ a function defined on $D$. Divide $D$ arbitrarily into $k$ small regions $D_1,\dots,D_k$ (a partition $T$), let $\Delta\sigma_i$ be the area of $D_i$ and $\lambda(T)=\max_i\operatorname{diam}D_i$ the largest diameter of the pieces, choose arbitrary points $P_i\in D_i$, and form the sum $\sum_{i=1}^kf(P_i)\Delta\sigma_i$. If there is a constant $I$ such that for every $\varepsilon>0$ there is $\delta>0$ with

$$
\Big|\sum_{i=1}^kf(P_i)\Delta\sigma_i-I\Big|<\varepsilon
$$

for every partition with $\lambda(T)<\delta$ and every choice of points $P_i$, then $f$ is said to be (Riemann) integrable on $D$, written $f\in\mathcal{R}(D)$, and $I$ is called the **double integral** of $f$ over $D$, written

$$
\iint_Df(x,y)\,\mathrm{d}\sigma=\lim_{\lambda(T)\to0}\sum_{i=1}^kf(P_i)\Delta\sigma_i.
$$

$f$ is called the integrand and $\mathrm{d}\sigma$ the area element. The sum above is the two-dimensional version of the **Riemann sum**; the definition contains two arbitrary choices, the partition and the sample points.

**Definition 12.1.2 (Triple Integral)** Let $\Omega\subset\mathbb{R}^3$ be a bounded closed region. Divide $\Omega$ arbitrarily into small regions $\Omega_1,\dots,\Omega_k$ of volumes $\Delta V_i$ and choose arbitrary $P_i\in\Omega_i$. If $\sum f(P_i)\Delta V_i$ has a limit as $\lambda(T)\to0$ (independent of the partition and the sample points), $f$ is said to be integrable on $\Omega$, and the limit is called the **triple integral** of $f$ over $\Omega$, written $\iiint_\Omega f(x,y,z)\,\mathrm{d}V$.

Double and triple integrals are collectively called *multiple integrals*. $\iint_D1\,\mathrm{d}\sigma$ is the area of $D$ and $\iiint_\Omega1\,\mathrm{d}V$ the volume of $\Omega$; for $f\ge0$, $\iint_Df\,\mathrm{d}\sigma$ is the volume of the solid under the graph, and $\iiint_\Omega\rho\,\mathrm{d}V$ is the mass of a body with density $\rho$.

### 12.1.2. Integrability and Properties

As for the definite integral, an integrable function is necessarily bounded; but a bounded function need not be integrable. For example, the function on $D=[0,1]^2$ equal to $1$ when $x,y$ are both rational and $0$ otherwise (a two-dimensional version of the **Dirichlet function**) has oscillation $1$ on every small region, and its Riemann sums have no limit. A commonly used sufficient condition is:

**Theorem 12.1.1** If $f$ is continuous on a bounded closed region $D$, then $f\in\mathcal{R}(D)$. More generally, if $f$ is bounded on $D$ and its points of discontinuity lie on finitely many smooth curves, then $f\in\mathcal{R}(D)$.

In this course, the boundaries of regions always consist of finitely many smooth curves (surfaces) and the integrands are piecewise continuous, so the multiple integrals always exist. We state the properties for double integrals; those for triple integrals are identical. Let $f,g\in\mathcal{R}(D)$ and let $\sigma$ be the area of $D$.

**Property 12.1.1 (Linearity)** $\iint_D(\alpha f+\beta g)\,\mathrm{d}\sigma=\alpha\iint_Df\,\mathrm{d}\sigma+\beta\iint_Dg\,\mathrm{d}\sigma$.

**Property 12.1.2 (Additivity over Regions)** If $D=D_1\cup\cdots\cup D_k$ and the pairwise intersections of the $D_i$ have zero area, then $\iint_Df\,\mathrm{d}\sigma=\sum_{i=1}^k\iint_{D_i}f\,\mathrm{d}\sigma$.

**Property 12.1.3 (Monotonicity)** If $f\le g$ on $D$, then $\iint_Df\,\mathrm{d}\sigma\le\iint_Dg\,\mathrm{d}\sigma$. In particular, $|f|\in\mathcal{R}(D)$ and $\Big|\iint_Df\,\mathrm{d}\sigma\Big|\le\iint_D|f|\,\mathrm{d}\sigma$.

**Property 12.1.4 (Estimation Theorem)** If $m\le f\le M$ on $D$, then $m\sigma\le\iint_Df\,\mathrm{d}\sigma\le M\sigma$.

**Property 12.1.5 (Mean Value Theorem for Integrals)** If $f$ is continuous on $D$, then there is $(\xi,\eta)\in D$ with $\iint_Df\,\mathrm{d}\sigma=f(\xi,\eta)\sigma$.

Property 12.1.5 follows from the estimation theorem and the **intermediate value theorem** on bounded closed regions; it says that the mean value $\frac1\sigma\iint_Df\,\mathrm{d}\sigma$ of a continuous function on $D$ is attained at some point.

**Property 12.1.6 (Symmetry)** Let $D$ be symmetric about the $y$-axis and let $D_1$ be the part of $D$ to the right of the $y$-axis. If $f(-x,y)=-f(x,y)$ ($f$ is odd in $x$), then $\iint_Df\,\mathrm{d}\sigma=0$; if $f(-x,y)=f(x,y)$, then $\iint_Df\,\mathrm{d}\sigma=2\iint_{D_1}f\,\mathrm{d}\sigma$. Symmetry about the $x$-axis or the origin is handled similarly; for triple integrals there is also symmetry about the coordinate planes.

**Property 12.1.7 (Symmetry under Interchange of Variables)** If $D$ is symmetric about the line $y=x$ (that is, $(x,y)\in D\Leftrightarrow(y,x)\in D$), then $\iint_Df(x,y)\,\mathrm{d}\sigma=\iint_Df(y,x)\,\mathrm{d}\sigma$.

When using symmetry, the symmetry of the region and the parity of the integrand must refer to the same variable. Symmetry under interchange of variables is specific to integrals in several variables: a definite integral has only one variable, so there is nothing to interchange.

**Example 12.1.1** Let $D=\{x^2+y^2\le R^2\}$.

1. If $m,n$ are nonnegative integers at least one of which is odd, then $\iint_Dx^my^n\,\mathrm{d}\sigma=0$ (if $m$ is odd, the integrand is odd in $x$ and $D$ is symmetric about the $y$-axis).
2. By symmetry under interchange of variables, $\iint_Dx^2\,\mathrm{d}\sigma=\iint_Dy^2\,\mathrm{d}\sigma=\frac12\iint_D(x^2+y^2)\,\mathrm{d}\sigma$, and the latter is easily computed in polar coordinates ([12.2.4](#sec-12.2.4)) to be $\frac{\pi R^4}{4}$.

**Example 12.1.2** Estimate $I=\iint_D\dfrac{\mathrm{d}\sigma}{100+\cos^2x+\cos^2y}$ with $D=\{|x|+|y|\le10\}$. $D$ is a square with diagonals of length $20$ and area $200$; the integrand lies between $\frac1{102}$ and $\frac1{100}$, so $\frac{200}{102}\le I\le2$.

The table compares the properties of definite and multiple integrals (for line and surface integrals see [2.2.13](/2.2.13)):

| Property | Definite integral $\int_a^b$ | Multiple integral |
|---|---|---|
| Orientation | $\int_a^b=-\int_b^a$ | None; $\mathrm{d}\sigma,\mathrm{d}V>0$ |
| Linearity, additivity, monotonicity, estimation, mean value | Yes | Yes |
| Symmetry | About the origin (odd and even functions) | About coordinate axes, the origin, coordinate planes |
| Symmetry under interchange of variables | No | Yes |

## 12.2. Evaluation of Double Integrals

### 12.2.1. Iterated Integrals over Rectangles

The basic method of evaluating a double integral is to reduce it to an *iterated integral*: fix one variable and integrate with respect to the other, then integrate with respect to the remaining variable. Intuitively, cutting the solid by the plane $x=x_0$ gives a cross section of area $A(x_0)=\int_c^df(x_0,y)\,\mathrm{d}y$, and the formula for the "volume of a solid with known cross-sectional areas" $V=\int_a^bA(x)\,\mathrm{d}x$ ([2.2.7](/2.2.7)) then gives the volume.

**Theorem 12.2.1** Let $f$ be continuous on the rectangle $D=[a,b]\times[c,d]$. Then

$$
\iint_Df(x,y)\,\mathrm{d}\sigma=\int_a^b\Big(\int_c^df(x,y)\,\mathrm{d}y\Big)\mathrm{d}x=\int_c^d\Big(\int_a^bf(x,y)\,\mathrm{d}x\Big)\mathrm{d}y.
$$

**Proof** Let $F(x)=\int_c^df(x,y)\,\mathrm{d}y$; it is continuous on $[a,b]$ (Theorem 12.6.1). Partition $D$ into small rectangles $D_{ij}$ by $a=x_0<\cdots<x_m=b$ and $c=y_0<\cdots<y_l=d$, and let $m_{ij}$, $M_{ij}$ be the infimum and supremum of $f$ on $D_{ij}$. For $x\in[x_{i-1},x_i]$,

$$
\sum_jm_{ij}\Delta y_j\le F(x)\le\sum_jM_{ij}\Delta y_j.
$$

Integrating in $x$ and summing over $i$ gives $\sum_{i,j}m_{ij}\Delta x_i\Delta y_j\le\int_a^bF(x)\,\mathrm{d}x\le\sum_{i,j}M_{ij}\Delta x_i\Delta y_j$. The two sides are **Darboux sums** of the double integral, and both tend to $\iint_Df\,\mathrm{d}\sigma$ as the partition is refined. The other order is similar. $\square$

The iterated integral $\int_a^b\Big(\int_c^df\,\mathrm{d}y\Big)\mathrm{d}x$ is usually abbreviated $\int_a^b\mathrm{d}x\int_c^df(x,y)\,\mathrm{d}y$ and called the iterated integral first in $y$, then in $x$. In Cartesian coordinates the area element is written $\mathrm{d}\sigma=\mathrm{d}x\,\mathrm{d}y$, corresponding to a partition of the region by lines parallel to the coordinate axes. Theorems of this kind, reducing a multiple integral to iterated integrals, are generally called *Fubini's theorem*.

### 12.2.2. Iterated Integrals over General Regions

**Theorem 12.2.2** Let $f$ be continuous on $D$.

1. If $D=\{(x,y)\mid a\le x\le b,\ y_1(x)\le y\le y_2(x)\}$ (a type X region: every line parallel to the $y$-axis passing through the interior of $D$ meets the boundary in exactly two points) with $y_1,y_2$ continuous, then
$$
\iint_Df\,\mathrm{d}\sigma=\int_a^b\mathrm{d}x\int_{y_1(x)}^{y_2(x)}f(x,y)\,\mathrm{d}y;
$$
2. if $D=\{(x,y)\mid c\le y\le d,\ x_1(y)\le x\le x_2(y)\}$ (a type Y region), then $\iint_Df\,\mathrm{d}\sigma=\int_c^d\mathrm{d}y\int_{x_1(y)}^{x_2(y)}f(x,y)\,\mathrm{d}x$.

**Proof** Take a rectangle $[a,b]\times[c,d]$ containing $D$ and extend $f$ by $0$ outside $D$. The extended function can be discontinuous only on the boundary of $D$, so it is still integrable, and the method of Theorem 12.2.1 applies. $\square$

**Algorithm 12.2.1 (Reducing a Double Integral to an Iterated Integral)**

1. Sketch the region of integration $D$ and find the intersection points of the boundary curves;
2. choose the order of integration: if every line parallel to the $y$-axis meets the boundary of $D$ in at most two points, integrate first in $y$ and then in $x$; otherwise split $D$ into pieces by lines parallel to the coordinate axes and treat them separately; take the integrand into account as well, and choose the order that is easier to integrate;
3. determine the limits. The limits of the outer integral are the projection interval of $D$ on the corresponding axis (constants); through any point of the projection interval draw a line parallel to the other axis: the boundary where it enters $D$ gives the lower limit of the inner integral and the boundary where it leaves gives the upper limit (in general functions of the outer variable);
4. evaluate the iterated integral. The lower limit must not exceed the upper limit.

**Example 12.2.1** Write $\iint_Df\,\mathrm{d}\sigma$ as iterated integrals:

1. $D$ is bounded by $y=x$, $y=3x$, $x=1$ and $x=3$: integrating first in $y$ needs only one integral, $\int_1^3\mathrm{d}x\int_x^{3x}f\,\mathrm{d}y$; integrating first in $x$ requires two pieces, $\int_1^3\mathrm{d}y\int_1^{y}f\,\mathrm{d}x+\int_3^9\mathrm{d}y\int_{y/3}^{3}f\,\mathrm{d}x$.
2. $D$ is the ellipse $\frac{x^2}4+\frac{y^2}6\le1$: $\int_{-2}^2\mathrm{d}x\int_{-\sqrt{6(1-x^2/4)}}^{\sqrt{6(1-x^2/4)}}f\,\mathrm{d}y$.

**Example 12.2.2** Evaluate the following double integrals.

1. $\iint_D|xy|\,\mathrm{d}\sigma$, $D=\{x^2+y^2\le a^2\}$: by symmetry it equals $4$ times the integral over the first quadrant, $4\int_0^a\mathrm{d}x\int_0^{\sqrt{a^2-x^2}}xy\,\mathrm{d}y=4\int_0^a\frac{x(a^2-x^2)}2\,\mathrm{d}x=\frac{a^4}2$.
2. $\iint_Dx\mathrm{e}^{xy}\,\mathrm{d}\sigma$, $D=[0,1]\times[-1,0]$: integrating first in $y$, $\int_0^1\mathrm{d}x\int_{-1}^0x\mathrm{e}^{xy}\,\mathrm{d}y=\int_0^1(1-\mathrm{e}^{-x})\,\mathrm{d}x=\frac1{\mathrm{e}}$. Integrating first in $x$ would require integration by parts and be much more laborious.
3. $\iint_D\frac xy\,\mathrm{d}\sigma$, $D$ bounded by $y=1$, $x=2$ and $y=x^2$: integrating first in $x$, $\int_1^4\mathrm{d}y\int_{\sqrt y}^2\frac xy\,\mathrm{d}x=\int_1^4\frac{4-y}{2y}\,\mathrm{d}y=4\ln2-\frac32$.

### 12.2.3. Changing the Order of Integration

The same region is often both of type X and of type Y (possibly after splitting), and the iterated integrals in the two orders are equal. To change the order of integration, sketch the region from the limits of the given iterated integral and then determine the limits anew in the other order.

**Example 12.2.3** Change the order of integration in $I=\int_0^1\mathrm{d}y\int_{y^2/2}^{\sqrt{3-y^2}}f(x,y)\,\mathrm{d}x$. The region is bounded by the parabola $y^2=2x$, the circle $x^2+y^2=3$ and the lines $y=0$ and $y=1$, which meet pairwise at $\big(\frac12,1\big)$, $(\sqrt2,1)$ and $(\sqrt3,0)$. Integrating first in $y$, the upper boundary consists of three arcs, so the region must be split into three pieces:

$$
I=\int_0^{1/2}\mathrm{d}x\int_0^{\sqrt{2x}}f\,\mathrm{d}y+\int_{1/2}^{\sqrt2}\mathrm{d}x\int_0^1f\,\mathrm{d}y+\int_{\sqrt2}^{\sqrt3}\mathrm{d}x\int_0^{\sqrt{3-x^2}}f\,\mathrm{d}y.
$$

![The region of Example 12.2.3: slicing into horizontal strips (first in x, then in y) needs only one iterated integral, while slicing into vertical strips (first in y, then in x) needs three pieces](./plots/integration-order.py)

Sometimes the order must be changed to make the integral computable at all, because certain functions (such as $\mathrm{e}^{y^2}$ and $\frac{\sin y}y$) have no elementary antiderivatives.

**Example 12.2.4** Evaluate $\int_0^2\mathrm{d}x\int_x^2\mathrm{e}^{y^2}\,\mathrm{d}y$. The inner integral cannot be computed in closed form. The region is $0\le x\le y\le2$; changing the order,

$$
\int_0^2\mathrm{d}y\int_0^y\mathrm{e}^{y^2}\,\mathrm{d}x=\int_0^2y\mathrm{e}^{y^2}\,\mathrm{d}y=\frac{\mathrm{e}^4-1}2.
$$

### 12.2.4. Double Integrals in Polar Coordinates

When the boundary of the region consists of circles or rays and the integrand involves $x^2+y^2$, it is more convenient to use **polar coordinates** $x=r\cos\theta$, $y=r\sin\theta$. Partition the region by circles centered at the origin and rays from the origin; the piece between $r$ and $r+\Delta r$ and between $\theta$ and $\theta+\Delta\theta$ has area

$$
\frac12(r+\Delta r)^2\Delta\theta-\frac12r^2\Delta\theta=r\,\Delta r\,\Delta\theta+\frac12(\Delta r)^2\Delta\theta\approx r\,\Delta r\,\Delta\theta,
$$

so the area element is $\mathrm{d}\sigma=r\,\mathrm{d}r\,\mathrm{d}\theta$. The factor $r$ here is exactly the Jacobian determinant of the polar coordinate transformation (Example 10.7.4 in [2.2.10](/2.2.10)); the general principle is in [12.4](#sec-12.4).

**Theorem 12.2.3** Let $f$ be continuous on $D$, and let $D$ be described in polar coordinates as $\{(r,\theta)\mid\alpha\le\theta\le\beta,\ r_1(\theta)\le r\le r_2(\theta)\}$. Then

$$
\iint_Df(x,y)\,\mathrm{d}\sigma=\int_\alpha^\beta\mathrm{d}\theta\int_{r_1(\theta)}^{r_2(\theta)}f(r\cos\theta,r\sin\theta)\,r\,\mathrm{d}r.
$$

Do not forget the factor $r$ in the area element. When the pole lies in the interior of $D$, $\theta$ runs from $0$ to $2\pi$ and $r$ starts at $0$.

**Example 12.2.5** Limits for common regions: the disk $x^2+y^2\le R^2$ is $0\le\theta\le2\pi$, $0\le r\le R$; the annulus $a^2\le x^2+y^2\le b^2$ is $0\le\theta\le2\pi$, $a\le r\le b$; the disk $x^2+y^2\le Rx$, with boundary $r=R\cos\theta$, is $-\frac\pi2\le\theta\le\frac\pi2$, $0\le r\le R\cos\theta$; for the triangle $0\le x\le1$, $0\le y\le1-x$, the hypotenuse $x+y=1$ becomes $r=\frac1{\cos\theta+\sin\theta}$, giving $0\le\theta\le\frac\pi2$, $0\le r\le\frac1{\cos\theta+\sin\theta}$.

**Example 12.2.6** Evaluate:

1. $\iint_Dx\sqrt{x^2+y^2}\,\mathrm{d}\sigma$, where $D$ is the part of the annulus $4\le x^2+y^2\le16$ in the first quadrant: $\int_0^{\pi/2}\cos\theta\,\mathrm{d}\theta\int_2^4r^3\,\mathrm{d}r=1\cdot\frac{4^4-2^4}4=60$.
2. $\iint_D\sqrt{R^2-x^2-y^2}\,\mathrm{d}\sigma$, $D=\{x^2+y^2\le Rx\}$ (half the volume of the part of the ball cut out by the cylinder):
$$
\int_{-\pi/2}^{\pi/2}\mathrm{d}\theta\int_0^{R\cos\theta}\sqrt{R^2-r^2}\,r\,\mathrm{d}r=\int_{-\pi/2}^{\pi/2}\frac{R^3}3\big(1-|\sin\theta|^3\big)\,\mathrm{d}\theta=\frac{R^3}{3}\Big(\pi-\frac43\Big).
$$
Note that $\sqrt{1-\cos^2\theta}=|\sin\theta|$; the absolute value must not be dropped.
3. The area of the region enclosed by the curve $(x^2+y^2)^2=3x^3$: its polar equation is $r=3\cos^3\theta$ ($-\frac\pi2\le\theta\le\frac\pi2$), and the area is $\int_{-\pi/2}^{\pi/2}\frac92\cos^6\theta\,\mathrm{d}\theta=9\int_0^{\pi/2}\cos^6\theta\,\mathrm{d}\theta=9\cdot\frac{5\cdot3\cdot1}{6\cdot4\cdot2}\cdot\frac\pi2=\frac{45\pi}{32}$, using the **Wallis integrals**.

### 12.2.5. Improper Double Integrals and the Gaussian Integral

On an unbounded region, or for an unbounded integrand, the double integral is defined as the limit of integrals over a sequence of bounded regions that "gradually exhaust" the region, in analogy with the one-variable **improper integral**. For a nonnegative integrand, the limit does not depend on the choice of the sequence of regions.

**Example 12.2.7** Discuss the convergence of $\iint_{\mathbb{R}^2}\dfrac{\mathrm{d}\sigma}{(1+x^2+y^2)^p}$. On the disk $D_a=\{x^2+y^2\le a^2\}$,

$$
\iint_{D_a}\frac{\mathrm{d}\sigma}{(1+x^2+y^2)^p}=2\pi\int_0^a\frac{r\,\mathrm{d}r}{(1+r^2)^p}=\begin{cases}\pi\ln(1+a^2),&p=1,\\[2pt] \dfrac{\pi}{1-p}\big[(1+a^2)^{1-p}-1\big],&p\ne1.\end{cases}
$$

As $a\to+\infty$, the integral converges to $\dfrac{\pi}{p-1}$ for $p>1$ and diverges for $p\le1$. Compare with the one-variable integral $\int_1^{+\infty}\frac{\mathrm{d}x}{x^{q}}$, which converges for $q>1$: in two dimensions the area element carries an extra factor $r$, and the critical exponent grows with the dimension.

**Proposition 12.2.1 (Gaussian Integral)** $\displaystyle\int_{-\infty}^{+\infty}\mathrm{e}^{-x^2}\,\mathrm{d}x=\sqrt\pi$, that is, $\displaystyle\int_0^{+\infty}\mathrm{e}^{-x^2}\,\mathrm{d}x=\frac{\sqrt\pi}2$.

**Proof** The antiderivative of $\mathrm{e}^{-x^2}$ is not elementary, and one-variable methods are powerless; the trick is to write the square of the integral as a double integral and then use polar coordinates. Let $I(a)=\int_0^a\mathrm{e}^{-x^2}\,\mathrm{d}x$. By Theorem 12.2.1,

$$
I(a)^2=\int_0^a\mathrm{e}^{-x^2}\,\mathrm{d}x\int_0^a\mathrm{e}^{-y^2}\,\mathrm{d}y=\iint_{[0,a]^2}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d}\sigma.
$$

The square $[0,a]^2$ lies between the two quarter disks $D_1$ (radius $a$) and $D_2$ (radius $\sqrt2a$) in the first quadrant, and the integrand is positive, so

$$
\frac\pi4\big(1-\mathrm{e}^{-a^2}\big)=\iint_{D_1}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d}\sigma\le I(a)^2\le\iint_{D_2}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d}\sigma=\frac\pi4\big(1-\mathrm{e}^{-2a^2}\big),
$$

where $\iint_{D_1}=\int_0^{\pi/2}\mathrm{d}\theta\int_0^a\mathrm{e}^{-r^2}r\,\mathrm{d}r$. Letting $a\to+\infty$, the squeeze theorem gives $I(+\infty)^2=\frac\pi4$. $\square$

The substitution $x=\sqrt t$ gives $\Gamma\big(\frac12\big)=\int_0^{+\infty}t^{-1/2}\mathrm{e}^{-t}\,\mathrm{d}t=2\int_0^{+\infty}\mathrm{e}^{-x^2}\,\mathrm{d}x=\sqrt\pi$ (the **gamma function**); a further linear substitution gives $\frac1{\sqrt{2\pi}\sigma}\int_{-\infty}^{+\infty}\mathrm{e}^{-(x-\mu)^2/(2\sigma^2)}\,\mathrm{d}x=1$, that is, the density of the normal distribution $\mathcal{N}(\mu,\sigma^2)$ integrates to $1$.

## 12.3. Evaluation of Triple Integrals

### 12.3.1. Preliminaries: Quadric Surfaces and Projections

The regions of triple integrals are often bounded by *quadric surfaces*; to determine the limits, one must know their shapes and the projections of their intersection curves onto the coordinate planes.

| Name | Standard equation | Features |
|---|---|---|
| Ellipsoid | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}+\dfrac{z^2}{c^2}=1$ | Horizontal cross sections are ellipses of area $\pi ab\big(1-\frac{z^2}{c^2}\big)$ |
| Elliptic paraboloid | $z=\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}$ | A paraboloid of revolution when $a=b$ |
| Hyperbolic paraboloid (saddle surface) | $z=\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}$ | The origin is a stationary point but not an extreme point |
| Hyperboloid of one sheet | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}-\dfrac{z^2}{c^2}=1$ | Horizontal cross sections are ellipses, smallest at $z=0$ |
| Hyperboloid of two sheets | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}-\dfrac{z^2}{c^2}=-1$ | Has points only where $\lvert z\rvert\ge c$ |
| Elliptic cone | $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=\dfrac{z^2}{c^2}$ | Made up of lines through the vertex |

![The six quadric surfaces: ellipsoid, elliptic paraboloid, hyperbolic paraboloid, hyperboloid of one sheet, hyperboloid of two sheets and cone](./plots/quadric-surfaces.py)

Projection of a space curve $F(x,y,z)=0$, $G(x,y,z)=0$ onto the $xy$-plane: eliminating $z$ from the two equations gives the projecting cylinder $f(x,y)=0$, and the projected curve is $f(x,y)=0$, $z=0$. For example, for the intersection of $z=x^2+y^2$ and $x+y+z=1$, eliminating $z$ gives $\big(x+\frac12\big)^2+\big(y+\frac12\big)^2=\frac32$, so the projection is a circle in the $xy$-plane. The projection of a region $\Omega$ onto the $xy$-plane is the region enclosed by the boundary obtained in this way.

### 12.3.2. Cartesian Coordinates: Projection and Cross Sections

**Theorem 12.3.1 (Projection Method: One Then Two)** Let $\Omega=\{(x,y,z)\mid(x,y)\in D_{xy},\ z_1(x,y)\le z\le z_2(x,y)\}$, where $D_{xy}$ is the projection of $\Omega$ onto the $xy$-plane, and let $f$ be continuous on $\Omega$. Then

$$
\iiint_\Omega f\,\mathrm{d}V=\iint_{D_{xy}}\mathrm{d}\sigma\int_{z_1(x,y)}^{z_2(x,y)}f(x,y,z)\,\mathrm{d}z.
$$

Geometrically, this partitions $\Omega$ into "vertical columns" parallel to the $z$-axis: above each point of the projected region, the column enters through the lower surface $z=z_1$ and leaves through the upper surface $z=z_2$. The outer double integral is then reduced to an iterated integral, giving three successive definite integrals in the end.

**Theorem 12.3.2 (Cross-Section Method: Two Then One)** Let $\Omega$ lie between the planes $z=c_1$ and $z=c_2$, and let $D_z$ be the cross section of $\Omega$ by the horizontal plane at height $z$. Then

$$
\iiint_\Omega f\,\mathrm{d}V=\int_{c_1}^{c_2}\mathrm{d}z\iint_{D_z}f(x,y,z)\,\mathrm{d}\sigma.
$$

This partitions the region into horizontal "slices". When the integrand depends only on $z$ and the area of the cross section $D_z$ is easy to find, the cross-section method is particularly simple. In Cartesian coordinates $\mathrm{d}V=\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$.

**Example 12.3.1** Evaluate $\iiint_\Omega\dfrac{\mathrm{d}V}{(1+x+y+z)^3}$, where $\Omega$ is bounded by the three coordinate planes and the plane $x+y+z=1$. The projection $D_{xy}$ is $0\le x\le1$, $0\le y\le1-x$, and $z$ runs from $0$ to $1-x-y$:

$$
\int_0^1\mathrm{d}x\int_0^{1-x}\mathrm{d}y\int_0^{1-x-y}\frac{\mathrm{d}z}{(1+x+y+z)^3}
=\int_0^1\mathrm{d}x\int_0^{1-x}\Big[\frac{1}{2(1+x+y)^2}-\frac18\Big]\mathrm{d}y
=\frac12\int_0^1\Big(\frac{1}{1+x}-\frac{3-x}{4}\Big)\mathrm{d}x=\frac{\ln2}2-\frac5{16}.
$$

**Example 12.3.2** Evaluate $\iiint_\Omega xyz\,\mathrm{d}V$, $\Omega=\{x^2+y^2+z^2\le1,\ x,y,z\ge0\}$.

$$
\int_0^1\mathrm{d}z\int_0^{\sqrt{1-z^2}}\mathrm{d}x\int_0^{\sqrt{1-z^2-x^2}}xyz\,\mathrm{d}y=\int_0^1\mathrm{d}z\int_0^{\sqrt{1-z^2}}\frac{xz(1-z^2-x^2)}2\,\mathrm{d}x=\int_0^1\frac{z(1-z^2)^2}8\,\mathrm{d}z=\frac1{48}.
$$

**Example 12.3.3** Let $\Omega$ be the solid ellipsoid $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\le1$. By the cross-section method, $D_z$ is an ellipse with semi-axes $a\sqrt{1-z^2/c^2}$ and $b\sqrt{1-z^2/c^2}$ and area $\pi ab\big(1-\frac{z^2}{c^2}\big)$, so

$$
V=\int_{-c}^c\pi ab\Big(1-\frac{z^2}{c^2}\Big)\mathrm{d}z=\frac43\pi abc,\qquad
\iiint_\Omega z^2\,\mathrm{d}V=\int_{-c}^cz^2\pi ab\Big(1-\frac{z^2}{c^2}\Big)\mathrm{d}z=\frac4{15}\pi abc^3.
$$

From this (by interchanging the roles of the variables) we get $\iiint_\Omega\big(\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\big)\mathrm{d}V=\frac45\pi abc$.

### 12.3.3. Cylindrical Coordinates

**Definition 12.3.1 (Cylindrical Coordinates)** The **cylindrical coordinates** of a point $(x,y,z)$ in space are $(r,\theta,z)$, where $x=r\cos\theta$, $y=r\sin\theta$, $z=z$ ($r\ge0$, $0\le\theta<2\pi$).

Cylindrical coordinates are polar coordinates in the $xy$-plane with $z$ unchanged. The surfaces $r=$ const are circular cylinders, $\theta=$ const half-planes, and $z=$ const planes. The volume element is $\mathrm{d}V=r\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}z$. When the projection of $\Omega$ onto a coordinate plane is simple in polar coordinates (the region is bounded by surfaces of revolution and circular cylinders, and the integrand involves $x^2+y^2$), first use the projection method to write the integral as "$\iint_{D_{xy}}\mathrm{d}\sigma\int\mathrm{d}z$", and then use polar coordinates for the outer double integral.

**Example 12.3.4** Evaluate:

1. $\iiint_\Omega z\,\mathrm{d}V$, where $\Omega$ is bounded by the cone $z=\sqrt{x^2+y^2}$ and the plane $z=2$. By the cross-section method, $D_z$ is a disk of radius $z$: $\int_0^2z\cdot\pi z^2\,\mathrm{d}z=4\pi$.
2. $\iiint_\Omega(x^2+y^2)\,\mathrm{d}V$, where $\Omega$ is bounded by $x^2+y^2=2z$ and $z=2$. Projection method: the projection is $r\le2$, and $z$ runs from $\frac{r^2}2$ to $2$,
$$
\int_0^{2\pi}\mathrm{d}\theta\int_0^2r^2\Big(2-\frac{r^2}2\Big)r\,\mathrm{d}r=2\pi\Big(8-\frac{16}{3}\Big)=\frac{16\pi}3;
$$
cross-section method: $\int_0^2\mathrm{d}z\int_0^{2\pi}\mathrm{d}\theta\int_0^{\sqrt{2z}}r^3\,\mathrm{d}r=\int_0^22\pi z^2\,\mathrm{d}z=\frac{16\pi}3$, the same result.

### 12.3.4. Spherical Coordinates

**Definition 12.3.2 (Spherical Coordinates)** The **spherical coordinates** of a point $(x,y,z)$ in space are $(\rho,\varphi,\theta)$, where

$$
x=\rho\sin\varphi\cos\theta,\qquad y=\rho\sin\varphi\sin\theta,\qquad z=\rho\cos\varphi,
$$

$\rho\ge0$ is the distance to the origin, $\varphi\in[0,\pi]$ is the angle with the positive $z$-axis, and $\theta\in[0,2\pi)$ is as in cylindrical coordinates.

The surfaces $\rho=$ const are spheres, $\varphi=$ const half-cones with vertex at the origin, and $\theta=$ const half-planes. The volume element is $\mathrm{d}V=\rho^2\sin\varphi\,\mathrm{d}\rho\,\mathrm{d}\varphi\,\mathrm{d}\theta$ (derived from the Jacobian determinant in Example 12.4.4; it can also be seen from the three edge lengths $\mathrm{d}\rho$, $\rho\,\mathrm{d}\varphi$, $\rho\sin\varphi\,\mathrm{d}\theta$ of a small "spherical box"). Spherical coordinates are used when the region is bounded by spheres and cones and the integrand involves $x^2+y^2+z^2$.

**Example 12.3.5** Express and evaluate in spherical coordinates:

1. The ball $x^2+y^2+z^2\le R^2$: $\iiint_\Omega f\,\mathrm{d}V=\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\mathrm{d}\varphi\int_0^Rf\,\rho^2\sin\varphi\,\mathrm{d}\rho$, with spherical coordinates substituted into $f$. For $f=1$ this gives the volume $\frac43\pi R^3$ of the ball.
2. $\iiint_\Omega\sqrt{x^2+y^2+z^2}\,\mathrm{d}V$, $\Omega=\{x^2+y^2+z^2\le z\}$ (the ball with center $(0,0,\frac12)$ and radius $\frac12$): the equation of the sphere becomes $\rho=\cos\varphi$, and
$$
\int_0^{2\pi}\mathrm{d}\theta\int_0^{\pi/2}\mathrm{d}\varphi\int_0^{\cos\varphi}\rho\cdot\rho^2\sin\varphi\,\mathrm{d}\rho=2\pi\int_0^{\pi/2}\frac{\cos^4\varphi}4\sin\varphi\,\mathrm{d}\varphi=\frac\pi{10}.
$$
3. Convert the iterated integral $\int_0^1\mathrm{d}x\int_0^{\sqrt{1-x^2}}\mathrm{d}y\int_{\sqrt{x^2+y^2}}^{\sqrt{2-x^2-y^2}}z^2\,\mathrm{d}z$ to spherical coordinates and evaluate it. The region lies above the cone $z=\sqrt{x^2+y^2}$ ($\varphi=\frac\pi4$), inside the sphere $\rho=\sqrt2$, in the first octant:
$$
\int_0^{\pi/2}\mathrm{d}\theta\int_0^{\pi/4}\mathrm{d}\varphi\int_0^{\sqrt2}\rho^2\cos^2\varphi\cdot\rho^2\sin\varphi\,\mathrm{d}\rho=\frac\pi2\cdot\frac{1}{3}\Big(1-\frac{\sqrt2}{4}\Big)\cdot\frac{4\sqrt2}5=\frac{\pi}{15}(2\sqrt2-1).
$$

## 12.4. Change of Variables in Multiple Integrals

### 12.4.1. Change of Variables in Double Integrals

Cartesian and polar coordinates are special ways of partitioning a region. In general, let the transformation $x=x(u,v)$, $y=y(u,v)$ map a region $D'$ in the $uv$-plane one-to-one onto a region $D$ in the $xy$-plane. Partition $D$ by the net of coordinate curves $u=$ const, $v=$ const. A small rectangle in the $uv$-plane with corner $(u,v)$ and sides $\Delta u,\Delta v$ is mapped to a small curvilinear quadrilateral, which to first order is the parallelogram with sides

$$
\boldsymbol{a}=(x_u,y_u)\Delta u,\qquad\boldsymbol{b}=(x_v,y_v)\Delta v
$$

(this is the meaning of differentiability in [2.2.10](/2.2.10): locally the map is approximately the linear map $J$). The area of the parallelogram is the absolute value of the determinant with columns $\boldsymbol{a},\boldsymbol{b}$, so

$$
\Delta\sigma\approx\Big|\det\frac{\partial(x,y)}{\partial(u,v)}\Big|\Delta u\,\Delta v,\qquad\text{that is,}\quad\mathrm{d}x\,\mathrm{d}y=\Big|\det\frac{\partial(x,y)}{\partial(u,v)}\Big|\mathrm{d}u\,\mathrm{d}v.
$$

This is the local application of the linear algebra fact that "the determinant is the volume scaling factor of a linear transformation": near each point a differentiable map is approximately the linear map $J_f$, which multiplies areas by $|\det J_f|$.

**Theorem 12.4.1 (Change of Variables Formula for Double Integrals)** Let $f$ be continuous on a bounded closed region $D$, and let the transformation $x=x(u,v)$, $y=y(u,v)$ have continuous partial derivatives, map $D'$ one-to-one onto $D$, and satisfy $\det\dfrac{\partial(x,y)}{\partial(u,v)}\ne0$ (this may fail on a set of zero area). Then

$$
\iint_Df(x,y)\,\mathrm{d}x\,\mathrm{d}y=\iint_{D'}f\big(x(u,v),y(u,v)\big)\Big|\det\frac{\partial(x,y)}{\partial(u,v)}\Big|\,\mathrm{d}u\,\mathrm{d}v.
$$

Compare with substitution in a definite integral: there $\mathrm{d}x=x'(t)\,\mathrm{d}t$ carries a sign, because the definite integral has an orientation; in a multiple integral areas are positive, and we take the absolute value of the Jacobian determinant. The main purpose of a change of variables in a multiple integral is often to simplify the region of integration rather than the integrand. By the inverse function theorem, $\det\dfrac{\partial(x,y)}{\partial(u,v)}=1\Big/\det\dfrac{\partial(u,v)}{\partial(x,y)}$; when the new variables $u,v$ are given directly in terms of $x,y$, the latter is more convenient to compute.

![Images of coordinate grids under transformations: polar coordinates map squares in the (r, θ)-plane to annular sectors, with area scaling factor r; the transformation x = u^(−2/5) v^(1/5), y = u^(−1/5) v^(3/5) maps squares to curvilinear quadrilaterals (Example 12.4.3)](./plots/change-of-variables-grid.py)

**Example 12.4.1 (Polar Coordinates)** The Jacobian determinant of $x=r\cos\theta$, $y=r\sin\theta$ is $r$, and Theorem 12.4.1 immediately gives Theorem 12.2.3. The transformation is not one-to-one at $r=0$, where the Jacobian determinant vanishes, but this is a set of zero area and does not affect the formula.

**Definition 12.4.1 (Generalized Polar Coordinates)** The transformation $x=x_0+ar\cos\theta$, $y=y_0+br\sin\theta$ ($a,b>0$) is called the **generalized polar coordinates** transformation; its Jacobian determinant is $abr$.

It transforms the ellipse $\frac{(x-x_0)^2}{a^2}+\frac{(y-y_0)^2}{b^2}\le1$ into $r\le1$ and is used for elliptical regions. The area of the ellipse is $\int_0^{2\pi}\mathrm{d}\theta\int_0^1abr\,\mathrm{d}r=\pi ab$.

**Example 12.4.2** Evaluate $\iint_D\sqrt{1-\frac{x^2}{a^2}-\frac{y^2}{b^2}}\,\mathrm{d}\sigma$, where $D$ is the ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}\le1$. In generalized polar coordinates,

$$
\int_0^{2\pi}\mathrm{d}\theta\int_0^1\sqrt{1-r^2}\,abr\,\mathrm{d}r=2\pi ab\cdot\frac13=\frac{2\pi ab}3.
$$

**Example 12.4.3** Evaluate $\iint_Dxy\,\mathrm{d}x\,\mathrm{d}y$, where $D$ is the region in the first quadrant bounded by $y=ax^3$, $y=bx^3$, $y^2=px$ and $y^2=qx$ ($0<a<b$, $0<p<q$). Let $u=\dfrac y{x^3}$, $v=\dfrac{y^2}x$; then $D$ becomes the rectangle $[a,b]\times[p,q]$, and

$$
\det\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}-3yx^{-4}&x^{-3}\\ -y^2x^{-2}&2yx^{-1}\end{vmatrix}=-\frac{5y^2}{x^5},\qquad\Big|\det\frac{\partial(x,y)}{\partial(u,v)}\Big|=\frac{x^5}{5y^2}.
$$

Solving for $x,y$ gives $x=u^{-2/5}v^{1/5}$ and $y=u^{-1/5}v^{3/5}$, so $xy\cdot\dfrac{x^5}{5y^2}=\dfrac{x^6}{5y}=\dfrac15u^{-11/5}v^{3/5}$ and

$$
\iint_Dxy\,\mathrm{d}x\,\mathrm{d}y=\frac15\int_a^bu^{-11/5}\,\mathrm{d}u\int_p^qv^{3/5}\,\mathrm{d}v=\frac5{48}\big(a^{-6/5}-b^{-6/5}\big)\big(q^{8/5}-p^{8/5}\big).
$$

### 12.4.2. Change of Variables in Triple Integrals

The three-dimensional case is entirely analogous: the transformation $x=x(u,v,w)$, $y=y(u,v,w)$, $z=z(u,v,w)$ maps a small box approximately onto the parallelepiped with edges $\boldsymbol{r}_u\Delta u$, $\boldsymbol{r}_v\Delta v$, $\boldsymbol{r}_w\Delta w$, whose volume is the absolute value of the scalar triple product, namely $\Big|\det\dfrac{\partial(x,y,z)}{\partial(u,v,w)}\Big|\Delta u\,\Delta v\,\Delta w$.

**Theorem 12.4.2 (Change of Variables Formula for Triple Integrals)** Under the same conditions as in Theorem 12.4.1,

$$
\iiint_\Omega f(x,y,z)\,\mathrm{d}V=\iiint_{\Omega'}f\big(x(u,v,w),y(u,v,w),z(u,v,w)\big)\Big|\det\frac{\partial(x,y,z)}{\partial(u,v,w)}\Big|\,\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w.
$$

**Example 12.4.4 (Volume Elements in Cylindrical and Spherical Coordinates)** The Jacobian determinant of cylindrical coordinates is

$$
\det\frac{\partial(x,y,z)}{\partial(r,\theta,z)}=\begin{vmatrix}\cos\theta&-r\sin\theta&0\\ \sin\theta&r\cos\theta&0\\ 0&0&1\end{vmatrix}=r.
$$

Expanding the Jacobian determinant of spherical coordinates along the third row:

$$
\det\frac{\partial(x,y,z)}{\partial(\rho,\varphi,\theta)}=\begin{vmatrix}\sin\varphi\cos\theta&\rho\cos\varphi\cos\theta&-\rho\sin\varphi\sin\theta\\ \sin\varphi\sin\theta&\rho\cos\varphi\sin\theta&\rho\sin\varphi\cos\theta\\ \cos\varphi&-\rho\sin\varphi&0\end{vmatrix}
=\rho^2\cos^2\varphi\sin\varphi+\rho^2\sin^3\varphi=\rho^2\sin\varphi.
$$

**Example 12.4.5 (Generalized Spherical Coordinates)** Find the volume of the solid ellipsoid $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\le1$. Let $x=a\rho\sin\varphi\cos\theta$, $y=b\rho\sin\varphi\sin\theta$, $z=c\rho\cos\varphi$; the Jacobian determinant is $abc\rho^2\sin\varphi$ and the region becomes $\rho\le1$:

$$
V=\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\mathrm{d}\varphi\int_0^1abc\rho^2\sin\varphi\,\mathrm{d}\rho=2\pi\cdot2\cdot\frac{abc}3=\frac43\pi abc,
$$

in agreement with Example 12.3.3.

**Example 12.4.6** Evaluate $\iiint_\Omega(x+y+z)\cos(x+y+z)^2\,\mathrm{d}V$, where $\Omega$ is given by $0\le x-y\le1$, $0\le x-z\le1$, $0\le x+y+z\le1$. Let $u=x-y$, $v=x-z$, $w=x+y+z$; then $\Omega$ becomes the unit cube, and

$$
\det\frac{\partial(u,v,w)}{\partial(x,y,z)}=\begin{vmatrix}1&-1&0\\ 1&0&-1\\ 1&1&1\end{vmatrix}=3,\qquad\mathrm{d}V=\frac13\,\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w,
$$

so the integral equals $\dfrac13\int_0^1\mathrm{d}u\int_0^1\mathrm{d}v\int_0^1w\cos w^2\,\mathrm{d}w=\dfrac{\sin1}6$. This is a linear transformation, and its Jacobian determinant is a constant, namely the volume scaling factor of the linear transformation.

### 12.4.3. Further Examples

**Example 12.4.7** Prove that the tangent plane to the surface $z=x^2+y^2+a$ ($a>0$) at any point encloses, together with the surface $z=x^2+y^2$, a solid of volume $\frac{\pi a^2}2$.

**Proof** The tangent plane at $(x_0,y_0,z_0)$ is $z=z_0+2x_0(x-x_0)+2y_0(y-y_0)=2x_0x+2y_0y-z_0+2a$ (using $z_0=x_0^2+y_0^2+a$). The projection onto the $xy$-plane of its intersection with $z=x^2+y^2$ is $(x-x_0)^2+(y-y_0)^2=a$. The enclosed volume is

$$
V=\iint_{(x-x_0)^2+(y-y_0)^2\le a}\big[2x_0x+2y_0y-z_0+2a-(x^2+y^2)\big]\mathrm{d}\sigma=\iint_{u^2+v^2\le a}\big(a-u^2-v^2\big)\,\mathrm{d}u\,\mathrm{d}v,
$$

where the translation $u=x-x_0$, $v=y-y_0$ has Jacobian determinant $1$ and the simplified integrand does not depend on the point of tangency. In polar coordinates, $V=2\pi\int_0^{\sqrt a}(a-r^2)r\,\mathrm{d}r=\frac{\pi a^2}2$. $\square$

**Example 12.4.8** Let $f\in C[0,1]$. Prove that $\displaystyle\int_0^1\mathrm{d}x\int_x^1\mathrm{d}y\int_x^yf(x)f(y)f(z)\,\mathrm{d}z=\frac16\Big(\int_0^1f(t)\,\mathrm{d}t\Big)^3$.

**Proof** Let $F(u)=\int_0^uf(t)\,\mathrm{d}t$. Integrating successively: the innermost integral is $f(x)f(y)\big(F(y)-F(x)\big)$; integrating in $y$, $\int_x^1f(y)\big(F(y)-F(x)\big)\,\mathrm{d}y=\frac12\big(F(1)-F(x)\big)^2$; finally $\frac12\int_0^1f(x)\big(F(1)-F(x)\big)^2\,\mathrm{d}x=\frac16F(1)^3$. $\square$

Another way to see this: the region of integration is $0\le x\le z\le y\le1$, the integrand is symmetric in $x,y,z$, and the cube $[0,1]^3$ splits according to the ordering of the three coordinates into $6$ congruent parts, over each of which the integral is the same.

## 12.5. Applications of Multiple Integrals

The formulas for area and volume have already been used repeatedly: $\sigma(D)=\iint_D\mathrm{d}\sigma$ and $V(\Omega)=\iiint_\Omega\mathrm{d}V$. The area of a surface requires the area element on the surface and is deferred to [2.2.13](/2.2.13).

Let a body $\Omega$ have density $\rho(x,y,z)$ and mass $M=\iiint_\Omega\rho\,\mathrm{d}V$. The center of mass of a system of particles is the mass-weighted average position; replacing the sum by an integral:

**Definition 12.5.1 (Center of Mass)** The **center of mass** $(\bar x,\bar y,\bar z)$ of a body $\Omega$ with density $\rho$ is

$$
\bar x=\frac1M\iiint_\Omega x\rho\,\mathrm{d}V,\qquad\bar y=\frac1M\iiint_\Omega y\rho\,\mathrm{d}V,\qquad\bar z=\frac1M\iiint_\Omega z\rho\,\mathrm{d}V.
$$

The center of mass of a plane lamina is defined similarly by double integrals. When the density is constant, the center of mass is called the centroid and depends only on the shape; by symmetry, the centroid lies on any axis (plane) of symmetry.

**Definition 12.5.2 (Moment of Inertia)** The **moment of inertia** of a body $\Omega$ about an axis is $I=\iiint_\Omega d^2\rho\,\mathrm{d}V$, where $d$ is the distance from the point to the axis. For example, about the $z$-axis $I_z=\iiint_\Omega(x^2+y^2)\rho\,\mathrm{d}V$; for a plane lamina about the $x$-axis $I_x=\iint_Dy^2\mu\,\mathrm{d}\sigma$.

**Example 12.5.1** The centroid of the uniform half-disk $D=\{x^2+y^2\le a^2,\ y\ge0\}$: by symmetry $\bar x=0$, and

$$
\bar y=\frac{1}{\pi a^2/2}\int_0^\pi\mathrm{d}\theta\int_0^ar\sin\theta\cdot r\,\mathrm{d}r=\frac{2}{\pi a^2}\cdot2\cdot\frac{a^3}3=\frac{4a}{3\pi}.
$$

**Example 12.5.2** The moment of inertia of a uniform ball of mass $M$ and radius $R$ about a diameter. Take the diameter as the $z$-axis; the density is $\rho_0=\frac{3M}{4\pi R^3}$, and in spherical coordinates

$$
I_z=\rho_0\int_0^{2\pi}\mathrm{d}\theta\int_0^\pi\mathrm{d}\varphi\int_0^R\rho^2\sin^2\varphi\cdot\rho^2\sin\varphi\,\mathrm{d}\rho=\rho_0\cdot2\pi\cdot\frac43\cdot\frac{R^5}5=\frac25MR^2.
$$

Finally, gravitational attraction. The force exerted by a body of density $\rho$ on a particle of unit mass at $P_0(x_0,y_0,z_0)$ is $\boldsymbol{F}=G\iiint_\Omega\dfrac{\rho\,(x-x_0,y-y_0,z-z_0)}{r^3}\,\mathrm{d}V$, where $r$ is the distance from $(x,y,z)$ to $P_0$ and $G$ is the gravitational constant. Each component is a triple integral. One can compute, for example, that a uniform ball attracts a particle outside it as if its entire mass were concentrated at its center; in [2.2.14](/2.2.14) this conclusion is obtained more simply from the divergence theorem.

## 12.6. Integrals Depending on a Parameter

### 12.6.1. Definite Integrals Depending on a Parameter

Many functions are defined by integrals, for example the **gamma function** $\Gamma(s)=\int_0^{+\infty}x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x$. When the integrand contains a parameter, the value of the integral is a function of the parameter, and we are interested in its continuity, integrability and differentiability, that is, in whether we may take limits, integrate and differentiate under the integral sign.

**Definition 12.6.1 (Integral Depending on a Parameter)** Suppose that for each $x$ in an interval $I$, $g(x,y)$ is integrable in $y$ on $[c,d]$. Then

$$
f(x)=\int_c^dg(x,y)\,\mathrm{d}y,\qquad x\in I
$$

is called an **integral depending on a parameter** ($x$ is the parameter). The limits of integration may also depend on $x$: $\int_{\alpha(x)}^{\beta(x)}g(x,y)\,\mathrm{d}y$.

**Theorem 12.6.1 (Continuity)** If $g$ is continuous on the rectangle $[a,b]\times[c,d]$, then $f(x)=\int_c^dg(x,y)\,\mathrm{d}y$ is continuous on $[a,b]$.

**Proof** Since $g$ is continuous on a bounded closed region, it has the property of **uniform continuity**: for every $\varepsilon>0$ there is $\delta>0$ such that $|g(x_1,y)-g(x_2,y)|<\frac{\varepsilon}{d-c}$ for all $y\in[c,d]$ whenever $|x_1-x_2|<\delta$. Hence $|f(x_1)-f(x_2)|\le\int_c^d|g(x_1,y)-g(x_2,y)|\,\mathrm{d}y<\varepsilon$. $\square$

Therefore $\lim\limits_{x\to x_0}\int_c^dg(x,y)\,\mathrm{d}y=\int_c^d\lim\limits_{x\to x_0}g(x,y)\,\mathrm{d}y$: for continuous integrands, limit and integral can be interchanged.

**Theorem 12.6.2 (Interchanging the Order of Integration)** If $g$ is continuous on $[a,b]\times[c,d]$, then

$$
\int_a^b\mathrm{d}x\int_c^dg(x,y)\,\mathrm{d}y=\int_c^d\mathrm{d}y\int_a^bg(x,y)\,\mathrm{d}x.
$$

This is Theorem 12.2.1: both sides equal the double integral of $g$ over the rectangle.

**Theorem 12.6.3 (Differentiation under the Integral Sign)** If $g$ and $g_x$ are both continuous on $[a,b]\times[c,d]$, then $f(x)=\int_c^dg(x,y)\,\mathrm{d}y$ is differentiable on $[a,b]$, and

$$
f'(x)=\int_c^d\frac{\partial g}{\partial x}(x,y)\,\mathrm{d}y.
$$

**Proof** By the mean value theorem,

$$
\frac{f(x+\Delta x)-f(x)}{\Delta x}=\int_c^d\frac{g(x+\Delta x,y)-g(x,y)}{\Delta x}\,\mathrm{d}y=\int_c^dg_x(x+\theta\Delta x,y)\,\mathrm{d}y,
$$

with $\theta=\theta(x,\Delta x,y)\in(0,1)$. Since $g_x$ is uniformly continuous on the rectangle, for every $\varepsilon>0$ and sufficiently small $|\Delta x|$ we have $|g_x(x+\theta\Delta x,y)-g_x(x,y)|<\frac{\varepsilon}{d-c}$ for all $y$, so the expression above differs from $\int_c^dg_x(x,y)\,\mathrm{d}y$ by less than $\varepsilon$. $\square$

**Theorem 12.6.4 (Variable Limits)** If $g$ and $g_x$ are continuous on $[a,b]\times[c,d]$ and $\alpha(x),\beta(x)$ are differentiable on $[a,b]$ with values in $[c,d]$, then $f(x)=\int_{\alpha(x)}^{\beta(x)}g(x,y)\,\mathrm{d}y$ is differentiable, and

$$
f'(x)=\int_{\alpha(x)}^{\beta(x)}\frac{\partial g}{\partial x}(x,y)\,\mathrm{d}y+g\big(x,\beta(x)\big)\beta'(x)-g\big(x,\alpha(x)\big)\alpha'(x).
$$

**Proof** Let $\Phi(x,u,v)=\int_u^vg(x,y)\,\mathrm{d}y$; then $f(x)=\Phi(x,\alpha(x),\beta(x))$. By Theorem 12.6.3 and the derivative of an **integral with a variable upper limit**, $\Phi_x=\int_u^vg_x\,\mathrm{d}y$, $\Phi_v=g(x,v)$ and $\Phi_u=-g(x,u)$, all continuous, so $\Phi$ is differentiable, and the chain rule gives the result. $\square$

The two "boundary terms" come from the variation of the limits of integration, and the first term from the variation of the integrand. When $g$ does not depend on $x$, this is the formula for the derivative of an integral with a variable upper limit.

**Example 12.6.1** Evaluate $\displaystyle\int_0^\pi\ln\Big(1+\frac12\cos x\Big)\mathrm{d}x$. Introduce a parameter: let $I(y)=\int_0^\pi\ln(1+y\cos x)\,\mathrm{d}x$ ($|y|<1$), so that $I(0)=0$. By Theorem 12.6.3,

$$
I'(y)=\int_0^\pi\frac{\cos x}{1+y\cos x}\,\mathrm{d}x=\frac1y\int_0^\pi\Big(1-\frac1{1+y\cos x}\Big)\mathrm{d}x=\frac\pi y-\frac{\pi}{y\sqrt{1-y^2}}\qquad(y\ne0),
$$

where $\int_0^\pi\frac{\mathrm{d}x}{1+y\cos x}=\frac{\pi}{\sqrt{1-y^2}}$ is obtained by the **Weierstrass substitution** $t=\tan\frac x2$. Integrating with $y=\sin\varphi$ gives $I(y)=\pi\ln\big(1+\sqrt{1-y^2}\big)+C$, and $I(0)=0$ gives $C=-\pi\ln2$. Therefore

$$
\int_0^\pi\ln\Big(1+\frac12\cos x\Big)\mathrm{d}x=I\Big(\frac12\Big)=\pi\ln\frac{2+\sqrt3}{4}.
$$

**Example 12.6.2** Evaluate $\displaystyle\int_0^1\frac{x^b-x^a}{\ln x}\,\mathrm{d}x$ ($0<a<b$). Note that $\dfrac{x^b-x^a}{\ln x}=\int_a^bx^y\,\mathrm{d}y$ and the integrand $x^y$ is continuous on $[0,1]\times[a,b]$; by Theorem 12.6.2 we may interchange the order of integration:

$$
\int_0^1\mathrm{d}x\int_a^bx^y\,\mathrm{d}y=\int_a^b\mathrm{d}y\int_0^1x^y\,\mathrm{d}x=\int_a^b\frac{\mathrm{d}y}{y+1}=\ln\frac{1+b}{1+a}.
$$

### 12.6.2. Improper Integrals Depending on a Parameter

When the interval of integration is infinite (or the integrand is unbounded), interchanging limits and integrals requires a condition stronger than convergence for each value of the parameter, just as series of functions require **uniform convergence**.

**Definition 12.6.2 (Uniform Convergence)** Suppose that for each $x\in I$, $\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ converges to $f(x)$. If for every $\varepsilon>0$ there is $N$, independent of $x$, such that for $T>N$

$$
\Big|\int_c^Tg(x,y)\,\mathrm{d}y-f(x)\Big|=\Big|\int_T^{+\infty}g(x,y)\,\mathrm{d}y\Big|<\varepsilon
$$
for all $x\in I$, then the improper integral $\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ depending on the parameter is said to **converge uniformly** in $x\in I$.

The following results are stated without proof; the proofs parallel those of the corresponding theorems for series of functions ([2.2.9](/2.2.9)).

**Theorem 12.6.5 (Cauchy Criterion and M-Test)** $\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ converges uniformly in $x\in I$ if and only if for every $\varepsilon>0$ there is $N$ such that $\Big|\int_S^Tg(x,y)\,\mathrm{d}y\Big|<\varepsilon$ for all $x\in I$ whenever $T>S>N$. In particular, if there is $M(y)$ with $|g(x,y)|\le M(y)$ for all $x\in I$ and $\int_c^{+\infty}M(y)\,\mathrm{d}y$ converges, then the integral converges uniformly in $x\in I$.

**Theorem 12.6.6** Let $g$ be continuous on $I\times[c,+\infty)$ and let $f(x)=\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ converge uniformly in $x\in I$. Then:

1. $f$ is continuous on $I$;
2. if $I=[a,b]$, then $\int_a^bf(x)\,\mathrm{d}x=\int_c^{+\infty}\mathrm{d}y\int_a^bg(x,y)\,\mathrm{d}x$;
3. if $g_x$ is also continuous on $I\times[c,+\infty)$, $\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ converges for each $x\in I$, and $\int_c^{+\infty}g_x(x,y)\,\mathrm{d}y$ converges uniformly in $x\in I$, then $f'(x)=\int_c^{+\infty}g_x(x,y)\,\mathrm{d}y$.

**Proposition 12.6.1 (Dirichlet Integral)** For a constant $a$,

$$
\int_0^{+\infty}\frac{\sin ax}{x}\,\mathrm{d}x=\frac\pi2\operatorname{sgn}a,\qquad\text{in particular}\quad\int_0^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x=\frac\pi2.
$$

**Proof** The integral converges only conditionally, and we cannot differentiate directly with respect to the parameter $a$ ($\int_0^{+\infty}\cos ax\,\mathrm{d}x$ diverges). Introduce the convergence factor $\mathrm{e}^{-kx}$ ($k>0$) and let

$$
I(a)=\int_0^{+\infty}\mathrm{e}^{-kx}\frac{\sin ax}{x}\,\mathrm{d}x.
$$

The integral $\int_0^{+\infty}\mathrm{e}^{-kx}\cos ax\,\mathrm{d}x$ obtained by differentiating with respect to $a$ is dominated by $\mathrm{e}^{-kx}$, so by the M-test it converges uniformly in $a\in\mathbb{R}$; integrating by parts twice shows that it equals $\dfrac{k}{a^2+k^2}$. By part 3 of Theorem 12.6.6, $I'(a)=\dfrac{k}{a^2+k^2}$, and since $I(0)=0$, $I(a)=\arctan\dfrac ak$.

Now regard $\int_0^{+\infty}\mathrm{e}^{-kx}\frac{\sin ax}{x}\,\mathrm{d}x$ as an integral with parameter $k$ (with $a\ne0$ fixed). Estimating $\int_S^T$ by integration by parts, one shows that it converges uniformly in $k\in[0,+\infty)$; by part 1 of Theorem 12.6.6 it is right-continuous at $k=0$, so

$$
\int_0^{+\infty}\frac{\sin ax}{x}\,\mathrm{d}x=\lim_{k\to0^+}\arctan\frac ak=\frac\pi2\operatorname{sgn}a.\qquad\square
$$

The antiderivative of $\frac{\sin x}{x}$ is not elementary; the method used here (introduce a parameter, differentiate with respect to it, then integrate back) is a typical technique for computing such definite integrals.

## Summary

| Integral | Coordinates | Area / volume element | When to use |
|---|---|---|---|
| Double integral | Cartesian | $\mathrm{d}x\,\mathrm{d}y$ | Boundary given by $y=y_i(x)$ or $x=x_i(y)$ |
| | Polar | $r\,\mathrm{d}r\,\mathrm{d}\theta$ | Disks, sectors, annuli; integrand involves $x^2+y^2$ |
| | Generalized polar | $abr\,\mathrm{d}r\,\mathrm{d}\theta$ | Elliptical regions |
| | General substitution | $\Big\lvert\det\dfrac{\partial(x,y)}{\partial(u,v)}\Big\rvert\mathrm{d}u\,\mathrm{d}v$ | Boundary made up of two families of curves $u=$ const, $v=$ const |
| Triple integral | Cartesian | $\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ | Projection method (one then two), cross-section method (two then one) |
| | Cylindrical | $r\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}z$ | Solids of revolution, cylinders; integrand involves $x^2+y^2$ |
| | Spherical | $\rho^2\sin\varphi\,\mathrm{d}\rho\,\mathrm{d}\varphi\,\mathrm{d}\theta$ | Balls, cones; integrand involves $x^2+y^2+z^2$ |
| | General substitution | $\Big\lvert\det\dfrac{\partial(x,y,z)}{\partial(u,v,w)}\Big\rvert\mathrm{d}u\,\mathrm{d}v\,\mathrm{d}w$ | Region bounded by three families of surfaces |

| Integral depending on a parameter | Condition | Conclusion |
|---|---|---|
| Proper integral $\int_c^dg(x,y)\,\mathrm{d}y$ | $g$ continuous | Continuous; order of integration can be interchanged |
| | $g,g_x$ continuous | Differentiation under the integral sign; with variable limits add the boundary terms $g(x,\beta)\beta'-g(x,\alpha)\alpha'$ |
| Improper integral $\int_c^{+\infty}g(x,y)\,\mathrm{d}y$ | Uniform convergence (M-test) | Continuous; order can be interchanged; may differentiate if the integral of the derivative converges uniformly |
