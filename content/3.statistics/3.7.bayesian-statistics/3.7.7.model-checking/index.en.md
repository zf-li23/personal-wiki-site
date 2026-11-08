---
title: Model Checking
description: Why Bayesian models must be checked, sensitivity analysis and external validation, posterior predictive checks with replicated data, test quantities and posterior predictive p-values (binary sequence and Newcomb's speed of light), their interpretation, and graphical checks with the chi-square discrepancy for the rat tumor data and the sodium-in-beer example.
---

Every posterior in the previous chapters was computed as if the model were true: the sampling distribution, the prior and, for **hierarchical models**, the population distribution were taken for granted, and Bayes' rule did the rest. Bayesian inference is only as good as these assumptions, and a posterior distribution reports its uncertainty *within* the model; it says nothing about whether the model describes the data at all. This chapter is about the step that closes the loop of a Bayesian analysis: comparing the fitted model with the data and with what we know about the problem. The main tool is the **posterior predictive distribution** of [3.2.7](/3.2.7) and [3.7.1](/3.7.1): if the model is adequate, data simulated from it should look like the data we have. After the motivation (§7.1) and a short look at checking against new data (§7.2), the chapter develops posterior predictive checks with test quantities and p-values (§7.3) and their graphical versions (§7.4). The examples reuse the models of [3.7.3](/3.7.3) and [3.7.6](/3.7.6). The next chapter ([3.7.8](/3.7.8)) turns from checking one model to comparing several.

## 7.1. Why Check Models

"All models are wrong but some models are useful" (George E. P. Box). Classical analyses routinely check model assumptions; in linear regression, for instance, one checks the form of the regression function (linear or quadratic), constant variance of the residuals, their independence and their normality. A Bayesian analysis needs the same care, and the question is not whether the model is correct (it is not) but whether its inaccuracies matter for the conclusions we want to draw.

### 7.1.1. How Much Do the Assumptions Matter?

The basic question is how sensitive the posterior inferences are to the modeling assumptions. Recall the rat tumor data of [3.7.6](/3.7.6): in each of $J=71$ groups of laboratory rats, $y_j$ of $n_j$ rats developed a tumor. Three reasonable models for the tumor rates are:

| | Data model | Parameter model | Hyperprior |
|---|---|---|---|
| 1. Beta hierarchy | $y_j\mid\theta_j\sim\mathrm{Bin}(n_j,\theta_j)$ independently | $\theta_j\mid\alpha,\beta\overset{\text{iid}}{\sim}\mathrm{Beta}(\alpha,\beta)$ | $p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$ |
| 2. Logit-normal hierarchy | $y_j\mid\theta_j\sim\mathrm{Bin}(n_j,\theta_j)$ independently | $\operatorname{logit}(\theta_j)\mid\mu,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ | $p(\mu,\sigma^2)\propto\sigma^{-2}$ |
| 3. Beta-binomial data model | $y_j\mid\alpha_j,\beta_j\sim\mathrm{BetaBin}(n_j,\alpha_j,\beta_j)$ independently | $\alpha_j\sim\Gamma(\gamma_\alpha,\delta_\alpha)$, $\beta_j\sim\Gamma(\gamma_\beta,\delta_\beta)$, all independent | $p(\gamma_\alpha,\delta_\alpha,\gamma_\beta,\delta_\beta)\propto1$ |

In the third model the tumor rate of group $j$ is $\mathbb{E}(y_j/n_j\mid\alpha_j,\beta_j)=\alpha_j/(\alpha_j+\beta_j)$. Do the three models give substantially different answers about the tumor rates? If they do, the choice among them has to be justified; if they do not, the conclusions are robust to it.

Experience from classical statistics shows both cases. In the linear model $Y=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$, the least-squares estimator $\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$ is unbiased as soon as $\mathbb{E}\boldsymbol{\varepsilon}=\boldsymbol{0}$, and by the **Gauss–Markov theorem** it has minimum variance among linear unbiased estimators if in addition the errors are uncorrelated with constant variance; neither result requires normality, so moderate non-normality does little harm, at least in large samples. By contrast, the $F$-test of $H_0\colon\sigma_1^2=\sigma_2^2$ against $H_1\colon\sigma_1^2\ne\sigma_2^2$ depends heavily on the normality of each group, and its error rates can be far from nominal for heavy-tailed data.

### 7.1.2. Model Checking in a Bayesian Analysis

A Bayesian analysis has three steps, which are iterated:

1. construct a full probability model for all observable and unobservable quantities;
2. compute the posterior distribution of all estimands;
3. assess the fit of the model to the data and to our substantive knowledge, and improve the model if necessary.

Checking is crucial because Bayes' rule faithfully propagates whatever the model says: when the model is poor, prior-to-posterior inference can be confidently misleading.

**Definition 7.1.1 (Sensitivity Analysis)** A **sensitivity analysis** asks how much the posterior inferences change when other reasonable probability models are used in place of the present one, for instance with a different prior, a different sampling distribution, or different information included.

Often more than one reasonable model fits the data adequately, and such models may still differ substantially in their priors, their sampling distributions or the information they use. Ideally one would build a "super-model": a comprehensive joint distribution over all possible true models, whose posterior would automatically average over the uncertainty about the model. In practice a super-model that includes all possibilities and all substantive knowledge is conceptually impossible and computationally infeasible in all but the simplest problems. Instead, checks are based on the posterior predictive distribution: does the data look the way the fitted model says it should? This can be done in two ways.

- *External validation*: future data are compared with the posterior predictive distribution (§7.2).
- *Internal validation*: the observed data are compared with the posterior predictive distribution (§7.3, §7.4).

## 7.2. External Validation

**Definition 7.2.1 (External Validation)** **External validation** checks a model by using it to predict data that were not used in fitting it, collecting those data, and comparing them with the predictions.

External validation is the most direct check of a model's usefulness, and it is the standard of the experimental sciences. It has two practical difficulties.

- We often need to check a model before new data are available, and collecting them may be expensive or impossible.
- One model can make many different predictions, for instance for an existing group or for a new group of a hierarchical model, so choosing which predictions to focus on is itself a modeling decision.

## 7.3. Posterior Predictive Checking

The internal version of the same idea is self-consistency: if the model fits, replicated data generated under the model should look similar to the observed data. A discrepancy is due either to model misspecification or to chance, and the task is to tell the two apart. The procedure is to draw simulated data sets from the posterior predictive distribution, compare them with the observed data, and treat any systematic difference as a potential failing of the model.

**Definition 7.3.1 (Posterior Predictive Check)** Let $y$ be the observed data and $\theta$ the vector of all parameters (including hyperparameters). The **replicated data** $y^{\mathrm{rep}}$ are the data that could have been observed if the experiment that produced $y$ were repeated tomorrow with the same model and the same value of $\theta$; their distribution is the posterior predictive distribution

$$
p(y^{\mathrm{rep}}\mid y)=\int p(y^{\mathrm{rep}}\mid\theta)\,p(\theta\mid y)\,\mathrm{d}\theta.
$$
A **posterior predictive check** compares the observed data $y$ with draws of $y^{\mathrm{rep}}$ from this distribution.

The notation distinguishes $y^{\mathrm{rep}}$ from a general future observation $\tilde y$. A replication is an exact copy of the observed design: it conditions on the same covariates and the same structure. In the rat tumor example, $y^{\mathrm{rep}}$ consists of $71$ counts with the same group sizes $n_1,\dots,n_{71}$ as the data. A future outcome $\tilde y$ need not have the covariate structure of the data; the number of tumors in a new, 72nd group is a $\tilde y$ but not part of a $y^{\mathrm{rep}}$.

### 7.3.1. Test Quantities and Posterior Predictive p-Values

Comparing data sets as a whole is hopeless, so, as in **hypothesis testing**, we choose a scalar summary that measures the aspect of the data we are worried about.

**Definition 7.3.2 (Test Quantity)** A **test quantity**, or discrepancy measure, is a scalar function $T(y,\theta)$ of the data and the parameters used to compare the data with predictive simulations. A test quantity that depends on the data only, $T(y)$, is a test statistic in the classical sense.

**Definition 7.3.3 (Posterior Predictive p-Value)** The **posterior predictive p-value** (Bayesian p-value) of a test quantity $T$ is

$$
p_B=\mathbb{P}\big(T(y^{\mathrm{rep}},\theta)\ge T(y,\theta)\mid y\big)=\iint\boldsymbol{1}\{T(y^{\mathrm{rep}},\theta)\ge T(y,\theta)\}\,p(y^{\mathrm{rep}}\mid\theta)\,p(\theta\mid y)\,\mathrm{d}y^{\mathrm{rep}}\,\mathrm{d}\theta,
$$
the probability under the posterior predictive distribution that the replicated data are at least as extreme as the observed data, with $\theta$ and $y^{\mathrm{rep}}$ drawn jointly.

Compare the classical **p-value** for a test statistic $T(y)$,

$$
p_C=\mathbb{P}\big(T(y^{\mathrm{rep}})\ge T(y)\mid\theta\big).
$$
In $p_C$ the parameter $\theta$ is fixed (at the null value, or eliminated by choosing a pivotal $T$) and only $y^{\mathrm{rep}}$ is random. In $p_B$ both $y^{\mathrm{rep}}$ and $\theta$ are random, and the uncertainty about $\theta$ is averaged over with the posterior: when $T$ depends on $y$ only, $p_B=\int p_C(\theta)\,p(\theta\mid y)\,\mathrm{d}\theta$ is the posterior mean of the classical p-value (Question 3). Choosing $T$ plays the role that choosing a powerful test statistic plays in classical testing.

The double integral is rarely available in closed form, but simulation is straightforward.

**Algorithm 7.3.1 (Posterior Predictive p-Value by Simulation)** Given $L$ draws $\theta^1,\dots,\theta^L$ from $p(\theta\mid y)$:

1. for each $l$, draw one replicated data set $y^{\mathrm{rep},l}\sim p(y^{\mathrm{rep}}\mid\theta^l)$;
2. compute the realized and the replicated test quantities $T(y,\theta^l)$ and $T(y^{\mathrm{rep},l},\theta^l)$;
3. estimate $p_B$ by the proportion of draws in which the replication is at least as extreme,

$$
\hat p_B=\frac1L\sum_{l=1}^L\boldsymbol{1}\{T(y^{\mathrm{rep},l},\theta^l)\ge T(y,\theta^l)\}.
$$

The pairs $\big(T(y,\theta^l),T(y^{\mathrm{rep},l},\theta^l)\big)$ are draws from their joint posterior predictive distribution, which is also what the graphical checks of §7.4 display.

### 7.3.2. Example: Checking Independence in Binomial Trials

**Example 7.3.1** A binary sequence $y_1,\dots,y_n$ is modeled as independent trials with a common probability of success $\theta$, with the uniform prior $\theta\sim\mathrm{Beta}(1,1)$, so that $\theta\mid y\sim\mathrm{Beta}(\sum y_i+1,n-\sum y_i+1)$. The observed sequence, in order, is

$$
1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,
$$
with $n=20$, $\sum y_i=7$ and posterior $\mathrm{Beta}(8,14)$. The long runs suggest positive autocorrelation, which the model ignores. To check independence, take $T$ to be the number of switches between $0$ and $1$ in the sequence; here $T(y)=3$, while independent trials with $\theta\approx0.35$ would switch about eight times. The posterior predictive distribution of $T(y^{\mathrm{rep}})$ is simulated by drawing $\theta^s\sim\mathrm{Beta}(8,14)$ and then $y^{\mathrm{rep},s}=(y_1^{\mathrm{rep},s},\dots,y_{20}^{\mathrm{rep},s})$ as independent Bernoulli variables with probability $\theta^s$, for $s=1,\dots,10000$.

![Posterior predictive checks. Left: number of switches in 10,000 replications of the binary sequence, against the observed T(y) = 3; 98% of the replications switch at least as often. Right: smallest of the 66 values in each of 5,000 replications of Newcomb's data under the normal model, against the observed minimum −44.](./plots/ppc_switches.py)

In the simulation $98.3\%$ of the replications have at least as many switches as the data, $\hat p_B=\mathbb{P}(T(y^{\mathrm{rep}})\ge T(y)\mid y)\approx0.98$, and only $1.7\%$ have fewer than three. An extreme p-value near $1$ is as much evidence against the model as one near $0$: the observed sequence switches unusually rarely. (The opposite tail $\mathbb{P}(T(y^{\mathrm{rep}})\le T(y)\mid y)\approx0.03$ expresses the same thing; one can also use $-T$ to put the evidence in the upper tail.) The independence assumption fails, and a model with dependence, such as a Markov chain for the sequence, is needed.

### 7.3.3. Choosing Test Quantities

A probability model can fail to reflect the process that generated the data in any number of ways, so posterior predictive p-values are computed for several test quantities, each probing one possible failure. Two principles guide the choice.

- Ideally, $T$ reflects aspects of the model that are relevant to the scientific purpose of the inference: a misfit that does not affect the conclusions is of little concern.
- $T$ should measure a feature of the data that the model does not directly address, such as the ranks of the sample, or the correlation of the residuals with a possible explanatory variable. A statistic the model fits by construction, such as a **sufficient statistic**, gives no information: for the binary sequence, $T(y)=\sum y_i$ gives $\hat p_B\approx0.59$ whatever the order of the data (Question 1).

**Example 7.3.2 (Newcomb's Speed of Light)** In 1882 Simon Newcomb measured the time light needs to travel about $7.4\,\mathrm{km}$; the $n=66$ measurements, recorded as deviations from $24800\,\mathrm{ns}$, have mean $26.2$ and standard deviation $10.75$, but two of them, $-44$ and $-2$, lie far below the rest. With the normal model $y_i\mid\mu,\sigma^2\sim\mathcal{N}(\mu,\sigma^2)$ and the non-informative prior $p(\mu,\log\sigma)\propto1$ of [3.7.3](/3.7.3), the worry is the effect of outliers, so $T$ must focus on this issue.

- $T(y)=\min_iy_i$ addresses low outliers. In the figure above, none of the $5000$ replicated data sets has a minimum anywhere near $-44$; even the smallest replicated minimum is above $-30$ and the typical one is about $1$, so $\hat p_B=\mathbb{P}(\min y^{\mathrm{rep}}\le\min y\mid y)\approx0$.
- $T(y,\theta)=\max_i\lvert y_i-\mu\rvert$ is appropriate if the worry is a large residual in either direction. It depends on the parameter $\mu$, and the check compares $\max_i\lvert y_i-\mu^s\rvert$ with $\max_i\lvert y_i^{\mathrm{rep},s}-\mu^s\rvert$ for each draw; for Newcomb's data it again gives $\hat p_B\approx0$.

The normal sampling model is inadequate for the extremes of the data. A revised model replaces it with a heavy-tailed one, $y_i\mid\mu,\sigma^2\sim t_\nu(\mu,\sigma^2)$, in which a few large deviations are expected and have less influence on the inference about $\mu$.

:::

The second test quantity illustrates a real advantage over classical testing. A classical test statistic may depend on the data only, and its distribution under the null must be known or approximated. A Bayesian test quantity may depend on the data and on the parameters and hyperparameters, its exact distribution is never needed (both $T(y,\theta)$ and $T(y^{\mathrm{rep}},\theta)$ are unknowns represented by simulations), and many problems have a function of data and parameters that addresses a particular aspect of the model directly, where a function of the data alone would be difficult or awkward.

### 7.3.4. Interpreting Posterior Predictive p-Values

- An extreme p-value (near $0$ or $1$) says that the observed pattern would be unlikely if the model were true. It is a probability, but not $\mathbb{P}(\text{model is true}\mid y)$: it is $\mathbb{P}\big(T(y^{\mathrm{rep}},\theta)\ge T(y,\theta)\mid y\big)$, a statement about data sets under the model, not about models.
- If a p-value is extreme, it usually does not matter how extreme. A p-value of $0.00001$ is effectively no stronger evidence than one of $0.001$; both say that the model fails in this respect.
- As with classical p-values, $p_B$ measures statistical significance, not practical significance. Small changes to the model can produce large changes in the p-value, and a misfit that is statistically clear may be irrelevant for the purposes of the analysis.
- Finding an extreme p-value is never the end of an analysis: it points to a direction in which the model should be improved, and the next step is usually a better model.

**Remark 7.3.1** Posterior predictive p-values use the data twice, once to fit $\theta$ and once to check, so even when the model is true they are not uniformly distributed on $[0,1]$: they tend to concentrate around $0.5$, and a small $p_B$ is rarer than a small classical p-value. The check is therefore conservative; this does not invalidate the method, whose aim is to reveal misfit rather than to control error rates.

*Multiple comparisons.* A model is usually checked with several test quantities from several angles. One could adjust for **multiple comparisons**, for instance by computing the probability of the most extreme p-value or by a **Bonferroni correction**, but this is not recommended in model checking. We are not concerned with a Type I error rate for accepting or rejecting the model, which we know to be wrong anyway; we try to understand the limits of its applicability in realistic replications, and each check answers a separate question about this.

*The likelihood principle.* A posterior predictive check depends on the sampling distribution through $p(y^{\mathrm{rep}}\mid\theta)$, that is, on data that might have been observed but were not, so it does not obey the **likelihood principle**: two experiments with proportional likelihoods, such as binomial and negative binomial sampling, give the same posterior but different replications and different checks. This is intended. The posterior is conditional on the model, while a check asks whether the model, including the design that generated the data, is adequate.

## 7.4. Graphical Posterior Predictive Checks

The basic idea of graphical checks is to display the data alongside data simulated from the fitted model and to look for systematic discrepancies between them. A p-value summarizes one aspect in one number; a graph can show where and how the model fails. There are three kinds of display:

1. direct display of all the data;
2. display of data summaries or parameter inferences;
3. graphs of residuals or other measures of discrepancy between model and data.

### 7.4.1. Direct Display of the Data

**Example 7.4.1** In an experiment in psychology, each of six persons answered yes or no to whether they would show each of $15$ possible reactions (such as getting angry, laughing or crying) in each of $23$ situations (such as learning that an examination has been announced, or that it has been canceled). The data are six $15\times23$ arrays of binary responses, and they were fitted with a logistic regression model. Displayed in the original order of rows and columns, the observed arrays and seven arrays $y^{\mathrm{rep}}$ simulated from the fitted model all look fuzzy and random, and no failure of the model can be detected. After the rows and columns of each array are sorted in increasing order of average response, the observed data show strong row and column patterns for individual persons (for example, a nearly white row in the middle of one person's array) that do not appear in the replications. The patterns are not captured by the model, which suggests a model failure. Finding a display that reveals such structure is a real art.

### 7.4.2. Graphs Based on Test Quantities

The p-value tells only part of the story. It is also useful to look at the joint distribution of the realized and the replicated test quantities over the posterior draws, displayed as a scatterplot of $T(y^{\mathrm{rep},s},\theta^s)$ against $T(y,\theta^s)$, or as a histogram of the differences $T(y^{\mathrm{rep},s},\theta^s)-T(y,\theta^s)$ (or of their ratios). Under the model, the scatterplot should be symmetric about the $45^\circ$ line, and the histogram of differences should include $0$ (that of the ratios should include $1$).

Besides test quantities aimed at a particular failure, there are general measures of fit. The most common is the omnibus $\chi^2$ discrepancy

$$
T(y,\theta)=\sum_i\frac{\big(y_i-\mathbb{E}(y_i\mid\theta)\big)^2}{\operatorname{Var}(y_i\mid\theta)}.
$$
For known $\theta$ it is the classical Pearson $\chi^2$ statistic of a **goodness-of-fit test**; here it is a test quantity that depends on the parameters, and its reference distribution comes from simulation, not from $\chi^2$ asymptotics.

**Example 7.4.2 (Rat Tumors)** For the $71$ groups of rats, compare two models.

1. *Common tumor rate*: $y_j\mid\theta\sim\mathrm{Bin}(n_j,\theta)$ independently, one $\theta$ for all groups.
2. *Variable tumor rates*: $y_j\mid\theta_j\sim\mathrm{Bin}(n_j,\theta_j)$, $\theta_j\mid\alpha,\beta\overset{\text{iid}}{\sim}\mathrm{Beta}(\alpha,\beta)$, $p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$, the hierarchical model of [3.7.6](/3.7.6).

The $\chi^2$ discrepancy is $T(y,\theta)=\sum_j(y_j-n_j\theta_j)^2/\big(n_j\theta_j(1-\theta_j)\big)$, with $\theta_j=\theta$ in the first model. Replicated data keep the group sizes: $y_j^{\mathrm{rep},s}\sim\mathrm{Bin}(n_j,\theta_j^s)$.

![Chi-square discrepancy for the 71 rat tumor groups (Tarone 1982), 5,000 posterior draws. Each point is (T(y, θ^s), T(y_rep,s, θ^s)); the line is the 45° diagonal. Left: a common tumor rate; every realized discrepancy exceeds its replication. Right: the hierarchical beta-binomial model; the cloud straddles the diagonal.](./plots/ppc_chi2_discrepancy.py)

| Model | Mean of $T(y,\theta^s)$ | Mean of $T(y^{\mathrm{rep},s},\theta^s)$ | $\hat p_B$ |
|---|---|---|---|
| common rate | $143$ | $71$ | $0.00$ |
| variable rates | $72$ | $71$ | $0.48$ |

With a common rate, the realized discrepancy, about $143$, is twice what replications produce, about $71$ (the number of groups, as for a $\chi^2_{71}$ variable); not one draw has $T(y^{\mathrm{rep}},\theta)\ge T(y,\theta)$. The groups vary far more than binomial sampling around one rate allows: the data are overdispersed. Under the hierarchical model, the realized and replicated discrepancies have nearly the same distribution, the cloud lies across the diagonal, and $\hat p_B\approx0.48$ shows no evidence of misfit. (The values are from the simulation in the figure; another run differs in the second digit of $\hat p_B$.)

### 7.4.3. Example: Sodium Content in Beer

**Example 7.4.3** A study investigated the sodium content of beer: $6$ brands were chosen at random, and $8$ randomly chosen bottles or cans of each brand were analyzed, giving the sodium content $y_{ij}$ (in $\mathrm{mg}$) of bottle $i$ of brand $j$. The brand means differ considerably (from about $10$ to about $24\,\mathrm{mg}$), and bottles within a brand vary little. A hierarchical normal model as in [3.7.6](/3.7.6) treats the brand means $\theta_j$ as draws from $\mathcal{N}(\mu,\tau^2)$, with the sampling variance of each brand mean treated as known, $\sigma_j^2=0.0895$, derived from the mean squared error of a one-way **analysis of variance**. The posterior summaries are

$$
\mathbb{E}(\tau\mid y)=6.448,\quad\operatorname{mode}(\tau\mid y)=4.61,\quad\mathbb{E}(\tau^2\mid y)=50.85,\quad\operatorname{mode}(\tau^2\mid y)=21.25,\quad\mathbb{E}(\mu\mid y)=17.67,\quad\operatorname{sd}(\mu\mid y)=2.928.
$$
The amount of shrinkage is visible in the conditional posterior mean

$$
\mathbb{E}(\theta_j\mid\mu,\tau,y)=\frac{\tau^2}{\sigma_j^2+\tau^2}\,\bar y_{\cdot j}+\frac{\sigma_j^2}{\sigma_j^2+\tau^2}\,\mu:
$$
since $\sigma_j^2$ is tiny compared with $\tau^2$, each $\theta_j$ is essentially its brand mean $\bar y_{\cdot j}$. Displaying the observed data next to replicated data sets (a direct display, §7.4.1) shows no obvious discrepancy: the replications reproduce the separation of the brands and the small spread within each.

Two concerns remain, conditional normality of the observations and constant variance between brands, though both are of limited concern here because the total sample size is fairly large and the design is balanced. Two test quantities address them.

1. *Normality.* Let $e_{ij}=y_{ij}-\theta_j$ be the residuals and $e_{(1)}\le e_{(2)}\le\cdots\le e_{(n)}$ their ordered values, $n=48$. Take

   $$
   T(y,\theta)=\operatorname{Corr}\Big(e_{(i)},\,\Phi^{-1}\Big(\frac{i-\frac12}{n}\Big)\Big),
   $$
   the correlation of the points in a **normal Q–Q plot** of the residuals. If the data are conditionally normal the correlation is close to $1$; non-linearity in the plot pulls it down. The histogram of $T(y^{\mathrm{rep},s},\theta^s)-T(y,\theta^s)$ is centered near $0$, so the observed data lie in the middle of what the model predicts, and $\hat p_B=0.53$.
2. *Equal variance.* Let $s_j^2$ be the sample variance of the observations of brand $j$. If the variances are equal, $T(y)=\max_js_j^2/\min_js_j^2$ should not be much larger than its replications. Here $\hat p_B=0.35$.

Neither check reveals a problem. Note that the normality check needs the parameters $\theta_j$, because the residuals are defined with respect to them: this is a test quantity that a classical test could only imitate by plugging in estimates.

## Summary

| Step | What is done | Key formula or tool |
|---|---|---|
| Purpose | decide whether the model needs improvement and in which direction | Box: all models are wrong; do the errors matter? |
| Sensitivity analysis (Definition 7.1.1) | refit with other reasonable models and compare inferences | super-model as the ideal, rarely feasible |
| External validation (Definition 7.2.1) | compare predictions with new data | needs new data; choose which predictions |
| Posterior predictive check (Definition 7.3.1) | compare $y$ with replications $y^{\mathrm{rep}}\sim p(y^{\mathrm{rep}}\mid y)$ | same design as $y$; differs from a future $\tilde y$ |
| Test quantity (Definition 7.3.2) | scalar $T(y,\theta)$ aimed at a feature the model does not fit directly | may depend on $\theta$; no sampling distribution needed |
| Posterior predictive p-value (Definition 7.3.3) | $p_B=\mathbb{P}(T(y^{\mathrm{rep}},\theta)\ge T(y,\theta)\mid y)$ | Algorithm 7.3.1; extreme near $0$ or $1$ |
| Graphical checks (§7.4) | data vs replications; scatterplot of $T(y,\theta^s)$ and $T(y^{\mathrm{rep},s},\theta^s)$ about the $45^\circ$ line | $\chi^2$ discrepancy as an omnibus measure |

- Posterior predictive checks resemble hypothesis tests but are not the same: $\theta$ is averaged over its posterior, $T$ may involve parameters, and the result is a probability about data sets, not about the truth of the model.
- An extreme p-value measures statistical, not practical, significance; it does not matter how extreme it is, and it is a starting point for improving the model. Several test quantities are used without a multiple-comparison adjustment.
- In the examples, independence failed for the binary sequence ($\hat p_B\approx0.98$ for the number of switches), normality failed at the extremes of Newcomb's data, a common tumor rate failed for the rats ($\hat p_B=0$) while the hierarchical model fitted ($\hat p_B\approx0.5$), and the beer model passed checks of normality and equal variance.

## Questions

1. In Example 7.3.1, use the test quantity $T(y)=\sum_iy_i$, the number of successes. Find the exact posterior predictive distribution of $T(y^{\mathrm{rep}})$ and the p-value. Why is this a poor choice of test quantity?

   **Answer** Given $\theta$, $\sum_iy_i^{\mathrm{rep}}\sim\mathrm{Bin}(20,\theta)$, and $\theta\mid y\sim\mathrm{Beta}(8,14)$, so $T(y^{\mathrm{rep}})\mid y\sim\mathrm{BetaBin}(20,8,14)$, with mean $20\cdot8/22=7.27$. Then $p_B=\mathbb{P}(T(y^{\mathrm{rep}})\ge7\mid y)=0.585$. The p-value is unremarkable, and it would be the same for any ordering of the $20$ values, including the strongly clustered one observed: $\sum y_i$ is a sufficient statistic, the very quantity the model fits, so it cannot detect a failure of independence. A useful test quantity measures a feature the model does not directly address, such as the number of switches.
2. In the rat tumor example, explain the difference between $y^{\mathrm{rep}}$ and a future observation $\tilde y$ by describing how to simulate each under the hierarchical model, and say which one is used for model checking.

   **Answer** For $y^{\mathrm{rep}}$, draw $(\alpha,\beta,\theta_1,\dots,\theta_{71})$ from the posterior and then $y_j^{\mathrm{rep}}\sim\mathrm{Bin}(n_j,\theta_j)$ for the same $71$ groups with the same sizes $n_j$: a replication of the whole experiment with the same tumor rates. For a new 72nd group of size $\tilde n$, draw $(\alpha,\beta)$ from the posterior, a new rate $\tilde\theta\sim\mathrm{Beta}(\alpha,\beta)$, and $\tilde y\sim\mathrm{Bin}(\tilde n,\tilde\theta)$. Model checking compares the observed data with $y^{\mathrm{rep}}$, which has exactly the structure of $y$; $\tilde y$ is used for prediction and, once observed, for external validation.
3. Show that if the test quantity depends on the data only, $p_B=\int p_C(\theta)\,p(\theta\mid y)\,\mathrm{d}\theta$, where $p_C(\theta)=\mathbb{P}(T(y^{\mathrm{rep}})\ge T(y)\mid\theta)$. What does this say about the relation between Bayesian and classical p-values?

   **Answer** In Definition 7.3.3 integrate first over $y^{\mathrm{rep}}$ for fixed $\theta$:

   $$
   p_B=\int\Big[\int\boldsymbol{1}\{T(y^{\mathrm{rep}})\ge T(y)\}\,p(y^{\mathrm{rep}}\mid\theta)\,\mathrm{d}y^{\mathrm{rep}}\Big]p(\theta\mid y)\,\mathrm{d}\theta=\int p_C(\theta)\,p(\theta\mid y)\,\mathrm{d}\theta.
   $$
   The Bayesian p-value is the classical p-value averaged over the posterior uncertainty about $\theta$, instead of being evaluated at a single null value or made independent of $\theta$ by a pivotal statistic. When $T$ is pivotal, $p_C$ does not depend on $\theta$ and the two coincide.
4. Let $y_1,\dots,y_n\overset{\text{iid}}{\sim}\mathcal{N}(\theta,\sigma^2)$ with $\sigma^2$ known and $p(\theta)\propto1$. Compute $p_B$ for $T(y)=\bar y$. What does the result illustrate?

   **Answer** The posterior is $\theta\mid y\sim\mathcal{N}(\bar y,\sigma^2/n)$, and given $\theta$, $\bar y^{\mathrm{rep}}\sim\mathcal{N}(\theta,\sigma^2/n)$, so $\bar y^{\mathrm{rep}}\mid y\sim\mathcal{N}(\bar y,2\sigma^2/n)$ by the **law of total variance**. Hence $p_B=\mathbb{P}(\bar y^{\mathrm{rep}}\ge\bar y\mid y)=0.5$ exactly, whatever the data. The model is fitted to $\bar y$, so the check cannot fail; it illustrates both the principle of §7.3.3 and Remark 7.3.1 (posterior predictive p-values pile up near $0.5$ for quantities that the fit uses).
5. Counts $y_1,\dots,y_n$ are modeled as $\mathrm{Poi}(\theta)$ with prior $\Gamma(\alpha,\beta)$. Propose a test quantity for overdispersion and describe the posterior predictive check step by step. What would a p-value of $0.002$ suggest, and what would you do next?

   **Answer** A Poisson model forces the variance to equal the mean, so take $T(y)=s_y^2/\bar y$, the ratio of the sample variance to the sample mean (close to $1$ under the model), or the $\chi^2$ discrepancy $T(y,\theta)=\sum_i(y_i-\theta)^2/\theta$. For $s=1,\dots,L$: draw $\theta^s\sim\Gamma(\alpha+\sum y_i,\beta+n)$, draw $y_1^{\mathrm{rep},s},\dots,y_n^{\mathrm{rep},s}\overset{\text{iid}}{\sim}\mathrm{Poi}(\theta^s)$, and record whether $T(y^{\mathrm{rep},s})\ge T(y)$; the proportion is $\hat p_B$. A value of $0.002$ means that the data are much more variable than Poisson replications: the counts are overdispersed. It does not matter whether it is $0.002$ or $0.0002$; the next step is a better model, for instance a hierarchical model with unit-specific rates $\theta_i\sim\Gamma(\alpha,\beta)$, which makes the counts negative binomial.
6. Why is the test quantity $\max_i\lvert y_i-\mu\rvert$ in Example 7.3.2 not available as a classical test statistic, and how is its p-value computed?

   **Answer** It depends on the unknown $\mu$, so it cannot be computed from the data alone, and its classical sampling distribution would depend on $(\mu,\sigma)$. In a posterior predictive check, for each posterior draw $(\mu^s,\sigma^s)$ we draw $y^{\mathrm{rep},s}$ of $66$ values from $\mathcal{N}(\mu^s,(\sigma^s)^2)$ and compare $\max_i\lvert y_i-\mu^s\rvert$ with $\max_i\lvert y_i^{\mathrm{rep},s}-\mu^s\rvert$; $\hat p_B$ is the proportion of draws in which the replication is at least as large. No distribution theory is needed. For Newcomb's data the realized value, driven by $-44$, exceeds almost all replicated values.
7. A model is checked with ten test quantities, and one of them has $\hat p_B=0.03$. Should the p-values be adjusted for multiple comparisons before drawing conclusions?

   **Answer** No adjustment is recommended. The purpose is not to decide, with a controlled Type I error rate, whether to accept or reject a model that we already know to be wrong, but to find in which respects it fails to reproduce the data. Each test quantity answers its own question, and a p-value of $0.03$ flags the corresponding feature for a closer look: is the misfit practically important for the scientific questions, and does a graphical check confirm a systematic discrepancy? Since posterior predictive p-values are conservative (Remark 7.3.1), a value this small deserves attention.
8. In the rat tumor example the common-rate model gives a mean realized discrepancy of about $143$ and a mean replicated discrepancy of about $71$. Explain why the replicated value is close to the number of groups, and why the realized value is so much larger.

   **Answer** Under the model, each term $(y_j^{\mathrm{rep}}-n_j\theta)^2/(n_j\theta(1-\theta))$ has expectation $\operatorname{Var}(y_j^{\mathrm{rep}}\mid\theta)/(n_j\theta(1-\theta))=1$, so the replicated discrepancy has mean $J=71$ for every $\theta$. The realized discrepancy evaluates the same sum with the observed counts. Because the true tumor rates differ between groups, $y_j-n_j\theta$ includes the deviation of the group rate from the common rate, $n_j(\theta_j-\theta)$, in addition to binomial noise, and the sum is roughly doubled. The hierarchical model lets each group have its own rate, which removes this extra variation.
