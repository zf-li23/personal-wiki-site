---
title: Standard Distributions and Conjugate Families
description: Reference chapter for Bayesian data analysis. Notation on this site compared with Gelman et al. and scipy.stats, recognizing distributions from kernels, tables of continuous and discrete distributions with densities, means, variances and modes, the relations between them, a summary of conjugate families with prior and posterior predictive distributions, and computing with scipy.
---

Bayesian computations constantly produce products of densities that have to be recognized as members of a known family, and their answers are read off from that family's mean, variance, mode and quantiles. This chapter collects the distributions used in [3.7.1](/3.7.1)–[3.7.3](/3.7.3) and in the rest of the course, in one place and in one notation. Its main purpose is reference: the same distribution is parametrized differently in different books and programs, and confusing a rate with a scale, a variance with a squared scale, or a scale matrix with its inverse is the most common source of wrong numbers. §4.1 sets the notation and compares it with that of Gelman et al., *Bayesian Data Analysis*, whose distribution tables are a standard reference, and with `scipy.stats`; it also describes how a distribution is identified from its kernel. §4.2 and §4.3 tabulate the continuous and discrete distributions, §4.4 lists the relations between them, §4.5 summarizes the conjugate families of the preceding chapters, and §4.6 shows the corresponding computations in Python. Most of the distributions are defined in [3.1](/3.1), [3.4.3](/3.4.3) or [3.7.2](/3.7.2)–[3.7.3](/3.7.3); four further families (Laplace, logistic, log-logistic and LKJ) are defined here.

## 4.1. Notation and Parametrizations

### 4.1.1. Three Conventions

The following table lists, for each distribution, the notation used on this site (the site-wide conventions, with the additions of [3.7.2](/3.7.2)–[3.7.3](/3.7.3)), the notation of Gelman et al., and the corresponding `scipy.stats` object. Parameters with the same letter have the same meaning unless a conversion is shown.

| Distribution | This site | Gelman et al. | `scipy.stats` |
|---|---|---|---|
| uniform | $\mathrm{U}(a,b)$ | $\mathrm{U}(\alpha,\beta)$ | `uniform(loc=a, scale=b-a)` |
| normal | $\mathcal{N}(\mu,\sigma^2)$ | $\mathrm{N}(\mu,\sigma^2)$ | `norm(loc=mu, scale=sigma)` |
| lognormal | $\mathrm{LN}(\mu,\sigma^2)$ | $\mathrm{lognormal}(\mu,\sigma^2)$ | `lognorm(s=sigma, scale=exp(mu))` |
| multivariate normal | $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $\mathrm{N}(\mu,\Sigma)$ | `multivariate_normal(mean=mu, cov=Sigma)` |
| gamma, rate $\beta$ | $\Gamma(\alpha,\beta)$ | $\mathrm{Gamma}(\alpha,\beta)$ | `gamma(a=alpha, scale=1/beta)` |
| inverse-gamma, scale $\beta$ | $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ | $\mathrm{Inv\text{-}gamma}(\alpha,\beta)$ | `invgamma(a=alpha, scale=beta)` |
| chi-square | $\chi^2_\nu$ | $\chi^2_\nu$ | `chi2(df=nu)` |
| inverse-chi-square | $\mathrm{Inv}\text{-}\chi^2_\nu$ | $\mathrm{Inv}\text{-}\chi^2_\nu$ | `invgamma(a=nu/2, scale=1/2)` |
| scaled inverse-chi-square | $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ | $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ | `invgamma(a=nu/2, scale=nu*s2/2)` |
| exponential, rate $\beta$ | $\mathrm{Exp}(\beta)$ | $\mathrm{Expon}(\beta)$ | `expon(scale=1/beta)` |
| Laplace | $\mathrm{Laplace}(\mu,\sigma)$ | $\mathrm{Laplace}(\mu,\sigma)$ | `laplace(loc=mu, scale=sigma)` |
| Weibull | $\mathrm{Weibull}(\alpha,\lambda)$, $\lambda=\beta^{-\alpha}$ | $\mathrm{Weibull}(\alpha,\beta)$, scale $\beta$ | `weibull_min(c=alpha, scale=beta)` |
| Wishart | $W_d(\nu,S)$ | $\mathrm{Wishart}_\nu(S)$ | `wishart(df=nu, scale=S)` |
| inverse-Wishart | $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ | $\mathrm{Inv\text{-}Wishart}_\nu(\Psi^{-1})$ | `invwishart(df=nu, scale=Psi)` |
| LKJ | $\mathrm{LKJ}(\eta)$ | $\mathrm{LkjCorr}(\eta)$ | none (Stan: `lkj_corr(eta)`) |
| $t$, location–scale | $t_\nu(\mu,\sigma^2)$ | $t_\nu(\mu,\sigma^2)$ | `t(df=nu, loc=mu, scale=sigma)` |
| multivariate $t$ | $t_\nu(\boldsymbol{\mu},\Sigma)$ | $t_\nu(\mu,\Sigma)$ | `multivariate_t(loc=mu, shape=Sigma, df=nu)` |
| beta | $\mathrm{Beta}(\alpha,\beta)$ | $\mathrm{Beta}(\alpha,\beta)$ | `beta(a=alpha, b=beta)` |
| Dirichlet | $\mathrm{Dir}(\boldsymbol{\alpha})$ | $\mathrm{Dirichlet}(\alpha_1,\dots,\alpha_k)$ | `dirichlet(alpha)` |
| logistic | $\mathrm{Logistic}(\mu,\sigma)$ | $\mathrm{Logistic}(\mu,\sigma)$ | `logistic(loc=mu, scale=sigma)` |
| log-logistic | $\mathrm{LogLogistic}(\alpha,\beta)$ | $\mathrm{Log\text{-}logistic}(\alpha,\beta)$ | `fisk(c=beta, scale=alpha)` |
| Poisson | $\mathrm{Poi}(\lambda)$ | $\mathrm{Poisson}(\lambda)$ | `poisson(mu=lam)` |
| binomial | $\mathrm{Bin}(n,p)$ | $\mathrm{Bin}(n,p)$ | `binom(n, p)` |
| multinomial | $\mathrm{Mult}(n,\boldsymbol{p})$ | $\mathrm{Multin}(n;p_1,\dots,p_k)$ | `multinomial(n, p)` |
| negative binomial | $\mathrm{NB}\big(\alpha,\frac{\beta}{\beta+1}\big)$ | $\mathrm{Neg\text{-}bin}(\alpha,\beta)$ | `nbinom(n=alpha, p=beta/(beta+1))` |
| beta-binomial | $\mathrm{BetaBin}(n,\alpha,\beta)$ | $\mathrm{Beta\text{-}bin}(n,\alpha,\beta)$ | `betabinom(n, a=alpha, b=beta)` |
| Dirichlet-multinomial | $\mathrm{DirMult}(n,\boldsymbol{\alpha})$ | not tabulated | `dirichlet_multinomial(alpha, n)` |

Gelman et al. also write $p(\theta)=\mathrm{N}(\theta\mid\mu,\sigma^2)$, $\mathrm{Beta}(\theta\mid\alpha,\beta)$ and so on for the density evaluated at $\theta$; we use this form occasionally as well, for instance $\mathcal{N}(\theta\mid\mu_n,\tau_n^2)$ in [3.7.2](/3.7.2).

### 4.1.2. Points to Watch

