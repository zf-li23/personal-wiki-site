---
title: Stratified and Paired Randomized Experiments
description: Inference for stratified and paired randomized experiments with the four approaches of the previous chapters. Fisher tests with stratum-aware statistics, Neyman's stratified estimator with its variance and the precision gain over complete randomization, regression with stratum indicators and with a saturated interaction model, hierarchical models; for paired experiments the within-pair differences, a conservative variance estimator that needs no within-pair replication, and regression on pair-level covariates. Examples from Project STAR and the Electric Company experiment.
---

A completely randomized experiment treats all units alike. Often, however, it is known before the experiment that the outcomes differ systematically between groups of units: schools differ in their average test scores, patients of different ages in their prognosis. If such groups are formed in the design and the treatment is randomized separately within each, chance imbalance between the groups is ruled out, and the comparison of treated and control units is made among similar units. This is the **stratified randomized experiment** of [3.9.2](/3.9.2) (Definition 2.4.7), the causal-inference counterpart of **blocking** ([3.8.2](/3.8.2)) and the **randomized complete block design** ([3.8.6](/3.8.6)). Its limiting case, with two units per stratum, is the **paired randomized experiment** (Definition 2.4.8), corresponding to the **paired design** of [3.8.2](/3.8.2). This chapter adapts the four approaches developed for the CRE in [3.9.3](/3.9.3)–[3.9.6](/3.9.6) to these designs. The adaptations are mostly straightforward; the instructive points are where they are not. The same structure reappears in observational studies, where strata defined by the propensity score play the role of the design's strata ([3.9.9](/3.9.9), [3.9.10](/3.9.10)).

## 7.1. Stratified Randomized Experiments

### 7.1.1. Design and Notation

The $N$ units are partitioned into $J$ strata on the basis of their covariates, and a CRE is carried out within each stratum, independently across strata. Let $G_i \in \{1, \dots, J\}$ be the stratum of unit $i$ and $B_i(j) = \boldsymbol{1}\{G_i = j\}$. Stratum $j$ contains $N(j)$ units, of which $N_{\mathrm{t}}(j)$ are treated and $N_{\mathrm{c}}(j) = N(j) - N_{\mathrm{t}}(j)$ are controls; its share of the sample is $q(j) = N(j)/N$, and its propensity score is $e(j) = N_{\mathrm{t}}(j)/N(j)$. The assignment mechanism is

$$
\mathbb{P}\bigl(\boldsymbol{W} \mid \boldsymbol{X}, \boldsymbol{Y}(0), \boldsymbol{Y}(1)\bigr) = \prod_{j=1}^{J}\binom{N(j)}{N_{\mathrm{t}}(j)}^{-1} \quad \text{for } \boldsymbol{W} \in \mathcal{W}^+ = \Bigl\{\boldsymbol{W} \in \mathcal{W} : \sum_{i: G_i = j}W_i = N_{\mathrm{t}}(j) \text{ for } j = 1, \dots, J\Bigr\},
$$
and zero otherwise. The design is also called a randomized block experiment. Its distinguishing feature, compared with a CRE, is that the propensity score may differ between strata, and that it fixes the number of treated units in every stratum rather than only in total.

### 7.1.2. Project STAR

The Student/Teacher Achievement Ratio experiment (Project STAR), carried out in Tennessee in 1985–1986, evaluated the effect of class size on test scores, and it is one of the most influential randomized experiments in education. In the kindergarten data used here, the unit is the teacher, or class, rather than the individual student: students in the same class influence one another, and analyzing classes makes the no-interference part of SUTVA plausible ([3.9.1](/3.9.1)). The treatment is a small class (13–17 students), the control a regular class (22–25 students), and the outcome the class average of a mathematics test score. There are $N = 68$ classes in 16 schools, and the randomization was done within schools, so the school is the stratum:

| Schools | $N_{\mathrm{t}}(j)$ | $N_{\mathrm{c}}(j)$ | $e(j)$ | Assignments per school |
|---|---|---|---|---|
| 13 | 2 | 2 | 0.50 | $\binom{4}{2} = 6$ |
| 2 | 3 | 2 | 0.60 | $\binom{5}{3} = 10$ |
| 1 | 4 | 2 | 0.67 | $\binom{6}{4} = 15$ |

The number of possible assignment vectors is $6^{13} \times 10^2 \times 15 \approx 2 \times 10^{13}$, far fewer than the $\binom{68}{36} \approx 2.5 \times 10^{19}$ of a CRE with the same total number $N_{\mathrm{t}} = 36$ of small classes; stratification has excluded all assignments that would put, say, all small classes in a few schools.

### 7.1.3. Estimands

The effect within stratum $j$ and the overall effect are

$$
\tau_{\mathrm{fs}}(j) = \frac{1}{N(j)}\sum_{i: G_i = j}\bigl(Y_i(1) - Y_i(0)\bigr), \qquad
\tau_{\mathrm{fs}} = \frac{1}{N}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0)\bigr) = \sum_{j=1}^{J}q(j)\,\tau_{\mathrm{fs}}(j).
$$
The overall effect is the average of the stratum effects weighted by the stratum shares. With two strata, say females ($f$) and males ($m$), $\tau_{\mathrm{fs}} = q\,\tau_{\mathrm{fs}}(f) + (1 - q)\,\tau_{\mathrm{fs}}(m)$ with $q = N(f)/N$. Other weightings define other estimands, such as the effect for the treated, $\tau_{\mathrm{fs,t}}$, which weights stratum $j$ by its share $N_{\mathrm{t}}(j)/N_{\mathrm{t}}$ of the treated units.

### 7.1.4. Why Stratify, and What Makes It Harder

Stratification is used for three reasons: a CRE may be infeasible, for instance when the treatment must be implemented within each school or hospital; it gives more precise estimates when the strata predict the outcomes (Theorem 7.3.2); and understanding stratified experiments is the key to observational studies, which are analyzed as stratified experiments with unknown propensity scores ([3.9.8](/3.9.8)). In principle each stratum is a CRE and can be analyzed by the methods of [3.9.3](/3.9.3)–[3.9.6](/3.9.6). In practice the strata are often small (two treated and two control classes per school in STAR), the stratum-specific effects are not of interest in themselves, and the question is how to combine the strata into inference about $\tau_{\mathrm{fs}}$ or $\tau_{\mathrm{fs,t}}$.

## 7.2. Fisher's Exact P-Values

Fisher's sharp null hypothesis, $H_0\colon Y_i(0) = Y_i(1)$ for $i = 1, \dots, N$, is the same as in a CRE, and under it all missing outcomes are known. The p-value is computed exactly as in [3.9.3](/3.9.3), except that the randomization distribution is taken over $\mathcal{W}^+$ of the stratified design: the assignment is re-randomized within each stratum. Any statistic gives a valid test; the design matters for which statistic has power.

