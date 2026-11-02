---
title: Hierarchical Models
description: Why parameters of related groups should be modeled together; the rat tumor example and the problems of a prior fixed from historical data; no, complete and partial pooling; exchangeability and de Finetti's theorem; the structure of fully Bayesian hierarchical models, hyperpriors and the three-step analysis of conjugate hierarchical models; the beta-binomial model for rat tumors with the choice of hyperprior, grid computation and shrinkage; the normal hierarchical model for the eight schools, the posterior of the between-group standard deviation, and predictions for existing and new groups.
---

Data often come in groups: tumor counts from many laboratory experiments, test score gains in several schools, outcomes in many hospitals. Each group has its own parameter $\theta_j$, and the groups are related, so that what we learn about one tells us something about the others. Treating the $\theta_j$ as unrelated wastes this information, and with little data per group the separate estimates are noisy; treating them as equal ignores real differences. A hierarchical model takes the middle course: the $\theta_j$ are themselves drawn from a population distribution whose parameters, the hyperparameters, are estimated from all groups together. The introductory account in [3.2.7](/3.2.7) defines the **hierarchical model**; this chapter develops it in full.

We start from an example in which a prior is constructed from historical data (§6.1) and see why a full model is better (§6.2). The probabilistic justification for modeling group parameters as draws from a common distribution is exchangeability and de Finetti's theorem (§6.3). The general structure and a three-step method for conjugate hierarchical models (§6.4) are then applied to the two standard examples, binomial data with a beta population distribution (§6.5) and normal data with a normal population distribution (§6.6). The computations combine the conjugate results of [3.7.1](/3.7.1)–[3.7.3](/3.7.3) with the grid sampling of [3.7.5](/3.7.5); the empirical Bayes argument of [3.7.5](/3.7.5) §5.6 is the non-Bayesian shortcut that the fully Bayesian analysis replaces. The model checks applied to these examples follow in [3.7.7](/3.7.7) and their comparison in [3.7.8](/3.7.8). In experimental design, the same structure appears as the random-effects model ([3.8.5](/3.8.5)).

## 6.1. Motivation: Tumor Risk in a Group of Rats

**Example 6.1.1 (Rat Tumors)** In a laboratory experiment on the carcinogenicity of a drug, a control group of $n=14$ rats, which received no drug, developed $y=4$ tumors of a certain type. We want to estimate the risk $\theta$ of such a tumor in this type of rat. Data from 70 earlier experiments with control groups of the same type of rat are also available (Tarone, 1982):

| $y_j/n_j$ | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| 0/20 | 0/20 | 0/20 | 0/20 | 0/20 | 0/20 | 0/20 | 0/19 | 0/19 | 0/19 |
| 0/19 | 0/18 | 0/18 | 0/17 | 1/20 | 1/20 | 1/20 | 1/20 | 1/19 | 1/19 |
| 1/18 | 1/18 | 2/25 | 2/24 | 2/23 | 2/20 | 2/20 | 2/20 | 2/20 | 2/20 |
| 2/20 | 1/10 | 5/49 | 2/19 | 5/46 | 3/27 | 2/17 | 7/49 | 7/47 | 3/20 |
| 3/20 | 2/13 | 9/48 | 10/50 | 4/20 | 4/20 | 4/20 | 4/20 | 4/20 | 4/20 |
| 4/20 | 10/48 | 4/19 | 4/19 | 4/19 | 5/22 | 11/46 | 12/49 | 5/20 | 5/20 |
| 6/23 | 5/19 | 6/22 | 6/20 | 6/20 | 6/20 | 16/52 | 15/47 | 15/46 | 9/24 |

Model the current experiment as $y\mid\theta\sim\mathrm{Bin}(14,\theta)$. With a $\mathrm{Beta}(\alpha,\beta)$ prior the posterior is $\mathrm{Beta}(\alpha+4,\beta+10)$ ([3.7.1](/3.7.1), §1.6.2); the question is how to choose $\alpha$ and $\beta$, the **hyperparameters** that control the shape of the prior.

A first thought is to let the historical data determine them. Assume that the tumor probabilities $\theta_1,\dots,\theta_{70}$ of the earlier experiments, and $\theta_{71}=\theta$ of the current one, are draws from a common population distribution $\mathrm{Beta}(\alpha,\beta)$. The observed rates $y_j/n_j$, $j=1,\dots,70$, have mean $0.136$ and standard deviation $0.103$. Matching these to the mean and variance of the beta distribution,

$$
\frac{\alpha}{\alpha+\beta}=0.136,\qquad\alpha+\beta=\frac{\mathbb{E}\theta\,(1-\mathbb{E}\theta)}{\operatorname{Var}\theta}-1=\frac{0.136\times0.864}{0.103^2}-1\approx10,
$$
gives $\alpha\approx1.4$, $\beta\approx8.6$. The posterior for the current experiment is then $\mathrm{Beta}(5.4,18.6)$, with mean $0.223$ and standard deviation $0.083$, well below the raw rate $4/14=0.286$.

This is an **empirical Bayes** analysis ([3.7.5](/3.7.5), Definition 5.6.3), and it is sensible, but it has defects.

- It is not a Bayesian calculation, because it is not based on a full probability model for all the data. The point estimates of $\alpha$ and $\beta$ are somewhat arbitrary and ignore their uncertainty: with 70 experiments of about 20 rats each, $\alpha$ and $\beta$ are far from known exactly.
- If the estimated prior were used for inference about the first 70 experiments themselves, the data would be used twice, once to form the prior and once in the likelihood.
- The moment estimate also confuses two sources of variation. The variance of $y_j/n_j$ is the variance of $\theta_j$ plus the binomial variance $\theta_j(1-\theta_j)/n_j$, so the observed spread overstates the spread of the $\theta_j$, and $\alpha+\beta$ is underestimated.

The fully Bayesian approach treats the hyperparameters as unknowns like all others and gives them a prior distribution $p(\alpha,\beta)$. The joint prior of all parameters is

$$
p(\alpha,\beta,\theta_1,\dots,\theta_{71})=p(\alpha,\beta)\,p(\theta_1,\dots,\theta_{71}\mid\alpha,\beta),
$$
and the joint posterior is

$$
p(\alpha,\beta,\theta_1,\dots,\theta_{71}\mid y)\propto p(\alpha,\beta,\theta_1,\dots,\theta_{71})\,p(y_1,\dots,y_{71}\mid\theta_1,\dots,\theta_{71},\alpha,\beta)=p(\alpha,\beta,\theta_1,\dots,\theta_{71})\,p(y_1,\dots,y_{71}\mid\theta_1,\dots,\theta_{71}),
$$
since the data depend on the hyperparameters only through the $\theta_j$. This is an ordinary multiparameter problem ([3.7.3](/3.7.3)) with $73$ parameters, which §6.5 solves.

## 6.2. Why Hierarchical Models

A hierarchical model describes a complex joint distribution by breaking it into simpler conditional pieces, each easy to understand, which together specify the joint distribution of all data and parameters. In a sense all the models so far were hierarchical with two levels, data given parameters and parameters given hyperparameters fixed in advance; the new step is to make the upper level uncertain as well. There may be further hierarchical structure within each piece.

