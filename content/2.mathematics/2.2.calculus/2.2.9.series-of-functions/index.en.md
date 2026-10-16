---
title: Series of Functions, Power Series and Fourier Series
source_hash: 85cb3d0f3e64
---

Every term of the series in [Chapter 8](/2.2.8) is a number; in this chapter every term is a function, as in $\sum x^n$ or $\sum\frac{\sin nx}{n}$. For each fixed $x$ such a series is a numerical series, and the tests of Chapter 8 still apply. The new questions concern the properties of the sum: is an infinite sum of continuous functions continuous? May we integrate or differentiate term by term? The answer is in general no, and the crucial additional hypothesis is uniform convergence (9.1).

We then study the two most important kinds of series of functions. A power series $\sum a_nx^n$ is a "polynomial of infinite degree": its domain of convergence is an interval, inside which it can be differentiated and integrated term by term (9.2). Letting the **Taylor polynomial** of [Chapter 5](/2.2.5) run to infinitely many terms gives the Taylor series, and elementary functions such as $\mathrm{e}^x$, $\sin x$ and $\ln(1 + x)$ can all be expanded in power series. A Fourier series $\frac{a_0}{2} + \sum(a_n\cos nx + b_n\sin nx)$ represents a periodic function as a superposition of trigonometric functions of different frequencies (9.3); its coefficients are the coordinates of the function with respect to an **orthogonal system of functions**, the same idea as the inner product spaces of [Linear Algebra 2.1.12](/2.1.12). Power series become a central tool in complex analysis, and Fourier series are the foundation for solving partial differential equations and for signal analysis.

## 9.1. Series of Functions

**Definition 9.1.1 (Series of Functions)** Let $u_n(x)$ ($n = 1, 2, \dots$) be a sequence of functions defined on an interval $I$. Then $\sum_{n=1}^\infty u_n(x)$ is called a series of functions on $I$, and $S_n(x) = \sum_{k=1}^n u_k(x)$ its partial sums. If $\sum u_n(x)$ converges for every $x \in I$, then $S(x) = \sum_{n=1}^\infty u_n(x) = \lim_{n\to\infty}S_n(x)$ is a function on $I$, called the **sum function** of the series.

### 9.1.1. Points and Domain of Convergence

**Definition 9.1.2 (Domain of Convergence)** If $\sum u_n(x_0)$ converges, $x_0$ is called a point of convergence of $\sum u_n(x)$; the set of all points of convergence is called its domain of convergence.

Finding the domain of convergence means testing a numerical series for each $x$. Usually one applies the ratio or root test to $\sum|u_n(x)|$ and then examines separately the points where the test is inconclusive.

**Example 9.1.1**

1. $\sum_{n=0}^\infty ax^n$ ($a \ne 0$): a **geometric series**, with domain of convergence $(-1,1)$ and sum function $\frac{a}{1-x}$.
2. $\sum_{n=1}^\infty\frac{x^n}{n^p}$: $\left|\frac{u_{n+1}}{u_n}\right| \to |x|$, so the series converges absolutely for $|x| < 1$, and its general term does not tend to zero for $|x| > 1$. At $x = \pm1$, the **p-series** and the **Leibniz test** show that the domain of convergence is $(-1,1)$ for $p \le 0$, $[-1,1)$ for $0 < p \le 1$, and $[-1,1]$ for $p > 1$.
3. $\sum_{n=1}^\infty\left(\frac{n+1}{n}\right)^nx^n$: $\sqrt[n]{|u_n|} = \left(1 + \frac1n\right)|x| \to |x|$, and for $|x| = 1$, $|u_n| \to \mathrm{e} \ne 0$. The domain of convergence is $(-1,1)$.

Let $I$ be contained in the domain of convergence. We ask three questions:

1. If every $u_n$ is continuous at $x_0$, is $S$ continuous at $x_0$? That is, may we take limits term by term: $\lim_{x\to x_0}\sum u_n(x) = \sum\lim_{x\to x_0}u_n(x)$?
2. If every $u_n$ is integrable on $[a,b]$, may we integrate term by term: $\int_a^b\sum u_n(x)\,\mathrm{d}x = \sum\int_a^b u_n(x)\,\mathrm{d}x$?
3. If every $u_n$ is differentiable, may we differentiate term by term: $\left(\sum u_n(x)\right)' = \sum u_n'(x)$?

All three questions ask whether two limiting processes can be interchanged. In general they cannot: the series $x + \sum_{n=2}^\infty(x^n - x^{n-1})$ has partial sums $S_n(x) = x^n$, domain of convergence $(-1,1]$, and sum function

$$
S(x) = \begin{cases}0, & -1 < x < 1,\\ 1, & x = 1;\end{cases}
$$
every term is continuous, but the sum function is discontinuous at $x = 1$.

### 9.1.2. Uniform Convergence

For a sequence of functions $\{f_n\}$, "converges to $f$ on $I$" can mean two things of different strength.

**Definition 9.1.3 (Uniform Convergence)** Let $\{f_n(x)\}$ and $f(x)$ be defined on an interval $I$.

1. If $\lim_{n\to\infty}f_n(x) = f(x)$ for every $x \in I$, we speak of **pointwise convergence** of $\{f_n\}$ to $f$ on $I$. In $\varepsilon$-$N$ language: for every $x \in I$ and $\varepsilon > 0$ there exists $N = N(\varepsilon, x)$ such that $|f_n(x) - f(x)| < \varepsilon$ for $n > N$.
2. If for every $\varepsilon > 0$ there exists $N = N(\varepsilon)$, depending only on $\varepsilon$, such that $|f_n(x) - f(x)| < \varepsilon$ for all $n > N$ and all $x \in I$, we speak of **uniform convergence** of $\{f_n\}$ to $f$ on $I$, and say that $\{f_n\}$ converges uniformly to $f$.

A series of functions $\sum u_n(x)$ is said to converge uniformly on $I$ if its sequence of partial sums $\{S_n(x)\}$ converges uniformly on $I$ to the sum function $S(x)$.

The difference lies in whether $N$ can be chosen independently of $x$, just as **continuity** differs from **uniform continuity**. Geometrically, uniform convergence says that for every $\varepsilon$, once $n$ is large enough, the entire graph of $y = S_n(x)$ lies within the band $S(x) - \varepsilon < y < S(x) + \varepsilon$; the convergence proceeds at "roughly the same rate" at all points, and therefore $S_n$ and $S$ have similar properties.

**Theorem 9.1.1** $\{f_n\}$ converges uniformly to $f$ on $I$ $\iff$ $\lim_{n\to\infty}\sup_{x\in I}|f_n(x) - f(x)| = 0$.

This is a direct reformulation of the definition, and also the most common way to establish uniform convergence: find the maximal deviation of $f_n - f$ on $I$ and see whether it tends to zero.

**Example 9.1.2** The sequence $f_n(x) = x^n$ converges pointwise to $0$ on $(0,1)$, but not uniformly: $\sup_{(0,1)}x^n = 1$. Concretely, take $\varepsilon = \frac12$; no matter how large $n$ is, at $x = 2^{-1/n} \in (0,1)$ we have $x^n = \frac12$, so part of the graph always lies outside the $\varepsilon$-band. For every $0 < b < 1$, however, the convergence is uniform on $[0,b]$: $\sup_{[0,b]}x^n = b^n \to 0$.

