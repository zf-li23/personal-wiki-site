---
title: Model-Based Inference for Completely Randomized Experiments
description: Bayesian model-based imputation of the missing potential outcomes in a completely randomized experiment. The three inputs (assignment mechanism, model for the potential outcomes, prior) and the four steps leading to the posterior of the finite-sample average effect; why randomization lets the assignment mechanism drop out; analytic examples with a normal model for six NSW units and a Bernoulli–Beta model; the unidentified correlation between potential outcomes, covariates, Monte Carlo implementation, the super-population effect, and four models for the NSW job-training data.
---

The Neyman–Rubin framework of [3.9.1](/3.9.1) is a language for stating causal questions: it defines units, potential outcomes and estimands, and [3.9.2](/3.9.2) adds a description of how the data were collected. It does not prescribe a method of inference. Fisher's test, Neyman's estimator and regression ([3.9.3](/3.9.3)–[3.9.5](/3.9.5)) are three methods that can be built on it; this chapter presents a fourth, which treats causal inference directly as a missing-data problem. Every causal estimand in a finite sample is a function of the observed outcomes and of the missing potential outcomes. A statistical model for the potential outcomes, combined with a prior distribution for its parameters, gives a posterior predictive distribution for the missing outcomes, and therefore a posterior distribution for any estimand. The approach is Bayesian, and the general theory of [3.7](/3.7) is assumed; only the parts needed here are recalled. Compared with the earlier methods it is more flexible, since any estimand (a quantile effect, a proportion of units who benefit) can be handled in the same way, and more explicit about its assumptions, since everything rests on the model.

## 6.1. Motivation: Imputing the Missing Outcomes

### 6.1.1. The NSW Data

The National Supported Work (NSW) demonstration was a job-training program for men substantially disadvantaged in the labor market; its experimental data were analyzed by LaLonde (1986). The sample used here has $N = 445$ men, of whom $N_{\mathrm{t}} = 185$ were assigned to the training program by a completely randomized design and $N_{\mathrm{c}} = 260$ to no active treatment. The outcome is earnings in 1978 (in thousands of dollars), and seven covariates were recorded before the assignment: age, years of education, marital status, absence of a high-school degree, race (black), and earnings in 1974 and 1975. Many of the men had no earnings at all in 1978, so the outcome has a large mass at zero and a long right tail, a fact that matters for the choice of model (Section 6.8).

The estimators of the previous chapters give, for the effect of training on 1978 earnings, $\hat\tau^{\mathrm{dif}} = 1.79$ with Neyman standard error $0.67$, and a covariate-adjusted regression estimate of $1.67$ with standard error $0.64$.

### 6.1.2. The Estimand as a Function of the Missing Outcomes

The first six observations are the running example of this chapter.

| Unit | $Y_i(0)$ | $Y_i(1)$ | $W_i$ | $Y_i^{\mathrm{obs}}$ |
|---|---|---|---|---|
| 1 | 0 | ? | 0 | 0 |
| 2 | ? | 9.9 | 1 | 9.9 |
| 3 | 12.4 | ? | 0 | 12.4 |
| 4 | ? | 3.6 | 1 | 3.6 |
| 5 | 0 | ? | 0 | 0 |
| 6 | ? | 24.9 | 1 | 24.9 |

The finite-sample average effect is $\tau_{\mathrm{fs}} = \frac{1}{6}\sum_{i=1}^{6}(Y_i(1) - Y_i(0))$. Since $Y_i(1) = Y_i^{\mathrm{obs}}$ if $W_i = 1$ and $Y_i^{\mathrm{mis}}$ if $W_i = 0$, and conversely for $Y_i(0)$,

$$
\tau_{\mathrm{fs}} = \tilde\tau\bigl(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{W}\bigr) = \frac{1}{N}\sum_{i=1}^{N}(2W_i - 1)\bigl(Y_i^{\mathrm{obs}} - Y_i^{\mathrm{mis}}\bigr).
$$
Given $\boldsymbol{Y}^{\mathrm{obs}}$ and $\boldsymbol{W}$, the only unknown is $\boldsymbol{Y}^{\mathrm{mis}}$. Any method that produces a distribution for $\boldsymbol{Y}^{\mathrm{mis}}$ given the data produces a distribution for $\tau_{\mathrm{fs}}$. The key question is how to impute the missing outcomes.

### 6.1.3. Two Naive Imputations

*Imputation by group means.* Replace every missing $Y_i(0)$ by the control mean $\bar Y_{\mathrm{c}}^{\mathrm{obs}} = (0 + 12.4 + 0)/3 = 4.13$ and every missing $Y_i(1)$ by the treated mean $\bar Y_{\mathrm{t}}^{\mathrm{obs}} = (9.9 + 3.6 + 24.9)/3 = 12.8$. The completed data give $\hat\tau = 12.8 - 4.13 = 8.67$, which is exactly $\hat\tau^{\mathrm{dif}}$. But the imputation mechanism is degenerate, $\mathbb{P}(Y_i^{\mathrm{mis}} = 12.8 \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) = 1$ for control units: it fills in the missing values as if there were no uncertainty about them, and gives no measure of precision.

*Imputation from the empirical distribution.* For each control unit draw $Y_i(1)$ from the three observed treated outcomes $\{9.9, 3.6, 24.9\}$ with probability $1/3$ each, and for each treated unit draw $Y_i(0)$ from $\{0, 12.4, 0\}$. This gives $3^6 = 729$ equally likely completed data sets and a distribution of $\tau_{\mathrm{fs}}$. It acknowledges the variation of the outcomes around their group means, but it treats the empirical distribution of three observations as if it were the true distribution of the potential outcomes. It ignores the uncertainty about that distribution itself, which with three observations per group is large.

Both problems call for (1) a more flexible model for how the potential outcomes are generated, with parameters that are themselves uncertain, and (2) a systematic way to propagate that uncertainty to $\boldsymbol{Y}^{\mathrm{mis}}$. Bayesian inference provides both.

## 6.2. Bayesian Inference in Brief

Bayesian inference treats all unknowns, parameters included, as random variables. Its elements are the **prior distribution** $p(\theta)$, the sampling distribution or **likelihood function** $p(y \mid \theta)$, the joint distribution $p(y, \theta) = p(\theta)p(y \mid \theta)$, and the **posterior distribution** given by Bayes' theorem,

