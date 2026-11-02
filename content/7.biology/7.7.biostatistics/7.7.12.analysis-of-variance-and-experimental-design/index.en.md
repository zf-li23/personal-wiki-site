---
title: Analysis of Variance and Experimental Design
description: Why multiple t tests should not be used to compare several groups; the model, sum-of-squares decomposition, F test and assumptions of one-way analysis of variance; multiple comparisons (family-wise error rate, LSD, Bonferroni, Holm, Tukey, Dunnett) and how to choose among them; contrasts and linear and quadratic trends in dose; two-way analysis of variance, main effects, interaction and simple effects; analysis of covariance and adjusted means; the basic principles of experimental design (replication, randomization and blocking), completely randomized, randomized block and factorial designs, experimental units, biological and technical replicates, pseudoreplication, sample size; nonparametric alternatives. The examples are the guinea-pig vitamin C experiment (ToothGrowth) and birth weight.
source_hash: 11bd1e99447e
---

[7.7.7](/7.7.7) compared two groups; with three or more groups two new problems arise: what is the test that compares all the groups at once, and, once a difference among the groups has been found, how do we learn which groups differ without being misled by the many tests involved. Analysis of variance (ANOVA) answers the first question and multiple comparisons answer the second. This chapter begins with one-way analysis of variance and multiple comparisons, and then treats contrasts (prespecified, biologically meaningful comparisons among groups, such as the trend of a dose response), two-way analysis of variance and interaction when two factors vary together, and analysis of covariance with a continuous covariate. Analysis of variance was invented by R. A. Fisher at the Rothamsted agricultural station to analyze field trials, and it is one with experimental design: the second half of the chapter covers the basic principles of design, namely replication, randomization and blocking, factorial designs, and one of the commonest and most serious errors in laboratory research, pseudoreplication. The main example is Crampton's (1947) guinea-pig experiment ToothGrowth: [7.7.7](/7.7.7) compared the two delivery methods at each dose, and [7.7.8](/7.7.8) compared the three doses by the Kruskal–Wallis test; here dose and delivery method are put into one model. The mathematics of one-way and two-way analysis of variance (the cell-means model, the factor-effects model, the derivation of multiple comparisons) is in [3.3.12](/3.3.12)–[3.3.14](/3.3.14); the relationship of analysis of variance to regression is in [7.7.10](/7.7.10), Section 10.7.3; models with blocks or individuals as random effects (repeated measures, between-batch variation) are in [7.7.17](/7.7.17).

## 12.1. Why Not Many t Tests

Among $k$ groups there are $m = k(k - 1)/2$ pairs to compare. If a t test is done on each pair at $\alpha = 0.05$, then even when the population means of all the groups are equal, the probability of at least one false positive is far greater than 0.05. If the $m$ tests were mutually independent this probability would be $1 - 0.95^m$: 0.14 for $k = 3$, 0.40 for $k = 5$ and 0.90 for $k = 10$. The pairwise tests are not in fact independent (they share the data of the groups), so the probability is somewhat lower than this upper bound but still far above 0.05: in a simulation with 10 normal observations per group, it is 0.13, 0.29 and 0.63 for $k = 3, 5, 10$ (panel A below).

What is controlled here is the error rate of a family of tests as a whole, the **family-wise error rate** ([3.4.12](/3.4.12)): the probability of making at least one type I error in the family. Analysis of variance first answers "are all the group means equal?" with a single F test, whose type I error rate is $\alpha$; when we need to know which groups differ, we then use multiple-comparison methods that control the family-wise error rate (Section 12.3).

## 12.2. One-Way Analysis of Variance

### 12.2.1. The Model and the Decomposition of the Sum of Squares

**Formula 12.2.1 (One-Way Analysis of Variance)** Suppose group $i$ ($i = 1, \dots, k$) has $n_i$ observations, $N = \sum n_i$, and the model is

$$
y_{ij} = \mu + \alpha_i + \varepsilon_{ij}, \qquad \varepsilon_{ij} \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2), \quad \textstyle\sum_i n_i\alpha_i = 0,
$$
where $\mu$ is the overall mean and $\alpha_i$ the effect of group $i$. The total sum of squares decomposes as

$$
\underbrace{\sum_{i,j} (y_{ij} - \bar y)^2}_{\mathrm{SS}_{\text{total}}} = \underbrace{\sum_i n_i(\bar y_i - \bar y)^2}_{\mathrm{SS}_{\text{between}}} + \underbrace{\sum_{i,j} (y_{ij} - \bar y_i)^2}_{\mathrm{SS}_{\text{within}}},
$$
with degrees of freedom $N - 1 = (k - 1) + (N - k)$. Under $H_0\colon \alpha_1 = \cdots = \alpha_k = 0$,

$$
F = \frac{\mathrm{SS}_{\text{between}}/(k - 1)}{\mathrm{SS}_{\text{within}}/(N - k)} = \frac{\mathrm{MS}_{\text{between}}}{\mathrm{MS}_{\text{within}}} \sim F_{k-1,\,N-k}.
$$

The name **analysis of variance** comes from its reasoning: the within-group mean square $\mathrm{MS}_{\text{within}}$ is an unbiased estimator of $\sigma^2$ whether or not $H_0$ holds; the between-group mean square also estimates $\sigma^2$ under $H_0$, and otherwise includes the differences among groups, with expectation $\sigma^2 + \sum n_i\alpha_i^2/(k - 1)$. A ratio of the two **mean squares** much greater than 1 shows that the dispersion of the group means exceeds what random error can explain. For $k = 2$, $F = t^2$ and analysis of variance is the pooled-variance **two-sample t-test**. The within-group mean square $\mathrm{MS}_{\text{within}}$ generalizes the pooled variance of [7.7.7](/7.7.7) to $k$ groups and is the basis of all the standard errors in multiple comparisons.

### 12.2.2. The Dose of Vitamin C

**Example 12.2.1 (Dose in ToothGrowth)** Sixty guinea pigs were randomly divided into 6 groups of 10, with three daily doses (0.5, 1, 2 mg/d) × two delivery methods (orange juice OJ, ascorbic acid VC), and the length of the odontoblasts was measured. First ignore the delivery method and compare the three doses (20 animals each): the means are 10.61, 19.74 and 26.10, the standard deviations 4.50, 4.42 and 3.77, and the overall mean 18.81.

| Source | Degrees of freedom | Sum of squares | Mean square | $F$ | $p$ |
|---|---|---|---|---|---|
| Dose | 2 | 2426.4 | 1213.2 | 67.4 | $9.5 \times 10^{-16}$ |
| Within | 57 | 1025.8 | 18.00 | | |
| Total | 59 | 3452.2 | | | |

