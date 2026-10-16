---
title: Conformal Mappings
---

So far analytic functions have been studied through series and integrals. This chapter takes the geometric point of view: an analytic function $w = f(z)$ is a map from a region of the $z$-plane to a region of the $w$-plane, and where $f' \ne 0$ it preserves angles. Such conformal mappings transform one domain into another while carrying analytic functions to analytic functions and harmonic functions to harmonic functions. A boundary value problem for Laplace's equation in a complicated plane domain can therefore be transplanted to a disk or a half-plane, where it is solved by an explicit formula. This is the classical method for steady heat conduction, electrostatics and ideal fluid flow in two dimensions, and it complements the methods for Laplace's equation in [2.5.8](/2.5.8).

The central theoretical result is the Riemann mapping theorem: every simply connected proper subdomain of $\mathbb{C}$ can be mapped conformally onto the unit disk. Its proof is not constructive, so in practice one assembles mappings from a small toolkit. The toolkit consists of Möbius transformations, which map circles to circles and are determined by three points, together with powers, exponentials and the Joukowski map. We use the geometric meaning of the derivative from [2.3.2](/2.3.2), the elementary functions of [2.3.3](/2.3.3), and the local mapping theorem of [2.3.7](/2.3.7) (Theorem 7.7.3).

## 8.1. Conformality

### 8.1.1. Analytic Functions Preserve Angles

Let $\gamma(t)$ be a smooth curve with $\gamma(t_0) = z_0$ and $\gamma'(t_0) \ne 0$, and let $f$ be analytic at $z_0$. The image curve $\Gamma = f\circ\gamma$ has tangent vector

$$
\Gamma'(t_0) = f'(z_0)\,\gamma'(t_0).
$$

If $f'(z_0) = \rho\,\mathrm{e}^{\mathrm{i}\varphi} \ne 0$, then $\arg\Gamma'(t_0) = \arg\gamma'(t_0) + \varphi$: every curve through $z_0$ is turned through the same angle $\varphi = \arg f'(z_0)$. Moreover $\lvert f(z) - f(z_0)\rvert = \rho\lvert z - z_0\rvert + o(\lvert z - z_0\rvert)$: infinitesimal lengths at $z_0$ are stretched by the same factor $\rho = \lvert f'(z_0)\rvert$ in every direction.

**Definition 8.1.1** A continuous map $f$ defined near $z_0$ is said to be conformal at $z_0$ if for any two smooth curves through $z_0$ with nonzero tangents, the angle between their images at $f(z_0)$ equals the angle between the curves, in size and in orientation.

**Theorem 8.1.1** If $f$ is analytic at $z_0$ and $f'(z_0) \ne 0$, then $f$ is conformal at $z_0$, with rotation angle $\arg f'(z_0)$ and linear magnification $\lvert f'(z_0)\rvert$.

Both conditions matter. At a critical point the angles are multiplied: if $f - f(z_0)$ has a zero of order $m \ge 2$, then $f(z) - f(z_0) \approx c(z - z_0)^m$, and angles at $z_0$ are multiplied by $m$ (for $w = z^2$ at $0$ the right angle between the positive real and imaginary axes opens to a straight angle). The reflection $z \mapsto \bar z$ preserves the size of angles but reverses their orientation. Conversely, a real $C^1$ map of a plane domain that preserves angles with orientation and has nonzero Jacobian satisfies the Cauchy–Riemann equations (Theorem 2.2.1), so conformal maps are exactly the analytic functions with $f' \ne 0$.

**Definition 8.1.2** Let $D$ and $G$ be domains in $\mathbb{C}$ (or in $\hat{\mathbb{C}}$). A bijective analytic map $f\colon D \to G$ is called a **conformal mapping** of $D$ onto $G$; $D$ and $G$ are then said to be conformally equivalent. A conformal mapping of $D$ onto itself is a conformal automorphism of $D$.

**Theorem 8.1.2** If $f$ is analytic and injective on a domain $D$, then $f'(z) \ne 0$ for all $z \in D$, the image $G = f(D)$ is a domain, and $f^{-1}\colon G \to D$ is analytic with $(f^{-1})'(w) = \dfrac{1}{f'(z)}$ for $w = f(z)$.

**Proof** If $f'(z_0) = 0$, then $z_0$ is a zero of order $m \ge 2$ of $f - f(z_0)$ ($f$ is not constant, being injective), and by Theorem 7.7.3, values near $f(z_0)$ are taken $m$ times near $z_0$, contradicting injectivity. By the open mapping theorem (Theorem 7.7.4), $G$ is open, and it is connected as a continuous image of a connected set. The same theorem shows that $f^{-1}$ is continuous. Finally, if $w_1 \to w$ in $G$, then $z_1 = f^{-1}(w_1) \to z$, and $\frac{f^{-1}(w_1) - f^{-1}(w)}{w_1 - w} = \left(\frac{f(z_1) - f(z)}{z_1 - z}\right)^{-1} \to \frac{1}{f'(z)}$. $\square$

Hence every conformal mapping is conformal at every point in the sense of Definition 8.1.1, and its inverse is again a conformal mapping.

### 8.1.2. The Riemann Mapping Theorem

The basic problem of the theory is: given two domains, find a conformal mapping of one onto the other. Since a conformal mapping preserves topological properties, a simply connected domain cannot be mapped onto an annulus. The whole plane cannot be mapped onto the disk either, since such a map would be a bounded entire function, constant by **Liouville's theorem**. These are the only obstructions:

**Theorem 8.1.3 (Riemann Mapping Theorem)** Let $D \subsetneq \mathbb{C}$ be a simply connected domain and $z_0 \in D$. Then there is exactly one conformal mapping $f$ of $D$ onto the unit disk $\mathbb{D}$ with $f(z_0) = 0$ and $f'(z_0) > 0$.

We do not prove existence; uniqueness follows from the Schwarz lemma (§8.4). Two further facts, also stated without proof, are used constantly in applications.

- If $D$ is bounded by a Jordan curve, then $f$ extends to a homeomorphism of the closures $\overline{D} \to \overline{\mathbb{D}}$ (Carathéodory), so boundary points correspond to boundary points.
- Boundary correspondence: if $f$ is analytic on a domain bounded by a Jordan curve $C$, continuous up to $C$, and maps $C$ bijectively onto a Jordan curve $\Gamma$, then $f$ maps the interior of $C$ conformally onto the interior of $\Gamma$. In practice: traverse the boundary so that the domain lies on the left; the image domain then lies on the left of the image boundary.

The Riemann mapping theorem guarantees existence but no formula. Explicit mappings are built from the elementary maps of the next two sections.

## 8.2. Möbius Transformations

### 8.2.1. Definition and Basic Properties

**Definition 8.2.1** A map of the form

$$
w = T(z) = \frac{az + b}{cz + d}, \qquad a, b, c, d \in \mathbb{C}, \quad ad - bc \ne 0, \tag{8.1}
$$
is called a **Möbius transformation** (or fractional linear transformation). It is extended to $\hat{\mathbb{C}}$ by $T(-d/c) = \infty$ and $T(\infty) = a/c$ if $c \ne 0$, and by $T(\infty) = \infty$ if $c = 0$.

The condition $ad - bc \ne 0$ excludes constants: $T'(z) = \frac{ad - bc}{(cz + d)^2}$. Solving for $z$ gives the inverse $z = \frac{dw - b}{-cw + a}$, again a Möbius transformation, so $T$ is a bijection of $\hat{\mathbb{C}}$. The coefficients are determined only up to a common factor, and composition corresponds to multiplication of the coefficient matrices $\begin{bmatrix}a & b\\ c & d\end{bmatrix}$; the Möbius transformations form a group under composition.

For $c \ne 0$,

$$
T(z) = \frac{a}{c} + \frac{bc - ad}{c}\cdot\frac{1}{cz + d},
$$

so $T$ is a composition of three kinds of elementary maps: translations $z \mapsto z + h$, rotation-dilations $z \mapsto kz$ ($k \ne 0$), and the inversion $z \mapsto \frac1z$. (For $c = 0$, $T$ is a linear map $z \mapsto \frac adz + \frac bd$.) Translations and rotation-dilations are similarities; the inversion $\frac1z = \frac{1}{\lvert z\rvert}\mathrm{e}^{-\mathrm{i}\arg z}$ is the reflection in the unit circle ($z \mapsto z/\lvert z\rvert^2$) followed by the reflection in the real axis.

**Theorem 8.2.1** Every Möbius transformation is a conformal mapping of $\hat{\mathbb{C}}$ onto itself. Here conformality at $\infty$ and at $-d/c$ is understood in the coordinate $\zeta = 1/z$ near $\infty$ (respectively $1/w$ near $w = \infty$).

**Proof** On $\mathbb{C}\setminus\{-d/c\}$, $T' \ne 0$. Near $z = -d/c$ the function $1/T(z) = \frac{cz + d}{az + b}$ is analytic with nonzero derivative, and near $\infty$ the function $T(1/\zeta) = \frac{a + b\zeta}{c + d\zeta}$ is analytic in $\zeta$ with nonzero derivative at $\zeta = 0$. $\square$

### 8.2.2. Circles and Symmetric Points

On the Riemann sphere, lines are circles through $\infty$. We call circles and lines together *generalized circles*. A generalized circle can be written as

$$
A z\bar z + \bar\beta z + \beta\bar z + D = 0, \qquad A, D \in \mathbb{R}, \quad \beta \in \mathbb{C}, \quad \lvert\beta\rvert^2 > AD, \tag{8.2}
$$

which is a line when $A = 0$ and a circle when $A \ne 0$ (with $x^2 + y^2 = z\bar z$ and $x = \frac{z + \bar z}{2}$, $y = \frac{z - \bar z}{2\mathrm{i}}$, Eq. (8.2) is the general equation $A(x^2 + y^2) + Bx + Cy + D = 0$).

**Theorem 8.2.2 (Circle-Preserving Property)** A Möbius transformation maps generalized circles onto generalized circles.

**Proof** Translations and rotation-dilations obviously preserve circles and lines, so by the decomposition above it suffices to consider $w = \frac1z$. Substituting $z = \frac1w$ into Eq. (8.2) and multiplying by $w\bar w$ gives $A + \bar\beta\bar w + \beta w + Dw\bar w = 0$, an equation of the same form with $A$ and $D$ interchanged and $\beta$ replaced by $\bar\beta$. $\square$

A generalized circle through the pole $-d/c$ of $T$ is mapped to a line, and all others to circles. This is the main device for simplifying domains bounded by circular arcs: send an intersection point of the arcs to $\infty$, and the arcs become rays or lines.

**Definition 8.2.2** Two points $z$ and $z^*$ are **symmetric points** with respect to the circle $\lvert z - a\rvert = r$ if they lie on the same ray from $a$ and $\lvert z - a\rvert\,\lvert z^* - a\rvert = r^2$, that is,

