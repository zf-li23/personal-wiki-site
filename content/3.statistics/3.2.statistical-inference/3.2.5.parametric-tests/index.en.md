---
title: Parametric Hypothesis Testing
description: Null and alternative hypotheses, rejection regions and test functions, the two types of error, power and p-values; tests for normal, Bernoulli and Poisson parameters; likelihood ratio tests and Wilks' theorem; the Neyman–Pearson lemma and uniformly most powerful tests; the duality with confidence intervals; tests in linear regression and two-way ANOVA.
---

Parameter estimation and hypothesis testing are the two main tasks of statistical inference. In a parametric problem the form of the distribution is known, $\{f(x;\theta)\colon\theta\in\Theta\}$, and we ask whether the parameter of interest lies in a specified subset of the parameter space; when the form of the distribution is unknown, the methods must not depend on it, which is the subject of nonparametric testing in [3.2.6](/3.2.6). This chapter first sets up the vocabulary (hypotheses, rejection regions, the two types of error, power and $p$-values) and the classical tests for normal, Bernoulli and Poisson populations, whose test statistics rest on the sampling distributions of [3.2.2](/3.2.2). It then introduces two general principles for constructing tests: the likelihood ratio test, which builds on **maximum likelihood estimation** ([3.2.3](/3.2.3)), and the Neyman–Pearson theory of most powerful tests. Finally it shows that tests and **confidence intervals** ([3.2.4](/3.2.4)) are two descriptions of the same object, and applies the theory to linear regression and the analysis of variance, which are developed further in [3.3](/3.3).

Historically, K. Pearson introduced the $\chi^2$ test for categorical data in 1900; in the 1920s R. A. Fisher developed significance tests based on the $t$ and $F$ distributions; from 1928 J. Neyman and E. S. Pearson spent ten years on criteria for comparing tests, turning testing into a mathematical optimization problem (the NP theory); A. Wald embedded it in statistical decision theory around 1950, while the Bayesian approach ([3.2.7](/3.2.7)) developed alongside as an alternative to the frequentist one.

## 5.1. General Concepts

### 5.1.1. Hypotheses

The following examples show the kind of question a test answers.

**Example 5.1.1** The long-run scrap rate of a product made in a factory is $p$. A store will purchase the products only if the scrap rate is lower than $0.01$. In a random sample of $100$ products, $3$ are scrap. Should the store purchase? There are two possibilities,

$$
H_0\colon 0<p\le0.01 \quad\text{vs.}\quad H_1\colon 0.01<p<1,
$$
and the store has to decide which of them is better supported by the data.

**Example 5.1.2** A government agency wants to know whether the unemployment rate $\theta$ of a city is acceptable, that is, lower than $\theta_0=6.25\%$, by sampling $n$ members of the labor force. It tests $H_0\colon\theta>\theta_0$ against $H_1\colon\theta\le\theta_0$: the agency declares the rate acceptable only if the data give strong evidence for it.

**Example 5.1.3** A city health department wants to know whether the mean bacteria count per unit volume of water at a lake beach is within the safety level $200$. With the Poisson model $\mathrm{Poi}(\theta)$ and $n$ independent water samples, it tests $H_0\colon\theta>200$ against $H_1\colon\theta\le200$.

**Example 5.1.4** The mean $\theta$ of a random variable $X\sim\mathcal{N}(\theta,\sigma^2)$ ($\sigma$ known) is the dosage of a drug. The drug is both safe and effective only if $\theta_1<\theta<\theta_2$ for two specified values, so we test $H_0\colon\theta\le\theta_1$ or $\theta\ge\theta_2$ against $H_1\colon\theta_1<\theta<\theta_2$.

**Example 5.1.5** It is claimed that a new treatment prolongs the lives of terminal cancer patients more than the standard one. Let the survival times under the standard and the new treatment be $X\sim\mathcal{N}(\theta_1,\sigma_1^2)$ and $Y\sim\mathcal{N}(\theta_2,\sigma_2^2)$, where $\theta_1$ is known from long experience. The hypotheses are $H_0\colon\theta_2=\theta_1$ and $H_1\colon\theta_2>\theta_1$. One could also take $H_0\colon\theta_2\le\theta_1$; writing $\theta_2=\theta_1$ expresses the assumption that the new treatment is not inferior. "No difference between the treatments" is the origin of the word *null*.

**Definition 5.1.1 (Null and Alternative Hypotheses)** Let $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ be a family of distributions and $\boldsymbol{X}=(X_1,\dots,X_n)$ a random sample from it. Let $\Theta_0$ be a nonempty proper subset of $\Theta$ and $\Theta_1=\Theta\setminus\Theta_0$.

- The **null hypothesis** is $H_0\colon\theta\in\Theta_0$, meaning that $X_i\sim f(x;\theta_0)$ for some $\theta_0\in\Theta_0$; the **alternative hypothesis** is $H_1\colon\theta\in\Theta_1$. We write the problem as $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$.
- $H_0$ (or $H_1$) is a **simple hypothesis** if $\Theta_0$ (or $\Theta_1$) contains a single point, and a **composite hypothesis** otherwise.
- The procedure of deciding, on the basis of the observed values $x_1,\dots,x_n$, whether to reject $H_0$ is called **hypothesis testing** ($H_0$ is tested against $H_1$).

When $\Theta\subseteq\mathbb{R}$, the common forms are

| | $H_0$ | $H_1$ |
|---|---|---|
| simple vs. simple | $\theta=\theta_0$ | $\theta=\theta_1$ |
| two-sided | $\theta=\theta_0$ | $\theta\ne\theta_0$ |
| one-sided | $\theta=\theta_0$ or $\theta\le\theta_0$ | $\theta>\theta_0$ |
| one-sided | $\theta=\theta_0$ or $\theta\ge\theta_0$ | $\theta<\theta_0$ |
| interval | $\theta\le\theta_1$ or $\theta\ge\theta_2$ | $\theta_1<\theta<\theta_2$ |

**Remark 5.1.1** The roles of $H_0$ and $H_1$ cannot be exchanged. As Section 5.1.3 will show, a test controls the probability of wrongly rejecting $H_0$ but not of wrongly accepting it, so $H_0$ is the statement that we are not willing to give up without strong evidence (the status quo, "no effect"), and $H_1$ is the claim that the data must establish.

### 5.1.2. Rejection Regions and Test Functions

**Example 5.1.6** Let $X_1,\dots,X_{10}$ be a sample from $\mathcal{N}(\theta,1)$ and test $H_0\colon\theta=1$ vs. $H_1\colon\theta\ne1$. The sample mean $\bar X$ estimates $\theta$, so it is natural to reject $H_0$ when $\lvert\bar X-1\rvert>A$ and to accept it when $\lvert\bar X-1\rvert\le A$, for instance with $A=1.96/\sqrt{10}=0.62$ (Section 5.2 explains this choice). For the observations $2.2, 3.7, 1.6, 1.2, 2.5, 1.3, 2.7, 2.5, 2.2, 2.0$ we get $\bar x=2.19$ and $\lvert\bar x-1\rvert=1.19>0.62$, so $H_0$ is rejected.

**Definition 5.1.2 (Rejection Region)** A statistic $T(\boldsymbol{X})$ on which the decision is based is called a **test statistic**. A subset $D$ of the sample space $\mathcal{X}$ such that $H_0$ is rejected when $\boldsymbol{x}\in D$ is called a **rejection region** (or critical region), and its complement $D^{\mathsf c}=\mathcal{X}\setminus D$ is the **acceptance region**. When $D$ has the form $\{T(\boldsymbol{X})>A\}$ or $\{\lvert T(\boldsymbol{X})\rvert>A\}$, the boundary value $A$ is the **critical value**.

In Example 5.1.6 the test statistic is $\bar X$, the critical value is $A$, and $D=\{\boldsymbol{X}\colon\lvert\bar X-1\rvert>A\}$. A rejection region must be computable from the data, so it may not involve unknown parameters; to determine $A$ we need the sampling distribution of the test statistic under $H_0$.

**Definition 5.1.3 (Test Function)** A function $\varphi(\boldsymbol{x})$ defined on the sample space $\mathcal{X}$ with values in $[0,1]$ is called a **test function**; $\varphi(\boldsymbol{x})$ is the probability of rejecting $H_0$ when $\boldsymbol{x}$ is observed. If $\varphi$ takes only the values $0$ and $1$, the test is a **nonrandomized test**, and it is equivalent to the rejection region $D=\{\boldsymbol{x}\colon\varphi(\boldsymbol{x})=1\}$; if $\varphi$ takes values in $(0,1)$ on a set of positive probability, it is a **randomized test**.

The test of Example 5.1.6 is $\varphi(\boldsymbol{X})=1$ if $\lvert\bar X-1\rvert>A$ and $0$ otherwise. Randomization is needed for discrete data. In Example 5.1.1, let $X_i=1$ if the $i$-th product is scrap and $X_i=0$ otherwise, and $T(\boldsymbol{X})=\sum_{i=1}^{100}X_i$. We accept $H_0$ if $T<c$ and reject it if $T>c$; at $T=c$ we compromise and reject $H_0$ with probability $r\in(0,1)$, decided by an auxiliary random experiment (like drawing lots between candidates with equal scores for a scholarship):

$$
\varphi(\boldsymbol{X})=\begin{cases}1, & T(\boldsymbol{X})>c,\\ r, & T(\boldsymbol{X})=c,\\ 0, & T(\boldsymbol{X})<c.\end{cases}
$$
Section 5.2.3 shows how $c$ and $r$ are chosen.

**Remark 5.1.2** A criminal trial is a good analogy. The jury begins with the presumption of innocence, $H_0$: the defendant is innocent, against $H_1$: the defendant is guilty. It keeps this belief unless the evidence is strong enough, beyond a threshold, in which case it rejects $H_0$ and convicts; otherwise it acquits. An acquittal is not a proof of innocence and a conviction is not a proof of guilt: the verdict is a decision that may be wrong.

### 5.1.3. Type I and Type II Errors and the Power Function

Since the sample is random, either decision may be wrong.

**Definition 5.1.4 (Type I and Type II Errors)** A **type I error** is the rejection of $H_0$ when $H_0$ is true (the jury convicts an innocent defendant); a **type II error** is the acceptance of $H_0$ when $H_0$ is false (the jury acquits a guilty one). Their probabilities are

$$
\begin{aligned}
\alpha(\theta)&=\mathbb{P}_\theta(\boldsymbol{X}\in D),&&\theta\in\Theta_0,\\
\beta(\theta)&=\mathbb{P}_\theta(\boldsymbol{X}\in D^{\mathsf c}),&&\theta\in\Theta_1.
\end{aligned}
$$

For instance, in Example 5.1.1 with the test "reject if $T>3$", if the true scrap rate is $p=0.005$ but we observe $T=5$, we commit a type I error. Once the test is fixed, both error probabilities are determined, and for each $\theta$ only one of them can occur.

**Definition 5.1.5 (Size and Level of Significance)** The maximal probability of a type I error, $\sup_{\theta\in\Theta_0}\alpha(\theta)$, is called the **size** of the test. A test is said to have **level of significance** $\alpha$ (or to be a level-$\alpha$ test) if its size does not exceed $\alpha$.

For most tests in this chapter the size equals the prescribed $\alpha$, and the two words are used interchangeably. The trivial test $D=\varnothing$ (always accept $H_0$) has size $0$ but $\beta(\theta)=1$ for every $\theta\in\Theta_1$; for a fixed sample size $n$ the two error probabilities cannot be made small simultaneously.

**Definition 5.1.6 (Power Function)** The **power function** of a test $\varphi$ is

$$
\pi_\varphi(\theta)=\mathbb{P}_\theta(\text{$\varphi$ rejects $H_0$})=\mathbb{E}_\theta[\varphi(\boldsymbol{X})],\qquad\theta\in\Theta;\tag{5.1}
$$
its values on $\Theta_1$ are the power of the test.

For a nonrandomized test $\pi_\varphi(\theta)=\mathbb{P}_\theta(\boldsymbol{X}\in D)$; for the randomized test above, $\pi_\varphi(\theta)=\mathbb{P}_\theta(T>c)+r\,\mathbb{P}_\theta(T=c)$. The two error probabilities are read off the power function:

$$
\alpha(\theta)=\pi_\varphi(\theta)\ (\theta\in\Theta_0),\qquad \beta(\theta)=1-\pi_\varphi(\theta)\ (\theta\in\Theta_1).
$$
A good power function is small (at most $\alpha$) on $\Theta_0$ and rises quickly towards $1$ on $\Theta_1$.

![Type I and type II error probabilities of the one-sided test that rejects H₀: μ ≤ μ₀ when Z = √n (X̄ − μ₀)/σ > z_α. Moving the critical value to the right decreases α but increases β](./plots/type-errors.py)

Since the two errors cannot be controlled at once, J. Neyman and E. S. Pearson proposed the *Neyman–Pearson principle*: first control the probability of a type I error at a prescribed level of significance $\alpha$, and then, among all tests of level $\alpha$, choose one whose probability of a type II error is as small as possible (whose power is as large as possible).

**Remark 5.1.3** Under this principle, rejecting $H_0$ risks a type I error, whose probability is small (say $0.05$); accepting $H_0$ risks a type II error, whose probability may be large (say $0.9$). The two conclusions are therefore not equally reliable. When the data fall in the acceptance region we should say that the data do not provide enough evidence to reject $H_0$, not that $H_0$ has been shown to be true. This is why the null hypothesis should be the statement whose false rejection has the most serious consequences, a statement we are confident about and do not give up lightly. In Example 5.1.2 the agency takes "the rate is too high" as $H_0$, so that it declares the rate acceptable only on strong evidence.

**Remark 5.1.4** The smaller $\alpha$, the smaller the probability of a type I error, the larger that of a type II error, the harder it is to reject $H_0$, and the more reliable a rejection is. Choosing $\alpha$ is not a mathematical problem: it may be agreed upon between the parties (the store and the factory in Example 5.1.1), taken very small when a type I error has serious consequences (approving an ineffective treatment in Example 5.1.5), or based on prior information. In practice, rejecting $H_0$ often means overthrowing an old theory or replacing an old method, which requires significant evidence from the data. The conventional values are $\alpha=0.05$ and $0.01$.

### 5.1.4. p-Values

A test reports only "reject" or "accept", not how strong the evidence is.

**Example 5.1.7** Let $X_1,\dots,X_{16}$ be a sample from $\mathcal{N}(\mu,1)$ and test $H_0\colon\mu=0$ vs. $H_1\colon\mu\ne0$ at $\alpha=0.05$ with $D=\{\lvert\sqrt{16}\,\bar X\rvert>1.96\}=\{\lvert\bar X\rvert>0.49\}$. Both $\bar x=0.48$ and $\bar x=0.12$ lead to acceptance, but the first is nearly in the rejection region and the second is not. Under $H_0$, $U=\sqrt{16}\,\bar X\sim\mathcal{N}(0,1)$, and if we use the observed value as the critical value, the probability of a result at least as extreme is

$$
p=\mathbb{P}_{H_0}(\lvert\bar X\rvert\ge\lvert\bar x\rvert)=\mathbb{P}(\lvert U\rvert\ge4\lvert\bar x\rvert),
$$
which equals $0.055$ for $\bar x=0.48$ and $0.631$ for $\bar x=0.12$.

**Definition 5.1.7 (p-Value)** Let $T(\boldsymbol{X})$ be the test statistic and $t(\boldsymbol{x})$ its observed value. The **p-value** is the probability, computed under the null hypothesis, of obtaining a value of the test statistic at least as extreme as the observed one; that is, the probability of the rejection region obtained when $t(\boldsymbol{x})$ is used as the critical value:

| Problem | Rejection region | $p$-value |
|---|---|---|
| $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta\ne\theta_0$ | $\lvert T\rvert>c$ | $\mathbb{P}_{\theta_0}(\lvert T(\boldsymbol{X})\rvert\ge\lvert t(\boldsymbol{x})\rvert)$ |
| $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$ | $T>c$ | $\mathbb{P}_{\theta_0}(T(\boldsymbol{X})\ge t(\boldsymbol{x}))$ |
| $H_0\colon\theta\ge\theta_0$ vs. $H_1\colon\theta<\theta_0$ | $T<c$ | $\mathbb{P}_{\theta_0}(T(\boldsymbol{X})\le t(\boldsymbol{x}))$ |

