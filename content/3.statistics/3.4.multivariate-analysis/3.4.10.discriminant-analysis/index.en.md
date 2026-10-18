---
title: Discriminant Analysis
description: Fisher's linear discriminant, minimum expected cost classification, LDA and QDA for normal populations, Fisher's discriminants for several groups, and how to evaluate a classification rule.
---

The previous chapters described the structure of one set of variables ([principal components](/3.4.5), [factor analysis](/3.4.8)) or the relation between two sets ([canonical correlation](/3.4.9)). This chapter turns to a supervised problem: the observations come with known group labels, and we want a rule that assigns a new observation to one of the groups. Two ideas lead to the same answer under normality. Fisher looked for the linear combination of the variables that separates the groups best; the likelihood approach minimizes the expected cost of misclassification using the group densities, prior probabilities and costs, which is the **Bayes action** of [statistical decision theory](/3.2.7#sec-7.9) for a particular **loss function**. The resulting rules, linear and quadratic discriminant analysis, rest on the **multivariate normal distribution** ([3.4.2](/3.4.2)) and on the comparison of mean vectors ([3.4.4](/3.4.4)). The chapter ends with methods for estimating the error rate of a rule, in particular cross-validation, which is used again for choosing the number of clusters in the [next chapter](/3.4.11).

## 10.1. Introduction

Consider a few classification problems.

- A university wants to set an admission rule. For past students it knows whether they graduated successfully and their high-school grades and entrance-examination scores; a new applicant has only the scores.
- From brain-imaging measurements, decide which of several mental states a subject is in.
- For each of 150 iris flowers, four measurements (sepal length and width, petal length and width) were recorded together with the species (setosa, versicolor, virginica). Fisher developed his method in 1936 to classify these three species, and the iris data are used as a running example below.

*Discriminant analysis* is concerned with separation and classification: from measurements $\boldsymbol{x}$ on objects whose groups are known, we construct a rule that assigns a new object of unknown group to one of the prespecified groups. The training data form an $n \times (p+1)$ array whose last column is a group label, a categorical variable rather than a continuous one,

$$
D = \begin{bmatrix} x_{11} & x_{12} & \cdots & x_{1p} & g_1 \\ x_{21} & x_{22} & \cdots & x_{2p} & g_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ x_{n1} & x_{n2} & \cdots & x_{np} & g_n \end{bmatrix}, \qquad \tilde D = \begin{bmatrix} x_{01} & \cdots & x_{0p} & ? \end{bmatrix},
$$

and the task is to fill in the label of the new row $\tilde D$. The same problem is called pattern recognition or classification in machine learning.

Classification is needed when the group cannot be observed directly: it is revealed only in the future (whether an applicant will graduate), observing it destroys the object (the lifetime of a light bulb), or it is unavailable or expensive (a diagnosis that requires surgery). It is a prediction problem, but unlike [linear regression](/3.4.7) the response is a group label. We study two approaches:

1. Fisher's linear discriminant analysis, a geometric approach;
2. likelihood-based classification built on **Bayes' theorem**.

## 10.2. Fisher's Approach for Two Populations

Fisher's idea is to transform the multivariate observations $\boldsymbol{x}$ into univariate observations $y = \boldsymbol{a}^{\mathsf T}\boldsymbol{x}$ such that the values of $y$ coming from the populations $\pi_1$ and $\pi_2$ are separated as much as possible. The only assumption is that the two populations have a common covariance matrix, $\Sigma_1 = \Sigma_2$; normality is not assumed.

Let $\boldsymbol{x}_{11}, \dots, \boldsymbol{x}_{1n_1}$ be the sample from $\pi_1$ and $\boldsymbol{x}_{21}, \dots, \boldsymbol{x}_{2n_2}$ the sample from $\pi_2$, with sample means $\bar{\boldsymbol{x}}_1, \bar{\boldsymbol{x}}_2$ and sample covariance matrices $S_1, S_2$. The projected values are $y_{ij} = \boldsymbol{a}^{\mathsf T}\boldsymbol{x}_{ij}$ with means $\bar y_i = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_i$. Separation is measured by the distance between the projected means in units of the pooled standard deviation of $y$,

$$
\text{separation} = \frac{\lvert \bar y_1 - \bar y_2\rvert}{s_y}, \qquad s_y^2 = \frac{\sum_{j=1}^{n_1}(y_{1j}-\bar y_1)^2 + \sum_{j=1}^{n_2}(y_{2j}-\bar y_2)^2}{n_1+n_2-2}.
$$

Writing $y_{ij} - \bar y_i = \boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_{ij} - \bar{\boldsymbol{x}}_i)$ gives

$$
s_y^2 = \frac{\sum_{j}\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_{1j}-\bar{\boldsymbol{x}}_1)(\boldsymbol{x}_{1j}-\bar{\boldsymbol{x}}_1)^{\mathsf T}\boldsymbol{a} + \sum_{j}\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_{2j}-\bar{\boldsymbol{x}}_2)(\boldsymbol{x}_{2j}-\bar{\boldsymbol{x}}_2)^{\mathsf T}\boldsymbol{a}}{n_1+n_2-2} = \boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a},
$$

where $S_{\mathrm{pooled}} = \frac{(n_1-1)S_1 + (n_2-1)S_2}{n_1+n_2-2}$ is the **pooled sample covariance matrix**, the estimate of the common covariance matrix used for comparing two mean vectors in [3.4.4](/3.4.4).

**Theorem 10.2.1 (Fisher's Linear Discriminant)** Let $\boldsymbol{d} = \bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2$ and let $S_{\mathrm{pooled}}$ be positive definite. The linear combination

$$
\hat y = \hat{\boldsymbol{a}}^{\mathsf T}\boldsymbol{x} = (\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}\boldsymbol{x}
$$
maximizes the squared separation

$$
\frac{(\bar y_1 - \bar y_2)^2}{s_y^2} = \frac{(\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_1 - \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_2)^2}{\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a}} = \frac{(\boldsymbol{a}^{\mathsf T}\boldsymbol{d})^2}{\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a}}
$$
over all nonzero coefficient vectors $\boldsymbol{a}$; the maximizer is unique up to a nonzero scalar multiple, and the maximum value is $D^2 = (\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)$.

**Proof** This is the maximization lemma, Lemma 4.3.1, with $B = S_{\mathrm{pooled}}$. Directly: by the Cauchy–Schwarz inequality for the inner product $\langle \boldsymbol{u}, \boldsymbol{v}\rangle = \boldsymbol{u}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{v}$,

$$
(\boldsymbol{a}^{\mathsf T}\boldsymbol{d})^2 = \bigl(\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}(S_{\mathrm{pooled}}^{-1}\boldsymbol{d})\bigr)^2 \le (\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a})(\boldsymbol{d}^{\mathsf T}S_{\mathrm{pooled}}^{-1}\boldsymbol{d}),
$$
with equality if and only if $\boldsymbol{a} = c\,S_{\mathrm{pooled}}^{-1}\boldsymbol{d}$ for some $c \ne 0$. Dividing by $\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a} > 0$ gives the bound $D^2$, attained at $\hat{\boldsymbol{a}} = S_{\mathrm{pooled}}^{-1}\boldsymbol{d}$. $\square$

