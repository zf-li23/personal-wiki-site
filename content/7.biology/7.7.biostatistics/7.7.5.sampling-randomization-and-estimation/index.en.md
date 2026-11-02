---
title: Sampling, Randomization and Estimation
description: Designs for probability sampling (simple random, systematic, stratified, cluster); randomization methods and blinding in randomized clinical trials; properties of point estimators and maximum likelihood; confidence intervals for means, variances, proportions and Poisson rates (t and chi-square intervals, Wilson and Clopper–Pearson intervals, exact Poisson intervals); one-sided intervals, sample size and margin of error; bootstrap intervals; Bayesian estimation with the beta–binomial model. Illustrated with birth weight, diagnostic accuracy, an occupational cohort and lung cancer screening.
source_hash: 960f8532b88b
---

Statistical inference goes from the data to the population, and where the data come from determines whether this step can be taken. The first half of this chapter treats the two "good sources" of data: probability sampling from a population, which ensures that the sample can represent the population, and random allocation in an experiment, which ensures that differences between groups can arise only from the treatment or from chance. The second half treats estimation: using a number computed from the sample (a point estimate) to estimate a population parameter, and expressing the uncertainty of that estimate by an interval (a confidence interval). The construction of intervals relies on the sampling distributions of the previous chapter: the sample mean is approximately normal, the $t$ distribution is used when $\sigma$ is unknown, the chi-square distribution for variances, and there are special methods for proportions and counts. The examples continue the main threads: the mean birth weight and the proportion of low birth weight among infants of smoking mothers (birthwt), the sensitivity and specificity of the CT scores in [7.7.3](/7.7.3), the lung cancer mortality in the NLST, and the median of FEV; randomization is illustrated with the Physicians' Health Study (PHS). The mathematics of the properties of estimators, maximum likelihood and interval estimation is in [3.2.3](/3.2.3) and [3.2.4](/3.2.4), the bootstrap in [3.5.7](/3.5.7) and Bayesian inference in [3.2.7](/3.2.7); the next chapter, [7.7.6](/7.7.6), uses the same sampling distributions for hypothesis tests, and the two are the two sides of one coin.

## 5.1. Sampling Methods

### 5.1.1. Why Probability Sampling

A study wanted to know the prevalence of hypertension among adults in a city and surveyed 2000 people at the cardiology outpatient clinic of a top-tier hospital, finding 45%. The number is very precise (standard error about 1.1%) but nearly useless: people who come to a cardiology clinic are for that very reason more likely to have hypertension. No matter how large the sample, it cannot correct the bias caused by the way the sample was drawn.

The reliable approach is *probability sampling*: every individual in the population has a known, nonzero probability of being selected, and a random mechanism decides who is included. The composition of the sample is then not affected by the subjective choices of the investigator or respondents, and sampling error can be computed with probability theory, which is the premise of all the sampling distributions in [7.7.4](/7.7.4). Sampling requires a list of the population (the sampling frame), such as a residents' register, a school roster or a hospital's records database.

### 5.1.2. Four Basic Designs

The **simple random sample** is the most basic design: draw $n$ of $N$ individuals so that every combination of $n$ individuals has the same probability of being selected ([7.7.1](/7.7.1)). Example: a national nurses' cohort has 100,000 members and 100 are to be chosen to try a new method of blood collection. Taking the 100 with the smallest identification numbers is not a random sample (the first two digits of the number represent the state, and the 100 may all come from one state); generating 100 random numbers from 1–100,000 by computer, so that every nurse has the same chance of being selected, gives a simple random sample.

**Definition 5.1.1 (Systematic, Stratified and Cluster Sampling)** Choosing a random starting point on the list and then taking every $k$th individual is **systematic sampling**. Dividing the population into non-overlapping strata according to some characteristic and drawing a simple random sample separately within each stratum is **stratified sampling**. Dividing the population into many clusters (families, schools, villages, wards), drawing a random set of clusters and surveying all members of the selected clusters is **cluster sampling**.

![Four probability sampling designs: 12 people drawn from 120. The four rows are four strata (such as age groups), and each row is divided by dotted lines into 5 clusters (6 people each, such as families or villages). A: simple random sampling, in which every combination of 12 people has the same chance. B: systematic sampling, taking 1 person in every 10 after a random start. C: stratified sampling, drawing 3 people at random from each stratum. D: cluster sampling, drawing 2 clusters at random and surveying all their members. Schematic](./plots/sampling-schemes.py)

| Design | Advantages | Disadvantages | Biomedical example |
|---|---|---|---|
| Simple random | Simplest theory, unbiased estimates | Needs a complete list; the sample may be scattered, making surveys costly | Randomly drawing records from a records database |
| Systematic | Easy to carry out, spread evenly over the list | Bias if the list is periodic | Surveying 1 of every 3 outpatients |
| Stratified | Ensures adequate representation of every stratum; higher precision when strata are homogeneous | Needs to know the stratum of every individual | Drawing survey participants stratified by age and sex |
| Cluster | No list of individuals needed; cheap fieldwork | Individuals within a cluster are similar, so precision is lower for the same sample size | Surveying parasite infection or myopia by village or school |
| Convenience | Cheap and fast | Not probability sampling; bias cannot be estimated | Outpatient volunteers, online questionnaires |

The estimate of the population mean in stratified sampling is the average of the stratum sample means weighted by the stratum weights, $\bar x_{\mathrm{st}} = \sum_h W_h \bar x_h$, where $W_h = N_h/N$ is the proportion of the population in stratum $h$. When the strata differ greatly and the variation within strata is small, the variance of stratified sampling is much smaller than that of a simple random sample of the same size. Cluster sampling is the opposite: people in the same cluster share the same living environment and have similar outcomes, so sampling 20 people from each of 50 villages provides much less information than 1000 independently sampled people; the factor by which the variance is inflated (the design effect) is computed in Question 10 of [7.7.4](/7.7.4) and in [7.7.17](/7.7.17).

Large population surveys usually combine these designs. The US National Health and Nutrition Examination Survey (NHANES) uses multistage sampling: counties are drawn first, then blocks within counties, and then households and individuals; older adults, ethnic minorities and low-income people are deliberately oversampled to ensure adequate sample sizes in these subgroups. Such a sample is not a simple random sample, and the sampling weights must be used in analysis; otherwise the estimated prevalence is biased toward the oversampled groups.

### 5.1.3. Random Numbers

