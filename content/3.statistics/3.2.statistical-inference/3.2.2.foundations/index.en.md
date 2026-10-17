---
title: Fundamentals of Statistics
description: Sampling distributions of normal samples, the chi-square, t and F distributions, limiting distributions and Slutsky's theorem; exponential families and their natural form; sufficient, minimal sufficient and complete statistics, the factorization theorem and Basu's theorem.
---

A statistic is a random variable, and every statement about the quality of an inference method (how often an estimate is close to the truth, how often a test errs) is a statement about the distribution of a statistic. This chapter develops three tools used throughout the rest of the course. The first is the sampling distribution: for normal samples the sample mean and the sample variance are independent and have explicit distributions, which leads to the $\chi^2$, $t$ and $F$ distributions behind most confidence intervals and tests; when exact distributions are out of reach, limiting distributions and Slutsky's theorem take their place. The second is the exponential family, a class containing the normal, binomial, Poisson and gamma distributions, for which most optimality problems of the later chapters have clean answers. The third is the pair of notions sufficiency and completeness, which say when a statistic loses no information about the parameter and when it is rich enough to determine unbiased estimators uniquely; they underlie the UMVUE theory of [3.2.3](/3.2.3) and the optimal tests of [3.2.5](/3.2.5). We use the vocabulary of [3.2.1](/3.2.1) and the limit theorems of probability theory ([3.1.12](/3.1.12)–[3.1.14](/3.1.14)).

## 2.1. Sampling Distributions

### 2.1.1. Sampling Distributions and Limiting Distributions

The sample is a random vector, so a statistic, being a function of it, is a random variable or random vector.

**Definition 2.1.1 (Sampling Distribution)** The distribution of a statistic is called its **sampling distribution**.

Sampling distributions are used to study the properties of statistics and to evaluate inference methods; finding them is one of the basic problems of mathematical statistics. There are two kinds. The exact sampling distribution, for a known form of the population distribution, is the distribution for a fixed sample size $n$. It is often too complicated to obtain, and most of the known results concern normal populations. The limiting distribution is the limit of the sampling distribution as $n\to\infty$. It is easier to obtain, its form is often simple, and it approximates the exact distribution well once $n$ is large.

Suppose $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$, a model for the weight of an object, the height and weight of people, the return of a stock or a log-transformed income. Natural estimates of $a$ and $\sigma^2$ are $\bar X$ and $S^2$. How good are they, that is, what are $\mathbb{E}[(\bar X-a)^2]$ and $\mathbb{E}[(S^2-\sigma^2)^2]$? How do we build confidence intervals for $a$ and $\sigma^2$? Both questions require the distributions of $\bar X$ and $S^2$.

### 2.1.2. Linear Functions of Normal Variables

**Theorem 2.1.1** Let $X_1,\dots,X_n$ be independent with $X_k\sim\mathcal{N}(a_k,\sigma_k^2)$, $k=1,\dots,n$, let $c_1,\dots,c_n$ be constants and $T=\sum_{k=1}^nc_kX_k$. Then $T\sim\mathcal{N}(\mu,\tau^2)$ with

$$
\mu=\sum_{k=1}^nc_ka_k,\qquad\tau^2=\sum_{k=1}^nc_k^2\sigma_k^2.
$$

**Proof** We use **characteristic functions**. Since $X_k\sim\mathcal{N}(a_k,\sigma_k^2)$, $\varphi_k(t)=\mathbb{E}[\mathrm{e}^{\mathrm{i}tX_k}]=\mathrm{e}^{\mathrm{i}a_kt-\frac12\sigma_k^2t^2}$. By independence,

$$
\varphi_T(t)=\mathbb{E}\left[\prod_{k=1}^n\mathrm{e}^{\mathrm{i}tc_kX_k}\right]=\prod_{k=1}^n\varphi_k(c_kt)=\prod_{k=1}^n\mathrm{e}^{\mathrm{i}c_ka_kt-\frac12c_k^2\sigma_k^2t^2}=\exp\left\{\mathrm{i}t\sum_{k=1}^nc_ka_k-\frac12t^2\sum_{k=1}^nc_k^2\sigma_k^2\right\},
$$
which is the characteristic function of $\mathcal{N}(\mu,\tau^2)$. The characteristic function determines the distribution. $\square$

In words, a linear combination of independent normal random variables is normal; its mean and variance are those computed by linearity, and the content of the theorem is that the distribution stays normal.

**Corollary 2.1.1** In Theorem 2.1.1, if $a_1=\dots=a_n=a$ and $\sigma_1^2=\dots=\sigma_n^2=\sigma^2$, then

$$
T\sim\mathcal{N}\left(a\sum_{k=1}^nc_k,\ \sigma^2\sum_{k=1}^nc_k^2\right).
$$

**Corollary 2.1.2** If $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$, then $\bar X\sim\mathcal{N}(a,\sigma^2/n)$.

**Proof** Take $c_1=\dots=c_n=1/n$ in Corollary 2.1.1. $\square$

**Theorem 2.1.2 (Linear Transformation of a Normal Sample)** Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$, $\boldsymbol{X}=(X_1,\dots,X_n)^{\mathsf T}$, let $A=(a_{ij})$ be an $n\times n$ constant matrix and $\boldsymbol{Y}=(Y_1,\dots,Y_n)^{\mathsf T}=A\boldsymbol{X}$, that is,

$$
\begin{pmatrix}Y_1\\ \vdots\\ Y_n\end{pmatrix}=\begin{pmatrix}a_{11}&\cdots&a_{1n}\\ \vdots&&\vdots\\ a_{n1}&\cdots&a_{nn}\end{pmatrix}\begin{pmatrix}X_1\\ \vdots\\ X_n\end{pmatrix}.
$$

1. Each $Y_i$ is normal, and

   $$
   \mathbb{E}[Y_i]=a\sum_{k=1}^na_{ik},\qquad\operatorname{Var}(Y_i)=\sigma^2\sum_{k=1}^na_{ik}^2,\qquad\operatorname{Cov}(Y_i,Y_j)=\sigma^2\sum_{k=1}^na_{ik}a_{jk}.
   $$
2. If $A$ is an orthogonal matrix, then $Y_1,\dots,Y_n$ are independent and $Y_i\sim\mathcal{N}(\mu_i,\sigma^2)$ with $\mu_i=a\sum_{k=1}^na_{ik}$.
3. If moreover $a=0$, then $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$.

**Proof** (1) Since $Y_i=\sum_{k=1}^na_{ik}X_k$, Corollary 2.1.1 gives $Y_i\sim\mathcal{N}\big(a\sum_ka_{ik},\ \sigma^2\sum_ka_{ik}^2\big)$, and

$$
\operatorname{Cov}(Y_i,Y_j)=\mathbb{E}[(Y_i-\mathbb{E}Y_i)(Y_j-\mathbb{E}Y_j)]=\sum_{k=1}^n\sum_{l=1}^na_{ik}a_{jl}\,\mathbb{E}[(X_k-a)(X_l-a)]=\sum_{k=1}^n\sum_{l=1}^na_{ik}a_{jl}\delta_{kl}\sigma^2=\sigma^2\sum_{k=1}^na_{ik}a_{jk},
$$
where $\delta_{kl}=1$ if $k=l$ and $0$ otherwise.

(2) The vector $\boldsymbol{Y}=A\boldsymbol{X}$ is a linear image of the normal vector $\boldsymbol{X}$, so it has a **multivariate normal distribution**, and for jointly normal variables, uncorrelated is equivalent to independent. If $A$ is orthogonal, its rows are orthonormal: $\sum_ka_{ik}^2=1$, so $\operatorname{Var}(Y_i)=\sigma^2$, and $\sum_ka_{ik}a_{jk}=0$ for $i\ne j$, so $\operatorname{Cov}(Y_i,Y_j)=0$. Hence $Y_1,\dots,Y_n$ are independent with $Y_i\sim\mathcal{N}(\mu_i,\sigma^2)$.

(3) If $a=0$ then every $\mu_i=0$. $\square$

In matrix form: $\boldsymbol{X}\sim\mathcal{N}_n(a\boldsymbol{1},\sigma^2I_n)$, hence $\boldsymbol{Y}=A\boldsymbol{X}\sim\mathcal{N}_n(aA\boldsymbol{1},\sigma^2AA^{\mathsf T})$, and $AA^{\mathsf T}=I_n$ for orthogonal $A$. A spherically symmetric normal vector stays spherically symmetric under rotations.

### 2.1.3. Sample Mean and Sample Variance of a Normal Sample

**Theorem 2.1.3** Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$ ($n\ge2$), with sample mean $\bar X$ and sample variance $S^2$. Then

1. $\bar X\sim\mathcal{N}(a,\sigma^2/n)$;
2. $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$;
3. $\bar X$ and $S^2$ are independent.

Here $\chi^2_{n-1}$ is the chi-square distribution with $n-1$ degrees of freedom, the distribution of a sum of squares of $n-1$ independent standard normal variables (Definition 2.1.2 below).

**Proof** (1) is Corollary 2.1.2. (2) The idea is to write $(n-1)S^2$ as a sum of squares of $n-1$ independent normal variables by a suitable orthogonal transformation. Let

$$
A=\begin{pmatrix}\frac1{\sqrt n}&\frac1{\sqrt n}&\cdots&\frac1{\sqrt n}\\ a_{21}&a_{22}&\cdots&a_{2n}\\ \vdots&\vdots&&\vdots\\ a_{n1}&a_{n2}&\cdots&a_{nn}\end{pmatrix}
$$
be an orthogonal matrix whose first row is $(1/\sqrt n,\dots,1/\sqrt n)$; the other rows exist by the **Gram–Schmidt process**. Let $\boldsymbol{Y}=A\boldsymbol{X}$. Then $Y_1=\frac1{\sqrt n}\sum_{i=1}^nX_i=\sqrt n\,\bar X$, and an orthogonal transformation preserves length, $\sum_{i=1}^nY_i^2=\sum_{i=1}^nX_i^2$. Therefore

