---
title: Multiparameter Models
description: Parameters of interest and nuisance parameters, joint, conditional and marginal posteriors; the multinomial model with Dirichlet priors; the normal model with unknown mean and variance under non-informative and normal-inverse-chi-square priors, its marginal likelihood and posterior predictive distribution; the Behrens–Fisher problem by simulation; the multivariate normal model with normal-inverse-Wishart and non-informative priors.
---

Almost every realistic model has more than one unknown parameter, while a question usually concerns only some of them. A normal sample has a mean and a variance, but we may only care about the mean; a survey with $k$ answer categories has $k-1$ free probabilities, but we may only care about the difference between two of them. The Bayesian answer to this situation is simple in principle: write down the joint posterior of all unknowns and integrate out those that are not of interest. This chapter develops that principle (§3.1) and works it out for the three classical multiparameter models: the multinomial with Dirichlet priors (§3.2), the normal with unknown mean and variance, first under a non-informative prior (§3.3) and then under its conjugate prior (§3.4), with the comparison of two normal means as an application (§3.5), and the multivariate normal (§3.6). These models extend the single-parameter models of [3.7.2](/3.7.2) and reuse its distributions, above all the **scaled inverse-chi-square distribution** (Definition 2.4.1). The distributions that appear for the first time here are collected, with their parametrizations in different references and software, in [3.7.4](/3.7.4). Exact results of this kind are available only for conjugate models; general models need the simulation methods of [3.7.5](/3.7.5), for which the factorizations of this chapter are the template.

## 3.1. Nuisance Parameters and Marginal Posteriors

Let the parameter be split as $\theta=(\theta_1,\theta_2)$, where each part may itself be a vector.

**Definition 3.1.1 (Parameter of Interest and Nuisance Parameter)** If inference is wanted only for $\theta_1$, then $\theta_1$ is the parameter of interest and $\theta_2$ is a **nuisance parameter**: it has to be in the model for the model to describe the data, but it is not the target of the analysis.

For normal data $y_i\mid\mu,\sigma^2\sim\mathcal{N}(\mu,\sigma^2)$ with both parameters unknown, interest commonly centers on $\mu$ and $\sigma^2$ is a nuisance parameter. The general framework of Bayesian inference for a multiparameter model is

$$
\begin{aligned}
\text{prior}\qquad&p(\theta_1,\theta_2),\\
\text{joint posterior}\qquad&p(\theta_1,\theta_2\mid y)\propto p(y\mid\theta_1,\theta_2)\,p(\theta_1,\theta_2),\\
\text{marginal posterior}\qquad&p(\theta_1\mid y)=\int p(\theta_1,\theta_2\mid y)\,\mathrm{d}\theta_2=\int p(\theta_1\mid\theta_2,y)\,p(\theta_2\mid y)\,\mathrm{d}\theta_2.
\end{aligned}
$$
The marginal posterior of the parameter of interest is obtained by averaging over the nuisance parameter. The last form says more: $p(\theta_1\mid y)$ is a mixture of the conditional posteriors $p(\theta_1\mid\theta_2,y)$, one for each value of the nuisance parameter, weighted by the marginal posterior $p(\theta_2\mid y)$ of the nuisance parameter. Frequentist methods remove nuisance parameters by conditioning on a statistic, by plugging in an estimate, or by finding a **pivotal quantity** whose distribution does not involve them; the Bayesian approach has a single rule, integration, which always applies.

The mixture form translates directly into simulation, the **Monte Carlo method** that [3.7.5](/3.7.5) develops. The joint posterior factors as

$$
p(\theta_1,\theta_2\mid y)=p(\theta_1\mid\theta_2,y)\,p(\theta_2\mid y),
$$
so a draw from it is obtained in two steps: draw $\theta_2$ from its marginal posterior $p(\theta_2\mid y)$, then draw $\theta_1$ from the conditional posterior $p(\theta_1\mid\theta_2,y)$ at that value. Repeating this gives draws $(\theta_1^s,\theta_2^s)$, $s=1,\dots,S$, from the joint posterior; keeping only the $\theta_1^s$ gives draws from the marginal posterior $p(\theta_1\mid y)$, without computing the integral. In conjugate models both factors are standard distributions. The factor $p(\theta_2\mid y)$ itself can often be found without integration from

$$
p(\theta_2\mid y)=\frac{p(\theta_1,\theta_2\mid y)}{p(\theta_1\mid\theta_2,y)},
$$
which holds for every value of $\theta_1$, so that all factors involving $\theta_1$ must cancel, the same device that gave the negative binomial prior predictive distribution in [3.7.2](/3.7.2).

## 3.2. The Multinomial Model and the Dirichlet Prior

### 3.2.1. The Model

A document can be summarized by how often each word of a vocabulary occurs in it, ignoring the order of the words: the **bag of words** representation. If the words of a document are drawn independently from a vocabulary of $k$ words with probabilities $\theta_1,\dots,\theta_k$, the vector of counts $\boldsymbol{y}=(y_1,\dots,y_k)$, $\sum_jy_j=n$, follows the **multinomial distribution** $\mathrm{Mult}(n,\boldsymbol{\theta})$; topic models of text are built from such multinomial components. More generally the multinomial model describes $n$ independent observations each falling into one of $k$ categories. Its likelihood is

$$
p(\boldsymbol{y}\mid\boldsymbol{\theta})\propto\prod_{j=1}^k\theta_j^{y_j},\qquad\boldsymbol{\theta}\in\Delta_k=\Big\{\boldsymbol{\theta}\colon\theta_j\ge0,\ \sum_{j=1}^k\theta_j=1\Big\},
$$
a generalization of the binomial likelihood $\theta^y(1-\theta)^{n-y}$ (the case $k=2$). The parameter has $k-1$ free components. Just as the Beta family is conjugate to the binomial ([3.7.1](/3.7.1)), its multivariate analogue is conjugate to the multinomial.

### 3.2.2. The Dirichlet Distribution

**Definition 3.2.1 (Dirichlet Distribution)** Let $\boldsymbol{\alpha}=(\alpha_1,\dots,\alpha_k)$ with all $\alpha_j>0$, and $\alpha_0=\sum_{j=1}^k\alpha_j$. The **Dirichlet distribution** $\mathrm{Dir}(\boldsymbol{\alpha})$ is the distribution on the simplex $\Delta_k$ with density

$$
p(\boldsymbol{\theta}\mid\boldsymbol{\alpha})=\frac{\Gamma(\alpha_0)}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_k)}\prod_{j=1}^k\theta_j^{\alpha_j-1},\qquad\boldsymbol{\theta}\in\Delta_k,
$$
with respect to Lebesgue measure on $(\theta_1,\dots,\theta_{k-1})$, where $\theta_k=1-\sum_{j<k}\theta_j$.

For $k=2$ this is the **beta distribution**: $(\theta_1,1-\theta_1)\sim\mathrm{Dir}(\alpha_1,\alpha_2)$ if and only if $\theta_1\sim\mathrm{Beta}(\alpha_1,\alpha_2)$. The moments are

$$
\mathbb{E}\theta_j=\frac{\alpha_j}{\alpha_0},\qquad\operatorname{Var}\theta_j=\frac{\alpha_j(\alpha_0-\alpha_j)}{\alpha_0^2(\alpha_0+1)},\qquad\operatorname{Cov}(\theta_i,\theta_j)=-\frac{\alpha_i\alpha_j}{\alpha_0^2(\alpha_0+1)}\quad(i\ne j),
$$
and if all $\alpha_j>1$ the mode is $\theta_j=\frac{\alpha_j-1}{\alpha_0-k}$. The covariances are negative because the components must sum to one. The mean vector $\boldsymbol{\alpha}/\alpha_0$ gives the location and the total $\alpha_0$ the concentration: the larger $\alpha_0$, the smaller all variances.

**Proposition 3.2.1 (Gamma Representation and Aggregation)** Let $G_1,\dots,G_k$ be independent with $G_j\sim\Gamma(\alpha_j,1)$ and $G=\sum_jG_j$. Then $\boldsymbol{\theta}=(G_1/G,\dots,G_k/G)\sim\mathrm{Dir}(\boldsymbol{\alpha})$, independently of $G\sim\Gamma(\alpha_0,1)$. Consequently, if $\boldsymbol{\theta}\sim\mathrm{Dir}(\boldsymbol{\alpha})$:

1. merging categories adds their parameters: $(\theta_1+\theta_2,\theta_3,\dots,\theta_k)\sim\mathrm{Dir}(\alpha_1+\alpha_2,\alpha_3,\dots,\alpha_k)$, and in general the sums of $\boldsymbol{\theta}$ over the blocks of any partition of the categories are Dirichlet with the summed parameters;
2. each component is Beta: $\theta_j\sim\mathrm{Beta}(\alpha_j,\alpha_0-\alpha_j)$.

**Proof** The joint density of $(G_1,\dots,G_k)$ is $\prod_j\frac{1}{\Gamma(\alpha_j)}g_j^{\alpha_j-1}\mathrm{e}^{-g_j}$. Change variables to $(\theta_1,\dots,\theta_{k-1},G)$ with $g_j=G\theta_j$ ($\theta_k=1-\sum_{j<k}\theta_j$); the Jacobian is $G^{k-1}$. The new density is

