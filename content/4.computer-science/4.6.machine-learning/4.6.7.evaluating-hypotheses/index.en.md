---
title: Evaluating Hypotheses and Comparing Learning Algorithms
description: Sample error and true error; confidence intervals for the error rate from the binomial distribution and its normal approximation; comparing the error rates of two hypotheses; comparing learning algorithms with k-fold cross-validation and the paired t-test, the 5×2 cross-validation test and McNemar's test.
source_hash: 5b493ea98ffe
---

After learning a hypothesis, we want to know how it performs on data it has not seen; when comparing two models or two algorithms, we want to know whether the observed difference is real or due to chance. Data are always finite, and the accuracy on a test set is itself a random variable, so these are statistical questions. This chapter answers three questions about evaluating hypotheses:

1. How well does the accuracy of a hypothesis on a finite sample represent its accuracy over the whole instance space?
2. If hypothesis $h_1$ outperforms $h_2$ on one sample, how likely is it that $h_1$ is better in general?
3. When data are limited, how can they best be used both for learning and for evaluation, and for comparing two learning algorithms?

All the statistical tools used have been covered in the statistics courses: the **binomial distribution** and the **central limit theorem** ([3.1.4](/3.1.4), [3.1.13](/3.1.13)), **confidence intervals** ([3.2.4](/3.2.4)), and **hypothesis testing** and the **t-test** ([3.2.5](/3.2.5)). This chapter applies them to the evaluation of machine learning, and adds the problems specific to machine learning: the dependence between training and test sets, the correlation among the folds of cross-validation, and the tests designed for them. For evaluation metrics and the basic principles of experimental design see [4.6.2](/4.6.2).

## 7.1. Sample Error and True Error

Let the instances in the instance space $X$ occur according to some fixed but unknown distribution $\mathcal{D}$, let the target concept $c\colon X \to \{0, 1\}$ give the true label of each instance, and let the learning algorithm choose a hypothesis $h$ from the **hypothesis space** $H$. We would like $h(x) = c(x)$ to hold for all $x \in X$, but $X$ is usually enormous: if an instance is described by $n$ binary attributes, $X$ has $2^n$ elements, and there are $2^{2^n}$ concepts on $X$ (each concept is a subset of $X$). We can check $h$ only on the set $S \subseteq X$ of examples we can obtain, whereas what we really care about is its performance on the whole of $X$.

**Definition 7.1.1 (Sample Error and True Error)** The **true error** of a hypothesis $h$ with respect to the target concept $c$ and the distribution $\mathcal{D}$ is the probability that $h$ misclassifies an instance drawn at random according to $\mathcal{D}$,

$$
\operatorname{error}_{\mathcal{D}}(h) = \mathbb{P}_{x \sim \mathcal{D}}\big(c(x) \ne h(x)\big).
$$
The **sample error** of $h$ on a sample $S$ of $n$ examples is the fraction of examples in $S$ misclassified by $h$,

$$
\operatorname{error}_S(h) = \frac1n\sum_{x \in S}\boldsymbol{1}\{c(x) \ne h(x)\}.
$$

The true error is the quantity we want to know but cannot observe directly, and the sample error is the quantity we can compute directly. The question throughout this chapter is how good $\operatorname{error}_S(h)$ is as an estimate of $\operatorname{error}_{\mathcal{D}}(h)$.

## 7.2. Estimating the Error Rate of a Hypothesis

### 7.2.1. The Distribution of the Error Estimate

Suppose the $n$ examples in $S$ are drawn independently according to $\mathcal{D}$ and independently of $h$ (they took no part in the training and selection of $h$). Whether each example is misclassified is a Bernoulli trial with success (misclassification) probability $p = \operatorname{error}_{\mathcal{D}}(h)$. The number of misclassifications $r$ follows the **binomial distribution** $\mathrm{Bin}(n, p)$:

$$
\mathbb{P}(r = k) = \binom nk p^k(1 - p)^{n-k},\qquad \mathbb{E}[r] = np,\qquad \operatorname{Var}(r) = np(1 - p).
$$
Hence $\operatorname{error}_S(h) = r/n$ satisfies

