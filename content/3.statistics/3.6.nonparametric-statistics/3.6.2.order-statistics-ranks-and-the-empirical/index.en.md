---
title: Order Statistics, Ranks and the Empirical Distribution Function
description: Order statistics and their distributions, uniform order statistics and the probability integral transform; ranks and antiranks, the uniform distribution of the rank vector and the moments of ranks; distribution-free statistics and rank statistics; U-statistics and their kernels; the empirical distribution function, the Kolmogorov distance, its distribution-free property and the DKW inequality; pointwise confidence intervals versus confidence bands for a distribution function; the empirical quantile function and Q-Q plots with confidence bands.
---

The permutation test of [3.6.1](/3.6.1) obtains a null distribution by rearranging the observed data, so the reference distribution must be recomputed for every data set. This chapter introduces the objects that turn that idea into ready-made, tabulated procedures. If we discard the numerical values of the observations and keep only their order, the ranks, the result has the same distribution for every continuous population: a rank statistic is distribution-free, and its null distribution can be computed once and for all. At the other extreme we keep all the values but view them through the empirical distribution function, which estimates the whole population distribution; its distance from a hypothesized distribution function is again distribution-free, and the Dvoretzky–Kiefer–Wolfowitz inequality turns it into a confidence band that holds for every population and every sample size. Between the two sit the order statistics, which connect ranks and values, and the U-statistics, which give a common framework for many estimators and test statistics of the following chapters.

Several of these objects have already appeared: order statistics and quantiles in probability theory ([3.1.7](/3.1.7)), the **empirical distribution function** and the **Glivenko–Cantelli theorem** in [3.2.1](/3.2.1), and the Kolmogorov–Smirnov test in [3.2.6](/3.2.6). Here we collect what nonparametric inference needs from them and develop the parts that are new: ranks and their distribution (§2.2–2.3), U-statistics (§2.4), the distribution-free property of the Kolmogorov distance and the DKW inequality (§2.6), confidence bands (§2.7) and Q–Q plots with bands (§2.8). The limiting theory of the empirical process behind the Kolmogorov–Smirnov test follows in [3.6.6](/3.6.6).

## 2.1. Order Statistics

### 2.1.1. Definition

We usually pay no attention to the order in which the observations $X_1, \dots, X_n$ of a sample arrive. Many questions, however, concern the ordered values: the probability that the highest score in an exam exceeds $98$, the $80$th percentile of a sample of heart rates, the range of a set of measurements.

**Definition 2.1.1 (Order Statistics)** Let $X_1, \dots, X_n$ be independent observations from a population with continuous distribution function $F$. Continuity implies $\mathbb{P}(X_i = X_j) = 0$ for $i \ne j$, so with probability one the observations can be ordered with strict inequalities,

$$
X_{(1)} < X_{(2)} < \cdots < X_{(n)},
$$
and $X_{(i)}$ is called the $i$-th **order statistic**.

Order statistics of particular interest are the minimum $X_{(1)}$, the maximum $X_{(n)}$ and the **sample median**

$$
\tilde X = \begin{cases} X_{((n+1)/2)}, & n \text{ odd},\\[2pt] \tfrac12\bigl(X_{(n/2)} + X_{(n/2+1)}\bigr), & n \text{ even},\end{cases}
$$
together with measures of dispersion built from them: the range $X_{(n)} - X_{(1)}$, the **interquartile range** (the difference of the upper and lower sample quartiles) and the semi-interquartile range (half of it). In R, `median(x)` returns `NA` if `x` contains missing values, and `median(x, na.rm = TRUE)` computes the median of the remaining ones; for `x <- c(2, 3, 5, NA, 4, NA, 6)` the latter gives $4$.

### 2.1.2. Distributions

The distributions of order statistics were derived in [3.1.7](/3.1.7); we restate them for reference.

**Theorem 2.1.1** Let $X_1, \dots, X_n$ be i.i.d. with distribution function $F$ and density $f$.

1. The distribution function of $X_{(i)}$ is the probability that at least $i$ of the $n$ observations are at most $x$:
   $$
   F_{(i)}(x) = \mathbb{P}(X_{(i)} \le x) = \sum_{k=i}^n \binom nk F(x)^k\bigl(1 - F(x)\bigr)^{n-k};
   $$
   in particular $F_{(1)}(x) = 1 - \bigl(1 - F(x)\bigr)^n$ and $F_{(n)}(x) = F(x)^n$.
2. The density of $X_{(i)}$ is
   $$
   f_{(i)}(x) = \frac{n!}{(i-1)!\,(n-i)!}F(x)^{i-1}\bigl(1 - F(x)\bigr)^{n-i}f(x).
   $$
3. For $j < k$ the joint density of $(X_{(j)}, X_{(k)})$ is, for $x < y$,
   $$
   f_{(j,k)}(x, y) = \frac{n!}{(j-1)!\,(k-j-1)!\,(n-k)!}F(x)^{j-1}\bigl(F(y) - F(x)\bigr)^{k-j-1}\bigl(1 - F(y)\bigr)^{n-k}f(x)f(y);
   $$
   in particular $f_{(1,n)}(x, y) = n(n-1)\bigl(F(y) - F(x)\bigr)^{n-2}f(x)f(y)$.
4. The joint density of all the order statistics is $n!\,f(x_1)\cdots f(x_n)$ for $x_1 < \cdots < x_n$.

**Proof** Part 1: $\{X_{(i)} \le x\}$ is the event that at least $i$ of the observations are at most $x$, and the number of such observations is $\mathrm{Bin}(n, F(x))$. Part 2 follows by differentiating (the sum telescopes), or heuristically: for $X_{(i)}$ to lie in $[x, x + \mathrm{d}x]$, one observation must fall there, $i - 1$ below $x$ and $n - i$ above, and the multinomial coefficient counts the ways to choose them. Parts 3 and 4 follow by the same multinomial argument with three groups and with $n$ groups. $\square$

The uniform case is the key to the rest of the chapter.

**Corollary 2.1.1** If $U_1, \dots, U_n \overset{\text{iid}}{\sim} \mathrm{U}(0, 1)$, then $U_{(i)} \sim \mathrm{Beta}(i, n - i + 1)$, with $\mathbb{E}U_{(i)} = \frac{i}{n+1}$. If $F$ is continuous and $X_1, \dots, X_n \overset{\text{iid}}{\sim} F$, then $\bigl(F(X_{(1)}), \dots, F(X_{(n)})\bigr)$ has the distribution of $(U_{(1)}, \dots, U_{(n)})$, whatever $F$ is.