For a composite $H_0$ the probability is computed at the boundary point $\theta_0$, where it is largest for the tests of this chapter. For continuous statistics it does not matter whether the inequalities are strict.

![p-values of a two-sided and a one-sided test based on a statistic that is standard normal under H₀, for the observed value t(x) = 2.2 (shaded areas); the dotted lines are the critical values for α = 0.05](./plots/p-values.py)

**Proposition 5.1.1** Suppose that $T(\boldsymbol{X})$ has a continuous distribution under $\theta_0$. Then the size-$\alpha$ test rejects $H_0$ if and only if $p<\alpha$; that is, the $p$-value is the smallest level of significance at which the observed data lead to rejection. In practice the decision rule is: reject $H_0$ if $p\le\alpha$.

**Proof** Consider the right-sided problem; the other cases are the same. The size-$\alpha$ test rejects when $t(\boldsymbol{x})>c_\alpha$, where $G(c_\alpha)=\alpha$ for the continuous, nonincreasing function $G(c)=\mathbb{P}_{\theta_0}(T\ge c)$, and $p=G(t(\boldsymbol{x}))$. If $t(\boldsymbol{x})>c_\alpha$, then $p\le\alpha$, with equality only if $G$ is constant on $[c_\alpha,t(\boldsymbol{x})]$, an event of probability zero; conversely, $p<\alpha=G(c_\alpha)$ forces $t(\boldsymbol{x})>c_\alpha$. $\square$

**Remark 5.1.5** The $p$-value measures the strength of evidence against $H_0$: the smaller it is, the stronger the rejection ($p=0.01$ versus $p=10^{-8}$). It is usually reported together with a rejection, and a very small $p$-value is described as the result being highly statistically significant. It is computed under the assumed model, so it is only as reliable as the model. It is not the probability that $H_0$ is true, and statistical significance is not practical significance: with a large sample, a difference too small to matter can have a tiny $p$-value.

### 5.1.5. General Steps

1. State the null hypothesis $H_0$ and the alternative $H_1$.
2. Choose a test statistic $T(\boldsymbol{X})$ and the form of the rejection region, for example $D=\{\lvert T(\boldsymbol{X})\rvert>A\}$ with $A$ to be determined.
3. Choose the level of significance $\alpha$ (for example $0.05$ or $0.01$) and determine the critical value $A$ from the sampling distribution of $T(\boldsymbol{X})$ under $H_0$.
4. Compute the observed value of $T$ and reject or accept $H_0$; report the $p$-value as well.

**Example 5.1.8** Are male students of a university taller than $174\,\mathrm{cm}$ on average? A census is costly and unnecessary; we sample $15$ male students instead:

$$
174,\ 171,\ 175,\ 174,\ 176,\ 177,\ 175,\ 171,\ 178,\ 177,\ 175,\ 179,\ 176,\ 174,\ 177.
$$
Assume the heights are $\mathcal{N}(\mu,\sigma^2)$ and test $H_0\colon\mu=174$ vs. $H_1\colon\mu>174$ at $\alpha=0.05$. Here $\bar x=175.27$, $s^2=5.21$, $s=2.28$. The test statistic and rejection region are

$$
T(\boldsymbol{X})=\frac{\sqrt{n}(\bar X-174)}{S}\overset{H_0}{\sim}t_{n-1},\qquad D=\{T(\boldsymbol{X})>A\},
$$
and $\mathbb{P}_{H_0}(T>A)=0.05$ gives $A=t_{14,0.05}=1.761$. The observed value is $t(\boldsymbol{x})=\sqrt{15}(175.27-174)/2.28=2.15>1.761$, so $H_0$ is rejected; the $p$-value is $\mathbb{P}(t_{14}\ge2.15)=0.025<0.05$. The data support the claim that the mean height exceeds $174\,\mathrm{cm}$.

## 5.2. Tests for Parameters of Various Populations

This section derives the standard tests for one and two normal populations, for Bernoulli and Poisson populations, and the large-sample tests based on the **central limit theorem**. Throughout, $\Phi$ is the distribution function of $\mathcal{N}(0,1)$, and $z_\alpha$, $t_{n,\alpha}$, $\chi^2_{n,\alpha}$, $F_{m,n,\alpha}$ are the upper $\alpha$ quantiles of $\mathcal{N}(0,1)$, $t_n$, $\chi^2_n$ and $F_{m,n}$.

### 5.2.1. Tests for the Mean of a Normal Population

Let $\boldsymbol{X}=(X_1,\dots,X_n)$ be a sample from $\mathcal{N}(\mu,\sigma^2)$ and consider, for a given $\mu_0$ and level $\alpha$,

$$
\text{(1) } H_0\colon\mu=\mu_0 \text{ vs. } H_1\colon\mu\ne\mu_0;\quad
\text{(2) } H_0\colon\mu\le\mu_0 \text{ vs. } H_1\colon\mu>\mu_0;\quad
\text{(3) } H_0\colon\mu\ge\mu_0 \text{ vs. } H_1\colon\mu<\mu_0.
$$

**Definition 5.2.1 (One-Sided and Two-Sided Tests)** A problem such as (1), whose alternative lies on both sides of the null value, is a **two-sided test**; problems such as (2) and (3) are **one-sided tests**.

Suppose first that $\sigma^2$ is known and consider problem (1). $\bar X$ estimates $\mu$, and $H_0$ is doubtful when $\lvert\bar X-\mu_0\rvert$ is large, so we take $D=\{\lvert\bar X-\mu_0\rvert>A\}$. Under $H_0$, $\bar X\sim\mathcal{N}(\mu_0,\sigma^2/n)$, so

$$
Z=\frac{\sqrt{n}(\bar X-\mu_0)}{\sigma}\overset{H_0}{\sim}\mathcal{N}(0,1).
$$
With the test statistic $Z$ and rejection region $\{\lvert Z\rvert>c\}$, the condition $\mathbb{P}_{H_0}(\lvert Z\rvert>c)=\alpha$ gives $c=z_{\alpha/2}$:

$$
D_1=\left\{\boldsymbol{X}\colon\left\lvert\frac{\sqrt{n}(\bar X-\mu_0)}{\sigma}\right\rvert>z_{\alpha/2}\right\}.
$$
Writing $\bar X-\mu_0=(\bar X-\mu)+(\mu-\mu_0)$, where $\sqrt{n}(\bar X-\mu)/\sigma\sim\mathcal{N}(0,1)$ under $\mathbb{P}_\mu$, gives the power function

$$
\pi_1(\mu)=1-\Phi\left(z_{\alpha/2}+\frac{\sqrt{n}(\mu_0-\mu)}{\sigma}\right)+\Phi\left(-z_{\alpha/2}+\frac{\sqrt{n}(\mu_0-\mu)}{\sigma}\right).\tag{5.2}
$$

**Proposition 5.2.1** The power function (5.2) satisfies $\pi_1(\mu_0)=\alpha$ and $\pi_1(\mu)=\pi_1(2\mu_0-\mu)$, and it is strictly increasing for $\mu\ge\mu_0$. For each $\mu\ne\mu_0$, $\pi_1(\mu)$ increases with $n$ and decreases with $\sigma$, and $\pi_1(\mu)\to1$ as $n\to\infty$.

**Proof** With $d=\sqrt{n}(\mu-\mu_0)/\sigma$, (5.2) reads $g(d)=1-\Phi(z_{\alpha/2}-d)+\Phi(-z_{\alpha/2}-d)$, which is even in $d$ because $\Phi(-x)=1-\Phi(x)$; this is the symmetry. Its derivative $g'(d)=\phi(z_{\alpha/2}-d)-\phi(z_{\alpha/2}+d)$, where $\phi$ is the standard normal density, is positive for $d>0$ since $\lvert z_{\alpha/2}-d\rvert<z_{\alpha/2}+d$. Hence $\pi_1$ grows with $\lvert d\rvert$, which increases with $n$ and $\lvert\mu-\mu_0\rvert$ and decreases with $\sigma$; and $g(d)\to1$ as $\lvert d\rvert\to\infty$. $\square$

For problem (2), still with $\sigma^2$ known, we again use $Z$ and reject when $Z>c$. The condition $\mathbb{P}_{\mu_0}(Z>c)=\alpha$ gives $c=z_\alpha$, and the region

$$
D_2=\left\{\boldsymbol{X}\colon\frac{\sqrt{n}(\bar X-\mu_0)}{\sigma}>z_\alpha\right\}
$$
has size $\alpha$ for the simple null $H_0^*\colon\mu=\mu_0$. For the composite null $\mu\le\mu_0$ we must also check that the probability of a type I error does not exceed $\alpha$ when $\mu<\mu_0$.

**Proposition 5.2.2** The power function of $D_2$ is $\pi_2(\mu)=1-\Phi\big(z_\alpha+\sqrt{n}(\mu_0-\mu)/\sigma\big)$. It is strictly increasing in $\mu$, so $\pi_2(\mu)\le\pi_2(\mu_0)=\alpha$ for all $\mu\le\mu_0$, and $D_2$ is a level-$\alpha$ rejection region for problem (2). Similarly, $D_3=\{\sqrt{n}(\bar X-\mu_0)/\sigma<-z_\alpha\}$ is a level-$\alpha$ rejection region for problem (3).

**Proof** $\pi_2(\mu)=\mathbb{P}_\mu\big(\sqrt{n}(\bar X-\mu)/\sigma>z_\alpha+\sqrt{n}(\mu_0-\mu)/\sigma\big)$, and $\sqrt{n}(\bar X-\mu)/\sigma\sim\mathcal{N}(0,1)$ under $\mathbb{P}_\mu$. The argument of $\Phi$ decreases in $\mu$. Problem (3) is symmetric. $\square$

A test based on a statistic that is $\mathcal{N}(0,1)$ under $H_0$ is called a *Z-test* (in Chinese textbooks, the $U$ test); the tests above are one-sample Z-tests.

![Power functions of Z-tests for a normal mean with μ₀ = 1, σ² = 4 and α = 0.05. Left: the two-sided test for three sample sizes; the curves are symmetric about μ₀ and steeper for larger n. Right: for testing μ = μ₀ against μ ≠ μ₀, the one-sided region D₂ has power below α on the left of μ₀](./plots/power-functions.py)

When $\sigma^2$ is unknown, we estimate $\sigma^2$ by the sample variance $S^2=\sum_{i=1}^n(X_i-\bar X)^2/(n-1)$ and use

$$
T=\frac{\sqrt{n}(\bar X-\mu_0)}{S}\overset{H_0}{\sim}t_{n-1}.
$$
By the same arguments the rejection regions for problems (1), (2), (3) are

$$
D_1'=\{\lvert T\rvert>t_{n-1,\alpha/2}\},\qquad D_2'=\{T>t_{n-1,\alpha}\},\qquad D_3'=\{T<-t_{n-1,\alpha}\}.
$$
Tests based on the $t$ statistic (W. S. Gosset, 1908) are called *t-tests*; this one is the one-sample $t$-test. Its power functions, such as $\pi_1'(\mu)=\mathbb{P}_\mu(\lvert T\rvert>t_{n-1,\alpha/2})$, have no simple closed form: under $\mathbb{P}_\mu$, $T$ has the noncentral $t$ distribution with $n-1$ degrees of freedom and noncentrality $\delta=\sqrt{n}(\mu-\mu_0)/\sigma$, so the power depends on the unknown $\sigma$. It can be computed numerically or approximated by Monte Carlo simulation.

| | $H_0$ | $H_1$ | Test statistic | Rejection region |
|---|---|---|---|---|
| $\sigma^2$ known | $\mu=\mu_0$ | $\mu\ne\mu_0$ | $Z=\sqrt{n}(\bar X-\mu_0)/\sigma$ | $\lvert Z\rvert>z_{\alpha/2}$ |
| | $\mu\le\mu_0$ | $\mu>\mu_0$ | $Z\overset{\mu=\mu_0}{\sim}\mathcal{N}(0,1)$ | $Z>z_\alpha$ |
| | $\mu\ge\mu_0$ | $\mu<\mu_0$ | | $Z<-z_\alpha$ |
| $\sigma^2$ unknown | $\mu=\mu_0$ | $\mu\ne\mu_0$ | $T=\sqrt{n}(\bar X-\mu_0)/S$ | $\lvert T\rvert>t_{n-1,\alpha/2}$ |
| | $\mu\le\mu_0$ | $\mu>\mu_0$ | $T\overset{\mu=\mu_0}{\sim}t_{n-1}$ | $T>t_{n-1,\alpha}$ |
| | $\mu\ge\mu_0$ | $\mu<\mu_0$ | | $T<-t_{n-1,\alpha}$ |

**Remark 5.2.1** When $\sigma^2$ is known, both $D_1$ and the $t$-test region $D_1'$ have size $\alpha$ for problem (1). The Z-test is slightly more powerful, because it uses the known $\sigma$ instead of the noisy estimate $S$ (for $\mu_0=1$, $\sigma^2=4$, $n=20$ the two power curves almost coincide, the $t$-test lying a little below). The difference vanishes as $n$ grows.

**Remark 5.2.2** One-sided or two-sided region? For problem (1), the one-sided region $D_2$ also has size $\alpha$ at $\mu_0$, but its power is below $\alpha$ for $\mu<\mu_0$ and tends to $0$: it cannot detect deviations to the left (right panel of the figure). For problem (2), and also for $H_0\colon\mu=\mu_0$ vs. $H_1\colon\mu>\mu_0$, both $D$ and $D_2$ have size $\alpha$, but $D_2$ has larger power at every $\mu>\mu_0$, so the one-sided region is better. The shape of the rejection region should follow the alternative. Section 5.4 makes "better" precise.

**Example 5.2.1** A machine fills cans with a nominal weight of $500\,\mathrm{g}$. Ten cans weigh (in grams) $495, 510, 505, 498, 503, 492, 502, 512, 497, 506$. Assume the weight is $\mathcal{N}(\mu,\sigma^2)$ with $\sigma=6.5$. Is the machine working properly at $\alpha=0.05$? We test $H_0\colon\mu=500$ vs. $H_1\colon\mu\ne500$ with $D_1$, where $z_{0.025}=1.96$. Since $\bar x=502$,

$$
\lvert z\rvert=\left\lvert\frac{\sqrt{10}(502-500)}{6.5}\right\rvert=0.973<1.96,
$$
there is not enough evidence to reject $H_0$; the $p$-value is $\mathbb{P}(\lvert Z\rvert\ge0.973)=0.331$. By (5.2), the power at $\mu=505$ is

$$
\pi(505)=1-\Phi\left(1.96+\frac{\sqrt{10}(500-505)}{6.5}\right)+\Phi\left(-1.96+\frac{\sqrt{10}(500-505)}{6.5}\right)=0.682,
$$
and $\pi(510)=0.998$: a shift of $10\,\mathrm{g}$ would almost surely be detected, one of $5\,\mathrm{g}$ only with probability about $2/3$.

**Example 5.2.2** The breaking strength of floor tiles from a factory is $\mathcal{N}(\mu,\sigma^2)$. Six tiles give (in $\mathrm{kg/cm^2}$) $32.56, 29.66, 31.64, 30.00, 31.87, 31.03$. Can the mean strength be considered at least $32.50$ ($\alpha=0.05$)? We test $H_0\colon\mu\ge32.50$ vs. $H_1\colon\mu<32.50$ with the one-sample $t$-test, $D=\{T<-t_{5,0.05}\}$, $t_{5,0.05}=2.015$. Here $\bar x=31.13$ and $s=1.123$, so

$$
t=\frac{\sqrt{6}(31.13-32.50)}{1.123}=-2.99<-2.015,
$$
and $H_0$ is rejected: the mean strength is below $32.50$. The $p$-value is $\mathbb{P}(t_5\le-2.99)=0.015$. The power at $\mu=31$ depends on $\sigma$, because

$$
\frac{\sqrt{n}(\bar X-\mu_0)}{S}=\frac{\sqrt{n}(\bar X-31)}{S}+\frac{\sqrt{n}(31-\mu_0)}{S},
$$
where the first term has a distribution free of $\sigma$ under $\mu=31$ but the second does not. If $\sigma=1.123$, the noncentral $t$ distribution gives $\pi(31)=0.875$.

### 5.2.2. Tests for the Variance of a Normal Population

For a sample from $\mathcal{N}(\mu,\sigma^2)$ consider