$$
\prod_{j=1}^k\frac{(G\theta_j)^{\alpha_j-1}}{\Gamma(\alpha_j)}\,\mathrm{e}^{-G}\,G^{k-1}=\frac{\prod_j\theta_j^{\alpha_j-1}}{\prod_j\Gamma(\alpha_j)}\,G^{\alpha_0-1}\mathrm{e}^{-G},
$$
which factors into a $\mathrm{Dir}(\boldsymbol{\alpha})$ density of $\boldsymbol{\theta}$ and a $\Gamma(\alpha_0,1)$ density of $G$. For the aggregation property, $G_1+G_2\sim\Gamma(\alpha_1+\alpha_2,1)$ is independent of $G_3,\dots,G_k$, and $\theta_1+\theta_2=(G_1+G_2)/G$; apply the first part to the $k-1$ variables $G_1+G_2,G_3,\dots,G_k$. Merging all categories except $j$ gives $(\theta_j,1-\theta_j)\sim\mathrm{Dir}(\alpha_j,\alpha_0-\alpha_j)$. $\square$

The representation is also the standard way to simulate from a Dirichlet distribution.

### 3.2.3. Conjugate Posterior

With the prior $\boldsymbol{\theta}\sim\mathrm{Dir}(\boldsymbol{\alpha})$, $p(\boldsymbol{\theta})\propto\prod_j\theta_j^{\alpha_j-1}$,

$$
p(\boldsymbol{\theta}\mid\boldsymbol{y})\propto\prod_{j=1}^k\theta_j^{\alpha_j+y_j-1},\qquad\boldsymbol{\theta}\mid\boldsymbol{y}\sim\mathrm{Dir}(\boldsymbol{\alpha}+\boldsymbol{y}).
$$
As in the binomial model, the **hyperparameters** act as prior counts. Relative to the uniform baseline $\mathrm{Dir}(1,\dots,1)$, the prior $\mathrm{Dir}(\boldsymbol{\alpha})$ is worth $\sum_j\alpha_j-k$ observations, $\alpha_j-1$ of them in category $j$; relative to the improper baseline $\mathrm{Dir}(0,\dots,0)$ it is worth $\alpha_0$ observations, $\alpha_j$ in category $j$. The posterior mean

$$
\mathbb{E}(\theta_j\mid\boldsymbol{y})=\frac{\alpha_j+y_j}{\alpha_0+n}=\frac{n}{\alpha_0+n}\cdot\frac{y_j}{n}+\frac{\alpha_0}{\alpha_0+n}\cdot\frac{\alpha_j}{\alpha_0}
$$
is a weighted average of the observed proportion and the prior mean, with weights $n$ and $\alpha_0$. In machine learning this estimate with all $\alpha_j=1$ is known as Laplace smoothing ([4.6.3](/4.6.3)).

*Collapsing.* By Proposition 3.2.1 the marginal posterior of one probability is $\theta_j\mid\boldsymbol{y}\sim\mathrm{Beta}(\alpha_j+y_j,\alpha_0-\alpha_j+n-y_j)$. This is exactly the posterior of a binomial analysis that only distinguishes "category $j$" from "any other category", with prior $\mathrm{Beta}(\alpha_j,\alpha_0-\alpha_j)$: coarsening the categories, before or after the analysis, gives the same answer. The marginal posterior of a sum such as $\theta_1+\theta_2$ is Beta in the same way. Contrasts such as $\theta_1-\theta_2$ or ratios $\theta_1/\theta_2$ are not Beta, and they are handled by simulating $\boldsymbol{\theta}$.

*Posterior predictive distribution.* For one new observation $\tilde y$, by the **law of total expectation**,

$$
\mathbb{P}(\tilde y=j\mid\boldsymbol{y})=\mathbb{E}(\theta_j\mid\boldsymbol{y})=\frac{\alpha_j+y_j}{\alpha_0+n},
$$
the multinomial version of Laplace's rule of succession $\frac{y+1}{n+2}$ ([3.7.1](/3.7.1)). The counts of $m$ new observations have the Dirichlet-multinomial distribution with parameters $m$ and $\boldsymbol{\alpha}+\boldsymbol{y}$ ([3.7.4](/3.7.4)).

*Non-informative priors.* Three choices are in common use:

| Prior | Rationale | Properness of the posterior |
|---|---|---|
| $\alpha_j=\frac12$ for all $j$ | **Jeffreys' prior** for the multinomial model | always proper |
| $\alpha_j=1$ for all $j$ | uniform on the simplex $\Delta_k$ | always proper |
| $\alpha_j=0$ for all $j$ | flat on the log-ratios $\log(\theta_j/\theta_k)$, the multivariate logit | proper only if every $y_j\ge1$ |

The last row generalizes $\mathrm{Beta}(0,0)$ of [3.7.2](/3.7.2): under $\phi_j=\log(\theta_j/\theta_k)$, $j<k$, a flat density on $(\phi_1,\dots,\phi_{k-1})$ corresponds to $p(\boldsymbol{\theta})\propto\prod_j\theta_j^{-1}$. When $k$ is large relative to $n$, as with a vocabulary of words, these priors are far from harmless: $\mathrm{Dir}(1,\dots,1)$ adds one prior count to each of $k$ categories, $k$ in total, which can outweigh the data for rare categories.

**Example 3.2.1 (Symptom Words)** In a collection of medical records restricted to four words describing symptoms, the counts are thirst $y_1=10$, polyuria $y_2=8$, hunger $y_3=15$ and weight loss $y_4=13$, so $n=46$. With the uniform prior $\mathrm{Dir}(1,1,1,1)$ the posterior is $\mathrm{Dir}(11,9,16,14)$, with $\alpha_0+n=50$ and posterior means $0.22,0.18,0.32,0.28$. The probability of "hunger" has marginal posterior $\mathrm{Beta}(16,34)$, with $95\%$ central posterior interval $[0.199,0.454]$. Is "hunger" more frequent than "thirst"? Simulating $\boldsymbol{\theta}$ from $\mathrm{Dir}(11,9,16,14)$ by Proposition 3.2.1 gives $\mathbb{P}(\theta_3>\theta_1\mid\boldsymbol{y})\approx0.84$ and a $95\%$ interval $[-0.10,0.30]$ for $\theta_3-\theta_1$: the data favor "hunger", but not decisively. The predictive probability that the next of these words is "hunger" is $0.32$.

## 3.3. The Normal Model with a Non-informative Prior

### 3.3.1. The Location–Scale t Notation

The marginal posteriors of normal means turn out to be shifted and scaled $t$-distributions, for which we use the following notation.

**Remark 3.3.1** For $\nu>0$, $\mu\in\mathbb{R}$ and $\sigma>0$ we write $\theta\sim t_\nu(\mu,\sigma^2)$ if $(\theta-\mu)/\sigma$ follows the **t-distribution** $t_\nu$ ([3.1.4](/3.1.4)), so that

$$
p(\theta)=\frac{\Gamma(\frac{\nu+1}{2})}{\Gamma(\frac\nu2)\sqrt{\nu\pi}\,\sigma}\Big(1+\frac1\nu\Big(\frac{\theta-\mu}{\sigma}\Big)^2\Big)^{-(\nu+1)/2},
$$
and $t_\nu=t_\nu(0,1)$. The second parameter $\sigma^2$ is the square of the scale, not the variance: $\operatorname{Var}\theta=\frac{\nu}{\nu-2}\sigma^2$ for $\nu>2$. As $\nu\to\infty$, $t_\nu(\mu,\sigma^2)\to\mathcal{N}(\mu,\sigma^2)$.

### 3.3.2. Joint, Conditional and Marginal Posteriors

Let $y_1,\dots,y_n\mid\mu,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ with both parameters unknown, and write

$$
\bar y=\frac1n\sum_{i=1}^ny_i,\qquad s^2=\frac{1}{n-1}\sum_{i=1}^n(y_i-\bar y)^2.
$$
A non-informative prior is obtained by combining the priors of [3.7.2](/3.7.2) for a location parameter and a scale parameter, flat in $\mu$ and in $\log\sigma$, and assuming that they are independent a priori:

$$
p(\mu,\sigma^2)\propto(\sigma^2)^{-1}.
$$
Each factor is **Jeffreys' prior** for its parameter with the other one known. (Jeffreys' rule $\lvert\det J\rvert^{1/2}$ applied to $(\mu,\sigma^2)$ jointly gives $(\sigma^2)^{-3/2}$ instead; the independence version is the standard choice because its posterior reproduces the classical $t$ results below.) Using $\sum_i(y_i-\mu)^2=(n-1)s^2+n(\bar y-\mu)^2$, the joint posterior is

$$
p(\mu,\sigma^2\mid y)\propto\sigma^{-n-2}\exp\Big(-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\mu)^2\Big)=\sigma^{-n-2}\exp\Big(-\frac{1}{2\sigma^2}\big[(n-1)s^2+n(\bar y-\mu)^2\big]\Big),
$$
which depends on the data only through the **sufficient statistic** $(\bar y,s^2)$.

**Proposition 3.3.1** Under the prior $p(\mu,\sigma^2)\propto\sigma^{-2}$ and with $n\ge2$:

1. $\mu\mid\sigma^2,y\sim\mathcal{N}(\bar y,\sigma^2/n)$;
2. $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$;
3. $\mu\mid y\sim t_{n-1}(\bar y,s^2/n)$, that is, $\dfrac{\mu-\bar y}{s/\sqrt n}\;\Big|\;y\sim t_{n-1}$;
4. $\sigma^2\mid\mu,y\sim\mathrm{Inv}\text{-}\chi^2(n,v)$ with $v=\frac1n\sum_i(y_i-\mu)^2$.

**Proof** (1) For fixed $\sigma^2$ the joint posterior is proportional to $\exp\big(-\frac{n}{2\sigma^2}(\mu-\bar y)^2\big)$, a normal kernel in $\mu$; this is the known-variance result of [3.7.2](/3.7.2) with a flat prior.

(2) Integrate $\mu$ out; the Gaussian integral is $\int\exp\big(-\frac{n}{2\sigma^2}(\bar y-\mu)^2\big)\,\mathrm{d}\mu=\sqrt{2\pi\sigma^2/n}$, so

$$
p(\sigma^2\mid y)\propto\sigma^{-n-2}\exp\Big(-\frac{(n-1)s^2}{2\sigma^2}\Big)\sqrt{2\pi\sigma^2/n}\propto(\sigma^2)^{-(n+1)/2}\exp\Big(-\frac{(n-1)s^2}{2\sigma^2}\Big),
$$
the kernel of $\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$, since $(n+1)/2=(n-1)/2+1$.

(3) Integrate $\sigma^2$ out. With $A=(n-1)s^2+n(\mu-\bar y)^2$ and the substitution $z=A/(2\sigma^2)$, $\mathrm{d}\sigma^2=-\frac{A}{2z^2}\,\mathrm{d}z$,

$$
p(\mu\mid y)\propto\int_0^\infty(\sigma^2)^{-(n+2)/2}\exp\Big(-\frac{A}{2\sigma^2}\Big)\,\mathrm{d}\sigma^2\propto A^{-n/2}\int_0^\infty z^{(n-2)/2}\mathrm{e}^{-z}\,\mathrm{d}z\propto\Big[1+\frac{n(\mu-\bar y)^2}{(n-1)s^2}\Big]^{-n/2},
$$
which is the $t_{n-1}(\bar y,s^2/n)$ kernel of Remark 3.3.1 with $\nu+1=n$.

(4) For fixed $\mu$ the joint posterior is $(\sigma^2)^{-(n/2+1)}\exp\big(-\frac{nv}{2\sigma^2}\big)$, as for the normal variance with known mean in [3.7.2](/3.7.2). $\square$

Parts (1) and (2) give the factorization $p(\mu,\sigma^2\mid y)=p(\mu\mid\sigma^2,y)\,p(\sigma^2\mid y)$ of §3.1, and hence the simulation scheme: draw $\sigma^2$ from $\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$, as $(n-1)s^2/X$ with $X\sim\chi^2_{n-1}$, then $\mu$ from $\mathcal{N}(\bar y,\sigma^2/n)$. Part (3) shows the mixture form at work: averaging the normal conditional posteriors over the uncertainty in $\sigma^2$ produces the heavier-tailed $t$. Parts (1) and (4) are the two full conditionals used by the Gibbs sampler of later chapters.

### 3.3.3. Comparison with Frequentist Pivotal Quantities

Classical inference for the normal mean and variance rests on two pivotal quantities ([3.2.4](/3.2.4)). The Bayesian results under $p(\mu,\sigma^2)\propto\sigma^{-2}$ give the same quantities the same distributions, with the roles of data and parameters exchanged:

| Quantity | Bayesian, given $y$ | Frequentist, given $(\mu,\sigma^2)$ |
|---|---|---|
| $\dfrac{\mu-\bar y}{s/\sqrt n}$ | $t_{n-1}$; $\mu$ random, $\bar y$ and $s$ fixed | $t_{n-1}$; $\bar y$ and $s$ random, $\mu$ fixed |
| $\dfrac{(n-1)s^2}{\sigma^2}$ | $\chi^2_{n-1}$; $\sigma^2$ random | $\chi^2_{n-1}$; $s^2$ random |

Consequently the $95\%$ central posterior interval $\bar y\pm t_{n-1,0.025}\,s/\sqrt n$ coincides numerically with the classical $t$ **confidence interval**, and the posterior probability $\mathbb{P}(\mu>\mu_0\mid y)$ equals one minus the one-sided $t$-test **p-value** for $H_0\colon\mu\le\mu_0$. The interpretations differ: the credible interval is a probability statement about $\mu$ given the observed data, the confidence interval a statement about the procedure over repeated samples.

The posterior predictive distribution of a new observation follows from $\tilde y=\mu+\varepsilon$: given $\sigma^2$ and $y$, $\tilde y\sim\mathcal{N}\big(\bar y,(1+\frac1n)\sigma^2\big)$, and averaging over $\sigma^2\mid y$ as in part (3) of Proposition 3.3.1 gives

$$
\tilde y\mid y\sim t_{n-1}\Big(\bar y,\Big(1+\frac1n\Big)s^2\Big),
$$
whose central intervals are the classical prediction intervals for a new normal observation.

## 3.4. The Normal Model with a Conjugate Prior

### 3.4.1. The Normal-Inverse-Chi-Square Family

The posterior of §3.3 has the structure "$\sigma^2$ scaled inverse-$\chi^2$, and $\mu$ given $\sigma^2$ normal with variance proportional to $\sigma^2$". A prior of the same structure is conjugate.

**Definition 3.4.1 (Normal-Inverse-Chi-Square Distribution)** Let $\mu_0\in\mathbb{R}$ and $\kappa_0,\nu_0,\sigma_0^2>0$. The pair $(\mu,\sigma^2)$ has the **normal-inverse-chi-square distribution** $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$ if

$$
\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2),\qquad\mu\mid\sigma^2\sim\mathcal{N}(\mu_0,\sigma^2/\kappa_0),
$$
that is, if its joint density is

$$
p(\mu,\sigma^2)\propto\sigma^{-1}(\sigma^2)^{-(\nu_0/2+1)}\exp\Big(-\frac{1}{2\sigma^2}\big[\nu_0\sigma_0^2+\kappa_0(\mu-\mu_0)^2\big]\Big).
$$

The four hyperparameters have the following meanings, all in the "prior data" sense of [3.7.2](/3.7.2):

| Hyperparameter | Meaning |
|---|---|
| $\mu_0$ | prior mean of $\mu$ |
| $\kappa_0$ | number of prior observations on which $\mu_0$ is based |
| $\sigma_0^2$ | prior estimate of the sampling variance $\sigma^2$ |
| $\nu_0$ | number of prior observations (degrees of freedom) on which $\sigma_0^2$ is based |

In this family $\mu$ and $\sigma^2$ are dependent a priori: the prior variance of $\mu$ given $\sigma^2$ is $\sigma^2/\kappa_0$, proportional to the sampling variance, as if $\mu_0$ were the mean of $\kappa_0$ earlier observations from the same population. This is natural when the prior information comes from earlier data of the same kind, but not always appropriate; an independent prior $\mu\sim\mathcal{N}(\mu_0,\tau_0^2)$, $\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$ is not conjugate (its conditional posteriors are standard, but the marginal posteriors are not), and it is treated by the simulation methods of [3.7.5](/3.7.5).

### 3.4.2. The Joint Posterior

**Theorem 3.4.1** Let $y_1,\dots,y_n\mid\mu,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ and $(\mu,\sigma^2)\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$. Then

$$
(\mu,\sigma^2)\mid y\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_n,\sigma_n^2/\kappa_n;\nu_n,\sigma_n^2),
$$
with

$$
\begin{aligned}
\mu_n&=\frac{\kappa_0}{\kappa_0+n}\mu_0+\frac{n}{\kappa_0+n}\bar y,\qquad\kappa_n=\kappa_0+n,\qquad\nu_n=\nu_0+n,\\
\nu_n\sigma_n^2&=\nu_0\sigma_0^2+(n-1)s^2+\frac{\kappa_0n}{\kappa_0+n}(\bar y-\mu_0)^2.
\end{aligned}
$$

**Proof** Multiply the prior density by the likelihood $(\sigma^2)^{-n/2}\exp\big(-\frac{1}{2\sigma^2}[(n-1)s^2+n(\bar y-\mu)^2]\big)$:

$$
p(\mu,\sigma^2\mid y)\propto\sigma^{-1}(\sigma^2)^{-((\nu_0+n)/2+1)}\exp\Big(-\frac{1}{2\sigma^2}\big[\nu_0\sigma_0^2+(n-1)s^2+\kappa_0(\mu-\mu_0)^2+n(\bar y-\mu)^2\big]\Big).
$$
Complete the square in $\mu$. The coefficient of $\mu^2$ in $\kappa_0(\mu-\mu_0)^2+n(\bar y-\mu)^2$ is $\kappa_n$ and that of $-2\mu$ is $\kappa_0\mu_0+n\bar y=\kappa_n\mu_n$, so

