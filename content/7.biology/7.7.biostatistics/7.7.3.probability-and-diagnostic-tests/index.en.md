---
title: Probability and Diagnostic Tests
description: The basic rules of probability and Bayes' formula; measures of disease frequency (prevalence, cumulative incidence, person-time and incidence rate); sensitivity, specificity, predictive values and diagnostic likelihood ratios of screening and diagnostic tests and their dependence on prevalence; ROC curves, AUC and the Youden index; Bayesian inference with several diagnoses. Illustrated with low-dose CT lung cancer screening and COVID-19 antigen tests.
source_hash: b049381df0a2
---

Probability is the language of uncertainty. In medicine its most direct use is diagnosis: for a person with a positive test result, how likely is it that the disease is really present? The answer is often surprisingly low, and it depends on how common the disease is in the population tested. This chapter first reviews the rules of probability briefly (addition, multiplication, conditional probability, total probability and Bayes' formula; the mathematical development is in [3.1.2](/3.1.2)), then defines the quantities that describe how much disease there is in a population (prevalence, cumulative incidence and incidence rate), and then uses conditional probability to characterize screening and diagnostic tests: sensitivity, specificity, predictive values, diagnostic likelihood ratios and, for continuous markers, the ROC curve. The main example of the chapter is low-dose CT (LDCT) lung cancer screening, which continues the smoking and lung cancer thread of [7.7.1](/7.7.1); COVID-19 rapid antigen testing serves as a contrast, showing how the same formulas behave for a highly specific test and at different levels of prevalence. The sensitivity and specificity obtained here are proportions estimated from samples; their confidence intervals are in [7.7.5](/7.7.5), the comparison of two tests in [7.7.9](/7.7.9), and prediction models based on logistic regression in [7.7.14](/7.7.14) and [7.7.21](/7.7.21).

## 3.1. The Basic Rules of Probability

### 3.1.1. The Meaning of Probability

The probability of an event is a number between 0 and 1 that measures how likely it is to occur. The frequency interpretation regards probability as the limit of the relative frequency of the event in a large number of repeated trials (the **law of large numbers**): saying "the probability of a complication of some operation is 3%" means that about 3% of a large number of similar patients develop the complication. The subjective (Bayesian) interpretation regards probability as a degree of belief in a proposition under incomplete information: a physician's judgment that this patient has "a 30% chance of pneumonia" cannot be tested by repeating the same patient, but can be updated by Bayes' formula as new information arrives (Section 3.5). Both interpretations obey the same mathematical rules, Kolmogorov's **axioms of probability**: the probability of any event is nonnegative, the probability of the certain event is 1, and the probability of a union of mutually exclusive events is the sum of their probabilities.

Write $\bar A$ for the complement of $A$, $A \cap B$ for the occurrence of both $A$ and $B$, and $A \cup B$ for the occurrence of at least one of them. From the axioms we get at once $\mathbb{P}(\bar A) = 1 - \mathbb{P}(A)$.

### 3.1.2. The Addition and Multiplication Rules

**Formula 3.1.1 (Addition Rule)** For any two events,

$$
\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B).
$$
For mutually exclusive events $\mathbb{P}(A \cap B) = 0$, and the right side reduces to the sum of the two probabilities.

**Formula 3.1.2 (Multiplication Rule and Independence)** For $\mathbb{P}(B) > 0$, the **conditional probability** of $A$ given that $B$ occurs is $\mathbb{P}(A \mid B) = \mathbb{P}(A \cap B)/\mathbb{P}(B)$, and hence

$$
\mathbb{P}(A \cap B) = \mathbb{P}(B)\,\mathbb{P}(A \mid B) = \mathbb{P}(A)\,\mathbb{P}(B \mid A).
$$
If $\mathbb{P}(A \cap B) = \mathbb{P}(A)\,\mathbb{P}(B)$, or equivalently $\mathbb{P}(A \mid B) = \mathbb{P}(A)$, then $A$ and $B$ are said to be independent: knowing that $B$ occurs does not change the assessment of $A$.

**Example 3.1.1 (Readings by two physicians)** Two physicians A and B at a sexually transmitted disease clinic each review all suspected cases of syphilis. A calls 10% positive and B calls 17% positive, and both call 8% positive. If either calls a case positive it is sent for laboratory confirmation. The proportion sent is

$$
\mathbb{P}(A^+ \cup B^+) = 0.10 + 0.17 - 0.08 = 0.19.
$$
Are the two physicians' judgments independent? If they were, the proportion called positive by both would be $0.10 \times 0.17 = 0.017$, but the actual proportion is $0.08$, nearly 5 times higher. This is to be expected: the two see the same patients, and true cases are more likely to be called positive by both. How to measure the agreement between readings (Cohen's $\kappa$) is treated in [7.7.9](/7.7.9).

### 3.1.3. The Law of Total Probability

If $B_1, \dots, B_k$ are mutually exclusive and exhaustive (exactly one occurs), then by the **law of total probability**

$$
\mathbb{P}(A) = \sum_{j=1}^k \mathbb{P}(A \mid B_j)\,\mathbb{P}(B_j),
$$
the total probability is the average of the conditional probabilities over the strata, weighted by the proportions of the strata.

**Example 3.1.2 (Low birth weight)** In the birthwt data there are 74 smoking mothers, of whom 30 had low birth weight infants, and 115 nonsmoking mothers, of whom 29 did. $\mathbb{P}(\text{low} \mid \text{smoker}) = 30/74 = 0.405$, $\mathbb{P}(\text{low} \mid \text{nonsmoker}) = 29/115 = 0.252$, and the proportion of smokers is $74/189 = 0.392$. By the law of total probability,

$$
\mathbb{P}(\text{low}) = 0.405 \times 0.392 + 0.252 \times 0.608 = 0.312 = 59/189.
$$
The law of total probability shows that the overall rate in a population depends on the rates in the strata and on the composition of the population: if the smoking rate among pregnant women fell to 10% with the two conditional probabilities unchanged, the proportion of low birth weight would fall to $0.405 \times 0.1 + 0.252 \times 0.9 = 0.267$. Such "what if" calculations implicitly assume that smoking is a cause; whether this holds is a question for [7.7.15](/7.7.15).