- *Rate or scale.* In $\Gamma(\alpha,\beta)$ and $\mathrm{Exp}(\beta)$ the parameter $\beta$ is a rate (an inverse scale): the mean is $\alpha/\beta$. In $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ the same letter is a scale: if $X\sim\Gamma(\alpha,\beta)$ then $1/X\sim\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$, with mean $\beta/(\alpha-1)$. scipy always uses a scale: `gamma(a, scale=1/beta)` but `invgamma(a, scale=beta)`.
- *Variance or scale.* $\mathcal{N}(\mu,\sigma^2)$ and $t_\nu(\mu,\sigma^2)$ are written with the squared scale, but scipy's `norm` and `t` take `scale=sigma`. For $t_\nu(\mu,\sigma^2)$, $\sigma^2$ is not the variance: the variance is $\frac{\nu}{\nu-2}\sigma^2$. In `multivariate_normal` the argument is the covariance matrix, in `multivariate_t` the scale matrix `shape`.
- *Scale matrix or its inverse.* Gelman et al. write $\mathrm{Inv\text{-}Wishart}_\nu(\Psi^{-1})$ for the distribution with scale matrix $\Psi$ and mean $\Psi/(\nu-d-1)$; here and in scipy this is $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ ([3.7.3](/3.7.3)). The Wishart notation $W_d(\nu,S)$ of [3.4.3](/3.4.3) has the scale matrix in the argument in all three conventions.
- *Negative binomial.* Both $\mathrm{NB}(r,p)$ here and $\mathrm{Neg\text{-}bin}(\alpha,\beta)$ in Gelman et al. count failures (values $0,1,2,\dots$), with real shape $\alpha>0$ allowed; Gelman et al. parametrize by the gamma parameters of the Poisson–gamma mixture, and $p=\beta/(\beta+1)$. scipy's `nbinom(n, p)` is the same as $\mathrm{NB}(n,p)$.
- *Weibull.* [3.1.4](/3.1.4) writes the density $\lambda\alpha x^{\alpha-1}\mathrm{e}^{-\lambda x^\alpha}$ with a rate-type $\lambda$; Gelman et al. and scipy use the scale $\beta=\lambda^{-1/\alpha}$.
- *Lognormal.* $\mu$ and $\sigma^2$ are the mean and variance of $\log\theta$, not of $\theta$; scipy's `lognorm` takes `s=sigma` and `scale=exp(mu)`.

### 4.1.3. Recognizing a Distribution from Its Kernel

By Bayes' rule a posterior is known once it is known up to a constant, $p(\theta\mid y)\propto p(\theta)p(y\mid\theta)$. In conjugate models the right side, as a function of $\theta$ with everything else fixed, is the kernel of a standard density, and the normalizing constant, moments and quantiles are then those of that family. The kernels to recognize are:

| Kernel in $\theta$ | Range | Distribution |
|---|---|---|
| $\theta^{a-1}\mathrm{e}^{-b\theta}$ | $\theta>0$ | $\Gamma(a,b)$ |
| $\theta^{-(a+1)}\mathrm{e}^{-b/\theta}$ | $\theta>0$ | $\mathrm{Inv}\text{-}\Gamma(a,b)$; with $a=\frac\nu2$, $b=\frac{\nu s^2}{2}$: $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ |
| $\theta^{a-1}(1-\theta)^{b-1}$ | $0<\theta<1$ | $\mathrm{Beta}(a,b)$ |
| $\prod_j\theta_j^{a_j-1}$ | simplex | $\mathrm{Dir}(\boldsymbol{a})$ |
| $\exp\big(-\frac12(A\theta^2-2B\theta)\big)$, $A>0$ | $\mathbb{R}$ | $\mathcal{N}(B/A,1/A)$ |
| $\exp\big(-\frac12(\boldsymbol{\theta}^{\mathsf T}A\boldsymbol{\theta}-2\boldsymbol{b}^{\mathsf T}\boldsymbol{\theta})\big)$ | $\mathbb{R}^d$ | $\mathcal{N}_d(A^{-1}\boldsymbol{b},A^{-1})$ |
| $\big(1+\frac{(\theta-m)^2}{\nu c}\big)^{-(\nu+1)/2}$ | $\mathbb{R}$ | $t_\nu(m,c)$ |
| $\sigma^{-1}(\sigma^2)^{-(\nu/2+1)}\exp\big(-\frac{\nu s^2+\kappa(\mu-m)^2}{2\sigma^2}\big)$ | $(\mu,\sigma^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(m,s^2/\kappa;\nu,s^2)$ |
| $(\det W)^{(\nu-d-1)/2}\exp\big(-\frac12\operatorname{tr}(S^{-1}W)\big)$ | positive definite | $W_d(\nu,S)$ |
| $(\det\Sigma)^{-(\nu+d+1)/2}\exp\big(-\frac12\operatorname{tr}(\Psi\Sigma^{-1})\big)$ | positive definite | $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ |

The normal rows are completing the square: $A$ is the precision and $B/A$ the mean. A kernel can only be matched if it is integrable, which is how improper posteriors are detected: $\theta^{a-1}(1-\theta)^{b-1}$ with $a=0$, or $\theta^{a-1}\mathrm{e}^{-b\theta}$ with $b=0$, is not a density.

**Example 4.1.1** Let $y_1,\dots,y_n\mid\theta\overset{\text{iid}}{\sim}\mathcal{N}(0,1/\theta)$, normal with precision $\theta$, and let $\theta\sim\Gamma(\alpha,\beta)$. Then

$$
p(\theta\mid y)\propto\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}\cdot\theta^{n/2}\exp\Big(-\frac\theta2\sum_iy_i^2\Big)=\theta^{\alpha+n/2-1}\exp\Big(-\Big(\beta+\frac12\sum_iy_i^2\Big)\theta\Big),
$$
so $\theta\mid y\sim\Gamma\big(\alpha+\frac n2,\beta+\frac12\sum_iy_i^2\big)$, with posterior mean $\frac{2\alpha+n}{2\beta+\sum_iy_i^2}$. For the variance $\sigma^2=1/\theta$ this is the inverse-gamma posterior $\mathrm{Inv}\text{-}\Gamma\big(\alpha+\frac n2,\beta+\frac12\sum_iy_i^2\big)$, the analysis of [3.7.2](/3.7.2) in another parametrization: $\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$ is $\mathrm{Inv}\text{-}\Gamma(\frac{\nu_0}2,\frac{\nu_0\sigma_0^2}2)$.

## 4.2. Continuous Distributions

### 4.2.1. Distributions on the Real Line

Besides the normal and the $t$ distributions, two symmetric families with heavier tails than the normal appear in Bayesian modeling.

**Definition 4.2.1 (Laplace Distribution)** Let $\mu\in\mathbb{R}$ and $\sigma>0$. The **Laplace distribution** (double exponential distribution) $\mathrm{Laplace}(\mu,\sigma)$ has density

$$
p(\theta)=\frac{1}{2\sigma}\exp\Big(-\frac{\lvert\theta-\mu\rvert}{\sigma}\Big),\qquad\theta\in\mathbb{R}.
$$

The difference of two independent $\mathrm{Exp}(1/\sigma)$ variables, shifted by $\mu$, is $\mathrm{Laplace}(\mu,\sigma)$. As a prior for regression coefficients it gives a posterior mode equal to the lasso estimate, just as the normal prior gives ridge regression ([3.3.12](/3.3.12)).

**Definition 4.2.2 (Logistic Distribution)** Let $\mu\in\mathbb{R}$ and $\sigma>0$. The **logistic distribution** $\mathrm{Logistic}(\mu,\sigma)$ has distribution function and density

