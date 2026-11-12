---
title: Regression Methods for Completely Randomized Experiments
description: Linear regression as a tool for estimating average treatment effects in completely randomized experiments. Without covariates the OLS estimator is the difference in means, its causal meaning comes from randomization, and robust standard errors reproduce Neyman's variance estimator; with covariates the population coefficient equals the super-population average effect even when the model is wrong, the estimator is asymptotically normal and more precise when covariates predict the outcome; interactions, tests of effect heterogeneity, and the LRC-CPPT cholesterol data.
---

Neyman's analysis of [3.9.4](/3.9.4) uses only the treatment indicator and the outcome. Most experiments also record pre-treatment variables, and when these predict the outcome they carry information that the difference in means throws away. Linear regression is the most common way of using them: regress the observed outcome on the treatment indicator and the covariates, and read off the coefficient of the treatment. Regression by itself only describes associations, and it can be run on any data set. In a **completely randomized experiment**, however, the randomization gives the regression coefficient a causal meaning, and it does so without requiring the linear model to be true. This chapter makes that statement precise. Throughout, the units are a random sample from a **super-population**, so that the estimand is $\tau_{\mathrm{sp}}$ and expectations $\mathbb{E}_{\mathrm{sp}}$ and variances $\operatorname{Var}_{\mathrm{sp}}$ are taken over both the sampling of the units and the assignment ([3.9.4](/3.9.4)). The regression results are large-sample results, in contrast to the exact finite-sample results of Fisher and Neyman. The matrix form of least squares and the robust variance estimator are taken from [3.3.7](/3.3.7) and [3.3.12](/3.3.12); the stratified designs of [3.9.7](/3.9.7) and the observational studies of [3.9.10](/3.9.10) reuse the same regression arguments.

## 5.1. Setting

### 5.1.1. Can a Covariate Help?

By Theorem 4.3.1, the sampling variance of the **difference-in-means estimator** in a CRE is

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{S_{\mathrm{tc}}^2}{N},
$$
where $S_{\mathrm{c}}^2$ and $S_{\mathrm{t}}^2$ are the finite-population variances of $Y_i(0)$ and $Y_i(1)$, and $S_{\mathrm{tc}}^2$ is that of the unit-level effects. The leading terms are the variances of the potential outcomes. A covariate can reduce them only by explaining part of the variation in the outcomes. Two extreme cases show what is possible:

- the covariate is independent of the potential outcomes: it carries no information about them, and adjusting for it can only add noise;
- the covariate is strongly correlated with the potential outcomes, and therefore with $Y_i^{\mathrm{obs}}$: comparing treated and control units with similar covariate values removes much of the outcome variation, and the effect is estimated more precisely.

The four approaches to a CRE answer different questions:

| Approach | Question | Chapter |
|---|---|---|
| Fisher's exact p-values | Is there any non-zero unit-level effect? | [3.9.3](/3.9.3) |
| Neyman's repeated sampling | How can the average effect be estimated, and how precisely? | [3.9.4](/3.9.4) |
| Regression | How can covariates improve the estimate of the average effect? | this chapter |
| Model-based inference | How do parametric models of the potential outcomes help? | [3.9.6](/3.9.6) |

### 5.1.2. The Super-Population and Notation

The sample of $N$ units is drawn at random from an infinite super-population, and then $N_{\mathrm{t}}$ of them are assigned to treatment by a CRE. The potential outcomes of the sampled units are therefore random, and the properties of an estimator are evaluated by repeated sampling from the population followed by repeated assignment. The covariates $X_i$ form a $1 \times K$ row vector. The population quantities used below are

$$
\begin{aligned}
&\tau_{\mathrm{sp}} = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1) - Y_i(0)\bigr], \qquad
\mu_{\mathrm{c}}(x) = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(0) \mid X_i = x\bigr], \qquad
\mu_{\mathrm{t}}(x) = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1) \mid X_i = x\bigr],\\
&\sigma_{\mathrm{c}}^2(x) = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(0) \mid X_i = x\bigr), \qquad
\sigma_{\mathrm{t}}^2(x) = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(1) \mid X_i = x\bigr), \qquad
\tau(x) = \mu_{\mathrm{t}}(x) - \mu_{\mathrm{c}}(x),\\
&\mu_{\mathrm{c}} = \mathbb{E}_{\mathrm{sp}}[\mu_{\mathrm{c}}(X_i)], \qquad
\sigma_{\mathrm{c}}^2 = \mathbb{E}_{\mathrm{sp}}\bigl[\sigma_{\mathrm{c}}^2(X_i)\bigr] + \operatorname{Var}_{\mathrm{sp}}\bigl(\mu_{\mathrm{c}}(X_i)\bigr) \quad (\text{and likewise for } \mathrm{t}),\\
&\mu_X = \mathbb{E}_{\mathrm{sp}}[X_i], \qquad
\Omega_X = \operatorname{Var}_{\mathrm{sp}}(X_i) = \mathbb{E}_{\mathrm{sp}}\bigl[(X_i - \mu_X)^{\mathsf T}(X_i - \mu_X)\bigr].
\end{aligned}
$$
The decomposition of $\sigma_{\mathrm{c}}^2$ is the law of total variance ([3.1.9](/3.1.9)); its second term is the part of the outcome variance that a covariate can explain. In the large-sample statements, $p = \lim_{N \to \infty} N_{\mathrm{t}}/N \in (0, 1)$ is the limiting proportion of treated units. In the super-population a CRE makes the treatment indicator of a randomly chosen unit independent of everything else about it: $W_i \perp \bigl(Y_i(0), Y_i(1), X_i\bigr)$, with $\mathbb{P}(W_i = 1) = N_{\mathrm{t}}/N$. This independence is the only feature of the design used below.

### 5.1.3. The LRC-CPPT Cholesterol Data

The Lipid Research Clinics Coronary Primary Prevention Trial (LRC-CPPT) was a randomized, double-blind trial of the cholesterol-lowering drug cholestyramine in men with high cholesterol. The subsample analyzed here, studied by Efron and Feldman (1991), contains $N = 337$ men, $N_{\mathrm{c}} = 172$ assigned to a placebo and $N_{\mathrm{t}} = 165$ to the drug. A placebo makes the two groups differ only in the drug itself: without it, the knowledge of being treated could change diet, exercise and other behavior that also affects cholesterol, and the comparison would measure the effect of the whole package rather than of the drug.

| Variable | Timing | Control mean (s.d.) | Treated mean (s.d.) |
|---|---|---|---|
| `chol1`: cholesterol, first pre-treatment measurement | pre | 297.1 (23.1) | 297.0 (20.4) |
| `chol2`: cholesterol, second pre-treatment measurement | pre | 289.2 (24.1) | 287.4 (21.4) |
| `cholp`: combined pre-treatment level | pre | 291.2 (23.2) | 289.9 (20.4) |
| `cholf`: cholesterol after treatment (outcome) | post | 282.7 (24.9) | 256.5 (26.2) |
| `chold` $=$ `cholf` $-$ `cholp` | post | $-8.5$ (10.8) | $-33.4$ (21.3) |
| `comp`: percentage of the prescribed dose taken | post | 74.5 (21.0) | 59.9 (24.4) |