$$
\text{(4) } H_0\colon\sigma^2=\sigma_0^2 \text{ vs. } H_1\colon\sigma^2\ne\sigma_0^2;\quad
\text{(5) } H_0\colon\sigma^2\le\sigma_0^2 \text{ vs. } H_1\colon\sigma^2>\sigma_0^2;\quad
\text{(6) } H_0\colon\sigma^2\ge\sigma_0^2 \text{ vs. } H_1\colon\sigma^2<\sigma_0^2.
$$

Suppose first that $\mu$ is unknown. Then $S^2$ estimates $\sigma^2$, and $H_0$ in (4) is doubtful when $S^2/\sigma_0^2$ is too small or too large. Under $\sigma^2=\sigma_0^2$,

$$
\chi^2=\frac{(n-1)S^2}{\sigma_0^2}\sim\chi^2_{n-1},
$$
so with the rejection region $\{\chi^2<c_1\text{ or }\chi^2>c_2\}$ we may take the equal-tailed choice $c_1=\chi^2_{n-1,1-\alpha/2}$, $c_2=\chi^2_{n-1,\alpha/2}$. For (5) and (6) the regions are $\{\chi^2>\chi^2_{n-1,\alpha}\}$ and $\{\chi^2<\chi^2_{n-1,1-\alpha}\}$; their power functions are monotone in $\sigma^2$, as in Proposition 5.2.2.

When $\mu$ is known, $S_\mu^2=\sum_{i=1}^n(X_i-\mu)^2/n$ estimates $\sigma^2$, and

$$
\chi^2_\mu=\frac{nS_\mu^2}{\sigma_0^2}=\sum_{i=1}^n\left(\frac{X_i-\mu}{\sigma_0}\right)^2\overset{\sigma^2=\sigma_0^2}{\sim}\chi^2_n;
$$
the rejection regions are the same with $n$ degrees of freedom instead of $n-1$.

| | $H_0$ | $H_1$ | Test statistic | Rejection region |
|---|---|---|---|---|
| $\mu$ known | $\sigma^2=\sigma_0^2$ | $\sigma^2\ne\sigma_0^2$ | $\chi^2_\mu=nS_\mu^2/\sigma_0^2$ | $\chi^2_\mu<\chi^2_{n,1-\alpha/2}$ or $\chi^2_\mu>\chi^2_{n,\alpha/2}$ |
| | $\sigma^2\le\sigma_0^2$ | $\sigma^2>\sigma_0^2$ | $\chi^2_\mu\overset{\sigma^2=\sigma_0^2}{\sim}\chi^2_n$ | $\chi^2_\mu>\chi^2_{n,\alpha}$ |
| | $\sigma^2\ge\sigma_0^2$ | $\sigma^2<\sigma_0^2$ | | $\chi^2_\mu<\chi^2_{n,1-\alpha}$ |
| $\mu$ unknown | $\sigma^2=\sigma_0^2$ | $\sigma^2\ne\sigma_0^2$ | $\chi^2=(n-1)S^2/\sigma_0^2$ | $\chi^2<\chi^2_{n-1,1-\alpha/2}$ or $\chi^2>\chi^2_{n-1,\alpha/2}$ |
| | $\sigma^2\le\sigma_0^2$ | $\sigma^2>\sigma_0^2$ | $\chi^2\overset{\sigma^2=\sigma_0^2}{\sim}\chi^2_{n-1}$ | $\chi^2>\chi^2_{n-1,\alpha}$ |
| | $\sigma^2\ge\sigma_0^2$ | $\sigma^2<\sigma_0^2$ | | $\chi^2<\chi^2_{n-1,1-\alpha}$ |

Tests based on the $\chi^2$ distribution are called $\chi^2$ tests.

**Remark 5.2.3** When $\mu$ is known, the test based on $S^2$ and $\chi^2_{n-1}$ is still a valid level-$\alpha$ test, but it wastes the information that $\mu$ is known: estimating $\mu$ by $\bar X$ costs one degree of freedom, and the test based on $S_\mu^2$ is more powerful.

### 5.2.3. Tests for a Bernoulli Parameter

Let $\boldsymbol{X}$ be a sample from $\mathrm{Ber}(\theta)$ and $T(\boldsymbol{X})=\sum_{i=1}^nX_i\sim\mathrm{Bin}(n,\theta)$. Consider first $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta>\theta_0$. Since $\bar X=T/n$ estimates $\theta$, we reject for large $T$; under $H_0$, $T\sim\mathrm{Bin}(n,\theta_0)$. Because $T$ is discrete, there is in general no $c$ with $\mathbb{P}_{\theta_0}(T>c)=\alpha$ exactly, so we use the randomized test

$$
\varphi(\boldsymbol{X})=\begin{cases}1, & T>c,\\ r, & T=c,\\ 0, & T<c,\end{cases}\qquad
\mathbb{E}_{\theta_0}\varphi(\boldsymbol{X})=\mathbb{P}_{\theta_0}(T>c)+r\,\mathbb{P}_{\theta_0}(T=c)=\alpha,\tag{5.3}
$$
with $0\le r\le1$: $c$ is the integer with $\mathbb{P}_{\theta_0}(T>c)\le\alpha<\mathbb{P}_{\theta_0}(T\ge c)$, and then $r=\big(\alpha-\mathbb{P}_{\theta_0}(T>c)\big)/\mathbb{P}_{\theta_0}(T=c)$. The power function $\pi(\theta)=\mathbb{P}_\theta(T>c)+r\,\mathbb{P}_\theta(T=c)$ is increasing in $\theta$ (the binomial family is stochastically increasing in $\theta$), so $\pi(\theta)\le\pi(\theta_0)=\alpha$ for $\theta\le\theta_0$, and (5.3) is also a level-$\alpha$ test for $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$.

**Example 5.2.3** In Example 5.1.1, $n=100$, $\theta_0=0.01$, $\alpha=0.05$, and $T\sim\mathrm{Bin}(100,0.01)$ under $H_0$. Then $\mathbb{P}_{\theta_0}(T>3)=0.0184\le0.05<\mathbb{P}_{\theta_0}(T\ge3)$, so

$$
c=3,\qquad r=\frac{0.05-0.01837}{0.06100}=0.518.
$$
The observed value $T=3$ falls exactly on the boundary: the test rejects $H_0$ (refuses the purchase) with probability $0.518$.

For $H_0\colon\theta\ge\theta_0$ vs. $H_1\colon\theta<\theta_0$ the test rejects for small $T$: $\varphi=1$ if $T<c$, $r$ if $T=c$, $0$ if $T>c$, with $\mathbb{P}_{\theta_0}(T<c)+r\,\mathbb{P}_{\theta_0}(T=c)=\alpha$. For the two-sided problem,

$$
\varphi(\boldsymbol{X})=\begin{cases}1, & T<c_1\text{ or }T>c_2,\\ r_i, & T=c_i\ (i=1,2),\\ 0, & c_1<T<c_2,\end{cases}
$$
where $\mathbb{P}_{\theta_0}(T<c_1)+r_1\mathbb{P}_{\theta_0}(T=c_1)=\alpha/2$ and $\mathbb{P}_{\theta_0}(T>c_2)+r_2\mathbb{P}_{\theta_0}(T=c_2)=\alpha/2$.

**Example 5.2.4** In Example 5.1.2, suppose that $20$ of $n=500$ people are unemployed, and test $H_0\colon\theta\ge0.0625$ vs. $H_1\colon\theta<0.0625$ at $\alpha=0.05$. The left-sided randomized test has $c=23$, $r=0.099$; since $T=20<23$, $H_0$ is rejected: the unemployment rate is significantly below $6.25\%$.

**Remark 5.2.4** The same arguments apply to a Poisson population $\mathrm{Poi}(\theta)$, with $T=\sum X_i\sim\mathrm{Poi}(n\theta)$.

### 5.2.4. Comparing the Means of Two Normal Populations

Let $\boldsymbol{X}=(X_1,\dots,X_m)$ be a sample from $\mathcal{N}(\mu_1,\sigma_1^2)$ and $\boldsymbol{Y}=(Y_1,\dots,Y_n)$ a sample from $\mathcal{N}(\mu_2,\sigma_2^2)$, independent of each other. Typical questions: is a new treatment better than the standard one (Example 5.1.5)? Do professors and assistant professors, or men and women, earn significantly different salaries? Consider

$$
\text{(7) } \mu_1-\mu_2=\mu_0 \text{ vs. } \mu_1-\mu_2\ne\mu_0;\quad
\text{(8) } \mu_1-\mu_2\le\mu_0 \text{ vs. } \mu_1-\mu_2>\mu_0;\quad
\text{(9) } \mu_1-\mu_2\ge\mu_0 \text{ vs. } \mu_1-\mu_2<\mu_0,
$$
in the cases (a) $\sigma_1^2,\sigma_2^2$ known; (b) $\sigma_1^2=\sigma_2^2=\sigma^2$ unknown; (c) $\sigma_1^2,\sigma_2^2$ unknown and possibly different; (d) $m=n$ and the samples paired, so that $X_i$ and $Y_i$ may be dependent.

In case (a), $\bar X-\bar Y$ estimates $\mu_1-\mu_2$, and under $\mu_1-\mu_2=\mu_0$

$$
U=\frac{\bar X-\bar Y-\mu_0}{\sqrt{\sigma_1^2/m+\sigma_2^2/n}}\sim\mathcal{N}(0,1).
$$
As in Section 5.2.1, the rejection regions for (7), (8), (9) are $\{\lvert U\rvert>z_{\alpha/2}\}$, $\{U>z_\alpha\}$, $\{U<-z_\alpha\}$ (the two-sample Z-test).

In case (b), with the pooled variance $S_p^2=\big((m-1)S_X^2+(n-1)S_Y^2\big)/(m+n-2)$,

$$
T=\frac{\bar X-\bar Y-\mu_0}{S_p\sqrt{1/m+1/n}}\overset{\mu_1-\mu_2=\mu_0}{\sim}t_{m+n-2},
$$
and the rejection regions are $\{\lvert T\rvert>t_{m+n-2,\alpha/2}\}$, $\{T>t_{m+n-2,\alpha}\}$, $\{T<-t_{m+n-2,\alpha}\}$ (the two-sample $t$-test).

**Example 5.2.5** To compare the red blood cell counts of healthy adult men and women, $156$ men and $74$ women were examined, with sample means and standard deviations (in $10^4/\mathrm{mm^3}$)

$$
\bar x=465.13,\ s_X=54.80\ \text{(men)};\qquad \bar y=422.16,\ s_Y=49.20\ \text{(women)}.
$$
Assuming normal populations with equal variances, is the count related to sex ($\alpha=0.01$)? We test $\mu_1-\mu_2=0$ vs. $\mu_1-\mu_2\ne0$. Here $t_{228,0.005}=2.598$ and

$$
\lvert t\rvert=\frac{\lvert\bar x-\bar y\rvert}{s_p\sqrt{1/156+1/74}}=5.74>2.598,
$$
so $H_0$ is rejected; the $p$-value is $\mathbb{P}(\lvert t_{228}\rvert\ge5.74)=3\times10^{-8}$.

Case (c) is the Behrens–Fisher problem, which has no exact solution of the above kind. When $m,n$ are not large, B. L. Welch (1938) proposed the statistic

$$
T_*=\frac{\bar X-\bar Y-\mu_0}{\sqrt{S_X^2/m+S_Y^2/n}},
$$
which is not $t$-distributed, but whose distribution under $\mu_1-\mu_2=\mu_0$ is well approximated by $t_r$, where $r$ is the integer nearest to

$$
\left(\frac{S_X^2}{m}+\frac{S_Y^2}{n}\right)^2\Bigg/\left[\frac{S_X^4}{m^2(m-1)}+\frac{S_Y^4}{n^2(n-1)}\right].
$$
The rejection regions $\{\lvert T_*\rvert>t_{r,\alpha/2}\}$, $\{T_*>t_{r,\alpha}\}$, $\{T_*<-t_{r,\alpha}\}$ have level approximately $\alpha$; this is *Welch's t-test* (statistical software uses the non-integer $r$ directly). When $m,n$ are large, the normal approximation of Section 5.2.6 can be used instead.

Case (d) arises, for example, in the following study. To study a sleeping pill, the nightly sleep times $X_i$ before and $Y_i$ after taking the pill are recorded for $n$ insomnia patients. Such paired data violate the assumptions above: $X_i$ and $Y_i$ are dependent (same patient), and the $X_i$ are not identically distributed (different patients). The remedy, called *paired comparison*, is to work with the differences $Z_i=Y_i-X_i$, which must be meaningful (the effect of the pill on patient $i$), with average effect $\mu=\mathbb{E}Z_i$, and to assume $Z_1,\dots,Z_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$. Testing $H_0\colon\mu=0$ vs. $H_1\colon\mu\ne0$ is then a one-sample $t$-test with rejection region $\{\lvert\sqrt{n}\,\bar Z/S_Z\rvert>t_{n-1,\alpha/2}\}$, where $\bar Z$, $S_Z^2$ are the sample mean and variance of the differences.

**Example 5.2.6** Two spectrometers $A$ and $B$ measure the metal content of $9$ material samples with different contents (in $\%$):

| sample | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| $A$ | 0.20 | 0.30 | 0.40 | 0.50 | 0.60 | 0.70 | 0.80 | 0.90 | 1.00 |
| $B$ | 0.10 | 0.21 | 0.52 | 0.32 | 0.78 | 0.59 | 0.68 | 0.77 | 0.89 |

Do the instruments differ significantly at $\alpha=0.01$? The measurements of different samples are not identically distributed, and $X_i$, $Y_i$ refer to the same sample, so we use $Z_i=X_i-Y_i$; if the instruments are equally good, $Z_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$. Here $\bar z=0.06$, $s_Z^2=0.01505$, $s_Z=0.1227$, $t_{8,0.005}=3.355$, and

$$
\frac{\sqrt{9}\,\lvert\bar z\rvert}{s_Z}=\frac{3\times0.06}{0.1227}=1.47<3.355.
$$
The data do not provide enough evidence of a difference; the $p$-value is $0.18$.

### 5.2.5. Comparing the Variances of Two Normal Populations

For the same two independent samples consider

$$
\text{(10) } \frac{\sigma_2^2}{\sigma_1^2}=1 \text{ vs. } \frac{\sigma_2^2}{\sigma_1^2}\ne1;\quad
\text{(11) } \frac{\sigma_2^2}{\sigma_1^2}\le1 \text{ vs. } \frac{\sigma_2^2}{\sigma_1^2}>1;\quad
\text{(12) } \frac{\sigma_2^2}{\sigma_1^2}\ge1 \text{ vs. } \frac{\sigma_2^2}{\sigma_1^2}<1.
$$
If the means are unknown, $S_X^2$ and $S_Y^2$ are unbiased estimates of $\sigma_1^2$ and $\sigma_2^2$, and $H_0$ in (10) is doubtful when $S_Y^2/S_X^2$ is too small or too large. Under $\sigma_1^2=\sigma_2^2$,

$$
F=\frac{S_Y^2}{S_X^2}\sim F_{n-1,m-1},
$$
and the rejection regions are $\{F<F_{n-1,m-1,1-\alpha/2}\text{ or }F>F_{n-1,m-1,\alpha/2}\}$, $\{F>F_{n-1,m-1,\alpha}\}$ and $\{F<F_{n-1,m-1,1-\alpha}\}$. If the means are known, then with $S_{X*}^2=\sum_{i=1}^m(X_i-\mu_1)^2/m$ and $S_{Y*}^2=\sum_{j=1}^n(Y_j-\mu_2)^2/n$, the statistic $F_*=S_{Y*}^2/S_{X*}^2\sim F_{n,m}$ under $H_0$, and the degrees of freedom become $n,m$. Tests based on the $F$ distribution are called *F-tests*.

**Example 5.2.7** Two batches of $6$ electronic components have mean resistances $\bar x=0.140$, $\bar y=0.139$ and sample standard deviations $s_X=0.0026$, $s_Y=0.0024$. Assuming $\mathcal{N}(\mu_1,\sigma_1^2)$ and $\mathcal{N}(\mu_2,\sigma_2^2)$ with all parameters unknown and independent samples, are the mean resistances equal ($\alpha=0.05$)? Since we do not know whether $\sigma_1^2=\sigma_2^2$, we first test $\sigma_2^2=\sigma_1^2$ with the $F$-test: $s_Y^2/s_X^2=0.0024^2/0.0026^2=0.85$, and $F_{5,5,0.975}=0.14<0.85<F_{5,5,0.025}=7.15$, so equal variances are not rejected. We then test $\mu_1=\mu_2$ with the two-sample $t$-test: $\lvert t\rvert=0.693<t_{10,0.025}=2.228$, so there is not enough evidence that the mean resistances differ.