Both sampling and randomization depend on random numbers. A computer generates pseudorandom numbers: they are produced by a deterministic algorithm from an initial value (the seed), look random, and can be reproduced by fixing the seed (principle in [3.5.8](/3.5.8)). The study protocol should record the method of generating random numbers and the seed, so that the sampling or allocation can be audited. Do not substitute "seemingly random" human choices (such as the parity of the birth date or alternating groups in order of presentation) for random numbers: such patterns are easy to guess and may be related to the outcome.

## 5.2. Randomized Clinical Trials

### 5.2.1. Why Randomize

Sampling determines to which population the conclusions can be generalized (external validity), and the way of allocation determines whether the comparison between groups is fair (internal validity). In an observational study exposure is "chosen" by people themselves: in [7.7.1](/7.7.1) the smoking children are on average 4 years older, and their higher FEV does not show that smoking is beneficial. If physicians decide who receives the new treatment, patients with milder disease and better prognosis may be assigned more often to the new treatment group, and the result is equally untrustworthy.

**Definition 5.2.1 (Randomization)** Using a random mechanism to decide which treatment each participant receives, so that allocation is unrelated to any characteristic of the participants (measured or unmeasured), is **randomization**.

Randomization has two functions. First, it makes the groups differ only randomly in all baseline characteristics (including factors unknown to the investigator), so that systematic differences in outcome between groups can be attributed to the treatment, the basis of causal conclusions ([7.7.15](/7.7.15)). Second, it gives statistical inference a probabilistic foundation: under the null hypothesis that "the treatment is ineffective", the distribution of the observed difference between groups is determined entirely by the random allocation (the permutation test of [7.7.8](/7.7.8)). The 1948 Medical Research Council trial of streptomycin for pulmonary tuberculosis was the first clinical trial to use random numbers formally for allocation ([7.7.1](/7.7.1)).

### 5.2.2. Methods of Randomization

- Simple randomization: each participant is independently assigned to A or B with probability 1/2 (a coin toss). In small samples the numbers in the two groups may differ considerably: for $n = 20$ the probability that the group sizes differ by 6 or more (7:13 or more unbalanced) is 0.26.
- Block randomization: ensures that among every $b$ consecutively enrolled participants the groups have equal numbers.
- Stratified randomization: block randomization within each stratum, ensuring that the groups are balanced on important prognostic factors.

**Definition 5.2.2 (Block Randomization and Stratified Randomization)** Dividing consecutively enrolled participants into blocks of $b$ ($b$ a multiple of the number of groups) and randomly permuting the assignments within each block so that the groups have equal numbers within each block is **block randomization**. Stratifying participants first by important prognostic factors (center, disease stage, age group) and performing block randomization separately within each stratum is **stratified randomization**.

Example: with two groups and block length 4, each block is one of the 6 arrangements AABB, ABAB, ABBA, BAAB, BABA, BBAA, chosen at random. After 4, 8, 12, … participants are enrolled, the two groups always have equal numbers. When the block length is fixed and known to the investigators, the last assignment in each block can be guessed, so block lengths 4 and 6 are often mixed at random and kept confidential from the investigators.

The effect of randomization also depends on *allocation concealment*: the person who recruits participants must not know what the next assignment is before the participant is enrolled; otherwise he or she may deliberately or unconsciously let a patient with milder disease "happen" to enter the new treatment group. Central telephone or web-based randomization systems and sealed, opaque, sequentially numbered envelopes are common methods.

```python
import numpy as np

rng = np.random.default_rng(20240501)          # record the seed in the protocol

def block_randomization(n, block_sizes=(4, 6), arms=("A", "B")):
    """Permuted blocks of randomly mixed sizes; arms are balanced within each block."""
    out = []
    while len(out) < n:
        b = rng.choice(block_sizes)
        block = np.repeat(arms, b // len(arms))
        out.extend(rng.permutation(block))
    return out[:n]

# stratified randomization: a separate sequence for each centre
schedule = {centre: block_randomization(40) for centre in ["centre 1", "centre 2", "centre 3"]}
print(schedule["centre 1"][:12])
```

### 5.2.3. Blinding

**Definition 5.2.3 (Blinding)** Keeping the participants, the therapists or the people assessing the outcome unaware of which treatment a participant receives is **blinding**. Blinding only the participants is single blinding, and blinding both participants and investigators (therapists and outcome assessors) is double blinding.

Patients who know they are taking a new drug may report better feelings (the reverse of the placebo effect), physicians who know the allocation may treat complications in the new drug group more actively, and assessors who know the allocation may read ambiguous images in favor of the new drug. A double-blind placebo-controlled design can remove these biases. Trials that cannot be blinded (surgery versus drugs, lifestyle interventions) should at least keep the outcome assessors unaware of the allocation and use objective endpoints (death, laboratory indices) as far as possible.

### 5.2.4. The Physicians' Health Study: A Factorial Design

**Example 5.2.1** The Physicians' Health Study (Example 3.1.4 of [7.7.3](/7.7.3)) tested two questions at the same time: whether 325 mg of aspirin on alternate days prevents myocardial infarction, and whether 50 mg of β-carotene on alternate days prevents cancer. The 22,071 male physicians were randomized to 4 groups in a 2×2 arrangement: aspirin + β-carotene, aspirin + placebo, placebo + β-carotene, and two placebos, with all tablets looking identical (double blind). Everyone took part in two comparisons: the effect of aspirin is the comparison of the first two groups with the last two, and the effect of β-carotene the comparison of groups 1 and 3 with groups 2 and 4; one trial yields the information of two trials, provided that the effects of the two treatments do not interact (the factorial design of [7.7.12](/7.7.12)). The aspirin component was stopped early in 1988 by the data monitoring committee because of the significant reduction in myocardial infarction ([7.7.18](/7.7.18)); the β-carotene component continued until 1995 and, after 12 years, found no effect on cancer or cardiovascular disease.

## 5.3. Point Estimation

### 5.3.1. Estimators and Their Properties

Population parameters are estimated by sample statistics: the sample mean $\bar x$ estimates $\mu$, the sample proportion $\hat p$ estimates $p$, and the sample standard deviation $s$ estimates $\sigma$. As a rule (a function of the sample) it is called a **point estimator**, and the number obtained by inserting the data is the estimate. A good estimator should be:

- unbiased: $\mathbb{E}[\hat\theta] = \theta$, neither too high nor too low on average (an **unbiased estimator**);
- precise: the variance of its sampling distribution is small, that is, the **standard error** is small;
- when both matter, judged by the **mean squared error** $\operatorname{MSE}(\hat\theta) = \mathbb{E}[(\hat\theta - \theta)^2] = \operatorname{Var}(\hat\theta) + [\mathbb{E}(\hat\theta) - \theta]^2$; a slightly biased estimator with a much smaller variance may be better (regularization in [7.7.21](/7.7.21));
- consistent: the estimate converges to the true value as the sample size grows (a **consistent estimator**).