The motivation is a trade-off familiar from model selection. Non-hierarchical models with few parameters, such as a single $\theta$ for all groups, generally do not fit grouped data well. Non-hierarchical models with many parameters, such as an unrelated $\theta_j$ for every group, fit the data well but predict poorly, the problem of overfitting. Hierarchical models fit the data with a small number of effective parameters and predict well. They can even have more parameters than data points and still give reasonable answers, because the population distribution restrains the group parameters. The three possibilities have names.

**Definition 6.2.1 (No, Complete and Partial Pooling)** For grouped data with group parameters $\theta_1,\dots,\theta_J$: **no pooling** estimates each $\theta_j$ from the data of group $j$ alone; **complete pooling** assumes $\theta_1=\dots=\theta_J$ and estimates the common value from all the data; **partial pooling** models the $\theta_j$ as draws from a common population distribution with unknown parameters, so that each estimate combines the data of its own group with information from the other groups.

No pooling and complete pooling are the limits of partial pooling as the population variance tends to infinity and to zero; the eight schools example (§6.6) shows the whole range.

## 6.3. Exchangeability

### 6.3.1. Definition

What justifies treating the $\theta_j$ as draws from a common distribution? If no information other than the data $y$ is available to distinguish any of the $\theta_j$ from any of the others, and no ordering or grouping of the parameters can be made, we must assume symmetry among the parameters in their prior distribution.

**Definition 6.3.1 (Exchangeability)** Random variables $\theta_1,\dots,\theta_J$ are **exchangeable** if their joint distribution is invariant under permutations of the indices: $p(\theta_1,\dots,\theta_J)=p(\theta_{\pi(1)},\dots,\theta_{\pi(J)})$ for every permutation $\pi$ of $(1,\dots,J)$. An infinite sequence is exchangeable if every finite subsequence is.

In the rat tumor example there is no prior reason to think that $\theta_{70}<\theta_{71}$ is more likely than $\theta_{70}>\theta_{71}$; with the information given, the order in which the experiments are listed is meaningless, and an exchangeable prior is reasonable. If there is information in the indices, exchangeability usually is not reasonable. Suppose different pure-bred strains of rats were used in experiments 50–71 than in experiments 1–49. Then exchanging indices 49 and 50 would change the meaning of the parameters, and a better model treats the parameters as exchangeable within strains, or includes the strain as a group-level covariate so that the parameters are exchangeable given it.

Exchangeability does not imply independence. The bivariate normal distribution

$$
\begin{bmatrix}\theta_1\\\theta_2\end{bmatrix}\sim\mathcal{N}_2\left(\begin{bmatrix}\mu\\\mu\end{bmatrix},\begin{bmatrix}\sigma^2&\rho\sigma^2\\\rho\sigma^2&\sigma^2\end{bmatrix}\right),\qquad\rho\ne0,
$$
is exchangeable, since swapping $\theta_1$ and $\theta_2$ leaves it unchanged, but it is obviously not independent. Exchangeability implies that all the marginal distributions are the same (the $\theta_j$ are identically distributed) and that the dependence between any two components is the same, but nothing about independence. Conversely, every independent identically distributed sequence is exchangeable.

### 6.3.2. De Finetti's Theorem

The simplest way to build an exchangeable distribution is to make the $\theta_j$ independent given an unknown parameter $\phi$, with $\phi$ itself random:

$$
p(\theta_1,\dots,\theta_J)=\int\Big[\prod_{j=1}^Jp(\theta_j\mid\phi)\Big]p(\phi)\,\mathrm{d}\phi.
$$
The integrand is symmetric in the indices, and so is the mixture. The remarkable fact is that, for infinite sequences, there is essentially no other way.

