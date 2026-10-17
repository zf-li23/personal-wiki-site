---
title: Covariance and Correlation
source_hash: 3a21c3933e7a
---

Expectation and variance summarize a single random variable; this chapter introduces numerical characteristics that summarize the relationship between two random variables. In portfolio theory, Markowitz (Nobel Memorial Prize in Economics, 1990) measured the return of a portfolio by its expectation and its risk by its variance, and the variance of a portfolio depends not only on the variances of the individual assets but also on the covariances between them; in neuroscience, the "functional connectivity" between the signals of two brain regions is often measured by a correlation coefficient. We first define the covariance and establish its properties, then standardize it into the correlation coefficient, discuss the relation between uncorrelatedness and independence, the geometric meaning of the correlation coefficient (the cosine of an angle) and the best linear predictor, and finally extend these notions to random vectors by defining the covariance matrix. The chapter uses the expectation and variance of [3.1.8](/3.1.8) and the conditional expectation of [3.1.9](/3.1.9); the covariance matrix is the foundation of the multivariate normal distribution ([3.1.15](/3.1.15)), linear regression ([3.3](/3.3)) and multivariate statistical analysis.

## 10.1. Covariance

### 10.1.1. Definition

How can a single number summarize how $X$ and $Y$ vary together? First remove location by centering, and consider $X - \mathbb{E}X$ and $Y - \mathbb{E}Y$. Taking $(\mathbb{E}X, \mathbb{E}Y)$ as the origin divides the plane into four quadrants. If $(X, Y)$ falls mostly in the first and third quadrants (both large or both small at the same time), the product $(X - \mathbb{E}X)(Y - \mathbb{E}Y)$ is mostly positive; if it falls mostly in the second and fourth quadrants, the product is mostly negative. Averaging the product gives the covariance.

**Definition 10.1.1 (Covariance)** Suppose $\mathbb{E}X$ and $\mathbb{E}Y$ exist. If $\mathbb{E}\lvert(X - \mathbb{E}X)(Y - \mathbb{E}Y)\rvert < \infty$, the quantity

$$
\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}X)(Y - \mathbb{E}Y)]
$$
is called the **covariance** of the random variables $X$ and $Y$.

When the covariance is positive, zero or negative, $X$ and $Y$ are said to be positively correlated, uncorrelated or negatively correlated, respectively. By the Cauchy–Schwarz inequality, the covariance exists whenever $X$ and $Y$ have finite variances.

**Property 10.1.1** Assuming all covariances involved exist,

1. $\operatorname{Cov}(X, X) = \operatorname{Var}(X)$;
2. $\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)$;
3. $\operatorname{Cov}(X, Y) = \mathbb{E}(XY) - \mathbb{E}X\,\mathbb{E}Y$ (the usual computational formula);
4. if $c$ is a constant, then $\operatorname{Cov}(X, c) = 0$;
5. (bilinearity) $\operatorname{Cov}(cX, Y) = c\operatorname{Cov}(X, Y)$ and $\operatorname{Cov}(X, Y + Z) = \operatorname{Cov}(X, Y) + \operatorname{Cov}(X, Z)$;
6. $\operatorname{Var}(X_1 + X_2) = \operatorname{Var}(X_1) + \operatorname{Var}(X_2) + 2\operatorname{Cov}(X_1, X_2)$.

All of these follow from the linearity of expectation. For item 6, for example,

$$
\operatorname{Var}(X_1 + X_2) = \mathbb{E}[(X_1 - \mathbb{E}X_1) + (X_2 - \mathbb{E}X_2)]^2 = \operatorname{Var}(X_1) + \operatorname{Var}(X_2) + 2\mathbb{E}[(X_1 - \mathbb{E}X_1)(X_2 - \mathbb{E}X_2)].
$$
More generally, bilinearity gives

