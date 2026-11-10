---
title: The Binomial Test, the Sign Test and the Wilcoxon Signed-Rank Test
description: The exact binomial test, its one- and two-sided p-values and the competing definitions of a two-sided p-value, discreteness and conservatism, comparison with the z-test, the accuracy of the normal approximation and the continuity correction; tests derived from the binomial test; the median of continuous and discrete distributions; the sign test and its assumptions; the Wilcoxon signed-rank test, the role of symmetry, its exact null distribution, the normal approximation with continuity correction, ties, midranks and the variance correction, zeros, why jittering is not a remedy, and paired data.
---

The simplest nonparametric procedures reduce the data to counts. If each observation either has or does not have some property, and the null hypothesis fixes the probability of the property, the number of observations that have it follows a binomial distribution, and the test based on that count is exact for every sample size. This binomial test is the engine of a whole family of distribution-free tests: the sign test for a median, McNemar's test for before-and-after studies and the Cox–Stuart test for trend are all binomial tests in disguise. The first half of this chapter develops the binomial test itself, including some subtleties of discrete tests that recur throughout the course: how to define a two-sided $p$-value, why discrete tests are conservative and when the normal approximation can be trusted.

The second half turns to the oldest problem of nonparametric statistics, inference about the location of a single population or about the difference within pairs. The sign test uses only the signs of the deviations from a hypothesized median and needs almost no assumptions. The Wilcoxon signed-rank test also uses the ranks of their magnitudes; it is usually much more powerful, at the price of a symmetry assumption. Both were introduced in [3.2.6](/3.2.6) with their large-sample forms; here we concentrate on what that chapter did not cover: the assumptions in detail, exact null distributions, the continuity correction, and ties. Confidence intervals and point estimates derived from these tests, and their efficiency, follow in [3.6.4](/3.6.4) and [3.6.5](/3.6.5).

## 3.1. The Binomial Test

### 3.1.1. The Test and Its p-Values

As its name indicates, a binomial test examines whether a population proportion equals a specified value. Suppose we wish to know whether half of the college seniors are eligible for graduate recommendation. A simple random sample of $10$ seniors is asked, and only $3$ say yes. Does the sample proportion $0.3$ mean that the population proportion is not $0.5$, or is $3$ out of $10$ a plausible result if $50\%$ are actually eligible?

**Definition 3.1.1 (Binomial Test)** Let $X$ be the number of successes in $n$ independent trials, each with the same success probability $p$. The **binomial test** of $H_0\colon p = p_0$ uses $X$ itself, whose null distribution is $\mathrm{Bin}(n, p_0)$. For the observed value $x$, the exact one-sided $p$-values are

$$
\mathbb{P}_{p_0}(X \ge x)\quad\text{against } H_1\colon p > p_0,\qquad \mathbb{P}_{p_0}(X \le x)\quad\text{against } H_1\colon p < p_0.
$$

The model has two key assumptions: the $n$ trials (individuals, pairs, items) are mutually independent, and the probability of the outcome is the same for all of them. In R:

```r
binom.test(x = 3, n = 10, p = 0.5)   # alternative = "two.sided" by default
```

```text
	Exact binomial test

data:  3 and 10
number of successes = 3, number of trials = 10, p-value = 0.3438
alternative hypothesis: true probability of success is not equal to 0.5
95 percent confidence interval:
 0.06673951 0.65245285
sample estimates:
probability of success 
                   0.3 
```

The two-sided $p$-value is $0.3438 = 2\,\mathbb{P}(X \le 3)$, so $3$ out of $10$ is entirely plausible when $p = 0.5$. The confidence interval reported is the exact Clopper–Pearson interval, discussed with other intervals for a proportion in [3.6.5](/3.6.5). The function's arguments are `x` (the number of successes), `n` (the number of trials), `p` (the hypothesized probability of success), `alternative` (`"two.sided"`, `"less"` or `"greater"`) and `conf.level`.

### 3.1.2. Two-Sided p-Values

When $p_0 = 1/2$ the binomial distribution is symmetric and the two-sided $p$-value is unambiguous. Otherwise it is skewed, and "results at least as extreme as the observed one in either direction" can be defined in more than one way. Is doubling a one-tailed probability the correct way? There are three common methods:

1. *Doubling*: $\min\bigl\{1,\ 2\min\{\mathbb{P}(X \le x), \mathbb{P}(X \ge x)\}\bigr\}$.
2. *Equal distance from the mean*: add the probabilities of all outcomes at least as far from $np_0$ as $x$, that is, $\mathbb{P}\bigl(\lvert X - np_0\rvert \ge \lvert x - np_0\rvert\bigr)$.
3. *Probabilities not exceeding that of the observed value*: add $\mathbb{P}(X = k)$ over all $k$ with $\mathbb{P}(X = k) \le \mathbb{P}(X = x)$. This orders the outcomes by their null probability, as a likelihood ratio test would, and is the method used by `binom.test` (with a small relative tolerance for numerical ties).

All three give valid $p$-values, since each is $\mathbb{P}_{H_0}(T \ge t_{\mathrm{obs}})$ for some ordering $T$ of the outcomes, and all coincide when $p_0 = 1/2$. Otherwise none is uniformly smaller than the others, as the case $n = 10$, $p_0 = 0.75$ shows:

| $x$ | $4$ | $5$ | $6$ | $10$ |
|---|---|---|---|---|
| Doubling | $0.0395$ | $0.156$ | $0.448$ | $0.113$ |
| Equal distance from the mean | $0.0197$ | $0.134$ | $0.468$ | $0.134$ |
| Probabilities $\le \mathbb{P}(X = x)$ | $0.0197$ | $0.134$ | $0.280$ | $0.076$ |

