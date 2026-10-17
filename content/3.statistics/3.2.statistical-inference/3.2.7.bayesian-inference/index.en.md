---
title: Bayesian Inference
description: The Bayesian approach to inference — prior, likelihood and posterior, conjugate priors, uniform, Jeffreys, maximum entropy and hierarchical priors, Bayes estimators and the posterior mean squared error, credible and HPD intervals, Bayesian tests and Bayes factors, posterior prediction and Bayesian decisions.
---

Everything in the earlier chapters of this course belongs to classical, or frequentist, statistics: the parameter $\theta$ is a fixed unknown constant, probabilities are long-run frequencies under repeated sampling, and procedures are judged by their behavior over hypothetical repetitions of the experiment. That theory gave us the three types of inference: point estimation (bias, consistency, efficiency, maximum likelihood, moments, UMVUE; [3.2.3](/3.2.3)), interval estimation with its frequency interpretation ([3.2.4](/3.2.4)), and **hypothesis testing** (likelihood ratio tests, the Neyman–Pearson lemma, UMP tests, nonparametric tests; [3.2.5](/3.2.5), [3.2.6](/3.2.6)). Bayesian statistics treats the parameter as a random variable. Inference starts from a prior distribution expressing what is believed about $\theta$ before the data are seen, and Bayes' theorem ([3.1.2](/3.1.2)) turns it into a posterior distribution given the observed data, on which all inference is then based. This chapter compares the two viewpoints (§7.1), introduces the prior–posterior calculus and conjugate priors (§7.2–§7.3), discusses how to choose a prior (§7.4), and then redoes the three inference problems in Bayesian form: point estimation (§7.5), credible intervals (§7.6) and tests (§7.7), followed by prediction (§7.8) and decision theory (§7.9). Bayesian methods are developed in depth in [3.6](/3.6).

## 7.1. Frequentist and Bayesian Statistics

### 7.1.1. Two Ideas of Probability

In frequentist statistics the probability of an event is the limiting proportion of occurrences in infinitely many repeatable trials, and parameters are fixed quantities without distributions. In subjective Bayesian inference probability measures the strength of belief. Before any data are collected there is uncertainty about the value of a parameter; it is formalized by a probability density for the parameter. An experiment then provides data that carry information about the parameter, and Bayes' theorem combines the prior beliefs with the data into an updated description of the uncertainty.

For example, suppose we are given a coin and told that it is a bit biased. We might represent our beliefs about the probability $\theta$ of heads by a $\mathrm{Beta}(4,4)$ distribution, symmetric about $0.5$ but spread out. If we then observe $30$ heads and $10$ tails, probability theory gives the posterior distribution $\mathrm{Beta}(34,14)$ for $\theta$, concentrated around $0.7$ (Example 7.2.1).

Bayesian methods go back to Bayes and Laplace (late 18th to mid 19th century). In the 1920s Fisher put forward the opposing view that inference must rest on probabilities with a direct experimental interpretation, the repeated sampling principle. Jeffreys' *Theory of Probability* (1939) started a revival of Bayesian inference that continued through the 1950s and 1960s, as problems with the frequentist approach became apparent. Simulation-based computation has transformed Bayesian statistics in the last decades, and it now plays a prominent part in modern statistics.

### 7.1.2. Problems with Frequentist Inference

The first problem is that frequentist inference generally does not condition on the observed data. A confidence interval is a set-valued function $C(\boldsymbol{X})\subseteq\Theta$ of the data that covers the true $\theta$ for a fraction $1-\alpha$ of repeated draws of $\boldsymbol{X}$. This is not the statement that, given the data $\boldsymbol{X}=\boldsymbol{x}$, the interval $C(\boldsymbol{x})$ covers $\theta$ with probability $1-\alpha$, although this is the kind of statement we would like to make.

**Example 7.1.1** Let $X_1,X_2\overset{\text{iid}}{\sim}\mathrm{U}(\theta-0.5,\theta+0.5)$ with order statistics $X_{(1)}\le X_{(2)}$. Since $\theta$ lies between $X_1$ and $X_2$ exactly when one of them is below $\theta$ and the other above, $\mathbb{P}_\theta\big(X_{(1)}\le\theta\le X_{(2)}\big)=2\cdot\frac12\cdot\frac12=\frac12$: the interval $[X_{(1)},X_{(2)}]$ is a confidence interval with confidence level $0.5$. Suppose that in the observed data $x_{(2)}-x_{(1)}>0.5$, which happens in a quarter of all data sets (the range of two such uniforms exceeds $0.5$ with probability $(1-0.5)^2=1/4$). Then both points lie within $0.5$ of $\theta$ and more than $0.5$ apart, so it must hold that $\theta\in[x_{(1)},x_{(2)}]$. For these data we are certain that the interval covers $\theta$, yet the frequentist statement still reports confidence $0.5$.

The second problem is that frequentist inference depends on data that were never observed.

**Definition 7.1.1 (Likelihood Principle)** The **likelihood principle** states: if two experiments $E_1,E_2$ about $\theta$ give data $y_1,y_2$ whose likelihood functions are proportional, i.e. for some constant $c>0$

$$
L(\theta;y_1,E_1)=c\,L(\theta;y_2,E_2)\qquad\text{for all }\theta,
$$
then the two experiments lead to identical conclusions about $\theta$.

The method of **maximum likelihood estimation** respects the likelihood principle: the MLE is the same in both experiments. Significance tests do not. In a pure significance test we specify only $H_0$, choose a test statistic $T(\boldsymbol{X})$, and define the $p$-value of the observed $T(\boldsymbol{x})=t$ as

$$
p=\mathbb{P}\big(T(\boldsymbol{X})\ \text{at least as extreme as}\ t\mid H_0\big).
$$
The choice of $T(\boldsymbol{X})$ amounts to a statement about the direction of likely departures from the null, which already involves alternative models. Moreover, the $p$-value is a sum (or integral) over data that were not observed, so it can depend on the form of the experiment; and a $p$-value is not $\mathbb{P}\big(H_0\mid T(\boldsymbol{x})=t\big)$.

**Example 7.1.2** A Bernoulli trial succeeds with probability $p$. Experiment $E_1$ performs a fixed number $n=12$ of trials and counts the successes $Y$; experiment $E_2$ performs trials until a fixed number $y=3$ of successes is reached and counts the number of trials $N$. Suppose $3$ of $12$ trials succeed and the $12$th trial is a success, which is possible under both designs. The likelihoods

$$
L(p;y_1,E_1)=\binom{12}{3}p^3(1-p)^9\quad(\text{binomial}),\qquad L(p;y_2,E_2)=\binom{11}{2}p^3(1-p)^9\quad(\text{Pascal})
$$
are proportional, and the MLE is $\hat p=1/4$ in both cases. But test $H_0\colon p=0.5$ against $H_1\colon p<0.5$. Under $E_1$ the $p$-value is

$$
\mathbb{P}(Y\le3\mid p=0.5)=\sum_{k=0}^{3}\binom{12}{k}0.5^{12}=0.073,
$$
and under $E_2$ it is

$$
\mathbb{P}(N\ge12\mid p=0.5)=\sum_{k=12}^{\infty}\binom{k-1}{2}0.5^{k}=0.033 .
$$
At level $0.05$ the two experiments lead to different conclusions, although the data and the likelihoods are the same. The $p$-values disagree because they sum over different portions of two different sample spaces.