The maximal separation $D^2$ is the squared **Mahalanobis distance** between the two sample means; it is the quantity behind the two-sample **Hotelling's T²** statistic, $T^2 = \frac{n_1 n_2}{n_1+n_2}D^2$ ([3.4.4](/3.4.4)). Thus Fisher's direction is the direction in which the two-sample test sees the largest difference. Geometrically, $S_{\mathrm{pooled}}^{-1}$ first "whitens" the data so that the within-group scatter becomes spherical, and in the whitened coordinates the best direction is simply the line joining the two means.

To classify a new observation $\boldsymbol{x}_0$, compute $\hat y_0 = \hat{\boldsymbol{a}}^{\mathsf T}\boldsymbol{x}_0$ and compare it with the midpoint of the projected means,

$$
\hat m = \tfrac{1}{2}(\bar y_1 + \bar y_2) = \tfrac12(\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1 + \bar{\boldsymbol{x}}_2):
$$
allocate $\boldsymbol{x}_0$ to $\pi_1$ if $\hat y_0 \ge \hat m$ and to $\pi_2$ otherwise. This rule is linear discriminant analysis in its original form; §10.4 shows that it is also the optimal rule for two normal populations with equal priors and costs.

## 10.3. Classification with Costs and Priors

### 10.3.1. The Model

A good classification rule should make few misclassifications, but it should also take into account that misclassifications may have different costs (classifying a diseased patient as healthy is worse than the reverse) and that one population may be much more common than the other. Suppose, for example, that two iris species have different commercial value, and that one species is rare.

Let $f_1(\boldsymbol{x})$ and $f_2(\boldsymbol{x})$ be the probability densities of the $p \times 1$ random vector $\boldsymbol{X}$ in the populations $\pi_1$ and $\pi_2$, and let $\Omega$ be the sample space, the set of all possible observations $\boldsymbol{x}$. A classification rule is a partition of $\Omega$ into two disjoint regions: $R_1$, the set of $\boldsymbol{x}$ that we classify as $\pi_1$, and $R_2 = \Omega \setminus R_1$, the set classified as $\pi_2$. Let $p_1, p_2$ be the prior probabilities of $\pi_1, \pi_2$, with $p_1 + p_2 = 1$. The costs of misclassification form a cost matrix:

| True population | Classified as $\pi_1$ | Classified as $\pi_2$ |
|---|---|---|
| $\pi_1$ | $0$ | $c(2\mid 1)$ |
| $\pi_2$ | $c(1\mid 2)$ | $0$ |

The densities, priors and costs are given; the regions $R_1, R_2$ are what we want to find. The conditional probabilities of misclassification are

$$
\mathbb{P}(2\mid 1) = \mathbb{P}(\boldsymbol{X}\in R_2 \mid \pi_1) = \int_{R_2} f_1(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}, \qquad \mathbb{P}(1\mid 2) = \mathbb{P}(\boldsymbol{X}\in R_1 \mid \pi_2) = \int_{R_1} f_2(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x},
$$
so that an observation is misclassified as $\pi_2$ with probability $\mathbb{P}(\boldsymbol{X}\in R_2, \boldsymbol{X}\in\pi_1) = \mathbb{P}(2\mid 1)\,p_1$ and misclassified as $\pi_1$ with probability $\mathbb{P}(1\mid 2)\,p_2$.

### 10.3.2. Minimizing the Expected Cost of Misclassification

**Definition 10.3.1 (Expected Cost of Misclassification)** The cost of classifying an observation is the random variable that equals $c(2\mid 1)$ if $\boldsymbol{X}\in\pi_1$ and $\boldsymbol{X}\in R_2$, equals $c(1\mid 2)$ if $\boldsymbol{X}\in\pi_2$ and $\boldsymbol{X}\in R_1$, and is $0$ otherwise. Its expectation

$$
\mathrm{ECM}(R_1) = c(2\mid 1)\,\mathbb{P}(2\mid 1)\,p_1 + c(1\mid 2)\,\mathbb{P}(1\mid 2)\,p_2
$$
is the **expected cost of misclassification**.

**Theorem 10.3.1 (Minimum ECM Rule)** The regions $R_1$ and $R_2$ that minimize the ECM are

$$
R_1 = \left\{\boldsymbol{x} : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} \ge \frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right\}, \qquad R_2 = \left\{\boldsymbol{x} : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} < \frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right\},
$$
that is, classify as $\pi_1$ when (density ratio) $\ge$ (cost ratio) $\times$ (prior ratio).

**Proof** Since $R_1 \cup R_2 = \Omega$ and $\int_\Omega f_1 = 1$, we have $\mathbb{P}(2\mid 1) = 1 - \int_{R_1} f_1(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$. Hence

$$
\mathrm{ECM}(R_1) = c(2\mid 1)\,p_1 + \int_{R_1} h(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}, \qquad h(\boldsymbol{x}) = c(1\mid 2)\,p_2 f_2(\boldsymbol{x}) - c(2\mid 1)\,p_1 f_1(\boldsymbol{x}).
$$
The first term does not depend on the rule, and the integral is smallest when $R_1$ contains exactly the points where the integrand is nonpositive, $R_1 = \{\boldsymbol{x} : h(\boldsymbol{x}) \le 0\}$. Rearranging $h(\boldsymbol{x}) \le 0$ gives the stated inequality. (Points with $h(\boldsymbol{x}) = 0$ may be assigned either way.) $\square$

**Corollary 10.3.1** Special cases of the minimum ECM regions:

1. equal priors, $p_2/p_1 = 1$: $R_1 : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} \ge \frac{c(1\mid 2)}{c(2\mid 1)}$;
2. equal costs, $c(1\mid 2)/c(2\mid 1) = 1$: $R_1 : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} \ge \frac{p_2}{p_1}$;
3. equal priors and equal costs (or, more generally, $\frac{p_2}{p_1} = \frac{c(2\mid 1)}{c(1\mid 2)}$): $R_1 : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} \ge 1$.

In each case $R_2$ is the complement of $R_1$. Only ratios of costs and of priors matter, which is convenient because absolute costs are seldom known while relative costs often are.

### 10.3.3. Other Criteria

**Definition 10.3.2 (Total Probability of Misclassification)** Ignoring the costs, the **total probability of misclassification** of a rule is

$$
\mathrm{TPM} = \mathbb{P}(\text{misclassifying an observation}) = \mathbb{P}(1\mid 2)\,p_2 + \mathbb{P}(2\mid 1)\,p_1 = p_2\int_{R_1} f_2(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} + p_1\int_{R_2} f_1(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}.
$$

The TPM is the ECM with $c(1\mid 2) = c(2\mid 1) = 1$, so the rule minimizing it is case 2 of Corollary 10.3.1.

