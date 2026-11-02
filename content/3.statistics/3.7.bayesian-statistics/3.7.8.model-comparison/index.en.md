---
title: Model Comparison
description: Predictive accuracy (mse, log predictive density, elpd, elppd and the within-sample lppd), AIC with its asymptotic derivation, DIC, WAIC and leave-one-out cross-validation as bias-corrected estimates of out-of-sample accuracy, the eight schools comparison, BIC, and Bayes factors with the hemophilia example, Jeffreys' scale, Lindley's paradox, improper priors and the Laplace approximation behind BIC.
---

Model checking ([3.7.7](/3.7.7)) asks whether one model fits the data, using discrepancy measures aimed at particular failures. Model comparison asks which of several models is better, and it serves a second purpose as well: the comparison of an expanded model with the current one shows in which direction a model can be improved. Two kinds of answer are developed in this chapter. The first judges a model by its predictive accuracy for new data (§8.1). Since new data are usually unavailable, accuracy must be estimated from the data used to fit the model, and the central difficulty is to correct for the optimism of evaluating a model on its own training data. The information criteria AIC, DIC and WAIC correct the within-sample accuracy by an effective number of parameters (§8.2–§8.4); cross-validation holds data out instead (§8.5). The eight schools example of [3.7.6](/3.7.6) compares all of them (§8.6). The second answer is the Bayesian answer to model selection proper: the posterior probability of each model, governed by the **Bayes factor** of [3.2.7](/3.2.7) (§8.8), with BIC as its large-sample approximation (§8.7). The two answers pursue different goals, prediction and identification of the true model, and they can disagree.

## 8.1. Measures of Predictive Accuracy

Predictive accuracy is one way to evaluate a model. Sometimes it is valued for its own sake, as in judging a forecast; more often it is a yardstick for comparing models. The accuracy of predictions can be measured in many ways: classification accuracy, monetary cost, mean squared error, or the log-likelihood. Which measure is appropriate depends on the kind of prediction.

### 8.1.1. Point and Probabilistic Prediction

In *point prediction* a single value is reported as the prediction of each observation, and a natural measure of accuracy is the mean squared error of the predictions $\mathbb{E}(y_i\mid\theta)$,

$$
\frac1n\sum_{i=1}^n\big(y_i-\mathbb{E}(y_i\mid\theta)\big)^2,\qquad\text{or the weighted version}\qquad\frac1n\sum_{i=1}^n\frac{\big(y_i-\mathbb{E}(y_i\mid\theta)\big)^2}{\operatorname{Var}(y_i\mid\theta)}.
$$
These are easy to interpret but are less appropriate for models far from normal, and they ignore the uncertainty of the prediction. In *probabilistic prediction* the full predictive distribution is reported, and it should be judged as a distribution.

**Definition 8.1.1 (Log Predictive Density)** The **log predictive density** of data $y$ under a model with parameter $\theta$ is $\log p(y\mid\theta)$, the logarithm of the **likelihood function** evaluated at the data. For a predictive distribution with density $g$, the log predictive density of an observation $\tilde y$ is $\log g(\tilde y)$, the logarithmic score of the prediction.

The log predictive density is the measure used in the rest of the chapter, for two reasons.

- In a normal model with constant variance, $\log p(y\mid\theta)=-\frac n2\log(2\pi\sigma^2)-\frac1{2\sigma^2}\sum_i\big(y_i-\mathbb{E}(y_i\mid\theta)\big)^2$ is a linear function of the mean squared error, so the two measures agree.
- If the data come from a true density $f$, the expected log predictive density of a prediction $g$ is $\mathbb{E}_f\log g(\tilde y)=\mathbb{E}_f\log f(\tilde y)-\operatorname{KL}(f\,\Vert\,g)$. The first term does not depend on the model, so maximizing the expected log predictive density is the same as minimizing the **Kullback–Leibler divergence** from the truth to the prediction.

### 8.1.2. Out-of-Sample and Within-Sample Accuracy

A Bayesian prediction of a new observation $\tilde y_i$ is not $p(\tilde y_i\mid\theta)$ at a particular $\theta$ but the posterior predictive density $p_{\mathrm{post}}(\tilde y_i)=\int p(\tilde y_i\mid\theta)\,p_{\mathrm{post}}(\theta)\,\mathrm{d}\theta$, with $p_{\mathrm{post}}(\theta)=p(\theta\mid y)$. Its log predictive density is

$$
\log p_{\mathrm{post}}(\tilde y_i)=\log\mathbb{E}_{\mathrm{post}}\big(p(\tilde y_i\mid\theta)\big)=\log\int p(\tilde y_i\mid\theta)\,p_{\mathrm{post}}(\theta)\,\mathrm{d}\theta.
$$

**Definition 8.1.2 (Expected Log Pointwise Predictive Density)** Let $f$ be the true distribution that generates the data. The expected log predictive density for a new data point, and the **expected log pointwise predictive density** for a new data set of $n$ points, are

$$
\mathrm{elpd}=\mathbb{E}_f\big(\log p_{\mathrm{post}}(\tilde y_i)\big)=\int\big(\log p_{\mathrm{post}}(\tilde y)\big)f(\tilde y)\,\mathrm{d}\tilde y,\qquad\mathrm{elppd}=\sum_{i=1}^n\mathbb{E}_f\big(\log p_{\mathrm{post}}(\tilde y_i)\big).
$$

The elppd measures out-of-sample predictive accuracy, and it is the key quantity for model comparison: of two models, the one with the larger elppd predicts new data better on average. It cannot be computed, because $f$ is unknown. What can be computed is the accuracy for the data at hand.

**Definition 8.1.3 (Log Pointwise Predictive Density)** The **log pointwise predictive density** of the observed data $y=(y_1,\dots,y_n)$ is

$$
\mathrm{lppd}=\log\prod_{i=1}^np_{\mathrm{post}}(y_i)=\sum_{i=1}^n\log\int p(y_i\mid\theta)\,p_{\mathrm{post}}(\theta)\,\mathrm{d}\theta.
$$
Given draws $\theta^1,\dots,\theta^S$ from the posterior, it is computed by Monte Carlo integration as

$$
\widehat{\mathrm{lppd}}=\sum_{i=1}^n\log\Big(\frac1S\sum_{s=1}^{S}p(y_i\mid\theta^s)\Big).
$$

The lppd is within-sample predictive accuracy, and it usually overestimates the elppd: the same data are used to fit the model and to assess it, and the optimism is likely to grow with the number of parameters. There are two ways to estimate the elppd from the available data.

- *Adjusted within-sample accuracy*: subtract from the lppd (or from the log predictive density at a point estimate) a correction for the bias, which takes the form of an *effective number of parameters*, the amount of fitting to noise the model is capable of. AIC, DIC and WAIC are of this form; they are quick and need only one fit.
- Cross-validation: fit the model to part of the data and evaluate its predictive accuracy on the held-out part; this is closer to the definition but can be computationally expensive.

For historical reasons, measures of predictive accuracy are called information criteria and are reported on the scale of the *deviance* $D(\theta)=-2\log p(y\mid\theta)$, the log predictive density multiplied by $-2$, so that smaller values are better. (In generalized linear models the deviance is customarily measured relative to the saturated model, which changes it by a constant that does not depend on $\theta$ and does not affect comparisons.)

## 8.2. Akaike Information Criterion

