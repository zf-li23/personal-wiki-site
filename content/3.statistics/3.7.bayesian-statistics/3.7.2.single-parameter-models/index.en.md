---
title: Single-Parameter Models and Classes of Priors
description: Poisson–Gamma models with and without exposure and the negative binomial prior predictive, the normal mean with known variance and its posterior predictive, the normal variance with known mean and the scaled inverse-chi-square family, conjugate priors for exponential families, proper and improper priors, Jeffreys' prior, pivotal quantities and reference priors.
---

A single-parameter model has one unknown scalar $\theta$. Such models are the building blocks of everything that follows: they show in closed form how prior and data combine, how a posterior is used for prediction, and what goes wrong when we try to express ignorance. [3.7.1](/3.7.1) treated the binomial model with Beta priors. This chapter works through the other standard models, the Poisson (§2.2), the normal with known variance (§2.3) and the normal with known mean (§2.4), and identifies the common structure behind their conjugate priors, the exponential family (§2.5). The second half continues the classification of priors begun in [3.7.1](/3.7.1) §1.6: after informative conjugate priors come non-informative ones, proper and improper priors (§2.6), Jeffreys' prior (§2.7), priors derived from pivotal quantities (§2.8) and reference priors (§2.9). The multiparameter versions of these models follow in [3.7.3](/3.7.3); all distributions used here are collected in [3.7.4](/3.7.4).

Throughout, $\Gamma(\alpha,\beta)$ is the **gamma distribution** with shape $\alpha$ and rate $\beta$, density $\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-\beta x}$ for $x>0$, mean $\alpha/\beta$ and variance $\alpha/\beta^2$. The rate $\beta$ is an inverse scale: $X\sim\Gamma(\alpha,\beta)$ if and only if $\beta X\sim\Gamma(\alpha,1)$.

## 2.1. Standard Single-Parameter Models

| Model | Likelihood of $y=(y_1,\dots,y_n)$ | Conjugate prior | Posterior |
|---|---|---|---|
| binomial, $y\sim\mathrm{Bin}(n,\theta)$ | $\binom ny\theta^y(1-\theta)^{n-y}$ | $\mathrm{Beta}(\alpha,\beta)$ | $\mathrm{Beta}(\alpha+y,\beta+n-y)$ |
| Poisson, $y_i\sim\mathrm{Poi}(\theta)$ | $\propto\theta^{n\bar y}\mathrm{e}^{-n\theta}$ | $\Gamma(\alpha,\beta)$ | $\Gamma(\alpha+n\bar y,\beta+n)$ |
| exponential, $y_i\sim\mathrm{Exp}(\theta)$ | $\theta^n\mathrm{e}^{-\theta n\bar y}$ | $\Gamma(\alpha,\beta)$ | $\Gamma(\alpha+n,\beta+n\bar y)$ |
| normal, known variance, $y_i\sim\mathcal{N}(\theta,\sigma^2)$ | $\propto\exp\big(-\frac{n}{2\sigma^2}(\bar y-\theta)^2\big)$ | $\mathcal{N}(\mu_0,\tau_0^2)$ | $\mathcal{N}(\mu_n,\tau_n^2)$, §2.3 |
| normal, known mean, $y_i\sim\mathcal{N}(\theta,\sigma^2)$ | $\propto(\sigma^2)^{-n/2}\exp\big(-\frac{n}{2\sigma^2}v\big)$, $v=\frac1n\sum_i(y_i-\theta)^2$ | $\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$ | $\mathrm{Inv}\text{-}\chi^2\big(\nu_0+n,\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\big)$, §2.4 |

In each case the likelihood depends on the data only through a **sufficient statistic** ($y$, $n\bar y$, $\bar y$ or $v$), and the conjugate prior has the same functional form in $\theta$ as the likelihood. The binomial row was derived in [3.7.1](/3.7.1); the exponential row is Question 6.

## 2.2. The Poisson Model

### 2.2.1. The Gamma Conjugate Prior

For counts $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathrm{Poi}(\theta)$, the likelihood is

$$
p(y\mid\theta)=\prod_{i=1}^n\frac{\theta^{y_i}\mathrm{e}^{-\theta}}{y_i!}\propto\theta^{n\bar y}\mathrm{e}^{-n\theta}.
$$
As a function of $\theta$ this is the kernel of a gamma density, so the gamma family is conjugate: with the prior $p(\theta)\propto\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}$, $\theta\sim\Gamma(\alpha,\beta)$,