$$
\kappa_0(\mu-\mu_0)^2+n(\bar y-\mu)^2=\kappa_n(\mu-\mu_n)^2+\kappa_0\mu_0^2+n\bar y^2-\kappa_n\mu_n^2=\kappa_n(\mu-\mu_n)^2+\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2,
$$
where the last step is $\kappa_n(\kappa_0\mu_0^2+n\bar y^2)-(\kappa_0\mu_0+n\bar y)^2=\kappa_0n(\bar y-\mu_0)^2$. The bracket equals $\nu_n\sigma_n^2+\kappa_n(\mu-\mu_n)^2$, and the posterior has the form of Definition 3.4.1 with the stated parameters. $\square$

Each update has a direct reading. The posterior mean $\mu_n$ averages the prior mean and the sample mean with weights $\kappa_0$ and $n$. The two prior sample sizes grow by $n$. The posterior sum of squares $\nu_n\sigma_n^2$ adds three parts: the prior sum of squares $\nu_0\sigma_0^2$, the sample sum of squares $(n-1)s^2$, and a term for the disagreement between prior mean and sample mean, which increases the posterior uncertainty about $\sigma^2$ when the two conflict.

### 3.4.3. Conditional and Marginal Posteriors

By Definition 3.4.1 and Theorem 3.4.1,

$$
\mu\mid\sigma^2,y\sim\mathcal{N}\Big(\mu_n,\frac{\sigma^2}{\kappa_n}\Big),\qquad\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(\nu_n,\sigma_n^2).
$$
The conditional posterior of $\mu$ is the known-variance result of [3.7.2](/3.7.2), with prior precision $\kappa_0/\sigma^2$ and data precision $n/\sigma^2$:

$$
\mu_n=\frac{\frac{\kappa_0}{\sigma^2}\mu_0+\frac{n}{\sigma^2}\bar y}{\frac{\kappa_0}{\sigma^2}+\frac{n}{\sigma^2}},\qquad\frac{\kappa_n}{\sigma^2}=\frac{\kappa_0}{\sigma^2}+\frac{n}{\sigma^2};
$$
because both precisions are proportional to $1/\sigma^2$, the weights do not depend on $\sigma^2$. Integrating $\sigma^2$ out exactly as in part (3) of Proposition 3.3.1, now with $A=\nu_n\sigma_n^2+\kappa_n(\mu-\mu_n)^2$ and the power $(\sigma^2)^{-(\nu_n+3)/2}$, gives

$$
p(\mu\mid y)\propto\Big(1+\frac{\kappa_n(\mu-\mu_n)^2}{\nu_n\sigma_n^2}\Big)^{-(\nu_n+1)/2},\qquad\mu\mid y\sim t_{\nu_n}\Big(\mu_n,\frac{\sigma_n^2}{\kappa_n}\Big).
$$

### 3.4.4. The Marginal Likelihood

For a proper prior ($\kappa_0,\nu_0,\sigma_0^2>0$) the **marginal likelihood** $p(y)=\iint p(y\mid\mu,\sigma^2)\,p(\mu,\sigma^2)\,\mathrm{d}\mu\,\mathrm{d}\sigma^2$ is available in closed form. It is the quantity needed for Bayes factors ([3.7.8](/3.7.8)).

**Proposition 3.4.1** In the setting of Theorem 3.4.1,

$$
p(y)=\frac{\Gamma(\nu_n/2)}{\Gamma(\nu_0/2)}\sqrt{\frac{\kappa_0}{\kappa_n}}\,\frac{(\nu_0\sigma_0^2)^{\nu_0/2}}{(\nu_n\sigma_n^2)^{\nu_n/2}}\,\pi^{-n/2}.
$$

**Proof** By Bayes' rule, $p(y)=p(y\mid\mu,\sigma^2)\,p(\mu,\sigma^2)/p(\mu,\sigma^2\mid y)$ for every $(\mu,\sigma^2)$. Write the normalized $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$ density as $c(\kappa_0,\nu_0,\nu_0\sigma_0^2)\,\sigma^{-1}(\sigma^2)^{-(\nu_0/2+1)}\exp(\cdots)$ with

$$
c(\kappa,\nu,S)=\sqrt{\frac{\kappa}{2\pi}}\cdot\frac{(S/2)^{\nu/2}}{\Gamma(\nu/2)},
$$
the product of the normal and the scaled inverse-$\chi^2$ normalizing constants. The likelihood is $(2\pi)^{-n/2}(\sigma^2)^{-n/2}\exp(\cdots)$. In the ratio, the powers of $\sigma^2$ and the exponentials cancel by the proof of Theorem 3.4.1, leaving

$$
p(y)=(2\pi)^{-n/2}\,\frac{c(\kappa_0,\nu_0,\nu_0\sigma_0^2)}{c(\kappa_n,\nu_n,\nu_n\sigma_n^2)}.
$$
Since $\nu_n-\nu_0=n$, the powers of $2$ combine to $(2\pi)^{-n/2}\,2^{n/2}=\pi^{-n/2}$, which gives the formula. $\square$

The factor $\sqrt{\kappa_0/\kappa_n}$ tends to $0$ as $\kappa_0\to0$: with a vague prior on $\mu$, any particular data set has small prior predictive density, and with the improper prior of §3.3 the marginal likelihood is not defined at all.

### 3.4.5. The Posterior Predictive Distribution

A new observation is $\tilde y=\mu+\varepsilon$ with $\varepsilon\sim\mathcal{N}(0,\sigma^2)$ independent of $\mu$ given $\sigma^2$. Given $\sigma^2$ and $y$ it is therefore $\mathcal{N}\big(\mu_n,\sigma^2(1+\frac1{\kappa_n})\big)$, and averaging over $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(\nu_n,\sigma_n^2)$ as in §3.4.3 gives the **posterior predictive distribution**

$$
\tilde y\mid y\sim t_{\nu_n}\Big(\mu_n,\frac{\kappa_n+1}{\kappa_n}\sigma_n^2\Big).
$$
The same result follows from the marginal likelihood: $p(\tilde y\mid y)=p(y,\tilde y)/p(y)$, and by Proposition 3.4.1 applied to $n+1$ observations only the factor $(\nu_{n+1}\sigma_{n+1}^2)^{-(\nu_n+1)/2}$ depends on $\tilde y$, where updating the posterior once more by $\tilde y$ gives $\nu_{n+1}\sigma_{n+1}^2=\nu_n\sigma_n^2+\frac{\kappa_n}{\kappa_n+1}(\tilde y-\mu_n)^2$. Hence $p(\tilde y\mid y)\propto\big(\nu_n\sigma_n^2+\frac{\kappa_n}{\kappa_n+1}(\tilde y-\mu_n)^2\big)^{-(\nu_n+1)/2}$, the same $t$ kernel. The scale factor $\frac{\kappa_n+1}{\kappa_n}=1+\frac{1}{\kappa_n}$ adds the posterior uncertainty about $\mu$ to the sampling variability, as in the known-variance case.

### 3.4.6. Example and the Non-informative Limit

**Example 3.4.1 (Moisture of Cheese)** The water content (in percent) of the pieces of a cheese product is modeled as $\mathcal{N}(\mu,\sigma^2)$. What is the plausible range of the average water content $\mu$? Two analysts use the same data, the water contents of $25$ pieces:

$45.6, 41.1, 44.5, 44.0, 40.6, 44.1, 39.0, 39.5, 39.5, 41.7, 42.0, 42.6, 43.0, 42.5, 42.7, 42.1, 42.4, 44.8, 41.0, 39.9, 43.9, 41.3, 45.1, 38.5, 43.8$,

with $\bar y=42.208$ and $(n-1)s^2=95.618$. Ann has no prior information and uses $p(\mu,\sigma^2)\propto\sigma^{-2}$. Bob uses the conjugate prior with $\mu_0=40$, $\kappa_0=1$, $\nu_0=1$, and believes that the median of $\sigma$ is $3$. Since $\sigma^2=\nu_0\sigma_0^2/X$ with $X\sim\chi^2_1$, whose median is $0.4549$, the median of $\sigma^2$ is $\sigma_0^2/0.4549=3^2$, so $\sigma_0^2=4.094$. The posterior parameters are

| | $\mu_0$ | $\kappa_0$ | $\nu_0$ | $\nu_0\sigma_0^2$ | $\mu_n$ | $\kappa_n$ | $\nu_n$ | $\nu_n\sigma_n^2$ |
|---|---|---|---|---|---|---|---|---|
| Ann | — | — | — | — | $42.208$ | $25$ | $24$ | $95.618$ |
| Bob | $40$ | $1$ | $1$ | $4.094$ | $42.123$ | $26$ | $26$ | $95.618+4.094+\frac{25}{26}(42.208-40)^2=104.40$ |

and the marginal posteriors of $\mu$ are

| | $\mu\mid y$ | $95\%$ central posterior interval for $\mu$ | posterior median of $\sigma$ | $95\%$ posterior predictive interval |
|---|---|---|---|---|
| Ann | $t_{24}(42.208,\,0.3992^2)$ | $[41.38,\,43.03]$ | $2.02$ | $[38.01,\,46.41]$ |
| Bob | $t_{26}(42.123,\,0.3930^2)$ | $[41.32,\,42.93]$ | $2.03$ | $[37.93,\,46.32]$ |

