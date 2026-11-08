---
title: Probability Distributions and Sampling Distributions
description: Random variables, expectation and variance; the use and conditions of the binomial, Poisson and normal distributions in biomedicine; the normal approximation and continuity correction; the log-normal, exponential, Weibull and negative binomial distributions; sampling distributions of the sample mean and proportion and the central limit theorem; the chi-square, t and F distributions derived from the normal. Illustrated with birth weight, differential white cell counts, colony counts, incubation periods and lung cancer survival times.
source_hash: 4f910b2afdf9
---

[7.7.3](/7.7.3) used probability to describe single events: one positive test, one person with a disease. This chapter shifts the viewpoint from events to **random variables**: how many children in a family are affected, how many colonies grow on a culture dish, how much a newborn weighs, how long a lung cancer patient will live. Each kind of number has a "typical" probability distribution, determined by the mechanism that generates the data: independent yes-or-no trials give the binomial distribution, counts of rare events give the Poisson distribution, the superposition of many small factors gives the normal distribution, multiplicative superposition gives the log-normal distribution, and the waiting time under a constant hazard gives the exponential distribution. Knowing these distributions is useful in two ways: to compute probabilities from mechanisms ("if smoking is unrelated to birth weight, how likely is it to see 30 low birth weight infants among 74 smoking mothers?") and to provide models for the estimation and testing that follow. The second half of the chapter turns to the central objects of statistical inference, **sampling distributions**: the sample mean and sample proportion vary from sample to sample, and the **central limit theorem** tells us that they are approximately normally distributed, which is the common basis of the confidence intervals of [7.7.5](/7.7.5) and the hypothesis tests of [7.7.6](/7.7.6). The mathematical definitions, properties and proofs of the distributions are in [3.1.4](/3.1.4), [3.1.13](/3.1.13) and [3.2.2](/3.2.2); this chapter treats their conditions, their use and how they look in biomedical data. The main datasets remain birthwt (birth weight), FEV (children's lung function) and veteran (the lung cancer chemotherapy trial), and the laboratory examples are differential white cell counts and colony counts.

## 4.1. Random Variables and Probability Distributions

### 4.1.1. Random Variables

**Definition 4.1.1 (Random Variable)** A rule that assigns a numerical value to each possible outcome of a random experiment is a **random variable**. One that takes finitely or countably many values is a **discrete random variable** (the number of episodes of otitis media a child has before age 2, the number of affected children in a family); one that can take any value in an interval is a **continuous random variable** (birth weight, serum cholesterol, survival time).

A random variable is denoted by a capital letter $X$ and an observed value of it by a lowercase $x$. A discrete random variable is described by its **probability mass function** $\mathbb{P}(X = k)$; a continuous random variable has probability 0 of taking any specific value and is described by its **probability density function** $f(x)$, with the probability on an interval being the area under the density curve: $\mathbb{P}(a < X \le b) = \int_a^b f(x)\,\mathrm{d}x$. Both kinds can be described uniformly by the **distribution function** $F(x) = \mathbb{P}(X \le x)$, whose inverse gives the **quantiles**.

A probability distribution is the theoretical model of a population, and the frequency distribution of a sample is its empirical counterpart: when we sample from a population, the relative frequencies in the sample approach the probability distribution as the sample size grows (the histogram of [7.7.2](/7.7.2) is an estimate of the density curve). The method for testing from a sample whether the data conform to a given distribution is the **goodness-of-fit test** ([7.7.9](/7.7.9)).

### 4.1.2. Expectation and Variance

The center and the spread of a distribution are summarized by the expectation and the variance, the population counterparts of the sample mean and the sample variance of [7.7.2](/7.7.2).

**Formula 4.1.1 (Expectation and Variance)** The **expectation** and **variance** of a discrete random variable are

$$
\mu = \mathbb{E}[X] = \sum_k k\,\mathbb{P}(X = k), \qquad \sigma^2 = \operatorname{Var}(X) = \mathbb{E}[(X - \mu)^2] = \mathbb{E}[X^2] - \mu^2;
$$
for a continuous variable the sum is replaced by the integral $\int x f(x)\,\mathrm{d}x$. The **standard deviation** $\sigma = \sqrt{\operatorname{Var}(X)}$ has the same unit as $X$.

**Formula 4.1.2 (Linear Operations)** For constants $a, b$, $\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b$ and $\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X)$. For any random variables $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$; if $X$ and $Y$ are independent, also $\operatorname{Var}(X \pm Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$.

Note that the variance of the difference of two independent variables is also the sum of the variances: the difference is more uncertain than either one. When they are not independent, the covariance term $\pm 2\operatorname{Cov}(X, Y)$ must be added, and the paired design makes use of a positive covariance to reduce the variance of the difference ([7.7.7](/7.7.7)).

**Example 4.1.1 (Pooled sample testing)** In a region with limited resources, an infection with a prevalence of 10% is to be screened in 500 blood samples. Half of each of $m$ samples is taken and mixed into one tube for testing: if the pooled sample is negative, all $m$ are negative and only 1 test is used; if it is positive, the samples are tested one by one, for $m + 1$ tests in all (assuming the test is perfectly accurate). The number of tests $X$ for each group is a random variable taking two values,

$$
\mathbb{E}[X] = 1 \times 0.9^m + (m + 1)(1 - 0.9^m).
$$
For $m = 20$, $\mathbb{E}[X] = 18.57$, about 464 tests for 25 groups; for $m = 10$, $\mathbb{E}[X] = 7.51$, about 376 tests for 50 groups; for $m = 5$, $\mathbb{E}[X] = 3.05$, about 305 tests for 100 groups, a saving of nearly 40% compared with testing individually. The optimal group size depends on prevalence: the lower the prevalence, the larger the group can be. This method was proposed by Dorfman in 1943 for screening US Army draftees for syphilis and was widely used in 2020 for COVID-19 nucleic acid testing.

## 4.2. The Binomial Distribution

### 4.2.1. Bernoulli Trials

A random experiment with only two outcomes ("success" and "failure") is a Bernoulli trial; the outcomes are coded 1 and 0 and the probability of "success" is $p$, the **Bernoulli distribution** $\mathrm{Ber}(p)$. "Success" is only a label: that a newborn is a boy, that a white cell is a neutrophil, or that a patient dies within 30 days may all be coded as "success".

**Definition 4.2.1 (Binomial Distribution)** Repeat a Bernoulli trial $n$ times. If

1. the number of trials $n$ is fixed in advance;
2. each trial has only two outcomes;
3. the probability $p$ of "success" is the same in every trial;
4. the trials are mutually independent,

then the number of successes $X$ follows the **binomial distribution** $\mathrm{Bin}(n, p)$:

$$
\mathbb{P}(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \qquad k = 0, 1, \dots, n.
$$
Its expectation and variance are $\mathbb{E}[X] = np$ and $\operatorname{Var}(X) = np(1 - p)$.

Here $\binom{n}{k}$ is the number of ways to choose $k$ successes among $n$ trials, and $p^k(1 - p)^{n-k}$ is the probability of any one particular order. The expectation and variance follow directly from the fact that $X$ is the sum of $n$ independent $\mathrm{Ber}(p)$ variables: each has expectation $p$ and variance $p(1-p)$, which add by Formula 4.1.2. For $p = 0.5$ the distribution is symmetric; as $p$ departs from 0.5 it becomes skewed, and the skewness weakens as $n$ grows (figure below).

### 4.2.2. Examples

**Example 4.2.1 (Sex ratio and differential white cell count)** The probability that a newborn is a boy is about 0.51. In a family with 5 children, the probability of exactly 2 boys is $\binom{5}{2}\,0.51^2\,0.49^3 = 0.306$. In a differential white cell count on a blood smear, about 60% of the white cells of a normal person are neutrophils; if 5 white cells are counted at random, the number of neutrophils $X \sim \mathrm{Bin}(5, 0.6)$ has the distribution

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\mathbb{P}(X = k)$ | 0.010 | 0.077 | 0.230 | 0.346 | 0.259 | 0.078 |

A differential count usually classifies 100 cells; the distribution in that case and its normal approximation are in Section 4.5.

**Example 4.2.2 (Familial aggregation)** A researcher found that in 20 families in which both parents had bronchitis, the infants of 3 families developed chronic bronchitis within the first year of life, while the national incidence within the first year is 5%. If the infants of these families had the same risk as infants nationally, the number of families with an affected infant would be $X \sim \mathrm{Bin}(20, 0.05)$, with an expectation of only 1. The probability of at least 3 is

$$
\mathbb{P}(X \ge 3) = 1 - \mathbb{P}(X = 0) - \mathbb{P}(X = 1) - \mathbb{P}(X = 2) = 1 - 0.358 - 0.377 - 0.189 = 0.075.
$$
Under the assumption that the risk is not raised, such a result is not rare (about 1 in 13): with only 20 families, the evidence is insufficient to show that parental bronchitis raises the risk for the infants. This reasoning is the one-sample binomial test ([7.7.6](/7.7.6)).

**Example 4.2.3 (Low birth weight among smoking mothers)** In the birthwt data, 29 of the 115 infants of nonsmoking mothers had low birth weight (< 2500 g), a proportion of 0.252. If smoking did not affect birth weight, the number of low birth weight infants among the 74 smoking mothers would follow $\mathrm{Bin}(74, 0.252)$, with expectation $74 \times 0.252 = 18.7$ and standard deviation $\sqrt{74 \times 0.252 \times 0.748} = 3.74$. The number actually observed is 30,

$$
\mathbb{P}(X \ge 30) = \sum_{k=30}^{74} \binom{74}{k} 0.252^k\, 0.748^{74-k} = 0.0027.
$$
If smoking were really unrelated, so many low birth weight infants would occur only about once in 370 times. Here 0.252 is treated as a known constant, ignoring that it is itself estimated from 115 people; the method that treats the two groups symmetrically is the two-proportion test of [7.7.9](/7.7.9).

:::

![Three binomial distributions in this course (computed exactly). A: the number of families with an affected infant among 20 families with parental bronchitis, assuming each infant has the national risk of 5%; 3 were observed, P(X ≥ 3) = 0.075. B: the number of low birth weight infants among the 74 smoking mothers in the birthwt data, assuming the same risk as nonsmoking mothers (29/115); 30 were observed, P(X ≥ 30) = 0.0027. C: the number of neutrophils among 100 white cells (p = 0.6) and its normal approximation N(60, 24), with the bars of the normal range 50–75 colored](./plots/binomial.py)

### 4.2.3. When the Conditions Fail

The four conditions of the binomial distribution often hold only approximately in biomedical data, and the last two are the most easily violated.

- Independence: siblings in the same family, patients in the same ward and mice in the same litter often have correlated outcomes. Positive correlation makes the number of "successes" more dispersed than the binomial (overdispersion): either many or few. Analyzing the mice of one litter as independent individuals underestimates the variance (pseudoreplication in [7.7.12](/7.7.12), clustered data in [7.7.17](/7.7.17)).
- Equal probability: different individuals have different risks (age, genotype); when the counts are pooled and the individual $p_i$ come from a distribution, the count follows a mixture more dispersed than the binomial, the most common being the **beta-binomial distribution**.

A simple check is to compare the sample variance with $n\hat p(1 - \hat p)$: when the former is clearly larger, the standard errors and p-values given by the binomial model are too optimistic.

## 4.3. The Poisson Distribution

### 4.3.1. Counts of Rare Events

The number of cases of a rare disease admitted by a hospital in a period, the number of colonies on a culture dish, the number of cells in a small square of a hemocytometer, and the number of mutations in a stretch of DNA are all counts arising from "a large number of opportunities, each with a very small probability".

**Definition 4.3.1 (Poisson Distribution)** If in a fixed period of time (or area, volume, length)

1. the probability of two or more events in a sufficiently short subinterval is negligible;
2. the probability that an event occurs is the same in any two subintervals of equal length;
3. events in non-overlapping intervals occur independently,

then the number of events $X$ in that period follows the **Poisson distribution** $\mathrm{Poi}(\mu)$:

$$
\mathbb{P}(X = k) = \frac{\mathrm{e}^{-\mu}\mu^k}{k!}, \qquad k = 0, 1, 2, \dots
$$
Its expectation and variance are both equal to $\mu$. If events occur at a constant rate $\lambda$ (the number of events per unit time or area), then $\mu = \lambda t$ in an interval of length $t$.

Equality of expectation and variance is the hallmark of the Poisson distribution: the standard deviation of a Poisson count is about $\sqrt{\mu}$, so a count with mean 100 fluctuates roughly between 80 and 120, with a relative error of $1/\sqrt{\mu} = 10\%$. This is why, in counting experiments (colonies, cells, radioactive decays, sequencing reads), "the more you count, the more accurate" (Poisson noise in the number of molecules in a cell is in [7.6.32](/7.6.32)). For small $\mu$ the distribution is right-skewed, and it becomes symmetric as $\mu$ increases (panel A below).

### 4.3.2. The Poisson Approximation

The **Poisson limit theorem** ([3.1.4](/3.1.4)) states that when $n$ is large, $p$ is small and $np = \mu$ is moderate, $\mathrm{Bin}(n, p) \approx \mathrm{Poi}(np)$. Empirically the approximation is already good when $n \ge 100$ and $p \le 0.01$:

| $k$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\mathrm{Bin}(100, 0.01)$ | 0.3660 | 0.3697 | 0.1849 | 0.0610 | 0.0149 |
| $\mathrm{Poi}(1)$ | 0.3679 | 0.3679 | 0.1839 | 0.0613 | 0.0153 |

This makes the Poisson distribution the standard model for case counts in epidemiology: in a large population each person has a very small probability of falling ill, and the total number of cases is approximately Poisson; one needs to know only the expected number of cases, not the number of people or each person's probability.

**Example 4.3.1 (Cases in person-time)** In the NLST the lung cancer mortality in the low-dose CT group was 247 per 100,000 person-years (Section 3.2.2 of [7.7.3](/7.7.3)). Suppose another screening cohort of heavy smokers accumulates 10,000 person-years; if the mortality is the same, the number of lung cancer deaths follows $\mathrm{Poi}(24.7)$, with standard deviation $\sqrt{24.7} = 5.0$. If the cohort observes only 20 deaths, $\mathbb{P}(X \le 20) = 0.20$: 5 fewer than expected is entirely within random fluctuation. If 31 deaths are observed (equivalent to the mortality of the radiograph group, 30.9), $\mathbb{P}(X \ge 31) = 0.12$. So even with 10,000 person-years it is hard to distinguish two situations whose mortalities differ by 20%, which is why the NLST needed more than 50,000 people followed for over 6 years (sample size calculations in [7.7.18](/7.7.18)).

**Example 4.3.2 (Colony counts)** On an agar plate of 100 cm², colonies are randomly distributed with a mean density of 0.1 per cm², so the number of colonies on the plate is $X \sim \mathrm{Poi}(10)$. Is it unusual to observe 20 colonies? $\mathbb{P}(X \ge 20) = 0.0035$: so many colonies are rarely produced by random fluctuation and more likely reflect too large an inoculum or contamination.

Actual plate counts are often more dispersed than the Poisson distribution: the inoculum, culture conditions and operators differ between plates, and the $\mu$ of each plate itself varies (panel C below). The variance then exceeds the mean, called overdispersion, which motivates the negative binomial distribution of Section 4.6.3.

![Poisson counts. A: Poisson distributions with means 1, 4 and 10; the larger the mean, the more symmetric. B: 200 simulated plates with an average of 10 colonies each (Poisson sampling), in agreement with the Poisson expectation, the variance being about equal to the mean. C: 200 simulated plates with the same mean but additional variation between plates (negative binomial, variance 30): the counts are overdispersed and the Poisson expectation is too narrow. Simulated data](./plots/poisson.py)

### 4.3.3. The Poisson Process and Waiting Times

If events occur randomly in time at a constant rate $\lambda$ (a **Poisson process**), the waiting time $T$ from any instant to the next event satisfies $\mathbb{P}(T > t) = \mathbb{P}(\text{no event in an interval of length } t) = \mathrm{e}^{-\lambda t}$, that is, $T$ follows the **exponential distribution** $\mathrm{Exp}(\lambda)$. This is the origin of the statement in [7.7.3](/7.7.3) that "with a constant incidence rate the cumulative incidence is $1 - \mathrm{e}^{-It}$". The exponential distribution has the **memoryless property**: a person who has already waited for $s$ has the same probability of waiting a further $t$ as one who has just begun to wait. For events whose hazard rises with age (most chronic diseases and death) this assumption fails, and one must use the Weibull distribution of Section 4.6.2 or the nonparametric methods of [7.7.16](/7.7.16).

## 4.4. The Normal Distribution

### 4.4.1. Medical Indices and the Normal Distribution

The distributions of height, adult weight, hemoglobin, serum cholesterol and birth weight in a homogeneous population are approximately symmetric and bell-shaped. An intuitive reason is that when a quantity is the sum of many mutually independent factors, each with a small effect (many genes, nutrition, environment), its distribution is close to normal, which is the content of the central limit theorem (Section 4.7).

**Definition 4.4.1 (Normal Distribution)** The distribution with density

$$
f(x) = \frac{1}{\sqrt{2\pi}\,\sigma} \exp\!\left[-\frac{(x - \mu)^2}{2\sigma^2}\right], \qquad -\infty < x < \infty
$$
is the **normal distribution** $\mathcal{N}(\mu, \sigma^2)$, where $\mu$ is the expectation and $\sigma^2$ the variance. The one with $\mu = 0$ and $\sigma = 1$ is the **standard normal distribution**, whose distribution function is denoted $\Phi(z)$.

The normal curve is symmetric about $\mu$, with the mean, median and mode coinciding; the inflection points are at $\mu \pm \sigma$. About 68.3% of the probability lies within $\mu \pm \sigma$, 95.0% within $\mu \pm 1.96\sigma$, 99.0% within $\mu \pm 2.58\sigma$ and 99.7% within $\mu \pm 3\sigma$. The interval $\mu \pm 1.96\sigma$ is the 95% **reference interval** under the normal distribution ([7.7.2](/7.7.2)).

Not all medical indices are approximately normal. Concentrations, titers, enzyme activities, lengths of stay and survival times are often right-skewed; data that mix different populations (healthy people and patients, men and women) may be bimodal. The word "normal" in "normal distribution" is the same word as in "normal" (healthy) people only by coincidence of terminology; the values of healthy people need not follow a normal distribution, and the judgment must rest on the data (the QQ plots of [7.7.2](/7.7.2)).

### 4.4.2. Standardization and Quantiles

**Formula 4.4.1 (Standardization)** If $X \sim \mathcal{N}(\mu, \sigma^2)$, then $Z = (X - \mu)/\sigma \sim \mathcal{N}(0, 1)$, and therefore

$$
\mathbb{P}(a < X \le b) = \Phi\!\left(\frac{b - \mu}{\sigma}\right) - \Phi\!\left(\frac{a - \mu}{\sigma}\right).
$$

$Z$ is the **z-score** of [7.7.2](/7.7.2). Under the normal distribution, z-scores can be converted into percentiles: $z = -1.645$ corresponds to the 5th percentile and $z = 1.96$ to the 97.5th percentile. Denote the upper $\alpha$ quantile of the standard normal distribution by $z_\alpha$, that is, $\mathbb{P}(Z > z_\alpha) = \alpha$: $z_{0.05} = 1.645$, $z_{0.025} = 1.960$ and $z_{0.005} = 2.576$. These numbers will appear in every later chapter.

**Example 4.4.1 (Birth weight)** In the birthwt data the 189 newborns have a mean birth weight of 2945 g and a standard deviation of 729 g. If birth weight followed $\mathcal{N}(2945, 729^2)$, the probability of low birth weight (< 2500 g) would be $\Phi\!\left(\frac{2500 - 2945}{729}\right) = \Phi(-0.61) = 0.271$, whereas the actual proportion is $59/189 = 0.312$; likewise the normal model gives the 2.5th and 97.5th percentiles as 1515 g and 4374 g, while the actual ones are 1554 g and 4157 g. By smoking status, the normal model gives proportions of low birth weight of 0.230 and 0.340 for the nonsmoking and smoking groups, against actual values of 0.252 and 0.405. The normal curve describes the middle of the distribution but underestimates the left tail: low birth weight is often associated with pathological processes such as prematurity, and these infants are not an extension of "normal variation". One must be especially careful in using a normal model to infer tail proportions (such as the number of people below a diagnostic threshold); it is best to use empirical proportions directly or to model the tail.

![Birth weight and the normal distribution (birthwt data: 189 newborns at Baystate Medical Center in 1986, Hosmer and Lemeshow; R package MASS). A: histogram of birth weight with the fitted normal density N(2945, 729²); the shaded area below 2500 g is the proportion of low birth weight estimated by the normal model. B: the same comparison by maternal smoking, with a short vertical tick for each newborn. The normal curve describes the middle but underestimates the proportion in the left tail](./plots/birthweight-normal.py)

### 4.4.3. Linear Combinations of Normal Variables

**Theorem 4.4.1** If $X_1, \dots, X_n$ are mutually independent with $X_i \sim \mathcal{N}(\mu_i, \sigma_i^2)$, then for constants $c_1, \dots, c_n$,

$$
\sum_{i=1}^n c_i X_i \sim \mathcal{N}\!\left(\sum_{i=1}^n c_i\mu_i,\ \sum_{i=1}^n c_i^2\sigma_i^2\right).
$$

The expectation and variance follow from Formula 4.1.2; "still normal" is a property peculiar to the normal distribution (for the proof see [Theorem 2.1.1 of 3.2.2](/3.2.2#thm-2.1.1)). Two useful corollaries:

- A single blood pressure measurement of one person is $X = \mu + \varepsilon$, with measurement error $\varepsilon \sim \mathcal{N}(0, \sigma^2)$; measuring twice and averaging reduces the variance of the error to $\sigma^2/2$ and the standard deviation to $\sigma/\sqrt2$. This is why blood pressure is measured several times and averaged in clinical practice (provided the errors of the two measurements are independent).
- The difference of two independent normal variables is $X - Y \sim \mathcal{N}(\mu_X - \mu_Y, \sigma_X^2 + \sigma_Y^2)$, the starting point of the comparison of two means ([7.7.7](/7.7.7)).

## 4.5. The Normal Approximation

Before computers were widespread, probabilities of the binomial and Poisson distributions were computed from tables or by the normal approximation. Today exact computation is no problem, but the normal approximation remains important: it explains why many test statistics are approximately normally distributed and gives formulas convenient for hand calculation and sample size estimation.

### 4.5.1. The Normal Approximation to the Binomial

By the **de Moivre–Laplace theorem** ([3.1.13](/3.1.13)), when $n$ is sufficiently large, $\mathrm{Bin}(n, p) \approx \mathcal{N}(np, np(1-p))$. The usual condition is $np(1-p) \ge 5$ (some textbooks write $np \ge 10$ and $n(1-p) \ge 10$); the further $p$ is from 0.5, the larger the $n$ required.

The binomial distribution is discrete, and the bar for $k$ occupies $[k - 0.5, k + 0.5]$ on the horizontal axis; when approximating by a continuous normal curve, the areas should be computed with the endpoints of this interval.

**Definition 4.5.1 (Continuity Correction)** When a continuous distribution is used to approximate an integer-valued random variable, approximating $\mathbb{P}(a \le X \le b)$ by the probability of the continuous distribution on $[a - 0.5, b + 0.5]$ is called the **continuity correction**:

$$
\mathbb{P}(a \le X \le b) \approx \Phi\!\left(\frac{b + 0.5 - np}{\sqrt{np(1-p)}}\right) - \Phi\!\left(\frac{a - 0.5 - np}{\sqrt{np(1-p)}}\right).
$$

**Example 4.5.1 (Differential white cell count)** The number of neutrophils among 100 white cells of a normal person is $X \sim \mathrm{Bin}(100, 0.6)$, with $np(1-p) = 24 \ge 5$. Clinically 50–75 is regarded as the normal range. Exact computation gives $\mathbb{P}(50 \le X \le 75) = 0.9827$; using $\mathcal{N}(60, 24)$ with the continuity correction,

$$
\Phi\!\left(\frac{75.5 - 60}{4.899}\right) - \Phi\!\left(\frac{49.5 - 60}{4.899}\right) = \Phi(3.16) - \Phi(-2.14) = 0.9832,
$$
almost the same; without the correction (using 50 and 75) we get 0.9783, an error ten times larger. Thus for a person with a normal proportion of neutrophils, the probability that the differential count falls outside the "normal range" is about 1.7%: a single abnormal count is not sufficient to show disease, since the count itself has sampling error.

### 4.5.2. The Normal Approximation to the Poisson

For $\mu \ge 10$, $\mathrm{Poi}(\mu) \approx \mathcal{N}(\mu, \mu)$, again with the continuity correction. But the approximation is poor in the tails: in Example 4.3.2 the exact value of $\mathbb{P}(X \ge 20 \mid \mu = 10)$ is 0.0035, while the normal approximation $\mathbb{P}(Y \ge 19.5) = 1 - \Phi(3.00) = 0.0013$ is only a third of the exact value, because the Poisson distribution is right-skewed and its right tail is thicker than the normal. Small probabilities are exactly what matters most in tests, so for count data exact methods should be used for tests and intervals where possible (Section 5.7 of [7.7.5](/7.7.5), Section 6.7 of [7.7.6](/7.7.6)).

## 4.6. Other Common Distributions

### 4.6.1. The Log-Normal Distribution

Many biological quantities arise multiplicatively: the multiplication factor of cell proliferation in each generation, the stepwise metabolism of a drug in the body, serial dilution of antibodies. A product becomes a sum on taking logarithms, so the logarithm of such a quantity is approximately normal.

**Definition 4.6.1 (Log-Normal Distribution)** If $\ln X \sim \mathcal{N}(\mu, \sigma^2)$, the positive random variable $X$ follows the **log-normal distribution**. Its median is $\mathrm{e}^\mu$ (the geometric mean) and its expectation is $\mathrm{e}^{\mu + \sigma^2/2}$, which is larger than the median; the larger $\sigma$, the more right-skewed the distribution.

The log-normal distribution describes blood concentrations of drugs and hormones, antibody titers, bacterial and viral loads, gene expression levels and the incubation periods of infectious diseases. For such data one takes logarithms first and then uses methods based on the normal distribution; transformed back to the original scale, the results are geometric means and fold changes ("the geometric mean of the treatment group is 1.8 times that of the control"), which is the statistical basis of the **geometric mean** in [7.7.2](/7.7.2). The skewness of the FEV data is 0.66 and after the natural logarithm it is −0.21, close to symmetric; the mean of log FEV transformed back to the original scale gives a geometric mean of 2.50 L, slightly smaller than the arithmetic mean of 2.64 L.

**Example 4.6.1 (Incubation period)** As early as 1950 Sartwell found that the incubation periods of many infectious diseases are approximately log-normally distributed. Lauer et al. (2020) estimated from 181 confirmed COVID-19 cases that the incubation period follows a log-normal distribution with a mean of 1.621 and a standard deviation of 0.418 on the log scale. From this, the median incubation period is $\mathrm{e}^{1.621} = 5.1$ days and the mean is $\mathrm{e}^{1.621 + 0.418^2/2} = 5.5$ days; 97.5% of infected people develop symptoms within $\mathrm{e}^{1.621 + 1.96 \times 0.418} = 11.5$ days, and only 0.7% after more than 14 days. This was the basis of the 14-day quarantine period at the time: using the upper tail of the distribution to set the quarantine period is much more reliable than using the mean or median.

### 4.6.2. The Exponential and Weibull Distributions

Survival time (from enrollment to death or relapse) is positive and right-skewed, and is often subject to **censoring** ([7.7.1](/7.7.1)). The simplest model is the exponential distribution: with a constant hazard $\lambda$, the survival function is $S(t) = \mathbb{P}(T > t) = \mathrm{e}^{-\lambda t}$, the mean is $1/\lambda$ and the median is $\ln 2/\lambda$.

The exponential distribution has a property that is especially convenient for censored data: the maximum likelihood estimate of $\lambda$ is "number of events ÷ total follow-up time", the incidence rate of [7.7.3](/7.7.3). The 137 lung cancer patients of the veteran trial were followed for a total of 16,663 days, with 128 deaths (9 censored), giving $\hat\lambda = 128/16\,663 = 0.00768$ per day and an estimated median survival time of $\ln 2/\hat\lambda = 90$ days.

The **Weibull distribution** generalizes the exponential, with survival function $S(t) = \exp[-(t/\eta)^k]$: for shape parameter $k = 1$ it is the exponential distribution; for $k > 1$ the hazard increases with time (aging, tumor progression) and for $k < 1$ it decreases (the risk is highest soon after surgery). Fitting the veteran data by maximum likelihood (taking censoring into account) gives $\hat k = 0.85$, a hazard that declines slightly with time: the sickest patients die first, and those who survive have on average a lower risk. The Kaplan–Meier estimate, which depends on no distributional assumption, gives a median survival time of 80 days, the Weibull model 78 days and the exponential model 90 days (panel B below). The survival function, the **hazard function** and these methods of estimation are the subject of [7.7.16](/7.7.16).

![Two right-skewed time distributions. A: the log-normal distribution of the COVID-19 incubation period estimated by Lauer et al. (2020) (mean 1.621 and standard deviation 0.418 on the log scale): median 5.1 days, mean 5.5 days, 97.5% of cases develop symptoms within 11.5 days, and only 0.7% after 14 days. B: survival times in the Veterans Administration lung cancer trial (137 patients, 128 deaths; Kalbfleisch and Prentice; R package survival): the Kaplan–Meier estimate (step line) compared with the exponential model (constant hazard, rate = deaths / total follow-up time) and the Weibull model (fitted by maximum likelihood); a Weibull shape parameter below 1 means that the hazard declines with time](./plots/skewed.py)

### 4.6.3. The Negative Binomial Distribution: Overdispersed Counts

The plate counts of Section 4.3.2 show that biological counts are often more dispersed than the Poisson distribution: even among samples given the same treatment, the true rates themselves differ. If the Poisson mean $\mu_i$ of each sample comes from a gamma distribution, the mixture distribution of the counts is the **negative binomial distribution**, with variance

$$
\operatorname{Var}(X) = \mu + \frac{\mu^2}{k},
$$
the smaller $k$ the more dispersed, and as $k \to \infty$ it returns to the Poisson distribution. The simulated plates of panel C above use $\mu = 10$ and $k = 5$, with variance 30. The negative binomial distribution describes the aggregated distribution of individuals in ecology (parasites among hosts, insects among plants), "superspreading" in epidemiology (a few infected people cause most transmission), and in RNA-seq the differences in gene counts between biological replicates under the same condition ([7.7.20](/7.7.20)). [3.1.4](/3.1.4) defines the negative binomial distribution as the number of failures before the $r$th success, $\mathrm{NB}(r, p)$; taking $r = k$ and $p = k/(k + \mu)$ gives the "mean–dispersion" parametrization used here, in which $k$ need not be an integer.

## 4.7. Sampling Distributions and the Central Limit Theorem

### 4.7.1. The Sampling Distribution of a Statistic

The distributions of the preceding sections describe individual observations. Statistical inference is concerned with another kind of distribution: draw a sample of size $n$ from a population and compute a statistic (such as the sample mean $\bar X$); with a different sample the statistic is different. The distribution of a statistic over all possible samples is its **sampling distribution**. It answers the question left open by [7.7.1](/7.7.1): how far a statistic can be from the parameter.

**Theorem 4.7.1 (Sampling Distribution of the Sample Mean)** Let $X_1, \dots, X_n$ be a **simple random sample** from a population with mean $\mu$ and variance $\sigma^2$. Then

$$
\mathbb{E}[\bar X] = \mu, \qquad \operatorname{Var}(\bar X) = \frac{\sigma^2}{n}, \qquad \operatorname{SD}(\bar X) = \frac{\sigma}{\sqrt n}.
$$
If the population is normal, $\bar X \sim \mathcal{N}(\mu, \sigma^2/n)$ holds exactly.

**Proof** By Formula 4.1.2, $\mathbb{E}[\bar X] = \frac1n\sum \mathbb{E}[X_i] = \mu$; by independence, $\operatorname{Var}(\bar X) = \frac{1}{n^2}\sum \operatorname{Var}(X_i) = \sigma^2/n$. The normal case follows from Theorem 4.4.1. $\square$

The standard deviation of $\bar X$, $\sigma/\sqrt n$, is the **standard error** of the mean (replacing $\sigma$ by the sample standard deviation $s$ gives its estimate $s/\sqrt n$). The standard deviation describes variation between individuals and does not change with the sample size; the standard error describes the uncertainty of the sample mean and decreases with $\sqrt n$ (Section 2.2.5 of [7.7.2](/7.7.2)). Precision proportional to $\sqrt n$ means diminishing returns: to halve the standard error, the sample size must be increased to 4 times.

### 4.7.2. The Central Limit Theorem

Theorem 4.7.1 gives only the expectation and variance of $\bar X$. When the population is not normal, the shape of the distribution of $\bar X$ is given by the following theorem, the most important result in statistics.

**Theorem 4.7.2 (Central Limit Theorem)** Let $X_1, \dots, X_n$ be independent and identically distributed with expectation $\mu$ and variance $0 < \sigma^2 < \infty$. Then as $n \to \infty$

$$
\frac{\bar X - \mu}{\sigma/\sqrt n} \xrightarrow{d} \mathcal{N}(0, 1),
$$
that is, for sufficiently large $n$, whatever the distribution of the population, $\bar X$ is approximately $\mathcal{N}(\mu, \sigma^2/n)$.

(For the rigorous statement and proof see [3.1.13](/3.1.13).) The figure below demonstrates this by simulation: the population is a right-skewed distribution of length of stay (a gamma distribution with mean 6 days and skewness 1.63), from which samples of size 5, 10 and 30 are drawn repeatedly; the histograms of the sample means come closer and closer to the normal curve, and the skewness decreases at the rate $1/\sqrt n$.

![Simulation of the central limit theorem. Left: a right-skewed population, a gamma distribution with shape 1.5 and mean 6 days, as a model of length of stay. The others: histograms of 10,000 sample means for sample sizes n = 5, 10 and 30; the curves are the normal densities N(μ, σ²/n) given by the central limit theorem; the skewness of the mean, 2/√(1.5n), decreases with 1/√n. Simulated data](./plots/clt.py)

How large "sufficiently large $n$" is depends on how far the population departs from normality: for a symmetric population $n \ge 15$ is usually enough; for a moderately skewed one (as above) $n \ge 30$; for a highly skewed one or one with extreme outliers (hospital costs, some counts) several hundred may be needed. Three practical implications of the central limit theorem:

- It underlies most of the methods in this course: with a fairly large sample, the $t$-test, the z-test for proportions and tests of regression coefficients are insensitive to non-normality of the population (when Section 2.6.5 of [7.7.2](/7.7.2) says "whether the departure is large enough to affect the conclusions", this is what is meant).
- It requires independent and identically distributed variables (or weaker conditions) but not normality; it concerns only the mean and not the individuals: it cannot be used to claim that "with a large sample the data become normal", since the larger the sample, the closer the histogram comes to the shape of the population itself.
- It explains why indices influenced by the superposition of many small independent factors are approximately normal (Section 4.4.1).

**Example 4.7.1** If the standard deviation of newborn birth weight is 729 g and 10 newborns are drawn at random, the standard error of the mean is $729/\sqrt{10} = 231$ g, and the probability that the sample mean differs from the population mean by at most 300 g is $2\Phi(300/231) - 1 = 0.81$. With 40 newborns the standard error is 115 g and this probability rises to 0.99.

### 4.7.3. The Sampling Distribution of a Proportion

The sample proportion $\hat p = X/n$ is the mean of $n$ 0/1 variables and therefore also obeys the central limit theorem: $\mathbb{E}[\hat p] = p$, the standard error is $\sqrt{p(1-p)/n}$, and when $np(1-p) \ge 5$, $\hat p$ is approximately $\mathcal{N}(p, p(1-p)/n)$.

**Example 4.7.2** Suppose the smoking rate among adults in a region is 20% and 100 people are surveyed at random; the standard error of the sample smoking rate $\hat p$ is $\sqrt{0.2 \times 0.8/100} = 0.04$. The probability that the sample smoking rate reaches 25% or more is, exactly, $\mathbb{P}(X \ge 25) = 0.131$; the normal approximation with the continuity correction is $1 - \Phi\!\left(\frac{24.5 - 20}{4}\right) = 0.130$, and without the correction 0.106. Even if the true smoking rate is 20%, a survey of 100 people giving 25% is not remarkable: it happens about once in 8 surveys. To reduce the standard error to 1 percentage point, 1600 people are needed (sample size calculation in [7.7.5](/7.7.5)).

## 4.8. Distributions Derived from the Normal

The sampling distributions of the sample variance of a normal population, of the standardized sample mean and of the ratio of two sample variances are three distributions derived from the normal. Their definitions and proofs are in [3.2.2](/3.2.2); here we give their use.

| Distribution | Construction | Main uses | Chapters in this course |
|---|---|---|---|
| **Chi-square distribution** $\chi^2_\nu$ | Sum of squares of $\nu$ independent standard normal variables | Intervals and tests for a normal variance, $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$; contingency tables and goodness-of-fit tests | [7.7.5](/7.7.5), [7.7.6](/7.7.6), [7.7.9](/7.7.9) |
| **t distribution** $t_\nu$ | $Z/\sqrt{V/\nu}$, with $Z \sim \mathcal{N}(0,1)$ and $V \sim \chi^2_\nu$ independent | Intervals and tests for a mean when $\sigma$ is unknown, $(\bar X - \mu)/(S/\sqrt n) \sim t_{n-1}$; regression coefficients | [7.7.5](/7.7.5)–[7.7.7](/7.7.7), [7.7.10](/7.7.10) |
| **F-distribution** $F_{m,n}$ | $(V_1/m)/(V_2/n)$ for two independent chi-square variables | Ratio of two variances; analysis of variance; overall test in regression | [7.7.7](/7.7.7), [7.7.12](/7.7.12) |

![Distributions derived from the normal. A: chi-square distributions with 1, 4 and 9 degrees of freedom (the expectation equals the degrees of freedom and the variance is twice the degrees of freedom); right-skewed, becoming symmetric as the degrees of freedom increase. B: t distributions with 1, 4 and 30 degrees of freedom and the standard normal distribution: the tails are thicker when the degrees of freedom are small; the dashed and dotted lines are the upper 2.5% quantiles 2.262 of t₉ and 1.960 of the standard normal, respectively. C: F distributions with (2, 57), (4, 30) and (9, 9) degrees of freedom](./plots/derived.py)

Some intuition:

- The chi-square distribution takes positive values and is right-skewed, with expectation equal to the degrees of freedom $\nu$ and variance $2\nu$. The upper 2.5% and lower 2.5% quantiles are asymmetric: for $\nu = 9$ they are 19.02 and 2.70, which is why the confidence interval for a variance is not "point estimate ± margin of error" (Section 5.5 of [7.7.5](/7.7.5)).
- The t distribution is symmetric and bell-shaped, with thicker tails than the standard normal, reflecting the extra uncertainty of estimating $\sigma$ by $S$. As the degrees of freedom increase it approaches the standard normal: the upper 2.5% quantile $t_{\nu, 0.025}$ is 2.776, 2.262, 2.045 and 1.984 for $\nu = 4, 9, 29, 99$ and 1.960 as $\nu \to \infty$. In small samples, using 1.96 in place of a $t$ quantile makes the interval too narrow.
- The F distribution has two degrees of freedom (numerator and denominator), takes positive values and is right-skewed; $F_{1,\nu} = t_\nu^2$.

The derivation of all three distributions depends on normality of the population. The $t$ methods rely on the central limit theorem and are quite robust to non-normality; the chi-square method for variances and the F test, however, are very sensitive to non-normality, and a large sample does not help (Section 7.4 of [7.7.7](/7.7.7)).

## 4.9. Computing with Python

Every distribution in `scipy.stats` has the same set of methods: `pmf`/`pdf` (probability or density), `cdf` (distribution function), `sf` ($1 - F$, the right-tail probability, more accurate than `1 - cdf`), `ppf`/`isf` (quantiles) and `rvs` (random numbers).

```python
import numpy as np
from scipy import stats

# binomial: Examples 4.2.2 and 4.2.3
print(stats.binom.sf(2, 20, 0.05))          # P(X >= 3) = 0.075
print(stats.binom.sf(29, 74, 29 / 115))     # P(X >= 30) = 0.0027

# normal approximation with continuity correction: Example 4.5.1
n, p = 100, 0.6
exact = stats.binom.cdf(75, n, p) - stats.binom.cdf(49, n, p)
mu, sd = n * p, np.sqrt(n * p * (1 - p))
approx = stats.norm.cdf(75.5, mu, sd) - stats.norm.cdf(49.5, mu, sd)
print(exact, approx)                        # 0.9827, 0.9832

# Poisson: Examples 4.3.1 and 4.3.2
print(stats.poisson.cdf(20, 24.7), stats.poisson.sf(19, 10))   # 0.20, 0.0035

# normal: Example 4.4.1
print(stats.norm.cdf(2500, 2945, 729))      # 0.271

# log-normal incubation period: Example 4.6.1 (scipy: s = sigma, scale = exp(mu))
inc = stats.lognorm(0.418, scale=np.exp(1.621))
print(inc.median(), inc.mean(), inc.ppf(0.975), inc.sf(14))   # 5.1, 5.5, 11.5, 0.0074

# upper quantiles used throughout the course
print(stats.norm.isf(0.025), stats.t.isf(0.025, 9), stats.chi2.isf(0.025, 9), stats.chi2.ppf(0.025, 9))

# the central limit theorem by simulation
rng = np.random.default_rng(1)
means = rng.gamma(1.5, 4.0, size=(10000, 30)).mean(axis=1)
print(means.mean(), means.std(), np.sqrt(1.5) * 4.0 / np.sqrt(30))   # about 6, 0.89, 0.89
```

## Summary

- The distribution of a random variable is determined by the mechanism generating the data (Definition 4.1.1); among the linear operations on expectation and variance (Formula 4.1.2), the variance of the difference of independent variables is the sum of the variances.
- Common distributions and their conditions:

  | Distribution | Mechanism | Expectation; variance | Biomedical examples |
  |---|---|---|---|
  | $\mathrm{Bin}(n, p)$ | $n$ independent yes-or-no trials with the same $p$ (Definition 4.2.1) | $np$; $np(1-p)$ | Affected children in a family, number of low birth weight infants (Examples 4.2.2, 4.2.3) |
  | $\mathrm{Poi}(\mu)$ | Counts of rare, independent, uniformly occurring events (Definition 4.3.1) | $\mu$; $\mu$ | Cases in person-time, colonies (Examples 4.3.1, 4.3.2) |
  | $\mathcal{N}(\mu, \sigma^2)$ | Sum of many small independent factors (Definition 4.4.1) | $\mu$; $\sigma^2$ | Birth weight, height (Example 4.4.1) |
  | Log-normal | Product of factors (Definition 4.6.1) | Median $\mathrm{e}^\mu$ | Concentrations, titers, incubation periods (Example 4.6.1) |
  | Exponential, Weibull | Waiting time; constant or monotone hazard | $1/\lambda$ (exponential) | Survival time (veteran) |
  | Negative binomial | The Poisson rate varies between samples | $\mu$; $\mu + \mu^2/k$ | Overdispersed counts, RNA-seq |

- The conditions of the binomial distribution most often violated are independence and equal $p$, with the consequences of overdispersion and underestimated standard errors.
- Normal approximation: $np(1-p) \ge 5$ or $\mu \ge 10$, with the continuity correction (Definition 4.5.1, Example 4.5.1); compute tail probabilities exactly where possible. The normal model often underestimates tail proportions (Example 4.4.1).
- The expectation of the sample mean is $\mu$ and its standard error is $\sigma/\sqrt n$ (Theorem 4.7.1); the central limit theorem (Theorem 4.7.2) makes $\bar X$ and $\hat p$ approximately normal in large samples, whatever the distribution of the population. The standard deviation describes individuals and the standard error describes the mean.
- The $\chi^2$, $t$ and $F$ distributions derived from the normal are used for variances, for means when $\sigma$ is unknown, and for ratios of variances, respectively (Section 4.8); $z_{0.025} = 1.960$ and $t_{9, 0.025} = 2.262$.

## Questions

1. In Example 4.1.1, if the prevalence is only 2% and the group size is $m = 10$, how many tests per blood sample are needed on average? How does this compare with a prevalence of 10%? Why is pooled testing not worthwhile when prevalence is high?

   **Answer** The expected number of tests per group is $\mathbb{E}[X] = 0.98^{10} + 11(1 - 0.98^{10}) = 0.817 + 11 \times 0.183 = 2.83$, so $2.83/10 = 0.283$ tests per sample, a saving of about 72%; at a prevalence of 10% it is $7.51/10 = 0.751$ per sample, a saving of only 25%. When prevalence is high, most pooled samples are positive and almost every group must be retested individually, so one extra pooled test is used; the expected number of tests per sample $\mathbb{E}[X]/m = 1 + 1/m - (1 - \pi)^m$ is less than 1 only if $(1 - \pi)^m > 1/m$; even the most favorable $m = 3$ satisfies this only when the prevalence is $\pi < 30.7\%$, and at higher prevalence no group size does better than testing individually.

2. For an autosomal recessive disease, each child of a couple who are both carriers has probability 1/4 of being affected. They have 4 children. Find: (a) the probability that exactly 1 is affected; (b) the probability that at least 1 is affected; (c) the expectation and variance of the number of affected children.

   **Answer** $X \sim \mathrm{Bin}(4, 0.25)$ (the inheritance of the children is independent). (a) $\binom41 0.25 \times 0.75^3 = 0.422$. (b) $1 - 0.75^4 = 1 - 0.316 = 0.684$. (c) $\mathbb{E}[X] = 1$ and $\operatorname{Var}(X) = 4 \times 0.25 \times 0.75 = 0.75$. Note (b): many people think that exactly 1 affected child among 4 is inevitable, but in fact 32% of such families have no affected child, which affects the estimation of segregation ratios from pedigree data ([7.4.7](/7.4.7)).

3. A hospital admits on average 2.5 patients with acute myocardial infarction per day. Assume the daily number follows a Poisson distribution; find the probability of 0 admissions on a day and of at least 5. What is the probability that more than 25 are admitted in a week (7 days)?

   **Answer** $\mathbb{P}(X = 0) = \mathrm{e}^{-2.5} = 0.082$; $\mathbb{P}(X \ge 5) = 1 - \sum_{k=0}^4 \mathrm{e}^{-2.5}2.5^k/k! = 1 - 0.891 = 0.109$. The number in a week (a sum of independent Poisson variables) follows $\mathrm{Poi}(17.5)$, and $\mathbb{P}(Y \ge 26) = 0.034$; the normal approximation $1 - \Phi\!\left(\frac{25.5 - 17.5}{\sqrt{17.5}}\right) = 1 - \Phi(1.91) = 0.028$ is somewhat low (right tail). A "busy week" about once a month can be produced by random fluctuation and does not necessarily mean that incidence has risen.

4. Suppose the systolic blood pressure of adult men follows $\mathcal{N}(125, 15^2)$ (mmHg). (a) What proportion have systolic pressure ≥ 140? (b) What is the probability that the mean of two independent measurements of one person is ≥ 140 (assume each measurement is the true value plus an independent error, the true values in the population follow $\mathcal{N}(125, 13^2)$, and the standard deviation of the measurement error is 7.5)?

   **Answer** (a) $1 - \Phi(1) = 0.159$. (b) The variance of a single measurement is $13^2 + 7.5^2 = 225.25$ (standard deviation 15.0, consistent with (a)); the mean of two measurements is the true value plus the mean error, with variance $169 + 7.5^2/2 = 197.1$ and standard deviation 14.04. $\mathbb{P} = 1 - \Phi(15/14.04) = 1 - \Phi(1.07) = 0.143$. Taking the mean of two measurements reduces the proportion classified as "hypertensive" from 15.9% to 14.3%: some people cross the threshold only because of a single high measurement, and repeated measurement reduces misclassification, but it cannot remove the variation of true values in the population.

5. Why is the proportion of low birth weight estimated with the normal distribution (0.271) in the birthwt data lower than the actual one (0.312)? Answer from the viewpoints of the data-generating mechanism and of statistics. How would you estimate the proportion with birth weight < 1500 g (very low birth weight)?

   **Answer** Mechanistically, a considerable part of the low birth weight infants arise from pathological processes such as prematurity, placental insufficiency and preeclampsia, which form a left tail superimposed on "normal variation"; the overall distribution is a mixture, and its left tail is thicker than a single normal. Statistically, the normal model is fitted with the mean and standard deviation of all the data and reflects mainly the middle; its estimate of the tail depends on the assumption of normality, and the assumption is most likely to fail in the tail (Example 4.4.1). To estimate the proportion < 1500 g: the normal model gives 0.024 and the sample has 5/189 = 0.026. In this sample the two are close, but the sample is small (only 5 cases), and one should use the empirical proportion with an exact binomial confidence interval ([7.7.5](/7.7.5)), or larger birth registry data; the normal model should not be extrapolated.

6. A study reports that the median survival time for a cancer is 18 months and the mean is 30 months. What shape of distribution does this indicate? If survival time followed an exponential distribution, what should be the ratio of the median to the mean? Is the result of this study consistent with an exponential distribution?

   **Answer** The mean exceeds the median, so the distribution is right-skewed: a few long-term survivors pull up the mean. For the exponential distribution the ratio of the median $\ln 2/\lambda$ to the mean $1/\lambda$ is $\ln 2 = 0.693$, so a mean of 30 months corresponds to a median of 20.8 months; the actual value is 18 months, a ratio of 0.6, more skewed than the exponential, suggesting that the hazard declines with time (a Weibull shape parameter < 1, as in the veteran data) or that there is a subgroup with a very good prognosis (some patients are cured). Moreover, a mean cannot simply be computed for censored survival data ([7.7.16](/7.7.16)), and one needs to see how the reported "mean" was estimated.

7. The plate colony counts in a laboratory for 6 plates at the same dilution are 38, 52, 29, 61, 45 and 33. Can a Poisson distribution describe these counts? If not, what does this mean for the precision of the estimated concentration of the stock?

   **Answer** The mean is $\bar x = 43.0$ and the sample variance is $s^2 = 146.0$, a variance-to-mean ratio of 3.4, far more than the 1 of the Poisson. The dispersion test $\sum(x_i - \bar x)^2/\bar x = 5s^2/\bar x = 17.0$ is approximately $\chi^2_5$ under the Poisson assumption, giving $p = 0.0045$: the counts are overdispersed, and there are also errors between plates from inoculation, pipetting and so on. Computed as Poisson, the standard error of the mean is $\sqrt{43/6} = 2.68$; computed from the actual variation it is $s/\sqrt6 = 4.93$, almost twice as large. A precision given by "the square root of the count" alone is too optimistic; one should use the actual variation between replicate plates and, when necessary, the negative binomial model (Section 4.6.3).

8. In a phase I trial of a new drug, the investigators plan to stop dose escalation if 2 or more of 6 participants have dose-limiting toxicity. If the true toxicity rate at the dose is 10%, 30% or 50%, what is the probability of stopping escalation in each case? What is wrong with this rule?

   **Answer** $X \sim \mathrm{Bin}(6, p)$ and $\mathbb{P}(X \ge 2) = 1 - (1-p)^6 - 6p(1-p)^5$. For $p = 0.1$: $1 - 0.531 - 0.354 = 0.114$; for $p = 0.3$: $1 - 0.118 - 0.303 = 0.580$; for $p = 0.5$: $1 - 0.016 - 0.094 = 0.891$. Even if the true toxicity rate is as high as 30%, there is a 42% probability of continuing escalation; at a toxicity rate of 10% there is an 11% probability of wrongly judging the dose too toxic. Six participants provide limited information, and the "operating characteristics" of a rule must be computed in this way in advance rather than set by intuition (design of phase I trials in [7.7.18](/7.7.18)).

9. The distribution of an index in the population is right-skewed (population mean 50, standard deviation 40). An investigator says: "I sampled 400 people, the sample is large enough, and by the central limit theorem these 400 values are approximately normally distributed, so I can use mean ± 1.96 standard deviations as the reference interval." What is wrong? What should be done?

   **Answer** The central limit theorem says that the distribution of the sample mean is approximately normal, not that of the individual observations; the histogram of the 400 values will come closer and closer to the right-skewed shape of the population itself. Mean ± 1.96 standard deviations gives $50 \pm 78$, whose lower limit is negative, clearly unreasonable, and the upper limit is also inaccurate. The reference interval should use empirical percentiles (the 2.5th and 97.5th percentiles, [7.7.2](/7.7.2)), or, if the data are approximately normal after a transformation (such as the logarithm), be computed under normality and transformed back to the original scale. The central limit theorem can be used to estimate the uncertainty of the "mean": the standard error of $\bar x$ is $40/\sqrt{400} = 2$.

10. (Design question) You want to estimate the myopia rate among schoolchildren in a city, expected to be around 50%, and want the standard error of the sample proportion to be at most 1.5 percentage points. How many students are needed? If cluster sampling by school is used and the myopia status of students in the same school is correlated, how does the required number change?

    **Answer** From $\sqrt{p(1-p)/n} \le 0.015$ with $p = 0.5$, $n \ge 0.25/0.015^2 = 1111$. With cluster sampling, the outcomes of students in the same school are positively correlated, the variance of the proportion exceeds the binomial variance and the effective sample size is reduced: the design effect is $\mathrm{DEFF} = 1 + (m - 1)\rho$, where $m$ is the number of students sampled per school and $\rho$ the intraclass correlation within schools. For example, with 50 students per school and $\rho = 0.05$, $\mathrm{DEFF} = 3.45$ and about 3830 students are needed. This is the quantitative consequence of the failure of independence in Section 4.2.3 (cluster sampling in [7.7.5](/7.7.5), design effect in [7.7.17](/7.7.17)).