$$
\mathbb{E}\big[\operatorname{error}_S(h)\big] = \operatorname{error}_{\mathcal{D}}(h),\qquad
\sigma_{\operatorname{error}_S(h)} = \sqrt{\frac{\operatorname{error}_{\mathcal{D}}(h)\big(1 - \operatorname{error}_{\mathcal{D}}(h)\big)}{n}} \approx \sqrt{\frac{\operatorname{error}_S(h)\big(1 - \operatorname{error}_S(h)\big)}{n}} .
$$

**Example 7.2.1** Suppose $h$ errs on $r = 12$ of $n = 100$ test examples, so $\operatorname{error}_S(h) = 0.12$ and the standard deviation is about $\sqrt{0.12 \times 0.88/100} \approx 0.032$; if it errs on only 3 of $n = 25$ examples, the sample error is again $0.12$ but the standard deviation is about $0.065$. The same point estimate is far more credible in the former case.

### 7.2.2. Bias and Variance of the Estimate

The bias of the estimator $\operatorname{error}_S(h)$ is $\mathbb{E}[\operatorname{error}_S(h)] - \operatorname{error}_{\mathcal{D}}(h)$. The unbiasedness above requires $h$ to be independent of $S$. If $S$ is the **training set**, then $h$ was chosen precisely to perform well on $S$, and $\operatorname{error}_S(h)$ is biased, and optimistically so; the more complex the model and the stronger its **overfitting**, the larger the bias. This gives two basic rules of evaluation: do not report results on the training set as test results; and do not tune parameters or select models on the **test set** (otherwise the test set becomes part of training).

Even if the estimate is unbiased, a single $\operatorname{error}_S(h)$ can still differ considerably from $\operatorname{error}_{\mathcal{D}}(h)$ (the standard deviations are 3.2% and 6.5% in Example 7.2.1). Among unbiased estimates we should choose the one of smallest variance; for the error rate, this means using as many independent test examples as possible.

### 7.2.3. Confidence Intervals for the Error Rate

An $N\%$ **confidence interval** for $p$ is a random interval that contains $p$ with probability $N\%$, and $N\%$ is called the **confidence level**. It describes the uncertainty of the estimate: the interval is centered at the point estimate, and its width depends on the variance of the estimate. Computing an interval directly from the binomial distribution is cumbersome, whereas intervals for the normal distribution are easy: if $Y \sim \mathcal{N}(\mu, \sigma^2)$, then $Y$ falls in $\mu \pm z_N\sigma$ with probability $N\%$, where $z_N$ is the two-sided quantile of the standard normal distribution:

| Confidence level $N\%$ | 50% | 68% | 80% | 90% | 95% | 98% | 99% |
|---|---|---|---|---|---|---|---|
| $z_N$ | 0.67 | 1.00 | 1.28 | 1.64 | 1.96 | 2.33 | 2.58 |

By the **de Moivre–Laplace theorem**, for large $n$ the distribution $\mathrm{Bin}(n, p)$ is well approximated by the **normal distribution** (rule of thumb: $n \ge 30$ and $np(1-p) \ge 5$). Hence:

**Proposition 7.2.1** Let the test sample $S$ consist of $n$ examples drawn independently and independently of $h$, let $h$ err on $r$ of them, and let $n$ be sufficiently large. Then an approximate $N\%$ confidence interval for $\operatorname{error}_{\mathcal{D}}(h)$ is

$$
\operatorname{error}_S(h) \pm z_N\sqrt{\frac{\operatorname{error}_S(h)\big(1 - \operatorname{error}_S(h)\big)}{n}} .
$$

In Example 7.2.1, for $n = 100$ the 95% confidence interval is $0.12 \pm 1.96 \times 0.032 = [0.056, 0.184]$. This is the Wald interval for a Bernoulli proportion of [3.2.4](/3.2.4), where it is also explained that its coverage is insufficient for small $n$ or for $p$ near 0 or 1, and that it can even extend below $0$; in these cases we should use the Wilson score interval instead:

```python
from math import sqrt
from statistics import NormalDist

z = NormalDist().inv_cdf


def wald(r, n, level=0.95):
    """Normal-approximation interval error_S +- z * sqrt(error_S (1 - error_S) / n)."""
    e = r / n
    h = z(0.5 + level / 2) * sqrt(e * (1 - e) / n)
    return e - h, e + h


def wilson(r, n, level=0.95):
    """Wilson score interval; better for small n or error rates near 0 or 1."""
    e, zz = r / n, z(0.5 + level / 2)
    center = (e + zz**2 / (2 * n)) / (1 + zz**2 / n)
    half = zz * sqrt(e * (1 - e) / n + zz**2 / (4 * n**2)) / (1 + zz**2 / n)
    return center - half, center + half


for r, n in [(12, 100), (3, 25), (1, 40)]:
    lo, hi = wald(r, n)
    wlo, whi = wilson(r, n)
    print(f"r={r:2d} n={n:3d}  error_S={r / n:.3f}  Wald [{lo:.3f}, {hi:.3f}]  Wilson [{wlo:.3f}, {whi:.3f}]")
```

```text
r=12 n=100  error_S=0.120  Wald [0.056, 0.184]  Wilson [0.070, 0.198]
r= 3 n= 25  error_S=0.120  Wald [-0.007, 0.247]  Wilson [0.042, 0.300]
r= 1 n= 40  error_S=0.025  Wald [-0.023, 0.073]  Wilson [0.004, 0.129]
```

The meaning of a confidence interval is that if we repeatedly draw test sets and construct intervals by the same method, about $N\%$ of the intervals contain the true error rate. The figure below simulates this; the half-width of the interval is inversely proportional to $\sqrt n$, so the test set must be enlarged fourfold to halve the interval.

![Left: for a true error rate of 0.2, the 95% Wald intervals given by 100 test sets of size 50; the 8 in red do not cover the true error rate (nominally about 5 would be expected; for small n the coverage of the normal approximation is slightly low). Right: the half-width of the 95% interval as a function of the test set size n, with the dashed line at 0.05](./plots/error-rate-intervals.py)

**Example 7.2.2** The true error rate of a hypothesis is known to lie between $0.2$ and $0.6$. How many test examples are needed at least to make the width of a 95% two-sided confidence interval less than $0.1$? The half-width satisfies $1.96\sqrt{p(1-p)/n} \le 0.05$, and the maximum of $p(1-p)$ over $[0.2, 0.6]$ is attained at $p = 0.5$ and equals $0.25$, so $n \ge (1.96/0.05)^2 \times 0.25 \approx 384.2$, and at least 385 examples are needed.

### 7.2.4. One-Sided Confidence Intervals

Sometimes we care only about how large the error rate can be, that is, an upper bound. By the symmetry of the normal distribution, if $[L, U]$ is a two-sided interval at confidence level $100(1 - \alpha)\%$, then $(-\infty, U]$ is a one-sided interval at confidence level $100(1 - \alpha/2)\%$: the upper end $\mu + 1.96\sigma$ of the two-sided 95% interval is a one-sided upper bound at 97.5%; a one-sided upper bound at 95% is $\mu + 1.645\sigma$, which corresponds to the upper end of the two-sided 90% interval.

### 7.2.5. A General Method for Deriving Confidence Intervals

The derivation above can be summarized as a general procedure that applies to many other problems:

1. Identify the parameter $p$ to be estimated, such as $\operatorname{error}_{\mathcal{D}}(h)$;
2. Choose an estimator $Y$, such as $\operatorname{error}_S(h)$, preferably an unbiased one with as small a variance as possible;
3. Determine the distribution of $Y$, including its mean and variance;
4. From the distribution, find the $N\%$ confidence interval $[L, U]$ (possibly with $L = -\infty$ or $U = \infty$), for example by looking up $z_N$ for the normal distribution.

The central limit theorem greatly simplifies step 3: if $Y_1, \dots, Y_n$ are independent and identically distributed with mean $\mu$ and finite variance $\sigma^2$, then whatever the distribution of $Y_i$, the sample mean $\bar Y$ is approximately $\mathcal{N}(\mu, \sigma^2/n)$, and after standardization it is approximately standard normal. Most evaluation metrics in machine learning (error rate, average loss) are averages of some kind, so approximate confidence intervals can be constructed for them in this way; metrics that are not averages (such as AUC and F1) can have their intervals constructed with the **bootstrap** ([3.5.7](/3.5.7)).

## 7.3. Comparing Two Hypotheses

### 7.3.1. The Difference of Error Rates