A method that tends to give smaller $p$-values rejects more often and therefore has more power, with the same guarantee of validity; the third method is usually the least conservative of the three, which is one reason it is the default in R. Whichever method is used should be chosen before the data are seen.

### 3.1.3. Discreteness

Discrete $p$-values pose a problem: a test may never be able to reject $H_0$. For $n = 10$ and $p_0 = 0.75$ the null probabilities, rounded, are

```r
round(dbinom(0:10, size = 10, prob = 0.75), digits = 2)
```

```text
 [1] 0.00 0.00 0.00 0.00 0.02 0.06 0.15 0.25 0.28 0.19 0.06
```

The most extreme outcome above the mean, $x = 10$, already has probability $0.056$, so no outcome above the mean is significant at the two-sided $5\%$ level, whichever method is used: the test cannot detect $p > 0.75$ at all with ten trials. More generally, the attainable significance levels are the tail probabilities of the binomial distribution, and the test with nominal level $\alpha$ uses the largest attainable level not exceeding $\alpha$. It is a conservative test: its actual type I error rate is smaller than the nominal level (Definition 1.5.1). With $n = 10$ and $p_0 = 0.5$, for example, the two-sided rejection region $\{0, 1, 9, 10\}$ has actual level $0.021$, and adding $2$ and $8$ would give $0.109$; a nominal level of exactly $5\%$ can be achieved only by a **randomized test** (see [3.6.4](/3.6.4)).

Is the binomial test a parametric test, and is it exact? It is exact in the sense of Definition 1.3.1: it uses the exact null distribution, and its type I error never exceeds the nominal level, whatever $n$. Whether it is parametric depends on the use. Formally the binomial family is a one-parameter family and the hypothesis concerns that parameter, so the test is parametric; but the binomial distribution usually arises not as an assumption about the shape of a population but from counting how many observations fall into a category, and in that role (the sign test below, the quantile tests of [3.6.7](/3.6.7)) the binomial test is a distribution-free procedure for a nonparametric hypothesis.

### 3.1.4. Comparison with the z-Test

For large $n$, the **Z-test** for one proportion, based on

$$
Z = \frac{X - np_0}{\sqrt{np_0(1 - p_0)}} \overset{\cdot}{\sim} \mathcal{N}(0, 1),
$$
gives $p$-values almost identical to those of the binomial test, by the de Moivre–Laplace theorem. The $z$-test has traditionally been preferred: it is computationally lighter, especially for large samples; it comes with a simple confidence interval for the proportion; and its power has a closed-form approximation. These advantages have largely disappeared. Exact binomial probabilities are computed instantly, exact intervals exist, and the power of the binomial test is an exact finite sum, $\sum_{k\in C}\binom nk p^k(1 - p)^{n-k}$ over the rejection region $C$; for $n = 10$, $C = \{0, 1, 9, 10\}$ and $p = 0.2$ it equals $0.376$.

The difficulty with the $z$-test is that the normal approximation can be poor. A common rule of thumb is that it is adequate when

$$
np_0 \ge 5\quad\text{and}\quad n(1 - p_0) \ge 5.
$$
The approximation is improved by the **continuity correction**, which accounts for the fact that a continuous distribution is approximating a discrete one: each integer value $k$ is represented by the interval $(k - \frac12, k + \frac12)$. Thus, for an integer-valued $X$ and a normal approximation $Y$,

$$
\begin{aligned}
\mathbb{P}(X = k) &\approx \mathbb{P}(k - 0.5 < Y < k + 0.5), & \mathbb{P}(X \le k) &\approx \mathbb{P}(Y < k + 0.5), & \mathbb{P}(X < k) &\approx \mathbb{P}(Y < k - 0.5),\\
\mathbb{P}(X > k) &\approx \mathbb{P}(Y > k + 0.5), & \mathbb{P}(X \ge k) &\approx \mathbb{P}(Y > k - 0.5). & &
\end{aligned}
$$
The correction always moves the boundary half a unit towards the center of the distribution. For $p = 0.2$, the errors of the corrected approximation to the point probabilities $\mathbb{P}(X = k)$, averaged over $k = 0, \dots, n$ and at their largest, are

| $np$ | $n$ | mean absolute error | maximum absolute error |
|---|---|---|---|
| $3$ | $15$ | $0.00556$ | $0.02392$ |
| $4$ | $20$ | $0.00373$ | $0.01717$ |
| $5$ | $25$ | $0.00287$ | $0.01479$ |
| $6$ | $30$ | $0.00219$ | $0.01266$ |
| $7$ | $35$ | $0.00175$ | $0.01090$ |

The error falls only slowly as $np$ grows. The figure shows why the rule of thumb is a rough guide: what matters is the skewness of the binomial distribution, $(1 - 2p)/\sqrt{np(1-p)}$, so at the same $np$ the approximation is much better for $p = 0.5$ than for $p = 0.05$. In small samples, and for $p_0$ near $0$ or $1$, the exact test should be used.

![Left: the Bin(20, 0.2) distribution with its continuity-corrected normal approximation; the binomial distribution is visibly skewed. Right: the largest error of the continuity-corrected normal approximation to the binomial distribution function, against np, for p = 0.5, 0.2 and 0.05.](./plots/binomial-normal-error.py)

## 3.2. Tests Derived from the Binomial Test

People sometimes split continuous data into categories precisely so that they can use exact binomial results. The resulting tests need only the two assumptions of Definition 3.1.1, applied to the derived binary outcomes.

- The **sign test** for a median (§3.4) allocates a sign, $+$ or $-$, to each observation according to whether it lies above or below the hypothesized median, and drops observations equal to it. It is the binomial test with $p_0 = 1/2$.
- **McNemar's test** for before-and-after studies with a binary response uses only the pairs that changed, and tests whether changes in the two directions are equally likely ([3.6.8](/3.6.8)).
- The **Cox–Stuart test** for a monotonic trend pairs each observation in the first half of a series with one in the second half and applies the sign test to the differences ([3.6.7](/3.6.7)).