**Theorem 6.3.1 (de Finetti's Theorem)** Let $\theta_1,\theta_2,\dots$ be an infinite exchangeable sequence of random variables (suitably well behaved, for example real-valued). Then there is a random parameter $\phi$, in general a random probability distribution, such that given $\phi$ the $\theta_j$ are independent and identically distributed, and for every $J$

$$
p(\theta_1,\dots,\theta_J)=\int\prod_{j=1}^Jp(\theta_j\mid\phi)\,p(\phi)\,\mathrm{d}\phi.
$$

De Finetti proved the theorem for binary sequences (1931), and Hewitt and Savage (1955) extended it to general spaces; we do not give the proof. In words: in the limit $J\to\infty$, any suitably well-behaved exchangeable distribution on $(\theta_1,\dots,\theta_J)$ can be expressed as a mixture of independent and identical distributions. For a finite $J$ the representation holds approximately, and exactly if the $J$ variables can be regarded as part of a longer exchangeable sequence. This is the theoretical support for the hierarchical model: if we judge the group parameters exchangeable, we may as well model them as independent draws from a population distribution $p(\theta\mid\phi)$ with a prior $p(\phi)$ on its parameter. The conditional independence of the $\theta_j$ given $\phi$, which holds in the rat tumor model and in most hierarchical models, will also be useful for the **Gibbs sampler** ([3.5.9](/3.5.9)).

The finite and infinite cases do differ. A mixture of independent identically distributed variables always has $\operatorname{Cov}(\theta_1,\theta_2)=\operatorname{Var}\big(\mathbb{E}(\theta_1\mid\phi)\big)\ge0$, so the bivariate normal above with $\rho<0$ is exchangeable but not of this form; it cannot be extended to a long exchangeable sequence (Question 6).

### 6.3.3. Exchangeability Reflects Information, Not the World

Whether a set of parameters is exchangeable depends on what we know, not on the parameters themselves.

**Example 6.3.1** A researcher wants to know the proportions $\theta_1,\dots,\theta_6$ of people who regularly play a particular sport in six countries. What can be said about $\theta_6$ before any data are collected?

1. *No information distinguishes the countries.* The six rates must be modeled exchangeably. If the rates of five countries are then observed, they tell us about the population distribution and hence about $\theta_6$.
2. *We know which country is the sixth, and that the sport is far more popular there than anywhere else, while the five observed countries are the others.* Even before seeing the five observed rates, we cannot assign an exchangeable prior to the six rates. Once the five are observed, a reasonable posterior for $\theta_6$ should put most of its mass above all of them: $\mathbb{P}\big(\theta_6>\max(\theta_1,\dots,\theta_5)\mid\theta_1,\dots,\theta_5\big)$ should be large.
3. *We know the six countries, including that one of them is exceptional, but not which index belongs to which country.* The six rates are again exchangeable, since nothing distinguishes the indices. But the population distribution must now allow one value far from the others, for example a heavy-tailed distribution rather than a normal one.

The same parameters are exchangeable in situations 1 and 3 and not in situation 2; and exchangeability alone does not fix the form of the population distribution, which must also reflect what we know.

## 6.4. Fully Bayesian Hierarchical Models

### 6.4.1. Structure

A hierarchical model for $J$ groups with data $y_j$ (a vector of observations in group $j$) has three levels:

$$
y_j\mid\theta,\phi\sim p(y_j\mid\theta_j),\qquad\theta\mid\phi\sim p(\theta\mid\phi)=\prod_{j=1}^Jp(\theta_j\mid\phi),\qquad\phi\sim p(\phi).
$$
Here $\theta=(\theta_1,\dots,\theta_J)$, the distribution $p(\theta_j\mid\phi)$ is the population distribution, and

**Definition 6.4.1 (Hyperprior)** In a hierarchical model, the prior distribution $p(\phi)$ of the hyperparameters $\phi$ is the **hyperprior**.

The joint prior is $p(\theta,\phi)=p(\phi)p(\theta\mid\phi)$, and the joint posterior is

$$
p(\theta,\phi\mid y)\propto p(\phi)\,p(\theta\mid\phi)\,p(y\mid\theta,\phi)=p(\phi)\,p(\theta\mid\phi)\,p(y\mid\theta)=p(\phi)\prod_{j=1}^Jp(\theta_j\mid\phi)\prod_{j=1}^Jp(y_j\mid\theta_j).
$$
The quantities of interest are of two kinds.

- The posterior $p(\theta\mid y)=\int p(\theta,\phi\mid y)\,\mathrm{d}\phi$ of the group parameters, obtained through the joint posterior of $(\theta,\phi)$.
- **Posterior predictive distributions**, in two situations: (1) a future observation $\tilde y$ from an existing group $j$, whose distribution $p(\tilde y\mid\theta_j)$ is averaged over the posterior of $\theta_j$; (2) an observation $\tilde y$ from a new group, whose parameter $\tilde\theta$ is a new draw from the population distribution $p(\tilde\theta\mid\phi)$, averaged over the posterior of $\phi$.

The hyperprior is usually chosen to be weakly informative or non-informative, since the point of the model is to learn the population distribution from the groups. But as §6.5 and §6.6 show, an **improper prior** on hyperparameters easily produces an improper posterior, and the choice requires care.

### 6.4.2. Conjugate Hierarchical Models: Three Steps

When the population distribution is conjugate to the likelihood, the posterior can be analyzed in three steps.

1. Write the joint posterior $p(\theta,\phi\mid y)$ in unnormalized form, as the product of the hyperprior $p(\phi)$, the population distribution $p(\theta\mid\phi)$ and the likelihood $p(y\mid\theta)$.
2. Determine analytically the conditional posterior $p(\theta\mid\phi,y)$ of $\theta$ given the hyperparameters. For fixed observed $y$ it is a function of $\phi$; by conjugacy and conditional independence it is a product of standard distributions, one for each group.
3. Estimate $\phi$ in the Bayesian way, that is, obtain its marginal posterior $p(\phi\mid y)$.

The marginal posterior of step 3 can be found in two ways. By brute-force integration, $p(\phi\mid y)=\int p(\theta,\phi\mid y)\,\mathrm{d}\theta$, which is a high-dimensional integral and usually difficult. Or by the conditional probability formula

$$
p(\phi\mid y)=\frac{p(\theta,\phi\mid y)}{p(\theta\mid\phi,y)},
$$
valid for every $\theta$. In the second way the normalizing constant of $p(\theta\mid\phi,y)$ depends on $\phi$ and must be kept, which is where care is needed. Equivalently, $p(\phi\mid y)\propto p(\phi)p(y\mid\phi)$ with the **marginal likelihood**

$$
p(y\mid\phi)=\prod_{j=1}^J\int p(y_j\mid\theta_j)\,p(\theta_j\mid\phi)\,\mathrm{d}\theta_j,
$$
a product of the prior predictive densities of the groups, available in closed form for conjugate models. To draw from the joint posterior, reverse steps 3 and 2: draw $\phi^s$ from $p(\phi\mid y)$, usually on a grid ([3.7.5](/3.7.5), Algorithm 5.2.1), since $\phi$ is low-dimensional; then draw $\theta^s$ from the standard distribution $p(\theta\mid\phi^s,y)$; then, if needed, predictive values $\tilde y^s$. This is Proposition 5.1.2 of [3.7.5](/3.7.5) with $\phi$ in the role of $x$.

## 6.5. The Beta–Binomial Hierarchical Model: Rat Tumors

### 6.5.1. The Posterior

For the rat tumor data (Example 6.1.1) with $J=71$ experiments, the hierarchical model is

$$
y_j\mid\theta_j\sim\mathrm{Bin}(n_j,\theta_j),\qquad\theta_j\mid\alpha,\beta\overset{\text{iid}}{\sim}\mathrm{Beta}(\alpha,\beta),\qquad(\alpha,\beta)\sim p(\alpha,\beta),
$$
with the numbers of tumors $y_j$, the known sample sizes $n_j$, and the hyperparameters $(\alpha,\beta)$, whose hyperprior is still to be specified. Following the three steps:

1. The joint posterior is
   $$
   p(\theta,\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_{j=1}^J\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}\prod_{j=1}^J\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}.
   $$
2. Given $(\alpha,\beta)$, the $\theta_j$ are independent with beta posteriors,
   $$
   p(\theta\mid\alpha,\beta,y)=\prod_{j=1}^J\frac{\Gamma(\alpha+\beta+n_j)}{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}\theta_j^{\alpha+y_j-1}(1-\theta_j)^{\beta+n_j-y_j-1},\qquad\theta_j\mid\alpha,\beta,y\sim\mathrm{Beta}(\alpha+y_j,\beta+n_j-y_j).
   $$
3. Dividing the first expression by the second,
   $$
   p(\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_{j=1}^J\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\cdot\frac{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}{\Gamma(\alpha+\beta+n_j)}.
   $$
   Each factor is $\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)/\mathrm{B}(\alpha,\beta)$, the **beta-binomial distribution** of $y_j$ without its binomial coefficient: this is the marginal likelihood $p(y\mid\alpha,\beta)$ of §6.4.2. It is not a standard density in $(\alpha,\beta)$, but it is easily evaluated on a grid.

### 6.5.2. Choosing the Hyperprior

The hyperprior should express ignorance about $(\alpha,\beta)$ while giving a proper posterior. Several natural choices fail.

*An improper uniform prior, $p(\alpha,\beta)\propto1$, gives an improper posterior.* Fix the prior mean $\mu=\alpha/(\alpha+\beta)$ and let the prior sample size $s=\alpha+\beta$ tend to infinity. Then $\mathrm{Beta}(\alpha,\beta)$ concentrates at $\mu$, and each factor of the marginal likelihood tends to a positive constant,

$$
\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}=\frac{\prod_{k=0}^{y_j-1}(\alpha+k)\prod_{k=0}^{n_j-y_j-1}(\beta+k)}{\prod_{k=0}^{n_j-1}(\alpha+\beta+k)}\to\mu^{y_j}(1-\mu)^{n_j-y_j},
$$
the likelihood of complete pooling at the value $\mu$. The data cannot rule out that all groups share one rate, so the likelihood does not decay as $\alpha,\beta\to\infty$, and $\int\!\!\int p(\alpha,\beta\mid y)\,\mathrm{d}\alpha\,\mathrm{d}\beta=\infty$. For the posterior to be proper, $p(\alpha,\beta)$ must have a sufficiently light tail in this direction.