$$
(n-1)S^2=\sum_{i=1}^n(X_i-\bar X)^2=\sum_{i=1}^nX_i^2-n\bar X^2=\sum_{i=1}^nY_i^2-Y_1^2=\sum_{i=2}^nY_i^2.
$$

By Theorem 2.1.2, $Y_1,\dots,Y_n$ are independent and $Y_i\sim\mathcal{N}(\mu_i,\sigma^2)$, where for $i\ge2$

$$
\mu_i=a\sum_{k=1}^na_{ik}=\sqrt n\,a\sum_{k=1}^n\frac1{\sqrt n}a_{ik}=0,
$$
because row $i$ of $A$ is orthogonal to the first row. Thus $Y_2/\sigma,\dots,Y_n/\sigma\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$ and $(n-1)S^2/\sigma^2=\sum_{i=2}^n(Y_i/\sigma)^2\sim\chi^2_{n-1}$.

(3) In the proof of (2), $S^2$ is a function of $Y_2,\dots,Y_n$ and $\bar X$ is a function of $Y_1$, and $Y_1,\dots,Y_n$ are independent. $\square$

Theorem 2.1.3 is the basis of the confidence intervals and tests for the mean and the variance of a normal population in [3.2.4](/3.2.4) and [3.2.5](/3.2.5). The independence in (3) characterizes the normal distribution: for no other population are $\bar X$ and $S^2$ independent. A simulation shows the three distributions involved.

![Histograms over 1000 simulated samples of size 100 from N(1, 4) of the sample mean, the sample variance and the t statistic, with the theoretical densities](./plots/normal-sample-simulation.py)

The right panel shows that $\sqrt n(\bar X-a)/S$ looks standard normal. We shall see two explanations: its exact distribution is $t_{n-1}$ (Corollary 2.1.4), which is close to $\mathcal{N}(0,1)$ for large $n$, and its limiting distribution is $\mathcal{N}(0,1)$ by Slutsky's theorem (Example 2.1.2).

### 2.1.4. The Chi-Square, t and F Distributions

**Definition 2.1.2 (Chi-Square Distribution)** Let $X_1,\dots,X_r\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$. The distribution of

$$
\xi=\sum_{i=1}^rX_i^2
$$
is called the **chi-square distribution** with $r$ **degrees of freedom**, written $\xi\sim\chi^2_r$. Its density is

$$
f(x)=\frac1{\Gamma(r/2)\,2^{r/2}}x^{r/2-1}\mathrm{e}^{-x/2},\qquad x>0,
$$
and $f(x)=0$ for $x\le0$.

Here $\Gamma(\alpha)=\int_0^\infty y^{\alpha-1}\mathrm{e}^{-y}\,\mathrm{d}y$ is the **gamma function**. The density can be obtained from the joint density $(2\pi)^{-r/2}\exp\{-\frac12\sum x_i^2\}$ of $X_1,\dots,X_r$ by integrating over the ball $\{\sum x_i^2\le x\}$ in spherical coordinates. Equivalently, $\chi^2_r=\Gamma(r/2,1/2)$ in the rate parametrization: the square of a standard normal variable is $\Gamma(1/2,1/2)$, and independent gamma variables with a common rate add their shape parameters. The density is supported on $(0,\infty)$; it decreases monotonically for $r=1,2$, has a single peak for $r\ge3$, and becomes more symmetric as $r$ grows (it is asymptotically normal by the **central limit theorem**). Chi-square distributions arise for the sample variance of a normal sample, for likelihood ratio statistics and for Pearson's $\chi^2$ goodness-of-fit test, and are used in confidence intervals and tests for variances.

**Definition 2.1.3 (Upper Quantile)** Let $\xi$ be a random variable with a continuous distribution and $0<\alpha<1$. A number $c$ with $\mathbb{P}(\xi>c)=\alpha$ is called the **upper $\alpha$ quantile** of the distribution. For the standard normal, $\chi^2_r$, $t_r$ and $F_{r_1,r_2}$ distributions it is denoted $z_\alpha$, $\chi^2_{r,\alpha}$, $t_{r,\alpha}$ and $F_{r_1,r_2,\alpha}$.

**Proposition 2.1.1** Let $\xi\sim\chi^2_r$.

1. The characteristic function of $\xi$ is $\varphi(t)=(1-2\mathrm{i}t)^{-r/2}$.
2. $\mathbb{E}[\xi]=r$ and $\operatorname{Var}(\xi)=2r$.
3. If $\xi_1\sim\chi^2_{r_1}$, $\xi_2\sim\chi^2_{r_2}$ are independent, then $\xi_1+\xi_2\sim\chi^2_{r_1+r_2}$; more generally, if $\xi_i\sim\chi^2_{r_i}$, $i=1,\dots,k$, are independent, then $\sum_{i=1}^k\xi_i\sim\chi^2_{r_1+\cdots+r_k}$.

**Proof** For $X\sim\mathcal{N}(0,1)$, $\mathbb{E}[\mathrm{e}^{\mathrm{i}tX^2}]=\frac1{\sqrt{2\pi}}\int\mathrm{e}^{-(1-2\mathrm{i}t)x^2/2}\,\mathrm{d}x=(1-2\mathrm{i}t)^{-1/2}$, and (1) follows by independence. (2) $\mathbb{E}[X^2]=1$ and $\operatorname{Var}(X^2)=\mathbb{E}[X^4]-1=3-1=2$, so by independence $\mathbb{E}[\xi]=r$ and $\operatorname{Var}(\xi)=2r$. (3) By (1) the characteristic function of the sum is $(1-2\mathrm{i}t)^{-(r_1+\cdots+r_k)/2}$; alternatively, the sum is directly a sum of $r_1+\dots+r_k$ independent squared standard normals. $\square$

**Definition 2.1.4 (t-Distribution)** Let $X\sim\mathcal{N}(0,1)$ and $Y\sim\chi^2_r$ be independent. The distribution of