$$
p(\theta \mid y) = \frac{p(\theta)p(y \mid \theta)}{\int p(\theta)p(y \mid \theta)\,\mathrm{d}\theta} \propto p(\theta)p(y \mid \theta).
$$
Predictions of a new or unobserved quantity $\tilde y$ that is conditionally independent of $y$ given $\theta$ use the **posterior predictive distribution** $p(\tilde y \mid y) = \int p(\tilde y \mid \theta)p(\theta \mid y)\,\mathrm{d}\theta$, which averages over the posterior uncertainty about $\theta$. The binomial model with a uniform prior, which Laplace used for the proportion of male births in Paris, is worked out in [Example 1.4.1](/3.7.1#ex-1.4.1); with $y$ successes in $n$ trials and the prior $\mathrm{Beta}(\alpha, \beta)$ the posterior is $\mathrm{Beta}(\alpha + y, \beta + n - y)$, the **conjugate prior** case.

Two generalizations are needed. First, the data may be only partly observed, $y = (y^{\mathrm{obs}}, y^{\mathrm{mis}})$; the likelihood of the observed data is then $p(y^{\mathrm{obs}} \mid \theta) = \int p(y^{\mathrm{obs}}, y^{\mathrm{mis}} \mid \theta)\,\mathrm{d}y^{\mathrm{mis}}$, and the missing data have the posterior predictive distribution $p(y^{\mathrm{mis}} \mid y^{\mathrm{obs}}) = \int p(y^{\mathrm{mis}} \mid y^{\mathrm{obs}}, \theta)p(\theta \mid y^{\mathrm{obs}})\,\mathrm{d}\theta$. Second, only some functions of the unknowns may be of interest, the others being **nuisance parameters** that are integrated out of the joint posterior. In causal inference the missing potential outcomes play the role of $y^{\mathrm{mis}}$, the parameters of the outcome model are nuisance parameters, and the quantity of interest is the estimand $\tau$.

The Bayesian approach answers the question researchers usually ask ("what is the probability that the effect is positive?"), combines information from several sources in a principled way, and handles complicated models through simulation. Its main point of debate is the choice of prior. In the applications below the priors are weak, and the sample information dominates.

## 6.3. Theory without Correlation or Covariates

### 6.3.1. Three Inputs and the Target

**Definition 6.3.1 (Model-Based Imputation)** **Model-based imputation** of a causal estimand $\tau = \tau(\boldsymbol{Y}(0), \boldsymbol{Y}(1), \boldsymbol{X}, \boldsymbol{W})$ derives its posterior distribution $f(\tau \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \boldsymbol{X})$ from three inputs:

1. the assignment mechanism $\mathbb{P}(\boldsymbol{W} \mid \boldsymbol{X}, \boldsymbol{Y}(0), \boldsymbol{Y}(1))$, which in a CRE is $\binom{N}{N_{\mathrm{t}}}^{-1}$ for every $\boldsymbol{W} \in \mathcal{W}^+$;
2. a model $f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \boldsymbol{X}, \theta)$ for the potential outcomes given a parameter $\theta$;
3. a prior distribution $p(\theta)$;

by computing the posterior predictive distribution of $\boldsymbol{Y}^{\mathrm{mis}}$ and transforming it through $\tau = \tilde\tau(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{W})$.

:::

The model for the potential outcomes is usually built from exchangeability of the units in the sense of [de Finetti's theorem](/3.7.6#thm-6.3.1): if the labels of the units carry no information, the joint distribution can be written as a mixture of i.i.d. models,

$$
f\bigl(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta\bigr) = \prod_{i=1}^{N} f\bigl(Y_i(0), Y_i(1) \mid \theta\bigr),
$$
where the mixing distribution is the prior $p(\theta)$. In this section there are no covariates, and the two potential outcomes are independent given $\theta$: $f(Y_i(0), Y_i(1) \mid \theta) = f_{\mathrm{c}}(Y_i(0) \mid \theta_{\mathrm{c}})f_{\mathrm{t}}(Y_i(1) \mid \theta_{\mathrm{t}})$ with $\theta = (\theta_{\mathrm{c}}, \theta_{\mathrm{t}})$. Section 6.4 discusses what this choice means.

### 6.3.2. Four Steps

The target $f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})$ is reached in four steps.

| Step | Computes | Formula |
|---|---|---|
| 1 | conditional distribution of the missing outcomes given $\theta$ | $f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta) = \dfrac{f(\boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)}{\int f(\boldsymbol{y}^{\mathrm{mis}}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)\,\mathrm{d}\boldsymbol{y}^{\mathrm{mis}}}$ |
| 2 | posterior of the parameter | $p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) = \dfrac{p(\theta)f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)}{\int p(\theta)f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)\,\mathrm{d}\theta}$ |
| 3 | posterior predictive distribution of the missing outcomes | $f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) = \int f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta)\,p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})\,\mathrm{d}\theta$ |
| 4 | posterior of the estimand | distribution of $\tilde\tau(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{W})$ under Step 3 |

Here $f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta) = \int f(\boldsymbol{y}^{\mathrm{mis}}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)\,\mathrm{d}\boldsymbol{y}^{\mathrm{mis}}$ is the likelihood of the observed data, and the joint distribution of all quantities given $\theta$ is $f(\boldsymbol{Y}(0), \boldsymbol{Y}(1), \boldsymbol{W} \mid \theta) = \mathbb{P}(\boldsymbol{W} \mid \boldsymbol{Y}(0), \boldsymbol{Y}(1))\,f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)$, rewritten in terms of $(\boldsymbol{Y}^{\mathrm{mis}}, \boldsymbol{Y}^{\mathrm{obs}})$, which is a one-to-one relabeling of $(\boldsymbol{Y}(0), \boldsymbol{Y}(1))$ once $\boldsymbol{W}$ is fixed.

**Theorem 6.3.1** Suppose the assignment mechanism is unconfounded and does not depend on $\theta$ (in particular, a CRE). Then the assignment mechanism drops out of Steps 1 and 2:

$$
f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta) = \frac{f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)}{\int f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)\,\mathrm{d}\boldsymbol{Y}^{\mathrm{mis}}}, \qquad
p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) \propto p(\theta)\int f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)\,\mathrm{d}\boldsymbol{Y}^{\mathrm{mis}}.
$$
If moreover the units are i.i.d. given $\theta$ with independent potential outcomes, then given $(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta)$ the missing outcomes are independent, with $Y_i^{\mathrm{mis}} \sim f_{\mathrm{t}}(\cdot \mid \theta_{\mathrm{t}})$ for control units and $Y_i^{\mathrm{mis}} \sim f_{\mathrm{c}}(\cdot \mid \theta_{\mathrm{c}})$ for treated units, and the likelihood is