The oldest correction, proposed by Akaike in 1973–1974, estimates the predictive accuracy of the plug-in prediction $p(\tilde y\mid\hat\theta)$ at the **maximum likelihood estimator** $\hat\theta=\hat\theta(y)$. For large $n$ the posterior concentrates at $\hat\theta$ ([3.7.5](/3.7.5)), and $\mathrm{elpd}$ is approximated by

$$
\mathrm{elpd}_{\hat\theta}=\mathbb{E}_f\log p\big(\tilde y_i\mid\hat\theta(y)\big),
$$
the expected log density of a new point $\tilde y_i\sim f$ under the fitted model. It cannot be computed directly, but its expectation over the data can be approximated: $\hat\theta$ is asymptotically $\mathcal{N}(\theta_0,V_0/n)$, and $\tilde y_i$ is independent of $\hat\theta$, so $\mathbb{E}_{\tilde y_i\times\hat\theta}\log p(\tilde y_i\mid\hat\theta)=\mathbb{E}_{\tilde y_i}\big[\mathbb{E}_{\hat\theta}\log p(\tilde y_i\mid\hat\theta)\big]$ can be expanded around $\theta_0$.

**Proposition 8.2.1** Let $y_1,\dots,y_n\overset{\text{iid}}{\sim}f$ and let the model $p(y\mid\theta)$, $\theta\in\mathbb{R}^k$, be regular and contain the true distribution, $f=p(\cdot\mid\theta_0)$. Then, to first order as $n\to\infty$,

$$
\mathbb{E}\big[\log p(y\mid\hat\theta)\big]-n\,\mathbb{E}\big[\mathrm{elpd}_{\hat\theta}\big]\to k.
$$

**Proof** (sketch). Let $S(y,\theta)$ be the **score function** of one observation, $H(y,\theta)$ its Hessian, $J=J(\theta_0)=-\mathbb{E}_fH(y,\theta_0)$ the **Fisher information** of one observation, $c(\theta_0)=\int f(y)\log p(y\mid\theta_0)\,\mathrm{d}y$, and $Z_n=\sqrt n(\hat\theta-\theta_0)$, which converges in distribution to $\mathcal{N}(\boldsymbol{0},J^{-1})$. Expanding around $\theta_0$ and using $\mathbb{E}_fS(\tilde y,\theta_0)=\boldsymbol{0}$,

$$
\mathrm{elpd}_{\hat\theta}\approx c(\theta_0)+(\hat\theta-\theta_0)^{\mathsf T}\mathbb{E}_fS(\tilde y,\theta_0)-\frac12(\hat\theta-\theta_0)^{\mathsf T}J(\hat\theta-\theta_0)=c(\theta_0)-\frac1{2n}Z_n^{\mathsf T}JZ_n.
$$
For the within-sample term, the likelihood equation $\boldsymbol{0}=\sum_iS(y_i,\hat\theta)\approx\sum_iS(y_i,\theta_0)+\sum_iH(y_i,\theta_0)(\hat\theta-\theta_0)$ gives $\frac1n\sum_iS(y_i,\theta_0)\approx J(\hat\theta-\theta_0)$, and $\frac1n\sum_iH(y_i,\theta_0)\approx-J$, so

$$
\frac1n\log p(y\mid\hat\theta)\approx\frac1n\sum_{i=1}^n\log p(y_i\mid\theta_0)+(\hat\theta-\theta_0)^{\mathsf T}J(\hat\theta-\theta_0)-\frac12(\hat\theta-\theta_0)^{\mathsf T}J(\hat\theta-\theta_0)=\frac1n\sum_{i=1}^n\log p(y_i\mid\theta_0)+\frac1{2n}Z_n^{\mathsf T}JZ_n.
$$
The first term has expectation $c(\theta_0)$. Subtracting, $\mathbb{E}[\log p(y\mid\hat\theta)]-n\,\mathbb{E}[\mathrm{elpd}_{\hat\theta}]\approx\mathbb{E}[Z_n^{\mathsf T}JZ_n]=\operatorname{tr}(JJ^{-1})=k$. $\square$

The within-sample log-likelihood is therefore too optimistic by $k$ on average, and $\widehat{\mathrm{elpd}}_{\mathrm{AIC}}=\log p(y\mid\hat\theta)-k$ is an approximately unbiased estimate of $n\,\mathrm{elpd}_{\hat\theta}$. (If the model does not contain $f$, the same argument gives the correction $\operatorname{tr}(J^{-1}K)$ with $K=\operatorname{Var}_fS(y,\theta_0)$, which reduces to $k$ when $K=J$.) On the deviance scale this is the **Akaike information criterion**, already met in [3.4.11](/3.4.11).

**Definition 8.2.1 (Akaike Information Criterion)** For a model with $k$ parameters and maximum likelihood estimator $\hat\theta_{\mathrm{MLE}}$,

$$
\mathrm{AIC}=-2\log p(y\mid\hat\theta_{\mathrm{MLE}})+2k=-2\,\widehat{\mathrm{elpd}}_{\mathrm{AIC}}.
$$
Smaller values indicate higher estimated predictive accuracy.

A practical rule is that a difference of less than $2$ between the AICs of two models indicates no substantial difference between them. The rule has a testing interpretation. Let model 1 (simple, $k_1$ parameters) be nested in model 2 (complex, $k_2>k_1$). Then

$$
\mathrm{AIC}_1-\mathrm{AIC}_2>2\iff-2\log\frac{p(y\mid\hat\theta_1)}{p(y\mid\hat\theta_2)}>2+2(k_2-k_1),
$$
and the left side is the **likelihood ratio** statistic, approximately $\chi^2_{k_2-k_1}$ when the simple model is true. For $k_2-k_1=1$, preferring the complex model by more than $2$ means rejecting the simple one when $\chi^2_1>4$, a test at level $0.046$.

AIC is a frequentist construction: it plugs in the MLE and counts parameters. It does not apply to models whose effective complexity is not the number of parameters, such as hierarchical models, where the population distribution constrains the group parameters, and it ignores the prior.

## 8.3. Deviance Information Criterion

The deviance information criterion of Spiegelhalter et al. (2002) is a Bayesian version of AIC. It replaces the MLE by the posterior mean and the parameter count by a data-based estimate. Write $d(y,\theta,\tilde\theta)=-2\log p(y\mid\theta)+2\log p(y\mid\tilde\theta)$ for the difference between the deviance at $\theta$ and at an estimate $\tilde\theta=\tilde\theta(y)$. AIC evaluates the excess at the true value, $d(y,\theta_0,\hat\theta_{\mathrm{MLE}})$, whose expectation is about $k$. The Bayesian view treats $\theta$ as random and averages over the posterior, which is where the prior acts:

$$
p_{\mathrm{DIC}}=\mathbb{E}_{\theta\mid y}\,d(y,\theta,\tilde\theta)=\mathbb{E}_{\theta\mid y}\big[-2\log p(y\mid\theta)\big]+2\log p(y\mid\tilde\theta).
$$

**Definition 8.3.1 (Deviance Information Criterion)** Let $\hat\theta_{\mathrm{Bayes}}=\mathbb{E}(\theta\mid y)$ be the posterior mean. The **effective number of parameters** of DIC is

$$
p_{\mathrm{DIC}}=2\Big(\log p(y\mid\hat\theta_{\mathrm{Bayes}})-\mathbb{E}_{\mathrm{post}}\big(\log p(y\mid\theta)\big)\Big),\qquad\text{computed as}\qquad2\Big(\log p(y\mid\hat\theta_{\mathrm{Bayes}})-\frac1S\sum_{s=1}^S\log p(y\mid\theta^s)\Big),
$$
that is, the posterior mean deviance minus the deviance at the posterior mean. With $\widehat{\mathrm{elpd}}_{\mathrm{DIC}}=\log p(y\mid\hat\theta_{\mathrm{Bayes}})-p_{\mathrm{DIC}}$, the **deviance information criterion** is