The outcome is $Y = $ `cholf`, the treatment $W$ is assignment to the drug, and the pre-treatment measurements are covariates $X$. They are balanced across the groups, as randomization implies, and strongly predictive of the outcome: in the control group the standard deviation of the change `chold` is less than half that of `cholf`. The compliance variable `comp` is measured after assignment and differs between the groups; Section 5.3.8 explains why it must not be used as a covariate.

## 5.2. Regression without Covariates

### 5.2.1. The Estimator

Consider the regression model

$$
Y_i^{\mathrm{obs}} = \alpha + \tau W_i + \varepsilon_i,
$$
and the least squares estimator $(\hat\alpha^{\mathrm{ols}}, \hat\tau^{\mathrm{ols}}) = \arg\min_{\alpha, \tau}\sum_{i=1}^{N}\bigl(Y_i^{\mathrm{obs}} - \alpha - \tau W_i\bigr)^2$.

**Theorem 5.2.1** The least squares estimators are

$$
\hat\tau^{\mathrm{ols}} = \frac{\sum_{i=1}^{N}(W_i - \bar W)(Y_i^{\mathrm{obs}} - \bar Y^{\mathrm{obs}})}{\sum_{i=1}^{N}(W_i - \bar W)^2} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = \hat\tau^{\mathrm{dif}}, \qquad
\hat\alpha^{\mathrm{ols}} = \bar Y_{\mathrm{c}}^{\mathrm{obs}},
$$
where $\bar W = N_{\mathrm{t}}/N$.

**Proof** The first equality is the slope of a simple linear regression. Because $W_i^2 = W_i$, the denominator is $\sum_i W_i - N\bar W^2 = N_{\mathrm{t}} - N_{\mathrm{t}}^2/N = N_{\mathrm{t}}N_{\mathrm{c}}/N$. The numerator is $\sum_i W_iY_i^{\mathrm{obs}} - N\bar W\bar Y^{\mathrm{obs}} = N_{\mathrm{t}}\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \frac{N_{\mathrm{t}}}{N}\bigl(N_{\mathrm{t}}\bar Y_{\mathrm{t}}^{\mathrm{obs}} + N_{\mathrm{c}}\bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)$. Dividing gives $\hat\tau^{\mathrm{ols}} = \hat\tau^{\mathrm{dif}}$, and $\hat\alpha^{\mathrm{ols}} = \bar Y^{\mathrm{obs}} - \hat\tau^{\mathrm{ols}}\bar W = \bar Y_{\mathrm{c}}^{\mathrm{obs}}$. $\square$

The regression with a single binary regressor reproduces Neyman's estimator exactly, so in a CRE $\hat\tau^{\mathrm{ols}}$ is unbiased for $\tau_{\mathrm{fs}}$ over the assignment and for $\tau_{\mathrm{sp}}$ over sampling and assignment (Theorems 4.2.1 and 4.6.1).

### 5.2.2. Causal Interpretation

The coefficients and the error term of the regression can be defined directly in terms of the potential outcomes. Let $\mu_{\mathrm{c}} = \mathbb{E}_{\mathrm{sp}}[Y_i(0)]$ and $\mu_{\mathrm{t}} = \mathbb{E}_{\mathrm{sp}}[Y_i(1)]$, and set

$$
\alpha = \mu_{\mathrm{c}}, \qquad \tau = \mu_{\mathrm{t}} - \mu_{\mathrm{c}} = \tau_{\mathrm{sp}}, \qquad
\varepsilon_i = \begin{cases} Y_i(0) - \mu_{\mathrm{c}}, & W_i = 0,\\ Y_i(1) - \mu_{\mathrm{t}}, & W_i = 1. \end{cases}
$$
Then $Y_i^{\mathrm{obs}} = \alpha + \tau W_i + \varepsilon_i$ holds by construction, for every unit: it is an identity, not a model. The substance lies in the properties of the error. Since $W_i$ is independent of $(Y_i(0), Y_i(1))$ in a CRE,

$$
\mathbb{E}_{\mathrm{sp}}[\varepsilon_i \mid W_i = 1] = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1) - \mu_{\mathrm{t}} \bigm| W_i = 1\bigr] = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1)\bigr] - \mu_{\mathrm{t}} = 0,
$$
and likewise $\mathbb{E}_{\mathrm{sp}}[\varepsilon_i \mid W_i = 0] = 0$. The conditional variance is

$$
\operatorname{Var}_{\mathrm{sp}}(\varepsilon_i \mid W_i) = \sigma_{\mathrm{t}}^2 W_i + \sigma_{\mathrm{c}}^2(1 - W_i).
$$
The usual regression condition $\mathbb{E}[\varepsilon_i \mid W_i] = 0$, which in an observational analysis is an assumption that can fail, is here a consequence of the randomization. This is the step from an association statement to a causal statement: the population regression coefficient of $Y^{\mathrm{obs}}$ on $W$ is $\mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 1] - \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 0]$ in any data set, and only because of the CRE does it equal $\mathbb{E}_{\mathrm{sp}}[Y_i(1)] - \mathbb{E}_{\mathrm{sp}}[Y_i(0)] = \tau_{\mathrm{sp}}$. The units are i.i.d. draws, so the standard regularity conditions of the linear model hold, and all the theory for inference on $(\alpha, \tau)$ applies, with the one caveat that the error variance may differ between the two groups.

### 5.2.3. Inference

Stack the units with the $N_{\mathrm{c}}$ controls first. In the matrix notation of [3.3.7](/3.3.7), $\boldsymbol{Y}^{\mathrm{obs}} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ with $\boldsymbol{\beta} = (\alpha, \tau)^{\mathsf T}$ and

$$
X = \begin{bmatrix} \boldsymbol{1}_{N_{\mathrm{c}}} & \boldsymbol{0}_{N_{\mathrm{c}}} \\ \boldsymbol{1}_{N_{\mathrm{t}}} & \boldsymbol{1}_{N_{\mathrm{t}}} \end{bmatrix}, \qquad
\mathbb{E}_{\mathrm{sp}}[\boldsymbol{\varepsilon} \mid X] = \boldsymbol{0}, \qquad
\operatorname{Var}_{\mathrm{sp}}(\boldsymbol{\varepsilon} \mid X) = \Sigma = \operatorname{diag}\bigl(\sigma_{\mathrm{c}}^2\boldsymbol{1}_{N_{\mathrm{c}}}^{\mathsf T}, \sigma_{\mathrm{t}}^2\boldsymbol{1}_{N_{\mathrm{t}}}^{\mathsf T}\bigr).
$$
The estimator is $\hat{\boldsymbol{\beta}} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}^{\mathrm{obs}} = \boldsymbol{\beta} + H\boldsymbol{\varepsilon}$ with $H = (X^{\mathsf T}X)^{-1}X^{\mathsf T}$, whose two rows are $\bigl(\boldsymbol{1}_{N_{\mathrm{c}}}^{\mathsf T}/N_{\mathrm{c}},\ \boldsymbol{0}^{\mathsf T}\bigr)$ and $\bigl(-\boldsymbol{1}_{N_{\mathrm{c}}}^{\mathsf T}/N_{\mathrm{c}},\ \boldsymbol{1}_{N_{\mathrm{t}}}^{\mathsf T}/N_{\mathrm{t}}\bigr)$. Hence $\operatorname{Var}_{\mathrm{sp}}(\hat{\boldsymbol{\beta}} \mid X) = H\Sigma H^{\mathsf T}$, and its $(2,2)$ entry is

