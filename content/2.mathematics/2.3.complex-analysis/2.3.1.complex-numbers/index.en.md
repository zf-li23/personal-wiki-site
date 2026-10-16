---
title: Complex Numbers and the Complex Plane
description: The algebra and geometry of complex numbers, arguments and roots, the extended plane and the Riemann sphere, plane point sets and curves, and limits and continuity of complex functions.
---

Complex analysis studies functions $w=f(z)$ of a complex variable that are differentiable in the complex sense. Such functions turn out to be far more rigid, and far more useful, than differentiable functions of a real variable: a single derivative forces infinitely many, values on a curve determine values inside it, and real integrals that resist every trick of calculus are evaluated by summing a few residues. Before any of this we need the stage on which it happens. This chapter reviews the arithmetic and geometry of complex numbers, already met in linear algebra ([2.1.9](/2.1.9)), with an eye on what complex analysis needs: the multivalued argument and its principal value, roots, the point at infinity and the Riemann sphere, the topology of plane sets (regions, curves, simple connectivity) and limits and continuity of complex functions. The plane topology is that of $\mathbb{R}^2$ from multivariable calculus ([2.2.10](/2.2.10)); the point of the chapter is to see which facts carry over verbatim and which new phenomena (the point $\infty$, the discontinuity of the principal argument) need attention. The derivative is introduced in [2.3.2](/2.3.2).

## 1.1. Complex Numbers

### 1.1.1. Algebraic Form

A **complex number** is $z=x+\mathrm{i}y$ with $x,y\in\mathbb{R}$ and $\mathrm{i}^2=-1$; $x=\operatorname{Re}z$ and $y=\operatorname{Im}z$ are its real and imaginary parts, and two complex numbers are equal exactly when their real parts and their imaginary parts are equal. Addition and multiplication follow the rules of polynomial arithmetic with $\mathrm{i}^2=-1$, and $\mathbb{C}$ is a field. The **complex conjugate** of $z$ is $\bar z=x-\mathrm{i}y$ and the **modulus** is $|z|=\sqrt{x^2+y^2}$. Identifying $z=x+\mathrm{i}y$ with the point $(x,y)$ turns $\mathbb{C}$ into the complex plane, with the real axis and the imaginary axis as coordinate axes; $|z_1-z_2|$ is then the Euclidean distance between the points $z_1$ and $z_2$.

**Proposition 1.1.1** For all $z,z_1,z_2\in\mathbb{C}$:

1. $\overline{z_1\pm z_2}=\bar z_1\pm\bar z_2$, $\overline{z_1z_2}=\bar z_1\bar z_2$, $\overline{z_1/z_2}=\bar z_1/\bar z_2$ ($z_2\ne0$), and $\bar{\bar z}=z$;
2. $z\bar z=|z|^2$, $\operatorname{Re}z=\dfrac{z+\bar z}{2}$, $\operatorname{Im}z=\dfrac{z-\bar z}{2\mathrm{i}}$;
3. $|z_1z_2|=|z_1|\,|z_2|$, $|\bar z|=|z|$, and $\max\{|\operatorname{Re}z|,|\operatorname{Im}z|\}\le|z|\le|\operatorname{Re}z|+|\operatorname{Im}z|$;
4. (triangle inequality) $\big||z_1|-|z_2|\big|\le|z_1+z_2|\le|z_1|+|z_2|$.

**Proof** Items 1 and 2 are direct computations. For 3, $|z_1z_2|^2=z_1z_2\overline{z_1z_2}=z_1\bar z_1\,z_2\bar z_2=|z_1|^2|z_2|^2$; the inequalities follow from $x^2\le x^2+y^2\le(|x|+|y|)^2$. For 4,

$$
|z_1+z_2|^2=(z_1+z_2)(\bar z_1+\bar z_2)=|z_1|^2+|z_2|^2+2\operatorname{Re}(z_1\bar z_2)\le|z_1|^2+|z_2|^2+2|z_1|\,|z_2|=(|z_1|+|z_2|)^2,
$$

