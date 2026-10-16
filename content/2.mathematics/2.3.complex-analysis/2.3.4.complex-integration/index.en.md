---
title: Complex Integration and Cauchy's Theorem
description: Contour integrals and the ML inequality, Cauchy's integral theorem and the deformation principle, antiderivatives, Cauchy's integral formula and its consequences (infinite differentiability, Cauchy's estimate, Liouville's theorem, the fundamental theorem of algebra, Morera's theorem), and the maximum modulus principle.
---

This chapter is the heart of the course. Integrating an analytic function along a closed curve gives zero (Cauchy's integral theorem); dividing first by $\zeta-z$ gives $2\pi\mathrm{i}f(z)$ (Cauchy's integral formula). From these two facts follow, with little further effort, nearly all the properties that make analytic functions special: they are infinitely differentiable, bounded entire functions are constant, every polynomial has a root, and $|f|$ attains its maximum on the boundary. Later chapters build on the same foundation: power and Laurent series ([2.3.5](/2.3.5)) are obtained by expanding the Cauchy kernel $\frac1{\zeta-z}$ in a geometric series, and the residue theorem ([2.3.6](/2.3.6)) is Cauchy's theorem applied to a region with holes. A complex integral is a **line integral of a vector field** in disguise, and the main tool for the first theorems is **Green's theorem** from [2.2.13](/2.2.13); the curves, regions and orientations are those of [2.3.1](/2.3.1).

## 4.1. Complex Integrals

### 4.1.1. Definition and Computation

**Definition 4.1.1 (Complex Integral)** Let $C$ be a piecewise smooth oriented curve from $z_0$ to $z_n$, and let $f$ be a function defined on $C$. Choose points $z_0,z_1,\dots,z_n$ along $C$ in the direction of the orientation and points $\zeta_k$ on the arc from $z_{k-1}$ to $z_k$, and set $\Delta z_k=z_k-z_{k-1}$. If, as the maximal length of the arcs tends to $0$, the sums $\sum_{k=1}^{n}f(\zeta_k)\Delta z_k$ converge to a limit independent of the choices, the limit is called the **complex integral** (or contour integral) of $f$ along $C$ and is denoted $\int_Cf(z)\,\mathrm{d}z$. If $C$ is closed, we write $\oint_Cf(z)\,\mathrm{d}z$; unless stated otherwise, a closed curve is positively oriented (counterclockwise).

**Theorem 4.1.1** Let $f=u+\mathrm{i}v$ be continuous on a piecewise smooth curve $C$. Then $\int_Cf(z)\,\mathrm{d}z$ exists and

$$
\int_Cf(z)\,\mathrm{d}z=\int_Cu\,\mathrm{d}x-v\,\mathrm{d}y+\mathrm{i}\int_Cv\,\mathrm{d}x+u\,\mathrm{d}y. \tag{4.1}
$$

If $C$ is parametrized by $z(t)$, $a\le t\le b$, in the direction of its orientation, then

$$
\int_Cf(z)\,\mathrm{d}z=\int_a^bf\big(z(t)\big)\,z'(t)\,\mathrm{d}t. \tag{4.2}
$$

**Proof** With $\Delta z_k=\Delta x_k+\mathrm{i}\Delta y_k$ and $f(\zeta_k)=u_k+\mathrm{i}v_k$, the Riemann sum splits as

$$
\sum f(\zeta_k)\Delta z_k=\sum(u_k\Delta x_k-v_k\Delta y_k)+\mathrm{i}\sum(v_k\Delta x_k+u_k\Delta y_k),
$$

and the two real sums are the sums defining real line integrals of continuous functions along a piecewise smooth curve, which converge to the right-hand side of Eq. (4.1). Substituting $x=x(t)$, $y=y(t)$ in those line integrals and recombining gives Eq. (4.2), since $(u+\mathrm{i}v)(x'+\mathrm{i}y')=(ux'-vy')+\mathrm{i}(vx'+uy')$. $\square$

Formally, Eq. (4.1) is obtained by multiplying out $(u+\mathrm{i}v)(\mathrm{d}x+\mathrm{i}\,\mathrm{d}y)$. The integral inherits the properties of line integrals:

- linearity: $\int_C(\alpha f+\beta g)\,\mathrm{d}z=\alpha\int_Cf\,\mathrm{d}z+\beta\int_Cg\,\mathrm{d}z$ for $\alpha,\beta\in\mathbb{C}$;
- reversing the orientation changes the sign: $\int_{C^-}f\,\mathrm{d}z=-\int_Cf\,\mathrm{d}z$;
- additivity: if $C$ consists of $C_1$ followed by $C_2$, then $\int_C=\int_{C_1}+\int_{C_2}$;
- independence of the parametrization (as long as the orientation is kept);
- $\big|\int_Cf(z)\,\mathrm{d}z\big|\le\int_C|f(z)|\,|\mathrm{d}z|$, where $|\mathrm{d}z|=\mathrm{d}s=|z'(t)|\,\mathrm{d}t$ is the element of **arc length**, so the right-hand side is a **line integral of a scalar function**.

**Example 4.1.1** Let $C_r$ be the circle $|z-z_0|=r$, positively oriented, and $n\in\mathbb{Z}$. Then

$$
\oint_{C_r}(z-z_0)^n\,\mathrm{d}z=\begin{cases}2\pi\mathrm{i}, & n=-1,\\ 0, & n\ne-1.\end{cases} \tag{4.3}
$$

Indeed, with $z=z_0+r\mathrm{e}^{\mathrm{i}t}$, $0\le t\le2\pi$, and $\mathrm{d}z=\mathrm{i}r\mathrm{e}^{\mathrm{i}t}\,\mathrm{d}t$, the integral equals $\mathrm{i}r^{n+1}\int_0^{2\pi}\mathrm{e}^{\mathrm{i}(n+1)t}\,\mathrm{d}t$, which is $2\pi\mathrm{i}$ for $n=-1$ and $0$ otherwise. The result does not depend on $r$. Formula (4.3) is the single most used computation in the course: with Laurent series it underlies the residue theorem.

**Example 4.1.2** Integrate $f(z)=\bar z$ from $0$ to $1+\mathrm{i}$ along (a) the segment $z=t(1+\mathrm{i})$, $0\le t\le1$; (b) the polygonal path $0\to1\to1+\mathrm{i}$.

(a) $\int_0^1t(1-\mathrm{i})(1+\mathrm{i})\,\mathrm{d}t=\int_0^12t\,\mathrm{d}t=1$.

(b) On $[0,1]$, $z=t$ and the integral is $\int_0^1t\,\mathrm{d}t=\frac12$. On the vertical segment, $z=1+\mathrm{i}t$, $\mathrm{d}z=\mathrm{i}\,\mathrm{d}t$, and the integral is $\int_0^1(1-\mathrm{i}t)\mathrm{i}\,\mathrm{d}t=\mathrm{i}+\frac12$. The total is $1+\mathrm{i}$.

The two answers differ: the integral of $\bar z$ depends on the path. By contrast, for $f(z)=z$ both paths give $\frac{(1+\mathrm{i})^2}{2}=\mathrm{i}$, as we will see is forced by the analyticity of $z$ (§4.3).

### 4.1.2. The ML Inequality

**Theorem 4.1.2 (ML Inequality)** If $|f(z)|\le M$ on a piecewise smooth curve $C$ of length $L$, then

$$
\Big|\int_Cf(z)\,\mathrm{d}z\Big|\le ML.
$$

**Proof** $\big|\int_Cf\,\mathrm{d}z\big|\le\int_C|f|\,\mathrm{d}s\le M\int_C\mathrm{d}s=ML$. $\square$

The ML inequality is used to show that integrals over small or large arcs tend to $0$; its sharpness rarely matters.

**Example 4.1.3** Let $\Gamma_R$ be the upper half of the circle $|z|=R$ ($R>1$). For $z\in\Gamma_R$, $|z^2+1|\ge|z|^2-1=R^2-1$ by the triangle inequality, so

$$
\Big|\int_{\Gamma_R}\frac{\mathrm{d}z}{z^2+1}\Big|\le\frac{\pi R}{R^2-1}\to0\qquad(R\to\infty).
$$

This estimate is the first step in evaluating $\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^2+1}$ by residues ([2.3.7](/2.3.7)). In general, $\int_{\Gamma_R}f\,\mathrm{d}z\to0$ whenever $Rf(z)\to0$ uniformly on $\Gamma_R$, i.e. whenever $f$ decays faster than $1/|z|$.

