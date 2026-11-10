---
title: Unconfounded Assignment and the Propensity Score
description: Observational studies with a regular assignment mechanism. The barbiturate exposure data; why unconfoundedness cannot be tested and why it is so widely assumed; regular assignment mechanisms as stratified experiments with unknown propensity scores; balancing scores, the balancing property of the propensity score, the propensity score as the coarsest balancing score and unconfoundedness given a balancing score; propensity score and covariate balance; an overview of six estimation strategies (imputation, regression, weighting, blocking, matching, mixed); estimating the propensity score by logistic regression with a three-step covariate selection.
---

With this chapter we leave randomized experiments and turn to observational studies, in which the researcher does not control the assignment and does not know the assignment mechanism. Without restrictions on the mechanism nothing can be said about causal effects, so we work with the most tractable class: the **regular assignment mechanism** of [3.9.2](/3.9.2), which is individualistic, probabilistic and unconfounded, but has an unknown propensity score. Such a mechanism behaves like a **stratified randomized experiment** ([3.9.7](/3.9.7)) in which the probability of treatment in each stratum is unknown and the strata are defined by the covariates. The key tool is the **propensity score**: it is the coarsest function of the covariates that balances them between the treatment groups, and almost every method for regular assignment mechanisms uses it. This chapter states the assumptions and their limits (§8.1), proves the balancing properties of the propensity score (§8.2), surveys the estimation strategies (§8.3) and shows how the propensity score is estimated (§8.4). The design of the study with the estimated score follows in [3.9.9](/3.9.9), the estimators of the treatment effect in [3.9.10](/3.9.10). When unconfoundedness fails because of an unobserved confounder, different tools are needed: instrumental variables ([3.9.14](/3.9.14)) or the graphical criteria of [3.9.12](/3.9.12).

Throughout the chapter we use the **super-population** view: the units are a random sample, $(Y_i(0), Y_i(1), W_i, X_i)$ are independent and identically distributed, $\mathbb{E}$ without subscript is over this joint distribution, $X_i$ is a $1 \times K$ row vector of pre-treatment covariates, and the propensity score is $e(x) = \mathbb{P}(W_i = 1 \mid X_i = x)$.

## 8.1. Assumptions in Observational Studies

### 8.1.1. The Barbiturate Exposure Data

**Example 8.1.1 (Prenatal Exposure to Barbiturates)** Reinisch, Sanders, Mortensen and Rubin (1995) studied the effect of prenatal exposure to barbiturates, a class of sedatives acting on the central nervous system, on the cognitive development of children. The treated units are children who were exposed in utero to substantial amounts of barbiturates, the controls children who were not; the outcomes are measures of cognitive development in adulthood. Seventeen covariates were recorded for each child, describing the mother (for example her age and socioeconomic status), the course of the pregnancy and the child (for example sex). In the sample used below there are $N_{\mathrm{t}} = 742$ exposed and $N_{\mathrm{c}} = 4462$ unexposed children.

:::

No one would randomize pregnant women to sedatives, so the effect can only be studied observationally. The treatment was chosen by doctors and mothers on the basis of the mother's health and circumstances, which also affect the child's development: the exposed and unexposed children differ systematically in their covariates, and a simple comparison of outcomes would mix the effect of the drug with these differences. The data illustrate the whole design phase: here and in §8.4 the propensity score is estimated, and [3.9.9](/3.9.9) uses it to assess and improve the balance of the covariates.

### 8.1.2. Regular Assignment Mechanisms

Recall the classification of [3.9.2](/3.9.2). A randomized experiment is probabilistic and has a known functional form controlled by the researcher; a classical randomized experiment is in addition individualistic and **unconfounded**. An **observational study** is an assignment mechanism with unknown functional form. The difference from an experiment is not the presence of chance but our ignorance of the mechanism. A regular assignment mechanism is the observational counterpart of a classical randomized experiment: it is

1. individualistic: unit $i$'s assignment probability depends only on its own covariates and potential outcomes;
2. probabilistic: $0 < \mathbb{P}(W_i = 1 \mid X_i, Y_i(0), Y_i(1)) < 1$;
3. unconfounded: $\mathbb{P}(\boldsymbol{W} \mid \boldsymbol{X}, \boldsymbol{Y}(0), \boldsymbol{Y}(1)) = \mathbb{P}(\boldsymbol{W} \mid \boldsymbol{X})$.

Under the three conditions the assignment mechanism is a product of propensity scores (up to the set of allowed assignments and a constant),

$$
\mathbb{P}\bigl(\boldsymbol{W} \mid \boldsymbol{X}, \boldsymbol{Y}(0), \boldsymbol{Y}(1)\bigr) = c \cdot \prod_{i=1}^{N} e(X_i)^{W_i}\bigl(1 - e(X_i)\bigr)^{1 - W_i}, \qquad 0 < e(x) < 1,
$$
and in the super-population the conditions reduce to **strong ignorability**: $W_i \perp (Y_i(0), Y_i(1)) \mid X_i$ and $0 < e(x) < 1$. The first part is a **conditional independence** statement: among units with the same covariates, those who were treated and those who were not have the same distribution of potential outcomes. Epidemiologists call the same condition conditional exchangeability, since the treated and untreated units could be exchanged without changing the distribution of potential outcomes; it is the unconfoundedness of this course in other words. The second part is **positivity**: every type of unit could have received either treatment.

### 8.1.3. Unconfoundedness Cannot Be Tested

**Remark 8.1.1 (Unconfoundedness Is Not Testable)** Unconfoundedness restricts the joint distribution of $W_i$ and $(Y_i(0), Y_i(1))$ given $X_i$. For every unit one of the two potential outcomes is missing, so the restriction involves $Y_i^{\mathrm{mis}}$, and the data contain no information that could reveal a violation, however many units we observe. Indeed, for any distribution of the observed data $(Y_i^{\mathrm{obs}}, W_i, X_i)$ we can construct a joint distribution of $(Y_i(0), Y_i(1), W_i, X_i)$ that reproduces it and satisfies unconfoundedness: let $Y_i(1)$ given $X_i = x$ have, for all units, the observed distribution of $Y_i^{\mathrm{obs}}$ given $W_i = 1$, $X_i = x$, and similarly for $Y_i(0)$. We can equally construct one that reproduces it and violates unconfoundedness. Any claim that unconfoundedness fails must therefore rest on additional information: substantive knowledge, a second control group, or a pseudo-outcome known to be unaffected by the treatment.

