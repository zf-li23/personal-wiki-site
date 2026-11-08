---
title: Nonparametric Methods
description: When nonparametric methods are needed (ordinal data, skewness, small samples, outliers); the idea of ranks and asymptotic relative efficiency; the sign test, Wilcoxon signed-rank test, Wilcoxon rank-sum test and Mann–Whitney U (equivalence with the AUC, ties and exact p-values), the Hodges–Lehmann estimator; the Kruskal–Wallis test and Dunn's test; permutation tests; the Kolmogorov–Smirnov test; Spearman and Kendall rank correlation; choosing between parametric and nonparametric methods. Examples are captopril blood-pressure reduction, Student's sleep data, children's FEV, CT rating scores and the guinea-pig vitamin C experiment.
source_hash: 6d894b166901
---

The t methods of [7.7.6](/7.7.6) and [7.7.7](/7.7.7) assume that the data (or the differences) are approximately normal. When the sample is large, the **central limit theorem** makes them quite robust. Three kinds of data, however, give cause for concern: ordinal outcomes (pain scores, five-point imaging ratings, "improved / unchanged / worse"), for which arithmetic has no meaning in itself; small samples with clearly skewed distributions (length of hospital stay, cytokine concentrations); and small samples containing a few outliers. **Nonparametric tests** do not assume that the population belongs to a parametric family. Most of them use only the order of the observations (their ranks), and so are insensitive to the shape of the distribution and to outliers. This chapter treats, in turn, the sign test and Wilcoxon signed-rank test for paired data, the Wilcoxon rank-sum test for two independent samples, the Kruskal–Wallis test for several groups, the permutation test that needs no distribution table, the Kolmogorov–Smirnov test that compares whole distributions, and rank correlation. The examples continue those of the previous two chapters: the paired data on captopril and on sleeping pills; FEV in smokers and nonsmokers (rank methods reach the same conclusion as the t test, which again shows that the FEV paradox lies in the design, not in the test); the CT rating scores of [7.7.3](/7.7.3) (the Mann–Whitney statistic is the area under the ROC curve); and the guinea-pig vitamin C dose experiment. The null distributions and proofs for these tests are in [3.2.6](/3.2.6); here we cover their use, conditions and interpretation.

## 8.1. When Nonparametric Methods Are Needed

### 8.1.1. Ranks

Arrange $N$ observations from smallest to largest; the position of each observation is its rank. Equal observations (ties) receive the average of the positions they occupy. Ranks retain only the order: whether the largest observation is 4.6 or 46, its rank is the same. Rank-based tests are therefore not dragged around by outliers and are unchanged by any monotone transformation (logarithm, square root). Moreover, under $H_0$ the distribution of the ranks depends only on the sample sizes and not on the population distribution; this is why these tests are called "distribution-free".

![Ranks discard the scale and keep the order. Difference in extra hours of sleep between two hypnotics in 10 patients (data of Cushny and Peebles 1905, used by Student 1908). A: the differences on the original scale; 4.6 lies far from the rest. B: the ranks of the absolute differences used by the Wilcoxon signed-rank test (ties receive average ranks and the zero difference is dropped), with the original values in small type below; if 4.6 is changed to 46, no rank changes](./plots/ranks.py)

### 8.1.2. Efficiency

The price of nonparametric methods is that, when the data really are normal, they are slightly weaker than the t test. The quantity that measures this price is efficiency.

**Definition 8.1.1 (Asymptotic Relative Efficiency)** Consider two tests at the same level that attain the same power against the same alternative. The limit of the ratio $n_B/n_A$ of the sample sizes they require, as the sample size tends to infinity and the alternative tends to the null hypothesis, is called the **asymptotic relative efficiency** (ARE) of test $A$ relative to test $B$.

Some classical results (Pitman efficiency; proofs omitted):

| Comparison | Normal population | General result |
|---|---|---|
| Wilcoxon test relative to the t test | $3/\pi = 0.955$ | Never below 0.864 for any continuous symmetric distribution; can be much greater than 1 for heavy tails (infinite for the Cauchy distribution) |
| Sign test relative to the t test | $2/\pi = 0.637$ | 2 for the double-exponential distribution |
| Sample median relative to sample mean (efficiency of estimation) | $2/\pi = 0.637$ | Same as above |

That is, for normal data the power that the Wilcoxon test reaches with 100 observations is reached by the t test with about 96, so the loss is small; but once the distribution is heavy-tailed or skewed, the rank test can be far better (the simulation of Section 8.9). The sign test uses only the signs of the differences and loses more. The remark in [7.7.2](/7.7.2) that for normal data the median "fluctuates more than the mean" is exactly this $2/\pi$: the variance of the sample median is about $\pi/2 = 1.57$ times that of the sample mean.

## 8.2. The Sign Test

The simplest test for paired data (or for a single sample against a given value) looks only at the signs of the differences.

**Formula 8.2.1 (Sign Test)** Suppose that $n$ of the differences among the pairs are nonzero (zero differences are dropped) and that $n_+$ of them are positive. Under $H_0$ (the median difference is 0, that is, positive and negative differences are equally likely), $n_+ \sim \mathrm{Bin}(n, 1/2)$, and the p-value is computed from the exact binomial distribution. For $n \ge 20$ the normal approximation can be used:

$$
z = \frac{\lvert n_+ - n/2\rvert - 1/2}{\sqrt{n/4}}.
$$

