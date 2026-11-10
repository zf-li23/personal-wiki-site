---
title: "Completely Randomized Experiments: Fisher's Exact P-Values"
description: Fisher's approach to completely randomized experiments. The honey experiment; Fisher's sharp null hypothesis and the imputation of all missing potential outcomes; test statistics (difference in means, quantiles, t-statistic, normalized ranks, model-based and Kolmogorov–Smirnov statistics, combinations); the exact p-value by enumeration and its validity, Monte Carlo approximation, the finite population central limit theorem and the link to two-sample t-tests; covariates in the test statistic; and Fisher intervals by test inversion.
---

From this chapter to [3.9.7](/3.9.7) we study randomized experiments, the setting in which the assignment mechanism is known because the researcher chose it. The simplest case is the completely randomized experiment (CRE) of [3.9.2](/3.9.2): $N_{\mathrm{t}}$ of the $N$ units are drawn at random for the treatment. Four approaches to inference in a CRE are developed in this and the next three chapters.

| Approach | Question | Estimand or hypothesis | Source of randomness | Chapter |
|---|---|---|---|---|
| Fisher's exact p-value | Is there any effect at all? | sharp null: $Y_i(1) = Y_i(0)$ for all $i$ | assignment only | [3.9.3](/3.9.3) |
| Neyman's repeated sampling | How large is the average effect? | $\tau_{\mathrm{fs}}$ or $\tau_{\mathrm{sp}}$ | assignment (and sampling) | [3.9.4](/3.9.4) |
| Regression | Average effect, adjusting for covariates | $\tau_{\mathrm{sp}}$ | sampling and assignment | [3.9.5](/3.9.5) |
| Model-based imputation | Any estimand, through the distribution of the missing outcomes | any $\tau(\boldsymbol{Y}(0), \boldsymbol{Y}(1), \boldsymbol{X}, \boldsymbol{W})$ | posterior distribution | [3.9.6](/3.9.6) |

Fisher's approach is the oldest and requires the fewest assumptions. Its idea is that under the hypothesis that the treatment has no effect on any unit, all potential outcomes are known, and the only remaining randomness is the assignment, whose distribution the researcher controls. The distribution of any test statistic under the hypothesis can therefore be computed exactly, without any model for the outcomes and without large-sample approximations. This is the reasoning behind Fisher's lady tasting tea ([3.8.1](/3.8.1)), and it is a **permutation test** ([3.6.1](/3.6.1)) whose justification is the actual randomization rather than an assumption about the data.

## 3.1. The Honey Experiment and the Sharp Null Hypothesis

### 3.1.1. The Data

Our running example is a randomized trial of honey as a treatment for nighttime cough in children with upper respiratory infections, from the honey and the no-treatment arms of a study by Paul et al. (2007).

| | |
|---|---|
| Units | $N = 72$ children |
| Treatment | a single dose of buckwheat honey before bedtime |
| Control | no active treatment |
| Assignment | completely randomized, $N_{\mathrm{t}} = 35$, $N_{\mathrm{c}} = 37$ |
| Outcomes | cough frequency afterwards (cfa) and cough severity afterwards (csa) |
| Covariates | cough frequency prior (cfp) and cough severity prior (csp) |

All four variables are measured on a scale from 0 ("not at all frequent/severe") to 6 ("extremely frequent/severe"). The covariates are measured on the night before the treatment. To illustrate the calculations, we use the first six units, with cough frequency as the outcome.

| Unit | $Y_i(0)$ | $Y_i(1)$ | $W_i$ | $X_i$ (cfp) | $Y_i^{\mathrm{obs}}$ (cfa) |
|---|---|---|---|---|---|
| 1 | ? | 3 | 1 | 4 | 3 |
| 2 | ? | 5 | 1 | 6 | 5 |
| 3 | ? | 0 | 1 | 4 | 0 |
| 4 | 4 | ? | 0 | 4 | 4 |
| 5 | 0 | ? | 0 | 1 | 0 |
| 6 | 1 | ? | 0 | 5 | 1 |

Half of the potential outcomes are missing, which is the fundamental problem of [3.9.1](/3.9.1) in concrete form.

### 3.1.2. Fisher's Sharp Null Hypothesis