### 7.1.3. Overview

The Bayesian approach introduced in this chapter consists of priors (conjugate priors, improper priors, Jeffreys' prior and others), posterior inference by "posterior $\propto$ likelihood $\times$ prior", interval estimation by credible and HPD intervals, and hypothesis testing by posterior probabilities, marginal likelihoods and Bayes factors. When analytic solutions are unavailable, approximate computational techniques are used: Markov chain Monte Carlo (MCMC) methods, which simulate a Markov chain whose stationary distribution is the posterior; approximations to marginal likelihoods (variational approximations, Laplace approximations, the Bayesian information criterion BIC); and the EM algorithm, useful in both frequentist and Bayesian inference for missing-data problems. Finally, statistical decision theory (§7.9) adds a loss function to the posterior and chooses the action with the smallest expected loss.

## 7.2. Prior and Posterior Distributions

**Definition 7.2.1 (Prior and Posterior)** Let the data $\boldsymbol{x}$ have density (or probability mass function) $f(\boldsymbol{x}\mid\theta)$, $\theta\in\Theta$. A **prior distribution** is any probability distribution on the parameter space $\Theta$, with density $\pi(\theta)$; it measures the strength of belief about $\theta$ before the data are observed. The **posterior distribution** is the conditional distribution of $\theta$ given $\boldsymbol{x}$,

$$
\pi(\theta\mid\boldsymbol{x})=\frac{f(\boldsymbol{x}\mid\theta)\pi(\theta)}{m(\boldsymbol{x})},\qquad m(\boldsymbol{x})=\int_\Theta f(\boldsymbol{x}\mid\theta)\pi(\theta)\,\mathrm{d}\theta,
$$
where the normalizing constant $m(\boldsymbol{x})$, the density of $\boldsymbol{x}$ after $\theta$ is integrated out, is called the **marginal likelihood**.

Here $f(\boldsymbol{x}\mid\theta)\pi(\theta)=f_{\boldsymbol{X},\theta}(\boldsymbol{x},\theta)$ is the joint density of the data and the parameter. As a function of $\theta$ the posterior is

$$
\pi(\theta\mid\boldsymbol{x})\propto f(\boldsymbol{x}\mid\theta)\pi(\theta),\qquad\text{posterior}\propto\text{likelihood}\times\text{prior},
$$
and the same formula holds for discrete $\theta$ with sums in place of integrals. *Bayesian inference* bases all inference on the posterior distribution. It respects the likelihood principle: if two likelihood functions are proportional, the constant cancels between numerator and denominator in Bayes' formula, and the two posteriors coincide. If we know nothing about the success probability $p$ of a Bernoulli trial, one possible prior is $\mathrm{U}(0,1)$; how to determine a prior in general is the subject of §7.4.

**Example 7.2.1 (Binomial Data, Beta Prior)** Let $X\sim\mathrm{Bin}(n,\theta)$ with $n$ known, and represent the prior knowledge about $\theta$ by a Beta distribution,

$$
\pi(\theta)=\frac{\theta^{a-1}(1-\theta)^{b-1}}{\mathrm{B}(a,b)},\qquad0<\theta<1 .
$$
The parameters $a,b>0$ give a flexible family: $a=b=1$ is uniform, $a=b=20$ is concentrated near $0.5$, $a<b$ favors small $\theta$, and so on. With the likelihood $f(x\mid\theta)=\binom nx\theta^x(1-\theta)^{n-x}$, $x=0,\dots,n$,

$$
\pi(\theta\mid x)\propto\theta^{a-1}(1-\theta)^{b-1}\theta^x(1-\theta)^{n-x}=\theta^{a+x-1}(1-\theta)^{n-x+b-1},
$$
so the posterior has the same form as the prior with $a,b$ replaced by $a+x$, $b+n-x$:

$$
\theta\mid x\sim\mathrm{Beta}(a+x,\ b+n-x),\qquad \pi(\theta\mid x)=\frac{\theta^{a+x-1}(1-\theta)^{n-x+b-1}}{\mathrm{B}(a+x,b+n-x)}.
$$
The coin of §7.1.1 is the case $a=b=4$, $n=40$, $x=30$. Since $\mathrm{Beta}(a,b)$ has mean $\frac{a}{a+b}$ and variance $\frac{ab}{(a+b)^2(a+b+1)}$, the posterior mean and variance are

$$
\mathbb{E}[\theta\mid X]=\frac{a+X}{a+b+n},\qquad \operatorname{Var}(\theta\mid X)=\frac{(a+X)(b+n-X)}{(a+b+n)^2(a+b+n+1)}.
$$
If $X=n$ and $a=b=1$, the posterior mean is $\frac{n+1}{n+2}$: when we observe events of only one type, the point estimate is not $0$ or $1$, which is sensible especially for small samples. For large $n$ the posterior mean and variance are approximately $\frac Xn$ and $\frac{X(n-X)}{n^3}$, the classical estimate $\hat\theta=X/n$ and its estimated variance $\hat\theta(1-\hat\theta)/n$.

**Example 7.2.2** Suppose the true value is $\theta=0.3$, but the prior has mean $0.7$ and standard deviation $0.1$, which is $\mathrm{Beta}(14,6)$. Observing $n=10$ trials with $X=3$ gives the posterior $\mathrm{Beta}(17,13)$, still pulled toward the prior; observing $n=100$ trials with $X=30$ gives $\mathrm{Beta}(44,76)$, close to the truth. As $n$ increases, the likelihood overwhelms the information in the prior.

![Left: Beta prior densities for several parameter choices. Right: a Beta(14, 6) prior centered at 0.7 and the posteriors after observing 3 successes in 10 trials and 30 successes in 100 trials; the dashed line is the true value 0.3.](./plots/beta-prior-posterior.py)

## 7.3. Conjugate Priors

**Definition 7.3.1 (Conjugate Prior)** A family $\mathcal{P}$ of prior distributions is **conjugate** for the model $\{f(x\mid\theta)\}$ if for every prior in $\mathcal{P}$ and every data set the posterior again belongs to $\mathcal{P}$. A member of such a family is called a **conjugate prior**.

With a conjugate prior the posterior is obtained by updating finitely many parameters, so Bayesian computations can be done in closed form. The Beta family is conjugate for binomial data (Example 7.2.1). Common conjugate pairs ($X_1,\dots,X_n$ i.i.d., $x=\sum_ix_i$ where relevant):

| Model | Prior | Posterior |
|---|---|---|
| $\mathrm{Bin}(n,\theta)$, one observation $x$ | $\mathrm{Beta}(a,b)$ | $\mathrm{Beta}(a+x,\ b+n-x)$ |
| $\mathrm{Ber}(\theta)$ | $\mathrm{Beta}(a,b)$ | $\mathrm{Beta}(a+x,\ b+n-x)$ |
| $\mathrm{Poi}(\theta)$ | $\Gamma(\alpha,\lambda)$ | $\Gamma(\alpha+x,\ \lambda+n)$ |
| $\mathrm{Exp}(\theta)$ | $\Gamma(\alpha,\lambda)$ | $\Gamma(\alpha+n,\ \lambda+x)$ |
| $\mathcal{N}(\theta,\sigma^2)$, $\sigma^2$ known | $\mathcal{N}(\mu,\tau^2)$ | $\mathcal{N}\big(\mu_n(\boldsymbol{x}),\eta_n^2\big)$, Example 7.5.1 |
| $\mathcal{N}(\mu,1/\tau)$, both unknown | normal–gamma | normal–gamma, Example 7.3.1 |

(The Gamma distributions use the rate parametrization.)

**Example 7.3.1 (Normal Data, Unknown Mean and Variance)** Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ with both parameters unknown, and write $\tau=1/\sigma^2$, the *precision*, and $\theta=(\tau,\mu)$. Take the prior $\tau\sim\Gamma(\alpha,\beta)$ ($\alpha,\beta>0$) and, conditionally on $\tau$, $\mu\sim\mathcal{N}\big(\nu,\frac{1}{k\tau}\big)$ for some $k>0$, $\nu\in\mathbb{R}$:

$$
\pi(\tau,\mu)=\frac{\beta^\alpha}{\Gamma(\alpha)}\tau^{\alpha-1}\mathrm{e}^{-\beta\tau}\cdot(2\pi)^{-1/2}(k\tau)^{1/2}\exp\Big\{-\frac{k\tau}{2}(\mu-\nu)^2\Big\}\propto\tau^{\alpha-1/2}\exp\Big[-\tau\Big\{\beta+\frac k2(\mu-\nu)^2\Big\}\Big].
$$
The likelihood is $f(\boldsymbol{x}\mid\mu,\tau)=(2\pi)^{-n/2}\tau^{n/2}\exp\big\{-\frac\tau2\sum_{i=1}^n(x_i-\mu)^2\big\}$, so

$$
\pi(\tau,\mu\mid\boldsymbol{x})\propto\tau^{\alpha+n/2-1/2}\exp\Big[-\tau\Big\{\beta+\frac k2(\mu-\nu)^2+\frac12\sum_{i=1}^n(x_i-\mu)^2\Big\}\Big].
$$
Completing the square,

$$
k(\mu-\nu)^2+\sum_{i=1}^n(x_i-\mu)^2=(k+n)\Big(\mu-\frac{k\nu+n\bar x}{k+n}\Big)^2+\frac{nk}{n+k}(\bar x-\nu)^2+\sum_{i=1}^n(x_i-\bar x)^2 .
$$
Hence

$$
\pi(\tau,\mu\mid\boldsymbol{x})\propto\tau^{\alpha'-1/2}\exp\Big[-\tau\Big\{\beta'+\frac{k'}{2}(\mu-\nu')^2\Big\}\Big]
$$
with

