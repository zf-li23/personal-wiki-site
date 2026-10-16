---
title: Elementary Functions
description: The complex exponential, logarithm, powers, trigonometric, hyperbolic and inverse trigonometric functions; multivalued functions, branches, branch cuts and branch points, and the idea of a Riemann surface.
---

The elementary functions of calculus extend to complex arguments, and the extension both unifies and complicates them. It unifies: the exponential, sine, cosine and the hyperbolic functions become a single function $\mathrm{e}^z$ seen along different directions, and identities such as $\cos^2z+\sin^2z=1$ remain valid. It complicates: $\mathrm{e}^z$ is periodic with the imaginary period $2\pi\mathrm{i}$, so its inverse, the logarithm, is multivalued, and with it all powers $z^\alpha$ and inverse trigonometric functions. Making such functions single-valued and analytic requires choosing a branch on a suitably cut region, which is the central skill of this chapter and is used constantly in the integrals of [2.3.4](/2.3.4) and [2.3.7](/2.3.7). We define the exponential directly through its real and imaginary parts; that it coincides with the power series $\sum z^n/n!$ is shown in [2.3.5](/2.3.5). Analyticity is checked with the Cauchy–Riemann equations of [2.3.2](/2.3.2).

## 3.1. The Exponential Function

**Definition 3.1.1 (Complex Exponential Function)** For $z=x+\mathrm{i}y$, the **complex exponential function** is

$$
\mathrm{e}^z=\exp z=\mathrm{e}^x(\cos y+\mathrm{i}\sin y).
$$

For real $z=x$ this is the real exponential, and for $z=\mathrm{i}y$ it is **Euler's formula**. The definition is forced if we want an entire function that agrees with $\mathrm{e}^x$ on the real axis (by the identity theorem of [2.3.5](/2.3.5)); it is also the only entire function with $f'=f$ and $f(0)=1$.

**Theorem 3.1.1** The exponential function has the following properties.

1. $\mathrm{e}^z$ is entire and $(\mathrm{e}^z)'=\mathrm{e}^z$.
2. $\mathrm{e}^{z_1+z_2}=\mathrm{e}^{z_1}\mathrm{e}^{z_2}$; consequently $(\mathrm{e}^z)^n=\mathrm{e}^{nz}$ for $n\in\mathbb{Z}$ and $1/\mathrm{e}^z=\mathrm{e}^{-z}$.
3. $|\mathrm{e}^z|=\mathrm{e}^{\operatorname{Re}z}$ and $\arg\mathrm{e}^z=\{\operatorname{Im}z+2k\pi\}$; in particular $\mathrm{e}^z\ne0$ for all $z$.
4. $\mathrm{e}^z$ is periodic with period $2\pi\mathrm{i}$, and $\mathrm{e}^{z_1}=\mathrm{e}^{z_2}$ if and only if $z_1-z_2\in2\pi\mathrm{i}\,\mathbb{Z}$.
5. $\overline{\mathrm{e}^z}=\mathrm{e}^{\bar z}$, and $\lim_{z\to\infty}\mathrm{e}^z$ does not exist.

**Proof** 1. With $u=\mathrm{e}^x\cos y$ and $v=\mathrm{e}^x\sin y$, $u_x=\mathrm{e}^x\cos y=v_y$ and $u_y=-\mathrm{e}^x\sin y=-v_x$, all continuous; by Corollary 2.2.1, $\mathrm{e}^z$ is entire with derivative $u_x+\mathrm{i}v_x=\mathrm{e}^z$.

2. $\mathrm{e}^{x_1}\mathrm{e}^{x_2}=\mathrm{e}^{x_1+x_2}$, and $(\cos y_1+\mathrm{i}\sin y_1)(\cos y_2+\mathrm{i}\sin y_2)=\cos(y_1+y_2)+\mathrm{i}\sin(y_1+y_2)$ by the addition formulas.

3. Read off from the definition.

