---
title: Longitudinal Data, Repeated Measures and Mixed Models
description: Structure of repeated measures and within-subject correlation, and the consequences of ignoring it; summary-statistic methods; random-effects one-way ANOVA, variance components and the intraclass correlation coefficient, assay reproducibility and the coefficient of variation; linear mixed models (random intercepts and slopes, REML, shrinkage and best linear unbiased prediction); generalized estimating equations and marginal models; crossover designs, washout periods and carryover effects; clustered data and the design effect; missing-data mechanisms (MCAR, MAR, MNAR) and multiple imputation; measurement error and regression dilution. Illustrated by the sleepstudy sleep-deprivation experiment, between-run variability in DNase ELISA, and repeated estradiol assays in the Nurses' Health Study.
source_hash: a525e3d34122
---

So far almost every method has assumed that observations are independent. Biomedical data, however, often come in groups: reaction time measured every day for 10 days in the same person, replicate wells on the same plate, many cells from the same mouse, the two ears of the same child, patients of the same clinic. Observations in the same group resemble one another, and [7.7.12](/7.7.12) has already shown that treating them as independent samples inflates the type I error rate several-fold (**pseudoreplication**). This chapter deals with this structure head-on: it first explains the sources and consequences of within-subject correlation in **longitudinal data** ([7.7.1](/7.7.1) Section 1.4), and then presents three correct kinds of analysis: the summary-statistic method that compresses each person into one number, the mixed model that writes individual differences as random variables, and generalized estimating equations that model only the mean and estimate standard errors robustly. Random-effects analysis of variance splits the total variation into a "between subjects" and a "within subjects" part, and at the same time answers a question that is often asked in the laboratory: how reproducible is an assay? The chapter also treats three practical problems of longitudinal studies: the crossover design in which the same person receives two treatments in sequence, missing data during follow-up, and the regression dilution caused by measurement error in the exposure. The running examples are sleepstudy (the 6 subjects shown in the figure in [7.7.1](/7.7.1); here all 18 are used) and, from laboratory assays, thread 4: the 11 independent runs of the DNase ELISA ([7.7.11](/7.7.11) has fitted a standard curve for each run). Two-way analysis of variance and factor-effect models are in [3.3.14](/3.3.14), and the EM algorithm and the likelihood with missing data in [3.5.6](/3.5.6); linear mixed models in population genetics with a relatedness matrix as covariance are in [7.8.13](/7.8.13).

## 17.1. The Structure of Repeated Measures

### 17.1.1. Within-Subject Correlation

**Definition 17.1.1 (Repeated Measures)** Data obtained by measuring the same variable several times on the same experimental unit (individual, animal, culture dish) at different times or under different conditions are called **repeated measures**. Repeated measures arranged in time order and aimed at describing change are longitudinal data.

The value of repeated measures is that each person serves as his or her own control: differences between individuals (baseline reaction speed, body size, genetic background) cancel when "change" is compared, as in a paired design ([7.7.7](/7.7.7) Definition 7.1.1). The price is that observations on the same individual are correlated. A simple model shows where the correlation comes from: let the $j$th measurement on the $i$th person be

$$
y_{ij} = \mu + b_i + \varepsilon_{ij}, \qquad b_i \sim \mathcal{N}(0, \sigma_b^2), \quad \varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2),
$$
where $b_i$ is this person's persistent deviation and $\varepsilon_{ij}$ is the fluctuation of each measurement, the two being independent. Two measurements on the same person share $b_i$,

$$
\operatorname{Cov}(y_{ij}, y_{ij'}) = \sigma_b^2, \qquad \operatorname{Corr}(y_{ij}, y_{ij'}) = \frac{\sigma_b^2}{\sigma_b^2 + \sigma^2},
$$
while measurements on different people are independent. The larger the differences between individuals, the more alike the observations on the same person. Longitudinal data have another source of correlation: measurements close in time are more correlated than those far apart (autocorrelation), as for the displacements in adjacent frames in single-particle tracking (the mean squared displacement in [7.6.23](/7.6.23)).

### 17.1.2. Consequences of Ignoring Correlation

**Example 17.1.1 (Sleep Deprivation)** sleepstudy records the mean daily reaction time of 18 subjects over 10 days of sleeping only 3 hours per night (day 0 is the baseline) (Belenky et al. 2003), 180 observations in all. Treating the 180 points as an independent sample in an ordinary least squares regression:

$$
\hat y = 251.4 + 10.47 \times \text{day}, \qquad \mathrm{SE}(\hat\beta_1) = 1.24.
$$
There is nothing wrong with the slope estimate, but the standard error is wrong: it assumes 180 independent people, whereas the information actually comes from 18 people. Different people react at different speeds and also deteriorate at different rates (panel A of the figure below), and the uncertainty of the slope comes mainly from "slope differences between people", which OLS treats as noise in 180 independent residuals. The correct analysis (Sections 17.2 and 17.4) gives a standard error of 1.55.

:::

The direction of the error when correlation is ignored depends on what is being compared:

| Effect compared | Example | Standard error when correlation is ignored |
|---|---|---|
| Between individuals (each person belongs to one group) | Mean lung function of smokers and nonsmokers, each measured 3 times | Too small: 3 measurements are treated as 3 people (pseudoreplication) |
| Within individuals (each person goes through all conditions) | Before and after treatment in the same person, change over time | The intercept-related part is too large (individuals are not used as their own controls), but if individuals' slopes differ, the standard error of the slope is too small |

The rule of thumb is that whenever the unit of observation is not the **experimental unit** ([7.7.12](/7.7.12) Definition 12.7.3), the methods of this chapter are needed.

## 17.2. The Summary-Statistic Method

The simplest and entirely correct method is first to compress each person's repeated measurements into one meaningful number and then to carry out an ordinary one-sample or two-sample analysis on these numbers.

| Research question | Summary per person |
|---|---|
| Speed of change | Slope of the individual regression |
| Total exposure or total response | Area under the curve, AUC (trapezoidal rule) |
| Peak | Maximum and time to peak ($C_{\max}$, $t_{\max}$ in pharmacokinetics) |
| Change from before to after treatment | Last value minus baseline, or mean over follow-up minus baseline |

**Example 17.2.1** Fitting a straight line of reaction time on day separately for each of the 18 subjects, the mean slope is 10.47 ms/day with standard deviation 6.56 and standard error $6.56/\sqrt{18} = 1.55$; the one-sample t test gives $t_{17} = 6.77$, $p = 3.3 \times 10^{-6}$. The mean equals the OLS slope (every person was measured on the same days, so the design is balanced), but the standard error is 25% larger than the OLS one: it correctly reflects the slope differences among the 18 people.

:::

The advantages of the summary-statistic method are that it is transparent, makes no assumption about the correlation structure, and has the experimental unit as the unit of analysis, for the same reason as "testing the mean of each mouse" in [7.7.12](/7.7.12). The limitations are: when people are measured different numbers of times, their slopes have different precision but are weighted equally; missing data are handled crudely; between-subject and within-subject variation cannot be estimated at the same time; and it is inconvenient to adjust for time-varying covariates. Mixed models solve these problems, and in a balanced design they give the same inference as the summary-statistic method (Example 17.4.1).

## 17.3. Random-Effects Analysis of Variance