$$
F(\theta)=\frac{1}{1+\mathrm{e}^{-(\theta-\mu)/\sigma}},\qquad p(\theta)=\frac{\mathrm{e}^{-(\theta-\mu)/\sigma}}{\sigma\big(1+\mathrm{e}^{-(\theta-\mu)/\sigma}\big)^2},\qquad\theta\in\mathbb{R}.
$$

Its distribution function is the inverse of the logit, $F(\theta)=\operatorname{logit}^{-1}((\theta-\mu)/\sigma)$, so that $\mu+\sigma\log\frac{U}{1-U}\sim\mathrm{Logistic}(\mu,\sigma)$ for $U\sim\mathrm{U}(0,1)$. A logistic regression is a model in which a latent variable with logistic errors crosses a threshold.

| Distribution | Density | Mean | Variance | Mode |
|---|---|---|---|---|
| $\mathrm{U}(a,b)$, $a<b$ | $\frac{1}{b-a}$, $\theta\in[a,b]$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | none |
| $\mathcal{N}(\mu,\sigma^2)$ | $\frac{1}{\sqrt{2\pi}\sigma}\exp\big(-\frac{(\theta-\mu)^2}{2\sigma^2}\big)$ | $\mu$ | $\sigma^2$ | $\mu$ |
| $t_\nu(\mu,\sigma^2)$ | $\frac{\Gamma(\frac{\nu+1}2)}{\Gamma(\frac\nu2)\sqrt{\nu\pi}\sigma}\big(1+\frac1\nu(\frac{\theta-\mu}{\sigma})^2\big)^{-\frac{\nu+1}{2}}$ | $\mu$ ($\nu>1$) | $\frac{\nu}{\nu-2}\sigma^2$ ($\nu>2$) | $\mu$ |
| $\mathrm{Laplace}(\mu,\sigma)$ | $\frac{1}{2\sigma}\exp\big(-\frac{\lvert\theta-\mu\rvert}{\sigma}\big)$ | $\mu$ | $2\sigma^2$ | $\mu$ |
| $\mathrm{Logistic}(\mu,\sigma)$ | $\frac{\exp(-(\theta-\mu)/\sigma)}{\sigma(1+\exp(-(\theta-\mu)/\sigma))^2}$ | $\mu$ | $\frac{\pi^2}{3}\sigma^2$ | $\mu$ |

The $t$ family contains the **Cauchy distribution** $t_1(\mu,\sigma^2)$, which has no mean, and tends to the normal as $\nu\to\infty$. Compared at equal variance, the normal has the lightest tails, decaying like $\mathrm{e}^{-\theta^2/2}$; the logistic and Laplace tails decay exponentially, and $t$ tails only like a power $\lvert\theta\rvert^{-(\nu+1)}$.

![Shapes of standard distributions. Left: normal, scaled t with 5 degrees of freedom, Laplace and logistic densities, all with mean 0 and variance 1. Middle: their right tails on a logarithmic scale. Right: gamma, inverse-gamma and lognormal densities, all with mean 1 and variance 1/4.](./plots/distribution_shapes.py)

### 4.2.2. Distributions on the Positive Half-Line

**Definition 4.2.3 (Log-logistic Distribution)** Let $\alpha,\beta>0$. A positive random variable $\theta$ has the **log-logistic distribution** $\mathrm{LogLogistic}(\alpha,\beta)$ with scale $\alpha$ and shape $\beta$ if $\log\theta\sim\mathrm{Logistic}(\log\alpha,1/\beta)$, equivalently if

$$
\mathbb{P}(\theta\le x)=\frac{1}{1+(x/\alpha)^{-\beta}},\qquad p(\theta)=\frac{(\beta/\alpha)(\theta/\alpha)^{\beta-1}}{\big(1+(\theta/\alpha)^\beta\big)^2},\qquad\theta>0.
$$

Its median is $\alpha$. It is used in survival analysis because, unlike the Weibull, its hazard can rise and then fall.

| Distribution | Density, $\theta>0$ | Mean | Variance | Mode |
|---|---|---|---|---|
| $\mathrm{LN}(\mu,\sigma^2)$ | $\frac{1}{\sqrt{2\pi}\sigma\theta}\exp\big(-\frac{(\log\theta-\mu)^2}{2\sigma^2}\big)$ | $\mathrm{e}^{\mu+\sigma^2/2}$ | $\mathrm{e}^{2\mu+\sigma^2}(\mathrm{e}^{\sigma^2}-1)$ | $\mathrm{e}^{\mu-\sigma^2}$ |
| $\Gamma(\alpha,\beta)$ | $\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}$ | $\frac\alpha\beta$ | $\frac{\alpha}{\beta^2}$ | $\frac{\alpha-1}{\beta}$ ($\alpha\ge1$) |
| $\mathrm{Exp}(\beta)=\Gamma(1,\beta)$ | $\beta\mathrm{e}^{-\beta\theta}$ | $\frac1\beta$ | $\frac1{\beta^2}$ | $0$ |
| $\chi^2_\nu=\Gamma(\frac\nu2,\frac12)$ | $\frac{2^{-\nu/2}}{\Gamma(\nu/2)}\theta^{\nu/2-1}\mathrm{e}^{-\theta/2}$ | $\nu$ | $2\nu$ | $\nu-2$ ($\nu\ge2$) |
| $\mathrm{Weibull}$, shape $\alpha$, scale $\beta$ | $\frac\alpha\beta\big(\frac\theta\beta\big)^{\alpha-1}\exp\big(-(\frac\theta\beta)^\alpha\big)$ | $\beta\,\Gamma(1+\frac1\alpha)$ | $\beta^2\big[\Gamma(1+\frac2\alpha)-\Gamma(1+\frac1\alpha)^2\big]$ | $\beta(1-\frac1\alpha)^{1/\alpha}$ ($\alpha\ge1$) |
| $\mathrm{LogLogistic}(\alpha,\beta)$ | $\frac{(\beta/\alpha)(\theta/\alpha)^{\beta-1}}{(1+(\theta/\alpha)^\beta)^2}$ | $\frac{\alpha b}{\sin b}$, $b=\frac\pi\beta$ ($\beta>1$) | $\alpha^2\big(\frac{2b}{\sin2b}-\frac{b^2}{\sin^2b}\big)$ ($\beta>2$) | $\alpha\big(\frac{\beta-1}{\beta+1}\big)^{1/\beta}$ ($\beta>1$) |
| $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ | $\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{-(\alpha+1)}\mathrm{e}^{-\beta/\theta}$ | $\frac{\beta}{\alpha-1}$ ($\alpha>1$) | $\frac{\beta^2}{(\alpha-1)^2(\alpha-2)}$ ($\alpha>2$) | $\frac{\beta}{\alpha+1}$ |
| $\mathrm{Inv}\text{-}\chi^2_\nu=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac12)$ | $\frac{2^{-\nu/2}}{\Gamma(\nu/2)}\theta^{-(\nu/2+1)}\mathrm{e}^{-1/(2\theta)}$ | $\frac{1}{\nu-2}$ ($\nu>2$) | $\frac{2}{(\nu-2)^2(\nu-4)}$ ($\nu>4$) | $\frac{1}{\nu+2}$ |
| $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac{\nu s^2}2)$ | $\frac{(\nu/2)^{\nu/2}}{\Gamma(\nu/2)}s^\nu\theta^{-(\nu/2+1)}\mathrm{e}^{-\nu s^2/(2\theta)}$ | $\frac{\nu}{\nu-2}s^2$ ($\nu>2$) | $\frac{2\nu^2}{(\nu-2)^2(\nu-4)}s^4$ ($\nu>4$) | $\frac{\nu}{\nu+2}s^2$ |