4. By 2 it suffices to find all $z$ with $\mathrm{e}^z=1$: then $\mathrm{e}^x=1$, $\cos y=1$, $\sin y=0$, so $x=0$ and $y\in2\pi\mathbb{Z}$.

5. The first is clear. Along the positive real axis $\mathrm{e}^z\to+\infty$, along the negative real axis $\mathrm{e}^z\to0$, and along the imaginary axis $|\mathrm{e}^z|=1$. $\square$

The periodicity means that $\mathrm{e}^z$ takes each value in every horizontal strip $\{a<\operatorname{Im}z\le a+2\pi\}$. Concretely, $w=\mathrm{e}^z$ maps the vertical line $\operatorname{Re}z=x$ onto the circle $|w|=\mathrm{e}^x$ (wrapping infinitely often), and the horizontal line $\operatorname{Im}z=y$ onto the ray $\arg w=y$.

![The map w = exp(z). In the strip -pi < Im z <= pi, vertical segments go to circles centered at 0 and horizontal lines go to rays from 0; the two edges Im z = pi and Im z = -pi both go to the negative real axis. The shaded strip 0 < Im z < pi/6 goes onto a sector of angle pi/6. The whole strip covers the plane minus 0 exactly once.](./plots/exp-map.py)

**Theorem 3.1.2** The map $w=\mathrm{e}^z$ is a bijection from the strip $\{-\pi<\operatorname{Im}z\le\pi\}$ onto $\mathbb{C}\setminus\{0\}$, and an analytic bijection from the open strip $\{-\pi<\operatorname{Im}z<\pi\}$ onto the slit plane $\mathbb{C}\setminus(-\infty,0]$.

**Proof** For $w\ne0$, $\mathrm{e}^{x+\mathrm{i}y}=w$ means $\mathrm{e}^x=|w|$ and $y\in\arg w$; within the strip the only choice is $x=\ln|w|$, $y=\operatorname{Arg}w$. The open strip corresponds to $\operatorname{Arg}w\ne\pi$. $\square$

**Example 3.1.1** Solve $\mathrm{e}^z=1+\sqrt3\,\mathrm{i}$. Since $|1+\sqrt3\,\mathrm{i}|=2$ and $\operatorname{Arg}(1+\sqrt3\,\mathrm{i})=\frac\pi3$, the solutions are $z=\ln2+\mathrm{i}\big(\frac\pi3+2k\pi\big)$, $k\in\mathbb{Z}$. Also, $|\mathrm{e}^{z^2}|=\mathrm{e}^{\operatorname{Re}z^2}=\mathrm{e}^{x^2-y^2}$, and $|\mathrm{e}^{\mathrm{i}z}|=\mathrm{e}^{-y}$, which is bounded on the upper half-plane; the latter fact is the basis of Jordan's lemma in [2.3.7](/2.3.7).

