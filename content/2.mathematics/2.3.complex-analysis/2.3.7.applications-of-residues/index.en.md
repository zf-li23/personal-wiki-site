---
title: Applications of Residues
---

The **residue theorem** of [2.3.6](/2.3.6) reduces a contour integral to a finite sum of residues. This chapter turns that observation into a set of practical methods. Many definite integrals over $[0, 2\pi]$ or over the real line, including integrals with no elementary antiderivative, become the real part of a contour integral once a suitable closed contour is chosen and the contributions of its auxiliary pieces are shown to vanish. The same estimates (the large-arc lemma, Jordan's lemma and the small-arc lemma) are the ones used to compute Fourier transforms and to invert Laplace transforms by residues, which is how these transforms are applied to partial differential equations in [2.5.6](/2.5.6). Residues also sum certain series in closed form.

In the last section the integrand is the logarithmic derivative $f'/f$. Its residues count zeros and poles, which gives the argument principle and Rouché's theorem, tools for locating the zeros of polynomials and transcendental functions without computing them. They also give local information about analytic maps (the open mapping theorem and local injectivity), which the next chapter ([2.3.8](/2.3.8)) needs for conformal mappings.

## 7.1. Trigonometric Integrals

Let $R(x, y)$ be a rational function of two variables that is finite on the unit circle $x^2 + y^2 = 1$, and consider

$$
I = \int_0^{2\pi}R(\cos\theta, \sin\theta)\,\mathrm{d}\theta.
$$

On the unit circle $z = \mathrm{e}^{\mathrm{i}\theta}$ we have

$$
\cos\theta = \frac{1}{2}\left(z + \frac1z\right), \qquad \sin\theta = \frac{1}{2\mathrm{i}}\left(z - \frac1z\right), \qquad \mathrm{d}\theta = \frac{\mathrm{d}z}{\mathrm{i}z},
$$

and as $\theta$ runs over $[0, 2\pi]$, $z$ runs once around $\lvert z\rvert = 1$ counterclockwise. Hence $I$ is the integral of a rational function of $z$ over the unit circle:

$$
I = \oint_{\lvert z\rvert = 1}R\left(\frac{z + z^{-1}}{2}, \frac{z - z^{-1}}{2\mathrm{i}}\right)\frac{\mathrm{d}z}{\mathrm{i}z} = 2\pi\mathrm{i}\sum_{\lvert z_k\rvert < 1}\operatorname{Res}(F, z_k), \tag{7.1}
$$

where $F$ denotes the integrand in $z$ and the sum runs over its poles inside the unit disk.

**Example 7.1.1** For $a > \lvert b\rvert > 0$,

$$
\int_0^{2\pi}\frac{\mathrm{d}\theta}{a + b\cos\theta} = \oint_{\lvert z\rvert = 1}\frac{2\,\mathrm{d}z}{\mathrm{i}(bz^2 + 2az + b)} = \frac{2\pi}{\sqrt{a^2 - b^2}}.
$$

The roots of $bz^2 + 2az + b$ are $z_\pm = \frac{-a \pm \sqrt{a^2 - b^2}}{b}$. They are real, their product is $1$, and $\lvert z_+\rvert < 1 < \lvert z_-\rvert$. The residue at the simple pole $z_+$ is $\frac{2}{\mathrm{i}b(z_+ - z_-)} = \frac{1}{\mathrm{i}\sqrt{a^2 - b^2}}$, and Eq. (7.1) gives the result.

**Example 7.1.2** Let $0 < \lvert p\rvert < 1$ be real and $n \ge 0$ an integer. We show

$$
\int_0^{2\pi}\frac{\cos n\theta}{1 - 2p\cos\theta + p^2}\,\mathrm{d}\theta = \frac{2\pi p^n}{1 - p^2}.
$$

Writing $\cos n\theta = \frac12(z^n + z^{-n})$ would produce a pole of order $n$ at $0$. It is better to integrate $\mathrm{e}^{\mathrm{i}n\theta} = z^n$ and take the real part. Since $1 - 2p\cos\theta + p^2 = (1 - pz)(1 - p/z) = \frac{(1 - pz)(z - p)}{z}$,

$$
J = \int_0^{2\pi}\frac{\mathrm{e}^{\mathrm{i}n\theta}\,\mathrm{d}\theta}{1 - 2p\cos\theta + p^2} = \oint_{\lvert z\rvert = 1}\frac{z^n\,\mathrm{d}z}{\mathrm{i}(1 - pz)(z - p)}.
$$

The only pole inside the unit circle is $z = p$, with residue $\frac{p^n}{\mathrm{i}(1 - p^2)}$, so $J = \frac{2\pi p^n}{1 - p^2}$. This is real, so it is the value of the cosine integral (and the sine integral vanishes, as symmetry also shows). For example, with $p = \frac12$ and $n = 2$, since $5 - 4\cos\theta = 4\left(1 - \cos\theta + \frac14\right)$,

$$
\int_0^{2\pi}\frac{\cos2\theta}{5 - 4\cos\theta}\,\mathrm{d}\theta = \frac14\cdot\frac{2\pi\cdot\frac14}{1 - \frac14} = \frac{\pi}{6}.
$$

## 7.2. Integrals of Rational Functions over the Real Line

For integrals over $\mathbb{R}$ we close the interval $[-R, R]$ by an arc and let $R \to \infty$. The arc contributes nothing if the integrand decays fast enough:

**Lemma 7.2.1 (Large-Arc Lemma)** Let $f$ be continuous on the arcs $C_R = \{R\mathrm{e}^{\mathrm{i}\theta} : \theta_1 \le \theta \le \theta_2\}$ for all large $R$, and suppose $\max_{z\in C_R}\lvert zf(z)\rvert \to 0$ as $R \to \infty$. Then $\int_{C_R}f(z)\,\mathrm{d}z \to 0$.

**Proof** By the ML inequality (Theorem 4.1.2), $\left\lvert\int_{C_R}f\,\mathrm{d}z\right\rvert \le \max_{C_R}\lvert f\rvert\cdot R(\theta_2 - \theta_1) = (\theta_2 - \theta_1)\max_{C_R}\lvert zf(z)\rvert \to 0$. $\square$

**Theorem 7.2.1** Let $R = \frac PQ$ be a rational function with $\deg Q \ge \deg P + 2$ and no real poles. Then

$$
\int_{-\infty}^{\infty}R(x)\,\mathrm{d}x = 2\pi\mathrm{i}\sum_{\operatorname{Im}z_k > 0}\operatorname{Res}(R, z_k). \tag{7.2}
$$

**Proof** The integral converges absolutely since $\lvert R(x)\rvert = O(x^{-2})$. For $R$ larger than the moduli of all poles, apply the residue theorem to the closed contour formed by $[-R, R]$ and the upper semicircle $C_R$ (panel (a) of the figure in §7.4): $\int_{-R}^RR(x)\,\mathrm{d}x + \int_{C_R}R(z)\,\mathrm{d}z = 2\pi\mathrm{i}\sum_{\operatorname{Im}z_k > 0}\operatorname{Res}(R, z_k)$. Since $zR(z) = O(1/z)$, Lemma 7.2.1 shows that the arc integral tends to $0$. $\square$

One may equally close in the lower half-plane; the result is then $-2\pi\mathrm{i}$ times the sum of the residues in the lower half-plane, consistent with Theorem 6.3.3 because $\operatorname{Res}(R, \infty) = 0$.

**Example 7.2.1** 1. $\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{(x^2 + 1)^2}$: the only pole in the upper half-plane is $\mathrm{i}$, of order $2$, with residue $\frac{\mathrm{d}}{\mathrm{d}z}(z + \mathrm{i})^{-2}\big|_{z=\mathrm{i}} = -2(2\mathrm{i})^{-3} = \frac{1}{4\mathrm{i}}$. The integral is $2\pi\mathrm{i}\cdot\frac{1}{4\mathrm{i}} = \frac\pi2$.
2. $\int_0^\infty\frac{\mathrm{d}x}{x^4 + 1} = \frac12\int_{-\infty}^\infty\frac{\mathrm{d}x}{x^4 + 1}$. The poles in the upper half-plane are $\mathrm{e}^{\mathrm{i}\pi/4}$ and $\mathrm{e}^{3\mathrm{i}\pi/4}$, with residues $-\frac{z_k}{4}$ (Example 6.3.1), whose sum is $-\frac{\mathrm{i}\sqrt2}{4}$. Hence $\int_0^\infty\frac{\mathrm{d}x}{x^4 + 1} = \frac12\cdot2\pi\mathrm{i}\cdot\left(-\frac{\mathrm{i}\sqrt2}{4}\right) = \frac{\pi}{2\sqrt2}$.

Contours other than semicircles are useful when the integrand has a rotational symmetry.

**Example 7.2.2** For an integer $n \ge 2$,

$$
\int_0^\infty\frac{\mathrm{d}x}{1 + x^n} = \frac{\pi/n}{\sin(\pi/n)}.
$$

Integrate $f(z) = \frac1{1 + z^n}$ over the boundary of the sector $0 \le \arg z \le \frac{2\pi}{n}$, $\lvert z\rvert \le R$. On the ray $z = t\mathrm{e}^{2\pi\mathrm{i}/n}$ we have $z^n = t^n$, so this edge, traversed inward, contributes $-\mathrm{e}^{2\pi\mathrm{i}/n}I$, where $I$ is the desired integral. The arc contributes $0$ in the limit by Lemma 7.2.1. The only pole inside is $z_0 = \mathrm{e}^{\mathrm{i}\pi/n}$, with residue $\frac{1}{nz_0^{n-1}} = \frac{z_0}{nz_0^n} = -\frac{z_0}{n}$. Therefore

$$
\left(1 - \mathrm{e}^{2\pi\mathrm{i}/n}\right)I = -\frac{2\pi\mathrm{i}}{n}\mathrm{e}^{\mathrm{i}\pi/n}, \qquad I = \frac{2\pi\mathrm{i}}{n\left(\mathrm{e}^{\mathrm{i}\pi/n} - \mathrm{e}^{-\mathrm{i}\pi/n}\right)} = \frac{\pi}{n\sin(\pi/n)}.
$$

For $n = 3$ this gives $\frac{2\pi}{3\sqrt3}$, and for $n = 4$ the value $\frac{\pi}{2\sqrt2}$ of Example 7.2.1.

## 7.3. Fourier-Type Integrals and Jordan's Lemma

### 7.3.1. Jordan's Lemma

Integrals $\int_{-\infty}^\infty R(x)\mathrm{e}^{\mathrm{i}ax}\,\mathrm{d}x$ occur whenever a Fourier transform is computed. If $\deg Q = \deg P + 1$, the large-arc lemma does not apply, but the factor $\mathrm{e}^{\mathrm{i}az}$ decays in the upper half-plane when $a > 0$, since $\lvert\mathrm{e}^{\mathrm{i}az}\rvert = \mathrm{e}^{-a\operatorname{Im}z}$. Jordan's lemma makes this decay quantitative.

**Lemma 7.3.1 (Jordan's Lemma)** Let $a > 0$, let $g$ be continuous on the upper semicircles $C_R = \{R\mathrm{e}^{\mathrm{i}\theta} : 0 \le \theta \le \pi\}$ for all large $R$, and suppose $M(R) = \max_{C_R}\lvert g\rvert \to 0$. Then

$$
\lim_{R\to\infty}\int_{C_R}g(z)\,\mathrm{e}^{\mathrm{i}az}\,\mathrm{d}z = 0.
$$

**Proof** On $C_R$, $\lvert\mathrm{e}^{\mathrm{i}az}\rvert = \mathrm{e}^{-aR\sin\theta}$. Jordan's inequality $\sin\theta \ge \frac{2\theta}{\pi}$ for $0 \le \theta \le \frac\pi2$ (concavity of $\sin$) and the symmetry $\theta \mapsto \pi - \theta$ give

$$
\left\lvert\int_{C_R}g\,\mathrm{e}^{\mathrm{i}az}\,\mathrm{d}z\right\rvert \le M(R)\int_0^\pi\mathrm{e}^{-aR\sin\theta}R\,\mathrm{d}\theta = 2M(R)\int_0^{\pi/2}\mathrm{e}^{-aR\sin\theta}R\,\mathrm{d}\theta \le 2M(R)\int_0^{\pi/2}\mathrm{e}^{-2aR\theta/\pi}R\,\mathrm{d}\theta < \frac{\pi}{a}M(R),
$$

which tends to $0$. $\square$

Only $M(R) \to 0$ is required, not $RM(R) \to 0$: the exponential factor supplies the missing decay. For $a < 0$ the same holds on lower semicircles, and the analogous statement for left half-circles $\{c + R\mathrm{e}^{\mathrm{i}\theta} : \frac\pi2 \le \theta \le \frac{3\pi}2\}$ and the factor $\mathrm{e}^{st}$ with $t > 0$ is used for Laplace transforms below.

### 7.3.2. Integrals with an Oscillating Factor

**Theorem 7.3.1** Let $R = \frac PQ$ be rational with $\deg Q \ge \deg P + 1$ and no real poles, and let $a > 0$. Then

$$
\int_{-\infty}^{\infty}R(x)\,\mathrm{e}^{\mathrm{i}ax}\,\mathrm{d}x = 2\pi\mathrm{i}\sum_{\operatorname{Im}z_k > 0}\operatorname{Res}\left(R(z)\mathrm{e}^{\mathrm{i}az}, z_k\right). \tag{7.3}
$$

For $a < 0$ one closes in the lower half-plane: the integral is $-2\pi\mathrm{i}$ times the sum of the residues with $\operatorname{Im}z_k < 0$. If $R$ is real on $\mathbb{R}$, the real and imaginary parts of Eq. (7.3) give $\int R(x)\cos ax\,\mathrm{d}x$ and $\int R(x)\sin ax\,\mathrm{d}x$.

**Proof** Close $[-R, R]$ by the upper semicircle and apply Jordan's lemma with $g = R$, which tends to $0$ at $\infty$. $\square$

When $\deg Q = \deg P + 1$ the integral converges only conditionally, and the semicircle argument proves convergence of the symmetric limits $\int_{-R}^R$. The integrals over $[0, B]$ and $[-A, 0]$ converge separately by **Dirichlet's test** for integrals, so the improper integral exists in the usual sense.

**Example 7.3.1** Compute $\int_{-\infty}^{\infty}\frac{\cos x}{x^2 - 2x + 5}\,\mathrm{d}x$ and $\int_{-\infty}^{\infty}\frac{\sin x}{x^2 - 2x + 5}\,\mathrm{d}x$.

The poles of $\frac{\mathrm{e}^{\mathrm{i}z}}{z^2 - 2z + 5}$ are $1 \pm 2\mathrm{i}$; only $1 + 2\mathrm{i}$ lies in the upper half-plane, with residue $\frac{\mathrm{e}^{\mathrm{i}(1 + 2\mathrm{i})}}{4\mathrm{i}} = \frac{\mathrm{e}^{-2}\mathrm{e}^{\mathrm{i}}}{4\mathrm{i}}$. By Eq. (7.3),

$$
\int_{-\infty}^{\infty}\frac{\mathrm{e}^{\mathrm{i}x}}{x^2 - 2x + 5}\,\mathrm{d}x = \frac{\pi}{2\mathrm{e}^2}(\cos1 + \mathrm{i}\sin1),
$$

so the two integrals equal $\frac{\pi\cos1}{2\mathrm{e}^2}$ and $\frac{\pi\sin1}{2\mathrm{e}^2}$.

**Example 7.3.2** $\int_0^\infty\frac{x\sin x}{x^2 + 4}\,\mathrm{d}x$. Here $\deg Q = \deg P + 1$, so Jordan's lemma is essential. The residue of $\frac{z\mathrm{e}^{\mathrm{i}z}}{z^2 + 4}$ at $2\mathrm{i}$ is $\frac{2\mathrm{i}\,\mathrm{e}^{-2}}{4\mathrm{i}} = \frac{\mathrm{e}^{-2}}{2}$, so $\int_{-\infty}^\infty\frac{x\mathrm{e}^{\mathrm{i}x}}{x^2 + 4}\,\mathrm{d}x = \pi\mathrm{i}\,\mathrm{e}^{-2}$. Taking imaginary parts and using that the integrand is even, $\int_0^\infty\frac{x\sin x}{x^2 + 4}\,\mathrm{d}x = \frac{\pi}{2\mathrm{e}^2}$.

### 7.3.3. Fourier and Laplace Transforms

With the convention $\hat f(\xi) = \int_{\mathbb{R}}f(x)\,\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x$ of [2.5.6](/2.5.6), Theorem 7.3.1 computes the Fourier transforms of rational functions. The sign of $\xi$ decides in which half-plane the contour must be closed.

**Example 7.3.3** Let $b > 0$ and $f(x) = \frac{1}{x^2 + b^2}$. For $\xi < 0$ the factor $\mathrm{e}^{-\mathrm{i}\xi z}$ decays in the upper half-plane, and the residue at $\mathrm{i}b$ gives $\hat f(\xi) = 2\pi\mathrm{i}\cdot\frac{\mathrm{e}^{\xi b}}{2\mathrm{i}b} = \frac\pi b\mathrm{e}^{\xi b}$. For $\xi > 0$ we close in the lower half-plane: $\hat f(\xi) = -2\pi\mathrm{i}\cdot\frac{\mathrm{e}^{-\xi b}}{-2\mathrm{i}b} = \frac\pi b\mathrm{e}^{-\xi b}$. Together, and by continuity at $\xi = 0$,

$$
\hat f(\xi) = \frac{\pi}{b}\,\mathrm{e}^{-b\lvert\xi\rvert}.
$$

This pair (a Lorentzian and a two-sided exponential) reappears in [2.5.6](/2.5.6) and in the Poisson kernel of the half-plane.

The inverse Laplace transform of $F(s)$ is given by the Bromwich integral

$$
f(t) = \frac{1}{2\pi\mathrm{i}}\int_{c - \mathrm{i}\infty}^{c + \mathrm{i}\infty}F(s)\,\mathrm{e}^{st}\,\mathrm{d}s, \qquad t > 0,
$$

along a vertical line $\operatorname{Re}s = c$ to the right of all singularities of $F$ (derived in [2.5.6](/2.5.6)). If $F$ is rational with $\deg Q > \deg P$, the line can be closed by a large half-circle to the left; for $t > 0$ the factor $\mathrm{e}^{st}$ decays there, the version of Jordan's lemma for left half-circles kills the arc, and

$$
f(t) = \sum_k\operatorname{Res}\left(F(s)\,\mathrm{e}^{st}, s_k\right), \tag{7.4}
$$

the sum running over all poles $s_k$ of $F$.

**Example 7.3.4** 1. $F(s) = \frac{1}{s^2 + 1}$: the residues of $\frac{\mathrm{e}^{st}}{s^2 + 1}$ at $\pm\mathrm{i}$ are $\pm\frac{\mathrm{e}^{\pm\mathrm{i}t}}{2\mathrm{i}}$, whose sum is $\sin t$.
2. $F(s) = \frac{1}{s(s+1)^2}$: the residue at $0$ is $1$, and at the double pole $-1$ it is $\frac{\mathrm{d}}{\mathrm{d}s}\frac{\mathrm{e}^{st}}{s}\big|_{s=-1} = \frac{(st - 1)\mathrm{e}^{st}}{s^2}\big|_{s=-1} = -(1 + t)\mathrm{e}^{-t}$. Hence $f(t) = 1 - (1 + t)\mathrm{e}^{-t}$. A pole of order $m$ produces terms $t^k\mathrm{e}^{s_kt}$ with $k < m$, exactly the resonance terms familiar from linear differential equations with constant coefficients.

## 7.4. Poles on the Real Axis and Principal Values

If the integrand has a simple pole on the real axis, the integral diverges in the ordinary sense, but a symmetric limit may exist.

**Definition 7.4.1** Let $f$ be continuous on $\mathbb{R}$ except at $x_0$. The **Cauchy principal value** of its integral is

$$
\operatorname{PV}\int_{-\infty}^{\infty}f(x)\,\mathrm{d}x = \lim_{\substack{\varepsilon\to0^+\\R\to\infty}}\left(\int_{-R}^{x_0 - \varepsilon} + \int_{x_0 + \varepsilon}^{R}\right)f(x)\,\mathrm{d}x,
$$

when the limit exists (with the obvious modification for several points $x_0$).

For example, $\operatorname{PV}\int_{-1}^{1}\frac{\mathrm{d}x}{x} = 0$ although $\int_0^1\frac{\mathrm{d}x}{x}$ diverges. To compute principal values we indent the contour by a small semicircle around the pole (panel (b) of the figure below), whose contribution is computed by the following lemma.

**Lemma 7.4.1 (Small-Arc Lemma)** Let $z_0$ be a simple pole of $f$, and let $C_\varepsilon$ be the arc $z_0 + \varepsilon\mathrm{e}^{\mathrm{i}\theta}$, $\theta_1 \le \theta \le \theta_1 + \alpha$, traversed counterclockwise. Then

$$
\lim_{\varepsilon\to0}\int_{C_\varepsilon}f(z)\,\mathrm{d}z = \mathrm{i}\alpha\operatorname{Res}(f, z_0).
$$

**Proof** Write $f = \frac{c_{-1}}{z - z_0} + g(z)$ with $g$ analytic, hence bounded, near $z_0$. Then $\int_{C_\varepsilon}\frac{c_{-1}\,\mathrm{d}z}{z - z_0} = c_{-1}\int_{\theta_1}^{\theta_1+\alpha}\mathrm{i}\,\mathrm{d}\theta = \mathrm{i}\alpha c_{-1}$, while $\left\lvert\int_{C_\varepsilon}g\,\mathrm{d}z\right\rvert \le \alpha\varepsilon\max\lvert g\rvert \to 0$. $\square$

A full circle ($\alpha = 2\pi$) recovers the definition of the residue; a semicircle gives half of it. For a pole of order $\ge 2$ the small arc does not have a finite limit in general, and the principal value does not exist.

**Theorem 7.4.1** Let $R = \frac PQ$ with $\deg Q \ge \deg P + 1$, and suppose all real poles $x_j$ of $R$ are simple. For $a > 0$,

$$
\operatorname{PV}\int_{-\infty}^{\infty}R(x)\,\mathrm{e}^{\mathrm{i}ax}\,\mathrm{d}x = 2\pi\mathrm{i}\sum_{\operatorname{Im}z_k > 0}\operatorname{Res}\left(R\,\mathrm{e}^{\mathrm{i}az}, z_k\right) + \pi\mathrm{i}\sum_j\operatorname{Res}\left(R\,\mathrm{e}^{\mathrm{i}az}, x_j\right).
$$

**Proof** Use the indented contour: along $[-R, R]$ with small upper semicircles of radius $\varepsilon$ around each $x_j$, closed by the upper semicircle $C_R$. The residue theorem gives $2\pi\mathrm{i}$ times the residues in the upper half-plane. Each small semicircle is traversed clockwise ($\alpha = -\pi$), so by Lemma 7.4.1 it tends to $-\pi\mathrm{i}\operatorname{Res}(\cdot, x_j)$; the big arc vanishes by Jordan's lemma. Moving the small-arc contributions to the right side gives the formula. $\square$

**Example 7.4.1** The **Dirichlet integral**: $\int_0^\infty\frac{\sin x}{x}\,\mathrm{d}x = \frac\pi2$. The function $\frac{\mathrm{e}^{\mathrm{i}z}}{z}$ has only a simple pole at $0$, with residue $1$, so $\operatorname{PV}\int_{-\infty}^\infty\frac{\mathrm{e}^{\mathrm{i}x}}{x}\,\mathrm{d}x = \pi\mathrm{i}$. The imaginary part is $\int_{-\infty}^{\infty}\frac{\sin x}{x}\,\mathrm{d}x = \pi$; no principal value is needed here, because $\frac{\sin x}{x}$ is continuous at $0$. (The real part says $\operatorname{PV}\int\frac{\cos x}{x}\,\mathrm{d}x = 0$, which is clear by oddness.)

**Example 7.4.2** $\int_0^\infty\frac{1 - \cos x}{x^2}\,\mathrm{d}x = \frac\pi2$. Consider $f(z) = \frac{1 - \mathrm{e}^{\mathrm{i}z}}{z^2}$. Since $1 - \mathrm{e}^{\mathrm{i}z} = -\mathrm{i}z + \frac{z^2}{2} + \cdots$, $f$ has a simple pole at $0$ with residue $-\mathrm{i}$; on large semicircles $\lvert f\rvert \le 2/R^2$. The argument of Theorem 7.4.1 gives $\operatorname{PV}\int_{-\infty}^\infty f(x)\,\mathrm{d}x = \pi\mathrm{i}\cdot(-\mathrm{i}) = \pi$. Taking real parts, $\int_{-\infty}^\infty\frac{1 - \cos x}{x^2}\,\mathrm{d}x = \pi$, and the integrand is even.

![Three standard contours. (a) The segment [-R, R] closed by the upper semicircle C_R; only the poles in the upper half-plane (red) contribute, and the arc vanishes by the large-arc lemma or Jordan's lemma. (b) The same contour indented by a small semicircle C_ε around a simple pole on the real axis. (c) The keyhole contour for integrands with a branch cut along the positive real axis: the two edges of the cut carry different values of z^α or log z](./plots/contours.py)

## 7.5. Integrals Involving Multivalued Functions

### 7.5.1. Powers: the Keyhole Contour

For $\int_0^\infty x^{\alpha - 1}R(x)\,\mathrm{d}x$ with non-integer $\alpha$, we use the branch of $z^{\alpha - 1} = \mathrm{e}^{(\alpha - 1)\log z}$ with $0 < \arg z < 2\pi$, which is analytic in $\mathbb{C}$ minus the **branch cut** $[0, +\infty)$ ([2.3.3](/2.3.3)). The keyhole contour (panel (c) above) runs along the upper edge of the cut from $\varepsilon$ to $R$, around the large circle, back along the lower edge, and around the small circle clockwise. On the upper edge $z^{\alpha - 1} = x^{\alpha - 1}$, while on the lower edge $\arg z = 2\pi$ and $z^{\alpha - 1} = x^{\alpha - 1}\mathrm{e}^{2\pi\mathrm{i}(\alpha - 1)} = x^{\alpha - 1}\mathrm{e}^{2\pi\mathrm{i}\alpha}$. The two edges therefore do not cancel; they contribute $\left(1 - \mathrm{e}^{2\pi\mathrm{i}\alpha}\right)\int_\varepsilon^Rx^{\alpha - 1}R(x)\,\mathrm{d}x$.

**Example 7.5.1** For $0 < \alpha < 1$,

$$
\int_0^\infty\frac{x^{\alpha - 1}}{1 + x}\,\mathrm{d}x = \frac{\pi}{\sin\pi\alpha}. \tag{7.5}
$$

On the large circle $\lvert zf(z)\rvert \approx R^{\alpha - 1} \to 0$, and on the small circle $\lvert zf(z)\rvert \approx \varepsilon^\alpha \to 0$, so both circles contribute nothing in the limit (Lemma 7.2.1 and its analogue for $\varepsilon \to 0$). The only pole is $-1 = \mathrm{e}^{\mathrm{i}\pi}$ (with the chosen branch), and the residue there is $\mathrm{e}^{\mathrm{i}\pi(\alpha - 1)} = -\mathrm{e}^{\mathrm{i}\pi\alpha}$. Hence

$$
\left(1 - \mathrm{e}^{2\pi\mathrm{i}\alpha}\right)I = -2\pi\mathrm{i}\,\mathrm{e}^{\mathrm{i}\pi\alpha}, \qquad I = \frac{2\pi\mathrm{i}}{\mathrm{e}^{\mathrm{i}\pi\alpha} - \mathrm{e}^{-\mathrm{i}\pi\alpha}} = \frac{\pi}{\sin\pi\alpha}.
$$

With $x = t^n$ and $\alpha = \frac1n$, Eq. (7.5) becomes the formula of Example 7.2.2. In terms of the Gamma function, Eq. (7.5) is the reflection formula $\Gamma(\alpha)\Gamma(1 - \alpha) = \frac{\pi}{\sin\pi\alpha}$.

The same argument gives, for a rational function $R$ without poles on $[0, \infty)$ and $\lvert x^\alpha R(x)\rvert \to 0$ at both $0$ and $\infty$,

$$
\int_0^\infty x^{\alpha - 1}R(x)\,\mathrm{d}x = \frac{2\pi\mathrm{i}}{1 - \mathrm{e}^{2\pi\mathrm{i}\alpha}}\sum_k\operatorname{Res}\left(z^{\alpha - 1}R(z), z_k\right),
$$

the sum running over all poles of $R$, with $0 < \arg z_k < 2\pi$.

### 7.5.2. Logarithms

The keyhole contour can also integrate rational functions over $[0, \infty)$ that have no symmetry, by inserting a logarithm. With $\log z$ the branch with $0 < \arg z < 2\pi$, the upper and lower edges carry $\ln x$ and $\ln x + 2\pi\mathrm{i}$. For $\int_0^\infty R(x)\,\mathrm{d}x$ the logarithmic terms cancel, and the $2\pi\mathrm{i}$ term survives:

$$
\int_0^\infty R(x)\,\mathrm{d}x = -\sum_k\operatorname{Res}\left(R(z)\log z, z_k\right), \tag{7.6}
$$

valid when $\deg Q \ge \deg P + 2$ and $R$ has no poles on $[0, \infty)$ (the circles vanish since $\lvert zR(z)\log z\rvert \to 0$ at $0$ and at $\infty$).

**Example 7.5.2** $\int_0^\infty\frac{\mathrm{d}x}{1 + x^3}$. The poles $z_k = \mathrm{e}^{\mathrm{i}\pi/3}, \mathrm{e}^{\mathrm{i}\pi}, \mathrm{e}^{5\mathrm{i}\pi/3}$ have $\log z_k = \frac{\mathrm{i}\pi}{3}, \mathrm{i}\pi, \frac{5\mathrm{i}\pi}{3}$ on the chosen branch, and $\operatorname{Res}\left(\frac{\log z}{1 + z^3}, z_k\right) = \frac{\log z_k}{3z_k^2} = -\frac{z_k\log z_k}{3}$. By Eq. (7.6),

$$
I = \frac{1}{3}\sum_kz_k\log z_k = \frac{\mathrm{i}\pi}{9}\left(\mathrm{e}^{\mathrm{i}\pi/3} - 3 + 5\,\mathrm{e}^{-\mathrm{i}\pi/3}\right) = \frac{\mathrm{i}\pi}{9}\left(-2\sqrt3\,\mathrm{i}\right) = \frac{2\pi}{3\sqrt3},
$$

in agreement with Example 7.2.2.

## 7.6. Summation of Series

The function $\pi\cot\pi z$ has simple poles at every integer $n$, with residue $\frac{\pi\cos\pi n}{\pi\cos\pi n} = 1$. Multiplying by $f(z)$ therefore produces residues $f(n)$ at the integers, and a contour integral can capture the whole series.

**Theorem 7.6.1** Let $f = \frac PQ$ be rational with $\deg Q \ge \deg P + 2$, and suppose no pole $z_1, \dots, z_m$ of $f$ is an integer. Then

$$
\sum_{n=-\infty}^{\infty}f(n) = -\sum_{k=1}^m\operatorname{Res}\left(\pi\cot(\pi z)f(z), z_k\right).
$$

**Proof** (Sketch.) Let $C_N$ be the boundary of the square with vertices $\left(N + \frac12\right)(\pm1 \pm \mathrm{i})$. One checks that $\lvert\cot\pi z\rvert$ is bounded on all $C_N$ by a constant independent of $N$ (on the vertical sides $\lvert\cot\pi z\rvert = \lvert\tanh\pi y\rvert < 1$, on the horizontal sides $\lvert\cot\pi z\rvert \le \coth\frac{\pi}{2}$). Since $\lvert f\rvert = O(N^{-2})$ on $C_N$ and the length of $C_N$ is $O(N)$, the integral of $\pi\cot(\pi z)f(z)$ over $C_N$ tends to $0$. By the residue theorem, the sum of all residues inside $C_N$, namely $\sum_{\lvert n\rvert\le N}f(n)$ plus the residues at the $z_k$, tends to $0$. $\square$

**Example 7.6.1** For $a > 0$, $f(z) = \frac{1}{z^2 + a^2}$ has simple poles $\pm\mathrm{i}a$. Using $\cot(\mathrm{i}y) = -\mathrm{i}\coth y$, both residues of $\frac{\pi\cot\pi z}{z^2 + a^2}$ equal $-\frac{\pi\coth\pi a}{2a}$. Hence

$$
\sum_{n=-\infty}^{\infty}\frac{1}{n^2 + a^2} = \frac{\pi}{a}\coth\pi a, \qquad \sum_{n=1}^\infty\frac{1}{n^2 + a^2} = \frac{\pi a\coth\pi a - 1}{2a^2}.
$$

Letting $a \to 0$ and using $\pi a\coth\pi a = 1 + \frac{\pi^2a^2}{3} + O(a^4)$ gives $\sum_{n\ge1}\frac1{n^2} = \frac{\pi^2}{6}$. Replacing $\pi\cot\pi z$ by $\frac{\pi}{\sin\pi z}$, whose residues at $n$ are $(-1)^n$, sums alternating series in the same way.

## 7.7. The Argument Principle and Rouché's Theorem

### 7.7.1. Counting Zeros and Poles

If $z_0$ is a zero of order $m$ of $f$, then $f = (z - z_0)^m\varphi$ with $\varphi(z_0) \ne 0$, and

$$
\frac{f'(z)}{f(z)} = \frac{m}{z - z_0} + \frac{\varphi'(z)}{\varphi(z)},
$$

so the logarithmic derivative $\frac{f'}{f}$ has a simple pole at $z_0$ with residue $m$. At a pole of order $m$, $f = (z - z_0)^{-m}\varphi$, and the residue of $\frac{f'}{f}$ is $-m$. The residue theorem gives:

**Theorem 7.7.1 (Argument Principle)** Let $C$ be a positively oriented, piecewise smooth simple closed curve, and let $f$ be analytic inside and on $C$ except for finitely many poles inside $C$, with no zeros or poles on $C$. If $N$ and $P$ denote the numbers of zeros and poles of $f$ inside $C$, each counted with its order, then

$$
\frac{1}{2\pi\mathrm{i}}\oint_C\frac{f'(z)}{f(z)}\,\mathrm{d}z = N - P. \tag{7.7}
$$

The name comes from the interpretation of the left side. Locally $\frac{f'}{f} = (\log f)'$, so the integral measures the total change of $\log f(z) = \ln\lvert f(z)\rvert + \mathrm{i}\arg f(z)$ as $z$ goes once around $C$. The modulus returns to its initial value, so

$$
N - P = \frac{1}{2\pi}\Delta_C\arg f(z),
$$

the number of times the image curve $f(C)$ winds around the origin. Counting zeros is thus reduced to watching how the image curve turns, a method that also underlies the Nyquist stability criterion in control theory.

### 7.7.2. Rouché's Theorem

**Theorem 7.7.2 (Rouché's Theorem)** Let $f$ and $g$ be analytic inside and on a simple closed curve $C$, with $\lvert g(z)\rvert < \lvert f(z)\rvert$ on $C$. Then $f$ and $f + g$ have the same number of zeros inside $C$, counted with order.

**Proof** For $t \in [0, 1]$, $\lvert f + tg\rvert \ge \lvert f\rvert - \lvert g\rvert > 0$ on $C$, so $f + tg$ has no zeros on $C$, and by Eq. (7.7) the number of its zeros inside $C$ is

$$
N(t) = \frac{1}{2\pi\mathrm{i}}\oint_C\frac{f'(z) + tg'(z)}{f(z) + tg(z)}\,\mathrm{d}z.
$$

The integrand is continuous in $(t, z) \in [0, 1] \times C$, so $N(t)$ is continuous in $t$. Being integer-valued, $N(t)$ is constant, and $N(0) = N(1)$. $\square$

Intuitively, $\lvert g\rvert < \lvert f\rvert$ means that the perturbation $g$ cannot drag the image curve of $f + g$ across the origin, so the winding number does not change. To use the theorem, split the function into a dominant term $f$ whose zeros are known and a remainder $g$ that is smaller on $C$.

**Example 7.7.1** How many zeros does $p(z) = z^7 - 5z^3 + z - 2$ have in $\lvert z\rvert < 1$ and in $1 < \lvert z\rvert < 2$?

- On $\lvert z\rvert = 1$ take $f = -5z^3$ and $g = z^7 + z - 2$: $\lvert g\rvert \le 1 + 1 + 2 = 4 < 5 = \lvert f\rvert$. So $p$ has as many zeros in $\lvert z\rvert < 1$ as $-5z^3$, namely $3$.
- On $\lvert z\rvert = 2$ take $f = z^7$: $\lvert -5z^3 + z - 2\rvert \le 40 + 2 + 2 = 44 < 128$. So all $7$ zeros lie in $\lvert z\rvert < 2$.
- On $\lvert z\rvert = 1$ itself $\lvert p\rvert \ge 5 - 4 > 0$. Hence exactly $7 - 3 = 4$ zeros lie in the annulus $1 < \lvert z\rvert < 2$.

![The argument principle for p(z) = z^7 - 5z^3 + z - 2. Left: domain coloring of p with its seven zeros; three lie inside |z| = 1 (white dashed) and all seven inside |z| = 2 (dark dashed). Middle and right: the image curves p(|z| = 1) and p(|z| = 2) wind 3 and 7 times around the origin](./plots/argument-principle.py)

**Example 7.7.2** 1. Rouché's theorem gives a short proof of the **fundamental theorem of algebra**. For $p(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$ and $R > \max\left(1, \sum\lvert a_k\rvert\right)$, on $\lvert z\rvert = R$ we have $\lvert a_{n-1}z^{n-1} + \cdots + a_0\rvert \le R^{n-1}\sum\lvert a_k\rvert < R^n = \lvert z^n\rvert$. So $p$ has exactly $n$ zeros in $\lvert z\rvert < R$, as $z^n$ does.
2. If $\lvert a\rvert > \mathrm{e}$ and $n \ge 1$, the equation $\mathrm{e}^z = az^n$ has exactly $n$ roots in $\lvert z\rvert < 1$: on $\lvert z\rvert = 1$, $\lvert\mathrm{e}^z\rvert = \mathrm{e}^{\operatorname{Re}z} \le \mathrm{e} < \lvert az^n\rvert$, so $az^n - \mathrm{e}^z$ has as many zeros as $az^n$.

### 7.7.3. Local Behavior of Analytic Maps

Applied to $f(z) - w$ for $w$ near a value $w_0 = f(z_0)$, Rouché's theorem describes how an analytic function maps a neighborhood of a point.

**Theorem 7.7.3** Let $f$ be analytic at $z_0$, $w_0 = f(z_0)$, and suppose $z_0$ is a zero of order $m$ of $f - w_0$. Then there are $\rho > 0$ and $\delta > 0$ such that for every $w$ with $0 < \lvert w - w_0\rvert < \delta$, the equation $f(z) = w$ has exactly $m$ solutions in $\lvert z - z_0\rvert < \rho$, all of them simple. In particular, if $f'(z_0) \ne 0$, then $f$ is injective near $z_0$.

**Proof** Zeros of $f - w_0$ and of $f'$ are isolated (Theorem 5.4.2; $f'$ is not identically zero since $m$ is finite), so we can choose $\rho$ such that $f - w_0$ and $f'$ have no zeros in $0 < \lvert z - z_0\rvert \le \rho$. Let $\delta = \min_{\lvert z - z_0\rvert = \rho}\lvert f(z) - w_0\rvert > 0$. For $\lvert w - w_0\rvert < \delta$, apply Rouché's theorem with $F = f - w_0$ and $G = w_0 - w$: $f - w$ has $m$ zeros in the disk. For $w \ne w_0$ none of them is $z_0$, and at each of them $f' \ne 0$, so they are simple and hence distinct. $\square$

**Theorem 7.7.4 (Open Mapping Theorem)** A nonconstant analytic function on a domain maps open sets to open sets.

**Proof** By Theorem 7.7.3, for every $z_0$ the image of each small disk around $z_0$ contains a disk around $f(z_0)$. $\square$

The open mapping theorem gives another proof of the **maximum modulus principle** ([2.3.4](/2.3.4)): if $\lvert f\rvert$ had a local maximum at $z_0$, the image of a neighborhood of $z_0$ would contain a disk around $f(z_0)$, and thus points of larger modulus. Theorem 7.7.3 also says that near a point where $f'(z_0) = 0$ (a zero of order $m \ge 2$ of $f - w_0$), $f$ is $m$-to-one; this is why conformality breaks down exactly at the critical points of $f$ ([2.3.8](/2.3.8)).

## Summary

| Integral | Contour | Result |
|---|---|---|
| $\int_0^{2\pi}R(\cos\theta, \sin\theta)\,\mathrm{d}\theta$ | Unit circle, $z = \mathrm{e}^{\mathrm{i}\theta}$ | $2\pi\mathrm{i}\sum_{\lvert z_k\rvert<1}\operatorname{Res}$ |
| $\int_{-\infty}^\infty R(x)\,\mathrm{d}x$, $\deg Q \ge \deg P + 2$ | Upper semicircle; large-arc lemma | $2\pi\mathrm{i}\sum_{\operatorname{Im}z_k>0}\operatorname{Res}$ |
| $\int_{-\infty}^\infty R(x)\mathrm{e}^{\mathrm{i}ax}\,\mathrm{d}x$, $a > 0$, $\deg Q \ge \deg P + 1$ | Upper semicircle; Jordan's lemma | $2\pi\mathrm{i}\sum_{\operatorname{Im}z_k>0}\operatorname{Res}(R\mathrm{e}^{\mathrm{i}az})$ |
| Simple poles on $\mathbb{R}$ | Indentation; small-arc lemma | Principal value; real poles count with $\pi\mathrm{i}$ |
| $\int_0^\infty x^{\alpha-1}R(x)\,\mathrm{d}x$, $\int_0^\infty R(x)\,\mathrm{d}x$ | Keyhole around the cut $[0, \infty)$ | Edges differ by $\mathrm{e}^{2\pi\mathrm{i}\alpha}$ or $2\pi\mathrm{i}$ |
| Inverse Laplace transform | Bromwich line closed to the left | $\sum\operatorname{Res}(F(s)\mathrm{e}^{st})$ |
| $\sum_nf(n)$ | Squares $C_N$ | $-\sum\operatorname{Res}(\pi\cot(\pi z)f)$ at the poles of $f$ |
| Zeros of $f$ | Argument principle, Rouché | $N - P = \frac{1}{2\pi}\Delta_C\arg f$; dominant term decides |