$$
\mathrm{DIC}=-2\log p(y\mid\hat\theta_{\mathrm{Bayes}})+2p_{\mathrm{DIC}}=-2\,\widehat{\mathrm{elpd}}_{\mathrm{DIC}}.
$$

With a flat prior and a nearly normal posterior, $p_{\mathrm{DIC}}\approx k$ and DIC reduces to AIC. With an informative prior or a hierarchical structure, the parameters are not free to fit the noise, and $p_{\mathrm{DIC}}$ is smaller than their number.

**Example 8.3.1 (Effective Number of Parameters in a Hierarchical Model)** Consider the hierarchical normal model with known group variances, $\bar y_{\cdot i}\mid\theta_i\sim\mathcal{N}(\theta_i,\sigma_i^2)$ and $\theta_i\sim\mathcal{N}(\mu,\tau^2)$, $i=1,\dots,J$, and let

$$
\rho_i=\frac{\tau^2}{\tau^2+\sigma_i^2}
$$
be the fraction of the variance of $\bar y_{\cdot i}$ due to the variation of the group means (the intraclass correlation in group $i$).

- If $\mu$ and $\tau^2$ are known, $p_{\mathrm{DIC}}=\sum_i\rho_i$.
- If $\tau^2$ is known and $\mu$ has a uniform hyperprior, $p_{\mathrm{DIC}}=\sum_i\rho_i+\dfrac{\sum_i\rho_i(1-\rho_i)}{\sum_i\rho_i}$; if moreover all $\sigma_i^2$ are equal, so that $\rho_i=\rho$, this is $p_{\mathrm{DIC}}=1+(J-1)\rho$.

*Derivation.* For this normal likelihood, $-2\log p(y\mid\theta)=\sum_i(\bar y_{\cdot i}-\theta_i)^2/\sigma_i^2+\text{const}$, and for this quadratic form the posterior mean deviance minus the deviance at the posterior mean is $p_{\mathrm{DIC}}=\sum_i\operatorname{Var}(\theta_i\mid y)/\sigma_i^2$. With $\mu,\tau$ known, $\theta_i\mid y\sim\mathcal{N}\big(\rho_i\bar y_{\cdot i}+(1-\rho_i)\mu,\rho_i\sigma_i^2\big)$, which gives $\sum_i\rho_i$. With $\mu$ unknown, $\theta_i=\rho_i\bar y_{\cdot i}+(1-\rho_i)\mu+\text{noise}$ with $\operatorname{Var}(\mu\mid y)=\big(\sum_j(\sigma_j^2+\tau^2)^{-1}\big)^{-1}$ ([3.7.6](/3.7.6)), so $\operatorname{Var}(\theta_i\mid y)=\rho_i\sigma_i^2+(1-\rho_i)^2\operatorname{Var}(\mu\mid y)$. Since $(1-\rho_i)^2/\sigma_i^2=\rho_i(1-\rho_i)/\tau^2$ and $(\sigma_j^2+\tau^2)^{-1}=\rho_j/\tau^2$, the extra term is $\sum_i\rho_i(1-\rho_i)/\sum_j\rho_j$. For equal $\rho_i=\rho$ it equals $1-\rho$, and $p_{\mathrm{DIC}}=J\rho+1-\rho$. $\square$

The two limits are instructive. As $\tau\to\infty$ ($\rho\to1$, no pooling) $p_{\mathrm{DIC}}\to J$, one parameter per group; as $\tau\to0$ ($\rho\to0$, complete pooling) $p_{\mathrm{DIC}}\to1$, the common mean. A hierarchical model lies in between, and its effective number of parameters is determined by the data through $\tau$.

DIC still uses a point estimate, so it depends on the parametrization ($\hat\theta_{\mathrm{Bayes}}$ is not invariant) and can behave badly when the posterior mean is a poor summary, for instance for a bimodal posterior.

## 8.4. Watanabe–Akaike Information Criterion

The Watanabe–Akaike (or widely applicable) information criterion of Watanabe (2010) is a more fully Bayesian approach. It starts from the lppd, the within-sample accuracy of the actual posterior predictive distribution, rather than from a plug-in estimate; it estimates the effective number of parameters pointwise; and it can be derived as an approximation to cross-validation.

**Definition 8.4.1 (Watanabe–Akaike Information Criterion)** Let $\mathrm{lppd}$ be as in Definition 8.1.3. Two estimates of the effective number of parameters are

$$
p_{\mathrm{WAIC}1}=2\sum_{i=1}^n\Big(\log\big(\mathbb{E}_{\mathrm{post}}p(y_i\mid\theta)\big)-\mathbb{E}_{\mathrm{post}}\big(\log p(y_i\mid\theta)\big)\Big),\qquad p_{\mathrm{WAIC}2}=\sum_{i=1}^n\operatorname{Var}_{\mathrm{post}}\big(\log p(y_i\mid\theta)\big),
$$
computed from posterior draws as

$$
\hat p_{\mathrm{WAIC}1}=2\sum_{i=1}^n\Big(\log\Big(\frac1S\sum_{s=1}^{S}p(y_i\mid\theta^s)\Big)-\frac1S\sum_{s=1}^S\log p(y_i\mid\theta^s)\Big),\qquad\hat p_{\mathrm{WAIC}2}=\sum_{i=1}^nV_{s=1}^S\log p(y_i\mid\theta^s),
$$
where $V_{s=1}^S$ denotes the sample variance over the draws. With $\widehat{\mathrm{elppd}}_{\mathrm{WAIC}}=\mathrm{lppd}-p_{\mathrm{WAIC}}$, the **Watanabe–Akaike information criterion** is $\mathrm{WAIC}=-2\,\widehat{\mathrm{elppd}}_{\mathrm{WAIC}}$.

Both corrections are sums over data points of a measure of how much the posterior uncertainty affects the fit to that point. By Jensen's inequality $p_{\mathrm{WAIC}1}\ge0$, and the two are asymptotically equal for regular models; $p_{\mathrm{WAIC}2}$ is generally recommended because its behavior is closer to that of leave-one-out cross-validation. Unlike DIC, WAIC averages over the posterior instead of conditioning on a point estimate, so it is invariant to reparametrization, and it works for singular models such as mixtures, where the posterior is far from normal. Because it is computed pointwise, it requires the data to be partitioned into conditionally independent pieces $y_i$, which is natural for regression but not for, say, time series or spatial data.

**Remark 8.4.1 (Theoretical Background)** Watanabe's theory distinguishes regular from singular models (the Hessian of the log-likelihood at the true distribution is positive definite or not) and realizable from unrealizable ones (the true distribution is in the model or not). If the true distribution is regular for and realizable by the model, WAIC is asymptotically equivalent to AIC and DIC; otherwise they are not equivalent. Even when the true distribution is singular for or unrealizable by the model, WAIC is asymptotically equivalent, as a random variable, to Bayesian leave-one-out cross-validation.

## 8.5. Cross-Validation