using $\operatorname{Re}(z_1\bar z_2)\le|z_1\bar z_2|=|z_1|\,|z_2|$. Applying this to $z_1=(z_1+z_2)+(-z_2)$ gives $|z_1|-|z_2|\le|z_1+z_2|$, and exchanging the roles gives the left inequality. $\square$

Item 2 lets us pass between the real coordinates $(x,y)$ and the pair $(z,\bar z)$: $x=\frac{z+\bar z}{2}$ and $y=\frac{z-\bar z}{2\mathrm{i}}$. This change of variables is the basis of the Wirtinger derivatives in [2.3.2](/2.3.2).

### 1.1.2. Polar Form and the Argument

Every $z\ne0$ can be written in **polar form** $z=r(\cos\theta+\mathrm{i}\sin\theta)=r\mathrm{e}^{\mathrm{i}\theta}$, where $r=|z|$ and $\theta$ is an **argument** of $z$, the angle from the positive real axis to the vector $z$; the second expression uses **Euler's formula** $\mathrm{e}^{\mathrm{i}\theta}=\cos\theta+\mathrm{i}\sin\theta$ ([2.1.9](/2.1.9)). Since $\mathrm{e}^{\mathrm{i}\theta}$ has period $2\pi$, the argument is determined only up to an integer multiple of $2\pi$. In complex analysis this ambiguity cannot be swept aside: it is the source of all multivalued functions in [2.3.3](/2.3.3). We therefore name both the full set of arguments and a preferred representative.

**Definition 1.1.1 (Principal Argument)** For $z\ne0$, the set of all arguments of $z$ is denoted $\arg z$. The unique argument lying in $(-\pi,\pi]$ is called the **principal argument** of $z$ and is denoted $\operatorname{Arg}z$. Thus

$$
\arg z=\{\operatorname{Arg}z+2k\pi\mid k\in\mathbb{Z}\}.
$$

The argument of $0$ is not defined.

With $z=x+\mathrm{i}y\ne0$, the principal argument is computed from $\arctan\frac yx\in\left(-\frac\pi2,\frac\pi2\right)$ by correcting for the quadrant:

$$
\operatorname{Arg}z=\begin{cases}\arctan\dfrac yx, & x>0,\\[2mm] \arctan\dfrac yx+\pi, & x<0,\ y\ge0,\\[2mm] \arctan\dfrac yx-\pi, & x<0,\ y<0,\\[2mm] \pm\dfrac\pi2, & x=0,\ y\gtrless0.\end{cases}
$$

For example $\operatorname{Arg}(-1)=\pi$, $\operatorname{Arg}(-\mathrm{i})=-\frac\pi2$ and $\operatorname{Arg}(-1-\sqrt3\,\mathrm{i})=\frac\pi3-\pi=-\frac{2\pi}3$.

Multiplication multiplies moduli and adds arguments: if $z_k=r_k\mathrm{e}^{\mathrm{i}\theta_k}$, then

$$
z_1z_2=r_1r_2\mathrm{e}^{\mathrm{i}(\theta_1+\theta_2)},\qquad \frac{z_1}{z_2}=\frac{r_1}{r_2}\mathrm{e}^{\mathrm{i}(\theta_1-\theta_2)}.
$$

Geometrically, multiplication by $z_2$ rotates the plane by $\theta_2$ and scales it by $r_2$. As identities between sets, $\arg(z_1z_2)=\arg z_1+\arg z_2$ and $\arg(z_1/z_2)=\arg z_1-\arg z_2$ hold exactly (the sum of two sets means all sums of an element of each). For principal values they can fail: $\operatorname{Arg}(-1)+\operatorname{Arg}(-1)=2\pi\ne0=\operatorname{Arg}\big((-1)(-1)\big)$. Equations involving $\operatorname{Arg}$ are therefore valid only up to multiples of $2\pi$, a point that returns with the logarithm.

Iterating the product formula gives *de Moivre's formula*

$$
(\cos\theta+\mathrm{i}\sin\theta)^n=\cos n\theta+\mathrm{i}\sin n\theta\qquad(n\in\mathbb{Z}).
$$

