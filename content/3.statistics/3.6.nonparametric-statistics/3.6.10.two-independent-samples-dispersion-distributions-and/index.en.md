---
title: "Two Independent Samples: Dispersion, Distributions and Quantile Regression"
description: "Beyond location for two independent samples: the Siegel–Tukey test for a difference in spread; the two-sample runs test and the Smirnov test for a difference anywhere in the distributions (asymptotic Kolmogorov law, exact p-values by lattice paths, ties, comparison of the two); and quantile regression: quantiles as minimizers of the check loss, the linear quantile model, linear programming and other algorithms, interpretation of coefficients across quantiles, and its limits."
---

[3.6.9](/3.6.9) asked whether two independent samples differ in location. Two populations can, however, have the same center and differ in spread, or differ in shape in a way that no single parameter captures. This chapter takes up the remaining two-sample questions. Section 10.1 compares dispersion with the Siegel–Tukey test, which is the Wilcoxon–Mann–Whitney (WMW) test applied to a cleverly chosen set of ranks. Section 10.2 asks whether the two distributions are the same at all, using the two-sample runs test, built on the runs of [3.6.7](/3.6.7), and the Smirnov test, the two-sample counterpart of the Kolmogorov–Smirnov test of [3.6.6](/3.6.6).

The second half of the chapter turns the question "how do two distributions differ?" into a regression problem. When a covariate changes, the whole conditional distribution of the response may change, not only its mean: the spread may grow, the upper tail may move faster than the lower. Quantile regression (Section 10.3) models each conditional quantile separately, by replacing the squared loss of least squares with an asymmetric absolute loss. With a single binary covariate it reduces to comparing the quantiles of two samples, which is why it belongs to this chapter. Several samples follow in [3.6.11](/3.6.11).

## 10.1. Comparing Dispersion: The Siegel–Tukey Test

### 10.1.1. The Test

The classical test of equal variances, the $F$-test on $s_x^2/s_y^2$, is notoriously sensitive to non-normality: for heavy-tailed data its actual level can be several times the nominal one, and for this reason **Levene's test** and its median version, the **Brown–Forsythe test** ([3.3.5](/3.3.5)), are usually preferred. A rank test for dispersion rests on a simple observation. If two samples come from populations that differ only in spread, the sample from the more dispersed population tends to occupy both ends of the pooled ordered sample, and the other sample the middle. A rank test for dispersion should therefore give extreme observations, at either end, small ranks and central observations large ranks; then it can be completed as a WMW test.

**Definition 10.1.1 (Siegel–Tukey Test)** Let $x_1,\dots,x_m$ and $y_1,\dots,y_n$ be independent samples from distributions with a common median (or aligned to have one). Order the $N=m+n$ pooled observations and assign rank $1$ to the smallest, ranks $2$ and $3$ to the largest and second largest, ranks $4$ and $5$ to the second and third smallest, ranks $6$ and $7$ to the third and fourth largest, and so on, alternating between the two ends in pairs and moving toward the middle. The **Siegel–Tukey test** of $H_0$: the two distributions are the same, against the alternative that one is more dispersed, is the WMW test (Definition 9.3.1) applied to these ranks: with $W_x$ the sum of the Siegel–Tukey ranks of the first sample and $U_x=W_x-m(m+1)/2$, a small $U_x$ indicates that the $x$'s are more spread out.

The alternating scheme keeps the ranks at the two ends roughly balanced: the lowest observation gets $1$, the two highest $2$ and $3$, so that the sum of the ranks given to the lower half of the sample and to the upper half are nearly equal. Because the ranks are a fixed permutation of $1,\dots,N$, the null distribution of $W_x$ is exactly that of the WMW statistic, and the tables, the normal approximation and the tie corrections of [3.6.9](/3.6.9) apply unchanged.

**Example 10.1.1 (Tire Failures)** Davis and Lawrence (1989) give the time in hours to two types of tire failure under similar test conditions: type A is rubber chunking on the shoulder, type B cracking of the side wall.

| Type A | 177 | 200 | 227 | 230 | 232 | 268 | 272 | 297 | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Type B | 47 | 105 | 126 | 142 | 158 | 172 | 197 | 220 | 225 | 230 | 262 | 270 |

Do the data suggest that the variances differ? The two medians are $231$ and $184.5$. Since the test compares spreads around a common center, we first align the samples by subtracting the difference of medians, $46.5$, from every type A value, which gives $130.5, 153.5, 180.5, 183.5, 185.5, 221.5, 225.5, 250.5$. The pooled ordered sample and its Siegel–Tukey ranks are:

| Value | 47 | 105 | 126 | 130.5 | 142 | 153.5 | 158 | 172 | 180.5 | 183.5 |
|---|---|---|---|---|---|---|---|---|---|---|
| Rank | 1 | 4 | 5 | 8 | 9 | 12 | 13 | 16 | 17 | 20 |
| Value | 185.5 | 197 | 220 | 221.5 | 225 | 225.5 | 230 | 250.5 | 262 | 270 |
| Rank | 19 | 18 | 15 | 14 | 11 | 10 | 7 | 6 | 3 | 2 |

The type A ranks ($130.5$ and the other shifted values) sum to $W_A=106$, so $U_A=106-8\cdot9/2=70$ and $U_B=mn-U_A=96-70=26$. A large $U_A$ means that type A sits in the middle: type B is the more dispersed. The exact two-sided $p$-value of the WMW test with $m=8$, $n=12$ is $0.098$: there is only weak evidence against equal variances, not enough to reject $H_0$ at the $5\%$ level.

```r
A <- c(177, 200, 227, 230, 232, 268, 272, 297)
B <- c(47, 105, 126, 142, 158, 172, 197, 220, 225, 230, 262, 270)
A2 <- A - (median(A) - median(B))               # align the medians
v <- c(A2, B); o <- order(v); N <- length(v)
st <- integer(N); lo <- 1; hi <- N; r <- 1
st[o[lo]] <- r; lo <- lo + 1; r <- r + 1; side <- "high"
while (lo <= hi) {
  for (k in 1:2) if (lo <= hi) {
    if (side == "high") { st[o[hi]] <- r; hi <- hi - 1 } else { st[o[lo]] <- r; lo <- lo + 1 }
    r <- r + 1
  }
  side <- if (side == "high") "low" else "high"
}
sum(st[1:8])                                    # W_A = 106
wilcox.test(st[1:8], st[9:20])                  # W = 70, p-value = 0.09788
```