### 17.3.1. Fixed Effects and Random Effects

The one-way analysis of variance of [7.7.12](/7.7.12) compares a few specific groups (three doses, three races); if the experiment were repeated, it would be the same groups again, the interest is in the group means themselves, and the group effects are fixed effects. In another class of problems the groups are drawn at random from a larger population: 5 women, 11 ELISA runs, 20 clinics. We have no interest in "the mean of woman number 3"; what matters is how large the variation between groups is.

**Definition 17.3.1 (Random-Effects Model and Variance Components)** Suppose $k$ groups are drawn at random from a population of groups, and group $i$ has $n$ observations,

$$
y_{ij} = \mu + a_i + \varepsilon_{ij}, \qquad a_i \sim \mathcal{N}(0, \sigma_A^2), \quad \varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2),
$$
with $a_i$ and $\varepsilon_{ij}$ independent. Such a model is called a one-way **random-effects model**, and $\sigma_A^2$ and $\sigma^2$ are called the between-group and within-group **variance components**.

**Formula 17.3.1 (Estimating the Variance Components)** In a balanced design, the expectations of the between-group mean square $\mathrm{MS}_B$ and the within-group mean square $\mathrm{MS}_W$ of the analysis of variance table are

$$
\mathbb{E}(\mathrm{MS}_W) = \sigma^2, \qquad \mathbb{E}(\mathrm{MS}_B) = \sigma^2 + n\sigma_A^2,
$$
so the method-of-moments estimates are $\hat\sigma^2 = \mathrm{MS}_W$ and $\hat\sigma_A^2 = \max\{(\mathrm{MS}_B - \mathrm{MS}_W)/n,\ 0\}$. The statistic $F = \mathrm{MS}_B/\mathrm{MS}_W$ for testing $H_0\colon \sigma_A^2 = 0$ is the same as in the fixed-effects model and follows $F_{k-1,\,k(n-1)}$ under $H_0$. In an unbalanced design, $n$ is replaced by $n_0 = \bigl(N - \sum n_i^2/N\bigr)/(k - 1)$, or REML (Section 17.4.2) is used directly.

The expectation of $\mathrm{MS}_B$ has the extra term $n\sigma_A^2$ because the variance of a group mean $\bar y_i$ is $\sigma_A^2 + \sigma^2/n$, and $\mathrm{MS}_B$ is $n$ times the sample variance of the group means. When $\mathrm{MS}_B < \mathrm{MS}_W$ the moment estimate is negative and is truncated to 0; the REML estimate is nonnegative by construction.

### 17.3.2. The Intraclass Correlation Coefficient

**Definition 17.3.2 (Intraclass Correlation Coefficient)** In the random-effects model, the correlation coefficient between two observations in the same group,

$$
\rho_I = \frac{\sigma_A^2}{\sigma_A^2 + \sigma^2}
$$
is called the **intraclass correlation coefficient** (ICC); it is the proportion of the total variance that is between-group variance. The estimate is $\hat\rho_I = \hat\sigma_A^2/(\hat\sigma_A^2 + \hat\sigma^2)$.

The ICC has two equivalent meanings. As a correlation: the correlation between two observations drawn at random within a randomly chosen group; unlike the ordinary Pearson correlation, the two observations in a group are not labeled "x" and "y" (the two ears of a child, the two members of a twin pair). As a ratio of variances: in reproducibility studies it is the reliability of the assay, the share of the variance of a single measurement that reflects true differences between individuals as opposed to measurement noise. The closer the ICC is to 1, the better a single measurement represents a person's "true level".

### 17.3.3. Reproducibility of an Assay

**Example 17.3.1 (Repeated Estradiol Assays)** To relate serum hormone levels to the risk of breast cancer, the Nurses' Health Study first ran a reproducibility substudy: the blood sample of each of 5 postmenopausal women was split into two portions and sent blind to the same laboratory (data published in Rosner's textbook, units pg/mL):

| Woman | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Portion 1 | 25.5 | 11.1 | 8.0 | 20.7 | 5.8 |
| Portion 2 | 30.4 | 15.0 | 8.1 | 16.9 | 8.4 |

The difference between the two portions increases with the mean (a difference of 4.9 for woman 1 and only 0.1 for woman 3); laboratory measurements often have this kind of error with "standard deviation proportional to the mean", so the analysis is on the log scale. For $\ln$ estradiol, $\mathrm{MS}_B = 0.6644$ (4 degrees of freedom), $\mathrm{MS}_W = 0.0300$ (5 degrees of freedom), $F = 22.1$, $p = 0.0022$.

$$
\hat\sigma_A^2 = \frac{0.6644 - 0.0300}{2} = 0.317, \qquad \hat\rho_I = \frac{0.317}{0.317 + 0.030} = 0.91.
$$
The between-individual variance is 10 times the measurement error, and a single assay suffices to rank the women. On the log scale, the within-group standard deviation $\sqrt{0.0300} = 0.173$ approximates the within-group coefficient of variation on the original scale: $\mathrm{CV} \approx 17.3\%$ (if the standard deviation of $\ln y$ is $s$, the CV of $y$ is $\sqrt{\mathrm{e}^{s^2} - 1} \approx s$). Laboratories often take a CV below 20% as acceptable. With only 5 people, $\sigma_A^2$ has only 4 degrees of freedom and the interval is wide; a formal reproducibility study needs more individuals.

**Example 17.3.2 (Between-Run and Within-Run Variation in ELISA)** The DNase data (Davidian and Giltinan 1995) are the standard curves of 11 independent ELISA runs, with 2 replicate wells at each concentration. At 0.78 ng/mL, the mean optical density is 0.407, $\mathrm{MS}_B = 0.00151$ and $\mathrm{MS}_W = 0.0000737$ ($F_{10,11} = 20.5$),

$$
\hat\sigma_A = 0.0268, \qquad \hat\sigma = 0.0086, \qquad \hat\rho_I = 0.91.
$$
The within-run (between replicate wells) CV is only 2.1% and the between-run CV is 6.6%: two wells on the same day are almost identical, and it is between days that appreciable differences arise. This is why [7.7.11](/7.7.11) requires each plate to carry its own standard curve and why the quality-control scheme of [7.7.2](/7.7.2) reports within-run and between-run CVs separately. Replicate wells can reduce only the within-run error; to reduce the between-run error, one must increase the number of independent runs. Panel C of the figure below shows that both CVs rise at the low-concentration end (the signal approaches the background), with the ICC between 0.6 and 0.96.

![Between-group and within-group variation: one-way random-effects analysis of variance. A: plasma estradiol of 5 postmenopausal women in the reproducibility substudy of the Nurses' Health Study, with each blood sample split into two portions and assayed blind (table published in Rosner's textbook), log scale; horizontal lines are the mean of each woman and the dashed line is the grand mean. B: optical density at 0.78 ng/mL in the 11 independent runs of the DNase ELISA, with 2 replicate wells per run (Davidian and Giltinan 1995; R dataset DNase), sorted by run mean. C: between-run and within-run standard deviations at each of the 8 standard concentrations of DNase (coefficients of variation as percentages of the mean, log scale) and the intraclass correlation coefficient (right axis), all computed from the mean squares of the random-effects analysis of variance](./plots/variance-components.py)