$$
\operatorname{Var}\Big(\sum_{i=1}^n X_i\Big) = \sum_{i=1}^n\operatorname{Var}(X_i) + 2\sum_{1 \le i < j \le n}\operatorname{Cov}(X_i, X_j), \qquad \operatorname{Cov}\Big(\sum_i a_iX_i, \sum_j b_jY_j\Big) = \sum_{i,j}a_ib_j\operatorname{Cov}(X_i, Y_j).
$$
Hence the variance of a sum of pairwise uncorrelated random variables is the sum of their variances (item 4 of Theorem 8.3.1 needs only this assumption). The risk $w^2\operatorname{Var}(X) + (1 - w)^2\operatorname{Var}(Y) + 2w(1 - w)\operatorname{Cov}(X, Y)$ of the portfolio $wX + (1 - w)Y$ decreases as the covariance decreases: combining negatively correlated assets diversifies risk.

![Variance of a portfolio of two assets with unit variance, held in proportions w and 1 - w, as a function of w and the correlation coefficient rho](./plots/portfolio-variance.py)

### 10.1.2. Examples

**Example 10.1.1** Let $(X_1, \dots, X_k) \sim \mathrm{Mult}(n, \boldsymbol{p})$ with $\boldsymbol{p} = (p_1, \dots, p_k)^{\mathsf T}$ and $\sum_{i=1}^k p_i = 1$. Find $\operatorname{Cov}(X_i, X_j)$.

**Solution** For $i = j$, Property 6.2.1 gives $X_i \sim \mathrm{Bin}(n, p_i)$, so $\operatorname{Cov}(X_i, X_i) = \operatorname{Var}(X_i) = np_i(1 - p_i)$.

For $i \ne j$, decompose into indicators: let $I_t$ and $J_t$ be the indicators that $A_i$ and $A_j$ occur in the $t$-th trial, so that $X_i = \sum_{t=1}^n I_t$ and $X_j = \sum_{s=1}^n J_s$. Different trials are independent, so $\operatorname{Cov}(I_t, J_s) = 0$ for $t \ne s$; within one trial $A_i$ and $A_j$ are mutually exclusive, so $I_tJ_t = 0$ and $\operatorname{Cov}(I_t, J_t) = 0 - p_ip_j$. By bilinearity,

$$
\operatorname{Cov}(X_i, X_j) = \sum_{t=1}^n\operatorname{Cov}(I_t, J_t) = -np_ip_j.
$$
The negative sign agrees with intuition: the total number of trials is fixed at $n$, so more outcomes of one type tend to mean fewer of another.

**Example 10.1.2** Roll $n$ fair dice independently and let $X$ and $Y$ be the numbers of dice showing 1 and 2. By Example 10.1.1 (with $p_1 = p_2 = \frac{1}{6}$), $\operatorname{Var}(X) = \operatorname{Var}(Y) = \frac{5n}{36}$ and $\operatorname{Cov}(X, Y) = -\frac{n}{36}$. When computing directly, note that the two indicators $X_k$ and $Y_k$ of the same die are not independent: $X_kY_k = 0$ and $\operatorname{Cov}(X_k, Y_k) = -\frac{1}{36} \ne 0$. Only indicators of different dice are independent.

**Example 10.1.3 (Variance of the Hypergeometric Distribution)** In Example 8.2.5, $X = \sum_{k=1}^n X_k \sim \mathrm{H}(n, M, N)$ with $X_k \sim \mathrm{Ber}(M/N)$. For $j \ne k$, $\mathbb{P}(X_j = X_k = 1) = \frac{M(M - 1)}{N(N - 1)}$, so

$$
\operatorname{Cov}(X_j, X_k) = \frac{M(M - 1)}{N(N - 1)} - \frac{M^2}{N^2} = -\frac{M(N - M)}{N^2(N - 1)},
$$
and therefore

$$
\operatorname{Var}(X) = n\frac{M}{N}\Big(1 - \frac{M}{N}\Big) - n(n - 1)\frac{M(N - M)}{N^2(N - 1)} = n\frac{M}{N}\Big(1 - \frac{M}{N}\Big)\frac{N - n}{N - 1}.
$$
The factor $\frac{N - n}{N - 1}$ is the correction to the variance for sampling without replacement relative to sampling with replacement (the binomial distribution).