$$
\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{ols}}\bigr) = \frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}}.
$$
Each component of $\hat{\boldsymbol{\beta}}$ is an average of i.i.d. errors within a group, so it is asymptotically normal by the **central limit theorem**. Two variance estimators correspond to two assumptions about $\Sigma$:

| Assumption | Variance estimate | Equals | R |
|---|---|---|---|
| homoscedastic, $\sigma_{\mathrm{t}}^2 = \sigma_{\mathrm{c}}^2 = \sigma^2$ | $\hat\sigma^2\bigl(\frac{1}{N_{\mathrm{c}}} + \frac{1}{N_{\mathrm{t}}}\bigr)$, $\hat\sigma^2 = \frac{1}{N - 2}\sum_i \hat\varepsilon_i^2$ | $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$ of [3.9.4](/3.9.4) | `lm` |
| heteroscedastic, $\sigma_{\mathrm{t}}^2 \ne \sigma_{\mathrm{c}}^2$ allowed | $\frac{\hat\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\hat\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}}$, $\hat\sigma_{\mathrm{t}}^2 = \frac{1}{N_{\mathrm{t}} - 1}\sum_{i: W_i = 1}\hat\varepsilon_i^2$ | $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$ (Definition 4.4.1) | `car::hccm` |

The residuals are $\hat\varepsilon_i = Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}$ for treated and $Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$ for control units, so $\hat\sigma_{\mathrm{t}}^2 = s_{\mathrm{t}}^2$ and $\hat\sigma_{\mathrm{c}}^2 = s_{\mathrm{c}}^2$. Regression inference therefore reproduces Neyman's inference exactly: the conventional OLS standard error is the pooled estimator that is valid under a constant effect, and the heteroscedasticity-robust one is the Neyman estimator.

In general the robust estimator is the **White estimator** ([Definition 12.1.1](/3.3.12#def-12.1.1)), also called the Eicker–Huber–White or heteroscedasticity-consistent covariance matrix estimator,

$$
\widehat{\operatorname{Var}}\bigl(\hat{\boldsymbol{\beta}}\bigr) = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\operatorname{diag}\bigl(\hat\varepsilon_1^2, \dots, \hat\varepsilon_N^2\bigr)X(X^{\mathsf T}X)^{-1},
$$
a moment estimator of $(X^{\mathsf T}X)^{-1}X^{\mathsf T}\Sigma X(X^{\mathsf T}X)^{-1}$. Its finite-sample corrections differ slightly: the original form (HC0) gives $\frac{N_{\mathrm{c}} - 1}{N_{\mathrm{c}}}\frac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{N_{\mathrm{t}} - 1}{N_{\mathrm{t}}}\frac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}}$, and the HC2 correction, which divides $\hat\varepsilon_i^2$ by $1 - h_{ii}$ with leverage $h_{ii} = 1/N_{\mathrm{t}}$ or $1/N_{\mathrm{c}}$, gives exactly $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$. The default of `car::hccm` is HC3, which is slightly larger still.

```r
library(car)
fit <- lm(cholf ~ W, data = lrc)              # tau-hat = difference in means
sqrt(vcov(fit)["W", "W"])                     # pooled: valid under a constant effect
sqrt(hccm(fit, type = "hc2")["W", "W"])       # robust: equals the Neyman standard error
```

### 5.2.4. Two Further Interpretations

*Imputation.* The difficulty of causal inference is missing data: for each unit one potential outcome is missing. Under unconfoundedness, $\mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 0] = \mathbb{E}_{\mathrm{sp}}[Y_i(0)]$ and $\mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 1] = \mathbb{E}_{\mathrm{sp}}[Y_i(1)]$, so the fitted regression predicts the missing outcomes by $\hat Y_i(0) = \hat\alpha$ for treated units and $\hat Y_i(1) = \hat\alpha + \hat\tau$ for control units. The estimated unit-level effects are $\hat\tau_i = Y_i^{\mathrm{obs}} - \hat Y_i(0)$ if $W_i = 1$ and $\hat\tau_i = \hat Y_i(1) - Y_i^{\mathrm{obs}}$ if $W_i = 0$, and their average is

$$
\frac{1}{N}\sum_{i=1}^{N}\hat\tau_i = \frac{1}{N}\sum_{i=1}^{N}\Bigl\{W_i\bigl(Y_i^{\mathrm{obs}} - \hat Y_i(0)\bigr) + (1 - W_i)\bigl(\hat Y_i(1) - Y_i^{\mathrm{obs}}\bigr)\Bigr\} = \hat\tau^{\mathrm{ols}}.
$$
This view, in which regression is one particular imputation rule, is developed into a full method in [3.9.6](/3.9.6).

*Large-sample limit.* As $N \to \infty$ the least squares estimators converge to the minimizers of the population objective,

$$
(\alpha^*, \tau^*) = \arg\min_{\alpha, \tau}\mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \alpha - \tau W_i)^2\bigr],
$$
and the solution of this problem is $\tau^* = \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 1] - \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 0]$, which equals $\tau_{\mathrm{sp}}$ in a CRE. The regression estimator is thus a **consistent estimator** of a population quantity that the design makes causal. The same argument, with covariates added, is the core of Section 5.3.

### 5.2.5. What Regression Adds and What It Does Not

Regression methods are familiar and easy to compute, reproduce Neyman's results, and extend directly to covariates. The other side deserves equal emphasis. A regression can be run on any data set and always returns a coefficient; in general that coefficient describes an association. Its causal meaning comes from the design, not from the regression: in a CRE it is the randomization that makes $\mathbb{E}[\varepsilon_i \mid W_i] = 0$ true and $\tau^* = \tau_{\mathrm{sp}}$. In observational studies, where nothing guarantees this, the same regression can be badly biased ([3.9.8](/3.9.8), [3.9.10](/3.9.10)).

## 5.3. Regression with Covariates

### 5.3.1. Model and Population Counterparts

Add the covariates to the regression:

$$
Y_i^{\mathrm{obs}} = \alpha + \tau W_i + X_i\boldsymbol{\beta} + \varepsilon_i, \qquad
(\hat\tau^{\mathrm{ols}}, \hat\alpha^{\mathrm{ols}}, \hat{\boldsymbol{\beta}}^{\mathrm{ols}}) = \arg\min_{\tau, \alpha, \boldsymbol{\beta}}\sum_{i=1}^{N}\bigl(Y_i^{\mathrm{obs}} - \alpha - \tau W_i - X_i\boldsymbol{\beta}\bigr)^2.
$$
In the language of experimental design this is the **analysis of covariance**. Unlike in Section 5.2.2, the linear model can now be wrong: $\mu_{\mathrm{c}}(x)$ need not be linear, and the effect $\tau(x)$ need not be constant. Rather than assume it is right, define the target of the estimator as the minimizer of the population objective,

$$
(\alpha^*, \tau^*, \boldsymbol{\beta}^*) = \arg\min_{\alpha, \tau, \boldsymbol{\beta}}\mathbb{E}_{\mathrm{sp}}\Bigl[\bigl(Y_i^{\mathrm{obs}} - \alpha - \tau W_i - X_i\boldsymbol{\beta}\bigr)^2\Bigr].
$$
Under the regularity conditions that $\Omega_X$ is positive definite and the second moments are finite, $(\hat\tau^{\mathrm{ols}}, \hat\alpha^{\mathrm{ols}}, \hat{\boldsymbol{\beta}}^{\mathrm{ols}}) \to (\tau^*, \alpha^*, \boldsymbol{\beta}^*)$ in probability. The question is what $\tau^*$ is.

### 5.3.2. The Population Coefficient Is the Average Effect

**Theorem 5.3.1** In a CRE on a random sample from a super-population, $\tau^* = \tau_{\mathrm{sp}}$, whatever the true conditional expectations $\mu_{\mathrm{c}}(x)$ and $\mu_{\mathrm{t}}(x)$ are.

**Proof** Center the covariates by reparametrizing the intercept as $\tilde\alpha = \alpha + \mu_X\boldsymbol{\beta}$. The objective becomes

$$
Q(\tilde\alpha, \tau, \boldsymbol{\beta}) = \mathbb{E}_{\mathrm{sp}}\Bigl[\bigl(Y_i^{\mathrm{obs}} - \tilde\alpha - \tau W_i - (X_i - \mu_X)\boldsymbol{\beta}\bigr)^2\Bigr],
$$
and the minimizing $\tau$ is the same as before, because the reparametrization does not involve $\tau$. Expanding the square,

$$
\begin{aligned}
Q(\tilde\alpha, \tau, \boldsymbol{\beta}) &= \mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \tilde\alpha - \tau W_i)^2\bigr] + \mathbb{E}_{\mathrm{sp}}\bigl[\bigl((X_i - \mu_X)\boldsymbol{\beta}\bigr)^2\bigr]\\
&\quad - 2\,\mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \tilde\alpha - \tau W_i)(X_i - \mu_X)\boldsymbol{\beta}\bigr].
\end{aligned}
$$
In the cross term, $\mathbb{E}_{\mathrm{sp}}[\tilde\alpha(X_i - \mu_X)\boldsymbol{\beta}] = 0$ because $X_i - \mu_X$ has mean zero, and $\mathbb{E}_{\mathrm{sp}}[\tau W_i(X_i - \mu_X)\boldsymbol{\beta}] = \tau\,\mathbb{E}_{\mathrm{sp}}[W_i]\,\mathbb{E}_{\mathrm{sp}}[X_i - \mu_X]\boldsymbol{\beta} = 0$ because the CRE makes $W_i$ independent of $X_i$. Hence

$$
Q(\tilde\alpha, \tau, \boldsymbol{\beta}) = \underbrace{\mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \tilde\alpha - \tau W_i)^2\bigr]}_{\text{depends on } (\tilde\alpha, \tau) \text{ only}} + \underbrace{\mathbb{E}_{\mathrm{sp}}\bigl[\bigl((X_i - \mu_X)\boldsymbol{\beta}\bigr)^2\bigr] - 2\,\mathbb{E}_{\mathrm{sp}}\bigl[Y_i^{\mathrm{obs}}(X_i - \mu_X)\boldsymbol{\beta}\bigr]}_{\text{depends on } \boldsymbol{\beta} \text{ only}}.
$$
The objective separates, so the minimizing $(\tilde\alpha, \tau)$ is the minimizer of the first term alone. That term is the objective of the regression without covariates, whose minimizer is $\tau^* = \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 1] - \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 0]$ (Section 5.2.4). By the independence of $W_i$ and the potential outcomes, this equals $\mathbb{E}_{\mathrm{sp}}[Y_i(1)] - \mathbb{E}_{\mathrm{sp}}[Y_i(0)] = \tau_{\mathrm{sp}}$. $\square$

The proof uses only one property of the design, $W_i \perp X_i$ together with $W_i \perp (Y_i(0), Y_i(1))$, and no property of the regression model. The covariates change $\boldsymbol{\beta}^*$ and the residual, and therefore the precision, but not the target. In an observational study $W_i$ and $X_i$ are typically dependent, the cross term does not vanish, and $\tau^*$ is in general not a causal effect.

### 5.3.3. Asymptotic Normality

**Theorem 5.3.2** Suppose a CRE is conducted on a sample drawn at random from an infinite super-population, with $N_{\mathrm{t}}/N \to p \in (0, 1)$. Then $\hat\tau^{\mathrm{ols}} \xrightarrow{p} \tau^* = \tau_{\mathrm{sp}}$ and

$$
\sqrt{N}\bigl(\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}}\bigr) \xrightarrow{d} \mathcal{N}\left(0,\ \frac{\mathbb{E}_{\mathrm{sp}}\bigl[(W_i - p)^2\bigl(Y_i^{\mathrm{obs}} - \alpha^* - \tau_{\mathrm{sp}}W_i - X_i\boldsymbol{\beta}^*\bigr)^2\bigr]}{p^2(1 - p)^2}\right).
$$
The theorem holds whether or not the regression model is correct.

**Proof** (sketch) By the **Frisch–Waugh–Lovell theorem**, $\hat\tau^{\mathrm{ols}}$ is the slope in the regression of $Y^{\mathrm{obs}}$ on the residual $\tilde W_i$ of $W_i$ after regression on an intercept and $X_i$. Because $W_i$ and $X_i$ are independent, the population residual is $W_i - p$, and the sample residual differs from it by $O_p(N^{-1/2})$. Writing $\varepsilon_i^* = Y_i^{\mathrm{obs}} - \alpha^* - \tau_{\mathrm{sp}}W_i - X_i\boldsymbol{\beta}^*$, whose first-order conditions give $\mathbb{E}_{\mathrm{sp}}[\varepsilon_i^*] = \mathbb{E}_{\mathrm{sp}}[W_i\varepsilon_i^*] = 0$ and $\mathbb{E}_{\mathrm{sp}}[X_i^{\mathsf T}\varepsilon_i^*] = \boldsymbol{0}$, one obtains