The effect of dose is overwhelmingly significant, with the between-group sum of squares accounting for $2426.4/3452.2 = 70\%$ of the total (in analysis of variance this proportion is called $\eta^2$, the $R^2$ of regression). The Kruskal–Wallis test of [7.7.8](/7.7.8) Example 8.5.1 gives $H = 40.7$ and $p = 1.5 \times 10^{-9}$ for the same data, with the same conclusion. The format of the analysis-of-variance table is exactly that of the **ANOVA table** of regression: a regression with only categorical independent variables is an analysis of variance ([7.7.10](/7.7.10), Section 10.7.3).

![Decomposition of the variation in the ToothGrowth experiment (60 guinea pigs, Crampton 1947; R datasets::ToothGrowth). A: odontoblast length grouped by daily vitamin C dose (the two delivery methods pooled, 20 animals per dose); short horizontal bars are the group means and the dashed line is the overall mean; the between-group part is the dispersion of the group means about the overall mean (arrows) and the within-group part is the dispersion of the animals about their own group mean (thin lines). B: decomposition of the total sum of squares in one-way (dose) and two-way (dose, delivery method, interaction) analysis of variance: with the second factor and the interaction in the model the residual part falls from 1026 to 712](./plots/anova-decomposition.py)

### 12.2.3. Assumptions and Transformations

The assumptions of analysis of variance are those of the two-sample t test: observations within groups are independent, each group is approximately normal, and the groups have equal variance.

