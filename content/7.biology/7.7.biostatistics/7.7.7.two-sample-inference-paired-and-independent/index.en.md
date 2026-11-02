---
title: "Two-Sample Inference: Paired and Independent Samples"
description: The difference between paired and independent samples; the paired t-test and confidence interval for paired differences; the two-sample t-test with pooled variance; the F test and Levene test for equality of variances; Welch's test for unequal variances; sample size for two-sample comparisons and the efficiency of the paired design; geometric mean ratios on the log scale; decisions for two-sample problems. Illustrated with captopril and blood pressure, maternal smoking and birth weight, the paradox of smoking children and FEV, and a vitamin C experiment in guinea pigs.
source_hash: bab039069fd0
---

[7.7.6](/7.7.6) compared one sample with a known reference value, and its closing examples already exposed the weakness of such a comparison: the birth weight of infants of smoking mothers is far below the national mean, but infants of nonsmoking mothers in the same hospital are also below the national mean, so the external reference value is not comparable with the population studied. Most research questions are in fact comparisons of two groups: has blood pressure changed between before and after the drug? How much does the birth weight of infants of smoking mothers differ from that of nonsmoking mothers? Which is the more effective way to supplement vitamin C, orange juice or ascorbic acid? The parameters of both populations are then unknown, and two samples are compared with each other. This chapter first distinguishes two kinds of design, the paired design (the same individual measured twice, or similar individuals matched into pairs) and independent samples (two groups of unrelated individuals), which determine the method of analysis; it then treats in turn the paired **t-test**, the two-sample t-test with pooled variance, tests of equality of variances and **Welch's t-test** for unequal variances, sample size for two-group comparisons, and comparisons on the log scale. The examples follow the main threads of the course: the birth weights of birthwt can at last be compared within one sample; the paradox of "smoking children have better lung function" in the FEV data persists under the two-sample t-test, which shows that the problem lies not in the test but in the design. The mathematical derivations (the distribution of the pooled-variance t statistic, the Behrens–Fisher problem) are in [3.2.5](/3.2.5#sec-5.2.4) and [3.2.4](/3.2.4#sec-4.3.3); rank methods for data that do not satisfy normality are in [7.7.8](/7.7.8), and comparisons of more than two groups are in [7.7.12](/7.7.12).

## 7.1. Two Kinds of Design

### 7.1.1. Paired and Independent

**Definition 7.1.1 (Paired Design and Independent Samples)** If each observation in the first sample corresponds to exactly one observation in the second sample, and the two corresponding observations come from the same individual or from two individuals matched on some characteristics, the two samples are paired, and such a study design is a **paired design**. If there is no correspondence between the observations of the two samples, they are **independent samples**.

Common forms of pairing:

| Form | Example | What pairing controls |
|---|---|---|
| Self-controlled before and after | Blood pressure of the same patient before and after a drug | The individual's baseline level |
| Two sites on the same individual | Two sunscreens applied randomly to the left and right arms | The individual's skin type and sun exposure |
| Matched individuals | Patients and controls matched by age and sex | The matching variables |
| Twins | Bone density of 41 pairs of middle-aged female twins discordant for smoking (Hopper and Seeman 1994) | Genetic background and upbringing |

Whether data are paired is determined by the design, not by the data: that two columns of numbers have the same number of rows does not make them paired. The criterion is whether one can say why the two observations in "pair $i$" belong together. In the guinea pig experiment the third animal fed orange juice has nothing to do with the third animal fed ascorbic acid; they merely happen to be in the same row of the data file.

### 7.1.2. Longitudinal and Cross-Sectional Studies

The two kinds of design correspond to two kinds of study. **Longitudinal data** come from repeated observation of the same individuals over a period of time (follow-up studies): they show changes in individuals directly, and the individual's baseline level cancels in the comparison; the drawbacks are cost and duration, loss to follow-up, and possible practice or fatigue effects from repeated measurement. **Cross-sectional data** come from a single measurement of different individuals at one moment: cheap and fast, but only different people can be compared, and all differences between individuals enter the error. For the same question, "does smoking impair lung function", one can measure the FEV of the same children every year (longitudinal, to see whether the growth of FEV slows after smoking begins) or measure 654 children once, as in the FEV data (cross-sectional, comparing smokers with nonsmokers). The two do not answer exactly the same question, and the latter is more easily disturbed by factors such as age (Section 7.3). The full analysis of longitudinal data is in [7.7.17](/7.7.17).

### 7.1.3. Limitations of Before-and-After Comparisons

A paired design can improve precision, but the simple "before and after the drug" comparison has three often overlooked problems:

1. No control: anything that happens between the two measurements (season, diet, placebo effect, the natural course of the disease) is mixed into the difference. In particular, if the entry criterion is "blood pressure above a certain value", the second measurement will on average be lower automatically, which is **regression to the mean**.
2. It is not always feasible: many interventions (education, surgery) cannot be compared one after another in the same individual, or cannot be "undone".
3. Pairing does not necessarily save effort: the difference contains the error of both measurements. If there are no large and stable differences between individuals, pairing not only gains nothing but counts the random within-individual error twice (Section 7.6).

A typical mistake is to make before-and-after comparisons only within each group. Imagine a preclinical toxicity trial of a new drug in which young rats are divided into several dose groups and a saline control group, and body weight is recorded before dosing and several weeks later: the paired t-test in every group, including the control group, will be extremely significant, because the rats are growing. Whether the drug affects weight must be judged by comparing the dose groups with the control group, that is, by comparing the "change" between groups (with the independent two-sample method), not by seeing whether there is a change within each group.

## 7.2. The Paired t-Test

### 7.2.1. Reduction to a One-Sample Problem

Let the two observations of pair $i$ be $x_{i1}, x_{i2}$. The individuals' baseline levels $\mu_i$ all differ, but if we assume $x_{i1} \sim \mathcal{N}(\mu_i, \sigma^2)$ and $x_{i2} \sim \mathcal{N}(\mu_i + \Delta, \sigma^2)$, the distribution of the difference $d_i = x_{i2} - x_{i1}$ does not depend on $\mu_i$: $d_i \sim \mathcal{N}(\Delta, \sigma_d^2)$. The comparison of two samples is thus reduced to the one-sample t-test of [7.7.6](/7.7.6) on the $n$ differences.