$$
p(\theta\mid y)\propto\theta^{\alpha+n\bar y-1}\mathrm{e}^{-(\beta+n)\theta},\qquad\theta\mid y\sim\Gamma(\alpha+n\bar y,\,\beta+n).
$$
The prior can be read as additional data: it adds a total count to the observed total $n\bar y$ and a number of observation periods to $n$. Relative to the improper baseline $p(\theta)\propto\theta^{-1}$ ($\Gamma(0,0)$, Jeffreys' scale prior of §2.8) the prior $\Gamma(\alpha,\beta)$ is worth a total count $\alpha$ in $\beta$ periods; relative to the flat baseline $p(\theta)\propto1$ ($\Gamma(1,0)$) it is worth $\alpha-1$ counts in $\beta$ periods. The posterior mean

$$
\mathbb{E}(\theta\mid y)=\frac{\alpha+n\bar y}{\beta+n}=\frac{n}{\beta+n}\,\bar y+\frac{\beta}{\beta+n}\cdot\frac\alpha\beta
$$
is again a compromise between the sample mean and the prior mean, with weights $n$ and $\beta$.

**Example 2.2.1 (Traffic Accidents)** The number of traffic accidents on a campus in a week is modeled as $\mathrm{Poi}(\theta)$. The counts in 8 weeks are $3,2,0,8,2,4,6,1$, so $n=8$ and $n\bar y=26$, $\bar y=3.25$. Prior information says that the weekly mean is about $2.5$ with standard deviation $1$. Matching the moments of a gamma prior, $\alpha/\beta=2.5$ and $\alpha/\beta^2=1$, gives $\beta=2.5$, $\alpha=6.25$: the prior is worth about $6$ accidents observed in $2.5$ weeks. The posterior is

$$
\theta\mid y\sim\Gamma(6.25+26,\,2.5+8)=\Gamma(32.25,\,10.5),
$$
with the summaries

| mean | median | mode | standard deviation | $95\%$ central posterior interval | $\mathbb{P}(\theta>3\mid y)$ |
|---|---|---|---|---|---|
| 3.071 | 3.040 | 2.976 | 0.5408 | $[2.104,\,4.219]$ | 0.5296 |

The mode is $(\alpha+n\bar y-1)/(\beta+n)$. A one-sided question such as $H_0\colon\theta\le3$ against $H_1\colon\theta>3$ is answered directly by the posterior probability $0.53$: the data are nearly balanced between the two. A point hypothesis $H_0\colon\theta=3$ cannot be treated the same way, since a continuous posterior gives $\mathbb{P}(\theta=3\mid y)=0$; it needs a prior that puts positive probability on $\theta=3$, which leads to the **Bayes factor** ([3.7.8](/3.7.8)).

### 2.2.2. Poisson Model with Exposure

Often the counts arise from units of different size: deaths in cities of different population, failures over different operating times. The extended model is

$$
y_i\mid\theta\sim\mathrm{Poi}(x_i\theta),\qquad i=1,\dots,n,
$$
where the known positive $x_i$ is the exposure of unit $i$ and the unknown $\theta$ is the rate per unit of exposure. The likelihood is $p(y\mid\theta)\propto\theta^{\sum_iy_i}\mathrm{e}^{-\theta\sum_ix_i}$ (the factors $x_i^{y_i}$ do not involve $\theta$), the gamma family is still conjugate, and

$$
\theta\mid y\sim\Gamma\Big(\alpha+\sum_{i=1}^ny_i,\;\beta+\sum_{i=1}^nx_i\Big).
$$

**Example 2.2.2 (Asthma Mortality)** A study of causes of death in a city of $200{,}000$ people in one year finds $y=3$ deaths from asthma, a crude rate of $1.5$ cases per $100{,}000$ persons per year. Measure $\theta$ in cases per $100{,}000$ persons per year; then the exposure is $x=2.0$ and $y\sim\mathrm{Poi}(2.0\,\theta)$. Reviews of asthma mortality in comparable countries suggest that rates above $1.5$ per $100{,}000$ are rare and that typical rates are around $0.6$. A gamma prior with mean $0.6$ and $97.5\%$ quantile about $1.44$ is $\Gamma(3.0,5.0)$; it gives $\mathbb{P}(\theta>1.5)=0.02$. The posterior is

$$
\theta\mid y\sim\Gamma(3+3,\,5+2)=\Gamma(6,7),
$$
with mean $0.86$, well below the crude estimate $1.5$: three deaths in one year are weak evidence, and the prior pulls the estimate strongly toward typical values. The posterior probability that the long-term rate exceeds $1$ is $\mathbb{P}(\theta>1\mid y)=0.30$. If instead $y=30$ deaths had been observed over ten years in the same population, the exposure would be $x=20$ and the posterior $\Gamma(33,25)$, with mean $1.32$ and $\mathbb{P}(\theta>1\mid y)=0.93$: with ten times the data the posterior moves most of the way to the crude rate and becomes much more concentrated.

![Poisson–Gamma updating. Left: traffic accidents, with prior, normalized likelihood and posterior. Right: asthma mortality, with the prior Gamma(3, 5) and the posteriors after 3 deaths in one year and after 30 deaths in ten years.](./plots/poisson_gamma.py)

### 2.2.3. The Prior Predictive Distribution Is Negative Binomial

For a single observation $y\mid\theta\sim\mathrm{Poi}(\theta)$ with $\theta\sim\Gamma(\alpha,\beta)$ the posterior is $\Gamma(\alpha+y,\beta+1)$. The **prior predictive distribution** $p(y)=\int p(y\mid\theta)p(\theta)\,\mathrm{d}\theta$ can be found without integrating. Bayes' rule $p(\theta\mid y)=p(y\mid\theta)p(\theta)/p(y)$ holds for every $\theta$, so

$$
p(y)=\frac{p(y\mid\theta)\,p(\theta)}{p(\theta\mid y)}=\frac{\mathrm{Poi}(y\mid\theta)\,\Gamma(\theta\mid\alpha,\beta)}{\Gamma(\theta\mid\alpha+y,\beta+1)}
=\frac{\Gamma(\alpha+y)\,\beta^\alpha}{\Gamma(\alpha)\,y!\,(1+\beta)^{\alpha+y}}
=\binom{\alpha+y-1}{y}\Big(\frac{\beta}{\beta+1}\Big)^\alpha\Big(\frac{1}{\beta+1}\Big)^y,
$$
where all factors involving $\theta$ cancel, and $\binom{\alpha+y-1}{y}=\frac{\Gamma(\alpha+y)}{\Gamma(\alpha)\,y!}$ for real $\alpha>0$. This is the **negative binomial distribution**

$$
y\sim\mathrm{NB}\Big(\alpha,\frac{\beta}{\beta+1}\Big),\qquad y=0,1,2,\dots,
$$
in the convention of [3.1.6](/3.1.6): for integer $\alpha$ it is the number of failures before the $\alpha$-th success in independent Bernoulli trials with success probability $\beta/(\beta+1)$, and the formula extends to real $\alpha>0$. Gelman et al. write this distribution $\mathrm{Neg\text{-}bin}(\alpha,\beta)$, parametrized directly by the gamma parameters. The derivation shows that the negative binomial is a **mixture distribution** of Poisson distributions with gamma-distributed means. By the **law of total expectation** and the **law of total variance**,

$$
\mathbb{E}y=\mathbb{E}\theta=\frac\alpha\beta,\qquad\operatorname{Var}y=\mathbb{E}\theta+\operatorname{Var}\theta=\frac\alpha\beta+\frac{\alpha}{\beta^2},
$$
so the mixture is overdispersed relative to a Poisson with the same mean; this is why the negative binomial is a standard model for counts whose variance exceeds their mean.

The same argument with the posterior in place of the prior gives the **posterior predictive distribution**. A new count $\tilde y$ with exposure $\tilde x$, given data with posterior $\Gamma(\alpha',\beta')$, $\alpha'=\alpha+\sum_iy_i$, $\beta'=\beta+\sum_ix_i$, has

$$
\tilde y\mid y\sim\mathrm{NB}\Big(\alpha',\frac{\beta'}{\beta'+\tilde x}\Big),
$$
since $\tilde x\theta\mid y\sim\Gamma(\alpha',\beta'/\tilde x)$.

## 2.3. Normal Mean with Known Variance

### 2.3.1. One Observation

Let $y\mid\theta\sim\mathcal{N}(\theta,\sigma^2)$ with $\sigma^2$ known. As a function of $\theta$ the likelihood is the exponential of a quadratic, so the conjugate family consists of densities $p(\theta)=\mathrm{e}^{A\theta^2+B\theta+C}$ with $A<0$, that is the normal distributions $\theta\sim\mathcal{N}(\mu_0,\tau_0^2)$:

$$
p(\theta)\propto\exp\Big(-\frac{1}{2\tau_0^2}(\theta-\mu_0)^2\Big).
$$
Then

$$
p(\theta\mid y)\propto\exp\Big(-\frac12\Big[\frac{(y-\theta)^2}{\sigma^2}+\frac{(\theta-\mu_0)^2}{\tau_0^2}\Big]\Big)\propto\exp\Big(-\frac{1}{2\tau_1^2}(\theta-\mu_1)^2\Big),
$$
by completing the square in $\theta$: the coefficient of $\theta^2$ in the bracket is $\frac{1}{\sigma^2}+\frac1{\tau_0^2}$ and that of $-2\theta$ is $\frac{y}{\sigma^2}+\frac{\mu_0}{\tau_0^2}$. Hence $\theta\mid y\sim\mathcal{N}(\mu_1,\tau_1^2)$ with

$$
\mu_1=\frac{\frac{1}{\tau_0^2}\mu_0+\frac{1}{\sigma^2}y}{\frac{1}{\tau_0^2}+\frac{1}{\sigma^2}},\qquad\frac{1}{\tau_1^2}=\frac{1}{\tau_0^2}+\frac{1}{\sigma^2}.
$$
The inverse of a variance is called a precision. The posterior precision is the sum of the prior precision and the data precision, and the posterior mean is the precision-weighted average of the prior mean and the observation. Equivalent forms make the compromise explicit:

$$
\mu_1=\mu_0+(y-\mu_0)\frac{\tau_0^2}{\sigma^2+\tau_0^2}=y-(y-\mu_0)\frac{\sigma^2}{\sigma^2+\tau_0^2}:
$$
the prior mean adjusted toward the observation, or the observation shrunk toward the prior mean.

### 2.3.2. Several Observations

For $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathcal{N}(\theta,\sigma^2)$,

$$
p(\theta\mid y)\propto p(\theta)\prod_{i=1}^np(y_i\mid\theta)\propto\exp\Big(-\frac12\Big[\frac{(\theta-\mu_0)^2}{\tau_0^2}+\frac{1}{\sigma^2}\sum_{i=1}^n(y_i-\theta)^2\Big]\Big).
$$
Since $\sum_i(y_i-\theta)^2=\sum_i(y_i-\bar y)^2+n(\bar y-\theta)^2$, the posterior depends on the data only through $\bar y$, and it is the one-observation result with $y$ replaced by $\bar y\mid\theta\sim\mathcal{N}(\theta,\sigma^2/n)$:

$$
p(\theta\mid y_1,\dots,y_n)=p(\theta\mid\bar y)=\mathcal{N}(\theta\mid\mu_n,\tau_n^2),\qquad
\mu_n=\frac{\frac{1}{\tau_0^2}\mu_0+\frac{n}{\sigma^2}\bar y}{\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}},\qquad
\frac{1}{\tau_n^2}=\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}.
$$
The data precision grows linearly in $n$. Writing $\sigma^2=\kappa_0\tau_0^2$, the prior is worth $\kappa_0$ observations, and $\mu_n=\frac{\kappa_0\mu_0+n\bar y}{\kappa_0+n}$.

