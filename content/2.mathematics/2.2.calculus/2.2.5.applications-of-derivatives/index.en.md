---
title: Studying Functions with Derivatives
source_hash: 58fcf68a51bf
---

The previous chapter ([2.2.4](/2.2.4)) defined the **derivative** and established the rules of differentiation; this chapter uses derivatives to study functions themselves: monotonicity, local and global extrema, convexity and inflection points, asymptotes and curve sketching, as well as computing limits with derivatives (L'Hôpital's rule), proving inequalities, and approximating functions by polynomials (Taylor's formula). The bridge between derivatives (local information) and function values (global information) is the mean value theorem, which relies on the **extreme value theorem** for **continuous functions** on closed intervals ([2.2.3](/2.2.3)); almost everything else in the chapter follows from it. Taylor's formula is the other core topic of the chapter: it pushes the idea of **equivalent infinitesimals** to arbitrary order, is a powerful tool for computing limits and estimating errors, and underlies the Taylor series of [2.2.9](/2.2.9) as well as the multivariable Taylor formula and the tests for extrema in [2.2.11](/2.2.11). Convex functions and Jensen's inequality are also used frequently in probability theory.

## 5.1. Mean Value Theorems

### 5.1.1. Local Extrema and Fermat's Theorem

**Definition 5.1.1 (Local Extremum)** If there is a neighborhood $N(x_0,\delta)$ of $x_0$ such that $f(x)\le f(x_0)$ ($f(x)\ge f(x_0)$) for all $x$ in it, then $x_0$ is called a local maximum point (local minimum point) of $f$, and $f(x_0)$ is called a **local maximum** (**local minimum**) of $f$. Local maxima and local minima are each called a **local extremum**, and local maximum and minimum points are collectively called local extreme points.

A local extremum is a local notion: a local maximum need not exceed a local minimum, nor need it be the global maximum; moreover, a local extreme point must be an interior point of the domain.

**Theorem 5.1.1 (Fermat's Theorem)** If $f$ has a local extremum at $x_0$ and $f'(x_0)$ exists, then $f'(x_0) = 0$.

**Proof** Without loss of generality let $f$ have a local maximum at $x_0$. Then $f(x)-f(x_0)\le0$ near $x_0$, so

$$
f'_+(x_0) = \lim_{x\to x_0^+}\frac{f(x)-f(x_0)}{x-x_0}\le0,\qquad f'_-(x_0) = \lim_{x\to x_0^-}\frac{f(x)-f(x_0)}{x-x_0}\ge0.
$$

Since $f'(x_0) = f'_-(x_0) = f'_+(x_0)$, we get $f'(x_0) = 0$. $\square$

**Definition 5.1.2** A point $x_0$ with $f'(x_0) = 0$ is called a **stationary point** of $f$ (also called a critical point).

Fermat's theorem says that for differentiable functions, "the derivative vanishes" is a necessary condition for a local extremum, but not a sufficient one, as $x^3$ at $0$ shows. Geometrically, the tangent line at a local extreme point where the function is differentiable is horizontal.

### 5.1.2. Rolle's Theorem and the Lagrange Mean Value Theorem

Below, "$f$ is continuous on $[a,b]$ and differentiable on $(a,b)$" is written as "$f\in C[a,b]$ and $f$ is differentiable on $(a,b)$."

**Theorem 5.1.2 (Rolle's Theorem)** Let $f\in C[a,b]$ be differentiable on $(a,b)$ with $f(a) = f(b)$. Then there exists $\xi\in(a,b)$ such that $f'(\xi) = 0$.

**Proof** By the **extreme value theorem**, $f$ has a maximum $M$ and a minimum $m$ on $[a,b]$. If $M = m$, then $f$ is constant and any $\xi\in(a,b)$ works. If $M>m$, then since $f(a) = f(b)$, at least one of $M$ and $m$ is attained at an interior point $\xi\in(a,b)$; this $\xi$ is a local extreme point, and $f'(\xi) = 0$ by Fermat's theorem. $\square$

**Theorem 5.1.3 (Lagrange Mean Value Theorem)** Let $f\in C[a,b]$ be differentiable on $(a,b)$. Then there exists $\xi\in(a,b)$ such that

$$
f'(\xi) = \frac{f(b)-f(a)}{b-a}.
$$

**Proof** Construct the auxiliary function (the difference between the ordinates of the curve and of the chord) $\varphi(x) = f(x)-\frac{f(b)-f(a)}{b-a}(x-a)$. Then $\varphi\in C[a,b]$, $\varphi$ is differentiable on $(a,b)$, and $\varphi(a) = \varphi(b) = f(a)$. By Rolle's theorem there exists $\xi\in(a,b)$ with $\varphi'(\xi) = f'(\xi)-\frac{f(b)-f(a)}{b-a} = 0$. $\square$

Geometric meaning: at some point of the curve $y = f(x)$ the tangent line is parallel to the chord joining the endpoints; Rolle's theorem is the special case of a horizontal chord. Kinematic meaning: the average velocity is attained as the instantaneous velocity at some moment. The Lagrange mean value theorem is often written as the finite increment formula

$$
f(b)-f(a) = f'(\xi)(b-a),\quad\xi\in(a,b),\qquad\text{or}\qquad f(b)-f(a) = f'\bigl(a+\theta(b-a)\bigr)(b-a),\quad0<\theta<1.
$$

The latter form also holds for $a>b$. Compared with $\Delta y\approx f'(x_0)\Delta x$, it is an exact equality, at the price of not knowing where $\xi$ is.

![The Lagrange mean value theorem: at ξ₁ and ξ₂ the tangent lines to the curve are parallel to the chord joining (a, f(a)) and (b, f(b)).](./plots/mean-value-theorem.py)

**Corollary 5.1.1** (1) If $f'(x)\equiv0$ on an interval $I$, then $f$ is constant on $I$; (2) if $f'(x)\equiv g'(x)$ on $I$, then $f(x) = g(x)+c$ for some constant $c$.

**Proof** (1) For any $x_1<x_2$ in $I$, $f(x_2)-f(x_1) = f'(\xi)(x_2-x_1) = 0$. (2) Apply (1) to $f-g$. $\square$

Corollary 5.1.1 (2) is the reason why, in [2.2.6](/2.2.6), "two antiderivatives differ by a constant."

**Corollary 5.1.2 (Test for Monotonicity)** Let $f\in C[a,b]$ be differentiable on $(a,b)$.

1. If $f'(x)\ge0$ ($\le0$) on $(a,b)$, then $f$ is nondecreasing (nonincreasing) on $[a,b]$;
2. If $f'(x)>0$ ($<0$) on $(a,b)$, then $f$ is strictly increasing (decreasing) on $[a,b]$;
3. If $f$ is nondecreasing (nonincreasing) on $[a,b]$, then $f'(x)\ge0$ ($\le0$) on $(a,b)$.

**Proof** 1 and 2: for any $a\le x<y\le b$, $f(y)-f(x) = f'(\xi)(y-x)$ with $\xi\in(x,y)$, and the sign is determined by $f'(\xi)$. 3: if $f$ is nondecreasing, the difference quotients satisfy $\frac{f(x+h)-f(x)}{h}\ge0$, and passing to the limit gives the result. $\square$

Thus 1 and 3 together give a necessary and sufficient condition for **monotonic functions** (in the non-strict sense); 2 is only a sufficient condition: $y = x^3$ is strictly increasing, but $y'(0) = 0$.

Rolle's theorem is often used to count zeros of a function: if $f$ has $k$ distinct zeros, then $f'$ has at least $k-1$ distinct zeros.

**Example 5.1.1** Prove that the equation $\mathrm{e}^x = ax^2+bx+c$ has at most 3 real roots.

**Proof** Suppose $f(x) = \mathrm{e}^x-ax^2-bx-c$ has 4 zeros $x_1<x_2<x_3<x_4$. By Rolle's theorem, $f'(x) = \mathrm{e}^x-2ax-b$ has at least 3 distinct zeros, $f''(x) = \mathrm{e}^x-2a$ at least 2, and $f'''(x) = \mathrm{e}^x$ at least 1, a contradiction. $\square$

**Example 5.1.2** Prove that $P_n(x) = \frac{\mathrm{d}^n}{\mathrm{d}x^n}(x^2-1)^n$ has exactly $n$ distinct zeros in $(-1,1)$.

**Proof** Let $f(x) = (x^2-1)^n = (x-1)^n(x+1)^n$. Then $\pm1$ are zeros of $f, f', \dots, f^{(n-1)}$. By Rolle's theorem, $f'$ has a zero in $(-1,1)$, so together with $\pm1$, $f'$ has 3 zeros in $[-1,1]$; hence $f''$ has 2 zeros in $(-1,1)$ and 4 in $[-1,1]$; continuing in this way, $f^{(n-1)}$ has $n+1$ zeros in $[-1,1]$, and $f^{(n)} = P_n$ has at least $n$ distinct zeros in $(-1,1)$. Since $P_n$ is a **polynomial** of degree $2n-n = n$, it has at most $n$ zeros, hence exactly $n$. $\square$

(Up to a constant factor, $P_n$ is the Legendre polynomial of degree $n$.)

**Example 5.1.3** Prove that $\frac{x}{1+x}<\ln(1+x)<x$ for $x>0$, and that $\lim\limits_{n\to\infty}\Bigl(\sum\limits_{k=1}^n\frac1k-\ln n\Bigr)$ exists.

**Proof** Apply the Lagrange mean value theorem to $\ln t$ on $[1,1+x]$: $\ln(1+x) = \frac{x}{\xi}$ with $\xi\in(1,1+x)$, whence $\frac{x}{1+x}<\ln(1+x)<x$. Replacing $x$ by $\frac1n$ gives

$$
\frac{1}{n+1}<\ln\Bigl(1+\frac1n\Bigr)<\frac1n.
$$

Let $a_n = \sum_{k=1}^n\frac1k-\ln n$. Then $a_{n+1}-a_n = \frac1{n+1}-\ln\bigl(1+\frac1n\bigr)<0$, so $\{a_n\}$ is strictly decreasing; moreover, $\ln n = \sum_{k=1}^{n-1}\ln\bigl(1+\frac1k\bigr)$, so

$$
a_n = \sum_{k=1}^{n-1}\Bigl[\frac1k-\ln\Bigl(1+\frac1k\Bigr)\Bigr]+\frac1n>0,
$$

and $\{a_n\}$ is bounded below. By the **monotone convergence theorem**, $\{a_n\}$ converges; its limit is denoted $\gamma$ (the Euler–Mascheroni constant, $\gamma\approx0.5772$), that is, $1+\frac12+\cdots+\frac1n = \ln n+\gamma+o(1)$. $\square$

**Example 5.1.4** Prove that $f(x) = \bigl(1+\frac1x\bigr)^x$ is strictly increasing on $(0,+\infty)$.

**Proof** $f'(x) = \bigl(1+\frac1x\bigr)^x\Bigl[\ln\bigl(1+\frac1x\bigr)-\frac{1}{x+1}\Bigr]>0$ by the inequality of Example 5.1.3. $\square$

**Example 5.1.5** Let $b>a>0$. Prove: (1) $b^p-a^p<(b-a)^p$ for $0<p<1$; (2) $b^p-a^p>(b-a)^p$ for $p>1$.

**Proof** Let $f(x) = x^p-a^p-(x-a)^p$ ($x\ge a$). Then $f(a) = 0$ and $f'(x) = p\bigl[x^{p-1}-(x-a)^{p-1}\bigr]$. For $0<p<1$, $f'(x)<0$ for $x>a$, so $f$ is strictly decreasing on $[a,+\infty)$ and $f(b)<f(a) = 0$; for $p>1$, $f'(x)>0$ and $f(b)>0$. $\square$

In particular, $\sqrt[n]{b}-\sqrt[n]{a}<\sqrt[n]{b-a}$ ($n\ge2$).

**Example 5.1.6** Let $f$ be twice differentiable on $(-\infty,+\infty)$ with $f''\equiv0$. Prove that $f(x) = ax+b$.

**Proof** By Corollary 5.1.1, $f'\equiv a$; then by the Lagrange mean value theorem $f(x)-f(0) = f'(\xi)x = ax$, so $f(x) = ax+b$ with $b = f(0)$. $\square$

By induction: if $f^{(n+1)}\equiv0$, then $f$ is a polynomial of degree at most $n$.

### 5.1.3. Cauchy's Mean Value Theorem

**Theorem 5.1.4 (Cauchy's Mean Value Theorem)** Let $f, g\in C[a,b]$ be differentiable on $(a,b)$ with $g'(x)\ne0$ on $(a,b)$. Then there exists $\xi\in(a,b)$ such that

$$
\frac{f'(\xi)}{g'(\xi)} = \frac{f(b)-f(a)}{g(b)-g(a)}.
$$

**Proof** First, $g(b)\ne g(a)$: otherwise, by Rolle's theorem, $g'$ would have a zero in $(a,b)$. Let

$$
\varphi(x) = f(x)-\frac{f(b)-f(a)}{g(b)-g(a)}\bigl(g(x)-g(a)\bigr).
$$

Then $\varphi(a) = \varphi(b) = f(a)$, and by Rolle's theorem there exists $\xi$ with $\varphi'(\xi) = f'(\xi)-\frac{f(b)-f(a)}{g(b)-g(a)}g'(\xi) = 0$. $\square$

Another interpretation: regard $(g(t), f(t))$ ($t\in[a,b]$) as parametric equations of a plane curve. Then $\frac{f(b)-f(a)}{g(b)-g(a)}$ is the slope of the chord and $\frac{f'(\xi)}{g'(\xi)}$ is the slope of the tangent line at $t = \xi$ (Section 4.3.2), so the theorem is the Lagrange mean value theorem for a parametric curve. Taking $g(x) = x$ recovers the Lagrange mean value theorem. Note that one cannot apply the Lagrange mean value theorem separately to the numerator and the denominator and then divide: the two intermediate points so obtained are in general different.

### 5.1.4. The Intermediate Value Property of Derivatives and Mean Value Problems

**Theorem 5.1.5 (Darboux's Theorem)** Let $f$ be differentiable on $[a,b]$ (with one-sided derivatives at the endpoints), $f'_+(a)\ne f'_-(b)$, and let $\mu$ lie between $f'_+(a)$ and $f'_-(b)$. Then there exists $\xi\in(a,b)$ such that $f'(\xi) = \mu$.

This theorem is also called the intermediate value theorem for derivatives: even when a derivative is discontinuous, it has the intermediate value property, just like a continuous function.

**Proof** Without loss of generality let $f'_+(a)<\mu<f'_-(b)$. Let $h(x) = f(x)-\mu x$. Then $h$ is continuous on $[a,b]$, $h'_+(a) = f'_+(a)-\mu<0$ and $h'_-(b) = f'_-(b)-\mu>0$. Since $h'_+(a)<0$, we have $h(x)<h(a)$ for $x$ just to the right of $a$; since $h'_-(b)>0$, we have $h(x)<h(b)$ for $x$ just to the left of $b$. Hence the minimum of $h$ on $[a,b]$ can only be attained at an interior point $\xi$, and by Fermat's theorem $h'(\xi) = f'(\xi)-\mu = 0$. $\square$

Consequence: a derivative cannot have a **discontinuity of the first kind**. For example, the sign function $\operatorname{sgn}x$ has a jump at $0$, so it is not the derivative of any function on $\mathbb{R}$ (this concerns the existence of antiderivatives in [2.2.6](/2.2.6)).

To prove that "there exists $\xi$ satisfying some equation involving $f(\xi)$ and $f'(\xi)$," the key is to construct an auxiliary function $h$ for which the desired equation is exactly $h'(\xi) = 0$, and then to check that $h$ satisfies the hypotheses of Rolle's theorem; alternatively, rearrange the equation into the form $\frac{f'(\xi)}{g'(\xi)}$ and use Cauchy's mean value theorem.

**Example 5.1.7** Let $f, g\in C[a,b]$ be differentiable on $(a,b)$ with $f(a) = f(b) = 0$. Prove that there exists $\xi\in(a,b)$ such that $f'(\xi)+g'(\xi)f(\xi) = 0$.

**Proof** Let $h(x) = \mathrm{e}^{g(x)}f(x)$. Then $h(a) = h(b) = 0$. By Rolle's theorem there exists $\xi$ with $h'(\xi) = \mathrm{e}^{g(\xi)}\bigl(f'(\xi)+g'(\xi)f(\xi)\bigr) = 0$, and $\mathrm{e}^{g(\xi)}>0$. $\square$

Where the factor $\mathrm{e}^{g}$ comes from: we want $(\mathrm{e}^{g}f)' = \mathrm{e}^{g}(f'+g'f)$; this is the same idea as the integrating factor for first-order linear differential equations ([2.2.15](/2.2.15)).

**Example 5.1.8** Let $f\in C[1,2]$ be differentiable on $(1,2)$. Prove: (1) there exists $\xi\in(1,2)$ such that $f(2)-f(1) = \frac12\xi^2f'(\xi)$; (2) there exists $\eta\in(1,2)$ such that $f(2)-f(1) = \eta f'(\eta)\ln2$.

**Proof** (1) Take $g(x) = \frac1x$; Cauchy's mean value theorem gives $\frac{f(2)-f(1)}{\frac12-1} = \frac{f'(\xi)}{-1/\xi^2}$, which is the claim. (2) Take $g(x) = \ln x$: $\frac{f(2)-f(1)}{\ln2} = \frac{f'(\eta)}{1/\eta}$. $\square$

**Example 5.1.9 (Constructing Auxiliary Functions)** Let $f\in C[0,2]$ be differentiable on $(0,2)$ with $f(1) = 0$. With the auxiliary functions in parentheses one can prove:

1. there exists $\xi\in(0,1)$ with $f(\xi)+\xi f'(\xi) = 0$ ($h(x) = xf(x)$, Rolle's theorem on $[0,1]$);
2. there exists $\xi\in(1,2)$ with $f(\xi) = (2-\xi)f'(\xi)$ ($h(x) = (x-2)f(x)$);
3. there exists $\xi\in(0,2)$ with $f\bigl(\frac\xi2\bigr)+\frac\xi2f'\bigl(\frac\xi2\bigr) = 0$ ($h(x) = xf\bigl(\frac x2\bigr)$, $h(0) = h(2) = 0$);
4. there exists $\xi\in(0,1)$ with $f(1)-f(0) = \sqrt{1-\xi^2}\,\frac{\pi}{2}f'(\xi)$ ($g(x) = \arcsin x$, Cauchy's mean value theorem);
5. there exists $\xi\in(0,2)$ with $f(2)-f(0) = (1+\xi^2)\arctan2\cdot f'(\xi)$ ($g(x) = \arctan x$, Cauchy's mean value theorem).

## 5.2. L'Hôpital's Rule

The limit of a ratio of two infinitesimals or of two infinitely large quantities can be anything, or may fail to exist; such limits are called *indeterminate forms*, of type $\frac00$ and $\frac\infty\infty$, respectively. We have already handled some indeterminate forms by substituting **equivalent infinitesimals**; Cauchy's mean value theorem provides a more systematic method: replace the ratio of the functions by the ratio of their derivatives.

**Theorem 5.2.1 (L'Hôpital's Rule)** Suppose that

1. $\lim\limits_{x\to x_0^-}f(x) = \lim\limits_{x\to x_0^-}g(x) = 0$;
2. there exists $\delta>0$ such that $f$ and $g$ are differentiable on $(x_0-\delta,x_0)$ and $g'(x)\ne0$ there;
3. $\lim\limits_{x\to x_0^-}\frac{f'(x)}{g'(x)} = a$ ($a$ a real number, or $+\infty$, $-\infty$, $\infty$).

Then $\lim\limits_{x\to x_0^-}\frac{f(x)}{g(x)} = a$. The same conclusion holds for $x\to x_0^+$ and $x\to x_0$ (with the interval of differentiability taken to be $(x_0,x_0+\delta)$ and the punctured neighborhood $N^*(x_0,\delta)$, respectively).

**Proof** Define $f(x_0) = g(x_0) = 0$; then $f$ and $g$ are continuous on $(x_0-\delta,x_0]$. For every $x\in(x_0-\delta,x_0)$, $f$ and $g$ satisfy the hypotheses of Cauchy's mean value theorem on $[x,x_0]$, so there exists $\xi_x\in(x,x_0)$ with

$$
\frac{f(x)}{g(x)} = \frac{f(x)-f(x_0)}{g(x)-g(x_0)} = \frac{f'(\xi_x)}{g'(\xi_x)}.
$$

As $x\to x_0^-$, $\xi_x\to x_0^-$, and condition 3 gives $\frac{f(x)}{g(x)}\to a$. $\square$

**Theorem 5.2.2** Let $\lim\limits_{x\to+\infty}f(x) = \lim\limits_{x\to+\infty}g(x) = 0$, let $f$ and $g$ be differentiable on $[b,+\infty)$ with $g'(x)\ne0$, and let $\lim\limits_{x\to+\infty}\frac{f'(x)}{g'(x)} = a$ ($a$ real, or $\pm\infty$, $\infty$). Then $\lim\limits_{x\to+\infty}\frac{f(x)}{g(x)} = a$. The same conclusion holds for $x\to-\infty$ (with differentiability on $(-\infty,b]$) and for $x\to\infty$.

**Proof** Let $x = \frac1u$, $F(u) = f\bigl(\frac1u\bigr)$ and $G(u) = g\bigl(\frac1u\bigr)$. Then $x\to+\infty\iff u\to0^+$, and $\frac{F'(u)}{G'(u)} = \frac{-f'(1/u)/u^2}{-g'(1/u)/u^2} = \frac{f'(x)}{g'(x)}$; apply Theorem 5.2.1 to $F$ and $G$. $\square$

**Theorem 5.2.3 (Type $\frac\infty\infty$)** In Theorems 5.2.1 and 5.2.2, if condition 1 is replaced by $\lim f(x) = \lim g(x) = \infty$, the conclusion still holds. In fact only $\lim g(x) = \infty$ is needed, with no requirement on the limit of $f$ (type $\frac{*}{\infty}$).

**Proof** (Case $x\to x_0^-$ with $a$ finite.) Given $\varepsilon>0$, choose $c\in(x_0-\delta,x_0)$ such that $\bigl\lvert\frac{f'}{g'}-a\bigr\rvert<\varepsilon$ on $(c,x_0)$. For $x\in(c,x_0)$, Cauchy's mean value theorem gives $\frac{f(x)-f(c)}{g(x)-g(c)} = \frac{f'(\xi)}{g'(\xi)}$ with $\xi\in(c,x)$, so

$$
\frac{f(x)}{g(x)} = \frac{f'(\xi)}{g'(\xi)}\Bigl(1-\frac{g(c)}{g(x)}\Bigr)+\frac{f(c)}{g(x)}.
$$

Fix $c$ and let $x\to x_0^-$. Since $g(x)\to\infty$, the expression in parentheses tends to $1$ and the last term tends to $0$, so $\limsup\bigl\lvert\frac{f(x)}{g(x)}-a\bigr\rvert\le\varepsilon$. Since $\varepsilon$ is arbitrary, the result follows. The case of infinite $a$ is similar. $\square$

When using L'Hôpital's rule, keep in mind:

- At each step, first verify that the limit is of type $\frac00$ or $\frac\infty\infty$. If the derivatives of $f$ and $g$ of orders $1$ through $n-1$ still tend to $0$ (or $\infty$) in the limit process and $\lim\frac{f^{(n)}}{g^{(n)}} = a$, the rule can be applied $n$ times in succession: $\lim\frac fg = \lim\frac{f'}{g'} = \cdots = \lim\frac{f^{(n)}}{g^{(n)}} = a$.
- If condition 3 fails, the rule says nothing. For example, $\lim\limits_{x\to\infty}\frac{x+\sin x}{x} = 1$, whereas $\frac{(x+\sin x)'}{x'} = 1+\cos x$ has no limit.
- Substituting equivalent infinitesimals for factors of products and quotients, and splitting off factors with nonzero limits beforehand, often simplifies the differentiation considerably.

**Example 5.2.1** Find $\lim\limits_{x\to0}\frac{\mathrm{e}^x-x-\cos x}{x^2}$.

**Solution** Apply L'Hôpital's rule twice (each time the limit is of type $\frac00$):

$$
\lim_{x\to0}\frac{\mathrm{e}^x-x-\cos x}{x^2} = \lim_{x\to0}\frac{\mathrm{e}^x-1+\sin x}{2x} = \lim_{x\to0}\frac{\mathrm{e}^x+\cos x}{2} = 1.
$$

By contrast, for $\lim\limits_{x\to0}\frac{\mathrm{e}^x-\cos x}{x^2}$, writing $\lim\frac{\mathrm{e}^x+\sin x}{2x} = \lim\frac{\mathrm{e}^x+\cos x}{2} = 1$ is wrong: after the first step the numerator tends to $1$, and the limit is no longer an indeterminate form. The correct result is $\lim\frac{\mathrm{e}^x+\sin x}{2x} = \infty$.

**Example 5.2.2** Find $\lim\limits_{x\to0}\frac{x-\sin x}{x-x\cos x}$.

**Solution** Method 1: apply L'Hôpital's rule three times directly:

$$
\lim_{x\to0}\frac{1-\cos x}{1-\cos x+x\sin x} = \lim_{x\to0}\frac{\sin x}{2\sin x+x\cos x} = \lim_{x\to0}\frac{\cos x}{3\cos x-x\sin x} = \frac13.
$$

Method 2: first replace $1-\cos x$ in the denominator by $\frac{x^2}2$, then apply L'Hôpital's rule:

$$
\lim_{x\to0}\frac{x-\sin x}{x(1-\cos x)} = \lim_{x\to0}\frac{x-\sin x}{\frac12x^3} = \lim_{x\to0}\frac{1-\cos x}{\frac32x^2} = \frac13.
$$

**Example 5.2.3** Find $\lim\limits_{x\to+\infty}\frac{\frac\pi2-\arctan x}{\sin\frac1x}$.

**Solution** Since $\sin\frac1x\sim\frac1x$,

$$
\lim_{x\to+\infty}\frac{\frac\pi2-\arctan x}{1/x} = \lim_{x\to+\infty}\frac{-1/(1+x^2)}{-1/x^2} = \lim_{x\to+\infty}\frac{x^2}{1+x^2} = 1.
$$

**Example 5.2.4** Prove that $\lim\limits_{x\to+\infty}\frac{x^\alpha}{a^x} = 0$ ($a>1$, $\alpha>0$).

**Proof** Choose a positive integer $k$ with $k-1<\alpha\le k$ and apply L'Hôpital's rule $k$ times in succession (each time the limit is of type $\frac\infty\infty$):

$$
\lim_{x\to+\infty}\frac{x^\alpha}{a^x} = \lim_{x\to+\infty}\frac{\alpha x^{\alpha-1}}{a^x\ln a} = \cdots = \lim_{x\to+\infty}\frac{\alpha(\alpha-1)\cdots(\alpha-k+1)x^{\alpha-k}}{(\ln a)^ka^x} = 0. \qquad\square
$$

**Example 5.2.5** Prove that $\lim\limits_{x\to+\infty}\frac{(\ln x)^\beta}{x^\alpha} = 0$ for all $\alpha>0$ and $\beta>0$.

**Proof** $\lim\limits_{x\to+\infty}\frac{(\ln x)^\beta}{x^\alpha} = \lim\limits_{x\to+\infty}\frac{\beta(\ln x)^{\beta-1}}{\alpha x^\alpha}$; each application of the rule lowers the power of $\ln x$ by $1$, and after $k$ applications ($k-1<\beta\le k$) the power in the numerator is $\beta-k\le0$, so the limit is $0$. Alternatively, substitute $x = \mathrm{e}^t$ to reduce to Example 5.2.4. $\square$

Examples 5.2.4 and 5.2.5 show that, as $x\to+\infty$, the three kinds of infinitely large quantities grow at rates satisfying

$$
(\ln x)^\beta\ll x^\alpha\ll a^x\qquad(\alpha,\beta>0,\ a>1),
$$

where $u\ll v$ means $u/v\to0$.

Other indeterminate forms. The forms $0\cdot\infty$, $\infty-\infty$, $0^0$, $1^\infty$ and $\infty^0$ can all be reduced to type $\frac00$ or $\frac\infty\infty$:

- $0\cdot\infty$: $fg = \frac{f}{1/g}$ or $\frac{g}{1/f}$;
- $\infty-\infty$: combine into a single fraction or rationalize;
- $0^0$, $1^\infty$, $\infty^0$: $u^v = \mathrm{e}^{v\ln u}$, where the exponent $v\ln u$ is of type $0\cdot\infty$; then pass to the limit using the continuity of the exponential function and the theorem on the **limit of a composite function**.

**Example 5.2.6** Find the limits: (1) $\lim\limits_{x\to0}\Bigl(\frac1{x^2}-\cot^2x\Bigr)$; (2) $\lim\limits_{x\to0^+}\ln x\tan x$; (3) $\lim\limits_{x\to+\infty}\bigl(\frac\pi2-\arctan x\bigr)^{\frac1{\ln x}}$; (4) $\lim\limits_{x\to0^+}(\cot x)^{\frac1{\ln x}}$.

**Solution** (1) Type $\infty-\infty$. Combine into a single fraction and use $\sin^2x\sim x^2$:

$$
\lim_{x\to0}\frac{\sin^2x-x^2\cos^2x}{x^2\sin^2x} = \lim_{x\to0}\frac{\sin^2x-x^2\cos^2x}{x^4} = \lim_{x\to0}\frac{\sin x\cos x-x\cos^2x+x^2\sin x\cos x}{2x^3}.
$$

The numerator equals $\frac12\sin2x-x\cos^2x+\frac12x^2\sin2x$; applying the rule once more,

$$
\lim_{x\to0}\frac{\cos2x-\cos^2x+x\sin2x+x\sin2x+x^2\cos2x}{6x^2} = \lim_{x\to0}\frac{-\sin^2x+2x\sin2x+x^2\cos2x}{6x^2} = \frac{-1+4+1}{6} = \frac23.
$$

(2) Type $0\cdot\infty$: $\lim\limits_{x\to0^+}\frac{\ln x}{\cot x} = \lim\limits_{x\to0^+}\frac{1/x}{-\csc^2x} = -\lim\limits_{x\to0^+}\frac{\sin^2x}{x} = 0$.

(3) Type $0^0$: the exponent $\frac{\ln(\frac\pi2-\arctan x)}{\ln x}$ is of type $\frac\infty\infty$, and

$$
\lim_{x\to+\infty}\frac{\ln(\frac\pi2-\arctan x)}{\ln x} = \lim_{x\to+\infty}\frac{-x}{(\frac\pi2-\arctan x)(1+x^2)} = -1,
$$

where the last step uses the result $\frac\pi2-\arctan x\sim\frac1x$ of Example 5.2.3. Hence the limit is $\mathrm{e}^{-1}$.

(4) Type $\infty^0$:

$$
\lim_{x\to0^+}\frac{\ln\cot x}{\ln x} = \lim_{x\to0^+}\frac{-\csc^2x/\cot x}{1/x} = -\lim_{x\to0^+}\frac{x}{\sin x\cos x} = -1,
$$

so the limit is $\mathrm{e}^{-1}$.

## 5.3. Extrema of Functions and Their Applications

### 5.3.1. Local Extrema of Functions

By Fermat's theorem, a local extreme point of a differentiable function must be a stationary point, but a stationary point is only a candidate. Points of nondifferentiability may also be local extreme points (for example, $|x|$ at $0$). Thus the local extreme points of an elementary function can only be stationary points or points of nondifferentiability, and each must be examined.

**Theorem 5.3.1 (First Derivative Test)** Let $f$ be continuous at $x_0$ and differentiable on some punctured neighborhood $N^*(x_0,\delta)$.

1. If $f'(x)\ge0$ on $(x_0-\delta,x_0)$ and $f'(x)\le0$ on $(x_0,x_0+\delta)$, then $f$ has a local maximum at $x_0$;
2. If $f'(x)\le0$ on $(x_0-\delta,x_0)$ and $f'(x)\ge0$ on $(x_0,x_0+\delta)$, then $f$ has a local minimum at $x_0$.

**Proof** 1. By Corollary 5.1.2, $f$ is nondecreasing on $(x_0-\delta,x_0]$ and nonincreasing on $[x_0,x_0+\delta)$ (here the continuity of $f$ at $x_0$ is used), so $x_0$ is a local maximum point. 2 is similar. $\square$

Continuity at $x_0$ cannot be omitted: $f(x) = |x|$ ($x\ne0$), $f(0) = 1$ satisfies the hypotheses of 2 on both sides of $0$, yet $0$ is a local maximum point. If $f'$ does not change sign at $x_0$, then $x_0$ is not a local extreme point.

**Theorem 5.3.2 (Second Derivative Test)** Let $f$ be differentiable on some neighborhood of $x_0$ with $f'(x_0) = 0$, and suppose $f''(x_0)$ exists. If $f''(x_0)>0$, then $f$ has a local minimum at $x_0$; if $f''(x_0)<0$, then $f$ has a local maximum at $x_0$.

**Proof** Let $f''(x_0)>0$. Since $\lim\limits_{x\to x_0}\frac{f'(x)}{x-x_0} = \lim\limits_{x\to x_0}\frac{f'(x)-f'(x_0)}{x-x_0} = f''(x_0)>0$, local sign preservation for limits of functions gives $\delta>0$ such that $\frac{f'(x)}{x-x_0}>0$ on $N^*(x_0,\delta)$; that is, $f'$ is negative to the left of $x_0$ and positive to the right. By Theorem 5.3.1, $x_0$ is a local minimum point. $\square$

When $f''(x_0) = 0$ the second derivative test fails: $x^4$, $-x^4$ and $x^3$ have, at $0$, a local minimum, a local maximum and no local extremum, respectively. In this case one may use higher-order derivatives (Taylor's formula in Section 5.5) or the first derivative test.

**Example 5.3.1** Find the local extrema of $f(x) = x^{2/3}(x^2-4)$.

**Solution** $f'(x) = \frac23x^{-1/3}(x^2-4)+2x\cdot x^{2/3} = \frac83(x^2-1)x^{-1/3}$; the stationary points are $x = \pm1$, and $x = 0$ is a point of nondifferentiability. Since $f''(x) = \frac89(5x^2+1)x^{-4/3}$ and $f''(\pm1)>0$, $f(\pm1) = -3$ are local minima. Just to the left of $0$, $f'(x)>0$, and just to the right, $f'(x)<0$, so by Theorem 5.3.1 $f(0) = 0$ is a local maximum.

**Example 5.3.2** Let $f(x) = a\sin x+\frac13\sin3x$ have a local extremum at $x = \frac\pi3$. Find $a$ and determine whether the extremum is a maximum or a minimum.

**Solution** $f'(x) = a\cos x+\cos3x$, and $f'\bigl(\frac\pi3\bigr) = \frac a2-1 = 0$ gives $a = 2$. Since $f''(x) = -2\sin x-3\sin3x$ and $f''\bigl(\frac\pi3\bigr) = -\sqrt3<0$, $f\bigl(\frac\pi3\bigr) = \sqrt3$ is a local maximum.

**Example 5.3.3** Let $y = y(x)$ be determined by the equation $2y^3-2y^2+2xy-x^2 = 1$. Find the local extrema of $y(x)$.

**Solution** Differentiating both sides with respect to $x$ gives $(6y^2-4y+2x)y'+2y-2x = 0$, so $y' = \frac{x-y}{3y^2-2y+x}$. From $y' = 0$ we get $x = y$; substituting into the equation gives $2x^3-x^2-1 = (x-1)(2x^2+x+1) = 0$, so $x = 1$ and $y(1) = 1$. At $x = 1$ (using $y' = 0$),

$$
y''(1) = \frac{(1-y')(3y^2-2y+x)-(x-y)(6yy'-2y'+1)}{(3y^2-2y+x)^2}\bigg|_{x=y=1} = \frac{2}{4} = \frac12>0,
$$

so $y(1) = 1$ is a local minimum.

### 5.3.2. Maxima and Minima of Functions

A continuous function on a closed interval always has a maximum and a minimum (the **extreme value theorem**). A point where an extreme value is attained is either a local extreme point in the interior of the interval (hence a stationary point or a point of nondifferentiability) or an endpoint of the interval. So to find the extreme values, it suffices to compare the values of the function at interior stationary points, at points of nondifferentiability and at the endpoints.

**Example 5.3.4** Find the maximum and minimum of $f(x) = \frac{x^2-5x+6}{x^2+1}$ on $[-1,3]$.

**Solution** $f'(x) = \frac{5(x^2-2x-1)}{(x^2+1)^2}$, with stationary points $x_1 = 1-\sqrt2$ and $x_2 = 1+\sqrt2$, both in $[-1,3]$.

$$
f(x_1) = \frac{4+3\sqrt2}{4-2\sqrt2} = \frac{7+5\sqrt2}{2}\approx7.04,\qquad f(x_2) = \frac{4-3\sqrt2}{4+2\sqrt2} = \frac{7-5\sqrt2}{2}\approx-0.036,
$$

and at the endpoints $f(-1) = 6$ and $f(3) = 0$. Comparing, the maximum is $f(1-\sqrt2) = \frac{7+5\sqrt2}{2}$ and the minimum is $f(1+\sqrt2) = \frac{7-5\sqrt2}{2}$.

**Example 5.3.5** Find the maximum and minimum of $f(x) = x\mathrm{e}^{-x^2}$ on $(-\infty,+\infty)$.

**Solution** The interval is unbounded, so we first show that the extreme values exist. As $x\to\infty$, $f(x)\to0$, while $f(1)>0$ and $f(-1)<0$; hence there exists $M>1$ such that $f(-1)<f(x)<f(1)$ for $|x|>M$. The extreme values of $f$ on $[-M,M]$ are then its extreme values on $\mathbb{R}$, and they are not attained at the endpoints $\pm M$, so they are attained at interior stationary points. From $f'(x) = (1-2x^2)\mathrm{e}^{-x^2} = 0$ we get $x = \pm\frac{1}{\sqrt2}$; the maximum is $f\bigl(\frac1{\sqrt2}\bigr) = \frac{1}{\sqrt{2\mathrm{e}}}$ and the minimum is $f\bigl(-\frac1{\sqrt2}\bigr) = -\frac{1}{\sqrt{2\mathrm{e}}}$.

Practical problems often have only one stationary point, in which case the following simple test applies.

**Theorem 5.3.3 (Unique Stationary Point Theorem)** Let $f$ be differentiable everywhere on an interval $I$ and have exactly one stationary point $x_0$ in the interior of $I$. If $f(x_0)$ is a local minimum, then it is the minimum of $f$ on $I$; if $f(x_0)$ is a local maximum, then it is the maximum of $f$ on $I$.

**Proof** Suppose $f(x_0)$ is a local minimum but not the minimum. Then there exists $x_1\in I$ with $f(x_1)<f(x_0)$; without loss of generality $x_1<x_0$. Just to the left of $x_0$ we have $f(x)\ge f(x_0)$. If $f(x) = f(x_0)$ at all these points, then $f$ is constant on an interval, all of whose points are stationary points, contradicting uniqueness; otherwise there exists $x_2\in(x_1,x_0)$ with $f(x_2)>f(x_0)>f(x_1)$. Then the maximum of $f$ on $[x_1,x_0]$ exceeds the values at both endpoints, so it is attained at an interior point $\xi$, which is another stationary point, a contradiction. The case of a local maximum is similar. $\square$

**Example 5.3.6** A source with electromotive force $E$ and internal resistance $r$ is connected to a load resistance $R$. For what $R$ does the load receive the maximum power?

**Solution** The current is $I = \frac{E}{r+R}$, and the power delivered to the load is $P(R) = I^2R = \frac{E^2R}{(r+R)^2}$, $R\in(0,+\infty)$. Setting $P'(R) = \frac{E^2(r-R)}{(r+R)^3} = 0$ gives the unique stationary point $R = r$, and $P''(r) = -\frac{E^2}{8r^3}<0$, so $R = r$ is a local maximum point. By Theorem 5.3.3, the power is maximal for $R = r$, and the maximum power is $\frac{E^2}{4r}$ (impedance matching).

### 5.3.3. Proving Inequalities by Extrema

To prove $f(x)\le g(x)$ ($x\in I$), let $F = g-f$ and find the minimum (or infimum) of $F$ on $I$; if it is nonnegative, the inequality holds. This is often combined with monotonicity: if $F(a) = 0$ and $F'\ge0$, then $F(x)\ge0$ for $x\ge a$.

**Example 5.3.7** Let $p, q, a, b$ be positive numbers with $\frac1p+\frac1q = 1$. Prove that $ab\le\frac{a^p}{p}+\frac{b^q}{q}$.

**Proof** Let $F(x) = \frac{a^p}{p}+\frac{x^q}{q}-ax$ ($x>0$). Then $F'(x) = x^{q-1}-a$, with the unique stationary point $x_0 = a^{\frac1{q-1}}$. Since $\frac1p+\frac1q = 1$, we have $q>1$ and $F''(x_0) = (q-1)x_0^{q-2}>0$, so $x_0$ is a local minimum point, and by Theorem 5.3.3 also the minimum point. Moreover, $\frac{q}{q-1} = p$, so

$$
F(x_0) = \frac{a^p}{p}+\frac{a^{p}}{q}-a^{p} = a^p\Bigl(\frac1p+\frac1q-1\Bigr) = 0.
$$

Hence $F(x)\ge0$, and taking $x = b$ gives the result. $\square$

This inequality is called *Young's inequality for products*; equality holds if and only if $a^p = b^q$. For $p = q = 2$ it reads $ab\le\frac{a^2+b^2}{2}$. From it one can derive Hölder's inequality, which generalizes the **Cauchy–Schwarz inequality**.

**Example 5.3.8** Prove: (1) $\ln(1+x)>\frac{\arctan x}{1+x}$ for $x>0$; (2) $\frac{1}{2^{p-1}}\le x^p+(1-x)^p\le1$ for $x\in[0,1]$ and $p>1$.

**Proof** (1) Let $f(x) = (1+x)\ln(1+x)-\arctan x$. Then $f(0) = 0$, and for $x>0$, $f'(x) = \ln(1+x)+1-\frac1{1+x^2}>0$, so $f$ is strictly increasing on $[0,+\infty)$ and $f(x)>0$.

(2) The extreme values of $f(x) = x^p+(1-x)^p$ on $[0,1]$ can only be attained at the endpoints or at interior stationary points. Setting $f'(x) = p\bigl[x^{p-1}-(1-x)^{p-1}\bigr] = 0$ gives $x = \frac12$. Since $f(0) = f(1) = 1$ and $f\bigl(\frac12\bigr) = \frac1{2^{p-1}}$, the minimum is $\frac1{2^{p-1}}$ and the maximum is $1$. $\square$

**Example 5.3.9** Let $f$ be twice differentiable on $\mathbb{R}$ with $f''>0$. Prove that $f(x+h)+f(x-h)>2f(x)$ for every $x$ and every nonzero real number $h$.

**Proof** Fix $x$ and let $F(h) = f(x+h)+f(x-h)-2f(x)$, so that $F(0) = 0$. Then $F'(h) = f'(x+h)-f'(x-h)$ and $F'(0) = 0$; since $F''(h) = f''(x+h)+f''(x-h)>0$, $F'$ is strictly increasing, so $h = 0$ is the unique stationary point, and it is a local minimum point. By Theorem 5.3.3, $F(0) = 0$ is the minimum, attained only at $0$, so $F(h)>0$ for $h\ne0$. $\square$

(This is a property of the convex functions of Section 5.4: $f\bigl(\frac{u+v}2\bigr)<\frac{f(u)+f(v)}{2}$.)

**Example 5.3.10** Suppose the equation $kx+\frac1{x^2} = 1$ has exactly one root in $(0,+\infty)$. Find $k$.

**Solution** Let $F(x) = kx+\frac1{x^2}-1$ ($x>0$); then $F'(x) = k-\frac2{x^3}$.

- If $k\le0$, then $F'<0$ and $F$ is strictly decreasing; $F\to+\infty$ as $x\to0^+$, and $F\to-\infty$ ($k<0$) or $F\to-1$ ($k = 0$) as $x\to+\infty$; so $F$ has exactly one zero.
- If $k>0$, then $F$ has the unique stationary point $x_0 = \sqrt[3]{2/k}$, $F''(x_0)>0$, and $F(x_0) = \frac{3}{\sqrt[3]4}k^{2/3}-1$ is the minimum. When $F(x_0) = 0$, that is, $k = \frac{2\sqrt3}{9}$, the equation has exactly one root; for $k>\frac{2\sqrt3}9$, $F>0$ and there is no root; for $0<k<\frac{2\sqrt3}9$, $F(x_0)<0$ while $F\to+\infty$ both as $x\to0^+$ and as $x\to+\infty$, so the equation has two roots.

Therefore $k\le0$ or $k = \frac{2\sqrt3}{9}$.

## 5.4. Curve Sketching

### 5.4.1. Convexity of Curves

Monotonicity tells us only whether a curve rises or falls; a rising curve can bend upward (like $\mathrm{e}^x$) or downward (like $\ln x$). Convexity describes the direction of bending: the arc between any two points of the curve lies below (or above) the chord. Let $x = \lambda_1x_1+\lambda_2x_2$ ($\lambda_1,\lambda_2\ge0$, $\lambda_1+\lambda_2 = 1$) be a point between $x_1$ and $x_2$; the corresponding ordinate on the chord is $\lambda_1f(x_1)+\lambda_2f(x_2)$.

**Definition 5.4.1** Let $f$ be defined on $[a,b]$. If for all $x_1,x_2\in[a,b]$ and all nonnegative numbers $\lambda_1,\lambda_2$ with $\lambda_1+\lambda_2 = 1$

$$
f(\lambda_1x_1+\lambda_2x_2)\le\lambda_1f(x_1)+\lambda_2f(x_2),
$$
then $f$ is called a **convex function** on $[a,b]$; if the inequality is reversed ($\ge$), then $f$ is called a **concave function** on $[a,b]$. If the inequality is strict whenever $x_1\ne x_2$ and $\lambda_1\lambda_2\ne0$, then $f$ is said to be strictly convex (concave).

We follow the internationally standard terminology: a convex function has "the arc below the chord," like $x^2$ and $\mathrm{e}^x$; a concave function has "the arc above the chord," like $\ln x$ and $\sqrt x$. (The course slides, following many Chinese textbooks, call these "convex downward" and "convex upward," respectively.) A function $f$ is concave if and only if $-f$ is convex, so below we state results only for convex functions.

**Theorem 5.4.1 (Jensen's Inequality)** $f$ is convex on $[a,b]$ if and only if for all $x_1,\dots,x_n\in[a,b]$ and all nonnegative real numbers $\lambda_i$ with $\lambda_1+\cdots+\lambda_n = 1$,

$$
f(\lambda_1x_1+\cdots+\lambda_nx_n)\le\lambda_1f(x_1)+\cdots+\lambda_nf(x_n).
$$

For concave functions the inequality is reversed.

**Proof** Sufficiency: take $n = 2$. Necessity: induction on $n$; the cases $n = 1, 2$ hold. Suppose the statement holds for $n = k$ and consider $k+1$ points. If $\lambda_k+\lambda_{k+1} = 0$, this reduces to the case $n = k-1$; otherwise, combine the last two terms:

$$
\begin{aligned}
f\Bigl(\sum_{i=1}^{k+1}\lambda_ix_i\Bigr) &= f\Bigl(\sum_{i=1}^{k-1}\lambda_ix_i+(\lambda_k+\lambda_{k+1})\Bigl(\frac{\lambda_k}{\lambda_k+\lambda_{k+1}}x_k+\frac{\lambda_{k+1}}{\lambda_k+\lambda_{k+1}}x_{k+1}\Bigr)\Bigr)\\
&\le\sum_{i=1}^{k-1}\lambda_if(x_i)+(\lambda_k+\lambda_{k+1})f\Bigl(\frac{\lambda_kx_k+\lambda_{k+1}x_{k+1}}{\lambda_k+\lambda_{k+1}}\Bigr)\\
&\le\sum_{i=1}^{k-1}\lambda_if(x_i)+\lambda_kf(x_k)+\lambda_{k+1}f(x_{k+1}),
\end{aligned}
$$

where the first inequality uses the induction hypothesis ($k$ points) and the second uses the case $n = 2$. $\square$

Geometrically, $\sum\lambda_i(x_i,f(x_i))$ is a weighted average (center of mass) of $n$ points on the curve; it lies in the convex polygon spanned by these points, and the region above the graph of a convex function is a convex set. In probability theory, Jensen's inequality reads $f(\mathbb{E}[X])\le\mathbb{E}[f(X)]$.

**Theorem 5.4.2 (Derivative Tests for Convexity)** (1) Let $f\in C[a,b]$ be differentiable on $(a,b)$. Then $f$ is convex (concave) on $[a,b]$ if and only if $f'$ is nondecreasing (nonincreasing) on $(a,b)$.

(2) Let $f\in C[a,b]$ be twice differentiable on $(a,b)$. Then $f$ is convex (concave) on $[a,b]$ if and only if $f''(x)\ge0$ ($\le0$) on $(a,b)$.

**Proof** (1) We treat only convex functions. Necessity: take any $a<x_1<x<x_2<b$ and substitute $x = \frac{x_2-x}{x_2-x_1}x_1+\frac{x-x_1}{x_2-x_1}x_2$ into the definition of convexity; rearranging gives the relation among the slopes of three chords,

$$
\frac{f(x)-f(x_1)}{x-x_1}\le\frac{f(x_2)-f(x_1)}{x_2-x_1}\le\frac{f(x_2)-f(x)}{x_2-x}.
$$

Letting $x\to x_1^+$ on the left and $x\to x_2^-$ on the right gives $f'(x_1)\le\frac{f(x_2)-f(x_1)}{x_2-x_1}\le f'(x_2)$.

Sufficiency: let $f'$ be nondecreasing, $a\le x_1<x_2\le b$, $\lambda_1,\lambda_2>0$, $\lambda_1+\lambda_2 = 1$ and $x = \lambda_1x_1+\lambda_2x_2$. Then $x-x_1 = \lambda_2(x_2-x_1)$ and $x_2-x = \lambda_1(x_2-x_1)$. By the Lagrange mean value theorem there exist $\xi\in(x_1,x)$ and $\eta\in(x,x_2)$ with

$$
\lambda_1f(x_1)+\lambda_2f(x_2)-f(x) = \lambda_1\bigl(f(x_1)-f(x)\bigr)+\lambda_2\bigl(f(x_2)-f(x)\bigr) = \lambda_1\lambda_2(x_2-x_1)\bigl(f'(\eta)-f'(\xi)\bigr)\ge0.
$$

(2) By (1) and Corollary 5.1.2: $f'$ is nondecreasing $\iff$ $f''\ge0$. $\square$

The proof shows that $f$ is strictly convex when $f''>0$. Geometrically, $f$ is convex if and only if the slope of the tangent line increases with $x$, and then the curve lies above each of its tangent lines: $f(x)\ge f(x_0)+f'(x_0)(x-x_0)$.

**Definition 5.4.2** Let $M$ be a point on the curve $y = f(x)$. If the curve has different convexity on the two sides of $M$, then $M$ is called an **inflection point** of the curve.

**Corollary 5.4.1** Let $f$ be differentiable on some neighborhood of $x_0$, and suppose $f''(x_0)$ exists. If $M(x_0,f(x_0))$ is an inflection point, then $f''(x_0) = 0$.

**Proof** By Theorem 5.4.2 (1), $f'$ has opposite monotonicity on the two sides of $x_0$, so $x_0$ is a local extreme point of $f'$, and by Fermat's theorem $(f')'(x_0) = f''(x_0) = 0$. $\square$

Thus inflection points can occur only where $f'' = 0$ or where $f''$ does not exist; for example, $y = \sqrt[3]x$ has no second derivative at $0$, yet $(0,0)$ is an inflection point. Conversely, $f''(x_0) = 0$ does not guarantee an inflection point: $x^4$ has $f'' = 0$ at $0$, but it is convex everywhere.

**Example 5.4.1** Discuss the convexity and inflection points of $y = \mathrm{e}^{-x^2}$.

**Solution** $y' = -2x\mathrm{e}^{-x^2}$ and $y'' = (4x^2-2)\mathrm{e}^{-x^2}$; $y'' = 0$ gives $x = \pm\frac1{\sqrt2}$.

| $x$ | $\bigl(-\infty,-\frac1{\sqrt2}\bigr)$ | $-\frac1{\sqrt2}$ | $\bigl(-\frac1{\sqrt2},\frac1{\sqrt2}\bigr)$ | $\frac1{\sqrt2}$ | $\bigl(\frac1{\sqrt2},+\infty\bigr)$ |
|---|---|---|---|---|---|
| $y''$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $y$ | convex | inflection point | concave | inflection point | convex |

The inflection points are $\bigl(\pm\frac1{\sqrt2},\mathrm{e}^{-1/2}\bigr)$. This bell-shaped curve has the shape of the normal density, and the distance from an inflection point to the axis of symmetry is exactly the standard deviation (here $\sigma = \frac1{\sqrt2}$).

**Example 5.4.2** Prove that if $x_1,\dots,x_n$ are nonnegative real numbers, then $\sqrt[n]{x_1x_2\cdots x_n}\le\frac{x_1+\cdots+x_n}{n}$.

**Proof** On $(0,+\infty)$, $f(x) = \ln x$ has $f''(x) = -\frac1{x^2}<0$, so it is concave by Theorem 5.4.2. By Jensen's inequality (with $\lambda_i = \frac1n$),

$$
\ln\frac{x_1+\cdots+x_n}{n}\ge\frac{\ln x_1+\cdots+\ln x_n}{n} = \ln\sqrt[n]{x_1\cdots x_n},
$$

and the result follows from the monotonicity of $\ln$. If some $x_i$ is $0$, the inequality is obvious. $\square$

This is the *inequality of arithmetic and geometric means*. The same argument gives the weighted form and the power mean form: if $x_i\ge0$, $\lambda_i\ge0$ and $\sum\lambda_i = 1$, then

$$
x_1^{\lambda_1}\cdots x_n^{\lambda_n}\le\lambda_1x_1+\cdots+\lambda_nx_n,\qquad x_1^{\lambda_1}\cdots x_n^{\lambda_n}\le\bigl(\lambda_1x_1^q+\cdots+\lambda_nx_n^q\bigr)^{1/q}\ \ (q>0).
$$

The second follows from the first by replacing $x_i$ with $x_i^q$. The weighted form with $n = 2$, $\lambda_1 = \frac1p$, $x_1 = a^p$ and $x_2 = b^q$ is exactly Young's inequality of Example 5.3.7. As another example, applying Jensen's inequality to the convex function $x^p$ ($p\ge1$) gives $\bigl(\frac{x_1+x_2+x_3}{3}\bigr)^p\le\frac{x_1^p+x_2^p+x_3^p}{3}$ ($x_i\ge0$).

We now have three common methods for proving inequalities: (1) finding the maximum or minimum of a function (Section 5.3.3); (2) using convexity (Jensen's inequality); (3) using the Lagrange mean value theorem: if $m\le f'\le M$ between $x$ and $y$, then $m(y-x)\le f(y)-f(x)\le M(y-x)$ ($y>x$), as in Example 5.1.3.

### 5.4.2. Sketching Graphs of Functions

The graph of a function $f$ is the locus of the points $(x,f(x))$. In sketching we cannot plot every point; we plot only "key points" and determine the shape of each piece: the domain; symmetry (parity) and periodicity; intervals of monotonicity and local extreme points; intervals of convexity and inflection points; asymptotes. The first four have been discussed; we now discuss asymptotes.

**Definition 5.4.3** If the distance from a point on the curve $y = f(x)$ to some line tends to zero as the point moves along the curve infinitely far from the origin, then the line is called an **asymptote** of the curve. According to direction, asymptotes are classified as vertical asymptotes, horizontal asymptotes and oblique asymptotes.

1. The line $x = x_0$ is a vertical asymptote if and only if $f(x)\to\infty$ as $x\to x_0^+$ or $x\to x_0^-$. In this case $x_0$ is an infinite discontinuity of $f$ (or an endpoint of its domain).
2. The line $y = y_0$ is a horizontal asymptote if and only if $y_0 = \lim\limits_{x\to+\infty}f(x)$ or $y_0 = \lim\limits_{x\to-\infty}f(x)$.

**Theorem 5.4.3 (Oblique Asymptotes)** Let $f$ be defined on $[c,+\infty)$. Then the line $y = ax+b$ is an asymptote of the curve $y = f(x)$ as $x\to+\infty$ if and only if

$$
\lim_{x\to+\infty}\frac{f(x)}{x} = a,\qquad\lim_{x\to+\infty}\bigl(f(x)-ax\bigr) = b.
$$

The case $x\to-\infty$ is analogous. For $a = 0$ this is a horizontal asymptote.

**Proof** The distance from the point $(x,f(x))$ to the line is $\frac{|f(x)-ax-b|}{\sqrt{1+a^2}}$, so $y = ax+b$ is an asymptote if and only if $\lim\limits_{x\to+\infty}(f(x)-ax-b) = 0$, that is, $\lim(f(x)-ax) = b$. In this case $\frac{f(x)}x-a = \frac{f(x)-ax-b}{x}+\frac bx\to0$. Conversely, the two limits directly give $f(x)-ax-b\to0$. $\square$

**Algorithm 5.4.1 (Curve Sketching)**

1. Find the domain and determine parity and periodicity (with symmetry, only part of the graph needs to be drawn);
2. Compute $f'$, find the stationary points and points of nondifferentiability, and determine the intervals of monotonicity and the local extrema;
3. Compute $f''$, find the points where $f'' = 0$ or $f''$ does not exist, and determine the intervals of convexity and the inflection points;
4. List these division points in increasing order in a table, recording on each piece the signs of $f'$ and $f''$ and the shape of the curve;
5. Find the vertical, horizontal and oblique asymptotes;
6. Compute the coordinates of the local extreme points, the inflection points and the intercepts with the coordinate axes, plot them and join them.

**Example 5.4.3** Sketch the graph of $f(x) = \frac{(x-1)^3}{(x+1)^2}$.

**Solution** The domain is $(-\infty,-1)\cup(-1,+\infty)$; the function is neither even nor odd and not periodic.

$$
f'(x) = \frac{(x-1)^2(x+5)}{(x+1)^3},\qquad f''(x) = \frac{24(x-1)}{(x+1)^4}.
$$

The stationary points are $x = -5$ and $x = 1$; $f''(x) = 0$ gives $x = 1$. The table:

| $x$ | $(-\infty,-5)$ | $-5$ | $(-5,-1)$ | $-1$ | $(-1,1)$ | $1$ | $(1,+\infty)$ |
|---|---|---|---|---|---|---|---|
| $f'$ | $+$ | $0$ | $-$ | undefined | $+$ | $0$ | $+$ |
| $f''$ | $-$ | $-$ | $-$ | undefined | $-$ | $0$ | $+$ |
| $f$ | increasing, concave | local maximum $-13.5$ | decreasing, concave | | increasing, concave | inflection point $(1,0)$ | increasing, convex |

The point $x = 1$ is a stationary point, but $f'$ does not change sign there, so it is not a local extreme point but an inflection point (with a horizontal tangent line). Asymptotes: $\lim\limits_{x\to-1}f(x) = -\infty$, so $x = -1$ is a vertical asymptote; $\lim\limits_{x\to\infty}\frac{f(x)}{x} = 1$ and $\lim\limits_{x\to\infty}(f(x)-x) = \lim\limits_{x\to\infty}\frac{-5x^2+2x-1}{(x+1)^2} = -5$, so $y = x-5$ is an oblique asymptote on both sides.

![Graph of f(x) = (x − 1)³/(x + 1)²: vertical asymptote x = −1, oblique asymptote y = x − 5, local maximum point (−5, −13.5), inflection point (1, 0).](./plots/curve-sketching.py)

**Example 5.4.4** Sketch the graph of $y = x\mathrm{e}^{-x^2}$.

**Solution** The domain is $\mathbb{R}$ and the function is odd, so the graph is symmetric about the origin and it suffices to consider $x\ge0$. $y' = (1-2x^2)\mathrm{e}^{-x^2}$, with the stationary point $x = \frac1{\sqrt2}$; $y'' = 2x(2x^2-3)\mathrm{e}^{-x^2}$, and $y'' = 0$ gives $x = 0$ and $x = \sqrt{3/2}$.

| $x$ | $0$ | $\bigl(0,\frac1{\sqrt2}\bigr)$ | $\frac1{\sqrt2}$ | $\bigl(\frac1{\sqrt2},\sqrt{\frac32}\bigr)$ | $\sqrt{\frac32}$ | $\bigl(\sqrt{\frac32},+\infty\bigr)$ |
|---|---|---|---|---|---|---|
| $y'$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ |
| $y''$ | $0$ | $-$ | $-$ | $-$ | $0$ | $+$ |
| $y$ | inflection point $(0,0)$ | increasing, concave | local maximum $\frac1{\sqrt{2\mathrm{e}}}$ | decreasing, concave | inflection point | decreasing, convex |

The inflection points are $\bigl(\pm\sqrt{3/2},\pm\sqrt{3/2}\,\mathrm{e}^{-3/2}\bigr)$ and $(0,0)$; the local minimum $-\frac1{\sqrt{2\mathrm{e}}}$ is attained at $x = -\frac1{\sqrt2}$; and since $\lim\limits_{x\to\infty}x\mathrm{e}^{-x^2} = 0$, $y = 0$ is a horizontal asymptote.

## 5.5. Taylor's Formula and Its Applications

### 5.5.1. Taylor's Formula at a Point

By the definition of the differential, $f(x) = f(x_0)+f'(x_0)(x-x_0)+o(x-x_0)$; that is, near $x_0$ we approximate $f$ by a polynomial of degree one, with an error of higher order than $x-x_0$, which is not accurate enough. Polynomials are "simple and familiar" functions, so it is natural to approximate $f$ near $x_0$ by a polynomial of higher degree

$$
p(x) = a_0+a_1(x-x_0)+a_2(x-x_0)^2+\cdots+a_n(x-x_0)^n.
$$

At the very least we require $p$ and $f$ to "behave alike" at $x_0$: $p^{(k)}(x_0) = f^{(k)}(x_0)$ ($k = 0,1,\dots,n$). Since $p^{(k)}(x_0) = k!\,a_k$, this gives $a_k = \frac{f^{(k)}(x_0)}{k!}$.

**Definition 5.5.1 (Taylor Polynomial)** Let $f$ be $n$ times differentiable at $x_0$. The polynomial

$$
P_n(x) = f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n
$$
is called the **Taylor polynomial** of degree $n$ of $f$ at $x_0$.

**Theorem 5.5.1 (Taylor's Formula)** Let $f$ have derivatives of orders $1$ through $n$ at $x_0$. Then, as $x\to x_0$,

$$
f(x) = f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n+o\bigl((x-x_0)^n\bigr).
$$

This is called Taylor's formula with the Peano remainder, and the remainder $R_n(x) = f(x)-P_n(x) = o\bigl((x-x_0)^n\bigr)$ is called the *Peano form of the remainder*.

**Proof** We must show that $\lim\limits_{x\to x_0}\frac{R_n(x)}{(x-x_0)^n} = 0$. The existence of $f^{(n)}(x_0)$ means that $f^{(n-1)}$ exists on some neighborhood of $x_0$, and $R_n(x_0) = R_n'(x_0) = \cdots = R_n^{(n-1)}(x_0) = 0$. Apply L'Hôpital's rule $n-1$ times in succession (each time the limit is of type $\frac00$), and then use the definition of $f^{(n)}(x_0)$:

$$
\lim_{x\to x_0}\frac{R_n(x)}{(x-x_0)^n} = \cdots = \lim_{x\to x_0}\frac{R_n^{(n-1)}(x)}{n!\,(x-x_0)} = \frac1{n!}\lim_{x\to x_0}\Bigl[\frac{f^{(n-1)}(x)-f^{(n-1)}(x_0)}{x-x_0}-f^{(n)}(x_0)\Bigr] = 0,
$$

where we used $R_n^{(n-1)}(x) = f^{(n-1)}(x)-f^{(n-1)}(x_0)-f^{(n)}(x_0)(x-x_0)$. $\square$

The Peano remainder only says that the error is an infinitesimal of higher order as $x\to x_0$, which suits the computation of limits; to estimate the size of the error, we need an explicit form of the remainder.

**Theorem 5.5.2 (Taylor's Formula with the Lagrange Remainder)** Let $f$ have derivatives of orders $1$ through $n+1$ on an open interval $(a,b)$ containing $x_0$. Then for every $x\in(a,b)$,

$$
f(x) = \sum_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1},
$$
where $\xi = x_0+\theta(x-x_0)$, $0<\theta<1$.

The remainder $R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$ is called the *Lagrange form of the remainder*. For $n = 0$ this is the Lagrange mean value theorem, so Theorem 5.5.2 is a higher-order generalization of the mean value theorem.

**Proof** Let $x\ne x_0$. The function $R_n = f-P_n$ satisfies $R_n(x_0) = R_n'(x_0) = \cdots = R_n^{(n)}(x_0) = 0$ and $R_n^{(n+1)} = f^{(n+1)}$, while $G(t) = (t-x_0)^{n+1}$ satisfies $G(x_0) = \cdots = G^{(n)}(x_0) = 0$ and $G^{(n+1)} = (n+1)!$. Applying Cauchy's mean value theorem to $R_n$ and $G$ repeatedly,

$$
\frac{R_n(x)}{G(x)} = \frac{R_n(x)-R_n(x_0)}{G(x)-G(x_0)} = \frac{R_n'(\xi_1)}{G'(\xi_1)} = \frac{R_n'(\xi_1)-R_n'(x_0)}{G'(\xi_1)-G'(x_0)} = \frac{R_n''(\xi_2)}{G''(\xi_2)} = \cdots = \frac{R_n^{(n+1)}(\xi)}{G^{(n+1)}(\xi)} = \frac{f^{(n+1)}(\xi)}{(n+1)!},
$$

where $\xi_1$ lies between $x_0$ and $x$, $\xi_2$ between $x_0$ and $\xi_1$, and so on, so that $\xi$ lies between $x_0$ and $x$. $\square$

The two theorems have different hypotheses: the Peano remainder needs only the existence of $f^{(n)}(x_0)$; the Lagrange remainder needs the $(n+1)$-th derivative to exist on the whole interval, and in return gives an explicit expression for the error: if $|f^{(n+1)}|\le M$, then $|R_n(x)|\le\frac{M}{(n+1)!}|x-x_0|^{n+1}$.

Taylor's formula with $x_0 = 0$,

$$
f(x) = f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\cdots+\frac{f^{(n)}(0)}{n!}x^n+R_n(x),
$$

is called *Maclaurin's formula*. From $(\mathrm{e}^x)^{(n)} = \mathrm{e}^x$, Examples 4.4.2 and 4.4.3, and similar computations, we obtain five frequently used Maclaurin formulas ($0<\theta<1$):

$$
\begin{aligned}
\mathrm{e}^x &= 1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+\frac{\mathrm{e}^{\theta x}}{(n+1)!}x^{n+1}, &&x\in\mathbb{R};\\
\sin x &= x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots+(-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}+\frac{\sin(\theta x+k\pi)}{(2k)!}x^{2k}, &&x\in\mathbb{R};\\
\cos x &= 1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots+(-1)^k\frac{x^{2k}}{(2k)!}+\frac{\cos\bigl(\theta x+\frac{(2k+1)\pi}{2}\bigr)}{(2k+1)!}x^{2k+1}, &&x\in\mathbb{R};\\
(1+x)^\alpha &= 1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^2+\cdots+\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n+\frac{\alpha(\alpha-1)\cdots(\alpha-n)}{(n+1)!}(1+\theta x)^{\alpha-n-1}x^{n+1}, &&x>-1;\\
\ln(1+x) &= x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots+(-1)^{n-1}\frac{x^n}{n}+\frac{(-1)^n}{(n+1)(1+\theta x)^{n+1}}x^{n+1}, &&x>-1.
\end{aligned}
$$

Replacing the remainders by $o(x^n)$ (by $o(x^{2k})$ and $o(x^{2k+1})$ for $\sin$ and $\cos$, respectively) gives the forms with the Peano remainder. Taking $x = 1$ gives $\mathrm{e} = 1+1+\frac1{2!}+\cdots+\frac1{n!}+\frac{\mathrm{e}^\theta}{(n+1)!}$ with an error less than $\frac{3}{(n+1)!}$, which allows **Euler's number** to be computed quickly.

A question: does $x^\alpha$ ($\alpha>0$ not an integer) have a Taylor formula of order $n$ at $0$? Only for $n<\alpha$ (in which case the Taylor polynomial is $0$); for $n>\alpha$, $f^{(n)}(0)$ does not exist ($x^\alpha$ may not even be defined for $x<0$). Taylor's formula requires the function to be sufficiently smooth at the point.

![Taylor polynomials P₁, P₃, …, P₁₁ of sin x at 0: the higher the degree, the wider the range on which they agree with sin x.](./plots/taylor-sine.py)

**Example 5.5.1** Find the second-order Taylor formula at $x = 0$ of $f(x) = x^3\ln|x|$ ($x\ne0$), $f(0) = 0$.

**Solution** For $x\ne0$, $f'(x) = 3x^2\ln|x|+x^2$, and $f'(0) = \lim\limits_{x\to0}x^2\ln|x| = 0$; $f''(x) = 6x\ln|x|+5x$, and $f''(0) = \lim\limits_{x\to0}\frac{f'(x)}{x} = \lim\limits_{x\to0}(3x\ln|x|+x) = 0$. So the second-order Taylor formula with the Peano remainder is $f(x) = o(x^2)$. Note that $f'''(0) = \lim\limits_{x\to0}(6\ln|x|+5)$ does not exist, so there is no third-order Taylor formula.

**Example 5.5.2** Find the third-order Taylor formulas of $f(x) = x^3+2x+1$ at $x = 0$ and at $x = 1$.

**Solution** $f' = 3x^2+2$, $f'' = 6x$, $f''' = 6$ and $f^{(4)} = 0$, so the Lagrange remainder vanishes. At $0$, $f(x) = 1+2x+x^3$; at $1$, $f(1) = 4$, $f'(1) = 5$, $\frac{f''(1)}{2!} = 3$ and $\frac{f'''(1)}{3!} = 1$, so

$$
f(x) = 4+5(x-1)+3(x-1)^2+(x-1)^3.
$$

In general, the Taylor polynomial of degree $n$ of a polynomial of degree $n$ is the polynomial itself, and its Taylor formula at $x_0$ is simply its re-expansion in powers of $x-x_0$ (in agreement with the expansion of a polynomial in powers of $x-c$ by synthetic division in [2.1.9](/2.1.9)).

The next theorem gives another way to find Taylor polynomials: there is no need to differentiate order by order; any expansion of the form "polynomial $+\,o((x-x_0)^n)$," however obtained, is the Taylor formula.

**Theorem 5.5.3 (Uniqueness)** Let $f$ have derivatives of orders $1$ through $n$ at $x_0$. If the polynomial $a_0+a_1(x-x_0)+\cdots+a_n(x-x_0)^n$ satisfies

$$
f(x) = a_0+a_1(x-x_0)+\cdots+a_n(x-x_0)^n+o\bigl((x-x_0)^n\bigr)\qquad(x\to x_0),
$$
then $a_k = \frac{f^{(k)}(x_0)}{k!}$ ($k = 0,1,\dots,n$); that is, this polynomial is the Taylor polynomial of degree $n$ of $f$.

**Proof** By Theorem 5.5.1, $\sum_{k=0}^n\bigl(a_k-\frac{f^{(k)}(x_0)}{k!}\bigr)(x-x_0)^k = o\bigl((x-x_0)^n\bigr)$. If the coefficients are not all zero, let $c_m$ ($m\le n$) be the first nonzero one; dividing both sides by $(x-x_0)^m$ and letting $x\to x_0$ gives $c_m = 0$, a contradiction. $\square$

**Example 5.5.3** Find the Taylor formula of order $2n$ of $f(x) = \mathrm{e}^{x^2}$ at $x = 0$.

**Solution** Substitute $t = x^2$ into the Maclaurin formula for $\mathrm{e}^t$:

$$
\mathrm{e}^{x^2} = 1+x^2+\frac{x^4}{2!}+\cdots+\frac{x^{2n}}{n!}+\frac{\mathrm{e}^{\theta x^2}}{(n+1)!}x^{2(n+1)}.
$$

The remainder is $o(x^{2n})$, so by Theorem 5.5.3 this is the Taylor formula of order $2n$ of $\mathrm{e}^{x^2}$; as a by-product, $f^{(2k)}(0) = \frac{(2k)!}{k!}$, and the derivatives of odd order at $0$ vanish.

**Example 5.5.4** Find the Taylor formula of order $n$ with the Lagrange remainder of $f(x) = \ln x$ at $x = 3$.

**Solution** $\ln x = \ln3+\ln\bigl(1+\frac{x-3}{3}\bigr)$; substituting $t = \frac{x-3}3$ ($x>0$) into the Maclaurin formula for $\ln(1+t)$,

$$
\ln x = \ln3+\sum_{k=1}^n\frac{(-1)^{k-1}}{k}\Bigl(\frac{x-3}{3}\Bigr)^k+\frac{(-1)^n}{(n+1)\bigl(1+\theta\frac{x-3}{3}\bigr)^{n+1}}\Bigl(\frac{x-3}{3}\Bigr)^{n+1},\qquad0<\theta<1.
$$

**Example 5.5.5** Find the third-order Taylor formula with the Peano remainder of $\sqrt[3]{\cos x}$ at $0$.

**Solution** Write $\cos x = 1+u$ with $u = -\frac{x^2}{2}+o(x^3)$; and $(1+u)^{1/3} = 1+\frac13u-\frac19u^2+o(u^2)$. Since $u^2 = o(x^3)$,

$$
\sqrt[3]{\cos x} = 1+\frac13\Bigl(-\frac{x^2}{2}+o(x^3)\Bigr)+o(x^3) = 1-\frac{x^2}{6}+o(x^3).
$$

(Differentiating order by order also gives $f(0) = 1$, $f'(0) = 0$, $f''(0) = -\frac13$ and $f'''(0) = 0$, but with much more computation.)

### 5.5.2. Applications of Taylor's Formula

Error estimates. The error in approximating $f(x)$ by $P_n(x)$ is the Lagrange remainder $|R_n(x)| = \frac{|f^{(n+1)}(\xi)|}{(n+1)!}|x-x_0|^{n+1}$.

**Example 5.5.6** Use Taylor's formula to approximate $\sin10^\circ$.

**Solution** $10^\circ = \frac{\pi}{18}\approx0.174533$. The first-order Taylor polynomial gives $\sin10^\circ\approx0.174533$ with error $|R_1| = \bigl\lvert\frac{\sin(\xi+\pi)}{2!}\bigr\rvert(0.174533)^2<0.02$; the third-order Taylor polynomial gives $\sin10^\circ\approx0.174533-\frac16(0.174533)^3\approx0.173647$ with error $|R_3| = \bigl\lvert\frac{\sin(\xi+2\pi)}{4!}\bigr\rvert(0.174533)^4\le\frac{(0.174533)^5}{4!}<10^{-5}$ (here $0<\xi<0.174533$ and $|\sin\xi|\le\xi$; since $P_3 = P_4$, the error is in fact at most $\frac{(0.174533)^5}{5!}\approx1.4\times10^{-6}$). If the error is required not to exceed $10^{-6}$, we look for the smallest $n$ with $\frac{(0.174533)^{n+1}}{(n+1)!}<10^{-6}$ and find $n = 5$ (for $n = 4$ the bound is about $1.4\times10^{-6}$, for $n = 5$ about $3.9\times10^{-8}$).

Computing limits. Expanding numerator and denominator to the same order turns an indeterminate form into a ratio of polynomials; this is a refinement of the substitution of equivalent infinitesimals that can handle cancellation in sums and differences.

**Example 5.5.7** Find $\lim\limits_{x\to0}\frac{\sqrt[3]{\cos x}-1-x(\mathrm{e}^x-1)}{(2^x-1)\tan x}$.

**Solution** The denominator is $\sim x\ln2\cdot x = x^2\ln2$. By Example 5.5.5 and $\mathrm{e}^x-1 = x+o(x)$, the numerator equals $-\frac{x^2}6-x^2+o(x^2) = -\frac76x^2+o(x^2)$, so the limit is $-\frac{7}{6\ln2}$.

**Example 5.5.8** Find $\lim\limits_{x\to0^+}\frac{\mathrm{e}^{x^2}-\cos(2\sqrt x)-2x}{x^2}$.

**Solution** $\mathrm{e}^{x^2} = 1+x^2+o(x^2)$ and $\cos(2\sqrt x) = 1-\frac{(2\sqrt x)^2}{2}+\frac{(2\sqrt x)^4}{4!}+o(x^2) = 1-2x+\frac23x^2+o(x^2)$, so the numerator equals $\frac13x^2+o(x^2)$ and the limit is $\frac13$.

Proving boundedness and inequalities.

**Example 5.5.9** Let $f$ have a third derivative on $(-\infty,+\infty)$, and suppose $f$ and $f'''$ are bounded. Prove that $f'$ and $f''$ are also bounded.

**Proof** Let $|f|\le M$ and $|f'''|\le N$. For any $x$, expand $f(x\pm1)$ at $x$ by the second-order Taylor formula with the Lagrange remainder:

$$
f(x+1) = f(x)+f'(x)+\frac{f''(x)}{2}+\frac{f'''(\xi)}{6},\qquad f(x-1) = f(x)-f'(x)+\frac{f''(x)}{2}-\frac{f'''(\eta)}{6}.
$$