**Definition 3.1.1 (Fisher's Sharp Null Hypothesis)** **Fisher's sharp null hypothesis** is the hypothesis that the treatment has no effect on any unit,

$$
H_0\colon\ Y_i(0) = Y_i(1) \quad \text{for all } i = 1, \dots, N.
$$
More generally, a null hypothesis is sharp if, together with the observed data, it determines all missing potential outcomes.

The sharp null is much stronger than the hypothesis that the average effect is zero, $\tau_{\mathrm{fs}} = 0$, which allows positive effects for some units to cancel negative effects for others; the latter is sometimes called Neyman's weak null hypothesis and is the subject of [3.9.4](/3.9.4). The strength of the sharp null is what makes Fisher's approach possible: under $H_0$ we can fill in every missing potential outcome, $Y_i^{\mathrm{mis}} = Y_i^{\mathrm{obs}}$.

| Unit | $Y_i(0)$ | $Y_i(1)$ | $W_i$ | $X_i$ | $Y_i^{\mathrm{obs}}$ |
|---|---|---|---|---|---|
| 1 | (3) | 3 | 1 | 4 | 3 |
| 2 | (5) | 5 | 1 | 6 | 5 |
| 3 | (0) | 0 | 1 | 4 | 0 |
| 4 | 4 | (4) | 0 | 4 | 4 |
| 5 | 0 | (0) | 0 | 1 | 0 |
| 6 | 1 | (1) | 0 | 5 | 1 |

The values in parentheses are imputed under $H_0$. Other sharp null hypotheses are a constant additive effect, $Y_i(1) = Y_i(0) + C$ for all $i$, and a constant multiplicative effect, $Y_i(1) = C \cdot Y_i(0)$ for all $i$, with a specified constant $C$; under either, $Y_i^{\mathrm{mis}}$ again follows from $Y_i^{\mathrm{obs}}$ and $W_i$. Fisher's approach applies to all of them, and Section 3.5 uses them to build intervals.

### 3.1.3. The Three Steps

Fisher's exact p-value is obtained in three steps:

1. specify a sharp null hypothesis;
2. choose a test statistic, a known real-valued function $T(\boldsymbol{W}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{X})$ of everything we observe;
3. measure how extreme the observed value of the statistic is, by comparing it with its exact distribution under $H_0$, obtained by enumerating all possible assignments.

The first step was just discussed. The next two sections take up the second and third.

## 3.2. Test Statistics

### 3.2.1. Statistics Based on Differences of Location

Under the sharp null all potential outcomes are fixed, so a **test statistic** $T(\boldsymbol{W}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{X})$ becomes a function of the random assignment $\boldsymbol{W}$ alone. Any statistic gives a valid test; the choice affects only the power against the alternatives one cares about. The most common choice is the absolute difference in average outcomes between the groups,

$$
T^{\mathrm{dif}} = \bigl\lvert \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} \bigr\rvert = \left\lvert \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1} Y_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0} Y_i^{\mathrm{obs}} \right\rvert,
$$
which has good power against a constant additive effect $H_1\colon Y_i(1) = Y_i(0) + C$. The absolute value makes the test two-sided; without it, the test is one-sided. Variations of the same idea are:

- the difference in average logarithms, $T^{\log} = \bigl\lvert \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\ln Y_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\ln Y_i^{\mathrm{obs}} \bigr\rvert$ for positive outcomes, suited to a constant multiplicative effect $Y_i(1) = C \cdot Y_i(0)$;
- differences of medians or other quantiles, $T^{\mathrm{median}} = \lvert \operatorname{med}_{\mathrm{t}}(Y_i^{\mathrm{obs}}) - \operatorname{med}_{\mathrm{c}}(Y_i^{\mathrm{obs}}) \rvert$ and $T^{\mathrm{quant}} = \lvert q_{\delta,\mathrm{t}}(Y_i^{\mathrm{obs}}) - q_{\delta,\mathrm{c}}(Y_i^{\mathrm{obs}}) \rvert$, where $q_{\delta,\mathrm{t}}$ is the $\delta$ quantile in the treatment group, which are insensitive to outliers;
- the $t$-statistic
  $$
  T^{\text{t-stat}} = \left\lvert \frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}}} \right\rvert, \qquad
  s_{\mathrm{t}}^2 = \frac{1}{N_{\mathrm{t}} - 1}\sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2,
  $$
  with $s_{\mathrm{c}}^2$ defined in the same way, which accounts for unequal variances in the two groups. Used inside Fisher's approach it is just another statistic; its $t$ distribution is not needed.

### 3.2.2. Rank Statistics

Outliers and skewed distributions reduce the power of the difference in means. Replacing the outcomes by their ranks gives statistics that are insensitive to both. Ranks are the subject of [3.6.2](/3.6.2); here we only need a version centered at zero that handles ties by averaging.

**Definition 3.2.1 (Normalized Rank)** The normalized rank of unit $i$ among the observed outcomes is

$$
R_i = R_i\bigl(Y_1^{\mathrm{obs}}, \dots, Y_N^{\mathrm{obs}}\bigr) = \sum_{j=1}^{N}\boldsymbol{1}\bigl\{Y_j^{\mathrm{obs}} < Y_i^{\mathrm{obs}}\bigr\} + \frac{1}{2}\left(1 + \sum_{j=1}^{N}\boldsymbol{1}\bigl\{Y_j^{\mathrm{obs}} = Y_i^{\mathrm{obs}}\bigr\}\right) - \frac{N + 1}{2}.
$$
The rank statistic is the absolute difference of the average normalized ranks,

$$
T^{\operatorname{rank}} = \bigl\lvert \bar R_{\mathrm{t}} - \bar R_{\mathrm{c}} \bigr\rvert = \left\lvert \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1} R_i - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0} R_i \right\rvert.
$$

The first two terms give the usual rank, with tied observations receiving the average of the ranks they occupy, and subtracting $(N + 1)/2$ makes the ranks sum to zero. Since the ranks are a function of the observed outcomes, which are fixed under the sharp null, $T^{\operatorname{rank}}$ is a function of $\boldsymbol{W}$ only and its null distribution is computed in the same way as that of $T^{\mathrm{dif}}$. This test is equivalent to the **Wilcoxon rank-sum test** of [3.2.6](/3.2.6): with $N_{\mathrm{t}}$ fixed, the sum of the treated ranks is a linear function of $\bar R_{\mathrm{t}} - \bar R_{\mathrm{c}}$. Among the first six honey units the observed outcomes $(3, 5, 0, 4, 0, 1)$ have ranks $(4, 6, 1.5, 5, 1.5, 3)$ and normalized ranks $(0.5, 2.5, -2, 1.5, -2, -0.5)$, so $T^{\operatorname{rank}} = \lvert 1/3 - (-1/3) \rvert = 2/3$.