**Proof** With $F(x) = x$ and $f = 1$ on $(0, 1)$, part 2 of Theorem 2.1.1 is the $\mathrm{Beta}(i, n - i + 1)$ density ([3.1.7](/3.1.7), where the densities are plotted). For continuous $F$, the **probability integral transform** gives $F(X_i) \overset{\text{iid}}{\sim} \mathrm{U}(0, 1)$, and since $F$ is nondecreasing, the order of the $F(X_i)$ is that of the $X_i$ (ties among the $F(X_i)$ have probability zero). $\square$

The second statement says that, on the probability scale, the order statistics of every continuous population behave alike. For instance, $\mathbb{P}\bigl(F(X_{(n)}) > 1 - \varepsilon\bigr) = 1 - (1 - \varepsilon)^n$ for every continuous $F$.

**Example 2.1.1** A sample of $12$ observations is taken from $\mathrm{U}(0, 1)$. The largest value exceeds $0.95$ unless all twelve are at most $0.95$, so $\mathbb{P}(X_{(12)} > 0.95) = 1 - 0.95^{12} = 0.460$. By Corollary 2.1.1 the same number is the probability that the largest of $12$ observations from any continuous population exceeds the population's $95\%$ quantile.

## 2.2. Ranks

### 2.2.1. Ranks and Antiranks

**Definition 2.2.1 (Rank)** Let $X_1, \dots, X_n$ be a sample from a continuous distribution with order statistics $X_{(1)} < \cdots < X_{(n)}$. The observation $X_i$ has **rank** $R_i$ among $X_1, \dots, X_n$ if $X_i = X_{(R_i)}$; this is well defined when there are no ties, which holds with probability one. Equivalently,

$$
R_i = 1 + \sum_{j \ne i}\boldsymbol{1}\{X_j < X_i\},
$$
one plus the number of observations smaller than $X_i$. The vector $\boldsymbol{R} = (R_1, \dots, R_n)$ is the rank vector; $R_i$ is also called the $i$-th rank-order statistic. The inverse permutation $\boldsymbol{D} = (D_1, \dots, D_n)$, defined by $X_{(i)} = X_{D_i}$, gives the indices of the ordered observations (the antiranks).

The functional form is often written with $I_+(t) = \boldsymbol{1}\{t > 0\}$ as $R_i = 1 + \sum_{j\ne i}I_+(X_i - X_j)$; it is the form used to compute expectations of rank statistics. In R, `rank(x)` returns the ranks and `order(x)` returns the antiranks:

```r
set.seed(1)
x <- sample(1:30, 5)
x
rank(x)      # x[1] = 8 is the 2nd smallest value
order(x)     # the smallest value is x[5]
x[order(x)]  # sorting
```

```text
[1]  8 11 17 25  6
[1] 2 3 4 5 1
[1] 5 1 2 3 4
[1]  6  8 11 17 25
```

### 2.2.2. The Distribution of the Rank Vector

**Theorem 2.2.1** Let $X_1, \dots, X_n$ be i.i.d. from a continuous distribution (more generally, exchangeable with no ties with probability one), and let $\mathcal{R}$ be the set of all $n!$ permutations of $(1, 2, \dots, n)$. Then the rank vector $\boldsymbol{R}$ is uniformly distributed over $\mathcal{R}$:

$$
\mathbb{P}(\boldsymbol{R} = \boldsymbol{r}) = \frac{1}{n!}\quad\text{for every } \boldsymbol{r} \in \mathcal{R}.
$$
Moreover, for i.i.d. observations $\boldsymbol{R}$ is independent of the vector of order statistics.

**Proof** For a permutation $\pi$ let $\boldsymbol{X}^\pi = (X_{\pi(1)}, \dots, X_{\pi(n)})$. The rank of its $i$-th coordinate is $R_{\pi(i)}$, so the rank vector of $\boldsymbol{X}^\pi$ is $\boldsymbol{R}\circ\pi$. By exchangeability (Definition 1.4.1) $\boldsymbol{X}^\pi \overset{d}{=} \boldsymbol{X}$, hence $\boldsymbol{R}\circ\pi \overset{d}{=} \boldsymbol{R}$ and $\mathbb{P}(\boldsymbol{R} = \boldsymbol{r}) = \mathbb{P}(\boldsymbol{R}\circ\pi = \boldsymbol{r}) = \mathbb{P}(\boldsymbol{R} = \boldsymbol{r}\circ\pi^{-1})$. As $\pi$ ranges over all permutations, $\boldsymbol{r}\circ\pi^{-1}$ ranges over all of $\mathcal{R}$, so the $n!$ probabilities are equal; since ties have probability zero, they add up to one. For independence, the joint density $n!\prod f(x_{(i)})$ of the order statistics (Theorem 2.1.1) is the same whichever $\boldsymbol{r}$ produced them: $\mathbb{P}\bigl(\boldsymbol{R} = \boldsymbol{r},\ (X_{(1)},\dots,X_{(n)}) \in A\bigr) = \int_A\prod_i f(x_i)\,\mathrm{d}\boldsymbol{x} = \frac{1}{n!}\mathbb{P}\bigl((X_{(1)},\dots,X_{(n)}) \in A\bigr)$. $\square$

**Corollary 2.2.1** Under the conditions of Theorem 2.2.1, for $i \ne j$ and distinct $r, s \in \{1, \dots, n\}$,

$$
\mathbb{P}(R_i = r) = \frac1n,\qquad \mathbb{P}(R_i = r, R_j = s) = \frac{1}{n(n-1)},
$$
$$
\mathbb{E}R_i = \frac{n+1}{2},\quad \operatorname{Var}(R_i) = \frac{(n+1)(n-1)}{12},\quad \operatorname{Cov}(R_i, R_j) = -\frac{n+1}{12},\quad \operatorname{Corr}(R_i, R_j) = -\frac{1}{n-1}.
$$

**Proof** The probabilities count the permutations with prescribed values in one or two places: $(n-1)!/n!$ and $(n-2)!/n!$. So $R_i$ is uniform on $\{1, \dots, n\}$, with mean $\frac{n+1}{2}$ and variance $\frac1n\sum_{r=1}^nr^2 - \bigl(\frac{n+1}{2}\bigr)^2 = \frac{(n+1)(2n+1)}{6} - \frac{(n+1)^2}{4} = \frac{(n+1)(n-1)}{12}$. For the covariance, $\sum_iR_i = \frac{n(n+1)}{2}$ is constant, so

$$
0 = \operatorname{Var}\Bigl(\sum_iR_i\Bigr) = n\operatorname{Var}(R_1) + n(n-1)\operatorname{Cov}(R_1, R_2),
$$
which gives $\operatorname{Cov}(R_i, R_j) = -\operatorname{Var}(R_1)/(n-1) = -\frac{n+1}{12}$ and the correlation $-\frac{1}{n-1}$. $\square$