$$
\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}} = \frac{\frac{1}{N}\sum_i (W_i - p)\varepsilon_i^*}{p(1 - p)} + o_p\bigl(N^{-1/2}\bigr).
$$
The summands are i.i.d. with mean zero and variance $\mathbb{E}_{\mathrm{sp}}[(W_i - p)^2(\varepsilon_i^*)^2]$, and the **central limit theorem** with **Slutsky's theorem** gives the result. $\square$

Without covariates ($\boldsymbol{\beta}^* = \boldsymbol{0}$), $\varepsilon_i^* = Y_i(1) - \mu_{\mathrm{t}}$ for treated and $Y_i(0) - \mu_{\mathrm{c}}$ for control units, and the asymptotic variance is

$$
\frac{p(1 - p)^2\sigma_{\mathrm{t}}^2 + (1 - p)p^2\sigma_{\mathrm{c}}^2}{p^2(1 - p)^2} = \frac{\sigma_{\mathrm{t}}^2}{p} + \frac{\sigma_{\mathrm{c}}^2}{1 - p},
$$
which is $N$ times the Neyman variance $\sigma_{\mathrm{c}}^2/N_{\mathrm{c}} + \sigma_{\mathrm{t}}^2/N_{\mathrm{t}}$ of Theorem 4.6.1. With covariates, the residual $\varepsilon_i^*$ is what remains after the best linear prediction from $X_i$, and it is smaller when the covariates predict the outcome.

### 5.3.4. The Gain in Precision: a Special Case

**Example 5.3.1** Suppose that the linear model with a common slope is correct and the outcome variance does not depend on the treatment or the covariates:

$$
\mathbb{E}_{\mathrm{sp}}\bigl[Y_i^{\mathrm{obs}} \bigm| X_i = x, W_i = w\bigr] = \alpha_{\mathrm{c}} + \tau_{\mathrm{sp}}w + x\boldsymbol{\beta}, \qquad
\operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(w) \mid X_i = x\bigr) = \sigma_{Y \mid W, X}^2 \quad \text{for } w = 0, 1 \text{ and all } x.
$$
Show that adjusting for $X$ reduces the asymptotic variance by the factor $1 - R^2$, where $R^2$ is the proportion of the outcome variance (within a treatment group) explained by $X$.

*Without covariates.* Within each treatment group the outcome variance is the same, $\sigma_{Y \mid W}^2 = \operatorname{Var}_{\mathrm{sp}}(Y_i(w))$. The homoscedastic variance estimate is

$$
\widehat{\operatorname{Var}}{}^{\mathrm{homosk}} = \frac{\hat\sigma_{Y \mid W}^2}{\sum_{i=1}^{N}(W_i - \bar W)^2} = \hat\sigma_{Y \mid W}^2\Bigl(\frac{1}{N_{\mathrm{c}}} + \frac{1}{N_{\mathrm{t}}}\Bigr), \qquad
\hat\sigma_{Y \mid W}^2 = \frac{1}{N - 2}\Bigl(\sum_{i: W_i = 0}(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}})^2 + \sum_{i: W_i = 1}(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}})^2\Bigr),
$$
and $N \cdot \widehat{\operatorname{Var}}{}^{\mathrm{homosk}} \xrightarrow{p} \sigma_{Y \mid W}^2/\bigl(p(1 - p)\bigr)$.

*With covariates.* The model is correct, so $\boldsymbol{\beta}^* = \boldsymbol{\beta}$ and $\varepsilon_i^*$ has conditional variance $\sigma_{Y \mid W, X}^2$ given $(W_i, X_i)$. In Theorem 5.3.2, $\mathbb{E}_{\mathrm{sp}}[(W_i - p)^2(\varepsilon_i^*)^2] = \mathbb{E}_{\mathrm{sp}}[(W_i - p)^2]\,\sigma_{Y \mid W, X}^2 = p(1 - p)\sigma_{Y \mid W, X}^2$, so the asymptotic variance of $\sqrt{N}(\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}})$ is $\sigma_{Y \mid W, X}^2/\bigl(p(1 - p)\bigr)$.

*Comparison.* Since $X_i \perp W_i$, the law of total variance within a treatment group gives $\sigma_{Y \mid W}^2 = \sigma_{Y \mid W, X}^2 + \boldsymbol{\beta}^{\mathsf T}\Omega_X\boldsymbol{\beta}$. Hence

$$
\frac{\text{asymptotic variance with } X}{\text{asymptotic variance without } X} = \frac{\sigma_{Y \mid W, X}^2}{\sigma_{Y \mid W}^2} = 1 - R^2, \qquad R^2 = \frac{\boldsymbol{\beta}^{\mathsf T}\Omega_X\boldsymbol{\beta}}{\sigma_{Y \mid W}^2}.
$$
A covariate with $R^2 = 0.75$ halves the standard error; the gain is the same as quadrupling the sample size.

:::

In this special case adjustment never hurts. In general it can: Freedman (2008) showed that when the slopes differ between the two groups and the design is unbalanced ($p \ne 1/2$), the asymptotic variance of the estimator of Theorem 5.3.2 can exceed that of $\hat\tau^{\mathrm{dif}}$, and the conventional (homoscedastic) standard error can then be inconsistent. The remedy is to include interactions (Section 5.4), and to use the robust variance estimator of the next subsection, which is valid in either case.

### 5.3.5. Estimating the Variance

Replacing population expectations by sample averages in Theorem 5.3.2 gives the heteroscedasticity-robust estimator of the sampling variance,

$$
\widehat{\operatorname{Var}}{}^{\mathrm{hetero}}_{\mathrm{sp}} = \frac{1}{N(N - 1 - K)} \cdot \frac{\sum_{i=1}^{N}(W_i - \bar W)^2\bigl(Y_i^{\mathrm{obs}} - \hat\alpha^{\mathrm{ols}} - \hat\tau^{\mathrm{ols}}W_i - X_i\hat{\boldsymbol{\beta}}^{\mathrm{ols}}\bigr)^2}{\bar W^2(1 - \bar W)^2},
$$
and under homoscedasticity the simpler

$$
\widehat{\operatorname{Var}}{}^{\mathrm{homo}}_{\mathrm{sp}} = \frac{1}{N(N - 1 - K)} \cdot \frac{\sum_{i=1}^{N}\bigl(Y_i^{\mathrm{obs}} - \hat\alpha^{\mathrm{ols}} - \hat\tau^{\mathrm{ols}}W_i - X_i\hat{\boldsymbol{\beta}}^{\mathrm{ols}}\bigr)^2}{\bar W(1 - \bar W)},
$$
where $K = \dim X_i$. The first is, up to the degrees-of-freedom factor, the $(\tau, \tau)$ entry of the White estimator for this regression; it is the one to use unless the homoscedastic model has good support.

### 5.3.6. Imputation Interpretation