**Example 5.2.8** For the salaries of $397$ American professors in 2008–09 (the `Salaries` data of R), the two-step procedure gives:

| Comparison | $m$ | $n$ | $\bar x$ | $\bar y$ | $s_X$ | $s_Y$ | $F$-test | Mean test |
|---|---|---|---|---|---|---|---|---|
| professors vs. assistant professors | 266 | 67 | 126772 | 80776 | 27719 | 8174 | $F=11.50$, $p<10^{-15}$ | Welch: $t=23.33$, $r=324.3$, $p<10^{-15}$ |
| men vs. women | 358 | 39 | 115090 | 101002 | 30437 | 25922 | $F=1.38$, $p=0.23$ | pooled: $t=2.78$, $p=0.0057$ |

The variances of the first pair differ greatly, so Welch's test is used; those of the second pair do not differ significantly, so the pooled $t$-test is used. Both mean differences are significant at $\alpha=0.01$.

### 5.2.6. Large-Sample Tests

Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}F$ with mean $\mu$ and variance $\sigma^2\in(0,\infty)$. If $F$ is normal, $\sqrt{n}(\bar X_n-\mu)/\sigma\sim\mathcal{N}(0,1)$ and $\sqrt{n}(\bar X_n-\mu)/S\sim t_{n-1}$. Otherwise these exact distributions are unknown, but by the **central limit theorem**, the **law of large numbers** ($S\to\sigma$ almost surely) and Slutsky's theorem,

$$
\frac{\sqrt{n}(\bar X_n-\mu)}{\sigma}\xrightarrow{d}\mathcal{N}(0,1),\qquad \frac{\sqrt{n}(\bar X_n-\mu)}{S}\xrightarrow{d}\mathcal{N}(0,1).
$$
Replacing exact quantiles by $z_\alpha$ gives tests whose level is approximately $\alpha$ for large $n$.

**Proposition 5.2.3** In the two-sample setting with $\sigma_1^2,\sigma_2^2$ unknown, under $\mu_1-\mu_2=\mu_0$,

$$
U^*=\frac{\bar X-\bar Y-\mu_0}{\sqrt{S_X^2/m+S_Y^2/n}}\xrightarrow{d}\mathcal{N}(0,1)\qquad(m,n\to\infty),
$$
whether or not the populations are normal, provided the variances are finite and positive. Hence $\{\lvert U^*\rvert>z_{\alpha/2}\}$, $\{U^*>z_\alpha\}$, $\{U^*<-z_\alpha\}$ are rejection regions of approximate level $\alpha$ for (7), (8), (9).

**Proof** Write

$$
U^*=\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{\sqrt{\sigma_1^2/m+\sigma_2^2/n}}\cdot\sqrt{\frac{\sigma_1^2/m+\sigma_2^2/n}{S_X^2/m+S_Y^2/n}}.
$$
The first factor is exactly $\mathcal{N}(0,1)$ for normal populations and tends to $\mathcal{N}(0,1)$ in distribution by the central limit theorem in general. Since $S_X^2\to\sigma_1^2$ and $S_Y^2\to\sigma_2^2$ almost surely, the ratio $\big(\sigma_1^2/m+\sigma_2^2/n\big)/\big(S_X^2/m+S_Y^2/n\big)$ lies between $\min(\sigma_1^2/S_X^2,\sigma_2^2/S_Y^2)$ and $\max(\sigma_1^2/S_X^2,\sigma_2^2/S_Y^2)$, so the second factor tends to $1$. Slutsky's theorem gives the claim. $\square$

**Example 5.2.9** In Example 5.2.5, drop the assumption of equal variances. With $z_{0.005}=2.576$,

$$
\lvert u^*\rvert=\frac{\lvert422.16-465.13\rvert}{\sqrt{54.80^2/156+49.20^2/74}}=5.96>2.576,
$$
so $H_0$ is rejected again; the $p$-value is $\mathbb{P}(\lvert\mathcal{N}(0,1)\rvert\ge5.96)=2.5\times10^{-9}$.

The same idea applies to Bernoulli and Poisson means. For a sample from $\mathrm{Ber}(\theta)$, $\sqrt{n}(\bar X-\theta)/\sqrt{\theta(1-\theta)}\xrightarrow{d}\mathcal{N}(0,1)$, so under $H_0\colon\theta=\theta_0$

$$
U=\frac{\sqrt{n}(\bar X-\theta_0)}{\sqrt{\theta_0(1-\theta_0)}}\xrightarrow{d}\mathcal{N}(0,1),
$$
and $\{\lvert U\rvert>z_{\alpha/2}\}$, $\{U>z_\alpha\}$ (for $\theta\le\theta_0$ vs. $\theta>\theta_0$) and $\{U<-z_\alpha\}$ (for $\theta\ge\theta_0$ vs. $\theta<\theta_0$) have approximate level $\alpha$. For $\mathrm{Poi}(\theta)$ the statistic is $U_0=\sqrt{n}(\bar X-\theta_0)/\sqrt{\theta_0}$, with the same regions.

**Remark 5.2.5** The large-sample tests do not need the normality assumption. For example, to compare the support rates of two candidates we may take $X_i\overset{\text{iid}}{\sim}\mathrm{Ber}(\theta_1)$ and $Y_j\overset{\text{iid}}{\sim}\mathrm{Ber}(\theta_2)$ and use $U^*$. In summary, for two normal means with unknown unequal variances, Welch's $t$ approximation is used when $m$ or $n$ is small and the normal approximation when both are large; when the samples are small and the populations not normal, resampling methods such as the bootstrap can be used.

## 5.3. Likelihood Ratio Tests

The tests of Section 5.2 were found by intuition. The likelihood ratio test, proposed by J. Neyman and E. S. Pearson in 1928, is a general method that plays in testing the role that **maximum likelihood estimation** plays in point estimation; it is widely applicable, and most of the work needed to set it up has already been done in finding the maximum likelihood estimators.

### 5.3.1. Definition

For a simple problem $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$ it is natural to reject $H_0$ when the likelihood of $\theta_0$ is small relative to that of $\theta_1$, $L(\theta_0;\boldsymbol{x})/L(\theta_1;\boldsymbol{x})<c$. For composite hypotheses we compare the best fit within $\Theta_0$ with the best fit overall. Let $L(\theta)=f(\boldsymbol{x};\theta)=\prod_{i=1}^nf(x_i;\theta)$ be the likelihood, and let $\hat\theta_{\mathrm{MLE},0}$ and $\hat\theta_{\mathrm{MLE}}$ maximize it over $\Theta_0$ and over $\Theta$:

$$
\sup_{\theta\in\Theta_0}L(\theta;\boldsymbol{x})=L(\hat\theta_{\mathrm{MLE},0}),\qquad \sup_{\theta\in\Theta}L(\theta;\boldsymbol{x})=L(\hat\theta_{\mathrm{MLE}}).
$$
If $H_0$ is true and $L$ is continuous in $\theta$, both estimators approach the true value $\theta_0\in\Theta_0$ as $n$ grows, so the two maximal likelihoods are close and their ratio is close to $1$; if $H_0$ is false, the estimators need not be close, and neither need the ratio be.

**Definition 5.3.1 (Likelihood Ratio Test)** The **likelihood ratio** is

$$
\lambda(\boldsymbol{x})=\frac{L(\hat\theta_{\mathrm{MLE},0})}{L(\hat\theta_{\mathrm{MLE}})}=\frac{\sup_{\theta\in\Theta_0}f(\boldsymbol{x};\theta)}{\sup_{\theta\in\Theta}f(\boldsymbol{x};\theta)}\in[0,1].
$$
The **likelihood ratio test** rejects $H_0$ when $\lambda(\boldsymbol{x})<\lambda_0$, equivalently when $-2\log\lambda(\boldsymbol{x})>C=-2\log\lambda_0$:

$$
\varphi(\boldsymbol{x})=\begin{cases}1, & \lambda<\lambda_0,\\ r, & \lambda=\lambda_0,\\ 0, & \lambda>\lambda_0,\end{cases}
$$
where $r=0$ for continuous distributions and $r\in(0,1)$ may be needed for discrete ones. The constants $\lambda_0$ (or $C$) and $r$ are determined by the level: $\mathbb{E}_\theta\varphi(\boldsymbol{X})\le\alpha$ for all $\theta\in\Theta_0$.

**Remark 5.3.1** Taking the supremum over $\Theta$ rather than over $\Theta_1$ in the denominator guarantees $\lambda\le1$ and makes the denominator the maximized likelihood itself. In practice one rarely works with the distribution of $\lambda$ directly: one shows that $\lambda$ is a monotone function of a familiar statistic and rewrites the rejection region in terms of it, or, for large samples, uses the limiting distribution of $-2\log\lambda$ (Section 5.3.4).

### 5.3.2. Two Examples

**Example 5.3.1** Let $X$ be a single observation from the Cauchy density $f(x;\theta)=\dfrac{1}{\pi}\cdot\dfrac{1}{1+(x-\theta)^2}$, $\theta\in\mathbb{R}$. Find the likelihood ratio test of $H_0\colon\theta=0$ vs. $H_1\colon\theta\ne0$ at level $\alpha$.

The likelihood $f(x;\theta)$ is maximized at $\theta=x$, with maximum $1/\pi$, so

$$
\lambda=\frac{1/[\pi(1+x^2)]}{1/\pi}=\frac{1}{1+x^2},
$$
and $\lambda<\lambda_0$ if and only if $x^2>1/\lambda_0-1$, that is, $\lvert x\rvert>C$. By symmetry of $f(x;0)$, $C$ is determined by $\mathbb{P}_0(X>C)=\alpha/2$. Substituting $x=\tan t$,

$$
\mathbb{P}_0(X>C)=\int_C^\infty\frac{\mathrm{d}x}{\pi(1+x^2)}=\frac1\pi\left(\frac\pi2-\arctan C\right)=\frac\alpha2,
$$
so $C=\tan\big((1-\alpha)\pi/2\big)$. For $\alpha=0.05$, $C=\tan(0.475\pi)=12.706$, and $H_0$ is rejected when $\lvert x\rvert>12.706$.

**Example 5.3.2** Let $X_1,\dots,X_n$ be a sample from $\mathrm{Exp}(\theta)$, $f(x;\theta)=\theta\mathrm{e}^{-\theta x}$ ($x>0$, $\theta>0$). Find the likelihood ratio test of $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta\ne\theta_0$.

With $t=\sum_{i=1}^nx_i$, $L(\theta)=\theta^n\mathrm{e}^{-\theta t}$ and the maximum likelihood estimator is $\hat\theta=n/t$. Hence

$$
\lambda=\frac{\theta_0^n\mathrm{e}^{-\theta_0t}}{(n/t)^n\mathrm{e}^{-n}}=\left(\frac{\mathrm{e}\theta_0}{n}\right)^nt^n\mathrm{e}^{-\theta_0t},
$$
and $\lambda<\lambda_0$ if and only if $g(t)=t\mathrm{e}^{-\theta_0t/n}<C_0$. The function $g$ increases on $(0,n/\theta_0)$, decreases on $(n/\theta_0,\infty)$ and attains its maximum at $t=n/\theta_0$, so $g(t)<C_0$ if and only if $t<C_1$ or $t>C_2$, where $C_1<n/\theta_0<C_2$ satisfy $g(C_1)=g(C_2)=C_0$. With $T=\sum X_i$, the level condition is $\mathbb{P}_{\theta_0}(T<C_1)+\mathbb{P}_{\theta_0}(T>C_2)=\alpha$. Under $H_0$, $T\sim\Gamma(n,\theta_0)$, i.e. $2\theta_0T\sim\chi^2_{2n}$.

The exact test requires solving the two equations $g(C_1)=g(C_2)$ and the level condition simultaneously. For simplicity one usually takes equal tails, $\mathbb{P}_{\theta_0}(T<C_1)=\mathbb{P}_{\theta_0}(T>C_2)=\alpha/2$, that is, $C_1=\chi^2_{2n,1-\alpha/2}/(2\theta_0)$ and $C_2=\chi^2_{2n,\alpha/2}/(2\theta_0)$; this is an approximation to the likelihood ratio test of the same level. For $n=2$, $\alpha=0.05$ the equal-tailed equations read $0.975\mathrm{e}^p-p=1$ and $0.025\mathrm{e}^q-q=1$ for $p=\theta_0C_1$, $q=\theta_0C_2$, giving $p=0.242$, $q=5.572$: reject when $t<0.242/\theta_0$ or $t>5.572/\theta_0$. The exact likelihood ratio test would use $\theta_0C_1=0.304$, $\theta_0C_2=6.401$.

### 5.3.3. Likelihood Ratio Tests for Normal Populations

The tests of Section 5.2 for normal populations are all likelihood ratio tests. Below, $\omega=\Theta_0$, $\Omega=\Theta$, and $\hat\omega$, $\hat\Omega$ denote the maximum likelihood estimators over them.

**Example 5.3.3 (Mean, $\sigma$ known.)** For $H_0\colon\mu=\mu_0$ with $\Omega=\{\mu\in\mathbb{R}\}$,

$$
L(\hat\omega)=(2\pi\sigma^2)^{-n/2}\exp\Big[-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu_0)^2\Big],\qquad L(\hat\Omega)=(2\pi\sigma^2)^{-n/2}\exp\Big[-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\bar x)^2\Big],
$$
so

$$
-2\log\lambda=\frac{1}{\sigma^2}\sum_{i=1}^n\big[(x_i-\mu_0)^2-(x_i-\bar x)^2\big]=\left[\frac{\sqrt{n}(\bar x-\mu_0)}{\sigma}\right]^2.
$$
Thus $-2\log\lambda>C^2$ if and only if $\lvert\sqrt{n}(\bar x-\mu_0)/\sigma\rvert>C$, and the level condition gives $C=z_{\alpha/2}$: the likelihood ratio test is the two-sided Z-test.

**Example 5.3.4 (Mean, $\sigma$ unknown.)** Now $\omega=\{(\mu_0,\sigma^2)\colon\sigma^2>0\}$, $\Omega=\{(\mu,\sigma^2)\colon\mu\in\mathbb{R},\sigma^2>0\}$, $\hat\sigma_\omega^2=\frac1n\sum(x_i-\mu_0)^2$, $\hat\sigma_\Omega^2=\frac1n\sum(x_i-\bar x)^2$, and both maximal likelihoods have the form $(2\pi\hat\sigma^2)^{-n/2}\mathrm{e}^{-n/2}$. Hence, using $\sum(x_i-\mu_0)^2=\sum(x_i-\bar x)^2+n(\bar x-\mu_0)^2$,

$$
\lambda^{2/n}=\frac{\hat\sigma_\Omega^2}{\hat\sigma_\omega^2}=\frac{\sum(x_i-\bar x)^2}{\sum(x_i-\bar x)^2+n(\bar x-\mu_0)^2}=\frac{1}{1+t^2/(n-1)},\qquad t=\frac{\sqrt{n}(\bar x-\mu_0)}{s}.
$$
Since $\lambda$ is a decreasing function of $t^2$, the test rejects when $\lvert t\rvert>C$, and $C=t_{n-1,\alpha/2}$: the two-sided $t$-test.

**Example 5.3.5 (One-sided, $\sigma$ unknown.)** For $H_0\colon\mu\le\mu_0$, $\omega=\{(\mu,\sigma^2)\colon\mu\le\mu_0\}$ and $L(\hat\Omega)$ is as before. Since

$$
L(\mu,\sigma^2)=(2\pi\sigma^2)^{-n/2}\exp\Big[-\frac{1}{2\sigma^2}\sum(x_i-\bar x)^2-\frac{n(\bar x-\mu)^2}{2\sigma^2}\Big],
$$
for each $\sigma^2$ the likelihood is maximized over $\mu\le\mu_0$ at $\mu=\bar x$ if $\bar x\le\mu_0$ and at $\mu=\mu_0$ if $\bar x>\mu_0$. Therefore

