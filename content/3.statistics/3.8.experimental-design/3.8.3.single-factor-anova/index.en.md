---
title: "Single-Factor Experiments: Analysis of Variance"
description: The completely randomized single-factor experiment and its analysis of variance; means and effects models, the partition of sums of squares, expected mean squares, the F-test and the ANOVA table; the geometry of the decomposition and Cochran's theorem; ANOVA as a regression, a general linear test and a likelihood ratio test.
---

A simple comparative experiment compares two treatments; most experiments compare more. When one factor is varied over $a$ levels and every other condition is held fixed or randomized, the natural question "do the levels differ in mean response?" is answered by the **analysis of variance**. With $a = 2$ levels the ANOVA $F$-test is exactly the pooled **two-sample t-test** of [3.8.2](/3.8.2) ($F = t^2$), so the method is its generalization to several groups. The regression course already treated one-way ANOVA from the modeling side ([3.3.12](/3.3.12), [3.3.13](/3.3.13)); this chapter develops it from the side of the experiment: how the data are collected (the completely randomized design), what each entry of the ANOVA table means and why it is computed the way it is, the geometry behind the degrees of freedom, and why the ANOVA $F$-test, the general linear test and the likelihood ratio test are one and the same test. The step that follows a significant $F$-test, deciding which levels differ, is the subject of [3.8.4](/3.8.4); checking the assumptions, planning the sample size and treating the levels as random come in [3.8.5](/3.8.5).

Notation. A factor has $a$ levels with $n_i$ observations at level $i$ ($n_i = n$ in a balanced experiment) and $N = \sum_i n_i$ observations in total. A dot replaces an index that has been summed over and a bar denotes an average: $y_{i\cdot} = \sum_j y_{ij}$, $\bar y_{i\cdot} = y_{i\cdot}/n_i$, $y_{\cdot\cdot} = \sum_{i,j} y_{ij}$, $\bar y_{\cdot\cdot} = y_{\cdot\cdot}/N$. In models and theorems the observations are random variables and are written $Y_{ij}$; in data and worked examples they are written $y_{ij}$ (much of the experimental design literature writes lowercase for both). Sums of squares and mean squares carry upright subscripts, $\mathrm{SS}_{\mathrm{T}}$, $\mathrm{SS}_{\mathrm{Tr}}$, $\mathrm{SS}_{\mathrm{E}}$, $\mathrm{MS}_{\mathrm{Tr}}$, $\mathrm{MS}_{\mathrm{E}}$; they correspond to the SSTO, SSTR, SSE, MSTR and MSE of [3.3.12](/3.3.12).

## 3.1. Single-Factor Experiments and the Completely Randomized Design

An engineer studies a single-wafer plasma etching tool. The etch rate depends on the radio-frequency (RF) power applied to the chamber, and she wants to know whether the four power settings of interest, $160$, $180$, $200$ and $220\,\mathrm{W}$, give different mean etch rates; she suspects that higher power gives a higher rate. Five wafers are etched at each setting, and the $20$ runs are made in random order. The response is recorded in $\mathrm{\mathring{A}}/\mathrm{min}$ (one ångström is $0.1\,\mathrm{nm}$).

| RF power / W | Observations | $y_{i\cdot}$ | $\bar y_{i\cdot}$ | $s_i$ |
|---|---|---|---|---|
| 160 | 575, 542, 530, 539, 570 | 2756 | 551.2 | 20.02 |
| 180 | 565, 593, 590, 579, 610 | 2937 | 587.4 | 16.74 |
| 200 | 600, 651, 610, 637, 629 | 3127 | 625.4 | 20.53 |
| 220 | 725, 700, 715, 685, 710 | 3535 | 707.0 | 15.25 |
| | | $y_{\cdot\cdot} = 12355$ | $\bar y_{\cdot\cdot} = 617.75$ | |

The data are entered in R as a data frame whose explanatory variable is a factor:

```r
y <- c(575, 542, 530, 539, 570,
       565, 593, 590, 579, 610,
       600, 651, 610, 637, 629,
       725, 700, 715, 685, 710)
X <- rep(c(160, 180, 200, 220), each = 5)
etch.rate <- data.frame(RF = as.factor(X), rate = y)
```

![Etch rate against RF power: the individual wafers (points), the level means (diamonds) and the grand mean (dashed line), with box plots of the four groups.](./plots/etch-data.py)

The plot suggests two questions, which organize this chapter and the next: (1) do the four power levels have equal mean etch rate? (2) if not, which pairs of levels differ?

In this experiment RF power is the only **factor**, its four settings are the **factor levels** (treatments), each wafer is an experimental unit, and the order of the $20$ runs was chosen at random. This is the simplest experimental design.

**Definition 3.1.1 (Completely Randomized Design)** In a **completely randomized design** (CRD) the $N$ experimental units are assigned to the $a$ treatments completely at random, $n_i$ units to treatment $i$, so that every assignment with these group sizes is equally likely; when the runs are made in sequence, the run order is also random.

Randomization makes the groups comparable: unknown sources of variation (a drifting chamber, a change of operator) are spread over the treatments instead of being confounded with them, and it justifies treating the errors as independent. The CRD contains no restriction on randomization; designs that randomize within blocks follow in later chapters. Here the four levels are the only power settings of interest and the conclusions are about these four levels: the factor is fixed. If the levels were a random sample from a larger population of levels, the inference would be about that population; that random effects model is the subject of [3.8.5](/3.8.5).

The experiment is balanced, $n_1 = \cdots = n_a$. As shown for two groups in [3.8.2](/3.8.2), a **balanced design** maximizes the power of the comparison for a fixed total number of runs and makes the test less sensitive to unequal variances; for several groups it also makes the sums of squares of the ANOVA decomposition orthogonal and easy to compute. All formulas below are nevertheless written for general $n_i$.

## 3.2. Models

### 3.2.1. Means Model and Effects Model

There are two equivalent ways to write a model for the data. The **cell means model** (means model) is

$$
Y_{ij} = \mu_i + \varepsilon_{ij},\qquad \varepsilon_{ij} \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2),\qquad i = 1, \dots, a,\quad j = 1, \dots, n_i,
$$
where $\mu_i$ is the mean response at level $i$. The **factor effects model** (effects model) writes each mean as an overall mean plus a deviation,

$$
Y_{ij} = \mu + \tau_i + \varepsilon_{ij},\qquad \sum_{i=1}^a \tau_i = 0,
$$
where $\mu$ is the overall mean, $\tau_i = \mu_i - \mu$ is the **treatment effect** of level $i$, and $\varepsilon_{ij}$ is the random experimental error. The two models describe the same distributions; the effects model has one parameter more than there are means, and the constraint removes that redundancy (other constraints are possible, see [3.3.13](/3.3.13)). With the constraint $\sum_i\tau_i = 0$, $\mu = \frac1a\sum_i\mu_i$; for unbalanced data the weighted constraint $\sum_i n_i\tau_i = 0$ is often more convenient, and then $\mu = \sum_i n_i\mu_i/N$. Both models assume that the observations are independent, normal and of common variance $\sigma^2$.

The hypothesis of equal treatment means takes two equivalent forms:

$$
H_0\colon \mu_1 = \mu_2 = \cdots = \mu_a \quad\text{versus}\quad H_1\colon \mu_i \ne \mu_j \text{ for at least one pair } (i, j),
$$

$$
H_0\colon \tau_1 = \tau_2 = \cdots = \tau_a = 0 \quad\text{versus}\quad H_1\colon \tau_i \ne 0 \text{ for at least one } i.
$$