### 2.3.3. The Posterior Predictive Distribution

A future observation $\tilde y$ satisfies $\tilde y\mid\theta\sim\mathcal{N}(\theta,\sigma^2)$, independently of $y$ given $\theta$. Its posterior predictive density is

$$
p(\tilde y\mid y)=\int p(\tilde y\mid\theta)p(\theta\mid y)\,\mathrm{d}\theta\propto\int\exp\Big(-\frac{(\tilde y-\theta)^2}{2\sigma^2}\Big)\exp\Big(-\frac{(\theta-\mu_n)^2}{2\tau_n^2}\Big)\,\mathrm{d}\theta.
$$
The integrand is the exponential of a quadratic form in $(\tilde y,\theta)$, so $(\tilde y,\theta)$ is bivariate normal given $y$ and the marginal $\tilde y\mid y$ is normal. Its moments follow from the **law of total expectation** and the **law of total variance**:

$$
\begin{aligned}
\mathbb{E}(\tilde y\mid y)&=\mathbb{E}\big[\mathbb{E}(\tilde y\mid\theta,y)\mid y\big]=\mathbb{E}(\theta\mid y)=\mu_n,\\
\operatorname{Var}(\tilde y\mid y)&=\mathbb{E}\big[\operatorname{Var}(\tilde y\mid\theta,y)\mid y\big]+\operatorname{Var}\big[\mathbb{E}(\tilde y\mid\theta,y)\mid y\big]=\sigma^2+\tau_n^2.
\end{aligned}
$$
So $\tilde y\mid y\sim\mathcal{N}(\mu_n,\sigma^2+\tau_n^2)$. Equivalently $\tilde y=\theta+\varepsilon$ with $\theta\mid y\sim\mathcal{N}(\mu_n,\tau_n^2)$ and an independent $\varepsilon\sim\mathcal{N}(0,\sigma^2)$. The predictive variance has two parts: the sampling variance $\sigma^2$, which remains however much data we have, and the posterior uncertainty $\tau_n^2$ about $\theta$, which vanishes as $n\to\infty$. Before any data, the prior predictive distribution of one observation is $\mathcal{N}(\mu_0,\sigma^2+\tau_0^2)$, wider because $\tau_0^2>\tau_n^2$.

**Example 2.3.1 (Fish Length)** The lengths of fish in a pond are $\mathcal{N}(\theta,2^2)$ in centimeters. Prior knowledge: the average length is about $30\,\mathrm{cm}$, and an average below $18$ or above $42\,\mathrm{cm}$ is nearly impossible. Reading "nearly impossible" as three standard deviations, $\mu_0=30$ and $\tau_0=12/3=4$. The average length of $n=12$ caught fish is $\bar y=32$. Then

$$
\mu_n=\frac{\frac{1}{4^2}\cdot30+\frac{12}{2^2}\cdot32}{\frac{1}{4^2}+\frac{12}{2^2}}=31.96,\qquad\frac{1}{\tau_n^2}=\frac{1}{4^2}+\frac{12}{2^2}=\frac{1}{0.5714^2},
$$
so $\theta\mid y\sim\mathcal{N}(31.96,0.5714^2)$, with $95\%$ central posterior interval $31.96\pm1.96\times0.5714=[30.84,33.08]$. The data precision $3$ is 48 times the prior precision $1/16$, so the posterior mean is close to $\bar y$. The length of the next fish caught has

$$
\tilde y\mid y\sim\mathcal{N}(31.96,\;2^2+0.5714^2)=\mathcal{N}(31.96,\;2.080^2),
$$
with $95\%$ predictive interval $[27.88,36.04]$. The predictive distribution is much wider than the posterior of $\theta$, since an individual fish varies around the mean with standard deviation $2$; it is only slightly wider than $\mathcal{N}(\theta,2^2)$ with $\theta$ known, because $\theta$ is already well determined.

![Fish length example: prior and posterior of the mean length θ, prior predictive distribution of one fish, and posterior predictive distribution of the next fish.](./plots/normal_mean_predictive.py)

## 2.4. Normal Variance with Known Mean

### 2.4.1. Inverse Gamma and Inverse Chi-square Distributions

Let $y_1,\dots,y_n\mid\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\theta,\sigma^2)$ with known mean $\theta$. The likelihood of $\sigma^2$ is

$$
p(y\mid\sigma^2)\propto\sigma^{-n}\exp\Big(-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\theta)^2\Big)=(\sigma^2)^{-n/2}\exp\Big(-\frac{n}{2\sigma^2}v\Big),\qquad v=\frac1n\sum_{i=1}^n(y_i-\theta)^2,
$$
with sufficient statistic $v$. As a function of $\sigma^2$ this is a power of $\sigma^2$ times $\exp(-c/\sigma^2)$, the kernel of the following family.

**Definition 2.4.1 (Inverse Gamma and Inverse Chi-square Distributions)** Let $\alpha,\beta>0$. A positive random variable $X$ has the **inverse-gamma distribution** $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ if $1/X\sim\Gamma(\alpha,\beta)$; its density is

$$
p(x)=\frac{\beta^\alpha}{\Gamma(\alpha)}x^{-(\alpha+1)}\mathrm{e}^{-\beta/x},\qquad x>0,
$$
and $\beta$ is a scale parameter of $X$. The **inverse-chi-square distribution** with $\nu>0$ degrees of freedom is $\mathrm{Inv}\text{-}\chi^2_\nu=\mathrm{Inv}\text{-}\Gamma(\nu/2,1/2)$, the distribution of $1/Z$ for $Z\sim\chi^2_\nu$. The **scaled inverse-chi-square distribution** with $\nu$ degrees of freedom and scale $s^2>0$ is

$$
\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma\Big(\frac\nu2,\frac{\nu s^2}{2}\Big),\qquad p(x)\propto x^{-(\nu/2+1)}\exp\Big(-\frac{\nu s^2}{2x}\Big),
$$
the distribution of $X=\nu s^2/Z$ with $Z\sim\chi^2_\nu$.

The density follows from the change of variables $x=1/u$, $\lvert\mathrm{d}u/\mathrm{d}x\rvert=x^{-2}$. The moments and the mode are

| | $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ | $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ |
|---|---|---|
| mean | $\frac{\beta}{\alpha-1}$ ($\alpha>1$) | $\frac{\nu}{\nu-2}s^2$ ($\nu>2$) |
| variance | $\frac{\beta^2}{(\alpha-1)^2(\alpha-2)}$ ($\alpha>2$) | $\frac{2\nu^2}{(\nu-2)^2(\nu-4)}s^4$ ($\nu>4$) |
| mode | $\frac{\beta}{\alpha+1}$ | $\frac{\nu}{\nu+2}s^2$ |