**Definition 10.3.3 (Bayes Classifier)** The posterior probability that an observation $\boldsymbol{x}_0$ comes from $\pi_1$ follows from **Bayes' theorem**:

$$
\mathbb{P}(\pi_1 \mid \boldsymbol{x}_0) = \frac{p_1 f_1(\boldsymbol{x}_0)}{p_1 f_1(\boldsymbol{x}_0) + p_2 f_2(\boldsymbol{x}_0)}, \qquad \mathbb{P}(\pi_2 \mid \boldsymbol{x}_0) = \frac{p_2 f_2(\boldsymbol{x}_0)}{p_1 f_1(\boldsymbol{x}_0) + p_2 f_2(\boldsymbol{x}_0)}.
$$
The **Bayes classifier** allocates $\boldsymbol{x}_0$ to $\pi_1$ when $\mathbb{P}(\pi_1 \mid \boldsymbol{x}_0) > \mathbb{P}(\pi_2 \mid \boldsymbol{x}_0)$, and to $\pi_2$ otherwise.

Since $\mathbb{P}(\pi_1\mid\boldsymbol{x}_0) > \mathbb{P}(\pi_2\mid\boldsymbol{x}_0)$ is the same as $p_1f_1(\boldsymbol{x}_0) > p_2f_2(\boldsymbol{x}_0)$, the Bayes classifier is again the minimum ECM rule with equal costs, so the three criteria agree. In the language of [decision theory](/3.2.7#sec-7.9), the action is the choice of a population, the unknown state is the true population, and the minimum ECM rule is the **Bayes action** under the **loss function** given by the cost matrix; with the $0$–$1$ loss it reduces to choosing the population with the larger **posterior distribution** probability. The ECM, TPM and Bayes classifier are thus three views of one rule; what remains is to specify the densities.

## 10.4. Two Multivariate Normal Populations

Assume now that $\pi_1 : \mathcal{N}_p(\boldsymbol{\mu}_1, \Sigma_1)$ and $\pi_2 : \mathcal{N}_p(\boldsymbol{\mu}_2, \Sigma_2)$. As in the comparison of two mean vectors ([3.4.4](/3.4.4)), we treat the cases $\Sigma_1 = \Sigma_2$ and $\Sigma_1 \ne \Sigma_2$ separately.

### 10.4.1. Equal Covariance Matrices: LDA

When $\Sigma_1 = \Sigma_2 = \Sigma$, the densities are

$$
f_i(\boldsymbol{x}) = \frac{1}{(2\pi)^{p/2}\lvert\Sigma\rvert^{1/2}}\exp\left\{-\frac12(\boldsymbol{x}-\boldsymbol{\mu}_i)^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_i)\right\}, \qquad i = 1, 2.
$$

**Theorem 10.4.1** For two normal populations with a common covariance matrix $\Sigma$, the regions that minimize the ECM are

$$
R_1 : (\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}\boldsymbol{x} - \frac12(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1+\boldsymbol{\mu}_2) \ge \ln\left[\frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right],
$$
and $R_2$ is the set where the reverse strict inequality holds.

**Proof** Taking logarithms in Theorem 10.3.1, $R_1 = \{\boldsymbol{x} : \ln(f_1(\boldsymbol{x})/f_2(\boldsymbol{x})) \ge \ln[(c(1\mid 2)/c(2\mid 1))(p_2/p_1)]\}$. The normalizing constants cancel because the covariance matrices are equal, so

$$
\begin{aligned}
\ln\frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} &= -\frac12(\boldsymbol{x}-\boldsymbol{\mu}_1)^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_1) + \frac12(\boldsymbol{x}-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_2) \\
&= -\frac12\bigl(-2\boldsymbol{\mu}_1^{\mathsf T}\Sigma^{-1}\boldsymbol{x} + \boldsymbol{\mu}_1^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_1\bigr) + \frac12\bigl(-2\boldsymbol{\mu}_2^{\mathsf T}\Sigma^{-1}\boldsymbol{x} + \boldsymbol{\mu}_2^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_2\bigr) \\
&= (\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}\boldsymbol{x} - \frac12(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1+\boldsymbol{\mu}_2).
\end{aligned}
$$
In the second line the quadratic terms $\boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}$ cancel, and we used $\boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_i = \boldsymbol{\mu}_i^{\mathsf T}\Sigma^{-1}\boldsymbol{x}$ (a scalar equals its transpose). The last line uses $\boldsymbol{\mu}_2^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_1 = \boldsymbol{\mu}_1^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_2$ for the same reason. $\square$

In practice $\boldsymbol{\mu}_1, \boldsymbol{\mu}_2, \Sigma$ are unknown and are replaced by the estimates used in two-sample inference: $\bar{\boldsymbol{x}}_1, \bar{\boldsymbol{x}}_2$ and $S_{\mathrm{pooled}}$.

**Definition 10.4.1 (Linear Discriminant Analysis)** The estimated minimum ECM rule for two normal populations with equal covariance matrices allocates $\boldsymbol{x}$ to $\pi_1$ if

$$
(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}\boldsymbol{x} - \frac12(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1+\bar{\boldsymbol{x}}_2) \ge \ln\left[\frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right]
$$
and to $\pi_2$ otherwise, where $S_{\mathrm{pooled}} = \frac{1}{n_1+n_2-2}\left[\sum_{j=1}^{n_1}(\boldsymbol{x}_{1j}-\bar{\boldsymbol{x}}_1)(\boldsymbol{x}_{1j}-\bar{\boldsymbol{x}}_1)^{\mathsf T} + \sum_{j=1}^{n_2}(\boldsymbol{x}_{2j}-\bar{\boldsymbol{x}}_2)(\boldsymbol{x}_{2j}-\bar{\boldsymbol{x}}_2)^{\mathsf T}\right]$. This rule is called **linear discriminant analysis** (LDA): its boundary is a hyperplane.

When $\frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1} = 1$ the right-hand side is $0$, and with $\hat y = (\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}\boldsymbol{x} = \hat{\boldsymbol{a}}^{\mathsf T}\boldsymbol{x}$ and $\bar y_i = \hat{\boldsymbol{a}}^{\mathsf T}\bar{\boldsymbol{x}}_i$ the rule becomes

$$
R_1 : \hat y \ge \tfrac12(\bar y_1 + \bar y_2), \qquad R_2 : \hat y < \tfrac12(\bar y_1 + \bar y_2),
$$
which is exactly Fisher's rule of §10.2. Fisher arrived at it without normality, by maximizing separation; the likelihood approach shows that under normality with equal covariances (and equal priors and costs) the same rule minimizes the expected cost. Unequal priors or costs only shift the threshold.

**Example 10.4.1** For the iris data with all four measurements, LDA with the sample proportions as priors (here equal, $50$ flowers per species) classifies the training data as follows (rows: true species; columns: predicted species).