## 4.2. Cauchy's Integral Theorem

### 4.2.1. The Theorem

Example 4.1.1 shows that $\oint z^n\,\mathrm{d}z=0$ around circles for $n\ge0$, while Example 4.1.2 shows a nonzero integral of $\bar z$ around the triangle $0\to1\to1+\mathrm{i}\to0$ (namely $(1+\mathrm{i})-1=\mathrm{i}$). The difference is analyticity, and Green's theorem makes this precise.

**Lemma 4.2.1 (Complex Form of Green's Theorem)** Let $D$ be a bounded region whose boundary $\partial D$ consists of finitely many piecewise smooth Jordan curves, positively oriented, and let $f$ have continuous first-order partial derivatives on $\bar D=D\cup\partial D$. Then

$$
\oint_{\partial D}f(z)\,\mathrm{d}z=2\mathrm{i}\iint_D\frac{\partial f}{\partial\bar z}\,\mathrm{d}x\,\mathrm{d}y. \tag{4.4}
$$

**Proof** Apply Green's theorem ([2.2.13](/2.2.13#thm-13.4.1)) to the complex-valued 1-form $f\,\mathrm{d}x+\mathrm{i}f\,\mathrm{d}y$ (that is, to its real and imaginary parts separately):

$$
\oint_{\partial D}f\,\mathrm{d}x+\mathrm{i}f\,\mathrm{d}y=\iint_D\Big(\mathrm{i}\frac{\partial f}{\partial x}-\frac{\partial f}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y=\mathrm{i}\iint_D\Big(\frac{\partial f}{\partial x}+\mathrm{i}\frac{\partial f}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y,
$$

and the last integrand is $2\frac{\partial f}{\partial\bar z}$ (Definition 2.4.1). $\square$

**Example 4.2.1** For $f=\bar z$, $\frac{\partial f}{\partial\bar z}=1$, so $\oint_C\bar z\,\mathrm{d}z=2\mathrm{i}\cdot\operatorname{area}$ of the interior of any piecewise smooth Jordan curve $C$. For the triangle above, the area is $\frac12$ and the integral is $\mathrm{i}$, as computed. For the ellipse $\frac{x^2}{4}+y^2=1$ (area $2\pi$), $\oint\bar z\,\mathrm{d}z=4\pi\mathrm{i}$; the parametrization $z=2\cos t+\mathrm{i}\sin t$ gives the same result.

**Theorem 4.2.1 (Cauchy's Integral Theorem)** Let $f$ be analytic on a simply connected region $D$. Then

$$
\oint_Cf(z)\,\mathrm{d}z=0
$$

for every closed piecewise smooth curve $C$ in $D$.

**Proof** (Under the additional assumption that $f'$ is continuous, and for $C$ a Jordan curve.) Since $D$ is simply connected, the interior $G$ of $C$ lies in $D$, so $f$ has continuous partial derivatives on $\bar G$, and $\frac{\partial f}{\partial\bar z}=0$ there by Theorem 2.4.1. Eq. (4.4) gives $\oint_Cf\,\mathrm{d}z=0$. In real terms: by Eq. (4.1) and Green's theorem, $\oint_C(u\,\mathrm{d}x-v\,\mathrm{d}y)=\iint_G(-v_x-u_y)\,\mathrm{d}x\,\mathrm{d}y$ and $\oint_C(v\,\mathrm{d}x+u\,\mathrm{d}y)=\iint_G(u_x-v_y)\,\mathrm{d}x\,\mathrm{d}y$, and both integrands vanish by the Cauchy–Riemann equations. A closed curve that crosses itself finitely many times splits into finitely many Jordan curves, to each of which the argument applies; the general case requires an approximation argument that we omit. $\square$

The additional assumption is harmless in hindsight: Theorem 4.4.2 below shows that $f'$ is automatically continuous. But that theorem is proved with Cauchy's theorem, so a logically complete development must avoid the assumption, and this is what Goursat did.

**Theorem 4.2.2 (Goursat's Theorem)** If $f$ is complex differentiable at every point of an open set containing a closed triangle $T$ (with its interior), then $\oint_{\partial T}f(z)\,\mathrm{d}z=0$. No continuity of $f'$ is assumed.

**Proof** (Sketch.) Let $I=\big|\oint_{\partial T}f\,\mathrm{d}z\big|$. Joining the midpoints of the sides divides $T$ into four similar triangles, and the boundary integrals over the four add up to the integral over $\partial T$ (interior edges cancel); so for one of them, $T_1$, $\big|\oint_{\partial T_1}f\big|\ge I/4$. Repeating gives nested triangles $T_n$ with perimeter $2^{-n}p$ and $\big|\oint_{\partial T_n}f\big|\ge4^{-n}I$, shrinking to a point $z_0$. Near $z_0$, $f(z)=f(z_0)+f'(z_0)(z-z_0)+\varepsilon(z)(z-z_0)$ with $\varepsilon(z)\to0$. The linear part has an antiderivative, so its integral over $\partial T_n$ vanishes (§4.3), and by the ML inequality the remainder contributes at most $\sup_{T_n}|\varepsilon|\cdot2^{-n}p\cdot2^{-n}p$. Hence $I\le p^2\sup_{T_n}|\varepsilon|\to0$. $\square$

From the triangle case one obtains the integral over every closed polygon, then the existence of antiderivatives on discs, and then Theorem 4.2.1 in full generality; we do not pursue this. The theorem also holds for a closed curve that is the boundary: if $D$ is bounded by a piecewise smooth Jordan curve $C$, $f$ is analytic on $D$ and continuous on $\bar D$, then $\oint_Cf\,\mathrm{d}z=0$.

### 4.2.2. Multiply Connected Regions and Deformation of Contours

**Theorem 4.2.3 (Cauchy's Theorem for Multiply Connected Regions)** Let $C_0$ be a piecewise smooth Jordan curve and $C_1,\dots,C_n$ piecewise smooth Jordan curves inside $C_0$, each lying outside the others, and let $D$ be the region inside $C_0$ and outside all $C_k$. If $f$ is analytic on an open set containing $\bar D$, then, with all curves oriented counterclockwise,

$$
\oint_{C_0}f(z)\,\mathrm{d}z=\sum_{k=1}^{n}\oint_{C_k}f(z)\,\mathrm{d}z. \tag{4.5}
$$

Equivalently, $\oint_{\partial D}f\,\mathrm{d}z=0$ for the positively oriented boundary $\partial D$ (outer curve counterclockwise, inner curves clockwise).

**Proof** If $f'$ is continuous, this is Eq. (4.4) applied to $D$, since $\partial f/\partial\bar z=0$. Without that assumption, join $C_0$ to $C_1$, $C_1$ to $C_2$, …, $C_n$ to $C_0$ by cuts, as in the figure. The cuts divide $D$ into two simply connected pieces, each bounded by a Jordan curve; Cauchy's theorem gives zero for each, and in the sum the cuts are traversed once in each direction and cancel, leaving $\oint_{\partial D}$. $\square$

![Left: a region D with two holes and its positively oriented boundary, the outer curve C0 counterclockwise and the inner curves C1, C2 clockwise. Right: cuts joining the boundary curves split D into an upper and a lower simply connected part; each cut belongs to the boundary of both parts and is traversed once in each direction, so the cut contributions cancel.](./plots/multiply-connected.py)

The case $n=1$ is used constantly.

**Corollary 4.2.1 (Deformation Principle)** Let $C_0$ and $C_1$ be positively oriented piecewise smooth Jordan curves, $C_1$ inside $C_0$, and let $f$ be analytic on an open set containing the closed region between them. Then $\oint_{C_0}f\,\mathrm{d}z=\oint_{C_1}f\,\mathrm{d}z$.

In words: a contour may be deformed continuously without changing the integral, as long as it does not pass over a singular point of $f$. Integrals around complicated curves thus reduce to integrals around small circles about the singular points.

**Example 4.2.2** Let $C$ be any positively oriented piecewise smooth Jordan curve and $a\notin C$. By Corollary 4.2.1 and Eq. (4.3),

$$
\oint_C\frac{\mathrm{d}z}{(z-a)^n}=\begin{cases}2\pi\mathrm{i}, & n=1\text{ and }a\text{ inside }C,\\ 0, & \text{otherwise}\end{cases}\qquad(n\in\mathbb{Z}).
$$

If $a$ is outside $C$, the integrand is analytic on a simply connected neighborhood of $C$ and its interior, and Theorem 4.2.1 gives $0$.

**Example 4.2.3** Compute $\displaystyle\oint_{|z|=2}\frac{2z-1}{z^2-z}\,\mathrm{d}z$ and $\displaystyle\oint_{|z|=2}\frac{\mathrm{d}z}{z^2-1}$. By partial fractions $\frac{2z-1}{z(z-1)}=\frac1z+\frac1{z-1}$, and both singular points lie inside $|z|=2$, so the first integral is $2\pi\mathrm{i}+2\pi\mathrm{i}=4\pi\mathrm{i}$. Similarly $\frac{1}{z^2-1}=\frac12\big(\frac1{z-1}-\frac1{z+1}\big)$ gives $\frac12(2\pi\mathrm{i}-2\pi\mathrm{i})=0$ for the second, although the integrand is not analytic inside the curve: Cauchy's theorem gives a sufficient condition for a zero integral, not a necessary one.

## 4.3. Antiderivatives

**Theorem 4.3.1** Let $f$ be continuous on a region $D$, and suppose that $\int_Cf\,\mathrm{d}z$ depends only on the endpoints of $C$ for piecewise smooth curves $C$ in $D$ (equivalently, $\oint_Cf\,\mathrm{d}z=0$ for every closed piecewise smooth curve in $D$). Fix $z_0\in D$ and let

$$
F(z)=\int_{z_0}^{z}f(\zeta)\,\mathrm{d}\zeta.
$$

Then $F$ is analytic on $D$ and $F'=f$.

**Proof** For $z\in D$ and small $h$, the segment $[z,z+h]$ lies in $D$, and by path independence $F(z+h)-F(z)=\int_{[z,z+h]}f(\zeta)\,\mathrm{d}\zeta$. Since $\int_{[z,z+h]}\mathrm{d}\zeta=h$,

$$
\Big|\frac{F(z+h)-F(z)}{h}-f(z)\Big|=\Big|\frac1h\int_{[z,z+h]}\big(f(\zeta)-f(z)\big)\,\mathrm{d}\zeta\Big|\le\max_{\zeta\in[z,z+h]}|f(\zeta)-f(z)|\to0
$$

by the ML inequality and the continuity of $f$. $\square$

A function $F$ with $F'=f$ on $D$ is called an **antiderivative** (primitive) of $f$ on $D$, as in [2.2.6](/2.2.6). Two antiderivatives on a region differ by a constant (Theorem 2.3.2). Combining Theorems 4.2.1 and 4.3.1:

**Corollary 4.3.1** An analytic function $f$ on a simply connected region $D$ has an antiderivative on $D$, and for any antiderivative $\Phi$ and any piecewise smooth curve $C$ in $D$ from $z_1$ to $z_2$,

$$
\int_Cf(z)\,\mathrm{d}z=\Phi(z_2)-\Phi(z_1).
$$

**Proof** Existence was shown above. For any antiderivative $\Phi$ and a parametrization $z(t)$, $a\le t\le b$, of $C$, $\frac{\mathrm{d}}{\mathrm{d}t}\Phi(z(t))=f(z(t))z'(t)$, so Eq. (4.2) and the fundamental theorem of calculus (applied to real and imaginary parts) give $\Phi(z_2)-\Phi(z_1)$. $\square$

The second statement holds on any region on which $f$ has an antiderivative, simply connected or not. Thus integration techniques from calculus (substitution, integration by parts) carry over verbatim.

**Example 4.3.1** $\displaystyle\int_0^{\mathrm{i}}z\cos z\,\mathrm{d}z=\big[z\sin z+\cos z\big]_0^{\mathrm{i}}=\mathrm{i}\sin\mathrm{i}+\cos\mathrm{i}-1=-\sinh1+\cosh1-1=\mathrm{e}^{-1}-1$, along any path, since $z\cos z$ is entire.

**Example 4.3.2** Let $\Gamma^+$ and $\Gamma^-$ be the upper and lower halves of the unit circle, both from $1$ to $-1$. On the region $\mathbb{C}\setminus\{-\mathrm{i}t\mid t\ge0\}$, which contains $\Gamma^+$, the branch $\ln|z|+\mathrm{i}\theta$ with $-\frac\pi2<\theta<\frac{3\pi}2$ is an antiderivative of $\frac1z$ (Theorem 3.2.1 of [2.3.3](/2.3.3)), so $\int_{\Gamma^+}\frac{\mathrm{d}z}{z}=\mathrm{i}\pi-0=\mathrm{i}\pi$. Using the branch with $-\frac{3\pi}2<\theta<\frac\pi2$ for $\Gamma^-$ gives $\int_{\Gamma^-}\frac{\mathrm{d}z}{z}=-\mathrm{i}\pi$. The difference $2\pi\mathrm{i}$ is the integral around the full circle. It also shows that $\frac1z$ has no antiderivative on $\mathbb{C}\setminus\{0\}$: otherwise every closed integral would vanish.

## 4.4. Cauchy's Integral Formula

### 4.4.1. The Formula

**Theorem 4.4.1 (Cauchy's Integral Formula)** Let $f$ be analytic on a region $D$, and let $C$ be a positively oriented piecewise smooth Jordan curve in $D$ whose interior lies in $D$. Then for every $z$ inside $C$,

$$
f(z)=\frac{1}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)}{\zeta-z}\,\mathrm{d}\zeta. \tag{4.6}
$$

**Proof** The integrand is analytic in $\zeta$ on $D\setminus\{z\}$, so by the deformation principle the integral equals the integral over any small circle $|\zeta-z|=\rho$ inside $C$:

$$
\oint_C\frac{f(\zeta)}{\zeta-z}\,\mathrm{d}\zeta=f(z)\oint_{|\zeta-z|=\rho}\frac{\mathrm{d}\zeta}{\zeta-z}+\oint_{|\zeta-z|=\rho}\frac{f(\zeta)-f(z)}{\zeta-z}\,\mathrm{d}\zeta.
$$

The first term is $2\pi\mathrm{i}f(z)$ by Eq. (4.3). By the ML inequality the second is at most $2\pi\rho\cdot\frac1\rho\max_{|\zeta-z|=\rho}|f(\zeta)-f(z)|$, which tends to $0$ as $\rho\to0$ by continuity of $f$. The left side does not depend on $\rho$, so the second term is $0$. $\square$

Cauchy's integral formula says that the values of an analytic function inside a curve are completely determined by its values on the curve, a statement with no analogue for real differentiable functions. It also turns integrals into evaluations.

**Example 4.4.1** $\displaystyle\oint_{|z|=2}\frac{\mathrm{e}^z}{z-1}\,\mathrm{d}z=2\pi\mathrm{i}\,\mathrm{e}$, by Eq. (4.6) with $f=\mathrm{e}^z$ and $z=1$.

**Example 4.4.2** Compute $\displaystyle\oint_{|z|=2}\frac{\sin z}{z^2+1}\,\mathrm{d}z$. Both $\pm\mathrm{i}$ lie inside. Either split $\frac1{z^2+1}=\frac1{2\mathrm{i}}\big(\frac1{z-\mathrm{i}}-\frac1{z+\mathrm{i}}\big)$, or deform the contour into two small circles around $\pm\mathrm{i}$ (Theorem 4.2.3). Applying Eq. (4.6) to each term,

$$
\oint_{|z|=2}\frac{\sin z}{z^2+1}\,\mathrm{d}z=\frac{2\pi\mathrm{i}}{2\mathrm{i}}\big(\sin\mathrm{i}-\sin(-\mathrm{i})\big)=2\pi\sin\mathrm{i}=2\pi\mathrm{i}\sinh1.
$$

Taking $C$ to be the circle $|\zeta-z_0|=r$ and $\zeta=z_0+r\mathrm{e}^{\mathrm{i}t}$ in Eq. (4.6) gives the following.

**Corollary 4.4.1 (Mean Value Property)** If $f$ is analytic on an open set containing the closed disc $|z-z_0|\le r$, then

$$
f(z_0)=\frac1{2\pi}\int_0^{2\pi}f\big(z_0+r\mathrm{e}^{\mathrm{i}t}\big)\,\mathrm{d}t.
$$

The value at the center is the average of the values on any circle around it. Taking real parts, harmonic functions have the same mean value property (§4.6).

### 4.4.2. Derivatives of All Orders

Formally differentiating Eq. (4.6) under the integral sign with respect to $z$ suggests formulas for all derivatives. They are true.

**Theorem 4.4.2 (Cauchy's Integral Formula for Derivatives)** Under the hypotheses of Theorem 4.4.1, $f$ has complex derivatives of all orders at every point $z$ inside $C$, and

$$
f^{(n)}(z)=\frac{n!}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,\mathrm{d}\zeta,\qquad n=0,1,2,\dots \tag{4.7}
$$

**Proof** We prove $n=1$; the induction step is the same computation with higher powers. Let $d>0$ be the distance from $z$ to $C$, $|h|<d/2$, $M=\max_C|f|$ and $L$ the length of $C$. By Eq. (4.6),

$$
\frac{f(z+h)-f(z)}{h}-\frac1{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)\,\mathrm{d}\zeta}{(\zeta-z)^2}=\frac{h}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)\,\mathrm{d}\zeta}{(\zeta-z-h)(\zeta-z)^2}.
$$

On $C$, $|\zeta-z|\ge d$ and $|\zeta-z-h|\ge d/2$, so by the ML inequality the right side is at most $\frac{|h|}{2\pi}\cdot\frac{2M}{d^3}\cdot L\to0$. $\square$

Since every point of a region $D$ lies inside a small circle in $D$, we obtain a fundamental structural fact.

**Corollary 4.4.2** If $f$ is analytic on an open set $D$, then so is $f'$; hence $f$ has complex derivatives of all orders on $D$. The real and imaginary parts of $f$ have continuous partial derivatives of all orders.

This completes the proof of Theorem 2.5.1 in [2.3.2](/2.3.2), and it is the first sign that the theory of analytic functions differs from the theory of real differentiable functions: there is no complex analogue of a function that is differentiable once but not twice. In applications Eq. (4.7) is used in reverse, to evaluate integrals.

**Example 4.4.3** $\displaystyle\oint_{|z|=1}\frac{\mathrm{e}^{2z}}{z^4}\,\mathrm{d}z=\frac{2\pi\mathrm{i}}{3!}\,\frac{\mathrm{d}^3}{\mathrm{d}z^3}\mathrm{e}^{2z}\Big|_{z=0}=\frac{2\pi\mathrm{i}\cdot8}{6}=\frac{8\pi\mathrm{i}}3$.

**Example 4.4.4** Compute $\displaystyle\oint_{|z-\mathrm{i}|=1}\frac{\mathrm{d}z}{(z^2+1)^2}$. Inside the circle the only singular point is $\mathrm{i}$ ($-\mathrm{i}$ is at distance $2$ from the center). Write the integrand as $\frac{g(z)}{(z-\mathrm{i})^2}$ with $g(z)=\frac1{(z+\mathrm{i})^2}$, analytic on the closed disc. By Eq. (4.7) with $n=1$,

$$
\oint_{|z-\mathrm{i}|=1}\frac{\mathrm{d}z}{(z^2+1)^2}=2\pi\mathrm{i}\,g'(\mathrm{i})=2\pi\mathrm{i}\cdot\frac{-2}{(2\mathrm{i})^3}=2\pi\mathrm{i}\cdot\frac{-2}{-8\mathrm{i}}=\frac\pi2.
$$

## 4.5. Consequences of the Integral Formula

### 4.5.1. Cauchy's Estimate and Liouville's Theorem

**Theorem 4.5.1 (Cauchy's Estimate)** Let $f$ be analytic on an open set containing the closed disc $|z-z_0|\le R$, and let $M(R)=\max_{|z-z_0|=R}|f(z)|$. Then

$$
\big|f^{(n)}(z_0)\big|\le\frac{n!\,M(R)}{R^n},\qquad n=0,1,2,\dots
$$

**Proof** Apply the ML inequality to Eq. (4.7) on the circle $|\zeta-z_0|=R$: $\big|f^{(n)}(z_0)\big|\le\frac{n!}{2\pi}\cdot\frac{M(R)}{R^{n+1}}\cdot2\pi R$. $\square$

**Theorem 4.5.2 (Liouville's Theorem)** A bounded entire function is constant.

**Proof** If $|f|\le M$ on $\mathbb{C}$, then for every $z_0$ and every $R>0$, Theorem 4.5.1 with $n=1$ gives $|f'(z_0)|\le M/R$. Letting $R\to\infty$, $f'(z_0)=0$. So $f'\equiv0$ and $f$ is constant (Theorem 2.3.2). $\square$

In the real domain, $\sin x$ and $\frac1{1+x^2}$ are bounded, smooth and nonconstant; Liouville's theorem says that their complex extensions must be unbounded (for $\sin z$ see Theorem 3.4.1 of [2.3.3](/2.3.3)) or have singular points ($\frac1{1+z^2}$ at $\pm\mathrm{i}$). The theorem is typically applied to an auxiliary function built from $f$, as in the following examples. Entire functions of polynomial growth, $|f(z)|\le M|z|^m$ for large $|z|$, are polynomials of degree at most $m$, by the same argument with Cauchy's estimate for $f^{(m+1)}$; this generalization and its uses are discussed in [2.3.6](/2.3.6).

**Example 4.5.1** If $f$ is entire and $\operatorname{Re}f(z)\le1$ for all $z$, then $f$ is constant. Indeed $g=\mathrm{e}^{f}$ is entire with $|g|=\mathrm{e}^{\operatorname{Re}f}\le\mathrm{e}$, so $g$ is constant by Liouville's theorem; then $0=g'=f'\mathrm{e}^f$ and $\mathrm{e}^f\ne0$ give $f'\equiv0$. The same argument applies to any one-sided bound on $\operatorname{Re}f$ or $\operatorname{Im}f$ (use $\mathrm{e}^{-f}$, $\mathrm{e}^{\pm\mathrm{i}f}$).

**Example 4.5.2** If $f$ is entire and its image avoids a disc, $|f(z)-w_0|\ge\delta>0$ for all $z$, then $g=\frac1{f-w_0}$ is entire with $|g|\le\frac1\delta$, hence constant, and so is $f$. A nonconstant entire function therefore has dense image. (Much more is true: by Picard's little theorem, it omits at most one complex value.)

**Example 4.5.3** Find all entire $f$ such that $f'=A+\mathrm{i}B$ satisfies $A\ge-2$ everywhere and $f(0)=0$, $f(1)=3$. By Example 4.5.1 applied to the entire function $-f'$ (whose real part is at most $2$), $f'$ is a constant $a$. Thus $f(z)=az+b$, and the conditions give $b=0$, $a=3$; indeed $\operatorname{Re}f'=3\ge-2$. So $f(z)=3z$.

### 4.5.2. The Fundamental Theorem of Algebra

**Theorem 4.5.3 (Fundamental Theorem of Algebra)** Every polynomial $p(z)=a_nz^n+\cdots+a_1z+a_0$ of degree $n\ge1$ with complex coefficients has a root in $\mathbb{C}$. Consequently it has exactly $n$ roots counted with multiplicity.

**Proof** Suppose $p(z)\ne0$ for all $z$. Then $g=1/p$ is entire. Since $p(z)\to\infty$ as $z\to\infty$ (Example 1.4.2 of [2.3.1](/2.3.1)), there is $R$ with $|g(z)|\le1$ for $|z|\ge R$, and $|g|$ is bounded on the compact disc $|z|\le R$ by continuity. So $g$ is a bounded entire function, constant by Liouville's theorem, and so is $p$, a contradiction. The second statement follows by dividing off linear factors $z-z_1$ one at a time. $\square$

This is the theorem used in linear algebra to guarantee eigenvalues over $\mathbb{C}$ ([Theorem 9.8.1](/2.1.9#thm-9.8.1)); the proof there was postponed to this course. A second proof, by counting zeros with Rouché's theorem, is given in [2.3.7](/2.3.7).

### 4.5.3. Morera's Theorem

Cauchy's theorem has a converse.

**Theorem 4.5.4 (Morera's Theorem)** Let $f$ be continuous on a region $D$, and suppose that $\oint_{\partial T}f(z)\,\mathrm{d}z=0$ for every closed triangle $T$ contained in $D$. Then $f$ is analytic on $D$.

**Proof** Analyticity is a local property, so it suffices to work on a disc $B\subset D$ with center $z_0$. For $z\in B$ let $F(z)=\int_{[z_0,z]}f(\zeta)\,\mathrm{d}\zeta$. For $z,z+h\in B$, the triangle with vertices $z_0,z,z+h$ lies in $B$, and the hypothesis gives $F(z+h)-F(z)=\int_{[z,z+h]}f\,\mathrm{d}\zeta$. The estimate in the proof of Theorem 4.3.1 then shows $F'=f$ on $B$. So $F$ is analytic on $B$, and by Corollary 4.4.2 so is $F'=f$. $\square$

Morera's theorem is the standard tool for proving that a function defined by a limit or an integral is analytic. For example, if $f_n$ are analytic on $D$ and $f_n\to f$ with **uniform convergence on compact subsets** of $D$, then $f$ is continuous and $\oint_{\partial T}f=\lim\oint_{\partial T}f_n=0$, so $f$ is analytic. This is the basis of the theory of power series in [2.3.5](/2.3.5).

## 4.6. The Maximum Modulus Principle and Harmonic Functions

### 4.6.1. The Maximum Modulus Principle

**Theorem 4.6.1 (Maximum Modulus Principle)** Let $f$ be analytic on a region $D$. If $|f|$ attains its maximum over $D$ at a point of $D$, then $f$ is constant on $D$. Consequently, if $D$ is bounded and $f$ is continuous on $\bar D$, then $\max_{\bar D}|f|$ is attained on the boundary $\partial D$.

**Proof** Let $M=\max_D|f|=|f(z_0)|$, and let $E=\{z\in D\mid |f(z)|=M\}$; $E$ is nonempty and closed in $D$. If $z_1\in E$ and the closed disc $|z-z_1|\le r$ lies in $D$, Corollary 4.4.1 gives

$$
M=|f(z_1)|\le\frac1{2\pi}\int_0^{2\pi}\big|f(z_1+\rho\mathrm{e}^{\mathrm{i}t})\big|\,\mathrm{d}t\le M\qquad(0<\rho\le r).
$$

Equality throughout forces the continuous function $M-|f|\ge0$ to vanish on every circle $|z-z_1|=\rho$, so $|f|=M$ on the disc, and the disc lies in $E$. Thus $E$ is also open, and since $D$ is connected, $E=D$. So $|f|$ is constant on $D$, and $f$ is constant by Corollary 2.3.1. For the second statement: $|f|$ attains its maximum on the compact set $\bar D$; if it did so only at interior points, $f$ would be constant, and then the maximum would also be attained on $\partial D$. $\square$

By the identity theorem of [2.3.5](/2.3.5), even a local maximum of $|f|$ at an interior point forces $f$ to be constant. If $f$ has no zeros in $D$, applying the theorem to $1/f$ gives the minimum modulus principle: $|f|$ then attains its minimum over $\bar D$ on $\partial D$ as well. The condition on zeros is necessary: $f(z)=z$ on $\mathbb{D}$ has minimum modulus $0$ at the center.

![The modulus of f(z) = z^2 + 2z - 1 over the closed unit disc. The surface |f| has no peak inside the disc; its maximum 2 sqrt 2 is attained on the boundary circle at z = i and z = -i (right panel). The minimum 0 is attained inside, at the zero sqrt 2 - 1 of f.](./plots/max-modulus.py)

**Example 4.6.1** Find $\max_{|z|\le1}|z^2+2z-1|$. By Theorem 4.6.1 it suffices to consider $z=\mathrm{e}^{\mathrm{i}t}$:

$$
\big|\mathrm{e}^{2\mathrm{i}t}+2\mathrm{e}^{\mathrm{i}t}-1\big|=\big|\mathrm{e}^{\mathrm{i}t}+2-\mathrm{e}^{-\mathrm{i}t}\big|=|2+2\mathrm{i}\sin t|=2\sqrt{1+\sin^2t},
$$

after dividing by $|\mathrm{e}^{\mathrm{i}t}|=1$. The maximum is $2\sqrt2$, attained at $z=\pm\mathrm{i}$.

### 4.6.2. Harmonic Functions

Through Theorem 2.5.2, the results of this chapter transfer to harmonic functions.

**Theorem 4.6.2 (Mean Value Property and Maximum Principle for Harmonic Functions)** Let $u$ be harmonic on a region $D$. Then

1. $u$ has continuous partial derivatives of all orders on $D$;
2. for every closed disc $|z-z_0|\le r$ in $D$, $u(z_0)=\frac1{2\pi}\int_0^{2\pi}u\big(z_0+r\mathrm{e}^{\mathrm{i}t}\big)\,\mathrm{d}t$;
3. if $u$ attains its maximum or its minimum over $D$ at a point of $D$, then $u$ is constant. Consequently, if $D$ is bounded and $u$ is continuous on $\bar D$, then $\max_{\bar D}u$ and $\min_{\bar D}u$ are attained on $\partial D$.

**Proof** Every disc $B\subset D$ is simply connected, so by Theorem 2.5.2 there is an analytic $f$ on $B$ with $u=\operatorname{Re}f$ there. Items 1 and 2 follow from Corollaries 4.4.2 and 4.4.1 by taking real parts. Item 3 follows from 2 by the open–closed argument in the proof of Theorem 4.6.1, applied to $u$ instead of $|f|$ (and to $-u$ for the minimum). $\square$

**Corollary 4.6.1** Let $D$ be a bounded region and $u_1,u_2$ harmonic on $D$, continuous on $\bar D$, with $u_1=u_2$ on $\partial D$. Then $u_1=u_2$ on $D$.

**Proof** The difference $u_1-u_2$ is harmonic, continuous on $\bar D$ and zero on $\partial D$; by Theorem 4.6.2 its maximum and minimum over $\bar D$ are $0$. $\square$

So the Dirichlet problem for the Laplace equation, find $u$ harmonic on $D$ with prescribed boundary values, has at most one solution. Existence, Green's functions and the Poisson formula are treated in [2.5.8](/2.5.8); conformal mappings ([2.3.8](/2.3.8)) transfer explicit solutions from the disc or half-plane to other regions.

## Summary

| Result | Statement | Typical use |
|---|---|---|
| Parametrization, Eq. (4.2) | $\int_Cf\,\mathrm{d}z=\int_a^bf(z(t))z'(t)\,\mathrm{d}t$ | direct computation |
| Eq. (4.3) | $\oint_{\lvert z-z_0\rvert=r}(z-z_0)^n\,\mathrm{d}z=2\pi\mathrm{i}$ if $n=-1$, else $0$ | basis of residues |
| ML inequality | $\lvert\int_Cf\,\mathrm{d}z\rvert\le ML$ | vanishing of arc integrals |
| Cauchy's theorem | $\oint_Cf\,\mathrm{d}z=0$ on simply connected regions | path independence |
| Deformation | integrals unchanged when contours are deformed avoiding singular points | reduce to small circles |
| Antiderivatives | $\int_{z_1}^{z_2}f\,\mathrm{d}z=\Phi(z_2)-\Phi(z_1)$ | integrals of entire functions |
| Integral formula, Eq. (4.7) | $f^{(n)}(z)=\frac{n!}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,\mathrm{d}\zeta$ | evaluate integrals; $f\in C^\infty$ |
| Cauchy's estimate | $\lvert f^{(n)}(z_0)\rvert\le n!M(R)/R^n$ | Liouville, growth arguments |
| Liouville | bounded entire $\Rightarrow$ constant | fundamental theorem of algebra |
| Morera | zero triangle integrals $\Rightarrow$ analytic | limits of analytic functions |
| Maximum modulus | $\max\lvert f\rvert$ on the boundary | estimates, uniqueness |