![x^n converges pointwise on [0,1] to a discontinuous limit, but its graph always sticks out of the ε-band (left); x^n(1-x)^n is dominated by 4^{-n} and converges uniformly (right)](./plots/uniform-convergence.py)

**Theorem 9.1.2 (Cauchy Criterion for Uniform Convergence)** $\sum u_n(x)$ converges uniformly on $I$ $\iff$ for every $\varepsilon > 0$ there exists $N$ such that for all $n > N$, all positive integers $p$ and all $x \in I$,

$$
|u_{n+1}(x) + u_{n+2}(x) + \cdots + u_{n+p}(x)| < \varepsilon.
$$

**Proof** Necessity: $|S_{n+p}(x) - S_n(x)| \le |S_{n+p}(x) - S(x)| + |S(x) - S_n(x)|$. Sufficiency: the condition says that for each $x$, $\{S_n(x)\}$ is a **Cauchy sequence** and therefore has a limit $S(x)$; letting $p \to \infty$ in $|S_{n+p}(x) - S_n(x)| < \varepsilon$ gives $|S(x) - S_n(x)| \le \varepsilon$ for all $x$. $\square$

Consequently, if $\sum|u_n(x)|$ converges uniformly on $I$, then so does $\sum u_n(x)$ (since $|\sum_{k=n+1}^{n+p}u_k| \le \sum_{k=n+1}^{n+p}|u_k|$).

**Theorem 9.1.3 (Weierstrass M-Test)** If there is a convergent series of nonnegative terms $\sum c_n$ such that $|u_n(x)| \le c_n$ for all $x \in I$ and all $n$, then $\sum u_n(x)$ converges (absolutely and) uniformly on $I$.

**Proof** For each $x$, $\sum u_n(x)$ converges absolutely by the **comparison test**. Moreover, by the Cauchy criterion for numerical series, for $\varepsilon > 0$ there exists $N$ such that $\sum_{k=n+1}^{n+p}c_k < \varepsilon$ for $n > N$, so $\left|\sum_{k=n+1}^{n+p}u_k(x)\right| \le \sum_{k=n+1}^{n+p}c_k < \varepsilon$ for all $x \in I$; apply Theorem 9.1.2. $\square$

The series $\sum c_n$ is called a *majorant*. The Weierstrass M-test is simple and convenient, but it can only detect series that converge both absolutely and uniformly.

**Example 9.1.3** The series $\sum_{n=1}^\infty x^n(1-x)^n$ converges uniformly on $[0,1]$: $x(1-x) = \frac14 - \left(x - \frac12\right)^2 \le \frac14$, so $0 \le x^n(1-x)^n \le \frac{1}{4^n}$, and $\sum\frac{1}{4^n}$ converges.

**Example 9.1.4** For $\delta > 0$, the series $\sum_{n=1}^\infty\frac{1}{n^x}$ converges uniformly on $[1+\delta, +\infty)$, since $\frac{1}{n^x} \le \frac{1}{n^{1+\delta}}$. It does not converge uniformly on $(1, +\infty)$: $\sum_{k=n+1}^{2n}\frac{1}{k^x} \ge \frac{n}{(2n)^x} \to \frac12$ as $x \to 1^+$, so for each fixed $n$ the supremum of the left-hand side is at least $\frac12$, and the Cauchy criterion fails.

### 9.1.3. Analytic Properties of Uniformly Convergent Series

Each of the following three theorems is first stated for sequences of functions and then applied to partial sums to obtain the result for series.

**Theorem 9.1.4 (Termwise Limits)** Let $I$ be an interval.

1. If $f_n \in C(I)$ and $\{f_n\}$ converges uniformly to $f$ on $I$, then $f \in C(I)$;
2. If $u_n \in C(I)$ and $\sum u_n(x)$ converges uniformly on $I$, then the sum function satisfies $S \in C(I)$; that is, for $x_0 \in I$, $\lim_{x\to x_0}\sum u_n(x) = \sum\lim_{x\to x_0}u_n(x)$.

**Proof** 1. Take any $x_0 \in I$ and $\varepsilon > 0$. Then

$$
|f(x) - f(x_0)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)|.
$$
By uniform convergence, fix $n$ so that the first and third terms are less than $\varepsilon/3$ for all $x$; for this $n$, the continuity of $f_n$ at $x_0$ gives $\delta$ such that the second term is less than $\varepsilon/3$ whenever $|x - x_0| < \delta$. (Here we used that the first term is small uniformly in $x$, which pointwise convergence cannot guarantee.) 2. Apply 1 to the partial sums $S_n$. $\square$

This can also be used in reverse to show that convergence is not uniform: in Example 9.1.2 the functions $x^n$ are continuous but the limit function is discontinuous at $x = 1$, so $x^n$ does not converge uniformly on $[0,1]$.

**Theorem 9.1.5 (Termwise Integration)** 1. If $f_n \in C[a,b]$ and $\{f_n\}$ converges uniformly to $f$ on $[a,b]$, then $f$ is integrable on $[a,b]$ and

$$
\int_a^b\lim_{n\to\infty}f_n(x)\,\mathrm{d}x = \lim_{n\to\infty}\int_a^b f_n(x)\,\mathrm{d}x.
$$

2. If $u_n \in C[a,b]$ and $\sum u_n(x)$ converges uniformly on $[a,b]$, then $\int_a^b\sum u_n(x)\,\mathrm{d}x = \sum\int_a^b u_n(x)\,\mathrm{d}x$.

**Proof** By Theorem 9.1.4, $f$ is continuous and hence integrable. For $n$ large enough, $|f_n(x) - f(x)| < \frac{\varepsilon}{b-a}$ for all $x$, so $\left|\int_a^b f_n - \int_a^b f\right| \le \int_a^b|f_n - f| < \varepsilon$. $\square$

