---
title: Noncompliance and Instrumental Variables
description: Randomized experiments in which units do not take the assigned treatment, and the instrumental variable method. Unobserved confounding and noncompliance, encouragement designs; intention-to-treat, as-treated and per-protocol analyses on a worked example; the econometric instrumental variable model, covariance ratio, Wald estimator and two-stage least squares; the potential outcomes formulation with compliance types, the exclusion restriction, one-sided noncompliance and the complier average causal effect with the vitamin A data; two-sided noncompliance, monotonicity and the local average treatment effect theorem; the five assumptions; the connection with econometrics, natural experiments and the 2021 Nobel prize; Balke–Pearl bounds for the population average effect.
---

The methods of [3.9.8](/3.9.8)–[3.9.10](/3.9.10) rest on unconfoundedness: all variables that affect both the treatment and the outcome are observed. When an important confounder $U$ is not observed, adjustment for the observed covariates does not remove the bias, and in the language of causal graphs ([3.9.12](/3.9.12)) neither the backdoor nor the front-door criterion applies. This chapter shows that something can still be learned if there is a variable that affects the treatment, is itself as good as randomly assigned, and affects the outcome only through the treatment: an instrumental variable. The leading example is a randomized experiment with noncompliance, where the random assignment is the instrument and the treatment actually received is chosen by the units. The chapter connects three traditions: the Rubin framework, in which noncompliance is a non-regular assignment mechanism ([3.9.2](/3.9.2)); Pearl's causal graphs, which show the structure of the problem; and econometrics, where instrumental variables were developed for linear simultaneous equations. Their synthesis, by Angrist, Imbens and Rubin (1996), shows what the instrumental variable estimand means without constant effects: the average effect for the subpopulation of compliers.

Notation: as in the rest of the Rubin framework, $Z_i$ is the assignment, $W_i$ the treatment received and $Y_i$ the outcome. Pearl's graphs in [3.9.11](/3.9.11)–[3.9.13](/3.9.13) call the treatment $X$, and econometric texts usually write the treatment received as $D_i$; here it is always $W_i$.

## 14.1. The Problem

### 14.1.1. Unobserved Confounding

In the first panel of the figure below, $U$ affects both the treatment $W$ and the outcome $Y$. If $U$ were observed, adjusting for it would identify the effect of $W$ on $Y$; since it is not, the association between $W$ and $Y$ mixes the causal effect with the effect of $U$, and no adjustment for observed variables can separate them. Suppose, however, that a variable $Z$ affects $W$, is independent of $U$, and has no path to $Y$ other than through $W$ (second panel). Then the variation in $W$ caused by $Z$ is free of confounding, and its effect on $Y$ can be traced. If $Z$ also affects $Y$ directly (third panel), this argument breaks down.

![Three causal graphs: an unobserved confounder U of the treatment W and the outcome Y; a randomized instrument Z that affects Y only through W; and a violation of the exclusion restriction, with a direct effect of Z on Y](./plots/iv_dag.py)

### 14.1.2. Noncompliance in Randomized Experiments

**Example 14.1.1 (Vitamin A Supplements)** Sommer and Zeger (1991) analyzed a randomized experiment in Indonesia on the effect of vitamin A supplements on infant mortality. The supplements were randomly assigned to villages, but some of the individuals in villages assigned to the treatment did not receive them, while none of the individuals in control villages received them.

:::

Often we cannot force subjects to take a treatment: patients skip pills, participants assigned to a training program do not attend. The units who refrain from taking the treatment may differ in unobserved characteristics, health or motivation, from those who take it, and these characteristics may affect the outcome. The assignment is randomized, but the receipt of treatment is not.

**Definition 14.1.1 (Noncompliance)** In a randomized experiment with **noncompliance**, the treatment actually received, $W_i$, differs for some units from the assigned treatment $Z_i$. An **encouragement design** randomizes the encouragement to receive the treatment (an invitation, a voucher, a reminder) rather than the receipt of the treatment itself, so that noncompliance is built into the design.

Two designs should be distinguished. In an encouragement design the encouragement may affect the outcome through other channels than the treatment (being invited to a program may itself motivate). In a double-blind experiment with noncompliance, neither the subjects nor the staff know the assignment, and the assignment can affect the outcome only through the treatment actually received. This chapter focuses on the second situation, where the graph of the second panel is credible. Either way, the receipt of treatment depends on the assignment and possibly on the potential outcomes, so the assignment mechanism for $W$ is not regular, and the methods of [3.9.8](/3.9.8)–[3.9.10](/3.9.10) do not apply.

## 14.2. Three Naive Analyses

Three simple comparisons are in common use. With the assignment $Z_i$, the receipt $W_i$ and the observed outcome $Y_i^{\mathrm{obs}}$,

**Definition 14.2.1 (Naive Analyses of Experiments with Noncompliance)** The intention-to-treat analysis compares units by assignment, $\tau^{\mathrm{itt}} = \mathbb{E}[Y_i^{\mathrm{obs}} \mid Z_i = 1] - \mathbb{E}[Y_i^{\mathrm{obs}} \mid Z_i = 0]$. The **as-treated analysis** compares units by the treatment received, $\tau^{\mathrm{at}} = \mathbb{E}[Y_i^{\mathrm{obs}} \mid W_i = 1] - \mathbb{E}[Y_i^{\mathrm{obs}} \mid W_i = 0]$. The **per-protocol analysis** compares only the units who complied with their assignment, $\tau^{\mathrm{pp}} = \mathbb{E}[Y_i^{\mathrm{obs}} \mid W_i = Z_i = 1] - \mathbb{E}[Y_i^{\mathrm{obs}} \mid W_i = Z_i = 0]$.

The **intention-to-treat analysis** ([7.7.18](/7.7.18)) is the standard primary analysis of clinical trials: it is justified by randomization alone, but it estimates the effect of being assigned to the treatment, not of taking it. The other two compare groups formed after randomization.

**Example 14.2.1 (A Virtual Experiment)** A new drug for lung cancer is tested in a randomized experiment with ten patients. The assignment $Z$ is random, but patients may take the new drug ($W = 1$) or the old one ($W = 0$) regardless of their assignment. The outcome is the lifetime $Y$ in years; the new drug extends every patient's life by exactly 3 years, and the assignment affects the outcome only through the drug taken. The complete data, including the unobservable potential treatments and outcomes, are:

| Unit | $Z$ | $W(0)$ | $W(1)$ | $W$ | $Y(W = 0)$ | $Y(W = 1)$ | $Y^{\mathrm{obs}}$ | Type |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 1 | 5 | 8 | 8 | complier |
| 2 | 1 | 1 | 1 | 1 | 4 | 7 | 7 | always-taker |
| 3 | 1 | 1 | 1 | 1 | 3 | 6 | 6 | always-taker |
| 4 | 1 | 0 | 0 | 0 | 2 | 5 | 2 | never-taker |
| 5 | 1 | 0 | 0 | 0 | 1 | 4 | 1 | never-taker |
| 6 | 0 | 1 | 1 | 1 | 5 | 8 | 8 | always-taker |
| 7 | 0 | 0 | 1 | 0 | 4 | 7 | 4 | complier |
| 8 | 0 | 0 | 0 | 0 | 3 | 6 | 3 | never-taker |
| 9 | 0 | 0 | 1 | 0 | 2 | 5 | 2 | complier |
| 10 | 0 | 0 | 1 | 0 | 1 | 4 | 1 | complier |

The three analyses give:

- intention to treat: $\frac{8 + 7 + 6 + 2 + 1}{5} - \frac{8 + 4 + 3 + 2 + 1}{5} = 4.8 - 3.6 = 1.2$;
- as treated: the four units with $W = 1$ (units 1, 2, 3, 6) against the six with $W = 0$, $\frac{29}{4} - \frac{13}{6} = 7.25 - 2.17 = 5.08$;
- per protocol: units 1, 2, 3 ($Z = W = 1$) against units 7–10 ($Z = W = 0$), $7 - 2.5 = 4.5$.

None of them equals the true effect $3$. The intention-to-treat effect is diluted, because only some of the assigned units take the drug and some control units take it anyway. The as-treated and per-protocol comparisons are biased, because the units who take the drug are healthier (the always-takers, units 2, 3 and 6, have high outcomes under either drug), so the groups formed by $W$ are not comparable.

:::

The per-protocol analysis seems to respect the randomization, since it compares units within their assigned arms. Its flaw is that the compliance types defined in §14.4 are distributed differently among the selected units. Among those assigned to treatment who took it ($Z = W = 1$) are the compliers and the always-takers; among those assigned to control who did not take it ($Z = W = 0$) are the compliers and the never-takers. The comparison therefore contrasts always-takers with never-takers, two groups that differ in their potential outcomes, in addition to the effect of the treatment on compliers. Randomization balances the types between the arms, but selecting on the treatment received destroys this balance.

## 14.3. The Econometric Instrumental Variable Model

### 14.3.1. The Linear Model

In econometrics the problem is posed with a linear model. With all variables centered (so there are no intercepts),

$$
W = \rho Z + \delta U + \varepsilon_W, \qquad Y = \beta W + \gamma U + \varepsilon_Y,
$$
where $U$ is unobserved and the errors are independent of everything else. The coefficient $\beta$ is the effect of $W$ on $Y$. A regression of $Y$ on $W$ estimates $\beta + \gamma\operatorname{Cov}(W, U)/\operatorname{Var}(W)$, which is biased unless $\gamma = 0$ or $\delta = 0$. The variable $Z$ is called an instrument if

$$
Z \perp U, \qquad Z \not\perp W, \qquad Z \perp Y \mid (W, U),
$$
that is, it is independent of the confounder, it is related to the treatment ($\rho \ne 0$), and it is excluded from the outcome equation.

**Theorem 14.3.1 (Identification in the Linear Instrumental Variable Model)** Under the linear model and the three conditions,

$$
\beta = \frac{\operatorname{Cov}(Z, Y)}{\operatorname{Cov}(Z, W)}.
$$

**Proof** From the outcome equation, $\operatorname{Cov}(Z, Y) = \beta\operatorname{Cov}(Z, W) + \gamma\operatorname{Cov}(Z, U) + \operatorname{Cov}(Z, \varepsilon_Y) = \beta\operatorname{Cov}(Z, W)$, because $Z$ is independent of $U$ and of $\varepsilon_Y$. Since $\operatorname{Cov}(Z, W) = \rho\operatorname{Var}(Z) \ne 0$, we can divide. $\square$

The sample version, $\hat\beta = \widehat{\operatorname{Cov}}(Z, Y)/\widehat{\operatorname{Cov}}(Z, W)$, is the instrumental variable estimator. Two special forms are standard.

### 14.3.2. The Wald Estimator and Two-Stage Least Squares

If $Z$ is binary, taking conditional expectations of the outcome equation given $Z = 1$ and $Z = 0$ and subtracting gives

$$
\mathbb{E}[Y \mid Z = 1] - \mathbb{E}[Y \mid Z = 0] = \beta\bigl(\mathbb{E}[W \mid Z = 1] - \mathbb{E}[W \mid Z = 0]\bigr) + \gamma\bigl(\mathbb{E}[U \mid Z = 1] - \mathbb{E}[U \mid Z = 0]\bigr),
$$
and the last term vanishes because $Z \perp U$.

**Definition 14.3.1 (Wald Estimator)** For a binary instrument the **Wald estimator** is

$$
\hat\beta^{\mathrm{wald}} = \frac{\bar Y_1 - \bar Y_0}{\bar W_1 - \bar W_0},
$$
where $\bar Y_z$ and $\bar W_z$ are the averages of the outcome and the treatment among units with $Z_i = z$: the effect of the instrument on the outcome divided by its effect on the treatment.

In Example 14.2.1 the instrument's effect on the outcome is $1.2$ (the intention-to-treat effect) and its effect on the treatment is $\frac{3}{5} - \frac{1}{5} = 0.4$, so $\hat\beta^{\mathrm{wald}} = 1.2/0.4 = 3$, the true effect.

**Definition 14.3.2 (Two-Stage Least Squares)** Let $\boldsymbol{D} = [\boldsymbol{1}\ \ \boldsymbol{W}]$ be the matrix of the regressors of the outcome equation $\boldsymbol{Y} = \boldsymbol{D}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ and $\boldsymbol{Z} = [\boldsymbol{1}\ \ \boldsymbol{Z}]$ the matrix of the instruments, and $P_{\boldsymbol{Z}} = \boldsymbol{Z}(\boldsymbol{Z}^{\mathsf T}\boldsymbol{Z})^{-1}\boldsymbol{Z}^{\mathsf T}$. The **two-stage least squares** (2SLS) estimator is