*A uniform prior on a bounded region is proper but must not cut off the posterior.* With independent $\alpha\sim\mathrm{U}(0,20)$, $\beta\sim\mathrm{U}(0,20)$,

$$
p(\alpha,\beta\mid y)\propto\boldsymbol{1}\{\alpha\le20\}\boldsymbol{1}\{\beta\le20\}\prod_{j=1}^J\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\cdot\frac{\Gamma(\alpha+y_j)\Gamma(\beta+n_j-y_j)}{\Gamma(\alpha+\beta+n_j)},
$$
and the posterior is clipped by the upper limit on $\beta$, where much of its mass would lie. Extending the limits to $\alpha\sim\mathrm{U}(0,40)$, $\beta\sim\mathrm{U}(0,100)$ captures the posterior, but the answer still depends on the arbitrary bounds, since the posterior has a long tail toward large $\alpha+\beta$.

*Reparametrization.* It is easier to think about the hyperparameters on the scale

$$
(\alpha,\beta)\longmapsto\Big(\log\frac\alpha\beta,\;\log(\alpha+\beta)\Big),
$$
where $\log(\alpha/\beta)=\operatorname{logit}\frac{\alpha}{\alpha+\beta}$ is the logit of the prior mean and $\alpha+\beta$ is the prior sample size, the size of the additional data the prior represents ([3.7.1](/3.7.1), §1.6.2). The advantage is that "prior mean" and "prior sample size" are separated and can be assigned prior distributions independently, and both new parameters range over the whole real line. But an improper uniform prior on $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)$ again gives an improper posterior: the likelihood tends to a positive constant as $\log(\alpha+\beta)\to\infty$.

*A diffuse prior with a proper posterior.* Take a uniform prior on $\big(\frac{\alpha}{\alpha+\beta},(\alpha+\beta)^{-1/2}\big)$, the prior mean and, roughly, the prior standard deviation scale, since the standard deviation of $\mathrm{Beta}(\alpha,\beta)$ is $\sqrt{\mu(1-\mu)/(\alpha+\beta+1)}$. With $u=\frac{\alpha}{\alpha+\beta}$, $v=(\alpha+\beta)^{-1/2}$ and $s=\alpha+\beta$, the Jacobian is

$$
\Big\lvert\frac{\partial(u,v)}{\partial(\alpha,\beta)}\Big\rvert=\left\lvert\det\begin{bmatrix}\beta/s^2&-\alpha/s^2\\-\frac12s^{-3/2}&-\frac12s^{-3/2}\end{bmatrix}\right\rvert=\frac12s^{-7/2}(\alpha+\beta)=\frac12(\alpha+\beta)^{-5/2},
$$
so

$$
p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2},\qquad\text{equivalently}\qquad p\Big(\log\frac\alpha\beta,\log(\alpha+\beta)\Big)\propto\alpha\beta(\alpha+\beta)^{-5/2},
$$
since the Jacobian of $(\alpha,\beta)\mapsto(\log\frac\alpha\beta,\log(\alpha+\beta))$ is $\frac{1}{\alpha\beta}$. In the coordinates $(\mu,s)$ this prior behaves like $s^{-3/2}$ for large $s$, which is integrable, and the posterior is proper. Other choices with sufficiently light tails are possible; what matters is that the conclusions are insensitive to the choice among reasonable ones.

### 6.5.3. Computation

Under the prior $p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$, compute the log of

$$
p\Big(\log\frac\alpha\beta,\log(\alpha+\beta)\Bigm|y\Big)\propto\alpha\beta(\alpha+\beta)^{-5/2}\prod_{j=1}^{71}\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}
$$
on a grid in the transformed coordinates, including the Jacobian $\alpha\beta$. The posterior is roughly symmetric on this scale, with its mode near $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)=(-1.79,2.74)$. The simulation then proceeds as follows.

1. Draw 1000 values of $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)$ from their posterior by discrete-grid sampling ([3.7.5](/3.7.5), Algorithm 5.2.1).
2. For $l=1,\dots,1000$:
   1. transform the $l$-th draw to the scale $(\alpha,\beta)$, which gives a draw of the hyperparameters from their marginal posterior;
   2. for each $j=1,\dots,J$, draw $\theta_j$ from its conditional posterior $\theta_j\mid\alpha,\beta,y\sim\mathrm{Beta}(\alpha+y_j,\beta+n_j-y_j)$.

The posterior means of the hyperparameters, computed from such draws, depend on the hyperprior in an instructive way:

| hyperprior | $\mathbb{E}(\alpha\mid y)$ | $\mathbb{E}(\beta\mid y)$ | $\mathbb{E}\big(\frac{\alpha}{\alpha+\beta}\mid y\big)$ | $\mathbb{E}(\alpha+\beta\mid y)$ |
|---|---|---|---|---|
| $p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$ | 2.4 | 14.3 | 0.144 | 16.7 |
| $\alpha\sim\mathrm{U}(0,40)$, $\beta\sim\mathrm{U}(0,100)$ | 3.5 | 20.7 | 0.143 | 24.2 |

As expected, the prior $(\alpha+\beta)^{-5/2}$ pulls $\alpha+\beta$ down, while the bounded uniform prior lets the long tail toward large $\alpha+\beta$ contribute. The estimated center of the population distribution is the same under both. The empirical Bayes estimate $\alpha+\beta\approx10$ of §6.1 is smaller than either, as the third remark of §6.1 predicts.

### 6.5.4. Shrinkage

What we really want are the tumor rates $\theta_j$:

$$
p(\theta\mid y)=\int p(\theta\mid\alpha,\beta,y)\,p(\alpha,\beta\mid y)\,\mathrm{d}\alpha\,\mathrm{d}\beta,
$$
which has no closed form but is represented by the simulated $\theta_j$. For an observed group $j$, by the **law of total expectation**,

$$
\mathbb{E}(\theta_j\mid y)=\mathbb{E}\big[\mathbb{E}(\theta_j\mid\alpha,\beta,y)\bigm|y\big]=\mathbb{E}\Big[\frac{\alpha+y_j}{\alpha+\beta+n_j}\Bigm|y\Big],
\qquad
\frac{\alpha+y_j}{\alpha+\beta+n_j}=\frac{\alpha+\beta}{\alpha+\beta+n_j}\cdot\frac{\alpha}{\alpha+\beta}+\frac{n_j}{\alpha+\beta+n_j}\cdot\frac{y_j}{n_j}.
$$
Each estimate is a weighted average of the group's own rate $y_j/n_j$ and the population mean $\frac{\alpha}{\alpha+\beta}$, with weights $n_j$ and $\alpha+\beta$, averaged over the posterior of the hyperparameters. This is partial pooling, and the pull toward the population mean is the **shrinkage** of [3.7.5](/3.7.5) §5.6: each group borrows information from the others. Groups with small $n_j$ and groups with extreme raw rates are pulled most. The experiments with $0$ tumors in about $20$ rats get posterior means near $0.06$ rather than $0$, and the highest rate $9/24=0.375$ is pulled to about $0.28$. The bounded uniform hyperprior, which has the larger effective prior sample size $\alpha+\beta$, shrinks the estimates more than $(\alpha+\beta)^{-5/2}$ does, though toward about the same place.