$$
z^* = a + \frac{r^2}{\bar z - \bar a};
$$

the center $a$ and $\infty$ are also considered symmetric. With respect to a line, symmetric points are mirror images.

For example, $z$ and $\frac{1}{\bar z}$ are symmetric with respect to the unit circle, and $z$ and $\bar z$ with respect to the real axis. A geometric characterization, which follows from elementary geometry (the power of a point), is that $z$ and $z^*$ are symmetric with respect to a generalized circle $\Gamma$ if and only if every generalized circle through $z$ and $z^*$ meets $\Gamma$ at right angles. Since Möbius transformations preserve generalized circles (Theorem 8.2.2) and angles (Theorem 8.2.1), they preserve this characterization:

**Theorem 8.2.3 (Symmetry Principle)** If a Möbius transformation $T$ maps the generalized circle $\Gamma$ onto $\Gamma'$, then it maps every pair of points symmetric with respect to $\Gamma$ to a pair symmetric with respect to $\Gamma'$.

### 8.2.3. The Cross-Ratio

A Möbius transformation has three free complex parameters (four coefficients up to a common factor), and three points determine it.

**Definition 8.2.3** For distinct points $z_1, z_2, z_3 \in \hat{\mathbb{C}}$ and $z \in \hat{\mathbb{C}}$, the **cross-ratio** is

$$
(z, z_1, z_2, z_3) = \frac{z - z_1}{z - z_3}\cdot\frac{z_2 - z_3}{z_2 - z_1},
$$

with the factors containing $\infty$ omitted when one of the points is $\infty$ (for instance, $(z, z_1, z_2, \infty) = \frac{z - z_1}{z_2 - z_1}$).

As a function of $z$, the cross-ratio is the unique Möbius transformation that sends $z_1, z_2, z_3$ to $0, 1, \infty$ respectively.

**Theorem 8.2.4** 1. Möbius transformations preserve the cross-ratio: $(Tz, Tz_1, Tz_2, Tz_3) = (z, z_1, z_2, z_3)$.
2. For distinct $z_1, z_2, z_3$ and distinct $w_1, w_2, w_3$ there is exactly one Möbius transformation with $T(z_k) = w_k$ ($k = 1, 2, 3$). It is obtained by solving the following equation for $w$:

$$
(w, w_1, w_2, w_3) = (z, z_1, z_2, z_3). \tag{8.3}
$$

**Proof** A Möbius transformation $S \ne \mathrm{id}$ has at most two fixed points in $\hat{\mathbb{C}}$: the fixed points in $\mathbb{C}$ satisfy $cz^2 + (d - a)z - b = 0$, which, unless it is the zero polynomial ($S = \mathrm{id}$), has at most two roots, and when $c = 0$ the point $\infty$ is fixed but the equation has degree at most $1$. Hence two Möbius transformations that agree at three points are equal. This proves uniqueness in 2. Let $S(z) = (z, z_1, z_2, z_3)$ and $S'(w) = (w, w_1, w_2, w_3)$. Then $S'^{-1}\circ S$ sends $z_k$ to $w_k$, which proves existence. For 1, apply the same uniqueness argument to $S\circ T^{-1}$ and $z \mapsto (z, Tz_1, Tz_2, Tz_3)$, which both send $Tz_1, Tz_2, Tz_3$ to $0, 1, \infty$. $\square$

**Example 8.2.1** Find the Möbius transformation that sends $1, \mathrm{i}, -1$ to $0, 1, \infty$, and the image of the unit disk.

By Eq. (8.3), $w = (z, 1, \mathrm{i}, -1) = \frac{z - 1}{z + 1}\cdot\frac{\mathrm{i} + 1}{\mathrm{i} - 1} = \mathrm{i}\,\frac{1 - z}{1 + z}$. The unit circle passes through $1, \mathrm{i}, -1$, so its image is the generalized circle through $0, 1, \infty$, the real axis. Since $w(0) = \mathrm{i}$, the unit disk is mapped onto the upper half-plane. (Alternatively: traversing the circle counterclockwise through $1, \mathrm{i}, -1$ keeps the disk on the left, and the image traverses the real axis through $0, 1, \infty$, with the upper half-plane on the left.)

### 8.2.4. Disks and Half-Planes

Let $\mathbb{H} = \{z : \operatorname{Im}z > 0\}$ denote the upper half-plane. The following mappings are the building blocks of most constructions.

**Theorem 8.2.5** The Möbius transformations mapping $\mathbb{H}$ onto $\mathbb{D}$ are exactly

$$
w = \mathrm{e}^{\mathrm{i}\theta}\,\frac{z - a}{z - \bar a}, \qquad a \in \mathbb{H}, \quad \theta \in \mathbb{R}, \tag{8.4}
$$

and such a map sends $a$ to $0$.

**Proof** Let $T$ map $\mathbb{H}$ onto $\mathbb{D}$, and let $a = T^{-1}(0) \in \mathbb{H}$. The real axis is mapped to the unit circle. Since $a$ and $\bar a$ are symmetric with respect to the real axis, and $0$ and $\infty$ with respect to the unit circle, the symmetry principle gives $T(\bar a) = \infty$. So $T(z) = k\frac{z - a}{z - \bar a}$, and for real $x$ we have $\lvert x - a\rvert = \lvert x - \bar a\rvert$, so $\lvert T(x)\rvert = \lvert k\rvert = 1$. Conversely, Eq. (8.4) maps the real axis onto the unit circle and $a \in \mathbb{H}$ to $0 \in \mathbb{D}$, hence $\mathbb{H}$ onto $\mathbb{D}$. $\square$