**Theorem 9.1.6 (Termwise Differentiation)** 1. Let $f_n \in C^1[a,b]$, let $\{f_n\}$ converge pointwise to $f$ on $[a,b]$, and let $\{f_n'\}$ converge uniformly on $[a,b]$. Then $f$ is differentiable on $[a,b]$ and $f'(x) = \lim_{n\to\infty}f_n'(x)$.

2. Let $u_n \in C^1[a,b]$, let $\sum u_n(x)$ converge on $[a,b]$, and let $\sum u_n'(x)$ converge uniformly on $[a,b]$. Then $\sum u_n(x)$ is differentiable and $\left(\sum u_n(x)\right)' = \sum u_n'(x)$.

**Proof** Let $f_n' \to g$ uniformly; then $g$ is continuous (Theorem 9.1.4). By the **fundamental theorem of calculus**, $f_n(x) = f_n(a) + \int_a^x f_n'(t)\,\mathrm{d}t$; letting $n \to \infty$ and using Theorem 9.1.5 gives $f(x) = f(a) + \int_a^x g(t)\,\mathrm{d}t$, so $f' = g$. $\square$

The hypothesis for termwise differentiation is imposed on the series of derivatives, not on the original series. Uniform convergence of the original series is far from enough:

**Example 9.1.5** The series $\sum_{n=1}^\infty\frac{\sin(n^2x)}{n^2}$ converges uniformly on $(-\infty, +\infty)$ (with majorant $\sum\frac1{n^2}$), and its sum is continuous; but the termwise derivative $\sum\cos(n^2x)$ diverges for every $x$. Indeed, if $\cos(n^2x) \to 0$, then $\cos(4n^2x) = \cos\bigl((2n)^2x\bigr)$ also tends to zero, whereas $\cos4\theta = 8\cos^4\theta - 8\cos^2\theta + 1$ gives $\cos(4n^2x) \to 1$, a contradiction.

**Example 9.1.6** The function $S(x) = \sum_{n=1}^\infty\frac{\sin nx}{n^3}$ is continuously differentiable on $(-\infty, +\infty)$: the series converges, and the series of derivatives $\sum\frac{\cos nx}{n^2}$ has the majorant $\sum\frac{1}{n^2}$ and thus converges uniformly. By Theorem 9.1.6, $S'(x) = \sum\frac{\cos nx}{n^2}$, and by Theorem 9.1.4, $S'$ is continuous.

**Example 9.1.7** The function $S(x) = \sum_{n=1}^\infty n\mathrm{e}^{-nx}$ is continuous and differentiable on $(0, +\infty)$.

**Proof** Take any $x_0 > 0$ and let $\delta = x_0/2$. On $[\delta, +\infty)$ we have $n\mathrm{e}^{-nx} \le n\mathrm{e}^{-n\delta}$, and $\sum n\mathrm{e}^{-n\delta}$ converges (ratio test), so by the Weierstrass M-test the series converges uniformly on $[\delta, +\infty)$, and $S$ is continuous at $x_0$. The series of derivatives $\sum(-n^2\mathrm{e}^{-nx})$ has the majorant $\sum n^2\mathrm{e}^{-n\delta}$, so likewise $S$ is differentiable at $x_0$. $\square$

Neither series converges uniformly on $(0, +\infty)$ (as $x \to 0^+$ the terms are not uniformly small), but continuity and differentiability are local properties: it suffices to have uniform convergence on a closed interval around each point. This is called uniform convergence on compact subsets (or locally uniform convergence).

## 9.2. Power Series

**Definition 9.2.1 (Power Series)** A series of functions of the form $\sum_{n=0}^\infty a_n(x - x_0)^n = a_0 + a_1(x - x_0) + a_2(x - x_0)^2 + \cdots$ is called a power series, and the $a_n$ are called its coefficients.

The substitution $t = x - x_0$ reduces everything to the case $x_0 = 0$, so we mainly discuss $\sum a_nx^n$.

### 9.2.1. Radius and Domain of Convergence

The domains of convergence of $\sum\frac{x^n}{2^n}$, $\sum\frac{x^n}{n!}$ and $\sum n!\,x^n$ are $(-2,2)$, $(-\infty, +\infty)$ and $\{0\}$ respectively, all intervals centered at $0$. This is no coincidence:

**Theorem 9.2.1 (Abel's Theorem)** 1. If $\sum a_nx^n$ converges at $x = b \ne 0$, then it converges absolutely at every point of $(-|b|, |b|)$;
2. If $\sum a_nx^n$ diverges at $x = b$, then it diverges at every point outside $[-|b|, |b|]$.

**Proof** 1. Since $\sum a_nb^n$ converges, its terms are bounded: $|a_nb^n| \le M$. For $|x| < |b|$, let $r = |x/b| < 1$; then $|a_nx^n| = |a_nb^n|\cdot r^n \le Mr^n$, and we compare with a geometric series. 2. If the series converged at some $x_1$ with $|x_1| > |b|$, then by 1 it would converge absolutely at $b$, a contradiction. $\square$

Hence a power series has only three possible kinds of convergence behavior: it converges only at $x = 0$; it converges everywhere on $(-\infty, +\infty)$; or there is $R > 0$ such that it converges absolutely on $(-R, R)$ and diverges outside $[-R,R]$ ($R$ is the **supremum** of the set $\{|b| : \sum a_nb^n \text{ converges}\}$).

**Definition 9.2.2 (Radius of Convergence)** The number $R$ in the third case above is called the radius of convergence of the power series; in the first and second cases we set $R = 0$ and $R = +\infty$ respectively. The domain of convergence of a power series, $(-R, R)$ together with those endpoints at which it converges, is called its **interval of convergence**.

The radius of convergence determines only the open interval $(-R,R)$; at the endpoints $x = \pm R$ the series may converge or diverge and must be examined separately as a numerical series (Example 9.1.1, part 2).

**Theorem 9.2.2** If $\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| = \rho$, then the radius of convergence is $R = \frac1\rho$ (with $R = +\infty$ if $\rho = 0$ and $R = 0$ if $\rho = +\infty$).

**Theorem 9.2.3** If $\lim_{n\to\infty}\sqrt[n]{|a_n|} = \rho$, then the radius of convergence is $R = \frac1\rho$ (with the same conventions).

**Proof** Apply the **ratio test** and the **root test**, respectively, to $\sum|a_nx^n|$: $\left|\frac{a_{n+1}x^{n+1}}{a_nx^n}\right| \to \rho|x|$ and $\sqrt[n]{|a_nx^n|} \to \rho|x|$. If $\rho|x| < 1$, the series converges absolutely; if $\rho|x| > 1$, its general term does not tend to zero and it diverges. $\square$

In general (when these limits do not exist) there is the Cauchy–Hadamard formula $R = 1\big/\limsup_{n\to\infty}\sqrt[n]{|a_n|}$, which we do not develop here.

**Example 9.2.1**

1. $\sum_{n=1}^\infty\frac{x^n}{n^p}$: $\frac{n^p}{(n+1)^p} \to 1$, so $R = 1$; for the interval of convergence see Example 9.1.1.
2. $\sum_{n=1}^\infty(2^n + 3^n)x^n$: $\sqrt[n]{2^n + 3^n} \to 3$, so $R = \frac13$; at $x = \pm\frac13$ the general term does not tend to zero, and the interval of convergence is $\left(-\frac13, \frac13\right)$.
3. $\sum_{n=1}^\infty\frac{x^{2n+1}}{n\cdot3^n}$: only odd powers occur, so the ratio of consecutive coefficients is meaningless; apply the ratio test directly to the general term: $\left|\frac{u_{n+1}}{u_n}\right| \to \frac{x^2}{3}$, so $R = \sqrt3$. At $x = \pm\sqrt3$ the general term is $\pm\frac{\sqrt3}{n}$, and the series diverges. The interval of convergence is $(-\sqrt3, \sqrt3)$.

### 9.2.2. Analytic Properties of Power Series

**Lemma 9.2.1** Let the radius of convergence $R$ of $\sum a_nx^n$ be positive. Then the series converges uniformly on $[-b, b]$ for every $0 < b < R$.

**Proof** $|a_nx^n| \le |a_nb^n|$, and since $b$ lies inside the interval of convergence, $\sum|a_nb^n|$ converges; apply the **Weierstrass M-test**. $\square$

That is, a power series converges uniformly on compact subsets of $(-R, R)$ (though not necessarily uniformly on $(-R,R)$ itself; for example, $\sum x^n$ does not converge uniformly on $(-1,1)$).

**Lemma 9.2.2** The termwise derivative $\sum_{n=1}^\infty na_nx^{n-1}$ of a power series has the same radius of convergence as the original series, and so does the termwise integral $\sum\frac{a_n}{n+1}x^{n+1}$.

**Proof** Let $R'$ be the radius of convergence of the differentiated series. If $R' < R$, choose $R' < x_0 < x_1 < R$; then

$$
n|a_n|x_0^{n-1} = \frac{n}{x_1}\left(\frac{x_0}{x_1}\right)^{n-1}|a_n|x_1^n \le M|a_n|x_1^n
$$
(since $n(x_0/x_1)^{n-1} \to 0$, this factor is bounded), and $\sum|a_n|x_1^n$ converges, so $\sum n|a_n|x_0^{n-1}$ converges, contradicting $x_0 > R'$. If $R' > R$, choose $R < x_0 < R'$; for $n > x_0$ we have $|a_n|x_0^n \le n|a_n|x_0^{n-1}$, and the sum of the latter converges, contradicting $x_0 > R$. For the integrated series: the original series is the termwise derivative of the integrated one. $\square$

**Theorem 9.2.4** Let $\sum a_nx^n$ have radius of convergence $R > 0$ and sum function $f(x)$. Then

1. $f$ is continuous on $(-R, R)$;
2. $f$ is differentiable on $(-R, R)$ and can be differentiated term by term: $f'(x) = \sum_{n=1}^\infty na_nx^{n-1}$;
3. for $x \in (-R, R)$ it can be integrated term by term: $\int_0^x f(t)\,\mathrm{d}t = \sum_{n=0}^\infty\frac{a_n}{n+1}x^{n+1}$.

**Proof** Take any $x \in (-R, R)$ and choose $|x| < b < R$. By Lemma 9.2.1, both the original series and the series of derivatives (whose radius of convergence is also $R$ by Lemma 9.2.2) converge uniformly on $[-b, b]$; Theorems 9.1.4, 9.1.6 and 9.1.5 then give 1, 2 and 3 respectively. $\square$

**Corollary 9.2.1** The sum function of a power series has derivatives of all orders on $(-R, R)$, and

$$
f^{(k)}(x) = \sum_{n=k}^\infty n(n-1)\cdots(n-k+1)a_nx^{n-k}, \qquad \text{in particular} \quad a_k = \frac{f^{(k)}(0)}{k!}.
$$

The last formula shows that if a function can be expanded in a power series, the expansion is unique: its coefficients are determined by the derivatives of the function at $0$.

Theorem 9.2.4 concerns only the open interval $(-R,R)$. If the series converges at an endpoint, the one-sided continuity of the sum function there requires another theorem:

**Theorem 9.2.5 (Abel's Second Theorem)** If $\sum a_nx^n$ converges at $x = R$, then it converges uniformly on $[0, R]$, and its sum function is left-continuous at $x = R$: $\lim_{x\to R^-}\sum a_nx^n = \sum a_nR^n$. The same holds at $x = -R$.

(In much of the English-language literature, it is this result that is called Abel's theorem.)

**Proof** Write $a_nx^n = a_nR^n\cdot\left(\frac xR\right)^n$. The series $\sum a_nR^n$ converges (independently of $x$), and for each $x \in [0,R]$ the sequence $\left(\frac xR\right)^n$ is monotone and bounded by $1$. Repeating the proof of **Abel's test** (the bound in Lemma 8.3.1 does not depend on $x$) and using the Cauchy criterion for uniform convergence gives uniform convergence; Theorem 9.1.4 then gives continuity. $\square$

Therefore the sum function of a power series is continuous on its entire interval of convergence (including the endpoints at which the series converges).

**Example 9.2.2** From $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$ ($|x| < 1$), termwise differentiation and integration give

$$
\frac{1}{(1-x)^2} = \sum_{n=1}^\infty nx^{n-1}, \qquad -\ln(1-x) = \sum_{n=1}^\infty\frac{x^n}{n}, \qquad |x| < 1.
$$

The second series converges at $x = -1$ (the alternating harmonic series), so by Abel's second theorem, letting $x \to -1^+$ gives $\ln2 = 1 - \frac12 + \frac13 - \cdots$.

### 9.2.3. Power Series Expansions of Functions

**Definition 9.2.3 (Taylor Series)** Let $f$ have derivatives of all orders in some **neighborhood** of $x_0$. The power series

$$
\sum_{n=0}^\infty\frac{f^{(n)}(x_0)}{n!}(x - x_0)^n = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \cdots
$$
is called the Taylor series of $f$ at $x_0$, written $f(x) \sim \sum\frac{f^{(n)}(x_0)}{n!}(x - x_0)^n$; for $x_0 = 0$ it is called the **Maclaurin series** of $f$.

The symbol $\sim$ indicates that the Taylor series is only written down formally: it need not converge, and even when it converges, its sum need not be $f(x)$.

**Example 9.2.3** Let $f(x) = \mathrm{e}^{-1/x^2}$ ($x \ne 0$) and $f(0) = 0$. One can check that $f$ is infinitely differentiable on $\mathbb{R}$ and that $f^{(n)}(0) = 0$ for all $n$ (each differentiation produces an expression of the form $P(1/x)\mathrm{e}^{-1/x^2}$ with $P$ a polynomial, which tends to zero as $x \to 0$). Hence the Maclaurin series of $f$ converges everywhere to $0$, but it equals $f(x)$ only at $x = 0$.

When does the Taylor series equal $f$? By **Taylor's formula**, $f(x) = \sum_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x - x_0)^k + R_n(x)$, and the partial sums of the Taylor series are exactly the **Taylor polynomials**; therefore:

**Theorem 9.2.6** Let $f$ have derivatives of all orders on $(x_0 - R, x_0 + R)$. Then $f$ can be expanded in its Taylor series on this interval (that is, the Taylor series converges to $f(x)$) if and only if the remainder satisfies $R_n(x) \to 0$ ($n \to \infty$) for every $x$ in the interval.

For the remainder one may use the **Lagrange form of the remainder** $R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)^{n+1}$ ($\xi$ between $x_0$ and $x$), or the integral form

$$
R_n(x) = \frac{1}{n!}\int_{x_0}^x f^{(n+1)}(t)(x - t)^n\,\mathrm{d}t
$$
(obtained by repeatedly integrating $f(x) - f(x_0) = \int_{x_0}^x f'(t)\,\mathrm{d}t$ by parts).

**Theorem 9.2.7** Let $f$ have derivatives of all orders on $(x_0 - R, x_0 + R)$, and suppose there is $M > 0$ such that $|f^{(n)}(x)| \le M$ for all $x$ in the interval and all $n$. Then $f$ can be expanded in its Taylor series on this interval.

**Proof** $|R_n(x)| \le \frac{M}{(n+1)!}|x - x_0|^{n+1} \le \frac{MR^{n+1}}{(n+1)!} \to 0$. $\square$

**Example 9.2.4 (Five Basic Expansions)**

1. $\mathrm{e}^x$: for every $R > 0$, on $(-R,R)$ we have $|(\mathrm{e}^x)^{(n)}| = \mathrm{e}^x \le \mathrm{e}^R$, so by Theorem 9.2.7, $\mathrm{e}^x = \sum_{n=0}^\infty\frac{x^n}{n!}$ for $x \in \mathbb{R}$.
2. $\sin x$: $\sin^{(n)}x = \sin\left(x + \frac{n\pi}{2}\right)$ and $|\sin^{(n)}x| \le 1$, so $\sin x = \sum_{k=0}^\infty\frac{(-1)^k}{(2k+1)!}x^{2k+1}$ for $x \in \mathbb{R}$; differentiating term by term gives $\cos x = \sum_{k=0}^\infty\frac{(-1)^k}{(2k)!}x^{2k}$ for $x \in \mathbb{R}$.
3. $\ln(1 + x)$: integrating $\frac{1}{1+t} = \sum(-1)^nt^n$ term by term over $[0,x]$ gives $\ln(1 + x) = \sum_{n=1}^\infty\frac{(-1)^{n-1}}{n}x^n$ for $|x| < 1$. At $x = 1$ the series converges, so by Abel's second theorem (or by directly estimating the Lagrange remainder, $|R_n(1)| \le \frac{1}{n+1}$) the expansion holds on $(-1, 1]$.
4. $(1 + x)^\alpha$ ($\alpha$ not a nonnegative integer): let $\binom\alpha n = \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}$ denote the generalized binomial coefficient. The ratio test shows that $\sum\binom\alpha nx^n$ has radius of convergence $1$, and with the integral form of the remainder one can prove that $R_n(x) \to 0$ for $|x| < 1$. Hence

$$
(1 + x)^\alpha = \sum_{n=0}^\infty\binom\alpha nx^n, \qquad |x| < 1;
$$
the right-hand side is called the *binomial series*. When $\alpha$ is a nonnegative integer it is a finite sum, namely the binomial theorem, valid for all $x$. The behavior at the endpoints depends on $\alpha$: for $\alpha \le -1$ the series diverges at both endpoints and the expansion holds on $(-1,1)$; for $-1 < \alpha < 0$ it converges only at $x = 1$ and the expansion holds on $(-1, 1]$; for $\alpha > 0$ it converges at both endpoints and the expansion holds on $[-1, 1]$. The case $\alpha = -1$ is $\frac{1}{1+x} = \sum(-1)^nx^n$.

![The Taylor partial sums of 1/(1+x^2) approximate the function for |x| < 1 and diverge for |x| > 1, although the function is smooth on the whole real line](./plots/taylor-radius.py)

The radius of convergence cannot always be read off from the behavior of the function on the real line: $\frac{1}{1+x^2} = \sum(-1)^nx^{2n}$ has radius of convergence $1$, although this function is infinitely differentiable everywhere on $\mathbb{R}$. The reason lies in the complex plane: $1 + z^2$ vanishes at $z = \pm\mathrm{i}$, whose distance from the origin is $1$. Complex analysis provides the complete explanation.

In practice one rarely computes $f^{(n)}(x_0)$ directly to find an expansion. More often it is derived from the basic expansions by substitution, arithmetic operations, and termwise differentiation and integration (indirect expansion); the uniqueness of the expansion (Corollary 9.2.1) guarantees that the result is the Taylor series.

**Example 9.2.5**

1. $\frac{1}{(1-x)(2-x)} = \frac{1}{1-x} - \frac{1}{2-x} = \sum_{n=0}^\infty x^n - \frac12\sum_{n=0}^\infty\left(\frac x2\right)^n = \sum_{n=0}^\infty\left(1 - \frac{1}{2^{n+1}}\right)x^n$ for $|x| < 1$ (the intersection of the two intervals of convergence).
2. To expand $\ln x$ in powers of $x - 2$: $\ln x = \ln2 + \ln\left(1 + \frac{x-2}{2}\right) = \ln2 + \sum_{n=1}^\infty\frac{(-1)^{n-1}}{n\,2^n}(x - 2)^n$; from $-1 < \frac{x-2}{2} \le 1$, the expansion holds on $(0, 4]$.
3. $\arctan x = \int_0^x\frac{\mathrm{d}t}{1+t^2} = \sum_{n=0}^\infty\frac{(-1)^n}{2n+1}x^{2n+1}$ for $|x| < 1$; at $x = \pm1$ the series converges, so by Abel's second theorem the expansion holds on $[-1,1]$. Setting $x = 1$ gives $\frac\pi4 = 1 - \frac13 + \frac15 - \cdots$.

### 9.2.4. Summing Power Series

Conversely, given a power series we can find its sum function, and from it the sums of numerical series.

**Algorithm 9.2.1 (Summing a Power Series)**

1. Find the radius and the interval of convergence;
2. By termwise differentiation or integration (after multiplying or dividing by a power of $x$ if necessary), transform the series into one whose sum is known (a geometric series, $\mathrm{e}^x$, and so on);
3. Invert the operations of step 2 (integrate or differentiate) to obtain the sum function, paying attention to constants of integration and to the special treatment of $x = 0$;
4. To sum a numerical series $\sum c_n$: find a power series $\sum c_nx^n$ and substitute a suitable $x$ (at an endpoint, use Abel's second theorem).

**Example 9.2.6** Compute $\sum_{n=1}^\infty\frac{n}{(n+1)!}$.

**Solution** Let $S(x) = \sum_{n=1}^\infty\frac{n}{(n+1)!}x^{n-1}$, with $R = +\infty$. Integrating term by term, for $x \ne 0$,

$$
\int_0^x S(t)\,\mathrm{d}t = \sum_{n=1}^\infty\frac{x^n}{(n+1)!} = \frac1x\sum_{n=1}^\infty\frac{x^{n+1}}{(n+1)!} = \frac{\mathrm{e}^x - 1 - x}{x}.
$$

Differentiating gives $S(x) = \frac{(x-1)\mathrm{e}^x + 1}{x^2}$, and the required sum is $S(1) = 1$. (Alternatively, telescope directly: $\frac{n}{(n+1)!} = \frac{1}{n!} - \frac{1}{(n+1)!}$.)

**Example 9.2.7** Compute $\sum_{n=1}^\infty(-1)^n\frac{n(n+1)}{2^n}$.

**Solution** Let $S(x) = \sum_{n=1}^\infty(-1)^nn(n+1)x^{n-1}$ for $|x| < 1$; the required sum is $\frac12S\left(\frac12\right)$. Integrating twice,

$$
\int_0^x\left(\int_0^t S(s)\,\mathrm{d}s\right)\mathrm{d}t = \sum_{n=1}^\infty(-1)^nx^{n+1} = -\frac{x^2}{1+x} = 1 - x - \frac{1}{1+x}.
$$

Differentiating twice gives $S(x) = -\frac{2}{(1+x)^3}$, and the required sum is $\frac12\cdot\left(-\frac{2}{(3/2)^3}\right) = -\frac{8}{27}$.

## 9.3. Fourier Series

### 9.3.1. Fourier Series of Periodic Functions

The simplest motion with period $T$ is simple harmonic motion $A\sin(\omega x + \varphi)$, where $A > 0$ is the amplitude, $\omega = \frac{2\pi}{T}$ the angular frequency and $\varphi$ the initial phase. For a positive integer $n$, $A_n\sin(n\omega x + \varphi_n)$ also has period $T$; it is called the $n$-th harmonic and can be written as $a_n\cos n\omega x + b_n\sin n\omega x$ (with $a_n = A_n\sin\varphi_n$, $b_n = A_n\cos\varphi_n$). A series of the form

$$
\frac{a_0}{2} + \sum_{n=1}^\infty(a_n\cos n\omega x + b_n\sin n\omega x)
$$
is called a *trigonometric series*. The question is: can a function with period $T$ be represented as a superposition of harmonics? The approach is to assume first that it can, determine what the coefficients must be, and then investigate whether the series actually converges to $f$. We first take $T = 2\pi$ ($\omega = 1$).

The key to finding the coefficients is the orthogonality of the trigonometric functions.

**Definition 9.3.1 (Orthogonal System of Functions)** Let $f, g$ be functions on an interval $[a,b]$ (finite or infinite). If $\int_a^b f(x)g(x)\,\mathrm{d}x = 0$, then $f$ and $g$ are said to be orthogonal on $[a,b]$. If a sequence of functions $\varphi_0, \varphi_1, \varphi_2, \dots$ satisfies $\int_a^b\varphi_i(x)\varphi_j(x)\,\mathrm{d}x = 0$ ($i \ne j$), it is called an orthogonal system of functions on $[a,b]$; if moreover $\int_a^b\varphi_i^2\,\mathrm{d}x = 1$, it is called orthonormal.

This is precisely **orthogonality** with respect to the integral **inner product** $\langle f, g\rangle = \int_a^b fg\,\mathrm{d}x$ on a function space ([Section 12.3 of 2.1.12](/2.1.12#sec-12.3)).

**Example 9.3.1** The trigonometric system $1, \cos x, \sin x, \cos2x, \sin2x, \dots$ is an orthogonal system of functions on $[-\pi, \pi]$: by the product-to-sum formulas, $\int_{-\pi}^\pi\cos mx\cos nx\,\mathrm{d}x = \int_{-\pi}^\pi\sin mx\sin nx\,\mathrm{d}x = 0$ for $m \ne n$, and $\int_{-\pi}^\pi\sin mx\cos nx\,\mathrm{d}x = 0$ for all $m, n$ (the integrand is odd). Moreover,

$$
\int_{-\pi}^\pi1\,\mathrm{d}x = 2\pi, \qquad \int_{-\pi}^\pi\cos^2nx\,\mathrm{d}x = \int_{-\pi}^\pi\sin^2nx\,\mathrm{d}x = \pi \quad (n \ge 1),
$$
so $\frac{1}{\sqrt{2\pi}}, \frac{\cos x}{\sqrt\pi}, \frac{\sin x}{\sqrt\pi}, \dots$ is orthonormal. More generally, $1, \cos\frac{n\pi x}{l}, \sin\frac{n\pi x}{l}$ ($n \ge 1$) is an orthogonal system of functions on any interval of length $2l$.

Suppose $f$ has period $2\pi$, $f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty(a_n\cos nx + b_n\sin nx)$, and the right-hand side may be integrated term by term (for instance, if it converges uniformly). Integrating both sides over $[-\pi,\pi]$, orthogonality leaves only one term: $\int_{-\pi}^\pi f\,\mathrm{d}x = \pi a_0$. Multiplying both sides by $\cos nx$ and integrating leaves only $\int_{-\pi}^\pi f(x)\cos nx\,\mathrm{d}x = a_n\pi$; multiplying by $\sin nx$ works the same way. This is exactly the principle that "coordinates with respect to an orthogonal basis are obtained by taking inner products".

**Definition 9.3.2 (Fourier Series)** Let $f$ have period $2\pi$ and be integrable on $[-\pi, \pi]$. The numbers

$$
a_n = \frac1\pi\int_{-\pi}^\pi f(x)\cos nx\,\mathrm{d}x \;(n = 0, 1, 2, \dots), \qquad b_n = \frac1\pi\int_{-\pi}^\pi f(x)\sin nx\,\mathrm{d}x \;(n = 1, 2, \dots)
$$
are called the **Fourier coefficients** of $f$, and the trigonometric series formed with them is called the Fourier series of $f$, written

$$
f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty(a_n\cos nx + b_n\sin nx).
$$

The formula for $a_0$ agrees with that for $a_n$, which is why the constant term is written $\frac{a_0}{2}$. As with Taylor series, $\sim$ only means "the series computed from $f$": the Fourier series of an integrable function need not converge, and even when it converges, it need not converge to $f$. The following theorem gives a sufficient condition that is easy to verify.

**Theorem 9.3.1 (Dirichlet's Convergence Theorem)** Let $f$ have period $2\pi$, be piecewise monotone on $[-\pi, \pi]$ (or have only finitely many extreme points), and have at most finitely many discontinuities, all of the first kind (removable or jump). Then the Fourier series of $f$ converges everywhere, and

1. at a point of continuity $x_0$ of $f$, the sum of the series equals $f(x_0)$;
2. at a point of discontinuity $x_0$ of $f$, the sum of the series equals $\frac12\bigl(f(x_0 - 0) + f(x_0 + 0)\bigr)$;
3. at the endpoints $x = \pm\pi$, the sum of the series equals $\frac12\bigl(f(-\pi + 0) + f(\pi - 0)\bigr)$.

The hypotheses of the theorem are called the **Dirichlet conditions**. Item 3 is really item 2: once a function on $[-\pi,\pi]$ is extended periodically, $\pm\pi$ are in general jump discontinuities. This theorem is sometimes also called "Dirichlet's test"; to distinguish it from **Dirichlet's test** for numerical series in Section 8.3.4, we call it Dirichlet's convergence theorem. The proof uses the Dirichlet kernel of Section 9.3.3 and is omitted here.

**Example 9.3.2** Let $f$ have period $2\pi$ with $f(x) = -1$ for $-\pi < x < 0$ and $f(x) = 1$ for $0 < x < \pi$ (a square wave). Since $f$ is an **odd function**, $a_n = 0$, and

$$
b_n = \frac2\pi\int_0^\pi\sin nx\,\mathrm{d}x = \frac{2(1 - \cos n\pi)}{n\pi} = \begin{cases}\dfrac{4}{n\pi}, & n \text{ odd},\\ 0, & n \text{ even}.\end{cases}
$$

By Dirichlet's convergence theorem,

$$
\frac4\pi\sum_{n=1}^\infty\frac{\sin(2n-1)x}{2n-1} = \begin{cases}1, & 0 < x < \pi,\\ 0, & x = -\pi, 0, \pi,\\ -1, & -\pi < x < 0.\end{cases}
$$

At the jumps, the series converges to the average $0$ of the one-sided limits. Setting $x = \frac\pi2$ gives $1 - \frac13 + \frac15 - \cdots = \frac\pi4$.

![Fourier partial sums of the square wave: they converge to 0 at the jump (left); near the jump the overshoot narrows as the number of terms grows, but its height does not decrease and stays at about 9% of the jump (right)](./plots/fourier-gibbs.py)

The figure shows that near a jump the partial sums always have a peak of about $1.179$ (the jump has height $2$, so the overshoot of about $0.179$ is about $9\%$ of it). As the number of terms increases, the peak moves toward the jump and becomes narrower, but its height does not decrease. This is called the *Gibbs phenomenon*. It does not contradict Dirichlet's convergence theorem: for each fixed $x \ne 0$ the peak eventually moves to the left of $x$, and $S_N(x) \to 1$; but the convergence is not uniform near the jump. This is also the contrapositive of Theorem 9.1.4: a uniform limit of continuous functions (the partial sums) must be continuous, whereas the square wave is not.

**Example 9.3.3** Let $f$ have period $2\pi$ with $f(x) = \frac\pi2 - |x|$ for $-\pi \le x \le \pi$ (a triangle wave). Since $f$ is an **even function**, $b_n = 0$; moreover $a_0 = 0$ and

$$
a_n = \frac2\pi\int_0^\pi\left(\frac\pi2 - x\right)\cos nx\,\mathrm{d}x = \frac{2(1 - \cos n\pi)}{\pi n^2}, \qquad a_{2k} = 0, \quad a_{2k+1} = \frac{4}{\pi(2k+1)^2}.
$$

Since $f$ is continuous and $f(-\pi) = f(\pi)$, Dirichlet's convergence theorem gives $f(x) = \frac4\pi\sum_{k=0}^\infty\frac{\cos(2k+1)x}{(2k+1)^2}$ for all $x$ (by the Weierstrass M-test, the convergence is even uniform). Setting $x = 0$,

$$
\sum_{k=0}^\infty\frac{1}{(2k+1)^2} = \frac{\pi^2}{8}, \qquad \text{hence} \quad \sum_{n=1}^\infty\frac{1}{n^2} = \frac{\pi^2}{8} + \frac14\sum_{n=1}^\infty\frac{1}{n^2} \;\Rightarrow\; \sum_{n=1}^\infty\frac{1}{n^2} = \frac{\pi^2}{6}.
$$

The triangle wave is continuous, and its coefficients decay like $\frac{1}{n^2}$; the square wave has jumps, and its coefficients decay only like $\frac1n$. The smoother the function, the faster its Fourier coefficients decay.

For a function with period $2l$, the substitution $x = \frac{l}{\pi}t$ turns the period $2l$ into $2\pi$ and gives

$$
f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty\left(a_n\cos\frac{n\pi x}{l} + b_n\sin\frac{n\pi x}{l}\right), \quad a_n = \frac1l\int_{-l}^lf(x)\cos\frac{n\pi x}{l}\,\mathrm{d}x, \quad b_n = \frac1l\int_{-l}^lf(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x.
$$

By the integral property of **periodic functions** ([Theorem 7.4.3](/2.2.7#thm-7.4.3)), the coefficients may be computed over any period $[a, a+2l]$ of length $2l$. Dirichlet's convergence theorem remains valid.

**Example 9.3.4** Represent $f(x) = 2x + 1$ on $[0,2)$ by a Fourier series.

**Solution** Regard $f$ as a function with period $2$ ($l = 1$) and compute the coefficients over $[0,2]$: $a_0 = \int_0^2(2x+1)\,\mathrm{d}x = 6$, $a_n = \int_0^2(2x+1)\cos n\pi x\,\mathrm{d}x = 0$, and $b_n = \int_0^2(2x+1)\sin n\pi x\,\mathrm{d}x = -\frac{4}{n\pi}$. By Dirichlet's convergence theorem,

$$
3 - \frac4\pi\sum_{n=1}^\infty\frac{\sin n\pi x}{n} = \begin{cases}2x + 1, & 0 < x < 2,\\ \frac12\bigl(f(0) + f(2 - 0)\bigr) = 3, & x = 0, 2.\end{cases}
$$

### 9.3.2. Sine Series and Cosine Series

If $f$ is an **odd function** on $[-\pi,\pi]$, then $a_n = 0$ and $b_n = \frac2\pi\int_0^\pi f(x)\sin nx\,\mathrm{d}x$, so the Fourier series of $f$ contains only sine terms; it is called a *Fourier sine series*. If $f$ is an **even function**, then $b_n = 0$ and $a_n = \frac2\pi\int_0^\pi f(x)\cos nx\,\mathrm{d}x$, so the Fourier series contains only a constant term and cosine terms; it is called a *Fourier cosine series*.

A function defined only on $[0, \pi]$ can first be extended to $[-\pi, \pi]$ and then extended periodically with period $2\pi$; different extensions give different series:

- Setting $f(x) = -f(-x)$ ($-\pi \le x < 0$), the *odd extension*, gives the sine series $f(x) \sim \sum_{n=1}^\infty b_n\sin nx$ with $b_n = \frac2\pi\int_0^\pi f(x)\sin nx\,\mathrm{d}x$;
- Setting $f(x) = f(-x)$ ($-\pi \le x < 0$), the *even extension*, gives the cosine series $f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty a_n\cos nx$ with $a_n = \frac2\pi\int_0^\pi f(x)\cos nx\,\mathrm{d}x$.

The same applies to functions on $[0, l]$: $b_n = \frac2l\int_0^lf(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x$ and $a_n = \frac2l\int_0^lf(x)\cos\frac{n\pi x}{l}\,\mathrm{d}x$. Both expansions converge to $f$ at the points of continuity in $(0,l)$; they differ at the endpoints. The odd extension generally creates jumps at $x = 0, l$, where the sine series converges to $0$; the even extension preserves continuity, and the cosine series converges to $f(0)$ and $f(l)$ at the endpoints.

**Example 9.3.5** Expand $f(x) = x$ ($0 \le x \le \pi$) in a cosine series and in a sine series.

**Solution** Cosine series: $a_0 = \frac2\pi\int_0^\pi x\,\mathrm{d}x = \pi$ and $a_n = \frac2\pi\int_0^\pi x\cos nx\,\mathrm{d}x = \frac{2\bigl((-1)^n - 1\bigr)}{\pi n^2}$. The even extension is a continuous triangle wave, and

$$
x = \frac\pi2 - \frac4\pi\sum_{k=0}^\infty\frac{\cos(2k+1)x}{(2k+1)^2}, \qquad 0 \le x \le \pi.
$$

Sine series: $b_n = \frac2\pi\int_0^\pi x\sin nx\,\mathrm{d}x = \frac{2(-1)^{n-1}}{n}$. The odd extension jumps at $x = \pi$, and

$$
x = 2\sum_{n=1}^\infty\frac{(-1)^{n-1}\sin nx}{n}, \qquad 0 \le x < \pi,
$$
while at $x = \pi$ the sum of the series is $0$. The coefficients of the cosine series decay like $\frac{1}{n^2}$, those of the sine series only like $\frac1n$, in agreement with the observation made in Examples 9.3.2 and 9.3.3.

**Example 9.3.6** Expand $f(x) = \sin\frac{\pi x}{l}$ ($0 \le x < \frac l2$), $f(x) = 0$ ($\frac l2 \le x \le l$) in a sine series.

**Solution** $b_1 = \frac2l\int_0^{l/2}\sin^2\frac{\pi x}{l}\,\mathrm{d}x = \frac12$. For $n \ge 2$, the product-to-sum formula shows that $b_n = \frac2l\int_0^{l/2}\sin\frac{\pi x}{l}\sin\frac{n\pi x}{l}\,\mathrm{d}x$ equals $0$ for odd $n$ and $-\frac{(-1)^k4k}{\pi(4k^2 - 1)}$ for $n = 2k$. Hence

$$
\frac12\sin\frac{\pi x}{l} - \frac4\pi\sum_{k=1}^\infty\frac{(-1)^kk}{4k^2 - 1}\sin\frac{2k\pi x}{l} = f(x), \qquad x \in \left[0, \frac l2\right) \cup \left(\frac l2, l\right],
$$
and at the jump $x = \frac l2$ the sum of the series is $\frac12$.

### 9.3.3. The Complex Form of Fourier Series

By **Euler's formula** $\mathrm{e}^{\mathrm{i}x} = \cos x + \mathrm{i}\sin x$,

$$
\cos nx = \frac{\mathrm{e}^{\mathrm{i}nx} + \mathrm{e}^{-\mathrm{i}nx}}{2}, \qquad \sin nx = \frac{\mathrm{e}^{\mathrm{i}nx} - \mathrm{e}^{-\mathrm{i}nx}}{2\mathrm{i}},
$$
and substituting into the Fourier series gives $\frac{a_0}{2} + \sum_{n=1}^\infty\left(\frac{a_n - \mathrm{i}b_n}{2}\mathrm{e}^{\mathrm{i}nx} + \frac{a_n + \mathrm{i}b_n}{2}\mathrm{e}^{-\mathrm{i}nx}\right)$. With $c_0 = \frac{a_0}{2}$, $c_n = \frac{a_n - \mathrm{i}b_n}{2}$ and $c_{-n} = \frac{a_n + \mathrm{i}b_n}{2}$ ($n \ge 1$), the three coefficient formulas merge into one:

$$
f(x) \sim \sum_{n=-\infty}^{+\infty}c_n\mathrm{e}^{\mathrm{i}nx}, \qquad c_n = \frac{1}{2\pi}\int_{-\pi}^\pi f(x)\mathrm{e}^{-\mathrm{i}nx}\,\mathrm{d}x, \quad n = 0, \pm1, \pm2, \dots
$$

Note that the exponents have opposite signs: $\mathrm{e}^{\mathrm{i}nx}$ in the series and $\mathrm{e}^{-\mathrm{i}nx}$ in the coefficients. The symmetric sum $\sum_{n=-\infty}^{+\infty}$ is understood as $\lim_{N\to\infty}\sum_{n=-N}^N$, and $c_0$ appears only once. For a real function the coefficients satisfy $c_{-n} = \overline{c_n}$ (the **complex conjugate**). The system $\{\mathrm{e}^{\mathrm{i}nx}\}$ is orthogonal with respect to the complex inner product $\langle f, g\rangle = \int_{-\pi}^\pi f\bar g\,\mathrm{d}x$, and $c_n = \frac{\langle f, \mathrm{e}^{\mathrm{i}nx}\rangle}{\langle\mathrm{e}^{\mathrm{i}nx}, \mathrm{e}^{\mathrm{i}nx}\rangle}$ is once again "coordinate equals inner product". For period $2l$,

$$
f(x) \sim \sum_{n=-\infty}^{+\infty}c_n\mathrm{e}^{\mathrm{i}n\pi x/l}, \qquad c_n = \frac{1}{2l}\int_{-l}^lf(x)\mathrm{e}^{-\mathrm{i}n\pi x/l}\,\mathrm{d}x.
$$

The complex form makes the partial sums easy to compute. Substituting the coefficients into $S_n(x) = \sum_{k=-n}^nc_k\mathrm{e}^{\mathrm{i}kx}$, putting $t = u - x$, and using the periodicity of the integrand,

$$
S_n(x) = \frac{1}{2\pi}\int_{-\pi}^\pi f(x + t)D_n(t)\,\mathrm{d}t, \qquad D_n(t) = \sum_{k=-n}^n\mathrm{e}^{-\mathrm{i}kt} = \frac{\sin\left(n + \frac12\right)t}{\sin\frac t2},
$$
where the last step sums a geometric series. The function $D_n$ is called the Dirichlet kernel: the partial sum is a weighted average of $f$ against $D_n$. The proof of Dirichlet's convergence theorem starts from this expression and analyzes how $D_n$ concentrates near $t = 0$ as $n \to \infty$.

## Summary

| Concept | Key points |
|---|---|
| Uniform convergence | $\sup_I\lvert S_n - S\rvert \to 0$; tests: Cauchy criterion for uniform convergence, Weierstrass M-test $\lvert u_n(x)\rvert \le c_n$ |
| Termwise limits | Continuous terms + uniform convergence $\Rightarrow$ continuous sum function |
| Termwise integration | Continuous terms + uniform convergence $\Rightarrow$ $\int\sum = \sum\int$ |
| Termwise differentiation | Convergent series + uniformly convergent series of derivatives $\Rightarrow$ $(\sum u_n)' = \sum u_n'$ |
| Radius of convergence | Abel's theorem; $R = 1/\lim\lvert a_{n+1}/a_n\rvert = 1/\lim\sqrt[n]{\lvert a_n\rvert}$; endpoints examined separately |
| Sum function | Differentiable to all orders on $(-R,R)$; termwise differentiation and integration preserve $R$; one-sided continuity at a convergent endpoint (Abel's second theorem) |
| Taylor series | Converges to $f$ $\iff$ $R_n(x) \to 0$; uniformly bounded derivatives suffice; $\mathrm{e}^{-1/x^2}$ is a counterexample |
| Fourier coefficients | $a_n = \frac1\pi\int_{-\pi}^\pi f\cos nx$, $b_n = \frac1\pi\int_{-\pi}^\pi f\sin nx$, $c_n = \frac{1}{2\pi}\int_{-\pi}^\pi f\mathrm{e}^{-\mathrm{i}nx}$ |
| Dirichlet's convergence theorem | Piecewise monotone, finitely many discontinuities of the first kind: converges to $f$ at points of continuity, to the average of the one-sided limits at discontinuities |

| Function | Maclaurin series | Range of validity |
|---|---|---|
| $\mathrm{e}^x$ | $\sum_{n=0}^\infty\frac{x^n}{n!}$ | $(-\infty, +\infty)$ |
| $\sin x$ | $\sum_{k=0}^\infty\frac{(-1)^kx^{2k+1}}{(2k+1)!}$ | $(-\infty, +\infty)$ |
| $\cos x$ | $\sum_{k=0}^\infty\frac{(-1)^kx^{2k}}{(2k)!}$ | $(-\infty, +\infty)$ |
| $\ln(1 + x)$ | $\sum_{n=1}^\infty\frac{(-1)^{n-1}x^n}{n}$ | $(-1, 1]$ |
| $\frac{1}{1-x}$ | $\sum_{n=0}^\infty x^n$ | $(-1, 1)$ |
| $\arctan x$ | $\sum_{n=0}^\infty\frac{(-1)^nx^{2n+1}}{2n+1}$ | $[-1, 1]$ |
| $(1 + x)^\alpha$ | $\sum_{n=0}^\infty\binom\alpha nx^n$ | $\alpha \le -1$: $(-1,1)$; $-1 < \alpha < 0$: $(-1,1]$; $\alpha > 0$: $[-1,1]$ |

| Expansion | Coefficients | Sum at the endpoints $x = 0, l$ |
|---|---|---|
| Period $2l$ | $a_n = \frac1l\int_{-l}^lf\cos\frac{n\pi x}{l}$, $b_n = \frac1l\int_{-l}^lf\sin\frac{n\pi x}{l}$ | — |
| Sine series (odd extension) | $b_n = \frac2l\int_0^lf\sin\frac{n\pi x}{l}$ | $0$ |
| Cosine series (even extension) | $a_n = \frac2l\int_0^lf\cos\frac{n\pi x}{l}$ | $f(0)$, $f(l)$ |