$$
\alpha'=\alpha+\frac n2,\quad \beta'=\beta+\frac12\cdot\frac{nk}{n+k}(\bar x-\nu)^2+\frac12\sum_{i=1}^n(x_i-\bar x)^2,\quad k'=k+n,\quad \nu'=\frac{k\nu+n\bar x}{k+n}.
$$
This has the same form as the prior, so the normal–gamma family is conjugate. The posterior mean of $\mu$, $\nu'$, is a weighted average of the prior mean $\nu$ and $\bar x$, with weights $k$ and $n$: the prior acts like $k$ additional observations.

The examples are instances of a general fact for exponential families (Definition 2.2.1).

**Theorem 7.3.1 (Conjugate Priors for Exponential Families)** Let the sample have the exponential-family density

$$
f(\boldsymbol{x}\mid\theta)=C(\theta)^n\exp\Big\{\sum_{j=1}^kQ_j(\theta)\sum_{i=1}^nT_j(x_i)\Big\}\prod_{i=1}^nh(x_i).
$$
Then the family of priors

$$
\pi(\theta\mid\tau_0,\dots,\tau_k)\propto C(\theta)^{\tau_0}\exp\Big\{\sum_{j=1}^kQ_j(\theta)\tau_j\Big\},
$$
indexed by constants $\tau_0,\dots,\tau_k$ (for which the right side is integrable), is conjugate: the posterior is

$$
f(\boldsymbol{x}\mid\theta)\pi(\theta\mid\tau_0,\dots,\tau_k)\propto C(\theta)^{n+\tau_0}\exp\Big\{\sum_{j=1}^kQ_j(\theta)\Big[\sum_{i=1}^nT_j(x_i)+\tau_j\Big]\Big\},
$$
the prior with updated parameters $\tau_0'=n+\tau_0$ and $\tau_j'=\sum_{i=1}^nT_j(x_i)+\tau_j$.

The prior parameters enter exactly as the sufficient statistics do: $\tau_0$ plays the role of a prior sample size and $\tau_j$ of prior totals of $T_j$.

## 7.4. Constructing Priors

### 7.4.1. Subjective and Non-subjective Priors

A *subjective prior* is a distribution representing knowledge about the parameter before the data are available; if possible, it is built from a model for the parameter. If different scientists have different priors, or it is unclear how to express prior knowledge as a distribution, we should consider several priors, repeat the analysis, and check that the conclusions are insensitive to priors representing different points of view (sensitivity analysis).

Several approaches promise an "automatic", even "objective" prior, a *non-informative prior*: the uniform prior, Jeffreys' prior and maximum entropy priors. In practice, if such a prior conflicted with real prior knowledge, we would not use it. These approaches are useful to complete the specification of a prior once the subjective considerations have been taken into account.

### 7.4.2. Uniform and Improper Priors

The uniform prior is $\pi(\theta)\propto\text{constant}$. If $\Theta$ is unbounded, this is not a probability density.

**Definition 7.4.1 (Improper Prior)** A prior "density" $\pi(\theta)\ge0$ with $\int_\Theta\pi(\theta)\,\mathrm{d}\theta=\infty$ is called an **improper prior** (generalized prior density).

An improper prior can still be used if the posterior is proper. With a uniform prior the posterior is

$$
\pi(\theta\mid x)=\frac{L(\theta;x)}{\int_\Theta L(\theta;x)\,\mathrm{d}\theta},
$$
which is a probability density if and only if $\int_\Theta L(\theta;x)\,\mathrm{d}\theta<\infty$. If this integral is infinite, the posterior is improper too and all inference based on it is meaningless.

**Example 7.4.1** Let $X\sim\mathrm{Exp}(1/\mu)$ (mean $\mu$) and observe only $N=\boldsymbol{1}_{\{X<1\}}\in\{0,1\}$. Suppose we observe $N=0$. Then $L(\mu;0)=\mathbb{P}(X\ge1)=\exp(-1/\mu)$, and with $\pi(\mu)\propto1$ on $\mu>0$ we get $\pi(\mu\mid N=0)\propto\exp(-1/\mu)$. This is improper: $\exp(-1/\mu)\to1$ as $\mu\to\infty$, so $\int_0^\infty\exp(-1/\mu)\,\mathrm{d}\mu$ diverges.

If the prior is uniform (perhaps improper) but the posterior is proper, and treating all parameter values as equally probable a priori is a fair representation of prior knowledge, the uniform prior may be useful (see also Example 7.4.4).

### 7.4.3. Jeffreys' Prior

A drawback of the uniform prior is that it is not invariant: uniform on $\theta$ is not uniform on $\theta^2$ or $\log\theta$. Jeffreys reasoned that a rule for constructing priors should lead to the same distribution whether it is applied to $\theta$ or to another parametrization $\psi$ with $\theta=g(\psi)$.