$$
T=\frac X{\sqrt{Y/r}}
$$
is called the **$t$-distribution** (Student's $t$-distribution) with $r$ degrees of freedom, written $T\sim t_r$. Its density is

$$
f_T(t)=\frac{\Gamma\left(\frac{r+1}2\right)}{\Gamma\left(\frac r2\right)\sqrt{\pi r}}\left(1+\frac{t^2}r\right)^{-(r+1)/2},\qquad t\in\mathbb{R}.
$$

The distribution was found by W. S. Gosset, who published under the pseudonym "Student" in 1908. The density is symmetric about $0$, so $t_{r,1-\alpha}=-t_{r,\alpha}$; it has heavier tails than the normal density.

**Proposition 2.1.2** Let $T\sim t_r$.

1. $\mathbb{E}[T^k]$ exists if and only if $k<r$, and then

   $$
   \mathbb{E}[T^k]=\begin{cases}r^{k/2}\dfrac{\Gamma\left(\frac{k+1}2\right)\Gamma\left(\frac{r-k}2\right)}{\Gamma\left(\frac r2\right)\Gamma\left(\frac12\right)}, & k\text{ even},\\[3mm] 0, & k\text{ odd}.\end{cases}
   $$
   In particular $\mathbb{E}[T]=0$ for $r\ge2$ and $\operatorname{Var}(T)=r/(r-2)$ for $r\ge3$.
2. For $r=1$, $t_1$ is the standard Cauchy distribution, with density $f_1(t)=\dfrac1{\pi(1+t^2)}$, $t\in\mathbb{R}$; it has no mean.
3. As $r\to\infty$, $t_r$ converges to $\mathcal{N}(0,1)$.

**Proof** (1) The tail of $f_T$ behaves like $|t|^{-(r+1)}$, so $\int|t|^kf_T(t)\,\mathrm{d}t<\infty$ exactly when $k<r$. For even $k<r$, independence gives $\mathbb{E}[T^k]=r^{k/2}\,\mathbb{E}[X^k]\,\mathbb{E}[Y^{-k/2}]$ with $\mathbb{E}[X^k]=2^{k/2}\Gamma(\frac{k+1}2)/\Gamma(\frac12)$ and $\mathbb{E}[Y^{-k/2}]=2^{-k/2}\Gamma(\frac{r-k}2)/\Gamma(\frac r2)$, which multiply to the formula; odd moments vanish by symmetry. For $k=2$ the formula gives $r\cdot\frac{\Gamma(3/2)\Gamma(r/2-1)}{\Gamma(r/2)\Gamma(1/2)}=\frac r{2(r/2-1)}=\frac r{r-2}$. (2) Substitute $r=1$, $\Gamma(1)=1$, $\Gamma(\frac12)=\sqrt\pi$. (3) By the **law of large numbers** $Y/r\to1$ in probability, so $T\xrightarrow{d}\mathcal{N}(0,1)$ by Slutsky's theorem (Theorem 2.1.4); the densities also converge pointwise, since $(1+t^2/r)^{-(r+1)/2}\to\mathrm{e}^{-t^2/2}$. $\square$

**Definition 2.1.5 (F-Distribution)** Let $X\sim\chi^2_{r_1}$ and $Y\sim\chi^2_{r_2}$ be independent. The distribution of

$$
F=\frac{X/r_1}{Y/r_2}
$$
is called the **$F$-distribution** with $r_1$ and $r_2$ degrees of freedom, written $F\sim F_{r_1,r_2}$. Its density is

$$
f_{r_1,r_2}(x)=\begin{cases}\dfrac{\Gamma\left(\frac{r_1+r_2}2\right)}{\Gamma\left(\frac{r_1}2\right)\Gamma\left(\frac{r_2}2\right)}\left(\dfrac{r_1}{r_2}\right)^{r_1/2}x^{r_1/2-1}\left(1+\dfrac{r_1}{r_2}x\right)^{-(r_1+r_2)/2}, & x>0,\\[3mm] 0, & x\le0.\end{cases}
$$

The $F$-distribution is used, for example, to compare the variances of two normal populations and in the analysis of variance.

**Proposition 2.1.3**

1. If $F\sim F_{r_1,r_2}$, then $1/F\sim F_{r_2,r_1}$.
2. If $T\sim t_r$, then $T^2\sim F_{1,r}$.
3. If $F\sim F_{r_1,r_2}$ and $0<2k<r_2$, then

   $$
   \mathbb{E}[F^k]=\left(\frac{r_2}{r_1}\right)^k\frac{\Gamma\left(\frac{r_1}2+k\right)\Gamma\left(\frac{r_2}2-k\right)}{\Gamma\left(\frac{r_1}2\right)\Gamma\left(\frac{r_2}2\right)};
   $$
   in particular

   $$
   \mathbb{E}[F]=\frac{r_2}{r_2-2}\quad(r_2\ge3),\qquad\operatorname{Var}(F)=\frac{2r_2^2(r_1+r_2-2)}{r_1(r_2-2)^2(r_2-4)}\quad(r_2\ge5).
   $$
4. $F_{r_1,r_2,1-\alpha}=1/F_{r_2,r_1,\alpha}$.

**Proof** (1) $1/F=\frac{Y/r_2}{X/r_1}$ with the roles of $X$ and $Y$ exchanged. (2) $T^2=\frac{X^2/1}{Y/r}$ with $X^2\sim\chi^2_1$ independent of $Y\sim\chi^2_r$. (3) By independence $\mathbb{E}[F^k]=(r_2/r_1)^k\,\mathbb{E}[X^k]\,\mathbb{E}[Y^{-k}]$, and for $\xi\sim\chi^2_r$ and $s>-r/2$, $\mathbb{E}[\xi^s]=2^s\Gamma(\frac r2+s)/\Gamma(\frac r2)$. (4) By (1), $1-\alpha=\mathbb{P}(F>F_{r_1,r_2,1-\alpha})=\mathbb{P}(1/F<1/F_{r_1,r_2,1-\alpha})$, so $\mathbb{P}(1/F>1/F_{r_1,r_2,1-\alpha})=\alpha$ with $1/F\sim F_{r_2,r_1}$. $\square$

Property (4) is why tables of the $F$-distribution list only small values of $\alpha$.

![Densities of the chi-square distribution for r = 1, 2, 4, 8 with the upper 0.05 quantile for r = 4 shaded, of the t distribution for r = 1, 5, 10 against the standard normal density, and of the F distribution for three pairs of degrees of freedom](./plots/sampling-distributions.py)

### 2.1.5. Some Useful Corollaries

The following corollaries combine Theorem 2.1.3 with the definitions above; they are the pivotal quantities of the normal-theory intervals and tests in [3.2.4](/3.2.4) and [3.2.5](/3.2.5).

**Corollary 2.1.3** If $X_1,\dots,X_n$ are independent with $X_i\sim\mathcal{N}(a_i,\sigma_i^2)$, then

$$
\sum_{i=1}^n\left(\frac{X_i-a_i}{\sigma_i}\right)^2\sim\chi^2_n.
$$

**Proof** The standardized variables $(X_i-a_i)/\sigma_i$ are iid $\mathcal{N}(0,1)$. $\square$

**Corollary 2.1.4** If $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$, then

$$
T=\frac{\sqrt n(\bar X-a)}S\sim t_{n-1}.
$$

**Proof** Write $T=\dfrac{\sqrt n(\bar X-a)/\sigma}{\sqrt{[(n-1)S^2/\sigma^2]/(n-1)}}$. By Theorem 2.1.3 the numerator is $\mathcal{N}(0,1)$, the quantity in brackets is $\chi^2_{n-1}$, and the two are independent. $\square$

**Corollary 2.1.5** Let $X_1,\dots,X_m\overset{\text{iid}}{\sim}\mathcal{N}(a_1,\sigma^2)$ and $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(a_2,\sigma^2)$, the two samples being independent. Then

$$
T=\frac{(\bar X-\bar Y)-(a_1-a_2)}{S_w}\sqrt{\frac{mn}{m+n}}\sim t_{m+n-2},
$$
where $(m+n-2)S_w^2=(m-1)S_X^2+(n-1)S_Y^2$, $S_X^2=\frac1{m-1}\sum_{i=1}^m(X_i-\bar X)^2$ and $S_Y^2=\frac1{n-1}\sum_{j=1}^n(Y_j-\bar Y)^2$.

**Proof** By Theorem 2.1.1, $\bar X-\bar Y\sim\mathcal{N}\big(a_1-a_2,\ \sigma^2(\frac1m+\frac1n)\big)$, so $U=\frac{(\bar X-\bar Y)-(a_1-a_2)}\sigma\sqrt{\frac{mn}{m+n}}\sim\mathcal{N}(0,1)$. By Theorem 2.1.3 and Proposition 2.1.1, $V=(m+n-2)S_w^2/\sigma^2=(m-1)S_X^2/\sigma^2+(n-1)S_Y^2/\sigma^2\sim\chi^2_{m+n-2}$, and $V$ is independent of $U$ because $\bar X,S_X^2,\bar Y,S_Y^2$ are mutually independent. Hence $T=U/\sqrt{V/(m+n-2)}\sim t_{m+n-2}$. $\square$

**Corollary 2.1.6** Let $X_1,\dots,X_m\overset{\text{iid}}{\sim}\mathcal{N}(a_1,\sigma_1^2)$ and $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(a_2,\sigma_2^2)$, the two samples being independent. Then

$$
F=\frac{S_X^2}{S_Y^2}\cdot\frac{\sigma_2^2}{\sigma_1^2}\sim F_{m-1,n-1}.
$$

**Proof** $F=\dfrac{[(m-1)S_X^2/\sigma_1^2]/(m-1)}{[(n-1)S_Y^2/\sigma_2^2]/(n-1)}$, a ratio of independent $\chi^2_{m-1}$ and $\chi^2_{n-1}$ variables divided by their degrees of freedom. $\square$

**Corollary 2.1.7** If $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathrm{Exp}(\lambda)$, with density $f(x;\lambda)=\lambda\mathrm{e}^{-\lambda x}\boldsymbol{1}_{(0,\infty)}(x)$, then

$$
2\lambda n\bar X=2\lambda\sum_{i=1}^nX_i\sim\chi^2_{2n}.
$$

**Proof** First consider $2\lambda X_1$: for $x>0$, $\mathbb{P}(2\lambda X_1>x)=\mathbb{P}(X_1>x/(2\lambda))=\mathrm{e}^{-x/2}$, so $2\lambda X_1$ has density $\frac12\mathrm{e}^{-x/2}$, which is the $\chi^2_2$ density. The variables $2\lambda X_i$ are independent $\chi^2_2$, and Proposition 2.1.1 gives the sum $\chi^2_{2n}$. $\square$

### 2.1.6. Limiting Distributions

**Definition 2.1.6 (Limiting Distribution)** If the distribution of a statistic converges to a given distribution as the sample size $n\to\infty$, this distribution is called the **limiting distribution** (large-sample distribution) of the statistic.

Limiting distributions are needed because exact distributions are usually hard to obtain, and even when available may be too complicated to use; the limit provides an approximation, and it is also the standard tool for comparing inference methods. Properties of a statistic or a method as $n\to\infty$ are called large-sample properties, and their study is large-sample (asymptotic) theory; properties for a fixed sample size are small-sample properties.

**Example 2.1.1** Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}F$, not necessarily normal, with mean $a_F$ and variance $\sigma_F^2\in(0,\infty)$, and let $\bar X_n$ be the sample mean. Large-sample properties: by the strong **law of large numbers** $\mathbb{P}(\lim_{n\to\infty}\bar X_n=a_F)=1$, and by the **central limit theorem** $\sqrt n(\bar X_n-a_F)/\sigma_F\xrightarrow{d}\mathcal{N}(0,1)$, so that

$$
\mathbb{P}(|\bar X_n-a_F|>c)\approx2\left[1-\Phi\left(\frac{c\sqrt n}{\sigma_F}\right)\right]
$$
for large $n$, where $\Phi$ is the standard normal distribution function. A small-sample property: $\mathbb{E}[\bar X_n]=a_F$ for every $n$.

The main tool for limiting distributions is Slutsky's theorem, proved in [3.1.14](/3.1.14).