| | setosa | versicolor | virginica |
|---|---|---|---|
| setosa | $50$ | $0$ | $0$ |
| versicolor | $0$ | $48$ | $2$ |
| virginica | $0$ | $1$ | $49$ |

Three of the 150 flowers are misclassified, all in the overlap of versicolor and virginica; setosa is perfectly separated. (The three-group rule used here is the one of §10.5.)

### 10.4.2. Unequal Covariance Matrices: QDA

**Theorem 10.4.2** For two normal populations $\mathcal{N}_p(\boldsymbol{\mu}_1, \Sigma_1)$ and $\mathcal{N}_p(\boldsymbol{\mu}_2, \Sigma_2)$ with $\Sigma_1 \ne \Sigma_2$, the regions that minimize the ECM are

$$
R_1 : -\frac12\boldsymbol{x}^{\mathsf T}(\Sigma_1^{-1} - \Sigma_2^{-1})\boldsymbol{x} + (\boldsymbol{\mu}_1^{\mathsf T}\Sigma_1^{-1} - \boldsymbol{\mu}_2^{\mathsf T}\Sigma_2^{-1})\boldsymbol{x} - k \ge \ln\left[\frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right],
$$
and $R_2$ is the set where the reverse strict inequality holds, where

$$
k = \frac12\ln\frac{\lvert\Sigma_1\rvert}{\lvert\Sigma_2\rvert} + \frac12\bigl(\boldsymbol{\mu}_1^{\mathsf T}\Sigma_1^{-1}\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2^{\mathsf T}\Sigma_2^{-1}\boldsymbol{\mu}_2\bigr).
$$

**Proof** Now the normalizing constants contribute $-\frac12\ln(\lvert\Sigma_1\rvert/\lvert\Sigma_2\rvert)$ to $\ln(f_1/f_2)$, and expanding the two quadratic forms as before gives $\ln\frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} = -\frac12\boldsymbol{x}^{\mathsf T}(\Sigma_1^{-1}-\Sigma_2^{-1})\boldsymbol{x} + (\boldsymbol{\mu}_1^{\mathsf T}\Sigma_1^{-1}-\boldsymbol{\mu}_2^{\mathsf T}\Sigma_2^{-1})\boldsymbol{x} - k$. Apply Theorem 10.3.1. $\square$

**Definition 10.4.2 (Quadratic Discriminant Analysis)** Replacing $\boldsymbol{\mu}_i$ by $\bar{\boldsymbol{x}}_i$ and $\Sigma_i$ by $S_i$ in Theorem 10.4.2 gives the **quadratic discriminant analysis** (QDA) rule; its boundary is a quadratic surface.

The quadratic term disappears exactly when $\Sigma_1 = \Sigma_2$, in which case QDA reduces to LDA. QDA estimates a separate covariance matrix for each group, $p(p+1)/2$ parameters per group instead of $p(p+1)/2$ in total, so it needs larger samples. It also relies more heavily on normality: the linear rule has Fisher's justification without normality, while the quadratic rule does not, and it can be badly affected by non-normal data.

**Example 10.4.2** For the iris data, QDA misclassifies the same three training flowers as LDA, so the apparent error rates coincide in this example; under the leave-one-out evaluation of §10.6, QDA makes one more error than LDA.

![Two simulated normal populations with unequal covariance matrices. Left: the LDA boundary is a straight line. Right: the QDA boundary is a conic that adapts to the different spreads.](./plots/lda-qda-boundaries.py)

## 10.5. Classification for Several Populations

This section extends both approaches to $g > 2$ populations. The emphasis is on the geometric meaning of Fisher's discriminants and on applying the rules; the derivations follow the two-population case.

### 10.5.1. The Minimum ECM Rule

Let $f_i$ be the density of population $\pi_i$, $p_i$ its prior probability, $R_i$ the region classified as $\pi_i$, and $c(k\mid i)$ the cost of classifying an object of $\pi_i$ as $\pi_k$ (with $c(i\mid i) = 0$). With $\mathbb{P}(k\mid i) = \mathbb{P}(\boldsymbol{X}\in R_k \mid \pi_i) = \int_{R_k} f_i(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$, the conditional expected cost for an object of $\pi_i$ is $\mathrm{ECM}(i) = \sum_{k\ne i}\mathbb{P}(k\mid i)\,c(k\mid i)$, and

$$
\mathrm{ECM} = \sum_{i=1}^g p_i\,\mathrm{ECM}(i) = \sum_{i=1}^g p_i\sum_{k\ne i}\mathbb{P}(k\mid i)\,c(k\mid i).
$$

**Theorem 10.5.1** The ECM is minimized over all partitions $R_1, \dots, R_g$ by allocating $\boldsymbol{x}$ to the population $\pi_k$ for which

$$
\sum_{i\ne k} p_i f_i(\boldsymbol{x})\,c(k\mid i)
$$
is smallest. If all misclassification costs are equal, this means allocating $\boldsymbol{x}$ to $\pi_k$ when $p_k f_k(\boldsymbol{x}) > p_i f_i(\boldsymbol{x})$ for all $i \ne k$, equivalently when the posterior probability

$$
\mathbb{P}(\pi_k \mid \boldsymbol{x}) = \frac{p_k f_k(\boldsymbol{x})}{p_1 f_1(\boldsymbol{x}) + \cdots + p_g f_g(\boldsymbol{x})}
$$
is the largest.

**Proof** Exchanging the sums, $\mathrm{ECM} = \sum_{k=1}^g\int_{R_k}\sum_{i\ne k}p_i f_i(\boldsymbol{x})\,c(k\mid i)\,\mathrm{d}\boldsymbol{x}$, and this is smallest when every $\boldsymbol{x}$ is put in the region whose integrand is smallest at $\boldsymbol{x}$. With equal costs $c$, the integrand is $c\bigl(\sum_i p_i f_i(\boldsymbol{x}) - p_k f_k(\boldsymbol{x})\bigr)$, which is smallest when $p_k f_k(\boldsymbol{x})$ is largest. $\square$

For normal populations, maximizing $\ln(p_k f_k(\boldsymbol{x}))$ gives the quadratic discriminant scores $-\frac12\ln\lvert\Sigma_k\rvert - \frac12(\boldsymbol{x}-\boldsymbol{\mu}_k)^{\mathsf T}\Sigma_k^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_k) + \ln p_k$, and, with a common $\Sigma$, the linear scores $\boldsymbol{\mu}_k^{\mathsf T}\Sigma^{-1}\boldsymbol{x} - \frac12\boldsymbol{\mu}_k^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_k + \ln p_k$; the sample versions are QDA and LDA for $g$ groups.

### 10.5.2. Fisher's Discriminants for Several Groups

For $g$ groups Fisher's approach raises three questions: in how many dimensions should we project, along which directions, and how do we classify a new unit in the projected space? The answer generalizes the decomposition of variation used in **analysis of variance**. Let $\boldsymbol{x}_{lj}$, $j = 1, \dots, n_l$, be the sample from group $l$, $\bar{\boldsymbol{x}}_l$ the group means and $\bar{\boldsymbol{x}}$ the overall mean. For one variable, the total sum of squares splits into a between-groups and a within-groups part,

