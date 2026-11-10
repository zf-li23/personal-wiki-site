---
title: "Completely Randomized Experiments: Neyman's Repeated Sampling Approach"
description: Neyman's approach to completely randomized experiments. The difference-in-means estimator and its unbiasedness for the finite-sample average treatment effect; the exact randomization variance, its proof and its representation through the correlation of the potential outcomes; the conservative Neyman variance estimator and its alternatives; large-sample confidence intervals and tests of the weak null hypothesis, illustrated with the honey data; and the super-population view with two layers of randomness.
---

Fisher's approach of [3.9.3](/3.9.3) answers a narrow question: is there any unit for which the treatment has an effect? Its sharp null hypothesis is restrictive, and rejecting it gives no estimate of how large the effect is. Neyman (1923), in the paper that introduced potential outcomes, asked a different question: what is the average effect of the treatment, and how precisely can a randomized experiment estimate it? His answer is the difference in average outcomes between the two groups, an estimator that is unbiased for the average treatment effect over the randomization alone, together with a variance formula, a conservative estimate of that variance, and large-sample confidence intervals. In this chapter the potential outcomes are first held fixed, so that the only randomness is the assignment of the completely randomized experiment (CRE); at the end the units are regarded as a sample from a super-population, which adds a second layer of randomness. The regression methods of [3.9.5](/3.9.5) and the stratified and paired designs of [3.9.7](/3.9.7) build on the results derived here.

## 4.1. Fisher's and Neyman's Approaches

| | Fisher | Neyman |
|---|---|---|
| Question | Is there any unit-level effect? | How large is the average effect? |
| Hypothesis or estimand | sharp null $Y_i(1) = Y_i(0)$ for all $i$ | $\tau_{\mathrm{fs}} = \bar Y(1) - \bar Y(0)$ (or $\tau_{\mathrm{sp}}$) |
| Missing outcomes | imputed exactly under $H_0$ | not imputed; only averages matter |
| Output | exact p-value | unbiased point estimate, variance, confidence interval |
| Randomness | assignment $\boldsymbol{W}$ | assignment, and in the super-population also sampling of the units |
| Inference | exact in finite samples | approximate, based on the normal distribution in large samples |

Throughout the chapter, $\mathbb{E}_W$ and $\operatorname{Var}_W$ denote moments over the random assignment with the potential outcomes held fixed, and $\mathbb{E}_{\mathrm{sp}}$, $\operatorname{Var}_{\mathrm{sp}}$ moments over both sampling and assignment ([3.9.1](/3.9.1)).

## 4.2. The Difference-in-Means Estimator

### 4.2.1. Unbiasedness

The estimand is the finite-sample **average treatment effect** $\tau_{\mathrm{fs}} = \frac{1}{N}\sum_{i=1}^{N}(Y_i(1) - Y_i(0))$.

**Definition 4.2.1 (Difference-in-Means Estimator)** In a CRE with $N_{\mathrm{t}}$ treated and $N_{\mathrm{c}}$ control units, the **difference-in-means estimator**, or Neyman estimator, is

$$
\hat\tau^{\mathrm{dif}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}Y_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}Y_i^{\mathrm{obs}}.
$$

To study it as a function of the random assignment, write it in terms of the fixed potential outcomes and the random indicators. Since $W_iY_i^{\mathrm{obs}} = W_iY_i(1)$ and $(1 - W_i)Y_i^{\mathrm{obs}} = (1 - W_i)Y_i(0)$,

$$
\hat\tau^{\mathrm{dif}} = \frac{1}{N}\sum_{i=1}^{N}\left(\frac{N}{N_{\mathrm{t}}}W_iY_i(1) - \frac{N}{N_{\mathrm{c}}}(1 - W_i)Y_i(0)\right).
$$

**Theorem 4.2.1 (Unbiasedness of the Difference in Means)** In a CRE, $\mathbb{E}_W[\hat\tau^{\mathrm{dif}}] = \tau_{\mathrm{fs}}$.

**Proof** Each unit is treated with probability $N_{\mathrm{t}}/N$, so $\mathbb{E}_W[W_i] = N_{\mathrm{t}}/N$ and $\mathbb{E}_W[1 - W_i] = N_{\mathrm{c}}/N$. The potential outcomes are constants, so by linearity

$$
\mathbb{E}_W\bigl[\hat\tau^{\mathrm{dif}}\bigr] = \frac{1}{N}\sum_{i=1}^{N}\left(\frac{N}{N_{\mathrm{t}}}\cdot\frac{N_{\mathrm{t}}}{N}Y_i(1) - \frac{N}{N_{\mathrm{c}}}\cdot\frac{N_{\mathrm{c}}}{N}Y_i(0)\right) = \frac{1}{N}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0)\bigr) = \tau_{\mathrm{fs}}. \qquad \square
$$

The result requires nothing about the potential outcomes: no model, no constant effect, no distributional assumption. It is the randomization alone that makes the treated group's average an unbiased estimate of the average of all $Y_i(1)$, and the control group's average an unbiased estimate of the average of all $Y_i(0)$. In this sense $\hat\tau^{\mathrm{dif}}$ is an **unbiased estimator** of the finite-sample effect, where "unbiased" refers to hypothetical repetitions of the randomization on the same units: hence the name repeated sampling approach.