:::

Nesting at more than one level is also common: patient–visit–multiple readings per visit (blood pressure), mouse–section–field of view. Each level has a variance component, and which level's error is the most economical to reduce depends on the sizes of the components and on the cost at each level.

**Formula 17.3.2 (Reliability of the Mean of Several Measurements)** If $m$ independent replicates are averaged for each person, the reliability of the mean is

$$
\rho_m = \frac{\sigma_A^2}{\sigma_A^2 + \sigma^2/m} = \frac{m\rho_I}{1 + (m - 1)\rho_I}.
$$
This is the Spearman–Brown formula of psychometrics. For $\rho_I = 0.5$, averaging 2 measurements raises the reliability to 0.67, and 4 measurements to 0.80.

## 17.4. Linear Mixed Models

### 17.4.1. Random Intercepts and Random Slopes

The random-effects model can be combined with regression: the fixed effects describe the average pattern in the population, and the random effects describe the individual's deviation from it.

**Definition 17.4.1 (Linear Mixed Model)** Let the $n_i$ observations of the $i$th individual be $\boldsymbol{y}_i$,

$$
\boldsymbol{y}_i = X_i\boldsymbol{\beta} + Z_i\boldsymbol{b}_i + \boldsymbol{\varepsilon}_i, \qquad \boldsymbol{b}_i \sim \mathcal{N}_q(\boldsymbol{0}, G), \quad \boldsymbol{\varepsilon}_i \sim \mathcal{N}(\boldsymbol{0}, \sigma^2 I_{n_i}),
$$
with independence between individuals and between $\boldsymbol{b}_i$ and $\boldsymbol{\varepsilon}_i$, where $X_i$ and $Z_i$ are known design matrices, $\boldsymbol{\beta}$ are the fixed effects and $\boldsymbol{b}_i$ the random effects. Such a model is called a **linear mixed model**. Hence $\boldsymbol{y}_i \sim \mathcal{N}(X_i\boldsymbol{\beta},\ V_i)$ with $V_i = Z_iGZ_i^{\mathsf T} + \sigma^2 I$.

The two most commonly used in longitudinal data:

**Definition 17.4.2 (Random-Intercept and Random-Slope Models)** Let $t_{ij}$ be the time of the $j$th measurement on the $i$th person. The model

$$
y_{ij} = (\beta_0 + b_{0i}) + \beta_1 t_{ij} + \varepsilon_{ij}
$$
is called a **random intercept** model: each person has his or her own starting point and the rate of change is the same.

$$
y_{ij} = (\beta_0 + b_{0i}) + (\beta_1 + b_{1i})t_{ij} + \varepsilon_{ij}, \qquad \begin{pmatrix} b_{0i} \\ b_{1i}\end{pmatrix} \sim \mathcal{N}_2\left(\boldsymbol{0}, \begin{pmatrix}\sigma_0^2 & \sigma_{01} \\ \sigma_{01} & \sigma_1^2\end{pmatrix}\right)
$$
is called a **random slope** model: each person has a different starting point and a different rate of change, and the two may be correlated.

The correlation structure implied by the random-intercept model is "compound symmetry": the correlation between any two measurements is $\sigma_0^2/(\sigma_0^2 + \sigma^2)$, the ICC. In the random-slope model the variance changes with time, $\operatorname{Var}(y_{ij}) = \sigma_0^2 + 2\sigma_{01}t_{ij} + \sigma_1^2t_{ij}^2 + \sigma^2$, and measurements farther apart are less correlated (if the slope differences are large).

### 17.4.2. Estimation: REML

When the covariance is known, the optimal estimator of $\boldsymbol{\beta}$ is generalized least squares, $\hat{\boldsymbol{\beta}} = \bigl(\sum_i X_i^{\mathsf T}V_i^{-1}X_i\bigr)^{-1}\sum_i X_i^{\mathsf T}V_i^{-1}\boldsymbol{y}_i$. The variance components are estimated by likelihood. Ordinary **maximum likelihood estimation** underestimates the variance components, for the same reason that the sample variance is too small when divided by $n$: it does not subtract the degrees of freedom used in estimating $\boldsymbol{\beta}$. Restricted maximum likelihood (REML) is based on the likelihood of residual contrasts that do not involve $\boldsymbol{\beta}$; in the balanced one-way design it gives exactly the estimates of Formula 17.3.1 (when positive) and is the default method for mixed models. To compare models with different fixed effects one uses the ML likelihood ratio test, and to compare random-effects structures the REML likelihood ratio; when testing that a variance component is 0, the null hypothesis lies on the boundary of the parameter space and the $\chi^2$ approximation is conservative (the true null distribution is a mixture of $\chi^2_0$, $\chi^2_1$ and so on).

**Example 17.4.1 (Mixed Models for sleepstudy)** Two models fitted by REML:

| | Random intercept | Random slope |
|---|---|---|
| Fixed intercept (SE) | 251.4 (9.75) | 251.4 (6.82) |
| Fixed slope, ms/day (SE) | 10.47 (0.80) | 10.47 (1.55) |
| SD of intercept $\hat\sigma_0$ | 37.1 | 24.7 |
| SD of slope $\hat\sigma_1$ | — | 5.92 |
| Correlation of intercept and slope | — | 0.07 |
| Residual SD $\hat\sigma$ | 31.0 | 25.6 |
| REML log-likelihood | −893.2 | −871.8 |

The likelihood ratio of the random-slope model is $2(-871.8 + 893.2) = 42.8$ (42.1 for ML fits) with 2 degrees of freedom, $p < 10^{-9}$: the rates of deterioration really do differ between people. The meaning of $\hat\sigma_1 = 5.92$ is that the slopes of about 95% of people lie within $10.5 \pm 2 \times 5.9$, that is, between $-1.4$ and $22.3$ ms/day: some people are hardly affected, and others slow by 20 ms per day.

The two models have the same fixed slope, but their standard errors differ by a factor of two: the random-intercept model assumes that every person has the same slope, so slope differences between people are treated as residuals and the standard error 0.80 of the slope is too small; the 1.55 of the random-slope model is exactly the result of the summary-statistic method (Example 17.2.1). A model should include random effects at the same level as the effect of interest: when the interest is in "change over time", the individual's slope is random. The ICC of the random-intercept model is $37.1^2/(37.1^2 + 31.0^2) = 0.59$.

### 17.4.3. Shrinkage and Best Linear Unbiased Prediction

A mixed model also gives each person's own line. The "estimates" of random effects are called predictions (they are random variables, not parameters):

**Theorem 17.4.1 (Best Linear Unbiased Prediction)** In a linear mixed model, the conditional expectation of $\boldsymbol{b}_i$ given $\boldsymbol{y}_i$ is

$$
\hat{\boldsymbol{b}}_i = \mathbb{E}(\boldsymbol{b}_i \mid \boldsymbol{y}_i) = GZ_i^{\mathsf T}V_i^{-1}(\boldsymbol{y}_i - X_i\boldsymbol{\beta}),
$$
and the prediction obtained by substituting estimates for $G$, $\sigma^2$ and $\boldsymbol{\beta}$ is called the *best linear unbiased prediction*, abbreviated BLUP. In the random-intercept model it reduces to

