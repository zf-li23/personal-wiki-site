---
title: Hypothesis Testing for Categorical Data
description: Comparing two proportions (normal approximation, the chi-square test for 2×2 tables, Yates's correction and the condition on expected frequencies); Fisher's exact test; McNemar's test for paired proportions; sample size for comparing two proportions; tests of independence and homogeneity for R×C tables and the likelihood-ratio chi-square; the Cochran–Armitage trend test for ordered categories; goodness-of-fit tests; measures of association and agreement (phi, Cramér's V, Cohen's kappa). Examples are maternal smoking, hypertension and low birth weight, the Physicians' Health Study, breast cancer and age at first birth, and reaction times under sleep deprivation.
source_hash: 1ba39e2bb830
---

In the previous chapters the outcome variables were continuous: blood pressure, birth weight, FEV. In medical research the commoner outcomes are categorical: whether a person is ill, whether they die, whether the birth weight is low, whether a test is positive or negative, which blood group they have. Such data are summarized as counts in the categories, and what is compared is proportions. In [7.7.6](/7.7.6) the one-sample binomial test compared the proportion of low-birth-weight infants among smoking mothers with a "known" reference value of 0.252; it was pointed out there that 0.252 was itself estimated from 115 nonsmoking mothers and that the correct approach is to treat the two groups alike. This chapter starts from that two-proportion comparison: the normal approximation and the chi-square test for a 2×2 **contingency table** are the same test, and when the expected frequencies are too small we turn to Fisher's exact test; two dichotomous measurements on the same individuals require McNemar's test. We then extend to tables with several rows and columns, trend tests for ordered categories and goodness-of-fit tests, and finally discuss measures of the strength of association and of the agreement between raters. The limiting distribution of the chi-square statistic and the derivation of the test of independence are in [3.2.6](/3.2.6#sec-6.3); here we treat use and conditions. Measures of effect (the risk difference, the relative risk and the **odds ratio**) appear here only as companions of the test; their meaning in study design is the subject of [7.7.13](/7.7.13), and methods that adjust for several variables at once are the logistic regression of [7.7.14](/7.7.14).

## 9.1. Comparing Two Proportions

### 9.1.1. The Normal Approximation

Suppose two independent groups have $n_1$ and $n_2$ individuals with $x_1$ and $x_2$ events, and sample proportions $\hat p_1 = x_1/n_1$ and $\hat p_2 = x_2/n_2$. Under $H_0\colon p_1 = p_2$ the common proportion is estimated by the pooled value $\hat p = (x_1 + x_2)/(n_1 + n_2)$.

**Formula 9.1.1 (z Test for Two Proportions)** The statistic

$$
z = \frac{\hat p_1 - \hat p_2}{\sqrt{\hat p(1 - \hat p)\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}}
$$
is approximately $\mathcal{N}(0, 1)$ under $H_0$ (when $n\hat p\hat q$ is at least about 5 in each group). An approximate 95% confidence interval for the difference $p_1 - p_2$ is $\hat p_1 - \hat p_2 \pm 1.96\sqrt{\hat p_1\hat q_1/n_1 + \hat p_2\hat q_2/n_2}$, where $\hat q = 1 - \hat p$.

The test uses the pooled proportion (the standard error under $H_0$), whereas the confidence interval uses the separate proportions (without assuming $H_0$), for the same reason as in [7.7.6](/7.7.6) Formula 6.6.1.

**Example 9.1.1 (Maternal Smoking and Low Birth Weight)** In birthwt, 30 of the 74 smoking mothers had a low-birth-weight infant ($\hat p_1 = 0.405$) and 29 of the 115 nonsmoking mothers ($\hat p_2 = 0.252$); the pooled proportion is $\hat p = 59/189 = 0.312$.

$$
z = \frac{0.405 - 0.252}{\sqrt{0.312 \times 0.688 \times (1/74 + 1/115)}} = \frac{0.153}{0.0691} = 2.22, \qquad p = 0.026.
$$
The 95% interval for the difference 0.153 is $(0.016, 0.290)$. [7.7.6](/7.7.6) Example 6.6.1 treated 0.252 as a known constant and obtained $p = 0.0012$ (normal approximation); since both groups are subject to sampling error, the evidence is in fact weaker by more than an order of magnitude.

**Example 9.1.2 (The Physicians' Health Study)** In the aspirin group, 139 of 11 037 men had a myocardial infarction (1.26%), and in the placebo group 239 of 11 034 (2.17%; [7.7.3](/7.7.3) Example 3.1.4). Then $z = -5.19$, $p = 2 \times 10^{-7}$; the risk difference is $-0.91\%$ with 95% interval $(-1.25\%, -0.56\%)$. Although the event rate is low, each group has over 10 000 men and over 100 events, so the normal approximation is entirely reliable.

### 9.1.2. The 2×2 Table and the Chi-Square Test

The same data can be arranged in a 2×2 table:

| | Low birth weight | Normal | Total |
|---|---|---|---|
| Smoker | 30 | 44 | 74 |
| Nonsmoker | 29 | 86 | 115 |
| Total | 59 | 130 | 189 |

If smoking and low birth weight were unrelated, the *expected frequency* of each cell would be (row total × column total) / grand total: for smokers with low birth weight, $74 \times 59/189 = 23.1$, and for the other three cells 50.9, 35.9 and 79.1. The difference between observed and expected frequencies is summarized by Pearson's chi-square statistic.

**Formula 9.1.2 (Chi-Square Test for a 2×2 Table)** Let the four cells of a 2×2 table be $a, b$ (first row) and $c, d$ (second row), with total $n$, and let $O_i$ and $E_i$ be the observed and expected frequencies. The statistic

$$
X^2 = \sum_{i=1}^4 \frac{(O_i - E_i)^2}{E_i} = \frac{n(ad - bc)^2}{(a+b)(c+d)(a+c)(b+d)}
$$
is approximately $\chi^2_1$ under $H_0$ (the row and column variables are independent, or the proportions in the two rows are equal). The rejection region lies on the right only: $X^2 > \chi^2_{1,\alpha}$ (3.84 for $\alpha = 0.05$).

In Example 9.1.1, $X^2 = 189 \times (30 \times 86 - 44 \times 29)^2/(74 \times 115 \times 59 \times 130) = 4.92$ and $p = 0.026$, exactly $z^2 = 2.22^2$. This is no coincidence: for a 2×2 table the chi-square test and the two-sided z test of Formula 9.1.1 are the same test, since $\chi^2_1$ is the square of a standard normal variable ([7.7.4](/7.7.4), Section 4.8). The advantage of the z test is that it permits one-sided tests and directly gives an interval for the difference.

A 2×2 table can arise from different sampling schemes: the sizes of the two groups may be fixed (as in a randomized trial comparing the event proportions of two groups; the **test of homogeneity**), only the total may be fixed (a cross-sectional survey testing whether two variables are independent; the **test of independence**), or the numbers of cases and controls may be fixed (a case-control study comparing the proportions exposed in the two groups). The test statistic and its approximate null distribution are identical in the three situations ([3.2.6](/3.2.6#sec-6.4)); what differs is the kind of effect that can be estimated ([7.7.13](/7.7.13)).

**Example 9.1.3 (Breast Cancer and Age at First Birth)** An international case-control study (MacMahon et al. 1970) surveyed women who had had at least one child: of 3220 breast cancer patients, 683 (21.2%) were 30 or older at first birth, as against 1498 (14.6%) of 10 245 controls. The numbers of cases and controls are fixed here, and what is compared is the proportion exposed (late childbearing). $X^2 = 78.4$ and $p = 9 \times 10^{-19}$; the odds ratio is $683 \times 8747/(2537 \times 1498) = 1.57$ with 95% interval $(1.42, 1.74)$: late age at first birth is associated with higher breast cancer risk.

:::

![Mosaic plots of two 2×2 tables from birthwt (189 deliveries, Baystate Medical Center 1986; Hosmer and Lemeshow). The width of each column is proportional to the size of the exposure group, the height of the shaded part is the proportion with low birth weight (< 2500 g), and the dashed line is the overall proportion 59/189. A: maternal smoking (30 of 74 smokers, 29 of 115 nonsmokers). B: history of hypertension (7 of 12 with, 52 of 177 without): the proportions differ greatly, but the exposed group is very small](./plots/mosaic.py)

### 9.1.3. Expected Frequencies and Yates's Correction

The chi-square distribution is an approximation: the observed frequencies are discrete integers, and $X^2$ can take only finitely many values. The classical condition for the approximation is that all expected frequencies in the 2×2 table are at least 5 (expected, not observed, frequencies).

**Definition 9.1.1 (Yates's Correction)** In the chi-square statistic of a 2×2 table, subtract 1/2 from each $\lvert O_i - E_i\rvert$ before squaring:

$$
X^2_{\mathrm{Y}} = \sum_{i=1}^4 \frac{(\lvert O_i - E_i\rvert - 1/2)^2}{E_i} = \frac{n(\lvert ad - bc\rvert - n/2)^2}{(a+b)(c+d)(a+c)(b+d)}.
$$
This is called the chi-square statistic with **Yates's correction for continuity**.

It is the form taken in the 2×2 table by the **continuity correction** of the normal approximation to the binomial distribution ([7.7.4](/7.7.4), Section 4.5). In Example 9.1.1, $X^2_{\mathrm{Y}} = 4.24$ and $p = 0.040$; in Example 9.1.3, $X^2_{\mathrm{Y}} = 77.9$, almost the same as the uncorrected 78.4: with large samples the correction is immaterial.

Whether to apply the correction has long been debated. Yates's correction brings the p-value close to that of Fisher's exact test (Section 9.2) and is therefore conservative: the actual type I error rate is often far below the nominal level (the figure in the next section). The current recommendation is to report the uncorrected chi-square test when all expected frequencies are large enough (R's `chisq.test` corrects by default, and so does `scipy.stats.chi2_contingency`, for which one writes `correction=False`), and when the expected frequencies are small to use Fisher's exact test directly rather than the corrected chi-square.

## 9.2. Fisher's Exact Test

### 9.2.1. The Hypergeometric Distribution

When the expected frequencies are too small, we avoid approximation and compute exact probabilities. Fisher's idea is to regard both the row totals and the column totals of the 2×2 table as fixed; once one cell (say $a$) is known, the other three are determined.

**Definition 9.2.1 (Fisher's Exact Test)** Let the row totals of a 2×2 table be $n_1 = a + b$ and $n_2 = c + d$, the column totals $m_1 = a + c$ and $m_2 = b + d$, and the grand total $n$. Under $H_0$ (rows and columns independent) and given all the marginal totals, $a$ has the **hypergeometric distribution**

$$
\mathbb{P}(a) = \frac{\dbinom{n_1}{a}\dbinom{n_2}{m_1 - a}}{\dbinom{n}{m_1}}.
$$
The test whose p-value is computed from this distribution is called **Fisher's exact test**. The two-sided p-value is usually taken as the sum of the probabilities of all tables whose probability does not exceed that of the observed table.

The meaning of the hypergeometric distribution is this: $m_1$ of the $n$ individuals have the event; if the event is unrelated to group, these $m_1$ events fall at random into the two groups, and $\mathbb{P}(a)$ is the probability that exactly $a$ of them fall in the first. This is the same idea as the permutation test of [7.7.8](/7.7.8): Fisher's exact test is the permutation test with $a$ as the statistic.

**Example 9.2.1 (History of Hypertension and Low Birth Weight)** In birthwt only 12 mothers had a history of hypertension, of whom 7 had a low-birth-weight infant (58%); among the 177 without, 52 did (29%). The expected frequency of the cell "hypertension and low birth weight" is $12 \times 59/189 = 3.75 < 5$, so the chi-square approximation is unreliable. With the marginal totals fixed, the number of low-birth-weight infants among the 12 hypertensive mothers has a hypergeometric distribution (figure below); the outcomes with probability no larger than $\mathbb{P}(a = 7) = 0.032$ are $a \ge 7$ and $a = 0$, giving a two-sided $p = 0.052$. The conclusions of the three methods fluctuate around 0.05:

| Method | $p$ |
|---|---|
| Pearson chi-square (uncorrected) | 0.036 |
| Chi-square with Yates's correction | 0.076 |
| Fisher's exact test | 0.052 |

The correct course here is to report Fisher's exact test and to state that 7 of the 12 hypertensive mothers had a low-birth-weight infant (odds ratio 3.4); the evidence suggests an association but is uncertain because the exposed group is so small. More important, "which side of 0.05" should not decide the conclusion ([7.7.6](/7.7.6), Section 6.8).

![Fisher's exact test for history of hypertension and low birth weight in birthwt (7 of the 12 mothers with hypertension had a low-birth-weight infant; 59 of the 189 mothers in all). With the marginal totals fixed, under H0 the number of low-birth-weight infants among the 12 hypertensive mothers has a hypergeometric distribution (bars; expectation 3.75). The two-sided p-value is the sum of the probabilities of all tables whose probability does not exceed that of the observed table (shaded), p = 0.052; the uncorrected Pearson chi-square gives 0.036 and, with Yates's correction, 0.076](./plots/fisher-null.py)

### 9.2.2. Exact Tests Are Conservative

Fisher's exact test conditions on the marginal totals and its null distribution is discrete, so its actual type I error rate never exceeds $\alpha$ and is often far below it. The figure below computes exactly the actual type I error rates of three tests for groups of 8–60 with identical true proportions in the two groups: Fisher's test and the chi-square with Yates's correction almost coincide, and with small expected frequencies the actual level is less than half the nominal level; the uncorrected chi-square fluctuates around 0.05 and is already quite accurate when the expected frequencies are somewhat larger. Conservatism means a loss of power. One compromise is to report the mid-p value (counting only half the probability of the observed table itself), whose actual level is closer to the nominal one. When the expected frequencies are large enough, the differences among the three are negligible.

![Actual type I error rates of three tests for 2×2 tables with small expected frequencies. Both groups have sample size n and the same true proportion (A: p = 0.1; B: p = 0.3); the two-sided nominal level is α = 0.05, and the rejection probability is summed exactly over all possible binomial outcomes of the two groups. The uncorrected Pearson chi-square is close to 0.05 once the expected frequencies are moderate, sometimes slightly above (0.059 for p = 0.1, n = 40); Yates's correction and Fisher's exact test are both conservative, with actual levels often less than half the nominal level. Exact computation](./plots/chisq-size.py)

## 9.3. Paired Proportions: McNemar's Test

When the same individuals are measured twice with a dichotomous outcome (before and after treatment, two tests, two raters), or when cases and controls are matched one to one, the two proportions are not independent and none of the preceding methods applies.

Arrange the $n$ pairs in a different kind of 2×2 table, in which each cell counts pairs:

| | Second $+$ | Second $-$ |
|---|---|---|
| First $+$ | $a$ (concordant) | $b$ (discordant) |
| First $-$ | $c$ (discordant) | $d$ (concordant) |

The proportions positive on the two occasions are $(a + b)/n$ and $(a + c)/n$, and their difference $(b - c)/n$ depends only on the discordant pairs. Concordant pairs (positive both times or negative both times) give no information about the difference between the two occasions. Under $H_0$ (the two positive proportions are equal), each discordant pair is equally likely to belong to $b$ or to $c$, so $b \sim \mathrm{Bin}(b + c, 1/2)$; this is exactly the sign test applied to the discordant pairs ([7.7.8](/7.7.8), Section 8.2).

**Formula 9.3.1 (McNemar's Test)** Let $n_D = b + c$ be the number of discordant pairs. The exact test computes the p-value from $b \sim \mathrm{Bin}(n_D, 1/2)$; for $n_D \ge 20$ or so the approximation

$$
X^2 = \frac{(\lvert b - c\rvert - 1)^2}{b + c} \overset{H_0}{\approx} \chi^2_1
$$
can be used (the $-1$ is a continuity correction).

This is **McNemar's test** ([4.6.7](/4.6.7) uses it to compare the errors of two classifiers on the same test set).

**Example 9.3.1 (Sleep Deprivation and Reaction Time)** The sleepstudy data (Belenky et al. 2003) record the mean reaction times of 18 subjects over several days of sleep restriction ([7.7.1](/7.7.1)). Taking 300 ms as the threshold for "slow reaction", compare day 0 with day 9: 2 subjects were slow on both days, 0 only on day 0, 12 only on day 9, and 4 on neither. The proportion slow rises from $2/18 = 11\%$ to $14/18 = 78\%$. All 12 discordant pairs go in the same direction, and the exact two-sided $p = 2 \times 0.5^{12} = 0.0005$; the approximation gives $X^2 = (12 - 1)^2/12 = 10.1$, $p = 0.0015$ ($n_D = 12$ is small, and the exact test should be used). Treating the two days wrongly as two independent samples in a chi-square test would ignore the correlation between the two days within a subject. Dichotomizing a continuous reaction time loses information, and the proper analysis of these data is the linear mixed model of [7.7.17](/7.7.17); here the data merely illustrate the structure of paired dichotomous data.

:::

Typical uses of McNemar's test: two diagnostic methods applied to the same patients (only patients are used to compare sensitivities, only non-patients to compare specificities); the exposures of cases and their matched controls in a matched case-control study ([7.7.13](/7.7.13)); a state in the same people before and after an intervention.

## 9.4. Sample Size for Comparing Two Proportions

**Formula 9.4.1 (Sample Size for Two Proportions)** The sample size per group needed by a two-sided test at level $\alpha$ to detect a difference between proportions $p_1$ and $p_2$ with power $1 - \beta$ is

$$
n = \frac{\left[z_{\alpha/2}\sqrt{2\bar p\bar q} + z_\beta\sqrt{p_1 q_1 + p_2 q_2}\right]^2}{(p_1 - p_2)^2},
$$
where $\bar p = (p_1 + p_2)/2$, $\bar q = 1 - \bar p$ and $q_j = 1 - p_j$.

As with the sample size formula for means ([7.7.7](/7.7.7) Formula 7.6.1), the number required is inversely proportional to the square of the difference; the difference is that the variance of a binomial is determined by the proportion itself, so $\sigma$ need not be estimated separately.

**Example 9.4.1** (a) If the true proportions of low-birth-weight infants among nonsmoking and smoking mothers are 0.25 and 0.40, a two-sided $\alpha = 0.05$ and 80% power require 152 per group, and 90% power requires 203. The two birthwt groups have only 115 and 74, and for so large a difference the power is only about 0.59; the $p = 0.026$ of Example 9.1.1 therefore has some element of luck. (b) The number required increases sharply when the event is rare: to detect a fall in the cumulative incidence of myocardial infarction from 2.2% to 1.65% (a 25% relative reduction), about 9800 per group are needed. This is why the Physicians' Health Study enrolled 11 000 per group ([7.7.18](/7.7.18)).

## 9.5. R×C Contingency Tables

### 9.5.1. The Chi-Square Test

When one variable has $R$ categories and the other $C$, the data form an $R \times C$ contingency table, and the expected frequency of cell $(i, j)$ is still $E_{ij} = (\text{row } i \text{ total})(\text{column } j \text{ total})/n$.

**Formula 9.5.1 (Chi-Square Test for an R×C Table)** The statistic

$$
X^2 = \sum_{i=1}^R \sum_{j=1}^C \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
$$
is approximately $\chi^2_{(R-1)(C-1)}$ under $H_0$ (rows and columns independent, or all rows having the same column distribution). The likelihood-ratio chi-square statistic

$$
G^2 = 2\sum_{i,j} O_{ij}\ln\frac{O_{ij}}{E_{ij}}
$$
has the same limiting distribution (the **likelihood ratio test**, [3.2.5](/3.2.5#sec-5.3)), and in large samples the two values are very close.

The degrees of freedom $(R - 1)(C - 1)$ arise because, given the marginal totals, only $(R-1)(C-1)$ cells can take values freely, the rest being determined by the totals. The empirical condition for the approximation is that no more than 20% of the cells have expected frequency below 5 and none below 1; otherwise merge categories of similar meaning, or use the generalization of Fisher's exact test (software can compute exact or Monte Carlo p-values for $R \times C$ tables). No continuity correction is applied to $R \times C$ tables.

**Example 9.5.1 (Race and Low Birth Weight)** In birthwt the proportions of low-birth-weight infants among white, black and other-race mothers are 23/96 (24%), 11/26 (42%) and 25/67 (37%). All expected frequencies exceed 8, $X^2 = 5.00$ with 2 degrees of freedom, and $p = 0.082$ ($G^2 = 5.01$). There is no significant difference at the 0.05 level, but the proportions for black and other-race mothers are nearly half as high again, and the sample is too small to confirm this.

**Example 9.5.2 (Race and Smoking)** Among the same mothers the proportions who smoked were 52/96 (54%) for white, 10/26 (38%) for black and 12/67 (18%) for other-race mothers. $X^2 = 21.8$ with 2 degrees of freedom, $p = 2 \times 10^{-5}$. Smoking is closely related to race, and race is in turn related to low birth weight (Example 9.5.1, in the opposite direction: the white mothers, who smoke most, have the lowest proportion of low-birth-weight infants). The crude association between smoking and low birth weight (Example 9.1.1) may therefore be distorted by race, and requires stratification by race or adjustment in a regression ([7.7.13](/7.7.13), [7.7.14](/7.7.14)).

### 9.5.2. After a Significant Result

The chi-square test for an $R \times C$ table is global: "not independent" does not say which cells are responsible. Examine the standardized residuals $(O_{ij} - E_{ij})/\sqrt{E_{ij}}$ of the cells (cells with absolute value above about 2 deviate considerably), or split the table into meaningful 2×2 subtables with a multiple-comparison correction. If one variable is ordered, the global test wastes the information in the ordering, and the trend test of the next section should be used.

## 9.6. Trend Tests for Ordered Categories

### 9.6.1. The Cochran–Armitage Test

When the exposure is divided into ordered levels (dose, age group, severity grade), the research question is usually "does the proportion with the event change monotonically with exposure level?". The global chi-square test for a $2 \times C$ table responds to any difference but has little power against a monotone trend; concentrating the power on the single direction of trend gives the trend test.

**Definition 9.6.1 (Cochran–Armitage Trend Test)** Let the exposure have $C$ ordered levels with scores $s_1 < s_2 < \dots < s_C$; level $j$ has $n_j$ individuals, of whom $x_j$ have the event; $N = \sum n_j$ and $\bar p = \sum x_j/N$. The **Cochran–Armitage trend test** uses the statistic

$$
X^2_{\mathrm{trend}} = \frac{\left[\sum_j x_j s_j - \bar p\sum_j n_j s_j\right]^2}{\bar p(1 - \bar p)\left[\sum_j n_j s_j^2 - \left(\sum_j n_j s_j\right)^2/N\right]},
$$
which is approximately $\chi^2_1$ under $H_0$ (the same event proportion at every level).

$X^2_{\mathrm{trend}}$ is equivalent to the test of the slope in a linear regression with the scores as the independent variable and the event indicator as the dependent variable. The global chi-square decomposes into a trend part (1 degree of freedom) and a part for deviation from linearity ($C - 2$ degrees of freedom): $X^2 = X^2_{\mathrm{trend}} + X^2_{\mathrm{dev}}$. The scores are usually taken as $1, 2, \dots, C$ or as the median exposure of each group; the conclusion is not very sensitive to any reasonable choice of scores.

**Example 9.6.1 (Dose Response for Age at First Birth)** The study of Example 9.1.3 divided age at first birth into five groups:

| Age at first birth / years | < 20 | 20–24 | 25–29 | 30–34 | ≥ 35 |
|---|---|---|---|---|---|
| Cases | 320 | 1206 | 1011 | 463 | 220 |
| Controls | 1422 | 4432 | 2893 | 1092 | 406 |
| Proportion cases | 0.184 | 0.214 | 0.259 | 0.298 | 0.351 |

The global $2 \times 5$ chi-square is $X^2 = 130.3$ with 4 degrees of freedom. With scores 1–5, the trend chi-square is $X^2_{\mathrm{trend}} = 129.0$ with 1 degree of freedom, $p = 7 \times 10^{-30}$; the part for deviation from linearity is $130.3 - 129.0 = 1.3$ with 3 degrees of freedom, $p = 0.72$. Almost all of the between-group difference is explained by a monotone linear trend: for each later level of age at first birth the proportion of cases rises by about 4 percentage points. A dose-response relationship is one of the grounds for judging causation (the Bradford Hill criteria of [7.7.13](/7.7.13)).

![The trend chi-square test: the international case-control study of breast cancer and age at first birth (MacMahon et al. 1970, Bull. WHO 43:209), 3220 cases and 10 245 controls, all parous women. Dots are the proportions of cases in each age-at-first-birth group with 95% Wilson intervals; the dashed line is the weighted least-squares line with the Cochran–Armitage scores 1–5 as the independent variable (trend chi-square 129.0, 1 degree of freedom; deviation from linearity 1.3, 3 degrees of freedom)](./plots/trend.py)

### 9.6.2. The Link with GWAS

In a **genome-wide association study**, the three genotypes AA, Aa and aa at a SNP form an ordered three-level exposure (the number of risk alleles 0, 1, 2). On the $2 \times 3$ table of cases and controls, the Cochran–Armitage trend test with scores 0, 1, 2 is the association test under the additive genetic model. It does not require the population to be in **Hardy–Weinberg equilibrium**, and so is one of the standard single-marker tests of GWAS; the 2×2 chi-square test on allele counts, by contrast, requires HWE to hold ([7.4.25](/7.4.25)).

## 9.7. Goodness-of-Fit Tests

### 9.7.1. The General Form

A **goodness-of-fit test** asks: do the observed frequencies in the categories agree with a given theoretical distribution?

**Formula 9.7.1 (Chi-Square Goodness-of-Fit Test)** Let the observed frequencies of $k$ categories be $O_i$ and the expected frequencies given by the theoretical distribution be $E_i = np_i$. The statistic $X^2 = \sum_{i=1}^k (O_i - E_i)^2/E_i$ is approximately $\chi^2_{k-1-s}$ under $H_0$, where $s$ is the number of parameters of the theoretical distribution estimated from the same data (by maximum likelihood on the grouped data, [3.2.6](/3.2.6#sec-6.3.3)). The expected frequency of each category should generally be at least 5; otherwise adjacent categories are merged.

The commonest use in genetics is to test segregation ratios: for Mendel's 556 F₂ peas, computed against the expected frequencies of 9:3:3:1, $X^2 = 0.47$ with 3 degrees of freedom and $p = 0.93$ ([7.4.2 Example 2.5.1](/7.4.2#ex-2.5.1)); the test of Hardy–Weinberg proportions requires estimating one allele frequency from the data, so the degrees of freedom are $3 - 1 - 1 = 1$ ([7.4.22 Algorithm 22.2.1](/7.4.22#alg-22.2.1)).

**Example 9.7.1 (Is the Number of Prenatal Visits Poisson?)** birthwt records the number of visits each mother made in the first trimester: 0 visits for 100 mothers, 1 for 47, 2 for 30, and 3 or more for 12 (mean 0.794, variance 1.122). Fitting a Poisson distribution with the sample mean as parameter, the expected frequencies of the four categories are 85.5, 67.8, 26.9 and 8.8 (the fourth is $\mathbb{P}(X \ge 3)$). $X^2 = 10.4$ with $4 - 1 - 1 = 2$ degrees of freedom and $p = 0.006$: the Poisson distribution does not fit, since mothers with no visits and those with many visits are both more numerous than the Poisson distribution predicts, and those with one visit fewer. The variance exceeds the mean, which is *overdispersion*: mothers differ in their propensity to attend (depending on insurance, transport, health awareness), so the numbers of visits are not draws from a single Poisson process. Overdispersed counts are ubiquitous in omics data, and the model is the negative binomial distribution ([7.7.4](/7.7.4), Section 4.6.3; [7.7.20](/7.7.20)).

![Poisson fit to the number of first-trimester prenatal visits of 189 mothers in birthwt (Baystate Medical Center 1986). Bars are the observed numbers of mothers with 0, 1, 2 and 3 or more visits; dots (numbers in parentheses) are the expected numbers for a Poisson distribution with the sample mean 0.794 as parameter. Mothers with no visits and with many visits are too numerous and those with one visit too few: chi-square 10.4, 2 degrees of freedom, p = 0.006; the variance 1.12 exceeds the mean, a sign of overdispersion](./plots/gof-ftv.py)

### 9.7.2. Interpreting Goodness of Fit

The $H_0$ of a goodness-of-fit test is "the theoretical distribution is correct", and the investigator usually hopes not to reject it. This inverts the logic of the test: with a small sample and low power any theory "fits well", and with a large sample any theory is rejected. "Not significant" cannot prove the theory correct ([7.7.6](/7.7.6), Section 6.4.4); and when testing a continuous distribution (such as normality), the way the data are grouped also affects the conclusion, so better tools are the QQ plot and the **Shapiro–Wilk test**. Conversely, a fit that is "too good" is also suspicious: Fisher (1936) pooled all of Mendel's experiments and found a total chi-square value unusually small, a controversy still unresolved ([7.4.2](/7.4.2)).

## 9.8. Measures of Association and Agreement

### 9.8.1. Strength of Association

The chi-square test answers only "is there an association"; $X^2$ grows with the sample size and cannot be used to compare the strength of associations. The most commonly used measures of effect for a 2×2 table are the difference in proportions (risk difference), the ratio of proportions (relative risk) and the odds ratio:

| Measure | Definition | Example 9.1.1 (smoking × low birth weight) |
|---|---|---|
| Risk difference RD | $\hat p_1 - \hat p_2$ | 0.153 (0.016, 0.290) |
| Relative risk RR | $\hat p_1/\hat p_2$ | 1.61 (1.06, 2.44) |
| Odds ratio OR | $\dfrac{a/b}{c/d} = \dfrac{ad}{bc}$ | 2.02 (1.08, 3.78) |

Their intervals, their interpretation and whether they can be estimated under different study designs are the subject of [7.7.13](/7.7.13). For general $R \times C$ tables, dimensionless measures derived from the chi-square are commonly used.

**Definition 9.8.1 (Phi Coefficient and Cramér's V)** The **phi coefficient** of a 2×2 table is

$$
\varphi = \frac{ad - bc}{\sqrt{(a+b)(c+d)(a+c)(b+d)}}, \qquad \varphi^2 = X^2/n,
$$
which is the Pearson correlation coefficient of two 0/1 variables. **Cramér's V** for an $R \times C$ table is

$$
V = \sqrt{\frac{X^2}{n(\min(R, C) - 1)}} \in [0, 1].
$$

In Example 9.1.1, $\varphi = 0.16$; in Example 9.5.2 (race × smoking) $V = 0.34$, and in Example 9.5.1 (race × low birth weight) $V = 0.16$; in Example 9.1.3, $\varphi = 0.076$: with $p$ as small as $10^{-18}$ the association is nevertheless weak, which is characteristic of large samples. Another old measure is the contingency coefficient $C = \sqrt{X^2/(X^2 + n)}$, whose maximum depends on the size of the table and which is less convenient than $V$. These measures have no direct medical interpretation, and in medicine RR and OR are more often reported.

### 9.8.2. Agreement Between Raters: Cohen's Kappa

Two radiologists independently read the same set of CT scans, or two laboratory assays classify the same set of samples, and the question is how well the two agree. The most natural measure appears to be the proportion of agreement $p_o$, but even if the two read completely at random, a considerable proportion of agreement will occur, especially when most readings are negative.

**Definition 9.8.2 (Cohen's Kappa)** Let two raters classify $n$ subjects, let $p_o$ be the proportion on which they agree, and let $p_e = \sum_k p_{k\cdot}\,p_{\cdot k}$ be the proportion of agreement expected if the two rated independently (according to their own marginal proportions). The quantity

$$
\kappa = \frac{p_o - p_e}{1 - p_e}
$$
is called **Cohen's kappa**.

$\kappa = 1$ means perfect agreement, $\kappa = 0$ means agreement no greater than chance, and $\kappa < 0$ means agreement worse than chance. A commonly used (and arbitrary) scale of interpretation is that of Landis and Koch (1977): 0.41–0.60 moderate, 0.61–0.80 substantial, above 0.81 almost perfect.

**Example 9.8.1 (A Worked Example)** Suppose two physicians read 200 chest radiographs; both call 20 positive, only A calls 10 positive, only B calls 15 positive, and both call 155 negative (the numbers are made up for demonstration). $p_o = 175/200 = 0.875$; A's proportion positive is 0.15 and B's 0.175, so $p_e = 0.15 \times 0.175 + 0.85 \times 0.825 = 0.728$ and $\kappa = (0.875 - 0.728)/(1 - 0.728) = 0.54$, moderate agreement. If in another 200 radiographs the two both call 2 positive, each calls 4 more positive alone, and both call 190 negative, the proportion of agreement is as high as 96%, but $p_e = 0.942$ and $\kappa$ is only 0.31: almost all of the agreement comes from "both call negative", while among the few positives where judgment is actually needed the two mostly disagree.

This example shows two sides of $\kappa$: it corrects for chance agreement and therefore reflects the reliability of the readings better than $p_o$ does; but it depends on the proportion positive (the "prevalence paradox"), so $\kappa$ values from different populations should not be compared directly. A report should also give the 2×2 table, or the proportions of agreement among positives and among negatives separately. For ordered multi-level ratings (such as a five-point scale) one uses weighted $\kappa$, which treats a disagreement of one level differently from a disagreement of four levels; agreement of continuous measurements is assessed by the intraclass correlation coefficient ([7.7.17](/7.7.17)) and the Bland–Altman plot ([7.7.11](/7.7.11)).

## 9.9. Computing in Python

```python
import numpy as np
import pandas as pd
from scipy import stats

bw = pd.read_csv("birthwt.csv")
tab = pd.crosstab(bw.smoke, bw.low).loc[[1, 0], [1, 0]].to_numpy()   # [[30, 44], [29, 86]]

# two proportions, chi-square with and without Yates (Example 9.1.1)
print(stats.chi2_contingency(tab, correction=False)[:2])   # X2 = 4.92, p = 0.026
print(stats.chi2_contingency(tab)[:2])                     # Yates: 4.24, p = 0.040 (scipy's default)
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep
print(proportions_ztest([30, 29], [74, 115]))              # z = 2.22
print(confint_proportions_2indep(30, 74, 29, 115, method="wald"))   # (0.016, 0.290)

# Fisher's exact test (Example 9.2.1)
ht = pd.crosstab(bw.ht, bw.low).loc[[1, 0], [1, 0]].to_numpy()       # [[7, 5], [52, 125]]
print(stats.fisher_exact(ht))                               # OR 3.37, p = 0.052

# McNemar (Example 9.3.1): b = 0, c = 12 discordant pairs
from statsmodels.stats.contingency_tables import mcnemar
print(mcnemar([[2, 0], [12, 4]], exact=True).pvalue)        # 0.00049

# R x C table, likelihood-ratio chi-square, Cramer's V (Examples 9.5.1 and 9.5.2)
rs = pd.crosstab(bw.race, bw.smoke).to_numpy()
chi = stats.chi2_contingency(rs)
print(chi.statistic, chi.pvalue)                            # 21.8, 2e-5
print(stats.chi2_contingency(rs, lambda_="log-likelihood")[:2])
print(stats.contingency.association(rs, method="cramer"))   # 0.34

# Cochran-Armitage trend test (Example 9.6.1)
cases = np.array([320, 1206, 1011, 463, 220])
controls = np.array([1422, 4432, 2893, 1092, 406])
s = np.arange(1, 6)
n, N, pbar = cases + controls, (cases + controls).sum(), cases.sum() / (cases + controls).sum()
T = (cases * s).sum() - pbar * (n * s).sum()
V = pbar * (1 - pbar) * ((n * s**2).sum() - (n * s).sum()**2 / N)
print(T**2 / V, stats.chi2.sf(T**2 / V, 1))                 # 129.0, 7e-30

# goodness of fit with one estimated parameter (Example 9.7.1): ddof=1 removes one more df
obs = np.array([100, 47, 30, 12])
lam = bw.ftv.mean()
p = np.r_[stats.poisson.pmf([0, 1, 2], lam), stats.poisson.sf(2, lam)]
print(stats.chisquare(obs, obs.sum() * p, ddof=1))          # 10.4, p = 0.006

# Cohen's kappa from a 2 x 2 agreement table (Example 9.8.1)
from statsmodels.stats.inter_rater import cohens_kappa
print(cohens_kappa(np.array([[20, 10], [15, 155]])).kappa)  # 0.54
```

## Summary

- The z test for two proportions (Formula 9.1.1) and the chi-square test for a 2×2 table (Formula 9.1.2) are the same test, with $X^2 = z^2$; the sampling scheme (two fixed groups, fixed total, case-control) does not change the test but only the effect that can be estimated.
- Choice of method:

  | Data | Method | Condition or point | Example |
  |---|---|---|---|
  | Two independent proportions | z test / chi-square test | All expected frequencies at least 5 | Examples 9.1.1–9.1.3 |
  | Two independent proportions, small expected frequencies | Fisher's exact test (Definition 9.2.1) | Hypergeometric distribution; conservative | Example 9.2.1 |
  | Paired proportions | McNemar's test (Formula 9.3.1) | Uses only the discordant pairs | Example 9.3.1 |
  | $R \times C$ table | Chi-square or $G^2$ (Formula 9.5.1) | Degrees of freedom $(R-1)(C-1)$; at most 20% of cells with $E < 5$ | Examples 9.5.1, 9.5.2 |
  | Ordered exposure | Cochran–Armitage trend test (Definition 9.6.1) | 1 degree of freedom; power concentrated on a monotone trend | Example 9.6.1 |
  | Frequencies against a theoretical distribution | Goodness-of-fit test (Formula 9.7.1) | Degrees of freedom $k - 1 - s$ | Example 9.7.1 |

- Yates's correction (Definition 9.1.1) and Fisher's test are both conservative; report the uncorrected chi-square when the expected frequencies are sufficient and Fisher's test when they are small. The sample size (Formula 9.4.1) grows sharply for rare events.
- Strength of association is measured by RD, RR and OR ([7.7.13](/7.7.13)) or by $\varphi$ and Cramér's V (Definition 9.8.1), not by $X^2$ or the p-value; agreement between raters is measured by Cohen's kappa (Definition 9.8.2), which depends on the proportion positive.
- Main thread: the proportion of low-birth-weight infants is 0.405 for smoking mothers against 0.252, $p = 0.026$, OR 2.02 (1.08–3.78); but smoking is strongly related to race (Example 9.5.2) and race is related to low birth weight, so the crude association needs adjustment. This is the starting point of the stratified analysis of [7.7.13](/7.7.13) and the logistic regression of [7.7.14](/7.7.14).

## Questions

1. Recompute the chi-square value for the Physicians' Health Study (aspirin 139/11 037, placebo 239/11 034) with the shortcut formula of Formula 9.1.2, and verify that it equals $z^2$. Why does Yates's correction have almost no effect in this study?

   **Answer** $a = 139$, $b = 10\,898$, $c = 239$, $d = 10\,795$, $n = 22\,071$. $ad - bc = 139 \times 10\,795 - 10\,898 \times 239 = 1\,500\,505 - 2\,604\,622 = -1\,104\,117$. $X^2 = 22\,071 \times 1\,104\,117^2/(11\,037 \times 11\,034 \times 378 \times 21\,693) = 26.9$, $p = 2 \times 10^{-7}$, equal to $z^2 = 5.19^2 = 26.9$. Yates's correction subtracts $n/2 = 11\,036$ from $\lvert ad - bc\rvert$, which changes a quantity of 1.1 million by only 1%, so $X^2_{\mathrm{Y}} = 26.4$: when the numbers of events are all above 100, the continuity correction is immaterial.

2. A hospital reports that 1 of 12 patients who had a new operation developed a postoperative infection, against 6 of 13 patients who had the conventional operation. (a) Why is the chi-square test inappropriate? (b) Write down the hypergeometric distribution used by Fisher's exact test and explain how to compute the one-sided p-value (the result is $p = 0.046$). (c) Does the result show that the new operation is better?

   **Answer** (a) There are 7 infections in all; the expected frequency of the infection cell in the new-operation group is $12 \times 7/25 = 3.36 < 5$, and in the other group $13 \times 7/25 = 3.64 < 5$, so the chi-square approximation is unreliable. (b) With the margins fixed (12 and 13 patients, 7 infected and 18 not), the number of infections $a$ in the new-operation group has $\mathbb{P}(a) = \binom{12}{a}\binom{13}{7-a}/\binom{25}{7}$, $a = 0, \dots, 7$. The one-sided p-value (fewer infections with the new operation) is $\mathbb{P}(a \le 1) = [\binom{13}{7} + 12\binom{13}{6}]/\binom{25}{7} = (1716 + 12 \times 1716)/480\,700 = 22\,308/480\,700 = 0.046$ (with $\binom{13}{6} = \binom{13}{7} = 1716$). (c) Even if it is significant at the one-sided 0.05 level, this does not show it: the sample is very small and the 95% confidence interval very wide; if the patients were not randomly allocated, the two groups may differ in severity and in the surgeons' experience (selection bias); comparing operations requires a larger randomized trial.

3. Use Fisher's exact test and the permutation test of Section 8.6 to explain why it is reasonable for Fisher's test to treat the marginal totals as fixed.

   **Answer** Under $H_0$ (treatment unrelated to outcome), each individual's outcome is independent of the group to which he or she is assigned. If the outcome is regarded as an inherent attribute of the individual, the total number of events (the column total) is fixed; random allocation fixes the sizes of the two groups (the row totals). The only random element is then "which individuals are assigned to the first group", and the number of events in the first group has a hypergeometric distribution: this is precisely the permutation test for a dichotomous outcome with the number of events as the statistic. Conditioning on the marginal totals also eliminates the unknown common proportion $p$, so that the test does not depend on it ($p$ is a nuisance parameter and the marginal totals are a sufficient statistic for it).

4. In a study 100 patients with suspected tuberculosis received two rapid tests simultaneously, with sputum culture as the gold standard. Among the 40 confirmed patients, both tests were positive in 28, only A in 8, only B in 1, and both negative in 3. (a) Compare the sensitivities of the two tests. (b) Why can the chi-square test for two proportions not be used?

   **Answer** (a) The sensitivity of A is $(28 + 8)/40 = 0.90$ and that of B is $(28 + 1)/40 = 0.725$. The discordant pairs are $b = 8$ and $c = 1$; the exact McNemar test gives twice $\mathbb{P}(\text{Bin}(9, 1/2) \ge 8) = 2 \times (9 + 1)/512 = 0.039$; the approximation $(\lvert 8 - 1\rvert - 1)^2/9 = 4.0$ gives $p = 0.046$. The sensitivity of A is significantly higher. (b) The two sensitivities come from the same 40 patients and are not two independent samples: the two test results of the same patient are highly correlated (patients with a high bacillary load tend to be positive on both tests). A test for independent samples ignores this correlation and its standard error is incorrect. The comparison of specificities likewise uses only paired data from the 60 non-patients.

5. (Design question) A randomized trial is planned to compare the cure rates of a new and an old regimen. The old regimen is expected to cure 60% and the new regimen should be detectable if it raises this to 75%. How many are needed per group for a two-sided $\alpha = 0.05$ and 80% power? If only 100 patients (50 per group) can be recruited, what is the approximate power?

   **Answer** $\bar p = 0.675$, $\sqrt{2\bar p\bar q} = \sqrt{2 \times 0.675 \times 0.325} = 0.6624$ and $\sqrt{p_1q_1 + p_2q_2} = \sqrt{0.24 + 0.1875} = 0.6538$. $n = (1.96 \times 0.6624 + 0.842 \times 0.6538)^2/0.15^2 = (1.2983 + 0.5505)^2/0.0225 = 3.418/0.0225 = 151.9$, so 152 per group. With 50 per group the approximate power is $\Phi\big((0.15\sqrt{50} - 1.96 \times 0.6624)/0.6538\big) = \Phi\big((1.0607 - 1.2983)/0.6538\big) = \Phi(-0.36) = 0.36$: in most cases the result would be nonsignificant, and such a trial is not worth doing except as a pilot.

6. Using the data of Example 9.6.1, explain why a trend test is more appropriate than the global $2 \times 5$ chi-square test for an ordered exposure. What would the trend test do if the data were U-shaped (low in the middle, high at both ends)?

   **Answer** The global chi-square has 4 degrees of freedom and responds to any departure, so the statistic is spread over 4 directions; the trend test concentrates all the power on the single direction of monotone change. Of the global chi-square of 130.3 in Example 9.6.1, 129.0 comes from the linear trend and only 1.3 from other directions: with 1 degree of freedom we obtain almost as large a statistic, a much smaller p-value, and a meaningful conclusion (risk rises monotonically with age at first birth). If the relationship were U-shaped, the slope of the linear trend could be close to 0, the trend test would be nonsignificant and the part for deviation from linearity would be large; a global test or fitting a quadratic trend would then be more suitable. One should therefore plot the proportions at each level before choosing a test, and report the deviation from linearity.

7. In birthwt, the chi-square test for race and low birth weight has $p = 0.082$ and that for race and smoking has $p = 2 \times 10^{-5}$. Write down the smallest expected frequency in each of the two tables, decide whether the chi-square approximation is applicable, and explain why the second result matters for interpreting Example 9.1.1.

   **Answer** Race × low birth weight: the smallest expected frequency is that of the cell black and low birth weight, $26 \times 59/189 = 8.1$; race × smoking: the cell black and smoker, $26 \times 74/189 = 10.2$. Both exceed 5, so the chi-square approximation applies. Smoking is commonest among white mothers (54%), who have the lowest proportion of low-birth-weight infants (24%); if race affects birth weight by other routes (socioeconomic status, access to care), then after stratification by race the association between smoking and low birth weight may be stronger than the crude analysis shows (confounding by race biases the crude OR toward 1). This requires comparing smoking and nonsmoking mothers within the same race, that is, stratified analysis and logistic regression ([7.7.13](/7.7.13), [7.7.14](/7.7.14)).

8. The 2×2 table of a study is as follows: two pathologists both call 45 cases "malignant", only the first calls 5 "malignant", only the second calls 10 "malignant", and both call 40 "benign". Compute the proportion of agreement and Cohen's kappa, and use McNemar's test to decide whether the two differ in their tendency to call "malignant".

   **Answer** $n = 100$ and $p_o = 0.85$. The first pathologist's proportion malignant is 0.50 and the second's 0.55, so $p_e = 0.50 \times 0.55 + 0.50 \times 0.45 = 0.50$ and $\kappa = (0.85 - 0.50)/0.50 = 0.70$, substantial agreement. McNemar: the discordant pairs are $b = 5$ and $c = 10$, and the exact two-sided $p = 2\,\mathbb{P}(\text{Bin}(15, 1/2) \le 5) = 2 \times 0.151 = 0.30$; there is no evidence that the two differ in their tendency to read. $\kappa$ and McNemar answer different questions: $\kappa$ asks whether the two agree on the same case, McNemar asks whether the overall proportions called "malignant" are the same; the two can have the same proportions and yet poor agreement (each reading at random).

9. A GWAS obtains the following genotype counts at a SNP: cases AA/Aa/aa = 300/500/200 and controls 360/480/160. Compute (a) the trend test with scores 0, 1, 2 and (b) the global $2 \times 3$ chi-square test on genotype, and compare the two.

   **Answer** Take the number of a alleles as the score. $N = 2000$, $n_j = 660, 980, 360$, and the proportion of cases is $\bar p = 0.5$. $\sum x_j s_j = 500 + 400 = 900$, $\sum n_j s_j = 980 + 720 = 1700$, $T = 900 - 0.5 \times 1700 = 50$; $\sum n_j s_j^2 = 980 + 1440 = 2420$, and the variance term is $0.25 \times (2420 - 1700^2/2000) = 0.25 \times 975 = 243.75$; $X^2_{\mathrm{trend}} = 2500/243.75 = 10.26$ with 1 degree of freedom, $p = 0.0014$. Global chi-square: each expected frequency is half the corresponding column total (330, 490, 180), so $X^2 = 2 \times (30^2/330 + 10^2/490 + 20^2/180) = 2 \times (2.727 + 0.204 + 2.222) = 10.31$ with 2 degrees of freedom, $p = 0.0058$. The two statistics are almost equal (the part for deviation from additivity is only 0.05), but the trend test uses only 1 degree of freedom and its p-value is 4 times smaller. When the additive model is reasonable, the trend test is the more efficient choice ([7.4.25](/7.4.25)).

10. (Open question) A paper used chi-square tests to compare the intake of 20 foods (yes / no) with a certain cancer (yes / no), reported that 2 of them had $p < 0.05$, and stated in the abstract that "two carcinogenic foods were found". Comment point by point from the standpoint of this chapter and [7.7.6](/7.7.6).

    **Answer** Main points: (1) Multiple testing: with 20 tests at $\alpha = 0.05$, one significant result is expected even if none has any association, so 2 is not surprising; all results should be reported with a correction (the Bonferroni threshold is 0.0025), or the findings treated as hypotheses to be confirmed ([7.7.20](/7.7.20)). (2) The strength of association and its interval (OR with 95% interval) should be reported, not the p-value alone; with large samples even a very weak association is significant (the $\varphi = 0.076$ of Example 9.1.3). (3) Association is not causation; the conclusion "carcinogenic" requires ruling out confounding (people who eat a certain food may differ in smoking, drinking and income), recall bias (in a case-control study patients may be more likely to recall or exaggerate certain diets) and reverse causation ([7.7.13](/7.7.13), [7.7.15](/7.7.15)). (4) Check the expected frequencies: cells for rare foods may require Fisher's exact test. (5) If food intake is graded (never / occasionally / often), dichotomizing loses information and a trend test should be done; a dose-response relationship is also one of the grounds for judging causation.
