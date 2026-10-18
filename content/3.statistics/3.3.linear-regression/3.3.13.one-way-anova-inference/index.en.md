---
title: Inference for One-Way Analysis of Variance
description: The cell means and factor effects models as regressions on indicator variables, identifiability and constraints; the F-test as a general linear test; confidence intervals for level means; the multiplicity problem and the LSD, Bonferroni, Tukey and Scheffé procedures; linear combinations, contrasts and contrast sums of squares.
---

The previous chapter introduced the two models of single-factor analysis of variance, the cell means model $Y_{ij}=\mu_i+\varepsilon_{ij}$ and the factor effects model $Y_{ij}=\mu+\tau_i+\varepsilon_{ij}$ ([3.3.12](/3.3.12)). This chapter first writes both as linear regressions, with explicit **design matrix**, and shows why the factor effects model needs a constraint. It then carries out inference: the $F$-test of equal means as a **general linear test** ([3.3.9](/3.3.9)), confidence intervals for the level means, and the step that follows a rejection, namely finding out which means differ. Comparing many pairs of means raises the multiplicity problem already met in the **Bonferroni correction** ([3.2.4](/3.2.4)); we compare the standard procedures that control the **family-wise error rate**, the topic taken up again for large numbers of tests in [3.4.12](/3.4.12). Contrasts, the linear combinations that express research questions about the means, close the chapter. Two factors follow in [3.3.14](/3.3.14).

## 13.1. One-Way ANOVA as a Regression Model

### 13.1.1. The Cell Means Model

Order the observations by level, so that the first $n_1$ observations are from level $1$, the next $n_2$ from level $2$, and so on. The cell means model $Y_{ij}=\mu_i+\varepsilon_{ij}$ is the regression $\boldsymbol{Y}=X\boldsymbol\beta+\boldsymbol\varepsilon$ with $r$ indicator columns and no intercept:

$$
X=\begin{bmatrix}\boldsymbol{1}_{n_1}&\boldsymbol{0}&\cdots&\boldsymbol{0}\\\boldsymbol{0}&\boldsymbol{1}_{n_2}&\cdots&\boldsymbol{0}\\\vdots&&\ddots&\vdots\\\boldsymbol{0}&\boldsymbol{0}&\cdots&\boldsymbol{1}_{n_r}\end{bmatrix}_{n_T\times r},\qquad \boldsymbol\beta=\begin{bmatrix}\mu_1\\\mu_2\\\vdots\\\mu_r\end{bmatrix},
$$
where $\boldsymbol{1}_{n_i}$ is the vector of $n_i$ ones.

**Proposition 13.1.1** In the cell means model $X^{\mathsf T}X=\operatorname{diag}(n_1,\dots,n_r)$ and $X^{\mathsf T}\boldsymbol{Y}=(n_1\bar Y_{1\cdot},\dots,n_r\bar Y_{r\cdot})^{\mathsf T}$, so the least squares estimator is

$$
\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}=(\bar Y_{1\cdot},\dots,\bar Y_{r\cdot})^{\mathsf T},\qquad \operatorname{Cov}(\boldsymbol{b})=\sigma^2\operatorname{diag}(1/n_1,\dots,1/n_r).
$$

This recovers Theorem 12.2.1 from the matrix formulas of [3.3.7](/3.3.7): $\hat\mu_i=\bar Y_{i\cdot}$, the fitted value of every observation is its level mean, and the estimated standard error of $\hat\mu_i$ is $s/\sqrt{n_i}$ with the pooled $s=\sqrt{\mathrm{MSE}}$.

### 13.1.2. The Factor Effects Model and Its Constraints

The factor effects model $Y_{ij}=\mu+\tau_i+\varepsilon_{ij}$ has the parameters $\mu,\tau_1,\dots,\tau_r$ and $\sigma^2$, that is, $r+2$ parameters against the $r+1$ of the cell means model. Its natural design matrix has a column of ones followed by the $r$ indicator columns:

$$
X\boldsymbol\beta=\begin{bmatrix}\boldsymbol{1}_{n_1}&\boldsymbol{1}_{n_1}&\boldsymbol{0}&\cdots&\boldsymbol{0}\\\boldsymbol{1}_{n_2}&\boldsymbol{0}&\boldsymbol{1}_{n_2}&\cdots&\boldsymbol{0}\\\vdots&&&\ddots&\vdots\\\boldsymbol{1}_{n_r}&\boldsymbol{0}&\boldsymbol{0}&\cdots&\boldsymbol{1}_{n_r}\end{bmatrix}\begin{bmatrix}\mu\\\tau_1\\\vdots\\\tau_r\end{bmatrix}.
$$
The first column is the sum of the others, so $X$ has **rank** $r<r+1$ and $X^{\mathsf T}X$ has no inverse: the parameters cannot all be estimated uniquely.