The sample mean is an unbiased estimator of $\mu$ with standard error $\sigma/\sqrt n$ (Theorem 4.7.1 of [7.7.4](/7.7.4)); for a normal population it has the smallest variance among all unbiased estimators. The sample proportion $\hat p$ is also unbiased, with standard error $\sqrt{p(1-p)/n}$.

### 5.3.2. Why the Sample Variance Divides by $n - 1$

**Theorem 5.3.1** Let $X_1, \dots, X_n$ be independent and identically distributed with variance $\sigma^2$. Then the sample variance $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar X)^2$ is an unbiased estimator of $\sigma^2$, whereas the expectation of $\frac{1}{n}\sum (X_i - \bar X)^2$, which divides by $n$, is $\frac{n-1}{n}\sigma^2$.

**Proof** $\sum (X_i - \bar X)^2 = \sum (X_i - \mu)^2 - n(\bar X - \mu)^2$. Taking expectations: $\mathbb{E}\sum(X_i - \mu)^2 = n\sigma^2$ and $\mathbb{E}[n(\bar X - \mu)^2] = n \cdot \sigma^2/n = \sigma^2$, so $\mathbb{E}\sum (X_i - \bar X)^2 = (n-1)\sigma^2$. $\square$

Intuitively, the spread of the data around their own mean $\bar X$ is always smaller than around the true mean $\mu$ ($\bar X$ is exactly the point that minimizes the sum of squares), and dividing by $n - 1$ compensates for this. The quantity $n - 1$ is the number of **degrees of freedom**: the $n$ deviations $x_i - \bar x$ sum to 0, so only $n - 1$ of them can vary freely. For $n = 5$, dividing by $n$ underestimates the variance by 20% on average, and for $n = 100$ by only 1%. Note that $S$ itself is not an unbiased estimator of $\sigma$ (the square root is concave, $\mathbb{E}S < \sigma$), but the bias is negligible when the sample is not too small.

### 5.3.3. Maximum Likelihood Estimation

How do we construct an estimator for a new problem? The most general method is **maximum likelihood estimation**: take the parameter value that maximizes the probability of the observed data (the **likelihood function**).

**Example 5.3.1** In the birthwt data, 30 of the 74 smoking mothers had low birth weight infants. Treat the risk $p$ of low birth weight for smoking mothers as an unknown parameter; under the binomial model the probability of observing 30 cases is

$$
L(p) = \binom{74}{30} p^{30} (1 - p)^{44}.
$$
The log-likelihood is $\ell(p) = 30\ln p + 44\ln(1 - p) + \text{constant}$, and setting the derivative $30/p - 44/(1 - p) = 0$ gives $\hat p = 30/74 = 0.405$, the sample proportion. For common problems such as the normal mean and the Poisson rate (events ÷ person-time, Section 4.6.2 of [7.7.4](/7.7.4)), maximum likelihood gives the "natural" estimators; its power lies in applying equally to complex models (logistic regression, survival models, mixed models), and in large samples it is approximately unbiased, approximately normal and of minimum variance ([3.2.3](/3.2.3)).

## 5.4. Confidence Intervals for a Mean

### 5.4.1. Construction

A point estimate is almost never exactly equal to the parameter, and we must also say how far it may deviate.

**Formula 5.4.1 (Confidence Interval for a Mean)** Suppose the sample comes from a normal population or the sample size is large enough. When the population standard deviation $\sigma$ is known, the $100(1 - \alpha)\%$ **confidence interval** for $\mu$ is

$$
\bar x \pm z_{\alpha/2} \frac{\sigma}{\sqrt n};
$$
when $\sigma$ is unknown and replaced by the sample standard deviation $s$, it is

$$
\bar x \pm t_{n-1, \alpha/2} \frac{s}{\sqrt n}.
$$

Both intervals have the form "point estimate ± **margin of error**": margin of error = quantile × standard error. The second interval rests on $(\bar X - \mu)/(S/\sqrt n) \sim t_{n-1}$ (Section 4.8 of [7.7.4](/7.7.4)). The case of known $\sigma$ is rare in practice; when $n$ is large, $t_{n-1,\alpha/2}$ is close to $z_{\alpha/2}$ and the two are almost identical.

**Example 5.4.1 (Mean birth weight of infants of smoking mothers)** For the 74 infants of smoking mothers in the birthwt data, the mean birth weight is $\bar x = 2771.9$ g, the standard deviation $s = 659.6$ g, and the standard error $659.6/\sqrt{74} = 76.7$ g. With $t_{73, 0.025} = 1.993$, the 95% confidence interval is

$$
2771.9 \pm 1.993 \times 76.7 = (2619.1,\ 2924.7)\ \text{g}.
$$
The 99% confidence interval uses $t_{73, 0.005} = 2.645$ and is $(2569.1, 2974.7)$ g, wider. The 115 infants of nonsmoking mothers have a mean of 3055.7 g and a 95% confidence interval of $(2916.7, 3194.7)$ g. The two intervals do not overlap, suggesting that the population means of the two groups do differ; but the correct way to compare two groups is an interval estimate for the difference ([7.7.7](/7.7.7)), and "whether the intervals overlap" is a conservative, rough judgment.

### 5.4.2. What "95% Confidence" Means

The most common misreading of a confidence interval is "the true value has a 95% probability of lying between 2619 and 2925". In the frequentist framework, the true value $\mu$ is a fixed number and either lies in this interval or does not; it is the interval that is random. The 95% refers to the method of constructing the interval: if one samples repeatedly and constructs an interval by Formula 5.4.1 each time, in the long run 95% of these intervals will cover the true value (figure below). It is like casting a net for fish: 95% describes the catch rate of the net, not the probability that there is a fish in one particular cast. To make a probability statement about the parameter itself ("the probability that $\mu$ lies in the interval is 95%"), a Bayesian credible interval is needed (Section 5.11).

!["95% confidence" explained. One hundred samples of 20 newborns each are drawn by simulation from a normal population with mean 2945 g and standard deviation 729 g (the values of the birthwt data), and a 95% t interval is computed for each sample (vertical lines; dots are sample means). Intervals that fail to cover the true mean (horizontal line) are shown in orange, 4 in this simulation. The width of an interval varies with the sample standard deviation. Simulated data](./plots/ci-coverage.py)