| Statistic | Definition | Assessment |
|---|---|---|
| one stratum only | $T^{\mathrm{dif}}(j) = \lvert\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - \bar Y_{\mathrm{c}}^{\mathrm{obs}}(j)\rvert$ | valid but wasteful: uses part of the data and may miss violations of $H_0$ elsewhere |
| pooled difference | $T^{\mathrm{dif}} = \lvert\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\rvert$ | valid, but if $e(j)$ varies and the strata differ in outcome level, it is not centered at zero under $H_0$, which costs power |
| weighted within-stratum differences | $T^{\mathrm{dif}, \lambda} = \Bigl\lvert\sum_{j=1}^{J}\lambda(j)\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - \bar Y_{\mathrm{c}}^{\mathrm{obs}}(j)\bigr)\Bigr\rvert$, $\sum_j\lambda(j) = 1$ | recommended; $\lambda(j) = q(j)$ targets $\tau_{\mathrm{fs}}$, $\lambda(j) \propto q(j)e(j)(1 - e(j))$ weights strata by their precision |
| pooled ranks | $T^{\operatorname{rank}} = \lvert\bar R_{\mathrm{t}} - \bar R_{\mathrm{c}}\rvert$ with ranks in the whole sample | as in a CRE; unattractive when the outcome levels differ much between strata |
| within-stratum ranks | $T^{\mathrm{rank,stratum}} = \lvert\bar R_{\mathrm{t}}^{\mathrm{strat}} - \bar R_{\mathrm{c}}^{\mathrm{strat}}\rvert$ | recommended; robust, and unaffected by differences in level between strata |

To see why the pooled difference is not centered, take two strata with $e(f) \ne e(m)$ and a null hypothesis that holds, but with higher outcomes among females. The treated group then contains a larger share of the stratum with higher outcomes than the control group, so $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$ is systematically positive although no unit has any effect. The test remains valid, because its randomization distribution is shifted in the same way, but a real effect is harder to distinguish from the shift.

The within-stratum normalized rank of unit $i$ ranks its outcome only among the units of its own stratum, centered as in [3.9.3](/3.9.3) (Definition 3.2.1):

$$
R_i^{\mathrm{strat}} = \sum_{i': G_{i'} = G_i}\boldsymbol{1}\bigl\{Y_{i'}^{\mathrm{obs}} < Y_i^{\mathrm{obs}}\bigr\} + \frac{1}{2}\Bigl(1 + \sum_{i': G_{i'} = G_i}\boldsymbol{1}\bigl\{Y_{i'}^{\mathrm{obs}} = Y_i^{\mathrm{obs}}\bigr\}\Bigr) - \frac{N(G_i) + 1}{2},
$$
and $\bar R_{\mathrm{t}}^{\mathrm{strat}}$, $\bar R_{\mathrm{c}}^{\mathrm{strat}}$ are its averages over treated and control units. Because the ranks are computed within strata, they remove differences in level between strata entirely, in the same way that the **Wilcoxon signed-rank test** removes pair effects ([3.6.8](/3.6.8)); these stratified rank tests belong to the family of **rank statistics** of [3.6](/3.6).

For Project STAR, with p-values approximated by simulation from the stratified randomization distribution:

| Statistic | Value | p-value |
|---|---|---|
| $T^{\mathrm{dif}}$ | 0.224 | 0.034 |
| $T^{\mathrm{dif}, \lambda}$, $\lambda(j) = q(j)$ | 0.241 | 0.023 |
| $T^{\mathrm{rank,stratum}}$ | 0.48 | 0.15 |

The tests based on means reject the null hypothesis of no effect at the $5\%$ level; the rank test does not. The difference arises because the evidence from the means rests partly on a few classes with extreme outcomes, which the ranks downweight. The two kinds of statistic answer slightly different questions, and the choice between them should be made before the data are seen.

## 7.3. Neyman's Approach

### 7.3.1. The Stratified Estimator

Within each stratum the assignment is a CRE, so the results of [3.9.4](/3.9.4) apply to the stratum-specific difference in means $\hat\tau^{\mathrm{dif}}(j) = \bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - \bar Y_{\mathrm{c}}^{\mathrm{obs}}(j)$: it is unbiased for $\tau_{\mathrm{fs}}(j)$, with the variance of Theorem 4.3.1 computed within the stratum. Combining the strata with the weights that define $\tau_{\mathrm{fs}}$ gives the stratified estimator.

**Theorem 7.3.1** In a stratified randomized experiment with $N_{\mathrm{t}}(j), N_{\mathrm{c}}(j) \ge 2$ for every stratum, let

$$
\hat\tau^{\mathrm{strat}} = \sum_{j=1}^{J}q(j)\,\hat\tau^{\mathrm{dif}}(j), \qquad
\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = \sum_{j=1}^{J}q(j)^2\left(\frac{s_{\mathrm{c}}^2(j)}{N_{\mathrm{c}}(j)} + \frac{s_{\mathrm{t}}^2(j)}{N_{\mathrm{t}}(j)}\right),
$$
where $s_{\mathrm{c}}^2(j)$ and $s_{\mathrm{t}}^2(j)$ are the sample variances of the observed outcomes of the control and treated units in stratum $j$. Then

$$
\mathbb{E}_W\bigl[\hat\tau^{\mathrm{strat}}\bigr] = \tau_{\mathrm{fs}}, \qquad
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{strat}}\bigr) = \sum_{j=1}^{J}q(j)^2\left(\frac{S_{\mathrm{c}}^2(j)}{N_{\mathrm{c}}(j)} + \frac{S_{\mathrm{t}}^2(j)}{N_{\mathrm{t}}(j)} - \frac{S_{\mathrm{tc}}^2(j)}{N(j)}\right),
$$
with the finite-population variances $S^2(j)$ computed within stratum $j$, and $\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] \ge \operatorname{Var}_W(\hat\tau^{\mathrm{strat}})$, with equality if the unit-level effect is constant within each stratum.

**Proof** By Theorem 4.2.1 applied within stratum $j$, $\mathbb{E}_W[\hat\tau^{\mathrm{dif}}(j)] = \tau_{\mathrm{fs}}(j)$, so by linearity $\mathbb{E}_W[\hat\tau^{\mathrm{strat}}] = \sum_j q(j)\tau_{\mathrm{fs}}(j) = \tau_{\mathrm{fs}}$. The assignments in different strata are independent, so the $\hat\tau^{\mathrm{dif}}(j)$ are independent and

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{strat}}\bigr) = \sum_{j=1}^{J}q(j)^2\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}(j)\bigr),
$$
where each term is given by Theorem 4.3.1 within the stratum. By Theorem 4.4.1 within each stratum, $\mathbb{E}_W[s_{\mathrm{c}}^2(j)] = S_{\mathrm{c}}^2(j)$ and $\mathbb{E}_W[s_{\mathrm{t}}^2(j)] = S_{\mathrm{t}}^2(j)$, so $\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] - \operatorname{Var}_W(\hat\tau^{\mathrm{strat}}) = \sum_j q(j)^2S_{\mathrm{tc}}^2(j)/N(j) \ge 0$, with equality exactly when every $S_{\mathrm{tc}}^2(j) = 0$. $\square$

