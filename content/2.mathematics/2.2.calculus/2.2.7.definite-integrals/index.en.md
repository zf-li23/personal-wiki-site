---
title: The Definite Integral
source_hash: 104919a26330
---

The indefinite integral of [Chapter 6](/2.2.6) is the inverse of differentiation; the definite integral of this chapter comes from entirely different problems: the area under a curve, the mass of a rod of variable density, the work done by a variable force. All of them can be computed in four steps (partition, approximate, sum, take the limit), and abstracting this procedure gives the Riemann integral. We first give the definition and conditions for integrability (7.1) and list the properties of the integral (7.2). We then prove the fundamental theorem of calculus (7.3): the integral of a continuous function with variable upper limit is an antiderivative of it, so definite integrals can be computed with **antiderivatives**, and differential and integral calculus become linked. Section 7.4 carries substitution and integration by parts over to definite integrals, and Sections 7.5 and 7.6 present geometric and physical applications (area, arc length, curvature, solids of revolution, and the method of differential elements common in physics). Section 7.7 extends the integral to unbounded intervals and unbounded functions; the comparison tests and the notion of absolute convergence established there reappear almost verbatim for series in [Chapter 8](/2.2.8). The gamma and beta functions are also defined there, and the gamma and beta distributions of [probability theory](/3.1) are built on them.

## 7.1. Definition and Existence of the Definite Integral

### 7.1.1. Motivating Examples

The area under a curve: let $f \in C[a,b]$ with $f(x) \ge 0$, and let $S$ be the area of the region bounded by the curve $y = f(x)$, the lines $x = a$ and $x = b$, and the $x$-axis.

1. Partition: insert points $a = x_0 < x_1 < \cdots < x_n = b$; the lines $x = x_i$ divide the region into $n$ thin strips;
2. Approximate: choose any $\xi_i$ in $[x_{i-1}, x_i]$; the area of the $i$-th strip is $S_i \approx f(\xi_i)\Delta x_i$, where $\Delta x_i = x_i - x_{i-1}$;
3. Sum: $S \approx \sum_{i=1}^n f(\xi_i)\Delta x_i$;
4. Take the limit: with $\lambda = \max_{1\le i\le n}\Delta x_i$, $S = \lim_{\lambda\to 0}\sum_{i=1}^n f(\xi_i)\Delta x_i$.

The mass of a rod: for a thin rod occupying $[a,b]$ with linear density $\rho(x) \in C[a,b]$, the same four steps give the mass $m = \lim_{\lambda\to0}\sum_{i=1}^n \rho(\xi_i)\Delta x_i$.

The two problems have exactly the same mathematical structure: a function defined on a bounded closed interval yields a number through "partition, approximate, sum, take the limit".

### 7.1.2. Definition of the Riemann Integral

**Definition 7.1.1 (Definite Integral)** Let $f$ be a **bounded function** on a bounded closed interval $[a,b]$. For any partition $T\colon a = x_0 < x_1 < \cdots < x_n = b$ and any choice of points $\xi_i \in [x_{i-1}, x_i]$, form the sum

$$
\sum_{i=1}^n f(\xi_i)\Delta x_i, \qquad \Delta x_i = x_i - x_{i-1},
$$
called a **Riemann sum** of $f$. Let $\lambda = \max_i \Delta x_i$. If the limit $\lim_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i$ exists (independently of the partition and of the choice of the $\xi_i$), then $f$ is said to be (Riemann) integrable on $[a,b]$, written $f \in \mathcal{R}[a,b]$, and the limit is called the **definite integral** (Riemann integral) of $f$ over $[a,b]$, denoted by $\int_a^b f(x)\,\mathrm{d}x$.

Here $a$ and $b$ are called the lower and upper limits of integration, $f(x)$ is the integrand, and $\mathrm{d}x$ is the length element. Some remarks:

- The definite integral is a special kind of limit: the limiting process is determined jointly by the partition and the choice of points, but the limiting value is independent of both. The condition "$\lambda \to 0$" is stronger than "$n \to \infty$": if $n$ is large but some subinterval does not shrink, the sum need not be close to the integral.
- The value of the integral depends only on $f$ and $[a,b]$, not on the name of the variable of integration: $\int_a^b f(x)\,\mathrm{d}x = \int_a^b f(t)\,\mathrm{d}t$.
- Constant functions are integrable: $\int_a^b c\,\mathrm{d}x = c(b-a)$.
- Geometric meaning: if $f \in C[a,b]$ and $f \ge 0$, then $\int_a^b f(x)\,\mathrm{d}x$ is the area under the curve described above; in general it is the area above the $x$-axis minus the area below it. For example, for $0 < a < b$, $\int_a^b x\,\mathrm{d}x = \frac12(a+b)(b-a) = \frac12(b^2 - a^2)$ (the area of a trapezoid).

### 7.1.3. Conditions for Integrability

Deciding integrability directly from the definition is inconvenient, since all partitions and all choices of points must be controlled at once. The remedy is to squeeze the Riemann sums between the suprema and infima of $f$ on the subintervals.

**Definition 7.1.2 (Darboux Sums)** Let $f$ be a bounded function on $[a,b]$ and $T\colon a = x_0 < \cdots < x_n = b$ a partition. Set

$$
M_i = \sup_{x\in[x_{i-1},x_i]} f(x), \qquad m_i = \inf_{x\in[x_{i-1},x_i]} f(x).
$$
The number $\omega_i = M_i - m_i$ is called the **oscillation** of $f$ on $[x_{i-1}, x_i]$, and $S(T) = \sum_i M_i\Delta x_i$ and $s(T) = \sum_i m_i\Delta x_i$ are called the upper and lower Darboux sums of $f$ with respect to $T$.

For every choice of points, $s(T) \le \sum_i f(\xi_i)\Delta x_i \le S(T)$; moreover, by letting $\xi_i$ range over $[x_{i-1},x_i]$, the Riemann sums come arbitrarily close to $s(T)$ and to $S(T)$. Hence the Riemann sums have a limit if and only if the difference between the upper and lower sums,

$$
S(T) - s(T) = \sum_{i=1}^n \omega_i\Delta x_i,
$$
tends to $0$ as $\lambda \to 0$. This is the following criterion (we omit the details of the proof).

**Theorem 7.1.1** Let $f$ be bounded on the bounded closed interval $[a,b]$. Then

$$
f \in \mathcal{R}[a,b] \iff \lim_{\lambda\to0}\sum_{i=1}^n \omega_i\Delta x_i = 0.
$$

An equivalent formulation (due to Darboux) is: for every $\varepsilon > 0$ there exists a partition $T$ with $S(T) - s(T) < \varepsilon$. Note the order of quantifiers: "for each $\varepsilon$ there is a partition", not "there is a partition for which the limit is zero".

![Upper and lower Darboux sums of x^2 on [0,1]: with n equal subintervals, S - s = 1/n, and both tend to 1/3](./plots/darboux-sums.py)

**Example 7.1.1** The **Dirichlet function** $D(x) = \boldsymbol{1}_{\mathbb{Q}}(x)$ (equal to $1$ at rational points and $0$ at irrational points) is not integrable on any interval $[a,b]$.

**Proof** Both the rationals and the irrationals are dense in the reals, so for every partition we have $M_i = 1$, $m_i = 0$ and $\omega_i = 1$ on each subinterval, whence $\sum_i\omega_i\Delta x_i = b - a \not\to 0$. By Theorem 7.1.1, $D$ is not integrable. $\square$

**Theorem 7.1.2** Let $f$ be bounded on the bounded closed interval $[a,b]$.

1. If $f \in C[a,b]$, then $f \in \mathcal{R}[a,b]$;
2. If $f$ is monotone on $[a,b]$, then $f \in \mathcal{R}[a,b]$;
3. If $f$ has only finitely many discontinuities on $[a,b]$, then $f \in \mathcal{R}[a,b]$.

**Proof** We prove only 1 and 2.

1. By the **Heine–Cantor theorem** we have **uniform continuity** of $f$ on $[a,b]$: for $\varepsilon > 0$ there is $\delta > 0$ such that $|u - v| < \delta$ implies $|f(u) - f(v)| < \varepsilon/(b-a)$. Hence as soon as $\lambda < \delta$, we have $\omega_i \le \varepsilon/(b-a)$ (a continuous function attains its maximum and minimum on a closed interval) and $\sum_i\omega_i\Delta x_i \le \varepsilon$. By Theorem 7.1.1, $f$ is integrable.
2. Without loss of generality let $f$ be increasing with $f(b) > f(a)$. Then $\omega_i = f(x_i) - f(x_{i-1})$, and for $\lambda < \varepsilon/(f(b) - f(a))$,

$$
\sum_{i=1}^n\omega_i\Delta x_i \le \lambda\sum_{i=1}^n\bigl(f(x_i) - f(x_{i-1})\bigr) = \lambda\bigl(f(b) - f(a)\bigr) < \varepsilon. \qquad \square
$$

A monotone function can have infinitely many discontinuities (for example, a step function that jumps at the points $x = 1/n$), so case 2 is not contained in case 3.

## 7.2. Properties of the Definite Integral

Throughout, let $f, g \in \mathcal{R}[a,b]$.

**Property 7.2.1 (Linearity)** For constants $\alpha, \beta$, we have $\alpha f + \beta g \in \mathcal{R}[a,b]$ and $\int_a^b(\alpha f + \beta g)\,\mathrm{d}x = \alpha\int_a^b f\,\mathrm{d}x + \beta\int_a^b g\,\mathrm{d}x$.