### 5.4.3. Determinants of the Width of the Interval

The margin of error $t_{n-1,\alpha/2}\, s/\sqrt n$ is determined by three factors:

- Confidence level: the higher the level, the larger the quantile and the wider the interval (1.96 for 95%, 2.58 for 99%);
- The variability of the data $s$: the greater the differences between individuals, the wider the interval; improving the measurement method and choosing homogeneous participants can reduce $s$;
- The sample size $n$: the width of the interval is proportional to $1/\sqrt n$, and increasing the sample size to 4 times halves the width.

The validity of a confidence interval depends on the representativeness of the sample. It quantifies only random sampling error and cannot correct selection bias or measurement bias like that of Section 5.1.1: a narrow interval from a biased sample only estimates the wrong quantity precisely.

## 5.5. Confidence Intervals for a Variance

Questions such as the precision of an assay and within-individual variation require estimating the variance itself.

**Formula 5.5.1 (Confidence Interval for a Normal Variance)** Suppose the sample comes from a normal population. From $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$, the $100(1 - \alpha)\%$ confidence interval for $\sigma^2$ is

$$
\left(\frac{(n-1)s^2}{\chi^2_{n-1, \alpha/2}},\ \frac{(n-1)s^2}{\chi^2_{n-1, 1-\alpha/2}}\right),
$$
where $\chi^2_{n-1, \alpha/2}$ is the upper $\alpha/2$ quantile. Taking square roots of both ends gives the confidence interval for $\sigma$.

**Example 5.5.1 (Interobserver variation of a new blood pressure monitor)** To evaluate an ultrasound blood pressure monitor, two observers each measured the systolic pressure of 10 participants with it, and the variance of the difference $d_i$ between the two readings measures the interobserver variation. The sample variance is $s^2 = 8.178$ mmHg². With $\chi^2_{9, 0.025} = 19.02$ and $\chi^2_{9, 0.975} = 2.70$, the 95% confidence interval for $\sigma^2$ is

$$
\left(\frac{9 \times 8.178}{19.02},\ \frac{9 \times 8.178}{2.70}\right) = (3.87,\ 27.26),
$$
and the interval for the standard deviation is $(1.97, 5.22)$ mmHg. The interval is asymmetric and very wide: the upper limit is 7 times the lower. Estimating a variance from only 10 people has low precision; variance estimates usually require far more data than mean estimates. Whether this interval shows that the new instrument varies less than the standard sphygmomanometer (with known variance 35) is addressed in Example 6.5.1 of [7.7.6](/7.7.6).

This interval depends strictly on the normality assumption; with heavy tails or outliers the actual coverage may be far below the nominal level, and a large sample does not help (unlike the $t$ interval for the mean). For non-normal data the bootstrap (Section 5.10) can be used.

## 5.6. Confidence Intervals for a Proportion

### 5.6.1. The Wald Interval and Its Defects

From the normal approximation to the sample proportion (Section 4.7.3 of [7.7.4](/7.7.4)), the most direct interval is the Wald interval

$$
\hat p \pm z_{\alpha/2}\sqrt{\frac{\hat p(1 - \hat p)}{n}}.
$$
It is the standard form in many textbooks, but performs poorly: when $p$ is near 0 or 1, or $n$ is not large, the actual coverage is far below the nominal 95% and oscillates irregularly with $n$ and $p$ (figure below). When $\hat p = 0$ it degenerates to $[0, 0]$, and when $\hat p$ is small the lower limit is negative.

### 5.6.2. The Wilson and Clopper–Pearson Intervals

**Definition 5.6.1 (Wilson Score Interval)** The interval obtained by solving the inequality $\lvert\hat p - p\rvert \le z_{\alpha/2}\sqrt{p(1 - p)/n}$ (using $p$ rather than $\hat p$ in the standard error),

$$
\frac{\hat p + \frac{z^2}{2n}}{1 + \frac{z^2}{n}} \pm \frac{z}{1 + \frac{z^2}{n}}\sqrt{\frac{\hat p(1 - \hat p)}{n} + \frac{z^2}{4n^2}}, \qquad z = z_{\alpha/2},
$$
is the **Wilson score interval** for a proportion.

Its center shrinks from $\hat p$ toward 1/2, it still has a positive upper limit when $\hat p = 0$, and its coverage is close to the nominal level throughout $(0, 1)$. The derivation is in [3.2.4](/3.2.4).

**Definition 5.6.2 (Clopper–Pearson Interval)** The interval $(p_L, p_U)$ constructed directly from the binomial distribution, where $p_L$ satisfies $\mathbb{P}(X \ge x \mid p_L) = \alpha/2$ and $p_U$ satisfies $\mathbb{P}(X \le x \mid p_U) = \alpha/2$, is the **Clopper–Pearson interval** (exact interval). It can be expressed through quantiles of the beta distribution: $p_L$ is the lower $\alpha/2$ quantile of $\mathrm{Beta}(x, n - x + 1)$ and $p_U$ is the $1-\alpha/2$ quantile of $\mathrm{Beta}(x + 1, n - x)$.

"Exact" means that the computation uses the binomial distribution itself rather than the normal approximation, not that the coverage is exactly 95%: because the binomial distribution is discrete, it guarantees a coverage of at least 95%, at the price of being wider on average (the average coverage in the figure below is 97.3%).

![Actual coverage of three nominal 95% intervals for a proportion with n = 30 (for each true proportion p, the binomial probabilities of all outcomes whose interval covers p are summed; computed exactly). The Wald interval has serious undercoverage when p is near 0 and 1 and oscillates irregularly; the Wilson interval stays close to 95%; the Clopper–Pearson interval is never below 95% but is conservative](./plots/proportion-coverage.py)

Recommended practice: use the Wilson interval in general; use the Clopper–Pearson interval when coverage must be guaranteed to be at least the nominal level (regulatory submissions, rare adverse events); no longer use the Wald interval.

**Example 5.6.1 (Proportion of low birth weight)** Among smoking mothers the proportion with low birth weight is $\hat p = 30/74 = 0.405$. The 95% confidence intervals are: Wald $(0.294, 0.517)$, Wilson $(0.301, 0.519)$, Clopper–Pearson $(0.293, 0.526)$. For nonsmoking mothers $29/115 = 0.252$, with Wilson interval $(0.182, 0.339)$. When $n$ is fairly large and $\hat p$ is not extreme, the three methods differ little.

