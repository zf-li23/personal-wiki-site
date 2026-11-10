---
title: Quantiles, Trends, Randomness and Angular Data
description: Further one-sample inference built on the sign test and on counting. The quantile test and distribution-free confidence intervals for quantiles; the Cox–Stuart test for monotone, periodic and specified trends; the runs test for randomness (exact distribution, mean and variance by indicators, normal approximation, several categories); and angular data, where linear statistics fail, the Kolmogorov statistic depends on the origin, and Kuiper's rotation-invariant statistic replaces it.
---

The **sign test** of [3.6.3](/3.6.3) reduces a question about a median to counting successes in independent trials, and then uses the **binomial test**. The same reduction answers several other one-sample questions, which this chapter collects. If the question concerns a **quantile** other than the median, the success probability is no longer $1/2$ but the order of the quantile (Section 7.2). If the observations form a time series and the question is whether they drift, pairing early with late observations again produces signs (the Cox–Stuart test, Section 7.3). A different kind of counting, the number of runs of like symbols in a sequence, tests whether the order of the observations is random (Section 7.4). Finally, data that are directions or times of day live on a circle rather than a line: there the arithmetic mean and the Kolmogorov statistic of [3.6.6](/3.6.6) depend on an arbitrary origin, and a rotation-invariant statistic due to Kuiper is needed (Section 7.5).