$$
\hat{\boldsymbol{\beta}}^{\mathrm{2sls}} = \bigl(\boldsymbol{D}^{\mathsf T}P_{\boldsymbol{Z}}\boldsymbol{D}\bigr)^{-1}\boldsymbol{D}^{\mathsf T}P_{\boldsymbol{Z}}\boldsymbol{Y} = \bigl(\boldsymbol{D}^{\mathsf T}\boldsymbol{Z}(\boldsymbol{Z}^{\mathsf T}\boldsymbol{Z})^{-1}\boldsymbol{Z}^{\mathsf T}\boldsymbol{D}\bigr)^{-1}\boldsymbol{D}^{\mathsf T}\boldsymbol{Z}(\boldsymbol{Z}^{\mathsf T}\boldsymbol{Z})^{-1}\boldsymbol{Z}^{\mathsf T}\boldsymbol{Y}.
$$

The name describes a computation with two **least squares** fits ([3.3.7](/3.3.7)). In the first stage, regress the treatment on the instruments and form the fitted values $\hat{\boldsymbol{D}} = P_{\boldsymbol{Z}}\boldsymbol{D}$; they contain only the part of the variation in the treatment that is due to the instrument. In the second stage, regress $\boldsymbol{Y}$ on $\hat{\boldsymbol{D}}$: since $P_{\boldsymbol{Z}}$ is symmetric and idempotent, $(\hat{\boldsymbol{D}}^{\mathsf T}\hat{\boldsymbol{D}})^{-1}\hat{\boldsymbol{D}}^{\mathsf T}\boldsymbol{Y}$ equals the formula above. When there are as many instruments as regressors, $\boldsymbol{Z}^{\mathsf T}\boldsymbol{D}$ is square and the formula simplifies to $(\boldsymbol{Z}^{\mathsf T}\boldsymbol{D})^{-1}\boldsymbol{Z}^{\mathsf T}\boldsymbol{Y}$; with a single binary instrument this is the Wald estimator, and with a single continuous one the covariance ratio. The estimator is a **consistent estimator** of $\boldsymbol{\beta}$ if $\mathbb{E}[Z_i\varepsilon_i] = 0$ and the instruments are relevant; under homoskedasticity its variance is estimated by $\hat\sigma^2(\boldsymbol{D}^{\mathsf T}P_{\boldsymbol{Z}}\boldsymbol{D})^{-1}$, with $\hat\sigma^2$ computed from the residuals $\boldsymbol{Y} - \boldsymbol{D}\hat{\boldsymbol{\beta}}^{\mathrm{2sls}}$ (not from the residuals of the second-stage regression, which use $\hat{\boldsymbol{D}}$).

### 14.3.3. What the Linear Model Assumes

The linear model implies that the unit-level effect of $W$ on $Y$ is the same constant $\beta$ for everyone. In Example 14.2.1 this was true by construction. In most applications effects differ between units, and the units whose treatment is changed by the instrument may not be typical. Two questions arise: can the constant-effect assumption be relaxed, and if so, what does the instrumental variable estimand mean? The potential outcomes framework answers both.

## 14.4. Noncompliance in the Potential Outcomes Framework

### 14.4.1. Setup and Assumptions

Consider a completely randomized experiment with noncompliance. The assignment $Z_i \in \{0, 1\}$ is randomized and is of secondary interest; the receipt of treatment, of primary interest, is a potential outcome of the assignment, $W_i(z) \in \{0, 1\}$, with $W_i^{\mathrm{obs}} = W_i(Z_i)$. Since both the assignment and the receipt could in principle affect the outcome, each unit has four potential outcomes $Y_i(z, w)$, $z, w \in \{0, 1\}$, of which $Y_i^{\mathrm{obs}} = Y_i(Z_i, W_i(Z_i))$ is observed. We assume **SUTVA** ([3.9.1](/3.9.1)) for both $Z$ and $W$: no hidden versions of the treatments, and no effect of one unit's assignment on another unit's receipt or outcome.

**Definition 14.4.1 (Unconfounded Assignment of the Instrument)** The assignment is unconfounded if

$$
Z_i \perp \bigl(W_i(0), W_i(1), Y_i(0, 0), Y_i(0, 1), Y_i(1, 0), Y_i(1, 1)\bigr).
$$

In a randomized experiment this holds by design. It concerns $Z$ only: the receipt $W_i$ is not unconfounded, because it depends on the unit's characteristics.

**Definition 14.4.2 (Exclusion Restriction for Noncompliance)** The **exclusion restriction** holds if the assignment affects the outcome only through the treatment received:

$$
Y_i(0, w) = Y_i(1, w) \quad \text{for all units } i \text{ and } w \in \{0, 1\}.
$$
We then write $Y_i(w)$ for the common value, and each unit has only two potential outcomes.

The exclusion restriction says that the estimated effect is due to the receipt of the drug, not to the assignment to receive it. It is the key assumption underlying the interpretation of all randomized experiments with or without noncompliance, it is not implied by the randomization of the assignment, and it can be made plausible by design features such as double blinding. In an encouragement design it is a substantive assumption, which fails if, for example, the encouragement itself changes behavior.

### 14.4.2. Compliance Types

**Definition 14.4.3 (Compliance Types)** The **compliance type** $G_i$ of unit $i$ is determined by the pair of potential treatments $(W_i(0), W_i(1))$:

| $W_i(0)$ | $W_i(1)$ | Type $G_i$ |
|---|---|---|
| 0 | 0 | never-taker (nt) |
| 0 | 1 | complier (co) |
| 1 | 0 | defier (df) |
| 1 | 1 | always-taker (at) |

A **never-taker** does not take the treatment whatever the assignment, a **complier** takes it exactly when assigned to it, a **defier** does the opposite of the assignment, and an **always-taker** takes it whatever the assignment. Let $\pi_g = \mathbb{P}(G_i = g)$.

The compliance type is a latent characteristic of the unit: it is a function of the two potential treatments, of which only one is observed, so it is not known for any unit without further assumptions. It does not depend on the assignment, and by the unconfoundedness of $Z$ its distribution is the same in both arms; it can therefore be treated like a pre-treatment covariate that we cannot observe. Under the exclusion restriction the treatment received cannot affect the outcome of never-takers and always-takers in any comparison between arms, because their treatment does not change with $Z$.

### 14.4.3. Intention-to-Treat Effects

**Definition 14.4.4 (Intention-to-Treat Effects)** The **intention-to-treat effects** are the effects of the assignment on the receipt of treatment and on the outcome,

$$
\mathrm{ITT}_W = \mathbb{E}\bigl[W_i(1) - W_i(0)\bigr], \qquad \mathrm{ITT}_Y = \mathbb{E}\bigl[Y_i(1, W_i(1)) - Y_i(0, W_i(0))\bigr],
$$
and within a compliance type $g$, $\mathrm{ITT}_{W,g} = \mathbb{E}[W_i(1) - W_i(0) \mid G_i = g]$ and $\mathrm{ITT}_{Y,g} = \mathbb{E}[Y_i(1, W_i(1)) - Y_i(0, W_i(0)) \mid G_i = g]$.