The **log-normal distribution**, the gamma and the inverse-gamma can have the same mean and variance and still differ markedly in shape: in the figure above the inverse-gamma has the lightest left tail and the heaviest right tail, because $1/\theta$ is gamma. The inverse-gamma, inverse-chi-square and **scaled inverse-chi-square distribution** are defined in [3.7.2](/3.7.2) (Definition 2.4.1).

In the table of Gelman et al. the entries for the log-logistic distribution should be read with care: the expression given in the mean column, $1/(1+(x/\alpha)^{-\beta})$, is the distribution function, and the one in the variance column, $\alpha^2\frac{2\pi/\beta}{\sin(2\pi/\beta)}$, is the second moment $\mathbb{E}\theta^2$; the mean and variance are the expressions in the table above (verified numerically against `scipy.stats.fisk`).

### 4.2.3. Distributions on the Unit Interval and the Simplex

| Distribution | Density | Mean | Variance and covariance | Mode |
|---|---|---|---|---|
| $\mathrm{Beta}(\alpha,\beta)$ | $\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\theta^{\alpha-1}(1-\theta)^{\beta-1}$, $\theta\in[0,1]$ | $\frac{\alpha}{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | $\frac{\alpha-1}{\alpha+\beta-2}$ ($\alpha,\beta>1$) |
| $\mathrm{Dir}(\boldsymbol{\alpha})$, $\alpha_0=\sum_j\alpha_j$ | $\frac{\Gamma(\alpha_0)}{\prod_j\Gamma(\alpha_j)}\prod_j\theta_j^{\alpha_j-1}$, $\boldsymbol{\theta}$ in the simplex | $\mathbb{E}\theta_j=\frac{\alpha_j}{\alpha_0}$ | $\operatorname{Var}\theta_j=\frac{\alpha_j(\alpha_0-\alpha_j)}{\alpha_0^2(\alpha_0+1)}$, $\operatorname{Cov}(\theta_i,\theta_j)=-\frac{\alpha_i\alpha_j}{\alpha_0^2(\alpha_0+1)}$ | $\frac{\alpha_j-1}{\alpha_0-k}$ (all $\alpha_j>1$) |

Gelman et al. call the parameters of these two families "prior sample sizes", in line with their interpretation as prior counts ([3.7.1](/3.7.1), [3.7.3](/3.7.3)). The **beta distribution** and the **Dirichlet distribution** are defined in [3.1](/3.1) and [3.7.3](/3.7.3) (Definition 3.2.1).

### 4.2.4. Multivariate Distributions

Hierarchical models for vectors need priors for covariance matrices. The inverse-Wishart prior ties the variances and correlations together; a modern alternative separates them, $\Sigma=\operatorname{diag}(\boldsymbol{\tau})\,\Omega\,\operatorname{diag}(\boldsymbol{\tau})$, with scales $\boldsymbol{\tau}$ and a correlation matrix $\Omega$ that receive separate priors. For $\Omega$ the standard choice is the following family, due to Lewandowski, Kurowicka and Joe (2009).

**Definition 4.2.4 (LKJ Distribution)** Let $\eta>0$. The **LKJ distribution** $\mathrm{LKJ}(\eta)$ on the set of $d\times d$ correlation matrices (symmetric positive definite with unit diagonal) has density

$$
p(\Omega)\propto(\det\Omega)^{\eta-1}.
$$

For $\eta=1$ it is uniform over correlation matrices; for $\eta>1$ it concentrates around the identity matrix, and for $\eta<1$ it favors strong correlations. Each correlation $\omega_{ij}$ satisfies $\frac{\omega_{ij}+1}{2}\sim\mathrm{Beta}(\eta-1+\frac d2,\eta-1+\frac d2)$, so $\mathbb{E}\Omega=I_d$ and $\operatorname{Var}\omega_{ij}=\frac{1}{2\eta+d-1}$. For $d=2$ the density of the single correlation $r$ is proportional to $(1-r^2)^{\eta-1}$.

| Distribution | Density | Mean | Variance | Mode |
|---|---|---|---|---|
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $(2\pi)^{-d/2}(\det\Sigma)^{-1/2}\exp\big(-\frac12(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\big)$ | $\boldsymbol{\mu}$ | $\Sigma$ | $\boldsymbol{\mu}$ |
| $t_\nu(\boldsymbol{\mu},\Sigma)$ | $\frac{\Gamma(\frac{\nu+d}2)}{\Gamma(\frac\nu2)(\nu\pi)^{d/2}}(\det\Sigma)^{-1/2}\big(1+\frac1\nu(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\big)^{-\frac{\nu+d}2}$ | $\boldsymbol{\mu}$ ($\nu>1$) | $\frac{\nu}{\nu-2}\Sigma$ ($\nu>2$) | $\boldsymbol{\mu}$ |
| $W_d(\nu,S)$, $\nu>d-1$ | $\frac{(\det W)^{(\nu-d-1)/2}\exp(-\frac12\operatorname{tr}(S^{-1}W))}{2^{\nu d/2}(\det S)^{\nu/2}\Gamma_d(\nu/2)}$ | $\nu S$ | $\operatorname{Var}W_{ij}=\nu(s_{ij}^2+s_{ii}s_{jj})$ | $(\nu-d-1)S$ ($\nu\ge d+1$) |
| $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$, $\nu>d-1$ | $\frac{(\det\Psi)^{\nu/2}(\det\Sigma)^{-(\nu+d+1)/2}\exp(-\frac12\operatorname{tr}(\Psi\Sigma^{-1}))}{2^{\nu d/2}\Gamma_d(\nu/2)}$ | $\frac{\Psi}{\nu-d-1}$ ($\nu>d+1$) | | $\frac{\Psi}{\nu+d+1}$ |
| $\mathrm{LKJ}(\eta)$ | $\propto(\det\Omega)^{\eta-1}$ | $I_d$ | $\operatorname{Var}\omega_{ij}=\frac{1}{2\eta+d-1}$ | $I_d$ ($\eta>1$) |

Here $\Gamma_d(a)=\pi^{d(d-1)/4}\prod_{i=1}^d\Gamma(a+\frac{1-i}{2})$ is the multivariate gamma function. The **multivariate normal distribution** is defined in [3.1](/3.1), the **Wishart distribution** in [3.4.3](/3.4.3), the **inverse-Wishart distribution** and the **multivariate t-distribution** in [3.7.3](/3.7.3) (Definitions 3.6.1 and 3.6.2).

## 4.3. Discrete Distributions

The beta-binomial and the Dirichlet-multinomial are the prior predictive distributions of the binomial–beta and multinomial–Dirichlet models. The latter is the multivariate beta-binomial: we say that $\boldsymbol{\theta}=(\theta_1,\dots,\theta_k)$ has the *Dirichlet-multinomial distribution* $\mathrm{DirMult}(n,\boldsymbol{\alpha})$ if $\boldsymbol{\theta}\mid\boldsymbol{p}\sim\mathrm{Mult}(n,\boldsymbol{p})$ with $\boldsymbol{p}\sim\mathrm{Dir}(\boldsymbol{\alpha})$; integrating $\boldsymbol{p}$ out gives the probability function in the table.

| Distribution | Probability function | Mean | Variance and covariance | Mode |
|---|---|---|---|---|
| $\mathrm{Poi}(\lambda)$ | $\frac{\lambda^\theta}{\theta!}\mathrm{e}^{-\lambda}$, $\theta=0,1,\dots$ | $\lambda$ | $\lambda$ | $\lfloor\lambda\rfloor$ |
| $\mathrm{Bin}(n,p)$ | $\binom n\theta p^\theta(1-p)^{n-\theta}$, $\theta=0,\dots,n$ | $np$ | $np(1-p)$ | $\lfloor(n+1)p\rfloor$ |
| $\mathrm{Mult}(n,\boldsymbol{p})$ | $\frac{n!}{\theta_1!\cdots\theta_k!}p_1^{\theta_1}\cdots p_k^{\theta_k}$, $\sum_j\theta_j=n$ | $np_j$ | $np_j(1-p_j)$; $\operatorname{Cov}(\theta_i,\theta_j)=-np_ip_j$ | |
| $\mathrm{NB}\big(\alpha,\frac{\beta}{\beta+1}\big)$ | $\binom{\theta+\alpha-1}{\theta}\big(\frac{\beta}{\beta+1}\big)^\alpha\big(\frac{1}{\beta+1}\big)^\theta$, $\theta=0,1,\dots$ | $\frac\alpha\beta$ | $\frac{\alpha}{\beta^2}(\beta+1)$ | $\lfloor\frac{\alpha-1}{\beta}\rfloor$ ($\alpha>1$), else $0$ |
| $\mathrm{BetaBin}(n,\alpha,\beta)$ | $\binom n\theta\frac{\mathrm{B}(\alpha+\theta,\beta+n-\theta)}{\mathrm{B}(\alpha,\beta)}$, $\theta=0,\dots,n$ | $\frac{n\alpha}{\alpha+\beta}$ | $\frac{n\alpha\beta(\alpha+\beta+n)}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | |
| $\mathrm{DirMult}(n,\boldsymbol{\alpha})$ | $\frac{n!}{\prod_j\theta_j!}\frac{\Gamma(\alpha_0)}{\Gamma(\alpha_0+n)}\prod_j\frac{\Gamma(\alpha_j+\theta_j)}{\Gamma(\alpha_j)}$, $\sum_j\theta_j=n$ | $\frac{n\alpha_j}{\alpha_0}$ | $\frac{n\alpha_j(\alpha_0-\alpha_j)(\alpha_0+n)}{\alpha_0^2(\alpha_0+1)}$ | |

In the negative binomial row, $\binom{\theta+\alpha-1}{\theta}=\frac{\Gamma(\theta+\alpha)}{\Gamma(\alpha)\,\theta!}$ for real $\alpha$. The Poisson mode is also attained at $\lambda-1$ when $\lambda$ is an integer, and similarly for the binomial at $(n+1)p-1$ when $(n+1)p$ is an integer. Compared with the binomial and multinomial with the same mean, the beta-binomial and the Dirichlet-multinomial are overdispersed by the factor $\frac{\alpha_0+n}{\alpha_0+1}$ (with $\alpha_0=\alpha+\beta$ for the beta-binomial), just as the negative binomial is overdispersed relative to the Poisson. The **Poisson distribution**, the **binomial distribution**, the **negative binomial distribution** and the **multinomial distribution** are defined in [3.1](/3.1), the **beta-binomial distribution** in [3.2.7](/3.2.7).

## 4.4. Relations Between Distributions

Most of the distributions above are built from a few: the gamma (with the exponential and chi-square), the normal, and their inverses, ratios and mixtures. The relations below are used constantly, both to derive posteriors and to compute with them.

| Relation | Statement |
|---|---|
| gamma family | $\mathrm{Exp}(\beta)=\Gamma(1,\beta)$, $\chi^2_\nu=\Gamma(\frac\nu2,\frac12)$; if $X\sim\Gamma(\alpha,\beta)$ then $cX\sim\Gamma(\alpha,\beta/c)$ and $2\beta X\sim\chi^2_{2\alpha}$; independent $\Gamma(\alpha_i,\beta)$ add to $\Gamma(\sum_i\alpha_i,\beta)$ |
| inverses | $X\sim\Gamma(\alpha,\beta)\iff1/X\sim\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$; $\mathrm{Inv}\text{-}\chi^2_\nu=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac12)$; $X\sim\mathrm{Inv}\text{-}\chi^2(\nu,s^2)\iff\nu s^2/X\sim\chi^2_\nu$, so $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac{\nu s^2}{2})$ |
| distribution functions of inverses | $\mathbb{P}(X\le x)=1-F_G(1/x)$ where $F_G$ is the gamma distribution function; the lower $p$ quantile of $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ is $1/F_G^{-1}(1-p)$; the lower $p$ quantile of $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ is $\nu s^2/\chi^2_{\nu,p}$, with $\chi^2_{\nu,p}$ the upper $p$ quantile of $\chi^2_\nu$ |
| beta and Dirichlet | for independent $G_j\sim\Gamma(\alpha_j,1)$, $(G_j/\sum_iG_i)_j\sim\mathrm{Dir}(\boldsymbol{\alpha})$; $\mathrm{Dir}(\alpha_1,\alpha_2)$ is $\mathrm{Beta}(\alpha_1,\alpha_2)$; merged components are Dirichlet, single components Beta (Proposition 3.2.1) |
| normal scale mixtures | $\theta\mid V\sim\mathcal{N}(\mu,V)$ with $V\sim\mathrm{Inv}\text{-}\chi^2(\nu,\sigma^2)$ gives $\theta\sim t_\nu(\mu,\sigma^2)$; with $V\sim\mathrm{Exp}(1/(2\sigma^2))$ (mean $2\sigma^2$) it gives $\theta\sim\mathrm{Laplace}(\mu,\sigma)$; $t_1$ is Cauchy and $t_\nu\to\mathcal{N}$ as $\nu\to\infty$ |
| multivariate $t$ | $\boldsymbol{\mu}+\boldsymbol{z}/\sqrt{u/\nu}\sim t_\nu(\boldsymbol{\mu},\Sigma)$ for independent $\boldsymbol{z}\sim\mathcal{N}_d(\boldsymbol{0},\Sigma)$, $u\sim\chi^2_\nu$; $\frac1d(\boldsymbol{\theta}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{\theta}-\boldsymbol{\mu})\sim F_{d,\nu}$ |
| normal-inverse-chi-square marginals | if $(\mu,\sigma^2)\sim\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\sigma_0^2/\kappa_0;\nu_0,\sigma_0^2)$ then $\mu\sim t_{\nu_0}(\mu_0,\sigma_0^2/\kappa_0)$ and $\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$ ([3.7.3](/3.7.3)) |
| count mixtures | $\mathrm{Poi}(\theta)$ with $\theta\sim\Gamma(\alpha,\beta)$ is $\mathrm{NB}(\alpha,\frac{\beta}{\beta+1})$ ([3.7.2](/3.7.2)); $\mathrm{Bin}(n,\theta)$ with $\theta\sim\mathrm{Beta}(\alpha,\beta)$ is $\mathrm{BetaBin}(n,\alpha,\beta)$ ([3.7.1](/3.7.1)); $\mathrm{Mult}(n,\boldsymbol{p})$ with $\boldsymbol{p}\sim\mathrm{Dir}(\boldsymbol{\alpha})$ is $\mathrm{DirMult}(n,\boldsymbol{\alpha})$ |
| logarithms | $\theta\sim\mathrm{LN}(\mu,\sigma^2)\iff\log\theta\sim\mathcal{N}(\mu,\sigma^2)$; $\theta\sim\mathrm{LogLogistic}(\alpha,\beta)\iff\log\theta\sim\mathrm{Logistic}(\log\alpha,1/\beta)$ |
| Wishart in one dimension | $W_1(\nu,s^2)=s^2\chi^2_\nu$; $\mathrm{Inv}\text{-}W_1(\nu,\psi)=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac\psi2)=\mathrm{Inv}\text{-}\chi^2(\nu,\psi/\nu)$; the diagonal entries of $W\sim W_d(\nu,S)$ are $s_{ii}\chi^2_\nu$ |