All the procedures are distribution-free in the sense of [3.6.2](/3.6.2): their null distributions are binomial, combinatorial or (for Kuiper's statistic) those of a statistic of uniform order statistics, whatever the population. The next chapter, [3.6.8](/3.6.8), applies the same ideas to paired samples, where Cox–Stuart and runs arguments test correlation and the sign test becomes McNemar's test.

## 7.1. The Sign Test as a Binomial Test

Recall the structure. Let $X_1,\dots,X_n$ be independent with a common median $\theta$, and let $\theta_0$ be a hypothesized value. Writing $p=\mathbb{P}(X\le\theta_0)$ for a continuous population (more generally $p=\mathbb{P}(X<\theta_0)$ after discarding ties with $\theta_0$),

$$
H_0\colon \theta=\theta_0 \quad\Longleftrightarrow\quad H_0\colon p=\tfrac12 ,
$$
and the number $S$ of observations below $\theta_0$ has the $\mathrm{Bin}(n,1/2)$ distribution under $H_0$.

**Example 7.1.1 (Water Content of Agricultural Land)** The percentage water content of soil usually varies little over an area. For $20$ quadrats the values, in increasing order, are

$$
5.6,\ 6.1,\ 6.3,\ 6.3,\ 6.5,\ 6.6,\ 7.0,\ 7.5,\ 7.9,\ 8.0,\ 8.1,\ 8.1,\ 8.2,\ 8.4,\ 8.5,\ 8.7,\ 8.7,\ 9.4,\ 14.3,\ 26.0 .
$$

We test $H_0\colon\theta=9$ against $H_1\colon\theta\ne9$. No observation equals $9$, and $17$ of the $20$ lie below it.

```r
x <- c(5.6, 6.1, 6.3, 6.3, 6.5, 6.6, 7.0, 7.5, 7.9, 8.0,
       8.1, 8.1, 8.2, 8.4, 8.5, 8.7, 8.7, 9.4, 14.3, 26.0)
binom.test(sum(x < 9), length(x))
```

```text
number of successes = 17, number of trials = 20, p-value = 0.002577
95 percent confidence interval:
 0.6210732 0.9679291
```

The two-sided $p$-value $0.0026$ is strong evidence that the median water content is below $9$. The two outlying values $14.3$ and $26.0$ do not affect the test at all: only their side of $9$ matters.

The same binomial distribution gives a confidence interval for $\theta$ ([3.6.4](/3.6.4)). Since $\mathbb{P}(S\le5)=0.0207$ and $\mathbb{P}(S\le6)=0.0577$ for $S\sim\mathrm{Bin}(20,1/2)$, the critical value is $k=5$, and by Proposition 7.2.1 below (with $q=1/2$) the interval runs from the $(k+1)$th to the $(n-k)$th order statistic,

$$
[x_{(6)},\,x_{(15)}]=[6.6,\ 8.5],
$$
with exact coverage $\mathbb{P}(6\le S\le14)=1-2\times0.0207=0.959$. The interval excludes $9$, in agreement with the test.
:::

The duality between the test and the interval can also be read from the binomial side. The interval consists of the values $\theta_0$ for which the observed count below $\theta_0$ is compatible with $p=1/2$. If $14$ observations lie below $\theta_0$, the exact $95\%$ interval for $p$ is $(0.457,\,0.881)$, which contains $0.5$; if $15$ do, it is $(0.508,\,0.913)$, which does not; by symmetry $6$ is accepted and $5$ rejected. So $\theta_0$ is accepted exactly when between $6$ and $14$ observations lie below it, that is, when $x_{(6)}<\theta_0\le x_{(15)}$. Note that the upper end point is the $15$th order statistic, not the $14$th: the number $14$ is a count of observations, and $14$ observations lie below every $\theta_0$ in $(x_{(14)},x_{(15)}]$. The interval $[x_{(6)},x_{(14)}]=[6.6,\,8.4]$ would have coverage only $\mathbb{P}(6\le S\le13)=0.922$.

## 7.2. Quantile Tests

### 7.2.1. The Test

Nothing in the argument of Section 7.1 used the value $1/2$ except through the definition of the median. Let $\xi_q$ denote a $q$-quantile of the population, so that $\mathbb{P}(X<\xi_q)\le q\le\mathbb{P}(X\le\xi_q)$, and suppose for simplicity that the population is continuous at the hypothesized value.

**Definition 7.2.1 (Quantile Test)** Let $X_1,\dots,X_n$ be independent with a common distribution $F$, continuous at $Q_0$. To test $H_0\colon\xi_q=Q_0$, the **quantile test** uses the number

$$
S=\#\{i\colon X_i<Q_0\}
$$
of observations below $Q_0$. Under $H_0$, $\mathbb{P}(X_i<Q_0)=q$, so $S\sim\mathrm{Bin}(n,q)$, and the test is the binomial test of $p=q$. Large values of $S$ indicate $\xi_q<Q_0$, small values $\xi_q>Q_0$. Observations equal to $Q_0$ are discarded, as in the sign test.

The sign test is the case $q=1/2$. For $q\ne1/2$ the null distribution is skewed, so the two tails of a two-sided test are not mirror images, and `binom.test` uses the rule "sum the probabilities of all outcomes no more likely than the observed one" of [3.6.3](/3.6.3).

**Example 7.2.1 (Examination Marks)** An examining body states that three quarters of the candidates for a paper obtain a mark of $40$ or more. One school entered $32$ candidates, of whom $13$ scored below $40$. The chairman of the parents' association argues that the school's performance is below the national standard. Is this justified?

The national statement says that the lower quartile is $40$: $\xi_{0.25}=40$, or $p=\mathbb{P}(X<40)=0.25$. Below-standard performance means that more than a quarter of the school's candidates fall below $40$, that is, $\xi_{0.25}<40$. Hence

$$
H_0\colon \xi_{0.25}=40 \ \text{ vs. }\ H_1\colon \xi_{0.25}<40
\quad\Longleftrightarrow\quad
H_0\colon p=0.25 \ \text{ vs. }\ H_1\colon p>0.25 .
$$

Under $H_0$ the number below $40$ is $\mathrm{Bin}(32,0.25)$, with mean $8$; the school has $13$.

```r
binom.test(x = 13, n = 32, p = 0.25, alternative = "greater")
binom.test(x = 13, n = 32, p = 0.25)     # two-sided, for comparison
```

```text
number of successes = 13, number of trials = 32, p-value = 0.03775
alternative hypothesis: true probability of success is greater than 0.25
...
number of successes = 13, number of trials = 32, p-value = 0.06291
95 percent confidence interval:
 0.2369841 0.5935508
```

The one-sided alternative matches the question, and its $p$-value $0.038$ is below $0.05$: there is moderate evidence that the school falls short. A two-sided test, appropriate only if the question had been "does the school differ from the national standard", gives $0.063$. The decision at the $5\%$ level depends on this choice, which must be made before looking at the data. Two further cautions: the $32$ candidates are not a random sample from a population but the whole entry of one year, so the "population" is the hypothetical stream of candidates the school would produce; and a $p$-value near $0.05$ from $32$ candidates is weak grounds for a strong claim.
:::

**Remark 7.2.1** Can the $t$-test or the **Wilcoxon signed-rank test** replace the quantile test? No. The $t$-test is a test about the mean, which is unrelated to $\xi_{0.25}$ without a parametric model. The signed-rank test requires the distribution to be symmetric about the hypothesized value, and a distribution symmetric about $Q_0$ has $Q_0$ as its median, not as its lower quartile. The binomial count is the only one of the three whose null distribution is known when the hypothesis concerns a quantile of order $q\ne1/2$.

### 7.2.2. Confidence Intervals for a Quantile

Inverting the quantile test gives an interval whose end points are **order statistics**, exactly as for the median.

**Proposition 7.2.1** Let $X_1,\dots,X_n$ be i.i.d. from a continuous distribution with $q$-quantile $\xi_q$, and let $B\sim\mathrm{Bin}(n,q)$. For integers $1\le r<s\le n$,

$$
\mathbb{P}\bigl(X_{(r)}\le\xi_q<X_{(s)}\bigr)=\mathbb{P}(r\le B\le s-1)=\sum_{k=r}^{s-1}\binom{n}{k}q^k(1-q)^{n-k}.
$$
This does not depend on $F$, so $[X_{(r)},X_{(s)}]$ is a distribution-free confidence interval for $\xi_q$.

**Proof** Let $B=\#\{i\colon X_i\le\xi_q\}\sim\mathrm{Bin}(n,q)$. Then $X_{(r)}\le\xi_q$ if and only if at least $r$ observations are at most $\xi_q$, that is, $B\ge r$; and $\xi_q<X_{(s)}$ if and only if fewer than $s$ observations are at most $\xi_q$, that is, $B\le s-1$. $\square$

In practice $r$ and $s$ are chosen so that $\mathbb{P}(B\le r-1)\le\alpha/2$ and $\mathbb{P}(B\ge s)\le\alpha/2$, as close to $\alpha/2$ as the discreteness permits. Because the distribution of the order statistics is continuous, whether the end points are included does not matter.

**Example 7.2.2** For the water content data of Example 7.1.1, a $95\%$ interval for the upper quartile $\xi_{0.75}$ uses $B\sim\mathrm{Bin}(20,0.75)$. With $r=11$, $s=19$ we have $\mathbb{P}(B\le10)=0.014$ and $\mathbb{P}(B\ge19)=0.024$, so

$$
[x_{(11)},x_{(19)}]=[8.1,\ 14.3]
$$
has coverage $0.962$. The interval is very asymmetric about the sample upper quartile, because the upper tail of the sample is sparse: an upper-quartile interval for $20$ observations is bound to reach into the two largest values.

## 7.3. The Cox–Stuart Test for Trend

### 7.3.1. Comparing Observations at a Lag

When observations are made in time order, a common question is whether they show a trend or fluctuate randomly about a constant level.

**Example 7.3.1 (Annual Mileages)** The mean annual mileages (in thousands of miles) of cars and trucks for the years 1970–83, were:

| Year | 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cars | 9.8 | 9.9 | 10.0 | 9.8 | 9.2 | 9.4 | 9.5 | 9.6 | 9.8 | 9.3 | 8.9 | 8.7 | 9.2 | 9.3 |
| Trucks | 11.5 | 11.5 | 12.2 | 11.5 | 10.9 | 10.6 | 11.1 | 11.1 | 11.0 | 10.8 | 11.4 | 12.3 | 11.2 | 11.2 |

Is there evidence of a monotone trend in either series? Since we have no prior direction, a two-sided test is appropriate.

A first idea is to look at year-to-year changes $x_{i+1}-x_i$. For the cars they are $0.1,0.1,-0.2,-0.6,0.2,0.1,0.1,0.2,-0.5,-0.4,-0.2,0.5,0.1$: eight increases and five decreases, and a sign test gives $p=0.58$. Year-to-year changes are dominated by noise. Comparing observations $k$ years apart, for $k=1,\dots,7$, gives

| Lag $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Nonzero differences | 13 | 12 | 10 | 9 | 8 | 8 | 7 |
| Decreases | 5 | 6 | 7 | 8 | 7 | 8 | 7 |
| Sign-test $p$-value | 0.58 | 1.00 | 0.34 | 0.039 | 0.070 | 0.0078 | 0.016 |

As the lag grows, a systematic drift accumulates while the noise does not, and the evidence of a downward trend becomes clear. But only the largest lag gives a valid test: for $k<7$ the pairs $(x_i,x_{i+k})$ overlap (each observation enters two differences), so the differences are not independent and the binomial null distribution is wrong. At lag $n/2$ every observation is used exactly once.
:::

### 7.3.2. The Test

**Definition 7.3.1 (Cox–Stuart Test)** Let $x_1,\dots,x_n$ be observations in time order. If $n=2m$, form the $m$ differences

$$
x_{m+1}-x_1,\ x_{m+2}-x_2,\ \dots,\ x_{2m}-x_m ;
$$
if $n=2m+1$, omit the middle value $x_{m+1}$ and form $x_{m+2}-x_1,\dots,x_{2m+1}-x_m$. Discard zero differences, leaving $m'$ of them. The **Cox–Stuart test** (Cox and Stuart 1955) of $H_0$: no trend, against an increasing (decreasing) trend, is the sign test applied to these differences: under $H_0$ the number of positive differences is $\mathrm{Bin}(m',1/2)$, and many positive (negative) signs indicate an increasing (decreasing) trend.

