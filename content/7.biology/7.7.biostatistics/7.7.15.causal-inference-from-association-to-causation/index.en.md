---
title: "Causal Inference: From Association to Causation"
description: "Correlation is not causation: ecological fallacy, reverse causation and confounding; the potential-outcomes framework and individual and average treatment effects; why randomization identifies causal effects (exchangeability, positivity, consistency); causal diagrams, the backdoor criterion, mediators and collider bias; propensity-score matching, stratification and inverse probability weighting with balance diagnostics; sensitivity analysis for unmeasured confounding (Cornfield's inequality and the E-value); instrumental variables and Mendelian randomization; reporting observational studies. Illustrated by smoking and FEV in children, maternal smoking and birth weight, and the historical debate on smoking and lung cancer."
source_hash: 5d2586cb9b9b
---

This course opened with a puzzle: children in East Boston who smoke have a higher FEV, so does that mean smoking is harmless ([7.7.1](/7.7.1) Example 1.5.1)? In [7.7.10](/7.7.10), adjusting for age in a multiple regression changed the sign of the smoking coefficient from positive to negative; [7.7.13](/7.7.13) named this phenomenon **confounding** and handled it by standardization and stratification; [7.7.14](/7.7.14) used logistic regression to adjust for several variables at once. But all of these methods sidestep a more fundamental question: what exactly do we want to estimate, and under what conditions can an adjusted estimate be read as "how the outcome would change if we changed the exposure"? Which variables should be adjusted for, and which should not? This chapter presents three basic tools of modern causal inference. **Potential outcomes** define a "causal effect" as a comparison of the same person's outcomes under two treatments, and explain why randomization works and what additional assumptions an observational study needs. A **causal diagram** draws the investigator's knowledge about how the data are generated and uses it to decide what to adjust for. The **propensity score** compresses many confounders into a single number, so that matching, stratification or weighting can imitate a randomized trial. Finally we discuss two remedies for when the assumptions fail: sensitivity analysis for unmeasured confounding (the heart of the 1950s debate on smoking and lung cancer), and instrumental variables and Mendelian randomization, which exploit "natural experiments". The running theme remains smoking: the different roles of age and height in the FEV data, the effect of maternal smoking on birth weight in birthwt, and whether the strong association with lung cancer in the British doctors cohort could be explained by an unmeasured factor.

## 15.1. Correlation Is Not Causation

### 15.1.1. Three Noncausal Explanations

When $A$ and $Y$ are observed to be associated, there are at least three explanations besides "$A$ causes $Y$": chance (handled by confidence intervals and tests); confounding, in which $A$ and $Y$ share a common cause ([7.7.13](/7.7.13) Definition 13.5.1); and reverse causation, in which $Y$ causes $A$. Selection bias (Section 15.4.4) and measurement error are further possibilities.

Reverse causation is especially common in cross-sectional studies. In cross-sectional surveys, nondrinkers are often in worse health than light drinkers, partly because "sick quitters" are classified as nondrinkers; likewise, recent quitters of smoking sometimes have higher short-term mortality than continuing smokers, because many people quit only after a serious disease has been diagnosed. In a prospective cohort the exposure is measured before the outcome, which avoids this problem, but if the exposure itself is influenced by early, not yet diagnosed disease, events in the first few years of follow-up should still be excluded as a sensitivity analysis.

### 15.1.2. The Ecological Fallacy

**Definition 15.1.1 (Ecological Fallacy)** The error of inferring an individual-level association from a group-level association is called the **ecological fallacy**.

[7.7.1](/7.7.1) Section 1.5.2 gave the example of the country-level correlation between per capita chocolate consumption and the number of Nobel laureates (Messerli 2012, $r = 0.79$). A classic quantitative example is Robinson's (1950) analysis of the 1930 US census: across the 48 states, the correlation between the proportion of foreign-born residents and the illiteracy rate was $-0.53$ (states with many immigrants had lower illiteracy), whereas at the individual level the correlation between being foreign-born and being illiterate was $+0.12$. The reason is that immigrants tended to settle in industrial states where literacy among the native-born was high. A group-level association reflects differences between groups in many factors, and it can have the opposite sign to the individual-level association. Ecological studies ([7.7.13](/7.7.13) Definition 13.1.3) remain useful, because some exposures are group-level by nature (air pollution, water fluoridation, policies), but their conclusions apply only to groups.

## 15.2. Potential Outcomes

### 15.2.1. Individual Causal Effects

To say clearly that "smoking causes low birth weight", we first have to say clearly what is being compared.

**Definition 15.2.1 (Potential Outcome)** For a binary treatment $A \in \{0, 1\}$, each individual has two **potential outcomes**: the outcome $Y(1)$ if treated and the outcome $Y(0)$ if not treated. The difference $Y(1) - Y(0)$ is the causal effect for that individual. The outcome actually observed is $Y = A\,Y(1) + (1 - A)\,Y(0)$, the one that corresponds to the treatment actually received; the other is called the counterfactual outcome.

The fundamental difficulty of causal inference is that only one of the two potential outcomes can be observed for each person. The same mother cannot both smoke and not smoke during the same pregnancy. Individual causal effects are therefore generally not identifiable; what can be estimated are averages over a population.

**Definition 15.2.2 (Average Treatment Effect)** The quantity $\mathrm{ATE} = \mathbb{E}[Y(1) - Y(0)] = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$ is called the **average treatment effect**; averaging only over those who actually received the treatment gives $\mathrm{ATT} = \mathbb{E}[Y(1) - Y(0) \mid A = 1]$, the average treatment effect in the treated. For a binary outcome one can also compare $\mathbb{P}(Y(1) = 1)/\mathbb{P}(Y(0) = 1)$, the causal RR.

**Example 15.2.1 (A Worked Example)** Suppose the potential outcomes of 8 patients are as follows (1 = death; the numbers are made up for illustration), and that physicians tend to give the drug to sicker patients:

| Patient | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| $Y(0)$ | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| $Y(1)$ | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 |
| Drug actually given, $A$ | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |

The true $\mathrm{ATE} = 5/8 - 4/8 = 0.125$: the drug raises mortality by 12.5 percentage points on average. What is actually observed, however, is $Y(1)$ for the treated (patients 3, 4, 6, 8) and $Y(0)$ for the untreated (patients 1, 2, 5, 7): the mortality is $3/4$ in the treated group and $0/4$ in the untreated group, so the naive difference is 0.75. The discrepancy arises because the treated and the untreated had different prognoses to begin with (all the treated have $Y(0) = 1$); this is confounding, known clinically as confounding by indication.

### 15.2.2. Well-Defined Interventions

Potential outcomes require the treatment to be an intervention that one can imagine applying. "What would happen if this person had a different sex?" is not a well-defined causal question: changing sex involves everything from the fertilized egg onward, and there is no corresponding intervention; "what would happen if everything else on the résumé stayed the same and only the sex field changed?" is a well-defined question ([7.7.1](/7.7.1) Section 1.5.2). Likewise, "the causal effect of obesity" must specify the intervention: weight loss through diet, exercise or surgery need not have the same effect.