**Theorem 2.1.4 (Slutsky's Theorem)** Let $X_n$ and $Y_n$ be sequences of random variables with $X_n\xrightarrow{d}X$ and $Y_n\xrightarrow{p}c$, where $c$ is a constant. Then

1. $X_n+Y_n\xrightarrow{d}X+c$;
2. $X_nY_n\xrightarrow{d}cX$;
3. $X_n/Y_n\xrightarrow{d}X/c$, provided $c\ne0$.

**Example 2.1.2** In Example 2.1.1, $S_n^2\to\sigma_F^2$ almost surely, since $S_n^2=\frac n{n-1}\left(\frac1n\sum X_i^2-\bar X_n^2\right)$ and both averages converge by the strong law; hence $\sigma_F/S_n\xrightarrow{p}1$, and Slutsky's theorem gives

$$
\frac{\sqrt n(\bar X_n-a_F)}{S_n}=\frac{\sqrt n(\bar X_n-a_F)}{\sigma_F}\cdot\frac{\sigma_F}{S_n}\xrightarrow{d}\mathcal{N}(0,1)
$$
for any population with finite positive variance. For a normal population the exact distribution of this statistic is $t_{n-1}$ (Corollary 2.1.4); the two facts are consistent because $t_{n-1}\to\mathcal{N}(0,1)$.

**Example 2.1.3** Let $X_1,\dots,X_n$ be a sample from the Bernoulli population $\mathrm{Ber}(p)$, $0<p<1$. Then the limiting distribution of $\dfrac{\sqrt n(\bar X_n-p)}{\sqrt{\bar X_n(1-\bar X_n)}}$ is $\mathcal{N}(0,1)$.

**Proof** Let $\hat p=\bar X_n$. By the **central limit theorem** and the weak law of large numbers,

$$
\frac{\sqrt n(\hat p-p)}{\sqrt{p(1-p)}}\xrightarrow{d}\mathcal{N}(0,1),\qquad\frac{p(1-p)}{\hat p(1-\hat p)}\xrightarrow{p}1
$$
(the second because $\hat p\xrightarrow{p}p$ and $x\mapsto p(1-p)/[x(1-x)]$ is continuous at $p$). By Slutsky's theorem,

$$
\frac{\sqrt n(\bar X_n-p)}{\sqrt{\bar X_n(1-\bar X_n)}}=\frac{\sqrt n(\hat p-p)}{\sqrt{p(1-p)}}\cdot\sqrt{\frac{p(1-p)}{\hat p(1-\hat p)}}\xrightarrow{d}\mathcal{N}(0,1).
$$

The statistic is undefined when $\hat p\in\{0,1\}$, but this event has probability $p^n+(1-p)^n\to0$ and does not affect the limit. $\square$

This example is the basis of the large-sample confidence interval for a proportion in [3.2.4](/3.2.4).

## 2.2. Exponential Families

### 2.2.1. Distribution Families and the Likelihood

A distribution family $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ ([3.2.1](/3.2.1)) may have a vector parameter $\theta=(\theta_1,\dots,\theta_k)$. The notations $f_\theta(x)$, $f(x\mid\theta)$ and $f(x;\theta)$ are used interchangeably; $f$ is a density in the continuous case and a probability mass function in the discrete case. Regarded as a function of $\theta$ for the observed $x$, the density is called the likelihood function $L(\theta;x)=f(x;\theta)$, and $\ell(\theta;x)=\log L(\theta;x)$ is the log-likelihood; they are central in [3.2.3](/3.2.3).

Many familiar families look alike:

- normal $\mathcal{N}(\theta,1)$: $f(x;\theta)=\frac1{\sqrt{2\pi}}\mathrm{e}^{-(x-\theta)^2/2}$, $x\in\mathbb{R}$, $\theta\in\mathbb{R}$;
- Poisson: $f(x;\theta)=\frac{\theta^x}{x!}\mathrm{e}^{-\theta}$, $x=0,1,2,\dots$, $\theta>0$;
- exponential: $f(x;\theta)=\theta\mathrm{e}^{-\theta x}$, $x>0$, $\theta>0$;
- normal $\mathcal{N}(\mu,\sigma^2)$: $f(x;\theta)=\frac1{\sqrt{2\pi}\sigma}\mathrm{e}^{-(x-\mu)^2/(2\sigma^2)}$, $x\in\mathbb{R}$, $\theta=(\mu,\sigma^2)\in\mathbb{R}\times(0,\infty)$.

In each, the parameter and the observation interact only through an exponential of a sum of products of a function of $\theta$ and a function of $x$.

### 2.2.2. Definition and Examples

**Definition 2.2.1 (Exponential Family)** Let $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ be a distribution family with parameter space $\Theta$. If the densities have the form

$$
f(x;\theta)=C(\theta)\exp\left\{\sum_{i=1}^kQ_i(\theta)T_i(x)\right\}h(x),
$$
where $k$ is a positive integer, $C(\theta)>0$ and $Q_1(\theta),\dots,Q_k(\theta)$ are functions of $\theta$ alone (not depending on $x$), and $h(x)\ge0$ and $T_1(x),\dots,T_k(x)$ are functions of $x$ alone (not depending on $\theta$), then $\mathcal{F}$ is called an **exponential family**.

The point of the definition is not the common shape of the formulas but what they share structurally: many problems of statistical theory (sufficiency, completeness, optimal estimators and tests) have complete solutions for exponential families. The notion goes back to E. J. G. Pitman, G. Darmois and B. O. Koopman (1935–1936), who showed that, among families whose support does not depend on the parameter, essentially only exponential families admit sufficient statistics of fixed dimension for every sample size (the Pitman–Koopman–Darmois theorem).

**Example 2.2.1** Let $\boldsymbol{X}=(X_1,\dots,X_n)$ be a sample from $\mathcal{N}(\mu,\sigma^2)$. With $\theta=(\mu,\sigma^2)\in\Theta=\{(\mu,\sigma^2)\colon-\infty<\mu<\infty,\ \sigma^2>0\}$, the joint density is

$$
f(\boldsymbol{x};\theta)=(\sqrt{2\pi}\sigma)^{-n}\exp\left\{-\frac1{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2\right\}=(\sqrt{2\pi}\sigma)^{-n}\mathrm{e}^{-\frac{n\mu^2}{2\sigma^2}}\exp\left\{\frac\mu{\sigma^2}\sum_{i=1}^nx_i-\frac1{2\sigma^2}\sum_{i=1}^nx_i^2\right\},
$$
which has the form $C(\theta)\exp\{Q_1(\theta)T_1(\boldsymbol{x})+Q_2(\theta)T_2(\boldsymbol{x})\}h(\boldsymbol{x})$ with

$$
C(\theta)=(\sqrt{2\pi}\sigma)^{-n}\mathrm{e}^{-n\mu^2/(2\sigma^2)},\quad Q_1(\theta)=\frac\mu{\sigma^2},\quad Q_2(\theta)=-\frac1{2\sigma^2},\quad T_1(\boldsymbol{x})=\sum_{i=1}^nx_i,\quad T_2(\boldsymbol{x})=\sum_{i=1}^nx_i^2,\quad h(\boldsymbol{x})=1.
$$

So the family of sample distributions is an exponential family. With $n=1$ the same computation shows that $\{\mathcal{N}(\mu,\sigma^2)\}$ itself is an exponential family; the property does not depend on the sample size, and in general the joint density of a sample from an exponential family is again of exponential form, with $T_i(\boldsymbol{x})=\sum_{j=1}^nT_i(x_j)$.

**Example 2.2.2** Let $\boldsymbol{X}$ be a sample from the gamma distribution $\Gamma(\gamma,\lambda)$ with density $\frac{\lambda^\gamma}{\Gamma(\gamma)}x^{\gamma-1}\mathrm{e}^{-\lambda x}\boldsymbol{1}_{(0,\infty)}(x)$, $\theta=(\gamma,\lambda)\in\Theta=\{(\gamma,\lambda)\colon\gamma>0,\ \lambda>0\}$. Then

$$
f(\boldsymbol{x};\theta)=\prod_{i=1}^n\frac{\lambda^\gamma}{\Gamma(\gamma)}x_i^{\gamma-1}\mathrm{e}^{-\lambda x_i}\boldsymbol{1}_{(0,\infty)}(x_i)=\frac{\lambda^{n\gamma}}{(\Gamma(\gamma))^n}\exp\left\{-\lambda\sum_{i=1}^nx_i+(\gamma-1)\sum_{i=1}^n\log x_i\right\}\prod_{i=1}^n\boldsymbol{1}_{(0,\infty)}(x_i),
$$
an exponential family with $C(\theta)=\lambda^{n\gamma}/(\Gamma(\gamma))^n$, $Q_1(\theta)=-\lambda$, $Q_2(\theta)=\gamma-1$, $T_1(\boldsymbol{x})=\sum x_i$, $T_2(\boldsymbol{x})=\sum\log x_i$, $h(\boldsymbol{x})=\prod\boldsymbol{1}_{(0,\infty)}(x_i)$.

**Example 2.2.3** The binomial family $\{\mathrm{Bin}(n,\theta)\colon0<\theta<1\}$ is an exponential family. For $X\sim\mathrm{Bin}(n,\theta)$, with sample space $\mathcal{X}=\{0,1,\dots,n\}$ and $\Theta=(0,1)$,

$$
f(x;\theta)=\binom nx\theta^x(1-\theta)^{n-x}=(1-\theta)^n\exp\left\{x\log\frac\theta{1-\theta}\right\}\binom nx,
$$
so $C(\theta)=(1-\theta)^n$, $Q_1(\theta)=\log\frac\theta{1-\theta}$, $T_1(x)=x$ and $h(x)=\binom nx$.

**Example 2.2.4** The Poisson family $\{\mathrm{Poi}(\theta)\colon\theta>0\}$ is an exponential family: for $x\in\mathcal{X}=\{0,1,2,\dots\}$,

$$
f(x;\theta)=\frac{\mathrm{e}^{-\theta}\theta^x}{x!}=\mathrm{e}^{-\theta}\exp\{x\log\theta\}\frac1{x!},
$$
with $\Theta=(0,\infty)$, $C(\theta)=\mathrm{e}^{-\theta}$, $Q_1(\theta)=\log\theta$, $T_1(x)=x$ and $h(x)=1/x!$.

The support $\{x\colon f(x;\theta)>0\}=\{x\colon h(x)>0\}$ of an exponential family does not depend on $\theta$: all distributions in the family have the same support. This gives a quick way to recognize families that are not exponential.

**Example 2.2.5** (1) The uniform family $\{\mathrm{U}(0,\theta)\colon\theta>0\}$, with $f(x;\theta)=\frac1\theta\boldsymbol{1}_{[0,\theta]}(x)$, is not an exponential family, because its support $[0,\theta]$ depends on $\theta$.

(2) The Cauchy location family $f(x;\theta)=\dfrac1{\pi[1+(x-\theta)^2]}$, $x\in\mathbb{R}$, $\theta\in\mathbb{R}$, has a fixed support but is not an exponential family either. If it were, then $\log f(x;\theta)-\log f(x;0)=\log(1+x^2)-\log(1+(x-\theta)^2)$ would lie, for every $\theta$, in the span of the finitely many functions $1,T_1(x),\dots,T_k(x)$; but the functions $\log(1+(x-\theta)^2)$ for different $\theta$ span an infinite-dimensional space.

### 2.2.3. The Natural Form

Writing $\varphi_i=Q_i(\theta)$ and expressing $C(\theta)$ as a function $C^*(\varphi)$ of $\varphi=(\varphi_1,\dots,\varphi_k)$ simplifies the form; afterwards we rename $\varphi_i$ as $\theta_i$.

**Definition 2.2.2 (Natural Form)** An exponential family written as

$$
f(x;\theta)=C^*(\theta)\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)
$$
is said to be in **natural form** (canonical form), and $\theta=(\theta_1,\dots,\theta_k)$ is the **natural parameter**. The set

$$
\Theta^*=\left\{(\theta_1,\dots,\theta_k)\colon\int_{\mathcal{X}}\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)\,\mathrm{d}x<\infty\right\}
$$
is called the **natural parameter space**.