![Rat tumor example under the prior p(α, β) ∝ (α + β)^(−5/2). Left: contours of the marginal posterior of (log(α/β), log(α + β)) on a grid, with 500 of the simulated draws. Right: posterior medians and 95% intervals of the 71 tumor rates θj against the observed rates yj/nj (jittered horizontally); the dashed line is no pooling, and the current experiment 4/14 is marked.](./plots/rat_tumor_hyperposterior.py)

For the current experiment, the posterior of $\theta_{71}$ has mean $0.21$ and $95\%$ central posterior interval $[0.08,0.38]$, close to the empirical Bayes answer $\mathrm{Beta}(5.4,18.6)$ of §6.1 (mean $0.223$, interval $[0.08,0.41]$). With 70 informative experiments the uncertainty about $(\alpha,\beta)$ matters little for this one group, which explains why the empirical Bayes shortcut works reasonably here; the hierarchical model makes this a conclusion rather than an assumption.

For a new experiment, not yet observed, the rate $\tilde\theta$ is a new draw from the population distribution, and

$$
\mathbb{E}(\tilde\theta\mid y)=\mathbb{E}\big[\mathbb{E}(\tilde\theta\mid\alpha,\beta,y)\bigm|y\big]=\mathbb{E}\Big[\frac{\alpha}{\alpha+\beta}\Bigm|y\Big]=0.144,
$$
with $95\%$ interval $[0.02,0.36]$, much wider than for any observed group, because nothing is known about this group beyond the population.

## 6.6. The Normal Hierarchical Model: Eight Schools

### 6.6.1. Parallel Experiments in Eight Schools

**Example 6.6.1 (Eight Schools)** A study for the Educational Testing Service analyzed the effects of special coaching programs on the verbal part of the SAT (SAT-V) in eight high schools (Rubin, 1981). In each school, students were randomly assigned to coaching or control, and the treatment effect $y_j$ and its standard error $\sigma_j$ were estimated by a separate analysis of covariance in each school:

| school | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| estimated treatment effect $y_j$ | 28 | 8 | $-3$ | 7 | $-1$ | 1 | 18 | 12 |
| standard error $\sigma_j$ | 15 | 10 | 16 | 11 | 9 | 11 | 10 | 18 |

Each school had more than 30 students, so we treat the $y_j$ as eight independent normal observations, $y_j\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2)$, with known variances. The SAT-V scores range from 200 to 800, and the coaching programs were designed to raise them.

Some effects look large: can school A's $28$ be just chance? The two simple analyses are both unsatisfactory.

- *Separate estimates* (no pooling): the effect in school A is estimated as $28$ with standard error $15$. Under a flat prior, $\mathbb{P}(\theta_A>28\mid y)=0.5$, which seems too high: none of the other schools shows such an effect.
- *Pooled estimate* (complete pooling): all $\theta_j$ are assumed equal. With a non-informative prior the common effect has posterior mean equal to the precision-weighted average $\sum_jy_j/\sigma_j^2\big/\sum_j1/\sigma_j^2=7.7$, posterior variance $\big(\sum_j1/\sigma_j^2\big)^{-1}=16.6$, standard error $4.1$ and $95\%$ posterior interval $[-0.3,15.7]$. A chi-square test of homogeneity, $\sum_j(y_j-7.7)^2/\sigma_j^2=4.7$ on 7 degrees of freedom, does not reject equality. But then $\mathbb{P}(\theta_A<7.7\mid y)=0.5$ and even $\mathbb{P}(\theta_A<\theta_C\mid y)=0.5$, although school A estimated $28$ and school C $-3$.

Neither estimate is fully satisfactory. We want a compromise that combines information from all eight experiments without assuming all the $\theta_j$ to be equal: partial pooling.

### 6.6.2. The Model and Its Posterior

In general, let $y_{ij}\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma^2)$ for $i=1,\dots,n_j$ in groups $j=1,\dots,J$, with known variance. The group means $\bar y_{\cdot j}=\frac1{n_j}\sum_iy_{ij}$ are sufficient, with $\bar y_{\cdot j}\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2)$, $\sigma_j^2=\sigma^2/n_j$; in the eight schools $\bar y_{\cdot j}$ is $y_j$. The population distribution is normal with unknown hyperparameters $\mu$ and $\tau$:

$$
\bar y_{\cdot j}\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2),\qquad p(\theta_1,\dots,\theta_J\mid\mu,\tau)=\prod_{j=1}^J\mathcal{N}(\theta_j\mid\mu,\tau^2),\qquad(\mu,\tau)\sim p(\mu,\tau).
$$
The three steps give the following.

1. *Joint posterior.*
   $$
   p(\theta,\mu,\tau\mid y)\propto p(\mu,\tau)\,p(\theta\mid\mu,\tau)\,p(y\mid\theta)\propto p(\mu,\tau)\prod_{j=1}^J\mathcal{N}(\theta_j\mid\mu,\tau^2)\prod_{j=1}^J\mathcal{N}(\bar y_{\cdot j}\mid\theta_j,\sigma_j^2).
   $$
2. *Conditional posterior of the group means.* For fixed $(\mu,\tau)$ each $\theta_j$ is a normal mean with known variance and a normal prior ([3.7.2](/3.7.2), §2.3), so the $\theta_j$ are independent with
   $$
   \theta_j\mid\mu,\tau,y\sim\mathcal{N}(\hat\theta_j,V_j),\qquad\hat\theta_j=\frac{\frac1{\sigma_j^2}\bar y_{\cdot j}+\frac1{\tau^2}\mu}{\frac1{\sigma_j^2}+\frac1{\tau^2}},\qquad V_j=\frac{1}{\frac1{\sigma_j^2}+\frac1{\tau^2}}.
   $$
3. *Marginal posterior of the hyperparameters.* Integrating out $\theta_j$, $\bar y_{\cdot j}\mid\mu,\tau\sim\mathcal{N}(\mu,\sigma_j^2+\tau^2)$ independently, so
   $$
   p(\mu,\tau\mid y)\propto p(\mu,\tau)\prod_{j=1}^J\mathcal{N}(\bar y_{\cdot j}\mid\mu,\sigma_j^2+\tau^2).
   $$

We assign $\mu$ a non-informative uniform hyperprior given $\tau$, $p(\mu,\tau)=p(\mu\mid\tau)p(\tau)\propto p(\tau)$; a proper prior on $\mu$ would make little difference, since the data determine $\mu$ well once $\tau$ is given. The marginal posterior factors further as $p(\mu,\tau\mid y)=p(\mu\mid\tau,y)\,p(\tau\mid y)$. Given $\tau$, $\mu$ is the common mean of $J$ normal observations with variances $\sigma_j^2+\tau^2$, so