Subtracting and adding the two formulas gives

$$
f'(x) = \frac12\Bigl[f(x+1)-f(x-1)-\frac{f'''(\xi)+f'''(\eta)}{6}\Bigr],\qquad f''(x) = f(x+1)+f(x-1)-2f(x)-\frac{f'''(\xi)-f'''(\eta)}{6},
$$

so $|f'(x)|\le M+\frac N6$ and $|f''(x)|\le4M+\frac N3$. $\square$

## Summary

| Theorem | Hypotheses | Conclusion |
|---|---|---|
| Fermat's theorem | $x_0$ is a local extreme point and $f'(x_0)$ exists | $f'(x_0) = 0$ |
| Rolle's theorem | $f\in C[a,b]$, differentiable on $(a,b)$, $f(a) = f(b)$ | $\exists\,\xi$, $f'(\xi) = 0$ |
| Lagrange mean value theorem | $f\in C[a,b]$, differentiable on $(a,b)$ | $f(b)-f(a) = f'(\xi)(b-a)$ |
| Cauchy's mean value theorem | In addition $g$ with $g'\ne0$ | $\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(\xi)}{g'(\xi)}$ |
| Darboux's theorem | $f$ differentiable on $[a,b]$ | $f'$ takes every value between $f'_+(a)$ and $f'_-(b)$ |
| L'Hôpital's rule | Type $\frac00$ or $\frac{*}{\infty}$, $g'\ne0$, $\lim\frac{f'}{g'}$ exists or is infinite | $\lim\frac fg = \lim\frac{f'}{g'}$ |
| Tests for extrema | $f'$ changes sign at $x_0$ ($f$ continuous at $x_0$); or $f'(x_0) = 0$, $f''(x_0)\ne0$ | Local extremum; a local minimum if $f''(x_0)>0$ |
| Unique stationary point theorem | Unique interior stationary point, which is a local minimum (maximum) point | Minimum (maximum) |
| Test for convexity | $f'$ nondecreasing, or $f''\ge0$ | $f$ convex; Jensen's inequality |
| Oblique asymptote | $a = \lim\frac{f(x)}{x}$, $b = \lim(f(x)-ax)$ | $y = ax+b$ |
| Taylor's formula | $f^{(n)}(x_0)$ exists / $f^{(n+1)}$ exists on the interval | Remainder $o((x-x_0)^n)$ / $\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$ |

| Standard Maclaurin expansions (Peano remainder) | |
|---|---|
| $\mathrm{e}^x$ | $1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+o(x^n)$ |
| $\sin x$ | $x-\frac{x^3}{3!}+\cdots+(-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}+o(x^{2k})$ |
| $\cos x$ | $1-\frac{x^2}{2!}+\cdots+(-1)^k\frac{x^{2k}}{(2k)!}+o(x^{2k+1})$ |
| $(1+x)^\alpha$ | $1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^2+\cdots+\binom{\alpha}{n}x^n+o(x^n)$ |
| $\ln(1+x)$ | $x-\frac{x^2}2+\cdots+(-1)^{n-1}\frac{x^n}{n}+o(x^n)$ |

Here $\binom\alpha n = \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}$ is the generalized binomial coefficient.
