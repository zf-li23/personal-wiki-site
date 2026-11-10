---
title: Confidence Intervals for the Median and the Efficiency of Tests
description: Confidence intervals for a median by inverting the sign test (trial and error, order statistics, normal approximation) and the Wilcoxon signed-rank test (Walsh averages); a comparison with the t interval; the power of a test, relative efficiency and randomized decision rules; Pitman asymptotic relative efficiency, efficacy and its regularity conditions, with the efficiencies of the sign and Wilcoxon tests under normal and heavy-tailed populations.
---

The **sign test** and the **Wilcoxon signed-rank test** of [3.6.3](/3.6.3) answer a yes-or-no question about a median: is $\theta=\theta_0$? A data analyst usually wants more, namely a range of plausible values for $\theta$. This chapter obtains it by inverting the two tests: a confidence interval is the set of all $\theta_0$ that the test does not reject. The construction needs no distributional model beyond what the test itself assumed, which is the main advantage over the $t$ interval, whose validity rests on normality or a large sample. The sign test gives intervals whose endpoints are **order statistics** of the data; the signed-rank test gives intervals whose endpoints are order statistics of the pairwise means, the Walsh averages. The second half of the chapter asks how good these tests are. Power, relative efficiency and, above all, the Pitman asymptotic relative efficiency turn the question "which test should I use?" into a number that depends only on the shape of the population. The point estimates that go with the intervals and the comparison of tests under outliers follow in [3.6.5](/3.6.5); the efficiency ideas return for two-sample tests in [3.6.9](/3.6.9).

Throughout, $X_1,\dots,X_n$ are independent observations with median $\theta$, $X_{(1)}<\cdots<X_{(n)}$ are their order statistics, and the running example is the change in heart rate of $12$ female students,

$$
-2,\ 4,\ 8,\ 25,\ -5,\ 16,\ 3,\ 1,\ 12,\ 17,\ 20,\ 9,
$$
sorted: $-5,-2,1,3,4,8,9,12,16,17,20,25$. For the sign test of $H_0\colon\theta=\theta_0$ we write $K=\#\{i\colon X_i>\theta_0\}$ (the $n_+$ of [3.2.6](/3.2.6)), which is $\mathrm{Bin}(n,1/2)$ under $H_0$; for the signed-rank test $S_+$ and $S_-$ are the sums of the ranks of $\lvert X_i-\theta_0\rvert$ over the positive and negative differences ($S_+$ is the $W^+$ of [3.2.6](/3.2.6)), with $S_++S_-=n(n+1)/2$.

## 4.1. Confidence Intervals by Inverting Tests