For discrete distributions the integral is a sum. $\Theta^*$ is the set of all $\theta$ for which the formula defines a probability distribution, with $C^*(\theta)=\left(\int\mathrm{e}^{\sum\theta_iT_i}h\,\mathrm{d}x\right)^{-1}$; it contains the image of the original parameter space and may be larger.

**Example 2.2.6** For a normal sample (Example 2.2.1), let

$$
\begin{cases}\varphi_1=\mu/\sigma^2,\\ \varphi_2=-1/(2\sigma^2),\end{cases}\qquad\text{so that}\qquad\begin{cases}\sigma^2=-1/(2\varphi_2),\\ \mu^2/\sigma^2=-\varphi_1^2/(2\varphi_2).\end{cases}
$$

Then $C(\theta)=C^*(\varphi)=(-\pi/\varphi_2)^{-n/2}\exp\{n\varphi_1^2/(4\varphi_2)\}$, and

$$
f(\boldsymbol{x};\varphi)=C^*(\varphi)\exp\{\varphi_1T_1(\boldsymbol{x})+\varphi_2T_2(\boldsymbol{x})\}h(\boldsymbol{x}),\qquad\Theta^*=\{(\varphi_1,\varphi_2)\colon-\infty<\varphi_1<\infty,\ -\infty<\varphi_2<0\}.
$$

**Example 2.2.7** For the binomial family (Example 2.2.3), let $\varphi=\log[\theta/(1-\theta)]$; then $-\infty<\varphi<\infty$ and $1-\theta=1/(1+\mathrm{e}^\varphi)$, so

$$
f(x;\varphi)=(1+\mathrm{e}^\varphi)^{-n}\exp\{\varphi x\}\binom nx,\qquad\Theta^*=(-\infty,\infty).
$$

The natural parameter is the log-odds, the parameter of logistic regression.

### 2.2.4. Properties of Exponential Families

**Theorem 2.2.1** Let $\{f(x;\theta)\colon\theta\in\Theta^*\}$ be an exponential family in natural form.

1. All distributions in the family have the same support $\{x\colon h(x)>0\}$, which does not depend on $\theta$.
2. The natural parameter space $\Theta^*$ is a convex set.
3. Suppose $\Theta^*$ has interior points, and let $\Theta_0$ be the set of its interior points. If $g(x)$ is a real function for which

   $$
   G(\theta)=\int_{\mathcal{X}}g(x)\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)\,\mathrm{d}x
   $$
   exists and is finite on $\Theta^*$, then $G$ has partial derivatives of all orders on $\Theta_0$, obtained by differentiating under the integral sign:

   $$
   \frac{\partial^mG(\theta)}{\partial\theta_1^{m_1}\cdots\partial\theta_k^{m_k}}=\int_{\mathcal{X}}g(x)\prod_{i=1}^kT_i(x)^{m_i}\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)\,\mathrm{d}x,\qquad m=m_1+\cdots+m_k.
   $$
4. The family is preserved under smooth invertible transformations: if $Y=Y(X)$ is a smooth invertible transformation of $X$, the distributions of $Y$ again form an exponential family with the same $C$ and $Q_i$.

**Proof** (1) is immediate since $C^*(\theta)>0$ and the exponential is positive. (2) Let $\theta^0,\theta^1\in\Theta^*$, $0<\alpha<1$ and $\theta=\alpha\theta^0+(1-\alpha)\theta^1$. By Hölder's inequality $\|fg\|_1\le\|f\|_p\|g\|_q$ with $p=1/\alpha$, $q=1/(1-\alpha)$,

$$
\int_{\mathcal{X}}\mathrm{e}^{\sum_i\theta_iT_i(x)}h(x)\,\mathrm{d}x=\int_{\mathcal{X}}\left[\mathrm{e}^{\sum_i\theta^0_iT_i(x)}h(x)\right]^\alpha\left[\mathrm{e}^{\sum_i\theta^1_iT_i(x)}h(x)\right]^{1-\alpha}\mathrm{d}x\le\left[\int_{\mathcal{X}}\mathrm{e}^{\sum_i\theta^0_iT_i}h\,\mathrm{d}x\right]^\alpha\left[\int_{\mathcal{X}}\mathrm{e}^{\sum_i\theta^1_iT_i}h\,\mathrm{d}x\right]^{1-\alpha}<\infty,
$$
so $\theta\in\Theta^*$. (3) Near an interior point the integrand and its derivatives are dominated by integrable functions of the form $|g|\,\mathrm{e}^{\sum(\theta_i\pm\delta)T_i}h$, and dominated convergence justifies differentiation under the integral sign; we omit the details. (4) By the change-of-variables formula,

$$
f_Y(y;\theta)=f_X(x(y);\theta)\left|\frac{\partial x}{\partial y}\right|=C(\theta)\exp\left\{\sum_{i=1}^kQ_i(\theta)T_i(x(y))\right\}h(x(y))\left|\frac{\partial x}{\partial y}\right|.
$$

The Jacobian depends only on $y$, so $C(\theta)$ and $Q_i(\theta)$ are unchanged, while $T_i$ becomes $T_i(x(y))$ and $h$ becomes $h(x(y))\,|\partial x/\partial y|$. $\square$

Property 3 with $g=1$ computes the moments of $T_i(X)$ from the normalizing constant alone.

**Corollary 2.2.1** In natural form, let $D(\theta)=\log C^*(\theta)$. For $\theta\in\Theta_0$,

$$
\mathbb{E}_\theta[T_i(X)]=-\frac{\partial D(\theta)}{\partial\theta_i},\qquad\operatorname{Cov}_\theta(T_i(X),T_j(X))=-\frac{\partial^2D(\theta)}{\partial\theta_i\partial\theta_j};
$$
in particular $\operatorname{Var}_\theta(T_i(X))=-\partial^2D(\theta)/\partial\theta_i^2$.

**Proof** Since $\int f(x;\theta)\,\mathrm{d}x=1$,

$$
\int_{\mathcal{X}}\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)\,\mathrm{d}x=\frac1{C^*(\theta)}=\mathrm{e}^{-D(\theta)}.
$$

Differentiating with respect to $\theta_i$ under the integral sign (Theorem 2.2.1(3)),

$$
\int_{\mathcal{X}}T_i(x)\exp\left\{\sum_{l=1}^k\theta_lT_l(x)\right\}h(x)\,\mathrm{d}x=-\frac{\partial D(\theta)}{\partial\theta_i}\mathrm{e}^{-D(\theta)},
$$
and multiplying by $\mathrm{e}^{D(\theta)}=C^*(\theta)$ gives $\mathbb{E}_\theta[T_i(X)]=-\partial D/\partial\theta_i$. Differentiating this identity, written as $\int T_i\,f(x;\theta)\,\mathrm{d}x=-\partial_iD$, with respect to $\theta_j$ gives $\int T_i(T_j+\partial_jD)f\,\mathrm{d}x=-\partial_i\partial_jD$, that is, $\mathbb{E}[T_iT_j]-\mathbb{E}[T_i]\mathbb{E}[T_j]=-\partial_i\partial_jD$. $\square$

**Example 2.2.8** For $X\sim\mathrm{Bin}(n,\theta)$ in the natural form of Example 2.2.7, $\theta=\mathrm{e}^\varphi/(1+\mathrm{e}^\varphi)$, $T_1(x)=x$ and $D(\varphi)=\log C^*(\varphi)=-n\log(1+\mathrm{e}^\varphi)$. Hence

$$
\mathbb{E}[X]=-\frac{\partial D}{\partial\varphi}=n\frac{\mathrm{e}^\varphi}{1+\mathrm{e}^\varphi}=n\theta,\qquad\operatorname{Var}(X)=-\frac{\partial^2D}{\partial\varphi^2}=n\frac{\mathrm{e}^\varphi}{(1+\mathrm{e}^\varphi)^2}=n\theta(1-\theta),
$$
recovering the binomial mean and variance without any summation.

## 2.3. Sufficient and Complete Statistics

### 2.3.1. Sufficient Statistics

Let $\boldsymbol{X}=(X_1,\dots,X_n)$ be a sample from $f(x;\theta)$. A statistic $T(\boldsymbol{X})$ simplifies, or summarizes, the information about $\theta$ in the sample. We want as much simplification as possible with as little loss of information as possible. Intuitively,

