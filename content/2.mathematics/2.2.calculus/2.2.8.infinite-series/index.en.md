---
title: Infinite Series
source_hash: c3187806bc1f
---

Does it make sense to add infinitely many numbers? The sum $1 + \frac12 + \frac14 + \cdots$ ought to equal $2$, whereas $1 - 1 + 1 - 1 + \cdots$ seems to equal nothing at all. This chapter defines an infinite sum as the limit of the **sequence** of partial sums, so convergence of a series is just convergence of a sequence in the sense of [Chapter 2](/2.2.2), and the **Cauchy criterion** and the **monotone convergence theorem** can be used directly.

The main theme of the chapter is testing for convergence, in two stages according to the type of series. Section 8.2 treats series of nonnegative terms: their partial sums are monotone, so such a series converges if and only if its partial sums are bounded. This yields the comparison test, the ratio and root tests, and the integral test, which correspond almost one to one to the tests for improper integrals in Section 7.7 of [Chapter 7](/2.2.7) (the $p$-series corresponds to $\int_1^{+\infty}x^{-p}\,\mathrm{d}x$). Section 8.3 treats general series: the Leibniz test for alternating series, the distinction between absolute and conditional convergence, and the tests of Abel and Dirichlet. Absolutely convergent series can be rearranged and multiplied freely, just like finite sums; conditionally convergent series cannot, and a rearrangement may change the sum. The next chapter extends these results to series whose terms are functions, and all the tests of this chapter will be used there.

## 8.1. Series and Their Basic Properties

### 8.1.1. Basic Definitions

**Definition 8.1.1 (Series)** Let $\{u_n\}$ be a sequence. The expression

$$
\sum_{n=1}^\infty u_n = u_1 + u_2 + \cdots + u_n + \cdots
$$
is called an (infinite) series, and $u_n$ is called its general term. The number $S_n = u_1 + \cdots + u_n$ is called the $n$-th **partial sum** of the series, and $\{S_n\}$ the sequence of partial sums. If $\lim_{n\to\infty}S_n = S$ exists, the series is said to converge, and $S$ is called the sum of the series, written $\sum_{n=1}^\infty u_n = S$; otherwise the series is said to diverge.

Series and sequences can be converted into each other: $u_n = S_n - S_{n-1}$. So the theory of series is not a new theory of limits; its point is to decide whether the sequence of partial sums converges by looking at the general term $u_n$ rather than at the partial sums.

**Example 8.1.1** Consider $\sum_{n=1}^\infty\frac{1}{n(n+1)}$. Since $\frac{1}{n(n+1)} = \frac1n - \frac{1}{n+1}$, the partial sums are $S_n = 1 - \frac{1}{n+1} \to 1$, so the series converges with sum $1$. Summation by cancellation of adjacent terms in this way is called telescoping.

**Example 8.1.2** Consider $\sum_{n=1}^\infty\frac{1}{\sqrt n}$. Since $S_n \ge n\cdot\frac{1}{\sqrt n} = \sqrt n \to +\infty$, the series diverges, even though its general term tends to $0$.

### 8.1.2. Properties of Series

**Property 8.1.1 (Necessary Condition for Convergence)** If $\sum u_n$ converges, then $\lim_{n\to\infty}u_n = 0$.

**Proof** $u_n = S_n - S_{n-1} \to S - S = 0$. $\square$

The converse is false (Example 8.1.2). The useful form is the contrapositive: a series whose general term does not tend to $0$ diverges, for example $\sum(-1)^n$ and $\sum\frac{n}{2n+1}$.

**Property 8.1.2 (Linearity)** If $\sum u_n$ and $\sum v_n$ converge, then for constants $\alpha, \beta$ the series $\sum(\alpha u_n + \beta v_n)$ converges, and $\sum(\alpha u_n + \beta v_n) = \alpha\sum u_n + \beta\sum v_n$.

**Property 8.1.3 (Associativity)** If $\sum u_n$ converges, then any series obtained from it by inserting parentheses, without changing the order of the terms, also converges, and to the same sum.

**Proof** The sequence of partial sums of the parenthesized series is a **subsequence** of $\{S_n\}$, and every subsequence of a convergent sequence converges to the same limit. $\square$

The converse is false: $\sum_{n=1}^\infty(-1)^n$ diverges, but $\sum_{k=1}^\infty\bigl[(-1)^{2k-1} + (-1)^{2k}\bigr] = 0$ converges. Thus parentheses may not be inserted arbitrarily into a divergent series, nor removed arbitrarily from a convergent one.

**Property 8.1.4** Adding, deleting or changing finitely many terms of a series does not affect its convergence or divergence (although, in the convergent case, it may change the sum).