Quantiles come from **chi-square distribution** quantiles, which is how they are computed by hand. With $\chi^2_{\nu,p}$ the upper $p$ quantile of $\chi^2_\nu$, the event $X\le\nu s^2/\chi^2_{\nu,p}$ is the event $Z\ge\chi^2_{\nu,p}$, so the lower $p$ quantile of $X\sim\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ is $\nu s^2/\chi^2_{\nu,p}$. The scale $s^2$ lies between the mode and the mean, and as $\nu\to\infty$ the distribution concentrates at $s^2$.

![Densities of the inverse-chi-square distributions with ν = 1, 2, 3, 5, 10 degrees of freedom (left) and of the scaled inverse-chi-square distributions with ν = 5 and different scales s² (right).](./plots/inv_chi2_family.py)

### 2.4.2. The Conjugate Update

With the prior $\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$, $p(\sigma^2)\propto(\sigma^2)^{-(\nu_0/2+1)}\exp\big(-\frac{\nu_0\sigma_0^2}{2\sigma^2}\big)$,

$$
p(\sigma^2\mid y)\propto(\sigma^2)^{-(\nu_0/2+1)}\exp\Big(-\frac{\nu_0\sigma_0^2}{2\sigma^2}\Big)\cdot(\sigma^2)^{-n/2}\exp\Big(-\frac{nv}{2\sigma^2}\Big)
=(\sigma^2)^{-((n+\nu_0)/2+1)}\exp\Big(-\frac{\nu_0\sigma_0^2+nv}{2\sigma^2}\Big),
$$
so

$$
\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2\Big(\nu_0+n,\;\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\Big).
$$
The prior is worth $\nu_0$ observations with mean squared deviation $\sigma_0^2$: the degrees of freedom add, and the posterior scale is the degrees-of-freedom-weighted average of the prior scale and the data estimate $v$.

**Example 2.4.1 (Powder Milk)** The weight of a bottle of powder milk is $\mathcal{N}(1015,\sigma^2)$ in grams, with known mean $1015$. What is the plausible range of $\sigma$? The prior information is that the median of $\sigma$ is $5\,\mathrm{g}$. Take a conjugate prior with $\nu_0=1$, the weakest one that is still proper. Since $\sigma^2=\sigma_0^2/Z$ with $Z\sim\chi^2_1$, and $\sigma^2$ is a decreasing function of $Z$, the median of $\sigma^2$ is $\sigma_0^2$ divided by the median $0.4549$ of $\chi^2_1$; setting it equal to $5^2$ gives

$$
\sigma_0^2=25\times0.4549=11.37,\qquad\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(1,11.37).
$$
The weights of $10$ bottles are $1011,1009,1019,1012,1011,1016,1018,1021,1016,1012$. Their deviations from $1015$ are $-4,-6,4,-3,-4,1,3,6,1,-3$, so $nv=\sum_i(y_i-1015)^2=149$ and $v=14.9$ (and $\sqrt v=3.862$). The posterior is

$$
\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2\Big(11,\;\frac{11.37+149}{11}\Big)=\mathrm{Inv}\text{-}\chi^2(11,\;14.58).
$$
The posterior median of $\sigma$ is $\sqrt{160.37/\chi^2_{11,0.5}}=\sqrt{160.37/10.34}=3.938$, and the $95\%$ central posterior interval for $\sigma$ is

$$
\Big[\sqrt{160.37/\chi^2_{11,0.025}},\;\sqrt{160.37/\chi^2_{11,0.975}}\Big]=\Big[\sqrt{160.37/21.92},\;\sqrt{160.37/3.816}\Big]=[2.70,\;6.48].
$$
Medians and central intervals transform directly from $\sigma^2$ to $\sigma=\sqrt{\sigma^2}$ because the square root is increasing. The mean and the mode do not: $\sqrt{\mathbb{E}(\sigma^2\mid y)}=\sqrt{160.37/9}=4.221$ and $\sqrt{\operatorname{mode}(\sigma^2\mid y)}=\sqrt{160.37/13}=3.512$, whereas $\sigma$ itself has posterior mean $4.106$ and mode $3.656$ (Question 5). The comparison with other priors is in Example 2.7.1.

## 2.5. Conjugate Priors for Exponential Families

The conjugate pairs of §2.1–§2.4 are all instances of one construction. Suppose the sampling distribution belongs to an **exponential family**,

$$
p(y_i\mid\theta)=f(y_i)\exp\big(\boldsymbol{\phi}(\theta)^{\mathsf T}\boldsymbol{u}(y_i)-g(\theta)\big),
$$
where $\boldsymbol{\phi}(\theta)$ is the **natural parameter**. For an iid sample $y=(y_1,\dots,y_n)$ the likelihood is

$$
p(y\mid\theta)=\Big(\prod_{i=1}^nf(y_i)\Big)\exp\Big(\boldsymbol{\phi}(\theta)^{\mathsf T}\sum_{i=1}^n\boldsymbol{u}(y_i)-n\,g(\theta)\Big)\propto\exp\big(\boldsymbol{\phi}(\theta)^{\mathsf T}\boldsymbol{t}(y)-n\,g(\theta)\big),
$$
with the sufficient statistic $\boldsymbol{t}(y)=\sum_{i=1}^n\boldsymbol{u}(y_i)$.

**Proposition 2.5.1** For the exponential family above, the priors

$$
p(\theta)\propto\exp\big(\boldsymbol{\phi}(\theta)^{\mathsf T}\boldsymbol{\nu}-n_0\,g(\theta)\big),
$$
indexed by the hyperparameters $(\boldsymbol{\nu},n_0)$ for which the right side is integrable, form a conjugate family, and the posterior is

$$
p(\theta\mid y)\propto\exp\big(\boldsymbol{\phi}(\theta)^{\mathsf T}(\boldsymbol{\nu}+\boldsymbol{t}(y))-(n_0+n)\,g(\theta)\big),
$$
the member with hyperparameters $(\boldsymbol{\nu}+\boldsymbol{t}(y),\,n_0+n)$.

**Proof** Multiply the prior by the likelihood; the exponents add. $\square$