### 3.2.2. The Models as Regressions

Order the observations by level. Both models are linear regressions $\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ with $\boldsymbol{\varepsilon} \sim \mathcal{N}_N(\boldsymbol{0}, \sigma^2 I_N)$; they differ in the **design matrix**. For the means model $\boldsymbol{\beta} = (\mu_1, \dots, \mu_a)^{\mathsf T}$ and $X$ consists of $a$ indicator columns:

$$
X = \begin{bmatrix} \boldsymbol{1}_{n_1} & \boldsymbol{0} & \cdots & \boldsymbol{0} \\ \boldsymbol{0} & \boldsymbol{1}_{n_2} & \cdots & \boldsymbol{0} \\ \vdots & & \ddots & \vdots \\ \boldsymbol{0} & \boldsymbol{0} & \cdots & \boldsymbol{1}_{n_a} \end{bmatrix}.
$$
For the effects model with $\sum_i\tau_i = 0$, the last effect is $\tau_a = -\tau_1 - \cdots - \tau_{a-1}$, so $\boldsymbol{\beta} = (\mu, \tau_1, \dots, \tau_{a-1})^{\mathsf T}$, the first column of $X$ is $\boldsymbol{1}_N$, and the rows of level $a$ have $-1$ in every $\tau$ column:

$$
X = \begin{bmatrix} \boldsymbol{1}_{n_1} & \boldsymbol{1}_{n_1} & \boldsymbol{0} & \cdots & \boldsymbol{0} \\ \boldsymbol{1}_{n_2} & \boldsymbol{0} & \boldsymbol{1}_{n_2} & \cdots & \boldsymbol{0} \\ \vdots & & & \ddots & \vdots \\ \boldsymbol{1}_{n_{a-1}} & \boldsymbol{0} & \boldsymbol{0} & \cdots & \boldsymbol{1}_{n_{a-1}} \\ \boldsymbol{1}_{n_a} & -\boldsymbol{1}_{n_a} & -\boldsymbol{1}_{n_a} & \cdots & -\boldsymbol{1}_{n_a} \end{bmatrix}.
$$

R uses neither of these by default. For a factor it uses treatment contrasts: an intercept column and indicators of levels $2, \dots, a$, which corresponds to the constraint $\tau_1 = 0$. The intercept is then the mean of the first level and each coefficient is the difference between a level mean and the first level mean.

```r
fit1 <- lm(rate ~ RF, data = etch.rate)
model.matrix(fit1)
```

```text
   (Intercept) RF180 RF200 RF220
1            1     0     0     0
...
5            1     0     0     0
6            1     1     0     0
...
11           1     0     1     0
...
16           1     0     0     1
...
20           1     0     0     1
```

The formula `rate ~ 0 + RF` removes the intercept and gives the means model, with coefficients `RF160`, …, `RF220` equal to the four level means. All three parametrizations have the same column space, hence the same fitted values, residuals and ANOVA table.

### 3.2.3. Estimation

**Proposition 3.2.1** In the means model, the least squares estimators of $\mu_1, \dots, \mu_a$ are $\hat\mu_i = \bar Y_{i\cdot}$. In the effects model with $\sum_i\tau_i = 0$ and equal $n_i$, $\hat\mu = \bar Y_{\cdot\cdot}$ and $\hat\tau_i = \bar Y_{i\cdot} - \bar Y_{\cdot\cdot}$. In both cases the fitted value of $Y_{ij}$ is $\bar Y_{i\cdot}$ and the residual is $e_{ij} = Y_{ij} - \bar Y_{i\cdot}$.

**Proof** The least squares criterion separates over the groups:

$$
Q(\mu_1, \dots, \mu_a) = \sum_{i=1}^a\sum_{j=1}^{n_i}(Y_{ij} - \mu_i)^2 = \sum_{i=1}^a Q_i(\mu_i),\qquad Q_i(\mu_i) = \sum_{j=1}^{n_i}(Y_{ij} - \mu_i)^2.
$$
Each $Q_i$ depends on $\mu_i$ alone, and $Q_i(\mu_i) = \sum_j(Y_{ij} - \bar Y_{i\cdot})^2 + n_i(\bar Y_{i\cdot} - \mu_i)^2$ is minimized at $\mu_i = \bar Y_{i\cdot}$. The effects model is a reparametrization, $\mu = \frac1a\sum_i\mu_i$, $\tau_i = \mu_i - \mu$, so its estimators are the same functions of the $\hat\mu_i$; with equal $n_i$, $\frac1a\sum_i\bar Y_{i\cdot} = \bar Y_{\cdot\cdot}$. $\square$

The error variance is estimated by pooling the within-group variation,

$$
\hat\sigma^2 = \mathrm{MS}_{\mathrm{E}} = \frac{\sum_i\sum_j(Y_{ij} - \bar Y_{i\cdot})^2}{N - a} = \frac{\sum_i(n_i - 1)s_i^2}{N - a},
$$
the **pooled variance** of the $a$ groups; it is unbiased (Theorem 3.3.1). Since $\bar Y_{i\cdot} \sim \mathcal{N}(\mu_i, \sigma^2/n_i)$ independently of $\mathrm{MS}_{\mathrm{E}}$, and $(N - a)\mathrm{MS}_{\mathrm{E}}/\sigma^2 \sim \chi^2_{N-a}$, the $100(1 - \alpha)\%$ **confidence interval** for a level mean and for a difference of two level means are

$$
\bar y_{i\cdot} \pm t_{N-a,\alpha/2}\sqrt{\frac{\mathrm{MS}_{\mathrm{E}}}{n_i}},\qquad \bar y_{i\cdot} - \bar y_{j\cdot} \pm t_{N-a,\alpha/2}\sqrt{\mathrm{MS}_{\mathrm{E}}\Bigl(\frac{1}{n_i} + \frac{1}{n_j}\Bigr)}.
$$
The variance estimate uses all $N$ observations, so the intervals use $N - a$ degrees of freedom rather than the $n_i - 1$ of one group. For the etching data, $\mathrm{MS}_{\mathrm{E}} = 333.7$ (computed below), $\sqrt{333.7/5} = 8.17$ and $t_{16,0.025} = 2.120$, so the 95% interval for the mean at $220\,\mathrm{W}$ is $707.0 \pm 17.3$, and for $\mu_4 - \mu_1$ it is $155.8 \pm 24.5$. These are individual intervals; intervals that hold simultaneously for several comparisons are the subject of [3.8.4](/3.8.4).

## 3.3. The Partition of Sums of Squares and the ANOVA Table

### 3.3.1. The Partition

The name "analysis of variance" comes from partitioning the total variability of the response into components that correspond to the terms of the model. The total variability is measured by the **total sum of squares**

$$
\mathrm{SS}_{\mathrm{T}} = \sum_{i=1}^a\sum_{j=1}^{n_i}(y_{ij} - \bar y_{\cdot\cdot})^2.
$$
Writing $y_{ij} - \bar y_{\cdot\cdot} = (y_{ij} - \bar y_{i\cdot}) + (\bar y_{i\cdot} - \bar y_{\cdot\cdot})$ and squaring, the cross term $2\sum_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})\sum_j(y_{ij} - \bar y_{i\cdot})$ vanishes because the inner sum is zero. Hence

