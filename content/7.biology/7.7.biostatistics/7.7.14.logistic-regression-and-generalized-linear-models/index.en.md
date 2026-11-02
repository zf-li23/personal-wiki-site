---
title: Logistic Regression and Generalized Linear Models
description: Why linear regression is not used for a binary outcome; the logit and logistic functions and the odds-ratio interpretation of coefficients; maximum likelihood estimation, Wald tests, likelihood ratio tests and profile intervals; adjustment, interaction and model comparison in multiple logistic regression; deviance, the Hosmer–Lemeshow test, calibration plots and the AUC; logit and probit analysis of binary dose response and the LD50; conditional logistic regression; the generalized linear model framework, Poisson regression with an offset, and overdispersion. The examples are low birth weight in birthwt, Bliss's beetle toxicity experiment and coronary deaths among British doctors.
source_hash: e3342193366a
---

[7.7.13](/7.7.13) adjusted for one confounder by stratified analysis: split by the person's own smoking into two strata, compare within each, and combine by the Mantel–Haenszel method. When age, weight, race, medical history and other variables must be adjusted for at the same time, stratification quickly becomes impossible: with three levels per variable, five variables give 243 strata, most of which contain only a few people. Multiple linear regression for a continuous outcome ([7.7.10](/7.7.10)) solves the same problem; for a binary outcome the corresponding tool is **logistic regression**. This chapter takes low birth weight (< 2500 g) in birthwt as its main thread: [7.7.9](/7.7.9) computed a crude odds ratio of 2.02 for maternal smoking, and [7.7.13](/7.7.13) explained that it may be confounded by race, weight and other factors; here multiple logistic regression gives adjusted odds ratios and the discrimination and calibration of the model are assessed. The same machinery is then placed in the framework of the **generalized linear model**: binary dose response in toxicology (probit analysis and the $\mathrm{LD}_{50}$) is the same model with a different link function, and data on counts and rates use Poisson regression, so that the stratified analysis of coronary deaths among British doctors becomes a model with an interaction term. The definition of logistic regression, the IRLS algorithm and the general theory of GLMs are in [3.4.12](/3.4.12), [3.5.5](/3.5.5) and [3.3.6](/3.3.6); this chapter treats their use and interpretation in biomedicine. Cox regression for survival data is in [7.7.16](/7.7.16), and the building and validation of clinical prediction models is in [7.7.21](/7.7.21).

## 14.1. From Proportions to the Logit

### 14.1.1. Problems with the Linear Probability Model

The most direct idea is to treat the 0/1 outcome as a continuous variable and do a linear regression, $\mathbb{E}(Y \mid x) = \mathbb{P}(Y = 1 \mid x) = \beta_0 + \beta_1 x$. With the mother's weight (lb) at the last menstrual period as the independent variable in birthwt, we get $\hat p = 0.647 - 0.00258\,x$: at a weight of 250 lb the predicted probability is 0.002, and beyond the range of the data it becomes negative. This "linear probability model" has three problems: predictions can fall outside $[0, 1]$; $\operatorname{Var}(Y \mid x) = p(1 - p)$ varies with $x$, so the assumption of equal variance necessarily fails; and the change of a probability near 0 and 1 should not be linear to begin with: a rise in risk from 1% to 2% is very different from a rise from 50% to 51%.

### 14.1.2. The Logit Transformation

Transforming the probability to the whole real line and building a linear model there avoids these problems.

**Definition 14.1.1 (Logit and the Logistic Function)** The log odds of a probability $p \in (0, 1)$,

$$
\operatorname{logit} p = \ln\frac{p}{1 - p},
$$
is called the **logit**; its inverse $p = \mathrm{e}^\eta/(1 + \mathrm{e}^\eta) = 1/(1 + \mathrm{e}^{-\eta})$ is called the logistic function.

The logit maps $(0, 1)$ one-to-one onto $(-\infty, \infty)$, with $p = 0.5$ corresponding to 0, stretched near 0 and 1: $\operatorname{logit} 0.01 = -4.6$ and $\operatorname{logit} 0.99 = 4.6$. The **logistic regression** model assumes

$$
\operatorname{logit} \mathbb{P}(Y = 1 \mid \boldsymbol{x}) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k,
$$
that is, the log odds of the outcome is a linear function of the independent variables, while the probability is an S-shaped curve.

![Low birth weight (< 2500 g) against maternal weight at the last menstrual period (189 deliveries, Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt). A: the 0/1 outcome (jittered), the proportions with low birth weight in five groups of maternal weight (dots, plotted at the mean weight in each group), the line of the linear probability model and the logistic curve fitted by maximum likelihood; the line gives negative probabilities above 250 lb. B: the same five groups on the logit scale (empirical log odds with 95% intervals), where the logistic model is a straight line](./plots/logistic-lwt.py)

## 14.2. Interpreting the Coefficients: Odds Ratios

### 14.2.1. A Binary Independent Variable

**Theorem 14.2.1 (Coefficients and Odds Ratios)** In a logistic regression model, if $x_j$ increases by 1 unit with the other independent variables unchanged, the odds of the outcome are multiplied by $\mathrm{e}^{\beta_j}$. Hence $\mathrm{e}^{\beta_j}$ is the **odds ratio** between two kinds of people whose $x_j$ differs by 1 unit (adjusted for the other variables in the model); with a single binary independent variable $x$, $\mathrm{e}^{\hat\beta_1}$ is the $ad/(bc)$ of the 2×2 table.

**Proof** The difference of the log odds of the two kinds of people is $[\beta_0 + \beta_j(x_j + 1) + \cdots] - [\beta_0 + \beta_j x_j + \cdots] = \beta_j$, and exponentiating gives the ratio of odds. With only one 0/1 independent variable the model has two parameters and two groups of data and is saturated: the maximum likelihood estimates make the fitted proportions of the two groups equal to the observed proportions, $\hat\beta_0 = \operatorname{logit}(c/(c + d))$ and $\hat\beta_0 + \hat\beta_1 = \operatorname{logit}(a/(a + b))$, and subtracting gives $\hat\beta_1 = \ln[ad/(bc)]$. $\square$

**Example 14.2.1 (Smoking)** Logistic regression of low on smoke gives $\hat\beta_0 = -1.087$ and $\hat\beta_1 = 0.704$ (standard error 0.320). The odds of low birth weight for nonsmoking mothers are $\mathrm{e}^{-1.087} = 0.337 = 29/86$ and for smoking mothers $\mathrm{e}^{-1.087 + 0.704} = 0.682 = 30/44$, so $\widehat{\mathrm{OR}} = \mathrm{e}^{0.704} = 2.02$, exactly the same as the 2×2 table of [7.7.9](/7.7.9); the 95% interval $\exp(0.704 \pm 1.96 \times 0.320) = (1.08, 3.78)$ is Woolf's interval ([7.7.13](/7.7.13) Formula 13.2.1).

