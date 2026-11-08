---
title: "Hypothesis Testing: One-Sample Inference"
description: The logic of hypothesis testing (the jury analogy, null and alternative hypotheses, the two types of error, significance level, critical values and p-values, one- and two-sided tests); z and t tests for a normal mean; the duality of tests and confidence intervals; power and sample size; the chi-square test for a normal variance; one-sample binomial and Poisson tests and the standardized mortality ratio; misuses of the p-value, effect sizes and the ASA statement. Illustrated with the birth weight of a low-income population, cholesterol in immigrants, low birth weight among smoking mothers and an occupational cohort.
source_hash: 7cc7e043b49c
---

[7.7.5](/7.7.5) used confidence intervals to answer "roughly what is the parameter". Many research questions, however, take the form "whether": is the mean birth weight of newborns in a low-income region lower than the national level? Is the risk of low birth weight higher among smoking mothers than among nonsmoking mothers? Do rubber workers die of bladder cancer more often than the general population? **Hypothesis testing** provides the standard procedure for answering such questions: first assume "no difference", then see how far the data are from this assumption, and use probability to measure whether the departure is too large to be explained by chance. This chapter treats the situation with a single sample compared with a known reference value, one-sample inference: the z test and t test for a mean, the chi-square test for a variance, the binomial test for a proportion, and the Poisson test for counts and the standardized mortality ratio. The logic of testing (the two types of error, the p-value, power) is worked out thoroughly here, and the tests in all later chapters follow the same logic. The chapter also discusses the commonest misuses of the p-value: statistical significance does not imply importance, and nonsignificance does not imply no difference. The mathematical theory of testing (the Neyman–Pearson lemma, likelihood ratio tests, uniformly most powerful tests) is in [3.2.5](/3.2.5); two-group comparisons are in [7.7.7](/7.7.7), and the problems of carrying out thousands of tests at once are in [7.7.20](/7.7.20).

## 6.1. The Logic of Testing

### 6.1.1. The Jury Analogy

A criminal trial is a good metaphor for a hypothesis test. The defendant is presumed innocent, and the prosecution must present evidence showing guilt "beyond a reasonable doubt"; when the evidence is insufficient the jury pronounces "not guilty", which is not the same as pronouncing "innocent" and says only that the evidence is insufficient for conviction. A trial can make two kinds of error: convicting the innocent, or letting the guilty go free. The law fears the former more and therefore sets a high threshold for conviction, at the price that some guilty people go free.

| Trial | Hypothesis test |
|---|---|
| Presumption of innocence | Null hypothesis $H_0$ (no difference, no effect) |
| Guilt | Alternative hypothesis $H_1$ |
| Evidence | The data, summarized as a test statistic |
| "Beyond a reasonable doubt" | Significance level $\alpha$ (such as 0.05) |
| Convicting the innocent | Type I error |
| Letting the guilty go free | Type II error |
| "Not guilty" is not "innocent" | "Failing to reject $H_0$" is not "$H_0$ is true" |

### 6.1.2. Null and Alternative Hypotheses

The **null hypothesis** $H_0$ is the hypothesis being tested, usually expressing "no difference" or "equal to some known value", the skeptic's position; the **alternative hypothesis** $H_1$ is the conclusion that the investigator hopes to find evidence for. The two are mutually exclusive.

**Example 6.1.1 (Birth weight in a low-income population)** To study whether mothers of low socioeconomic status are more likely to have underweight infants, investigators collected the birth weights of 100 consecutive full-term live births in the delivery room of a hospital in a low-income area, with a mean of 115 oz (3260 g) and a standard deviation of 24 oz (680 g). The mean birth weight of newborns nationally is 120 oz (3402 g). The question is whether the mean birth weight $\mu$ of the population served by this hospital is lower than the national level:

$$
H_0\colon \mu = 120 \quad \text{vs.} \quad H_1\colon \mu < 120.
$$

The sample mean of 115 is below 120, but this may be only sampling error: even when 100 infants are drawn from a population with mean 120, the sample mean will not be exactly 120. The test must answer: if $H_0$ is true, how unusual is a sample mean of 115 or lower?

### 6.1.3. The Two Types of Error and the Significance Level

| | $H_0$ true | $H_0$ false |
|---|---|---|
| Fail to reject $H_0$ | Correct | Type II error (probability $\beta$) |
| Reject $H_0$ | Type I error (probability $\alpha$) | Correct (probability $1 - \beta$, the power) |

**Definition 6.1.1 (Types of Error and Significance Level)** Rejecting $H_0$ when it is true is a **Type I error** (false positive), and failing to reject $H_0$ when it is false is a **Type II error** (false negative). The maximum probability $\alpha$ of a Type I error that the test allows, specified in advance, is the **significance level**.

Compare with the diagnostic tests of [7.7.3](/7.7.3): regard "rejecting $H_0$" as a positive test and "$H_0$ false" as disease; then $\alpha = 1 - {}$specificity and $\beta = 1 - {}$sensitivity. Just as sensitivity and specificity trade off in diagnosis, $\alpha$ and $\beta$ trade off for a fixed sample size: the stricter the threshold (the smaller $\alpha$), the harder it is to reject $H_0$ and the more Type II errors there are. To reduce both at once the sample size must be increased.

By convention $\alpha = 0.05$ is used, and 0.01 or less when a Type I error has serious consequences ($5 \times 10^{-8}$ in GWAS, [7.7.20](/7.7.20)). There is no deep reason for 0.05; it is a convenient convention proposed by Fisher in the 1920s.

### 6.1.4. Test Statistic, Critical Value and p-Value

A test compresses the data into a **test statistic** whose distribution under $H_0$ is known. In Example 6.1.1, if $H_0$ is true, then by the central limit theorem of [7.7.4](/7.7.4) the sample mean is approximately $\mathcal{N}(120, \sigma^2/n)$, and approximating $\sigma$ by 24,

$$
z = \frac{\bar x - \mu_0}{\sigma/\sqrt n} = \frac{115 - 120}{24/\sqrt{100}} = -2.08.
$$
The sample mean is 2.08 standard errors below its expectation under $H_0$. There are two equivalent ways to decide whether to reject $H_0$.