The covariate-adjusted estimator is again an imputation estimator. Impute $\hat Y_i(0) = \hat\alpha^{\mathrm{ols}} + X_i\hat{\boldsymbol{\beta}}^{\mathrm{ols}}$ for treated units and $\hat Y_i(1) = \hat\alpha^{\mathrm{ols}} + \hat\tau^{\mathrm{ols}} + X_i\hat{\boldsymbol{\beta}}^{\mathrm{ols}}$ for control units. With residuals $\hat\varepsilon_i$, the estimated unit-level effect is $\hat\tau^{\mathrm{ols}} + \hat\varepsilon_i$ for treated units and $\hat\tau^{\mathrm{ols}} - \hat\varepsilon_i$ for control units, so

$$
\frac{1}{N}\sum_{i=1}^{N}\hat\tau_i = \hat\tau^{\mathrm{ols}} + \frac{1}{N}\Bigl(\sum_{i: W_i = 1}\hat\varepsilon_i - \sum_{i: W_i = 0}\hat\varepsilon_i\Bigr) = \hat\tau^{\mathrm{ols}},
$$
because the normal equations for the intercept and for $W$ make the residuals sum to zero in each group. Under unconfoundedness, the regression is a device for predicting each missing potential outcome from the unit's covariates; a better prediction gives a more precise estimate.

### 5.3.7. The LRC-CPPT Results

| Covariates | Estimate | (s.e.) |
|---|---|---|
| none | $-26.22$ | $(3.93)$ |
| `cholp` | $-25.01$ | $(2.60)$ |
| `chol1`, `chol2` | $-25.02$ | $(2.59)$ |
| `chol1`, `chol2`, interacted with $W$ | $-25.04$ | $(2.56)$ |

The effect of assignment to the drug on post-treatment cholesterol is a reduction of about 25 units. The point estimate hardly moves when the covariates are added, as randomization implies, but the standard error falls by a third: the pre-treatment measurements explain more than half of the outcome variance ($1 - (2.60/3.93)^2 \approx 0.56$). Using two separate pre-treatment measurements instead of their combination, or adding interactions, changes almost nothing.

### 5.3.8. Are More Covariates Always Better?

Even under unconfoundedness the answer is no, for three reasons.

- *Post-treatment variables.* The argument of Theorem 5.3.1 requires $X_i \perp W_i$, which holds only for variables determined before the assignment. The compliance variable `comp` of the LRC-CPPT is affected by the treatment (the treated took a smaller share of their dose, presumably because of side effects), so it is a function of the assignment, and adjusting for it changes the estimand to something that is no longer a causal effect of assignment. Effects in subgroups defined by post-treatment behavior require the methods of [3.9.14](/3.9.14).
- *Finite-sample bias.* $\hat\tau^{\mathrm{ols}}$ with covariates is consistent but, unlike $\hat\tau^{\mathrm{dif}}$, not exactly unbiased; its bias is of order $1/N$ and grows with the number of covariates relative to the sample size.
- *Precision.* A covariate that does not predict the outcome costs a degree of freedom and, in the unbalanced heterogeneous case of Section 5.3.4, can increase the variance.

In practice the covariates should be few, measured before the assignment, chosen for their expected predictive power, and fixed before looking at the outcomes, so that the choice cannot be tuned to the result.

## 5.4. Interactions and Tests

### 5.4.1. The Interacted Regression

Allowing the slope to differ between the groups gives the model

$$
Y_i^{\mathrm{obs}} = \alpha + \tau W_i + X_i\boldsymbol{\beta} + W_i(X_i - \bar X)\boldsymbol{\gamma} + \varepsilon_i,
$$
with least squares estimators $(\hat\tau^{\mathrm{ols}}, \hat\alpha^{\mathrm{ols}}, \hat{\boldsymbol{\beta}}^{\mathrm{ols}}, \hat{\boldsymbol{\gamma}}^{\mathrm{ols}})$ and population counterparts $(\tau^*, \alpha^*, \boldsymbol{\beta}^*, \boldsymbol{\gamma}^*)$, defined with $\mu_X$ in place of $\bar X$. Because the model is fully interacted, it is equivalent to separate regressions in the two groups, $\hat\mu_{\mathrm{c}}(x) = \hat\alpha_{\mathrm{c}} + x\hat{\boldsymbol{\beta}}_{\mathrm{c}}$ and $\hat\mu_{\mathrm{t}}(x) = \hat\alpha_{\mathrm{t}} + x\hat{\boldsymbol{\beta}}_{\mathrm{t}}$, and centering the interaction at $\bar X$ makes the coefficient of $W_i$ the average of the predicted effects over the whole sample,

$$
\hat\tau^{\mathrm{ols}} = \hat\mu_{\mathrm{t}}(\bar X) - \hat\mu_{\mathrm{c}}(\bar X) = \frac{1}{N}\sum_{i=1}^{N}\bigl(\hat\mu_{\mathrm{t}}(X_i) - \hat\mu_{\mathrm{c}}(X_i)\bigr).
$$
Without the centering, the coefficient of $W_i$ would be the predicted effect at $X_i = 0$, which is usually not of interest. This is again an imputation estimator, now with a separate prediction model for each potential outcome.

**Theorem 5.4.1** In a CRE on a random sample from a super-population, (i) $\tau^* = \tau_{\mathrm{sp}}$, and (ii)

$$
\sqrt{N}\bigl(\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}}\bigr) \xrightarrow{d} \mathcal{N}\left(0,\ \frac{\mathbb{E}_{\mathrm{sp}}\bigl[(W_i - p)^2\bigl(Y_i^{\mathrm{obs}} - \alpha^* - \tau_{\mathrm{sp}}W_i - X_i\boldsymbol{\beta}^* - W_i(X_i - \mu_X)\boldsymbol{\gamma}^*\bigr)^2\bigr]}{p^2(1 - p)^2}\right).
$$
The proof follows that of Theorems 5.3.1 and 5.3.2: $\mu_{\mathrm{t}}^{\mathrm{lin}}(\mu_X) - \mu_{\mathrm{c}}^{\mathrm{lin}}(\mu_X)$, the difference of the two population linear predictions at the covariate mean, equals $\mathbb{E}_{\mathrm{sp}}[Y_i(1)] - \mathbb{E}_{\mathrm{sp}}[Y_i(0)]$ because each population regression with an intercept reproduces the mean of its outcome at the mean of its regressors, and $X_i$ has the same distribution in both groups.

The advantage of the interactions is that the two groups may have different slopes. Lin (2013) showed that the interacted estimator is asymptotically at least as precise as both $\hat\tau^{\mathrm{dif}}$ and the estimator of Section 5.3, whatever the true regression functions, and that the robust variance estimator is consistent or conservative for it. With a common slope, or with $p = 1/2$, the interactions bring no asymptotic gain, but they cost little.

![Simulated completely randomized experiments with N = 100 and one normal covariate (average effect 1). Left: with a common slope and half the units treated, the two regression estimators have a much smaller spread than the difference in means. Right: with slopes -1 under control and 3 under treatment, the regression without interaction can be less precise than the difference in means when the design is unbalanced, while the interacted regression is the most precise for every proportion treated. Simulated data](./plots/covariate_adjustment.py)