**Property 7.2.2 (Additivity over Intervals)** If $c \in (a,b)$, then $f \in \mathcal{R}[a,c]$, $f \in \mathcal{R}[c,b]$, and $\int_a^b f\,\mathrm{d}x = \int_a^c f\,\mathrm{d}x + \int_c^b f\,\mathrm{d}x$.

**Property 7.2.3 (Orientation)** By convention, $\int_b^a f\,\mathrm{d}x = -\int_a^b f\,\mathrm{d}x$ and $\int_a^a f\,\mathrm{d}x = 0$. With this convention, Property 7.2.2 holds for $a, b, c$ in any order (provided the integrals involved exist).

**Property 7.2.4 (Positivity)** If $f(x) \ge 0$ for $x \in [a,b]$, then $\int_a^b f\,\mathrm{d}x \ge 0$.

**Property 7.2.5 (Monotonicity)** If $f(x) \le g(x)$ for $x \in [a,b]$, then $\int_a^b f\,\mathrm{d}x \le \int_a^b g\,\mathrm{d}x$.

**Property 7.2.6 (Integrability of the Absolute Value)** $|f| \in \mathcal{R}[a,b]$, and $\left|\int_a^b f\,\mathrm{d}x\right| \le \int_a^b |f|\,\mathrm{d}x$.

The converse fails: the function $f(x) = 1$ for rational $x$ and $f(x) = -1$ for irrational $x$ is not integrable on $[0,1]$ (its oscillation on every subinterval is $2$), but $|f| \equiv 1$ is integrable.

**Property 7.2.7 (Estimate)** If $m \le f(x) \le M$ for $x \in [a,b]$, then $m(b-a) \le \int_a^b f\,\mathrm{d}x \le M(b-a)$.

**Property 7.2.8 (Mean Value Theorem for Integrals)** If $f \in C[a,b]$, then there exists $\xi \in [a,b]$ such that $\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b-a)$.

**Proof** Let $m$ and $M$ be the minimum and maximum of $f$ on $[a,b]$ (**extreme value theorem**). By Property 7.2.7, $m \le \frac{1}{b-a}\int_a^b f\,\mathrm{d}x \le M$. By the **intermediate value theorem** for continuous functions, there is $\xi \in [a,b]$ at which $f(\xi)$ equals this average. $\square$

The quantity $\frac{1}{b-a}\int_a^b f\,\mathrm{d}x$ is called the average value of $f$ on $[a,b]$. Geometrically, the area under the curve equals the area of a rectangle of height $f(\xi)$.

**Property 7.2.9 (Integrability of Products)** $fg \in \mathcal{R}[a,b]$.

**Proof** First assume $0 \le f \le M$ and $0 \le g \le N$. Let $\omega_i, \omega_i', \omega_i''$ denote the oscillations of $f, g, fg$ on $[x_{i-1}, x_i]$. For any $u, v$ in this subinterval,

$$
|f(u)g(u) - f(v)g(v)| \le |f(u)|\,|g(u) - g(v)| + |g(v)|\,|f(u) - f(v)| \le M\omega_i' + N\omega_i,
$$
so $\omega_i'' \le M\omega_i' + N\omega_i$, and Theorem 7.1.1 shows that $fg$ is integrable. In general, let $f_1 = \frac12(|f| + f)$ and $f_2 = \frac12(|f| - f)$ (both nonnegative and integrable, with $f = f_1 - f_2$), and define $g_1, g_2$ similarly. Then $fg = f_1g_1 - f_1g_2 - f_2g_1 + f_2g_2$ is integrable by linearity. $\square$

**Property 7.2.10 (Generalized Mean Value Theorem for Integrals)** If $f \in C[a,b]$, $g \in \mathcal{R}[a,b]$, and $g$ does not change sign on $[a,b]$, then there exists $\xi \in [a,b]$ such that

$$
\int_a^b f(x)g(x)\,\mathrm{d}x = f(\xi)\int_a^b g(x)\,\mathrm{d}x.
$$

**Proof** Without loss of generality let $g \ge 0$. From $m \le f \le M$ we get $m\int_a^b g \le \int_a^b fg \le M\int_a^b g$. If $\int_a^b g = 0$, then $\int_a^b fg = 0$ and any $\xi$ works; otherwise $\int_a^b fg\big/\int_a^b g \in [m, M]$, and by the **intermediate value theorem** there is $\xi$ with $f(\xi)$ equal to this quotient. $\square$

With $g \equiv 1$ this reduces to Property 7.2.8. The proofs of both mean value theorems use only the intermediate value theorem for continuous functions and have nothing to do with the mean value theorems of differential calculus.

**Example 7.2.1** Let $f \in C[a,b]$, $f \ge 0$, and $\int_a^b f(x)\,\mathrm{d}x = 0$. Then $f \equiv 0$.

**Proof** Suppose $f(x_0) > 0$ for some $x_0$. By continuity we may assume $x_0 \in (a,b)$, and there is $\delta > 0$ such that $[x_0 - \delta, x_0 + \delta] \subset [a,b]$ and $f(x) > f(x_0)/2$ on this interval. Then

$$
\int_a^b f\,\mathrm{d}x \ge \int_{x_0-\delta}^{x_0+\delta} f\,\mathrm{d}x \ge 2\delta\cdot\frac{f(x_0)}{2} = \delta f(x_0) > 0,
$$
a contradiction. $\square$

This result says that the integral of a nonnegative continuous function cannot vanish "for no reason"; it is the basis for the positive definiteness of the **inner product** $\langle f, g\rangle = \int_a^b fg\,\mathrm{d}x$; see [Linear Algebra 2.1.12](/2.1.12).

**Example 7.2.2** Let $f(0) = 0$, and let $f$ be differentiable on $[0,a]$ with $M = \sup_{[0,a]}|f'| < +\infty$. Then $\left|\int_0^a f(x)\,\mathrm{d}x\right| \le \frac12 a^2M$.

**Proof** By the **mean value theorem**, $f(x) = f(x) - f(0) = f'(\eta)x$, so $|f(x)| \le Mx$ and $\left|\int_0^a f\right| \le \int_0^a Mx\,\mathrm{d}x = \frac12a^2M$. $\square$

**Example 7.2.3** Let $f$ be twice differentiable on $[a,b]$ with $f'' \le 0$. Then $\int_a^b f(x)\,\mathrm{d}x \le (b-a)f\left(\frac{a+b}{2}\right)$.

**Proof** The condition $f'' \le 0$ means that $f$ is a **concave function** (also called "convex upward"), so its graph lies below its **tangent line** at $c = \frac{a+b}{2}$: $f(x) \le f(c) + f'(c)(x - c)$. Integrating both sides and using $\int_a^b (x - c)\,\mathrm{d}x = 0$ gives $\int_a^b f \le (b-a)f(c)$. $\square$

Geometrically, the trapezoid bounded by the tangent line, $x = a$, $x = b$ and the $x$-axis has area exactly $(b-a)f(c)$, and the region under the curve lies inside it.

## 7.3. Integrals with Variable Upper Limit and the Newton–Leibniz Formula

### 7.3.1. Integrals with Variable Upper Limit

**Definition 7.3.1 (Integral with a Variable Upper Limit)** Let $f \in \mathcal{R}[a,b]$. By Property 7.2.2, $\int_a^x f(t)\,\mathrm{d}t$ exists for every $x \in [a,b]$, so

$$
F(x) = \int_a^x f(t)\,\mathrm{d}t, \qquad a \le x \le b
$$
is a function on $[a,b]$, called the integral of $f$ with variable upper limit; $F(a) = 0$.

**Theorem 7.3.1** Let $f \in \mathcal{R}[a,b]$ and $F(x) = \int_a^x f(t)\,\mathrm{d}t$. Then

1. $F$ is continuous on $[a,b]$;
2. If $f$ is continuous at $x_0 \in [a,b]$, then $F$ is differentiable at $x_0$ and $F'(x_0) = f(x_0)$ (a one-sided derivative at the endpoints);
3. If $f \in C[a,b]$, then $F'(x) = f(x)$ for every $x \in [a,b]$.

**Proof** 1. An integrable function is bounded, say $|f| \le M$; then $|F(x + \Delta x) - F(x)| = \left|\int_x^{x+\Delta x} f(t)\,\mathrm{d}t\right| \le M|\Delta x| \to 0$.

2. Given $\varepsilon > 0$, by the continuity of $f$ at $x_0$ there is $\delta > 0$ such that $|f(t) - f(x_0)| < \varepsilon$ whenever $|t - x_0| < \delta$. Hence for $0 < |\Delta x| < \delta$,

$$
\left|\frac{F(x_0 + \Delta x) - F(x_0)}{\Delta x} - f(x_0)\right| = \left|\frac{1}{\Delta x}\int_{x_0}^{x_0+\Delta x}\bigl(f(t) - f(x_0)\bigr)\,\mathrm{d}t\right| \le \varepsilon.
$$

3 follows immediately from 2. $\square$

**Corollary 7.3.1** A continuous function on an interval always has an **antiderivative**: $\int_a^x f(t)\,\mathrm{d}t$ is one. This supplies the proof, postponed in [Chapter 6](/2.2.6), that continuous functions have antiderivatives.

Combined with the **chain rule**, this gives the formulas for differentiating integrals with variable limits: if $f$ is continuous and $u, v$ are differentiable, then