Both are average causal effects of the randomized assignment, so by the unconfoundedness of $Z$ they are identified, $\mathrm{ITT}_W = \mathbb{E}[W_i^{\mathrm{obs}} \mid Z_i = 1] - \mathbb{E}[W_i^{\mathrm{obs}} \mid Z_i = 0]$ and similarly for $Y$, and estimated by the **difference-in-means estimator** of [3.9.4](/3.9.4) with its Neyman variance. By the law of total expectation $\mathrm{ITT}_Y = \sum_g\pi_g\mathrm{ITT}_{Y,g}$ and $\mathrm{ITT}_W = \sum_g\pi_g\mathrm{ITT}_{W,g}$, with $\mathrm{ITT}_{W,\mathrm{co}} = 1$, $\mathrm{ITT}_{W,\mathrm{df}} = -1$ and $\mathrm{ITT}_{W,\mathrm{nt}} = \mathrm{ITT}_{W,\mathrm{at}} = 0$.

### 14.4.4. One-Sided Noncompliance

**Definition 14.4.5 (One-Sided Noncompliance)** Noncompliance is **one-sided** if units assigned to control cannot receive the treatment: $W_i(0) = 0$ for all units.

This is the situation of Example 14.1.1, where the supplements were not available in control villages. Then there are no always-takers and no defiers, only compliers and never-takers. The type is observed for units assigned to treatment ($W_i = 1$ means complier, $W_i = 0$ never-taker) and unknown for units assigned to control.

**Definition 14.4.6 (Complier Average Causal Effect)** The **complier average causal effect** is the average effect of the treatment received among compliers,

$$
\tau_{\mathrm{CACE}} = \mathbb{E}\bigl[Y_i(1) - Y_i(0) \mid G_i = \mathrm{co}\bigr].
$$
It is also called the local average treatment effect (LATE).

**Theorem 14.4.1 (CACE under One-Sided Noncompliance)** Under SUTVA, unconfounded assignment of $Z$, the exclusion restriction, one-sided noncompliance and $\pi_{\mathrm{co}} > 0$,

$$
\mathrm{ITT}_W = \pi_{\mathrm{co}}, \qquad \mathrm{ITT}_Y = \pi_{\mathrm{co}}\,\tau_{\mathrm{CACE}}, \qquad \tau_{\mathrm{CACE}} = \frac{\mathrm{ITT}_Y}{\mathrm{ITT}_W}.
$$

**Proof** With one-sided noncompliance only never-takers and compliers exist, so $\mathrm{ITT}_W = \pi_{\mathrm{nt}} \cdot 0 + \pi_{\mathrm{co}} \cdot 1 = \pi_{\mathrm{co}}$. For a never-taker $W_i(0) = W_i(1) = 0$, so the unit-level effect of the assignment on the outcome is $Y_i(1, 0) - Y_i(0, 0)$, which is zero by the exclusion restriction; hence $\mathrm{ITT}_{Y,\mathrm{nt}} = 0$. For a complier, $Y_i(1, W_i(1)) - Y_i(0, W_i(0)) = Y_i(1, 1) - Y_i(0, 0) = Y_i(1) - Y_i(0)$, so $\mathrm{ITT}_{Y,\mathrm{co}} = \tau_{\mathrm{CACE}}$. Therefore $\mathrm{ITT}_Y = \pi_{\mathrm{nt}} \cdot 0 + \pi_{\mathrm{co}}\tau_{\mathrm{CACE}}$, and dividing by $\mathrm{ITT}_W = \pi_{\mathrm{co}} > 0$ gives the ratio. $\square$

The intention-to-treat effect on the outcome is the complier effect diluted by the share of compliers, and the ratio undoes the dilution. The proof also shows what the data cannot give: the effect for never-takers, who never take the treatment in the experiment, is not identified, and $\tau_{\mathrm{CACE}}$ is in general not the population average effect.

To estimate the complier effect, replace the two intention-to-treat effects by their difference-in-means estimates, $\hat\tau_{\mathrm{CACE}} = \widehat{\mathrm{ITT}}_Y/\widehat{\mathrm{ITT}}_W$, the Wald estimator. Its variance follows from the **Delta method** ([3.1.14](/3.1.14)) applied to $g(a, b) = a/b$:

$$
\widehat{\operatorname{Var}}(\hat\tau_{\mathrm{CACE}}) \approx \frac{\widehat{\operatorname{Var}}(\widehat{\mathrm{ITT}}_Y)}{\widehat{\mathrm{ITT}}_W^2} + \frac{\widehat{\mathrm{ITT}}_Y^2\,\widehat{\operatorname{Var}}(\widehat{\mathrm{ITT}}_W)}{\widehat{\mathrm{ITT}}_W^4} - \frac{2\,\widehat{\mathrm{ITT}}_Y\,\widehat{\operatorname{Cov}}(\widehat{\mathrm{ITT}}_Y, \widehat{\mathrm{ITT}}_W)}{\widehat{\mathrm{ITT}}_W^3}.
$$
Under one-sided noncompliance $W_i = 0$ for every unit assigned to control, so $\widehat{\mathrm{ITT}}_W$ is the proportion treated in the treatment arm, its variance comes from that arm only, and the covariance is the sample covariance of $Y_i^{\mathrm{obs}}$ and $W_i$ in the treatment arm divided by its size.

**Example 14.4.1 (The Vitamin A Data)** The data of Example 14.1.1 comprise $N = 23{,}682$ children; $Y_i = 1$ means survival to the end of the study:

| Assignment $Z_i$ | Received $W_i$ | Survived $Y_i$ | Number of units | Compliance type |
|---|---|---|---|---|
| 0 | 0 | 0 | 74 | complier or never-taker |
| 0 | 0 | 1 | 11,514 | complier or never-taker |
| 1 | 0 | 0 | 34 | never-taker |
| 1 | 0 | 1 | 2,385 | never-taker |
| 1 | 1 | 0 | 12 | complier |
| 1 | 1 | 1 | 9,663 | complier |

In the control arm (11,588 children) the survival rate is $0.99361$; in the treatment arm (12,094 children) it is $(2385 + 9663)/12094 = 0.99620$, and the proportion who received the supplement is $9675/12094 = 0.79998$. Hence