The case $a = \mathrm{i}$, $\theta = 0$ is the Cayley map $w = \frac{z - \mathrm{i}}{z + \mathrm{i}}$, shown in the figure below.

![The Cayley map w = (z - i)/(z + i) from the upper half-plane (left) onto the unit disk (right). Horizontal lines Im z = c become circles tangent to the unit circle at w = 1, vertical lines Re z = c become circular arcs through w = 1 orthogonal to the unit circle, and the point i goes to the center. The two families stay orthogonal, as conformality requires](./plots/cayley-grid.py)

**Theorem 8.2.6** The Möbius transformations mapping $\mathbb{D}$ onto itself are exactly

$$
w = \mathrm{e}^{\mathrm{i}\theta}\,\frac{z - a}{1 - \bar az}, \qquad \lvert a\rvert < 1, \quad \theta \in \mathbb{R}. \tag{8.5}
$$

**Proof** As before, if $T(a) = 0$ then $T\left(1/\bar a\right) = \infty$ by symmetry with respect to the unit circle (for $a = 0$, $T(\infty) = \infty$). So $T(z) = k\frac{z - a}{1 - \bar az}$. For $\lvert z\rvert = 1$, $\lvert 1 - \bar az\rvert = \lvert z\rvert\,\lvert\bar z - \bar a\rvert = \lvert z - a\rvert$, hence $\lvert k\rvert = 1$. Conversely, Eq. (8.5) maps the unit circle onto itself and $a$ to $0$. $\square$

The map in Eq. (8.5) has $w'(a) = \frac{\mathrm{e}^{\mathrm{i}\theta}}{1 - \lvert a\rvert^2}$, so $\theta$ is the rotation angle at $a$. By §8.4 these are all the conformal automorphisms of $\mathbb{D}$, not only the Möbius ones.

**Theorem 8.2.7** Let $T(z) = \frac{az + b}{cz + d}$ with real coefficients. Then $T$ maps $\mathbb{H}$ onto $\mathbb{H}$ if $ad - bc > 0$, and onto the lower half-plane if $ad - bc < 0$.

**Proof** Multiplying numerator and denominator by $\overline{cz + d} = c\bar z + d$,

$$
T(z) = \frac{ac\lvert z\rvert^2 + adz + bc\bar z + bd}{\lvert cz + d\rvert^2}, \qquad \operatorname{Im}T(z) = \frac{(ad - bc)\operatorname{Im}z}{\lvert cz + d\rvert^2}.
$$

So $\operatorname{Im}T(z)$ has the sign of $(ad - bc)\operatorname{Im}z$. Since $T$ maps $\hat{\mathbb{R}} = \mathbb{R}\cup\{\infty\}$ onto itself and is a bijection of $\hat{\mathbb{C}}$, it maps $\mathbb{H}$ onto $\mathbb{H}$ in the first case and onto the lower half-plane in the second. $\square$

Every conformal automorphism of $\mathbb{H}$ is of this form with $ad - bc > 0$ (conjugate Theorem 8.2.6 by the Cayley map).

**Example 8.2.2** 1. The map of $\mathbb{D}$ onto itself with $\frac12 \mapsto 0$ and $f'\left(\frac12\right) > 0$ is $w = \frac{z - 1/2}{1 - z/2} = \frac{2z - 1}{2 - z}$, with $w'\left(\frac12\right) = \frac43$.
2. The right half-plane $\operatorname{Re}z > 0$ is mapped onto $\mathbb{D}$ with $1 \mapsto 0$ by $w = \frac{z - 1}{z + 1}$: the point symmetric to $1$ with respect to the imaginary axis is $-1$, which must go to $\infty$.
3. The disk $\lvert z - z_0\rvert < r$ is mapped onto $\lvert w - w_0\rvert < R$ with $z_1 \mapsto w_0$ by normalizing both disks to $\mathbb{D}$: with $\zeta = \frac{z - z_0}{r}$ and $\zeta_1 = \frac{z_1 - z_0}{r}$,

$$
\frac{w - w_0}{R} = \mathrm{e}^{\mathrm{i}\theta}\,\frac{\zeta - \zeta_1}{1 - \bar\zeta_1\zeta}.
$$

## 8.3. Mappings by Elementary Functions

### 8.3.1. Powers and Exponentials

For powers, in polar form $w = z^\alpha$ (principal branch, $\alpha > 0$) sends $z = r\mathrm{e}^{\mathrm{i}\theta}$ to $r^\alpha\mathrm{e}^{\mathrm{i}\alpha\theta}$, so it multiplies angles at the origin by $\alpha$. The sector $0 < \arg z < \beta$ ($0 < \beta \le 2\pi$) is mapped conformally onto the upper half-plane by

$$
w = z^{\pi/\beta}.
$$

For example, $z^2$ maps the first quadrant onto $\mathbb{H}$, and $\sqrt z$ (with $0 < \arg z < 2\pi$) maps the plane slit along $[0, \infty)$ onto $\mathbb{H}$. The map is not conformal at the vertex $0$, where angles are multiplied by $\frac\pi\beta$; this is exactly what straightens the corner.

For the exponential, writing $z = x + \mathrm{i}y$, $w = \mathrm{e}^z = \mathrm{e}^x\mathrm{e}^{\mathrm{i}y}$ maps horizontal lines $y = c$ onto rays $\arg w = c$ and vertical segments $x = c$, $0 < y < 2\pi$, onto circles $\lvert w\rvert = \mathrm{e}^c$ minus a point. Hence:

| Domain in the $z$-plane | Image under $\mathrm{e}^z$ |
|---|---|
| Strip $0 < \operatorname{Im}z < \pi$ | Upper half-plane $\mathbb{H}$ |
| Strip $0 < \operatorname{Im}z < 2\pi$ | Plane slit along $[0, +\infty)$ |
| Half-strip $\operatorname{Re}z < 0$, $0 < \operatorname{Im}z < \pi$ | Upper half-disk $\lvert w\rvert < 1$, $\operatorname{Im}w > 0$ |
| Strip $0 < \operatorname{Im}z < \beta$ ($\beta \le 2\pi$) | Sector $0 < \arg w < \beta$ |

A strip of width $h$ in any direction is first moved to $0 < \operatorname{Im}z < h$ by a rotation and translation and then scaled by $\frac\pi h$. The inverse maps are branches of the logarithm: $\operatorname{Log}$ maps $\mathbb{H}$ onto the strip $0 < \operatorname{Im}z < \pi$.

**Example 8.3.1** The strip $0 < \operatorname{Im}z < \pi$ is mapped onto $\mathbb{D}$ by $w = \frac{\mathrm{e}^z - \mathrm{i}}{\mathrm{e}^z + \mathrm{i}}$: first $\mathrm{e}^z$ onto $\mathbb{H}$, then the Cayley map. The point $z = \frac{\mathrm{i}\pi}{2}$ goes to $0$.

### 8.3.2. The Joukowski Map

The *Joukowski map* is

$$
w = J(z) = \frac12\left(z + \frac1z\right). \tag{8.6}
$$

Since $J(z) = J(1/z)$ and $J(z_1) - J(z_2) = \frac12(z_1 - z_2)\left(1 - \frac{1}{z_1z_2}\right)$, we have $J(z_1) = J(z_2)$ if and only if $z_1 = z_2$ or $z_1z_2 = 1$. Thus $J$ is injective on $\lvert z\rvert > 1$ and on $0 < \lvert z\rvert < 1$, and $J'(z) = \frac12\left(1 - \frac{1}{z^2}\right)$ vanishes only at $\pm1$. In polar coordinates $z = r\mathrm{e}^{\mathrm{i}\theta}$,

$$
u = \frac12\left(r + \frac1r\right)\cos\theta, \qquad v = \frac12\left(r - \frac1r\right)\sin\theta.
$$

- The circle $\lvert z\rvert = r > 1$ is mapped onto the ellipse $\frac{u^2}{a^2} + \frac{v^2}{b^2} = 1$ with $a = \frac12\left(r + \frac1r\right)$ and $b = \frac12\left(r - \frac1r\right)$. Since $a^2 - b^2 = 1$, all these ellipses have foci $\pm1$.
- The unit circle is mapped onto the segment $[-1, 1]$, traversed twice ($J(\mathrm{e}^{\mathrm{i}\theta}) = \cos\theta$).
- The ray $\arg z = \theta$, $r > 1$, is mapped onto a branch of the hyperbola $\frac{u^2}{\cos^2\theta} - \frac{v^2}{\sin^2\theta} = 1$, with the same foci.

**Theorem 8.3.1** The Joukowski map is a conformal mapping of $\{\lvert z\rvert > 1\}$ onto $\mathbb{C}\setminus[-1, 1]$; it maps $\{\lvert z\rvert > 1, \operatorname{Im}z > 0\}$ onto $\mathbb{H}$ and the upper half-disk $\{\lvert z\rvert < 1, \operatorname{Im}z > 0\}$ onto the lower half-plane.

**Proof** Injectivity on $\lvert z\rvert > 1$ was shown above. For $w \notin [-1, 1]$, the equation $J(z) = w$, that is, $z^2 - 2wz + 1 = 0$, has two roots with product $1$, neither on the unit circle (since $J$ maps the circle into $[-1, 1]$); so exactly one root lies in $\lvert z\rvert > 1$, and $J$ is onto. The statements about half-planes follow from the sign of $v$: for $\sin\theta > 0$, $v > 0$ when $r > 1$ and $v < 0$ when $r < 1$. $\square$

The inverse on $\mathbb{C}\setminus[-1, 1]$ is $z = w + \sqrt{w^2 - 1}$, with the branch of the square root that makes $\lvert z\rvert > 1$. A circle through $z = 1$ that encloses $z = -1$ is mapped to a closed curve with a cusp at $J(1) = 1$: since $J'(1) = 0$, the straight angle of the circle at $1$ is doubled to a full turn. Such images are the Joukowski airfoils, historically the first wing profiles for which lift could be computed in closed form.

![The Joukowski map w = (z + 1/z)/2. Left: images of the circles |z| = r ≥ 1 (ellipses with foci ±1; r = 1 gives the segment [-1, 1]) and of rays from the origin (hyperbolas with the same foci). Right: a circle through z = 1 slightly offset from the origin (dashed) and its image, a Joukowski airfoil with a sharp trailing edge at w = 1](./plots/joukowski.py)

### 8.3.3. Composite Mappings

Most mapping problems are solved by composing a few standard steps:

| Step | Map | Effect |
|---|---|---|
| Circular arcs meeting at $p$ and $q$ | $\dfrac{z - p}{z - q}$ | Arcs through $p, q$ become rays from $0$ |
| Two circles tangent at $p$ | $\dfrac{1}{z - p}$ | Circles become parallel lines |
| Sector of angle $\beta$ at $0$ | $z^{\pi/\beta}$ | Upper half-plane |
| Strip of width $\pi$ | $\mathrm{e}^z$ | Upper half-plane |
| Upper half-plane | $\dfrac{z - a}{z - \bar a}$ | Unit disk, $a \mapsto 0$ |