$$
\lambda=\begin{cases}1, & \bar x\le\mu_0,\\ \left(1+\dfrac{t^2}{n-1}\right)^{-n/2}, & \bar x>\mu_0,\end{cases}
$$
which is a nonincreasing function of $t$. The rejection region $\{\lambda<\lambda_0\}$ is $\{t>c\}$, and $\mathbb{P}_{\mu_0}(T>c)=\alpha$ gives $c=t_{n-1,\alpha}$. That this test has level $\alpha$ on the whole of $\omega$ follows because its power function is increasing in $\mu$: under $\mathbb{P}_{\mu,\sigma}$, $T$ has a noncentral $t$ distribution with noncentrality $\sqrt{n}(\mu-\mu_0)/\sigma$, which is stochastically increasing in the noncentrality.

**Example 5.3.6 (Variance, $\mu$ known.)** For $H_0\colon\sigma^2=\sigma_0^2$, $\hat\sigma_\Omega^2=\frac1n\sum(x_i-\mu)^2$ and

$$
\lambda=\left(\frac{\hat\sigma_\Omega^2}{\sigma_0^2}\right)^{n/2}\mathrm{e}^{n/2}\exp\Big[-\frac{1}{2\sigma_0^2}\sum(x_i-\mu)^2\Big]=\mathrm{e}^{n/2}u^{n/2}\mathrm{e}^{-nu/2},\qquad u=\frac1n\sum_{i=1}^n\left(\frac{x_i-\mu}{\sigma_0}\right)^2.
$$
The function $\lambda(u)$, $u\ge0$, is $0$ at $u=0$, strictly increasing on $[0,1]$, strictly decreasing on $(1,\infty)$ with maximum $\lambda(1)=1$, and tends to $0$ as $u\to\infty$. Hence $\lambda\le\lambda_0$ if and only if $u\le C_1$ or $u\ge C_2$. Under $H_0$, $nU=\sum((X_i-\mu)/\sigma_0)^2\sim\chi^2_n$, and splitting $\alpha$ equally between the tails gives $nC_1=\chi^2_{n,1-\alpha/2}$, $nC_2=\chi^2_{n,\alpha/2}$: the $\chi^2$ test of Section 5.2.2 (again with the equal-tail simplification).

**Example 5.3.7 (Variance, $\mu$ unknown.)** Now $\hat\mu_\omega=\hat\mu_\Omega=\bar x$, $\hat\sigma_\Omega^2=\frac1n\sum(x_i-\bar x)^2$, and

$$
\lambda=\left(\frac{\hat\sigma_\Omega^2}{\sigma_0^2}\right)^{n/2}\mathrm{e}^{n/2}\exp\Big[-\frac{1}{2\sigma_0^2}\sum(x_i-\bar x)^2\Big];
$$
the same argument with $u=\frac1n\sum((x_i-\bar x)/\sigma_0)^2$ leads to rejection when $\sum((x_i-\bar x)/\sigma_0)^2\le\chi^2_{n-1,1-\alpha/2}$ or $\ge\chi^2_{n-1,\alpha/2}$.

**Example 5.3.8 (Two means, equal unknown variances.)** For two independent samples from $\mathcal{N}(\mu_1,\sigma^2)$ and $\mathcal{N}(\mu_2,\sigma^2)$, test $H_0\colon\mu_1=\mu_2$. Over $\Omega$, $\hat\mu_1=\bar x$, $\hat\mu_2=\bar y$, $\hat\sigma_\Omega^2=\frac{1}{m+n}\big[\sum(x_i-\bar x)^2+\sum(y_j-\bar y)^2\big]$; over $\omega=\{(\mu,\mu,\sigma^2)\}$, $\hat\mu_\omega=(m\bar x+n\bar y)/(m+n)$ and $\hat\sigma_\omega^2=\frac{1}{m+n}\big[\sum(x_i-\hat\mu_\omega)^2+\sum(y_j-\hat\mu_\omega)^2\big]$. Both maximal likelihoods have the form $(2\pi\hat\sigma^2)^{-(m+n)/2}\mathrm{e}^{-(m+n)/2}$, so $\lambda^{2/(m+n)}=\hat\sigma_\Omega^2/\hat\sigma_\omega^2$. Since $\sum(x_i-\hat\mu_\omega)^2=\sum(x_i-\bar x)^2+\frac{mn^2(\bar x-\bar y)^2}{(m+n)^2}$ and similarly for $y$,

$$
\hat\sigma_\omega^2=\hat\sigma_\Omega^2+\frac{mn(\bar x-\bar y)^2}{(m+n)^2},\qquad
\lambda^{2/(m+n)}=\left(1+\frac{t^2}{m+n-2}\right)^{-1},
$$
where

$$
t=\sqrt{\frac{mn}{m+n}}\,(\bar x-\bar y)\Bigg/\sqrt{\frac{1}{m+n-2}\Big[\sum_{i=1}^m(x_i-\bar x)^2+\sum_{j=1}^n(y_j-\bar y)^2\Big]}
$$
is the two-sample $t$ statistic. The likelihood ratio test rejects when $\lvert t\rvert>t_{m+n-2,\alpha/2}$.

**Example 5.3.9 (Two variances, means unknown.)** For $H_0\colon\sigma_1^2=\sigma_2^2$, let $a=\sum(x_i-\bar x)^2$ and $b=\sum(y_j-\bar y)^2$. Then $\hat\sigma_{1,\Omega}^2=a/m$, $\hat\sigma_{2,\Omega}^2=b/n$, $\hat\sigma_\omega^2=(a+b)/(m+n)$, and

$$
\lambda=\frac{(\hat\sigma_{1,\Omega}^2)^{m/2}(\hat\sigma_{2,\Omega}^2)^{n/2}}{(\hat\sigma_\omega^2)^{(m+n)/2}}=\frac{(m+n)^{(m+n)/2}}{m^{m/2}n^{n/2}}\cdot\frac{\big(\frac{m-1}{n-1}u\big)^{m/2}}{\big(1+\frac{m-1}{n-1}u\big)^{(m+n)/2}},\qquad u=\frac{a/(m-1)}{b/(n-1)}.
$$
As a function of $u\ge0$, $\lambda$ increases up to its maximum $1$ at $u_0=\frac{m(n-1)}{n(m-1)}$ and then decreases to $0$, so $\lambda\le\lambda_0$ if and only if $u\le C_1$ or $u\ge C_2$. Under $H_0$, $U=S_X^2/S_Y^2\sim F_{m-1,n-1}$; with equal tails $C_1=F_{m-1,n-1,1-\alpha/2}$, $C_2=F_{m-1,n-1,\alpha/2}$: the $F$-test.

### 5.3.4. The Limiting Distribution of the Likelihood Ratio

When $\lambda$ cannot be reduced to a statistic with a known distribution, the following theorem gives an approximate test.