### 5.4.2. Tests of Effect Heterogeneity

The interacted model also allows tests of how the effect varies with the covariates. Let $\widehat{\operatorname{Var}}(\hat\tau^{\mathrm{ols}}, \hat{\boldsymbol{\gamma}}^{\mathrm{ols}})$ be the robust estimate of the covariance matrix of $(\hat\tau^{\mathrm{ols}}, \hat{\boldsymbol{\gamma}}^{\mathrm{ols}})$, with blocks $\widehat{\operatorname{Var}}_\tau$, $\widehat{\operatorname{Var}}_\gamma$ and $\widehat{\operatorname{Cov}}_{\tau, \gamma}$. Two null hypotheses are of interest:

| Null hypothesis | Statistic | Limit under $H_0$ |
|---|---|---|
| constant effect: $H_0'\colon \tau(x) = \tau_{\mathrm{sp}}$ for all $x$ | $Q_{\mathrm{const}} = (\hat{\boldsymbol{\gamma}}^{\mathrm{ols}})^{\mathsf T}\widehat{\operatorname{Var}}_\gamma^{-1}\hat{\boldsymbol{\gamma}}^{\mathrm{ols}}$ | $\chi^2_K$ |
| zero effect: $H_0\colon \tau(x) = 0$ for all $x$ | $Q_{\mathrm{zero}} = \begin{pmatrix}\hat\tau^{\mathrm{ols}}\\ \hat{\boldsymbol{\gamma}}^{\mathrm{ols}}\end{pmatrix}^{\mathsf T}\widehat{\operatorname{Var}}(\hat\tau^{\mathrm{ols}}, \hat{\boldsymbol{\gamma}}^{\mathrm{ols}})^{-1}\begin{pmatrix}\hat\tau^{\mathrm{ols}}\\ \hat{\boldsymbol{\gamma}}^{\mathrm{ols}}\end{pmatrix}$ | $\chi^2_{K+1}$ |

**Theorem 5.4.2** In a CRE on a random sample from a large population, if $Y_i(1) - Y_i(0) = \tau$ for some constant $\tau$ and all units, then $\boldsymbol{\gamma}^* = \boldsymbol{0}$ and $Q_{\mathrm{const}} \xrightarrow{d} \chi^2_K$; if $Y_i(1) - Y_i(0) = 0$ for all units, then $\tau^* = 0$, $\boldsymbol{\gamma}^* = \boldsymbol{0}$ and $Q_{\mathrm{zero}} \xrightarrow{d} \chi^2_{K+1}$.

Both are **Wald tests** of several parameters, and their conclusions are about linear projections: $\boldsymbol{\gamma}^* = \boldsymbol{0}$ does not exclude heterogeneity that is uncorrelated with linear functions of $X$. The zero-effect hypothesis is a sharp null, so it can also be tested exactly with $Q_{\mathrm{zero}}$ as the statistic of Fisher's test ([3.9.3](/3.9.3)).

For the LRC-CPPT data with `chol1` and `chol2` as covariates ($K = 2$):

| Hypothesis | Method | p-value |
|---|---|---|
| zero effect | $\chi^2_3$ approximation | $< 0.001$ |
| zero effect | Fisher exact p-value | $< 0.001$ |
| constant effect | $\chi^2_2$ approximation | $0.029$ |

The evidence that the drug lowers cholesterol is overwhelming. There is some evidence that the effect varies with the pre-treatment level ($p = 0.029$), but the variation is small relative to the average effect, and allowing for it leaves the estimated average effect unchanged.

## Summary

| Regression | Target | Key property | Variance (times $N$, asymptotically) |
|---|---|---|---|
| $Y^{\mathrm{obs}} \sim 1 + W$ | $\tau_{\mathrm{sp}}$ | $\hat\tau^{\mathrm{ols}} = \hat\tau^{\mathrm{dif}}$ (Theorem 5.2.1); $\mathbb{E}[\varepsilon \mid W] = 0$ by randomization | $\sigma_{\mathrm{t}}^2/p + \sigma_{\mathrm{c}}^2/(1 - p)$ |
| $Y^{\mathrm{obs}} \sim 1 + W + X$ | $\tau^* = \tau_{\mathrm{sp}}$ (Theorem 5.3.1) | consistent and asymptotically normal even if the model is wrong (Theorem 5.3.2) | $\mathbb{E}[(W - p)^2\varepsilon^{*2}]/(p(1 - p))^2$ |
| $Y^{\mathrm{obs}} \sim 1 + W + X + W(X - \bar X)$ | $\tau^* = \tau_{\mathrm{sp}}$ (Theorem 5.4.1) | separate slopes; never worse asymptotically | same form with the interacted residual |

- The causal meaning of the regression coefficient comes from the design: $W_i \perp (Y_i(0), Y_i(1), X_i)$ in a CRE. The same regression in an observational study estimates an association.
- Without covariates, the conventional standard error is $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$ and the robust (HC2) one is $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$; regression inference coincides with Neyman's.
- Covariates help by explaining outcome variance: under a correct homoscedastic model the variance is multiplied by $1 - R^2$ (Example 5.3.1). Without interactions, adjustment can hurt when slopes differ and $p \ne 1/2$; with interactions it cannot (asymptotically).
- Every regression estimator here is an imputation estimator: the average of $Y_i^{\mathrm{obs}} - \hat Y_i(0)$ and $\hat Y_i(1) - Y_i^{\mathrm{obs}}$.
- Use only pre-treatment covariates, few of them, chosen before seeing the outcomes; report robust standard errors.
- LRC-CPPT: $-26.2$ (3.9) without and $-25.0$ (2.6) with pre-treatment cholesterol.

## Questions