At each step one checks the images of a few boundary points and of one interior point.

**Example 8.3.2** Map the upper half-disk $D_+ = \{\lvert z\rvert < 1, \operatorname{Im}z > 0\}$ onto $\mathbb{D}$.

The boundary arcs (the segment $[-1, 1]$ and the upper semicircle) meet at $\pm1$ at right angles. The map $\zeta_1 = \frac{1 + z}{1 - z}$ sends $-1 \mapsto 0$, $1 \mapsto \infty$, $0 \mapsto 1$, $\mathrm{i} \mapsto \mathrm{i}$; it maps the segment onto the positive real axis and the semicircle onto the positive imaginary axis, so $D_+$ goes onto the first quadrant. Then $\zeta_2 = \zeta_1^2$ maps the quadrant onto $\mathbb{H}$, and the Cayley map finishes:

$$
w = \frac{\zeta_2 - \mathrm{i}}{\zeta_2 + \mathrm{i}} = \frac{(1 + z)^2 - \mathrm{i}(1 - z)^2}{(1 + z)^2 + \mathrm{i}(1 - z)^2}.
$$

**Example 8.3.3** Map the crescent $D = \{\lvert z - 1\rvert < 1,\ \lvert z - \frac12\rvert > \frac12\}$ onto $\mathbb{D}$.

The two boundary circles are tangent at $0$. The inversion $w_1 = \frac1z$ sends the circle $\lvert z - 1\rvert = 1$ (through $0$ and $2$) to the line $\operatorname{Re}w_1 = \frac12$, and the circle $\lvert z - \frac12\rvert = \frac12$ (through $0$ and $1$) to the line $\operatorname{Re}w_1 = 1$. The point $z = \frac32 \in D$ goes to $\frac23$, so $D$ is mapped onto the strip $\frac12 < \operatorname{Re}w_1 < 1$. Next, $w_2 = 2\pi\mathrm{i}\left(w_1 - \frac12\right)$ rotates and scales it onto $0 < \operatorname{Im}w_2 < \pi$; $w_3 = \mathrm{e}^{w_2}$ maps that onto $\mathbb{H}$; and $w = \frac{w_3 - \mathrm{i}}{w_3 + \mathrm{i}}$ maps onto $\mathbb{D}$. Since $\mathrm{e}^{w_2} = \mathrm{e}^{2\pi\mathrm{i}/z}\mathrm{e}^{-\mathrm{i}\pi} = -\mathrm{e}^{2\pi\mathrm{i}/z}$,

$$
w = \frac{\mathrm{e}^{2\pi\mathrm{i}/z} + \mathrm{i}}{\mathrm{e}^{2\pi\mathrm{i}/z} - \mathrm{i}}.
$$

**Example 8.3.4** Map the sector $S = \{\lvert z\rvert < 1,\ 0 < \arg z < \frac\pi2\}$ (a quarter disk) onto $\mathbb{H}$. The map $\zeta = z^2$ opens it to the upper half-disk, and Example 8.3.2 maps the upper half-disk onto the first quadrant by $\frac{1 + \zeta}{1 - \zeta}$; squaring once more gives

$$
w = \left(\frac{1 + z^2}{1 - z^2}\right)^2.
$$

## 8.4. The Schwarz Lemma

The maximum modulus principle yields a rigidity theorem for self-maps of the disk, which determines all conformal automorphisms of $\mathbb{D}$ and gives the uniqueness in the Riemann mapping theorem.

**Theorem 8.4.1 (Schwarz Lemma)** Let $f$ be analytic on $\mathbb{D}$ with $\lvert f(z)\rvert < 1$ and $f(0) = 0$. Then

$$
\lvert f(z)\rvert \le \lvert z\rvert \quad (z \in \mathbb{D}), \qquad \lvert f'(0)\rvert \le 1.
$$

If $\lvert f(z_0)\rvert = \lvert z_0\rvert$ for some $z_0 \ne 0$, or $\lvert f'(0)\rvert = 1$, then $f(z) = \mathrm{e}^{\mathrm{i}\theta}z$ for some real $\theta$.

**Proof** The function $g(z) = \frac{f(z)}{z}$, with $g(0) = f'(0)$, has a removable singularity at $0$ and is analytic on $\mathbb{D}$. For $0 < r < 1$, $\lvert g\rvert \le \frac1r$ on $\lvert z\rvert = r$, hence on $\lvert z\rvert \le r$ by the **maximum modulus principle**. Letting $r \to 1$ gives $\lvert g\rvert \le 1$ on $\mathbb{D}$, which is both inequalities. If $\lvert g\rvert = 1$ at an interior point, $\lvert g\rvert$ attains its maximum there, so $g$ is a constant of modulus $1$. $\square$

**Corollary 8.4.1** Every conformal automorphism of $\mathbb{D}$ is a Möbius transformation of the form in Eq. (8.5).

**Proof** Let $f$ be a conformal automorphism of $\mathbb{D}$, let $a = f^{-1}(0)$, and let $\varphi_a(z) = \frac{z - a}{1 - \bar az}$. Then $h = f\circ\varphi_a^{-1}$ is a conformal automorphism with $h(0) = 0$. The Schwarz lemma applied to $h$ and $h^{-1}$ gives $\lvert h'(0)\rvert \le 1$ and $\lvert 1/h'(0)\rvert \le 1$, so $\lvert h'(0)\rvert = 1$ and $h(z) = \mathrm{e}^{\mathrm{i}\theta}z$. Hence $f = \mathrm{e}^{\mathrm{i}\theta}\varphi_a$. $\square$