The value $185.5$ is the shifted type A median: alignment has placed the two medians next to each other in the middle of the ordering, as it should.
:::

![Siegel–Tukey ranks of the pooled aligned tire data. Red points are type A (shifted by $-46.5$), blue points type B; the numbers are the ranks, which alternate between the two ends in pairs and increase toward the middle. Type A occupies the middle and receives the larger ranks.](./plots/siegel-tukey.py)

### 10.1.2. Why the Samples Must Be Aligned

The Siegel–Tukey test, like every rank test for dispersion, compares the spreads only when the two distributions have the same center. If the $x$'s are shifted far to the right of the $y$'s, the $x$'s occupy the upper end of the pooled sample and the $y$'s the lower end, both samples receive small ranks, and the test may reject because of the shift, not because of a difference in spread. Formally, the test is exact for $H_0\colon F=G$ and consistent against alternatives $G(t)=F(t/\sigma)$ with $\sigma\ne1$ for distributions centered at $0$; for a location–scale family $G(t)=F\bigl((t-\mu)/\sigma\bigr)$ it is valid only when the centers are known to be equal or are aligned.

Aligning with the sample medians, as in Example 10.1.1, solves the practical problem but costs exactness: the aligned observations are no longer exchangeable under $H_0$, since the alignment uses the data. The test is then approximately valid for moderate samples. With a known difference of centers (from theory, or from a previous study), one subtracts that known value and the test remains exact.

Two related rank tests deserve mention. The Ansari–Bradley test uses the same idea with scores that decrease symmetrically from both ends ($1,2,3,\dots,3,2,1$) and is equivalent to the Siegel–Tukey test in large samples. The **squared ranks test** of [3.6.11](/3.6.11) ranks the absolute deviations from the sample means and uses the squares of these ranks as scores; it extends directly to several samples and is the rank analogue of Levene's test. All of them test for a difference in spread under the assumption that the distributions otherwise have the same shape, and none of them can distinguish a difference in variance from a difference in, say, tail weight.

## 10.2. Tests for a Common Distribution

Sometimes no particular feature is of interest: we want to know whether $H_0\colon F=G$, against the alternative that the distributions differ in any way, in location, spread, skewness or shape. The WMW and Siegel–Tukey tests have little power against differences they are not designed for. Two omnibus tests are considered here.

### 10.2.1. The Two-Sample Runs Test

Pool the two samples, order them, and replace each observation by the label of its sample. For example, if the $x$-values are $0.1, 0.4, 0.5, 0.6, 0.8, 0.9$ and the $y$-values $0.2, 0.3, 0.7, 1.0, 1.1, 1.2$, the ordered labels are

$$
x\;yy\;xxx\;y\;xx\;yyy ,
$$
a sequence with $R=6$ **runs** (Definition 7.4.1). If $H_0$ holds, the labels are independent of the values and every arrangement of the $m$ labels $x$ and $n$ labels $y$ is equally likely; the number of runs then has the null distribution of Theorem 7.4.1, with mean $1+2mn/N$. If the distributions differ in location, the $x$'s tend to cluster at one end; if they differ in spread, the $x$'s cluster at both ends or in the middle; in either case there are fewer runs than expected. The two-sample **runs test** (the Wald–Wolfowitz runs test, Definition 7.4.2) therefore rejects $H_0$ for small values of $R$ only.

**Example 10.2.1 (Television Hours)** Is the weekly time spent watching television the same for students of two schools? Random samples of eight students from each gave

| School $X$ | 16.75 | 19.25 | 22.00 | 20.50 | 22.50 | 15.50 | 17.25 | 20.75 |
|---|---|---|---|---|---|---|---|---|
| School $Y$ | 24.75 | 21.50 | 19.75 | 17.75 | 22.75 | 23.50 | 13.00 | 19.00 |

The pooled ordered sample $13.00, 15.50, 16.75, \dots, 24.75$ has the label sequence

$$
y\;xxx\;yy\;x\;y\;xx\;y\;xx\;yyy ,
$$
with $R=9$ runs. For $m=n=8$, $\mathbb{E}R=9$: the observed value is exactly what is expected under $H_0$. The exact $p$-value is

$$
\mathbb{P}(R\le9)=\sum_{r\le9}\mathbb{P}(R=r)=0.595 ,
$$
from Theorem 7.4.1 (the single term $\mathbb{P}(R=9)=2\binom73\binom74/\binom{16}8=0.190$ is already larger than $0.10$). There is no evidence that the distributions differ. At level $0.10$ the critical region would be $R\le5$, with actual size $\mathbb{P}(R\le5)=0.032$, since $\mathbb{P}(R\le6)=0.1002$ just exceeds $0.10$.
:::

The runs test is simple and completely general, but it has two weaknesses. First, ties between the samples make the label sequence ambiguous: a tied $x$ and $y$ can be ordered either way, and the number of runs depends on the choice; the usual remedy is to compute $R$ for all orderings of the tied groups and report the most conservative result. Second, and more important, it has low power: the number of runs uses only how often the labels change, not where. Against location alternatives its asymptotic relative efficiency relative to the WMW test is zero. It is most useful when the observations have a natural order in time or space and the question is whether the groups are randomly mixed along that order (Section 10.2.5).

### 10.2.2. The Smirnov Test

The more powerful omnibus test compares the empirical distribution functions of the two samples directly, as the Kolmogorov–Smirnov test of [3.6.6](/3.6.6) compares one EDF with a hypothesized distribution function.

**Definition 10.2.1 (Smirnov Test)** Let $F_m$ and $G_n$ be the **empirical distribution functions** of independent samples $x_1,\dots,x_m$ from $F$ and $y_1,\dots,y_n$ from $G$. The **Smirnov test** (two-sample Kolmogorov–Smirnov test) of $H_0\colon F=G$, for continuous distributions, uses