- Critical value method: under $H_0$, the probability that $z$ falls in $(-\infty, -z_{0.05}] = (-\infty, -1.645]$ is 0.05. This region is the **rejection region**, and $-1.645$ is the **critical value**. Since $z = -2.08$ lies in the rejection region, $H_0$ is rejected at $\alpha = 0.05$.
- p-value method: compute the probability, under $H_0$, of a result as extreme as or more extreme than the one observed, $\Phi(-2.08) = 0.019$. It is smaller than $\alpha$, so $H_0$ is rejected.

**Definition 6.1.2 (p-Value)** The probability, computed on the assumption that the null hypothesis is true, that the test statistic takes a value as extreme as or more extreme than the observed one is the **p-value**. When $p \le \alpha$, $H_0$ is rejected at level $\alpha$ and the result is said to be "statistically significant at level $\alpha$".

The p-value provides more information than "reject / do not reject": $p = 0.049$ and $p = 0.0001$ are both "significant", yet the strength of evidence differs enormously. The meaning of the p-value must be understood precisely: it is not the probability that $H_0$ is true (Section 6.8).

### 6.1.5. One-Sided and Two-Sided Tests

The $H_1\colon \mu < 120$ of Example 6.1.1 is concerned with one direction only and is a **one-sided test**; if the question were "is the birth weight of this population different from the national one", $H_1\colon \mu \ne 120$ would be a **two-sided test**, with the rejection region taking $\alpha/2$ on each side and the p-value twice the one-sided value: $2 \times 0.019 = 0.037$.

A one-sided test rejects $H_0$ more easily at the same $\alpha$, so it must be chosen before seeing the data and on the basis of the research question: a one-sided test is used only when a result in the other direction is meaningless or impossible (for example, a new screening protocol will be adopted only if it is better than the existing one). Deciding to carry out the one-sided test of $H_1\colon \mu < 120$ only after seeing $\bar x < 120$ gives an actual Type I error rate of 10% rather than 5%. Most medical studies, especially evaluations of new therapies, conventionally use two-sided tests: a new therapy may also be harmful, and harm too needs to be detected.

### 6.1.6. Steps of a Test

1. Write $H_0$ and $H_1$ according to the research question and decide between one-sided and two-sided;
2. Specify the significance level $\alpha$ in advance;
3. Choose the test, check its premises (type of data, distribution, independence) and compute the test statistic;
4. Find the p-value (or compare with the critical value);
5. State the statistical conclusion, translate it into the language of the research question, and report the size of the effect with a confidence interval (Sections 6.3 and 6.8).

## 6.2. Tests for a Normal Mean

### 6.2.1. The z Test

**Formula 6.2.1 (One-Sample z Test)** Suppose the sample comes from a normal population (or $n$ is large enough) and the population standard deviation $\sigma$ is known. The statistic for testing $H_0\colon \mu = \mu_0$ is

$$
z = \frac{\bar x - \mu_0}{\sigma/\sqrt n},
$$
which follows $\mathcal{N}(0, 1)$ under $H_0$. The two-sided p-value is $2[1 - \Phi(\lvert z\rvert)]$; for the one-sided $H_1\colon \mu < \mu_0$ it is $\Phi(z)$, and for $H_1\colon \mu > \mu_0$ it is $1 - \Phi(z)$.

Situations in which $\sigma$ is truly known are few: a standardized assay with long-term quality control data, or a very large reference population. Most of the time $\sigma$ must be estimated from the same sample, and the t test should be used.

### 6.2.2. The t Test

**Formula 6.2.2 (One-Sample t Test)** Suppose the sample comes from a normal population and $\sigma$ is unknown and replaced by the sample standard deviation $s$. The statistic for testing $H_0\colon \mu = \mu_0$ is

$$
t = \frac{\bar x - \mu_0}{s/\sqrt n},
$$
which follows the **t-distribution** with $n - 1$ degrees of freedom under $H_0$. The p-value and critical values are computed from the $t_{n-1}$ distribution.

In Example 6.1.1 the $\sigma$ was in fact estimated by the 24 oz of the sample, and strictly the t test should be used: $t = -2.08$ with 99 degrees of freedom gives a one-sided $p = 0.020$, almost the same as the 0.019 of the z test. The difference becomes marked only for small samples: for $n = 10$, $t_{9, 0.025} = 2.262$ whereas $z_{0.025} = 1.960$.

**Example 6.2.1 (Serum cholesterol in immigrants)** The mean serum cholesterol of US women aged 21–40 is 190 mg/dL. One hundred recent Asian immigrant women of the same age range are drawn at random, with mean cholesterol 181.52 mg/dL and standard deviation 40 mg/dL. Is their mean cholesterol different from that of the general US population? The two-sided test of $H_0\colon \mu = 190$:

$$
t = \frac{181.52 - 190}{40/\sqrt{100}} = -2.12, \qquad p = 2\,\mathbb{P}(t_{99} \le -2.12) = 0.037.
$$
$H_0$ is rejected at $\alpha = 0.05$: the mean cholesterol of the immigrant women is lower than that of the general US population. If the same mean and standard deviation came from 200 women, $t = -3.00$ and $p = 0.003$, much stronger evidence: for a difference of the same size, the larger the sample, the more easily it is significant.

**Example 6.2.2 (Birth weight of infants of smoking mothers)** In the birthwt data the 74 infants of smoking mothers have a mean birth weight of 2771.9 g with a standard deviation of 659.6 g. Taking 3400 g (close to the national mean of 120 oz in Example 6.1.1) as the reference value,

$$
t = \frac{2771.9 - 3400}{659.6/\sqrt{74}} = \frac{-628.1}{76.7} = -8.19, \qquad \text{one-sided } p = 3 \times 10^{-12}.
$$
The result is extremely significant but hard to interpret: birthwt comes from pregnant women treated at one medical center, and the infants of nonsmoking mothers have a mean of only 3056 g, also far below 3400 g. A comparison with an external reference value confounds the effect of smoking with the characteristics of this sample's population (socioeconomic status, racial composition, the catchment of this hospital). To isolate the effect of smoking one should compare smoking and nonsmoking mothers within the same sample, which is the two-sample t test of [7.7.7](/7.7.7). A one-sample test is appropriate only when the reference value truly applies to the population studied.

The premises of the t test are independent observations and a normal population. Thanks to the central limit theorem it is quite robust to non-normality when $n$ is large; when $n$ is small and the data are clearly skewed or contain outliers, one can transform the data first (such as by taking logarithms) or use the sign test or the Wilcoxon signed-rank test ([7.7.8](/7.7.8)). A violation of independence (repeated measurements on the same person, members of the same family) is not compensated by a large sample.