**Example 4.2.1** For the honey experiment of [3.9.3](/3.9.3), with $N = 72$, $N_{\mathrm{t}} = 35$ and cough frequency as the outcome, $\hat\tau^{\mathrm{dif}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = -0.697$: children who received honey coughed on average about $0.7$ points less frequently on the $0$–$6$ scale. To judge whether this is more than chance we need its variance.

### 4.2.2. From Variance to Confidence Interval

A confidence interval for $\tau_{\mathrm{fs}}$ is built in three steps:

1. derive the sampling variance of the estimator over the randomization;
2. develop an estimator of this sampling variance;
3. create a large-sample confidence interval from the estimate and its estimated variance, using a normal approximation.

Sections 4.3–4.5 carry out these steps.

## 4.3. The Sampling Variance

### 4.3.1. The Variance Theorem

Define the finite-population means $\bar Y(w) = \frac{1}{N}\sum_i Y_i(w)$ and the finite-population variances

$$
S_{\mathrm{c}}^2 = \frac{1}{N - 1}\sum_{i=1}^{N}\bigl(Y_i(0) - \bar Y(0)\bigr)^2, \qquad
S_{\mathrm{t}}^2 = \frac{1}{N - 1}\sum_{i=1}^{N}\bigl(Y_i(1) - \bar Y(1)\bigr)^2,
$$

$$
S_{\mathrm{tc}}^2 = \frac{1}{N - 1}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0) - \tau_{\mathrm{fs}}\bigr)^2.
$$
$S_{\mathrm{c}}^2$ and $S_{\mathrm{t}}^2$ are the variances of the control and the treated potential outcomes over all $N$ units, and $S_{\mathrm{tc}}^2$ is the variance of the unit-level treatment effects. All three are fixed numbers, and all involve missing potential outcomes. The proof of the variance formula rests on the joint distribution of the assignment indicators.

**Lemma 4.3.1** In a CRE, let $D_i = W_i - N_{\mathrm{t}}/N$. Then $\sum_{i=1}^{N}D_i = 0$, $\mathbb{E}_W[D_i] = 0$ and

$$
\mathbb{E}_W\bigl[D_i^2\bigr] = \operatorname{Var}_W(W_i) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2}, \qquad
\mathbb{E}_W[D_iD_j] = \operatorname{Cov}_W(W_i, W_j) = -\frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2(N - 1)} \quad (i \ne j).
$$
Consequently, for any constants $a_1, \dots, a_N$ with mean $\bar a$,

$$
\operatorname{Var}_W\left(\sum_{i=1}^{N}D_ia_i\right) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}\cdot\frac{1}{N - 1}\sum_{i=1}^{N}(a_i - \bar a)^2.
$$

**Proof** The first identity holds because exactly $N_{\mathrm{t}}$ of the $W_i$ equal one. $W_i$ is Bernoulli with probability $N_{\mathrm{t}}/N$, so $\operatorname{Var}_W(W_i) = \frac{N_{\mathrm{t}}}{N}\cdot\frac{N_{\mathrm{c}}}{N}$. For $i \ne j$, both units are treated with probability $\frac{N_{\mathrm{t}}(N_{\mathrm{t}} - 1)}{N(N - 1)}$, so

$$
\operatorname{Cov}_W(W_i, W_j) = \frac{N_{\mathrm{t}}(N_{\mathrm{t}} - 1)}{N(N - 1)} - \frac{N_{\mathrm{t}}^2}{N^2} = \frac{N_{\mathrm{t}}\bigl[N(N_{\mathrm{t}} - 1) - N_{\mathrm{t}}(N - 1)\bigr]}{N^2(N - 1)} = -\frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2(N - 1)}.
$$
(Alternatively: $0 = \operatorname{Var}_W(\sum_i D_i) = N\operatorname{Var}_W(D_i) + N(N - 1)\operatorname{Cov}_W(D_i, D_j)$.) For the last formula,

$$
\operatorname{Var}_W\left(\sum_i D_ia_i\right) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2}\left[\sum_i a_i^2 - \frac{1}{N - 1}\sum_{i \ne j}a_ia_j\right]
= \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2}\cdot\frac{N\sum_i a_i^2 - \bigl(\sum_i a_i\bigr)^2}{N - 1},
$$
using $\sum_{i \ne j}a_ia_j = (\sum_i a_i)^2 - \sum_i a_i^2$, and $N\sum_i a_i^2 - (\sum_i a_i)^2 = N\sum_i (a_i - \bar a)^2$. $\square$

The last formula is the variance of a sum over a simple random sample drawn without replacement, written in a convenient form; the factor $\frac{N_{\mathrm{c}}}{N}$ hidden in it is the finite population correction. Applied with $a_i = Y_i(1)/N_{\mathrm{t}}$ it gives $\operatorname{Var}_W(\bar Y_{\mathrm{t}}^{\mathrm{obs}}) = \frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}S_{\mathrm{t}}^2 = \left(\frac{1}{N_{\mathrm{t}}} - \frac{1}{N}\right)S_{\mathrm{t}}^2$, since $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y(1) = \frac{1}{N_{\mathrm{t}}}\sum_i D_iY_i(1)$.

**Theorem 4.3.1 (Sampling Variance of the Difference in Means)** In a CRE,

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{S_{\mathrm{tc}}^2}{N}. \tag{4.1}
$$

**Proof** Substituting $W_i = D_i + N_{\mathrm{t}}/N$ and $1 - W_i = N_{\mathrm{c}}/N - D_i$ in the representation of Section 4.2.1,

$$
\hat\tau^{\mathrm{dif}} = \frac{1}{N}\sum_i\bigl(Y_i(1) - Y_i(0)\bigr) + \sum_i D_i\left(\frac{Y_i(1)}{N_{\mathrm{t}}} + \frac{Y_i(0)}{N_{\mathrm{c}}}\right)
= \tau_{\mathrm{fs}} + \sum_{i=1}^{N}D_ia_i, \qquad a_i = \frac{Y_i(1)}{N_{\mathrm{t}}} + \frac{Y_i(0)}{N_{\mathrm{c}}}.
$$
By Lemma 4.3.1, $\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}S_a^2$, where $S_a^2$ is the finite-population variance of the $a_i$. Let $S_{01} = \frac{1}{N - 1}\sum_i (Y_i(1) - \bar Y(1))(Y_i(0) - \bar Y(0))$ be the finite-population covariance of the two potential outcomes. Then