$$
D_{m,n}=\sup_t\lvert F_m(t)-G_n(t)\rvert,\qquad
D_{m,n}^+=\sup_t\bigl(F_m(t)-G_n(t)\bigr),\qquad
D_{m,n}^-=\sup_t\bigl(G_n(t)-F_m(t)\bigr),
$$
and rejects for large values of $D_{m,n}$ against $H_1\colon F\ne G$, of $D_{m,n}^+$ against $H_1\colon F(t)\ge G(t)$ for all $t$ with strict inequality somewhere ($X$ tends to be smaller), and of $D_{m,n}^-$ against the opposite one-sided alternative.

Both EDFs are step functions that jump only at the observations, so the supremum is attained at one of the $N$ pooled values, and it suffices to compute $F_m-G_n$ there. Under $H_0$ the distribution of $D_{m,n}$ does not depend on $F$: by the probability integral transform, as in Theorem 2.6.1, the pooled sample may be replaced by a sample from $\mathrm{U}(0,1)$, and $D_{m,n}$ depends only on the arrangement of the labels $x$ and $y$ in the pooled ordering. The Smirnov test is thus a rank test, and its null distribution is computed by counting arrangements (Section 10.2.4).

**Example 10.2.2 (Saliva Production)** The rates of saliva production (ml/min) were measured for $7$ women and $21$ men:

| Women | 0.45 | 0.60 | 0.80 | 0.85 | 0.95 | 1.00 | 1.75 | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Men | 0.40 | 0.50 | 0.55 | 0.65 | 0.70 | 0.75 | 0.90 | 1.05 | 1.15 | 1.25 | 1.30 |
| | 1.35 | 1.45 | 1.50 | 1.85 | 1.90 | 2.30 | 2.55 | 2.70 | 2.85 | 3.85 |

Are the samples from the same distribution? The two EDFs are computed at each pooled value and their difference is largest just after $1.00$, where all six of the seven women's values but only $7$ of the men's lie at or below: $F_7(1.00)-G_{21}(1.00)=6/7-7/21=0.524$. The difference is positive almost everywhere, suggesting that the distribution function for women rises faster, that is, that women tend to produce less saliva.

```r
Fe <- c(0.45, 0.60, 0.80, 0.85, 0.95, 1.00, 1.75)
Ma <- c(0.40, 0.50, 0.55, 0.65, 0.70, 0.75, 0.90, 1.05, 1.15, 1.25, 1.30,
        1.35, 1.45, 1.50, 1.85, 1.90, 2.30, 2.55, 2.70, 2.85, 3.85)
ks.test(Fe, Ma)
ks.test(Fe, Ma, alternative = "greater")
```

```text
Exact two-sample Kolmogorov-Smirnov test
D = 0.52381, p-value = 0.09296
alternative hypothesis: two-sided

D^+ = 0.52381, p-value = 0.04648
alternative hypothesis: the CDF of x lies above that of y
```

In R the alternative `"greater"` refers to the distribution function of the first sample lying above that of the second, the alternative of $D_{m,n}^+$. The exact two-sided $p$-value is $0.093$ and the one-sided $0.046$. If a one-sided alternative had been specified in advance there would be moderate evidence that the women's distribution function lies above the men's; as an omnibus comparison, the evidence is weak.
:::

![EDFs of saliva production for $7$ women (red) and $21$ men (blue). The black segment marks the Smirnov distance $D_{7,21}=0.524$, attained at $x=1.00$.](./plots/smirnov-saliva.py)

### 10.2.3. The Asymptotic Distribution

**Theorem 10.2.1 (Smirnov)** Under $H_0\colon F=G$ with $F$ continuous, if $m,n\to\infty$ with $m/(m+n)\to\lambda\in(0,1)$, then for every $d>0$

$$
\lim\mathbb{P}\Bigl(\sqrt{\tfrac{mn}{m+n}}\,D_{m,n}\le d\Bigr)=1-2\sum_{k=1}^\infty(-1)^{k-1}\mathrm{e}^{-2k^2d^2},\qquad
\lim\mathbb{P}\Bigl(\sqrt{\tfrac{mn}{m+n}}\,D_{m,n}^+\le d\Bigr)=1-\mathrm{e}^{-2d^2}.
$$

The limit of the two-sided statistic is the **Kolmogorov distribution** (Definition 6.2.3), the same as for $\sqrt n D_n$ in the one-sample case; the one-sided limit is that of $\sqrt n D_n^+$. The only change is the normalizing factor.

**Proof** (Sketch.) By Donsker's theorem (Theorem 6.2.1), with $F=G$ the uniform distribution, $\sqrt m(F_m-F)$ and $\sqrt n(G_n-F)$ converge to independent Brownian bridges $B_1$ and $B_2$. Then

$$
\sqrt{\tfrac{mn}{m+n}}\,(F_m-G_n)=\sqrt{\tfrac{n}{m+n}}\,\sqrt m(F_m-F)-\sqrt{\tfrac{m}{m+n}}\,\sqrt n(G_n-F)
\ \Rightarrow\ \sqrt{1-\lambda}\,B_1-\sqrt{\lambda}\,B_2 ,
$$
and a linear combination of independent Brownian bridges with squared coefficients summing to $1$ is again a Brownian bridge (it is a centered Gaussian process with the covariance $s(1-t)$, $s\le t$). The continuous mapping theorem applied to the supremum gives the result. $\square$

The factor $mn/(m+n)=1/(1/m+1/n)$ is the harmonic-mean-type "effective sample size" of the comparison, and it is dominated by the smaller sample. This explains the practical warnings about the ratio $m/n$:

- If $m$ is fixed and $n\to\infty$, $G_n\to F$ uniformly (Glivenko–Cantelli), and $D_{m,n}$ tends to the one-sample statistic $D_m$ for the fixed $m$: the test degenerates into a one-sample test of the small sample against a distribution known almost exactly. The asymptotic distribution of Theorem 10.2.1 then does not apply.
- In practice one does not check whether $m/n$ "remains constant", but whether the observed ratio is very unbalanced (say beyond $1\colon10$) or the smaller sample is small; in such cases the exact distribution, which is always available for moderate $N$, or a permutation $p$-value should be used instead of the asymptotic one.
- For a fixed total $N=m+n$, $mn/(m+n)$ is maximized by $m=n$: a balanced design gives the most powerful comparison, a general principle for two-sample problems.