$$
\mu\mid\tau,y\sim\mathcal{N}(\hat\mu,V_\mu),\qquad\hat\mu=\frac{\sum_{j=1}^J\frac{1}{\sigma_j^2+\tau^2}\bar y_{\cdot j}}{\sum_{j=1}^J\frac{1}{\sigma_j^2+\tau^2}},\qquad V_\mu^{-1}=\sum_{j=1}^J\frac{1}{\sigma_j^2+\tau^2}.
$$
By the conditional probability formula, for any $\mu$,

$$
p(\tau\mid y)=\frac{p(\mu,\tau\mid y)}{p(\mu\mid\tau,y)}\propto\frac{p(\tau)\prod_{j=1}^J\mathcal{N}(\bar y_{\cdot j}\mid\mu,\sigma_j^2+\tau^2)}{\mathcal{N}(\mu\mid\hat\mu,V_\mu)},
$$
and choosing $\mu=\hat\mu$, where the denominator is $(2\pi V_\mu)^{-1/2}$,

$$
p(\tau\mid y)\propto p(\tau)\,V_\mu^{1/2}\prod_{j=1}^J(\sigma_j^2+\tau^2)^{-1/2}\exp\Big(-\frac{(\bar y_{\cdot j}-\hat\mu)^2}{2(\sigma_j^2+\tau^2)}\Big),
$$
where $\hat\mu$ and $V_\mu$ depend on $\tau$. This one-dimensional density is evaluated on a grid.

### 6.6.3. The Hyperprior for $\tau$

The behavior of the likelihood factor at the two ends of the range of $\tau$ decides which hyperpriors work.

1. *Uniform, $p(\tau)\propto1$: proper posterior.* As $\tau\to0$ the likelihood factor tends to a positive constant (the complete pooling likelihood), which is integrable near $0$. As $\tau\to\infty$, $V_\mu^{1/2}\approx\tau/\sqrt J$ and the product behaves like $\tau^{-J}$, so $p(\tau\mid y)$ decays like $\tau^{1-J}$, which is integrable for $J\ge3$.
2. *Uniform on $\log\tau$, $p(\tau)\propto1/\tau$: improper posterior.* Near $\tau=0$ the posterior behaves like $c/\tau$ with $c>0$, whose integral diverges. This prior, natural for a scale parameter in other settings ([3.7.2](/3.7.2), §2.8), fails here because the data cannot rule out $\tau=0$: they are consistent with all groups having the same mean.
3. *A proper prior*, for example a scaled inverse-chi-square distribution for $\tau^2$, always gives a proper posterior. It must be chosen with care, since priors of this family put very little mass near $\tau=0$ and can then dominate the posterior when $J$ is small. Proper weakly informative priors that keep positive density at $\tau=0$, such as a half-normal or half-Cauchy distribution for $\tau$, are common alternatives.

We use the uniform prior on $\tau$, together with the uniform prior on $\mu$.

### 6.6.4. Simulation

To draw from the joint posterior $p(\theta,\mu,\tau\mid y)$, for $k=1,\dots,S$:

1. draw $\tau^k$ from $p(\tau\mid y)$ on a grid;
2. draw $\mu^k$ from $p(\mu\mid\tau^k,y)=\mathcal{N}(\hat\mu^k,V_\mu^k)$, where $\hat\mu^k$ and $V_\mu^k$ are $\hat\mu$ and $V_\mu$ evaluated at $\tau^k$;
3. draw $\theta^k$ from $p(\theta\mid\mu^k,\tau^k,y)$. The components are conditionally independent given $\mu^k$, $\tau^k$ and $y$, so draw $\theta_j^k\sim\mathcal{N}(\hat\theta_j^k,V_j^k)$ independently, with
   $$
   \hat\theta_j^k=\frac{\frac1{\sigma_j^2}\bar y_{\cdot j}+\frac1{(\tau^k)^2}\mu^k}{\frac1{\sigma_j^2}+\frac1{(\tau^k)^2}},\qquad V_j^k=\frac{1}{\frac1{\sigma_j^2}+\frac1{(\tau^k)^2}}.
   $$

### 6.6.5. Results

The marginal posterior $p(\tau\mid y)$ has its mode at $\tau=0$, where the data are most consistent with complete pooling, but it is broad: its median is about $5$, its $97.5\%$ quantile about $20$, and $\mathbb{P}(\tau>10\mid y)=0.21$. Values of $\tau$ that make the schools quite different are far from excluded. The marginal maximum likelihood estimate of $\tau$ is $0$, and so is the moment estimate (the sample variance $109$ of the $y_j$ is smaller than the average sampling variance $166$), so an empirical Bayes analysis would plug in $\tau=0$ and report complete pooling with its overconfident intervals.

How the school effects depend on $\tau$ is seen from the conditional posterior means and standard deviations. Averaging $\hat\theta_j$ and $V_j$ over $\mu\mid\tau,y$,

$$
\mathbb{E}(\theta_j\mid\tau,y)=\frac{\frac1{\sigma_j^2}\bar y_{\cdot j}+\frac1{\tau^2}\hat\mu}{\frac1{\sigma_j^2}+\frac1{\tau^2}},\qquad
\operatorname{Var}(\theta_j\mid\tau,y)=V_j+\Big(\frac{V_j}{\tau^2}\Big)^2V_\mu.
$$
At $\tau=0$ all means equal the pooled estimate $7.7$ with standard deviation $4.1$; as $\tau$ grows they spread out toward the separate estimates $y_j$, and their standard deviations grow toward $\sigma_j$. The posterior of $\tau$, concentrated on small to moderate values, determines how far along this path the final answer lies.

![Eight schools under uniform priors on μ and τ. Left: marginal posterior density p(τ | y). Middle: conditional posterior means E(θj | τ, y) of the eight school effects as functions of τ; they all equal the pooled estimate at τ = 0. Right: conditional posterior standard deviations sd(θj | τ, y).](./plots/eight_schools_tau.py)

Averaging over $\tau$ gives the marginal posterior of each school effect. Quantiles from $200{,}000$ simulation draws, rounded:

| school | $y_j$ | $\sigma_j$ | $2.5\%$ | $25\%$ | median | $75\%$ | $97.5\%$ |
|---|---|---|---|---|---|---|---|
| A | 28 | 15 | $-2$ | 6 | 10 | 16 | 32 |
| B | 8 | 10 | $-5$ | 4 | 8 | 12 | 21 |
| C | $-3$ | 16 | $-11$ | 2 | 7 | 11 | 21 |
| D | 7 | 11 | $-6$ | 4 | 8 | 12 | 21 |
| E | $-1$ | 9 | $-9$ | 1 | 6 | 9 | 16 |
| F | 1 | 11 | $-9$ | 2 | 7 | 10 | 19 |
| G | 18 | 10 | $-1$ | 6 | 10 | 15 | 26 |
| H | 12 | 18 | $-7$ | 4 | 8 | 13 | 26 |

The estimates are strongly shrunk toward the common mean. School A's median is $10$ rather than $28$, but its interval extends to $32$; the probability that its effect exceeds that of school C is $0.68$, not $0.5$ as under complete pooling, and the probability that school A has the largest of the eight effects is about $0.25$. The hierarchical analysis agrees with the observation that the data are consistent with equal effects, without forcing that conclusion.