The simple difference in means of all treated and all control units is in general biased in a stratified experiment: it weights stratum $j$ by $N_{\mathrm{t}}(j)/N_{\mathrm{t}}$ among the treated and by $N_{\mathrm{c}}(j)/N_{\mathrm{c}}$ among the controls, and these weights differ when the propensity scores differ. It is unbiased only if $e(j)$ is the same in all strata, in which case it coincides with $\hat\tau^{\mathrm{strat}}$.

**Example 7.3.1** For Project STAR, the stratified analysis gives $\hat\tau^{\mathrm{strat}} = 0.241$ and $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = 0.092^2$, so the $95\%$ interval for $\tau_{\mathrm{fs}}$ is $0.241 \pm 1.96 \times 0.092 = (0.061, 0.421)$. Analyzing the same data, incorrectly, as if they came from a CRE gives $\hat\tau^{\mathrm{dif}} = 0.224$ with standard error $0.141$ and the interval $(-0.053, 0.500)$, which includes zero.

The comparison shows two things. The CRE variance estimator is not valid here, because the probability of treatment varies between the strata ($0.5$, $0.6$, $0.67$) and the CRE formulas ignore the design; for the same reason $\hat\tau^{\mathrm{dif}}$ is not unbiased. And there is a substantial gain in precision from the stratification, because the average outcomes differ between schools: the stratified analysis removes the between-school variation from the error.

:::

### 7.3.2. Stratified versus Completely Randomized Experiments

The precision gain can be made precise in the super-population. Take two strata, $f$ and $m$, with shares $q$ and $1 - q$ in the population, and a common proportion $p$ of treated units in each stratum, so that the stratified and the completely randomized experiment treat the same number of units. Write $\mu_w(g)$ and $\sigma_w^2(g)$ for the mean and variance of $Y_i(w)$ in stratum $g$, for $w \in \{\mathrm{c}, \mathrm{t}\}$.

**Theorem 7.3.2** Under these conditions, with $N_{\mathrm{t}} = pN$,

$$
N\Bigl(\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{dif}}\bigr)_{\mathrm{CRE}} - \operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{strat}}\bigr)_{\mathrm{SRE}}\Bigr) = q(1 - q)\left(\frac{\bigl(\mu_{\mathrm{c}}(f) - \mu_{\mathrm{c}}(m)\bigr)^2}{1 - p} + \frac{\bigl(\mu_{\mathrm{t}}(f) - \mu_{\mathrm{t}}(m)\bigr)^2}{p}\right) \ge 0.
$$

**Proof** In the CRE, by Theorem 4.6.1, $N\operatorname{Var}_{\mathrm{sp}}(\hat\tau^{\mathrm{dif}}) = \sigma_{\mathrm{c}}^2/(1 - p) + \sigma_{\mathrm{t}}^2/p$, where $\sigma_w^2$ is the population variance of $Y_i(w)$. By the law of total variance over the strata,

$$
\sigma_w^2 = q\,\sigma_w^2(f) + (1 - q)\,\sigma_w^2(m) + q(1 - q)\bigl(\mu_w(f) - \mu_w(m)\bigr)^2.
$$
In the SRE, $\hat\tau^{\mathrm{strat}} = q\,\hat\tau^{\mathrm{dif}}(f) + (1 - q)\,\hat\tau^{\mathrm{dif}}(m)$, where stratum $g$ contains $qN$ or $(1 - q)N$ units of which a proportion $p$ is treated. Applying Theorem 4.6.1 within each stratum and using independence,

$$
N\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{strat}}\bigr) = q\left(\frac{\sigma_{\mathrm{c}}^2(f)}{1 - p} + \frac{\sigma_{\mathrm{t}}^2(f)}{p}\right) + (1 - q)\left(\frac{\sigma_{\mathrm{c}}^2(m)}{1 - p} + \frac{\sigma_{\mathrm{t}}^2(m)}{p}\right).
$$
Subtracting, the within-stratum variances cancel and only the between-stratum terms of the total variance remain. $\square$

The variance of the stratified estimator is never larger, and it is smaller exactly when the stratum means of the potential outcomes differ: one is never worse off stratifying on a covariate, in this setting. The gain is the variance that the stratifying covariate explains, the same quantity that regression adjustment exploits in [3.9.5](/3.9.5); stratification removes it in the design rather than in the analysis. In small samples there is a modest price: the variance estimator of Theorem 7.3.1 uses fewer degrees of freedom, and strata with a single treated or control unit allow no within-stratum variance estimate at all, a problem that the paired design of Section 7.6 has to solve.

## 7.4. Regression Methods

### 7.4.1. Stratum Indicators

A natural regression includes the treatment indicator and a separate intercept for each stratum:

$$
Y_i^{\mathrm{obs}} = \tau W_i + \sum_{j=1}^{J}\beta(j)B_i(j) + \varepsilon_i,
$$
with $J + 1$ parameters, least squares estimators $(\hat\tau^{\mathrm{ols}}, \hat{\boldsymbol{\beta}}^{\mathrm{ols}})$ and population counterparts $(\tau^*, \boldsymbol{\beta}^*) = \arg\min\mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \tau W_i - \sum_j\beta(j)B_i(j))^2\bigr]$. If the effect were the same in every stratum, $\tau_{\mathrm{sp}}(j) = \tau$, the model would be correct and $\tau^* = \tau$. Without that assumption the coefficient is a weighted average of the stratum effects, but not with the weights of $\tau_{\mathrm{sp}}$.

**Theorem 7.4.1** In a stratified randomized experiment on a sample drawn at random from an infinite population, with stratum probabilities $q(j)$ and propensity scores $e(j)$,

$$
\tau^* = \tau_\omega = \frac{\sum_{j=1}^{J}\omega(j)\,\tau_{\mathrm{sp}}(j)}{\sum_{j=1}^{J}\omega(j)}, \qquad \omega(j) = q(j)\,e(j)\bigl(1 - e(j)\bigr),
$$
and $\sqrt{N}(\hat\tau^{\mathrm{ols}} - \tau_\omega)$ is asymptotically normal with mean zero.