$$
\widehat{\mathrm{ITT}}_Y = 0.00258 \ (\text{s.e. } 0.00093), \qquad \widehat{\mathrm{ITT}}_W = 0.8000 \ (\text{s.e. } 0.0036), \qquad \hat\tau_{\mathrm{CACE}} = \frac{0.00258}{0.8000} = 0.00323 \ (\text{s.e. } 0.00116).
$$
Among compliers the supplement raises the survival rate by about 3.2 per thousand, an approximate 95% interval of $(0.0010, 0.0055)$. We can even recover the two survival rates of the compliers. Never-takers survive at rate $2385/2419 = 0.98594$ in the treatment arm, and by randomization at the same rate in the control arm, where they make up $\hat\pi_{\mathrm{nt}} = 0.200$ of the children; solving $0.99361 = 0.200 \times 0.98594 + 0.800\,\bar Y_{\mathrm{co}}(0)$ gives $\bar Y_{\mathrm{co}}(0) = 0.99553$, against $\bar Y_{\mathrm{co}}(1) = 9663/9675 = 0.99876$. The never-takers have clearly lower survival than the compliers: they are the children who are harder to reach, and their outcomes would be worse even without the supplement. This is why the naive analyses are biased: the as-treated difference is $0.0065$ and the per-protocol difference $0.0051$, both larger than the complier effect, because they compare the healthier compliers who took the supplement with a control group that includes the never-takers.

:::

## 14.5. Two-Sided Noncompliance

### 14.5.1. Monotonicity

One-sided noncompliance is a special case. In many studies units in both arms can deviate. Angrist (1990) studied the effect of military service on the later civilian earnings of white men born around 1950, using the Vietnam-era draft lottery as the instrument: $Z_i = 1$ if the man's randomly drawn lottery number made him eligible for the draft, $W_i = 1$ if he served. Some eligible men did not serve (never-takers, for example for health reasons), and some ineligible men volunteered (always-takers). All four compliance types are possible, and both $W_i(0) = 1$ and $W_i(1) = 0$ occur.

With all four types, the decomposition of the proof of Theorem 14.4.1 becomes, under the exclusion restriction ($\mathrm{ITT}_{Y,\mathrm{nt}} = \mathrm{ITT}_{Y,\mathrm{at}} = 0$) and with $\tau_g = \mathbb{E}[Y_i(1) - Y_i(0) \mid G_i = g]$,

$$
\mathrm{ITT}_Y = \pi_{\mathrm{co}}\tau_{\mathrm{co}} - \pi_{\mathrm{df}}\tau_{\mathrm{df}}, \qquad \mathrm{ITT}_W = \pi_{\mathrm{co}} - \pi_{\mathrm{df}},
$$
because a defier receives the treatment when assigned to control, so the effect of the assignment on his outcome is $Y_i(0) - Y_i(1)$. The minus sign means that the effects for compliers and defiers can cancel: a treatment that helps everyone could show no intention-to-treat effect at all. An additional assumption is needed.

**Definition 14.5.1 (Monotonicity)** The **monotonicity assumption** holds if $W_i(1) \ge W_i(0)$ for all units: there are no defiers, $\pi_{\mathrm{df}} = 0$.

Monotonicity says that the assignment never discourages anyone from taking the treatment. It is plausible in most designs: a draft-eligible number does not make anyone less likely to serve, an invitation to a program does not make anyone less likely to attend. One-sided noncompliance satisfies it automatically. In Example 14.2.1 it holds: units 1, 7, 9 and 10 are compliers, units 2, 3 and 6 always-takers, units 4, 5 and 8 never-takers, and no unit has $W(0) = 1$, $W(1) = 0$.

### 14.5.2. The Local Average Treatment Effect

**Theorem 14.5.1 (Local Average Treatment Effect)** (Imbens and Angrist 1994; Angrist, Imbens and Rubin 1996) Under SUTVA, unconfounded assignment of $Z$, the exclusion restriction, monotonicity, and $\mathrm{ITT}_W \ne 0$,

$$
\tau_{\mathrm{CACE}} = \mathbb{E}\bigl[Y_i(1) - Y_i(0) \mid G_i = \mathrm{co}\bigr] = \frac{\mathrm{ITT}_Y}{\mathrm{ITT}_W} = \frac{\mathbb{E}[Y_i^{\mathrm{obs}} \mid Z_i = 1] - \mathbb{E}[Y_i^{\mathrm{obs}} \mid Z_i = 0]}{\mathbb{E}[W_i^{\mathrm{obs}} \mid Z_i = 1] - \mathbb{E}[W_i^{\mathrm{obs}} \mid Z_i = 0]}.
$$

**Proof** By unconfoundedness of $Z$, the numerator and denominator of the last expression are $\mathrm{ITT}_Y$ and $\mathrm{ITT}_W$. Decompose both by compliance type. For never-takers and always-takers, $W_i(0) = W_i(1)$, so $\mathrm{ITT}_{W,g} = 0$, and by the exclusion restriction $Y_i(1, W_i(1)) = Y_i(0, W_i(0))$, so $\mathrm{ITT}_{Y,g} = 0$. Defiers do not exist by monotonicity. For compliers, $\mathrm{ITT}_{W,\mathrm{co}} = 1$ and $\mathrm{ITT}_{Y,\mathrm{co}} = \mathbb{E}[Y_i(1) - Y_i(0) \mid G_i = \mathrm{co}]$. Hence $\mathrm{ITT}_W = \pi_{\mathrm{co}}$, which is nonzero by assumption, and $\mathrm{ITT}_Y = \pi_{\mathrm{co}}\tau_{\mathrm{CACE}}$. $\square$

Monotonicity extends the one-sided result to two-sided noncompliance. In Example 14.2.1 the Wald estimate $3$ is the complier effect, and it coincides with the population effect only because the effect is $3$ for every unit. The theorem is the answer to the question of §14.3.3: the constant-effect assumption is not needed, but without it the instrumental variable estimand is the average effect for compliers, not for the population. Under monotonicity some types can be read off the data: units with $Z_i = 1, W_i = 0$ are never-takers and units with $Z_i = 0, W_i = 1$ always-takers, while those with $Z_i = W_i = 1$ are compliers or always-takers and those with $Z_i = W_i = 0$ compliers or never-takers. The proportions are identified, $\pi_{\mathrm{at}} = \mathbb{P}(W_i = 1 \mid Z_i = 0)$, $\pi_{\mathrm{nt}} = \mathbb{P}(W_i = 0 \mid Z_i = 1)$ and $\pi_{\mathrm{co}} = 1 - \pi_{\mathrm{at}} - \pi_{\mathrm{nt}}$, as are the mean potential outcomes of compliers under both treatments, by the same mixture argument as in Example 14.4.1.

The figure shows the four analyses in simulated experiments with heterogeneous effects (never-takers $0.5$, compliers $1$, always-takers $4$) and an unobserved health variable that drives both compliance and the outcome.

