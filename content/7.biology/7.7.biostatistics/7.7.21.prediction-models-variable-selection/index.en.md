---
title: "Prediction Models: Variable Selection, Regularization and Validation"
description: The difference between explanation and prediction; overfitting, training error and generalization error, the n = 8 omics counterexample and selection bias in cross-validation; stepwise regression on noise data and information criteria; ridge, lasso and elastic net, penalty paths and the choice of λ, sure independence screening; internal validation (cross-validation, bootstrap optimism correction) and external validation, data leakage; discrimination, calibration slope, the Brier score and decision curves; clinical risk scores and polygenic scores; sample size for prediction models and the TRIPOD reporting guideline. Illustrated by the birthwt and airway data.
source_hash: 71a23b42487a
---

The regression models so far were meant to answer "does a factor have an effect, and how large": by how much smoking lowers FEV ([7.7.10](/7.7.10)), by how much maternal smoking raises the odds of low birth weight ([7.7.14](/7.7.14)), whether the adjusted effect is causal ([7.7.15](/7.7.15)). Equally common in the clinic is another kind of question, prediction: what is the risk that this pregnant woman will deliver a low-birth-weight infant? What is the probability that this lung cancer patient is alive one year later? Will this tumor respond to immunotherapy? A model that answers such questions need not have a causal interpretation for every coefficient, but it must give accurate risks for new patients. This chapter treats the building and evaluation of prediction models: why evaluation on the data used to fit a model is always too optimistic (Section 21.2), how to select among many candidate variables (Sections 21.3 and 21.4), how to estimate honestly how the model will perform in new patients (Sections 21.5 and 21.6), and clinical risk scores and reporting guidelines (Sections 21.7 and 21.8). The mathematics of **overfitting**, **cross-validation**, **ridge regression** and the **Lasso** is in [3.3.11](/3.3.11), [3.3.12](/3.3.12), [3.4.10](/3.4.10) and the machine learning course [4.6.2](/4.6.2); here we discuss their use and pitfalls in biomedical prediction. The examples are birthwt of thread 1 (continuing the multiple logistic model of [7.7.14](/7.7.14)) and airway of thread 5 ([7.7.19](/7.7.19), [7.7.20](/7.7.20)).

## 21.1. Explanation and Prediction

The same regression equation can serve two purposes, with different requirements on the model:

| | Explanation (inference) | Prediction |
|---|---|---|
| Question | What is the effect of exposure $X$ on outcome $Y$ | What will $Y$ be given a person's characteristics |
| Quantity of interest | A coefficient $\beta_X$ and its confidence interval | The accuracy of the predicted value $\hat Y$ or risk $\hat p$ |
| Choice of variables | Determined by causal structure: adjust for confounders, not for mediators and colliders ([7.7.15](/7.7.15)) | Determined by predictive ability: any variable available at the time of prediction that improves prediction may be used |
| Bias | Coefficients must be unbiased (or as nearly so as possible) | May be biased as long as the mean squared error is small (shrinkage estimation) |
| Evaluation | Design, control of confounding, sensitivity analysis | Discrimination and calibration in new data (Section 21.6) |
| Ways of failing | Confounding, selection bias | Overfitting, data leakage, population shift |

Take FEV as an example ([7.7.10](/7.7.10)): to estimate the effect of smoking one must adjust for age and height; to predict the FEV of a child, height is almost the only variable needed, and the information on smoking contributes almost nothing to prediction, since smokers are only 10% and the effect is not large. Conversely, the coefficients of a well-predicting model need not have causal meaning: in a cardiovascular risk score, "currently taking antihypertensive medication" raises the predicted risk, which does not show that antihypertensives are harmful (people who take them had high blood pressure to begin with). Confusing the two is a common error: interpreting coefficients in a prediction model, or defending a causal conclusion by "a high $R^2$". The distinction between these two cultures in statistics was made explicit by Breiman (2001); biostatistics has traditionally emphasized inference, and omics and electronic health record data have made prediction equally important (the discussion on the page of the statistics discipline [3](/3)).

## 21.2. Overfitting

### 21.2.1. Training Error and Generalization Error

The error of a model on the data used to fit it (the **training error**, [4.7.1](/4.7.1)) always underestimates its error on new data (the **generalization error**): the parameters were chosen to fit this particular data set, noise included. The more complex the model, the lower the training error, while the generalization error first falls and then rises (figure below). The falling part is the reduction of bias and the rising part the increase of variance (the **bias–variance trade-off**, [3.2.3](/3.2.3)).

**Example 21.2.1 (Simulation)** 30 points are drawn from $y = \sin(2\pi x) + \varepsilon$ (standard deviation of $\varepsilon$ 0.3) and fitted by polynomials of degree 1–12. The training error falls monotonically from 0.22 for degree 1 to 0.067 for degree 12, below the noise variance of 0.09: the degree-12 polynomial is already fitting noise; the error on 10,000 new points is smallest at degree 3 (0.100) and 1.89 at degree 12. The error of 10-fold cross-validation is smallest at degrees 3–4 (0.114), correctly finding a suitable complexity, and its shape resembles the error on new data.

![Training error, cross-validation error and error on new data (simulation, seed 2). The training sample consists of 30 points of $y = \sin(2\pi x)$ plus noise (standard deviation 0.3), with $x$ uniformly distributed on $(0, 1)$, fitted by least squares with polynomials of degree 1–12. A: the data and the fits of degree 1, 3 and 12; the dashed line is the true mean. B: mean squared error on the training data, by 10-fold cross-validation and on 10,000 new points from the same population (log axis); the dotted line is the noise variance 0.09, the smallest error attainable](./plots/overfit-curve.py)

### 21.2.2. Events per Variable