$$
S_a^2 = \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}^2} + \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}^2} + \frac{2S_{01}}{N_{\mathrm{t}}N_{\mathrm{c}}},
\qquad
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{1}{N}\left(\frac{N_{\mathrm{c}}}{N_{\mathrm{t}}}S_{\mathrm{t}}^2 + \frac{N_{\mathrm{t}}}{N_{\mathrm{c}}}S_{\mathrm{c}}^2 + 2S_{01}\right).
$$
The variance of the differences is $S_{\mathrm{tc}}^2 = S_{\mathrm{t}}^2 + S_{\mathrm{c}}^2 - 2S_{01}$, so $2S_{01} = S_{\mathrm{t}}^2 + S_{\mathrm{c}}^2 - S_{\mathrm{tc}}^2$, and

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{1}{N}\left[\left(\frac{N_{\mathrm{c}}}{N_{\mathrm{t}}} + 1\right)S_{\mathrm{t}}^2 + \left(\frac{N_{\mathrm{t}}}{N_{\mathrm{c}}} + 1\right)S_{\mathrm{c}}^2 - S_{\mathrm{tc}}^2\right] = \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} + \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} - \frac{S_{\mathrm{tc}}^2}{N}. \qquad \square
$$

The first two terms are what one would get by treating the two group means as independent samples from two populations; the third, negative term reflects the fact that the two groups are drawn from the same $N$ units without replacement, so that their means are negatively related. It vanishes only when the unit-level effects are all equal.

**Corollary 4.3.1** If the treatment effect is constant, $Y_i(1) - Y_i(0) = \tau_{\mathrm{fs}}$ for all $i$, then $S_{\mathrm{tc}}^2 = 0$, $S_{\mathrm{t}}^2 = S_{\mathrm{c}}^2 = S^2$ and

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} = S^2\left(\frac{1}{N_{\mathrm{c}}} + \frac{1}{N_{\mathrm{t}}}\right).
$$

Under the sharp null of [3.9.3](/3.9.3), the constant effect is zero, and this is Theorem 3.3.2 again.

**Example 4.3.1** Return to the four patients of Example 1.5.1, with $Y(0) = (1, 6, 1, 8)$ and $Y(1) = (7, 5, 5, 7)$, now assigned by a CRE with $N_{\mathrm{t}} = 2$. The six possible treated pairs and the resulting estimates are

| Treated units | $\{1,2\}$ | $\{1,3\}$ | $\{1,4\}$ | $\{2,3\}$ | $\{2,4\}$ | $\{3,4\}$ |
|---|---|---|---|---|---|---|
| $\hat\tau^{\mathrm{dif}}$ | $1.5$ | $-1$ | $3.5$ | $0.5$ | $5$ | $2.5$ |

Their average is $2 = \tau_{\mathrm{fs}}$, as Theorem 4.2.1 says, and their variance (with divisor $6$, since each assignment has probability $1/6$) is $3.833$. The formula gives the same: $S_{\mathrm{c}}^2 = 38/3 \approx 12.667$, $S_{\mathrm{t}}^2 = 4/3$, the unit-level effects $(6, -1, 4, -1)$ have $S_{\mathrm{tc}}^2 = 38/3$, and

$$
\frac{38/3}{2} + \frac{4/3}{2} - \frac{38/3}{4} = \frac{19}{3} + \frac{2}{3} - \frac{19}{6} = \frac{23}{6} \approx 3.833.
$$
Ignoring the third term would overstate the variance by $S_{\mathrm{tc}}^2/N = 19/6$, almost doubling it.

### 4.3.2. Representation through the Correlation of the Potential Outcomes

Let $\rho_{\mathrm{tc}} = S_{01}/(S_{\mathrm{t}}S_{\mathrm{c}})$ be the finite-population **correlation coefficient** of $Y_i(1)$ and $Y_i(0)$.

**Theorem 4.3.2** In a CRE,

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = S_{\mathrm{c}}^2\cdot\frac{N_{\mathrm{t}}}{N\cdot N_{\mathrm{c}}} + S_{\mathrm{t}}^2\cdot\frac{N_{\mathrm{c}}}{N\cdot N_{\mathrm{t}}} + \rho_{\mathrm{tc}}\cdot S_{\mathrm{c}}\cdot S_{\mathrm{t}}\cdot\frac{2}{N}.
$$
For given $S_{\mathrm{c}}$ and $S_{\mathrm{t}}$ the variance is largest when $\rho_{\mathrm{tc}} = 1$ and smallest when $\rho_{\mathrm{tc}} = -1$.

**Proof** Substitute $S_{\mathrm{tc}}^2 = S_{\mathrm{t}}^2 + S_{\mathrm{c}}^2 - 2\rho_{\mathrm{tc}}S_{\mathrm{t}}S_{\mathrm{c}}$ in (4.1) and use $\frac{1}{N_{\mathrm{c}}} - \frac{1}{N} = \frac{N_{\mathrm{t}}}{NN_{\mathrm{c}}}$, $\frac{1}{N_{\mathrm{t}}} - \frac{1}{N} = \frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}$. The variance is increasing in $\rho_{\mathrm{tc}}$, which lies in $[-1, 1]$. $\square$

With $\rho_{\mathrm{tc}} = 1$ the bound is

$$
\frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{(S_{\mathrm{t}} - S_{\mathrm{c}})^2}{N},
$$
which equals (4.1) with $S_{\mathrm{tc}}^2$ replaced by its smallest possible value $(S_{\mathrm{t}} - S_{\mathrm{c}})^2$. The case $\rho_{\mathrm{tc}} = 1$ includes the constant effect, where $Y_i(1)$ is $Y_i(0)$ shifted. The intuition for the sign is that a strong positive correlation means that units with high $Y_i(0)$ also have high $Y_i(1)$; if by chance the treated group contains many such units, the treated mean is high and the control mean low, and both errors push $\hat\tau^{\mathrm{dif}}$ in the same direction.