For the saliva data, $\sqrt{7\cdot21/28}\,D=1.200$; the asymptotic two-sided $p$-value is $\mathbb{P}(K>1.200)=0.112$ and the one-sided $\mathrm{e}^{-2(1.2)^2}=0.056$, noticeably larger than the exact values $0.093$ and $0.046$. With $7$ observations in the smaller sample, the asymptotic approximation is not yet accurate, and it errs on the conservative side here.

### 10.2.4. Exact Null Distribution by Lattice Paths

Under $H_0$ all $\binom{m+n}{m}$ arrangements of the labels are equally likely. Each arrangement can be drawn as a lattice path from $(0,0)$ to $(m,n)$ that moves one step to the right for an $x$ and one step up for a $y$. After $u$ of the $x$'s and $v$ of the $y$'s, $F_m-G_n=u/m-v/n$, so

$$
D_{m,n}=\max_{\text{path points}}\Bigl\lvert\frac um-\frac vn\Bigr\rvert ,
$$
and $n\lvert u/m-v/n\rvert$ is the vertical distance from the point $(u,v)$ to the diagonal $nx-my=0$ joining $(0,0)$ and $(m,n)$. The event $D_{m,n}<d$ means that the path stays strictly inside the band of vertical half-width $nd$ about the diagonal. Let $A(u,v)$ be the number of paths from $(0,0)$ to $(u,v)$ that stay strictly inside the band. Since the last step into $(u,v)$ comes either from $(u-1,v)$ or from $(u,v-1)$,

$$
A(u,v)=A(u-1,v)+A(u,v-1)\quad\text{for }(u,v)\text{ inside the band},\qquad A(u,v)=0\text{ outside},
$$
with $A(0,0)=1$, and then $\mathbb{P}(D_{m,n}\ge d)=1-A(m,n)/\binom{m+n}m$.

**Example 10.2.3 (A Small Case)** Let $m=3$, $n=4$ and the pooled ordering be $x\,y\,y\,x\,x\,y\,y$. Along the path, $F_3-G_4$ takes the values $1/3$, $1/12$, $-1/6$, $1/6$, $1/2$, $1/4$, $0$, so $D_{3,4}=1/2$, attained after the fifth observation. For $d=1/2$ the band has vertical half-width $nd=2$. Filling in the recursion over the points inside the band gives $A(3,4)=12$ of the $\binom73=35$ paths, so

$$
\mathbb{P}(D_{3,4}\ge\tfrac12)=1-\tfrac{12}{35}=0.657 .
$$
The observed arrangement is entirely typical of $H_0$.
:::

The same recursion with a one-sided band gives the distribution of $D_{m,n}^+$. For equal sample sizes there are closed forms by the reflection principle, for example $\mathbb{P}(D_{n,n}^+\ge k/n)=\binom{2n}{n-k}/\binom{2n}n$; in general, software uses recursions of this kind. R's `ks.test` computes exact $p$-values for moderate sample sizes, including, in recent versions, in the presence of ties.

### 10.2.5. Ties, Power and the Choice Between the Two Tests

Consider ties first. The Smirnov statistic is defined through the EDFs, so with ties one simply evaluates the EDFs at the distinct pooled values. If the null distribution for continuous data is still used, the test is conservative: Goodman (1954) showed that with discrete data the actual level is at most the nominal one. The exact conditional distribution given the tie pattern restores the correct level.

As for power, the Smirnov test is sensitive to every kind of difference between $F$ and $G$, and for this reason it is mainly a tool for a first look at the data. Against Lehmann alternatives $G=F^k$ it is more powerful than the runs test in large samples. Against a pure location or pure scale difference it is less powerful than a test designed for that difference: it can happen that the WMW or the Siegel–Tukey test establishes a difference while the Smirnov test does not. The large-sample efficiency of the Smirnov test against specific location or scale alternatives varies considerably with the population sampled (Capon 1965).

The two omnibus tests compare as follows.

| | Runs test | Smirnov test |
|---|---|---|
| Uses | the sequence of labels in the pooled ordering (or in a natural time or space order) | the maximal vertical distance between the two EDFs |
| Sensitive to | clustering of the labels; few runs indicate a difference in location, spread or shape | any difference between $F$ and $G$ |
| Assumptions | continuous data (ties make $R$ ambiguous) | continuous data (ties make the classical null distribution conservative) |
| Power | low; ARE $0$ against shifts relative to WMW | good omnibus power; lower than specific tests against pure shift or scale |
| Typical use | sequential data: are the groups randomly mixed along a production line, a transect, a time axis? | general comparison of two unordered random samples |

When the observations come in a meaningful order, for instance items from two production lines recorded in production order, the runs test can be applied to that order rather than to the order of the values; it then answers a different question, whether the groups are randomly interspersed in time. When the order is irrelevant, the Smirnov test is the better general-purpose test. Neither test replaces looking at the two EDFs, which shows where the distributions differ.

## 10.3. Quantile Regression

### 10.3.1. Motivation

Least squares regression models the conditional mean $\mathbb{E}[Y\mid\boldsymbol{x}]$. When the spread of $Y$ changes with $\boldsymbol{x}$, a common situation for incomes, expenditures, growth and many biological measurements, the mean tells only part of the story, and the usual inference for least squares is not valid under **heteroscedasticity**. A transformation such as $\log Y$ may stabilize the variance, but it changes the quantity being modelled and often leaves other problems (skewness, outliers) in place. Weighted least squares corrects the inference for the mean, but still describes only the mean.

A different approach is to model several percentiles of the response at once: the conditional median, the conditional $10$th and $90$th percentiles, and so on. Together these regression lines describe how the whole conditional distribution of $Y$ changes with $\boldsymbol{x}$. Note that this cannot be done by splitting the sample according to $y$, for instance by dropping the lowest $90\%$ of the observations and fitting least squares to the rest: selecting on the response biases the fit (truncation on the dependent variable), and it ignores the dependence of the conditional quantile on $\boldsymbol{x}$. The right tool is a loss function whose minimizer is a quantile.

