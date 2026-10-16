---
title: Isolated Singularities and Residues
---

The points where an analytic function fails to be analytic carry most of the information about it. A rational function is determined, up to an additive constant, by the principal parts of its poles. The integral of a function around a closed curve depends only on its singularities inside the curve, and the growth of an entire function at infinity determines whether it is a polynomial. This chapter uses the Laurent series of [2.3.5](/2.3.5) to classify isolated singularities into three types (removable singularities, poles and essential singularities), including the point at infinity, and characterizes each type by the behavior of $f(z)$ near the point.

The coefficient $c_{-1}$ of the Laurent series is the residue. The residue theorem turns the computation of a contour integral into the computation of finitely many residues, which is mostly algebra; the next chapter ([2.3.7](/2.3.7)) applies it to real integrals, to the inverse Fourier and Laplace transforms used in partial differential equations ([2.5.6](/2.5.6)), and to counting zeros. The word "singular point" here refers to a point where a function is not analytic; it should not be confused with the singular points of a differential equation in [2.4](/2.4), although the two are related: the singular points of a linear equation with analytic coefficients are the singularities of the coefficients.

## 6.1. Isolated Singularities

### 6.1.1. Classification by the Laurent Series

**Definition 6.1.1** If $f$ is analytic in a punctured disk $0 < \lvert z - z_0\rvert < \delta$ but not analytic at $z_0$ (possibly not defined there), then $z_0$ is called an **isolated singularity** of $f$.

For example, $0$ is an isolated singularity of $\frac{\sin z}{z}$, $\frac1{z^2}$ and $\mathrm{e}^{1/z}$. Not every singular point is isolated:

- $f(z) = \frac{1}{\sin(1/z)}$ is singular at $z = \frac{1}{k\pi}$ ($k \in \mathbb{Z}\setminus\{0\}$) and at $0$. Each $\frac1{k\pi}$ is isolated, but $0$ is not, since every disk around $0$ contains points $\frac{1}{k\pi}$.
- $\operatorname{Log} z$ is not analytic on any punctured disk around $0$, because no branch of $\log z$ is continuous on a full circle around $0$ ([2.3.3](/2.3.3)). The branch point $0$ is therefore not an isolated singularity.

At an isolated singularity, Laurent's theorem (Theorem 5.5.2) gives an expansion

$$
f(z) = \sum_{n=-\infty}^{\infty}c_n(z - z_0)^n = \underbrace{\sum_{n=1}^\infty\frac{c_{-n}}{(z - z_0)^n}}_{\text{principal part}} + \underbrace{\sum_{n=0}^\infty c_n(z - z_0)^n}_{\text{analytic part}}, \qquad 0 < \lvert z - z_0\rvert < \delta. \tag{6.1}
$$

**Definition 6.1.2** In Eq. (6.1), the sum of the negative powers is the **principal part** of $f$ at $z_0$. The isolated singularity $z_0$ is called

1. a **removable singularity** if the principal part is zero ($c_{-n} = 0$ for all $n \ge 1$);
2. a **pole** of order $m$ if the principal part has finitely many terms and $c_{-m} \ne 0$, $c_{-n} = 0$ for $n > m$; the integer $m \ge 1$ is the **order of the pole**, and a pole of order $1$ is a **simple pole**;
3. an **essential singularity** if the principal part has infinitely many nonzero terms.

The principal part is the only part of $f$ that "feels" the singularity: the analytic part is a power series, convergent in $\lvert z - z_0\rvert < \delta$. The three types have very different behavior, characterized in the next three subsections by the limit of $f(z)$ as $z \to z_0$.

### 6.1.2. Removable Singularities