**Example 3.1.2** Find the entire function $f$ with $\operatorname{Re}f=u=\mathrm{e}^x(x\cos y-y\sin y)$ and $f(0)=0$. First, $u_x=\mathrm{e}^x(x\cos y-y\sin y+\cos y)$ and $u_y=\mathrm{e}^x(-x\sin y-\sin y-y\cos y)$. Using method 3 of [§2.5.3](/2.3.2#sec-2.5.3), $f'(z)=u_x(z,0)-\mathrm{i}u_y(z,0)=\mathrm{e}^z(z+1)$, so $f(z)=z\mathrm{e}^z+\mathrm{i}c$ with $c$ real, and $f(0)=0$ gives $f(z)=z\mathrm{e}^z$. Indeed $\operatorname{Re}\big((x+\mathrm{i}y)\mathrm{e}^x(\cos y+\mathrm{i}\sin y)\big)=\mathrm{e}^x(x\cos y-y\sin y)$.

## 3.2. The Logarithm

### 3.2.1. The Multivalued Logarithm

Since $\mathrm{e}^z$ is not injective, its inverse is not a function in the ordinary sense. As in Theorem 3.1.2, the equation $\mathrm{e}^w=z$ ($z\ne0$) has the solutions $w=\ln|z|+\mathrm{i}\theta$, $\theta\in\arg z$.

**Definition 3.2.1 (Complex Logarithm)** For $z\ne0$, the **complex logarithm** of $z$ is the set of all solutions $w$ of $\mathrm{e}^w=z$:

$$
\log z=\ln|z|+\mathrm{i}\arg z=\{\ln|z|+\mathrm{i}(\operatorname{Arg}z+2k\pi)\mid k\in\mathbb{Z}\},
$$
where $\ln$ is the real natural logarithm. The value with $k=0$,
$$
\operatorname{Log}z=\ln|z|+\mathrm{i}\operatorname{Arg}z,\qquad -\pi<\operatorname{Im}\operatorname{Log}z\le\pi,
$$
is called the **principal logarithm** (the principal value of the logarithm). The logarithm of $0$ is not defined.

Notation varies between textbooks: many write $\operatorname{Ln}z$ for the multivalued logarithm and $\ln z$ for its principal value. We follow the usage of most of the English literature, $\log z$ and $\operatorname{Log}z$, and reserve $\ln$ for real arguments.

**Example 3.2.1** $\operatorname{Log}(-1)=\mathrm{i}\pi$ and $\log(-1)=\{(2k+1)\pi\mathrm{i}\}$; $\log\mathrm{i}=\{\mathrm{i}(\frac\pi2+2k\pi)\}$; $\operatorname{Log}(-1-\mathrm{i})=\frac12\ln2-\frac{3\pi}4\mathrm{i}$; and $\log1=\{2k\pi\mathrm{i}\}$: even a positive real number has infinitely many complex logarithms, of which only the principal one is real.

As sets,

$$
\log(z_1z_2)=\log z_1+\log z_2,\qquad \log\frac{z_1}{z_2}=\log z_1-\log z_2,
$$

which follows from the corresponding identities for $\arg$ (§1.1.2 of [2.3.1](/2.3.1)). Two familiar rules fail. First, $\operatorname{Log}(z_1z_2)\ne\operatorname{Log}z_1+\operatorname{Log}z_2$ in general: $\operatorname{Log}\big((-1)(-1)\big)=0$ but $\operatorname{Log}(-1)+\operatorname{Log}(-1)=2\pi\mathrm{i}$. Second, $\log z^n\ne n\log z$ for $n\ge2$: the set $n\log z=\{n\ln|z|+\mathrm{i}n(\operatorname{Arg}z+2k\pi)\}$ contains only every $n$-th value of $\log z^n$; e.g. $\log\mathrm{i}^2=\log(-1)$ contains $-\pi\mathrm{i}$, but $2\log\mathrm{i}$ does not. On the other hand $\mathrm{e}^{\log z}=z$ for every value, and $\log\mathrm{e}^z=\{z+2k\pi\mathrm{i}\}$.

### 3.2.2. Branches, Branch Cuts and Branch Points

To do analysis with the logarithm we need a single-valued function, and we want it to be continuous.

**Definition 3.2.2 (Branch)** Let $F$ be a multivalued function and $D$ a region. A continuous (single-valued) function $f$ on $D$ such that $f(z)$ is one of the values of $F(z)$ for every $z\in D$ is called a **branch** of $F$ on $D$.

**Theorem 3.2.1** $\operatorname{Log}z$ is a branch of $\log z$ on the slit plane $\mathbb{C}\setminus(-\infty,0]$, it is analytic there, and

$$
(\operatorname{Log}z)'=\frac1z.
$$

Every branch of $\log z$ on this region has the form $\operatorname{Log}z+2k\pi\mathrm{i}$ for a fixed $k\in\mathbb{Z}$, and has the same derivative.

**Proof** $\ln|z|$ is continuous on $\mathbb{C}\setminus\{0\}$ and $\operatorname{Arg}z$ is continuous on the slit plane (Example 1.4.3 of [2.3.1](/2.3.1)), so $\operatorname{Log}$ is continuous there. It is the inverse of the analytic bijection $\mathrm{e}^w$ from the open strip $|\operatorname{Im}w|<\pi$ onto the slit plane (Theorem 3.1.2), with $(\mathrm{e}^w)'=\mathrm{e}^w\ne0$, so by the inverse function rule of §2.1 of [2.3.2](/2.3.2) it is complex differentiable with derivative $\frac{1}{\mathrm{e}^w}=\frac1z$. (Alternatively, in polar form $u=\ln r$, $v=\theta$ satisfy $u_r=\frac1r=\frac1rv_\theta$ and $v_r=0=-\frac1ru_\theta$, and Eq. (2.4) gives $f'=\mathrm{e}^{-\mathrm{i}\theta}\cdot\frac1r=\frac1z$.) If $f$ is another branch, $\frac{f(z)-\operatorname{Log}z}{2\pi\mathrm{i}}$ is a continuous integer-valued function on a connected set, hence constant. $\square$