## 10.2. The Correlation Coefficient

Covariance depends on units. If $\operatorname{Var}(Z) = \operatorname{Var}(W) = 1$ and $\operatorname{Cov}(Z, W) = 0.42$, then $X = 10Z$ and $Y = 10W$ have covariance $42$, although the strength of the relationship between $X$ and $Y$ is unchanged. To obtain a comparable measure, we standardize $X$ and $Y$ before taking the covariance:

$$
\operatorname{Cov}\Big(\frac{X - \mathbb{E}X}{\sqrt{\operatorname{Var}(X)}}, \frac{Y - \mathbb{E}Y}{\sqrt{\operatorname{Var}(Y)}}\Big) = \frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X)}\sqrt{\operatorname{Var}(Y)}}.
$$

**Definition 10.2.1 (Correlation Coefficient)** If $0 < \operatorname{Var}(X)\operatorname{Var}(Y) < \infty$, the quantity

$$
\operatorname{Corr}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X)}\sqrt{\operatorname{Var}(Y)}}
$$
is called the **correlation coefficient** (Pearson correlation coefficient) of $X$ and $Y$, also written $\rho_{XY}$.

By definition, $\operatorname{Corr}(aX + b, cY + d) = \operatorname{sgn}(ac)\operatorname{Corr}(X, Y)$ for $ac \ne 0$: the correlation coefficient is unaffected by shifts and positive rescalings, which makes it comparable across settings. In the example above, $\operatorname{Corr}(X, Y) = \operatorname{Corr}(Z, W) = 0.42$.

**Example 10.2.1** If $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$, then $\operatorname{Corr}(X, Y) = \rho$.

**Solution** Since the correlation coefficient is unaffected by shifts and rescalings, we may assume $(X, Y) \sim \mathcal{N}(0, 0, 1, 1, \rho)$, so that $\mathbb{E}X = \mathbb{E}Y = 0$ and $\operatorname{Var}(X) = \operatorname{Var}(Y) = 1$. By Example 6.5.2, $\mathbb{E}(X \mid Y) = \rho Y$, so by the law of iterated expectations and property 3 of Theorem 9.3.2,

$$
\operatorname{Cov}(X, Y) = \mathbb{E}(XY) = \mathbb{E}[Y\,\mathbb{E}(X \mid Y)] = \rho\,\mathbb{E}Y^2 = \rho,
$$
and hence $\operatorname{Corr}(X, Y) = \rho$. (One can also compute the integral $\int\!\!\int xy f(x, y)\,\mathrm{d}x\,\mathrm{d}y$ directly.) This explains why the fifth parameter of the bivariate normal distribution is denoted $\rho$.

**Theorem 10.2.1** Let $\operatorname{Corr}(X, Y)$ be the correlation coefficient of $X$ and $Y$. Then

1. $\lvert\operatorname{Corr}(X, Y)\rvert \le 1$;
2. $\lvert\operatorname{Corr}(X, Y)\rvert = 1$ if and only if there are constants $a, b, c$, with $a, b$ not both zero, such that $aX + bY = c$ a.s.; in this case $X$ and $Y$ are said to be linearly related.

**Proof** Write $\tilde X = X - \mathbb{E}X$ and $\tilde Y = Y - \mathbb{E}Y$. By the Cauchy–Schwarz inequality (Theorem 8.5.2),

$$
\lvert\operatorname{Cov}(X, Y)\rvert = \lvert\mathbb{E}(\tilde X\tilde Y)\rvert \le \sqrt{\mathbb{E}\tilde X^2\,\mathbb{E}\tilde Y^2} = \sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)},
$$
which is item 1. Equality holds if and only if there are $a, b$, not both zero, with $a\tilde X + b\tilde Y = 0$ a.s., that is, $aX + bY = a\mathbb{E}X + b\mathbb{E}Y =: c$ a.s. $\square$