The same argument proves uniqueness in Theorem 8.1.3: if $f_1, f_2$ both map $D$ onto $\mathbb{D}$ with $z_0 \mapsto 0$ and positive derivative, then $f_2\circ f_1^{-1}$ is an automorphism of $\mathbb{D}$ fixing $0$ with positive derivative, hence the identity.

**Example 8.4.1** Let $f$ be analytic on $\mathbb{D}$ with $\lvert f\rvert < 1$ and $f\left(\frac12\right) = 0$. How large can $\lvert f(0)\rvert$ be? Let $\varphi(z) = \frac{2z - 1}{2 - z}$ (Example 8.2.2), which maps $\mathbb{D}$ onto itself with $\varphi\left(\frac12\right) = 0$ and $\varphi(0) = -\frac12$. The function $g = f\circ\varphi^{-1}$ satisfies the hypotheses of the Schwarz lemma, so $\lvert f(0)\rvert = \lvert g(\varphi(0))\rvert \le \lvert\varphi(0)\rvert = \frac12$, with equality exactly for $f = \mathrm{e}^{\mathrm{i}\theta}\varphi$.

## 8.5. Applications to Laplace's Equation

### 8.5.1. Harmonic Functions under Conformal Mappings

**Theorem 8.5.1** Let $f\colon D \to G$ be analytic and $u$ harmonic on $G$. Then $u\circ f$ is harmonic on $D$. Moreover

$$
\Delta(u\circ f)(z) = \lvert f'(z)\rvert^2\,(\Delta u)(f(z))
$$

for every $C^2$ function $u$ on $G$.

**Proof** Let $z_0 \in D$ and let $B$ be a disk around $f(z_0)$ in $G$. On the simply connected domain $B$ the **harmonic function** $u$ has a **harmonic conjugate** $v$ ([2.3.2](/2.3.2)), so $u = \operatorname{Re}F$ with $F = u + \mathrm{i}v$ analytic on $B$. Near $z_0$, $u\circ f = \operatorname{Re}(F\circ f)$ is the real part of an analytic function, hence harmonic. The formula for general $u$ follows from the chain rule and the Cauchy–Riemann equations for $f$. $\square$

Boundary conditions transform simply as well. Dirichlet data are carried along pointwise ($u = \varphi$ on $\partial G$ becomes $u\circ f = \varphi\circ f$ on $\partial D$). A homogeneous Neumann condition $\frac{\partial u}{\partial\boldsymbol{n}} = 0$ (an insulated boundary or a wall) is preserved, because conformal mappings preserve the orthogonality of level curves and boundary. Hence, to solve the Dirichlet problem

$$
\Delta u = 0 \ \text{ in } D, \qquad u = \varphi \ \text{ on } \partial D,
$$

on a simply connected domain $D$, we map $D$ conformally onto $\mathbb{H}$ or $\mathbb{D}$ by some $f$, solve there by the Poisson integral formula ([2.5.8](/2.5.8)) or by inspection, and compose with $f$. For piecewise constant boundary data the solution on $\mathbb{H}$ is elementary: $\operatorname{Arg}(z - x_0) = \operatorname{Im}\operatorname{Log}(z - x_0)$ is harmonic on $\mathbb{H}$, equal to $\pi$ on the real axis left of $x_0$ and $0$ on the right.

**Example 8.5.1** On $\mathbb{H}$, let the boundary values be $T_0$ on $(-\infty, x_1)$, $T_1$ on $(x_1, x_2)$, …, $T_n$ on $(x_n, +\infty)$. Then

$$
u(z) = T_n + \frac1\pi\sum_{k=1}^n(T_{k-1} - T_k)\operatorname{Arg}(z - x_k)
$$

is the bounded harmonic function with these boundary values: for real $x \in (x_j, x_{j+1})$ the arguments equal $\pi$ for $k > j$ and $0$ for $k \le j$, and the sum telescopes to $T_j$. For $n = 1$ the isotherms are rays from $x_1$; for $n = 2$ and $T_0 = T_2$ they are circular arcs through $x_1$ and $x_2$.

**Example 8.5.2** Steady temperature in the first quadrant with $u = T_1$ on the positive real axis and $u = T_2$ on the positive imaginary axis. The map $z^2$ sends the quadrant onto $\mathbb{H}$, the positive real axis to the positive real axis and the positive imaginary axis to the negative real axis. By Example 8.5.1 with $n = 1$,

$$
u = T_1 + \frac{T_2 - T_1}{\pi}\operatorname{Arg}z^2 = T_1 + \frac{2(T_2 - T_1)}{\pi}\operatorname{Arg}z,
$$

and the isotherms are rays from the corner.

**Example 8.5.3** Find the harmonic function in $\mathbb{D}$ with boundary values $1$ on the upper semicircle and $0$ on the lower semicircle.

The map $\zeta = \mathrm{i}\frac{1 + z}{1 - z}$ is the map of Example 8.2.1 composed with the rotation $z \mapsto -z$, so it maps $\mathbb{D}$ onto $\mathbb{H}$. On the boundary, $z = \mathrm{e}^{\mathrm{i}\theta}$ gives $\frac{1 + z}{1 - z} = \mathrm{i}\cot\frac\theta2$, so $\zeta = -\cot\frac\theta2$: the upper semicircle ($0 < \theta < \pi$) goes to the negative real axis and the lower one to the positive real axis. The function $\frac1\pi\operatorname{Arg}\zeta$ is harmonic on $\mathbb{H}$, equal to $1$ on the negative and $0$ on the positive real axis. Since $\frac{1 + z}{1 - z} = \frac{1 - \lvert z\rvert^2 + 2\mathrm{i}y}{\lvert 1 - z\rvert^2}$ lies in the right half-plane,