## 4.4. Estimating the Sampling Variance

### 4.4.1. The Neyman Variance Estimator

Each term of (4.1) involves missing outcomes, but the first two can be estimated without bias from the group sample variances

$$
s_{\mathrm{c}}^2 = \frac{1}{N_{\mathrm{c}} - 1}\sum_{i:W_i = 0}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2, \qquad
s_{\mathrm{t}}^2 = \frac{1}{N_{\mathrm{t}} - 1}\sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2.
$$

**Theorem 4.4.1** In a CRE with $N_{\mathrm{t}}, N_{\mathrm{c}} \ge 2$, $\mathbb{E}_W[s_{\mathrm{t}}^2] = S_{\mathrm{t}}^2$ and $\mathbb{E}_W[s_{\mathrm{c}}^2] = S_{\mathrm{c}}^2$.

**Proof** For the treated group, $(N_{\mathrm{t}} - 1)s_{\mathrm{t}}^2 = \sum_i W_iY_i(1)^2 - N_{\mathrm{t}}(\bar Y_{\mathrm{t}}^{\mathrm{obs}})^2$. Using $\mathbb{E}_W[W_i] = N_{\mathrm{t}}/N$ and $\mathbb{E}_W[(\bar Y_{\mathrm{t}}^{\mathrm{obs}})^2] = \bar Y(1)^2 + \left(\frac{1}{N_{\mathrm{t}}} - \frac{1}{N}\right)S_{\mathrm{t}}^2$,

$$
(N_{\mathrm{t}} - 1)\,\mathbb{E}_W\bigl[s_{\mathrm{t}}^2\bigr] = \frac{N_{\mathrm{t}}}{N}\Bigl(\sum_i Y_i(1)^2 - N\bar Y(1)^2\Bigr) - \Bigl(1 - \frac{N_{\mathrm{t}}}{N}\Bigr)S_{\mathrm{t}}^2
= \left(\frac{N_{\mathrm{t}}(N - 1)}{N} - \frac{N - N_{\mathrm{t}}}{N}\right)S_{\mathrm{t}}^2 = (N_{\mathrm{t}} - 1)S_{\mathrm{t}}^2.
$$
The control group is handled in the same way. $\square$

The variance of the unit-level effects, $S_{\mathrm{tc}}^2$, cannot be estimated at all: it depends on the pairing of $Y_i(1)$ and $Y_i(0)$ within units, and no unit reveals both. Since $S_{\mathrm{tc}}^2 \ge 0$, dropping the third term errs on the safe side.

**Definition 4.4.1 (Neyman Variance Estimator)** The **Neyman variance estimator** of the sampling variance of $\hat\tau^{\mathrm{dif}}$ is

$$
\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = \frac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}}.
$$

**Theorem 4.4.2** In a CRE,

$$
\mathbb{E}_W\bigl[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}\bigr] = \operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) + \frac{S_{\mathrm{tc}}^2}{N} \ge \operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr),
$$
with equality if and only if the treatment effect is constant. Thus the Neyman variance estimator is conservative in general and unbiased under a constant effect.

**Proof** By Theorem 4.4.1, $\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] = S_{\mathrm{c}}^2/N_{\mathrm{c}} + S_{\mathrm{t}}^2/N_{\mathrm{t}}$, which exceeds (4.1) by $S_{\mathrm{tc}}^2/N$; this is zero exactly when all $Y_i(1) - Y_i(0)$ are equal. $\square$

There is a second reason to use this estimator. It is unbiased for the variance of $\hat\tau^{\mathrm{dif}}$ as an estimator of the super-population effect $\tau_{\mathrm{sp}}$ (Section 4.6). So whichever estimand one has in mind, $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$ is either unbiased or conservative.

### 4.4.2. Two Alternatives

If the effect is constant, then also $S_{\mathrm{t}}^2 = S_{\mathrm{c}}^2 = S^2$, and the two group variances can be pooled:

$$
\widehat{\operatorname{Var}}{}^{\mathrm{const}} = s^2\left(\frac{1}{N_{\mathrm{c}}} + \frac{1}{N_{\mathrm{t}}}\right), \qquad
s^2 = \frac{(N_{\mathrm{c}} - 1)s_{\mathrm{c}}^2 + (N_{\mathrm{t}} - 1)s_{\mathrm{t}}^2}{N - 2} = \frac{1}{N - 2}\left(\sum_{i:W_i = 0}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2 + \sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2\right).
$$
This is the variance estimate of the equal-variance two-sample $t$-test. Under a constant effect it is unbiased, by Theorem 4.4.1 and Corollary 4.3.1. Without that assumption it can be biased in either direction, and it can seriously underestimate the variance when the groups have unequal sizes and the larger group has the smaller variance (Question 5).

At the other extreme, one can use the bound of Theorem 4.3.2 with a pre-specified correlation, replacing the population quantities by their sample counterparts,

$$
\widehat{\operatorname{Var}}{}^{\rho_{\mathrm{tc}}} = s_{\mathrm{c}}^2\cdot\frac{N_{\mathrm{t}}}{N\cdot N_{\mathrm{c}}} + s_{\mathrm{t}}^2\cdot\frac{N_{\mathrm{c}}}{N\cdot N_{\mathrm{t}}} + \rho_{\mathrm{tc}}\cdot s_{\mathrm{c}}\cdot s_{\mathrm{t}}\cdot\frac{2}{N}.
$$
Choosing $\rho_{\mathrm{tc}} = 1$ gives a sharper bound than the Neyman estimator,