### 6.6.6. Posterior Predictions

Predictions fit into the simulations already done, in the two situations of §6.4.1.

1. *A new observation $\tilde y$ from a school $j$ already observed* (for example the estimated effect in a repetition of the study at school $j$, with standard error $\sigma_j$): for each draw $k$, sample $\tilde y_j^k\sim\mathcal{N}(\theta_j^k,\sigma_j^2)$. If $m$ observations are needed, draw $m$ values from the same distribution.
2. *An observation from a new school $\tilde j$*: for each draw $k$, first sample the new school's effect from the population distribution, $\theta_{\tilde j}^k\sim\mathcal{N}(\mu^k,(\tau^k)^2)$, a draw from the prior for $\theta$ given the hyperparameters, not from the posterior of any existing $\theta_j$; then sample $\tilde y_{\tilde j}^k\sim\mathcal{N}(\theta_{\tilde j}^k,\tilde\sigma^2)$, and similarly for $m$ observations.

The key difference is whether a new $\theta$ must be drawn or an existing one can be used. The second situation leads to more variable predictions, because there is less information about the corresponding $\theta$: the $95\%$ predictive interval for the effect $\theta_{\tilde j}$ of a new school is about $[-12,29]$, wider than the posterior interval for any existing school except A, and adding sampling error with $\tilde\sigma=10$ widens it to about $[-20,36]$.

## Summary

| Topic | Key facts |
|---|---|
| motivation | a prior fixed from historical data (empirical Bayes) ignores uncertainty in the hyperparameters and uses data twice; the full model puts a hyperprior on them (§6.1) |
| pooling | no pooling (separate $\theta_j$), complete pooling (common $\theta$), partial pooling (hierarchical) (Definition 6.2.1) |
| exchangeability | joint distribution invariant under permutations (Definition 6.3.1); not independence; reflects information, not the world (Example 6.3.1) |
| de Finetti | infinite exchangeable sequences are mixtures of i.i.d. sequences (Theorem 6.3.1): the basis for $\theta_j\mid\phi\overset{\text{iid}}{\sim}p(\theta\mid\phi)$ |
| structure | $p(\theta,\phi\mid y)\propto p(\phi)\prod_jp(\theta_j\mid\phi)\prod_jp(y_j\mid\theta_j)$; hyperprior $p(\phi)$ (Definition 6.4.1); predictions for existing and new groups |
| three steps | joint posterior; conditional $p(\theta\mid\phi,y)$; marginal $p(\phi\mid y)=p(\theta,\phi\mid y)/p(\theta\mid\phi,y)\propto p(\phi)p(y\mid\phi)$; simulate in reverse order |
| beta-binomial | $\theta_j\mid\alpha,\beta,y\sim\mathrm{Beta}(\alpha+y_j,\beta+n_j-y_j)$; $p(\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_j\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)/\mathrm{B}(\alpha,\beta)$ |
| hyperprior (beta) | flat on $(\alpha,\beta)$ or on $(\log\frac\alpha\beta,\log(\alpha+\beta))$: improper posterior; flat on $\big(\frac\alpha{\alpha+\beta},(\alpha+\beta)^{-1/2}\big)$, i.e. $(\alpha+\beta)^{-5/2}$: proper |
| shrinkage | $\mathbb{E}(\theta_j\mid y)=\mathbb{E}\big[\frac{\alpha+\beta}{\alpha+\beta+n_j}\frac{\alpha}{\alpha+\beta}+\frac{n_j}{\alpha+\beta+n_j}\frac{y_j}{n_j}\bigm|y\big]$; new group: $\mathbb{E}\big[\frac{\alpha}{\alpha+\beta}\bigm|y\big]$ |
| normal model | $\theta_j\mid\mu,\tau,y\sim\mathcal{N}(\hat\theta_j,V_j)$ (precision weighting); $\bar y_{\cdot j}\mid\mu,\tau\sim\mathcal{N}(\mu,\sigma_j^2+\tau^2)$; $\mu\mid\tau,y\sim\mathcal{N}(\hat\mu,V_\mu)$; $p(\tau\mid y)\propto p(\tau)V_\mu^{1/2}\prod_j(\sigma_j^2+\tau^2)^{-1/2}\mathrm{e}^{-(\bar y_{\cdot j}-\hat\mu)^2/(2(\sigma_j^2+\tau^2))}$ |
| hyperprior (normal) | $p(\tau)\propto1$ proper for $J\ge3$; $p(\log\tau)\propto1$ improper; proper priors on $\tau$ fine |
| eight schools | $\tau=0$ is the mode but $\mathbb{P}(\tau>10\mid y)\approx0.2$; school effects shrunk toward $7.7$; new-school predictions are wider |

## Questions

1. Derive the marginal posterior $p(\alpha,\beta\mid y)$ of the beta-binomial hierarchical model in two ways: by the conditional probability formula, and by integrating out each $\theta_j$.

   **Answer** Ratio: dividing the joint posterior of §6.5.1 by $p(\theta\mid\alpha,\beta,y)=\prod_j\frac{\theta_j^{\alpha+y_j-1}(1-\theta_j)^{\beta+n_j-y_j-1}}{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}$, all powers of $\theta_j$ cancel and $p(\alpha,\beta\mid y)\propto p(\alpha,\beta)\prod_j\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}$, using $\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}=\frac1{\mathrm{B}(\alpha,\beta)}$. Integration: $\int_0^1\frac{\theta^{\alpha+y_j-1}(1-\theta)^{\beta+n_j-y_j-1}}{\mathrm{B}(\alpha,\beta)}\,\mathrm{d}\theta=\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}$ for each $j$; the product times $p(\alpha,\beta)$ is the same expression. The normalizing constants $\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)$ of the conditional posterior depend on the hyperparameters, which is why they must be kept in the ratio.
2. Show that the prior $p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$ corresponds, in the coordinates $\mu=\frac{\alpha}{\alpha+\beta}$, $s=\alpha+\beta$, to $p(\mu,s)\propto s^{-3/2}$, and explain why this gives a proper posterior while $p(\alpha,\beta)\propto1$ does not.

   **Answer** $\alpha=\mu s$, $\beta=(1-\mu)s$, so $\big\lvert\frac{\partial(\alpha,\beta)}{\partial(\mu,s)}\big\rvert=\lvert\det\begin{bmatrix}s&\mu\\-s&1-\mu\end{bmatrix}\rvert=s$ and $p(\mu,s)\propto s\cdot s^{-5/2}=s^{-3/2}$. As $s\to\infty$ the marginal likelihood tends to the positive function $\prod_j\mu^{y_j}(1-\mu)^{n_j-y_j}$ of $\mu$, so the tail of the posterior in $s$ behaves like the prior: $\int^\infty s^{-3/2}\,\mathrm{d}s<\infty$, a proper posterior. Under $p(\alpha,\beta)\propto1$ the density in $(\mu,s)$ is $\propto s$, and $\int^\infty s\,\mathrm{d}s=\infty$. Near $s=0$ the likelihood vanishes (each group with $0<y_j<n_j$ contributes a factor of order $s$), so no problem arises there.