The negative real axis plays no special role for $\log z$ itself. Any ray from $0$ to $\infty$ could be removed instead: on $\mathbb{C}\setminus[0,+\infty)$, for example, choosing the argument in $(0,2\pi)$ gives the branch $\ln|z|+\mathrm{i}\theta$, $0<\theta<2\pi$. What cannot be avoided is removing some curve from $0$ to $\infty$, because of the following phenomenon.

**Definition 3.2.3 (Branch Point)** Let $F$ be a multivalued function. A point $z_0\in\hat{\mathbb{C}}$ is called a **branch point** of $F$ if for every sufficiently small circle around $z_0$ (for $z_0=\infty$: every sufficiently large circle $|z|=R$), starting from a value of $F$ at a point of the circle and following it continuously once around the circle leads back to a different value.

For $\log z$, following $\ln|z|+\mathrm{i}\theta$ once counterclockwise around any circle centered at $0$ increases $\theta$ by $2\pi$ and the value by $2\pi\mathrm{i}$, so $0$ is a branch point; the same circles are the large circles around $\infty$, so $\infty$ is a branch point too. A curve removed from the region to make the function single-valued is called a *branch cut*; for $\log z$ it must join the two branch points $0$ and $\infty$, since a region in which some closed curve winds around $0$ admits no branch. With a cut along the negative real axis, the values of $\operatorname{Log}$ just above and just below the cut differ by $2\pi\mathrm{i}$:

$$
\lim_{\varepsilon\to0^+}\operatorname{Log}(x+\mathrm{i}\varepsilon)-\lim_{\varepsilon\to0^+}\operatorname{Log}(x-\mathrm{i}\varepsilon)=2\pi\mathrm{i}\qquad(x<0).
$$

This jump is exactly what makes the keyhole contours of [2.3.7](/2.3.7) work.

### 3.2.3. Riemann Surfaces

Instead of cutting the plane, Riemann proposed to enlarge the domain. Take countably many copies ("sheets") $S_k$ of the slit plane, $k\in\mathbb{Z}$, carrying the branches $\operatorname{Log}z+2k\pi\mathrm{i}$, and glue the lower edge of the cut on $S_k$ to the upper edge of the cut on $S_{k+1}$. The result is a connected spiral surface, the *Riemann surface* of $\log z$, on which $\log$ is a single-valued analytic function: walking once around $0$ moves us to the next sheet. For $\sqrt z$ two sheets suffice, glued crosswise along the cut, since going around $0$ twice returns the original value.

![Riemann surfaces. Left: the height is Im log z = arg z over three turns around the origin; each turn is one sheet, and the sheets join into a single spiral around the branch point 0. Right: the height is Re sqrt z over two turns; after one turn the surface comes back with the opposite sign, after two turns it closes up.](./plots/riemann-surfaces.py)