The consequence is that the choice of covariates is the crucial scientific decision of an observational study. Unconfoundedness becomes more plausible when the covariates include everything that drove the assignment and is related to the outcomes; it can only be argued, never verified.

### 8.1.4. Why Unconfoundedness Is So Widely Assumed

The assumption is used far more often than it is stated, because it is usually hidden in a functional form. In the linear model

$$
Y_i^{\mathrm{obs}} = \alpha + \tau W_i + X_i\boldsymbol{\beta} + \varepsilon_i, \qquad \mathbb{E}[\varepsilon_i \mid W_i, X_i] = 0,
$$
the second condition, exogeneity of the regressors, seems to be a statement about an error term, not about potential outcomes. But if the model is to have a causal meaning, the potential outcomes are $Y_i(w) = \alpha + \tau w + X_i\boldsymbol{\beta} + \varepsilon_i$ with the same $\varepsilon_i$ for both $w$ (a constant unit-level effect $\tau$), so $\varepsilon_i = Y_i(0) - \alpha - X_i\boldsymbol{\beta}$ is a function of $Y_i(0)$ and $X_i$. Exogeneity says that $W_i$ carries no information about the mean of $Y_i(0)$ given $X_i$, which is (the mean version of) unconfoundedness. Regression analyses of observational data thus assume unconfoundedness together with linearity and a constant effect; the methods of this and the next two chapters keep the first assumption and drop the other two.

### 8.1.5. Regular Assignment Mechanisms and Stratified Experiments

A regular assignment mechanism and a stratified randomized experiment have the same structure. In both, inference is based on strata of units with the same covariate value $X_i = x$, and within each stratum the assignment is random, so stratum-level causal effects are identified and can be estimated by comparing the treated and control units of the stratum. The difference lies in what is known:

| | Stratified randomized experiment | Regular assignment mechanism |
|---|---|---|
| Strata | chosen by the design | defined by the covariate values |
| Assignment within a stratum | completely randomized | individualistic, unconfounded, probabilistic |
| Stratum propensity score $e(j)$ | known, $N_{\mathrm{t}}(j)/N(j)$ | unknown, estimated by $\hat e(j) = N_{\mathrm{t}}(j)/N(j)$ |
| Number of strata | small, fixed in advance | number of distinct covariate values |

A regular assignment mechanism can thus be analyzed as a stratified randomized experiment with an unknown propensity score in each stratum. If $X_i$ takes only a few values, this works directly: estimate the effect within each stratum by the difference in means and average the estimates with the stratum proportions as weights. The obstacle is the sample size. With $K$ binary covariates there are $2^K$ strata, which for $K = 17$ is more than $10^5$, far more than the units of Example 8.1.1; with a single continuous covariate there are as many strata as units. Most strata then contain only treated or only control units, and the saturated stratification is infeasible. The rest of the chapter shows how the propensity score reduces the dimension of the problem from $K$ to one.

## 8.2. Balancing Scores and the Propensity Score

### 8.2.1. Balancing Scores

The idea is to stratify not on $X_i$ but on a lower-dimensional function of it that still makes the treated and control units comparable.

**Definition 8.2.1 (Balancing Score)** A **balancing score** is a function $b(x)$ of the covariates such that

$$
W_i \perp X_i \mid b(X_i).
$$
In words, among units with the same value of the balancing score, the distribution of the covariates is the same in the treatment and the control group.

The covariates themselves, $b(x) = x$, are a trivial balancing score, and so is any one-to-one function of them. The question is how coarse a balancing score can be.

**Theorem 8.2.1 (Balancing Property of the Propensity Score)** The propensity score is a balancing score: $W_i \perp X_i \mid e(X_i)$.

**Proof** Since $W_i$ is binary, it suffices to show that $\mathbb{P}(W_i = 1 \mid X_i, e(X_i))$ does not depend on $X_i$. Because $e(X_i)$ is a function of $X_i$, conditioning on both is the same as conditioning on $X_i$, so by the definition of the propensity score $\mathbb{P}(W_i = 1 \mid X_i, e(X_i)) = \mathbb{P}(W_i = 1 \mid X_i) = e(X_i)$. On the other hand, by the law of total expectation ([3.1.9](/3.1.9)),

$$
\mathbb{P}(W_i = 1 \mid e(X_i)) = \mathbb{E}[W_i \mid e(X_i)] = \mathbb{E}\bigl[\mathbb{E}[W_i \mid X_i, e(X_i)] \bigm| e(X_i)\bigr] = \mathbb{E}\bigl[e(X_i) \mid e(X_i)\bigr] = e(X_i).
$$
Hence $\mathbb{P}(W_i = 1 \mid X_i, e(X_i)) = \mathbb{P}(W_i = 1 \mid e(X_i))$, which is the conditional independence $W_i \perp X_i \mid e(X_i)$. $\square$

The proof uses nothing about the potential outcomes: the balancing property holds by the definition of the propensity score, whether or not assignment is unconfounded. It is a property of the joint distribution of $W_i$ and $X_i$ alone, and it can therefore be checked in the data, which is what [3.9.9](/3.9.9) does.

**Theorem 8.2.2 (The Propensity Score Is the Coarsest Balancing Score)** A function $b(x)$ is a balancing score if and only if the propensity score is a function of it, $e(x) = g(b(x))$ for some function $g$.

**Proof** If $e(x) = g(b(x))$, then by the argument of Theorem 8.2.1, $\mathbb{P}(W_i = 1 \mid b(X_i)) = \mathbb{E}[e(X_i) \mid b(X_i)] = g(b(X_i)) = e(X_i) = \mathbb{P}(W_i = 1 \mid X_i, b(X_i))$, so $b$ is a balancing score.