The quantile rule for the scaled inverse-chi-square is the one used by hand, with a chi-square table, as in Example 2.4.1: since $\nu s^2/X\sim\chi^2_\nu$ is a decreasing function of $X$, the event $X\le\nu s^2/c$ is the event $\nu s^2/X\ge c$.

## 4.5. Conjugate Families

The first table summarizes the conjugate analyses of [3.7.1](/3.7.1)–[3.7.3](/3.7.3) and the standard non-informative priors, the second the corresponding predictive distributions. In each row the data are $n$ iid observations unless stated otherwise, with $\bar y$ the sample mean, $s^2$ the sample variance, $S$ the sum-of-squares matrix about $\bar{\boldsymbol{y}}$, and, for a known mean $\theta$ or $\boldsymbol{\mu}$, $v=\frac1n\sum_i(y_i-\theta)^2$ and $S_0=\sum_i(\boldsymbol{y}_i-\boldsymbol{\mu})(\boldsymbol{y}_i-\boldsymbol{\mu})^{\mathsf T}$.

| Model | Conjugate prior | Posterior | Non-informative prior |
|---|---|---|---|
| $y\sim\mathrm{Bin}(n,\theta)$ | $\mathrm{Beta}(\alpha,\beta)$ | $\mathrm{Beta}(\alpha+y,\beta+n-y)$ | Jeffreys $\mathrm{Beta}(\frac12,\frac12)$; uniform $\mathrm{Beta}(1,1)$ |
| $y_i\sim\mathrm{Poi}(x_i\theta)$, exposures $x_i$ | $\Gamma(\alpha,\beta)$ | $\Gamma(\alpha+\sum_iy_i,\beta+\sum_ix_i)$ | Jeffreys $\theta^{-1/2}$ |
| $y_i\sim\mathrm{Exp}(\theta)$ | $\Gamma(\alpha,\beta)$ | $\Gamma(\alpha+n,\beta+n\bar y)$ | Jeffreys $\theta^{-1}$ |
| $y_i\sim\mathcal{N}(\theta,\sigma^2)$, $\sigma^2$ known | $\mathcal{N}(\mu_0,\tau_0^2)$ | $\mathcal{N}(\mu_n,\tau_n^2)$, $\frac1{\tau_n^2}=\frac1{\tau_0^2}+\frac n{\sigma^2}$, $\mu_n=\tau_n^2\big(\frac{\mu_0}{\tau_0^2}+\frac{n\bar y}{\sigma^2}\big)$ | flat: $\mathcal{N}(\bar y,\frac{\sigma^2}n)$ |
| $y_i\sim\mathcal{N}(\theta,\sigma^2)$, $\theta$ known | $\mathrm{Inv}\text{-}\chi^2(\nu_0,\sigma_0^2)$ | $\mathrm{Inv}\text{-}\chi^2\big(\nu_0+n,\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\big)$ | Jeffreys $\sigma^{-2}$: $\mathrm{Inv}\text{-}\chi^2(n,v)$ |
| $y_i\sim\mathcal{N}(\mu,\sigma^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_0,\frac{\sigma_0^2}{\kappa_0};\nu_0,\sigma_0^2)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}\chi^2(\mu_n,\frac{\sigma_n^2}{\kappa_n};\nu_n,\sigma_n^2)$ (Theorem 3.4.1) | $\sigma^{-2}$: $\mu\mid y\sim t_{n-1}(\bar y,\frac{s^2}n)$, $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$ |
| $\boldsymbol{y}\sim\mathrm{Mult}(n,\boldsymbol{\theta})$ | $\mathrm{Dir}(\boldsymbol{\alpha})$ | $\mathrm{Dir}(\boldsymbol{\alpha}+\boldsymbol{y})$ | Jeffreys $\mathrm{Dir}(\frac12,\dots,\frac12)$; uniform $\mathrm{Dir}(1,\dots,1)$ |
| $\boldsymbol{y}_i\sim\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$, $\Sigma$ known | $\mathcal{N}_d(\boldsymbol{\mu}_0,\Lambda_0)$ | $\mathcal{N}_d(\boldsymbol{\mu}_n,\Lambda_n)$, $\Lambda_n^{-1}=\Lambda_0^{-1}+n\Sigma^{-1}$, $\boldsymbol{\mu}_n=\Lambda_n(\Lambda_0^{-1}\boldsymbol{\mu}_0+n\Sigma^{-1}\bar{\boldsymbol{y}})$ | flat: $\mathcal{N}_d(\bar{\boldsymbol{y}},\frac\Sigma n)$ |
| $\boldsymbol{y}_i\sim\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$, $\boldsymbol{\mu}$ known | $\mathrm{Inv}\text{-}W_d(\nu_0,\Lambda_0)$ | $\mathrm{Inv}\text{-}W_d(\nu_0+n,\Lambda_0+S_0)$ | $(\det\Sigma)^{-(d+1)/2}$: $\mathrm{Inv}\text{-}W_d(n,S_0)$ |
| $\boldsymbol{y}_i\sim\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_0,\frac{\Lambda_0}{\kappa_0};\nu_0,\Lambda_0)$ | $\mathcal{N}\text{-}\mathrm{Inv}\text{-}W(\boldsymbol{\mu}_n,\frac{\Lambda_n}{\kappa_n};\nu_n,\Lambda_n)$ (Theorem 3.6.1) | $(\det\Sigma)^{-(d+1)/2}$: $\boldsymbol{\mu}\mid\boldsymbol{y}\sim t_{n-d}(\bar{\boldsymbol{y}},\frac{S}{n(n-d)})$, $\Sigma\mid\boldsymbol{y}\sim\mathrm{Inv}\text{-}W_d(n-1,S)$ |