$$
\underbrace{\sum_{i=1}^a\sum_{j=1}^{n_i}(y_{ij} - \bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{T}}} = \underbrace{\sum_{i=1}^a n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{Tr}}} + \underbrace{\sum_{i=1}^a\sum_{j=1}^{n_i}(y_{ij} - \bar y_{i\cdot})^2}_{\mathrm{SS}_{\mathrm{E}}}. \tag{3.1}
$$
The **treatment sum of squares** $\mathrm{SS}_{\mathrm{Tr}}$ measures the differences between the level means, the variation between groups; the error sum of squares $\mathrm{SS}_{\mathrm{E}}$ measures the variation of the observations around their own level mean, within groups. In regression language $\mathrm{SS}_{\mathrm{Tr}} = \sum_{i,j}(\hat\mu_i - \hat{\bar\mu})^2$ is the regression sum of squares of the fitted means and $\mathrm{SS}_{\mathrm{E}}$ is what is left over. A large $\mathrm{SS}_{\mathrm{Tr}}$ relative to $\mathrm{SS}_{\mathrm{E}}$ points to differences between the treatment means.

The degrees of freedom split in the same way:

$$
N - 1 = (a - 1) + (N - a).
$$
$\mathrm{SS}_{\mathrm{T}}$ is a sum of $N$ squared deviations subject to one linear restriction ($\sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot}) = 0$); $\mathrm{SS}_{\mathrm{Tr}}$ involves $a$ level means subject to one restriction ($\sum_i n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot}) = 0$); $\mathrm{SS}_{\mathrm{E}}$ pools $a$ within-group sums, each with $n_i - 1$ degrees of freedom. Section 3.4 makes this counting precise.

For hand calculation, the sums of squares are computed from totals:

$$
\mathrm{SS}_{\mathrm{T}} = \sum_{i,j} y_{ij}^2 - \frac{y_{\cdot\cdot}^2}{N},\qquad \mathrm{SS}_{\mathrm{Tr}} = \sum_{i=1}^a \frac{y_{i\cdot}^2}{n_i} - \frac{y_{\cdot\cdot}^2}{N},\qquad \mathrm{SS}_{\mathrm{E}} = \mathrm{SS}_{\mathrm{T}} - \mathrm{SS}_{\mathrm{Tr}}.
$$

### 3.3.2. Expected Mean Squares

Sums of squares cannot be compared directly, because they are sums of different numbers of terms. Dividing each by its degrees of freedom gives the **mean squares**

$$
\mathrm{MS}_{\mathrm{Tr}} = \frac{\mathrm{SS}_{\mathrm{Tr}}}{a - 1},\qquad \mathrm{MS}_{\mathrm{E}} = \frac{\mathrm{SS}_{\mathrm{E}}}{N - a},
$$
and their expectations show what each one estimates.

**Theorem 3.3.1 (Expected Mean Squares)** In the effects model $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$ with $\sum_i n_i\tau_i = 0$ (in a balanced experiment, $\sum_i\tau_i = 0$),

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{E}}] = \sigma^2,\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}] = \sigma^2 + \frac{\sum_{i=1}^a n_i\tau_i^2}{a - 1},
$$
which for $n_i = n$ is $\sigma^2 + n\sum_i\tau_i^2/(a - 1)$.

**Proof** Write $\bar\varepsilon_{i\cdot} = \frac{1}{n_i}\sum_j\varepsilon_{ij}$ and $\bar\varepsilon_{\cdot\cdot} = \frac1N\sum_{i,j}\varepsilon_{ij}$. Then $\bar Y_{i\cdot} = \mu + \tau_i + \bar\varepsilon_{i\cdot}$ and, because $\sum_i n_i\tau_i = 0$, $\bar Y_{\cdot\cdot} = \mu + \bar\varepsilon_{\cdot\cdot}$. For the error sum of squares, $Y_{ij} - \bar Y_{i\cdot} = \varepsilon_{ij} - \bar\varepsilon_{i\cdot}$, and $\sum_j(\varepsilon_{ij} - \bar\varepsilon_{i\cdot})^2$ is $n_i - 1$ times a sample variance of $n_i$ independent $\mathcal{N}(0, \sigma^2)$ variables, so its expectation is $(n_i - 1)\sigma^2$; summing over $i$, $\mathbb{E}[\mathrm{SS}_{\mathrm{E}}] = (N - a)\sigma^2$. For the treatment sum of squares,

$$
\mathrm{SS}_{\mathrm{Tr}} = \sum_i n_i(\tau_i + \bar\varepsilon_{i\cdot} - \bar\varepsilon_{\cdot\cdot})^2 = \sum_i n_i\tau_i^2 + 2\sum_i n_i\tau_i(\bar\varepsilon_{i\cdot} - \bar\varepsilon_{\cdot\cdot}) + \sum_i n_i(\bar\varepsilon_{i\cdot} - \bar\varepsilon_{\cdot\cdot})^2.
$$
The middle term has expectation zero. In the last term, $\sum_i n_i(\bar\varepsilon_{i\cdot} - \bar\varepsilon_{\cdot\cdot})^2 = \sum_i n_i\bar\varepsilon_{i\cdot}^2 - N\bar\varepsilon_{\cdot\cdot}^2$, whose expectation is $\sum_i n_i\cdot\sigma^2/n_i - N\cdot\sigma^2/N = (a - 1)\sigma^2$. Hence $\mathbb{E}[\mathrm{SS}_{\mathrm{Tr}}] = \sum_i n_i\tau_i^2 + (a - 1)\sigma^2$; divide by $a - 1$. $\square$

$\mathrm{MS}_{\mathrm{E}}$ is an unbiased estimator of $\sigma^2$ whether or not $H_0$ holds. $\mathrm{MS}_{\mathrm{Tr}}$ is also unbiased for $\sigma^2$ under $H_0$, but under $H_1$ its expectation exceeds $\sigma^2$ by a nonnegative quantity that grows with the size of the treatment effects and with the sample sizes. The comparison of the two mean squares is therefore a test of $H_0$, and only a large ratio is evidence against $H_0$. These expected mean squares will be compared with those of the random effects model in [3.8.5](/3.8.5), where the same ratio is used to test a different hypothesis.

### 3.3.3. The F-Test and the ANOVA Table

**Theorem 3.3.2 (ANOVA F-Test)** In the normal model, $\mathrm{SS}_{\mathrm{E}}/\sigma^2 \sim \chi^2_{N-a}$. If $H_0\colon \tau_1 = \cdots = \tau_a = 0$ holds, then also $\mathrm{SS}_{\mathrm{Tr}}/\sigma^2 \sim \chi^2_{a-1}$, independent of $\mathrm{SS}_{\mathrm{E}}$, and

$$
F_0 = \frac{\mathrm{SS}_{\mathrm{Tr}}/(a - 1)}{\mathrm{SS}_{\mathrm{E}}/(N - a)} = \frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}} \sim F_{a-1,N-a}.
$$
The level-$\alpha$ test rejects $H_0$ when $F_0 > F_{a-1,N-a,\alpha}$, the upper $\alpha$ quantile of the **F-distribution**; the **p-value** is $\mathbb{P}(F_{a-1,N-a} > F_0)$.

The distributional statements follow from Cochran's theorem in Section 3.4. The test is one-sided (upper tail) even though $H_1$ is "the means are not all equal": by Theorem 3.3.1, departures from $H_0$ in any direction increase $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]$ and leave $\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]$ unchanged, so they make $F_0$ large, never small. (An unusually small $F_0$ is not evidence about the means; it may indicate that the model is wrong, for example that the runs were not independent.)

The computations are summarized in the **ANOVA table**:

| Source of variation | Sum of squares | Degrees of freedom | Mean square | $F_0$ | $p$-value |
|---|---|---|---|---|---|
| Between treatments | $\mathrm{SS}_{\mathrm{Tr}} = \sum_i n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2$ | $a - 1$ | $\mathrm{MS}_{\mathrm{Tr}} = \dfrac{\mathrm{SS}_{\mathrm{Tr}}}{a - 1}$ | $\dfrac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}$ | $\mathbb{P}(F_{a-1,N-a} > F_0)$ |
| Error (within treatments) | $\mathrm{SS}_{\mathrm{E}} = \sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2$ | $N - a$ | $\mathrm{MS}_{\mathrm{E}} = \dfrac{\mathrm{SS}_{\mathrm{E}}}{N - a}$ | | |
| Total | $\mathrm{SS}_{\mathrm{T}} = \sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2$ | $N - 1$ | | | |

Each column has a role. The sums of squares and the degrees of freedom are additive down the column (the total row is the sum of the other two), the mean squares are not. $\mathrm{MS}_{\mathrm{E}}$ is the estimate of $\sigma^2$, and its square root is the residual standard error that `lm` reports. $\mathrm{MS}_{\mathrm{Tr}}$ estimates $\sigma^2$ plus the treatment effects. $F_0$ is their ratio and is referred to the $F_{a-1,N-a}$ distribution. Because of the additivity, any two of the three sums of squares, together with $a$ and $N$, determine the whole table; that is how tables with missing entries are completed.

The ANOVA has a simple invariance. If every observation is replaced by $y'_{ij} = c\,y_{ij} + d$ with $c > 0$, the level means and the grand mean transform in the same way, so $\hat\tau'_i = c\,\hat\tau_i$, $\hat\sigma' = c\,\hat\sigma$, every sum of squares is multiplied by $c^2$, and $F_0$ is unchanged: the analysis does not depend on the location and the unit of measurement of the response. In particular, coding the data by subtracting a convenient constant before hand calculation is harmless.

### 3.3.4. Example: The Plasma Etching Experiment

From the totals in Section 3.1, $\sum y_{ij}^2 = 7{,}704{,}511$ and $y_{\cdot\cdot}^2/N = 12355^2/20 = 7{,}632{,}301.25$, so

$$
\mathrm{SS}_{\mathrm{T}} = 72{,}209.75,\qquad \mathrm{SS}_{\mathrm{Tr}} = \frac{2756^2 + 2937^2 + 3127^2 + 3535^2}{5} - 7{,}632{,}301.25 = 66{,}870.55,
$$
and $\mathrm{SS}_{\mathrm{E}} = 72{,}209.75 - 66{,}870.55 = 5339.20$. In R:

```r
etch.rate.aov <- aov(rate ~ RF, data = etch.rate)
summary(etch.rate.aov)
fit1 <- lm(rate ~ RF, data = etch.rate)
anova(fit1)               # the same table from the regression fit
```

```text
Analysis of Variance Table

Response: rate
          Df Sum Sq Mean Sq F value    Pr(>F)    
RF         3  66871 22290.2  66.797 2.883e-09 ***
Residuals 16   5339   333.7                      
```

Reading the output row by row: the factor `RF` has $a - 1 = 3$ degrees of freedom and $\mathrm{SS}_{\mathrm{Tr}} = 66871$, so $\mathrm{MS}_{\mathrm{Tr}} = 66871/3 = 22290.2$; the residual row has $N - a = 16$ degrees of freedom and $\mathrm{SS}_{\mathrm{E}} = 5339$, so $\mathrm{MS}_{\mathrm{E}} = 333.7$ and $\hat\sigma = \sqrt{333.7} = 18.27\,\mathrm{\mathring{A}/min}$. The ratio $F_0 = 22290.2/333.7 = 66.80$ is far beyond $F_{3,16,0.05} = 3.24$ and $F_{3,16,0.01} = 5.29$; $\mathbb{P}(F_{3,16} > 66.80) = 2.9\times10^{-9}$. The total row is not printed: $\mathrm{SS}_{\mathrm{T}} = 66871 + 5339 = 72210$ on $19$ degrees of freedom. We conclude that the RF power setting affects the mean etch rate. The estimated effects are $\hat\tau_i = \bar y_{i\cdot} - \bar y_{\cdot\cdot} = -66.55, -30.35, 7.65, 89.25$.

![The F(3, 16) density: the 5% rejection region lies to the right of 3.24, while the observed F0 = 66.8 is far off the scale of the density.](./plots/f-reference.py)

### 3.3.5. Between and Within: An Intuitive View

$F_0$ is proportional to the ratio

$$
\frac{\sum_i n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2}{\sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2},
$$
so the evidence for a factor effect has two ingredients. A large spread of the level means around the grand mean makes the effect more significant, and a large scatter of the observations around their own level mean makes it less significant. Two experiments whose group means differ by the same amounts can therefore reach opposite conclusions, if the observations within groups are tightly clustered in one and widely scattered in the other.

![Two simulated experiments with the same level means (five levels, ten observations each). Left: small within-group scatter, large F0. Right: the same means with six times the within-group standard deviation; the differences of the means are no longer significant.](./plots/between-within.py)

The sample sizes are the third ingredient. Side-by-side box plots show the distribution of the individual $y_{ij}$, but the test concerns the means, and the significance depends on the sampling variability of the $\bar y_{i\cdot}$, whose variance is $\sigma^2/n_i$, not on the spread of the $y_{ij}$ themselves. The weights $n_i$ in $\mathrm{SS}_{\mathrm{Tr}}$ express this: two data sets with identical box plots give a much larger $F_0$ when each box summarizes $500$ observations than when it summarizes $5$. A box plot is a description of the data, not of the precision of the means, and box plots that overlap heavily are compatible with a highly significant $F$-test.

The partition (3.1) has a probabilistic counterpart. Let $X$ be the group label of an observation chosen at random from the experiment and $Y$ its response. The **law of total variance** ([3.1.9](/3.1.9)),

$$
\operatorname{Var}(Y) = \mathbb{E}\bigl[\operatorname{Var}(Y \mid X)\bigr] + \operatorname{Var}\bigl(\mathbb{E}[Y \mid X]\bigr),
$$
splits the variance of the response into the average within-group variance and the variance of the group means. Dividing (3.1) by $N$ gives the empirical version: $\mathrm{SS}_{\mathrm{T}}/N$ is the variance of all observations, $\mathrm{SS}_{\mathrm{E}}/N$ the weighted average of the within-group variances, and $\mathrm{SS}_{\mathrm{Tr}}/N$ the weighted variance of the group means. A factor predicts $Y$ well when the second term dominates, that is, when knowing the group moves the conditional mean $\mathbb{E}[Y \mid X]$ far from the overall mean while the conditional distributions are narrow.

## 3.4. Geometry and Distribution Theory

### 3.4.1. Degrees of Freedom

The degrees of freedom of a sum of squares can be understood in several equivalent ways: as the number of quantities in it that are free to vary once the restrictions are taken into account; as the dimension of the space in which the corresponding random vector lives; or as the minimum number of independent coordinates needed to specify that vector. Fisher, who introduced the concept, arrived at it through multidimensional geometry. For a sample $x_1, \dots, x_n$, regard the observations as a point $P = (x_1, \dots, x_n)$ of $\mathbb{R}^n$ and let $M = (\bar x, \dots, \bar x) = \bar x\,\boldsymbol{1}$. Then $M$ is the orthogonal projection of $P$ onto the line through $O$ in the direction $\boldsymbol{1}$, and