$$
f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta) \propto \prod_{i: W_i = 0}f_{\mathrm{c}}\bigl(Y_i^{\mathrm{obs}} \mid \theta_{\mathrm{c}}\bigr)\prod_{i: W_i = 1}f_{\mathrm{t}}\bigl(Y_i^{\mathrm{obs}} \mid \theta_{\mathrm{t}}\bigr).
$$

**Proof** For an unconfounded mechanism, $\mathbb{P}(\boldsymbol{W} \mid \boldsymbol{Y}(0), \boldsymbol{Y}(1)) = \mathbb{P}(\boldsymbol{W})$ does not involve the potential outcomes, and by assumption it does not involve $\theta$. It is therefore a constant factor in the numerator and denominator of Step 1, which cancels, and a constant factor in the likelihood $f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)$ of Step 2, which is absorbed into the normalizing constant. This gives the two displayed formulas. With independent potential outcomes and i.i.d. units, $f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)$ is the product over units of $f_{\mathrm{c}}(Y_i(0) \mid \theta_{\mathrm{c}})f_{\mathrm{t}}(Y_i(1) \mid \theta_{\mathrm{t}})$. For a control unit the first factor is $f_{\mathrm{c}}(Y_i^{\mathrm{obs}} \mid \theta_{\mathrm{c}})$ and the second $f_{\mathrm{t}}(Y_i^{\mathrm{mis}} \mid \theta_{\mathrm{t}})$, and conversely for a treated unit. Integrating over $\boldsymbol{Y}^{\mathrm{mis}}$ integrates each factor containing a missing outcome to one, which gives the likelihood; dividing the product by the likelihood leaves $\prod_{W_i = 0}f_{\mathrm{t}}(Y_i^{\mathrm{mis}} \mid \theta_{\mathrm{t}})\prod_{W_i = 1}f_{\mathrm{c}}(Y_i^{\mathrm{mis}} \mid \theta_{\mathrm{c}})$, the claimed conditional distribution. $\square$

The theorem is the Bayesian counterpart of the role of randomization in the earlier chapters: the design does not need to be modeled, because it carries no information about the potential outcomes. The same conclusion holds for any ignorable mechanism ([3.9.2](/3.9.2)), which is why model-based imputation extends to observational studies under unconfoundedness. If, in addition, the priors of $\theta_{\mathrm{c}}$ and $\theta_{\mathrm{t}}$ are independent, the likelihood factorizes and so does the posterior: $\theta_{\mathrm{c}}$ is learned from the control units only and $\theta_{\mathrm{t}}$ from the treated units only.

### 6.3.3. A Normal Example with Six Units

**Example 6.3.1** For the six NSW units of Section 6.1.2, take the model and prior

$$
\begin{pmatrix} Y_i(0) \\ Y_i(1) \end{pmatrix} \Bigm| \theta \sim \mathcal{N}\left(\begin{pmatrix} \mu_{\mathrm{c}} \\ \mu_{\mathrm{t}} \end{pmatrix}, \begin{pmatrix} 100 & 0 \\ 0 & 64 \end{pmatrix}\right), \qquad
\begin{pmatrix} \mu_{\mathrm{c}} \\ \mu_{\mathrm{t}} \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 10\,000 & 0 \\ 0 & 10\,000 \end{pmatrix}\right),
$$
so that $\theta = (\mu_{\mathrm{c}}, \mu_{\mathrm{t}})$, the outcome standard deviations $\sigma_{\mathrm{c}} = 10$ and $\sigma_{\mathrm{t}} = 8$ are known, and the prior is very diffuse. Find the posterior of $\tau_{\mathrm{fs}}$.

*Step 1.* By Theorem 6.3.1, given $\theta$ the missing outcomes are independent normals: $Y_i^{\mathrm{mis}} \sim \mathcal{N}(\mu_{\mathrm{t}}, 64)$ for the control units $i = 1, 3, 5$ and $Y_i^{\mathrm{mis}} \sim \mathcal{N}(\mu_{\mathrm{c}}, 100)$ for the treated units $i = 2, 4, 6$. In vector form, $\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta \sim \mathcal{N}\bigl((\mu_{\mathrm{t}}, \mu_{\mathrm{c}}, \mu_{\mathrm{t}}, \mu_{\mathrm{c}}, \mu_{\mathrm{t}}, \mu_{\mathrm{c}})^{\mathsf T}, \operatorname{diag}(64, 100, 64, 100, 64, 100)\bigr)$.

*Step 2.* The likelihood factorizes, and each mean has a normal prior and normal data with known variance, the conjugate case of [3.7.2](/3.7.2). The posterior precision of $\mu_{\mathrm{c}}$ is $N_{\mathrm{c}}/\sigma_{\mathrm{c}}^2 + 1/10\,000 = 0.0301$, and the posterior mean is $\bar Y_{\mathrm{c}}^{\mathrm{obs}} \cdot \frac{N_{\mathrm{c}} \cdot 10\,000}{N_{\mathrm{c}} \cdot 10\,000 + 100} = 4.12$; likewise for $\mu_{\mathrm{t}}$, with $\bar Y_{\mathrm{t}}^{\mathrm{obs}} \cdot \frac{N_{\mathrm{t}} \cdot 10\,000}{N_{\mathrm{t}} \cdot 10\,000 + 64} = 12.77$. Hence

$$
\begin{pmatrix} \mu_{\mathrm{c}} \\ \mu_{\mathrm{t}} \end{pmatrix} \Bigm| \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}\left(\begin{pmatrix} 4.12 \\ 12.77 \end{pmatrix}, \begin{pmatrix} 5.76^2 & 0 \\ 0 & 4.61^2 \end{pmatrix}\right),
$$
with variances $33.2$ and $21.3$. The diffuse prior shrinks the means negligibly towards zero.

