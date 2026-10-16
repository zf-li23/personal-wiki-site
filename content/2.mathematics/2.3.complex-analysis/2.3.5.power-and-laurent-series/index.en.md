---
title: Power Series and Laurent Series
---

In real analysis a function can be infinitely differentiable without being the sum of its Taylor series, and the radius of convergence of a Taylor series is often hard to explain from the real line alone ([2.2.9](/2.2.9)). In the complex plane both puzzles disappear. Cauchy's integral formula ([2.3.4](/2.3.4)) shows that an analytic function is, near every point, the sum of a convergent **power series**, and that the series converges in the largest disk on which the function stays analytic. Analyticity is therefore a local power series property, which in turn yields the isolation of zeros and the identity theorem: an analytic function on a domain is determined by its values on any set with a limit point.

Near a point where a function fails to be analytic, power series are no longer enough, and we need series with negative powers as well. These Laurent series converge in annuli, and their coefficients are given by contour integrals. The coefficient of $(z - z_0)^{-1}$ is the residue of the next chapter ([2.3.6](/2.3.6)), which drives all the applications in [2.3.7](/2.3.7). The material on real power series in [2.2.9](/2.2.9) is assumed; most proofs carry over verbatim once absolute values are read as moduli.

## 5.1. Series of Complex Numbers and Functions

### 5.1.1. Complex Series

**Definition 5.1.1** Let $z_n = a_n + \mathrm{i}b_n$ be complex numbers. The series $\sum_{n=1}^\infty z_n$ is said to converge to $S$ if its partial sums $S_n = \sum_{k=1}^n z_k$ satisfy $\lvert S_n - S\rvert \to 0$; otherwise it diverges. The series is **absolutely convergent** if $\sum\lvert z_n\rvert$ converges, and **conditionally convergent** if it converges but not absolutely.

Since $\max(\lvert a_n\rvert, \lvert b_n\rvert) \le \lvert z_n\rvert \le \lvert a_n\rvert + \lvert b_n\rvert$, convergence questions reduce to real series:

**Theorem 5.1.1** 1. $\sum z_n$ converges if and only if both $\sum a_n$ and $\sum b_n$ converge, and then $\sum z_n = \sum a_n + \mathrm{i}\sum b_n$.
2. If $\sum z_n$ converges, then $z_n \to 0$.
3. An absolutely convergent series converges, and its terms may be rearranged without changing the sum.

The **Cauchy criterion**, the comparison, ratio and root tests for $\sum \lvert z_n\rvert$, and the **Cauchy product** of two absolutely convergent series hold exactly as for real series. **Dirichlet's test** also holds for complex $b_n$: if the real numbers $a_n$ decrease monotonically to $0$ and the partial sums of $\sum b_n$ are bounded, then $\sum a_nb_n$ converges (the proof by Abel summation in [2.2.8](/2.2.8) uses only the triangle inequality).

**Example 5.1.1** For $\theta \notin 2\pi\mathbb{Z}$ the partial sums of $\sum_{n\ge1}\mathrm{e}^{\mathrm{i}n\theta}$ are bounded:

$$
\left\lvert\sum_{k=1}^n \mathrm{e}^{\mathrm{i}k\theta}\right\rvert = \left\lvert\frac{\mathrm{e}^{\mathrm{i}\theta}(1 - \mathrm{e}^{\mathrm{i}n\theta})}{1 - \mathrm{e}^{\mathrm{i}\theta}}\right\rvert \le \frac{2}{\lvert 1 - \mathrm{e}^{\mathrm{i}\theta}\rvert} = \frac{1}{\lvert\sin(\theta/2)\rvert}.
$$

Hence $\sum_{n\ge1}\frac{\mathrm{e}^{\mathrm{i}n\theta}}{n^p}$ converges for every $p > 0$ and $\theta \notin 2\pi\mathbb{Z}$; it converges absolutely only for $p > 1$. This bound is used repeatedly below when we study power series on their circle of convergence.

### 5.1.2. Series of Functions and Uniform Convergence

For a **series of functions** $\sum f_n(z)$ on a set $E \subseteq \mathbb{C}$, pointwise convergence, **uniform convergence** and the **Weierstrass M-test** are defined and proved as in [2.2.9](/2.2.9): if $\lvert f_n(z)\rvert \le M_n$ on $E$ and $\sum M_n < \infty$, the series converges absolutely and uniformly on $E$. A uniform limit of continuous functions is continuous, and a uniformly convergent series of continuous functions can be integrated term by term along any piecewise smooth curve $\gamma \subseteq E$, because $\left\lvert\int_\gamma g\,\mathrm{d}z\right\rvert \le L(\gamma)\sup_\gamma\lvert g\rvert$.

For analytic functions much more is true. The natural mode of convergence is **uniform convergence on compact subsets** (uniform convergence on every compact subset of the domain, equivalently on every closed disk contained in it), and it is preserved under differentiation without any extra hypothesis.

**Theorem 5.1.2 (Weierstrass)** Let $f_n$ be analytic on a domain $D$, and let $\sum f_n$ converge uniformly on compact subsets of $D$ to $f$. Then $f$ is analytic on $D$, and for every $k \ge 1$ the differentiated series $\sum f_n^{(k)}$ converges to $f^{(k)}$ uniformly on compact subsets of $D$.