### 6.2.3. Using Tables

Without software, one can look up a t table. Each row of the table is a degree of freedom and each column an upper (or two-sided) probability, and the entries are the corresponding quantiles. When reading a table, first confirm whether the heading gives a one-sided or two-sided probability, and whether it is the upper quantile $t_{\nu,\alpha}$ ($\mathbb{P}(t_\nu > t_{\nu,\alpha}) = \alpha$) or the lower quantile (some tables write $t_{\nu, 1-\alpha}$, the same number). Example: for $\nu = 9$ the one-sided 0.05 critical value is 1.833 and the two-sided 0.05 (0.025 on each side) critical value is 2.262; for $\nu = 99$ the two-sided 0.05 critical value is 1.984. If the degrees of freedom are not in the table, take the adjacent smaller row (conservative). When the observed $\lvert t\rvert$ lies between two columns, the p-value also lies between the probabilities of those two columns: for $\nu = 99$ and $\lvert t\rvert = 2.12$, which lies between the two-sided 0.05 (1.984) and 0.02 (2.365) critical values, $0.02 < p < 0.05$. When software is used, report the exact p-value.

## 6.3. Tests and Confidence Intervals

**Theorem 6.3.1 (Duality of Tests and Confidence Intervals)** For a normal mean, the two-sided t test at level $\alpha$ rejects $H_0\colon \mu = \mu_0$ if and only if $\mu_0$ is not within the $100(1 - \alpha)\%$ confidence interval $\bar x \pm t_{n-1,\alpha/2}\, s/\sqrt n$ for $\mu$.

**Proof** $H_0$ is not rejected $\iff$ $\lvert\bar x - \mu_0\rvert/(s/\sqrt n) < t_{n-1,\alpha/2}$ $\iff$ $\bar x - t_{n-1,\alpha/2}\, s/\sqrt n < \mu_0 < \bar x + t_{n-1,\alpha/2}\, s/\sqrt n$. $\square$

In other words, the confidence interval is the set of all parameter values that the test would not reject (the general duality is in [3.2.5](/3.2.5)). In Example 6.2.1 the 95% confidence interval for the cholesterol of the immigrant women is $181.52 \pm 1.984 \times 4 = (173.6, 189.5)$ mg/dL, which does not contain 190, consistent with $p = 0.037 < 0.05$.

The interval provides more information than the test: it says both whether the result is significant (whether it contains $\mu_0$) and how large the effect may be and how precisely it is estimated. "The mean is 8.5 mg/dL below the reference value, 95% interval 0.5–16.4" is far more useful than "$p = 0.037$": the reader can judge whether the most likely difference is clinically important and can see that the data are compatible with both a very small difference (0.5) and a fairly large one (16). Modern reporting guidelines therefore require effect estimates with confidence intervals as the main result and p-values as secondary.

## 6.4. Power and Sample Size

### 6.4.1. Power

**Definition 6.4.1 (Power)** The probability that the test rejects $H_0$ when a given parameter value in the alternative hypothesis is true is the **statistical power** of the test at that parameter value, equal to $1 - \beta$. As a function of the parameter value, it is the **power function** of the test ([3.2.5](/3.2.5)).

Power answers: if there really is an effect of a given size, how likely is the study to find it? A study with low power is likely to produce a "nonsignificant" result even when the effect is real.

**Formula 6.4.1 (Power of the z Test)** The power of the one-sided z test ($H_1\colon \mu < \mu_0$, level $\alpha$) at the true value $\mu_1 < \mu_0$ is

$$
1 - \beta = \Phi\!\left(\frac{(\mu_0 - \mu_1)\sqrt n}{\sigma} - z_\alpha\right);
$$
the power of the two-sided test is approximately $\Phi\!\left(\frac{\lvert\mu_0 - \mu_1\rvert\sqrt n}{\sigma} - z_{\alpha/2}\right)$ (ignoring the very small probability of rejection on the other side).

**Example 6.4.1** In Example 6.1.1, if the true mean of the population is indeed 115 oz ($\sigma = 24$), the power of the one-sided test with $n = 100$ is $\Phi(5 \times 10/24 - 1.645) = \Phi(0.438) = 0.67$: there is a one-third chance of a nonsignificant result. If only 10 infants were collected, the power would fall to $\Phi(5\sqrt{10}/24 - 1.645) = \Phi(-0.986) = 0.16$, and a false negative conclusion would be almost certain.

![Type I and Type II errors and power of a one-sided z test: mean birth weight of a low-income population, H0: μ = 120 oz versus H1: μ < 120 oz, σ = 24 oz, α = 0.05. The two curves are the sampling distributions of the sample mean under H0 (μ = 120) and under the alternative μ = 115. A: n = 100, standard error 2.4 oz, H0 is rejected when the sample mean is below 116.05 oz, and the power is 0.67. B: n = 10, standard error 7.6 oz, and the same difference is detected with probability only 0.16. Exact normal computation](./plots/errors-power.py)

### 6.4.2. Four Determinants of Power

By Formula 6.4.1, power increases with:

- the effect size $\lvert\mu_0 - \mu_1\rvert$: the larger the difference, the easier it is to detect;
- the sample size $n$: power grows with $\sqrt n$;
- the significance level $\alpha$: the larger $\alpha$, the looser the critical value and the higher the power (at the price of more Type I errors);
- the variability of the data $\sigma$: the smaller the better; improving measurement, choosing homogeneous participants and the paired design ([7.7.7](/7.7.7)) can all reduce it.

A one-sided test has higher power than a two-sided test in the right direction, but this is no reason to choose a one-sided test (Section 6.1.5).

![Power and sample size for tests of a normal mean. A: power of the one-sided z test of H0: μ = 120 oz (σ = 24 oz, α = 0.05) as a function of the true mean, for n = 10, 25 and 100; at μ = 120 every curve equals α, and the dots are the power at the true mean of 115 oz. B: sample size required for 80% and 90% power of the two-sided z test (α = 0.05) as a function of the standardized difference Δ/σ (logarithmic axes); for Δ/σ = 0.2, 0.5 and 0.8, 80% power requires 197, 32 and 13 subjects, respectively. Exact normal computation](./plots/power-curves.py)