### 3.1.4. Bayes' Formula

Conditional probability is asymmetric: $\mathbb{P}(A \mid B)$ and $\mathbb{P}(B \mid A)$ usually differ greatly. **Bayes' theorem** turns one direction into the other:

$$
\mathbb{P}(B_i \mid A) = \frac{\mathbb{P}(A \mid B_i)\,\mathbb{P}(B_i)}{\sum_{j=1}^k \mathbb{P}(A \mid B_j)\,\mathbb{P}(B_j)}.
$$
$\mathbb{P}(B_i)$ is the probability before $A$ is observed (the prior probability), and $\mathbb{P}(B_i \mid A)$ is the probability afterwards (the posterior probability).

**Example 3.1.3 (The case-control study of Doll and Hill)** In 1950 Doll and Hill surveyed 649 male lung cancer patients and 649 male controls of similar age in London hospitals, of whom 647 and 622, respectively, were smokers. From this we can estimate $\mathbb{P}(\text{smoker} \mid \text{lung cancer}) = 647/649 = 0.997$ and $\mathbb{P}(\text{smoker} \mid \text{control}) = 622/649 = 0.958$. But what we really want to know is the other direction, $\mathbb{P}(\text{lung cancer} \mid \text{smoker})$. A case-control study samples by disease status, with cases and controls each making up half, far above the proportion of lung cancer in the population, so $647/(647 + 622)$ cannot be used directly to estimate the disease risk of smokers; to use Bayes' formula we would also need the prevalence of lung cancer in the population. The quantity such a study can estimate directly is the **odds ratio**, $\frac{647 \times 27}{2 \times 622} = 14.0$, which for a rare disease approximates the ratio of the risk of smokers to that of nonsmokers ([7.7.13](/7.7.13)).

### 3.1.5. Ratios of Risks

Ratios of conditional probabilities are basic quantities of epidemiology. Let $D$ denote disease and $E$ exposure; the ratio of the risk of disease in the exposed to that in the unexposed, $\mathbb{P}(D \mid E)/\mathbb{P}(D \mid \bar E)$, is the *relative risk* (RR). If exposure and disease are independent, RR = 1; the stronger the association, the further RR is from 1.