**Cross-validation** estimates out-of-sample accuracy by holding data out. The data are partitioned into a training set $y_{\mathrm{train}}$ and a validation set $y_{\mathrm{validation}}$; the model is fitted to the training data, giving the posterior $p_{\mathrm{train}}(\theta)=p(\theta\mid y_{\mathrm{train}})$; and the fit is evaluated by the log predictive density of the validation data, $\log p_{\mathrm{train}}(y_{\mathrm{validation}})=\log\int p(y_{\mathrm{validation}}\mid\theta)\,p_{\mathrm{train}}(\theta)\,\mathrm{d}\theta$, typically estimated by simulation from $p_{\mathrm{train}}(\theta)$. The validation data play the role of new data, so no correction for optimism is needed beyond the fact that the model is fitted to fewer data.

**Definition 8.5.1 (Leave-One-Out Cross-Validation)** In **leave-one-out cross-validation** the model is fitted $n$ times, each time leaving out one point $y_i$, whose posterior is $p_{\mathrm{post}(-i)}(\theta)=p(\theta\mid y_{-i})$. The estimated lppd is

$$
\mathrm{lppd}_{\mathrm{loo\text{-}cv}}=\sum_{i=1}^n\log p_{\mathrm{post}(-i)}(y_i),\qquad\text{computed as}\qquad\sum_{i=1}^n\log\Big(\frac1S\sum_{s=1}^{S}p(y_i\mid\theta^{is})\Big),
$$
where $\theta^{is}$, $s=1,\dots,S$, are draws from $p_{\mathrm{post}(-i)}$. The implied effective number of parameters is $p_{\mathrm{loo\text{-}cv}}=\mathrm{lppd}-\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$.

Each fit uses $n-1$ instead of $n$ data points, so $\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$ slightly underestimates the accuracy of the model fitted to all the data. A bias-corrected version is

$$
\mathrm{lppd}_{\mathrm{cloo\text{-}cv}}=\mathrm{lppd}_{\mathrm{loo\text{-}cv}}+b,\qquad b=\mathrm{lppd}-\overline{\mathrm{lppd}}_{-i},\qquad\overline{\mathrm{lppd}}_{-i}=\frac1n\sum_{i=1}^n\sum_{j=1}^n\log p_{\mathrm{post}(-i)}(y_j),
$$
where $\overline{\mathrm{lppd}}_{-i}$ is computed as $\frac1n\sum_i\sum_j\log\big(\frac1S\sum_sp(y_j\mid\theta^{is})\big)$; for large $n$ the correction $b$ is usually ignored. Exact leave-one-out cross-validation needs $n$ posterior simulations. In practice it is approximated from a single fit by importance sampling with weights $1/p(y_i\mid\theta^s)$, stabilized by Pareto smoothing (PSIS-LOO). Cross-validation, like WAIC, requires the data to be divisible into exchangeable or conditionally independent pieces, and the choice of the pieces (individual observations or whole groups of a hierarchical model) defines what "new data" means.

## 8.6. Example: Eight Schools

**Example 8.6.1** Recall the eight schools of [3.7.6](/3.7.6): in eight randomized experiments, the estimated effects $y_j$ of special coaching on SAT verbal scores, with standard errors $\sigma_j$, are

| School | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| $y_j$ | $28$ | $8$ | $-3$ | $7$ | $-1$ | $1$ | $18$ | $12$ |
| $\sigma_j$ | $15$ | $10$ | $16$ | $11$ | $9$ | $11$ | $10$ | $18$ |

The data are treated as eight normally distributed observations $y_j\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2)$ with known variances, and three models are compared, all with non-informative priors:

1. **no pooling** (separate estimates, $\tau=\infty$): $\theta_1,\dots,\theta_8$ with $p(\theta_1,\dots,\theta_8)\propto1$, so that $\theta_j\mid y\sim\mathcal{N}(y_j,\sigma_j^2)$;
2. **complete pooling** ($\tau=0$): $\theta_1=\cdots=\theta_8=\theta$ with $p(\theta)\propto1$, giving the pooled posterior $\theta\mid y\sim\mathcal{N}(7.7,4.1^2)$;
3. the **hierarchical model** ($\tau$ estimated): $\theta_j\mid\mu,\tau\sim\mathcal{N}(\mu,\tau^2)$ with $p(\mu,\tau)\propto1$.

The criteria, on the deviance scale and computed by the script of the figure below from posterior simulations (the last digit varies with the Monte Carlo error), are:

| | | No pooling | Complete pooling | Hierarchical |
|---|---|---|---|---|
| AIC | $-2\log p(y\mid\hat\theta_{\mathrm{MLE}})$ | $54.6$ | $59.4$ | |
| | $k$ | $8$ | $1$ | |
| | $\mathrm{AIC}$ | $70.6$ | $61.4$ | |
| DIC | $-2\log p(y\mid\hat\theta_{\mathrm{Bayes}})$ | $54.6$ | $59.4$ | $57.4$ |
| | $p_{\mathrm{DIC}}$ | $8.0$ | $1.0$ | $2.8$ |
| | $\mathrm{DIC}$ | $70.6$ | $61.4$ | $63.1$ |
| WAIC | $-2\,\mathrm{lppd}$ | $60.2$ | $59.8$ | $59.2$ |
| | $p_{\mathrm{WAIC}1}$ | $2.5$ | $0.6$ | $1.0$ |
| | $p_{\mathrm{WAIC}2}$ | $4.0$ | $0.7$ | $1.3$ |
| | $\mathrm{WAIC}$ (with $p_{\mathrm{WAIC}1}$) | $65.1$ | $60.9$ | $61.3$ |
| | $\mathrm{WAIC}$ (with $p_{\mathrm{WAIC}2}$) | $68.2$ | $61.1$ | $61.9$ |
| LOO-CV | $p_{\mathrm{loo\text{-}cv}}$ | | $0.7$ | $1.7$ |
| | $-2\,\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$ | | $61.1$ | $62.7$ |

![Eight schools. Left: estimated −2 elppd from AIC, DIC, WAIC (with p_WAIC2) and exact leave-one-out cross-validation for the three models; AIC is not defined for the hierarchical model and LOO-CV not for no pooling. Right: Bayes factor of complete pooling against separate effects when both models get the proper prior N(0, A²); it grows without bound as A increases (§8.8.5).](./plots/eight_schools_ic.py)

Several features deserve comment.

- No pooling fits the data perfectly at the MLE ($\hat\theta_j=y_j$), so its within-sample deviance is the lowest, but the penalty of $8$ parameters makes it the worst model by every criterion. Its corrections can be computed exactly (Question 4): $p_{\mathrm{DIC}}=8$, $p_{\mathrm{WAIC}1}=8(1-\log2)=2.45$ and $p_{\mathrm{WAIC}2}=4$. Here $p_{\mathrm{WAIC}}$ is much smaller than the number of parameters, and WAIC underestimates the optimism of a model that fits each data point with its own parameter; the pointwise corrections of WAIC rely on the data being plentiful relative to the parameters, which fails with one observation per parameter.
- Complete pooling has a single parameter and all criteria agree, $p\approx1$ or less.
- The hierarchical model has $8$ group parameters plus $\mu$ and $\tau$, yet its effective number of parameters is between $1.0$ and $2.8$, because the posterior of $\tau$ is concentrated near small values and the $\theta_j$ are strongly pooled (Example 8.3.1). AIC cannot handle it at all.
- LOO-CV is not available for no pooling: with a flat prior on each $\theta_j$, the posterior given the other seven schools says nothing about the left-out school, and its predictive distribution is improper.

The differences between complete pooling and the hierarchical model are well under $2$ on the deviance scale: with only eight data points, the data cannot distinguish them by predictive accuracy, which is consistent with the posterior of $\tau$ having much of its mass near $0$. The hierarchical model is still the natural choice, since it contains both extremes and lets the data determine the amount of pooling; the criteria confirm that the extra flexibility costs little.