$$
\lvert PM\rvert^2 = (x_1 - \bar x)^2 + \cdots + (x_n - \bar x)^2 = (n - 1)s^2.
$$
For given $\bar x$ and $s^2$, $P$ lies on a sphere of dimension $n - 1$ centered at $M$, in the hyperplane at right angles to the line $OM$: the deviation vector $P - M$ ranges over an $(n-1)$-dimensional space, and $s^2$ has $n - 1$ degrees of freedom.

Algebraically, each sum of squares in ANOVA is a **quadratic form** $Q = \boldsymbol{Y}^{\mathsf T}A\boldsymbol{Y}$ with $A$ symmetric, and its degrees of freedom are $\operatorname{rank}(A)$. In ANOVA every such $A$ is an **orthogonal projection matrix**, and for a projection matrix $\operatorname{rank}(A) = \operatorname{tr}(A)$. A more general definition, used for smoothers and penalized fits, applies to any linear fit $\hat{\boldsymbol{Y}} = C\boldsymbol{Y}$ of observations with variance $\sigma^2$:

$$
\mathrm{df} = \frac{1}{\sigma^2}\sum_{i=1}^N\operatorname{Cov}(\hat Y_i, Y_i) = \operatorname{tr}(C),
$$
which reduces to the rank when $C$ is a projection.

### 3.4.2. The Partition of Spaces

Let $\boldsymbol{y} \in \mathbb{R}^N$ be the vector of all observations. In the means model $\mathbb{E}[\boldsymbol{Y}] = X\boldsymbol{\beta}$ lies in the column space $\Omega$ of the indicator matrix $X$, the space of vectors that are constant within each group; $\dim\Omega = a$. Under $H_0$ the mean vector is $\mu\boldsymbol{1}$, which lies in $\omega = \operatorname{span}\{\boldsymbol{1}\}$, $\dim\omega = 1$. Let $P_\Omega$ and $P_\omega$ be the orthogonal projections onto these spaces ([2.1.4](/2.1.4)). Then $P_\Omega\boldsymbol{y} = \hat{\boldsymbol{y}}$ is the vector of fitted values (each entry replaced by its group mean) and $P_\omega\boldsymbol{y} = \bar y_{\cdot\cdot}\boldsymbol{1}$. The space decomposes into three mutually orthogonal subspaces,

$$
\mathbb{R}^N = \omega \oplus (\Omega \ominus \omega) \oplus \Omega^{\perp},\qquad N = 1 + (a - 1) + (N - a),
$$
where $\Omega \ominus \omega$ is the orthogonal complement of $\omega$ in $\Omega$ (the group-constant vectors whose entries sum to zero) and $\Omega^{\perp}$ is the residual space. Accordingly,

$$
\boldsymbol{y} - \bar y_{\cdot\cdot}\boldsymbol{1} = (\hat{\boldsymbol{y}} - \bar y_{\cdot\cdot}\boldsymbol{1}) + (\boldsymbol{y} - \hat{\boldsymbol{y}}),\qquad \hat{\boldsymbol{y}} - \bar y_{\cdot\cdot}\boldsymbol{1} = (P_\Omega - P_\omega)\boldsymbol{y} \in \Omega \ominus \omega,\quad \boldsymbol{y} - \hat{\boldsymbol{y}} = (I - P_\Omega)\boldsymbol{y} \in \Omega^{\perp}.
$$
The two pieces are orthogonal, and the Pythagorean theorem is the ANOVA identity (3.1):

$$
\mathrm{SS}_{\mathrm{T}} = \lVert\boldsymbol{y} - \bar y_{\cdot\cdot}\boldsymbol{1}\rVert^2,\qquad \mathrm{SS}_{\mathrm{Tr}} = \lVert(P_\Omega - P_\omega)\boldsymbol{y}\rVert^2,\qquad \mathrm{SS}_{\mathrm{E}} = \lVert(I - P_\Omega)\boldsymbol{y}\rVert^2.
$$
The projection matrices $P_\Omega - P_\omega$ and $I - P_\Omega$ have ranks (and traces) $a - 1$ and $N - a$: the degrees of freedom are the dimensions of the subspaces in which the vectors lie.

![The geometry of one-way ANOVA: the observation vector y, its projection y-hat onto the model space Omega, and the projection of both onto the line omega spanned by the vector of ones. The three right-angled legs have squared lengths SS_T, SS_Tr and SS_E.](./plots/anova-geometry.py)

### 3.4.3. Cochran's Theorem

Why are $\mathrm{SS}_{\mathrm{Tr}}$ and $\mathrm{SS}_{\mathrm{E}}$ independent $\chi^2$ variables? If $Z_1, \dots, Z_k$ are independent $\mathcal{N}(0, 1)$, then $\sum_iZ_i^2 \sim \chi^2_k$. The question is when a decomposition of $\sum_iZ_i^2$ into several quadratic forms gives independent $\chi^2$ pieces.