Suppose $h_1$ is tested on a sample $S_1$ of $n_1$ independent examples and $h_2$ on an independent sample $S_2$ of $n_2$ examples. The parameter to be estimated is the difference of the true error rates

$$
d = \operatorname{error}_{\mathcal{D}}(h_1) - \operatorname{error}_{\mathcal{D}}(h_2),
$$
and an unbiased estimator is $\hat d = \operatorname{error}_{S_1}(h_1) - \operatorname{error}_{S_2}(h_2)$. Both sample error rates are approximately normal and independent, so $\hat d$ is also approximately normal with mean $d$ and variance equal to the sum of the two variances:

$$
\sigma_{\hat d}^2 \approx \frac{\operatorname{error}_{S_1}(h_1)\big(1 - \operatorname{error}_{S_1}(h_1)\big)}{n_1} + \frac{\operatorname{error}_{S_2}(h_2)\big(1 - \operatorname{error}_{S_2}(h_2)\big)}{n_2} .
$$
An approximate $N\%$ confidence interval for $d$ is $\hat d \pm z_N\sigma_{\hat d}$.

### 7.3.2. One-Sided Tests

Now we ask: having observed $\hat d > 0$, how confident can we be that $\operatorname{error}_{\mathcal{D}}(h_1) > \operatorname{error}_{\mathcal{D}}(h_2)$ (that is, that $h_2$ is better)? This is a **one-sided test**: the confidence that $d > 0$ is the confidence level at which the one-sided interval $(0, \infty)$ just contains $d$, namely $\Phi(\hat d/\sigma_{\hat d})$, where $\Phi$ is the standard normal distribution function. In the language of **hypothesis testing**, this is the z-test of the **null hypothesis** $d \le 0$, with **p-value** $1 - \Phi(\hat d/\sigma_{\hat d})$.

**Example 7.3.1** Let $n_1 = n_2 = 100$, $\operatorname{error}_{S_1}(h_1) = 0.30$ and $\operatorname{error}_{S_2}(h_2) = 0.20$. Then $\hat d = 0.10$,

$$
\sigma_{\hat d} \approx \sqrt{\frac{0.3 \times 0.7}{100} + \frac{0.2 \times 0.8}{100}} \approx 0.061,\qquad z = \frac{0.10}{0.061} \approx 1.64 .
$$
The value $z = 1.64$ corresponds to a two-sided confidence level of 90%, that is, a one-sided confidence level of 95%: we can be 95% confident that the true error rate of $h_2$ is lower (the p-value is about 0.05).

**Example 7.3.2** With the same error rates but $n_1 = n_2 = 30$, we get $\sigma_{\hat d} \approx 0.111$, $z \approx 0.90$ and $\Phi(0.90) \approx 0.82$: the one-sided confidence is only about 82% (about 63% two-sided), far from enough to draw a conclusion. With the same gap of 10 percentage points, a test set that is too small cannot tell the hypotheses apart.

### 7.3.3. Comparison on the Same Test Set: McNemar's Test

The discussion above assumed that $S_1, S_2$ are independent. In practice two classifiers are more often compared on the same test set; the two sample error rates are then positively correlated, the variance formula above overestimates the variance of $\hat d$, and the test is conservative. It is more appropriate to look only at the examples on which the two classifiers disagree.