1. Show that in a CRE the estimator $\hat\tau^{\mathrm{ols}}$ of the regression without covariates is unbiased for $\tau_{\mathrm{sp}}$, using only the regression representation of Section 5.2.2.

   **Answer** By Theorem 5.2.1, $\hat\tau^{\mathrm{ols}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$. Insert $Y_i^{\mathrm{obs}} = \alpha + \tau W_i + \varepsilon_i$: $\bar Y_{\mathrm{t}}^{\mathrm{obs}} = \alpha + \tau + \bar\varepsilon_{\mathrm{t}}$ and $\bar Y_{\mathrm{c}}^{\mathrm{obs}} = \alpha + \bar\varepsilon_{\mathrm{c}}$, so $\hat\tau^{\mathrm{ols}} = \tau + \bar\varepsilon_{\mathrm{t}} - \bar\varepsilon_{\mathrm{c}}$. Conditional on $\boldsymbol{W}$, each $\varepsilon_i$ has mean zero because $\mathbb{E}_{\mathrm{sp}}[\varepsilon_i \mid W_i] = 0$ and the units are i.i.d. and independent of the assignment. Hence $\mathbb{E}_{\mathrm{sp}}[\hat\tau^{\mathrm{ols}} \mid \boldsymbol{W}] = \tau = \tau_{\mathrm{sp}}$, and unbiasedness follows by averaging over $\boldsymbol{W}$.

2. In a CRE with $N = 6$, $N_{\mathrm{t}} = 3$, the observed outcomes are $3, 5, 7$ (treated) and $2, 2, 5$ (control). Compute $\hat\tau^{\mathrm{ols}}$, the conventional OLS standard error, and the HC0 and HC2 robust standard errors. Which one equals the Neyman standard error?

   **Answer** $\bar Y_{\mathrm{t}}^{\mathrm{obs}} = 5$, $\bar Y_{\mathrm{c}}^{\mathrm{obs}} = 3$, so $\hat\tau^{\mathrm{ols}} = 2$. The residual sums of squares are $4 + 0 + 4 = 8$ (treated) and $1 + 1 + 4 = 6$ (control), so $s_{\mathrm{t}}^2 = 4$, $s_{\mathrm{c}}^2 = 3$. Conventional: $\hat\sigma^2 = 14/4 = 3.5$, variance $3.5(1/3 + 1/3) = 2.333$, s.e. $1.53$. HC0: $8/9 + 6/9 = 1.556$, s.e. $1.25$. HC2: $s_{\mathrm{t}}^2/3 + s_{\mathrm{c}}^2/3 = 4/3 + 1 = 2.333$, s.e. $1.53$. HC2 equals the Neyman estimate $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$. Here it also coincides with the conventional one, because $N_{\mathrm{t}} = N_{\mathrm{c}}$: with equal group sizes the pooled and the Neyman estimators are identical.

3. Where exactly does the proof of Theorem 5.3.1 use the randomization? Give an example of an observational study in which $\tau^* \ne \tau_{\mathrm{sp}}$ even though the true regression of each potential outcome on $X$ is linear.

   **Answer** Twice: to make the cross term vanish ($\mathbb{E}[W_i(X_i - \mu_X)] = 0$ needs $W_i \perp X_i$), and to identify the coefficient of the regression of $Y^{\mathrm{obs}}$ on $W$ alone with $\tau_{\mathrm{sp}}$ ($W_i \perp (Y_i(0), Y_i(1))$). Example: $X_i \sim \mathcal{N}(0, 1)$, $Y_i(0) = X_i$ and $Y_i(1) = 3X_i$, so both regressions are linear and $\tau_{\mathrm{sp}} = \mathbb{E}[2X_i] = 0$, and units with large $X_i$ are treated, $W_i = \boldsymbol{1}\{X_i > 1\}$. The regression $Y^{\mathrm{obs}} \sim 1 + W + X$ forces a common slope; because the treated units all have large $X_i$, where $Y_i(1) - Y_i(0) = 2X_i$ is large, the coefficient of $W$ absorbs this: a numerical calculation gives $\tau^* \approx 2.85$, far from $\tau_{\mathrm{sp}} = 0$. It measures roughly the effect among the treated, not the population average, and even that only through extrapolation of a misspecified line. Observational studies need the design tools of [3.9.8](/3.9.8)–[3.9.10](/3.9.10) for this reason.

4. (Gain from covariates) In Example 5.3.1, suppose the pre-treatment cholesterol explains $60\%$ of the within-group variance of post-treatment cholesterol. By how much does adjusting for it reduce the standard error, and how many units would an unadjusted analysis need to reach the same precision?

   **Answer** The variance is multiplied by $1 - R^2 = 0.4$, so the standard error by $\sqrt{0.4} \approx 0.63$, a reduction of $37\%$. Since the variance is inversely proportional to $N$, the unadjusted analysis would need $N/0.4 = 2.5N$ units.

5. Show that the interacted estimator of Section 5.4.1 with centering at $\bar X$ satisfies $\hat\tau^{\mathrm{ols}} = (\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}) - (\bar X_{\mathrm{t}} - \bar X)\hat{\boldsymbol{\beta}}_{\mathrm{t}} + (\bar X_{\mathrm{c}} - \bar X)\hat{\boldsymbol{\beta}}_{\mathrm{c}}$, and interpret the correction terms.

   **Answer** In the separate regressions, the fitted line passes through the group means: $\hat\alpha_{\mathrm{t}} + \bar X_{\mathrm{t}}\hat{\boldsymbol{\beta}}_{\mathrm{t}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}}$, so $\hat\mu_{\mathrm{t}}(\bar X) = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - (\bar X_{\mathrm{t}} - \bar X)\hat{\boldsymbol{\beta}}_{\mathrm{t}}$, and likewise for the control group. Subtracting gives the formula. Each group mean is moved from the group's own covariate mean to the overall mean along the group's own regression line. In a CRE $\bar X_{\mathrm{t}} - \bar X$ and $\bar X_{\mathrm{c}} - \bar X$ are small, of order $N^{-1/2}$, and the correction removes the part of $\hat\tau^{\mathrm{dif}}$ due to chance covariate imbalance.

6. (Vote) If the assignment is unconfounded, is adding more covariates always better? Give an argument for each side and a conclusion.

   **Answer** For: under unconfoundedness each additional pre-treatment covariate leaves the target $\tau^* = \tau_{\mathrm{sp}}$ unchanged (Theorem 5.3.1) and may explain more outcome variance. Against: a variable measured after the assignment (such as compliance) is not covered by the theorem and changes the estimand; with many covariates relative to $N$ the finite-sample bias and the loss of degrees of freedom grow; without interactions, covariates can even increase the asymptotic variance when slopes differ and the design is unbalanced. Conclusion: not always; use a small number of pre-treatment covariates chosen in advance for their predictive power, preferably with interactions and robust standard errors.

7. In the LRC-CPPT data, the standard error falls from $3.93$ to $2.60$ when `cholp` is added. Estimate the proportion of outcome variance explained by `cholp`, and explain why the point estimate changes from $-26.22$ to $-25.01$ although randomization makes both estimators consistent for the same quantity.

   **Answer** Approximately $1 - (2.60/3.93)^2 = 1 - 0.438 \approx 0.56$. The change of $1.2$ is chance imbalance: the treated group's mean `cholp` is $1.3$ lower than the control group's ($289.9$ vs $291.2$), and with a slope of about one the adjusted estimate removes the part of the difference in means attributable to this imbalance. The change is well within one standard error, as it should be in a randomized experiment.

8. Why is the zero-effect test of Section 5.4.2 available both as a $\chi^2$ test and as an exact Fisher test, while the constant-effect test is only approximate?

   **Answer** Under the zero-effect hypothesis, $Y_i(1) = Y_i(0)$ for all units is a sharp null: all missing potential outcomes are known, and the randomization distribution of any statistic, including $Q_{\mathrm{zero}}$, can be computed exactly ([3.9.3](/3.9.3)). The constant-effect hypothesis leaves the value of $\tau$ unspecified, so the missing outcomes are known only up to the nuisance parameter $\tau$; the test must rely on the large-sample $\chi^2_K$ approximation (or on a more elaborate construction that maximizes or plugs in over $\tau$).