$$
\widehat{\operatorname{Var}}{}^{\rho = 1} = \frac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{(s_{\mathrm{t}} - s_{\mathrm{c}})^2}{N},
$$
which is still conservative in large samples, because the true variance cannot exceed its value at $\rho_{\mathrm{tc}} = 1$. (In small samples it is only approximately so, because $s_{\mathrm{t}}$ and $s_{\mathrm{c}}$ are not unbiased for $S_{\mathrm{t}}$ and $S_{\mathrm{c}}$.) It improves on the Neyman estimator only when the two group variances differ.

| Estimator | Formula | Assumption for unbiasedness | Otherwise |
|---|---|---|---|
| $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$ | $s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}$ | constant effect (or super-population estimand) | conservative, bias $S_{\mathrm{tc}}^2/N$ |
| $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$ | $s^2(1/N_{\mathrm{c}} + 1/N_{\mathrm{t}})$ | constant effect | bias of either sign |
| $\widehat{\operatorname{Var}}{}^{\rho = 1}$ | $s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}} - (s_{\mathrm{t}} - s_{\mathrm{c}})^2/N$ | $\rho_{\mathrm{tc}} = 1$ | conservative in large samples |

The Neyman estimator is the standard choice: it is simple, it does not require a constant effect, and its conservativeness disappears for the super-population estimand.

## 4.5. Confidence Intervals and Tests

### 4.5.1. Confidence Intervals

By the **finite population central limit theorem** (Theorem 3.3.3, applied to the vector of both group means), the randomization distribution of $\hat\tau^{\mathrm{dif}}$ is approximately normal in large samples, with mean $\tau_{\mathrm{fs}}$ and variance (4.1). Replacing the variance by an estimate $\widehat{\operatorname{Var}}$, such as the Neyman estimator, gives the large-sample **confidence interval**

$$
\mathrm{CI}^{1 - \alpha}(\tau_{\mathrm{fs}}) = \left(\hat\tau^{\mathrm{dif}} - z_{\alpha/2}\sqrt{\widehat{\operatorname{Var}}},\ \hat\tau^{\mathrm{dif}} + z_{\alpha/2}\sqrt{\widehat{\operatorname{Var}}}\right),
$$
where $z_{\alpha/2}$ is the upper $\alpha/2$ quantile of the standard normal distribution; for a $90\%$ interval, $z_{0.05} = 1.645$. Because the Neyman estimator overestimates the variance on average, the interval covers $\tau_{\mathrm{fs}}$ with probability at least $1 - \alpha$ in large samples; it is exact when the effect is constant. Neyman's intervals are valid (they reach the nominal coverage) and efficient as far as the data allow, since the only excess width comes from the unidentifiable $S_{\mathrm{tc}}^2$.

### 4.5.2. Testing the Weak Null Hypothesis

Neyman's framework also gives a test, but of a different hypothesis from Fisher's. To test that the average effect is zero,

$$
H_0\colon\ \tau_{\mathrm{fs}} = \frac{1}{N}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0)\bigr) = 0 \quad \text{against} \quad H_a\colon\ \tau_{\mathrm{fs}} \ne 0,
$$
use the $t$-statistic

$$
t = \frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}}}
$$
with the p-value $2(1 - \Phi(\lvert t\rvert))$ from the normal approximation. The test is valid for the weak null hypothesis, which allows the unit-level effects to vary as long as they average to zero, and it is an approximate test, justified in large samples. Fisher's test of [3.9.3](/3.9.3) is exact but tests the sharp null; with the statistic $T^{\text{t-stat}}$, the two tests use the same function of the data but compare it with different reference distributions.

| | Neyman | Fisher |
|---|---|---|
| Null hypothesis | $\tau_{\mathrm{fs}} = 0$ (weak) | $Y_i(1) = Y_i(0)$ for all $i$ (sharp) |
| Statistic | $t = \hat\tau^{\mathrm{dif}}/\sqrt{\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}}$ | any, e.g. $T^{\mathrm{dif}}$ |
| Reference distribution | standard normal (large samples) | exact randomization distribution |
| Validity | approximate, for heterogeneous effects | exact, only under the sharp null |

**Example 4.5.1** For the honey data (cough frequency), $\hat\tau^{\mathrm{dif}} = -0.697$, and the three variance estimates are all about $0.139$: the two groups have similar sizes ($35$ and $37$) and similar sample variances, so pooling changes almost nothing, and the correction $(s_{\mathrm{t}} - s_{\mathrm{c}})^2/N$ is negligible. The standard error is $\sqrt{0.139} \approx 0.373$, and the $90\%$ confidence interval is

$$
-0.697 \pm 1.645 \times 0.373 \approx [-1.31, -0.08].
$$
The $t$-statistic is $-0.697/0.373 \approx -1.87$, with two-sided p-value $0.062$. Fisher's exact test with $T^{\mathrm{dif}}$ gave $0.067$. The two approaches agree closely here, although they test different hypotheses: at the $10\%$ level both reject the absence of an effect, at the $5\%$ level neither does.

## 4.6. The Super-Population

### 4.6.1. Two Layers of Randomness

Now regard the $N$ units as a simple random sample from an infinite super-population ([3.9.2](/3.9.2)), and assign treatments to them by a CRE. There are two layers of randomness: the sampling of the units from the super-population, and the randomized assignment of the treatments to the sampled units. The estimand is the super-population average treatment effect

$$
\tau_{\mathrm{sp}} = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1) - Y_i(0)\bigr],
$$
and the relevant population variances are

$$
\sigma_{\mathrm{c}}^2 = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(0)\bigr), \qquad
\sigma_{\mathrm{t}}^2 = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(1)\bigr), \qquad
\sigma_{\mathrm{tc}}^2 = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(1) - Y_i(0)\bigr).
$$
The finite-sample effect $\tau_{\mathrm{fs}}$ is now a random variable: the average of $N$ i.i.d. unit-level effects, with $\mathbb{E}_{\mathrm{sp}}[\tau_{\mathrm{fs}}] = \tau_{\mathrm{sp}}$ and $\operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}}) = \sigma_{\mathrm{tc}}^2/N$.