### 3.2.3. Model-Based and Distributional Statistics

A statistic can also be derived from a model that is believed to approximate the distribution of the potential outcomes under some alternative. For example, if $Y_i(0) \sim \mathcal{N}(\mu_{\mathrm{c}}, \sigma_{\mathrm{c}}^2)$ and $Y_i(1) \sim \mathcal{N}(\mu_{\mathrm{t}}, \sigma_{\mathrm{t}}^2)$, the statistic can be the maximum likelihood estimate of $\mu_{\mathrm{t}} - \mu_{\mathrm{c}}$, possibly standardized; if $\ln Y_i(0) \sim \mathcal{N}(\mu_{\mathrm{c}}, \sigma_{\mathrm{c}}^2)$ and $\ln Y_i(1) \sim \mathcal{N}(\mu_{\mathrm{t}}, \sigma_{\mathrm{t}}^2)$, the corresponding estimate under the log-normal model. The model is used only to choose the statistic. The test remains exact even if the model is wrong, because the null distribution comes from the randomization; a wrong model only costs power.

To detect any difference between the distributions of the outcomes in the two groups, and not only a shift, one can use the Kolmogorov–Smirnov statistic

$$
T^{\mathrm{ks}} = \sup_y \bigl\lvert \hat F_{\mathrm{t}}(y) - \hat F_{\mathrm{c}}(y) \bigr\rvert, \qquad
\hat F_{\mathrm{t}}(y) = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\boldsymbol{1}\bigl\{Y_i^{\mathrm{obs}} \le y\bigr\},
$$
with $\hat F_{\mathrm{c}}$ defined in the same way: the maximal distance between the empirical distribution functions, as in the two-sample **Kolmogorov–Smirnov test** of [3.2.6](/3.2.6).

### 3.2.4. Choosing a Statistic by Power

Since every statistic gives a valid test, the choice should be governed by power: the probability of rejecting $H_0$ when it is false, against the alternatives that are plausible in the application. A simulation study compares the difference in means, the difference in medians and the rank statistic at level $\alpha = 0.1$ under three models: an additive effect with normal outcomes, an additive effect with outliers, and a multiplicative effect with log-normal outcomes.