The binomial distribution with unequal success and failure probabilities appears in tests for quantiles other than the median ([3.6.7](/3.6.7)).

## 3.3. Inference About the Median

### 3.3.1. The Median of a Distribution

For data $x_1, \dots, x_n$ the sample median is $x_{((n+1)/2)}$ if $n$ is odd and $\frac12\bigl(x_{(n/2)} + x_{(n/2+1)}\bigr)$ if $n$ is even ([3.6.2](/3.6.2)). For a continuous random variable $X$ with density $f$ and distribution function $F$, a median $\theta$ satisfies

$$
\int_{-\infty}^\theta f(x)\,\mathrm{d}x = F(\theta) = \frac12;
$$
if $F$ is strictly increasing near $\theta$, then $\theta = F^{-1}(0.5)$ is the unique $50$th percentile, and $X$ lies below $\theta$ half of the time and above it half of the time. For a discrete distribution, "the middle value" with equal chances of $X$ being greater or less may not exist, and the definition must allow for the atoms.

**Definition 3.3.1 (Median)** A **median** of a random variable $X$ is any real number $M$ such that

$$
\mathbb{P}(X \le M) \ge \frac12\quad\text{and}\quad \mathbb{P}(X \ge M) \ge \frac12.
$$

The set of medians is a nonempty closed interval, often a single point. For

| $x$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|
| $\mathbb{P}(X = x)$ | $0.2$ | $0.2$ | $0.4$ | $0.2$ |

$\mathbb{P}(X \le 3) = 0.8$ and $\mathbb{P}(X \ge 3) = 0.6$, while $\mathbb{P}(X \le M) \le 0.4$ for $M < 3$ and $\mathbb{P}(X \ge M) \le 0.2$ for $M > 3$, so the median is $3$, although $X$ equals $3$ with probability $0.4$ and is not "equally likely" to be above or below it. If instead the probabilities are $0.2, 0.3, 0.2, 0.3$, then every $M \in [2, 3]$ satisfies both inequalities ($\mathbb{P}(X \le 2) = 0.5$, $\mathbb{P}(X \ge 3) = 0.5$), and the median is the whole interval $[2, 3]$. The quantile function of [3.1.7](/3.1.7) picks the left end, $F^{-1}(0.5) = 2$, and other conventions use the midpoint $2.5$.

The median is a natural measure of location for nonparametric inference: it always exists, it is not affected by the tails, and it remains meaningful for skewed data. For a symmetric distribution whose mean exists, the mean and the median coincide, so a test for the median is then also a test for the mean.

### 3.3.2. The Problem

Let $X_1, \dots, X_n$ be a random sample from a continuous distribution with unknown median $\theta$. We wish to test

$$
H_0\colon \theta = \theta_0
$$
against a one- or two-sided alternative. Paired data reduce to this problem by taking differences.

**Example 3.3.1 (Two Analgesics)** The table shows the hours of relief provided by two analgesic drugs in $12$ patients suffering from arthritis. Is there any evidence that one drug provides longer relief than the other?

| Case | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Drug A | 2.0 | 3.6 | 2.6 | 2.6 | 7.3 | 3.4 | 14.9 | 6.6 | 2.3 | 2.0 | 6.8 | 8.5 |
| Drug B | 3.5 | 5.7 | 2.9 | 2.4 | 9.9 | 3.3 | 16.7 | 6.0 | 3.8 | 4.0 | 9.1 | 20.9 |

Each patient received both drugs, so the comparison is essentially a one-sample inference on the differences $B - A$:

$$
+1.5,\ +2.1,\ +0.3,\ -0.2,\ +2.6,\ -0.1,\ +1.8,\ -0.6,\ +1.5,\ +2.0,\ +2.3,\ +12.4,
$$
with sample median $\frac12(1.5 + 1.8) = 1.65$ hours. We test $H_0$: the median difference is $\theta_0 = 0$. The value $+12.4$ is far from the others; a $t$-test would be heavily influenced by it.

## 3.4. The Sign Test

**Definition 3.4.1 (Sign Test)** Let $X_1, \dots, X_n$ be independent with a continuous distribution and common median $\theta$. Allocate to each observation the sign $+$ or $-$ according to whether it is greater or less than $\theta_0$, and let $N_+$ and $N_-$ be the numbers of plus and minus signs. Under $H_0\colon\theta = \theta_0$, each $X_i$ exceeds $\theta_0$ with probability $\frac12$, so $N_+ \sim \mathrm{Bin}(n, \frac12)$, and the **sign test** is the binomial test of $p = \frac12$ applied to $N_+$.

($N_+$ is the statistic $n_+$ of [3.2.6](/3.2.6).) The test rests on an equivalence: for a continuous distribution,

$$
\theta = \theta_0 \iff \mathbb{P}(X > \theta_0) = \mathbb{P}(X < \theta_0) = \frac12.
$$
A test of "the proportion of observations above $\theta_0$ is one half" is therefore a test of the median. The sign test requires only independence and a common median: the observations need not be identically distributed, and no symmetry or other shape assumption is needed. That answers a question students often ask: the sign test does not require a symmetric distribution.

**Example 3.4.1** For the analgesic differences, $9$ signs are positive and $3$ negative. Is this set of signs substantially different from what we would expect by chance?

```r
binom.test(9, 12)
```

```text
	Exact binomial test

data:  9 and 12
number of successes = 9, number of trials = 12, p-value = 0.146
alternative hypothesis: true probability of success is not equal to 0.5
95 percent confidence interval:
 0.4281415 0.9451394
sample estimates:
probability of success 
                  0.75 
```