$$
\underbrace{\sum_{l=1}^g\sum_{j=1}^{n_l}(x_{lj}-\bar x)^2}_{\text{total (corrected) SS}} = \underbrace{\sum_{l=1}^g n_l(\bar x_l-\bar x)^2}_{\text{between-groups SS}} + \underbrace{\sum_{l=1}^g\sum_{j=1}^{n_l}(x_{lj}-\bar x_l)^2}_{\text{within-groups SS}},
$$
and for vectors the same identity holds for matrices of sums of squares and cross products:

$$
\sum_{l=1}^g\sum_{j=1}^{n_l}(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}})(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}})^{\mathsf T} = B + W, \qquad B = \sum_{l=1}^g n_l(\bar{\boldsymbol{x}}_l-\bar{\boldsymbol{x}})(\bar{\boldsymbol{x}}_l-\bar{\boldsymbol{x}})^{\mathsf T}, \quad W = \sum_{l=1}^g\sum_{j=1}^{n_l}(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}}_l)(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}}_l)^{\mathsf T}.
$$

Assume a common covariance matrix, $\Sigma_1 = \cdots = \Sigma_g = \Sigma$, and consider $Y = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$. Then $\mathbb{E}[Y \mid \pi_i] = \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}_i$ and $\operatorname{Var}(Y) = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}$ in every population. The sample means of $Y$ are $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_i$ in the groups and $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}$ overall, and the projected data have between-groups SS $\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}$ and within-groups SS $\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}$. Fisher's criterion is the ratio

$$
\frac{\sum_{i=1}^g n_i(\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_i - \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}})^2}{\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}} = \frac{\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}},
$$
the spread of the projected group means relative to the spread within groups. It is a generalized **Rayleigh quotient**, and its maximization is a generalized eigenvalue problem.

**Theorem 10.5.2 (Fisher's Discriminants)** Let $W$ be positive definite, let $\hat\lambda_1 \ge \cdots \ge \hat\lambda_s > 0$ be the $s \le \min(g-1, p)$ nonzero **eigenvalues** of $W^{-1}B$, and let $\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_s$ be corresponding **eigenvectors**, scaled so that $\hat{\boldsymbol{e}}_k^{\mathsf T}S_{\mathrm{pooled}}\hat{\boldsymbol{e}}_k = 1$, where $S_{\mathrm{pooled}} = W/(n_1+\cdots+n_g-g)$ is the estimate of $\Sigma$. Then the coefficient vector that maximizes $\frac{\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}}$ is $\hat{\boldsymbol{a}}_1 = \hat{\boldsymbol{e}}_1$, with maximum $\hat\lambda_1$; and for $k = 2, \dots, s$, $\hat{\boldsymbol{a}}_k = \hat{\boldsymbol{e}}_k$ maximizes the ratio subject to $\hat{\boldsymbol{a}}_k^{\mathsf T}S_{\mathrm{pooled}}\hat{\boldsymbol{a}}_i = 0$ for $i < k$, with maximum $\hat\lambda_k$. The linear combination $\hat y_k = \hat{\boldsymbol{a}}_k^{\mathsf T}\boldsymbol{x}$ is called the sample $k$-th discriminant, $k \le s$.

**Proof** Write $W = W^{1/2}W^{1/2}$ and substitute $\boldsymbol{b} = W^{1/2}\boldsymbol{a}$: the ratio becomes $\frac{\boldsymbol{b}^{\mathsf T}W^{-1/2}BW^{-1/2}\boldsymbol{b}}{\boldsymbol{b}^{\mathsf T}\boldsymbol{b}}$, the Rayleigh quotient of the symmetric positive semidefinite matrix $W^{-1/2}BW^{-1/2}$. Its successive maxima under orthogonality constraints are its eigenvalues, attained at its eigenvectors $\boldsymbol{b}_k$ ([2.1.7](/2.1.7)). The matrix $W^{-1/2}BW^{-1/2}$ has the same eigenvalues as $W^{-1}B$, and $\boldsymbol{a}_k = W^{-1/2}\boldsymbol{b}_k$ are eigenvectors of $W^{-1}B$; orthogonality $\boldsymbol{b}_i^{\mathsf T}\boldsymbol{b}_k = 0$ translates into $\boldsymbol{a}_i^{\mathsf T}W\boldsymbol{a}_k = 0$, that is $\boldsymbol{a}_i^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a}_k = 0$. Finally, $B$ is a sum of $g$ rank-one matrices whose vectors $\bar{\boldsymbol{x}}_l - \bar{\boldsymbol{x}}$ satisfy $\sum_l n_l(\bar{\boldsymbol{x}}_l - \bar{\boldsymbol{x}}) = \boldsymbol{0}$, so $\operatorname{rank}(B) \le \min(g-1, p)$. $\square$

The discriminants are uncorrelated with unit variance in the pooled metric: $\hat{\boldsymbol{a}}_i^{\mathsf T}S_{\mathrm{pooled}}\hat{\boldsymbol{a}}_k = 1$ if $i = k \le s$ and $0$ otherwise. With two groups, $B$ has rank one and $\hat{\boldsymbol{a}}_1 \propto S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)$, which recovers Theorem 10.2.1.

To classify, let $Y_k = \boldsymbol{a}_k^{\mathsf T}\boldsymbol{X}$ be the $k$-th discriminant and $\boldsymbol{Y} = (Y_1, \dots, Y_r)^{\mathsf T}$ the vector of the first $r \le s$ discriminants; in population $\pi_i$ it has mean $\boldsymbol{\mu}_{iY} = (\boldsymbol{a}_1^{\mathsf T}\boldsymbol{\mu}_i, \dots, \boldsymbol{a}_r^{\mathsf T}\boldsymbol{\mu}_i)^{\mathsf T}$ and, by the normalization, identity covariance matrix. Fisher's rule allocates $\boldsymbol{y}$ to the group whose projected mean is closest in Euclidean distance:

$$
\text{allocate to } \pi_k \text{ if } (\boldsymbol{y}-\boldsymbol{\mu}_{kY})^{\mathsf T}(\boldsymbol{y}-\boldsymbol{\mu}_{kY}) = \sum_{j=1}^r(y_j - \mu_{kY_j})^2 \le \sum_{j=1}^r(y_j - \mu_{iY_j})^2 \quad \text{for all } i \ne k,
$$
with the sample quantities $\hat{\boldsymbol{a}}_j$ and $\bar{\boldsymbol{x}}_i$ substituted. In discriminant coordinates the groups have spherical scatter, so Euclidean distance there is Mahalanobis distance in the original space; using all $s$ discriminants, the rule coincides with the linear rule of Theorem 10.5.1 with equal priors. The value of the projection is that $r = 1$ or $2$ discriminants usually carry almost all the separation and can be plotted.