### 10.3.2. Quantiles as Minimizers of the Check Loss

The $\tau$th **quantile** of a random variable $Y$ with distribution function $F$ is $Q_Y(\tau)=F^{-1}(\tau)=\inf\{y\colon F(y)\ge\tau\}$, $0<\tau<1$. Different losses give different centers:

$$
\arg\min_c\sum_{i=1}^n(y_i-c)^2=\bar y,\qquad
\arg\min_c\sum_{i=1}^n\lvert y_i-c\rvert=\text{a sample median}.
$$
Tilting the absolute loss gives the other quantiles.

**Definition 10.3.1 (Check Loss)** For $0<\tau<1$, the **check loss** (quantile loss, pinball loss) is

$$
\rho_\tau(r)=r\bigl(\tau-\boldsymbol{1}\{r<0\}\bigr)=\begin{cases}\tau r,& r\ge0,\\(\tau-1)r=(1-\tau)\lvert r\rvert,& r<0,\end{cases}
$$
equivalently $\rho_\tau(r)=\tau\max(0,r)+(1-\tau)\max(0,-r)$.

The name comes from the shape of the graph, a tilted "V" (a check mark). For $\tau=1/2$, $\rho_{1/2}(r)=\lvert r\rvert/2$. With $r=y-\hat y$, a positive residual (underestimation, $\hat y<y$) costs $\tau$ per unit and a negative residual (overestimation) costs $1-\tau$ per unit. For $\tau=0.9$ underestimation is penalized nine times as heavily as overestimation, so the fit moves up until only about $10\%$ of the observations lie above it.

**Theorem 10.3.1** Let $Y$ have a continuous distribution function $F$ with density $f$ and $\mathbb{E}\lvert Y\rvert<\infty$. Then $c\mapsto\mathbb{E}\rho_\tau(Y-c)$ is convex and minimized at $c=F^{-1}(\tau)$. Likewise, any minimizer of $\sum_{i=1}^n\rho_\tau(y_i-c)$ is a sample $\tau$-quantile.

**Proof** Write

$$
\mathbb{E}\rho_\tau(Y-c)=\tau\int_{-\infty}^\infty(y-c)f(y)\,\mathrm{d}y-\int_{-\infty}^c(y-c)f(y)\,\mathrm{d}y
=\tau(\mathbb{E}Y-c)-\int_{-\infty}^c(y-c)f(y)\,\mathrm{d}y .
$$
By Leibniz's rule the derivative of the last integral with respect to $c$ is $(c-c)f(c)-\int_{-\infty}^cf(y)\,\mathrm{d}y=-F(c)$, so

$$
\frac{\mathrm{d}}{\mathrm{d}c}\mathbb{E}\rho_\tau(Y-c)=-\tau+F(c),\qquad
\frac{\mathrm{d}^2}{\mathrm{d}c^2}\mathbb{E}\rho_\tau(Y-c)=f(c)\ge0 .
$$
The first derivative vanishes at $F(c)=\tau$, and the function is convex, so $c=F^{-1}(\tau)$ is a minimizer. For the sample version, apply the same argument to the empirical distribution: the function $c\mapsto\sum_i\rho_\tau(y_i-c)$ is convex and piecewise linear, with right derivative $n F_n(c)-n\tau$, which changes sign at a sample $\tau$-quantile. $\square$

![Left: the check loss $\rho_\tau$ for $\tau=0.1$, $0.5$, $0.9$, compared with half the squared loss. Right: the expected check loss $\mathbb{E}\rho_\tau(Y-c)$ for $Y\sim\Gamma(2,1)$ as a function of $c$; each curve is minimized at the corresponding quantile (dotted lines).](./plots/check-loss.py)

### 10.3.3. The Linear Quantile Regression Model

In linear regression the mean is modelled as $\mathbb{E}[Y_i\mid\boldsymbol{x}_i]=\beta_0+\beta_1x_{i1}+\dots+\beta_px_{ip}$ and the coefficients are estimated by minimizing the sum of squared residuals. Replacing the mean by a quantile and the squared loss by the check loss gives quantile regression.

**Definition 10.3.2 (Quantile Regression)** For a fixed $\tau\in(0,1)$, the linear **quantile regression** model assumes that the conditional $\tau$-quantile of the response is

$$
Q_\tau(Y_i\mid\boldsymbol{x}_i)=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}(\tau)=\beta_0(\tau)+\beta_1(\tau)x_{i1}+\dots+\beta_p(\tau)x_{ip},
$$
and estimates the coefficients by

$$
\hat{\boldsymbol{\beta}}(\tau)=\arg\min_{\boldsymbol{\beta}}\sum_{i=1}^n\rho_\tau\bigl(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}\bigr).
$$
For $\tau=1/2$ this is median regression, the **least absolute deviations** fit ([3.3.12](/3.3.12)).

Each level $\tau$ has its own coefficient vector $\boldsymbol{\beta}(\tau)$; a set of quantile regressions for $\tau=0.1,0.2,\dots,0.9$ describes the conditional distribution. The coefficient $\beta_j(\tau)$ is the change in the conditional $\tau$-quantile of $Y$ per unit change in $x_j$, the other covariates held fixed. If the errors are i.i.d. and independent of $\boldsymbol{x}$ (the classical location model $Y=\boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}+\varepsilon$), all quantile lines are parallel: only the intercept depends on $\tau$. Slopes that change with $\tau$ are the signature of heteroscedasticity or, more generally, of covariates that change the shape of the distribution.

**Example 10.3.1 (One Outlier)** Seven points $(x_i,y_i)$ with $x=1,\dots,7$ and $y=1.5, 2.3, 2.8, 4.1, 5.3, 0, 6.8$ lie close to a line except the sixth, $(6,0)$.

```r
d <- data.frame(predictor = 1:7, outcome = c(1.5, 2.3, 2.8, 4.1, 5.3, 0, 6.8))
coef(lm(outcome ~ predictor, data = d))                    # 1.286, 0.493
coef(quantreg::rq(outcome ~ predictor, data = d, tau = 0.5)) # 0.500, 0.900
```

