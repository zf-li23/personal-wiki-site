---
title: Clinical Trials, Sample Size and Meta-Analysis
description: Phases and designs of randomized controlled trials (parallel, factorial, crossover, cluster randomized); primary and surrogate endpoints; intention-to-treat and per-protocol analysis; superiority, non-inferiority and equivalence, margins and two one-sided tests; a unified sample-size formula with corrections for dropout, noncompliance and clustering; interim analyses, O'Brien–Fleming and Pocock boundaries and alpha spending functions; pitfalls of multiple endpoints and subgroup analyses; lead-time bias, length bias and overdiagnosis in screening trials; fixed-effect and random-effects meta-analysis, heterogeneity Q and I-squared, forest plots, cumulative meta-analysis, funnel plots and publication bias; preregistration and reporting guidelines. Illustrated by the Physicians' Health Study, the aspirin primary prevention trials, the NLST and the veteran trial.
source_hash: ecda93c5cd93
---

Randomization ([7.7.5](/7.7.5)) makes the treated and control groups comparable with respect to both known and unknown factors and is the most reliable source of causal conclusions ([7.7.15](/7.7.15) Theorem 15.3.1). But whether a randomized trial can answer its question also depends on many statistical decisions: which endpoint to compare, on whom to base the analysis, how many people are needed, whether the data may be looked at midway and the trial stopped early, how to test that "the new drug is not worse than the old one", and whether a positive result among dozens of subgroups should be believed. Once a single trial has answered, a second-level question follows: how should evidence be combined when several trials disagree? This chapter follows thread 2: [7.7.3](/7.7.3) Example 3.1.4, [7.7.5](/7.7.5) Example 5.2.1 and [7.7.13](/7.7.13) Example 13.2.1 have already computed from the Physicians' Health Study (PHS) an RR of 0.58 and an NNT of 110 for aspirin; here we first use it to discuss sample size and early stopping, and then use seven primary prevention trials from 1998–2018 for a meta-analysis to see how the evidence is updated by new trials. The sample-size formulas given separately in earlier chapters ([7.7.6](/7.7.6), [7.7.7](/7.7.7), [7.7.9](/7.7.9), [7.7.16](/7.7.16)) are unified in Section 18.4; the biases of screening are illustrated with the NLST of thread 3; the veteran trial ([7.7.16](/7.7.16)) serves as an example for intention-to-treat analysis and power.

## 18.1. Design of Clinical Trials

### 18.1.1. Phases

**Definition 18.1.1 (Randomized Controlled Trial)** A prospective study in which eligible participants are allocated by a random mechanism to the experimental treatment or to a control (placebo, standard treatment), and the groups are compared on a prespecified endpoint, is called a **randomized controlled trial** (RCT).

The clinical development of a new drug is usually divided into four phases:

| Phase | Participants | Main question | Typical size and design |
|---|---|---|---|
| I | Healthy volunteers (patients for cancer drugs) | Safety, tolerated dose, pharmacokinetics | Tens of people; dose escalation (such as the 3 + 3 design) |
| II | Target patients | Signal of efficacy, dose selection | Tens to hundreds of people; single-arm or randomized, often with a surrogate endpoint |
| III | Target patients | Confirming efficacy and safety | Hundreds to tens of thousands of people; randomized controlled, clinical endpoints |
| IV | Post-marketing population | Rare adverse reactions, long-term effects, real-world use | Observational studies, registries, large simple trials |

Dose escalation in phase I and single-arm designs in phase II can be analyzed with the one-sample methods of [7.7.6](/7.7.6); this chapter focuses on the confirmatory phase III trial.

### 18.1.2. Types of Design

- Parallel design: each person receives only one treatment; the most common.
- **Factorial design** ([7.7.12](/7.7.12) Definition 12.7.2): PHS used a 2×2 factorial design to test aspirin and β-carotene at the same time ([7.7.5](/7.7.5) Example 5.2.1), the two questions sharing 22,071 people; the prerequisite is that the two treatments have no marked interaction.
- Crossover design ([7.7.17](/7.7.17) Definition 17.6.1): each person receives two treatments in sequence; suitable for chronic, stable and reversible conditions.
- Cluster randomized design: the unit of randomization is the clinic, school or village; suitable for interventions aimed at groups (health education, care processes) or for preventing "contamination" between groups; the analysis and sample size must take into account the design effect ([7.7.17](/7.7.17) Definition 17.7.1).
- Adaptive designs: according to prespecified rules, the sample size is modified on the basis of interim data, ineffective arms are dropped or the allocation ratios adjusted; platform trials (such as the RECOVERY trial in the UK during the COVID-19 pandemic) compare several treatments simultaneously or in sequence within one framework.

## 18.2. Endpoints and Analysis Populations

### 18.2.1. Primary and Surrogate Endpoints

Each confirmatory trial should prespecify a single primary endpoint: the sample size is calculated for it and the conclusion is based on it. The endpoint should be meaningful to patients (death, myocardial infarction, stroke, function, quality of life). Measuring these endpoints directly requires many people and long follow-up, so earlier, more easily measured biomarkers are often used as substitutes.

**Definition 18.2.1 (Surrogate Endpoint)** A laboratory measurement or sign that is used in place of a clinical endpoint (blood pressure, LDL cholesterol, HbA1c, tumor shrinkage, viral load) is called a **surrogate endpoint**. A valid surrogate endpoint requires that the effect of treatment on the surrogate reliably predict its effect on the clinical endpoint.

It is not enough that "the surrogate is correlated with the clinical endpoint". The classic counterexample is the Cardiac Arrhythmia Suppression Trial (CAST, 1989–1991): ventricular premature beats after myocardial infarction are a strong predictor of sudden death, and the antiarrhythmic drugs encainide and flecainide suppressed the premature beats effectively but raised mortality, and the trial was therefore stopped early. A drug may affect the outcome through pathways other than the surrogate, and the surrogate may not be on the causal pathway. Viral load for HIV antiviral treatment and blood pressure for antihypertensives are surrogates validated by many trials; the prediction of overall survival by tumor shrinkage varies by drug.

### 18.2.2. Intention-to-Treat Analysis

After randomization there are always people who do not receive the treatment as assigned: they stop the drug, switch to the drug of the control group, or are lost to follow-up.

**Definition 18.2.2 (Intention-to-Treat and Per-Protocol Analysis)** Analyzing all randomized participants according to the group to which they were randomly assigned, regardless of what treatment they actually received and whether they completed the trial, is called **intention-to-treat analysis** (ITT); analyzing only the participants who received the assigned treatment per protocol without major protocol violations is called **per-protocol analysis**.