**Example 5.6.2 (Confidence intervals for sensitivity and specificity)** In Example 3.4.1 of [7.7.3](/7.7.3), taking a CT score of "grade 4 and above" as positive, the sensitivity is $44/51 = 0.863$ and the specificity is $45/58 = 0.776$. The Wilson 95% intervals are $(0.743, 0.932)$ and $(0.653, 0.864)$, respectively. Taking "grade 5" as positive the specificity is $56/58 = 0.966$, and the Wald interval is $(0.919, 1.012)$, whose upper limit exceeds 1; the Wilson interval is $(0.883, 0.991)$. A few dozen cases can estimate the sensitivity only to about ±10 percentage points, and a study of diagnostic accuracy that reports point estimates must also report confidence intervals (reporting guidelines in [7.7.21](/7.7.21)).

### 5.6.3. Zero Events

A study observes no serious adverse reaction among 50 patients receiving a new therapy. Can we say that the therapy "has no serious adverse reactions"? No: $\hat p = 0$, but the true risk may not be zero. The one-sided 95% upper confidence limit solves $(1 - p_U)^{50} = 0.05$, giving $p_U = 1 - 0.05^{1/50} = 0.058$. A convenient approximation is $3/n = 0.06$: when no event is observed in $n$ cases, the 95% upper confidence limit is about $3/n$. To exclude a risk above 1% with 95% confidence, at least 300 people must be observed without an event. This explains why premarketing trials (usually a few thousand people) cannot detect rare adverse reactions below one in a thousand, and postmarketing surveillance is needed.

## 5.7. Confidence Intervals for Poisson Counts and Rates

Counts of rare events (deaths, cases) are often described by the Poisson distribution (Section 4.3 of [7.7.4](/7.7.4)).

**Formula 5.7.1 (Exact Confidence Interval for a Poisson Mean)** When $x$ events are observed, the exact $100(1 - \alpha)\%$ confidence interval for the Poisson mean $\mu$ is

$$
\left(\tfrac12\chi^2_{2x,\, 1-\alpha/2},\ \tfrac12\chi^2_{2(x+1),\, \alpha/2}\right),
$$
with lower limit 0 when $x = 0$. If these events occurred in $T$ person-years, the interval for the rate $\lambda = \mu/T$ is obtained by dividing each end by $T$. For large $x$ ($x \ge 20$ or so) the approximation $x \pm z_{\alpha/2}\sqrt x$ can be used.

This interval comes from the relation between the Poisson and gamma distributions (and hence the chi-square distribution), on the same principle as the Clopper–Pearson interval.

**Example 5.7.1 (An occupational cohort)** In a 10-year follow-up of 8418 rubber workers, 4 deaths from Hodgkin's disease were observed (Andjelkovic et al. 1976). The 95% confidence interval for the expected number of deaths $\mu$ is $(\frac12\chi^2_{8, 0.975}, \frac12\chi^2_{10, 0.025}) = (1.09, 10.24)$. With only 4 cases the upper and lower limits differ by nearly a factor of 10. In the same cohort there were 21 deaths from bladder cancer, with a 95% interval of $(13.00, 32.10)$. Comparison with the number expected from general population mortality is the standardized mortality ratio of [7.7.6](/7.7.6).

**Example 5.7.2 (Lung cancer mortality in the NLST)** In the low-dose CT group of the NLST there were 356 lung cancer deaths in about 144,000 person-years, a mortality of 247 per 100,000 person-years (Aberle et al. 2011). The exact 95% interval for $\mu$ is $(320.0, 395.0)$, which converts to a mortality of 222–274 per 100,000 person-years; the approximation $356 \pm 1.96\sqrt{356} = (319.0, 393.0)$ is almost the same. The radiograph group had 443 deaths, 309 per 100,000 person-years, and the rate ratio of the two groups, 0.80, with its interval is in [7.7.16](/7.7.16).

## 5.8. One-Sided Confidence Intervals

Sometimes only one direction of the parameter matters: how high the adverse reaction rate of a new drug can be at most, how high the concentration of a pollutant can be at most, how large the efficacy of a new therapy is at least.

**Formula 5.8.1 (One-Sided Confidence Limits)** The one-sided $100(1 - \alpha)\%$ **upper confidence limit** for $\mu$ is $\bar x + t_{n-1,\alpha}\, s/\sqrt n$ and the lower confidence limit is $\bar x - t_{n-1,\alpha}\, s/\sqrt n$. The quantile is $t_{n-1,\alpha}$ rather than $t_{n-1,\alpha/2}$: all of $\alpha$ is placed on one side.

Example: the one-sided 95% upper confidence limit for the mean birth weight of infants of smoking mothers is $2771.9 + 1.666 \times 76.7 = 2899.7$ g ($t_{73, 0.05} = 1.666$), tighter than the upper limit 2924.7 g of the two-sided interval. A one-sided interval must be decided on before seeing the data, according to the research question, and cannot be adopted because the two-sided interval "does not look good enough" (Section 6.1.5 of [7.7.6](/7.7.6)). The zero-event upper limit of Section 5.6.3 is also a one-sided interval.

## 5.9. Sample Size and Margin of Error

When designing a study, first decide how precisely the parameter is to be estimated (the margin of error $E$) and then work back to the required sample size.

**Formula 5.9.1 (Sample Size for Estimation)** To estimate a mean to within $\pm E$ at confidence level $100(1 - \alpha)\%$ requires

$$
n = \left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^2;
$$
to estimate a proportion to within $\pm E$ requires

$$
n = \frac{z_{\alpha/2}^2\, p(1 - p)}{E^2}.
$$
Round up the result. Since $\sigma$ and $p$ are unknown, substitute values from a pilot study, the literature or a conservative guess; when nothing is known about a proportion take $p = 0.5$ (which maximizes $p(1 - p)$).

**Example 5.9.1** To estimate the mean birth weight of newborns in a region to within ±100 g with 95% confidence, take $\sigma = 729$ g: $n = (1.96 \times 729/100)^2 = 204.2$, so 205 newborns are needed. To estimate the smoking rate of pregnant women to within ±3 percentage points with nothing known about the smoking rate, take $p = 0.5$: $n = 1.96^2 \times 0.25/0.03^2 = 1067.1$, so 1068 people are needed; if the smoking rate is expected to be about 20%, only 683 are needed. These formulas assume simple random sampling, and for cluster sampling they must also be multiplied by the design effect.

Note that the formulas guarantee only the margin of error and not the ability to "detect a difference": the sample size for a test must take power into account, see Section 6.4 of [7.7.6](/7.7.6).