In this course Riemann surfaces serve only as a picture; computations are done with branches on cut regions.

## 3.3. Powers and General Exponentials

**Definition 3.3.1 (Complex Power)** For $z\ne0$ and $\alpha\in\mathbb{C}$,

$$
z^\alpha=\mathrm{e}^{\alpha\log z}=\{\exp\big(\alpha(\operatorname{Log}z+2k\pi\mathrm{i})\big)\mid k\in\mathbb{Z}\};
$$

the value $\mathrm{e}^{\alpha\operatorname{Log}z}$ is the principal value. Similarly, for $a\ne0$ the general exponential is $a^z=\mathrm{e}^{z\log a}$; by convention $\mathrm{e}^z$ always denotes the exponential function of §3.1, not the multivalued $\exp(z\log\mathrm{e})$.

The number of distinct values of $z^\alpha$ is governed by the factor $\mathrm{e}^{2k\pi\mathrm{i}\alpha}$:

| $\alpha$ | values of $z^\alpha$ |
|---|---|
| integer $n$ | one value, the ordinary power $z^n$ |
| rational $p/q$ in lowest terms, $q\ge2$ | exactly $q$ values, the $q$-th roots of $z^p$ |
| irrational or non-real | infinitely many values |

**Example 3.3.1** Compute $\mathrm{i}^{\mathrm{i}}$, $\mathrm{i}^\pi$ and $1^{\sqrt2}$.

- $\mathrm{i}^{\mathrm{i}}=\exp\big(\mathrm{i}\cdot\mathrm{i}(\frac\pi2+2k\pi)\big)=\mathrm{e}^{-\pi/2-2k\pi}$, $k\in\mathbb{Z}$: infinitely many values, all of them positive real numbers; the principal value is $\mathrm{e}^{-\pi/2}$.
- $\mathrm{i}^\pi=\exp\big(\pi\cdot\mathrm{i}(\frac\pi2+2k\pi)\big)=\cos\big(\frac{\pi^2}2+2k\pi^2\big)+\mathrm{i}\sin\big(\frac{\pi^2}2+2k\pi^2\big)$: infinitely many values on the unit circle (distinct because $\pi$ is irrational); the principal value is $\mathrm{e}^{\mathrm{i}\pi^2/2}$.
- $1^{\sqrt2}=\mathrm{e}^{2\sqrt2k\pi\mathrm{i}}$: infinitely many points of the unit circle, dense in it, although the principal value is $1$.

**Theorem 3.3.1** On the slit plane $\mathbb{C}\setminus(-\infty,0]$, the principal value $z^\alpha=\mathrm{e}^{\alpha\operatorname{Log}z}$ is analytic, and $(z^\alpha)'=\alpha\,\dfrac{z^\alpha}{z}$. The same formula holds for every branch $\mathrm{e}^{\alpha f(z)}$, where $f$ is a branch of $\log$ on a region $D$.

**Proof** By the chain rule, $(\mathrm{e}^{\alpha f(z)})'=\mathrm{e}^{\alpha f(z)}\cdot\frac{\alpha}{z}$. $\square$

For non-integer $\alpha$, the branch points of $z^\alpha$ are $0$ and $\infty$, like those of $\log z$. The square root $\sqrt z=z^{1/2}$ has two branches on the slit plane, $\pm\sqrt{|z|}\,\mathrm{e}^{\mathrm{i}\operatorname{Arg}z/2}$; going once around $0$ multiplies the value by $\mathrm{e}^{\mathrm{i}\pi}=-1$.