ITT preserves randomization: the two groups compared are comparable at baseline, and differences can come only from the assignment itself. The people removed in a per-protocol analysis are not random: those who stop the drug because they cannot tolerate it, or change treatment because their disease worsens, often have a different prognosis; it reintroduces confounding. ITT estimates the effect of "being assigned to this treatment", the effect of the strategy under actual adherence, and usually underestimates the effect of "actually taking" it; when the interest is in the effect of actually taking the treatment, use random assignment as an instrumental variable ([7.7.15](/7.7.15) Definition 15.7.1) rather than simply excluding the nonadherent. The log-rank test of the veteran trial ([7.7.16](/7.7.16) Example 16.6.1) is an ITT analysis: all 137 patients are analyzed according to the chemotherapy assigned.

In a superiority trial, noncompliance brings the two groups closer and the ITT conclusion is conservative; in a non-inferiority trial (Section 18.3) the same bias makes it easier for "not worse than the control" to hold, so a non-inferiority trial should report both the ITT and the per-protocol analysis, and the conclusion is credible only if the two agree.

## 18.3. Superiority, Non-Inferiority and Equivalence

When an effective standard treatment already exists, a placebo control is often unethical. The value of a new treatment may lie in being safer, cheaper or more convenient (oral instead of injection), as long as its efficacy is "not much worse than the standard".

**Definition 18.3.1 (Non-Inferiority and Equivalence Trials)** Let $\Delta$ be the difference in effect between the new and the standard treatment (in terms of the risk of an adverse outcome, a positive value meaning that the new treatment is worse), and $M > 0$ a prespecified margin. A trial that tests

$$
H_0\colon \Delta \ge M \quad \text{vs} \quad H_1\colon \Delta < M
$$
is called a **non-inferiority trial**; a trial that tests $H_0\colon \lvert\Delta\rvert \ge M$ vs $H_1\colon \lvert\Delta\rvert < M$ is called an **equivalence trial**.

The conclusion of non-inferiority is equivalent to the upper limit of the two-sided 95% confidence interval of $\Delta$ being less than $M$ (corresponding to a one-sided test with $\alpha = 0.025$). The choice of margin is a clinical judgment, not a statistical problem, and it usually does not exceed half of the known effect of the standard treatment relative to placebo, to ensure that the new treatment retains at least half of the efficacy of the standard treatment. The conclusion of a non-inferiority trial depends on an assumption that cannot be tested within the trial: that the effect of the standard treatment in this trial is the same as in the historical placebo-controlled trials (the "constancy assumption").

**Definition 18.3.2 (Two One-Sided Tests)** The test of equivalence is decomposed into two one-sided tests at level $\alpha$: $H_{01}\colon \Delta \le -M$ and $H_{02}\colon \Delta \ge M$; equivalence is concluded when both are rejected. This method is called the **two one-sided tests** (TOST) procedure. It is equivalent to the $100(1 - 2\alpha)\%$ confidence interval of $\Delta$ lying entirely within $(-M, M)$.

**Example 18.3.1 (Non-Inferiority, a Worked Example)** A new oral anticoagulant is compared with the standard treatment for the 2-year risk of stroke, with margin $M = 1$ percentage point. With 5000 people per group, stroke occurs in 2.3% versus 2.1% (the numbers are made up for illustration). The difference is 0.2 percentage points with standard error 0.293 and 95% interval $(-0.37, 0.77)$; the upper limit is less than 1, so non-inferiority is concluded; the $z$ for testing $H_0\colon \Delta \ge 1$ is $(0.2 - 1)/0.293 = -2.73$, with one-sided $p = 0.003$. The interval also contains 0, so we cannot say that the new drug is better or worse.

**Example 18.3.2 (Bioequivalence, a Worked Example)** A generic drug and the original drug are compared on AUC in a crossover trial of 24 subjects. The regulatory criterion is that the 90% interval of the geometric mean ratio lie within 0.80–1.25 (TOST on the log scale, $\alpha = 0.05$, $M = \ln 1.25$). Suppose the difference on the log scale is $\ln 0.95 = -0.051$ with standard error 0.040 and 22 degrees of freedom: the 90% interval $\exp(-0.051 \pm 1.717 \times 0.040) = (0.887, 1.018)$ is within 0.80–1.25, the $p$-values of the two one-sided tests are 0.0001 and $3 \times 10^{-7}$, and bioequivalence is concluded.

![Reading superiority, non-inferiority and equivalence from confidence intervals (schematic). Each line is the confidence interval of the difference in the risk of an adverse outcome, new treatment minus standard treatment (negative values favor the new treatment); $M$ is the non-inferiority margin and $\pm M$ the equivalence margins. On the right are the conclusions for each interval: an interval entirely below 0 is superiority; an upper limit below $M$ is non-inferiority (even if the interval is entirely above 0, being "significantly worse" but not by much can still be judged non-inferior); an interval that crosses $M$ is inconclusive; one entirely above $M$ is inferiority. Equivalence requires the interval (the 90% interval for TOST) to lie entirely within $\pm M$](./plots/noninferiority.py)

"Not significant" is not the same as equivalent: a $p = 0.4$ in a small trial says only that the interval is wide. To claim "no difference", one must prespecify a margin and calculate the sample size under a non-inferiority or equivalence design.

## 18.4. Sample Size

### 18.4.1. A Unified Formula

The sample-size formulas of the earlier chapters ([7.7.6](/7.7.6) Formula 6.4.2, [7.7.7](/7.7.7) Formula 7.6.1, [7.7.9](/7.7.9) Formula 9.4.1, [7.7.16](/7.7.16) Formula 16.10.1) all come from the same argument.

**Formula 18.4.1 (General Form of the Sample Size)** Suppose the estimator $\hat\theta$ of the effect is approximately normal with variance that can be written $v/n$ ($n$ is the number of people or events per group, and $v$ the "variance per unit"). The number needed for a two-sided level-$\alpha$ test to detect $\theta = \delta$ with power $1 - \beta$ is

$$
n = \frac{(z_{\alpha/2} + z_\beta)^2\, v}{\delta^2}.
$$

**Proof** The rejection region is $\lvert\hat\theta\rvert > z_{\alpha/2}\sqrt{v/n}$. Under $\theta = \delta > 0$, ignoring the tiny probability on the other side, the power is $\mathbb{P}(\hat\theta > z_{\alpha/2}\sqrt{v/n}) = \Phi\bigl(\delta\sqrt{n/v} - z_{\alpha/2}\bigr)$. Setting it equal to $1 - \beta$ gives $\delta\sqrt{n/v} - z_{\alpha/2} = z_\beta$, and solving for $n$ gives the result. $\square$

