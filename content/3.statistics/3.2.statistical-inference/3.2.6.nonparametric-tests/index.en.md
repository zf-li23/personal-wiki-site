---
title: Nonparametric Hypothesis Testing
description: Tests that do not assume a parametric form for the population — the sign test, the Wilcoxon signed-rank and rank-sum tests, Pearson's chi-squared goodness-of-fit test, independence and homogeneity tests for contingency tables, and the Kolmogorov–Smirnov and Shapiro–Wilk tests of normality.
---

The tests of [3.2.5](/3.2.5) assume that the population belongs to a family $\{f(x;\theta)\colon \theta\in\Theta\}$ whose form is known, and they test a statement about the finite-dimensional parameter $\theta$. Their critical values come from the exact distribution of a statistic under that model, typically a normal model, and they can be misleading when the model is wrong: a single outlier can change the conclusion of a $t$ test. This chapter develops tests whose validity does not depend on the mathematical form of the population distribution. Two ideas recur. The first replaces the observations by their signs or ranks, whose null distribution is the same for every continuous population; this gives the sign test and the Wilcoxon tests (§6.2), the nonparametric counterparts of the one- and two-sample $t$ tests. The second compares observed counts with the counts expected under the null hypothesis and relies on large-sample theory, in particular on the **central limit theorem** ([3.1.13](/3.1.13)); this gives Pearson's $\chi^2$ test of goodness of fit (§6.3) and its applications to contingency tables (§6.4). Section 6.5 treats the most common goodness-of-fit question, whether data are normal, with the Kolmogorov–Smirnov test, the Shapiro–Wilk test and the normal Q–Q plot. Nonparametric statistics as a subject is developed further in [3.6](/3.6).

## 6.1. Parametric and Nonparametric Tests

All the problems of [3.2.5](/3.2.5) are parametric. For example: given a sample $\boldsymbol{X}=(X_1,\dots,X_n)$ from $\mathcal{N}(\theta,\sigma^2)$ with $\sigma^2$ known, test $H_0\colon\theta=\theta_0$ against $H_1\colon\theta\ne\theta_0$; from $\mathrm{Ber}(\theta)$, test $H_0\colon\theta\le\theta_0$ against $H_1\colon\theta>\theta_0$; from $\mathrm{Poi}(\theta)$, test $H_0\colon\theta\ge\theta_0$ against $H_1\colon\theta<\theta_0$.

**Definition 6.1.1 (Parametric and Nonparametric Tests)** A testing problem is a **parametric hypothesis test** if the distribution function (or density) of the population is known up to a parameter, $\{f(x;\theta)\colon\theta\in\Theta\}$ with $\Theta$ finite-dimensional, and the hypotheses state whether $\theta$ lies in a specified subset of $\Theta$. It is a **nonparametric hypothesis test** if the form of the population distribution is essentially unknown; the test procedure must then not depend on a mathematical formula for the population distribution.

The hypotheses of a nonparametric test may concern a location parameter such as the median, the equality of two distributions, independence of two variables, or the distribution itself, for instance "the sample comes from a normal distribution". The following five examples motivate the methods of this chapter; they are analyzed in the later sections.

**Example 6.1.1 (Two Soporific Drugs)** Each of $10$ subjects receives Drug 1 and, on another occasion, Drug 2; the observations are the hours of extra sleep.

| Subject | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Drug 1 ($X_i$) | 1.9 | −1.6 | −0.2 | −1.2 | −0.1 | 3.4 | 3.7 | 0.8 | 0.0 | 2.0 |
| Drug 2 ($Y_i$) | 0.7 | 0.8 | 1.1 | 0.1 | −0.1 | 4.4 | 5.5 | 1.6 | 4.6 | 3.4 |
| $Z_i=Y_i-X_i$ | −1.2 | 2.4 | 1.3 | 1.3 | 0.0 | 1.0 | 1.8 | 0.8 | 4.6 | 1.4 |

Is one drug more effective? These are paired data (a paired comparison): $X_1,\dots,X_n$ are independent and so are $Y_1,\dots,Y_n$, but $X_i$ and $Y_i$ come from the same subject and are dependent, so the two-sample $t$ test does not apply. We work with the differences $Z_i$, which are i.i.d. If they are normal, the one-sample $t$ test of $H_0\colon\mathbb{E}Z_i=0$ applies; if little is known about their distribution, we use the sign test or the Wilcoxon signed-rank test, with the null hypothesis "for every subject, the difference is equally likely to be positive or negative".

**Example 6.1.2 (Survival of Mice)** Sixteen mice underwent surgery; $7$ of them, chosen at random, received a new treatment and the other $9$ served as controls. Survival times in days:

| Treatment ($X_i$) | 16 | 23 | 38 | 94 | 99 | 141 | 197 | | |
|---|---|---|---|---|---|---|---|---|---|
| Control ($Y_j$) | 10 | 27 | 31 | 40 | 46 | 50 | 52 | 104 | 146 |

Assume $X_1,\dots,X_m\overset{\text{iid}}{\sim}F_X$ and $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}F_Y$, independent of each other, and test whether the treatment changes survival. If $F_X=\mathcal{N}(\mu_1,\sigma^2)$ and $F_Y=\mathcal{N}(\mu_2,\sigma^2)$, the two-sample $t$ test applies; if the forms are unknown but $m,n$ are large, the normal approximation for $\bar X-\bar Y$ gives a large-sample test. With unknown forms and small samples we use the Wilcoxon rank-sum test (§6.2.4).