3. For the normal hierarchical model, show that $\bar y_{\cdot j}\mid\mu,\tau\sim\mathcal{N}(\mu,\sigma_j^2+\tau^2)$ and that $p(\tau)\propto1/\tau$ gives an improper posterior.

   **Answer** Write $\bar y_{\cdot j}=\theta_j+\varepsilon_j$ with $\theta_j\mid\mu,\tau\sim\mathcal{N}(\mu,\tau^2)$ and an independent $\varepsilon_j\sim\mathcal{N}(0,\sigma_j^2)$; a sum of independent normal variables is normal, with mean $\mu$ and variance $\tau^2+\sigma_j^2$. In $p(\tau\mid y)\propto p(\tau)V_\mu^{1/2}\prod_j(\sigma_j^2+\tau^2)^{-1/2}\exp(\dots)$ every factor except $p(\tau)$ has a finite positive limit as $\tau\to0$ (the values for complete pooling). Hence $p(\tau\mid y)\approx c/\tau$ near $0$ with $c>0$, and $\int_0^\varepsilon c/\tau\,\mathrm{d}\tau=\infty$.
4. In the eight schools at $\tau=10$, one finds $\hat\mu=8.13$ and $V_\mu=30.5$. Compute $\mathbb{E}(\theta_A\mid\tau=10,y)$ and $\operatorname{sd}(\theta_A\mid\tau=10,y)$ and interpret them.

   **Answer** With $\sigma_A^2=225$ and $\tau^2=100$, $V_A=\big(\frac1{225}+\frac1{100}\big)^{-1}=69.2$ and $\mathbb{E}(\theta_A\mid\tau,y)=69.2\big(\frac{28}{225}+\frac{8.13}{100}\big)=14.2$: the estimate moves about $70\%$ of the way from $28$ to the overall mean, because school A's standard error $15$ is large relative to $\tau=10$. The variance is $V_A+(V_A/\tau^2)^2V_\mu=69.2+0.692^2\times30.5=83.8$, so the standard deviation is $9.2$, smaller than $\sigma_A=15$ but larger than $\sqrt{V_A}=8.3$ because $\mu$ is uncertain too.
5. Decide whether exchangeability is a reasonable prior assumption, and if not, how to modify the model: (a) the mean blood pressures of 30 patients in a clinical trial, about whom nothing else is recorded; (b) the mortality rates of 50 hospitals whose numbers of beds are known and believed to matter; (c) a patient's daily weight over 30 days of a diet.

   **Answer** (a) Exchangeable: nothing distinguishes the patients, so a common population distribution is appropriate. (b) Not exchangeable unconditionally, since the size carries information; model the rates as exchangeable given size, for example $\operatorname{logit}\theta_j\sim\mathcal{N}(\gamma_0+\gamma_1x_j,\tau^2)$ with $x_j$ the log number of beds, which is a hierarchical regression. (c) Not exchangeable: the order of the days matters (a trend is expected, and nearby days are more alike), so a time series or regression on time is needed; the deviations from the trend might be treated as exchangeable.
6. Show that the equicorrelated normal vector $(\theta_1,\dots,\theta_J)$ with common variance $\sigma^2$ and correlation $\rho$ exists only if $\rho\ge-1/(J-1)$, and that an infinite exchangeable sequence with finite variances must have $\rho\ge0$.

   **Answer** The covariance matrix $\sigma^2[(1-\rho)I_J+\rho\boldsymbol{1}\boldsymbol{1}^{\mathsf T}]$ has eigenvalues $\sigma^2(1-\rho)$ (multiplicity $J-1$) and $\sigma^2(1+(J-1)\rho)$ (eigenvector $\boldsymbol{1}$), and it is positive semidefinite if and only if $-\frac{1}{J-1}\le\rho\le1$. For an infinite exchangeable sequence every finite segment must satisfy this, so $\rho\ge-1/(J-1)$ for all $J$, that is $\rho\ge0$. Equivalently, $0\le\operatorname{Var}\big(\sum_{j=1}^J\theta_j\big)=J\sigma^2+J(J-1)\rho\sigma^2$ for all $J$ forces $\rho\ge0$. This agrees with de Finetti's theorem, under which $\operatorname{Cov}(\theta_1,\theta_2)=\operatorname{Var}\big(\mathbb{E}(\theta_1\mid\phi)\big)\ge0$.
7. In the rat tumor example, approximate the posterior means of $\theta_j$ for a group with $0/20$ and for the current group $4/14$ by plugging the posterior means $\alpha=2.4$, $\beta=14.3$ into $\frac{\alpha+y_j}{\alpha+\beta+n_j}$. Why is this only an approximation?

   **Answer** For $0/20$: $\frac{2.4}{16.7+20}=0.065$. For $4/14$: $\frac{2.4+4}{16.7+14}=0.208$. Both are close to the simulation results ($0.06$ and $0.21$). The exact posterior mean is $\mathbb{E}\big[\frac{\alpha+y_j}{\alpha+\beta+n_j}\bigm|y\big]$, the posterior expectation of a nonlinear function of $(\alpha,\beta)$, which in general differs from the function evaluated at the posterior means; the difference is small here because $(\alpha,\beta)$ is fairly well determined by 71 groups.
8. An analyst estimates $\tau$ in the eight schools by marginal maximum likelihood, obtains $\hat\tau=0$, and reports the complete pooling result for every school. What is wrong, and how does the fully Bayesian analysis differ?

   **Answer** The likelihood of $\tau$ is maximized at the boundary value $0$, but it is flat over a wide range: values of $\tau$ up to about $20$ are reasonably consistent with the data. Plugging in $\hat\tau=0$ treats this uncertain estimate as known and reports intervals for each school of half-width about $8$ around $7.7$, which are far too narrow and rule out school-to-school differences that the data do not rule out. The fully Bayesian analysis averages over $p(\tau\mid y)$: the school effects are still shrunk strongly toward $7.7$, but their intervals (for school A $[-2,32]$) reflect both the possibility of equal effects and that of substantial differences. This is the typical failure of empirical Bayes with few groups, and an instance of a parameter on the boundary ([3.7.5](/3.7.5), §5.5.6).
9. Explain why the predictive distribution of an observation from a new school is wider than that of a new observation from school B, and write its variance in terms of posterior moments.

   **Answer** For school B the posterior of $\theta_B$ is informed by school B's own data and the other schools, and $\operatorname{Var}(\tilde y_B\mid y)=\sigma_B^2+\operatorname{Var}(\theta_B\mid y)$. For a new school the effect is a fresh draw from the population distribution, so by the **law of total variance** $\operatorname{Var}(\tilde\theta\mid y)=\mathbb{E}(\tau^2\mid y)+\operatorname{Var}(\mu\mid y)$, and $\operatorname{Var}(\tilde y\mid y)=\tilde\sigma^2+\mathbb{E}(\tau^2\mid y)+\operatorname{Var}(\mu\mid y)$. The variance $\operatorname{Var}(\theta_B\mid y)$ is reduced by school B's data, while $\mathbb{E}(\tau^2\mid y)$ is the full between-school variation with no data to reduce it.