The conditions are those of a sign test on the pairs:

1. the pairs $(X_i,X_{i+m})$ are mutually independent;
2. under $H_1$ the direction is consistent: $\mathbb{P}(X_i<X_{i+m})$ exceeds $\mathbb{P}(X_i>X_{i+m})$ for all pairs (or falls below it for all pairs);
3. each pair can be judged as a plus, a minus or a tie.

A null hypothesis that implies $\mathbb{P}(X_i<X_{i+m})=\mathbb{P}(X_i>X_{i+m})$ for every pair is enough; the classical one is that $X_1,\dots,X_n$ are i.i.d. The observations need not be normal, and a trend need not be linear.

**Example 7.3.2 (Annual Mileages, Continued)** For the cars, $m=7$ and the differences are

$$
9.6-9.8,\ 9.8-9.9,\ 9.3-10.0,\ 8.9-9.8,\ 8.7-9.2,\ 9.2-9.4,\ 9.3-9.5 ,
$$
all negative. The two-sided $p$-value is $2\times2^{-7}=0.016$: there is strong evidence of a downward trend in car mileages.

For the trucks the seven differences have signs $-,-,-,-,+,+,+$: three plus and four minus signs, $p=1$. This is the strongest possible support for "no monotone trend". But the pattern of signs is itself informative: the first four differences are negative and the last three positive, which suggests a decrease followed by an increase rather than random fluctuation. A test of no monotone trend cannot see a U-shape.

```r
cox_stuart <- function(x) {
  n <- length(x); m <- n %/% 2
  d <- x[(n - m + 1):n] - x[1:m]     # drops the middle value when n is odd
  d <- d[d != 0]
  binom.test(sum(d > 0), length(d))
}
cox_stuart(cars)     # p-value = 0.01562
cox_stuart(trucks)   # p-value = 1
```

The inference is about the vehicles sampled: if different vehicles were sampled independently each year, the yearly means are independent; if the same vehicles were followed over the years, the conclusion would apply only to that fleet.
:::

![Cox–Stuart pairing for the mileage data. Each arrow joins the value of a year to the value seven years later; blue arrows are increases and red arrows decreases. All seven car pairs decrease, while the truck pairs decrease in the first half and increase in the second.](./plots/cox-stuart-cars.py)

**Remark 7.3.1** The Cox–Stuart test compares the second half of the series with the first half, pair by pair. It therefore detects whether later values tend to be larger than earlier ones, not whether the series is monotone: a series that rises, falls back and rises again can give the same signs as a steadily rising one, and a series that falls and then rises (as the trucks) can give no evidence at all. A plot of the series should precede the test; if it is not monotone, a specific pattern has to be formulated and tested, as in the next subsection.

### 7.3.3. Periodic and Specified Trends

Many series have a cyclic component. Mean weekly temperature, for example, rises from February to July and falls from August to January; pairing observations half a series apart can then pair rising with falling stretches, and the Cox–Stuart test misses the trend. Two devices handle such cases.

The first is to pair observations that are a whole cycle apart. Suppose the monthly average discharge of a stream is recorded for $24$ months and we wish to test

$$
H_0\colon \text{the rate of discharge is not decreasing}\quad\text{vs.}\quad H_1\colon\text{it is decreasing}.
$$
Discharge follows a yearly cycle, so comparing two different months tells us nothing. Pairing each month of the first year with the same month of the second year removes the seasonal pattern, and a one-sided sign test on the $12$ differences tests the trend. This is the Cox–Stuart test with the lag equal to the period.

The second device applies when the alternative specifies a pattern. Then the data are rearranged so that, under $H_1$, the rearranged sequence should increase, and the one-sided Cox–Stuart test is applied to it.

**Example 7.3.3 (Egg Laying)** The numbers of eggs laid by a group of insects are counted every hour during a $24$-hour experiment. The hypotheses are

- $H_0$: the $24$ counts are observations of $24$ identically distributed random variables;
- $H_1$: egg laying is least around 2:15 p.m., increases to a maximum around 2:15 a.m., and decreases again to 2:15 p.m.

