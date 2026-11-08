---
title: Design and Analysis of Epidemiologic Studies
description: Cohort, case-control, cross-sectional and ecological studies and what each can estimate; risk difference, relative risk and odds ratio with confidence intervals, and the approximation of RR by OR for rare diseases; attributable fractions and the number needed to treat; selection bias, information bias and confounding; direct and indirect standardization; stratified analysis, the Mantel–Haenszel method and effect modification; dose response and the Bradford Hill criteria; matched case-control studies. The examples are the Doll–Hill case-control study, the British doctors' cohort, the Physicians' Health Study and a study of passive smoking.
source_hash: 31097c83c31c
---

The preceding chapters treated the 2×2 table as an object of testing ([7.7.9](/7.7.9)): do the proportions in two groups differ? Epidemiology asks more specific questions. By how much does the exposure raise the risk of disease? How many cases in the population can be attributed to the exposure? Are the two groups compared comparable? The answers depend first of all on how the data were collected. This chapter begins by comparing four kinds of observational design (cohort, case-control, cross-sectional and ecological studies) and the measures of effect each can estimate (risk difference, relative risk, odds ratio), and then discusses the three kinds of bias in observational studies, with emphasis on confounding: standardization and stratified analysis (the Mantel–Haenszel method) are the classical tools for dealing with confounding before logistic regression, and they show most directly the difference between confounding and effect modification. The whole chapter develops along the thread of smoking: the Doll–Hill case-control study of [7.7.3](/7.7.3) Example 3.1.3 gave an odds ratio of 14, and here we add its interval and interpretation; the British doctors' cohort gives the dose-response relationship; and finally the Bradford Hill criteria answer "when can an association be regarded as causal?". The basic measures of disease frequency (**prevalence**, **cumulative incidence**, **person-time** and **incidence rate**) were defined in [7.7.3](/7.7.3); methods that adjust for several variables at once are the logistic and Poisson regression of [7.7.14](/7.7.14); the formal framework of causal inference is in [7.7.15](/7.7.15); the design of randomized controlled trials and meta-analysis are in [7.7.18](/7.7.18).

## 13.1. Study Designs

### 13.1.1. Cohort Studies

**Definition 13.1.1 (Cohort Study)** A study that selects a group of people who do not have the disease under study at the start, divides them by exposure status, follows them for a period and compares the new cases in each group is called a **cohort study**. A cohort recruited at the start and followed into the future is called a prospective cohort; one reconstructed from existing records (occupational files, medical records) at some time in the past and followed up to the present is called a retrospective (historical) cohort.

The time direction of a cohort study agrees with the direction of causation: exposure first, then disease. It gives the **cumulative incidence** or **incidence rate** of each group directly and so can estimate all the measures of effect (Section 13.2), and it can study several outcomes of one exposure at once. The cost is the need for a large sample and long follow-up: for a rare disease, tens of thousands of people must be followed for years to accumulate enough cases.