**Definition 7.3.1 (McNemar's Test)** On the same test set of $n$ examples, let $n_{01}$ be the number of examples that $h_1$ classifies correctly and $h_2$ incorrectly, and $n_{10}$ the number that $h_1$ classifies incorrectly and $h_2$ correctly. Under the null hypothesis that the two error rates are equal, each example on which they disagree falls into either of the two classes with probability $1/2$. **McNemar's test** uses the statistic

$$
\chi^2 = \frac{(\lvert n_{01} - n_{10}\rvert - 1)^2}{n_{01} + n_{10}},
$$
which under the null hypothesis is approximately distributed as the **chi-square distribution** with 1 degree of freedom (the $-1$ is a continuity correction); when $n_{01} + n_{10}$ is small, the exact test based on $\mathrm{Bin}(n_{01} + n_{10}, 1/2)$ is used instead.

Examples that both classifiers classify correctly or both incorrectly carry no information about the difference and therefore do not enter the statistic. Simulations by Dietterich (1998) show that when training can be done only once (for example, because training is expensive), the type I error probability of McNemar's test is close to the nominal level, which makes it a good choice for comparing two classifiers.

## 7.4. Comparing Learning Algorithms

### 7.4.1. The Problem

Beyond comparing two hypotheses, we more often want to compare two learning algorithms $L_A$ and $L_B$: which is better "in general"? The ideal quantity is the difference averaged over all training sets $S$ of size $n$ drawn according to $\mathcal{D}$,

$$
\mathbb{E}_{S \sim \mathcal{D}^n}\Big[\operatorname{error}_{\mathcal{D}}\big(L_A(S)\big) - \operatorname{error}_{\mathcal{D}}\big(L_B(S)\big)\Big],
$$
where $L(S)$ is the hypothesis output by algorithm $L$ on training set $S$. In practice we have only one fixed finite data set $D_0$. The simplest approach is to split $D_0$ into a training set $S_0$ and a test set $T_0$ and compute $\operatorname{error}_{T_0}(L_A(S_0)) - \operatorname{error}_{T_0}(L_B(S_0))$; it is better to repeat this process several times and average. Each time both algorithms are trained on the same training set and tested on the same test set, so the comparison is paired (a paired test), which cancels the differences caused by the data split.

### 7.4.2. k-Fold Cross-Validation and the Paired t-Test

**Algorithm 7.4.1 (Comparing Two Learning Algorithms by k-Fold Cross-Validation)**

1. Randomly split $D_0$ into $k$ disjoint subsets $T_1, \dots, T_k$ of equal size, each containing at least 30 examples;
2. For $i = 1, \dots, k$: take $T_i$ as the test set and the rest $S_i = D_0 \setminus T_i$ as the training set, and compute $\delta_i = \operatorname{error}_{T_i}(L_A(S_i)) - \operatorname{error}_{T_i}(L_B(S_i))$;
3. Output $\bar\delta = \frac1k\sum_i\delta_i$ together with an approximate $N\%$ confidence interval $\bar\delta \pm t_{k-1}\,s_{\bar\delta}$ for it, where

   $$
   s_{\bar\delta} = \sqrt{\frac{1}{k(k-1)}\sum_{i=1}^k(\delta_i - \bar\delta)^2},
   $$
   and $t_{k-1}$ is the corresponding two-sided quantile of the **t-distribution** with $k - 1$ degrees of freedom.

We use the t-distribution rather than the normal distribution here because there are only $k$ (usually 10) differences, and the uncertainty of the sample variance itself cannot be ignored. This is exactly the paired t-test:

**Definition 7.4.1 (Paired t-Test)** Let the results of two models on $n$ paired experiments (with the same training and test sets) be $x_{1i}, x_{2i}$, and let the differences $d_i = x_{1i} - x_{2i}$ be independent and normally distributed. The **paired t-test** uses

$$
t = \frac{\bar x_1 - \bar x_2}{\sqrt{\sum_{i=1}^n(d_i - \bar d)^2/\big(n(n-1)\big)}}
$$
as the test statistic; under the null hypothesis of no difference, $t$ follows the t-distribution with $n - 1$ degrees of freedom.

It is the one-sample t-test applied to the differences (the paired-data case in [3.2.5](/3.2.5)). If the two sets of experiments are not paired (for example, each repeated independently $n_1$ and $n_2$ times), the sample sizes and variances may differ, and we use **Welch's t-test**:

$$
t = \frac{\bar x_1 - \bar x_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}},\qquad
\mathrm{df} = \frac{\big(s_1^2/n_1 + s_2^2/n_2\big)^2}{\dfrac{(s_1^2/n_1)^2}{n_1 - 1} + \dfrac{(s_2^2/n_2)^2}{n_2 - 1}},
$$
where $s_j^2 = \frac{1}{n_j - 1}\sum_i(x_{ji} - \bar x_j)^2$ is the sample variance. When the experiments are paired, the differences cancel the variation among the splits and the test has much higher power, so we should pair whenever we can.