**Example 3.3.2** Let $f$ be the branch of $\sqrt z$ on $\mathbb{C}\setminus[0,+\infty)$ with $f(-1)=\mathrm{i}$. Find $f(\mathrm{i})$ and $f(-\mathrm{i})$. On this region we may write $z=r\mathrm{e}^{\mathrm{i}\theta}$ with $0<\theta<2\pi$, and the two branches are $\pm\sqrt r\,\mathrm{e}^{\mathrm{i}\theta/2}$. At $z=-1$ ($\theta=\pi$) the plus sign gives $\mathrm{e}^{\mathrm{i}\pi/2}=\mathrm{i}$, so $f(z)=\sqrt r\,\mathrm{e}^{\mathrm{i}\theta/2}$. Hence $f(\mathrm{i})=\mathrm{e}^{\mathrm{i}\pi/4}=\frac{1+\mathrm{i}}{\sqrt2}$ and $f(-\mathrm{i})=\mathrm{e}^{3\pi\mathrm{i}/4}=\frac{-1+\mathrm{i}}{\sqrt2}$. Note that $f(-\mathrm{i})$ is not the principal value $\mathrm{e}^{-\mathrm{i}\pi/4}$.

**Example 3.3.3** The function $F(z)=\sqrt{z^2-1}=\sqrt{(z-1)(z+1)}$ has branch points $1$ and $-1$, but not $\infty$. Following a value continuously along a closed curve multiplies it by $(-1)^{m}$, where $m$ is the total number of times the curve winds around $1$ and around $-1$. A large circle winds once around each, so $m=2$ and the value returns. Hence on $\mathbb{C}\setminus[-1,1]$ the function $F$ has two analytic branches, one of which behaves like $z$ as $z\to\infty$. In general, which points are branch points must be checked; it is not enough to look at the zeros of the radicand.

## 3.4. Trigonometric and Hyperbolic Functions

From Euler's formula, $\cos y=\frac{\mathrm{e}^{\mathrm{i}y}+\mathrm{e}^{-\mathrm{i}y}}{2}$ and $\sin y=\frac{\mathrm{e}^{\mathrm{i}y}-\mathrm{e}^{-\mathrm{i}y}}{2\mathrm{i}}$ for real $y$. We take these as definitions for complex arguments.

**Definition 3.4.1 (Complex Trigonometric and Hyperbolic Functions)** For $z\in\mathbb{C}$,

$$
\cos z=\frac{\mathrm{e}^{\mathrm{i}z}+\mathrm{e}^{-\mathrm{i}z}}{2},\qquad \sin z=\frac{\mathrm{e}^{\mathrm{i}z}-\mathrm{e}^{-\mathrm{i}z}}{2\mathrm{i}},\qquad \cosh z=\frac{\mathrm{e}^{z}+\mathrm{e}^{-z}}{2},\qquad \sinh z=\frac{\mathrm{e}^{z}-\mathrm{e}^{-z}}{2},
$$

and $\tan z=\frac{\sin z}{\cos z}$, $\cot z=\frac{\cos z}{\sin z}$, $\tanh z=\frac{\sinh z}{\cosh z}$, wherever the denominators are nonzero.

These extend the real trigonometric functions and the real **hyperbolic functions**, and the definitions show at once that

$$
\cos(\mathrm{i}z)=\cosh z,\qquad \sin(\mathrm{i}z)=\mathrm{i}\sinh z,\qquad \cosh(\mathrm{i}z)=\cos z,\qquad \sinh(\mathrm{i}z)=\mathrm{i}\sin z.
$$

Over $\mathbb{C}$ the circular and hyperbolic functions are therefore the same functions with rotated arguments.

**Theorem 3.4.1** The following hold for all $z,z_1,z_2\in\mathbb{C}$.

1. $\sin z$ and $\cos z$ are entire, $(\sin z)'=\cos z$, $(\cos z)'=-\sin z$; $\sin$ is odd, $\cos$ is even, and both have period $2\pi$.
2. All the real addition formulas remain valid, e.g. $\sin(z_1+z_2)=\sin z_1\cos z_2+\cos z_1\sin z_2$ and $\sin^2z+\cos^2z=1$.
3. With $z=x+\mathrm{i}y$, $\sin z=\sin x\cosh y+\mathrm{i}\cos x\sinh y$, $\cos z=\cos x\cosh y-\mathrm{i}\sin x\sinh y$, and