![Sampling distributions over 500 simulated randomized experiments with two-sided noncompliance, no defiers and an unobserved variable affecting compliance and the outcome: the as-treated, per-protocol and intention-to-treat analyses and the Wald (CACE) estimator, with the true complier effect and the population average effect. Simulated data](./plots/iv_simulation.py)

The as-treated and per-protocol estimates are far above both targets, because the healthy always-takers dominate the treated groups. The intention-to-treat estimate is diluted. The Wald estimator is centered on the complier effect, with the largest spread, the price of dividing by $\widehat{\mathrm{ITT}}_W$; it does not estimate the population average effect, which is larger here because the always-takers benefit most.

### 14.5.3. The Five Assumptions

The identification of the intention-to-treat effects needs only two assumptions: SUTVA and unconfounded assignment of $Z$. Interpreting their ratio as the complier effect needs three more (Angrist, Imbens and Rubin 1996).

**Definition 14.5.2 (Instrumental Variable)** A variable $Z$ is an **instrumental variable** for the effect of $W$ on $Y$ if it satisfies:

1. SUTVA for $Z$ and $W$;
2. unconfoundedness: $Z_i \perp (W_i(0), W_i(1), Y_i(z, w)_{z,w \in \{0,1\}})$;
3. the exclusion restriction: $Y_i(0, w) = Y_i(1, w)$, so that never-takers and always-takers have zero intention-to-treat effect;
4. monotonicity: no defiers;
5. relevance (a nonzero first stage): $\mathrm{ITT}_W = \mathbb{E}[W_i \mid Z_i = 1] - \mathbb{E}[W_i \mid Z_i = 0] \ne 0$.

Only the relevance condition can be checked directly in the data, by estimating $\mathrm{ITT}_W$; an estimate close to zero signals a weak instrument, for which the Wald ratio is unstable and its normal approximation poor. Unconfoundedness holds by design when $Z$ is randomized and is an assumption otherwise; the exclusion restriction and monotonicity involve unobservable potential outcomes and are justified by the design and by substantive knowledge, although they have some testable implications (for example, the identified potential outcome distributions of compliers must be nonnegative). In graphical terms, conditions 2 and 3 are the second panel of the first figure: no common cause of $Z$ and $Y$, and no arrow from $Z$ to $Y$ other than through $W$.

## 14.6. Connections with Econometrics

### 14.6.1. Two Frameworks

The traditional econometric framework considers a general setting with several endogenous regressors $D_i = (D_{i1}, \dots, D_{iJ})$ and several instruments $Z_i = (Z_{i1}, \dots, Z_{iL})$ in a linear model $\boldsymbol{Y} = \boldsymbol{D}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ with $\mathbb{E}[\varepsilon_i] = 0$. The regressors may be endogenous, $D_i \not\perp \varepsilon_i$, but the instruments must be exogenous and excluded from the model, $Z_i \perp \varepsilon_i$. Identification requires at least as many instruments as endogenous regressors, and exogenous covariates can be added by including them in both stages of 2SLS.

| | Traditional econometric framework | Potential outcomes framework |
|---|---|---|
| Treatments and instruments | multiple, not necessarily binary | usually one binary of each |
| Covariates | easily included in both stages | require extensions |
| Effects | constant, by the linear model | heterogeneous |
| Estimand | the coefficient $\beta$ | the complier average causal effect |
| Assumptions | exogeneity and exclusion of $Z$ in the error term | SUTVA, unconfoundedness, exclusion, monotonicity, relevance, stated in terms of potential outcomes |

The traditional framework appears more versatile, but this comes at two costs: the linear model inherently makes a constant-effect assumption, and it obscures the fact that the effect is identified only for the particular subpopulation that complies with the assignment. The potential outcomes formulation makes the assumptions explicit and the estimand interpretable; 2SLS remains the computational tool, and with a binary instrument and treatment it estimates the complier effect.

### 14.6.2. Natural Experiments and the 2021 Nobel Prize

In observational economics an instrument is rarely randomized by a researcher. The instrument comes from a natural experiment.

**Definition 14.6.1 (Natural Experiment)** A **natural experiment** is an event, occurring naturally or through institutional rules or policy changes, that assigns some units to different levels of a treatment of interest in a way that is plausibly unrelated to their potential outcomes, so that it can be analyzed like a randomized experiment, often as an instrument for the treatment.

Examples are the draft lottery, the quarter of birth, which through school entry and compulsory schooling laws affects years of education (Angrist and Krueger 1991), natural disasters and wars, and policy changes that affect some regions but not their neighbors. **Mendelian randomization** ([7.4.25](/7.4.25)) uses genetic variants, which are allocated at conception independently of most environmental confounders, as instruments for modifiable exposures in epidemiology; its assumptions are the five above, with pleiotropy as the main threat to the exclusion restriction.

The 2021 Nobel Memorial Prize in Economic Sciences recognized this line of work. One half went to David Card for his empirical contributions to labor economics, the other half jointly to Joshua Angrist and Guido Imbens for their methodological contributions to the analysis of causal relationships. Card used natural experiments to study central questions of labor economics. In the best-known example, Card and Krueger (1994) compared fast-food restaurants in New Jersey, which raised its minimum wage in 1992, with restaurants in neighboring Pennsylvania, which did not, and found no evidence that the increase reduced employment in New Jersey ([3.9.10](/3.9.10) uses these data to illustrate matching). This is an empirical finding about a particular moderate increase, which changed the received view that minimum wages necessarily reduce employment; it is not a general proposition that raising the minimum wage never reduces employment, and the size of such effects remains an active research question. Angrist and Imbens recast the instrumental variable method in the potential outcomes framework and showed precisely what can be learned from natural experiments with heterogeneous effects: the local average treatment effect of Theorem 14.5.1.

## 14.7. The Whole Population: Balke–Pearl Bounds

The complier effect is identified, but what if we care about the average effect in the whole population? Without monotonicity and without assumptions on the effects of never-takers and always-takers, the population effect is not identified, but the data still restrict it. Balke and Pearl (1997) formulated the problem with the graph of the second panel and discrete variables. With $Z$, $W$, $Y$ binary and $U$ unrestricted, the model implies