*Step 3.* Write $Y_i^{\mathrm{mis}} = \mu_{\mathrm{t}} + e_i$ for control and $\mu_{\mathrm{c}} + e_i$ for treated units, where the $e_i$ are independent normal errors, independent of $\theta$. Given the data, $(\mu_{\mathrm{c}}, \mu_{\mathrm{t}}, e_1, \dots, e_6)$ is jointly normal, so $\boldsymbol{Y}^{\mathrm{mis}}$, a linear function of it, is multivariate normal ([Theorem 15.3.2](/3.1.15#thm-15.3.2)). No integration is needed: only its mean and covariance matrix have to be found. By the laws of total expectation and total covariance,

$$
\mathbb{E}\bigl[Y_i^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}\bigr] = W_i \cdot 4.12 + (1 - W_i) \cdot 12.77,
$$
$$
\operatorname{Var}\bigl(Y_i^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}\bigr) = \mathbb{E}\bigl[\operatorname{Var}(Y_i^{\mathrm{mis}} \mid \cdot, \theta)\bigr] + \operatorname{Var}\bigl(\mathbb{E}[Y_i^{\mathrm{mis}} \mid \cdot, \theta]\bigr) = \begin{cases} 64 + 21.3 = 85.3, & W_i = 0,\\ 100 + 33.2 = 133.2, & W_i = 1, \end{cases}
$$
and $\operatorname{Cov}(Y_i^{\mathrm{mis}}, Y_{i'}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})$ equals $21.3$ if both are control units (they share the uncertain $\mu_{\mathrm{t}}$), $33.2$ if both are treated, and $0$ otherwise. So

$$
\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}\left(\begin{pmatrix} 12.8 \\ 4.1 \\ 12.8 \\ 4.1 \\ 12.8 \\ 4.1 \end{pmatrix}, \begin{bmatrix}
85.3 & 0 & 21.3 & 0 & 21.3 & 0\\
0 & 133.2 & 0 & 33.2 & 0 & 33.2\\
21.3 & 0 & 85.3 & 0 & 21.3 & 0\\
0 & 33.2 & 0 & 133.2 & 0 & 33.2\\
21.3 & 0 & 21.3 & 0 & 85.3 & 0\\
0 & 33.2 & 0 & 33.2 & 0 & 133.2
\end{bmatrix}\right).
$$

*Step 4.* $\tau_{\mathrm{fs}} = \frac{1}{6}\bigl[(Y_1^{\mathrm{mis}} + Y_3^{\mathrm{mis}} + Y_5^{\mathrm{mis}}) - 12.4 + 38.4 - (Y_2^{\mathrm{mis}} + Y_4^{\mathrm{mis}} + Y_6^{\mathrm{mis}})\bigr]$ is linear in $\boldsymbol{Y}^{\mathrm{mis}}$, hence normal, with mean $\frac{1}{6}(3 \cdot 12.77 + 26.0 - 3 \cdot 4.12) = 8.66$. The sum of three missing $Y(1)$ values has variance $3 \cdot 85.3 + 6 \cdot 21.3 = 383.6$, the sum of three missing $Y(0)$ values $3 \cdot 133.2 + 6 \cdot 33.2 = 598.8$, and the two sums are independent, so $\operatorname{Var}(\tau_{\mathrm{fs}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}) = (383.6 + 598.8)/36 = 27.3$:

$$
\tau_{\mathrm{fs}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}(8.7, 5.2^2).
$$
The posterior mean is essentially $\hat\tau^{\mathrm{dif}} = 8.67$, and the posterior standard deviation $5.2$ now reflects both the variability of the outcomes and the uncertainty about their means.

### 6.3.4. A Binary Example

**Example 6.3.2** Let the outcome be binary, with $Y_i(0) \mid \theta \sim \mathrm{Ber}(\pi_{\mathrm{c}})$ and $Y_i(1) \mid \theta \sim \mathrm{Ber}(\pi_{\mathrm{t}})$ independent, $\theta = (\pi_{\mathrm{c}}, \pi_{\mathrm{t}})$, and independent priors $\pi_{\mathrm{c}} \sim \mathrm{Beta}(a_{\mathrm{c}}, b_{\mathrm{c}})$, $\pi_{\mathrm{t}} \sim \mathrm{Beta}(a_{\mathrm{t}}, b_{\mathrm{t}})$. In a CRE, $y_{\mathrm{t}} = \sum_{W_i = 1}Y_i^{\mathrm{obs}}$ treated and $y_{\mathrm{c}} = \sum_{W_i = 0}Y_i^{\mathrm{obs}}$ control units have $Y^{\mathrm{obs}} = 1$. Derive the posterior of $\tau_{\mathrm{fs}}$, and evaluate it for $N_{\mathrm{t}} = N_{\mathrm{c}} = 5$, $y_{\mathrm{t}} = 4$, $y_{\mathrm{c}} = 2$ and uniform priors.

*Step 1.* Given $\theta$, the missing $Y_i(1)$ of the control units are i.i.d. $\mathrm{Ber}(\pi_{\mathrm{t}})$ and the missing $Y_i(0)$ of the treated units i.i.d. $\mathrm{Ber}(\pi_{\mathrm{c}})$. Only their sums matter for $\tau_{\mathrm{fs}}$: $M_1 = \sum_{W_i = 0}Y_i^{\mathrm{mis}} \mid \theta \sim \mathrm{Bin}(N_{\mathrm{c}}, \pi_{\mathrm{t}})$ and $M_0 = \sum_{W_i = 1}Y_i^{\mathrm{mis}} \mid \theta \sim \mathrm{Bin}(N_{\mathrm{t}}, \pi_{\mathrm{c}})$.

*Step 2.* The likelihood is $\pi_{\mathrm{t}}^{y_{\mathrm{t}}}(1 - \pi_{\mathrm{t}})^{N_{\mathrm{t}} - y_{\mathrm{t}}}\pi_{\mathrm{c}}^{y_{\mathrm{c}}}(1 - \pi_{\mathrm{c}})^{N_{\mathrm{c}} - y_{\mathrm{c}}}$, so by conjugacy $\pi_{\mathrm{t}} \mid \text{data} \sim \mathrm{Beta}(a_{\mathrm{t}} + y_{\mathrm{t}}, b_{\mathrm{t}} + N_{\mathrm{t}} - y_{\mathrm{t}})$ and $\pi_{\mathrm{c}} \mid \text{data} \sim \mathrm{Beta}(a_{\mathrm{c}} + y_{\mathrm{c}}, b_{\mathrm{c}} + N_{\mathrm{c}} - y_{\mathrm{c}})$, independently.

*Step 3.* Integrating the binomial over the Beta posterior gives the **beta-binomial distribution**:

$$
M_1 \mid \text{data} \sim \mathrm{BetaBin}\bigl(N_{\mathrm{c}}, a_{\mathrm{t}} + y_{\mathrm{t}}, b_{\mathrm{t}} + N_{\mathrm{t}} - y_{\mathrm{t}}\bigr), \qquad
M_0 \mid \text{data} \sim \mathrm{BetaBin}\bigl(N_{\mathrm{t}}, a_{\mathrm{c}} + y_{\mathrm{c}}, b_{\mathrm{c}} + N_{\mathrm{c}} - y_{\mathrm{c}}\bigr),
$$
independently, where $\mathbb{P}(M = m) = \binom{n}{m}\frac{\mathrm{B}(m + \alpha, n - m + \beta)}{\mathrm{B}(\alpha, \beta)}$, with mean $n\alpha/(\alpha + \beta)$ and variance $\frac{n\alpha\beta(\alpha + \beta + n)}{(\alpha + \beta)^2(\alpha + \beta + 1)}$. Unlike the Bernoulli draws given $\theta$, the imputed outcomes are dependent across units, because they share the uncertain $\pi_{\mathrm{t}}$ or $\pi_{\mathrm{c}}$.

*Step 4.* $\tau_{\mathrm{fs}} = \frac{1}{N}\bigl[(y_{\mathrm{t}} + M_1) - (y_{\mathrm{c}} + M_0)\bigr]$, whose distribution is that of a difference of two independent beta-binomial variables.

With the numbers given, $M_1 \sim \mathrm{BetaBin}(5, 5, 2)$ and $M_0 \sim \mathrm{BetaBin}(5, 3, 4)$, so $\mathbb{E}[M_1] = 25/7 = 3.57$, $\operatorname{Var}(M_1) = 1.53$, $\mathbb{E}[M_0] = 15/7 = 2.14$, $\operatorname{Var}(M_0) = 1.84$, and

$$
\mathbb{E}[\tau_{\mathrm{fs}} \mid \text{data}] = \frac{4 + 3.57 - 2 - 2.14}{10} = 0.343, \qquad
\operatorname{sd}(\tau_{\mathrm{fs}} \mid \text{data}) = \frac{\sqrt{1.53 + 1.84}}{10} = 0.18.
$$
The posterior is discrete, supported on multiples of $0.1$; summing the products of the two probability mass functions gives $\mathbb{P}(\tau_{\mathrm{fs}} > 0 \mid \text{data}) = 0.94$. The posterior mean is pulled from $\hat\tau^{\mathrm{dif}} = 0.4$ towards zero by the uniform priors, whose means are $1/2$: with five units per group the prior counts as two additional observations in each group.

:::

## 6.4. Correlation between the Potential Outcomes

The independence of $Y_i(0)$ and $Y_i(1)$ given $\theta$ is a substantive assumption. A more general normal model has

$$
\begin{pmatrix} Y_i(0) \\ Y_i(1) \end{pmatrix} \Bigm| \theta \sim \mathcal{N}\left(\begin{pmatrix} \mu_{\mathrm{c}} \\ \mu_{\mathrm{t}} \end{pmatrix}, \begin{pmatrix} \sigma_{\mathrm{c}}^2 & \rho\sigma_{\mathrm{c}}\sigma_{\mathrm{t}} \\ \rho\sigma_{\mathrm{c}}\sigma_{\mathrm{t}} & \sigma_{\mathrm{t}}^2 \end{pmatrix}\right), \qquad p(\theta) = p(\rho)\,p(\mu_{\mathrm{c}}, \mu_{\mathrm{t}}, \sigma_{\mathrm{c}}^2, \sigma_{\mathrm{t}}^2).
$$
The four steps are unchanged, except that in Step 1 the missing outcome of a control unit now has the conditional distribution $\mathcal{N}\bigl(\mu_{\mathrm{t}} + \rho\frac{\sigma_{\mathrm{t}}}{\sigma_{\mathrm{c}}}(Y_i^{\mathrm{obs}} - \mu_{\mathrm{c}}),\ (1 - \rho^2)\sigma_{\mathrm{t}}^2\bigr)$ ([Theorem 15.5.1](/3.1.15#thm-15.5.1)), and symmetrically for treated units.

The correlation coefficient is different from the other parameters. Each unit contributes to the likelihood only through the marginal density of its observed outcome, $f_{\mathrm{c}}$ or $f_{\mathrm{t}}$, in which $\rho$ does not appear. With a prior in which $\rho$ is independent of the other parameters, its posterior is therefore identical to its prior: the data contain no information about it. This is the Bayesian form of the fact, seen in Theorem 4.3.2, that $S_{\mathrm{tc}}^2$ cannot be estimated, because the two potential outcomes are never observed together. The posterior of $\tau_{\mathrm{fs}}$ does depend on $\rho$, and an analysis should either justify its choice of $\rho$ or show the results for a range of values.

For the six-unit example take $\rho = 1$, that is, the covariance $80 = \sqrt{100 \cdot 64}$. Then $Y_i(1) = \mu_{\mathrm{t}} + 0.8(Y_i(0) - \mu_{\mathrm{c}})$ exactly, the missing outcomes are deterministic functions of the observed ones and of $\theta$, and $\tau_{\mathrm{fs}}$ becomes a linear function of $(\mu_{\mathrm{c}}, \mu_{\mathrm{t}})$, namely $\tau_{\mathrm{fs}} = 1.125\mu_{\mathrm{t}} - 0.9\mu_{\mathrm{c}} - 2.01$. With the posterior of Step 2, which does not change,

$$
\tau_{\mathrm{fs}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}\bigl(8.6, 7.3^2\bigr) \quad (\rho = 1), \qquad \text{compared with } \mathcal{N}(8.7, 5.2^2) \quad (\rho = 0).
$$
The point estimate barely moves, but the uncertainty grows by forty percent. The reason is that with $\rho = 1$ the imputed outcomes carry no unit-level noise of their own: each is the observed outcome shifted and rescaled by the uncertain parameters, so the errors in $\mu_{\mathrm{c}}$ and $\mu_{\mathrm{t}}$ enter every imputation in the same direction and do not average out, and the coefficients $1.125$ and $-0.9$ amplify them. This parallels Neyman's analysis, in which the sampling variance of $\hat\tau^{\mathrm{dif}}$ is largest when the potential outcomes are perfectly correlated (Theorem 4.3.2). Independence ($\rho = 0$) is a convenient default, but the analyst should know that it is a choice and not a finding.

## 6.5. Covariates

Covariates enter through the outcome model, for example

$$
Y_i(0) \mid X_i, \theta \sim \mathcal{N}\bigl(X_i\boldsymbol{\beta}_{\mathrm{c}}, \sigma_{\mathrm{c}}^2\bigr), \qquad
Y_i(1) \mid X_i, \theta \sim \mathcal{N}\bigl(X_i\boldsymbol{\beta}_{\mathrm{t}}, \sigma_{\mathrm{t}}^2\bigr),
$$
with $X_i$ containing an intercept and $\theta = (\boldsymbol{\beta}_{\mathrm{c}}, \boldsymbol{\beta}_{\mathrm{t}}, \sigma_{\mathrm{c}}^2, \sigma_{\mathrm{t}}^2)$. The procedure is the same: in Step 1 the missing $Y_i(1)$ of a control unit is drawn from the treated-group regression evaluated at the unit's own covariates, and Step 2 is a pair of Bayesian linear regressions. This is the Bayesian version of the interacted regression of [3.9.5](/3.9.5), with the added benefit that the uncertainty about the coefficients is propagated to the imputations. With unknown variances, or with non-normal models, the steps no longer have closed forms, and simulation is used.

## 6.6. Implementation by Simulation

In most models Steps 2 and 3 cannot be computed analytically. A distribution can, however, be represented by a large sample from it: if $\theta^{(1)}, \dots, \theta^{(S)}$ are draws from $p(\theta \mid y)$, then $\mathbb{E}[h(\theta) \mid y] \approx \frac{1}{S}\sum_{s}h(\theta^{(s)})$, with error of order $S^{-1/2}$ by the law of large numbers and the central limit theorem. Probabilities, quantiles and densities of any function of the unknowns are obtained in the same way. The four steps become a loop.

**Algorithm 6.6.1 (Model-Based Imputation by Simulation)** For $s = 1, \dots, S$:

1. draw $\theta^{(s)}$ from the posterior $p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})$, directly or as the current state of a Markov chain;
2. draw $\boldsymbol{Y}^{\mathrm{mis}, (s)}$ from $f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta^{(s)})$;
3. compute $\tau^{(s)} = \tilde\tau(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{mis}, (s)}, \boldsymbol{W})$.