Under $H_1$, counts recorded nearest 2:15 p.m. should be smallest and those nearest 2:15 a.m. largest. Ordering the hours by their distance from 2:15 p.m. (2 p.m., 3 p.m., 1 p.m., 4 p.m., noon, and so on, up to 2 a.m.) should therefore produce an increasing sequence. The first half of the rearranged sequence is paired with the second half:

| Time | Eggs | Time | Eggs |
|---|---|---|---|
| 2 p.m. | 84 | 8 a.m. | 137 |
| 3 p.m. | 60 | 9 p.m. | 163 |
| 1 p.m. | 63 | 7 a.m. | 139 |
| 4 p.m. | 109 | 10 p.m. | 208 |
| Noon | 111 | 6 a.m. | 174 |
| 5 p.m. | 83 | 11 p.m. | 283 |
| 11 a.m. | 146 | 5 a.m. | 176 |
| 6 p.m. | 166 | Midnight | 296 |
| 10 a.m. | 119 | 4 a.m. | 176 |
| 7 p.m. | 143 | 1 a.m. | 286 |
| 9 a.m. | 151 | 3 a.m. | 223 |
| 8 p.m. | 116 | 2 a.m. | 235 |

In all $12$ pairs the count in the right column exceeds that in the left. The one-sided $p$-value is $2^{-12}=0.0002$ (`binom.test(12, 12, alternative = "greater")`), and we conclude that the predicted daily pattern is present.
:::

**Remark 7.3.2** The pattern must be specified before the data are examined, as in Example 7.3.3, where it came from knowledge of the insects. It is tempting, after seeing the truck mileages of Example 7.3.2 fall and then rise, to rearrange them around the minimum and test the U-shape on the same data; but a pattern suggested by the data is guaranteed to look supported by them, and the resulting $p$-value has no meaning. Such a pattern is a hypothesis for the next data set.

## 7.4. The Runs Test for Randomness

### 7.4.1. Runs

Most inferences in this course assume that the data are an independent random sample. How can independence itself be tested? Consider three sequences of $20$ coin tosses:

1. H H H H H T T T T T T T T T T H H H H H
2. H T H T H T H T H T H T H T H T H T H T
3. H H T H T T T H T H H T H T H H H T T H

Few people would accept the first two as random, although each has about equally many heads and tails. What distinguishes them is how the symbols are grouped.

**Definition 7.4.1 (Run)** In a sequence of symbols of two (or more) kinds, a **run** is a maximal block of consecutive identical symbols. The number of runs is denoted $R$.

The first sequence has $R=3$ runs (five heads, ten tails, five heads), too few for a random sequence: like symbols cluster. The second has $R=20$, too many: the symbols alternate. The third has $R=13$, an intermediate number. Too few runs indicate positive dependence, clustering or a trend; too many indicate negative dependence or systematic alternation.

Throughout, the sequence consists of $N$ ordered observations, $m$ of one kind and $n=N-m$ of the other. The null hypothesis of randomness is taken in the conditional form: given $m$ and $n$, all $\binom{N}{m}$ arrangements of the symbols are equally likely. This holds when the observations are i.i.d. (in particular for independent tosses with any probability of heads), and more generally when they are **exchangeable**.

### 7.4.2. The Exact Null Distribution

**Theorem 7.4.1** Under the null hypothesis of randomness, for $s\ge1$,

$$
\mathbb{P}(R=2s)=\frac{2\dbinom{m-1}{s-1}\dbinom{n-1}{s-1}}{\dbinom{N}{m}},\qquad
\mathbb{P}(R=2s+1)=\frac{\dbinom{m-1}{s-1}\dbinom{n-1}{s}+\dbinom{m-1}{s}\dbinom{n-1}{s-1}}{\dbinom{N}{m}}.
$$

**Proof** Call the two kinds $X$ and $Y$. Runs of $X$ and runs of $Y$ alternate. An even number $R=2s$ of runs means $s$ runs of each kind, and the sequence starts with either kind ($2$ ways). Splitting $m$ symbols $X$ into $s$ nonempty runs amounts to choosing $s-1$ of the $m-1$ gaps between consecutive $X$'s as break points: $\binom{m-1}{s-1}$ ways; similarly $\binom{n-1}{s-1}$ ways for $Y$. The multiplication rule gives the numerator. An odd number $R=2s+1$ means either $s+1$ runs of $X$ and $s$ runs of $Y$ (the sequence starts and ends with $X$), in $\binom{m-1}{s}\binom{n-1}{s-1}$ ways, or $s$ runs of $X$ and $s+1$ of $Y$, in $\binom{m-1}{s-1}\binom{n-1}{s}$ ways. Dividing by the number $\binom{N}{m}$ of equally likely arrangements completes the proof. $\square$

For example, HHTTTHHH ($N=8$, $m=5$, $n=3$) has $R=3$, $s=1$; HHTTTHHHT ($N=9$, $m=5$, $n=4$) has $R=4$, $s=2$. Tables of the tail probabilities for $m,n\le20$ go back to Swed and Eisenhart (1943); today they are computed directly from Theorem 7.4.1.

### 7.4.3. Mean, Variance and the Normal Approximation

**Theorem 7.4.2** Under the null hypothesis of randomness,

$$
\mathbb{E}R=1+\frac{2mn}{N},\qquad
\operatorname{Var}(R)=\frac{2mn(2mn-N)}{N^2(N-1)},
$$
and if $m,n\to\infty$ with $m/N$ bounded away from $0$ and $1$, $(R-\mathbb{E}R)/\sqrt{\operatorname{Var}(R)}\xrightarrow{d}\mathcal{N}(0,1)$.

**Proof** Let $I_j$ be the indicator that the $j$th and $(j+1)$th symbols differ, $j=1,\dots,N-1$. Every change of symbol starts a new run, so $R=1+\sum_{j=1}^{N-1}I_j$. Under randomness the symbols at any fixed positions are a sample without replacement from the $N$ symbols. Hence