![Power of Fisher's exact test at level 0.1 for the difference in means, the difference in medians and the rank statistic, against the effect size, under an additive normal model, an additive model with outlying observations, and a multiplicative log-normal model; simulated data](./plots/fep_power.py)

The results follow a clear pattern.

- With normal outcomes, the difference in means is the best of the three, but the rank statistic is almost as powerful; the median is clearly worse.
- With outliers, the difference in means loses much of its power, while the rank and median statistics are barely affected.
- With multiplicative effects on skewed outcomes, the rank statistic is again close to the best.

The rank statistic is therefore an attractive default: it has relatively good power in all settings and is robust to the form of the outcome distribution. The other statistics perform well only in the settings that play to their advantages, at the expense of relatively poor power elsewhere.

### 3.2.5. Statistics with Several Components

Sometimes there are several alternatives of interest (a difference in means and a difference in variances, say) or several outcomes per unit (cough frequency and severity in the honey experiment). Testing each separately with its own statistic and combining the conclusions informally runs into the multiple testing problem: with two tests at level $\alpha$, the probability that at least one rejects under $H_0$ exceeds $\alpha$. Within Fisher's framework the natural solution is to combine the components into a single statistic, $T^{\mathrm{comb}} = g(T^1, T^2)$, and compute its exact null distribution in the usual way. A standard choice for two outcomes is a statistic of the form of **Hotelling's T² statistic**,

$$
T^{\mathrm{Hotelling}} =
\begin{pmatrix} \bar Y_{\mathrm{t},1}^{\mathrm{obs}} - \bar Y_{\mathrm{c},1}^{\mathrm{obs}} \\ \bar Y_{\mathrm{t},2}^{\mathrm{obs}} - \bar Y_{\mathrm{c},2}^{\mathrm{obs}} \end{pmatrix}^{\mathsf T}
\left(\frac{\hat\Sigma_{\mathrm{c}}}{N_{\mathrm{c}}} + \frac{\hat\Sigma_{\mathrm{t}}}{N_{\mathrm{t}}}\right)^{-1}
\begin{pmatrix} \bar Y_{\mathrm{t},1}^{\mathrm{obs}} - \bar Y_{\mathrm{c},1}^{\mathrm{obs}} \\ \bar Y_{\mathrm{t},2}^{\mathrm{obs}} - \bar Y_{\mathrm{c},2}^{\mathrm{obs}} \end{pmatrix},
$$
where $\hat\Sigma_{\mathrm{t}}$ and $\hat\Sigma_{\mathrm{c}}$ are the sample covariance matrices of the two outcomes in the two groups. Because the null hypothesis is that neither outcome is affected for any unit, a single randomization distribution covers both components and the level is exactly $\alpha$.

## 3.3. Computing the P-Value

### 3.3.1. The Exact P-Value

**Definition 3.3.1 (Fisher's Exact P-Value)** Let $T^{\mathrm{obs}} = T(\boldsymbol{W}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{X})$ be the observed value of the statistic. Under a sharp null hypothesis, let $T(\boldsymbol{w})$ denote the value the statistic would take under assignment $\boldsymbol{w}$, computed from the imputed potential outcomes. **Fisher's exact p-value** is

$$
p = \mathbb{P}_W\bigl(T(\boldsymbol{W}) \ge T^{\mathrm{obs}}\bigr) = \sum_{\boldsymbol{w} \in \mathcal{W}^+} \mathbb{P}(\boldsymbol{W} = \boldsymbol{w}) \, \boldsymbol{1}\bigl\{T(\boldsymbol{w}) \ge T^{\mathrm{obs}}\bigr\},
$$
which in a CRE is the fraction of the $\binom{N}{N_{\mathrm{t}}}$ possible assignments that give a value at least as large as the observed one.

The p-value answers the question: how unusual is the observed value of the statistic, if the null hypothesis is true? The distribution of $T(\boldsymbol{W})$ over the random assignment is the exact null distribution of the statistic. Its only source of randomness is the assignment vector, which is the reason why the result is exact for any sample size: it involves neither a model for the outcomes nor an asymptotic approximation.

**Example 3.3.1** For the six honey units, $\boldsymbol{W}^{\mathrm{obs}} = (1, 1, 1, 0, 0, 0)$ and $T^{\mathrm{dif}, \mathrm{obs}} = \lvert (3 + 5 + 0)/3 - (4 + 0 + 1)/3 \rvert = \lvert 8/3 - 5/3 \rvert = 1$. Under the sharp null the outcomes $(3, 5, 0, 4, 0, 1)$ are fixed, and each of the $\binom{6}{3} = 20$ assignments with three treated units has probability $1/20$. Enumerating them gives the null distribution of $T^{\mathrm{dif}}$:

| $T^{\mathrm{dif}}$ | $1/3$ | $1$ | $5/3$ | $7/3$ | $11/3$ |
|---|---|---|---|---|---|
| Number of assignments | 4 | 6 | 6 | 2 | 2 |

Sixteen of the twenty assignments give $T^{\mathrm{dif}} \ge 1$, so $p = 16/20 = 0.80$. The rank statistic, with $T^{\operatorname{rank}, \mathrm{obs}} = 2/3$, has null distribution

| $T^{\operatorname{rank}}$ | $0$ | $2/3$ | $1$ | $4/3$ | $5/3$ | $7/3$ | $3$ |
|---|---|---|---|---|---|---|---|
| Number of assignments | 4 | 4 | 2 | 4 | 2 | 2 | 2 |

and again $p = 16/20 = 0.80$. There is no evidence against the hypothesis of no effect.

![Exact null distribution of the absolute difference in means over the 20 assignments of the six honey units, with the observed value 1 marked; and the randomization distribution of the difference in means for a simulated experiment with 72 units, with its normal approximation from the finite population central limit theorem](./plots/fep_null_distribution.py)

:::

Is this result consistent with intuition? Unit 2, treated, had the highest prior cough frequency and still coughed a lot afterwards, while unit 4, a control, had a high prior frequency and a high outcome; the treated and control units differ in their prior cough as much as in their outcomes. More fundamentally, six units cannot provide much evidence. Each assignment and its complement (treated and control swapped) give the same value of $\lvert\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\rvert$, so every value of the statistic occurs at least twice and the smallest attainable p-value is $2/20 = 0.10$: with $N = 6$ and $N_{\mathrm{t}} = 3$, no outcome whatever could lead to rejection at the $5\%$ level. A test with no power cannot be expected to detect an effect, and a large p-value is not evidence that there is none.

The exact p-value deserves its name because it controls the level exactly, whatever the statistic and the sample size.

**Theorem 3.3.1 (Validity of Fisher's Exact Test)** Under the sharp null hypothesis, for every $\alpha \in [0, 1]$,

$$
\mathbb{P}_W(p \le \alpha) \le \alpha,
$$
with equality when $\alpha$ is one of the values that $p$ can take.

**Proof** Under $H_0$ the function $\boldsymbol{w} \mapsto T(\boldsymbol{w})$ on $\mathcal{W}^+$ is fixed, and the observed statistic is $T(\boldsymbol{W})$ with $\boldsymbol{W}$ drawn from the assignment mechanism. Let $G(t) = \mathbb{P}_W(T(\boldsymbol{W}) \ge t)$, a non-increasing function, so that $p = G(T(\boldsymbol{W}))$. Let $t^* = \min\{t \in T(\mathcal{W}^+) : G(t) \le \alpha\}$, the smallest attained value of the statistic whose tail probability is at most $\alpha$ (if there is none, $\mathbb{P}_W(p \le \alpha) = 0$). Since $G$ is non-increasing, $p \le \alpha$ if and only if $T(\boldsymbol{W}) \ge t^*$, and therefore $\mathbb{P}_W(p \le \alpha) = G(t^*) \le \alpha$. If $\alpha$ is an attained value of $p$, then $G(t^*) = \alpha$. $\square$

### 3.3.2. Approximation by Simulation

Exact enumeration quickly becomes infeasible: for the full honey data there are $\binom{72}{35} \approx 4.4 \times 10^{20}$ assignments. A precise approximation is obtained by simulation. Draw $K$ assignment vectors $\boldsymbol{W}^1, \dots, \boldsymbol{W}^K$ independently from the assignment mechanism, compute the statistic for each, and estimate the p-value by

$$
\hat p = \frac{1}{K}\sum_{k=1}^{K}\boldsymbol{1}\bigl\{T(\boldsymbol{W}^k) \ge T^{\mathrm{obs}}\bigr\}.
$$
The indicators are independent Bernoulli variables with success probability $p$, the true p-value, so $\hat p$ is unbiased with standard error

$$
\sqrt{\frac{p(1 - p)}{K}} \le \frac{1}{2\sqrt{K}},
$$
because $p(1 - p) \le 1/4$. With $K = 10{,}000$ draws the standard error is at most $0.005$, and with $K = 10^6$ at most $0.0005$, whatever the number of units. For the honey data and the rank statistic the estimated p-values are:

| Number of draws $K$ | 100 | 1,000 | 10,000 | 100,000 | 1,000,000 |
|---|---|---|---|---|---|
| $\hat p$ | 0.010 | 0.044 | 0.044 | 0.042 | 0.043 |
| Estimated standard error | 0.010 | 0.006 | 0.002 | 0.001 | 0.000 |

With a million draws, $p \approx 0.043$: the data provide moderate evidence that honey affects cough frequency for at least some children.

### 3.3.3. Large-Sample Approximations

For the difference in means, the null distribution has a simple large-sample approximation. Under $H_0$, write $y_i = Y_i(0) = Y_i(1)$, $\bar y = \frac{1}{N}\sum_i y_i$ and $S^2 = \frac{1}{N - 1}\sum_{i=1}^{N}(y_i - \bar y)^2$, all of them fixed.

**Theorem 3.3.2** In a CRE, under Fisher's sharp null hypothesis,

$$
\mathbb{E}_W\bigl[\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr] = 0, \qquad
\operatorname{Var}_W\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr) = \frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}}\,S^2.
$$