**Proof** Let $\overline{D(z_0, r)} \subseteq D$. On this closed disk $f$ is a uniform limit of continuous functions, hence continuous. For every closed triangle $\Delta$ in $D(z_0, r)$, term-by-term integration and **Cauchy's integral theorem** give $\oint_{\partial\Delta} f\,\mathrm{d}z = \sum_n\oint_{\partial\Delta} f_n\,\mathrm{d}z = 0$, so $f$ is analytic in $D(z_0, r)$ by **Morera's theorem**. For the derivatives, let $C$ be the circle $\lvert \zeta - z_0\rvert = r$ and $\lvert z - z_0\rvert \le r/2$. By **Cauchy's integral formula** for derivatives (Theorem 4.4.2),

$$
\left\lvert f^{(k)}(z) - \sum_{n=1}^N f_n^{(k)}(z)\right\rvert = \left\lvert\frac{k!}{2\pi\mathrm{i}}\oint_C\frac{f(\zeta) - \sum_{n=1}^N f_n(\zeta)}{(\zeta - z)^{k+1}}\,\mathrm{d}\zeta\right\rvert \le \frac{k!\,2^{k+1}}{r^k}\sup_{\zeta\in C}\left\lvert f(\zeta) - \sum_{n=1}^N f_n(\zeta)\right\rvert,
$$

which tends to $0$ uniformly in $\lvert z - z_0\rvert \le r/2$. Every compact subset of $D$ is covered by finitely many such half-size disks. $\square$

The contrast with real analysis is striking: on $\mathbb{R}$ the Weierstrass approximation theorem shows that uniform limits of polynomials can be nowhere differentiable, while in $\mathbb{C}$ the uniform limit of analytic functions is automatically analytic.

## 5.2. Power Series

### 5.2.1. Abel's Theorem and the Radius of Convergence

**Definition 5.2.1** A series of the form

$$
\sum_{n=0}^\infty c_n(z - z_0)^n = c_0 + c_1(z - z_0) + c_2(z - z_0)^2 + \cdots, \qquad c_n \in \mathbb{C},
$$

is called a (complex) power series with center $z_0$ and coefficients $c_n$.

By the substitution $w = z - z_0$ we may take $z_0 = 0$. The basic fact is the same as on the real line:

**Theorem 5.2.1 (Abel's Theorem)** If $\sum c_nz^n$ converges at $z_1 \ne 0$, then it converges absolutely for every $\lvert z\rvert < \lvert z_1\rvert$, and uniformly on every closed disk $\lvert z\rvert \le \rho$ with $\rho < \lvert z_1\rvert$. Consequently, if it diverges at $z_2$, it diverges for every $\lvert z\rvert > \lvert z_2\rvert$.

**Proof** The terms $c_nz_1^n$ tend to $0$, so $\lvert c_nz_1^n\rvert \le M$. For $\lvert z\rvert \le \rho < \lvert z_1\rvert$ we get $\lvert c_nz^n\rvert \le M(\rho/\lvert z_1\rvert)^n$, a convergent **geometric series**; the Weierstrass M-test gives absolute and uniform convergence. $\square$

Let $R = \sup\{\lvert z\rvert : \sum c_nz^n \text{ converges}\}$ (possibly $0$ or $+\infty$). Abel's theorem shows that the series converges absolutely in the open disk $\lvert z\rvert < R$ and diverges for $\lvert z\rvert > R$, so the **domain of convergence** is the disk together with some subset of its boundary circle.

**Definition 5.2.2** The number $R \in [0, +\infty]$ above is the **radius of convergence** of the power series; for $0 < R < \infty$ the disk $D(z_0, R)$ is its **disk of convergence** and the circle $\lvert z - z_0\rvert = R$ its **circle of convergence**.

**Theorem 5.2.2 (Cauchy–Hadamard Formula)** The radius of convergence of $\sum c_n(z - z_0)^n$ is

$$
R = \frac{1}{\limsup_{n\to\infty}\sqrt[n]{\lvert c_n\rvert}}, \tag{5.1}
$$

with $1/0 = +\infty$ and $1/\infty = 0$. If $\lim\lvert c_{n+1}/c_n\rvert = \rho$ exists, then also $R = 1/\rho$.

**Proof** Apply the root test to $\sum\lvert c_n\rvert\lvert z - z_0\rvert^n$: $\limsup\sqrt[n]{\lvert c_n\rvert\lvert z - z_0\rvert^n} = \lvert z - z_0\rvert/R$, which is $< 1$ for $\lvert z - z_0\rvert < R$ (absolute convergence) and $> 1$ for $\lvert z - z_0\rvert > R$ (then infinitely many terms have modulus $\ge 1$, so the terms do not tend to $0$). The ratio form follows because $\lim\lvert c_{n+1}/c_n\rvert = \rho$ implies $\lim\sqrt[n]{\lvert c_n\rvert} = \rho$. $\square$

The $\limsup$ form is needed for series with gaps, where the ratio of consecutive coefficients is undefined.

**Example 5.2.1** 1. $\sum_{n\ge1}\frac{n^n}{n!}z^{2n}$. Only even powers occur: the coefficient of $z^k$ is $c_{2n} = \frac{n^n}{n!}$ and $c_{2n+1} = 0$. By Stirling's formula $\sqrt[n]{n^n/n!} \to \mathrm{e}$, hence $\limsup\sqrt[k]{\lvert c_k\rvert} = \lim\left(\frac{n^n}{n!}\right)^{1/(2n)} = \sqrt{\mathrm{e}}$ and $R = \mathrm{e}^{-1/2}$. Equivalently, set $w = z^2$: the series in $w$ has radius $1/\mathrm{e}$, so it converges for $\lvert z\rvert^2 < 1/\mathrm{e}$.
2. $\sum_{n\ge0} 2^{n^2}z^{n^2}$: $\sqrt[k]{\lvert c_k\rvert}$ equals $2^{n}$ for $k = n^2$ and $0$ otherwise, so the $\limsup$ is $+\infty$ and $R = 0$.
3. $\sum_{n\ge1}(1 - \mathrm{i})^n n^{-2} z^n$: $\sqrt[n]{\lvert c_n\rvert} = \sqrt2\,n^{-2/n} \to \sqrt2$, so $R = 1/\sqrt2$.

### 5.2.2. Behavior on the Circle of Convergence

On the circle of convergence the radius gives no information: the series may converge absolutely everywhere, diverge everywhere, or behave differently at different points.

**Example 5.2.2** All three series below have $R = 1$.

1. $\sum z^n$ diverges at every point of $\lvert z\rvert = 1$, since its terms have modulus $1$.
2. $\sum \frac{z^n}{n}$ diverges at $z = 1$ (the harmonic series) and converges conditionally at every other point $z = \mathrm{e}^{\mathrm{i}\theta}$ of the circle, by Dirichlet's test and Example 5.1.1.
3. $\sum \frac{z^n}{n^2}$ converges absolutely on the whole circle, since $\sum\frac1{n^2} < \infty$.

To classify the convergence at a point $z^*$ of the circle (absolute convergence, conditional convergence or divergence) we first look at $\sum\lvert c_n\rvert R^n$; if it diverges, we write $c_n(z^* - z_0)^n = a_n\mathrm{e}^{\mathrm{i}n\theta}$ and try Dirichlet's test, or check whether the terms tend to $0$.

**Example 5.2.3** Consider $\sum_{n\ge1}\frac{z^{2n}}{\sqrt n\,4^n}$. In the variable $w = z^2/4$ it is $\sum w^n/\sqrt n$, which converges for $\lvert w\rvert < 1$, so $R = 2$. On $\lvert z\rvert = 2$ we have $w = \mathrm{e}^{\mathrm{i}\theta}$ and $\sum\lvert w^n\rvert/\sqrt n = \sum 1/\sqrt n$ diverges, so there is no absolute convergence anywhere on the circle.

- At $z = \sqrt3 + \mathrm{i}$: $z^2 = 2 + 2\sqrt3\,\mathrm{i}$, so $w = \mathrm{e}^{\mathrm{i}\pi/3} \ne 1$. Since $1/\sqrt n$ decreases to $0$, the series converges conditionally.
- At $z = 2\mathrm{i}$: $w = -1$, an alternating series; it converges conditionally.
- At $z = \pm2$: $w = 1$ and the series $\sum 1/\sqrt n$ diverges.

**Example 5.2.4** Consider $\sum_{n\ge1}\frac{1}{\sqrt n}\sin\frac{\mathrm{i}}{n}\,z^n$. Since $\sin(\mathrm{i}t) = \mathrm{i}\sinh t$, the coefficients are $c_n = \frac{\mathrm{i}}{\sqrt n}\sinh\frac1n$, and $\lvert c_n\rvert \sim n^{-3/2}$. Hence $R = 1$, and because $\sum n^{-3/2} < \infty$ the series converges absolutely at every point of $\lvert z\rvert = 1$, for instance at $z = \mathrm{e}^{\mathrm{i}\pi/4}$.

### 5.2.3. The Sum of a Power Series Is Analytic

**Theorem 5.2.3** Let $\sum c_n(z - z_0)^n$ have radius of convergence $R > 0$ and sum $f(z)$ in $D = D(z_0, R)$. Then:

1. $f$ is analytic in $D$, and $f'(z) = \sum_{n\ge1}nc_n(z - z_0)^{n-1}$, a power series with the same radius $R$;
2. $f$ has derivatives of all orders in $D$, and $c_n = \dfrac{f^{(n)}(z_0)}{n!}$;
3. for every piecewise smooth curve $\gamma$ in $D$ from $z_0$ to $z$, $\displaystyle\int_\gamma f(\zeta)\,\mathrm{d}\zeta = \sum_{n\ge0}\frac{c_n}{n+1}(z - z_0)^{n+1}$.

**Proof** By Abel's theorem the series converges uniformly on every closed disk $\lvert z - z_0\rvert \le \rho < R$, hence uniformly on compact subsets of $D$, and each term is a polynomial. Theorem 5.1.2 gives 1 and, by induction, the termwise formula for $f^{(n)}$; setting $z = z_0$ gives 2. Integrating term by term gives 3. That $\sum nc_n(z - z_0)^{n-1}$ has radius $R$ follows from Eq. (5.1), because $\sqrt[n]{n} \to 1$. $\square$

In particular, the coefficients of a power series are determined by its sum: if two power series with the same center agree on a disk around the center, they are identical. Termwise differentiation and integration are the main tools for finding sums.

**Example 5.2.5** 1. For $\lvert z\rvert < 1$, applying the operator $z\frac{\mathrm{d}}{\mathrm{d}z}$ twice to $\sum_{n\ge0}z^n = \frac1{1-z}$ gives

$$
\sum_{n\ge1}nz^n = \frac{z}{(1-z)^2}, \qquad \sum_{n\ge1}n^2z^n = z\frac{\mathrm{d}}{\mathrm{d}z}\frac{z}{(1-z)^2} = \frac{z(1+z)}{(1-z)^3}.
$$

2. $\sum_{n\ge0}\frac{n+1}{n!}z^n = \sum_{n\ge1}\frac{z^n}{(n-1)!} + \sum_{n\ge0}\frac{z^n}{n!} = (z + 1)\mathrm{e}^z$ for all $z \in \mathbb{C}$ ($R = \infty$).

## 5.3. Taylor Series

### 5.3.1. Taylor's Theorem

**Theorem 5.3.1 (Taylor's Theorem)** Let $f$ be analytic in a domain $D$, let $z_0 \in D$, and let $d$ be the distance from $z_0$ to the boundary of $D$ ($d = +\infty$ if $D = \mathbb{C}$). Then

$$
f(z) = \sum_{n=0}^\infty c_n(z - z_0)^n, \qquad c_n = \frac{f^{(n)}(z_0)}{n!} = \frac{1}{2\pi\mathrm{i}}\oint_{\lvert\zeta - z_0\rvert = r}\frac{f(\zeta)}{(\zeta - z_0)^{n+1}}\,\mathrm{d}\zeta \quad (0 < r < d), \tag{5.2}
$$

for every $z$ with $\lvert z - z_0\rvert < d$, and this expansion is unique.

**Proof** Fix $z$ with $\lvert z - z_0\rvert < d$, choose $r$ with $\lvert z - z_0\rvert < r < d$, and let $C$ be the positively oriented circle $\lvert\zeta - z_0\rvert = r$. For $\zeta \in C$ we have $q = \lvert z - z_0\rvert/r < 1$, so

$$
\frac{1}{\zeta - z} = \frac{1}{(\zeta - z_0) - (z - z_0)} = \frac{1}{\zeta - z_0}\cdot\frac{1}{1 - \frac{z - z_0}{\zeta - z_0}} = \sum_{n=0}^\infty\frac{(z - z_0)^n}{(\zeta - z_0)^{n+1}},
$$

and the $n$-th term has modulus at most $q^n/r$, so the series converges uniformly in $\zeta \in C$. Multiply by $f(\zeta)/(2\pi\mathrm{i})$, which is bounded on $C$, and integrate term by term. By Cauchy's integral formula the left side becomes $f(z)$, and the right side becomes $\sum c_n(z - z_0)^n$ with $c_n$ given by the integral in Eq. (5.2), which equals $f^{(n)}(z_0)/n!$ by the formula for derivatives. Uniqueness follows from Theorem 5.2.3. $\square$

The power series in Eq. (5.2) is the **Taylor series** of $f$ at $z_0$ (the **Maclaurin series** when $z_0 = 0$). Combining Theorems 5.2.3 and 5.3.1:

**Corollary 5.3.1** A function is analytic at $z_0$ if and only if it is the sum of a convergent power series in some disk $D(z_0, r)$. The Taylor series of $f$ at $z_0$ converges to $f$ in the largest open disk centered at $z_0$ that is contained in the domain of analyticity of $f$.

This is the decisive difference from real analysis. On $\mathbb{R}$ the function equal to $\mathrm{e}^{-1/x^2}$ for $x \ne 0$ and $0$ at $0$ has all derivatives $0$ at $0$, so its Taylor series is identically zero and does not represent it. In $\mathbb{C}$ this function is not even continuous at $0$: along the imaginary axis $\mathrm{e}^{-1/(\mathrm{i}y)^2} = \mathrm{e}^{1/y^2} \to \infty$.

### 5.3.2. The Radius of Convergence and Singularities

Corollary 5.3.1 says $R \ge d$. Conversely, the radius cannot be larger than the function allows:

**Theorem 5.3.2** Let $f$ be analytic in $\mathbb{C}$ except at finitely many points $a_1, \dots, a_m$, and suppose $\lvert f(z)\rvert \to \infty$ as $z \to a_j$ for each $j$. Then the radius of convergence of the Taylor series of $f$ at any $z_0 \ne a_j$ equals $\min_j\lvert z_0 - a_j\rvert$.

**Proof** Let $d = \min_j\lvert z_0 - a_j\rvert$; then $R \ge d$ by Theorem 5.3.1. Suppose $R > d$, let $g$ be the sum of the series in $D(z_0, R)$, and let $a_j$ be a point with $\lvert z_0 - a_j\rvert = d$. The functions $f$ and $g$ agree on $D(z_0, d)$, and $D(z_0, R)$ minus the finitely many $a_k$ is connected, so $f = g$ there by the identity theorem (Theorem 5.4.3 below). But $g$ is continuous at $a_j$ whereas $\lvert f\rvert \to \infty$, a contradiction. $\square$

This explains the example from [2.2.9](/2.2.9): $\frac{1}{1+x^2} = \sum(-1)^nx^{2n}$ has radius $1$ although the function is smooth on the whole real line, because $\frac{1}{1+z^2}$ blows up at $z = \pm\mathrm{i}$, at distance $1$ from the origin. Similarly the Maclaurin series of $\tan z$ has radius $\frac{\pi}{2}$ (the zeros $\pm\frac\pi2$ of $\cos z$), and that of $\frac{z}{\mathrm{e}^z - 1}$ has radius $2\pi$ (the zeros $\pm2\pi\mathrm{i}$ of the denominator; $z = 0$ is harmless because the quotient tends to $1$ there).

![Error of the Taylor partial sums with 30 terms for 1/(1 - z) and 1/(1 + z^2) at the center 0. In both cases the partial sums converge exactly inside the unit disk (dashed), whose radius is the distance to the nearest singularity (red crosses); for 1/(1 + z^2) the singularities ±i lie off the real axis](./plots/taylor-convergence.py)

### 5.3.3. Standard Expansions and Indirect Methods

The following expansions follow from Eq. (5.2) or from the corresponding real expansions and Theorem 5.4.3:

| Function | Maclaurin series | Region |
|---|---|---|
| $\mathrm{e}^z$ | $\sum_{n\ge0}\dfrac{z^n}{n!}$ | $\mathbb{C}$ |
| $\sin z$, $\cos z$ | $\sum_{n\ge0}\dfrac{(-1)^nz^{2n+1}}{(2n+1)!}$, $\ \sum_{n\ge0}\dfrac{(-1)^nz^{2n}}{(2n)!}$ | $\mathbb{C}$ |
| $\sinh z$, $\cosh z$ | $\sum_{n\ge0}\dfrac{z^{2n+1}}{(2n+1)!}$, $\ \sum_{n\ge0}\dfrac{z^{2n}}{(2n)!}$ | $\mathbb{C}$ |
| $\dfrac{1}{1-z}$ | $\sum_{n\ge0}z^n$ | $\lvert z\rvert < 1$ |
| $\operatorname{Log}(1+z)$ | $\sum_{n\ge1}\dfrac{(-1)^{n-1}}{n}z^n$ | $\lvert z\rvert < 1$ |
| $(1+z)^\alpha = \mathrm{e}^{\alpha\operatorname{Log}(1+z)}$ | $\sum_{n\ge0}\dbinom{\alpha}{n}z^n$ | $\lvert z\rvert < 1$ |

Here $\operatorname{Log}$ is the principal branch ([2.3.3](/2.3.3)), which is analytic in $\lvert z\rvert < 1$ because $1 + z$ stays in the right half-plane; the last row is the complex **binomial series**. In practice one rarely computes $f^{(n)}(z_0)$ directly. By uniqueness, any method that produces a convergent power series gives the Taylor series: substitution, termwise differentiation and integration, multiplication (Cauchy product), division by a series with nonzero constant term, and partial fractions.

**Example 5.3.1** Find $f^{(2024)}(0)$ and $f^{(2025)}(0)$ for $f(z) = \operatorname{Log}(1 + z^4)$.

Substituting $z^4$ into the logarithmic series gives, for $\lvert z\rvert < 1$,

$$
\operatorname{Log}(1 + z^4) = \sum_{k\ge1}\frac{(-1)^{k-1}}{k}z^{4k}.
$$

The coefficient of $z^{2024} = z^{4\cdot506}$ is $\frac{(-1)^{505}}{506} = -\frac1{506}$, so $f^{(2024)}(0) = -\frac{2024!}{506} = -4\cdot2023!$. Since $2025$ is not a multiple of $4$, $f^{(2025)}(0) = 0$.

**Example 5.3.2** 1. $\frac{\mathrm{e}^z}{1-z}$ for $\lvert z\rvert < 1$: the Cauchy product of $\sum z^n/n!$ and $\sum z^n$ gives $\sum_{n\ge0}\left(\sum_{k=0}^n\frac1{k!}\right)z^n = 1 + 2z + \frac52z^2 + \frac83z^3 + \cdots$.
2. $\tan z = \frac{\sin z}{\cos z}$: writing $\tan z = a_1z + a_3z^3 + a_5z^5 + \cdots$ (an odd function) and comparing coefficients in $\left(z - \frac{z^3}{6} + \frac{z^5}{120} - \cdots\right) = \left(1 - \frac{z^2}{2} + \frac{z^4}{24} - \cdots\right)(a_1z + a_3z^3 + a_5z^5 + \cdots)$ gives $a_1 = 1$, $a_3 = \frac13$, $a_5 = \frac2{15}$. The series converges for $\lvert z\rvert < \frac\pi2$.
3. $\frac{1}{(1-z)^2} = \frac{\mathrm{d}}{\mathrm{d}z}\frac1{1-z} = \sum_{n\ge0}(n+1)z^n$ for $\lvert z\rvert < 1$.

## 5.4. Zeros and the Identity Theorem

### 5.4.1. Order of a Zero

**Definition 5.4.1** Let $f$ be analytic at $z_0$ and not identically zero near $z_0$, with $f(z_0) = 0$. If

$$
f(z_0) = f'(z_0) = \cdots = f^{(m-1)}(z_0) = 0, \qquad f^{(m)}(z_0) \ne 0,
$$
then $z_0$ is called a zero of order $m$ of $f$, and $m$ is the **order of the zero**; a zero of order $1$ is a **simple zero**.

Such an $m$ always exists: if all derivatives vanished at $z_0$, the Taylor series would be zero and $f \equiv 0$ near $z_0$.

**Theorem 5.4.1** $z_0$ is a zero of order $m$ of $f$ if and only if $f(z) = (z - z_0)^m\varphi(z)$ near $z_0$, where $\varphi$ is analytic at $z_0$ and $\varphi(z_0) \ne 0$.

**Proof** By Taylor's theorem $f(z) = \sum_{n\ge m}c_n(z - z_0)^n = (z - z_0)^m\sum_{k\ge0}c_{m+k}(z - z_0)^k$, and $\varphi(z_0) = c_m = f^{(m)}(z_0)/m! \ne 0$. The converse follows by differentiating the product. $\square$

For instance $z = 0$ is a zero of order $3$ of $z - \sin z = \frac{z^3}{6} - \frac{z^5}{120} + \cdots$, and every $z = k\pi$ is a simple zero of $\sin z$ because $\cos k\pi \ne 0$. Orders add under multiplication: if $z_0$ is a zero of order $m$ of $f$ and of order $k$ of $g$, it is a zero of order $m + k$ of $fg$.

### 5.4.2. Isolated Zeros and the Identity Theorem

**Theorem 5.4.2** Let $f$ be analytic on a domain $D$ and not identically zero. Then the zeros of $f$ are isolated: every zero $z_0$ has a punctured neighborhood $0 < \lvert z - z_0\rvert < \delta$ free of zeros.

**Proof** Let $E$ be the set of points of $D$ at which all derivatives of $f$ (including $f$ itself) vanish. $E$ is closed in $D$ by continuity of the derivatives. $E$ is also open: if $z_1 \in E$, the Taylor series at $z_1$ vanishes, so $f \equiv 0$ on a disk around $z_1$, and that disk lies in $E$. Since $D$ is connected and $f \not\equiv 0$, $E = \varnothing$. So every zero $z_0$ has a finite order $m$, and by Theorem 5.4.1, $f(z) = (z - z_0)^m\varphi(z)$ with $\varphi$ continuous and $\varphi(z_0) \ne 0$; hence $\varphi \ne 0$ on a disk around $z_0$, and $f \ne 0$ there except at $z_0$. $\square$

**Theorem 5.4.3 (Identity Theorem)** Let $f$ and $g$ be analytic on a domain $D$, and suppose $f = g$ on a set $E \subseteq D$ that has a limit point in $D$ (for instance a sequence $z_n \to z^* \in D$ with $z_n \ne z^*$, or an arc of a curve). Then $f \equiv g$ on $D$.

**Proof** Apply Theorem 5.4.2 to $f - g$: its zeros contain the non-isolated zero $z^*$ (a zero by continuity), so $f - g \equiv 0$. $\square$

An analytic function on a domain is therefore determined by its values on an arbitrarily small disk or segment. This has several consequences:

- Real identities extend to $\mathbb{C}$: $\sin^2z + \cos^2z - 1$ is entire and vanishes on $\mathbb{R}$, so it vanishes everywhere. The same argument proves the addition formulas for $\mathrm{e}^z$, $\sin z$ and $\cos z$ in [2.3.3](/2.3.3).
- If an analytic function $f$ on $D$ and an analytic function $g$ on a larger domain $G \supseteq D$ agree on $D$, then $g$ is the only such extension of $f$ to $G$; it is called the *analytic continuation* of $f$ to $G$. For example $\sum z^n$ ($\lvert z\rvert < 1$) continues analytically to $\frac1{1-z}$ on $\mathbb{C}\setminus\{1\}$.
- The theorem fails for smooth real functions: $\mathrm{e}^{-1/x^2}$ (extended by $0$) and the zero function agree on $(-\infty, 0]$ without being equal.

**Example 5.4.1** Is there a function $f$ analytic in $\mathbb{D}$ with $f\left(\frac1n\right) = \frac{(-1)^n}{n}$ for $n = 2, 3, \dots$? The points $\frac1{2k}$ accumulate at $0 \in \mathbb{D}$ and $f\left(\frac1{2k}\right) = \frac1{2k}$, so $f(z) = z$ by the identity theorem. Then $f\left(\frac1{2k+1}\right) = \frac1{2k+1} \ne -\frac1{2k+1}$, a contradiction; no such $f$ exists. On the other hand, $f\left(\frac1n\right) = \frac1{n^2}$ is satisfied by $f(z) = z^2$, and by no other analytic function on $\mathbb{D}$.

**Example 5.4.2** The condition that the limit point lies in $D$ is essential. The function $\sin\frac{\pi}{z}$ is analytic on $D = \mathbb{C}\setminus\{0\}$ and vanishes at $z = \frac1n$, but $\frac1n \to 0 \notin D$, and the function is not identically zero.

## 5.5. Laurent Series

### 5.5.1. Series in Positive and Negative Powers

Functions such as $\mathrm{e}^{1/z}$ or $\frac{1}{z(1-z)}$ are analytic in a punctured disk or in an annulus, but not at the center, so they have no Taylor series there. The appropriate replacement is a series in both positive and negative powers.

**Definition 5.5.1** A series of the form

$$
\sum_{n=-\infty}^{\infty}c_n(z - z_0)^n = \sum_{n=1}^\infty\frac{c_{-n}}{(z - z_0)^n} + \sum_{n=0}^\infty c_n(z - z_0)^n \tag{5.3}
$$
is called a **Laurent series** with center $z_0$. It is said to converge at $z$ if both series on the right converge there; its sum is the sum of the two.

The second series on the right is a power series in $z - z_0$, convergent for $\lvert z - z_0\rvert < R$ with $R = 1/\limsup\sqrt[n]{\lvert c_n\rvert}$. The first is a power series in $w = \frac{1}{z - z_0}$, with radius $1/r$ where $r = \limsup\sqrt[n]{\lvert c_{-n}\rvert}$; it converges for $\lvert z - z_0\rvert > r$. Hence:

**Theorem 5.5.1** Let $r$ and $R$ be as above. If $r < R$, the Laurent series as in Eq. (5.3) converges absolutely in the annulus $r < \lvert z - z_0\rvert < R$ and uniformly on every closed sub-annulus $r < \rho_1 \le \lvert z - z_0\rvert \le \rho_2 < R$, and its sum is analytic in the annulus. It diverges at every point with $\lvert z - z_0\rvert < r$ or $\lvert z - z_0\rvert > R$.

**Definition 5.5.2** The annulus $r < \lvert z - z_0\rvert < R$ of Theorem 5.5.1 is the **annulus of convergence** of the Laurent series; $r = 0$ (a punctured disk) and $R = +\infty$ are allowed.

**Example 5.5.1** 1. $\sum_{n=-\infty}^{\infty}\frac{z^n}{2^n + 3^n}$. For $n \ge 0$, $c_n \sim 3^{-n}$, so $R = 3$. For $n = -m < 0$, $c_{-m} = \frac{1}{2^{-m} + 3^{-m}} = \frac{6^m}{2^m + 3^m} \sim 2^m$, so $r = 2$. The annulus of convergence is $2 < \lvert z\rvert < 3$.
2. $\sum_{n=-\infty}^{\infty}2^{-n^2}z^n$: $\sqrt[\lvert n\rvert]{\lvert c_n\rvert} = 2^{-\lvert n\rvert} \to 0$ in both directions, so $r = 0$, $R = \infty$, and the series converges in $0 < \lvert z\rvert < \infty$.
3. $\sum_{n=-\infty}^{\infty}z^n$: $r = R = 1$, and the series converges nowhere.

### 5.5.2. Laurent's Theorem

The converse of Theorem 5.5.1 is the main result of this chapter: every function analytic in an annulus is the sum of a Laurent series there.

**Theorem 5.5.2 (Laurent's Theorem)** Let $f$ be analytic in the annulus $A = \{r < \lvert z - z_0\rvert < R\}$, where $0 \le r < R \le +\infty$. Then

$$
f(z) = \sum_{n=-\infty}^{\infty}c_n(z - z_0)^n, \qquad c_n = \frac{1}{2\pi\mathrm{i}}\oint_{\lvert\zeta - z_0\rvert = \rho}\frac{f(\zeta)}{(\zeta - z_0)^{n+1}}\,\mathrm{d}\zeta \quad (n \in \mathbb{Z}), \tag{5.4}
$$

for every $z \in A$, where $\rho \in (r, R)$ is arbitrary and the circle is positively oriented. The expansion is unique: if $f(z) = \sum a_n(z - z_0)^n$ in $A$ for some coefficients $a_n$, then $a_n = c_n$.

**Proof** The integral in Eq. (5.4) does not depend on $\rho$, by Cauchy's integral theorem for the region between two circles. Fix $z \in A$ and choose $r < \rho_1 < \lvert z - z_0\rvert < \rho_2 < R$; let $C_1$ and $C_2$ be the positively oriented circles of radii $\rho_1$ and $\rho_2$. Cauchy's integral formula for the annulus between them ([2.3.4](/2.3.4)) gives

$$
f(z) = \frac{1}{2\pi\mathrm{i}}\oint_{C_2}\frac{f(\zeta)}{\zeta - z}\,\mathrm{d}\zeta - \frac{1}{2\pi\mathrm{i}}\oint_{C_1}\frac{f(\zeta)}{\zeta - z}\,\mathrm{d}\zeta.
$$

On $C_2$ we have $\lvert z - z_0\rvert < \lvert\zeta - z_0\rvert$, and exactly as in the proof of Taylor's theorem the first integral equals $\sum_{n\ge0}c_n(z - z_0)^n$. On $C_1$ we have $\lvert\zeta - z_0\rvert < \lvert z - z_0\rvert$, and we expand in the other direction:

$$
-\frac{1}{\zeta - z} = \frac{1}{(z - z_0) - (\zeta - z_0)} = \sum_{k=0}^\infty\frac{(\zeta - z_0)^k}{(z - z_0)^{k+1}},
$$

uniformly in $\zeta \in C_1$. Integrating term by term, the second integral (with its minus sign) becomes $\sum_{k\ge0}(z - z_0)^{-k-1}\frac{1}{2\pi\mathrm{i}}\oint_{C_1}f(\zeta)(\zeta - z_0)^k\,\mathrm{d}\zeta = \sum_{n\ge1}c_{-n}(z - z_0)^{-n}$.

For uniqueness, the series $\sum a_n(z - z_0)^n$ converges uniformly on the circle $\lvert z - z_0\rvert = \rho$ (Theorem 5.5.1). Multiply it by $(z - z_0)^{-k-1}$ and integrate term by term; since $\oint(z - z_0)^{n-k-1}\,\mathrm{d}z$ equals $2\pi\mathrm{i}$ for $n = k$ and $0$ otherwise, we obtain $2\pi\mathrm{i}\,c_k = 2\pi\mathrm{i}\,a_k$. $\square$

Some remarks:

- Taylor's theorem is the special case in which $f$ is analytic in the whole disk $\lvert z - z_0\rvert < R$: then $f(\zeta)(\zeta - z_0)^{-n-1}$ is analytic inside the circle for $n \le -1$, so $c_n = 0$ for $n < 0$. In general $c_n \ne f^{(n)}(z_0)/n!$, since $f$ need not even be defined at $z_0$.
- A function may have several different Laurent expansions with the same center, one for each annulus of analyticity; uniqueness holds within each annulus.
- For $n = -1$, Eq. (5.4) gives $\oint_{\lvert\zeta - z_0\rvert = \rho}f(\zeta)\,\mathrm{d}\zeta = 2\pi\mathrm{i}\,c_{-1}$. Reading this formula from right to left, that is, computing a contour integral from a single Laurent coefficient, is the idea behind the residue theorem of [2.3.6](/2.3.6).

### 5.5.3. Computing Laurent Expansions

The integrals in Eq. (5.4) are seldom evaluated directly. By uniqueness, any convergent expansion in the right annulus is the Laurent series. The main tools are partial fractions, the geometric series in the form

$$
\frac{1}{z - a} = \begin{cases}-\displaystyle\sum_{n\ge0}\frac{z^n}{a^{n+1}}, & \lvert z\rvert < \lvert a\rvert,\\[2ex] \displaystyle\sum_{n\ge1}\frac{a^{n-1}}{z^n}, & \lvert z\rvert > \lvert a\rvert,\end{cases}
$$

and substitution into known Taylor series.

**Example 5.5.2** Expand $f(z) = \frac{1}{(z-1)(z-2)} = \frac{1}{z-2} - \frac{1}{z-1}$ in every annulus centered at $0$ or at $1$ in which it is analytic.

Centered at $0$, the poles $1$ and $2$ split the plane into three regions.

1. $\lvert z\rvert < 1$ (Taylor series): $f(z) = -\sum\frac{z^n}{2^{n+1}} + \sum z^n = \sum_{n\ge0}\left(1 - \frac1{2^{n+1}}\right)z^n$.
2. $1 < \lvert z\rvert < 2$: here $\frac1{z-2}$ is expanded in positive powers and $\frac1{z-1}$ in negative powers:

$$
f(z) = -\sum_{n\ge0}\frac{z^n}{2^{n+1}} - \sum_{n\ge1}\frac{1}{z^n}.
$$

3. $\lvert z\rvert > 2$: $f(z) = \sum_{n\ge1}\frac{2^{n-1} - 1}{z^n} = \sum_{n\ge2}\frac{2^{n-1} - 1}{z^n} = \frac1{z^2} + \frac3{z^3} + \frac7{z^4} + \cdots$.

Centered at $1$, write $w = z - 1$, so that $f = \frac{1}{w(w-1)}$.

4. $0 < \lvert z - 1\rvert < 1$: $f = -\frac1w\cdot\frac1{1-w} = -\frac{1}{z-1} - \sum_{n\ge0}(z-1)^n$.
5. $\lvert z - 1\rvert > 1$: $f = \frac1{w^2}\cdot\frac{1}{1 - 1/w} = \sum_{n\ge2}\frac{1}{(z-1)^n}$.

In region 4 the coefficient of $(z-1)^{-1}$ is $-1$, so $\oint_{\lvert z-1\rvert = 1/2}f\,\mathrm{d}z = -2\pi\mathrm{i}$; in regions 3 and 5 it is $0$, so the integral of $f$ over any circle enclosing both poles vanishes.

![Left: the three regions |z| < 1, 1 < |z| < 2 and |z| > 2 in which f(z) = 1/((z - 1)(z - 2)) has a Laurent expansion centered at 0. Right: the two regions 0 < |z - 1| < 1 and |z - 1| > 1 for the center 1. The boundaries of the annuli pass through the poles](./plots/laurent-annuli.py)

**Example 5.5.3** 1. $\mathrm{e}^{1/z} = \sum_{n\ge0}\frac{1}{n!\,z^n} = 1 + \frac1z + \frac{1}{2z^2} + \cdots$ in $0 < \lvert z\rvert < \infty$: infinitely many negative powers.
2. $\frac{\sin z}{z^3} = \frac{1}{z^2} - \frac16 + \frac{z^2}{120} - \cdots$ in $0 < \lvert z\rvert < \infty$: only finitely many negative powers.
3. $\frac{1}{(1 + 2z^2)^2}$ in $\lvert z\rvert > \frac{1}{\sqrt2}$. Write it as $\frac{1}{4z^4}\left(1 + \frac{1}{2z^2}\right)^{-2}$ and use $(1+u)^{-2} = \sum_{k\ge0}(-1)^k(k+1)u^k$ for $\lvert u\rvert < 1$ with $u = \frac{1}{2z^2}$:

$$
\frac{1}{(1 + 2z^2)^2} = \sum_{k\ge0}\frac{(-1)^k(k+1)}{2^{k+2}}\,z^{-2k-4} = \frac{1}{4z^4} - \frac{1}{4z^6} + \frac{3}{16z^8} - \cdots.
$$

In $\lvert z\rvert < \frac1{\sqrt2}$ the same function has the Taylor series $\sum_{k\ge0}(-1)^k(k+1)2^kz^{2k}$.

**Example 5.5.4** Let $f(z) = z\,\mathrm{e}^{1/(z-1)}$ on $0 < \lvert z - 1\rvert < \infty$, and find the coefficients $c_n$ of its Laurent series centered at $1$.

With $w = z - 1$,

$$
f = (1 + w)\sum_{k\ge0}\frac{w^{-k}}{k!} = \sum_{k\ge0}\frac{w^{-k}}{k!} + \sum_{k\ge0}\frac{w^{1-k}}{k!}.
$$

Collecting powers: $c_1 = 1$, $c_0 = 1 + 1 = 2$, and for $n \ge 1$, $c_{-n} = \frac1{n!} + \frac1{(n+1)!} = \frac{n+2}{(n+1)!}$; all other coefficients vanish. For example $c_{-2025} = \frac{2027}{2026!}$, and $c_{-1} = \frac32$, so $\oint_{\lvert z - 1\rvert = 1}z\,\mathrm{e}^{1/(z-1)}\,\mathrm{d}z = 3\pi\mathrm{i}$.

## Summary

| Topic | Key facts |
|---|---|
| Power series | Abel's theorem; $R = 1/\limsup\sqrt[n]{\lvert c_n\rvert}$; on $\lvert z - z_0\rvert = R$ check absolute convergence, then Dirichlet's test |
| Sum of a power series | Analytic in the disk; termwise differentiation and integration; $c_n = f^{(n)}(z_0)/n!$ |
| Taylor's theorem | Analytic in $D(z_0, d)$ $\Rightarrow$ Taylor series converges there; radius = distance to the nearest singularity |
| Zeros | $f = (z - z_0)^m\varphi$, $\varphi(z_0) \ne 0$; zeros are isolated; identity theorem |
| Laurent series | Converges in an annulus $r < \lvert z - z_0\rvert < R$; analytic in an annulus $\Rightarrow$ unique Laurent expansion, coefficients by Eq. (5.4) |
| Computation | Partial fractions, geometric series in $z/a$ or $a/z$, substitution; never differentiate directly |
| Link to residues | $\oint_{\lvert z - z_0\rvert = \rho}f\,\mathrm{d}z = 2\pi\mathrm{i}\,c_{-1}$ |