### 4.6.2. Unbiasedness and Variance

**Theorem 4.6.1** Let the $N$ units be a random sample from a super-population and the treatment be assigned by a CRE. Then

$$
\mathbb{E}_{\mathrm{sp}}\bigl[\hat\tau^{\mathrm{dif}}\bigr] = \tau_{\mathrm{sp}}, \qquad
\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}},
$$
and the Neyman variance estimator is unbiased for this variance: $\mathbb{E}_{\mathrm{sp}}[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] = \operatorname{Var}_{\mathrm{sp}}(\hat\tau^{\mathrm{dif}})$.

**Proof** Condition on the sample, that is, on the potential outcomes of the $N$ units. Given the sample, the assignment is a CRE, so Theorems 4.2.1, 4.3.1 and 4.4.1 apply conditionally. By the **law of total expectation**,

$$
\mathbb{E}_{\mathrm{sp}}\bigl[\hat\tau^{\mathrm{dif}}\bigr] = \mathbb{E}_{\mathrm{sp}}\Bigl[\mathbb{E}_W\bigl[\hat\tau^{\mathrm{dif}} \bigm| \boldsymbol{Y}(0), \boldsymbol{Y}(1)\bigr]\Bigr] = \mathbb{E}_{\mathrm{sp}}[\tau_{\mathrm{fs}}] = \tau_{\mathrm{sp}}.
$$
By the **law of total variance** ([3.1.9](/3.1.9#thm-9.4.1)),

$$
\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \mathbb{E}_{\mathrm{sp}}\Bigl[\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}} \bigm| \boldsymbol{Y}(0), \boldsymbol{Y}(1)\bigr)\Bigr] + \operatorname{Var}_{\mathrm{sp}}\Bigl(\mathbb{E}_W\bigl[\hat\tau^{\mathrm{dif}} \bigm| \boldsymbol{Y}(0), \boldsymbol{Y}(1)\bigr]\Bigr)
= \mathbb{E}_{\mathrm{sp}}\left[\frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{S_{\mathrm{tc}}^2}{N}\right] + \operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}}).
$$
The finite-population variances $S_{\mathrm{c}}^2$, $S_{\mathrm{t}}^2$ and $S_{\mathrm{tc}}^2$ are sample variances (with divisor $N - 1$) of $N$ i.i.d. draws, so their expectations are $\sigma_{\mathrm{c}}^2$, $\sigma_{\mathrm{t}}^2$ and $\sigma_{\mathrm{tc}}^2$. With $\operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}}) = \sigma_{\mathrm{tc}}^2/N$,

$$
\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{\sigma_{\mathrm{tc}}^2}{N} + \frac{\sigma_{\mathrm{tc}}^2}{N} = \frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}}.
$$
Finally, $\mathbb{E}_{\mathrm{sp}}[s_{\mathrm{t}}^2] = \mathbb{E}_{\mathrm{sp}}[\mathbb{E}_W[s_{\mathrm{t}}^2 \mid \boldsymbol{Y}(1)]] = \mathbb{E}_{\mathrm{sp}}[S_{\mathrm{t}}^2] = \sigma_{\mathrm{t}}^2$, and likewise for the control group, so $\mathbb{E}_{\mathrm{sp}}[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] = \sigma_{\mathrm{c}}^2/N_{\mathrm{c}} + \sigma_{\mathrm{t}}^2/N_{\mathrm{t}}$. $\square$

Equivalently, the deviation of the estimator from $\tau_{\mathrm{sp}}$ splits into two uncorrelated parts,

$$
\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{sp}} = \bigl(\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}}\bigr) + \bigl(\tau_{\mathrm{fs}} - \tau_{\mathrm{sp}}\bigr);
$$
the cross term has expectation zero because the first part has conditional mean zero given the sample. The first part is the error due to the assignment, with variance $\sigma_{\mathrm{c}}^2/N_{\mathrm{c}} + \sigma_{\mathrm{t}}^2/N_{\mathrm{t}} - \sigma_{\mathrm{tc}}^2/N$ on average; the second is the error due to sampling, with variance $\sigma_{\mathrm{tc}}^2/N$.

### 4.6.3. Interpretation

Theorem 4.6.1 resolves the puzzle of the conservative variance estimator. The quantity $S_{\mathrm{tc}}^2/N$, by which the Neyman estimator overestimates the finite-sample variance, is on average exactly the variance $\sigma_{\mathrm{tc}}^2/N$ of the finite-sample effect around the super-population effect. If the target is $\tau_{\mathrm{sp}}$, the estimator is unbiased; if the target is $\tau_{\mathrm{fs}}$, the units at hand are fixed, the sampling variation is absent, and the same estimator is conservative. Estimating the effect for the $N$ units in the experiment is easier than estimating it for the population they were drawn from, and the difference is precisely the heterogeneity of the effects: with a constant effect, $\tau_{\mathrm{fs}} = \tau_{\mathrm{sp}}$ and the two variances coincide. In practice the same interval, $\hat\tau^{\mathrm{dif}} \pm z_{\alpha/2}\sqrt{\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}}$, is used for both estimands; it is approximately exact for $\tau_{\mathrm{sp}}$ and conservative for $\tau_{\mathrm{fs}}$.

![For a fixed simulated finite population of 100 units: the randomization distribution of the difference in means with the normal densities implied by the true variance and by the expected Neyman variance estimate; the true sampling variance and the expectations of the Neyman and rho = 1 variance estimators as the heterogeneity of the unit-level effects grows; and the coverage of the nominal 95% Neyman interval for the finite-sample effect](./plots/neyman_variance.py)