**Remark 10.5.1** Finding the directions does not require equal covariance matrices: maximizing $\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}/\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}$ simply finds the projections in which the group centers are most spread out relative to the within-group scatter. The assumption is needed for the classification step: if the covariance matrices differ, the projected groups do not have a common spherical scatter, and Euclidean distance to the projected means is no longer a sensible rule.

**Example 10.5.1** For the iris data, $g = 3$ and $p = 4$, so there are $s = 2$ discriminants, and the plot of the discriminant scores shows all the separation available to a linear rule. The first discriminant alone separates setosa from the other two species and carries over $99\%$ of the between-group variation ($\hat\lambda_1/(\hat\lambda_1+\hat\lambda_2)$). A new flower is classified by computing its two scores and finding the nearest projected group mean.

![Iris data projected onto the first two sample discriminants (left) and onto the first two principal components (right). The discriminants maximize between-group relative to within-group spread, while the principal components maximize total variance without using the labels; crosses mark group means.](./plots/iris-discriminant-projection.py)

**Remark 10.5.2 (LDA and Canonical Correlation)** Let $\boldsymbol{X}$ be the measurements and let the second set of variables consist of group indicators, $Z_l = \boldsymbol{1}_{\{\text{group } l\}}$; only $g-1$ of them are needed, since the indicators sum to one. Then the first canonical coefficient vector of $\boldsymbol{X}$ in **canonical correlation analysis** ([3.4.9](/3.4.9)) is proportional to Fisher's first discriminant, although the two methods are motivated differently. Indeed, CCA takes eigenvectors of $\Sigma_{11}^{-1}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$. With indicator variables, the sample version of $\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ is proportional to $B$ (the variation of $\boldsymbol{X}$ explained by the group means), and the sample version of $\Sigma_{11}$ is proportional to $B + W$; at the population level this is the **law of total variance**, $\operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[\operatorname{Cov}(\boldsymbol{X}\mid G)] + \operatorname{Cov}(\mathbb{E}[\boldsymbol{X}\mid G])$. If $(B+W)^{-1}B\boldsymbol{a} = \rho^2\boldsymbol{a}$, then $(1-\rho^2)B\boldsymbol{a} = \rho^2 W\boldsymbol{a}$, so

$$
W^{-1}B\boldsymbol{a} = \frac{\rho^2}{1-\rho^2}\boldsymbol{a}:
$$
the eigenvectors coincide and the eigenvalues are related by $\hat\lambda = \rho^2/(1-\rho^2)$, where $\rho$ is a canonical correlation. This identity holds whether or not the covariance matrices are equal.

### 10.5.3. Relation to MANOVA

The decomposition $B + W$ is the one used in *multivariate analysis of variance* (MANOVA), which tests whether $g$ mean vectors are equal. The one-way model is

$$
\boldsymbol{X}_{lj} = \boldsymbol{\mu} + \boldsymbol{\tau}_l + \boldsymbol{e}_{lj}, \qquad j = 1, \dots, n_l, \ l = 1, \dots, g, \qquad \sum_{l=1}^g n_l\boldsymbol{\tau}_l = \boldsymbol{0},
$$
with overall mean $\boldsymbol{\mu}$, treatment effects $\boldsymbol{\tau}_l$ (the constraint makes them identifiable) and independent errors $\boldsymbol{e}_{lj} \sim \mathcal{N}_p(\boldsymbol{0}, \Sigma)$. The null hypothesis is $H_0 : \boldsymbol{\tau}_1 = \cdots = \boldsymbol{\tau}_g = \boldsymbol{0}$. Each observation decomposes as

$$
\boldsymbol{x}_{lj} = \underbrace{\bar{\boldsymbol{x}}}_{\text{overall mean}} + \underbrace{(\bar{\boldsymbol{x}}_l - \bar{\boldsymbol{x}})}_{\text{estimated treatment effect}} + \underbrace{(\boldsymbol{x}_{lj} - \bar{\boldsymbol{x}}_l)}_{\text{residual}},
$$
and the sums of squares of the univariate ANOVA table become matrices:

| Source of variation | Matrix of sums of squares and cross products | Degrees of freedom |
|---|---|---|
| Treatments | $B = \sum_{l} n_l(\bar{\boldsymbol{x}}_l-\bar{\boldsymbol{x}})(\bar{\boldsymbol{x}}_l-\bar{\boldsymbol{x}})^{\mathsf T}$ | $g-1$ |
| Residual (error) | $W = \sum_{l}\sum_{j}(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}}_l)(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}}_l)^{\mathsf T}$ | $\sum_l n_l - g$ |
| Total (corrected for the mean) | $B + W = \sum_{l}\sum_{j}(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}})(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}})^{\mathsf T}$ | $\sum_l n_l - 1$ |

MANOVA tests are functions of the eigenvalues $\hat\lambda_k$ of $W^{-1}B$; for instance, Wilks' lambda is $\lvert W\rvert/\lvert B+W\rvert = \prod_k(1+\hat\lambda_k)^{-1}$. MANOVA asks whether the groups differ; Fisher's discriminants show in which directions they differ most.

## 10.6. Evaluating Classification Functions

Can two heavily overlapping populations be separated with high accuracy? No rule can do better than the overlap allows, so before judging a procedure we want to know the bound on what is achievable, and we need a way to estimate the error rate of any procedure from data. There are two kinds of measures:

- when the densities $f_1, f_2$ are known: the total probability of misclassification (population-based) and the actual error rate of a rule built from a sample;
- when the distributions are unknown (the general case): the apparent error rate and cross-validated error rates.

### 10.6.1. The Optimum Error Rate

**Definition 10.6.1 (Optimum and Actual Error Rates)** The **optimum error rate** is the smallest TPM, attained by the minimum TPM rule of §10.3. The **actual error rate** of a rule $\hat R_1, \hat R_2$ constructed from a sample is its TPM under the true densities,

$$
\mathrm{AER} = p_1\int_{\hat R_2} f_1(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} + p_2\int_{\hat R_1} f_2(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}.
$$

**Proposition 10.6.1** Let $\pi_i = \mathcal{N}_p(\boldsymbol{\mu}_i, \Sigma)$, $i = 1, 2$, with $p_1 = p_2$, and let $\Delta^2 = (\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)$ be the squared Mahalanobis distance between the populations. Then the optimum error rate is

$$
\min \mathrm{TPM} = \Phi\left(-\frac{\Delta}{2}\right),
$$
where $\Phi$ is the standard normal distribution function.

**Proof** With equal priors and costs the optimal rule (Theorem 10.4.1) depends on $\boldsymbol{x}$ only through $Y = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ with $\boldsymbol{a} = \Sigma^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)$: allocate to $\pi_1$ if $Y \ge m = \frac12(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1+\boldsymbol{\mu}_2)$. Under $\pi_i$, $Y$ is normal with mean $\mu_{iY} = \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}_i$ and variance $\sigma_Y^2 = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} = \Delta^2$, and $m - \mu_{1Y} = -\frac12\Delta^2$, $m - \mu_{2Y} = \frac12\Delta^2$. Hence

