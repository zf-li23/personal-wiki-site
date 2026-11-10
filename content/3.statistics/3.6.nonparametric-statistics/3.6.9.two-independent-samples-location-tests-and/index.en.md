---
title: "Two Independent Samples: Location Tests and Estimates"
description: Comparing the centres of two independent samples without normality. The two-sample permutation test and the choice of statistic; the Wilcoxon–Mann–Whitney test (rank sums and the U statistic, exact and normal null distributions, ties); the confidence interval and Hodges–Lehmann estimate of a shift; what the WMW test really tests (location-shift model, stochastic equality and dominance, counterexamples); the Brunner–Munzel test; Mood's median test; bootstrapping the difference of medians; and how to choose among these methods.
---

Two independent random samples are drawn from two populations, and we want to know whether the populations differ, and in particular whether one tends to give larger values than the other. Under normality the answer is the two-sample $t$-test (3.2.5, [3.8.2](/3.8.2)). This chapter develops the distribution-free alternatives. The starting point is the two-sample permutation test of [3.6.1](/3.6.1): under the null hypothesis that the two populations are the same, the group labels are exchangeable. Replacing the observations by their ranks gives the Wilcoxon–Mann–Whitney (WMW) test, introduced briefly in 3.2.6, whose null distribution can be tabulated once and for all. Inverting it gives a confidence interval and a point estimate for a shift, exactly as the signed-rank test gave the Walsh-average interval and the Hodges–Lehmann estimate in the one-sample case ([3.6.4](/3.6.4), [3.6.5](/3.6.5)).

The central lesson of the chapter, however, is about interpretation. The WMW test is widely described as a test of equal medians, but it is one only under a location-shift model; in general it tests whether $\mathbb{P}(X>Y)=1/2$ (Section 9.5). This leads to the Brunner–Munzel test, which targets that hypothesis without assuming equal shapes, to Mood's median test, which targets medians, and to the bootstrap. Section 9.9 sets out how to choose. Comparisons of spread and of whole distributions follow in [3.6.10](/3.6.10), and more than two samples in [3.6.11](/3.6.11).

## 9.1. The Problem and the Classical Method

**Example 9.1.1 (Pocket Calculators)** Trigonometric function values can be obtained on two types of pocket calculator: on type A one enters the number before pressing the function key, on type B one selects the function first. A teacher wished to know whether type A allows calculations to be performed faster. Of $21$ pupils, $10$ used type A and $11$ type B, and the total times (minutes) to complete a set of calculations were:

| Group A | 23 | 18 | 17 | 25 | 22 | 19 | 31 | 26 | 29 | 33 | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Group B | 21 | 28 | 32 | 30 | 41 | 24 | 35 | 34 | 27 | 39 | 36 |

The hypotheses depend on the question. If it is "is one model superior?", the alternative is two-sided; if it is "does type A allow faster calculation?", it is one-sided, $H_1$: times with A tend to be smaller. The parameter (mean, median, or something else) is not yet specified: making it precise is one of the aims of this chapter.
:::

The classical analysis assumes $X_1,\dots,X_{n_1}\overset{\text{iid}}{\sim}\mathcal{N}(\mu_x,\sigma^2)$ independent of $Y_1,\dots,Y_{n_2}\overset{\text{iid}}{\sim}\mathcal{N}(\mu_y,\sigma^2)$, with parameter of interest $\theta=\mu_x-\mu_y$, estimate $\hat\theta=\bar X-\bar Y$ and statistic

$$
T=\frac{\bar X-\bar Y}{s_p\sqrt{1/n_1+1/n_2}},\qquad s_p^2=\frac{(n_1-1)s_x^2+(n_2-1)s_y^2}{n_1+n_2-2},
$$
which is $t_{n_1+n_2-2}$ under $H_0\colon\theta=0$; the $1-\alpha$ interval is $\bar X-\bar Y\pm t_{n_1+n_2-2,\alpha/2}\,s_p\sqrt{1/n_1+1/n_2}$. **Welch's t-test** drops the equal-variance assumption. For the calculators, $\bar x=24.3$ and $\bar y=31.5$; the pooled test gives $t=-2.81$, $p=0.011$, and Welch's test $t=-2.83$, $p=0.011$. With samples of $10$ and $11$, the normality on which these $p$-values rest cannot be checked with any confidence.

## 9.2. The Two-Sample Permutation Test

If the two groups do not differ, that is, if the $n_1+n_2$ observations come from one distribution, then every partition of the pooled observations into a group of size $n_1$ and a group of size $n_2$ is equally likely to have been the observed one. There are

$$
K=\binom{n_1+n_2}{n_1}
$$
partitions, each giving a value $D_k$ of the chosen statistic; for the calculators $K=\binom{21}{10}=352\,716$. If $K$ is too large, a random sample of, say, $10\,000$ partitions is used. The $D_k$ form the permutation distribution, the reference distribution for the $p$-value: for a two-sided test based on a statistic centred at zero, the $p$-value is $\#\{k\colon\lvert D_k\rvert\ge\lvert D_{\mathrm{obs}}\rvert\}/K$. For the difference of means, $10^5$ random partitions give $p\approx0.014$ for the calculator data, close to the $t$-test.

Several statistics can be used, and some of them are equivalent.

**Proposition 9.2.1** Over the permutations of a fixed pooled sample, the difference of means $\bar X-\bar Y$, the sum $S_x$ of the observations in the first group, and the pooled two-sample $t$ statistic are increasing functions of one another, and therefore give the same permutation $p$-values.

**Proof** The total $S=S_x+S_y$ is the same for every partition, so

$$
\bar X-\bar Y=\frac{S_x}{n_1}-\frac{S-S_x}{n_2}=S_x\Bigl(\frac1{n_1}+\frac1{n_2}\Bigr)-\frac{S}{n_2},
$$
an increasing function of $S_x$. The total sum of squares $\mathrm{SS}_{\mathrm T}=\sum(\text{all observations}-\text{grand mean})^2$ is also fixed, and the within-group sum of squares is $\mathrm{SS}_{\mathrm T}-\frac{n_1n_2}{N}(\bar X-\bar Y)^2$ with $N=n_1+n_2$. Hence $T=c\,\Delta/\sqrt{\mathrm{SS}_{\mathrm T}-k\Delta^2}$ with $\Delta=\bar X-\bar Y$ and constants $c,k>0$, an increasing function of $\Delta$ on its range. $\square$