$$
\frac{\mathrm{d}}{\mathrm{d}x}\int_a^x f(t)\,\mathrm{d}t = f(x), \qquad \frac{\mathrm{d}}{\mathrm{d}x}\int_x^b f(t)\,\mathrm{d}t = -f(x), \qquad \frac{\mathrm{d}}{\mathrm{d}x}\int_{u(x)}^{v(x)} f(t)\,\mathrm{d}t = f\bigl(v(x)\bigr)v'(x) - f\bigl(u(x)\bigr)u'(x).
$$

Proof of the last formula: fix $c$ and write the integral as $\int_c^{v(x)} f - \int_c^{u(x)} f$; with $G(v) = \int_c^v f(t)\,\mathrm{d}t$ we have $\frac{\mathrm{d}}{\mathrm{d}x}G(v(x)) = G'(v)v'(x) = f(v(x))v'(x)$. Note that the integrand must not contain $x$; if it does (as in $\int_0^x xf(t)\,\mathrm{d}t$), first move $x$ outside the integral sign.

**Example 7.3.1** Find $\lim_{x\to0}\dfrac{1}{x^3}\displaystyle\int_0^x\left(\int_{\sin s}^0 t\,\mathrm{d}t\right)\mathrm{d}s$.

**Solution** This is of the form $\frac00$; apply **L'Hôpital's rule** twice:

$$
\lim_{x\to0}\frac{\int_0^x\left(\int_{\sin s}^0 t\,\mathrm{d}t\right)\mathrm{d}s}{x^3} = \lim_{x\to0}\frac{\int_{\sin x}^0 t\,\mathrm{d}t}{3x^2} = \lim_{x\to0}\frac{-\sin x\cos x}{6x} = -\frac16.
$$

**Example 7.3.2** As $x \to +\infty$, $\int_a^x \mathrm{e}^{t^2}\,\mathrm{d}t \sim \dfrac{1}{2x}\mathrm{e}^{x^2}$.

**Solution** By L'Hôpital's rule (form $\frac{\infty}{\infty}$),

$$
\lim_{x\to+\infty}\frac{\int_a^x\mathrm{e}^{t^2}\,\mathrm{d}t}{\mathrm{e}^{x^2}/(2x)} = \lim_{x\to+\infty}\frac{\mathrm{e}^{x^2}}{\mathrm{e}^{x^2}\left(1 - \frac{1}{2x^2}\right)} = 1.
$$

The antiderivative of $\mathrm{e}^{t^2}$ is not an **elementary function**, yet the integral with variable upper limit still tells us its rate of growth.

### 7.3.2. The Newton–Leibniz Formula

**Theorem 7.3.2 (Fundamental Theorem of Calculus)** Let $f \in C[a,b]$, and let $G$ be any antiderivative of $f$ on $[a,b]$. Then

$$
\int_a^b f(x)\,\mathrm{d}x = G(b) - G(a) \;\eqqcolon\; G(x)\Big|_a^b.
$$

**Proof** By Corollary 7.3.1, $F(x) = \int_a^x f(t)\,\mathrm{d}t$ is an antiderivative of $f$. Two antiderivatives of the same function differ by a constant, $G = F + C$, so $G(b) - G(a) = F(b) - F(a) = \int_a^b f\,\mathrm{d}x$. $\square$

This formula is also called the Newton–Leibniz formula. It reduces the computation of a definite integral (a limit of sums) to finding an antiderivative, so all the integration techniques of [Chapter 6](/2.2.6) become available for definite integrals. The theorem requires $f$ to be continuous; for an integrable function with finitely many jump discontinuities, it can be applied piece by piece.

**Example 7.3.3**

1. $\int_0^1\frac{x}{\sqrt{1+x^2}}\,\mathrm{d}x = \sqrt{1+x^2}\Big|_0^1 = \sqrt2 - 1$; $\int_1^{\mathrm{e}}\frac{\ln^2 x}{x}\,\mathrm{d}x = \frac13\ln^3x\Big|_1^{\mathrm{e}} = \frac13$.
2. $\int_{-\pi/2}^{\pi/2}\sqrt{1 - \cos x}\,\mathrm{d}x$: since $1 - \cos x = 2\sin^2\frac{x}{2}$, the integrand is $\sqrt2\,\bigl|\sin\frac{x}{2}\bigr|$; the absolute value produced by the square root must not be dropped. It is an **even function**, so the integral equals $2\sqrt2\int_0^{\pi/2}\sin\frac{x}{2}\,\mathrm{d}x = 2\sqrt2\left(-2\cos\frac x2\right)\Big|_0^{\pi/2} = 4(\sqrt2 - 1)$.

The limit of Riemann sums does not depend on the partition or on the choice of points. Conversely, if $f \in C[0,1]$ is known, we may take equally spaced points and right endpoints and thereby convert certain limits of sums into integrals.

**Algorithm 7.3.1 (Limits of Sums via Definite Integrals)** Let $f \in C[0,1]$. Then

$$
\lim_{n\to\infty}\frac1n\sum_{i=1}^n f\left(\frac in\right) = \int_0^1 f(x)\,\mathrm{d}x.
$$

1. Write the sum in the form $\frac1n\sum f(i/n)$ (factor out $\frac1n$ so that the general term depends only on $i/n$);
2. Identify $f$, changing the interval to $[0,k]$ if necessary: $\frac1n\sum_{i=1}^{kn} f(i/n) \to \int_0^k f$;
3. For a product, first take logarithms to turn it into a sum.

**Example 7.3.4**

1. $\displaystyle\lim_{n\to\infty}\sum_{i=1}^n\frac{n}{n^2+i^2} = \lim_{n\to\infty}\frac1n\sum_{i=1}^n\frac{1}{1+(i/n)^2} = \int_0^1\frac{\mathrm{d}x}{1+x^2} = \frac\pi4$.
2. $\displaystyle\lim_{n\to\infty}\frac{1^2 + 2^2 + \cdots + (2n)^2}{n^3} = \lim_{n\to\infty}\frac1n\sum_{i=1}^{2n}\left(\frac in\right)^2 = \int_0^2 x^2\,\mathrm{d}x = \frac83$.
3. If $f \in C[0,1]$ and $f > 0$, then $\displaystyle\lim_{n\to\infty}\sqrt[n]{f\left(\tfrac1n\right)f\left(\tfrac2n\right)\cdots f\left(\tfrac nn\right)} = \lim_{n\to\infty}\exp\left(\frac1n\sum_{i=1}^n\ln f\left(\frac in\right)\right) = \exp\left(\int_0^1\ln f(x)\,\mathrm{d}x\right)$.
4. For $p > 0$, $\displaystyle\lim_{n\to\infty}\frac{1^p + 2^p + \cdots + n^p}{n^{p+1}} = \int_0^1 x^p\,\mathrm{d}x = \frac{1}{p+1}$.

## 7.4. Substitution and Integration by Parts

### 7.4.1. Substitution

**Theorem 7.4.1 (First Substitution Rule)** Let $f \in C[\alpha,\beta]$, and let $u = \varphi(x)$ be continuously differentiable on $[a,b]$ with range contained in $[\alpha,\beta]$, $\varphi(a) = \alpha'$ and $\varphi(b) = \beta'$. Then