Ann's interval is the classical $t$ interval (§3.3.3). Bob's prior mean lies about $5.5$ posterior standard deviations below $\bar y$, but it carries the weight of a single observation against $25$, so it moves the posterior mean by only $0.085$; his prior guess $\sigma\approx3$ exceeds the sample standard deviation $s=1.996$, but with one degree of freedom against $24$ it hardly changes the posterior of $\sigma$. Bob's interval is slightly narrower because $\nu_n$ and $\kappa_n$ are larger. With $25$ observations the data dominate both priors.

![Cheese moisture example. Left and middle: contours of the joint posterior density of (μ, σ) for Ann (non-informative prior) and Bob (conjugate prior), with 400 posterior draws obtained by drawing σ² and then μ given σ². Right: the marginal posterior t-densities of μ and Bob's prior mean.](./plots/cheese_joint_posterior.py)

*The non-informative prior as a limit.* Letting $\kappa_0\to0$, $\nu_0\to-1$ and $\sigma_0^2\to0$ in the density of Definition 3.4.1 gives

$$
p(\mu,\sigma^2)\propto\sigma^{-1}(\sigma^2)^{-(-1/2+1)}=\sigma^{-2},
$$
the prior of §3.3, and the posterior parameters of Theorem 3.4.1 become $\mu_n=\bar y$, $\kappa_n=n$, $\nu_n=n-1$ and $\nu_n\sigma_n^2=(n-1)s^2$, the results of Proposition 3.3.1. The value $\nu_0=-1$ shows that $p(\mu,\sigma^2)\propto\sigma^{-2}$ is not the conjugate prior with "zero prior data": it corresponds to minus one prior degree of freedom for the variance. This is the bookkeeping that makes the posterior of $\sigma^2$ have $n-1$ degrees of freedom, one being used to estimate $\mu$, exactly as in the classical theory.

## 3.5. Comparing Two Normal Means: the Behrens–Fisher Problem

Suppose $y_{11},\dots,y_{1n_1}$ are iid $\mathcal{N}(\mu_1,\sigma_1^2)$ and, independently, $y_{21},\dots,y_{2n_2}$ are iid $\mathcal{N}(\mu_2,\sigma_2^2)$, and consider $\delta=\mu_1-\mu_2$, for instance to assess $H_0\colon\delta=0$. When $\sigma_1^2=\sigma_2^2$, the classical analysis uses the pooled two-sample $t$ statistic, which is an exact pivotal quantity with $n_1+n_2-2$ degrees of freedom. When $\sigma_1^2\ne\sigma_2^2$, no exact pivotal quantity free of the variance ratio exists: this is the **Behrens–Fisher problem** ([3.2.4](/3.2.4)), for which frequentist practice relies on approximations such as **Welch's t-test**.

The Bayesian treatment needs no new idea. Give the two groups independent priors, for instance conjugate priors

$$
\mu_j\mid\sigma_j^2\sim\mathcal{N}(\mu_0,\sigma_j^2/\kappa_0),\qquad\sigma_j^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2),\qquad j=1,2,
$$
or the non-informative $p(\mu_j,\sigma_j^2)\propto\sigma_j^{-2}$. The likelihood factors over the groups, so the posteriors of $(\mu_1,\sigma_1^2)$ and $(\mu_2,\sigma_2^2)$ are independent, and by §3.4.3

$$
\mu_j\mid y\sim t_{\nu_{jn}}\Big(\mu_{jn},\frac{\sigma_{jn}^2}{\kappa_{jn}}\Big),\qquad j=1,2,
$$
with the group-specific posterior parameters of Theorem 3.4.1 (under the non-informative prior, $t_{n_j-1}(\bar y_j,s_j^2/n_j)$). The posterior of $\delta$ is the distribution of the difference of two independent $t$ variables with different degrees of freedom and scales. It has no standard closed form, but it is easily simulated: draw $\mu_1^s$ and $\mu_2^s$ from their posteriors and set $\delta^s=\mu_1^s-\mu_2^s$, $s=1,\dots,S$. Posterior probabilities such as $\mathbb{P}(\delta>0\mid y)$ and intervals for $\delta$ are then read off from the draws. Under the non-informative prior this posterior coincides with the Behrens–Fisher distribution of Fisher's fiducial argument, as Jeffreys observed.

**Example 3.5.1** Consider illustrative summary statistics $n_1=10$, $\bar y_1=5.2$, $s_1=1.0$ and $n_2=15$, $\bar y_2=4.4$, $s_2=2.5$, with non-informative priors. Then $\mu_1\mid y\sim t_9(5.2,\,0.316^2)$ and $\mu_2\mid y\sim t_{14}(4.4,\,0.645^2)$. With $S=4\times10^5$ draws, $\delta\mid y$ has mean $0.80$, $95\%$ central posterior interval $[-0.75,2.36]$, and $\mathbb{P}(\delta>0\mid y)=0.85$. Welch's approximate $95\%$ confidence interval is $[-0.70,2.30]$ with $19.8$ degrees of freedom, close to the Bayesian interval but obtained from an approximation to a sampling distribution that depends on the unknown variance ratio.

![Behrens–Fisher problem with illustrative summary data: marginal posteriors of μ₁ and μ₂ (left) and a histogram of simulated draws of δ = μ₁ − μ₂ with its 95% central posterior interval (right).](./plots/behrens_fisher.py)

## 3.6. The Multivariate Normal Model

### 3.6.1. The Likelihood

Let $\boldsymbol{y}_1,\dots,\boldsymbol{y}_n\in\mathbb{R}^d$ be iid with the **multivariate normal distribution** $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$. With the trace identity $\boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}=\operatorname{tr}(\Sigma^{-1}\boldsymbol{x}\boldsymbol{x}^{\mathsf T})$ the likelihood is

$$
p(\boldsymbol{y}_1,\dots,\boldsymbol{y}_n\mid\boldsymbol{\mu},\Sigma)\propto(\det\Sigma)^{-n/2}\exp\Big(-\frac12\sum_{i=1}^n(\boldsymbol{y}_i-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{y}_i-\boldsymbol{\mu})\Big)=(\det\Sigma)^{-n/2}\exp\Big(-\frac12\operatorname{tr}(\Sigma^{-1}S_0)\Big),
$$
where $S_0=\sum_i(\boldsymbol{y}_i-\boldsymbol{\mu})(\boldsymbol{y}_i-\boldsymbol{\mu})^{\mathsf T}$. As in one dimension,

$$
S_0=S+n(\bar{\boldsymbol{y}}-\boldsymbol{\mu})(\bar{\boldsymbol{y}}-\boldsymbol{\mu})^{\mathsf T},\qquad S=\sum_{i=1}^n(\boldsymbol{y}_i-\bar{\boldsymbol{y}})(\boldsymbol{y}_i-\bar{\boldsymbol{y}})^{\mathsf T},
$$
with the sum-of-squares matrix $S$ (the **sample covariance matrix** times $n-1$).

The two simpler cases are the multivariate versions of [3.7.2](/3.7.2):

- *Known $\Sigma$.* The prior $\boldsymbol{\mu}\sim\mathcal{N}_d(\boldsymbol{\mu}_0,\Lambda_0)$ is conjugate, and $\boldsymbol{\mu}\mid\boldsymbol{y}\sim\mathcal{N}_d(\boldsymbol{\mu}_n,\Lambda_n)$ with $\Lambda_n^{-1}=\Lambda_0^{-1}+n\Sigma^{-1}$ and $\boldsymbol{\mu}_n=\Lambda_n(\Lambda_0^{-1}\boldsymbol{\mu}_0+n\Sigma^{-1}\bar{\boldsymbol{y}})$: precision matrices add, and the posterior mean is a precision-weighted average.
- *Known $\boldsymbol{\mu}$.* The likelihood $(\det\Sigma)^{-n/2}\exp(-\frac12\operatorname{tr}(\Sigma^{-1}S_0))$ is, as a function of $\Sigma$, the kernel of the inverse-Wishart distribution defined below, the matrix analogue of the scaled inverse-$\chi^2$.

### 3.6.2. Wishart, Inverse-Wishart and Multivariate t-Distributions

Recall the **Wishart distribution** of [3.4.3](/3.4.3): if $\boldsymbol{z}_1,\dots,\boldsymbol{z}_\nu\overset{\text{iid}}{\sim}\mathcal{N}_d(\boldsymbol{0},\Lambda)$, then $W=\sum_{i=1}^\nu\boldsymbol{z}_i\boldsymbol{z}_i^{\mathsf T}\sim W_d(\nu,\Lambda)$, with mean $\nu\Lambda$. It is the multivariate analogue of a scaled $\chi^2$: for $d=1$, $\sum_iz_i^2\sim\tau^2\chi^2_\nu$ when $z_i\sim\mathcal{N}(0,\tau^2)$.

**Definition 3.6.1 (Inverse-Wishart Distribution)** Let $\nu>d-1$ and let $\Psi$ be a symmetric positive definite $d\times d$ matrix. A random symmetric positive definite matrix $\Sigma$ has the **inverse-Wishart distribution** $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ with $\nu$ degrees of freedom and scale matrix $\Psi$ if $\Sigma^{-1}\sim W_d(\nu,\Psi^{-1})$. Its density is