**Theorem 6.1.1 (Riemann's Removable Singularity Theorem)** Let $z_0$ be an isolated singularity of $f$. The following are equivalent:

1. $z_0$ is a removable singularity;
2. $\lim_{z\to z_0}f(z)$ exists and is finite;
3. $f$ is bounded in some punctured disk $0 < \lvert z - z_0\rvert < \delta'$.

When they hold, setting $f(z_0) = c_0 = \lim_{z\to z_0}f(z)$ makes $f$ analytic at $z_0$.

**Proof** (1)$\Rightarrow$(2): $f$ equals a convergent power series in the punctured disk, whose sum is continuous at $z_0$ with value $c_0$. (2)$\Rightarrow$(3) is clear. (3)$\Rightarrow$(1): let $\lvert f\rvert \le M$ for $0 < \lvert z - z_0\rvert < \delta'$. For $n \ge 1$ and $0 < \rho < \delta'$, the coefficient formula in Eq. (5.4) and the ML inequality (Theorem 4.1.2) give

$$
\lvert c_{-n}\rvert = \left\lvert\frac{1}{2\pi\mathrm{i}}\oint_{\lvert z - z_0\rvert = \rho}f(z)(z - z_0)^{n-1}\,\mathrm{d}z\right\rvert \le \frac{1}{2\pi}\cdot M\rho^{n-1}\cdot2\pi\rho = M\rho^n.
$$

Letting $\rho \to 0$ gives $c_{-n} = 0$. $\square$

The theorem says that a singularity of a bounded analytic function is never genuine. It is used constantly to show that a quotient is in fact analytic.

**Example 6.1.1** 1. $\frac{\sin z}{z} = 1 - \frac{z^2}{6} + \cdots$ and $\frac{\mathrm{e}^z - 1}{z} = 1 + \frac z2 + \cdots$ have removable singularities at $0$, with values $1$.
2. $\frac{1}{z^2} - \frac{1}{z\sin z}$ has a removable singularity at $0$: from $\frac{z}{\sin z} = 1 + \frac{z^2}{6} + \frac{7z^4}{360} + \cdots$ we get $\frac{1}{z\sin z} = \frac{1}{z^2} + \frac16 + \frac{7z^2}{360} + \cdots$, so the difference tends to $-\frac16$.

### 6.1.3. Poles

**Theorem 6.1.2** Let $z_0$ be an isolated singularity of $f$ and $m \ge 1$. The following are equivalent:

1. $z_0$ is a pole of order $m$;
2. $f(z) = \dfrac{g(z)}{(z - z_0)^m}$ near $z_0$, where $g$ is analytic at $z_0$ and $g(z_0) \ne 0$;
3. $\lim_{z\to z_0}(z - z_0)^mf(z)$ exists, is finite and is nonzero;
4. $z_0$ is a zero of order $m$ of $\frac1f$ (after the removable singularity of $\frac1f$ at $z_0$ is removed).

In particular, $z_0$ is a pole if and only if $\lim_{z\to z_0}f(z) = \infty$.

**Proof** (1)$\Leftrightarrow$(2): multiplying Eq. (6.1) by $(z - z_0)^m$ gives $g(z) = c_{-m} + c_{-m+1}(z - z_0) + \cdots$, analytic with $g(z_0) = c_{-m}$; conversely, dividing the Taylor series of $g$ by $(z - z_0)^m$ gives a principal part ending at $c_{-m} = g(z_0) \ne 0$. (2)$\Leftrightarrow$(3) follows from Theorem 6.1.1 applied to $(z - z_0)^mf$. (2)$\Leftrightarrow$(4): $\frac1f = (z - z_0)^m\frac{1}{g}$ with $\frac1g$ analytic and nonzero at $z_0$; use Theorem 5.4.1. For the last statement: a pole gives $\lvert f\rvert = \lvert g\rvert/\lvert z - z_0\rvert^m \to \infty$; conversely, if $f \to \infty$, then $\frac1f \to 0$, so $\frac1f$ has a removable singularity with a zero at $z_0$, of some finite order $m$ by Theorem 5.4.2 (since $\frac1f \not\equiv 0$), and (4) applies. $\square$

For quotients, the order of a pole is read off from the orders of zeros:

**Theorem 6.1.3** Let $P$ and $Q$ be analytic at $z_0$ and not identically zero, where $z_0$ is a zero of order $k$ of $P$ ($k = 0$ if $P(z_0) \ne 0$) and a zero of order $l \ge 1$ of $Q$. Then $\frac{P}{Q}$ has a pole of order $l - k$ at $z_0$ if $l > k$, and a removable singularity if $l \le k$.

**Proof** Write $P = (z - z_0)^k\varphi$, $Q = (z - z_0)^l\psi$ with $\varphi(z_0), \psi(z_0) \ne 0$; then $\frac PQ = (z - z_0)^{k-l}\frac{\varphi}{\psi}$, and $\frac\varphi\psi$ is analytic and nonzero at $z_0$. $\square$

**Example 6.1.2** 1. $\frac{1}{\sin z}$, $\cot z$ and $\frac{1}{\mathrm{e}^z - 1}$ have simple poles at the simple zeros of their denominators: $z = k\pi$, $z = k\pi$ and $z = 2k\pi\mathrm{i}$ respectively ($k \in \mathbb{Z}$).
2. $\frac{z}{1 - \cos z}$ at $0$: the numerator has a zero of order $1$, and $1 - \cos z = \frac{z^2}{2} - \cdots$ a zero of order $2$; so $0$ is a simple pole.
3. $\frac{\mathrm{e}^z - 1}{z^4}$ has a pole of order $3$ at $0$, and $\frac{z - \sin z}{z^5}$ a pole of order $2$, because $z - \sin z$ has a zero of order $3$. Counting only the power in the denominator would give the wrong order.

### 6.1.4. Essential Singularities

By Theorems 6.1.1 and 6.1.2, an isolated singularity is removable if and only if $f$ has a finite limit, and a pole if and only if $f \to \infty$. The remaining case is therefore characterized by the absence of any limit:

**Theorem 6.1.4** An isolated singularity $z_0$ of $f$ is essential if and only if $\lim_{z\to z_0}f(z)$ exists neither as a finite number nor as $\infty$.

**Example 6.1.3** $0$ is an essential singularity of $\mathrm{e}^{1/z} = \sum_{n\ge0}\frac{1}{n!z^n}$. Along the positive real axis $\mathrm{e}^{1/x} \to +\infty$; along the negative real axis $\mathrm{e}^{1/x} \to 0$; on the imaginary axis $\lvert\mathrm{e}^{1/(\mathrm{i}y)}\rvert = 1$. Similarly $\sin\frac1z$ and $\cos\frac1z$ have essential singularities at $0$.

Near an essential singularity, the behavior is in fact as wild as possible:

**Theorem 6.1.5 (Casorati–Weierstrass Theorem)** If $z_0$ is an essential singularity of $f$, then for every $A \in \mathbb{C}$ there is a sequence $z_n \to z_0$ with $f(z_n) \to A$. Equivalently, the image of every punctured disk $0 < \lvert z - z_0\rvert < \delta$ is dense in $\mathbb{C}$.

**Proof** Suppose not: then there are $A \in \mathbb{C}$, $\varepsilon > 0$ and $\delta > 0$ such that $\lvert f(z) - A\rvert \ge \varepsilon$ for $0 < \lvert z - z_0\rvert < \delta$. The function $g(z) = \frac{1}{f(z) - A}$ is analytic and bounded by $\frac1\varepsilon$ there, so by Theorem 6.1.1 $z_0$ is a removable singularity of $g$. If $g(z_0) \ne 0$, then $f = A + \frac1g$ has a finite limit at $z_0$; if $g(z_0) = 0$, then $f \to \infty$. Either way $z_0$ is not essential, a contradiction. $\square$

A much deeper result, which we state without proof, says that density can be replaced by equality with at most one exception:

**Theorem 6.1.6 (Picard's Great Theorem)** In every punctured neighborhood of an essential singularity, $f$ takes every complex value infinitely often, with at most one exception.

**Example 6.1.4** For $\mathrm{e}^{1/z}$ the exceptional value is $0$. For any $w \ne 0$, the equation $\mathrm{e}^{1/z} = w$ means $\frac1z = \operatorname{Log}w + 2k\pi\mathrm{i}$, and its solutions

$$
z_k = \frac{1}{\operatorname{Log}w + 2k\pi\mathrm{i}}, \qquad k \in \mathbb{Z},
$$

tend to $0$ as $\lvert k\rvert \to \infty$. Thus every nonzero value is taken infinitely often in every disk around $0$.

![Domain coloring of 1/z^2 (left) and e^{1/z} (right) near 0: the hue shows the argument of f(z), the bright bands are level sets of log2 |f(z)|. Around the pole of order 2 every color appears twice and the modulus grows uniformly; near the essential singularity the colors and bands crowd together and every value is taken infinitely often. White dots: solutions of e^{1/z} = 1 + i, which accumulate at 0](./plots/singularity-types.py)

The classification is summarized as follows.

| Type at $z_0$ | Principal part of the Laurent series | Behavior of $f(z)$ as $z \to z_0$ |
|---|---|---|
| Removable singularity | $0$ | Finite limit; $f$ bounded nearby |
| Pole of order $m$ | Finite, ending at $c_{-m}(z - z_0)^{-m}$ | $f \to \infty$; $(z - z_0)^mf \to c_{-m} \ne 0$ |
| Essential singularity | Infinitely many terms | No limit; image of each punctured disk dense (Casorati–Weierstrass) |

## 6.2. The Point at Infinity

### 6.2.1. Classification at Infinity

The behavior of $f$ for large $\lvert z\rvert$ is studied by regarding $\infty$ as a point of the extended plane $\hat{\mathbb{C}}$ and substituting $z = \frac1w$.

**Definition 6.2.1** If $f$ is analytic in $R < \lvert z\rvert < \infty$ for some $R \ge 0$, then $\infty$ is called an isolated singularity of $f$. Its type (removable, pole of order $m$, essential) is defined to be the type of the isolated singularity $w = 0$ of $g(w) = f\left(\frac1w\right)$.

In terms of the Laurent series of $f$ in the annulus $R < \lvert z\rvert < \infty$,

$$
f(z) = \sum_{n=-\infty}^{\infty}c_nz^n, \qquad g(w) = \sum_{n=-\infty}^{\infty}c_nw^{-n},
$$

the principal part at $\infty$ consists of the positive powers $\sum_{n\ge1}c_nz^n$. Hence $\infty$ is removable if $f$ has no positive powers (equivalently, $f$ has a finite limit as $z \to \infty$); a pole of order $m$ if the highest power is $c_mz^m$ with $c_m \ne 0$ (equivalently, $f \to \infty$); and essential if there are infinitely many positive powers (equivalently, $f$ has no limit, finite or infinite).

**Example 6.2.1** 1. A polynomial of degree $m \ge 1$ has a pole of order $m$ at $\infty$.
2. A rational function $\frac{P}{Q}$ has a removable singularity at $\infty$ if $\deg P \le \deg Q$ and a pole of order $\deg P - \deg Q$ otherwise.
3. $\mathrm{e}^z$, $\sin z$, $\cos z$ have essential singularities at $\infty$: their Maclaurin series are also their Laurent series in $0 < \lvert z\rvert < \infty$.
4. $z^2\mathrm{e}^{1/z} = z^2 + z + \frac12 + \frac{1}{6z} + \cdots$ has a pole of order $2$ at $\infty$ (and an essential singularity at $0$).
5. $\tan z$ and $\frac{1}{\sin z}$: the poles $\frac\pi2 + k\pi$ (respectively $k\pi$) tend to $\infty$, so $\infty$ is not an isolated singularity.

**Example 6.2.2** Find and classify all singularities in $\hat{\mathbb{C}}$ of

$$
f(z) = z\,\mathrm{e}^{1/(z-1)} + \frac{1}{z^2} - \frac{1}{z\sin z}.
$$

The first term is analytic except at $z = 1$; the other two are analytic except at the zeros $z = k\pi$ of $z\sin z$ ($k \in \mathbb{Z}$).

- $z = 0$: the first term is analytic there and the other two combine into a removable singularity (Example 6.1.1). So $0$ is a removable singularity.
- $z = k\pi$, $k \ne 0$: $z\sin z$ has a simple zero, so $\frac{1}{z\sin z}$ has a simple pole, while the other terms are analytic. So each $k\pi$ is a simple pole.
- $z = 1$: $z\,\mathrm{e}^{1/(z-1)}$ has infinitely many negative powers of $z - 1$ (Example 5.5.4), and the other terms are analytic at $1$. So $1$ is an essential singularity.
- $z = \infty$: the poles $k\pi$ accumulate at $\infty$, so $\infty$ is a non-isolated singularity.

Note that a sum may have a better singularity than its summands (at $0$), but never a better one at a point where only one summand is singular.

### 6.2.2. Entire and Rational Functions

For an **entire function** $f(z) = \sum_{n\ge0}c_nz^n$, the Maclaurin series converges in all of $\mathbb{C}$ and is therefore also the Laurent series at $\infty$. Its principal part at $\infty$ is $\sum_{n\ge1}c_nz^n$, and the type of $\infty$ determines what kind of function $f$ is:

**Theorem 6.2.1** Let $f$ be entire. Then

1. $\infty$ is a removable singularity of $f$ if and only if $f$ is constant;
2. $\infty$ is a pole of order $m$ if and only if $f$ is a polynomial of degree $m$;
3. otherwise $\infty$ is an essential singularity (and $f$ is called a transcendental entire function).

Part 1 contains **Liouville's theorem** (Theorem 4.5.2): a bounded entire function has a removable singularity at $\infty$ (Theorem 6.1.1 applied to $f(1/w)$) and is therefore constant. The following generalization is the standard tool for "find all entire functions such that…" problems.

**Theorem 6.2.2 (Generalized Liouville Theorem)** Let $f$ be entire, and suppose there are constants $M, R_0 > 0$ and an integer $m \ge 0$ such that $\lvert f(z)\rvert \le M\lvert z\rvert^m$ for $\lvert z\rvert \ge R_0$. Then $f$ is a polynomial of degree at most $m$.

**Proof** By the coefficient formula in Eq. (5.2) on the circle $\lvert z\rvert = \rho \ge R_0$,

$$
\lvert c_n\rvert \le \frac{1}{2\pi}\cdot\frac{M\rho^m}{\rho^{n+1}}\cdot2\pi\rho = M\rho^{m-n}.
$$

For $n > m$ the right side tends to $0$ as $\rho \to \infty$, so $c_n = 0$. $\square$

**Example 6.2.3** Find all entire functions with $\lvert f(z)\rvert \le \lvert z\rvert^2$ for all $z \in \mathbb{C}$ and $f(1 + \mathrm{i}) = \mathrm{i}$.

The function $g(z) = \frac{f(z)}{z^2}$ is analytic in $0 < \lvert z\rvert < \infty$ and bounded by $1$. By Theorem 6.1.1 its singularity at $0$ is removable, so $g$ is entire and bounded, hence a constant $c$ with $\lvert c\rvert \le 1$. Thus $f(z) = cz^2$, and $f(1 + \mathrm{i}) = 2\mathrm{i}c = \mathrm{i}$ gives $c = \frac12$. The only such function is $f(z) = \frac{z^2}{2}$ (and $\lvert c\rvert = \frac12 \le 1$, so it satisfies the inequality).

**Example 6.2.4** Bounds on the real or imaginary part also force rigidity, after composing with a suitable function.

1. If $f$ is entire and $\operatorname{Re}f(z) \le M$ for all $z$, then $\lvert\mathrm{e}^{f(z)}\rvert = \mathrm{e}^{\operatorname{Re}f(z)} \le \mathrm{e}^M$, so $\mathrm{e}^f$ is constant; then $f'\mathrm{e}^f = 0$ gives $f' = 0$, and $f$ is constant.
2. If $f$ is entire and $\operatorname{Im}f(z) \ge -1$, then $\lvert f(z) + 2\mathrm{i}\rvert \ge \operatorname{Im}f(z) + 2 \ge 1$, so $\frac{1}{f + 2\mathrm{i}}$ is a bounded entire function, and $f$ is constant.
3. Find all entire $f$ with $0 \le \operatorname{Re}f'(z) \le 1$ for all $z$. By part 1 applied to $f'$, $f'$ is a constant $a$ with $0 \le \operatorname{Re}a \le 1$. Hence the set of such functions is $\{az + b : b \in \mathbb{C},\ 0 \le \operatorname{Re}a \le 1\}$, and every function of this form clearly qualifies.

**Definition 6.2.2** A function that is analytic on a domain $D$ except at isolated singularities, all of which are poles, is said to be meromorphic on $D$. A function meromorphic on $\mathbb{C}$ is called a **meromorphic function**.

Rational functions, $\tan z$ and $\frac{1}{\mathrm{e}^z - 1}$ are meromorphic functions; $\mathrm{e}^{1/z}$ is not. Allowing $\infty$ as well characterizes the rational functions:

**Theorem 6.2.3** If $f$ is analytic in $\hat{\mathbb{C}}$ except for poles (with $\infty$ either a pole or a removable singularity), then $f$ is a rational function, and it equals the sum of its principal parts at the finite poles, plus the polynomial principal part at $\infty$, plus a constant.

**Proof** Since $\infty$ is at worst an isolated singularity, $f$ is analytic in some annulus $R < \lvert z\rvert < \infty$, so all finite poles lie in some disk $\lvert z\rvert \le R$; they cannot accumulate at a finite point either (an accumulation point would be a non-isolated singularity), so there are finitely many, $a_1, \dots, a_k$. Let $P_j(z)$ be the principal part at $a_j$, a polynomial in $\frac{1}{z - a_j}$, and $P_\infty(z)$ the principal part at $\infty$, a polynomial in $z$ without constant term. Then $h = f - P_\infty - \sum_jP_j$ has only removable singularities in $\mathbb{C}$, and at $\infty$ each $P_j \to 0$ while $f - P_\infty$ has a finite limit. So $h$ is a bounded entire function, hence constant by Liouville's theorem. $\square$

This theorem is the complex-analytic meaning of the partial fraction decomposition.

## 6.3. Residues

### 6.3.1. The Residue Theorem

**Definition 6.3.1** Let $z_0 \in \mathbb{C}$ be an isolated singularity of $f$, with Laurent series as in Eq. (6.1). The **residue** of $f$ at $z_0$ is

$$
\operatorname{Res}(f, z_0) = c_{-1} = \frac{1}{2\pi\mathrm{i}}\oint_{\lvert z - z_0\rvert = \rho}f(z)\,\mathrm{d}z, \qquad 0 < \rho < \delta.
$$

The second equality is Eq. (5.4) with $n = -1$; it explains the name: when $f$ is integrated around $z_0$, every term of the Laurent series integrates to $0$ except $c_{-1}(z - z_0)^{-1}$, which leaves the "residue" $2\pi\mathrm{i}\,c_{-1}$.

**Theorem 6.3.1 (Residue Theorem)** Let $C$ be a positively oriented, piecewise smooth simple closed curve, and let $f$ be analytic on $C$ and inside $C$ except at finitely many isolated singularities $z_1, \dots, z_n$ inside $C$. Then

$$
\oint_Cf(z)\,\mathrm{d}z = 2\pi\mathrm{i}\sum_{k=1}^n\operatorname{Res}(f, z_k). \tag{6.2}
$$

**Proof** Surround each $z_k$ by a small positively oriented circle $C_k$ inside $C$, the circles being disjoint. In the multiply connected region between $C$ and the $C_k$, $f$ is analytic, so by Cauchy's integral theorem for multiply connected domains ([2.3.4](/2.3.4)), $\oint_Cf\,\mathrm{d}z = \sum_k\oint_{C_k}f\,\mathrm{d}z = \sum_k2\pi\mathrm{i}\operatorname{Res}(f, z_k)$. $\square$

Cauchy's integral theorem ($f$ analytic inside: all residues zero) and **Cauchy's integral formula** (the residue of $\frac{f(z)}{z - z_0}$ at $z_0$ is $f(z_0)$) are special cases.

### 6.3.2. Computing Residues

At an essential singularity the residue must be read off from the Laurent series. At poles there are formulas that avoid the series.

**Theorem 6.3.2** Let $z_0 \in \mathbb{C}$ be an isolated singularity of $f$.

1. If $z_0$ is removable, $\operatorname{Res}(f, z_0) = 0$.
2. If $z_0$ is a simple pole, $\operatorname{Res}(f, z_0) = \lim_{z\to z_0}(z - z_0)f(z)$.
3. If $f = \frac PQ$ with $P$, $Q$ analytic at $z_0$, $P(z_0) \ne 0$, $Q(z_0) = 0$ and $Q'(z_0) \ne 0$, then $\operatorname{Res}(f, z_0) = \dfrac{P(z_0)}{Q'(z_0)}$.
4. If $z_0$ is a pole of order at most $m$, then

$$
\operatorname{Res}(f, z_0) = \frac{1}{(m-1)!}\lim_{z\to z_0}\frac{\mathrm{d}^{m-1}}{\mathrm{d}z^{m-1}}\left[(z - z_0)^mf(z)\right]. \tag{6.3}
$$

**Proof** 1 is the definition. For 4, $(z - z_0)^mf(z) = c_{-m} + c_{-m+1}(z - z_0) + \cdots + c_{-1}(z - z_0)^{m-1} + \cdots$ is analytic at $z_0$ (some leading coefficients may vanish if the order is less than $m$), and its $(m-1)$-th derivative at $z_0$ is $(m-1)!\,c_{-1}$. Case 2 is $m = 1$. For 3, $z_0$ is a simple pole and $(z - z_0)\frac{P(z)}{Q(z)} = \frac{P(z)}{(Q(z) - Q(z_0))/(z - z_0)} \to \frac{P(z_0)}{Q'(z_0)}$. $\square$

Eq. (6.3) remains valid if $m$ is larger than the true order, which is convenient when the exact order is tedious to determine; but the differentiation becomes longer. If $f$ is even, $f(-z) = f(z)$, then its Laurent series at $0$ has only even powers and $\operatorname{Res}(f, 0) = 0$.

**Example 6.3.1** 1. $f(z) = \frac{\mathrm{e}^z}{z^2(z-1)}$. At the simple pole $1$: $\operatorname{Res}(f, 1) = \frac{\mathrm{e}^z}{z^2}\big|_{z=1} = \mathrm{e}$. At the pole of order $2$ at $0$:

$$
\operatorname{Res}(f, 0) = \frac{\mathrm{d}}{\mathrm{d}z}\frac{\mathrm{e}^z}{z - 1}\bigg|_{z=0} = \frac{\mathrm{e}^z(z - 2)}{(z-1)^2}\bigg|_{z=0} = -2.
$$

Hence $\oint_{\lvert z\rvert = 2}f\,\mathrm{d}z = 2\pi\mathrm{i}(\mathrm{e} - 2)$, while $\oint_{\lvert z\rvert = 1/2}f\,\mathrm{d}z = -4\pi\mathrm{i}$.
2. $\cot z = \frac{\cos z}{\sin z}$ at $k\pi$: by rule 3, $\operatorname{Res}(\cot z, k\pi) = \frac{\cos k\pi}{\cos k\pi} = 1$.
3. $\frac{1}{z^4 + 1}$ at a root $z_k$ of $z^4 = -1$: $\operatorname{Res} = \frac{1}{4z_k^3} = \frac{z_k}{4z_k^4} = -\frac{z_k}{4}$.
4. $\frac{z}{1 - \cos z}$ at the simple pole $0$ (Example 6.1.2): $\lim_{z\to0}\frac{z^2}{1 - \cos z} = 2$, so the residue is $2$.
5. $z^2\sin\frac1z = z^2\left(\frac1z - \frac{1}{6z^3} + \frac{1}{120z^5} - \cdots\right) = z - \frac{1}{6z} + \cdots$ at the essential singularity $0$: the residue is $-\frac16$.
6. For the function of Example 6.2.2: $\operatorname{Res}(f, 0) = 0$ (removable). At $k\pi$ ($k \ne 0$), rule 3 applied to $-\frac{1}{z\sin z}$ gives $-\frac{1}{(\sin z + z\cos z)|_{z=k\pi}} = -\frac{(-1)^k}{k\pi}$. At the essential singularity $1$, Example 5.5.4 gives $\operatorname{Res}(f, 1) = c_{-1} = \frac32$.

### 6.3.3. The Residue at Infinity

**Definition 6.3.2** Let $\infty$ be an isolated singularity of $f$, with Laurent series $\sum c_nz^n$ in $R < \lvert z\rvert < \infty$. The residue of $f$ at $\infty$ is

$$
\operatorname{Res}(f, \infty) = \frac{1}{2\pi\mathrm{i}}\oint_{C^-}f(z)\,\mathrm{d}z = -c_{-1},
$$

where $C^-$ is a circle $\lvert z\rvert = \rho > R$ traversed clockwise (so that the neighborhood of $\infty$ is on the left).

Two warnings. First, the residue at $\infty$ is minus the coefficient of $z^{-1}$, not of a positive power. Second, it can be nonzero even when $\infty$ is removable: $\operatorname{Res}\left(\frac1z, \infty\right) = -1$. Substituting $z = \frac1w$ in the integral gives the practical formulas

$$
\operatorname{Res}(f, \infty) = -\operatorname{Res}\left(\frac{1}{w^2}f\left(\frac1w\right), 0\right); \qquad \operatorname{Res}(f, \infty) = -\lim_{z\to\infty}zf(z) \ \text{ if } f(z) \to 0 \text{ as } z \to \infty.
$$

In particular, if $f(z) = O(z^{-2})$ at $\infty$, then $\operatorname{Res}(f, \infty) = 0$.

**Theorem 6.3.3** If $f$ is analytic in $\mathbb{C}$ except at finitely many isolated singularities $z_1, \dots, z_n$, then the sum of all residues in $\hat{\mathbb{C}}$ vanishes:

$$
\sum_{k=1}^n\operatorname{Res}(f, z_k) + \operatorname{Res}(f, \infty) = 0.
$$

**Proof** Take $\rho$ so large that all $z_k$ lie inside $\lvert z\rvert = \rho$. By the residue theorem the counterclockwise integral equals $2\pi\mathrm{i}\sum_k\operatorname{Res}(f, z_k)$, and by definition the clockwise integral equals $2\pi\mathrm{i}\operatorname{Res}(f, \infty)$. $\square$

The theorem replaces many residues inside a curve by the few residues outside it.

**Example 6.3.2** Compute $\oint_{\lvert z\rvert = 2}\frac{z^{15}}{(z^2+1)^2(z^4+2)^3}\,\mathrm{d}z$.

All singularities, $\pm\mathrm{i}$ (poles of order $2$) and the four roots of $z^4 = -2$ (poles of order $3$, with modulus $2^{1/4}$), lie inside the circle; computing their residues directly would be laborious. Outside there is only $\infty$. The denominator has degree $16$, so $zf(z) \to 1$ and $\operatorname{Res}(f, \infty) = -1$. Hence the integral is $-2\pi\mathrm{i}\operatorname{Res}(f, \infty) = 2\pi\mathrm{i}$.

**Example 6.3.3** Compute $I = \oint_{\lvert z\rvert = 2}\frac{z^2\,\mathrm{e}^{1/z}}{(z-1)(z-3)}\,\mathrm{d}z$.

Inside the circle there are the essential singularity $0$ and the simple pole $1$. Outside there are the simple pole $3$ and $\infty$, so $I = -2\pi\mathrm{i}\left[\operatorname{Res}(f, 3) + \operatorname{Res}(f, \infty)\right]$. First, $\operatorname{Res}(f, 3) = \frac{9\,\mathrm{e}^{1/3}}{2}$. For $\lvert z\rvert > 3$,

$$
f(z) = \mathrm{e}^{1/z}\left(1 - \frac1z\right)^{-1}\left(1 - \frac3z\right)^{-1} = \left(1 + \frac1z + \cdots\right)\left(1 + \frac1z + \cdots\right)\left(1 + \frac3z + \cdots\right) = 1 + \frac5z + \cdots,
$$

so $\operatorname{Res}(f, \infty) = -5$. Therefore $I = -2\pi\mathrm{i}\left(\frac92\mathrm{e}^{1/3} - 5\right) = (10 - 9\,\mathrm{e}^{1/3})\pi\mathrm{i}$. The residue at the essential singularity $0$ was never needed.

**Example 6.3.4** The only finite singularity of $z\,\mathrm{e}^{1/(z-1)}$ is $1$, with residue $\frac32$ (Example 5.5.4). By Theorem 6.3.3, $\operatorname{Res}\left(z\,\mathrm{e}^{1/(z-1)}, \infty\right) = -\frac32$; one can confirm this by expanding $\frac{1}{w^2}f\left(\frac1w\right)$ at $w = 0$.

## Summary

| Topic | Key facts |
|---|---|
| Removable singularity | Bounded near $z_0$ $\Leftrightarrow$ finite limit $\Leftrightarrow$ no principal part (Riemann) |
| Pole of order $m$ | $f = g/(z - z_0)^m$, $g(z_0) \ne 0$ $\Leftrightarrow$ $f \to \infty$; for $P/Q$ subtract the orders of the zeros |
| Essential singularity | No limit; Casorati–Weierstrass, Picard |
| Point at infinity | Type of $f(1/w)$ at $0$; principal part = positive powers; entire $f$: constant / polynomial / transcendental |
| Liouville type results | $\lvert f\rvert \le M\lvert z\rvert^m$ $\Rightarrow$ polynomial of degree $\le m$; bounded real or imaginary part $\Rightarrow$ constant |
| Residue | $\operatorname{Res}(f, z_0) = c_{-1}$; simple pole: $\lim(z - z_0)f$ or $P/Q'$; order $m$: Eq. (6.3); essential: Laurent series |
| Residue theorem | $\oint_Cf\,\mathrm{d}z = 2\pi\mathrm{i}\sum\operatorname{Res}$ inside $C$ |
| Residue at $\infty$ | $-c_{-1}$; sum of all residues in $\hat{\mathbb{C}}$ is $0$ |