A further property explains much of the appeal of ranks: they are invariant under strictly increasing transformations. If $g$ is strictly increasing, the ranks of $g(X_1), \dots, g(X_n)$ are those of $X_1, \dots, X_n$. A rank procedure therefore gives the same answer whether the data are analyzed on the original scale, on a log scale or on any other monotone rescaling, and it is unaffected by how far an outlier lies from the rest: the largest observation has rank $n$ however large it is.

## 2.3. Distribution-Free Statistics and Rank Statistics

**Definition 2.3.1 (Distribution-Free Statistic)** Let $Y_1, \dots, Y_n$ have a joint distribution $D$ belonging to a family $\mathcal{F}$ of possible joint distributions. A statistic $T(Y_1, \dots, Y_n)$ is **distribution-free** over $\mathcal{F}$ if the distribution of $T$ is the same for every $D \in \mathcal{F}$.

**Definition 2.3.2 (Rank Statistic)** A statistic that depends on $X_1, \dots, X_n$ only through the rank vector $\boldsymbol{R}$ is called a **rank statistic**.

**Theorem 2.3.1** Let $\mathcal{F}$ be the family of joint distributions of $n$ i.i.d. continuous random variables. Every rank statistic $V(\boldsymbol{R})$ is distribution-free over $\mathcal{F}$.

**Proof** By Theorem 2.2.1, $\boldsymbol{R}$ is uniform on $\mathcal{R}$ for every member of $\mathcal{F}$, so $\mathbb{P}\bigl(V(\boldsymbol{R}) = v\bigr) = \#\{\boldsymbol{r}\in\mathcal{R}\colon V(\boldsymbol{r}) = v\}/n!$ does not depend on the distribution. $\square$

This is why we may discard the numerical values and keep only the ranks: the null distribution of the test statistic becomes a combinatorial object that can be computed, or tabulated, without knowing the population. Distribution-freeness refers to the null hypothesis: under alternatives, the distribution of a rank statistic does depend on the populations, and so does its power.

**Example 2.3.1 (The Shift Problem)** Let $X_1, \dots, X_n$ and $Y_1, \dots, Y_m$ be independent samples from continuous distributions with distribution functions $F(x)$ and $G(x) = F(x - \Delta)$, $-\infty < \Delta < \infty$, so that $\Delta$ is a shift parameter. How can we test $H_0\colon\Delta = 0$ against $H_1\colon\Delta > 0$?

The permutation idea of [3.6.1](/3.6.1) applies: if $H_0$ is true, shuffled data sets look like the real data; otherwise they look different, and the position of the observed statistic among the shuffled ones gives a $p$-value. To obtain a test whose null distribution does not depend on the data, combine the two samples and let $R_1, \dots, R_n$ and $Q_1, \dots, Q_m$ be the ranks of the $X$'s and $Y$'s in the combined sample; $(R_1, \dots, R_n, Q_1, \dots, Q_m)$ is a permutation of $(1, 2, \dots, m + n)$. To compare the $X$-ranks with the $Y$-ranks it suffices to consider a statistic of the $X$-ranks alone, and Wilcoxon proposed the rank sum