Conversely, suppose $b$ is a balancing score but $e$ is not a function of $b$. Then there are covariate values $x$ and $x'$ with $b(x) = b(x')$ but $e(x) \ne e(x')$. Among units with $b(X_i) = b(x)$,

$$
\mathbb{P}(W_i = 1 \mid X_i = x) = e(x) \ne e(x') = \mathbb{P}(W_i = 1 \mid X_i = x'),
$$
so the probability of treatment depends on $X_i$ given $b(X_i) = b(x)$, and $W_i$ and $X_i$ are not independent given $b(X_i)$. This contradicts the assumption that $b$ is a balancing score. $\square$

Every balancing score therefore carries at least the information in $e(x)$, and $e(x)$ itself is the coarsest one, a scalar however many covariates there are. This is the dimension reduction promised in §8.1.5.

### 8.2.2. Unconfoundedness Given a Balancing Score

Balance of the covariates is useful only because it transfers to the potential outcomes.

**Theorem 8.2.3 (Unconfoundedness Given a Balancing Score)** Suppose assignment is unconfounded, $W_i \perp (Y_i(0), Y_i(1)) \mid X_i$. Then assignment is unconfounded given any balancing score:

$$
W_i \perp \bigl(Y_i(0), Y_i(1)\bigr) \mid b(X_i).
$$
In particular, $W_i \perp (Y_i(0), Y_i(1)) \mid e(X_i)$.

**Proof** We show that $\mathbb{P}(W_i = 1 \mid Y_i(0), Y_i(1), b(X_i))$ does not depend on the potential outcomes. By the law of total expectation, conditioning in addition on $X_i$,

$$
\begin{aligned}
\mathbb{P}\bigl(W_i = 1 \mid Y_i(0), Y_i(1), b(X_i)\bigr) &= \mathbb{E}\Bigl[\mathbb{E}\bigl[W_i \mid Y_i(0), Y_i(1), X_i\bigr] \Bigm| Y_i(0), Y_i(1), b(X_i)\Bigr] \\
&= \mathbb{E}\Bigl[\mathbb{E}[W_i \mid X_i] \Bigm| Y_i(0), Y_i(1), b(X_i)\Bigr] \\
&= \mathbb{E}\Bigl[\mathbb{E}[W_i \mid b(X_i)] \Bigm| Y_i(0), Y_i(1), b(X_i)\Bigr] = \mathbb{E}[W_i \mid b(X_i)].
\end{aligned}
$$
The first step uses that $b(X_i)$ is a function of $X_i$; the second, unconfoundedness; the third, the balancing property, by which $\mathbb{E}[W_i \mid X_i] = \mathbb{E}[W_i \mid X_i, b(X_i)] = \mathbb{E}[W_i \mid b(X_i)]$; the last, that $\mathbb{E}[W_i \mid b(X_i)]$ is a function of $b(X_i)$. The result is $\mathbb{P}(W_i = 1 \mid b(X_i))$, free of the potential outcomes. $\square$

**Corollary 8.2.1 (Identification through the Propensity Score)** Under strong ignorability,

$$
\tau_{\mathrm{sp}} = \mathbb{E}\Bigl[\mathbb{E}\bigl[Y_i^{\mathrm{obs}} \mid W_i = 1, e(X_i)\bigr] - \mathbb{E}\bigl[Y_i^{\mathrm{obs}} \mid W_i = 0, e(X_i)\bigr]\Bigr].
$$

**Proof** By Theorem 8.2.3, $\mathbb{E}[Y_i^{\mathrm{obs}} \mid W_i = 1, e(X_i)] = \mathbb{E}[Y_i(1) \mid W_i = 1, e(X_i)] = \mathbb{E}[Y_i(1) \mid e(X_i)]$, and positivity guarantees that both conditional expectations are defined. The same holds for $W_i = 0$, and averaging $\mathbb{E}[Y_i(1) - Y_i(0) \mid e(X_i)]$ over the distribution of $e(X_i)$ gives $\tau_{\mathrm{sp}}$. $\square$

The corollary is the theoretical basis of stratification and matching on the propensity score: units with the same propensity score form, in effect, a completely randomized experiment, whatever their covariates. Comparing treated and control units with similar $e(X_i)$ removes all bias due to the observed covariates, without modeling how the outcomes depend on them. It does not remove bias due to unobserved covariates: Theorem 8.2.3 inherits unconfoundedness, it does not create it.

### 8.2.3. Propensity Score and Covariate Balance

Theorem 8.2.1 says that balance holds conditionally on the propensity score. The next theorem relates the marginal difference between the groups to the variation of the propensity score; it underlies the use of the propensity score as a summary measure of imbalance in [3.9.9](/3.9.9). Let $f_{\mathrm{t}}(x)$ and $f_{\mathrm{c}}(x)$ be the densities (or probability functions) of $X_i$ in the treated and control subpopulations, and $p = \mathbb{P}(W_i = 1) = \mathbb{E}[e(X_i)]$.

**Theorem 8.2.4 (Propensity Score and Covariate Balance)** Suppose the assignment mechanism is unconfounded and individualistic, and $0 < p < 1$. Then

$$
\mathbb{E}[e(X_i) \mid W_i = 1] - \mathbb{E}[e(X_i) \mid W_i = 0] = \frac{\operatorname{Var}(e(X_i))}{p(1 - p)},
$$
and

$$
\operatorname{Var}(e(X_i)) = \mathbb{E}\left[\left(\frac{f_{\mathrm{t}}(X_i) - f_{\mathrm{c}}(X_i)}{f_{\mathrm{t}}(X_i)\,p + f_{\mathrm{c}}(X_i)(1 - p)}\right)^2\right] p^2(1 - p)^2.
$$

**Proof** For the first identity, $\mathbb{E}[e(X_i)W_i] = \mathbb{E}[e(X_i)\,\mathbb{E}[W_i \mid X_i]] = \mathbb{E}[e(X_i)^2] = \operatorname{Var}(e(X_i)) + p^2$, so

$$
\mathbb{E}[e(X_i) \mid W_i = 1] = \frac{\mathbb{E}[e(X_i)W_i]}{p} = \frac{\operatorname{Var}(e(X_i))}{p} + p.
$$
Since $p = \mathbb{E}[e(X_i)] = p\,\mathbb{E}[e(X_i) \mid W_i = 1] + (1 - p)\,\mathbb{E}[e(X_i) \mid W_i = 0]$,

$$
\mathbb{E}[e(X_i) \mid W_i = 0] = \frac{p - p\,\mathbb{E}[e(X_i) \mid W_i = 1]}{1 - p} = p - \frac{\operatorname{Var}(e(X_i))}{1 - p},
$$
and the difference is $\operatorname{Var}(e(X_i))\bigl(\frac{1}{p} + \frac{1}{1 - p}\bigr) = \frac{\operatorname{Var}(e(X_i))}{p(1 - p)}$.

For the second, Bayes' theorem gives

$$
e(x) = \mathbb{P}(W_i = 1 \mid X_i = x) = \frac{f_{\mathrm{t}}(x)\,p}{f_{\mathrm{t}}(x)\,p + f_{\mathrm{c}}(x)(1 - p)}, \qquad e(x) - p = \frac{f_{\mathrm{t}}(x) - f_{\mathrm{c}}(x)}{f_{\mathrm{t}}(x)\,p + f_{\mathrm{c}}(x)(1 - p)}\,p(1 - p),
$$
and $\operatorname{Var}(e(X_i)) = \mathbb{E}[(e(X_i) - p)^2]$. $\square$

The theorem connects three statements. The difference in the mean propensity score between the groups is zero if and only if $\operatorname{Var}(e(X_i)) = 0$, that is, if the propensity score is constant; by the second identity this happens if and only if $f_{\mathrm{t}}(x) = f_{\mathrm{c}}(x)$ for (almost) all $x$, which is perfect balance of the whole covariate distribution. A difference in the means of a single number, the propensity score, therefore detects any difference between the two multivariate covariate distributions, and a small difference indicates that the distributions are close. In practice we use the linearized propensity score $\ell(x) = \log\frac{e(x)}{1 - e(x)}$, a monotone transformation that is closer to normally distributed; [3.9.9](/3.9.9) measures balance by its normalized difference between the groups.

## 8.3. An Overview of Estimation Strategies

Under strong ignorability the average effect is identified (Corollary 8.2.1), but there are many ways to estimate it. They fall into six groups, which differ in what they model: the outcomes, the assignment, or neither.

| Strategy | Models | Main idea | Weakness |
|---|---|---|---|
| 1. Model-based imputation | $\mathbb{P}(Y \mid W, X)$ | predict the missing potential outcomes from a model | sensitive to the model with many covariates |
| 2. Regression estimators | $\mathbb{E}[Y \mid W, X]$ | adjust by a linear regression | extrapolates when the groups differ |
| 3. Weighting | $\mathbb{P}(W \mid X)$ | weight by the inverse of the propensity score | unstable when $\hat e$ is near 0 or 1 |
| 4. Blocking (subclassification) | $\mathbb{P}(W \mid X)$ | analyze strata of similar $\hat e$ as CREs | residual bias within blocks |
| 5. Matching | a distance on $X$ | compare each unit with similar units of the other group | bias from inexact matches |
| 6. Mixed methods | both | combine 3–5 with regression adjustment | more choices to make |

### 8.3.1. Model-Based Imputation

As in [3.9.6](/3.9.6), we build a model for the missing potential outcomes and use it to impute them. The working model is a unit-level joint model $f(Y_i(0), Y_i(1) \mid X_i, \theta)$ with a prior on $\theta$; its justification is the [exchangeability](/3.7.6#def-6.3.1) of the units in the sense of **de Finetti's theorem** ([3.7.6](/3.7.6)), and unconfoundedness allows the assignment mechanism to be dropped from the likelihood, exactly as in a randomized experiment. With no or few covariates it is easy to specify a flexible model for the conditional distribution of the outcomes. With many covariates the specification is difficult, and when the covariate distributions of the two groups differ, the imputations for one group rely on the model far from the data of the other group, so the results can be sensitive to choices that the data cannot settle. In completely randomized experiments this sensitivity is minor because the two covariate distributions are similar by design. **Model-based imputation** is therefore not recommended as the primary method for general observational studies.

### 8.3.2. Regression Estimators

Suppose the potential outcomes follow separate linear models, $\mathbb{E}[Y_i(w) \mid X_i] = X_i\boldsymbol{\beta}_w$ for $w = 0, 1$, where $X_i$ now includes a constant. Estimate the two coefficient vectors by least squares within the groups,

$$
\hat{\boldsymbol{\beta}}_{\mathrm{c}} = \arg\min_{\boldsymbol{\beta}} \sum_{i:W_i = 0}(Y_i^{\mathrm{obs}} - X_i\boldsymbol{\beta})^2, \qquad \hat{\boldsymbol{\beta}}_{\mathrm{t}} = \arg\min_{\boldsymbol{\beta}} \sum_{i:W_i = 1}(Y_i^{\mathrm{obs}} - X_i\boldsymbol{\beta})^2,
$$
and impute each missing outcome by its prediction:

$$
\hat\tau^{\mathrm{ols}} = \frac{1}{N}\sum_{i=1}^{N}\Bigl(W_i\bigl(Y_i^{\mathrm{obs}} - X_i\hat{\boldsymbol{\beta}}_{\mathrm{c}}\bigr) + (1 - W_i)\bigl(X_i\hat{\boldsymbol{\beta}}_{\mathrm{t}} - Y_i^{\mathrm{obs}}\bigr)\Bigr) = \frac{N_{\mathrm{t}}}{N}\hat\tau_{\mathrm{t}}^{\mathrm{ols}} + \frac{N_{\mathrm{c}}}{N}\hat\tau_{\mathrm{c}}^{\mathrm{ols}}.
$$
Because a least squares fit with an intercept passes through the means, $\bar X_{\mathrm{t}}\hat{\boldsymbol{\beta}}_{\mathrm{t}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}}$ and $\bar X_{\mathrm{c}}\hat{\boldsymbol{\beta}}_{\mathrm{c}} = \bar Y_{\mathrm{c}}^{\mathrm{obs}}$, so the two components are

$$
\hat\tau_{\mathrm{t}}^{\mathrm{ols}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar X_{\mathrm{t}}\hat{\boldsymbol{\beta}}_{\mathrm{c}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} - (\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\hat{\boldsymbol{\beta}}_{\mathrm{c}}, \qquad \hat\tau_{\mathrm{c}}^{\mathrm{ols}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} - (\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\hat{\boldsymbol{\beta}}_{\mathrm{t}}.
$$

The regression adjusts the difference in means by the term $(\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\hat{\boldsymbol{\beta}}$. In a completely or pairwise randomized experiment $\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}}$ is close to zero, the adjustment is small, and its exact form matters little ([3.9.5](/3.9.5)). In an observational study the difference in covariate means can be large; the adjustment then predicts, for the treated units, control outcomes at covariate values where few control units exist, and the answer depends on the linear extrapolation rather than on data. Two specifications that fit the observed data equally well can give very different estimates. Regression is therefore not recommended without substantial modifications; it becomes valuable after the design phase has removed most of the imbalance, as a local adjustment within blocks or matched pairs ([3.9.10](/3.9.10)).

### 8.3.3. Weighting Estimators

Weighting models the assignment instead of the outcomes. The key identity is

$$
\mathbb{E}\left[\frac{W_iY_i^{\mathrm{obs}}}{e(X_i)}\right] = \mathbb{E}\left[\frac{\mathbb{E}[W_iY_i(1) \mid X_i]}{e(X_i)}\right] = \mathbb{E}\left[\frac{\mathbb{E}[W_i \mid X_i]\,\mathbb{E}[Y_i(1) \mid X_i]}{e(X_i)}\right] = \mathbb{E}\bigl[\mathbb{E}[Y_i(1) \mid X_i]\bigr] = \mathbb{E}[Y_i(1)],
$$
where the first step uses $W_iY_i^{\mathrm{obs}} = W_iY_i(1)$, the second unconfoundedness, and the third $\mathbb{E}[W_i \mid X_i] = e(X_i) > 0$. In the same way $\mathbb{E}[(1 - W_i)Y_i^{\mathrm{obs}}/(1 - e(X_i))] = \mathbb{E}[Y_i(0)]$. A treated unit with a small propensity score represents many units like it that were not treated, and is given a large weight.

**Definition 8.3.1 (Horvitz–Thompson Estimator)** With known propensity score, the **Horvitz–Thompson estimator** of the average treatment effect is

$$
\hat\tau^{\mathrm{ht}} = \frac{1}{N}\sum_{i=1}^{N}\frac{W_iY_i^{\mathrm{obs}}}{e(X_i)} - \frac{1}{N}\sum_{i=1}^{N}\frac{(1 - W_i)Y_i^{\mathrm{obs}}}{1 - e(X_i)} = \frac{1}{N}\sum_{i:W_i = 1}\lambda_iY_i^{\mathrm{obs}} - \frac{1}{N}\sum_{i:W_i = 0}\lambda_iY_i^{\mathrm{obs}},
$$
with weights $\lambda_i = 1/\bigl(e(X_i)^{W_i}(1 - e(X_i))^{1 - W_i}\bigr)$, that is, $1/e(X_i)$ for treated and $1/(1 - e(X_i))$ for control units. Estimating causal effects by weighting each unit with the inverse of the probability of the treatment it received is called **inverse probability weighting** (IPW).

The name comes from survey sampling, where Horvitz and Thompson (1952) weighted sampled units by the inverse of their inclusion probabilities. By the identity above, $\hat\tau^{\mathrm{ht}}$ is an **unbiased estimator** of $\tau_{\mathrm{sp}}$ whenever the weights are known functions of the covariates. In observational studies $e(x)$ must be replaced by an estimate $\hat e(x)$, and the weights are usually normalized to average one within each group,

$$
\hat\lambda_i = \begin{cases} N_{\mathrm{t}}\,\hat e(X_i)^{-1} \Big/ \sum_{j:W_j = 1}\hat e(X_j)^{-1}, & W_i = 1, \\ N_{\mathrm{c}}\,(1 - \hat e(X_i))^{-1} \Big/ \sum_{j:W_j = 0}(1 - \hat e(X_j))^{-1}, & W_i = 0, \end{cases}
$$
and $\hat\tau$ is computed with $\frac{1}{N_{\mathrm{t}}}\sum_{W_i = 1}\hat\lambda_iY_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{W_i = 0}\hat\lambda_iY_i^{\mathrm{obs}}$; the normalization makes the estimator invariant to adding a constant to all outcomes. The weakness of weighting is its dependence on the estimated propensity score near the boundary: when $\hat e(X_i)$ is close to zero for a treated unit or close to one for a control unit, a single unit receives a huge weight, and minor changes in the specification of the propensity score model change the estimate substantially.

### 8.3.4. Blocking on the Propensity Score

Blocking (subclassification) partitions the sample into $J$ blocks by the estimated propensity score, with boundaries $0 = b_0 < b_1 < \dots < b_J = 1$ and block indicators

$$
B_i(j) = \boldsymbol{1}\{b_{j-1} \le \hat e(X_i) < b_j\}, \qquad j = 1, \dots, J.
$$
Within a block the units have similar propensity scores, so by Corollary 8.2.1 the data of a block look approximately like data from a completely randomized experiment, and the block-level effects can be estimated by differences in means and combined as in a stratified randomized experiment. Blocking is more robust than weighting to units with extreme estimated propensity scores, because the score only determines the block membership, not the size of a weight. Within blocks some imbalance remains, and blocking becomes a recommended method once it is combined with regression adjustment within the blocks ([3.9.10](/3.9.10)).

### 8.3.5. Matching

Matching finds, for each unit, one or more units of the opposite treatment group with similar covariates, and compares their outcomes directly. If exact matches exist, this is the most transparent of all strategies: each comparison is between units that are identical in all observed respects. With several covariates exact matches are rare, and one has to decide which deviations from an exact match are acceptable, which requires a distance on the covariate space.

**Example 8.3.1 (Choosing a Match)** In an evaluation of a job training program, the target unit is a treated woman, and two potential controls are available, none of them exact:

| | Age | Children under 6 | Education | Months worked in the past 12 | Training |
|---|---|---|---|---|---|
| Target unit | 30 | 2 | high school | 4 | yes |
| Exact match (hypothetical) | 30 | 2 | high school | 4 | no |
| Match I | 34 | 2 | high school | 6 | no |
| Match II | 28 | 1 | high school | 2 | no |

Match I differs by four years of age and two months of work experience, match II by two years, one child and two months. Which is better depends on how strongly each covariate is related to the outcome (earnings) and to the decision to train, and a distance such as the **Mahalanobis distance** ([3.4.1](/3.4.1)) or the difference in estimated propensity scores makes the trade-off explicit. [3.9.9](/3.9.9) defines these distances and the matching algorithms.

### 8.3.6. Mixed Methods; Design and Analysis

Mixed methods combine weighting, blocking or matching with regression: the first step removes most of the imbalance, and a regression within blocks or matched pairs removes the residual bias without extrapolating far. These are the methods recommended in practice.

Two distinctions organize the six strategies. The first is what is modeled. Imputation and regression model the outcomes $\mathbb{P}(Y \mid \cdot)$; weighting, blocking and matching model the assignment $\mathbb{P}(W \mid \cdot)$ or only use the covariates, and their aim is to balance the covariates. The second is when the outcomes are used. Estimating the propensity score, blocking, matching and assessing balance use only $(W_i, X_i)$; they can and should be completed before the outcomes are seen, just as an experiment is designed before it is run. This separation of design and analysis protects against choosing, consciously or not, the specification that gives the desired answer. The design phase is the subject of [3.9.9](/3.9.9), the analysis phase of [3.9.10](/3.9.10). Almost all of the procedures involve the propensity score, which is why its estimation, the last section of this chapter, is the first step of every analysis.

## 8.4. Estimating the Propensity Score

### 8.4.1. Known and Unknown Propensity Scores

In randomized experiments the propensity score is known: $e(x) = N_{\mathrm{t}}/N$ for all $x$ in a completely randomized experiment, $e(x) = N_{\mathrm{t}}(j)/N(j)$ for $x$ in stratum $j$ of a stratified randomized experiment, and $e(x) = 1/2$ in a paired randomized experiment. In other settings it is rarely known. The typical situation is that, given the available pre-treatment variables, the researcher considers unconfoundedness a reasonable approximation to the actual assignment mechanism, but has only vague prior information about how the propensity score depends on the covariates. In medicine, for example, treatment decisions are based on clinically relevant patient characteristics that the doctors observe and enter in the medical records, but there is no explicit rule that requires a specific treatment for particular values of these characteristics.

If $X_i$ takes only a few values, the estimation is straightforward: partition the sample into subsamples that are homogeneous in the covariates and estimate the propensity score in each by the proportion of treated units. If $X_i$ takes many values, most cells contain a single unit, this saturated estimate is useless, and some form of smoothing, a parametric model or a flexible nonparametric one, is essential.

### 8.4.2. What Accuracy Is Needed

How much the accuracy of $\hat e(x)$ matters depends on the method that uses it. Weighting by the inverse of the estimated propensity score relies on an accurate approximation of the true score: it can in principle remove all biases from differences in the covariate distributions, but small errors in estimated scores near zero or one inflate the variance of the weights. Blocking on the estimated propensity score, followed by regression adjustment within the blocks, is much less sensitive: the score only serves to group units with similar true propensity scores, and the regression removes remaining differences.

More importantly, the goal is not to estimate the propensity score as well as possible in terms of mean squared error or any other measure of the distance between $\hat e$ and $e$. The goal is to obtain a score that balances the covariates in the sample: within subsamples with similar values of the estimated propensity score, the covariate distributions of the treated and control units should be similar. For this purpose the estimated score is often preferable to the true one.

**Example 8.4.1 (The Estimated Score Can Balance Better than the True One)** In a completely randomized experiment with a single binary covariate (say, sex), the true propensity score is $e(x) = N_{\mathrm{t}}/N$ for both values of $x$, and stratifying on it puts all units in one stratum. By chance the proportion of women will differ somewhat between the treated and the control group, so the stratum is not balanced in the sample. The estimated propensity score $\hat e(x) = N_{\mathrm{t}}(x)/N(x)$ takes two values, one for each sex, and stratifying on it gives two strata, women and men, each perfectly balanced on the covariate.

:::

Three further remarks describe the spirit of the estimation. First, the outcome data are not used at any point, so the specification of the propensity score cannot be tuned, deliberately or not, to produce a particular estimate of the treatment effect. Second, a fully automatic procedure is hard to give: the specification can be much improved by knowledge of which covariates drive the treatment decision and which are related to the outcome. Third, the propensity score model is a tool for balancing, not a model of behavior: we are not interested in a structural or causal interpretation of its coefficients, and collinearity or uninterpretable terms do no harm as long as balance improves.

### 8.4.3. Logistic Regression for the Propensity Score

The standard model is a **logistic regression** ([3.4.12](/3.4.12)) of $W_i$ on functions of the covariates,

$$
\mathbb{P}(W_i = 1 \mid X_i = x; \boldsymbol{\phi}) = \frac{\exp(h(x)\boldsymbol{\phi})}{1 + \exp(h(x)\boldsymbol{\phi})},
$$
where $h(x)$ is a row vector of functions of $x$ that includes a constant, linear terms and selected quadratic and interaction terms; the simplest choice is $h(x) = (1, x)$. The likelihood is

$$
\mathcal{L}(\boldsymbol{\phi} \mid \boldsymbol{W}, \boldsymbol{X}) = \prod_{i=1}^{N}e(X_i; \boldsymbol{\phi})^{W_i}\bigl(1 - e(X_i; \boldsymbol{\phi})\bigr)^{1 - W_i} = \prod_{i=1}^{N}\frac{\exp(W_i\,h(X_i)\boldsymbol{\phi})}{1 + \exp(h(X_i)\boldsymbol{\phi})},
$$
with log-likelihood

$$
L(\boldsymbol{\phi}) = \sum_{i=1}^{N}\Bigl(W_i\,h(X_i)\boldsymbol{\phi} - \log\bigl(1 + \exp(h(X_i)\boldsymbol{\phi})\bigr)\Bigr).
$$
Its gradient and Hessian are

$$
\frac{\partial L}{\partial\boldsymbol{\phi}} = \sum_{i=1}^{N}h(X_i)^{\mathsf T}\bigl(W_i - e(X_i; \boldsymbol{\phi})\bigr), \qquad \frac{\partial^2 L}{\partial\boldsymbol{\phi}\,\partial\boldsymbol{\phi}^{\mathsf T}} = -\sum_{i=1}^{N}e(X_i; \boldsymbol{\phi})\bigl(1 - e(X_i; \boldsymbol{\phi})\bigr)h(X_i)^{\mathsf T}h(X_i).
$$
The Hessian is negative semidefinite for every $\boldsymbol{\phi}$, so $L$ is concave, and it is strictly concave when $\sum_i h(X_i)^{\mathsf T}h(X_i)$ is positive definite. The maximum likelihood estimate $\hat{\boldsymbol{\phi}}$ is then unique if it exists, and **Newton's method** ([3.5.4](/3.5.4)) finds it.

**Algorithm 8.4.1 (Newton–Raphson for the Propensity Score)** Start from $\boldsymbol{\phi}^{(0)} = (\log(N_{\mathrm{t}}/N_{\mathrm{c}}), 0, \dots, 0)^{\mathsf T}$, the model with the constant only, fitted exactly. Iterate

$$
\boldsymbol{\phi}^{(k+1)} = \boldsymbol{\phi}^{(k)} - \left(\frac{\partial^2 L}{\partial\boldsymbol{\phi}\,\partial\boldsymbol{\phi}^{\mathsf T}}(\boldsymbol{\phi}^{(k)})\right)^{-1}\frac{\partial L}{\partial\boldsymbol{\phi}}(\boldsymbol{\phi}^{(k)})
$$
until the change is negligible. The estimated covariance matrix of $\hat{\boldsymbol{\phi}}$ is the inverse of the negative Hessian at $\hat{\boldsymbol{\phi}}$.

:::

The estimate does not exist (some coefficients diverge) when a linear combination of the terms in $h(x)$ separates the treated from the control units perfectly. This is not only a numerical nuisance: it means that some region of the covariate space contains units of one group only, so that positivity fails in the sample. Example 8.4.2 shows a case.

### 8.4.4. Selecting Covariates and Interactions

With many covariates, a model with all linear, quadratic and interaction terms has more parameters than the data can support, and a model with only linear terms may balance poorly. A stepwise procedure based on the **likelihood ratio test** ([3.2.5](/3.2.5)) chooses the specification.

**Algorithm 8.4.2 (Three-Step Specification of the Propensity Score)** Let $K$ be the number of covariates.

1. Select a set of $K_{\mathrm{B}}$ basic covariates on a priori grounds: covariates that are viewed as important for explaining the assignment, or as plausibly or strongly related to the outcomes. They are always included, whatever the data say.
2. Add linear terms. Among the $K - K_{\mathrm{B}}$ covariates not yet included, fit each in turn as an additional linear term and compute the likelihood ratio statistic of the model with it against the model without it. If the largest statistic exceeds a threshold $C_{\mathrm{L}}$, add that covariate and repeat; otherwise stop. Let $K_{\mathrm{L}}$ be the number of linear terms at the end.
3. Add second-order terms. Among the $K_{\mathrm{L}}(K_{\mathrm{L}} + 1)/2$ squares and pairwise interactions of the $K_{\mathrm{L}}$ selected covariates, add terms one at a time in the same forward manner, with a threshold $C_{\mathrm{Q}}$, until no remaining term has a likelihood ratio statistic above it.

:::

The thresholds are tuning constants. Values such as $C_{\mathrm{L}} = 1$ and $C_{\mathrm{Q}} = 2.71$ (the upper $0.10$ quantile of $\chi^2_1$) are common choices; the low threshold for linear terms reflects the view that omitting a relevant covariate is worse than including an irrelevant one. The procedure is forward selection, a greedy search: it is not meant to find the true model, only an adequate specification, and its adequacy is judged by the balance it achieves ([3.9.9](/3.9.9)). If balance is unsatisfactory, the specification is revised, for example by adding terms for the covariates that remain unbalanced, still without looking at the outcomes.

**Example 8.4.2 (The Propensity Score for the Barbiturate Data)** For the data of Example 8.1.1, three basic covariates are selected on substantive grounds: the child's sex, the mother's age (on the log scale) and the mother's socioeconomic status. Sex and the mother's age are likely to be associated with the outcomes, the mother's age and socioeconomic status with barbiturate exposure. In step 2, with $C_{\mathrm{L}} = 1$, the first covariate added (recorded as `lpbc420` in the data) has a likelihood ratio statistic of $1308$: a single covariate dominates the assignment. The second has a statistic of $66.1$, and after it the statistics drop quickly; the procedure adds ten covariates in total, the last with a statistic of $1.3$, and leaves four out, so the final model has 13 linear terms. Step 3 adds 17 quadratic and interaction terms. One interaction between two indicator covariates has an estimated coefficient of $-\infty$: one of the four cells they define contains no exposed children, so its estimated propensity score is zero, and those units have no comparable treated units at all. They will be removed by trimming in [3.9.9](/3.9.9).

:::

The figure shows a simulated version of the situation the estimated score reveals. The treated and control units are far apart on the propensity score scale, with many control units whose score is near zero and few treated units in that region; the linearized score spreads out the extremes and shows the overlap more clearly.

![Simulated observational data with three covariates and a propensity score estimated by logistic regression (fitted by Newton–Raphson, Algorithm 8.4.1): histograms of the estimated propensity score and of the linearized propensity score in the treatment and control groups. Many control units have scores near zero, where hardly any treated units are found; overlap is good only in the middle range. Simulated data](./plots/ps_overlap.py)

## Summary

- **Regular assignment mechanism** (individualistic, probabilistic, unconfounded with unknown $e(x)$): the observational analogue of a stratified randomized experiment with unknown, covariate-defined strata. In the super-population it is strong ignorability, $W_i \perp (Y_i(0), Y_i(1)) \mid X_i$ and $0 < e(x) < 1$.
- Unconfoundedness involves the missing potential outcomes and cannot be tested (Remark 8.1.1); it is hidden in the exogeneity assumption of every causal regression. Saturated stratification on $X_i$ fails with many or continuous covariates.
- Balancing scores and the propensity score:

  | Result | Statement | Needs unconfoundedness? |
  |---|---|---|
  | Theorem 8.2.1 | $W_i \perp X_i \mid e(X_i)$ | no |
  | Theorem 8.2.2 | $b$ is balancing iff $e = g(b)$; $e$ is the coarsest | no |
  | Theorem 8.2.3 | $W_i \perp (Y_i(0), Y_i(1)) \mid b(X_i)$ | yes |
  | Corollary 8.2.1 | $\tau_{\mathrm{sp}} = \mathbb{E}[\mathbb{E}[Y^{\mathrm{obs}} \mid W = 1, e] - \mathbb{E}[Y^{\mathrm{obs}} \mid W = 0, e]]$ | yes, and positivity |
  | Theorem 8.2.4 | $\mathbb{E}[e \mid W = 1] - \mathbb{E}[e \mid W = 0] = \operatorname{Var}(e)/(p(1 - p))$, zero iff $f_{\mathrm{t}} = f_{\mathrm{c}}$ | — |

- Six strategies (§8.3): imputation and regression model the outcomes and extrapolate when the groups differ; the Horvitz–Thompson (IPW) estimator weights by $1/e$ and $1/(1 - e)$ and is unbiased with the true score but unstable near 0 and 1; blocking and matching balance the covariates; mixed methods add regression within blocks or pairs. Design (using only $W$ and $X$) precedes analysis.
- Estimating $e(x)$: the aim is balance, not accuracy (Example 8.4.1); logistic regression with a concave log-likelihood fitted by Newton–Raphson (Algorithm 8.4.1); basic covariates, then forward selection of linear terms ($C_{\mathrm{L}}$) and second-order terms ($C_{\mathrm{Q}}$) by likelihood ratio statistics (Algorithm 8.4.2); outcomes are never used.

## Questions

1. Show that the identity $\mathbb{E}[W_iY_i^{\mathrm{obs}}/e(X_i)] = \mathbb{E}[Y_i(1)]$ can fail without unconfoundedness. Construct an example with no covariates in which treated units have systematically larger $Y_i(1)$.

   **Answer** Without covariates $e = p$ is constant, and $\mathbb{E}[W_iY_i(1)]/p = \mathbb{E}[Y_i(1) \mid W_i = 1]$. Let $Y_i(1) \in \{0, 1\}$ with $\mathbb{P}(Y_i(1) = 1) = 1/2$, and let units with $Y_i(1) = 1$ be treated with probability $0.8$, the others with probability $0.2$. Then $p = 0.5$ and $\mathbb{E}[Y_i(1) \mid W_i = 1] = 0.4/0.5 = 0.8 \ne 0.5 = \mathbb{E}[Y_i(1)]$. The step $\mathbb{E}[W_iY_i(1) \mid X_i] = \mathbb{E}[W_i \mid X_i]\,\mathbb{E}[Y_i(1) \mid X_i]$ requires $W_i \perp Y_i(1) \mid X_i$.
2. Prove directly, without Theorem 8.2.2, that $b(x) = (e(x), x_1)$, the propensity score together with the first covariate, is a balancing score. Is $b(x) = x_1$ a balancing score in general?

   **Answer** $\mathbb{P}(W_i = 1 \mid b(X_i)) = \mathbb{E}[e(X_i) \mid e(X_i), X_{i1}] = e(X_i)$, which equals $\mathbb{P}(W_i = 1 \mid X_i)$, so $W_i \perp X_i \mid b(X_i)$. In general $x_1$ alone is not: it is balancing only if $e(x)$ depends on $x$ through $x_1$ only, by Theorem 8.2.2.
3. A study has one covariate $X_i \in \{0, 1, 2\}$ with $\mathbb{P}(X_i = x) = 1/3$ and $e(x) = 0.2, 0.5, 0.8$. Compute $p$, $\operatorname{Var}(e(X_i))$, $\mathbb{E}[e(X_i) \mid W_i = 1]$ and $\mathbb{E}[e(X_i) \mid W_i = 0]$, and verify the first identity of Theorem 8.2.4.

   **Answer** $p = 0.5$; $\operatorname{Var}(e) = \frac{1}{3}(0.09 + 0 + 0.09) = 0.06$. $\mathbb{E}[e \mid W = 1] = \mathbb{E}[\mathrm{e}^2]/p = \frac{1}{3}(0.04 + 0.25 + 0.64)/0.5 = 0.62$, and $\mathbb{E}[e \mid W = 0] = \mathbb{E}[e(1 - e)]/(1 - p) = \frac{1}{3}(0.16 + 0.25 + 0.16)/0.5 = 0.38$. The difference $0.24$ equals $0.06/(0.5 \times 0.5) = 0.24$.
4. Show that the Horvitz–Thompson estimator with the true propensity score is not invariant to adding a constant $c$ to all outcomes, while the normalized version is. Why does this matter in finite samples?

   **Answer** Adding $c$ changes $\hat\tau^{\mathrm{ht}}$ by $c\bigl(\frac{1}{N}\sum_i W_i/e(X_i) - \frac{1}{N}\sum_i(1 - W_i)/(1 - e(X_i))\bigr)$, which has expectation zero but is nonzero in a given sample. With normalized weights, $\frac{1}{N_{\mathrm{t}}}\sum_{W_i = 1}\hat\lambda_i = \frac{1}{N_{\mathrm{c}}}\sum_{W_i = 0}\hat\lambda_i = 1$, so $c$ cancels. An estimate that depends on the arbitrary origin of the outcome scale has an avoidable variance component, which is large when some weights are large.
5. In Example 8.4.1, suppose $N = 20$, $N_{\mathrm{t}} = 10$, and there are 6 women among the treated and 4 among the controls. Compare the covariate balance obtained by stratifying on the true and on the estimated propensity score.

   **Answer** The true score is $1/2$ for everyone, so there is one stratum, with a proportion of women of $0.6$ among the treated and $0.4$ among the controls, a clear imbalance. The estimated score is $6/10 = 0.6$ for women and $4/10 = 0.4$ for men; stratifying on it gives a stratum of 10 women (6 treated, 4 control) and one of 10 men (4 treated, 6 control), each perfectly balanced on sex.
6. Derive the gradient and Hessian of the logistic log-likelihood $L(\boldsymbol{\phi})$, and show that the Newton–Raphson update is a weighted least squares fit.

   **Answer** With $\eta_i = h(X_i)\boldsymbol{\phi}$ and $e_i = \mathrm{e}^{\eta_i}/(1 + \mathrm{e}^{\eta_i})$, $\partial\log(1 + \mathrm{e}^{\eta_i})/\partial\boldsymbol{\phi} = e_ih(X_i)^{\mathsf T}$, so the gradient is $H^{\mathsf T}(\boldsymbol{W} - \boldsymbol{e})$ with $H$ the matrix of rows $h(X_i)$, and since $\partial e_i/\partial\eta_i = e_i(1 - e_i)$ the Hessian is $-H^{\mathsf T}DH$ with $D = \operatorname{diag}(e_i(1 - e_i))$. The update is $\boldsymbol{\phi}^{(k+1)} = \boldsymbol{\phi}^{(k)} + (H^{\mathsf T}DH)^{-1}H^{\mathsf T}(\boldsymbol{W} - \boldsymbol{e}) = (H^{\mathsf T}DH)^{-1}H^{\mathsf T}D\boldsymbol{z}$ with working response $z_i = \eta_i + (W_i - e_i)/(e_i(1 - e_i))$: weighted least squares of $\boldsymbol{z}$ on $H$ with weights $e_i(1 - e_i)$, which is iteratively reweighted least squares.
7. Explain why the outcome must not be used when selecting the covariates of the propensity score model, and why a covariate that predicts the outcome strongly but the assignment only weakly should still be included.

   **Answer** If outcomes were used, the analyst could (even unintentionally) try specifications until the estimated effect looked right, and the reported uncertainty would ignore this search; keeping the design blind to outcomes, as in an experiment, rules this out. A covariate strongly related to the outcome causes bias even if its imbalance is small, because the bias is roughly the imbalance times the effect of the covariate on the outcome; balancing it is cheap in variance and can remove a large bias. That is why such covariates are among the basic covariates of step 1.
8. A colleague argues that, because the propensity score is a balancing score, matching on $\hat e(X_i)$ makes the treated and control units comparable in all respects, observed and unobserved. What is wrong with this claim?

   **Answer** Theorem 8.2.1 concerns the observed covariates $X_i$ only: units with the same propensity score have the same distribution of $X_i$ across the groups. Unobserved variables that affect both treatment and outcome are not balanced unless they are functions of $X_i$ or independent of the assignment given $X_i$, which is exactly the untestable unconfoundedness assumption. Theorem 8.2.3 transfers unconfoundedness from $X_i$ to $e(X_i)$; it does not create it.