When $\operatorname{Corr}(X, Y) = 1$, $Y$ is an increasing linear function $Y = \alpha + \beta X$ of $X$ ($\beta > 0$); when it equals $-1$, $\beta < 0$. The closer $\lvert\operatorname{Corr}\rvert$ is to 1, the more tightly the scatter concentrates around a straight line.

![Scatter plots for various correlation coefficients; in the last two panels X and Y have a clear nonlinear relationship, yet the correlation coefficient is close to 0](./plots/correlation-scatter.py)

## 10.3. Uncorrelatedness and Independence

**Theorem 10.3.1** If $X$ and $Y$ are independent with finite variances, then they are uncorrelated, that is, $\operatorname{Cov}(X, Y) = 0$.

**Proof** By independence and item 5 of Theorem 8.2.2, $\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}X)(Y - \mathbb{E}Y)] = \mathbb{E}(X - \mathbb{E}X)\cdot\mathbb{E}(Y - \mathbb{E}Y) = 0$. $\square$

The converse fails: uncorrelated random variables need not be independent.

**Example 10.3.1** Let $(X, Y)$ be uniformly distributed on the unit disk $D = \{x^2 + y^2 \le 1\}$. Then $X$ and $Y$ are uncorrelated but not independent.

**Solution** By Example 8.2.3, $\mathbb{E}X = \mathbb{E}Y = 0$. The integrand $xy$ is odd in $x$, so

$$
\operatorname{Cov}(X, Y) = \int_{\mathbb{R}^2} xy\cdot\frac{1}{\pi}\boldsymbol{1}_D(x, y)\,\mathrm{d}x\,\mathrm{d}y = \frac{1}{\pi}\int_{-1}^1 y\Big(\int_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}} x\,\mathrm{d}x\Big)\mathrm{d}y = 0.
$$
By Remark 6.3.1, however, $X$ and $Y$ are not independent: for example, $\mathbb{P}(X > 0.8, Y > 0.8) = 0 \ne \mathbb{P}(X > 0.8)\mathbb{P}(Y > 0.8)$.

As another example, let $X \sim \mathcal{N}(0, 1)$ and $Y = X^2$. Then $\operatorname{Cov}(X, Y) = \mathbb{E}X^3 = 0$, although $Y$ is completely determined by $X$. The Pearson correlation coefficient measures only linear association; nonlinear association requires other tools, such as Spearman's rank correlation coefficient or mutual information.

The normal distribution is an important exception.

**Example 10.3.2** Let $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$. Then $X$ and $Y$ are independent if and only if they are uncorrelated. Indeed, by Example 10.2.1 uncorrelatedness means $\rho = 0$, and by Theorem 6.4.1, $\rho = 0$ if and only if $X$ and $Y$ are independent. Note that the hypothesis is that $(X, Y)$ is jointly bivariate normal; it is not enough that $X$ and $Y$ are each normally distributed.

**Example 10.3.3** Let $(X, Y)$ have a bivariate normal distribution and suppose that $\mathbb{E}(X \mid Y) = \mu$ is a constant. Then $X$ and $Y$ are independent.

**Proof** By the law of iterated expectations, $\mathbb{E}X = \mathbb{E}[\mathbb{E}(X \mid Y)] = \mu$. By property 3 of Theorem 9.3.2,

$$
\mathbb{E}[(X - \mu)Y] = \mathbb{E}\big[Y\,\mathbb{E}(X - \mu \mid Y)\big] = \mathbb{E}[Y(\mu - \mu)] = 0,
$$
so $\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mu)Y] - \mathbb{E}(X - \mu)\,\mathbb{E}Y = 0$. Thus $X$ and $Y$ are uncorrelated, and Example 10.3.2 gives independence. $\square$

The first half of the proof holds for any $(X, Y)$ with finite variances: a constant $\mathbb{E}(X \mid Y)$ implies uncorrelatedness. For general distributions it does not imply independence: in Example 10.3.1, symmetry gives $\mathbb{E}(X \mid Y) = 0$, yet $X$ and $Y$ are dependent. The three conditions are ordered by strength as