**Proof** By the **Frisch–Waugh–Lovell theorem**, $\tau^*$ is the population coefficient of $Y^{\mathrm{obs}}$ on the residual of $W$ after projection on the stratum indicators. That projection is $\sum_j e(j)B_i(j) = e(G_i)$, so the residual is $W_i - e(G_i)$ and

$$
\tau^* = \frac{\mathbb{E}_{\mathrm{sp}}\bigl[(W_i - e(G_i))Y_i^{\mathrm{obs}}\bigr]}{\mathbb{E}_{\mathrm{sp}}\bigl[(W_i - e(G_i))^2\bigr]}.
$$
Conditional on $G_i = j$, $W_i$ is $\mathrm{Ber}(e(j))$ and independent of the potential outcomes, so $\mathbb{E}[(W_i - e(j))^2 \mid G_i = j] = e(j)(1 - e(j))$ and

$$
\mathbb{E}\bigl[(W_i - e(j))Y_i^{\mathrm{obs}} \bigm| G_i = j\bigr] = e(j)(1 - e(j))\,\mathbb{E}[Y_i(1) \mid G_i = j] - (1 - e(j))e(j)\,\mathbb{E}[Y_i(0) \mid G_i = j] = e(j)(1 - e(j))\,\tau_{\mathrm{sp}}(j).
$$
Averaging over the strata with probabilities $q(j)$ gives the formula. Asymptotic normality follows as in Theorem 5.3.2. $\square$

The weights favor strata with many units and with propensity scores near $1/2$, the strata in which the effect is estimated most precisely. When the propensity score is the same in all strata, or when the effect is the same in all strata, $\tau_\omega = \tau_{\mathrm{sp}}$; otherwise the regression estimates a well-defined causal quantity, but not the average effect.

### 7.4.2. A Saturated Model

To recover $\tau_{\mathrm{sp}}$, allow a separate effect in each stratum, a **saturated model** with $2J$ parameters. In the parametrization

$$
Y_i^{\mathrm{obs}} = \tau W_i\frac{B_i(J)}{N(J)/N} + \sum_{j=1}^{J}\beta(j)B_i(j) + \sum_{j=1}^{J-1}\gamma(j)W_i\Bigl(B_i(j) - B_i(J)\frac{N(j)}{N(J)}\Bigr) + \varepsilon_i,
$$
the coefficient $\tau$ is directly the weighted average of the stratum effects. Equivalent forms are easier to read: (i) $Y_{i}^{\mathrm{obs}} = \beta_j + \tau_jW_i + \varepsilon_i$ for unit $i$ in stratum $j$, with $\tau = N^{-1}\sum_j N(j)\tau_j$; or (ii) $Y_{i}^{\mathrm{obs}} = \beta_j + \tau W_i + \gamma_jW_i + \varepsilon_i$ with the constraint $\sum_j N(j)\gamma_j = 0$.

**Theorem 7.4.2** In a stratified randomized experiment on a sample drawn at random from an infinite population, the population counterpart of the coefficient $\hat\tau^{\mathrm{ols,inter}}$ in the saturated model is $\tau^* = \tau_{\mathrm{sp}}$, and

$$
\sqrt{N}\bigl(\hat\tau^{\mathrm{ols,inter}} - \tau_{\mathrm{sp}}\bigr) \xrightarrow{d} \mathcal{N}\left(0,\ \sum_{j=1}^{J}q(j)^2\left(\frac{\sigma_{\mathrm{c}}^2(j)}{(1 - e(j))q(j)} + \frac{\sigma_{\mathrm{t}}^2(j)}{e(j)q(j)}\right)\right).
$$

In form (i) each $\hat\tau_j$ is the within-stratum difference in means, so $\hat\tau^{\mathrm{ols,inter}} = \sum_j q(j)\hat\tau^{\mathrm{dif}}(j) = \hat\tau^{\mathrm{strat}}$ exactly: the saturated regression reproduces Neyman's stratified estimator, and its asymptotic variance is the super-population version of the variance in Theorem 7.3.1. In R the two models are fitted by

```r
fit_add <- lm(Y_obs ~ W + Strata)   # coefficient of W estimates tau_omega
fit_sat <- lm(Y_obs ~ W * Strata)   # coefficient of W is the effect in the reference stratum
```

With R's default contrasts the coefficient of `W` in `fit_sat` is the effect in the first stratum, not the average effect; $\tau$ has to be computed as $\sum_j q(j)\hat\tau_j$ from the coefficients (or the model fitted in the centered parametrization above), and its standard error from the corresponding linear combination.

For Project STAR, the additive model gives $\hat\tau^{\mathrm{ols}} = 0.238$ (s.e. $0.103$) and the saturated model $\hat\tau^{\mathrm{ols,inter}} = 0.241$ (s.e. $0.095$). The two estimates are close, with similar standard errors, which is consistent with limited heterogeneity of the effect between schools: $\tau_\omega$ and $\tau_{\mathrm{sp}}$ differ little when the stratum effects are similar.

## 7.5. Model-Based Analysis

The model-based approach of [3.9.6](/3.9.6) carries over with one new choice. The three inputs are the stratified assignment mechanism, a model for the potential outcomes within each stratum, say $Y_i(w) \mid G_i = j, \theta \sim \mathcal{N}(\mu_w(j), \sigma_w^2)$, and a prior for the stratum parameters $\theta_j = (\mu_{\mathrm{c}}(j), \mu_{\mathrm{t}}(j))$. By Theorem 6.3.1 the assignment mechanism, which does not depend on the outcomes, again drops out. The priors can be independent across strata, which with two treated and two control units per stratum leaves each $\theta_j$ poorly determined, or hierarchical,

$$
\begin{pmatrix} \mu_{\mathrm{c}}(j) \\ \mu_{\mathrm{t}}(j) \end{pmatrix} \Bigm| \boldsymbol{\gamma}, \Sigma \overset{\text{iid}}{\sim} \mathcal{N}(\boldsymbol{\gamma}, \Sigma), \qquad j = 1, \dots, J,
$$
with a prior on the hyperparameters $(\boldsymbol{\gamma}, \Sigma)$. The **hierarchical model** ([3.7.6](/3.7.6)) lets each stratum borrow strength from the others, partially pooling the stratum means towards the common mean by an amount the data determine. It also makes new estimands available: the posterior of $\Sigma$ shows how much the average potential outcomes and the treatment effects vary between strata, and the variance of the stratum effects $\mu_{\mathrm{t}}(j) - \mu_{\mathrm{c}}(j)$ is a direct measure of effect heterogeneity. For Project STAR the hierarchical model asks how much the effect of small classes differs between schools, a question none of the other three methods addresses directly.

## 7.6. Paired Randomized Experiments

### 7.6.1. Design and Notation

