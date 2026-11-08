---
title: "Single-Factor Experiments: Diagnostics, Power, Random Effects, and the Regression Approach"
description: Residual diagnostics for one-way ANOVA (normal probability plot, standardized residuals, Bartlett's and Levene's tests, Welch's ANOVA, leverage 1/n_i); power and sample size from the noncentral F-distribution and power.anova.test; the one-way random-effects model with its covariance structure, expected mean squares, ANOVA and REML estimates of the variance components, the intraclass correlation coefficient, confidence intervals and the R output of aov, lm and lmer; choosing fixed or random effects; and the regression approach to a quantitative factor with lack-of-fit and polynomial terms.
---

The one-way analysis of variance of [3.8.3](/3.8.3) and the multiple comparisons of [3.8.4](/3.8.4) rest on a model, and this chapter completes the study of single-factor experiments with four questions about that model. First, are its assumptions (normal, independent errors with a common variance) supported by the data, and what can be done when the variances differ? Second, how many replicates are needed so that the $F$-test detects differences of a given size; this is the planning side of the same model. Third, what changes when the levels of the factor are not the only ones of interest but a random sample from a large population of levels; this leads to the random-effects model, its variance components and the intraclass correlation. Fourth, when the factor is quantitative, can the numerical values of its levels be used, by fitting a regression on them instead of treating the levels as unordered categories?

Much of the necessary machinery is already in the linear regression course: residual plots and tests of equal variances ([3.3.5](/3.3.5)), leverage and the hat matrix ([3.3.7](/3.3.7)), the lack-of-fit test ([3.3.5](/3.3.5)), polynomial regression ([3.3.10](/3.3.10)), and weighted ANOVA, transformations and the Kruskal–Wallis test ([3.3.14](/3.3.14)). Here we use these tools in the setting of designed experiments and add what is specific to it. Two running examples are used: the plasma etching experiment of [3.8.3](/3.8.3) (four levels of RF power, five wafers each) and a new experiment on the strength of fabric woven on randomly chosen looms.

## 5.1. Checking the Model Assumptions

The one-way model $Y_{ij}=\mu+\tau_i+\varepsilon_{ij}$ assumes that the errors $\varepsilon_{ij}$ are independent $\mathcal{N}(0,\sigma^2)$. The $F$-test, the confidence intervals and the multiple comparisons all inherit their validity from this assumption, so it must be checked. The errors are not observed, but the **residuals**

$$
e_{ij}=y_{ij}-\hat y_{ij}=y_{ij}-\bar y_{i\cdot}
$$
estimate them: under the model, $e_{ij}$ is normal with mean $0$ and variance $\sigma^2(1-1/n_i)$, so residuals that look like a sample of normal noise support the model, and systematic patterns reveal departures. Three questions are asked: are the errors normal, do they have a common variance, and are they independent? Behind them lie more general ones: is this the right model, and are there outliers that distort the analysis?

For the etching data the residuals are

| RF power (W) | residuals (run order in parentheses) | $\bar y_{i\cdot}$ |
|---|---|---|
| 160 | $23.8\ (13)$, $-9.2\ (14)$, $-21.2\ (8)$, $-12.2\ (5)$, $18.8\ (4)$ | 551.2 |
| 180 | $-22.4\ (18)$, $5.6\ (9)$, $2.6\ (6)$, $-8.4\ (16)$, $22.6\ (17)$ | 587.4 |
| 200 | $-25.4\ (7)$, $25.6\ (19)$, $-15.4\ (10)$, $11.6\ (20)$, $3.6\ (1)$ | 625.4 |
| 220 | $18.0\ (2)$, $-7.0\ (3)$, $8.0\ (15)$, $-22.0\ (11)$, $3.0\ (12)$ | 707.0 |

where the numbers in parentheses record the order in which the 20 runs were made (the design was a **completely randomized design**, so the order is a random permutation).

### 5.1.1. Normality, Outliers and Independence

**Definition 5.1.1 (Normal Probability Plot)** A **normal probability plot** (normal Q–Q plot) of a sample $x_1,\dots,x_m$ plots the ordered values $x_{(1)}\le\cdots\le x_{(m)}$ against the corresponding quantiles of the standard normal distribution, $\Phi^{-1}\big((k-0.5)/m\big)$ for $k=1,\dots,m$ (or a similar plotting position). If the sample comes from a normal distribution, the points lie close to a straight line, whose intercept and slope estimate the mean and standard deviation.

Applied to the residuals, the plot checks normality of the errors. Small samples wiggle around the line even under exact normality, so one looks for clear systematic shapes: an S-shape (light or heavy tails) or a curve (skewness). Moderate departures matter little for the fixed-effects $F$-test, which is robust to non-normality; heavy tails and outliers matter more.

A rough check for outliers uses the scaled residuals

$$
d_{ij}=\frac{e_{ij}}{\sqrt{\mathrm{MS}_{\mathrm{E}}}}.
$$
If the errors are $\mathcal{N}(0,\sigma^2)$, then $d_{ij}$ is approximately $\mathcal{N}(0,1)$, so about $95\%$ of them should lie within $\pm2$ and practically all within $\pm3$; a residual with $\lvert d_{ij}\rvert>3$ is a potential **outlier** and should be investigated (a recording error, a faulty run, or a genuine but unusual response). These $d_{ij}$ are what DAE texts call standardized residuals; they differ from the internally **standardized residuals** of regression, $r_{ij}=e_{ij}/\sqrt{\mathrm{MS}_{\mathrm{E}}(1-h_{ij})}$, only by the factor $\sqrt{1-1/n_i}$, because the leverage is $h_{ij}=1/n_i$ (Proposition 5.1.1 below).

For the etching data $\mathrm{MS}_{\mathrm{E}}=333.7$, so $\sqrt{\mathrm{MS}_{\mathrm{E}}}=18.27$, and the largest residual $25.6$ gives $\max\lvert d_{ij}\rvert=1.40$: no outliers. The normal probability plot in the figure below is close to a straight line.

Independence cannot be checked from the residuals alone, but a plot of the residuals against the run order (or against time, operator, position, and any other variable that might matter) reveals the most common violation: correlation between runs made close together, or a drift of the process. Runs of residuals with the same sign, or a trend, indicate dependence. Randomizing the run order is the main protection: it does not remove a drift, but it prevents the drift from being confounded with the treatments, as discussed in [3.8.2](/3.8.2). For the etching data the residuals against run order show no pattern.

![Residual diagnostics for the etching experiment: residuals against fitted values (the four level means), normal probability plot of the scaled residuals, residuals against run order, and scaled residuals by level with the limits plus and minus 3](./plots/etch-diagnostics.py)

### 5.1.2. Constant Variance

The assumption of **homoscedasticity**, $\sigma_1^2=\cdots=\sigma_a^2$, is checked first graphically: in a plot of the residuals against the fitted values (the level means), the vertical spread should be about the same for all levels. A funnel shape, with spread increasing with the mean, is the typical sign of **heteroscedasticity**. It often arises when the response has a skewed distribution, where the variance is a function of the mean (counts, times to failure, concentrations); a variance-stabilizing transformation, chosen for example by the Box–Cox method ([3.3.14](/3.3.14)), then usually cures both problems at once.

How much does a violation matter? Experience and simulation give a clear picture.

- In a balanced fixed-effects design the $F$-test is only slightly affected: its actual significance level stays close to the nominal one. This is one of the main advantages of a **balanced design** ([3.8.2](/3.8.2)).
- In an unbalanced design the effect is more serious, particularly when one variance is much larger than the others. If the larger variances occur in the smaller groups, the test becomes too liberal (too many false rejections); if they occur in the larger groups, it becomes conservative.
- In random-effects models (Section 5.3), unequal error variances can seriously disturb the inferences on the variance components even when the design is balanced.

Two formal tests of $H_0\colon\sigma_1^2=\cdots=\sigma_a^2$ against "at least one variance differs" are standard; both were introduced in [3.3.5](/3.3.5), and we give their statistics in the notation of this chapter. Let $S_i^2$ be the sample variance of level $i$, with $n_i-1$ degrees of freedom, $N=\sum_in_i$, and

$$
S_p^2=\frac{1}{N-a}\sum_{i=1}^a(n_i-1)S_i^2=\mathrm{MS}_{\mathrm{E}}
$$
the pooled variance.

**Bartlett's test** is a modification of the **likelihood ratio test** of equal variances under normality, designed to make the approximation by a $\chi^2$ distribution better:

$$
T=\frac{(N-a)\ln S_p^2-\sum_{i=1}^a(n_i-1)\ln S_i^2}{c}\ \overset{H_0}{\approx}\ \chi^2_{a-1},\qquad c=1+\frac{1}{3(a-1)}\left(\sum_{i=1}^a\frac{1}{n_i-1}-\frac{1}{N-a}\right),
$$
and $H_0$ is rejected when $T>\chi^2_{a-1,\alpha}$. The numerator compares the arithmetic mean of the $S_i^2$ (weighted by $w_i=(n_i-1)/(N-a)$) with their weighted geometric mean: with $l=\prod_i(S_i^2)^{w_i}/\sum_iw_iS_i^2$ the numerator is $-(N-a)\ln l$, and $0<l\le1$ by Jensen's inequality, with equality exactly when all $S_i^2$ are equal. So $T$ is large when the sample variances are spread out. Two cautions: the test is very sensitive to non-normality (heavy tails inflate it even when the variances are equal), and the $\chi^2$ approximation is poor for small samples; a common recommendation is $\min_in_i\ge3$ and most $n_i>5$.

**Levene's test** is robust to non-normality. It replaces each observation by its absolute deviation from the level center, $Z_{ij}=\lvert y_{ij}-\bar y_{i\cdot}\rvert$, and performs a one-way ANOVA on the $Z_{ij}$:

$$
T=\frac{N-a}{a-1}\cdot\frac{\sum_{i=1}^an_i(\bar Z_{i\cdot}-\bar Z_{\cdot\cdot})^2}{\sum_{i=1}^a\sum_{j=1}^{n_i}(Z_{ij}-\bar Z_{i\cdot})^2}\ \overset{H_0}{\approx}\ F_{a-1,N-a},
$$
rejecting $H_0$ when $T>F_{a-1,N-a,\alpha}$. If the variances are equal, the mean absolute deviations are about equal and $T$ is small. The **Brown–Forsythe test** (modified Levene test) uses the level medians, $Z_{ij}=\lvert y_{ij}-\tilde y_{i}\rvert$, which makes it more robust still against skewed distributions; it is the default of `car::leveneTest` in R.

For the etching data both tests agree that there is no evidence of unequal variances (the sample variances are $400.7$, $280.3$, $421.3$, $232.5$):

```r
bartlett.test(rate ~ RF, data = etch.rate)
library(car)
leveneTest(etch.rate.aov)
```

```text
	Bartlett test of homogeneity of variances

data:  rate by RF
Bartlett's K-squared = 0.43349, df = 3, p-value = 0.9332

Levene's Test for Homogeneity of Variance (center = median)
      Df F value Pr(>F)
group  3  0.1959 0.8977
      16
```

In the Bartlett output, `K-squared` is the statistic $T$ and `df` $=a-1=3$. The Levene output is an ANOVA table of the $Z_{ij}$: the row `group` has $a-1=3$ degrees of freedom, the unlabeled second row the residual $N-a=16$, and `center = median` says that this is the Brown–Forsythe version.

### 5.1.3. Welch's ANOVA

When the variances clearly differ, one option is to transform the response, another is a weighted ANOVA ([3.3.14](/3.3.14)). A third is to modify the test itself, exactly as **Welch's t-test** modifies the pooled two-sample $t$-test ([3.2.5](/3.2.5), [3.8.2](/3.8.2)): each level mean is weighted by its estimated precision, and the degrees of freedom are approximated by the **Satterthwaite approximation**.

**Definition 5.1.2 (Welch's ANOVA)** Let $\bar y_{i\cdot}$ and $s_i^2$ be the mean and variance of the $n_i$ observations at level $i$, and

$$
w_i=\frac{n_i}{s_i^2},\qquad w=\sum_{i=1}^aw_i,\qquad \bar y'=\frac{\sum_iw_i\bar y_{i\cdot}}{w},\qquad \Lambda=\sum_{i=1}^a\frac{(1-w_i/w)^2}{n_i-1}.
$$
**Welch's ANOVA** tests $H_0\colon\mu_1=\cdots=\mu_a$ without assuming equal variances by

$$
F_0^*=\frac{\frac{1}{a-1}\sum_{i=1}^aw_i(\bar y_{i\cdot}-\bar y')^2}{1+\frac{2(a-2)}{a^2-1}\Lambda}\ \overset{H_0}{\approx}\ F_{a-1,\,\nu},\qquad \nu=\frac{a^2-1}{3\Lambda},
$$
rejecting $H_0$ when $F_0^*>F_{a-1,\nu,\alpha}$.

The weight $w_i=n_i/s_i^2$ is the reciprocal of the estimated variance of $\bar y_{i\cdot}$, so precise means count more, and $\bar y'$ is the corresponding weighted grand mean. The numerator is a weighted treatment mean square; the denominator corrects for the variability of the estimated weights, and the denominator degrees of freedom $\nu$ are not an integer and are typically far below $N-a$. For $a=2$ the statistic reduces to the square of Welch's $t$ statistic, with the same Welch–Satterthwaite degrees of freedom. Welch's ANOVA still assumes normal and independent errors; it is most useful when the variances are unequal and the sample sizes are unequal or small, the situation in which the ordinary $F$-test is least reliable.

```r
oneway.test(rate ~ RF, data = etch.rate, var.equal = FALSE)
```

```text
	One-way analysis of means (not assuming equal variances)

data:  rate and RF
F = 68.719, num df = 3.0000, denom df = 8.8278, p-value = 1.913e-06
```

The conclusion agrees with the ordinary $F$-test ($F_0=66.80$ on 3 and 16 degrees of freedom): the variances of the etching data are similar, so the weights hardly change the statistic, but the price of not assuming equal variances is visible in the denominator degrees of freedom, $8.83$ instead of $16$.

If Welch's ANOVA protects the test of means anyway, why test for unequal variances at all? There are several reasons. Unequal variances are often a finding in themselves: a treatment that changes the variability of a process may matter more than one that shifts its mean, a point already made for two samples in [3.8.2](/3.8.2). Nonconstant variance is also a symptom: of a skewed response that should be transformed, of a missing factor, or of outliers. And the robust test covers only the global test of means; the multiple comparisons of [3.8.4](/3.8.4), the estimates of variance components in Section 5.3 and the multifactor analyses of [3.8.6](/3.8.6) have no equally simple Welch version and rely on the assumption of a common variance.

### 5.1.4. Diagnostic Plots in R and Leverage

In R, `plot` applied to a fitted `aov` object draws four diagnostic plots:

```r
opar <- par(mfrow = c(2, 2), cex = .8)
plot(etch.rate.aov)
par(opar)
```

They are the residuals against the fitted values, the normal Q–Q plot of the standardized residuals, the scale–location plot ($\sqrt{\lvert r_{ij}\rvert}$ against the fitted values, for detecting a trend in the spread), and a fourth plot that for regression models shows standardized residuals against **leverage**. For a one-way model R replaces the last one by residuals against the factor levels, and labels it "Constant Leverage". The reason is the following fact.

**Proposition 5.1.1** In the one-way model fitted by least squares, the leverage of the observation $y_{ij}$, that is, the diagonal element of the **hat matrix** $H$, is $h_{ij}=1/n_i$.

**Proof** Order the observations by level and use the means model $\boldsymbol{Y}=X\boldsymbol{\mu}+\boldsymbol{\varepsilon}$, whose **design matrix** $X$ has a column of level indicators for each level; the effects model has the same column space, hence the same $H$. Then $X^{\mathsf T}X=\operatorname{diag}(n_1,\dots,n_a)$ and

$$
H=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}=\begin{bmatrix}\frac{1}{n_1}\boldsymbol{1}_{n_1}\boldsymbol{1}_{n_1}^{\mathsf T}&&\\&\ddots&\\&&\frac{1}{n_a}\boldsymbol{1}_{n_a}\boldsymbol{1}_{n_a}^{\mathsf T}\end{bmatrix},
$$
a block diagonal matrix whose $i$-th block averages the observations of level $i$; indeed $H\boldsymbol{y}$ replaces each $y_{ij}$ by $\bar y_{i\cdot}$. Its diagonal elements are $1/n_i$. $\square$

In a balanced design all observations therefore have the same leverage $1/n$, and the plot of residuals against leverage degenerates to a vertical strip. This marks a real difference between diagnostics for ANOVA and for regression. In regression on continuous predictors, observations differ greatly in leverage, and a single point far out in the predictor space can determine the fit, so leverage and influence measures are central. In a one-way ANOVA no design point is more remote than another, the fitted value of a level is the mean of its own observations, and an outlier can only distort its own level mean and the pooled variance. The diagnostic effort therefore concentrates on the variance of each group, normality and outliers in the response, and independence; and when the design is unbalanced, the levels with few observations have the larger leverage.

## 5.2. Power and Sample Size

Before an experiment is run, one should decide how many replicates are needed. Too few, and real differences between treatments are likely to be missed; too many, and resources are wasted. For the one-way $F$-test the question is: given the significance level $\alpha$, the error standard deviation $\sigma$ and a configuration of treatment means that we would like to detect, which $n$ per level gives the test a prescribed **power** $1-\beta$? The answer requires the distribution of $F_0$ when $H_0$ is false.

### 5.2.1. The Noncentral F-Distribution

**Definition 5.2.1 (Noncentral Chi-Square Distribution)** Let $X_1,\dots,X_\nu$ be independent with $X_k\sim\mathcal{N}(\delta_k,1)$. The distribution of $\sum_{k=1}^\nu X_k^2$ depends only on $\nu$ and $\lambda=\sum_k\delta_k^2$; it is called the **noncentral chi-square distribution** $\chi^2_\nu(\lambda)$ with $\nu$ degrees of freedom and noncentrality parameter $\lambda$. Its mean is $\nu+\lambda$, and $\chi^2_\nu(0)$ is the ordinary **chi-square distribution**.

**Definition 5.2.2 (Noncentral F-Distribution)** If $U\sim\chi^2_{\nu_1}(\lambda)$ and $V\sim\chi^2_{\nu_2}$ are independent, the distribution of $(U/\nu_1)/(V/\nu_2)$ is the **noncentral F-distribution** $F_{\nu_1,\nu_2}(\lambda)$; for $\lambda=0$ it is the central **F-distribution**.

These are the analogues of the **noncentral t-distribution** used for the power of $t$-tests ([3.3.3](/3.3.3), [3.8.2](/3.8.2)). The larger the **noncentrality parameter** $\lambda$, the further the distribution is shifted to the right, and the more likely the statistic exceeds a fixed critical value.

**Theorem 5.2.1** In the balanced one-way fixed-effects model with $n$ observations per level,

$$
\frac{\mathrm{SS}_{\mathrm{Tr}}}{\sigma^2}\sim\chi^2_{a-1}(\lambda),\qquad \frac{\mathrm{SS}_{\mathrm{E}}}{\sigma^2}\sim\chi^2_{N-a},\qquad F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\sim F_{a-1,N-a}(\lambda),\qquad \lambda=\frac{n\sum_{i=1}^a\tau_i^2}{\sigma^2},
$$
with $\mathrm{SS}_{\mathrm{Tr}}$ and $\mathrm{SS}_{\mathrm{E}}$ independent. Under $H_0$ ($\lambda=0$) the distributions are central.

**Proof** The vector $\sqrt n(\bar Y_{1\cdot},\dots,\bar Y_{a\cdot})/\sigma$ is $\mathcal{N}_a(\sqrt n\boldsymbol{\mu}/\sigma,I_a)$, and $\mathrm{SS}_{\mathrm{Tr}}/\sigma^2=\lVert P\sqrt n\bar{\boldsymbol{Y}}/\sigma\rVert^2$ for the projection $P=I_a-\frac1a\boldsymbol{1}\boldsymbol{1}^{\mathsf T}$ of rank $a-1$. Rotating to an orthonormal basis of the range of $P$ gives a sum of $a-1$ squares of independent unit-variance normals, whose squared means add up to $\lVert P\sqrt n\boldsymbol{\mu}\rVert^2/\sigma^2=n\sum_i(\mu_i-\bar\mu)^2/\sigma^2=n\sum_i\tau_i^2/\sigma^2$. The distribution of $\mathrm{SS}_{\mathrm{E}}$ and the independence are as under $H_0$ ([3.8.3](/3.8.3)), since $\mathrm{SS}_{\mathrm{E}}$ does not involve the means. $\square$

The power of the level-$\alpha$ test is therefore

$$
1-\beta=\mathbb{P}\big(F_{a-1,N-a}(\lambda)>F_{a-1,N-a,\alpha}\big),
$$
an increasing function of $\lambda$, which in turn grows linearly in $n$ and in $\sum_i\tau_i^2/\sigma^2$, the spread of the true means measured in units of the error variance. To find the sample size, one increases $n$ until this probability reaches $1-\beta$. Before computers, the power was read off operating characteristic charts: each **OC curve** ([3.8.2](/3.8.2)) plots $\beta$ against the parameter

$$
\Phi=\sqrt{\frac{n\sum_{i=1}^a\tau_i^2}{a\sigma^2}}=\sqrt{\lambda/a}
$$
for given numerator and denominator degrees of freedom; since $\Phi$ itself contains $n$, the charts are used iteratively. Today the probability is computed directly (in R, `pf(q, df1, df2, ncp, lower.tail = FALSE)`).

### 5.2.2. Sample Size for the Etching Experiment

Suppose the experimenter wants to detect the configuration $\mu_1=575$, $\mu_2=600$, $\mu_3=650$, $\mu_4=675$ Å/min, with $\sigma=25$ Å/min, at level $\alpha=0.01$ and with power $0.90$. The effects are $\tau_i=\mu_i-625=-50,-25,25,50$, so $\sum\tau_i^2=6250$ and $\lambda=6250n/625=10n$.

```r
true.means <- c(575, 600, 650, 675); sd <- 25
power.anova.test(groups = 4, between.var = var(true.means),
                 within.var = sd^2, sig.level = .01, power = .90)
```

```text
     Balanced one-way analysis of variance power calculation 

         groups = 4
              n = 3.520243
    between.var = 2083.333
     within.var = 625
      sig.level = 0.01
          power = 0.9

NOTE: n is number in each group
```

The argument `between.var` is the sample variance of the means, $\sum_i(\mu_i-\bar\mu)^2/(a-1)=6250/3=2083.33$, with divisor $a-1$, not $a$; internally R uses $\lambda=(a-1)\,n\cdot\text{between.var}/\text{within.var}$, which is the same $\lambda=n\sum\tau_i^2/\sigma^2$. Supplying a variance with divisor $a$ would understate the effect. The solution $n=3.52$ is not an integer and must be rounded up: with $n=4$ wafers per level the power is $0.962$ (with $n=3$ it would be only $0.753$).

Often the experimenter cannot specify all the means, only the smallest difference between the largest and the smallest mean that is worth detecting, $\Delta=\max_i\mu_i-\min_i\mu_i$. The power depends on the means only through $\sum\tau_i^2$, and a guarantee for every configuration with range $\Delta$ is obtained from the least favorable one.

**Proposition 5.2.1** Among all means $\mu_1,\dots,\mu_a$ with $\max_i\mu_i-\min_i\mu_i=\Delta$,

$$
\min\sum_{i=1}^a\tau_i^2=\min\sum_{i=1}^a(\mu_i-\bar\mu)^2=\frac{\Delta^2}{2},
$$
attained when one mean is $\bar\mu+\Delta/2$, one is $\bar\mu-\Delta/2$, and all others equal $\bar\mu$.

**Proof** Let $u=\max_i\mu_i$ and $v=\min_i\mu_i$. Dropping the other terms, $\sum_i(\mu_i-\bar\mu)^2\ge(u-\bar\mu)^2+(v-\bar\mu)^2$. For any real $c$, $(u-c)^2+(v-c)^2=\frac{(u-v)^2}{2}+2\big(c-\frac{u+v}{2}\big)^2\ge\frac{\Delta^2}{2}$. Equality holds in both steps when the remaining means equal $\bar\mu$ and $\bar\mu=(u+v)/2$, which is consistent: the means $\bar\mu\pm\Delta/2$ and $a-2$ copies of $\bar\mu$ do have average $\bar\mu$. $\square$

So a sample size computed with $\sum\tau_i^2=\Delta^2/2$ ensures power at least $1-\beta$ whenever the range of the true means is at least $\Delta$. For the etching problem with $\Delta=75$, $\sum\tau_i^2=2812.5$ (the "SS Means" reported by Minitab) and $\lambda=4.5n$. With $\alpha=0.01$ and $\sigma=25$ the power is $0.805$ for $n=5$ and $0.915$ for $n=6$, so six wafers per level are needed: more than the four found above, because the least favorable configuration spreads the means less.

![Left: power of the F-test against the number of replicates per level, for the specified means and for the least favorable configuration with range 75, at alpha 0.05 and 0.01. Right: central and noncentral F densities with 3 and 12 degrees of freedom for n = 4, with the critical value at alpha 0.01; the shaded area is the power](./plots/anova-power.py)

## 5.3. The One-Way Random-Effects Model

### 5.3.1. Fixed and Random Factors

So far the $a$ levels of the factor were chosen deliberately, and they were the only levels of interest: four specific RF power settings. Conclusions concerned these levels and their means.

**Definition 5.3.1 (Fixed-Effects Model)** The one-way **fixed-effects model** is

$$
Y_{ij}=\mu+\tau_i+\varepsilon_{ij},\qquad i=1,\dots,a,\quad j=1,\dots,n_i,\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
where $\mu$ and the treatment effects $\tau_1,\dots,\tau_a$ are unknown constants subject to a constraint such as $\sum_i\tau_i=0$. The hypothesis of no treatment effect is $H_0\colon\tau_1=\cdots=\tau_a=0$, and the inferences apply to these $a$ levels only.

Now consider a different situation. A textile company weaves a fabric on a large number of looms, and the looms should be homogeneous so that the fabric has uniform strength. The process engineer suspects that besides the usual variation in strength within samples from the same loom, there may be significant variation between looms. To investigate this, she selects four looms at random and makes four strength determinations on the fabric from each:

| Loom | Observations | $y_{i\cdot}$ | $\bar y_{i\cdot}$ |
|---|---|---|---|
| 1 | 98, 97, 99, 96 | 390 | 97.50 |
| 2 | 91, 90, 93, 92 | 366 | 91.50 |
| 3 | 96, 95, 97, 95 | 383 | 95.75 |
| 4 | 95, 96, 99, 98 | 388 | 97.00 |
| | | $y_{\cdot\cdot}=1527$ | $\bar y_{\cdot\cdot}=95.44$ |

The four looms are of no interest in themselves; they stand for the whole population of looms in the plant, and the question is how much the looms of that population vary.

**Definition 5.3.2 (Fixed and Random Factors)** A factor is a **fixed factor** if its levels are chosen deliberately and the conclusions concern only those levels. It is a **random factor** if its levels in the experiment are a random sample from a larger population of possible levels and the conclusions are to be extended to that population.

**Definition 5.3.3 (Random-Effects Model)** The one-way **random-effects model** is

$$
Y_{ij}=\mu+\tau_i+\varepsilon_{ij},\qquad i=1,\dots,a,\quad j=1,\dots,n,
$$
where $\mu$ is a constant (the overall mean), $\tau_i\sim\mathcal{N}(0,\sigma_\tau^2)$ is the random effect of the $i$-th level, $\varepsilon_{ij}\sim\mathcal{N}(0,\sigma^2)$ is the experimental error, and all $\tau_i$ and $\varepsilon_{ij}$ are independent. The variances $\sigma_\tau^2$ and $\sigma^2$ are called the between-treatment and within-treatment **variance components**.

The model looks identical to the fixed-effects model, and the arithmetic of the ANOVA table is the same; what differs is the meaning of $\tau_i$. Here the $\tau_i$ are random variables, not parameters: the parameters are $\mu$, $\sigma_\tau^2$ and $\sigma^2$, three numbers regardless of how many levels are sampled. There is no constraint $\sum_i\tau_i=0$, since a sample of four random effects does not sum to zero. Since $\operatorname{Var}(Y_{ij})=\sigma_\tau^2+\sigma^2$, the total variance of an observation splits into a part due to the level and a part due to the error, which is why the analysis is also called a components-of-variance analysis.

**Definition 5.3.4 (Intraclass Correlation Coefficient)** In the random-effects model, the **intraclass correlation coefficient** is

$$
\rho_I=\frac{\sigma_\tau^2}{\sigma_\tau^2+\sigma^2},
$$
the proportion of the variance of an observation that is due to variation between levels. It equals the correlation between two observations at the same level (Section 5.3.2).

An intraclass correlation near $1$ means that observations at the same level are nearly alike and the levels differ greatly; near $0$, the levels hardly matter compared with the within-level noise. In the loom example, $\rho_I$ measures how much of the variability of fabric strength could be removed by making the looms uniform.

### 5.3.2. The Covariance Structure of the Observations

In the fixed-effects model the observations are independent with covariance matrix $\sigma^2I_N$. In the random-effects model they are not independent. For two observations at the same level $i$ and $j\ne j'$,

$$
\operatorname{Cov}(Y_{ij},Y_{ij'})=\operatorname{Cov}(\tau_i+\varepsilon_{ij},\tau_i+\varepsilon_{ij'})=\operatorname{Var}(\tau_i)=\sigma_\tau^2,
$$
while observations at different levels share no random term and are uncorrelated. Hence

$$
\operatorname{Var}(Y_{ij})=\sigma_\tau^2+\sigma^2,\qquad \operatorname{Corr}(Y_{ij},Y_{ij'})=\frac{\sigma_\tau^2}{\sigma_\tau^2+\sigma^2}=\rho_I\quad(j\ne j'),\qquad \operatorname{Cov}(Y_{ij},Y_{i'j'})=0\quad(i\ne i').
$$
Stacking the observations level by level, $\boldsymbol{Y}$ has a **multivariate normal distribution** $\mathcal{N}_N(\mu\boldsymbol{1}_N,\Sigma)$ with the block diagonal covariance matrix

$$
\Sigma=\begin{bmatrix}\Sigma_0&&\\&\ddots&\\&&\Sigma_0\end{bmatrix}=I_a\otimes\Sigma_0,\qquad \Sigma_0=\sigma^2I_n+\sigma_\tau^2\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}=\begin{bmatrix}\sigma_\tau^2+\sigma^2&\sigma_\tau^2&\cdots&\sigma_\tau^2\\ \sigma_\tau^2&\sigma_\tau^2+\sigma^2&\cdots&\sigma_\tau^2\\ \vdots&&\ddots&\vdots\\ \sigma_\tau^2&\sigma_\tau^2&\cdots&\sigma_\tau^2+\sigma^2\end{bmatrix}.
$$
Each block has equal variances on the diagonal and equal covariances off it (compound symmetry). So the observations in the random-effects model are not independent: they are exchangeable within a level and independent across levels. Independence holds only in the special case $\sigma_\tau^2=0$. The same structure reappears in repeated measurements on the same subject and in clustered sampling.

### 5.3.3. The Test of $\sigma_\tau^2=0$

In the fixed-effects model we test whether the particular treatment means are equal. With a random factor the interest is in the population of levels, and the natural hypotheses are

$$
H_0\colon\sigma_\tau^2=0\qquad\text{versus}\qquad H_1\colon\sigma_\tau^2>0.
$$
If $\sigma_\tau^2=0$, all random effects are $0$ with probability one and there is no variability between levels. The ANOVA identity $\mathrm{SS}_{\mathrm{T}}=\mathrm{SS}_{\mathrm{Tr}}+\mathrm{SS}_{\mathrm{E}}$ is purely algebraic and still holds; what changes are the expected mean squares.

**Theorem 5.3.1 (Expected Mean Squares in the Random-Effects Model)** In the balanced one-way random-effects model,

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+n\sigma_\tau^2,\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2.
$$
Moreover $\mathrm{SS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{N-a}$ and $\mathrm{SS}_{\mathrm{Tr}}/(\sigma^2+n\sigma_\tau^2)\sim\chi^2_{a-1}$, and the two are independent.

**Proof** Within level $i$, $Y_{ij}-\bar Y_{i\cdot}=\varepsilon_{ij}-\bar\varepsilon_{i\cdot}$ does not involve $\tau_i$, so $\mathrm{SS}_{\mathrm{E}}$ is the same function of the errors as in the fixed-effects model, and $\mathrm{SS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{N-a}$. For the treatment sum of squares, write $U_i=\bar Y_{i\cdot}=\mu+\tau_i+\bar\varepsilon_{i\cdot}$. The $U_i$ are independent and identically distributed $\mathcal{N}(\mu,\sigma_\tau^2+\sigma^2/n)$, and

$$
\mathrm{SS}_{\mathrm{Tr}}=n\sum_{i=1}^a(\bar Y_{i\cdot}-\bar Y_{\cdot\cdot})^2=n\sum_{i=1}^a(U_i-\bar U)^2 .
$$
By the theory of the sample variance of a normal sample, $\sum_i(U_i-\bar U)^2/(\sigma_\tau^2+\sigma^2/n)\sim\chi^2_{a-1}$; multiplying by $n$ gives the claim for $\mathrm{SS}_{\mathrm{Tr}}/(\sigma^2+n\sigma_\tau^2)$, and in particular $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=n(\sigma_\tau^2+\sigma^2/n)=\sigma^2+n\sigma_\tau^2$. Finally, $\mathrm{SS}_{\mathrm{Tr}}$ is a function of the level means $\bar\varepsilon_{i\cdot}$ and $\tau_i$, $\mathrm{SS}_{\mathrm{E}}$ a function of the deviations $\varepsilon_{ij}-\bar\varepsilon_{i\cdot}$, which are independent of the $\bar\varepsilon_{i\cdot}$ (normal samples) and of the $\tau_i$. $\square$

It is tempting to obtain Theorem 5.3.1 from the fixed-effects result $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+n\sum_i\tau_i^2/(a-1)$ of [3.8.3](/3.8.3) by conditioning on the $\tau_i$ and then taking expectations, $\mathbb{E}\big[n\sum_i\tau_i^2/(a-1)\big]=na\sigma_\tau^2/(a-1)$. This gives the wrong coefficient $na/(a-1)$ instead of $n$. The flaw is that the fixed-effects formula uses the constraint $\sum_i\tau_i=0$, which the random effects do not satisfy. Conditioning on the $\tau_i$ correctly gives

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}\mid\tau_1,\dots,\tau_a]=\sigma^2+\frac{n}{a-1}\sum_{i=1}^a(\tau_i-\bar\tau)^2,
$$
and since $\mathbb{E}\sum_i(\tau_i-\bar\tau)^2=(a-1)\sigma_\tau^2$, the **law of total variance** route, or plain iterated expectation, yields $\sigma^2+n\sigma_\tau^2$.

Under $H_0$ both mean squares estimate $\sigma^2$; under $H_1$ the treatment mean square is larger. The test statistic is therefore the same as in the fixed-effects model,

$$
F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\ \overset{H_0}{\sim}\ F_{a-1,N-a},
$$
and $H_0$ is rejected when $F_0>F_{a-1,N-a,\alpha}$. The difference lies in the alternative: by Theorem 5.3.1, in general

$$
F_0\sim\frac{\sigma^2+n\sigma_\tau^2}{\sigma^2}\,F_{a-1,N-a},
$$
a multiple of a central $F$ variable rather than a noncentral $F$. The power of the random-effects test is thus $\mathbb{P}\big(F_{a-1,N-a}>F_{a-1,N-a,\alpha}/(1+n\sigma_\tau^2/\sigma^2)\big)$, computed from the central $F$-distribution.

For unbalanced designs with $n_i$ observations at level $i$, $\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2$ still, and $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+n_0\sigma_\tau^2$ with $n_0=\big(N-\sum_in_i^2/N\big)/(a-1)$, which equals $n$ when all $n_i=n$; but $\mathrm{SS}_{\mathrm{Tr}}$ is then no longer a scaled $\chi^2$ variable, and the exact results of this section hold only approximately.

### 5.3.4. Estimating the Variance Components

The simplest estimates equate the observed mean squares to their expectations and solve:

$$
\hat\sigma^2=\mathrm{MS}_{\mathrm{E}},\qquad \hat\sigma_\tau^2=\frac{\mathrm{MS}_{\mathrm{Tr}}-\mathrm{MS}_{\mathrm{E}}}{n}.
$$
This is the analysis of variance method. The estimators are unbiased, need no distributional assumption beyond the moments, and in balanced designs they are the minimum-variance unbiased quadratic estimators under normality. The intraclass correlation is estimated by $\hat\rho_I=\hat\sigma_\tau^2/(\hat\sigma_\tau^2+\hat\sigma^2)$.

The method has a weakness: $\hat\sigma_\tau^2$ is negative whenever $\mathrm{MS}_{\mathrm{Tr}}<\mathrm{MS}_{\mathrm{E}}$, that is, whenever $F_0<1$, which happens with substantial probability when $\sigma_\tau^2$ is small (under $H_0$, with probability $\mathbb{P}(F_{a-1,N-a}<1)$, often around one half). A variance cannot be negative. The usual responses are:

- take $\hat\sigma_\tau^2=0$, accepting a biased estimator; $F_0<1$ is consistent with $H_0\colon\sigma_\tau^2=0$;
- use an estimation method that respects the parameter space, such as restricted maximum likelihood (Section 5.3.5), which gives a nonnegative estimate;
- treat a large negative estimate as evidence against the model: the errors may be correlated within levels in a way the model does not describe (for example a negative correlation induced by the measurement process), or the variances may differ across levels.

### 5.3.5. Example: The Fiber Strength Data in R

The ANOVA of the loom data:

```r
summary(aov(Obs ~ Loom, data = LoomData))
```

```text
            Df Sum Sq Mean Sq F value   Pr(>F)    
Loom         3  89.19  29.729   15.68 0.000188 ***
Residuals   12  22.75   1.896                     
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

Each entry has its usual meaning: $\mathrm{SS}_{\mathrm{Tr}}=4\sum_i(\bar y_{i\cdot}-95.4375)^2=89.19$ on $a-1=3$ degrees of freedom, $\mathrm{SS}_{\mathrm{E}}=22.75$ on $N-a=12$, the mean squares $29.729$ and $1.896$, $F_0=29.729/1.896=15.68$, and the $p$-value $\mathbb{P}(F_{3,12}>15.68)=0.000188$. The interpretation changes: we reject $H_0\colon\sigma_\tau^2=0$ and conclude that the looms in the plant (not only these four) differ significantly in strength. The variance components are

$$
\hat\sigma^2=1.896,\qquad \hat\sigma_\tau^2=\frac{29.729-1.896}{4}=6.958,\qquad \hat\sigma_y^2=\hat\sigma_\tau^2+\hat\sigma^2=8.854,\qquad \hat\rho_I=\frac{6.958}{8.854}=0.786 .
$$
About $79\%$ of the variance of fabric strength is attributable to differences between looms: the process engineer should look for the causes of the loom-to-loom variation (set-up, maintenance, operator training), since reducing it would make the fabric much more uniform.

The same data can be fitted as a regression with the loom as a factor:

```r
summary(lm(Obs ~ Loom, data = LoomData))
```

```text
Call:
lm(formula = Obs ~ Loom, data = LoomData)

Residuals:
    Min      1Q  Median      3Q     Max 
-2.0000 -0.8125 -0.1250  1.0625  2.0000 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  97.5000     0.6884 141.623  < 2e-16 ***
Loom2        -6.0000     0.9736  -6.163 4.85e-05 ***
Loom3        -1.7500     0.9736  -1.797   0.0975 .  
Loom4        -0.5000     0.9736  -0.514   0.6169    

Residual standard error: 1.377 on 12 degrees of freedom
Multiple R-squared:  0.7968,	Adjusted R-squared:  0.746 
F-statistic: 15.68 on 3 and 12 DF,  p-value: 0.0001878
```

This is the fixed-effects analysis in R's default treatment-contrast coding ([3.8.3](/3.8.3)): the intercept $97.5$ is the mean of loom 1, the baseline, and the coefficients `Loom2`, `Loom3`, `Loom4` are the differences $\bar y_{i\cdot}-\bar y_{1\cdot}$, namely $91.5-97.5=-6$, $-1.75$ and $-0.5$. The standard errors are $\sqrt{\mathrm{MS}_{\mathrm{E}}/n}=\sqrt{1.896/4}=0.6884$ for a level mean and $\sqrt{2\,\mathrm{MS}_{\mathrm{E}}/n}=0.9736$ for a difference of two means. The residual standard error is $\sqrt{\mathrm{MS}_{\mathrm{E}}}=1.377$ on 12 degrees of freedom, $R^2=\mathrm{SS}_{\mathrm{Tr}}/\mathrm{SS}_{\mathrm{T}}=89.19/111.94=0.797$, and the overall $F$-statistic $15.68$ on 3 and 12 degrees of freedom is the ANOVA $F_0$. These numbers describe the four particular looms; for a random factor the individual coefficients have no lasting meaning, but the $F$-test is the same.

The random-effects model is fitted with the function `lmer` of the package `lme4`, where `(1 | Loom)` declares a random intercept for each level of the grouping factor `Loom`:

```r
library(lme4)
summary(lmer(Obs ~ (1 | Loom), data = LoomData))
```

```text
Linear mixed model fit by REML ['lmerMod']
Formula: Obs ~ 1 + (1 | Loom)
   Data: LoomData

REML criterion at convergence: 63.2

Scaled residuals: 
     Min       1Q   Median       3Q      Max 
-1.38018 -0.57260 -0.04342  0.82574  1.52491 

Random effects:
 Groups   Name        Variance Std.Dev.
 Loom     (Intercept) 6.958    2.638   
 Residual             1.896    1.377   
Number of obs: 16, groups:  Loom, 4

Fixed effects:
            Estimate Std. Error t value
(Intercept)   95.438      1.363   70.01
```

`lmer` does not use the ANOVA method; it maximizes the restricted likelihood.

**Definition 5.3.5 (Restricted Maximum Likelihood)** For a linear model $\boldsymbol{Y}\sim\mathcal{N}_N(X\boldsymbol{\beta},\Sigma(\boldsymbol{\theta}))$ whose covariance matrix depends on variance parameters $\boldsymbol{\theta}$, and $X$ of rank $p$, the **restricted maximum likelihood** (REML) estimate of $\boldsymbol{\theta}$ maximizes the likelihood of $N-p$ linearly independent error contrasts $K^{\mathsf T}\boldsymbol{Y}$ with $K^{\mathsf T}X=O$, whose distribution does not involve $\boldsymbol{\beta}$. Up to a constant, $-2$ times this restricted log-likelihood is

$$
\ln\det\Sigma+\ln\det(X^{\mathsf T}\Sigma^{-1}X)+(\boldsymbol{y}-X\hat{\boldsymbol{\beta}})^{\mathsf T}\Sigma^{-1}(\boldsymbol{y}-X\hat{\boldsymbol{\beta}}),\qquad \hat{\boldsymbol{\beta}}=(X^{\mathsf T}\Sigma^{-1}X)^{-1}X^{\mathsf T}\Sigma^{-1}\boldsymbol{y}.
$$

Ordinary **maximum likelihood estimation** of variance components is biased downward because it ignores the degrees of freedom used to estimate the fixed effects; the simplest case is the estimator $\frac1N\sum(y_i-\bar y)^2$ of a normal variance, whose REML counterpart is the unbiased $\frac{1}{N-1}\sum(y_i-\bar y)^2$. REML removes this bias by working with the contrasts. In balanced one-way designs, the REML estimates coincide with the ANOVA estimates whenever these are nonnegative; when $\mathrm{MS}_{\mathrm{Tr}}<\mathrm{MS}_{\mathrm{E}}$, REML sets $\hat\sigma_\tau^2=0$. For unbalanced data the two methods differ, and REML is the standard choice.

The output reads as follows.

- `REML criterion at convergence: 63.2` is $-2$ times the maximized restricted log-likelihood (including the constant $(N-p)\ln 2\pi$); it is used to compare models with the same fixed effects.
- `Scaled residuals` are the residuals $y_{ij}-\hat\mu-\tilde\tau_i$ divided by $\hat\sigma$, where $\tilde\tau_i=\frac{n\hat\sigma_\tau^2}{n\hat\sigma_\tau^2+\hat\sigma^2}(\bar y_{i\cdot}-\bar y_{\cdot\cdot})$ is the predicted random effect. The predictions shrink the deviations of the loom means toward the grand mean by the factor $27.83/29.73=0.936$, so these residuals differ slightly from the fixed-effects residuals $y_{ij}-\bar y_{i\cdot}$.
- `Random effects` lists the two variance components and their square roots: $\hat\sigma_\tau^2=6.958$ ($\hat\sigma_\tau=2.638$) for the loom intercepts and $\hat\sigma^2=1.896$ ($\hat\sigma=1.377$) for the residual, the same as the ANOVA estimates because the design is balanced and $\hat\sigma_\tau^2>0$. `Number of obs: 16, groups: Loom, 4` gives $N$ and $a$.
- `Fixed effects`: the only fixed parameter is $\mu$, estimated by the grand mean $95.4375$ (rounded to $95.438$); it can be checked as $97.5+(-6-1.75-0.5)/4=95.4375$ from the `lm` coefficients. No $p$-value is printed, because the null distribution of the $t$ value is not exactly $t$ in general mixed models.

The standard error $1.363$ of the intercept is computed from the covariance structure of Section 5.3.2. Averaging over all observations,

$$
\operatorname{Var}(\bar Y_{\cdot\cdot})=\operatorname{Var}\Big(\mu+\bar\tau+\bar\varepsilon_{\cdot\cdot}\Big)=\frac{\sigma_\tau^2}{a}+\frac{\sigma^2}{an}=\frac{\sigma^2+n\sigma_\tau^2}{N},
$$
which is estimated by $\hat\sigma_\tau^2/a+\hat\sigma^2/(an)=\mathrm{MS}_{\mathrm{Tr}}/N$:

```r
sqrt(6.958/4 + 1.896/16)    # 1.363; equivalently sqrt(29.729/16)
```

This is twice the standard error $0.6884$ of the `lm` intercept, and the comparison shows the essential difference between the models. In the fixed-effects model the only uncertainty is the measurement error, and the 16 observations average it out. In the random-effects model the target is the mean strength of all looms in the plant, and only four looms were sampled: the between-loom variance $\sigma_\tau^2$ is averaged over $a=4$ levels only, however many measurements are made on each loom. Adding replicates per loom reduces only the second term; to estimate $\mu$ precisely one must sample more looms.

![Fiber strength on four randomly chosen looms: the observations, the loom means, the grand mean with a band of plus and minus the estimated between-loom standard deviation, and plus and minus the estimated within-loom standard deviation around each loom mean](./plots/loom-random-effects.py)

### 5.3.6. Confidence Intervals for the Variance Components

The distributional results of Theorem 5.3.1 give confidence intervals.

The error variance has an exact interval: since $(N-a)\mathrm{MS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{N-a}$,

$$
\frac{(N-a)\mathrm{MS}_{\mathrm{E}}}{\chi^2_{N-a,\alpha/2}}\le\sigma^2\le\frac{(N-a)\mathrm{MS}_{\mathrm{E}}}{\chi^2_{N-a,1-\alpha/2}} .
$$
For the looms, $\chi^2_{12,0.025}=23.34$ and $\chi^2_{12,0.975}=4.404$ give $0.975\le\sigma^2\le5.166$.

For $\sigma_\tau^2$ there is no exact interval, because $\hat\sigma_\tau^2$ is a difference of two independent scaled $\chi^2$ variables,

$$
\hat\sigma_\tau^2=\frac{\mathrm{MS}_{\mathrm{Tr}}-\mathrm{MS}_{\mathrm{E}}}{n}\sim\frac{\sigma^2+n\sigma_\tau^2}{n(a-1)}\chi^2_{a-1}-\frac{\sigma^2}{n(N-a)}\chi^2_{N-a},
$$
whose distribution depends on the unknown ratio of the components. The **Satterthwaite approximation** ([3.8.2](/3.8.2)) treats it as a scaled $\chi^2$ variable, $r\hat\sigma_\tau^2/\sigma_\tau^2\overset{\cdot}{\sim}\chi^2_r$, with the degrees of freedom matched by the method of moments:

$$
r=\frac{(\mathrm{MS}_{\mathrm{Tr}}-\mathrm{MS}_{\mathrm{E}})^2}{\mathrm{MS}_{\mathrm{Tr}}^2/(a-1)+\mathrm{MS}_{\mathrm{E}}^2/(N-a)},\qquad \frac{r\hat\sigma_\tau^2}{\chi^2_{r,\alpha/2}}\le\sigma_\tau^2\le\frac{r\hat\sigma_\tau^2}{\chi^2_{r,1-\alpha/2}} .
$$
For the looms $r=2.63$, and the approximate 95% interval is $2.12\le\sigma_\tau^2\le130$: with only four looms, the between-loom variance is very poorly determined, even though its existence is clearly established by the $F$-test. The approximation is rough when $r$ is small; profile-likelihood intervals from REML (`confint` of an `lmer` fit) or Bayesian intervals ([3.7.6](/3.7.6)) are alternatives.

Ratios of the components do have exact intervals. By Theorem 5.3.1,

$$
\frac{\mathrm{MS}_{\mathrm{Tr}}/(\sigma^2+n\sigma_\tau^2)}{\mathrm{MS}_{\mathrm{E}}/\sigma^2}\sim F_{a-1,N-a},
$$
so with probability $1-\alpha$

$$
F_{a-1,N-a,1-\alpha/2}\le\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\cdot\frac{\sigma^2}{\sigma^2+n\sigma_\tau^2}\le F_{a-1,N-a,\alpha/2}.
$$
Solving for $\sigma_\tau^2/\sigma^2$ gives the interval $[L,U]$ with

$$
L=\frac1n\left(\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\cdot\frac{1}{F_{a-1,N-a,\alpha/2}}-1\right),\qquad U=\frac1n\left(\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\cdot\frac{1}{F_{a-1,N-a,1-\alpha/2}}-1\right),
$$
where the lower quantile can be computed as $F_{a-1,N-a,1-\alpha/2}=1/F_{N-a,a-1,\alpha/2}$. Since $\rho_I=\frac{\sigma_\tau^2/\sigma^2}{1+\sigma_\tau^2/\sigma^2}$ is an increasing function of the ratio,

$$
\frac{L}{1+L}\le\frac{\sigma_\tau^2}{\sigma_\tau^2+\sigma^2}\le\frac{U}{1+U}
$$
is an exact $1-\alpha$ interval for the intraclass correlation (a negative $L$ is replaced by $0$). For the looms, $F_0=15.68$, $F_{3,12,0.025}=4.474$ and $F_{3,12,0.975}=0.0698$, so $L=0.626$, $U=55.95$, and $0.385\le\rho_I\le0.982$. Even at the lower end, more than a third of the variance is due to the looms.

### 5.3.7. Fixed or Random?

Whether a factor should be treated as fixed or random has little to do with the variable itself and a lot to do with the research question. Fixed effects are factors whose effect on the response is the object of study: we want conclusions about how these particular levels affect $Y$. Random effects are typically grouping factors that we need to account for but whose individual levels are not of interest (looms, batches, laboratories, subjects, fields); the levels in the data are a sample, and the results are generalized to the population of levels from which they were drawn, which requires that the sample be representative.

**Example 5.3.1** How accurate are laboratories at testing for a certain disease, and do laboratories differ in their accuracy? Different people are tested at 3 laboratories; the factor is the laboratory ($i=1,2,3$), the experimental unit is a person having a test, and $y_{ij}$ is the accuracy rating of the test for person $j$ at laboratory $i$. If we care only about these 3 laboratories (for example, to decide which of them a hospital should contract), the laboratory is a fixed effect. If the 3 laboratories are a random sample of all such laboratories and we care about laboratories in general (how much does accuracy vary from laboratory to laboratory?), it is a random effect.

| | Fixed-effects model | Random-effects model |
|---|---|---|
| Levels | chosen deliberately; the only ones of interest | random sample from a population of levels |
| $\tau_i$ | unknown constants | random variables, $\tau_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma_\tau^2)$, independent of the errors |
| Parameters | $\mu,\tau_1,\dots,\tau_a,\sigma^2$ ($a+1$ free) | $\mu,\sigma_\tau^2,\sigma^2$ (3, whatever $a$ is) |
| Constraint | $\sum_i\tau_i=0$ (or a baseline) | none |
| $\mathbb{E}[Y_{ij}]$, $\operatorname{Var}(Y_{ij})$ | $\mu+\tau_i$, $\sigma^2$ | $\mu$, $\sigma_\tau^2+\sigma^2$ |
| $\operatorname{Cov}(\boldsymbol{Y})$ | $\sigma^2I_N$: independent observations | $I_a\otimes(\sigma^2I_n+\sigma_\tau^2\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T})$: correlated within levels |
| $H_0$ | $\tau_1=\cdots=\tau_a=0$ | $\sigma_\tau^2=0$ |
| $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]$ | $\sigma^2+n\sum_i\tau_i^2/(a-1)$ | $\sigma^2+n\sigma_\tau^2$ |
| $F_0$ under $H_1$ | noncentral $F_{a-1,N-a}(\lambda)$ | $(1+n\sigma_\tau^2/\sigma^2)\,F_{a-1,N-a}$ |
| Estimation targets | treatment means, contrasts, multiple comparisons | variance components, $\rho_I$, the population mean $\mu$ |
| Scope of conclusions | these $a$ levels | the whole population of levels |

:::

The random-effects model is the frequentist counterpart of a **hierarchical model** ([3.7.6](/3.7.6)): there the group effects are given a common prior distribution whose parameters are estimated or given a hyperprior, and the posterior means of the group effects are shrunken toward the overall mean, just like the predicted random effects $\tilde\tau_i$ of `lmer`. Models with both fixed and random factors, mixed models, appear in the later chapters on blocking and multifactor designs.

## 5.4. The Regression Approach for a Quantitative Factor

### 5.4.1. Quantitative and Qualitative Factors

**Definition 5.4.1 (Quantitative and Qualitative Factors)** A factor is a **quantitative factor** if its levels are values of a numerical variable on an interval scale, such as a temperature, a pressure or the RF power, so that differences and distances between levels are meaningful. A factor is a **qualitative factor** (categorical factor) if its levels are categories without a numerical scale, such as types of material, operators or suppliers.

The fixed-effects model treats all factors as qualitative: the effects $\tau_1,\dots,\tau_a$ are unrelated parameters, and permuting the labels of the levels does not change the analysis. For a quantitative factor this ignores information. With the etching experiment, where the levels are $160$, $180$, $200$, $220$ W, the natural goals are to describe how the etch rate depends on the power, to predict the rate at untested settings, and to find the best setting; these call for a regression model in the power $x$. Such regression models are empirical rather than mechanistic: they approximate an unknown smooth relationship over the experimental region and should not be extrapolated far beyond it.

As a regression, the fixed-effects model of the etching experiment with the constraint $\sum\tau_i=0$ is $\boldsymbol{y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ with $\boldsymbol{\beta}=(\mu,\tau_1,\tau_2,\tau_3)^{\mathsf T}$ and $\tau_4=-\tau_1-\tau_2-\tau_3$; the rows of $X$ for the four levels are

$$
\begin{bmatrix}1&1&0&0\\1&0&1&0\\1&0&0&1\\1&-1&-1&-1\end{bmatrix}\otimes\boldsymbol{1}_n
$$
(each row repeated for the $n=5$ wafers). The alternative is the simple linear regression model

$$
y_{ij}=\beta_0+\beta_1x_i+\varepsilon_{ij},\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
with design matrix rows $(1,x_i)$, fitted by least squares $\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{y}$ with $\hat\sigma^2=\boldsymbol{e}^{\mathsf T}\boldsymbol{e}/(N-p)$, $p=2$, and tested by the usual $t$-tests of $H_0\colon\beta_j=0$ and the $F$-test of $H_0\colon\beta_1=0$.

Centering the predictor simplifies both computation and interpretation. With $z_i=(x_i-\bar x)/\Delta$, where $\bar x=190$ is the center and $\Delta=10$ W half the spacing, the levels become $z=-3,-1,1,3$, and the columns $\boldsymbol{1}$ and $\boldsymbol{z}$ of the design matrix are orthogonal, because $\sum_iz_i=0$. Then $X^{\mathsf T}X$ is diagonal, the estimates of intercept and slope are uncorrelated, the intercept estimates the mean response at the center of the design, and adding or removing a term does not change the other estimates. Orthogonality is a property of the design: with equally spaced levels and equal replication, it can always be achieved by such a linear transformation.

### 5.4.2. Comparing the Two Models

```r
x <- as.numeric(as.character(Etch$Power))   # as.numeric(Etch$Power) would give 1, 2, 3, 4
summary(lm(Rate ~ x, data = Etch))          # regression model
summary(lm(Rate ~ Power, data = Etch))      # fixed-effects model
```

```text
Coefficients (regression model):
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 137.6200    41.2108   3.339  0.00365 ** 
x             2.5270     0.2154  11.731 7.26e-10 ***
Residual standard error: 21.54 on 18 degrees of freedom
Multiple R-squared:  0.8843,	Adjusted R-squared:  0.8779 
F-statistic: 137.6 on 1 and 18 DF,  p-value: 7.263e-10

Coefficients (fixed-effects model):
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  551.200      8.169  67.471  < 2e-16 ***
Power180      36.200     11.553   3.133  0.00642 ** 
Power200      74.200     11.553   6.422 8.44e-06 ***
Power220     155.800     11.553  13.485 3.73e-10 ***
Residual standard error: 18.27 on 16 degrees of freedom
Multiple R-squared:  0.9261,	Adjusted R-squared:  0.9122 
F-statistic:  66.8 on 3 and 16 DF,  p-value: 2.883e-09
```

The fitted line says that each additional watt increases the etch rate by about $2.53$ Å/min, and the intercept $137.6$ is the extrapolated rate at zero power, without physical meaning. The fixed-effects model reports the mean $551.2$ of the 160 W level and the differences of the other level means from it.

| | Regression model $y_{ij}=\beta_0+\beta_1x_i+\varepsilon_{ij}$ | Fixed-effects model $y_{ij}=\mu+\tau_i+\varepsilon_{ij}$ |
|---|---|---|
| Free parameters | 3: $\beta_0,\beta_1,\sigma^2$ | $a+1$: $\mu,\tau_1,\dots,\tau_{a-1},\sigma^2$ |
| Error degrees of freedom | $N-2=18$ | $N-a=16$ |
| SSE (etching) | $8352.5$ | $5339.2$ |
| Residual standard error | $21.54$ | $18.27$ |
| $R^2$ | $0.884$ | $0.926$ |
| Needs replicates | no: two distinct levels suffice to fit a line | yes: $\sigma^2$ is estimated from the replicates within levels |
| Prediction at other $x$ | yes (interpolation within the range) | no: only the tested levels |
| Assumption on the shape | linear in $x$; sensitive to this assumption | none |

The regression model has fewer parameters, leaves more degrees of freedom for estimating $\sigma^2$, does not need replicates and can predict between the levels. Its limitation is the assumption of linearity. Its SSE is necessarily at least as large as that of the fixed-effects model, because the regression model is nested in it: a line $\beta_0+\beta_1x_i$ is a special choice of the level means $\mu+\tau_i$, while the fixed-effects model fits each level mean freely. Whether the larger SSE matters is exactly the lack-of-fit question of [3.3.5](/3.3.5).

The error deviation of the regression model splits into a pure error deviation and a lack-of-fit deviation,

$$
y_{ij}-\hat y_{ij}=(y_{ij}-\bar y_{i\cdot})+(\bar y_{i\cdot}-\hat y_{ij}),
$$
and summing squares (the cross products vanish) gives

$$
\mathrm{SSE}=\mathrm{SSPE}+\mathrm{SSLF},\qquad N-2=(N-a)+(a-2),
$$
where the **pure error sum of squares** $\mathrm{SSPE}=\sum_{i,j}(y_{ij}-\bar y_{i\cdot})^2$ is the SSE of the fixed-effects model and the **lack-of-fit sum of squares** $\mathrm{SSLF}=\sum_in_i(\bar y_{i\cdot}-\hat y_i)^2$ measures how far the level means are from the line. The test of $H_0$: "the mean response is linear in $x$" is

$$
F_0=\frac{\mathrm{SSLF}/(a-2)}{\mathrm{SSPE}/(N-a)}\ \overset{H_0}{\sim}\ F_{a-2,N-a},
$$
which is the **general linear test** of the regression model (the reduced model) against the fixed-effects model (the full model). For the etching data, $\mathrm{SSLF}=8352.5-5339.2=3013.3$ on $2$ degrees of freedom, $F_0=1506.6/333.7=4.51$ and $p=0.028$: at the 5% level the straight line is not adequate. In R, `anova(lm(Rate ~ x), lm(Rate ~ Power))` performs this test.

### 5.4.3. Quadratic and Polynomial Models

The lack of fit suggests curvature, and the plot of the level means against the power confirms that the rate increases faster at high power. A **polynomial regression** ([3.3.10](/3.3.10)) adds a quadratic term,

$$
y_{ij}=\beta_0+\beta_1x_i+\beta_2x_i^2+\varepsilon_{ij},
$$
in which $\beta_1$ describes the linear and $\beta_2$ the quadratic effect of the factor.

```r
modf <- lm(Rate ~ x + I(x^2), data = Etch)   # or: x2 <- x^2; lm(Rate ~ x + x2)
summary(modf)
```

```text
Coefficients:
              Estimate  Std. Error t value Pr(>|t|)   
(Intercept) 1147.77000   368.52081   3.115  0.00631 **
x             -8.25550     3.91993  -2.106  0.05037 . 
I(x^2)         0.02838     0.01030   2.754  0.01356 * 

Residual standard error: 18.43 on 17 degrees of freedom
Multiple R-squared:   0.92,	Adjusted R-squared:  0.9106 
F-statistic: 97.76 on 2 and 17 DF,  p-value: 4.74e-10
```

The quadratic term is significant ($p=0.014$), $R^2$ rises to $0.920$, and the residual standard error $18.43$ is close to the $18.27$ of the fixed-effects model. The lack-of-fit test of the quadratic model, $F_0=(5776.0-5339.2)/333.7=1.31$ on 1 and 16 degrees of freedom ($p=0.27$), finds no further departure: with three parameters for the mean the quadratic fits the four level means nearly as well as the four-parameter fixed-effects model, and it can interpolate.

Should the linear term, whose $p$-value $0.050$ is borderline, be dropped from the quadratic model? No, and the $p$-value is not the right criterion. In the uncentered model, $\beta_1$ is the slope of the parabola at $x=0$, far outside the experimental range, and its $t$-test asks whether the tangent at zero power is horizontal, a question of no interest. Its value and significance change with the origin of $x$, whereas the fitted curve does not. Models with a quadratic term should keep the lower-order term (the hierarchy principle of [3.3.10](/3.3.10)): without it, the curve would be forced to have its vertex at $x=0$. In the centered parametrization the linear coefficient is highly significant.

Centering also makes the quadratic model orthogonal. With $z=(x-190)/10$, the columns $\boldsymbol{1}$, $\boldsymbol{z}$ and $\boldsymbol{z}^2-5$ (the squares centered by their mean $5$) are mutually orthogonal because the design is symmetric, and the fit becomes

$$
\hat y=617.75+25.27\,z+2.84\,(z^2-5),
$$
with $617.75$ the grand mean, and the linear coefficient unchanged from the straight-line fit $2.527\times10$. For $a$ equally spaced levels this construction continues to orthogonal polynomials of degree up to $a-1$, which split the treatment sum of squares into single-degree-of-freedom contrasts. For the etching data, with the orthogonal polynomial **contrasts** $(-3,-1,1,3)$, $(1,-1,-1,1)$ and $(-1,3,-3,1)$, the linear, quadratic and cubic components are $63857.3$, $2576.5$ and $436.8$, adding up to $\mathrm{SS}_{\mathrm{Tr}}=66870.6$; the quadratic and cubic components together make up $\mathrm{SSLF}=3013.3$ of the straight line. The cubic model with $a=4$ levels interpolates the four means exactly and is the fixed-effects model again.

![Etch rate against RF power: the observations, the level means estimated by the fixed-effects model, and the fitted linear and quadratic regression curves](./plots/etch-regression.py)

## Summary {#summary}

Checking the assumptions of the one-way model:

| Assumption | Graphical check | Formal tool | Remarks |
|---|---|---|---|
| Normality | normal probability plot of the residuals | | $F$-test robust to moderate departures |
| No outliers | scaled residuals $d_{ij}=e_{ij}/\sqrt{\mathrm{MS}_{\mathrm{E}}}$ | $\lvert d_{ij}\rvert>3$ | leverage is $1/n_i$ (Proposition 5.1.1) |
| Independence | residuals against run order or time | | protected by randomization |
| Equal variances | residuals against fitted values | Bartlett (sensitive to non-normality), Levene / Brown–Forsythe (robust) | if violated: transform, weight, or Welch's ANOVA (Definition 5.1.2) |

Power and sample size: $F_0\sim F_{a-1,N-a}(\lambda)$ with $\lambda=n\sum\tau_i^2/\sigma^2$ (Theorem 5.2.1); `power.anova.test` uses `between.var` $=\sum\tau_i^2/(a-1)$; if only the range $\Delta$ is specified, use $\sum\tau_i^2=\Delta^2/2$ (Proposition 5.2.1); round $n$ up.

Fixed versus random effects, with the same ANOVA table:

| Source | df | MS | $\mathbb{E}[\mathrm{MS}]$, fixed | $\mathbb{E}[\mathrm{MS}]$, random |
|---|---|---|---|---|
| Treatments | $a-1$ | $\mathrm{MS}_{\mathrm{Tr}}$ | $\sigma^2+\dfrac{n\sum_i\tau_i^2}{a-1}$ | $\sigma^2+n\sigma_\tau^2$ |
| Error | $N-a$ | $\mathrm{MS}_{\mathrm{E}}$ | $\sigma^2$ | $\sigma^2$ |
| Total | $N-1$ | | | |

- Random effects: $H_0\colon\sigma_\tau^2=0$, the same $F_0=\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}$; $\hat\sigma^2=\mathrm{MS}_{\mathrm{E}}$, $\hat\sigma_\tau^2=(\mathrm{MS}_{\mathrm{Tr}}-\mathrm{MS}_{\mathrm{E}})/n$ (truncate at $0$ or use REML), $\hat\rho_I=\hat\sigma_\tau^2/(\hat\sigma_\tau^2+\hat\sigma^2)$.
- Observations within a level are correlated with correlation $\rho_I$ (compound symmetry); $\operatorname{Var}(\bar Y_{\cdot\cdot})=\sigma_\tau^2/a+\sigma^2/(an)$, estimated by $\mathrm{MS}_{\mathrm{Tr}}/N$.
- Intervals: exact for $\sigma^2$ ($\chi^2_{N-a}$) and for $\sigma_\tau^2/\sigma^2$ and $\rho_I$ ($F_{a-1,N-a}$); approximate (Satterthwaite) for $\sigma_\tau^2$.
- The choice depends on the research question: conclusions about these levels (fixed) or about a population of levels (random).

For a quantitative factor, the regression model ($3$ free parameters, $N-2$ error df, interpolation, no replicates needed) is nested in the fixed-effects model ($a+1$ parameters, smaller SSE); $\mathrm{SSE}=\mathrm{SSPE}+\mathrm{SSLF}$ gives the lack-of-fit test on $a-2$ and $N-a$ degrees of freedom; add polynomial terms while keeping lower-order terms, preferably in centered or orthogonal form.

## Questions

1. A one-way random-effects ANOVA gave the following table: Treatment, df $3$, SS $80$; Error, df $24$, SS $120$; Total, df $27$, SS $200$. Complete the mean squares and estimate $\sigma^2$, $\sigma_\tau^2$ and the intraclass correlation. Is $\sigma_\tau^2$ significantly positive at $\alpha=0.05$?

   **Answer** $a=4$ and $N=28$, so $n=7$. $\mathrm{MS}_{\mathrm{Tr}}=80/3=26.67$, $\mathrm{MS}_{\mathrm{E}}=120/24=5$ (and $\mathrm{SS}_{\mathrm{T}}/27=7.41$, the sample variance of all observations, which is not used). Then $\hat\sigma^2=5$, $\hat\sigma_\tau^2=(26.67-5)/7=3.10$, and $\hat\rho_I=3.10/8.10=0.38$. $F_0=26.67/5=5.33$ exceeds $F_{3,24,0.05}=3.01$ ($p\approx0.006$), so we reject $H_0\colon\sigma_\tau^2=0$.

2. In the random-effects model, show that the observations are not independent, and compute $\operatorname{Var}(\bar Y_{i\cdot})$ and $\operatorname{Var}(\bar Y_{\cdot j})$, where $\bar Y_{\cdot j}=\frac1a\sum_iY_{ij}$ averages the $j$-th observation over the levels.

   **Answer** $\operatorname{Cov}(Y_{ij},Y_{ij'})=\sigma_\tau^2$ for $j\ne j'$, which is nonzero unless $\sigma_\tau^2=0$; since the observations are jointly normal, they are independent only when $\sigma_\tau^2=0$. $\bar Y_{i\cdot}=\mu+\tau_i+\bar\varepsilon_{i\cdot}$ has variance $\sigma_\tau^2+\sigma^2/n$: the level effect is not averaged out within a level. $\bar Y_{\cdot j}=\mu+\bar\tau+\frac1a\sum_i\varepsilon_{ij}$ has variance $(\sigma_\tau^2+\sigma^2)/a$, because it averages over $a$ independent levels.

3. For each situation, decide whether the factor should be fixed or random. (a) A pharmaceutical company compares its three candidate formulations of a drug. (b) Five batches of raw material are sampled from a supplier's production to assess batch-to-batch variability. (c) An agronomist compares four specific fertilizers in the fields of one farm.

   **Answer** (a) Fixed: the three formulations are the only ones of interest, and the goal is to compare them. (b) Random: the batches are a sample, and the target is the variance component of the population of batches. (c) The fertilizer is fixed. If the fields were also a factor (as blocks, sampled to represent the region), the field would be random; the answer depends on the question, not on the variable.

4. Why does the random-effects intercept in the loom example have standard error $1.363$, while the `lm` intercept has $0.688$? What would reduce the first one most effectively?

   **Answer** The `lm` intercept estimates the mean of loom 1, whose only uncertainty is the measurement error: $\sqrt{\hat\sigma^2/4}=0.688$. The `lmer` intercept estimates the mean strength $\mu$ of all looms, and $\operatorname{Var}(\bar Y_{\cdot\cdot})=\sigma_\tau^2/a+\sigma^2/(an)$ includes the variation between the sampled looms: $\sqrt{6.958/4+1.896/16}=\sqrt{\mathrm{MS}_{\mathrm{Tr}}/N}=1.363$. Increasing $n$ only reduces the second term ($0.118$ of the total $1.858$); since the first term dominates, sampling more looms (increasing $a$) is much more effective.

5. A balanced one-way fixed-effects experiment with $a=5$ levels is planned with $\sigma=4$, $\alpha=0.05$ and target power $0.90$. The experimenter wants to detect any configuration in which the largest and smallest means differ by $\Delta=8$. Which value of `between.var` should be given to `power.anova.test`, and why does this guarantee the power for all such configurations?

   **Answer** The least favorable configuration has $\sum\tau_i^2=\Delta^2/2=32$ (Proposition 5.2.1), so `between.var` $=32/(a-1)=8$ and `within.var` $=16$. The power is increasing in $\lambda=n\sum\tau_i^2/\sigma^2$, and every configuration with range at least $\Delta$ has $\sum\tau_i^2\ge\Delta^2/2$, so its power is at least the power computed for the least favorable one. (The resulting $n$, about $8.7$, is rounded up to $9$ per level; with $n=8$ the power would be $0.866$.)

6. For the etching data, count the free parameters of the linear regression model and of the fixed-effects model, and explain which has the smaller SSE. Then carry out the lack-of-fit test of the linear model from the two R outputs alone.

   **Answer** The regression model has 3 free parameters ($\beta_0,\beta_1,\sigma^2$), the fixed-effects model $a+1=5$ ($\mu,\tau_1,\tau_2,\tau_3,\sigma^2$). The fixed-effects model has the smaller SSE, because the regression model is a special case of it (level means on a line). From the outputs, $\mathrm{SSE}_{\mathrm{reg}}=18\times21.54^2=8352$ and $\mathrm{SSPE}=16\times18.27^2=5339$, so $\mathrm{SSLF}=3013$ on $18-16=2$ degrees of freedom and $F_0=(3013/2)/(5339/16)=4.51>F_{2,16,0.05}=3.63$ ($p=0.028$): the straight line shows significant lack of fit.

7. Show that for $a=2$ levels, Welch's ANOVA statistic equals the square of Welch's $t$ statistic, and that $\nu$ equals the Welch–Satterthwaite degrees of freedom.

   **Answer** With $v_i=s_i^2/n_i=1/w_i$, $\bar y'=(w_1\bar y_1+w_2\bar y_2)/(w_1+w_2)$ and the numerator is $w_1(\bar y_1-\bar y')^2+w_2(\bar y_2-\bar y')^2=\frac{w_1w_2}{w_1+w_2}(\bar y_1-\bar y_2)^2=\frac{(\bar y_1-\bar y_2)^2}{v_1+v_2}=t^2$. For $a=2$ the correction factor in the denominator is $1+0=1$, so $F_0^*=t^2$. Further $1-w_1/w=v_1/(v_1+v_2)$ and $1-w_2/w=v_2/(v_1+v_2)$, so $\Lambda=\frac{v_1^2/(n_1-1)+v_2^2/(n_2-1)}{(v_1+v_2)^2}$ and $\nu=3/(3\Lambda)=\frac{(v_1+v_2)^2}{v_1^2/(n_1-1)+v_2^2/(n_2-1)}$, the Welch–Satterthwaite formula.