**Proof** Under $H_0$ the treated group is a simple random sample of size $N_{\mathrm{t}}$, drawn without replacement from the fixed values $y_1, \dots, y_N$, and $\bar Y_{\mathrm{t}}^{\mathrm{obs}}$ is its mean. From sampling theory, $\mathbb{E}_W[\bar Y_{\mathrm{t}}^{\mathrm{obs}}] = \bar y$ and $\operatorname{Var}_W(\bar Y_{\mathrm{t}}^{\mathrm{obs}}) = (1/N_{\mathrm{t}} - 1/N)S^2 = \frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}S^2$ (this also follows from Lemma 4.3.1). Since $N_{\mathrm{t}}\bar Y_{\mathrm{t}}^{\mathrm{obs}} + N_{\mathrm{c}}\bar Y_{\mathrm{c}}^{\mathrm{obs}} = N\bar y$,

$$
\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \frac{N\bar y - N_{\mathrm{t}}\bar Y_{\mathrm{t}}^{\mathrm{obs}}}{N_{\mathrm{c}}} = \frac{N}{N_{\mathrm{c}}}\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar y\bigr).
$$
Hence the expectation is zero and the variance is $\frac{N^2}{N_{\mathrm{c}}^2}\cdot\frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}S^2 = \frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}}S^2$. $\square$

The **central limit theorem** of [3.1.13](/3.1.13) concerns independent observations, but the treated outcomes of a CRE are drawn without replacement from a finite population and are dependent. The appropriate version is due to Hájek (1960).

**Theorem 3.3.3 (Finite Population Central Limit Theorem)** Let $\bar y_n$ be the mean of a simple random sample of size $n$ drawn without replacement from a finite population $y_1, \dots, y_N$ with mean $\bar y$ and variance $S^2 = \frac{1}{N - 1}\sum_i (y_i - \bar y)^2$, and consider a sequence of such populations with $N \to \infty$. If

$$
\frac{1}{\min(n, N - n)} \cdot \frac{\max_{1 \le i \le N}(y_i - \bar y)^2}{S^2} \to 0,
$$
then

$$
\frac{\bar y_n - \bar y}{\sqrt{(1/n - 1/N)S^2}} \xrightarrow{d} \mathcal{N}(0, 1).
$$

The condition says that both the sample and its complement grow and that no single value dominates the variance; it holds, for example, when $n/N$ stays bounded away from $0$ and $1$ and the outcomes are bounded, as in the honey data. Applied to the treated group and combined with Theorem 3.3.2, it gives under $H_0$

$$
\frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{\frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}}S^2}} \xrightarrow{d} \mathcal{N}(0, 1), \qquad N \to \infty.
$$
Since $S^2$ is fixed under $H_0$, this standardized statistic is a monotone function of $T^{\mathrm{dif}}$ and gives the same exact test; the normal distribution approximates its null distribution in large samples, as the right panel of the figure in Example 3.3.1 shows.

This explains why Fisher's test and the classical two-sample $t$-tests give similar answers in large randomized experiments, although the $t$-tests assume normally distributed outcomes. The equal-variance **two-sample t-test** uses

$$
\frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{\frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}(N - 2)}\Bigl[\sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2 + \sum_{i:W_i = 0}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2\Bigr]}} \sim t_{N-2}
$$
under normality. Compare it with the decomposition of the total sum of squares under $H_0$,