## 8.7. Bayesian Information Criterion

The **Bayesian information criterion** ([3.4.11](/3.4.11)), also known as the Schwarz criterion after Gideon Schwarz (1978), is often mentioned together with AIC, but it has a different origin.

**Definition 8.7.1 (Bayesian Information Criterion)** For a model with $k$ parameters fitted to $n$ observations,

$$
\mathrm{BIC}=-2\log p(y\mid\hat\theta)+k\log n.
$$

BIC is derived as an approximation to the marginal density of the data under the model, $p(y)$, not to the predictive accuracy (§8.8.6). It is therefore related to Bayes factors rather than to elppd. It looks like AIC with a harsher penalty, $k\log n$ instead of $2k$ (harsher as soon as $n\ge8$), and it tends to choose simpler models. The two criteria answer different questions.

- BIC assumes that one of the candidate models is true and tries to find the model most likely to be true in the Bayesian sense. As $n\to\infty$ it selects the true model with probability tending to $1$ when that model is among the candidates.
- AIC and cross-validation try to find the model that predicts best, whether or not any candidate is true; a model with a superfluous parameter may predict almost as well, and AIC does not penalize it enough to exclude it.

As a rule, AIC is suited to selecting a model intended for prediction and BIC to selecting a model intended for explanation. Despite its name, BIC is not a fully Bayesian quantity: like AIC, it uses a point estimate and a parameter count and ignores the prior beyond its order of magnitude.

## 8.8. Bayes Factors

### 8.8.1. Definition

Predictive criteria rank models; Bayesian model selection in the strict sense assigns probabilities to them. Suppose two models (hypotheses) $H_1$ and $H_2$ have prior probabilities $p(H_1)$, $p(H_2)$, and each defines a full probability model for the data, so that the data have the **marginal likelihood** $p(y\mid H)=\int p(y\mid\theta,H)\,p(\theta\mid H)\,\mathrm{d}\theta$ under each.

**Definition 8.8.1 (Bayes Factor)** The **Bayes factor** of $H_2$ against $H_1$ is the ratio of the marginal likelihoods,

$$
\mathrm{BF}(H_2;H_1)=\frac{p(y\mid H_2)}{p(y\mid H_1)}=\frac{\int p(y\mid\theta_2,H_2)\,p(\theta_2\mid H_2)\,\mathrm{d}\theta_2}{\int p(y\mid\theta_1,H_1)\,p(\theta_1\mid H_1)\,\mathrm{d}\theta_1},
$$
so that, by Bayes' rule,

$$
\underbrace{\frac{p(H_2\mid y)}{p(H_1\mid y)}}_{\text{posterior odds}}=\underbrace{\frac{p(H_2)}{p(H_1)}}_{\text{prior odds}}\times\mathrm{BF}(H_2;H_1).
$$

The Bayes factor measures how much the data change the odds in favor of one model against the other: it is the ratio of **posterior odds** to **prior odds**. Conversely, a Bayes factor determines the posterior probabilities once the prior ones are given.

**Proposition 8.8.1** If $H_1$ and $H_2$ are the only possible models and $B(y)=\mathrm{BF}(H_1;H_2)$, then

$$
p(H_1\mid y)=\frac{1}{1+\dfrac{1}{B(y)}\dfrac{p(H_2)}{p(H_1)}}.
$$

**Proof** $p(H_1\mid y)+p(H_2\mid y)=1$ and $p(H_2\mid y)/p(H_1\mid y)=\frac{p(H_2)}{p(H_1)}\cdot\frac1{B(y)}$; solve for $p(H_1\mid y)$. $\square$

Three remarks delimit the use of Bayes factors.

- A Bayes factor is defined only when the marginal density of $y$ under each model is proper, which requires proper priors (§8.8.5).
- Bayes factors work well when the underlying model space is truly discrete, that is, when each alternative makes scientific sense and there is no obvious model in between.
- They work less well for models that are inherently continuous, where a discrete choice between nested models is artificial; there, embedding the models in a larger continuous model (such as a hierarchical model) is usually more informative.

### 8.8.2. A Discrete Example: Hemophilia

**Example 8.8.1** Hemophilia is an X-linked recessive disease: a man with the gene on his single X chromosome is affected, while a woman with one copy is an unaffected carrier. Consider a woman whose brother is affected, which implies that her mother is a carrier; her father is not affected. The woman herself therefore carries the gene with probability $\frac12$. Let $\theta=1$ if she is a carrier and $\theta=0$ if not, with prior $\mathbb{P}(\theta=1)=\mathbb{P}(\theta=0)=\frac12$. The data are the status of her two sons (not identical twins), $y_i=1$ for an affected and $y_i=0$ for an unaffected son, and neither is affected. If she is a carrier, each son is affected with probability $\frac12$ independently; if not, neither can be affected:

$$
p(y_1=0,y_2=0\mid\theta=1)=\tfrac12\cdot\tfrac12=0.25,\qquad p(y_1=0,y_2=0\mid\theta=0)=1.
$$
The posterior probability that she is a carrier is $\mathbb{P}(\theta=1\mid y)=\frac{0.25\cdot0.5}{0.25\cdot0.5+1\cdot0.5}=0.2$. In the language of model comparison, with $H_1\colon\theta=1$ and $H_2\colon\theta=0$:

| Prior odds | Bayes factor | Posterior odds |
|---|---|---|
| $\dfrac{p(H_2)}{p(H_1)}=1$ | $\dfrac{p(y\mid H_2)}{p(y\mid H_1)}=\dfrac{1.0}{0.25}=4$ | $\dfrac{p(H_2\mid y)}{p(H_1\mid y)}=4$ |

The example has the two features that make Bayes factors helpful: each discrete alternative makes scientific sense and there is no scientific model in between, and the marginal distribution of the data under each model, $p(y\mid H_i)$, is proper.

### 8.8.3. Jeffreys' Scale of Evidence

A Bayes factor much greater than $1$ supports the model in the numerator. Jeffreys proposed verbal labels for the evidence, stated for $B(y)=p(y\mid H_2)/p(y\mid H_1)$ with $H_2$ the null model.

**Definition 8.8.2 (Jeffreys' Scale of Evidence)** **Jeffreys' scale of evidence** classifies the Bayes factor $B(y)$ of a null model $H_2$ against an alternative $H_1$ as follows:

| $B(y)$ | Evidence |
|---|---|
| $B(y)\ge1$ | $H_2$ supported |
| $10^{-1/2}\approx0.316\le B(y)<1$ | against $H_2$, but barely worth mentioning |
| $10^{-1}\le B(y)<10^{-1/2}$ | substantial against $H_2$ |
| $10^{-3/2}\approx0.0316\le B(y)<10^{-1}$ | strong against $H_2$ |
| $10^{-2}\le B(y)<10^{-3/2}$ | very strong against $H_2$ |
| $B(y)<10^{-2}$ | decisive against $H_2$ |

The grades are steps of half a unit in $\log_{10}B$, and the labels are clearly somewhat arbitrary; the scale is a convention for communication, not a decision rule. Some presentations merge the strong and very strong grades into a single grade for $0.01\le B(y)<0.1$.

### 8.8.4. Continuous Models and Lindley's Paradox

**Example 8.8.2** Let $y_1,\dots,y_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,1)$ and test $H_0\colon\mu=0$ against $H_1\colon\mu\ne0$, where under $H_1$ the prior is $\mu\sim\mathcal{N}(0,1)$. The sample mean $\bar y$ is sufficient. Under $H_0$ no integration is needed, $p(\bar y\mid H_0)=\mathcal{N}(\bar y\mid0,1/n)$; under $H_1$,