$$
p(\Sigma)=\frac{(\det\Psi)^{\nu/2}}{2^{\nu d/2}\,\Gamma_d(\nu/2)}\,(\det\Sigma)^{-(\nu+d+1)/2}\exp\Big(-\frac12\operatorname{tr}(\Psi\Sigma^{-1})\Big),
$$
where $\Gamma_d(a)=\pi^{d(d-1)/4}\prod_{i=1}^d\Gamma\big(a+\frac{1-i}{2}\big)$ is the multivariate gamma function. Its mean is $\mathbb{E}\Sigma=\Psi/(\nu-d-1)$ for $\nu>d+1$.

For $d=1$, $\mathrm{Inv}\text{-}W_1(\nu,\psi)=\mathrm{Inv}\text{-}\Gamma(\nu/2,\psi/2)=\mathrm{Inv}\text{-}\chi^2(\nu,\psi/\nu)$: the inverse-Wishart is the multivariate scaled inverse-$\chi^2$, with $\Psi$ playing the role of the prior sum of squares $\nu\sigma_0^2$.

The parametrization deserves care, because two conventions are in use for the same density. Gelman et al. write $\Sigma\sim\mathrm{Inv}\text{-}\mathrm{Wishart}_\nu(\Psi^{-1})$, putting in the argument the inverse of the scale matrix, that is, the scale matrix of the Wishart distribution of $\Sigma^{-1}$: in their notation, $\Sigma\sim\mathrm{Wishart}_\nu(\Lambda)$ implies $\Sigma^{-1}\sim\mathrm{Inv}\text{-}\mathrm{Wishart}_\nu(\Lambda)$. Software such as scipy (`invwishart(df=nu, scale=Psi)`) and most of the literature put the scale matrix $\Psi$ itself in the argument, so that $\mathbb{E}\Sigma$ is proportional to the argument. We use the scale-matrix form $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ throughout; to translate, $\mathrm{Inv}\text{-}\mathrm{Wishart}_\nu(\Psi^{-1})$ of Gelman et al. is our $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$. The table in [3.7.4](/3.7.4) lists both.

**Definition 3.6.2 (Multivariate t-Distribution)** Let $\nu>0$, $\boldsymbol{\mu}\in\mathbb{R}^d$ and $\Sigma$ symmetric positive definite. The **multivariate t-distribution** $t_\nu(\boldsymbol{\mu},\Sigma)$ has density

$$
p(\boldsymbol{\theta})=\frac{\Gamma(\frac{\nu+d}{2})}{\Gamma(\frac\nu2)\,(\nu\pi)^{d/2}}(\det\Sigma)^{-1/2}\Big(1+\frac1\nu(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\Big)^{-(\nu+d)/2},\qquad\boldsymbol{\theta}\in\mathbb{R}^d.
$$

Equivalently, $\boldsymbol{\theta}=\boldsymbol{\mu}+\boldsymbol{z}/\sqrt{u/\nu}$ with $\boldsymbol{z}\sim\mathcal{N}_d(\boldsymbol{0},\Sigma)$ independent of $u\sim\chi^2_\nu$. Its mean is $\boldsymbol{\mu}$ ($\nu>1$) and its covariance matrix $\frac{\nu}{\nu-2}\Sigma$ ($\nu>2$); for $d=1$ it is $t_\nu(\mu,\sigma^2)$ of Remark 3.3.1. The quadratic form satisfies $\frac1d(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\sim F_{d,\nu}$, so its level sets give elliptical credible regions.

### 3.6.3. The Normal-Inverse-Wishart Conjugate Prior

**Definition 3.6.3 (Normal-Inverse-Wishart Distribution)** Let $\boldsymbol{\mu}_0\in\mathbb{R}^d$, $\kappa_0>0$, $\nu_0>d-1$ and $\Lambda_0$ symmetric positive definite. The pair $(\boldsymbol{\mu},\Sigma)$ has the **normal-inverse-Wishart distribution** $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\Lambda_0/\kappa_0;\nu_0,\Lambda_0)$ if

$$
\Sigma\sim\mathrm{Inv}\text{-}W_d(\nu_0,\Lambda_0),\qquad\boldsymbol{\mu}\mid\Sigma\sim\mathcal{N}_d(\boldsymbol{\mu}_0,\Sigma/\kappa_0),
$$
with joint density

$$
p(\boldsymbol{\mu},\Sigma)\propto(\det\Sigma)^{-((\nu_0+d)/2+1)}\exp\Big(-\frac12\operatorname{tr}(\Lambda_0\Sigma^{-1})-\frac{\kappa_0}{2}(\boldsymbol{\mu}-\boldsymbol{\mu}_0)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}-\boldsymbol{\mu}_0)\Big).
$$

The exponent of $\det\Sigma$ collects $-(\nu_0+d+1)/2$ from the inverse-Wishart density and $-1/2$ from the normal density of $\boldsymbol{\mu}$.

**Theorem 3.6.1** Let $\boldsymbol{y}_1,\dots,\boldsymbol{y}_n\mid\boldsymbol{\mu},\Sigma\overset{\text{iid}}{\sim}\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ and $(\boldsymbol{\mu},\Sigma)\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\Lambda_0/\kappa_0;\nu_0,\Lambda_0)$. Then $(\boldsymbol{\mu},\Sigma)\mid\boldsymbol{y}\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_n,\Lambda_n/\kappa_n;\nu_n,\Lambda_n)$ with

$$
\begin{aligned}
\boldsymbol{\mu}_n&=\frac{\kappa_0}{\kappa_0+n}\boldsymbol{\mu}_0+\frac{n}{\kappa_0+n}\bar{\boldsymbol{y}},\qquad\kappa_n=\kappa_0+n,\qquad\nu_n=\nu_0+n,\\
\Lambda_n&=\Lambda_0+S+\frac{\kappa_0n}{\kappa_0+n}(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)^{\mathsf T}.
\end{aligned}
$$
In particular

$$
\boldsymbol{\mu}\mid\Sigma,\boldsymbol{y}\sim\mathcal{N}_d\Big(\boldsymbol{\mu}_n,\frac{\Sigma}{\kappa_n}\Big),\qquad\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}W_d(\nu_n,\Lambda_n),\qquad\boldsymbol{\mu}\mid\boldsymbol{y}\sim t_{\nu_n-d+1}\Big(\boldsymbol{\mu}_n,\frac{\Lambda_n}{\kappa_n(\nu_n-d+1)}\Big),
$$
and the posterior predictive distribution of a new observation is $\tilde{\boldsymbol{y}}\mid\boldsymbol{y}\sim t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\frac{(\kappa_n+1)\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$.

**Proof** Write every quadratic form as a trace. The product of prior and likelihood is

$$
(\det\Sigma)^{-((\nu_0+n+d)/2+1)}\exp\Big(-\frac12\operatorname{tr}\Big(\big[\Lambda_0+S+\kappa_0(\boldsymbol{\mu}-\boldsymbol{\mu}_0)(\boldsymbol{\mu}-\boldsymbol{\mu}_0)^{\mathsf T}+n(\bar{\boldsymbol{y}}-\boldsymbol{\mu})(\bar{\boldsymbol{y}}-\boldsymbol{\mu})^{\mathsf T}\big]\Sigma^{-1}\Big)\Big).
$$
The scalar identity in the proof of Theorem 3.4.1 holds verbatim for outer products:

$$
\kappa_0(\boldsymbol{\mu}-\boldsymbol{\mu}_0)(\boldsymbol{\mu}-\boldsymbol{\mu}_0)^{\mathsf T}+n(\bar{\boldsymbol{y}}-\boldsymbol{\mu})(\bar{\boldsymbol{y}}-\boldsymbol{\mu})^{\mathsf T}=\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}+\frac{\kappa_0n}{\kappa_n}(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)^{\mathsf T},
$$
so the bracket is $\Lambda_n+\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}$ and the product has the form of Definition 3.6.3 with the stated parameters. For the marginal of $\boldsymbol{\mu}$, integrate $\Sigma$ out using the normalizing constant of the inverse-Wishart density: $\int(\det\Sigma)^{-(\nu+d+1)/2}\exp(-\frac12\operatorname{tr}(A\Sigma^{-1}))\,\mathrm{d}\Sigma\propto(\det A)^{-\nu/2}$, here with $\nu=\nu_n+1$ and $A=\Lambda_n+\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}$. By the matrix determinant lemma $\det A=\det\Lambda_n\,\big(1+\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}\Lambda_n^{-1}(\boldsymbol{\mu}-\boldsymbol{\mu}_n)\big)$, so

$$
p(\boldsymbol{\mu}\mid\boldsymbol{y})\propto\big(1+\kappa_n(\boldsymbol{\mu}-\boldsymbol{\mu}_n)^{\mathsf T}\Lambda_n^{-1}(\boldsymbol{\mu}-\boldsymbol{\mu}_n)\big)^{-(\nu_n+1)/2}.
$$
Matching with Definition 3.6.2, $\nu+d=\nu_n+1$ gives $\nu=\nu_n-d+1$, and $\frac1\nu\Sigma^{-1}=\kappa_n\Lambda_n^{-1}$ gives the scale matrix $\Lambda_n/(\kappa_n(\nu_n-d+1))$. The predictive distribution follows in the same way from $\tilde{\boldsymbol{y}}\mid\Sigma,\boldsymbol{y}\sim\mathcal{N}_d\big(\boldsymbol{\mu}_n,(1+\frac1{\kappa_n})\Sigma\big)$. $\square$