The two-sided $p$-value is $2\,\mathbb{P}(N_+ \ge 9) = 2 \cdot 299/4096 = 0.146$: the sign test finds no significant difference between the drugs.

Observations equal to $\theta_0$ (zeros, for differences) carry no sign. The usual practice is to drop them and apply the test to the remaining $n$ observations, which gives a test conditional on the number of nonzero values; with continuous data zeros arise only through rounding. Other treatments, and their consequences, are discussed in [3.6.5](/3.6.5). Ties among the nonzero observations, on the other hand, do not matter to the sign test at all.

The price of this generality is that the sign test uses very little of the information in the data: the difference $+12.4$ counts exactly as much as $+0.3$. This makes it robust, since no single observation can have more influence than one sign, but it also makes it less powerful than tests that use the sizes of the deviations.

## 3.5. The Wilcoxon Signed-Rank Test

### 3.5.1. Using the Magnitudes: the Role of Symmetry

A possible improvement is to take the magnitudes into account through the ranks of the absolute deviations $\lvert X_i - \theta_0\rvert$. For the analgesic data:

| Difference | $-0.1$ | $-0.2$ | $+0.3$ | $-0.6$ | $+1.5$ | $+1.5$ | $+1.8$ | $+2.0$ | $+2.1$ | $+2.3$ | $+2.6$ | $+12.4$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rank of $\lvert\text{difference}\rvert$ | $1$ | $2$ | $3$ | $4$ | $5.5$ | $5.5$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
| Signed rank | $-1$ | $-2$ | $+3$ | $-4$ | $+5.5$ | $+5.5$ | $+7$ | $+8$ | $+9$ | $+10$ | $+11$ | $+12$ |

The negative differences are all small: they occupy ranks $1$, $2$ and $4$. If $H_0$ were true, positive and negative signs would be expected to be distributed at random among the ranks.

For this reasoning to be valid we need to add an assumption: the distribution of $X_i - \theta_0$ is symmetric about zero under $H_0$, that is, $X_i - \theta_0 \overset{d}{=} \theta_0 - X_i$. A distribution symmetric about $\theta$ has median $\theta$, and if it has a mean, the mean is also $\theta$. Symmetry is what makes the sign of a deviation independent of its magnitude: given $\lvert X_i - \theta_0\rvert$, the sign is $+$ or $-$ with probability $\frac12$ each. Without symmetry the test is not a test of the median. Suppose, for instance, that the ranks $1$ to $6$ all carry minus signs and the ranks $7$ to $12$ all carry plus signs. The sign test sees six of each and finds perfect agreement with $\theta_0$ being the median; the signed ranks show that the observations below $\theta_0$ are all close to it and those above are all far from it. This pattern is what a right-skewed distribution with median $\theta_0$ produces, and also what a symmetric distribution with center above $\theta_0$ produces; the signed-rank test cannot tell the two apart and will tend to reject in both cases. What it actually tests is symmetry about $\theta_0$; its natural target, the center of symmetry or more generally the pseudomedian, is studied in [3.6.5](/3.6.5).

The advantage of the stronger assumption is power: the test uses both the direction of each deviation and, through the ranks, its size.

### 3.5.2. The Test Statistic

Let $R_i^+$ be the rank of $\lvert X_i - \theta_0\rvert$ among $\lvert X_1 - \theta_0\rvert, \dots, \lvert X_n - \theta_0\rvert$, and let $Z_i = \boldsymbol{1}\{X_i > \theta_0\}$.

**Definition 3.5.1 (Wilcoxon Signed-Rank Test)** The **Wilcoxon signed-rank test** of $H_0$: the distribution of the $X_i$ is symmetric about $\theta_0$, uses the positive and negative rank sums

$$
S_+ = \sum_{i=1}^nZ_iR_i^+ = \sum_{X_i > \theta_0}R_i^+,\qquad S_- = \sum_{i=1}^n(1 - Z_i)R_i^+ = \sum_{X_i < \theta_0}R_i^+.
$$

($S_+$ is the statistic $W^+$ of [3.2.6](/3.2.6).) Since $S_+ + S_- = 1 + 2 + \cdots + n = \frac{n(n+1)}{2}$, the statistics $S_+$, $S_-$ and $S_+ - S_- = 2S_+ - \frac{n(n+1)}{2}$ are equivalent: each is a monotone function of the others, and under $H_0$ the difference $S_+ - S_-$ is expected to be near zero. We may take $W = S_+$ or $W = S_-$; tables traditionally give lower tail probabilities, so the smaller of the two observed values is used. For the analgesic data,

$$
S_- = 1 + 2 + 4 = 7,\qquad S_+ = 3 + 5.5 + 5.5 + 7 + 8 + 9 + 10 + 11 + 12 = 71,
$$
and $W = S_- = 7$. Next we need its distribution.

### 3.5.3. The Exact Null Distribution

The support of $W$ is $\{0, 1, \dots, \frac{n(n+1)}{2}\}$. Under $H_0$, given the magnitudes, the $n$ signs are independent and each is $+$ with probability $\frac12$, so the signs are allocated to the ranks in $2^n$ equally likely ways (for $n = 12$, `2^12` $= 4096$ ways). Hence

$$
\mathbb{P}(W = w) = \frac{c_n(w)}{2^n},
$$
where $c_n(w)$ is the number of allocations with $S_+ = \sum_{Z_i = 1}R_i^+ = w$, the number of subsets of $\{1, \dots, n\}$ with sum $w$. For a small sample size the exact distribution gives exact $p$-values. Take $n = 3$: the eight subsets of $\{1, 2, 3\}$ have sums $0, 1, 2, 3, 3, 4, 5, 6$, so

