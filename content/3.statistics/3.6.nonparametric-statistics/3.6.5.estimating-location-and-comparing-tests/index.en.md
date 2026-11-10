---
title: Estimating Location and Comparing Tests
description: Point estimates from confidence intervals; central tendency, the pseudomedian and the Hodges–Lehmann estimator; asymptotic normality of sample quantiles and the asymptotic relative efficiencies of the median, the Hodges–Lehmann estimator and the mean; the assumptions of the sign test and its zeros; exact and approximate intervals for a binomial proportion (Clopper–Pearson, Wilson, Agresti–Coull); the Pitman raw-data test, normal scores and linear signed rank statistics; robustness and efficiency of the one-sample location tests.
---

A confidence interval says where the center of a population plausibly lies; a point estimate says where it most plausibly lies. Shrinking the intervals of [3.6.4](/3.6.4) to a point turns the sign test into the **sample median** and the Wilcoxon signed-rank test into the median of the Walsh averages, the Hodges–Lehmann estimator. This chapter studies these estimators, measures their efficiency against the sample mean with the same asymptotic relative efficiencies that compared the tests, and then completes the one-sample location problem: the sign test once more (its minimal assumptions, its zeros, its large-sample forms), the intervals for a binomial proportion that the sign test leads to, other choices of scores (the raw data, normal scores) unified as linear signed rank statistics, and finally a comparison of the $t$, Pitman, Wilcoxon and sign tests on skewed data with outliers. The two-sample versions of these ideas, the Hodges–Lehmann shift estimator in particular, are developed in [3.6.9](/3.6.9).

Notation as in [3.6.4](/3.6.4): $X_1,\dots,X_n$ are independent with center $\theta$, $D_i=X_i-\theta_0$ for a hypothesized value $\theta_0$, $K=\#\{i\colon D_i>0\}$ is the sign statistic, and $S_+$, $S_-$ are the signed-rank sums.

## 5.1. From Confidence Intervals to Point Estimates

### 5.1.1. Shrinking an Interval

Both intervals of [3.6.4](/3.6.4) are symmetric in rank: the sign interval runs from the $(k+1)$-th smallest to the $(k+1)$-th largest observation, the Wilcoxon interval from the $(w+1)$-th smallest to the $(w+1)$-th largest Walsh average. As the confidence level decreases the intervals shrink, and in the limit they close on the middle of the ordered list. A natural point estimate is therefore the value of $\theta_0$ that is "least rejected", the $\theta_0$ at which the test statistic sits at the center of its null distribution: $K=n/2$ for the sign test, $S_+=S_-$ for the signed-rank test. For the sign test this is the sample median. For the signed-rank test, Theorem 4.3.1 of [3.6.4](/3.6.4) says that $S_+$ and $S_-$ count the Walsh averages $A_{ij}=(X_i+X_j)/2$, $i\le j$, above and below $\theta_0$, so $S_+=S_-$ when $\theta_0$ is the median of the Walsh averages.

The population quantity that this estimates has a name of its own.

**Definition 5.1.1 (Pseudomedian)** Let $X_1,X_2$ be independent with distribution $F$. The **pseudomedian** of $F$ is the median of the distribution of $(X_1+X_2)/2$.

The pseudomedian is well defined for every distribution, including the many (such as the Cauchy) that have no mean, and for a symmetric distribution it equals the center of symmetry, hence the median: if $F$ is symmetric about $\theta$, so is the distribution of $(X_1+X_2)/2$. For a skewed distribution it usually lies between the median and the mean.

**Definition 5.1.2 (Hodges–Lehmann Estimator)** The **Hodges–Lehmann estimator** of location is the median of the Walsh averages,

$$
\hat\theta_{\mathrm{HL}}=\operatorname*{median}\Big\{\frac{X_i+X_j}{2}\colon 1\le i\le j\le n\Big\}.
$$