| Model | Prior predictive of one observation | Posterior predictive of one new observation |
|---|---|---|
| $y\sim\mathrm{Bin}(n,\theta)$, Beta prior | $y\sim\mathrm{BetaBin}(n,\alpha,\beta)$ | $\tilde y$ in $\tilde n$ new trials: $\mathrm{BetaBin}(\tilde n,\alpha+y,\beta+n-y)$ |
| $\mathrm{Poi}(x\theta)$, gamma prior | $\mathrm{NB}\big(\alpha,\frac{\beta}{\beta+x}\big)$ | exposure $\tilde x$: $\mathrm{NB}\big(\alpha',\frac{\beta'}{\beta'+\tilde x}\big)$ with the posterior $\Gamma(\alpha',\beta')$ |
| $\mathrm{Exp}(\theta)$, gamma prior | $p(y)=\frac{\alpha\beta^\alpha}{(\beta+y)^{\alpha+1}}$, $y>0$ | the same with $(\alpha+n,\beta+n\bar y)$ |
| $\mathcal{N}(\theta,\sigma^2)$, $\sigma^2$ known | $\mathcal{N}(\mu_0,\sigma^2+\tau_0^2)$ | $\mathcal{N}(\mu_n,\sigma^2+\tau_n^2)$ |
| $\mathcal{N}(\theta,\sigma^2)$, $\theta$ known | $t_{\nu_0}(\theta,\sigma_0^2)$ | $t_{\nu_0+n}\big(\theta,\frac{\nu_0\sigma_0^2+nv}{\nu_0+n}\big)$ |
| $\mathcal{N}(\mu,\sigma^2)$, conjugate prior | $t_{\nu_0}\big(\mu_0,\frac{\kappa_0+1}{\kappa_0}\sigma_0^2\big)$ | $t_{\nu_n}\big(\mu_n,\frac{\kappa_n+1}{\kappa_n}\sigma_n^2\big)$; with $\sigma^{-2}$: $t_{n-1}\big(\bar y,(1+\frac1n)s^2\big)$ |
| $\mathrm{Mult}(n,\boldsymbol{\theta})$, Dirichlet prior | $\boldsymbol{y}\sim\mathrm{DirMult}(n,\boldsymbol{\alpha})$ | $\mathbb{P}(\tilde y=j\mid\boldsymbol{y})=\frac{\alpha_j+y_j}{\alpha_0+n}$; $m$ new: $\mathrm{DirMult}(m,\boldsymbol{\alpha}+\boldsymbol{y})$ |
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$, $\Sigma$ known | $\mathcal{N}_d(\boldsymbol{\mu}_0,\Sigma+\Lambda_0)$ | $\mathcal{N}_d(\boldsymbol{\mu}_n,\Sigma+\Lambda_n)$ |
| $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$, conjugate prior | $t_{\nu_0-d+1}\big(\boldsymbol{\mu}_0,\frac{(\kappa_0+1)\Lambda_0}{\kappa_0(\nu_0-d+1)}\big)$ | $t_{\nu_n-d+1}\big(\boldsymbol{\mu}_n,\frac{(\kappa_n+1)\Lambda_n}{\kappa_n(\nu_n-d+1)}\big)$ |

All the $t$ entries are instances of the normal scale mixture of §4.4, and all the count entries of the count mixtures. Every conjugate prior can be read as prior data (prior counts, prior exposure, prior observations $\kappa_0$ for a mean and $\nu_0$ for a variance), and every non-informative prior in the table is a limit of the conjugate family; in the normal models these limits reproduce the classical pivotal quantities ([3.7.3](/3.7.3)).

## 4.6. Computing with scipy

The conversions of §4.1 in code, checked against results of the earlier chapters:

```python
import numpy as np
from scipy import stats

# Gamma(alpha, beta), beta a rate: scipy's scale is 1/beta
post = stats.gamma(32.25, scale=1 / 10.5)               # traffic accidents (Example 2.2.1)
print(np.round([post.mean(), *post.ppf([0.025, 0.975]), post.sf(3)], 4))

# Inv-chi2(nu, s2) = Inv-Gamma(nu/2, nu*s2/2): scipy's invgamma has scale = nu*s2/2
nu, nus2 = 11, 160.37                                   # powder milk (Example 2.4.1)
sigma2 = stats.invgamma(nu / 2, scale=nus2 / 2)
print(np.round(np.sqrt(sigma2.ppf([0.025, 0.5, 0.975])), 3))
# the same quantiles by hand: nu*s2 divided by upper chi-square quantiles
print(np.round(np.sqrt(nus2 / stats.chi2(nu).ppf([0.975, 0.5, 0.025])), 3))

# t_nu(mu, sigma^2): scipy's scale is sigma, not sigma^2
mu_post = stats.t(24, loc=42.208, scale=np.sqrt(95.618 / 24 / 25))  # cheese, Ann (Example 3.4.1)
print(np.round(mu_post.ppf([0.025, 0.975]), 2))

# NB(alpha, beta/(beta+1)) = Gelman et al.'s Neg-bin(alpha, beta): scipy's nbinom(n, p) counts failures
pred = stats.nbinom(32.25, 10.5 / 11.5)                 # next week's accidents
print(np.round([pred.mean(), pred.var(), pred.pmf(0)], 3))

# Inv-W_d(nu, Psi) = Gelman et al.'s Inv-Wishart_nu(Psi^{-1}): scipy uses the scale matrix Psi
Psi = np.array([[2.0, 0.5], [0.5, 1.0]])
draws = stats.invwishart(df=7, scale=Psi).rvs(size=100000, random_state=0)
print(np.round(draws.mean(axis=0), 3), np.round(Psi / (7 - 2 - 1), 3), sep="\n")
```

```text
[3.0714 2.1043 4.2186 0.5296]
[2.705 3.938 6.483]
[2.705 3.938 6.483]
[41.38 43.03]
[3.071 3.364 0.053]
[[0.496 0.124]
 [0.124 0.249]]
[[0.5   0.125]
 [0.125 0.25 ]]
```

The numbers reproduce Example 2.2.1, the interval $[2.70,6.48]$ for $\sigma$ in Example 2.4.1 (computed both with `invgamma` and with chi-square quantiles), Ann's interval in Example 3.4.1, and the predictive distribution of next week's accidents from [3.7.2](/3.7.2); the simulated mean of the inverse-Wishart draws agrees with $\Psi/(\nu-d-1)$, which confirms that scipy's `scale` is $\Psi$ and not $\Psi^{-1}$. When a distribution is missing from scipy, it can be simulated through the relations of §4.4: a scaled inverse-chi-square as $\nu s^2/X$ with $X\sim\chi^2_\nu$, a Dirichlet through normalized gamma variables, a normal-inverse-chi-square pair by drawing $\sigma^2$ and then $\mu\mid\sigma^2$.

## Summary

- Notation: $\Gamma(\alpha,\beta)$ and $\mathrm{Exp}(\beta)$ with rate $\beta$; $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ with scale $\beta$; $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma(\frac\nu2,\frac{\nu s^2}2)$; $t_\nu(\mu,\sigma^2)$ with squared scale $\sigma^2$ and variance $\frac{\nu}{\nu-2}\sigma^2$; $\mathrm{NB}(\alpha,\frac{\beta}{\beta+1})$ for Gelman et al.'s $\mathrm{Neg\text{-}bin}(\alpha,\beta)$; $\mathrm{Inv}\text{-}W_d(\nu,\Psi)$ for their $\mathrm{Inv\text{-}Wishart}_\nu(\Psi^{-1})$ (§4.1.1).
- scipy uses scales throughout: `gamma(a, scale=1/beta)`, `invgamma(a, scale=beta)`, `norm(loc, scale=sigma)`, `t(df, loc, scale=sigma)`, `invwishart(df, scale=Psi)`.
- Posteriors in conjugate models are identified from their kernels (§4.1.3); a kernel that is not integrable signals an improper posterior.
- New families defined here: Laplace (Definition 4.2.1), logistic (Definition 4.2.2), log-logistic (Definition 4.2.3), LKJ for correlation matrices (Definition 4.2.4), and the Dirichlet-multinomial (§4.3).
- Relations (§4.4): inverses of gamma variables; Dirichlet from normalized gammas; the $t$ and Laplace distributions as normal scale mixtures; negative binomial, beta-binomial and Dirichlet-multinomial as count mixtures; quantiles of inverse distributions from those of the gamma and chi-square.
- Conjugate families with posteriors, non-informative priors and predictive distributions are tabulated in §4.5.

## Questions

1. A colleague reports a posterior $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(10,4)$. Give the same distribution as an inverse-gamma, write the scipy call, and compute the posterior median of $\sigma$ with a chi-square table, given $\chi^2_{10,0.5}=9.342$.

   **Answer** $\mathrm{Inv}\text{-}\chi^2(10,4)=\mathrm{Inv}\text{-}\Gamma(5,20)$, since $\frac{\nu s^2}{2}=\frac{10\times4}{2}=20$; in scipy, `invgamma(5, scale=20)`. Since $\sigma^2=40/X$ with $X\sim\chi^2_{10}$, the median of $\sigma^2$ is $40/9.342=4.282$, and the median of $\sigma$ is $\sqrt{4.282}=2.069$ (medians are preserved by the increasing map $\sigma^2\mapsto\sigma$). The mean $\frac{10}{8}\times4=5$ and the mode $\frac{10}{12}\times4=3.33$ of $\sigma^2$ bracket the scale $s^2=4$.
2. Gelman et al.'s table gives $\theta\sim\mathrm{Neg\text{-}bin}(\alpha,\beta)$ with mean $\alpha/\beta$ and variance $\frac{\alpha}{\beta^2}(\beta+1)$. Show that these agree with the moments of $\mathrm{NB}(r,p)$, $\mathbb{E}\theta=\frac{r(1-p)}{p}$ and $\operatorname{Var}\theta=\frac{r(1-p)}{p^2}$, under $r=\alpha$, $p=\frac{\beta}{\beta+1}$, and give the scipy call.

   **Answer** With $p=\frac{\beta}{\beta+1}$, $\frac{1-p}{p}=\frac{1/(\beta+1)}{\beta/(\beta+1)}=\frac1\beta$, so $\mathbb{E}\theta=\frac\alpha\beta$, and $\frac{1-p}{p^2}=\frac1\beta\cdot\frac{\beta+1}{\beta}$, so $\operatorname{Var}\theta=\frac{\alpha(\beta+1)}{\beta^2}$. In scipy: `nbinom(n=alpha, p=beta/(beta+1))`.
3. Identify the distribution with kernel $p(\theta\mid y)\propto\theta^{-7}\exp(-12/\theta)$, $\theta>0$, in three notations, and give its mean and mode.

   **Answer** The kernel $\theta^{-(\alpha+1)}\mathrm{e}^{-\beta/\theta}$ with $\alpha=6$, $\beta=12$ is $\mathrm{Inv}\text{-}\Gamma(6,12)$, which is $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)$ with $\frac\nu2=6$, $\frac{\nu s^2}2=12$, that is $\mathrm{Inv}\text{-}\chi^2(12,2)$; in scipy, `invgamma(6, scale=12)`. The mean is $\frac{12}{5}=2.4$ and the mode $\frac{12}{7}=1.714$.