This is [Theorem 7.3.1](/3.2.7#thm-7.3.1) of [3.2.7](/3.2.7) in a different parametrization. The hyperparameters behave like data: $n_0$ is a prior sample size and $\boldsymbol{\nu}$ a prior value of the sufficient statistic. Conjugate priors therefore always exist for exponential families and can always be interpreted as additional data. Conversely, apart from irregular cases in which the support depends on $\theta$, only exponential families admit a sufficient statistic of fixed dimension for every $n$ (the Pitman–Koopman–Darmois theorem), and hence a natural conjugate family of fixed dimension.

For the Poisson model, $p(y_i\mid\theta)=\frac{1}{y_i!}\exp(y_i\log\theta-\theta)$, so $\phi(\theta)=\log\theta$, $u(y_i)=y_i$, $g(\theta)=\theta$, and the conjugate prior is $\exp(\nu\log\theta-n_0\theta)=\theta^\nu\mathrm{e}^{-n_0\theta}$, the gamma density $\Gamma(\nu+1,n_0)$. For the binomial model with one observation, $\phi(\theta)=\log\frac{\theta}{1-\theta}$, $u(y)=y$, $g(\theta)=-n\log(1-\theta)$, and the conjugate prior $\theta^\nu(1-\theta)^{n_0n-\nu}$ is a Beta density.

## 2.6. Non-informative Priors

### 2.6.1. Motivation

When a prior distribution has no population basis it can be difficult to construct, and there has long been a desire for priors that are guaranteed to play a minimal role in the posterior. Such a **non-informative prior** is also called vague, flat or diffuse. The rationale is to let the data speak for themselves, so that inferences are unaffected by information external to the current data.

When the parameter lies in a bounded interval, as the binomial probability $\theta\in[0,1]$, the uniform distribution is the obvious candidate, and with it the posterior is proportional to the likelihood. When the parameter ranges over an infinite interval no uniform probability distribution exists. For the normal mean with known variance (§2.3) consider the limit of the conjugate prior as $\tau_0^2\to\infty$, so that the prior becomes ever flatter on the real line. The posterior formulas have a limit:

$$
\mu_n\to\bar y,\qquad\tau_n^2\to\frac{\sigma^2}{n},\qquad p(\theta\mid y)\to\mathcal{N}\Big(\theta\;\Big|\;\bar y,\frac{\sigma^2}{n}\Big).
$$
The same posterior is obtained directly from the "flat prior" $p(\theta)\propto1$ on $\mathbb{R}$. This prior is not a probability distribution, but it is the limit of a sequence of proper priors, and in this case the posterior is still a proper distribution. In the fish example (Example 2.3.1), the flat prior gives $\theta\mid y\sim\mathcal{N}(32,\,2^2/12)=\mathcal{N}(32,\,0.5774^2)$, almost the same as with the prior $\mathcal{N}(30,4^2)$ because that prior was already weak.

### 2.6.2. Proper and Improper Priors

**Definition 2.6.1 (Proper and Improper Priors)** A prior density $p(\theta)\ge0$ on $\Theta$ is a **proper prior** if $\int_\Theta p(\theta)\,\mathrm{d}\theta<\infty$, so that after normalization it is a probability distribution, and an **improper prior** if $\int_\Theta p(\theta)\,\mathrm{d}\theta=\infty$.

Priors only need to be specified up to a normalizing constant, so a finite integral is all that properness requires. If the prior is proper, the posterior is proper: $p(y)=\int p(y\mid\theta)p(\theta)\,\mathrm{d}\theta$ is finite for almost every $y$ (its integral over $y$ is $\int p(\theta)\,\mathrm{d}\theta<\infty$), and the posterior is $p(y\mid\theta)p(\theta)/p(y)$. If the prior is improper, the posterior may be proper or improper, and it must be checked. In theory any prior is acceptable as long as the posterior is proper, and for many common problems the popular improper priors lead to proper posteriors when there are enough data:

- normal mean: with $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathcal{N}(\theta,\sigma^2)$ and $p(\theta)\propto1$, the posterior $\mathcal{N}(\bar y,\sigma^2/n)$ is proper as soon as $n\ge1$;
- binomial with $p(\theta)\propto\theta^{-1}(1-\theta)^{-1}$ (formally $\mathrm{Beta}(0,0)$): the posterior $\propto\theta^{y-1}(1-\theta)^{n-y-1}$ is the proper $\mathrm{Beta}(y,n-y)$ when $0<y<n$, but is improper when $y=0$ or $y=n$, since $\int_0^1\theta^{-1}(1-\theta)^{n-1}\,\mathrm{d}\theta$ diverges at $0$.

An improper posterior is not a "very vague" answer but no answer at all: it does not define probabilities. Improper priors must also be avoided whenever the marginal $p(y)$ itself is needed, as in model comparison by Bayes factors ([3.7.8](/3.7.8)), because $p(y)$ then contains an arbitrary constant.

### 2.6.3. A Uniform Prior Depends on the Parametrization

Choosing a non-informative prior is less simple than "use a uniform", because uniformity depends on the scale on which the parameter is measured. Recall the change of variables: if $\theta$ has density $p(\theta)$ and $\phi=h(\theta)$ is one-to-one, then

$$
p_\phi(\phi)=p(\theta)\Big\lvert\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big\rvert=p(\theta)\,\lvert h'(\theta)\rvert^{-1},\qquad\theta=h^{-1}(\phi).
$$
For normal observations with known mean and unknown variance, a uniform prior $p(\sigma)\propto1$ on the standard deviation corresponds, with $h(\sigma)=\sigma^2$, to

$$
p(\sigma^2)\propto\frac{1}{2\sigma}\propto(\sigma^2)^{-1/2},
$$
which is not uniform: it decreases, so compared with a uniform prior on the variance it favors small variances. Conversely a uniform prior on $\sigma^2$ corresponds to $p(\sigma)\propto2\sigma$, which favors large standard deviations. In terms of intervals: under the uniform prior on $\sigma^2$ every interval $[a,a+0.1]$ of variances has the same prior probability as $[0.1,0.2]$; the corresponding intervals $[\sqrt a,\sqrt{a+0.1}]$ of standard deviations become shorter as $a$ grows, so the prior density of $\sigma$ must increase. A statement of ignorance must therefore say on which scale the ignorance holds.

## 2.7. Jeffreys' Prior

### 2.7.1. The Invariance Principle

Can we pick a prior by a rule for which the scale of measurement does not matter? Let $\pi(\cdot)$ denote the rule, which assigns to a model and a parameter a prior density. Let $\phi=h(\theta)$ be a one-to-one reparametrization. There are two ways to get a prior for $\phi$: transform the prior $\pi(\theta)$ obtained for $\theta$, which gives $p_\phi(\phi)=\pi(\theta)\lvert\mathrm{d}\theta/\mathrm{d}\phi\rvert$; or apply the rule directly to the model written in terms of $\phi$.

**Definition 2.7.1 (Jeffreys' Invariance Principle)** A rule for constructing prior densities satisfies **Jeffreys' invariance principle** if, for every one-to-one reparametrization $\phi=h(\theta)$, the rule applied to $\phi$ gives the transformed prior,

$$
\pi(\phi)=\pi(\theta)\Big\lvert\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big\rvert,\qquad\theta=h^{-1}(\phi).
$$

The uniform rule violates the principle (§2.6.3). A rule that satisfies it uses the **Fisher information** of the model ([3.2.3](/3.2.3)),

$$
J(\theta)=\mathbb{E}\Big[\Big(\frac{\mathrm{d}\log p(y\mid\theta)}{\mathrm{d}\theta}\Big)^2\;\Big|\;\theta\Big]=-\mathbb{E}\Big[\frac{\mathrm{d}^2\log p(y\mid\theta)}{\mathrm{d}\theta^2}\;\Big|\;\theta\Big],
$$
the second equality holding under the usual regularity conditions. For $n$ iid observations the information is $nJ_1(\theta)$, $n$ times the information of one observation; the **observed information** $-\frac{\mathrm{d}^2}{\mathrm{d}\theta^2}\log p(y\mid\theta)$ has expectation equal to it.

**Definition 2.7.2 (Jeffreys' Prior)** **Jeffreys' prior** is $p(\theta)\propto J(\theta)^{1/2}$. For a vector parameter it is $p(\boldsymbol{\theta})\propto\lvert\det J(\boldsymbol{\theta})\rvert^{1/2}$ with the **Fisher information matrix** $J(\boldsymbol{\theta})$.

**Theorem 2.7.1** Under a one-to-one differentiable reparametrization $\phi=h(\theta)$,

$$
J(\phi)=J(\theta)\Big(\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big)^2,\qquad\text{hence}\qquad J(\phi)^{1/2}=J(\theta)^{1/2}\Big\lvert\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big\rvert,
$$
so Jeffreys' prior satisfies Jeffreys' invariance principle.

**Proof** Write $\ell(\theta)=\log p(y\mid\theta)$ and differentiate $\ell(\theta(\phi))$ twice by the chain rule:

$$
\frac{\mathrm{d}^2\ell}{\mathrm{d}\phi^2}=\frac{\mathrm{d}^2\ell}{\mathrm{d}\theta^2}\Big(\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\Big)^2+\frac{\mathrm{d}\ell}{\mathrm{d}\theta}\,\frac{\mathrm{d}^2\theta}{\mathrm{d}\phi^2}.
$$
Take $-\mathbb{E}(\cdot\mid\theta)$. The score has expectation zero, $\mathbb{E}\big(\frac{\mathrm{d}\ell}{\mathrm{d}\theta}\mid\theta\big)=0$, so the second term vanishes, and $J(\phi)=J(\theta)\big(\frac{\mathrm{d}\theta}{\mathrm{d}\phi}\big)^2$. Taking square roots gives the second form, which is exactly the transformation rule of Definition 2.7.1. $\square$

### 2.7.2. Examples

*Normal standard deviation.* For $y\mid\sigma\sim\mathcal{N}(\theta,\sigma^2)$ with $\theta$ known, $\ell=-\log\sigma-\frac{(y-\theta)^2}{2\sigma^2}$ and $\frac{\mathrm{d}^2\ell}{\mathrm{d}\sigma^2}=\frac{1}{\sigma^2}-\frac{3(y-\theta)^2}{\sigma^4}$, so $J(\sigma)=-\frac1{\sigma^2}+\frac{3}{\sigma^2}=\frac{2}{\sigma^2}$ and Jeffreys' prior is

$$
p(\sigma)\propto\frac1\sigma,\qquad\text{equivalently}\qquad p(\sigma^2)\propto\frac{1}{\sigma^2},\qquad p(\log\sigma)\propto1.
$$
The three forms describe the same prior on different scales; by invariance it does not matter which parameter we start from. With this prior the normal variance model of §2.4 gives

$$
p(\sigma^2\mid y)\propto(\sigma^2)^{-1}\cdot(\sigma^2)^{-n/2}\exp\Big(-\frac{nv}{2\sigma^2}\Big)=(\sigma^2)^{-(n/2+1)}\exp\Big(-\frac{nv}{2\sigma^2}\Big),\qquad\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n,v),
$$
the conjugate posterior with $\nu_0=0$: Jeffreys' prior is the limit $\nu_0\to0$ of the conjugate family.

*Exponential data.* For $y_i\overset{\text{iid}}{\sim}\mathrm{Exp}(\theta)$ with rate $\theta=1/\mathbb{E}(y\mid\theta)$, $\ell=\log\theta-\theta y$ and $J(\theta)=1/\theta^2$, so $p(\theta)\propto1/\theta$. Parametrized by the mean $\lambda=1/\theta$, Jeffreys' prior is again $p(\lambda)\propto1/\lambda$, as invariance requires: $\frac1\theta\lvert\frac{\mathrm{d}\theta}{\mathrm{d}\lambda}\rvert=\lambda\cdot\lambda^{-2}$.

*Poisson.* $\ell=y\log\theta-\theta$, $J(\theta)=\mathbb{E}(y)/\theta^2=1/\theta$, so $p(\theta)\propto\theta^{-1/2}$, the improper limit $\Gamma(\frac12,0)$; the posterior is $\Gamma(n\bar y+\frac12,n)$.

*Binomial.* $\log p(y\mid\theta)=\text{const}+y\log\theta+(n-y)\log(1-\theta)$ gives $J(\theta)=\frac{n}{\theta(1-\theta)}$, so Jeffreys' prior is

$$
p(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2},\qquad\mathrm{Beta}\big(\tfrac12,\tfrac12\big).
$$
Two other "non-informative" choices compete with it:

| Principle | Prior on $\theta$ | Beta form |
|---|---|---|
| Jeffreys' prior | $\theta^{-1/2}(1-\theta)^{-1/2}$ | $\mathrm{Beta}(\frac12,\frac12)$, proper |
| Bayes–Laplace uniform prior | $1$ | $\mathrm{Beta}(1,1)$, proper |
| uniform on the natural parameter $\operatorname{logit}\theta$ | $\theta^{-1}(1-\theta)^{-1}$ | $\mathrm{Beta}(0,0)$, improper |

The last row follows from the change of variables with $\frac{\mathrm{d}}{\mathrm{d}\theta}\operatorname{logit}\theta=\frac{1}{\theta(1-\theta)}$. Different principles lead to different non-informative priors. The difference amounts to at most one prior success and one prior failure, so in practice it is small when the sample is reasonably large; it matters when $y$ is $0$ or $n$ or when $n$ is small.

For parameters with infinite parameter spaces, such as a normal mean or variance, Jeffreys' prior is often improper in the usual parametrizations, and the posterior must be checked for properness as in §2.6.2.

**Example 2.7.1 (Powder Milk, Three Priors)** Return to Example 2.4.1 with $n=10$, $nv=149$. Besides the conjugate prior, consider Jeffreys' prior $p(\sigma^2)\propto\sigma^{-2}$, which gives $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(10,14.9)$, and the uniform prior $p(\sigma)\propto1$, equivalent to $p(\sigma^2)\propto(\sigma^2)^{-1/2}$, which gives

$$
p(\sigma^2\mid y)\propto(\sigma^2)^{-((n-1)/2+1)}\exp\Big(-\frac{nv}{2\sigma^2}\Big),\qquad\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2\Big(n-1,\frac{nv}{n-1}\Big)=\mathrm{Inv}\text{-}\chi^2(9,16.56).
$$
Each posterior has the form $\sigma^2=S/Z$ with $Z\sim\chi^2_\nu$; the summaries for $\sigma$ are

| Prior | $\sigma^2\mid y$ | $\sqrt{\operatorname{mode}(\sigma^2\mid y)}$ | $\sqrt{\mathbb{E}(\sigma^2\mid y)}$ | mode of $\sigma$ | mean of $\sigma$ | median of $\sigma$ | $95\%$ interval for $\sigma$ |
|---|---|---|---|---|---|---|---|
| conjugate $\mathrm{Inv}\text{-}\chi^2(1,11.37)$ | $\mathrm{Inv}\text{-}\chi^2(11,14.58)$ | 3.512 | 4.221 | 3.656 | 4.106 | 3.938 | $[2.70,\,6.48]$ |
| Jeffreys $p(\sigma^2)\propto\sigma^{-2}$ | $\mathrm{Inv}\text{-}\chi^2(10,14.9)$ | 3.524 | 4.316 | 3.680 | 4.183 | 3.994 | $[2.70,\,6.77]$ |
| uniform $p(\sigma)\propto1$ | $\mathrm{Inv}\text{-}\chi^2(9,16.56)$ | 3.680 | 4.614 | 3.860 | 4.452 | 4.226 | $[2.80,\,7.43]$ |

For $\sigma^2=S/Z$ the posterior density of $\sigma$ is proportional to $\sigma^{-(\nu+1)}\exp(-S/(2\sigma^2))$, with mode $\sqrt{S/(\nu+1)}$ and mean $\sqrt{S/2}\,\Gamma(\frac{\nu-1}{2})/\Gamma(\frac\nu2)$. Under the uniform prior on $\sigma$ the posterior mode of $\sigma$ is the maximum likelihood estimate $\sqrt v=3.862$, as it must be when the prior is flat in the parameter considered. The conjugate prior with one prior degree of freedom changes little compared with Jeffreys' prior. The uniform prior on $\sigma$, which favors larger values relative to Jeffreys' prior, shifts the posterior visibly upward, especially its right tail: with only ten observations, the scale on which the prior is flat matters.

![Powder milk example: posterior densities of σ under the conjugate prior, Jeffreys' prior and the uniform prior on σ, together with the conjugate prior of σ (dashed).](./plots/powder_milk_priors.py)

## 2.8. Pivotal Quantities

In some situations the different approaches agree on the non-informative prior. They are the location and scale models, where a **pivotal quantity** fixes the prior.

**Definition 2.8.1 (Location and Scale Parameters)** If the density of $u=y-\theta$ given $\theta$ is a fixed function $f(u)$ not depending on $\theta$, then $y-\theta$ is a pivotal quantity and $\theta$ is a pure **location parameter**; the model is a location family, $p(y\mid\theta)=f(y-\theta)$. If $\theta>0$ and the density of $u=y/\theta$ given $\theta$ is a fixed function $g(u)$, then $y/\theta$ is a pivotal quantity and $\theta$ is a pure **scale parameter**; the model is a scale family, $p(y\mid\theta)=\frac1\theta g(y/\theta)$.

For example, for $y\sim\mathcal{N}(\theta,1)$ the mean is a location parameter with $f(u)=\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-u^2/2}$; for $y\sim\mathcal{N}(0,\theta^2)$ the standard deviation is a scale parameter with the same $g=f$. The standard deviation of a normal distribution and the mean of an exponential distribution are scale parameters.

The distribution of a pivotal quantity given $\theta$ is the same for every $\theta$ and does not involve $y$. A natural requirement for a non-informative prior is that it preserves this: the posterior distribution of the pivot given $y$ should be the same fixed distribution.

*Location families.* Require $p(y-\theta\mid y)=f(y-\theta)$. Since $\theta\mapsto u=y-\theta$ has unit Jacobian for fixed $y$, the posterior of $\theta$ is $p(\theta\mid y)=f(y-\theta)=p(y\mid\theta)$. Comparing with $p(\theta\mid y)\propto p(\theta)p(y\mid\theta)$ gives $p(\theta)\propto1$.

*Scale families.* Require that $u=y/\theta$ have posterior density $g(u)$. For fixed $y>0$, $\theta=y/u$ and $\lvert\mathrm{d}u/\mathrm{d}\theta\rvert=y/\theta^2$, so

$$
p(\theta\mid y)=g\Big(\frac y\theta\Big)\frac{y}{\theta^2}=\frac y\theta\cdot\frac1\theta g\Big(\frac y\theta\Big)=\frac{y}{\theta}\,p(y\mid\theta)\propto\frac1\theta\,p(y\mid\theta),
$$
which gives $p(\theta)\propto1/\theta$.

For the normal standard deviation this is Jeffreys' prior again. In some sense the "right" scale for a scale parameter is $\log\theta$, on which the prior is flat:

$$
p(\theta)\propto\frac1\theta,\qquad p(\theta^2)\propto\frac1{\theta^2},\qquad p(\log\theta)\propto1.
$$
Pivotal quantities are also the basis of standard frequentist inference. For $y_1,\dots,y_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ with sample mean $\bar y$ and sample variance $s^2$,

$$
\frac{\sqrt n(\bar y-\mu)}{s}\sim t_{n-1},\qquad\frac{(n-1)s^2}{\sigma^2}\sim\chi^2_{n-1},
$$
and the usual **confidence interval** and tests use the fact that these distributions do not depend on the parameters. Under the prior $p(\mu,\sigma^2)\propto\sigma^{-2}$, which is flat in $\mu$ and in $\log\sigma$, the same quantities have the same distributions a posteriori, given the data ([3.7.3](/3.7.3)); Bayesian credible intervals and classical confidence intervals then coincide numerically, though their interpretations differ.

## 2.9. Difficulties with Non-informative Priors; Reference Priors

The search for a prior that is always vague meets several difficulties.

- If the likelihood truly dominates in a given problem, the choice among a range of relatively flat priors cannot matter, so a single "correct" vague prior is unnecessary; if it does not dominate, the choice matters, and the prior has to be justified on substantive grounds anyway.
- For many problems there is no clear choice, since a density that is flat in one parametrization is not flat in another (§2.6.3), and different principles give different answers (the binomial table of §2.7.2).
- Further difficulties arise when averaging over or comparing competing models with improper priors, whose marginal likelihoods are defined only up to arbitrary constants.

A systematic answer is the reference prior, proposed by Bernardo (1979) and developed by Berger, Bernardo and others from the 1980s. The idea is that data and parameters should be maximally linked, so that the influence of the prior is minimal: the prior should be the one from which the experiment is expected to teach the most.

**Definition 2.9.1 (Reference Prior)** Let $T=T(y)$ be a sufficient statistic. The expected information about $\theta$ provided by the experiment under the prior $p(\theta)$ is

$$
I(\Theta,T)=\int p(t)\int p(\theta\mid t)\log\frac{p(\theta\mid t)}{p(\theta)}\,\mathrm{d}\theta\,\mathrm{d}t=\iint p(\theta,t)\log\frac{p(\theta,t)}{p(\theta)p(t)}\,\mathrm{d}\theta\,\mathrm{d}t,
$$
the expected **Kullback–Leibler divergence** of the prior from the posterior, which equals the mutual information between $\theta$ and $T$. A **reference prior** is a prior that maximizes it, $p^*(\theta)=\arg\max_{p(\theta)}I(\Theta,T)$; precisely, it is defined as the limit of such maximizers when the experiment is replicated $k$ times and $k\to\infty$, since for a single experiment the maximizer is often a discrete distribution.

For one-dimensional regular problems, in which the posterior is asymptotically normal, the reference prior coincides with Jeffreys' prior. In multiparameter problems Jeffreys' rule $\lvert\det J(\boldsymbol{\theta})\rvert^{1/2}$ can behave poorly, while reference priors, constructed by ordering the parameters by importance, still give reasonable answers.

In both Jeffreys' and the reference prior approach the prior is chosen by an expectation over the data, not for the specific data set at hand. The prior therefore depends on the sampling model and not only on the likelihood of the observed data, so these priors do not fully respect the **likelihood principle**: binomial and negative binomial sampling, which give proportional likelihoods, lead to different Jeffreys' priors (Question 4).

## Summary

| Model | Conjugate prior and posterior | Predictive distribution | Jeffreys' prior |
|---|---|---|---|
| $y_i\sim\mathrm{Poi}(x_i\theta)$ | $\Gamma(\alpha,\beta)\to\Gamma(\alpha+\sum y_i,\beta+\sum x_i)$ | prior predictive (one count, $x=1$) $\mathrm{NB}\big(\alpha,\frac{\beta}{\beta+1}\big)$ | $\theta^{-1/2}$ |
| $y_i\sim\mathrm{Exp}(\theta)$ | $\Gamma(\alpha,\beta)\to\Gamma(\alpha+n,\beta+n\bar y)$ | | $\theta^{-1}$ |
| $y_i\sim\mathcal{N}(\theta,\sigma^2)$, $\sigma^2$ known | $\mathcal{N}(\mu_0,\tau_0^2)\to\mathcal{N}(\mu_n,\tau_n^2)$, $\frac1{\tau_n^2}=\frac1{\tau_0^2}+\frac n{\sigma^2}$, $\mu_n$ precision-weighted | posterior predictive $\mathcal{N}(\mu_n,\sigma^2+\tau_n^2)$ | $1$ |
| $y_i\sim\mathcal{N}(\theta,\sigma^2)$, $\theta$ known | $\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)\to\mathrm{Inv}\text{-}\chi^2\big(\nu_0+n,\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\big)$ | | $\sigma^{-2}$ on $\sigma^2$, giving $\mathrm{Inv}\text{-}\chi^2(n,v)$ |
| $y\sim\mathrm{Bin}(n,\theta)$ | $\mathrm{Beta}(\alpha,\beta)\to\mathrm{Beta}(\alpha+y,\beta+n-y)$ | beta-binomial | $\mathrm{Beta}(\frac12,\frac12)$ |

- Posteriors are compromises between prior and data; conjugate hyperparameters act as prior data (prior counts and exposure, prior precision, prior degrees of freedom), and for exponential families this is a general fact (Proposition 2.5.1).
- The prior predictive distribution $p(y)$ describes data before the experiment and is a mixture of the sampling distribution over the prior (for Poisson–Gamma, the negative binomial); the posterior predictive distribution $p(\tilde y\mid y)$ mixes over the posterior, and its variance adds sampling variance and posterior uncertainty.
- $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ is the law of $\nu s^2/Z$, $Z\sim\chi^2_\nu$ (Definition 2.4.1); its quantiles come from chi-square quantiles, and medians and intervals, unlike means and modes, carry over from $\sigma^2$ to $\sigma$.
- Non-informative priors: proper vs improper (Definition 2.6.1), with the requirement of a proper posterior; uniformity depends on the parametrization; Jeffreys' prior $J(\theta)^{1/2}$ is invariant (Theorem 2.7.1); pivotal quantities give $p(\theta)\propto1$ for location and $p(\theta)\propto1/\theta$ for scale parameters (Definition 2.8.1); reference priors maximize the expected information and agree with Jeffreys' prior in one dimension (Definition 2.9.1).

## Questions

1. For the traffic accidents (Example 2.2.1), find the posterior predictive distribution of the number of accidents next week, its mean and variance, and the probability of a week without accidents.

   **Answer** With the posterior $\Gamma(32.25,10.5)$ and exposure $\tilde x=1$, $\tilde y\mid y\sim\mathrm{NB}(32.25,\,10.5/11.5)$. Its mean is $\mathbb{E}(\theta\mid y)=32.25/10.5=3.071$ and its variance $\mathbb{E}(\theta\mid y)+\operatorname{Var}(\theta\mid y)=3.071+32.25/10.5^2=3.364$, slightly above the mean because of the uncertainty about $\theta$. The probability of no accident is $(10.5/11.5)^{32.25}=0.053$, a little larger than the plug-in value $\mathrm{e}^{-3.071}=0.046$.
2. In the fish example (Example 2.3.1), how many fish must be measured for the posterior standard deviation of $\theta$ to be at most $0.25\,\mathrm{cm}$? Does the answer depend on the observed lengths?

   **Answer** We need $\frac{1}{\tau_n^2}=\frac1{16}+\frac n4\ge\frac{1}{0.25^2}=16$, that is $n\ge4(16-\frac1{16})=63.75$, so $n=64$. The posterior variance in this model depends only on $n$, $\sigma^2$ and $\tau_0^2$, not on the data, so the sample size can be planned in advance.
3. Find Jeffreys' prior for the Poisson model and the resulting posterior for the traffic data. Compare with the conjugate analysis.

   **Answer** $J(\theta)=1/\theta$ gives $p(\theta)\propto\theta^{-1/2}$, and the posterior is $\Gamma(26+\frac12,8)=\Gamma(26.5,8)$, which is proper for any data since $n\ge1$. Its mean is $3.31$ and its $95\%$ central interval $[2.17,4.69]$. The informative prior with mean $2.5$ pulled the posterior mean down to $3.07$ and narrowed the interval to $[2.10,4.22]$, because it added the equivalent of $2.5$ weeks of data.
4. In the negative binomial model, $y$ is the number of failures before the $r$-th success, $p(y\mid\theta)=\binom{y+r-1}{y}\theta^r(1-\theta)^y$. Find Jeffreys' prior and compare it with the binomial case. What does the comparison say about Jeffreys' prior and the likelihood principle?

   **Answer** $\ell=r\log\theta+y\log(1-\theta)+\text{const}$, so $-\frac{\mathrm{d}^2\ell}{\mathrm{d}\theta^2}=\frac{r}{\theta^2}+\frac{y}{(1-\theta)^2}$. With $\mathbb{E}(y\mid\theta)=r(1-\theta)/\theta$,

   $$
   J(\theta)=\frac{r}{\theta^2}+\frac{r}{\theta(1-\theta)}=\frac{r}{\theta^2(1-\theta)},\qquad p(\theta)\propto\theta^{-1}(1-\theta)^{-1/2},
   $$
   an improper prior, while binomial sampling gives $\mathrm{Beta}(\frac12,\frac12)$. If $r$ successes and $y$ failures are observed, both likelihoods are proportional to $\theta^r(1-\theta)^y$, yet the posteriors under the two Jeffreys' priors are $\mathrm{Beta}(r,y+\frac12)$ and $\mathrm{Beta}(r+\frac12,y+\frac12)$. Inference that should depend only on the likelihood depends on the stopping rule through the prior, because Jeffreys' prior is an expectation over the sample space of the experiment.
5. Let $\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$. Show that $\sigma$ has density proportional to $\sigma^{-(\nu+1)}\exp\big(-\frac{\nu s^2}{2\sigma^2}\big)$ and find its mode. Verify the value $3.656$ for the conjugate posterior of Example 2.4.1.

   **Answer** With $p(\sigma^2)\propto(\sigma^2)^{-(\nu/2+1)}\exp(-\frac{\nu s^2}{2\sigma^2})$ and $\frac{\mathrm{d}\sigma^2}{\mathrm{d}\sigma}=2\sigma$, $p(\sigma)\propto\sigma^{-\nu-2}\cdot\sigma\exp(-\frac{\nu s^2}{2\sigma^2})=\sigma^{-(\nu+1)}\exp(-\frac{\nu s^2}{2\sigma^2})$. The derivative of the logarithm, $-\frac{\nu+1}{\sigma}+\frac{\nu s^2}{\sigma^3}$, vanishes at $\sigma^2=\frac{\nu s^2}{\nu+1}$. In Example 2.4.1, $\nu s^2=160.37$ and $\nu=11$, so the mode is $\sqrt{160.37/12}=3.656$, different from $\sqrt{\operatorname{mode}(\sigma^2\mid y)}=\sqrt{160.37/13}=3.512$: the mode is not invariant under the transformation $\sigma^2\mapsto\sigma$.
6. Write the exponential distribution $p(y\mid\theta)=\theta\mathrm{e}^{-\theta y}$ in exponential-family form, find its conjugate family by Proposition 2.5.1, and give the posterior for $n$ observations. Show that the mean $\lambda=1/\theta$ is a scale parameter and derive $p(\lambda)\propto1/\lambda$ from the pivotal quantity.

   **Answer** $p(y\mid\theta)=\exp(-\theta y+\log\theta)$, so $\phi(\theta)=-\theta$, $u(y)=y$, $g(\theta)=-\log\theta$, $f(y)=1$. The conjugate prior is $\exp(-\nu\theta+n_0\log\theta)=\theta^{n_0}\mathrm{e}^{-\nu\theta}$, the gamma family $\Gamma(n_0+1,\nu)$; with $\theta\sim\Gamma(\alpha,\beta)$ the posterior is $\Gamma(\alpha+n,\beta+n\bar y)$. In terms of the mean, $p(y\mid\lambda)=\frac1\lambda\mathrm{e}^{-y/\lambda}=\frac1\lambda g(y/\lambda)$ with $g(u)=\mathrm{e}^{-u}$, so $y/\lambda\sim\mathrm{Exp}(1)$ is a pivotal quantity and $\lambda$ a scale parameter. By §2.8 the pivotal argument gives $p(\lambda)\propto1/\lambda$, which agrees with Jeffreys' prior for this model (§2.7.2).