$$
\mathbb{P}(I_j=1)=2\cdot\frac{m}{N}\cdot\frac{n}{N-1},\qquad
\mathbb{E}R=1+(N-1)\frac{2mn}{N(N-1)}=1+\frac{2mn}{N}.
$$
For the variance write $T=R-1=\sum_jI_j$, so $\operatorname{Var}(R)=\mathbb{E}T^2-(\mathbb{E}T)^2$ with $\mathbb{E}T^2=\mathbb{E}T+2\sum_{j<k}\mathbb{E}I_jI_k$. Two kinds of pairs occur.

- Adjacent indicators ($k=j+1$, $N-2$ pairs): $I_jI_{j+1}=1$ means that three consecutive symbols alternate, $XYX$ or $YXY$, with probability
  $\dfrac{mn(m-1)+nm(n-1)}{N(N-1)(N-2)}=\dfrac{mn}{N(N-1)}$.
- Non-adjacent indicators ($k\ge j+2$, $(N-2)(N-3)/2$ pairs): the two pairs of positions are disjoint and each must contain one $X$ and one $Y$, with probability
  $\dfrac{4mn(m-1)(n-1)}{N(N-1)(N-2)(N-3)}$.

Therefore

$$
\mathbb{E}T^2=\frac{2mn}{N}+\frac{2mn(N-2)}{N(N-1)}+\frac{4mn(m-1)(n-1)}{N(N-1)},
$$
and subtracting $(2mn/N)^2$ and simplifying gives the stated variance. The asymptotic normality is due to Wald and Wolfowitz (1940); we do not prove it. $\square$

**Definition 7.4.2 (Runs Test)** The **runs test** of the hypothesis that a two-symbol sequence is random rejects for small values of $R$ (against clustering or trend), for large values (against alternation), or for both (two-sided). The $p$-value is computed from Theorem 7.4.1, or for large samples from the normal approximation of Theorem 7.4.2 with a **continuity correction**: add $0.5$ to $R$ if $R<\mathbb{E}R$ and subtract $0.5$ if $R>\mathbb{E}R$. The approximation is customarily considered adequate when $m\ge10$ and $n\ge10$.

**Example 7.4.1 (Coin Tosses)** For the first two sequences of Section 7.4.1, $N=20$ and $m=n=10$, so $\mathbb{E}R=11$ and $\operatorname{Var}(R)=4.74$. From the exact distribution, $\mathbb{P}(R\le6)=\mathbb{P}(R\ge16)=0.0185$ and $\mathbb{P}(R\le7)=0.051$; a two-sided test at level $0.05$ accepts randomness for $7\le R\le15$ (actual size $0.037$). For the third sequence $m=11$, $n=9$. The two-sided $p$-values are:

| Sequence | $R$ | Exact | Normal approximation |
|---|---|---|---|
| I: H H H H H T T T T T T T T T T H H H H H | 3 | 0.0002 | 0.0006 |
| II: H T H T H T H T H T H T H T H T H T H T | 20 | $<0.0001$ | 0.0001 |
| III: H H T H T T T H T H H T H T H H H T T H | 13 | 0.454 | 0.457 |

There is strong evidence of nonrandomness in the first two sequences (clustering, then alternation) and none in the third.
:::

![Exact null distribution of the number of runs for $m=n=10$, with the normal approximation. The red bars form the two-sided rejection region at level $0.05$; the observed values of the three coin sequences are marked.](./plots/runs-null.py)

**Remark 7.4.1** Three points about the runs test.

1. The null hypothesis is randomness (the sequence is an exchangeable arrangement), and the alternative is nonrandomness; a large $p$-value does not prove randomness, it only fails to find evidence against it.
2. The test does not require $\mathbb{P}(\mathrm{H})=\mathbb{P}(\mathrm{T})=1/2$. Because it conditions on the observed numbers $m$ and $n$, its null distribution is the same for a biased coin. Whether the coin is fair is a separate question, answered by a binomial test of the frequencies.
3. Numerical data are reduced to two symbols by recording whether each observation lies above or below the sample median (values equal to the median are dropped). Few runs then indicate a trend or slow oscillation, many runs rapid oscillation. [3.6.8](/3.6.8) uses this device to test correlation, and [3.6.10](/3.6.10) uses runs in the pooled ordering of two samples to compare distributions.

### 7.4.4. More Than Two Categories

With $k\ge3$ categories the number of runs is defined in the same way. Let category $i$ occur $n_i$ times, $\sum_in_i=N$, and write $p_i=n_i/N$.

**Theorem 7.4.3** Under randomness (all arrangements of the given multiset equally likely),

$$
\mathbb{E}R=1+\frac{N^2-\sum_in_i^2}{N}=N\Bigl(1-\sum_{i=1}^kp_i^2\Bigr)+1,
$$
$$
\operatorname{Var}(R)=\frac{\sum_in_i^2\bigl(\sum_in_i^2+N(N+1)\bigr)-2N\sum_in_i^3-N^3}{N^2(N-1)} .
$$
For large $N$ the variance is approximately $N\bigl[\sum_i(p_i^2-2p_i^3)+(\sum_ip_i^2)^2\bigr]$, and $R$ is approximately normal.

**Proof** As before $R=1+\sum_{j=1}^{N-1}I_j$, and two fixed positions hold different categories with probability $\sum_{i\ne l}n_in_l/(N(N-1))=(N^2-\sum_in_i^2)/(N(N-1))$; this gives the mean. The variance follows from the same decomposition into adjacent and non-adjacent pairs of indicators as in Theorem 7.4.2, with sums over categories; we omit the algebra. For $k=2$ both formulas reduce to those of Theorem 7.4.2. $\square$

Barton and David (1957) suggested that the normal approximation is adequate for $N>12$ whatever the $n_i$. With one dominant category and small $N$, however, the distribution of $R$ is lumpy, and an exact or Monte Carlo $p$-value from random permutations of the observed sequence is easy to obtain and preferable.

**Example 7.4.2 (Methods of Delivery)** The methods of delivery for $17$ consecutive births in a London hospital were