The draws $\tau^{(1)}, \dots, \tau^{(S)}$ are a sample from the posterior of $\tau$.

:::

Drawing $\theta^{(s)}$ and then $\boldsymbol{Y}^{\mathrm{mis}, (s)}$ given it is a draw from their joint posterior, so $\boldsymbol{Y}^{\mathrm{mis}, (s)}$ is a draw from the marginal of Step 3: the integral over $\theta$ is done by simulation. When the posterior of $\theta$ is not of standard form, step 1 uses **Markov chain Monte Carlo** ([3.5.9](/3.5.9)). For the normal model with unknown variances, $\theta$ splits into blocks whose full conditional distributions are normal (the means) and scaled inverse-$\chi^2$ (the variances), and the **Gibbs sampler** draws them in turn; for non-conjugate blocks, such as the coefficients of a logistic regression, a **Metropolis–Hastings algorithm** step is used. Applied to the six-unit example, the loop reproduces the analytic posterior of Example 6.3.1.

![Left: 20 000 draws of the finite-sample average effect for the six NSW units from Algorithm 6.6.1 under the normal model of Example 6.3.1, with the analytic normal posterior. Right: analytic posteriors of the finite-sample effect with independent (rho = 0) and perfectly correlated (rho = 1) potential outcomes, and of the super-population effect](./plots/posterior_tau.py)