**Example 3.1.4 (The Physicians' Health Study)** This randomized trial divided 22,071 American male physicians into two groups taking 325 mg of aspirin or placebo on alternate days. Over about 5 years, 139 of the 11,037 men in the aspirin group had a myocardial infarction, and 239 of the 11,034 in the placebo group: the cumulative incidences in the two groups were 1.26% and 2.17%, RR = $0.0126/0.0217 = 0.58$, so aspirin reduced the risk of myocardial infarction by about 42%. Because the assignment was random, this ratio can be interpreted as a causal effect. Other measures of effect (risk difference, number needed to treat) and their confidence intervals are in [7.7.9](/7.7.9) and [7.7.13](/7.7.13).

## 3.2. Measures of Disease Frequency

### 3.2.1. Prevalence and Cumulative Incidence

**Definition 3.2.1 (Prevalence and Cumulative Incidence)** The proportion of a population that has a given disease at a given moment is the **prevalence** of the disease, the number of existing cases divided by the total population at that moment. The probability that a person free of the disease at the start develops it during a specified period is the **cumulative incidence**, the number of new cases divided by the number of disease-free people at the start.

Prevalence is a "snapshot", regardless of when the patients became ill; cumulative incidence is a "video recording" and must specify the period ("5-year cumulative incidence"). Example: in the 1999–2000 NHANES survey, 1225 of 6044 adults older than 17 were taking antihypertensive drugs, so the prevalence of hypertension is $1225/6044 = 20.3\%$. In Example 3.1.4 the 5-year cumulative incidence of myocardial infarction in the placebo group is 2.17%.

### 3.2.2. Person-Time and Incidence Rate

The follow-up time of the individuals in a cohort often differs: some enter the study midway, some are lost to follow-up or die of other causes (censoring in [7.7.1](/7.7.1)). The number of people is then no longer a suitable denominator; we use the sum of the times for which each person was actually at risk.

**Definition 3.2.2 (Person-Time and Incidence Rate)** The sum of the times that each person spends disease-free and under observation during the study is the **person-time**, in units of person-years, person-months and so on. The number of new cases divided by the person-time is the **incidence rate** (also called incidence density), in units of "per person-year".

Example: 10 people each followed for 1 year and 1 person followed for 10 years are both 10 person-years. The incidence rate is a rate (Section 1.3.3 of [7.7.1](/7.7.1)); it measures the speed of disease occurrence per unit time and can exceed 1. The Chinese word for "incidence" sometimes means cumulative incidence and sometimes the incidence rate, so when reading one must check whether the denominator is people or person-time. Example: the National Lung Screening Trial (NLST) randomized 53,454 heavy smokers to annual low-dose CT or chest radiograph screening with a median follow-up of 6.5 years; the incidence rate of lung cancer death was 247 per 100,000 person-years in the CT group and 309 in the radiograph group, a rate ratio of $247/309 = 0.80$, a 20% reduction in lung cancer mortality.

### 3.2.3. The Relation Among the Three

In a stable population (incidence balanced by recovery and death), the prevalence $P$, the incidence rate $I$ and the mean duration of disease $\bar D$ satisfy

**Formula 3.2.1** 

$$
\frac{P}{1 - P} = I \bar D, \qquad \text{for a rare disease} \quad P \approx I \bar D.
$$

The intuition is the "bathtub model": the water level (number of existing cases) depends on the inflow (new cases) and the time the water stays in the tub (duration of disease). If a disease has an incidence rate of 2/1000 per year and a mean duration of 5 years, its prevalence is about 1%. This shows that high prevalence does not necessarily mean many new cases: treatment prolongs the survival of patients and prevalence rises instead (as with HIV after effective treatment became widely available); an acute disease of very short duration (influenza) has many new cases and very low prevalence. Etiologic studies should compare incidence, not prevalence, otherwise the duration of disease is confounded with its cause.

For a fixed follow-up time $t$ and a constant incidence rate, the cumulative incidence is $1 - \mathrm{e}^{-It}$, approximately $It$ when $It$ is small (the survival function of the exponential distribution, [7.7.4](/7.7.4), [7.7.16](/7.7.16)).

## 3.3. Screening and Diagnostic Tests

### 3.3.1. The 2×2 Table and Four Conditional Probabilities

Cross-classify the people tested by true disease status (determined by a "gold standard" such as a pathological biopsy) and test result:

| | Diseased $D^+$ | Not diseased $D^-$ | Total |
|---|---|---|---|
| Test positive $T^+$ | $a$ (true positive) | $b$ (false positive) | $a + b$ |
| Test negative $T^-$ | $c$ (false negative) | $d$ (true negative) | $c + d$ |
| Total | $a + c$ | $b + d$ | $N$ |

**Definition 3.3.1 (Sensitivity and Specificity)** The probability that the test is positive in the diseased, $\mathbb{P}(T^+ \mid D^+)$, is the **sensitivity** (Se), and the probability that it is negative in the nondiseased, $\mathbb{P}(T^- \mid D^-)$, is the **specificity** (Sp). They are estimated from the table as $\mathrm{Se} = a/(a + c)$ and $\mathrm{Sp} = d/(b + d)$. $1 - \mathrm{Se}$ is the false negative rate and $1 - \mathrm{Sp}$ is the false positive rate.

Sensitivity and specificity are properties of the test itself (for a given spectrum of patients and a given reading criterion); they can be estimated separately in cases and controls and do not depend on how many patients there are in the population. But patients and physicians care about the probabilities in the opposite direction.

**Definition 3.3.2 (Predictive Values)** The probability that a person with a positive test truly has the disease, $\mathbb{P}(D^+ \mid T^+)$, is the **positive predictive value** (PPV), and the probability that a person with a negative test is truly free of the disease, $\mathbb{P}(D^- \mid T^-)$, is the **negative predictive value** (NPV).

Only when the people tested are a random sample from the target population (rather than recruited separately as cases and controls) can $\mathrm{PPV} = a/(a + b)$ and $\mathrm{NPV} = d/(c + d)$ be estimated directly from the table. In general, Bayes' formula combines the sensitivity, the specificity and the prevalence $\pi$ in the population tested (the pretest probability):

**Theorem 3.3.1 (Bayes' Formula for Predictive Values)** 

$$
\mathrm{PPV} = \frac{\mathrm{Se}\,\pi}{\mathrm{Se}\,\pi + (1 - \mathrm{Sp})(1 - \pi)}, \qquad \mathrm{NPV} = \frac{\mathrm{Sp}\,(1 - \pi)}{\mathrm{Sp}\,(1 - \pi) + (1 - \mathrm{Se})\,\pi}.
$$

**Proof** By Bayes' formula, $\mathbb{P}(D^+ \mid T^+) = \mathbb{P}(T^+ \mid D^+)\mathbb{P}(D^+) / \mathbb{P}(T^+)$; by the law of total probability, $\mathbb{P}(T^+) = \mathbb{P}(T^+ \mid D^+)\mathbb{P}(D^+) + \mathbb{P}(T^+ \mid D^-)\mathbb{P}(D^-) = \mathrm{Se}\,\pi + (1 - \mathrm{Sp})(1 - \pi)$. The NPV is similar. $\square$

### 3.3.2. Low-Dose CT Screening: Most People with a Positive Result Do Not Have Cancer

**Example 3.3.1** In the first screening round of the NLST, low-dose CT had a sensitivity of 93.8% and a specificity of 73.4% (a positive result was defined as finding a noncalcified nodule of ≥ 4 mm), and about 1.1% of those screened were diagnosed with lung cancer within the year. By Theorem 3.3.1,

$$
\mathrm{PPV} = \frac{0.938 \times 0.011}{0.938 \times 0.011 + 0.266 \times 0.989} = \frac{0.0103}{0.2734} = 3.8\%, \qquad \mathrm{NPV} = 99.9\%.
$$
About 27% of those screened have a positive scan, and fewer than 4% of those actually have lung cancer. Natural frequencies make this more intuitive:

![Natural frequencies for 10,000 people screened with low-dose CT, assuming a prevalence of 1.1%, a sensitivity of 93.8% and a specificity of 73.4% (the first NLST screening round). Of the 2734 positive scans only 103 come from patients with lung cancer: the positive predictive value is 103/2734 = 3.8%. Numbers are rounded](./plots/frequency-tree.py)

Many false positives do not mean that LDCT is a poor test: a sensitivity of 93.8% means that it seldom misses a cancer, and a negative result is very reliable; most positive results can be ruled out by a follow-up CT, and only a few require a needle biopsy. The NLST showed that this screening reduced lung cancer deaths by 20% in heavy smokers (Section 3.2.2). But false positives bring anxiety, additional radiation and the complications of invasive procedures, which are the costs of screening; later screening protocols (such as the Lung-RADS categories) raised the nodule size threshold for a positive result, trading a small loss of sensitivity for a much higher specificity. Biases peculiar to screening trials (lead time, overdiagnosis) are discussed in [7.7.18](/7.7.18).

### 3.3.3. Predictive Values Vary with Prevalence

![Predictive values depend on prevalence. A: positive predictive value, B: negative predictive value, with the prevalence in the population tested on the horizontal axis (logarithmic scale). The blue line is low-dose CT in the first NLST round (sensitivity 93.8%, specificity 73.4%), and the orange line is the rapid COVID-19 antigen test in symptomatic people (pooled sensitivity 73.0%, specificity 99.1%). The dot marks the prevalence of about 1.1% in the screening trial, where the predictive value of a positive CT is only 3.8%](./plots/ppv-prevalence.py)

The predictive values of the same test can differ enormously in different populations.

**Example 3.3.2 (COVID-19 antigen tests)** A Cochrane systematic review (2022) pooled a sensitivity of about 73.0% and a specificity of about 99.1% for rapid antigen tests in symptomatic people.

| Prevalence in the population tested | True positives per 10,000 | False positives | PPV | NPV |
|---|---|---|---|---|
| 1% (screening of asymptomatic people in a low-prevalence period) | 73 | 89 | 45% | 99.7% |
| 20% (febrile patients seeking care at the epidemic peak) | 1460 | 72 | 95% | 93.6% |

(The sensitivity is lower in asymptomatic people, about 55%; here the same pair of values is kept in order to isolate the effect of prevalence.) When prevalence is low, more than half of the positives are false positives, and positive results should be confirmed by a nucleic acid test; when prevalence is high, a positive result is almost conclusive, while the reliability of a negative result declines: at a prevalence of 20%, 6 of every 100 people with a negative result are in fact infected. Compared with LDCT, the antigen test has a much higher specificity, so its PPV rises much faster with prevalence (figure above).

The general rule: when prevalence is low, the PPV is determined mainly by specificity; when prevalence is high, the NPV is determined mainly by sensitivity. Population screening for a rare disease therefore requires an extremely high specificity, and a test used to "rule out" a diagnosis requires an extremely high sensitivity. Two mnemonics used in clinical practice express the same idea: a negative result of a highly sensitive test rules out the disease (SnNout), and a positive result of a highly specific test rules in the disease (SpPin).

### 3.3.4. Diagnostic Likelihood Ratios

Predictive values depend on prevalence and are inconvenient to transfer between populations; sensitivity and specificity are two numbers and inconvenient for directly updating a judgment. Diagnostic likelihood ratios combine the two into one quantity that acts directly on the pretest judgment.

**Definition 3.3.3 (Diagnostic Likelihood Ratio)** The **diagnostic likelihood ratio** of a positive result is $\mathrm{LR}^+ = \mathrm{Se}/(1 - \mathrm{Sp})$, and that of a negative result is $\mathrm{LR}^- = (1 - \mathrm{Se})/\mathrm{Sp}$; that is, the ratio of the probabilities with which a given test result occurs in the diseased and in the nondiseased.

**Formula 3.3.1 (Posttest Odds)** Converting probabilities to odds $\Omega = \pi/(1 - \pi)$, Bayes' formula becomes a multiplication:

$$
\Omega_{\text{post}} = \Omega_{\text{pre}} \times \mathrm{LR}.
$$
A result with $\mathrm{LR} > 1$ raises the probability of disease and one with $\mathrm{LR} < 1$ lowers it; it is generally held that a result with $\mathrm{LR}^+ > 10$ or $\mathrm{LR}^- < 0.1$ can change the diagnostic judgment substantially.

**Example 3.3.3** For LDCT, $\mathrm{LR}^+ = 0.938/0.266 = 3.5$ and $\mathrm{LR}^- = 0.062/0.734 = 0.084$; for the antigen test, $\mathrm{LR}^+ = 0.730/0.009 = 81$ and $\mathrm{LR}^- = 0.270/0.991 = 0.27$. For LDCT, the pretest probability of 1.1% corresponds to odds of $0.011/0.989 = 0.0111$, the odds after a positive result are $0.0111 \times 3.53 = 0.039$, and the probability is $0.039/1.039 = 3.8\%$, in agreement with Example 3.3.1. Thus a negative LDCT result is strong ($\mathrm{LR}^- < 0.1$) and a positive result serves only to "suggest further examination"; the antigen test is the opposite: a positive result is strong and a negative one is not very reliable.

The advantage of likelihood ratios is that they can be chained: if several tests are independent given the disease status, one simply multiplies by their likelihood ratios in turn. For a test with several grades or continuous values, each result interval has its own likelihood ratio (each grade of the CT score in the next section), which retains more information than the sensitivity and specificity at a single cutoff.

### 3.3.5. Combined Tests

Two tests can be combined in two ways. Suppose the two tests are independent given the disease status (conditionally independent):

- In series (positive only if both are positive): $\mathrm{Se} = \mathrm{Se}_1\,\mathrm{Se}_2$, $\mathrm{Sp} = 1 - (1 - \mathrm{Sp}_1)(1 - \mathrm{Sp}_2)$. Specificity rises and sensitivity falls; used for confirmation.
- In parallel (positive if either is positive): $\mathrm{Se} = 1 - (1 - \mathrm{Se}_1)(1 - \mathrm{Se}_2)$, $\mathrm{Sp} = \mathrm{Sp}_1\,\mathrm{Sp}_2$. Sensitivity rises and specificity falls; used for screening and ruling out.

Example: if two antigen tests taken at an interval are combined in parallel and are conditionally independent, the sensitivity rises from 73% to $1 - 0.27^2 = 92.7\%$ and the specificity falls from 99.1% to $0.991^2 = 98.2\%$. But conditional independence often fails: infected people with a low viral load are easily missed on both occasions, and the actual improvement is smaller than the formula estimates; only when the repeat test is a few days later, giving the viral load a chance to rise, does the effect approach independence.

### 3.3.6. Sensitivity and Specificity Are Not Constants

Sensitivity and specificity are often treated as intrinsic constants of a test, but they depend on the spectrum of the people tested: in patients with severe disease and typical symptoms the test is more likely to be positive; among "controls" with other similar diseases it is more likely to be falsely positive. This is why the sensitivity of the antigen test in symptomatic people (73%) is clearly higher than in asymptomatic people (55%). Accuracy estimated from severe cases and healthy volunteers is often too high (spectrum bias); when only those with a positive test undergo the gold standard examination, the estimated sensitivity is too high and the specificity too low (verification bias). A study evaluating diagnostic accuracy should be done in the population in which the test will actually be used in the future, with all participants confirmed by the gold standard (reporting guidelines in [7.7.21](/7.7.21)).

## 3.4. The ROC Curve and the AUC

### 3.4.1. Choosing a Cutoff

Many tests give continuous values (blood glucose, PSA, troponin) or ordered grades (imaging scores), which must be converted to positive or negative at some cutoff. The cutoff determines the trade-off between sensitivity and specificity: lowering the cutoff classifies more patients as positive (sensitivity rises) but also more healthy people as positive (specificity falls).

![How the cutoff of a continuous marker trades sensitivity against specificity (binormal model, computed exactly). A: the marker values of the nondiseased follow N(0, 1) and those of the diseased follow N(1.5, 1); with the cutoff at 1.0 the shaded areas are the false negatives (diseased to the left of the cutoff) and the false positives (healthy to the right of the cutoff). B: the ROC curve drawn by moving the cutoff; the dot is the cutoff of A, and the square is the cutoff 0.75 that maximizes the Youden index J = Se + Sp − 1. The area under the curve is Φ(1.5/√2) = 0.856](./plots/cutoff-tradeoff.py)

Plotting $(1 - \mathrm{Sp}, \mathrm{Se})$ for every possible cutoff as a curve gives the **ROC curve** ([3.4.10](/3.4.10) defines it in the context of classifiers). The ROC curve of a completely useless test (marker unrelated to disease) is the diagonal; a perfect test passes through the upper left corner $(0, 1)$. The closer the curve is to the upper left corner, the better the test.

### 3.4.2. The Area Under the Curve

The **area under the curve** (AUC) summarizes the whole ROC curve in one number and has a direct probabilistic interpretation.

**Theorem 3.4.1** Let $X_D$ and $X_N$ be the test values of a randomly chosen patient and a randomly chosen nonpatient, respectively; then the area under the ROC curve (points joined by the trapezoidal rule) is

$$
\mathrm{AUC} = \mathbb{P}(X_D > X_N) + \tfrac12\,\mathbb{P}(X_D = X_N).
$$

That is, the AUC is the probability that the test puts a random pair of "patient and nonpatient" in the correct order; it is 0.5 for a useless test and 1 for a perfect one. This quantity is the Mann–Whitney statistic divided by $n_D n_N$, so the AUC of two groups and the **Wilcoxon rank-sum test** are one and the same thing ([7.7.8](/7.7.8)). In the binormal model, if the two groups have equal standard deviations and their means differ by $\delta$ standard deviations, $\mathrm{AUC} = \Phi(\delta/\sqrt2)$.

**Example 3.4.1 (CT scores)** A radiologist graded CT images of 109 patients with possible neurological disease on a scale of 1–5 (1 = definitely normal, 5 = definitely abnormal), with the true status known (Hanley and McNeil 1982):

| Score | 1 | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|
| Normal | 33 | 6 | 6 | 11 | 2 | 58 |
| Abnormal | 3 | 2 | 2 | 11 | 33 | 51 |

Taking "score ≥ $k$" as positive gives the sensitivity and specificity at each cutoff:

| Positivity criterion | 1+ | 2+ | 3+ | 4+ | 5+ | 6+ |
|---|---|---|---|---|---|---|
| Sensitivity | 1.000 | 0.941 | 0.902 | 0.863 | 0.647 | 0 |
| Specificity | 0 | 0.569 | 0.672 | 0.776 | 0.966 | 1.000 |
| Youden index $J$ | 0 | 0.510 | 0.574 | 0.639 | 0.613 | 0 |

![The empirical ROC curve for one radiologist's five-grade scores of 109 CT images (58 normal, 51 abnormal; Hanley and McNeil 1982). A: distribution of scores by true status. B: each point corresponds to calling a given grade or higher positive (5+, 4+, 3+, 2+); the area under the curve by the trapezoidal rule is 0.893, the probability that a randomly chosen abnormal image receives a higher score than a normal one (ties count one half); the Youden index is largest at 4+ (0.64)](./plots/roc-ct.py)

The trapezoidal rule gives the area:

$$
\begin{aligned}
\mathrm{AUC} &= \tfrac12(0.647 + 0)(0.034) + \tfrac12(0.863 + 0.647)(0.190) + \tfrac12(0.902 + 0.863)(0.103) \\
&\quad + \tfrac12(0.941 + 0.902)(0.103) + \tfrac12(1 + 0.941)(0.569) = 0.893.
\end{aligned}
$$
Counting directly by Theorem 3.4.1 the number of the $58 \times 51 = 2958$ "normal–abnormal" pairs in which the abnormal image has the higher score (ties count one half) gives the same 0.893. The standard error given by Hanley and McNeil is about 0.032, and the 95% confidence interval of the AUC is about 0.83–0.96. The diagnostic likelihood ratios of the score grades are $\frac{3/51}{33/58} = 0.10$, $0.38$, $0.38$, $1.14$ and $18.8$: a score of 5 is almost diagnostic, a score of 1 strongly suggests normal, and grades 2–4 carry limited information.

The AUC is suited to comparing two tests for the same disease, but it treats all cutoffs alike, including regions that would never be used clinically (such as the part with a false positive rate of 80%); when two ROC curves cross, the one with the larger AUC is not necessarily better in the region that is needed. The AUC also says nothing about calibration: it looks only at ranking, not at whether the predicted probabilities are accurate ([7.7.21](/7.7.21)).

### 3.4.3. The Optimal Cutoff

**Definition 3.4.1 (Youden Index)** The **Youden index** of a cutoff is $J = \mathrm{Se} + \mathrm{Sp} - 1$, the vertical distance from the point on the ROC curve to the diagonal. The cutoff maximizing $J$ is a common choice when false positives and false negatives are equally important.

In Example 3.4.1, $J$ is largest at 4+ (0.639); in the binormal example of panel B of the figure above it is largest at the midpoint of the two means (0.547). But the Youden index implicitly assumes that one false positive and one false negative cost the same and that the prevalence is one half. In practice the choice of cutoff must take into account the consequences of missed and mistaken diagnoses and the prevalence in the population tested: missing a curable cancer is far worse than one more CT for a healthy person, so screening favors a cutoff with high sensitivity, whereas a test that precedes major surgery favors high specificity. Formally, if the ratio of the costs of a false positive to a false negative is $C$, the slope of the ROC curve at the cutoff with minimal expected cost is $C(1 - \pi)/\pi$.

## 3.5. Several Diagnoses and Bayesian Inference

### 3.5.1. The Prior Determines the Posterior

Bayes' formula applies equally to more than two disease states, and it shows clearly the role of prior information.

**Example 3.5.1 (Lung biopsy)** A 60-year-old man who has never smoked presents with chronic cough and intermittent shortness of breath, and the lung biopsy is consistent with both lung cancer and sarcoidosis (a fairly common, usually nonfatal lung disease). Let $A$ be this set of symptoms and biopsy findings, and let the three states be $B_1$ normal, $B_2$ lung cancer and $B_3$ sarcoidosis, with $\mathbb{P}(A \mid B_1) = 0.001$ and $\mathbb{P}(A \mid B_2) = \mathbb{P}(A \mid B_3) = 0.9$; among 60-year-old men who have never smoked the prior probabilities are $\mathbb{P}(B_1) = 0.99$, $\mathbb{P}(B_2) = 0.001$ and $\mathbb{P}(B_3) = 0.009$. The denominator is $0.001 \times 0.99 + 0.9 \times 0.001 + 0.9 \times 0.009 = 0.00999$, and so

$$
\mathbb{P}(B_1 \mid A) = \frac{0.00099}{0.00999} = 0.099, \quad \mathbb{P}(B_2 \mid A) = \frac{0.00090}{0.00999} = 0.090, \quad \mathbb{P}(B_3 \mid A) = \frac{0.00810}{0.00999} = 0.811.
$$
The most likely diagnosis is sarcoidosis. If the same patient had smoked two packs a day for 40 years, the prior probabilities become 0.98, 0.015 and 0.005, and the same findings give posterior probabilities of 0.052, 0.711 and 0.237: the most likely diagnosis becomes lung cancer.

![Bayesian inference with three diagnoses: the same symptoms and biopsy findings, with P(findings | normal) = 0.001 and P(findings | lung cancer) = P(findings | sarcoidosis) = 0.9. A: a man who has never smoked (priors 0.99, 0.001, 0.009). B: a heavy smoker (priors 0.98, 0.015, 0.005). The same evidence points to sarcoidosis in the former (0.81) and to lung cancer in the latter (0.71)](./plots/bayes-biopsy.py)

Lung cancer and sarcoidosis have the same likelihood (both 0.9), so the ratio of their posterior probabilities equals the ratio of their priors; the role of the evidence is to rule out "normal", and what decides between the two diseases is entirely the prior, that is, the smoking history. This is the statistical meaning of the medical history in diagnosis.

### 3.5.2. Bayesian Calculation in Genetic Counseling

Risk assessment in **genetic counseling** is a classic application of Bayes' formula (a systematic treatment is in [7.4.7](/7.4.7)). Example: a woman with a normal phenotype has a brother with cystic fibrosis (autosomal recessive), so her prior probability of being a carrier is $2/3$. Her carrier screening is negative, but the test detects only 90% of the disease-causing mutations in the population. By Bayes' formula,

$$
\mathbb{P}(\text{carrier} \mid \text{test negative}) = \frac{\frac23 \times 0.1}{\frac23 \times 0.1 + \frac13 \times 1} = \frac{1}{6} = 0.167.
$$
The negative result lowers the risk from 67% to 17%, but far from to 0; the calculation for a test that detects only some of the mutations is in [7.4.7](/7.4.7#sec-7.4.4).

### 3.5.3. From Diagnosis to Statistical Inference

In diagnosis the prior probability comes from objective data such as prevalence, and the meaning of the posterior probability is not disputed. Applying the same idea to an unknown parameter (such as the response rate of a new drug) gives Bayesian statistical inference: the prior distribution of the parameter is combined with the likelihood of the data to give the posterior distribution of the parameter ([3.2.7](/3.2.7); [7.7.5](/7.7.5) of this course has a beta–binomial example). The difficulty is that the prior of a parameter often has no objective basis and different people may give different priors; when the data are plentiful, the influence of the prior gradually disappears.

## 3.6. Computing with Python

```python
import numpy as np

def predictive_values(se, sp, prev):
    """PPV and NPV from sensitivity, specificity and prevalence (Theorem 3.3.1)."""
    ppv = se * prev / (se * prev + (1 - sp) * (1 - prev))
    npv = sp * (1 - prev) / (sp * (1 - prev) + (1 - se) * prev)
    return ppv, npv

print(predictive_values(0.938, 0.734, 0.011))     # low-dose CT: (0.038, 0.999)
for prev in [0.01, 0.20]:
    print(prev, predictive_values(0.730, 0.991, prev))   # antigen test

# likelihood ratios and post-test probability
se, sp, prev = 0.938, 0.734, 0.011
lr_pos, lr_neg = se / (1 - sp), (1 - se) / sp
post_odds = prev / (1 - prev) * lr_pos
print(lr_pos, lr_neg, post_odds / (1 + post_odds))

# empirical ROC and AUC for the CT ratings (Example 3.4.1)
normal = np.array([33, 6, 6, 11, 2])
abnormal = np.array([3, 2, 2, 11, 33])
sens = [abnormal[k:].sum() / abnormal.sum() for k in range(6)]   # criteria 1+ ... 6+
spec = [normal[:k].sum() / normal.sum() for k in range(6)]
fpr, tpr = 1 - np.array(spec), np.array(sens)
auc = np.trapezoid(tpr[::-1], fpr[::-1])
youden = tpr - fpr
print(round(auc, 3), youden.round(3))             # 0.893, maximum 0.639 at 4+

# the same AUC as a probability over all normal-abnormal pairs (Theorem 3.4.1)
pairs = sum(normal[i] * abnormal[j] * (1.0 if j > i else 0.5 if j == i else 0.0)
            for i in range(5) for j in range(5))
print(pairs / (normal.sum() * abnormal.sum()))
```

For individual-level data (one continuous test value and one true status per patient), `sklearn.metrics.roc_curve` and `roc_auc_score` give the ROC curve and the AUC.

## Summary

- Rules of probability: addition (Formula 3.1.1), multiplication and independence (Formula 3.1.2), the **law of total probability** and **Bayes' theorem**. **Conditional probability** is asymmetric: $\mathbb{P}(\text{smoker} \mid \text{lung cancer})$ is not $\mathbb{P}(\text{lung cancer} \mid \text{smoker})$; a case-control study can directly estimate only the former and the **odds ratio** (Example 3.1.3).
- Disease frequency (Definitions 3.2.1, 3.2.2):

  | Quantity | Numerator | Denominator | Dimension |
  |---|---|---|---|
  | Prevalence | Existing cases | Population at a moment | Proportion |
  | Cumulative incidence | New cases | Disease-free people at the start (period specified) | Proportion |
  | Incidence rate | New cases | Person-time | 1/time |

  In a stable population $P/(1 - P) = I\bar D$ (Formula 3.2.1); etiologic studies compare incidence rather than prevalence.
- Diagnostic tests (Definitions 3.3.1–3.3.3):

  | Quantity | Definition | Depends on prevalence? |
  |---|---|---|
  | Sensitivity, specificity | $\mathbb{P}(T^+ \mid D^+)$, $\mathbb{P}(T^- \mid D^-)$ | No (but depends on the spectrum of patients) |
  | PPV, NPV | $\mathbb{P}(D^+ \mid T^+)$, $\mathbb{P}(D^- \mid T^-)$ | Yes (Theorem 3.3.1) |
  | $\mathrm{LR}^\pm$ | $\mathrm{Se}/(1 - \mathrm{Sp})$, $(1 - \mathrm{Se})/\mathrm{Sp}$ | No; posttest odds = pretest odds × LR (Formula 3.3.1) |

  At a prevalence of 1.1% the PPV of LDCT is only 3.8% (Example 3.3.1); when prevalence is low the PPV is determined by specificity, and when it is high the NPV is determined by sensitivity (Example 3.3.2). Tests in series raise specificity and tests in parallel raise sensitivity, provided they are conditionally independent.
- The **ROC curve** plots $(1 - \mathrm{Sp}, \mathrm{Se})$ for all cutoffs; the **area under the curve** $= \mathbb{P}(X_D > X_N) + \frac12\mathbb{P}(X_D = X_N)$ (Theorem 3.4.1), and the AUC of the CT scores is 0.893 (Example 3.4.1). The Youden index (Definition 3.4.1) gives the cutoff when costs are equal; in practice the choice depends on the costs of misdiagnosis and on the prevalence.
- The posterior probabilities with several diagnoses are determined jointly by the likelihood and the prior: the same biopsy findings point to sarcoidosis in a nonsmoker and to lung cancer in a heavy smoker (Example 3.5.1).

## Questions

1. The prevalence of type 2 diabetes among people aged 40–59 in a city is 7% in whites, 10% in African Americans, 12% in Latinos and 5% in Asians; the composition of the population of this age group is 30% white, 25% African American, 40% Latino and 5% Asian. Find the overall prevalence in this age group; if a person with diabetes is drawn at random, what is the probability that he or she is Latino?

   **Answer** By the law of total probability, $\mathbb{P}(\mathrm{DM}) = 0.07 \times 0.30 + 0.10 \times 0.25 + 0.12 \times 0.40 + 0.05 \times 0.05 = 0.021 + 0.025 + 0.048 + 0.0025 = 0.0965$. By Bayes' formula, $\mathbb{P}(\text{Latino} \mid \mathrm{DM}) = 0.048/0.0965 = 0.497$. Latinos make up 40% of the population but half of the patients, because their prevalence is the highest.

2. A study reports the relation between PSA ≥ 4.1 ng/mL and prostate cancer: 92 with positive PSA and cancer, 27 positive without cancer, 46 negative with cancer, and 72 negative without cancer (everyone was biopsied). Find the sensitivity, specificity, PPV and NPV. What is the PPV if the test is used in a general population with a prevalence of 5%?

   **Answer** $\mathrm{Se} = 92/138 = 0.667$, $\mathrm{Sp} = 72/99 = 0.727$, and within the table $\mathrm{PPV} = 92/119 = 0.773$, $\mathrm{NPV} = 72/118 = 0.610$. The prevalence in the table is $138/237 = 58\%$ (a group biopsied because of symptoms or abnormalities), so the predictive values are high. In a population with a prevalence of 5%, $\mathrm{PPV} = \frac{0.667 \times 0.05}{0.667 \times 0.05 + 0.273 \times 0.95} = \frac{0.0333}{0.2926} = 0.114$: only about 11% of those with a positive result truly have cancer. Predictive values cannot be moved from one population to another, whereas sensitivity and specificity can (when the spectra of patients are similar).

3. A rare disease has a prevalence of 1/10,000. A test has a sensitivity of 99% and a specificity of 99%. What is the probability that a person with a positive test has the disease? If he repeats the same test and is positive again (assume conditional independence), what is the probability?

   **Answer** $\mathrm{LR}^+ = 0.99/0.01 = 99$. The pretest odds are $\approx 1/9999$, the odds after one positive result are $99/9999 = 0.0099$, and the probability is $0.98\%$, less than 1%. A second positive result multiplies by 99 again: the odds are $0.98$ and the probability $0.495$. Even for a "99% accurate" test, a single positive result in a rare disease is almost always a false positive; a conditionally independent repeat test can raise the PPV substantially, but in practice the errors of a repeated test are often correlated (the same interfering substance), and one should confirm with another test based on a different principle.

4. A chronic disease has an incidence rate of 5/1000 per year, and patients survive on average 8 years after diagnosis. Estimate the prevalence of the disease in a stable population. If a new therapy extends the mean survival of patients to 16 years without changing incidence, how does the prevalence change? What does this show?

   **Answer** $I\bar D = 0.005 \times 8 = 0.04$, $P = 0.04/1.04 = 3.85\%$ (about 4%). With survival extended to 16 years, $I\bar D = 0.08$ and $P = 0.08/1.08 = 7.4\%$, nearly doubling the prevalence. An effective therapy raises the prevalence; comparing the prevalence in two regions or two periods does not show where people are more likely to fall ill, and studies of etiology and prevention should compare incidence rates.

5. In a cohort study the follow-up of 5 participants is: A followed for 4 years without disease; B developed the disease after 2 years; C was lost to follow-up after 3 years; D followed for 5 years without disease; E developed the disease after 1 year. Find the person-time and the incidence rate. Why can "2 cases / 5 people = 40%" not be used as the incidence?

   **Answer** Person-time $= 4 + 2 + 3 + 5 + 1 = 15$ person-years (those who became ill count until the onset, and those lost to follow-up until they were lost). The incidence rate $= 2/15 = 0.133$ per person-year, that is 13.3 cases per 100 person-years. "40%" treats people followed for 1 year and for 5 years alike and does not specify the period; C had not developed the disease before being lost, but we do not know whether he did later, and counting him as "not diseased" would underestimate incidence. The person-time denominator correctly reflects the amount of observation each person contributes (this approach implicitly assumes a constant incidence rate, [7.7.16](/7.7.16)).

6. A new blood test is used for colorectal cancer screening. The investigators recruit 100 patients with confirmed advanced colorectal cancer and 100 healthy blood donors and obtain a sensitivity of 95% and a specificity of 98%. Point out the design problems of this study and estimate how these numbers may change in real screening.

   **Answer** The main problem is spectrum bias: the cases are all advanced, with a large tumor burden and high marker levels, so the sensitivity is overestimated; screening is meant to find early cancers and advanced adenomas, and the sensitivity will be much lower. The controls are healthy blood donors, without inflammatory bowel disease, hemorrhoids and other conditions that cause false positives, so the specificity is also overestimated. In addition, with 100 cases and 100 controls the "prevalence" in the table is 50%, a hundred times that of the screening population (about 0.5%), so the PPV cannot be estimated directly from this table. The test should be done prospectively in the population that will be screened (such as asymptomatic people aged 50–75), with everyone confirmed by colonoscopy as the gold standard.

7. In Example 3.4.1, suppose the radiologist calls grade 3 and above positive; find the sensitivity, specificity and Youden index. In a setting extremely sensitive to missed diagnoses (the consequences of a missed diagnosis far outweigh those of a false alarm), which cutoff would you recommend?

   **Answer** At 3+, $\mathrm{Se} = (2 + 11 + 33)/51 = 0.902$, $\mathrm{Sp} = (33 + 6)/58 = 0.672$, $J = 0.574$. The Youden index is largest at 4+ (0.639), which corresponds to equal costs of false positives and false negatives. If the cost of a missed diagnosis is much greater than that of a false alarm, a cutoff with higher sensitivity should be chosen, such as 2+ ($\mathrm{Se} = 0.941$, $\mathrm{Sp} = 0.569$), accepting more false positives and ruling them out by further examination; in the optimal slope $C(1 - \pi)/\pi$ the cost ratio $C$ (false alarm/missed diagnosis) is small, and the optimal point moves to the upper right part of the ROC curve.

8. Prove that for a test with only two results, positive and negative, the area under its ROC "curve" (the polyline connecting $(0,0)$, $(1 - \mathrm{Sp}, \mathrm{Se})$ and $(1,1)$) is $(\mathrm{Se} + \mathrm{Sp})/2$, and use this to interpret the Youden index.

   **Answer** By the trapezoidal rule the first trapezoid has area $\frac12 \mathrm{Se}(1 - \mathrm{Sp})$ and the second $\frac12(\mathrm{Se} + 1)\mathrm{Sp}$. Adding gives $\frac12[\mathrm{Se} - \mathrm{Se}\,\mathrm{Sp} + \mathrm{Se}\,\mathrm{Sp} + \mathrm{Sp}] = \frac{\mathrm{Se} + \mathrm{Sp}}{2}$. Hence $\mathrm{AUC} - \frac12 = \frac{\mathrm{Se} + \mathrm{Sp} - 1}{2} = J/2$: the Youden index is twice the amount by which the AUC of a single-cutoff test exceeds random guessing (0.5), and also the vertical distance from the ROC point to the diagonal.

9. (Open question) A region plans to screen all residents over 50 for lung cancer with an imaging examination whose PPV is only 4%. As a statistical consultant, what questions and recommendations would you raise?

   **Answer** Key points: (1) Prevalence determines the PPV: the 4% of the NLST was obtained in heavy smokers, and the prevalence among all residents over 50 (including many nonsmokers) is much lower, so the PPV would be even lower and there would be more false positives; screening should therefore be limited to high-risk people (selected by age and pack-years of smoking, or by a risk prediction model). (2) The value of screening lies not in the PPV but in whether it reduces mortality: there must be evidence from randomized trials (the NLST and NELSON showed a reduction in mortality in high-risk people), and overdiagnosis and lead-time bias must be considered ([7.7.18](/7.7.18)). (3) Set up a graded follow-up protocol for positive results (for example by nodule size and growth) to raise specificity and reduce invasive procedures. (4) Estimate costs and harms: how many false-positive follow-ups, biopsies and complications per cancer detected. (5) Design an evaluation plan: record the positivity rate, biopsy rate, cancer detection rate and stage of screening, and compare with an unscreened population.