**Example 13.1.1 (The British Doctors' Cohort)** In 1951 Doll and Hill sent a questionnaire about smoking habits to all registered doctors in Britain; 34 439 male doctors were enrolled for follow-up, their smoking status was re-surveyed several times thereafter, and each doctor's death and cause of death were ascertained from death registers until 2001 (Doll et al. 2004). This is a prospective cohort: smoking status was recorded before death and was not influenced by the cause of death. The choice of doctors was also deliberate: they are easy to follow, their causes of death are diagnosed reliably, and the proportion who smoked was similar to that in the general population.

### 13.1.2. Case-Control Studies

**Definition 13.1.2 (Case-Control Study)** A study that selects a group of people who have the disease under study (cases) and a group of people who do not have it and who represent the population that produced the cases (controls), and compares the past exposure of the two groups retrospectively, is called a **case-control study**.

Sampling in a case-control study is conditional on disease: the numbers of cases and controls are decided by the investigator and are usually of comparable size, so the proportion of cases in the sample is far higher than the proportion of the disease in the population. It therefore cannot estimate the risk of disease directly and can only compare the proportions exposed in the two groups ([7.7.3](/7.7.3) Example 3.1.3). Its advantage is that it saves time and money and suits rare diseases and diseases with long latency: the Doll–Hill study of 1950 used only 649 pairs of cases and controls and reached its conclusion several years earlier than the cohort studies that followed.

The choice of controls is the central difficulty of case-control studies: controls should be people who "would have entered the study as cases had they developed the disease". Hospital controls are convenient, but their diseases may also be related to the exposure (using patients with other smoking-related diseases as controls for lung cancer underestimates the effect of smoking); community controls are more representative but often have low response rates.

### 13.1.3. Cross-Sectional and Ecological Studies

**Definition 13.1.3 (Cross-Sectional and Ecological Studies)** A study that measures the exposure and disease status of everyone in a sample at the same time is called a **cross-sectional study**; a study whose unit of analysis is the group (country, region, period) rather than the individual, and which compares only the mean exposure and disease frequency of the groups, is called an **ecological study**.

A cross-sectional study estimates **prevalence** and not incidence, and what it compares is the ratio of prevalences ([7.7.3](/7.7.3) Section 3.2.3 explained that prevalence depends on both incidence and duration); it also cannot establish temporal order: the FEV data ([7.7.1](/7.7.1)) form a cross-sectional study in which smoking and lung function were measured at the same time. The data of ecological studies are often readily available (mortality rates and per capita consumption by country) and are often used for generating hypotheses, but associations at the group level cannot be carried over to individuals (the ecological fallacy, [7.7.15](/7.7.15)).

### 13.1.4. Designs and What They Can Estimate

![The direction of inquiry in the three basic observational designs (schematic). Cohort study: people free of disease at the start are grouped by exposure and followed into the future for new cases; the risk of disease in each group, the relative risk and the risk difference can be estimated. Case-control study: cases and controls are identified first and their past exposure is then examined; only the odds ratio can be estimated. Cross-sectional study: exposure and disease are measured at the same time, and prevalences and the ratio of prevalences are estimated](./plots/study-designs.py)

| Design | Basis of sampling | Directly estimates | Measures of effect | Main advantages | Main limitations |
|---|---|---|---|---|---|
| Randomized controlled trial | Random allocation of treatment | Risk of disease in each group | RD, RR, OR, NNT | Eliminates confounding ([7.7.5](/7.7.5)) | Many exposures cannot be assigned; costly |
| Prospective cohort | Exposure | Risk or incidence rate of disease in each group | RD, RR, rate ratio, OR | Clear temporal order; multiple outcomes | Large samples, long follow-up; loss to follow-up |
| Case-control | Disease | Proportions exposed in the two groups | OR only | Fast, cheap; suits rare diseases | Choice of controls; recall bias |
| Cross-sectional | Neither fixed | Prevalence | Ratio of prevalences, OR | Fast; describes burden | Unclear temporal order; duration mixed in |
| Ecological | Group | Group means | Correlation among groups | Data readily available | Cannot be carried over to individuals |

A randomized trial is an **experimental study** and all the others are **observational studies** ([7.7.1](/7.7.1), Section 1.5). Conclusions of observational studies must be treated with special care because the exposed and unexposed groups are not formed at random and may differ in many respects.

## 13.2. Measures of Effect

### 13.2.1. Three Measures

Let the risk of disease (cumulative incidence) over a period be $p_1$ in the exposed and $p_2$ in the unexposed. The four-fold table is

| | Diseased | Not diseased | Total |
|---|---|---|---|
| Exposed | $a$ | $b$ | $n_1$ |
| Unexposed | $c$ | $d$ | $n_2$ |

**Definition 13.2.1 (Risk Difference, Relative Risk and Odds Ratio)** The difference $\mathrm{RD} = p_1 - p_2$ of the risks of disease in the exposed and unexposed is called the **risk difference**; the ratio $\mathrm{RR} = p_1/p_2$ is called the **relative risk**; and the ratio of the odds of disease

$$
\mathrm{OR} = \frac{p_1/(1 - p_1)}{p_2/(1 - p_2)}
$$
is called the **odds ratio**. From cohort data the three are estimated by $\widehat{\mathrm{RD}} = a/n_1 - c/n_2$, $\widehat{\mathrm{RR}} = (a/n_1)/(c/n_2)$ and $\widehat{\mathrm{OR}} = ad/(bc)$. When follow-up times differ and comparison is by incidence rates $I_1, I_2$, $I_1/I_2$ is called the **rate ratio**.

RD is a measure on the absolute scale (how many extra cases per 100 exposed), while RR and OR are measures on the relative scale. With no association they are 0, 1 and 1 respectively. Chinese textbooks often call RD the "attributable risk", which is easily confused with the attributable fractions of Section 13.3, so here the term "risk difference" is used throughout.

### 13.2.2. Interval Estimation

The sampling distribution of a ratio is skewed and approximately normal on the log scale, so the interval is found on the log scale and then exponentiated.

**Formula 13.2.1 (Confidence Intervals for RR and OR)** In large samples,

$$
\operatorname{Var}(\ln \widehat{\mathrm{RR}}) \approx \frac{b}{a n_1} + \frac{d}{c n_2}, \qquad \operatorname{Var}(\ln \widehat{\mathrm{OR}}) \approx \frac1a + \frac1b + \frac1c + \frac1d,
$$
and the 95% interval is $\exp\bigl(\ln\widehat{\mathrm{RR}} \pm 1.96\sqrt{\operatorname{Var}}\bigr)$, and likewise for OR (the latter is called Woolf's method). For the rate ratio, $\operatorname{Var}(\ln \hat I_1/\hat I_2) \approx 1/a + 1/c$, where $a$ and $c$ are the numbers of cases in the two groups. The interval for RD uses the normal approximation directly, $\hat p_1 - \hat p_2 \pm 1.96\sqrt{\hat p_1\hat q_1/n_1 + \hat p_2\hat q_2/n_2}$ ([7.7.9](/7.7.9), Section 9.1).

All these variances come from the **delta method**: for example the variance of $\ln \hat p_1$ is $\operatorname{Var}(\hat p_1)/p_1^2 = (1 - p_1)/(n_1 p_1)$, and the two groups being independent, adding gives the variance of $\ln\widehat{\mathrm{RR}}$. The logarithm is undefined if any cell is 0; one often adds 0.5 to each cell or uses exact methods.

**Example 13.2.1 (The Physicians' Health Study)** In the randomized trial of [7.7.3](/7.7.3) Example 3.1.4, 139 of 11 037 in the aspirin group and 239 of 11 034 in the placebo group had a myocardial infarction:

| Measure | Estimate | 95% interval |
|---|---|---|
| RD | $1.26\% - 2.17\% = -0.91\%$ | $(-1.25\%, -0.56\%)$ |
| RR | $0.581$ | $(0.473, 0.715)$ |
| OR | $0.576$ | $(0.467, 0.711)$ |

The risk of myocardial infarction is about 2%, and OR and RR are almost the same.

**Example 13.2.2 (The Interval for Doll–Hill)** In [7.7.3](/7.7.3) Example 3.1.3, 647 of 649 male lung cancer cases smoked, against 622 of 649 controls. $\widehat{\mathrm{OR}} = 647 \times 27/(2 \times 622) = 14.0$, $\operatorname{Var}(\ln\widehat{\mathrm{OR}}) = 1/647 + 1/622 + 1/2 + 1/27 = 0.540$, the standard error is $0.735$, and the 95% interval is $\exp(2.642 \pm 1.96 \times 0.735) = (3.3, 59.3)$. The interval is wide because there are only 2 nonsmoking cases: almost all of the variance comes from the term $1/2$. **Fisher's exact test** gives $p = 1.3 \times 10^{-6}$. Even at the lower limit of the interval, the odds of lung cancer in smokers are more than 3 times those in nonsmokers.

### 13.2.3. For Rare Diseases the OR Approximates the RR

By definition,

$$
\mathrm{OR} = \mathrm{RR} \times \frac{1 - p_2}{1 - p_1}.
$$
When both risks are small the fraction on the right is close to 1, and OR ≈ RR; when the risks are larger, the OR is farther from 1 than the RR. For example, with RR = 2 the ORs for baseline risks of 1%, 10%, 20% and 30% are 2.02, 2.25, 2.67 and 3.50. In birthwt, low birth weight is not rare (31%): the RR for smoking mothers is $0.405/0.252 = 1.61$ and the OR is 2.02 ([7.7.9](/7.7.9), Section 9.8.1), and to describe the latter as "doubling the risk" would be an exaggeration.

### 13.2.4. Why a Case-Control Study Can Estimate Only the OR

**Theorem 13.2.1 (Symmetry of the Odds Ratio)** The odds ratio of exposure and disease equals both the ratio of the odds of disease in the exposed and unexposed and the ratio of the odds of exposure in cases and non-cases:

$$
\frac{\mathbb{P}(D \mid E)/\mathbb{P}(\bar D \mid E)}{\mathbb{P}(D \mid \bar E)/\mathbb{P}(\bar D \mid \bar E)} = \frac{\mathbb{P}(E \mid D)/\mathbb{P}(\bar E \mid D)}{\mathbb{P}(E \mid \bar D)/\mathbb{P}(\bar E \mid \bar D)}.
$$
Hence, as long as the sampling of cases and controls is independent of exposure (the cases are a random sample of all cases and the controls a random sample of non-cases), $ad/(bc)$ in a case-control study is an unbiased (consistent) estimate of the population OR, whereas the relative risk and the risk difference depend on the sampling proportions of cases and controls and cannot be estimated.

**Proof** Both sides equal $\dfrac{\mathbb{P}(D \cap E)\,\mathbb{P}(\bar D \cap \bar E)}{\mathbb{P}(\bar D \cap E)\,\mathbb{P}(D \cap \bar E)}$: on the left $\mathbb{P}(E)$ and $\mathbb{P}(\bar E)$ cancel between numerator and denominator, and on the right $\mathbb{P}(D)$ and $\mathbb{P}(\bar D)$ cancel. Case-control sampling draws cases with proportion $f_1$ and non-cases with proportion $f_0$, independently of exposure, so the expected numbers of the four kinds of people (exposed cases, unexposed cases, exposed controls, unexposed controls) are $f_1\,N\mathbb{P}(D \cap E)$, $f_1\,N\mathbb{P}(D \cap \bar E)$, $f_0\,N\mathbb{P}(\bar D \cap E)$ and $f_0\,N\mathbb{P}(\bar D \cap \bar E)$ ($N$ is the size of the population). In the ratio of cross products $f_1 f_0$ cancels, giving the expression above; but "the proportion of cases among the exposed" equals $f_1\mathbb{P}(D \cap E)/[f_1\mathbb{P}(D \cap E) + f_0\mathbb{P}(\bar D \cap E)]$, which depends on the $f_1/f_0$ chosen by the investigator. $\square$

Combined with Section 13.2.3: for a rare disease, the OR of a case-control study approximately estimates the RR. This is why the 14.0 of Doll–Hill can be read as "the risk of lung cancer in smokers is about 14 times that in nonsmokers"; the later cohort study (Example 13.7.1) gave a rate ratio of 14.6 for current smokers, a surprisingly close value. Modern case-control studies often sample controls from a cohort according to time of onset (risk-set sampling in a nested case-control study), and then the OR needs no rare-disease assumption and directly estimates the rate ratio.

## 13.3. Attributable Fractions and the Number Needed to Treat

### 13.3.1. Attributable Fractions in the Exposed and in the Population

The relative risk answers "how many times higher is the risk in the exposed than in the unexposed", whereas public health is more concerned with "how many cases could be avoided if the exposure were eliminated".

**Definition 13.3.1 (Attributable Fraction)** The proportion of cases among the exposed that can be attributed to the exposure,

$$
\mathrm{AF}_{\mathrm{e}} = \frac{p_1 - p_2}{p_1} = \frac{\mathrm{RR} - 1}{\mathrm{RR}},
$$
is called the **attributable fraction among the exposed**. The proportion of cases in the whole population that can be attributed to the exposure,

$$
\mathrm{PAF} = \frac{p - p_2}{p} = \frac{p_E(\mathrm{RR} - 1)}{1 + p_E(\mathrm{RR} - 1)},
$$
is called the **population attributable fraction**, where $p$ is the overall risk of disease in the population and $p_E$ is the proportion of the population exposed. The second equality is called Levin's formula.

Both formulas assume that the relation between exposure and disease is causal and unconfounded; they refer to "the risk of the exposed falling to the level of the unexposed". With confounding, PAF must use the adjusted RR and Miettinen's equivalent form $\mathrm{PAF} = p_c(\mathrm{RR} - 1)/\mathrm{RR}$, where $p_c$ is the proportion of cases who are exposed; this can be estimated directly in a case-control study (with OR in place of RR).

**Example 13.3.1** Among British doctors, the lung cancer mortality of current smokers is 2.49 per 1000 per year and that of never smokers is 0.17 per 1000 (Example 13.7.1); RR = 14.6 and $\mathrm{AF}_{\mathrm{e}} = 93\%$: about 93% of the lung cancer deaths among smokers would not have occurred. If 25% of men in some population smoked (the figure is made up for illustration), $\mathrm{PAF} = 0.25 \times 13.6/(1 + 0.25 \times 13.6) = 77\%$. In the Doll–Hill cases $647/649 = 99.7\%$ smoked, and by Miettinen's formula $\mathrm{PAF} = 0.997 \times 13.0/14.0 = 93\%$: in London in 1950 about nine tenths of lung cancer in men was attributable to smoking.

The population attributable fraction depends on both RR and the prevalence of exposure: an exposure with a very high RR but rare (some occupational exposure) may contribute less to the disease burden of a population than an exposure with a modest RR that is widespread. The RR for ischemic heart disease in British doctors is only $10.01/6.19 = 1.6$, but its baseline mortality is high, and smoking causes 3.8 extra deaths from heart disease per year per 1000 smokers, more than the 2.3 from lung cancer: on the absolute scale, smoking kills more heart disease patients than lung cancer patients.

### 13.3.2. The Number Needed to Treat

**Definition 13.3.2 (Number Needed to Treat)** The number of people who must be treated for a specified time to prevent one additional adverse event compared with control, $\mathrm{NNT} = 1/\lvert\mathrm{RD}\rvert$, is called the **number needed to treat**. When the treatment increases some adverse event (such as bleeding), $1/\mathrm{RD}$ is called the number needed to harm (NNH).

**Example 13.3.2** In the Physicians' Health Study $\mathrm{RD} = -0.91\%$ and $\mathrm{NNT} = 1/0.0091 = 110$: over about 5 years, one myocardial infarction is prevented for every 110 male doctors who take aspirin; taking reciprocals of the two ends of the interval for RD, the 95% interval for NNT is about 80–177. The same RR = 0.58 applied in a population whose baseline risk is 10 times higher (such as secondary prevention after myocardial infarction) gives an RD 10 times larger as well, and an NNT of about 11.

:::

RR is suited to being carried between populations (it is often fairly stable across risk levels), whereas RD and NNT determine the trade-offs at the individual and policy levels: for primary prevention the NNT is about 100, and then whether the serious bleeding caused by treatment is rare enough becomes the key question. Reporting only RR ("a 42% reduction in risk") and not the absolute risk readily exaggerates the benefit of a preventive measure. Later trials of aspirin for primary prevention and the synthesis of evidence are in [7.7.18](/7.7.18).

## 13.4. Bias

Errors of estimation are of two kinds: random error decreases as the sample size grows and is expressed by confidence intervals; systematic error (bias) does not decrease with sample size, and a large sample only makes a biased estimate more "precise".

**Definition 13.4.1 (Types of Bias)** Error that arises from the way study subjects are selected into or retained in the study and makes the association between exposure and disease in the study sample differ from that in the target population is called **selection bias**; error arising from measurement error and misclassification of exposure or disease is called **information bias**; and information bias arising because cases recall past exposures more completely (or differently) than controls is called **recall bias**.

- Typical examples of selection bias: in hospital case-control studies, controls whose diseases are related to the exposure; in cohort studies, loss to follow-up related to both exposure and outcome (the seriously ill among smokers are more likely to be lost); the healthy worker effect when the subjects are employed people ([7.7.6](/7.7.6), Section 6.7); and Berkson bias when only hospitalized patients are analyzed (two unrelated diseases are negatively associated among inpatients, [7.7.15](/7.7.15)).
- Information bias is of two kinds. When misclassification is unrelated to study group (nondifferential misclassification), the association for a dichotomous exposure is generally pulled toward the null value 1; when it is related to study group (differential misclassification) the direction is uncertain. Recall bias is differential: a mother who has borne a malformed baby will go over every drug she took in pregnancy again and again, whereas the mother of a normal baby will not. Using medical records from the pregnancy instead of questionnaires after the event, and blinding the interviewers, can reduce it.
- Confounding (the next section) differs from the other two: it is not an error of measurement but the fact that the exposed and unexposed groups were not comparable to begin with.

## 13.5. Confounding and Standardization

### 13.5.1. Confounding

**Definition 13.5.1 (Confounding)** The phenomenon in which, because the exposed and unexposed groups are distributed differently in other factors affecting the outcome, the crude association between exposure and outcome departs from the true effect of the exposure is called **confounding**; the variable that causes it is called a confounder. A confounder usually satisfies three conditions: (1) it is related to the outcome (also a risk factor for the outcome among the unexposed); (2) it is related to the exposure; (3) it is not an intermediate step in the pathway from exposure to outcome.

The FEV example is confounding: age affects lung function, only the older children smoke, and age is clearly not a consequence of smoking; without adjustment for age the "effect" of smoking is +0.71 L, and after adjustment it becomes negative ([7.7.10](/7.7.10) Example 10.7.1). The three conditions are only a rule of thumb: condition (3) says that mediators should not be adjusted for, and some variables satisfying (1) and (2) introduce bias when adjusted for; the precise judgment by causal diagrams is in [7.7.15](/7.7.15).

There are two kinds of ways to deal with confounding. At the design stage: randomization (applicable only to experiments), restriction (studying only one age range) and matching (Section 13.8). At the analysis stage: standardization, stratified analysis (Section 13.6) and regression models ([7.7.14](/7.7.14)).

### 13.5.2. Coronary Deaths Among British Doctors

**Example 13.5.1** In the first 10 years of follow-up of the British doctors' cohort, coronary deaths grouped by age and smoking status in 1951 were as follows (Doll and Hill 1966; as arranged by Breslow and Day 1987):

| Age / years | Smokers: deaths | Person-years | Rate / 100 000 person-years | Nonsmokers: deaths | Person-years | Rate / 100 000 person-years | Rate ratio |
|---|---|---|---|---|---|---|---|
| 35–44 | 32 | 52 407 | 61 | 2 | 18 790 | 11 | 5.74 |
| 45–54 | 104 | 43 248 | 240 | 12 | 10 673 | 112 | 2.14 |
| 55–64 | 206 | 28 612 | 720 | 28 | 5 710 | 490 | 1.47 |
| 65–74 | 186 | 12 663 | 1469 | 28 | 2 585 | 1083 | 1.36 |
| 75–84 | 102 | 5 317 | 1918 | 31 | 1 462 | 2120 | 0.90 |
| Total | 630 | 142 247 | 443 | 101 | 39 220 | 258 | 1.72 |

The pooled crude rate ratio is 1.72 (95% interval 1.39–2.12). But the age compositions of the two groups differ: 48% of the person-years of nonsmokers come from ages 35–44, against only 37% for smokers. Coronary mortality rises steeply with age (severalfold per 10 years), so the crude rate of the younger nonsmoking group is low and the crude rate ratio exaggerates the effect of smoking. The comparison should be among people of the same age.

![Coronary deaths in the first 10 years of follow-up of British male doctors, grouped by age and smoking status in 1951 (Doll and Hill 1966; as arranged by Breslow and Day 1987). A: mortality of smokers and nonsmokers in each age group (per 100 000 person-years, log scale). B: rate ratios by age group with 95% intervals (log scale); the dashed line is the crude rate ratio 1.72 of the pooled population, and the solid line the age-standardized rate ratio: direct standardization with the combined person-years of the two groups as the standard population and the Mantel–Haenszel estimate are both 1.42. The rate ratio falls with increasing age and is below 1 in the oldest group](./plots/coronary-age.py)

### 13.5.3. Direct and Indirect Standardization

**Definition 13.5.2 (Direct and Indirect Standardization)** Let $r_{1k}, r_{2k}$ be the rates of the two groups in the $k$-th age stratum. Choose a standard population with proportions $w_k$ in the strata ($\sum_k w_k = 1$) and average the stratum-specific rates of each group with the same weights,

$$
R_j^{\mathrm{dir}} = \sum_k w_k r_{jk};
$$
this is called **direct standardization**, and $R_1^{\mathrm{dir}}/R_2^{\mathrm{dir}}$ is the standardized rate ratio. Applying the stratum-specific rates $r_k^*$ of a reference population to the person-time $T_k$ of each stratum of the study group gives the expected number $E = \sum_k r_k^* T_k$; the comparison by the ratio $O/E$ of the observed number to it is called **indirect standardization**, and $O/E$ is the **standardized mortality ratio** ([7.7.6](/7.7.6) Definition 6.7.1).

**Example 13.5.2** With the combined person-years of the two groups as the standard population (stratum proportions 0.392, 0.297, 0.189, 0.084, 0.037), the directly standardized death rates are 427 for smokers and 301 for nonsmokers (per 100 000 person-years), and the standardized rate ratio is $427/301 = 1.42$. Indirect standardization: applying the stratum-specific rates of nonsmokers to the person-years of smokers gives 444.4 expected deaths against 630 observed, $\mathrm{SMR} = 630/444.4 = 1.42$ (exact 95% interval 1.31–1.53). Both methods reduce the crude rate ratio 1.72 to 1.42: about four tenths (0.30/0.72) of the 72% excess shown by the crude rate ratio comes from the difference in age composition.

:::

Direct standardization needs the stratum-specific rates of each group (each stratum must have enough events), and the result depends on the choice of standard population; indirect standardization needs only the total number observed in the study group and the person-time in each stratum, and suits small study populations (the workers of one factory), but it weights by the study group's own age composition, so the SMRs of two study groups should not be compared directly ([7.7.6](/7.7.6), Section 6.7). Age-standardized mortality rates published by countries often use the WHO world standard population; with different standard populations the standardized rates differ in value, but if the rate ratios in the strata are roughly constant, the standardized rate ratio changes little.

## 13.6. Stratified Analysis and the Mantel–Haenszel Method

### 13.6.1. Combining the Estimates of the Strata

Standardization is a kind of weighted average of rates. More generally, divide the data into $K$ strata by the confounder, compare the exposed and unexposed within each stratum, and combine the effects of the strata into one overall estimate, provided that the effects of the strata are roughly the same. Write the 2×2 table of stratum $i$ as $a_i, b_i, c_i, d_i$ ($a_i$ exposed cases, $b_i$ unexposed cases, $c_i$ exposed controls, $d_i$ unexposed controls), with $n_i$ the total in the stratum.

**Formula 13.6.1 (The Mantel–Haenszel Method)** When the odds ratios of the strata are the same, the Mantel–Haenszel estimate of the common odds ratio is

$$
\widehat{\mathrm{OR}}_{\mathrm{MH}} = \frac{\sum_i a_i d_i/n_i}{\sum_i b_i c_i/n_i}.
$$
To test $H_0$ that the OR of every stratum is 1: conditional on the margins of each stratum, $a_i$ has a hypergeometric distribution,

$$
\mathbb{E}(a_i) = \frac{(a_i + b_i)(a_i + c_i)}{n_i}, \qquad \operatorname{Var}(a_i) = \frac{(a_i + b_i)(c_i + d_i)(a_i + c_i)(b_i + d_i)}{n_i^2(n_i - 1)},
$$
$$
X^2_{\mathrm{MH}} = \frac{\bigl(\lvert \sum_i a_i - \sum_i \mathbb{E}(a_i)\rvert - 0.5\bigr)^2}{\sum_i \operatorname{Var}(a_i)} \overset{H_0}{\approx} \chi^2_1.
$$
This test is called the *Mantel–Haenszel test*, also the Cochran–Mantel–Haenszel test. With a single stratum it is the chi-square test of a 2×2 table (the denominator differing by a factor $n/(n-1)$); there is a corresponding form for rate data, $\widehat{\mathrm{RR}}_{\mathrm{MH}} = \sum_i (a_i T_{0i}/T_i)/\sum_i (b_i T_{1i}/T_i)$ ($a_i$, $b_i$ are the numbers of cases among the exposed and unexposed, $T_{1i}$, $T_{0i}$ the person-time of the two, and $T_i = T_{1i} + T_{0i}$).

$\widehat{\mathrm{OR}}_{\mathrm{MH}}$ is a weighted average of the ORs of the strata with weights $b_i c_i/n_i$ approximately proportional to the information in each stratum; it remains consistent when there are very many strata each of which is small (such as each pair in a matched study), which the inverse-variance weighting of Woolf's method does not. The variance of $\ln\widehat{\mathrm{OR}}_{\mathrm{MH}}$ is often estimated by the Robins–Breslow–Greenland formula (provided by software). In the British doctors' data of Example 13.5.2, $\widehat{\mathrm{RR}}_{\mathrm{MH}} = 1.42$, in agreement with direct standardization, and the MH test gives $X^2 = 11.0$, $p = 0.0009$.

**Example 13.6.1 (Passive Smoking and Cancer)** A 1985 case-control study (Sandler et al.) compared 518 cancer patients aged 15–59 with 518 controls matched for age and sex, the exposure being spouse smoking (passive smoking). A person's own smoking is related to cancer and also to whether the spouse smokes (smokers' spouses more often smoke), and is thus a potential confounder, so the data are stratified by own smoking:

| Own smoking | | Spouse smokes | Spouse does not smoke | Stratum OR (95% interval) |
|---|---|---|---|---|
| Nonsmoker | Cases | 120 | 111 | 2.09 (1.44, 3.04) |
| | Controls | 80 | 155 | |
| Smoker | Cases | 161 | 117 | 1.31 (0.93, 1.85) |
| | Controls | 130 | 124 | |

In the nonsmoking stratum, $\mathbb{E}(a_1) = 231 \times 200/466 = 99.1$ and $\operatorname{Var}(a_1) = 28.6$; in the smoking stratum, $\mathbb{E}(a_2) = 278 \times 291/532 = 152.1$ and $\operatorname{Var}(a_2) = 33.0$. There are 281 observed cases with a smoking spouse, against 251.2 expected, and

$$
X^2_{\mathrm{MH}} = \frac{(\lvert 281 - 251.2\rvert - 0.5)^2}{61.55} = 13.9, \qquad p = 0.0002.
$$
$\widehat{\mathrm{OR}}_{\mathrm{MH}} = (120 \times 155/466 + 161 \times 124/532)/(111 \times 80/466 + 117 \times 130/532) = 1.63$ (95% interval 1.26–2.09): among people with the same own smoking habit, the odds of cancer in those whose spouse smokes are 1.6 times those in those whose spouse does not. The crude OR of the pooled table is 1.64, almost the same as the adjusted one: in these data the person's own smoking did not cause noticeable confounding.

![Passive smoking and cancer, stratified by own smoking (518 cases and 518 controls, Sandler, Everson and Wilcox 1985). Odds ratios (cases against controls) for spouse smoking with 95% Woolf intervals: for nonsmokers, for smokers, the crude odds ratio of the pooled table, and the Mantel–Haenszel common odds ratio (Robins–Breslow–Greenland interval). The area of each square is proportional to the inverse variance of the log odds ratio](./plots/mh-forest.py)

### 13.6.2. Effect Modification

Combining presupposes that the effects of the strata are the same. When the effects in the strata really differ, combining them into one number hides important information.

**Definition 13.6.1 (Effect Modification)** The phenomenon in which the effect of an exposure (on some scale, such as OR or RR) differs according to the value of a third variable is called **effect modification**, and that variable is called an effect modifier.

Effect modification is the **interaction effect** of statistical models ([7.7.10](/7.7.10), Section 10.7.4; [7.7.12](/7.7.12), Section 12.5), and it depends on the scale: when the risks in two strata are 1% against 2% and 10% against 20%, RR is 2 in both (no modification on the multiplicative scale), while RD is 1% against 10% (modification on the additive scale). The usual tests of whether the ORs of the strata are the same are Woolf's test of homogeneity and the Breslow–Day test:

**Formula 13.6.2 (Woolf's Test of Homogeneity)** Let the variance of $\ln\widehat{\mathrm{OR}}_i$ be $v_i$, the weights $w_i = 1/v_i$, and $\bar L = \sum w_i \ln\widehat{\mathrm{OR}}_i/\sum w_i$. Under the hypothesis that the ORs of all strata are the same,

$$
X^2_{\mathrm{hom}} = \sum_i w_i(\ln\widehat{\mathrm{OR}}_i - \bar L)^2 \overset{H_0}{\approx} \chi^2_{K-1}.
$$

In Example 13.6.1, $X^2_{\mathrm{hom}} = 3.27$ with 1 degree of freedom and $p = 0.07$ (the Breslow–Day test is also 3.27): the OR for passive smoking appears larger in nonsmokers (2.1) than in smokers (1.3), but the evidence is insufficient. This is also plausible intuitively: smokers already receive a large dose of smoke, and the spouse's smoke adds relatively little. The power of homogeneity tests is usually low, and $p = 0.07$ cannot be taken as evidence of "no modification"; a report should give the estimates for each stratum as well.

The coronary example (Example 13.5.1) is clear effect modification: the rate ratio falls from 5.7 at ages 35–44 to 0.9 at ages 75–84; the likelihood-ratio test that the five rate ratios are equal gives $\chi^2_4 = 12.1$, $p = 0.016$, and the test for a linear trend of the rate ratio with age gives $p = 0.001$ ([7.7.14](/7.7.14) Example 14.8.1 uses an interaction term in Poisson regression). An "age-standardized rate ratio of 1.42" is then only a weighted average whose value depends on the standard population used; it is more informative to report by age: smoking multiplies the coronary death rate mainly in middle-aged people, whereas in the elderly the absolute excess death rate of smokers (386 more per 100 000 person-years at ages 65–74) is actually greater than in middle age.

### 13.6.3. The Difference Between Confounding and Effect Modification

| | Confounding | Effect modification |
|---|---|---|
| What it is | Bias from an unfair comparison | The effect itself varies with a third variable |
| How to recognize it | Estimates before and after adjustment clearly differ (empirically by more than 10%) | Estimates in the strata clearly differ |
| How to handle it | Adjust (standardization, pooling of strata, regression) and report the adjusted estimate | Report by stratum; do not combine; add an interaction term in the model |
| Does it depend on scale? | Not on whether RR or OR is used (but OR is noncollapsible, see below) | Yes (the multiplicative and additive scales can differ) |

A variable can be both a confounder and an effect modifier (age in Example 13.5.1) or just one of the two. **Simpson's paradox** ([3.3.10](/3.3.10)) is the most extreme case of confounding: the crude association is in the opposite direction to the association in every stratum. A detail: the OR is a "noncollapsible" measure: even when a third variable is not a confounder (independent of the exposure), adjusting for it moves the OR away from 1; RR and RD do not have this property. A change in OR before and after adjustment therefore does not necessarily show confounding, which is especially evident when the outcome is common.

## 13.7. Smoking and Lung Cancer: Dose Response and the Bradford Hill Criteria

### 13.7.1. Dose Response Among British Doctors

**Example 13.7.1 (Fifty Years of Follow-Up)** By 2001 more than 25 000 doctors in the British doctors' cohort had died, 1052 of them from lung cancer. Mortality rates (per 1000 per year) grouped by smoking habit at the most recent survey and indirectly standardized for age and year of survey were (Doll et al. 2004, Table 1):

| Cause of death | Never smoked | Ex-smokers | Current: 1–14/day | 15–24/day | ≥ 25/day | All current smokers |
|---|---|---|---|---|---|---|
| Lung cancer | 0.17 | 0.68 | 1.31 | 2.33 | 4.17 | 2.49 |
| Chronic obstructive pulmonary disease | 0.11 | 0.64 | 1.04 | 1.41 | 2.61 | 1.56 |
| Ischemic heart disease | 6.19 | 7.61 | 9.10 | 10.07 | 11.11 | 10.01 |
| All causes | 19.38 | 24.15 | 29.34 | 34.79 | 45.34 | 35.40 |

Relative to never smokers, the rate ratios for lung cancer are 7.7, 13.7 and 24.5 in current smokers of 1–14, 15–24 and ≥ 25 cigarettes per day, rising monotonically; the trend test has $\chi^2_1 = 452$ (taken from the original paper, tested by amount smoked). The rate ratio for ex-smokers is 4.0, between that of never smokers and current smokers. The rate ratio for ischemic heart disease is only 1.5–1.8, but the absolute excess is greater (Section 13.3). All-cause mortality in current smokers is 16 per 1000 per year higher than in never smokers.

![Mortality (per 1000 per year, indirectly standardized for age and year of survey) of British male doctors 1951–2001 (34 439 men; Doll, Peto, Boreham and Sutherland 2004, Table 1), grouped by smoking habit at the most recent survey. A: lung cancer, chronic obstructive pulmonary disease (COPD) and ischemic heart disease (IHD), for never smokers, ex-smokers, and current smokers of 1–14, 15–24 and ≥ 25 cigarettes per day in turn. B: rate ratios relative to never smokers (log scale): the rate ratios for lung cancer and COPD rise monotonically with amount smoked to about 24, and for ischemic heart disease only to 1.8](./plots/doctors-dose-response.py)

:::

The dose-response relationship is important evidence in causal inference: if the association between smoking and lung cancer arose only because smokers differ from nonsmokers in some unknown factor, that factor would also have to keep strict step with the amount smoked. The method of testing the trend is the same as the **Cochran–Armitage trend test** ([7.7.9](/7.7.9), Section 9.6); for rate data one uses Poisson regression with dose as a continuous variable ([7.7.14](/7.7.14)).

### 13.7.2. The Bradford Hill Criteria

In the 1950s there was a fierce debate on the conclusion that smoking causes lung cancer: Fisher suggested that there might be some hereditary "constitution" that both makes people like smoking and makes them prone to lung cancer ([7.7.15](/7.7.15), Section 15.6). Observational studies cannot randomize smoking, and a causal conclusion can come only from weighing evidence from many directions. In 1965 Bradford Hill listed nine aspects.

**Definition 13.7.1 (The Bradford Hill Criteria)** The nine aspects considered in judging whether an observed association reflects a causal relationship (strength of association, consistency, specificity, temporality, biological gradient (dose response), plausibility, coherence, experimental evidence and analogy) are called the **Bradford Hill criteria**.

| Aspect | Meaning | Smoking and lung cancer |
|---|---|---|
| Strength | The stronger the association, the harder it is to explain by unmeasured confounding | RR about 15, about 25 in heavy smokers (Example 13.7.1) |
| Consistency | Repeated in different populations, with different designs and by different investigators | Dozens of case-control and cohort studies, with consistent results in many countries |
| Specificity | One exposure corresponds to one outcome | Weak: smoking causes many diseases; this item is now rarely valued |
| Temporality | Exposure precedes outcome | Smoking status precedes the record of death in prospective cohorts |
| Biological gradient | Dose response | The more cigarettes and the more years of smoking, the higher the risk; risk falls after quitting |
| Plausibility | A biological mechanism exists | Carcinogens in tobacco smoke, DNA adducts |
| Coherence | Does not contradict the natural history of the disease or other knowledge | The rise of lung cancer in men lagged about 20 years behind the rise in cigarette consumption |
| Experimental evidence | Intervention changes the outcome | The risk of those who quit falls; animal experiments |
| Analogy | Similar exposures have similar effects | Other known inhaled carcinogens |

Hill himself stressed that these are "not hard-and-fast rules of evidence that must be obeyed, but viewpoints that help us answer one question: is there any other answer equally, or more, likely than cause and effect?" Only temporality is a necessary condition. The criteria do not replace statistics either: strength requires looking at the interval, consistency requires the synthesis of evidence (meta-analysis, [7.7.18](/7.7.18)), and whether unmeasured confounding could explain a strong association can be evaluated quantitatively (Cornfield's inequality and the E-value of [7.7.15](/7.7.15)).

## 13.8. Matched Designs

### 13.8.1. Matched Case-Control Studies

**Definition 13.8.1 (Matched Case-Control Study)** A case-control study in which, for each case, one or several controls are chosen who are the same as or close to the case in certain confounders (age, sex, residence), and the matching is preserved in the analysis, is called a **matched case-control study**. A 1:1 matching is called pair matching.

Matching makes the distribution of the matching factors the same in cases and controls, controlling confounding by these factors by design and raising efficiency when the matching factors are strongly related to the disease. The costs: the effect of the matching factors themselves can no longer be estimated; matching on a variable related to the exposure but not to the disease (overmatching) reduces efficiency; and the matching must be preserved in the analysis, otherwise (when the matching factors are related to the exposure) the OR is biased toward 1.

### 13.8.2. Analysis of Paired Data

The 1:1 matched data are arranged by "pair" in a 2×2 table:

| | Control exposed | Control unexposed |
|---|---|---|
| Case exposed | $u$ | $b$ |
| Case unexposed | $c$ | $v$ |

**Formula 13.8.1 (The Matched-Pair Odds Ratio)** Only discordant pairs give information about the association of exposure and disease. The matched-pair odds ratio is estimated by $\widehat{\mathrm{OR}} = b/c$ with $\operatorname{Var}(\ln\widehat{\mathrm{OR}}) \approx 1/b + 1/c$; the test of $\mathrm{OR} = 1$ is **McNemar's test** ([7.7.9](/7.7.9) Formula 9.3.1).

This is exactly the Mantel–Haenszel method with each pair as a stratum: each stratum has $n_i = 2$; concordant pairs contribute nothing to either numerator or denominator of $\widehat{\mathrm{OR}}_{\mathrm{MH}}$, pairs with the case exposed and the control unexposed contribute 1/2 to the numerator and the reverse pairs 1/2 to the denominator, so $\widehat{\mathrm{OR}}_{\mathrm{MH}} = b/c$ and the MH test reduces to McNemar's test. When the number of strata grows with the sample size and each stratum has only 2 people, the MH estimate remains consistent, while the unconditional maximum likelihood estimate that treats each pair as a stratum is biased to $(b/c)^2$; this is the starting point of the conditional logistic regression of [7.7.14](/7.7.14).

**Example 13.8.1 (A Worked Example)** Suppose that in a 1:1 matched study, among 200 pairs there are 30 with the case exposed and the control unexposed and 12 with the case unexposed and the control exposed (the numbers are made up for illustration). $\widehat{\mathrm{OR}} = 30/12 = 2.5$, $\operatorname{Var}(\ln\widehat{\mathrm{OR}}) = 1/30 + 1/12 = 0.117$, and the 95% interval is $\exp(0.916 \pm 1.96 \times 0.342) = (1.28, 4.88)$; McNemar's exact test gives $p = 0.008$. The remaining 158 pairs do not affect the conclusion, whether or not the exposure is common.

## 13.9. Computing in Python

```python
import numpy as np
from scipy import stats
from statsmodels.stats.contingency_tables import Table2x2, StratifiedTable

# RD, RR and OR with intervals (Example 13.2.1): rows exposed/unexposed, columns event/no event
phs = Table2x2(np.array([[139, 11037 - 139], [239, 11034 - 239]]))
print(phs.riskratio, phs.riskratio_confint())          # 0.581 (0.473, 0.715)
print(phs.oddsratio, phs.oddsratio_confint())          # 0.576 (0.467, 0.711), Woolf
rd = 139 / 11037 - 239 / 11034
print(rd, 1 / abs(rd))                                  # -0.0091, NNT 110

# Doll-Hill (Example 13.2.2): rows cases/controls, columns smoker/non-smoker
dh = Table2x2(np.array([[647, 2], [622, 27]]))
print(dh.oddsratio, dh.oddsratio_confint())            # 14.0 (3.3, 59.3)
print(stats.fisher_exact([[647, 2], [622, 27]]))       # p = 1.3e-6

# direct and indirect standardization (Examples 13.5.1 and 13.5.2)
d_s = np.array([32, 104, 206, 186, 102]); py_s = np.array([52407, 43248, 28612, 12663, 5317])
d_n = np.array([2, 12, 28, 28, 31]);      py_n = np.array([18790, 10673, 5710, 2585, 1462])
w = (py_s + py_n) / (py_s + py_n).sum()                 # standard population: both groups combined
print((w * d_s / py_s).sum() / (w * d_n / py_n).sum())  # standardized rate ratio 1.42
E = (d_n / py_n * py_s).sum()
print(d_s.sum() / E)                                    # SMR 630 / 444.4 = 1.42
T = py_s + py_n
print((d_s * py_n / T).sum() / (d_n * py_s / T).sum())  # Mantel-Haenszel rate ratio 1.42

# Mantel-Haenszel for stratified 2 x 2 tables (Example 13.6.1)
st = StratifiedTable([np.array([[120, 111], [80, 155]]), np.array([[161, 117], [130, 124]])])
print(st.oddsratio_pooled, st.oddsratio_pooled_confint())   # 1.63 (1.26, 2.09)
print(st.test_null_odds(correction=True))                    # X2 = 13.9, p = 0.0002
print(st.test_equal_odds())                                  # Breslow-Day 3.27, p = 0.07

# matched pairs (Example 13.8.1)
b, c = 30, 12
se = np.sqrt(1 / b + 1 / c)
print(b / c, np.exp(np.log(b / c) + np.array([-1.96, 1.96]) * se), stats.binomtest(b, b + c).pvalue)
```

In `Table2x2` the rows are the two groups and the columns are event and non-event, and `riskratio` is the first row against the second; for the table of a case-control study only `oddsratio` is meaningful.

## Summary

- The design determines what can be estimated (the table of Section 13.1.4): the **cohort study** (Definition 13.1.1) gives the risk of disease and RD, RR and rate ratios; the **case-control study** (Definition 13.1.2) samples by disease and can estimate only the OR (Theorem 13.2.1); the cross-sectional study estimates **prevalence**, and the ecological study compares only groups (Definition 13.1.3).
- Measures of effect (Definition 13.2.1):

  | Measure | Formula | No association | Variance of the logarithm (Formula 13.2.1) |
  |---|---|---|---|
  | RD | $p_1 - p_2$ | 0 | — |
  | RR | $p_1/p_2$ | 1 | $b/(an_1) + d/(cn_2)$ |
  | OR | $\frac{p_1/(1-p_1)}{p_2/(1-p_2)} = \frac{ad}{bc}$ | 1 | $1/a + 1/b + 1/c + 1/d$ |
  | Rate ratio | $I_1/I_2$ | 1 | $1/a + 1/c$ |

  For rare diseases OR ≈ RR; when the outcome is common the OR exaggerates the RR (birthwt: OR 2.02, RR 1.61).
- Measures for public health (Definitions 13.3.1, 13.3.2): $\mathrm{AF}_{\mathrm{e}} = (\mathrm{RR}-1)/\mathrm{RR}$, Levin's formula $\mathrm{PAF} = p_E(\mathrm{RR}-1)/[1 + p_E(\mathrm{RR}-1)]$, and $\mathrm{NNT} = 1/\lvert\mathrm{RD}\rvert$. Aspirin RR 0.58, NNT 110 (Example 13.3.2); about 93% of lung cancer in smokers is attributable to smoking (Example 13.3.1).
- Bias (Definition 13.4.1): selection bias, information bias (nondifferential misclassification tends toward the null; recall bias has an uncertain direction), and **confounding** (Definition 13.5.1). A large sample reduces only random error.
- Handling confounding: direct and indirect standardization (Definition 13.5.2), the Mantel–Haenszel pooled estimate and test (Formula 13.6.1), matching (Definition 13.8.1; matched-pair OR $= b/c$, Formula 13.8.1) and regression ([7.7.14](/7.7.14)). The crude rate ratio 1.72 for coronary deaths among British doctors falls to 1.42 after age standardization (Example 13.5.2); the passive-smoking $\mathrm{OR}_{\mathrm{MH}} = 1.63$ (Example 13.6.1).
- **Effect modification** (Definition 13.6.1) depends on scale, is detected by a test of homogeneity (Formula 13.6.2), and is reported by stratum without combining; the coronary rate ratio falls from 5.7 (ages 35–44) to 0.9 (ages 75–84).
- Judging causation: dose response (lung cancer rate ratios 7.7, 13.7, 24.5, Example 13.7.1) and the **Bradford Hill criteria** (Definition 13.7.1); only temporality is necessary, and the rest are viewpoints for weighing the evidence.

## Questions

1. State the design of each of the following studies and which measures of effect it can estimate: (a) 300 pancreatic cancer patients are identified from a cancer registry and 600 residents of the same region are drawn at random and asked about their past drinking habits; (b) the full employee roster of a chemical plant for 1970–1990 is retrieved, the employees are grouped by whether they worked in the benzene workshop, and followed to 2020 for leukemia; (c) per capita salt intake and stroke mortality of 30 countries are compared; (d) 5000 adults are drawn at random in a city and blood pressure and use of oral contraceptives are measured at the same time.

   **Answer** (a) A case-control study, which can estimate only the OR (pancreatic cancer is rare, so the OR approximates the RR). (b) A retrospective (historical) cohort study: exposure status is determined from past records and the outcome occurs afterward; it can estimate incidence rates, rate ratios, RD and RR (with person-time when follow-up times differ). (c) An ecological study, which gives only a correlation at the country level that cannot be carried over to individuals. (d) A cross-sectional study, estimating the prevalence of hypertension and the ratio of prevalences (or OR); because measurement is simultaneous, the temporal order of drug use and hypertension cannot be established (people with hypertension may already have been advised to stop the drug).

2. A cohort study follows 5000 current smoking women and 5000 never-smoking women for 10 years, with 13 and 4 new cases of lung cancer respectively (the numbers are made up for illustration). Find RR, RD, OR and the 95% interval of RR, and explain why OR and RR are almost the same.

   **Answer** $\hat p_1 = 13/5000 = 0.0026$ and $\hat p_2 = 4/5000 = 0.0008$. $\mathrm{RR} = 3.25$, $\mathrm{RD} = 0.0018$ (1.8 extra cases per 1000 persons in 10 years), and $\mathrm{OR} = (13 \times 4996)/(4 \times 4987) = 3.256$. $\operatorname{Var}(\ln\mathrm{RR}) = 4987/(13 \times 5000) + 4996/(4 \times 5000) = 0.0767 + 0.2498 = 0.3265$, the standard error is 0.571, and the 95% interval is $\exp(1.179 \pm 1.120) = (1.06, 9.96)$. Both risks are far below 1%, $(1 - p_2)/(1 - p_1) = 0.9992/0.9974 \approx 1.002$, so OR ≈ RR. There are few cases and the interval is very wide.

3. Prove that, in a case-control study with sampling proportion $f_1$ for cases and $f_0$ for controls, sampling being independent of exposure, the expected value of the table's "proportion of cases among the exposed" $a/(a + c)$ ($a$ exposed cases, $c$ exposed controls) depends on $f_1/f_0$ whereas $ad/(bc)$ does not.

   **Answer** Let the numbers of exposed cases and non-cases in the population be $A$ and $C$, and for the unexposed $B$ and $D$. After sampling, $\mathbb{E}(a) = f_1 A$, $\mathbb{E}(c) = f_0 C$, $\mathbb{E}(b) = f_1 B$ and $\mathbb{E}(d) = f_0 D$. Thus $a/(a + c) \approx f_1A/(f_1A + f_0C)$ varies with $f_1/f_0$: the more cases are sampled, the higher the "risk", and it is not the risk $A/(A + C)$ of the exposed in the population. But $ad/(bc) \approx f_1Af_0D/(f_1Bf_0C) = AD/(BC)$, in which $f_1 f_0$ cancels, and this is the OR of the population (Theorem 13.2.1).

4. In Levin's formula, if RR = 2, what is the PAF for prevalences of exposure $p_E$ of 5%, 30% and 60%? What if RR = 20 and $p_E = 1\%$? Explain from this how priorities in public health should be considered.

   **Answer** $\mathrm{PAF} = p_E(\mathrm{RR} - 1)/[1 + p_E(\mathrm{RR} - 1)]$. With RR = 2: for $p_E = 0.05$, $0.05/1.05 = 4.8\%$; for 0.30, $0.3/1.3 = 23\%$; for 0.60, $0.6/1.6 = 37.5\%$. With RR = 20 and $p_E = 0.01$: $0.19/1.19 = 16\%$. A factor that merely doubles risk but to which six in ten people are exposed causes more than twice the fraction of cases of a factor with RR 20 to which only 1% are exposed. The benefit of prevention depends on the PAF (and on the feasibility and cost of intervention), not on the size of RR alone; this presupposes that the association is causal and that removing the exposure would bring the risk down to that of the unexposed.

5. In a randomized trial a drug lowers the 5-year risk of stroke from 4% to 3% and at the same time raises serious bleeding from 0.5% to 1.5%. Find RR, NNT and NNH, and discuss whether the drug should be recommended in a low-risk population with a baseline stroke risk of 1% (assume RR and the bleeding risk are unchanged).

   **Answer** Stroke: RR = 0.75, RD = −1%, NNT = 100. Bleeding: RD = +1%, NNH = 100. In the original population, treating 100 people avoids 1 stroke and causes 1 more serious bleed, and the net benefit depends on the seriousness of the two events. In the low-risk population the stroke risk goes from 1% to 0.75%, RD = −0.25%, NNT = 400, while NNH is still 100: for each stroke avoided, 4 more serious bleeds are caused, and the drug should not be recommended. The same RR means completely different absolute benefits at different baseline risks, which is the danger of looking only at RR; clinical decisions require absolute risks.

6. Using the data of Example 13.5.1: (a) take the person-year composition of the smokers as the standard population and compute the directly standardized rates and rate ratio of the two groups; (b) explain why this result differs from the one with the combined person-years as standard (1.42), and what the difference shows.

   **Answer** (a) The person-year composition of the smokers is 0.368, 0.304, 0.201, 0.089, 0.037. The standardized rate of smokers is their crude rate 443; for nonsmokers it is $0.368 \times 10.6 + 0.304 \times 112.4 + 0.201 \times 490.4 + 0.089 \times 1083.2 + 0.037 \times 2120.4 = 3.9 + 34.2 + 98.6 + 96.4 + 79.3 = 312$ (per 100 000 person-years), and the rate ratio is $443/312 = 1.42$; this is in fact the SMR of Example 13.5.2, both being weighted by the age composition of the smokers and computed as $630/444.4$. (b) Here it happens to be close to the combined standard (both 1.42), because the two sets of weights differ little. In general, when the rate ratios of the strata differ (effect modification), the standardized rate ratio depends on the weights: more weight on the young strata makes the rate ratio larger (5.7 at ages 35–44), and more weight on the old strata makes it smaller. That the value of the standardized rate ratio depends on the standard population is precisely why one should report by stratum in this case.

7. Prove that the Mantel–Haenszel odds ratio of 1:1 matched data equals $b/c$.

   **Answer** Each pair is a stratum with $n_i = 2$, and the four cells of the stratum's 2×2 table (exposed case, unexposed case, exposed control, unexposed control) are each 0 or 1. $a_i d_i/n_i$ is nonzero if and only if the case is exposed ($a_i = 1$) and the control unexposed ($d_i = 1$), in which case it equals 1/2; there are $b$ such pairs. $b_i c_i/n_i$ is nonzero if and only if the case is unexposed and the control exposed, and equals 1/2; there are $c$ such pairs. In a pair in which both are exposed, $a_i = c_i = 1$ and $b_i = d_i = 0$, so both terms are 0; likewise for pairs in which neither is exposed. Hence $\widehat{\mathrm{OR}}_{\mathrm{MH}} = (b/2)/(c/2) = b/c$.

8. One study finds that the ORs for an exposure and a disease in two age strata are 3.0 and 3.2, and the crude OR of the pooled table is 1.4. In another study the ORs in the two strata are 1.0 and 4.0 and the crude OR is 2.4. State for each study whether age is a confounder or an effect modifier, and how the results should be reported.

   **Answer** The first: the stratum ORs are similar (3.0, 3.2), indicating no marked effect modification; the crude OR (1.4) differs greatly from the stratum ORs, indicating that age is a confounder (exposure is related to age and age to disease). The adjusted pooled estimate (MH OR about 3.1) and its interval should be reported. The second: the stratum ORs differ greatly (1.0 against 4.0), and age is an effect modifier: the exposure has an effect in only one age stratum. A single pooled OR should not be reported; the two ORs should be reported by stratum and the difference evaluated by a homogeneity test or an interaction term (whether age is also a confounder depends on whether the stratum estimates differ from the estimate pooled by some weighting, but pooling itself has limited meaning here).

9. The controls of the 1950 Doll–Hill study were non-lung-cancer inpatients of the same hospitals. (a) If a considerable proportion of the controls were patients with other smoking-related diseases (such as chronic bronchitis and coronary heart disease), would the OR be biased upward or downward? (b) The smoking history was elicited by interviewers who knew whether the respondent was a case or a control; what bias might this produce? (c) Why is it unlikely that these biases explain an OR of 14?

   **Answer** (a) The proportion of smokers among the controls is raised, close to that of the cases, and the OR is biased toward 1 (underestimated); this is selection bias in the direction that makes the true effect larger. (b) Interviewers who know the diagnosis may probe the smoking history of the cases more deeply, causing differential information bias and an upward bias of the OR. Doll and Hill checked this: the "cases" who were later found not to have lung cancer (misdiagnosed on admission) had smoking habits like the controls and not like the lung cancer cases, showing that the interviewing itself did not make the cases' smoking histories higher. (c) To explain a 14-fold association entirely by bias would need a bias of unbelievable size; the prospective cohort that followed (smoking history recorded before disease, with no recall or interviewer bias) obtained a similar rate ratio of 14.6 (Example 13.7.1), together with a clear dose response.

10. (Design question) You want to study whether taking a certain antidepressant in pregnancy increases the risk of congenital heart malformations in the newborn. The incidence of the malformation is about 1%, and about 3% of pregnant women take the drug. Compare the feasibility of a cohort design and a case-control design, and point out the main risks of bias and remedies for each.

    **Answer** Main points: (1) Cohort: if the true RR is 2, enough cases must be observed among those who take the drug. The exposed have about 20 cases per 1000 and the unexposed 10, so each group needs thousands of pregnant women taking the drug (on the order of thousands of pairs to test RR = 2); a retrospective cohort can be formed from a large birth registry or an insurance database, with exposure determined from prescription records, avoiding recall bias. Main biases: confounding (depression itself, smoking, drinking, age and other drugs), handled by propensity scores or regression ([7.7.15](/7.7.15)), and by comparison with "women who stopped the drug before pregnancy" to control confounding by indication; a prescription is not the same as actual use (nondifferential misclassification). (2) Case-control: take cases from a malformation registry and normal newborns of the same period as controls; this is efficient and suits rare outcomes; the main risk is recall bias (mothers of malformed infants are more likely to report drug use), and the remedies are to determine exposure from medical or pharmacy records and to use infants with other malformations as controls (their mothers have gone through the same psychological process of "searching for causes"). (3) Both need a clearly defined exposure window (early pregnancy is the period of heart development) and a diagnostic criterion for the malformation defined beforehand.

11. A study compares the risk of disease in exposed and unexposed people in three age strata: 2% against 1% in stratum 1, 10% against 5% in stratum 2, and 30% against 15% in stratum 3. Is there effect modification on the multiplicative scale and on the additive scale? What does this imply for health policy?

    **Answer** RR is 2 in all three strata, so there is no effect modification on the multiplicative scale; RD is 1%, 5% and 15%, so there is strong effect modification on the additive scale. If an intervention could eliminate the effect of the exposure, in stratum 3 15 cases would be avoided per 100 people intervened and in stratum 1 only 1: when resources are limited, intervening first in the population with high baseline risk yields the greatest benefit. Biological "interaction" (whether two factors act together on the same mechanism) usually corresponds to a departure on the additive scale; testing only on the multiplicative scale (OR, RR, the interaction term of logistic regression) may miss the modification most important to public health.