$$
W = \sum_{i=1}^nR_i.
$$
$W$ is a function of the data only through the rank vector. Under $H_0$ the $m + n$ observations are i.i.d. and continuous, so by Theorem 2.3.1 the distribution of $W$ is the same for every continuous $F$: it is the permutation distribution of the sum of $n$ numbers drawn without replacement from $\{1, \dots, m + n\}$. Small values of $W$ (the $X$'s tend to be smaller) support $H_1$. This is the **Wilcoxon rank-sum test** of [3.2.6](/3.2.6), whose theory is developed in [3.6.9](/3.6.9).

## 2.4. U-Statistics

### 2.4.1. Definition

Many common estimators, such as the sample mean, the sample variance and the sample covariance, share a structure: they average a function of a few observations over all subsets of the sample. Recognizing this structure gives one framework for their properties (unbiasedness, consistency, asymptotic normality) instead of treating each in isolation; it extends the use of order and rank information to numerical features such as correlations; and it underlies the Wilcoxon signed-rank and Mann–Whitney statistics of the following chapters.

**Definition 2.4.1 (U-Statistic)** Let $X_1, \dots, X_n$ be i.i.d. and let $\theta = \mathbb{E}\,h(X_1, \dots, X_k)$ be a population feature, where $k \le n$ and the kernel $h$ is a symmetric function of $k$ arguments: $h(x_{i_1}, \dots, x_{i_k})$ is unchanged by any permutation of its arguments. The **U-statistic** with kernel $h$ is

$$
U_n = \binom nk^{-1}\sum_{1\le i_1 < \cdots < i_k \le n}h(X_{i_1}, \dots, X_{i_k}),
$$
the average of $h$ over all $\binom nk$ subsets of size $k$ of the sample. The number $k$ is the degree (or order) of the kernel.

By linearity of expectation, $\mathbb{E}U_n = \theta$: every U-statistic is an **unbiased estimator** of its feature. Symmetry costs nothing: a non-symmetric kernel $h$ with $\mathbb{E}\,h(X_1, \dots, X_k) = \theta$ can be replaced by its symmetrization $h^*(x_1, \dots, x_k) = \frac{1}{k!}\sum_\pi h(x_{\pi(1)}, \dots, x_{\pi(k)})$, which has the same expectation. For example, $h(x_1, x_2) = \boldsymbol{1}\{x_1 \le x_2\}$ is not symmetric, since $h(x_1, x_2) \ne h(x_2, x_1)$ in general; its symmetrization is $\frac12\bigl(1 + \boldsymbol{1}\{x_1 = x_2\}\bigr)$, which equals $\frac12$ almost surely for a continuous population. Indicators of this kind become informative with two samples, where $\mathbb{P}(X \le Y)$ compares two populations.

### 2.4.2. Examples

**Example 2.4.1** (1) *Mean.* With $k = 1$ and $h(x) = x$, $U_n = \frac1n\sum_iX_i = \bar X$: the sample mean is a U-statistic of degree one.

(2) *Variance.* If $\mu$ is known, $h(x) = (x - \mu)^2$ gives the unbiased $\frac1n\sum_i(X_i - \mu)^2$. If $\mu$ is unknown, use $k = 2$ and $h(x_1, x_2) = \frac12(x_1 - x_2)^2$, since $\mathbb{E}\frac12(X_1 - X_2)^2 = \sigma^2$. Then

$$
U_n = \frac{1}{n(n-1)}\sum_{i<j}(X_i - X_j)^2 = \frac{1}{n-1}\sum_i(X_i - \bar X)^2 = S^2,
$$
the unbiased **sample variance**.

(3) *Square of the mean.* For $\theta = \mu^2$, the kernel $h(x_1, x_2) = x_1x_2$ gives $U_n = \binom n2^{-1}\sum_{i<j}X_iX_j$, which uses all pairwise products and is unbiased, unlike $\bar X^2$, whose expectation is $\mu^2 + \sigma^2/n$.

(4) *Gini mean difference.* For $\theta = \mathbb{E}\lvert X_1 - X_2\rvert$, a measure of spread, the kernel is $h(x_1, x_2) = \lvert x_1 - x_2\rvert$, which is symmetric. Ecologists measuring dissolved oxygen on four days obtain $6.2, 5.8, 6.5, 5.9\,\mathrm{mg\,L^{-1}}$; the six absolute differences are $0.4, 0.3, 0.3, 0.7, 0.1, 0.6$, so $U_4 = 2.4/6 = 0.4\,\mathrm{mg\,L^{-1}}$.

(5) *Wilcoxon signed-rank statistic.* For $\theta = \mathbb{P}(X_1 + X_2 > 0)$, the kernel $h(x_1, x_2) = \boldsymbol{1}\{x_1 + x_2 > 0\}$ is symmetric. The signed-rank statistic $S_+$ of [3.6.3](/3.6.3) can be written as $\sum_{i\le j}\boldsymbol{1}\{X_i + X_j > 0\}$, a count of positive pairwise averages; up to the $n$ terms with $i = j$ and a factor $\binom n2$, it is this U-statistic.

(6) *Two samples.* The definition extends to two samples with kernels $h(x_1, \dots, x_k; y_1, \dots, y_l)$ averaged over subsets of both. With $h(x; y) = \boldsymbol{1}\{x < y\}$, the two-sample U-statistic $\frac{1}{nm}\sum_{i,j}\boldsymbol{1}\{X_i < Y_j\}$ estimates $\mathbb{P}(X < Y)$; it is the Mann–Whitney form of the rank-sum statistic of Example 2.3.1 ([3.6.9](/3.6.9)).

### 2.4.3. Properties

Beyond unbiasedness, U-statistics have two important properties, stated here without proof.

- *Optimality.* Every symmetric statistic is a function of the order statistics, and $U_n$ is the conditional expectation of $h(X_1, \dots, X_k)$ given them. For the nonparametric family of all distributions for which $\theta$ exists, the order statistics are complete and sufficient, so $U_n$ is the **uniformly minimum variance unbiased estimator** of $\theta$ in that family (Halmos, 1946). Its precision guarantee is thus that of the best unbiased estimator when nothing is assumed about the population.
- *Asymptotic normality* (Hoeffding, 1948). Let $h_1(x) = \mathbb{E}\,h(x, X_2, \dots, X_k)$ and $\zeta_1 = \operatorname{Var}\bigl(h_1(X_1)\bigr)$. If $\mathbb{E}h^2 < \infty$ and $\zeta_1 > 0$, then
  $$
  \sqrt n\,(U_n - \theta) \xrightarrow{d} \mathcal{N}(0, k^2\zeta_1).
  $$
  For the sample mean, $k = 1$ and $\zeta_1 = \sigma^2$, the ordinary central limit theorem.

**Remark 2.4.1** Order statistics are sometimes described as a "trivial" U-statistic with $k = n$: the kernel $h(x_1, \dots, x_n) = \operatorname{median}(x_1, \dots, x_n)$ is symmetric and there is only one subset of size $n$, so $U_n$ is the sample median. This is a limiting case without the averaging that gives U-statistics their properties, and it estimates without bias only $\mathbb{E}\operatorname{median}(X_1, \dots, X_n)$, which changes with $n$ and generally differs from the population median. The theory above concerns kernels of fixed degree $k$. Note also that the word "kernel" here means the function $h$; it is unrelated to the **kernel function** of density estimation ([3.2.3](/3.2.3)).

## 2.5. The Empirical Distribution Function

**Definition 2.5.1 (Empirical Distribution Function)** Let $X_1, \dots, X_n$ be i.i.d. with distribution function $F$. The empirical distribution function (EDF) is

$$
F_n(x) = \frac1n\sum_{i=1}^n\boldsymbol{1}\{X_i \le x\},\qquad x \in \mathbb{R}.
$$

$F_n$ is a step function rising by $1/n$ at each observation (by $k/n$ at a value observed $k$ times); it is itself a distribution function, that of the uniform distribution on the observed values. Its basic properties ([3.2.1](/3.2.1)) all follow from one fact: for each fixed $x$,

$$
nF_n(x) = \sum_{i=1}^n\boldsymbol{1}\{X_i \le x\} \sim \mathrm{Bin}\bigl(n, F(x)\bigr).
$$
Hence $\mathbb{E}F_n(x) = F(x)$ and $\operatorname{Var}\bigl(F_n(x)\bigr) = \frac1nF(x)\bigl(1 - F(x)\bigr)$: $F_n(x)$ is an unbiased estimator of $F(x)$, it is consistent ($F_n(x) \xrightarrow{p} F(x)$, indeed almost surely), and by the de Moivre–Laplace theorem it is asymptotically normal, $\sqrt n\bigl(F_n(x) - F(x)\bigr) \xrightarrow{d} \mathcal{N}\bigl(0, F(x)(1 - F(x))\bigr)$. The Glivenko–Cantelli theorem strengthens consistency to uniform convergence, $\sup_x\lvert F_n(x) - F(x)\rvert \xrightarrow{\text{a.s.}} 0$, and is often called the fundamental theorem of (nonparametric) statistics.

The EDF can also be viewed as a nonparametric maximum likelihood estimator. Among all distribution functions $G$, consider the likelihood $L(G) = \prod_{i=1}^n\mathbb{P}_G(\{x_i\})$, the probability that $G$ assigns to the observed values. If the distinct values $x_1, \dots, x_m$ occur $k_1, \dots, k_m$ times and $p_j = \mathbb{P}_G(\{x_j\})$, then $L = \prod_jp_j^{k_j}$ with $\sum_jp_j \le 1$; maximizing $\sum_jk_j\log p_j$ under this constraint gives $p_j = k_j/n$, which is exactly $F_n$. Any distribution that puts mass outside the observed values, in particular any continuous one, has likelihood zero.

In R, `ecdf(x)` returns the EDF as a function, which can be evaluated and plotted:

```r
n <- 30
x <- rnorm(n)
Fn <- ecdf(x)                 # Fn is a function
plot(Fn, verticals = TRUE, do.points = FALSE)
curve(pnorm(x), add = TRUE, col = 2)   # the true CDF
```

Functions of the form "p followed by a distribution name" (`pnorm`, `pexp`, `pbinom`, ...) give the theoretical distribution functions for comparison; as $n$ increases the EDF gets closer to the CDF.

## 2.6. The Kolmogorov Distance

### 2.6.1. Definition and Computation

Is a given sample an exponential sample? A histogram with the exponential density superimposed is suggestive but depends on the bins; comparing the EDF with the hypothesized distribution function is more direct, and the size of the largest discrepancy summarizes the comparison.

**Definition 2.6.1 (Kolmogorov Distance)** The **Kolmogorov distance** between two distribution functions $G$ and $F$ is $D_{\mathrm{K}}(G, F) = \sup_x\lvert G(x) - F(x)\rvert$. For a sample with EDF $F_n$ and a hypothesized continuous $F$ we write

$$
D_n = D_{\mathrm{K}}(F_n, F) = \sup_x\lvert F_n(x) - F(x)\rvert = \max_{1\le i\le n}\max\Bigl\{\frac in - F(x_{(i)}),\ F(x_{(i)}) - \frac{i-1}{n}\Bigr\},
$$
where $x_{(1)} < \cdots < x_{(n)}$ is the ordered sample.

The formula holds because between consecutive order statistics $F_n$ is constant while $F$ is nondecreasing, so on each interval the largest gap occurs at an endpoint: just before $x_{(i)}$, where $F_n = \frac{i-1}{n}$, or at $x_{(i)}$, where $F_n = \frac in$. The computation needs only the sorted data:

```r
ksdist <- function(x, CDF, ...) {
  sortx <- sort(x); n <- length(x)
  distup   <- (1:n) / n - CDF(sortx, ...)        # right end of each jump
  distdown <- CDF(sortx, ...) - (0:(n - 1)) / n  # left end of each jump
  max(pmax(distup, distdown))                    # Kolmogorov distance
}
set.seed(10)
x <- rexp(100)
ksdist(x, pexp, rate = 1)
ks.test(x, "pexp", rate = 1)$statistic
ks.test(x, "pnorm", mean = 0, sd = 0.1)$statistic
```

```text
[1] 0.08466882
         D
0.08466882
        D
0.8077886
```

The distance to the true $\mathrm{Exp}(1)$ distribution is $0.085$; the distance to a badly wrong target, $\mathcal{N}(0, 0.1^2)$, is $0.81$. Does such a dramatic change of the distance with the target distribution show that the Kolmogorov test is not distribution-free? It does not: distribution-freeness is a statement about the null distribution of $D_n$, computed when the target $F$ is the true distribution, and says nothing about the distance to a wrong target. That the distance is large for a wrong target is exactly what gives the test its power.

Other distances compare the whole curves rather than their largest gap. The *one-sided* Kolmogorov statistics are $D_n^+ = \sup_x\bigl(F_n(x) - F(x)\bigr)$ and $D_n^- = \sup_x\bigl(F(x) - F_n(x)\bigr)$, with $D_n = \max(D_n^+, D_n^-)$; they test one-sided alternatives, they are distribution-free by the argument below, $D_n^+$ and $D_n^-$ have the same distribution by the symmetry $u \mapsto 1 - u$ of the uniform distribution, and their exact distributions are considerably easier to derive than that of $D_n$ ([3.6.6](/3.6.6)). The Cramér–von Mises distance

$$
D_{\mathrm{CvM}}(F_n, F) = \int\bigl(F_n(x) - F(x)\bigr)^2\,\mathrm{d}F(x)
$$
averages the squared discrepancy, and the Anderson–Darling distance weights it by $1/\bigl(F(1 - F)\bigr)$ to emphasize the tails; they lead to the **Cramér–von Mises test** and the **Anderson–Darling test** ([3.3.5](/3.3.5)).

### 2.6.2. The Distribution-Free Property

To test $H_0\colon X_1, \dots, X_n \overset{\text{iid}}{\sim} F$ against "otherwise" with the statistic $D_n$, we need its null distribution, and we should show that it does not depend on $F$. The idea is that a monotone transformation of the $x$-axis does not change vertical distances.

**Theorem 2.6.1** If $F$ is continuous and $X_1, \dots, X_n \overset{\text{iid}}{\sim} F$, then $D_n = D_{\mathrm{K}}(F_n, F)$ has the same distribution as $D_{\mathrm{K}}(U_n, F_{\mathrm{U}})$, where $U_n$ is the EDF of a sample of size $n$ from $\mathrm{U}(0, 1)$ and $F_{\mathrm{U}}(y) = y$. Thus $D_n$ is distribution-free over the family of continuous distributions.

**Proof** Let $U_i = F(X_i)$. By the probability integral transform, $U_1, \dots, U_n \overset{\text{iid}}{\sim} \mathrm{U}(0, 1)$, because $\mathbb{P}(F(X) \le y) = \mathbb{P}(X \le F^{-1}(y)) = F(F^{-1}(y)) = y$ for continuous $F$. Let $U_n(y) = \frac1n\sum_i\boldsymbol{1}\{U_i \le y\}$ be their EDF. For every $x$, $\boldsymbol{1}\{X_i \le x\} = \boldsymbol{1}\{F(X_i) \le F(x)\}$ almost surely, so $F_n(x) = U_n(F(x))$ and

$$
\sup_{x\in\mathbb{R}}\lvert F_n(x) - F(x)\rvert = \sup_{x\in\mathbb{R}}\bigl\lvert U_n(F(x)) - F(x)\bigr\rvert = \sup_{0<y<1}\lvert U_n(y) - y\rvert,
$$
the last step because a continuous $F$ takes every value in $(0, 1)$ (and the endpoints add nothing). Hence $\mathbb{P}(D_n \le t) = \mathbb{P}\bigl(\sup_y\lvert U_n(y) - y\rvert \le t\bigr)$ for every $t$. $\square$

The null distribution of $D_n$ can therefore be computed once, for the uniform distribution, and used for every continuous $F$. If $F$ has jumps, the same argument shows that $D_n$ is stochastically smaller than in the continuous case, so the test based on the continuous-case critical values is conservative.

![Left: the EDF of an exponential sample of size 100 and the Exp(1) distribution function, with the Kolmogorov distance marked. Right: the empirical distribution of sqrt(n) D_n over 10000 samples of size 20 from four different continuous populations, which coincide as Theorem 2.6.1 asserts, together with their limit as n grows.](./plots/ks-distance.py)

### 2.6.3. The Limiting Distribution and the DKW Inequality

The distance $D_n$ shrinks at rate $1/\sqrt n$, and Kolmogorov (1933) found the limiting distribution of the rescaled distance.

**Theorem 2.6.2 (Kolmogorov)** If $F$ is continuous, then for every $d > 0$,

$$
\lim_{n\to\infty}\mathbb{P}\bigl(\sqrt n\,D_n \le d\bigr) = K(d) = 1 - 2\sum_{k=1}^\infty(-1)^{k-1}\mathrm{e}^{-2k^2d^2}.
$$

The quantiles $K^{-1}(0.95) = 1.358$ and $K^{-1}(0.99) = 1.628$ give the large-sample critical values $1.358/\sqrt n$ and $1.628/\sqrt n$ of the Kolmogorov–Smirnov test. The approximation is adequate for moderate samples; for small $n$ the exact null distribution is tabulated, and R's `ks.test` computes exact $p$-values by default when $n < 100$ and there are no ties. In [3.6.6](/3.6.6) we shall see that $K$ is the distribution of $\sup_t\lvert B(t)\rvert$ for a Brownian bridge $B$, the limit of the uniform empirical process $\sqrt n\bigl(U_n(t) - t\bigr)$.

A handy non-asymptotic complement holds for every sample size.

**Theorem 2.6.3 (Dvoretzky–Kiefer–Wolfowitz Inequality)** For every distribution function $F$, every $n \ge 1$ and every $\varepsilon > 0$,

$$
\mathbb{P}\Bigl(\sup_x\lvert F_n(x) - F(x)\rvert > \varepsilon\Bigr) \le 2\mathrm{e}^{-2n\varepsilon^2}.
$$

Dvoretzky, Kiefer and Wolfowitz (1956) proved the inequality with an unspecified constant in place of $2$; Massart (1990) showed that the constant $2$ is valid, and it cannot be improved, since by Theorem 2.6.2 the leading term of $1 - K(\varepsilon\sqrt n)$ is $2\mathrm{e}^{-2n\varepsilon^2}$. The inequality needs no continuity of $F$ and gives an explicit rate for the Glivenko–Cantelli theorem: the probability of a uniform error larger than $\varepsilon$ decays exponentially in $n$.

## 2.7. Confidence Intervals and Confidence Bands for F

### 2.7.1. Pointwise Intervals

Recall that a confidence interval for a parameter $\theta$ with confidence level $1 - \alpha$ is a random interval $\bigl(l(\boldsymbol{X}), u(\boldsymbol{X})\bigr)$ with $\mathbb{P}\bigl(l(\boldsymbol{X}) < \theta < u(\boldsymbol{X})\bigr) \ge 1 - \alpha$ for every $\theta$. For a distribution function there are two different questions. The pointwise question fixes $x$ and asks for an interval $C(x) = \bigl(L(x), U(x)\bigr)$ such that, for every $F$,

$$
\mathbb{P}\bigl(F(x) \in C(x)\bigr) \ge 1 - \alpha.
$$
Since $nF_n(x) \sim \mathrm{Bin}(n, F(x))$, this is a question about a binomial proportion. The exact **Clopper–Pearson interval** ([3.6.5](/3.6.5)) gives, with $k = nF_n(x)$,

$$
\Bigl(\beta_{\alpha/2}(k, n - k + 1),\ \beta_{1-\alpha/2}(k + 1, n - k)\Bigr),
$$
where $\beta_q(a, b)$ is the $q$ quantile of $\mathrm{Beta}(a, b)$ (with lower limit $0$ when $k = 0$ and upper limit $1$ when $k = n$). In R, `binom.test(sum(x <= x0), n)$conf.int` computes it.

### 2.7.2. Simultaneous Bands

**Definition 2.7.1 (Confidence Band for a Distribution Function)** A pair of functions $L(x) \le U(x)$ computed from the sample is a $1 - \alpha$ confidence band for $F$ if, for every $F$,

$$
\mathbb{P}\bigl(L(x) \le F(x) \le U(x)\ \text{for all } x\bigr) \ge 1 - \alpha.
$$
Such bands are also called simultaneous confidence intervals or confidence envelopes.

Joining the pointwise intervals does not give a band. If $A$ and $B$ are the events that the intervals at $x_1$ and $x_2$ cover, each has probability $1 - \alpha$, but $\mathbb{P}(A\cap B)$ is in general smaller: it equals $(1 - \alpha)^2$ only if the two events were independent (they are not; $F_n(x_1)$ and $F_n(x_2)$ are positively correlated), and Bonferroni's inequality gives only $\mathbb{P}(A\cap B) \ge 1 - 2\alpha$. Over a continuum of $x$ the simultaneous coverage of the joined pointwise intervals can be far below $1 - \alpha$. At the same level, a band is therefore wider than the pointwise intervals. Its advantage is that it can be used to judge whole candidate distributions: any $F$ that leaves the band is rejected at level $\alpha$.

The Kolmogorov distance is a pivot for this purpose. By Theorem 2.6.2,

$$
1 - \alpha \approx \mathbb{P}\Bigl(\sqrt n\sup_x\lvert F_n(x) - F(x)\rvert \le K^{-1}(1 - \alpha)\Bigr) = \mathbb{P}\Bigl(F_n(x) - \frac{K^{-1}(1-\alpha)}{\sqrt n} \le F(x) \le F_n(x) + \frac{K^{-1}(1-\alpha)}{\sqrt n}\ \forall x\Bigr).
$$
Equivalently, and without any asymptotics, set the right side of the DKW inequality equal to $\alpha$:

$$
2\mathrm{e}^{-2n\varepsilon^2} = \alpha\quad\Longrightarrow\quad \varepsilon = \sqrt{\frac{1}{2n}\log\frac2\alpha}.
$$
Then

$$
L(x) = \max\{F_n(x) - \varepsilon, 0\},\qquad U(x) = \min\{F_n(x) + \varepsilon, 1\}
$$
define a $1 - \alpha$ confidence band for any $F$ and any $n$. For $\alpha = 0.05$, $\varepsilon = \sqrt{\log 40/(2n)} = 1.358/\sqrt n$, numerically the same as the asymptotic Kolmogorov band: the DKW inequality is essentially sharp at conventional levels.

```r
Fn <- ecdf(x); x <- sort(x); n <- length(x)
l1 <- u1 <- l2 <- u2 <- numeric(n)
epsilon <- sqrt((1 / (2 * n)) * log(2 / 0.05))
for (i in 1:n) {
  ci <- binom.test(sum(x <= x[i]), n)$conf.int   # pointwise Clopper-Pearson
  l1[i] <- ci[1]; u1[i] <- ci[2]
  l2[i] <- max(Fn(x[i]) - epsilon, 0)             # DKW band
  u2[i] <- min(Fn(x[i]) + epsilon, 1)
}
plot(Fn, verticals = TRUE, do.points = FALSE, main = "Confidence interval & band")
polygon(c(x, rev(x)), c(l2, rev(u2)), col = "gray85", border = FALSE)
polygon(c(x, rev(x)), c(l1, rev(u1)), col = "gray70", border = FALSE)
plot(Fn, verticals = TRUE, do.points = FALSE, add = TRUE)
```

![The EDF of a standard normal sample of size 50 with 95% pointwise Clopper-Pearson intervals (dark) and the 95% DKW confidence band (light), and the true distribution function, which lies inside the band.](./plots/edf-bands.py)

## 2.8. The Empirical Quantile Function and Q–Q Plots

### 2.8.1. The Empirical Quantile Function

For a continuous, strictly increasing $F$ the inverse function $F^{-1}$ is unique, and $F^{-1}(p) \le x \iff p \le F(x)$. A step function such as $F_n$ has no inverse, and we use the generalized inverse of [3.1.7](/3.1.7), the quantile function $F^{-1}(p) = \inf\{x\colon F(x) \ge p\}$.

**Definition 2.8.1 (Empirical Quantile Function)** The **empirical quantile function** of a sample is

$$
F_n^{-1}(p) = \inf\{y\colon F_n(y) \ge p\} = X_{(\lceil np\rceil)},\qquad 0 < p \le 1.
$$

The second expression holds because $F_n(X_{(i)}) = i/n$: the smallest order statistic at which $F_n$ reaches $p$ is the one with $i \ge np$. Like every quantile function, $F_n^{-1}$ is nondecreasing and left-continuous: $F^{-1}(p) \le x$ if and only if $p \le F(x)$, so $\{p\colon F^{-1}(p) \le x\} = (0, F(x)]$ is closed on the right, and this is equivalent to left continuity of $F^{-1}$. It is a step function with jumps at $p = i/n$.

**Example 2.8.1** For the sample $-1.55, -0.67, -0.39, 0.60$ ($n = 4$), $F_n^{-1}(0.25) = X_{(1)} = -1.55$ and $F_n^{-1}(0.4) = X_{(\lceil1.6\rceil)} = X_{(2)} = -0.67$. R's `quantile(x, p, type = 1)` computes this inverse; the default `type = 7` interpolates linearly between order statistics, so the reported sample quantiles depend on the convention used.

### 2.8.2. Q–Q Plots

The quantile–quantile plot compares two distributions through their quantile functions: it plots the points $\bigl(F^{-1}(p), F_n^{-1}(p)\bigr)$ for $p$ between $0$ and $1$, in practice the points

$$
\Bigl(F^{-1}(p_i),\ x_{(i)}\Bigr),\qquad p_i = \frac{i - 1/2}{n},\quad i = 1, \dots, n.
$$
The plotting positions $p_i = (i - 1/2)/n$ are used instead of $i/n$ because $F^{-1}(1)$ is infinite for distributions with unbounded support. A common choice of $F$ is the standard normal distribution, giving the **normal Q–Q plot** of [3.2.6](/3.2.6), but any specified distribution can be used. If the sample comes from the location–scale family of $F$, that is, from $F\bigl((x - \mu)/\sigma\bigr)$, the points lie near a straight line with intercept $\mu$ and slope $\sigma$; this is why the plot does not need the parameters to be known. Systematic departures have typical shapes on a normal Q–Q plot:

| Population | Shape of the normal Q–Q plot |
|---|---|
| Normal | straight line |
| Right-skewed (exponential) | convex curve: the upper quantiles are too large, the lower ones too close together |
| Heavy tails (Cauchy) | S-shape that steepens at both ends |
| Light tails (uniform) | inverted S-shape, flattening at both ends |

### 2.8.3. Q–Q Plots with Confidence Bands

When the points seem to deviate from a straight line, care is needed, because of sampling variability: even samples from the hypothesized distribution wander away from the line, especially in the tails. It is useful to indicate the likely range of sampling variability on the plot itself, and a simultaneous band for $F$ transforms directly into one for the Q–Q plot. A normal distribution $\mathcal{N}(\mu, \sigma^2)$ lies within the band $F_n \pm k$ if and only if

$$
F_n(x) - k \le \Phi\Bigl(\frac{x - \mu}{\sigma}\Bigr) \le F_n(x) + k\quad\text{for all } x,
$$
which is equivalent to

$$
\Phi^{-1}\bigl(F_n(x) - k\bigr) \le \frac{x - \mu}{\sigma} \le \Phi^{-1}\bigl(F_n(x) + k\bigr)\quad\text{for all } x,
$$
that is, to the straight line $z = (x - \mu)/\sigma$ lying between the two transformed bounds. With $k$ from the DKW inequality (or the Kolmogorov quantile), the band holds with probability at least $1 - \alpha$ simultaneously, and the data are consistent with normality at level $\alpha$ if some straight line fits inside it. At height $x_{(i)}$ the line must pass between $\Phi^{-1}(i/n - k)$ and $\Phi^{-1}\bigl((i-1)/n + k\bigr)$, the values of the bounds just at and just before the jump of $F_n$.

![Normal Q-Q plots with 95% simultaneous bands derived from the DKW band, for a normal sample (left) and an exponential sample (right) of size 50. A normal distribution is consistent with the data at level 0.05 if some straight line passes through every horizontal band segment. The curvature of the exponential sample is visible, but with n = 50 the band is wide.](./plots/qq-bands.py)

Two cautions. First, the band is for a fully specified $F$; if $\mu$ and $\sigma$ are estimated from the data, a fitted line passes closer to the points than the true one, and the band is conservative for judging "normality with some parameters", a problem taken up with the Lilliefors test in [3.6.6](/3.6.6). Second, a band of this kind is wide in the tails of the plot, where the normal quantiles change rapidly, so the Q–Q plot remains above all a visual diagnostic: a formal test quantifies the overall fit, while the plot shows where and how the fit fails.

## Summary

| Object | Definition | Key distributional fact |
|---|---|---|
| Order statistics $X_{(i)}$ (Definition 2.1.1) | sorted sample | $F(X_{(i)}) \sim \mathrm{Beta}(i, n - i + 1)$ for every continuous $F$ (Corollary 2.1.1) |
| Ranks $R_i$ (Definition 2.2.1) | $X_i = X_{(R_i)}$ | $\boldsymbol{R}$ uniform on the $n!$ permutations (Theorem 2.2.1); $\mathbb{E}R_i = \frac{n+1}{2}$, $\operatorname{Var}R_i = \frac{n^2-1}{12}$, $\operatorname{Cov} = -\frac{n+1}{12}$ |
| Rank statistic (Definition 2.3.2) | function of $\boldsymbol{R}$ only | distribution-free over i.i.d. continuous populations (Theorem 2.3.1); invariant under increasing transformations |
| U-statistic (Definition 2.4.1) | average of a symmetric kernel over all $k$-subsets | unbiased; minimum variance among unbiased estimators in the nonparametric family; asymptotically normal |
| EDF $F_n$ (Definition 2.5.1) | proportion of observations $\le x$ | $nF_n(x) \sim \mathrm{Bin}(n, F(x))$; uniform convergence (Glivenko–Cantelli); nonparametric MLE |
| Kolmogorov distance $D_n$ (Definition 2.6.1) | $\sup_x\lvert F_n - F\rvert$, computed at the jumps | distribution-free for continuous $F$ (Theorem 2.6.1); $\sqrt nD_n \to K$ (Theorem 2.6.2); DKW: $\mathbb{P}(D_n > \varepsilon) \le 2\mathrm{e}^{-2n\varepsilon^2}$ (Theorem 2.6.3) |
| Empirical quantile function (Definition 2.8.1) | $F_n^{-1}(p) = X_{(\lceil np\rceil)}$ | left-continuous step function; basis of the Q–Q plot |

- Pointwise interval for $F(x)$: Clopper–Pearson applied to $nF_n(x)$. Simultaneous band (Definition 2.7.1): $F_n \pm \varepsilon$ with $\varepsilon = \sqrt{\log(2/\alpha)/(2n)}$, which equals $1.358/\sqrt n$ at $\alpha = 0.05$. Joining pointwise intervals does not give a band; the band is wider.
- Q–Q plot: $(F^{-1}(p_i), x_{(i)})$ with $p_i = (i - \frac12)/n$; a straight line for the location–scale family of $F$; the DKW band transforms into a band for the plot.

## Questions

1. For an i.i.d. continuous sample with ranks $R_1, \dots, R_n$, show that $\mathbb{P}(R_i = r, R_j = s) = \frac{1}{n(n-1)}$ for $i \ne j$, $r \ne s$, and deduce $\operatorname{Cov}(R_i, R_j)$ directly from this joint distribution.

   **Answer** By Theorem 2.2.1 all $n!$ rank vectors are equally likely, and $(n-2)!$ of them have $r$ in position $i$ and $s$ in position $j$, so the probability is $(n-2)!/n! = \frac{1}{n(n-1)}$. Then
   $$
   \mathbb{E}R_iR_j = \frac{1}{n(n-1)}\sum_{r\ne s}rs = \frac{1}{n(n-1)}\Bigl[\Bigl(\sum_rr\Bigr)^2 - \sum_rr^2\Bigr] = \frac{1}{n(n-1)}\Bigl[\frac{n^2(n+1)^2}{4} - \frac{n(n+1)(2n+1)}{6}\Bigr] = \frac{(n+1)(3n+2)}{12},
   $$
   and $\operatorname{Cov}(R_i, R_j) = \frac{(n+1)(3n+2)}{12} - \frac{(n+1)^2}{4} = \frac{(n+1)(3n + 2 - 3n - 3)}{12} = -\frac{n+1}{12}$, in agreement with Corollary 2.2.1.
2. Is the quantile function $F^{-1}(p) = \inf\{x\colon F(x) \ge p\}$ left- or right-continuous? Why?

   **Answer** Left-continuous. Because $F$ is right-continuous, the infimum is attained, so $F^{-1}(p) \le x \iff p \le F(x)$. Let $p_k \uparrow p$. The values $F^{-1}(p_k)$ increase to some limit $x^* \le F^{-1}(p)$; for each $k$, $F^{-1}(p_k) \le x^*$, so $p_k \le F(x^*)$, and letting $k \to \infty$ gives $p \le F(x^*)$, that is, $F^{-1}(p) \le x^*$. Hence $F^{-1}(p_k) \to F^{-1}(p)$. It need not be right-continuous: where $F$ is flat at height $p$ on an interval $[a, b)$, $F^{-1}(p) = a$ but $F^{-1}(p + \delta) \ge b$ for every $\delta > 0$.
3. Generate $100$ observations, compute the $95\%$ DKW confidence band, and repeat $1000$ times, recording how often the band contains the true distribution function, once for $F = \mathcal{N}(0, 1)$ and once for the standard Cauchy distribution. What do you expect?

   **Answer** In both cases the proportion should be at least about $95\%$ (in fact close to $95\%$, slightly above, since $\varepsilon = 1.358/\sqrt{100}$ is almost exactly the Kolmogorov quantile and the finite-sample distribution of $\sqrt nD_n$ is slightly stochastically smaller than its limit). The heavy tails of the Cauchy distribution make no difference: the event $\{\sup_x\lvert F_n - F\rvert \le \varepsilon\}$ has the same probability for every continuous $F$ by Theorem 2.6.1, and the DKW inequality holds for every $F$. A simulation with $4000$ replications gave coverages of $0.955$ (normal) and $0.954$ (Cauchy).
4. Twenty-four observations come either from $\mathrm{U}(0, 10)$ or from the symmetric triangular distribution on $(0, 10)$: $4.17, 8.42, 3.02, 2.89, 9.77, 6.06, 2.72, 5.12, 6.00, 4.78, 2.62, 7.20, 1.61, 5.92, 7.25, 8.01, 4.76, 5.36, 5.34, 7.59, 0.66, 7.27, 3.39, 1.40$. Compare the two candidates with the Kolmogorov distance and the $95\%$ DKW band. Which is more plausible?

   **Answer** The Kolmogorov distances are $D = 0.137$ to $\mathrm{U}(0, 10)$ (largest gap at $x = 2.62$) and $D = 0.135$ to the triangular distribution (at $x = 7.20$), and the $95\%$ DKW half-width is $\varepsilon = \sqrt{\log 40/48} = 0.277$. Both distribution functions lie comfortably inside the band, and both Kolmogorov–Smirnov $p$-values are about $0.7$. The data cannot distinguish the two candidates: with $n = 24$ the band is too wide. Q–Q plots against each candidate would look roughly straight in both cases (the triangular plot slightly better in the middle, the uniform one in the tails), confirming that more data would be needed for a decision.
5. A U-statistic is to be used for $\theta = \mathbb{E}\lvert X_1 - X_2\rvert$, the mean absolute difference between dissolved oxygen levels on two independent days. Why is it unbiased, and why can no kernel of degree one do the job?

   **Answer** With the symmetric kernel $h(x_1, x_2) = \lvert x_1 - x_2\rvert$, every term $h(X_i, X_j)$ with $i < j$ involves two independent observations from the population, so its expectation is $\theta$, and the average of terms with expectation $\theta$ has expectation $\theta$ (Example 2.4.1 (4) gives $U_4 = 0.4$ for the four measurements). A kernel of degree one would require a function $g$ with $\mathbb{E}g(X) = \mathbb{E}\lvert X_1 - X_2\rvert$ for every distribution in the family, which is impossible because $\theta$ is a nonlinear functional of the distribution (for instance it is not a mixture-linear function: $\theta$ for a mixture of two distributions is not the corresponding mixture of their $\theta$'s). The degree of a feature is the smallest $k$ for which an unbiased kernel exists, here $k = 2$.