For a mean, a confidence interval needs assumptions: either a normal population or a sample large enough for the **central limit theorem**. For a median, or any other **quantile**, no such requirement is needed, because the sign test is exact for every continuous population. The bridge from tests to intervals is the duality of tests and confidence sets ([Theorem 5.5.1](/3.2.5#thm-5.5.1) in 3.2.5).

**Theorem 4.1.1 (Test Inversion)** For each $\theta_0$, let $A(\theta_0)$ be the acceptance region of a test of $H_0\colon\theta=\theta_0$ with level at most $\alpha$. Then the random set

$$
C(\boldsymbol{X})=\{\theta_0\colon\boldsymbol{X}\in A(\theta_0)\}
$$
satisfies $\mathbb{P}_\theta\big(\theta\in C(\boldsymbol{X})\big)\ge1-\alpha$ for every $\theta$: it is a confidence set of level $1-\alpha$.

**Proof** $\theta\in C(\boldsymbol{X})$ if and only if $\boldsymbol{X}\in A(\theta)$, and $\mathbb{P}_\theta(\boldsymbol{X}\in A(\theta))\ge1-\alpha$ because the test of the true value $\theta$ rejects with probability at most $\alpha$. $\square$

In words: the confidence interval collects the values of $\theta_0$ that "survive" the test. Two features carry over from the test to the interval. Its assumptions are those of the test, and nothing else; and when the test statistic is discrete, the interval's actual confidence level is $1$ minus the actual size of the test, usually a little above the nominal $1-\alpha$.

## 4.2. Intervals from the Sign Test

### 4.2.1. Trial and Error

The direct way to invert the sign test is to run it for many values of $\theta_0$. The two-sided level-$\alpha$ test rejects when $K\le k$ or $K\ge n-k$, where the critical value $k=k_{\alpha/2}$ is the largest integer with $\mathbb{P}(K\le k)\le\alpha/2$ under $\mathrm{Bin}(n,1/2)$. A value $\theta_0$ belongs to the interval when $k<K<n-k$, or equivalently when $\min(n_+,n_-)>k$.

The sign of $X_i-\theta_0$ changes only when $\theta_0$ passes $X_i$, so $K$ is a step function of $\theta_0$ that is constant between consecutive order statistics. It suffices to try one value in each of the $n+1$ gaps, for example $\theta_0=X_{(i)}-\varepsilon$ for $i=1,\dots,n$ and $\theta_0=X_{(n)}+\varepsilon$.

**Example 4.2.1 (Heart Rate Data)** For $n=12$, $\mathbb{P}(K\le2)=79/4096=0.0193$ and $\mathbb{P}(K\le3)=0.073$, so at $\alpha=0.05$ the critical value is $k=2$ and the test rejects when $\min(n_+,n_-)\le2$. Trying the midpoints between the sorted observations:

| $\theta_0$ | $-5.5$ | $-2.5$ | $0.5$ | $2.5$ | $3.5$ | $7.5$ | $8.5$ | $11.5$ | $15.5$ | $16.5$ | $19.5$ | $24.5$ | $25.5$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\min(n_+,n_-)$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ | $0$ |

The test does not reject for $\theta_0$ between $2.5$ and $16.5$, and since $\min(n_+,n_-)$ only changes at data points, the accepted values extend to the neighboring data points $1$ and $17$: the interval is $(1,17)$, with confidence level $1-2\times0.0193=96.14\%$.

```r
x <- sort(c(-2, 4, 8, 25, -5, 16, 3, 1, 12, 17, 20, 9))
n <- length(x)
k <- qbinom(p = 0.025, size = n, prob = 0.5)   # 3, but P(K <= 3) = 0.073 > 0.025
k <- k - 1                                     # 2, P(K <= 2) = 0.0193
theta <- c(x - 0.5, x[n] + 0.5)
k0 <- apply(sapply(theta, function(y) x - y), 2, function(d) min(sum(d < 0), sum(d > 0)))
rbind(theta, k0)
```

:::

Whether the endpoints are included does not matter for a continuous population: the probability that the median equals an observation is $0$. With ties or rounded data, the closed interval $[X_{(k+1)},X_{(n-k)}]$ is the safe choice, since it can only increase the coverage.

### 4.2.2. The Order-Statistic Method

The trial-and-error table shows a pattern: by the symmetry of $\mathrm{Bin}(n,1/2)$, the endpoints are the same number of places in from each end of the sorted sample. The candidate intervals are $(X_{(1)},X_{(n)})$, $(X_{(2)},X_{(n-1)})$, and so on, and their confidence levels can be written down directly.

**Theorem 4.2.1** Let $X_1,\dots,X_n$ be independent, each continuous with median $\theta$ (they need not be identically distributed), and let $1\le r\le n/2$. Then

$$
\mathbb{P}\big(X_{(r)}<\theta<X_{(n-r+1)}\big)=1-2\,\mathbb{P}(B\le r-1),\qquad B\sim\mathrm{Bin}(n,1/2).
$$
Consequently, with $k=k_{\alpha/2}$ the critical value of the sign test, $\big(X_{(k+1)},X_{(n-k)}\big)$ is a confidence interval for $\theta$ of level $1-2\,\mathbb{P}(B\le k)\ge1-\alpha$.

**Proof** Let $B$ be the number of observations below $\theta$; since $\mathbb{P}(X_i<\theta)=1/2$ independently for each $i$, $B\sim\mathrm{Bin}(n,1/2)$. The event $X_{(r)}>\theta$ means that fewer than $r$ observations lie below $\theta$, so $\mathbb{P}(X_{(r)}>\theta)=\mathbb{P}(B\le r-1)$; by the same argument applied to the observations above $\theta$, $\mathbb{P}(X_{(n-r+1)}<\theta)=\mathbb{P}(n-B\le r-1)=\mathbb{P}(B\le r-1)$. The two events are disjoint because $X_{(r)}\le X_{(n-r+1)}$, and ties with $\theta$ have probability $0$. $\square$

The same argument for a general quantile gives the interval of [3.6.7](/3.6.7). If $x_p$ is the $p$-quantile of a continuous distribution and $Y_1<\cdots<Y_n$ are the order statistics of an i.i.d. sample, with $Y_0=-\infty$ and $Y_{n+1}=+\infty$, then the number $K_p$ of observations below $x_p$ is $\mathrm{Bin}(n,p)$ and

$$
\mathbb{P}(Y_k\le x_p<Y_{k+1})=\mathbb{P}(K_p=k)=\binom nk p^k(1-p)^{n-k},\qquad \mathbb{P}(Y_r\le x_p<Y_s)=\sum_{k=r}^{s-1}\binom nk p^k(1-p)^{n-k}.
$$
It is worth being clear about what is random here: the quantile $x_p$ is a fixed number, and the probabilities are about the random order statistics $Y_k$ that bracket it.

**Example 4.2.2** For $n=12$ and $p=1/2$, the probabilities $\mathbb{P}(K_p=k)$ that the median lies between the $k$-th and $(k+1)$-th order statistic are

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\mathbb{P}(K_p=k)$ | $0.000$ | $0.003$ | $0.016$ | $0.054$ | $0.121$ | $0.193$ | $0.226$ | $0.193$ | $0.121$ | $0.054$ | $0.016$ | $0.003$ | $0.000$ |

Summing the middle entries from $k=2$ to $k=9$ gives $\mathbb{P}(X_{(3)}<\theta<X_{(10)})=0.9614$, the interval $(1,17)$ of Example 4.2.1, now obtained by counting three places in from each end of the sorted data.

:::

### 4.2.3. The Normal Approximation

For larger $n$ the binomial critical value can be replaced by its normal approximation. Under $H_0$, $K\approx\mathcal{N}(n/2,n/4)$, and with the **continuity correction**

$$
\mathbb{P}\big(X_{(k_1)}<\theta<X_{(k_2)}\big)=\mathbb{P}(k_1\le K_p\le k_2-1)\approx\mathbb{P}\left(\frac{2k_1-n-1}{\sqrt n}<Z<\frac{2k_2-n-1}{\sqrt n}\right),\qquad Z\sim\mathcal{N}(0,1).
$$
Setting the two bounds equal to $\mp z_{\alpha/2}$ gives the positions

$$
k_1=\frac{n+1}{2}-\frac{z_{\alpha/2}\sqrt n}{2},\qquad k_2=\frac{n+1}{2}+\frac{z_{\alpha/2}\sqrt n}{2}.
$$
The lower limit of the approximate $100(1-\alpha)\%$ interval is the order statistic with rank $k_1$, the upper limit the one with rank $k_2$, after rounding to integers (rounding $k_1$ down and $k_2$ up keeps the coverage on the safe side). The approximation is good when $np=n(1-p)=n/2\ge5$, and it becomes the method of choice from about $n\ge20$.

**Example 4.2.3** For the heart-rate data, $n/2=6\ge5$ and $z_{0.025}=1.96$, so $k_1=6.5-3.39=3.11$ and $k_2=9.89$. The nearest ranks are $3$ and $10$, which again give $(1,17)$.

:::

The three methods are one idea at three levels of convenience:

| Method | What it does | When to use | Steps |
|---|---|---|---|
| trial and error | test every $\theta_0$ and keep those not rejected | to understand the principle; any test | sort, test each gap, extend to data points |
| order statistics | the formula for the trial-and-error result | small samples | sort, find $k_{\alpha/2}$, count $k+1$ in from each end |
| normal approximation | the order-statistic method with a normal critical value | $n\ge20$ | compute $k_1,k_2$, round, count |

## 4.3. Intervals from the Wilcoxon Signed-Rank Test

### 4.3.1. Trial and Error

If the population is also symmetric about $\theta$, the signed-rank test uses the magnitudes of the differences and should give a shorter interval. Let $w=w_{\alpha/2}$ be the largest integer with $\mathbb{P}(S_+\le w)\le\alpha/2$ under $H_0$. The two-sided test accepts $H_0\colon\theta=\theta_0$ when $w<\min(S_+,S_-)$, and the interval consists of all such $\theta_0$; in principle we again find it by trying many values.

**Example 4.3.1** Eight observations from a continuous symmetric population are $-1,6,13,4,2,3,5,9$. The lower tail of the exact null distribution of $S_+$ for $n=8$ (out of $2^8=256$ equally likely sign patterns) is

| $s$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|---|
| positive ranks giving $S_+=s$ | none | $1$ | $2$ | $\{1,2\}$, $3$ | $\{1,3\}$, $4$ | $\{1,4\}$, $\{2,3\}$, $5$ |
| $\mathbb{P}(S_+=s)$ | $1/256$ | $1/256$ | $1/256$ | $2/256$ | $2/256$ | $3/256$ |

Since $256\times0.025=6.4$ and $\mathbb{P}(S_+\le3)=5/256=0.0195$ while $\mathbb{P}(S_+\le4)=7/256$, the critical value is $w=3$. Evaluating $\min(S_+,S_-)$ on a grid of $\theta_0$:

```r
W <- function(x) {
  x <- x[x != 0]; n <- length(x)
  wplus <- sum(rank(abs(x)) * (x > 0))
  min(wplus, n * (n + 1) / 2 - wplus)
}
x <- c(-1, 6, 13, 4, 2, 3, 5, 9)
theta <- seq(from = 1.1, to = 10.1, by = 0.5)
rbind(theta, w = sapply(theta, function(t0) W(x - t0)))
```

```text
theta 1.1 1.6 2.1 2.6  3.1  3.6  4.1  4.6  5.1  5.6  6.1  6.6 7.1 7.6 8.1 8.6 9.1 9.6 10.1
w     3.0 4.0 6.0 8.0 10.0 12.0 16.0 18.0 16.0 14.0 11.0 10.0 9.0 7.0 6.0 5.0 3.0 2.0  2.0
```

The statistic exceeds $w=3$ from just above $1.5$ to just below $9$ (indeed `W(x - 1.5)` and `W(x - 9)` give $3.5$, the boundary cases). The interval is $(1.5,9)$ with confidence level $1-2\times5/256=96.1\%$: hypothesized values outside it are rejected at the exact significance level $0.039$.

:::

The table has a striking regularity: $\min(S_+,S_-)$ rises steadily and then falls, without irregular bumps. The reason is the representation of the next subsection: as $\theta_0$ increases, $S_+$ drops by exactly one each time $\theta_0$ passes a Walsh average, so $S_+$ is a nonincreasing step function of $\theta_0$ and $\min(S_+,N-S_+)$, with $N=n(n+1)/2$, increases until $S_+$ crosses $N/2$ and decreases afterwards. Trial and error does not by itself tell us where the jumps are, and without that knowledge it does not lead to a unique interval; the Walsh averages do.

### 4.3.2. The Walsh Average Method

The rank of $x_i$ in a sample can be written as $r(x_i)=1+\sum_{j\ne i}\boldsymbol{1}\{x_i>x_j\}$, a count of pairwise comparisons. Writing the signed-rank statistic in the same way turns it into a count of pairwise means, an idea that goes back to Noether (1967).

**Definition 4.3.1 (Walsh Averages)** The **Walsh averages** of a sample $x_1,\dots,x_n$ are the $N=n(n+1)/2$ pairwise means

$$
A_{ij}=\frac{x_i+x_j}{2},\qquad 1\le i\le j\le n,
$$
including the $n$ observations themselves ($A_{ii}=x_i$).

**Theorem 4.3.1** Let $\theta_0$ differ from all Walsh averages, and let the absolute differences $\lvert x_i-\theta_0\rvert$ be distinct. Then

$$
S_+(\theta_0)=\#\{(i,j)\colon i\le j,\ A_{ij}>\theta_0\},\qquad S_-(\theta_0)=\#\{(i,j)\colon i\le j,\ A_{ij}<\theta_0\}.
$$

**Proof** Put $d_i=x_i-\theta_0$. The rank of $\lvert d_i\rvert$ is $\#\{j\colon\lvert d_j\rvert\le\lvert d_i\rvert\}$, so

$$
S_+=\sum_{i\colon d_i>0}\#\{j\colon \lvert d_j\rvert\le d_i\}=\#\{(i,j)\colon d_i>0,\ -d_i\le d_j\le d_i\},
$$
a count of ordered pairs, with $j=i$ allowed. The conditions $-d_i\le d_j\le d_i$ say $d_j\le d_i$ and $d_i+d_j\ge0$, and these two already imply $d_i\ge0$. Hence $S_+$ counts the ordered pairs with $d_j\le d_i$ and $d_i+d_j>0$. A pair $i\ne j$ with $d_i+d_j>0$ is counted exactly once (with the larger of the two in the role of $i$), and a pair $i=j$ is counted when $d_i>0$. Since $d_i+d_j>0$ is $A_{ij}>\theta_0$, the first formula follows; the second follows from $S_-=N-S_+$ and the assumption that no Walsh average equals $\theta_0$. $\square$

The theorem says that the signed-rank statistic of the data is the sign statistic of the Walsh averages: testing $\theta=\theta_0$ with $S_+$ on $x_1,\dots,x_n$ amounts to counting how many of $A_{11},A_{12},\dots,A_{nn}$ lie above $\theta_0$. (The count is not binomial, because the Walsh averages are dependent; its null distribution is that of $S_+$.) The interval therefore has the same form as the sign-test interval, with Walsh averages in place of observations.

**Corollary 4.3.1** For a continuous population symmetric about $\theta$, let $A_{(1)}<\cdots<A_{(N)}$ be the ordered Walsh averages and $w=w_{\alpha/2}$ the critical value of $S_+$. Then $\big(A_{(w+1)},A_{(N-w)}\big)$ is a confidence interval for $\theta$ of level $1-2\,\mathbb{P}(S_+\le w)\ge1-\alpha$.

**Proof** By Theorem 4.3.1, $S_+(\theta_0)>w$ if and only if more than $w$ Walsh averages exceed $\theta_0$, that is, $\theta_0<A_{(N-w)}$; and $S_-(\theta_0)>w$ if and only if $\theta_0>A_{(w+1)}$. The acceptance condition $\min(S_+,S_-)>w$ thus describes the open interval, and Theorem 4.1.1 gives its level. $\square$

**Algorithm 4.3.1 (Walsh Average Interval)** For a $100(1-\alpha)\%$ interval for the center of symmetry:

1. find the critical value $w_{\alpha/2}$ from the null distribution of $S_+$ (R: `qsignrank`, then step down by one if the tail probability exceeds $\alpha/2$);
2. compute the $N=n(n+1)/2$ Walsh averages $A_{ij}$ and sort them;
3. the $(w_{\alpha/2}+1)$-th values from either end are the endpoints.

For the sign test the recipe is identical with the data in place of the Walsh averages and $k_{\alpha/2}$ from $\mathrm{Bin}(n,1/2)$ in place of $w_{\alpha/2}$.

**Example 4.3.2** For the eight observations of Example 4.3.1, $w=3$ and there are $36$ Walsh averages. The fourth smallest is $1.5$ and the fourth largest is $9$, reproducing the interval $(1.5,9)$ at level $96.1\%$ without any trial and error.

```r
x <- c(-1, 6, 13, 4, 2, 3, 5, 9)
wa <- outer(x, x, "+") / 2                       # all pairwise means
wa <- sort(wa[lower.tri(wa, diag = TRUE)])       # the 36 Walsh averages
c(wa[3 + 1], wa[length(wa) - 3])                 # 1.5 9.0
wilcox.test(x, conf.int = TRUE)
```

```text
	Wilcoxon signed rank exact test

data:  x
V = 35, p-value = 0.01563
alternative hypothesis: true location is not equal to 0
95 percent confidence interval:
 1.5 9.0
sample estimates:
(pseudo)median 
          4.75 
```

R's `wilcox.test` with `conf.int = TRUE` uses exactly this method. The reported estimate $4.75$ is the median of the Walsh averages, not the midpoint $5.25$ of the interval; it is the Hodges–Lehmann estimate of [3.6.5](/3.6.5).

:::

**Example 4.3.3 (Heart Rate Data)** For $n=12$, `qsignrank(0.025, 12)` returns $14$, but $\mathbb{P}(S_+\le14)=0.026>0.025$; the critical value is $w=13$, with $\mathbb{P}(S_+\le13)=0.021$. The $14$-th smallest and $14$-th largest of the $78$ Walsh averages are $2.5$ and $16$:

```text
	Wilcoxon signed rank exact test

data:  x
V = 71, p-value = 0.009277
alternative hypothesis: true location is not equal to 0
95 percent confidence interval:
  2.5 16.0
sample estimates:
(pseudo)median 
             9 
```

The interval $(2.5,16)$ has exact level $1-2\times0.021=95.75\%$ and is shorter than the sign-test interval $(1,17)$; the $t$ interval is $(3.12,14.88)$.

:::

![Two-sided p-value functions for the heart-rate data: for each hypothesized median the p-value of the sign test (a step function that jumps at the data), of the Wilcoxon signed-rank test (which jumps at the Walsh averages) and of the t test. The 95% intervals, shown as bars, are the values where the p-value exceeds 0.05; the ticks mark the data.](./plots/pvalue-functions.py)

## 4.4. Comparing the Intervals

Two small skewed samples show how the three intervals behave in practice:

$$
\begin{aligned}
&\text{Sample I}\colon && 5.5,\ 6.0,\ 6.5,\ 7.6,\ 7.6,\ 7.7,\ 8.0,\ 8.2,\ 9.1,\ 15.1,\\
&\text{Sample II}\colon && 5.6,\ 6.1,\ 6.3,\ 6.3,\ 6.5,\ 6.6,\ 7.0,\ 7.5,\ 7.9,\ 8.0,\ 8.0,\ 8.1,\ 8.1,\ 8.2,\ 8.4,\ 8.5,\ 8.7,\ 9.4,\ 14.3,\ 26.0.
\end{aligned}
$$

**Example 4.4.1** Nominal $95\%$ intervals for the center of each sample:

| Interval | Sample I ($n=10$) | width | Sample II ($n=20$) | width |
|---|---|---|---|---|
| sign test | $(6.0,9.1)$, exact level $97.85\%$ | $3.1$ | $(6.6,8.4)$, exact level $95.86\%$ | $1.8$ |
| Wilcoxon (R, normal approximation) | $(6.55,10.80)$ | $4.25$ | $(7.15,8.50)$ | $1.35$ |
| $t$ | $(6.22,10.04)$ | $3.83$ | $(6.70,10.85)$ | $4.16$ |

Two entries contradict the naive expectation that more information gives shorter intervals. First, the $t$ interval for Sample II is longer than for Sample I although the sample is twice as large: the two extreme values $14.3$ and $26.0$ inflate the sample standard deviation. Second, for Sample I the Wilcoxon interval is longer than the sign interval: the signed-rank method assumes symmetry, and in a right-skewed sample (sample skewness $1.88$ for I and $3.18$ for II) the Walsh averages involving the large observation $15.1$ stretch the upper end. The sign interval, which assumes neither normality nor symmetry, shrinks as $n$ grows, as it should.

Both samples contain **ties** ($7.6$ twice in I; $6.3$, $8.0$, $8.1$ twice in II). The sign interval needs no adjustment, since its endpoints are order statistics either way. R's `wilcox.test` cannot compute exact intervals with ties and switches to a normal approximation, which is why its endpoints ($6.550001$, $10.799962$) are not Walsh averages; the exact Walsh method of Algorithm 4.3.1, applied as if there were no ties, gives $(6.6,10.55)$ for Sample I and $(7.15,8.5)$ for Sample II. Deleting tied values, or keeping one representative of each, would be wrong: it changes $n$ and discards real observations.

:::

The lesson is general. Increasing the sample size improves estimation when the method's assumptions hold; when it does not, check the assumptions (here symmetry and normality) before blaming the data, and look at the data first: a dot plot or the sample **skewness** would have flagged both problems. The robustness side of this comparison is continued in §5.6 of [3.6.5](/3.6.5).

## 4.5. The Power of a Test

Nonparametric tests come in many forms, often several for the same hypothesis. To choose among them we need a measure of performance, and the natural one is the ability to detect a false $H_0$: the **power function** of [3.2.5](/3.2.5),

$$
\gamma_n(\theta)=\mathbb{P}_\theta(\text{reject }H_0),
$$
or, at a fixed alternative, the **statistical power** $\gamma_n=\mathbb{P}_{H_1}(\text{reject }H_0)=1-\beta$, where $\beta$ is the probability of a **type II error**. The power of a test increases with

- the sample size $n$;
- the significance level $\alpha$ (a larger rejection region rejects more often under every $\theta$);
- the effect size, the distance between the true $\theta$ and $\theta_0$;
- the precision of the data (smaller variance of the observations).

A design question follows directly: how large must $n$ be to reach a given power, say $0.9$, at a given $\alpha$ and effect size? The answer depends on the test, and comparing the answers is how tests are compared.

The classical theory answers "which test is best?" with the **Neyman–Pearson lemma**: for two simple hypotheses the likelihood ratio test is most powerful, and when it is most powerful against every alternative in $\Theta_1$ it is a **uniformly most powerful test** (UMP). Such tests exist only in narrow classes of models, essentially one-parameter families with monotone likelihood ratio ([3.2.5](/3.2.5)). In the nonparametric setting, where the population is any continuous distribution with median $\theta$, there is no uniformly best test, and we compare tests instead through efficiencies.

## 4.6. Relative Efficiency

**Definition 4.6.1 (Relative Efficiency)** Let tests $T_1$ and $T_2$ of the same hypotheses reach the same power at the same level $\alpha$ against the same alternative with sample sizes $n_1$ and $n_2$. The **relative efficiency** of $T_1$ with respect to $T_2$ is

$$
\operatorname{RE}(T_1,T_2)=\frac{n_2}{n_1}.
$$
If $\operatorname{RE}>1$, the test $T_1$ is more efficient: it needs fewer observations for the same performance.

The relative efficiency is a ratio of sample sizes, so it has a direct practical meaning ("the sign test needs $78\%$ more observations"), but it depends on everything that was fixed: $\alpha$, the target power and the alternative.

**Example 4.6.1 (z Test Versus Sign Test)** Let the data be $\mathcal{N}(\mu,1)$ and test $H_0\colon\mu=0$ against $H_1\colon\mu>0$ at $\alpha=0.05$; we want power $0.9$ at $\mu=1$. The $z$ test has power $1-\Phi(1.645-\sqrt n)$, which first exceeds $0.9$ at $n_z=9$ (power $0.912$). The sign test counts $K=\#\{X_i>0\}$, which is $\mathrm{Bin}(n,p)$ with $p=\Phi(1)=0.841$ under the alternative; computing its power from the binomial distribution for each $n$ shows that the target is first reached at $n_{\mathrm{sign}}=16$ (power $0.904$, actual size $0.038$). Hence

$$
\operatorname{RE}(z,\operatorname{sgn})=\frac{16}{9}\approx1.78,
$$
or, the other way round, the sign test has efficiency $9/16=0.56$ relative to the $z$ test for this problem.

:::

The power of the sign test in this example is not monotone in $n$: at $n=13$ it is $0.862$, at $n=14$ only $0.830$. Because $K$ is discrete, the actual size of the nonrandomized test jumps around below $\alpha$ ($0.046$ at $n=13$, $0.029$ at $n=14$), and with it the power. Such jumps make sample-size comparisons erratic. The theoretical remedy is to randomize at the boundary of the rejection region, so that every test has size exactly $\alpha$.

**Example 4.6.2 (A Randomized Sign Test)** With $n=5$ observations, test $H_0\colon\theta=0$ against $H_1\colon\theta>0$ at $\alpha=0.10$. Under $H_0$, $\mathbb{P}(K=5)=1/32=0.031$ and $\mathbb{P}(K\ge4)=6/32=0.1875$, so the best nonrandomized test rejects only when $K=5$ and has size $0.031$, far below $0.10$. The **randomized test**

$$
\varphi(K)=\begin{cases}1, & K=5,\\ \gamma, & K=4,\\ 0, & K\le3,\end{cases}\qquad \gamma=\frac{0.10-1/32}{5/32}=0.44,
$$
rejects when $K=5$, and when $K=4$ rejects with probability $0.44$ (by an auxiliary random draw). Its size is $\frac1{32}+0.44\cdot\frac5{32}=0.10$ exactly.

:::

Randomized decision rules (the test functions $\varphi$ with values in $[0,1]$ of [3.2.5](/3.2.5)) let discrete tests attain an exact $\alpha$, or an exact power, and so make comparisons between tests fair. In applied work they are a minor theoretical correction rather than a tool: two analysts with the same data could reach different conclusions, and it is better to report the exact $p$-value together with the actual size of the test.

## 4.7. Pitman Asymptotic Relative Efficiency

### 4.7.1. Definition and Efficacy

The relative efficiency of Example 4.6.1 would change with $\alpha$, the target power and the alternative. To obtain a single number we let $n\to\infty$. Against a fixed alternative every reasonable test has power tending to $1$, so the alternatives must approach $\theta_0$ as $n$ grows; Pitman's choice is a sequence of local alternatives at the rate $1/\sqrt n$, at which the power stays strictly between $\alpha$ and $1$.

**Definition 4.7.1 (Asymptotic Relative Efficiency)** Consider a sequence of alternatives $\theta_k\to\theta_0$ (Pitman alternatives, $\theta_k=\theta_0+d/\sqrt{n_k}+o(1/\sqrt{n_k})$), and let $n_1(k)$ and $n_2(k)$ be the sample sizes with which tests $T_1$ and $T_2$ attain the same asymptotic power against $\theta_k$ at level $\alpha$. The (Pitman) **asymptotic relative efficiency** of $T_1$ with respect to $T_2$ is

$$
\operatorname{ARE}(T_1,T_2)=\lim_{k\to\infty}\frac{n_2(k)}{n_1(k)},
$$
when the limit exists.

The ARE is computed from a simpler quantity attached to each test statistic.

**Definition 4.7.2 (Efficacy)** Let $T_n$ be a test statistic with $\mu_n(\theta)=\mathbb{E}_\theta T_n$ and $\sigma_n^2(\theta)=\operatorname{Var}_\theta(T_n)$. The **efficacy** of $T_n$ at $\theta_0$ is

$$
e(T_n)=\frac{\big[\mu_n'(\theta_0)\big]^2}{\sigma_n^2(\theta_0)}.
$$

The efficacy measures how fast the mean of the statistic moves away from its null value, in units of its null standard deviation: a larger efficacy means a more sensitive, hence more powerful, test. The following conditions make this precise; they hold for all the common one-sample tests ($t$, sign, Wilcoxon).

1. $\mu_n(\theta)$ exists and is differentiable at $\theta_0$, with $\mu_n'(\theta_0)>0$ (the test rejects for large $T_n$).
2. The efficacy grows linearly: $e(T_n)/n\to c$ for a finite positive constant $c$.
3. Under Pitman alternatives $\theta_n=\theta_0+d/\sqrt n$, the derivative and the standard deviation are locally stable: $\mu_n'(\theta_n)/\mu_n'(\theta_0)\to1$ and $\sigma_n(\theta_n)/\sigma_n(\theta_0)\to1$.
4. $T_n$ is asymptotically normal under these alternatives: $\big(T_n-\mu_n(\theta_n)\big)/\sigma_n(\theta_n)\xrightarrow{d}\mathcal{N}(0,1)$ under $\theta_n$.
5. The test that rejects when $\big(T_n-\mu_n(\theta_0)\big)/\sigma_n(\theta_0)>z_\alpha$ has asymptotic level $\alpha$.

**Theorem 4.7.1 (Pitman–Noether)** Under conditions 1–5, the level-$\alpha$ test based on $T_n$ has asymptotic power

$$
\lim_{n\to\infty}\mathbb{P}_{\theta_n}(\text{reject }H_0)=1-\Phi\big(z_\alpha-d\sqrt c\big)\qquad\text{at }\theta_n=\theta_0+\frac{d}{\sqrt n}.
$$
For two tests satisfying the conditions with constants $c_1,c_2$,

$$
\operatorname{ARE}(T_1,T_2)=\frac{c_1}{c_2}=\lim_{n\to\infty}\frac{e\big(T_n^{(1)}\big)}{e\big(T_n^{(2)}\big)}.
$$

**Proof** Write $\mu_n=\mu_n(\theta_0)$, $\sigma_n=\sigma_n(\theta_0)$. The power at $\theta_n$ is

$$
\mathbb{P}_{\theta_n}\left(\frac{T_n-\mu_n(\theta_n)}{\sigma_n(\theta_n)}>\frac{\sigma_n}{\sigma_n(\theta_n)}\left(z_\alpha-\frac{\mu_n(\theta_n)-\mu_n}{\sigma_n}\right)\right).
$$
By the mean value theorem and condition 3, $\big(\mu_n(\theta_n)-\mu_n\big)/\sigma_n=\mu_n'(\tilde\theta_n)\,d/(\sqrt n\,\sigma_n)\to d\sqrt c$, using $\mu_n'(\theta_0)/\sigma_n=\sqrt{e(T_n)}$ and condition 2; also $\sigma_n/\sigma_n(\theta_n)\to1$. Condition 4 then gives the limit $1-\Phi(z_\alpha-d\sqrt c)$. For the ARE, two tests reach the same asymptotic power against the same alternatives $\theta_k-\theta_0=d_1/\sqrt{n_1}=d_2/\sqrt{n_2}$ exactly when $d_1\sqrt{c_1}=d_2\sqrt{c_2}$, that is, $n_1c_1=n_2c_2$, so $n_2/n_1\to c_1/c_2$. $\square$

The theorem explains the properties that make the ARE useful. It does not depend on $\alpha$, on the target power or on $d$: all of them cancel. It depends only on the population distribution, through the efficacies. The same calculation for estimators (the ratio of asymptotic variances) gives the same numbers for the estimators derived from these tests, which is the subject of §5.2 of [3.6.5](/3.6.5).

### 4.7.2. The t, Sign and Wilcoxon Tests

Consider the one-sample location model: $X_1,\dots,X_n$ are i.i.d. with distribution function $F(x-\theta)$, where $F$ is continuous with density $f$, median $0$ and variance $\sigma^2$, and we test $H_0\colon\theta=0$ against $H_1\colon\theta>0$.

**Example 4.7.1 (The t Test)** The $t$ statistic is $T_n^{(2)}=\sqrt n\bar X_n/S_n=(\sqrt n\bar X_n/\sigma)(\sigma/S_n)$, and $\sigma/S_n\to1$, so for large $n$ it behaves like the $z$ statistic with known $\sigma$. Then $\mathbb{E}T_n^{(2)}\approx\sqrt n\,\theta/\sigma$, so $\mathrm{d}\mathbb{E}T_n^{(2)}/\mathrm{d}\theta=\sqrt n/\sigma$, and $\operatorname{Var}T_n^{(2)}\approx n\operatorname{Var}(\bar X_n)/\sigma^2=1$. The efficacy is

$$
e\big(T_n^{(2)}\big)=\frac{n}{\sigma^2}.
$$

:::

**Example 4.7.2 (The Sign Test)** The sign statistic $T_n^{(1)}=K$ is $\mathrm{Bin}(n,p(\theta))$ with $p(\theta)=\mathbb{P}(X>0)=1-F(-\theta)$. Thus $\mathbb{E}K=np(\theta)$, $\mathrm{d}\mathbb{E}K/\mathrm{d}\theta|_{\theta=0}=nf(0)$, and $\operatorname{Var}K|_{\theta=0}=n/4$, so

$$
e\big(T_n^{(1)}\big)=4nf(0)^2,\qquad \operatorname{ARE}(\operatorname{sgn},t)=4\sigma^2f(0)^2 .
$$
For a normal population $f(0)=(2\pi\sigma^2)^{-1/2}$ and $\operatorname{ARE}(\operatorname{sgn},t)=2/\pi\approx0.637$: when the $t$ test is appropriate, the sign test wastes over a third of the sample.

:::

**Example 4.7.3 (The Wilcoxon Signed-Rank Test)** For a symmetric $F$, Theorem 4.3.1 writes $S_+=\sum_{i\le j}\boldsymbol{1}\{X_i+X_j>0\}$, so

$$
\mathbb{E}S_+=n\,\mathbb{P}(X_1>0)+\binom n2\mathbb{P}(X_1+X_2>0)=n\big[1-F(-\theta)\big]+\binom n2\int_{-\infty}^{\infty}\big[1-F(-x-2\theta)\big]\,\mathrm{d}F(x).
$$
Differentiating at $\theta=0$ and using $f(-x)=f(x)$,

$$
\left.\frac{\mathrm{d}\mathbb{E}S_+}{\mathrm{d}\theta}\right|_{\theta=0}=nf(0)+n(n-1)\int_{-\infty}^{\infty}f^2(x)\,\mathrm{d}x .
$$
With $\operatorname{Var}S_+=n(n+1)(2n+1)/24$ under $H_0$,

$$
e(S_+)=\frac{24\big[nf(0)+n(n-1)\int f^2\big]^2}{n(n+1)(2n+1)}\sim12n\left(\int f^2(x)\,\mathrm{d}x\right)^2,\qquad \operatorname{ARE}(\text{Wilcoxon},t)=12\sigma^2\left(\int f^2(x)\,\mathrm{d}x\right)^2 .
$$
For a normal population $\int f^2=1/(2\sigma\sqrt\pi)$ and the ARE is $3/\pi\approx0.955$.

:::

The formulas evaluated for several symmetric populations:

| Population | $\operatorname{ARE}(\operatorname{sgn},t)$ | $\operatorname{ARE}(\text{Wilcoxon},t)$ | $\operatorname{ARE}(\operatorname{sgn},\text{Wilcoxon})$ |
|---|---|---|---|
| uniform | $1/3$ | $1$ | $1/3$ |
| normal | $2/\pi\approx0.637$ | $3/\pi\approx0.955$ | $2/3$ |
| logistic | $\pi^2/12\approx0.822$ | $\pi^2/9\approx1.097$ | $3/4$ |
| Laplace (double exponential) | $2$ | $1.5$ | $4/3$ |
| $t_3$ | $1.62$ | $1.90$ | $0.85$ |
| Cauchy | $\infty$ | $\infty$ | $4/3$ |

The table shows how strongly the ARE depends on the tails. For the light-tailed uniform the sign test is poor; for the normal the $t$ test wins, but the Wilcoxon test loses less than $5\%$; as soon as the tails are heavier than normal (logistic, $t_3$, **Laplace distribution**) the nonparametric tests are more efficient, and for the **Cauchy distribution**, which has no variance, the $t$ test loses all its efficiency. Two general results frame the table: Hodges and Lehmann (1956) showed that $\operatorname{ARE}(\text{Wilcoxon},t)\ge108/125=0.864$ for every continuous symmetric population, so the Wilcoxon test can never be much worse than the $t$ test and can be infinitely better; the sign test has no such lower bound, and its efficiency relative to the Wilcoxon test exceeds $1$ only for sharply peaked or very heavy-tailed populations, like the Laplace. Summing up: for normal data prefer the $t$ test; for symmetric but heavy-tailed data the Wilcoxon test; without a symmetry assumption, the sign test.

The ARE is a large-sample, local criterion, but it is often a good guide for small samples: in Example 4.6.1 the small-sample relative efficiency of the sign test was $9/16=0.56$, against the asymptotic $2/\pi=0.64$, and for many tests the small-sample relative efficiency is close to, or even above, the Pitman value. In short: when it is relevant and valid, the $t$ test is the most powerful test of a mean; when it is not appropriate, other tests may have higher efficiency.

![Simulated power of the one-sided sign, Wilcoxon signed-rank and t tests at level 0.05 with n = 20, against a shift measured in standard deviations (4000 samples per point; the sign and Wilcoxon tests are randomized to exact level 0.05). Left: normal data, where the t and Wilcoxon tests are nearly equivalent and the sign test lags. Right: t distribution with 3 degrees of freedom scaled to unit variance, where the order is reversed.](./plots/power-curves.py)

## Summary

- Test inversion (Theorem 4.1.1): a confidence interval is the set of $\theta_0$ not rejected; it inherits the assumptions and, for discrete statistics, the actual level of the test.
- Sign-test interval (Theorem 4.2.1): $\big(X_{(k+1)},X_{(n-k)}\big)$ with $k=k_{\alpha/2}$ from $\mathrm{Bin}(n,1/2)$, exact level $1-2\,\mathbb{P}(B\le k)$; needs only independence and a common median. Normal approximation: ranks $\frac{n+1}{2}\mp\frac{z_{\alpha/2}\sqrt n}{2}$.
- Wilcoxon interval (Corollary 4.3.1): $\big(A_{(w+1)},A_{(N-w)}\big)$ from the $N=n(n+1)/2$ ordered Walsh averages, because $S_+(\theta_0)$ counts the Walsh averages above $\theta_0$ (Theorem 4.3.1); needs symmetry.
- Heart-rate data ($n=12$): sign $(1,17)$ at $96.1\%$, Wilcoxon $(2.5,16)$ at $95.8\%$, $t$ $(3.1,14.9)$. Skewness and outliers can reverse the usual ordering of interval lengths (Example 4.4.1).
- Relative efficiency (Definition 4.6.1) is a ratio of sample sizes for equal $\alpha$, power and alternative; randomized rules (Example 4.6.2) give discrete tests an exact size.
- Pitman ARE (Definition 4.7.1) is the limit of the relative efficiency under local alternatives; it equals the ratio of efficacies (Theorem 4.7.1) and depends only on the population:

| | general formula | normal | Laplace |
|---|---|---|---|
| $\operatorname{ARE}(\operatorname{sgn},t)$ | $4\sigma^2f(0)^2$ | $0.637$ | $2$ |
| $\operatorname{ARE}(\text{Wilcoxon},t)$ | $12\sigma^2\big(\int f^2\big)^2\ \ (\ge0.864)$ | $0.955$ | $1.5$ |

## Questions

1. Does it matter whether the sign-test interval of Example 4.2.1 is written as $(1,17)$ or $[1,17]$?

   **Answer** Not for a continuous population: $\mathbb{P}(\theta=X_i)=0$ for every $i$, so the open and closed intervals have the same coverage $96.14\%$. With ties or rounded data the median may coincide with an observed value, and the closed interval $[X_{(k+1)},X_{(n-k)}]$ is preferable because its coverage is at least that of the open one.

2. A student applies the normal approximation of $S_+$, $\big(S_+-n(n+1)/4\big)/\sqrt{n(n+1)(2n+1)/24}\approx\mathcal{N}(0,1)$, to the heart-rate data and obtains the "interval" $[14,64]$ from `qnorm(0.025)` and `qnorm(0.975)`. What went wrong?

   **Answer** The numbers $14$ and $64$ are bounds for the statistic $S_+$, not for $\theta$: they say that $H_0$ is accepted when $14<S_+<64$, approximately. To obtain an interval for $\theta$ we must find the $\theta_0$ for which $S_+(\theta_0)$ lies in this range, that is, use the critical value ($w\approx13$ or $14$) as a position in the ordered list of Walsh averages. This gives approximately $(2.5,16)$.

3. Show that for the uniform population $\mathrm{U}(\theta-\frac12,\theta+\frac12)$ the Pitman efficiency of the sign test relative to the $t$ test is $1/3$, and that of the Wilcoxon test is $1$.

   **Answer** Here $f=1$ on $(-\frac12,\frac12)$, so $f(0)=1$, $\sigma^2=1/12$ and $\int f^2=1$. Hence $\operatorname{ARE}(\operatorname{sgn},t)=4\sigma^2f(0)^2=4/12=1/3$ and $\operatorname{ARE}(\text{Wilcoxon},t)=12\sigma^2(\int f^2)^2=1$. With no tails at all, the magnitudes carry much information, which the sign test throws away.

4. Prove that for the Laplace density $f(x)=\frac\lambda2\mathrm{e}^{-\lambda\lvert x-\theta\rvert}$ the Pitman efficiency of the sign test relative to the $t$ test is $2$.

   **Answer** With $\theta=0$, $f(0)=\lambda/2$ and $\sigma^2=\int x^2\frac\lambda2\mathrm{e}^{-\lambda\lvert x\rvert}\,\mathrm{d}x=2/\lambda^2$. So $\operatorname{ARE}(\operatorname{sgn},t)=4\cdot\frac{2}{\lambda^2}\cdot\frac{\lambda^2}{4}=2$, independent of $\lambda$. (For the Wilcoxon test, $\int f^2=\lambda/4$ and the ARE is $12\cdot\frac2{\lambda^2}\cdot\frac{\lambda^2}{16}=1.5$.) For this population the sample median is the maximum likelihood estimator of $\theta$, which explains why the sign test does so well.

5. In Example 4.6.1 the sign test needs $16$ observations where the $z$ test needs $9$. Without computing powers, estimate the sample size the sign test needs when the $z$ test needs $100$ (same $\alpha$ and power, a smaller shift).

   **Answer** For large samples and small shifts the ratio of sample sizes approaches the ARE, $\pi/2\approx1.57$ for the sign test relative to the $z$ test under normality. The sign test needs about $100\pi/2\approx157$ observations. The small-sample ratio $16/9=1.78$ is somewhat larger, partly because of the discreteness of $K$ at $n=16$.