$$
X, Y \text{ independent} \ \Longrightarrow\ \mathbb{E}(X \mid Y) = \mathbb{E}X \ \Longrightarrow\ X, Y \text{ uncorrelated},
$$
neither converse holds in general, and under the bivariate normal distribution all three are equivalent.

## 10.4. Geometry of the Correlation Coefficient and the Best Linear Predictor

### 10.4.1. Cosine of an Angle

Regard the centered random variables $\tilde X = X - \mathbb{E}X$ and $\tilde Y = Y - \mathbb{E}Y$ as vectors with **inner product** $\langle\tilde X, \tilde Y\rangle = \mathbb{E}(\tilde X\tilde Y)$. The length $\|\tilde X\| = \sqrt{\mathbb{E}\tilde X^2}$ is then the standard deviation, and

$$
\operatorname{Corr}(X, Y) = \frac{\langle\tilde X, \tilde Y\rangle}{\|\tilde X\|\,\|\tilde Y\|} = \cos\varphi,
$$
where $\varphi$ is the angle between $\tilde X$ and $\tilde Y$. Thus $\lvert\operatorname{Corr}\rvert \le 1$ is the statement $\lvert\cos\varphi\rvert \le 1$, $\lvert\operatorname{Corr}\rvert = 1$ means that the two vectors are collinear, and uncorrelated means orthogonal.

### 10.4.2. The Best Linear Predictor

[3.1.8](/3.1.8) and [3.1.9](/3.1.9) found the best constant predictor $\mathbb{E}Y$ and the best predictor $\mathbb{E}(Y \mid X)$ in the mean-square sense. If only linear functions of $X$ may be used to predict $Y$, the optimal coefficients are determined by the covariance and the correlation coefficient.

**Theorem 10.4.1 (Best Linear Predictor)** Let $X, Y$ have finite variances with $\operatorname{Var}(X) > 0$. Then $\mathbb{E}[Y - (a + bX)]^2$ is minimized at

$$
b^* = \frac{\operatorname{Cov}(X, Y)}{\operatorname{Var}(X)} = \rho_{XY}\frac{\sigma_Y}{\sigma_X}, \qquad a^* = \mathbb{E}Y - b^*\mathbb{E}X,
$$
and the minimum value is $\operatorname{Var}(Y)(1 - \rho_{XY}^2)$. The random variable $\hat Y = a^* + b^*X = \mathbb{E}Y + \rho_{XY}\frac{\sigma_Y}{\sigma_X}(X - \mathbb{E}X)$ is called the best linear predictor of $Y$ from $X$.

**Proof** With $\tilde X, \tilde Y$ as above and $c = a + b\mathbb{E}X - \mathbb{E}Y$, we have $Y - (a + bX) = (\tilde Y - b\tilde X) - c$, so by Theorem 8.2.4,

$$
\mathbb{E}[Y - (a + bX)]^2 = \mathbb{E}(\tilde Y - b\tilde X)^2 + c^2 = \operatorname{Var}(Y) - 2b\operatorname{Cov}(X, Y) + b^2\operatorname{Var}(X) + c^2.
$$
Completing the square in $b$ shows that the minimum is attained at $b = b^*$, $c = 0$, with value $\operatorname{Var}(Y) - \frac{\operatorname{Cov}(X, Y)^2}{\operatorname{Var}(X)} = \operatorname{Var}(Y)(1 - \rho_{XY}^2)$. $\square$

Geometrically, $b^*\tilde X$ is the projection of $\tilde Y$ onto the direction of $\tilde X$, and the residual $\tilde Y - b^*\tilde X$ is orthogonal to $\tilde X$. The quantity $\rho_{XY}^2$ is the proportion of variance explained by linear prediction: for $\rho = 0$ linear prediction is useless, and for $\lvert\rho\rvert = 1$ it is exact. The three kinds of prediction compare as follows:

| Class of predictors | Best predictor | Interpretation |
|---|---|---|
| Constants $c$ | $\mathbb{E}Y = \operatorname*{argmin}_c\mathbb{E}(Y - c)^2$ | Center of mass |
| Linear functions $a + bX$ | $\mathbb{E}Y + \rho_{XY}\frac{\sigma_Y}{\sigma_X}(X - \mathbb{E}X)$ | Projection onto the span of $\{1, X\}$ |
| Arbitrary functions $g(X)$ | $\mathbb{E}(Y \mid X) = \operatorname*{argmin}_g\mathbb{E}[Y - g(X)]^2$ | Projection onto the space of functions of $X$ |

By Example 9.3.7 the last two coincide under the bivariate normal distribution; in general the mean squared error of the best linear predictor is at least that of $\mathbb{E}(Y \mid X)$. This is the population version of linear regression in statistics.

### 10.4.3. Correlation and Causation

Correlation does not imply causation. A rooster's crowing is highly correlated with sunrise, yet the sun rises whether or not the rooster crows; the signals of two brain regions may be correlated because a third region drives both, not because one influences the other. The correlation coefficient summarizes how two variables vary together, and it must be interpreted within its limits: it reflects only linear association and says nothing about the direction of influence. On the other hand, under suitable model assumptions the correlation structure can help uncover causal relations; for example, under a multivariate normal assumption, directed dependencies between variables can be inferred from the covariance matrix (learning gene regulatory networks is one instance). The systematic theory belongs to causal inference ([3.9](/3.9)).

## 10.5. Expectation and Covariance Matrix of a Random Vector

### 10.5.1. Expectation of Random Vectors and Random Matrices

Vectors are written as column vectors from now on. Let $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ be a random vector. If every $\mu_i = \mathbb{E}X_i$ exists, we say that the expectation of $\boldsymbol{X}$ exists and define

$$
\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X} = (\mathbb{E}X_1, \dots, \mathbb{E}X_n)^{\mathsf T}.
$$
Similarly, the expectation of a matrix $Y = (Y_{ij})_{m \times n}$ whose entries are random variables (a random matrix) is defined entrywise: $\mathbb{E}Y = (\mathbb{E}Y_{ij})_{m \times n}$.

Linearity of expectation readily gives, for a constant vector $\boldsymbol{a} \in \mathbb{R}^n$ and constant matrices $A_{k \times m}$, $B_{n \times j}$,

$$
\mathbb{E}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{a}^{\mathsf T}\mathbb{E}\boldsymbol{X}, \qquad \mathbb{E}(Y^{\mathsf T}) = (\mathbb{E}Y)^{\mathsf T}, \qquad \mathbb{E}(AYB) = A(\mathbb{E}Y)B.
$$

### 10.5.2. The Covariance Matrix

**Definition 10.5.1 (Covariance Matrix)** Let every component of the random vector $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ have finite variance and let $\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X}$. The matrix

$$
\Sigma = \operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}] = (\sigma_{ij})_{n \times n}, \qquad \sigma_{ij} = \operatorname{Cov}(X_i, X_j)
$$
is called the **covariance matrix** of $\boldsymbol{X}$.

A covariance matrix is symmetric, and its diagonal entries are the variances of the components. If $\det\Sigma = 0$, $\Sigma$ is called degenerate. For instance, the covariance matrix of the bivariate normal distribution $\mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$ is exactly the matrix $\Sigma$ of §6.4, and its mean vector is $\boldsymbol{\mu}$: the bivariate normal density is completely determined by the mean vector and the covariance matrix.

**Theorem 10.5.1** Let $\Sigma$ be the covariance matrix of $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$. Then

1. $\Sigma$ is a **positive semidefinite matrix**;
2. $\Sigma$ is degenerate if and only if there are constants $a_1, \dots, a_n$, not all zero, such that $\sum_{i=1}^n a_i(X_i - \mathbb{E}X_i) = 0$ a.s.