**Theorem 5.3.1 (Wilks' Theorem)** Suppose that $\Theta$ has dimension $k$ and $\Theta_0$ has dimension $s$, with $k-s=t>0$, and that the density satisfies certain regularity conditions. Then for testing $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$, under $H_0$ and as $n\to\infty$,

$$
-2\log\lambda(\boldsymbol{X})\xrightarrow{d}\chi^2_t.
$$
Consequently $\{-2\log\lambda>\chi^2_{t,\alpha}\}$ is a rejection region of approximate level $\alpha$.

**Remark 5.3.2** The dimension of $\Theta$ must be strictly larger than that of $\Theta_0$; for example, for a normal sample and $H_0\colon\mu=\mu_0$, $\Theta=\{(\mu,\sigma^2)\colon\mu\in\mathbb{R},\sigma^2>0\}$ has dimension $2$ and $\Theta_0=\{(\mu_0,\sigma^2)\colon\sigma^2>0\}$ dimension $1$. $\Theta_0$ may contain many points: the limit $\chi^2_t$ is the same for every $\theta\in\Theta_0$. The regularity conditions are those that make the maximum likelihood estimator asymptotically normal (the true value is an interior point, the dimension of the parameter is fixed as $n\to\infty$, and so on). In Example 5.3.4, $-2\log\lambda=n\log\big(1+T^2/(n-1)\big)\approx T^2\xrightarrow{d}\chi^2_1$, in agreement with the theorem.

**Example 5.3.10** Let $\boldsymbol{X}_i=(X_{i1},\dots,X_{in_i})$ be independent samples from $\mathcal{N}(\mu_i,\sigma_i^2)$, $i=1,\dots,m$. Derive the likelihood ratio test of $H_0\colon\sigma_1^2=\dots=\sigma_m^2$ against the alternative that they are not all equal.

Let $\theta=(\mu_1,\dots,\mu_m;\sigma_1^2,\dots,\sigma_m^2)$, so $\Theta$ has dimension $k=2m$ and $\Theta_0=\{\theta\colon\sigma_1^2=\dots=\sigma_m^2\}$ has dimension $s=m+1$. Let

$$
\bar X_i=\frac{1}{n_i}\sum_{j=1}^{n_i}X_{ij},\qquad S_i^2=\frac{1}{n_i}\sum_{j=1}^{n_i}(X_{ij}-\bar X_i)^2,\qquad S^2=\frac1n\sum_{i=1}^mn_iS_i^2,\qquad n=\sum_{i=1}^mn_i.
$$
Over $\Theta$ the maximum likelihood estimators are $\hat\mu_i=\bar X_i$, $\hat\sigma_i^2=S_i^2$, and $L(\hat\theta_{\mathrm{MLE}})=(2\pi\mathrm{e})^{-n/2}\prod_iS_i^{-n_i}$; under $H_0$, $\hat\sigma^2=S^2$ and $L(\hat\theta_{\mathrm{MLE},0})=(2\pi\mathrm{e})^{-n/2}S^{-n}$. Hence

$$
\lambda=\prod_{i=1}^mS_i^{n_i}\Big/S^n,\qquad -2\log\lambda=n\log S^2-\sum_{i=1}^mn_i\log S_i^2.
$$
By Theorem 5.3.1, as $\min\{n_1,\dots,n_m\}\to\infty$, $-2\log\lambda\xrightarrow{d}\chi^2_{m-1}$ under $H_0$, and $\{-2\log\lambda>\chi^2_{m-1,\alpha}\}$ is a rejection region of approximate level $\alpha$. (With a small-sample correction this is Bartlett's test for homogeneity of variances.)

## 5.4. Uniformly Most Powerful Tests

### 5.4.1. Definition

A testing problem has many tests of the same level; how should they be compared? By the Neyman–Pearson principle, every competitor must have probability of a type I error at most $\alpha$ on $\Theta_0$, and among these, the smaller the type II error, that is, the larger the power on $\Theta_1$, the better. For $H_0\colon\mu\le0$ vs. $H_1\colon\mu>0$ one level-$0.05$ test may dominate another for every $\mu>0$; but two tests can also have crossing power curves, in which case neither is better everywhere. The ideal is a test that is best at every point of $\Theta_1$ at once.

**Definition 5.4.1 (Uniformly Most Powerful Test)** Consider $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$. Let $\varphi$ be a test of level $\alpha$. If $\pi_\varphi(\theta)\ge\pi_{\varphi^*}(\theta)$ for all $\theta\in\Theta_1$ and every test $\varphi^*$ of level $\alpha$, then $\varphi$ is called a **uniformly most powerful test** (UMP test) of level $\alpha$. When $H_1$ is simple, $\Theta_1=\{\theta_1\}$, a UMP test is called a **most powerful test** (MP test).

**Remark 5.4.1** UMP tests are rare. They exist essentially only when $\theta$ is real-valued, for certain forms of $H_0$ and $H_1$ (mainly one-sided ones) and for special families $f(x;\theta)$. For multidimensional parameters, reasonable tests are constructed by other principles: likelihood ratio tests, goodness-of-fit tests ([3.2.6](/3.2.6)), decision-theoretic tests, and so on. For a simple null against a simple alternative an MP test always exists, by the Neyman–Pearson lemma below. That problem is unrealistic in itself, but it is the first step towards one-sided composite problems.

### 5.4.2. The Neyman–Pearson Lemma

**Theorem 5.4.1 (Neyman–Pearson Lemma)** Let $\boldsymbol{X}$ have density (or probability mass function) $f(\boldsymbol{x};\theta)$, and consider $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$ at level $\alpha\in(0,1)$. Define

$$
\varphi(\boldsymbol{x})=\begin{cases}1, & f(\boldsymbol{x};\theta_1)>Cf(\boldsymbol{x};\theta_0),\\ r, & f(\boldsymbol{x};\theta_1)=Cf(\boldsymbol{x};\theta_0),\\ 0, & f(\boldsymbol{x};\theta_1)<Cf(\boldsymbol{x};\theta_0).\end{cases}\tag{5.4}
$$
Then:

1. there exist constants $C\ge0$ and $r\in[0,1]$ such that
   $$
   \mathbb{E}_{\theta_0}\varphi(\boldsymbol{X})=\mathbb{P}_{\theta_0}\big(f(\boldsymbol{X};\theta_1)>Cf(\boldsymbol{X};\theta_0)\big)+r\,\mathbb{P}_{\theta_0}\big(f(\boldsymbol{X};\theta_1)=Cf(\boldsymbol{X};\theta_0)\big)=\alpha;
   $$
2. any test of the form (5.4) with $\mathbb{E}_{\theta_0}\varphi(\boldsymbol{X})=\alpha$ is a most powerful test among all tests of level $\alpha$.

**Proof** (1) Existence. Let $G$ be the distribution function of the likelihood ratio $f(\boldsymbol{X};\theta_1)/f(\boldsymbol{X};\theta_0)$ under $\mathbb{P}_{\theta_0}$ (the ratio is finite with $\mathbb{P}_{\theta_0}$-probability $1$, and nonnegative), $G(y)=\mathbb{P}_{\theta_0}\big(f(\boldsymbol{X};\theta_1)/f(\boldsymbol{X};\theta_0)\le y\big)$. It is nondecreasing and right-continuous, so there is $C\ge0$ with $G(C-0)\le1-\alpha\le G(C)$, where $G(C-0)=\lim_{y\uparrow C}G(y)$. Then

$$
\mathbb{E}_{\theta_0}\varphi(\boldsymbol{X})=1-G(C)+r\big[G(C)-G(C-0)\big].
$$
If $G$ is continuous at $C$, take $r=0$; otherwise take $r=\dfrac{G(C)-(1-\alpha)}{G(C)-G(C-0)}\in[0,1]$. In both cases $\mathbb{E}_{\theta_0}\varphi=\alpha$.

(2) Optimality. Let $\varphi^*$ be any test of level $\alpha$, and let $S^+=\{\boldsymbol{x}\colon\varphi(\boldsymbol{x})>\varphi^*(\boldsymbol{x})\}$, $S^-=\{\boldsymbol{x}\colon\varphi(\boldsymbol{x})<\varphi^*(\boldsymbol{x})\}$. On $S^+$, $\varphi>\varphi^*\ge0$, so $\varphi>0$ and, by (5.4), $f(\boldsymbol{x};\theta_1)-Cf(\boldsymbol{x};\theta_0)\ge0$; on $S^-$, $\varphi<\varphi^*\le1$, so $\varphi<1$ and $f(\boldsymbol{x};\theta_1)-Cf(\boldsymbol{x};\theta_0)\le0$. In both cases, and trivially elsewhere,

$$
\big[\varphi(\boldsymbol{x})-\varphi^*(\boldsymbol{x})\big]\big[f(\boldsymbol{x};\theta_1)-Cf(\boldsymbol{x};\theta_0)\big]\ge0.
$$
Integrating over $\mathcal{X}$ (summing in the discrete case),

$$
\int_{\mathcal{X}}\varphi f(\boldsymbol{x};\theta_1)\,\mathrm{d}\boldsymbol{x}-\int_{\mathcal{X}}\varphi^*f(\boldsymbol{x};\theta_1)\,\mathrm{d}\boldsymbol{x}\ge C\left[\int_{\mathcal{X}}\varphi f(\boldsymbol{x};\theta_0)\,\mathrm{d}\boldsymbol{x}-\int_{\mathcal{X}}\varphi^*f(\boldsymbol{x};\theta_0)\,\mathrm{d}\boldsymbol{x}\right]=C\big[\alpha-\mathbb{E}_{\theta_0}\varphi^*\big]\ge0,
$$
since $\mathbb{E}_{\theta_0}\varphi^*\le\alpha$. Hence $\mathbb{E}_{\theta_1}\varphi(\boldsymbol{X})\ge\mathbb{E}_{\theta_1}\varphi^*(\boldsymbol{X})$. $\square$

**Remark 5.4.2** For discrete $X_i$, a randomization $r\in(0,1)$ is in general indispensable to attain size exactly $\alpha$; for continuous $X_i$ the boundary has probability $0$ and $r=0$. The lemma holds verbatim for testing $H_0\colon f=f_0$ vs. $H_1\colon f=f_1$ with two arbitrary densities. Since the MP test depends on $\boldsymbol{x}$ only through the likelihood ratio, which by the factorization theorem ([3.2.2](/3.2.2)) depends only on a sufficient statistic, an MP test can always be chosen as a function of a sufficient statistic.

**Corollary 5.4.1** If $\varphi$ is a UMP test of level $\alpha$ for $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$, then $\mathbb{E}_\theta\varphi(\boldsymbol{X})\ge\alpha$ for all $\theta\in\Theta_1$.

**Proof** The constant test $\varphi^*\equiv\alpha$ has level $\alpha$, so $\mathbb{E}_\theta\varphi(\boldsymbol{X})\ge\mathbb{E}_\theta\varphi^*(\boldsymbol{X})=\alpha$ for $\theta\in\Theta_1$. $\square$

**Example 5.4.1** Let $X$ be a single observation from $f(x;\theta)=\theta x^{\theta-1}$, $0<x<1$ ($\theta>1$); this is a density since $\int_0^1\theta x^{\theta-1}\,\mathrm{d}x=1$. Find the MP test of $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$ at level $\alpha$ and its power.

By the lemma, $H_0$ is rejected when

$$
\frac{\theta_1x^{\theta_1-1}}{\theta_0x^{\theta_0-1}}>C^*,\quad\text{i.e.}\quad(\theta_1-\theta_0)\log x>\log\frac{\theta_0C^*}{\theta_1}.
$$
If $\theta_1>\theta_0$ this means $x>C$, and $\mathbb{P}_{\theta_0}(X>C)=1-C^{\theta_0}=\alpha$ gives $C=(1-\alpha)^{1/\theta_0}$; if $\theta_1<\theta_0$ it means $x<C$, and $\mathbb{P}_{\theta_0}(X<C)=C^{\theta_0}=\alpha$ gives $C=\alpha^{1/\theta_0}$. The power is

$$
\pi(\theta_1)=1-(1-\alpha)^{\theta_1/\theta_0}\ (\theta_1>\theta_0),\qquad \pi(\theta_1)=\alpha^{\theta_1/\theta_0}\ (\theta_1<\theta_0).
$$
For $\theta_0=4$, $\alpha=0.05$: if $\theta_1=6$, reject when $x>0.95^{1/4}=0.987$, with power $1-0.95^{1.5}=0.074$; if $\theta_1=2$, reject when $x<0.05^{1/4}=0.473$, with power $0.05^{1/2}=0.224$. With a single observation the power is low.

### 5.4.3. From Most Powerful to Uniformly Most Powerful Tests

**Proposition 5.4.1** Let $\varphi$ be an MP test of level $\alpha$ for $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$ ($\theta_1>\theta_0$). If $\varphi$ does not depend on $\theta_1$, then it is a UMP test of level $\alpha$ for $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta>\theta_0$.

**Proof** $\varphi$ has size $\alpha$ for the simple null $\theta=\theta_0$. Let $\varphi^*$ be any level-$\alpha$ test of this problem. For each fixed $\theta_1>\theta_0$, both $\varphi$ and $\varphi^*$ are level-$\alpha$ tests of $\theta=\theta_0$ vs. $\theta=\theta_1$, and $\varphi$ is MP for it, so $\mathbb{E}_{\theta_1}\varphi\ge\mathbb{E}_{\theta_1}\varphi^*$. $\square$

This gives a recipe for a general problem $H_0\colon\theta\in\Theta_0$ vs. $H_1\colon\theta\in\Theta_1$ with a real parameter:

1. choose $\theta_0\in\Theta_0$ as close to $\Theta_1$ as possible (the boundary point) and an arbitrary $\theta_1\in\Theta_1$;
2. construct the MP test $\varphi_{\theta_1}$ of $\theta=\theta_0$ vs. $\theta=\theta_1$ by the Neyman–Pearson lemma;
3. if $\varphi_{\theta_1}=\varphi$ does not depend on $\theta_1$, then $\varphi$ is UMP for $\theta=\theta_0$ vs. $\theta\in\Theta_1$;
4. if moreover $\mathbb{E}_\theta\varphi(\boldsymbol{X})\le\alpha$ for all $\theta\in\Theta_0$, then $\varphi$ is a UMP test of level $\alpha$ for $\theta\in\Theta_0$ vs. $\theta\in\Theta_1$ (every level-$\alpha$ test of the composite null is in particular a level-$\alpha$ test of $\theta=\theta_0$).

**Example 5.4.2** In Example 5.4.1:

1. the test rejecting $H_0\colon\theta=\theta_0$ when $x>(1-\alpha)^{1/\theta_0}$ is MP against every fixed $\theta_1>\theta_0$ and does not depend on $\theta_1$, so it is UMP of level $\alpha$ against $H_1\colon\theta>\theta_0$;
2. likewise, the test rejecting when $x<\alpha^{1/\theta_0}$ is UMP against $H_1'\colon\theta<\theta_0$;
3. there is no UMP test of $H_0\colon\theta=\theta_0$ against the two-sided alternative $H_1''\colon\theta\ne\theta_0$. A UMP test for it would be MP against each $\theta_1>\theta_0$ and against each $\theta_1<\theta_0$; by the uniqueness of MP tests (up to sets of probability zero) its rejection region would have to be both $\big((1-\alpha)^{1/\theta_0},1\big)$ and $\big(0,\alpha^{1/\theta_0}\big)$, which is impossible.

This is the typical situation: two-sided problems have no UMP test.

**Example 5.4.3** Let $X$ be a single observation from $f(x;\theta)=1+\theta^2\big(\tfrac12-x\big)$, $0<x<1$, $-1\le\theta\le1$, which is a density because it is nonnegative and $\int_0^1\big[1+\theta^2\big(\tfrac12-x\big)\big]\,\mathrm{d}x=1$. Test $H_0\colon\theta=0$ (the uniform distribution $\mathrm{U}(0,1)$) at level $\alpha$.

Against $H_1\colon\theta=\theta_1\ne0$, the lemma rejects when $1+\theta_1^2\big(\tfrac12-x\big)>C^*$, i.e. $x<C$, and $\mathbb{P}_0(X<C)=C=\alpha$. The test "reject when $x<\alpha$" does not depend on $\theta_1$, so it is UMP for $H_0\colon\theta=0$ against the two-sided alternative $H_1'\colon\theta\ne0$ (because $\theta$ enters only through $\theta^2$). For $\alpha=0.05$ it rejects when $x<0.05$. Its power is

$$
\pi(\theta)=\int_0^\alpha\Big[1+\theta^2\Big(\frac12-x\Big)\Big]\,\mathrm{d}x=\alpha+\frac12\alpha(1-\alpha)\theta^2,
$$
so $\pi(\pm1)=0.074$ and $\pi(\pm\frac12)=0.056$. Here a two-sided problem has a one-sided rejection region: since $\mathbb{E}_\theta X=\frac12-\frac{\theta^2}{12}$, any $\theta\ne0$ shifts the distribution to the left. The rejection region of a two-sided problem need not be two-sided.

**Example 5.4.4** Let $\boldsymbol{X}$ be a sample from $\mathrm{Ber}(\theta)$; construct an MP test of level $\alpha$ for $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta=\theta_1$ ($\theta_1>\theta_0$). With $T(\boldsymbol{x})=\sum x_i$,

$$
\frac{f(\boldsymbol{x};\theta_1)}{f(\boldsymbol{x};\theta_0)}=\left(\frac{1-\theta_1}{1-\theta_0}\right)^n\left(\frac{\theta_1(1-\theta_0)}{\theta_0(1-\theta_1)}\right)^{T(\boldsymbol{x})}.
$$
Since $1>\theta_1>\theta_0>0$, $\theta_1(1-\theta_0)>\theta_0(1-\theta_1)$, and the ratio is strictly increasing in $T$. So the MP test is (5.3): $\varphi=1$ if $T>c$, $r$ if $T=c$, $0$ if $T<c$, where

$$
\alpha_1=\sum_{k=c+1}^n\binom{n}{k}\theta_0^k(1-\theta_0)^{n-k}\le\alpha\le\sum_{k=c}^n\binom{n}{k}\theta_0^k(1-\theta_0)^{n-k},\qquad r=\frac{\alpha-\alpha_1}{\binom{n}{c}\theta_0^c(1-\theta_0)^{n-c}}.
$$
It does not depend on $\theta_1$, so by Proposition 5.4.1 it is UMP for $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta>\theta_0$, and, its power being increasing (Section 5.2.3), also for $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$.

### 5.4.4. UMP Tests in One-Parameter Exponential Families

The examples above work because the likelihood ratio is monotone in a statistic. This holds throughout one-parameter exponential families ([3.2.2](/3.2.2)), where the recipe of Section 5.4.3 is valid for one-dimensional parameters ranging over $\mathbb{R}$ or an interval.

**Theorem 5.4.2** Let $\boldsymbol{X}$ be a sample from a one-parameter exponential family

$$
f(x;\theta)=C(\theta)\mathrm{e}^{Q(\theta)T(x)}h(x),\qquad\theta\in\Theta\subseteq\mathbb{R},
$$
with $Q$ strictly increasing and $h$ not depending on $\theta$, and let $V(\boldsymbol{x})=\sum_{i=1}^nT(x_i)$.

1. For $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$, the test
   $$
   \varphi(\boldsymbol{x})=\begin{cases}1, & V(\boldsymbol{x})>C,\\ r, & V(\boldsymbol{x})=C,\\ 0, & V(\boldsymbol{x})<C,\end{cases}\qquad \mathbb{P}_{\theta_0}(V>C)+r\,\mathbb{P}_{\theta_0}(V=C)=\alpha,
   $$
   is UMP of level $\alpha$.
2. For $H_0\colon\theta\ge\theta_0$ vs. $H_1\colon\theta<\theta_0$, the test with $\varphi=1$ if $V<C$, $r$ if $V=C$, $0$ if $V>C$ and $\mathbb{P}_{\theta_0}(V<C)+r\,\mathbb{P}_{\theta_0}(V=C)=\alpha$ is UMP of level $\alpha$.

**Proof** We prove part 1; part 2 is symmetric. For $\theta'<\theta''$,

$$
\frac{f(\boldsymbol{x};\theta'')}{f(\boldsymbol{x};\theta')}=\left(\frac{C(\theta'')}{C(\theta')}\right)^n\exp\big\{\big(Q(\theta'')-Q(\theta')\big)V(\boldsymbol{x})\big\}
$$
is strictly increasing in $V(\boldsymbol{x})$, because $Q(\theta'')>Q(\theta')$. Hence a test of the form "reject if $V>C$, randomize if $V=C$" is of the form (5.4) for testing $\theta'$ against $\theta''$, and by part 2 of Theorem 5.4.1 it is MP at its own size $\mathbb{E}_{\theta'}\varphi$.

Taking $\theta'=\theta_0$: $\varphi$ is MP of level $\alpha$ against every $\theta''>\theta_0$ and does not depend on $\theta''$, so by Proposition 5.4.1 it is UMP for $\theta=\theta_0$ vs. $\theta>\theta_0$.

Monotonicity of the power: for any $\theta'<\theta''$, $\varphi$ is MP of level $\alpha'=\pi_\varphi(\theta')$ for $\theta'$ against $\theta''$, so by Corollary 5.4.1 (applied with the constant test $\alpha'$), $\pi_\varphi(\theta'')\ge\alpha'=\pi_\varphi(\theta')$. Thus $\pi_\varphi$ is nondecreasing and $\pi_\varphi(\theta)\le\pi_\varphi(\theta_0)=\alpha$ for $\theta\le\theta_0$, so $\varphi$ has level $\alpha$ for the composite null. Finally, any level-$\alpha$ test of $\theta\le\theta_0$ is a level-$\alpha$ test of $\theta=\theta_0$, and $\varphi$ is at least as powerful as it at every $\theta>\theta_0$. $\square$

The power curve of the test in part 1 increases through $\alpha$ at $\theta_0$; that of part 2 decreases through $\alpha$ at $\theta_0$.

**Example 5.4.5 (Binomial case.)** For $\mathrm{Ber}(\theta)$, $f(x;\theta)=(1-\theta)\exp\{x\log\frac{\theta}{1-\theta}\}$, so $T(x)=x$, $Q(\theta)=\log\frac{\theta}{1-\theta}$ is strictly increasing, and $V=\sum X_i\sim\mathrm{Bin}(n,\theta)$. The UMP test of $\theta\le\theta_0$ vs. $\theta>\theta_0$ is (5.3); to use binomial tables, write its size condition as $\mathbb{P}_{\theta_0}(V\le C)-\gamma\,\mathbb{P}_{\theta_0}(V=C)=1-\alpha$, with power $\pi(\theta)=1-\mathbb{P}_\theta(V\le C)+\gamma\,\mathbb{P}_\theta(V=C)$. For $n=25$, $\theta_0=0.125$, $\alpha=0.05$: $\mathbb{P}_{0.125}(V\le6)=0.9703$ is the first value above $0.95$, and $\mathbb{P}_{0.125}(V=6)=0.0534$, so

$$
C=6,\qquad\gamma=\frac{0.9703-0.95}{0.0534}=0.38.
$$
The power is $\pi(0.1875)=0.230$, $\pi(0.25)=0.508$, $\pi(0.375)=0.909$. If $V=7$ is observed, the $p$-value is $\mathbb{P}_{0.125}(V\ge7)=1-0.9703=0.030$: $H_0$ is rejected at level $0.05$.

**Example 5.4.6 (Normal mean.)** For $\mathcal{N}(\theta,\sigma^2)$ with $\sigma^2$ known,

$$
f(x;\theta)=\frac{1}{\sqrt{2\pi}\sigma}\mathrm{e}^{-\theta^2/(2\sigma^2)}\,\mathrm{e}^{\theta x/\sigma^2}\,\mathrm{e}^{-x^2/(2\sigma^2)},
$$
so $T(x)=x$ and $Q(\theta)=\theta/\sigma^2$ is strictly increasing. The UMP test of $\theta\le\theta_0$ vs. $\theta>\theta_0$ rejects when $\sum x_i>C$ ($\gamma=0$), and $\alpha=\mathbb{P}_{\theta_0}\big(\sqrt{n}(\bar X-\theta_0)/\sigma>(C-n\theta_0)/(\sigma\sqrt{n})\big)$ gives $C=n\theta_0+z_\alpha\sigma\sqrt{n}$, i.e. the one-sided Z-test $\sqrt{n}(\bar x-\theta_0)/\sigma>z_\alpha$, with power $\pi(\theta)=1-\Phi\big(z_\alpha+\sqrt{n}(\theta_0-\theta)/\sigma\big)$. The one-sided Z-test of Section 5.2.1 is therefore optimal.

For the interval problem of Example 5.1.4 a UMP test also exists.

**Theorem 5.4.3** In the setting of Theorem 5.4.2, for $H_0\colon\theta\le\theta_1$ or $\theta\ge\theta_2$ vs. $H_1\colon\theta_1<\theta<\theta_2$, the test

$$
\varphi(\boldsymbol{x})=\begin{cases}1, & C_1<V(\boldsymbol{x})<C_2,\\ r_i, & V(\boldsymbol{x})=C_i\ (i=1,2),\\ 0, & \text{otherwise},\end{cases}
$$
with constants $C_1,C_2$ and $r_1,r_2\in[0,1]$ determined by $\mathbb{E}_{\theta_1}\varphi(\boldsymbol{X})=\mathbb{E}_{\theta_2}\varphi(\boldsymbol{X})=\alpha$, is UMP of level $\alpha$.

Its power curve has a single peak inside $(\theta_1,\theta_2)$ and equals $\alpha$ at $\theta_1$ and $\theta_2$.

**Example 5.4.7** For $\mathcal{N}(\theta,\sigma^2)$ with $\sigma$ known, the UMP test of $\theta\le\theta_1$ or $\theta\ge\theta_2$ vs. $\theta_1<\theta<\theta_2$ rejects when $C_1\le\sum x_i\le C_2$, where, since $\sum X_i\sim\mathcal{N}(n\theta,n\sigma^2)$,

$$
\Phi\left(\frac{C_2-n\theta_i}{\sigma\sqrt{n}}\right)-\Phi\left(\frac{C_1-n\theta_i}{\sigma\sqrt{n}}\right)=\alpha,\quad i=1,2,
$$
and the power is $\pi(\theta)=\Phi\big((C_2-n\theta)/(\sigma\sqrt{n})\big)-\Phi\big((C_1-n\theta)/(\sigma\sqrt{n})\big)$. Take $n=25$, $\theta_1=1$, $\theta_2=3$, $\sigma=1$, $\alpha=0.01$. The two equations read

$$
\Phi\Big(\frac{C_2-25}{5}\Big)-\Phi\Big(\frac{C_1-25}{5}\Big)=\Phi\Big(\frac{C_2-75}{5}\Big)-\Phi\Big(\frac{C_1-75}{5}\Big)=0.01,
$$
and by symmetry they hold when $C_1+C_2=100$. With $C_1=C$, $\Phi\big((75-C)/5\big)-\Phi\big((C-25)/5\big)=0.01$ gives $C=36.6$. So $H_0$ is rejected when $36.6\le\sum x_i\le63.4$; the power is $\pi(1.5)=\pi(2.5)=0.569$ and $\pi(2)=0.992$.

For two-sided problems such as $\theta=\theta_0$ vs. $\theta\ne\theta_0$ there is in general no UMP test (Example 5.4.2), and the class of competitors has to be restricted. Corollary 5.4.1 suggests a natural restriction: a sensible test should reject with probability at least $\alpha$ whenever $H_1$ is true.

**Definition 5.4.2 (Unbiased Test)** A test $\varphi$ of level $\alpha$ is an **unbiased test** if $\pi_\varphi(\theta)\le\alpha$ for all $\theta\in\Theta_0$ and $\pi_\varphi(\theta)\ge\alpha$ for all $\theta\in\Theta_1$. A test that is uniformly most powerful among all unbiased tests of level $\alpha$ is a **uniformly most powerful unbiased test** (UMPU test).

**Remark 5.4.3** By Corollary 5.4.1, a UMP test is unbiased. The one-sided region $D_2$ used for a two-sided problem (Remark 5.2.2) is biased: its power is below $\alpha$ on one side. For one-parameter exponential families the two-sided problem $\theta=\theta_0$ vs. $\theta\ne\theta_0$ has a UMPU test that rejects when $V<C_1$ or $V>C_2$; the two-sided Z-test, and (by an extension to families with nuisance parameters) the two-sided $t$-test, are UMPU.

The essential property in the proof of Theorem 5.4.2 is the monotonicity of the likelihood ratio, and the theorem extends to all families with this property.

**Definition 5.4.3 (Monotone Likelihood Ratio)** A family $\{f(\boldsymbol{x};\theta)\colon\theta\in\Theta\subseteq\mathbb{R}\}$ has **monotone likelihood ratio** in a statistic $T(\boldsymbol{x})$ if for all $\theta'<\theta''$ the ratio $f(\boldsymbol{x};\theta'')/f(\boldsymbol{x};\theta')$ is a nondecreasing function of $T(\boldsymbol{x})$ on the set where at least one of the two densities is positive.

**Theorem 5.4.4 (Karlin–Rubin Theorem)** If the family has monotone likelihood ratio in $T$, then for $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$ the test that rejects when $T>C$ and randomizes with probability $r$ when $T=C$, with $\mathbb{P}_{\theta_0}(T>C)+r\,\mathbb{P}_{\theta_0}(T=C)=\alpha$, is UMP of level $\alpha$, and its power function is nondecreasing.

The proof is that of Theorem 5.4.2. One-parameter exponential families with $Q$ increasing have monotone likelihood ratio in $V$; so does the family $\mathrm{U}(0,\theta)$, in $\max_iX_i$, which is not an exponential family.

## 5.5. Hypothesis Testing and Confidence Intervals

Tests and confidence regions can be constructed from each other: a $1-\alpha$ **confidence interval** consists of the parameter values that a level-$\alpha$ test does not reject.

### 5.5.1. Confidence Intervals from Tests

Let $\boldsymbol{X}$ be a sample from $\{f(x;\theta)\colon\theta\in\Theta\}$ with $\theta$ real. To construct a $1-\alpha$ confidence interval for $\theta$, consider $H_0\colon\theta=\theta_0$ vs. $H_1\colon\theta\ne\theta_0$ and a rejection region $D$ of level $\alpha$, so that $\mathbb{P}_{\theta_0}(D^{\mathsf c})=1-\alpha$. Solving the inequality that defines the acceptance region $D^{\mathsf c}$ for $\theta_0$ gives $\hat\theta_1(\boldsymbol{X})\le\theta_0\le\hat\theta_2(\boldsymbol{X})$; replacing $\theta_0$ by $\theta$, $[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ is a $1-\alpha$ confidence interval. Upper confidence limits are obtained in the same way from $H_0\colon\theta\ge\theta_0$ vs. $H_1\colon\theta<\theta_0$, and lower confidence limits from $H_0\colon\theta\le\theta_0$ vs. $H_1\colon\theta>\theta_0$.

**Theorem 5.5.1** Let $\boldsymbol{X}$ be a sample from $f(x;\theta)$, $\theta\in\Theta\subseteq\mathbb{R}^k$. For each $\theta\in\Theta$, let $A(\theta)=D^{\mathsf c}(\theta)\subseteq\mathbb{R}^n$ be the acceptance region of a level-$\alpha$ test of $H_0\colon\theta^*=\theta$ vs. $H_1\colon\theta^*\ne\theta$, and for each $\boldsymbol{x}$ let $T(\boldsymbol{x})=\{\theta\in\Theta\colon\boldsymbol{x}\in A(\theta)\}$. Then $T(\boldsymbol{X})$ is a confidence region for $\theta$ with confidence level $1-\alpha$.

**Proof** For every $\theta$, $\mathbb{P}_\theta\big(\theta\in T(\boldsymbol{X})\big)=\mathbb{P}_\theta\big(\boldsymbol{X}\in A(\theta)\big)\ge1-\alpha$, with equality when the tests have size exactly $\alpha$. $\square$

**Example 5.5.1** Let $\boldsymbol{X}$ be a sample from $\mathcal{N}(\mu,\sigma^2)$ with both parameters unknown. The level-$\alpha$ $t$-test of $\mu=\mu_0$ vs. $\mu\ne\mu_0$ has acceptance region $\big\{\lvert\sqrt{n}(\bar X-\mu_0)/S\rvert\le t_{n-1,\alpha/2}\big\}$, whose probability under $\mu=\mu_0$ is $1-\alpha$. Solving for $\mu_0$ and replacing it by $\mu$ gives the confidence interval

$$
\left[\bar X-\frac{S}{\sqrt{n}}t_{n-1,\alpha/2},\ \bar X+\frac{S}{\sqrt{n}}t_{n-1,\alpha/2}\right].
$$
The acceptance region $\{\sqrt{n}(\bar X-\mu_0)/S\le t_{n-1,\alpha}\}$ of the test of $\mu\le\mu_0$ vs. $\mu>\mu_0$ gives the lower confidence limit $\bar X-St_{n-1,\alpha}/\sqrt{n}$, and similarly the upper limit is $\bar X+St_{n-1,\alpha}/\sqrt{n}$. The $\chi^2$ tests of Section 5.2.2 give, in the same way, the interval $\big[(n-1)S^2/\chi^2_{n-1,\alpha/2},\ (n-1)S^2/\chi^2_{n-1,1-\alpha/2}\big]$ for $\sigma^2$ and the corresponding one-sided limits.

### 5.5.2. Tests from Confidence Intervals

**Proposition 5.5.1** Let $\alpha\in(0,1)$.

1. If $[\hat\theta_1(\boldsymbol{X}),\hat\theta_2(\boldsymbol{X})]$ is a $1-\alpha$ confidence interval for $\theta$, then the test that rejects $H_0\colon\theta=\theta_0$ in favor of $\theta\ne\theta_0$ when $\theta_0\notin[\hat\theta_1,\hat\theta_2]$ has level $\alpha$.
2. If $\hat\theta_U(\boldsymbol{X})$ is a $1-\alpha$ upper confidence limit, the test that rejects $H_0\colon\theta\ge\theta_0$ in favor of $\theta<\theta_0$ when $\theta_0>\hat\theta_U$ has level $\alpha$.
3. If $\hat\theta_L(\boldsymbol{X})$ is a $1-\alpha$ lower confidence limit, the test that rejects $H_0\colon\theta\le\theta_0$ in favor of $\theta>\theta_0$ when $\theta_0<\hat\theta_L$ has level $\alpha$.

**Proof** In part 1, $\mathbb{P}_{\theta_0}(\text{reject})=1-\mathbb{P}_{\theta_0}\big(\theta_0\in[\hat\theta_1,\hat\theta_2]\big)\le\alpha$. In part 2, for every $\theta\ge\theta_0$, $\mathbb{P}_\theta(\theta_0>\hat\theta_U)\le\mathbb{P}_\theta(\theta>\hat\theta_U)\le\alpha$; part 3 is symmetric. $\square$

**Example 5.5.2** For the salaries of Example 5.2.8, let $X$ and $Y$ be the salaries of professors and assistant professors. Under normality with unknown unequal variances, the normal approximation gives the $95\%$ confidence interval $[42133,\,49860]$ for $\mu_1-\mu_2$, and Welch's method gives $[42118,\,49874]$. Since $0$ is not in the interval, $H_0\colon\mu_1-\mu_2=0$ is rejected at $\alpha=0.05$. Is the professors' mean salary more than $40000$ higher ($H_0\colon\mu_1-\mu_2\le40000$ vs. $H_1\colon\mu_1-\mu_2>40000$)? The $95\%$ Welch lower confidence limit is

$$
\bar x-\bar y-t_{r,0.05}\sqrt{s_X^2/m+s_Y^2/n}=42744>40000,
$$
so $H_0$ is rejected; correspondingly, the one-sided Welch test gives $t=3.04$ and $p=0.0013$.

## 5.6. Hypothesis Testing in Linear Models

### 5.6.1. t-Tests for Regression Coefficients

Which factors drive the price of a house? In the Ames housing data, the sale price $y$ of each of $n=1598$ houses is recorded together with $p=8$ explanatory variables (living area, lot area, number of full bathrooms, number of bedrooms, central air conditioning, pool area, basement area, year sold). The linear regression model is

$$
y_i=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}+\varepsilon_i,\quad i=1,\dots,n,\qquad\text{or}\qquad\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},
$$
where $\boldsymbol{\beta}=(\beta_0,\beta_1,\dots,\beta_p)^{\mathsf T}$, $\boldsymbol{x}_i=(1,x_{i1},\dots,x_{ip})^{\mathsf T}$, $\boldsymbol{Y}=(y_1,\dots,y_n)^{\mathsf T}$ is the random response, $X=(\boldsymbol{x}_1,\dots,\boldsymbol{x}_n)^{\mathsf T}$ is the fixed $n\times(p+1)$ design matrix (assumed of full column rank) and $\boldsymbol{\varepsilon}$ is the random error. For inference we assume $\varepsilon_1,\dots,\varepsilon_n\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$, so that the density of the data is $\prod_{i=1}^n\frac{1}{\sqrt{2\pi}\sigma}\exp\big\{-(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})^2/(2\sigma^2)\big\}$. The least squares estimator, which is also the maximum likelihood estimator, and the bias-corrected variance estimator are

$$
\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y},\qquad \hat\sigma^2=\frac{\mathrm{RSS}}{n-p-1},\qquad \mathrm{RSS}=\sum_{i=1}^n(y_i-\boldsymbol{x}_i^{\mathsf T}\hat{\boldsymbol{\beta}})^2=\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}\|_2^2.
$$
Write $c_{jj}=[(X^{\mathsf T}X)^{-1}]_{j+1,j+1}$ for the diagonal entry belonging to $\beta_j$ ($j=0,\dots,p$).

**Theorem 5.6.1** In the model above,

1. $\mathbb{E}\hat{\boldsymbol{\beta}}=\boldsymbol{\beta}$;
2. $\hat{\boldsymbol{\beta}}\sim\mathcal{N}_{p+1}\big(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1}\big)$, in particular $\hat\beta_j\sim\mathcal{N}(\beta_j,\sigma^2c_{jj})$;
3. $(n-p-1)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p-1}$;
4. $\hat{\boldsymbol{\beta}}$ and $\hat\sigma^2$ are independent.

The proof, based on the **multivariate normal distribution** and the projection onto the column space of $X$, is given in [3.3](/3.3). Consequently, for $j=0,1,\dots,p$,

$$
T_j=\frac{\hat\beta_j-\beta_j}{\hat\sigma\sqrt{c_{jj}}}\sim t_{n-p-1}.
$$
A $1-\alpha$ confidence interval for $\beta_j$ is $\big[\hat\beta_j-\hat\sigma\sqrt{c_{jj}}\,t_{n-p-1,\alpha/2},\ \hat\beta_j+\hat\sigma\sqrt{c_{jj}}\,t_{n-p-1,\alpha/2}\big]$, and one for $\sigma^2$ is $\big[(n-p-1)\hat\sigma^2/\chi^2_{n-p-1,\alpha/2},\ (n-p-1)\hat\sigma^2/\chi^2_{n-p-1,1-\alpha/2}\big]$. For two coefficients jointly, the rectangle formed by the two intervals with $t_{n-p-1,\alpha/4}$ in place of $t_{n-p-1,\alpha/2}$ covers $(\beta_1,\beta_2)$ with probability at least $1-\alpha$ (by the Bonferroni inequality).

To test whether the $j$-th variable has an effect, $H_{0j}\colon\beta_j=0$ vs. $H_{1j}\colon\beta_j\ne0$, we reject when $\lvert\hat\beta_j\rvert$ is large relative to its standard error. Under $H_{0j}$, $T_j=\hat\beta_j/(\hat\sigma\sqrt{c_{jj}})\sim t_{n-p-1}$, so the level-$\alpha$ test is

$$
\varphi=\begin{cases}1, & \lvert\hat\beta_j\rvert/(\hat\sigma\sqrt{c_{jj}})>t_{n-p-1,\alpha/2},\\ 0, & \text{otherwise},\end{cases}
$$
with $p$-value $\mathbb{P}(\lvert t_{n-p-1}\rvert\ge\lvert t_j\rvert)$, where $t_j$ is the observed value of $T_j$.

**Example 5.6.1** For the Ames data the fitted model gives ($\hat\sigma=39210$ on $1589$ degrees of freedom):

| | estimate | $t_j$ | $p$-value |
|---|---|---|---|
| intercept | $1.972\times10^6$ | $1.30$ | $0.192$ |
| living area | $98.22$ | $31.53$ | $<10^{-15}$ |
| lot area | $0.877$ | $4.70$ | $2.9\times10^{-6}$ |
| full bathrooms | $1.791\times10^4$ | $7.74$ | $1.7\times10^{-14}$ |
| bedrooms | $-2.520\times10^4$ | $-17.53$ | $<10^{-15}$ |
| central air | $2.427\times10^4$ | $6.35$ | $2.8\times10^{-10}$ |
| pool area | $-40.86$ | $-1.63$ | $0.103$ |
| basement area | $69.27$ | $25.82$ | $<10^{-15}$ |
| year sold | $-995.4$ | $-1.32$ | $0.186$ |

At $\alpha=0.05$, $H_{0j}$ is rejected for living area, lot area, full bathrooms, bedrooms, central air and basement area, and not for the intercept, pool area and year sold. (The negative coefficient of bedrooms is an effect given the other variables: at fixed living area, more bedrooms mean smaller rooms.)

### 5.6.2. Likelihood Ratio Tests in Linear Regression

The likelihood is $L(\boldsymbol{\beta},\sigma^2)=(2\pi\sigma^2)^{-n/2}\exp\big\{-\|\boldsymbol{Y}-X\boldsymbol{\beta}\|_2^2/(2\sigma^2)\big\}$ on $\Theta=\{(\boldsymbol{\beta},\sigma^2)\}\subseteq\mathbb{R}^{p+2}$. Over $\Theta$, $\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$, $\hat\sigma^2_{\mathrm{MLE}}=\frac1n\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2$, and the maximum is $(2\pi\hat\sigma^2_{\mathrm{MLE}})^{-n/2}\mathrm{e}^{-n/2}$.

Consider first a single coefficient. Under $H_{0j}\colon\beta_j=0$, $\Theta_0\subseteq\mathbb{R}^{p+1}$. Let $\boldsymbol{\beta}_{-j}$ be $\boldsymbol{\beta}$ without $\beta_j$ and $X_{-j}$ the design matrix without the corresponding column; then $\hat{\boldsymbol{\beta}}_{\mathrm{MLE},0}=(X_{-j}^{\mathsf T}X_{-j})^{-1}X_{-j}^{\mathsf T}\boldsymbol{Y}$, $\hat\sigma^2_{\mathrm{MLE},0}=\frac1n\|\boldsymbol{Y}-X_{-j}\hat{\boldsymbol{\beta}}_{\mathrm{MLE},0}\|_2^2$, and

$$
\lambda=\left(\frac{\hat\sigma^2_{\mathrm{MLE}}}{\hat\sigma^2_{\mathrm{MLE},0}}\right)^{n/2}=\left(\frac{\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2}{\|\boldsymbol{Y}-X_{-j}\hat{\boldsymbol{\beta}}_{\mathrm{MLE},0}\|_2^2}\right)^{n/2}.
$$
By Theorem 5.3.1 (dimensions $p+2$ and $p+1$), under $H_{0j}$ and as $n\to\infty$, $-2\log\lambda=n\log\|\boldsymbol{Y}-X_{-j}\hat{\boldsymbol{\beta}}_{\mathrm{MLE},0}\|_2^2-n\log\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2\xrightarrow{d}\chi^2_1$, and $\{-2\log\lambda>\chi^2_{1,\alpha}\}$ has approximate level $\alpha$.

**Proposition 5.6.1** $-2\log\lambda=n\log\big(1+T_j^2/(n-p-1)\big)$, where $T_j=\hat\beta_j/(\hat\sigma\sqrt{c_{jj}})$. Hence the exact likelihood ratio test of $H_{0j}$ is the $t$-test of Section 5.6.1.

**Proof** The increase of the residual sum of squares when the $j$-th column is removed is $\mathrm{RSS}_0-\mathrm{RSS}=\hat\beta_j^2/c_{jj}$ (a standard identity for nested least squares fits, proved in [3.3](/3.3)). Therefore $\mathrm{RSS}_0/\mathrm{RSS}=1+\hat\beta_j^2/(c_{jj}\mathrm{RSS})=1+T_j^2/(n-p-1)$, and $-2\log\lambda=n\log(\mathrm{RSS}_0/\mathrm{RSS})$. $\square$

Next we test the overall significance: is the linear model useful at all, $H_0\colon\beta_1=\dots=\beta_p=0$ vs. $H_1$: some $\beta_j\ne0$? Now $\Theta_0=\{(\beta_0,\sigma^2)\}$ has dimension $2$, $\hat\beta_0=\bar y$, $\hat\sigma^2=\frac1n\|\boldsymbol{Y}-\bar y\boldsymbol{1}\|_2^2$, and

$$
\lambda=\left(\frac{\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2}{\|\boldsymbol{Y}-\bar y\boldsymbol{1}\|_2^2}\right)^{n/2},\qquad -2\log\lambda\xrightarrow{d}\chi^2_p.
$$
An exact test is available. The sum of squares decomposes as

$$
\|\boldsymbol{Y}-\bar y\boldsymbol{1}\|_2^2=\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2+\|X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}-\bar y\boldsymbol{1}\|_2^2,
$$
and under $H_0$, $Z_1=\|X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}-\bar y\boldsymbol{1}\|_2^2/\sigma^2\sim\chi^2_p$ and $Z_2=\|\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}_{\mathrm{MLE}}\|_2^2/\sigma^2\sim\chi^2_{n-p-1}$ are independent, so