**Definition 7.4.2 (Jeffreys' Prior)** **Jeffreys' prior** is

$$
\pi(\theta)\propto\sqrt{I(\theta)},\qquad I(\theta)=\mathbb{E}_\theta\Big[\Big(\frac{\partial l}{\partial\theta}\Big)^2\Big],
$$
where $l=\log f(X\mid\theta)$ and $I(\theta)$ is the Fisher information ([3.2.3](/3.2.3)). For a vector parameter $\boldsymbol{\theta}$, $\pi(\boldsymbol{\theta})\propto\sqrt{\det I(\boldsymbol{\theta})}$ with the Fisher information matrix $I(\boldsymbol{\theta})$.

**Proposition 7.4.1** Jeffreys' rule is invariant under reparametrization: if $\theta=g(\psi)$ with $g$ smooth and one-to-one, the prior induced on $\psi$ by $\pi(\theta)\propto\sqrt{I_\theta}$ is $\pi_\Psi(\psi)\propto\sqrt{I_\psi}$.

**Proof** By the change-of-variables formula, $\pi_\Psi(\psi)\propto\pi(g(\psi))\lvert g'(\psi)\rvert=\sqrt{I_{g(\psi)}}\,\lvert g'(\psi)\rvert$. By the chain rule $\frac{\partial l}{\partial\psi}=\frac{\partial l}{\partial\theta}g'(\psi)$, so $I_\psi=g'(\psi)^2I_{g(\psi)}$. Hence $\pi_\Psi(\psi)\propto\sqrt{I_\psi}$. $\square$

**Example 7.4.2** For $X\sim\mathrm{Ber}(\theta)$, $I(\theta)=\frac{1}{\theta(1-\theta)}$, so Jeffreys' prior is $\pi(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2}$, the $\mathrm{Beta}(\frac12,\frac12)$ distribution. For $X\sim\mathcal{N}(\mu,\sigma^2)$ with $\sigma^2$ known, $I(\mu)=1/\sigma^2$ is constant and Jeffreys' prior on $\mu$ is the (improper) uniform prior.

It is sometimes desirable, on subjective grounds, to have a prior that is invariant under reparametrization; Jeffreys' prior provides one.

### 7.4.4. Maximum Entropy Priors

**Definition 7.4.3 (Maximum Entropy Prior)** A **maximum entropy prior** is a density $\pi(\theta)$ that maximizes the entropy

$$
\phi[\pi]=-\int_\Theta\pi(\theta)\log\pi(\theta)\,\mathrm{d}\theta
$$
over all densities $\pi$ satisfying given constraints. Finding it is a problem in the calculus of variations.

**Theorem 7.4.1** The density $\pi$ maximizing $\phi[\pi]$ subject to $\mathbb{E}[t_j(\theta)]=t_j$, $j=1,\dots,p$, has the $p$-parameter exponential-family form

$$
\pi(\theta)\propto\exp\Big\{\sum_{j=1}^p\lambda_jt_j(\theta)\Big\},\qquad\theta\in\Theta,
$$
where $\lambda_1,\dots,\lambda_p$ are determined by the constraints.

**Example 7.4.3** (1) Over all densities on $\Theta=\mathbb{R}$ with

$$
\int_{-\infty}^\infty\pi(\theta)\,\mathrm{d}\theta=1,\qquad\int_{-\infty}^\infty\theta\,\pi(\theta)\,\mathrm{d}\theta=\mu,\qquad\int_{-\infty}^\infty(\theta-\mu)^2\pi(\theta)\,\mathrm{d}\theta=\sigma^2,
$$
the entropy is maximized by the normal density $\pi(\theta)=\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(\theta-\mu)^2/(2\sigma^2)}$: by Theorem 7.4.1, $\pi(\theta)\propto\exp\{\lambda_1\theta+\lambda_2\theta^2\}$, and the constraints force this to be $\mathcal{N}(\mu,\sigma^2)$.

(2) Suppose the prior probabilities of intervals are specified, $\mathbb{P}(a_{j-1}<\theta\le a_j)=\phi_j$, $j=1,\dots,p$, with $\sum_j\phi_j=1$ and $\theta\in(a_0,a_p]$, $a_0<a_1<\cdots<a_p$. The conditions are $\mathbb{E}[t_j(\theta)]=\phi_j$ with $t_j(\theta)=\boldsymbol{1}_{(a_{j-1},a_j]}(\theta)$, so the maximum entropy prior density is

$$
\pi(\theta)\propto\exp\Big\{\sum_{j=1}^p\lambda_j\boldsymbol{1}_{(a_{j-1},a_j]}(\theta)\Big\},\qquad a_0<\theta\le a_p,
$$
which is constant on each interval: a histogram with bars on $(a_0,a_1],\dots,(a_{p-1},a_p]$ and heights $\phi_j/(a_j-a_{j-1})$.

### 7.4.5. Hierarchical Models

**Definition 7.4.4 (Hierarchical Model)** In a **hierarchical model** the prior itself has parameters that are given a probability distribution: the data $x$ have density $f(x\mid\theta)$, the prior of $\theta$ is $\pi(\theta\mid\psi)$, and the hyperparameter $\psi\in\Psi$ has a prior $g(\psi)$.

The hierarchical model simply specifies the prior of $\theta$ indirectly,

$$
\pi(\theta)=\int_\Psi\pi(\theta\mid\psi)g(\psi)\,\mathrm{d}\psi .
$$
We can work with the joint posterior $\pi(\theta,\psi\mid x)\propto f(x\mid\theta)\pi(\theta\mid\psi)g(\psi)$, or with $\pi(\theta\mid x)\propto f(x\mid\theta)\pi(\theta)$. Hierarchical models suit parameters with a group structure.

**Example 7.4.4** For $i=1,\dots,k$ we make $n_i$ observations $X_{i1},\dots,X_{in_i}$ on population $i$, with $X_{ij}\sim\mathcal{N}(\theta_i,\sigma^2)$; the means $\theta_i$ are unknown and $\sigma^2$ is known. Suppose the prior model for the means is $\theta_1,\dots,\theta_k\overset{\text{iid}}{\sim}\mathcal{N}(\phi,\tau^2)$: the populations are different but similar. With $\psi=(\phi,\tau)$,

$$
\pi(\theta_1,\dots,\theta_k\mid\psi)=\prod_{i=1}^k(2\pi\tau^2)^{-1/2}\exp\Big\{-\frac{1}{2\tau^2}(\theta_i-\phi)^2\Big\}.
$$
We still need a prior for $\phi$ and $\tau$; suppose we take $g(\phi,\tau)=\text{constant}$, all values equally likely a priori (an improper prior, to be used with care). The joint posterior is

$$
\pi(\boldsymbol{\theta},\psi\mid x)\propto\Big[\prod_{i=1}^k\exp\Big\{-\frac{1}{2\sigma^2}\sum_{j=1}^{n_i}(x_{ij}-\theta_i)^2\Big\}\Big]\Big[\prod_{i=1}^k\tau^{-1}\exp\Big\{-\frac{1}{2\tau^2}(\theta_i-\phi)^2\Big\}\Big].
$$
Integrating out $\phi$ and then $\tau$ (an exercise with a normal and a Gamma-type integral) gives the marginal posterior of $\boldsymbol{\theta}$,

