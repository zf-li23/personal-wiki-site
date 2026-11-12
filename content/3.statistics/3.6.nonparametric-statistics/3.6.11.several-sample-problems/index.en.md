---
title: Several-Sample Problems
description: "Rank tests for three or more samples. Independent samples: the Kruskal–Wallis test (from WMW and one-way ANOVA, exact and chi-squared p-values, ties), multiple comparisons with Dunn's test and how to report a significant global test with no significant pair; the Jonckheere–Terpstra test for ordered alternatives. Related samples in randomized blocks: the Friedman test and its relation to repeated-measures ANOVA, the Page test, Cochran's Q test for binary responses; and the squared ranks test for equal variances."
---

The two-sample methods of [3.6.9](/3.6.9) and [3.6.10](/3.6.10) extend to three or more samples in the same way that the two-sample $t$-test extends to the analysis of variance. Two designs must be distinguished. In a completely randomized design (CRD) the samples are independent, and the rank methods pool all observations and rank them together: the Kruskal–Wallis test is the rank version of one-way ANOVA, and the Jonckheere–Terpstra test is its refinement for an ordered alternative (Sections 11.1 and 11.2). In a randomized complete block design (RCBD) each block receives every treatment, the samples are related, and the observations are ranked within each block: the Friedman test is the rank version of the two-way ANOVA without replication, the Page test its refinement for ordered alternatives, and Cochran's $Q$ test the special case of binary responses (Section 11.3). Section 11.4 compares variances with the squared ranks test, and Section 11.5 collects the methods in one table.

All these tests are permutation tests in the sense of [3.6.1](/3.6.1): under the null hypothesis the observations (in a CRD) or the observations within each block (in an RCBD) are exchangeable, and replacing them by ranks makes the null distribution independent of the data. The parametric counterparts are developed in [3.8.3](/3.8.3) and [3.8.6](/3.8.6); the multiple-comparison problem in [3.8.4](/3.8.4).

## 11.1. Several Independent Samples: The Kruskal–Wallis Test

### 11.1.1. From the WMW Test and One-Way ANOVA

**Example 11.1.1 (Home Prices)** A British estate agency sells properties in three villages $A$, $B$ and $C$. The homes for sale are offered at the following prices (thousand pounds):

| Village $A$ | 139 | 145 | 171 | |
|---|---|---|---|---|
| Village $B$ | 151 | 163 | 188 | 197 |
| Village $C$ | 199 | 250 | 360 | |

Are there differences in the typical price level between the villages? With three, four and three observations nothing can be said about normality, and the value $360$ looks like an outlier.
:::

Kruskal and Wallis (1952) extended the WMW test to $k\ge3$ samples. Pool all $N=\sum_in_i$ observations and rank them from $1$ to $N$. If the samples come from the same population, each sample should contain a mixture of low and high ranks, and the mean rank $\bar R_i$ of every sample should be close to the overall mean rank $(N+1)/2$. The test statistic measures the spread of the $\bar R_i$ about $(N+1)/2$, exactly as the one-way ANOVA $F$ statistic measures the spread of the group means about the grand mean.

Write $x_{ij}$ for the $j$th observation of the $i$th sample, $R_{ij}$ for its rank in the pooled sample, $R_{i\cdot}=\sum_jR_{ij}$ for the rank sum and $\bar R_i=R_{i\cdot}/n_i$ for the mean rank of sample $i$.

**Definition 11.1.1 (Kruskal–Wallis Test)** The **Kruskal–Wallis test** of $H_0$: the $k$ samples come from the same continuous distribution, rejects for large values of

$$
H=\frac{12}{N(N+1)}\sum_{i=1}^kn_i\Bigl(\bar R_i-\frac{N+1}2\Bigr)^2=\frac{12}{N(N+1)}\sum_{i=1}^k\frac{R_{i\cdot}^2}{n_i}-3(N+1),
$$
whose exact null distribution is obtained by permutation, and which is approximately $\chi^2_{k-1}$ for large samples.

**Proposition 11.1.1** Let $\mathrm{SS}_{\mathrm{Tr}}=\sum_in_i(\bar R_i-\bar R)^2$ and $\mathrm{SS}_{\mathrm T}=\sum_{i,j}(R_{ij}-\bar R)^2$ be the treatment and total sums of squares of the ranks, $\bar R=(N+1)/2$. Then

$$
H=\frac{\mathrm{SS}_{\mathrm{Tr}}}{\mathrm{SS}_{\mathrm T}/(N-1)},
$$
the one-way ANOVA treatment sum of squares of the ranks divided by their total variance. Without ties $\mathrm{SS}_{\mathrm T}/(N-1)=N(N+1)/12$, and the two expressions of Definition 11.1.1 agree. For $k=2$, $H$ is the square of the standardized WMW statistic.

**Proof** Without ties the ranks are $1,\dots,N$, so $\mathrm{SS}_{\mathrm T}=\sum_{r=1}^Nr^2-N\bar R^2=\frac{N(N+1)(2N+1)}6-\frac{N(N+1)^2}4=\frac{N(N^2-1)}{12}$, and $\mathrm{SS}_{\mathrm T}/(N-1)=N(N+1)/12$. For the computational form, expand

$$
\sum_in_i(\bar R_i-\bar R)^2=\sum_i\frac{R_{i\cdot}^2}{n_i}-2\bar R\sum_iR_{i\cdot}+N\bar R^2=\sum_i\frac{R_{i\cdot}^2}{n_i}-N\bar R^2,
$$
since $\sum_iR_{i\cdot}=N\bar R$; multiplying by $12/(N(N+1))$ gives $\frac{12}{N(N+1)}\sum_iR_{i\cdot}^2/n_i-3(N+1)$. For $k=2$, $\bar R_1-\bar R=\frac{n_2}{N}(\bar R_1-\bar R_2)$ and similarly for $\bar R_2$, and a short computation gives $H=(W_x-\mathbb{E}W_x)^2/\operatorname{Var}(W_x)$ with the moments of Theorem 9.3.1. $\square$