$$
(N - 1)S^2 = \sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2 + \sum_{i:W_i = 0}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2 + \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2.
$$
The last term is of order one, while the within-group sums are of order $N$, so with large $N$ the pooled variance estimate in the $t$-statistic is close to $S^2$, and the $t$-test p-value (computed in R by `t.test` with `var.equal = TRUE`) is close to the p-value from the finite population central limit theorem. In the same way, under $H_0$,

$$
\frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}}} \xrightarrow{d} \mathcal{N}(0, 1),
$$
so the unequal-variance **Welch's t-test** (`var.equal = FALSE`) is also approximately valid. The R functions `wilcox.test` and `ks.test` compute exact or asymptotic p-values for the rank and Kolmogorov–Smirnov statistics. For the six honey units:

```r
y_obs <- c(3, 5, 0, 4, 0, 1)
w <- c(1, 1, 1, 0, 0, 0)
yt <- y_obs[w == 1]; yc <- y_obs[w == 0]

t.test(yt, yc, var.equal = TRUE)     # pooled two-sample t-test
t.test(yt, yc, var.equal = FALSE)    # Welch t-test
wilcox.test(yt, yc)                  # rank-sum test (normal approximation with ties)
ks.test(yt, yc)                      # two-sample Kolmogorov-Smirnov test

# Fisher's exact p-value by enumerating all 20 assignments
assignments <- combn(6, 3)
t_dif <- apply(assignments, 2, function(tr) abs(mean(y_obs[tr]) - mean(y_obs[-tr])))
t_obs <- abs(mean(yt) - mean(yc))
mean(t_dif >= t_obs - 1e-12)         # 0.8
```

With six units the asymptotic approximations are poor, and only the enumeration gives the exact answer $0.80$; with ties among the outcomes, `wilcox.test` falls back to a normal approximation, whereas Fisher's approach handles ties through the normalized ranks without any change.

## 3.4. Using Covariates

Covariates do not change the validity of Fisher's approach, but they can increase its power considerably, because they allow the statistic to remove part of the variation in the outcomes that is unrelated to the treatment. Three ways of using a pre-treatment covariate $X_i$ are common.

- Gain scores. Define new potential outcomes $Y_i'(w) = Y_i(w) - X_i$ for $w = 0, 1$, with observed values $Y_i'^{,\mathrm{obs}} = Y_i^{\mathrm{obs}} - X_i$. Since $X_i$ is not affected by the treatment, the sharp null for $Y$ is equivalent to the sharp null for $Y'$, and we may use
  $$
  T^{\mathrm{gain}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}Y_i'^{,\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}Y_i'^{,\mathrm{obs}} = \bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr) - \bigl(\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}}\bigr).
  $$
  The correction term $\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}}$ is zero on average over the randomization, but not in a given assignment; subtracting it removes the part of the outcome difference that is due to a chance imbalance in the covariate. If $X_i$ and the outcomes are strongly correlated, the variance of $T^{\mathrm{gain}}$ is much smaller than that of the plain difference.
- Proportional changes, $Y_i'(w) = (Y_i(w) - X_i)/X_i$, for positive covariates and outcomes on a ratio scale.
- Regression coefficients. Regress $Y_i^{\mathrm{obs}}$ on an intercept, $W_i$ and $X_i$ by least squares and use the estimated coefficient on $W_i$ as the statistic, $T^{\mathrm{reg\text{-}coef}}$.

The last option raises several questions. What if the regression model is wrong? The test is still valid, because the null distribution is computed from the randomization by recomputing the coefficient for each assignment; the model only defines a function of the data. Is it more effective? Usually, if the covariate predicts the outcome well. What is the causal meaning of the coefficient? Within Fisher's approach none is needed: the coefficient is just a statistic. Its interpretation as an estimate of the average effect is the subject of [3.9.5](/3.9.5).

For the full honey data, with $10^6$ simulated assignments, the statistics give the following values and p-values. The values are shown with their signs (treated minus control); the p-values are two-sided, $p = \mathbb{P}_W(\lvert T\rvert \ge \lvert T^{\mathrm{obs}}\rvert)$, and $T^{\operatorname{rank}}$ is the difference of the average ranks.

| Statistic | Value | p-value |
|---|---|---|
| $T^{\mathrm{dif}}$ | $-0.697$ | 0.067 |
| $T^{\mathrm{quant}}$, $\delta = 0.25$ | $-1.000$ | 0.440 |
| $T^{\mathrm{quant}}$, $\delta = 0.50$ | $-1.000$ | 0.637 |
| $T^{\mathrm{quant}}$, $\delta = 0.75$ | $-1.000$ | 0.576 |
| $T^{\text{t-stat}}$ | $-1.869$ | 0.065 |
| $T^{\operatorname{rank}}$ | $-9.785$ | 0.043 |
| $T^{\mathrm{ks}}$ | $0.304$ | 0.021 |
| $T^{\mathrm{gain}}$ | $-0.967$ | 0.006 |
| $T^{\mathrm{reg\text{-}coef}}$ | $-0.911$ | 0.008 |

The statistics that ignore the covariate give p-values between about $0.02$ and $0.6$; the quantile statistics have little power because the outcomes take only seven values, so that quantiles change in jumps. The two statistics that use the prior cough frequency give p-values below $0.01$. This reflects the strong correlation between prior and subsequent cough frequency: once the children's baseline differences are taken into account, the effect of honey stands out much more clearly.

