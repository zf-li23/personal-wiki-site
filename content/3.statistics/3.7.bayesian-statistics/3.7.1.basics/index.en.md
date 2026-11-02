---
title: Basics of Bayesian Inference
description: Three ways to understand probability, Bayes' rule as inverse probability and belief update, frequentist and Bayesian paradigms, the binomial model from Laplace's birth data, summaries of the posterior, prior and posterior odds, and conjugate Beta priors with the placenta previa example.
---

Data analysis is a pipeline: data requirements, collection, processing and cleaning, exploratory analysis, modeling and algorithms, and finally a data product that has to be communicated. At its center sits the statistical model, a device through which we make sense of what we observe. A model expresses knowledge quantitatively, describes how the data were collected, defines the quantities of interest and their connection with the data, and turns questions into formal problems with principled answers; it is then improved iteratively. A good model is reasonably behaved, as simple as possible, and faithful to the relevant scientific knowledge. The simplest example is a coin: $\mathbb{P}(\text{head}\mid\theta)=\theta$, $\mathbb{P}(\text{tail}\mid\theta)=1-\theta$, with parameter $\theta$ in the parameter space $[0,1]$.

Bayesian data analysis is the practice of building such models with probability distributions for all unknowns, conditioning on the observed data, and checking the result. This chapter lays the foundations: what probability means (§1.1), Bayes' rule (§1.2), how the Bayesian paradigm differs from the frequentist one (§1.3), the binomial model in full detail (§1.4), how a posterior is summarized (§1.5), and a first classification of priors, culminating in conjugate priors (§1.6). The introductory account in [3.2.7](/3.2.7) defines the basic objects; here they are developed at the depth needed for the rest of the course. The following chapters treat single-parameter models and non-informative priors ([3.7.2](/3.7.2)), models with several parameters ([3.7.3](/3.7.3)), the distributions that appear along the way ([3.7.4](/3.7.4)), simulation and large-sample theory ([3.7.5](/3.7.5)), hierarchical models ([3.7.6](/3.7.6)), and the checking and comparison of models ([3.7.7](/3.7.7), [3.7.8](/3.7.8)).

## 1.1. Three Ways to Understand Probability

*Long-run relative frequencies.* If an experiment consisting of independent trials is repeated over and over, the relative frequency of an event approaches its probability. Let $A$ be the event of interest with $p=\mathbb{P}(A)$, let $Y_i=\boldsymbol{1}\{A\text{ occurs in trial }i\}$ and $X_n=\sum_{i=1}^nY_i$. By the **law of large numbers**,

$$
\frac{X_n}{n}\to p,\qquad n\to\infty.
$$

Three famous coin-tossing experiments illustrate the convergence toward $\mathbb{P}(\text{head})=0.5$:

| Experimenter | Tosses | Heads | $\hat p$ |
|---|---|---|---|
| Count Buffon | 4040 | 2048 | 0.5069 |
| John Kerrich (while interned during the Second World War) | 10000 | 5067 | 0.5067 |
| Karl Pearson | 24000 | 12012 | 0.5005 |

*Models and physical understanding.* The structure of a problem often suggests a probability model. The physics of a tossed coin suggests that neither side is favored, so the two outcomes are equally likely; the long-run frequencies can then be used to verify the model rather than to define it.

*Subjective beliefs.* Many events of interest cannot be repeated, such as the result of next year's final between two particular teams. A degree of belief can still be quantified by comparison with standard events (is the win more or less likely than a head on one toss, or a six on a fair die?) or by comparing outcomes with each other ("1.5 times as likely as …"). Such beliefs are often expressed as odds,

$$
\text{odds}=\frac{\mathbb{P}}{1-\mathbb{P}},\qquad \mathbb{P}=\frac{\text{odds}}{1+\text{odds}}.
$$

The three views are not exclusive. Bayesian inference uses probability in all three senses, but its distinctive feature is that the third view applies to parameters as well: a parameter about which we are uncertain gets a probability distribution.

## 1.2. Bayes' Rule

For random quantities $X$ and $Y$, **Bayes' theorem** reads, for a continuous $X$,