$$
p(\bar y\mid H_1)=\int p(\bar y\mid\mu,H_1)\,p(\mu\mid H_1)\,\mathrm{d}\mu=\mathcal{N}\big(\bar y\mid0,1+\tfrac1n\big).
$$
Hence

$$
\mathrm{BF}(H_0;H_1)=\frac{p(\bar y\mid H_0)}{p(\bar y\mid H_1)}=\sqrt{\frac{1+1/n}{1/n}}\;\frac{\mathrm{e}^{-n\bar y^2/2}}{\mathrm{e}^{-\frac{n}{n+1}\bar y^2/2}}=\sqrt{n+1}\,\exp\Big(-\frac{n^2\bar y^2}{2(n+1)}\Big)\approx\sqrt n\,\mathrm{e}^{-n\bar y^2/2}.
$$
In terms of the classical statistic $z=\sqrt n\,\bar y$, $\mathrm{BF}(H_0;H_1)\approx\sqrt n\,\mathrm{e}^{-z^2/2}$, which equals $1$ when $n\bar y^2=\log n$, that is, $\lvert z\rvert=\sqrt{\log n}$.

For comparison, the classical two-sided test rejects $H_0$ at level $0.05$ when $\lvert z\rvert>1.96$, whatever $n$. The Bayesian threshold $\sqrt{\log n}$ grows with $n$: for fixed $z$ the Bayes factor in favor of $H_0$ grows like $\sqrt n$. Data that are just significant at $5\%$ ($z=1.96$) give $\mathrm{BF}(H_0;H_1)=0.58$ for $n=10$, $1.5$ for $n=100$ and $14.7$ for $n=10000$, so that with prior probability $\frac12$ the posterior probability of $H_0$ rises from $0.37$ to $0.60$ and $0.94$. This conflict between a significant p-value and strong Bayesian support for the null in large samples is *Lindley's paradox* (Lindley 1957; also called the Jeffreys–Lindley paradox).