The one-dimensional and the $d$-dimensional conjugate analyses correspond term by term:

| | Univariate normal (§3.4) | Multivariate normal |
|---|---|---|
| prior | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\Lambda_0/\kappa_0;\nu_0,\Lambda_0)$ |
| prior mean | $\mu_0$ | $\boldsymbol{\mu}_0$ |
| prior variance information | prior sample variance $\sigma_0^2$ | prior sum-of-squares matrix $\Lambda_0$ |
| prior data for the mean | $\kappa_0$ | $\kappa_0$ |
| prior data for the variance | $\nu_0$ | $\nu_0$ |
| posterior mean | $\mu_n=\frac{\kappa_0\mu_0+n\bar y}{\kappa_0+n}$ | $\boldsymbol{\mu}_n=\frac{\kappa_0\boldsymbol{\mu}_0+n\bar{\boldsymbol{y}}}{\kappa_0+n}$ |
| posterior variance information | $\nu_n\sigma_n^2=\nu_0\sigma_0^2+(n-1)s^2+\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2$ | $\Lambda_n=\Lambda_0+S+\frac{\kappa_0n}{\kappa_n}(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)(\bar{\boldsymbol{y}}-\boldsymbol{\mu}_0)^{\mathsf T}$ |
| marginal posterior of the mean | $t_{\nu_n}(\mu_n,\sigma_n^2/\kappa_n)$ | $t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\Lambda_n/(\kappa_n(\nu_n-d+1))\big)$ |

For $d=1$, $\Lambda_0=\nu_0\sigma_0^2$ and $\Lambda_n=\nu_n\sigma_n^2$, and the right column reduces to the left one.

### 3.6.4. The Non-informative Prior

As in one dimension, take the limit $\kappa_0\to0$, $\nu_0\to-1$, $\det\Lambda_0\to0$ of the conjugate density, which gives

$$
p(\boldsymbol{\mu},\Sigma)\propto(\det\Sigma)^{-(d+1)/2}.
$$
This is the multivariate version of $\sigma^{-2}$: flat in $\boldsymbol{\mu}$, and for $\Sigma$ the Jeffreys' prior of the covariance matrix of a normal distribution with known mean, combined under prior independence of location and scale. The posterior parameters become $\boldsymbol{\mu}_n=\bar{\boldsymbol{y}}$, $\kappa_n=n$, $\nu_n=n-1$, $\Lambda_n=S$, so that for $n>d$

$$
\boldsymbol{\mu}\mid\Sigma,\boldsymbol{y}\sim\mathcal{N}_d\Big(\bar{\boldsymbol{y}},\frac{\Sigma}{n}\Big),\qquad\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}W_d(n-1,S),\qquad\boldsymbol{\mu}\mid\boldsymbol{y}\sim t_{n-d}\Big(\bar{\boldsymbol{y}},\frac{S}{n(n-d)}\Big).
$$
In the notation of Gelman et al. the second statement reads $\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}\mathrm{Wishart}_{n-1}(S^{-1})$. The connection with frequentist inference is again exact. By the $F$ property of Definition 3.6.2, with the sample covariance matrix $S/(n-1)$,

$$
n(\boldsymbol{\mu}-\bar{\boldsymbol{y}})^{\mathsf T}\Big(\frac{S}{n-1}\Big)^{-1}(\boldsymbol{\mu}-\bar{\boldsymbol{y}})\;\Big|\;\boldsymbol{y}\sim\frac{(n-1)d}{n-d}F_{d,n-d},
$$
which is the distribution of Hotelling's $T^2$ statistic ([3.4.3](/3.4.3)); the posterior credible ellipsoids for $\boldsymbol{\mu}$ coincide with the classical confidence ellipsoids.

## Summary

| Model | Prior | Posterior | Marginal posterior of the mean | Posterior predictive |
|---|---|---|---|---|
| $\mathrm{Mult}(n,\boldsymbol{\theta})$ | $\mathrm{Dir}(\boldsymbol{\alpha})$ (Definition 3.2.1) | $\mathrm{Dir}(\boldsymbol{\alpha}+\boldsymbol{y})$ | $\theta_j\mid\boldsymbol{y}\sim\mathrm{Beta}(\alpha_j+y_j,\alpha_0-\alpha_j+n-y_j)$ (Proposition 3.2.1) | $\mathbb{P}(\tilde y=j\mid\boldsymbol{y})=\frac{\alpha_j+y_j}{\alpha_0+n}$ |
| $\mathcal{N}(\mu,\sigma^2)$ | $\sigma^{-2}$ | $\mu\mid\sigma^2,y\sim\mathcal{N}(\bar y,\frac{\sigma^2}{n})$, $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$ | $t_{n-1}(\bar y,\frac{s^2}{n})$ (Proposition 3.3.1) | $t_{n-1}\big(\bar y,(1+\frac1n)s^2\big)$ |
| $\mathcal{N}(\mu,\sigma^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\frac{\sigma_0^2}{\kappa_0};\nu_0,\sigma_0^2)$ (Definition 3.4.1) | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_n,\frac{\sigma_n^2}{\kappa_n};\nu_n,\sigma_n^2)$ (Theorem 3.4.1) | $t_{\nu_n}(\mu_n,\frac{\sigma_n^2}{\kappa_n})$ | $t_{\nu_n}\big(\mu_n,\frac{\kappa_n+1}{\kappa_n}\sigma_n^2\big)$ |
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\frac{\Lambda_0}{\kappa_0};\nu_0,\Lambda_0)$ (Definition 3.6.3) | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_n,\frac{\Lambda_n}{\kappa_n};\nu_n,\Lambda_n)$ (Theorem 3.6.1) | $t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\frac{\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$ | $t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\frac{(\kappa_n+1)\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$ |
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $(\det\Sigma)^{-(d+1)/2}$ | $\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}W_d(n-1,S)$ | $t_{n-d}\big(\bar{\boldsymbol{y}},\frac{S}{n(n-d)}\big)$ | |

- Nuisance parameters are integrated out: $p(\theta_1\mid y)=\int p(\theta_1\mid\theta_2,y)\,p(\theta_2\mid y)\,\mathrm{d}\theta_2$, a mixture of conditional posteriors; simulation draws $\theta_2$ first and then $\theta_1\mid\theta_2$ (§3.1).
- Conjugate hyperparameters are prior data: Dirichlet prior counts; $\kappa_0$ and $\nu_0$ prior observations for the mean and the variance; the posterior sum of squares includes a prior–data conflict term $\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2$.
- Non-informative priors are limits of conjugate ones ($\kappa_0\to0$, $\nu_0\to-1$, $\sigma_0^2\to0$ or $\Lambda_0\to0$) and reproduce the classical pivotal results: $t$ intervals, $\chi^2$ intervals for the variance, Hotelling's $T^2$ ellipsoids.
- The **marginal likelihood** of the normal model with a proper conjugate prior has the closed form of Proposition 3.4.1; it does not exist under improper priors.
- The Behrens–Fisher problem has a direct Bayesian solution: independent posteriors for the two groups and simulation of $\delta=\mu_1-\mu_2$ (§3.5).
- Inverse-Wishart parametrization: $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ here and in scipy is $\mathrm{Inv}\text{-}\mathrm{Wishart}_\nu(\Psi^{-1})$ in Gelman et al.; the mean is $\Psi/(\nu-d-1)$.

## Questions

1. Under the prior $p(\mu,\sigma^2)\propto\sigma^{-2}$, derive the posterior predictive distribution $\tilde y\mid y\sim t_{n-1}\big(\bar y,(1+\frac1n)s^2\big)$ and compute the $95\%$ predictive interval for the next piece of cheese in Example 3.4.1 (Ann). Compare it with the interval for $\mu$.

   **Answer** Given $\sigma^2$ and $y$, $\tilde y=\mu+\varepsilon$ with $\mu\mid\sigma^2,y\sim\mathcal{N}(\bar y,\sigma^2/n)$ and independent $\varepsilon\sim\mathcal{N}(0,\sigma^2)$, so $\tilde y\mid\sigma^2,y\sim\mathcal{N}(\bar y,(1+\frac1n)\sigma^2)$. With $c=1+\frac1n$, integrating against $p(\sigma^2\mid y)\propto(\sigma^2)^{-(n+1)/2}\exp(-\frac{(n-1)s^2}{2\sigma^2})$ gives $p(\tilde y\mid y)\propto\int(\sigma^2)^{-(n+2)/2}\exp\big(-\frac{1}{2\sigma^2}[(n-1)s^2+(\tilde y-\bar y)^2/c]\big)\,\mathrm{d}\sigma^2\propto\big[1+\frac{(\tilde y-\bar y)^2}{(n-1)cs^2}\big]^{-n/2}$, the $t_{n-1}(\bar y,cs^2)$ kernel. For the cheese data, $\sqrt{(1+\frac1{25})\times3.984}=2.036$ and $t_{24,0.025}=2.064$, so the interval is $42.208\pm4.20=[38.01,46.41]$. It is about five times wider than the interval $[41.38,43.03]$ for $\mu$, because it contains the variation of individual pieces, which does not decrease with $n$.
2. Bob in Example 3.4.1 changes his mind and gives his prior mean the weight of $\kappa_0=25$ observations, keeping $\mu_0=40$, $\nu_0=1$ and $\sigma_0^2=4.094$. Compute the posterior of $\mu$ and its $95\%$ interval. Explain why the posterior of $\sigma^2$ changes as well.

   **Answer** Now $\kappa_n=50$, $\mu_n=\frac{25\times40+25\times42.208}{50}=41.104$, $\nu_n=26$, and $\nu_n\sigma_n^2=4.094+95.618+\frac{25\times25}{50}(2.208)^2=160.65$, so $\sigma_n^2=6.179$ and $\mu\mid y\sim t_{26}(41.104,\,0.3515^2)$. The $95\%$ interval is $41.104\pm2.056\times0.3515=[40.38,41.83]$, which excludes the sample mean $42.208$. The posterior of $\sigma^2$ moves up because the conflict term $\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2$ grows from $4.69$ to $60.94$: in this model a strong prior on $\mu$ that disagrees with the data is explained partly by a larger sampling variance, since the prior variance of $\mu$ is $\sigma^2/\kappa_0$.
3. Prove the aggregation property of the Dirichlet posterior in Example 3.2.1 directly: show that the posterior of $\theta_1+\theta_2$ (thirst or polyuria) is the same whether we merge the two categories before or after the analysis, and give it.

   **Answer** After the analysis: $\boldsymbol{\theta}\mid\boldsymbol{y}\sim\mathrm{Dir}(11,9,16,14)$, and by Proposition 3.2.1 $(\theta_1+\theta_2,\theta_3,\theta_4)\mid\boldsymbol{y}\sim\mathrm{Dir}(20,16,14)$, so $\theta_1+\theta_2\mid\boldsymbol{y}\sim\mathrm{Beta}(20,30)$. Before: the merged counts are $(18,15,13)$ and the merged prior is $\mathrm{Dir}(2,1,1)$ (again by Proposition 3.2.1 applied to $\mathrm{Dir}(1,1,1,1)$); the posterior is $\mathrm{Dir}(20,16,14)$, the same. Note that the merged prior is not uniform on the coarser simplex: merging $k$ uniform categories gives a prior that favors the merged one. The posterior mean of $\theta_1+\theta_2$ is $0.40$.
4. Let $\theta\mid V\sim\mathcal{N}(\mu,V)$ with $V\sim\mathrm{Inv}\text{-}\chi^2(\nu,\sigma^2)$. Show that $\theta\sim t_\nu(\mu,\sigma^2)$. Which results of this chapter are instances of this fact?

   **Answer** $p(\theta)\propto\int V^{-1/2}\exp\big(-\frac{(\theta-\mu)^2}{2V}\big)V^{-(\nu/2+1)}\exp\big(-\frac{\nu\sigma^2}{2V}\big)\,\mathrm{d}V=\int V^{-((\nu+1)/2+1)}\exp\big(-\frac{A}{2V}\big)\,\mathrm{d}V$ with $A=\nu\sigma^2+(\theta-\mu)^2$. The integrand is an unnormalized $\mathrm{Inv}\text{-}\Gamma(\frac{\nu+1}2,\frac A2)$ density, whose integral is proportional to $A^{-(\nu+1)/2}\propto\big(1+\frac{(\theta-\mu)^2}{\nu\sigma^2}\big)^{-(\nu+1)/2}$, the $t_\nu(\mu,\sigma^2)$ kernel. The marginal posteriors $\mu\mid y$ of Proposition 3.3.1 and §3.4.3 ($V=\sigma^2/\kappa_n$, which is $\mathrm{Inv}\text{-}\chi^2(\nu_n,\sigma_n^2/\kappa_n)$) and the posterior predictive distributions of §3.3.3 and §3.4.5 are all of this form: a normal whose variance is proportional to $\sigma^2$, averaged over the scaled inverse-$\chi^2$ posterior of $\sigma^2$.
5. Two groups have equal but unknown variance: $y_{ji}\mid\mu_1,\mu_2,\sigma^2\sim\mathcal{N}(\mu_j,\sigma^2)$, with prior $p(\mu_1,\mu_2,\sigma^2)\propto\sigma^{-2}$. Find the posterior of $\delta=\mu_1-\mu_2$ and compare it with the classical pooled $t$ interval. Why is the unequal-variance case harder for frequentist methods but not for Bayesian ones?

   **Answer** Given $\sigma^2$, $\mu_1$ and $\mu_2$ are independent $\mathcal{N}(\bar y_j,\sigma^2/n_j)$, so $\delta\mid\sigma^2,y\sim\mathcal{N}\big(\bar y_1-\bar y_2,\sigma^2(\frac1{n_1}+\frac1{n_2})\big)$. Integrating $\mu_1,\mu_2$ out of the joint posterior gives $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n_1+n_2-2,s_p^2)$ with the pooled variance $s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$, and by Question 4, $\delta\mid y\sim t_{n_1+n_2-2}\big(\bar y_1-\bar y_2,s_p^2(\frac1{n_1}+\frac1{n_2})\big)$. Its central intervals are the pooled $t$ confidence intervals. With unequal variances the frequentist needs a statistic whose sampling distribution does not depend on $\sigma_1^2/\sigma_2^2$, and none exists; the Bayesian integrates over both variances, which is always possible, and only the computation (simulation instead of a $t$ table) changes.