The least squares line $\hat y=1.29+0.49x$ is pulled down by the outlier, whose squared residual dominates the fit; without the outlier, with $y_6=5.9$, least squares would give $0.44+0.91x$. The median regression line $\hat y=0.5+0.9x$ is essentially unaffected: it passes exactly through three of the points ($x=2,4,7$), with two points above and two below, and the outlier enters only through the sign of its residual. That a median regression fit interpolates $p+1$ observations (here $2$) is a general property of the linear programming solution (Section 10.3.4).
:::

### 10.3.4. Computation

The objective $\sum_i\rho_\tau(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})$ is convex but not differentiable, and there is no closed-form solution. Three approaches are common.

The first is linear programming. Split each residual and each coefficient into positive and negative parts, $u_i=\max(0,r_i)$, $v_i=\max(0,-r_i)$, $\boldsymbol{\beta}=\boldsymbol{l}-\boldsymbol{m}$ with $\boldsymbol{l},\boldsymbol{m}\ge\boldsymbol{0}$. Then $r_i=u_i-v_i$, $\rho_\tau(r_i)=\tau u_i+(1-\tau)v_i$, and the problem becomes the linear program

$$
\min_{\boldsymbol{u},\boldsymbol{v},\boldsymbol{l},\boldsymbol{m}}\ \tau\boldsymbol{1}^{\mathsf T}\boldsymbol{u}+(1-\tau)\boldsymbol{1}^{\mathsf T}\boldsymbol{v}
\quad\text{subject to}\quad X(\boldsymbol{l}-\boldsymbol{m})+\boldsymbol{u}-\boldsymbol{v}=\boldsymbol{y},\qquad \boldsymbol{u},\boldsymbol{v},\boldsymbol{l},\boldsymbol{m}\ge\boldsymbol{0}.
$$
An optimum of a linear program is attained at a vertex of the feasible region, which here corresponds to a fit that passes through $p+1$ observations (if $X$ has $p+1$ columns). Simplex-type algorithms move from vertex to vertex and are fast and exact for small and medium problems; R's `quantreg::rq` uses the Barrodale–Roberts simplex variant by default (`method = "br"`). Interior point methods move through the interior of the feasible region along a smooth path toward the optimum and are faster for large $n$ (`method = "fn"`, Frisch–Newton).

The second is iteratively reweighted least squares. Since $\rho_\tau(r)=w(r)\,r^2$ with $w(r)=\tau/\lvert r\rvert$ for $r\ge0$ and $(1-\tau)/\lvert r\rvert$ for $r<0$, the problem looks like a weighted least squares problem whose weights depend on the residuals. Starting from the least squares fit, one computes $w_i^{(t)}$ from the current residuals and sets

$$
\hat{\boldsymbol{\beta}}^{(t+1)}=\bigl(X^{\mathsf T}W^{(t)}X\bigr)^{-1}X^{\mathsf T}W^{(t)}\boldsymbol{y},\qquad W^{(t)}=\operatorname{diag}\bigl(w_1^{(t)},\dots,w_n^{(t)}\bigr).
$$
This is the same **iteratively reweighted least squares** idea as for robust regression ([3.3.12](/3.3.12)); in practice the weights are bounded, $w=\tau/\max(\lvert r\rvert,\delta)$, to avoid division by zero, and convergence can be slow near the solution. It is useful mainly for teaching and for small problems.

The third uses gradient methods. The loss has the subgradient

$$
\nabla_{\boldsymbol{\beta}}\sum_i\rho_\tau(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})=\sum_{i\colon r_i<0}\boldsymbol{x}_i-\tau\sum_{i=1}^n\boldsymbol{x}_i
$$
(at points with $r_i\ne0$), and **gradient descent** or its stochastic variants take steps $\boldsymbol{\beta}^{(t+1)}=\boldsymbol{\beta}^{(t)}-\eta\nabla$. This scales to very large or distributed data, and it is how the pinball loss is used to train neural networks that predict quantiles, but it converges only to an approximate solution.

| Method | Idea | Suited for | In `quantreg` |
|---|---|---|---|
| Linear programming (simplex, interior point) | split residuals into nonnegative parts; solve the LP exactly | small to large data, exact solution | `method = "br"` (default), `"fn"` for large $n$ |
| IRLS | a sequence of weighted least squares fits | teaching, small data | not exposed; easy to program |
| (Stochastic) gradient descent | step against the subgradient | very large or distributed data, neural networks | not provided |

### 10.3.5. Examples