The paired t-test with k-fold cross-validation has a flaw: the test sets of the folds are disjoint, but the training sets overlap heavily (the training sets of any two folds share a fraction $(k-2)/(k-1)$ of the data), so the $\delta_i$ are not independent but positively correlated. Consequently $s_{\bar\delta}$ underestimates the true variability, the test is too optimistic, and the probability of a type I error is higher than the nominal level (Dietterich, 1998). Nadeau and Bengio (2003) proposed a correction: replace the variance estimate $\frac1k s_\delta^2$ by $\big(\frac1k + \frac{n_{\mathrm{test}}}{n_{\mathrm{train}}}\big)s_\delta^2$, where $s_\delta^2$ is the sample variance of the $\delta_i$ and $n_{\mathrm{test}}/n_{\mathrm{train}} = 1/(k-1)$ for k-fold cross-validation. Even so, a comparison by k-fold cross-validation is still better than no comparison at all.

Another approach is to draw a random test set (of at least 30 examples) each time, use the rest as the training set, and repeat many times; but when the data set is not large enough these test sets also overlap and are not independent, and the problem is more serious.

### 7.4.3. The 5×2 Cross-Validation t-Test

Dietterich (1998) compared the type I error probabilities of many tests and proposed the 5×2 cross-validation (5×2cv) paired t-test:

**Algorithm 7.4.2 (5×2 Cross-Validation t-Test)** Repeat 5 times ($i = 1, \dots, 5$): split the data at random into halves $S_1, S_2$, train on $S_1$ and test on $S_2$, then swap, obtaining two differences of error rates $p_i^{(1)}, p_i^{(2)}$; let $\bar p_i = (p_i^{(1)} + p_i^{(2)})/2$ and $s_i^2 = (p_i^{(1)} - \bar p_i)^2 + (p_i^{(2)} - \bar p_i)^2$. The statistic

$$
\tilde t = \frac{p_1^{(1)}}{\sqrt{\frac15\sum_{i=1}^5 s_i^2}}
$$
is approximately distributed as the t-distribution with 5 degrees of freedom under the null hypothesis that the two algorithms do not differ.

The two training sets of a two-fold cross-validation do not overlap, so the two differences within each repetition are approximately independent; the repetition 5 times serves to estimate the variance more stably. In Dietterich's simulations, the type I error probabilities of both the 5×2cv t-test and McNemar's test were close to the nominal level, whereas those of the t-test with repeated random splits and the t-test with 10-fold cross-validation were too high. The numerator uses only $p_1^{(1)}$, so the result depends on the first split; Alpaydin (1999) used all 10 differences to construct a combined F statistic

$$
F = \frac{\sum_{i=1}^5\sum_{j=1}^2\big(p_i^{(j)}\big)^2}{2\sum_{i=1}^5 s_i^2},
$$
which under the null hypothesis is approximately distributed as $F_{10,5}$, and is more stable and more powerful.

### 7.4.4. An Example

Below we compare logistic regression with a random forest ([4.6.6](/4.6.6)) on the same data set, performing in turn the 10-fold cross-validated paired t-test, the Nadeau–Bengio correction, the 5×2cv t-test and McNemar's test:

```python
import numpy as np
from scipy import stats
from sklearn.base import clone
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, StratifiedKFold, train_test_split

X, y = make_classification(n_samples=1000, n_features=20, n_informative=6,
                           flip_y=0.05, random_state=1)
A = LogisticRegression(max_iter=1000)
B = RandomForestClassifier(n_estimators=200, random_state=0)


def error(model, Xtr, ytr, Xte, yte):
    return np.mean(clone(model).fit(Xtr, ytr).predict(Xte) != yte)


# 1. k-fold cross-validated paired t-test (same folds for both algorithms)
k = 10
delta = np.array([error(A, X[tr], y[tr], X[te], y[te]) - error(B, X[tr], y[tr], X[te], y[te])
                  for tr, te in StratifiedKFold(k, shuffle=True, random_state=0).split(X, y)])
t = delta.mean() / (delta.std(ddof=1) / np.sqrt(k))
print(f"mean difference {delta.mean():.4f}; paired t = {t:.2f}, p = {2 * stats.t.sf(abs(t), k - 1):.4f}")
# Nadeau-Bengio correction for the overlap of training sets
t_c = delta.mean() / np.sqrt((1 / k + 1 / (k - 1)) * delta.var(ddof=1))
print(f"corrected t = {t_c:.2f}, p = {2 * stats.t.sf(abs(t_c), k - 1):.4f}")

# 2. Dietterich's 5x2cv paired t-test
p1, s2 = None, []
for i in range(5):
    folds = list(KFold(2, shuffle=True, random_state=i).split(X))
    p = [error(A, X[a], y[a], X[b], y[b]) - error(B, X[a], y[a], X[b], y[b]) for a, b in folds]
    p1 = p[0] if p1 is None else p1
    s2.append((p[0] - np.mean(p)) ** 2 + (p[1] - np.mean(p)) ** 2)
t52 = p1 / np.sqrt(np.mean(s2))
print(f"5x2cv t = {t52:.2f}, p = {2 * stats.t.sf(abs(t52), 5):.4f}")

# 3. McNemar's test on a single test set
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
ra = clone(A).fit(Xtr, ytr).predict(Xte) == yte
rb = clone(B).fit(Xtr, ytr).predict(Xte) == yte
n01, n10 = int(np.sum(ra & ~rb)), int(np.sum(~ra & rb))
chi2 = (abs(n01 - n10) - 1) ** 2 / (n01 + n10)
print(f"McNemar: n01={n01}, n10={n10}, chi2 = {chi2:.2f}, p = {stats.chi2.sf(chi2, 1):.4f}")
```

```text
mean difference 0.0260; paired t = 2.57, p = 0.0304
corrected t = 1.77, p = 0.1112
5x2cv t = 1.08, p = 0.3312
McNemar: n01=9, n10=13, chi2 = 0.41, p = 0.5224
```

The random forest errs 2.6 percentage points less on average in 10-fold cross-validation. The uncorrected paired t-test finds the difference significant at the $0.05$ level, whereas the corrected test, the 5×2cv test and McNemar's test all find it insignificant: the uncorrected test ignores the overlap among training sets and exaggerates the evidence. Before reporting that "algorithm A outperforms algorithm B", we should use a test whose type I error is controlled, and report the size of the difference together with a confidence interval.

### 7.4.5. Small and Large Samples, Multiple Data Sets

The choice between the z-test and the t-test depends on the number of samples of the random variable:

| | z-test (normal approximation) | t-test |
|---|---|---|
| Random variable | Whether each test example is classified correctly | The metric of each experiment (each fold, each repetition) |
| Number of samples | Many (the number of test examples, at least 30) | Few (such as 10 folds, 5×2) |
| Typical use | A single evaluation: confidence interval on one test set, comparing two hypotheses | Multiple evaluations: repeated experiments, cross-validation |
| Basis | Central limit theorem | Differences approximately normal, variance to be estimated |

When algorithms are compared over multiple data sets, the error rates on different data sets are not comparable and do not follow a common normal distribution. Demšar (2006) recommends the **Wilcoxon signed-rank test** (ranking the differences over data sets) for comparing two algorithms, and the Friedman test (ranking the algorithms' performance on each data set) for comparing several algorithms, followed, if significant, by post hoc pairwise comparisons (such as the Nemenyi test). When many pairs of algorithms are compared simultaneously, the problem of multiple comparisons must also be kept in mind.

## Summary

| Question | Method | Key points |
|---|---|---|
| 1. Does the accuracy of a hypothesis represent its performance on unseen instances? | Binomial distribution → normal approximation → confidence interval | $\operatorname{error}_S(h) \pm z_N\sqrt{\operatorname{error}_S(h)(1-\operatorname{error}_S(h))/n}$; the test set must be independent of $h$; use the Wilson interval for small samples |
| 2. How likely is $h_1$ to be better than $h_2$ in general? | Normal approximation for the difference of error rates, one-sided confidence | Independent test sets: $\hat d \pm z_N\sigma_{\hat d}$; same test set: McNemar's test |
| 3. How to compare learning algorithms with limited data? | k-fold cross-validation + paired t-test, confidence interval from the t-distribution | Overlapping training sets make the test optimistic: use the corrected t-test, the 5×2cv t-test or the F-test; use rank tests across multiple data sets |

The basic principles of evaluating a learning system are: keep the test data independent of training and model selection; repeat the experiments; compare in pairs; judge differences with statistical significance tests; and report confidence intervals.