| $w$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|
| $\mathbb{P}(W = w)$ | $1/8$ | $1/8$ | $1/8$ | $2/8$ | $1/8$ | $1/8$ | $1/8$ |

The calculation is tedious but elementary, and it can be organized by a recursion: a subset of $\{1, \dots, n\}$ either omits $n$ or contains it, so

$$
c_n(w) = c_{n-1}(w) + c_{n-1}(w - n),
$$
equivalently $\sum_wc_n(w)t^w = \prod_{k=1}^n(1 + t^k)$. The distribution is symmetric about $\frac{n(n+1)}{4}$, since replacing a subset by its complement maps $w$ to $\frac{n(n+1)}{2} - w$; that is why a test may be based on either $S_+$ or $S_-$. Tables of the distribution, going back to Wilcoxon (1945), and R's `psignrank` give it directly. For $n = 12$ and no ties, $\mathbb{P}(W \le 7) = \mathbb{P}(W \ge 71) = 19/4096 = 0.0046$, so the two-sided $p$-value is $0.0093$: strong evidence of a difference between the drugs. (The data contain a tie, and the exact distribution with tied ranks (§3.5.5) gives $\mathbb{P}(S_- \le 7) = 18/4096$ and a two-sided $p$-value of $0.0088$.)

The contrast with the sign test ($p = 0.146$) is striking. The three negative differences are among the four smallest in magnitude, which the sign test cannot see; and the large difference $+12.4$ contributes only the rank $12$, so the signed-rank test is not dominated by it as a $t$-test would be.

### 3.5.4. The Normal Approximation

Working with the exact distribution is limiting for larger $n$, although modern software handles it easily up to a few hundred observations.

**Theorem 3.5.1** Under $H_0$ (independent observations, continuous and symmetric about $\theta_0$),

$$
\mathbb{E}W = \frac{n(n+1)}{4},\qquad \operatorname{Var}(W) = \frac{n(n+1)(2n+1)}{24},
$$
and, as $n \to \infty$,

$$
W' = \frac{S_+ - n(n+1)/4}{\sqrt{n(n+1)(2n+1)/24}} \xrightarrow{d} \mathcal{N}(0, 1).
$$

**Proof** Under $H_0$ the signs are independent of the ranks and of each other, so $S_+$ has the distribution of $U = \sum_{i=1}^nU_i$, where $U_1, \dots, U_n$ are independent and $\mathbb{P}(U_i = i) = \mathbb{P}(U_i = 0) = \frac12$. Then

$$
\mathbb{E}U_i = \frac i2,\qquad \operatorname{Var}(U_i) = \frac{i^2}{2} - \Bigl(\frac i2\Bigr)^2 = \frac{i^2}{4},
$$
and summing, $\mathbb{E}U = \frac12\cdot\frac{n(n+1)}{2}$ and $\operatorname{Var}(U) = \frac14\cdot\frac{n(n+1)(2n+1)}{6}$. The $U_i$ are independent but not identically distributed; the **Lyapunov central limit theorem** applies because $\sum_i\mathbb{E}\lvert U_i - i/2\rvert^3 = \frac18\sum_ii^3 \sim \frac{n^4}{32}$ is of smaller order than $\operatorname{Var}(U)^{3/2} \sim (n^3/12)^{3/2}$. The same holds for $S_- = \frac{n(n+1)}{2} - S_+$. $\square$

For the analgesic data, $n = 12$, $W = 7$, $\mathbb{E}W = 39$ and $\operatorname{Var}(W) = 162.5$, so

$$
W' = \frac{7 - 39}{\sqrt{162.5}} = -2.51,
$$
and the two-sided $p$-value is $2\Phi(-2.51) = 0.012$. We reject the null hypothesis: there is sufficient evidence at the $5\%$ level that one drug provides longer relief than the other.

If we ask which drug provides longer relief, the test is one-sided. Against $H_1$: drug B provides more relief than drug A (the differences $B - A$ tend to be positive), small values of $S_-$ are significant, and the one-sided $p$-value is $\Phi(W') = 0.006$. Against $H_1$: drug A provides more relief, the $p$-value is $1 - \Phi(W') = 0.994$.

Since $W$ is integer-valued (without ties), the normal approximation is improved by the continuity correction of §3.1.4: $\mathbb{P}(W \le 7) = \mathbb{P}(W < 7.5) \approx \Phi\bigl((7.5 - 39)/\sqrt{162.5}\bigr)$. The figure below shows how closely the normal density follows the exact distribution already for $n = 12$, except in the extreme tails.

![Left: the exact null distribution of the signed-rank statistic for n = 12 (4096 equally likely sign patterns) with its normal approximation, and the observed value 7 for the analgesic data. Right: the exact null distribution of S- for the seven observations 1, 1, 5, 5, 8, 8, 8 tested at theta0 = 3, whose absolute deviations have tied ranks, compared with the distribution without ties.](./plots/signed-rank-null.py)

### 3.5.5. Ties

Two observations with $\lvert X_i - \theta_0\rvert = \lvert X_j - \theta_0\rvert$ cannot be ranked; with continuous data this happens with probability zero, but recorded data are rounded and ties are common.

**Definition 3.5.2 (Ties and Midranks)** Observations with equal values form a **tie**. If a group of $d$ tied values would occupy the positions $a + 1, \dots, a + d$ in the ordered sample, each of them is assigned the **midrank** $a + \frac{d+1}{2}$, the average of the ranks they would otherwise receive.

For example, the seven observations $1, 1, 5, 5, 8, 8, 8$ tested at $\theta_0 = 3$ give the deviations $-2, -2, 2, 2, 5, 5, 5$; the four absolute deviations equal to $2$ share the ranks $1$ to $4$ and the three equal to $5$ share $5$ to $7$, so the signed ranks are $-2.5, -2.5, 2.5, 2.5, 6, 6, 6$. In the analgesic data the two differences $+1.5$ share ranks $5$ and $6$ and both receive $5.5$.