| Comparison | $\theta$ | $v$ | Source |
|---|---|---|---|
| Two means | $\mu_1 - \mu_2$ | $2\sigma^2$ | [7.7.7](/7.7.7) Formula 7.6.1 |
| Paired | Mean difference | $\sigma_d^2 = 2\sigma^2(1 - \rho)$ | [7.7.7](/7.7.7) Formula 7.6.2 |
| Two proportions | $p_1 - p_2$ | $\approx p_1q_1 + p_2q_2$ (under the null hypothesis $2\bar p\bar q$) | [7.7.9](/7.7.9) Formula 9.4.1 |
| Survival (number of events) | $\ln\mathrm{HR}$ | 4 ($n$ is the total number of events) | [7.7.16](/7.7.16) Formula 16.10.1 |
| Non-inferiority (proportions) | $p_1 - p_2 - M$ | $p_1q_1 + p_2q_2$, with $z_{\alpha/2}$ replaced by the one-sided $z_\alpha$ | Definition 18.3.1 |

For $\alpha = 0.05$, $(z_{\alpha/2} + z_\beta)^2$ is 7.85 for 80% power and 10.51 for 90% power. Four quantities determine the sample size: the smaller the effect, the larger the variability, the smaller the required $\alpha$ and the higher the power, the more people are needed; the sample size is inversely proportional to the square of the effect, and halving the effect to be detected multiplies the number of people by 4.

### 18.4.2. The Size of the Physicians' Health Study

**Example 18.4.1** When the 5-year cumulative incidence of myocardial infarction is about 2.2%, detecting a 25% relative reduction by aspirin (to 1.65%) with two-sided $\alpha = 0.05$ and 80% power needs about 9800 people per group ([7.7.9](/7.7.9) Example 9.4.1), and 90% power needs 13,100. PHS had about 11,000 per group, giving a power of about 0.84 for this effect. In retrospect, the actual effect of aspirin was larger (2.17% → 1.26%, a relative reduction of 42%): had this been known beforehand, 3200 per group would have given 80% power. This is exactly the dilemma of design: the sample size should be calculated for "the smallest clinically meaningful effect" rather than an optimistic guess, otherwise the trial fails when the true effect is slightly smaller.

### 18.4.3. Corrections

**Formula 18.4.2 (Corrections to the Sample Size)** (1) With an expected proportion lost to follow-up $L$ (the outcomes of those lost cannot be observed): $n' = n/(1 - L)$. (2) Noncompliance: a proportion $d_{\mathrm{in}}$ of the control group uses the study drug on their own, and a proportion $d_{\mathrm{out}}$ of the treatment group stops the drug; under ITT the effect is diluted to $(1 - d_{\mathrm{in}} - d_{\mathrm{out}})\delta$, and the number needed is $n' = n/(1 - d_{\mathrm{in}} - d_{\mathrm{out}})^2$. (3) A cluster randomized design with $m$ people per cluster and intraclass correlation $\rho$: $n' = n[1 + (m - 1)\rho]$.

Noncompliance has the greatest impact because the dilution of the effect enters the sample size as a square: a total of 20% noncompliance raises the number needed to $1/0.8^2 = 1.56$ times. The 9800 people in Example 18.4.1 become 15,300 per group with 20% noncompliance; with cluster randomization of 100 people per clinic and $\rho = 0.02$, this must be multiplied by a further 2.98.

## 18.5. Interim Analysis and Early Stopping

### 18.5.1. Why Adjustment Is Needed

A long-term trial needs monitoring: if the treatment is clearly effective, clearly harmful or clearly hopeless, it is unethical to keep half the people on the inferior treatment. An independent data monitoring committee periodically looks at the unblinded data. The problem is that looking many times means testing many times: if $\lvert z\rvert > 1.96$ is used at each of 5 equally spaced analyses, the overall type I error rate reaches 0.14 even if the treatment is ineffective (figure below).

**Definition 18.5.1 (Interim Analysis and Group Sequential Design)** An analysis of accumulating data carried out before the trial is complete, at prespecified fractions of the information (the proportion $t$ of the planned number of events observed), is called an **interim analysis**. A design that prespecifies that the trial is stopped if the test statistic $\lvert Z_k\rvert$ exceeds a boundary $b_k$ at the $k$th analysis, and makes the total probability of "crossing at any analysis" under the null hypothesis equal to $\alpha$, is called a group sequential design.

The $Z_k$ at different times are correlated (the later data contain the earlier), $\operatorname{Corr}(Z_j, Z_k) = \sqrt{t_j/t_k}$, and the probability of crossing is obtained by integrating over their joint normal distribution. Two commonly used boundaries:

| Design | Boundary $b_k$ | 5 analyses, overall $\alpha = 0.05$ | Features |
|---|---|---|---|
| Pocock | Constant $c$ | 2.41 each time (nominal $p = 0.016$) | Easy to stop early; the boundary at the final analysis is high, with a large loss of overall power |
| O'Brien–Fleming | $c/\sqrt{t_k}$ | 4.56, 3.23, 2.63, 2.28, 2.04 (nominal $p = 5 \times 10^{-6}$ to 0.041) | Extremely hard to stop early; the final analysis is hardly affected |

A fixed-sample trial designed with 90% power, with 5 O'Brien–Fleming analyses added, has its power reduced to 0.89 and the average information needed is 74% of the fixed design; with Pocock boundaries the power falls to 0.83 and the average information is 62%. The O'Brien–Fleming boundary is the most commonly used: early data are few and the estimate unstable, so only overwhelming evidence should stop the trial, and it hardly affects the final analysis.

### 18.5.2. The Alpha Spending Function

A group sequential design requires the number and timing of analyses to be fixed in advance. Lan and DeMets (1983) turned the problem into "how much of $\alpha$ is allowed to be spent up to the information fraction $t$".

**Definition 18.5.2 (Alpha Spending Function)** A function $\alpha^*(t)$ on $[0, 1]$ that is nondecreasing with $\alpha^*(0) = 0$ and $\alpha^*(1) = \alpha$ is called an **alpha spending function**. At the $k$th analysis, performed at information fraction $t_k$, the boundary $b_k$ is chosen so that, under the null hypothesis, the probability of "not crossing in the first $k - 1$ analyses and crossing at the $k$th" is exactly $\alpha^*(t_k) - \alpha^*(t_{k-1})$.

The function $\alpha^*(t) = 2 - 2\Phi(z_{\alpha/2}/\sqrt t)$ approximates the O'Brien–Fleming boundary, and $\alpha^*(t) = \alpha\ln[1 + (\mathrm{e} - 1)t]$ approximates the Pocock boundary. The number and timing of analyses can be changed during the trial (the dates of committee meetings are hard to fix in advance) as long as the spending function is prespecified. With 5 equally spaced analyses, the O'Brien–Fleming-type spending function gives boundaries of 4.39, 3.10, 2.56, 2.25 and 2.06, very close to the classical O'Brien–Fleming boundaries.