$$
F=\frac{Z_1/p}{Z_2/(n-p-1)}\sim F_{p,n-p-1},\qquad \lambda^{2/n}=\left(1+\frac{p}{n-p-1}F\right)^{-1}.
$$
The likelihood ratio test rejects when $F>F_{p,n-p-1,\alpha}$. For the Ames data $F=621.4$ on $8$ and $1589$ degrees of freedom, $p<10^{-15}$, and the coefficient of determination is $R^2=0.758$.

### 5.6.3. Two-Way Analysis of Variance

**Example 5.6.2** A firm considers buying a large number of machines from one of $I$ brands. Each of $J$ workers uses each brand for one day, and the output $Y_{ij}$ of brand $i$ with worker $j$ is modeled as

$$
Y_{ij}=\mu+\alpha_i+\beta_j+e_{ij},\qquad\sum_{i=1}^I\alpha_i=0,\quad\sum_{j=1}^J\beta_j=0,\qquad e_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
with $I,J\ge2$: $\mu$ is the grand mean, $\alpha_i$ the row effect (brand), $\beta_j$ the column effect (worker), and the effects are additive. The two factors have $I$ and $J$ levels, and the analysis of this layout is the two-way *analysis of variance* (ANOVA). We want to estimate $\mu$, $\alpha_i$, $\beta_j$, $\sigma^2$ and to test for row effects, $H_{0,A}\colon\alpha_1=\dots=\alpha_I=0$ (do the brands differ?), and for column effects, $H_{0,B}\colon\beta_1=\dots=\beta_J=0$ (do the workers differ?).