A paired randomized experiment is a stratified experiment with $J = N/2$ strata of two units each, one of which is treated: $N(j) = 2$ and $N_{\mathrm{t}}(j) = N_{\mathrm{c}}(j) = 1$. Each unit has assignment probability $1/2$, and there are $2^{N/2}$ possible assignment vectors. The design is chosen when the variation of the potential outcomes within pairs is expected to be much smaller than the variation between pairs; in a large population it is often possible to find pairs of units that are very similar in their covariates.

The two units of pair $j$ are labeled $A$ and $B$, with potential outcomes $Y_{j,A}(0), Y_{j,A}(1), Y_{j,B}(0), Y_{j,B}(1)$, covariates $X_{j,A}, X_{j,B}$, and treatment indicators $W_{j,A}$ and $W_{j,B} = 1 - W_{j,A}$. The observed difference in pair $j$, treated minus control, is

$$
\hat\tau^{\mathrm{pair}}(j) = W_{j,A}\bigl(Y_{j,A}^{\mathrm{obs}} - Y_{j,B}^{\mathrm{obs}}\bigr) + (1 - W_{j,A})\bigl(Y_{j,B}^{\mathrm{obs}} - Y_{j,A}^{\mathrm{obs}}\bigr),
$$
and the estimands are the pair-level and overall average effects

$$
\tau^{\mathrm{pair}}(j) = \frac{1}{2}\Bigl[\bigl(Y_{j,A}(1) - Y_{j,A}(0)\bigr) + \bigl(Y_{j,B}(1) - Y_{j,B}(0)\bigr)\Bigr], \qquad
\tau_{\mathrm{fs}} = \frac{1}{J}\sum_{j=1}^{J}\tau^{\mathrm{pair}}(j).
$$
Since every pair contributes one treated and one control unit, the treated and control subsamples are as alike as the pairing makes them.

### 7.6.2. The Electric Company Experiment

Around 1970 the Children's Television Workshop, the producer of *Sesame Street*, evaluated *The Electric Company*, an educational television program designed to teach reading (Ball and Bogatz 1972). Classes were paired within schools on the basis of their reading scores, and in each pair one class was randomly chosen to view the program. The unit is the class, the covariate $X$ the class average pre-test reading score, and the outcome $Y$ the post-test score. The eight pairs from Youngstown, Ohio:

| Pair | $W_{j,A}$ | $Y_{j,A}^{\mathrm{obs}}$ | $X_{j,A}$ | $W_{j,B}$ | $Y_{j,B}^{\mathrm{obs}}$ | $X_{j,B}$ | $\hat\tau^{\mathrm{pair}}(j)$ | $\Delta_{X,j}$ |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 54.6 | 12.9 | 1 | 60.6 | 12.0 | 6.0 | $-0.9$ |
| 2 | 0 | 56.5 | 15.1 | 1 | 55.5 | 13.9 | $-1.0$ | $-1.2$ |
| 3 | 0 | 75.2 | 16.8 | 1 | 84.8 | 17.2 | 9.6 | 0.4 |
| 4 | 0 | 75.6 | 15.8 | 1 | 101.9 | 18.9 | 26.3 | 3.1 |
| 5 | 0 | 55.3 | 13.9 | 1 | 70.6 | 15.3 | 15.3 | 1.4 |
| 6 | 0 | 59.3 | 14.5 | 1 | 78.4 | 16.6 | 19.1 | 2.1 |
| 7 | 0 | 87.0 | 17.0 | 1 | 84.2 | 16.0 | $-2.8$ | $-1.0$ |
| 8 | 0 | 73.7 | 15.8 | 1 | 108.6 | 20.1 | 34.9 | 4.3 |

Here the units are labeled so that unit $B$ is the treated one, and $\Delta_{X,j}$ is the difference in pre-test scores, treated minus control.

### 7.6.3. Fisher's Exact P-Values

The sharp null hypothesis and the randomization are those of an SRE: under $H_0$ the randomization distribution is obtained by flipping, independently for each pair, which unit is treated, which changes the sign of $\hat\tau^{\mathrm{pair}}(j)$. The statistics of Section 7.2 behave as in an SRE, with one exception: the stratum-specific statistic $T^{\mathrm{dif}}(j)$ is useless, because a single pair gives a single difference whose randomization distribution has two points. The natural statistic is $T = \lvert\frac{1}{J}\sum_j\hat\tau^{\mathrm{pair}}(j)\rvert$, which equals the weighted statistic $T^{\mathrm{dif}, \lambda}$ with $\lambda(j) = 1/J$. Its exact distribution is that of a sum of $\pm\hat\tau^{\mathrm{pair}}(j)$ with independent random signs, and replacing the differences by their ranks gives the **Wilcoxon signed-rank test** ([3.6.8](/3.6.8)), whose classical justification by symmetry is here replaced by the randomization of the design.

### 7.6.4. Neyman's Approach

The difference in means is the average of the pair differences, $\hat\tau^{\mathrm{dif}} = \frac{1}{J}\sum_j\hat\tau^{\mathrm{pair}}(j)$, and by Theorem 7.3.1 (or directly, since each $\hat\tau^{\mathrm{pair}}(j)$ takes its two possible values with probability $1/2$) it is unbiased. The problem is the variance. Within a pair, the variance of $\hat\tau^{\mathrm{pair}}(j)$ involves $Y_{j,A}(0)$, $Y_{j,A}(1)$, $Y_{j,B}(0)$ and $Y_{j,B}(1)$, of which only two are ever observed, and with one treated and one control unit there is no within-pair sample variance. The stratum-wise estimator of Theorem 7.3.1 is not defined. The solution is to use the variation between pairs instead.

**Theorem 7.6.1** Suppose there are $J$ pairs of units, and in each pair one unit is randomly assigned to treatment and the other to control. Then

1. $\mathbb{E}_W\bigl[\hat\tau^{\mathrm{dif}}\bigr] = \tau_{\mathrm{fs}}$;
2. $\displaystyle\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{1}{N^2}\sum_{j=1}^{J}\Bigl(Y_{j,A}(0) + Y_{j,A}(1) - Y_{j,B}(0) - Y_{j,B}(1)\Bigr)^2$;
3. the estimator $\displaystyle\widehat{\operatorname{Var}}{}^{\mathrm{pair}} = \frac{1}{J(J - 1)}\sum_{j=1}^{J}\bigl(\hat\tau^{\mathrm{pair}}(j) - \hat\tau^{\mathrm{dif}}\bigr)^2$ satisfies

$$
\mathbb{E}_W\bigl[\widehat{\operatorname{Var}}{}^{\mathrm{pair}}\bigr] = \operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) + \frac{1}{J(J - 1)}\sum_{j=1}^{J}\bigl(\tau^{\mathrm{pair}}(j) - \tau_{\mathrm{fs}}\bigr)^2 \ge \operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr).
$$