### 6.4.3. Sample Size

When designing a study, specify the smallest meaningful difference $\Delta$ to be detected, the significance level $\alpha$ and the desired power $1 - \beta$, and work back to the sample size.

**Formula 6.4.2 (Sample Size for a One-Sample Test of a Mean)** The sample size required for the two-sided z test to detect a difference $\Delta = \lvert\mu_1 - \mu_0\rvert$ with power $1 - \beta$ is

$$
n = \frac{\sigma^2 (z_{\alpha/2} + z_\beta)^2}{\Delta^2},
$$
and for a one-sided test $z_{\alpha/2}$ is replaced by $z_\alpha$. Round up the result.

Common values of $z_\beta$: for 80% power $z_{0.2} = 0.842$ and for 90% $z_{0.1} = 1.282$.

**Example 6.4.2** To detect, with 90% power and two-sided $\alpha = 0.05$, a change in the mean weight of men aged 20–29 from 170 lb (77 kg) to 190 lb ($\sigma = 40$ lb), we need $n = 40^2(1.96 + 1.282)^2/20^2 = 42.03$, which rounds up to 43 people. In Example 6.1.1, to detect a difference of 5 oz with 80% power (one-sided) we need $24^2(1.645 + 0.842)^2/5^2 = 142.5$, that is 143 infants; 90% power needs 198.

**Example 6.4.3 (Pilot study and the uncertainty of $\sigma$)** In a pilot study of a new drug to lower intraocular pressure, 10 patients with high intraocular pressure had a mean decrease of 5 mmHg after 1 month of treatment, with a standard deviation of 10 mmHg. The investigators plan to test in the main trial whether the mean decrease differs from 0. If the true decrease is 5 mmHg and $\sigma = 10$, 80% power and two-sided $\alpha = 0.05$ need $10^2(1.96 + 0.842)^2/5^2 = 31.4$, that is 32 people; the planned 100 people would have a power of 0.999. But $\sigma$ was estimated from only 10 people, and the upper limit of its 95% confidence interval is $\sqrt{9 \times 100/2.70} = 18.3$ mmHg (Formula 5.5.1 of [7.7.5](/7.7.5)); if the true $\sigma$ were that large, 105 people would be needed. A sample size computed from the standard deviation of a small pilot study is often too optimistic, and a common practice is to take the upper limit of the confidence interval of the standard deviation, or to compute for several plausible values of $\sigma$.

### 6.4.4. Nonsignificant Does Not Mean No Difference

A study with power of only 16% (Example 6.4.1 with $n = 10$) that obtains "$p > 0.05$" says almost nothing. "No evidence of a difference" (absence of evidence) is not "evidence of no difference" (evidence of absence), one of the most common misreadings in the medical literature. To judge whether a negative result is informative, look at the confidence interval: if the interval is narrow and contains only clinically unimportant differences, one can say that "the difference, if present, is small"; if it is wide and contains both 0 and very large differences, the only conclusion is "the data are insufficient". "Post hoc power" computed from the observed effect provides no information beyond the p-value and should not be used. To demonstrate "no difference" formally, an equivalence test is needed ([7.7.18](/7.7.18)).

## 6.5. Tests for a Normal Variance

Questions such as the precision of an assay and the stability of a production process require testing the variance itself.

**Formula 6.5.1 (Chi-Square Test for a Variance)** Suppose the sample comes from a normal population. The statistic for testing $H_0\colon \sigma^2 = \sigma_0^2$ is

$$
X^2 = \frac{(n - 1)s^2}{\sigma_0^2},
$$
which follows $\chi^2_{n-1}$ under $H_0$. The two-sided test rejects $H_0$ when $X^2 < \chi^2_{n-1, 1-\alpha/2}$ or $X^2 > \chi^2_{n-1, \alpha/2}$; the p-value is $2\min\{\mathbb{P}(\chi^2_{n-1} \le X^2), \mathbb{P}(\chi^2_{n-1} \ge X^2)\}$.

**Example 6.5.1 (The new blood pressure monitor)** In Example 5.5.1 of [7.7.5](/7.7.5), the sample variance of the differences between the two observers' readings with the new ultrasound monitor is $s^2 = 8.178$ ($n = 10$). The variance of the interobserver differences for the standard sphygmomanometer is known to be 35. Does the variation of the new instrument differ from that of the standard?

$$
X^2 = \frac{9 \times 8.178}{35} = 2.10 < \chi^2_{9, 0.975} = 2.70,
$$
and the two-sided $p = 2\,\mathbb{P}(\chi^2_9 \le 2.10) = 0.021$, so $H_0$ is rejected at $\alpha = 0.05$: the interobserver variation of the new instrument is smaller than that of the standard. This agrees with the conclusion of [7.7.5](/7.7.5): the 95% confidence interval $(3.87, 27.26)$ for the variance does not contain 35.