## 5.10. Bootstrap Confidence Intervals

For statistics such as the median, a ratio, a correlation coefficient or the AUC, the sampling distribution has no simple formula, or the formula depends on doubtful distributional assumptions. The **bootstrap** substitutes computation for derivation: the sample is treated as an approximation of the population, repeated samples are drawn from it with replacement, and the distribution of the statistic over these "bootstrap samples" approximates its sampling distribution (principle and theory in [3.5.7](/3.5.7)).

**Algorithm 5.10.1 (Percentile Bootstrap Interval)** Let the sample be $x_1, \dots, x_n$ and the statistic $\hat\theta$.

1. Draw $n$ values from $x_1, \dots, x_n$ with replacement to form a bootstrap sample and compute the statistic $\hat\theta^*$;
2. Repeat step 1 $B$ times ($B$ a few thousand to ten thousand) to obtain $\hat\theta^*_1, \dots, \hat\theta^*_B$;
3. Take the standard deviation of $\hat\theta^*$ as the estimate of the standard error of $\hat\theta$, and the 2.5th and 97.5th percentiles of $\hat\theta^*$ as the 95% confidence interval.

**Example 5.10.1 (Median of FEV)** The median FEV of the 654 children is 2.548 L. With 10,000 bootstrap resamples of the 654 children, the standard deviation of the bootstrap medians (the standard error) is 0.040 L and the 95% percentile interval is $(2.459, 2.619)$ L (panel A below). For comparison, the distribution-free interval based on order statistics (the 302nd and 353rd ordered values) is $(2.458, 2.631)$ L, close to the bootstrap result. The bootstrap distribution of the median is jagged: the median can take only values in the sample, which is typical of a discrete statistic in the bootstrap, and with small samples the percentile interval is not very reliable.

**Example 5.10.2 (Ratio of means)** The ratio of the mean FEV of smoking children to that of nonsmoking children is $3.277/2.566 = 1.277$. Bootstrapping separately within the two groups (keeping the sample size of each group), the 95% percentile interval for the ratio is $(1.200, 1.358)$ (panel B below): the mean FEV of smoking children is 20%–36% higher than that of nonsmoking children. The interval for this "paradox" is narrow, showing that the problem lies not in random error but in the different ages of the two groups ([7.7.10](/7.7.10)).

![Bootstrap confidence intervals for the FEV data (654 children in East Boston; Tager et al. 1979; the public version is from the Vanderbilt Department of Biostatistics database). A: bootstrap distribution of the median FEV of all children (10,000 resamples with replacement); the shaded area is the 95% percentile interval between the 2.5th and 97.5th percentiles; the median can take only values in the sample, so the distribution is jagged. B: bootstrap distribution of the ratio of mean FEV of smoking to nonsmoking children (resampling within each group)](./plots/bootstrap.py)

The bootstrap presupposes that the sample represents the population (independent and identically distributed); it cannot correct a biased sample and cannot handle correlated data (for repeated measurements and cluster samples one resamples by individual or by cluster). The percentile interval has inaccurate coverage when the statistic is biased or the distribution skewed, and the bias-corrected BCa interval can be used ([3.5.7](/3.5.7)).

## 5.11. A Glimpse of Bayesian Estimation

The frequentist approach treats the parameter as a fixed unknown constant, and the "95%" of a confidence interval is a long-run property of the method. The Bayesian approach also expresses the uncertainty about the parameter with a probability distribution: the knowledge before the study is written as the **prior distribution**, combined with the **likelihood function** of the data to give the **posterior distribution**, from which one reads directly the probability that the parameter lies in an interval ([3.2.7](/3.2.7)).

**Example 5.11.1 (Response rate in a phase II trial)** In a phase II trial of a new antitumor drug, 6 of 20 patients had tumor shrinkage (a response). Let the prior of the response rate $p$ be a beta distribution $\mathrm{Beta}(a, b)$. The product of the binomial likelihood $p^6(1 - p)^{14}$ and the beta prior is again a beta distribution (a **conjugate prior**), and the posterior is $\mathrm{Beta}(a + 6, b + 14)$.

- The noninformative uniform prior $\mathrm{Beta}(1, 1)$: the posterior is $\mathrm{Beta}(7, 15)$, the posterior mean is $7/22 = 0.318$, and the 95% **credible interval** (the 2.5th and 97.5th percentiles of the posterior) is $(0.146, 0.522)$. The posterior probability that "the response rate exceeds 20%" is 0.89. For comparison, the frequentist Clopper–Pearson interval is $(0.119, 0.543)$ and the Wilson interval $(0.145, 0.519)$.
- The informative prior $\mathrm{Beta}(2, 8)$ (the historical response rate of similar drugs is about 20%, equivalent to the information of 10 patients): the posterior is $\mathrm{Beta}(8, 22)$, with mean 0.267, 95% credible interval $(0.127, 0.435)$ and $\mathbb{P}(p > 0.2 \mid \text{data}) = 0.79$. The prior pulls the estimate toward 0.2.

![Bayesian estimation of a response rate: 6 of 20 patients responded in a phase II trial. A: under the uniform prior Beta(1, 1) the posterior is Beta(7, 15), essentially the normalized likelihood. B: under the informative prior Beta(2, 8) (mean 0.2, equivalent to 10 historical patients) the posterior Beta(8, 22) is pulled toward 0.2. Shaded areas are 95% equal-tailed credible intervals. Illustrative values](./plots/beta-binomial.py)

The beta prior $\mathrm{Beta}(a, b)$ can be understood as "having already observed $a - 1$ responses and $b - 1$ nonresponses" (for the uniform prior, $a = b = 1$ amounts to no data), and the posterior simply adds the new data. The more data, the smaller the influence of the prior. Bayesian methods are useful in early clinical trials: they can directly answer "how probable is it that the response rate of the new drug exceeds that of the standard therapy", and are updated continually as data accumulate to decide whether to continue the trial. The price is that the choice of prior must be justified, and the sensitivity of the conclusions to the prior should be reported.

## 5.12. Computing with Python