**Proof** The pair difference takes the value $d_j^{A} = Y_{j,A}(1) - Y_{j,B}(0)$ if $A$ is treated and $d_j^{B} = Y_{j,B}(1) - Y_{j,A}(0)$ if $B$ is treated, each with probability $1/2$. Its mean is $\frac{1}{2}(d_j^A + d_j^B) = \tau^{\mathrm{pair}}(j)$, which gives (1) after averaging over pairs. Its variance is $\frac{1}{4}(d_j^A - d_j^B)^2 = \frac{1}{4}\bigl(Y_{j,A}(1) + Y_{j,A}(0) - Y_{j,B}(1) - Y_{j,B}(0)\bigr)^2$. The pairs are assigned independently, so $\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) = \frac{1}{J^2}\sum_j\operatorname{Var}_W(\hat\tau^{\mathrm{pair}}(j))$, which is (2) because $4J^2 = N^2$. For (3), the $\hat\tau^{\mathrm{pair}}(j)$ are independent with means $\tau^{\mathrm{pair}}(j)$ and variances $v_j$. The standard computation for independent, not identically distributed variables gives

$$
\mathbb{E}_W\Bigl[\sum_{j=1}^{J}\bigl(\hat\tau^{\mathrm{pair}}(j) - \hat\tau^{\mathrm{dif}}\bigr)^2\Bigr] = \Bigl(1 - \frac{1}{J}\Bigr)\sum_{j=1}^{J}v_j + \sum_{j=1}^{J}\bigl(\tau^{\mathrm{pair}}(j) - \tau_{\mathrm{fs}}\bigr)^2.
$$
Dividing by $J(J - 1)$ and using $\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) = \frac{1}{J^2}\sum_j v_j$ gives (3). $\square$

The estimator is unbiased if the average effect is the same in every pair, $\tau^{\mathrm{pair}}(j) = \tau_{\mathrm{fs}}$ for all $j$, which holds in particular under the two extra assumptions sometimes made for paired designs: (A1) the effect is constant within pairs, $Y_{j,A}(1) - Y_{j,A}(0) = Y_{j,B}(1) - Y_{j,B}(0)$, and (A2) it is constant across pairs, with equal within-pair variances. Constancy within pairs alone is not needed. If the effects are heterogeneous across pairs, $\widehat{\operatorname{Var}}{}^{\mathrm{pair}}$ is upwardly biased, and the corresponding confidence intervals are conservative but still valid, exactly as for the Neyman estimator in a CRE.

**Example 7.6.1** For the Youngstown pairs, $\hat\tau^{\mathrm{dif}} = \frac{1}{8}\sum_j\hat\tau^{\mathrm{pair}}(j) = 107.4/8 = 13.4$ and

$$
\widehat{\operatorname{Var}}{}^{\mathrm{pair}} = \frac{1}{8 \cdot 7}\sum_{j=1}^{8}\bigl(\hat\tau^{\mathrm{pair}}(j) - 13.4\bigr)^2 = 4.6^2,
$$
so the $95\%$ interval is $13.4 \pm 1.96 \times 4.6 = (4.3, 22.5)$. If the same assignment had arisen from a CRE of the 16 classes, the estimate would be the same, $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = 13.4$, but the Neyman variance would use the sample standard deviations of the two groups, $s_{\mathrm{c}} = 12.2$ and $s_{\mathrm{t}} = 18.5$: $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = 12.2^2/8 + 18.5^2/8 = 7.8^2$, and the interval $(-2.0, 28.8)$. The pairing removes the large differences between classes in average reading level, which a CRE analysis leaves in the error, and the standard error falls by forty percent.

:::

### 7.6.5. Regression Methods

The regression of [3.9.5](/3.9.5) on individual units runs into the same difficulty as the Neyman variance: with stratum indicators for $J = N/2$ pairs, the saturated model has as many parameters as observations. The solution again follows Neyman: the difference in means is itself a regression estimator, the intercept of a regression of the pair differences on a constant, and the pair differences are the basic outcome of the analysis. Pair-level covariates can then be added:

| Model | Regression of $\hat\tau^{\mathrm{pair}}(j)$ on | Covariates |
|---|---|---|
| $M_1$ | $\tau + \varepsilon_j$ | none; $\hat\tau^{\mathrm{ols}} = \frac{2}{N}\sum_j\hat\tau^{\mathrm{pair}}(j) = \hat\tau^{\mathrm{dif}}$ |
| $M_2$ | $\tau + \beta\Delta_{X,j} + \varepsilon_j$ | within-pair difference $\Delta_{X,j} = W_{j,A}(X_{j,A} - X_{j,B}) + (1 - W_{j,A})(X_{j,B} - X_{j,A})$ |
| $M_3$ | $\tau + \gamma(\bar X_j - \bar X) + \varepsilon_j$ | pair average $\bar X_j = (X_{j,A} + X_{j,B})/2$ |
| $M_4$ | $\tau + \beta\Delta_{X,j} + \gamma(\bar X_j - \bar X) + \varepsilon_j$ | both |

The within-pair difference $\Delta_{X,j}$ adjusts for chance imbalance between the treated and control unit of a pair; the pair average $\bar X_j$ allows the effect to vary with the level of the pair, and is centered so that $\tau$ remains the average effect.

**Theorem 7.6.2** Suppose a paired randomized experiment is conducted on a sample of pairs drawn at random from a super-population of pairs, and let $(\tau^*, \beta^*, \gamma^*)$ be the population counterparts of the least squares coefficients in model $M_4$ (with $\mu_X$ in place of $\bar X$). Then $\tau^* = \tau_{\mathrm{sp}}$, and $\sqrt{J}(\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}})$ is asymptotically normal with mean zero.

The proof follows the pattern of Theorems 5.3.1 and 7.4.1. The randomization within the pair makes the sign of $\Delta_{X,j}$ equally likely to be positive or negative, independently of the pair's potential outcomes and of $\bar X_j$, so $\mathbb{E}[\Delta_{X,j}] = 0$ and $\mathbb{E}[\Delta_{X,j}(\bar X_j - \mu_X)] = 0$; the objective separates as in the CRE, and the intercept equals the population mean of $\hat\tau^{\mathrm{pair}}(j)$, which is $\tau_{\mathrm{sp}}$.

For the Youngstown pairs, ordinary least squares gives (conventional standard errors in parentheses):

| Model | $\hat\tau$ | coefficient of $\Delta_{X,j}$ | coefficient of $\bar X_j - \bar X$ |
|---|---|---|---|
| $M_1$ | 13.4 (4.6) | | |
| $M_2$ | 7.0 (1.0) | 6.3 (0.5) | |
| $M_3$ | 13.4 (4.2) | | 3.9 (2.5) |
| $M_4$ | 6.3 (0.9) | 6.9 (0.5) | $-1.1$ (0.5) |