**Formula 7.2.1 (Paired t-Test)** Let the differences $d_1, \dots, d_n$ of $n$ pairs be independently drawn from $\mathcal{N}(\Delta, \sigma_d^2)$, and let $\bar d$ and $s_d$ be their sample mean and sample standard deviation. The statistic for testing $H_0\colon \Delta = \Delta_0$ is

$$
t = \frac{\bar d - \Delta_0}{s_d/\sqrt n},
$$
which follows $t_{n-1}$ under $H_0$. The $100(1-\alpha)\%$ confidence interval for $\Delta$ is $\bar d \pm t_{n-1,\alpha/2}\, s_d/\sqrt n$.

This is the **paired t-test**. Its premises concern only the differences: the $n$ pairs are mutually independent and the differences are approximately normal (which can be relaxed when $n$ is large, by the **central limit theorem**). Whether the two measurements themselves are normal, and whether their variances are equal, do not matter.

### 7.2.2. Captopril and Systolic Pressure

**Example 7.2.1 (Captopril)** The angiotensin-converting enzyme inhibitor captopril was one of the first oral antihypertensive drugs. MacGregor et al. (1979) measured the systolic pressure (mmHg) of 15 patients with essential hypertension before and after the drug:

| Patient | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Before | 210 | 169 | 187 | 160 | 167 | 176 | 185 | 206 | 173 | 146 | 174 | 201 | 198 | 148 | 154 |
| After | 201 | 165 | 166 | 157 | 147 | 145 | 168 | 180 | 147 | 136 | 151 | 168 | 179 | 129 | 131 |
| Difference $d_i$ | 9 | 4 | 21 | 3 | 20 | 31 | 17 | 26 | 26 | 10 | 23 | 33 | 19 | 19 | 23 |

The mean of the differences (before minus after) is $\bar d = 18.93$, the standard deviation is $s_d = 9.03$, and the standard error is $9.03/\sqrt{15} = 2.331$. Testing $H_0\colon \Delta = 0$:

$$
t = \frac{18.93}{2.331} = 8.12, \qquad \nu = 14, \qquad p = 1.1 \times 10^{-6}.
$$
The 95% confidence interval is $18.93 \pm 2.145 \times 2.331 = (13.93, 23.93)$ mmHg.

What the investigators care about is not only "whether there is a decrease" but "whether the mean decrease exceeds 10 mmHg", a clinically meaningful magnitude. The one-sided test of $H_0\colon \Delta \le 10$ against $H_1\colon \Delta > 10$ gives $t = (18.93 - 10)/2.331 = 3.83$, $p = 0.0009$. The lower limit of the confidence interval, 13.9, is also above 10, consistent with this.

The conclusion still needs discounting: it is a before-and-after comparison without a control group (Section 7.1.3). The patients enrolled have high blood pressure, and the second measurement would be lower anyway because of regression to the mean; the patients also know they are taking a drug, so there is a placebo effect. How much of the 19 mmHg decrease is due to the drug must be answered by a randomized controlled trial (Section 5.2 of [7.7.5](/7.7.5)).

![Paired data: systolic pressure of 15 hypertensive patients before and after captopril (MacGregor et al. 1979). A: the two readings of each patient joined by a line, nearly all going down. B: scatter plot of before against after; the two readings of the same patient are highly correlated (r = 0.90), which the paired design exploits. C: the 15 differences (before minus after), their mean and 95% t interval, with reference lines at 0 and at the clinically meaningful 10 mmHg](./plots/captopril-paired.py)

### 7.2.3. Why Pairing Is More Precise

If the pairing is ignored and the before and after readings are treated as two independent samples (the method of Section 7.3), the same data give $t = 2.56$ and $p = 0.016$: the conclusion is still significant, but the evidence is weaker by five orders of magnitude. The reason is in panel B above: blood pressure differs greatly between patients (the standard deviation of both measurements is about 20 mmHg), and these differences between individuals all count as error in the comparison of two independent samples, whereas in the differences each patient's baseline level has been subtracted. By the variance of the difference of two random variables in [7.7.4](/7.7.4),

$$
\operatorname{Var}(x_{i2} - x_{i1}) = \sigma_1^2 + \sigma_2^2 - 2\rho\sigma_1\sigma_2,
$$
which for equal standard deviations $\sigma$ of the two measurements is $\sigma_d^2 = 2\sigma^2(1 - \rho)$. In the captopril data $\rho = 0.90$, and the standard deviation of the differences (9.0) is less than half that of a single measurement. The larger $\rho$, the greater the gain from pairing; at $\rho = 0.5$ the variance of the difference equals that of the independent design (but half the participants are still saved, Section 7.6); for $\rho < 0.5$ the difference is in fact more uncertain than a single measurement.

### 7.2.4. The First Example in History

**Example 7.2.2 (Hypnotic drug and sleep time)** In his 1908 paper introducing the t-distribution, Student (W. S. Gosset) used a set of paired data: Cushny and Peebles (1905) recorded, for 10 patients, the increase in sleep time (h) on nights with a hypnotic (levo-hyoscyamine) compared with nights without: 1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4 (the `sleep` dataset of R). The mean difference is $\bar d = 1.58$ h and the standard deviation is $s_d = 1.230$ h,

$$
t = \frac{1.58}{1.230/\sqrt{10}} = \frac{1.58}{0.389} = 4.06, \qquad \nu = 9, \qquad p = 0.0028,
$$
and the 95% confidence interval is $1.58 \pm 2.262 \times 0.389 = (0.70, 2.46)$ h. The paired t-test can be carried out knowing only the mean and standard deviation of the differences and the number of pairs; a paper that reports only the means and standard deviations under the two conditions (and not the standard deviation of the differences) does not allow readers to redo the paired analysis. The value 4.6 among the differences is far from the rest, and whether the conclusion depends on it can be checked with rank methods that are not affected by outliers ([7.7.8](/7.7.8), Example 8.3.2).

## 7.3. The Independent Two-Sample t-Test

### 7.3.1. Pooled Variance

Let two independent samples come from $\mathcal{N}(\mu_1, \sigma_1^2)$ and $\mathcal{N}(\mu_2, \sigma_2^2)$, and suppose $\mu_1$ and $\mu_2$ are to be compared. $\bar x_1 - \bar x_2$ is an estimate of $\mu_1 - \mu_2$, with variance $\sigma_1^2/n_1 + \sigma_2^2/n_2$. If the two variances are equal ($\sigma_1^2 = \sigma_2^2 = \sigma^2$), both samples provide information about $\sigma^2$ and should be combined, weighted by degrees of freedom.