![Group sequential boundaries for 5 equally spaced analyses with overall two-sided $\alpha = 0.05$ (obtained by numerical integration over the joint distribution of the interim test statistics). A: boundaries of the Pocock design (constant boundary), the O'Brien–Fleming design ($c/\sqrt t$) and the O'Brien–Fleming-type Lan–DeMets spending function; the dashed line is the unadjusted 1.96, which gives an overall type I error rate of about 0.14 if used at every analysis. B: type I error cumulatively spent by each design as a function of the information fraction (the legend applies to both panels)](./plots/group-sequential.py)

### 18.5.3. The Cost of Early Stopping

**Example 18.5.1** The aspirin component of PHS was stopped early on the recommendation of the data monitoring committee (preliminary results published in early 1988): the reduction in myocardial infarction was already very clear, and another objective of the trial, cardiovascular death, had too few events in this low-risk population of physicians to be answered even under the original plan (the final report gave an RR of 0.96 for cardiovascular death, 95% interval 0.60–1.54).

A trial stopped early for benefit has two statistical consequences. First, the effect estimate is too large: the trial crosses the boundary just when random fluctuation makes the effect look large, and on average overestimates the true effect (trials stopped early overestimate the most). Second, there is less information on secondary endpoints and safety: the conclusions of PHS on stroke and bleeding are therefore uncertain (RR 2.14 for hemorrhagic stroke, interval 0.96–4.77). The decision of a monitoring committee looks not only at boundaries but also at safety, external evidence and the implications of the conclusion for practice; the boundary is a guide, not a mechanical rule.

## 18.6. Multiplicity

A trial usually has one primary endpoint but reports dozens of secondary endpoints, several time points, several analysis populations and many subgroups. Without control, 1 in every 20 null comparisons will on average give $p < 0.05$.

- Several primary endpoints or dose groups: use **Holm's method** ([7.7.12](/7.7.12) Definition 12.3.1), fixed-sequence testing ordered by importance (test the next only if the previous is significant), or combine several endpoints into one composite endpoint.
- Interim analyses: Section 18.5.
- Subgroup analyses: the most misleading kind.

**Example 18.6.1 (Subgroups)** The ISIS-2 trial (1988) showed that aspirin lowers mortality after myocardial infarction; to illustrate the danger of subgroup analysis, the authors grouped the patients by astrological sign and found that patients born under Gemini and Libra had slightly higher mortality on aspirin. PHS reported that the reduction in myocardial infarction was seen only in those aged 50 or older, and WHS reported that aspirin significantly reduced major cardiovascular events and myocardial infarction in women aged 65 or older, while in all women neither was significant. These subgroup results may be real (the baseline risk is higher in older people, so the same RR gives a larger absolute benefit, [7.7.13](/7.7.13) Section 13.3.2) or they may be due to chance.

Requirements for subgroup conclusions: (1) prespecified and few in number; (2) based on a test of interaction (whether the effects differ between subgroups, [7.7.13](/7.7.13) Formula 13.6.2), not on "$p < 0.05$ in this subgroup and $p > 0.05$ in that one", since one subgroup being significant and another not may simply be because the latter has fewer people; (3) biologically plausible in direction and size, and replicated in other trials. If the true effect is the same in all subgroups, the probability that at least one of 10 subgroups is "significantly different" is about $1 - 0.95^{10} = 0.40$.

## 18.7. Biases Specific to Screening Trials

The goal of screening is to detect disease before symptoms appear so that treatment is more effective. Evaluating screening involves three biases that arise only here, all of which make the cases found by screening look to have a better prognosis even if screening does nothing.

**Definition 18.7.1 (Lead-Time Bias, Length Bias and Overdiagnosis)** Screening brings the time of diagnosis forward without changing the time of death, lengthening the "survival time from diagnosis"; this is called **lead-time bias**, and the time by which diagnosis is advanced is called the lead time. Cases that progress slowly and have a long detectable preclinical phase are more likely to be found by screening, so that the proportion with a good prognosis among the cases found by screening is too high; this is called **length bias**. Screening that finds lesions which, without screening, would never have caused symptoms or death in the person's lifetime is called **overdiagnosis**.

The common lesson of the three is that screening cannot be evaluated by comparing the survival of screen-detected and symptom-detected cases, nor by the "5-year survival" rising as screening becomes widespread: the 5-year survival of prostate cancer rose sharply after PSA screening became common, largely because of lead time and overdiagnosis. The correct endpoint is the disease mortality of all those screened (ITT) in a randomized trial, which is unaffected by these three biases.

**Example 18.7.1 (NLST)** The NLST randomly assigned 53,454 heavy smokers to 3 annual rounds of low-dose CT or chest radiography. At a median follow-up of 6.5 years, 1060 lung cancers had been diagnosed in the CT group and 941 in the chest radiography group (rate ratio 1.13, 95% interval 1.03–1.23), and lung cancer mortality was reduced by 20% ([7.7.16](/7.7.16) Example 16.1.1). Of the 119 extra diagnoses, some are lead time (these cancers would also have been diagnosed later in the chest radiography group) and some are overdiagnosis. With follow-up extended to a median of 11.3 years, the two groups had 1701 and 1681 lung cancers (rate ratio 1.01, 0.95–1.09), leaving an excess of only 20: most of the excess was due to lead time, and the upper bound for overdiagnosis is about 1% of the cancers in the CT group. Lung cancer deaths were 1147 versus 1236 (rate ratio 0.92, 0.85–1.00), and the number needed to screen is about 303 (extended follow-up of the NLST Research Team 2019).

![Biases specific to screening. A: lead time (schematic): screening advances the diagnosis (diamond) from the appearance of symptoms to the time of detectability while the time of death is unchanged, so that the "survival from diagnosis" changes from 3.0 to 4.8 years. B: length bias (simulation, seed 0): the length of the detectable preclinical phase follows a log-normal distribution (median 2 years); when a single screen is done at one time, the probability of being found is proportional to the length of the preclinical phase, the median preclinical phase of the tumors found is 3.8 years, and slowly progressing tumors are overrepresented. C: lung cancers diagnosed in the low-dose CT group and the chest radiography group of the NLST, at median follow-up of 6.5 years (Aberle et al. 2011) and 11.3 years (NLST Research Team 2019): the early excess of 119 in the CT group fell to 20 later, bounding the extent of overdiagnosis](./plots/screening-bias.py)

## 18.8. Meta-Analysis

### 18.8.1. Fixed-Effect Meta-Analysis

A single trial is often too small, and the conclusions of different trials often conflict. A systematic review finds all studies on a question by a prespecified search strategy and assesses their quality; on this basis the results are combined by statistical methods.

**Definition 18.8.1 (Meta-Analysis and Fixed-Effect Meta-Analysis)** A statistical analysis that quantitatively combines the effect estimates of several independent studies is called **meta-analysis**. Let the effect estimate of study $i$ be $\hat\theta_i$ (such as the log RR, log OR or mean difference) with variance $v_i$. Assuming that all studies estimate the same true effect $\theta$, weighting by the inverse variance,