$$
\pi(\boldsymbol{\theta}\mid x)\propto\Big[\prod_{i=1}^k\exp\Big\{-\frac{n_i}{2\sigma^2}(\theta_i-\bar x_i)^2\Big\}\Big]\Big[\sum_{i=1}^k(\theta_i-\bar\theta)^2\Big]^{1-k/2},
$$
where $\bar x_i$ is the mean of sample $i$ and $\bar\theta=\frac1k\sum_i\theta_i$ (we used $\sum_j(x_{ij}-\theta_i)^2=n_i(\theta_i-\bar x_i)^2+\text{const}$). The first factor pulls each $\theta_i$ toward its own sample mean; the second, which increases when the $\theta_i$ are close together, shrinks them toward their common mean. The prior on $(\phi,\tau)$ was improper, but this posterior is proper (for $k\ge3$).

## 7.5. Bayesian Point Estimation

### 7.5.1. Bayes Estimators

Bayesian analysis can be based on the posterior distribution alone, or it can take a loss function into account (statistical decision theory, §7.9). Without a loss function, the natural point estimates are summaries of the posterior.

**Definition 7.5.1 (Bayes Estimators)** Let $\pi(\theta\mid x)$ be the posterior distribution.

1. The **maximum a posteriori estimate** (MAP, posterior mode, also called the generalized maximum likelihood estimate) is $\hat\theta_{\mathrm{MAP}}=\arg\max_{\theta\in\Theta}\pi(\theta\mid x)$.
2. The **posterior median** estimate $\hat\theta_{\mathrm{median}}$ is the median of $\pi(\theta\mid x)$.
3. The **posterior mean** estimate (expected a posteriori) is $\hat\theta_{\mathrm{mean}}=\mathbb{E}[\theta\mid x]=\int_\Theta\theta\,\pi(\theta\mid x)\,\mathrm{d}\theta$.

When the posterior is symmetric and unimodal, the three estimates coincide.

**Example 7.5.1 (Normal Mean, Conjugate Prior)** Let $X_1,\dots,X_n$ be a sample from $\mathcal{N}(\theta,\sigma^2)$ with $\sigma^2$ known, and take the conjugate prior $\theta\sim\mathcal{N}(\mu,\tau^2)$ with $\mu,\tau^2$ known. Then

$$
\begin{aligned}
\pi(\theta\mid\boldsymbol{x})&\propto f(\boldsymbol{x}\mid\theta)\pi(\theta)\propto\exp\Big\{-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\theta)^2-\frac{1}{2\tau^2}(\theta-\mu)^2\Big\}\\
&\propto\exp\Big\{-\frac{1}{2\sigma^2\tau^2/(n\tau^2+\sigma^2)}\Big(\theta-\frac{\sigma^2\mu+n\tau^2\bar x}{n\tau^2+\sigma^2}\Big)^2\Big\},
\end{aligned}
$$
so the posterior is $\mathcal{N}\big(\mu_n(\boldsymbol{x}),\eta_n^2\big)$ with

$$
\mu_n(\boldsymbol{x})=\frac{\sigma^2/n}{\sigma^2/n+\tau^2}\mu+\frac{\tau^2}{\sigma^2/n+\tau^2}\bar x,\qquad \eta_n^2=\frac{\sigma^2\tau^2}{n\tau^2+\sigma^2}. \tag{7.1}
$$
All three Bayes estimates equal $\mu_n(\boldsymbol{x})$, a weighted average of the prior mean $\mu$ and the sample mean $\bar x$ with weights proportional to the precisions $1/\tau^2$ and $n/\sigma^2$. Equivalently, the posterior precision is the sum of the prior and data precisions, $1/\eta_n^2=1/\tau^2+n/\sigma^2$.

**Example 7.5.2 (Bernoulli Data, Beta Prior)** Let $X_1,\dots,X_n$ be a sample from $\mathrm{Ber}(\theta)$ and take the prior $\mathrm{Beta}(a,b)$ with $a,b$ known. With $x=\sum_ix_i$ the posterior is $\mathrm{Beta}(a+x,b+n-x)$ (Example 7.2.1), so

$$
\hat\theta_{\mathrm{MAP}}=\frac{x+a-1}{n+a+b-2},\qquad \hat\theta_{\mathrm{mean}}=\frac{x+a}{n+a+b}
$$
(the mode formula requires $a+x>1$ and $b+n-x>1$). For $a=b=1$, the uniform prior $\mathrm{U}(0,1)$,

$$
\hat\theta_{\mathrm{MAP}}=\frac xn,\qquad\hat\theta_{\mathrm{mean}}=\frac{x+1}{n+2}.
$$
Thus the MLE is the MAP estimate under the uniform prior; more generally, many classical estimators are MAP estimates under suitable priors. The posterior mean is often more appropriate than the MAP. For the scrap rate $\theta$ of a product, estimated from $n$ inspected items of which $x$ are scrap:

| $n$ | $x$ | $\hat\theta_{\mathrm{MAP}}=x/n$ | $\hat\theta_{\mathrm{mean}}=(x+1)/(n+2)$ |
|---|---|---|---|
| 3 | 0 | 0 | 0.200 |
| 10 | 0 | 0 | 0.083 |
| 3 | 3 | 1 | 0.800 |
| 10 | 10 | 1 | 0.917 |

The MAP (here the MLE) cannot distinguish $0$ scraps in $3$ items from $0$ in $10$, and claims a scrap rate of exactly $0$ or $1$; the posterior mean reflects the amount of evidence.

**Example 7.5.3** Let $X\sim f(x\mid\theta)=\mathrm{e}^{-(x-\theta)}\boldsymbol{1}_{[\theta,\infty)}(x)$, $-\infty<\theta<\infty$, with the Cauchy prior $\pi(\theta)=\frac{1}{\pi(1+\theta^2)}$. The posterior is

$$
\pi(\theta\mid x)=\frac{f(x\mid\theta)\pi(\theta)}{m(x)}=\frac{\mathrm{e}^{-(x-\theta)}}{m(x)\,\pi(1+\theta^2)}\boldsymbol{1}_{(-\infty,x]}(\theta),
$$
and for $\theta<x$

$$
\frac{\mathrm{d}\pi(\theta\mid x)}{\mathrm{d}\theta}=\frac{\mathrm{e}^{-x}}{\pi m(x)}\Big[\frac{\mathrm{e}^\theta}{1+\theta^2}-\frac{2\theta\mathrm{e}^\theta}{(1+\theta^2)^2}\Big]=\frac{\mathrm{e}^{-x}}{\pi m(x)}\cdot\frac{\mathrm{e}^\theta(\theta-1)^2}{(1+\theta^2)^2}\ge0 .
$$
So $\pi(\theta\mid x)$ increases on $(-\infty,x]$ and $\hat\theta_{\mathrm{MAP}}=x$. The posterior median and mean have no closed form and are computed numerically.

### 7.5.2. Precision of Bayes Estimators

**Definition 7.5.2 (Posterior Mean Squared Error)** The accuracy of an estimator $\delta(x)$ is measured by the **posterior mean squared error**

$$
\operatorname{PMSE}(\delta(x))=\mathbb{E}^{\theta\mid x}\big[(\theta-\delta(x))^2\big],
$$
the expectation being taken over $\theta$ with respect to the posterior distribution, for the observed $x$.