$$
\text{information about }\theta\text{ in }\boldsymbol{X}=\text{information in }T(\boldsymbol{X})+\text{information remaining in }\boldsymbol{X}\text{ once }T(\boldsymbol{X})\text{ is known}.
$$

If the last term is zero, $T$ extracts all the information and we may use $T(\boldsymbol{X})$ instead of the $n$ observations without loss. The remaining information is zero when, given $T$, the sample has a distribution not involving $\theta$: then the detailed data are like an extra random draw that could be generated without knowing $\theta$. The concept was proposed by R. A. Fisher in 1922.

**Example 2.3.1** Let $X_1,\dots,X_n$ be a sample from $\mathrm{Ber}(\theta)$, $0<\theta<1$, and $T(\boldsymbol{X})=\sum_{i=1}^nX_i\sim\mathrm{Bin}(n,\theta)$. Intuitively the number of successes contains all the information about $\theta$, and their order contains none. Indeed, with $t=\sum x_i$, $f_{\boldsymbol{X}}(\boldsymbol{x};\theta)=\theta^t(1-\theta)^{n-t}$ and $f_T(t;\theta)=\binom nt\theta^t(1-\theta)^{n-t}$, so for $\boldsymbol{x}$ with $\sum x_i=t$,

$$
f(\boldsymbol{x}\mid t)=\frac{\mathbb{P}(X_1=x_1,\dots,X_n=x_n,T=t)}{f_T(t)}=\frac{\mathbb{P}(X_1=x_1,\dots,X_{n-1}=x_{n-1},X_n=t-x_1-\dots-x_{n-1})}{f_T(t)}=\frac{\theta^t(1-\theta)^{n-t}}{\binom nt\theta^t(1-\theta)^{n-t}}=\frac1{\binom nt},
$$
and $f(\boldsymbol{x}\mid t)=0$ if $\sum x_i\ne t$. Given the number of successes, every arrangement is equally likely, whatever $\theta$ is.

**Definition 2.3.1 (Sufficient Statistic)** A statistic $T(\boldsymbol{X})$ is said to be **sufficient** for $\theta$, or a **sufficient statistic**, if the conditional distribution of $\boldsymbol{X}=(X_1,\dots,X_n)$ given $T=t$ does not depend on $\theta$:

$$
g(\boldsymbol{x}\mid t,\theta)=g(\boldsymbol{x}\mid t).
$$

**Remark 2.3.1**

- A sufficient statistic contains all the information about $\theta$ in the sample.
- If $T$ is sufficient for $\theta$ and $g$ is a one-to-one measurable function, then $T^*=g(T)$ is also sufficient, because conditioning on $T$ and on $T^*$ is the same thing.
- If $T$ is sufficient and $T_1$ is any other statistic, then $(T,T_1)$ is sufficient.
- If $\theta$ is $k$-dimensional, we usually need a multidimensional sufficient statistic, typically of dimension $k$.

**Example 2.3.2** Let $X_1,\dots,X_n$ be a sample from $\mathcal{N}(\theta,1)$. Then $T(\boldsymbol{X})=\bar X$ is sufficient for $\theta$. Deriving the conditional distribution of $\boldsymbol{X}$ given $\bar X$ directly is awkward; instead use the orthogonal matrix $A$ of the proof of Theorem 2.1.3 and $\boldsymbol{Y}=A\boldsymbol{X}$, so that

$$
Y_1=\frac1{\sqrt n}\sum_{i=1}^nX_i=\sqrt n\,\bar X,\qquad Y_j=\sum_{k=1}^na_{jk}X_k,\quad j=2,\dots,n.
$$

The transformation is one-to-one with Jacobian determinant of absolute value $1$, so the sufficiency of $\bar X$ for $\boldsymbol{X}$ is equivalent to the sufficiency of $Y_1$ for $\boldsymbol{Y}$. By the proof of Theorem 2.1.3, $Y_1,\dots,Y_n$ are independent, $Y_1\sim\mathcal{N}(\sqrt n\theta,1)$ and $Y_i\sim\mathcal{N}(0,1)$ for $i\ge2$. Hence the joint density of $\boldsymbol{Y}$ and the marginal density of $Y_1$ are

$$
f(y_1,\dots,y_n)=(2\pi)^{-n/2}\exp\left\{-\frac12(y_1-\sqrt n\theta)^2-\frac12\sum_{i=2}^ny_i^2\right\},\qquad f_{Y_1}(y_1)=(2\pi)^{-1/2}\exp\left\{-\frac12(y_1-\sqrt n\theta)^2\right\},
$$
and the conditional density of $\boldsymbol{Y}$ given $Y_1=y_1$ is

$$
f(y_1,\dots,y_n\mid y_1)=\frac{f(y_1,\dots,y_n)}{f_{Y_1}(y_1)}=(2\pi)^{-(n-1)/2}\exp\left\{-\frac12\sum_{i=2}^ny_i^2\right\},
$$
which does not depend on $\theta$.

**Example 2.3.3** In Example 2.3.2, $T(\boldsymbol{X})=X_1$ is not sufficient: it uses one observation and carries no information from $X_2,\dots,X_n$. Indeed

$$
f(x_1,\dots,x_n\mid x_1)=\frac{f(x_1,\dots,x_n)}{f_{X_1}(x_1)}=f(x_2,\dots,x_n)=(2\pi)^{-(n-1)/2}\exp\left\{-\frac12\sum_{i=2}^n(x_i-\theta)^2\right\}
$$
depends on $\theta$.

### 2.3.2. The Factorization Theorem

Checking sufficiency through conditional distributions is laborious. The factorization theorem, due to Fisher in the 1920s and proved in full generality by P. R. Halmos and L. J. Savage (1949) using the Radon–Nikodym theorem, reduces it to inspecting the joint density.

**Theorem 2.3.1 (Factorization Theorem)** Let $f(\boldsymbol{x};\theta)$ be the joint density of a sample $\boldsymbol{X}=(X_1,\dots,X_n)$ and $T(\boldsymbol{X})$ a statistic. Then $T(\boldsymbol{X})$ is sufficient for $\theta$ if and only if there are nonnegative functions $g$ and $h$ such that

$$
f(\boldsymbol{x};\theta)=g(t(\boldsymbol{x});\theta)\,h(\boldsymbol{x})\qquad\text{for all }\boldsymbol{x}\text{ and }\theta,
$$
where $t(\boldsymbol{x})$ is the observed value of $T(\boldsymbol{X})$; that is, $g$ depends on the sample only through $T$, and $h$ does not depend on $\theta$.

**Proof** *Discrete case.* If $f=g(t(\boldsymbol{x});\theta)h(\boldsymbol{x})$, then for $\boldsymbol{x}$ with $t(\boldsymbol{x})=t$,

$$
\mathbb{P}_\theta(\boldsymbol{X}=\boldsymbol{x}\mid T=t)=\frac{g(t;\theta)h(\boldsymbol{x})}{\sum_{\boldsymbol{y}\colon t(\boldsymbol{y})=t}g(t;\theta)h(\boldsymbol{y})}=\frac{h(\boldsymbol{x})}{\sum_{\boldsymbol{y}\colon t(\boldsymbol{y})=t}h(\boldsymbol{y})},
$$
which is free of $\theta$. Conversely, if $T$ is sufficient, $f(\boldsymbol{x};\theta)=\mathbb{P}_\theta(T=t(\boldsymbol{x}))\,\mathbb{P}(\boldsymbol{X}=\boldsymbol{x}\mid T=t(\boldsymbol{x}))$ is a factorization of the required form.

*Continuous case.* Let $\boldsymbol{T}=(T_1,\dots,T_k)$ with $k\le n$, and choose an $(n-k)$-dimensional statistic $\boldsymbol{Y}=(Y_1,\dots,Y_{n-k})$ such that $\boldsymbol{X}\mapsto(\boldsymbol{T},\boldsymbol{Y})$ is one-to-one with continuous first partial derivatives, so that $X_i=X_i(\boldsymbol{T},\boldsymbol{Y})$. Denote the absolute value of the Jacobian determinant by $w(\boldsymbol{t},\boldsymbol{y})=\left|\frac{\partial(x_1,\dots,x_n)}{\partial(\boldsymbol{t},\boldsymbol{y})}\right|$.

"If": the joint density of $(\boldsymbol{T},\boldsymbol{Y})$ is

$$
k(\boldsymbol{t},\boldsymbol{y};\theta)=f(\boldsymbol{x};\theta)\,w(\boldsymbol{t},\boldsymbol{y})=g(\boldsymbol{t};\theta)\,h\big(x_1(\boldsymbol{t},\boldsymbol{y}),\dots,x_n(\boldsymbol{t},\boldsymbol{y})\big)\,w(\boldsymbol{t},\boldsymbol{y})=g(\boldsymbol{t};\theta)\,\mu(\boldsymbol{t},\boldsymbol{y}),
$$
where $\mu$ does not depend on $\theta$. The marginal density of $\boldsymbol{T}$ is $V(\boldsymbol{t};\theta)=g(\boldsymbol{t};\theta)\int\mu(\boldsymbol{t},\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}$, so the conditional density of $\boldsymbol{Y}$ given $\boldsymbol{T}=\boldsymbol{t}$,

$$
q(\boldsymbol{y}\mid\boldsymbol{t})=\frac{k(\boldsymbol{t},\boldsymbol{y};\theta)}{V(\boldsymbol{t};\theta)}=\frac{\mu(\boldsymbol{t},\boldsymbol{y})}{\int_{\mathbb{R}^{n-k}}\mu(\boldsymbol{t},\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}},
$$
does not depend on $\theta$. Since $\boldsymbol{X}$ is a function of $(\boldsymbol{T},\boldsymbol{Y})$, the conditional distribution of $\boldsymbol{X}$ given $\boldsymbol{T}$ does not depend on $\theta$ either.