![Exact one-sample tests. A: bladder cancer deaths in a cohort of rubber workers (Andjelkovic et al. 1976): 21 observed, 18.1 expected from general population mortality. The bars are the Poisson(18.1) distribution, and the two-sided p-value is twice the right tail from 21 upward (shaded), p = 0.55, standardized mortality ratio 116%. B: the variance of the differences between two observers' readings with the new blood pressure monitor, s² = 8.178 (n = 10), compared with the variance 35 of the standard instrument: the statistic (n − 1)s²/35 = 2.10 is below the lower 2.5% quantile 2.70 of the chi-square distribution with 9 degrees of freedom (shaded rejection region), two-sided p = 0.021](./plots/exact-tests.py)

Unlike the t test for a mean, the chi-square test for a variance is very sensitive to the normality assumption: when the population has heavy tails, the actual Type I error rate can be far above $\alpha$ even for a large sample. Normality must be checked first (the QQ plots of [7.7.2](/7.7.2)), and when in doubt a bootstrap interval should be used (Section 5.10 of [7.7.5](/7.7.5)).

## 6.6. The One-Sample Binomial Test

### 6.6.1. The Normal Approximation

**Formula 6.6.1 (z Test for a Proportion)** Let $X \sim \mathrm{Bin}(n, p)$ and $\hat p = x/n$. For testing $H_0\colon p = p_0$ when $np_0(1 - p_0) \ge 5$, the statistic

$$
z = \frac{\hat p - p_0}{\sqrt{p_0(1 - p_0)/n}}
$$
is approximately $\mathcal{N}(0, 1)$ under $H_0$. Note that the standard error uses $p_0$ under $H_0$, not $\hat p$.

**Example 6.6.1 (Low birth weight among smoking mothers)** In Example 4.2.3 of [7.7.4](/7.7.4), 30 of 74 smoking mothers had low birth weight infants ($\hat p = 0.405$), with the proportion of nonsmoking mothers $p_0 = 0.252$ as the reference. Here $np_0(1 - p_0) = 13.96 \ge 5$, and

$$
z = \frac{0.405 - 0.252}{\sqrt{0.252 \times 0.748/74}} = 3.04, \qquad \text{one-sided } p = 0.0012.
$$
With the continuity correction (subtracting $0.5/n$ from the numerator) $z = 2.90$ and $p = 0.0019$; the exact binomial probability is $\mathbb{P}(X \ge 30) = 0.0027$ ([7.7.4](/7.7.4)). Even with $np_0(1-p_0)$ as large as 14, the normal approximation underestimates the p-value in the right tail by more than half; for samples of moderate size one should use the exact test directly. As noted before, 0.252 is treated here as a known constant, and the correct two-group comparison is in [7.7.9](/7.7.9).

### 6.6.2. The Exact Test

**Formula 6.6.2 (Exact Binomial Test)** Under $H_0\colon p = p_0$, $X \sim \mathrm{Bin}(n, p_0)$. If $\hat p > p_0$ the one-sided p-value is $\mathbb{P}(X \ge x)$; if $\hat p < p_0$ it is $\mathbb{P}(X \le x)$. Two definitions of the two-sided p-value are in common use: (1) twice the smaller tail probability (not exceeding 1), which is dual to the Clopper–Pearson interval; (2) the sum of the probabilities of all outcomes whose probability does not exceed $\mathbb{P}(X = x)$.

**Example 6.6.2 (Familial aggregation)** Example 4.2.2 of [7.7.4](/7.7.4): in 20 families with parental bronchitis, the infants of 3 families were affected, and the national risk is 5%. The one-sided $p = \mathbb{P}(X \ge 3) = 0.075$. The two-sided p-value is 0.151 by definition (1); by definition (2), the only outcomes with probability not exceeding $\mathbb{P}(X = 3) = 0.060$ are $X \ge 3$ ($X = 0, 1, 2$ all have larger probabilities), and the p-value is 0.075. The two definitions can differ by a factor of two when the distribution is asymmetric, and the method should be stated in a report (`scipy.stats.binomtest` uses definition (2) by default). Under either definition $H_0$ is not rejected at $\alpha = 0.05$.

## 6.7. The One-Sample Poisson Test and the Standardized Mortality Ratio

A typical question in occupational epidemiology is whether a certain cause of death is more frequent in an occupational group than in the general population. What is compared is then not a proportion but the observed number of deaths and the number expected from the mortality of the general population.

**Definition 6.7.1 (Standardized Mortality Ratio)** Applying the age-, sex- and period-specific death rates of the general (reference) population to the person-time of the study population gives the expected number of deaths $E$; the ratio of the observed number of deaths $O$ to $E$ is the **standardized mortality ratio** (SMR), often written as a percentage, $100\% \times O/E$. An SMR above 100% means that the study population has a higher risk of death than the reference population. When used for incidence it is called the standardized incidence ratio.

Under $H_0$ (the mortality of the study population equals that of the reference population), $O$ is approximately Poisson with mean $E$ (rare causes of death, Section 4.3 of [7.7.4](/7.7.4)).

**Formula 6.7.1 (One-Sample Poisson Test)** Let $O \sim \mathrm{Poi}(\mu)$ and test $H_0\colon \mu = E$. The exact two-sided p-value is $\min\{2\,\mathbb{P}(X \ge O \mid E), 1\}$ for $O \ge E$ and $\min\{2\,\mathbb{P}(X \le O \mid E), 1\}$ for $O < E$. For $E \ge 10$ the approximation $X^2 = (O - E)^2/E \overset{H_0}{\approx} \chi^2_1$ can be used. Equivalently, $H_0$ is rejected if and only if $E$ is not within the exact confidence interval for $\mu$ (Formula 5.7.1 of [7.7.5](/7.7.5)).

**Example 6.7.1 (Rubber workers)** In the rubber worker cohort of Example 5.7.1 of [7.7.5](/7.7.5), 4 deaths from Hodgkin's disease were observed against 3.3 expected from the mortality of white men in the United States. SMR $= 4/3.3 = 121\%$ and the two-sided $p = 2\,\mathbb{P}(X \ge 4 \mid 3.3) = 2 \times (1 - 0.580) = 0.84$. For bladder cancer 21 deaths were observed against 18.1 expected, SMR $= 116\%$ and $p = 2\,\mathbb{P}(X \ge 21 \mid 18.1) = 0.55$ (panel A above); the approximation gives $X^2 = 2.9^2/18.1 = 0.46$ and $p = 0.50$. Neither cause of death shows a significant excess. This agrees with the confidence intervals: $E = 3.3$ is within $(1.09, 10.24)$ and $E = 18.1$ is within $(13.00, 32.10)$. Note that the interval for Hodgkin's disease shows that such data are compatible with a mortality risk of either 1/3 or 3 times that of the general population: the result is nonsignificant because there are too few cases, not because the absence of risk has been demonstrated.

There are two pitfalls in interpreting the SMR. First, the "healthy worker effect": those at work must be healthy enough to work, and their overall mortality is often lower than that of the general population, so the SMR underestimates the harm of occupational exposure. Second, the SMRs of different study populations should not be compared directly, because they are weighted by their own age compositions (the difference between indirect and direct standardization, [7.7.13](/7.7.13)).

## 6.8. Misuses of the p-Value

### 6.8.1. What the p-Value Is Not

In 2016 the American Statistical Association (ASA) issued a statement on statistical significance and p-values (Wasserstein and Lazar 2016), proposing six principles:

1. P-values can indicate how incompatible the data are with a specified statistical model (the null hypothesis);
2. P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by chance alone;
3. Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold;
4. Proper inference requires full reporting and transparency (report all analyses done, not just the significant ones);
5. A p-value, or statistical significance, does not measure the size of an effect or the importance of a result;
6. By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis.

The second principle is the most often violated. "$p = 0.03$, so the probability that $H_0$ is true is only 3%" is wrong: the p-value is the probability of the data computed on the premise that $H_0$ is true, $\mathbb{P}(\text{data} \mid H_0)$, and not $\mathbb{P}(H_0 \mid \text{data})$. This is exactly the same distinction as that between $\mathbb{P}(\text{positive} \mid \text{not diseased})$ and $\mathbb{P}(\text{not diseased} \mid \text{positive})$ in [7.7.3](/7.7.3): regard the use of a test in many studies as screening, with $\alpha$ the "false positive rate" and $1 - \beta$ the "sensitivity"; "how many of the significant results are true" then also depends on how many of the hypotheses tested were true to begin with (the "prevalence"). If only 10% of the hypotheses tested in a field are true and the average power is 50%, then at $\alpha = 0.05$ the proportion of false positives among significant results is $\frac{0.9 \times 0.05}{0.9 \times 0.05 + 0.1 \times 0.5} = 47\%$. This is one reason why the conclusions of research in many fields are hard to replicate ([7.7.18](/7.7.18)). In 2019 the ASA's journal went further and called for abandoning the phrase "statistically significant" and for reporting p-values as continuous evidence.

### 6.8.2. Statistical Significance and Practical Importance

The p-value depends on both the size of the effect and the sample size. With a large enough sample, a trivial difference is highly significant: if an antihypertensive drug lowers systolic pressure by only 0.5 mmHg on average (standard deviation between individuals 15 mmHg), then among 100,000 participants $z = 0.5\sqrt{100\,000}/15 = 10.5$ and $p < 10^{-25}$, yet 0.5 mmHg has no clinical meaning. Conversely, a clinically important difference in a small sample may be nonsignificant (Section 6.4.4). To judge the importance of a result, look at the size of the effect and its confidence interval and compare them with the minimal clinically important difference specified in advance.

### 6.8.3. Effect Sizes

**Definition 6.8.1 (Effect Size)** A quantity that measures the size of an effect independently of the sample size is an **effect size**. It may be a difference in the original units (a mean difference of 5 oz, a risk ratio of 1.6) or a standardized difference, such as $d = (\bar x - \mu_0)/s$ in one-sample problems.

Standardized effect sizes make comparison possible across studies and measurement units and are the input of sample size calculations (the horizontal axis of panel B in Section 6.4.3). By Cohen's convention $\lvert d\rvert = 0.2, 0.5, 0.8$ count as "small, medium, large", but this is only a rough reference in the absence of domain knowledge. In Example 6.1.1, $d = -5/24 = -0.21$; in Example 6.2.1, $d = -8.48/40 = -0.21$; in Example 6.2.2, $d = -628/660 = -0.95$. The first two have almost the same standardized effect, and the difference in p-values (0.020 and 0.037) comes mainly from one-sided versus two-sided testing; the medical importance must be judged in original units: what a birth weight 5 oz (140 g) lower and a cholesterol 8.5 mg/dL lower mean for health must be judged separately.

### 6.8.4. Multiple Testing

Each test at $\alpha = 0.05$ has a 5% chance of a "significant" result even when $H_0$ is true. A study that tests 20 mutually independent hypotheses that are in fact all false (20 subgroups, 20 secondary endpoints, 20 genes) has a probability of at least one significant result of $1 - 0.95^{20} = 0.64$. The figure below shows the behavior of p-values: when $H_0$ is true the p-value is uniformly distributed on $(0, 1)$; when $H_1$ is true the p-values concentrate near 0, and the degree of concentration is the power. When thousands of tests are mixed together, the histogram of p-values is a uniform "floor" with a spike near 0, the starting point for estimating the false discovery rate in [7.7.20](/7.7.20).

![Distribution of p-values in 10,000 simulated one-sample t tests (n = 20, H0: μ = 0, two-sided). A: H0 true: p-values are uniform on (0, 1) and 5% are below 0.05. B: H1 true with standardized effect 0.5: p-values pile up near 0, and the proportion below 0.05 is the power (about 0.56). C: a mixture in which 80% of the H0 are true and 20% have an effect, as when thousands of genes are tested at once: a uniform floor plus a spike near 0. Simulated data](./plots/pvalue-distribution.py)

Specify one primary hypothesis in advance and report the others as exploratory analyses; when several hypotheses must be tested at the same time, use methods such as the **Bonferroni correction** to control the overall error rate ([7.7.12](/7.7.12), [7.7.20](/7.7.20)).

## 6.9. Computing with Python

```python
import numpy as np
import pandas as pd
from scipy import stats

# one-sample t test from raw data (Example 6.2.2)
bw = pd.read_csv("birthwt.csv")
x = bw.loc[bw.smoke == 1, "bwt"]
res = stats.ttest_1samp(x, popmean=3400, alternative="less")
print(res.statistic, res.pvalue)                     # -8.19, 3e-12

# from summary statistics (Example 6.2.1)
n, xbar, s, mu0 = 100, 181.52, 40, 190
t = (xbar - mu0) / (s / np.sqrt(n))
print(t, 2 * stats.t.cdf(-abs(t), n - 1))            # -2.12, 0.037

# power and sample size of the z test (Examples 6.4.1 and 6.4.2)
def power_one_sided(delta, sigma, n, alpha=0.05):
    return stats.norm.cdf(delta * np.sqrt(n) / sigma - stats.norm.isf(alpha))
print(power_one_sided(5, 24, 100), power_one_sided(5, 24, 10))   # 0.67, 0.16
z_a, z_b = stats.norm.isf(0.025), stats.norm.isf(0.10)
print(40**2 * (z_a + z_b)**2 / 20**2)                # 42.0
# the t-test version (noncentral t) with statsmodels
from statsmodels.stats.power import TTestPower
print(TTestPower().solve_power(effect_size=20 / 40, alpha=0.05, power=0.9))   # about 44

# chi-square test for a variance (Example 6.5.1)
X2 = 9 * 8.178 / 35
print(X2, 2 * min(stats.chi2.cdf(X2, 9), stats.chi2.sf(X2, 9)))   # 2.10, 0.021

# exact binomial tests (Examples 6.6.1 and 6.6.2)
print(stats.binomtest(30, 74, 29 / 115, alternative="greater").pvalue)   # 0.0027
print(stats.binomtest(3, 20, 0.05).pvalue)                               # 0.075 (method 2)

# one-sample Poisson test and SMR (Example 6.7.1)
O, E = 21, 18.1
print(O / E, min(1, 2 * stats.poisson.sf(O - 1, E)))                    # 1.16, 0.55
```

`TTestPower` in `statsmodels` computes power from the noncentral t distribution and gives a somewhat larger number than the normal approximation of Formula 6.4.2 (44 people instead of 43 in Example 6.4.2); for small samples it should be preferred.

## Summary

- The logic of testing (Section 6.1): compute how extreme the data are under $H_0$. The Type I error $\alpha$ and Type II error $\beta$ (Definition 6.1.1) correspond to $1 - {}$specificity and $1 - {}$sensitivity in diagnosis; the p-value (Definition 6.1.2) is $\mathbb{P}(\text{data as or more extreme} \mid H_0)$, not the probability that $H_0$ is true. One-sided or two-sided must be decided in advance.
- Summary of one-sample tests:

  | Problem | Statistic | Distribution under $H_0$ | Example |
  |---|---|---|---|
  | Mean, $\sigma$ known | $z = (\bar x - \mu_0)/(\sigma/\sqrt n)$ (Formula 6.2.1) | $\mathcal{N}(0,1)$ | Example 6.1.1 |
  | Mean, $\sigma$ unknown | $t = (\bar x - \mu_0)/(s/\sqrt n)$ (Formula 6.2.2) | $t_{n-1}$ | Examples 6.2.1, 6.2.2 |
  | Variance | $X^2 = (n-1)s^2/\sigma_0^2$ (Formula 6.5.1) | $\chi^2_{n-1}$ (strictly normal) | Example 6.5.1 |
  | Proportion | $z = (\hat p - p_0)/\sqrt{p_0q_0/n}$ or exact binomial (Formulas 6.6.1, 6.6.2) | $\mathcal{N}(0,1)$ / $\mathrm{Bin}(n, p_0)$ | Examples 6.6.1, 6.6.2 |
  | Counts and SMR | $O$ compared with expected $E$ (Formula 6.7.1, Definition 6.7.1) | $\mathrm{Poi}(E)$ | Example 6.7.1 |

- Tests and confidence intervals are dual (Theorem 6.3.1): $H_0$ is rejected if and only if $\mu_0$ is outside the interval; reports should emphasize effect estimates and intervals.
- Power $1 - \beta$ (Definition 6.4.1) increases with effect size, sample size and $\alpha$ and decreases with $\sigma$ (Formula 6.4.1); the sample size is $n = \sigma^2(z_{\alpha/2} + z_\beta)^2/\Delta^2$ (Formula 6.4.2), and when $\sigma$ comes from a small pilot study a margin should be left (Example 6.4.3). Nonsignificant does not mean no difference.
- An external reference value is meaningful only when it applies to the study population (Example 6.2.2); the SMR is affected by the healthy worker effect.
- Misuses of the p-value (Section 6.8): the six ASA principles; statistical significance is not practical importance, so report effect sizes (Definition 6.8.1); multiple testing accumulates false positives, and p-values are uniform under $H_0$.

## Questions

1. Using the jury analogy, explain: (a) why "failing to reject $H_0$" should not be described as "accepting $H_0$"; (b) why lowering $\alpha$ from 0.05 to 0.01 increases Type II errors; (c) how to reduce both types of error at once.

   **Answer** (a) A jury's "not guilty" says only that the prosecution's evidence is insufficient for conviction, not that the defendant is innocent; likewise, failing to reject $H_0$ says only that the data are compatible with $H_0$, and the data may also be compatible with many alternative values (especially when power is low). (b) Lowering $\alpha$ amounts to raising the evidentiary threshold for conviction: fewer innocent people are convicted, but more truly guilty people also go free because the evidence is "not sufficient": the rejection region shrinks, the probability of falling into it when $H_1$ is true (the power) falls and $\beta$ increases. (c) Collect more and better evidence: increase the sample size, reduce measurement error (reduce $\sigma$) and use a more efficient design (such as pairing), so that the two sampling distributions are further apart.

2. The national mean height of 7-year-old boys is 125 cm. Thirty-six 7-year-old boys in a locality are measured at random, with mean 123.2 cm and standard deviation 5.4 cm. Test at two-sided $\alpha = 0.05$ whether the mean height of local boys differs from the national one, and give a 95% confidence interval.

   **Answer** $t = (123.2 - 125)/(5.4/6) = -1.8/0.9 = -2.00$ with 35 degrees of freedom, and the two-sided $p = 2\,\mathbb{P}(t_{35} \le -2.00) = 0.053$. $H_0$ is not rejected (the result is borderline). With $t_{35, 0.025} = 2.030$ the 95% interval is $123.2 \pm 2.030 \times 0.9 = (121.37, 125.03)$ cm, which just contains 125, consistent with the test. The conclusion should not be stated as "no difference": the data are compatible with anything from 3.6 cm shorter to 0.03 cm taller on average, and a larger sample is needed for a clear conclusion.

3. Suppose the investigators of Example 6.1.1 originally planned a two-sided test but, after seeing $\bar x = 115 < 120$, switched to a one-sided test and reported $p = 0.019$. What is the actual Type I error rate of this procedure?

   **Answer** Whichever side $\bar x$ falls on, the investigators would choose the one-sided test for that side, which amounts to rejecting when $\lvert z\rvert > 1.645$, a Type I error rate of $2 \times 0.05 = 0.10$, twice the nominal level. The correct procedure is to report the two-sided test decided on in advance, $p = 0.037$.

4. A new nutritional supplement is claimed to raise the mean birth weight of full-term newborns by 100 g. The standard deviation of birth weight is known to be about 500 g. With two-sided $\alpha = 0.05$ and 80% power, how many pregnant women taking the supplement are needed (compared with the known population mean of 3300 g)? If only 100 can be recruited, what is the power? What is wrong with such a one-sample design?

   **Answer** $n = 500^2(1.96 + 0.842)^2/100^2 = 196.2$, so 197 are needed. For $n = 100$ the power is $\approx \Phi(100 \times 10/500 - 1.96) = \Phi(0.04) = 0.52$. Design problems: when compared with an external "population mean", pregnant women taking the supplement may differ from the general population in many respects (more health-conscious, higher socioeconomic status, from a particular hospital), and the difference cannot be attributed to the supplement (Example 6.2.2); and without a control group a time trend and a placebo effect cannot be excluded. A randomized controlled trial should be done (Section 5.2 of [7.7.5](/7.7.5)); the sample size for a two-group comparison is in [7.7.7](/7.7.7).

5. A hospital counted surgical site infections among 60 operations in 2023, with 9 infections; the national infection rate for such operations is 7%. Test with the exact binomial test and the normal approximation whether the hospital's infection rate is higher than the national level (one-sided $\alpha = 0.05$).

   **Answer** $\hat p = 0.15$. $np_0(1-p_0) = 60 \times 0.07 \times 0.93 = 3.91 < 5$, so the normal approximation is not applicable, but for comparison: $z = (0.15 - 0.07)/\sqrt{0.07 \times 0.93/60} = 0.08/0.0329 = 2.43$, $p = 0.0076$. The exact test gives $p = \mathbb{P}(X \ge 9 \mid n = 60, p = 0.07) = 0.023$. Both are below 0.05, but the normal approximation underestimates the p-value by a factor of about 3. Conclusion: the infection rate of the hospital is significantly higher than the national level (exact $p = 0.023$) and the cause should be investigated; at the same time one must consider whether the case mix (difficulty of operations, underlying diseases of the patients) is comparable with the national one, using standardization if necessary (Section 6.7, [7.7.13](/7.7.13)).

6. Among 1200 workers of a chemical plant, 12 deaths from liver cancer were observed during follow-up, against 5.2 expected from age-specific national mortality. Find the SMR, test whether there is an excess of deaths, and give a 95% confidence interval for the SMR.

   **Answer** SMR $= 12/5.2 = 231\%$. $p = 2\,\mathbb{P}(X \ge 12 \mid 5.2) = 2 \times 0.0073 = 0.015$, a significant excess of deaths. The exact 95% interval for $\mu$ is $(\frac12\chi^2_{24, 0.975}, \frac12\chi^2_{26, 0.025}) = (6.20, 20.96)$, so the interval for the SMR is $(6.20/5.2, 20.96/5.2) = (119\%, 403\%)$. The lower limit is above 100%, consistent with the test. One should also consider the healthy worker effect (which biases the SMR downward, so the true excess may be larger) and whether other risk factors (alcohol, hepatitis B virus infection) are more common among the workers.

7. A study reports "compared with the reference value, the new therapy group has $p = 0.08$, the difference is not statistically significant, and therefore the new therapy is ineffective". Point out the problems and explain how it should be reported.

   **Answer** Problems: (1) it equates "nonsignificant" with "ineffective" (Section 6.4.4): $p = 0.08$ indicates that the data provide some evidence that did not cross the 0.05 threshold; (2) it reports neither the size of the effect nor a confidence interval, so the reader cannot judge how large the effect might be; (3) it does not state the power of the study, and with a small sample a negative result is uninformative; (4) the comparison with a "reference value" may itself be biased (Example 6.2.2). It should report the point estimate of the effect (such as the mean difference) with a 95% confidence interval, state that the interval contains 0 but also clinically meaningful effects, conclude that "the evidence is insufficient" and that a larger study is needed, and preferably report the sample size calculation in advance.

8. A laboratory measures a standard 12 times with a new method, obtaining a standard deviation of 0.85 units; the manufacturer claims the standard deviation of the method does not exceed 0.6. Test the manufacturer's claim at one-sided $\alpha = 0.05$. What does this test depend on?

   **Answer** $H_0\colon \sigma^2 \le 0.36$, $H_1\colon \sigma^2 > 0.36$. $X^2 = 11 \times 0.85^2/0.36 = 11 \times 0.7225/0.36 = 22.08$ and $\chi^2_{11, 0.05} = 19.68$; $X^2 > 19.68$, the one-sided $p = \mathbb{P}(\chi^2_{11} \ge 22.08) = 0.024$, and $H_0$ is rejected: the standard deviation of the method is larger than the manufacturer's claim. The test depends strictly on the measured values being normally distributed and the measurements independent: if one or two measurements are abnormal (outliers), the chi-square test is very sensitive to them, and the data should be checked first and the reason for any abnormal values found.

9. A gene expression study carried out a t test on each of 10,000 genes, and 620 genes had $p < 0.05$. Assume all tests are independent. (a) If no gene is truly differentially expressed, how many $p < 0.05$ are expected? (b) Roughly estimate how many of the 620 "significant" genes are false positives. (c) If the probability of any false positive among the 10,000 tests must not exceed 0.05, what should the threshold of each test be?

   **Answer** (a) Under $H_0$ p-values are uniform, so $10\,000 \times 0.05 = 500$ are expected. (b) If the great majority of genes are not differentially expressed, about 500 (the number of truly nondifferential genes times 0.05, slightly fewer than 500) of the "significant" genes come from $H_0$; about 80% of the 620 are false positives and only about 120 may be real: "significant" has almost no discriminating power here (the screening analogy of Section 6.8.1). (c) Bonferroni: use $0.05/10\,000 = 5 \times 10^{-6}$ for each test. This controls the probability of "at least one false positive" but has very low power; omics studies more often control the false discovery rate ([7.7.20](/7.7.20)).

10. (Open question) A paper states: "We tested the relation between serum vitamin D and 15 diseases and found a significant association with depression ($p = 0.04$), suggesting that vitamin D supplementation can prevent depression." Comment point by point from the viewpoint of hypothesis testing.

    **Answer** Key points: (1) Multiple testing: among 15 tests the probability of at least one $p < 0.05$ is about $1 - 0.95^{15} = 0.54$, so a single $p = 0.04$ is quite likely due to chance; all 15 results should be reported and corrected for, or the finding treated as a hypothesis requiring validation. (2) $p = 0.04$ is marginal evidence, and when the prior proportion of true hypotheses among those tested is low, the likelihood of a false positive is high (Section 6.8.1); the effect size and confidence interval should be reported. (3) Association is not causation: people with depression spend less time outdoors and get less sunlight, so low vitamin D may be a result rather than a cause (reverse causation), or there may be common causes (obesity, chronic disease); an observational study cannot support the conclusion that "supplementation can prevent" ([7.7.15](/7.7.15)). (4) Testing the effect of supplementation requires a randomized controlled trial (in fact, large randomized trials have not found that vitamin D supplementation prevents depression).