**Example 13.1.1** Let $r=3$ with $\mu_1=10$, $\mu_2=20$, $\mu_3=30$. Any parameters with $\mu+\tau_i=\mu_i$ describe the same distributions, for instance

1. $\mu=0$, $\tau_1=10$, $\tau_2=20$, $\tau_3=30$;
2. $\mu=20$, $\tau_1=-10$, $\tau_2=0$, $\tau_3=10$;
3. $\mu=5000$, $\tau_1=-4990$, $\tau_2=-4980$, $\tau_3=-4970$.

All three give the same means, so no data can distinguish them.

A linear function of the parameters that has a linear unbiased estimator is called an *estimable function*; equivalently, it is a linear function of the cell means $\mu_i=\mu+\tau_i$. The combinations $\mu+\tau_i$ are estimable, estimated by the sample means $\bar Y_{i\cdot}$, and so are differences $\tau_i-\tau_k=\mu_i-\mu_k$; but $\mu$ and the individual $\tau_i$ are not. The solution is to put one linear constraint on the $\tau_i$, which reduces the number of free parameters by one and gives a design matrix of full column rank. Common choices are:

| Constraint | Meaning of $\mu$ | Design matrix |
|---|---|---|
| $\sum_i\tau_i=0$ | unweighted mean of the $\mu_i$ | drop the column of $\tau_r$; the rows of level $r$ get $-1$ in every $\tau$ column, since $\tau_r=-\tau_1-\cdots-\tau_{r-1}$ |
| $\tau_1=0$ (default in R) | mean of the baseline level $1$ | drop the column of $\tau_1$ |
| $\tau_r=0$ | mean of level $r$ | drop the column of $\tau_r$ |
| $\sum_in_i\tau_i=0$ | weighted mean $\sum_in_i\mu_i/n_T$ | as for $\sum_i\tau_i=0$, with weights |

Numerous other constraints are possible (even $\sum_i\tau_i=100$), and they only change the meaning of $\mu$ and the $\tau_i$. Whatever the constraint, $\mu_i=\mu+\tau_i$ and $\hat\mu_i=\bar Y_{i\cdot}$; the fitted values, residuals and ANOVA table are the same.

**Proposition 13.1.2** Under the constraint $\sum_{i=1}^r\tau_i=0$,

$$
\mu=\frac{1}{r}\sum_{i=1}^r\mu_i,\qquad \tau_i=\mu_i-\mu,\qquad \hat\mu=\frac{1}{r}\sum_{i=1}^r\bar Y_{i\cdot},\qquad \hat\tau_i=\bar Y_{i\cdot}-\hat\mu.
$$
If all $n_i=n$, then $\hat\mu=\bar Y_{\cdot\cdot}$. If instead a weighted mean is desired in the first place, define $\mu=\sum_in_i\mu_i/n_T=\sum_iw_i\mu_i$ with $w_i=n_i/n_T$; the constraint becomes $\sum_iw_i\tau_i=0$, and then $\hat\mu=\bar Y_{\cdot\cdot}$ for any $n_i$.

**Proof** Summing $\mu_i=\mu+\tau_i$ over $i$ gives $\sum_i\mu_i=r\mu$; the estimates follow by plugging in $\hat\mu_i=\bar Y_{i\cdot}$. The weighted case is the same with weights $w_i$. $\square$

So the overall mean $\hat\mu$ is the mean of the subsample means, which differs from the grand mean $\bar Y_{\cdot\cdot}$ when the $n_i$ are unequal. In terms of the effects, the hypotheses of the $F$-test become

$$
H_0\colon\tau_1=\tau_2=\cdots=\tau_r=0\qquad\text{versus}\qquad H_1\colon\text{at least one }\tau_i\ne0.
$$

### 13.1.3. Example: Cereal Package Designs

**Example 13.1.2** A cereal manufacturer compares $r=4$ package designs. Each design is used in several stores, and $Y$ is the number of cases sold; one store's data were lost, so $n_i=5,5,4,5$ and $n_T=19$.

| Design | Cases sold | $n_i$ | $\bar Y_{i\cdot}$ | $s_i$ |
|---|---|---|---|---|
| 1 | 11, 17, 16, 14, 15 | 5 | 14.6 | 2.302 |
| 2 | 12, 10, 15, 19, 11 | 5 | 13.4 | 3.647 |
| 3 | 23, 20, 18, 17 | 4 | 19.5 | 2.646 |
| 4 | 27, 33, 22, 26, 28 | 5 | 27.2 | 3.962 |