$$
\mathbb{P}(y, w, z, u) = \mathbb{P}(y \mid w, u)\,\mathbb{P}(w \mid z, u)\,\mathbb{P}(z)\,\mathbb{P}(u), \qquad \mathbb{P}(y, w \mid z) = \sum_u\mathbb{P}(y \mid w, u)\,\mathbb{P}(w \mid z, u)\,\mathbb{P}(u),
$$
and the interventional distribution is $\mathbb{P}(y \mid \operatorname{do}(W = w)) = \sum_u\mathbb{P}(y \mid w, u)\mathbb{P}(u)$. Every unit is characterized by its response types, the functions $z \mapsto W$ (four types: never-taker, complier, defier, always-taker) and $w \mapsto Y$ (four types), so $U$ can be replaced by a distribution over $16$ joint types. The observed probabilities $\mathbb{P}(y, w \mid z)$ are linear in the type probabilities, and so is

$$
\mathrm{ACE}(W \to Y) = \mathbb{P}\bigl(Y = 1 \mid \operatorname{do}(W = 1)\bigr) - \mathbb{P}\bigl(Y = 1 \mid \operatorname{do}(W = 0)\bigr).
$$

**Definition 14.7.1 (Balke–Pearl Bounds)** The **Balke–Pearl bounds** are the minimum and maximum of $\mathrm{ACE}(W \to Y)$, or of $\mathbb{P}(Y = 1 \mid \operatorname{do}(W = w))$, over all distributions of the response types that reproduce the observed $\mathbb{P}(y, w \mid z)$, computed by linear programming.

The solution has a closed form. Writing $p_{yw.z} = \mathbb{P}(Y = y, W = w \mid Z = z)$,

$$
\max\left\{\begin{matrix} p_{10.1} \\ p_{10.0} \\ p_{10.0} + p_{11.0} - p_{00.1} - p_{11.1} \\ p_{01.0} + p_{10.0} - p_{00.1} - p_{01.1} \end{matrix}\right\} \le \mathbb{P}\bigl(Y = 1 \mid \operatorname{do}(W = 0)\bigr) \le \min\left\{\begin{matrix} 1 - p_{00.1} \\ 1 - p_{00.0} \\ p_{01.0} + p_{10.0} + p_{10.1} + p_{11.1} \\ p_{10.0} + p_{11.0} + p_{01.1} + p_{10.1} \end{matrix}\right\},
$$
similar expressions bound $\mathbb{P}(Y = 1 \mid \operatorname{do}(W = 1))$, and the bounds on the ACE are given by eight-term maxima and minima of the same kind. The bounds are sharp: every value between them is compatible with the data and the model.

**Example 14.7.1 (Bounds for the Vitamin A Data)** For the data of Example 14.4.1, with $Y = 1$ for survival, the linear program gives

$$
-0.1946 \le \mathrm{ACE}(W \to Y) \le 0.0054.
$$
The interval contains the complier effect $0.0032$ but is wide, mostly on the negative side. The width reflects the 20% of never-takers: nothing in the data tells us how they would have fared with the supplement, and any value between their surviving for sure and their dying for sure is compatible with the observations.

:::

The bounds show the general trade-off of this chapter. Without assumptions beyond randomization and exclusion, the population effect is only partially identified; adding monotonicity identifies the effect for compliers exactly; identifying the population effect requires assumptions about the noncompliers, such as constant effects, that the data cannot check.

## Summary

- Unobserved confounding defeats adjustment; a randomized assignment with noncompliance, or a natural experiment, can serve as an **instrumental variable**.
- Naive analyses of Example 14.2.1 (true effect 3): intention to treat $1.2$ (diluted), as treated $5.08$, per protocol $4.5$ (biased by selection on the treatment received); IV (Wald) $1.2/0.4 = 3$.
- Econometric IV: $\beta = \operatorname{Cov}(Z, Y)/\operatorname{Cov}(Z, W)$ under $Z \perp U$, $Z \not\perp W$, exclusion (Theorem 14.3.1); Wald estimator for binary $Z$; 2SLS $\hat{\boldsymbol\beta} = (\boldsymbol{D}^{\mathsf T}P_{\boldsymbol{Z}}\boldsymbol{D})^{-1}\boldsymbol{D}^{\mathsf T}P_{\boldsymbol{Z}}\boldsymbol{Y}$; assumes constant effects.
- Potential outcomes: $Z_i$, $W_i(z)$, $Y_i(z, w)$; compliance types:

  | Type | $(W(0), W(1))$ | $\mathrm{ITT}_{W,g}$ | $\mathrm{ITT}_{Y,g}$ under exclusion |
  |---|---|---|---|
  | never-taker | $(0, 0)$ | 0 | 0 |
  | complier | $(0, 1)$ | 1 | $\tau_{\mathrm{co}}$ |
  | defier | $(1, 0)$ | $-1$ | $-\tau_{\mathrm{df}}$ |
  | always-taker | $(1, 1)$ | 0 | 0 |

- $\mathrm{ITT}_Y = \pi_{\mathrm{co}}\tau_{\mathrm{co}} - \pi_{\mathrm{df}}\tau_{\mathrm{df}}$, $\mathrm{ITT}_W = \pi_{\mathrm{co}} - \pi_{\mathrm{df}}$; with one-sided noncompliance (Theorem 14.4.1) or monotonicity (Theorem 14.5.1), $\tau_{\mathrm{CACE}} = \mathrm{ITT}_Y/\mathrm{ITT}_W$, with Delta method standard errors. Vitamin A: $\hat\tau_{\mathrm{CACE}} = 0.0032$ (s.e. $0.0012$).
- Five assumptions: SUTVA, unconfoundedness of $Z$, exclusion restriction, monotonicity, relevance; only relevance is directly testable.
- Without monotonicity or for the whole population: Balke–Pearl bounds by linear programming (vitamin A: $[-0.195, 0.005]$).

## Questions

1. In Example 14.2.1, compute $\pi_{\mathrm{nt}}$, $\pi_{\mathrm{co}}$, $\pi_{\mathrm{at}}$ from the observed data alone, assuming monotonicity, and compare with the true values. Why do they differ?

   **Answer** $\hat\pi_{\mathrm{at}} = \mathbb{P}(W = 1 \mid Z = 0) = 1/5 = 0.2$, $\hat\pi_{\mathrm{nt}} = \mathbb{P}(W = 0 \mid Z = 1) = 2/5 = 0.4$, so $\hat\pi_{\mathrm{co}} = 0.4$. The true proportions in the ten units are $0.3$, $0.4$, $0.3$. The estimates use each arm as a sample of five units, and by chance the treatment arm contains two of the three never-takers and the control arm only one of the three always-takers; in expectation over the randomization the estimates are unbiased.