The figure illustrates the finite-sample results. With a constant effect (heterogeneity zero) the Neyman estimator is unbiased and the interval has the nominal coverage. As the unit-level effects become more heterogeneous, the true variance falls below the expected Neyman estimate by $S_{\mathrm{tc}}^2/N$, and the coverage of the interval for $\tau_{\mathrm{fs}}$ rises above $95\%$. The $\rho = 1$ estimator removes part of the excess when the two potential outcome distributions have different spreads.

The approach has a limitation that shapes the next chapters: it does not use covariates. When pre-treatment variables predict the outcomes, they can reduce the variance considerably, as the gain-score statistic did for Fisher's test in [3.9.3](/3.9.3). Incorporating them into estimation is the topic of [3.9.5](/3.9.5) (regression) and [3.9.7](/3.9.7) (stratification).

## Summary

| | Finite sample | Super-population |
|---|---|---|
| Estimand | $\tau_{\mathrm{fs}} = \bar Y(1) - \bar Y(0)$ | $\tau_{\mathrm{sp}} = \mathbb{E}_{\mathrm{sp}}[Y_i(1) - Y_i(0)]$ |
| Randomness | assignment | sampling and assignment |
| Estimator | $\hat\tau^{\mathrm{dif}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$, unbiased (Theorem 4.2.1) | the same, unbiased (Theorem 4.6.1) |
| Variance | $\dfrac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \dfrac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \dfrac{S_{\mathrm{tc}}^2}{N}$ (Theorem 4.3.1) | $\dfrac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \dfrac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}}$ (Theorem 4.6.1) |
| Variance estimator | $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = \dfrac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \dfrac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}}$, conservative by $S_{\mathrm{tc}}^2/N$ (Theorem 4.4.2) | the same, unbiased |
| Interval | $\hat\tau^{\mathrm{dif}} \pm z_{\alpha/2}\sqrt{\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}}$, coverage $\ge 1 - \alpha$ | the same, coverage $\approx 1 - \alpha$ |

- The proof of the variance theorem uses $D_i = W_i - N_{\mathrm{t}}/N$ with $\operatorname{Var}_W(W_i) = N_{\mathrm{t}}N_{\mathrm{c}}/N^2$ and $\operatorname{Cov}_W(W_i, W_j) = -N_{\mathrm{t}}N_{\mathrm{c}}/(N^2(N - 1))$ (Lemma 4.3.1).
- With the correlation $\rho_{\mathrm{tc}}$ of the potential outcomes, the variance is increasing in $\rho_{\mathrm{tc}}$ (Theorem 4.3.2); $\rho_{\mathrm{tc}} = 1$ gives the sharpest identifiable upper bound and the estimator $\widehat{\operatorname{Var}}{}^{\rho = 1}$; under a constant effect the pooled $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$ is unbiased.
- Neyman's test concerns the weak null $\tau_{\mathrm{fs}} = 0$ and is approximate; Fisher's concerns the sharp null and is exact. In the honey data: $\hat\tau = -0.697$, variance about $0.139$, $90\%$ interval $[-1.31, -0.08]$, p-values $0.062$ (Neyman) and $0.067$ (Fisher).

## Questions

1. Three units have $Y(0) = (0, 2, 4)$ and $Y(1) = (1, 2, 6)$, and one of them is treated at random ($N_{\mathrm{t}} = 1$). List the three possible values of $\hat\tau^{\mathrm{dif}}$, and verify Theorems 4.2.1 and 4.3.1.

   **Answer** Treating unit 1: $1 - (2 + 4)/2 = -2$; unit 2: $2 - (0 + 4)/2 = 0$; unit 3: $6 - (0 + 2)/2 = 5$. The mean is $1 = \tau_{\mathrm{fs}}$, since the effects are $(1, 0, 2)$. The variance over the three assignments is $\frac{1}{3}[(-3)^2 + (-1)^2 + 4^2] = 26/3$. From the formula: $S_{\mathrm{c}}^2 = 4$, $S_{\mathrm{t}}^2 = \frac{1}{2}[(1 - 3)^2 + (2 - 3)^2 + (6 - 3)^2] = 7$, $S_{\mathrm{tc}}^2 = 1$, and $4/2 + 7/1 - 1/3 = 26/3$.
2. Show that $\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) \ge \frac{(S_{\mathrm{c}}\sqrt{N_{\mathrm{t}}/N_{\mathrm{c}}} - S_{\mathrm{t}}\sqrt{N_{\mathrm{c}}/N_{\mathrm{t}}})^2}{N}$, the value at $\rho_{\mathrm{tc}} = -1$. When is this lower bound zero, and what does that mean?

   **Answer** At $\rho_{\mathrm{tc}} = -1$, Theorem 4.3.2 gives $\frac{1}{N}\bigl[S_{\mathrm{c}}^2\frac{N_{\mathrm{t}}}{N_{\mathrm{c}}} + S_{\mathrm{t}}^2\frac{N_{\mathrm{c}}}{N_{\mathrm{t}}} - 2S_{\mathrm{c}}S_{\mathrm{t}}\bigr] = \frac{1}{N}\bigl(S_{\mathrm{c}}\sqrt{N_{\mathrm{t}}/N_{\mathrm{c}}} - S_{\mathrm{t}}\sqrt{N_{\mathrm{c}}/N_{\mathrm{t}}}\bigr)^2$, and the variance is increasing in $\rho_{\mathrm{tc}}$. It is zero when $S_{\mathrm{c}}N_{\mathrm{t}} = S_{\mathrm{t}}N_{\mathrm{c}}$ and the potential outcomes are perfectly negatively correlated; then $a_i = Y_i(1)/N_{\mathrm{t}} + Y_i(0)/N_{\mathrm{c}}$ is constant, so every assignment gives exactly $\hat\tau^{\mathrm{dif}} = \tau_{\mathrm{fs}}$.