**Example 1.1.1** Compute $\left(\dfrac{1+\sqrt3\,\mathrm{i}}{1-\mathrm{i}}\right)^{12}$. Since $1+\sqrt3\,\mathrm{i}=2\mathrm{e}^{\mathrm{i}\pi/3}$ and $1-\mathrm{i}=\sqrt2\,\mathrm{e}^{-\mathrm{i}\pi/4}$, the quotient is $\sqrt2\,\mathrm{e}^{\mathrm{i}7\pi/12}$, and its twelfth power is $2^6\mathrm{e}^{\mathrm{i}7\pi}=-64$.

**Example 1.1.2** Expanding $(\cos\theta+\mathrm{i}\sin\theta)^3$ by the binomial theorem and comparing real and imaginary parts with de Moivre's formula gives $\cos3\theta=\cos^3\theta-3\cos\theta\sin^2\theta=4\cos^3\theta-3\cos\theta$ and $\sin3\theta=3\sin\theta-4\sin^3\theta$. Summing the geometric series $\sum_{k=0}^{n}\mathrm{e}^{\mathrm{i}k\theta}$ and taking real parts gives in the same way, for $\theta\notin2\pi\mathbb{Z}$,

$$
\sum_{k=0}^{n}\cos k\theta=\frac12+\frac{\sin\big((n+\frac12)\theta\big)}{2\sin\frac\theta2},
$$

the Dirichlet kernel of Fourier series ([2.2.9](/2.2.9)).

### 1.1.3. Roots

**Theorem 1.1.1 ($n$-th Roots)** Let $w=\rho\mathrm{e}^{\mathrm{i}\varphi}\ne0$ and $n\ge1$. The equation $z^n=w$ has exactly $n$ distinct solutions

$$
z_k=\sqrt[n]{\rho}\,\exp\Big(\mathrm{i}\,\frac{\varphi+2k\pi}{n}\Big),\qquad k=0,1,\dots,n-1.
$$

They lie on the circle $|z|=\sqrt[n]\rho$ and are the vertices of a regular $n$-gon.

**Proof** Writing $z=r\mathrm{e}^{\mathrm{i}\theta}$, the equation $z^n=w$ means $r^n=\rho$ and $n\theta\in\varphi+2\pi\mathbb{Z}$, i.e. $r=\sqrt[n]\rho$ and $\theta=\frac{\varphi+2k\pi}{n}$, $k\in\mathbb{Z}$. Two values of $k$ give the same $z$ exactly when they differ by a multiple of $n$, so $k=0,\dots,n-1$ list each solution once. $\square$

The symbol $\sqrt[n]{w}$ for complex $w$ thus denotes $n$ values; for $w=1$ these are the $n$-th **roots of unity** $\mathrm{e}^{2k\pi\mathrm{i}/n}$, and every root of $w$ is one fixed root times a root of unity. Choosing one of the values continuously as $w$ varies is the subject of branches in [2.3.3](/2.3.3).