2. Show that the per-protocol estimand equals $\tau_{\mathrm{co}}$ plus a bias term under one-sided noncompliance, and express the bias in terms of the never-takers' and compliers' control outcomes.

   **Answer** Under one-sided noncompliance, $Z = W = 1$ selects the compliers in the treatment arm, with mean $\mathbb{E}[Y(1) \mid \mathrm{co}]$, and $Z = W = 0$ is the whole control arm, with mean $\pi_{\mathrm{co}}\mathbb{E}[Y(0) \mid \mathrm{co}] + \pi_{\mathrm{nt}}\mathbb{E}[Y(0) \mid \mathrm{nt}]$. The difference is $\tau_{\mathrm{co}} + \pi_{\mathrm{nt}}(\mathbb{E}[Y(0) \mid \mathrm{co}] - \mathbb{E}[Y(0) \mid \mathrm{nt}])$. In the vitamin A data the compliers' control survival ($0.9955$) exceeds the never-takers' ($0.9859$), so the bias is $0.2 \times 0.0096 \approx 0.0019$, and $0.0032 + 0.0019 = 0.0051$, the per-protocol estimate.
3. A trial of an exercise program uses an encouragement design: 1000 people receive an invitation and a voucher ($Z = 1$), 1000 do not. In the invited group 400 attend, in the other group 100 attend anyway. Mean weight loss is $2.0$ kg in the invited group and $0.8$ kg in the other. Estimate the complier effect, and discuss which assumption is most doubtful.

   **Answer** $\widehat{\mathrm{ITT}}_W = 0.4 - 0.1 = 0.3$, $\widehat{\mathrm{ITT}}_Y = 1.2$, so $\hat\tau_{\mathrm{CACE}} = 4.0$ kg among people who attend because they are invited. The exclusion restriction is doubtful: the invitation and the voucher may motivate people to diet or exercise on their own, which would affect weight even among never-takers and inflate the estimate. Monotonicity (nobody is discouraged by the invitation) is more plausible.
4. Prove that with a single binary instrument and a single binary treatment, the 2SLS estimator of the coefficient of $W$ equals the Wald estimator.

   **Answer** With $\boldsymbol{Z} = [\boldsymbol{1}\ \boldsymbol{Z}]$ and $\boldsymbol{D} = [\boldsymbol{1}\ \boldsymbol{W}]$, $\boldsymbol{Z}^{\mathsf T}\boldsymbol{D}$ is square and $\hat{\boldsymbol\beta} = (\boldsymbol{Z}^{\mathsf T}\boldsymbol{D})^{-1}\boldsymbol{Z}^{\mathsf T}\boldsymbol{Y}$ solves $\sum_i(Y_i - b_0 - b_1W_i) = 0$ and $\sum_iZ_i(Y_i - b_0 - b_1W_i) = 0$. Subtracting the means gives $\sum_i(Z_i - \bar Z)(Y_i - b_1W_i) = 0$, so $b_1 = \widehat{\operatorname{Cov}}(Z, Y)/\widehat{\operatorname{Cov}}(Z, W)$. For binary $Z$, $\widehat{\operatorname{Cov}}(Z, Y) = \frac{N_1N_0}{N^2}(\bar Y_1 - \bar Y_0)$ (with divisor $N$) and similarly for $W$; the factors cancel, leaving $(\bar Y_1 - \bar Y_0)/(\bar W_1 - \bar W_0)$.
5. Construct a population with compliers and defiers in which every unit benefits from the treatment by 1, yet $\mathrm{ITT}_Y = 0$. What does the Wald ratio equal?

   **Answer** Take $\pi_{\mathrm{co}} = \pi_{\mathrm{df}} = 0.5$ and $Y_i(1) - Y_i(0) = 1$ for all. Then $\mathrm{ITT}_Y = 0.5 \times 1 - 0.5 \times 1 = 0$ and $\mathrm{ITT}_W = 0.5 - 0.5 = 0$; the ratio is $0/0$, undefined, and the data are indistinguishable from a treatment with no effect. With $\pi_{\mathrm{co}} = 0.6$, $\pi_{\mathrm{df}} = 0.4$ and effects $\tau_{\mathrm{co}} = 1$, $\tau_{\mathrm{df}} = 2$, the ratio is $(0.6 - 0.8)/0.2 = -1$, of the wrong sign although everyone benefits: without monotonicity the Wald ratio need not be a weighted average of unit effects.
6. Derive the Delta method variance of $\hat\tau_{\mathrm{CACE}} = \hat a/\hat b$, and evaluate it for the vitamin A data using the standard errors given and a covariance of about $1.7 \times 10^{-7}$.

   **Answer** With $g(a, b) = a/b$, $\nabla g = (1/b, -a/b^2)$, so $\operatorname{Var}(\hat a/\hat b) \approx \operatorname{Var}(\hat a)/b^2 + a^2\operatorname{Var}(\hat b)/b^4 - 2a\operatorname{Cov}(\hat a, \hat b)/b^3$. With $a = 0.00258$, $b = 0.8$: $0.00093^2/0.64 = 1.35 \times 10^{-6}$; $0.00258^2 \times 0.0036^2/0.41 = 2.1 \times 10^{-10}$; $2 \times 0.00258 \times 1.7 \times 10^{-7}/0.512 = 1.7 \times 10^{-9}$. The variance is about $1.35 \times 10^{-6}$, a standard error of $0.00116$: almost all the uncertainty comes from $\widehat{\mathrm{ITT}}_Y$.
7. Explain why, in the second panel of the first figure, conditioning on $W$ does not make $Z$ independent of $Y$, and what this implies for the "excluded" condition $Z \perp Y \mid (W, U)$.

   **Answer** $W$ is a collider on the path $Z \to W \leftarrow U \to Y$; conditioning on it opens that path, so $Z$ and $Y$ are dependent given $W$ even without a direct arrow. Only conditioning on both $W$ and $U$ blocks all paths, which is why the exclusion condition is stated given $(W, U)$. It cannot be checked because $U$ is unobserved; in particular, a regression of $Y$ on $W$ and $Z$ showing a nonzero coefficient of $Z$ does not prove that the exclusion restriction fails.
8. Why are the Balke–Pearl bounds for the vitamin A data so asymmetric about zero? What additional assumption would narrow them, and what would it identify?

   **Answer** One-sided noncompliance leaves the survival of the 20% never-takers under treatment completely unknown; their observed survival without the supplement is $0.986$, so under treatment it could lie anywhere in $[0, 1]$, moving the population effect by up to $0.2 \times 0.986 \approx 0.197$ downward but only by $0.2 \times 0.014$ upward. Assuming that the effect for never-takers equals that for compliers (or is nonnegative) narrows the bounds; equality would identify the population effect as $\tau_{\mathrm{CACE}}$, nonnegativity gives the lower bound $\pi_{\mathrm{co}}\tau_{\mathrm{CACE}} = \mathrm{ITT}_Y$.