## 6.7. The Super-Population Effect

For the super-population estimand the imputation is unnecessary. With i.i.d. units, $\tau_{\mathrm{sp}} = \mathbb{E}[Y_i(1) - Y_i(0) \mid \theta] = \tau(\theta)$ is a function of the parameter alone, so its posterior follows from Step 2 directly. In the normal model, $\tau_{\mathrm{sp}} = \mu_{\mathrm{t}} - \mu_{\mathrm{c}}$, and for the six units

$$
\tau_{\mathrm{sp}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \sim \mathcal{N}\bigl(12.77 - 4.12,\ 21.3 + 33.2\bigr) = \mathcal{N}\bigl(8.7, 7.4^2\bigr).
$$
The posterior standard deviation $7.4$ is larger than the $5.2$ for $\tau_{\mathrm{fs}}$ (with $\rho = 0$). The reason is the one found for Neyman's approach in Theorem 4.6.1: the finite-sample effect is partly observed, since for each unit one of the two potential outcomes is known, while the population effect must also account for the sampling of the units. If the simulation of Algorithm 6.6.1 is used for $\tau_{\mathrm{sp}}$, step 2 can be omitted and $\tau^{(s)} = \tau(\theta^{(s)})$.

## 6.8. Example: Four Models for the NSW Data

Four models were fitted to the full NSW data, each with independent normal priors $\mathcal{N}(0, 100^2)$ on the regression or mean parameters and scaled inverse-$\chi^2$ priors $\mathrm{Inv}\text{-}\chi^2(2, 0.1^2)$ on the variances (earnings in thousands of dollars), so that the data dominate:

| Model | Mean depends on covariates | Variance specific to treatment | Potential outcomes independent | Two-part model |
|---|---|---|---|---|
| $M_1$: normal, common variance | no | no | no | no |
| $M_2$: normal | no | yes | yes | no |
| $M_3$: normal regression | yes | yes | yes | no |
| $M_4$: zero-inflated log-normal regression | yes | yes | yes | yes |

Model $M_4$ treats earnings as a two-part outcome: a logistic regression for the probability of positive earnings and a normal linear regression for log earnings among those with positive earnings, each separately for the two potential outcomes. Models $M_1$–$M_3$ have conjugate full conditionals and are fitted by Gibbs sampling; in $M_4$ the logistic part is updated by an independence Metropolis–Hastings step, with a normal proposal centered at the maximum likelihood estimate and covariance twice its estimated covariance matrix, and the log-normal part by Gibbs sampling. Starting values are maximum likelihood estimates, and the first third of each chain is discarded as burn-in.

Posterior means (standard deviations) of the finite-sample effects on the mean and on the quartiles, where the effect on a quantile is the difference between the quantile of the $N$ values $Y_i(1)$ and that of the $N$ values $Y_i(0)$:

| Model | Mean effect | 0.25 quantile | 0.50 quantile | 0.75 quantile |
|---|---|---|---|---|
| $M_1$ | 1.79 (0.63) | 1.79 (0.63) | 1.79 (0.63) | 1.79 (0.63) |
| $M_2$ | 1.78 (0.49) | 0.63 (0.35) | 1.63 (0.55) | 3.07 (0.64) |
| $M_3$ | 1.57 (0.50) | 0.42 (0.34) | 1.40 (0.55) | 2.89 (0.63) |
| $M_4$ | 1.79 (0.85) | 0.25 (0.30) | 1.03 (0.53) | 1.69 (0.72) |

For comparison, Neyman's estimate is 1.79 (0.67) and the covariate-adjusted regression estimate 1.67 (0.64).

Three lessons follow. First, all models agree that training raised average earnings by roughly 1.6 to 1.8 thousand dollars. Second, the quantile effects depend strongly on the model: $M_1$ assumes a pure shift of a normal distribution, so every quantile effect equals the mean effect, while the other models let the spreads differ. Third, the normal models misdescribe an outcome that is zero for many men and highly skewed for the rest; $M_4$ respects both features, and it is the most realistic of the four. Its larger posterior standard deviation for the mean effect is an honest consequence of the skewness, and it shows that a small effect at the lower quartile (most men in both groups earn little) coexists with gains concentrated in the upper part of the distribution. The model-based approach makes such distributional estimands as easy to estimate as the mean, which none of the earlier methods does.

## Summary

| | Fisher | Neyman | Regression | Model-based |
|---|---|---|---|---|
| Question | any effect? | average effect | average effect with covariates | any estimand, through a model |
| Random | $\boldsymbol{W}$ | $\boldsymbol{W}$ (and sampling) | $\boldsymbol{W}$, sampling | everything not observed |
| Output | exact p-value | estimate, variance, interval | estimate, robust s.e. | posterior distribution |

- Inputs: the assignment mechanism, a model $f(Y_i(0), Y_i(1) \mid \theta)$ (from exchangeability), and a prior $p(\theta)$ (Definition 6.3.1).
- Four steps: $f(\boldsymbol{Y}^{\mathrm{mis}} \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W}, \theta)$; $p(\theta \mid \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W})$; integrate over $\theta$ to get the imputation distribution; transform to $\tau$. Under unconfounded assignment the assignment mechanism drops out (Theorem 6.3.1).
- Independent potential outcomes: missing $Y_i(1)$ of controls are drawn from the treated-group model and vice versa; with independent priors, each group's parameters are learned from that group.
- Normal example: imputations are multivariate normal (shared parameter uncertainty induces correlations), $\tau_{\mathrm{fs}} \sim \mathcal{N}(8.7, 5.2^2)$; binary example: imputed counts are beta-binomial.
- The correlation $\rho$ of the potential outcomes is not identified; its posterior equals its prior, and $\rho = 1$ gives the widest posterior for $\tau_{\mathrm{fs}}$ ($7.3$ vs $5.2$).
- Simulation (Algorithm 6.6.1): draw $\theta$, draw $\boldsymbol{Y}^{\mathrm{mis}}$, compute $\tau$; MCMC when needed.
- $\tau_{\mathrm{sp}} = \tau(\theta)$ needs no imputation and has a wider posterior than $\tau_{\mathrm{fs}}$ ($7.4$ vs $5.2$), as in Neyman's approach.
- NSW: mean effects near 1.8 thousand dollars in all models; quantile effects depend on the model, and the zero-inflated log-normal model is the realistic one.