The within-pair difference in pre-test scores is a strong predictor: the treated classes happened to have higher pre-test scores than their partners by $1.0$ point on average ($\bar\Delta_X = 8.2/8$), and with a slope above $6$ this chance imbalance accounts for about half of the unadjusted estimate. Adjusting for it lowers the estimate to about $7$ and the standard error by a factor of four. With only eight pairs these numbers are fragile, and the large-sample justification of Theorem 7.6.2 is weak; the qualitative lesson, that the pairing removes between-pair variation while regression on $\Delta_{X,j}$ removes the remaining within-pair imbalance, is robust. The pair average, in contrast, contributes little.

### 7.6.6. Model-Based Analysis

The model-based analysis of a paired experiment is that of an SRE with a hierarchical prior, which is here almost unavoidable: each pair contributes only two observations, so pair-specific parameters cannot be estimated without pooling. A typical model writes

$$
Y_{j,u}(0) = \mu_j + \beta X_{j,u} + \varepsilon_{j,u}(0), \qquad Y_{j,u}(1) = \mu_j + \gamma + \beta X_{j,u} + \varepsilon_{j,u}(1), \qquad \mu_j \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma_\mu^2),
$$
for units $u \in \{A, B\}$, with normal errors of variances $\sigma_{\mathrm{c}}^2$ and $\sigma_{\mathrm{t}}^2$, so that $\tau_{\mathrm{sp}} = \gamma$. With weak priors on $\theta = (\mu, \beta, \gamma, \log\sigma_\mu, \log\sigma_{\mathrm{c}}, \log\sigma_{\mathrm{t}})$, the posterior is explored by a **random walk Metropolis** sampler; given $\theta$, the pair effects $\mu_j$ are drawn from their conditional posterior, the missing outcomes imputed, and $\tau_{\mathrm{fs}}$ computed for each draw as in Algorithm 6.6.1. For the Electric Company data the results are close to those of the regression with the within-pair difference in pre-test scores, partly because the model uses the same linear dependence on the covariate.

![Randomization distributions of the estimated average effect for one simulated population of 80 units whose potential outcomes depend strongly on a covariate (left), under complete randomization, stratification into four strata by covariate quartiles, and pairing of neighbouring units; and the potential outcomes with the stratum boundaries (right). Simulated data](./plots/sre_vs_cre.py)

The figure shows the gain from blocking on a predictive covariate. All three estimators are unbiased; the stratified design reduces the standard deviation by almost half, and pairing, which is the finest stratification, reduces it further.

## Summary

| | CRE | SRE | PRE |
|---|---|---|---|
| Randomization | $N_{\mathrm{t}}$ of $N$ units | CRE within each stratum | one of two units in each pair |
| Fisher | any statistic | within-stratum differences or ranks | sign-flipping of pair differences; signed ranks |
| Neyman estimator | $\hat\tau^{\mathrm{dif}}$ | $\hat\tau^{\mathrm{strat}} = \sum_j q(j)\hat\tau^{\mathrm{dif}}(j)$ | mean of $\hat\tau^{\mathrm{pair}}(j)$ |
| Variance estimator | $s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}$ | $\sum_j q(j)^2\bigl(s_{\mathrm{c}}^2(j)/N_{\mathrm{c}}(j) + s_{\mathrm{t}}^2(j)/N_{\mathrm{t}}(j)\bigr)$ | $\frac{1}{J(J - 1)}\sum_j(\hat\tau^{\mathrm{pair}}(j) - \hat\tau)^2$ |
| Regression | $Y \sim W + X$ | $Y \sim W + $ strata estimates $\tau_\omega$; saturated model gives $\tau_{\mathrm{sp}}$ | pair differences on $\Delta_X$, $\bar X_j$ |
| Model-based | i.i.d. units | independent or hierarchical prior over strata | hierarchical prior over pairs |

- Stratify in the design when treatment rates or potential outcomes vary systematically between strata; all four approaches adapt directly.
- The Neyman stratified estimator is unbiased with variance $\sum_j q(j)^2\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}(j))$ (Theorem 7.3.1); in the super-population it is never less precise than the CRE estimator, the gain being the between-stratum variance (Theorem 7.3.2).
- Analyzing an SRE as a CRE is wrong when propensity scores differ: the estimator is biased and its variance estimate invalid (Project STAR: $0.224 \pm 0.141$ vs $0.241 \pm 0.092$).
- Regression with stratum dummies weights stratum effects by $q(j)e(j)(1 - e(j))$ (Theorem 7.4.1); the saturated model recovers $\tau_{\mathrm{sp}}$ (Theorem 7.4.2).
- In a PRE the within-pair difference is the basic quantity: the variance estimator uses between-pair variation and is conservative unless the pair effects are constant (Theorem 7.6.1); regressions use pair differences as outcomes (Theorem 7.6.2).
- Electric Company: $13.4$ (s.e. $4.6$) as a paired analysis vs $7.8$ as a CRE analysis.

## Questions

1. An SRE has two strata. Stratum 1 has $N(1) = 4$ units with $N_{\mathrm{t}}(1) = 2$, and stratum 2 has $N(2) = 6$ units with $N_{\mathrm{t}}(2) = 2$. How many assignment vectors are possible? How many would a CRE with $N_{\mathrm{t}} = 4$ allow? What are $q(j)$ and $e(j)$?

   **Answer** $\binom{4}{2}\binom{6}{2} = 6 \times 15 = 90$, compared with $\binom{10}{4} = 210$ for the CRE. $q(1) = 0.4$, $q(2) = 0.6$; $e(1) = 0.5$, $e(2) = 1/3$.

2. In the SRE of Question 1, the observed outcomes are: stratum 1, treated $10, 12$, control $6, 8$; stratum 2, treated $5, 7$, control $2, 3, 4, 3$. Compute $\hat\tau^{\mathrm{strat}}$, its Neyman variance estimate, and the naive difference in means. Why do the two estimates differ?

   **Answer** Stratum 1: $\hat\tau^{\mathrm{dif}}(1) = 11 - 7 = 4$, $s_{\mathrm{t}}^2(1) = 2$, $s_{\mathrm{c}}^2(1) = 2$. Stratum 2: $\hat\tau^{\mathrm{dif}}(2) = 6 - 3 = 3$, $s_{\mathrm{t}}^2(2) = 2$, $s_{\mathrm{c}}^2(2) = 2/3$. Then $\hat\tau^{\mathrm{strat}} = 0.4 \cdot 4 + 0.6 \cdot 3 = 3.4$ and $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = 0.16(2/2 + 2/2) + 0.36\bigl((2/3)/4 + 2/2\bigr) = 0.32 + 0.42 = 0.74$, s.e. $0.86$. The naive estimate is $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = 34/4 - 26/6 = 8.5 - 4.33 = 4.17$. Stratum 1 has higher outcomes and a higher propensity score, so it is overrepresented among the treated ($50\%$ of the treated, $33\%$ of the controls); the naive estimate mixes the effect with the difference in levels between the strata.