**Example 1.1.3** Solve $z^4+16=0$. Here $-16=16\mathrm{e}^{\mathrm{i}\pi}$, so $z_k=2\mathrm{e}^{\mathrm{i}(\pi/4+k\pi/2)}$, that is $z=\pm\sqrt2\pm\sqrt2\,\mathrm{i}$ (all four sign combinations), the vertices of a square (first panel of the figure in [§1.3](#sec-1.3)). Grouping conjugate roots gives the real factorization $z^4+16=(z^2-2\sqrt2z+4)(z^2+2\sqrt2z+4)$.

### 1.1.4. Curves and Regions Described by Complex Equations

Because $|z-a|$ is a distance and $\operatorname{Arg}$ an angle, many plane figures have short complex descriptions:

| Equation or inequality | Figure |
|---|---|
| $\lvert z-z_0\rvert=r$, $\lvert z-z_0\rvert<r$ | circle, open disc with center $z_0$ and radius $r$ |
| $\lvert z-a\rvert=\lvert z-b\rvert$ | perpendicular bisector of the segment $ab$ |
| $\lvert z-a\rvert+\lvert z-b\rvert=2c$ ($2c>\lvert a-b\rvert$) | ellipse with foci $a,b$ |
| $\lvert z-a\rvert=k\lvert z-b\rvert$ ($k>0$, $k\ne1$) | circle of Apollonius |
| $\operatorname{Re}z>0$, $\operatorname{Im}z>0$ | right half-plane, upper half-plane |
| $\alpha<\operatorname{Arg}z<\beta$ | open sector with vertex $0$ |
| $\operatorname{Re}(\bar az)=c$ ($a\ne0$, $c\in\mathbb{R}$) | straight line with normal direction $a$ |

**Example 1.1.4** Every circle and every line in the plane has an equation of the form

$$
A z\bar z+\bar Bz+B\bar z+C=0,\qquad A,C\in\mathbb{R},\ B\in\mathbb{C},\ |B|^2>AC.
$$

Indeed, $|z-z_0|^2=r^2$ expands to $z\bar z-\bar z_0z-z_0\bar z+|z_0|^2-r^2=0$, and the line $\operatorname{Re}(\bar az)=c$ is $\bar az+a\bar z-2c=0$, the case $A=0$. Conversely, if $A\ne0$, dividing by $A$ and completing the square gives $|z+B/A|^2=(|B|^2-AC)/A^2>0$. This "generalized circle" form shows at once that inversion $w=1/z$ maps generalized circles to generalized circles: substituting $z=1/w$ and multiplying by $w\bar w$ gives $Cw\bar w+Bw+\bar B\bar w+A=0$, of the same form with the roles of $A$ and $C$ exchanged. This is a key step in the theory of Möbius transformations ([2.3.8](/2.3.8)).

## 1.2. The Extended Complex Plane and the Riemann Sphere

Many statements of complex analysis become cleaner if we add one point at infinity: $1/z$ becomes defined at $z=0$, lines become circles through $\infty$, and the behavior of a function for large $|z|$ becomes its behavior near a single point. Unlike the real line, which is naturally completed by two points $\pm\infty$, the plane is completed by only one, because $|z|\to\infty$ along every direction should lead to the same place.

**Definition 1.2.1 (Extended Complex Plane)** Adjoin to $\mathbb{C}$ a single new element $\infty$, the **point at infinity**. The set $\hat{\mathbb{C}}=\mathbb{C}\cup\{\infty\}$ is called the **extended complex plane**. For $a\in\mathbb{C}$ we set

$$
a\pm\infty=\infty,\qquad a\cdot\infty=\infty\ (a\ne0),\qquad \frac a\infty=0,\qquad \frac a0=\infty\ (a\ne0),
$$

while $\infty\pm\infty$, $0\cdot\infty$, $\frac00$ and $\frac\infty\infty$ are left undefined. The real part, imaginary part and argument of $\infty$ are not defined, and $|\infty|=+\infty$. For $R>0$ the set $\{z\mid |z|>R\}\cup\{\infty\}$ is called a neighborhood of $\infty$.

The extended plane can be pictured as a sphere. Let $S=\{(x_1,x_2,x_3)\in\mathbb{R}^3\mid x_1^2+x_2^2+x_3^2=1\}$ be the unit sphere, place the complex plane as the plane $x_3=0$ (so that $z=x+\mathrm{i}y$ is the point $(x,y,0)$), and let $N=(0,0,1)$ be the north pole.

**Definition 1.2.2 (Riemann Sphere)** For $z\in\mathbb{C}$, the line through $N$ and $z$ meets $S$ in exactly one point $P\ne N$; send $z$ to $P$, and send $\infty$ to $N$. This bijection $\hat{\mathbb{C}}\to S$ (and also its inverse) is called **stereographic projection**, and $S$ regarded as a model of $\hat{\mathbb{C}}$ is called the **Riemann sphere**.

Solving for the intersection of the line $N+t\big((x,y,0)-N\big)$ with $S$ gives explicit formulas: with $z=x+\mathrm{i}y$,

$$
P=\Big(\frac{2x}{|z|^2+1},\ \frac{2y}{|z|^2+1},\ \frac{|z|^2-1}{|z|^2+1}\Big),\qquad z=\frac{x_1+\mathrm{i}x_2}{1-x_3}. \tag{1.1}
$$

The unit circle goes to the equator, the disc $|z|<1$ to the southern hemisphere (with $0$ at the south pole), and the exterior $|z|>1$ to the northern hemisphere; $|z|\to\infty$ exactly when $P\to N$, so the neighborhoods of $\infty$ in Definition 1.2.1 are the images of small caps around $N$.

![Stereographic projection. Left: the line from the north pole N through a point z of the plane meets the sphere once more; points outside the unit circle land on the northern hemisphere, points inside on the southern one. Right: circles in the plane and a straight line (which passes through infinity) all become circles on the sphere.](./plots/riemann-sphere.py)

**Theorem 1.2.1** Under stereographic projection, circles and straight lines in $\mathbb{C}$ correspond exactly to circles on $S$; lines correspond to the circles through $N$.

**Proof** A circle on $S$ is the intersection of $S$ with a plane $a_1x_1+a_2x_2+a_3x_3=a_0$ (with $a_1^2+a_2^2+a_3^2=1$, $|a_0|<1$). Substituting Eq. (1.1) and multiplying by $|z|^2+1$ gives

$$
(a_3-a_0)(x^2+y^2)+2a_1x+2a_2y-(a_3+a_0)=0.
$$

If $a_3\ne a_0$ this is a circle (its radius squared is $\frac{a_1^2+a_2^2+a_3^2-a_0^2}{(a_3-a_0)^2}>0$), and if $a_3=a_0$, i.e. the plane passes through $N$, it is a line. Reversing the computation shows that every circle and every line arises this way. $\square$

Since a line passes through $\infty$ on the sphere, it is natural to regard lines as circles through $\infty$; the term generalized circle (Example 1.1.4) refers to both. The sphere also gives a bounded metric on $\hat{\mathbb{C}}$: the chordal distance $\frac{2|z_1-z_2|}{\sqrt{(1+|z_1|^2)(1+|z_2|^2)}}$ between the images of $z_1$ and $z_2$, with distance $\frac{2}{\sqrt{1+|z|^2}}$ from $z$ to $\infty$. In this course we use the sphere mainly as a picture: a statement about $f$ "at $\infty$" is a statement about $g(\zeta)=f(1/\zeta)$ at $\zeta=0$, and the sphere shows why this is the right substitution.

## 1.3. Point Sets and Curves in the Plane

### 1.3.1. Open Sets and Regions

The plane $\mathbb{C}$ with the distance $|z_1-z_2|$ is the Euclidean plane $\mathbb{R}^2$, so the topological notions of [2.2.10](/2.2.10) apply unchanged; we only fix the notation of complex analysis. The open disc with center $z_0$ and radius $r$ is $D(z_0,r)=\{z\mid |z-z_0|<r\}$, and $\mathbb{D}=D(0,1)$ is the unit disc. $D(z_0,\delta)$ is the $\delta$-**neighborhood** of $z_0$, and $0<|z-z_0|<\delta$ is its **punctured neighborhood**. For a set $E\subset\mathbb{C}$:

- $z_0$ is an interior point of $E$ if some neighborhood of $z_0$ lies in $E$; $E$ is an **open set** if all its points are interior points;
- $z_0$ is a **boundary point** of $E$ if every neighborhood of $z_0$ contains points of $E$ and points not in $E$; the set of boundary points is the boundary $\partial E$, and $E$ is a **closed set** if it contains its boundary;
- $E$ is a **bounded set** if $E\subset D(0,M)$ for some $M$; bounded closed sets are called compact;
- a connected open set is a **region** (in complex analysis also called a domain), and a region together with its boundary is a **closed region**.

In complex analysis, functions are almost always studied on regions. Openness guarantees that the difference quotient $\frac{f(z_0+h)-f(z_0)}{h}$ is defined for all small $h$ in every direction; connectedness guarantees that local information propagates through the whole set. For example, a function with zero derivative on a region is constant ([2.3.2](/2.3.2)), which fails on the disconnected open set $D(0,1)\cup D(3,1)$.

### 1.3.2. Curves

**Definition 1.3.1 (Curves)** A curve is a continuous map $\gamma\colon[a,b]\to\mathbb{C}$, $\gamma(t)=x(t)+\mathrm{i}y(t)$; $\gamma(a)$ and $\gamma(b)$ are its initial and terminal points. The curve is

- closed if $\gamma(a)=\gamma(b)$;
- simple if $\gamma(t_1)\ne\gamma(t_2)$ for $a\le t_1<t_2\le b$, except possibly $\gamma(a)=\gamma(b)$; a simple closed curve is called a **Jordan curve**;
- a **smooth curve** if $\gamma'(t)=x'(t)+\mathrm{i}y'(t)$ exists, is continuous and is nonzero on $[a,b]$;
- a **piecewise smooth curve** if $[a,b]$ can be divided into finitely many subintervals on each of which $\gamma$ is smooth.

A piecewise smooth curve is also called a contour; it is the class of curves along which we integrate in [2.3.4](/2.3.4). The nonzero vector $\gamma'(t)$ is tangent to the curve at $\gamma(t)$, and $\operatorname{Arg}\gamma'(t)$ is the direction of the tangent; this is how the angle between two curves is measured in [2.3.2](/2.3.2). For example, $\gamma(t)=z_0+r\mathrm{e}^{\mathrm{i}t}$ ($0\le t\le2\pi$) is the circle $|z-z_0|=r$ traversed once counterclockwise, a smooth Jordan curve; $\gamma(t)=\mathrm{e}^{2\mathrm{i}t}$ on the same interval traverses the unit circle twice and is not simple; the boundary of a square is a piecewise smooth Jordan curve that is not smooth.

**Theorem 1.3.1 (Jordan Curve Theorem)** The complement of a Jordan curve $C$ in $\mathbb{C}$ consists of exactly two regions, a bounded one (the interior of $C$) and an unbounded one (the exterior of $C$), and $C$ is the boundary of each.

The statement looks obvious, but the proof for general continuous curves is hard and belongs to topology; for piecewise smooth curves, the only ones we integrate over, it can be proved by elementary means. We use the theorem without proof. A Jordan curve is positively oriented if its interior lies to the left as the curve is traversed, i.e. it runs counterclockwise.

### 1.3.3. Simply Connected Regions

A region $D$ is a **simply connected domain** if the interior of every Jordan curve in $D$ lies in $D$ ([2.2.13](/2.2.13)); intuitively, $D$ has no holes, and every closed curve in $D$ can be shrunk to a point within $D$. Otherwise $D$ is a **multiply connected domain**. On the Riemann sphere, a region $D\subset\mathbb{C}$ is simply connected exactly when $\hat{\mathbb{C}}\setminus D$ is connected.

![Typical point sets. The fourth roots of -16 form a square (Example 1.1.3). A disc is simply connected; the annulus 1 < |z| < 2 is not, since the circle |z| = 1.5 cannot be shrunk to a point inside it; the plane with the negative real axis and 0 removed is simply connected although unbounded.](./plots/roots-and-regions.py)

The figure shows three cases that recur throughout the course:

- discs, half-planes, sectors and the whole plane are simply connected;
- the annulus $r<|z-z_0|<R$ and the punctured disc $0<|z-z_0|<R$ are not: a circle around $z_0$ encloses the excluded center. These are the regions of Laurent series ([2.3.5](/2.3.5));
- the slit plane $\mathbb{C}\setminus(-\infty,0]$ is simply connected: removing a ray from $0$ to $\infty$ destroys every loop around $0$. It is the region on which the principal logarithm is defined ([2.3.3](/2.3.3)).

Cauchy's theorem in [2.3.4](/2.3.4) holds on simply connected regions and requires correction terms on multiply connected ones, exactly as Green's theorem does.

## 1.4. Complex Functions, Limits and Continuity

### 1.4.1. Complex Functions

**Definition 1.4.1 (Complex Function)** Let $E\subset\mathbb{C}$. A rule assigning to every $z\in E$ a complex number $w=f(z)$ is called a **complex function** (a function of a complex variable) on $E$. If some $z$ are assigned several values, $f$ is called multivalued; unless stated otherwise, functions are single-valued.

Writing $z=x+\mathrm{i}y$ and $w=u+\mathrm{i}v$, a complex function is the same as a pair of real functions of two real variables,

$$
f(z)=u(x,y)+\mathrm{i}v(x,y),
$$

for example $z^2=(x^2-y^2)+\mathrm{i}\,2xy$ and $\frac1z=\frac{x}{x^2+y^2}-\mathrm{i}\frac{y}{x^2+y^2}$. Since the graph of $f$ would live in $\mathbb{R}^4$, we picture $f$ as a mapping from a set in the $z$-plane to a set in the $w$-plane, and study how it transforms curves and regions:

- $w=z+b$ translates, $w=az$ ($a=|a|\mathrm{e}^{\mathrm{i}\alpha}\ne0$) rotates by $\alpha$ and scales by $|a|$, and $w=\bar z$ reflects in the real axis;
- $w=z^2$ doubles arguments and squares moduli: the sector $0<\operatorname{Arg}z<\frac\pi2$ goes onto the upper half-plane, and the hyperbola $x^2-y^2=1$ onto the line $\operatorname{Re}w=1$;
- $w=\frac1z$ sends $r\mathrm{e}^{\mathrm{i}\theta}$ to $\frac1r\mathrm{e}^{-\mathrm{i}\theta}$: inversion in the unit circle followed by reflection in the real axis; the circle $|z|=2$ goes to $|w|=\frac12$, and by Example 1.1.4 generalized circles go to generalized circles.

### 1.4.2. Limits

**Definition 1.4.2 (Limit)** Let $f$ be defined on a punctured neighborhood of $z_0\in\mathbb{C}$ (or on a set having $z_0$ as a **limit point**). We write $\lim_{z\to z_0}f(z)=A$ if for every $\varepsilon>0$ there is $\delta>0$ such that $|f(z)-A|<\varepsilon$ whenever $0<|z-z_0|<\delta$ and $z$ is in the domain of $f$. The cases $z_0=\infty$ or $A=\infty$ are defined by replacing the corresponding disc with a neighborhood of $\infty$: for instance $\lim_{z\to z_0}f(z)=\infty$ means that for every $M>0$ there is $\delta>0$ such that $|f(z)|>M$ whenever $0<|z-z_0|<\delta$, and $\lim_{z\to\infty}f(z)=A$ means that for every $\varepsilon>0$ there is $R>0$ such that $|f(z)-A|<\varepsilon$ whenever $|z|>R$.

This is the **limit of a function** of two real variables written in complex notation, so $z$ may approach $z_0$ along any path, and the limit exists only if all paths give the same value. The following theorem reduces complex limits to real ones.

**Theorem 1.4.1** Let $f=u+\mathrm{i}v$, $z_0=x_0+\mathrm{i}y_0$ and $A=a+\mathrm{i}b$. Then $\lim_{z\to z_0}f(z)=A$ if and only if

$$
\lim_{(x,y)\to(x_0,y_0)}u(x,y)=a\quad\text{and}\quad\lim_{(x,y)\to(x_0,y_0)}v(x,y)=b.
$$

**Proof** By Proposition 1.1.1(3), $|u-a|,|v-b|\le|f-A|\le|u-a|+|v-b|$, so $|f-A|$ is small exactly when both $|u-a|$ and $|v-b|$ are. $\square$

Consequently the rules for limits of sums, products and quotients, and the Cauchy criterion, hold for complex functions exactly as for real ones.

**Example 1.4.1** The function $f(z)=\dfrac{\operatorname{Re}z}{|z|}$ has no limit at $0$: along the ray $z=t\mathrm{e}^{\mathrm{i}\theta}$ ($t\to0^+$) it is constantly $\cos\theta$, which depends on the direction. Likewise $\dfrac{z}{\bar z}=\mathrm{e}^{2\mathrm{i}\theta}$ has no limit at $0$. On the other hand $\dfrac{(\operatorname{Re}z)^2}{|z|}$ tends to $0$, since it is bounded by $|z|$.

**Example 1.4.2** $\displaystyle\lim_{z\to\infty}\frac{3z^2+\mathrm{i}z}{z^2-2}=3$, obtained by dividing numerator and denominator by $z^2$; and $\displaystyle\lim_{z\to\mathrm{i}}\frac{z^2+1}{z-\mathrm{i}}=\lim_{z\to\mathrm{i}}(z+\mathrm{i})=2\mathrm{i}$. For a polynomial $p$ of degree $n\ge1$, $\lim_{z\to\infty}p(z)=\infty$, because $|p(z)|\ge|a_n||z|^n\big(1-\sum_{k<n}\frac{|a_k|}{|a_n||z|^{n-k}}\big)$ and the bracket tends to $1$.

### 1.4.3. Continuity

**Definition 1.4.3 (Continuity)** A function $f$ defined near $z_0$ is continuous at $z_0$ if $\lim_{z\to z_0}f(z)=f(z_0)$; it is continuous on a set $E$ if it is continuous at every point of $E$ (limits taken within $E$).

By Theorem 1.4.1, $f=u+\mathrm{i}v$ is a **continuous function** exactly when $u$ and $v$ are. Sums, products, quotients (where the denominator is nonzero) and compositions of continuous functions are continuous; polynomials and rational functions are continuous wherever they are defined, and so are $\bar z$, $\operatorname{Re}z$ and $|z|$. A continuous function on a bounded closed set $E$ is bounded, $|f|$ attains its maximum and minimum on $E$, and $f$ is **uniformly continuous** on $E$, by the corresponding theorems for real functions of two variables applied to $|f|$, $u$ and $v$ ([2.2.10](/2.2.10)).

**Example 1.4.3** The principal argument $\operatorname{Arg}z$ is continuous on $\mathbb{C}\setminus(-\infty,0]$ and discontinuous at every point of the negative real axis. Indeed, near a point $x_0<0$, points just above the axis have $\operatorname{Arg}z$ close to $\pi$ and points just below have it close to $-\pi$. Away from the negative axis the formula of §1.1.2 expresses $\operatorname{Arg}$ through continuous functions (or, near the positive axis, through $\arctan\frac yx$ alone). The jump is not a defect of the formula: no continuous choice of argument exists on any circle around $0$, since following a continuous argument once around the circle increases it by $2\pi$. This is the phenomenon of branch points in [2.3.3](/2.3.3).

## Summary

| Topic | Key facts |
|---|---|
| Arithmetic | $\lvert z_1z_2\rvert=\lvert z_1\rvert\lvert z_2\rvert$, triangle inequality, $z\bar z=\lvert z\rvert^2$, $x=\frac{z+\bar z}2$, $y=\frac{z-\bar z}{2\mathrm{i}}$ |
| Argument | $\arg z$ is a set, $\operatorname{Arg}z\in(-\pi,\pi]$; $\arg(z_1z_2)=\arg z_1+\arg z_2$ holds as sets only |
| Roots | $z^n=w\ne0$ has $n$ roots on $\lvert z\rvert=\sqrt[n]{\lvert w\rvert}$, spaced by $2\pi/n$ |
| Infinity | $\hat{\mathbb{C}}=\mathbb{C}\cup\{\infty\}$ is the Riemann sphere; lines are circles through $\infty$ |
| Sets | regions (connected open sets); Jordan curves have an interior and an exterior; simply connected means no holes |
| Limits | $f\to A$ iff $u\to\operatorname{Re}A$ and $v\to\operatorname{Im}A$; $\operatorname{Arg}$ jumps across $(-\infty,0)$ |