## 3.5. Fisher Intervals

Fisher's approach tests hypotheses; it does not estimate effects. An interval for the effect can nevertheless be obtained by inverting a family of tests. Consider the sharp null hypotheses of a constant additive effect,

$$
H_0(C)\colon\ Y_i(1) = Y_i(0) + C \quad \text{for } i = 1, \dots, N.
$$
Under $H_0(C)$ the missing outcomes are $Y_i(0) = Y_i^{\mathrm{obs}} - C$ for treated units and $Y_i(1) = Y_i^{\mathrm{obs}} + C$ for control units, and a suitable statistic is $\lvert \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} - C \rvert$ (or the rank statistic computed from the adjusted outcomes $Y_i^{\mathrm{obs}} - CW_i$, which are the control potential outcomes under $H_0(C)$). Computing the exact p-value for each $C$ on a grid, the set of values of $C$ that are not rejected at level $\alpha$ is a $1 - \alpha$ Fisher interval for the constant effect.

**Definition 3.5.1 (Fisher Interval)** A **Fisher interval** at level $1 - \alpha$ is the set of constants $C$ for which Fisher's exact test of the sharp null hypothesis $H_0(C)$ does not reject at level $\alpha$.

By Theorem 3.3.1, if the effect really is constant and equal to $C_0$, the test of $H_0(C_0)$ rejects with probability at most $\alpha$, so the interval contains $C_0$ with probability at least $1 - \alpha$. For the honey data with cough frequency as the outcome, the p-values based on $T^{\mathrm{dif}}$ equal $0.05$ at about $C = -1.44$ and $C = 0.06$, giving the $95\%$ Fisher interval $[-1.44, 0.06]$; at $C = 0$ the p-value is $0.067$, consistent with the test of Section 3.4. The rank statistic gives an interval with endpoints near $-2$ and $0$; its p-values are piecewise constant in $C$, because with integer outcomes the ranks of $Y_i^{\mathrm{obs}} - CW_i$ change only at isolated values of $C$. The interpretation of a Fisher interval rests on the assumption of a constant effect; when effects vary across units, the average effect is better studied with Neyman's approach in [3.9.4](/3.9.4).

## Summary

- Fisher's approach tests a sharp null hypothesis, typically no effect for any unit: $H_0\colon Y_i(0) = Y_i(1)$ for all $i$ (Definition 3.1.1). Under it all missing potential outcomes are known, and the only randomness is the assignment.
- Three steps: sharp null; test statistic $T(\boldsymbol{W}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{X})$; exact p-value $p = \mathbb{P}_W(T(\boldsymbol{W}) \ge T^{\mathrm{obs}})$ by enumeration (Definition 3.3.1). The test is exact for any statistic and any sample size (Theorem 3.3.1).
- Statistics: any function of observed data is valid; choose by power.

  | Statistic | Good against |
  |---|---|
  | $T^{\mathrm{dif}}$, $T^{\text{t-stat}}$ | additive shifts, roughly normal outcomes |
  | $T^{\log}$ | multiplicative effects |
  | $T^{\mathrm{median}}$, $T^{\mathrm{quant}}$ | shifts with outliers |
  | $T^{\operatorname{rank}}$ (normalized ranks, Def. 3.2.1) | shifts, robust default |
  | $T^{\mathrm{ks}}$ | any difference in distribution |
  | $T^{\mathrm{gain}}$, $T^{\mathrm{reg\text{-}coef}}$ | shifts, using a predictive covariate |
  | $T^{\mathrm{comb}}$, Hotelling | several outcomes or alternatives |
- Computation: enumeration for small $N$ (six honey units: $p = 16/20 = 0.80$); otherwise $K$ random draws with standard error at most $1/(2\sqrt K)$. Under $H_0$, $\operatorname{Var}_W(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}) = \frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}}S^2$ (Theorem 3.3.2), and the finite population central limit theorem (Theorem 3.3.3) makes Fisher's test close to the two-sample $t$-tests in large samples.
- Covariates improve power without affecting validity (honey: $p = 0.067$ without, $0.006$ with the gain score). Fisher intervals invert tests of constant effects $H_0(C)$ (Definition 3.5.1).
- Limitations: the sharp null is restrictive, and rejecting it does not estimate the size of the effect; these are addressed by Neyman's approach.

## Questions

1. Four units are completely randomized with $N_{\mathrm{t}} = 2$; the observed outcomes are $Y^{\mathrm{obs}} = (7, 9, 2, 4)$ with $\boldsymbol{W}^{\mathrm{obs}} = (1, 1, 0, 0)$. Compute the exact null distribution of the one-sided statistic $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$ and the one-sided p-value. What is the smallest p-value this design can produce?

   **Answer** There are $\binom{4}{2} = 6$ assignments. With treated pairs $\{1,2\}, \{1,3\}, \{1,4\}, \{2,3\}, \{2,4\}, \{3,4\}$ the treated means are $8, 4.5, 5.5, 5.5, 6.5, 3$ and the control means $3, 6.5, 5.5, 5.5, 4.5, 8$, so the differences are $5, -2, 0, 0, 2, -5$. The observed value is $5$, the largest, and $p = 1/6 \approx 0.17$. This is the smallest possible one-sided p-value, so no data could give significance at the $10\%$ level.