The likelihood is $L(\boldsymbol{y};\mu,\boldsymbol{\alpha},\boldsymbol{\beta},\sigma^2)=(2\pi\sigma^2)^{-IJ/2}\exp\big[-\frac{1}{2\sigma^2}\sum_i\sum_j(y_{ij}-\mu-\alpha_i-\beta_j)^2\big]$, so for each $\sigma^2$ it is maximized by minimizing $\mathcal{S}(\mu,\boldsymbol{\alpha},\boldsymbol{\beta})=\sum_i\sum_j(y_{ij}-\mu-\alpha_i-\beta_j)^2$. Write $\bar y_{i\cdot}=\frac1J\sum_jy_{ij}$, $\bar y_{\cdot j}=\frac1I\sum_iy_{ij}$, $\bar y_{\cdot\cdot}=\frac{1}{IJ}\sum_i\sum_jy_{ij}$.

**Lemma 5.6.1** The unique minimizers of $\mathcal{S}$ under the constraints (the least squares estimators) are

$$
\hat\mu=\bar y_{\cdot\cdot},\qquad\hat\alpha_i=\bar y_{i\cdot}-\bar y_{\cdot\cdot},\qquad\hat\beta_j=\bar y_{\cdot j}-\bar y_{\cdot\cdot}.
$$

Hence the maximum likelihood estimator of $\sigma^2$ is $\hat\sigma^2=\frac{1}{IJ}\sum_i\sum_j(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2$. Under $H_{0,A}$ the same argument gives $\hat\mu_A=\bar y_{\cdot\cdot}$, $\hat\beta_{j,A}=\bar y_{\cdot j}-\bar y_{\cdot\cdot}$ and $\hat\sigma_A^2=\frac{1}{IJ}\sum_i\sum_j(y_{ij}-\bar y_{\cdot j})^2$. Both maximal likelihoods have the form $(2\pi\hat\sigma^2)^{-IJ/2}\mathrm{e}^{-IJ/2}$, so

$$
\lambda=\left(\hat\sigma^2/\hat\sigma_A^2\right)^{IJ/2},
$$
and $\lambda<C$ if and only if $\hat\sigma_A^2/\hat\sigma^2>C_0$. Define the sums of squares

$$
\begin{aligned}
\mathrm{SS}_e&=\sum_i\sum_j(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2=IJ\hat\sigma^2, & \mathrm{SS}_A&=J\sum_i(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2,\\
\mathrm{SS}_B&=I\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2, & \mathrm{SS}_T&=\sum_i\sum_j(y_{ij}-\bar y_{\cdot\cdot})^2.
\end{aligned}
$$

**Lemma 5.6.2** $IJ\hat\sigma_A^2=\mathrm{SS}_e+\mathrm{SS}_A$, and $\mathrm{SS}_T=\mathrm{SS}_e+\mathrm{SS}_A+\mathrm{SS}_B$. Moreover $\mathrm{SS}_A=J\sum_i\bar y_{i\cdot}^2-IJ\bar y_{\cdot\cdot}^2$, $\mathrm{SS}_B=I\sum_j\bar y_{\cdot j}^2-IJ\bar y_{\cdot\cdot}^2$ and $\mathrm{SS}_T=\sum_i\sum_jy_{ij}^2-IJ\bar y_{\cdot\cdot}^2$.

**Proof** Write $y_{ij}-\bar y_{\cdot j}=(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})+(\bar y_{i\cdot}-\bar y_{\cdot\cdot})$; the cross term vanishes because $\sum_j(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})=0$ for each $i$. The decomposition of $\mathrm{SS}_T$ is proved in the same way by splitting $y_{ij}-\bar y_{\cdot\cdot}$ into three parts whose pairwise cross sums vanish, and the computational formulas follow by expanding the squares. $\square$

By Lemma 5.6.2, $\hat\sigma_A^2/\hat\sigma^2=1+\mathrm{SS}_A/\mathrm{SS}_e$, so the likelihood ratio test rejects $H_{0,A}$ when $\mathrm{SS}_A/\mathrm{SS}_e>C_1$.

**Theorem 5.6.2** Replace the observations by the random variables $Y_{ij}$. Then $\mathrm{SS}_e/\sigma^2\sim\chi^2_{(I-1)(J-1)}$, and $\mathrm{SS}_e$, $\mathrm{SS}_A$, $\mathrm{SS}_B$ are independent. Under $H_{0,A}$, $\mathrm{SS}_A/\sigma^2\sim\chi^2_{I-1}$, so

$$
F_A=\frac{\mathrm{SS}_A/(I-1)}{\mathrm{SS}_e/[(I-1)(J-1)]}\sim F_{I-1,(I-1)(J-1)};
$$
similarly, under $H_{0,B}$, $F_B=\dfrac{\mathrm{SS}_B/(J-1)}{\mathrm{SS}_e/[(I-1)(J-1)]}\sim F_{J-1,(I-1)(J-1)}$.

The level-$\alpha$ tests reject $H_{0,A}$ when $F_A>F_{I-1,(I-1)(J-1),\alpha}$ and $H_{0,B}$ when $F_B>F_{J-1,(I-1)(J-1),\alpha}$. The computations are arranged in the ANOVA table:

| Source | Sum of squares | Degrees of freedom | Mean square |
|---|---|---|---|
| rows | $\mathrm{SS}_A=J\sum_i\hat\alpha_i^2$ | $I-1$ | $\mathrm{MS}_A=\mathrm{SS}_A/(I-1)$ |
| columns | $\mathrm{SS}_B=I\sum_j\hat\beta_j^2$ | $J-1$ | $\mathrm{MS}_B=\mathrm{SS}_B/(J-1)$ |
| residual | $\mathrm{SS}_e$ | $(I-1)(J-1)$ | $\mathrm{MS}_e=\mathrm{SS}_e/[(I-1)(J-1)]$ |
| total | $\mathrm{SS}_T$ | $IJ-1$ | |

and $F_A=\mathrm{MS}_A/\mathrm{MS}_e$, $F_B=\mathrm{MS}_B/\mathrm{MS}_e$.

**Remark 5.6.1** Here $\Theta$ has dimension $I+J$ ($\mu$, $I-1$ free $\alpha_i$, $J-1$ free $\beta_j$, $\sigma^2$) and $\Theta_0$ under $H_{0,A}$ has dimension $J+1$, so Theorem 5.3.1 would suggest $-2\log\lambda\approx\chi^2_{I-1}$. With one observation per cell, however, the number of parameters grows with $J$, and the regularity conditions fail: since $-2\log\lambda=IJ\log(1+\mathrm{SS}_A/\mathrm{SS}_e)$ and $\mathrm{SS}_e/(IJ)\to\frac{I-1}{I}\sigma^2$ as $J\to\infty$, the limit under $H_{0,A}$ is $\frac{I}{I-1}\chi^2_{I-1}$, not $\chi^2_{I-1}$. The exact $F$-test of Theorem 5.6.2 should be used.

For the data below (three brands, four workers),

| brand | worker 1 | worker 2 | worker 3 | worker 4 | $\bar y_{i\cdot}$ |
|---|---|---|---|---|---|
| 1 | 3 | 7 | 5 | 4 | 19/4 |
| 2 | −1 | 2 | 0 | 2 | 3/4 |
| 3 | 1 | 2 | 4 | 0 | 7/4 |
| $\bar y_{\cdot j}$ | 1 | 11/3 | 3 | 2 | $\bar y_{\cdot\cdot}=29/12$ |

we get $\hat\mu=29/12=2.417$, $\hat\alpha_1=7/3$, $\hat\alpha_2=-5/3$, $\hat\alpha_3=-2/3$, $\hat\beta_1=-17/12$, $\hat\beta_2=5/4$, $\hat\beta_3=7/12$, $\hat\beta_4=-5/12$, and

$$
\mathrm{SS}_A=\frac{104}{3}=34.667,\qquad\mathrm{SS}_B=\frac{147}{12}=12.25,\qquad\mathrm{SS}_T=\frac{707}{12}=58.917,\qquad\mathrm{SS}_e=\mathrm{SS}_T-\mathrm{SS}_A-\mathrm{SS}_B=12.
$$
The unbiased estimate of $\sigma^2$ is $\mathrm{SS}_e/[(I-1)(J-1)]=2$, whereas the maximum likelihood estimate is $12/12=1$. Further,

$$
F_A=\frac{(104/3)/2}{12/6}=\frac{26}{3}=8.667>F_{2,6,0.05}=5.143,\qquad F_B=\frac{(147/12)/3}{12/6}=\frac{147}{72}=2.042<F_{3,6,0.05}=4.757,
$$
so the hypothesis of no brand effect is rejected and that of no worker effect is not. The same arguments extend to two-way layouts with several observations per cell.

## Summary {#summary}

| Situation | Statistic and null distribution | Section |
|---|---|---|
| normal mean, $\sigma^2$ known | $Z=\sqrt{n}(\bar X-\mu_0)/\sigma\sim\mathcal{N}(0,1)$ | 5.2.1 |
| normal mean, $\sigma^2$ unknown | $T=\sqrt{n}(\bar X-\mu_0)/S\sim t_{n-1}$ | 5.2.1 |
| normal variance | $(n-1)S^2/\sigma_0^2\sim\chi^2_{n-1}$ ($nS_\mu^2/\sigma_0^2\sim\chi^2_n$ if $\mu$ known) | 5.2.2 |
| Bernoulli, Poisson | randomized tests on $\sum X_i$; large $n$: $U$, $U_0\overset{\cdot}{\sim}\mathcal{N}(0,1)$ | 5.2.3, 5.2.6 |
| two means, equal variances | $T=(\bar X-\bar Y-\mu_0)/(S_p\sqrt{1/m+1/n})\sim t_{m+n-2}$ | 5.2.4 |
| two means, unequal variances | Welch $T_*\overset{\cdot}{\sim}t_r$; large samples $U^*\overset{\cdot}{\sim}\mathcal{N}(0,1)$ | 5.2.4, 5.2.6 |
| paired data | one-sample $t$-test on the differences | 5.2.4 |
| two variances | $F=S_Y^2/S_X^2\sim F_{n-1,m-1}$ | 5.2.5 |
| general | likelihood ratio, $-2\log\lambda\overset{\cdot}{\sim}\chi^2_{k-s}$ | 5.3 |
| regression coefficient, whole model | $T_j\sim t_{n-p-1}$; $F\sim F_{p,n-p-1}$ | 5.6 |

- The Neyman–Pearson framework controls the type I error at level $\alpha$ and maximizes power; rejections are reliable, acceptances are not, so $H_0$ must be chosen with care. The $p$-value is the smallest level at which the data reject $H_0$.
- Likelihood ratio tests are the general-purpose method; all classical normal-theory tests are likelihood ratio tests, and Wilks' theorem gives large-sample approximations.
- The Neyman–Pearson lemma gives MP tests for simple hypotheses; in families with monotone likelihood ratio (in particular one-parameter exponential families) one-sided problems have UMP tests, while two-sided problems in general do not, and unbiased tests are used instead.
- A $1-\alpha$ confidence region is the set of parameter values not rejected by level-$\alpha$ tests, and conversely.