**Theorem 7.5.1** Let $\mu^\pi(x)=\mathbb{E}[\theta\mid x]$ and $V^\pi(x)=\operatorname{Var}(\theta\mid x)$ be the posterior mean and variance. For every estimator $\delta$,

$$
\operatorname{PMSE}(\delta(x))=V^\pi(x)+\big(\mu^\pi(x)-\delta(x)\big)^2\ge V^\pi(x),
$$
with equality if and only if $\delta(x)=\mu^\pi(x)$. Hence the posterior mean is optimal in the sense of minimizing the PMSE, and its PMSE is the posterior variance.

**Proof** Write $\theta-\delta(x)=\big(\theta-\mu^\pi(x)\big)+\big(\mu^\pi(x)-\delta(x)\big)$, square, and take the posterior expectation. The second term is a constant given $x$, and the cross term vanishes because $\mathbb{E}^{\theta\mid x}[\theta-\mu^\pi(x)]=0$. $\square$

The posterior variance is thus the natural measure of the uncertainty of a Bayesian point estimate, playing the role of the variance of an estimator in frequentist theory; but it is computed conditionally on the observed data, not over repeated samples.

**Example 7.5.4** In Example 7.5.1, compare the posterior mean $\hat\theta=\mu_n(\boldsymbol{x})$ with the classical MLE $\delta(\boldsymbol{x})=\bar x$. The posterior variance is $V^\pi(\boldsymbol{x})=\eta_n^2=\frac{\sigma^2\tau^2}{n\tau^2+\sigma^2}$, which is the PMSE of $\hat\theta$, while

$$
\operatorname{PMSE}(\bar x)=V^\pi(\boldsymbol{x})+\big(\mu^\pi(\boldsymbol{x})-\bar x\big)^2=V^\pi(\boldsymbol{x})+\Big(\frac{\sigma^2/n}{\sigma^2/n+\tau^2}\Big)^2(\mu-\bar x)^2\ge V^\pi(\boldsymbol{x}).
$$

**Example 7.5.5** In the same model take the uniform prior $\pi(\theta)\propto1$. Then

$$
\pi(\theta\mid\boldsymbol{x})\propto(2\pi\sigma^2)^{-n/2}\exp\Big\{-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\theta)^2\Big\}\propto\exp\Big\{-\frac{1}{2\sigma^2/n}(\theta-\bar x)^2\Big\},
$$
the normal distribution $\mathcal{N}(\bar x,\sigma^2/n)$. The posterior mean is $\hat\theta=\bar x$ with PMSE $V^\pi(\boldsymbol{x})=\sigma^2/n$: numerically the classical estimate and its variance, now with a conditional interpretation. This is the limit $\tau^2\to\infty$ of Example 7.5.1.

**Example 7.5.6** Let $X\sim\mathrm{Bin}(n,\theta)$ with prior $\mathrm{Beta}(a,b)$. The posterior mean estimate $\hat\theta_{\mathrm{mean}}=\frac{x+a}{n+a+b}$ has PMSE equal to the posterior variance

$$
V^\pi(x)=\frac{(x+a)(n-x+b)}{(a+b+n)^2(a+b+n+1)}.
$$
Under the uniform prior $\mathrm{U}(0,1)=\mathrm{Beta}(1,1)$, $\hat\theta_{\mathrm{mean}}=\frac{x+1}{n+2}$, $\hat\theta_{\mathrm{MAP}}=\frac xn$, $V^\pi(x)=\frac{(x+1)(n-x+1)}{(n+2)^2(n+3)}$, and

$$
\operatorname{PMSE}(\hat\theta_{\mathrm{MAP}})=V^\pi(x)+\big(\mu^\pi(x)-\hat\theta_{\mathrm{MAP}}\big)^2=\frac{(x+1)(n-x+1)}{(n+2)^2(n+3)}+\Big(\frac{x+1}{n+2}-\frac xn\Big)^2\ge V^\pi(x).
$$

## 7.6. Bayesian Interval Estimation

**Definition 7.6.1 (Credible Interval)** Let $\pi(\theta\mid\boldsymbol{x})$ be the posterior distribution of $\theta$ given $\boldsymbol{x}$, and let $0<\alpha<1$.

1. If there are statistics $\hat\theta_1=\hat\theta_1(\boldsymbol{x})$ and $\hat\theta_2=\hat\theta_2(\boldsymbol{x})$ such that $\mathbb{P}\big(\hat\theta_1\le\theta\le\hat\theta_2\mid\boldsymbol{x}\big)\ge1-\alpha$, then $[\hat\theta_1,\hat\theta_2]$ is a **credible interval** (Bayesian credible interval) for $\theta$ with credible level $1-\alpha$.
2. If $\mathbb{P}(\theta\ge\hat\theta_L\mid\boldsymbol{x})\ge1-\alpha$, then $\hat\theta_L=\hat\theta_L(\boldsymbol{x})$ is a Bayesian lower credible limit with credible level $1-\alpha$.
3. If $\mathbb{P}(\theta\le\hat\theta_U\mid\boldsymbol{x})\ge1-\alpha$, then $\hat\theta_U=\hat\theta_U(\boldsymbol{x})$ is a Bayesian upper credible limit with credible level $1-\alpha$.

The interpretation is direct. If, given the observed $\boldsymbol{x}$, the credible interval at level $0.90$ is $[1.2,2.0]$, then (for a continuous posterior) $\mathbb{P}(1.2\le\theta\le2.0\mid\boldsymbol{x})=0.90$: the probability that $\theta$ lies in this particular interval is $0.90$, which is exactly the statement a **confidence interval** cannot make (§7.1.2). Credible intervals are also often much easier to construct, since no pivot is needed: we only need quantiles of the posterior. The simplest choice is the equal-tailed interval between the $\alpha/2$ and $1-\alpha/2$ posterior quantiles. Among all intervals with the same credible level, the shortest is obtained by collecting the parameter values of highest posterior density.

**Definition 7.6.2 (HPD Interval)** A set $C=\{\theta\colon\pi(\theta\mid\boldsymbol{x})\ge k\}$, with $k$ the largest constant such that $\mathbb{P}(\theta\in C\mid\boldsymbol{x})\ge1-\alpha$, is a **highest posterior density** (HPD) region with credible level $1-\alpha$; when it is an interval it is called an HPD interval.

Every point inside an HPD region has higher posterior density than every point outside. For a unimodal posterior the HPD region is an interval, the shortest credible interval at the given level; for a symmetric unimodal posterior it coincides with the equal-tailed interval.

![Equal-tailed and HPD 90% credible intervals for a skewed Beta(3, 12) posterior: the HPD interval is shorter and its endpoints have equal posterior density.](./plots/credible-intervals.py)

**Example 7.6.1** In Example 7.5.1 the posterior is $\mathcal{N}\big(\mu_n(\boldsymbol{x}),\eta_n^2\big)$, so

$$
\mathbb{P}\big(\mu_n(\boldsymbol{x})-\eta_nz_{\alpha/2}\le\theta\le\mu_n(\boldsymbol{x})+\eta_nz_{\alpha/2}\mid\boldsymbol{x}\big)=1-\alpha,
$$
and $\big[\mu_n(\boldsymbol{x})-\eta_nz_{\alpha/2},\ \mu_n(\boldsymbol{x})+\eta_nz_{\alpha/2}\big]$ is a credible interval with credible level $1-\alpha$; it is also the HPD interval.