$$
\hat\theta_{\mathrm{FE}} = \frac{\sum_i w_i\hat\theta_i}{\sum_i w_i}, \qquad w_i = \frac{1}{v_i}, \qquad \operatorname{Var}(\hat\theta_{\mathrm{FE}}) = \frac{1}{\sum_i w_i},
$$
gives what is called a **fixed-effect meta-analysis**.

Inverse-variance weighting is the same idea as pooling stratified 2×2 tables in [7.7.13](/7.7.13): each study is a stratum, and a large study has a large weight. For binary data one can also pool directly by the Mantel–Haenszel estimate ([7.7.13](/7.7.13) Formula 13.6.1), which is more stable than the inverse-variance method in studies with few events; for very rare events use Peto's O − E method.

### 18.8.2. Heterogeneity and Random-Effects Meta-Analysis

Studies differ in populations, doses, endpoint definitions and length of follow-up, so the true effects may differ as well.

**Definition 18.8.2 (Test of Heterogeneity and $I^2$)** The differences in true effects between studies are called **heterogeneity**. Cochran's statistic

$$
Q = \sum_i w_i(\hat\theta_i - \hat\theta_{\mathrm{FE}})^2
$$
approximately follows $\chi^2_{k-1}$ when the true effects of all studies are the same ($k$ is the number of studies). The quantity

$$
I^2 = \max\Bigl\{0,\ \frac{Q - (k - 1)}{Q}\Bigr\}
$$
is called the **I-squared statistic**, the proportion of the total variation in the effect estimates that is due to true differences between studies (rather than sampling error).

The $Q$ test has very low power when there are few studies ($p > 0.10$ does not show that there is no heterogeneity) and is sensitive to unimportant differences when there are many; $I^2$ does not depend on the number of studies, and 25%, 50% and 75% are often used as rough criteria for low, moderate and high heterogeneity.

**Definition 18.8.3 (Random-Effects Meta-Analysis)** Assume that the true effects $\theta_i$ of the studies come from the distribution $\mathcal{N}(\mu, \tau^2)$ and $\hat\theta_i \mid \theta_i \sim \mathcal{N}(\theta_i, v_i)$, and estimate the average effect $\mu$ with weights $w_i^* = 1/(v_i + \hat\tau^2)$; such a pooling is called **random-effects meta-analysis**. The DerSimonian–Laird moment estimate of the between-study variance is

$$
\hat\tau^2 = \max\Bigl\{0,\ \frac{Q - (k - 1)}{\sum_i w_i - \sum_i w_i^2/\sum_i w_i}\Bigr\}.
$$

It is the random-effects model of [7.7.17](/7.7.17) (Definition 17.3.1), with "groups" replaced by studies and the within-group variance $v_i$ known. Compared with the fixed-effect model, its weights are more even (the relative weights of small studies increase) and the interval is wider; it estimates the mean of the distribution of effects, not a single common effect. $\tau$ also gives a more useful quantity: the 95% prediction interval for the true effect in a new study (a new population) is about $\hat\mu \pm t_{k-2}\sqrt{\hat\tau^2 + \widehat{\operatorname{Var}}(\hat\mu)}$. When $\tau^2 = 0$ the two models are identical. The DerSimonian–Laird estimate underestimates $\tau^2$ when there are few studies; REML or Paule–Mandel estimates, with intervals by the Hartung–Knapp method, are now often used.

### 18.8.3. Aspirin for Primary Prevention

**Example 18.8.1 (Meta-Analysis of Seven Trials)** We take seven randomized trials of aspirin for primary prevention published in 1998–2018, using for each the relative effect on the primary cardiovascular composite endpoint and its 95% interval as data (the endpoint definitions are not entirely the same; HOT reported only a 15% reduction and $p = 0.03$, from which the standard error is back-calculated):

| Trial | Population | Relative effect on the primary cardiovascular endpoint (95% interval) | Inverse-variance weight |
|---|---|---|---|
| TPT 1998 | 5085 high-risk men (factorial, including warfarin) | 0.80 (0.65, 0.99), ischemic heart disease | 87 |
| HOT 1998 | 18,790 hypertensive patients | 0.85 ($p = 0.03$), major cardiovascular events | 178 |
| PPP 2001 | 4495 people with risk factors | 0.77 (0.62, 0.95), total cardiovascular events | 84 |
| WHS 2005 | 39,876 women | 0.91 (0.80, 1.03), major cardiovascular events | 241 |
| ARRIVE 2018 | 12,546 people at moderate risk | 0.96 (0.81, 1.13) | 139 |
| ASCEND 2018 | 15,480 patients with diabetes | 0.88 (0.79, 0.97), serious vascular events | 365 |
| ASPREE 2018 | 19,114 people aged 70 or older | 0.95 (0.83, 1.08), cardiovascular disease | 222 |

The fixed-effect estimate is $\exp(\hat\theta_{\mathrm{FE}}) = 0.89$ (95% interval 0.84–0.94), $z = -4.32$, $p = 1.5 \times 10^{-5}$. $Q = 5.03$ with 6 degrees of freedom, $p = 0.54$, $I^2 = 0$ and $\hat\tau^2 = 0$: there is no heterogeneity beyond sampling error, and the random-effects estimate is identical to the fixed-effect one. The relative reduction of about 11% agrees with the 12% (serious vascular events 0.51% versus 0.57% per year) obtained by the Antithrombotic Trialists' Collaboration (2009) from individual data of six trials.

**Example 18.8.2 (Updating the Evidence)** Adding the trials one by one in order of publication year (cumulative meta-analysis, panel B of the figure below), the two trials of 1998 give 0.83 (0.74–0.94), by 2005 it is 0.85 (0.79–0.93), and after adding the three trials of 2018 it is 0.89 (0.84–0.94). Considering only the three trials of 2018, the pooled estimate is 0.92 (0.85–0.99). The relative effect moves slightly toward 1 in the newer trials, and the more important change is on the absolute scale: in the 2018 populations, antihypertensive treatment, lipid-lowering treatment and smoking cessation were already widespread and the baseline risk was much lower (the event rate in ARRIVE was far lower than expected at the design stage). In ASCEND aspirin reduced serious vascular events by 1.1 percentage points (NNT about 91, 7.4 years) but increased major bleeding by 0.9 percentage points (NNH about 112); in ASPREE the HR for major bleeding was 1.38 (1.18–1.62) and the HR for cardiovascular disease 0.95. Benefit and harm roughly cancel on the absolute scale, so the main guidelines after 2019 (ACC/AHA 2019, USPSTF 2022) no longer recommend the routine use of aspirin for primary prevention in the general population.