**Definition 7.3.1 (Two-Sample t-Test)** Let two independent samples come from normal populations with equal variances. The quantity

$$
s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}
$$
is the **pooled variance**. The **two-sample t-test** of $H_0\colon \mu_1 = \mu_2$ uses the statistic

$$
t = \frac{\bar x_1 - \bar x_2}{s_p\sqrt{1/n_1 + 1/n_2}},
$$
which follows $t_{n_1+n_2-2}$ under $H_0$. The $100(1-\alpha)\%$ confidence interval for $\mu_1 - \mu_2$ is $\bar x_1 - \bar x_2 \pm t_{n_1+n_2-2,\alpha/2}\, s_p\sqrt{1/n_1 + 1/n_2}$.

The pooled variance is a weighted average of the two sample variances, with the larger sample receiving more weight; for equal sample sizes it is the simple average. The proof of the distribution of the statistic is in [3.2.5](/3.2.5#sec-5.2.4).

### 7.3.2. Maternal Smoking and Birth Weight

**Example 7.3.1 (birthwt)** Among the 189 newborns of birthwt, the 115 infants of nonsmoking mothers have a mean birth weight of 3055.7 g (standard deviation 752.7 g) and the 74 infants of smoking mothers 2771.9 g (659.6 g), a difference of 283.8 g. The pooled standard deviation is

$$
s_p = \sqrt{\frac{114 \times 752.7^2 + 73 \times 659.6^2}{187}} = 717.8\ \mathrm{g},
$$
the standard error of the difference is $717.8\sqrt{1/115 + 1/74} = 107.0$ g, and

$$
t = \frac{283.8}{107.0} = 2.65, \qquad \nu = 187, \qquad p = 0.0087,
$$
with a 95% confidence interval of $283.8 \pm 1.973 \times 107.0 = (72.8, 494.8)$ g. Infants of smoking mothers are on average about 280 g lighter, and the data are compatible with anything from 70 g to 500 g lighter. The standardized **effect size** $d = 283.8/717.8 = 0.40$ is a "small-to-medium" effect; but a birth weight 280 g lower is clinically not a small matter, and the proportion of low birth weight rises correspondingly from 25% to 41% ([7.7.9](/7.7.9)).

[7.7.5](/7.7.5) used "the confidence intervals of the two groups do not overlap" to judge roughly that the groups differ; the test here gives the formal answer. Note that "the intervals do not overlap" is a conservative judgment: when two separate 95% intervals partially overlap, the 95% interval for the difference may still exclude 0, because the standard error of the difference, $\sqrt{\mathrm{SE}_1^2 + \mathrm{SE}_2^2}$, is smaller than the sum of the two standard errors.

This is an **observational study**: smoking and nonsmoking mothers may differ in racial composition, age, prepregnancy weight and the number of prenatal visits (in birthwt, 54% of white mothers smoke, 38% of black mothers and 18% of mothers of other races, Example 9.5.2 of [7.7.9](/7.7.9)), and these factors themselves affect birth weight. How much of the 280 g difference is caused by smoking is answered by multiple regression adjustment in [7.7.14](/7.7.14) and by the methods of causal inference in [7.7.15](/7.7.15).

![birthwt: birth weights of infants of 115 nonsmoking and 74 smoking mothers (Hosmer and Lemeshow, Baystate Medical Center 1986). A: each infant (jittered dots), the group means and their 95% t intervals. B: the difference of means (nonsmoking minus smoking) and its 95% interval, computed with the pooled-variance t and with Welch's t; neither contains 0](./plots/birthwt-groups.py)

### 7.3.3. FEV of Smoking Children: The Paradox Persists

**Example 7.3.2 (FEV)** The question posed in [7.7.1](/7.7.1): the 65 smoking children have a mean FEV of 3.277 L (standard deviation 0.750) and the 589 nonsmoking children 2.566 L (0.851). The two-sample t-test gives

$$
t = 6.46, \qquad \nu = 652, \qquad p = 2 \times 10^{-10},
$$
a difference of 0.711 L with a 95% confidence interval of $(0.49, 0.93)$ L. There is nothing wrong with the calculation: among these children of East Boston, the mean FEV of smokers really is higher than that of nonsmokers, and this is not sampling error. The error lies in interpreting it as "smoking improves lung function".

Smokers average 13.5 years of age and nonsmokers 9.5, and FEV grows rapidly with age and height. Panel B below compares by age separately: at most of the ages from 10 to 16 at which there are smokers, the mean FEV of smokers is lower than that of nonsmokers of the same age (for example at 13: 3.38 against 3.53 L, at 15: 3.09 against 3.92 L), but there are too few smokers at each age and the comparison at a single age is unstable. Comparing only children aged 9 and above (the smokers are all aged 9–19) is not enough either: the difference shrinks to 0.30 L (Welch $p = 0.003$), still positive, because nonsmokers in this range are still younger. The two-sample t-test answers "do the two group means differ" and not "what causes the difference"; smokers and nonsmokers are inherently not comparable in age, the most typical problem in **observational studies**. A comparison that takes both age and height into account needs multiple regression ([7.7.10](/7.7.10)).

![The paradox in the two-sample comparison of FEV (654 children in East Boston, Tager et al. 1979; public version Kahn 2005). A: FEV of 589 nonsmokers and 65 smokers, horizontal lines are means: the two-sample t-test shows a higher FEV for smokers. B: mean FEV of the two groups by age (years), with the area of each dot proportional to the number of children: at the same age smokers do not have a higher FEV, and smokers are concentrated at the older ages](./plots/fev-paradox.py)

### 7.3.4. A Laboratory Example: Vitamin C in Guinea Pigs

**Example 7.3.3 (ToothGrowth)** Crampton (1947) studied the effect of vitamin C on tooth growth in guinea pigs: 60 guinea pigs were randomized into 6 groups of 10, supplemented with vitamin C at three doses (0.5, 1, 2 mg/d) and by two delivery methods (orange juice OJ or ascorbic acid VC), and the length of the odontoblasts was measured. The two delivery methods are compared at each dose:

| Dose / (mg/d) | OJ mean (SD) | VC mean (SD) | Difference | 95% interval | Welch $t$ | $p$ |
|---|---|---|---|---|---|---|
| 0.5 | 13.23 (4.46) | 7.98 (2.75) | 5.25 | (1.72, 8.78) | 3.17 | 0.006 |
| 1 | 22.70 (3.91) | 16.77 (2.52) | 5.93 | (2.80, 9.06) | 4.03 | 0.001 |
| 2 | 26.06 (2.66) | 26.14 (4.80) | −0.08 | (−3.80, 3.64) | −0.05 | 0.96 |

At low doses orange juice is more effective, and at the high dose the two do not differ. The difference between the two methods varies with dose, an example of interaction, and the formal analysis (two-way analysis of variance) is in [7.7.12](/7.7.12). Carrying out one t-test at each dose makes three tests in all, and such a split brings the problem of multiple comparisons, which analysis of variance is also meant to solve.

These animals were randomized, and there is no correspondence between guinea pigs in different groups, so the independent two-sample method is used. Treating the OJ and VC in the same row of the data file as a "pair" and doing a paired t-test is wrong: the basis of pairing must come from the design.

## 7.4. Equality of Variances

### 7.4.1. The F Test

The pooled-variance t-test assumes $\sigma_1^2 = \sigma_2^2$. The classical method for comparing two normal variances is the **F test**.

**Formula 7.4.1 (F Test for a Ratio of Variances)** Let two independent samples come from normal populations. The statistic for testing $H_0\colon \sigma_1^2 = \sigma_2^2$,

$$
F = \frac{s_1^2}{s_2^2},
$$
follows $F_{n_1-1, n_2-1}$ under $H_0$. The two-sided p-value is $2\min\{\mathbb{P}(F_{n_1-1,n_2-1} \le F), \mathbb{P}(F_{n_1-1,n_2-1} \ge F)\}$. By convention the larger variance is placed in the numerator, so that only the upper quantile is needed.

**Example 7.4.1** In birthwt, $F = 752.7^2/659.6^2 = 1.30$ with $(114, 73)$ degrees of freedom and $p = 0.23$: there is no evidence that the variances of the two groups differ. In ToothGrowth, for the two groups at 2 mg/d the standard deviation of the ascorbic acid group (4.80) is nearly twice that of the orange juice group (2.66), $F = 4.80^2/2.66^2 = 3.27$ with $(9, 9)$ degrees of freedom and $p = 0.093$: with only 10 animals per group, even a threefold difference in variance does not reach significance with the F test, because the power of variance tests in small samples is very low.

### 7.4.2. The F Test Is Extremely Sensitive to Non-Normality

Unlike the t-test for means, the F test for variances depends heavily on the normality assumption, and no sample size remedies this (Section 4.8 of [7.7.4](/7.7.4)). In the simulation of panel B below, the variances of the two groups are actually equal and each group has 25 observations; if the data come from the heavy-tailed $t_4$ distribution, the F test with nominal level 5% rejects $H_0$ with probability 22%, and with log-normal and exponential data 27%–29%. When the F test is "significant", it often shows that the data are not normal rather than that the variances differ.

**Levene's test** is more robust: it replaces each observation by its absolute deviation from the center of its group, $\lvert x_{ij} - \tilde x_j\rvert$, and compares the means of these deviations with the two-sample t-test (one-way analysis of variance for several groups). The version centered at the median $\tilde x_j$ (the Brown–Forsythe variant, the default of `scipy.stats.levene`) maintains the nominal level even with non-normal data (panel B below). In birthwt the Levene test gives $p = 0.23$, the same conclusion as the F test.

### 7.4.3. The "Two-Step Method" Is Not Recommended

Many textbooks recommend first doing an F test, then using the pooled-variance t-test if the variances are equal and Welch's test if not. This two-step method is no longer recommended: (1) the power of the variance test itself is very low in small samples, and "nonsignificant" does not mean the variances are equal; (2) when the same data are used first to test variances and then to choose the test, the Type I error rate of the second step is no longer the nominal $\alpha$; (3) the sensitivity of the F test to non-normality often makes the conclusion of the first step wrong. Current practice is to use Welch's test directly (Section 7.5). Only when equality of variances has biological meaning in itself (such as whether a treatment increases the variation between individuals) is the comparison of variances made a research question, and then the Levene test is used.

## 7.5. Unequal Variances: Welch's Test

The comparison of two normal means with unequal variances is the **Behrens–Fisher problem**, which has no exact solution ([3.2.4](/3.2.4#sec-4.3.3)). The approximate solution given by Welch (1938) is accurate enough in practice.

**Formula 7.5.1 (Welch's t-Test)** Let two independent samples come from normal populations whose variances may differ. The statistic for testing $H_0\colon \mu_1 = \mu_2$ is

$$
t = \frac{\bar x_1 - \bar x_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}},
$$
which under $H_0$ approximately follows a t-distribution with

$$
\nu = \frac{\left(s_1^2/n_1 + s_2^2/n_2\right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1 - 1} + \dfrac{(s_2^2/n_2)^2}{n_2 - 1}}
$$
degrees of freedom (the Satterthwaite approximation; software uses the noninteger $\nu$ directly, and when looking up tables it is rounded down). The approximate confidence interval for $\mu_1 - \mu_2$ is $\bar x_1 - \bar x_2 \pm t_{\nu,\alpha/2}\sqrt{s_1^2/n_1 + s_2^2/n_2}$.

$\nu$ always lies between $\min(n_1, n_2) - 1$ and $n_1 + n_2 - 2$: when the variances and sample sizes are similar it is close to the latter and the test is almost the same as the pooled-variance test; when the $s^2/n$ of one group is much larger than that of the other it is close to the former.

**Example 7.5.1** In ToothGrowth, for the two groups at 0.5 mg/d (10 animals each), the orange juice group has mean 13.23 and standard deviation 4.46, and the ascorbic acid group 7.98 and 2.75. The standard error is $\sqrt{4.46^2/10 + 2.75^2/10} = 1.656$,

$$
t = \frac{13.23 - 7.98}{1.656} = 3.17, \qquad \nu = \frac{2.743^2}{1.989^2/9 + 0.754^2/9} = 14.97, \qquad p = 0.0064.
$$
With equal sample sizes the Welch statistic and the pooled-variance statistic have the same numerical value and differ only in the degrees of freedom (14.97 against 18 here; the latter gives $p = 0.0053$). For birthwt, Welch's test gives $t = 2.73$, $\nu = 170.1$, $p = 0.0070$, with a 95% interval $(78.6, 489.0)$ g, almost the same as the pooled-variance result (panel B of the figure in the previous section).

Why use Welch's test by default? The simulation in panel A below gives the answer. When the variances are equal, the Type I error rates of both tests are close to 5% and Welch's test loses almost nothing; when the variances and sample sizes are both unequal, the pooled-variance test can be badly distorted: when the smaller group has the larger variance ($n_1 = 20$, $n_2 = 10$, standard deviation ratio 1:3), the actual Type I error rate is as high as 15%; in the reverse case (the larger group has the larger variance) it is only 1% and the power drops greatly. Welch's test stays near 5% in all situations. The default of R's `t.test` is Welch's test; the default of `scipy.stats.ttest_ind` is the pooled variance, and one must write `equal_var=False`.

![Simulation for two-sample problems (20,000 runs per scenario, nominal level α = 0.05, two-sided). A: actual Type I error rates of the pooled-variance t-test and Welch's t-test when two normal populations have equal means; the horizontal axis gives (n1, n2) and the standard deviation ratio SD1 : SD2. When the smaller group has the larger variance, the pooled-variance test is badly too high (0.146), and in the reverse case badly too low (0.012); Welch's test is always close to 0.05. B: actual Type I error rates of the F test and the Levene test (centered at the median) with equal variances and 25 observations per group; data from the normal, t with 4 degrees of freedom, log-normal and exponential distributions. Once the data are not normal, the error rate of the F test multiplies. Simulated data](./plots/welch-error.py)

## 7.6. Sample Size and Power

### 7.6.1. Two Independent Samples

**Formula 7.6.1 (Sample Size for Comparing Two Means)** When both groups have standard deviation $\sigma$ and equal sample sizes, the sample size per group required for a two-sided test at level $\alpha$ to detect a mean difference $\Delta$ with power $1 - \beta$ is

$$
n = \frac{2\sigma^2 (z_{\alpha/2} + z_\beta)^2}{\Delta^2}.
$$
When the ratio of the group sizes is $k = n_2/n_1$ and the standard deviations are $\sigma_1, \sigma_2$, $n_1 = (\sigma_1^2 + \sigma_2^2/k)(z_{\alpha/2} + z_\beta)^2/\Delta^2$ and $n_2 = k n_1$.

Compared with Formula 6.4.2 of [7.7.6](/7.7.6) there is an extra factor of 2: both group means have sampling error, and the variance of the difference is twice that of a single mean. With $n$ per group and $2n$ in all, the total is 4 times that of a one-sample design; this is the price of having a control and the price of a trustworthy conclusion.

**Example 7.6.1** (a) A randomized trial is to test whether a smoking cessation intervention in pregnancy can raise birth weight by 200 g on average ($\sigma \approx 720$ g, taking the pooled standard deviation of birthwt), two-sided $\alpha = 0.05$ and 80% power: $n = 2 \times 720^2 \times (1.96 + 0.842)^2/200^2 = 203.4$, so 204 per group. (b) If the nutritional supplement of Question 4 of [7.7.6](/7.7.6) (raising birth weight by 100 g, $\sigma = 500$ g) were done as a randomized controlled trial, each group would need $2 \times 500^2 \times 2.802^2/100^2 = 392.5$, that is 393, and 786 in all; the one-sample design needs only 197, but its conclusion is not trustworthy.

When the sample sizes are unequal, among designs with the same total number of people the equally divided one has the highest power; when the control group is easy to obtain and the treated group is expensive, $k = 2$ or 3 can be used, but beyond $k = 4$ the power hardly increases.

### 7.6.2. The Paired Design

**Formula 7.6.2 (Sample Size for the Paired Design)** The number of pairs required for the two-sided paired t-test at level $\alpha$ to detect a mean difference $\Delta$ with power $1 - \beta$ is

$$
n = \frac{\sigma_d^2 (z_{\alpha/2} + z_\beta)^2}{\Delta^2}, \qquad \sigma_d^2 = 2\sigma^2(1 - \rho),
$$
where $\rho$ is the correlation coefficient of the two observations in a pair.

**Example 7.6.2** The standard deviation of a single blood pressure measurement between individuals is about 20 mmHg, and a 10 mmHg antihypertensive effect is to be detected (two-sided 0.05, power 80%). The independent two-group design needs $2 \times 400 \times 2.802^2/100 = 62.8$, that is 63 per group, 126 in all. In the before-and-after paired design, $\rho = 0.5$ requires $400 \times 2.802^2/100 = 31.4$, that is 32; for $\rho = 0.9$ (comparable to the captopril data) $\sigma_d = 8.9$ mmHg and only 7 are needed.

![Why pairing saves participants. A: the number of participants required to detect a mean difference of 10 mmHg (standard deviation of a single reading 20 mmHg, two-sided α = 0.05, power 80%) as a function of the correlation ρ between two readings of the same participant: the paired design (each person measured twice) needs fewer participants as ρ increases, 63, 32 and 7 for ρ = 0, 0.5 and 0.9; two independent groups need 63 + 63 regardless of ρ. B: the ratio of the standard deviation of the paired difference to that of a single reading, √(2(1 − ρ)): at ρ = 0.5 it equals that of a single reading, and for ρ < 0.5 the difference is more uncertain. Normal approximation](./plots/paired-sample-size.py)

These formulas are based on the normal approximation; for small samples one uses the noncentral t distribution (the code of Section 7.9), which gives slightly larger numbers (9 pairs for $\rho = 0.9$ in Example 7.6.2). The $\rho$ is usually taken from a pilot study or the literature, and as with $\sigma$ in Example 6.4.3 of [7.7.6](/7.7.6) it is safer to take a rather conservative value.

## 7.7. Comparison on the Log Scale

Many laboratory indices are positive and right-skewed: concentrations, titers, cell counts, enzyme activities and, to some extent, FEV. They often follow an approximate **log-normal distribution** ([7.7.4](/7.7.4)), and differences between groups appear more naturally as multiples ("30% higher") than as differences. The t-test is then applied to the logarithms of the data, and the results are transformed back to the original scale.

**Formula 7.7.1 (Ratio of Geometric Means)** Let $y = \ln x$, and let the difference of the sample means of $y$ in the two groups be $\bar y_1 - \bar y_2$, with $100(1-\alpha)\%$ confidence interval $(L, U)$ (by the Welch or pooled-variance t method). Then

$$
\exp(\bar y_1 - \bar y_2) = \frac{\mathrm{GM}_1}{\mathrm{GM}_2}
$$
is the ratio of the two **geometric means**, and $(\mathrm{e}^L, \mathrm{e}^U)$ is the confidence interval for the ratio of the population geometric means (for the log-normal distribution also the ratio of the two medians).

**Example 7.7.1** After taking logarithms of FEV, Welch's test gives $t = 8.48$, and the ratio of the geometric means of smokers to nonsmokers is 1.31, with a 95% interval of $(1.23, 1.40)$: the FEV of smoking children is on average 31% higher (again confounded by age). On the log scale the variances of the two groups are also closer than on the original scale: a ratio-type effect (every individual multiplied by the same factor) makes the group with the larger mean also have the larger variance on the original scale, and taking logarithms removes this dependence.

An interval transformed back to the original scale is no longer centered at the point estimate, which is normal. Do not transform the standard error of the mean difference on the log scale back directly, and do not report the "log mean" itself: what readers need is the fold change and its interval.

## 7.8. Decisions for Two-Sample Problems

| Problem | Design | Method | This chapter |
|---|---|---|---|
| Two measurements on the same individual (or matched individuals) | Paired | Paired t-test; Wilcoxon signed-rank test when the differences are skewed or have outliers ([7.7.8](/7.7.8)) | Formula 7.2.1 |
| Two groups of unrelated individuals, continuous outcome | Independent | Welch's t-test (default); the pooled-variance t-test only when the variances are really similar | Formula 7.5.1, Definition 7.3.1 |
| Right-skewed positive values (concentrations, titers) | Either | t-test after log transformation, reporting the geometric mean ratio | Formula 7.7.1 |
| Ordinal outcomes or severely skewed small samples | Either | Wilcoxon rank-sum test, sign test ([7.7.8](/7.7.8)) | — |
| Comparison of two variances | Independent | Levene test (the F test only for truly normal data) | Section 7.4 |
| Binary outcome | Paired / independent | McNemar test / two-proportion test, Fisher's exact test ([7.7.9](/7.7.9)) | — |
| Three or more groups | Independent | Analysis of variance ([7.7.12](/7.7.12)) | — |

Several principles run through the chapter:

- The unit of analysis must match the design. Analyzing paired data as independent samples loses precision (Section 7.2.3); more dangerous is the reverse, treating several measurements on the same animal or several cells in the same culture dish as independent observations, which greatly exaggerates the sample size (pseudoreplication, [7.7.12](/7.7.12)).
- Draw a graph first. A dot plot or box plot immediately shows skewness, outliers and differences between the variances of the two groups ([7.7.2](/7.7.2)); the t-test is sensitive to **outliers**, and suspicious data points should be checked first.
- Report effects and intervals. "$p = 0.009$" is less useful than "infants of smoking mothers were on average 284 g lighter (95% interval 73–495 g)" (Section 6.3 of [7.7.6](/7.7.6)).
- A significant difference between groups is not causation. In an observational comparison of two groups one must consider whether the groups are comparable in other respects (Example 7.3.2).

## 7.9. Computing with Python

```python
import numpy as np
import pandas as pd
from scipy import stats

# paired t test (Example 7.2.1)
before = np.array([210, 169, 187, 160, 167, 176, 185, 206, 173, 146, 174, 201, 198, 148, 154])
after = np.array([201, 165, 166, 157, 147, 145, 168, 180, 147, 136, 151, 168, 179, 129, 131])
res = stats.ttest_rel(before, after)
print(res.statistic, res.pvalue, res.confidence_interval())   # 8.12, 1.1e-6, (13.93, 23.93)
d = before - after
print(stats.ttest_1samp(d, 10, alternative="greater").pvalue)  # H0: mean drop <= 10 mmHg, 0.0009
print(stats.ttest_ind(before, after).pvalue)                   # wrong: ignores pairing, 0.016

# two independent samples (Examples 7.3.1 and 7.5.1)
bw = pd.read_csv("birthwt.csv")
x0, x1 = bw.loc[bw.smoke == 0, "bwt"], bw.loc[bw.smoke == 1, "bwt"]
pooled = stats.ttest_ind(x0, x1)                    # scipy default: pooled variance
welch = stats.ttest_ind(x0, x1, equal_var=False)    # Welch (R's default)
print(pooled.pvalue, pooled.confidence_interval())  # 0.0087, (72.8, 494.8)
print(welch.statistic, welch.df, welch.pvalue)      # 2.73, 170.1, 0.0070
print(stats.levene(x0, x1).pvalue)                  # median-centred (Brown-Forsythe), 0.23
# from summary statistics: ToothGrowth, dose 0.5 mg/d (Example 7.5.1)
print(stats.ttest_ind_from_stats(13.23, 4.46, 10, 7.98, 2.75, 10, equal_var=False))   # t = 3.17, p = 0.0064

# ratio of geometric means (Example 7.7.1)
fev = pd.read_csv("fev.csv")
y1, y0 = np.log(fev.loc[fev.smoke == 1, "fev"]), np.log(fev.loc[fev.smoke == 0, "fev"])
r = stats.ttest_ind(y1, y0, equal_var=False)
ci = r.confidence_interval()
print(np.exp(y1.mean() - y0.mean()), np.exp(ci.low), np.exp(ci.high))   # 1.31, 1.23, 1.40

# sample size (Examples 7.6.1 and 7.6.2)
z = stats.norm.isf
print(2 * 720**2 * (z(0.025) + z(0.2))**2 / 200**2)          # 203.4 per group
from statsmodels.stats.power import TTestIndPower, TTestPower
print(TTestIndPower().solve_power(effect_size=200 / 720, alpha=0.05, power=0.8))   # about 204.4
sd_diff = 20 * np.sqrt(2 * (1 - 0.9))
print(TTestPower().solve_power(effect_size=10 / sd_diff, alpha=0.05, power=0.8))   # about 8.4 pairs
```

## Summary

- The design determines the method (Definition 7.1.1): pairing comes from the same individual or matched individuals and is determined by the design and not by the data; a before-and-after comparison has no control group and is subject to regression to the mean, time trends and placebo effects, and before-and-after comparisons within groups cannot replace comparisons between groups (Section 7.1.3).
- Summary of two-sample t methods:

  | Design and assumption | Statistic | Degrees of freedom | Example |
  |---|---|---|---|
  | Paired | $t = \bar d/(s_d/\sqrt n)$ (Formula 7.2.1) | $n - 1$ | Examples 7.2.1, 7.2.2 |
  | Independent, equal variances | $t = (\bar x_1 - \bar x_2)/(s_p\sqrt{1/n_1 + 1/n_2})$ (Definition 7.3.1) | $n_1 + n_2 - 2$ | Examples 7.3.1, 7.3.2 |
  | Independent, variances may differ (default) | $t = (\bar x_1 - \bar x_2)/\sqrt{s_1^2/n_1 + s_2^2/n_2}$ (Formula 7.5.1) | Satterthwaite $\nu$ | Examples 7.3.3, 7.5.1 |
  | Ratio of variances | $F = s_1^2/s_2^2$ (Formula 7.4.1) | $(n_1 - 1, n_2 - 1)$ | Example 7.4.1 |
  | Log scale | $\exp(\bar y_1 - \bar y_2)$ = ratio of geometric means (Formula 7.7.1) | As above | Example 7.7.1 |

- The gain from pairing comes from the positive correlation within a pair: $\sigma_d^2 = 2\sigma^2(1 - \rho)$. In the captopril data $\rho = 0.90$, the paired analysis gives $p = 10^{-6}$, and wrongly treated as independent samples only 0.016.
- The F test is extremely sensitive to non-normality; the two-step method of "test the variances first, then choose the t-test" is not recommended, Welch's test is the default, and the Levene test is used when the variance itself is the research question.
- Sample size: for two independent groups $2\sigma^2(z_{\alpha/2} + z_\beta)^2/\Delta^2$ per group (Formula 7.6.1), a total 4 times that of a one-sample design; for the paired design $\sigma_d^2(z_{\alpha/2} + z_\beta)^2/\Delta^2$ pairs (Formula 7.6.2).
- The main thread: infants of smoking mothers are on average 284 g lighter (95% interval 73–495 g, $p = 0.009$); the higher FEV of smoking children by 0.71 L ($p = 2 \times 10^{-10}$) is a paradox produced by age and disappears when compared within age groups: the test is correct and the problem lies in the design, with adjustment methods in [7.7.10](/7.7.10).

## Questions

1. Decide whether a paired or an independent two-sample method should be used in each study, and explain why: (a) comparing the bone density of the smoking and nonsmoking twin in each of 30 pairs of identical twins; (b) randomly assigning 40 patients to a new drug or a standard drug and comparing hemoglobin after treatment; (c) measuring blood glucose in the same 25 blood samples with two instruments; (d) randomizing 200 hypertensive patients into a diet intervention group (102) and an exercise intervention group (98), measuring blood pressure once before and once after the intervention, and comparing the antihypertensive effects of the two interventions.

   **Answer** (a) Paired: each pair of twins shares genetic background and upbringing, and the basis of pairing comes from the design. (b) Independent: the two groups are different patients with no correspondence. (c) Paired: the two measurements of the same blood sample correspond to each other, and comparing the two instruments should use the differences (a method comparison should also draw a Bland–Altman plot, [7.7.11](/7.7.11)). (d) Independent two samples: compute each patient's own change (after minus before) and compare the changes of the two groups with the independent two-sample t-test (Welch). One must not do a separate paired t-test in each group and then compare p-values: both groups would be "significant", but this does not show which intervention is better (Section 7.1.3).

2. Using the captopril data of Example 7.2.1 ($\bar d = 18.93$, $s_d = 9.03$, $n = 15$): (a) find the 99% confidence interval for the mean decrease; (b) test at one-sided $\alpha = 0.05$ whether the mean decrease exceeds 15 mmHg; (c) explain the relation between the result of (b) and the 99% interval.

   **Answer** (a) $t_{14, 0.005} = 2.977$, and the interval is $18.93 \pm 2.977 \times 2.331 = (11.99, 25.87)$ mmHg. (b) $t = (18.93 - 15)/2.331 = 1.69$ with 14 degrees of freedom, one-sided $p = \mathbb{P}(t_{14} \ge 1.69) = 0.057$; at the 0.05 level the hypothesis that "the mean decrease does not exceed 15 mmHg" is not rejected. (c) A one-sided test at level 0.05 corresponds to the lower limit of the 90% two-sided interval ($18.93 - 1.761 \times 2.331 = 14.82$); the lower limit is slightly below 15, consistent with $p$ being slightly above 0.05; the 99% interval is wider and its lower limit 12.0 is far below 15. The data are sufficient to show a decrease of more than 10 mmHg (Example 7.2.1) but not more than 15 mmHg.

3. In ToothGrowth the two groups at 1 mg/d each have 10 guinea pigs: the orange juice group has mean 22.70 and standard deviation 3.91, and the ascorbic acid group 16.77 and 2.52. Compare the two groups with the pooled-variance t-test and with Welch's test, and explain why the two statistics are the same but the p-values differ.

   **Answer** The pooled variance is $s_p^2 = (3.91^2 + 2.52^2)/2 = 10.81$, $s_p = 3.288$, the standard error is $3.288\sqrt{2/10} = 1.470$, $t = 5.93/1.470 = 4.03$ with 18 degrees of freedom, and $p = 0.0008$. Welch: the standard error is $\sqrt{3.91^2/10 + 2.52^2/10} = \sqrt{1.530 + 0.633} = 1.470$, likewise $t = 4.03$; the degrees of freedom are $2.163^2/(1.530^2/9 + 0.633^2/9) = 15.36$ and $p = 0.0010$. When $n_1 = n_2$, $s_p^2(1/n_1 + 1/n_2) = (s_1^2 + s_2^2)/n = s_1^2/n_1 + s_2^2/n_2$, so the two standard errors are identical and the difference lies only in the degrees of freedom of the reference distribution: Welch's test takes into account that the uncertainty of the variance estimate comes mainly from the group with the larger variance, so the degrees of freedom are smaller and the p-value slightly larger. A design with equal sample sizes is therefore the least sensitive to unequal variances, which is one of the reasons to make the groups equal in experimental design.

4. Using the birthwt data (nonsmokers 115, mean 3055.7 g, standard deviation 752.7; smokers 74, 2771.9 g, 659.6), compute by hand the degrees of freedom of Welch's test and explain why it is close to 187 rather than close to 73.

   **Answer** $s_1^2/n_1 = 752.7^2/115 = 4926.6$, $s_2^2/n_2 = 659.6^2/74 = 5879.4$, and the sum is 10,806.0 (standard error 103.95). $\nu = 10\,806.0^2/(4926.6^2/114 + 5879.4^2/73) = 1.1677 \times 10^8/(212\,906 + 473\,524) = 170.1$. The $s^2/n$ of the two groups are similar in size (4927 and 5879), and the Welch degrees of freedom are then close to $n_1 + n_2 - 2 = 187$ of the pooled-variance test; only when the $s^2/n$ of one group is much larger than that of the other does $\nu$ approach $n - 1$ of that group. $t = 283.8/103.95 = 2.73$ and $p = 0.007$.

5. Use the simulation results of Section 7.5 to explain why the pooled-variance t-test rejects $H_0$ too often when the smaller group has the larger variance.

   **Answer** The pooled variance is weighted by degrees of freedom and is determined mainly by the larger sample. If the larger group has the smaller variance, $s_p^2$ is close to the smaller variance and underestimates the true $\operatorname{Var}(\bar x_1 - \bar x_2) = \sigma_1^2/n_1 + \sigma_2^2/n_2$, of which the smaller group (large variance, small $n$) contributes most. The standard error is underestimated, $\lvert t\rvert$ is too large and the Type I error rate rises (0.146 in the simulation with $n_1 = 20$, $n_2 = 10$ and standard deviation ratio 1:3). In the reverse case, when the larger group has the larger variance, $s_p^2$ overestimates the standard error, and the test is too conservative (0.012) with reduced power. Welch's test estimates each $s_j^2/n_j$ separately and has no such bias.

6. A randomized trial plans to compare the reduction in systolic pressure produced by two antihypertensive drugs, with an expected difference of 5 mmHg and a standard deviation of the reduction of 12 mmHg. (a) With two-sided $\alpha = 0.05$ and 90% power, how many are needed per group? (b) If 15% of the participants are expected to be lost to follow-up, how many should be recruited? (c) If a crossover design is used instead (each participant takes the two drugs in succession with a washout period between), and the correlation between the effects of the two drugs is estimated as 0.6, how many participants are needed?

   **Answer** (a) $n = 2 \times 12^2 \times (1.96 + 1.282)^2/5^2 = 288 \times 10.51/25 = 121.1$, so 122 per group. (b) $122/0.85 = 143.5$, so 144 per group are recruited, 288 in all. (c) $\sigma_d^2 = 2 \times 144 \times 0.4 = 115.2$ and $n = 115.2 \times 10.51/25 = 48.4$, so 49 participants. The crossover design greatly reduces the number of people but requires a stable disease, reversible drug effects and a washout period long enough to remove carryover ([7.7.17](/7.7.17)).

7. The serum concentrations of a cytokine (pg/mL) in two groups of mice are highly right-skewed. After log transformation, the difference of the mean log concentrations between the treated and control groups is 0.405, with a 95% confidence interval of (0.10, 0.71). Translate the result into a conclusion on the original scale.

   **Answer** The ratio of geometric means is $\mathrm{e}^{0.405} = 1.50$, with a 95% interval of $(\mathrm{e}^{0.10}, \mathrm{e}^{0.71}) = (1.11, 2.03)$: the cytokine concentration of the treated group (geometric mean, also the median for the log-normal distribution) is on average 1.5 times that of the control group, and the data are compatible with anything from 11% to about 2 times higher. The interval does not contain 1, and the difference is significant at the 0.05 level. This is not a ratio of arithmetic means; the arithmetic mean of right-skewed data is strongly influenced by a few high values.

8. A paper reports: smokers FEV $3.28 \pm 0.75$ L ($n = 65$), nonsmokers $2.57 \pm 0.85$ L ($n = 589$), $p < 0.001$, "suggesting that smoking is associated with improved lung function in adolescents". (a) Was the p-value miscalculated? (b) Point out the problems of the conclusion and propose two more reasonable analyses.

   **Answer** (a) It is not miscalculated: the two-sample t-test gives $t = 6.46$, $p = 2 \times 10^{-10}$ (Welch $p = 3 \times 10^{-10}$), and the difference is not due to chance. (b) The two groups differ in age by 4 years, and FEV grows with age and height: smoking is confounded with age, and the "improvement" is caused by age. More reasonable analyses: (1) stratified comparison, comparing smokers and nonsmokers among children of the same age or height (in Example 7.3.2 the FEV of smokers is mostly lower in same-age comparisons); (2) multiple linear regression adjusting simultaneously for age, height and sex and estimating the partial regression coefficient of smoking ([7.7.10](/7.7.10), where the coefficient becomes negative). A better design is a longitudinal study: compare the rate of growth of FEV thereafter in children who start smoking and those who do not.

9. (Design question) You want to evaluate whether a new local anesthetic cream reduces the pain of venipuncture (visual analogue scale 0–100). Write down two feasible designs and their methods of analysis and compare their strengths and weaknesses.

   **Answer** Design 1: a parallel-group randomized controlled trial, randomizing participants to the cream or a placebo cream, double-blind, with pain scored after the puncture; compare the group means with Welch's t-test (the Wilcoxon rank-sum test if the scores are skewed). Its strength is simplicity and the absence of carryover; its weakness is that individuals differ greatly in sensitivity to pain, and many participants are needed. Design 2: on the same participant the cream and the placebo are randomly assigned to the two arms (a self-controlled paired design), with one puncture per arm; analyze the differences between the scores of the two arms with the paired t-test. Its strength is control of the individual's pain sensitivity: if the correlation of the scores of the two arms is $\rho$, the number of participants needed is about $(1 - \rho)/2$ of the total in the parallel design; its weaknesses are that the order of the two punctures may affect the scores (the second may be more anxious or more habituated), so the order should be randomized, and that the creams on the two arms may be confused (participants can tell them apart), making it harder to maintain blinding. Both designs must specify in advance the minimal clinically meaningful difference (such as 10 points) and compute the sample size.

10. A laboratory compares the body weights of wild-type and knockout mice, with 3 mice of each genotype, each weighed 5 times, 15 + 15 data in all, and obtains $p = 0.001$ from the two-sample t-test. What is wrong with this analysis? How should it be analyzed?

    **Answer** The 5 weighings of the same mouse are not independent observations: they reflect the technical error of weighing and not the biological variation between mice. Treating the 30 data as independent samples is like pretending that each group has 15 mice; the standard error is badly underestimated and the p-value is far too small (pseudoreplication). The correct unit of analysis is the mouse: first compute the mean of the 5 weighings of each mouse, then do the two-sample t-test on the 3 means per group (about 4 degrees of freedom). The conclusion is then likely to be no longer significant: a study with 3 animals per group has very low power, and one should increase the number of animals rather than the number of measurements on the same animal ([7.7.12](/7.7.12), [7.7.17](/7.7.17)).