## Questions

1. In Example 6.3.1 suppose the prior variance of $\mu_{\mathrm{c}}$ and $\mu_{\mathrm{t}}$ tends to infinity. What is the limiting posterior of $\tau_{\mathrm{fs}}$? Compare its variance with the Neyman variance estimate based on the known outcome variances.

   **Answer** In the limit the posteriors are $\mu_{\mathrm{c}} \sim \mathcal{N}(\bar Y_{\mathrm{c}}^{\mathrm{obs}}, \sigma_{\mathrm{c}}^2/N_{\mathrm{c}}) = \mathcal{N}(4.13, 33.3)$ and $\mu_{\mathrm{t}} \sim \mathcal{N}(12.8, 21.3)$. The mean of $\tau_{\mathrm{fs}}$ becomes exactly $\frac{1}{6}(3 \cdot 12.8 - 12.4 + 38.4 - 3 \cdot 4.13) = 8.67 = \hat\tau^{\mathrm{dif}}$. Its variance is $\frac{1}{36}\bigl[N_{\mathrm{c}}\sigma_{\mathrm{t}}^2 + N_{\mathrm{c}}^2\sigma_{\mathrm{t}}^2/N_{\mathrm{t}} + N_{\mathrm{t}}\sigma_{\mathrm{c}}^2 + N_{\mathrm{t}}^2\sigma_{\mathrm{c}}^2/N_{\mathrm{c}}\bigr] = \frac{1}{36}(192 + 192 + 300 + 300) = 27.3$. In general, with $N = N_{\mathrm{c}} + N_{\mathrm{t}}$, this equals $\frac{N_{\mathrm{c}}}{N}\cdot\frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}} + \frac{N_{\mathrm{t}}}{N}\cdot\frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}}$, which is smaller than the Neyman variance $\sigma_{\mathrm{c}}^2/N_{\mathrm{c}} + \sigma_{\mathrm{t}}^2/N_{\mathrm{t}} = 54.6$: here exactly half of it, because $N_{\mathrm{t}} = N_{\mathrm{c}}$. The Neyman variance refers to the super-population (compare Section 6.7, $54.5$), the posterior of $\tau_{\mathrm{fs}}$ to the finite sample, in which half of the potential outcomes are known.

2. Prove that under a Bernoulli trial (each unit independently treated with known probability $q$) the posterior of $\theta$ is the same as under a CRE with the same observed data.

   **Answer** The Bernoulli assignment mechanism $\prod_i q^{W_i}(1 - q)^{1 - W_i}$ does not depend on the potential outcomes or on $\theta$. In Step 2 it is a constant factor of $f(\boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{W} \mid \theta)$, as is $\binom{N}{N_{\mathrm{t}}}^{-1}$ in a CRE, and it cancels in the normalization. Both posteriors are therefore proportional to $p(\theta)\int f(\boldsymbol{Y}(0), \boldsymbol{Y}(1) \mid \theta)\,\mathrm{d}\boldsymbol{Y}^{\mathrm{mis}}$ (Theorem 6.3.1).

3. Give an assignment mechanism for which Theorem 6.3.1 fails, and explain what goes wrong.

   **Answer** Example 2.2.3: the unit with the larger unit-level effect is treated. Then $\mathbb{P}(\boldsymbol{W} \mid \boldsymbol{Y}(0), \boldsymbol{Y}(1))$ is an indicator depending on the missing outcomes and does not cancel from Step 1: the observed assignment tells us that the missing outcomes satisfy an inequality, and an imputation that ignores this draws values incompatible with the design. Equivalently, the treated units are not a random sample of the population, so the treated-group model cannot be used to impute $Y_i(1)$ for control units.