$$
\mathrm{A\,A\,A\,A\,B\,A\,C\,C\,A\,A\,A\,A\,A\,D\,D\,A\,A},
$$
where A is a normal delivery, B forceps, C an elective Caesarean and D an emergency Caesarean. Is the method of delivery clustered in time? Here $N=17$, $k=4$, $n_{\mathrm{A}}=12$, $n_{\mathrm{B}}=1$, $n_{\mathrm{C}}=n_{\mathrm{D}}=2$, and $R=7$. Only clustering (few runs) is of interest, so the test is one-sided.

The mean is $\mathbb{E}R=1+(289-153)/17=9.0$. The large-sample variance is $1.689$, and $\Phi\bigl((7-9)/\sqrt{1.689}\bigr)=0.062$. The exact conditional variance from Theorem 7.4.3 is smaller, $1.294$, and the exact $p$-value, obtained by enumerating all $17!/(12!\,1!\,2!\,2!)=185\,640$ arrangements, is $\mathbb{P}(R\le7)=0.097$ (the normal approximation with the exact variance and a continuity correction gives $0.094$). Either way there is at most weak evidence of clustering in this short series.
:::

**Remark 7.4.2** Runs are a basic tool for testing **pseudorandom number generators**, which produce streams of bits. Test suites such as NIST SP 800-22, Dieharder and TestU01 contain a frequency test (are $0$s and $1$s equally frequent), a runs test (is the number of runs of identical bits as expected), a test of the longest run of ones in a block, and many others (binary matrix rank, template matching, and so on). Each detects a different kind of departure; no finite battery certifies a generator as random.

## 7.5. Angular Data

### 7.5.1. Why Linear Statistics Fail

The arithmetic mean of the angles $1^\circ$ and $359^\circ$ is $180^\circ$, yet both directions point almost due north and geometrically their mean ought to be $0^\circ$.

**Definition 7.5.1 (Circular Data)** Observations that are directions, represented as angles in $[0^\circ,360^\circ)$ or points on the unit circle, are called **circular data** (directional or angular data). Times on a periodic scale, such as the hour of the day or the day of the year, are circular data after the conversion $\theta=2\pi t/T$ with period $T$.

Examples are wind directions, the orientation of migrating animals, palaeomagnetic directions in rocks, the positions on a roulette wheel and the times of day at which events occur. The defining feature is that the scale is closed: $0^\circ$ and $360^\circ$ are the same point, and the choice of the zero direction is arbitrary. Gauss's linear theory of errors, built for astronomical observations, treats angles as numbers on a line; this works when all the observations lie in a short arc and the errors are small enough to be linearized, but it gives absurd results when the data spread around the circle. Statistics for circular data must not depend on the choice of origin. For instance, the natural location summary is the *mean direction*, the direction of the resultant vector

$$
\bar\theta=\operatorname{atan2}\Bigl(\sum_i\sin\theta_i,\ \sum_i\cos\theta_i\Bigr),
$$
which gives $0^\circ$ for $1^\circ$ and $359^\circ$ and rotates with the data when the origin is changed.

### 7.5.2. Testing Uniformity on the Circle

**Example 7.5.1 (Times of Birth)** The times of birth of $12$ consecutive home deliveries were

$$
01{:}00,\ 03{:}00,\ 04{:}20,\ 05{:}00,\ 05{:}40,\ 06{:}20,\ 06{:}40,\ 07{:}00,\ 09{:}40,\ 11{:}00,\ 12{:}00,\ 17{:}20 .
$$
Do births tend to occur at particular times of day? On a $24$-hour clock one hour corresponds to $15^\circ$, and the null hypothesis is that the times are uniformly distributed around the circle.

Two "uniform distributions" must be distinguished. The linear uniform distribution $\mathrm{U}(0,24)$ has distribution function $F_0(x)=x/24$ on $(0,24)$ and treats time as a segment with two separate ends. The circular uniform distribution has no end points: for every arc, including arcs that wrap around midnight such as from 23:00 to 01:00, the probability is the arc length divided by $24$ hours.

Applying the **Kolmogorov–Smirnov test** to the times measured from midnight, with $U_i=t_i/24$,

```r
x <- c("01:00", "03:00", "04:20", "05:00", "05:40", "06:20",
       "06:40", "07:00", "09:40", "11:00", "12:00", "17:20")
tm <- as.POSIXlt(paste(Sys.Date(), x))
hours <- tm$hour + tm$min / 60
theta <- hours * 2 * pi / 24
ks.test(theta, punif, min = 0, max = 2 * pi)
```

```text
D = 0.41667, p-value = 0.02115
```

suggests that births are not uniform. But midnight is an arbitrary origin. Measuring time from other origins gives:

| Origin | $D_n^+$ | $D_n^-$ | $D_n=\max(D_n^+,D_n^-)$ | KS $p$-value | $D_n^++D_n^-$ |
|---|---|---|---|---|---|
| 00:00 | 0.417 | 0.042 | 0.417 | 0.021 | 0.458 |
| 06:00 | 0.250 | 0.208 | 0.250 | 0.378 | 0.458 |
| 12:00 | 0.083 | 0.375 | 0.375 | 0.050 | 0.458 |
| 18:00 | 0.167 | 0.292 | 0.292 | 0.213 | 0.458 |

The same data are "significant" or not depending on where the clock is started. The last column, however, does not change.
:::

### 7.5.3. Kuiper's Test

Write the one-sided Kolmogorov distances ([3.6.6](/3.6.6)) in terms of the ordered transformed values $U_{(1)}\le\dots\le U_{(n)}$, $U_i=F_0(\theta_i)$:

$$
D_n^+=\sup_x\bigl(F_n(x)-F_0(x)\bigr)=\max_{1\le i\le n}\Bigl(\frac in-U_{(i)}\Bigr),\qquad
D_n^-=\sup_x\bigl(F_0(x)-F_n(x)\bigr)=\max_{1\le i\le n}\Bigl(U_{(i)}-\frac{i-1}n\Bigr).
$$