$$
\mathbb{P}(2\mid 1) = \mathbb{P}(Y < m \mid \pi_1) = \mathbb{P}\left(\frac{Y-\mu_{1Y}}{\sigma_Y} < \frac{-\Delta^2/2}{\Delta}\right) = \Phi\left(-\frac{\Delta}{2}\right),
$$
and similarly $\mathbb{P}(1\mid 2) = \Phi(-\Delta/2)$. Therefore $\min\mathrm{TPM} = \frac12\mathbb{P}(2\mid 1) + \frac12\mathbb{P}(1\mid 2) = \Phi(-\Delta/2)$. $\square$

For example, if $\Delta^2 = 2.56$ then $\Delta = 1.6$ and the minimum TPM is $\Phi(-0.8) = 0.2119$: even the optimal rule allocates about $21\%$ of the items to the wrong population. The error rate depends on the populations only through $\Delta$, so a large Mahalanobis distance between the means is the condition for easy classification.

![Left: the discriminant score Y has normal densities with means separated by Delta squared and common variance Delta squared; the shaded tails beyond the midpoint are the two misclassification probabilities. Right: the optimum error rate Phi(-Delta/2) as a function of Delta.](./plots/optimum-error-rate.py)

### 10.6.2. The Apparent Error Rate

Usually the populations are unknown, and we need an index that does not depend on a model. The idea is to estimate probabilities by proportions. Apply the sample classification rule to the training data and tabulate the result:

| | Predicted $\pi_1$ | Predicted $\pi_2$ | Total |
|---|---|---|---|
| Actual $\pi_1$ | $n_{1C}$ | $n_{1M} = n_1 - n_{1C}$ | $n_1$ |
| Actual $\pi_2$ | $n_{2M} = n_2 - n_{2C}$ | $n_{2C}$ | $n_2$ |

Here $n_{iC}$ is the number of items of $\pi_i$ correctly classified and $n_{iM}$ the number misclassified.

**Definition 10.6.2 (Apparent Error Rate)** The table above is the **confusion matrix** of the rule. The **apparent error rate** (APER) is the fraction of observations in the training sample that are misclassified by the sample classification function,

$$
\mathrm{APER} = \frac{n_{1M} + n_{2M}}{n_1 + n_2}.
$$

The APER is intuitive and easy to compute. Unfortunately it tends to underestimate the AER, because the same data are used twice: once to build the rule and once to evaluate it. The rule adapts to the particular sample, including its noise, and so performs better on that sample than on new data. Imagine two normal populations and six training points near the boundary: the rule built from them may classify all six correctly, giving $\mathrm{APER} = 0$, while its error probability under the true densities, the AER, is the whole area of the two tails on the wrong sides of the estimated boundary. Since the true densities are unknown, the AER cannot be computed; only the APER can, and it is optimistic. This is **overfitting**, met already in regression ([3.4.7](/3.4.7)), and it is a general problem of statistical learning, not limited to discriminant analysis.

### 10.6.3. Cross-Validation

The remedy for overfitting is not to use the same data twice: hold out one case (or a set of cases), build the rule from the remaining data, and evaluate it on the held-out cases. Cycling the hold-out over all the data gives a nearly unbiased estimate of the error rate, at a higher computational cost.

**Definition 10.6.3 (Cross-Validation)** **Cross-validation** splits the data into a training set, used to build the rule, and a validation set, used to evaluate it, and repeats the split so that every observation is used for validation once.

1. **Leave-one-out cross-validation** (LOOCV): for each sample point $\boldsymbol{x}_i$, build the rule from all the data except $\boldsymbol{x}_i$ and use it to classify $\boldsymbol{x}_i$; the proportion of misclassified points estimates the error rate.
2. $K$-fold cross-validation: divide the sample into $K$ parts of nearly equal size; for each part, build the rule from the other $K-1$ parts and evaluate it on that part; average the $K$ error rates.

Cross-validation is a general method: it applies to any procedure that is fitted to data and evaluated by a loss, and it is used again for choosing the number of clusters ([3.4.11](/3.4.11)) and the number of neighbors in $k$-nearest-neighbor classification ([3.4.12](/3.4.12)).

**Example 10.6.1** For LDA on the iris data, the APER is $3/150 = 0.02$, and the leave-one-out error rate is also $3/150 = 0.02$, with the same confusion matrix: the three misclassified flowers stay misclassified and no new errors appear. That the two estimates coincide is a coincidence of this well-separated example; usually the cross-validated error rate is larger than the APER. For QDA, which has more parameters, the APER is again $0.02$ but the leave-one-out error rate is $4/150 \approx 0.027$.

### 10.6.4. Other Evaluation Measures

For two groups, call one group positive and the other negative; the confusion matrix then counts true positives (TP), false negatives (FN), false positives (FP) and true negatives (TN).

**Definition 10.6.4 (Accuracy, Precision, Recall, Specificity)** For a two-group classification rule,

$$
\text{accuracy} = \frac{\mathrm{TP}+\mathrm{TN}}{\mathrm{TP}+\mathrm{TN}+\mathrm{FP}+\mathrm{FN}}, \quad \text{precision} = \frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}}, \quad \text{recall} = \frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}}, \quad \text{specificity} = \frac{\mathrm{TN}}{\mathrm{TN}+\mathrm{FP}}.
$$
The **accuracy** is $1 - \mathrm{APER}$; the **precision** is the proportion of true positives among those declared positive; the **recall** (or **sensitivity**) is the proportion of positives that are detected; the **specificity** is the proportion of negatives correctly declared negative.

Most rules have a threshold (in Theorem 10.4.1, the logarithm of the cost and prior ratios). Varying the threshold trades sensitivity against specificity, and plotting the true positive rate (sensitivity) against the false positive rate ($1 -$ specificity) over all thresholds gives the *ROC curve* (receiver operating characteristic). A rule that guesses at random lies on the diagonal; a better rule bends toward the upper left corner. The *area under the curve* (AUC) summarizes it in one number between $0.5$ (random) and $1$ (perfect separation). The ROC curve is designed for two groups; the precision–recall curve is preferred when positives are rare, and there are extensions of the ROC curve to more groups.

## 10.7. Discussion

### 10.7.1. Changing Scales

Should the variables be standardized when they are measured on very different scales? For LDA it is unnecessary: the results are invariant under nonsingular linear transformations, in the following sense. If $\boldsymbol{x}^* = A\boldsymbol{x} + \boldsymbol{b}$ with $A$ nonsingular, then $\bar{\boldsymbol{x}}_i^* = A\bar{\boldsymbol{x}}_i + \boldsymbol{b}$ and $S_{\mathrm{pooled}}^* = AS_{\mathrm{pooled}}A^{\mathsf T}$, so