**Example 7.6.2 (IQ)** The IQ score of a child is $X\sim\mathcal{N}(\theta,100)$, where $\theta$ is the child's true IQ, and the prior for $\theta$ (the population of children) is $\mathcal{N}(100,225)$. A child scores $x=115$. By Eq. (7.1) with $n=1$, the posterior is $\mathcal{N}(\mu(x),\eta^2)$ with

$$
\mu(x)=\frac{\sigma^2}{\sigma^2+\tau^2}\mu+\frac{\tau^2}{\sigma^2+\tau^2}x=\frac{100}{325}\cdot100+\frac{225}{325}\cdot115=110.38,\qquad \eta^2=\frac{\sigma^2\tau^2}{\sigma^2+\tau^2}=\frac{100\cdot225}{325}=8.32^2 .
$$
A $95\%$ credible interval for $\theta$ is $[\mu(x)-1.96\eta,\ \mu(x)+1.96\eta]=[94.08,\ 126.69]$. The classical $95\%$ confidence interval is $[x-1.96\sigma,\ x+1.96\sigma]=[115-19.6,\ 115+19.6]=[95.4,\ 134.6]$. The credible interval is shorter, because it uses the prior information, and it is shifted toward the population mean $100$: an unusually high score is partly due to luck.

## 7.7. Bayesian Hypothesis Testing

To test $H_0\colon\theta\in\Theta_0$ against $H_1\colon\theta\in\Theta_1$, the Bayesian simply computes the posterior probabilities of the two hypotheses,

$$
\alpha_0=\mathbb{P}(\theta\in\Theta_0\mid x),\qquad\alpha_1=\mathbb{P}(\theta\in\Theta_1\mid x),
$$
and rejects $H_0$ if $\alpha_0<\alpha_1$, accepting $H_0$ otherwise. The ratio $\alpha_0/\alpha_1$ is the *posterior odds* of $H_0$. Unlike a $p$-value, $\alpha_0$ is the probability of $H_0$ given the data.

**Example 7.7.1** Let $X\sim\mathrm{Bin}(n,\theta)$ with the uniform prior $\mathrm{U}(0,1)$, and test $H_0\colon\theta\le1/2$ against $H_1\colon\theta>1/2$. The posterior is $\mathrm{Beta}(x+1,n-x+1)$, $\pi(\theta\mid x)=\frac{\theta^x(1-\theta)^{n-x}}{\mathrm{B}(x+1,n-x+1)}$, so

$$
\alpha_0=\mathbb{P}(\theta\in\Theta_0\mid x)=\frac{1}{\mathrm{B}(x+1,n-x+1)}\int_0^{1/2}\theta^x(1-\theta)^{n-x}\,\mathrm{d}\theta .
$$
For $n=5$:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\alpha_0$ | 63/64 | 57/64 | 42/64 | 22/64 | 7/64 | 1/64 |
| $\alpha_1$ | 1/64 | 7/64 | 22/64 | 42/64 | 57/64 | 63/64 |
| $\alpha_0/\alpha_1$ | 63.0 | 8.14 | 1.91 | 0.52 | 0.12 | 0.016 |

We accept $H_0$ if $x=0,1,2$ and reject it if $x=3,4,5$.

**Example 7.7.2 (IQ)** In Example 7.6.2, test $H_0\colon\theta\le100$ against $H_1\colon\theta>100$. With the posterior $\mathcal{N}(110.38,8.32^2)$,

$$
\alpha_0=\mathbb{P}(\theta\le100\mid x)=0.106,\qquad\alpha_1=\mathbb{P}(\theta>100\mid x)=0.894,
$$
so we reject $H_0$.

The posterior odds depend on the prior probabilities $\pi_0=\mathbb{P}(\theta\in\Theta_0)$ and $\pi_1=\mathbb{P}(\theta\in\Theta_1)$. Dividing them out isolates the evidence provided by the data.

**Definition 7.7.1 (Bayes Factor)** The **Bayes factor** in favor of $H_1$ is the ratio of posterior odds to prior odds,

$$
\mathrm{BF}_{10}=\frac{\alpha_1/\alpha_0}{\pi_1/\pi_0}=\frac{m_1(x)}{m_0(x)},\qquad m_i(x)=\int_{\Theta_i}f(x\mid\theta)\,\pi_i(\theta)\,\mathrm{d}\theta,
$$
where $\pi_i$ is the prior density restricted to $\Theta_i$ and renormalized, so that $m_i(x)$ is the marginal likelihood of the data under $H_i$.

The second expression follows from Bayes' formula, since $\alpha_i\propto\pi_im_i(x)$. Thus posterior odds $=$ Bayes factor $\times$ prior odds. For two simple hypotheses the Bayes factor is the likelihood ratio $f(x\mid\theta_1)/f(x\mid\theta_0)$; in general it compares the average likelihoods of the two models, and it can compare any two models $M_0,M_1$ for the same data. Values $\mathrm{BF}_{10}>1$ indicate that the data support $H_1$. In Example 7.7.1 the uniform prior gives $\pi_0=\pi_1=1/2$, so the Bayes factor equals the posterior odds $\alpha_1/\alpha_0$.

The method extends directly to several hypotheses. To choose among $H_i\colon\theta\in\Theta_i$, $i=1,\dots,k$, with $\Theta_1\cup\cdots\cup\Theta_k=\Theta$, compute $\alpha_i=\mathbb{P}(\theta\in\Theta_i\mid x)$ and accept the hypothesis $H_j$ with $\alpha_j=\max_{1\le i\le k}\alpha_i$.

**Example 7.7.3 (IQ, Three Hypotheses)** In Example 7.6.2 consider $H_1\colon\theta\le90$, $H_2\colon90<\theta<110$, $H_3\colon\theta\ge110$. From the posterior $\mathcal{N}(110.38,8.32^2)$,

$$
\alpha_1=\mathbb{P}(\theta\le90\mid x)=0.007,\qquad\alpha_2=\mathbb{P}(90<\theta<110\mid x)=0.474,\qquad\alpha_3=\mathbb{P}(\theta\ge110\mid x)=0.518,
$$
so we accept $H_3$, although only by a small margin over $H_2$.

## 7.8. Bayesian Prediction

Let $X\sim f(x\mid\theta)$, let $\boldsymbol{X}=(X_1,\dots,X_n)$ be a sample from $X$, and let a future random variable $Z$ have density $g(z\mid\theta)$. How should we predict $Z$? Usually $Z$ and $\boldsymbol{X}$ are assumed independent given $\theta$. Then, given $\boldsymbol{X}=\boldsymbol{x}$, the joint density of $(Z,\theta)$ is $g(z\mid\theta)\pi(\theta\mid\boldsymbol{x})$, and integrating out $\theta$ gives the distribution of $Z$ given $\boldsymbol{x}$.

**Definition 7.8.1 (Posterior Predictive Distribution)** Let $\pi(\theta\mid\boldsymbol{x})$ be the posterior density of $\theta$ given $\boldsymbol{x}$. The **posterior predictive distribution** of $Z$ has density

$$
p(z\mid\boldsymbol{x})=\int_\Theta g(z\mid\theta)\,\pi(\theta\mid\boldsymbol{x})\,\mathrm{d}\theta .
$$