**Definition 15.2.3 (Consistency)** The consistency assumption holds if the observed outcome of an individual who actually received treatment $a$ equals the individual's potential outcome $Y(a)$, that is, $A = a \Rightarrow Y = Y(a)$. It requires that different versions of the treatment (different ways of losing weight) have the same effect on the outcome, and that one person's outcome is not affected by other people's treatments (no interference; this often fails for vaccination and infectious diseases).

## 15.3. Randomization and Identification

### 15.3.1. Exchangeability

**Definition 15.3.1 (Exchangeability and Positivity)** If the potential outcomes are independent of the treatment actually received, $\{Y(0), Y(1)\} \perp A$, the treated and control groups are said to be exchangeable, a condition called **exchangeability**. If $\{Y(0), Y(1)\} \perp A \mid L$ holds at every value of a covariate $L$, conditional exchangeability holds. If, for every value of $L$ (occurring in the population), the probabilities of receiving and not receiving the treatment are both greater than 0, $0 < \mathbb{P}(A = 1 \mid L = l) < 1$, **positivity** holds.

**Theorem 15.3.1 (Randomization Identifies the Average Treatment Effect)** If exchangeability and consistency hold, then $\mathbb{E}[Y \mid A = a] = \mathbb{E}[Y(a)]$, and hence the observed difference between groups $\mathbb{E}[Y \mid A = 1] - \mathbb{E}[Y \mid A = 0]$ equals the ATE.

**Proof** By consistency, $\mathbb{E}[Y \mid A = a] = \mathbb{E}[Y(a) \mid A = a]$; by exchangeability, $Y(a)$ is independent of $A$, so $\mathbb{E}[Y(a) \mid A = a] = \mathbb{E}[Y(a)]$. $\square$