4. In scipy, `stats.t(df=5, loc=0, scale=2)` is used for a $t_5(0,4)$ prior. Is it correct? What are the variance and the $97.5\%$ quantile of this distribution? What would `stats.t(df=5, loc=0, scale=4)` be in our notation?

   **Answer** Yes: $t_5(0,4)$ has squared scale $\sigma^2=4$, so `scale=2`. Its variance is $\frac{5}{3}\times4=6.67$, not $4$, and its $97.5\%$ quantile is $2\,t_{5,0.025}=2\times2.571=5.14$. The call with `scale=4` is $t_5(0,16)$, with variance $26.7$: confusing the scale with its square changes the spread by a factor of $2$.
5. Show that if $\theta\mid V\sim\mathcal{N}(\mu,V)$ and $V\sim\mathrm{Exp}(\lambda)$ (rate $\lambda$), then $\theta$ has the Laplace distribution, and find its scale parameter. (Use $\int_0^\infty V^{-1/2}\exp(-\frac{a}{V}-bV)\,\mathrm{d}V=\sqrt{\pi/b}\,\mathrm{e}^{-2\sqrt{ab}}$ for $a\ge0$, $b>0$.)

   **Answer** $p(\theta)=\int_0^\infty\frac{1}{\sqrt{2\pi V}}\mathrm{e}^{-(\theta-\mu)^2/(2V)}\lambda\mathrm{e}^{-\lambda V}\,\mathrm{d}V=\frac{\lambda}{\sqrt{2\pi}}\sqrt{\frac\pi\lambda}\exp\big(-2\sqrt{\lambda(\theta-\mu)^2/2}\big)=\sqrt{\frac\lambda2}\exp\big(-\sqrt{2\lambda}\lvert\theta-\mu\rvert\big)$, with $a=(\theta-\mu)^2/2$ and $b=\lambda$. This is $\mathrm{Laplace}(\mu,\sigma)$ with $\sigma=1/\sqrt{2\lambda}$, that is, $\lambda=\frac{1}{2\sigma^2}$ and $\mathbb{E}V=2\sigma^2$, consistent with $\operatorname{Var}\theta=\mathbb{E}V=2\sigma^2$.