$$
\int_a^b f\bigl(\varphi(x)\bigr)\varphi'(x)\,\mathrm{d}x = \int_{\alpha'}^{\beta'} f(u)\,\mathrm{d}u.
$$

**Theorem 7.4.2 (Second Substitution Rule)** Let $f \in C[a,b]$, and let $x = \varphi(t)$ be continuously differentiable on $[\alpha,\beta]$ with range contained in $[a,b]$, $\varphi(\alpha) = a$ and $\varphi(\beta) = b$. Then

$$
\int_a^b f(x)\,\mathrm{d}x = \int_\alpha^\beta f\bigl(\varphi(t)\bigr)\varphi'(t)\,\mathrm{d}t.
$$

**Proof** The two proofs are the same: if $F$ is an antiderivative of $f$, then $F(\varphi)$ is an antiderivative of $f(\varphi)\varphi'$ (**chain rule**); applying the Newton–Leibniz formula to both sides, each equals $F(\varphi(\text{upper limit})) - F(\varphi(\text{lower limit}))$. $\square$

Compared with **integration by substitution** for indefinite integrals:

- When the variable changes, the limits change with it, and there is no need to return to the original variable;
- The second substitution rule does not require $x = \varphi(t)$ to have an inverse (for indefinite integrals the inverse is needed to substitute back), and it allows $\alpha > \beta$;
- But $\varphi$ must be continuously differentiable, its range must not leave the interval on which $f$ is defined, and the endpoints must correspond.

**Example 7.4.1 (Pitfalls of Substitution)**

1. In $\int_0^3 x\sqrt[3]{1-x^2}\,\mathrm{d}x$ we cannot put $x = \sin t$, since $\sin t$ does not take values in $(1,3]$. Use $u = 1 - x^2$ instead (first substitution rule).
2. In $\int_0^1\sqrt{1-x^2}\,\mathrm{d}x$ with $x = \sin t$, we may let $t$ run from $\pi$ to $\frac\pi2$, but then $\sqrt{1-\sin^2t} = |\cos t| = -\cos t$, and the result $\int_\pi^{\pi/2}(-\cos t)\cos t\,\mathrm{d}t = \frac\pi4$ is still correct; forgetting the absolute value gives the wrong sign.
3. In $\int_{-1}^2 x\,\mathrm{d}x$ we cannot put $x = \sqrt t$ ($\sqrt t \ge 0$ never takes negative values); the first substitution $t = x^2$, however, is legitimate: $\int_{-1}^2 x\,\mathrm{d}x = \frac12\int_1^4\mathrm{d}t = \frac32$. Here $\varphi(x) = x^2$ need not be monotone.
4. In $\int_{-1}^1\frac{\mathrm{d}x}{1+x^2}$ we cannot put $t = 1/x$, which is undefined at $x = 0$. Forcing the computation gives $-\int_{-1}^1\frac{\mathrm{d}t}{1+t^2} = -\frac\pi2$, whereas the correct value is $\frac\pi2$.

**Example 7.4.2**

1. $\int_1^4\frac{\mathrm{d}x}{1+\sqrt x}$, with $x = t^2$: $= \int_1^2\frac{2t}{1+t}\,\mathrm{d}t = 2\bigl(t - \ln(1+t)\bigr)\Big|_1^2 = 2 + 2\ln\frac23$.
2. $\int_0^a\sqrt{a^2-x^2}\,\mathrm{d}x$, with $x = a\sin t$: $= a^2\int_0^{\pi/2}\cos^2t\,\mathrm{d}t = \frac{\pi a^2}{4}$ (the area of a quarter disk).
3. $\int_0^{\pi/2}\frac{\sin x}{1+\cos^2x}\,\mathrm{d}x$, with $u = \cos x$: $= \int_0^1\frac{\mathrm{d}u}{1+u^2} = \frac\pi4$.

**Theorem 7.4.3** Let $f$ be continuous.

1. If $f$ is an **even function** on $[-a,a]$, then $\int_{-a}^a f\,\mathrm{d}x = 2\int_0^a f\,\mathrm{d}x$; if it is an **odd function**, then $\int_{-a}^a f\,\mathrm{d}x = 0$.
2. If $f$ is a **periodic function** with period $T$, then $\int_a^{a+T} f\,\mathrm{d}x = \int_0^T f\,\mathrm{d}x$ for every $a$.
3. $\int_0^\pi xf(\sin x)\,\mathrm{d}x = \frac\pi2\int_0^\pi f(\sin x)\,\mathrm{d}x$.

**Proof** 1. In $\int_{-a}^0 f(x)\,\mathrm{d}x$ put $x = -t$ to get $\int_0^a f(-t)\,\mathrm{d}t$, and combine according to parity.

2. Write $\int_a^{a+T} = \int_a^0 + \int_0^T + \int_T^{a+T}$; putting $x = t + T$ in the last term gives $\int_0^a f(t)\,\mathrm{d}t$, which cancels the first term.

3. Put $x = \pi - t$: $I = \int_0^\pi(\pi - t)f(\sin t)\,\mathrm{d}t = \pi\int_0^\pi f(\sin t)\,\mathrm{d}t - I$. $\square$

**Example 7.4.3**

1. $\int_{-\pi/2}^{\pi/2}\tan x\,(1 + x^2)\,\mathrm{d}x = 0$ (odd integrand).
2. $\int_0^{100\pi}\sqrt{1 - \cos 2x}\,\mathrm{d}x = 100\int_0^\pi\sqrt2\,|\sin x|\,\mathrm{d}x = 200\sqrt2$ (period $\pi$).
3. $\int_{-1}^1\left(\sqrt{1-x^2} + x\mathrm{e}^{x^2}\right)\mathrm{d}x = 2\int_0^1\sqrt{1-x^2}\,\mathrm{d}x = \frac\pi2$.
4. $\int_0^\pi\frac{x\sin x}{1+\cos^2x}\,\mathrm{d}x = \frac\pi2\int_0^\pi\frac{\sin x}{1+\cos^2x}\,\mathrm{d}x = \frac\pi2\cdot\frac\pi2 = \frac{\pi^2}{4}$.

### 7.4.2. Integration by Parts

**Theorem 7.4.4** Let $u, v$ be continuously differentiable on $[a,b]$. Then

$$
\int_a^b u(x)v'(x)\,\mathrm{d}x = u(x)v(x)\Big|_a^b - \int_a^b u'(x)v(x)\,\mathrm{d}x.
$$

**Proof** Integrate $(uv)' = u'v + uv'$ over $[a,b]$ and use the Newton–Leibniz formula. $\square$

The choice of $u$ and $v'$ follows the same principles as in **integration by parts** for indefinite integrals; the advantage here is that the boundary term $uv|_a^b$ is often zero or very simple.

**Example 7.4.4**

1. $\int_0^{1/2}\arcsin x\,\mathrm{d}x = x\arcsin x\Big|_0^{1/2} - \int_0^{1/2}\frac{x\,\mathrm{d}x}{\sqrt{1-x^2}} = \frac{\pi}{12} + \frac{\sqrt3}{2} - 1$.
2. $\int_0^\pi\mathrm{e}^x\sin x\,\mathrm{d}x$: integrating by parts twice returns to the original integral, $I = \mathrm{e}^\pi + 1 - I$, so $I = \frac12(\mathrm{e}^\pi + 1)$.
3. $\int_0^1\mathrm{e}^{\sqrt x}\,\mathrm{d}x \overset{x = t^2}{=} 2\int_0^1 t\mathrm{e}^t\,\mathrm{d}t = 2\bigl(t\mathrm{e}^t - \mathrm{e}^t\bigr)\Big|_0^1 = 2$.
4. $\int_0^1(\arcsin x)^2\,\mathrm{d}x = x(\arcsin x)^2\Big|_0^1 - 2\int_0^1\frac{x\arcsin x}{\sqrt{1-x^2}}\,\mathrm{d}x = \frac{\pi^2}{4} + 2\left(\sqrt{1-x^2}\arcsin x\Big|_0^1 - \int_0^1\mathrm{d}x\right) = \frac{\pi^2}{4} - 2$.

**Formula 7.4.1 (Wallis Integrals)** Let $I_n = \int_0^{\pi/2}\sin^nx\,\mathrm{d}x$. Then $\int_0^{\pi/2}\cos^nx\,\mathrm{d}x = I_n$, and

$$
I_n = \frac{n-1}{n}I_{n-2}, \qquad I_n = \begin{cases}\dfrac{(n-1)!!}{n!!}\cdot\dfrac\pi2, & n \text{ even},\\[2ex] \dfrac{(n-1)!!}{n!!}, & n \text{ odd},\end{cases}
$$
where $n!! = n(n-2)(n-4)\cdots$ (down to $2$ or $1$).

**Proof** Let $u = \sin^{n-1}x$ and $\mathrm{d}v = \sin x\,\mathrm{d}x$:

$$
I_n = -\sin^{n-1}x\cos x\Big|_0^{\pi/2} + (n-1)\int_0^{\pi/2}\sin^{n-2}x\cos^2x\,\mathrm{d}x = (n-1)(I_{n-2} - I_n),
$$
that is, $I_n = \frac{n-1}{n}I_{n-2}$; then recurse from $I_0 = \frac\pi2$ and $I_1 = 1$. The substitution $x = \frac\pi2 - t$ shows that the integral of $\cos^n$ equals $I_n$. $\square$

For example, $\int_0^{\pi/2}\cos^2x\,\mathrm{d}x = \frac12\cdot\frac\pi2 = \frac\pi4$, $\int_0^{\pi/2}\sin^4x\,\mathrm{d}x = \frac34\cdot\frac12\cdot\frac\pi2 = \frac{3\pi}{16}$, and $\int_0^{\pi/2}\sin^5x\,\mathrm{d}x = \frac45\cdot\frac23 = \frac{8}{15}$.

**Example 7.4.5** Compute $I_n = \int_0^{\pi/4}\tan^{2n}x\,\mathrm{d}x$.

**Solution** Since $\tan^2x = \sec^2x - 1$, we have $I_n = \int_0^{\pi/4}\tan^{2n-2}x\,\mathrm{d}(\tan x) - I_{n-1} = \frac{1}{2n-1} - I_{n-1}$ with $I_0 = \frac\pi4$, so

$$
I_n = (-1)^n\left[\frac\pi4 - \left(1 - \frac13 + \frac15 - \cdots + \frac{(-1)^{n-1}}{2n-1}\right)\right].
$$

Since $0 \le \tan x \le \frac{4x}{\pi}$ on $[0,\frac\pi4]$ ($\tan$ is a **convex function** there, so its graph lies below the chord joining the endpoints), $0 \le I_n \le \int_0^{\pi/4}\left(\frac{4x}{\pi}\right)^{2n}\mathrm{d}x = \frac{\pi}{4(2n+1)} \to 0$. Therefore $1 - \frac13 + \frac15 - \cdots = \frac\pi4$; this is the Leibniz series.

## 7.5. Geometric Applications of the Definite Integral

### 7.5.1. Area of Plane Regions

In Cartesian coordinates, the area of the region bounded by a continuous curve $y = f(x)$, the lines $x = a$, $x = b$ and the $x$-axis is $S = \int_a^b|f(x)|\,\mathrm{d}x$; the area of the region bounded by two continuous curves $y = f(x)$, $y = g(x)$ and the lines $x = a$, $x = b$ is

$$
S = \int_a^b|f(x) - g(x)|\,\mathrm{d}x.
$$

For a curve given parametrically by $x = x(t)$, $y = y(t)$ (with $x(\alpha) = a$, $x(\beta) = b$ and $x(t)$ monotone), $\int_a^b y\,\mathrm{d}x = \int_\alpha^\beta y(t)x'(t)\,\mathrm{d}t$ (second substitution rule).

**Example 7.5.1** The curves $y = x^2$ and $y^2 = x$ intersect at $(0,0)$ and $(1,1)$, and the region they enclose has area $S = \int_0^1(\sqrt x - x^2)\,\mathrm{d}x = \frac23 - \frac13 = \frac13$.

**Example 7.5.2** The area between one arch of the cycloid $x = a(t - \sin t)$, $y = a(1 - \cos t)$ ($0 \le t \le 2\pi$, $a > 0$) and the $x$-axis is

$$
S = \int_0^{2\pi a}y\,\mathrm{d}x = \int_0^{2\pi}a^2(1 - \cos t)^2\,\mathrm{d}t = a^2(2\pi + \pi) = 3\pi a^2.
$$

Finally, polar coordinates. Choose a pole $O$ in the plane and a polar axis $Ox$ issuing from $O$. A point $P$ is determined by its distance $r$ to $O$ (the radial coordinate) and the angle $\theta$ between $OP$ and the polar axis (the polar angle); $(r,\theta)$ are called the *polar coordinates* of $P$. If the pole is the origin of a Cartesian system and the polar axis is the positive $x$-axis, then $x = r\cos\theta$ and $y = r\sin\theta$. A curve is written $r = r(\theta)$; for example, $r = a$ is the circle centered at the pole, and $\theta = \theta_0$ is a ray from the pole.

Let $r = r(\theta)$ be continuous and nonnegative on $[\alpha,\beta]$; we want the area of the sector-like region $D$ bounded by this curve and the rays $\theta = \alpha$, $\theta = \beta$. Partition $[\alpha,\beta]$; the rays $\theta = \theta_i$ cut $D$ into small pieces, the $i$-th of which is approximately a circular sector of radius $r(\xi_i)$ and central angle $\Delta\theta_i$, with area $\frac12r(\xi_i)^2\Delta\theta_i$. Summing and taking the limit,

$$
S = \frac12\int_\alpha^\beta r(\theta)^2\,\mathrm{d}\theta.
$$

![Area in polar coordinates: a cardioid approximated by small sectors (left) and a lemniscate (right)](./plots/polar-area.py)

**Example 7.5.3** The area enclosed by the lemniscate $r^2 = 2a^2\cos2\theta$ ($-\frac\pi4 \le \theta \le \frac\pi4$ or $\frac{3\pi}4 \le \theta \le \frac{5\pi}4$) is

$$
S = 2\cdot\frac12\int_{-\pi/4}^{\pi/4}2a^2\cos2\theta\,\mathrm{d}\theta = a^2\sin2\theta\Big|_{-\pi/4}^{\pi/4} = 2a^2.
$$

The area enclosed by the cardioid $r = a(1 + \cos\theta)$ is $\frac12\int_0^{2\pi}a^2(1 + \cos\theta)^2\,\mathrm{d}\theta = \frac{a^2}{2}(2\pi + \pi) = \frac32\pi a^2$.

### 7.5.2. Arc Length

A curve without self-intersections is called a simple curve. Let a simple curve $L$ have the parametric equations $x = x(t)$, $y = y(t)$ ($\alpha \le t \le \beta$).

**Definition 7.5.1** Choose points $M_0, M_1, \dots, M_n$ on $L$ in the order of the parameter and form the inscribed polygonal path. If, as the partition is refined ($\max_i\Delta t_i \to 0$), the length $\sum_i|M_{i-1}M_i|$ of the polygonal path has a limit, then $L$ is called a **rectifiable curve**, and the limit is called the **arc length** of $L$.

**Theorem 7.5.1** If $x(t)$ and $y(t)$ are continuously differentiable on $[\alpha,\beta]$, then $L$ is rectifiable and

$$
l = \int_\alpha^\beta\sqrt{x'(t)^2 + y'(t)^2}\,\mathrm{d}t.
$$

**Proof** By the **mean value theorem**, $|M_{i-1}M_i| = \sqrt{x'(\xi_i)^2 + y'(\eta_i)^2}\,\Delta t_i$ with $\xi_i, \eta_i \in [t_{i-1}, t_i]$. By the **uniform continuity** of $y'$, the error caused by replacing $\eta_i$ with $\xi_i$ tends to zero as $\lambda \to 0$, so the length of the polygonal path tends to the limit of the Riemann sums of $\sqrt{x'^2 + y'^2}$, which is the integral above. $\square$

The quantity $\mathrm{d}l = \sqrt{x'(t)^2 + y'(t)^2}\,\mathrm{d}t$ is called the element of arc length. Some special forms:

| Curve | Arc length |
|---|---|
| Parametric $x(t), y(t)$ | $\int_\alpha^\beta\sqrt{x'^2 + y'^2}\,\mathrm{d}t$ |
| Space curve $x(t), y(t), z(t)$ | $\int_\alpha^\beta\sqrt{x'^2 + y'^2 + z'^2}\,\mathrm{d}t$ |
| $y = f(x)$, $a \le x \le b$ ($x$ as the parameter) | $\int_a^b\sqrt{1 + f'(x)^2}\,\mathrm{d}x$ |
| Polar $r = r(\theta)$ ($x = r\cos\theta$, $y = r\sin\theta$) | $\int_\alpha^\beta\sqrt{r^2 + r'^2}\,\mathrm{d}\theta$ |

**Example 7.5.4**

1. The astroid $x = a\cos^3t$, $y = a\sin^3t$ ($0 \le t \le 2\pi$): $\sqrt{x'^2 + y'^2} = 3a|\sin t\cos t|$, so $l = \frac{3a}{2}\int_0^{2\pi}|\sin2t|\,\mathrm{d}t = 6a$.
2. The helix $x = a\sin t$, $y = a\cos t$, $z = ct$ ($0 \le t \le 2\pi$): $l = \int_0^{2\pi}\sqrt{a^2 + c^2}\,\mathrm{d}t = 2\pi\sqrt{a^2 + c^2}$.
3. The parabola $y = x^2$ ($0 \le x \le 1$): $l = \int_0^1\sqrt{1 + 4x^2}\,\mathrm{d}x \overset{t=2x}{=} \frac12\int_0^2\sqrt{1+t^2}\,\mathrm{d}t = \frac14\left(t\sqrt{1+t^2} + \ln\bigl(t + \sqrt{1+t^2}\bigr)\right)\Big|_0^2 = \frac{\sqrt5}{2} + \frac14\ln(2 + \sqrt5)$.
4. The cardioid $r = a(1 + \cos\theta)$: $r^2 + r'^2 = 2a^2(1 + \cos\theta) = 4a^2\cos^2\frac\theta2$, so $l = \int_0^{2\pi}2a\left|\cos\frac\theta2\right|\mathrm{d}\theta = 8a$.

### 7.5.3. Curvature of Plane Curves

**Definition 7.5.2 (Smooth Curve)** If $x'(t)$ and $y'(t)$ are continuous and $x'(t)^2 + y'(t)^2 \ne 0$, the curve $L\colon x = x(t), y = y(t)$ is called a smooth curve. A smooth curve has a tangent line at every point, and the direction of the tangent varies continuously along the curve.

The more sharply a curve bends, the larger the angle through which its tangent turns per unit length traveled along the curve. Let $M$ and $M'$ be two points on $L$, let $\Delta\varphi$ be the angle between the tangent lines at these points, and let $\Delta l$ be the arc length between them. Then $|\Delta\varphi/\Delta l|$ measures the average bending of the curve between $M$ and $M'$.

**Definition 7.5.3 (Curvature)** If the limit $k = \lim_{M'\to M}\left|\frac{\Delta\varphi}{\Delta l}\right|$ exists, $k$ is called the curvature of $L$ at $M$, and $R = \frac1k$ is called the **radius of curvature** of $L$ at $M$.

Let $\varphi$ be the angle between the tangent line and the $x$-axis, so that $\tan\varphi = \frac{y'(t)}{x'(t)}$. Then $\frac{\mathrm{d}\varphi}{\mathrm{d}t} = \frac{y''x' - y'x''}{x'^2 + y'^2}$, and since $\frac{\mathrm{d}l}{\mathrm{d}t} = \sqrt{x'^2 + y'^2}$,

$$
k = \left|\frac{\mathrm{d}\varphi/\mathrm{d}t}{\mathrm{d}l/\mathrm{d}t}\right| = \frac{|x'y'' - x''y'|}{(x'^2 + y'^2)^{3/2}}.
$$

Special cases:

$$
y = f(x)\colon\; k = \frac{|y''|}{(1 + y'^2)^{3/2}}; \qquad r = r(\theta)\colon\; k = \frac{|r^2 + 2r'^2 - rr''|}{(r^2 + r'^2)^{3/2}}.
$$

**Example 7.5.5** For the parabola $y = x^2$, at the point $(x, x^2)$ we have $k = \frac{2}{(1 + 4x^2)^{3/2}}$ and $R = \frac12(1 + 4x^2)^{3/2}$, so the parabola bends most sharply at its vertex. For the circle $r = R_0$ ($r' = r'' = 0$), $k = \frac{R_0^2}{R_0^3} = \frac{1}{R_0}$ everywhere: the radius of curvature is the radius of the circle. A straight line has curvature zero.

### 7.5.4. Volumes of Solids of Revolution and Areas of Surfaces of Revolution

Rotating the plane region bounded by a continuous curve $y = y(x)$, the lines $x = a$, $x = b$ and the $x$-axis one full turn about the $x$-axis produces a *solid of revolution*. Slice it by planes perpendicular to the $x$-axis; the slice over $[x, x + \mathrm{d}x]$ is approximately a cylinder of volume $\mathrm{d}V = \pi y(x)^2\,\mathrm{d}x$, so

$$
V = \pi\int_a^b y(x)^2\,\mathrm{d}x.
$$

**Example 7.5.6** Rotating the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ about the $x$-axis gives $V = \pi\int_{-a}^a\frac{b^2}{a^2}(a^2 - x^2)\,\mathrm{d}x = \frac43\pi ab^2$; with $a = b = R$ this is the volume $\frac43\pi R^3$ of a ball.

Parametric and polar forms:

- A curve $x = x(t)$, $y = y(t)$ rotated about the $x$-axis: $V = \pi\int_\alpha^\beta y(t)^2x'(t)\,\mathrm{d}t$. For example, one arch of the cycloid rotated about the $x$-axis gives $V = \pi a^3\int_0^{2\pi}(1 - \cos t)^3\,\mathrm{d}t = 5\pi^2a^3$.
- A sector-like region $0 \le r \le r(\theta)$, $\alpha \le \theta \le \beta$ ($0 \le \alpha < \beta \le \pi$) rotated about the polar axis: a thin sector rotated about the polar axis sweeps out a volume of approximately $\frac{2\pi}{3}r^3\sin\theta\,\mathrm{d}\theta$, so $V = \frac{2\pi}{3}\int_\alpha^\beta r(\theta)^3\sin\theta\,\mathrm{d}\theta$. For example, $r = R$, $0 \le \theta \le \pi$ gives the volume of a ball, $\frac{2\pi}{3}R^3\cdot2 = \frac43\pi R^3$.

Let $y(x) \ge 0$ be continuously differentiable on $[a,b]$. Rotating the curve $y = y(x)$ one full turn about the $x$-axis produces a *surface of revolution*. Cut it by the planes $x = x_i$ into thin bands, each approximately the lateral surface of a frustum of a cone, with area $\pi\bigl(y(x_{i-1}) + y(x_i)\bigr)|P_{i-1}P_i|$, where $|P_{i-1}P_i| = \sqrt{1 + y'(\xi_i)^2}\,\Delta x_i$. Summing and taking the limit gives

$$
S = 2\pi\int_a^b y(x)\sqrt{1 + y'(x)^2}\,\mathrm{d}x = 2\pi\int y\,\mathrm{d}l.
$$

Here one may not approximate by the lateral surface $2\pi y\,\mathrm{d}x$ of a cylinder: the sides of the bands are slanted, so the element of arc length $\mathrm{d}l$ must be used instead of $\mathrm{d}x$.

**Example 7.5.7** Rotating $y = \sqrt x$ ($0 \le x \le 1$) about the $x$-axis: $S = 2\pi\int_0^1\sqrt x\sqrt{1 + \frac{1}{4x}}\,\mathrm{d}x = \pi\int_0^1\sqrt{4x+1}\,\mathrm{d}x = \frac\pi6(5\sqrt5 - 1)$. Rotating the semicircle $y = \sqrt{R^2 - x^2}$ about the $x$-axis: $y\sqrt{1 + y'^2} = R$, so $S = 2\pi R\cdot2R = 4\pi R^2$.

## 7.6. Physical Applications of the Definite Integral

In mathematics the integral is defined by the four-step procedure (partition, approximate, sum, take the limit); in physics the following shortcut is more common.

**Algorithm 7.6.1 (Method of Differential Elements)** To find a quantity $Q$ distributed over $[a,b]$ and additive with respect to intervals:

1. Take a typical small interval $[x, x + \mathrm{d}x]$ and write down an approximation $\mathrm{d}Q = q(x)\,\mathrm{d}x$ of the part of $Q$ over it (the error being a **higher-order infinitesimal** with respect to $\mathrm{d}x$);
2. $Q = \int_a^b q(x)\,\mathrm{d}x$.

The method of differential elements is intuitive and concise, and it is essentially the Newton–Leibniz formula: if $Q(x)$ denotes "the part of the quantity from $a$ to $x$", step 1 says that $Q'(x) = q(x)$. The volume of a solid of revolution in Section 7.5 was derived in exactly this way.

**Example 7.6.1 (Gravitational Attraction)** A uniform thin rod has length $2l$ and mass $M$, and a unit point mass lies on the extension of the rod at distance $a$ ($a > l$) from its center. Take the midpoint of the rod as the origin. The segment $[x, x + \mathrm{d}x]$ has mass $\frac{M}{2l}\mathrm{d}x$ and attracts the point mass with force $\mathrm{d}F = \frac{GM}{2l}\frac{\mathrm{d}x}{(a - x)^2}$, so

$$
F = \frac{GM}{2l}\int_{-l}^l\frac{\mathrm{d}x}{(a - x)^2} = \frac{GM}{a^2 - l^2}.
$$

As $l \to 0$ we recover the attraction $GM/a^2$ between two point masses.

**Example 7.6.2 (Work Done by a Variable Force)** A force of $40\,\mathrm{N}$ stretches a spring by $5\,\mathrm{cm}$. How much work is needed to stretch it a further $3\,\mathrm{cm}$? By Hooke's law $F = kx$ with $k = 40/0.05 = 800\,\mathrm{N/m}$, so $W = \int_{0.05}^{0.08}800x\,\mathrm{d}x = 1.56\,\mathrm{J}$.

**Example 7.6.3 (Pumping Water)** A cylindrical tank of height $5\,\mathrm{m}$ and base radius $3\,\mathrm{m}$ is full of water, which is pumped out over the top. Take the $x$-axis pointing downward with origin at the top of the tank. Lifting the thin layer at depth $[x, x + \mathrm{d}x]$ to the top requires work $\mathrm{d}W = \rho g\cdot9\pi\,\mathrm{d}x\cdot x$, so $W = 9\pi\rho g\int_0^5x\,\mathrm{d}x = \frac{225}{2}\pi\rho g \approx 3.46 \times 10^6\,\mathrm{J}$ ($\rho = 10^3\,\mathrm{kg/m^3}$, $g = 9.8\,\mathrm{m/s^2}$).

## 7.7. Improper Integrals

The definite integral requires a bounded interval and a bounded integrand. Dropping one of these two conditions leads to an *improper integral*: an integral over an unbounded interval, or an integral of an unbounded function. Both are defined as limits of definite integrals.

### 7.7.1. Integrals over Unbounded Intervals

**Definition 7.7.1 (Improper Integral over an Unbounded Interval)** Let $f$ be defined on $[a, +\infty)$ with $f \in \mathcal{R}[a,A]$ for every $A > a$. The expression

$$
\int_a^{+\infty}f(x)\,\mathrm{d}x = \lim_{A\to+\infty}\int_a^A f(x)\,\mathrm{d}x
$$
is called the improper integral of $f$ over $[a,+\infty)$ (whether or not the limit exists). If the limit exists, the integral is said to converge; otherwise it diverges. The integral $\int_{-\infty}^b f(x)\,\mathrm{d}x$ is defined similarly. If for some $a$ both $\int_{-\infty}^a f$ and $\int_a^{+\infty}f$ converge, then $\int_{-\infty}^{+\infty}f$ is said to converge, and $\int_{-\infty}^{+\infty}f = \int_{-\infty}^a f + \int_a^{+\infty}f$.

Both the convergence and the value of $\int_{-\infty}^{+\infty}f$ are independent of the choice of $a$ (by additivity over intervals). Note that the two ends must converge separately; this cannot be replaced by $\lim_{A\to+\infty}\int_{-A}^A f$: we have $\int_{-A}^A x\,\mathrm{d}x = 0$, yet $\int_{-\infty}^{+\infty}x\,\mathrm{d}x$ diverges.

**Example 7.7.1** Let $p > 0$. For $p = 1$, $\int_1^A\frac{\mathrm{d}x}{x} = \ln A \to +\infty$; for $p \ne 1$, $\int_1^A\frac{\mathrm{d}x}{x^p} = \frac{A^{1-p} - 1}{1-p}$. Hence

$$
\int_1^{+\infty}\frac{\mathrm{d}x}{x^p}\;\begin{cases}= \dfrac{1}{p-1}, & p > 1,\\[1ex] \text{diverges}, & 0 < p \le 1.\end{cases}
$$

Convergent improper integrals over unbounded intervals can be handled with substitution, integration by parts and the Newton–Leibniz formula as usual, provided $G(+\infty)$ is understood as $\lim_{x\to+\infty}G(x)$.

**Example 7.7.2**

1. $\int_0^{+\infty}x^3\mathrm{e}^{-x^2}\,\mathrm{d}x \overset{u = x^2}{=} \frac12\int_0^{+\infty}u\mathrm{e}^{-u}\,\mathrm{d}u = \frac12\left(-u\mathrm{e}^{-u}\Big|_0^{+\infty} + \int_0^{+\infty}\mathrm{e}^{-u}\,\mathrm{d}u\right) = \frac12$.
2. $\int_1^{+\infty}\frac{\arctan x}{x^2}\,\mathrm{d}x = -\frac{\arctan x}{x}\Big|_1^{+\infty} + \int_1^{+\infty}\frac{\mathrm{d}x}{x(1+x^2)} = \frac\pi4 + \frac12\ln\frac{x^2}{1+x^2}\Big|_1^{+\infty} = \frac\pi4 + \frac12\ln2$.

### 7.7.2. Integrals of Unbounded Functions

**Definition 7.7.2 (Improper Integral of an Unbounded Function)** Let $f$ be defined on $(a,b]$ and unbounded in every right neighborhood of $a$, with $f \in \mathcal{R}[a+\eta, b]$ for every $\eta \in (0, b-a)$. The expression

$$
\int_a^b f(x)\,\mathrm{d}x = \lim_{\eta\to0^+}\int_{a+\eta}^b f(x)\,\mathrm{d}x
$$
is called the improper integral of $f$ over $(a,b]$, and $a$ is called a **singular point** of the integral. If the limit exists, the integral is said to converge; otherwise it diverges. Integrals with singular point $b$ are defined similarly; if a singular point lies inside the interval, split the integral there and require both parts to converge.

**Example 7.7.3** Let $p > 0$ and $0 < \eta < 1$. The integral $\int_\eta^1\frac{\mathrm{d}x}{x^p}$ equals $-\ln\eta$ for $p = 1$ and $\frac{1 - \eta^{1-p}}{1-p}$ for $p \ne 1$. Letting $\eta \to 0^+$, we obtain in general

$$
\int_a^b\frac{\mathrm{d}x}{(x-a)^p}\;\begin{cases}= \dfrac{(b-a)^{1-p}}{1-p}, & 0 < p < 1,\\[1ex] \text{diverges}, & p \ge 1.\end{cases}
$$

This is the opposite of Example 7.7.1: at infinity, $x^{-p}$ must decay fast enough ($p > 1$); near a singular point, $x^{-p}$ must grow slowly enough ($p < 1$). The case $p = 1$ diverges at both ends.

![The integral of x to the power -p converges on [1, +∞) and on (0, 1] under exactly opposite conditions (left, middle); the gamma function (right)](./plots/improper-p-integrals.py)

**Example 7.7.4**

1. $\int_1^{\sqrt2}\frac{\mathrm{d}x}{x\sqrt{x^2-1}} = \lim_{\eta\to0^+}\left(-\arcsin\frac1x\right)\Big|_{1+\eta}^{\sqrt2} = \frac\pi2 - \frac\pi4 = \frac\pi4$.
2. $\int_0^1\ln x\,\mathrm{d}x = \lim_{\eta\to0^+}\left(x\ln x\Big|_\eta^1 - \int_\eta^1\mathrm{d}x\right) = -1$ (since $\eta\ln\eta \to 0$).
3. $\int_1^{\mathrm{e}}\frac{\mathrm{d}x}{x\sqrt{1 - \ln^2x}} = \lim_{\eta\to0^+}\arcsin(\ln x)\Big|_1^{\mathrm{e}-\eta} = \frac\pi2$.

**Example 7.7.5** Find $\lim_{n\to\infty}\dfrac{\sqrt[n]{n!}}{n}$.

**Solution** Taking logarithms, $\ln\frac{\sqrt[n]{n!}}{n} = \frac1n\sum_{i=1}^n\ln\frac in$, which is a Riemann sum of $\ln x$ on $(0,1]$. Since $\ln x$ is unbounded near $0$, strictly speaking the improper integral requires a separate argument ($\ln x$ is monotone, so the sum can be squeezed between upper and lower sums of a monotone function); the result is $\frac1n\sum\ln\frac in \to \int_0^1\ln x\,\mathrm{d}x = -1$, so the limit is $\mathrm{e}^{-1}$.

An improper integral of an unbounded function can be converted into one over an unbounded interval: if $a$ is the singular point, put $x = a + \frac1u$; then

$$
\int_{a+\eta}^b f(x)\,\mathrm{d}x = \int_{1/(b-a)}^{1/\eta}f\left(a + \frac1u\right)\frac{\mathrm{d}u}{u^2}, \qquad \int_a^b f(x)\,\mathrm{d}x = \int_{1/(b-a)}^{+\infty}f\left(a + \frac1u\right)\frac{\mathrm{d}u}{u^2}.
$$

The theories of the two kinds of improper integrals are therefore parallel. Below we treat integrals over unbounded intervals in detail and only state the corresponding results for unbounded functions.

### 7.7.3. Convergence Tests for Improper Integrals

Many improper integrals have no computable antiderivative; we can only decide whether they converge.

**Theorem 7.7.1 (Cauchy Criterion for Integrals over Unbounded Intervals)** The integral $\int_a^{+\infty}f(x)\,\mathrm{d}x$ converges if and only if for every $\varepsilon > 0$ there exists $M > a$ such that $\left|\int_{A_1}^{A_2}f(x)\,\mathrm{d}x\right| < \varepsilon$ whenever $A_2 > A_1 > M$.

**Proof** Let $F(A) = \int_a^A f$. Convergence means that $\lim_{A\to+\infty}F(A)$ exists; by the **Cauchy criterion** for limits of functions, this is equivalent to $|F(A_2) - F(A_1)| = \left|\int_{A_1}^{A_2}f\right| < \varepsilon$ for all sufficiently large $A_1, A_2$. $\square$

**Definition 7.7.3 (Absolute Convergence)** If $\int_a^{+\infty}|f(x)|\,\mathrm{d}x$ converges, then $\int_a^{+\infty}f(x)\,\mathrm{d}x$ is said to be **absolutely convergent**; if $\int_a^{+\infty}f$ converges but not absolutely, it is said to be **conditionally convergent**. The same definitions apply to integrals of unbounded functions.

**Theorem 7.7.2** An absolutely convergent improper integral converges.

**Proof** By the Cauchy criterion, since $\left|\int_{A_1}^{A_2}f\right| \le \int_{A_1}^{A_2}|f| < \varepsilon$. $\square$

Compare with Property 7.2.6: for definite integrals, "integrable implies absolutely integrable", and the converse fails; for improper integrals, "absolutely convergent implies convergent", and the converse fails. For example, $\int_1^{+\infty}\frac{\sin x}{x}\,\mathrm{d}x$ converges conditionally. Integration by parts gives $\int_1^A\frac{\sin x}{x}\,\mathrm{d}x = \cos1 - \frac{\cos A}{A} - \int_1^A\frac{\cos x}{x^2}\,\mathrm{d}x$, and the right-hand side converges as $A \to +\infty$ (the last integral converges absolutely); on the other hand, $|\sin x| \ge \sin^2x = \frac12(1 - \cos2x)$, and $\int_1^{+\infty}\frac{1 - \cos2x}{2x}\,\mathrm{d}x$ diverges.

From now on let $f, g$ be nonnegative on $[a,+\infty)$ and integrable on every $[a,A]$. Then $F(A) = \int_a^A f$ is nondecreasing, and the integral converges if and only if $F$ is bounded above.

**Theorem 7.7.3 (Comparison Test)** Let $0 \le f(x) \le g(x)$ for $x \ge a$. If $\int_a^{+\infty}g$ converges, then $\int_a^{+\infty}f$ converges; if $\int_a^{+\infty}f$ diverges, then $\int_a^{+\infty}g$ diverges.

**Proof** $\int_a^A f \le \int_a^A g \le \int_a^{+\infty}g$, and a nondecreasing function that is bounded above has a limit at $+\infty$. The second half is the contrapositive of the first. $\square$

**Theorem 7.7.4 (Limit Comparison Test)** Let $f \ge 0$, $g > 0$, and $\lim_{x\to+\infty}\frac{f(x)}{g(x)} = q$.

1. If $0 \le q < +\infty$ and $\int_a^{+\infty}g$ converges, then $\int_a^{+\infty}f$ converges;
2. If $0 < q \le +\infty$ and $\int_a^{+\infty}g$ diverges, then $\int_a^{+\infty}f$ diverges.

In particular, if $0 < q < +\infty$, the two integrals converge or diverge together.

**Proof** 1. There is $A$ such that $0 \le f/g < q + 1$, that is, $f < (q+1)g$, for $x > A$; the claim follows from Theorem 7.7.3 and the fact that convergence is not affected by a finite interval. 2. If $q$ is finite, there is $A$ with $f > \frac q2g$ for $x > A$; if $q = +\infty$, then $f > g$ eventually. The claim follows from Theorem 7.7.3. $\square$

Taking $g = x^{-p}$ (Example 7.7.1) as the comparison function gives the most frequently used test.

**Theorem 7.7.5 (p-Test)** Let $f \ge 0$.

1. If for some $p > 1$ the limit $\lim_{x\to+\infty}x^pf(x)$ exists (and is finite), then $\int_a^{+\infty}f$ converges;
2. If for some $p \le 1$ the limit $\lim_{x\to+\infty}x^pf(x)$ exists and is nonzero, or equals $+\infty$, then $\int_a^{+\infty}f$ diverges.

Intuitively: the integral converges when $f$ is an **infinitesimal** of higher order than $1/x$ at infinity (at least like some $x^{-p}$ with $p > 1$).

**Example 7.7.6**

1. For every $\alpha$, $\int_1^{+\infty}x^\alpha\mathrm{e}^{-x}\,\mathrm{d}x$ converges: $\lim_{x\to+\infty}x^2\cdot x^\alpha\mathrm{e}^{-x} = 0$; take $p = 2$.
2. $\int_1^{+\infty}\frac{\ln(x+2) - \ln x}{\sqrt x}\,\mathrm{d}x$ converges: $x^{3/2}\cdot\frac{\ln(1 + 2/x)}{\sqrt x} = x\ln\left(1 + \frac2x\right) \to 2$; take $p = \frac32$.
3. $\int_1^{+\infty}x^2\mathrm{e}^{-x}\sin x\,\mathrm{d}x$ converges absolutely: $x^2\cdot x^2\mathrm{e}^{-x}|\sin x| \to 0$. When the integrand changes sign, first check whether the integral of $|f|$ converges.

The corresponding results for unbounded functions: let $a$ be the singular point of $\int_a^b f$.

**Theorem 7.7.6 (Cauchy Criterion for Integrals of Unbounded Functions)** $\int_a^b f$ converges $\iff$ for every $\varepsilon > 0$ there exists $\delta \in (0, b-a)$ such that $\left|\int_{a+\eta_1}^{a+\eta_2}f(x)\,\mathrm{d}x\right| < \varepsilon$ whenever $0 < \eta_1 < \eta_2 < \delta$.

The comparison test and its limit form remain valid for integrals of unbounded functions (with $x \to +\infty$ replaced by $x \to a^+$). The comparison function becomes $(x-a)^{-p}$, and by Example 7.7.3 the direction of the condition on $p$ is reversed:

**Theorem 7.7.7 (p-Test for Integrals of Unbounded Functions)** Let $f \ge 0$, and let $a$ be the singular point.

1. If for some $p < 1$ the limit $\lim_{x\to a^+}(x-a)^pf(x)$ exists (and is finite), then $\int_a^b f$ converges;
2. If for some $p \ge 1$ the limit $\lim_{x\to a^+}(x-a)^pf(x)$ exists and is nonzero, or equals $+\infty$, then $\int_a^b f$ diverges.

**Example 7.7.7** Consider $\int_0^1\frac{\ln x}{x^\alpha}\,\mathrm{d}x$ (the integrand does not change sign on $(0,1)$, so we may apply the $p$-test to $-\ln x/x^\alpha \ge 0$):

- For $\alpha < 1$, take $p = \frac{1+\alpha}{2} \in (\alpha, 1)$; then $x^p\cdot\frac{|\ln x|}{x^\alpha} = x^{p-\alpha}|\ln x| \to 0$, so the integral converges;
- For $\alpha \ge 1$, take $p = \alpha$; then $x^\alpha\cdot\frac{|\ln x|}{x^\alpha} = |\ln x| \to +\infty$, so the integral diverges. (For $\alpha \le 0$, $0$ is not a singular point and the integral is a proper one; the conclusion "converges" still holds.)

An integral may be improper both because of an unbounded interval and because of an unbounded integrand. In that case we split it into pieces, each improper in only one way, and require every piece to converge. The two most important improper integrals with a parameter in probability theory are treated in this way.

**Definition 7.7.4 (Gamma Function)** For $s > 0$, let

$$
\Gamma(s) = \int_0^{+\infty}x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x.
$$

**Example 7.7.8** This integral converges if and only if $s > 0$. Split it into $I_1 = \int_0^1x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x$ and $I_2 = \int_1^{+\infty}x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x$. $I_2$ converges for every $s$ (Example 7.7.6). For $s < 1$, $0$ is a singular point of $I_1$; take $p = 1 - s$, so that $x^p\cdot x^{s-1}\mathrm{e}^{-x} \to 1$: the integral converges when $s > 0$, i.e. $p < 1$, and diverges when $s \le 0$, i.e. $p \ge 1$.

Basic properties of the gamma function:

1. $\Gamma(1) = 1$ and $\Gamma(s+1) = s\Gamma(s)$ (by parts: $\int_0^{+\infty}x^s\mathrm{e}^{-x}\,\mathrm{d}x = -x^s\mathrm{e}^{-x}\Big|_0^{+\infty} + s\int_0^{+\infty}x^{s-1}\mathrm{e}^{-x}\,\mathrm{d}x$);
2. Hence $\Gamma(n+1) = n!$: the gamma function extends the factorial to the positive reals;
3. $\Gamma\left(\frac12\right) = \int_0^{+\infty}x^{-1/2}\mathrm{e}^{-x}\,\mathrm{d}x \overset{x = t^2}{=} 2\int_0^{+\infty}\mathrm{e}^{-t^2}\,\mathrm{d}t = \sqrt\pi$; the last step is the **Gaussian integral**, computed with a double integral in [Chapter 12](/2.2.12).

**Definition 7.7.5 (Beta Function)** For $\alpha > 0$ and $\beta > 0$, let

$$
\mathrm{B}(\alpha,\beta) = \int_0^1x^{\alpha-1}(1-x)^{\beta-1}\,\mathrm{d}x.
$$

**Example 7.7.9** This integral converges if and only if $\alpha > 0$ and $\beta > 0$. The possible singular points are $0$ and $1$; split the integral at $\frac12$. Near $0$, take $p = 1 - \alpha$; then $x^p\cdot x^{\alpha-1}(1-x)^{\beta-1} \to 1$, so the integral converges $\iff p < 1 \iff \alpha > 0$. Near $1$, similarly with $p = 1 - \beta$, it converges $\iff \beta > 0$.

The substitution $x = 1 - t$ gives $\mathrm{B}(\alpha,\beta) = \mathrm{B}(\beta,\alpha)$, and $x = \sin^2\theta$ gives $\mathrm{B}(\alpha,\beta) = 2\int_0^{\pi/2}\sin^{2\alpha-1}\theta\cos^{2\beta-1}\theta\,\mathrm{d}\theta$; for example, $\mathrm{B}\left(\frac12,\frac12\right) = \pi$. These are integrals of the same type as the Wallis integrals. The two functions are related by $\mathrm{B}(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$, whose proof also requires double integrals ([Chapter 12](/2.2.12)).

## Summary

| Topic | Key points |
|---|---|
| Definition | Limit of Riemann sums ($\lambda \to 0$, independent of partition and choice of points); integrable $\iff \sum\omega_i\Delta x_i \to 0$ |
| Sufficient conditions for integrability | Continuous; monotone; bounded with finitely many discontinuities. The Dirichlet function is not integrable |
| Properties | Linearity, additivity over intervals, monotonicity, $\lvert\int f\rvert \le \int\lvert f\rvert$, estimates, mean value theorem for integrals (proved with the intermediate value theorem) |
| Fundamental theorem of calculus | $\left(\int_a^x f\right)' = f(x)$ ($f$ continuous); $\int_a^b f = G(b) - G(a)$ |
| Computation | Change the limits along with the variable; watch the absolute value when taking square roots; parity and periodicity; Wallis integrals $\frac{(n-1)!!}{n!!}\left(\frac\pi2\right)$ |
| Limits of sums | $\frac1n\sum f(i/n) \to \int_0^1 f$ |

| Geometric quantity | Cartesian $y = f(x)$ | Parametric $x(t), y(t)$ | Polar $r(\theta)$ |
|---|---|---|---|
| Area | $\int_a^b\lvert f - g\rvert\,\mathrm{d}x$ | $\int_\alpha^\beta y(t)x'(t)\,\mathrm{d}t$ | $\frac12\int_\alpha^\beta r^2\,\mathrm{d}\theta$ |
| Arc length | $\int_a^b\sqrt{1 + f'^2}\,\mathrm{d}x$ | $\int_\alpha^\beta\sqrt{x'^2 + y'^2}\,\mathrm{d}t$ | $\int_\alpha^\beta\sqrt{r^2 + r'^2}\,\mathrm{d}\theta$ |
| Curvature | $\frac{\lvert y''\rvert}{(1 + y'^2)^{3/2}}$ | $\frac{\lvert x'y'' - x''y'\rvert}{(x'^2 + y'^2)^{3/2}}$ | $\frac{\lvert r^2 + 2r'^2 - rr''\rvert}{(r^2 + r'^2)^{3/2}}$ |
| Volume of revolution about the $x$-axis (polar axis) | $\pi\int_a^b f^2\,\mathrm{d}x$ | $\pi\int_\alpha^\beta y^2x'\,\mathrm{d}t$ | $\frac{2\pi}{3}\int_\alpha^\beta r^3\sin\theta\,\mathrm{d}\theta$ |
| Area of surface of revolution | $2\pi\int_a^b f\sqrt{1 + f'^2}\,\mathrm{d}x$ | $2\pi\int_\alpha^\beta y\sqrt{x'^2 + y'^2}\,\mathrm{d}t$ | — |

| Improper integral | Unbounded interval $\int_a^{+\infty}f$ | Unbounded function $\int_a^b f$ (singular point $a$) |
|---|---|---|
| Benchmark | $\int_1^{+\infty}x^{-p}\,\mathrm{d}x$ converges $\iff p > 1$ | $\int_a^b(x-a)^{-p}\,\mathrm{d}x$ converges $\iff p < 1$ |
| $p$-test ($f \ge 0$) | $x^pf(x)$ has a limit, $p > 1$: converges; limit nonzero or $+\infty$, $p \le 1$: diverges | $(x-a)^pf(x)$ has a limit, $p < 1$: converges; limit nonzero or $+\infty$, $p \ge 1$: diverges |
| General functions | Cauchy criterion; absolute convergence implies convergence | Same as left |
| Gamma and beta | $\Gamma(s)$ converges $\iff s > 0$, $\Gamma(n+1) = n!$, $\Gamma(\frac12) = \sqrt\pi$ | $\mathrm{B}(\alpha,\beta)$ converges $\iff \alpha, \beta > 0$ |