A plot of the data against design shows means that differ, and spreads that are comparable; the observations come from different stores, so independence is plausible, and with four or five observations per design normality can only be checked roughly (diagnostics for ANOVA models follow in [3.3.14](/3.3.14)).

```r
a1 <- read.table("CH16TA01.txt")
colnames(a1) <- c("cases", "design", "store")
a2 <- aggregate(a1$cases, list(a1$design), mean)      # level means
a2$sd <- tapply(a1$cases, a1$design, sd)
fit <- lm(cases ~ design, data = a1)                 # wrong: design treated as numeric
a1$design <- factor(a1$design)                       # inform R that design is a factor
fit1 <- lm(cases ~ 0 + design, data = a1)            # cell means model
fit  <- lm(cases ~ design, data = a1)                # factor effects model, tau_1 = 0
```

If `design` is left numeric, `lm` fits a straight line in the codes $1,2,3,4$ (slope $4.42$, residual standard error $3.936$ on 17 degrees of freedom), which is meaningless for a categorical variable. With `design` a factor, the two parametrizations give:

| Cell means model (`0 + design`) | Estimate | Std. error | Factor effects model (`design`) | Estimate | Std. error |
|---|---|---|---|---|---|
| design1 | 14.6 | 1.452 | (Intercept) | 14.6 | 1.452 |
| design2 | 13.4 | 1.452 | design2 | −1.2 | 2.054 |
| design3 | 19.5 | 1.624 | design3 | 4.9 | 2.179 |
| design4 | 27.2 | 1.452 | design4 | 12.6 | 2.054 |

Both have residual standard error $s=\sqrt{158.2/15}=3.248$ on $15$ degrees of freedom. The standard errors of the cell means are $s/\sqrt{n_i}$ (not $s_i/\sqrt{n_i}$): $3.248/\sqrt5=1.452$ and $3.248/\sqrt4=1.624$, which rests on the assumption of constant variance. R drops the column of design 1, which corresponds to the constraint $\tau_1=0$: the intercept $\hat\mu=14.6$ is the sample mean of the baseline level and $\hat\tau_i$ is (sample mean of level $i$) minus (sample mean of level $1$), for example $\hat\tau_2=13.4-14.6=-1.2$ and $\hat\tau_4=27.2-14.6=12.6$.

The overall $F$ statistics of the two fits differ: for the factor effects model, $F=18.59$ on $3$ and $15$ degrees of freedom tests $H_0\colon\tau_2=\tau_3=\tau_4=0$, the hypothesis of equal means; for the cell means model without intercept, $F=170.3$ on $4$ and $15$ degrees of freedom tests $\mu_1=\cdots=\mu_4=0$, and its $R^2=0.9785$ is computed about zero instead of about $\bar Y_{\cdot\cdot}$. Neither of the latter is of interest.

## 13.2. Tests and Confidence Intervals

### 13.2.1. The F-Test as a General Linear Test

The ANOVA **F-test** of Theorem 12.2.3, $F^*=\mathrm{MSTR}/\mathrm{MSE}\sim F_{r-1,n_T-r}$ under $H_0\colon\mu_1=\cdots=\mu_r$, is the **general linear test** of [3.3.4](/3.3.4) and [3.3.9](/3.3.9) with the full model $Y_{ij}=\mu_i+\varepsilon_{ij}$ and the reduced model $Y_{ij}=\mu+\varepsilon_{ij}$. The reduced model has $\mathrm{SSE}(R)=\mathrm{SSTO}$ on $n_T-1$ degrees of freedom and the full model $\mathrm{SSE}(F)=\mathrm{SSE}$ on $n_T-r$, so

$$
F^*=\frac{[\mathrm{SSE}(R)-\mathrm{SSE}(F)]/[(n_T-1)-(n_T-r)]}{\mathrm{SSE}(F)/(n_T-r)}=\frac{\mathrm{SSTR}/(r-1)}{\mathrm{SSE}/(n_T-r)}.
$$
It is common to report the $p$-value along with the decision.

```r
ful <- lm(cases ~ design, data = a1)
red <- lm(cases ~ 1, data = a1)
anova(red, ful)                     # general linear test
summary(aov(cases ~ design, data = a1))   # the same F-test as an ANOVA table
```