3. Show that if the propensity score is the same in every stratum, $e(j) = N_{\mathrm{t}}/N$, then $\hat\tau^{\mathrm{strat}} = \hat\tau^{\mathrm{dif}}$. Does it follow that the CRE variance estimator is appropriate?

   **Answer** With $N_{\mathrm{t}}(j) = e N(j)$, the treated mean is $\bar Y_{\mathrm{t}}^{\mathrm{obs}} = \sum_j\frac{N_{\mathrm{t}}(j)}{N_{\mathrm{t}}}\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) = \sum_j q(j)\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j)$, and likewise for the controls, so the two estimators coincide. The variance estimator does not follow: the CRE estimator includes the between-stratum variation of the outcomes in $s_{\mathrm{c}}^2$ and $s_{\mathrm{t}}^2$, which the stratified design has removed, so it is conservative, often substantially; the stratified estimator of Theorem 7.3.1 should be used.

4. Prove Theorem 7.4.1 for $J = 2$ by computing the least squares estimator directly, and show that $\tau_\omega = \tau_{\mathrm{sp}}$ if $e(1) = e(2)$.

   **Answer** With two strata, by the Frisch–Waugh–Lovell theorem $\hat\tau^{\mathrm{ols}} = \sum_i(W_i - e(G_i))Y_i^{\mathrm{obs}}/\sum_i(W_i - e(G_i))^2$, with $e(j)$ the sample treated proportions. In stratum $j$, $\sum_{G_i = j}(W_i - e(j))^2 = N(j)e(j)(1 - e(j))$ and $\sum_{G_i = j}(W_i - e(j))Y_i^{\mathrm{obs}} = N_{\mathrm{t}}(j)(1 - e(j))\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - N_{\mathrm{c}}(j)e(j)\bar Y_{\mathrm{c}}^{\mathrm{obs}}(j) = N(j)e(j)(1 - e(j))\hat\tau^{\mathrm{dif}}(j)$. Hence $\hat\tau^{\mathrm{ols}} = \sum_j\omega(j)\hat\tau^{\mathrm{dif}}(j)/\sum_j\omega(j)$ with $\omega(j) = q(j)e(j)(1 - e(j))$, and its limit is $\tau_\omega$. If $e(1) = e(2)$, $\omega(j) \propto q(j)$ and $\tau_\omega = \sum_j q(j)\tau_{\mathrm{sp}}(j) = \tau_{\mathrm{sp}}$.

5. Using Theorem 7.3.2, quantify the precision gain from stratifying on sex in a balanced experiment ($p = 1/2$, $q = 1/2$) when the outcome means differ by one within-stratum standard deviation between the sexes, for both potential outcomes, and the within-stratum variances are all $\sigma^2$.

   **Answer** Within-stratum terms: $N\operatorname{Var}(\hat\tau^{\mathrm{strat}}) = \sigma^2/(1/2) + \sigma^2/(1/2) = 4\sigma^2$. The gain is $q(1 - q)(\sigma^2/(1/2) + \sigma^2/(1/2)) = \frac{1}{4} \cdot 4\sigma^2 = \sigma^2$, so the CRE has $N\operatorname{Var} = 5\sigma^2$. Stratification reduces the variance by $20\%$ (the standard error by about $11\%$), equivalent to a $25\%$ larger CRE.

6. In a PRE, show that $\widehat{\operatorname{Var}}{}^{\mathrm{pair}}$ is unbiased if the treatment effect is constant across pairs, even when it varies within pairs. Construct a two-pair example in which the estimator is biased upwards.

   **Answer** By Theorem 7.6.1(3) the bias is $\frac{1}{J(J - 1)}\sum_j(\tau^{\mathrm{pair}}(j) - \tau_{\mathrm{fs}})^2$, which vanishes when all pair averages $\tau^{\mathrm{pair}}(j)$ are equal, whatever the effects of the individual units. Example: pair 1 with $Y(0) = Y(1) = 0$ for both units, pair 2 with $Y(0) = 0$, $Y(1) = 4$ for both units. Then $\hat\tau^{\mathrm{pair}}(1) = 0$ and $\hat\tau^{\mathrm{pair}}(2) = 4$ under every assignment, the true variance is $0$, but $\widehat{\operatorname{Var}}{}^{\mathrm{pair}} = \frac{1}{2}\bigl((0 - 2)^2 + (4 - 2)^2\bigr) = 4$ always. The whole value is bias, as the theorem says: here $\tau^{\mathrm{pair}}(1) = 0$, $\tau^{\mathrm{pair}}(2) = 4$ and $\tau_{\mathrm{fs}} = 2$.

7. In the Electric Company data, carry out Fisher's test of the sharp null hypothesis with the statistic $T = \lvert\frac{1}{J}\sum_j\hat\tau^{\mathrm{pair}}(j)\rvert$. How many sign patterns give a value at least as large as the observed $13.4$?

   **Answer** Under $H_0$ each difference keeps or flips its sign with probability $1/2$, giving $2^8 = 256$ equally likely values of $\sum_j\pm\lvert\hat\tau^{\mathrm{pair}}(j)\rvert$. The observed sum is $107.4$; the absolute differences are $6.0, 1.0, 9.6, 26.3, 15.3, 19.1, 2.8, 34.9$, with total $115.0$. A sign pattern gives $\lvert\text{sum}\rvert \ge 107.4$ only if the flipped differences have total at most $(115.0 - 107.4)/2 = 3.8$, that is, flipping nothing, $\{1.0\}$, $\{2.8\}$ or $\{1.0, 2.8\}$; together with the four mirror-image patterns this is $8$ patterns. The exact p-value is $8/256 = 0.031$.

8. When would you not stratify? Discuss in terms of Theorem 7.3.2 and of the practical requirements of the design.

   **Answer** In the super-population setting of Theorem 7.3.2 stratification never loses precision, so the reasons are practical: the stratifying variable must be measured before the assignment; with very many small strata, strata with a single treated or control unit leave the within-stratum variance unestimable (the pair problem of Theorem 7.6.1) and degrees of freedom are lost; and if the variable is unrelated to the outcomes the gain is zero while the design and analysis become more complicated. A design with many covariates may be better served by stratifying on a few strong predictors and adjusting for the rest by regression ([3.9.5](/3.9.5)), or by rerandomization ([3.9.15](/3.9.15)).