**Proof** For every $\boldsymbol{a} = (a_1, \dots, a_n)^{\mathsf T} \in \mathbb{R}^n$,

$$
\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} = \sum_{i=1}^n\sum_{j=1}^n a_ia_j\,\mathbb{E}[(X_i - \mathbb{E}X_i)(X_j - \mathbb{E}X_j)] = \mathbb{E}\Big[\sum_{i=1}^n a_i(X_i - \mathbb{E}X_i)\Big]^2 = \operatorname{Var}\Big(\sum_{i=1}^n a_iX_i\Big) \ge 0,
$$
so $\Sigma$ is positive semidefinite. A positive semidefinite matrix is degenerate if and only if $\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} = 0$ for some nonzero vector $\boldsymbol{a}$, that is, $\operatorname{Var}\big(\sum_i a_iX_i\big) = 0$, which by item 3 of Theorem 8.3.1 is equivalent to $\sum_i a_i(X_i - \mathbb{E}X_i) = 0$ a.s. $\square$

A degenerate covariance matrix therefore means that the random vector lies almost surely in a lower-dimensional hyperplane, so that some component is a linear combination of the others. The identity in the proof also gives the transformation rule of covariance matrices under linear maps: for a constant matrix $A_{k \times n}$ and a constant vector $\boldsymbol{b}$,

$$
\operatorname{Cov}(A\boldsymbol{X} + \boldsymbol{b}) = \mathbb{E}[A(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}A^{\mathsf T}] = A\Sigma A^{\mathsf T}.
$$
This formula is used over and over for the multivariate normal distribution ([3.1.15](/3.1.15)).

**Example 10.5.1** Let $\boldsymbol{X} = (X_1, \dots, X_k)^{\mathsf T} \sim \mathrm{Mult}(n, \boldsymbol{p})$. By Example 10.1.1,

$$
\Sigma = n\big(\operatorname{diag}(p_1, \dots, p_k) - \boldsymbol{p}\boldsymbol{p}^{\mathsf T}\big).
$$
Since $X_1 + \cdots + X_k = n$ is constant, taking $\boldsymbol{a} = \boldsymbol{1}$ gives $\sum_i(X_i - \mathbb{E}X_i) = 0$, so $\Sigma$ is degenerate by Theorem 10.5.1. Directly: $\Sigma\boldsymbol{1} = n(\boldsymbol{p} - \boldsymbol{p}(\boldsymbol{p}^{\mathsf T}\boldsymbol{1})) = \boldsymbol{0}$.

## Summary

- Covariance $\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}X)(Y - \mathbb{E}Y)] = \mathbb{E}(XY) - \mathbb{E}X\,\mathbb{E}Y$ is bilinear and symmetric; $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X, Y)$.
- The correlation coefficient $\operatorname{Corr}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sigma_X\sigma_Y} \in [-1, 1]$ is unaffected by shifts and rescalings; $\lvert\operatorname{Corr}\rvert = 1$ if and only if $X$ and $Y$ are almost surely linearly related; geometrically it is the cosine of the angle between the centered variables.
- Independence $\Rightarrow$ constant $\mathbb{E}(X \mid Y)$ $\Rightarrow$ uncorrelatedness, and the converses fail in general; under the bivariate normal distribution the three are equivalent.
- The best linear predictor is $\mathbb{E}Y + \rho\frac{\sigma_Y}{\sigma_X}(X - \mathbb{E}X)$, with mean squared error $\sigma_Y^2(1 - \rho^2)$.
- The covariance matrix $\Sigma = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}]$ is symmetric and positive semidefinite, $\operatorname{Cov}(A\boldsymbol{X} + \boldsymbol{b}) = A\Sigma A^{\mathsf T}$, and it is degenerate if and only if the components satisfy a linear relation almost surely.
- Techniques: write counts as sums of indicators and compute covariances by bilinearity (multinomial and hypergeometric distributions); use symmetry; when the high-dimensional case is unclear, start from the two-dimensional one.