Does using midranks change the distribution of $W$? Its mean is unchanged, since the midranks still add up to $\frac{n(n+1)}{2}$, but its variance decreases. The general statement treats each rank or midrank as a score.

**Theorem 3.5.2** Under $H_0$, let the absolute deviations receive scores $s_1, \dots, s_n$ (ranks or midranks), and let $S_+$ be the sum of the scores of the positive deviations. Conditionally on the scores,

$$
\mathbb{E}S_+ = \frac12\sum_{i=1}^ns_i,\qquad \operatorname{Var}(S_+) = \frac14\sum_{i=1}^ns_i^2.
$$
With midranks for $k$ groups of tied values of sizes $d_1, \dots, d_k$ (untied values being groups of size $d_j = 1$),

$$
\operatorname{Var}(S_+) = \frac{n(n+1)(2n+1)}{24} - \frac{1}{48}\sum_{j=1}^kd_j(d_j^2 - 1),
$$
so each group of $d$ tied values reduces the variance by $\frac{d^3 - d}{48}$.

**Proof** Given the scores, the signs are independent and fair under $H_0$, so $S_+ = \sum_is_iI_i$ with $I_i \overset{\text{iid}}{\sim} \mathrm{Ber}(\frac12)$, which gives the mean and variance. For the midranks, consider a group occupying ranks $a + 1, \dots, a + d$ with midrank $v = a + \frac{d+1}{2}$. Replacing the ranks by $v$ leaves their sum unchanged and reduces their sum of squares by

$$
\sum_{m=1}^d(a + m)^2 - dv^2 = \sum_{m=1}^d(a + m - v)^2 = \sum_{m=1}^d\Bigl(m - \frac{d+1}{2}\Bigr)^2 = \frac{d(d^2 - 1)}{12},
$$
the variance identity for the discrete uniform distribution on $d$ consecutive integers multiplied by $d$. Summing over the groups, $\sum_is_i^2 = \sum_{i=1}^ni^2 - \frac1{12}\sum_jd_j(d_j^2 - 1)$, and dividing by four gives the formula. $\square$

For the analgesic data there is one group of $2$ tied ranks, so the variance is reduced by $2(4 - 1)/48 = 0.125$. With the continuity correction,

$$
z = \frac{7 + 0.5 - 12\cdot13/4}{\sqrt{12\cdot13\cdot25/24 - 0.125}} = -2.472,
$$
which gives a two-sided $p$-value of $0.0134$ (computing from $S_+$ instead, $\mathbb{P}(W \ge 71) = \mathbb{P}(W > 70.5)$ gives $z = (71 - 0.5 - 39)/12.74 = +2.472$, the same). There is strong evidence that drug B provides more relief than drug A. R reports exactly this:

```r
A <- c(2.0, 3.6, 2.6, 2.6, 7.3, 3.4, 14.9, 6.6, 2.3, 2.0, 6.8, 8.5)
B <- c(3.5, 5.7, 2.9, 2.4, 9.9, 3.3, 16.7, 6.0, 3.8, 4.0, 9.1, 20.9)
wilcox.test(A, B, paired = TRUE, alternative = "two.sided")
```

```text
	Wilcoxon signed rank test with continuity correction

data:  A and B
V = 7, p-value = 0.01344
alternative hypothesis: true location shift is not equal to 0

Warning message:
In wilcox.test.default(A, B, paired = TRUE, alternative = "two.sided") :
  cannot compute exact p-value with ties
```

Here `V` is the sum of the positive ranks of `A - B`, which is $S_-$ for $B - A$. The warning means that R's exact algorithm assumes untied ranks, so with ties it falls back on the normal approximation with the corrected variance.

In practice there are three ways to deal with ties.

- *Ignore the problem.* The change that ties cause in the distribution of $W$ is usually not great, and using the untied tables or the uncorrected variance gives a slightly conservative test.
- *Use the exact conditional distribution of the scores.* With the midranks as fixed scores, the $2^n$ sign allocations are still equally likely, and the exact distribution can be computed by enumeration or by a permutation algorithm. For $1, 1, 5, 5, 8, 8, 8$ and $\theta_0 = 3$, $W = S_- = 5$ and $\mathbb{P}(S_- \le 5) = 11/128 = 0.086$ with the tied scores, against $10/128 = 0.078$ from the untied distribution. In each case the distribution of $S_-$ is symmetric, which is why the test may be based on either $S_+$ or $S_-$; but with ties it is heavily multimodal, takes unevenly spaced and not necessarily integer values, and has more marked discontinuities, whereas without ties it is unimodal with integer values in unit steps (right panel of the figure).
- *Use the normal approximation with the variance correction* of Theorem 3.5.2, as R does.

If the issue of ties really bothers us, why not add a little random noise to break them? The seven observations $1, 1, 5, 5, 8, 8, 8$ might become $0.9, 1.1, 5.2, 5.3, 7.9, 8.0, 8.1$, or equally $0.9, 1.0, 4.8, 4.9, 7.9, 8.0, 8.1$. The signed deviations from $3$ are then $-2.1, -1.9, 2.2, 2.3, 4.9, 5.0, 5.1$ with signed ranks $-2, -1, 3, 4, 5, 6, 7$, or $-2.1, -2.0, 1.8, 1.9, 4.9, 5.0, 5.1$ with signed ranks $-4, -3, 1, 2, 5, 6, 7$. There are now no ties, but $S_- = 3$ in the first case and $S_- = 7$ in the second, with