6. Show that the normal-inverse-Wishart analysis with $d=1$ reduces to the normal-inverse-chi-square analysis: identify $\Lambda_0$ and $\Lambda_n$, and check the degrees of freedom and the scale of the marginal $t$ posterior of the mean.

   **Answer** For $d=1$, $\mathrm{Inv}\text{-}W_1(\nu_0,\Lambda_0)=\mathrm{Inv}\text{-}\chi^2(\nu_0,\Lambda_0/\nu_0)$, so $\Lambda_0=\nu_0\sigma_0^2$; the posterior formula gives $\Lambda_n=\nu_0\sigma_0^2+(n-1)s^2+\frac{\kappa_0n}{\kappa_n}(\bar y-\mu_0)^2=\nu_n\sigma_n^2$, and $S=(n-1)s^2$. The marginal posterior $t_{\nu_n-d+1}\big(\mu_n,\frac{\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$ becomes $t_{\nu_n}\big(\mu_n,\frac{\nu_n\sigma_n^2}{\kappa_n\nu_n}\big)=t_{\nu_n}(\mu_n,\sigma_n^2/\kappa_n)$, as in §3.4.3. The density exponent $-((\nu_0+d)/2+1)$ becomes $-((\nu_0+1)/2+1)$, which is $\sigma^{-1}(\sigma^2)^{-(\nu_0/2+1)}$.
7. Ann wants to compare her normal model of Example 3.4.1 with a competing model by a Bayes factor. Why can she not use the marginal likelihood of her model, and what happens to Bob's marginal likelihood as he lets $\kappa_0\to0$?

   **Answer** Under the improper prior $p(\mu,\sigma^2)\propto\sigma^{-2}$ the prior density is defined only up to an arbitrary constant $c$, and $p(y)=\iint p(y\mid\mu,\sigma^2)\,c\,\sigma^{-2}\,\mathrm{d}\mu\,\mathrm{d}\sigma^2$ inherits that constant, so ratios of marginal likelihoods are arbitrary. In Proposition 3.4.1 the factor $\sqrt{\kappa_0/\kappa_n}$ tends to $0$ as $\kappa_0\to0$, while the posterior hardly changes: a model with an ever vaguer prior on $\mu$ spreads its prior predictive density over ever more data sets and is increasingly penalized. Bayes factors are therefore sensitive to the vagueness of priors that hardly affect the posterior, a theme of [3.7.8](/3.7.8).
8. In the multinomial model with the prior $\mathrm{Dir}(0,\dots,0)$, show that the posterior is proper if and only if every category has been observed at least once.

   **Answer** The posterior is proportional to $\prod_j\theta_j^{y_j-1}$ on the simplex. If all $y_j\ge1$, this is the kernel of $\mathrm{Dir}(\boldsymbol{y})$, which is proper. Suppose $y_1=0$. Parametrize the simplex by $\theta_1$ and $\theta_j=(1-\theta_1)\phi_j$ for $j\ge2$, with $(\phi_2,\dots,\phi_k)$ in the simplex $\Delta_{k-1}$; the Jacobian is $(1-\theta_1)^{k-2}$. The integral of the kernel becomes

   $$
   \int_0^1\theta_1^{-1}(1-\theta_1)^{\sum_{j\ge2}(y_j-1)+k-2}\,\mathrm{d}\theta_1\cdot\int_{\Delta_{k-1}}\prod_{j\ge2}\phi_j^{y_j-1}\,\mathrm{d}\boldsymbol{\phi}=\int_0^1\theta_1^{-1}(1-\theta_1)^{n-1}\,\mathrm{d}\theta_1\cdot\int_{\Delta_{k-1}}\prod_{j\ge2}\phi_j^{y_j-1}\,\mathrm{d}\boldsymbol{\phi},
   $$
   and the first factor diverges at $\theta_1=0$ while the second is positive (possibly infinite). So the posterior is improper. This is the multinomial version of the improper $\mathrm{Beta}(0,0)$ posterior when $y=0$ ([3.7.2](/3.7.2)).