6. Let $\Sigma\sim\mathrm{Inv}\text{-}W_2(\nu,\Psi)$ be a prior for a $2\times2$ covariance matrix. Choose $\nu$ and $\Psi$ so that the prior mean is the identity matrix, and write the prior in the notation of Gelman et al. What does a larger $\nu$ with the same mean express?

   **Answer** $\mathbb{E}\Sigma=\Psi/(\nu-3)$ for $\nu>3$, so $\Psi=(\nu-3)I_2$; for instance $\nu=5$, $\Psi=2I_2$. In the notation of Gelman et al. this is $\mathrm{Inv\text{-}Wishart}_5\big((2I_2)^{-1}\big)=\mathrm{Inv\text{-}Wishart}_5(\frac12I_2)$, and in scipy `invwishart(df=5, scale=2*np.eye(2))`. A larger $\nu$ with $\Psi=(\nu-3)I_2$ keeps the mean and concentrates the prior around it: $\nu$ is the number of prior observations for the covariance matrix ([3.7.3](/3.7.3)), and $\Psi$ the corresponding prior sum of squares.
7. Derive the prior predictive density $p(y)=\frac{\alpha\beta^\alpha}{(\beta+y)^{\alpha+1}}$ of one exponential observation $y\mid\theta\sim\mathrm{Exp}(\theta)$ with $\theta\sim\Gamma(\alpha,\beta)$, and its mean.

   **Answer** $p(y)=\int_0^\infty\theta\mathrm{e}^{-\theta y}\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{\alpha-1}\mathrm{e}^{-\beta\theta}\,\mathrm{d}\theta=\frac{\beta^\alpha}{\Gamma(\alpha)}\cdot\frac{\Gamma(\alpha+1)}{(\beta+y)^{\alpha+1}}=\frac{\alpha\beta^\alpha}{(\beta+y)^{\alpha+1}}$, recognizing the $\Gamma(\alpha+1,\beta+y)$ kernel. By the **law of total expectation**, $\mathbb{E}y=\mathbb{E}[\mathbb{E}(y\mid\theta)]=\mathbb{E}(1/\theta)=\frac{\beta}{\alpha-1}$ for $\alpha>1$, the mean of $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$. The tail $\mathbb{P}(y>t)=(\frac{\beta}{\beta+t})^\alpha$ decays only polynomially: mixing exponentials over an unknown rate produces a heavy-tailed distribution.