Different statistics make the test sensitive to different features. The difference of means is the usual choice and efficient for roughly normal data, but it is sensitive to unusually large or small values. The difference of medians is robust to outliers. A difference of trimmed means is a compromise that reduces the influence of extreme observations. The Welch statistic, unlike the pooled $t$, is not a monotone function of the mean difference and can give a different $p$-value. A rough guide: for approximately normal data use the difference of means, for symmetric data with outliers trimmed means, for skewed data medians. Whatever the statistic, the test is exact under the null hypothesis that the two distributions are identical; the statistic only determines against which alternatives the test has power.

The practical limitation of permutation tests is computation, especially for large samples. For statistics based on ranks this disappears: the ranks of the pooled sample are always $1,\dots,N$ (without ties), so the permutation distribution of a rank statistic depends only on $n_1$ and $n_2$ and can be computed once and tabulated. This is the idea of the Wilcoxon–Mann–Whitney test.

## 9.3. The Wilcoxon–Mann–Whitney Test

### 9.3.1. Rank Sums and the U Statistic

The WMW test is the two-sample counterpart of the Wilcoxon signed-rank test: combine the two samples, rank all the observations, and compare the ranks of the two groups. If the populations are the same, each sample should contain a mixture of low, medium and high ranks; if one population tends to give larger values, its sample should have predominantly high ranks.

**Definition 9.3.1 (Wilcoxon Rank-Sum Test)** Let $x_1,\dots,x_{n_1}$ and $y_1,\dots,y_{n_2}$ be independent samples and rank the $N=n_1+n_2$ pooled observations. Let $W_x$ and $W_y$ be the sums of the ranks of the two samples, and

$$
U_x=W_x-\frac{n_1(n_1+1)}2,\qquad U_y=W_y-\frac{n_2(n_2+1)}2 .
$$
The **Wilcoxon rank-sum test** (equivalently the Mann–Whitney $U$ test, together the **Wilcoxon–Mann–Whitney test**) of $H_0$: the two samples come from the same continuous distribution, rejects for extreme values of $W_x$, or equivalently of $U_x$. Large $U_x$ indicates that the $x$'s tend to be larger. By convention tables are given for $U=\min(U_x,U_y)$, small values of which indicate departures from $H_0$.