$$
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}=\frac{f_{Y\mid X}(y\mid x)f_X(x)}{\int_{\Omega_X}f_{Y\mid X}(y\mid x')f_X(x')\,\mathrm{d}x'},
$$
and for a discrete $X$ the integral becomes a sum, $\mathbb{P}(x\mid y)=\mathbb{P}(y\mid x)\mathbb{P}(x)\big/\sum_{x'}\mathbb{P}(y\mid x')\mathbb{P}(x')$. Following the usual practice in Bayesian statistics, we write $p(\cdot)$ for every density or probability mass function and let the arguments tell which one is meant: $p(\theta)$, $p(y\mid\theta)$, $p(\theta\mid y)$. Probabilities of events are written $\mathbb{P}(\cdot)$. We mostly write the continuous version; the discrete one is analogous.

The rule can be read in two ways.

1. *Inverse probability*: from $p(y\mid x)$, the probability of the effect given the cause, to $p(x\mid y)$, the probability of the cause given the effect. This is how Bayes and Laplace used it.
2. *Belief update*: from $p(x)$, the belief before seeing $y$, to $p(x\mid y)$, the belief after seeing $y$.

The second reading is the one that turns the rule into a method of inference. It applies even to historical questions: the only known portrait said to show Thomas Bayes has no documented source, and whether it really shows him is a probability that changes as evidence about its caption and the clothing in it is weighed.

**Example 1.2.1 (Spelling Correction)** A user types "radom". Which word $\theta$ was intended: $\theta_1$ = random, $\theta_2$ = radon, or $\theta_3$ = radom (a rare word, kept as typed)? The prior $p(\theta)$ comes from word frequencies in a large corpus, and the likelihood $p(\text{"radom"}\mid\theta)$ from a model of typing errors:

| $\theta$ | $p(\theta)$ | $p(\text{"radom"}\mid\theta)$ | $p(\theta)p(\text{"radom"}\mid\theta)$ | $p(\theta\mid\text{"radom"})$ |
|---|---|---|---|---|
| random | $7.60\times10^{-5}$ | $0.00193$ | $1.47\times10^{-7}$ | $0.325$ |
| radon | $6.05\times10^{-6}$ | $0.000143$ | $8.65\times10^{-10}$ | $0.002$ |
| radom | $3.12\times10^{-7}$ | $0.975$ | $3.04\times10^{-7}$ | $0.673$ |

The posterior is the product normalized by its sum, $p(\theta_1\mid\text{"radom"})=p(\theta_1)p(\text{"radom"}\mid\theta_1)\big/\sum_{j=1}^3p(\theta_j)p(\text{"radom"}\mid\theta_j)$. The rare word wins because a typist who means "radom" almost always types it correctly, while "random" is mistyped this way only about twice in a thousand times. If the prior came from documents about statistics, "random" would be far more frequent and would win.

## 1.3. Two Paradigms of Inference

Three schools have shaped statistical inference: the frequentist (Neyman–Pearson), the Fisherian (likelihood-based) and the Bayesian. We contrast the first and the last, which differ in what they treat as random.

### 1.3.1. The Frequentist Paradigm

Frequentist inference treats model parameters as unknown but fixed constants. Its main tools are point estimation (a statistic $S=f(\text{data})$), interval estimation (an interval $[a,b]$ with $a=f_1(\text{data})<b=f_2(\text{data})$) and **hypothesis testing** ($H_0\colon\theta=\theta_0$ against $H_1\colon\theta=\theta_1$). All of them are interpreted through a hypothetical sequence of repeated experiments: a $95\%$ **confidence interval** is produced by a procedure that covers the true value in $95\%$ of the repetitions.

This interpretation has limitations.

- It needs the hypothetical repetitions, which may not exist.
- Uncertainty is quantified for a population of cases. A patient asks "what is the success rate of my surgery?" and the doctor answers "95%, based on my history": the answer refers to past patients like this one.
- Logically it cannot quantify uncertainty about a specific data set, yet decisions are always made for a particular data set, which is unique (nobody is exactly like this patient). In this sense it may give a correct answer to the wrong question.

A modified coin example shows the difference between the frequency view and the other two. Someone is handed, at random, either a double-headed or a double-tailed coin and tosses it. Is $\mathbb{P}(\text{head})=0.5$? The symmetry argument still works: by symmetry of our ignorance about which coin we hold, head and tail are equally likely. The frequency argument breaks down: repeated tosses of the coin in hand give all heads or all tails, never a relative frequency near $0.5$.

### 1.3.2. The Bayesian Paradigm

Bayesian inference treats unknowns, in particular model parameters, as random variables. Its main elements are

- the **prior distribution** $p(\theta)$;
- the likelihood, or sampling distribution, $p(y\mid\theta)$, which as a function of $\theta$ is the **likelihood function**;
- the joint distribution $p(y,\theta)=p(\theta)p(y\mid\theta)$;
- the **posterior distribution** $p(\theta\mid y)=p(y,\theta)/p(y)$.

**Bayesian inference** then describes the quantities of scientific interest with probabilities, lets the rules of probability work out their consequences, and summarizes all uncertainty in the posterior distribution. Two further distributions describe observable quantities rather than parameters.

**Definition 1.3.1 (Prior Predictive Distribution)** The **prior predictive distribution** of the data $y$ is its marginal distribution under the model,

$$
p(y)=\int p(y,\theta)\,\mathrm{d}\theta=\int p(\theta)p(y\mid\theta)\,\mathrm{d}\theta.
$$
Evaluated at the observed data it is the **marginal likelihood**, the normalizing constant of the posterior. After $y$ has been observed, an unknown observable $\tilde y$ from the same process, conditionally independent of $y$ given $\theta$, has the **posterior predictive distribution**

$$
p(\tilde y\mid y)=\int p(\tilde y,\theta\mid y)\,\mathrm{d}\theta=\int p(\tilde y\mid\theta)p(\theta\mid y)\,\mathrm{d}\theta.
$$

The prior predictive distribution says what data we expect before the experiment; the posterior predictive distribution says what new data we expect after it. Both are averages of the sampling distribution, over the prior and over the posterior respectively. The second equality for $p(\tilde y\mid y)$ uses $p(\tilde y\mid\theta,y)=p(\tilde y\mid\theta)$, the **conditional independence** of $\tilde y$ and $y$ given $\theta$.

The generic scheme of a Bayesian analysis therefore has three steps:

1. set up a full probability model, a joint distribution $p(y,\theta)=p(\theta)p(y\mid\theta)$ for all observable and unobservable quantities, consistent with the knowledge about the problem and the data collection;
2. condition on the observed data: compute the posterior $p(\theta\mid y)\propto p(\theta)p(y\mid\theta)$, and predictions $p(\tilde y\mid y)$;
3. evaluate the fit of the model and the reasonableness of the conclusions, and if necessary revise the model ([3.7.7](/3.7.7)).

### 1.3.3. Comparing the Paradigms

Picture the joint distribution $p(y,\theta)$ on a plane with $\theta$ on one axis and $y$ on the other. Bayesian inference proceeds vertically: it fixes the observed $y$ and looks at the conditional distribution $p(\theta\mid y)$ along that line, which requires a prior $p(\theta)$. Frequentist inference proceeds horizontally: it fixes $\theta$ and studies the sampling distribution $p(y\mid\theta)$ of a method $t(y)$ designed to answer the specific question at hand. A Bayesian analysis answers all possible questions at once, since every question about $\theta$ is a question about one posterior distribution; the frequentist approach needs a separate estimator or test for each question, which is more work but allows a more intense inspection of particular problems.

| | Frequentist | Bayesian |
|---|---|---|
| parameter | fixed unknown constant | random variable with a prior |
| conditioning | on $\theta$; averages over hypothetical data | on the observed $y$ |
| uncertainty statement | about the procedure | about $\theta$ given these data |
| main requirement | a procedure $t(y)$ for each question | a prior $p(\theta)$ |
| answers | one question per procedure | all questions from one posterior |

The Bayesian approach answers the questions researchers usually ask ("what is the probability that …"); almost every frequentist method has a Bayesian counterpart; prior information and information from several studies or a sequence of data are combined by one consistent rule; complicated structured problems (hierarchical, missing data, latent variables) are handled within the same framework; and powerful simulation methods support the computation. The critical issue is the choice of the prior, the alleged subjectivity of the approach.

That criticism should be put in proportion. Every statistical method that uses probability is subjective in the sense that it relies on mathematical idealizations of the world, and in most problems scientific judgment is needed to specify both the likelihood and the prior. A linear regression model, for example, is generally at least as suspect as any prior distribution that might be assumed for its coefficients. What a Bayesian analysis adds is that the assumptions about the parameters are stated explicitly and can be checked and varied ([3.7.7](/3.7.7)).

## 1.4. The Binomial Model

**Example 1.4.1 (Laplace's Birth Data)** In 1786 Laplace asked whether the proportion of boys among births in Paris exceeds $0.5$. From 1745 to 1770 there were $251527$ boys and $241945$ girls. Assume the births are independent Bernoulli trials with probability $\theta$ of a boy, so that the number $y$ of boys among $n$ births satisfies $y\mid\theta\sim\mathrm{Bin}(n,\theta)$:

$$
p(y\mid\theta)=\binom ny\theta^y(1-\theta)^{n-y},\qquad\theta\in[0,1].
$$
The sample size $n$ is fixed by the design, and we drop it from the conditioning for brevity. Following Bayes, take the uniform prior $\theta\sim\mathrm{U}(0,1)$, $p(\theta)=1$ on $[0,1]$. Then

$$
\begin{aligned}
p(y,\theta)&=\binom ny\theta^y(1-\theta)^{n-y},\\
p(y)&=\int_0^1\binom ny\theta^y(1-\theta)^{n-y}\,\mathrm{d}\theta=\binom ny\mathrm{B}(y+1,n-y+1)=\binom ny\frac{y!\,(n-y)!}{(n+1)!}=\frac{1}{n+1},\\
p(\theta\mid y)&=(n+1)\binom ny\theta^y(1-\theta)^{n-y}.
\end{aligned}
$$
Under the uniform prior every count $y=0,1,\dots,n$ is a priori equally likely, which is how Bayes motivated the prior. The posterior is a **beta distribution**: the $\mathrm{Beta}(\alpha,\beta)$ density is $\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\theta^{\alpha-1}(1-\theta)^{\beta-1}$, and here

$$
\theta\mid y\sim\mathrm{Beta}(y+1,\,n-y+1).
$$
We write both $\theta\sim\mathrm{Beta}(\alpha,\beta)$ and, for the density as a function of $\theta$, $\mathrm{Beta}(\theta\mid\alpha,\beta)$. With Laplace's data the posterior is $\mathrm{Beta}(251528,241946)$, with mean $0.5097$, and

$$
\mathbb{P}(\theta\le0.5\mid y)\approx1.15\times10^{-42},
$$
so Laplace concluded that the boy birth rate in Paris is above $0.5$ with practical certainty.

The computation did not need $p(y)$. It is usually easier to work with the proportional form of Bayes' rule,

$$
p(\theta\mid y)\propto p(\theta)p(y\mid\theta),
$$
and to recognize the kernel of a known distribution. Here $p(\theta\mid y)\propto1\times\theta^y(1-\theta)^{n-y}$, the kernel of $\mathrm{Beta}(y+1,n-y+1)$; the normalizing constant follows from the known density.

The shape of the posterior follows the data. For $y=0$ the density decreases from its maximum at $\theta=0$; for $y=n$ it increases to its maximum at $\theta=1$; in between it is unimodal with mode $y/n$, skewed toward the nearer end when $y<n/2$ or $y>n/2$, and symmetric about $0.5$ when $y=n/2$. For a fixed observed proportion it concentrates around $y/n$ as $n$ grows, with standard deviation of order $1/\sqrt n$.

![Uniform-prior posteriors Beta(y + 1, n − y + 1). Left: n = 10 and different counts y. Right: a fixed observed proportion 0.3 with growing n; the posterior concentrates around 0.3.](./plots/binomial_posteriors.py)

Data enter only through the likelihood. Suppose we record the sexes of 8 children one by one and obtain either sample A $=(1,1,1,0,1,0,1,0)$ or sample B $=(0,0,1,0,1,1,1,1)$, where $1$ denotes a boy. Both have likelihood $\theta^5(1-\theta)^3$, so they give the same posterior. Bayesian analysis satisfies the **likelihood principle** ([Definition 7.1.1](/3.2.7#def-7.1.1)): two data sets $x,y$ whose likelihood functions are proportional, $L_x(\theta)=c\,L_y(\theta)$ for all $\theta\in\Theta$, lead to the same inferences, since the constant $c$ cancels on normalizing. Only the data actually observed enter, through their likelihood; data that could have been observed but were not play no role.

Evidence often arrives in stages. Does the order in which it is processed matter, and does updating step by step agree with a single update on all the data?

**Proposition 1.4.1** Let $y_1$ and $y_2$ be conditionally independent given $\theta$. Then

$$
p(\theta\mid y_1,y_2)\propto p(\theta\mid y_1)\,p(y_2\mid\theta),
$$
that is, the posterior after $y_1$ serves as the prior for $y_2$. The result is the same as the one-step posterior from $p(\theta)$ and $(y_1,y_2)$, and the same as updating first with $y_2$ and then with $y_1$.

**Proof** By conditional independence $p(y_1,y_2\mid\theta)=p(y_1\mid\theta)p(y_2\mid\theta)$, so

$$
p(\theta\mid y_1,y_2)\propto p(\theta)p(y_1\mid\theta)p(y_2\mid\theta)\propto p(\theta\mid y_1)p(y_2\mid\theta).
$$
The middle expression is symmetric in $y_1$ and $y_2$. $\square$

For the binomial model with prior $\mathrm{Beta}(\alpha,\beta)$, a first batch of $n_1$ trials with $y_1$ successes gives $\mathrm{Beta}(\alpha+y_1,\beta+n_1-y_1)$, and a second batch then gives $\mathrm{Beta}(\alpha+y_1+y_2,\beta+n_1+n_2-y_1-y_2)$, exactly the posterior from all $n_1+n_2$ trials at once.

Finally, under the uniform prior, the posterior predictive probability that the next trial is a success is

$$
\mathbb{P}(\tilde y=1\mid y)=\int_0^1\theta\,p(\theta\mid y)\,\mathrm{d}\theta=\mathbb{E}(\theta\mid y)=\frac{y+1}{n+2},
$$
Laplace's rule of succession. Even after $n$ successes in $n$ trials the predicted probability of another success is $\frac{n+1}{n+2}<1$.

## 1.5. Summarizing the Posterior

The posterior distribution is the complete answer of a Bayesian analysis, but it is usually reported through a few summaries, and the classical inference problems reappear as questions about it.

- Location: the **posterior mean** $\mathbb{E}(\theta\mid y)$, the **posterior median**, and the posterior mode or modes; the mode is the **maximum a posteriori estimate** (MAP). These are the Bayesian point estimates.
- Variation: the posterior standard deviation, the interquartile range and other **quantiles**.
- Intervals: the Bayesian counterpart of a confidence interval is a **credible interval**, a region that contains $\theta$ with a stated posterior probability.

For a skewed posterior the three location summaries differ; for the binomial posterior $\mathrm{Beta}(y+1,n-y+1)$ they are $\frac{y+1}{n+2}$ (mean), $\frac yn$ (mode) and a median between the two. Two kinds of credible region are in common use.

**Definition 1.5.1 (Central Posterior Interval)** Let $0<\alpha<1$. The $100(1-\alpha)\%$ **central posterior interval** for a real parameter $\theta$ is the interval between the $\alpha/2$ and $1-\alpha/2$ quantiles of $p(\theta\mid y)$, so that each tail outside it has posterior probability $\alpha/2$. A $100(1-\alpha)\%$ **highest posterior density** region is the set $\{\theta\colon p(\theta\mid y)\ge k\}$ with $k$ chosen so that its posterior probability is $1-\alpha$.

The central interval is easy to compute from quantiles, or from simulation draws by their empirical quantiles, and it is invariant under monotone transformations: if $\phi=h(\theta)$ with $h$ increasing, the central interval for $\phi$ is the image of the one for $\theta$. The HPD region has the property that every point inside it has higher posterior density than every point outside, so it is the smallest region with the given probability; it is not invariant under nonlinear transformations, and for a multimodal posterior it may consist of several disjoint intervals, which describes such a posterior better than a single central interval that includes a valley of low density. For a symmetric unimodal posterior the two coincide.

![For a bimodal posterior the 95% central interval contains the low-density valley between the modes, while the 95% HPD region consists of two intervals above the density level shown dotted.](./plots/central_vs_hpd.py)

When $\theta$ takes only two values $\theta_1,\theta_2$, hypothesis testing becomes a comparison of their posterior probabilities. One can compute $p(\theta_i\mid y)$ for $i=1,2$ directly; it is often simpler to work with odds.

**Definition 1.5.2 (Prior and Posterior Odds)** For two parameter values (or hypotheses) $\theta_1,\theta_2$, the **prior odds** of $\theta_1$ against $\theta_2$ are $p(\theta_1)/p(\theta_2)$, and the **posterior odds** are $p(\theta_1\mid y)/p(\theta_2\mid y)$.

**Proposition 1.5.1** Posterior odds equal prior odds times the **likelihood ratio**:

$$
\frac{p(\theta_1\mid y)}{p(\theta_2\mid y)}=\frac{p(\theta_1)p(y\mid\theta_1)}{p(\theta_2)p(y\mid\theta_2)}=\frac{p(\theta_1)}{p(\theta_2)}\cdot\frac{L(\theta_1\mid y)}{L(\theta_2\mid y)}.
$$

**Proof** Write both posteriors by Bayes' rule; the marginal $p(y)$ cancels in the ratio. $\square$

The likelihood ratio is the factor by which the data change the odds; for composite hypotheses its analogue is the **Bayes factor** ([3.7.8](/3.7.8)).

**Example 1.5.1** Observe $y=1$ success in $n=5$ trials, where it is known that $\theta=0.1$ or $\theta=0.2$. The likelihoods are

$$
\mathbb{P}(y=1\mid\theta=0.1)=5\cdot0.1\cdot0.9^4=0.328,\qquad \mathbb{P}(y=1\mid\theta=0.2)=5\cdot0.2\cdot0.8^4=0.410.
$$
With equal prior probabilities $0.5$, the posterior odds of $\theta=0.1$ against $\theta=0.2$ equal the likelihood ratio $0.801$, so $\mathbb{P}(\theta=0.1\mid y)=0.445$ and $\mathbb{P}(\theta=0.2\mid y)=0.555$. The data slightly favor $\theta=0.2$, and the answer does not depend on which value is called the null hypothesis.

A frequentist test treats the two values asymmetrically.

- $H_0\colon\theta=0.1$ against $H_1\colon\theta=0.2$: large $y$ is evidence against $H_0$, and the **p-value** is $\mathbb{P}(y\ge1\mid\theta=0.1)=1-0.9^5=0.410$.
- $H_0\colon\theta=0.2$ against $H_1\colon\theta=0.1$: now small $y$ is evidence against $H_0$, and the p-value is $\mathbb{P}(y\le1\mid\theta=0.2)=0.8^5+5\cdot0.2\cdot0.8^4=0.737$.

Neither test rejects, and the two p-values answer different questions about hypothetical data; neither is the probability of a hypothesis. The posterior probabilities directly state how plausible each value is given the one data set observed.

## 1.6. Specifying the Prior (I): Conjugate Priors

### 1.6.1. Interpretations and Classes of Priors

There are two ways to interpret a prior distribution.

- The population interpretation: the prior represents a population of possible parameter values from which the $\theta$ of current interest has been drawn, for example the sex ratios of many comparable populations.
- The state-of-knowledge interpretation: we express our knowledge and uncertainty about $\theta$ as if its value were a random realization from the prior. This is the more subjective reading and the one needed when no population exists.

Priors are classified by how much they say about $\theta$.

**Definition 1.6.1 (Classes of Priors)** An **informative prior** encodes substantial knowledge about $\theta$, from earlier data or from scientific understanding. A **weakly informative prior** encodes only a little knowledge, for instance the order of magnitude of $\theta$, enough to rule out implausible values while letting the data dominate. A **non-informative prior** is meant to express no knowledge and to play a minimal role in the posterior ([3.7.2](/3.7.2)).

A general principle holds for all classes: the prior should include all plausible values of $\theta$. Wherever $p(\theta)=0$, also $p(\theta\mid y)\propto p(\theta)p(y\mid\theta)=0$, whatever the data say.

### 1.6.2. Conjugate Priors

The uniform prior in the binomial model gave a Beta posterior. More generally, a Beta prior gives a Beta posterior, which is the defining property of conjugacy.

**Definition 1.6.2 (Conjugate Prior)** Let $\mathcal{F}$ be a class of sampling distributions $p(y\mid\theta)$ and $\mathcal{P}$ a class of prior distributions for $\theta$. The class $\mathcal{P}$ is conjugate for $\mathcal{F}$ if

$$
p(\theta\mid y)\in\mathcal{P}\quad\text{for all }p(\cdot\mid\theta)\in\mathcal{F}\text{ and }p(\cdot)\in\mathcal{P}.
$$
A member of $\mathcal{P}$ is then a **conjugate prior** for the model.

Conjugate priors have two practical advantages. Computation is convenient, because prior and posterior have the same form and updating only changes parameters. And they are easy to interpret, because the prior acts like additional data. Conjugacy as defined is neither unique nor automatic. It is not unique: the class of all distributions is trivially conjugate, and finite mixtures of conjugate priors again form a conjugate class (Proposition 1.6.1 below); one usually means the natural conjugate family, the smallest family with the same functional form as the likelihood. As for existence, every exponential family has a natural conjugate family ([3.7.2](/3.7.2), §2.5), and apart from irregular cases such as the uniform $\mathrm{U}(0,\theta)$ model only exponential families do.

Consider now the Beta–binomial model. Take the prior $\theta\sim\mathrm{Beta}(\alpha,\beta)$, $p(\theta)\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$. The parameters $\alpha,\beta$ of a prior are called *hyperparameters*; they control the shape of the prior. With $y\mid\theta\sim\mathrm{Bin}(n,\theta)$,

$$
p(\theta\mid y)\propto\theta^y(1-\theta)^{n-y}\,\theta^{\alpha-1}(1-\theta)^{\beta-1}=\theta^{y+\alpha-1}(1-\theta)^{n-y+\beta-1},
$$
so

$$
\theta\mid y\sim\mathrm{Beta}(\alpha+y,\,\beta+n-y).
$$
The update adds the number of successes to $\alpha$ and the number of failures to $\beta$. Relative to the uniform prior $\mathrm{Beta}(1,1)$, the prior $\mathrm{Beta}(\alpha,\beta)$ is therefore worth $\alpha-1$ prior successes and $\beta-1$ prior failures, a prior sample of size $\alpha+\beta-2$; relative to the improper limit $\mathrm{Beta}(0,0)$ ([3.7.2](/3.7.2)) it is worth $\alpha$ successes and $\beta$ failures, a prior sample size $\alpha+\beta$. The posterior moments are

$$
\mathbb{E}(\theta\mid y)=\frac{\alpha+y}{\alpha+\beta+n},\qquad
\operatorname{Var}(\theta\mid y)=\frac{(\alpha+y)(\beta+n-y)}{(\alpha+\beta+n)^2(\alpha+\beta+n+1)}=\frac{\mathbb{E}(\theta\mid y)\,[1-\mathbb{E}(\theta\mid y)]}{\alpha+\beta+n+1},
$$
and for $\alpha+y>1$, $\beta+n-y>1$ the MAP is $\frac{\alpha+y-1}{\alpha+\beta+n-2}$. The MAP equals the **maximum likelihood estimator** $y/n$ for every data set only when $\alpha=\beta=1$, the uniform prior, under which the posterior is proportional to the likelihood.

The posterior mean has an instructive decomposition:

$$
\frac{\alpha+y}{\alpha+\beta+n}=\frac{n}{\alpha+\beta+n}\cdot\frac yn+\frac{\alpha+\beta}{\alpha+\beta+n}\cdot\frac{\alpha}{\alpha+\beta}.
$$
It is a weighted average of the observed proportion $y/n$ and the prior mean $\alpha/(\alpha+\beta)$, with weights proportional to the sample size $n$ and the prior sample size $\alpha+\beta$: the posterior is a compromise between data and prior. As $n\to\infty$ with $y/n$ fixed, the weight of the prior vanishes, the posterior mean tends to $y/n$, and the posterior variance, of order $\frac{(y/n)(1-y/n)}{n}$, tends to $0$. The prior predictive distribution of $y$ is the **beta-binomial distribution** $p(y)=\binom ny\mathrm{B}(\alpha+y,\beta+n-y)/\mathrm{B}(\alpha,\beta)$, which reduces to $1/(n+1)$ for $\alpha=\beta=1$.

Any prior that is not conjugate to the sampling distribution is non-conjugate. They are needed because conjugate priors may not exist for complicated models, or a simple conjugate density may not express the available knowledge; conceptually they pose no problem, only the computation is harder (one-dimensional problems can always be handled on a grid, [3.7.5](/3.7.5)). A convenient middle way is a mixture of conjugate priors, which remains computable in closed form.

**Proposition 1.6.1 (Mixtures of Conjugate Priors)** If $p(\theta)=\sum_{k=1}^Kw_kp_k(\theta)$ with conjugate components $p_k$ and weights $w_k\ge0$, $\sum_kw_k=1$, then

$$
p(\theta\mid y)=\sum_{k=1}^Kw_k'\,p_k(\theta\mid y),\qquad w_k'=\frac{w_km_k(y)}{\sum_jw_jm_j(y)},\qquad m_k(y)=\int p(y\mid\theta)p_k(\theta)\,\mathrm{d}\theta,
$$
where $p_k(\theta\mid y)$ is the posterior under the prior $p_k$ alone. For the binomial model with $p_k=\mathrm{Beta}(\alpha_k,\beta_k)$, $m_k(y)=\binom ny\mathrm{B}(\alpha_k+y,\beta_k+n-y)/\mathrm{B}(\alpha_k,\beta_k)$.

**Proof** $p(y\mid\theta)p(\theta)=\sum_kw_kp(y\mid\theta)p_k(\theta)=\sum_kw_km_k(y)p_k(\theta\mid y)$; integrating over $\theta$ gives $p(y)=\sum_kw_km_k(y)$, and dividing gives the claim. $\square$

Each component is updated as usual, and its weight is updated in proportion to how well that component predicted the data.

### 1.6.3. Example: Girl Births with Placenta Previa

**Example 1.6.1 (Placenta Previa)** Placenta previa is a condition of pregnancy in which the placenta is implanted low in the uterus. In the general population of Germany the proportion of girls among births is $0.485$. A study of placenta previa births in Germany found $437$ girls among $n=980$ births, an observed proportion $0.446$. Is the proportion $\theta$ of girls among placenta previa births lower than in the general population? Consider three kinds of prior.

1. *Uniform prior.* The posterior is $\mathrm{Beta}(438,544)$, with mean $0.446$, standard deviation $0.016$ and $95\%$ central posterior interval $[0.415,0.477]$. The value $0.485$ lies outside the interval, and $\mathbb{P}(\theta\ge0.485\mid y)=0.007$. With a posterior this close to normal, the population value is about $2.5$ posterior standard deviations above the posterior mean.
2. *Beta priors.* The impression that placenta previa births are like the general population, based on roughly 20 earlier cases, can be expressed by a Beta prior with prior sample size about 20. For example $p(\theta)\propto\theta^9(1-\theta)^{11}$, that is $\mathrm{Beta}(10,12)$, corresponds to 9 girls and 11 boys seen on top of the uniform prior; the posterior $\mathrm{Beta}(447,554)$ has mean $0.447$ and $95\%$ interval $[0.416,0.477]$, practically unchanged. Fixing the prior mean at $0.485$ and varying the prior sample size $\alpha+\beta$ gives

   | $\frac{\alpha}{\alpha+\beta}$ | $\alpha+\beta$ | posterior median | $95\%$ posterior interval |
   |---|---|---|---|
   | 0.500 | 2 | 0.446 | $[0.415, 0.477]$ |
   | 0.485 | 2 | 0.446 | $[0.415, 0.477]$ |
   | 0.485 | 5 | 0.446 | $[0.415, 0.477]$ |
   | 0.485 | 10 | 0.446 | $[0.415, 0.477]$ |
   | 0.485 | 20 | 0.447 | $[0.416, 0.478]$ |
   | 0.485 | 100 | 0.450 | $[0.420, 0.479]$ |
   | 0.485 | 200 | 0.453 | $[0.424, 0.481]$ |

   Only when the prior is worth a sizable fraction of the 980 observations does it pull the posterior noticeably toward $0.485$, and even with $\alpha+\beta=200$ the interval excludes $0.485$.
3. *A non-conjugate prior.* Concentrate prior belief near the population value without excluding anything: take a density that puts half of its mass uniformly on $[0,1]$ and the other half on a triangle centered at $0.485$ on $[0.385,0.585]$, so that $40\%$ of the prior mass lies outside $[0.385,0.585]$. The posterior has no closed form but is easily computed on a grid; its median is $0.449$ and its $95\%$ central interval $[0.419,0.480]$.

![Placenta previa example. Left: the non-conjugate prior (half uniform, half triangular around 0.485). Middle: posteriors under the uniform and the non-conjugate prior. Right: posteriors under conjugate priors with mean 0.485 and prior sample size α + β from 2 to 1000; the dotted line marks 0.485.](./plots/placenta_previa.py)

Different priors lead to different posteriors, but with a sample of $980$ births the conclusions agree: the proportion of girls among placenta previa births is lower than $0.485$. The prior matters when its prior sample size is comparable to $n$, which is when the prior information is genuinely as strong as the data.

### 1.6.4. Posterior Versus Prior Information

How much do we expect to learn from data? Averaged over the prior predictive distribution of the data, the posterior is related to the prior by two identities.

**Proposition 1.6.2** For any parameter $\theta$ with finite variance, with expectations taken over the joint distribution $p(\theta,y)$,

$$
\mathbb{E}(\theta)=\mathbb{E}\big[\mathbb{E}(\theta\mid y)\big],\qquad
\operatorname{Var}(\theta)=\mathbb{E}\big[\operatorname{Var}(\theta\mid y)\big]+\operatorname{Var}\big[\mathbb{E}(\theta\mid y)\big].
$$
In particular $\mathbb{E}[\operatorname{Var}(\theta\mid y)]\le\operatorname{Var}(\theta)$.

**Proof** These are the **law of total expectation** and the **law of total variance** ([3.1.9](/3.1.9)) applied to $\theta$ conditioned on $y$; the inequality follows because $\operatorname{Var}[\mathbb{E}(\theta\mid y)]\ge0$. $\square$

The prior mean is the average of all possible posterior means over the distribution of possible data. The posterior variance is on average smaller than the prior variance, by an amount equal to the variation of the posterior means over the possible data: the more the posterior mean is expected to move, the more the data are expected to reduce our uncertainty. The statement is about averages. For a particular data set the posterior variance can exceed the prior variance, when the data conflict with a confident prior (Question 4).

## Summary

| Item | Content |
|---|---|
| probability | long-run frequency, symmetry or physical model, subjective belief (odds $=\mathbb{P}/(1-\mathbb{P})$) |
| Bayes' rule | $p(\theta\mid y)=p(\theta)p(y\mid\theta)/p(y)\propto p(\theta)p(y\mid\theta)$; inverse probability and belief update |
| elements | prior $p(\theta)$, likelihood $p(y\mid\theta)$, joint $p(y,\theta)$, posterior $p(\theta\mid y)$ |
| predictive distributions | prior predictive $p(y)=\int p(\theta)p(y\mid\theta)\,\mathrm{d}\theta$; posterior predictive $p(\tilde y\mid y)=\int p(\tilde y\mid\theta)p(\theta\mid y)\,\mathrm{d}\theta$ (Definition 1.3.1) |
| paradigms | frequentist: $\theta$ fixed, averages over hypothetical data ("horizontal"); Bayesian: $\theta$ random, conditions on the observed data ("vertical") |
| binomial, uniform prior | $\theta\mid y\sim\mathrm{Beta}(y+1,n-y+1)$, $p(y)=\frac1{n+1}$, $\mathbb{P}(\tilde y=1\mid y)=\frac{y+1}{n+2}$; likelihood principle; sequential updating (Proposition 1.4.1) |
| summaries | mean, median, mode (MAP); sd, quantiles; central interval vs HPD region (Definition 1.5.1); posterior odds = prior odds × likelihood ratio (Proposition 1.5.1) |
| prior classes | informative, weakly informative, non-informative (Definition 1.6.1); include all plausible values |
| conjugacy | Definition 1.6.2; $\mathrm{Beta}(\alpha,\beta)\to\mathrm{Beta}(\alpha+y,\beta+n-y)$; posterior mean = weighted average of $y/n$ and $\frac{\alpha}{\alpha+\beta}$ with weights $n$ and $\alpha+\beta$; mixtures of conjugate priors (Proposition 1.6.1) |
| learning from data | $\mathbb{E}\theta=\mathbb{E}[\mathbb{E}(\theta\mid y)]$, $\operatorname{Var}\theta=\mathbb{E}[\operatorname{Var}(\theta\mid y)]+\operatorname{Var}[\mathbb{E}(\theta\mid y)]$ (Proposition 1.6.2) |

With a large sample the choice among reasonable priors hardly matters, as the placenta previa example shows (Example 1.6.1); with little data or many parameters it matters a great deal, which is why priors are studied systematically in [3.7.2](/3.7.2) and [3.7.6](/3.7.6).

## Questions

1. With the prior $\theta\sim\mathrm{Beta}(2,2)$ we observe $y=7$ successes in $n=10$ binomial trials. Find the posterior, its mean, mode and variance, and write the posterior mean as a weighted average of the sample proportion and the prior mean.

   **Answer** The posterior is $\mathrm{Beta}(2+7,2+3)=\mathrm{Beta}(9,5)$. Its mean is $9/14=0.643$, its mode $(9-1)/(14-2)=0.667$, and its variance $\frac{9\cdot5}{14^2\cdot15}=0.0153$ (standard deviation $0.124$). The weights are $n/(\alpha+\beta+n)=10/14$ and $(\alpha+\beta)/(\alpha+\beta+n)=4/14$: $\frac{10}{14}\cdot0.7+\frac{4}{14}\cdot0.5=0.5+0.143=0.643$.
2. Experiment 1 performs $n=12$ Bernoulli trials and observes $3$ successes. Experiment 2 performs trials until the third success and needs $12$ trials. Show that with the same prior both give the same posterior, but that the one-sided p-values for $H_0\colon\theta=0.5$ against $H_1\colon\theta<0.5$ differ.

   **Answer** The likelihoods are $\binom{12}{3}\theta^3(1-\theta)^9$ (binomial) and $\binom{11}{2}\theta^3(1-\theta)^9$ (the last trial is the third success), both proportional to $\theta^3(1-\theta)^9$. With a $\mathrm{Beta}(\alpha,\beta)$ prior both posteriors are $\mathrm{Beta}(\alpha+3,\beta+9)$, as the likelihood principle requires. The p-values use different sample spaces. In experiment 1 small numbers of successes are extreme: $\mathbb{P}(Y\le3\mid\theta=0.5)=0.073$. In experiment 2 large numbers of trials are extreme: $\mathbb{P}(N\ge12\mid\theta=0.5)=\mathbb{P}(\text{at most 2 successes in the first 11 trials})=0.033$. At level $0.05$ the second rejects $H_0$ and the first does not, although the data and the likelihood are the same.
3. In Example 1.5.1 suppose the prior probabilities are $\mathbb{P}(\theta=0.1)=0.7$ and $\mathbb{P}(\theta=0.2)=0.3$. Find the posterior probability of $\theta=0.1$.

   **Answer** The prior odds are $0.7/0.3=2.333$ and the likelihood ratio is $0.328/0.410=0.801$, so the posterior odds are $1.869$ and $\mathbb{P}(\theta=0.1\mid y)=1.869/2.869=0.651$. The data move the odds by the same factor as before; only the starting point has changed.
4. Show that a particular data set can increase the posterior variance above the prior variance. Use the prior $\mathrm{Beta}(1,20)$ and a single trial with outcome $y=1$. Why is this consistent with Proposition 1.6.2?

   **Answer** The prior variance is $\frac{1\cdot20}{21^2\cdot22}=0.00206$. After $y=1$ in $n=1$ trial the posterior is $\mathrm{Beta}(2,20)$ with variance $\frac{2\cdot20}{22^2\cdot23}=0.00359$, larger than before: the success is surprising under a prior concentrated near $0$ and makes us less sure. Proposition 1.6.2 bounds only the average of $\operatorname{Var}(\theta\mid y)$ over the prior predictive distribution of $y$. Under this prior the outcome $y=1$ has probability $1/21$, and the more likely outcome $y=0$ leads to $\mathrm{Beta}(1,21)$ with the smaller variance $0.00189$; the average, $\frac{20}{21}\cdot0.00189+\frac1{21}\cdot0.00359=0.00197$, is below $0.00206$.
5. In the placenta previa example (Example 1.6.1), how large must the prior sample size $s=\alpha+\beta$ of a conjugate prior with mean $0.485$ be for the posterior mean to equal $0.46$? What does this say about the conclusion?

   **Answer** The posterior mean is $\frac{0.485s+437}{s+980}$. Setting it equal to $0.46$ gives $0.485s+437=0.46s+450.8$, so $0.025s=13.8$ and $s=552$. A prior would have to be worth more than half as many births as the study itself before the posterior mean moved about a third of the way from $0.446$ toward $0.485$; the conclusion that the proportion is below $0.485$ is robust to any reasonable prior.
6. Let $\phi=h(\theta)$ with $h$ strictly increasing and differentiable. Show that the central posterior interval for $\phi$ is the image of the central interval for $\theta$, and give an example in which the HPD interval does not have this property.

   **Answer** Since $h$ is increasing, $\mathbb{P}(\phi\le h(q)\mid y)=\mathbb{P}(\theta\le q\mid y)$, so the $p$ quantile of $\phi$ is $h$ of the $p$ quantile of $\theta$ for every $p$, in particular for $p=\alpha/2$ and $1-\alpha/2$. The HPD region is defined through densities, and $p_\phi(\phi\mid y)=p_\theta(\theta\mid y)\,\lvert\mathrm{d}\theta/\mathrm{d}\phi\rvert$ reorders the points when the Jacobian is not constant. Example: if $\theta\mid y\sim\mathcal{N}(0,1)$, the $95\%$ HPD interval is $[-1.96,1.96]$. For $\phi=\mathrm{e}^\theta$ (lognormal), its image $[0.141,7.10]$ is still a $95\%$ interval, but the density of $\phi$ at the endpoints is $p_\theta(\pm1.96)/\phi$, which is $50$ times larger at $0.141$ than at $7.10$; the HPD interval for $\phi$ is shifted toward $0$, where the lognormal density has its mode $\mathrm{e}^{-1}$.