**Definition 7.5.2 (Kuiper's Test)** For circular data and a continuous hypothesized distribution $F_0$ on the circle (for uniformity, $F_0(\theta)=\theta/(2\pi)$, $0<\theta\le2\pi$), **Kuiper's test** (Kuiper 1960) of $H_0\colon F=F_0$ against $H_1\colon F\ne F_0$ uses

$$
V_n=D_n^++D_n^-
$$
and rejects for large values. Under $H_0$, $V_n$ is distribution-free (it is a function of the uniform variables $U_i$), and critical values are tabulated.

The two one-sided distances measure the largest excess of the empirical over the hypothesized distribution and the largest deficit. Rotating the origin changes how the circle is cut open, which shifts the empirical-minus-hypothesized curve up or down by a constant; the excess and the deficit trade value, but their sum does not change.

**Theorem 7.5.1** $V_n$ does not depend on the choice of the zero direction, whereas $D_n=\max(D_n^+,D_n^-)$ in general does.

**Proof** Measure angles in units of a full turn, so that $F_0(u)=u$ on $[0,1)$. Extend the empirical distribution function to the real line by $F_n(u+1)=F_n(u)+1$; then $G(u)=F_n(u)-u$ is periodic with period $1$. If the origin is moved to the point $c$, the empirical distribution function of the rotated data is $F_n^{(c)}(t)=F_n(c+t)-F_n(c)$, $0\le t<1$, so

$$
F_n^{(c)}(t)-t=G(c+t)-G(c).
$$
Hence the rotated distances are $D_n^{+(c)}=\sup G-G(c)$ and $D_n^{-(c)}=G(c)-\inf G$, the suprema being over a full period (with the usual one-sided limits at the jumps). Their sum $\sup G-\inf G$ does not involve $c$, while each of them, and hence their maximum, does. $\square$

**Example 7.5.2 (Two Directions)** Take $\theta_1=80^\circ$, $\theta_2=100^\circ$. Starting from $0^\circ$, $U_{(1)}=80/360=0.222$ and $U_{(2)}=0.278$, so

$$
D_n^+=\max(0.5-0.222,\ 1-0.278)=0.722,\qquad D_n^-=\max(0.222-0,\ 0.278-0.5)=0.222 .
$$
Starting from $180^\circ$, $U_{(1)}=0.722$, $U_{(2)}=0.778$, and the values swap: $D_n^+=0.222$, $D_n^-=0.722$. Starting from $90^\circ$ ($U_{(1)}=0.472$, $U_{(2)}=0.528$), $D_n^+=D_n^-=0.472$. In every case $V_n=0.944$, while $D_n$ is $0.722$, $0.722$ and $0.472$.

:::

The asymptotic null distribution of $\sqrt n\,V_n$ is

$$
\mathbb{P}\bigl(\sqrt n\,V_n>z\bigr)=2\sum_{j=1}^\infty(4j^2z^2-1)\,\mathrm{e}^{-2j^2z^2}-\frac{8z}{3\sqrt n}\sum_{j=1}^\infty j^2(4j^2z^2-3)\,\mathrm{e}^{-2j^2z^2}+O(n^{-1}) ,
$$
and for $z>1.2$ the first term of each series already gives a good approximation. A convenient alternative (Stephens 1970) evaluates the first series at $(\sqrt n+0.155+0.24/\sqrt n)\,V_n$.

**Example 7.5.3 (Times of Birth, Continued)** For the birth times, $V_n=0.4583$ and $z=\sqrt{12}\times0.4583=1.588>1.2$.

```r
n <- length(theta)
u <- sort(theta / (2 * pi))
dplus <- max((1:n) / n - u)
dminus <- max(u - (0:(n - 1)) / n)
z <- (dplus + dminus) * sqrt(n)                  # 1.5877
2 * (4 * z^2 - 1) * exp(-2 * z^2) - 8 * z / (3 * sqrt(n)) * (4 * z^2 - 3) * exp(-2 * z^2)

library(circular)
kuiper.test(circular(theta), alpha = 0.05)
```

```text
[1] 0.06145804
```

The asymptotic $p$-value is $0.061$ (Stephens' approximation gives $0.069$, and a Monte Carlo simulation of $V_{12}$ under uniformity about $0.067$). In contrast with the Kolmogorov–Smirnov result from midnight, there is only weak evidence that births concentrate at particular times of day; the small sample is the main limitation.
:::

![Left: the $12$ birth times on a $24$-hour clock. Right: as the origin of the clock moves through the day, the Kolmogorov statistic $D_n$ (red) and its one-sided parts change, while Kuiper's $V_n=D_n^++D_n^-$ (orange, dashed) stays at $0.458$.](./plots/circular-births.py)

### 7.5.4. Other Questions about Directions

Uniformity is only one question. If the question is whether directions are symmetric about a known direction $\theta_0$, the data can be linearized: rotate so that $\theta_0$ becomes $0$, map each angle into $(-180^\circ,180^\circ]$, and apply the sign test or the Wilcoxon signed-rank test to the resulting signed values. This is legitimate because the hypothesis fixes the origin. If the centre is unknown, genuinely circular methods are needed, such as Watson's $U^2$ test (another rotation-invariant relative of the Cramér–von Mises statistic, available as `watson.test` in the `circular` package for uniformity or for a fitted von Mises distribution) and tests based on the von Mises distribution, the circular analogue of the normal distribution.

```r
theta <- c(80, 100, 350, 10, 90, 270)            # degrees
theta0 <- 0                                      # known centre
a <- (theta - theta0) %% 360
x <- ifelse(a <= 180, a, a - 360)                # signed deviations in (-180, 180]
binom.test(sum(x > 0), sum(x != 0))              # sign test
wilcox.test(x, mu = 0)                           # signed-rank test

library(circular)
watson.test(circular(theta, units = "degrees"))  # Watson's U2 test of uniformity
```

Standard references for circular statistics are the monographs of Mardia (1972; with Jupp, 2000) and N. I. Fisher (1993).

## Summary

- Many one-sample problems reduce to counting signs and a binomial test:

  | Question | Signs counted | Null distribution |
  |---|---|---|
  | Median $=\theta_0$ (sign test) | observations below $\theta_0$ | $\mathrm{Bin}(n,1/2)$ |
  | $q$-quantile $=Q_0$ (Definition 7.2.1) | observations below $Q_0$ | $\mathrm{Bin}(n,q)$ |
  | Monotone trend (Definition 7.3.1) | increases in the pairs $(x_i,x_{i+m})$, $m=\lfloor n/2\rfloor$ | $\mathrm{Bin}(m',1/2)$ |
  | Periodic trend | increases between observations one period apart | $\mathrm{Bin}(m',1/2)$ |
  | Specified pattern | Cox–Stuart on data rearranged to increase under $H_1$ | $\mathrm{Bin}(m',1/2)$ |

- Confidence intervals for quantiles have order statistics as end points, with coverage $\mathbb{P}(r\le B\le s-1)$, $B\sim\mathrm{Bin}(n,q)$ (Proposition 7.2.1). The $t$-test and the signed-rank test do not apply to quantiles other than the median (Remark 7.2.1).
- The Cox–Stuart test uses only the lag $n/2$ because only then are the pairs disjoint; it detects "later values larger", not monotonicity, so plot first (Remark 7.3.1), and specify any non-monotone pattern before seeing the data (Remark 7.3.2).
- Runs test (Definition 7.4.2): conditional on the counts, $R$ has the distribution of Theorem 7.4.1, with $\mathbb{E}R=1+2mn/N$ and $\operatorname{Var}(R)=2mn(2mn-N)/\bigl(N^2(N-1)\bigr)$ (Theorem 7.4.2, by indicators of symbol changes); normal approximation with continuity correction for $m,n\ge10$. Too few runs mean clustering or trend, too many alternation. For $k$ categories $\mathbb{E}R=N(1-\sum p_i^2)+1$ (Theorem 7.4.3); in small samples use exact or Monte Carlo $p$-values.
- Circular data (Definition 7.5.1) need statistics that do not depend on the origin. The Kolmogorov statistic does; Kuiper's $V_n=D_n^++D_n^-$ does not (Theorem 7.5.1) and is distribution-free under $H_0$ (Definition 7.5.2).

## Questions

1. In Example 7.3.1, why does the sign test on lag-$1$ differences have so little power, and why is it not valid to pick the lag with the smallest $p$-value?

   **Answer** Year-to-year changes are dominated by random variation, while a slow trend contributes only a small amount to each change; at lag $k$ the trend contributes $k$ times as much, the noise not more, so the signs become more informative. But the $p$-values in the table are not those of valid tests for $k<7$, because overlapping pairs give dependent differences; and choosing the lag after seeing seven $p$-values is a multiple-testing procedure whose overall error rate exceeds the nominal level. The Cox–Stuart rule fixes the lag at $n/2$ in advance.
2. A quality control engineer measures the thickness (mm) of $12$ consecutive glass panels: $4.1, 4.3, 4.4, 3.9, 3.8, 4.2, 4.5, 4.6, 3.7, 3.6, 4.0, 4.7$. Dichotomize at the sample median and test randomness of the sequence with the runs test.

   **Answer** The sample median is $(4.1+4.2)/2=4.15$. Writing $+$ above and $-$ below it, the sequence is $-\,+\,+\,-\,-\,+\,+\,+\,-\,-\,-\,+$, with $m=n=6$ and $R=6$ runs. Under randomness $\mathbb{E}R=1+2\cdot36/12=7$; from Theorem 7.4.1, $\mathbb{P}(R\le6)=0.392$, so the two-sided $p$-value is about $0.78$. There is no evidence against randomness. (The samples are below the size $m,n\ge10$ at which the normal approximation is customary; the exact distribution should be used.)
3. Show that the variance in Theorem 7.4.2 is at most about $N/4$ and explain why the runs test can have little power against a slow trend when the sequence is long.

   **Answer** With $m=n=N/2$, $\operatorname{Var}(R)=\tfrac{N}{2}\cdot\tfrac{N/2-1}{N-1}\approx N/4$, and this is the maximum over $m$ for fixed $N$ (the expression increases in $mn$ for $mn>N/4$). A slow monotone trend, dichotomized at the median, produces one long block of $-$ followed by one of $+$, which the runs test detects very well. A trend that is small relative to the noise, however, only reduces the expected number of runs slightly, by an amount that is small relative to $\sqrt{N}/2$; tests that use the direction of the trend, such as the Cox–Stuart test or a rank correlation with time, are more powerful against it, because the runs test spends its power on all kinds of departures from randomness.
4. The initial flight directions of $8$ released homing pigeons are $345^\circ, 350^\circ, 355^\circ, 5^\circ, 10^\circ, 15^\circ, 25^\circ, 30^\circ$ ($0^\circ$ is north). (a) What is the range if the data are treated as numbers? (b) What is the length of the smallest arc containing all the points (the circular range)? (c) Test uniformity with Kuiper's test.

   **Answer** (a) $355-5=350^\circ$, which suggests directions spread almost all around the circle. (b) The points lie in the arc from $345^\circ$ clockwise to $30^\circ$, of length $45^\circ$: the pigeons fly in a narrow band around north, and the linear range is meaningless. (c) With $U_i=\theta_i/360$ sorted, $D_n^+=0.542$ and $D_n^-=0.333$, so $V_8=0.875$ and $\sqrt8\,V_8=2.47$. The asymptotic $p$-value (Stephens' version) is about $3\times10^{-5}$, and a simulation of $V_8$ under uniformity never exceeded $0.875$ in $200\,000$ trials. Uniformity is firmly rejected; the directions are concentrated.
5. Why does the runs test, applied to a sequence of heads and tails from a biased coin, still have the null distribution of Theorem 7.4.1?

   **Answer** For independent tosses with $\mathbb{P}(\mathrm{H})=p$, every particular sequence with $m$ heads and $n$ tails has probability $p^m(1-p)^n$, the same for all $\binom{N}{m}$ arrangements. Conditionally on $m$, all arrangements are therefore equally likely, whatever $p$ is, and Theorem 7.4.1 applies. The runs test examines the order of the symbols, not their frequencies.