$$
|\sin z|^2=\sin^2x+\sinh^2y,\qquad |\cos z|^2=\cos^2x+\sinh^2y.
$$

4. The zeros of $\sin z$ are exactly $z=k\pi$, and those of $\cos z$ are exactly $z=\frac\pi2+k\pi$ ($k\in\mathbb{Z}$).
5. $\sin z$ and $\cos z$ are unbounded on $\mathbb{C}$.

**Proof** 1 follows from Definition 3.4.1 and Theorem 3.1.1. For 2, both sides of each identity are polynomials in $\mathrm{e}^{\pm\mathrm{i}z_1}$ and $\mathrm{e}^{\pm\mathrm{i}z_2}$, and the identities are verified by expanding (or: they hold for real arguments, and the identity theorem of [2.3.5](/2.3.5) extends them). For 3, use the addition formula with $\cos(\mathrm{i}y)=\cosh y$ and $\sin(\mathrm{i}y)=\mathrm{i}\sinh y$, then $|\sin z|^2=\sin^2x\cosh^2y+\cos^2x\sinh^2y=\sin^2x+\sinh^2y$ using $\cosh^2y=1+\sinh^2y$; similarly for $\cos$. For 4, $\sin z=0$ means $\mathrm{e}^{2\mathrm{i}z}=1$, i.e. $2\mathrm{i}z\in2\pi\mathrm{i}\mathbb{Z}$ by Theorem 3.1.1; and $\cos z=\sin\big(\frac\pi2-z\big)$. Item 5 follows from 3: $|\sin(\mathrm{i}y)|=|\sinh y|\to\infty$. $\square$

Item 5 contrasts sharply with the real case. It is no accident: by Liouville's theorem in [2.3.4](/2.3.4), every bounded entire function is constant. Item 4 says that complexification creates no new zeros, so that $\tan z$ and $\cot z$ are analytic except at the real zeros of $\cos$ and $\sin$.

**Example 3.4.1** Solve $\cos z=2$. Putting $t=\mathrm{e}^{\mathrm{i}z}$, the equation becomes $t+\frac1t=4$, i.e. $t^2-4t+1=0$, so $t=2\pm\sqrt3$. Then $\mathrm{i}z\in\log(2\pm\sqrt3)=\{\ln(2\pm\sqrt3)+2k\pi\mathrm{i}\}$, and since $\ln(2-\sqrt3)=-\ln(2+\sqrt3)$,

$$
z=2k\pi\pm\mathrm{i}\ln\big(2+\sqrt3\big),\qquad k\in\mathbb{Z}.
$$

All solutions lie on the vertical lines $\operatorname{Re}z=2k\pi$, where $\cos(2k\pi+\mathrm{i}y)=\cosh y$ takes every value $\ge1$.

**Example 3.4.2** Solve $\sin z=\mathrm{i}$. With $t=\mathrm{e}^{\mathrm{i}z}$, $\frac{t-t^{-1}}{2\mathrm{i}}=\mathrm{i}$ gives $t^2+2t-1=0$, so $t=-1\pm\sqrt2$. For $t=\sqrt2-1>0$: $\mathrm{i}z=\ln(\sqrt2-1)+2k\pi\mathrm{i}$, so $z=2k\pi+\mathrm{i}\ln(1+\sqrt2)$. For $t=-(1+\sqrt2)<0$: $\mathrm{i}z=\ln(1+\sqrt2)+\mathrm{i}(\pi+2k\pi)$, so $z=(2k+1)\pi-\mathrm{i}\ln(1+\sqrt2)$. Check: $\sin\big(\mathrm{i}\ln(1+\sqrt2)\big)=\mathrm{i}\sinh\ln(1+\sqrt2)=\mathrm{i}\cdot\frac{(1+\sqrt2)-(\sqrt2-1)}{2}=\mathrm{i}$, and $\sin(\pi-w)=\sin w$ gives the second family.

