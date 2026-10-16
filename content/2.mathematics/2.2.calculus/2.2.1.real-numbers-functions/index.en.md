---
title: Real Numbers and Functions
source_hash: d7cc114db433
---

Calculus studies functions defined on the set of real numbers, and its tool is the limit. This chapter lays two foundations. The first is the structure of the real line, in particular intervals, neighborhoods and suprema: the least-upper-bound property expresses that the real numbers have "no gaps," and it is the source of every existence theorem for limits in the next chapter. The second is a review of the basic notions of functions, their common properties and the elementary functions used throughout the course. Much of this material is treated more generally in discrete mathematics: the construction of the **real numbers** is in [1.2.4](/1.2.4#sec-4.1); functions as relations, injections and surjections, and inverse functions are in [1.2.3](/1.2.3); the **supremum** in a poset is in [1.2.2](/1.2.2#def-2.8.6). Here we restate these ideas on $\mathbb{R}$ in the language of calculus and add the facts that analysis needs.

[Chapter 2](/2.2.2) uses the least-upper-bound property of this chapter to prove the monotone convergence theorem, and [Chapter 3](/2.2.3) discusses the continuity of elementary functions.

## 1.1. Real Numbers

### 1.1.1. Intervals and Neighborhoods

The following subsets of the set $\mathbb{R}$ of real numbers are called intervals ($a < b$):

| Name | Notation and definition |
|---|---|
| Open interval | $(a, b) = \{x \mid a < x < b\}$ |
| Closed interval | $[a, b] = \{x \mid a \leq x \leq b\}$ |
| Half-open interval | $(a, b] = \{x \mid a < x \leq b\}$, $[a, b) = \{x \mid a \leq x < b\}$ |
| Infinite interval | $[a, +\infty) = \{x \mid x \geq a\}$, $(a, +\infty)$, $(-\infty, b]$, $(-\infty, b)$, $(-\infty, +\infty) = \mathbb{R}$ |

The symbols $+\infty$ and $-\infty$ are only notation; they are not real numbers. To define limits we must describe "$x$ is sufficiently close to $x_0$," and for this we introduce neighborhoods.

**Definition 1.1.1 (Neighborhood)** Let $x_0 \in \mathbb{R}$ and $\delta > 0$. The open interval

$$
N(x_0, \delta) = \{x \mid |x - x_0| < \delta\} = (x_0 - \delta, x_0 + \delta)
$$
is called the $\delta$-**neighborhood** of $x_0$; the set obtained by removing the center $x_0$,

$$
N^*(x_0, \delta) = \{x \mid 0 < |x - x_0| < \delta\} = (x_0 - \delta, x_0) \cup (x_0, x_0 + \delta),
$$
is called the $\delta$-**punctured neighborhood** (or deleted neighborhood) of $x_0$. When the radius $\delta$ does not matter, we write simply $N(x_0)$ and $N^*(x_0)$.

The punctured neighborhood is the stage on which limits of functions take place: the limit as $x \to x_0$ depends only on the values of $f$ on some $N^*(x_0, \delta)$, not on $f(x_0)$ ([Chapter 2](/2.2.2#sec-2.3)).

The absolute value satisfies the triangle inequality: for all real numbers $a, b, c$,

$$
\bigl||a| - |b|\bigr| \leq |a + b| \leq |a| + |b|, \qquad |a - b| \leq |a - c| + |c - b|.
$$

The second inequality justifies the trick of "inserting a term" in limit proofs: to estimate the distance between $a$ and $b$, insert a point $c$ close to both.

A **rational number** is a number that can be written as $\frac{m}{n}$ ($m \in \mathbb{Z}$, $n \in \mathbb{N}_+$); a real number that is not rational is called irrational.

**Example 1.1.1** $\sqrt2$ is irrational.

**Proof** Suppose $\sqrt2 = \frac{m}{n}$ with $m, n \in \mathbb{N}_+$ coprime. Then $m^2 = 2n^2$ is even, so $m$ is even; writing $m = 2k$ gives $n^2 = 2k^2$, so $n$ is even as well, contradicting the coprimality of $m$ and $n$. $\square$

**Theorem 1.1.1 (Archimedean Property)** For any $p > 0$ and $q > 0$ there exists $N \in \mathbb{N}_+$ such that $Np > q$.

Intuitively, however small $p$ and however large $q$, adding $p$ to itself enough times eventually exceeds $q$; taking $N = \lfloor q/p \rfloor + 1$ also gives $(N - 1)p \leq q < Np$. Obvious as it seems, the property depends on the completeness of the real numbers; its proof is Example 1.1.3. It yields the most basic facts, such as $\lim\limits_{n\to\infty} \frac1n = 0$.

**Theorem 1.1.2 (Density of the Rationals)** Every nonempty open interval $(a, b)$ contains a rational number, and hence infinitely many rational numbers.

**Proof** By Theorem 1.1.1, choose $n \in \mathbb{N}_+$ with $n(b - a) > 1$ and let $m = \lfloor na \rfloor + 1$. Then $na < m \leq na + 1 < nb$, that is, $a < \frac{m}{n} < b$. Repeating the argument on $(a, \frac mn)$ produces infinitely many rational numbers. $\square$

### 1.1.2. Bounds and Suprema of Sets of Real Numbers

**Definition 1.1.2 (Bounds, Supremum and Infimum)** Let $E$ be a nonempty subset of $\mathbb{R}$.

1. If there exists $a \in \mathbb{R}$ such that $x \leq a$ ($x \geq a$) for all $x \in E$, then $a$ is called an upper bound (lower bound) of $E$. A set with both an upper bound and a lower bound is said to be bounded.
2. If there exists $a \in E$ such that $x \leq a$ ($x \geq a$) for all $x \in E$, then $a$ is called the maximum (minimum) of $E$, denoted $\max E$ ($\min E$).
3. If $E$ is bounded above (below), its least upper bound (greatest lower bound) is called the **supremum** (**infimum**) of $E$, denoted $\sup E$ ($\inf E$).

The maximum must belong to $E$, whereas the supremum need not: $E = (0, 1)$ has no maximum, but $\sup E = 1$. The three notions are related by

$$
E \text{ has a maximum} \implies E \text{ has a supremum (and } \sup E = \max E\text{)} \implies E \text{ is bounded above}.
$$

Whether the second implication can be reversed is the central question of the theory of real numbers.

**Theorem 1.1.3 (Least-Upper-Bound Property)** Let $E \subseteq \mathbb{R}$ be nonempty.

1. If $E$ is bounded above, then $E$ has a supremum;
2. If $E$ is bounded below, then $E$ has an infimum.

In this course we use this theorem as a basic property (an axiom) of the real numbers, without proof; when the real numbers are constructed from Cauchy sequences ([1.2.4](/1.2.4#sec-4.1)), it becomes a provable theorem. It expresses the *completeness of the real numbers*, also called the continuity of the real line: the real numbers have no "gaps" on the number line. The rational numbers lack this property: $\{x \in \mathbb{Q} \mid x^2 < 2\}$ is bounded above in $\mathbb{Q}$ but has no rational least upper bound, because its would-be supremum $\sqrt2$ is irrational (Example 1.1.1). [Chapter 3](/2.2.3#sec-3.2) shows that the monotone convergence theorem, the nested interval theorem, the Bolzano–Weierstrass theorem and the Cauchy criterion are all equivalent to it.

**Theorem 1.1.4 (Characterization of Suprema and Infima)** Let $E$ be a nonempty set of real numbers and $a, b \in \mathbb{R}$. Then

1. $b = \sup E$ if and only if (i) $b$ is an upper bound of $E$, and (ii) for every $\varepsilon > 0$ there exists $x \in E$ with $x > b - \varepsilon$;
2. $a = \inf E$ if and only if (i) $a$ is a lower bound of $E$, and (ii) for every $\varepsilon > 0$ there exists $x \in E$ with $x < a + \varepsilon$.

**Proof** We prove only part 1. Condition (ii) says precisely that no number $b - \varepsilon$ smaller than $b$ is an upper bound; together with (i), this means that $b$ is the least upper bound. $\square$

Condition (ii) is the standard way of using a supremum: step down a little from $\sup E$ and you find an element of $E$. This is exactly how [Chapter 2](/2.2.2) proves the monotone convergence theorem.

**Example 1.1.2** Let $E = \left\{1 - \frac1n \;\middle|\; n \in \mathbb{N}_+\right\}$. Then $\min E = \inf E = 0$ and $\sup E = 1$, but $E$ has no maximum. Indeed, $1$ is an upper bound, and for any $\varepsilon > 0$, choosing $n > \frac1\varepsilon$ by Theorem 1.1.1 gives $1 - \frac1n > 1 - \varepsilon$.

**Example 1.1.3 (Proof of the Archimedean Property)** Let $p, q > 0$ and suppose $np \leq q$ for all $n \in \mathbb{N}_+$. Then $E = \{np \mid n \in \mathbb{N}_+\}$ is bounded above, so by Theorem 1.1.3 it has a supremum $s$. By Theorem 1.1.4 there exists $n$ with $np > s - p$, whence $(n + 1)p > s$, contradicting the fact that $s$ is an upper bound.

## 1.2. Functions

### 1.2.1. Definition of a Function

**Definition 1.2.1 (Function)** Let $D \subseteq \mathbb{R}$ be nonempty. If a definite rule $f$ assigns to each $x \in D$ a unique real number $y$, then $f$ is called a **function** defined on $D$, written

$$
y = f(x), \quad x \in D.
$$
Here $x$ is called the independent variable, $y$ the dependent variable, and $D$ the domain, denoted $D(f)$; the set of all values $R(f) = \{f(x) \mid x \in D\}$ is called the range.

This is the special case of a general **mapping** ([1.2.3](/1.2.3#def-3.1.1)) with $D \subseteq \mathbb{R}$ and values in $\mathbb{R}$. A function is determined by two ingredients, the rule $f$ and the domain $D(f)$; the letter used for the independent variable is immaterial, so $y = f(x)$ and $y = f(t)$ are the same function. When no domain is specified, the domain is understood to be the set of all values of the independent variable for which the expression (and, in applications, the problem) makes sense.

**Example 1.2.1** $y = x$ and $y = \frac{x^2}{x}$ are different functions: the domain of the first is $\mathbb{R}$, that of the second is $\mathbb{R} \setminus \{0\}$.

### 1.2.2. Some Important Properties of Functions

**Definition 1.2.2 (Odd and Even Functions)** Let the domain $D(f)$ of $f$ be symmetric about the origin. If $f(-x) = f(x)$ for all $x \in D(f)$, then $f$ is called an **even function**; if $f(-x) = -f(x)$ for all $x \in D(f)$, then $f$ is called an **odd function**.

The graph of an even function is symmetric about the $y$-axis, and the graph of an odd function is symmetric about the origin. Every function whose domain is symmetric about the origin can be written uniquely as the sum of an even function and an odd function:

$$
f(x) = \underbrace{\frac{f(x) + f(-x)}{2}}_{\text{even}} + \underbrace{\frac{f(x) - f(-x)}{2}}_{\text{odd}}.
$$

For example, $\mathrm{e}^x = \cosh x + \sinh x$ (hyperbolic functions are introduced in §1.2.4).

**Example 1.2.2** Determine the parity: (1) $y = x + \sin x$ is odd. (2) $y = x\,\frac{2^x + 1}{2^x - 1}$: the factor $g(x) = \frac{2^x + 1}{2^x - 1}$ satisfies $g(-x) = \frac{1 + 2^x}{1 - 2^x} = -g(x)$, so it is odd, and multiplying it by the odd function $x$ gives an even function. (3) $y = \ln\bigl(x + \sqrt{1 + x^2}\bigr)$: since $\bigl(-x + \sqrt{1+x^2}\bigr)\bigl(x + \sqrt{1+x^2}\bigr) = 1$, we have $f(-x) = -f(x)$, so it is odd.

**Definition 1.2.3 (Monotonic Function)** Let $f$ be defined on a set $D$. If for all $x_1, x_2 \in D$, $x_1 < x_2$ implies $f(x_1) < f(x_2)$ ($f(x_1) > f(x_2)$), then $f$ is said to be strictly increasing (strictly decreasing) on $D$; if $x_1 < x_2$ implies $f(x_1) \leq f(x_2)$ ($f(x_1) \geq f(x_2)$), then $f$ is said to be nondecreasing (nonincreasing) on $D$. Functions of these four kinds are collectively called **monotonic functions**.

A note on terminology: in this course (as in its textbook), "increasing" by itself means strictly increasing, while "monotonically increasing" in [1.2.3](/1.2.3#def-3.1.7) means nondecreasing; to avoid ambiguity we always say "strictly increasing" or "nondecreasing." Monotonicity depends on the interval: $\sin x$ is strictly increasing on $\left[-\frac\pi2, \frac\pi2\right]$ and strictly decreasing on $\left[\frac\pi2, \frac{3\pi}2\right]$, but it is not monotonic on $\mathbb{R}$.

**Definition 1.2.4 (Periodic Function)** If there exists $T > 0$ such that for every $x \in D(f)$ we have $x + T \in D(f)$ and $f(x + T) = f(x)$, then $f$ is called a **periodic function** with period $T$.

A period is not unique (if $T$ is a period, so are $2T, 3T, \dots$). "The period" usually means the smallest positive period, the fundamental period, but it need not exist: a constant function has every positive number as a period, and the function in the next example has every positive rational number as a period. If $f$ has period $T$, then $f(ax + b)$ ($a \ne 0$) has period $\frac{T}{|a|}$.

**Example 1.2.3** The *Dirichlet function*

$$
D(x) = \begin{cases} 1, & x \in \mathbb{Q}, \\ 0, & x \notin \mathbb{Q} \end{cases}
$$
is the **indicator function** $\chi_{\mathbb{Q}}$ of $\mathbb{Q}$. For every positive rational $r$, the numbers $x$ and $x + r$ are either both rational or both irrational, so $D(x + r) = D(x)$; since there is no smallest positive rational number, $D$ has no fundamental period. It is also the standard example of a function that is discontinuous everywhere ([Chapter 3](/2.2.3)) and of a function that is not integrable ([Chapter 7](/2.2.7)).

**Definition 1.2.5 (Bounded Function)** Let $f$ be defined on a set $D$. If there exists $M > 0$ such that

$$
|f(x)| \leq M, \quad \forall x \in D,
$$
then $f$ is said to be bounded on $D$, or a **bounded function** on $D$. If for every $M > 0$ there exists $x \in D$ with $|f(x)| > M$, then $f$ is said to be unbounded on $D$.

A function $f$ is bounded on $D$ if and only if its image $f(D)$ is contained in a finite interval. Boundedness also depends on the set: $\frac1x$ is bounded on $[1, +\infty)$ but unbounded on $(0, 1)$.

### 1.2.3. Inverse Functions and Composite Functions

Recall from [1.2.3](/1.2.3#def-3.1.4) that a mapping $f\colon X \to Y$ is an **injection** if $x_1 \ne x_2$ implies $f(x_1) \ne f(x_2)$, a **surjection** if $R(f) = Y$, and a **bijection** if it is both. A bijection $f$ has an inverse mapping $f^{-1}\colon Y \to X$, which sends $y$ to the unique $x$ with $f(x) = y$ and satisfies

$$
f^{-1} \circ f = \mathrm{id}_X, \qquad f \circ f^{-1} = \mathrm{id}_Y.
$$

**Definition 1.2.6 (Inverse Function)** Let the function $y = f(x)$ be a bijection from its domain $D(f)$ onto its range $R(f)$. Its inverse mapping $x = f^{-1}(y)$, $y \in R(f)$, is called the **inverse function** of $f$. Following convention, we rename the independent variable $x$ and write the inverse function as $y = f^{-1}(x)$, $x \in R(f)$.

- The point $(a, b)$ lies on the graph of $y = f(x)$ if and only if $(b, a)$ lies on the graph of $y = f^{-1}(x)$, so the two graphs are symmetric about the line $y = x$.
- A strictly monotonic function is a bijection onto its range, so it has an inverse function, which is monotonic in the same sense. This is how the inverse trigonometric functions are constructed: restrict a trigonometric function to an interval on which it is monotonic, and then invert.

![The graphs of a function and its inverse are symmetric about y = x: exponential and logarithm, sine and arcsine, tangent and arctangent. Dashed segments join pairs of symmetric points (a, b) and (b, a).](./plots/inverse-functions.py)

The inverse of the exponential function $y = a^x$ ($a > 0$, $a \ne 1$) is the logarithmic function $y = \log_a x$; for $a = \mathrm{e}$ it is written $\ln x$. The trigonometric functions are periodic, hence not bijections, and must first be restricted to an interval of monotonicity.

**Definition 1.2.7 (Inverse Trigonometric Functions)** Restrict $\sin x$, $\cos x$, $\tan x$ and $\cot x$ to $\left[-\frac\pi2, \frac\pi2\right]$, $[0, \pi]$, $\left(-\frac\pi2, \frac\pi2\right)$ and $(0, \pi)$, respectively. Their inverse functions $\arcsin x$, $\arccos x$, $\arctan x$ and $\operatorname{arccot} x$ are collectively called the **inverse trigonometric functions**.

Their properties are as follows:

| Function | Obtained by restricting | Domain | Range | Parity and monotonicity |
|---|---|---|---|---|
| $\arcsin x$ | $\sin x$, $x \in \left[-\frac\pi2, \frac\pi2\right]$ | $[-1, 1]$ | $\left[-\frac\pi2, \frac\pi2\right]$ | odd, strictly increasing |
| $\arccos x$ | $\cos x$, $x \in [0, \pi]$ | $[-1, 1]$ | $[0, \pi]$ | neither odd nor even, strictly decreasing |
| $\arctan x$ | $\tan x$, $x \in \left(-\frac\pi2, \frac\pi2\right)$ | $\mathbb{R}$ | $\left(-\frac\pi2, \frac\pi2\right)$ | odd, strictly increasing |
| $\operatorname{arccot} x$ | $\cot x$, $x \in (0, \pi)$ | $\mathbb{R}$ | $(0, \pi)$ | neither odd nor even, strictly decreasing |

![Graphs of the four inverse trigonometric functions: on the left those with domain [-1, 1], on the right those defined on the whole real line; dashed lines mark the boundaries of the ranges.](./plots/inverse-trig.py)

The inverse trigonometric functions satisfy the following frequently used relations:

1. $\arcsin x + \arccos x = \frac\pi2$, $x \in [-1, 1]$;
2. $\arctan x + \operatorname{arccot} x = \frac\pi2$, $x \in \mathbb{R}$;
3. $\arctan x + \arctan\frac1x = \frac\pi2 \operatorname{sgn} x$, $x \ne 0$ (the sign function $\operatorname{sgn}$ is defined in §1.2.5);
4. $\arctan x + \arctan y = \arctan\frac{x + y}{1 - xy}$ for $xy < 1$; when $xy > 1$, add $\pi$ (if $x > 0$) or $-\pi$ (if $x < 0$) to the right-hand side;
5. $|\arcsin x| \geq |x|$ for $x \in [-1, 1]$, and $|\arctan x| \leq |x|$ for $x \in \mathbb{R}$.

Relation 4 comes from the addition formula for $\tan(\alpha + \beta)$: with $\alpha = \arctan x$ and $\beta = \arctan y$ we have $\alpha + \beta \in (-\pi, \pi)$, and it lies in $\left(-\frac\pi2, \frac\pi2\right)$ exactly when $xy < 1$.

**Definition 1.2.8 (Composite Function)** Let $y = f(u)$ and $u = g(x)$ be functions with $R(g) \cap D(f) \ne \varnothing$. The function

$$
(f \circ g)(x) = f(g(x)), \quad x \in \{x \in D(g) \mid g(x) \in D(f)\},
$$
is called the **composite function** of $f$ and $g$, and $u$ is called the intermediate variable.

For example, $y = (\sin x)^2$ is the composite of $y = u^2$ and $u = \sin x$ (the chain $y - u - x$), and $y = 3^{\sin(x^2)}$ is the composite of $y = 3^u$, $u = \sin v$ and $v = x^2$ (the chain $y - u - v - x$). Breaking a composite function into a chain of simple functions is the starting point of the chain rule in [Chapter 4](/2.2.4).

**Example 1.2.4** Let $f(x) = \begin{cases} 3x, & 0 \leq x \leq 3, \\ x^2, & 3 < x \leq 5, \end{cases}$ and $g(x) = \ln x$. Find $f(g(x))$ and $g(f(x))$.

**Solution** Split according to which piece of $f$ the value $g(x)$ falls into: $0 \leq \ln x \leq 3 \iff 1 \leq x \leq \mathrm{e}^3$, so

$$
f(g(x)) = \begin{cases} 3\ln x, & 1 \leq x \leq \mathrm{e}^3, \\ (\ln x)^2, & \mathrm{e}^3 < x \leq \mathrm{e}^5; \end{cases}
\qquad
g(f(x)) = \begin{cases} \ln(3x), & 0 < x \leq 3, \\ 2\ln x, & 3 < x \leq 5. \end{cases}
$$
Note that the domain of $g(f(x))$ excludes $x = 0$, where $f(x) = 0$.

**Example 1.2.5** (1) Given $f\left(x + \frac1x\right) = x^2 + \frac1{x^2}$, find $f(x)$. (2) Given $f\left(\frac{x - 1}{x + 1}\right) = 3x$, find $f(x)$.

**Solution** (1) Let $u = x + \frac1x$; then $x^2 + \frac1{x^2} = u^2 - 2$, so $f(x) = x^2 - 2$. Since $\left|x + \frac1x\right| \geq 2$, the domain of this $f$ is $|x| \geq 2$. (2) Let $u = \frac{x - 1}{x + 1}$; solving gives $x = \frac{1 + u}{1 - u}$, so $f(x) = \frac{3(1 + x)}{1 - x}$, $x \ne 1$.

### 1.2.4. Elementary Functions

**Definition 1.2.9 (Basic Elementary Functions)** The following six classes of functions are called the **basic elementary functions**:

1. constant functions $f(x) = c$;
2. power functions $f(x) = x^\alpha$ ($\alpha \in \mathbb{R}$);
3. exponential functions $f(x) = a^x$ ($a > 0$, $a \ne 1$);
4. logarithmic functions $f(x) = \log_a x$ ($a > 0$, $a \ne 1$), including $\lg x$ and $\ln x$;
5. trigonometric functions $\sin x, \cos x, \tan x, \cot x, \sec x, \csc x$;
6. inverse trigonometric functions $\arcsin x, \arccos x, \arctan x, \operatorname{arccot} x$.

**Definition 1.2.10 (Elementary Function)** A function obtained from the basic elementary functions by finitely many arithmetic operations and finitely many compositions is called an **elementary function**.

The domain of the power function $x^\alpha$ depends on $\alpha$: it is $\mathbb{R}$ for $\alpha \in \mathbb{N}_+$, $\mathbb{R} \setminus \{0\}$ for negative integers $\alpha$, and $(0, +\infty)$ for irrational $\alpha$ (in which case $x^\alpha = \mathrm{e}^{\alpha\ln x}$). On $(0, +\infty)$, $x^\alpha$ is strictly increasing for $\alpha > 0$ and strictly decreasing for $\alpha < 0$.

The frequently used trigonometric formulas are collected below; they will be needed again and again for limits, derivatives and integrals (derivations omitted):

| Type | Formulas |
|---|---|
| Pythagorean identities | $\sin^2 x + \cos^2 x = 1$, $1 + \tan^2 x = \sec^2 x$, $1 + \cot^2 x = \csc^2 x$ |
| Addition formulas | $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$, $\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$, $\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$ |
| Double-angle formulas | $\sin 2x = 2\sin x\cos x$, $\cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$, $\tan 2x = \frac{2\tan x}{1 - \tan^2 x}$ |
| Triple-angle formulas | $\sin 3x = 3\sin x - 4\sin^3 x$, $\cos 3x = 4\cos^3 x - 3\cos x$ |
| Half-angle (power-reduction) formulas | $\sin^2\frac x2 = \frac{1 - \cos x}{2}$, $\cos^2\frac x2 = \frac{1 + \cos x}{2}$, $\tan\frac x2 = \frac{\sin x}{1 + \cos x} = \frac{1 - \cos x}{\sin x}$ |
| Tangent half-angle formulas ($t = \tan\frac x2$) | $\sin x = \frac{2t}{1 + t^2}$, $\cos x = \frac{1 - t^2}{1 + t^2}$, $\tan x = \frac{2t}{1 - t^2}$ |
| Product-to-sum formulas | $\sin\alpha\cos\beta = \frac12[\sin(\alpha + \beta) + \sin(\alpha - \beta)]$, $\cos\alpha\cos\beta = \frac12[\cos(\alpha + \beta) + \cos(\alpha - \beta)]$, $\sin\alpha\sin\beta = -\frac12[\cos(\alpha + \beta) - \cos(\alpha - \beta)]$ |
| Sum-to-product formulas | $\sin\alpha \pm \sin\beta = 2\sin\frac{\alpha \pm \beta}2\cos\frac{\alpha \mp \beta}2$, $\cos\alpha + \cos\beta = 2\cos\frac{\alpha + \beta}2\cos\frac{\alpha - \beta}2$, $\cos\alpha - \cos\beta = -2\sin\frac{\alpha + \beta}2\sin\frac{\alpha - \beta}2$ |
| Harmonic addition | $a\sin x + b\cos x = \sqrt{a^2 + b^2}\,\sin(x + \varphi)$, where $\cos\varphi = \frac{a}{\sqrt{a^2 + b^2}}$, $\sin\varphi = \frac{b}{\sqrt{a^2 + b^2}}$ ($\varphi = \arctan\frac ba$ when $a > 0$) |

An important example of elementary functions is the hyperbolic functions, which are built from the exponential function.

**Definition 1.2.11 (Hyperbolic Functions)** The functions

$$
\sinh x = \frac{\mathrm{e}^x - \mathrm{e}^{-x}}{2}, \qquad \cosh x = \frac{\mathrm{e}^x + \mathrm{e}^{-x}}{2}, \qquad \tanh x = \frac{\sinh x}{\cosh x} = \frac{\mathrm{e}^x - \mathrm{e}^{-x}}{\mathrm{e}^x + \mathrm{e}^{-x}}
$$
are called the hyperbolic sine, hyperbolic cosine and hyperbolic tangent, and $\coth x = \frac{1}{\tanh x}$, $\operatorname{sech} x = \frac{1}{\cosh x}$, $\operatorname{csch} x = \frac{1}{\sinh x}$ are called the hyperbolic cotangent, hyperbolic secant and hyperbolic cosecant. Together they are called the **hyperbolic functions**.

| Function | Domain | Range | Parity | Inverse function |
|---|---|---|---|---|
| $\sinh x$ | $\mathbb{R}$ | $\mathbb{R}$ | odd | $\operatorname{arsinh} x = \ln\bigl(x + \sqrt{x^2 + 1}\bigr)$, $x \in \mathbb{R}$ |
| $\cosh x$ | $\mathbb{R}$ | $[1, +\infty)$ | even | $\operatorname{arcosh} x = \ln\bigl(x + \sqrt{x^2 - 1}\bigr)$, $x \geq 1$ (the branch with values in $[0, +\infty)$) |
| $\tanh x$ | $\mathbb{R}$ | $(-1, 1)$ | odd | $\operatorname{artanh} x = \frac12\ln\frac{1 + x}{1 - x}$, $\lvert x \rvert < 1$ |
| $\coth x$ | $\mathbb{R} \setminus \{0\}$ | $(-\infty, -1) \cup (1, +\infty)$ | odd | $\operatorname{arcoth} x = \frac12\ln\frac{x + 1}{x - 1}$, $\lvert x \rvert > 1$ |

The identities for hyperbolic functions parallel those for trigonometric functions, up to some signs:

$$
\cosh^2 x - \sinh^2 x = 1, \qquad 1 - \tanh^2 x = \operatorname{sech}^2 x,
$$

$$
\sinh(x \pm y) = \sinh x\cosh y \pm \cosh x\sinh y, \qquad \cosh(x \pm y) = \cosh x\cosh y \pm \sinh x\sinh y,
$$

$$
\sinh 2x = 2\sinh x\cosh x, \qquad \cosh 2x = \cosh^2 x + \sinh^2 x.
$$

The first identity says that the point $(\cosh t, \sinh t)$ lies on the right branch of the hyperbola $x^2 - y^2 = 1$, just as $(\cos t, \sin t)$ lies on the unit circle; hence the name "hyperbolic." The parameter $t$ is exactly twice the area of the corresponding sector (this can be verified with definite integrals in [Chapter 7](/2.2.7)).

![Left: graphs of the hyperbolic functions; for large x both cosh x and sinh x are close to e^x/2. Right: parameter points on the unit circle and on the unit hyperbola; both shaded sectors have area t/2.](./plots/hyperbolic-functions.py)

### 1.2.5. Non-elementary Functions

Functions that are not elementary are just as common in calculus. There are three main kinds.

A piecewise function is given by different expressions on different parts of its domain. A piecewise function may be elementary (for example, $|x| = \sqrt{x^2}$) or not.

**Definition 1.2.12 (Sign Function)** The function

$$
\operatorname{sgn} x = \begin{cases} 1, & x > 0, \\ 0, & x = 0, \\ -1, & x < 0 \end{cases}
$$
is called the **sign function**. For every $x$ we have $x = |x|\operatorname{sgn} x$.

**Definition 1.2.13 (Floor Function)** For $x \in \mathbb{R}$, the greatest integer not exceeding $x$ is called the integer part of $x$, denoted $\lfloor x \rfloor$:

$$
\lfloor x \rfloor = n, \quad n \leq x < n + 1, \ n \in \mathbb{Z}.
$$
The function $y = \lfloor x \rfloor$ is called the **floor function**.

By definition, $x - 1 < \lfloor x \rfloor \leq x$; this inequality is useful when computing limits by squeezing ([Chapter 2](/2.2.2#sec-2.4.3)). For example, $\lfloor 2.5 \rfloor = 2$ and $\lfloor -2.5 \rfloor = -3$. The floor function "jumps" at every integer and is a typical example of a discontinuity of the first kind ([Chapter 3](/2.2.3)).

For an implicit function, the relation between the independent and the dependent variable is given by an equation $F(x, y) = 0$ rather than directly by $y = f(x)$.

**Definition 1.2.14 (Implicit Function)** Let $D \subseteq \mathbb{R}$ be nonempty. If for every $x \in D$ the equation $F(x, y) = 0$ has a unique solution $y$, then the function $y = y(x)$, $x \in D$, so determined is called the **implicit function** defined by the equation $F(x, y) = 0$.

An equation need not determine a unique function: under the restrictions $y \geq 0$ and $y \leq 0$, the equation $x^2 + y^2 = 1$ determines $y = \sqrt{1 - x^2}$ and $y = -\sqrt{1 - x^2}$, respectively. When an implicit function exists and whether it is differentiable are questions answered by the implicit function theorem of multivariable calculus ([2.2.10](/2.2.10)).

**Example 1.2.6** For $x < 0$, does the equation $2^y = xy + 2$ determine $y$ as a function of $x$?

**Solution** Fix $x_0 < 0$ and consider, in the $(y, u)$-plane, the curve $u = 2^y$ and the line $u = x_0 y + 2$. The former is strictly increasing and takes every value in $(0, +\infty)$; the latter is strictly decreasing and takes every value in $\mathbb{R}$; so they meet in exactly one point $(y_0, u_0)$. Hence for every $x_0 < 0$ the equation has exactly one solution $y_0$, and it determines an implicit function on $(-\infty, 0)$.

A function given by parametric equations has the form

$$
\begin{cases} x = x(t), \\ y = y(t), \end{cases} \quad t \in I.
$$
For example, the ellipse has the parametric equations $x = a\cos\theta$, $y = b\sin\theta$ ($a, b > 0$, $0 \leq \theta < 2\pi$); taking only $0 \leq \theta \leq \pi$ gives the upper half of the ellipse, which determines the function $y = \frac ba\sqrt{a^2 - x^2}$, $x \in [-a, a]$. If $x(t)$ is strictly monotonic, the parametric equations determine the function $y = y\bigl(x^{-1}(x)\bigr)$; the rule for differentiating it is given in [Chapter 4](/2.2.4).

## Summary

| Topic | Key points |
|---|---|
| Neighborhoods | $N(x_0, \delta) = (x_0 - \delta, x_0 + \delta)$; the punctured neighborhood $N^*(x_0, \delta)$ removes the center |
| Least-upper-bound property | Every nonempty set of real numbers that is bounded above has a supremum (completeness of the real numbers, taken as an axiom) |
| Characterization of suprema | $b = \sup E \iff$ $b$ is an upper bound and $\forall \varepsilon > 0$, $\exists x \in E$, $x > b - \varepsilon$ |
| Archimedean property, density | $\forall p, q > 0$, $\exists N$, $Np > q$; every open interval contains rational numbers |
| Properties of functions | Parity (symmetric domain), monotonicity (depends on the interval), periodicity (a fundamental period need not exist), boundedness (depends on the set) |
| Inverse functions | Only bijections have inverses; the graphs are symmetric about $y = x$; a strictly monotonic function has an inverse that is monotonic in the same sense |
| Elementary functions | The six classes of basic elementary functions combined by finitely many arithmetic operations and compositions; hyperbolic functions, $\cosh^2 x - \sinh^2 x = 1$ |
| Non-elementary functions | Piecewise functions ($\operatorname{sgn} x$, $\lfloor x \rfloor$, the Dirichlet function), implicit functions, parametric equations |