(Some authors use only the pairs $i<j$; the two versions have the same asymptotic behavior. R's `wilcox.test(x, conf.int = TRUE)` reports the version with $i\le j$ as the "(pseudo)median".)

**Example 5.1.1 (Heart Rate Data)** For the twelve differences $-2,4,8,25,-5,16,3,1,12,17,20,9$ of [3.6.4](/3.6.4), the sample median is $8.5$, the mean is $9$, and the median of the $78$ Walsh averages is $\hat\theta_{\mathrm{HL}}=9$. A small function returns the interval and the estimate together:

```r
waconflim <- function(x, alpha = 0.05) {
  x <- sort(x); n <- length(x)
  walp <- qsignrank(p = alpha / 2, n = n)
  if (psignrank(q = walp, n = n) > alpha / 2) walp <- walp - 1
  wa <- outer(x, x, "+") / 2
  wa <- sort(wa[lower.tri(wa, diag = TRUE)])
  l <- wa[walp + 1]; u <- wa[length(wa) - walp]
  paste0(round(1 - 2 * psignrank(q = walp, n = n), 4) * 100,
         "% CI = [", l, ", ", u, "], median = ", median(wa))
}
waconflim(c(-2, 4, 8, 25, -5, 16, 3, 1, 12, 17, 20, 9))
```

```text
[1] "95.75% CI = [2.5, 16], median = 9"
```

:::

The Hodges–Lehmann estimator combines the advantages of the mean and the median. Like the median it is robust: replacing an observation by an arbitrarily large value moves only the Walsh averages involving it, and the median of all Walsh averages stays bounded (it breaks down only when about $29\%$ of the observations are contaminated). It is consistent for the pseudomedian, median-unbiased for symmetric populations, and, as §5.2 shows, nearly as efficient as the mean for normal data and more efficient for heavy-tailed data.

![Sensitivity curves for the heart-rate data: the mean, the median and the Hodges–Lehmann estimate when the largest observation, 25, is replaced by a value y. The mean follows y without bound; the median and the Hodges–Lehmann estimate change only while y moves through the middle of the data and are constant beyond it.](./plots/outlier-sensitivity.py)

### 5.1.2. Measures of Central Tendency

The term central tendency (from the late 1920s) refers to a central or typical value of a distribution, which is a **location parameter**; its measures are informally called averages. The three classical ones serve different purposes:

| Measure | Definition | Strengths | Weaknesses |
|---|---|---|---|
| mean | $\mathbb{E}X$; estimated by $\bar X$ | efficient for normal data; algebraically convenient | sensitive to **outliers**; may not exist (Cauchy) |
| **median** | $\theta$ with $\mathbb{P}(X\le\theta)\ge\frac12\le\mathbb{P}(X\ge\theta)$; estimated by the sample median | robust; meaningful for skewed and ordinal data | needs more observations than the mean for the same precision under normality |
| **mode** | the most probable value | the only measure for nominal categories | poorly estimated for continuous data; may not be unique |

The pseudomedian adds a fourth measure, between the median and the mean in both meaning and behavior.

## 5.2. Asymptotic Relative Efficiency of Estimators

For two consistent and asymptotically normal estimators $T_1,T_2$ of the same parameter, with $\sqrt n(T_k-\theta)\xrightarrow{d}\mathcal{N}(0,v_k)$, the asymptotic relative efficiency of $T_1$ with respect to $T_2$ is the ratio of asymptotic variances $v_2/v_1$: the number of observations $T_2$ needs, per observation of $T_1$, for the same precision. This is the estimation version of Definition 4.7.1 of [3.6.4](/3.6.4), and for an estimator obtained by inverting a test it gives the same number as the ARE of the test.

The asymptotic variance of the sample median follows from that of the sample quantiles.

**Theorem 5.2.1 (Asymptotic Normality of Sample Quantiles)** Let $X_1,\dots,X_n$ be i.i.d. with distribution function $F$, let $0<p<1$, and let $F$ have a positive continuous density $f$ at $x_p=F^{-1}(p)$. Then the sample $p$-quantile $\hat x_p=X_{(\lceil np\rceil)}$ satisfies

$$
\sqrt n\,(\hat x_p-x_p)\xrightarrow{d}\mathcal{N}\left(0,\frac{p(1-p)}{f(x_p)^2}\right).
$$
In particular the sample median $\operatorname{Med}_n$ of a population with median $\theta$ satisfies $\operatorname{Med}_n\overset{\cdot}{\sim}\mathcal{N}\big(\theta,1/(4f(\theta)^2n)\big)$.

**Proof** Fix $t$ and put $x_n=x_p+t/\sqrt n$. The sample quantile is at most $x_n$ if and only if at least $\lceil np\rceil$ observations are at most $x_n$, that is, $nF_n(x_n)\ge\lceil np\rceil$, where $F_n$ is the **empirical distribution function** and $nF_n(x_n)\sim\mathrm{Bin}(n,F(x_n))$. Standardizing,

$$
\mathbb{P}\big(\sqrt n(\hat x_p-x_p)\le t\big)=\mathbb{P}\left(\frac{nF_n(x_n)-nF(x_n)}{\sqrt{nF(x_n)(1-F(x_n))}}\ge\frac{\lceil np\rceil-nF(x_n)}{\sqrt{nF(x_n)(1-F(x_n))}}\right).
$$
Since $F(x_n)=p+f(x_p)t/\sqrt n+o(1/\sqrt n)$, the right-hand bound tends to $-f(x_p)t/\sqrt{p(1-p)}$, and by the **central limit theorem** for triangular arrays of binomials (Lindeberg) the probability tends to $\Phi\big(f(x_p)t/\sqrt{p(1-p)}\big)$, the distribution function of $\mathcal{N}\big(0,p(1-p)/f(x_p)^2\big)$. $\square$

The same result can be read off heuristically with the **delta method**: $\sqrt n\big(F_n(x)-F(x)\big)\xrightarrow{d}\mathcal{N}\big(0,F(x)(1-F(x))\big)$, and the quantile is the inverse function $F^{-1}$, whose derivative at $p$ is $1/f(F^{-1}(p))$; this multiplies the variance $p(1-p)$ by $1/f(x_p)^2$. (Making the heuristic rigorous needs the functional delta method, because $F_n^{-1}$ is a function of the whole curve $F_n$.)

For the Hodges–Lehmann estimator we state the corresponding result (Hodges and Lehmann 1963), which follows from the asymptotics of $S_+$ by the same inversion argument: for $F$ symmetric about $\theta$ with density $f$,

$$
\sqrt n\,(\hat\theta_{\mathrm{HL}}-\theta)\xrightarrow{d}\mathcal{N}\left(0,\frac{1}{12\big(\int f^2(x)\,\mathrm{d}x\big)^2}\right).
$$
Comparing with $\sqrt n(\bar X_n-\theta)\xrightarrow{d}\mathcal{N}(0,\sigma^2)$,

$$
\operatorname{ARE}(\operatorname{Med}_n,\bar X_n)=4\sigma^2f(\theta)^2,\qquad \operatorname{ARE}(\hat\theta_{\mathrm{HL}},\bar X_n)=12\sigma^2\left(\int f^2(x)\,\mathrm{d}x\right)^2,
$$
exactly the efficiencies of the sign and signed-rank tests relative to the $t$ test in [3.6.4](/3.6.4).

**Example 5.2.1 (Normal and Laplace Populations)** For $\mathcal{N}(\theta,\sigma^2)$, $f(\theta)=1/\sqrt{2\pi\sigma^2}$ and $\int f^2=1/(2\sigma\sqrt\pi)$, so

$$
\operatorname{ARE}(\operatorname{Med}_n,\bar X_n)=\frac2\pi\approx0.64,\qquad \operatorname{ARE}(\hat\theta_{\mathrm{HL}},\bar X_n)=\frac3\pi\approx0.955.
$$
For the Laplace density $\frac\lambda2\mathrm{e}^{-\lambda\lvert x-\theta\rvert}$, $\sigma^2=2/\lambda^2$, $f(\theta)=\lambda/2$ and $\int f^2=\lambda/4$, so the efficiencies are $2$ and $1.5$. The value $2$ is no surprise: for the Laplace distribution the sample median is the **maximum likelihood estimator** of $\theta$, and it is twice as efficient as the mean.

:::

The comparison justifies the Hodges–Lehmann estimator as a compromise. Under normality it loses less than $5\%$ against the mean, where the median loses $36\%$; under heavy tails it gains, though less than the median does for the Laplace distribution; and its efficiency relative to the mean is never below $0.864$ for continuous symmetric populations. The general lesson is the same as for tests: the ARE depends dramatically on the shape of the density, and since that shape is rarely known, it is a benchmark to be used with caution. There is no estimator of location that is best for every population.

## 5.3. The Sign Test Revisited

### 5.3.1. Assumptions

The sign test and the signed-rank test are often presented together, but their assumptions differ, and it pays to state them precisely.

| | sign test | Wilcoxon signed-rank test | $t$ test |
|---|---|---|---|
| independence | required | required | required |
| identical distributions | not required: each $X_i$ only needs median $\theta$ | not required: each $X_i$ must be symmetric about the same $\theta$ (scales may differ) | required (or a large sample) |
| shape | none; continuity avoids zeros | continuous and symmetric | normal (or a large sample) |
| information used | signs of $X_i-\theta_0$ | signs and ranks of $\lvert X_i-\theta_0\rvert$ | values |
| null hypothesis | median $=\theta_0$ | center of symmetry $=\theta_0$ (also the mean, if it exists) | mean $=\theta_0$ |

The sign test thus makes the weakest assumptions of all location tests. Under symmetry the median is also the mean, so the sign test then tests the mean as well. Its main advantage is that it completely ignores the size of outliers; its main disadvantage is that it discards the information in the magnitudes. The signed-rank test keeps the ranks of the magnitudes, which protects against outliers while using more information, at the price of the symmetry assumption.

A quick illustration of the information each test uses: for testing $\theta=0$ with the three-observation samples $(5,6,-1)$, $(10000,6,-1)$, $(100,60,-1)$ and $(1,1,-1)$, the sign test sees four identical samples (two positive, one negative); the signed-rank test sees the first three as identical ($S_+=5$, $S_-=1$), while the tie in the last makes it different; and the $t$ test sees four different samples, with $t=1.52$, $1.00$, $1.80$ and $0.50$: the huge value $10000$ lowers $t$, because it inflates the standard deviation more than the mean.

### 5.3.2. Zeros

The derivation of the sign test assumed $\mathbb{P}(X_i=\theta_0)=0$, so that $K\sim\mathrm{Bin}(n,1/2)$ under $H_0$. With rounded data, some observations may equal $\theta_0$ exactly. Such zeros say nothing about the direction of a departure from $H_0$, yet they are evidence for $H_0$: they "speak in favor of" the null value. The counts $(N_+,N_0,N_-)$ of positive, zero and negative differences have a trinomial distribution, and the possible treatments are:

- Discard the zeros and apply the test to the $n-N_0$ nonzero differences, conditionally on $N_0$. This is the standard choice and gives a valid conditional test; it ignores the support that zeros give to $H_0$, so it is somewhat liberal when there are many zeros.
- Split the zeros equally between the positive and negative counts (Dixon and Mood, 1946). This keeps $n$ and makes the test conservative.
- Toss a coin for each zero to assign its sign. This adds randomness unrelated to the data and usually makes little difference; it has little to commend it.

The same issue arises as **ties** at zero in the signed-rank test and as ties between samples in the Wilcoxon–Mann–Whitney test (Randles, 2001, discusses both). Whatever the choice, it should be fixed before looking at the data and reported.

### 5.3.3. Exact and Approximate Computation

For moderate $n$ the sign test is a **binomial test** and is computed exactly. For very large $n$, exact tail sums are slow and can underflow, and the normal approximation is fast and very accurate.

**Example 5.3.1 (An Election Poll)** In a poll of $2000$ voters, $1080$ prefer candidate A. Test $H_0\colon p=0.5$ (no preference) against $H_1\colon p>0.5$.

```r
binom.test(x = 1080, n = 2000, alternative = "greater")                 # exact
prop.test(x = 1080, n = 2000, alternative = "greater", correct = TRUE)  # normal, continuity correction
chisq.test(x = c(1080, 920), p = c(0.5, 0.5), correct = FALSE)          # chi-squared, 1 df
```

The exact $p$-value is $1.875\times10^{-4}$, and the continuity-corrected normal approximation gives $1.887\times10^{-4}$; with $np=n(1-p)=1000\gg5$ the approximation is excellent. The uncorrected statistic is $z=(1080-1000)/\sqrt{500}=3.58$, and $z^2=12.8$ is the Pearson $\chi^2$ goodness-of-fit statistic with $1$ degree of freedom for the two categories; `chisq.test` reports the two-sided $p$-value $3.5\times10^{-4}$, twice the one-sided normal value, because the $\chi^2$ statistic cannot tell the direction of the departure.

:::

## 5.4. Confidence Intervals for a Binomial Proportion

The sign test is a test about a binomial proportion, and inverting the binomial test gives a confidence interval for any proportion $p$, from $x$ successes in $n$ independent trials.

### 5.4.1. The Exact Interval

By Theorem 4.1.1 of [3.6.4](/3.6.4), $p$ belongs to the $1-\alpha$ interval if neither one-sided binomial test rejects it at level $\alpha/2$:

$$
C=S_{\le}\cap S_{\ge},\qquad S_{\le}=\{p\colon\mathbb{P}_p(X\le x)>\alpha/2\},\quad S_{\ge}=\{p\colon\mathbb{P}_p(X\ge x)>\alpha/2\},\qquad X\sim\mathrm{Bin}(n,p).
$$
Trial and error over a grid of $p$ values finds it directly:

```r
find_ci <- function(x, n, alpha = 0.05) {
  p_grid <- seq(0, 1, by = 0.001)
  keep <- sapply(p_grid, function(p)
    pbinom(x, n, p) > alpha / 2 && 1 - pbinom(x - 1, n, p) > alpha / 2)
  range(p_grid[keep])
}
find_ci(9, 13)                    # 0.386 0.909
binom.test(x = 9, n = 13)$conf.int  # 0.3857383 0.9090796
```

A closed form comes from the link between binomial counts and uniform **order statistics** ([3.6.2](/3.6.2)): if $U_1,\dots,U_n$ are i.i.d. $\mathrm{U}(0,1)$, then $X=\#\{i\colon U_i\le p\}\sim\mathrm{Bin}(n,p)$, the $k$-th order statistic satisfies $U_{(k)}\sim\mathrm{Beta}(k,n-k+1)$, and

$$
X\le k\iff U_{(k+1)}>p,\qquad X\ge k\iff U_{(k)}\le p .
$$

**Definition 5.4.1 (Clopper–Pearson Interval)** For $x=1,\dots,n-1$ successes in $n$ trials, the **Clopper–Pearson interval** for $p$ at level $1-\alpha$ is

$$
\Big[\mathrm{Beta}_{\alpha/2}(x,\,n-x+1),\ \ \mathrm{Beta}_{1-\alpha/2}(x+1,\,n-x)\Big],
$$
where $\mathrm{Beta}_q(a,b)$ denotes the $q$-quantile of $\mathrm{Beta}(a,b)$ (lower quantile here). For $x=0$ the lower limit is $0$ and the upper limit is $1-(\alpha/2)^{1/n}$; for $x=n$ the interval is $\big[(\alpha/2)^{1/n},1\big]$.

The formula is the trial-and-error interval in closed form: $\mathbb{P}_p(X\le x)=\mathbb{P}(U_{(x+1)}>p)>\alpha/2$ means $p<\mathrm{Beta}_{1-\alpha/2}(x+1,n-x)$, and $\mathbb{P}_p(X\ge x)=\mathbb{P}(U_{(x)}\le p)>\alpha/2$ means $p>\mathrm{Beta}_{\alpha/2}(x,n-x+1)$. For $x=0$ the upper limit solves $(1-p)^n=\alpha/2$. (When $x=0$ the lower limit is trivially $0$, and some authors put the whole $\alpha$ into the upper tail, giving the shorter one-sided bound $1-\alpha^{1/n}$.)

The interval is called exact because its coverage is at least $1-\alpha$ for every $p$; because $X$ is discrete, the coverage is usually strictly larger, so the interval is conservative and wider than necessary.

### 5.4.2. Approximate Intervals

The textbook large-sample interval replaces $p$ by $\hat p=x/n$ in the standard error,

$$
\hat p\pm z_{\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}\qquad\text{(Wald interval)}.
$$
It is simple and badly behaved: its coverage falls far below the nominal level for small $n$ or $p$ near $0$ or $1$, it can extend outside $[0,1]$, and for $x=0$ it degenerates to the single point $0$. Keeping $p$ in the standard error and solving the quadratic inequality instead gives a much better interval.

**Definition 5.4.2 (Wilson Score Interval)** The **Wilson score interval** is the set of $p$ with $\lvert\hat p-p\rvert\le z\sqrt{p(1-p)/n}$, $z=z_{\alpha/2}$:

$$
\frac{\hat p+\dfrac{z^2}{2n}}{1+\dfrac{z^2}{n}}\ \pm\ \frac{z}{1+\dfrac{z^2}{n}}\sqrt{\frac{\hat p(1-\hat p)}{n}+\frac{z^2}{4n^2}} .
$$

It inverts the score test (R's `prop.test(x, n, correct = FALSE)$conf.int`), always lies in $[0,1]$, and has coverage close to the nominal level over the whole range of $p$, though, unlike the Clopper–Pearson interval, it can fall somewhat below it for particular $p$. Its center

$$
\frac{x+z^2/2}{n+z^2}=\frac{n}{n+z^2}\,\hat p+\frac{z^2}{n+z^2}\cdot\frac12
$$
is a weighted average of $\hat p$ and $1/2$, with weight on $\hat p$ increasing with $n$: the estimate is shrunk toward $1/2$, as if $z^2/2$ pseudo-successes and $z^2/2$ pseudo-failures had been added. This is additive smoothing (**Laplace smoothing** when one pseudocount is added to each category), a simple **shrinkage estimator**; it has the same form as the posterior mean of a normal mean under a normal prior ([3.2.7](/3.2.7)), a precision-weighted average of the data and the prior center.

Taking $z\approx2$ for a $95\%$ interval gives two pseudo-successes and two pseudo-failures, and a Wald-type interval around the smoothed estimate.

**Definition 5.4.3 (Agresti–Coull Interval)** With $\tilde n=n+z^2$ and $\tilde p=(x+z^2/2)/\tilde n$, the **Agresti–Coull interval** is

$$
\tilde p\pm z\sqrt{\frac{\tilde p(1-\tilde p)}{\tilde n}} ;
$$
for $95\%$ intervals it is commonly simplified to the plus-four rule $\tilde p=(x+2)/(n+4)$, $\tilde n=n+4$.

**Example 5.4.1** For $x=9$ successes in $n=13$ trials ($\hat p=0.692$), the four $95\%$ intervals are:

| Interval | Lower | Upper | Comment |
|---|---|---|---|
| Wald | $0.441$ | $0.943$ | centered at $\hat p$ |
| Wilson | $0.424$ | $0.873$ | centered at $0.648$ |
| Agresti–Coull (plus four) | $0.420$ | $0.874$ | centered at $11/17=0.647$ |
| Clopper–Pearson | $0.386$ | $0.909$ | widest |

:::

![Exact coverage of nominal 95% intervals for a binomial proportion with n = 20, as a function of the true p. The Wald interval undercovers badly, especially near 0 and 1; the Wilson and Agresti–Coull intervals oscillate around 95%; the Clopper–Pearson interval never falls below 95% and is usually well above it. The saw-tooth shape comes from the discreteness of the binomial distribution.](./plots/proportion-coverage.py)

For a small sample, a sensible default is the Wilson interval (or the plus-four interval when a formula must be computed by hand); when a guaranteed coverage is required, as in some regulatory settings, use Clopper–Pearson and accept its extra width; avoid the Wald interval unless $n$ is large and $p$ is far from $0$ and $1$.

## 5.5. Other Scores

### 5.5.1. The Pitman Test

The $t$ test is often a good approximation to an exact randomization test, and for samples that are not very small the signed-rank test leads to similar conclusions; for very small samples, though, we may want an exact test that does not assume normality and uses the actual values. Under the symmetry assumption of the signed-rank test, each $D_i$ is equally likely to be $+\lvert D_i\rvert$ or $-\lvert D_i\rvert$ under $H_0$, independently, whatever the magnitudes. Conditioning on the magnitudes therefore gives an exact **permutation test**, with the signed deviations themselves as scores instead of their signed ranks.

**Definition 5.5.1 (Pitman Test)** The **Pitman test** (Fisher–Pitman, or raw data, test) of $H_0\colon\theta=\theta_0$ for a sample from a distribution symmetric about $\theta$ uses $S_+=\sum_{i\colon D_i>0}\lvert D_i\rvert$, the sum of the positive deviations, and refers it to its conditional null distribution over the $2^n$ equally likely assignments of signs to $\lvert D_1\rvert,\dots,\lvert D_n\rvert$.

Equivalent statistics are $S_-=\sum_{i\colon D_i<0}\lvert D_i\rvert$ and $S_d=S_+-S_-=\sum_iD_i$, since $S_++S_-=\sum_i\lvert D_i\rvert$ is fixed by the conditioning.

**Example 5.5.1 (Heart Rate)** The heart rates (beats per minute) of seven subjects are $73,82,87,68,106,60,97$; test $H_0\colon\theta=70$ against $H_1\colon\theta>70$. The deviations are $3,12,17,-2,36,-10,27$, so $S_+=3+12+17+27+36=95$ and $S_-=12$, with $S_++S_-=107$. Larger values of $S_+$ arise exactly when the negative signs are attached to absolute deviations with sum at most $12$; from $\{2,3,10,12,17,27,36\}$ these are the subsets $\varnothing$, $\{2\}$, $\{3\}$, $\{2,3\}$, $\{10\}$, $\{2,10\}$, $\{12\}$, giving $S_+=107,105,104,102,97,95,95$. Hence

$$
p=\mathbb{P}(S_+\ge95)=\frac{7}{128}=0.055 .
$$
There is not enough evidence to reject $H_0$ at the $5\%$ level; a larger study would be needed. (The one-sided $t$ test gives $p=0.051$, and the signed-rank test, with $S_-=1+3=4$, gives the same $7/128$.)

:::

**Proposition 5.5.1** Given the magnitudes $\lvert D_1\rvert,\dots,\lvert D_n\rvert$, the one-sample $t$ statistic $t=\sqrt n\bar D/s$ is a strictly increasing function of $S_+$. Thus the Pitman test is the exact permutation version of the $t$ test: the same ordering of the sign patterns, with the permutation distribution in place of the $t_{n-1}$ distribution.

**Proof** Under sign changes, $Q=\sum_iD_i^2$ is fixed and $\sum_iD_i=2S_+-\sum_i\lvert D_i\rvert$ is increasing in $S_+$. Writing $u=\sum_iD_i/\sqrt{nQ}\in[-1,1]$, we have $(n-1)s^2=Q-(\sum_iD_i)^2/n=Q(1-u^2)$, so $t=\sqrt{n-1}\,u/\sqrt{1-u^2}$, which is strictly increasing in $u$. $\square$

So the Pitman test and the $t$ test are not identical tests (their reference distributions differ, and so do their $p$-values), but they rank the possible samples in the same way, and for moderate $n$ the permutation distribution is close to $t_{n-1}$. Exact enumeration of $2^n$ patterns is practical for small and moderate $n$; for larger $n$ use Monte Carlo sampling of the signs or the normal approximation $S_d/\sqrt{\sum_iD_i^2}\approx\mathcal{N}(0,1)$. The test uses all the information in the data, but it inherits the $t$ test's sensitivity to outliers (§5.6), it requires symmetry, and a confidence interval, though obtainable in principle by inversion, has no simple closed form.

### 5.5.2. Normal Scores

The signed-rank test replaces the magnitudes by their ranks; the Pitman test keeps them. An intermediate idea is to replace the ranks by numbers that look like the magnitudes of a normal sample. If $\lvert D_i\rvert$ has rank $R_i^+$ among $n$, the corresponding quantile of the distribution of $\lvert Z\rvert$, $Z\sim\mathcal{N}(0,1)$, is

$$
a(R_i^+)=\Phi^{-1}\left(\frac12+\frac{R_i^+}{2(n+1)}\right),
$$
the $R_i^+/(n+1)$ quantile of the half-normal distribution.

**Definition 5.5.2 (Normal Scores Test)** The one-sample **normal scores test** (Van der Waerden test) uses $S=\sum_{i\colon D_i>0}a(R_i^+)$ with the half-normal scores above. Under $H_0$ (symmetry about $\theta_0$),

$$
\mathbb{E}S=\frac12\sum_{i=1}^na(i),\qquad \operatorname{Var}S=\frac14\sum_{i=1}^na(i)^2,
$$
and the test refers $S$ to its exact distribution over the $2^n$ sign patterns or uses $\big(S-\mathbb{E}S\big)/\sqrt{\operatorname{Var}S}\approx\mathcal{N}(0,1)$.

Normal scores were proposed because they make a rank test behave like the $t$ test when the data are normal, while keeping the robustness of ranks when they are not: under normality the normal scores test has ARE $1$ relative to the $t$ test, and in shift models its ARE relative to the $t$ test is at least $1$ for every continuous population (Chernoff and Savage, 1958, proved this for the two-sample test; the one-sample analogue holds for symmetric populations). Closely related are the expected normal scores (Fisher–Yates, Terry–Hoeffding), which use the expected values of normal order statistics instead of quantiles.

**Example 5.5.2** For the sample $2,3,7,21,132$ and $H_0\colon\theta=10$ against $H_1\colon\theta>10$, the deviations are $-8,-7,-3,11,122$ with signed ranks $-3,-2,-1,4,5$. The half-normal scores for ranks $1,\dots,5$ ($n+1=6$) are $\Phi^{-1}(7/12),\dots,\Phi^{-1}(11/12)=0.210,0.431,0.674,0.967,1.383$. The positive deviations have ranks $4$ and $5$, so $S=0.967+1.383=2.350$; under $H_0$, $\mathbb{E}S=1.833$ and $\operatorname{Var}S=0.883$, so $z=0.55$ and the approximate $p$-value is $0.29$. The exact $p$-value, from the $32$ sign patterns, is $10/32=0.31$. For comparison, the signed-rank test gives $p=0.41$, the sign test $0.81$ and the $t$ test $0.20$; no test finds evidence against $H_0$, and the single huge value $132$ hardly matters to the rank-based tests.

:::

### 5.5.3. Linear Signed Rank Statistics

The sign, signed-rank and normal scores statistics have a common form.

**Definition 5.5.3 (Linear Rank Statistic)** A statistic $T=T(\boldsymbol{R})$ that depends on the data only through the rank vector $\boldsymbol{R}$ is a rank statistic. A **linear rank statistic** has the form

$$
S=\sum_{i=1}^Nc_i\,a(R_i),
$$
where $a(1),\dots,a(N)$ are the scores and $c_1,\dots,c_N$ are the regression constants. In the one-sample problem the analogous **linear signed rank statistic** is

$$
S=\sum_{i=1}^na(R_i^+)\,\boldsymbol{1}\{D_i>0\},
$$
where $R_i^+$ is the rank of $\lvert D_i\rvert$.

The two-sample Wilcoxon rank-sum statistic is the linear rank statistic with $c_i=1$ for the observations of one sample and $0$ for the other and with the ranks (midranks under ties) as scores; regression versions use $c_i=x_i$. The one-sample tests of this chapter are linear signed rank statistics:

| Test | Scores $a(i)$ |
|---|---|
| sign test | $a(i)\equiv1$, so $S=K$ |
| Wilcoxon signed-rank test | $a(i)=i$, so $S=S_+$ |
| normal scores test | $a(i)=\Phi^{-1}\big(\frac12+\frac{i}{2(n+1)}\big)$ |

The Pitman test is not a rank statistic at all: its "scores" are the observed magnitudes $\lvert D_i\rvert$, which depend on the data and not only on the ranks.

**Theorem 5.5.1** Let $D_1,\dots,D_n$ be independent, each continuous and symmetric about $0$. Then for any scores, $S=\sum_ia(R_i^+)\boldsymbol{1}\{D_i>0\}$ has the distribution of $\sum_{i=1}^na(i)I_i$ with $I_1,\dots,I_n$ i.i.d. $\mathrm{Ber}(1/2)$; in particular it is distribution-free, with $\mathbb{E}S=\frac12\sum_ia(i)$ and $\operatorname{Var}S=\frac14\sum_ia(i)^2$.

**Proof** For a continuous distribution symmetric about $0$, the sign of $D_i$ is independent of $\lvert D_i\rvert$ and equals $+$ with probability $1/2$. Hence the signs are i.i.d. fair coin flips independent of the magnitudes, and therefore of the ranks $R_i^+$. Let $I_k$ indicate that the observation with $\lvert D\rvert$-rank $k$ is positive; then $S=\sum_ka(k)I_k$ with $I_k$ i.i.d. $\mathrm{Ber}(1/2)$, and the moments follow. $\square$

The choice of scores is the choice of which populations the test is tuned to: constant scores are best for very heavy (Laplace-like) tails, linear scores for logistic-like tails, normal scores for normal tails. For ordered categorical data, Graubard and Korn (1987) compared midrank scores with equally spaced and other scores and showed that the choice can change the conclusion; scores should be fixed before seeing the data, guided by the alternatives of interest.

## 5.6. Comparing Tests: Robustness and Efficiency

Robustness asks whether a test is sensitive to departures from its assumptions. Efficiency, measured by the ARE, asks how well it uses the data when the assumptions hold. The two pull in opposite directions, and the skewed samples of [3.6.4](/3.6.4) show the trade-off.

**Example 5.6.1** Test $H_0\colon\theta=9$ against $H_1\colon\theta\ne9$ for Sample I ($5.5,6.0,6.5,7.6,7.6,7.7,8.0,8.2,9.1,15.1$) and Sample II ($5.6,6.1,6.3,6.3,6.5,6.6,7.0,7.5,7.9,8.0,8.0,8.1,8.1,8.2,8.4,8.5,8.7,9.4,14.3,26.0$) with four tests. The asymptotic Pitman $p$-value uses $\sum_iD_i/\sqrt{\sum_iD_i^2}\approx\mathcal{N}(0,1)$, the asymptotic sign test $(2K-n)/\sqrt n$ without continuity correction.

| Test | Sample I, exact | Sample I, asymptotic | Sample II, exact | Sample II, asymptotic |
|---|---|---|---|---|
| $t$ | $0.331$ | — | $0.823$ | — |
| Pitman | $0.352$ | $0.305$ | $0.916$ | $0.817$ |
| Wilcoxon | $0.102$ | $0.092$ | $0.015$ | $0.017$ |
| sign | $0.109$ | $0.058$ | $0.003$ | $0.002$ |

```r
s1 <- c(5.5, 6.0, 6.5, 7.6, 7.6, 7.7, 8.0, 8.2, 9.1, 15.1)
t.test(s1, mu = 9)
wilcox.test(s1, mu = 9)                     # normal approximation, continuity correction
wilcox.test(s1, mu = 9, correct = FALSE)
asht::wsrTest(s1, mu = 9)                   # exact, also with ties
binom.test(x = sum(s1 > 9), n = length(s1), p = 0.5)           # exact sign test
2 * pnorm(2 * (sum(s1 > 9) - length(s1) / 2) / sqrt(length(s1)))  # asymptotic sign test
pitman_test <- function(x, mu = 0, reps = 1e4) {   # Monte Carlo version of the Pitman test
  d <- x - mu
  stat <- function(d) min(sum(abs(d) * (d > 0)), sum(abs(d) * (d < 0)))
  s <- stat(d)
  mean(replicate(reps, stat(sample(c(1, -1), length(d), replace = TRUE) * abs(d))) <= s)
}
pitman_test(s1, mu = 9)
```

The $t$ test agrees with the Pitman test, as Proposition 5.5.1 leads us to expect, and both are far from significant for Sample II: the outliers $14.3$ and $26.0$ inflate the variance and pull the mean ($8.78$) toward $9$. The Wilcoxon and sign tests, which look at ranks or signs, see that $17$ of the $20$ observations lie below $9$ and reject clearly for Sample II. The Pitman and Wilcoxon tests reach completely different conclusions on the same data.

The continuity correction also matters for small samples. For the Wilcoxon test of Sample I, the exact $p$-value is $0.1016$, the corrected normal approximation $0.1027$ and the uncorrected one $0.0924$ (Sample II: $0.0149$, $0.0177$, $0.0169$); for the sign test of Sample I the uncorrected approximation $0.058$ is far from the exact $0.109$, while the corrected one gives $0.114$.

:::

**Example 5.6.2 (Outliers)** Replace the largest observations $15.1$ (Sample I) and $14.3$, $26.0$ (Sample II) by the less extreme values $12.7$ and $12.6$, $12.8$. They remain the largest deviations from $9$, so the ranks and signs, and with them the $p$-values of the Wilcoxon and sign tests, do not change at all. The exact Pitman $p$-values drop from $0.352$ to $0.123$ (Sample I) and from $0.916$ to $0.036$ (Sample II), and the $t$ test behaves in the same way ($0.331\to0.114$, $0.823\to0.033$): for Sample II, a change in two values that are outliers either way turns "no evidence at all" into "significant at $5\%$".

:::

The robustness of the Pitman test is thus much lower than that of the Wilcoxon test. Conversely, when a sample comes from a normal distribution, the $t$ test is more efficient than any other test, as the ARE results showed. The four tests line up along a single axis:

| Test | Information used | Efficiency under normality (ARE vs. $t$) | Robustness to outliers | Assumption |
|---|---|---|---|---|
| $t$ | values | $1$ | low | normality or large $n$ |
| Pitman | values | $1$ | low | symmetry |
| Wilcoxon signed-rank | signs and ranks | $0.955$ | high | symmetry |
| sign | signs | $0.637$ | highest | none beyond a common median |

The more of the data a test uses, the more efficient it is when its model is right and the more it is hurt when it is wrong. In practice, start with exploratory data analysis: plot the data and check for asymmetry and outliers. If the data are skewed or contain extreme values, use the sign test; if they are symmetric but not normal (heavy tails, a few outliers), use the Wilcoxon test; if they look normal, use the $t$ or Pitman test. A sign test is appropriate, for example, for motor insurance claims, where most claims are of the order of a thousand pounds but a few exceed a hundred thousand, so the distribution is certainly skewed. For marks in a well-established test of numerical skills, where a new teaching method is to be compared against a known population median, the Wilcoxon test (or its normal approximation) is appropriate if symmetry can be assumed, and the sign test otherwise.

## Summary

- Point estimates from tests: the $\theta_0$ that is least rejected; the sign test gives the sample median, the signed-rank test the Hodges–Lehmann estimator, the median of the Walsh averages (Definition 5.1.2), which estimates the pseudomedian (Definition 5.1.1) and equals the median for symmetric populations.
- Asymptotics: $\sqrt n(\hat x_p-x_p)\xrightarrow{d}\mathcal{N}\big(0,p(1-p)/f(x_p)^2\big)$ (Theorem 5.2.1). Efficiencies relative to the mean equal those of the corresponding tests relative to the $t$ test:

| Population | median | Hodges–Lehmann |
|---|---|---|
| normal | $2/\pi\approx0.64$ | $3/\pi\approx0.955$ |
| Laplace | $2$ | $1.5$ |
| any continuous symmetric | no lower bound | $\ge0.864$ |

- Sign test: independence and a common median only; zeros are discarded (standard), split, or randomized; large $n$: `prop.test`, $z^2=\chi^2_1$.
- Binomial proportion: Clopper–Pearson (Definition 5.4.1, Beta quantiles, conservative), Wilson (Definition 5.4.2, inverts the score test, shrinks toward $1/2$), Agresti–Coull and plus four (Definition 5.4.3); avoid the Wald interval for small $n$.
- Scores: Pitman (raw deviations, permutation version of the $t$ test, Proposition 5.5.1), normal scores (Definition 5.5.2), and the family of linear signed rank statistics $\sum_ia(R_i^+)\boldsymbol{1}\{D_i>0\}$ (Definition 5.5.3) containing the sign ($a\equiv1$) and signed-rank ($a(i)=i$) tests, all distribution-free (Theorem 5.5.1).
- Robustness versus efficiency: $t$ and Pitman are efficient but easily upset by outliers; the sign test is the most robust and the least efficient under normality; the Wilcoxon test is the usual compromise when symmetry is plausible.

## Questions

1. For which kind of population is the pseudomedian different from the median? Compute it for the exponential distribution $\mathrm{Exp}(1)$.

   **Answer** For any symmetric population they coincide; they differ for skewed ones. If $X_1,X_2\overset{\text{iid}}{\sim}\mathrm{Exp}(1)$, then $X_1+X_2\sim\Gamma(2,1)$ with $\mathbb{P}(X_1+X_2>s)=(1+s)\mathrm{e}^{-s}$. The median of the sum solves $(1+s)\mathrm{e}^{-s}=1/2$, so $s\approx1.678$ and the pseudomedian is $0.839$. It lies between the median $\log2\approx0.693$ and the mean $1$.

2. Using Theorem 5.2.1, show that the sample median of a Cauchy sample is a consistent, asymptotically normal estimator of the center, and give its asymptotic variance.

   **Answer** For the Cauchy density $f(x)=\frac{1}{\pi(1+(x-\theta)^2)}$, $f(\theta)=1/\pi$, so $\sqrt n(\operatorname{Med}_n-\theta)\xrightarrow{d}\mathcal{N}(0,\pi^2/4)$: the median is consistent with asymptotic variance $\pi^2/(4n)\approx2.47/n$. By contrast, the sample mean of $n$ Cauchy observations is again standard Cauchy for every $n$ and does not converge at all.

3. Verify that for the Laplace distribution $\operatorname{ARE}(\hat\theta_{\mathrm{HL}},\bar X_n)=1.5$, and use the result of [3.6.4](/3.6.4) to state the ARE of the Wilcoxon signed-rank test relative to the $t$ test for normal and Laplace populations.

   **Answer** For $f(x)=\frac\lambda2\mathrm{e}^{-\lambda\lvert x\rvert}$, $\int f^2=2\int_0^\infty\frac{\lambda^2}{4}\mathrm{e}^{-2\lambda x}\,\mathrm{d}x=\lambda/4$ and $\sigma^2=2/\lambda^2$, so $12\sigma^2(\int f^2)^2=12\cdot\frac2{\lambda^2}\cdot\frac{\lambda^2}{16}=1.5$. The test has the same efficiencies as the estimator: $3/\pi\approx0.955$ under normality and $1.5$ under the Laplace distribution.

4. Is a sign test a linear signed rank statistic? Is the Pitman test?

   **Answer** The sign statistic $K=\sum_i\boldsymbol{1}\{D_i>0\}$ is the linear signed rank statistic with constant scores $a(i)\equiv1$; it is a (degenerate) rank statistic because it depends on the data only through the signs, which are part of the signed ranks. The Pitman statistic $\sum_i\lvert D_i\rvert\boldsymbol{1}\{D_i>0\}$ uses the observed magnitudes as scores; these are not a function of the ranks, so the Pitman test is not a rank test, although it is a permutation test of the same sign-flipping kind.

5. The recovery times (days) of $15$ patients after minor surgery are $3,4,5,5,6,7,8,9,10,12,14,16,18,22,45$. Which point estimate of the center and which test of $H_0\colon\theta=10$ would you report?

   **Answer** The data are clearly right-skewed, with a far outlier at $45$: the mean $12.3$ is pulled up by it, the median is $9$. Since the population is not plausibly symmetric, the sign test (and the median with its sign-test interval) is the safe choice; the Wilcoxon test and the Hodges–Lehmann estimate assume symmetry, and the $t$ test would be dominated by the value $45$. Here $6$ observations are above $10$, $8$ below and one equals $10$; discarding the zero, $K=6$ out of $14$ and the two-sided exact $p$-value is $0.79$, so there is no evidence that the median differs from $10$. The $95\%$ sign interval for the median, from the $4$th smallest to the $4$th largest observation, is $[5,16]$ (exact level $96.5\%$).