2. Prove that in a CRE with $N_{\mathrm{t}} = N_{\mathrm{c}}$ the two-sided statistic $T^{\mathrm{dif}}$ takes each of its values at least twice, so that $p \ge 2/\binom{N}{N/2}$.

   **Answer** Let $\bar{\boldsymbol{w}} = \boldsymbol{1} - \boldsymbol{w}$ be the complementary assignment; it also has $N/2$ treated units, so it lies in $\mathcal{W}^+$, and it is different from $\boldsymbol{w}$. Under $H_0$ it swaps the groups, so the difference in means changes sign and $T^{\mathrm{dif}}(\bar{\boldsymbol{w}}) = T^{\mathrm{dif}}(\boldsymbol{w})$. Hence at least two assignments, the observed one and its complement, satisfy $T(\boldsymbol{w}) \ge T^{\mathrm{obs}}$, and $p \ge 2/\binom{N}{N/2}$.
3. How many random draws $K$ guarantee that the Monte Carlo standard error of a simulated p-value is at most $0.001$? If the true p-value is about $0.04$, how many draws are actually needed for this precision?

   **Answer** From $1/(2\sqrt K) \le 0.001$, $K \ge 250{,}000$. If $p \approx 0.04$, the standard error is $\sqrt{0.04 \times 0.96/K} \le 0.001$ when $K \ge 38{,}400$.
4. In the six-unit honey example, compute $T^{\mathrm{gain}}$ for the observed assignment, using $X = (4, 6, 4, 4, 1, 5)$. Why is the gain-score test still valid although $X$ is not a potential outcome?

   **Answer** The gains $Y_i^{\mathrm{obs}} - X_i$ are $(-1, -1, -4, 0, -1, -4)$; the treated mean is $-2$ and the control mean $-5/3$, so $T^{\mathrm{gain}} = -1/3$. Because $X_i$ is a covariate, unaffected by the treatment, the sharp null $Y_i(1) = Y_i(0)$ implies $Y_i(1) - X_i = Y_i(0) - X_i$; the gains are fixed under $H_0$, and their randomization distribution is computed exactly as for the original outcomes.
5. Explain the difference between the randomness in Fisher's exact test and in a permutation test of two independent samples. Under what assumption are the two computations identical?

   **Answer** In Fisher's test the units and their potential outcomes are fixed and the randomness is the assignment, whose distribution is known because the experimenter randomized; the reference distribution is justified by the design. In a permutation test of two samples, the randomness comes from sampling, and the permutation distribution is justified by the assumption that under the null hypothesis the observations are exchangeable (for example, i.i.d. from the same distribution). The computations coincide: both recompute the statistic for all ways of splitting the pooled observations into groups of sizes $N_{\mathrm{t}}$ and $N_{\mathrm{c}}$; they differ in what justifies the computation and in what the conclusion refers to.
6. Show that under $H_0$ the standardized statistic $(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}})/\sqrt{NS^2/(N_{\mathrm{t}}N_{\mathrm{c}})}$ and $T^{\mathrm{dif}}$ give the same exact p-value, but that the Welch statistic $T^{\text{t-stat}}$ in general does not.

   **Answer** Under $H_0$, $S^2$ is computed from all $N$ outcomes, which do not depend on the assignment, so the standardized statistic is $T^{\mathrm{dif}}$ divided by the same constant for every $\boldsymbol{w}$; the ordering of the assignments, and hence the p-value, is unchanged. The Welch denominator $\sqrt{s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}}$ depends on how the outcomes are split between the groups, so it changes from one assignment to another and can reorder them; it defines a different test.
7. Describe how you would compute a $90\%$ Fisher interval for a constant multiplicative effect $Y_i(1) = C \cdot Y_i(0)$ with positive outcomes.

   **Answer** For each $C > 0$ on a grid, impute $Y_i(0) = Y_i^{\mathrm{obs}}/C$ for treated units and $Y_i(1) = C\,Y_i^{\mathrm{obs}}$ for control units, so that the adjusted outcomes $Y_i^{\mathrm{obs}}/C^{W_i}$ are the fixed control outcomes under $H_0(C)$. Use a statistic such as the difference in mean logarithms of the adjusted outcomes, $\lvert \overline{\ln Y}_{\mathrm{t}} - \overline{\ln Y}_{\mathrm{c}} - \ln C \rvert$, compute its exact (or simulated) p-value, and keep all $C$ with $p > 0.10$. Equivalently, apply the additive procedure to $\ln Y_i^{\mathrm{obs}}$ and exponentiate the endpoints.
8. The honey data give $p = 0.067$ for $T^{\mathrm{dif}}$ and $p = 0.006$ for $T^{\mathrm{gain}}$. A colleague suggests reporting whichever statistic gives the smaller p-value. What is wrong with this, and what would be a valid way to use both?

   **Answer** Choosing the statistic after seeing the p-values makes the reported p-value the minimum of two p-values, which under $H_0$ is below $\alpha$ with probability greater than $\alpha$; the test is no longer exact. The statistic must be chosen before looking at the outcomes (it may use the covariates and the design). To use both, define a single combined statistic in advance, such as $T = \min(p^{\mathrm{dif}}, p^{\mathrm{gain}})$ treated as a statistic (smaller is more extreme), and compute its exact null distribution by recomputing both p-values for each assignment; or apply a Bonferroni correction.