**Example 18.8.3 (Pooling with Heterogeneity)** Five trials reported bleeding (with different endpoints: for HOT nonfatal major bleeding, RR 1.84 computed from 129/9399 versus 70/9391; for WHS gastrointestinal bleeding requiring transfusion; for ARRIVE gastrointestinal bleeding; for ASCEND and ASPREE major bleeding): the fixed-effect estimate is 1.42 (1.29–1.57); $Q = 7.62$ with 4 degrees of freedom, $p = 0.11$, $I^2 = 47\%$; the DerSimonian–Laird $\hat\tau^2 = 0.0123$ ($\hat\tau = 0.11$) and the random-effects estimate is 1.48 (1.28–1.71), with a wider interval and weights tilted toward small trials. Part of the heterogeneity comes from the different endpoint definitions. Another meta-analysis of 11 trials reported a pooled RR of 0.82 (0.71–0.94) for myocardial infarction with $I^2 = 67\%$, and the effect was no longer evident when only recent trials were considered (Mahmoud et al. 2019): heterogeneity is itself a signal that the evidence changes with the era.

![Meta-analysis of aspirin for primary prevention (published trial results). A: relative effects and 95% intervals on the primary cardiovascular composite endpoint of seven trials (endpoint definitions differ between trials) (square areas are proportional to the inverse-variance weights; the standard error of HOT is back-calculated from the reported 15% reduction and $p = 0.03$), and the pooled estimates (diamonds) by inverse-variance fixed-effect and DerSimonian–Laird random-effects models; TPT, HOT, PPP, WHS, ARRIVE, ASCEND and ASPREE are, respectively, the Medical Research Council General Practice Research Framework (1998), Hansson et al. (1998), the PPP Collaborative Group (2001), Ridker et al. (2005), Gaziano et al. (2018), the ASCEND Study Collaborative Group (2018) and McNeil et al. (2018). B: cumulative fixed-effect meta-analysis in order of publication. C: bleeding (nonfatal major bleeding for HOT, computed from event counts; gastrointestinal bleeding requiring transfusion for WHS; gastrointestinal bleeding for ARRIVE; major bleeding for ASCEND and ASPREE); moderate heterogeneity makes the random-effects interval wider](./plots/forest-aspirin.py)

**Definition 18.8.4 (Forest Plot)** A plot with one row per study, showing its effect estimate and confidence interval by a point (a square with area proportional to the weight) and a line segment, the pooled estimate by a diamond, and ratio-type effects on a logarithmic scale, is called a **forest plot**.

### 18.8.4. Publication Bias and the Funnel Plot

A meta-analysis can pool only the studies that can be found.

**Definition 18.8.5 (Publication Bias and the Funnel Plot)** The phenomenon that whether a study is published (or how quickly, or in what form) depends on the direction or significance of its results, so that published studies are not representative of all studies, is called **publication bias**. A scatter plot of the studies with the effect estimate on the horizontal axis and the standard error (increasing downward) on the vertical axis is called a **funnel plot**: without bias, the points are distributed symmetrically around the true effect, scattered widely for small studies and concentrated for large ones, in the shape of an inverted funnel.

Small negative studies are the most likely to go unpublished, which leaves one corner of the funnel plot empty and the plot asymmetric. Egger's test regresses $\hat\theta_i/\mathrm{SE}_i$ on $1/\mathrm{SE}_i$ and tests whether the intercept is 0 (it is 0 when symmetric). Funnel plot asymmetry does not necessarily come from publication bias: small studies may differ in population or quality (small-study effects), and true heterogeneity can also cause asymmetry; with fewer than 10 studies the test has almost no power. In the 7 trials of Example 18.8.1, Egger's test gives $p = 0.26$, which tells us nothing.

**Example 18.8.4 (Simulation)** We simulate 120 trials with a true log odds ratio of −0.15 (OR 0.86); all trials with a significant benefit are published, and only 20% of the rest. The fixed-effect estimate over all 120 trials is OR 0.84, close to the true value; the 35 published trials give OR 0.77, exaggerating the effect. The lower right corner of the funnel plot (panel B below) is clearly empty, but Egger's test gives $p = 0.30$. A more effective countermeasure than a statistical test is at the source: trial registration (Section 18.9) makes unpublished trials findable.