$$
\hat b_i = w_i(\bar y_i - \hat\mu_i), \qquad w_i = \frac{\sigma_0^2}{\sigma_0^2 + \sigma^2/n_i},
$$
where $\bar y_i - \hat\mu_i$ is the mean residual of person $i$.

**Proof** $(\boldsymbol{b}_i, \boldsymbol{y}_i)$ are jointly normal with $\operatorname{Cov}(\boldsymbol{b}_i, \boldsymbol{y}_i) = GZ_i^{\mathsf T}$ and $\operatorname{Var}(\boldsymbol{y}_i) = V_i$, and the formula for the conditional expectation of a multivariate normal ([3.4.2](/3.4.2)) gives the first expression. For a random intercept, $Z_i = \boldsymbol{1}$, $G = \sigma_0^2$, $V_i = \sigma_0^2\boldsymbol{1}\boldsymbol{1}^{\mathsf T} + \sigma^2 I$, and from $V_i^{-1}\boldsymbol{1} = \boldsymbol{1}/(\sigma^2 + n_i\sigma_0^2)$ we get $\hat b_i = \sigma_0^2 n_i(\bar y_i - \mu_i)/(\sigma^2 + n_i\sigma_0^2)$, which simplifies to the second expression. $\square$

Since $0 < w_i < 1$, an individual's estimate is "shrunk" toward the population mean. The fewer data a person has (small $n_i$), the noisier they are (large $\sigma^2$), or the smaller the individual differences in the population (small $\sigma_0^2$), the less reliable the person's own data are and the more that person "borrows strength" from the population. This is exactly the same as the weighted average of prior and data in Bayes estimation (the distribution of the random effects is the prior), and is the common idea behind the empirical Bayes method in [7.7.20](/7.7.20) and polygenic prediction in [7.4.25](/7.4.25). In the random-intercept model for sleepstudy, $w = 1378/(1378 + 960/10) = 0.93$, so the shrinkage is light; if each person were measured on only 2 days, $w$ would fall to 0.74.

**Example 17.4.2** In the random-slope model, subject 335 has an individual regression slope of −2.88 ms/day (the reaction actually becomes faster after sleep deprivation) and a BLUP of −0.28; the 3.01 of subject 330 shrinks to 5.65; the data of subject 337 lie almost on a straight line, and 19.03 hardly changes (19.10). The individual slope 2.26 of subject 309 actually becomes 1.85: the intercept is extremely low (205 ms), and under the joint distribution of intercept and slope, shrinkage of the intercept also drags the slope along. The BLUP is not "a truer individual slope" but the minimum-mean-squared-error prediction of it given the data: as a whole, the 18 BLUPs are on average closer to the true slopes than the 18 individual regressions (panel B of the figure below).

![Sleep restriction and reaction time: 18 subjects measured every day for 10 days of sleeping 3 hours per night (Belenky et al. 2003; sleepstudy data of the R package lme4, 180 observations). A: trajectory of each subject ("spaghetti plot") and the ordinary least squares line that ignores subjects. B: intercepts and slopes fitted separately for each person (open circles) and the predictions of the random-intercept random-slope linear mixed model (REML) (filled dots); the arrows show the mixed model shrinking the individual lines toward the population line (cross); the more uncertain or extreme an individual fit, the more it is shrunk. C: separate fits for 6 subjects (dashed), mixed-model predictions (solid) and the population line (gray)](./plots/sleepstudy-shrinkage.py)

### 17.4.4. Mixed Models in Experimental Design

Mixed models write the principle of the "experimental unit" of [7.7.12](/7.7.12) into the model:

- Mouse–cell: `response ~ treatment + (1 | mouse)`; the test of the treatment effect automatically takes the mouse as the unit while using the information from all cells; it is no problem if each mouse has a different number of cells.
- Several independent experiments–replicate wells: take the experiment (run, plate, date) as a random effect, the problem of pooling $\log\mathrm{IC}_{50}$ in the questions of [7.7.11](/7.7.11).
- Multicenter trial: center as a random intercept; if the interest is whether the treatment effect varies by center, add a random slope for treatment.
- Nonlinear mixed models: the 4PL parameters ([7.7.11](/7.7.11)) of each ELISA run each have random effects, for example $\log\mathrm{EC}_{50}$ varying normally between runs; population models in pharmacokinetics (each patient's clearance is random) are the same kind of model.

As an empirical rule, when the number of groups for a random effect is too small (fewer than 5–6 groups), the variance component estimate is very unstable, and it is safer to treat the groups as fixed effects (or to use the summary-statistic method).

## 17.5. Generalized Estimating Equations and Marginal Models

A mixed model models the individual's trajectory (conditional on $\boldsymbol{b}_i$) and fully assumes the correlation structure and the normal distribution. Another route models only the mean of the population and treats correlation as a nuisance to be tolerated.

**Definition 17.5.1 (Generalized Estimating Equations)** Let $\mathbb{E}(y_{ij}) = \mu_{ij}$ and $g(\mu_{ij}) = \boldsymbol{x}_{ij}^{\mathsf T}\boldsymbol{\beta}$ ($g$ is the link function of a **generalized linear model**). Specify a "working" correlation matrix $R_i(\alpha)$ (independence, exchangeable, autoregressive and so on), set $V_i = A_i^{1/2}R_iA_i^{1/2}$ ($A_i$ the diagonal matrix of the variance functions of the observations), and solve

$$
\sum_{i=1}^k D_i^{\mathsf T}V_i^{-1}(\boldsymbol{y}_i - \boldsymbol{\mu}_i) = \boldsymbol{0}, \qquad D_i = \frac{\partial\boldsymbol{\mu}_i}{\partial\boldsymbol{\beta}^{\mathsf T}},
$$
to obtain $\hat{\boldsymbol{\beta}}$; its variance is estimated by

$$
\widehat{\operatorname{Var}}(\hat{\boldsymbol{\beta}}) = B^{-1}\Bigl(\sum_i D_i^{\mathsf T}V_i^{-1}\hat{\boldsymbol{e}}_i\hat{\boldsymbol{e}}_i^{\mathsf T}V_i^{-1}D_i\Bigr)B^{-1}, \qquad B = \sum_i D_i^{\mathsf T}V_i^{-1}D_i
$$
($\hat{\boldsymbol{e}}_i$ are the residuals). This method is called **generalized estimating equations** (GEE).

The key property of GEE (Liang and Zeger 1986): as long as the mean model is correct, $\hat{\boldsymbol{\beta}}$ remains consistent even if the working correlation matrix is wrong, and the "sandwich" variance above (the same principle as the **White estimator**) remains correct; efficiency is higher when the working correlation is close to the truth. The price is that enough individuals are needed (empirically more than 40), otherwise the sandwich variance is too small; and it provides neither individual-level predictions nor variance components. As for missing data, GEE is unbiased only under missing completely at random (Section 17.8), which is a disadvantage compared with likelihood methods.

**Example 17.5.1** Fitting a linear mean for sleepstudy by GEE, the exchangeable working correlation (estimated working correlation 0.57) and the independence working correlation give the same slope 10.47, with robust standard errors both 1.50 (with 18 people slightly smaller than the 1.55 of the mixed model, the small-sample underestimate).

:::

In a linear model, the fixed effect of a mixed model and the marginal effect of GEE are the same quantity. With a nonlinear link function the two differ: in a logistic mixed model, $\beta$ is the log odds ratio for "the same person" exposed versus not (the conditional effect, or subject-specific effect); in GEE, $\beta$ is the log odds ratio between exposed and unexposed people in the population (the marginal effect, or population-averaged effect). When the standard deviation of the random intercept is $\sigma_0$, approximately $\beta_{\text{marginal}} \approx \beta_{\text{conditional}}/\sqrt{1 + 0.346\sigma_0^2}$: the larger the individual differences, the weaker the marginal effect. When the research question is a public-health one (how much will this policy lower the incidence in the population), use the marginal model; when it is clinical (what does this drug do to my risk), use the conditional model.

## 17.6. Crossover Designs

**Definition 17.6.1 (Crossover Design and Carryover Effect)** A trial in which each subject receives two (or more) treatments in sequence, with the order of treatments randomly assigned, is called a **crossover design**. In the simplest 2×2 crossover design, subjects are randomized to the sequence AB or BA, and between the two treatment periods there is often a washout period in which no treatment is given. The residual effect of the treatment of the previous period in the following period is called the **carryover effect**.

A crossover design lets each person serve as his or her own control, so that the comparison is of within-individual differences, and the number of subjects needed is much smaller than in a parallel design: when the correlation of the two measurements is $\rho$, the number needed is about $(1 - \rho)/2$ of that of a parallel design ([7.7.7](/7.7.7) Formula 7.6.2). It is suitable for stable chronic diseases and reversible treatments: hypertension, asthma, chronic pain, bioequivalence trials. It is unsuitable for curable diseases, for treatments with lasting effects, and for studies whose outcome is death.

**Formula 17.6.1 (Treatment Effect in a Crossover Design)** Let the sequence AB group have $n_1$ people, each with difference $d_{1j} = y_{\mathrm{A}} - y_{\mathrm{B}}$ (period 1 minus period 2); and the sequence BA group have $n_2$ people with $d_{2j} = y_{\mathrm{A}} - y_{\mathrm{B}}$ (period 2 minus period 1). In the absence of carryover, the estimate and test of the treatment effect are

$$
\hat\tau = \frac{\bar d_1 + \bar d_2}{2}, \qquad \mathrm{SE}(\hat\tau) = \frac{s_d}{2}\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}, \qquad t = \frac{\hat\tau}{\mathrm{SE}(\hat\tau)} \overset{H_0}{\sim} t_{n_1 + n_2 - 2},
$$
where $s_d^2$ is the pooled variance of the differences in the two groups ([7.7.7](/7.7.7) Definition 7.3.1). Half the difference of the group means of the differences, $(\bar d_2 - \bar d_1)/2$, estimates the period effect (the change from period 1 to period 2). Taking the sum of the two periods as the summary for each person and comparing the sums of the two groups is the test for carryover.