![Lindley's paradox for y_i ~ N(μ, 1), H0: μ = 0 against H1: μ ~ N(0, 1). Left: Bayes factor in favor of H0 for data held at fixed z = 1.96, 2.58 and 3.29 (two-sided p = 0.05, 0.01, 0.001) as the sample size grows. Right: the posterior probability of H0 with prior probability 1/2.](./plots/lindley_paradox.py)

Both answers are correct for their questions. The p-value fixes the evidence threshold while the precision of $\bar y$ increases, so ever smaller departures from $0$ become significant. The Bayes factor compares $\mu=0$ with a specific alternative that spreads its prior over values of order $1$: for large $n$ a $z$ of $1.96$ means $\bar y\approx1.96/\sqrt n$, a value much closer to $0$ than most values the alternative considers plausible, so the data favor the point null. The answer depends on the prior variance under $H_1$, which in a continuous problem is hard to justify; this is the sense in which Bayes factors do not work so well for inherently continuous models.

*History.* The Bayes factor was introduced by Harold Jeffreys (1935) and developed in his *Theory of Probability* (1939). Jeffreys was convinced that induction is an extended form of logic; that this "logic of partial beliefs" must treat degrees of belief as probabilities; that simple laws or hypotheses should be viewed as separate models with nonzero prior probabilities; and that a useful, logically consistent method of hypothesis testing must be comparative and based on the data at hand rather than on data that were never observed. The Bayes factor was his attempt at a consistent method of model selection and hypothesis testing that remedies the weaknesses of p-value testing.

### 8.8.5. Improper Priors: Eight Schools Again

**Example 8.8.3** In the eight schools example, compare the two extreme models of §8.6 by a Bayes factor:

$$
H_1\colon p(y\mid\theta_1,\dots,\theta_J)=\prod_{j=1}^J\mathcal{N}(y_j\mid\theta_j,\sigma_j^2),\quad p(\theta_1,\dots,\theta_J)\propto1;\qquad H_2\colon p(y\mid\theta)=\prod_{j=1}^J\mathcal{N}(y_j\mid\theta,\sigma_j^2),\quad p(\theta)\propto1.
$$
The Bayes factor $p(y\mid H_2)/p(y\mid H_1)$ is not defined, because both priors, and hence both marginal densities, are improper: an improper prior $c\cdot p(\theta)$ is as valid as $p(\theta)$ for every $c>0$, and it multiplies $p(y\mid H)$ by $c$. The ratio is therefore arbitrary. Bayes factors cannot be applied to the original models with non-informative prior densities.

Replace the flat priors by proper ones, $\theta_j\overset{\text{iid}}{\sim}\mathcal{N}(0,A^2)$ under $H_1$ and $\theta\sim\mathcal{N}(0,A^2)$ under $H_2$. Now the Bayes factor is defined, but it is highly sensitive to $A$. For large $A$, $p(y\mid H_1)\approx\prod_j(2\pi A^2)^{-1/2}\int\mathcal{N}(y_j\mid\theta_j,\sigma_j^2)\,\mathrm{d}\theta_j\propto A^{-J}$, while $p(y\mid H_2)\propto A^{-1}$, so $p(y\mid H_2)/p(y\mid H_1)$ grows like $A^{J-1}=A^7$ (Question 5): as $A$ increases, the posterior concentrates more and more on complete pooling, whatever the data. In the figure of §8.6 the Bayes factor is $3$ at $A=10$, about $10^3$ at $A=50$ and about $10^{12}$ at $A=1000$. A prior meant to be vague is not innocuous in a Bayes factor: it penalizes the model with more parameters by spreading their prior mass over implausible values.

The posterior inference within each model hardly changes when $A$ grows, but the Bayes factor does. Rather than choosing between two extreme models, we prefer the hierarchical model, which contains both as limiting cases ($\tau=\infty$ and $\tau=0$) and estimates the amount of pooling from the data.

### 8.8.6. The Laplace Approximation and BIC

For large $n$ the marginal likelihood $p(y\mid M)=\int p(y\mid\theta,M)\,p(\theta\mid M)\,\mathrm{d}\theta$ can be approximated by making the integral look like a normal integral. Write $p(y\mid M)=\int\mathrm{e}^{g(\theta)}\,\mathrm{d}\theta$ with

$$
g(\theta)=\log\big(p(y\mid\theta,M)\,p(\theta\mid M)\big),
$$
the log of the unnormalized posterior, and expand it to second order around the posterior mode $\tilde\theta$, where the gradient vanishes:

$$
g(\theta)\approx g(\tilde\theta)+\frac12(\theta-\tilde\theta)^{\mathsf T}H(\tilde\theta)(\theta-\tilde\theta)=g(\tilde\theta)-\frac12(\theta-\tilde\theta)^{\mathsf T}I_{\tilde\theta}(\theta-\tilde\theta),
$$
with $H=\big(\partial^2g/\partial\theta_i\partial\theta_j\big)$ the **Hessian matrix** and $I_{\tilde\theta}=-H(\tilde\theta)$ the **observed information** (including the small contribution of the prior). The *Laplace approximation* of the integral, for $\theta\in\mathbb{R}^k$, is

$$
p(y\mid M)\approx\mathrm{e}^{g(\tilde\theta)}\int\exp\Big(-\frac12(\theta-\tilde\theta)^{\mathsf T}I_{\tilde\theta}(\theta-\tilde\theta)\Big)\,\mathrm{d}\theta=\mathrm{e}^{g(\tilde\theta)}\,(2\pi)^{k/2}\lvert I_{\tilde\theta}\rvert^{-1/2},
$$
the normal approximation of [3.7.5](/3.7.5) applied to the normalizing constant. Taking logarithms,

$$
\log p(y\mid M)=\log p(y\mid\tilde\theta,M)+\log p(\tilde\theta\mid M)+\frac k2\log(2\pi)-\frac12\log\lvert I_{\tilde\theta}\rvert+o(1),
$$
an approximately penalized log-likelihood. For $n$ independent observations the information grows linearly, $I_{\tilde\theta}\approx nI_1$ with $I_1$ the information of one observation, so $\log\lvert I_{\tilde\theta}\rvert=k\log n+\log\lvert I_1\rvert$. All terms other than the log-likelihood and $-\frac k2\log n$ stay bounded as $n\to\infty$:

$$
\log p(y\mid M)=\log p(y\mid\tilde\theta,M)-\frac k2\log n+O(1).
$$
For two models $H_1$ and $H_2$ with $k_1$ and $k_2$ parameters and posterior modes $\hat\theta_1$, $\hat\theta_2$ (asymptotically equal to the MLEs), it follows that for large $n$

$$
\log\mathrm{BF}(H_2;H_1)\approx\log p(y\mid\hat\theta_2,H_2)-\log p(y\mid\hat\theta_1,H_1)-\frac12(k_2-k_1)\log n=-\frac12\big(\mathrm{BIC}_2-\mathrm{BIC}_1\big).
$$
Ranking models by the Bayes factor is thus asymptotically equivalent to ranking them by BIC. The error of the approximation is $O(1)$ and depends on the priors, so $\mathrm{e}^{-\Delta\mathrm{BIC}/2}$ approximates the Bayes factor only up to a bounded factor; BIC captures the dominant $\log n$ behavior, which is enough for consistent model selection but not for an accurate value of the Bayes factor.

## Summary

| Measure | Estimates | Fit term | Penalty (effective number of parameters) | Notes |
|---|---|---|---|---|
| AIC (Definition 8.2.1) | elpd of the plug-in MLE | $-2\log p(y\mid\hat\theta_{\mathrm{MLE}})$ | $2k$ | asymptotic, frequentist; no prior, no hierarchical models |
| DIC (Definition 8.3.1) | elpd of the plug-in posterior mean | $-2\log p(y\mid\hat\theta_{\mathrm{Bayes}})$ | $2p_{\mathrm{DIC}}$, posterior mean deviance minus deviance at the mean | depends on parametrization |
| WAIC (Definition 8.4.1) | elppd of the posterior predictive | $-2\,\mathrm{lppd}$ | $2p_{\mathrm{WAIC}}$, pointwise posterior variance of $\log p(y_i\mid\theta)$ | fully Bayesian; asymptotically equal to LOO-CV |
| LOO-CV (Definition 8.5.1) | elppd | $-2\,\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$ | implicit, $p_{\mathrm{loo\text{-}cv}}=\mathrm{lppd}-\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$ | $n$ fits, or importance sampling |
| BIC (Definition 8.7.1) | $-2\log p(y)$, marginal likelihood | $-2\log p(y\mid\hat\theta)$ | $k\log n$ | selects the true model; $\log\mathrm{BF}\approx-\frac12\Delta\mathrm{BIC}$ |
| Bayes factor (Definition 8.8.1) | ratio of marginal likelihoods | | automatic, through the prior | needs proper priors; sensitive to them |

- Predictive accuracy is defined with new data (elpd, elppd, Definition 8.1.2) and estimated without new data, from the within-sample lppd (Definition 8.1.3) corrected for optimism (Proposition 8.2.1), or by cross-validation. All are compared on the deviance scale; lower is better, and differences below about $2$ are not substantial.
- Information criteria serve prediction; Bayes factors and BIC serve the choice of a true model. Bayes factors are sensible for truly discrete alternatives with proper priors (Example 8.8.1, Jeffreys' scale in Definition 8.8.2), but for continuous model families they depend strongly on vague priors (Lindley's paradox, Example 8.8.2; eight schools, Example 8.8.3), and a hierarchical model that contains the alternatives is usually preferable.
- In the eight schools example, no pooling is clearly worst, and complete pooling and the hierarchical model are indistinguishable by predictive accuracy; the effective number of parameters of the hierarchical model is $1$–$3$, far below its ten parameters.

## Questions

1. A model is fitted to two observations and three posterior draws are kept. The likelihood values $p(y_i\mid\theta^s)$ are

   | $s$ | $p(y_1\mid\theta^s)$ | $p(y_2\mid\theta^s)$ |
   |---|---|---|
   | 1 | $0.20$ | $0.10$ |
   | 2 | $0.30$ | $0.05$ |
   | 3 | $0.10$ | $0.15$ |

   and at the posterior mean $p(y_1\mid\hat\theta_{\mathrm{Bayes}})=0.22$, $p(y_2\mid\hat\theta_{\mathrm{Bayes}})=0.11$. Compute the lppd, $p_{\mathrm{WAIC}1}$, $p_{\mathrm{WAIC}2}$ (sample variance with divisor $S-1$), WAIC, $p_{\mathrm{DIC}}$ and DIC.

   **Answer** The posterior means of the likelihoods are $0.2$ and $0.1$, so $\mathrm{lppd}=\log0.2+\log0.1=\log0.02=-3.912$. The means of the log-likelihoods over the draws are $\frac13(\log0.2+\log0.3+\log0.1)=-1.705$ and $\frac13(\log0.1+\log0.05+\log0.15)=-2.399$, so $p_{\mathrm{WAIC}1}=2\big[(-1.609+1.705)+(-2.303+2.399)\big]=0.384$. The sample variances of $\log p(y_1\mid\theta^s)$ and $\log p(y_2\mid\theta^s)$ are both $0.309$, so $p_{\mathrm{WAIC}2}=0.617$. Then $\mathrm{WAIC}=-2(-3.912-0.384)=8.59$ with $p_{\mathrm{WAIC}1}$, or $-2(-3.912-0.617)=9.06$ with $p_{\mathrm{WAIC}2}$. For DIC, $\log p(y\mid\hat\theta_{\mathrm{Bayes}})=\log(0.22\cdot0.11)=-3.722$ and the posterior mean of $\log p(y\mid\theta^s)=\log p(y_1\mid\theta^s)+\log p(y_2\mid\theta^s)$ is $-1.705-2.399=-4.104$, so $p_{\mathrm{DIC}}=2(-3.722+4.104)=0.765$ and $\mathrm{DIC}=-2(-3.722)+2(0.765)=8.97$.
2. In Example 8.8.1, suppose the woman has three unaffected sons. Find the Bayes factor of $H_2$ (not a carrier) against $H_1$ (carrier), the posterior probability that she is a carrier, and the grade on Jeffreys' scale with $H_2$ as the null. What happens if one son is affected?

   **Answer** $p(y\mid H_1)=(\frac12)^3=0.125$ and $p(y\mid H_2)=1$, so $\mathrm{BF}(H_2;H_1)=8$, and with prior odds $1$, $\mathbb{P}(\theta=1\mid y)=1/(1+8)=0.111$. Since $B(y)=8\ge1$, the data support the null $H_2$. If one son is affected, $p(y\mid H_2)=0$ (a non-carrier cannot have an affected son, ignoring new mutations), the Bayes factor is $0$, and the posterior probability that she is a carrier is $1$: decisive evidence against $H_2$.
3. Two nested regression models are fitted to $n=50$ observations: model 1 with $k_1=2$ parameters has maximized log-likelihood $-120.3$, model 2 with $k_2=4$ has $-117.9$. Compare them by AIC and BIC, and approximate the Bayes factor of model 2 against model 1. Explain why the two criteria disagree.

   **Answer** $\mathrm{AIC}_1=240.6+4=244.6$ and $\mathrm{AIC}_2=235.8+8=243.8$: AIC slightly prefers model 2, but the difference $0.8<2$ is not substantial. With $\log50=3.912$, $\mathrm{BIC}_1=240.6+2(3.912)=248.4$ and $\mathrm{BIC}_2=235.8+4(3.912)=251.4$: BIC prefers model 1 by $3.0$. By §8.8.6, $\mathrm{BF}(2;1)\approx\mathrm{e}^{-3.02/2}=0.22$: the data favor the simpler model 1 by a factor of about $4.5$. The penalty per parameter is $2$ for AIC and $\log n=3.9$ for BIC: the improvement of $2.4$ in log-likelihood buys the two extra parameters under AIC's predictive criterion but not under BIC's criterion of identifying the true model.
4. For the no pooling model of the eight schools, $y_j\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2)$ with $p(\theta)\propto1$ and $J=8$, compute $p_{\mathrm{DIC}}$, $p_{\mathrm{WAIC}1}$ and $p_{\mathrm{WAIC}2}$ exactly.

   **Answer** The posterior is $\theta_j\mid y\sim\mathcal{N}(y_j,\sigma_j^2)$, so $Z_j=(y_j-\theta_j)/\sigma_j\sim\mathcal{N}(0,1)$ independently and $\log p(y_j\mid\theta_j)=-\frac12\log(2\pi\sigma_j^2)-\frac12Z_j^2$. *DIC*: $\hat\theta_{\mathrm{Bayes}}=y$, so $p_{\mathrm{DIC}}=2\sum_j\mathbb{E}(\frac12Z_j^2)=J=8$. *WAIC1*: $\mathbb{E}_{\mathrm{post}}p(y_j\mid\theta_j)=\mathcal{N}(y_j\mid y_j,2\sigma_j^2)=(4\pi\sigma_j^2)^{-1/2}$, so each term is $2\big[-\frac12\log(4\pi\sigma_j^2)+\frac12\log(2\pi\sigma_j^2)+\frac12\big]=1-\log2$, and $p_{\mathrm{WAIC}1}=8(1-\log2)=2.45$. *WAIC2*: $\operatorname{Var}(\frac12Z_j^2)=\frac14\cdot2=\frac12$, so $p_{\mathrm{WAIC}2}=4$. Only DIC counts all eight parameters; the pointwise corrections of WAIC underestimate the optimism when every observation has its own parameter.