The chi-squared approximation has the same origin as in ANOVA. Under $H_0$, each $\bar R_i$ is approximately normal with mean $\bar R$ and variance $\frac{(N+1)(N-n_i)}{12\,n_i}$ (sampling without replacement), and the $k$ standardized deviations satisfy one linear constraint, $\sum_in_i(\bar R_i-\bar R)=0$, which leaves $k-1$ degrees of freedom. The approximation is customarily considered adequate when $k\ge3$ and every $n_i\ge5$; for smaller samples the exact distribution should be used.

**Example 11.1.2 (Home Prices, Continued)** The ten prices in increasing order belong to $A,A,B,B,A,B,B,C,C,C$, so the rank sums are $R_{A\cdot}=1+2+5=8$, $R_{B\cdot}=3+4+6+7=20$ and $R_{C\cdot}=8+9+10=27$, with mean ranks $2.67$, $5$ and $9$ against the overall $5.5$. Then $\sum R_{i\cdot}^2/n_i=64/3+400/4+729/3=364.33$ and

$$
H=\frac{12\times364.33}{10\times11}-3\times11=6.745 .
$$
The chi-squared approximation with $2$ degrees of freedom gives $p=0.034$. The exact permutation distribution of $H$ over the $10!/(3!\,4!\,3!)=4200$ equally likely allocations of the ranks gives $\mathbb{P}(H\ge6.745)=42/4200=0.010$: with such small samples the asymptotic $p$-value is three times too large.

```r
HP <- c(139, 145, 171, 151, 163, 188, 197, 199, 250, 360)
V <- factor(rep(c("A", "B", "C"), times = c(3, 4, 3)))
kruskal.test(HP ~ V)
library(NSM3)                                   # exact p-value
pKW(list(HP[1:3], HP[4:7], HP[8:10]), method = "Exact")
```

```text
Kruskal-Wallis rank sum test
Kruskal-Wallis chi-squared = 6.7455, df = 2, p-value = 0.0343

Kruskal-Wallis H Statistic: 6.7455
Exact upper-tail probability: 0.01
```

There is strong evidence that the price levels differ between the villages; properties in village $C$ appear to be the most expensive (it may have more executive-style homes). The outlier $360$ has no special influence: as the largest observation it simply has rank $10$.
:::

![Home prices in three villages. Left: raw prices. Right: pooled ranks with the mean rank of each village (bars) against the overall mean rank $5.5$; the Kruskal–Wallis statistic measures the spread of the mean ranks.](./plots/kw-homes.py)

### 11.1.2. Assumptions and Hypotheses

The Kruskal–Wallis test, like the WMW test, requires:

1. independence of all observations, within and between the samples;
2. random samples from the populations (or random allocation of units to treatments);
3. a response measured on at least an ordinal scale, so that it can be ranked.

It does not require normality or equal variances. Its null hypothesis is that the $k$ populations have identical distributions, $F_1=\dots=F_k$, and under this hypothesis the test is exact. As with the WMW test (Section 9.5), the test is often described as a test of equal medians, $H_0\colon\theta_1=\dots=\theta_k$ against $H_1$: the medians are not all equal. This reading is justified only when the populations differ at most by shifts, that is, have the same shape and spread. Otherwise the test detects differences in the tendency of one population to produce larger values than another ($\mathbb{P}(X_i>X_j)\ne\frac12$), and its level for a hypothesis about medians alone is not guaranteed.

### 11.1.3. Ties

With ties, all observations in a tied group receive the midrank (Definition 3.5.2). The mean rank is still $(N+1)/2$, but the total sum of squares of the ranks is smaller:

$$
\mathrm{SS}_{\mathrm T}=\frac{N(N^2-1)}{12}-\frac1{12}\sum_g(d_g^3-d_g),
$$
where $d_g$ is the size of the $g$th tied group. Using the form of Proposition 11.1.1 with the actual $\mathrm{SS}_{\mathrm T}$ gives the tie-corrected statistic

$$
H_c=\frac{\mathrm{SS}_{\mathrm{Tr}}}{\mathrm{SS}_{\mathrm T}/(N-1)}=\frac{H}{1-\sum_g(d_g^3-d_g)/(N^3-N)},
$$
where $H$ is computed with midranks by the no-tie formula. The correction always increases $H$ (and decreases the $p$-value), usually only slightly. The exact test uses the permutation distribution of the observed midranks.

**Example 11.1.3 (Sentence Lengths)** For three writers of detective fiction, the numbers of sentences per page on randomly selected pages in a work by each were:

| C. E. Vulliamy | 13 | 27 | 26 | 22 | 26 | | |
|---|---|---|---|---|---|---|---|
| Ellery Queen | 43 | 35 | 47 | 32 | 31 | 37 | |
| Helen McCloy | 33 | 37 | 33 | 26 | 44 | 33 | 54 |

Are these samples from identical populations? With $N=18$ there are three tied groups: $26$ three times, $33$ three times and $37$ twice. The rank sums are $17$, $72.5$ and $81.5$, the mean ranks $3.4$, $12.08$ and $11.64$. The no-tie formula gives $H=9.061$; the correction factor is $1-\frac{(27-3)+(27-3)+(8-2)}{18^3-18}=1-\frac{54}{5814}=0.9907$, so $H_c=9.146$ and $p=\mathbb{P}(\chi^2_2>9.146)=0.010$. There is strong evidence of a difference in the number of sentences per page: Vulliamy has fewer sentences per page, that is, longer sentences.
:::

### 11.1.4. Which Samples Differ? Multiple Comparisons

A significant Kruskal–Wallis test says that the samples do not all come from the same population, not which of them differ. The natural follow-up is a set of pairwise comparisons with a correction for **multiple comparisons** ([3.8.4](/3.8.4)), which controls the **family-wise error rate** (Bonferroni, Holm) or the **false discovery rate** (Benjamini–Hochberg).

There are two ways to make the pairwise comparisons. The first is to apply the WMW test to each pair of samples separately, re-ranking the two samples each time. The second, which is consistent with the Kruskal–Wallis test, uses the mean ranks from the pooled ranking.