$$
u(x, y) = \frac1\pi\operatorname{Arg}\left(\mathrm{i}\,\frac{1 + z}{1 - z}\right) = \frac12 + \frac1\pi\arctan\frac{2y}{1 - x^2 - y^2}.
$$

At the center $u = \frac12$, the mean of the boundary values, as the **mean value property** requires. The isotherms are arcs of circles through $\pm1$.

### 8.5.2. Complex Potentials of Plane Flows

Consider a steady, incompressible and irrotational flow of an ideal fluid in a plane domain, with velocity field $\boldsymbol{v} = (v_1, v_2)$. Incompressibility $\operatorname{div}\boldsymbol{v} = 0$ and irrotationality $\partial_xv_2 - \partial_yv_1 = 0$ say that, locally, $\boldsymbol{v} = \nabla\phi$ for a velocity potential $\phi$ and $(v_1, v_2) = (\psi_y, -\psi_x)$ for a stream function $\psi$. Then $\phi_x = \psi_y$ and $\phi_y = -\psi_x$, which are the Cauchy–Riemann equations.

**Definition 8.5.1** For such a flow, the analytic function $F = \phi + \mathrm{i}\psi$ is the **complex potential** of the flow; $\phi$ is its velocity potential and $\psi$ its **stream function**.

Since $F' = \phi_x + \mathrm{i}\psi_x = v_1 - \mathrm{i}v_2$, the velocity is $\boldsymbol{v} \leftrightarrow \overline{F'(z)}$, and the speed is $\lvert F'(z)\rvert$. The streamlines are the level curves $\psi = \text{const}$, orthogonal to the equipotentials $\phi = \text{const}$. Fluid cannot cross a solid wall, so walls must be streamlines.

**Example 8.5.4** 1. Uniform flow with speed $U$ in the $x$-direction: $F = Uz$.
2. Flow past the circular cylinder $\lvert z\rvert \le a$ that is uniform at infinity:

$$
F(z) = U\left(z + \frac{a^2}{z}\right).
$$

On $\lvert z\rvert = a$ we have $\frac{a^2}{z} = \bar z$, so $F = 2U\operatorname{Re}z$ is real and $\psi = 0$: the circle is a streamline, and $F \approx Uz$ at infinity. The velocity $\overline{F'} = U\left(1 - \frac{a^2}{\bar z^2}\right)$ vanishes at the stagnation points $\pm a$ and reaches its maximum $2U$ at $\pm\mathrm{i}a$. Up to the factor $2Ua$, $F$ is the Joukowski map of Eq. (8.6) applied to $z/a$; composing with a Joukowski map that sends a circle onto an airfoil gives the flow past the airfoil.
3. A source of strength $m$ at the origin: $F = \frac{m}{2\pi}\operatorname{Log}z$, with radial streamlines $\arg z = \text{const}$.

![Two applications. Left: the steady temperature in the unit disk with boundary values 1 on the upper semicircle and 0 on the lower one (Example 8.5.3); the isotherms are circular arcs through ±1. Right: streamlines Im F = const of the flow past a cylinder, F(z) = z + 1/z (Example 8.5.4); the unit circle is itself a streamline](./plots/laplace-applications.py)

## Summary

| Topic | Key facts |
|---|---|
| Conformality | $f'(z_0) \ne 0$: rotation by $\arg f'(z_0)$, magnification $\lvert f'(z_0)\rvert$; analytic and injective $\Rightarrow$ $f' \ne 0$, inverse analytic |
| Riemann mapping theorem | Simply connected $D \subsetneq \mathbb{C}$ $\cong$ $\mathbb{D}$, unique with $f(z_0) = 0$, $f'(z_0) > 0$ |
| Möbius transformations | Translations, rotation-dilations, inversion; generalized circles to generalized circles; symmetric points to symmetric points; three points determine the map via the cross-ratio |
| Standard Möbius maps | $\mathbb{H} \to \mathbb{D}$: $\mathrm{e}^{\mathrm{i}\theta}\frac{z - a}{z - \bar a}$; $\mathbb{D} \to \mathbb{D}$: $\mathrm{e}^{\mathrm{i}\theta}\frac{z - a}{1 - \bar az}$; real coefficients with $ad - bc > 0$: $\mathbb{H} \to \mathbb{H}$ |
| Elementary maps | $z^{\pi/\beta}$: sector $\to \mathbb{H}$; $\mathrm{e}^z$: strip of width $\pi$ $\to \mathbb{H}$; Joukowski: $\lvert z\rvert > 1 \to \mathbb{C}\setminus[-1, 1]$ |
| Schwarz lemma | $f(\mathbb{D}) \subseteq \mathbb{D}$, $f(0) = 0$ $\Rightarrow$ $\lvert f(z)\rvert \le \lvert z\rvert$; automorphisms of $\mathbb{D}$ are Möbius |
| Laplace's equation | Harmonic $\circ$ analytic is harmonic; map to $\mathbb{H}$ or $\mathbb{D}$, solve, compose back; complex potential $F = \phi + \mathrm{i}\psi$, velocity $\overline{F'}$ |