**Theorem 3.4.1 (Cochran's Theorem)** Let $Z_1, \dots, Z_k$ be independent $\mathcal{N}(0, 1)$, $\boldsymbol{Z} = (Z_1, \dots, Z_k)^{\mathsf T}$, and

$$
\sum_{i=1}^k Z_i^2 = Q_1 + Q_2 + \cdots + Q_s,\qquad Q_j = \boldsymbol{Z}^{\mathsf T}A_j\boldsymbol{Z},
$$
where $s \le k$ and each $A_j$ is symmetric with $\operatorname{rank}(A_j) = k_j$. Then $Q_1, \dots, Q_s$ are independent $\chi^2$ random variables with $k_1, \dots, k_s$ degrees of freedom if and only if

$$
k = k_1 + k_2 + \cdots + k_s.
$$

**Proof** (outline) If the $Q_j$ are independent $\chi^2_{k_j}$, comparing means gives $k = \sum_j k_j$. Conversely, suppose $\sum_jA_j = I_k$ and $\sum_j\operatorname{rank}(A_j) = k$. Then the column spaces of the $A_j$ together span $\mathbb{R}^k$ with dimensions adding up to $k$, so $\mathbb{R}^k$ is their direct sum. For any $\boldsymbol{x}$ in the column space of $A_l$, $\boldsymbol{x} = I\boldsymbol{x} = \sum_jA_j\boldsymbol{x}$, and uniqueness of the direct-sum decomposition forces $A_l\boldsymbol{x} = \boldsymbol{x}$ and $A_j\boldsymbol{x} = \boldsymbol{0}$ for $j \ne l$. Hence every $A_j$ is idempotent and $A_jA_l = O$ for $j \ne l$: the $A_j$ are orthogonal projections onto mutually orthogonal subspaces. Choosing an orthonormal basis adapted to these subspaces, $Q_j$ is the sum of squares of $k_j$ coordinates of an orthogonal transformation of $\boldsymbol{Z}$, which are independent $\mathcal{N}(0, 1)$; so the $Q_j$ are independent $\chi^2_{k_j}$. The idempotent case of this argument is the lemma on quadratic forms in [3.3.8](/3.3.8). $\square$

**Corollary 3.4.1** Under $H_0\colon \mu_1 = \cdots = \mu_a = \mu$, the variables $Z_{ij} = (Y_{ij} - \mu)/\sigma$ are independent $\mathcal{N}(0, 1)$, and

$$
\sum_{i,j}Z_{ij}^2 = \frac{N(\bar Y_{\cdot\cdot} - \mu)^2}{\sigma^2} + \frac{\mathrm{SS}_{\mathrm{Tr}}}{\sigma^2} + \frac{\mathrm{SS}_{\mathrm{E}}}{\sigma^2}
$$
is a decomposition into quadratic forms of ranks $1$, $a - 1$ and $N - a$, which add up to $N$. Hence $\mathrm{SS}_{\mathrm{Tr}}/\sigma^2 \sim \chi^2_{a-1}$ and $\mathrm{SS}_{\mathrm{E}}/\sigma^2 \sim \chi^2_{N-a}$ are independent, which proves Theorem 3.3.2. (Without $H_0$, the same argument applied to $(Y_{ij} - \mu_i)/\sigma$ shows that $\mathrm{SS}_{\mathrm{E}}/\sigma^2 \sim \chi^2_{N-a}$ always.)

The ranks are those of the three projections in Section 3.4.2, so the theorem is the probabilistic form of the orthogonal decomposition: orthogonal subspaces carry independent pieces of an isotropic normal vector. This fact is the foundation of the exact $F$-tests in all the balanced designs of later chapters.

## 3.5. ANOVA, Regression, the General Linear Test and the Likelihood Ratio Test

### 3.5.1. ANOVA Is Regression

Section 3.2.2 wrote both ANOVA models as linear regressions on indicator variables, so ANOVA is regression, and the ANOVA table above is the regression ANOVA table of [3.3.4](/3.3.4). The difference lies in what the models attend to. A regression model describes the statistical relation $\mathbb{E}Y = f(X)$ between quantitative predictors and the response; ANOVA does not use the numerical values of the levels, or even their order, and it estimates a separate mean for each level. The RF powers $160, \dots, 220\,\mathrm{W}$ are numbers, and a regression on power with one slope would use $2$ mean parameters where ANOVA uses $4$; it could interpolate between the settings, but it would be wrong if the relation is not linear. When the factor is quantitative the two approaches can be combined and compared, which is done in [3.8.5](/3.8.5).

### 3.5.2. The ANOVA F-Test as a General Linear Test

The **general linear test** ([3.3.4](/3.3.4)) compares a **full model** with a **reduced model** obtained by imposing $H_0$, through their error sums of squares:

$$
F_0 = \frac{\bigl[\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F)\bigr]/(\mathrm{df}_R - \mathrm{df}_F)}{\mathrm{SS}_{\mathrm{E}}(F)/\mathrm{df}_F} \sim F_{\mathrm{df}_R - \mathrm{df}_F,\,\mathrm{df}_F}\quad\text{under } H_0.
$$
The test is best thought of as a comparison of two linear models: does the extra structure of the full model reduce the error sum of squares by more than chance would? In a multiple regression with four predictors, for example, $H_0\colon \beta_1 = \beta_3 = 0$ reduces the full model $y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \beta_3x_3 + \beta_4x_4 + \varepsilon$ to $y = \beta_0 + \beta_2x_2 + \beta_4x_4 + \varepsilon$; in R the comparison is

```r
redmodel  <- lm(y ~ x2 + x4, data = gas)
fullmodel <- lm(y ~ x1 + x2 + x3 + x4, data = gas)
anova(redmodel, fullmodel)
```

```text
Analysis of Variance Table

Model 1: y ~ x2 + x4
Model 2: y ~ x1 + x2 + x3 + x4
  Res.Df    RSS Df Sum of Sq      F Pr(>F)
1     29 238.39                           
2     27 201.23  2    37.159 2.4929 0.1015
```

Here $\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F) = 238.39 - 201.23 = 37.16$ on $29 - 27 = 2$ degrees of freedom, $F_0 = (37.16/2)/(201.23/27) = 2.49$, and $p = 0.10$: $x_1$ and $x_3$ can be dropped.

For the single-factor experiment, the full model is $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$ and $H_0\colon \tau_1 = \cdots = \tau_a = 0$ gives the reduced model $Y_{ij} = \mu + \varepsilon_{ij}$, which says that all observations come from one group; the reduced model is just another way of stating the hypothesis. The full model's error sum of squares is $\mathrm{SS}_{\mathrm{E}}(F) = \sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2 = \mathrm{SS}_{\mathrm{E}}$ on $N - a$ degrees of freedom; the reduced model fits $\bar y_{\cdot\cdot}$ to every observation, so $\mathrm{SS}_{\mathrm{E}}(R) = \sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2 = \mathrm{SS}_{\mathrm{T}}$ on $N - 1$. Hence

$$
F_0 = \frac{(\mathrm{SS}_{\mathrm{T}} - \mathrm{SS}_{\mathrm{E}})/(a - 1)}{\mathrm{SS}_{\mathrm{E}}/(N - a)} = \frac{\mathrm{SS}_{\mathrm{Tr}}/(a - 1)}{\mathrm{SS}_{\mathrm{E}}/(N - a)},
$$
exactly the ANOVA $F$-test. Geometrically, $\mathrm{SS}_{\mathrm{E}}(R) = \lVert\boldsymbol{y} - P_\omega\boldsymbol{y}\rVert^2$ and $\mathrm{SS}_{\mathrm{E}}(F) = \lVert\boldsymbol{y} - P_\Omega\boldsymbol{y}\rVert^2$, and their difference is the squared length of the leg in $\Omega \ominus \omega$ in the figure of Section 3.4.2.

In R the same hypothesis can be written as linear restrictions on the coefficients of either parametrization, with `linearHypothesis` from the package `car`. In the means model the hypothesis $\mu_1 = \mu_2 = \mu_3 = \mu_4$ consists of three linearly independent restrictions:

```r
fit <- lm(rate ~ 0 + RF, data = etch.rate)          # means model
library(car)
linearHypothesis(fit, c("RF160-RF180", "RF180-RF200", "RF200-RF220"))
# or with an explicit restriction matrix
conmat <- matrix(0, nrow = 3, ncol = 4)
conmat[, 1] <- 1; conmat[1, 2] <- conmat[2, 3] <- conmat[3, 4] <- -1
linearHypothesis(fit, conmat)
```

```text
> conmat
     [,1] [,2] [,3] [,4]
[1,]    1   -1    0    0
[2,]    1    0   -1    0
[3,]    1    0    0   -1

Linear hypothesis test

Hypothesis:
RF160 - RF180 = 0
RF160 - RF200 = 0
RF160 - RF220 = 0

Model 1: restricted model
Model 2: rate ~ 0 + RF

  Res.Df   RSS Df Sum of Sq      F    Pr(>F)    
1     19 72210                                  
2     16  5339  3     66871 66.797 2.883e-09 ***
```

The restricted model has $\mathrm{RSS} = \mathrm{SS}_{\mathrm{T}} = 72210$ on $19$ degrees of freedom, the means model has $\mathrm{SS}_{\mathrm{E}} = 5339$ on $16$, and the difference $66871$ on $3$ degrees of freedom is $\mathrm{SS}_{\mathrm{Tr}}$: the result coincides with `anova(fit1)` in Section 3.3.4. With R's default coding (`fit1 <- lm(rate ~ RF)`, coefficients `(Intercept)`, `RF180`, `RF200`, `RF220`), the same hypothesis is that the three differences from the first level vanish:

```r
linearHypothesis(fit1, c("RF180 = 0", "RF200 = 0", "RF220 = 0"))
# or
conmat <- matrix(0, nrow = 3, ncol = 4)
conmat[1, 2] <- conmat[2, 3] <- conmat[3, 4] <- 1
linearHypothesis(fit1, conmat)
```