**Definition 11.1.2 (Dunn's Test)** After a Kruskal–Wallis test, **Dunn's test** compares samples $i$ and $j$ through the difference of their mean pooled ranks,

$$
z_{ij}=\frac{\bar R_i-\bar R_j}{\sqrt{\dfrac{N(N+1)}{12}\Bigl(\dfrac1{n_i}+\dfrac1{n_j}\Bigr)}},
$$
referred to $\mathcal{N}(0,1)$, with the $p$-values adjusted for the number of comparisons (Bonferroni or Holm). With ties, $N(N+1)/12$ is replaced by $\mathrm{SS}_{\mathrm T}/(N-1)$.

The denominator is the null standard deviation of $\bar R_i-\bar R_j$ when the ranks are a random permutation of $1,\dots,N$. Because every comparison uses the same pooled ranks, the comparisons are mutually consistent and use the information in all samples, which pairwise re-ranking does not.

**Example 11.1.4 (Home Prices: A Puzzling Result)** The pairwise WMW tests with Benjamini–Hochberg adjustment give:

```r
pairwise.wilcox.test(HP, V, p.adjust.method = "BH")
```

```text
Pairwise comparisons using Wilcoxon rank sum exact test
  A    B
B 0.23 -
C 0.15 0.15
P value adjustment method: BH
```

The global test is significant ($p=0.034$, exact $0.010$), but no pair is. Is this a contradiction? No, and the reasons are instructive.

1. With three observations in each of $A$ and $C$, the smallest possible two-sided exact $p$-value of the WMW test is $2/\binom63=0.10$, attained here (all of $A$ lie below all of $C$). For $B$ against $C$ the minimum $2/\binom73=0.057$ is attained as well. Such tests cannot reach $0.05$, before any adjustment: the raw $p$-values are $0.229$, $0.100$ and $0.057$, and the BH adjustment raises the last two to $0.15$.
2. The global test combines the evidence from all ten observations, the pairwise tests use only part of it. Dunn's test, which uses the pooled ranks, gives $z_{AC}=(2.67-9)/\sqrt{\frac{110}{12}\cdot\frac23}=-2.56$, raw $p=0.010$, Holm-adjusted $0.031$; the comparisons $B$–$C$ ($z=-1.73$, adjusted $0.17$) and $A$–$B$ ($z=-1.01$, adjusted $0.31$) are not significant. The global significance is driven by the contrast between $A$ and $C$.
:::

When the global test is significant but adjusted pairwise tests are not, several strategies are available, and they should be chosen before seeing the data:

- Report **effect sizes** with confidence intervals instead of only $p$-values, for instance the Hodges–Lehmann estimates of the pairwise shifts ([3.6.9](/3.6.9)) with their intervals, or a rank-based measure of the variance explained. For the home prices, the Hodges–Lehmann estimate of the price difference between villages $C$ and $A$ is $105$ (thousand pounds), the median of the nine differences; with three observations per village even the widest possible interval, from the smallest to the largest difference ($28$ to $221$), has confidence only $90\%$. Such a statement describes the data better than "no significant pairs".
- Distinguish confirmatory from exploratory analysis. In an exploratory study one may report raw and adjusted $p$-values side by side and identify the comparisons that look promising for a follow-up study; in a confirmatory study only the adjusted results count.
- Reduce the number of comparisons. If one group is a control and the question is which treatments differ from it, only $k-1$ comparisons are needed instead of $k(k-1)/2$: a many-to-one comparison with Dunn's statistic and a Bonferroni or Holm adjustment over $k-1$ tests, or Steel's many-to-one rank test, which plays the role of **Dunnett's test** in the rank setting. The penalty for multiplicity is then much smaller.
- Check sample sizes and ties. Very small groups and many ties make pairwise rank tests discrete and conservative; the honest conclusion is that the global test indicates a difference in location but the data are too few to locate it, and a larger study is needed.

## 11.2. Ordered Alternatives: The Jonckheere–Terpstra Test

### 11.2.1. The Test

Often the treatments have a natural order, such as increasing doses or speeds, and the alternative of interest is a monotone trend, $H_1\colon\theta_1\le\theta_2\le\dots\le\theta_k$ with at least one strict inequality (or the reverse). The Kruskal–Wallis test is an omnibus test: it treats every pattern of differences alike and wastes power against the specific ordered alternative. A test that looks only in the predicted direction is more powerful.

**Definition 11.2.1 (Jonckheere–Terpstra Test)** For independent samples $1,\dots,k$ arranged in the order predicted by the alternative, let

$$
U_{rs}=\sum_{h=1}^{n_r}\sum_{j=1}^{n_s}\Bigl[\boldsymbol{1}\{X_{rh}<X_{sj}\}+\tfrac12\boldsymbol{1}\{X_{rh}=X_{sj}\}\Bigr],\qquad1\le r<s\le k,
$$
be the Mann–Whitney count of pairs in which the observation from the later sample $s$ exceeds the one from the earlier sample $r$. The **Jonckheere–Terpstra test** of $H_0\colon F_1=\dots=F_k$ against the increasing alternative rejects for large values of

$$
J=\sum_{r<s}U_{rs}.
$$

Each $U_{rs}$ is the WMW statistic (Proposition 9.3.1) for the pair $(r,s)$, counted in the direction predicted by $H_1$. $J$ counts, over all pairs of observations from different samples, how many are in the predicted order: it is a generalization of **Kendall's tau** ([3.6.8](/3.6.8)) between the response and the group index, counting only pairs in different groups. For $k=2$ it reduces to the WMW test.

**Theorem 11.2.1** Under $H_0$ without ties,

$$
\mathbb{E}J=\frac{N^2-\sum_in_i^2}4,\qquad
\operatorname{Var}(J)=\frac{N^2(2N+3)-\sum_in_i^2(2n_i+3)}{72},
$$
and $Z=(J-\mathbb{E}J)/\sqrt{\operatorname{Var}(J)}$ is asymptotically $\mathcal{N}(0,1)$.

**Proof** By Theorem 9.3.1, $\mathbb{E}U_{rs}=n_rn_s/2$, so $\mathbb{E}J=\frac12\sum_{r<s}n_rn_s$. Since $N^2=\bigl(\sum_in_i\bigr)^2=\sum_in_i^2+2\sum_{r<s}n_rn_s$, $\sum_{r<s}n_rn_s=(N^2-\sum_in_i^2)/2$, which gives the mean. For the variance, $\operatorname{Var}(J)=\sum_{r<s}\operatorname{Var}(U_{rs})+\sum\operatorname{Cov}(U_{rs},U_{gh})$ over distinct pairs of pairs, with $\operatorname{Var}(U_{rs})=n_rn_s(n_r+n_s+1)/12$; the covariances vanish unless the two pairs share a sample and are computed from the joint distribution of three samples. Collecting the terms gives the stated formula; we omit the algebra. The asymptotic normality follows from the theory of U-statistics. $\square$

**Example 11.2.1 (Braking Distances)** Hinkley (1989) gives braking distances (feet) taken by motorists to stop when travelling at various speeds. A subset of his data is:

| Speed (mph) | Braking distances | | | |
|---|---|---|---|---|
| 20 | 48 | | | |
| 25 | 33 | 59 | 48 | 56 |
| 30 | 60 | 101 | 67 | |
| 35 | 85 | 107 | | |

We test $H_0$: braking distance does not depend on the initial speed, against $H_1$: braking distance increases with speed. The samples are already in the order predicted by $H_1$, with $k=4$ and $n=(1,4,3,2)$. The pairwise counts are $U_{12}=2.5$ (the speed-$20$ value $48$ is below $59$ and $56$, tied with $48$, above $33$), $U_{13}=3$, $U_{14}=2$, $U_{23}=12$, $U_{24}=8$ and $U_{34}=5$, so $J=32.5$. With $N=10$ and $\sum n_i^2=30$, $\mathbb{E}J=17.5$, $\operatorname{Var}(J)=\frac{100\cdot23-(1\cdot5+16\cdot11+9\cdot9+4\cdot7)}{72}=27.9$, $Z=(32.5-17.5)/5.28=2.84$, and the one-sided $p$-value is $0.0023$ (the small tie is ignored in the variance).

```r
distance <- c(48, 33, 59, 48, 56, 60, 101, 67, 85, 107)
speed <- ordered(rep(c(20, 25, 30, 35), times = c(1, 4, 3, 2)))
clinfun::jonckheere.test(distance, as.numeric(speed), alternative = "increasing")
kruskal.test(distance ~ speed)
```

```text
Jonckheere-Terpstra test
JT = 32.5, p-value = 0.002263
alternative hypothesis: increasing

Kruskal-Wallis rank sum test
Kruskal-Wallis chi-squared = 7.2599, df = 3, p-value = 0.06406
```

A Monte Carlo permutation $p$-value ($2\times10^5$ random allocations) is about $0.001$. There is clear evidence that braking distance increases with speed. The Kruskal–Wallis test, which ignores the order, gives only $p=0.064$.
:::

### 11.2.2. When to Use It

The Jonckheere–Terpstra test must be specified before the data are seen: choosing the direction after inspecting the means turns it into a test with inflated level. When the ordered alternative is correct it is generally more powerful than the Kruskal–Wallis test, as in Example 11.2.1; when the true pattern is not monotone (an increase followed by a decrease), it can miss differences that the Kruskal–Wallis test detects. Like the Kruskal–Wallis test, it is exact for $H_0\colon F_1=\dots=F_k$, and its interpretation as a test of ordered medians requires that the distributions differ at most by shifts. With ties, the $U_{rs}$ count tied pairs as one half and the variance is reduced; software applies a correction or computes the exact permutation distribution.

## 11.3. Several Related Samples

### 11.3.1. Randomized Complete Blocks

**Example 11.3.1 (Pulse Rates)** For seven students the pulse rate (per minute) was measured before exercise (I), immediately after exercise (II) and five minutes after exercise (III):

| Student | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| I | 72 | 96 | 88 | 92 | 74 | 76 | 82 |
| II | 120 | 120 | 132 | 120 | 101 | 96 | 112 |
| III | 76 | 95 | 104 | 96 | 84 | 72 | 76 |

We want to test for differences between the pulse rates on the three occasions.
:::

Here the three samples are not independent: the same seven students are measured three times. The occasions are the treatments, the students are **blocks**, and the design is a **randomized complete block design** ([3.8.6](/3.8.6)): the experimental units are grouped into blocks that are roughly homogeneous, every treatment occurs once in every block, and (in an experiment) treatments are assigned at random within blocks. It extends the paired design ([3.6.8](/3.6.8)) from two to $t\ge2$ treatments. The students may differ greatly in their resting pulse, and these differences between blocks would mask the treatment effect if the samples were treated as independent.

The remedy is to compare the treatments within each block. For two treatments the sign test does this: within each pair it records which treatment gives the larger value, that is, it ranks the two observations $1$ and $2$. For three treatments we rank the three observations within each block $1$, $2$ and $3$.

### 11.3.2. The Friedman Test

Let there be $b$ blocks and $t$ treatments, let $R_{ij}$ be the rank of the observation on treatment $i$ within block $j$, and let $s_i=\sum_{j=1}^bR_{ij}$ be the rank sum of treatment $i$.

**Definition 11.3.1 (Friedman Test)** The **Friedman test** of $H_0$: within each block the $t$ observations are exchangeable (no treatment differences), against $H_1$: the treatment distributions differ (for example the medians $\theta_i$ are not all equal), rejects for large values of

$$
T=\frac{12}{bt(t+1)}\sum_{i=1}^t\Bigl(s_i-\frac{b(t+1)}2\Bigr)^2=\frac{12}{bt(t+1)}\sum_{i=1}^ts_i^2-3b(t+1),
$$
whose exact null distribution is obtained from the $(t!)^b$ equally likely within-block permutations, and which is approximately $\chi^2_{t-1}$ when $b$ is not too small.

Under $H_0$ each $s_i$ has mean $b(t+1)/2$. The ANOVA view clarifies the statistic: within each block the ranks have mean $(t+1)/2$ and variance $(t^2-1)/12$, the treatment sum of squares of the ranks is $\mathrm{SS}_{\mathrm{Tr}}=\sum_ib\,(s_i/b-(t+1)/2)^2$, and

$$
T=\frac{\mathrm{SS}_{\mathrm{Tr}}}{\sum_{i,j}\bigl(R_{ij}-\frac{t+1}2\bigr)^2/\bigl(b(t-1)\bigr)} ,
$$
where without ties the denominator equals $t(t+1)/12$. With ties within blocks (midranks), using this form with the actual denominator gives the tie-corrected statistic, which is $T$ divided by $1-\sum(d^3-d)/\bigl(b(t^3-t)\bigr)$, the sum being over the tied groups in all blocks.

**Example 11.3.2 (Pulse Rates, Continued)** The within-student ranks are $(1,3,2)$ for students A, C, D, E and $(2,3,1)$ for B, F, G: occasion II is always the highest. The rank sums are $s=(10,21,11)$, $\sum s_i^2=662$, and

$$
T=\frac{12\times662}{7\times3\times4}-3\times7\times4=10.57 .
$$

```r
pr <- matrix(c(72, 120, 76, 96, 120, 95, 88, 132, 104, 92, 120, 96,
               74, 101, 84, 76, 96, 72, 82, 112, 76), ncol = 3, byrow = TRUE)
friedman.test(pr)
```

```text
Friedman rank sum test
Friedman chi-squared = 10.571, df = 2, p-value = 0.005063
```

The exact permutation $p$-value over the $6^7$ within-block arrangements is $0.0027$. There is strong evidence of a difference between the three occasions. For pairwise follow-up, the rank sums can be compared directly: under $H_0$, $\operatorname{Var}(s_i-s_{i'})=bt(t+1)/6=14$, so $(s_{\mathrm{II}}-s_{\mathrm I})/\sqrt{14}=2.94$ and $(s_{\mathrm{II}}-s_{\mathrm{III}})/\sqrt{14}=2.67$ both exceed the Bonferroni critical value $z_{0.05/6}=2.39$ for the three two-sided comparisons, while $\lvert s_{\mathrm I}-s_{\mathrm{III}}\rvert/\sqrt{14}=0.27$ does not: the pulse rate immediately after exercise differs from both the others, which do not differ from each other.
:::

![Pulse rates of seven students on three occasions. Left: raw profiles, with large differences between students. Right: ranks within students, which remove those differences; occasion II has rank $3$ for every student.](./plots/friedman-pulse.py)

### 11.3.3. Comparison with Repeated-Measures ANOVA

The parametric analysis of the same data is the **repeated measures** ANOVA, equivalent here to the two-way ANOVA without replication with treatments and blocks as factors:

```r
student <- factor(rep(1:7, each = 3)); time <- factor(rep(1:3, 7))
y <- as.vector(t(pr))
summary(aov(y ~ time + Error(student)))
```

```text
Error: student
          Df Sum Sq Mean Sq F value Pr(>F)
Residuals  6   1860     310

Error: Within
          Df Sum Sq Mean Sq F value   Pr(>F)
time       2   4218  2108.9   50.66 1.41e-06 ***
Residuals 12    500    41.6
```

The sums of squares split as $\mathrm{SS}_{\mathrm{time}}=b\sum_i(\bar x_{i\cdot}-\bar x)^2=4217.8$, $\mathrm{SS}_{\mathrm{student}}=t\sum_j(\bar x_{\cdot j}-\bar x)^2=1859.9$ and the error $\sum_{i,j}(x_{ij}-\bar x_{i\cdot}-\bar x_{\cdot j}+\bar x)^2=499.5$ on $(t-1)(b-1)=12$ degrees of freedom; $F=2108.9/41.6=50.66$. The model `y ~ time + student` without the error stratum gives the same $F$ for time.

The $F$-test's $p$-value $1.4\times10^{-6}$ is much smaller than Friedman's $0.005$, and this is typical: the ANOVA uses the sizes of the differences, which are large here (about $30$ beats per minute), while the Friedman test uses only the order within each block. With $t=3$ treatments and $b=7$ blocks, the smallest attainable exact $p$-value of the Friedman test is $6/6^7\approx2\times10^{-5}$ (all blocks ranked identically), and the observed pattern is not the most extreme. The repeated-measures ANOVA requires normal errors and, for more than two treatments, sphericity (equal variances of all pairwise differences); the Friedman test requires neither. Under normality its efficiency relative to the $F$-test is $\frac{3}{\pi}\cdot\frac{t}{t+1}$, which is $0.716$ for $t=3$ and tends to $0.955$ as $t$ grows.

Is the Friedman test simply the repeated-measures ANOVA applied to the within-block ranks? Almost. The $F$ statistic of the two-way ANOVA computed from the ranks $R_{ij}$ is a monotone function of $T$,

$$
F_R=\frac{(b-1)\,T}{b(t-1)-T},
$$
(because the block sum of squares of the ranks is zero and the total sum of squares is fixed), so the two give the same test if the same reference distribution is used; referring $F_R$ to $F_{t-1,(b-1)(t-1)}$ (the Iman–Davenport approximation) is often more accurate than referring $T$ to $\chi^2_{t-1}$. For the pulse data $F_R=18.5$.

When the number of treatments is small and the blocks differ in how variable they are, the Quade test is an alternative: it ranks the blocks by their ranges and weights each block's within-block ranks by the rank of its range, so that blocks with large differences between treatments count more. Like the Friedman test, it is exact under within-block exchangeability.

### 11.3.4. The Page Test for Ordered Alternatives

The Page test is to the Friedman test what the Jonckheere–Terpstra test is to the Kruskal–Wallis test: a test against the ordered alternative $H_1\colon\theta_1\le\theta_2\le\dots\le\theta_t$ (at least one strict) for blocked data.

**Definition 11.3.2 (Page's Test)** With the treatments numbered in the order predicted by $H_1$ and $s_i$ the within-block rank sums, **Page's test** of $H_0$ (exchangeability within blocks) against the increasing alternative rejects for large values of

$$
L=\sum_{i=1}^ti\,s_i .
$$
Under $H_0$ without ties,

$$
\mathbb{E}L=\frac{bt(t+1)^2}4,\qquad\operatorname{Var}(L)=\frac{b\,t^2(t+1)(t^2-1)}{144}=\frac{b(t^3-t)^2}{144(t-1)},
$$
and $(L-\mathbb{E}L)/\sqrt{\operatorname{Var}(L)}$ is approximately $\mathcal{N}(0,1)$; the test is one-sided.

$L$ weights the rank sums by the predicted order, so it is large when the ranks increase along the treatments. Equivalently, $L$ is a linear function of the average over blocks of Spearman's correlation between the within-block ranks and the treatment order. When the trend is real, Page's test is more powerful than the Friedman test.

For the pulse data an ordered alternative is not natural: the pulse rises after exercise and then falls. If the order I $<$ II $<$ III were tested anyway, $L=10+42+33=85$ against $\mathbb{E}L=84$ and $\operatorname{Var}(L)=14$ gives $z=0.27$: Page's test has no power against a rise-and-fall pattern, which the Friedman test detects. The direction must be chosen from the subject matter, not from the data.

### 11.3.5. Binary Responses: Cochran's Q Test

**Example 11.3.3 (Rock Climbs)** Five members $A,\dots,E$ of a mountaineering club each attempt three rock climbs, succeeding ($1$) or failing ($0$):

| Climb | A | B | C | D | E | Successes $T_i$ |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 0 | 0 | 1 | 3 |
| 2 | 1 | 0 | 0 | 1 | 0 | 2 |
| 3 | 0 | 1 | 1 | 1 | 1 | 4 |
| Block total $B_j$ | 2 | 2 | 1 | 2 | 2 | $N=9$ |

Are the climbs equally difficult?
:::

The data form an RCBD with $t=3$ treatments (climbs) and $b=5$ blocks (members), and a binary response. Let $x_{ij}\in\{0,1\}$, $T_i=\sum_jx_{ij}$ the number of successes for treatment $i$, $B_j=\sum_ix_{ij}$ the number for block $j$, and $N=\sum_iT_i=\sum_jB_j$.

**Definition 11.3.3 (Cochran's Q Test)** **Cochran's Q test** of $H_0$: within each block the $t$ binary responses are exchangeable (the success probabilities of the treatments are equal), rejects for large values of

$$
Q=\frac{(t-1)\Bigl(t\sum_{i=1}^tT_i^2-N^2\Bigr)}{tN-\sum_{j=1}^bB_j^2},
$$
which is approximately $\chi^2_{t-1}$ under $H_0$.

For the climbs, $Q=\frac{2\,(3\times29-81)}{27-17}=1.2$ and $p=\mathbb{P}(\chi^2_2>1.2)=0.55$: there is no evidence that the climbs differ in difficulty.

**Proposition 11.3.1** (a) Cochran's $Q$ equals the tie-corrected Friedman statistic computed from the binary data. (b) For $t=2$, $Q$ equals the uncorrected chi-squared statistic $(b_{10}-b_{01})^2/(b_{10}+b_{01})$ of **McNemar's test** (Definition 8.3.1), where $b_{10}$ and $b_{01}$ are the numbers of blocks with responses $(1,0)$ and $(0,1)$. (c) Blocks in which all responses are $0$ or all are $1$ do not change $Q$.

**Proof** (a) In a block with $B_j$ ones and $t-B_j$ zeros, the zeros receive the midrank $(t-B_j+1)/2$ and the ones the midrank $t-B_j+(B_j+1)/2$, larger by exactly $t/2$, whatever $B_j$. Hence $R_{ij}=a_j+\frac t2x_{ij}$ for constants $a_j$. In the ANOVA form of the tie-corrected Friedman statistic, a constant per block cancels in both the treatment sum of squares and the within-block total, and the common factor $(t/2)^2$ cancels in the ratio, so the statistic equals

$$
\frac{\sum_ib\,(T_i/b-N/(bt))^2}{\sum_{i,j}(x_{ij}-B_j/t)^2/(b(t-1))}
=\frac{(\sum_iT_i^2-N^2/t)/b\cdot b(t-1)}{N-\sum_jB_j^2/t}=Q,
$$
using $\sum_ix_{ij}^2=B_j$. (b) For $t=2$, $T_1+T_2=N$, and the blocks with $B_j=1$ are the discordant ones, $b_{10}+b_{01}$ in number; the blocks with $B_j=2$ contribute $4$ each to $\sum B_j^2$ and $2$ each to $N$, those with $B_j=0$ nothing. Then $2(T_1^2+T_2^2)-N^2=(T_1-T_2)^2=(b_{10}-b_{01})^2$ and $2N-\sum B_j^2=(b_{10}+b_{01})$, which gives the McNemar statistic. (c) A block with $B_j=0$ adds nothing to $T_i$, $N$ or $\sum B_j^2$. A block with $B_j=t$ adds $1$ to every $T_i$ and $t$ to $N$; then $t\sum T_i^2-N^2=t\sum(T_i-\bar T)^2$ is unchanged, and $tN-\sum B_j^2$ changes by $t\cdot t-t^2=0$. $\square$

For the climbs, the within-member ranks give rank sums $10$, $8.5$ and $11.5$, and the tie-corrected Friedman statistic is indeed $1.2$. Property (c) is the same as in McNemar's test: members who succeed (or fail) on every climb tell us nothing about which climbs are harder. Cochran's $Q$ is thus the McNemar test generalized to more than two related samples.

If the binary responses come from independent samples (for example, preferences in random samples from three regions), the design is a CRD, and the appropriate test is the chi-squared **test of homogeneity** for the $k\times2$ **contingency table** ([3.6.12](/3.6.12)), not Cochran's test.

## 11.4. Equality of Variances: The Squared Ranks Test

Location tests are insensitive to differences in spread, and the Kruskal–Wallis test is interpretable as a comparison of locations only when spreads are equal. **Levene's test** ([3.3.5](/3.3.5)) checks equality of variances by an ANOVA on the absolute deviations $\lvert x_{ij}-\bar x_i\rvert$. The squared ranks test does the same with ranks, by analogy with the Kruskal–Wallis test.

**Definition 11.4.1 (Squared Ranks Test)** Compute the absolute deviations $\lvert x_{ij}-m_i\rvert$ of the observations from their sample means $m_i$, rank them in the combined sample, and let $R_{ij}$ be these ranks. With $s_i=\sum_jR_{ij}^2$, $S_k=\sum_is_i^2/n_i$, $S_r=\sum_{i,j}R_{ij}^4$ and $C=\bigl(\sum_{i,j}R_{ij}^2\bigr)^2/N$, the **squared ranks test** of $H_0\colon\sigma_1^2=\dots=\sigma_k^2$ rejects for large values of

$$
T=\frac{(N-1)(S_k-C)}{S_r-C},
$$
which is approximately $\chi^2_{k-1}$ under $H_0$.

The test is the Kruskal–Wallis test with the squared ranks $R_{ij}^2$ as scores: $T$ is $(N-1)$ times the ratio of the between-sample sum of squares of the scores to their total sum of squares, exactly as $H$ in Proposition 11.1.1. Squaring the ranks emphasizes the largest deviations, which carry most of the information about spread. For $k=2$ it reduces to a two-sample test equivalent to a normal approximation of the linear rank statistic $\sum_jR_{1j}^2$.

**Example 11.4.1 (Braking Distances, Revisited)** Another subset of Hinkley's data is:

| Speed (mph) | Braking distances | | | |
|---|---|---|---|---|
| 5 | 2 | 8 | 8 | 4 |
| 10 | 8 | 7 | 14 | |
| 25 | 33 | 59 | 48 | 56 |
| 30 | 60 | 101 | 67 | |

Is the variability of the braking distance the same at all speeds? The sample means are $5.5$, $9.67$, $49$ and $76$, and the absolute deviations and their ranks in the combined sample are:

| Speed | Absolute deviations (ranks) |
|---|---|
| 5 | 3.5 (7), 2.5 (4.5), 2.5 (4.5), 1.5 (2) |
| 10 | 1.67 (3), 2.67 (6), 4.33 (8) |
| 25 | 16 (12.5), 10 (11), 1 (1), 7 (9) |
| 30 | 16 (12.5), 25 (14), 9 (10) |

Then $s_1=7^2+4.5^2+4.5^2+2^2=93.5$, $s_2=109$, $s_3=359.25$, $s_4=452.25$, and the formula gives $T=8.02$, larger than the $5\%$ critical value $\chi^2_{3,0.05}=7.815$ ($p=0.046$). There is some evidence that the variability differs between speeds; as one might expect, it is larger at higher speeds. For comparison, Levene's test (deviations from the means) gives $p=0.017$ and the Brown–Forsythe version (deviations from the medians) $p=0.37$: with such small samples the conclusion depends on the method, and the evidence should be regarded as weak.
:::

The squared ranks test inherits a limitation of all such tests: the absolute deviations are computed from estimated centers, so the deviations within a sample are not independent, and the test is only approximately distribution-free; deviations from the median are more robust for skewed data. For two samples, the Siegel–Tukey test of [3.6.10](/3.6.10) is the alternative.

## 11.5. Choosing a Test

The tests of this chapter, and their parametric counterparts, are organized by the design and by the alternative:

| | Completely randomized design (independent samples) | Randomized complete block design (related samples) |
|---|---|---|
| Ranking | all $N$ observations together | within each block |
| General alternative | Kruskal–Wallis $H$ (Definition 11.1.1) | Friedman $T$ (Definition 11.3.1); Quade |
| Ordered alternative | Jonckheere–Terpstra $J$ (Definition 11.2.1) | Page $L$ (Definition 11.3.2) |
| Binary response | chi-squared test of homogeneity for a $k\times2$ table | Cochran's $Q$ (Definition 11.3.3) |
| Two samples | WMW (Definition 9.3.1) | sign test, Wilcoxon signed-rank, McNemar |
| Pairwise follow-up | Dunn's test (Definition 11.1.2) with Holm or BH | rank-sum differences, $\operatorname{Var}(s_i-s_{i'})=bt(t+1)/6$ |
| Spread | squared ranks test (Definition 11.4.1) | — |
| Parametric counterpart | one-way ANOVA | two-way ANOVA without replication, repeated-measures ANOVA |

The procedure is the same in all cases: rank (in the whole sample or within blocks), sum the ranks per treatment, and choose the statistic according to the alternative. Using the independent-samples tests for related samples ignores the blocks and loses power to the between-block variation; using the block tests for independent samples is not possible, since there are no blocks.

## Summary

- Kruskal–Wallis (Definition 11.1.1): pooled ranks, $H=\frac{12}{N(N+1)}\sum R_{i\cdot}^2/n_i-3(N+1)$, the ANOVA treatment sum of squares of the ranks over their total variance (Proposition 11.1.1); $\chi^2_{k-1}$ for $n_i\ge5$, exact otherwise (home prices: $H=6.745$, $\chi^2$ $p=0.034$, exact $0.010$); ties: divide by $1-\sum(d^3-d)/(N^3-N)$. Exact for identical distributions; a test of medians only under shifts.
- Follow-up: Dunn's test (Definition 11.1.2) uses pooled ranks; pairwise re-ranked WMW tests with tiny groups cannot reach significance (minimum $p=0.10$ for $3$ vs $3$). Report effect sizes, reduce the number of comparisons (many-to-one), distinguish exploratory from confirmatory analysis.
- Jonckheere–Terpstra (Definition 11.2.1): $J=\sum_{r<s}U_{rs}$, mean $(N^2-\sum n_i^2)/4$ (Theorem 11.2.1); more powerful than KW against a prespecified monotone trend (braking: $p=0.002$ vs $0.064$).
- RCBD: rank within blocks. Friedman (Definition 11.3.1): $T=\frac{12}{bt(t+1)}\sum s_i^2-3b(t+1)\approx\chi^2_{t-1}$ (pulse: $T=10.57$, $p=0.005$); a monotone function of the rank-based two-way ANOVA $F$; less powerful than repeated-measures ANOVA under normality (efficiency $\frac3\pi\frac t{t+1}$) but needs neither normality nor sphericity.
- Page (Definition 11.3.2): $L=\sum is_i$, one-sided, for ordered alternatives in blocks.
- Cochran's $Q$ (Definition 11.3.3): binary responses in blocks; equals the tie-corrected Friedman statistic, reduces to McNemar for $t=2$, ignores all-$0$ and all-$1$ blocks (Proposition 11.3.1).
- Squared ranks test (Definition 11.4.1): Kruskal–Wallis on squared ranks of absolute deviations; rank analogue of Levene's test (braking: $T=8.02$, $p=0.046$).

## Questions

1. Show that for $k=2$ the Kruskal–Wallis statistic is the square of the standardized Wilcoxon rank-sum statistic, so that the Kruskal–Wallis test with two samples is the two-sided WMW test with the normal approximation.

   **Answer** With two samples, $n_1(\bar R_1-\bar R)+n_2(\bar R_2-\bar R)=0$, so $\bar R_2-\bar R=-\frac{n_1}{n_2}(\bar R_1-\bar R)$ and $\sum_in_i(\bar R_i-\bar R)^2=n_1(\bar R_1-\bar R)^2\bigl(1+\frac{n_1}{n_2}\bigr)=\frac{n_1N}{n_2}(\bar R_1-\bar R)^2$. With $W_x=n_1\bar R_1$ and $\mathbb{E}W_x=n_1(N+1)/2$, $(\bar R_1-\bar R)^2=(W_x-\mathbb{E}W_x)^2/n_1^2$. Hence $H=\frac{12}{N(N+1)}\cdot\frac{N}{n_1n_2}(W_x-\mathbb{E}W_x)^2=\frac{(W_x-\mathbb{E}W_x)^2}{n_1n_2(N+1)/12}$, the square of the standardized $W_x$ (Theorem 9.3.1), and $\chi^2_1$ is the distribution of the square of a standard normal variable.
2. In Example 11.1.4 the global Kruskal–Wallis test is significant while no BH-adjusted pairwise WMW test is. A colleague concludes that "the Kruskal–Wallis result must be a false positive". Do you agree?

   **Answer** No. The two analyses answer different questions with different amounts of information. The global test uses all ten observations jointly; the pairwise tests use only two groups at a time and re-rank them, and with groups of three or four the exact WMW test cannot produce a $p$-value below $0.057$ or $0.10$, so they had essentially no chance of significance. The global significance means that at least one difference exists; Dunn's test on the pooled ranks locates it between $A$ and $C$ (Holm-adjusted $p=0.031$). The appropriate report gives the global test, the Dunn comparisons and estimates of the differences with intervals, and acknowledges that the samples are too small for precise pairwise conclusions.
3. Five employees are ranked from $1$ (best) to $5$ in leadership ability by each of three supervisors. Why is this an RCBD, and how is the Friedman statistic related to Kendall's coefficient of concordance $W=T/\bigl(b(t-1)\bigr)$?

   **Answer** Each supervisor ranks all employees, so the supervisors are blocks and the employees are treatments; the observations are already within-block ranks. Under $H_0$ (the supervisors do not agree; each ranking is a random permutation) the Friedman statistic $T$ is approximately $\chi^2_4$ with $t=5$, $b=3$, and a large $T$ means that some employees receive consistently high or low ranks, that is, that the supervisors agree. Kendall's $W=T/(b(t-1))$ rescales $T$ to $[0,1]$: $W=1$ when all supervisors give identical rankings (then $T=b(t-1)$), and $W=0$ when all rank sums are equal. The test of no agreement based on $W$ is the Friedman test.
4. Use the result of Proposition 11.3.1(c): what happens to Cochran's $Q$ in Example 11.3.3 if three more members join who fail all three climbs, and what if they succeed in all of them?

   **Answer** In both cases $Q$ is unchanged ($1.2$), by Proposition 11.3.1(c). Members who fail everywhere add zero to every $T_i$, to $N$ and to $\sum B_j^2$. Members who succeed everywhere add $1$ to every $T_i$ (which does not change the spread of the $T_i$) and $3$ to $N$ and $9$ to $\sum B_j^2$ each, which leaves $tN-\sum B_j^2$ unchanged. They carry no information about which climb is harder, and the number of informative blocks does not grow, so the chi-squared approximation, which is justified by the number of informative blocks, may be unreliable when most blocks are uninformative.
5. Why would it be wrong to analyze the pulse data of Example 11.3.1 with the Kruskal–Wallis test, and in which direction would the result typically be wrong?

   **Answer** The three samples consist of the same seven students, so they are not independent, and the null distribution of $H$, which assumes that all $21$ observations are exchangeable, is invalid. The differences between students (resting pulses from $72$ to $96$) inflate the variation within each occasion and mask the treatment effect, so the Kruskal–Wallis test typically loses power: with positively correlated measurements within a block, it is conservative. Ranking within blocks removes the block effects and leaves the treatment comparison.
6. A test of $H_0\colon\theta_1=\theta_2=\theta_3$ is to be made for three increasing doses of a drug, and the investigator expects the response to increase with dose. Which test would you use for independent groups of patients, and which if each patient receives all three doses in random order with washout periods? What is the danger of choosing the test after looking at the data?

   **Answer** For independent groups, the Jonckheere–Terpstra test with the doses in increasing order; for the crossover-type design, in which each patient is a block, Page's test. Both are one-sided tests whose direction must be fixed in advance. If the direction or the ordered test is chosen after seeing that the means increase, the type I error rate is inflated, since one would in effect be applying the most favourable of several tests; with no prior expectation of monotonicity, the Kruskal–Wallis or Friedman test should be used.