$$
\hat{\boldsymbol{a}}^* = (S_{\mathrm{pooled}}^*)^{-1}(\bar{\boldsymbol{x}}_1^* - \bar{\boldsymbol{x}}_2^*) = A^{-\mathsf T}\hat{\boldsymbol{a}}, \qquad \hat{\boldsymbol{a}}^{*\mathsf T}\boldsymbol{x}^* = \hat{\boldsymbol{a}}^{\mathsf T}\boldsymbol{x} + \hat{\boldsymbol{a}}^{\mathsf T}A^{-1}\boldsymbol{b}.
$$
The coefficients change, but the discriminant scores change only by a constant that also shifts the threshold, and the separation $D^2$ is unchanged. Every observation is therefore classified in the same way. Standardizing the variables (a diagonal $A$) only rescales the coefficients, which can make them easier to compare; for the iris data the plot of the classification after standardization is the earlier plot with relabeled axes. QDA has the same invariance.

### 10.7.2. Limitations and Transformations

LDA can only produce linear boundaries. Two classes arranged as concentric rings cannot be separated by any linear rule in the original coordinates $(x_1, x_2)$, but after the transformation $(x_1, x_2) \mapsto (x_1^2, x_2^2)$ they are separated by a straight line. More generally, a linear boundary in the five-dimensional space $(X_1, X_2, X_1X_2, X_1^2, X_2^2)$ is a quadratic boundary in the original plane. Enlarging the feature space in this way, explicitly or implicitly through a kernel as in **kernel PCA** ([3.4.6](/3.4.6)), turns linear methods into flexible nonlinear ones.

### 10.7.3. Other Classification Methods

From the point of view of applications, the following extend or replace LDA.

- Regularized LDA, for when $S_{\mathrm{pooled}}$ is not of full rank (for instance $p > n$): replace $S_{\mathrm{pooled}}$ by $S_{\mathrm{pooled}} + \lambda I_p$, $\lambda > 0$, so that $R_1 : (\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}(S_{\mathrm{pooled}}+\lambda I_p)^{-1}\boldsymbol{x} \ge \frac12(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}(S_{\mathrm{pooled}}+\lambda I_p)^{-1}(\bar{\boldsymbol{x}}_1+\bar{\boldsymbol{x}}_2)$; a more general form is discussed in [3.4.12](/3.4.12).
- Kernel Fisher discriminant analysis, when linear discriminants are not suitable: Fisher's criterion in a feature space defined by a kernel.
- Mixture discriminant analysis: each group is modeled by a mixture of normal distributions instead of a single one (compare the Gaussian mixtures of [3.4.11](/3.4.11)).
- Logistic and probit regression, which model the posterior probability directly, $\ln\frac{p}{1-p} = \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$ or $\Phi^{-1}(p) = \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$, where $p = \mathbb{P}(\pi_1\mid\boldsymbol{x})$. They do not require normality, but when the normal model holds they are less efficient than LDA ([3.4.12](/3.4.12)).
- Support vector machines, $k$-nearest neighbors and decision trees, from statistical learning.

Two of these deserve a closer look. A *support vector machine* (SVM) uses data $(\boldsymbol{x}_i, y_i)$, $i = 1, \dots, n$, with labels $y_i \in \{-1, 1\}$, and a linear function $f(\boldsymbol{x}) = \boldsymbol{\beta}^{\mathsf T}\boldsymbol{x} + \beta_0$. The hyperplane $\{\boldsymbol{x} : f(\boldsymbol{x}) = 0\}$ has normal vector $\boldsymbol{\beta}$, which we may normalize to $\|\boldsymbol{\beta}\| = 1$; the rule classifies by $\operatorname{sgn}(f(\boldsymbol{x}))$, and if the classes are separable we can find $f$ with $y_i f(\boldsymbol{x}_i) > 0$ for all $i$. Among all separating hyperplanes, the SVM chooses the one with the largest margin $M$:

$$
\max_{\boldsymbol{\beta}, \beta_0, \|\boldsymbol{\beta}\| = 1} M \quad \text{subject to } y_i(\boldsymbol{\beta}^{\mathsf T}\boldsymbol{x}_i + \beta_0) \ge M, \ i = 1, \dots, n,
$$
which is equivalent to $\min_{\boldsymbol{\beta}, \beta_0}\|\boldsymbol{\beta}\|$ subject to $y_i(\boldsymbol{\beta}^{\mathsf T}\boldsymbol{x}_i + \beta_0) \ge 1$ (set $M = 1/\|\boldsymbol{\beta}\|$). The solution depends only on the points on the margin, the support vectors; points well inside their class do not affect the boundary, in contrast to LDA, which uses all points through the means and covariances. When the classes overlap, slack variables $\varepsilon_i$ allow some points on the wrong side:

$$
\max_{\boldsymbol{\beta}, \beta_0, \|\boldsymbol{\beta}\| = 1} M \quad \text{subject to } y_i(\boldsymbol{\beta}^{\mathsf T}\boldsymbol{x}_i + \beta_0) \ge M(1 - \varepsilon_i), \quad \varepsilon_i \ge 0, \quad \sum_i\varepsilon_i \le C.
$$

A decision tree grows by recursively splitting the data on one variable at a time, choosing each split to minimize an impurity function of the class proportions in the resulting nodes, until a stopping rule is met; the tree is then pruned. Two common impurity functions are the entropy, whose minimization corresponds to maximizing the multinomial likelihood of the node labels, and the Gini index $\sum_k \hat p_k(1-\hat p_k)$, which is the expected error rate of a rule that labels a point at random according to the node proportions $\hat p_k$.

## Summary {#summary}

| | Assumptions | Rule | Boundary |
|---|---|---|---|
| Fisher's discriminant (projection) | $\Sigma_1 = \Sigma_2$; no normality | maximize $(\boldsymbol{a}^{\mathsf T}\boldsymbol{d})^2/\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a}$, so $\hat{\boldsymbol{a}} \propto S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)$ | linear |
| Minimum ECM / Bayes classifier | densities, priors, costs known | $f_1/f_2 \ge (c(1\mid 2)/c(2\mid 1))(p_2/p_1)$ | any |
| LDA | normal, $\Sigma_1 = \Sigma_2$ | minimum ECM with $\bar{\boldsymbol{x}}_i$, $S_{\mathrm{pooled}}$; equals Fisher's rule when costs × priors are balanced | linear |
| QDA | normal, $\Sigma_1 \ne \Sigma_2$ | minimum ECM with $\bar{\boldsymbol{x}}_i$, $S_i$ | quadratic |
| $g$ groups (Fisher) | common $\Sigma$ for classification | eigenvectors of $W^{-1}B$; nearest projected mean | linear |

The rules are evaluated by the APER or ROC curve combined with cross-validation, which corrects the optimism of evaluating a rule on its own training data, and the minimum TPM gives the bound on achievable accuracy. In R, LDA and QDA are the functions `lda` and `qda` of the package MASS (with `predict` for new data; the option `CV = TRUE` gives leave-one-out predictions).