Random assignment of the treatment (**randomization**, [7.7.5](/7.7.5) Section 5.2) lets a coin toss determine $A$, so that $A$ is independent of every characteristic of the individual, including the potential outcomes; exchangeability then holds by design. This is why randomized controlled trials can support causal conclusions (for example, the Physicians' Health Study with RR = 0.58, [7.7.13](/7.7.13) Example 13.2.1). In Example 15.2.1 exchangeability fails: the $Y(0)$ of the treated differ from those of the untreated.

### 15.3.2. Observational Studies: Conditional Exchangeability

In an observational study, exchangeability can only be hoped for within the strata of the measured covariates $L$: among mothers of the same age, race and weight, whether a mother smokes is "as if random". This assumption cannot be tested with the data; it can only be argued from knowledge of the research question, and causal diagrams (Section 15.4) are the tool for such arguments.

**Theorem 15.3.2 (Standardization and Inverse Probability Weighting)** If consistency, conditional exchangeability (given $L$) and positivity hold, then

$$
\mathbb{E}[Y(a)] = \sum_l \mathbb{E}[Y \mid A = a, L = l]\,\mathbb{P}(L = l) = \mathbb{E}\left[\frac{\boldsymbol{1}_{\{A = a\}}\,Y}{\mathbb{P}(A = a \mid L)}\right].
$$

**Proof** First expression: $\mathbb{E}[Y(a)] = \sum_l \mathbb{E}[Y(a) \mid L = l]\mathbb{P}(L = l)$; by conditional exchangeability $\mathbb{E}[Y(a) \mid L = l] = \mathbb{E}[Y(a) \mid A = a, L = l]$, which by consistency equals $\mathbb{E}[Y \mid A = a, L = l]$; positivity guarantees that this conditional expectation is defined. Second expression: given $L$, $\mathbb{E}[\boldsymbol{1}_{\{A = a\}}Y \mid L] = \mathbb{P}(A = a \mid L)\,\mathbb{E}[Y \mid A = a, L]$; dividing by $\mathbb{P}(A = a \mid L)$ and taking the expectation over $L$ returns the first expression. $\square$

The first expression is the general form of the direct standardization of [7.7.13](/7.7.13) (with the whole study population as the standard population) and is called the g-formula; the second is the basis of the inverse probability weighting in Section 15.5: each person is weighted by the reciprocal of the probability of receiving the treatment actually received, so that in the weighted population the treatment is unrelated to $L$, as in a randomized trial. Both require positivity: if everyone of some type (say, with $L = l$) smokes, the data cannot tell us what would happen to them if they did not smoke.

## 15.4. Causal Diagrams

### 15.4.1. Directed Acyclic Graphs

**Definition 15.4.1 (Causal Diagram)** A **directed acyclic graph** whose nodes represent variables and whose directed edges $X \to Z$ mean that $X$ is a direct cause of $Z$ is called a **causal diagram** if it includes all common causes of any two variables in the graph.

A causal diagram encodes the investigator's assumptions about how the data are generated: a drawn arrow means "there may be a direct effect", and an omitted arrow is the stronger assumption "there is no direct effect". A path between two variables is a sequence of edges (regardless of direction); association flows along paths, but one kind of node blocks it.

Three basic structures (panels A–C of the figure below) determine whether association is transmitted along a path:

| Structure | Form | Without adjusting for the intermediate variable | After adjusting for it (conditioning on it) |
|---|---|---|---|
| Fork (confounding) | $A \leftarrow L \to Y$ | Path open; $A$ and $Y$ are associated | Path blocked |
| Chain (mediation) | $A \to M \to Y$ | Path open (causal path) | Path blocked; part of the effect is adjusted away |
| Collider | $A \to C \leftarrow Y$ | Path blocked | Path opened; spurious association arises |

**Definition 15.4.2 (Mediator and Collider)** A variable on the causal path from exposure to outcome ($M$ in $A \to M \to Y$) is called a **mediator**; a variable at which two arrowheads on a path meet ($C$ in $A \to C \leftarrow Y$) is called a **collider** on that path. The association introduced between its two causes by conditioning on a collider (or on its descendant) is called **collider bias**.

![Causal diagrams (schematic). A–C: the three basic structures through which an exposure A and an outcome Y are connected via a third variable: the confounder L (fork, A ← L → Y), the mediator M (chain, A → M → Y) and the collider C (A → C ← Y). Adjusting for L removes bias; adjusting for M adjusts away part of the effect; adjusting for C creates an association between A and Y that would otherwise be unrelated. D: a causal diagram for smoking and FEV in children: age and sex influence smoking, height and FEV, and height lies partly on the path from smoking to FEV; dashed lines indicate possible effects](./plots/dag-basics.py)

### 15.4.2. The Backdoor Criterion

**Theorem 15.4.1 (Backdoor Criterion)** In a causal diagram, a path from $A$ to $Y$ that begins with $A \leftarrow \cdots$ (the first edge points into $A$) is called a backdoor path. Suppose a set of variables $L$ satisfies: (1) no member of $L$ is a descendant of $A$; and (2) $L$ blocks every backdoor path between $A$ and $Y$ (a path is blocked if and only if it contains a collider that is not in $L$ and none of whose descendants is in $L$, or it contains a noncollider that is in $L$). Then conditional exchangeability holds given $L$, and the average effect of $A$ on $Y$ is identified by Theorem 15.3.2. A set $L$ satisfying these two conditions is said to satisfy the **backdoor criterion**.

For the proof see Pearl (2009); here we use only its consequences. Condition (1) excludes mediators and colliders on the causal path: adjusting for a consequence of the exposure either adjusts away part of the effect or introduces bias. Condition (2) requires that all confounding paths be closed. More than one set may satisfy the criterion, and there may be none (if a key confounder is unmeasured). Note that the criterion does not require "adjusting for all variables associated with both $A$ and $Y$": the three rules of thumb in [7.7.13](/7.7.13) Definition 13.5.1 agree with the backdoor criterion in most cases, but fail in the presence of colliders (Section 15.4.4).

### 15.4.3. FEV: Age Is a Confounder, Height Is a Mediator

**Example 15.4.1** Panel D of the figure above is a plausible causal diagram for smoking and FEV in children: age affects whether a child smokes (older children are the ones who smoke), height and FEV; sex affects height and FEV and may also affect smoking; smoking may inhibit growth (affecting height) and may also directly damage lung function; height affects FEV. The backdoor paths from smoking to FEV are "smoking ← age → FEV", "smoking ← age → height → FEV" and similar paths through sex; {age, sex} blocks all of them, whereas height is a descendant of smoking and should not be adjusted for. Using the data on 654 children:

| Adjustment set | Smoking coefficient (FEV / L) | 95% interval | What is estimated |
|---|---|---|---|
| None | $+0.711$ | $(0.495, 0.927)$ | Crude difference, confounded by age |
| Age | $-0.209$ | $(-0.368, -0.050)$ | Main confounder adjusted for |
| Age, sex | $-0.154$ | $(-0.307, -0.001)$ | Total effect (backdoor criterion) |
| Age, sex, height | $-0.110$ | $(-0.228, 0.008)$ | The part not through height (needs stronger assumptions) |

On the log scale, after adjusting for age and sex, the FEV of smokers is on average 7.1% lower (95% interval 1.5%–12.3%); after additionally adjusting for height, it is 4.5% lower (0.5%–8.3%, the last row of [7.7.10](/7.7.10) Example 10.7.1). The difference between the two reflects the role of the path "smoking → height → FEV": among children of the same age and sex, smokers are on average 0.64 in shorter (95% interval −1.60 to 0.32); the evidence is not strong, but the direction agrees with smoking inhibiting growth. If the research question is "the total harm of smoking to lung function in children", the estimate that does not adjust for height should be reported. The coefficient after adjusting for height is often called the "direct effect", but interpreting it as a causal direct effect requires the further assumption that there is no unmeasured confounding between height and FEV (for example nutrition or genetics); formal mediation analysis is beyond the scope of this course.

These estimates still depend on the diagram being correct: if there are unmeasured common causes (family socioeconomic status, passive smoking from parental smoking) that were not drawn in, {age, sex} is not enough to block all the backdoor paths.

### 15.4.4. Collider Bias

Collider bias is the most counterintuitive kind of bias, and it often arises through selection: studying only hospitalized patients, only published studies, or only individuals who survived are all cases of conditioning on a collider.

**Example 15.4.2 (Berkson's Bias, Simulation)** Suppose the severities $X$ and $Y$ of two diseases are independent in the population, and that either one being severe enough leads to hospitalization ($X + Y > 1.5$). Among hospitalized patients the two severities are strongly negatively correlated ($r = -0.69$ in the simulation): if a hospitalized patient's $X$ is not severe, he is probably in hospital because his $Y$ is. A case-control study that uses hospital patients as controls ([7.7.13](/7.7.13) Section 13.1.2) may therefore find a "protective effect" between two diseases that are in fact unrelated.

![Collider bias (Berkson's bias), simulation. The severities X and Y of two diseases are independent (standard normal, 2000 people) and almost uncorrelated in the population (A, r = −0.02). People with X + Y > 1.5 are hospitalized (orange). Among hospitalized patients the two are negatively correlated (B, r = −0.69): hospitalization is a common effect of both, and conditioning on it opens a noncausal path between them](./plots/collider-sim.py)

**Example 15.4.3 (The Birth Weight Paradox)** Many studies have found that among low-birth-weight infants, the infant mortality of smoking mothers is lower than that of nonsmoking mothers, as if smoking "protected" low-birth-weight babies. Hernández-Díaz, Schisterman and Hernán (2006) explained this with a causal diagram: birth weight is a consequence of smoking and also of other serious causes (congenital malformations and so on), which also directly raise infant mortality; birth weight is a collider on the path "smoking → low birth weight ← congenital malformation → death". Looking only at low-birth-weight infants, the low birth weight of smokers' infants is probably "just because of smoking", whereas that of nonsmokers' infants is more likely to have a more dangerous cause. Stratifying by birth weight introduces a negative association between smoking and those causes.

:::

The lesson: do not adjust for variables that come after the exposure unless the question itself is about them; "the more you adjust, the safer you are" is wrong.

## 15.5. Propensity Scores

### 15.5.1. Definition and Balancing Property

When there are many covariates to adjust for, regression adjustment must correctly specify the relationship between the outcome and all the covariates (linearity, interactions), and stratification quickly becomes infeasible because there are too many strata. The propensity score models the mechanism of treatment assignment on its own.

**Definition 15.5.1 (Propensity Score)** The conditional probability of receiving the treatment given the covariates $L$, $e(L) = \mathbb{P}(A = 1 \mid L)$, is called the **propensity score**.

**Theorem 15.5.1 (Rosenbaum–Rubin)** (1) Given the propensity score, treatment and covariates are independent: $A \perp L \mid e(L)$. (2) If conditional exchangeability holds given $L$, then it also holds given $e(L)$: $\{Y(0), Y(1)\} \perp A \mid e(L)$.

**Proof** (1) $\mathbb{P}(A = 1 \mid L, e(L)) = \mathbb{P}(A = 1 \mid L) = e(L)$, while $\mathbb{P}(A = 1 \mid e(L)) = \mathbb{E}[\mathbb{P}(A = 1 \mid L) \mid e(L)] = e(L)$; the two are equal, so given $e(L)$ the distribution of $A$ does not depend on $L$. (2) $\mathbb{P}(A = 1 \mid Y(0), Y(1), e(L)) = \mathbb{E}[\mathbb{P}(A = 1 \mid Y(0), Y(1), L) \mid Y(0), Y(1), e(L)] = \mathbb{E}[e(L) \mid Y(0), Y(1), e(L)] = e(L)$, where the second equality uses conditional exchangeability given $L$. $\square$

For two people with the same propensity score, the distributions of the covariates in the treated and control groups are the same (balanced), as if treatment had been randomly assigned within this stratum. A multidimensional adjustment is thus reduced to one dimension: match, stratify or weight on the propensity score. In an observational study $e(L)$ is unknown and is usually estimated by **logistic regression** ([7.7.14](/7.7.14)). The propensity score cannot solve the problem of unmeasured confounding: it balances only the covariates that enter the model.

### 15.5.2. Three Uses

- Matching: for each treated person, find a control with a close propensity score (often on the logit scale), leaving the pair unmatched if the distance exceeds a caliper (commonly 0.2 times the standard deviation of the logit); then compare the outcomes of the two matched groups, which estimates the ATT. Propensity-score matching is simple and intuitive, but it discards unmatched individuals, and the result depends somewhat on the matching algorithm.
- Stratification: divide the people into five strata by quintiles of the propensity score, compare within each stratum, and average with weights proportional to stratum size. Early results of Cochran showed that five strata usually remove about 90% of the bias due to the covariates.
- Weighting: see below.

**Definition 15.5.2 (Inverse Probability Weighting)** Using the weights $w_i = 1/\hat e(L_i)$ for the treated and $w_i = 1/(1 - \hat e(L_i))$ for the controls, compare the weighted means of the outcomes in the two groups,

$$
\widehat{\mathrm{ATE}}_{\mathrm{IPW}} = \frac{\sum_{A_i = 1} w_i Y_i}{\sum_{A_i = 1} w_i} - \frac{\sum_{A_i = 0} w_i Y_i}{\sum_{A_i = 0} w_i},
$$
which is called **inverse probability weighting** (IPW). It is the sample version of the second expression in Theorem 15.3.2 (normalized here by the sum of the weights).

Weighting constructs a "pseudo-population": each treated person stands for the people with the same covariates who were unlikely to be treated. Treated people with a propensity score near 0 (or controls with a score near 1) receive huge weights, a few individuals dominate the whole estimate, and the variance rises sharply; this is how positivity shows up in finite samples. Common remedies are truncating the weights (setting weights above some percentile equal to that percentile); dropping individuals with extreme propensity scores; or switching to overlap weights $w_i = 1 - \hat e(L_i)$ (treated) and $\hat e(L_i)$ (controls), which estimate the average effect in "the part of the population for whom both choices are common". The weights are bounded, and when the propensity score is estimated by logistic regression, the weighted mean of every covariate in the model is exactly equal in the two groups.

### 15.5.3. Balance Diagnostics

The quality of a propensity score is judged not by how well it predicts treatment (a high AUC means the two groups differ a lot and overlap little, which is not good) but by whether it balances the covariates between the two groups.

**Definition 15.5.3 (Standardized Mean Difference)** The **standardized mean difference** (SMD) of a covariate $x$ between the two groups is $(\bar x_1 - \bar x_0)/\sqrt{(s_1^2 + s_0^2)/2}$; after weighting or matching, the means are the weighted or matched ones, and the denominator keeps the unadjusted standard deviations.

The SMD does not depend on the sample size (unlike the $p$-value of a test), and $\lvert\mathrm{SMD}\rvert < 0.1$ is commonly used as the criterion for good balance. Balance diagnostics are the only part of a propensity-score analysis that can be checked against the data: if imbalance remains after weighting or matching, modify the propensity-score model (add squared terms or interactions) or switch to another method, and this step does not look at the outcome, which avoids "cherry-picking results".

### 15.5.4. Maternal Smoking and Birth Weight

**Example 15.5.1** Among the 189 mothers in birthwt, a logistic regression was used to estimate the propensity score for smoking, with covariates age, weight at the last menstrual period, race (two dummy variables), previous preterm labor, history of hypertension, uterine irritability and whether the mother visited a physician in the first trimester (ftv ≥ 1): all characteristics determined before smoking during this pregnancy (or unaffected by it). The $c$-statistic of the propensity score is 0.77: the characteristics of smokers and nonsmokers differ considerably, chiefly race ("other" race mothers rarely smoke; unadjusted SMD −0.72) and previous preterm labor (SMD 0.37).

| Method | Effect of smoking on birth weight / g | 95% interval | Target of estimation |
|---|---|---|---|
| Crude difference ([7.7.7](/7.7.7)) | $-284$ | $(-488, -80)$ | — |
| Regression adjustment (8 covariates) | $-323$ | $(-516, -116)$ | ATE (if the model is correct) |
| Propensity-score quintile stratification | $-328$ | $(-485, -31)$ | ATE |
| Propensity-score matching (52 pairs) | $-377$ | $(-684, -69)$ | ATT |
| IPW | $-148$ | $(-392, 98)$ | ATE |
| IPW, weights truncated at the 1st and 99th percentiles | $-210$ | $(-433, 0)$ | ATE (approximately) |
| Overlap weights | $-325$ | $(-524, -110)$ | Average effect in the overlap population |

The intervals are percentile bootstrap intervals (2000 resamples, re-estimating the propensity score each time), except for matching (a paired $t$ interval of the 52 pair differences).

Most methods give an effect of about −320 to −380 g, roughly consistent with the analysis of covariance in [7.7.12](/7.7.12) Example 12.6.1 (−400 g). Untruncated IPW is an exception (−148 g). Diagnostics show why: one smoking mother of "other" race, weighing 250 lb and with 6 first-trimester visits, has a propensity score of only 0.023 and a weight of 42.8, and her baby weighs 3303 g; she alone accounts for 18% of the total weight of the 74 smokers, and the **effective sample size** $(\sum w_i)^2/\sum w_i^2$ of the smoking group is only 18.9. After IPW the SMD for weight is 0.65, worse than before weighting (−0.09). After truncating the weights all SMDs are within 0.25, and overlap weights balance all covariates exactly. Matching found partners for only 52 smokers (the other 22 had no control within the caliper), and the two matched groups still have SMDs of 0.3 for age and history of hypertension.

![Propensity score of maternal smoking (189 cases, Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt), estimated by logistic regression on age, weight, race, previous preterm labor, history of hypertension, uterine irritability and first-trimester visits. A: distributions of the propensity score for smokers (orange, upward) and nonsmokers (blue, downward); smokers with a propensity score above 0.8 have almost no comparable nonsmokers. B: standardized mean differences of the covariates: unadjusted (gray), inverse probability weighting (orange), weights truncated at the 1st and 99th percentiles (light orange), overlap weights (green, exactly balanced by construction); the light band is |SMD| < 0.1](./plots/propensity.py)

![Different estimates of the effect of smoking on birth weight (189 cases, Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt), adjusting for the same 8 covariates as in the propensity-score model: difference in means (g) and its 95% interval. All intervals are percentile bootstrap intervals (2000 resamples, refitting the propensity-score model each time) except matching (paired t interval of 52 caliper-matched pairs). Matching estimates the effect among smokers, overlap weights estimate the effect in the population for whom both choices are common, and the other methods estimate the average effect in the whole sample](./plots/ate-estimates.py)

This example illustrates several practical points about propensity-score methods: (1) differences between methods should first be explained by looking at balance diagnostics and the weight distribution, rather than by picking the "significant" one; (2) with a small sample and poor overlap, IPW is unstable, and truncation or overlap weights buy stability at the price of changing the target of estimation; (3) all the methods adjust only for measured covariates: the mothers' socioeconomic status, alcohol use and nutrition were not measured, and if they affect both smoking and birth weight, all of these estimates are biased. The next section discusses this possibility quantitatively.

## 15.6. Sensitivity Analysis for Unmeasured Confounding

### 15.6.1. Fisher and Cornfield

In the 1950s, studies such as that of Doll and Hill had already shown that smokers' risk of lung cancer was more than 10 times that of nonsmokers. Fisher (1958) proposed the "constitutional hypothesis": perhaps some inherited constitution both predisposes people to smoke and makes them prone to lung cancer, and smoking itself is harmless. This cannot be ruled out logically with observational data. The answer of Cornfield et al. (1959) was quantitative: for a binary hidden factor $U$ to fully explain the RR (about 9) between smoking and lung cancer, its prevalence among smokers would have to be at least 9 times that among nonsmokers. No characteristic known at the time had an association anywhere near that strong, and the factor would also have to explain a series of facts such as the dose-response relationship and the fall in risk after quitting ([7.7.13](/7.7.13) Section 13.7).

### 15.6.2. The E-Value

Ding and VanderWeele (2016) generalized Cornfield's argument to take into account the strength of association of the unmeasured confounder with both the exposure and the outcome. Let $\mathrm{RR}_{EU}$ be the maximum prevalence ratio of the unmeasured confounder $U$ between exposed and unexposed (the largest such ratio if $U$ is multivalued), and $\mathrm{RR}_{UD}$ the maximum risk ratio of $U$ for the outcome (within strata of the exposure).

**Theorem 15.6.1 (Bound on Confounding)** Under this setting, the ratio of the observed RR to the true causal RR does not exceed

$$
B = \frac{\mathrm{RR}_{EU}\,\mathrm{RR}_{UD}}{\mathrm{RR}_{EU} + \mathrm{RR}_{UD} - 1}.
$$
Therefore, for $U$ to explain an observed $\mathrm{RR}_{\mathrm{obs}} > 1$ entirely as no effect, it must satisfy $B \ge \mathrm{RR}_{\mathrm{obs}}$.

**Definition 15.6.1 (E-Value)** The value $E$ for which $\mathrm{RR}_{EU} = \mathrm{RR}_{UD} = E$ gives exactly $B = \mathrm{RR}_{\mathrm{obs}}$,

$$
E = \mathrm{RR}_{\mathrm{obs}} + \sqrt{\mathrm{RR}_{\mathrm{obs}}(\mathrm{RR}_{\mathrm{obs}} - 1)},
$$
is called the **E-value** of the estimate. When $\mathrm{RR}_{\mathrm{obs}} < 1$, take the reciprocal first. The E-value computed for the confidence limit closer to 1 gives the strength of confounding needed to make the interval include 1.

The meaning of $E$ is that an unmeasured confounder must be associated with both the exposure and the outcome by a factor of at least $E$ (beyond the covariates already adjusted for) to fully explain the observed association; weaker confounding cannot. The E-value does not say whether such a confounder exists; it replaces the unanswerable question "is there unmeasured confounding?" with the question "how strong would unmeasured confounding have to be?", which can be judged using domain knowledge.

**Example 15.6.1** (1) In the British doctors cohort the lung-cancer rate ratio for current smokers is 14.6 ([7.7.13](/7.7.13) Example 13.7.1), so $E = 14.6 + \sqrt{14.6 \times 13.6} = 28.7$: an unmeasured factor would have to differ by nearly 29-fold in the proportion who smoke and at the same time by nearly 29-fold in lung cancer risk to explain this association; for those smoking 25 or more cigarettes per day the rate ratio of 24.5 corresponds to $E = 48.5$. This is exactly the modern form of Cornfield's argument. (2) In birthwt, the adjusted OR for the effect of smoking on low birth weight is 2.36 (1.07–5.22, [7.7.14](/7.7.14) Example 14.4.1). Low birth weight is not rare (31%), so we first use the approximation $\mathrm{RR} \approx \sqrt{\mathrm{OR}}$ (recommended by VanderWeele 2017) to convert: $\mathrm{RR} \approx 1.54$, $E = 2.44$; the lower limit 1.07 converts to 1.03, $E = 1.22$. That is, an unmeasured factor (socioeconomic status, for example) associated with both smoking and low birth weight by a factor of only about 1.2 would suffice to make the interval include 1, and confounding of this strength is entirely possible: these data support the harmfulness of smoking, but alone they cannot strongly rule out unmeasured confounding.

![Sensitivity to an unmeasured confounder U. For an observed risk ratio RR, a binary confounder can fully explain the association if and only if RR_EU × RR_UD /(RR_EU + RR_UD − 1) ≥ RR, where RR_EU is the prevalence ratio of U between exposed and unexposed and RR_UD is the risk ratio of U for the outcome (Ding and VanderWeele 2016). The curves give the joint strengths just needed to explain RR = 1.54 (the square root of the adjusted OR of 2.36 for smoking and low birth weight in birthwt, as an approximation to the RR), RR = 3 and RR = 14.6 (the lung-cancer rate ratio of current smokers among British doctors); confounding to the upper right of a curve suffices to explain the association; the dots are the E-values at equal strengths: 2.44, 5.45 and 28.7](./plots/evalue.py)

### 15.6.3. Negative Controls

Another way to check for unmeasured confounding is the negative control: find an outcome that is known not to be affected by the exposure but has the same confounding structure (a negative control outcome), or an "exposure" that is known not to affect the outcome but has the same confounding structure as the exposure (a negative control exposure). For example, in studying the effect of influenza vaccination on mortality in older adults, if vaccinated people already have much lower mortality before the influenza season begins, "healthier people are more willing to be vaccinated" is a strong confounder, and the protective effect during the season is overestimated. In the study of smoking and birth weight, paternal smoking can serve as a negative control exposure: if the association of paternal smoking with birth weight (adjusting for maternal smoking) is as strong as that of maternal smoking, it suggests a shared family factor rather than an intrauterine exposure effect.

## 15.7. Instrumental Variables and Mendelian Randomization

### 15.7.1. Instrumental Variables

Sometimes one can find a "natural experiment": a variable that affects the exposure, is unrelated to the confounders, and affects the outcome only through the exposure.

**Definition 15.7.1 (Instrumental Variable)** A variable $Z$ is called an **instrumental variable** for the effect of exposure $A$ on outcome $Y$ if: (1) $Z$ is associated with $A$ (relevance); (2) $Z$ is independent of all unmeasured confounders of the $A$–$Y$ relationship (independence); and (3) $Z$ affects $Y$ only through $A$ (exclusion restriction).

**Formula 15.7.1 (Wald Estimator)** If the effect of $A$ on $Y$ is linear and the same for everyone,

$$
\hat\beta_{\mathrm{IV}} = \frac{\widehat{\operatorname{Cov}}(Z, Y)}{\widehat{\operatorname{Cov}}(Z, A)};
$$
for a binary $Z$ this is $\dfrac{\bar Y_{Z=1} - \bar Y_{Z=0}}{\bar A_{Z=1} - \bar A_{Z=0}}$: the effect of the instrument on the outcome divided by the effect of the instrument on the exposure.

Conditions (2) and (3) cannot be tested with the data and can only be argued. Random assignment in a randomized trial is itself an instrumental variable: when patients are assigned to a group ($Z$) but do not necessarily take the drug ($A$), the intention-to-treat analysis ([7.7.18](/7.7.18)) estimates the effect of $Z$ on $Y$, and the Wald estimator converts it into the effect of actually taking the drug (among compliers). When the association between instrument and exposure is weak (a weak instrument), the denominator of the Wald estimator is close to 0, the variance is large, and the estimator is extremely sensitive to slight violations of conditions (2) and (3).

### 15.7.2. Mendelian Randomization

**Mendelian randomization** ([7.4.25](/7.4.25)) uses genetic variants that affect the exposure as instruments: alleles are randomly allocated at meiosis (the law of segregation in [7.4.2](/7.4.2)) and are largely unrelated to postnatal lifestyle and socioeconomic status, so condition (2) is approximately satisfied; they are also not changed by disease in return, which rules out reverse causation. The main threats are violation of condition (3) (horizontal pleiotropy: the variant affects the outcome through other pathways), population stratification (ancestry differences in [7.4.25](/7.4.25) that affect both allele frequency and the outcome) and weak instruments. The Wald ratio for a single variant, inverse-variance-weighted pooling of several variants and pleiotropy-robust methods are covered in [7.4.25](/7.4.25) and are not repeated here.

An example related to the theme of this chapter is the use of variants in the *CHRNA5* region, which affect the amount smoked, to study the effect of smoking: they affect only how much smokers smoke and should have no effect in never smokers, and the latter can serve as a negative control to test the exclusion restriction.

## 15.8. Reporting and Robustness of Observational Studies

The causal conclusions of an observational study ultimately depend on assumptions that cannot be fully tested, so the point of reporting is to let readers judge these assumptions.

- State the question first: what the interventions for treatment and control are, who the target population is, and whether the ATE or the ATT is estimated. A useful practice is to imagine a randomized trial that would answer the same question (the target trial) and to design the analysis of the observational data to emulate it as closely as possible: specify the eligibility criteria, "time zero" (the start of exposure aligned with the start of follow-up), the definition of the treatment and the end of follow-up. Many biases in observational studies come from misalignment at time zero (for example, immortal time bias from counting only people who "survived until starting the drug").
- Draw the causal diagram and justify the choice of the adjustment set (Theorem 15.4.1); do not adjust for variables that come after the exposure.
- Report the balance diagnostics and the weight distribution (Section 15.5.3), not just the final estimate.
- Sensitivity analyses: the E-value (Definition 15.6.1), negative controls (Section 15.6.3), different adjustment sets and model specifications, different propensity-score methods; are the conclusions robust to these choices?
- Follow reporting guidelines: STROBE (the reporting guideline for observational studies) lists the items to be reported for cohort, case-control and cross-sectional studies, including study design, selection of participants, definitions of variables, handling of bias, sample size, missing data and sensitivity analyses.

Finally, causal conclusions rarely come from a single study. The conclusion that smoking causes lung cancer rests on the mutual corroboration of case-control studies, cohort studies, dose-response, the change in risk after quitting, animal experiments and molecular mechanisms (the Bradford Hill criteria in [7.7.13](/7.7.13)), and on the robustness of this evidence under Cornfield-style sensitivity analysis.

## 15.9. Computing with Python

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# FEV: which adjustment set (Example 15.4.1)
fev = pd.read_csv("fev.csv")
for f in ["fev ~ smoke", "fev ~ smoke + age", "fev ~ smoke + age + sex", "fev ~ smoke + age + sex + height"]:
    m = smf.ols(f, fev).fit()
    print(f, m.params["smoke"].round(3), m.conf_int().loc["smoke"].round(3).values)

# birthwt: propensity score and balance (Example 15.5.1)
bw = pd.read_csv("birthwt.csv")
bw = bw.assign(ptd=(bw.ptl > 0).astype(int), black=(bw.race == 2).astype(int),
               other=(bw.race == 3).astype(int), ftv1=(bw.ftv > 0).astype(int))
cov = ["age", "lwt", "black", "other", "ptd", "ht", "ui", "ftv1"]
ps = smf.glm("smoke ~ " + " + ".join(cov), bw, family=sm.families.Binomial()).fit().predict(bw)
t, y = bw.smoke.to_numpy(), bw.bwt.to_numpy(float)

def smd(x, w):
    m1, m0 = np.average(x[t == 1], weights=w[t == 1]), np.average(x[t == 0], weights=w[t == 0])
    return (m1 - m0) / np.sqrt((x[t == 1].var(ddof=1) + x[t == 0].var(ddof=1)) / 2)

def wdiff(w):
    return np.average(y[t == 1], weights=w[t == 1]) - np.average(y[t == 0], weights=w[t == 0])

w_ipw = np.where(t == 1, 1 / ps, 1 / (1 - ps))
w_trunc = np.clip(w_ipw, *np.quantile(w_ipw, [0.01, 0.99]))
w_overlap = np.where(t == 1, 1 - ps, ps)
for name, w in [("none", np.ones_like(y)), ("IPW", w_ipw), ("truncated", w_trunc), ("overlap", w_overlap)]:
    print(name, round(wdiff(w)), [round(smd(bw[c].to_numpy(float), w), 2) for c in cov])
wt = w_ipw[t == 1]
print(w_ipw.max(), wt.sum() ** 2 / (wt ** 2).sum())   # largest weight 42.8; effective n of smokers 18.9

# E-value (Definition 15.6.1)
def e_value(rr):
    rr = 1 / rr if rr < 1 else rr
    return rr + np.sqrt(rr * (rr - 1))
print(e_value(14.6), e_value(np.sqrt(2.36)), e_value(np.sqrt(1.07)))   # 28.7, 2.44, 1.22
```

Propensity-score matching can be done with packages such as `causalml` and `DoWhy`, or written by hand in a few lines as above (nearest neighbor, caliper, without replacement); for bootstrap intervals the propensity score must be re-estimated in every resample.

## Summary

- Noncausal explanations of an association: chance, confounding, reverse causation, selection bias; a group-level association cannot be carried over to individuals (the **ecological fallacy**, Definition 15.1.1; Robinson 1950: −0.53 versus +0.12).
- **Potential outcomes** (Definition 15.2.1) define the causal effect: $\mathrm{ATE} = \mathbb{E}[Y(1) - Y(0)]$, and the $\mathrm{ATT}$ averages only over the treated (Definition 15.2.2); only one potential outcome can be observed per person; the intervention must be well defined (consistency, Definition 15.2.3).
- Identification conditions (Definition 15.3.1): consistency, **exchangeability** (guaranteed by randomization through design, Theorem 15.3.1), conditional exchangeability and **positivity** (which an observational study must argue for); under these conditions standardization (the g-formula) and inverse probability weighting identify the ATE (Theorem 15.3.2).
- **Causal diagrams** (Definition 15.4.1): the fork, chain and collider structures; the **backdoor criterion** (Theorem 15.4.1) determines the adjustment set: adjust for confounders, not for **mediators** or **colliders** (Definition 15.4.2). FEV: adjusting for age and sex gives a total effect of −0.154 L (−7.1%); additionally adjusting for height changes this to −4.5% (Example 15.4.1). Collider bias: Berkson's bias (Example 15.4.2) and the birth weight paradox (Example 15.4.3).
- The **propensity score** (Definition 15.5.1) balances covariates (Theorem 15.5.1); matching (ATT), stratification, **inverse probability weighting** (Definition 15.5.2) and overlap weights; look at the standardized mean difference (Definition 15.5.3) and the weight distribution, not at the AUC of the propensity score. birthwt: maternal smoking lowers birth weight by about 320–380 g; untruncated IPW is pulled to −148 g by a single individual with weight 42.8 (Example 15.5.1).
- Unmeasured confounding: Cornfield's inequality, the bound on confounding (Theorem 15.6.1) and the **E-value** (Definition 15.6.1): lung cancer $E = 28.7$, birthwt low birth weight $E = 2.44$ (lower limit 1.22, Example 15.6.1); negative controls.
- **Instrumental variables** (Definition 15.7.1) and the Wald estimator (Formula 15.7.1); **Mendelian randomization** uses genetic variants as instruments ([7.4.25](/7.4.25)).
- Reporting: the target trial, the causal diagram, balance diagnostics, sensitivity analyses, STROBE; causal conclusions come from the mutual corroboration of several kinds of evidence.

## Questions

1. In Example 15.2.1, suppose the physician instead decides by coin toss who gets the drug, and it happens that patients 1, 3, 5 and 7 receive it. What is the observed difference in mortality between the two groups? What does its difference from the ATE show? What is the expected value of the difference over repeated random assignments?

   **Answer** The drug group (1, 3, 5, 7) has observed $Y(1)$ equal to 0, 0, 0, 1, a mortality of $1/4$; the no-drug group (2, 4, 6, 8) has observed $Y(0)$ equal to 0, 1, 1, 1, a mortality of $3/4$; the difference is $-0.5$, whereas the ATE is $+0.125$. A single random assignment among 8 people can still produce a large difference between the groups (here it happened to put the people with the better prognosis into the drug group); this is random error, reflected in the confidence interval. What randomization guarantees is unbiasedness: over all $\binom{8}{4} = 70$ equally likely assignments, the average of the difference is exactly the ATE $= 0.125$ (each person is in the drug group and in the no-drug group with probability 1/2, so the expected means of the two groups are $\mathbb{E}[Y(1)]$ and $\mathbb{E}[Y(0)]$ respectively).

2. Draw the causal diagram for the following scenario and decide which variables should be adjusted for to estimate the total effect of $A$ on $Y$: $A$ = taking folic acid during pregnancy, $Y$ = neural tube defect; $L_1$ = the mother's education (affecting both folic acid supplementation and dietary folate intake, the latter affecting $Y$); $M$ = serum folate level in early pregnancy; $C$ = whether an ultrasound was done at the prenatal visit (affected by $Y$ and also by $L_1$).

   **Answer** Edges: $L_1 \to A$, $L_1 \to$ diet $\to Y$ (or simply $L_1 \to Y$), $A \to M \to Y$, $Y \to C$, $L_1 \to C$. Backdoor path: $A \leftarrow L_1 \to Y$, so $L_1$ (or dietary folate) needs to be adjusted for. $M$ is a mediator; adjusting for it would adjust away the main pathway of the effect of folic acid, so it is not adjusted for when estimating the total effect. $C$ is a descendant of $Y$ and a collider between $Y$ and $L_1$; conditioning on it (for example analyzing only the pregnant women who had an ultrasound) introduces bias, so it should be neither adjusted for nor restricted on. Adjustment set: $\{L_1\}$.

3. Prove that for a binary treatment, the (unnormalized) inverse probability weighting estimator $\frac1n\sum_i \frac{A_iY_i}{e(L_i)} - \frac1n\sum_i\frac{(1 - A_i)Y_i}{1 - e(L_i)}$ is an unbiased estimator of the ATE when the propensity score is known and the identification conditions hold.

   **Answer** By linearity it suffices to show $\mathbb{E}[AY/e(L)] = \mathbb{E}[Y(1)]$. By consistency $AY = AY(1)$. Then $\mathbb{E}[AY(1)/e(L)] = \mathbb{E}\{\mathbb{E}[A \mid Y(1), L]\,Y(1)/e(L)\}$; by conditional exchangeability, $\mathbb{E}[A \mid Y(1), L] = \mathbb{P}(A = 1 \mid L) = e(L)$, so this equals $\mathbb{E}[Y(1)]$. Positivity guarantees $e(L) > 0$, so the division makes sense. The control group is handled in the same way. (In practice $e$ is estimated and the normalized form is often used, in which case the estimator is consistent rather than exactly unbiased.)

4. A study reports an adjusted RR = 0.70 (95% interval 0.55–0.89) for coffee drinking and type 2 diabetes. Compute the E-values for the point estimate and for the upper limit of the interval, and interpret them.

   **Answer** Since $\mathrm{RR} < 1$, take the reciprocal: $1/0.70 = 1.429$, $E = 1.429 + \sqrt{1.429 \times 0.429} = 1.429 + 0.783 = 2.21$. For the upper limit 0.89 → $1/0.89 = 1.124$, $E = 1.124 + \sqrt{1.124 \times 0.124} = 1.124 + 0.373 = 1.50$. An unmeasured confounder would need to be associated with coffee drinking and with diabetes by at least 2.2-fold each to fully explain the point estimate, and 1.5-fold would suffice to make the interval include 1. Other aspects of diet and lifestyle (physical activity, general health consciousness) may well be associated with both by 1.5-fold, so the conclusion is moderately sensitive to unmeasured confounding.

5. Data from a hospital show that among patients hospitalized for heart failure, obese patients have lower mortality than normal-weight patients (the "obesity paradox"). Give at least two noncausal explanations and say what structure in a causal diagram each corresponds to.

   **Answer** (1) Collider bias (selection): hospitalization is a common effect of obesity and of other serious causes (such as more severe cardiomyopathy, cancer, cachexia); among hospitalized patients, those of normal weight are more likely to be there because of a more dangerous cause, so conditioning on hospitalization introduces a negative association between obesity and these causes ($\text{obesity} \to \text{hospitalization} \leftarrow U \to \text{death}$). (2) Reverse causation: severe disease causes weight loss, so the "normal weight" group is contaminated with the sickest patients who are already thin ($\text{death risk} \leftarrow \text{disease severity} \to \text{weight}$, with weight a consequence of disease). (3) Confounding: age (older heart-failure patients have lower BMI and higher mortality). One should measure weight before hospitalization, exclude early events, stratify by cause, and study the question in a population cohort rather than among hospitalized patients.

6. In Example 15.5.1 the $c$-statistic of the propensity score is 0.77. A colleague suggests adding more variables strongly associated with smoking (such as whether the father smokes and household income) to bring the $c$-statistic up to 0.95 and "make the propensity score more accurate". How do you respond?

   **Answer** The purpose of the propensity score is to balance confounders, not to predict treatment. The variables to add are those that affect both smoking and birth weight (household income is very likely such a confounder and should be added); variables that affect only smoking and not birth weight (instrument-like variables; the father's smoking is of this kind if it acts only through the mother's smoking) do not reduce bias but make the propensity score more extreme, the overlap worse and the weights larger, which increases variance and, in the presence of unmeasured confounding, can amplify bias. A $c$-statistic of 0.95 means the two groups hardly overlap, positivity is in effect destroyed, IPW will be extremely unstable and matching will fail to find partners for most people. The propensity-score model should be evaluated by balance diagnostics (SMD), not by the $c$-statistic.

7. A study uses a genetic variant associated with LDL cholesterol as an instrument to estimate the effect of LDL on coronary heart disease. The variant raises LDL by 0.20 mmol/L on average and raises the log odds of coronary heart disease by 0.10 (the two estimates come from different large samples). Find the Wald ratio estimate and explain when this estimate would be biased.

   **Answer** $\hat\beta = 0.10/0.20 = 0.50$: each 1 mmol/L increase in LDL raises the log odds of coronary heart disease by 0.50 (OR $\mathrm{e}^{0.5} = 1.65$). Sources of bias: (1) pleiotropy: the variant affects coronary heart disease through other pathways (such as triglycerides or inflammation), violating the exclusion restriction; (2) population stratification: populations of different ancestry in the sample differ in both the variant frequency and coronary heart disease risk, violating independence; (3) linkage disequilibrium: the variant is correlated with another nearby variant that affects coronary heart disease; (4) weak instruments: when the sample is not large, the estimate is biased (toward the null in a two-sample design, toward the observational estimate in a one-sample design). In addition, a genetic variant represents a lifelong difference in LDL, whose effect may be larger than that of a short-term lipid-lowering treatment in adulthood, so the interpretation should attend to the definition of the intervention (consistency).

8. Are the following statements true? Explain. (a) "Randomized controlled trials do not need causal diagrams." (b) "The more variables you adjust for, the closer the estimate is to the causal effect." (c) "An E-value greater than 2 shows that the conclusion is reliable." (d) "Propensity-score methods can deal with unmeasured confounding."

   **Answer** (a) Largely true: randomization guarantees exchangeability, and comparing the intention-to-treat groups needs no adjustment. But causal diagrams may still be needed in trials: when loss to follow-up and adherence are influenced by treatment and prognosis, analyzing only completers or analyzing by the treatment actually taken conditions on a post-treatment variable (which can introduce collider bias). (b) False. Adjusting for a mediator adjusts away part of the effect, adjusting for a collider introduces bias, and adjusting for a variable that affects only the treatment increases variance (Question 6). The adjustment set should be chosen by the backdoor criterion. (c) Not necessarily. The E-value says only how strong unmeasured confounding would have to be; whether that is "large enough" depends on the strength of confounding known in the field; and the E-value says nothing about other biases (selection bias, measurement error) or model specification. (d) False. The propensity score balances only the (measured) covariates that enter the model, and is as powerless against unmeasured confounding as regression adjustment.

9. (Design question) You want to use a large health-insurance database to study whether statins reduce the risk of dementia in older adults. Design the analysis following the target trial approach and list the main risks of bias.

   **Answer** Target trial: enroll people aged 65 or older with no dementia and no statin use in the past year; the treatment is starting a statin versus not starting; time zero is the day the drug is started (for controls, a matched calendar date in the same period); the outcome is a diagnosis of dementia during follow-up; compare the intention-to-treat cumulative incidence. Observational emulation: a new-user design (including only those who newly start the drug, to avoid prevalent-user bias); exposure and follow-up begin at the same moment, to avoid immortal time bias; estimate a propensity score from baseline age, sex, cardiovascular disease, diabetes, hypertension, number of medications, number of visits and so on, and check balance; treat death as a competing risk ([7.7.16](/7.7.16)). Main biases: the healthy-user effect (people who are willing to start and adhere to preventive medication are healthier overall, which is negatively associated with dementia risk), checked with negative control outcomes (such as hip fracture or accidental injury); reverse causation (people in early cognitive decline are less likely to be started on preventive medication), handled by excluding diagnoses made in the first 1–2 years of follow-up; misclassification of the dementia diagnosis; unmeasured confounding (education, physical activity), handled by reporting the E-value.

10. Using the standardization formula of Theorem 15.3.2, compute from the British doctors data of [7.7.13](/7.7.13) Example 13.5.1 the coronary-death rates "if everyone smoked" and "if no one smoked" (using the age distribution of all person-years as the standard), and state what assumptions a causal interpretation of this calculation requires.

    **Answer** Take the age distribution of all person-years as $\mathbb{P}(L = l)$: 0.392, 0.297, 0.189, 0.084, 0.037. "Everyone smokes": $\sum_l r_{1l}\mathbb{P}(L = l) = 427$ per 100,000 person-years; "no one smokes": 301 per 100,000 person-years (this is the directly standardized rate of Example 13.5.2); the causal rate ratio is 1.42 and the rate difference is 126 per 100,000 person-years. A causal interpretation requires: (1) conditional exchangeability: within the same age group, the coronary risks of smokers and nonsmokers differ only because of smoking (no other confounding, such as social class or diet; these data adjust only for age); (2) positivity: every age group contains both smokers and nonsmokers (satisfied); (3) consistency: smoking is a well-defined treatment (the amount smoked differs, and "smoking" includes several versions). Because the rate ratio varies strongly with age (effect modification), this average rate ratio depends on the standard population used.