$$
\mathbb{P}(S_- \le 3) = \frac{5}{128} = 0.039,\qquad \mathbb{P}(S_- \le 7) = \frac{19}{128} = 0.148.
$$
The conclusion at the $5\%$ level depends on the arbitrary noise. Jittering invents an ordering that the data do not contain, makes the analysis irreproducible, and can be steered towards a desired conclusion; it is not a legitimate remedy. Ties are information about the data and should be handled by midranks.

Zeros, observations with $X_i = \theta_0$, are a separate issue. The usual approach, due to Wilcoxon, discards them and reduces $n$ accordingly, as for the sign test. An alternative due to Pratt (1959) ranks the absolute deviations including the zeros and then drops the zeros' ranks from both sums, so that the remaining ranks reflect the positions of the nonzero values among all of them. The two methods can give different results when there are many zeros.

### 3.5.6. Paired Data

For paired observations $(A_i, B_i)$, the test is applied to the differences $D_i = B_i - A_i$, and the null hypothesis that the median difference is zero; the alternative is that the median of $B - A$ is not zero (two-sided) or that it is positive or negative (one-sided), according to the question asked. The symmetry assumption is then about the differences. It holds automatically under the natural null hypothesis of a paired experiment, that the two treatments are interchangeable for every pair: if $(A_i, B_i) \overset{d}{=} (B_i, A_i)$, which is exchangeability within the pair (Definition 1.4.1), then $D_i \overset{d}{=} -D_i$ is symmetric about zero. In a randomized crossover or before-and-after experiment this is the same argument as the paired permutation test of Remark 1.2.1, with ranks in place of the differences. Equal marginal distributions of $A$ and $B$ alone are not enough: dependence within the pair can make $B - A$ asymmetric even when $A$ and $B$ have the same distribution.

The one-sample and paired problems are thus unified. In either case the Wilcoxon signed-rank test can be used in place of a one-sample $t$-test or a **paired t-test** when normality is doubtful, provided that the differences can be meaningfully ranked by magnitude. For ordinal responses where only the direction of a change is meaningful, the sign test is the appropriate choice.

| | Sign test | Wilcoxon signed-rank test |
|---|---|---|
| Information used | signs of the deviations | signs and ranks of the magnitudes |
| Assumptions | independence, common median, continuity | independence, symmetry about $\theta_0$, continuity |
| What is tested | median $= \theta_0$ | center of symmetry $= \theta_0$ |
| Null distribution | $\mathrm{Bin}(n, \frac12)$ | sum of a random subset of the ranks; mean $\frac{n(n+1)}{4}$, variance $\frac{n(n+1)(2n+1)}{24}$ |
| Robustness | maximal: each observation contributes one sign | high: an outlier contributes only its rank |
| Power | lower | higher when symmetry holds |
| Analgesic data, two-sided $p$ | $0.146$ | $0.0134$ (normal approximation), $0.0088$ (exact) |

The difference in power is explained by information: the sign test uses only the location of each observation relative to $\theta_0$, while the signed-rank test also uses how far away it is, through its rank. How large the gain is, and how it depends on the population, is quantified by the asymptotic relative efficiency in [3.6.4](/3.6.4).

## Summary

- Binomial test (Definition 3.1.1): $X \sim \mathrm{Bin}(n, p_0)$ under $H_0$; exact one-sided $p$-values; three definitions of the two-sided $p$-value, which coincide for $p_0 = \frac12$ (R uses "probabilities not exceeding that of the observed value"). It is exact and conservative because of discreteness; for small $n$ some alternatives cannot be detected at all.
- Normal approximation: $Z = (X - np_0)/\sqrt{np_0(1-p_0)}$, with the continuity correction of $\frac12$ towards the center; rule of thumb $np_0, n(1-p_0) \ge 5$, but the accuracy depends on the skewness, and exact computation is always available.
- Derived tests: sign, McNemar, Cox–Stuart (all binomial tests with $p_0 = \frac12$).
- Median: any $M$ with $\mathbb{P}(X \le M) \ge \frac12$ and $\mathbb{P}(X \ge M) \ge \frac12$ (Definition 3.3.1); unique for continuous strictly increasing $F$, possibly an interval for discrete distributions.
- Sign test (Definition 3.4.1): $N_+ \sim \mathrm{Bin}(n, \frac12)$; needs only independence and a common median; zeros are dropped.
- Wilcoxon signed-rank test (Definition 3.5.1): $S_+ + S_- = \frac{n(n+1)}{2}$; needs symmetry; exact distribution from the $2^n$ sign allocations, $c_n(w) = c_{n-1}(w) + c_{n-1}(w-n)$; $\mathbb{E}W = \frac{n(n+1)}{4}$, $\operatorname{Var}W = \frac{n(n+1)(2n+1)}{24}$, asymptotically normal (Theorem 3.5.1).
- Ties (Definition 3.5.2): midranks; the variance falls by $\sum(d^3 - d)/48$ (Theorem 3.5.2); with general scores the mean is $\sum s_i/2$ and the variance $\sum s_i^2/4$. Do not break ties by adding noise.
- Paired data: apply the one-sample tests to the differences; exchangeability within pairs implies the needed symmetry.

## Questions