In logistic and Cox regression the amount of information is determined by the number of the rarer outcome. The rule of thumb in [7.7.14](/7.7.14) Section 14.9, at least about 10 events per parameter (EPV), comes precisely from overfitting. In the simulation of panel B below, for a logistic model with 20 candidate variables (15 of them irrelevant) the calibration slope in new data (Definition 21.6.2; 1 means no overfitting) is only 0.25 at EPV about 1.2, 0.51 at EPV about 2.3, 0.85 at EPV about 9 and 0.97 at EPV about 37: even at EPV of 10 the predicted risks are about 15% too extreme. EPV is a rough lower bound, and a better method is to compute the sample size directly from the expected performance of the model (Section 21.8.1).

### 21.2.3. $p \gg n$: The airway Counterexample

**Example 21.2.2 (Can 8 Samples Build a Classifier?)** Divide the 8 airway samples arbitrarily into two groups of 4. There are 35 ways to divide 8 samples into two unordered groups of 4: 1 corresponds to treatment, 3 correspond to pairing the donors two by two, and the other 31 have no biological meaning. For each division, count the genes among the 18,899 whose counts separate the two groups perfectly (the maximum of one group is below the minimum of the other): the true treatment grouping has 3258, the donor groupings 711–1124, and the 31 meaningless groupings also have 100–964 (median 302). Even when the grouping is completely arbitrary, each can find hundreds of "perfect marker genes".