### 14.2.2. Continuous and Multicategory Independent Variables

For a continuous independent variable $\mathrm{e}^\beta$ is the odds ratio per unit increase; when the unit is too small it is easier to read the $\mathrm{e}^{\Delta\beta}$ of a clinically meaningful increment $\Delta$. The coefficient of maternal weight is $-0.0141$ (standard error 0.0062), and the OR per 10 lb is $\mathrm{e}^{-0.141} = 0.87$ (95% interval 0.77–0.98). This OR is the same at every weight, which is an assumption of the model (log odds linear); it does not mean that the probability falls by the same amount per 10 lb. Multicategory variables use **dummy variables** ([7.7.10](/7.7.10), Section 10.7.3): with white as reference, the ORs for black and "other" race are 2.33 (0.94–5.77) and 1.89 (0.96–3.74).

## 14.3. Estimation and Inference

### 14.3.1. Maximum Likelihood Estimation

Let there be $n$ independent individuals with $p_i = \mathbb{P}(Y_i = 1 \mid \boldsymbol{x}_i)$. The log-likelihood is

$$
\ell(\boldsymbol{\beta}) = \sum_{i=1}^n \bigl[y_i \ln p_i + (1 - y_i)\ln(1 - p_i)\bigr], \qquad \operatorname{logit} p_i = \boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}.
$$
The score equations $X^{\mathsf T}(\boldsymbol{y} - \boldsymbol{p}) = \boldsymbol{0}$ have no explicit solution and are solved by **Newton's method**; for logistic regression the Hessian does not depend on $\boldsymbol{y}$, so Newton's method is the same as **Fisher scoring**, and each step is a weighted least-squares fit, that is **iteratively reweighted least squares** ([3.5.5 Algorithm 5.1.2](/3.5.5#alg-5.1.2)). The value of $-\nabla^2\ell$ at $\hat{\boldsymbol{\beta}}$, $X^{\mathsf T}\hat WX$ ($\hat W = \operatorname{diag}\{\hat p_i(1 - \hat p_i)\}$), is an estimate of the **Fisher information matrix**, and its inverse gives the approximate covariance matrix of $\hat{\boldsymbol{\beta}}$.

When a variable in the data completely separates the two outcomes (such as all people in one category being cases), the likelihood increases monotonically as $\beta \to \infty$ and the MLE does not exist (complete separation); software may give huge coefficients and standard errors without necessarily reporting an error. Watch for this in small samples and with rare categories; Firth's penalized likelihood can be used.

### 14.3.2. Three Tests

**Definition 14.3.1 (Wald Test and Likelihood Ratio Test)** For testing $H_0\colon \beta_j = 0$, the test with statistic $z = \hat\beta_j/\operatorname{SE}(\hat\beta_j)$ (or $z^2 \overset{H_0}{\approx} \chi^2_1$) is called the **Wald test**. For comparing two nested models, the test with statistic $G = 2[\ell(\hat{\boldsymbol{\beta}}_{\text{large}}) - \ell(\hat{\boldsymbol{\beta}}_{\text{small}})] \overset{H_0}{\approx} \chi^2_q$ ($q$ the difference in the numbers of parameters of the two models) is the **likelihood ratio test**.

The third is the score test, fitted under $H_0$ only; for a single binary independent variable it is Pearson's chi-square test for the 2×2 table. In Example 14.2.1 the Wald statistic is $z^2 = (0.704/0.320)^2 = 4.85$, the likelihood ratio is $G = 4.87$ and Pearson's $X^2 = 4.92$, with $p$ about 0.027 for all: in large samples the three agree. They can differ in small samples or when a coefficient is large, and the likelihood ratio test is then more reliable; the Wald test fails badly near complete separation (the standard error grows faster than the coefficient and $z$ actually becomes smaller). To test several coefficients simultaneously equal to 0 (such as the two dummy variables for race) use the likelihood ratio test or the multivariate Wald test.

**Formula 14.3.1 (Profile Likelihood Interval)** The 95% profile likelihood interval for $\beta_j$ is the set of $\beta_j$ for which $2[\ell(\hat{\boldsymbol{\beta}}) - \max_{\boldsymbol{\beta}_{-j}} \ell(\beta_j, \boldsymbol{\beta}_{-j})] \le \chi^2_{1, 0.05} = 3.84$. It is the inversion of the likelihood ratio test, does not require the log-likelihood to be quadratic, and is invariant under reparametrization.

In Example 14.2.1 the profile interval for the OR of smoking is (1.08, 3.80), almost the same as the Wald interval (1.08, 3.78); when events are few the two can differ noticeably, and the profile interval is more reliable (R's `confint` gives profile intervals by default, while statsmodels gives Wald intervals).

## 14.4. Multiple Logistic Regression

### 14.4.1. Adjusted Odds Ratios

**Example 14.4.1 (Risk Factors for Low Birth Weight)** Put the mother's age, weight, race, smoking, previous premature labor (ptl > 0) and history of hypertension into the model together:

| Variable | $\hat\beta$ | SE | Adjusted OR (95% interval) | $p$ | Univariate OR |
|---|---|---|---|---|---|
| Age (per 5 years) | $-0.0428$ (per year) | 0.0376 | 0.81 (0.56, 1.17) | 0.25 | 0.77 |
| Weight (per 10 lb) | $-0.0154$ (per lb) | 0.0070 | 0.86 (0.75, 0.98) | 0.028 | 0.87 |
| Black (vs white) | 1.168 | 0.533 | 3.22 (1.13, 9.14) | 0.028 | 2.33 |
| Other race (vs white) | 0.815 | 0.443 | 2.26 (0.95, 5.38) | 0.066 | 1.89 |
| Smoking | 0.858 | 0.405 | 2.36 (1.07, 5.22) | 0.034 | 2.02 |
| Previous premature labor | 1.334 | 0.458 | 3.80 (1.55, 9.31) | 0.004 | 4.32 |
| History of hypertension | 1.741 | 0.703 | 5.70 (1.44, 22.6) | 0.013 | 3.37 |

The intercept is 0.925. The overall likelihood ratio test of the model (against the intercept-only model) is $G = 35.5$ with 7 degrees of freedom and $p = 9 \times 10^{-6}$; the likelihood ratio test of the two dummy variables for race is $G = 6.24$ with 2 degrees of freedom and $p = 0.044$; that for smoking is $G = 4.62$, $p = 0.032$.

After adjustment the OR for smoking rises from 2.02 to 2.36: as in the analysis of covariance for birth weight in [7.7.12](/7.7.12) Example 12.6.1, race masks the effect of smoking here, since in this sample white mothers smoke most and the babies of white mothers have low birth weight less often to begin with. With only race adjusted for, the OR for smoking is 3.05, with weight added it is 2.89, and it falls back after previous premature labor is added (previous premature labor is more common among smokers, and part of the risk of smokers is expressed through it). Which variables to adjust for is not a statistical question but depends on their position in the causal structure: if previous premature labor is a consequence of smoking (lying on the pathway "smoking → tendency to premature labor → low birth weight"), adjusting for it removes part of the effect of smoking. This is the question taken up in [7.7.15](/7.7.15).

![Odds ratios for low birth weight (189 deliveries, Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt). Open circles are univariate logistic regressions, filled squares are the multiple model containing maternal age, weight, race, smoking, previous premature labor and history of hypertension together, and the segments are 95% Wald intervals (log scale). Age is per 5 years and weight per 10 lb. After adjustment the odds ratios for smoking and race become larger, because white mothers smoke most and have low birth weight less often](./plots/or-forest.py)

### 14.4.2. Predicted Probabilities

The fitted model gives the risk of any kind of person: for a 25-year-old nonsmoking white mother weighing 130 lb with no previous premature labor or hypertension, $\operatorname{logit}\hat p = 0.925 - 0.0428 \times 25 - 0.0154 \times 130 = -2.15$ and $\hat p = 0.104$; for a smoker in the same circumstances $\operatorname{logit}\hat p = -2.15 + 0.858 = -1.29$ and $\hat p = 0.215$; if both previous premature labor and hypertension are present, $\hat p = 0.716$ for the nonsmoker and $\hat p = 0.856$ for the smoker. The OR is the same in all kinds of people (2.36), but the risk difference varies with baseline risk: smoking increases the risk by 0.111 in low-risk mothers and by 0.140 in mothers with previous premature labor and hypertension. This is the model version of the statement "effect modification depends on scale" of [7.7.13](/7.7.13), Section 13.6.2.

### 14.4.3. Interaction

An **interaction effect** is represented by a product term, with the same meaning as in linear regression ([7.7.10](/7.7.10), Section 10.7.4), but on the logit scale: the OR varies with another variable. Adding "age × smoking" to the model of Example 14.4.1 gives a likelihood ratio $G = 0.30$, $p = 0.58$; adding "race × smoking" (two product terms) gives $G = 1.85$ with 2 degrees of freedom and $p = 0.40$: there is no evidence that the OR for smoking varies with age or race. The power of tests of interaction is far lower than that of tests of main effects (the data on 59 low-birth-weight infants are insufficient to detect modification of moderate size), and "not significant" does not mean that "the OR is the same in all groups".

### 14.4.4. Comparison with Linear Regression

| | Linear regression | Logistic regression |
|---|---|---|
| Outcome | Continuous | 0/1 (or number of events among $n$) |
| Model | $\mathbb{E}(Y \mid \boldsymbol{x}) = \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$ | $\operatorname{logit}\mathbb{P}(Y = 1 \mid \boldsymbol{x}) = \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$ |
| Meaning of a coefficient | Difference of means | Log odds ratio |
| Estimation | Least squares (explicit solution) | Maximum likelihood (iterative) |
| Tests | $t$, $F$ | Wald $z$, likelihood ratio $\chi^2$ |
| Measures of fit | $R^2$, residual sum of squares | Deviance, AIC, AUC, calibration |
| Assumptions not needed | — | Normality and equal variance (the variance is determined by $p(1 - p)$) |

## 14.5. Model Evaluation

### 14.5.1. Deviance

**Definition 14.5.1 (Deviance)** Twice the difference between the log-likelihood of a model and that of the saturated model (each observation has its own parameter and the fitted value equals the observed value),

$$
D = 2\bigl[\ell_{\text{saturated}} - \ell(\hat{\boldsymbol{\beta}})\bigr],
$$
is called the **deviance** of the model. The difference between the deviances of two nested models is the likelihood ratio statistic $G$.

For individual 0/1 data, $\ell_{\text{saturated}} = 0$ and $D = -2\ell(\hat{\boldsymbol{\beta}})$; for the model of Example 14.4.1, $D = 199.2$, while for the intercept-only model (the null deviance) it is 234.7, and the difference 35.5 is the overall test above. For 0/1 data $D$ does not follow $\chi^2_{n-k-1}$ and cannot be used to test goodness of fit; $D \overset{\cdot}{\sim} \chi^2$ holds only when the data are grouped by covariate pattern with fairly many individuals per group (such as the dose groups of Section 14.6). Non-nested models are compared by the **Akaike information criterion** $\mathrm{AIC} = D + 2(k + 1)$ ([7.7.11](/7.7.11), Section 11.8.2); for Example 14.4.1 it is 215.2.

### 14.5.2. Calibration: The Hosmer–Lemeshow Test

**Definition 14.5.2 (Hosmer–Lemeshow Test)** Sort the individuals by predicted probability, divide them into $g$ groups (usually $g = 10$), and compare the observed number of events $O_k$ in each group with the predicted number $E_k = \sum_{i \in k}\hat p_i$:

$$
\hat C = \sum_{k=1}^g \frac{(O_k - E_k)^2}{E_k(1 - E_k/n_k)} \overset{\cdot}{\sim} \chi^2_{g-2}.
$$
This test is called the **Hosmer–Lemeshow test**; a small $p$-value indicates that the predicted probabilities and the observed frequencies disagree (poor calibration).

For the model of Example 14.4.1, $\hat C = 8.65$ with 8 degrees of freedom and $p = 0.37$. This test should be used with caution: the result depends on how the groups are formed (another grouping may give a different conclusion), its power is very low in small samples, and in large samples any small departure is significant. More informative is the calibration plot: the observed proportion in each group against its mean predicted probability, ideally lying on the diagonal.

### 14.5.3. Discrimination: The AUC

Treating the predicted probability of the model as a continuous "test" and calling people high-risk at different thresholds gives an **ROC curve** ([7.7.3](/7.7.3), Section 3.4). Its **area under the curve** is the probability that a randomly chosen case has a higher predicted probability than a randomly chosen non-case ([7.7.3](/7.7.3) Theorem 3.4.1), that is, the Mann–Whitney statistic $U/(n_1 n_0)$ (the **Wilcoxon rank-sum test**, [7.7.8](/7.7.8)); here it is also called the $c$ statistic.

**Example 14.5.1** The AUC of the model of Example 14.4.1 is 0.750: among the $59 \times 130 = 7670$ pairs of the 59 low-birth-weight and 130 normal-weight infants, in 75% the former has the higher predicted risk. With smoking as the only variable the AUC is 0.585. On the decile calibration plot the observed proportions agree roughly with the diagonal over the whole range of predicted probabilities.

![Discrimination and calibration of the multiple logistic model for birthwt (maternal age, weight, race, smoking, previous premature labor, history of hypertension) (189 deliveries, Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt). A: the ROC curve of the fitted probabilities (AUC 0.750) and the ROC curve with smoking alone (AUC 0.585). B: calibration plot: divided by predicted risk into ten groups (18 or 19 each), the observed proportion of each group against the mean predicted probability, with 95% Wilson intervals as error bars; Hosmer–Lemeshow statistic 8.65 with 8 degrees of freedom (p = 0.37). The model is evaluated on the same data that were used to fit it, and both measures are optimistic](./plots/roc-calibration.py)

Discrimination and calibration are different things: multiplying all the predicted probabilities by 0.5 leaves the AUC unchanged (the ordering is unchanged) but destroys the calibration. Both should be reported; evaluating on the same data used to fit the model overestimates its performance (overfitting), and external validation, cross-validation and bootstrap correction of optimism are in [7.7.21](/7.7.21).

## 14.6. Binary Dose Response: Logit and Probit Analysis

### 14.6.1. Toxicity Experiments

In toxicology and pharmacology, animals are often divided into groups exposed to different doses and the number of deaths (or responders) in each group is recorded. The dose-response curves of [7.7.11](/7.7.11), Section 11.6, described continuous responses (enzyme activity, optical density); here the response of each animal is "dies or does not", and the data are binomial counts, the grouped form of logistic regression: $Y_j \sim \mathrm{Bin}(n_j, p_j)$ and $g(p_j) = \beta_0 + \beta_1 x_j$, with $x_j$ usually the log dose.

**Definition 14.6.1 (Probit Model and Median Lethal Dose)** Binomial regression with the inverse of the standard normal distribution function as link, $\Phi^{-1}(p) = \beta_0 + \beta_1 x$, is called the **probit model**. The dose that kills half the individuals in a population is called the **median lethal dose** ($\mathrm{LD}_{50}$); in experiments with inhalation or exposure in water the corresponding quantity is the median lethal concentration $\mathrm{LC}_{50}$. In the logit and probit models $p = 0.5$ corresponds to $\eta = 0$, and $\log_{10}\mathrm{LD}_{50} = -\beta_0/\beta_1$.

The probit model has a mechanistic interpretation (the tolerance model): each individual has its own lethal threshold whose logarithm is normally distributed, and the individual dies when the dose exceeds the threshold, so the proportion dead is the distribution function of the thresholds. The logit corresponds to thresholds with a logistic distribution; the two have almost the same shape, with coefficients differing by a factor of about 1.6–1.8. The $\mathrm{LD}_{50}$ is the median of the threshold distribution ([7.7.2](/7.7.2)), and the larger $\beta_1$, the more concentrated the thresholds and the steeper the curve.

### 14.6.2. Bliss's Beetle Data

**Example 14.6.1** Bliss (1935) exposed flour beetles for 5 hours to carbon disulfide vapor at eight concentrations and recorded the deaths:

| $\log_{10}$ concentration (mg/L) | 1.6907 | 1.7242 | 1.7552 | 1.7842 | 1.8113 | 1.8369 | 1.8610 | 1.8839 |
|---|---|---|---|---|---|---|---|---|
| Number of beetles | 59 | 60 | 62 | 56 | 63 | 59 | 62 | 60 |
| Number dead | 6 | 13 | 18 | 28 | 52 | 53 | 61 | 60 |

Fits with three link functions:

| Link function | $\hat\beta_0$ | $\hat\beta_1$ (SE) | Deviance (6 degrees of freedom) | $\mathrm{LD}_{50}$ (mg/L, 95% interval) |
|---|---|---|---|---|
| logit | $-60.72$ | 34.27 (2.91) | 11.23 | 59.1 (58.1, 60.2) |
| probit | $-34.94$ | 19.73 (1.49) | 10.12 | 59.0 (58.0, 60.0) |
| complementary log-log $\ln[-\ln(1 - p)]$ | $-39.57$ | 22.04 (1.80) | 3.45 | 60.1 (59.0, 61.2) |

The data are grouped by dose with about 60 animals per group, so the deviance can serve as a test of goodness of fit: the logit's $D = 11.23$ corresponds to $p = 0.08$, and the residuals show that it underestimates mortality at low doses and overestimates it at middle doses; the asymmetric complementary log-log link (which corresponds to thresholds with an extreme-value distribution, with the curve approaching 1 faster at the high-dose end) has $D = 3.45$, clearly better. The $\mathrm{LD}_{50}$ of all three models lies at 59–60 mg/L, a difference far smaller than when estimating the $\mathrm{LD}_{10}$ or $\mathrm{LD}_{99}$ in the tails of the curve: the choice of model mainly affects the tails.

![Dose–mortality relationship of flour beetles exposed to carbon disulfide vapor for 5 hours (Bliss 1935; 8 concentrations, 481 beetles). Dots are the observed proportions dead, the horizontal axis is log10 concentration (mg/L); the curves are the maximum likelihood fits of binomial regression with logit, probit and complementary log-log (cloglog) links. The dotted line marks the median lethal concentration 59.1 mg/L (95% interval 58.1–60.2) estimated by the logit model. Residual deviance: logit 11.2, probit 10.1, cloglog 3.4 (6 degrees of freedom)](./plots/beetle-dose.py)

### 14.6.3. Intervals for the LD50

$\theta = \log_{10}\mathrm{LD}_{50} = -\beta_0/\beta_1$ is a ratio of parameters and has two kinds of interval.

**Formula 14.6.1 (Confidence Intervals for the LD50)** Delta method: $\operatorname{Var}(\hat\theta) \approx \boldsymbol{g}^{\mathsf T}\hat V\boldsymbol{g}$, $\boldsymbol{g} = (-1/\hat\beta_1, \hat\beta_0/\hat\beta_1^2)^{\mathsf T}$, $\hat V$ the covariance matrix of $(\hat\beta_0, \hat\beta_1)$, and the interval is $\hat\theta \pm 1.96\sqrt{\operatorname{Var}(\hat\theta)}$. Fieller's method: the interval for $\theta$ is the set of $\theta$ with $(\hat\beta_0 + \theta\hat\beta_1)^2 \le 1.96^2 \operatorname{Var}(\hat\beta_0 + \theta\hat\beta_1)$, that is, the solution of a quadratic inequality in $\theta$.

Fieller's interval does not depend on a linear approximation to the ratio and can be asymmetric; when the slope is not significantly different from 0 it is even unbounded, correctly reflecting that the $\mathrm{LD}_{50}$ cannot then be estimated. The slope in the Bliss data is extremely significant ($z = 11.8$), and the two intervals are almost the same: the Delta and Fieller intervals of the logit model are both 58.1–60.2 mg/L (1.7642–1.7793 and 1.7639–1.7792 before taking antilogarithms). When comparing the potency of two drugs, the horizontal distance between parallel dose-response lines is the logarithm of the relative potency ([7.7.11](/7.7.11), Section 11.6.2), which can be estimated by adding a dummy variable for the drug to the probit or logit model.

## 14.7. Conditional Logistic Regression

In a matched case-control study ([7.7.13](/7.7.13), Section 13.8) each matched set has its own baseline risk. If each set is given an intercept, the number of parameters grows with the number of sets, and the unconditional maximum likelihood estimate is not consistent: for 1:1 pairs and one binary exposure it converges to $2\ln(b/c)$, squaring the OR.

**Definition 14.7.1 (Conditional Logistic Regression)** Conditioning on "exactly this many cases in the set", the likelihood formed from the conditional probability that the case is the actual person (or persons) is

$$
L(\boldsymbol{\beta}) = \prod_{\text{set } s} \frac{\exp(\boldsymbol{x}_{s,\text{case}}^{\mathsf T}\boldsymbol{\beta})}{\sum_{j \in s}\exp(\boldsymbol{x}_{sj}^{\mathsf T}\boldsymbol{\beta})}
$$
(with one case per set), in which the intercept of each set is cancelled; the method of estimating $\boldsymbol{\beta}$ from it is called **conditional logistic regression**.

For 1:1 pairs and one binary exposure, the conditional MLE is exactly $\ln(b/c)$ and the test is McNemar's test ([7.7.13](/7.7.13) Formula 13.8.1); conditional logistic regression extends this to 1:$m$ matching and several covariates. This likelihood has the same form as the partial likelihood of Cox regression (each matched set is like a risk set, [7.7.16](/7.7.16)), and software often fits it with the Cox routine. A study stratified by the matching factors (age–sex strata with many people in each) can instead add dummy variables for the strata directly in ordinary logistic regression.

## 14.8. Generalized Linear Models and Poisson Regression

### 14.8.1. The Framework

Linear regression, logistic regression and the probit model are all special cases of the **generalized linear model** ([3.3.6](/3.3.6)). A GLM has three components:

| Component | Meaning | Linear regression | Logistic regression | Poisson regression |
|---|---|---|---|---|
| Random part | $Y_i$ has a distribution in the **exponential family** | Normal | Binomial | Poisson |
| Linear predictor | $\eta_i = \boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}$ | | | |
| **Link function** | $g(\mu_i) = \eta_i$ | Identity | Logit (or probit) | Log |
| Variance function | $\operatorname{Var}(Y_i) = \phi V(\mu_i)$ | $\sigma^2$ | $\mu(1 - \mu)/n$ | $\mu$ |
| Meaning of $\mathrm{e}^\beta$ | — | — | Odds ratio | Rate ratio |

All GLMs are fitted by the same IRLS algorithm and models are compared by deviance and likelihood ratio tests; they differ only in distribution and link function.

### 14.8.2. Counts and Rates: The Offset

**Definition 14.8.1 (Poisson Regression and the Offset)** Let $Y_i$ be the number of events in group $i$ in person-time $T_i$, $Y_i \sim \mathrm{Poi}(\mu_i)$, with

$$
\ln\mu_i = \ln T_i + \boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta},
$$
that is, the logarithm of the incidence rate $\mu_i/T_i$ is a linear function of the independent variables. This model is called **Poisson regression**, and the term $\ln T_i$ whose coefficient is fixed at 1 is called the **offset**. $\mathrm{e}^{\beta_j}$ is the rate ratio for a 1-unit increase in $x_j$.

The offset puts "rates" into a model for counts: different groups have different person-time, and what is compared is the rates and not the counts. With a single binary independent variable $\mathrm{e}^{\hat\beta}$ is the crude rate ratio of the two groups; when the data are grouped by strata and dummy variables for the strata are added, it is the rate ratio adjusted for the strata, very close to the Mantel–Haenszel rate ratio.

**Example 14.8.1 (Coronary Deaths Among British Doctors)** Use as data the 10 groups (5 age groups × smoking or not) of [7.7.13](/7.7.13) Example 13.5.1, with age groups coded 1–5:

| Model | Rate ratio for smoking (95% interval) | Deviance | Degrees of freedom |
|---|---|---|---|
| Smoking | 1.72 (1.39, 2.12) | 906.0 | 8 |
| Age group (4 dummy variables) + smoking | 1.43 (1.15, 1.76) | 12.13 | 4 |
| Age + age² + smoking | 1.43 (1.15, 1.76) | 12.18 | 6 |
| Age + age² + smoking + smoking × age | see below | 1.64 | 5 |

With smoking alone the rate ratio is the crude rate ratio 1.72; with age added it falls to 1.43, in agreement with the age-standardized 1.42 ([7.7.13](/7.7.13) Example 13.5.2). But the deviance of "age group + smoking" is 12.13 (4 degrees of freedom, $p = 0.016$): the assumption that the effect of smoking is the same in all age groups does not hold. Adding the smoking × age interaction reduces the deviance to 1.64 (5 degrees of freedom, $p = 0.90$), and the likelihood ratio for the interaction term is $G = 10.5$, $p = 0.001$. The final model is

$$
\ln\frac{\mu}{T} = -10.79 + 2.377\,\text{age} - 0.198\,\text{age}^2 + 1.441\,\text{smoking} - 0.308\,\text{smoking} \times \text{age},
$$
and the rate ratio for smoking is $\exp(1.441 - 0.308a)$: 3.11 at ages 35–44 ($a = 1$), 2.28 at 45–54, 1.68 at 55–64, 1.23 at 65–74 and 0.91 at 75–84. This is the effect modification seen in the stratified analysis ([7.7.13](/7.7.13), Section 13.6.2), summarized by the model in two parameters (instead of five stratum rate ratios).

![Poisson regression of coronary deaths in the 10-year follow-up of British male doctors (Doll and Hill 1966; as arranged by Breslow and Day 1987). A: observed death rates (dots, per 100 000 person-years) and the fitted rates (lines) of the model log(deaths) = log(person-years) + b0 + b1 age + b2 age² + b3 smoking + b4 smoking × age, with age coded 1–5 in 10-year groups (residual deviance 1.6, 5 degrees of freedom). B: the fitted rate ratio exp(b3 + b4 age) with its 95% interval band, and the observed rate ratios of the age groups as dots](./plots/doctors-poisson.py)

### 14.8.3. Overdispersion

The variance of a Poisson distribution equals its mean. If the risks of individuals within the same group are not the same (unmeasured heterogeneity), or the events are not independent (clustering of infectious disease), the variance of the counts will exceed the mean, which is **overdispersion** ([7.7.9](/7.7.9)). The coefficients of Poisson regression are still consistent, but the standard errors are underestimated and the tests are too optimistic.

The check is to look at Pearson's statistic $X^2 = \sum(y_i - \hat\mu_i)^2/\hat\mu_i$ or the ratio of the deviance to the residual degrees of freedom: a value clearly greater than 1 suggests overdispersion (provided that the mean part of the model is correct; in Example 14.8.1 the $D/\mathrm{df} = 2.0$ of the model without the interaction came from the omitted interaction and not from overdispersion; after the interaction is added $X^2 = 1.55$ with 5 degrees of freedom and there is no overdispersion). There are two remedies: the quasi-Poisson approach keeps the Poisson mean model and multiplies the variance by an estimated dispersion parameter $\hat\phi = X^2/\mathrm{df}$, multiplying the standard errors by $\sqrt{\hat\phi}$; negative binomial regression assumes $\operatorname{Var}(Y) = \mu + \alpha\mu^2$, which corresponds to a mixture in which the Poisson rates of the individuals have a Gamma distribution (the **negative binomial distribution**, [7.7.4](/7.7.4)). The read counts of RNA-seq are severely overdispersed count data, and the negative binomial GLM is the standard model for differential expression analysis ([7.7.20](/7.7.20)).

## 14.9. Sample Size: Events per Variable

The information in logistic regression depends mainly on the number of the less frequent outcome and not on the total sample size. The rule of thumb is at least about 10 events for each independent variable (each parameter) (events per variable, EPV): simulation studies show that below an EPV of 10 the coefficients are noticeably biased, the coverage of intervals is inadequate and variable selection is unstable. Example 14.4.1 has 59 low-birth-weight infants and 7 parameters, an EPV of about 8.4, slightly below this standard: this is an exploratory model, and its coefficients (especially for history of hypertension, with only 12 mothers having it and an interval of 1.4–22.6) should not be over-interpreted.

The EPV rule is only a rough lower bound. Modern sample-size methods compute the required sample size from the expected performance of the model (the predicted $R^2$, the acceptable degree of overfitting, the precision of calibration) ([7.7.21](/7.7.21)); when only the OR of one exposure (such as smoking) is to be tested, the sample size is computed from the formula for comparing two proportions ([7.7.9](/7.7.9), Section 9.4) and enlarged according to the correlation of exposure with the covariates, by a factor of about $1/(1 - R^2)$, where $R^2$ is the coefficient of determination of the regression of exposure on the other covariates.

## 14.10. Computing in Python

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import roc_auc_score

bw = pd.read_csv("birthwt.csv")
bw["ptd"] = (bw.ptl > 0).astype(int)
binom = sm.families.Binomial()

# univariate model: exp(coef) is the 2 x 2 odds ratio (Example 14.2.1)
m0 = smf.glm("low ~ smoke", bw, family=binom).fit()
print(np.exp(m0.params), np.exp(m0.conf_int()))        # OR 2.02 (1.08, 3.78), Wald
print(m0.null_deviance - m0.deviance)                   # likelihood ratio G = 4.87

# multiple logistic regression (Example 14.4.1)
m = smf.glm("low ~ age + lwt + C(race) + smoke + ptd + ht", bw, family=binom).fit()
print(pd.DataFrame({"OR": np.exp(m.params), "lo": np.exp(m.conf_int()[0]), "hi": np.exp(m.conf_int()[1])}))
m_norace = smf.glm("low ~ age + lwt + smoke + ptd + ht", bw, family=binom).fit()
print(m_norace.deviance - m.deviance)                   # G = 6.24 on 2 df for race
m_int = smf.glm("low ~ age * smoke + lwt + C(race) + ptd + ht", bw, family=binom).fit()
print(m.deviance - m_int.deviance)                      # G = 0.30 for age x smoking

# discrimination and calibration (Example 14.5.1, Definition 14.5.2)
p = m.predict(bw)
print(roc_auc_score(bw.low, p))                         # 0.750
g = pd.qcut(p.rank(method="first"), 10, labels=False)
tab = pd.DataFrame({"o": bw.low, "e": p, "g": g}).groupby("g").agg(o=("o", "sum"), e=("e", "sum"), n=("o", "size"))
print((((tab.o - tab.e) ** 2) / (tab.e * (1 - tab.e / tab.n))).sum())   # Hosmer-Lemeshow 8.65

# grouped binomial data, three links, LD50 by the delta method (Example 14.6.1)
x = np.array([1.6907, 1.7242, 1.7552, 1.7842, 1.8113, 1.8369, 1.8610, 1.8839])
n = np.array([59, 60, 62, 56, 63, 59, 62, 60]); k = np.array([6, 13, 18, 28, 52, 53, 61, 60])
for link in (sm.families.links.Logit(), sm.families.links.Probit(), sm.families.links.CLogLog()):
    f = sm.GLM(np.column_stack([k, n - k]), sm.add_constant(x), family=sm.families.Binomial(link)).fit()
    print(type(link).__name__, f.params.round(2), round(f.deviance, 2))
f = sm.GLM(np.column_stack([k, n - k]), sm.add_constant(x), family=binom).fit()
b0, b1 = f.params
theta = -b0 / b1
grad = np.array([-1 / b1, b0 / b1**2])
se = np.sqrt(grad @ f.cov_params() @ grad)
print(10**theta, 10 ** (theta + np.array([-1.96, 1.96]) * se))   # 59.1 (58.1, 60.2) mg/L

# Poisson regression with an offset (Example 14.8.1)
d = pd.DataFrame({"age": [1, 2, 3, 4, 5] * 2, "smoke": [1] * 5 + [0] * 5,
                  "deaths": [32, 104, 206, 186, 102, 2, 12, 28, 28, 31],
                  "py": [52407, 43248, 28612, 12663, 5317, 18790, 10673, 5710, 2585, 1462]})
pois = smf.glm("deaths ~ age + I(age**2) + smoke + smoke:age", d,
               family=sm.families.Poisson(), offset=np.log(d.py)).fit()
print(pois.params, pois.deviance, pois.pearson_chi2)    # deviance 1.64, Pearson 1.55 on 5 df
# overdispersed counts: sm.families.NegativeBinomial(alpha=...) or smf.negativebinomial(...)
# matched sets: statsmodels.discrete.conditional_models.ConditionalLogit(y, X, groups=set_id)
```

## Summary

- A binary outcome is modeled linearly through the **logit** (Definition 14.1.1): $\operatorname{logit}\mathbb{P}(Y = 1 \mid \boldsymbol{x}) = \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$; $\mathrm{e}^{\beta_j}$ is the **odds ratio** adjusted for the other variables (Theorem 14.2.1), and for a single binary independent variable it equals the OR of the 2×2 table (Example 14.2.1).
- Estimation is by maximum likelihood (IRLS); Wald and likelihood ratio tests (Definition 14.3.1) and profile likelihood intervals (Formula 14.3.1); with complete separation the MLE does not exist.
- birthwt (Example 14.4.1): after adjustment for race, weight, previous premature labor, history of hypertension and age, the OR for smoking is 2.36 (1.07–5.22), larger than the crude OR 2.02, because race masked the effect of smoking; interaction terms are nonsignificant but the power is low. With a constant OR the risk difference varies with baseline risk (Section 14.4.2).
- Model evaluation: the **deviance** (Definition 14.5.1) is for comparing nested models (it cannot be used to test goodness of fit for 0/1 data) and AIC for non-nested models; calibration is assessed by the **Hosmer–Lemeshow test** (Definition 14.5.2, 8.65, $p = 0.37$) and calibration plots, and discrimination by the AUC $= U/(n_1n_0)$ (0.750, Example 14.5.1).
- Binary dose response (Definition 14.6.1): logit, probit and complementary log-log links; the $\mathrm{LD}_{50}$ of Bliss's beetles is 59–60 mg/L, with the cloglog fitting best (Example 14.6.1); intervals use the delta method or Fieller's method (Formula 14.6.1).
- Matched data use **conditional logistic regression** (Definition 14.7.1), which reduces to $b/c$ and McNemar's test for 1:1 matching.
- The **generalized linear model**: distribution, link function and linear predictor (the table of Section 14.8.1). Counts and rates use **Poisson regression** with an **offset** (Definition 14.8.1): the rate ratio for coronary disease among British doctors is adjusted from the crude 1.72 to 1.43, and the interaction term shows it falling from 3.1 at ages 35–44 to 0.9 at ages 75–84 (Example 14.8.1). Overdispersion is handled by quasi-Poisson or negative binomial regression.
- Sample size: about 10 events per parameter (Section 14.9).

## Questions

1. A study reports a logistic regression coefficient of $\hat\beta = 0.405$ with standard error 0.15 for a factor. Find the OR with its 95% interval and the Wald $p$-value. If the factor is a continuous variable (in mmHg), how should the OR per 10 mmHg be reported?

   **Answer** $\mathrm{OR} = \mathrm{e}^{0.405} = 1.50$ with interval $\exp(0.405 \pm 1.96 \times 0.15) = \exp(0.111, 0.699) = (1.12, 2.01)$; $z = 0.405/0.15 = 2.70$ and $p = 0.007$. If the unit is mmHg, the OR per 10 mmHg is $\mathrm{e}^{10 \times 0.405} = \mathrm{e}^{4.05} = 57$ with interval $\exp(10 \times (0.111, 0.699)) = (3.0, 1086)$; so large a number suggests that the unit of the original coefficient is probably not mmHg or that the variable was standardized, and the unit must be stated before reporting. In general the OR per $\Delta$ units is $\mathrm{e}^{\Delta\beta}$, and the endpoints of the interval are multiplied by $\Delta$ before exponentiating.

2. Prove that the component of the score equations of logistic regression that contains the intercept implies $\sum_i \hat p_i = \sum_i y_i$, that is, the total predicted number of events equals the total observed number. What does this imply for the sum over the groups of the Hosmer–Lemeshow test?

   **Answer** $\partial\ell/\partial\beta_0 = \sum_i (y_i - p_i) \cdot 1 = 0$, so $\sum\hat p_i = \sum y_i$ at the MLE. Similarly, the score equation of each binary independent variable implies that, among the people for whom the variable is 1, the predicted number of events equals the observed number. Thus the $O_k - E_k$ of the Hosmer–Lemeshow groups sum to 0, and the departures of the groups can only cancel one another, which is one reason why the degrees of freedom of the test statistic are $g - 2$ and not $g$ (the constraint on another parameter comes, approximately, from the score equation in the direction of the slope).

3. Fit the logistic regression $\operatorname{logit}\mathbb{P}(\text{case} \mid \boldsymbol{x}) = \beta_0^* + \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$ in a case-control study. Explain why $\boldsymbol{\beta}$ can be interpreted as the log odds ratios in the population whereas the intercept $\beta_0^*$ cannot be interpreted as the baseline risk in the population.

   **Answer** Let the sampling proportion of cases be $f_1$ and of non-cases $f_0$, independent of $\boldsymbol{x}$. By Bayes' formula, in the sample $\mathbb{P}(\text{case} \mid \boldsymbol{x}, \text{selected}) / \mathbb{P}(\text{control} \mid \boldsymbol{x}, \text{selected}) = (f_1/f_0) \times$ the odds in the population. Taking logarithms, the logit increases only by the constant $\ln(f_1/f_0)$: $\beta_0^* = \beta_0 + \ln(f_1/f_0)$ and the slopes are unchanged. So the slopes are the log odds ratios of the population (the regression version of [7.7.13](/7.7.13) Theorem 13.2.1), whereas the intercept depends on the ratio of cases to controls chosen by the investigator; to obtain population risk, external information on incidence is needed to correct the intercept.

4. Using the coefficients of Example 14.4.1, compute the predicted probability of low birth weight for a 30-year-old black smoking mother weighing 110 lb (no previous premature labor, no hypertension), and the change in the predicted probability if she stopped smoking in pregnancy (assuming everything else unchanged and the coefficients of the model to be causal effects).

   **Answer** $\operatorname{logit}\hat p = 0.925 - 0.0428 \times 30 - 0.0154 \times 110 + 1.168 + 0.858 = 0.925 - 1.284 - 1.694 + 1.168 + 0.858 = -0.027$, so $\hat p = 1/(1 + \mathrm{e}^{0.027}) = 0.493$. Not smoking: $\operatorname{logit} = -0.885$ and $\hat p = 0.292$. The risk difference is about 0.20, far greater than the 0.11 of the low-risk mother in Section 14.4.2: the same OR of 2.36 corresponds to a greater absolute benefit at high baseline risk. "Assuming the coefficients are causal" is a strong assumption: variables such as previous premature labor may lie on the causal pathway of smoking, and adjusting for them makes the coefficient of smoking underestimate the total effect ([7.7.15](/7.7.15)).

5. For the logit model of the Bliss beetle data ($\hat\beta_0 = -60.72$, $\hat\beta_1 = 34.27$), find the $\mathrm{LD}_{90}$ (mg/L). Why is the choice of model more important in estimating the $\mathrm{LD}_{90}$ than in estimating the $\mathrm{LD}_{50}$?

   **Answer** For $p = 0.9$, $\operatorname{logit} p = \ln 9 = 2.197$, $x_{90} = (2.197 + 60.72)/34.27 = 1.8360$, and $\mathrm{LD}_{90} = 10^{1.836} = 68.5$ mg/L. The three models are tightly constrained by the data at the middle doses, and the curves almost coincide (the figure of Example 14.6.1); in the tails their shapes are determined by the link function (the logistic distribution has heavier tails than the normal, and the complementary log-log is asymmetric), and when extrapolated to 10% or 99% the differences are noticeable. The observed 53/59, 61/62 and 60/60 at the high-dose end are exactly the region in which the cloglog fits well and the logit underestimates, and the $\mathrm{LD}_{99}$ estimated by the logit would be clearly too high.

6. In a 1:1 matched case-control study, there are 40 pairs in which the case is exposed and the control unexposed, 16 pairs of the reverse, 25 pairs in which both are exposed and 119 pairs in which neither is. (a) Estimate the OR and its 95% interval by conditional logistic regression (or an equivalent method); (b) if the matching is ignored and the data are treated as an ordinary 2×2 table of 200 cases and 200 controls, what is the OR? Why do the two differ?

   **Answer** (a) $\widehat{\mathrm{OR}} = b/c = 40/16 = 2.5$, $\operatorname{SE}(\ln\mathrm{OR}) = \sqrt{1/40 + 1/16} = 0.296$, and the interval is $\exp(0.916 \pm 0.580) = (1.40, 4.46)$. (b) Exposed among the cases $25 + 40 = 65$ and among the controls $25 + 16 = 41$; the OR of the ordinary 2×2 table is $(65 \times 159)/(135 \times 41) = 1.87$. When a matching factor (such as age) is related to exposure, the similarity of cases and controls in the matching factor draws the proportion exposed among controls toward that of cases, and the crude OR that ignores the matching is biased toward 1; the matched analysis uses only the discordant pairs and restores the within-set comparison.

7. Explain the role of the offset in Poisson regression: in one region 50 000 person-years were observed over two years with 40 cases of a disease, and in another 20 000 person-years with 24 cases; write the model and find the rate ratio. What would be obtained without the offset?

   **Answer** The model is $\ln\mu_i = \ln T_i + \beta_0 + \beta_1 x_i$, with $x = 1$ for the second region. With two groups the model is saturated: $\mathrm{e}^{\hat\beta_0} = 40/50\,000 = 0.8$ per thousand person-years, $\mathrm{e}^{\hat\beta_0 + \hat\beta_1} = 24/20\,000 = 1.2$ per thousand person-years, and the rate ratio is $\mathrm{e}^{\hat\beta_1} = 1.5$ with $\operatorname{SE}(\hat\beta_1) = \sqrt{1/40 + 1/24} = 0.258$ and 95% interval $(0.90, 2.49)$. Without the offset the comparison would be of counts, and $\mathrm{e}^{\hat\beta_1} = 24/40 = 0.6$: the conclusion is completely reversed, because the second region has less person-time. The offset makes the model compare rates.

8. Why can the residual deviance $D$ not be used to test the goodness of fit of a model for 0/1 data, whereas it can for Bliss's grouped data?

   **Answer** The $\chi^2$ approximation requires the expected count in each "cell" to grow with the sample size. In 0/1 data each observation forms its own group, with $n_i = 1$; as the sample size grows the number of parameters of the saturated model also grows, and the distribution of $D$ does not converge to $\chi^2_{n-k-1}$ (in fact for logistic regression $D = -2\ell(\hat{\boldsymbol\beta})$ depends only on the fitted values and contains almost no information about goodness of fit). The Bliss data have 8 dose groups with about 60 animals each, so the number of groups is fixed while the count in each group grows, and $D \overset{\cdot}{\sim} \chi^2_6$ holds. For individual data one must use grouping methods such as Hosmer–Lemeshow, calibration plots, or likelihood ratio tests aimed at particular departures (nonlinearity, interaction).

9. A clinical team wants to build a logistic model predicting postoperative complications from 300 patients (30 of whom had complications), with 20 candidate variables. Evaluate this plan and propose improvements.

   **Answer** With 30 events and 20 variables the EPV is 1.5, far below 10: the model will overfit severely, the coefficients will be too large and unstable, the calibration in new patients will be poor, and stepwise selection will pick out variables that are significant by chance. Improvements: (1) select, from clinical knowledge and the literature, about 3 of the most important predictors beforehand (EPV ≈ 10), or combine related variables into a score; (2) shrink the coefficients by penalized regression (ridge, lasso) ([7.7.21](/7.7.21)); (3) estimate and correct the optimism by the bootstrap, and report the calibration slope; (4) ideally collect more data or validate in external data. Do not dichotomize continuous variables casually (loss of information), and do not try many models repeatedly on the same data and report only the best.

10. (Analysis question) In a multicenter observational study the investigators use logistic regression to estimate the association of a drug with acute kidney injury, adjusting for age, sex and baseline creatinine, and obtain OR = 1.8 (1.3–2.5). The incidence of acute kidney injury in the study population is about 25%. A reviewer holds that the statement "the drug increases the risk of acute kidney injury by 80%" is inaccurate. Is he right? How should the result be reported?

    **Answer** Yes. When the outcome is not rare (25%) the OR is clearly greater than the RR ([7.7.13](/7.7.13), Section 13.2.3): if the risk in those not taking the drug is 22%, an OR of 1.8 corresponds to a risk of $0.22 \times 1.8/(1 - 0.22 + 0.22 \times 1.8) = 0.337$ in those taking the drug, so that RR is about 1.5, a risk increase of about 50% and not 80%. The adjusted risks should be reported (the model's predicted probabilities for each person with and without the drug are computed and averaged, that is, marginal standardization), giving the adjusted RR and risk difference; or the RR can be estimated directly by binomial regression with a log link or by Poisson regression with robust standard errors. In addition, the causal wording "increases the risk" in an observational study requires a discussion of the possibility of unmeasured confounding (such as severity of illness) (the E-value of [7.7.15](/7.7.15)).