"Only if": if $\boldsymbol{T}$ is sufficient, $q(\boldsymbol{y}\mid\boldsymbol{t})$ does not depend on $\theta$ and $k(\boldsymbol{t},\boldsymbol{y};\theta)=q(\boldsymbol{y}\mid\boldsymbol{t})V(\boldsymbol{t};\theta)$. Transforming back,

$$
f(\boldsymbol{x};\theta)=k(\boldsymbol{t},\boldsymbol{y};\theta)\left|\frac{\partial(\boldsymbol{t},\boldsymbol{y})}{\partial(x_1,\dots,x_n)}\right|=V(\boldsymbol{t}(\boldsymbol{x});\theta)\cdot q(\boldsymbol{y}(\boldsymbol{x})\mid\boldsymbol{t}(\boldsymbol{x}))\left|\frac{\partial(\boldsymbol{t},\boldsymbol{y})}{\partial(x_1,\dots,x_n)}\right|,
$$
which is $g(t(\boldsymbol{x});\theta)h(\boldsymbol{x})$ with $g=V$. $\square$

**Example 2.3.4** The factorization theorem recovers Examples 2.3.1 and 2.3.2 at once. For $\mathrm{Ber}(\theta)$, with $t=\sum x_i$, $f(\boldsymbol{x};\theta)=\theta^t(1-\theta)^{n-t}=g(t(\boldsymbol{x});\theta)\cdot1$. For $\mathcal{N}(\theta,1)$, with $t=\bar x$,

$$
f(\boldsymbol{x};\theta)=(2\pi)^{-n/2}\exp\left\{-\frac12\sum_{i=1}^n(x_i-\theta)^2\right\}=\underbrace{(2\pi)^{-n/2}\mathrm{e}^{-\frac{n\theta^2}2+n\theta t}}_{g(t;\theta)}\cdot\underbrace{\mathrm{e}^{-\frac12\sum_{i=1}^nx_i^2}}_{h(\boldsymbol{x})}.
$$

**Example 2.3.5** Let $X_1,\dots,X_n$ be a sample from $\mathrm{U}(0,\theta)$. Then $T(\boldsymbol{X})=X_{(n)}$ is sufficient for $\theta$, because

$$
f(\boldsymbol{x};\theta)=\frac1{\theta^n}\boldsymbol{1}_{\{0<x_i<\theta,\ i=1,\dots,n\}}=\frac1{\theta^n}\boldsymbol{1}_{\{x_{(n)}<\theta\}}\cdot\boldsymbol{1}_{\{x_{(1)}>0\}}=g(t(\boldsymbol{x});\theta)\,h(\boldsymbol{x}).
$$

**Example 2.3.6 (Sufficiency in an Exponential Family)** Let $\boldsymbol{X}$ be a sample from an exponential family. Then $T(\boldsymbol{X})=(T_1(\boldsymbol{X}),\dots,T_k(\boldsymbol{X}))$ is sufficient for $\theta$, since

$$
f(\boldsymbol{x};\theta)=C(\theta)\exp\left\{\sum_{i=1}^kQ_i(\theta)t_i(\boldsymbol{x})\right\}h(\boldsymbol{x})=g(t(\boldsymbol{x});\theta)\,h(\boldsymbol{x}).
$$

For a normal sample, $(\sum X_i,\sum X_i^2)$, or equivalently $(\bar X,S^2)$, is sufficient for $(\mu,\sigma^2)$; for a gamma sample, $(\sum X_i,\sum\log X_i)$ is sufficient for $(\gamma,\lambda)$.

### 2.3.3. Minimal Sufficient Statistics

Sufficient statistics are not unique. In Example 2.3.2, $T(\boldsymbol{X})=\bar X$ is sufficient, and so is $T_1(\boldsymbol{X})=\left(\sum_{i=1}^mX_i,\ \sum_{i=m+1}^nX_i\right)$ for any $1\le m<n$; $T$ is a function of $T_1$ and is simpler. The whole sample is always sufficient. We look for the greatest reduction.

**Definition 2.3.2 (Minimal Sufficient Statistic)** A sufficient statistic is called a **minimal sufficient statistic** if it can be expressed as a function of every other sufficient statistic.

A minimal sufficient statistic achieves the greatest data reduction possible without losing information. In an exponential family in natural form whose natural parameter space has interior points, $(T_1,\dots,T_k)$ is minimal sufficient.

### 2.3.4. Complete Statistics

Completeness is modeled on the completeness of an orthogonal system of functions: a system $M$ is complete if the only function orthogonal to every member of $M$ is $0$. For statistics it is the key to the uniqueness of unbiased estimators (the UMVUE theory of [3.2.3](/3.2.3)).

**Definition 2.3.3 (Complete Statistic)** Let $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ be a distribution family with parameter space $\Theta$, and $T=T(\boldsymbol{X})$ a statistic. If for every function $\varphi$ satisfying

$$
\mathbb{E}_\theta[\varphi(T(\boldsymbol{X}))]=0\qquad\text{for all }\theta\in\Theta
$$
we have

$$
\mathbb{P}_\theta(\varphi(T(\boldsymbol{X}))=0)=1\qquad\text{for all }\theta\in\Theta,
$$
then $T(\boldsymbol{X})$ is called a **complete statistic** for $\theta$.

If $T$ has density $g(t;\theta)$, the condition reads: $\int\varphi(t)g(t;\theta)\,\mathrm{d}t=0$ for all $\theta$ implies $\varphi=0$ almost everywhere on the support. That is, the only function "orthogonal" to the whole family $\{g(t;\theta)\colon\theta\in\Theta\}$ is $0$, so the completeness of $T$ is the completeness of this function family. Two consequences are immediate: if $T$ is complete, so is $\delta(T)$ for every measurable function $\delta$ (apply the definition to $\varphi\circ\delta$); and if $T$ is complete, two functions $\varphi_1(T)$, $\varphi_2(T)$ with the same expectation for every $\theta$ coincide with probability one.

**Example 2.3.7** Let $X_1,\dots,X_n$ be a sample from $\mathrm{Ber}(\theta)$. Then $T(\boldsymbol{X})=\sum X_i$ is complete for $\theta\in(0,1)$. Indeed $T\sim\mathrm{Bin}(n,\theta)$, and $\mathbb{E}_\theta\varphi(T)=0$ for $0<\theta<1$ means

$$
\sum_{k=0}^n\varphi(k)\binom nk\theta^k(1-\theta)^{n-k}=0\quad\Longleftrightarrow\quad\sum_{k=0}^n\varphi(k)\binom nk\delta^k=0,\qquad\delta=\frac\theta{1-\theta}\in(0,\infty).
$$

A polynomial of degree at most $n$ in $\delta$ that vanishes on $(0,\infty)$ has all coefficients zero, so $\varphi(k)\binom nk=0$, that is, $\varphi(k)=0$ for $k=0,1,\dots,n$. Since $\{0,1,\dots,n\}$ is the support of $T$, $\mathbb{P}_\theta(\varphi(T)=0)=1$.

**Example 2.3.8** Let $X_1,\dots,X_n$ be a sample from $\mathcal{N}(\theta,1)$, $\theta\in\mathbb{R}$. Then $T(\boldsymbol{X})=\bar X$ is complete. By Corollary 2.1.2, $\bar X\sim\mathcal{N}(\theta,1/n)$, so $\mathbb{E}_\theta\varphi(T)=0$ for all $\theta$ means

$$
\sqrt{\frac n{2\pi}}\int_{-\infty}^\infty\varphi(t)\mathrm{e}^{-n(t-\theta)^2/2}\,\mathrm{d}t=\sqrt{\frac n{2\pi}}\,\mathrm{e}^{-n\theta^2/2}\int_{-\infty}^\infty\varphi(t)\mathrm{e}^{-nt^2/2}\mathrm{e}^{nt\theta}\,\mathrm{d}t=0,
$$
hence, with $z=n\theta$,

$$
G(z)=\int_{-\infty}^\infty\varphi(t)\mathrm{e}^{-nt^2/2}\mathrm{e}^{tz}\,\mathrm{d}t=0,\qquad-\infty<z<\infty.
$$

Since the integral converges absolutely for every real $z$, $G$ extends to an **entire function** of the complex variable $z$, and it vanishes on the real axis; by the uniqueness theorem for analytic functions, $G(z)=0$ for all $z\in\mathbb{C}$. Taking $z=-\mathrm{i}u$ gives

$$
\int_{-\infty}^\infty\varphi(t)\mathrm{e}^{-nt^2/2}\mathrm{e}^{-\mathrm{i}ut}\,\mathrm{d}t=0,\qquad u\in\mathbb{R}:
$$
the **Fourier transform** of $\varphi(t)\mathrm{e}^{-nt^2/2}$ vanishes identically, so $\varphi(t)\mathrm{e}^{-nt^2/2}=0$ for almost every $t$, that is, $\varphi=0$ almost everywhere. Hence $T$ is complete.

**Example 2.3.9** Let $X_1,\dots,X_n$ be a sample from $\mathrm{U}(0,\theta)$, $\theta>0$. Then $T(\boldsymbol{X})=X_{(n)}$ is complete. The density of $X_{(n)}$ is $g(t;\theta)=nt^{n-1}\theta^{-n}\boldsymbol{1}_{(0,\theta)}(t)$, so $\mathbb{E}_\theta\varphi(T)=0$ for all $\theta>0$ means

$$
\frac n{\theta^n}\int_0^\theta\varphi(t)t^{n-1}\,\mathrm{d}t=0,\quad\text{i.e.}\quad\int_0^\theta\varphi(t)t^{n-1}\,\mathrm{d}t=0\qquad\text{for all }\theta>0.
$$