**Example 10.3.2 (Engel's Food Expenditure Data)** The classical `engel` data set in the R package `quantreg` contains the annual household income and the annual food expenditure (both in Belgian francs) of $235$ Belgian working-class households in the nineteenth century. A scatter plot shows that expenditure increases with income and that its spread increases as well; the residual plots of the least squares fit show a funnel shape and heavy tails.

```r
library(quantreg)
data(engel)
lr <- lm(foodexp ~ income, data = engel)
mr <- rq(foodexp ~ income, data = engel, tau = 0.5)     # median regression
summary(mr)
```

```text
Coefficients:
            coefficients lower bd  upper bd
(Intercept)  81.48225    53.25915 114.01156
income        0.56018     0.48702   0.60199
```

The intervals reported by `summary.rq` for small samples are obtained by inverting a rank test (they need not be symmetric about the estimate). The median food expenditure increases by about $0.56$ franc per franc of income. Fitting $\tau=0.1,0.2,\dots,0.9$ shows slopes that increase with $\tau$, the upper quantile lines being steeper and fanning out; the least squares line lies above the median line at low incomes, pulled up by a few large expenditures. The figure below reproduces the same features with simulated data of the same size. The lines for large $\tau$ lie closer together than those for small $\tau$, so the conditional distribution of food expenditure is skewed to the left at given income: a few households spend much less than is typical.
:::

![Quantile regression for simulated heteroscedastic expenditure data ($n=235$, spread proportional to income). Left: fitted lines for $\tau=0.1$, $0.25$, $0.5$, $0.75$, $0.9$ and the least squares line (dashed). Right: the slope estimate as a function of $\tau$ with a $90\%$ pairs-bootstrap band ($60$ replicates), against the constant least squares slope. Under homoscedasticity the slope curve would be flat.](./plots/quantreg-lines.py)

**Example 10.3.3 (Wages and Job Class)** The `Wage` data (R package `ISLR2`) give the wages (in thousands of dollars) of $3000$ male workers in the Mid-Atlantic region of the USA, with covariates including the job class, industrial or information. For the regression of wage on job class alone, diagnostic checks of the least squares fit report strongly non-normal residuals and unequal variances in the two groups. The fitted coefficients are:

| Fit | Intercept (industrial) | Information |
|---|---|---|
| Least squares | 103.32 | 17.27 |
| $\tau=0.1$ | 66.04 | 8.40 |
| $\tau=0.5$ | 99.69 | 12.96 |
| $\tau=0.9$ | 145.81 | 25.96 |

```r
library(ISLR2); library(quantreg)
coef(lm(wage ~ jobclass, data = Wage))
coef(rq(wage ~ jobclass, data = Wage, tau = c(0.1, 0.5, 0.9)))
q <- rq(wage ~ jobclass, data = Wage, tau = seq(0.1, 0.9, by = 0.1))
plot(summary(q), parm = "jobclass2. Information")
```

With a single binary covariate the fits have a simple meaning. Least squares gives the mean of the industrial group as intercept and the difference of the two group means as slope; quantile regression gives the $\tau$-quantile of the industrial group and the difference of the two groups' $\tau$-quantiles. Quantile regression with one binary covariate is therefore exactly the comparison of the quantiles of two independent samples. Here the information–industrial gap is about $8$ at the $10$th percentile, $13$ at the median and $26$ at the $90$th percentile: the information sector's wage distribution is not just shifted but stretched upward. The mean difference of $17.3$ overstates the gap at the bottom of the distribution and understates it at the top.

Adding age and race to the model and plotting the coefficients for $\tau=0.05,\dots,0.95$ shows the same phenomenon for every covariate. For example, the estimated difference between Black and White workers (with the same job class and age) is close to zero at the lowest quantiles and widens to about $-30$ at the upper quantiles: the effects of job class, age and race on wages are not constant but depend on the part of the wage distribution considered.
:::

The interpretation of these coefficients needs care. They compare quantiles of two distributions; they do not say how the wage of a particular worker would change if that worker switched sectors. Reading $\beta(0.1)=8.4$ as "a low earner gains $8.4$ by moving to the information sector" requires that a worker would keep the same rank in the wage distribution after switching (rank invariance) and that job class is not confounded with other determinants of wages, neither of which the data establish. The quantile regression describes the conditional distributions honestly; causal claims need the designs and assumptions of [3.9](/3.9).

### 10.3.6. Properties and Limits

The main properties of quantile regression are:

- The model is distribution-free: no assumption is made about the form of the error distribution; heteroscedasticity is not a nuisance but part of what is estimated. Under the location model the estimates are consistent and asymptotically normal, $\sqrt n(\hat{\boldsymbol{\beta}}(\tau)-\boldsymbol{\beta}(\tau))\xrightarrow{d}\mathcal{N}\bigl(\boldsymbol{0},\,\tau(1-\tau)f(F^{-1}(\tau))^{-2}(\mathbb{E}\boldsymbol{x}\boldsymbol{x}^{\mathsf T})^{-1}\bigr)$, which generalizes the asymptotic normality of sample quantiles (Theorem 5.2.1); the sparsity $1/f$ appears, so estimates for extreme $\tau$, where data are scarce, are much less precise.
- The fit is equivariant under monotone transformations: for any increasing function $h$, $Q_\tau(h(Y)\mid\boldsymbol{x})=h\bigl(Q_\tau(Y\mid\boldsymbol{x})\bigr)$. A model fitted to $\log Y$ can be transformed back to quantiles of $Y$ exactly, which is not true for means.
- It is robust in the response: the fit depends on the responses only through the signs of the residuals near the fitted plane, so it is not affected by how far an outlying $y$ lies from the line (Example 10.3.1). Even the mean of the errors need not exist: with Cauchy errors least squares is useless and quantile regression works.
- It is not robust in the covariates: a single point with an extreme value of $\boldsymbol{x}$, a high-**leverage** point, can still pull the fitted line arbitrarily far, as for least squares. The breakdown point of median regression is $1/n$ in the design. Quantile regression is robust to outliers in $Y$, not in $\boldsymbol{x}$.

The limitations follow from the same features. Each $\tau$ is fitted separately, so the estimated quantile lines may cross for some $\boldsymbol{x}$ (especially near the edge of the data), which is logically impossible for true quantiles; this is a sign of misspecification or of too little data. Extreme quantiles need enough data in the tails. Inference is less routine than for least squares: confidence intervals come from inverting rank tests, from estimates of the sparsity, or from the bootstrap (resampling pairs $(\boldsymbol{x}_i,y_i)$).

| | Least squares | Quantile regression |
|---|---|---|
| Target | conditional mean $\mathbb{E}[Y\mid\boldsymbol{x}]$ | conditional quantiles $Q_\tau(Y\mid\boldsymbol{x})$, hence the conditional distribution |
| Loss | squared | check loss $\rho_\tau$ |
| Error assumptions | for exact inference: normal, homoscedastic | none on the form; heteroscedasticity allowed |
| Outliers in $Y$ | sensitive | insensitive |
| High-leverage $\boldsymbol{x}$ | sensitive | sensitive |
| Data requirements | works with small $n$ | needs enough observations in the tails of interest |
| Computation | closed form | linear programming |

Quantile regression is the method of choice when interest lies in the tails (low birth weights, high pollution levels, low and high earners), when the covariates change the spread or shape of the response, and when the response has heavy tails or outliers. When the errors are close to normal and homoscedastic and the mean is the target, least squares is more efficient.

## Summary

- Dispersion (Section 10.1): the Siegel–Tukey test (Definition 10.1.1) ranks the pooled sample alternately from both ends toward the middle and applies the WMW test; small rank sum means more dispersion. It needs a common center: align by a known shift (exact) or by the difference of sample medians (approximate). Tire data: $U_A=70$, $p=0.098$ (Example 10.1.1).
- Common distribution, runs (Section 10.2.1): few runs of the labels in the pooled ordering indicate a difference; one-sided test on $R$ with the distribution of Theorem 7.4.1. Low power, ARE $0$ against shifts; useful for sequential data. TV data: $R=9=\mathbb{E}R$, $p=0.595$ (Example 10.2.1).
- Common distribution, Smirnov (Definition 10.2.1): $D_{m,n}=\sup\lvert F_m-G_n\rvert$, a rank statistic; $\sqrt{mn/(m+n)}D_{m,n}$ has the Kolmogorov limit (Theorem 10.2.1), valid only when both samples grow, with the factor dominated by the smaller sample; exact $p$-values by lattice paths (Section 10.2.4); conservative with ties. Saliva data: $D=0.524$, exact $p=0.093$ (two-sided), $0.046$ (one-sided).
- Choice: specific tests (WMW, Siegel–Tukey) for specific differences; Smirnov for an omnibus comparison; runs test for groups in a natural order.
- Check loss (Definition 10.3.1): $\rho_\tau(r)=r(\tau-\boldsymbol{1}\{r<0\})$; its expected value is minimized by the $\tau$-quantile (Theorem 10.3.1).
- Quantile regression (Definition 10.3.2): $Q_\tau(Y\mid\boldsymbol{x})=\boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}(\tau)$, fitted by minimizing the check loss; $\tau=1/2$ is LAD. Computed by linear programming (fit through $p+1$ points), IRLS or gradient methods. Slopes varying with $\tau$ reveal heteroscedasticity; with a binary covariate, coefficients are differences of group quantiles (Example 10.3.3). Robust to outliers in $Y$, not to high-leverage $\boldsymbol{x}$; coefficients are not individual causal effects.