5. Show that in Example 8.8.3 with the priors $\mathcal{N}(0,A^2)$ the Bayes factor $p(y\mid H_2)/p(y\mid H_1)$ grows like $A^{J-1}$ as $A\to\infty$. Why is the Bayes factor undefined with the flat priors?

   **Answer** Under $H_1$, $y_j\sim\mathcal{N}(0,\sigma_j^2+A^2)$ independently, so $p(y\mid H_1)=\prod_j\big(2\pi(\sigma_j^2+A^2)\big)^{-1/2}\exp\big(-\frac{y_j^2}{2(\sigma_j^2+A^2)}\big)\sim(2\pi A^2)^{-J/2}$. Under $H_2$, $p(y\mid H_2)=\int\prod_j\mathcal{N}(y_j\mid\theta,\sigma_j^2)\,\mathcal{N}(\theta\mid0,A^2)\,\mathrm{d}\theta$; for large $A$ the prior density is nearly constant, $(2\pi A^2)^{-1/2}$, over the region where the likelihood is non-negligible, so $p(y\mid H_2)\sim(2\pi A^2)^{-1/2}\int\prod_j\mathcal{N}(y_j\mid\theta,\sigma_j^2)\,\mathrm{d}\theta$, a constant times $A^{-1}$. The ratio grows like $(2\pi A^2)^{(J-1)/2}\propto A^{J-1}$. With flat priors, $p(\theta)\propto1$ means $p(\theta)=c$ for an arbitrary $c>0$, which multiplies $p(y\mid H)$ by $c$ (or by $c^J$ for $J$ parameters); the two marginal densities carry unrelated arbitrary factors, so their ratio can take any value. The calculation above makes this concrete: letting the proper priors become flat sends the ratio to infinity at a rate set by the difference in dimension.
6. In Example 8.8.2, how large must $n$ be for data with $z=1.96$ to favor $H_0$, according to the approximation $\mathrm{BF}\approx\sqrt n\,\mathrm{e}^{-z^2/2}$ and to the exact formula?

   **Answer** The approximation gives $\mathrm{BF}(H_0;H_1)>1$ when $\log n>z^2=3.84$, that is, $n>\mathrm{e}^{3.84}\approx47$. The exact Bayes factor $\sqrt{n+1}\exp\big(-\frac{z^2n}{2(n+1)}\big)$ equals $1$ at $n\approx42$. Beyond about $40$ observations, a result that is just significant at the $5\%$ level is evidence in favor of the null hypothesis under this prior.
7. For a binomial observation $y$ out of $n$ with a uniform prior on $\theta$, the exact marginal likelihood is $p(y)=1/(n+1)$ ([3.7.1](/3.7.1)). Derive the Laplace approximation of $p(y)$ and evaluate both for $n=20$, $y=7$.

   **Answer** With $g(\theta)=\log\binom ny+y\log\theta+(n-y)\log(1-\theta)$, the mode is $\tilde\theta=y/n$ and $-g''(\tilde\theta)=\frac{y}{\tilde\theta^2}+\frac{n-y}{(1-\tilde\theta)^2}=\frac{n}{\tilde\theta(1-\tilde\theta)}$. Hence

   $$
   p(y)\approx\binom ny\tilde\theta^y(1-\tilde\theta)^{n-y}\sqrt{\frac{2\pi\tilde\theta(1-\tilde\theta)}{n}}.
   $$
   For $n=20$, $y=7$, $\tilde\theta=0.35$, this is $0.0493$, against the exact $1/21=0.0476$: the relative error is $3.5\%$ and decreases as $n$ grows (it is the error of Stirling's formula in the Beta function).
8. Explain why AIC is not defined for the hierarchical eight schools model and why DIC and WAIC are. Which of the computed criteria would you report, and why?

   **Answer** AIC needs the MLE and a parameter count $k$. In the hierarchical model the $\theta_j$ are constrained by their population distribution, so the number of parameters is neither $10$ ($\theta_1,\dots,\theta_8,\mu,\tau$) nor $2$, and the maximum of the likelihood over $(\mu,\tau)$ with $\theta_j$ integrated out does not account for the posterior uncertainty in $\tau$. DIC and WAIC estimate the effective number of parameters from the posterior simulations ($p_{\mathrm{DIC}}=2.8$, $p_{\mathrm{WAIC}2}=1.3$), so they adapt to the amount of pooling. I would report WAIC with $p_{\mathrm{WAIC}2}$ together with exact or importance-sampling LOO-CV, which are fully Bayesian, invariant to the parametrization, and estimate the predictive accuracy of the posterior predictive distribution actually used; for this small data set the differences of less than $2$ between complete pooling and the hierarchical model should be reported as no real difference.