**Example 6.1.3 (Mendel's Peas)** In Mendel's hybrid experiment $556$ peas were classified by shape and color:

| Type | round, yellow | angular, yellow | round, green | angular, green |
|---|---|---|---|---|
| Observed count | 315 | 101 | 108 | 32 |
| Theoretical ratio | 9 | 3 | 3 | 1 |

Writing $X=i$ when a pea is of type $i$, the theory predicts $H_0\colon \mathbb{P}(X=1)=\frac{9}{16}$, $\mathbb{P}(X=2)=\mathbb{P}(X=3)=\frac{3}{16}$, $\mathbb{P}(X=4)=\frac{1}{16}$. Do the data fit this distribution? This calls for a goodness-of-fit test (§6.3).

**Example 6.1.4 (Smoking and Lung Cancer)** One hundred people are classified by smoking ($X$) and lung cancer ($Y$):

| | lung cancer | no lung cancer | total |
|---|---|---|---|
| smoking | 39 | 15 | 54 |
| non-smoking | 21 | 25 | 46 |
| total | 60 | 40 | 100 |

The cancer rate is $72.22\%$ among smokers and $45.65\%$ among non-smokers. Are smoking and lung cancer related? The null hypothesis is that $X$ and $Y$ are independent; such a two-way table of counts is a contingency table (§6.4).

**Example 6.1.5 (House Prices)** Normality is a basic assumption in many analyses. Are the sale prices $Y_i$ in a large data set of house sales (the Ames housing data) normally distributed? Their histogram is strongly skewed to the right. The null hypothesis "there exist $\mu$ and $\sigma^2$ such that $Y_i\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$" is a nonparametric hypothesis about the whole distribution, tested in §6.5.

## 6.2. The Sign Test and the Wilcoxon Tests

### 6.2.1. When the t Test Goes Wrong

The one-sample $t$ test of $H_0\colon\mu=\mu_0$ and the two-sample $t$ test of $H_0\colon\mu_1-\mu_2=0$ are derived for normal data. They are fairly robust and often work well without exact normality, but not always: an extreme outlier inflates the sample variance and can destroy the evidence.

**Example 6.2.1** Compare two samples with the (Welch) two-sample $t$ test.

| | Sample 1 | Sample 2 | means | variances | $t$ | $p$-value |
|---|---|---|---|---|---|---|
| (a) | $1,2,\dots,10$ | $7,8,\dots,20$ | 5.5, 13.5 | 9.2, 17.5 | $-5.435$ | $0.000019$ |
| (b) | $1,2,\dots,10$ | $7,8,\dots,20,\ 200$ | 5.5, 25.9 | 9.2, 2335 | $-1.633$ | $0.12$ |

Adding the single value $200$, which makes the second sample look even larger, turns a highly significant difference into an insignificant one. A test based on ranks is unaffected by how extreme the outlier is: the Wilcoxon rank-sum test of §6.2.4 gives $p\approx0.0003$ in case (a) and $p\approx0.0002$ in case (b).

### 6.2.2. The Sign Test

Let $Z_1,\dots,Z_n$ be i.i.d. (in Example 6.1.1, $Z_i=Y_i-X_i$) and define the signs

$$
S_i=\begin{cases}1, & Z_i>0,\\ -1, & Z_i<0,\\ 0, & Z_i=0.\end{cases}
$$
"The two drugs have the same effect" is formalized as: for every subject the difference is equally likely to be positive or negative, $\mathbb{P}(S_i=1)=\mathbb{P}(S_i=-1)$. This holds, for example, when the distribution of $Z_i$ is symmetric about $0$, and in general it says that $0$ is a median of $Z_i$. Discard the observations with $Z_i=0$, let $n_+$ and $n_-$ be the numbers of positive and negative $Z_i$, and $n_0=n_++n_-$. Conditionally on $n_0$, $n_+\sim\mathrm{Bin}(n_0,\theta)$ with $\theta=\mathbb{P}(Z_i>0\mid Z_i\ne0)$, and the problem becomes the binomial test

$$
H_0\colon\theta=0.5\quad\longleftrightarrow\quad H_1\colon\theta\ne0.5 .
$$

**Definition 6.2.1 (Sign Test)** The **sign test** at level $\alpha$ rejects $H_0$ when $n_+\ge c$ or $n_+\le d$, where $c$ is the smallest integer with

$$
\sum_{i=c}^{n_0}\binom{n_0}{i}0.5^{n_0}\le\frac{\alpha}{2},\qquad d=n_0-c .
$$
Equivalently, with $x_0=\min\{n_+,\,n_0-n_+\}$ the exact $p$-value is

$$
p=\sum_{i=0}^{x_0}\binom{n_0}{i}0.5^{n_0}+\sum_{i=n_0-x_0}^{n_0}\binom{n_0}{i}0.5^{n_0}
$$
(defined as $p=1$ if $n_0$ is even and $n_+=n_0/2$), and $H_0$ is rejected when $p<\alpha$.

For large $n_0$, the **central limit theorem** applied to $n_+\sim\mathrm{Bin}(n_0,0.5)$ under $H_0$ gives

$$
U=\frac{n_+-\mathbb{E}n_+}{\sqrt{\operatorname{Var}(n_+)}}=\frac{n_+-0.5n_0}{\sqrt{n_0/4}}=\frac{2n_+-n_0}{\sqrt{n_0}}\xrightarrow[n_0\to\infty]{d}\mathcal{N}(0,1),
$$
so the rejection region $\{\lvert U\rvert>z_{\alpha/2}\}$ has level approximately $\alpha$, and with $u$ the observed value of $U$ the approximate $p$-value is $p=\mathbb{P}(\lvert \mathcal{N}(0,1)\rvert>\lvert u\rvert)=2\big(1-\Phi(\lvert u\rvert)\big)$, where $\Phi$ is the standard normal distribution function.

**Example 6.2.2 (Drug Data)** In Example 6.1.1, subject 5 has $Z_5=0$, so $n_0=9$ and $n_+=8$. The exact $p$-value is the probability of $0,1,8$ or $9$ positive signs,

$$
p=\frac{1+9+9+1}{2^9}=0.039<0.05,
$$
so $H_0$ is rejected at level $0.05$. The normal approximation gives $u=(16-9)/3=2.33$ and $p\approx0.020$.

**Example 6.2.3 (Two Recipes)** A beverage is sold in a traditional recipe A and a modified recipe B. Of $10000$ returned questionnaires, $5150$ prefer A and $4850$ prefer B. A support rate of $0.515$ is only slightly above $0.5$; is the difference significant? With $n_+=5150$ and $n_0=10000$ the sample is large, and

$$
U=\frac{2n_+-n_0}{\sqrt{n_0}}=\frac{10300-10000}{100}=3,\qquad p=\mathbb{P}(\lvert U\rvert>3\mid H_0)\approx0.0027<0.01 .
$$
At level $0.01$ we reject the hypothesis that the two recipes are equally popular: the survey shows a significant preference for the traditional recipe. With a large sample, a small difference in proportions can be statistically significant.

The sign test also tests a hypothesis about the median $m_{0.5}$ of a single population: apply it to $Y_i=X_i-m_0$.

**Example 6.2.4 (Fineness of Vinylon)** The deniers (fineness) of $100$ vinylon fibers are grouped as follows.

| Denier | 1.26 | 1.29 | 1.32 | 1.35 | 1.38 | 1.41 | 1.44 | 1.47 | 1.50 | 1.53 |
|---|---|---|---|---|---|---|---|---|---|---|
| Frequency | 1 | 4 | 7 | 22 | 23 | 25 | 10 | 6 | 1 | 1 |

Test $H_0\colon m_{0.5}=1.40$ against $H_1\colon m_{0.5}\ne1.40$ at $\alpha=0.05$. With $Y_i=X_i-1.40$, under $H_0$ we have $\mathbb{P}(Y_i>0)=\mathbb{P}(Y_i<0)=0.5$; no $Y_i$ is zero, so $n=n_++n_-=100$ and $n_+\sim\mathrm{Bin}(100,\theta)$, and we test $\theta=0.5$. The large-sample rejection region is $\{\lvert 2n_+-n\rvert/\sqrt n>z_{0.025}=1.96\}$. Here $n_+=25+10+6+1+1=43$ and $\lvert 86-100\rvert/10=1.4<1.96$: there is not enough evidence to reject $H_0$.

The one-sided problem $H_0\colon\theta\le0.5$ against $H_1\colon\theta>0.5$ is treated in the same way, rejecting for large $n_+$. The sign test is the simplest test that the population median is zero and the nonparametric analogue of the one-sample $t$ test. Its drawback is that it ignores the magnitudes completely, which makes it inefficient (of low power). Many nonparametric methods instead replace the raw values by their ranks, the positions in the ordered sample: the data $3.2, 2.4, 5, 3.8$ have ranks $2, 1, 4, 3$. In case of ties, mid-ranks (average ranks) are used: the data $105, 120, 120, 121$ have ranks $1, 2.5, 2.5, 4$.

### 6.2.3. The Wilcoxon Signed-Rank Test

The signed-rank test keeps the signs and adds the ranks of the magnitudes. For the paired data of Example 6.1.1: compute $Z_i=Y_i-X_i$ and its sign $S_i$; discard the observations with $Z_i=0$, leaving $n_0$ of them; let $R_i$ be the rank of $\lvert Z_i\rvert$ among $\lvert Z_1\rvert,\dots,\lvert Z_{n_0}\rvert$; the signed ranks are $S_iR_i$.

**Definition 6.2.2 (Wilcoxon Signed-Rank Test)** The **Wilcoxon signed-rank test** of the hypothesis that the distribution of $Z_i$ is symmetric about $0$ uses the sum of the positive signed ranks

$$
W^+=\sum_{i=1}^{n_0}R_i\boldsymbol{1}_{\{S_i>0\}}
$$
(equivalently $W=\sum_{i=1}^{n_0}S_iR_i=2W^+-\frac{n_0(n_0+1)}{2}$) and rejects $H_0$ when $W^+\ge c$ or $W^+\le d$, where $d=\frac{n_0(n_0+1)}{2}-c$ and $c$ is chosen from tables so that the type I error is at most $\alpha$.

**Theorem 6.2.1** Let $Z_1,\dots,Z_{n_0}$ be i.i.d. with a continuous distribution symmetric about $0$. Then $W^+$ has the same distribution as $\sum_{k=1}^{n_0}k\,I_k$ with $I_1,\dots,I_{n_0}\overset{\text{iid}}{\sim}\mathrm{Ber}(1/2)$; in particular its distribution does not depend on the distribution of $Z_i$, and

$$
\mathbb{E}W^+=\frac{n_0(n_0+1)}{4},\qquad \operatorname{Var}(W^+)=\frac{n_0(n_0+1)(2n_0+1)}{24}.
$$

**Proof** For a continuous symmetric distribution, $\operatorname{sgn}(Z_i)$ and $\lvert Z_i\rvert$ are independent and $\mathbb{P}(Z_i>0)=1/2$. Hence the signs are i.i.d. $\pm1$ with probability $1/2$ each and independent of the vector of magnitudes, and therefore of the ranks. Let $I_k$ indicate that the observation with rank $k$ is positive; then $I_1,\dots,I_{n_0}$ are i.i.d. $\mathrm{Ber}(1/2)$ and $W^+=\sum_k kI_k$. Thus $\mathbb{E}W^+=\frac12\sum_k k=\frac{n_0(n_0+1)}{4}$ and $\operatorname{Var}(W^+)=\frac14\sum_k k^2=\frac{n_0(n_0+1)(2n_0+1)}{24}$. $\square$

The exact null distribution of $W^+$ is that of a sum of a random subset of $\{1,\dots,n_0\}$; it is symmetric about $n_0(n_0+1)/4$. If $w^+$ is the observed value and $a=\max\{w^+,\ \frac{n_0(n_0+1)}{2}-w^+\}$, the exact $p$-value is

$$
p=\mathbb{P}\Big(W^+\ge a\ \text{or}\ W^+\le\frac{n_0(n_0+1)}{2}-a\ \Big|\ H_0\Big).
$$
For large $n_0$, $U=\big(W^+-\mathbb{E}W^+\big)/\sqrt{\operatorname{Var}(W^+)}\xrightarrow{d}\mathcal{N}(0,1)$ under $H_0$; we reject when $\lvert U\rvert>z_{\alpha/2}$, and with $u$ the observed value the approximate $p$-value is $\mathbb{P}(\lvert\mathcal{N}(0,1)\rvert>\lvert u\rvert)$. Using $W$ instead of $W^+$ gives the same test.

**Example 6.2.5 (Drug Data)** The nonzero differences in Example 6.1.1 have absolute values $1.2, 2.4, 1.3, 1.3, 1.0, 1.8, 0.8, 4.6, 1.4$ with ranks $3, 8, 4.5, 4.5, 2, 7, 1, 9, 6$; only the first difference is negative. Hence $W^+=45-3=42$ and $W=42-3=39$. With $n_0=9$, $\mathbb{E}W^+=22.5$ and $\operatorname{Var}(W^+)=71.25$, so $u=19.5/\sqrt{71.25}=2.31$ and the approximate $p$-value is $0.021$ (R's `wilcox.test`, which corrects the variance for the tied pair, reports $0.0208$). We reject $H_0$ at level $0.05$ and conclude that Drug 2 increases sleep more than Drug 1.

```r
x <- c(1.9, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0)
y <- c(0.7, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4)
wilcox.test(y - x, correct = FALSE, exact = FALSE)   # V = 42, p-value = 0.02077
wilcox.test(y, x, correct = FALSE, exact = FALSE, paired = TRUE)   # the same test
```

The signed-rank test assumes that the distribution of the differences is symmetric; it then tests whether the center of symmetry, which is both the mean and the median, is zero. The three one-sample procedures differ in how much of the data they use: the $t$ test uses the values of the observations, the sign test only their signs, and the signed-rank test lies in between, using signs and ranks.

### 6.2.4. The Wilcoxon Rank-Sum Test

For two independent samples as in Example 6.1.2, assume moreover that the two distributions have the same shape and differ only in location (a shift model): $X_1,\dots,X_m\overset{\text{iid}}{\sim}F(x)$ and $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}F(x-\theta)$, so that $Y$ has the distribution of $X+\theta$ and $\theta=\mathbb{E}Y-\mathbb{E}X$ when the means exist. The problem is nonparametric because $F$ is unknown. Test

$$
H_0\colon\theta=0\quad\longleftrightarrow\quad H_1\colon\theta\ne0 .
$$
Let $N=m+n$ and let $R_1,\dots,R_n$ be the ranks of $Y_1,\dots,Y_n$ in the pooled sample $X_1,\dots,X_m,Y_1,\dots,Y_n$.

**Definition 6.2.3 (Wilcoxon Rank-Sum Test)** The **Wilcoxon rank-sum test** (Wilcoxon 1945; equivalent to the Mann–Whitney $U$ test, hence also called the Wilcoxon–Mann–Whitney test) uses the rank-sum statistic

$$
W=R_1+\cdots+R_n
$$
and rejects $H_0$ when $W\le c$ or $W\ge d$, with $c,d$ chosen so that $\mathbb{P}(W\le c\ \text{or}\ W\ge d\mid H_0)\le\alpha$. For small $m,n$ the constants are tabulated.

**Theorem 6.2.2** Under $H_0$, with $F$ continuous, the vector of ranks is uniformly distributed over the $N(N-1)\cdots(N-n+1)$ ordered $n$-tuples of distinct integers in $\{1,\dots,N\}$:

$$
\mathbb{P}(R_1=r_1,\dots,R_n=r_n)=\frac{1}{N(N-1)\cdots(N-n+1)}.
$$
Consequently

$$
\mathbb{E}W=\frac{n(N+1)}{2},\qquad \operatorname{Var}(W)=\frac{mn(N+1)}{12}.
$$

**Proof** Under $H_0$ the $N$ pooled observations are i.i.d. and continuous, so ties have probability zero and all $N!$ orderings are equally likely; the first claim follows. Each $R_j$ is then uniform on $\{1,\dots,N\}$, with $\mathbb{E}R_j=\frac{N+1}{2}$ and $\operatorname{Var}(R_j)=\frac{N^2-1}{12}$. By exchangeability all pairs of distinct ranks have the same covariance, and the ranks of all $N$ pooled observations sum to the constant $N(N+1)/2$; hence $0=N\operatorname{Var}(R_1)+N(N-1)\operatorname{Cov}(R_1,R_2)$, i.e. $\operatorname{Cov}(R_i,R_j)=-\frac{N+1}{12}$ for $i\ne j$. Therefore

$$
\operatorname{Var}(W)=n\frac{N^2-1}{12}-n(n-1)\frac{N+1}{12}=\frac{n(N+1)(N-n)}{12}=\frac{mn(N+1)}{12}. \qquad\square
$$

Under $H_0$ the statistic $W$ takes values around its mean $n(N+1)/2$; a positive shift $\theta$ makes the $Y$'s large and $W$ large. If $m,n$ are large, then by a central limit theorem for rank statistics

$$
W^*=\frac{W-n(N+1)/2}{\sqrt{mn(N+1)/12}}\xrightarrow[m,n\to\infty]{d}\mathcal{N}(0,1)
$$
under $H_0$. The rejection region $\{\lvert W^*\rvert>z_{\alpha/2}\}$ has level approximately $\alpha$, and the approximate $p$-value is $\mathbb{P}(\lvert\mathcal{N}(0,1)\rvert>\lvert w^*\rvert)$ for the observed value $w^*$. The one-sided problems are handled in the same way: for $H_0\colon\theta\le0$ against $H_1\colon\theta>0$ reject when $W^*\ge z_\alpha$, and for $H_0\colon\theta\ge0$ against $H_1\colon\theta<0$ reject when $W^*\le -z_\alpha$.

The Mann–Whitney form of the statistic is $W-\frac{n(n+1)}{2}$, the number of pairs $(X_i,Y_j)$ with $X_i<Y_j$; it ranges from $0$ to $mn$ and is what R reports as `W`.

**Example 6.2.6 (Mice Data)** In Example 6.1.2 the control group has $n=9$, the treatment group $m=7$, $N=16$. In the pooled ordering the control survival times have ranks $1, 4, 5, 7, 8, 9, 10, 13, 15$, so $W=72$ (R reports $72-\frac{9\cdot10}{2}=27$). Under $H_0$, $\mathbb{E}W=76.5$. From the exact null distribution, the level-$0.05$ critical values are $c=57$ and $d=96$ ($\mathbb{P}(W\le57)=\mathbb{P}(W\ge96)\approx0.021$). Since $57<72<96$, the data do not provide enough evidence to reject $H_0$; the exact $p$-value is $0.68$.

```r
x <- c(16, 23, 38, 94, 99, 141, 197)
y <- c(10, 27, 31, 40, 46, 50, 52, 104, 146)
wilcox.test(y, x)                  # W = 27, p-value = 0.6806 (exact)
wilcox.test(y, x, exact = FALSE)   # W = 27, p-value = 0.672 (normal approximation, continuity correction)
```

By default R computes an exact $p$-value when both samples have fewer than $50$ values and there are no ties, and a normal approximation otherwise.

In short, the signed-rank test is the alternative to the one-sample (or paired) $t$ test and the rank-sum test is the alternative to the two-sample $t$ test. Rank tests are attractive when the parametric assumptions are believed to be violated. Their drawback is that, being based on ranks, they say little about the size of the effect; they are most attractive when what is needed is a $p$-value.

## 6.3. Goodness-of-Fit Tests

### 6.3.1. The General Problem

Let $\boldsymbol{X}=(X_1,\dots,X_n)$ be a sample from a population $X$, and let $F$ be a given distribution function, the theoretical distribution. We wish to test

$$
H_0\colon X\sim F .
$$
In Example 6.1.3, $F$ is the distribution on $\{1,2,3,4\}$ with probabilities $\frac{9}{16},\frac{3}{16},\frac{3}{16},\frac{1}{16}$; another example is $H_0\colon X\sim\mathcal{N}(\mu,\sigma^2)$ for given $\mu,\sigma^2$. The theoretical distribution may be completely known (as in Mendel's experiment) or contain unknown parameters (as in "there exist $\mu$ and $\sigma^2$ such that $X_i\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$").

Intuitively we define a statistic $D=D(X_1,\dots,X_n;F)$ that measures the discrepancy between the data and $F$, and reject $H_0$ when $D\ge c$. In reality $X$ probably neither follows $F$ exactly nor is far from it; rather than a yes-or-no answer we report a number in $[0,1]$ that measures how well the data fit $F$.

**Definition 6.3.1 (Goodness of Fit)** Let $d_0$ be the observed value of the discrepancy $D$. The number

$$
p(d_0)=\mathbb{P}(D\ge d_0\mid H_0)
$$
is the **goodness of fit** of the data to $F$. A **goodness-of-fit test** at level $\alpha$ rejects $H_0$ if $p(d_0)<\alpha$ and accepts it if $p(d_0)\ge\alpha$.

The goodness of fit is the $p$-value of the test based on $D$. The classical choices of $D$ are Pearson's $\chi^2$ statistic (K. Pearson, 1900) and Kolmogorov's statistic (A. N. Kolmogorov, 1933; §6.5.1).

### 6.3.2. Pearson's Chi-Squared Test

Suppose the theoretical distribution is discrete,

$$
F\colon\ \mathbb{P}(X=a_i)=p_i,\quad i=1,\dots,r,\qquad p_i\ge0,\ \sum_{i=1}^r p_i=1,
$$
with known $p_i$, and test $H_0\colon\mathbb{P}(X=a_i)=p_i$, $i=1,\dots,r$. Let $v_i$ be the observed frequency of $a_i$ in the sample, so $\sum_i v_i=n$. Under $H_0$ the relative frequency $v_i/n$ converges to $p_i$ by the **law of large numbers**, so a natural discrepancy is $\sum_i c_i(v_i/n-p_i)^2$ with weights $c_i$. Pearson took $c_i=n/p_i$:

$$
K_n=\sum_{i=1}^{r}\frac{(v_i-np_i)^2}{np_i}=\sum_{i=1}^r\frac{(\text{observed}-\text{expected})^2}{\text{expected}} .
$$

**Theorem 6.3.1 (Pearson)** Under $H_0$, as $n\to\infty$, $K_n\xrightarrow{d}\chi^2_{r-1}$.

**Proof** (for $r=2$) Under $H_0$, $(v_1,\dots,v_r)\sim\mathrm{Mult}(n,\boldsymbol{p})$. For $r=2$, $v_1\sim\mathrm{Bin}(n,p_1)$, $v_2=n-v_1$ and $p_2=1-p_1$, so $v_2-np_2=-(v_1-np_1)$ and

$$
K_n=\frac{(v_1-np_1)^2}{np_1}+\frac{(v_1-np_1)^2}{np_2}=\Big(\frac{v_1-np_1}{\sqrt{np_1p_2}}\Big)^2 .
$$
By the **central limit theorem**, $(v_1-np_1)/\sqrt{np_1p_2}\xrightarrow{d}\mathcal{N}(0,1)$, hence $K_n\xrightarrow{d}\chi^2_1$ by the continuous mapping theorem. $\square$

For $r>2$ the theorem is proved with the multivariate central limit theorem (or the **characteristic function** method): $\big((v_i-np_i)/\sqrt{np_i}\big)_{i=1}^r$ converges to a normal vector whose covariance matrix is the projection $I_r-\sqrt{\boldsymbol{p}}\sqrt{\boldsymbol{p}}^{\mathsf T}$ of rank $r-1$, and the squared length of such a vector is $\chi^2_{r-1}$. One degree of freedom is lost because the counts satisfy the constraint $\sum_i v_i=n$.

The test rejects $H_0$ if $K_n>\chi^2_{r-1,\alpha}$; with $k_0$ the observed value of $K_n$, the goodness of fit is $p(k_0)=\mathbb{P}(K_n\ge k_0\mid H_0)\approx\mathbb{P}(\chi^2_{r-1}\ge k_0)$.

**Example 6.3.1 (Mendel's Peas)** In Example 6.1.3, $v_1=315$, $v_2=101$, $v_3=108$, $v_4=32$, $n=556$, and

$$
k_0=\frac{(315-556\cdot\frac{9}{16})^2}{556\cdot\frac{9}{16}}+\frac{(101-556\cdot\frac{3}{16})^2}{556\cdot\frac{3}{16}}+\frac{(108-556\cdot\frac{3}{16})^2}{556\cdot\frac{3}{16}}+\frac{(32-556\cdot\frac{1}{16})^2}{556\cdot\frac{1}{16}}=0.470 .
$$
With $r-1=3$ degrees of freedom, $p(k_0)\approx\mathbb{P}(\chi^2_3\ge0.470)=0.925$: the data fit Mendel's theory very well.

```r
chisq.test(c(315, 101, 108, 32), p = c(9, 3, 3, 1) / 16)   # X-squared = 0.47002, df = 3, p-value = 0.9254
```

If $F$ is a continuous distribution on $\mathbb{R}$, we group the data. Choose constants $-\infty=a_0<a_1<\cdots<a_{r-1}<a_r=+\infty$ that divide the line into the intervals

$$
I_1=(-\infty,a_1],\quad I_2=(a_1,a_2],\quad\dots,\quad I_r=(a_{r-1},+\infty),
$$
compute $p_j=\mathbb{P}_F(X\in I_j)=F(a_j)-F(a_{j-1})$ under $H_0$, and test $H_0\colon\mathbb{P}(X\in I_j)=p_j$, $j=1,\dots,r$, with $v_j$ the number of observations in $I_j$. By Theorem 6.3.1, $K_n=\sum_j(v_j-np_j)^2/(np_j)\xrightarrow{d}\chi^2_{r-1}$ under $H_0$.

**Remark 6.3.1** (1) The approximation requires large expected counts: as a rule, every expected frequency $np_j$ (and preferably every observed frequency) should be at least $5$; otherwise merge neighboring intervals. (2) The cut points $a_1,\dots,a_{r-1}$ must not depend on the sample; we cannot choose them after looking at where the data fall. (3) Grouping loses information, and the result depends on the chosen partition.

### 6.3.3. Theoretical Distributions with Unknown Parameters

Often $H_0$ specifies only a parametric family, $H_0\colon X\sim F(x;\boldsymbol{\theta})$ for some $\boldsymbol{\theta}=(\theta_1,\dots,\theta_s)$. Pearson (1900) proposed to estimate $\boldsymbol{\theta}$ and use the estimated probabilities $\hat p_j=p_j(\hat{\boldsymbol{\theta}})$, believing that Theorem 6.3.1 still holds. Fisher showed that the degrees of freedom must be reduced by one for each estimated parameter.

**Theorem 6.3.2 (Fisher)** If $\hat{\boldsymbol{\theta}}$ is the maximum likelihood estimator (more generally, any consistent root of the likelihood equations) of the $s$ parameters based on the grouped counts $v_1,\dots,v_r$, and regularity conditions hold, then under $H_0$

$$
K_n=\sum_{j=1}^r\frac{(v_j-n\hat p_j)^2}{n\hat p_j}\xrightarrow{d}\chi^2_{r-1-s}.
$$

**Example 6.3.2 (Compressive Strength of Concrete)** The compressive strengths (in $\mathrm{kg/cm^2}$) of $200$ concrete specimens are grouped as follows. Is the strength normally distributed ($\alpha=0.05$)?

| Interval | 190–200 | 200–210 | 210–220 | 220–230 | 230–240 | 240–250 |
|---|---|---|---|---|---|---|
| Frequency | 10 | 26 | 56 | 64 | 30 | 14 |

We test $H_0$: there exist $\mu,\sigma^2$ with $X\sim\mathcal{N}(\mu,\sigma^2)$. Using the class midpoints, the maximum likelihood estimates are

$$
\hat\mu=\bar x=\tfrac{1}{200}(195\cdot10+205\cdot26+\cdots+245\cdot14)=221,\qquad \hat\sigma^2=\tfrac{1}{200}\sum_{i=1}^{200}(x_i-\bar x)^2=12.33^2,
$$
and the problem becomes testing $H_0\colon X\sim\mathcal{N}(221,12.33^2)$. With $u_j=(a_j-221)/12.33$, the class probabilities are $\hat p_j=\Phi(u_j)-\Phi(u_{j-1})$, the two outer classes extended to $\pm\infty$:

| $j$ | interval | $v_j$ | $\hat p_j$ | $n\hat p_j$ | $(v_j-n\hat p_j)^2/(n\hat p_j)$ |
|---|---|---|---|---|---|
| 1 | $(-\infty,200]$ | 10 | 0.044 | 8.9 | 0.149 |
| 2 | $(200,210]$ | 26 | 0.142 | 28.4 | 0.199 |
| 3 | $(210,220]$ | 56 | 0.282 | 56.3 | 0.002 |
| 4 | $(220,230]$ | 64 | 0.300 | 59.9 | 0.277 |
| 5 | $(230,240]$ | 30 | 0.171 | 34.2 | 0.518 |
| 6 | $(240,+\infty)$ | 14 | 0.062 | 12.3 | 0.226 |

Thus $K_n=1.37$. Two parameters were estimated, so the degrees of freedom are $6-1-2=3$, and the goodness of fit is $p\approx\mathbb{P}(\chi^2_3>1.37)=0.71>\alpha$. There is not enough evidence to reject normality. (Strictly, Theorem 6.3.2 requires the estimates from the grouped data; the midpoint estimates used here are a standard and close approximation.)

## 6.4. Contingency Tables: Independence and Homogeneity

### 6.4.1. Test of Independence

In Example 6.1.4 let $X=1$ (smoking) or $2$ (non-smoking) and $Y=1$ (lung cancer) or $2$ (no lung cancer). In general let $X$ take the values $1,\dots,r$ and $Y$ the values $1,\dots,s$, with $p_{ij}=\mathbb{P}(X=i,Y=j)$, $\sum_i\sum_j p_{ij}=1$, and marginal probabilities $p_{i\cdot}=\sum_j p_{ij}$, $p_{\cdot j}=\sum_i p_{ij}$. A sample of size $n$ is cross-classified into an $r\times s$ *contingency table* of counts $n_{ij}$, with row sums $n_{i\cdot}$ and column sums $n_{\cdot j}$:

| $X\backslash Y$ | $1$ | $\cdots$ | $j$ | $\cdots$ | $s$ | $\Sigma$ |
|---|---|---|---|---|---|---|
| $1$ | $n_{11}$ | $\cdots$ | $n_{1j}$ | $\cdots$ | $n_{1s}$ | $n_{1\cdot}$ |
| $\vdots$ | $\vdots$ | | $\vdots$ | | $\vdots$ | $\vdots$ |
| $r$ | $n_{r1}$ | $\cdots$ | $n_{rj}$ | $\cdots$ | $n_{rs}$ | $n_{r\cdot}$ |
| $\Sigma$ | $n_{\cdot1}$ | $\cdots$ | $n_{\cdot j}$ | $\cdots$ | $n_{\cdot s}$ | $n$ |

The *test of independence* tests

$$
H_0\colon p_{ij}=p_{i\cdot}\,p_{\cdot j},\qquad i=1,\dots,r,\ j=1,\dots,s,
$$
which is a goodness-of-fit problem for the multinomial distribution of the $rs$ cells, with the unknown parameters $p_{1\cdot},\dots,p_{r\cdot}$ and $p_{\cdot1},\dots,p_{\cdot s}$ (subject to $\sum_ip_{i\cdot}=\sum_jp_{\cdot j}=1$). Under $H_0$ the likelihood is

$$
L=c\prod_{i=1}^r\prod_{j=1}^s(p_{i\cdot}p_{\cdot j})^{n_{ij}}=c\Big(\prod_{i=1}^r p_{i\cdot}^{n_{i\cdot}}\Big)\Big(\prod_{j=1}^s p_{\cdot j}^{n_{\cdot j}}\Big),\qquad c=\frac{n!}{\prod_i\prod_j n_{ij}!},
$$
which factors into two multinomial likelihoods, so the maximum likelihood estimates are

$$
\hat p_{i\cdot}=\frac{n_{i\cdot}}{n},\qquad \hat p_{\cdot j}=\frac{n_{\cdot j}}{n}.
$$
The estimated expected count of cell $(i,j)$ is $n\hat p_{i\cdot}\hat p_{\cdot j}=n_{i\cdot}n_{\cdot j}/n$, and Pearson's statistic is

$$
K_n=\sum_{i=1}^r\sum_{j=1}^s\frac{\big(n_{ij}-n_{i\cdot}n_{\cdot j}/n\big)^2}{n_{i\cdot}n_{\cdot j}/n}=n\Big(\sum_{i=1}^r\sum_{j=1}^s\frac{n_{ij}^2}{n_{i\cdot}n_{\cdot j}}-1\Big).
$$

**Theorem 6.4.1** Under $H_0$, as $n\to\infty$,

$$
K_n\xrightarrow{d}\chi^2_{rs-1-(r+s-2)}=\chi^2_{(r-1)(s-1)} .
$$

This is Theorem 6.3.2 with $rs$ cells and $(r-1)+(s-1)$ estimated parameters. The test rejects $H_0$ if $K_n>\chi^2_{(r-1)(s-1),\alpha}$, or equivalently if $p(k_0)\approx\mathbb{P}(\chi^2_{(r-1)(s-1)}\ge k_0)<\alpha$.

**Example 6.4.1 (Smoking and Lung Cancer)** For the $2\times2$ table of Example 6.1.4, $K_n=7.307$ with $1$ degree of freedom and $p=0.0069$. Smoking and lung cancer are significantly associated.

```r
chisq.test(matrix(c(39, 21, 15, 25), ncol = 2), correct = FALSE)   # X-squared = 7.3068, df = 1, p-value = 0.00687
```

**Example 6.4.2 (Age and Television)** Viewers are classified by favorite program ($X$) and age group ($Y$):

| $X\backslash Y$ | old | middle-aged | young |
|---|---|---|---|
| opera | 20 | 10 | 2 |
| song and dance | 5 | 20 | 35 |
| ball games | 2 | 10 | 20 |

For this $3\times3$ table, $K_n=47.82$ with $(3-1)(3-1)=4$ degrees of freedom, and $p\approx1.0\times10^{-9}$: program preference strongly depends on age.

### 6.4.2. Test of Homogeneity

Now consider $r$ populations $X^{(1)},\dots,X^{(r)}$, each classified into the same $s$ categories $a_1,\dots,a_s$, and a sample of predetermined size $n_{i\cdot}$ from population $i$; $n_{ij}$ is the number of observations from population $i$ in category $a_j$. The table looks the same as before, but the row sums $n_{i\cdot}$ are now fixed by the design and not random. With $p_i(j)=\mathbb{P}(X^{(i)}=a_j)$, the *test of homogeneity* tests whether the populations have the same distribution,

$$
H_0\colon p_1(j)=p_2(j)=\cdots=p_r(j),\qquad j=1,\dots,s .
$$

If the common distribution is completely specified, $H_0\colon p_i(j)=p_j^0$ with known $p_j^0$, $\sum_jp_j^0=1$, use

$$
K_n=\sum_{i=1}^r\sum_{j=1}^s\frac{(n_{ij}-n_{i\cdot}p_j^0)^2}{n_{i\cdot}p_j^0}\xrightarrow{d}\chi^2_{r(s-1)}\qquad(n_{i\cdot}\to\infty,\ i=1,\dots,r):
$$
the $r$ inner sums are independent Pearson statistics, each with $s-1$ degrees of freedom by Theorem 6.3.1.

If the common distribution $p_j=p_i(j)$ is unknown, its $s-1$ free parameters are estimated by $\hat p_j=n_{\cdot j}/n$, and the statistic is the same as for independence,

$$
K_n=n\Big(\sum_{i=1}^r\sum_{j=1}^s\frac{n_{ij}^2}{n_{i\cdot}n_{\cdot j}}-1\Big)\xrightarrow{d}\chi^2_{(r-1)(s-1)}\qquad(n_{i\cdot}\to\infty,\ i=1,\dots,r),
$$
with $r(s-1)-(s-1)=(r-1)(s-1)$ degrees of freedom. We reject $H_0$ if $K_n>\chi^2_{(r-1)(s-1),\alpha}$. Independence and homogeneity are thus tested by the same computation; they differ in the sampling design and in the interpretation.

**Example 6.4.3 (Three Shifts)** A factory works in three shifts, and its products are graded $1,\dots,6$. To check whether the three shifts produce the same quality, $83$, $95$ and $83$ products are sampled from shifts A, B and C:

| | 1 | 2 | 3 | 4 | 5 | 6 | $\Sigma$ |
|---|---|---|---|---|---|---|---|
| A | 11 | 23 | 8 | 5 | 18 | 18 | 83 |
| B | 17 | 29 | 10 | 17 | 7 | 15 | 95 |
| C | 6 | 21 | 8 | 24 | 15 | 9 | 83 |
| $\Sigma$ | 34 | 73 | 26 | 46 | 40 | 42 | 261 |

Test $H_0$: the quality distributions of the three shifts are the same, at $\alpha=0.01$. Here $r=3$, $s=6$, $(r-1)(s-1)=10$ and $\chi^2_{10,0.01}=23.21$. The statistic is $K_n=26.27>23.21$, so $H_0$ is rejected; $p(k_0)=\mathbb{P}(\chi^2_{10}\ge26.27)=0.0034<0.01$.

## 6.5. Tests of Normality

Testing the normality assumption (Example 6.1.5) is a goodness-of-fit problem in which the theoretical distribution has the unknown parameters $\mu,\sigma^2$: $H_0$: there exist $\mu,\sigma^2$ such that $X_i\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$. Pearson's test with estimated parameters (Example 6.3.2) is one option; this section presents tests that do not group the data.

### 6.5.1. The Kolmogorov–Smirnov Test

Let $\boldsymbol{X}=(X_1,\dots,X_n)$ be a sample from an unknown distribution function $F$, and let $F_0$ be a known continuous distribution function, for example that of $\mathcal{N}(0,1)$. Test

$$
H_0\colon F(x)=F_0(x)\quad\text{for all }x\in\mathbb{R}.
$$
The empirical distribution function $F_n(x)=\frac1n\#\{i\colon X_i\le x\}$ ([3.2.1](/3.2.1)) is a good estimate of $F$.

**Definition 6.5.1 (Kolmogorov–Smirnov Test)** The **Kolmogorov–Smirnov test** uses the statistic

$$
D_n=\sup_{-\infty<x<+\infty}\lvert F_n(x)-F_0(x)\rvert
$$
and rejects $H_0$ when $D_n>c$. With $d_0$ the observed value of $D_n$, the goodness of fit is $p(d_0)=\mathbb{P}(D_n\ge d_0\mid H_0)$, and $H_0$ is rejected if $p(d_0)<\alpha$.

Under $H_0$, $D_n\xrightarrow{\text{a.s.}}0$ by the Glivenko–Cantelli theorem (Theorem 1.5.2), while under an alternative $F\ne F_0$ the statistic $D_n$ converges to $\sup_x\lvert F(x)-F_0(x)\rvert>0$; large values of $D_n$ are evidence against $H_0$. Since $D_n$ only changes at the order statistics, it is computed as $D_n=\max_{1\le i\le n}\max\big\{\frac in-F_0(X_{(i)}),\ F_0(X_{(i)})-\frac{i-1}{n}\big\}$.

![The Kolmogorov–Smirnov statistic is the largest vertical distance between the empirical distribution function of a sample and the hypothesized distribution function.](./plots/ks-statistic.py)

**Theorem 6.5.1** Let $F_0$ be continuous. Under $H_0$:

1. the distribution of $D_n$ does not depend on $F_0$;
2. (Kolmogorov, 1933) for every $t>0$,

$$
\lim_{n\to\infty}\mathbb{P}\big(\sqrt n\,D_n\le t\big)=1-2\sum_{k=1}^\infty(-1)^{k-1}\mathrm{e}^{-2k^2t^2}.
$$

Part 1 follows from the probability integral transform: $U_i=F_0(X_i)$ are i.i.d. $\mathrm{U}(0,1)$ under $H_0$, and $D_n$ equals the Kolmogorov–Smirnov statistic of $U_1,\dots,U_n$ against the uniform distribution. Thus the test is exactly distribution-free, and its critical values are tabulated once for all continuous $F_0$; for large $n$ the asymptotic level-$0.05$ critical value is $1.358/\sqrt n$.

For a one-dimensional continuous $F_0$, the Kolmogorov–Smirnov test is generally preferable to Pearson's $\chi^2$ test: it uses the ungrouped data and is exact for small samples. Its weakness is the treatment of theoretical distributions with unknown parameters: if $\mu,\sigma^2$ are estimated from the same data, the null distribution of $D_n$ changes (the critical values become smaller) and the tables above no longer apply. (The Lilliefors test tabulates the corrected critical values for the normal family.)

**Example 6.5.1 (House Prices)** For the house prices of Example 6.1.5, testing $H_0\colon Y_i\sim\mathcal{N}(180000,80000^2)$ gives $D=0.122$ and $p<2.2\times10^{-16}$: this normal distribution is firmly rejected. For comparison, a simulated sample of $100$ standard normal values tested against $\mathcal{N}(0,1)$ gave $D=0.109$, $p=0.18$.

```r
ks.test(SalePrice, "pnorm", 180000, 80000)   # D = 0.12177, p-value < 2.2e-16
ks.test(rnorm(100), "pnorm")                 # e.g. D = 0.10913, p-value = 0.1846
```

### 6.5.2. The Shapiro–Wilk Test

The Shapiro–Wilk test is designed for the composite null hypothesis of normality with unknown $\mu,\sigma^2$. If $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ with order statistics $X_{(1)}\le\cdots\le X_{(n)}$, then $Y_i=(X_i-\mu)/\sigma$ are i.i.d. $\mathcal{N}(0,1)$ and $Y_{(i)}=(X_{(i)}-\mu)/\sigma$. Let

$$
m_i=\mathbb{E}Y_{(i)},\qquad e_i=X_{(i)}-\mathbb{E}X_{(i)},\qquad i=1,\dots,n .
$$
The $m_i$ do not depend on $\mu,\sigma^2$, and

$$
X_{(i)}=\mu+\sigma m_i+e_i,\qquad i=1,\dots,n,
$$
where $(e_1,\dots,e_n)$ have mean $0$ and covariance matrix $\sigma^2V$, with $V$ the (known) covariance matrix of $(Y_{(1)},\dots,Y_{(n)})$. Hence under $H_0$ the points $(m_1,X_{(1)}),\dots,(m_n,X_{(n)})$ lie close to a straight line with intercept $\mu$ and slope $\sigma$. Their squared correlation

$$
R^2=\frac{\Big(\sum_{i=1}^n(X_{(i)}-\bar X)(m_i-\bar m)\Big)^2}{\sum_{i=1}^n(X_{(i)}-\bar X)^2\sum_{i=1}^n(m_i-\bar m)^2}
$$
is close to $1$ under $H_0$, and normality is rejected if $R^2<c$. Shapiro and Wilk replaced $\boldsymbol{m}$ by the generalized least-squares weights that account for the correlation of the order statistics:

**Definition 6.5.2 (Shapiro–Wilk Test)** The **Shapiro–Wilk test** of normality uses the statistic

$$
W=\frac{\Big(\sum_{i=1}^{\lfloor n/2\rfloor}a_i\big(X_{(n+1-i)}-X_{(i)}\big)\Big)^2}{\sum_{i=1}^n(X_{(i)}-\bar X)^2},
$$
where $a_i=c_{n+1-i}$ and $(c_1,\dots,c_n)=\boldsymbol{m}^{\mathsf T}V^{-1}/\lVert V^{-1}\boldsymbol{m}\rVert$ (an antisymmetric vector, $c_{n+1-i}=-c_i$, so that the numerator equals $\big(\sum_{i=1}^nc_iX_{(i)}\big)^2$), and rejects normality when $W$ is small ($W\le c$, with tabulated or numerically computed critical values).

The statistic satisfies $0<W\le1$, and it is invariant under location and scale changes, so its null distribution does not depend on $\mu,\sigma^2$. The Shapiro–Wilk test targets normality specifically and is generally more powerful against non-normal alternatives than the Kolmogorov–Smirnov and Pearson $\chi^2$ tests.

**Example 6.5.2 (House Prices)** For the house prices, `shapiro.test(SalePrice)` gives $W=0.887$ and $p<2.2\times10^{-16}$, so normality is rejected; for a simulated normal sample of size $100$ it gave $W=0.982$, $p=0.197$.

### 6.5.3. The Normal Q–Q Plot

A graphical check complements the formal tests. The *normal Q–Q plot* plots the ordered sample $x_{(1)}\le\cdots\le x_{(n)}$ against the standard normal quantiles $\Phi^{-1}\big(\frac{i-0.5}{n}\big)$, $i=1,\dots,n$ (R: `qqnorm`). Since $\Phi^{-1}\big(\frac{i-0.5}{n}\big)$ approximates $m_i=\mathbb{E}Y_{(i)}$, under normality the points lie near a straight line with slope $\sigma$ and intercept $\mu$, the idea behind $R^2$ in §6.5.2. Typical departures are easy to recognize: an outlier is a single point far from the line; a right-skewed distribution gives a convex curve that lies above the line at both ends (as for the house prices); heavy tails pull the lower end below and the upper end above the line (an S shape).

![Normal Q–Q plots of samples of size 50 from a normal distribution, a normal distribution with one outlier, a right-skewed distribution and a heavy-tailed distribution; the line passes through the quartiles.](./plots/qq-patterns.py)

## Summary {#summary}

| Test | Data | Null hypothesis | Assumptions | Statistic and null distribution |
|---|---|---|---|---|
| sign test | one sample or paired differences | median $=0$ | continuous (or discard zeros) | $n_+\sim\mathrm{Bin}(n_0,0.5)$ |
| Wilcoxon signed-rank test | one sample or paired differences | center of symmetry $=0$ | symmetric distribution | $W^+$, mean $\frac{n_0(n_0+1)}{4}$, variance $\frac{n_0(n_0+1)(2n_0+1)}{24}$ |
| Wilcoxon rank-sum test | two independent samples | no location shift | same shape (shift model) | $W$, mean $\frac{n(N+1)}{2}$, variance $\frac{mn(N+1)}{12}$ |
| Pearson $\chi^2$ goodness of fit | counts in $r$ classes | given distribution ($s$ parameters estimated) | large counts ($np_j\ge5$) | $K_n\approx\chi^2_{r-1-s}$ |
| contingency table $\chi^2$ | $r\times s$ table | independence or homogeneity | large counts | $K_n\approx\chi^2_{(r-1)(s-1)}$ |
| Kolmogorov–Smirnov | continuous data | $F=F_0$, fully specified | $F_0$ continuous | $D_n$, distribution-free |
| Shapiro–Wilk | continuous data | normality, $\mu,\sigma^2$ unknown | — | $W$, small values reject |

When should we use nonparametric methods? Under correct parametric assumptions, such as normality, parametric tests are more efficient and powerful, but often by less than one might think: under normality the asymptotic relative efficiency of the Wilcoxon tests with respect to the $t$ tests is $3/\pi\approx0.955$ (that of the sign test is $2/\pi\approx0.637$). The efficiency of the Wilcoxon tests relative to the $t$ test is never below $0.864$ for continuous shift models, and if normality is grossly violated (heavy tails, outliers) they can be much more powerful. Nonparametric tests thus have a wide range of application and are robust, and large-sample theory plays a central role in them; parametric tests are more powerful when the underlying model is true.