## Questions

1. Why must the two samples be aligned before the Siegel–Tukey test, and why does aligning by the sample medians make the test only approximately exact?

   **Answer** The ranks measure distance from the middle of the pooled sample. If the centers differ, one sample occupies one end of the ordering and the other sample the other end; both then receive small ranks, and differences in location are mistaken for differences in spread. Subtracting a known shift preserves exchangeability under $H_0$, so the WMW null distribution applies exactly. The difference of sample medians is computed from the data, so after the subtraction the pooled observations are no longer exchangeable, and the null distribution is only approximately correct; the error is small for moderate samples.
2. Apply the two-sample runs test to the tire data of Example 10.1.1 (without alignment). What does the result suggest about the difference between the two failure types, and what is its limitation?

   **Answer** The pooled ordering of the raw data is $\mathrm{BBBBBB\,A\,B\,A\,BB\,AA\,B\,A\,B\,A\,B\,AA}$: the six smallest times are all type B, and the four largest values alternate. The tie at $230$ can be broken either way, and both orders give $R=12$ runs. With $m=8$, $n=12$, $\mathbb{E}R=1+2\cdot96/20=10.6$, and the exact $p$-value is $\mathbb{P}(R\le12)=0.82$: the runs test sees nothing unusual, although the type B times are lower and more spread out. Its limitation is low power: the long initial run of six B's counts only as one run, and the information in where the runs lie is discarded.
3. Show that for $m=n$ and integer $k\ge1$, $\mathbb{P}(D_{n,n}^+\ge k/n)=\binom{2n}{n-k}/\binom{2n}{n}$.

   **Answer** In the lattice path from $(0,0)$ to $(n,n)$, $nF_n-nG_n=u-v$, so $D^+_{n,n}\ge k/n$ if and only if the path reaches the line $u-v=k$. By the reflection principle, reflecting the part of such a path after its first visit to the line $u-v=k$ gives a bijection with all paths from $(0,0)$ to the reflected end point $(n+k,n-k)$, of which there are $\binom{2n}{n-k}$. Dividing by the total number $\binom{2n}n$ of paths gives the result.
4. Verify Theorem 10.3.1 for a sample: with $y=(1,2,3,10)$ and $\tau=0.75$, find all minimizers of $\sum_i\rho_\tau(y_i-c)$.

   **Answer** The right derivative is $nF_n(c)-n\tau=4F_n(c)-3$. For $c<3$, $F_n(c)\le1/2$ and the derivative is at most $-1$; for $3\le c<10$, $F_n(c)=3/4$ and the derivative is $0$; for $c\ge10$ it is $1$. So the objective decreases up to $3$, is constant on $[3,10]$ and increases after $10$: every $c\in[3,10]$ minimizes it, and these are exactly the sample $0.75$-quantiles (any value between $y_{(3)}$ and $y_{(4)}$). The minimum value is $6$: at $c=3$ the residuals $-2,-1,0,7$ give $0.25\cdot3+0.75\cdot7=6$, and at $c=10$ the residuals $-9,-8,-7,0$ give $0.25\cdot24=6$, as they must on the flat part; at $c=2$ or $c=11$ the loss is $7$.
5. In a simple regression with i.i.d. errors independent of $x$, what do the quantile regression lines for different $\tau$ look like? What does it mean if the estimated slopes increase with $\tau$?

   **Answer** If $Y=\beta_0+\beta_1x+\varepsilon$ with $\varepsilon$ independent of $x$, then $Q_\tau(Y\mid x)=\beta_0+F_\varepsilon^{-1}(\tau)+\beta_1x$: the lines are parallel, with intercepts that differ by the error quantiles, and the slope does not depend on $\tau$. Slopes increasing with $\tau$ mean that the upper conditional quantiles grow faster with $x$ than the lower ones, so the conditional distribution spreads out as $x$ increases, as in a model $Y=\beta_0+\beta_1x+(\gamma_0+\gamma_1x)\varepsilon$ with $\gamma_1>0$, for which $\beta_1(\tau)=\beta_1+\gamma_1F_\varepsilon^{-1}(\tau)$.
6. Explain why median regression is not robust against a single observation with an extreme value of $x$.

   **Answer** The median regression line passes through $p+1$ observations and balances the signs of the residuals. A point far out in the $x$ direction has a residual that changes by a large amount for a small change of slope, so the fit can reduce the loss by passing through or near it: moving that single point far away in $x$ and $y$ drags the line with it. The insensitivity holds only for the size of the residuals in the $y$ direction at fixed design points; the design itself enters the loss linearly, so one high-leverage point can determine the slope, and the breakdown point in the design is $1/n$.