Averaging over the two sequences cancels the period effect: if period 2 is generally somewhat better (season, adaptation to the study, natural fluctuation of the disease), the differences in the AB group are too small and those in the BA group too large, and they cancel on averaging. The carryover effect, however, cannot be removed in this way. The test for carryover compares sums between individuals and has very low power; the two-stage strategy of "test for carryover first, and use only the first-period data if it is significant" inflates the type I error rate (Freeman 1989) and is no longer recommended. Carryover should be excluded by design: a sufficiently long washout period (usually more than 5 half-lives of the drug) and a pharmacological argument for reversibility.

![A 2×2 crossover design (schematic). Top: subjects are randomized to the sequence AB or BA and each receives the two treatments, with a washout period without treatment in between. Bottom: expected responses of each sequence in the two treatment periods; in the figure period 2 is generally slightly better (period effect) and the effect of A carries over into period 2 (dashed line, open circle is the response to B without carryover); each person's difference $A - B$ cancels the person's own level, averaging over the two sequences cancels the period effect, but carryover makes the difference in the AB group too small](./plots/crossover.py)

**Example 17.6.1 (A Worked Example)** In a crossover trial comparing two analgesics with 20 people per sequence, the difference in pain relief score (A − B) has mean 1.2 in the AB group and 0.8 in the BA group, with pooled standard deviation 1.5 (the numbers are made up for illustration). $\hat\tau = 1.0$, $\mathrm{SE} = (1.5/2)\sqrt{0.1} = 0.237$, $t_{38} = 4.22$, $p = 0.0001$; the period effect is estimated as $(0.8 - 1.2)/2 = -0.2$ (pain relief is slightly lower in period 2).

## 17.7. Clustered Data and the Design Effect

When observations are clustered in groups (clinics, schools, families, litters, the two eyes or ears of the same person), correlation within clusters makes the effective independent information smaller than the number of observations.

**Definition 17.7.1 (Design Effect)** In a cluster sampling or cluster randomized design with $m$ observations per cluster and intraclass correlation coefficient $\rho$, the ratio of the variance of the estimator of a mean (or proportion) to that of a simple random sample with the same number of observations,

$$
\mathrm{Deff} = 1 + (m - 1)\rho
$$
is called the **design effect**. For a clustered sample with $N$ observations in total, the **effective sample size** is $N/\mathrm{Deff}$.

Derivation: the variance of a cluster mean $\bar y_c$ is $\sigma^2[1 + (m - 1)\rho]/m$ (the covariance of any two of the $m$ observations is $\rho\sigma^2$), the variance of the overall mean of $N/m$ clusters is $\sigma^2[1 + (m - 1)\rho]/N$, and comparing with $\sigma^2/N$ under independence gives the result. Even if $\rho$ is small, the design effect can be considerable when $m$ is large: with $\rho = 0.02$ (a typical difference between clinics) and 100 patients per clinic, $\mathrm{Deff} = 2.98$, and a cluster randomized trial of 30,000 people is worth only 10,000 people in an individually randomized trial. The pseudoreplication simulation in [7.7.12](/7.7.12) Example 12.7.2 and the sample size of cluster randomized trials in [7.7.18](/7.7.18) are both applications of this formula.