![Publication bias in a funnel plot (simulation, seed 0). 120 two-arm trials, with true log odds ratio −0.15 (OR 0.86), 20–800 people per arm (event risk 0.2), the standard error of each trial determined by its size; trials with a significant benefit ($z < -1.96$) are all published, and the others with probability 0.2. A: all 120 trials, with dashed pseudo-confidence limits at the true value ± 1.96 SE, the vertical black line at the true value, the dotted line at 0 and the orange line the fixed-effect estimate. B: only the 35 published trials: small trials not showing benefit are missing at the lower right, the funnel is asymmetric, the pooled estimate exaggerates the benefit, and Egger's regression test has very low power](./plots/funnel.py)

## 18.9. Reproducibility and Reporting Guidelines

Beyond statistical methods, the credibility of evidence depends on the transparency of the research process:

- Preregistration: since 2005 the International Committee of Medical Journal Editors (ICMJE) has required clinical trials to register the primary endpoint and the sample size in a public registry (ClinicalTrials.gov, the WHO International Clinical Trials Registry Platform and others) before the first participant is enrolled. Post hoc changes of the primary endpoint ("outcome switching") can be detected from the registry record.
- Statistical analysis plan: written before unblinding, fixing the primary analysis, covariate adjustment, handling of missing data ([7.7.17](/7.7.17) Section 17.8) and the rules for subgroup and interim analyses.
- Reporting guidelines: randomized trials follow CONSORT (the flow diagram reports the numbers at each stage: screened, randomized, treated, lost to follow-up, analyzed), systematic reviews and meta-analyses follow PRISMA 2020, observational studies STROBE, and diagnostic accuracy studies STARD.
- Observational and laboratory studies are subject to the same: write the analysis plan in advance, distinguish confirmatory from exploratory analyses ([7.7.1](/7.7.1) Section 1.6), and report all comparisons that were made, not only the significant one.

## 18.10. Computing with Python

```python
import numpy as np
from scipy import stats
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.meta_analysis import combine_effects

z = stats.norm.ppf
# sample size for two proportions (Example 18.4.1) and the adjustments of Formula 18.4.2
p2, p1 = 0.022, 0.022 * 0.75
pb = (p1 + p2) / 2
n = (z(0.975) * np.sqrt(2 * pb * (1 - pb)) + z(0.8) * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p1 - p2) ** 2
print(n, n / 0.8 ** 2, n / 0.8 ** 2 * (1 + 99 * 0.02))      # 9796, 15306, 45612 per arm
h = proportion_effectsize(p1, p2)                            # arcsine version, similar answer
print(NormalIndPower().solve_power(h, alpha=0.05, power=0.8))

# non-inferiority (Example 18.3.1) and TOST for bioequivalence (Example 18.3.2)
d, se = 0.023 - 0.021, np.sqrt(0.023 * 0.977 / 5000 + 0.021 * 0.979 / 5000)
print(d + np.array([-1.96, 1.96]) * se, stats.norm.cdf((d - 0.01) / se))   # upper 0.77%, p = 0.003
est, se, df = np.log(0.95), 0.040, 22
print(np.exp(est + np.array([-1, 1]) * stats.t.ppf(0.95, df) * se))       # (0.887, 1.018)

# meta-analysis of the seven aspirin trials (Example 18.8.1)
rr = np.array([0.80, 0.85, 0.77, 0.91, 0.96, 0.88, 0.95])
lo = np.array([0.65, np.nan, 0.62, 0.80, 0.81, 0.79, 0.83])
hi = np.array([0.99, np.nan, 0.95, 1.03, 1.13, 0.97, 1.08])
y = np.log(rr)
se = (np.log(hi) - np.log(lo)) / (2 * z(0.975))
se[1] = abs(y[1]) / z(1 - 0.03 / 2)                          # HOT: from p = 0.03
res = combine_effects(y, se ** 2, method_re="chi2")         # "chi2" = DerSimonian-Laird
print(res.summary_frame())          # fixed 0.89 (0.84, 0.94); Q = 5.03, I2 = 0, tau2 = 0 on the log scale
```

`combine_effects` returns a table of the individual studies and the fixed-effect and random-effects pooled estimates (on the log scale; exponentiate to obtain ratios), and `res.q`, `res.i2` and `res.tau2` are the heterogeneity statistics; `method_re="chi2"` is the DerSimonian–Laird estimate, and the default `"iterated"` gives the Paule–Mandel estimate. The boundaries of a group sequential design can be computed by the numerical integration used for the figure, or with a dedicated software package.

## Summary

- The four phases of an RCT (Definition 18.1.1); designs: parallel, factorial (PHS), crossover, cluster randomized (multiplied by the design effect), adaptive and platform trials.
- Endpoints: prespecify a single primary endpoint; a surrogate endpoint (Definition 18.2.1) requires that the effect of treatment on it predict the effect on the clinical endpoint (the counterexample of CAST).
- Analysis populations (Definition 18.2.2): ITT preserves randomization and is the primary analysis in superiority trials; per-protocol analysis reintroduces confounding; non-inferiority trials report both.
- Non-inferiority and equivalence (Definitions 18.3.1, 18.3.2): an upper limit $< M$ is non-inferiority; TOST is equivalent to the 90% interval lying within $(-M, M)$; bioequivalence is 0.80–1.25 (Example 18.3.2). "Not significant" is not equivalence.
- Sample size (Formula 18.4.1): $n = (z_{\alpha/2} + z_\beta)^2v/\delta^2$, with $(z_{\alpha/2} + z_\beta)^2 = 7.85$ (80%) and 10.51 (90%); corrections: loss to follow-up $1/(1 - L)$, noncompliance $1/(1 - d_{\mathrm{in}} - d_{\mathrm{out}})^2$, clustering $1 + (m - 1)\rho$ (Formula 18.4.2). PHS: detecting a 25% reduction needs about 9800 per group (Example 18.4.1).
- Interim analysis (Definition 18.5.1): 5 unadjusted tests give $\alpha$ of 0.14; Pocock 2.41, O'Brien–Fleming 4.56 → 2.04; the alpha spending function (Definition 18.5.2) allows flexible analysis times. Early stopping overestimates the effect and reduces secondary information (PHS, Example 18.5.1).
- Multiplicity: for several endpoints use Holm or a fixed sequence; subgroups need an interaction test, prespecification and replication (the astrological signs in ISIS-2, Example 18.6.1).
- Screening (Definition 18.7.1): lead-time bias, length bias and overdiagnosis make survival rates meaningless; use disease mortality in a randomized trial as the endpoint. The excess diagnoses in the NLST fell from 119 to 20 (Example 18.7.1).
- Meta-analysis:

  | | Fixed effect (Definition 18.8.1) | Random effects (Definition 18.8.3) |
  |---|---|---|
  | Assumption | Common effect $\theta$ | $\theta_i \sim \mathcal{N}(\mu, \tau^2)$ |
  | Weight | $1/v_i$ | $1/(v_i + \hat\tau^2)$ |
  | Quantity estimated | Common effect | Mean of the distribution of effects; prediction interval |

  Heterogeneity $Q$, $I^2$ (Definition 18.8.2), DerSimonian–Laird $\hat\tau^2$. Seven aspirin trials: 0.89 (0.84–0.94), $I^2 = 0$ (Example 18.8.1); cumulative analysis and the balance of absolute benefit and harm changed the guidelines (Example 18.8.2); bleeding $I^2 = 47\%$ (Example 18.8.3).
- Forest plot (Definition 18.8.4); publication bias and the funnel plot (Definition 18.8.5), with low power of Egger's test (Example 18.8.4); countermeasures are registration, analysis plans, and CONSORT and PRISMA.

## Questions

1. A phase III trial following phase II expects a remission rate of 20% for the standard treatment and 30% for the new treatment. How many people per group are needed for two-sided $\alpha = 0.05$ and 80% power? What if 10% loss to follow-up is expected?

   **Answer** By Formula 9.4.1 ([7.7.9](/7.7.9)), $\bar p = 0.25$: $n = [1.96\sqrt{2 \times 0.25 \times 0.75} + 0.842\sqrt{0.3 \times 0.7 + 0.2 \times 0.8}]^2/0.1^2 = [1.200 + 0.512]^2/0.01 = 293.2$, so 294 per group. Correcting for loss to follow-up, $294/0.9 = 326.7$, so 327 per group are recruited.

2. Use Formula 18.4.1 to derive the sample size of a non-inferiority trial: the true stroke risk is 2.1% in both groups and the margin is 1 percentage point; how many people per group are needed for one-sided $\alpha = 0.025$ and 90% power? Why is a non-inferiority trial often larger than a superiority trial?

   **Answer** The true difference is 0, and to reject $H_0\colon\Delta \ge M$ with power 0.9, $\delta = M = 0.01$ and $v = 2 \times 0.021 \times 0.979 = 0.0411$, so $n = (1.96 + 1.282)^2 \times 0.0411/0.01^2 = 4320$ per group. The margin is usually much smaller than the difference a superiority trial wants to detect (here 1 percentage point, a relative 48%), and the sample size is inversely proportional to $\delta^2$; moreover the one-sided 0.025 required by regulators is equivalent to the two-sided 0.05 and cannot be relaxed.

3. In a trial, 10% of the control group take the study drug on their own and 15% of the treatment group stop the drug. Under full compliance each group would need 800 people. Allowing for noncompliance and 5% loss to follow-up, how many people should be recruited? What does ITT estimate?

   **Answer** $n' = 800/(1 - 0.10 - 0.15)^2 = 800/0.5625 = 1422$, and dividing by 0.95 gives 1497, about 1500 per group. ITT estimates the effect of "being assigned to the new treatment" under this compliance, about 75% of the effect under full compliance; it is the effect that will actually be obtained in policy and clinical practice.

4. A trial designed with O'Brien–Fleming boundaries and 5 planned analyses has $z = 3.5$ at the first interim analysis (information fraction 0.2). Should it stop? What if Pocock boundaries were used? What if $z = 2.7$ at the third analysis?

   **Answer** The O'Brien–Fleming boundary at the first analysis is 4.56 and $3.5 < 4.56$, so continue; the Pocock boundary is 2.41 and $3.5 > 2.41$, so the rule says to stop. At the third analysis with $z = 2.7$: the O'Brien–Fleming boundary is 2.63, which is crossed, so the trial may stop; Pocock's 2.41 is also crossed. With only 20% of the information early on, the effect estimate behind $z = 3.5$ is very unstable (its standard error is $\sqrt5$ times the final one), and O'Brien–Fleming demands stronger evidence precisely to avoid stopping because of an early random peak and overestimating the effect.

5. Three trials have log RRs of −0.4, −0.1 and 0.1 with standard errors 0.20, 0.10 and 0.15. Compute the fixed-effect estimate, $Q$, $I^2$, the DerSimonian–Laird $\hat\tau^2$ and the random-effects estimate.

   **Answer** The weights are 25, 100 and 44.4, $\hat\theta_{\mathrm{FE}} = (-10 - 10 + 4.44)/169.4 = -0.092$ (RR 0.91), SE $= 1/\sqrt{169.4} = 0.077$. $Q = 25(-0.308)^2 + 100(-0.008)^2 + 44.4(0.192)^2 = 2.37 + 0.007 + 1.64 = 4.02$ with 2 degrees of freedom, $p = 0.13$, $I^2 = (4.02 - 2)/4.02 = 50\%$. $\hat\tau^2 = 2.02/(169.4 - (625 + 10\,000 + 1975)/169.4) = 2.02/95.1 = 0.0212$. The random-effects weights $1/(v_i + 0.0212)$ are 16.3, 32.0 and 22.9, $\hat\mu = -0.105$ (RR 0.90), with SE 0.118 (versus 0.077 for the fixed effect). The weights become more even and the interval wider.

6. The 5-year survival of a cancer rose from 50% to 70% after screening was introduced, yet the mortality from the disease (per 100,000 person-years) did not change. Explain this phenomenon and say what kind of evidence could show that screening is effective.

   **Answer** Lead time lengthens survival counted from diagnosis, length bias makes slowly progressing cases more numerous among those found by screening, and overdiagnosis adds "cases" that would never have been fatal; all three raise the 5-year survival without changing the number of deaths; an unchanged population mortality suggests precisely that screening may not have postponed any deaths. A randomized controlled trial is needed, with the disease-specific mortality (ideally together with all-cause mortality) of all those randomized (ITT) as the endpoint, such as the 20% reduction in lung cancer mortality in the NLST.

7. A trial reports that the HR of the treatment is 0.70 in men (log SE 0.15, $p = 0.02$) and 0.95 in women (SE 0.12, $p = 0.67$), and the authors conclude that "the treatment works only in men". Evaluate this conclusion.

   **Answer** The correct comparison is the interaction: $\ln 0.70 - \ln 0.95 = -0.305$, SE $= \sqrt{0.15^2 + 0.12^2} = 0.192$, $z = -1.59$, $p = 0.11$; there is no evidence that the effects differ between men and women. "One significant and one not" does not mean "the two differ". If the subgroups were not prespecified, or many subgroups were compared, the conclusion is even less credible. A reasonable report gives the overall effect and its interval, with the estimates in each subgroup and the $p$-value of the interaction test.

8. Why do trials stopped early for benefit tend to overestimate the effect? In a trial whose true effect is small, if the O'Brien–Fleming boundary is crossed at the first interim analysis, what is the least the estimated effect can be (expressed as a multiple of the effect that would just be detectable at the final analysis)?

   **Answer** The condition for stopping is that "the estimate at this moment is large": among the many possible courses of a trial, only those that cross the boundary just when random fluctuation makes the effect look largest are stopped, and conditional on stopping, the expected value of the estimate is greater than the true value (selection by truncation). The O'Brien–Fleming boundary at the first analysis ($t = 0.2$) is 4.56; the standard error of the estimate at this time is $1/\sqrt{0.2} = 2.24$ times the final one, so a crossing estimate is at least $4.56 \times 2.24 = 10.2$ "final standard errors", whereas the boundary at the final analysis is 2.04. That is, the crossing estimate is at least 5 times what would be just significant at the final analysis, far beyond most realistic effects.

9. Does $I^2 = 0$ in a meta-analysis show that the true effects of the studies are the same? In the aspirin example $I^2 = 0$; why do guidelines still hold that the benefit differs across populations?

   **Answer** It does not: with few studies the power of $Q$ is very low, $I^2 = 0$ shows only that the observed differences do not exceed sampling error, and the interval of $I^2$ itself is often very wide (with 7 studies it can run from 0 to more than 70%). More important, the heterogeneity statistics are computed on the relative scale (log RR): when the relative effect is constant, the absolute effect still varies in proportion to the baseline risk. The baseline risk of the 2018 populations is low, so the same 11% relative reduction brings only a small absolute benefit, while the absolute increase in bleeding does not shrink accordingly, and the balance of benefit and harm changes (Example 18.8.2).

10. (Design question) You want to conduct a systematic review and meta-analysis on "whether vitamin D supplementation in pregnancy reduces preterm birth". Write down the key steps and statistical decisions.

    **Answer** (1) Preregister the protocol (for example in PROSPERO) and state the question with PICO: pregnant women, vitamin D supplementation (dose, time of starting), placebo or no supplementation, preterm birth (< 37 weeks). (2) Search several databases systematically, including trial registries and unpublished studies; two reviewers screen and extract data independently, and quality is assessed with a risk-of-bias tool. (3) Effect measure: the RR and interval of each trial (or the 2×2 table), pooled by Mantel–Haenszel or inverse variance; state in advance that a random-effects model is used (differences in dose and population are expected to be large), and report $\tau^2$, $I^2$ and the prediction interval. (4) Prespecify a few subgroups or a meta-regression (dose, baseline vitamin D level, gestational week at which supplementation starts) and interpret them by interaction tests. (5) Sensitivity analyses: include only trials at low risk of bias, and remove the influence of any single large trial. (6) Funnel plot and Egger's test (with at least 10 trials), compared against unpublished trials in the registries. (7) Assess the certainty of the evidence with GRADE, report according to PRISMA 2020, and also give absolute effects (how many fewer preterm births per 1000 pregnant women).