The subtraction of $n_1(n_1+1)/2$, the smallest possible value of $W_x$ (all $x$'s ranked lowest), adjusts for the different sample sizes, so that $U_x$ and $U_y$ are directly comparable, and gives the count interpretation below.

**Proposition 9.3.1** Without ties,

$$
U_x=\#\{(i,j)\colon x_i>y_j\}=\sum_{i=1}^{n_1}\sum_{j=1}^{n_2}\boldsymbol{1}\{x_i-y_j>0\},
$$
the number of the $n_1n_2$ pairs in which the $x$ exceeds the $y$. In particular $U_x+U_y=n_1n_2$, $0\le U_x\le n_1n_2$, and under $H_0$ we expect $U_x\approx U_y\approx n_1n_2/2$.

**Proof** Let $x_{(1)}<\dots<x_{(n_1)}$. The rank of $x_{(k)}$ in the pooled sample is $k$ (the $x$'s at or below it) plus the number of $y$'s below it. Summing over $k$,

$$
W_x=\sum_{k=1}^{n_1}k+\sum_{k=1}^{n_1}\#\{j\colon y_j<x_{(k)}\}=\frac{n_1(n_1+1)}2+U_x .
$$
The same argument for $y$ gives $U_y=\#\{(i,j)\colon y_j>x_i\}$, and every pair is counted in exactly one of them. $\square$

Any increase in $U_x$ is matched by an equal decrease in $U_y$. Using $W_x$ or $U_x$ as the statistic gives the same test, since they differ by a constant.

**Example 9.3.1 (Pocket Calculators, Continued)** In the pooled ranking the ranks of group A are $1,2,3,5,6,8,9,12,14,16$, so $W_x=76$ and $W_y=155$; then $U_x=76-55=21$ and $U_y=155-66=89$, with $21+89=110=n_1n_2$.

```r
A <- c(23, 18, 17, 25, 22, 19, 31, 26, 29, 33)
B <- c(21, 28, 32, 30, 41, 24, 35, 34, 27, 39, 36)
sum(rank(c(A, B))[1:10])                    # W_x = 76
wilcox.test(A, B)
wilcox.test(A, B, alternative = "less")
```

```text
Wilcoxon rank sum exact test
W = 21, p-value = 0.01587
alternative hypothesis: true location shift is not equal to 0

W = 21, p-value = 0.007936
alternative hypothesis: true location shift is less than 0
```

R reports $U_x$ under the name `W`. The one-sided $p$-value $0.0079$, appropriate for the question whether type A is faster, gives fairly strong evidence that pupils perform these calculations faster with type A. It would nevertheless be unreasonable to recommend type A calculators on the basis of this study alone: a calculator convenient for trigonometric functions may perform worse on other tasks, such as computing a mean or a standard deviation.
:::

### 9.3.2. The Exact Null Distribution

Under $H_0$ all $\binom{N}{n_1}$ assignments of the ranks $1,\dots,N$ to the first sample are equally likely, and the distribution of $U_x$ is obtained by counting. Let $c(u;n_1,n_2)$ be the number of arrangements of $n_1$ symbols $x$ and $n_2$ symbols $y$ with $U_x=u$. Conditioning on whether the largest observation is an $x$ (which then exceeds all $n_2$ $y$'s) or a $y$ gives the recursion

$$
c(u;n_1,n_2)=c(u-n_2;n_1-1,n_2)+c(u;n_1,n_2-1),
$$
from which $\mathbb{P}(U_x=u)=c(u;n_1,n_2)/\binom{N}{n_1}$; R's `dwilcox`, `pwilcox` and `qwilcox` evaluate it. The distribution is symmetric about $n_1n_2/2$.

**Example 9.3.2 (A Tiny Example)** Let $x=(1,4)$ and $y=(2)$, so $U_x=1$ (only $4>2$). The three equally likely ways of choosing which pooled value is the $y$ give

| $y$ | $x$ | $U_x$ |
|---|---|---|
| 1 | 2, 4 | 2 |
| 2 | 1, 4 | 1 |
| 4 | 1, 2 | 0 |

so $U_x$ is uniform on $\{0,1,2\}$, and the one-sided $p$-value for $H_1$: $x$ tends to be larger is $\mathbb{P}(U_x\ge1)=2/3$, as `wilcox.test(x, y, alternative = "greater")` reports. It is tempting to treat the $n_1n_2=2$ differences $x_i-y_j$, here $-1$ and $2$, as a sample and apply a sign test, which would give $\mathbb{P}(\mathrm{Bin}(2,1/2)\ge1)=3/4$. This is wrong: the differences $x_i-y_j$ share observations and are not independent, and only the permutation argument gives the correct null distribution.
:::

### 9.3.3. Mean, Variance and the Normal Approximation

**Theorem 9.3.1** Under $H_0$ (no ties),

$$
\mathbb{E}W_x=\frac{n_1(N+1)}2,\qquad \mathbb{E}U_x=\frac{n_1n_2}2,\qquad \operatorname{Var}(W_x)=\operatorname{Var}(U_x)=\frac{n_1n_2(N+1)}{12},
$$
and as $n_1,n_2\to\infty$,

$$
Z=\frac{U_x-n_1n_2/2}{\sqrt{n_1n_2(N+1)/12}}\xrightarrow{d}\mathcal{N}(0,1).
$$

**Proof** Let $Z_k=1$ if the $k$th smallest pooled observation comes from the first sample and $Z_k=0$ otherwise, so that $W_x=\sum_{k=1}^NkZ_k$. Under $H_0$ the vector $(Z_1,\dots,Z_N)$ is a random arrangement of $n_1$ ones and $n_2$ zeros, so

$$
\mathbb{E}Z_k=\frac{n_1}N,\qquad \operatorname{Var}(Z_k)=\frac{n_1n_2}{N^2},\qquad
\operatorname{Cov}(Z_k,Z_l)=\frac{n_1(n_1-1)}{N(N-1)}-\frac{n_1^2}{N^2}=-\frac{n_1n_2}{N^2(N-1)}\quad(k\ne l).
$$
Hence $\mathbb{E}W_x=\frac{n_1}N\cdot\frac{N(N+1)}2=\frac{n_1(N+1)}2$, and

$$
\operatorname{Var}(W_x)=\frac{n_1n_2}{N^2}\sum_kk^2-\frac{n_1n_2}{N^2(N-1)}\sum_{k\ne l}kl
=\frac{n_1n_2}{N^2(N-1)}\Bigl[N\sum_kk^2-\Bigl(\sum_kk\Bigr)^2\Bigr],
$$
using $\sum_{k\ne l}kl=(\sum_kk)^2-\sum_kk^2$. With $\sum_kk^2=N(N+1)(2N+1)/6$ and $\sum_kk=N(N+1)/2$ the bracket is $N^2(N+1)(N-1)/12$, which gives the variance. The statements for $U_x$ follow because $U_x$ and $W_x$ differ by a constant. The asymptotic normality is a consequence of the theory of $U$-statistics ([3.6.2](/3.6.2)), or of a central limit theorem for sampling without replacement; we do not prove it. $\square$

The mean and variance depend only on $n_1$ and $n_2$, which is why the test can be tabulated; by contrast the permutation mean and variance of $\bar X-\bar Y$ depend on the observed values. A continuity correction of $\pm\frac12$ improves the approximation. For the calculators, $\mathbb{E}U_x=55$, $\operatorname{Var}(U_x)=201.7$, and $z=(21+0.5-55)/14.20=-2.36$, a two-sided $p$-value of $0.018$, close to the exact $0.016$.

![Exact null distribution of $U_x$ for $n_1=10$, $n_2=11$, with the normal approximation. The red bars are the two-sided rejection region at the nominal $5\%$ level, $U_x\le26$ or $U_x\ge84$, whose actual size is $0.043$; the calculator data give $U_x=21$.](./plots/u-null.py)

### 9.3.4. U as a U-Statistic, and the Name

Proposition 9.3.1 shows that $U_x$ is a two-sample **U-statistic** ([3.6.2](/3.6.2)) with the kernel $h(x,y)=\boldsymbol{1}\{x>y\}$ of degree $(1,1)$: it counts how many times an observation from the first population exceeds one from the second. Its standardized form

$$
\frac{U_x}{n_1n_2}=\frac1{n_1n_2}\sum_{i=1}^{n_1}\sum_{j=1}^{n_2}\boldsymbol{1}\{X_i>Y_j\}
$$
is an unbiased estimator of $\mathbb{P}(X>Y)$ for continuous populations. This quantity is also the empirical **area under the curve** of the ROC curve that uses the measured value to discriminate the two populations: the WMW statistic and the AUC are the same number in two notations.

The test was proposed by Wilcoxon (1945), for samples of equal size, as a sum of ranks. Mann and Whitney (1947) introduced the statistic $U$ for samples of unequal sizes, tabulated its distribution and established its limiting normality; hence the two names.

### 9.3.5. Ties

With ties within or between the samples, the pooled observations receive **midranks**, as for the signed-rank test ([3.6.3](/3.6.3)). Ties within one sample do not change $W_x$; ties between the samples are the ones that matter. Correspondingly, $U_x$ counts a tied pair as one half:

$$
U_x=\sum_{i,j}\Bigl[\boldsymbol{1}\{x_i>y_j\}+\tfrac12\boldsymbol{1}\{x_i=y_j\}\Bigr],\qquad
U_y=\sum_{i,j}\Bigl[\boldsymbol{1}\{x_i<y_j\}+\tfrac12\boldsymbol{1}\{x_i=y_j\}\Bigr],
$$
which equals $W_x-n_1(n_1+1)/2$ with midranks. The exact null distribution is now the permutation distribution of the observed midranks, which differs from the tabulated one. For the normal approximation the mean is unchanged, $\mathbb{E}U_x=n_1n_2/2$, and the variance is reduced to

$$
\operatorname{Var}(U_x)=\frac{n_1n_2}{12}\left[(N+1)-\frac{\sum_g(d_g^3-d_g)}{N(N-1)}\right],
$$
where $d_g$ is the number of observations in the $g$th group of tied values ($d_g=1$ for an untied value). The correction makes the variance, and usually the $p$-value, slightly smaller. Ties arise most often when data are recorded coarsely or grouped.

**Example 9.3.3 (A Second Calculator Experiment)** A second, similar experiment gave the times

| Group A | 16 | 18 | 19 | 22 | 22 | 25 | 28 | 28 | 28 | 31 | 33 | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Group B | 22 | 23 | 25 | 27 | 27 | 28 | 30 | 32 | 33 | 35 | 36 | 38 | 38 |

with several ties (the pooled ranks begin $1,2,3,5,5,5,7,8.5,8.5,\dots$). Here $U_x=35.5$. The normal approximation with the tie-corrected variance and a continuity correction gives a two-sided $p$-value of $0.039$; the exact permutation distribution of the midranks gives $0.036$ (`asht::wmwTest(A, B, exact = TRUE)` reports $0.037$, using a slightly different two-sided convention); the no-tie table, `2 * pwilcox(35, 11, 13)`, gives $0.035$. There is some evidence that calculations are completed more rapidly with type A.
:::

The no-tie tables are least satisfactory when there are many ties, or ties in unbalanced samples.

**Example 9.3.4 (When Ties Matter)** For $x=(1,2,2)$ and $y=(1,1,4,5,5,5,7,8,9,9,9,9,10)$, $U_x=5$ and R warns that it cannot compute an exact $p$-value with ties. Its normal approximation gives $p=0.056$, and the no-tie table gives $0.057$; the exact permutation test allowing for ties gives $0.046$ (doubling the one-sided exact $p$-value). With a $p$-value this close to $0.05$, the method of computation decides the verdict, and the exact conditional $p$-value is the one to report. Ignoring the ties and using the no-tie null distribution usually overstates the $p$-value, because ties reduce the null variance of $U_x$; but because of the discreteness this is a tendency, not a rule.
:::

## 9.4. Confidence Interval and Hodges–Lehmann Shift Estimate

To estimate how much faster type A is, we need a parameter. The natural one comes from assuming that the two distributions differ only by a shift.

Suppose $X\overset{d}{=}Y+\Delta$, so that $\Delta$ is the difference of the medians (and of the means, if they exist). Then $X_i-\Delta$ and $Y_j$ have the same distribution, and

$$
U_x(\Delta_0)=\#\{(i,j)\colon x_i-y_j>\Delta_0\}
$$
has the null distribution of $U_x$ when $\Delta_0=\Delta$. Testing $H_0\colon\Delta=\Delta_0$ with the WMW test applied to $x_i-\Delta_0$ and $y_j$ and collecting the accepted values gives a confidence interval, exactly as the Walsh averages did in the one-sample case. Let $D_{(1)}\le\dots\le D_{(n_1n_2)}$ be the ordered pairwise differences $D_{ij}=x_i-y_j$.

**Proposition 9.4.1** Let $c$ be the largest integer with $\mathbb{P}(U_x\le c)\le\alpha/2$ under $H_0$. Then under the shift model, for continuous distributions,

$$
\mathbb{P}\bigl(D_{(c+1)}\le\Delta<D_{(n_1n_2-c)}\bigr)=1-2\,\mathbb{P}(U_x\le c)\ge1-\alpha,
$$
so $[D_{(c+1)},D_{(n_1n_2-c)}]$ (the $(c+1)$th smallest to the $(c+1)$th largest difference) is a $1-\alpha$ confidence interval for $\Delta$. The **Hodges–Lehmann estimator** of the shift is the median of the $n_1n_2$ differences $D_{ij}$.

**Proof** $U_x(\Delta_0)$ is the number of $D_{ij}$ exceeding $\Delta_0$, a non-increasing step function of $\Delta_0$. Hence $U_x(\Delta)\ge c+1$ if and only if $\Delta<D_{(n_1n_2-c)}$, and $U_x(\Delta)\le n_1n_2-c-1$ if and only if $\Delta\ge D_{(c+1)}$. Since $U_x(\Delta)$ has the null distribution, which is symmetric, the probability that both hold is $1-2\,\mathbb{P}(U_x\le c)$. $\square$

The point estimate is the value $\hat\Delta$ that makes $U_x(\hat\Delta)$ equal to its null centre $n_1n_2/2$, the same construction that produced the one-sample Hodges–Lehmann estimate from the signed-rank test ([3.6.5](/3.6.5)); it is also called the Hodges–Lehmann–Sen shift estimator.

**Example 9.4.1 (Pocket Calculators, Continued)** For $n_1=10$, $n_2=11$, $\mathbb{P}(U_x\le26)=0.0215$ and $\mathbb{P}(U_x\le27)=0.0257$, so $c=26$ (`qwilcox(0.025, 10, 11)` returns $27$, the smallest $u$ with $\mathbb{P}(U_x\le u)\ge0.025$). The $95\%$ interval runs from the $27$th smallest to the $27$th largest of the $110$ differences:

```r
d <- outer(A, B, "-")
sort(d)[27]; sort(d, decreasing = TRUE)[27]     # -13, -2
median(d)                                       # -7.5
wilcox.test(A, B, conf.int = TRUE)
```

The interval for $\Delta=\theta_A-\theta_B$ is $[-13,\,-2]$ minutes, with exact coverage $1-2\times0.0215=0.957$, and the Hodges–Lehmann estimate is $-7.5$ minutes. The interval does not contain $0$, consistent with the two-sided test. No permutation is involved in the calculation: as in the one-sample case, the interval is read off from ordered differences with the critical value from the table. Equivalently, by trial and error: shifting group B by $\Delta_0=-2$ (adding $-2$ to every $y$) and recomputing $U$, the value $\Delta_0$ belongs to the interval if and only if $U\ge c+1=27$.
:::

**Remark 9.4.1** Is the Hodges–Lehmann estimate the "difference between the medians"? Under the shift model both estimate the same $\Delta$. For the calculators the sample medians are $24$ and $32$, a difference of $-8$, close to $-7.5$. In general they differ: for $x=(-1,0,1)$ and $y=(-0.5,0,2)$ the nine differences are $-3,-2,-1,-1,-0.5,0,0.5,1,1.5$, with median $-0.5$, while both sample medians are $0$. Without the shift model, the Hodges–Lehmann estimate estimates the median of the distribution of $X-Y$, not the difference of the two medians. The interval of Proposition 9.4.1 also relies on the shift model; its coverage is not guaranteed if the shapes differ.

## 9.5. What the WMW Test Tests

### 9.5.1. Assumptions

Compared with the two-sample $t$-test, the WMW test as a test of $H_0\colon F=G$ requires:

1. independent observations (within and between the samples);
2. random samples from the two populations (or random allocation of units to the groups);
3. no normality;
4. no continuity in an essential way: with ties, midranks and the permutation distribution of the midranks give an exact test;
5. no separate assumption of equal variances, since $F=G$ implies equal variances under $H_0$.

The last point is where the trouble starts. The test is exact for the null hypothesis that the two distributions are identical. But that is rarely the hypothesis of interest: one usually wants to know whether the medians, or the means, are equal, while allowing the distributions to differ in other respects.

### 9.5.2. Counterexamples

The perception that the WMW procedure tests equality of medians is pervasive and mostly wrong; it is true only when the two distributions are shifted versions of each other, differing in location but not in shape or scale (Divine et al. 2017, who quote the same warning from O'Brien and Castelloe 2006).

**Example 9.5.1 (Medians Far Apart, WMW Insensitive)** Two samples of $15$ values each:

| Value | 1 | 2 | 3 | 9 | 105 | 106 | 107 |
|---|---|---|---|---|---|---|---|
| Count in A | 2 | 3 | 2 | 1 | 2 | 3 | 2 |

| Value | 5 | 6 | 7 | 99 | 101 | 102 | 103 |
|---|---|---|---|---|---|---|---|
| Count in B | 2 | 3 | 2 | 1 | 2 | 3 | 2 |

The sample medians are $9$ and $99$. Of the $225$ pairs $(a,b)$, $112$ have $a>b$ and $113$ have $a<b$, so $U_x=112$ is as close to $n_1n_2/2=112.5$ as possible, and `wilcox.test(A, B)` gives $p=1$. Each sample is bimodal, and A has the more extreme values in both clusters; a randomly chosen A is as likely to exceed a randomly chosen B as the reverse, although the medians differ by $90$.
:::

**Example 9.5.2 (Equal Medians, WMW Significant)** Changes in a post-operative nausea score were recorded for two groups of patients:

| Change | $-3$ | $-2$ | $-1$ | $0$ | $1$ |
|---|---|---|---|---|---|
| Group 1 ($n=78$) | 0 | 6 | 34 | 33 | 5 |
| Group 2 ($n=74$) | 4 | 11 | 46 | 12 | 1 |

Both medians are $-1$, yet `wilcox.test` gives $p=2.4\times10^{-5}$. Of the $5772$ pairs, $2031$ are ties, and among the $3741$ others the group-1 value is larger in $2912$. The estimated $\mathbb{P}(X>Y)+\frac12\mathbb{P}(X=Y)$ is $0.68$: a patient from group 1 tends to have a larger change than a patient from group 2, which the medians, stuck on the large tied category $-1$, do not show.
:::

Both examples have the same explanation. What the rank sum measures is the tendency of one sample to exceed the other, that is, $\mathbb{P}(X>Y)$.

### 9.5.3. Shift, Stochastic Equality and Stochastic Dominance

**Definition 9.5.1 (Location-Shift Model)** Two distributions $F$ (of $X$) and $G$ (of $Y$) follow the **location-shift model** if $F(t)=G(t-\Delta)$ for all $t$ and some $\Delta$, that is, $X\overset{d}{=}Y+\Delta$: the distributions have the same shape and spread and differ only in location.

**Definition 9.5.2 (Stochastic Equality and Stochastic Dominance)** Independent random variables $X$ and $Y$ are **stochastically equal** if

$$
\mathbb{P}(X>Y)+\tfrac12\mathbb{P}(X=Y)=\tfrac12 ,
$$
that is (for continuous variables), a randomly chosen value from one population is equally likely to be smaller or larger than one from the other; this property is called **stochastic equality**. $X$ is **stochastically larger** than $Y$ (exhibits **stochastic dominance** over $Y$) if $F(t)\le G(t)$ for all $t$, with strict inequality for some $t$.

The concepts are nested. If the shift model holds, then $\Delta=0$ means $F=G$, and $\Delta>0$ makes $X$ stochastically larger than $Y$, which in turn implies $\mathbb{P}(X>Y)+\frac12\mathbb{P}(X=Y)>\frac12$. Conversely, stochastic equality does not imply equal medians or equal distributions (Example 9.5.1). The WMW statistic estimates $p=\mathbb{P}(X>Y)+\frac12\mathbb{P}(X=Y)$, and the test is consistent against alternatives with $p\ne1/2$ and has no power against those with $p=1/2$.

The null distribution, however, is computed by permuting labels, which requires that under $H_0$ the ranks are exchangeable between the two samples. The typical way to obtain this is that the two distributions are identical (have the same shape and spread) when $H_0$ is true. If one uses the WMW test as a test of stochastic equality, allowing the distributions to differ, the label exchangeability fails, and the level is no longer controlled. The following simulation shows how badly.

![Rejection rates at nominal level $0.05$ when $X\sim\mathcal{N}(0,s^2)$ and $Y\sim\mathcal{N}(0,1)$, so that the medians are equal and $\mathbb{P}(X>Y)=1/2$ exactly, for $4000$ replications. When the smaller sample has the larger spread (left), the WMW test rejects up to about $12\%$ of the time; when the larger sample has the larger spread (right), it becomes very conservative. Welch's $t$-test and the Brunner–Munzel test stay close to $5\%$.](./plots/wmw-size.py)

So the WMW test can be read in two ways:

- if the two samples come from distributions of the same shape (the shift model), the test compares their medians (or means), and Section 9.4 gives the interval and estimate of the shift;
- if the shapes may differ, it tests the more general question whether a randomly selected member of one population tends to exceed a randomly selected member of the other, without telling us anything about medians, and its level is exact only for $F=G$.

## 9.6. The Brunner–Munzel Test

With unequal variances, especially combined with unequal sample sizes, the Brunner–Munzel test (Brunner and Munzel 2000), also called the generalized Wilcoxon test, is recommended. It tests the hypothesis of stochastic equality, $H_0\colon p=\frac12$ with $p=\mathbb{P}(X<Y)+\frac12\mathbb{P}(X=Y)$, without assuming that the two distributions have the same shape.

**Definition 9.6.1 (Brunner–Munzel Test)** Let $R_1,\dots,R_N$ be the midranks in the pooled sample, $\bar R_X$ and $\bar R_Y$ the mean pooled midranks of the two samples, and $R_i^{(X)}$, $R_j^{(Y)}$ the midranks within each sample. With the variance estimates

$$
s_X^2=\frac1{n_1-1}\sum_{i=1}^{n_1}\Bigl(R_i-R_i^{(X)}-\bar R_X+\frac{n_1+1}2\Bigr)^2
$$
and $s_Y^2$ defined analogously, the **Brunner–Munzel test** uses

$$
B=\frac{\bar R_Y-\bar R_X}{(n_1+n_2)\sqrt{\dfrac{s_X^2}{n_1n_2^2}+\dfrac{s_Y^2}{n_1^2n_2}}},
$$
referred to a $t$ distribution with degrees of freedom estimated by a Welch–Satterthwaite-type formula. The relative effect is estimated by $\hat p=\bigl(\bar R_Y-(n_2+1)/2\bigr)/n_1$.

The degrees of freedom are obtained as in the **Satterthwaite approximation** for Welch's test. The quantity $R_i-R_i^{(X)}$ is the number of $y$'s below $x_i$ (counting ties as one half), the "placement" of $x_i$ among the $y$'s; $s_X^2$ is their sample variance. The statistic is thus a rank analogue of Welch's $t$: a difference of mean ranks divided by an estimate of its standard error that does not assume equal variances. It can be regarded as the nonparametric version of Welch's $t$-test, robust to heteroscedasticity.

For the calculators, `lawstat::brunner.munzel.test(A, B)` gives $B=3.24$ and $p=0.0044$, with $\hat p=0.81$ ($=1-U_x/(n_1n_2)$: a type B pupil is slower than a type A pupil with estimated probability $0.81$). For the nausea data of Example 9.5.2 it gives $p=7\times10^{-6}$.

**Remark 9.6.1** The Brunner–Munzel test controls the type I error only approximately, through the $t$ approximation, not exactly. The simulation above shows good control for samples of $10$ and $30$; for very small samples (fewer than about $10$ per group) the $t$ approximation can be liberal, and a studentized permutation version of the test (Neubert and Brunner 2007) is preferable. When the shift model is credible, the WMW test is exact and slightly more powerful.

## 9.7. Mood's Median Test

Just as the sign test is the one-sample test that counts observations above a hypothesized median, Mood's median test counts observations above the pooled median.

**Definition 9.7.1 (Mood's Median Test)** Let $M$ be the median of the pooled sample $x_1,\dots,x_{n_1},y_1,\dots,y_{n_2}$, and cross-classify the observations by sample and by whether they lie above $M$:

| | First sample | Second sample | Total |
|---|---|---|---|
| Above $M$ | $A$ | $t-A$ | $t$ |
| Not above $M$ | $n_1-A$ | $n_2-t+A$ | $N-t$ |

**Mood's median test** of $H_0$: the two populations have the same median, rejects when $A$ is far from $n_1t/N$. Under $H_0\colon F=G$, conditionally on the margins, $A$ has the hypergeometric distribution

$$
\mathbb{P}(A=a)=\frac{\binom{n_1}{a}\binom{n_2}{t-a}}{\binom{N}{t}},
$$
which gives Fisher's exact test for the table; for large samples the chi-squared test of independence is used. Observations equal to $M$ are dropped or counted as not above $M$ (conventions differ).

:::

In other words, Mood's test is **Fisher's exact test** ([3.6.12](/3.6.12)) applied to the table obtained by dichotomizing at $M$, with the **hypergeometric distribution** as its null distribution. The test is usually justified under a shift model, $G(y)=F(y-\theta)$ with $H_0\colon\theta=0$, but it is designed to compare medians and is much less affected than the WMW test by differences in shape or spread, and very insensitive to outliers, since it records only on which side of $M$ each observation falls.

**Example 9.7.1** Scores were recorded for $7$ males and $21$ females:

| Males | 15 | 16 | 20 | 24 | 27 | 31 | 34 | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Females | 8 | 9 | 11 | 11 | 14 | 15 | 16 | 16 | 16 | 17 | 18 | 18 | 19 | 21 | 23 | 23 | 25 | 25 | 25 | 27 | 32 |

The pooled median is $M=18.5$, and the $2\times2$ table with fixed margins is

| | Males | Females | Total |
|---|---|---|---|
| Above $M$ | 5 | 9 | 14 |
| Below $M$ | 2 | 12 | 14 |

Under $H_0$ the number $A$ of males above $M$ has the hypergeometric distribution with $\binom{28}{14}$ in the denominator, symmetric about its mean $3.5$; the most likely tables are those with $3$ or $4$ males above $M$, and the least likely those with $0$ or $7$. The two-sided $p$-value is

$$
2\bigl[\mathbb{P}(A=5)+\mathbb{P}(A=6)+\mathbb{P}(A=7)\bigr]=0.385 .
$$

```r
males <- c(15, 16, 20, 24, 27, 31, 34)
females <- c(8, 9, 11, 11, 14, 15, 16, 16, 16, 17, 18, 18, 19, 21, 23, 23, 25, 25, 25, 27, 32)
fisher.test(rbind(c(5, 2), c(9, 12)))      # p-value = 0.3845
chisq.test(rbind(c(5, 2), c(9, 12)))       # X-squared = 0.762 (continuity corrected), p-value = 0.383
wilcox.test(males, females)                 # p-value = 0.1295
```

Neither test finds a difference; the WMW $p$-value is much smaller than Mood's, reflecting the information Mood's test discards.
:::

The price of Mood's robustness is power. Under normality its asymptotic relative efficiency is $2/\pi\approx0.64$ relative to the $t$-test, the same as the sign test, and $2/3$ relative to the WMW test ([3.6.4](/3.6.4)). Its level is exact only when $F=G$; with equal medians but different densities at the median it is only approximately correct, which, together with the low power, has led some authors to recommend against its routine use (Freidlin and Gastwirth 2000). It is most useful for large samples with heavy tails, outliers or censoring above some value.

## 9.8. Bootstrapping the Difference of Medians

If the parameter of interest is the difference of the two medians and the shapes may differ, we can estimate the sampling distribution of the difference of sample medians by the **nonparametric bootstrap** ([3.5.7](/3.5.7)):

1. draw a **bootstrap sample** from each group: a sample of the same size as the original, drawn with replacement from that group's observations;
2. compute the bootstrap statistic, the median of the first bootstrap sample minus the median of the second;
3. repeat steps 1 and 2 many times to obtain the **bootstrap distribution** of the difference of medians;
4. take the middle $95\%$ of the bootstrap distribution (the percentile interval) as a confidence interval.

For the calculators the observed difference is $24-32=-8$ minutes, and $20\,000$ bootstrap replicates give a $95\%$ percentile interval of about $(-15,\,-0.5)$; the end points depend on the random seed. The interval excludes $0$.

The bootstrap and the permutation test answer different questions:

| | Permutation test | Bootstrap |
|---|---|---|
| Main purpose | testing (is there a difference?) | estimation (how large is the difference, and how uncertain?) |
| Resampling | shuffle the group labels, without replacement | resample each group with replacement |
| Requirement | labels exchangeable under $H_0$ (for example $F=G$) | samples representative of their populations; $n$ not too small |
| Null hypothesis | $F=G$ | none by itself; a bootstrap test must resample from data modified to satisfy $H_0$ (3.5.7) |
| Output | $p$-value | bootstrap distribution, standard error, confidence interval |

The two complement each other: a permutation test (or the WMW test, which is one) can establish that the groups differ, and a bootstrap interval can quantify by how much in terms of the parameter of interest. Neither is free of assumptions. The bootstrap of a median is unreliable for small samples and for discrete data with many ties, because the sample median can take only a few values and its bootstrap distribution is lumpy (3.5.7); with $10$ and $11$ observations the interval above should be regarded as rough.

## 9.9. Choosing a Method

The first step is to decide what difference is of interest: a difference of means, a difference of medians, or the more general tendency of one population to give larger values (stochastic dominance, measured by $\mathbb{P}(X>Y)$). Different questions call for different tests.

| Target | Conditions | First choice | Alternatives |
|---|---|---|---|
| Difference of means | approximately normal data, or large samples (CLT); equal or unequal variances | Welch $t$-test (pooled $t$ if variances are equal) | permutation test on the difference of means (exact for $F=G$) |
| Difference of medians | shapes may differ | bootstrap interval for the difference of medians (moderate or large samples) | Mood's median test (robust, low power) |
| $\mathbb{P}(X>Y)=\frac12$ (stochastic equality) | similar shapes and spreads | WMW test | Brunner–Munzel test, especially with unequal spreads and sizes; its permutation version for small samples |
| A location shift | the location-shift model is credible | WMW test with Hodges–Lehmann estimate and interval | $t$-test if the data are normal |

A few comments. The $t$-test is the most direct test of means but relies on normality or on large samples; it is sensitive to outliers and to severe skewness in small samples (less than about $15$ per group). The WMW test is the standard nonparametric test for a tendency of one group to exceed the other; under a shift it is a test of location with high efficiency ($3/\pi\approx0.955$ relative to $t$ under normality, never below $0.864$). When the distributions differ in shape, its result is about $\mathbb{P}(X>Y)$, not about medians, and its level is not guaranteed; the Brunner–Munzel test is then the better test of stochastic equality, and, if medians are the target, the bootstrap or Mood's test. Permutation and bootstrap methods are general frameworks that can be applied to any statistic, and they underlie all the others.

## Summary

- Two-sample permutation test (Section 9.2): under $F=G$ all $\binom{N}{n_1}$ partitions are equally likely; $\bar X-\bar Y$, $S_x$ and the pooled $t$ are equivalent statistics (Proposition 9.2.1). With ranks, the permutation distribution no longer depends on the data.
- WMW test (Definition 9.3.1): $U_x=W_x-n_1(n_1+1)/2=\#\{x_i>y_j\}$ (Proposition 9.3.1), $U_x+U_y=n_1n_2$; exact distribution by counting (do not apply a sign test to the dependent $x_i-y_j$, Example 9.3.2); $\mathbb{E}U_x=n_1n_2/2$, $\operatorname{Var}(U_x)=n_1n_2(N+1)/12$ (Theorem 9.3.1). $U_x/(n_1n_2)$ is a U-statistic estimating $\mathbb{P}(X>Y)$, the empirical AUC.
- Ties: midranks, tied pairs count $\frac12$ in $U$; tie-corrected variance $\frac{n_1n_2}{12}\bigl[(N+1)-\sum(d_g^3-d_g)/(N(N-1))\bigr]$; with many ties use the exact permutation distribution of the midranks (Example 9.3.4).
- Under the location-shift model (Definition 9.5.1): $95\%$ interval for $\Delta$ from the $(c+1)$th smallest to the $(c+1)$th largest $x_i-y_j$, Hodges–Lehmann estimate = median of the $x_i-y_j$ (Proposition 9.4.1); for the calculators $[-13,-2]$ and $-7.5$.
- What WMW tests: $p=\mathbb{P}(X>Y)+\frac12\mathbb{P}(X=Y)$, stochastic equality versus stochastic dominance (Definition 9.5.2); equal medians only under the shift model (Examples 9.5.1–9.5.2). Its null distribution needs $F=G$; with unequal spreads and sizes its level is wrong.
- Brunner–Munzel (Definition 9.6.1): a Welch-type rank test of stochastic equality, approximately valid without equal shapes. Mood's median test (Definition 9.7.1): $2\times2$ table about the pooled median, Fisher or chi-squared, robust but low power (ARE $2/\pi$ against $t$). Bootstrap: intervals for the difference of medians; permutation tests test $F=G$.
- Choose the target first (means, medians, or $\mathbb{P}(X>Y)$), then the method (Section 9.9).

## Questions

1. For $x=(1,2,2)$ and $y=(1,1,4,5,5)$, assign midranks to the pooled sample, compute $W_x$ and $U_x$, and check $U_x$ by counting pairs. Why are the no-tie tables inaccurate here?

   **Answer** The pooled values $1,1,1,2,2,4,5,5$ have midranks $2,2,2,4.5,4.5,6,7.5,7.5$. The $x$'s have ranks $2,4.5,4.5$, so $W_x=11$ and $U_x=11-3\cdot4/2=5$. Counting: $x=1$ ties with two $y$'s ($2\times\frac12=1$) and exceeds none; each $x=2$ exceeds the two $y$'s equal to $1$ (2 each); total $1+2+2=5$. With $8$ observations in three tied groups, $U_x$ can take only a few distinct values, its permutation distribution is far from the no-tie table, and its variance is smaller: $\frac{15}{12}\bigl[9-\frac{24+6+6}{56}\bigr]=10.45$ instead of $11.25$. The exact permutation distribution of the midranks should be used.
2. A teacher compares two teaching methods with $10$ randomly assigned students each. Which of the two-sample $t$-test, the WMW test and Mood's median test would you use if (a) both groups look symmetric and roughly normal with similar variances; (b) A $=(88, 90, 85, 87, 89, 92, 86, 88, 84, 91)$ and B $=(60, 65, 70, 75, 80, 85, 90, 95, 100, 55)$; (c) both groups have a similar shape but B contains one extreme value ($200$ among values from $60$ to $100$)?

   **Answer** (a) The $t$-test: its assumptions hold and it is the most efficient. (b) The spreads are very different (A between $84$ and $92$, B between $55$ and $100$), so the shift model fails; the WMW test would test $\mathbb{P}(X>Y)=\frac12$ with a level that is not guaranteed. If the question concerns medians, use Mood's test (or a bootstrap interval); if it concerns the tendency of one method to give higher scores, the Brunner–Munzel test; Welch's $t$ if means are the target. (c) The WMW test: the shapes are similar, so the shift model is plausible, and the rank test is unaffected by how extreme the value $200$ is, whereas the $t$-test would be dominated by it.
3. Show that under the shift model $X\overset{d}{=}Y+\Delta$ with $\Delta>0$, $X$ is stochastically larger than $Y$, and that $\mathbb{P}(X>Y)>\frac12$ for continuous distributions with a density positive on an interval.

   **Answer** $F(t)=\mathbb{P}(Y+\Delta\le t)=G(t-\Delta)\le G(t)$ since $G$ is non-decreasing, with strict inequality wherever $G$ increases on $(t-\Delta,t]$; so $X$ is stochastically larger. For independent continuous $X$, $Y$, $\mathbb{P}(X>Y)=\int\bigl(1-F(t)\bigr)\,\mathrm{d}G(t)\ge\int\bigl(1-G(t)\bigr)\,\mathrm{d}G(t)=\frac12$, and the inequality is strict because $1-F>1-G$ on a set of positive $G$-probability.
4. Why does the WMW test become liberal when the smaller sample comes from the population with the larger spread (left panel of the simulation), even though $\mathbb{P}(X>Y)=\frac12$?

   **Answer** The null variance $n_1n_2(N+1)/12$ is computed for $F=G$. When $F\ne G$, the true variance of $U_x$ under stochastic equality (continuous case) is $n_1n_2\bigl[\frac14+(n_2-1)\operatorname{Var}(G(X))+(n_1-1)\operatorname{Var}(F(Y))\bigr]$, which reduces to $n_1n_2(N+1)/12$ when $F=G$ (then $G(X)$ and $F(Y)$ are uniform, with variance $\frac1{12}$) and in general involves the spreads of the placements. If the smaller sample ($n_1=10$) has the larger spread, $\operatorname{Var}(G(X))$ is large and is multiplied by the larger $n_2-1=29$, so the true variance exceeds the permutation variance and the test rejects too often; with the allocation reversed, the large variance is multiplied by the smaller factor and the test is conservative. The Brunner–Munzel test estimates exactly this variance from the placements, which is why it keeps the level.
5. Why is the Hodges–Lehmann interval of Proposition 9.4.1 computed without any permutations, although the WMW test is a permutation test?

   **Answer** The null distribution of $U_x$ depends only on $n_1$ and $n_2$, so its critical value $c$ is known in advance. For each candidate shift $\Delta_0$, $U_x(\Delta_0)$ is the number of differences $x_i-y_j$ exceeding $\Delta_0$, and the set of $\Delta_0$ with $c+1\le U_x(\Delta_0)\le n_1n_2-c-1$ is the interval between two order statistics of the $n_1n_2$ differences. Only sorting is needed, as for the Walsh-average interval in the one-sample case.