For the cereal data, $\mathrm{SSE}(R)=746.42$ on $18$ degrees of freedom and $\mathrm{SSE}(F)=158.20$ on $15$, so $\mathrm{SSTR}=588.22$, $\mathrm{MSTR}=196.07$, $\mathrm{MSE}=10.547$ and $F^*=18.59$ with $p=2.6\times10^{-5}$: the mean sales differ among the four designs.

### 13.2.2. Confidence Intervals for the Level Means

Since $\bar Y_{i\cdot}\sim\mathcal{N}(\mu_i,\sigma^2/n_i)$ and $\mathrm{SSE}/\sigma^2\sim\chi^2_{n_T-r}$ independently, a $1-\alpha$ **confidence interval** for $\mu_i$ is

$$
\bar Y_{i\cdot}\pm t_{n_T-r,\alpha/2}\,\frac{s}{\sqrt{n_i}},\qquad s=\sqrt{\mathrm{MSE}}=\sqrt{\frac{\sum_i(n_i-1)s_i^2}{n_T-r}}.
$$
The degrees of freedom $n_T-r$ are larger than the $n_i-1$ of a single group because we pool the variances into one estimate $s$; this is an advantage of ANOVA when the model assumptions are appropriate. For the cereal data, $\mathrm{SSE}=4(2.30)^2+4(3.65)^2+3(2.65)^2+4(3.96)^2=158.2$, $s=3.25$ and $t_{15,0.025}=2.131$.

| Design | $\bar Y_{i\cdot}$ | $s_i$ | 95% CI with pooled $s$ | 95% CI with $s_i$, $n_i-1$ d.f. |
|---|---|---|---|---|
| 1 | 14.6 | 2.302 | $[11.50,\ 17.70]$ | $[11.74,\ 17.46]$ |
| 2 | 13.4 | 3.647 | $[10.30,\ 16.50]$ | $[8.87,\ 17.93]$ |
| 3 | 19.5 | 2.646 | $[16.04,\ 22.96]$ | $[15.29,\ 23.71]$ |
| 4 | 27.2 | 3.962 | $[24.10,\ 30.30]$ | $[22.28,\ 32.12]$ |

The intervals without pooling use $\bar Y_{i\cdot}\pm t_{n_i-1,\alpha/2}\,s_i/\sqrt{n_i}$. The pooled intervals are usually narrower, mainly because the $t$ quantile with $15$ degrees of freedom ($2.13$) is much smaller than with $3$ or $4$ ($3.18$, $2.78$); for design 1 the pooled interval is slightly wider, because its own $s_1=2.30$ is smaller than $s=3.25$.

```r
fit1 <- lm(cases ~ 0 + design, data = a1)
confint(fit1)                       # pooled intervals
```