3. Derive $\widehat{\operatorname{Var}}{}^{\rho = 1}$ from Theorem 4.3.2, and show that it is never larger than $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$.

   **Answer** Setting $\rho_{\mathrm{tc}} = 1$ and replacing $S$ by $s$: $s_{\mathrm{c}}^2\frac{N_{\mathrm{t}}}{NN_{\mathrm{c}}} + s_{\mathrm{t}}^2\frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}} + \frac{2s_{\mathrm{c}}s_{\mathrm{t}}}{N} = s_{\mathrm{c}}^2\bigl(\frac{1}{N_{\mathrm{c}}} - \frac{1}{N}\bigr) + s_{\mathrm{t}}^2\bigl(\frac{1}{N_{\mathrm{t}}} - \frac{1}{N}\bigr) + \frac{2s_{\mathrm{c}}s_{\mathrm{t}}}{N} = \frac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{(s_{\mathrm{t}} - s_{\mathrm{c}})^2}{N}$. The subtracted term is nonnegative, so $\widehat{\operatorname{Var}}{}^{\rho = 1} \le \widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$, with equality when $s_{\mathrm{t}} = s_{\mathrm{c}}$.
4. Show that in a CRE the covariance of the two group means is $\operatorname{Cov}_W(\bar Y_{\mathrm{t}}^{\mathrm{obs}}, \bar Y_{\mathrm{c}}^{\mathrm{obs}}) = -S_{01}/N$, where $S_{01}$ is the finite-population covariance of $Y_i(1)$ and $Y_i(0)$, and use it to give a second proof of Theorem 4.3.1.

   **Answer** $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y(1) = \frac{1}{N_{\mathrm{t}}}\sum_i D_iY_i(1)$ and $\bar Y_{\mathrm{c}}^{\mathrm{obs}} - \bar Y(0) = -\frac{1}{N_{\mathrm{c}}}\sum_i D_iY_i(0)$. By the bilinear version of Lemma 4.3.1, $\operatorname{Cov}_W(\sum_i D_ia_i, \sum_i D_ib_i) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}S_{ab}$, so the covariance is $-\frac{1}{N_{\mathrm{t}}N_{\mathrm{c}}}\cdot\frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}S_{01} = -S_{01}/N$. Then $\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) = (\frac{1}{N_{\mathrm{t}}} - \frac{1}{N})S_{\mathrm{t}}^2 + (\frac{1}{N_{\mathrm{c}}} - \frac{1}{N})S_{\mathrm{c}}^2 + \frac{2S_{01}}{N}$, and substituting $2S_{01} = S_{\mathrm{t}}^2 + S_{\mathrm{c}}^2 - S_{\mathrm{tc}}^2$ gives (4.1).
5. A CRE has $N = 100$, $N_{\mathrm{t}} = 10$, $S_{\mathrm{t}}^2 = 4$, $S_{\mathrm{c}}^2 = 1$. Compute an upper bound for the true variance of $\hat\tau^{\mathrm{dif}}$ and the expectations of $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$ and $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$. What do you conclude?

   **Answer** $S_{\mathrm{tc}}^2 \ge (S_{\mathrm{t}} - S_{\mathrm{c}})^2 = 1$, so the variance is at most $1/90 + 4/10 - 1/100 \approx 0.401$. $\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] = 1/90 + 4/10 \approx 0.411$, slightly conservative. $\mathbb{E}_W[s^2] = (89 \times 1 + 9 \times 4)/98 \approx 1.276$, so $\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{const}}] \approx 1.276\,(1/90 + 1/10) \approx 0.142$, about a third of the true variance. The pooled estimator, the one of the equal-variance $t$-test, is badly anti-conservative when the smaller group has the larger variance; intervals based on it would be far too narrow.
6. How many units are needed in a balanced CRE ($N_{\mathrm{t}} = N_{\mathrm{c}} = N/2$) for the $95\%$ Neyman interval to have half-width at most $0.2$, if $\sigma_{\mathrm{c}} = \sigma_{\mathrm{t}} = 1$?

   **Answer** The super-population variance is $2/(N/2) \cdot 1 = 4/N$, so the half-width is $1.96 \times 2/\sqrt N \le 0.2$, giving $\sqrt N \ge 19.6$ and $N \ge 385$; with even group sizes, $N = 386$.
7. In the super-population setting, compute $\operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}})$ and explain why $\operatorname{Var}_{\mathrm{sp}}(\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}})$ is smaller than $\operatorname{Var}_{\mathrm{sp}}(\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{sp}})$ by exactly this amount.

   **Answer** $\tau_{\mathrm{fs}}$ is the mean of $N$ i.i.d. unit-level effects with variance $\sigma_{\mathrm{tc}}^2$, so $\operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}}) = \sigma_{\mathrm{tc}}^2/N$. Writing $\hat\tau - \tau_{\mathrm{sp}} = (\hat\tau - \tau_{\mathrm{fs}}) + (\tau_{\mathrm{fs}} - \tau_{\mathrm{sp}})$, the two terms are uncorrelated, because $\mathbb{E}_W[\hat\tau - \tau_{\mathrm{fs}} \mid \text{sample}] = 0$ and the second term is a function of the sample. Hence the variances add, and the difference is $\sigma_{\mathrm{tc}}^2/N$.
8. Explain why the Neyman test of $\tau_{\mathrm{fs}} = 0$ can reject while Fisher's exact test of the sharp null does not, and give a reason why the opposite can also happen.

   **Answer** The tests compare similar statistics with different reference distributions, and both are only approximately comparable. Neyman's test uses a normal approximation, which can be too optimistic in small samples or with skewed outcomes, so it may reject when the exact randomization distribution does not. Conversely, Fisher's test with a statistic other than the difference in means (for example ranks or a gain score) may be more powerful against the alternative that actually holds, and rejects the sharp null while the difference in means is not significant; and effects of opposite signs can make the sharp null false while $\tau_{\mathrm{fs}} \approx 0$, which a distributional statistic like $T^{\mathrm{ks}}$ can detect but Neyman's test, by design, cannot.
