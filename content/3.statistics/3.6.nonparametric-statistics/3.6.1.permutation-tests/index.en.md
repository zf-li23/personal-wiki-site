---
title: Permutation Tests
description: Why classical tests fail for tiny samples; constructing a permutation test from a test statistic and the reference set of rearrangements; exact and Monte Carlo (randomization) tests and why their p-values are valid; equivalent statistics; exchangeability and where it comes from; internal and external validity; permutation tests for a regression slope, nominal, actual and observed significance levels, size distortion of the t-test under a misspecified model and fair power comparisons; permutation tests versus the bootstrap.
---

Most of the tests met so far are parametric: the $t$-test, the $F$-test and the likelihood ratio test assume that the data come from a family of distributions known up to a few parameters, usually the normal family, and derive the null distribution of the test statistic from that assumption. A **nonparametric hypothesis test** ([Definition 6.1.1](/3.2.6#def-6.1.1) in [3.2.6](/3.2.6)) makes no such assumption about the shape of the population, so its null distribution has to come from somewhere else. This course studies where it can come from and what is gained and lost. Three sources recur throughout: rearrangements of the observed data (this chapter), ranks and other functions of the data whose distribution is the same for every continuous population ([3.6.2](/3.6.2)), and counts of events with a known probability under the null hypothesis, which lead to the binomial distribution ([3.6.3](/3.6.3)).

Two cautions belong at the start. First, "distribution-free" does not mean "assumption-free": every method in this course assumes something, such as independence, a common median, symmetry or exchangeability, and a nonparametric test is only as good as these assumptions. Second, freedom from distributional assumptions is bought with information. Nonparametric methods are attractive when samples are small, when the data are skewed, heavy-tailed or contain outliers, when only ranks or ordered categories are available, or when the population is simply unknown; but they are not the most efficient methods under every model, and under normality a well-chosen parametric test can be more powerful. How much is lost, and when nonparametric methods actually win, is measured by the relative efficiency of tests in [3.6.4](/3.6.4).

The permutation test is the most direct nonparametric idea and the conceptual root of most rank tests. We introduce it through a tiny example (§1.1), give the general construction (§1.2) and show that its $p$-values are exact (§1.3); we then examine the assumption it rests on, exchangeability, and its limits (§1.4), compare it with the $t$-test in regression, where a misspecified model distorts the $t$-test but not the permutation test (§1.5), and close with its relation to the bootstrap of [3.5.7](/3.5.7) (§1.6). The same logic underlies Fisher's randomization inference for causal effects in [3.9](/3.9).

## 1.1. A Tiny Example

**Example 1.1.1 (Two Students)** Two students, Jane and John, sit a test at the start of the semester and a final exam at the end. Their scores (in percent) are

| | Jane | John | Average |
|---|---|---|---|
| Pre-semester test | $70$ | $75$ | $72.5$ |
| Final exam | $76$ | $72$ | $74.0$ |

Based on this tiny sample we would like to know whether the course improves the students' knowledge.

A first instinct is to reach for a $t$-test: a two-sample $t$-test of $H_0$: "the mean scores are the same in the two tests" against $H_1$: "the final scores are higher", or, since the same students sit both tests, a **paired t-test** on the differences $+6$ and $-3$. Each of these requires that the observations (or the differences) be independent draws from a normal population, and the paired test would have a single degree of freedom. With two students nothing is known about the population and nothing can be checked, so these assumptions may simply fail, and if they do the inference could be badly distorted. Nor can we appeal to the **central limit theorem**: with $n = 2$ there is no asymptotics to speak of. We need a test whose validity does not depend on the shape of a population we know nothing about.

## 1.2. Constructing a Permutation Test

### 1.2.1. The Test Statistic

State the hypotheses in words:

$$
H_0\colon \text{the course brings no improvement in knowledge},\qquad H_1\colon \text{it brings a positive improvement}.
$$
A **test statistic** should increase monotonically as we move away from $H_0$ in the direction of $H_1$, so that large values are evidence against $H_0$. Unlike the statistics of classical tests, it does not have to be a **pivotal quantity**: we need not know its distribution in advance, because the permutation argument will supply it. A natural choice here is the difference between the "after" and "before" averages,

$$
S = \bar x_{\mathrm{F}} - \bar x_{\mathrm{P}},\qquad S_{\mathrm{obs}} = 74.0 - 72.5 = 1.5.
$$
The observed value is positive, but is it different from zero in any important sense? The key observation is that if $H_0$ is true, the labels "pre" and "final" carry no information: a shuffled data set, in which the four scores are reassigned to the two labels, is just as likely as the original one.

### 1.2.2. The Reference Distribution

Treat the four scores $70, 72, 75, 76$ as a pool and assign two of them to "pre" and two to "final". There are $\binom42 = 6$ ways to do this, and under $H_0$ they are equally likely. For each assignment $\pi$ compute $S_\pi = \bar x^*_{\mathrm{F}} - \bar x^*_{\mathrm{P}}$:

| $\pi$ | $70$ | $72$ | $75$ | $76$ | $S_\pi$ |
|---|---|---|---|---|---|
| 1 | P | P | F | F | $4.5$ |
| 2 | P | F | P | F | $1.5$ (observed) |
| 3 | P | F | F | P | $0.5$ |
| 4 | F | P | P | F | $-0.5$ |
| 5 | F | P | F | P | $-1.5$ |
| 6 | F | F | P | P | $-4.5$ |

For the one-sided alternative "a positive improvement" we ask what fraction of the six values $S_\pi$ is greater than or equal to $S_{\mathrm{obs}}$. The answer, $2/6 = 1/3$, is the **p-value** of the permutation test, and there is clearly no evidence of an improvement. If instead we ask whether the course led to any change in performance, the two-sided $p$-value counts the values with $\lvert S_\pi\rvert \ge \lvert S_{\mathrm{obs}}\rvert$, giving $4/6 = 2/3$.

The table also shows the limits of such a small experiment: the smallest attainable $p$-value is $1/6$, so no outcome whatsoever could be significant at the $5\%$ level. A permutation test with $M$ equally likely rearrangements can reject at level $\alpha$ only if $1/M \le \alpha$.

**Remark 1.2.1** The table pools the four scores as if they were two independent samples, which is how the example is usually presented. Because the same two students sit both tests, a reference set that respects the design permutes only within each student: under $H_0$ each student's two scores may be swapped, which flips the sign of that student's difference. The four sign patterns of the differences $(+6, -3)$ give mean differences $1.5, 4.5, -1.5, -4.5$, so the one-sided $p$-value is $2/4 = 1/2$. In general the reference set must consist of exactly those rearrangements that $H_0$ (together with the design) makes equally likely; paired designs are treated this way in [3.6.8](/3.6.8).

### 1.2.3. The General Construction

**Definition 1.2.1 (Permutation Test)** Let $\boldsymbol{X}$ denote the data and let $\mathcal{G}$ be a finite group of $M$ rearrangements $g$ of the data (permutations of observations, of group labels, or sign changes) such that, under $H_0$, $g\boldsymbol{X}$ has the same distribution as $\boldsymbol{X}$ for every $g \in \mathcal{G}$. For a test statistic $T$, the set $\{T(g\boldsymbol{X})\colon g\in\mathcal{G}\}$ is the *reference distribution*, and the **permutation test** rejects $H_0$ for small values of the $p$-value

$$
p(\boldsymbol{X}) = \frac{1}{M}\,\#\{g \in \mathcal{G}\colon T(g\boldsymbol{X}) \ge T(\boldsymbol{X})\}.
$$

For two samples of sizes $n$ and $m$, $\mathcal{G}$ is the group of all $(n+m)!$ permutations of the pooled observations, but a statistic that depends only on which observations fall into which group takes each of its $\binom{n+m}{n}$ possible values equally often, so it suffices to enumerate the $\binom{n+m}{n}$ splits, as in the table above. In practice the procedure has four steps:

1. choose a test statistic that is large (or extreme) under $H_1$;
2. shuffle the data in the ways that $H_0$ makes equally likely ("force the null hypothesis to be true");
3. compute the statistic for every rearrangement to obtain its null sampling distribution;
4. locate the observed value in this distribution and compute the one- or two-sided $p$-value, the proportion of rearrangements giving a value at least as extreme as the observed one.

The hypothesis tested is a strong one: not merely that two means are equal, but that the data-generating mechanism is invariant under the rearrangements, for instance that the treatment has absolutely no effect on any outcome. When $H_0$ is rejected, the conclusion is that something other than the random allocation explains the observed difference.

## 1.3. Exact Tests and Randomization Tests

### 1.3.1. Exactness

**Definition 1.3.1 (Exact Test)** A test of $H_0$ is an **exact test** at level $\alpha$ if its probability of a type I error is at most $\alpha$ for every distribution in $H_0$ and every sample size $n$. A test whose type I error probability tends to $\alpha$ only as $n \to \infty$ is called asymptotic, or approximate.

The $t$-test is exact when the data are normal; for non-normal data its level is correct only asymptotically, through the central limit theorem. The permutation test is exact under the sole assumption that the rearrangements are equally likely under $H_0$, however small the sample.

**Theorem 1.3.1** Under the conditions of Definition 1.2.1, $\mathbb{P}_{H_0}\bigl(p(\boldsymbol{X}) \le u\bigr) \le u$ for every $u \in [0, 1]$. If the $M$ values $T(g\boldsymbol{X})$ are distinct with probability one, equality holds whenever $uM$ is an integer. Consequently the test that rejects when $p(\boldsymbol{X}) \le \alpha$ is exact at level $\alpha$.

**Proof** Fix a data set $\boldsymbol{x}$. Since $\mathcal{G}$ is a group, $\{hg\colon h\in\mathcal{G}\} = \mathcal{G}$ for every $g$, so the multiset of values $\{T(hg\boldsymbol{x})\colon h\in\mathcal{G}\}$ is the same for every point $g\boldsymbol{x}$ of the orbit, and

$$
p(g\boldsymbol{x}) = \frac1M\#\{h\colon T(h\boldsymbol{x}) \ge T(g\boldsymbol{x})\}
$$
is the proportion of the $M$ values that are at least as large as $T(g\boldsymbol{x})$. For any list of $M$ numbers, at most $\lfloor uM\rfloor$ of them have this proportion $\le u$ (exactly $\lfloor uM\rfloor$ if they are distinct). Hence $\frac1M\#\{g\colon p(g\boldsymbol{x}) \le u\} \le u$ for every $\boldsymbol{x}$. Now let $G$ be uniformly distributed on $\mathcal{G}$ and independent of $\boldsymbol{X}$. Under $H_0$, $g\boldsymbol{X}$ has the distribution of $\boldsymbol{X}$ for each fixed $g$, so $G\boldsymbol{X}$ does too, and

$$
\mathbb{P}\bigl(p(\boldsymbol{X}) \le u\bigr) = \mathbb{P}\bigl(p(G\boldsymbol{X}) \le u\bigr) = \mathbb{E}\Bigl[\frac1M\#\{g\colon p(g\boldsymbol{X}) \le u\}\Bigr] \le u. \qquad\square
$$

Because the permutation $p$-value takes only the values $k/M$, the attainable levels are discrete: with the six assignments of Example 1.1.1 only the levels $1/6, 2/6, \dots$ can be attained exactly. Exactness in the sense of Definition 1.3.1 then means that the type I error never exceeds the nominal level; to attain a level between two attainable values exactly one would need the **randomized test** of [3.2.5](/3.2.5), which is discussed in [3.6.4](/3.6.4).

### 1.3.2. Monte Carlo Permutation Tests

The number of rearrangements grows explosively: $\binom{20}{10} = 184756$, and $20! \approx 2.43\times10^{18}$. In practice we draw a large random sample of $B$ rearrangements and use them in place of the full reference set, an application of the **Monte Carlo method**. Such a test is often called a *randomization test*. With $T_b = T(g_b\boldsymbol{X})$ for random $g_1, \dots, g_B$, the estimate

$$
\hat p = \frac{1 + \#\{b\colon T_b \ge T_{\mathrm{obs}}\}}{B + 1}
$$
is itself a valid $p$-value: under $H_0$ the observed statistic and the $B$ simulated ones are exchangeable, so the rank of $T_{\mathrm{obs}}$ among the $B + 1$ values is uniformly distributed (with no ties), and the argument of Theorem 1.3.1 applies with $M = B + 1$. The simpler $\#\{b\colon T_b \ge T_{\mathrm{obs}}\}/B$ is common in code and differs only slightly for large $B$, but it can return $p = 0$, which no permutation test should. Viewed as an estimate of the exact permutation $p$-value $p$, $\hat p$ has standard error about $\sqrt{p(1-p)/B}$, so the accuracy can be made as high as we wish by choosing $B$ large.

**Example 1.3.1 (Price and Supply)** We wish to test whether the quantity supplied ($Q$) of a good is correlated with its market price ($P$), against the one-sided alternative of a positive correlation. A sample of $20$ prices and the corresponding quantities is

| $P$ | 5.0 | 4.8 | 4.7 | 4.0 | 5.3 | 4.1 | 5.5 | 4.7 | 3.3 | 4.0 | 4.0 | 4.6 | 5.3 | 3.0 | 3.5 | 3.9 | 4.7 | 5.0 | 5.2 | 4.6 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $Q$ | 60 | 59 | 58 | 47 | 65 | 48 | 67 | 70 | 55 | 63 | 62 | 65 | 71 | 56 | 59 | 60 | 74 | 77 | 78 | 62 |

A natural statistic is the sample (Pearson) **correlation coefficient** $r$, whose observed value is $r_{\mathrm{obs}} = 0.6183$. If there is no association, any pairing of the $20$ prices with the $20$ quantities is as likely as the observed one; so we keep the order of the $Q$ values and permute the $20$ values of $P$. There are $20! \approx 2.43\times10^{18}$ permutations, and we draw $50{,}000$ of them at random:

```r
set.seed(123456)
price <- c(5.0, 4.8, 4.7, 4.0, 5.3, 4.1, 5.5, 4.7, 3.3, 4.0,
           4.0, 4.6, 5.3, 3.0, 3.5, 3.9, 4.7, 5.0, 5.2, 4.6)
quantity <- c(60, 59, 58, 47, 65, 48, 67, 70, 55, 63,
              62, 65, 71, 56, 59, 60, 74, 77, 78, 62)
n <- 20; nrep <- 50000
r_obs <- cor(price, quantity)
r_perm <- numeric(nrep)
for (i in 1:nrep) {
  y <- sample(price, n, replace = FALSE)    # a random permutation of the prices
  r_perm[i] <- cor(quantity, y)
}
pval <- mean(r_perm >= r_obs)               # one-sided p-value
round(c(r_obs = r_obs, pval = pval), 4)
```

```text
 r_obs   pval
0.6183 0.0016
```

The one-sided $p$-value is about $0.002$ (the run above gives $0.0016$, the run in the figure $0.0021$; the Monte Carlo standard error is about $0.0002$), and on the basis of this very small $p$-value we reject the hypothesis of no correlation. For a two-sided alternative we count the permuted correlations with $\lvert r_\pi\rvert \ge \lvert r_{\mathrm{obs}}\rvert$, which gives about $0.004$.

![Monte Carlo permutation distribution of the sample correlation between the permuted prices and the quantities (50,000 permutations), with the observed correlation 0.6183 and its mirror image for the two-sided test.](./plots/perm-null-correlation.py)

### 1.3.3. Equivalent Statistics

The correlation coefficient was a natural choice, but are there other options, and would another choice change the $p$-value? It does not, whenever the new statistic is an increasing function of the old one over the reference set.

**Proposition 1.3.1** If $T' = a + bT$ with $b > 0$, where $a$ and $b$ may depend on the data but take the same value for every rearrangement in $\mathcal{G}$, then the permutation tests based on $T$ and $T'$ have identical $p$-values.

**Proof** For every $g$, $T'(g\boldsymbol{X}) \ge T'(\boldsymbol{X})$ if and only if $T(g\boldsymbol{X}) \ge T(\boldsymbol{X})$, so the two counts in Definition 1.2.1 coincide. $\square$

In Example 1.3.1, consider $S = \sum_{i=1}^n P_iQ_i$. Since

$$
r = \frac{\sum_i P_iQ_i - n\bar P\bar Q}{\sqrt{\sum_i (P_i - \bar P)^2\sum_i (Q_i - \bar Q)^2}},
$$
and permuting the $P_i$ changes neither $\bar P$, $\bar Q$ nor the two sums of squares, $r$ is an increasing linear function of $S$ over the reference set, and both statistics give the same $p$-value. The simpler $S$ is cheaper to compute. In the same way, for two samples with a fixed pooled sum, the difference of the sample means and the sum of the first sample are equivalent statistics ([3.6.9](/3.6.9)). Statistics that are not monotone functions of each other, such as the mean difference and the median difference, generally give different $p$-values; the choice should be made before seeing the data, according to the alternative of interest.

## 1.4. When Is a Permutation Test Valid?

The permutation test needs neither normality nor constant variance, nor any particular assumption about an underlying population; it is conceptually simple; the null hypothesis can be a general statement; and the test statistic need not be pivotal. What it does need is that shuffling the observations is legitimate, that is, that the data can be treated as exchangeable under $H_0$.

### 1.4.1. Exchangeability

**Definition 1.4.1 (Exchangeability)** Random variables $X_1, \dots, X_n$ are **exchangeable** if their joint distribution is invariant under every permutation of the indices:

$$
(X_1, \dots, X_n) \overset{d}{=} (X_{\pi(1)}, \dots, X_{\pi(n)})\quad\text{for every permutation } \pi \text{ of } \{1,\dots,n\}.
$$
Equivalently, when a joint density exists, $f(x_1, \dots, x_n) = f(x_{\pi(1)}, \dots, x_{\pi(n)})$ for all $\pi$.

**Proposition 1.4.1** **Independent and identically distributed** random variables are exchangeable; exchangeable random variables need not be independent.

**Proof** If $X_1, \dots, X_n$ are i.i.d. with density $f$, the joint density $\prod_i f(x_i)$ is a symmetric function of its arguments. The converse fails by the examples below. $\square$

**Example 1.4.1** (1) Let $(X, Y)$ be bivariate normal with $\mu_X = \mu_Y$, $\sigma_X = \sigma_Y$ and correlation $\rho$. The density depends on $(x, y)$ only through $(x - \mu)^2 + (y - \mu)^2$ and $(x - \mu)(y - \mu)$, so $f(x, y) = f(y, x)$: the pair is exchangeable, but dependent when $\rho \ne 0$.

(2) Draw balls one at a time from an urn with $B$ black and $W$ white balls, without replacement. The probability of a sequence depends only on how many black and white balls it contains, not on their order; for example

$$
\mathbb{P}(\text{b, w, b}) = \frac{B}{B+W}\cdot\frac{W}{B+W-1}\cdot\frac{B-1}{B+W-2} = \frac{W}{B+W}\cdot\frac{B}{B+W-1}\cdot\frac{B-1}{B+W-2} = \mathbb{P}(\text{w, b, b}).
$$
The colors of the draws are therefore exchangeable but not independent. The same holds for Pólya's urn, in which each drawn ball is returned together with $c$ further balls of its color: $\mathbb{P}(\text{b, w, b}) = \frac{B}{B+W}\cdot\frac{W}{B+W+c}\cdot\frac{B+c}{B+W+2c} = \mathbb{P}(\text{w, b, b})$. Sampling without replacement is exactly the mechanism of random assignment in an experiment, which is why it matters here.

For infinite sequences, **de Finetti's theorem** ([3.7.6](/3.7.6)) shows that exchangeable sequences are mixtures of i.i.d. sequences; this is the probabilistic basis of hierarchical models in Bayesian statistics.

Exchangeability enters the permutation test through the condition of Definition 1.2.1. It can arise in two ways.

- Random sampling: If, under $H_0$, all observations are i.i.d. from a common population (for two samples: both populations are the same), the pooled observations are exchangeable by Proposition 1.4.1.
- Random assignment: In a randomized experiment, think of each unit's response as fixed before the experiment. Under the "sharp" null hypothesis that the treatment has no effect on any unit, the responses would have been the same whatever the assignment, and the assignment itself is a random permutation of the treatment labels chosen by the experimenter. The permutation distribution is then the actual randomization distribution of the statistic, with no assumption about any population at all. This requires that one unit's treatment does not affect another unit's response and that the treatment is the same for all recipients; these conditions belong to the formulation of causal effects in terms of **potential outcomes** ([3.9](/3.9)) and are distinct from exchangeability itself.

In a **completely randomized design** ([3.8.2](/3.8.2)), for example, the treatment labels are allocated completely at random, so under the null hypothesis of no treatment effect every relabeling with the same group sizes is equally likely and the condition holds. In a design with blocks or pairs only the rearrangements within blocks are equally likely (Remark 1.2.1).

### 1.4.2. Internal and External Validity

The two sources of exchangeability lead to conclusions of different scope.

| Aspect | Classical $t$-test | Permutation test |
|---|---|---|
| Core assumption | i.i.d. sampling, normality and so on | exchangeability under $H_0$ |
| Requirement on sampling | random sampling from the population | none beyond exchangeability, which random assignment guarantees |
| Scope of the conclusion | the population (external validity) | the units actually studied (internal validity) |
| Typical setting | inference about a population from a random sample | randomized experiments, convenience samples, volunteers |

Random assignment of treatments ensures the *internal validity* of the comparison: within the experiment, a significant difference cannot be explained by the allocation alone. Generalizing the conclusion to a wider population (*external validity*) depends on how the units were obtained, and requires random sampling or a substantive argument that the units are representative. If the units were randomly sampled, the permutation test also supports population conclusions, and it remains exact. When the experiment effectively involves the whole population of interest and the only data are ranks, a permutation test is the best test available; random allocation is essential for its validity, which may not always be possible for ethical reasons. Ludbrook and Dudley (1998) argue on these grounds that permutation tests are preferable to $t$- and $F$-tests in biomedical research, where experimental animals are rarely a random sample from anything.

### 1.4.3. Limitations

The permutation test is not a panacea.

- It compares values, ranks or counts across groups, and so it does not apply to every testing problem, including some obvious and simple ones. For a single sample and $H_0\colon \mu = \mu_0$, permuting the observations changes neither their mean nor their median: there is nothing to shuffle. A one-sample test can be built only from an additional assumption, such as symmetry about $\mu_0$, which makes the signs of the deviations exchangeable; this leads to the sign-flipping tests of [3.6.3](/3.6.3) and the Pitman test of [3.6.5](/3.6.5). For a tiny single sample, therefore, a permutation test of the mean is not available as an alternative to the $t$-test.
- Exchangeability fails for some null hypotheses. If $X_i \sim \mathcal{N}(\mu_i, \sigma_i^2)$ independently and $H_0$ says only that all $\mu_i$ are equal, observations with different variances are not exchangeable, and a permutation test of equal means is not exact (the Behrens–Fisher situation). Conversely, the strong null of identical distributions can be rejected because of differences in spread or shape rather than in location, so a rejection should be interpreted with care.
- The computational cost can be high, although a Monte Carlo test with a few thousand rearrangements is cheap for most problems; and with very small samples the discreteness of the reference distribution limits the attainable significance levels.

### 1.4.4. Historical Notes

Permutation tests date back to the 1930s, when they were proposed by Fisher (1935) and Pitman (1937, 1938) among others. Fisher used them as the logical justification of the $t$-test rather than as a practical method; in 1936 he wrote:

> Actually, the statistician does not carry out this very simple and very tedious process, but his conclusions have no justification beyond the fact that they agree with those which could have been arrived at by this elementary method.

Modern computing has made these methods, once too "tedious" to apply, readily accessible. George Cobb (2007) drew the consequence for teaching:

> What we teach is largely the technical machinery of numerical approximations based on the normal distribution and its many subsidiary cogs. This machinery was once necessary, because the conceptually simpler alternative based on permutations was computationally beyond our reach. Before computers statisticians had no choice. These days we have no excuse.

## 1.5. Permutation Tests in Regression

### 1.5.1. Testing a Slope

Consider the simple regression model

$$
y_i = \beta_0 + \beta_1x_i + \varepsilon_i,\qquad i = 1, \dots, n,
$$
and the hypothesis $H_0\colon \beta_1 = 0$ that $x$ has no linear effect on $y$. We take the $x_i$ as non-random and assume that the errors are exchangeable. Under $H_0$, $y_i = \beta_0 + \varepsilon_i$, so the responses are exchangeable whatever the value of $\beta_0$, and every pairing of the $y$ values with the fixed $x$ values is equally likely. The permutation test shuffles the $y$ values against the $x$ values, exactly as in Example 1.3.1. As test statistic we may use the **least squares** slope $b_1$ or the Pearson correlation; since $b_1 = r\sqrt{S_{yy}/S_{xx}}$ and $S_{xx}$, $S_{yy}$ do not change under permutations, the two are equivalent by Proposition 1.3.1.

We use this setting for two purposes: to show that the permutation test remains exact even when the regression model is misspecified, here by fitting it through the origin, and to compare the powers of the permutation test and the $t$-test fairly.

### 1.5.2. Three Significance Levels

**Definition 1.5.1 (Significance Levels)** (1) The *nominal* significance level is the level a test is designed to achieve, very often $5\%$ or $1\%$; it is chosen before the data are collected, and in many situations, for example with discrete statistics or approximate null distributions, it cannot be achieved precisely. (2) The *actual* significance level, or size, is the true probability that the test rejects $H_0$ when $H_0$ is true. (3) The *observed* (empirical) significance level is computed from the data: the probability, if $H_0$ were true, of a value of the test statistic as extreme as or more extreme than the one observed, that is, the $p$-value.

**Definition 1.5.2 (Size Distortion)** The difference between the actual and the nominal significance level of a test is its **size distortion**. It is *downward* if the actual level is smaller than the nominal one (the test is conservative) and *upward* if it is larger (the test is liberal).

An exact test has no upward size distortion. A test used outside the conditions under which its null distribution was derived generally has one.

### 1.5.3. A Monte Carlo Experiment

To get a fair comparison, the data are generated with i.i.d. disturbances $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$, for which the $t$-test is optimal when the model is correctly specified. The model fitted is a regression through the origin, $y_i = \beta_1x_i + \varepsilon_i$, and its slope is tested with the usual $t$-test on $n - 1$ degrees of freedom; the permutation test uses the correlation and $5000$ random permutations (`perm.cor.test` from the package `jmuOutlier`). The design $x$ is generated once and kept fixed.

```r
library(jmuOutlier)              # perm.cor.test: permutation test for a correlation
set.seed(12345)
n <- 15; sig <- 0.05; nrep <- 2000
tcrit <- qt(1 - sig / 2, df = n - 1)   # no intercept in the fitted model
beta0 <- 0; beta1 <- 0                 # case 1; the null hypothesis beta1 = 0 is true
x <- rnorm(n)                          # fixed design, created just once
tstat <- pvalp <- numeric(nrep)
for (i in 1:nrep) {
  y <- beta0 + beta1 * x + rnorm(n)
  fit <- lm(y ~ x - 1)                 # mis-specified if beta0 != 0
  tstat[i] <- coef(summary(fit))[, "t value"]
  pvalp[i] <- perm.cor.test(x, y, "two.sided", "pearson", num.sim = 5000)$p.value
}
powert <- mean(abs(tstat) > tcrit)     # rejection rate of the t-test
powerp <- mean(pvalp <= sig)           # rejection rate of the permutation test
```

In case 1, $\beta_0 = \beta_1 = 0$: the data-generating process has no intercept, the fitted model is correct, $H_0$ is true, and both tests reject about $5\%$ of the time. In case 2 we rerun the code with `beta0 <- 1`, keeping $\beta_1 = 0$. Now the model is underspecified, and

```text
> powert
[1] 0.007
> powerp
[1] 0.043
```

The $t$-test, nominally at $5\%$, actually rejects a true null hypothesis in only $0.7\%$ of the samples: a downward size distortion of about $4.3$ percentage points. The permutation test still rejects at very nearly $5\%$ (the difference from $0.05$ is Monte Carlo error): even with the misspecified model it remains exact with respect to the nominal level. A run with $n = 30$ gave, for $\beta_0 = 1$,

| $\beta_1$ | $0$ | $0.1$ | $0.2$ | $0.3$ | $0.4$ | $0.5$ | $0.6$ | $0.8$ | $1.0$ |
|---|---|---|---|---|---|---|---|---|---|
| Permutation test | $0.050$ | $0.083$ | $0.165$ | $0.307$ | $0.484$ | $0.685$ | $0.840$ | $0.976$ | $0.999$ |
| $t$-test | $0.010$ | $0.035$ | $0.091$ | $0.192$ | $0.351$ | $0.543$ | $0.723$ | $0.947$ | $0.994$ |

(with $\beta_0 = 0$ both rejection rates at $\beta_1 = 0$ were $0.050$ and $0.051$). The $t$-test has a downward size distortion and appears less powerful throughout.

### 1.5.4. Why the t-Test Is Distorted

Why are the usual central $t$ critical values no longer correct? Write $S_x = \sum_i x_i$ and $S_{xx}^0 = \sum_i x_i^2$ (uncentered). Fitting through the origin gives

$$
b = \frac{\sum_i x_iy_i}{S_{xx}^0},\qquad s^2 = \frac{1}{n-1}\sum_i (y_i - bx_i)^2,\qquad T = \frac{b}{s/\sqrt{S_{xx}^0}},
$$
and if the model is correct, $T \sim t_{n-1}$ under $H_0$.

**Theorem 1.5.1** Let $y_i = \beta_0 + \beta_1x_i + \varepsilon_i$ with $\varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$, and let $T$ be the $t$-statistic for $\beta_1 = 0$ in the model fitted through the origin. Then

$$
T = \frac{Z + \beta_1\sqrt{S_{xx}^0}/\sigma + \delta}{\sqrt{V/(n-1)}},\qquad \delta = \frac{\beta_0S_x}{\sigma\sqrt{S_{xx}^0}},
$$
where $Z \sim \mathcal{N}(0, 1)$ and $V$ are independent and $V$ has a **noncentral chi-square distribution** with $n - 1$ degrees of freedom and noncentrality parameter $\lambda = \beta_0^2\bigl(n - S_x^2/S_{xx}^0\bigr)/\sigma^2$. Under $H_0$, $T$ therefore has a doubly noncentral $t$-distribution, which is the central $t_{n-1}$ only when $\beta_0 = 0$.

**Proof** Write $\boldsymbol{y} = \beta_0\boldsymbol{1} + \beta_1\boldsymbol{x} + \boldsymbol{\varepsilon}$ and let $P$ be the orthogonal projection onto $\boldsymbol{x}$. Then $b = \boldsymbol{x}^{\mathsf T}\boldsymbol{y}/S_{xx}^0 = \beta_1 + \beta_0S_x/S_{xx}^0 + \boldsymbol{x}^{\mathsf T}\boldsymbol{\varepsilon}/S_{xx}^0$, so $b\sqrt{S_{xx}^0}/\sigma = \beta_1\sqrt{S_{xx}^0}/\sigma + \delta + Z$ with $Z = \boldsymbol{x}^{\mathsf T}\boldsymbol{\varepsilon}/(\sigma\sqrt{S_{xx}^0}) \sim \mathcal{N}(0, 1)$. The residual vector is $(I - P)\boldsymbol{y} = (I - P)(\beta_0\boldsymbol{1} + \boldsymbol{\varepsilon})$, which is independent of $P\boldsymbol{\varepsilon}$ and hence of $Z$, and $V = \lVert(I - P)\boldsymbol{y}\rVert^2/\sigma^2$ is a sum of squares of $n - 1$ independent unit-variance normal coordinates with means given by $(I - P)\beta_0\boldsymbol{1}/\sigma$, whose squared length is $\beta_0^2(n - S_x^2/S_{xx}^0)/\sigma^2 = \lambda$. Finally $s^2 = \sigma^2V/(n-1)$. $\square$

The two noncentralities act in opposite directions. The omitted intercept inflates the residual variance, and so the denominator: since $\lambda/(n-1) \approx \beta_0^2/\sigma^2$, the denominator is roughly $\sqrt{1 + \beta_0^2/\sigma^2}$ times too large, which pulls $T$ towards zero and causes a downward distortion. The shift $\delta$ of the numerator pushes $T$ away from zero and causes an upward distortion. For a design drawn as $x_i \sim \mathcal{N}(0, 1)$, $\delta \approx \beta_0\sqrt n\,\bar x/\sigma$ is itself of order one whatever $n$, so the net distortion depends on the particular design: with $\beta_0 = \sigma = 1$ and $\delta \approx 0$, $T \approx Z/\sqrt2$ and the actual level is about $\mathbb{P}(\lvert Z\rvert > 1.96\sqrt2) \approx 0.006$, close to the $0.007$ observed above; with $\delta = 2$ it is about $\mathbb{P}(\lvert Z + 2\rvert > 2.77) \approx 0.22$. The permutation test, by contrast, uses the correlation, which is unaffected by the intercept, and is exact by Theorem 1.3.1 because the $y_i = \beta_0 + \varepsilon_i$ are exchangeable under $H_0$.

### 1.5.5. Comparing Powers Fairly

Is a downward size distortion an advantage? A test with nominal level $5\%$ and actual level $0.05\%$ makes far fewer type I errors, but it is not the test it claims to be, its distortion depends on the unknown $\beta_0$ and on the design, and the conservatism is paid for with power. A size distortion in either direction means that the reported significance levels are wrong.

Power comparisons are therefore valid, strictly, only between tests with the same actual significance level. The one exception is when test $A$ has a lower actual level than test $B$ and yet a higher rejection rate whenever the null hypothesis is false; then $A$ is better without qualification, as the permutation test is in the table above. In all other cases the "true" power is not clear. One way to deal with this is to size-adjust any test that exhibits size distortion: "jiggle" its critical values until it rejects $5\%$ of the time when the null is true, and only then compute power curves and compare them.

![Rejection rates against the true slope for the permutation test and for the t-test of the slope in a regression fitted through the origin, when the true model has intercept 1 (n = 30, 4000 replications). Left: a design with delta = 0, where the t-test is strongly conservative. Right: a design with delta = 2, where it rejects a true null hypothesis 22% of the time. The dotted curves use size-adjusted critical values.](./plots/misspecified-power.py)

The figure shows both directions. On the left ($\delta = 0$) the $t$-test is conservative and loses power everywhere; once size-adjusted it coincides with the permutation test, because the only effect of the misspecification is a common rescaling of $T$. On the right ($\delta = 2$) the $t$-test appears far more powerful for positive slopes, but only because it rejects $22\%$ of the time when $\beta_1 = 0$; for negative slopes it is much worse, and even after size adjustment its two-sided rejection region is lopsided (it falls below $5\%$ near $\beta_1 = -0.3$, so it is a biased test). This is also why simulations with different sample sizes can appear to reverse the ranking of the two tests: for one design the $t$-test had a downward and for another an upward distortion, and its "power" was compared with that of a test of a different size. The magnitudes of the distortions and of the powers are specific to the choice of $\beta_0$ and of the design.

## 1.6. Permutation Tests and the Bootstrap

Both permutation tests and the **bootstrap** ([3.5.7](/3.5.7)) recompute a statistic on many rearranged or resampled versions of the observed data, but their logic is quite different.

| | Permutation test | Bootstrap |
|---|---|---|
| Resampling | rearranges the observed data without replacement | samples with replacement from the empirical distribution function $F_n$ |
| What it targets | the null distribution of a test statistic under exchangeability | the sampling variability of an estimator under the actual (unknown) distribution |
| Validity | exact for every $n$ (Theorem 1.3.1) | approximate, justified asymptotically |
| Natural use | hypothesis testing | standard errors and confidence intervals |
| Null hypothesis | the strong null: the labels do not matter (for example, the two distributions are identical) | a specific parameter value, other features of the distributions left free |

A permutation test asks whether the samples could have come from the same population, using a statistic only as a summary; a bootstrap test looks at the statistic itself. In this sense the permutation test makes a "deeper", more general comparison, but of a stronger null hypothesis. The bootstrap itself involves no hypothesis: it estimates the sampling distribution of the statistic from $F_n$. To use it for a test, the resampling must be done from a distribution that satisfies $H_0$, for example from the two samples after shifting them to a common mean (the **nonparametric bootstrap** test of [3.5.7](/3.5.7), §7.3.4); resampling from the unadjusted data would describe the statistic under the alternative, not under the null. As a rule of thumb, a permutation test is best for testing hypotheses and the bootstrap is best for estimating standard errors and confidence intervals; the two are compared again for medians in [3.6.9](/3.6.9).

## Summary

- Construction: Choose a test statistic that is large under $H_1$ (it need not be pivotal); rearrange the data in the ways $H_0$ makes equally likely; the $p$-value is the proportion of rearrangements giving a value at least as extreme as the observed one (Definition 1.2.1). Statistics that are increasing functions of each other over the reference set give the same $p$-value (Proposition 1.3.1).
- Exactness: Under $H_0$, $\mathbb{P}(p \le \alpha) \le \alpha$ for every sample size (Theorem 1.3.1); the Monte Carlo version with $\hat p = (1 + \#\{T_b \ge T_{\mathrm{obs}}\})/(B + 1)$ is valid as well. With $M$ rearrangements no $p$-value is smaller than $1/M$.
- Assumption: Exchangeability under $H_0$ (Definition 1.4.1): implied by i.i.d. sampling, not equivalent to it, and guaranteed by random assignment under the sharp null hypothesis of no effect. The reference set must match the design (pairs and blocks permute only within themselves).
- Scope: Random assignment gives internal validity; external validity depends on how the units were sampled. Permutation tests do not apply to every problem (a single sample has nothing to permute without a symmetry assumption) and test a strong null hypothesis.
- Misspecification: A $t$-test applied to a misspecified model has a size distortion (Definition 1.5.2), downward or upward depending on the design (Theorem 1.5.1); the permutation test stays exact. Powers may be compared only at equal actual levels, if necessary after size adjustment.
- Permutation versus bootstrap: the permutation test rearranges the data without replacement under $H_0$ and is exact, so it is the tool for testing; the bootstrap resamples with replacement from $F_n$, is approximate and serves for standard errors and intervals; a bootstrap test must resample from a distribution satisfying $H_0$.

## Questions

1. In an experiment, $2$ males and $2$ females are randomly assigned to each of three treatments A, B and C, with responses (males; females) A: $4, 6$; $6, 8$; B: $6, 8$; $8, 10$; C: $8, 10$; $17, 17$. Propose a permutation test of the hypothesis that the treatments have the same effect. How many relabelings must be considered?

   **Answer** A natural statistic is the between-treatment sum of squares $\sum_j n_j(\bar y_j - \bar y)^2$ (equivalently the one-way ANOVA $F$ statistic, which is a monotone function of it once the total sum of squares is fixed), since large values indicate differences among treatments. If treatments were assigned to all $12$ subjects completely at random, the reference set consists of the $\frac{12!}{4!\,4!\,4!} = 34650$ allocations into three groups of four. Since the design balanced the sexes, the randomization was done within each sex (sex is a block), so the correct reference set permutes treatment labels only within males and within females: $\bigl(\frac{6!}{2!\,2!\,2!}\bigr)^2 = 90^2 = 8100$ relabelings. Permuting across sexes would mix the sex effect into the reference distribution.
2. Two independent samples $X_1, \dots, X_{n_1}$ and $Y_1, \dots, Y_{n_2}$ are compared by a permutation test of $H_0$: both are drawn from the same distribution, against the alternative that the mean of $X$ is larger. Show that $S = \sum_{i=1}^{n_1}X_i$ is an equivalent statistic to $T = \bar X - \bar Y$.

   **Answer** Let $A = \sum_iX_i + \sum_jY_j$ be the pooled sum, which is the same for every relabeling. Then $\bar Y = (A - S)/n_2$ and
   $$
   T = \frac{S}{n_1} - \frac{A - S}{n_2} = S\Bigl(\frac{1}{n_1} + \frac{1}{n_2}\Bigr) - \frac{A}{n_2},
   $$
   an increasing linear function of $S$ with coefficients that do not change under relabeling. By Proposition 1.3.1 the two statistics give the same $p$-value.
3. Is a downward size distortion beneficial? For example, a test with nominal $\alpha = 0.05$ has actual level $0.0005$, so it almost never makes a type I error.

   **Answer** No. The test does not do what it claims: the reported level is wrong, the distortion depends on unknown features of the model (in Theorem 1.5.1 on $\beta_0$ and on the design), and the same mechanism can produce an upward distortion in another situation. A conservative test also has lower power than a test of correct size, so real effects are missed. A test should have actual level as close as possible to the nominal one, and comparisons of power are meaningful only at equal actual levels.
4. Simulated power curves of the permutation test and of the $t$-test in a regression through the origin (true intercept $\beta_0 = 1$) showed the permutation test more powerful for $n = 15$ but the $t$-test more powerful for $n = 60$. Why can the comparison reverse?

   **Answer** The $t$-test is not of size $5\%$ in either case. By Theorem 1.5.1 its null distribution is shifted by $\delta = \beta_0\sum_ix_i/(\sigma\sqrt{\sum_ix_i^2})$ and scaled down by the inflated residual variance; with $x_i$ drawn from $\mathcal{N}(0, 1)$, $\delta$ is of order one for every $n$ and its value depends on the particular draw of $x$. For the design with $n = 15$, $\delta$ was small and the test conservative; for the design with $n = 60$, $\delta$ was large enough to give an upward distortion, so the $t$-test rejected more often both under $H_0$ and under alternatives with slopes of the same sign as $\delta$. The reversal is an artifact of comparing tests of different sizes; after size adjustment, the comparison would reflect power alone.
5. Can a permutation test replace the one-sample $t$-test of $H_0\colon \mu = \mu_0$ for a tiny sample, using the sample mean as test statistic?

   **Answer** Not directly: all permutations of a single sample have the same mean, so the reference distribution is degenerate. One needs an additional assumption that creates a group of equally likely rearrangements, typically that the distribution is symmetric about $\mu_0$ under $H_0$; then the signs of the deviations $X_i - \mu_0$ can be flipped independently, giving $2^n$ equally likely sign patterns. This is the Pitman (sign-flipping) permutation test, and with ranks in place of the deviations it becomes the Wilcoxon signed-rank test of [3.6.3](/3.6.3). Even then, with $n = 2$ the smallest attainable $p$-value is $1/4$.