![Left: the cereal sales by package design with the level means. Right: 95% confidence intervals for the four level means, with the pooled standard deviation and with each level's own standard deviation.](./plots/cereal-means-intervals.py)

## 13.3. Multiple Comparisons

### 13.3.1. The Multiplicity Problem

We have constructed four (in general $r$) 95% confidence intervals. Each covers its mean with probability $0.95$, but the probability that all of them cover their means simultaneously, the overall confidence level, is less than $0.95$. The same happens with tests: many scientific studies evaluate more than one question at once, and each additional test is another chance of a false rejection, so the probability of at least one **type I error** grows with the number of tests ($\alpha$ inflation). Reporting only the comparisons that came out significant among many that were made produces findings that do not replicate; selective publication of such results (publication bias) is a well-known source of false discoveries.

Two error rates must therefore be distinguished. The *comparisonwise error rate* is the probability of a type I error in one comparison considered by itself; the **family-wise error rate** (FWER), also called the experimentwise error rate, is the probability of at least one false rejection among all comparisons of the family. "Family-wise" means "simultaneously": with $r=4$ means there are $6$ pairwise hypotheses $H_0\colon\mu_i=\mu_k$, and if all means are equal, an error occurs in a study whenever any of the six is falsely rejected. Repeating the study $100$ times with each test at level $0.05$, the single comparison $\mu_1=\mu_2$ is falsely rejected about $5$ times; controlling the FWER at $0.05$ means that about $5$ of the $100$ studies contain any false rejection at all. For six independent tests at level $0.05$ the FWER would be $1-0.95^6=0.26$.

Multiple comparison procedures are of two types. A single-step procedure uses one critical value for all comparisons, so the decision for each comparison does not depend on the outcomes of the others; all four methods below are of this type. In a stepwise procedure the comparisons are made in sequence and the critical value, or whether a comparison is made at all, depends on the previous results; for example, in Fisher's protected LSD the pairwise tests are made only if the overall $F$-test is significant, and the Holm procedure tests the ordered $p$-values against increasing thresholds.

The adjustment we already know is Bonferroni's: for $g$ intervals use level $1-\alpha/g$ for each, which guarantees joint coverage at least $1-\alpha$. For the four cereal means:

```r
confint(fit1, level = 1 - 0.05/4)   # Bonferroni simultaneous 95% intervals
```

gives $[10.48,\ 18.72]$, $[9.28,\ 17.52]$, $[14.89,\ 24.11]$ and $[23.08,\ 31.32]$, wider than the individual intervals above.

Tests of $H_0\colon\mu_i=0$ for an individual mean are usually not of interest. To test $H_0\colon\mu_i=c$ for a constant $c$, subtract $c$ from the observations at that level (or simply check whether $c$ lies in the confidence interval for $\mu_i$).

### 13.3.2. Pairwise Comparisons of Means

The usual follow-up questions concern differences of means. Since $\bar Y_{i\cdot}-\bar Y_{k\cdot}\sim\mathcal{N}\big(\mu_i-\mu_k,\ \sigma^2(1/n_i+1/n_k)\big)$, the intervals for $\mu_i-\mu_k$ have the form

$$
\bar Y_{i\cdot}-\bar Y_{k\cdot}\pm t_c\,s(\bar Y_{i\cdot}-\bar Y_{k\cdot}),\qquad s(\bar Y_{i\cdot}-\bar Y_{k\cdot})=s\sqrt{\frac{1}{n_i}+\frac{1}{n_k}},
$$
and a test rejects $\mu_i=\mu_k$ when the interval excludes $0$. There are $\binom r2=r(r-1)/2$ pairwise comparisons, and the multiplicity problem is handled through the choice of $t_c$: either by changing the level, as Bonferroni does, or by using a different distribution.

**Definition 13.3.1 (Least Significant Difference)** **Fisher's least significant difference** (LSD) method uses $t_c=t_{n_T-r,\alpha/2}$ for every comparison: each pairwise interval is an ordinary $1-\alpha$ interval with the pooled $s$.

The LSD method ignores the multiplicity issue: it controls the comparisonwise error rate, not the family-wise one. The Bonferroni method uses the error budget idea: with $g=r(r-1)/2$ comparisons it replaces $\alpha$ by $\alpha/g$ for each, $t_c=t_{n_T-r,\alpha/(2g)}$, so the FWER is at most $\alpha$.

**Definition 13.3.2 (Studentized Range Distribution)** Let $Z_1,\dots,Z_r$ be independent $\mathcal{N}(0,1)$ and $V\sim\chi^2_\nu$ independent of them. The distribution of

$$
Q=\frac{\max_iZ_i-\min_iZ_i}{\sqrt{V/\nu}}
$$
is the **studentized range distribution** with parameters $r$ and $\nu$; its upper $\alpha$ quantile is denoted $q_{r,\nu,\alpha}$.

**Theorem 13.3.1 (Tukey's Method)** Suppose all $n_i=n$. Then the intervals

$$
\bar Y_{i\cdot}-\bar Y_{k\cdot}\pm\frac{q_{r,n_T-r,\alpha}}{\sqrt2}\,s\sqrt{\frac2n},\qquad 1\le i<k\le r,
$$
have simultaneous coverage probability exactly $1-\alpha$. In particular, under $H_0\colon\mu_1=\cdots=\mu_r$,

$$
\mathbb{P}\Big(\max_{i,k}\frac{\lvert\bar Y_{i\cdot}-\bar Y_{k\cdot}\rvert}{s\sqrt{2/n}}>\frac{q_{r,n_T-r,\alpha}}{\sqrt2}\Big)=\mathbb{P}\Big(\frac{\bar Y_{\max}-\bar Y_{\min}}{s/\sqrt n}>q_{r,n_T-r,\alpha}\Big)=\alpha.
$$

**Proof** Put $Z_i=(\bar Y_{i\cdot}-\mu_i)/(\sigma/\sqrt n)$, independent $\mathcal{N}(0,1)$, and $V=\mathrm{SSE}/\sigma^2\sim\chi^2_{n_T-r}$, independent of the $Z_i$. All intervals cover simultaneously if and only if $\lvert Z_i-Z_k\rvert\le q_{r,n_T-r,\alpha}\sqrt{V/(n_T-r)}$ for all pairs, that is, if and only if $(\max_iZ_i-\min_iZ_i)/\sqrt{V/(n_T-r)}\le q_{r,n_T-r,\alpha}$, which has probability $1-\alpha$. $\square$

Tukey's honestly significant difference (HSD) test thus replaces $t_c$ by $q_c/\sqrt2$. For unequal $n_i$ the same $t_c$ with $s\sqrt{1/n_i+1/n_k}$ gives the Tukey–Kramer intervals, whose family-wise coverage is at least $1-\alpha$.

**Theorem 13.3.2 (Scheffé's Method)** For every contrast $L=\sum_ic_i\mu_i$ with $\sum_ic_i=0$ (Definition 13.4.1), let $\hat L=\sum_ic_i\bar Y_{i\cdot}$ and $s^2(\hat L)=\mathrm{MSE}\sum_ic_i^2/n_i$. Then the intervals

$$
\hat L\pm t_c\,s(\hat L),\qquad t_c=\sqrt{(r-1)F_{r-1,n_T-r,\alpha}},
$$
cover all contrasts simultaneously with probability $1-\alpha$.

**Proof** Let $D_i=\bar Y_{i\cdot}-\mu_i$ and $\bar D=\sum_in_iD_i/n_T$. For a contrast, $\hat L-L=\sum_ic_i(D_i-\bar D)$, and by the Cauchy–Schwarz inequality

$$
(\hat L-L)^2=\Big(\sum_i\frac{c_i}{\sqrt{n_i}}\sqrt{n_i}(D_i-\bar D)\Big)^2\le\sum_i\frac{c_i^2}{n_i}\cdot\sum_in_i(D_i-\bar D)^2,
$$
with equality for $c_i=n_i(D_i-\bar D)$, which is a contrast. Hence $\sup_{\boldsymbol c}(\hat L-L)^2/s^2(\hat L)=\sum_in_i(D_i-\bar D)^2/\mathrm{MSE}$. The numerator is the treatment sum of squares computed from the $D_i$, so it is $\sigma^2\chi^2_{r-1}$ and independent of $\mathrm{MSE}$ (Theorem 12.2.3); thus the supremum divided by $r-1$ has the $F_{r-1,n_T-r}$ distribution, and all intervals cover if and only if it is at most $F_{r-1,n_T-r,\alpha}$. $\square$

Scheffé's method takes care of multiplicity for all linear combinations of means (all contrasts), not just pairwise comparisons, and it is consistent with the overall $F$-test: $F^*>F_{r-1,n_T-r,\alpha}$ if and only if at least one contrast is significant by Scheffé's criterion. The price is wide intervals when only a few comparisons are of interest.

| Method | $t_c$ for the cereal data ($\alpha=0.05$, $n_T-r=15$) | Controls | Comment |
|---|---|---|---|
| LSD | $t_{15,0.025}=2.131$ | comparisonwise error rate | too liberal (too many type I errors) |
| Bonferroni | $t_{15,0.05/12}=3.036$ | FWER, any $g$ comparisons | fine when $g$ is small |
| Tukey | $q_{4,15,0.05}/\sqrt2=4.076/\sqrt2=2.882$ | FWER, all pairs | recommended for pairwise comparisons |
| Scheffé | $\sqrt{3F_{3,15,0.05}}=\sqrt{3\times3.287}=3.140$ | FWER, all contrasts | too conservative (low power) for pairs |

Before choosing a procedure, decide whether the family-wise error rate is the focus, how many comparisons there are in total, and whether the interest is in pairwise comparisons or in general linear combinations. Other procedures exist and are worth considering, such as Dunnett's method for comparisons with a control and the stepwise procedures mentioned above.

### 13.3.3. The Cereal Example Revisited

**Example 13.3.1** The pairwise comparisons for the cereal data, with simultaneous (LSD: individual) 95% intervals:

| Comparison | $\bar Y_{i\cdot}-\bar Y_{k\cdot}$ | LSD | Bonferroni | Tukey | Scheffé |
|---|---|---|---|---|---|
| 2 − 1 | −1.2 | $[-5.58,\ 3.18]$ | $[-7.44,\ 5.04]$ | $[-7.12,\ 4.72]$ | $[-7.65,\ 5.25]$ |
| 3 − 1 | 4.9 | $[0.26,\ 9.54]$ | $[-1.71,\ 11.51]$ | $[-1.38,\ 11.18]$ | $[-1.94,\ 11.74]$ |
| 4 − 1 | 12.6 | $[8.22,\ 16.98]$ | $[6.36,\ 18.84]$ | $[6.68,\ 18.52]$ | $[6.15,\ 19.05]$ |
| 3 − 2 | 6.1 | $[1.46,\ 10.74]$ | $[-0.51,\ 12.71]$ | $[-0.18,\ 12.38]$ | $[-0.74,\ 12.94]$ |
| 4 − 2 | 13.8 | $[9.42,\ 18.18]$ | $[7.56,\ 20.04]$ | $[7.88,\ 19.72]$ | $[7.35,\ 20.25]$ |
| 4 − 3 | 7.7 | $[3.06,\ 12.34]$ | $[1.09,\ 14.31]$ | $[1.42,\ 13.98]$ | $[0.86,\ 14.54]$ |

The LSD method declares five of the six pairs different (all except designs 1 and 2); Bonferroni, Tukey and Scheffé each declare three: design 4 sells more than each of the other three, while designs 1, 2 and 3 cannot be separated at the family-wise level. Tukey's intervals are the shortest of the three methods that control the FWER, and Scheffé's the longest, as the critical values predict.

```r
pairwise.t.test(a1$cases, a1$design, p.adjust = "none", pool.sd = TRUE)        # Fisher's LSD
pairwise.t.test(a1$cases, a1$design, p.adjust = "bonferroni", pool.sd = TRUE)  # Bonferroni
mod1 <- aov(cases ~ design, data = a1)
TukeyHSD(mod1, conf.level = 0.95)              # Tukey's HSD
library(agricolae)
LSD.test(mod1, trt = "design", group = FALSE, console = TRUE)
scheffe.test(mod1, trt = "design", group = FALSE, console = TRUE)
```

![Simultaneous 95% intervals for the six pairwise differences of the cereal means by the LSD, Bonferroni, Tukey and Scheffé methods; intervals that exclude zero are drawn solid.](./plots/pairwise-comparisons.py)

## 13.4. Contrasts

### 13.4.1. Linear Combinations and Contrasts

Many research questions are about linear combinations $L=\sum_ic_i\mu_i$ of the level means, for example "is the average of designs 1 and 2 lower than that of designs 3 and 4?". The coefficients should come from the research questions, not from an examination of the data (choosing them after looking at the data is a hidden multiple comparison; Scheffé's method covers that case). The estimator is

$$
\hat L=\sum_ic_i\bar Y_{i\cdot}\sim\mathcal{N}\big(L,\operatorname{Var}(\hat L)\big),\qquad \operatorname{Var}(\hat L)=\sum_ic_i^2\operatorname{Var}(\bar Y_{i\cdot})=\sigma^2\sum_i\frac{c_i^2}{n_i},\qquad \widehat{\operatorname{Var}}(\hat L)=\mathrm{MSE}\sum_i\frac{c_i^2}{n_i},
$$
and the linear model gives a $t$-test of any linear combination: under $H_0\colon L=L_0$,

$$
T=\frac{\hat L-L_0}{\sqrt{\widehat{\operatorname{Var}}(\hat L)}}\sim t_{n_T-r}.
$$

**Definition 13.4.1 (Contrast)** A linear combination $L=\sum_ic_i\mu_i$ is a **contrast** if $\sum_ic_i=0$.

A contrast compares groups of means, and it does not depend on the overall level: $\sum_ic_i\mu_i=\sum_ic_i\tau_i$ under any constraint, so contrasts are estimable in the factor effects model. Examples are $\mu_1-\mu_2$, $\mu_1-(\mu_2+\mu_3)/2$, and $(\mu_1+\mu_2)/2-(\mu_3+\mu_4)/2$.

### 13.4.2. Contrast Sums of Squares

For $H_0\colon L=0$ the statistic is $T=\sum_ic_i\bar Y_{i\cdot}\big/\sqrt{\mathrm{MSE}\sum_ic_i^2/n_i}\sim t_{n_T-r}$, and since $t_{n_T-r}^2$ has the $F_{1,n_T-r}$ distribution,

$$
T^2=\frac{\big(\sum_ic_i\bar Y_{i\cdot}\big)^2}{\mathrm{MSE}\sum_ic_i^2/n_i}=\frac{\mathrm{SSC}/1}{\mathrm{MSE}}\sim F_{1,n_T-r},\qquad \mathrm{SSC}=\frac{\big(\sum_ic_i\bar Y_{i\cdot}\big)^2}{\sum_ic_i^2/n_i}.
$$
The *contrast sum of squares* $\mathrm{SSC}$, with one degree of freedom, represents the amount of variation due to this contrast. The proof of Theorem 13.3.2 shows that $\mathrm{SSC}\le\mathrm{SSTR}$ for every contrast, with equality for the best one.

We can also test a collection of contrasts simultaneously, with one degree of freedom for each linearly independent contrast. $H_0\colon\mu_2=\mu_3=\mu_4$ consists of two contrasts ($\mu_2-\mu_3=0$, $\mu_3-\mu_4=0$), and its $F$ statistic has the $F_{2,n_T-r}$ distribution; $H_0\colon\mu_1=(\mu_2+\mu_3+\mu_4)/3$ is a single contrast with an $F_{1,n_T-r}$ distribution. Both are general linear tests.

**Example 13.4.1** For the cereal data, the package `multcomp` estimates and tests several contrasts at once:

```r
mod1 <- aov(cases ~ 0 + design, data = a1)
cntrMat <- rbind("1&2 v 3&4"  = c(0.5, 0.5, -0.5, -0.5),
                 "1 v 2&3&4"  = c(1, -1/3, -1/3, -1/3),
                 "1 v 2&3&4 (x3)" = c(3, -1, -1, -1),
                 "2 v 3"      = c(0, 1, -1, 0))
library(multcomp)
summary(glht(mod1, linfct = cntrMat))      # simultaneous tests, single-step adjustment
```

| Contrast | $\hat L$ | Std. error | $t$ | adjusted $p$ |
|---|---|---|---|---|
| $(\mu_1+\mu_2)/2-(\mu_3+\mu_4)/2$ | $-9.350$ | $1.497$ | $-6.25$ | $<0.001$ |
| $\mu_1-(\mu_2+\mu_3+\mu_4)/3$ | $-5.433$ | $1.694$ | $-3.21$ | $0.015$ |
| $3\mu_1-\mu_2-\mu_3-\mu_4$ | $-16.300$ | $5.083$ | $-3.21$ | $0.015$ |
| $\mu_2-\mu_3$ | $-6.100$ | $2.179$ | $-2.80$ | $0.033$ |

For instance, $\hat L_1=(14.6+13.4)/2-(19.5+27.2)/2=-9.35$ with standard error $\sqrt{10.547\,(0.25/5+0.25/5+0.25/4+0.25/5)}=1.497$. Multiplying a contrast by a constant ($3\mu_1-\mu_2-\mu_3-\mu_4$ versus $\mu_1-(\mu_2+\mu_3+\mu_4)/3$) changes $\hat L$ and its standard error but not the test. The $p$-values are adjusted for the four simultaneous tests, so they are larger than the unadjusted $t$-test $p$-values.

A general linear test and a set of multiple comparisons answer different questions. To compare designs 2, 3 and 4:

```r
library(car)
linearHypothesis(fit1, rbind(c(0, 1, -1, 0), c(0, 0, 1, -1)))    # one F-test, 2 d.f.
summary(glht(fit1, rbind(c(0, 1, -1, 0), c(0, 0, 1, -1))))       # two adjusted t-tests
```

The general linear test compares the restricted model ($\mathrm{SSE}=636.13$ on $17$ degrees of freedom) with the cell means model ($158.20$ on $15$): $F=\frac{(636.13-158.20)/2}{10.547}=22.66$ on $2$ and $15$ degrees of freedom, $p=2.9\times10^{-5}$, so $\mu_2,\mu_3,\mu_4$ are not all equal. The multiple comparisons say which differences are responsible: $\mu_2-\mu_3$ ($\hat L=-6.1$, adjusted $p=0.024$) and $\mu_3-\mu_4$ ($\hat L=-7.7$, adjusted $p=0.0056$).

## Summary {#summary}

- In the cell means model $X$ consists of $r$ indicator columns and $\hat\mu_i=\bar Y_{i\cdot}$ with standard error $s/\sqrt{n_i}$. In the factor effects model the column of ones makes $X$ rank-deficient: $\mu+\tau_i$ and contrasts are estimable, $\mu$ and $\tau_i$ are not until a constraint is imposed ($\sum\tau_i=0$, or $\tau_1=0$ as in R).
- The ANOVA $F$-test is the general linear test of $Y_{ij}=\mu+\varepsilon_{ij}$ against $Y_{ij}=\mu_i+\varepsilon_{ij}$. Intervals for $\mu_i$ use the pooled $s$ with $n_T-r$ degrees of freedom.
- With many comparisons the family-wise error rate exceeds $\alpha$. LSD ignores multiplicity; Bonferroni divides $\alpha$ by the number of comparisons; Tukey's studentized range method is exact for all pairs with equal $n_i$; Scheffé's method covers all contrasts.
- A contrast $\sum c_i\mu_i$ with $\sum c_i=0$ is tested by $T=\hat L/s(\hat L)\sim t_{n_T-r}$, equivalently by $\mathrm{SSC}/\mathrm{MSE}\sim F_{1,n_T-r}$; several contrasts together form a general linear test.