Which restrictions are written does not matter, as long as they define the same reduced model. The general linear test is also how the theory extends: for two factors, blocks or covariates, each $F$-test in an ANOVA table compares a model with a submodel ([3.3.9](/3.3.9)).

### 3.5.3. The General Linear Model

The models of this chapter, of the comparative experiments of [3.8.2](/3.8.2) and of the regression course are all instances of one model.

**Definition 3.5.1 (General Linear Model)** The **general linear model** is

$$
\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon},\qquad \boldsymbol{\varepsilon} \sim \mathcal{N}_N(\boldsymbol{0}, \sigma^2 I_N),
$$
where $X$ is a known $N \times p$ matrix whose columns may be quantitative predictors, indicators of factor levels, or both, and $\boldsymbol{\beta}$ is an unknown parameter vector.

The one-sample $z$- and $t$-tests ($X = \boldsymbol{1}$), the two-sample $t$-test (two indicator columns), one-way and multi-way ANOVA, linear regression and the analysis of covariance are special cases, and their tests of linear hypotheses are general linear tests. The name should not be confused with the **generalized linear model** ([3.3.6](/3.3.6)), which allows non-normal responses (binomial, Poisson) and a link function between the mean and the linear predictor.

### 3.5.4. Equivalence with the Likelihood Ratio Test

The $F$-test of a linear hypothesis in the normal general linear model is always equivalent to the **likelihood ratio test** ([3.2.5](/3.2.5)). Consider first $H_0\colon \beta_1 = 0$ in the simple linear regression $Y_i = \beta_0 + \beta_1x_i + \varepsilon_i$. The maximum likelihood estimates are $\hat{\boldsymbol\theta} = (b_0, b_1, s^2)$ with $s^2 = \sum_i(y_i - b_0 - b_1x_i)^2/n$ in the full model, and $\hat{\boldsymbol\theta}_0 = (\bar y, 0, s_Y^2)$ with $s_Y^2 = \sum_i(y_i - \bar y)^2/n$ in the reduced model. A normal likelihood evaluated at the MLE of the variance is $(2\pi\hat\sigma^2)^{-n/2}\mathrm{e}^{-n/2}$, so

$$
\Lambda = \frac{L(\hat{\boldsymbol\theta}_0)}{L(\hat{\boldsymbol\theta})} = \Bigl(\frac{s^2}{s_Y^2}\Bigr)^{n/2},\qquad -2\log\Lambda = n\log\frac{s_Y^2}{s^2}.
$$
Since $s_Y^2/s^2 = \mathrm{SST}/\mathrm{SSE} = 1 + \mathrm{SSR}/\mathrm{SSE} = 1 + F/(n - 2)$,

$$
-2\log\Lambda = n\log\Bigl(1 + \frac{F}{n - 2}\Bigr),
$$
a strictly increasing function of $F$. **Wilks' theorem** gives $-2\log\Lambda \to \chi^2_1$ in distribution, but the exact distribution of $F$ makes the approximation unnecessary: rejecting for large $-2\log\Lambda$ is the same as rejecting for large $F$, and the $F$ distribution gives the exact critical value.

The same computation applies to one-way ANOVA. The MLE of $\sigma^2$ is $\mathrm{SS}_{\mathrm{E}}/N$ in the full model and $\mathrm{SS}_{\mathrm{T}}/N$ in the reduced model $Y_{ij} = \mu + \varepsilon_{ij}$, so

$$
-2\log\Lambda = N\log\frac{\mathrm{SS}_{\mathrm{T}}}{\mathrm{SS}_{\mathrm{E}}} = N\log\Bigl(1 + \frac{a - 1}{N - a}F_0\Bigr),
$$
again a monotone function of $F_0$. For the etching data, $-2\log\Lambda = 20\log(72209.75/5339.2) = 52.1$. The likelihood ratio test, the general linear test and the ANOVA $F$-test are three derivations of the same procedure.

## Summary

The single-factor ANOVA for a completely randomized design (Definition 3.1.1), in the model $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$, $\varepsilon_{ij} \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$:

| Source | SS | df | MS | $\mathbb{E}[\mathrm{MS}]$ | $F_0$ |
|---|---|---|---|---|---|
| Treatments | $\sum_i n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2 = \sum_i\frac{y_{i\cdot}^2}{n_i} - \frac{y_{\cdot\cdot}^2}{N}$ | $a - 1$ | $\mathrm{SS}_{\mathrm{Tr}}/(a - 1)$ | $\sigma^2 + \frac{\sum_i n_i\tau_i^2}{a - 1}$ | $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}} \overset{H_0}{\sim} F_{a-1,N-a}$ |
| Error | $\sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2 = \mathrm{SS}_{\mathrm{T}} - \mathrm{SS}_{\mathrm{Tr}}$ | $N - a$ | $\mathrm{SS}_{\mathrm{E}}/(N - a)$ | $\sigma^2$ | |
| Total | $\sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2 = \sum_{i,j}y_{ij}^2 - \frac{y_{\cdot\cdot}^2}{N}$ | $N - 1$ | | | |

- Estimates (Proposition 3.2.1): $\hat\mu_i = \bar y_{i\cdot}$, $\hat\tau_i = \bar y_{i\cdot} - \bar y_{\cdot\cdot}$ (balanced), $\hat\sigma^2 = \mathrm{MS}_{\mathrm{E}}$; intervals use $t_{N-a,\alpha/2}$ and $\mathrm{MS}_{\mathrm{E}}$.
- Expected mean squares (Theorem 3.3.1) explain the upper-tailed $F$-test (Theorem 3.3.2); $F_0$ grows with the spread of the level means and with $n_i$, and shrinks with the within-group scatter.
- Geometry: $\mathbb{R}^N = \omega \oplus (\Omega \ominus \omega) \oplus \Omega^{\perp}$ with dimensions $1$, $a - 1$, $N - a$; the sums of squares are squared lengths of projections, the degrees of freedom are dimensions, and Cochran's theorem (Theorem 3.4.1) turns orthogonality into independence of the $\chi^2$ pieces.
- One test, four names:

| View | Full model / statistic | Reduced model | Equivalence |
|---|---|---|---|
| ANOVA | $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}$ | — | definition |
| Regression | overall $F$ of the regression on $a - 1$ indicators | intercept only | same table |
| General linear test | $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$, $\mathrm{SS}_{\mathrm{E}}(F) = \mathrm{SS}_{\mathrm{E}}$ | $Y_{ij} = \mu + \varepsilon_{ij}$, $\mathrm{SS}_{\mathrm{E}}(R) = \mathrm{SS}_{\mathrm{T}}$ | $\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F) = \mathrm{SS}_{\mathrm{Tr}}$ |
| Likelihood ratio test | $-2\log\Lambda = N\log(\mathrm{SS}_{\mathrm{T}}/\mathrm{SS}_{\mathrm{E}})$ | | monotone in $F_0$ |

- ANOVA is a special case of the general linear model (Definition 3.5.1); unlike regression on a quantitative factor, it ignores the numerical values of the levels.

## Questions

1. Complete the following ANOVA table of a balanced single-factor experiment and give the range of the $p$-value.

   | Source | SS | df | MS | $F_0$ |
   |---|---|---|---|---|
   | Factor | ? | ? | 14.0 | ? |
   | Error | 30.0 | ? | ? | |
   | Total | 72.0 | 23 | | |

   **Answer** $\mathrm{SS}_{\mathrm{Tr}} = 72.0 - 30.0 = 42.0$, so $a - 1 = 42.0/14.0 = 3$, $a = 4$, and $N - a = 23 - 3 = 20$ (hence $n = 6$). Then $\mathrm{MS}_{\mathrm{E}} = 30.0/20 = 1.5$ and $F_0 = 14.0/1.5 = 9.33$. Since $F_{3,20,0.01} = 4.94$ and $F_{3,20,0.001} = 8.10$, $p < 0.001$ (exactly, $p = 4.6\times10^{-4}$).