Binary clustered data (whether each of a child's two ears has middle-ear effusion, whether each of several herpes lesions on a patient has shrunk) follow the same logic: treating each ear as an independent observation in a chi-square test gives too small a $p$-value; the correct approach is to analyze with the child as the unit (both ears cured, one ear, neither), to correct the chi-square statistic with the design effect (dividing by Deff), or to use logistic GEE or a logistic mixed model.

## 17.8. Missing Data

Longitudinal studies almost always have missing data: patients are lost to follow-up, a visit is missed, a sample is hemolyzed. The impact of missingness depends on "why it is missing".

**Definition 17.8.1 (Missing-Data Mechanisms)** Let $\boldsymbol{Y}$ be the complete data, split into the observed part $\boldsymbol{Y}_{\mathrm{obs}}$ and the missing part $\boldsymbol{Y}_{\mathrm{mis}}$, and let $\boldsymbol{R}$ be the missingness indicator.

- If $\mathbb{P}(\boldsymbol{R} \mid \boldsymbol{Y}) = \mathbb{P}(\boldsymbol{R})$, missingness is unrelated to any data and is called **missing completely at random** (MCAR);
- if $\mathbb{P}(\boldsymbol{R} \mid \boldsymbol{Y}) = \mathbb{P}(\boldsymbol{R} \mid \boldsymbol{Y}_{\mathrm{obs}})$, missingness depends only on the observed data and is called **missing at random** (MAR);
- otherwise, missingness depends on the unobserved values themselves and is called **missing not at random** (MNAR).

Examples: a sample tube broken in transit is MCAR; a patient whose blood pressure at the last visit was very high being referred and leaving the study is MAR (the dropout is determined by the observed blood pressure); a patient who feels too poorly to come for a checkup because of worsening illness is MNAR if the worsening was not reflected in the earlier measurements.

| Method | MCAR | MAR | MNAR |
|---|---|---|---|
| Complete-case analysis (using only individuals without missing data) | Unbiased, but wastes information | Generally biased | Biased |
| Last observation carried forward (LOCF) | Generally biased | Biased | Biased |
| Likelihood methods (a mixed model using all observations), multiple imputation | Unbiased | Unbiased (if the model is correct) | Biased |
| Sensitivity analysis (pattern-mixture models, selection models, δ adjustment) | — | — | Assesses robustness of conclusions |

Likelihood methods are valid under MAR because the likelihood of the observed data factors into a "data model" and a "missingness mechanism", the latter not containing the parameters of interest and therefore ignorable (Rubin 1976, "ignorability"); the EM algorithm ([3.5.6](/3.5.6)) is the general tool for maximizing under such a likelihood. LOCF used to be standard practice in clinical trials; it assumes that values stay unchanged after dropout, and in progressive disease it is both biased and underestimates variance; it is no longer recommended (report of the US National Research Council, 2010).

**Example 17.8.1 (Simulation of MAR Dropout)** Using the estimates of the sleepstudy mixed model, we simulate 100 subjects; from day 3 on, the slower a person's reaction the previous day, the more likely the person is to drop out (dropout probability $\mathrm{logistic}(-3 + 0.03(y_{\text{previous day}} - 300))$), and about half the people drop out along the way. Over 300 replications, the averages of four estimates of the true slope 10.47 are: completers only 7.73, OLS on all available data 7.46, LOCF 8.92, and the mixed model (likelihood using all observations) 10.41. The dropouts are precisely those who deteriorate fastest, so looking only at completers underestimates the effect of sleep deprivation; the mixed model, from the data of the dropouts before they leave, "knows" that they deteriorate fast and makes the correct inference about the missing part accordingly.

![Dropout that depends on observed values (missing at random, MAR; simulation, seed 0). Data are generated from the estimates of the sleepstudy mixed model (fixed intercept 251.4 ms, slope 10.47 ms/day, SDs of random effects 24.7 and 5.92, correlation 0.07, residual SD 25.6), 100 subjects, 10 days; from day 3 on, people with slower reaction the previous day are more likely to drop out. A: observed values of 40 subjects in one simulation (blue: completers; orange: the part of dropouts before they leave) and unobserved values (light gray). B: average slopes of four analyses over 300 replications: completers only, ordinary least squares on all available data, last observation carried forward (LOCF) and likelihood analysis of a mixed model using all observed data (here generalized least squares with the true covariance); only the last is unbiased under MAR](./plots/missing-data.py)

**Definition 17.8.2 (Multiple Imputation)** Draw $M$ sets of imputed values independently from the predictive distribution of the missing values given the observed data, obtaining $M$ complete data sets; analyze each as complete data to get $\hat\theta_m$ and variance $W_m$, and combine them by Rubin's rules:

$$
\bar\theta = \frac1M\sum_m\hat\theta_m, \qquad T = \bar W + \Bigl(1 + \frac1M\Bigr)B, \qquad \bar W = \frac1M\sum_m W_m, \quad B = \frac{1}{M - 1}\sum_m(\hat\theta_m - \bar\theta)^2.
$$
This method is called **multiple imputation**.

Single imputation (filling in the mean or a regression prediction) treats guessed values as observed and underestimates variance; the between-imputation variance $B$ of multiple imputation reflects exactly the uncertainty of "not knowing what the missing values are". The imputation model should include all the variables of the analysis model (including the outcome) and auxiliary variables related to missingness; in Python, `statsmodels.imputation.mice` and scikit-learn's `IterativeImputer` implement conditional imputation variable by variable (MICE). MAR itself cannot be tested with data: clinical-trial guidelines require the analysis under MAR to be primary, with sensitivity analyses for MNAR (for example assuming that the outcomes of dropouts are worse by δ than predicted under MAR, and seeing at what δ the conclusion changes).

## 17.9. Measurement Error and Regression Dilution

**Definition 17.9.1 (Regression Dilution)** Suppose the outcome depends on the true level $X$ of the exposure, $\mathbb{E}(Y \mid X) = \alpha + \beta X$, while the exposure can be measured only as $W = X + U$, with error $U$ independent of $X$ and $Y$ (classical measurement error). The slope of the regression of $Y$ on $W$ converges to

$$
\beta^* = \lambda\beta, \qquad \lambda = \frac{\operatorname{Var}(X)}{\operatorname{Var}(X) + \operatorname{Var}(U)},
$$
that is, the true effect is attenuated by the factor $\lambda$. This phenomenon is called **regression dilution**, and $\lambda$ is called the attenuation factor; it is the reliability (ICC) of a single measurement.

Derivation: $\operatorname{Cov}(Y, W) = \operatorname{Cov}(\alpha + \beta X + e, X + U) = \beta\operatorname{Var}(X)$, $\operatorname{Var}(W) = \operatorname{Var}(X) + \operatorname{Var}(U)$, and the slope is $\operatorname{Cov}/\operatorname{Var}(W) = \lambda\beta$. If a subsample has repeated measurements of $W$, $\lambda$ can be estimated (the correlation of two measurements, or the ICC of the random-effects analysis of variance) and $\hat\beta^*/\hat\lambda$ used as a correction (regression calibration). Measurement error in the outcome $Y$, in contrast, does not bias the slope but only increases the residual variance ([7.7.11](/7.7.11) Section 11.1 discussed Deming regression when $x$ has error).

Regression dilution has a large influence in epidemiology. Blood pressure, cholesterol, diet and other exposures all have appreciable within-individual fluctuation in a single measurement: in prospective studies, estimating the relation of blood pressure to stroke with a single blood pressure measurement underestimates the true effect of "long-term average blood pressure", and the corrected effect is about 60% larger (MacMahon et al. 1990). In Example 17.3.1 the ICC of estradiol is 0.91, so a single assay attenuates the effect by only about 9%; an exposure with an ICC of 0.5 would halve the effect. When several exposures have errors, the dilution is no longer necessarily toward zero: inadequate adjustment for a poorly measured confounder (residual confounding, [7.7.15](/7.7.15)) can make the effect of another exposure look larger.

![Regression dilution (simulation, seed 0). The outcome depends on the long-term true level $X$ of the exposure (slope 1), while the exposure is measured only once, $W = X + U$, with reliability = $\operatorname{Var}(X)/\operatorname{Var}(W)$. A: 400 simulated individuals with reliability 0.5; the slope of the regression of $Y$ on the true $X$ is about 1, and on the single measurement $W$ about 0.5. B: estimated slope against the reliability of a single measurement, 200 replications at each reliability (dots are means, the line is the attenuation factor itself); squares are corrected slopes obtained by estimating the reliability from repeated measurements on 100 people and dividing by it](./plots/regression-dilution.py)

## 17.10. Computing with Python

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

sleep = pd.read_csv("sleepstudy.csv")            # reaction (ms), days 0-9, subject

# naive OLS and the summary-statistic method (Examples 17.1.1, 17.2.1)
print(smf.ols("reaction ~ days", sleep).fit().bse["days"])                 # 1.24, too small
slopes = sleep.groupby("subject").apply(lambda g: np.polyfit(g.days, g.reaction, 1)[0])
print(slopes.mean(), stats.ttest_1samp(slopes, 0))                           # 10.47, t = 6.77

# linear mixed models by REML (Example 17.4.1)
ri = smf.mixedlm("reaction ~ days", sleep, groups="subject").fit(reml=True)
rs = smf.mixedlm("reaction ~ days", sleep, groups="subject", re_formula="~days").fit(reml=True)
print(rs.summary())                     # slope 10.47 (SE 1.55); SD intercept 24.7, slope 5.92
print(np.sqrt(np.diag(rs.cov_re)), np.sqrt(rs.scale))
print(rs.random_effects["335"])         # BLUP deviations for subject 335 (Example 17.4.2)

# GEE with exchangeable working correlation (Example 17.5.1)
gee = smf.gee("reaction ~ days", "subject", sleep, cov_struct=sm.cov_struct.Exchangeable()).fit()
print(gee.params["days"], gee.bse["days"])                                  # 10.47, robust SE 1.50

# one-way random-effects ANOVA and the ICC (Example 17.3.1)
y = np.log(np.array([[25.5, 30.4], [11.1, 15.0], [8.0, 8.1], [20.7, 16.9], [5.8, 8.4]]))
k, n = y.shape
msb = n * y.mean(1).var(ddof=1)
msw = ((y - y.mean(1, keepdims=True)) ** 2).sum() / (k * (n - 1))
sa2 = max((msb - msw) / n, 0)
print(msb, msw, sa2 / (sa2 + msw), 100 * np.sqrt(msw))                     # ICC 0.91, CV 17.3%
```

The `MixedLM` of `statsmodels` uses REML by default; the groups of the random effects are specified by `groups` and random slopes by `re_formula`. For binary or count outcomes, statsmodels has only a Bayesian approximation for mixed models (`BinomialBayesMixedGLM`); common alternatives are GEE (`smf.gee(..., family=sm.families.Binomial())`) or dedicated software packages.

## Summary

- Repeated measures (Definition 17.1.1) share an individual effect, so observations on the same person are correlated, with correlation coefficient $\sigma_b^2/(\sigma_b^2 + \sigma^2)$; ignoring it makes standard errors of between-subject comparisons too small (pseudoreplication) and the efficiency and standard errors of within-subject comparisons wrong. The OLS standard error of the slope for sleepstudy is 1.24; the correct value is 1.55 (Example 17.1.1).
- Three correct kinds of analysis:

  | Method | What is modeled | Advantages | Limitations |
  |---|---|---|---|
  | Summary-statistic method (Section 17.2) | One number per person | Transparent, no correlation assumption | Unequal precision, crude handling of missing data |
  | Linear mixed model (Definitions 17.4.1, 17.4.2) | Individual trajectories + variance components | Valid under MAR; BLUP; nested structures | Needs assumptions on distribution and correlation structure |
  | GEE (Definition 17.5.1) | Population mean | Consistent even with a wrong correlation structure (sandwich variance) | Needs many individuals; unbiased only for MCAR |

- The random-effects model (Definition 17.3.1): $\mathbb{E}(\mathrm{MS}_B) = \sigma^2 + n\sigma_A^2$, $\hat\sigma_A^2 = (\mathrm{MS}_B - \mathrm{MS}_W)/n$ (Formula 17.3.1); ICC $= \sigma_A^2/(\sigma_A^2 + \sigma^2)$ (Definition 17.3.2), and the reliability of the mean of $m$ measurements is $m\rho/[1 + (m-1)\rho]$ (Formula 17.3.2). Estradiol ICC 0.91, CV 17.3% (Example 17.3.1); DNase within-run CV 2.1%, between-run 6.6% (Example 17.3.2).
- The random-slope model for sleepstudy: slope 10.47 (SE 1.55), SD of individual slopes 5.92, residual 25.6 (Example 17.4.1); the standard error 0.80 of the slope in the random-intercept model is too small. REML is the default.
- BLUP (Theorem 17.4.1) shrinks individual estimates toward the population, with weight $\sigma_0^2/(\sigma_0^2 + \sigma^2/n_i)$; the −2.88 of subject 335 shrinks to −0.28 (Example 17.4.2).
- Conditional versus marginal effects: the same in linear models; in logistic models $\beta_{\text{marginal}} \approx \beta_{\text{conditional}}/\sqrt{1 + 0.346\sigma_0^2}$.
- Crossover design (Definition 17.6.1): $\hat\tau = (\bar d_1 + \bar d_2)/2$, period effects cancel, and carryover is excluded by a washout period rather than by a preliminary test (Formula 17.6.1).
- Design effect $1 + (m - 1)\rho$ (Definition 17.7.1), effective sample size $N/\mathrm{Deff}$.
- Missing-data mechanisms MCAR, MAR, MNAR (Definition 17.8.1): under MAR use likelihood methods or multiple imputation (Definition 17.8.2), not complete cases or LOCF; in the simulation 7.73, 7.46, 8.92 versus 10.41 (truth 10.47, Example 17.8.1); do sensitivity analysis for MNAR.
- Regression dilution (Definition 17.9.1): the slope is attenuated to $\lambda\beta$, with $\lambda$ the ICC of a single measurement; correct using a subsample with repeated measurements.

## Questions

1. In a reproducibility study, 10 subjects are each measured 3 times, and the random-effects analysis of variance gives $\mathrm{MS}_B = 50$ and $\mathrm{MS}_W = 10$. Find the two variance components, the ICC, and the reliability when the mean of 3 measurements is used.

   **Answer** $\hat\sigma^2 = 10$, $\hat\sigma_A^2 = (50 - 10)/3 = 13.33$, $\hat\rho_I = 13.33/23.33 = 0.571$. The reliability of the mean of 3 measurements is $13.33/(13.33 + 10/3) = 0.80$, which also follows from Formula 17.3.2: $3 \times 0.571/(1 + 2 \times 0.571) = 0.80$. $F = 5$ with $(9, 20)$ degrees of freedom, $p \approx 0.001$, so there are indeed differences between individuals.

2. In Example 17.3.1, if the coefficient of variation of each woman's mean estradiol is to be no more than 10%, how many portions must be assayed per person at least? What is the reliability of the mean then?

   **Answer** On the log scale the within-group standard deviation is 0.173, and the within-group standard deviation of the mean of $m$ portions is $0.173/\sqrt m$; requiring $\le 0.10$ gives $m \ge 2.99$, so take 3 portions. The reliability is $0.317/(0.317 + 0.030/3) = 0.97$. Since the ICC is already high, additional replicates help little with ranking and mainly improve the precision of the absolute concentration.

3. A cluster randomized trial enrolls 50 patients in each of 20 clinics (10 per arm), and the intraclass correlation coefficient of the outcome is 0.02. What are the design effect and the effective sample size? What if there were 40 clinics with 25 patients each?

   **Answer** $\mathrm{Deff} = 1 + 49 \times 0.02 = 1.98$, and the effective sample size of 1000 people is about $1000/1.98 = 505$. With 40 clinics of 25 each: $\mathrm{Deff} = 1 + 24 \times 0.02 = 1.48$ and the effective sample size is $1000/1.48 = 676$. For the same total number of people, the more clusters and the smaller each cluster, the higher the efficiency; the power of a cluster trial is determined mainly by the number of clusters.

4. In the random-intercept model for sleepstudy, $\hat\sigma_0^2 = 1378$ and $\hat\sigma^2 = 960$. What are the BLUPs of a subject measured on only 2 days with mean residual +40 ms, and of a subject measured on 10 days with the same mean residual +40 ms? Explain the difference.

   **Answer** $w_2 = 1378/(1378 + 960/2) = 0.742$, $\hat b = 29.7$ ms; $w_{10} = 1378/(1378 + 96) = 0.935$, $\hat b = 37.4$ ms. With only 2 measurements, a larger part of the +40 ms may be chance fluctuation of measurement, so it is shrunk more toward the population mean; the mean of 10 measurements is more trustworthy. This is exactly "borrowing strength": individuals with fewer data rely more on information from the population.

5. State whether each of the following missingness is MCAR, MAR or MNAR, and whether a complete-case analysis is biased: (a) the laboratory freezer breaks down and 10% of the blood samples are lost at random; (b) in a diabetes trial, patients whose previous HbA1c exceeds 9% withdraw per protocol and switch to rescue treatment; (c) in a depression trial, patients whose mood worsens do not come for follow-up, and the worsening occurred after the last visit.

   **Answer** (a) MCAR; the complete-case analysis is unbiased and only loses precision. (b) MAR: withdrawal is entirely determined by the observed HbA1c; the complete-case analysis is biased (those who remain are all better controlled), while a mixed model using all observations or multiple imputation can give unbiased estimates. (c) MNAR: missingness depends on the unobserved worsening, and any method relying only on the observed data may be biased; a sensitivity analysis should be done, such as assuming the scores of the missing are worse by δ than predicted under MAR and reporting at what δ the conclusion changes.

6. In the design of Example 17.6.1, if carryover raises B in period 2 of the AB group by 0.6 points, by how much will the treatment-effect estimate be biased? Why can the test for carryover not be used to decide whether to use only the first-period data?

   **Answer** The difference in the AB group is A in period 1 minus B in period 2; with B raised by 0.6, $\bar d_1$ is too small by 0.6, and $\hat\tau = (\bar d_1 + \bar d_2)/2$ is too small by 0.3 (underestimating the advantage of A). The test for carryover compares the sums of individuals between the two groups, its variance includes the between-individual variation, and its power is very low; choosing the analysis method conditional on it, the type I error rate of the two-stage procedure is far above the nominal level (Freeman 1989). The correct approach is to ensure by design that the washout period is long enough, and to switch to a parallel design if carryover cannot be ruled out.

7. A cohort study uses single measurements of systolic blood pressure and estimates that each 10 mmHg of systolic pressure raises the log of the stroke risk by 0.25. A repeated-measures study of blood pressure gives an ICC of 0.6 for a single measurement. About what is the true effect of long-term average blood pressure? What else could make this correction inaccurate?

   **Answer** After correction, $0.25/0.6 = 0.417$, so the risk ratio per 10 mmHg rises from $\mathrm{e}^{0.25} = 1.28$ to $\mathrm{e}^{0.417} = 1.52$. The correction assumes that the error is classical (independent of the true value and of constant variance), that the reliability is the same in the cohort population as in the repeated-measures study, and that the model is approximately linear (in logistic or Cox models regression calibration is only an approximation). If the interval between repeated measurements differs from the time scale of the "long-term average", the ICC will differ as well.

8. A researcher uses 3 wild-type and 3 mutant mice and records the firing rates of 40 neurons in each mouse. Write down an appropriate mixed model, state roughly how many degrees of freedom the test of the treatment effect has, and explain why increasing the number of neurons recorded per mouse helps power only a little.

   **Answer** $y_{ijk} = \mu + \tau_i + b_{ij} + \varepsilon_{ijk}$, where $\tau_i$ is the genotype (fixed), $b_{ij} \sim \mathcal{N}(0, \sigma_b^2)$ is the mouse (random) and $\varepsilon_{ijk}$ is the variation between neurons (`rate ~ genotype + (1 | mouse)`). The effective degrees of freedom of the genotype comparison are about $6 - 2 = 4$ (number of mice minus number of groups), not 238. The variance of a group mean is $(\sigma_b^2 + \sigma^2/40)/3$: more neurons reduce only the term $\sigma^2/40$, the between-mouse variance $\sigma_b^2/3$ stays the same, and power is determined by the number of mice (pseudoreplication in [7.7.12](/7.7.12)).

9. In a random-intercept logistic model, the conditional odds ratio of a drug is 3.0 and the standard deviation of the random intercept is 1.5. About what is the population-averaged (marginal) odds ratio? Which should a clinician and which a health-policy maker care about?

   **Answer** $\beta_{\text{marginal}} \approx \ln 3/\sqrt{1 + 0.346 \times 2.25} = 1.0986/1.3336 = 0.824$, and the marginal OR is $\approx \mathrm{e}^{0.824} = 2.28$. The conditional OR (3.0) describes the comparison of the same person taking the drug or not, the quantity a clinician explains to a patient; the marginal OR (2.28) describes the comparison between those who take the drug and those who do not in the population, the quantity for estimating the population-level effect of a policy. Both are correct and answer different questions; the larger the variance of the random effects, the larger the difference.

10. (Design question) You want to evaluate the reproducibility of a new assay for exosomal miRNA, and plan to measure the plasma of 20 patients in 3 laboratories, 4 days per laboratory and 2 replicate wells per day. Write down the variance-component model, explain the meaning of each component and how to use it to decide the assay scheme per sample in clinical use.

    **Answer** $y_{pldr} = \mu + P_p + L_l + D_{d(l)} + (PL)_{pl} + \varepsilon_{pldr}$: $P_p$ is the patient (true biological difference, which we want to be large), $L_l$ the laboratory (systematic bias), $D_{d(l)}$ the day-to-day (between-run) variation within a laboratory, $(PL)$ the patient-by-laboratory interaction (some samples read high in some laboratory), and $\varepsilon$ the error between replicate wells (within-run); all are random effects, estimated by REML. Report the proportion of the total variance due to each component, the within-run and between-run CVs, and the ICC for a single laboratory and single assay (patient variance / total variance). Decisions: if the within-run variance dominates, add replicate wells; if the day-to-day variance dominates, replicate wells are useless and one needs to repeat the assay on different days or include a calibrator on every plate; if the laboratory variance is large, standardization is needed or comparisons should be made only within a single laboratory. Use Formula 17.3.2 to choose the most economical scheme that reaches the target reliability (such as 0.8).