```python
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportion_confint

bw = pd.read_csv("birthwt.csv")
x = bw.loc[bw.smoke == 1, "bwt"]

# t interval for a mean (Example 5.4.1)
res = stats.ttest_1samp(x, popmean=0)
print(res.confidence_interval(0.95))            # (2619.1, 2924.7)
print(stats.t.interval(0.95, df=len(x) - 1, loc=x.mean(), scale=stats.sem(x)))

# chi-square interval for a variance (Example 5.5.1)
s2, n = 8.178, 10
print((n - 1) * s2 / stats.chi2.isf(0.025, n - 1), (n - 1) * s2 / stats.chi2.ppf(0.025, n - 1))   # 3.87, 27.26

# intervals for a proportion (Examples 5.6.1 and 5.6.2)
for method in ["normal", "wilson", "beta"]:     # "normal" = Wald, "beta" = Clopper-Pearson
    print(method, proportion_confint(30, 74, alpha=0.05, method=method))
print(stats.binomtest(56, 58).proportion_ci(confidence_level=0.95, method="wilson"))
print(1 - 0.05 ** (1 / 50))                     # zero events in 50: one-sided upper limit 0.058

# exact Poisson interval (Example 5.7.1)
x_obs = 4
print(stats.chi2.ppf(0.025, 2 * x_obs) / 2, stats.chi2.isf(0.025, 2 * (x_obs + 1)) / 2)   # 1.09, 10.24

# bootstrap percentile interval for a median (Example 5.10.1)
fev = pd.read_csv("fev.csv")["fev"].to_numpy()
res = stats.bootstrap((fev,), np.median, n_resamples=10000, method="percentile",
                      random_state=np.random.default_rng(0))
print(res.confidence_interval, res.standard_error)

# Beta-binomial posterior (Example 5.11.1)
post = stats.beta(1 + 6, 1 + 14)
print(post.mean(), post.ppf([0.025, 0.975]), post.sf(0.2))   # 0.318, (0.146, 0.522), 0.89
```

## Summary

- Probability sampling (simple random, systematic, stratified, cluster; Definition 5.1.1) makes the sample representative of the population and sampling error computable; the bias of a convenience sample cannot be corrected by enlarging the sample. Stratification raises precision, clustering lowers it (design effect), and weights must be used when analyzing complex samples.
- Randomization (Definition 5.2.1) makes the groups differ only randomly and is the basis of causal inference and of tests; block and stratified randomization ensure balance (Definition 5.2.2), allocation concealment and blinding (Definition 5.2.3) prevent selection bias and assessment bias; a factorial design answers two questions at once (Example 5.2.1).
- A point estimate is judged by unbiasedness, standard error and mean squared error; $S^2$ is unbiased only when divided by $n - 1$ (Theorem 5.3.1); maximum likelihood is the general method for constructing estimators (Example 5.3.1).
- Summary of confidence intervals:

  | Parameter | Interval | Conditions |
  |---|---|---|
  | Mean | $\bar x \pm t_{n-1,\alpha/2}\, s/\sqrt n$ (Formula 5.4.1) | Normal or large sample |
  | Variance | $\left((n-1)s^2/\chi^2_{n-1,\alpha/2},\ (n-1)s^2/\chi^2_{n-1,1-\alpha/2}\right)$ (Formula 5.5.1) | Strictly normal |
  | Proportion | Wilson (Definition 5.6.1); Clopper–Pearson when conservative (Definition 5.6.2); not Wald | Binomial |
  | Poisson mean and rate | $\left(\frac12\chi^2_{2x,1-\alpha/2},\ \frac12\chi^2_{2(x+1),\alpha/2}\right)$, divided by person-time (Formula 5.7.1) | Rare events |
  | Any statistic | Bootstrap percentile interval (Algorithm 5.10.1) | Independent and identically distributed, representative sample |

- The 95% refers to the long-run coverage of the method that constructs the interval (about 95 of 100 intervals cover the true value), not the probability that one particular interval contains the true value; an interval reflects only random error, not bias.
- With zero events the 95% upper limit is about $3/n$; one-sided intervals must be decided in advance (Formula 5.8.1); the sample size for estimation is $n = (z\sigma/E)^2$ or $z^2p(1-p)/E^2$ (Formula 5.9.1).
- Bayesian estimation: beta prior + binomial data → beta posterior, and a credible interval can be interpreted directly as a probability interval for the parameter (Example 5.11.1).

## Questions