Differentiating with respect to $\theta$ gives $\theta^{n-1}\varphi(\theta)=0$, so $\varphi(\theta)=0$ for almost every $\theta>0$ (every point of continuity), and $\mathbb{P}_\theta(\varphi(T)=0)=1$.

These examples are instances of a general theorem.

**Theorem 2.3.2 (Completeness in Exponential Families)** Let $\boldsymbol{X}$ be a sample from an exponential family in natural form, with joint density

$$
f(\boldsymbol{x};\theta)=C(\theta)\exp\left\{\sum_{i=1}^k\theta_iT_i(\boldsymbol{x})\right\}h(\boldsymbol{x}),\qquad\theta=(\theta_1,\dots,\theta_k)\in\Theta^*.
$$

If the natural parameter space $\Theta^*$, as a subset of $\mathbb{R}^k$, has interior points, then $T(\boldsymbol{X})=(T_1(\boldsymbol{X}),\dots,T_k(\boldsymbol{X}))$ is complete for $\theta$.

The proof extends the argument of Example 2.3.8: the vanishing of $\mathbb{E}_\theta\varphi(T)$ on an open set of $\theta$ makes a multivariate **Laplace transform** vanish on an open set, hence everywhere by analyticity, and its uniqueness forces $\varphi=0$; we omit the details.

**Example 2.3.10** Let $X_1,\dots,X_n$ be a sample from $\mathcal{N}(\mu,\sigma^2)$ with $\Theta=\{(\mu,\sigma^2)\colon-\infty<\mu<\infty,\ \sigma^2>0\}$. Then $(\bar X,S^2)$ is complete for $\theta=(\mu,\sigma^2)$. By Example 2.2.6 the natural parameter space $\Theta^*=\{(\varphi_1,\varphi_2)\colon\varphi_1\in\mathbb{R},\ \varphi_2<0\}$ is an open half-plane, so by Theorem 2.3.2 $(\sum X_i,\sum X_i^2)$ is complete, and $(\bar X,S^2)$, a function of it, is complete as well. If $\sigma^2$ is known, the family is a one-parameter exponential family with natural parameter $\mu/\sigma^2$ ranging over $\mathbb{R}$ and $T=\sum X_i$, so $\bar X$ is complete; if $\mu$ is known, the natural parameter is $-1/(2\sigma^2)\in(-\infty,0)$ and $\sum(X_i-\mu)^2$ is complete.

**Example 2.3.11 (A Sufficient Statistic That Is Not Complete)** Let $X_1,\dots,X_n$ ($n\ge2$) be a sample from $\mathrm{U}(\theta-\frac12,\theta+\frac12)$, $\theta\in\mathbb{R}$. Since

$$
f(\boldsymbol{x};\theta)=\boldsymbol{1}_{\{\theta-1/2<x_{(1)}\}}\boldsymbol{1}_{\{x_{(n)}<\theta+1/2\}},
$$

$T(\boldsymbol{X})=(X_{(1)},X_{(n)})$ is sufficient by the factorization theorem. It is not complete: we must find $\varphi$ with $\mathbb{E}_\theta\varphi(T)=0$ but $\mathbb{P}_\theta(\varphi(T)=0)\ne1$. Let $Y_i=X_i-(\theta-\frac12)$; then $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathrm{U}(0,1)$, whose distribution does not involve $\theta$, and so the range $Z=X_{(n)}-X_{(1)}=Y_{(n)}-Y_{(1)}$ has a distribution free of $\theta$, with $\mathbb{E}[Z]=\frac{n-1}{n+1}$. Hence $\varphi(T)=X_{(n)}-X_{(1)}-\frac{n-1}{n+1}$ has expectation $0$ for every $\theta$, but it is a continuous random variable and is not $0$ with probability one. (Equally well, choose constants $a<b$ with $\mathbb{P}(Z<a)=\mathbb{P}(Z>b)>0$ and let $\varphi=1$ on $\{Z<a\}$, $-1$ on $\{Z>b\}$ and $0$ otherwise; this $\varphi$ is bounded.)

The example shows the typical obstruction: a sufficient statistic fails to be complete when some nonconstant function of it has a distribution that does not depend on $\theta$.

### 2.3.5. Bounded Completeness and Basu's Theorem

**Definition 2.3.4 (Bounded Complete Statistic)** If the implication of Definition 2.3.3 holds for every bounded function $\varphi$, then $T(\boldsymbol{X})$ is called a **bounded complete statistic** for $\theta$.

A complete statistic is bounded complete, since the condition is required for fewer functions; the converse fails in general. The bounded $\varphi$ constructed at the end of Example 2.3.11 shows that $(X_{(1)},X_{(n)})$ is not even bounded complete.

**Definition 2.3.5 (Ancillary Statistic)** A statistic $V(\boldsymbol{X})$ whose distribution does not depend on $\theta$ is called an **ancillary statistic**.

An ancillary statistic alone tells us nothing about $\theta$. The range in Example 2.3.11 is ancillary. Basu's theorem says that an ancillary statistic is independent of every bounded complete sufficient statistic.

**Theorem 2.3.3 (Basu's Theorem)** Let $T(\boldsymbol{X})$ be a bounded complete sufficient statistic for $\theta$. If the distribution of $V(\boldsymbol{X})$ does not depend on $\theta$, then $V(\boldsymbol{X})$ and $T(\boldsymbol{X})$ are independent for every $\theta\in\Theta$.

**Proof** Fix a set $B$ and let $p_B=\mathbb{P}_\theta(V\in B)$, which does not depend on $\theta$ because $V$ is ancillary. Let $\eta(T)=\mathbb{P}(V\in B\mid T)$; since $T$ is sufficient, the conditional distribution of the sample given $T$, and hence $\eta$, does not depend on $\theta$, so $\eta(T)$ is a statistic. It is bounded, and $\mathbb{E}_\theta[\eta(T)-p_B]=\mathbb{P}_\theta(V\in B)-p_B=0$ for every $\theta$. By bounded completeness $\eta(T)=p_B$ with probability one, that is, $\mathbb{P}(V\in B\mid T)=\mathbb{P}(V\in B)$, so $V$ is independent of $T$. $\square$

The theorem is due to D. Basu (1955). It is a convenient way to prove independence without computing joint distributions.

**Example 2.3.12** Let $X_1,\dots,X_n$ be a sample from $\mathcal{N}(\theta,1)$, $R(\boldsymbol{X})=X_{(n)}-X_{(1)}$ the sample range and $T(\boldsymbol{X})=\bar X$. Then $R$ and $T$ are independent. By Examples 2.3.2 and 2.3.8, $T$ is sufficient and complete. Let $Y_i=X_i-\theta$; then $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$, whose distribution does not depend on $\theta$, so the distribution of $R(\boldsymbol{X})=Y_{(n)}-Y_{(1)}$ does not depend on $\theta$. By Basu's theorem $T$ and $R$ are independent.

The same argument gives a second proof of Theorem 2.1.3(3). Fix $\sigma^2$ and regard $\{\mathcal{N}(\mu,\sigma^2)\colon\mu\in\mathbb{R}\}$ as the model; $\bar X$ is complete and sufficient for $\mu$ (Example 2.3.10), and $S^2$ is a function of the deviations $X_i-\mu$, whose distribution is free of $\mu$, so $S^2$ is ancillary. Hence $\bar X$ and $S^2$ are independent for every $\mu$, and $\sigma^2$ was arbitrary. Without normality the conclusion fails, as the following simulation of the sample mean and range shows.

![Scatter plots of sample mean against sample range for 3000 samples of size 10: uncorrelated for normal samples, clearly dependent for exponential samples](./plots/basu-independence.py)

## Summary

| Topic | Key results |
|---|---|
| Normal samples | $\bar X\sim\mathcal{N}(a,\sigma^2/n)$, $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$, $\bar X$ and $S^2$ independent |
| $\chi^2_r$ | sum of $r$ squared iid $\mathcal{N}(0,1)$; mean $r$, variance $2r$; additive |
| $t_r$ | $X/\sqrt{Y/r}$; symmetric, heavy tails; $t_1$ Cauchy; $t_r\to\mathcal{N}(0,1)$ |
| $F_{r_1,r_2}$ | $(X/r_1)/(Y/r_2)$; $1/F\sim F_{r_2,r_1}$; $t_r^2\sim F_{1,r}$; $F_{r_1,r_2,1-\alpha}=1/F_{r_2,r_1,\alpha}$ |
| Pivotal quantities | $\sqrt n(\bar X-a)/S\sim t_{n-1}$; two-sample $t$ with pooled $S_w$; variance ratio $F_{m-1,n-1}$; $2\lambda\sum X_i\sim\chi^2_{2n}$ |
| Limiting distributions | CLT plus Slutsky: $\sqrt n(\bar X-a)/S\xrightarrow{d}\mathcal{N}(0,1)$ for any finite-variance population |
| Exponential family | $C(\theta)\exp\{\sum Q_i(\theta)T_i(x)\}h(x)$; fixed support; convex $\Theta^*$; $\mathbb{E}T_i=-\partial_iD$, $\operatorname{Cov}(T_i,T_j)=-\partial_i\partial_jD$ |
| Sufficiency | conditional law of the sample given $T$ free of $\theta$; factorization $f=g(t(\boldsymbol{x});\theta)h(\boldsymbol{x})$ |
| Completeness | $\mathbb{E}_\theta\varphi(T)=0$ for all $\theta$ implies $\varphi(T)=0$ a.s.; holds for $(T_1,\dots,T_k)$ in exponential families with interior points |
| Basu's theorem | bounded complete sufficient statistic $\perp$ ancillary statistic |