On such data, what do we get from "selecting the 10 genes that best distinguish the two groups, building a nearest-centroid classifier and evaluating by leave-one-out cross-validation"? If the genes are first selected on all 8 samples and leave-one-out cross-validation is done afterward, all 31 meaningless groupings have 0 errors; if in each fold the genes are selected using only the other 7 samples, the average is 5.3 errors in 8 samples, no better than guessing (slightly worse than 4, a known bias of the leave-one-out method in small samples: after one sample is left out, its group becomes the minority). The former practice is **data leakage** ([4.6.2](/4.6.2) [Definition 2.5.1](/4.6.2#def-2.5.1)): the predicted sample took part in feature selection. Ambroise and McLachlan (2002) pointed out in a well-known reanalysis that quite a few early microarray classification studies made this error; the simulation in [7.9.13](/7.9.13) gives the same conclusion ([Example 13.6.1](/7.9.13#ex-13.6.1)).

There are two lessons: (1) when $p \gg n$, perfect separation on the training set provides no evidence at all; (2) cross-validation must include every step of the modeling (normalization, filtering, variable selection, tuning), all done only on the training folds. The airway data with $n = 8$ can be used to test differential expression ([7.7.20](/7.7.20)) but not to build and evaluate the accuracy of a model that "predicts whether dexamethasone treatment was received": the former answers a question for each gene and draws on information across the 20,000 genes; the latter needs enough independent samples to estimate the generalization error.

## 21.3. Variable Selection

### 21.3.1. Problems with Stepwise Regression

**Stepwise regression** ([3.3.11](/3.3.11) [Definition 11.1.2](/3.3.11#def-11.1.2)) automatically adds (**forward selection**) or removes (**backward elimination**) variables using $p$-values or information criteria. It has serious problems for both purposes ([7.7.10](/7.7.10) Section 10.8):

- The same data are used for both selection and testing: the $p$-values of the selected variables are too small, the confidence intervals too narrow and the coefficients too large (they were selected precisely because they happened to be large in this sample, the "winner's curse").
- The selection is unstable: a small change in the data can yield a completely different set of selected variables.
- Noise variables are often selected, and real but weaker variables are often missed.

**Example 21.3.1 (Simulation: Stepwise Selection in Noise)** With $n = 100$, the outcome and 50 candidate variables are all independent standard normal noise, and forward selection at $p < 0.05$ is used. Over 500 replications, 89% select at least one variable, 2.8 variables are selected on average, the median $R^2$ of the final model is 0.14, and the overall $F$ test of the final model has $p < 0.05$ in 89%, against a nominal level of 5%.

### 21.3.2. Information Criteria

The **Akaike information criterion** and the **Bayesian information criterion** ([3.4.11](/3.4.11) [Definition 11.4.2](/3.4.11#def-11.4.2); [3.3.11](/3.3.11) Section 11.2.3) trade off goodness of fit against the number of parameters: $\mathrm{AIC} = -2\ell + 2k$, $\mathrm{BIC} = -2\ell + k\log n$. AIC approximately targets the log-likelihood of leave-one-out cross-validation and suits prediction; BIC selects the true model consistently when it belongs to the candidate set and suits the search for the "true" few variables. Both are more principled than a $p$-value threshold, but when used in a stepwise search they have the same problem of post-selection inference: the standard errors reported on the selected model do not include the uncertainty of the selection step.

For $p$ candidate variables there are $2^p$ subsets; with $p = 27$ this already exceeds $10^8$. Modern practice no longer searches among discrete subsets but turns selection into a continuous shrinkage problem.

## 21.4. Regularization

### 21.4.1. Three Penalties

**Regularization** ([4.7.1](/4.7.1)) adds a penalty term to the negative log-likelihood to pull coefficients toward 0. With the predictors standardized (mean 0, standard deviation 1, so that the penalty is fair to all variables), the penalized estimate for logistic regression is

$$
\hat{\boldsymbol{\beta}}_\lambda = \operatorname*{arg\,min}_{\beta_0, \boldsymbol{\beta}}\Bigl\{-\frac1n\ell(\beta_0, \boldsymbol{\beta}) + \lambda\Bigl[\frac{1 - a}{2}\lVert\boldsymbol{\beta}\rVert_2^2 + a\lVert\boldsymbol{\beta}\rVert_1\Bigr]\Bigr\},
$$
with the intercept unpenalized. For $a = 0$ this is **ridge regression** ([3.3.12](/3.3.12) [Definition 12.1.4](/3.3.12#def-12.1.4)), for $a = 1$ the **Lasso** ([3.3.12](/3.3.12) [Definition 12.1.5](/3.3.12#def-12.1.5)), and for $0 < a < 1$ the **elastic net** ([3.3.12](/3.3.12) [Definition 12.1.6](/3.3.12#def-12.1.6)).

| Penalty | Effect | Suited to |
|---|---|---|
| Ridge ($\ell_2$) | All coefficients shrink proportionally and are not 0; correlated variables share the coefficient | Many variables with weak effects; multicollinearity |
| Lasso ($\ell_1$) | Some coefficients are exactly 0: shrinkage and selection together | Belief that only a few variables matter; need for a parsimonious model |
| Elastic net | Both selection and a "grouping" effect: highly correlated variables enter and leave together | Groups of correlated omics variables such as gene expression and methylation |

The $\ell_1$ penalty produces exact zeros because it is not differentiable at 0: at each step of coordinate descent the update of a coefficient is the soft threshold $\operatorname{sgn}(z)\max(\lvert z\rvert - \lambda, 0)$, and partial scores with absolute value below $\lambda$ are directly truncated to 0. $\lambda$ starts from $\lambda_{\max} = \max_j\lvert\boldsymbol{x}_j^{\mathsf T}(\boldsymbol{y} - \bar y)\rvert/n$, at which all coefficients are 0, and decreases gradually, using the solution at the previous $\lambda$ as the starting value for the next, so that the computation for the whole path is comparable to that of one ordinary fit (the path algorithm of glmnet, Friedman, Hastie and Tibshirani 2010).

### 21.4.2. Choosing λ

$\lambda$ is chosen by cross-validation: compute the $K$-fold cross-validated deviance at each $\lambda$ and take the minimizer $\lambda_{\min}$; or take the largest $\lambda$ whose deviance does not exceed the minimum plus one standard error ($\lambda_{1\mathrm{se}}$, the "one-standard-error rule"), which gives a more parsimonious and more stable model. The cross-validation curve is usually flat near the minimum, and the difference between $\lambda_{\min}$ and $\lambda_{1\mathrm{se}}$ reflects the uncertainty of the selection itself.

**Example 21.4.1 (Lasso for birthwt)** In addition to the variables of [7.7.14](/7.7.14) Example 14.4.1, we add uterine irritability, number of visits, interactions of smoking with 8 other variables, and 10 pure-noise variables, giving 27 candidate variables in all (figure below). $\lambda_{\min}$ selects 17 variables, including 6 noise variables; the main effect of smoking is not selected, its role being "replaced" by interactions of smoking with race, history of preterm labor and so on; $\lambda_{1\mathrm{se}}$ keeps only 2 variables: history of preterm labor and one noise variable. With 189 infants and 59 events there is far too little information to select reliably among 27 variables: the lasso cannot create information out of nothing, it merely lays out "the selection is imprecise" in the form of a coefficient path.

![Lasso logistic regression for low birth weight (189 cases, Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt), 27 candidate variables: maternal age, weight, race (two indicators), smoking, previous preterm labor, hypertension, uterine irritability, number of visits, interactions of smoking with the other 8 variables, and 10 pure-noise standard normal variables (seed 0). Variables are standardized, and the penalized likelihood is solved by coordinate descent (as in glmnet) at 50 values of $\lambda$. A: coefficient paths; colored for clinical main effects, solid gray for interactions of smoking, dashed gray for noise variables; vertical lines at $\lambda_{1\mathrm{se}}$ and $\lambda_{\min}$. B: 10-fold cross-validated deviance per observation (mean and standard error over folds), with the number of nonzero coefficients on the top axis](./plots/lasso-path.py)

**Example 21.4.2 (An Honest Comparison)** Using nested cross-validation (10 outer folds for evaluation, and 10 inner folds in each outer training set to choose $\lambda$, repeated 5 times), we compare the AUC and calibration slope of several models on new data:

| Model | AUC on training data | Cross-validated AUC | Cross-validated calibration slope |
|---|---|---|---|
| The 7 variables of [7.7.14](/7.7.14), maximum likelihood | 0.750 | 0.707 | 0.76 |
| 27 variables, maximum likelihood | 0.845 | 0.690 | 0.35 |
| 27 variables, lasso | 0.817 | 0.664 | 0.78 |
| 27 variables, ridge regression | 0.826 | 0.721 | 1.07 |

(The random splits differ, so the cross-validated AUC of the 7-variable model differs slightly from the 0.695 of Example 21.5.1.) The maximum likelihood model with 27 variables is best on the training data and has very poor calibration in new data (slope 0.35: the predicted risks are too extreme). The shrinkage of ridge regression repairs the calibration and also gives the best discrimination; the lasso is no better than ridge at this sample size because different variables are selected in each fold. The 7 variables chosen beforehand from subject-matter knowledge are about as good as these. In small samples, good prior knowledge is more valuable than automatic selection.

### 21.4.3. Ultrahigh Dimensions and Post-Selection Inference

When $p$ reaches tens of thousands or millions (gene expression, SNPs), a common strategy is first to screen with simple marginal statistics and then to build the model. The sure independence screening (SIS) of Fan and Lv (2008) ranks variables by the absolute value of their marginal correlation with the outcome and keeps the top $d$ (such as $d = n/\log n$), which under suitable conditions keeps all the true variables with probability tending to 1, and then applies the lasso or another method to the retained variables; the marginal correlation can also be replaced by nonlinear measures such as distance correlation and mutual information. Screening is part of the modeling, and in cross-validation it must be redone within each training fold (Example 21.2.2). Bayesian variable selection gives each coefficient a "spike-and-slab" prior (exactly 0 with some probability) and yields the posterior probability that each variable is included, another line of thought.

Whichever method is used, the set of selected variables is random. Repeating the entire selection process with the bootstrap and counting how often each variable is selected (stability selection) is more honest than reporting the result of a single selection; reporting ordinary $p$-values and confidence intervals directly on the selected model is incorrect, and correct "post-selection inference" needs special methods.

## 21.5. Validation

### 21.5.1. Internal Validation

Internal validation estimates the performance of the model in new patients from the same population using the development data themselves, in three ways:

- Split sample: randomly hold out 25%–50% as a test set. It is simple and intuitive, but it wastes data and the result depends on a single random split, so it is not recommended when the sample is not large.
- **Cross-validation** ([3.4.10](/3.4.10) [Definition 10.6.3](/3.4.10#def-10.6.3); for the $K$-fold algorithm see [4.6.2](/4.6.2)): every observation is predicted exactly once, by a model that does not contain it. $K = 10$ is a common compromise; repeating the random fold assignment several times reduces the variance.
- Bootstrap optimism correction (Efron and Gong 1983; the practice recommended by Harrell):

**Definition 21.5.1 (Optimism)** The difference between the estimate of a performance measure $\theta$ (AUC, calibration slope, Brier score and so on) on the development data (the apparent performance) $\theta_{\mathrm{app}}$ and the true performance of the model on new data from the same population is called the **optimism** of the model.

**Algorithm 21.5.1 (Bootstrap Optimism Correction)** Given the development data and the complete modeling steps (including variable selection, transformation and tuning):

1. Build the model on the original data and compute the apparent performance $\theta_{\mathrm{app}}$.
2. For $b = 1, \dots, B$ (usually $B = 200$): draw $n$ observations with replacement to obtain a bootstrap sample, repeat all the modeling steps on it to obtain a model $M_b$; compute the performance $\theta_b^{\mathrm{boot}}$ of $M_b$ on that bootstrap sample and its performance $\theta_b^{\mathrm{orig}}$ on the original data; the estimate of optimism is $o_b = \theta_b^{\mathrm{boot}} - \theta_b^{\mathrm{orig}}$.
3. The corrected performance is $\theta_{\mathrm{app}} - \frac1B\sum_b o_b$.

Each bootstrap requires a refit, so the computation is $B$ model fits. It uses all the data to build the final model, and the variance of its estimate is much smaller than that of a split sample; but if variable selection or any other step is omitted in step 2, the optimism is underestimated.

**Example 21.5.1 (Internal Validation of the birthwt Model)** The model with 7 variables of [7.7.14](/7.7.14) Example 14.4.1 has an AUC of 0.750 on the data used to fit it (panel A below). Ten-fold cross-validation repeated 20 times gives 0.695, and the optimism correction with 200 bootstraps gives 0.715; the cross-validated calibration slope is 0.71 and after bootstrap correction 0.81. In new pregnant women this model will exaggerate the differences in risk by about 20%–30%, with discrimination of about 0.70–0.72. The Hosmer–Lemeshow test in [7.7.14](/7.7.14) ($p = 0.37$) is a test on the same data and cannot detect this overfitting.

### 21.5.2. External Validation

Internal validation answers "how does the model perform in new patients from the same population". When the model is actually used it often faces a different population: another hospital, another country, patients ten years later. The outcome rate, the distribution and measurement of the predictors, and the practice of care all change, and the calibration of the model is especially prone to fail (discrimination is usually more stable). External validation evaluates the model on data that were not used in development and come from a different time or place, a necessary step before a prediction model is put into use. When external validation finds poor calibration, it is often enough to re-estimate the intercept (different outcome rates) or the overall calibration slope without rebuilding the model.

### 21.5.3. Data Leakage

**Data leakage** ([4.6.2](/4.6.2)) is the most insidious error in the evaluation of prediction models: information is used in the evaluation that would not be available at the time of actual prediction. Typical cases in biomedical data:

- Normalization, batch correction, imputation or feature selection on all samples, followed by cross-validation (Example 21.2.2).
- Multiple samples of the same patient (several time points, several lesions, image patches from several slides) appearing in both the training and test sets: the model learns to recognize the patient, not the disease. Split by patient.
- Using variables recorded only after the outcome occurred: diagnosis codes, tests done to confirm the diagnosis, the treatment itself.
- Using future data to predict the past: splitting electronic health records randomly in time rather than training on earlier patients and testing on later patients.

## 21.6. Measures of Predictive Performance

### 21.6.1. Discrimination

**Definition 21.6.1 (Discrimination)** The ability of a model to rank individuals with different outcomes correctly by predicted risk is called **discrimination**. For a binary outcome it is measured by the area under the **ROC curve** (the **area under the curve**, AUC, also called the C statistic): the probability that, of a randomly chosen individual with the outcome and one without, the former has the higher predicted risk ([7.7.3](/7.7.3), [7.7.14](/7.7.14) Section 14.5.3). For survival outcomes Harrell's C index is used, the proportion of comparable pairs of individuals in which the ordering of predicted risk agrees with the ordering of actual survival time.

The AUC depends only on ranking: multiplying all predicted risks by 0.5 leaves the AUC unchanged. It also does not change with the outcome rate, and so cannot tell us whether the predicted risks are correct.

### 21.6.2. Calibration

**Definition 21.6.2 (Calibration Slope and Calibration Intercept)** Let the model give the linear predictor $\widehat{\mathrm{LP}}_i = \operatorname{logit}\hat p_i$. On the evaluation data, fit

$$
\operatorname{logit}\mathbb{P}(Y_i = 1) = a + b\,\widehat{\mathrm{LP}}_i,
$$
where $b$ is called the **calibration slope**; with $b = 1$ fixed (that is, using $\widehat{\mathrm{LP}}_i$ as an offset), the estimated $a$ is called the **calibration intercept** (calibration-in-the-large), which indicates whether the mean predicted risk agrees with the observed outcome rate. With perfect calibration $a = 0$ and $b = 1$.

$b < 1$ means that the predictions are too extreme: the risk of the high-risk is overestimated and that of the low-risk underestimated, a typical sign of overfitting (figure below); $b > 1$ means the predictions are too conservative. On the development data $b$ is identically 1 (a property of maximum likelihood), so calibration can only be evaluated on new data or by cross-validation or the bootstrap. A calibration plot ([7.7.14](/7.7.14) Section 14.5.2) groups by predicted risk and plots the observed proportions, or plots a smoothed calibration curve; it is more informative than the Hosmer–Lemeshow test.

The expected degree of overfitting can be estimated beforehand. Let the likelihood ratio $\chi^2$ statistic of the model be $\chi^2_{\mathrm{model}}$ with $p$ degrees of freedom; the heuristic shrinkage factor of Van Houwelingen and le Cessie (1990) is

$$
\hat s = \frac{\chi^2_{\mathrm{model}} - p}{\chi^2_{\mathrm{model}}}.
$$
For the 7-variable birthwt model, $\chi^2_{\mathrm{model}} = 35.5$ and $\hat s = 0.80$, close to the bootstrap calibration slope of 0.81. Multiplying all coefficients (except the intercept) by $\hat s$ and re-estimating the intercept is a simple post hoc shrinkage; penalized estimation (Section 21.4) accomplishes the shrinkage at the time of modeling.

![An overfitted model is poorly calibrated in new data (simulation, seed 0). True model $\operatorname{logit}\mathbb{P}(Y = 1) = -1.5 + 0.5(x_1 + \cdots + x_5)$, 20 independent standard normal candidate variables of which 15 have no effect, outcome rate about 0.25; all 20 variables are fitted by maximum likelihood. A: one development sample with $n = 200$ (49 events, about 2.5 events per variable): calibration plot with ten groups by predicted risk, on the development data (apparent) and on 20,000 new observations, with the curves being calibration lines from the logistic regression of the outcome on the linear predictor and the calibration slopes in the legend. B: calibration slope in new data against events per variable, the median and interquartile range of 200 development samples for each $n$ from 100 to 3200; the vertical line is EPV = 10](./plots/calibration-slope.py)

### 21.6.3. Overall Accuracy

**Definition 21.6.3 (Brier Score)** For a binary outcome $y_i \in \{0, 1\}$ and predicted probability $\hat p_i$,

$$
\mathrm{BS} = \frac1n\sum_{i=1}^{n}(\hat p_i - y_i)^2
$$
is called the **Brier score**; smaller is better.

The Brier score reflects both discrimination and calibration. Its magnitude depends on the outcome rate: for the "noninformative model" that predicts the outcome rate $\bar y$ for everyone, $\mathrm{BS} = \bar y(1 - \bar y)$; the proportional improvement relative to it (the scaled Brier score) is often reported. The apparent Brier score of the birthwt model is 0.176 and that of the noninformative model is $0.312 \times 0.688 = 0.215$; after bootstrap correction it is about 0.194, and the improvement falls from 18% to about 10%.

### 21.6.4. Clinical Usefulness: Decision Curves

Neither discrimination nor calibration directly answers "is it better to use this model to make decisions than not to?" If an intervention (such as intensified prenatal care for high-risk pregnant women) is delivered only when the risk exceeds a threshold $p_t$, the threshold itself expresses a trade-off of gains and losses: at $p_t$ the expected gains of intervening and not intervening are equal, that is, the ratio of the cost of a false positive to the benefit of a true positive is $p_t/(1 - p_t)$.

**Definition 21.6.4 (Net Benefit and Decision Curve Analysis)** At a threshold probability $p_t$, intervening on those with predicted risk $\hat p \ge p_t$ has **net benefit**

$$
\mathrm{NB}(p_t) = \frac{\mathrm{TP}}{n} - \frac{\mathrm{FP}}{n}\cdot\frac{p_t}{1 - p_t},
$$
where TP and FP are the numbers of true and false positives. Plotting the net benefit of the model as a function of $p_t$ and comparing it with "intervene on everyone" ($\mathrm{NB} = \bar y - (1 - \bar y)p_t/(1 - p_t)$) and "intervene on no one" ($\mathrm{NB} = 0$) is called **decision curve analysis** (Vickers and Elkin 2006).

The unit of net benefit is "true positives per person": $\mathrm{NB} = 0.08$ is equivalent to identifying 8 more correctly per 100 people without adding false positives. The model is useful only over the range of thresholds in which its net benefit exceeds that of the two default strategies.

**Example 21.6.1 (Decision Curve for birthwt)** Computed with cross-validated predicted risks (panel B below). For thresholds below about 0.15 the model is about as good as "intensify care for all pregnant women" (0.233 versus 0.236 at threshold 0.1): when the cost of the intervention is small, the model does not help. At threshold 0.3 the net benefit of the model is 0.082 and "intervene on all" has only 0.017, with the model flagging 77 of the 189; at threshold 0.4 it is 0.067 versus $-0.146$. For thresholds above about 0.6 almost no one is flagged by the model and the net benefit approaches 0.

![Internal validation and decision curve of the birthwt logistic model of [7.7.14](/7.7.14) (maternal age, weight, race, smoking, previous preterm labor, hypertension; 189 cases, Baystate Medical Center 1986; Hosmer and Lemeshow; R MASS::birthwt). A: AUC and calibration slope estimated on the fitted data (apparent), by 10-fold cross-validation (average over 20 random splits) and by bootstrap optimism correction (200 resamples); seed 0. B: decision curve: net benefit of acting at each threshold probability according to the cross-validated predicted risk, compared with acting on everyone and on no one](./plots/validation-dca.py)

## 21.7. Clinical Risk Scores

### 21.7.1. From Model to Score

Prediction models used in the clinic are often simplified into scores: the coefficient of each variable is converted into integer points (taking the coefficient for a one-unit increment of some reference variable as 1 point and the other coefficients in proportion), and the total score corresponds to a risk table. The cardiovascular risk score from the Framingham Heart Study (a community cohort in Massachusetts, USA, begun in 1948) is the earliest and most widely used example: age, sex, total cholesterol and HDL cholesterol, systolic blood pressure and whether on antihypertensive treatment, smoking and diabetes are used to predict the 10-year risk of cardiovascular events (the general version of D'Agostino et al. 2008), and it was built by Cox regression. This example also illustrates the issue of Section 21.5.2: in populations with lower baseline risk, the original Framingham equation overestimated the risk of coronary heart disease, and it could be used only after recalibrating the intercept (with local incidence rates and mean risk factor levels). Countries have therefore built their own equations (SCORE2 in Europe, China-PAR in China) or recalibrated the Framingham equation locally.

Scores divide continuous variables into bands and round coefficients, losing some information; now that computers and electronic health records are widespread, computing risk directly from the equation is no longer difficult.

### 21.7.2. Polygenic Scores

A **polygenic score** ([7.4.25](/7.4.25) Section 25.6) is a risk score summed with weights over the whole genome, the weights coming from GWAS effect estimates after shrinkage (selecting significant SNPs and "pruning" linkage, or shrinking all SNPs simultaneously by Bayesian methods): an application of the regularization idea of this chapter in a million dimensions. Its problems in prediction are also the problems of this chapter: outside the ancestry population in which it was developed, the predictive ability of the score falls markedly (the structure of allele frequencies and linkage disequilibrium differs), a typical failure of external validation; its discrimination alone is often limited, and its clinical value must be judged by the improvement and net benefit after adding it to traditional risk factors, not by how significant its association with the disease is.

## 21.8. Sample Size, Reporting and Reproducibility

### 21.8.1. Sample Size for Prediction Models

[7.7.14](/7.7.14) Section 14.9 noted that the EPV rule is only a rough lower bound. Riley et al. (2019, 2020) compute the required sample size directly from the requirement that "the developed model should have only a small amount of overfitting". The criterion that most often decides is:

**Formula 21.8.1 (Sample Size by Expected Shrinkage)** Suppose the model has $p$ parameters (excluding the intercept), the anticipated Cox–Snell $R^2$ is $R^2_{\mathrm{CS}}$, and the expected shrinkage factor (calibration slope) is required to be no less than $S$ (usually 0.9). The required sample size is

$$
n = \frac{p}{(S - 1)\ln\bigl(1 - R^2_{\mathrm{CS}}/S\bigr)}.
$$

The other criteria require a small difference between the apparent and corrected $R^2$ (such as no more than 0.05) and a sufficiently precise estimate of the outcome rate, and the largest sample size required by any criterion is taken. $R^2_{\mathrm{CS}}$ can be converted from the $\chi^2_{\mathrm{model}}$ of a published similar model: $R^2_{\mathrm{CS}} = 1 - \exp(-\chi^2_{\mathrm{model}}/n)$.

**Example 21.8.1** The 7-parameter birthwt model has $R^2_{\mathrm{CS}} = 0.171$. By Formula 21.8.1, for $S = 0.9$ we need $n = 7/[(-0.1)\ln(1 - 0.171/0.9)] = 7/0.0211 = 332$ pregnant women, with about 104 events (EPV about 15); the actual 189 can guarantee a shrinkage factor of only about 0.80, consistent with the bootstrap calibration slope of Example 21.5.1.

### 21.8.2. Reporting Guidelines

TRIPOD (Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis, 2015; extended in 2024 to TRIPOD+AI to cover machine learning methods) lists the items that a prediction model study should report: source and time span of the data, definitions and timing of measurement of the outcome and predictors, handling of missing data, the basis of the sample size, all steps of the modeling (including variable selection and tuning), the method of internal validation, discrimination and calibration (including the calibration plot), and the complete model equation (so that others can compute risks and do external validation). The corresponding guideline for diagnostic accuracy studies is STARD ([7.7.3](/7.7.3)).

### 21.8.3. Reproducibility

"Torture the data long enough and they will confess to anything": this oft-quoted saying describes exactly the pitfalls of this chapter: by trying enough combinations of variables, models, thresholds and subgroups, one can always obtain good-looking results on the training data. The countermeasures are those that recur in this course: write the analysis plan beforehand ([7.7.18](/7.7.18) Section 18.9) and distinguish exploratory from confirmatory analyses; evaluation of prediction must include every step of the modeling; make the data and code public so that others can reproduce and externally validate.

## 21.9. Computing with Python

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.metrics import brier_score_loss, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

bw = pd.read_csv("birthwt.csv")
bw["ptd"] = (bw.ptl > 0).astype(int)
f = "low ~ age + lwt + C(race) + smoke + ptd + ht"
m = smf.glm(f, bw, family=sm.families.Binomial()).fit()
p_app = m.predict(bw)
print(roc_auc_score(bw.low, p_app), brier_score_loss(bw.low, p_app))      # 0.750, 0.176

# bootstrap optimism correction (Algorithm 21.5.1)
rng = np.random.default_rng(0)
opt = []
for _ in range(200):
    d = bw.iloc[rng.integers(0, len(bw), len(bw))]
    mb = smf.glm(f, d, family=sm.families.Binomial()).fit()
    opt.append(roc_auc_score(d.low, mb.predict(d)) - roc_auc_score(bw.low, mb.predict(bw)))
print(roc_auc_score(bw.low, p_app) - np.mean(opt))                       # about 0.71

# calibration slope of cross-validated predictions (Definition 21.6.2)
X = pd.get_dummies(bw[["age", "lwt", "race", "smoke", "ptd", "ht"]].astype({"race": str}), drop_first=True)
cv = StratifiedKFold(10, shuffle=True, random_state=0)
p_cv = cross_val_predict(make_pipeline(StandardScaler(), LogisticRegression(C=1e8)), X, bw.low, cv=cv,
                         method="predict_proba")[:, 1]
lp = np.log(p_cv / (1 - p_cv))
print(sm.GLM(bw.low, sm.add_constant(lp), family=sm.families.Binomial()).fit().params)   # slope about 0.7

# lasso / ridge / elastic net with lambda chosen inside each training fold (nested CV, Example 21.4.2)
lasso = make_pipeline(StandardScaler(),
                      LogisticRegressionCV(Cs=30, cv=10, l1_ratios=[1.0], solver="saga", scoring="neg_log_loss"))
p_nested = cross_val_predict(lasso, X_candidates, bw.low, cv=cv, method="predict_proba")[:, 1]

# net benefit at a threshold (Definition 21.6.4)
def net_benefit(y, p, t):
    return np.mean((p >= t) & (y == 1)) - np.mean((p >= t) & (y == 0)) * t / (1 - t)

# Riley sample size (Formula 21.8.1)
r2cs = 1 - np.exp(2 * (m.llnull - m.llf) / len(bw))                     # 0.171
print(7 / ((0.9 - 1) * np.log(1 - r2cs / 0.9)))                          # 332
```

## Summary

- Explanation requires unbiased coefficients and control of confounding; prediction requires accurate risks for new individuals; their selection of variables, evaluation and ways of failing differ (Section 21.1).
- Training error underestimates generalization error; as complexity increases the generalization error first falls and then rises (Example 21.2.1). The smaller the EPV, the smaller the calibration slope: 0.51 at EPV about 2.3 and 0.85 at about 9 (Section 21.2.2). When $p \gg n$, even arbitrary groupings have hundreds of perfectly separating genes, and selecting genes on all samples and then cross-validating gives 0 errors (Example 21.2.2): cross-validation must include every step.
- Stepwise selection selects variables in pure noise in 89% of cases, and the $F$ test of the final model is "significant" in 89% (Example 21.3.1); AIC favors prediction and BIC the true model, and both have the problem of post-selection inference.
- Penalized likelihood: ridge (shrinkage, no selection), lasso (soft threshold, selection), elastic net (grouping); $\lambda$ is chosen by cross-validation, $\lambda_{\min}$ or $\lambda_{1\mathrm{se}}$. birthwt with 27 candidates: the lasso selects noise variables (Example 21.4.1); in nested cross-validation ridge regression has AUC 0.721 and calibration slope 1.07, while the 27-variable maximum likelihood model has calibration slope 0.35 (Example 21.4.2). In ultrahigh dimensions screen first with SIS; look at the stability of the selection.
- Internal validation: cross-validation or bootstrap optimism correction (Definition 21.5.1, Algorithm 21.5.1); birthwt: AUC 0.750 → 0.695 (CV) / 0.715 (bootstrap), calibration slope 0.71 / 0.81 (Example 21.5.1). External validation tests transportability, with calibration the most likely to fail; common forms of data leakage (Section 21.5.3).
- Performance: discrimination (Definition 21.6.1, AUC, C index), calibration slope and intercept (Definition 21.6.2; the heuristic shrinkage $(\chi^2 - p)/\chi^2$), the Brier score (Definition 21.6.3), net benefit and the decision curve (Definition 21.6.4; birthwt at threshold 0.3: 0.082 versus 0.017, Example 21.6.1).
- Risk scores must be recalibrated to the population (Framingham); polygenic scores are shrinkage models in a million dimensions and transfer poorly across ancestries (Section 21.7).
- Sample size is computed from the expected shrinkage (Formula 21.8.1; birthwt needs 332, Example 21.8.1); report the complete model equation and validation according to TRIPOD.

## Questions

1. The predicted risks of 4 pregnant women are 0.9, 0.2, 0.6, 0.1, and the actual outcomes are 1, 0, 0, 0. Compute the Brier score and compare it with the noninformative model that predicts the outcome rate for everyone.

   **Answer** $\mathrm{BS} = [(0.9 - 1)^2 + 0.2^2 + 0.6^2 + 0.1^2]/4 = (0.01 + 0.04 + 0.36 + 0.01)/4 = 0.105$. The outcome rate is 0.25, and the noninformative model gives $[(0.25 - 1)^2 + 3 \times 0.25^2]/4 = (0.5625 + 0.1875)/4 = 0.1875 = 0.25 \times 0.75$. The model lowers the Brier score by $1 - 0.105/0.1875 = 44\%$; its prediction for the third woman (0.6 without the outcome) is the main source of error.

2. Of 1000 patients, 100 have the outcome. At threshold 0.2 the model flags 280 people, of whom 80 have the outcome. Compute the net benefit of the model, of "intervene on all" and of "intervene on none", and explain their meaning.

   **Answer** $p_t/(1 - p_t) = 0.25$. Model: $80/1000 - 200/1000 \times 0.25 = 0.08 - 0.05 = 0.03$. Intervene on all: $0.1 - 0.9 \times 0.25 = -0.125$. Intervene on none: 0. Under the trade-off that the cost of a false positive is 1/4 of the benefit of a true positive, using the model is equivalent to a net gain of 30 true positives per 1000 people with no extra false positives; intervening on all is harmful.

3. A logistic prediction model with 10 parameters is to be built, and the Cox–Snell $R^2$ of similar models is about 0.10. The expected shrinkage factor is required to be at least 0.9; how many people are needed by Formula 21.8.1? If the outcome rate is 20%, what EPV does this correspond to?

   **Answer** $n = 10/[(0.9 - 1)\ln(1 - 0.10/0.9)] = 10/[(-0.1)(-0.1178)] = 10/0.01178 = 849$. The number of events is $0.2 \times 849 = 170$, and the EPV is 17. When $R^2$ is small (weak predictive information) the required EPV is higher than the rule of thumb of 10.

4. A model with 12 parameters has a likelihood ratio $\chi^2$ of 48. Estimate its calibration slope in new data; if its AUC on the development data is 0.78 and the average optimism estimated by the bootstrap is 0.05, what is the corrected AUC?

   **Answer** The heuristic shrinkage factor is $(48 - 12)/48 = 0.75$: the predicted risks are exaggerated by about 1/3 on the log-odds scale, and should be shrunk or penalized estimation used instead. The corrected AUC is $0.78 - 0.05 = 0.73$.

5. In Example 21.4.1 the lasso selected 6 pure-noise variables at $\lambda_{\min}$. Why? How should this affect the use of the lasso's selection?

   **Answer** With 59 events among 189 people, each noise variable has some chance correlation with the outcome in the sample; among 10 noise variables there are always some whose chance correlation is no smaller than a real but weak effect (such as smoking), and the cross-validated deviance curve is flat near the minimum and cannot tell them apart. The lasso can recover the true set of variables reliably only when the signal is strong enough and the correlation among variables is not too strong (the irrepresentable condition). The selection of the lasso should therefore be regarded as being for prediction, not as a conclusion about "which factors really matter"; the stability of the selection should be reported (the frequency with which each variable is selected in bootstrap samples), and causal or mechanistic questions return to the design and adjustment of [7.7.15](/7.7.15).

6. A study uses the tumor transcriptomes (20,000 genes) of 120 patients to predict the response to immunotherapy: it first selects the 50 genes with the largest differences by $t$ tests on all patients and then evaluates an SVM classifier by 5-fold cross-validation, reporting an AUC of 0.92. Point out the problem and give the correct approach.

   **Answer** Feature selection used the outcomes of all patients, and the predicted patients took part in gene selection: this is data leakage (Example 21.2.2). Even when the outcome has nothing to do with gene expression, this procedure can give a very high AUC. The correct approach is to put the gene selection (and normalization, batch correction and tuning) inside the training set of each fold, evaluating by nested cross-validation; better still, validate externally at another center or in another batch of patients. One should also check whether several samples of the same patient fall into different folds and whether batch is confounded with response ([7.7.19](/7.7.19) Section 19.7).

7. A cardiovascular risk model built in a US cohort is applied to a Chinese population and has an AUC of 0.76 (close to the original study), but the predicted 10-year risk averages 12% whereas 6% is observed. Can the model be used? How should it be handled?

   **Answer** Discrimination is maintained, which shows that the ranking of risk remains valid; the calibration intercept is poor, with predictions systematically too high by about a factor of two, and deciding on treatment by the original threshold would cause a great deal of overtreatment. The model need not be rebuilt: re-estimate the intercept (the calibration intercept) with the local incidence, if necessary also estimate the overall calibration slope, and then validate the calibration plot and decision curve in independent local data. This is exactly how the Framingham equation was handled in other populations (Section 21.7.1).

8. Why is the calibration slope on the development data always 1? Explain from this why a "nonsignificant" Hosmer–Lemeshow test on the development data does not show that the model is well calibrated in new patients.

   **Answer** The maximum likelihood estimate satisfies the score equations $\sum_i(y_i - \hat p_i)\boldsymbol{x}_i = \boldsymbol{0}$; when logistic regression is refitted with $\widehat{\mathrm{LP}}$ as the only covariate, $(a, b) = (0, 1)$ satisfies its score equations (both $\sum(y_i - \hat p_i) = 0$ and $\sum(y_i - \hat p_i)\widehat{\mathrm{LP}}_i = 0$ follow as linear combinations of the original score equations) and is therefore the solution. The coefficients of the model were chosen to fit this data set, so on this data set it is necessarily "well calibrated"; the inflation of coefficients caused by overfitting shows up as a slope below 1 only in new data. The Hosmer–Lemeshow test on the same data tests whether the functional form of the model is seriously inappropriate, not overfitting.

9. Compare the performance of ridge regression and the lasso in the following two situations, and explain why: (a) 20 highly correlated methylation sites jointly reflect one biological process, each with a small effect; (b) among 500 candidate genes only 3 have strong effects and the rest are irrelevant.

   **Answer** (a) Ridge regression (or the elastic net) is better: with many small effects and highly correlated variables, ridge regression spreads the coefficient evenly across correlated variables, stably and with good prediction; the lasso tends to pick only one arbitrarily from a group of correlated variables, so that the selection is unstable and prediction suffers from truncating the small effects. (b) The lasso is better: the true model is sparse, and the $\ell_1$ penalty can set the coefficients of the 497 irrelevant variables to 0, giving a parsimonious model with small variance; ridge regression retains small coefficients for all variables and noise accumulates. The elastic net compromises between the two situations, and $a$ can also be chosen by cross-validation.

10. (Analysis design) A hospital wants to use electronic health record data (about 200 variables such as age at admission, vital signs, laboratory tests and comorbidity codes; about 30,000 admissions in 5 years, of which 1500 died within 30 days) to build a model for the 30-day mortality risk at admission. Write a plan for modeling and validation and point out the possible sources of data leakage.

    **Answer** (1) Definition: the time of prediction is a few hours after admission, only variables recorded before that time are used, and the outcome is all-cause death within 30 days. (2) Sample size: with 1500 events and 200 candidate variables (EPV 7.5), check by Formula 21.8.1 whether this is sufficient, and if necessary first reduce the variables by subject-matter knowledge or use penalized regression. (3) Splitting: by time, developing on the first 4 years and using the last year for temporal external validation; multiple admissions of the same patient go into the same part. (4) Modeling: impute missing values by multiple imputation ([7.7.17](/7.7.17)), with the imputation model fitted only on the development data; keep nonlinearity of continuous variables with splines; use elastic net logistic regression, with $\lambda$ and $a$ chosen by cross-validation within the development data; compare with a simple model containing only a few clinical variables. (5) Validation: bootstrap optimism correction within the development data, and report AUC, calibration intercept and slope, the calibration plot, the Brier score and the decision curve on the last year's data. (6) Reporting: report the complete equation according to TRIPOD. Sources of leakage: diagnosis codes and discharge summaries recorded only after admission; outcome-related events such as "transfer to the ICU" and "start of palliative care"; random rather than temporal splitting; imputation, standardization or variable screening on all the data; multiple admissions of the same patient split between the training and test sets.