1. A company claims that a quarter of the bolts sent to them are faulty. In a random sample of $50$ bolts, the number of faulty ones is recorded. (a) Why is a binomial model suitable? (b) Find the critical region of a two-sided test of $p = \frac14$ at the $5\%$ level, with the probability of rejection in each tail as close as possible to $0.025$. (c) What is its actual significance level? (d) The sample contains $8$ faulty bolts. Comment on the claim.

   **Answer** (a) Each bolt is faulty or not; if the bolts are sampled at random from a large consignment, the outcomes are (approximately) independent with a common probability $p$ of being faulty, so the count is $\mathrm{Bin}(50, p)$. (b) Under $H_0$, $\mathbb{P}(X \le 6) = 0.0194$ and $\mathbb{P}(X \le 7) = 0.0453$, so the lower tail closest to $0.025$ is $\{X \le 6\}$; $\mathbb{P}(X \ge 19) = 0.0287$ and $\mathbb{P}(X \ge 20) = 0.0139$, so the upper tail is $\{X \ge 19\}$. The critical region is $\{X \le 6\}\cup\{X \ge 19\}$. (c) The actual level is $0.0194 + 0.0287 = 0.048$. (d) $8$ is not in the critical region ($\mathbb{P}(X \le 8) = 0.092$; `binom.test(8, 50, 0.25)` gives $p = 0.19$), so the data are consistent with the company's claim, although the observed proportion $0.16$ is below $0.25$.
2. An education authority runs $114$ primary schools. A random sample of $12$ is drawn to test whether the median number of children per school is $225$; $3$ of the sampled schools have fewer than $225$ children. (a) Why is a binomial model suitable? (b) Find the two-sided $5\%$ critical region with each tail as close as possible to $0.025$, (c) its actual level, and (d) the conclusion.

   **Answer** (a) Under $H_0$ each sampled school has probability $\frac12$ of having fewer than $225$ children; strictly, sampling $12$ of $114$ schools without replacement makes the count hypergeometric, but with $114$ schools the binomial $\mathrm{Bin}(12, \frac12)$ is a close approximation (and exact if the $114$ schools are viewed as a sample from a population of possible schools). (b) $\mathbb{P}(X \le 2) = 0.0193$ and $\mathbb{P}(X \le 3) = 0.0730$, so the region is $\{X \le 2\}\cup\{X \ge 10\}$. (c) Its actual level is $2 \times 0.0193 = 0.039$. (d) $X = 3$ is not in the region (two-sided $p = 2 \times 0.073 = 0.146$), so $H_0\colon\theta = 225$ is retained.
3. The developers of a diet claim that adults following it lose a median of $5\,\mathrm{kg}$ in two months. Sixteen adults lost $4, 6, 3, 1, 2, 5, 4, 0, 3, 6, 3, 1, 7, 2, 5, 6\,\mathrm{kg}$. (a) Test the claim without assuming symmetry. (b) If symmetry is assumed, which test is more appropriate, and (c) what does it give?

   **Answer** (a) Sign test: the deviations from $5$ are $-1, 1, -2, -4, -3, 0, -1, -5, -2, 1, -2, -4, 2, -3, 0, 1$. Dropping the two zeros, $N_+ = 4$ of $n = 14$, and the two-sided $p$-value is $2\,\mathbb{P}(N_+ \le 4) = 0.180$: no significant evidence against the claim. (b) Under symmetry the Wilcoxon signed-rank test uses the magnitudes and is more powerful. (c) The absolute deviations have many ties (midranks $3$ for the five $1$'s, $7.5$ for the four $2$'s, $10.5$, $12.5$ and $14$); $S_+ = 3 + 3 + 7.5 + 3 = 16.5$ and $S_- = 88.5$ with $n = 14$. With the tie-corrected variance and continuity correction, `wilcox.test(x, mu = 5)` gives $p \approx 0.025$. The signed-rank test rejects the claim at the $5\%$ level: most deviations are negative and the negative ones are the larger ones. The sample median weight loss is $3.5\,\mathrm{kg}$.
4. With $12$ observations, suppose that the ranks $1$ to $6$ of the absolute deviations from $\theta_0$ all carry minus signs and the ranks $7$ to $12$ all carry plus signs. What do the sign test and the signed-rank test say, and what does the pattern suggest?

   **Answer** The sign test has $N_+ = 6$ of $12$, the most likely value under $H_0$, with $p = 1$. The signed-rank test has $S_- = 21$ and $S_+ = 57$; with mean $39$ and standard deviation $12.75$, $z \approx -1.37$ (continuity-corrected), $p \approx 0.17$, and the exact $p$-value is $2 \cdot 361/4096 = 0.176$: not significant with $n = 12$, but a clear tilt towards large positive deviations. The pattern says that the observations above $\theta_0$ are systematically farther from it than those below: the distribution looks right-skewed with median near $\theta_0$, or symmetric with center above $\theta_0$. The two tests answer different questions here, and the signed-rank test is not a valid test of the median when symmetry is in doubt.
5. Lengths (in cm) of $12$-year-old Greenland turbot, with frequencies in parentheses, are $64(1)$, $65(2)$, $66(1)$, $67(1)$, $68(4)$, $69(3)$, $70(4)$, $71(5)$, $72(3)$, $73(3)$, $75(1)$, $77(6)$, $78(1)$, $83(1)$. Is a Wilcoxon signed-rank test of $H_0\colon\theta = 73.5$ appropriate, and what issues must be handled?

   **Answer** There are $36$ fish and no zeros (no length equals $73.5$), but the data are heavily tied, so midranks and the variance correction of Theorem 3.5.2 are essential, and the exact distribution must be computed for the tied scores rather than taken from untied tables. The symmetry assumption is doubtful: the six fish of length $77$ and the single long fish at $83$ suggest a right tail. If the aim is the median, the sign test is safer: $27$ fish are shorter than $73.5$ and $9$ longer, so $N_+ = 9$ of $36$ and $p = 2\,\mathbb{P}(N_+ \le 9) = 0.004$, strong evidence that the median length is below $73.5\,\mathrm{cm}$. The signed-rank test gives $S_+ = 170.5$, $S_- = 495.5$ and $p \approx 0.011$ (normal approximation with tie correction): it also rejects, but less strongly than the sign test, because the few fish above $73.5$ deviate by large amounts and so carry large ranks. Its conclusion concerns the center of symmetry, which is meaningful only if the distribution is roughly symmetric.