1. Determine the type of each of the following sampling methods and point out possible biases: (a) from the discharge records of a hospital in 2023, take 1 of every 20 records by record number; (b) randomly draw 30 primary schools in a city and measure the vision of all fourth graders in each school; (c) divide the residents of a city into 40 strata by district and age group and randomly draw 50 people from each stratum; (d) recruit waiting-room patients in a hospital hall who are willing to fill in a questionnaire.

   **Answer** (a) Systematic sampling. If the numbering of the records has a periodicity (such as every 20 numbers forming a ward or a day's admissions), certain kinds of patients may be systematically missed or overrepresented; in general it approximates a simple random sample. (b) Cluster sampling (schools are the clusters). Students of the same school have similar visual environments, so precision is lower than for a simple random sample of the same size, and correlation within schools must be accounted for in the analysis. (c) Stratified sampling. If the strata have different populations while 50 are drawn from every stratum, the sampling fractions differ between strata, and the estimate of the prevalence in the city must be weighted by the population proportions of the strata. (d) Convenience sampling. People in the waiting room are those seeking care, and their health, age and schedules differ from the general population; volunteers and refusers may also differ; the results cannot be generalized to the city and the direction and size of the bias cannot be estimated.

2. A two-group trial plans to enroll 24 participants using simple randomization (an independent coin toss for each). What is the probability that the group sizes differ by 8 or more (that is, one group has ≤ 8 people)? What does block randomization (block length 4) guarantee?

   **Answer** The size of one group is $X \sim \mathrm{Bin}(24, 0.5)$, and $\mathbb{P}(X \le 8 \text{ or } X \ge 16) = 2\,\mathbb{P}(X \le 8) = 2 \times 0.0758 = 0.152$. About 15% of trials would have an allocation of 8:16 or more unbalanced, reducing the efficiency of the comparison. With block length 4, every 4 participants enrolled have 2 in each group, the difference between the group sizes never exceeds 2 at any time, and the final 24 are exactly 12:12.

3. A study measured the fasting glucose of 25 diabetic patients, with mean 8.6 mmol/L and standard deviation 2.1 mmol/L. Find the 95% and 99% confidence intervals for the population mean. If the sample size is increased to 100 with the sample statistics unchanged, by what factor does the width of the 95% interval change?

   **Answer** The standard error is $2.1/5 = 0.42$. With $t_{24, 0.025} = 2.064$ the 95% interval is $8.6 \pm 0.867 = (7.73, 9.47)$; with $t_{24, 0.005} = 2.797$ the 99% interval is $8.6 \pm 1.175 = (7.43, 9.78)$. For $n = 100$ the standard error is 0.21 and $t_{99, 0.025} = 1.984$, so the 95% interval is $8.6 \pm 0.417 = (8.18, 9.02)$; the width falls from 1.73 to 0.83, about 48% of the original: $\sqrt{25/100} = 1/2$ comes from the sample size, and the remainder $1.984/2.064$ from the decrease of the $t$ quantile.

4. One investigator reports: "The 95% confidence interval of this study is (2.1, 3.5), so there is a 95% probability that the population mean lies between 2.1 and 3.5." Another says: "If this study is repeated, 95% of the sample means will fall in (2.1, 3.5)." Are the two statements correct? What is the correct statement?

   **Answer** Neither is correct. The first treats the true value as random; in the frequentist framework the true value is fixed, and a particular interval either contains it or does not. The second is also wrong: (2.1, 3.5) is centered on the sample mean of this study, whereas future sample means are centered on the true value; it can be shown that the average probability that a future sample mean falls within this 95% interval is only about 83%. The correct statement is: when intervals are constructed by this method, 95% of the intervals in repeated sampling will cover the true population mean; this particular interval was obtained by a method that is "95% reliable".

5. A new test for a rare disease detects all 40 confirmed patients as positive. What is wrong with reporting "sensitivity 100%"? Give the 95% Clopper–Pearson and Wilson intervals for the sensitivity.

   **Answer** 40/40 only means that no case was missed in this sample; the true sensitivity may be below 100%. Clopper–Pearson: the lower limit solves $p_L^{40} = 0.025$, giving $p_L = 0.025^{1/40} = 0.912$, so the interval is $(0.912, 1)$; the lower limit of the Wilson interval is also 0.912. That is, the data are compatible with a sensitivity as low as 91%. Spectrum bias should also be noted: confirmed patients often have more severe disease (Section 3.3.6 of [7.7.3](/7.7.3)), and the sensitivity in actual use may be lower.

6. A city reported 7 cases of a rare tumor in the past year, and its population is 1.2 million. Find the annual incidence (per 100,000 person-years) and its exact 95% confidence interval. If the national incidence is 0.3 per 100,000 person-years, is the city's incidence high?

   **Answer** The incidence is $7/120 = 0.583$ per 100,000 person-years. The 95% interval for $\mu$ is $(\frac12\chi^2_{14, 0.975}, \frac12\chi^2_{16, 0.025}) = (2.81, 14.42)$, and dividing by 12 (in units of 100,000 person-years) gives $(0.235, 1.202)$ per 100,000 person-years. The national rate of 0.3 lies within the interval, so the data are compatible with the national level and do not show that the city is high: the difference between 7 cases and the expected 3.6 may be only random fluctuation of a count of rare events. The formal test is the one-sample Poisson test ([7.7.6](/7.7.6)), and one should also beware of the multiple comparison problem of "picking the highest among many cities".

7. A cross-sectional survey plans to estimate the prevalence of hepatitis B surface antigen among adults in a region, expected to be about 6%, with a 95% confidence interval half-width of at most 1 percentage point. How many people are needed? If cluster sampling by village is used with an estimated design effect of 2.5, how many are needed?

   **Answer** $n = 1.96^2 \times 0.06 \times 0.94/0.01^2 = 2166.6$, so 2167 people are needed. With cluster sampling, multiply by the design effect: $2167 \times 2.5 = 5417$ people. In addition, when the prevalence is near 0 the interval is asymmetric, and the calculation can be checked against the formula for the Wilson interval; allowing for 10%–20% refusals, the number of people actually to be surveyed must be increased accordingly.

8. Why is the bootstrap distribution of the median of the FEV data jagged? If the sample has only 15 people, is the bootstrap percentile interval still reliable? What is an alternative?

   **Answer** The median is the middle observation (or the average of two) after sorting, and the median of a bootstrap sample can take only a few values of the original sample (or averages of them), so the bootstrap distribution is concentrated on discrete points and looks jagged. When the sample is very small (such as 15 people), the bootstrap distribution has mass at only a few values, the coverage of the percentile interval may deviate markedly from 95%, and the sample may not represent the shape of the population. An alternative is the distribution-free interval based on order statistics: for the median one can use the binomial distribution $\mathrm{Bin}(n, 0.5)$ to choose the order statistics $x_{(k)}$ and $x_{(n-k+1)}$ so that the coverage is at least 95% ($k = 4$ for $n = 15$, with coverage 0.965); its coverage is guaranteed exactly.

9. In a phase I trial of a vaccine, 0 of 30 participants had serious adverse reactions. (a) Give the one-sided 95% upper confidence limit for the rate of serious adverse reactions (exact method and the 3/n approximation). (b) With the uniform prior $\mathrm{Beta}(1, 1)$, what is the posterior distribution? What is its 95% quantile? Compare the results of the two methods.

   **Answer** (a) The exact upper limit is $1 - 0.05^{1/30} = 0.095$, and $3/n = 0.100$. (b) The posterior is $\mathrm{Beta}(1, 31)$, with distribution function $1 - (1 - p)^{31}$ and 95% quantile $1 - 0.05^{1/31} = 0.092$. The two methods give almost the same upper limit (about 9%–10%): 30 people without events can exclude only risks above about 10%. The difference lies in the interpretation: the frequentist upper limit is "this method is not below the true value in 95% of cases"; the Bayesian conclusion is "under the uniform prior, the posterior probability that the risk does not exceed 9.2% is 95%".

10. (Open question) A company recruits 5000 volunteers online, measures heart rate variability with a smartphone application, and on this basis gives "reference values of heart rate variability for Chinese adults". As a reviewer, what comments would you make on the sampling and estimation?

    **Answer** Key points: (1) Sampling: online volunteers are a convenience sample, biased toward young, well-educated, health-conscious people with new smartphones, and cannot represent Chinese adults; a large sample size cannot correct this bias (Section 5.1.1). The recruitment method and response rate should be stated and the age, sex and regional composition compared with the census; for generalization, stratified probability sampling or at least weighting by the population composition should be used. (2) Measurement: measurements by a smartphone application must be compared with the standard method (electrocardiography) for agreement (the Bland–Altman method of [7.7.11](/7.7.11)). (3) Estimation: reference intervals should be given by age and sex strata, using percentiles rather than "mean ± 2 standard deviations" (heart rate variability is right-skewed, [7.7.2](/7.7.2)), with confidence intervals for the percentiles (for example by bootstrap). (4) Exclusion criteria: the reference population should exclude people with cardiovascular disease or taking drugs that affect heart rate.