- Independence is guaranteed by the design and is the most important (pseudoreplication, Section 12.7.4).
- Normality: when the group sizes are similar and not too small, analysis of variance is quite robust to non-normality (the **central limit theorem** acting on the group means); check with a Q–Q plot of the residuals, and consider a transformation or rank methods (Section 12.8) when there is severe skewness or there are outliers. The Shapiro–Wilk test of the ToothGrowth residuals gives $p = 0.11$.
- Homogeneity of variance: with equal sample sizes, analysis of variance is also quite robust to unequal variances; when the sample sizes are unequal and the small groups have larger variance, the F test is too liberal (the same reasoning as in [7.7.7](/7.7.7), Section 7.5). The check is **Levene's test** ([3.3.5](/3.3.5); the version centered at the median is the **Brown–Forsythe test**), not **Bartlett's test**, which is sensitive to non-normality. For the three ToothGrowth doses Levene's test gives $p = 0.53$. When the variances are clearly unequal, use Welch's one-way analysis of variance (R's `oneway.test`).

The choice of transformation is as in [7.7.10](/7.7.10), Section 10.5: take logarithms when the standard deviation is proportional to the mean (titers, concentrations, latencies); the square root when the variance is proportional to the mean (counts, approximately Poisson); and the logit or arcsine square root for proportions or percentages. These are all **variance-stabilizing transformations** ([3.3.6](/3.3.6)).

### 12.2.4. An Example with Unequal Sample Sizes

**Example 12.2.2 (Birth Weight and Race)** The 189 newborns in birthwt are divided by maternal race into three groups: white, 96, mean 3103 g (standard deviation 728); black, 26, 2720 g (639); other, 67, 2805 g (722). One-way analysis of variance gives $F = 4.91$ with degrees of freedom $(2, 186)$ and $p = 0.008$. The sample sizes of the three groups differ greatly but the standard deviations are similar, so the F test is credible. This is an **observational study**: the differences between races may arise partly from other factors (smoking, maternal weight, socioeconomic status), which Section 12.6 adds to the model.

## 12.3. Multiple Comparisons

### 12.3.1. Pairwise Comparisons and the Family-Wise Error Rate

After a significant F test, we often ask which groups differ. The t statistic comparing group $i$ with group $j$ uses the within-group mean square of the analysis of variance as the estimate of variance:

$$
t_{ij} = \frac{\bar y_i - \bar y_j}{\sqrt{\mathrm{MSE}(1/n_i + 1/n_j)}}, \qquad \nu = N - k,
$$
and the methods differ in the critical value used, that is, in how the family-wise error rate is controlled.

- The LSD method, that is the **least significant difference** method (see [3.3.13](/3.3.13)): use $t_{\nu,\alpha/2}$ with no adjustment. It is done only after a significant F test (Fisher's protected LSD), which controls the family-wise error rate when $k = 3$ but not when $k \ge 4$.
- The **Bonferroni correction**: use $\alpha/m$ for each test, or multiply the p-values by $m$. It is valid under any dependence structure and is too conservative when there are many comparisons.

**Definition 12.3.1 (Holm's Method)** Arrange the $m$ p-values in increasing order $p_{(1)} \le \cdots \le p_{(m)}$, with the corresponding hypotheses $H_{(1)}, \dots, H_{(m)}$. Starting from the smallest: if $p_{(1)} \le \alpha/m$, reject $H_{(1)}$ and continue; if $p_{(2)} \le \alpha/(m - 1)$, reject $H_{(2)}$ and continue; and so on; stop the first time that $p_{(r)} > \alpha/(m - r + 1)$ occurs, and do not reject $H_{(r)}, \dots, H_{(m)}$. This stepwise testing procedure is called **Holm's method**. Equivalently, the adjusted p-values are $\tilde p_{(r)} = \max_{s \le r}\min\{1, (m - s + 1)p_{(s)}\}$.

Like Bonferroni, Holm's method controls the family-wise error rate under any dependence structure, but it is always at least as powerful, so there is no reason to use Bonferroni instead of Holm. Hochberg's method proceeds backward from the largest p-value and is more powerful when the test statistics are positively correlated.

**Example 12.3.1** Four comparisons have p-values 0.005, 0.015, 0.021 and 0.09, with $\alpha = 0.05$. Bonferroni: only $0.005 \le 0.0125$, so one is rejected (adjusted p-values 0.02, 0.06, 0.084, 0.36). Holm: $0.005 \le 0.05/4$, $0.015 \le 0.05/3 = 0.0167$, $0.021 \le 0.05/2$, $0.09 > 0.05$, so three are rejected (adjusted p-values 0.02, 0.045, 0.045, 0.09). Hochberg: starting from the largest, $0.09 > 0.05$ and $0.021 \le 0.025$, so 0.021 and the three smaller ones are rejected, the same as Holm.

### 12.3.2. Tukey and Dunnett

The $m$ pairwise comparisons have a specific correlation structure, which can be exploited to obtain more exact critical values than Bonferroni's.

- **Tukey's method** ([3.3.13](/3.3.13)): all pairwise comparisons. The largest difference of group means divided by the standard error has the studentized range distribution $q_{k,\nu}$; with equal sample sizes, any pair whose difference exceeds

  $$
  \mathrm{HSD} = q_{k,\nu,\alpha}\sqrt{\mathrm{MSE}/n}
  $$
  is declared significant, with confidence intervals $\bar y_i - \bar y_j \pm \mathrm{HSD}$; with unequal sample sizes the Tukey–Kramer modification is used ($n$ replaced by $2/(1/n_i + 1/n_j)$). The family-wise error rate is exactly $\alpha$ (with equal sample sizes).

**Definition 12.3.2 (Dunnett's Test)** When each of $k - 1$ treatment groups is compared with the same control group, the multiple-comparison method that takes into account the correlation among these $k - 1$ comparisons caused by their sharing the control mean and makes the family-wise error rate exactly $\alpha$ is called **Dunnett's test**.

When only the comparisons of each treatment with the control are of interest, Dunnett's test has fewer comparisons ($k - 1$ rather than $k(k-1)/2$) and is more powerful than Tukey's. It is the standard procedure in pharmacology and toxicology for "comparing each dose group with the vehicle control".

**Example 12.3.2 (Dose in ToothGrowth)** $\mathrm{MSE} = 18.00$, $\nu = 57$, $n = 20$ per group, and the standard error of a pairwise difference is $\sqrt{18.00 \times 2/20} = 1.341$.

| Comparison | Difference | Unadjusted 95% interval | Tukey 95% simultaneous interval | Holm-adjusted $p$ |
|---|---|---|---|---|
| 1 versus 0.5 mg/d | 9.13 | $(6.44, 11.82)$ | $(5.90, 12.36)$ | $1.3 \times 10^{-8}$ |
| 2 versus 0.5 mg/d | 15.50 | $(12.81, 18.18)$ | $(12.27, 18.72)$ | $4 \times 10^{-16}$ |
| 2 versus 1 mg/d | 6.37 | $(3.68, 9.05)$ | $(3.14, 9.59)$ | $1.4 \times 10^{-5}$ |

The LSD is $t_{57,0.025} \times 1.341 = 2.69$ and Tukey's HSD is $q_{3,57,0.05}\sqrt{18.00/20} = 3.403 \times 0.949 = 3.23$. All three pairs are highly significant: each doubling of the dose clearly increases tooth growth. If 0.5 mg/d is taken as the control, Dunnett's simultaneous intervals are $(6.09, 12.17)$ for 1 mg/d and $(12.45, 18.54)$ for 2 mg/d, slightly narrower than Tukey's.

![Multiple comparisons. A: the probability of at least one false positive when all pairwise t tests among k groups (each at α = 0.05) are done and all the null hypotheses hold: the upper bound 1 − 0.95^m for independent tests (m = k(k − 1)/2, dashed) and simulation (10 normal observations per group, 2000 repetitions for each k); positive correlation among the tests makes the actual proportion lower than the bound, but still far above 0.05 (dotted). B: 95% intervals for the pairwise differences of the three doses of ToothGrowth (Crampton 1947; R datasets::ToothGrowth) (delivery methods pooled): thin lines are the unadjusted pooled-variance t intervals and thick lines the Tukey simultaneous intervals](./plots/multiple-comparisons.py)

### 12.3.3. Principles of Choice

| Situation | Method |
|---|---|
| One or two prespecified comparisons (the main hypotheses) | Ordinary t test or contrast (Section 12.4), unadjusted |
| A few prespecified comparisons | Holm (or Bonferroni) |
| All pairwise comparisons | Tukey (Tukey–Kramer) |
| Each treatment against a control | Dunnett |
| Post hoc exploration of arbitrary contrasts (including combinations) | Scheffé's method ([3.3.13](/3.3.13)), the most conservative |
| Hundreds or thousands of tests (genes, metabolites) | Control the false discovery rate rather than the family-wise error rate ([7.7.20](/7.7.20)) |

Some principles: plan the comparisons before looking at the data; do not do an F test first and then, if it is nonsignificant, "switch to another multiple-comparison method" until something is significant; report which method was used and how many pairs were compared, and give adjusted intervals and not merely asterisks. Multiple comparisons exist to control wrong conclusions and are not a procedural requirement: in a trial with two preregistered primary comparisons, testing each of them separately is reasonable ([7.7.18](/7.7.18)).

## 12.4. Contrasts and Trends

In many experiments the groups are not unrelated categories but have structure: increasing doses, "control, low dose, high dose", two drugs and their combination. The meaningful question is then not "are they all equal?" but a specific combination determined beforehand, for example "does the response increase linearly with dose?".

**Definition 12.4.1 (Contrast)** A linear combination of group means $L = \sum_{i=1}^k c_i\mu_i$ whose coefficients satisfy $\sum_i c_i = 0$ is called a **contrast**. Its estimate $\hat L = \sum c_i\bar y_i$ has standard error $\sqrt{\mathrm{MSE}\sum c_i^2/n_i}$, and $t = \hat L/\operatorname{se}(\hat L)$ has a t distribution with $N - k$ degrees of freedom; the sum of squares of the contrast is $\hat L^2/\sum(c_i^2/n_i)$ with 1 degree of freedom. With equal sample sizes, two contrasts whose coefficients satisfy $\sum_i c_i c_i' = 0$ are called orthogonal; $k - 1$ mutually orthogonal contrasts decompose the between-group sum of squares completely.

The difference of two groups ($c = (1, -1, 0)$) is the simplest contrast. When the dose levels are equally spaced, the orthogonal polynomial coefficients give tests of trend: for 3 levels the linear contrast is $(-1, 0, 1)$ and the quadratic contrast $(1, -2, 1)$; for 4 levels they are $(-3, -1, 1, 3)$, $(1, -1, -1, 1)$ and $(-1, 3, -3, 1)$.

**Example 12.4.1 (Trend of the Dose Response)** The ToothGrowth doses 0.5, 1 and 2 mg/d are equally spaced on the log scale (each doubles). The linear contrast is $\hat L = -10.61 + 26.10 = 15.50$ with standard error $\sqrt{18.00 \times 2/20} = 1.341$, $t = 11.55$ and sum of squares 2401.0; the quadratic contrast is $\hat L = 10.61 - 2 \times 19.74 + 26.10 = -2.77$ with standard error $\sqrt{18.00 \times 6/20} = 2.324$, $t = -1.19$, $p = 0.24$ and sum of squares 25.5. Their sum $2401.0 + 25.5 = 2426.4$ is exactly the between-group sum of squares. The effect of dose is almost entirely a linear trend in log dose (length increases by about 7.7 for each doubling), with no significant curvature.

A linear contrast uses only 1 degree of freedom and concentrates the test on one specific alternative; when the true pattern is indeed a trend, it is more powerful than the overall F test with 2 degrees of freedom. When the outcome in the dose groups is dichotomous, the corresponding method is the **Cochran–Armitage trend test** ([7.7.9](/7.7.9)). The coefficients of a contrast must be chosen before looking at the data; choosing coefficients after looking at the means is a post hoc comparison and requires an adjustment such as Scheffé's.

## 12.5. Two-Way Analysis of Variance

### 12.5.1. The Model and Interaction

When two factors vary together, for example dose (3 levels) and delivery method (2 levels) with all 6 combinations each given to $n$ animals, both factors can be studied in one model.

**Definition 12.5.1 (Main Effects and Interaction)** Let factor A have $a$ levels and factor B have $b$ levels, and write the population mean of the $(i, j)$-th combination (cell) as $\mu_{ij}$, with

$$
\mu_{ij} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij},
$$
$\sum_i\alpha_i = \sum_j\beta_j = \sum_i(\alpha\beta)_{ij} = \sum_j(\alpha\beta)_{ij} = 0$. $\alpha_i$ and $\beta_j$ are called the **main effects** of A and B, and $(\alpha\beta)_{ij}$ the **interaction effect** of A and B. When all $(\alpha\beta)_{ij} = 0$, the differences among the levels of A are the same at every level of B, and the effects of the two factors are said to be additive.

An interaction means that "the effect of one factor depends on the level of the other". It may be a difference of degree (both lines rise but with different slopes) or a difference of direction (A is better than B under one condition and the reverse under another). Whether an interaction exists depends on the scale: an interaction on the original scale may disappear on the log scale (multiplicative effects are additive on the log scale), so the scale must be stated.

The total sum of squares decomposes into A, B, AB and error ($\mathrm{SS}_A + \mathrm{SS}_B + \mathrm{SS}_{AB} + \mathrm{SS}_E$), with degrees of freedom $(a - 1) + (b - 1) + (a - 1)(b - 1) + ab(n - 1)$, and the F statistic of each effect has $\mathrm{MS}_E$ as denominator ([3.3.14](/3.3.14)). Each cell must have at least 2 observations to separate the interaction from the error.

### 12.5.2. Dose × Delivery Method

**Example 12.5.1 (Two-Way Analysis of Variance for ToothGrowth)** The means of the 6 cells (10 animals each):

| Delivery method | 0.5 mg/d | 1 mg/d | 2 mg/d |
|---|---|---|---|
| Orange juice (OJ) | 13.23 | 22.70 | 26.06 |
| Ascorbic acid (VC) | 7.98 | 16.77 | 26.14 |

| Source | Degrees of freedom | Sum of squares | Mean square | $F$ | $p$ |
|---|---|---|---|---|---|
| Delivery method | 1 | 205.4 | 205.4 | 15.6 | 0.0002 |
| Dose | 2 | 2426.4 | 1213.2 | 92.0 | $4 \times 10^{-18}$ |
| Interaction | 2 | 108.3 | 54.2 | 4.11 | 0.022 |
| Error | 54 | 712.1 | 13.19 | | |
| Total | 59 | 3452.2 | | | |

The interaction is significant ($p = 0.022$): the difference between delivery methods varies with dose. The **interaction plot** ([3.3.14](/3.3.14)) below shows two lines that are not parallel: at low and medium doses orange juice is clearly better, and at 2 mg/d the two are the same. With the delivery method and the interaction in the model, the error mean square falls from 18.00 in the one-way analysis to 13.19, and the F statistic for dose also rises from 67.4 to 92.0: more variation is explained and the error term is smaller. On the log scale the interaction is still significant ($F = 5.67$, $p = 0.006$); it is not caused by the scale.

When an interaction is significant, tests of main effects are hard to interpret: "the main effect of delivery method" is the difference averaged over the three doses, and this difference is 0 at 2 mg/d and about 5–6 at the low doses, so the average describes neither actual situation. The simple effects should be reported: compare the two delivery methods at each dose (using the two-way model's $\mathrm{MS}_E = 13.19$ with 54 degrees of freedom, so the standard error of a difference is $\sqrt{13.19 \times 2/10} = 1.624$):

| Dose | OJ − VC | 95% interval | $p$ |
|---|---|---|---|
| 0.5 mg/d | 5.25 | $(1.99, 8.51)$ | 0.002 |
| 1 mg/d | 5.93 | $(2.67, 9.19)$ | 0.0006 |
| 2 mg/d | $-0.08$ | $(-3.34, 3.18)$ | 0.96 |

This agrees with the Welch t tests done separately in [7.7.7](/7.7.7) Example 7.3.3, but uses all 60 animals to estimate the error and so gives narrower intervals; the three simple effects are comparisons of prior interest, and if the family-wise error rate is to be controlled, Holm's method can be applied to the three p-values (adjusted values 0.004, 0.002, 0.96). A biological interpretation: the vitamin C in orange juice is better absorbed or used at low doses (or other constituents of orange juice contribute), and at the high dose both sources have already brought the effect close to saturation.

![Interaction plot for ToothGrowth (Crampton 1947; R datasets::ToothGrowth): the mean odontoblast length of 10 guinea pigs in each group with 95% confidence intervals (based on the error mean square of the two-way analysis of variance, 54 degrees of freedom); the horizontal axis is the daily dose on a log scale, orange for orange juice (OJ) and blue for ascorbic acid (VC). The two lines are clearly not parallel: orange juice is better at 0.5 and 1 mg/d, and the two are the same at 2 mg/d](./plots/interaction-plot.py)

### 12.5.3. Unbalanced Data

When the cell sample sizes are equal (a balanced design), the sums of squares of the effects are uniquely determined and do not depend on the order of entry into the model. When the sample sizes are unequal, the factors are no longer orthogonal, and the sum of squares of an effect depends on which other effects are adjusted for: sequential sums of squares (type I, in order of entry), sums of squares adjusted for the other main effects (type II), and sums of squares adjusted for all other effects including interactions (type III). Type II is recommended in the absence of interaction; with interaction, rather than arguing over which kind of sum of squares, simply report the cell means and the simple effects. A balanced design is statistically the most efficient, the most robust to unequal variances and the simplest to interpret, which is the reason for making the groups equal in size whenever possible when designing an experiment.

## 12.6. Analysis of Covariance

**Definition 12.6.1 (Analysis of Covariance)** Add a continuous covariate $x$ to the analysis-of-variance model:

$$
y_{ij} = \mu + \alpha_i + \beta(x_{ij} - \bar x) + \varepsilon_{ij},
$$
and compare the groups at the same value of the covariate; this analysis is called **analysis of covariance** (ANCOVA). The fitted values $\mu + \alpha_i$ of the groups at $x = \bar x$ are called adjusted means, that is **least squares means** ([3.3.14](/3.3.14)).

Analysis of covariance is multiple regression with dummy variables and a continuous variable ([7.7.10](/7.7.10), Section 10.7). It has two uses: in a randomized experiment, adding a baseline value related to the outcome (such as the blood pressure before treatment) reduces the error variance and raises power; in observational data, it adjusts for differences among the groups in the covariate (confounding). The basic assumption is that the regression lines of the groups are parallel (the same slope $\beta$), tested by a model with a "group × covariate" interaction term; when the slopes clearly differ, the adjusted mean depends on the $x$ at which the comparison is made, and a single adjusted mean is meaningless.

**Example 12.6.1 (Race, Smoking and Birth Weight)** The three groups of mothers in Example 12.2.2 differ in the proportion who smoke (white 52/96, black 10/26, other 12/67) and in weight (mean weight at the last menstrual period: white 132 lb, black 147 lb, other 120 lb). Putting smoking and maternal weight into the model:

$$
\widehat{\text{birth weight}} = 2799 - 504\,\text{black} - 395\,\text{other} - 400\,\text{smoking} + 3.94\,\text{maternal weight (lb)}.
$$
The test of parallelism of the groups (race × maternal weight) gives $F = 0.49$, $p = 0.61$. The effect of race is more pronounced after adjustment ($F = 8.68$ with degrees of freedom $(2, 184)$, $p = 0.0003$, against $p = 0.008$ before adjustment): the adjusted means (at the mean proportion smoking and mean maternal weight) are 3154 g for white, 2650 g for black and 2759 g for other, and the difference between black and white rises from the unadjusted 383 g to 504 g (95% interval 202–806 g), because black mothers are on average heavier and each additional 1 kg of maternal weight goes with 8.7 g more in the baby. The coefficient of smoking is $-400$ g (95% interval $-614$ to $-186$), larger than the unadjusted difference between the two groups of 284 g in [7.7.7](/7.7.7): in this sample the proportion of white mothers who smoke is the highest, and the babies of white mothers are heavier to begin with, so without adjustment for race the harm of smoking is partly masked. Confounding can not only create spurious associations (the FEV example) but also mask real ones.

![Analysis of covariance for birth weight (189 deliveries, Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt). A: birth weight against maternal weight at the last menstrual period (lb), colored by race; the lines are from the model with race, smoking and maternal weight (common slope), drawn for nonsmokers. B: unadjusted means (circles) and adjusted means (squares, at the mean maternal weight and proportion smoking) of birth weight in each race, with 95% intervals](./plots/ancova-birthwt.py)

## 12.7. Basic Principles of Experimental Design

### 12.7.1. Replication, Randomization and Blocking

The three principles Fisher proposed for field trials remain the foundation of all experimental design:

1. Replication: each treatment is applied to several independent experimental units, so that error can be estimated, inferences made, and error reduced by averaging.
2. **Randomization** ([7.7.5](/7.7.5)): treatments are allocated to experimental units at random, so that unknown disturbing factors are spread evenly over the groups, and a basis is provided for the test (the theoretical basis of the permutation test, [7.7.8](/7.7.8)).
3. Blocking: similar experimental units (mice of the same litter, experiments of the same day, the same plate) are grouped into blocks and the treatments are compared within each block, removing the differences between blocks from the error.

The slogan is "block what you can, randomize what you cannot": known, controllable disturbing factors are eliminated by blocking, and unknown ones are averaged out by randomization.

### 12.7.2. Completely Randomized and Randomized Block Designs

A completely randomized design allocates all the experimental units at random to the treatments and is analyzed by one-way analysis of variance; it is the simplest, but all the differences among experimental units enter the error.

**Definition 12.7.1 (Randomized Block Design)** Divide the experimental units into $b$ blocks, each containing $t$ units (equal to the number of treatments), and within each block allocate the $t$ treatments at random to the units. This design is called a **randomized complete block design**. The model for analysis is $y_{ij} = \mu + \tau_i + \beta_j + \varepsilon_{ij}$ ($\tau_i$ the treatment effect, $\beta_j$ the block effect, no interaction assumed), the total sum of squares decomposes into treatment, block and error, and the error has $(t - 1)(b - 1)$ degrees of freedom.

The paired t test is the randomized block design with $t = 2$ (each pair is a block). When the differences between blocks are large, the randomized block design is far more efficient than the completely randomized design.

**Example 12.7.1 (Littermate Mice, Simulated)** An experiment compares the effect of a control and three diets (A, B, C) on the body weight (g) of young mice at 21 days of age, using 6 litters of 4 mice, with the 4 diets allocated at random within each litter (simulated data: between-litter standard deviation 2, within-litter standard deviation 1):

| Litter | Control | A | B | C |
|---|---|---|---|---|
| L1 | 22.1 | 24.8 | 25.2 | 28.9 |
| L2 | 15.1 | 15.5 | 16.6 | 15.7 |
| L3 | 19.8 | 21.4 | 23.3 | 22.1 |
| L4 | 19.8 | 19.7 | 20.9 | 21.9 |
| L5 | 19.6 | 19.6 | 20.9 | 21.1 |
| L6 | 21.5 | 20.3 | 21.3 | 22.1 |

Analyzed as a randomized block design, diet has $F = 5.61$ with degrees of freedom $(3, 15)$ and $p = 0.009$; litter has $F = 31.4$ with degrees of freedom $(5, 15)$. If the litters are ignored and the data analyzed as a completely randomized design, the differences among litters (sum of squares 187.3) all enter the error: diet has $F = 0.65$ with degrees of freedom $(3, 20)$ and $p = 0.59$, and nothing can be detected. By the error estimate of the block design, its efficiency relative to the completely randomized design is about 7.6: to reach the same precision, the completely randomized design would need about 7.6 times as many mice. The nonparametric Friedman test (ranking within each block) gives $\chi^2 = 12.8$, $p = 0.005$. Note that the analysis must be consistent with the design: an experiment done as a block design must be analyzed by block.

### 12.7.3. Factorial Designs

**Definition 12.7.2 (Factorial Design)** A design in which all combinations of the levels of two or more factors are treatments, and each combination has replicate observations, is called a **factorial design**. A $2 \times 2$ factorial design has 4 treatments, and a $2^k$ factorial design has $2^k$.

A factorial design has two advantages. One is efficiency: in the absence of interaction, every observation gives information on the effect of each factor at once, so a $2 \times 2$ factorial experiment answers two questions with the same sample size, equivalent to two one-factor experiments. The Physicians' Health Study tested aspirin and β-carotene simultaneously in this way ([7.7.5](/7.7.5) Example 5.2.1). The other is that interaction can be tested: only by changing two factors together in the same experiment can one discover that "the effect of one factor depends on the other"; an experiment that changes one factor at a time never sees interaction. ToothGrowth is a $3 \times 2$ factorial design. The disadvantage is that the number of treatments grows rapidly with the number of factors ($2^6 = 64$); a fractional factorial design then runs only some of the combinations, at the price that certain higher-order interactions are confounded with main effects.

### 12.7.4. Experimental Units and Pseudoreplication

**Definition 12.7.3 (Experimental Unit)** The smallest unit that receives a treatment independently is called the **experimental unit**: the treatment is allocated to it at random, and given the treatment its outcome is independent of the outcomes of the other units.

Several measurements on the same experimental unit are only repeated measurements of that one unit.

| Experiment | Experimental unit | Not the experimental unit |
|---|---|---|
| A drug is given to mice by gavage and 50 liver cells of each mouse are measured | Mouse | Cell |
| 3 culture dishes are treated and 5 fields are counted in each dish | Dish | Field |
| 4 cages each hold 5 mice, with diet allocated by cage | Cage | Mouse |
| The same RNA is sequenced 3 times | Sample | Sequencing replicate |

This distinguishes two kinds of replication: **biological replicates** ([7.9.2](/7.9.2)) are independent experimental units (different animals, patients, independently cultured cells), and the variation among them is the biological variation that the inference is meant to generalize; **technical replicates** are repeated measurements of the same experimental unit (duplicate wells, repeated loading, multiple sequencing runs of the same sample), and reflect only measurement error. If the conclusion is to be generalized to "mice" or "patients", the sample size is the number of biological replicates.

**Definition 12.7.4 (Pseudoreplication)** Treating multiple measurements within the same experimental unit (technical replicates, several cells or sites of the same individual) as independent replicates in statistical inference is called **pseudoreplication**.

The term comes from Hurlbert's (1984) criticism of ecological experiments, but the practice is equally common in cell biology and neuroscience: data with "$n = 150$ cells from 3 mice" are used in a t test with 150 as the sample size. Cells of the same mouse are correlated (they share heredity, treatment and differences in sampling), and the degree of correlation is measured by the intraclass correlation coefficient $\rho$ ([7.7.17](/7.7.17)). When $m$ cells are measured on each mouse, the variance of a group mean is $1 + (m - 1)\rho$ times what it would be with independence (the design effect): 3.7 times for $m = 10$ and $\rho = 0.3$. Treating the cells as independent samples underestimates the standard error and inflates the type I error rate accordingly.

**Example 12.7.2 (A Simulation of Pseudoreplication)** Two groups of 3 mice each, 10 cells measured in each mouse, with no true difference between the groups. Panel B below shows that, with intraclass correlation 0.1, 0.3 and 0.5, the type I error rate of a t test treating 30 + 30 cells as independent samples is 0.16, 0.33 and 0.45; a t test on the mouse means (3 + 3) keeps the error rate at about 0.05 throughout. The correct analysis: test the means of the experimental units; or use a mixed model with mouse as a random effect, which also uses the information at the cell level ([7.7.17](/7.7.17)). Measuring more cells cannot replace using more mice: the mean of each mouse becomes more precise as $m$ increases, but the variation among mice does not decrease accordingly, and power is determined mainly by the number of mice.

![Pseudoreplication (simulation): two groups of 3 mice, 10 cells measured per mouse, no true difference between groups; the cells of one mouse share a mouse effect, and the intraclass correlation (ICC) is the proportion of the total variance that is variance between mice. A: one simulated data set (ICC = 0.3), the cells clustered by mouse, horizontal lines the mean of each mouse. B: type I error rate at nominal level 0.05 (20 000 simulated experiments for each ICC): the t test treating the 30 cells per group as independent samples (orange) inflates rapidly with ICC, while the t test on the 3 mouse means per group (blue) stays at 0.05](./plots/pseudoreplication.py)

A report of an experiment should state clearly what the experimental unit is, what $n$ means ("$n = 3$ mice, 50 cells each"), how many times the experiment was independently repeated, and whether the error bars are standard deviations or standard errors and based on $n$ at which level.

### 12.7.5. Sample Size

The power of a one-way analysis of variance is determined by the effect size, the number of groups, the sample size per group and $\alpha$. The effect size is often taken as Cohen's $f = \sigma_{\text{group means}}/\sigma$ (the ratio of the standard deviation of the group means to the within-group standard deviation; $f = 0.10$, $0.25$ and $0.40$ are called small, medium and large). Under $H_1$ the F statistic has a noncentral F distribution with noncentrality parameter $\lambda = Nf^2$, and the power is the probability that it exceeds the critical value.

**Example 12.7.3** For $k = 3$ groups, $\alpha = 0.05$ and power 80%: $f = 0.25$ requires 53 experimental units per group and $f = 0.40$ requires 22 per group. For the three ToothGrowth doses $f = 1.50$, so large an effect that 3–4 animals per group suffice to detect it; but the interaction and the simple effects are smaller effects and need more animals. In actual calculations it is better to write down directly the expected group means and standard deviations (from pilot experiments or the literature) and compute the sample size for the contrast or simple effect of greatest interest ([7.7.18](/7.7.18)). The sample size of animal experiments must also follow the ethical principle of reduction in the use of animals: enough to answer the question and no more than needed.

## 12.8. Nonparametric Alternatives

When the data are clearly skewed, have outliers or are ordered grades:

| Design | Parametric method | Rank method |
|---|---|---|
| Completely randomized, $k$ groups | One-way analysis of variance | **Kruskal–Wallis test** ([7.7.8](/7.7.8)), with Dunn's test for pairwise comparisons |
| Randomized blocks | Analysis of variance for the randomized block design | Friedman test (ranking within blocks) |
| Ordered dose groups | Linear contrast | Jonckheere–Terpstra trend test |
| Any design | — | Permutation test: permute the labels within what the design allows (within blocks) |

Rank methods test whether the location of the distributions differs and do not directly give an estimate of the difference of means; there is no simple rank version of a two-way interaction. In many cases analysis of variance after a log transformation is the better choice, since it retains the estimate of effects and the test of interaction.

## 12.9. Computing in Python

```python
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multitest import multipletests

tg = pd.read_csv("toothgrowth.csv")
tg["fdose"] = tg["dose"].astype(str)                       # dose as a factor

# one-way ANOVA (Example 12.2.1) and assumption checks
m1 = smf.ols("len ~ C(fdose)", data=tg).fit()
print(sm.stats.anova_lm(m1))                               # F = 67.4, p = 9.5e-16
groups = [g["len"] for _, g in tg.groupby("fdose")]
print(stats.levene(*groups).pvalue)                        # median-centred, 0.53
print(stats.f_oneway(*groups))                             # same F from scipy

# multiple comparisons (Examples 12.3.1, 12.3.2)
print(pairwise_tukeyhsd(tg["len"], tg["fdose"]))           # HSD intervals
print(stats.dunnett(groups[1], groups[2], control=groups[0]).confidence_interval())
print(multipletests([0.005, 0.015, 0.021, 0.09], method="holm")[1])   # 0.02, 0.045, 0.045, 0.09

# linear and quadratic contrasts on log2 dose (Example 12.4.1)
mse, means = m1.scale, tg.groupby("dose")["len"].mean().to_numpy()
for c in ([-1, 0, 1], [1, -2, 1]):
    c = np.array(c)
    L, se = c @ means, np.sqrt(mse * (c ** 2 / 20).sum())
    print(L, L / se, 2 * stats.t.sf(abs(L / se), m1.df_resid))

# two-way ANOVA with interaction (Example 12.5.1)
m2 = smf.ols("len ~ C(supp) * C(fdose)", data=tg).fit()
print(sm.stats.anova_lm(m2, typ=2))                        # interaction F = 4.11, p = 0.022

# ANCOVA (Example 12.6.1)
bw = pd.read_csv("birthwt.csv")
bw["race"] = bw["race"].map({1: "white", 2: "black", 3: "other"})
m3 = smf.ols('bwt ~ C(race, Treatment("white")) + smoke + lwt', data=bw).fit()
print(m3.params, sm.stats.anova_lm(m3, typ=2))
grid = pd.DataFrame({"race": ["white", "black", "other"], "smoke": bw.smoke.mean(), "lwt": bw.lwt.mean()})
print(m3.predict(grid))                                    # adjusted means 3154, 2650, 2759

# power of a one-way ANOVA (Example 12.7.3); nobs is the total over all groups
from statsmodels.stats.power import FTestAnovaPower
print(FTestAnovaPower().solve_power(effect_size=0.25, alpha=0.05, power=0.8, k_groups=3) / 3)   # about 53
```

## Summary

- Do not do many t tests to compare several groups: for pairwise comparisons among 5 groups the family-wise error rate is about 0.29 (upper bound 0.40 for independent tests). One-way analysis of variance (Formula 12.2.1) divides the total sum of squares into between-group and within-group parts, and $F = \mathrm{MS}_{\text{between}}/\mathrm{MS}_{\text{within}}$; for the ToothGrowth dose $F = 67.4$ (Example 12.2.1). Assumptions: independence (guaranteed by design), approximate normality, equal variances (Levene's test; Welch's analysis of variance or a transformation when they are unequal).
- Multiple comparisons: Holm (Definition 12.3.1) is always better than Bonferroni (Example 12.3.1); use Tukey for all pairwise comparisons, Dunnett for comparisons with a control (Definition 12.3.2), Scheffé for post hoc arbitrary contrasts, and FDR for thousands of tests (Example 12.3.2 and the table of choices).
- Contrasts (Definition 12.4.1) divide the between-group sum of squares into meaningful single-degree-of-freedom comparisons; the linear trend in log dose explains 99% of the dose effect in ToothGrowth (Example 12.4.1).
- Two-way analysis of variance: main effects and interaction (Definition 12.5.1); the ToothGrowth interaction has $p = 0.022$, with orange juice better at low and medium doses and the same as ascorbic acid at 2 mg/d (Example 12.5.1). When an interaction is present report simple effects and do not interpret main effects; interaction depends on the scale; balanced designs are best.
- Analysis of covariance (Definition 12.6.1) is regression with a covariate and gives adjusted means; in birthwt the effect of smoking increases from 284 g to 400 g after adjustment for race (Example 12.6.1): confounding can also mask an association.
- Experimental design: replication, randomization, blocking; the randomized block design (Definition 12.7.1) is far more efficient when the differences among blocks are large (about 7.6 times in the littermate-mouse simulation, Example 12.7.1); a factorial design (Definition 12.7.2) studies several factors at once and can reveal interactions.
- The experimental unit determines $n$: biological replicates are independent experimental units and technical replicates are not; pseudoreplication (Definition 12.7.4), treating cells as mice, inflates the type I error rate from 0.05 to 0.3–0.45 (Example 12.7.2). Sample size is determined by the effect size and the number of experimental units (Example 12.7.3); rank methods and permutation tests are the nonparametric alternatives (Section 12.8).

## Questions

1. A study compares the growth rate of a bacterial strain in 6 culture media. The authors did all 15 pairwise t tests, reported that 2 pairs had $p < 0.05$, and recommended a medium on this basis. (a) If the media in fact do not differ, what is the probability that at least one of 15 independent tests has $p < 0.05$? (b) How should the data be analyzed?

   **Answer** (a) $1 - 0.95^{15} = 0.54$; the 15 comparisons are not independent, so the actual probability is somewhat lower (about 0.35 for $k = 6$ in the simulation of Section 12.1), but far greater than 0.05, and the two "significant" comparisons are quite possibly due to chance. (b) First test by one-way analysis of variance whether the 6 media differ; then do all pairwise comparisons by Tukey's method (giving simultaneous confidence intervals) or, if there is a standard medium to serve as the control, compare the other 5 with it by Dunnett's test; report effect sizes and not merely asterisks. If there were one or two specific hypotheses before the comparison, they should have been stated before the experiment.

2. Complete the one-way analysis-of-variance table and do the F test from the following summary data: three groups of 8 rats each, the mean serum activity of an enzyme being 52, 58 and 61, and the standard deviations 6, 7 and 5.

   **Answer** The overall mean is $\bar y = (52 + 58 + 61)/3 = 57$. The between-group sum of squares is $8[(52 - 57)^2 + (58 - 57)^2 + (61 - 57)^2] = 8(25 + 1 + 16) = 336$ with 2 degrees of freedom and mean square 168. The within-group sum of squares is $7(36 + 49 + 25) = 770$ with 21 degrees of freedom and mean square 36.67. $F = 168/36.67 = 4.58$; the 0.05 critical value of $F_{2,21}$ is 3.47, and $p \approx 0.022$: the three group means are not all equal. Tukey's HSD $= q_{3,21,0.05}\sqrt{36.67/8} = 3.565 \times 2.141 = 7.63$: only the difference between group 1 and group 3 (9) exceeds it, and the differences between groups 1 and 2 (6) and between groups 2 and 3 (3) are not significant.

3. In analyzing the six cells of ToothGrowth, the investigators first test the interaction ($p = 0.022$) and then say "since the interaction is significant, the main effects lose their meaning, and we do not report the effect of dose". Is this right?

   **Answer** Partly. A significant interaction means that the main effect of delivery method (the average difference over the three doses) cannot summarize the effect of delivery method, and the simple effects at each dose (the table of Example 12.5.1) should be reported instead. But the effect of dose is very large and in the same direction under both delivery methods (both lines rise steeply with dose, and the interaction only changes the amount of rise), so the main effect of dose still has a clear meaning: whichever delivery method is used, increasing the dose increases tooth growth. The right course is to look at the interaction plot, decide whether the interaction is "quantitative" or "qualitative", and report the cell means and the simple effects of interest, rather than mechanically deciding what to keep.

4. Use Definition 12.4.1 to verify that, in 3 groups of equal sample size, the linear contrast $(-1, 0, 1)$ and the quadratic contrast $(1, -2, 1)$ are orthogonal, and explain why their sums of squares add up to the between-group sum of squares.

   **Answer** $\sum c_i c_i' = (-1)(1) + 0(-2) + (1)(1) = 0$, so the two are orthogonal. The vector of deviations of the group means $(\bar y_1 - \bar y, \bar y_2 - \bar y, \bar y_3 - \bar y)$ lies in the two-dimensional subspace orthogonal to $(1, 1, 1)$ (the three deviations sum to 0), and $(-1, 0, 1)$ and $(1, -2, 1)$ form an orthogonal basis of this subspace. The between-group sum of squares $n\sum(\bar y_i - \bar y)^2$ is $n$ times the squared length of the deviation vector, which, decomposed along an orthogonal basis, equals the sum of the squares of the two projections, and the sum of squares of each projection is exactly the sum of squares of the contrast $\hat L^2/(\sum c_i^2/n)$. In Example 12.4.1, $2401.0 + 25.5 = 2426.4$.

5. A toxicology study randomly divides 40 rats into a vehicle control and 3 dose groups (10 each); the main question is "which dose groups differ from the control?". Should Tukey or Dunnett be used? What if we also want to know whether the effect increases monotonically with dose?

   **Answer** The main question involves only 3 comparisons with the control, so use Dunnett's test: it adjusts for the multiplicity of only 3 comparisons and is more powerful than Tukey's, which adjusts for all 6 pairs. For the trend of the dose response, specify a linear contrast beforehand (orthogonal polynomial coefficients for equally spaced doses, otherwise coefficients determined from the actual doses or their logarithms), or use methods designed for monotone dose response such as Williams' test or the Jonckheere–Terpstra test; better still, treat dose as a continuous variable, fit a dose-response model and estimate quantities such as the $\mathrm{EC}_{50}$ or a benchmark dose ([7.7.11](/7.7.11)), instead of answering only "which dose is significant".

6. An experiment compares the effect of two treatments on the migration speed of cultured cells: 2 culture dishes per treatment, 40 cells tracked in each dish, and the authors report $n = 80$ against $n = 80$, $p = 10^{-6}$. (a) What is the experimental unit? (b) If the intraclass correlation of cell speeds within a dish is 0.2, what is the design effect? About what is the effective sample size? (c) How would you reanalyze, and how would you suggest improving the design?

   **Answer** (a) The treatment is applied to the dish, so the experimental unit is the dish, and each treatment has only 2 experimental units. (b) The design effect is $1 + (40 - 1) \times 0.2 = 8.8$; the effective sample size is about $80/8.8 \approx 9$ cell equivalents, but the more fundamental problem is that each group has only 2 dishes, and the variation among dishes (culture conditions, cell density) can be estimated only from 2 dishes. (c) Analyze the dish means: 2 numbers per group, 2 degrees of freedom, almost no power, and the original $p = 10^{-6}$ is a product of pseudoreplication; a mixed model with dish as a random effect can also be used, but the conclusion is still limited by the 4 dishes. Improvements: increase the number of independent dishes (say 6–8 per group, done independently over several days), allocate the treatments at random within each experimental day (day as block), and the number of cells tracked per dish can be reduced; state in the report that $n$ is the number of dishes.

7. Using the idea of Example 12.7.1, explain why the paired t test can be regarded as a special case of the randomized block design. What is the "block" here, and why is the treatment × block interaction treated as error?

   **Answer** In a paired design each pair (two measurements on the same individual, two animals of the same litter) is a block, containing 2 units and 2 treatments, with treatments allocated at random within the block (or self-control). In the randomized block model $y_{ij} = \mu + \tau_i + \beta_j + \varepsilon_{ij}$, the F test for the treatment effect (with $1$ and $b - 1$ degrees of freedom) equals the square of the paired t statistic: the difference $d_j = y_{2j} - y_{1j} = (\tau_2 - \tau_1) + (\varepsilon_{2j} - \varepsilon_{1j})$ eliminates the block effect $\beta_j$. Each block has only one observation per treatment, so the treatment × block interaction cannot be separated from error; treating it as error amounts to assuming that the treatment effect is the same in all blocks and that variation among blocks is merely random error, which is exactly what is meant by the paired t test taking the variance of the differences as the error.

8. In Example 12.6.1 the adjusted effect of smoking ($-400$ g) is larger than the unadjusted one ($-284$ g). Another investigator says: "Adjustment should make the effect smaller; that it becomes larger shows something is wrong with the model." How would you answer?

   **Answer** The direction of adjustment depends on the direction of the confounding. If a confounder is positively related to the exposure and also positively related to the outcome (age with smoking, age with FEV), then without adjustment the exposure looks "better" and after adjustment the effect moves in the unfavorable direction; in birthwt, white mothers have the highest proportion who smoke (52/96) and the babies of white mothers are on average the heaviest, so race makes the babies of smokers "look" heavier, masking the harm of smoking, and a larger effect after adjustment is reasonable (negative confounding). After adjustment the effect may become smaller, larger or even change sign, depending on the directions of the relationships of the confounder with exposure and outcome; whether a variable should be adjusted for is decided by the causal structure ([7.7.15](/7.7.15)), not by the direction of change of the effect after adjustment.

9. (Design question) You want to study whether a transgenic mouse is more sensitive to obesity induced by a high-fat diet. Wild-type and transgenic mice are available, with two diets (standard, high-fat), and the endpoint is weight gain at 12 weeks. Design the experiment and write the analysis plan.

   **Answer** Design: a $2 \times 2$ factorial design (genotype × diet); the research question is precisely the interaction ("is the response of transgenic mice to a high-fat diet greater?"). Experimental unit: if the mice are housed singly the unit is the mouse; if group-housed with diet allocated by cage, the unit is the cage, and one should house singly where possible or increase the number of cages. Allocation: genotype cannot be randomized, so use wild-type and transgenic littermates (offspring of heterozygote crosses) as controls, with litter as the block and diets allocated at random within litters; restrict to one sex (or do both sexes and treat sex as a factor); blind the experimenter to genotype. Sample size: estimate the standard deviation of weight gain from a pilot experiment and compute the sample size for the interaction (the difference between the high-fat effects in the two genotypes) as the main contrast: the standard error of an interaction is twice that of a main effect, so the sample size needed is about 4 times that for testing a main effect. Analysis: two-way analysis of variance (or a mixed model with litter as a random effect), the main test being the genotype × diet interaction, and report the four cell means and the simple effects of the high-fat diet in the two genotypes with intervals; do an analysis of covariance with starting weight as covariate to improve precision; if weight gain is right-skewed, consider the log scale and state the scale on which the interaction is defined.

10. A researcher measures the effect of 4 treatments on cell proliferation on a 96-well plate, with 24 wells per treatment placed, in order of treatment, in columns 1–3, 4–6, 7–9 and 10–12, and obtains $p < 0.001$ by one-way analysis of variance. Point out two problems with the design and give an improved plan.

    **Answer** (1) Treatment is completely confounded with position on the plate: a 96-well plate has edge effects (wells on the outer ring evaporate more and are at a different temperature) and gradients along columns (order of loading, time differences in plate reading), and when treatments are allocated by column, any position effect will be taken for a treatment effect. (2) The 24 wells are technical replicates on the same plate and from the same seeding of cells, not independent biological replicates; $p < 0.001$ shows only that the 4 sets of wells on this plate differ and cannot be generalized to "the treatment changes cell proliferation". Improvement: randomize the positions of the treatments within the plate (or use a Latin-square arrangement) and avoid or do not use the outermost ring of wells; repeat the entire experiment independently at least 3 times on different days with different passages of cells, with each experiment (or each plate) as a block; analyze using the mean of the wells for each treatment in each experiment as the unit, by analysis of variance for a randomized block design (or a mixed model with experiment as a random effect), the degrees of freedom of the treatment effect being determined by the number of independent experiments.