2. Three drugs are given to $n = 7$ patients each, and a higher score is better. The sample means are $5.54$, $5.03$ and $5.93$, and the pooled within-group variance is $\mathrm{MS}_{\mathrm{E}} = 0.25$. Construct the ANOVA table and test equality of the means at $\alpha = 0.05$.

   **Answer** $N = 21$, $\bar y_{\cdot\cdot} = (5.54 + 5.03 + 5.93)/3 = 5.50$. $\mathrm{SS}_{\mathrm{Tr}} = 7\bigl(0.04^2 + 0.47^2 + 0.43^2\bigr) = 7 \times 0.4074 = 2.852$ on $2$ degrees of freedom, $\mathrm{MS}_{\mathrm{Tr}} = 1.426$; $\mathrm{SS}_{\mathrm{E}} = 18 \times 0.25 = 4.50$ on $18$; $\mathrm{SS}_{\mathrm{T}} = 7.352$ on $20$. $F_0 = 1.426/0.25 = 5.70 > F_{2,18,0.05} = 3.55$, $p = 0.012$: the mean scores differ. Note that the table can be built from the summary statistics alone: the means give $\mathrm{SS}_{\mathrm{Tr}}$ and $\mathrm{MS}_{\mathrm{E}}$ gives $\mathrm{SS}_{\mathrm{E}}$.

3. Show that for $a = 2$ the ANOVA statistic equals the square of the pooled two-sample $t$ statistic, $F_0 = t_0^2$, and that the two tests are identical.

   **Answer** With $a = 2$, $\bar y_{\cdot\cdot} = (n_1\bar y_{1\cdot} + n_2\bar y_{2\cdot})/N$, so $\bar y_{1\cdot} - \bar y_{\cdot\cdot} = \frac{n_2}{N}(\bar y_{1\cdot} - \bar y_{2\cdot})$ and $\bar y_{2\cdot} - \bar y_{\cdot\cdot} = -\frac{n_1}{N}(\bar y_{1\cdot} - \bar y_{2\cdot})$. Hence
   $$
   \mathrm{SS}_{\mathrm{Tr}} = \frac{n_1n_2^2 + n_2n_1^2}{N^2}(\bar y_{1\cdot} - \bar y_{2\cdot})^2 = \frac{(\bar y_{1\cdot} - \bar y_{2\cdot})^2}{1/n_1 + 1/n_2}.
   $$
   $\mathrm{MS}_{\mathrm{E}} = \mathrm{SS}_{\mathrm{E}}/(N - 2) = s_p^2$, so $F_0 = \mathrm{SS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}} = (\bar y_{1\cdot} - \bar y_{2\cdot})^2/\bigl(s_p^2(1/n_1 + 1/n_2)\bigr) = t_0^2$. Since $t_{N-2}^2 \sim F_{1,N-2}$ and $F_{1,N-2,\alpha} = t_{N-2,\alpha/2}^2$, rejecting when $F_0 > F_{1,N-2,\alpha}$ is the same as rejecting when $\lvert t_0\rvert > t_{N-2,\alpha/2}$.

4. In the general linear test for the single-factor experiment, which of the quantities $\sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2$, $\sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2$ and $\sum_i n(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2$ is the error sum of squares of the full model, and which that of the reduced model?

   **Answer** The full model $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$ fits $\bar y_{i\cdot}$, so its error sum of squares is $\sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2 = \mathrm{SS}_{\mathrm{E}}$. The reduced model $Y_{ij} = \mu + \varepsilon_{ij}$ fits $\bar y_{\cdot\cdot}$, so its error sum of squares is $\sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2 = \mathrm{SS}_{\mathrm{T}}$. The third quantity, $\mathrm{SS}_{\mathrm{Tr}}$, is their difference, the reduction in error achieved by the factor.

5. Two experiments each compare five levels with the same sample size, and their level means are equally spread. In experiment A the observations within each level are tightly clustered; in experiment B they vary widely. In which experiment is the factor effect more significant? And if two experiments have the same means and the same within-group spread, but experiment C has $3$ observations per level and experiment D has $300$?

   **Answer** Experiment A: with the same $\mathrm{SS}_{\mathrm{Tr}}$, the smaller $\mathrm{SS}_{\mathrm{E}}$ gives the larger $F_0$. Experiment D: $\mathrm{SS}_{\mathrm{Tr}} = \sum_i n(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2$ is $100$ times larger, $\mathrm{MS}_{\mathrm{E}}$ estimates the same $\sigma^2$, so $F_0$ is about $100$ times larger, and the error degrees of freedom are larger too. The significance depends on the variance $\sigma^2/n$ of the level means, not on the spread of the observations seen in a box plot.

6. Prove that $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}] = \sigma^2 + n\sum_i\tau_i^2/(a - 1)$ in a balanced experiment by writing $\mathrm{SS}_{\mathrm{Tr}}$ in terms of the level means $\bar Y_{i\cdot}$ only.

   **Answer** The $\bar Y_{i\cdot} \sim \mathcal{N}(\mu + \tau_i, \sigma^2/n)$ are independent, and $\mathrm{SS}_{\mathrm{Tr}} = n\sum_i(\bar Y_{i\cdot} - \bar{\bar Y})^2$ with $\bar{\bar Y} = \frac1a\sum_i\bar Y_{i\cdot} = \bar Y_{\cdot\cdot}$. For independent $W_i$ with means $\theta_i$ and common variance $v$, $\mathbb{E}\sum_i(W_i - \bar W)^2 = \sum_i(\theta_i - \bar\theta)^2 + (a - 1)v$. With $W_i = \bar Y_{i\cdot}$, $\theta_i - \bar\theta = \tau_i$ (since $\sum_i\tau_i = 0$) and $v = \sigma^2/n$, so $\mathbb{E}[\mathrm{SS}_{\mathrm{Tr}}] = n\sum_i\tau_i^2 + (a - 1)\sigma^2$.

7. Show that $-2\log\Lambda$ for one-way ANOVA is $N\log\bigl(1 + \frac{a-1}{N-a}F_0\bigr)$, and compare the likelihood ratio test based on Wilks' theorem with the $F$-test for the etching data.

   **Answer** $\mathrm{SS}_{\mathrm{T}}/\mathrm{SS}_{\mathrm{E}} = 1 + \mathrm{SS}_{\mathrm{Tr}}/\mathrm{SS}_{\mathrm{E}} = 1 + \frac{(a-1)\mathrm{MS}_{\mathrm{Tr}}}{(N-a)\mathrm{MS}_{\mathrm{E}}}$, and $-2\log\Lambda = N\log(\mathrm{SS}_{\mathrm{T}}/\mathrm{SS}_{\mathrm{E}})$ (Section 3.5.4). For the etching data $-2\log\Lambda = 20\log(1 + \frac{3}{16}\times 66.80) = 52.1$, referred to $\chi^2_3$, $p \approx 3\times10^{-11}$, smaller than the exact $p = 2.9\times10^{-9}$ of the $F$-test. Both reject; the asymptotic $\chi^2$ calibration is too liberal for $N = 20$, which is why the exact $F$ distribution is used.