**Proof** By the **Cauchy criterion** for sequences, $\sum u_n$ converges $\iff$ for every $\varepsilon > 0$ there exists $N$ such that $|S_n - S_m| = |u_{m+1} + \cdots + u_n| < \varepsilon$ whenever $n > m > N$. This condition involves only terms far enough out. $\square$

### 8.1.3. Geometric Series and p-Series

Two basic families of series serve as the "yardsticks" for all the comparison tests that follow.

For $a \ne 0$, the series $\sum_{n=1}^\infty aq^{n-1} = a + aq + aq^2 + \cdots$ is called a *geometric series*. For $q \ne 1$, $S_n = \frac{a(1 - q^n)}{1 - q}$, so

- if $|q| < 1$, the series converges, with sum $\dfrac{a}{1-q}$;
- if $|q| \ge 1$, the general term does not tend to $0$, and the series diverges.

For a constant $p$, the series $\sum_{n=1}^\infty\frac{1}{n^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \cdots$ is called a *p-series*; the case $p = 1$, $\sum\frac1n$, is called the *harmonic series*.

**Theorem 8.1.1** The $p$-series converges for $p > 1$ and diverges for $p \le 1$.

**Proof** For $p \le 0$ the general term does not tend to $0$. Let $p > 0$. Then $x^{-p}$ is decreasing, so for $k \ge 2$,

$$
\int_k^{k+1}\frac{\mathrm{d}x}{x^p} \le \frac{1}{k^p} \le \int_{k-1}^k\frac{\mathrm{d}x}{x^p}.
$$

For $p > 1$, $S_n \le 1 + \int_1^n x^{-p}\,\mathrm{d}x \le 1 + \frac{1}{p-1}$; the partial sums of a series of nonnegative terms are increasing and bounded above, so the series converges. For $0 < p \le 1$, $S_n \ge \int_1^{n+1}x^{-p}\,\mathrm{d}x \to +\infty$ (the **improper integral over an unbounded interval** diverges), so the series diverges. $\square$

The idea of this proof is generalized to the integral test in Section 8.2.3. For the harmonic series it also gives $\ln(n+1) \le 1 + \frac12 + \cdots + \frac1n \le 1 + \ln n$: the harmonic series diverges, but extremely slowly; the sum of its first million terms is still less than $15$.

## 8.2. Convergence Tests for Series of Nonnegative Terms

**Definition 8.2.1 (Series of Nonnegative Terms)** A series all of whose terms are nonnegative is called a series of nonnegative terms.

The partial sums of a series of nonnegative terms form a nondecreasing sequence, so by the **monotone convergence theorem**,

$$
\text{a series of nonnegative terms converges} \iff \text{its sequence of partial sums is bounded above}.
$$

A series of nonnegative terms either converges to a finite sum or diverges to $+\infty$; all the tests below rest on this fact. The $p$-series and the geometric series (with $a > 0$, $q \ge 0$) are series of nonnegative terms.

### 8.2.1. The Comparison Test and the p-Test

Throughout, $\sum u_n$ and $\sum v_n$ are series of nonnegative terms.

**Theorem 8.2.1 (Comparison Test)** Suppose there are $M > 0$ and a positive integer $N$ such that $u_n \le Mv_n$ for $n > N$.

1. If $\sum v_n$ converges, then $\sum u_n$ converges;
2. If $\sum u_n$ diverges, then $\sum v_n$ diverges.

**Proof** By Property 8.1.4 we may assume $u_n \le Mv_n$ for all $n$. Then $\sum_{k=1}^n u_k \le M\sum_{k=1}^\infty v_k$, so the partial sums are bounded above. Part 2 is the contrapositive of part 1. $\square$

**Example 8.2.1**

1. $\sum\frac{3}{n^2 - 5n + 5}$: for $n \ge 9$, $n^2 - 5n + 5 \ge \frac{n^2}{2}$, so the general term is at most $\frac{6}{n^2}$; since $\sum\frac1{n^2}$ converges, so does this series.
2. $\sum\frac{1}{\sqrt{n^2 + 2n + 100}}$: for $n \ge 2$, $n^2 + 2n + 100 \le 100n^2$, so the general term is at least $\frac{1}{10n}$; since the harmonic series diverges, so does this series.
3. $\sum\frac{n!}{n^n}$: $\frac{n!}{n^n} = \frac1n\cdot\frac2n\cdots\frac nn \le \frac{2}{n^2}$ ($n \ge 2$), so the series converges.

Taking a $p$-series as the comparison series gives:

**Corollary 8.2.1 (p-Test)** Let $\sum u_n$ be a series of nonnegative terms and $M > 0$.

1. If for some $p > 1$ we have $u_n \le \frac{M}{n^p}$ for all sufficiently large $n$, then $\sum u_n$ converges;
2. If for some $p \le 1$ we have $u_n \ge \frac{M}{n^p}$ for all sufficiently large $n$, then $\sum u_n$ diverges.

The inequalities are often hard to write down directly; the limit form is more convenient, since it only compares the rates at which the general terms tend to zero.

**Theorem 8.2.2 (Limit Comparison Test)** Let $v_n > 0$ and $\lim_{n\to\infty}\frac{u_n}{v_n} = q$.

1. If $0 \le q < +\infty$ and $\sum v_n$ converges, then $\sum u_n$ converges;
2. If $0 < q \le +\infty$ and $\sum v_n$ diverges, then $\sum u_n$ diverges.

In particular, if $0 < q < +\infty$, the two series converge or diverge together; this holds a fortiori when $u_n$ and $v_n$ are **equivalent infinitesimals**.

**Proof** 1. For $n$ large enough, $u_n/v_n < q + 1$; apply Theorem 8.2.1. 2. If $q < +\infty$, then $u_n > \frac q2v_n$ for $n$ large enough; if $q = +\infty$, then $u_n > v_n$ eventually; apply Theorem 8.2.1. $\square$

**Example 8.2.2**

1. $\sum 2^n\sin\frac{1}{3^n}$: $\lim\frac{2^n\sin(1/3^n)}{(2/3)^n} = 1$, and the geometric series $\sum(2/3)^n$ converges, so the series converges.
2. $\sum\ln\left(1 + \frac1n\right)$: $\ln(1 + \frac1n) \sim \frac1n$, so the series diverges.
3. $\sum\ln\left(2 - \cos\frac1n\right)$: $\ln\left(1 + \left(1 - \cos\frac1n\right)\right) \sim 1 - \cos\frac1n \sim \frac{1}{2n^2}$, so the series converges.

**Corollary 8.2.2 (Limit Form of the p-Test)** Let $\sum u_n$ be a series of nonnegative terms.

1. If for some $p > 1$ the limit $\lim_{n\to\infty}n^pu_n$ exists (and is finite), then $\sum u_n$ converges;
2. If for some $p \le 1$ the limit $\lim_{n\to\infty}n^pu_n$ exists and is nonzero, or equals $+\infty$, then $\sum u_n$ diverges.

This is completely parallel to the $p$-test for improper integrals over unbounded intervals ([Theorem 7.7.5](/2.2.7#thm-7.7.5)): the series converges when its general term is an infinitesimal of higher order than $\frac1n$ (at least like $n^{-p}$ with $p > 1$).

**Example 8.2.3**

1. $\sum\frac{\ln n}{n^p}$ ($p > 1$): choose $1 < q < p$; then $n^q\cdot\frac{\ln n}{n^p} = \frac{\ln n}{n^{p-q}} \to 0$, so the series converges. A logarithmic factor does not affect the criterion "the exponent is strictly greater than 1".
2. $\sum\frac{1}{\sqrt[3]{n^2 + n + 7}}$: $n^{2/3}u_n \to 1$ with $p = \frac23 \le 1$, so the series diverges.
3. $\sum\frac{1}{\sqrt n}\tan\frac1n$: $n^{3/2}u_n \to 1$, so the series converges.

**Example 8.2.4** Consider $\sum\left[\frac1n - \ln\left(1 + \frac1n\right)\right]$. By **Taylor's formula** $\ln(1 + x) = x - \frac{x^2}{2} + o(x^2)$, the general term equals $\frac{1}{2n^2} + o\left(\frac{1}{n^2}\right) > 0$, and $n^2u_n \to \frac12$, so the series converges. Consequently $1 + \frac12 + \cdots + \frac1n - \ln(n+1) = \sum_{k=1}^n\left[\frac1k - \ln\left(1 + \frac1k\right)\right]$ converges; its limit is the Euler constant $\gamma \approx 0.5772$.

Finding the principal part of the general term with Taylor's formula and then applying the $p$-test is the most effective way to handle series of this kind.

### 8.2.2. The Ratio Test and the Root Test

Comparing a series with itself: if $u_n$ decays like a geometric series, the ratio of consecutive terms, or the $n$-th root, settles near some number less than $1$.

**Theorem 8.2.3 (Ratio Test)** Let $u_n > 0$ and $\lim_{n\to\infty}\frac{u_{n+1}}{u_n} = q$ (or $+\infty$).

1. If $q < 1$, then $\sum u_n$ converges;
2. If $q > 1$ or $q = +\infty$, then $\sum u_n$ diverges.

If $q = 1$, the test is inconclusive.

**Proof** 1. Choose $r$ with $q < r < 1$. There is $N$ such that $\frac{u_{n+1}}{u_n} < r$ for $n > N$, so $u_{N+k} \le u_{N+1}r^{k-1}$; the claim follows from the comparison test and the convergence of the geometric series $\sum r^k$. 2. Choose $1 < r < q$. For $n$ large enough, $u_{n+1} > ru_n > u_n$, so the general term is increasing and does not tend to zero; the series diverges. $\square$

**Example 8.2.5**

1. $\sum\frac{n^2}{3^n}$: $\frac{u_{n+1}}{u_n} = \frac{(n+1)^2}{3n^2} \to \frac13$, so the series converges.
2. $\sum\frac{1}{3^n - n^3}$: the ratio tends to $\frac13$, so the series converges.
3. $\sum\frac{(n!)^2}{(2n)!}$: $\frac{u_{n+1}}{u_n} = \frac{(n+1)^2}{(2n+2)(2n+1)} \to \frac14$, so the series converges.

The ratio test suits general terms involving factorials and exponentials. It fails when $q = 1$: for both $\sum\frac1n$ and $\sum\frac1{n^2}$ the limit of the ratio is $1$, yet the first diverges and the second converges; in that case use the $p$-test instead.

**Theorem 8.2.4 (Root Test)** Let $u_n \ge 0$ and $\lim_{n\to\infty}\sqrt[n]{u_n} = q$ (or $+\infty$).

1. If $q < 1$, then $\sum u_n$ converges;
2. If $q > 1$ or $q = +\infty$, then $\sum u_n$ diverges.

If $q = 1$, the test is inconclusive.

**Proof** 1. Choose $q < r < 1$; for $n$ large enough, $u_n < r^n$, and we compare with a geometric series. 2. For $n$ large enough, $u_n > 1$, so the general term does not tend to zero. $\square$

**Example 8.2.6**

1. $\sum\frac{n^2}{3^n + 2^n}$: $\sqrt[n]{u_n} \to \frac13$, so the series converges.
2. $\sum\left(\frac{n+1}{n}\right)^{n^2}\frac{1}{3^n}$: $\sqrt[n]{u_n} = \left(1 + \frac1n\right)^n\cdot\frac13 \to \frac{\mathrm{e}}{3} < 1$, so the series converges.
3. $\sum\frac{n\,[\sqrt2 + (-1)^n]^n}{3^n}$: the general term is at most $\frac{n(\sqrt2 + 1)^n}{3^n}$, whose $n$-th root tends to $\frac{\sqrt2 + 1}{3} < 1$, so the series converges by the comparison test. Here the ratio $u_{n+1}/u_n$ tends to $+\infty$ along odd $n$ and to $0$ along even $n$, so the ratio test cannot be applied.

In general, if the limit of the ratios exists, then the limit of the roots also exists and the two are equal, so the root test has a wider range of applicability; the ratio, however, is often easier to compute. Both tests can only detect series that converge "as fast as a geometric series"; for series like the $p$-series they always give $q = 1$.

### 8.2.3. The Integral Test

The proof of Theorem 8.1.1 squeezed a series between improper integrals; in general:

**Theorem 8.2.7 (Integral Test)** Let $f$ be continuous, nonnegative and decreasing on $[1, +\infty)$, and let $u_n = f(n)$. Then

$$
\sum_{n=1}^\infty u_n \text{ converges} \iff \int_1^{+\infty}f(x)\,\mathrm{d}x \text{ converges}.
$$

**Proof** By monotonicity, $u_k \le \int_{k-1}^k f(x)\,\mathrm{d}x \le u_{k-1}$ ($k \ge 2$). Summing over $k = 2, \dots, n$ and writing $S_n = \sum_{k=1}^n u_k$ and $Y_n = \int_1^n f$, we get

$$
S_n - u_1 \le Y_n \le S_{n-1}.
$$

Both $\{S_n\}$ and $\{Y_n\}$ are nondecreasing, and by this inequality one is bounded if and only if the other is. Moreover, since $f \ge 0$, $\int_1^A f$ is monotone in $A$, so $\int_1^{+\infty}f$ converges $\iff \{Y_n\}$ is bounded. $\square$

![The integral test: two families of rectangles built from f(n) squeeze the area under the curve; for p = 1 the series and the integral both diverge, for p = 2 both converge](./plots/integral-test.py)

**Example 8.2.7** The Bertrand series $\sum_{n=2}^\infty\frac{1}{n(\ln n)^p}$ converges if and only if $p > 1$ (starting the sum at $2$ does not affect the proof).

**Proof** The function $f(x) = \frac{1}{x(\ln x)^p}$ is nonnegative on $[2, +\infty)$ and decreasing for $p \ge 0$ (for $p < 0$ the general term is at least $\frac1n$, and the series obviously diverges). With $u = \ln x$, $\int_2^{+\infty}\frac{\mathrm{d}x}{x(\ln x)^p} = \int_{\ln2}^{+\infty}\frac{\mathrm{d}u}{u^p}$, which converges if and only if $p > 1$. $\square$

The series $\sum\frac{1}{n\ln n}$ diverges, even though its general term tends to zero faster than $\frac1n$. The $p$-test fails for it ($n^pu_n$ tends to $+\infty$ for $p > 1$ and to $0$ for $p \le 1$, so neither part applies), whereas the integral test settles the question.

## 8.3. Series with Terms of Arbitrary Sign

When the terms have varying signs, the partial sums are no longer monotone. The simplest case is alternating signs.

### 8.3.1. Alternating Series

**Definition 8.3.1 (Alternating Series)** Let $u_n > 0$. The series $\sum_{n=1}^\infty(-1)^{n-1}u_n = u_1 - u_2 + u_3 - \cdots$ is called an alternating series.

**Theorem 8.3.1 (Alternating Series Test)** If in the alternating series $\sum(-1)^{n-1}u_n$ the sequence $\{u_n\}$ is decreasing and $u_n \to 0$, then

1. $\sum(-1)^{n-1}u_n$ converges;
2. its sum $S$ satisfies $0 \le S \le u_1$;
3. the remainder $r_n = \sum_{k=n+1}^\infty(-1)^{k-1}u_k$ satisfies $|r_n| \le u_{n+1}$.

**Proof** 1. The even partial sums satisfy $S_{2n+2} = S_{2n} + (u_{2n+1} - u_{2n+2}) \ge S_{2n}$, so they increase; moreover

$$
S_{2n} = u_1 - (u_2 - u_3) - \cdots - (u_{2n-2} - u_{2n-1}) - u_{2n} \le u_1,
$$
so they are bounded above, and hence $S_{2n} \to S$. Also $S_{2n-1} = S_{2n} + u_{2n} \to S$. The odd and even subsequences have the same limit, so $S_n \to S$.

2. Take the limit in $0 \le S_{2n} \le u_1$.

3. $r_n = (-1)^n(u_{n+1} - u_{n+2} + \cdots)$, and the series in parentheses is an alternating series satisfying the same hypotheses, so part 2 gives $|r_n| \le u_{n+1}$. $\square$

The remainder estimate says that when the sum of an alternating series is approximated by a partial sum, the error is at most the first omitted term. For example, $\sum\frac{(-1)^{n-1}}{n} = \ln2$ ([Chapter 9](/2.2.9)), and taking the first $1000$ terms gives an error less than $10^{-3}$.

**Example 8.3.1** The series $\sum\frac{(-1)^n}{n}$, $\sum\frac{(-1)^n}{\sqrt n}$ and $\sum_{n=2}^\infty\frac{(-1)^n}{n\ln n}$ all satisfy the hypotheses of the Leibniz test and therefore converge.

Monotonicity cannot be dropped: with $u_{2k-1} = \frac1k$ and $u_{2k} = \frac{1}{k^2}$ we have $u_n \to 0$, but the sum of the first $2n$ terms of $\sum(-1)^{n-1}u_n$ is $\sum_{k=1}^n\left(\frac1k - \frac1{k^2}\right) \to +\infty$.

### 8.3.2. Absolute and Conditional Convergence

**Theorem 8.3.2 (Cauchy Criterion for Series)** $\sum u_n$ converges $\iff$ for every $\varepsilon > 0$ there exists a positive integer $N$ such that for all $n > N$ and all positive integers $p$,

$$
|u_{n+1} + u_{n+2} + \cdots + u_{n+p}| < \varepsilon.
$$

**Proof** This is precisely the **Cauchy criterion** $|S_{n+p} - S_n| < \varepsilon$ for the sequence of partial sums $\{S_n\}$. $\square$

**Definition 8.3.2 (Absolute Convergence)** If $\sum|u_n|$ converges, then $\sum u_n$ is said to be **absolutely convergent**; if $\sum u_n$ converges but $\sum|u_n|$ diverges, then $\sum u_n$ is said to be **conditionally convergent**.

This is the same notion as absolute and conditional convergence of improper integrals in Section 7.7.3: a series can be viewed as the improper integral of a step function.

**Theorem 8.3.3** An absolutely convergent series converges.

**Proof** $|u_{n+1} + \cdots + u_{n+p}| \le |u_{n+1}| + \cdots + |u_{n+p}|$; apply Theorem 8.3.2. $\square$

So to test a general series, first look at $\sum|u_n|$: it is a series of nonnegative terms, and all the tests of Section 8.2 apply. If $\sum|u_n|$ diverges, use the Leibniz test or the tests of Section 8.3.4 to decide whether the series converges conditionally.

**Example 8.3.2** The series $\sum\frac{(-1)^n}{n}$, $\sum\frac{(-1)^n}{\sqrt n}$ and $\sum\frac{(-1)^n}{\ln(n+1)}$ converge conditionally; $\sum\frac{(-1)^n}{n^2}$, $\sum\frac{(-1)^n}{n\sqrt n}$ and $\sum\frac{(-1)^n}{n^p\ln n}$ ($p > 1$) converge absolutely.

**Example 8.3.3** Determine the convergence of $\sum_{n=1}^\infty(-1)^n\frac{a^n}{n^p}$ ($p > 0$).

**Solution** Apply the ratio test to $\sum\frac{|a|^n}{n^p}$: $\frac{|u_{n+1}|}{|u_n|} = \frac{n^p}{(n+1)^p}|a| \to |a|$.

| Case | Conclusion | Reason |
|---|---|---|
| $\lvert a\rvert < 1$ | Converges absolutely | Ratio test |
| $\lvert a\rvert > 1$ | Diverges | General term does not tend to $0$ |
| $a = 1$: $\sum\frac{(-1)^n}{n^p}$ | Converges absolutely for $p > 1$; conditionally for $0 < p \le 1$ | $p$-series; Leibniz test |
| $a = -1$: $\sum\frac{1}{n^p}$ | Converges (absolutely) for $p > 1$; diverges for $0 < p \le 1$ | $p$-series |

### 8.3.3. Properties of Absolutely Convergent Series

Finite sums can be reordered, regrouped and multiplied out freely. For infinite sums, absolute convergence is exactly the condition that makes these operations legitimate.

**Property 8.3.1** If $\sum u_n$ and $\sum v_n$ both converge absolutely, then so does $\sum(au_n + bv_n)$.

**Proof** $|au_n + bv_n| \le |a||u_n| + |b||v_n|$; apply the comparison test. $\square$

**Property 8.3.2 (Commutativity)** If $\sum u_n$ converges absolutely, then every series $\sum v_n$ obtained by reordering its terms ($v_n = u_{i_n}$, where $n \mapsto i_n$ is a **bijection** of the positive integers) also converges absolutely, and to the same sum.

**Proof** 1. First let $u_n \ge 0$. With $m = \max\{i_1, \dots, i_n\}$ we have $\sum_{k=1}^n v_k \le S_m \le \sum_{k=1}^\infty u_k$, so $\sum v_n$ converges and $\sum v_n \le \sum u_n$; conversely, $\sum u_n$ is a rearrangement of $\sum v_n$, so $\sum u_n \le \sum v_n$.

2. In general, let $p_n = \frac{|u_n| + u_n}{2}$ and $q_n = \frac{|u_n| - u_n}{2}$. Then $u_n = p_n - q_n$ and $0 \le p_n, q_n \le |u_n|$, so $\sum p_n$ and $\sum q_n$ both converge. The positive and negative parts of $\sum v_n$ are rearrangements of $\sum p_n$ and $\sum q_n$ respectively, so by 1, $\sum v_n = \sum p_{i_n} - \sum q_{i_n} = \sum p_n - \sum q_n = \sum u_n$. $\square$

Conditionally convergent series are not commutative. The alternating harmonic series $1 - \frac12 + \frac13 - \frac14 + \cdots = \ln2$ converges conditionally; rearrange it as "one positive term, then two negative terms":

$$
\left(1 - \frac12\right) - \frac14 + \left(\frac13 - \frac16\right) - \frac18 + \cdots + \left(\frac{1}{2k-1} - \frac{1}{2(2k-1)}\right) - \frac{1}{4k} + \cdots = \frac12\left(1 - \frac12 + \frac13 - \frac14 + \cdots\right) = \frac12\ln2.
$$

![Partial sums of the harmonic series, of 1/n^2, and of the alternating harmonic series (left); the rearranged alternating harmonic series converges to half of the original sum (right)](./plots/partial-sums.py)

In fact, a conditionally convergent series can be rearranged to produce any result whatsoever.

**Theorem 8.3.4 (Riemann Rearrangement Theorem)** If $\sum u_n$ converges conditionally, then for every $S \in [-\infty, +\infty]$ there is a rearrangement of $\sum u_n$ with sum $S$; there is also a rearrangement whose partial sums oscillate without converging.

Idea of the proof: for a conditionally convergent series, the sum of the positive terms and the sum of the negative terms both diverge to infinity (otherwise $\sum|u_n|$ would converge or $\sum u_n$ would diverge), while $u_n \to 0$. So take positive terms until the partial sum exceeds $S$, then negative terms until it falls below $S$, and so on. The partial sums swing around $S$ by no more than the last term taken, which tends to zero.

Absolutely convergent series can also be multiplied like polynomials. Expanding $\left(\sum_{n=0}^\infty u_n\right)\left(\sum_{n=0}^\infty v_n\right)$ produces all the products $u_iv_j$; grouping them by $i + j$ gives:

**Definition 8.3.3 (Cauchy Product)** The Cauchy product of the series $\sum_{n=0}^\infty u_n$ and $\sum_{n=0}^\infty v_n$ is $\sum_{n=0}^\infty c_n$, where $c_n = \sum_{k=0}^n u_kv_{n-k} = u_0v_n + u_1v_{n-1} + \cdots + u_nv_0$.

**Property 8.3.3** If $\sum u_n = U$ and $\sum v_n = V$ both converge absolutely, then their Cauchy product $\sum c_n$ also converges absolutely, and $\sum c_n = UV$.

The product of two power series ([Chapter 9](/2.2.9)) is a Cauchy product: $\sum a_nx^n\cdot\sum b_nx^n = \sum\left(\sum_{k=0}^n a_kb_{n-k}\right)x^n$. The hypothesis of absolute convergence cannot simply be dropped: $\sum_{n=0}^\infty\frac{(-1)^n}{\sqrt{n+1}}$ converges conditionally, but its Cauchy product with itself satisfies $|c_n| = \sum_{k=0}^n\frac{1}{\sqrt{(k+1)(n-k+1)}} \ge \sum_{k=0}^n\frac{2}{n+2} = \frac{2(n+1)}{n+2}$ (by the **inequality of arithmetic and geometric means**), so its general term does not tend to zero and it diverges.

**Example 8.3.4** Prove that $\left(\sum_{n=0}^\infty\frac{1}{n!}\right)\left(\sum_{n=0}^\infty\frac{(-1)^n}{n!}\right) = 1$.

**Proof** Both series converge absolutely (ratio test). The general term of the Cauchy product is $c_0 = 1$ and, for $n \ge 1$,

$$
c_n = \sum_{k=0}^n\frac{1}{k!}\cdot\frac{(-1)^{n-k}}{(n-k)!} = \frac{1}{n!}\sum_{k=0}^n\binom nk(-1)^{n-k} = \frac{(1-1)^n}{n!} = 0.
$$

Hence the product is $1$; that is, $\mathrm{e}\cdot\mathrm{e}^{-1} = 1$. $\square$

**Example 8.3.5** Compute $I = \sum_{n=0}^\infty\frac{1}{2^n}\cos\frac{2n\pi}{3}$.

**Solution** The series converges absolutely, so we may split it into three groups according to the residue of $n$ modulo $3$ and sum each group separately:

$$
I = \sum_{k=0}^\infty\frac{1}{8^k}\left(1 + \frac12\cos\frac{2\pi}{3} + \frac14\cos\frac{4\pi}{3}\right) = \frac87\left(1 - \frac14 - \frac18\right) = \frac57.
$$

### 8.3.4. Abel's Test and Dirichlet's Test

For a series of the form $\sum a_nb_n$ in which $\{a_n\}$ is monotone and the partial sums of $\sum b_n$ are under control, "summation by parts" turns it into an absolutely convergent series; this is the discrete analogue of integration by parts.

**Lemma 8.3.1 (Abel Transformation)** Let $B_k = b_1 + \cdots + b_k$ and $B_0 = 0$. Then

$$
\sum_{k=1}^n a_kb_k = a_nB_n - \sum_{k=1}^{n-1}(a_{k+1} - a_k)B_k.
$$

If $\{a_k\}$ is monotone and $|B_k| \le M$ ($1 \le k \le n$), then $\left|\sum_{k=1}^n a_kb_k\right| \le M(|a_1| + 2|a_n|)$.

**Proof** Substituting $b_k = B_k - B_{k-1}$ into the left-hand side and regrouping gives the identity. If $a_k$ is monotone, the differences $a_{k+1} - a_k$ do not change sign, so $\sum_{k=1}^{n-1}|a_{k+1} - a_k| = |a_n - a_1|$, and the left-hand side is at most $M|a_n| + M|a_n - a_1| \le M(|a_1| + 2|a_n|)$. $\square$

**Theorem 8.3.5 (Abel's Test)** If the sequence $\{a_n\}$ is monotone and bounded and $\sum b_n$ converges, then $\sum a_nb_n$ converges.

**Theorem 8.3.6 (Dirichlet's Test)** If the sequence $\{a_n\}$ is monotone with $\lim_{n\to\infty}a_n = 0$ and the partial sums of $\sum b_n$ are bounded, then $\sum a_nb_n$ converges.

**Proof** Apply Lemma 8.3.1 to the block $\sum_{k=m+1}^{m+p}a_kb_k$ (with partial sums counted from $k = m+1$) and verify the Cauchy criterion.

- Dirichlet: let $|B_n| \le M$. Then $|b_{m+1} + \cdots + b_{m+j}| \le 2M$, and the block is at most $2M(|a_{m+1}| + 2|a_{m+p}|) \le 6M|a_{m+1}| \to 0$ (since $|a_n|$ decreases to $0$).
- Abel: let $|a_n| \le K$. Given $\varepsilon > 0$, for $m$ large enough we have $|b_{m+1} + \cdots + b_{m+j}| < \varepsilon$ for all $j$, and the block is at most $3K\varepsilon$. $\square$

The Leibniz test is a special case of Dirichlet's test ($b_n = (-1)^{n-1}$, whose partial sums are $0$ or $1$). Dirichlet's test requires the partial sums of $\sum b_n$ to be bounded, not $\sum b_n$ to converge; the statement "$\{a_n\}$ decreases monotonically to zero and $\sum b_n$ converges" is merely a special case of Abel's test.

**Example 8.3.6** For every $x$, the series $\sum_{n=1}^\infty\frac{\sin nx}{n}$ converges. For $x = 2k\pi$ all terms vanish. Otherwise $\sin\frac x2 \ne 0$, and by the product-to-sum formula,

$$
\sum_{k=1}^n\sin kx = \frac{\cos\frac x2 - \cos\left(n + \frac12\right)x}{2\sin\frac x2}, \qquad \left|\sum_{k=1}^n\sin kx\right| \le \frac{1}{\left|\sin\frac x2\right|},
$$
so the partial sums are bounded, while $\frac1n$ decreases monotonically to zero; by Dirichlet's test the series converges. For $x \ne k\pi$ the convergence is conditional: $|\sin nx| \ge \sin^2nx = \frac12(1 - \cos2nx)$, where $\sum\frac1{2n}$ diverges and $\sum\frac{\cos2nx}{2n}$ converges (by the same argument). This series is a typical example of the Fourier series of [Chapter 9](/2.2.9).

**Example 8.3.7** The series $\sum\frac{(-1)^n}{n}\left(1 + \frac1n\right)^n$ converges: $\sum\frac{(-1)^n}{n}$ converges, and $\left(1 + \frac1n\right)^n$ is increasing and bounded (it tends to $\mathrm{e}$), so Abel's test applies.

Putting the methods of this chapter together gives a general procedure for testing convergence.

**Algorithm 8.3.1 (Testing a Series for Convergence)**

1. Look at the general term: if $u_n \not\to 0$, the series diverges.
2. For a series of nonnegative terms (or for $\sum|u_n|$): find the principal part of the general term with Taylor's formula or equivalent infinitesimals and compare with a $p$-series or a geometric series; for terms containing $n!$ or $a^n$, use the ratio test; for terms containing $n$-th powers, use the root test; for terms of the form $f(n)$ with $f$ monotone and easy to integrate, use the integral test.
3. If $\sum|u_n|$ converges, the series converges absolutely; otherwise apply the Leibniz, Dirichlet or Abel test to the series itself, and if it converges, the convergence is conditional.
4. If necessary, study the partial sums directly (telescoping, known sums of series).

## Summary

| Test | Applies to | Hypotheses and conclusion | Fails when |
|---|---|---|---|
| Comparison test | Nonnegative terms | $u_n \le Mv_n$: $\sum v_n$ converges $\Rightarrow$ $\sum u_n$ converges | No suitable $v_n$ can be found |
| Limit form | Nonnegative terms | $u_n/v_n \to q \in (0, +\infty)$: same behavior | — |
| $p$-test | Nonnegative terms | $n^pu_n$ has a limit, $p > 1$: converges; nonzero limit, $p \le 1$: diverges | Terms like $\frac{1}{n\ln n}$ |
| Ratio test | Nonnegative terms | $u_{n+1}/u_n \to q$: converges if $q < 1$, diverges if $q > 1$ | $q = 1$ |
| Root test | Nonnegative terms | $\sqrt[n]{u_n} \to q$: converges if $q < 1$, diverges if $q > 1$ | $q = 1$ |
| Integral test | $u_n = f(n)$, $f$ nonnegative and decreasing | Same behavior as $\int_1^{+\infty}f$ | $f$ not monotone |
| Leibniz test | Alternating series | $u_n$ decreases to $0$: converges, $\lvert r_n\rvert \le u_{n+1}$ | $u_n$ not monotone |
| Dirichlet's test | $\sum a_nb_n$ | $a_n$ monotone and tends to $0$, partial sums of $\sum b_n$ bounded | — |
| Abel's test | $\sum a_nb_n$ | $a_n$ monotone and bounded, $\sum b_n$ converges | — |

| Standard series | Condition for convergence |
|---|---|
| Geometric series $\sum aq^{n-1}$ | $\lvert q\rvert < 1$, with sum $\frac{a}{1-q}$ |
| $p$-series $\sum\frac{1}{n^p}$ | $p > 1$ |
| Bertrand series $\sum\frac{1}{n(\ln n)^p}$ | $p > 1$ |
| $\sum\frac{(-1)^n}{n^p}$ | Absolutely for $p > 1$, conditionally for $0 < p \le 1$ |

| Operation | Convergent series | Absolutely convergent series |
|---|---|---|
| Linear combination | Allowed | Allowed |
| Inserting parentheses | Allowed (removing them is not) | Allowed |
| Reordering | Not allowed (Riemann rearrangement theorem) | Allowed; the sum is unchanged |
| Cauchy product | Need not converge | Converges to the product |