The **sign test** has only one prerequisite: the pairs are mutually independent. It applies to data in which only the direction can be judged, for example two sunscreens applied to the left and right arms when we can only say which side is less red ([3.2.6](/3.2.6#sec-6.2.2)).

**Example 8.2.1** In the 15 captopril patients ([7.7.7](/7.7.7) Example 7.2.1) blood pressure fell in every one after treatment: $n_+ = 15$ and the two-sided $p = 2 \times 0.5^{15} = 6.1 \times 10^{-5}$. A more meaningful question is whether the mean reduction exceeds 10 mmHg: among the $d_i - 10$, 11 are positive, 3 negative and 1 zero, so the one-sided $p = \mathbb{P}(X \ge 11 \mid n = 14, p = 1/2) = 0.029$. The paired t test gives $p = 0.0009$ for the same question: the sign test discards the sizes of the differences, and the evidence is much weaker. In Student's sleep data all 9 nonzero differences are positive, and the two-sided $p = 2 \times 0.5^9 = 0.0039$.

## 8.3. The Wilcoxon Signed-Rank Test

The signed-rank test uses both the signs of the differences and the order of their sizes.

**Formula 8.3.1 (Wilcoxon Signed-Rank Test)** After dropping zero differences, rank the absolute values of the $n$ differences (ties receive average ranks) and let $T_+$ be the sum of the ranks of the positive differences. Under $H_0$ (the distribution of the differences is symmetric about 0),

$$
\mathbb{E}T_+ = \frac{n(n+1)}{4}, \qquad \operatorname{Var}(T_+) = \frac{n(n+1)(2n+1)}{24} - \sum_j \frac{t_j^3 - t_j}{48},
$$
where $t_j$ is the size of the $j$-th group of ties. For small $n$ the exact null distribution is used ([3.2.6 Theorem 6.2.1](/3.2.6#thm-6.2.1)); for $n \ge 16$ or so the normal approximation $z = (T_+ - \mathbb{E}T_+)/\sqrt{\operatorname{Var}(T_+)}$ can be used (often with a continuity correction of 1/2).

This is the **Wilcoxon signed-rank test**. Unlike the sign test, it requires the distribution of the differences to be symmetric, so what it tests is the center of the distribution of the differences (where the median equals the mean).

**Example 8.3.1** For the captopril data, testing whether the mean reduction exceeds 10 mmHg by a signed-rank test on $d_i - 10$ gives a one-sided $p = 0.0019$, between the sign test (0.029) and the t test (0.0009), in agreement with the ordering of the efficiencies. The *Hodges–Lehmann estimator* of the center of the differences is the median of all $(d_i + d_j)/2$ ($i \le j$; 120 Walsh averages), which is 19.75 mmHg, close to the mean 18.93.

**Example 8.3.2 (Sleeping Pills)** In Student's data all 9 nonzero differences are positive, $T_+ = 45$ attains its maximum possible value, and the exact two-sided $p = 2/2^9 = 0.0039$. The paired t test gives $p = 0.0028$ ([7.7.7](/7.7.7) Example 7.2.2). The two agree: the 4.6 h that lies far from the other data does not drive the conclusion; in the ranks it is merely "the largest".

## 8.4. The Wilcoxon Rank-Sum Test and the Mann–Whitney U

### 8.4.1. The Test

**Formula 8.4.1 (Wilcoxon Rank-Sum Test)** Pool the two independent samples (sizes $n_1, n_2$, $N = n_1 + n_2$), rank the pooled observations, and let $W$ be the sum of the ranks of the first sample. Under $H_0$ (the two populations have the same distribution),

$$
\mathbb{E}W = \frac{n_1(N+1)}{2}, \qquad \operatorname{Var}(W) = \frac{n_1 n_2 (N+1)}{12} - \frac{n_1 n_2 \sum_j (t_j^3 - t_j)}{12N(N-1)}.
$$
For small samples the exact distribution is used; the normal approximation is used when both $n_1$ and $n_2$ are at least about 10. Equivalently, the Mann–Whitney statistic $U = W - n_1(n_1+1)/2$ is the number of pairs in which the observation from the first sample exceeds that from the second (ties count 1/2).

This is the **Wilcoxon rank-sum test**, also called the Mann–Whitney U test ([3.2.6](/3.2.6#sec-6.2.4)). It requires the two samples to be independent and each to consist of independent, identically distributed observations; it is most sensitive to a location shift (one distribution lying wholly above the other).

### 8.4.2. The Meaning of U: The AUC

$U/(n_1 n_2)$ estimates

$$
\theta = \mathbb{P}(X_1 > X_2) + \tfrac12\,\mathbb{P}(X_1 = X_2),
$$
the probability that, when one individual is drawn at random from each group, the one from the first group is larger. Under $H_0$, $\theta = 1/2$. In diagnosis this quantity has a familiar name: if the first group is regarded as patients, the second as non-patients and the observations as test readings, $\theta$ is the **area under the curve** of the ROC curve ([7.7.3](/7.7.3), Section 3.4.2). So "comparing the readings of two groups by the Mann–Whitney test" and "testing whether the AUC equals 0.5" are the same thing.

**Example 8.4.1 (CT Rating Scores)** Among the 109 patients of Hanley and McNeil (1982), radiologists rated the CT images of 58 normal and 51 abnormal subjects on a five-point scale (1 = definitely normal, ..., 5 = definitely abnormal). The frequencies were 33, 6, 6, 11, 2 for the normal subjects and 3, 2, 2, 11, 33 for the abnormal ones. These are ordinal data with many ties: the 109 observations take only 5 distinct values. The number of pairs in which the abnormal subject is rated higher than the normal one, plus half the number of tied pairs, is $U = 2642$, and $U/(58 \times 51) = 0.893$, which is exactly the AUC of [7.7.3](/7.7.3) Example 3.4.1. The normal approximation with a correction for ties gives $p = 2 \times 10^{-13}$. A t test on such five-point ratings (treating 1–5 as equally spaced numbers) can also be computed, but nothing justifies the assumption that the difference between "definitely normal" and "probably normal" equals that between "probably abnormal" and "definitely abnormal"; rank methods use only the order and avoid the problem.

**Example 8.4.2 (FEV)** For the FEV of 65 smoking and 589 nonsmoking children, the rank sum of the smokers is $W = 30\,831$; its expectation under $H_0$ is $65 \times 655/2 = 21\,287.5$, so $z = 6.60$ and $p = 4 \times 10^{-11}$. We have $U/(n_1 n_2) = 0.749$: if we pick a smoking and a nonsmoking child at random, the probability that the former has the higher FEV is about 75%. The Hodges–Lehmann estimate of the location difference between the two groups (the median of all $65 \times 589$ between-group differences) is 0.75 L, with an approximate 95% interval $(0.54, 0.95)$ L, almost identical to the 0.71 L (0.49–0.93) of the t method. Switching to rank methods does not dissolve the paradox: both tests correctly answer "is the FEV of smoking children higher?", and the error lies in treating this as an effect of smoking ([7.7.7](/7.7.7) Example 7.3.2).

**Example 8.4.3 (ToothGrowth)** For 10 guinea pigs given orange juice and 10 given ascorbic acid at a dose of 0.5 mg/d, $U = 80.5$ (there is one tied pair) and the exact two-sided $p = 0.023$; the Welch t test gives 0.0064 ([7.7.7](/7.7.7) Example 7.5.1). In small samples the p-value of a rank test can take only finitely many values, so its resolution is low; when the data show no marked skewness, the t test has somewhat higher power.

### 8.4.3. What the Rank-Sum Test Tests

It is often said that "the rank-sum test compares the medians of two groups", but this is correct only when the two distributions have the same shape and differ by a location shift alone. In general it tests $\theta = 1/2$. When two groups have the same median but different spread, the rank-sum test may also be "significant"; conversely, when the variances of the two groups differ greatly, its control of the type I error also deteriorates (as with the pooled-variance t test). A report should state that the comparison concerns "the location of the distribution" and give $\theta$ or the Hodges–Lehmann shift estimate with an interval, not the p-value alone.

## 8.5. The Kruskal–Wallis Test

For three or more independent samples, the rank version of one-way analysis of variance ([7.7.12](/7.7.12)) is the **Kruskal–Wallis test** ([3.3.14](/3.3.14)).

**Formula 8.5.1 (Kruskal–Wallis Test)** Pool the $N$ observations from the $k$ groups and rank them; let $\bar R_j$ be the mean rank of group $j$ (with $n_j$ observations). The statistic

$$
H = \frac{12}{N(N+1)} \sum_{j=1}^k n_j\left(\bar R_j - \frac{N+1}{2}\right)^2
$$
is approximately $\chi^2_{k-1}$ under $H_0$ (all groups have the same distribution), provided each group has at least 5 observations. With ties, $H$ is divided by $1 - \sum_j (t_j^3 - t_j)/(N^3 - N)$.

**Example 8.5.1 (Dose in ToothGrowth)** Pooling the two delivery methods, we compare tooth growth at the three doses 0.5, 1 and 2 mg/d (20 guinea pigs each). The group medians are 9.85, 19.25 and 25.95, and the mean ranks are 12.3, 31.9 and 47.4 (overall mean rank 30.5). After the correction for ties, $H = 40.67$ with 2 degrees of freedom and $p = 1.5 \times 10^{-9}$: the dose effect is overwhelmingly significant. The delivery methods are pooled here only for demonstration; a complete analysis would consider dose and delivery method together with their interaction (two-way analysis of variance, [7.7.12](/7.7.12)).

![The Kruskal–Wallis test for ToothGrowth (60 guinea pigs, Crampton 1947): grouping by daily vitamin C dose, with the two delivery methods pooled (20 animals per dose; circles are orange juice OJ, triangles ascorbic acid VC). A: the raw data and the group medians. B: the ranks of the same animals among all 60 and the group mean ranks (12.3, 31.9, 47.4); the dashed line is the overall mean rank 30.5. The Kruskal–Wallis statistic compares the deviations of the mean ranks from 30.5; H = 40.7 with 2 degrees of freedom](./plots/toothgrowth-dose.py)

### 8.5.1. Pairwise Comparisons: Dunn's Test

A significant $H$ says only that "the groups are not all the same". To find out which two groups differ, *Dunn's test* compares the mean ranks of two groups:

**Formula 8.5.2 (Dunn's Test)** The statistic comparing group $i$ with group $j$ is

$$
z_{ij} = \frac{\bar R_i - \bar R_j}{\sqrt{\left(\dfrac{N(N+1)}{12} - \dfrac{\sum_l (t_l^3 - t_l)}{12(N-1)}\right)\left(\dfrac{1}{n_i} + \dfrac{1}{n_j}\right)}},
$$
which is approximately $\mathcal{N}(0, 1)$; for $m$ comparisons the **Bonferroni correction** (multiply the p-values by $m$) or Holm's method ([7.7.12](/7.7.12)) is used.

In Example 8.5.1 the three comparisons give: 0.5 versus 1 mg/d, $z = 3.55$ and adjusted $p = 0.001$; 0.5 versus 2, $z = 6.36$ and $p < 10^{-9}$; 1 versus 2, $z = 2.81$ and $p = 0.015$. The three doses differ pairwise. Dunn's test uses the ranks of all the data pooled; do not re-rank the data for each pair of groups and run separate rank-sum tests, since the ranks used in the different comparisons would then be inconsistent and the results could contradict each other.

## 8.6. Permutation Tests

### 8.6.1. The Idea

**Definition 8.6.1 (Permutation Test)** Suppose that, under the null hypothesis, the group labels of the observations can be interchanged (exchangeability) without changing the joint distribution of the data. Compute the test statistic under every way of reassigning the labels among the observations; this gives its exact distribution under $H_0$, and the tail probability of the observed statistic in that distribution is the p-value. Such a test is called a **permutation test**.

The logic of the permutation test comes directly from randomization ([7.7.5](/7.7.5), Section 5.2). In an experiment with random assignment, if the treatment has no effect at all, each animal would have the same outcome whichever group it was assigned to, and the observed group difference depends only on the random event "who was assigned to which group". Listing all possible assignments gives the distribution of the group difference when "the treatment has no effect", with no need to assume normality or a large sample, and the statistic can be chosen freely (difference of means, difference of medians, t statistic). The rank-sum test is itself a permutation test with the rank sum as statistic, and its null distribution can be computed in advance and tabulated.

**Example 8.6.1** At 0.5 mg/d the difference between the mean of the orange-juice group and that of the ascorbic-acid group (10 animals each) is 5.25. There are $\binom{20}{10} = 184\,756$ ways to choose 10 of the 20 guinea pigs to label "orange juice". Computing the mean difference for every one of them, the proportion with absolute value at least 5.25 is 0.0052, and this is the exact two-sided p-value. It is almost identical to the pooled-variance t test ($p = 0.0053$): the p-value of the t test can be viewed as an approximation to the permutation distribution, which is another reason why the t test is robust to non-normality (Fisher's 1935 argument).

![An exact permutation test: the odontoblast length of 10 guinea pigs fed orange juice (OJ) and 10 fed ascorbic acid (VC) at vitamin C 0.5 mg/d (ToothGrowth, Crampton 1947). Under H0 the group labels are interchangeable: all 184 756 ways of choosing 10 of the 20 animals to label OJ give the null distribution of the mean difference (histogram); the observed difference 5.25 and its mirror image mark the two tails (shaded), and the two-sided permutation p-value is 0.0052](./plots/permutation.py)

### 8.6.2. Monte Carlo Permutation

With somewhat larger samples the number of possible assignments is too large to enumerate (about $10^{29}$ for two groups of 50 observations each). Then one draws $B$ random reassignments of the labels (say $10^4$) and uses $(1 + \#\{\lvert T^*\rvert \ge \lvert T_{\mathrm{obs}}\rvert\})/(B + 1)$ as the estimate of the p-value (adding 1 to numerator and denominator keeps the p-value from being 0 and ensures that the level of the test does not exceed its nominal value). With $B = 10^4$ the Monte Carlo error when the true $p = 0.05$ is about $\sqrt{0.05 \times 0.95/10^4} = 0.002$.

The prerequisite of a permutation test is exchangeability: under $H_0$ the two groups must have exactly the same distribution. When we test only "the means are equal" and allow unequal variances, simple label permutation is no longer exact. For paired data the permutation exchanges the two members of each pair at random (equivalent to randomly changing the signs of the differences) instead of shuffling across all observations. The determination of empirical significance thresholds in genome-wide association studies by permutation (shuffling the correspondence between phenotype and genotype while keeping the linkage structure within the genome) is the same idea ([7.4.25](/7.4.25)). Permutation tests and the **bootstrap** ([7.7.5](/7.7.5), Section 5.10) both rely on resampling but serve different purposes: permutation reassigns labels under $H_0$ to obtain a p-value, whereas the bootstrap resamples from the data themselves to estimate the sampling distribution and confidence intervals.

## 8.7. Comparing Distributions: The Kolmogorov–Smirnov Test

The rank-sum test is sensitive mainly to differences in location. To ask whether two distributions differ in any respect (location, spread, shape), we can compare the two **empirical distribution functions** directly.

**Formula 8.7.1 (Two-Sample Kolmogorov–Smirnov Test)** Let $\hat F_1$ and $\hat F_2$ be the empirical distribution functions of the two samples. The statistic

$$
D = \sup_x \lvert \hat F_1(x) - \hat F_2(x)\rvert
$$
has, under $H_0\colon F_1 = F_2$ (continuous distributions), a distribution that does not depend on $F$; the limiting distribution of $\sqrt{n_1 n_2/(n_1 + n_2)}\,D$ is the Kolmogorov distribution, and the critical value at $\alpha = 0.05$ is about $1.36\sqrt{(n_1 + n_2)/(n_1 n_2)}$.

The one-sample form of the **Kolmogorov–Smirnov test** ([3.2.6](/3.2.6#sec-6.5.1)) is used to test whether the data come from a completely specified distribution.

**Example 8.7.1** For FEV in smokers and nonsmokers, $D = 0.435$, attained at FEV $\approx 2.9$ L (about 70% of nonsmokers lie below this value, against only 26% of smokers), and $p = 1.6 \times 10^{-10}$.

The advantage of the KS test is that it can detect "any kind of difference"; the price is that for any one specific kind of difference (such as a location shift) its power is lower than that of a dedicated test. It is sensitive to differences in the middle of the distribution and insensitive to differences in the tails. When the one-sample KS test is used to test normality and the mean and standard deviation have been estimated from the same data, the standard critical values no longer apply (the test is too conservative); the Lilliefors correction or the **Shapiro–Wilk test** should be used instead, always together with a QQ plot ([7.7.2](/7.7.2)).

![Comparing whole distributions. A: the empirical distribution functions of FEV for the 589 nonsmokers and 65 smokers among 654 children in East Boston (Tager et al. 1979; public version Kahn 2005); the Kolmogorov–Smirnov statistic D = 0.435 is the largest vertical distance between the two step functions. B: the five-point CT ratings of Hanley and McNeil (1982), 58 normal and 51 abnormal subjects: the Mann–Whitney statistic U/(n1 n2) = 0.893 is the area under the ROC curve](./plots/fev-ecdf.py)

## 8.8. Rank Correlation

The **correlation coefficient** (Pearson's $r$) measures linear association and is sensitive to outliers, and its test relies on bivariate normality. When we care only whether "the larger one variable is, the larger the other tends to be" (a monotone relationship), we use rank correlation.

**Definition 8.8.1 (Spearman and Kendall Rank Correlation Coefficients)** Rank the $x$ and the $y$ values of $n$ pairs of observations $(x_i, y_i)$ separately. The Pearson correlation coefficient between the two sets of ranks is called **Spearman's rank correlation coefficient** $r_s$; without ties,

$$
r_s = 1 - \frac{6\sum_i d_i^2}{n(n^2 - 1)},
$$
where $d_i$ is the difference between the two ranks of the $i$-th pair. Among all $\binom{n}{2}$ pairs of observations, call a pair concordant if $(x_i - x_j)(y_i - y_j) > 0$ and discordant if $< 0$; with $C$ and $D$ the numbers of concordant and discordant pairs,

$$
\tau = \frac{C - D}{n(n-1)/2}
$$
is called **Kendall's tau** (with ties one uses $\tau_b$, which adjusts the denominator).

Both lie in $[-1, 1]$, equal 1 for a monotone increasing relationship and $-1$ for a monotone decreasing one, and are invariant under monotone transformations. $\tau$ has a direct probabilistic interpretation: $(1 + \tau)/2$ is the probability that two randomly chosen individuals are ordered in the "same direction" by the two variables. For the same data $\lvert\tau\rvert$ is usually smaller than $\lvert r_s\rvert$ (approximately $\tau \approx \frac23 r_s$), so the two values cannot be compared with each other. For large $n$, $r_s\sqrt{(n-2)/(1 - r_s^2)}$ is approximately $t_{n-2}$.

**Example 8.8.1 (FEV with Age and Height)** For the 654 children:

| | Pearson $r$ | Spearman $r_s$ | Kendall $\tau_b$ |
|---|---|---|---|
| FEV and age | 0.756 | 0.798 | 0.625 |
| FEV and height | 0.868 | 0.888 | 0.721 |

The rank correlations are slightly higher than the Pearson correlations: FEV does not grow with height along a straight line but curves upward ([7.7.10](/7.7.10) fits log FEV), so the monotone relationship is stronger than the linear one. All three coefficients show that FEV is more strongly associated with height than with age. A full discussion of regression and correlation is in [7.7.10](/7.7.10).

## 8.9. Parametric or Nonparametric Methods

![Power of the t test (pooled variance) and the Wilcoxon rank-sum test: 20 observations per group, two-sided α = 0.05, 4000 simulations per point; the horizontal axis is the shift between the two distributions. A: normal data; the t test is slightly better (asymptotic relative efficiency 0.955). B: t distribution with 3 degrees of freedom (heavy tails). C: log-normal data (σ = 1, strongly right-skewed): at a shift of 0.6 the power of the t test is 0.34 and that of the rank-sum test 0.71. With heavy tails and skewness the power of the rank test is clearly higher. Simulated data](./plots/power-sim.py)

| Data and design | Parametric method | Nonparametric method |
|---|---|---|
| Paired, differences | Paired t test ([7.7.7](/7.7.7)) | Sign test (direction only), Wilcoxon signed-rank test |
| Two independent samples | Welch t test | Wilcoxon rank-sum test (Mann–Whitney U), permutation test |
| Three or more groups | One-way analysis of variance ([7.7.12](/7.7.12)) | Kruskal–Wallis test + Dunn's test |
| Whole distribution | — | Kolmogorov–Smirnov test |
| Association of two continuous variables | Pearson correlation ([7.7.10](/7.7.10)) | Spearman and Kendall rank correlation |

Principles for the choice:

1. For ordinal data (scores, grades) use rank methods: the arithmetic mean has no meaning for them (Example 8.4.1).
2. Do not switch to nonparametric methods for continuous data merely because "the normality test is significant". In large samples a normality test is significant even for negligible departures, while the t test is already robust enough; in small samples a normality test has very low power, and "not significant" proves nothing. Look at graphs (histogram, QQ plot) and judge in light of what you know about where the data come from.
3. For positive, right-skewed data whose group differences look like ratios (concentrations, titers), a t test after log transformation is often better than a rank test: it keeps the numerical information and yields a meaningful effect size such as the ratio of geometric means ([7.7.7](/7.7.7), Section 7.7).
4. For small samples with heavy tails or outliers, the power of rank methods can be far higher than that of the t test (panels B and C of the figure above).
5. Whichever method is used, report the size of the effect and an interval: the mean difference for t methods, the Hodges–Lehmann shift or $\theta = \mathbb{P}(X_1 > X_2)$ for rank methods. Nonparametric methods are not "assumption-free": independence is a prerequisite common to all methods, the rank-sum test also assumes that the two distributions have the same shape (otherwise it does not test location), and the permutation test assumes exchangeability.

## 8.10. Computing in Python

```python
import itertools
import numpy as np
import pandas as pd
from scipy import stats

# paired data: sign test and signed-rank test (Examples 8.2.1, 8.3.1, 8.3.2)
before = np.array([210, 169, 187, 160, 167, 176, 185, 206, 173, 146, 174, 201, 198, 148, 154])
after = np.array([201, 165, 166, 157, 147, 145, 168, 180, 147, 136, 151, 168, 179, 129, 131])
d = before - after - 10                       # H0: median drop <= 10 mmHg
print(stats.binomtest((d > 0).sum(), (d != 0).sum(), alternative="greater").pvalue)   # sign test, 0.029
print(stats.wilcoxon(d, alternative="greater").pvalue)                                # signed rank, 0.0019
sleep = np.array([1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4])
print(stats.wilcoxon(sleep).pvalue)                                                   # 0.0039 (zero dropped)

# rank-sum test, U / (n1 n2) and Hodges-Lehmann shift (Example 8.4.2)
fev = pd.read_csv("fev.csv")
x1, x0 = fev.loc[fev.smoke == 1, "fev"].to_numpy(), fev.loc[fev.smoke == 0, "fev"].to_numpy()
mw = stats.mannwhitneyu(x1, x0)
print(mw.pvalue, mw.statistic / (x1.size * x0.size))          # 4e-11, 0.749
print(np.median(np.subtract.outer(x1, x0)))                   # Hodges-Lehmann shift, 0.75 L

# ordinal CT ratings: U / (n1 n2) equals the AUC (Example 8.4.1)
normal = np.repeat(np.arange(1, 6), [33, 6, 6, 11, 2])
abnormal = np.repeat(np.arange(1, 6), [3, 2, 2, 11, 33])
u = stats.mannwhitneyu(abnormal, normal)
print(u.statistic / (normal.size * abnormal.size), u.pvalue)   # 0.893, 2e-13

# Kruskal-Wallis and Dunn (Example 8.5.1); Dunn's test e.g. scikit_posthocs.posthoc_dunn
tg = pd.read_csv("toothgrowth.csv")
groups = [g["len"].to_numpy() for _, g in tg.groupby("dose")]
print(stats.kruskal(*groups))                                 # H = 40.67, p = 1.5e-9

# exact permutation test (Example 8.6.1)
oj = tg.query("dose == 0.5 and supp == 'OJ'")["len"].to_numpy()
vc = tg.query("dose == 0.5 and supp == 'VC'")["len"].to_numpy()
res = stats.permutation_test((oj, vc), lambda a, b: a.mean() - b.mean(),
                             permutation_type="independent", n_resamples=np.inf)
print(res.statistic, res.pvalue)                              # 5.25, 0.0052

# Kolmogorov-Smirnov and rank correlation (Examples 8.7.1, 8.8.1)
print(stats.ks_2samp(x1, x0))                                 # D = 0.435
print(stats.spearmanr(fev.height, fev.fev).statistic, stats.kendalltau(fev.height, fev.fev).statistic)
```

## Summary

- Rank methods use only the order of the observations; their null distributions do not depend on the population distribution, and they are unaffected by outliers and monotone transformations (Section 8.1). Their cost is measured by the asymptotic relative efficiency (Definition 8.1.1): for normal data it is $3/\pi = 0.955$ for the Wilcoxon test relative to the t test and $2/\pi = 0.637$ for the sign test, while with heavy tails or skewness the rank tests can be far better than the t test (the figure of Section 8.9).
- Summary of methods:

  | Problem | Method | Statistic | Example |
  |---|---|---|---|
  | Paired, direction only | Sign test (Formula 8.2.1) | $n_+ \sim \mathrm{Bin}(n, 1/2)$ | Example 8.2.1 |
  | Paired, symmetric differences | Wilcoxon signed-rank test (Formula 8.3.1) | $T_+$ | Examples 8.3.1, 8.3.2 |
  | Two independent samples | Wilcoxon rank-sum test / Mann–Whitney U (Formula 8.4.1) | $W$, $U/(n_1n_2)$ = AUC | Examples 8.4.1–8.4.3 |
  | Several groups | Kruskal–Wallis (Formula 8.5.1) + Dunn (Formula 8.5.2) | $H \overset{H_0}{\approx} \chi^2_{k-1}$ | Example 8.5.1 |
  | Arbitrary statistic | Permutation test (Definition 8.6.1) | Exact distribution under label reassignment | Example 8.6.1 |
  | Whole distribution | Kolmogorov–Smirnov (Formula 8.7.1) | $D = \sup\lvert\hat F_1 - \hat F_2\rvert$ | Example 8.7.1 |
  | Monotone association | Spearman $r_s$, Kendall $\tau$ (Definition 8.8.1) | Correlation of ranks | Example 8.8.1 |

- The Mann–Whitney $U/(n_1 n_2)$ estimates $\mathbb{P}(X_1 > X_2) + \frac12\mathbb{P}(X_1 = X_2)$, the area under the ROC curve: the AUC of 0.893 for the CT ratings is the statistic of the rank-sum test (Example 8.4.1). The rank-sum test is a comparison of medians only when the two distributions have the same shape.
- The permutation test rests on randomization, and the p-value of the t test approximates the permutation p-value (Example 8.6.1: 0.0053 versus 0.0052).
- Main thread: the rank-sum test for FEV ($p = 4 \times 10^{-11}$, shift 0.75 L) agrees with the t test; changing the test cannot repair confounding built into the design. Do not switch to a nonparametric method merely because "the normality test is significant"; ordinal data, heavy tails and outliers are where rank methods earn their keep.

## Questions

1. State which test should be used in each of the following situations: (a) 20 patients each rate pain relief under two drugs (none / mild / moderate / complete); (b) tumor volumes in two groups of mice, 6 per group, with one tumor 10 times as large as the rest; (c) comparison of weight gain in rats on three diets, 30 per group, with roughly symmetric data; (d) testing whether the expression of each of 50 genes is monotonically related to the concentration of a protein.

   **Answer** (a) Paired ordinal data: the Wilcoxon signed-rank test needs the sizes of the differences to be meaningful, which differences between ordered grades need not be, so the safest choice is the sign test (compare only under which drug each patient's relief was better). (b) Small samples with an extreme outlier: the Wilcoxon rank-sum test (or a permutation test), after first checking whether this mouse's data are in error ([7.7.2](/7.7.2)); if the volumes are roughly symmetric on the log scale, a t test after log transformation is also possible. (c) Large samples, symmetric data: one-way analysis of variance ([7.7.12](/7.7.12)); nonparametric methods are unnecessary. (d) The Spearman rank correlation of each gene with the protein concentration (insensitive to measurement scale and outliers); the 50 tests require a multiple-testing correction ([7.7.20](/7.7.20)).

2. For Student's sleep data (differences 1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4), carry out the Wilcoxon signed-rank test by hand: write down the rank of each nonzero difference, find $T_+$, and obtain the two-sided p-value from the exact distribution; then compute $z$ from the normal approximation (no continuity correction, with the correction for ties) and compare the two.

   **Answer** Dropping 0.0 leaves 9 values, which sorted by absolute value are 0.8 (1), 1.0 (2), 1.2 (3), 1.3, 1.3 (4.5, 4.5), 1.4 (6), 1.8 (7), 2.4 (8), 4.6 (9). $T_+ = 45$ (all are positive), the largest possible value. In the exact distribution $T_+ = 45$ arises from only one combination of signs, so $\mathbb{P}(T_+ = 45) = 1/2^9$ and the two-sided $p = 2/512 = 0.0039$. Normal approximation: $\mathbb{E}T_+ = 9 \times 10/4 = 22.5$, $\operatorname{Var} = 9 \times 10 \times 19/24 - (2^3 - 2)/48 = 71.25 - 0.125 = 71.125$, $z = 22.5/8.434 = 2.67$, and the two-sided $p = 0.0076$. At $n = 9$ the normal approximation overestimates the p-value by a factor of two; with small samples the exact distribution should be used.

3. Using the captopril data, explain why, for the same question (does the mean reduction exceed 10 mmHg?), the p-values of the sign test, the signed-rank test and the t test decrease in that order (0.029, 0.0019, 0.0009). Under what circumstances would the order be reversed?

   **Answer** The three use progressively more information: the sign test uses only the signs of $d_i - 10$ (11 positive, 3 negative); the signed-rank test also uses the order of their sizes (the three negative differences $-1$, $-6$, $-7$ are all small and have low ranks); the t test uses all the numerical values. For approximately normal data, more information means higher power (asymptotic relative efficiencies 0.637 < 0.955 < 1). If the distribution of the differences is heavy-tailed (a few extreme values), the mean and standard deviation in the t test are dominated by the extreme values and its power falls, so the rank test may be better; if the distribution is asymmetric or only the direction can be trusted, the sign test is the only test whose assumptions hold.

4. In the CT data of Hanley and McNeil, suppose ratings 4 and 5 are merged as "abnormal" and ratings 1–3 as "normal". What are the sensitivity and specificity for this single cutoff? What is the "AUC" corresponding to this single cutoff, and why is it smaller than 0.893?

   **Answer** Among the abnormal subjects, $11 + 33 = 44$ are rated 4–5, so the sensitivity is $44/51 = 0.863$; among the normal subjects, $33 + 6 + 6 = 45$ are rated 1–3, so the specificity is $45/58 = 0.776$. After dichotomization the ROC curve has a single interior point, and the area under the polyline joining the points is $(\text{Se} + \text{Sp})/2 = (0.863 + 0.776)/2 = 0.819$; this equals $U/(n_1 n_2)$ after dichotomization. It is smaller than 0.893 because merging categories discards information: the five-point rating distinguishes "probably abnormal" from "definitely abnormal", whereas after dichotomization all the ordering within a category becomes ties.

5. Explain why a permutation test requires "exchangeability", and decide whether the p-value is reliable when a permutation test is used to compare the mean serum ferritin of 30 men and 30 women (the variances of the two groups differ greatly).

   **Answer** The null distribution of a permutation test is obtained under the assumption that "the labels can be interchanged without changing the joint distribution". If $H_0$ is only that "the means are equal" while the variances differ, interchanging labels changes the distribution of the data (moving high-variability observations into the low-variability group), the null distribution is no longer correct, and the type I error rate may deviate from its nominal value (the same problem as the pooled-variance t test with unequal variances, [7.7.7](/7.7.7), Section 7.5). The p-value here is therefore not entirely reliable, and the Welch test is preferable. Ferritin is right-skewed, so it is best to take logarithms first and compare geometric means (the log transformation often makes the variances similar), or to use the Welch statistic (rather than the mean difference) as the statistic to be permuted, which is approximately valid in large samples.

6. Suppose a study compares the inflammation scores (0–3, 6 rabbits per group) of four anti-inflammatory drugs in the rabbit eye by the Kruskal–Wallis test and obtains $p < 0.01$. The investigators then run a Wilcoxon rank-sum test on each pair of drugs, 6 in all, and report the two pairs with $p < 0.05$ as "significantly different". Point out the problems and give the correct procedure.

   **Answer** Problems: (1) the 6 comparisons are made without a multiplicity correction, so the overall type I error rate is inflated (up to about $6 \times 0.05$); (2) each comparison re-ranks only two groups, which is inconsistent with the ranks used in the Kruskal–Wallis test; (3) data scored 0–3 with 6 animals per group have very many ties, so exact or permutation p-values that take ties into account should be used. Correct procedure: use Dunn's test (based on the pooled ranks) with a Bonferroni or Holm correction for the 6 comparisons; if only comparisons of each drug with the control were of interest beforehand, do only those, which reduces the number of corrections and raises power. Also report the median and the distribution of scores in each group.

7. Compute from the definitions the Spearman and Kendall rank correlation coefficients for the following 5 pairs: $(x, y) = (1, 2), (2, 1), (3, 4), (4, 3), (5, 5)$.

   **Answer** The two sets of ranks are the data themselves. $d_i = -1, 1, -1, 1, 0$, $\sum d_i^2 = 4$, and $r_s = 1 - 6 \times 4/(5 \times 24) = 0.8$. Checking the 10 pairs one by one: observations 1 and 2, $(1,2),(2,1)$, are discordant; observations 3 and 4, $(3,4),(4,3)$, are discordant; the other 8 pairs are all concordant. $C = 8$, $D = 2$, and $\tau = (8 - 2)/10 = 0.6$. This is close to the approximation $\tau \approx \frac23 r_s = 0.53$, and $\tau$ is smaller than $r_s$.

8. For FEV, both the two-sample KS test and the rank-sum test are highly significant. Construct a situation in which the two groups have the same median and mean, the rank-sum test is not significant, and the KS test can detect the difference, and explain what this might mean biologically.

   **Answer** For example, one group comes from $\mathcal{N}(0, 1)$ and the other from $\mathcal{N}(0, 3^2)$ (or from a bimodal distribution centered at 0): the two groups have the same location, $\mathbb{P}(X_1 > X_2) = 1/2$, and the rank-sum test will hardly reject even in large samples; but the two empirical distribution functions are clearly separated on both sides, and the KS test can detect the difference. Biologically, a treatment that leaves the mean response unchanged but makes the responses of individuals more dispersed may indicate two subpopulations, responders and non-responders (for example, a drug effective only in carriers of a certain genotype); comparing only means or medians would then miss the most important information. One should plot the distributions and look for a variable that separates the subpopulations.

9. (Design question) A study compares the healing time (days) of two wound dressings, and about 10% of the wounds are expected still to be unhealed at the end of the 60-day follow-up. Why are neither the t test nor the rank-sum test quite appropriate? How should the data be analyzed?

   **Answer** For an unhealed wound we know only that "the healing time exceeds 60 days"; these are censored data ([7.7.1](/7.7.1)). Recording them as 60 days underestimates the healing time, and deleting them causes bias (the ones deleted are precisely the slowest to heal). The rank-sum test can place them all last (as tied maxima), which is feasible when all the censoring occurs at the same time, but it cannot handle loss to follow-up at different times. The standard approach is survival analysis: Kaplan–Meier curves describe the healing process in the two groups, the log-rank test compares the groups (it is itself a rank test), and the Cox model estimates the hazard ratio ([7.7.16](/7.7.16)).

10. A reviewer argues: "Your data have a Shapiro–Wilk $p = 0.03$ and so are not normally distributed; you should switch to a nonparametric test." The data are the systolic blood pressures of 400 adults, 200 in each of two groups. How would you respond?

    **Answer** (1) With 200 per group the sampling distribution of the mean is approximately normal by the central limit theorem, and the t test (Welch) is very robust to mild non-normality. (2) In large samples a normality test is significant even for departures that are practically irrelevant; $p = 0.03$ says only that the data are "not perfectly normal", and no real data are perfectly normal. (3) One should look at the QQ plot and the histogram to judge the extent and shape of the departure; if it is only mild right skewness, the t test can be reported, with the rank-sum test or a log transformation as a sensitivity analysis showing that the conclusion is unchanged. (4) Switching to the rank-sum test would change the quantity being compared (from the mean difference to $\mathbb{P}(X_1 > X_2)$), and the mean difference in systolic blood pressure is clinically more meaningful.