The predictive distribution accounts for two sources of uncertainty, the sampling variability of $Z$ given $\theta$ and the remaining uncertainty about $\theta$; plugging in a point estimate $\hat\theta$ would ignore the second.

**Example 7.8.1 (A Gambler)** A gambler won $3$ of the first $10$ games. Predict the number of wins in the next $5$ games. Model the number of wins in $n$ games by $X\sim\mathrm{Bin}(n,\theta)$, $f(x\mid\theta)=\binom nx\theta^x(1-\theta)^{n-x}$, and take the conjugate prior $\mathrm{Beta}(a,b)$, so that

$$
\pi(\theta\mid x)=\frac{\Gamma(n+a+b)}{\Gamma(x+a)\Gamma(n-x+b)}\theta^{x+a-1}(1-\theta)^{n-x+b-1}.
$$
Let $Z$ be the number of wins in the next $k$ games, $g(z\mid\theta)=\binom kz\theta^z(1-\theta)^{k-z}$, $z=0,1,\dots,k$. Then

$$
\begin{aligned}
p(z\mid x)&=\int_0^1\binom kz\theta^z(1-\theta)^{k-z}\pi(\theta\mid x)\,\mathrm{d}\theta=c\int_0^1\theta^{z+x+a-1}(1-\theta)^{k-z+n-x+b-1}\,\mathrm{d}\theta\\
&=c\,\frac{\Gamma(z+x+a)\Gamma(k-z+n-x+b)}{\Gamma(k+n+a+b)},\qquad c=\binom kz\frac{\Gamma(n+a+b)}{\Gamma(x+a)\Gamma(n-x+b)},
\end{aligned}
$$
the *beta-binomial distribution*. Here $n=10$, $x=3$, $k=5$; with the uniform prior $a=b=1$,

$$
p(z\mid x=3)=\binom5z\frac{\Gamma(12)\Gamma(4+z)\Gamma(13-z)}{\Gamma(4)\Gamma(8)\Gamma(17)},\qquad z=0,1,\dots,5,
$$
which gives

| $z$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $p(z\mid 3)$ | 0.1813 | 0.3022 | 0.2747 | 0.1648 | 0.0641 | 0.0128 |

Hence $\mathbb{P}(0\le Z\le3\mid x)=0.923$: with probability about $92\%$ the gambler wins at most $3$ of the next $5$ games.

## 7.9. Statistical Decision Theory

Decision theory formalizes choices under uncertainty by attaching costs to actions. Consider an example. You have been exposed to a deadly virus. About $1/3$ of the people exposed are infected, and all those infected die unless they receive a vaccine; by the time symptoms appear it is too late for the vaccine to work. You are offered the vaccine for £500. Do you take it? The most likely scenario is that you are not infected, but a decision based on this alone ignores the losses associated with the decisions, and we would put a very high loss on dying.

**Definition 7.9.1 (Bayes Action)** Let $\mathcal{A}$ be the set of possible actions and $L(a,\theta)\ge0$ a **loss function**, the loss incurred by taking action $a$ when the parameter is $\theta$. The posterior expected loss of $a$ is

$$
R(a\mid x)=\mathbb{E}\big[L(a,\theta)\mid x\big]=\int_\Theta L(a,\theta)\,\pi(\theta\mid x)\,\mathrm{d}\theta,
$$
and a **Bayes action** is an action $a^*\in\mathcal{A}$ that minimizes it, $a^*=\arg\min_{a\in\mathcal{A}}R(a\mid x)$.

In the vaccine example the state is "infected" (probability $1/3$) or "not infected" ($2/3$). Vaccination costs $500$ in both states, and declining costs $0$ if not infected and $L_{\mathrm{death}}$ if infected. The expected losses are $500$ and $L_{\mathrm{death}}/3$, so the Bayes action is to take the vaccine whenever the loss of dying is valued above £1500, as it surely is.

Point estimation and testing are decision problems with $\mathcal{A}=\Theta$ or $\mathcal{A}=\{\text{accept }H_0,\text{reject }H_0\}$, and the Bayes estimators of §7.5 are Bayes actions for particular losses.

**Theorem 7.9.1** For a real parameter:

1. under the squared loss $L(a,\theta)=(a-\theta)^2$, the Bayes action is the posterior mean (Theorem 7.5.1);
2. under the absolute loss $L(a,\theta)=\lvert a-\theta\rvert$, the Bayes action is a posterior median;
3. for testing $H_0\colon\theta\in\Theta_0$ against $H_1\colon\theta\in\Theta_1$ under the $0$–$1$ loss (loss $1$ for a wrong decision, $0$ for a correct one), the Bayes action chooses the hypothesis with the larger posterior probability, which is the rule of §7.7.

**Proof** Part 1 is Theorem 7.5.1. For part 2, $\frac{\mathrm{d}}{\mathrm{d}a}\mathbb{E}[\lvert a-\theta\rvert\mid x]=\mathbb{P}(\theta<a\mid x)-\mathbb{P}(\theta>a\mid x)$ for a continuous posterior, which is negative for $a$ below a median and positive above it. For part 3, accepting $H_0$ has expected loss $\alpha_1$ and rejecting it has expected loss $\alpha_0$, so we reject exactly when $\alpha_0<\alpha_1$. $\square$

With unequal losses, say $c_{\mathrm{I}}$ for a type I error and $c_{\mathrm{II}}$ for a type II error, the same argument rejects $H_0$ when $c_{\mathrm{I}}\alpha_0<c_{\mathrm{II}}\alpha_1$, which is how the vaccine decision was made.

## Summary {#summary}

| | Frequentist | Bayesian |
|---|---|---|
| parameter $\theta$ | fixed unknown constant | random variable with prior $\pi(\theta)$ |
| probability | long-run frequency | degree of belief |
| basis of inference | sampling distribution of statistics over repeated samples | posterior $\pi(\theta\mid\boldsymbol{x})\propto f(\boldsymbol{x}\mid\theta)\pi(\theta)$, given the observed data |
| point estimation | MLE, UMVUE, moments; judged by bias, variance, MSE | posterior mean (squared loss), median (absolute loss), mode (MAP); judged by PMSE |
| interval | confidence interval: covers $\theta$ in $1-\alpha$ of repetitions | credible interval: $\mathbb{P}(\theta\in C\mid\boldsymbol{x})\ge1-\alpha$; HPD is shortest |
| testing | $p$-value $=\mathbb{P}(\text{as extreme data}\mid H_0)$ | posterior probabilities $\alpha_0,\alpha_1$; Bayes factor $m_1(x)/m_0(x)$ |
| prediction | plug-in $g(z\mid\hat\theta)$ | posterior predictive $\int g(z\mid\theta)\pi(\theta\mid\boldsymbol{x})\,\mathrm{d}\theta$ |
| likelihood principle | violated by $p$-values | respected |

The prior is both the strength and the weak point of the method. Conjugate priors make the computations explicit; non-informative priors (uniform, Jeffreys, maximum entropy) aim at objectivity but may be improper, in which case the posterior must be checked to be proper; hierarchical priors pool information across related groups. As the sample size grows, the likelihood dominates the prior and Bayesian and classical answers usually agree (Example 7.2.1, Example 7.5.5).