4. (Binary outcomes) In a CRE with $N_{\mathrm{t}} = N_{\mathrm{c}} = 4$, three treated and one control unit have outcome $1$. With $\mathrm{Beta}(1, 1)$ priors and independent potential outcomes, find the posterior distribution of the number $M_1$ of control units that would have had outcome $1$ under treatment, and the posterior mean of $\tau_{\mathrm{fs}}$.

   **Answer** $\pi_{\mathrm{t}} \mid \text{data} \sim \mathrm{Beta}(4, 2)$, so $M_1 \sim \mathrm{BetaBin}(4, 4, 2)$, $\mathbb{P}(M_1 = m) = \binom{4}{m}\mathrm{B}(m + 4, 6 - m)/\mathrm{B}(4, 2)$. With $\mathrm{B}(4, 2) = 1/20$, for example $\mathbb{P}(M_1 = 4) = 20\,\mathrm{B}(8, 2) = 20/72 = 0.278$ and $\mathbb{P}(M_1 = 0) = 20\,\mathrm{B}(4, 6) = 20/504 = 0.040$; the full distribution of $M_1 = 0, 1, \dots, 4$ is $0.040, 0.127, 0.238, 0.317, 0.278$. Its mean is $\mathbb{E}[M_1] = 4 \cdot 4/6 = 2.67$; similarly $\pi_{\mathrm{c}} \sim \mathrm{Beta}(2, 4)$ and $\mathbb{E}[M_0] = 4 \cdot 2/6 = 1.33$. Then $\mathbb{E}[\tau_{\mathrm{fs}}] = \frac{1}{8}(3 + 2.67 - 1 - 1.33) = 0.417$, compared with $\hat\tau^{\mathrm{dif}} = 0.75 - 0.25 = 0.5$.

5. Explain why the posterior of $\rho$ equals its prior in the model of Section 6.4, and why this does not make $\rho$ irrelevant.

   **Answer** Each unit's contribution to the observed-data likelihood is the marginal density of the one observed potential outcome; in the bivariate normal the marginals depend on $(\mu_{\mathrm{c}}, \sigma_{\mathrm{c}}^2)$ or $(\mu_{\mathrm{t}}, \sigma_{\mathrm{t}}^2)$ only. So the likelihood is constant in $\rho$, and with $\rho$ a priori independent of the other parameters, Bayes' theorem returns the prior. But the conditional distribution of a missing outcome given the observed one depends on $\rho$ (Step 1), so the posterior of $\tau_{\mathrm{fs}}$, and of any estimand involving the joint distribution such as the proportion of units with $Y_i(1) > Y_i(0)$, depends on it. The data cannot settle the question; the analyst must argue for a value or report a sensitivity analysis.

6. For the super-population estimand in the normal model, why is no imputation needed? Show for Example 6.3.1 that the posterior variance of $\tau_{\mathrm{sp}}$ minus that of $\tau_{\mathrm{fs}}$ (with $\rho = 0$) is positive, and interpret the difference.

   **Answer** $\tau_{\mathrm{sp}} = \mu_{\mathrm{t}} - \mu_{\mathrm{c}}$ is a function of $\theta$ only, so its posterior follows from Step 2. The variances are $54.5$ and $27.3$, difference $27.2 > 0$. Writing $\tau_{\mathrm{fs}} = \frac{1}{N}\sum_i(Y_i(1) - Y_i(0))$, half of the terms involve observed values, which are fixed given the data, and the other half are imputed with variance coming from both $\theta$ and the unit-level noise. $\tau_{\mathrm{sp}}$ involves the whole population, none of which is fixed by the data. The difference corresponds to the term $\sigma_{\mathrm{tc}}^2/N$ that separates the finite-sample and super-population variances in Theorem 4.6.1.

7. Write out the Gibbs sampler for model $M_2$ of Section 6.8 (independent normal, treatment-specific variances, priors $\mu_w \sim \mathcal{N}(0, \omega^2)$ and $\sigma_w^2 \sim \mathrm{Inv}\text{-}\chi^2(M, S_0^2)$), including the imputation step for $\tau_{\mathrm{fs}}$.

   **Answer** For $w \in \{\mathrm{c}, \mathrm{t}\}$, with $N_w$ units and mean $\bar Y_w^{\mathrm{obs}}$ in group $w$: (1) draw $\mu_w \mid \sigma_w^2 \sim \mathcal{N}\Bigl(\frac{N_w\bar Y_w^{\mathrm{obs}}/\sigma_w^2}{N_w/\sigma_w^2 + 1/\omega^2}, \frac{1}{N_w/\sigma_w^2 + 1/\omega^2}\Bigr)$; (2) draw $\sigma_w^2 \mid \mu_w$ from $\mathrm{Inv}\text{-}\chi^2\Bigl(M + N_w, \frac{MS_0^2 + \sum_{i \in w}(Y_i^{\mathrm{obs}} - \mu_w)^2}{M + N_w}\Bigr)$, that is, $\bigl(MS_0^2 + \sum_{i \in w}(Y_i^{\mathrm{obs}} - \mu_w)^2\bigr)/\sigma_w^2 \sim \chi^2_{M + N_w}$; the two groups are conditionally independent. (3) Impute $Y_i^{\mathrm{mis}} \sim \mathcal{N}(\mu_{\mathrm{t}}, \sigma_{\mathrm{t}}^2)$ for control units and $\mathcal{N}(\mu_{\mathrm{c}}, \sigma_{\mathrm{c}}^2)$ for treated units; (4) compute $\tau_{\mathrm{fs}} = \frac{1}{N}\sum_i(2W_i - 1)(Y_i^{\mathrm{obs}} - Y_i^{\mathrm{mis}})$. Repeat, discarding a burn-in.

8. Why is the zero-inflated log-normal model more appropriate for the NSW data, and why can it give a quite different effect on the lower quartile?

   **Answer** A large fraction of the men (roughly a quarter of the treated and a third of the controls) had zero earnings in 1978, and positive earnings are strongly right-skewed. A normal model places positive probability on negative earnings and none on exactly zero, and it ties all quantiles to the mean and variance. The two-part model separates the effect of training on the probability of having any earnings from the effect on the amount earned. At the lower quartile, many men in both groups would have zero or very low earnings under either treatment, so the quantile effect is close to zero (0.25 in $M_4$), while the normal models extrapolate a symmetric shape and overstate it.