## 3.5. Inverse Trigonometric Functions

Solving $\cos w=z$, $\sin w=z$, $\tan w=z$ for $w$ as in Examples 3.4.1 and 3.4.2 leads to quadratic equations for $t=\mathrm{e}^{\mathrm{i}w}$ and then to logarithms. The complex **inverse trigonometric functions** are therefore multivalued and expressible through $\log$ and square roots:

$$
\operatorname{Arccos}z=-\mathrm{i}\log\big(z+\sqrt{z^2-1}\big),\qquad \operatorname{Arcsin}z=-\mathrm{i}\log\big(\mathrm{i}z+\sqrt{1-z^2}\big),\qquad \operatorname{Arctan}z=\frac{1}{2\mathrm{i}}\log\frac{1+\mathrm{i}z}{1-\mathrm{i}z}\ (z\ne\pm\mathrm{i}),
$$

where on the right all values of the square root and the logarithm are taken. For instance, $\tan w=\frac{t^2-1}{\mathrm{i}(t^2+1)}$ with $t=\mathrm{e}^{\mathrm{i}w}$; setting this equal to $z$ and solving gives $t^2=\frac{1+\mathrm{i}z}{1-\mathrm{i}z}$, hence the formula for $\operatorname{Arctan}$. On a region where branches of the square root and the logarithm are fixed, these are analytic with the familiar derivatives

$$
(\arcsin z)'=\frac{1}{\sqrt{1-z^2}},\qquad (\arctan z)'=\frac{1}{1+z^2},
$$

where in the first formula the branch of the square root is the one used in the definition. The branch points of $\operatorname{Arcsin}$ and $\operatorname{Arccos}$ are $\pm1$ and $\infty$, those of $\operatorname{Arctan}$ are $\pm\mathrm{i}$; for $\operatorname{Arctan}$, $\infty$ is not a branch point, since $\frac{1+\mathrm{i}z}{1-\mathrm{i}z}\to-1$ as $z\to\infty$.

**Example 3.5.1** $\operatorname{Arctan}(2\mathrm{i})=\frac1{2\mathrm{i}}\log\frac{1-2}{1+2}=\frac1{2\mathrm{i}}\log\big(-\tfrac13\big)=\frac1{2\mathrm{i}}\big(-\ln3+\mathrm{i}(2k+1)\pi\big)=\big(k+\tfrac12\big)\pi+\frac{\mathrm{i}}2\ln3$.

## Summary

| Function | Definition | Values | Branch points | Principal branch, region |
|---|---|---|---|---|
| $\mathrm{e}^z$ | $\mathrm{e}^x(\cos y+\mathrm{i}\sin y)$ | single, period $2\pi\mathrm{i}$, never $0$ | none | entire |
| $\log z$ | $\ln\lvert z\rvert+\mathrm{i}\arg z$ | infinitely many, spaced by $2\pi\mathrm{i}$ | $0,\infty$ | $\operatorname{Log}z$ on $\mathbb{C}\setminus(-\infty,0]$, derivative $1/z$ |
| $z^\alpha$ | $\mathrm{e}^{\alpha\log z}$ | $1$, $q$, or infinitely many | $0,\infty$ ($\alpha\notin\mathbb{Z}$) | $\mathrm{e}^{\alpha\operatorname{Log}z}$, derivative $\alpha z^\alpha/z$ |
| $\sin z$, $\cos z$ | combinations of $\mathrm{e}^{\pm\mathrm{i}z}$ | single, period $2\pi$, unbounded | none | entire; zeros only real |
| $\operatorname{Arcsin}$, $\operatorname{Arccos}$, $\operatorname{Arctan}$ | $\log$ of algebraic expressions | infinitely many | $\pm1,\infty$; $\pm\mathrm{i}$ | branches on cut regions |
