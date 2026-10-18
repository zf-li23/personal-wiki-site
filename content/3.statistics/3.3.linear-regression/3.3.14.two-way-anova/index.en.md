---
title: Two-Way Analysis of Variance, Diagnostics and Remedies
description: The cell means and factor effects models with two factors, main effects and interactions, the two-way ANOVA table and its F-tests, least squares means for unbalanced data; residual diagnostics and tests of equal variances for ANOVA models; weighted ANOVA, the Box–Cox transformation and the Kruskal–Wallis test.
---

This last chapter of the course extends the analysis of variance of [3.3.12](/3.3.12) and [3.3.13](/3.3.13) in two directions. First, the treatments may be classified by two factors at once; then a new question appears besides "does each factor matter?", namely whether the effect of one factor depends on the level of the other, which is the **interaction effect** already met in regression models with product terms ([3.3.10](/3.3.10)). The two-way ANOVA table answers these questions by $F$-tests, and least squares means summarize the factors when the data are unbalanced. Second, we adapt the regression diagnostics of [3.3.5](/3.3.5) and [3.3.11](/3.3.11) and the remedial measures of [3.3.6](/3.3.6) and [3.3.12](/3.3.12) to ANOVA models: residual plots, tests for equal variances, weighted ANOVA, transformations and a rank test. Designs with several factors are the subject of experimental design ([3.8](/3.8)); the multivariate analogue, with a vector response, is the **multivariate analysis of variance** ([3.4.10](/3.4.10)).

## 14.1. Two-Way ANOVA Models

### 14.1.1. Data and Assumptions

The response $Y$ is continuous, and there are now two categorical explanatory variables (factors): the treatments are classified in two ways and form a two-way table. Factor $A$ has levels $i=1,\dots,a$ and factor $B$ levels $j=1,\dots,b$; each combination $(i,j)$ is a cell, and $Y_{ijk}$ is the $k$-th observation in cell $(i,j)$. Unless stated otherwise we assume equal sample sizes $n_{ij}=n$ in all cells (a balanced design), so $n_T=abn$.

| | $A=1$ | $\cdots$ | $A=a$ |
|---|---|---|---|
| $B=1$ | $Y_{111},\dots,Y_{11n}$ | $\cdots$ | $Y_{a11},\dots,Y_{a1n}$ |
| $\vdots$ | $\vdots$ | | $\vdots$ |
| $B=b$ | $Y_{1b1},\dots,Y_{1bn}$ | $\cdots$ | $Y_{ab1},\dots,Y_{abn}$ |

We assume that the observations are normally distributed, with a mean that may depend only on the levels of the factors $A$ and $B$, with constant variance, and independent.

**Example 14.1.1** A bakery studies how the shelf display affects bread sales. $Y$ is the number of cases of bread sold; factor $A$ is the height of the display, with $a=3$ levels (bottom, middle, top), and factor $B$ its width, with $b=2$ levels (regular, wide). Each of the $3\times2=6$ treatment combinations is used in $n=2$ stores, so $n_T=12$.

| Width \ Height | 1 (bottom) | 2 (middle) | 3 (top) |
|---|---|---|---|
| 1 (regular) | 47, 43 | 62, 68 | 41, 39 |
| 2 (wide) | 46, 40 | 67, 71 | 42, 46 |

### 14.1.2. The Cell Means Model

**Definition 14.1.1 (Two-Way Cell Means Model)** The **two-way cell means model** is

$$
Y_{ijk}=\mu_{ij}+\varepsilon_{ijk},\qquad \varepsilon_{ijk}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
where $\mu_{ij}$ is the theoretical mean of all observations in cell $(i,j)$; equivalently, the $Y_{ijk}\sim\mathcal{N}(\mu_{ij},\sigma^2)$ are independent. The parameters are the $ab$ cell means $\mu_{ij}$ and $\sigma^2$.

This is the one-way cell means model with the $ab$ cells as the levels of a single factor, so the results of [3.3.12](/3.3.12) apply directly. We estimate $\mu_{ij}$ by the cell mean $\bar Y_{ij\cdot}=\sum_kY_{ijk}/n$, and pool the cell variances $s_{ij}^2=\sum_k(Y_{ijk}-\bar Y_{ij\cdot})^2/(n-1)$ with weights proportional to their degrees of freedom:

$$
s^2=\frac{\sum_{i,j}(n_{ij}-1)s_{ij}^2}{\sum_{i,j}(n_{ij}-1)},\qquad\text{which for }n_{ij}=n\text{ is }s^2=\frac{1}{ab}\sum_{i,j}s_{ij}^2,
$$
the average of the cell variances. The *marginal means* of the factor levels average over the other factor: $\bar Y_{i\cdot\cdot}$ for level $i$ of $A$ and $\bar Y_{\cdot j\cdot}$ for level $j$ of $B$.

For the bakery data, the cell means and marginal means are

| Width \ Height | 1 | 2 | 3 | width mean |
|---|---|---|---|---|
| 1 | 45 | 65 | 40 | 50 |
| 2 | 43 | 69 | 44 | 52 |
| height mean | 44 | 67 | 42 | 51 |

and the cell standard deviations are $2.83, 4.24, 4.24, 2.83, 1.41, 2.83$, so $s^2=(8+18+18+8+2+8)/6=10.33$ and $s=3.215$. Fitting the cell means model by regression on the six cell indicators reproduces these: each estimate has standard error $s/\sqrt2=2.273$.

```r
a <- read.table("CH19TA07.txt")
names(a) <- c("sales", "height", "width", "store")
a$height <- factor(a$height); a$width <- factor(a$width)
a$cell <- factor(paste0("h", a$height, "w", a$width))
summary(lm(sales ~ 0 + cell, data = a))                  # cell means model
aggregate(sales ~ height * width, data = a, FUN = mean)  # cell means by hand
with(a, interaction.plot(x.factor = height, trace.factor = width,
                         response = sales, fun = mean))   # interaction plot
```

The natural questions concern the *main effects* of the factors. Does the height of the display ($A$) affect sales? If yes, compare top with middle, top with bottom, and middle with bottom. Does the width ($B$) affect sales? If yes, compare regular and wide. But are such factor level comparisons meaningful? That depends on whether the effect of height on sales depends on the width, and whether the effect of width depends on the height. If it does, the factors interact, and the marginal comparisons may be significant but not meaningful: averaging over the levels of the other factor hides effects that change size or even sign.

An *interaction plot* shows the cell means $\bar Y_{ij\cdot}$ against the levels of one factor, with one line for each level of the other factor. Without interaction the lines are parallel: the effect of $A$ is the same at every level of $B$, shifted by a constant. Non-parallel lines indicate interaction; lines that cross indicate that even the direction of the effect of one factor depends on the other. For the bakery data the two lines are nearly parallel: middle shelves sell best at both widths.

![Left: interaction plot of the bakery cell means, sales against shelf height with one line per width. Middle and right: schematic patterns with no interaction (parallel lines) and with a crossing interaction, where the marginal means of factor A are equal although A has a strong effect at each level of B.](./plots/interaction-plots.py)

### 14.1.3. The Factor Effects Model

**Definition 14.1.2 (Two-Way Factor Effects Model)** Define the overall mean and the factor level means

$$
\mu_{\cdot\cdot}=\frac{1}{ab}\sum_{i,j}\mu_{ij},\qquad \mu_{i\cdot}=\frac1b\sum_j\mu_{ij},\qquad \mu_{\cdot j}=\frac1a\sum_i\mu_{ij}.
$$
The **main effects** of $A$ and $B$ are $\alpha_i=\mu_{i\cdot}-\mu_{\cdot\cdot}$ and $\beta_j=\mu_{\cdot j}-\mu_{\cdot\cdot}$, and the **interaction effects** are

$$
(\alpha\beta)_{ij}=\mu_{ij}-(\mu_{\cdot\cdot}+\alpha_i+\beta_j)=\mu_{ij}-\mu_{i\cdot}-\mu_{\cdot j}+\mu_{\cdot\cdot}.
$$
Writing $\mu=\mu_{\cdot\cdot}$, the **two-way factor effects model** is

$$
Y_{ijk}=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}+\varepsilon_{ijk},\qquad \varepsilon_{ijk}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
with the constraints $\alpha_\cdot=\sum_i\alpha_i=0$, $\beta_\cdot=\sum_j\beta_j=0$, $(\alpha\beta)_{\cdot j}=\sum_i(\alpha\beta)_{ij}=0$ for all $j$ and $(\alpha\beta)_{i\cdot}=\sum_j(\alpha\beta)_{ij}=0$ for all $i$.

The main effect $\alpha_i$ is the adjustment of the overall mean for level $i$ of $A$, and $\beta_j$ that for level $j$ of $B$. The interaction $(\alpha\beta)_{ij}$ is what the completely additive model $\mu+\alpha_i+\beta_j$ leaves unexplained: an additional adjustment that takes both $i$ and $j$ into account and cannot be explained by the previous ones. There is no interaction if and only if all $(\alpha\beta)_{ij}=0$, that is, $\mu_{ij}-\mu_{i'j}$ does not depend on $j$ (parallel lines in the interaction plot).

The constraints on the interactions consist of $a+b$ equations, of which $a+b-1$ are linearly independent (the sum of the row equations equals the sum of the column equations). So the parameters have $1+(a-1)+(b-1)+(a-1)(b-1)=ab$ free components, the same number as the cell means, and the model has $ab-1$ degrees of freedom: $a-1$ for $A$, $b-1$ for $B$ and $(a-1)(b-1)$ for the interaction.

**Proposition 14.1.1** In a balanced design the least squares estimators under the sum-to-zero constraints are

$$
\hat\mu=\bar Y_{\cdot\cdot\cdot},\qquad \hat\alpha_i=\bar Y_{i\cdot\cdot}-\bar Y_{\cdot\cdot\cdot},\qquad \hat\beta_j=\bar Y_{\cdot j\cdot}-\bar Y_{\cdot\cdot\cdot},\qquad \widehat{(\alpha\beta)}_{ij}=\bar Y_{ij\cdot}-\bar Y_{i\cdot\cdot}-\bar Y_{\cdot j\cdot}+\bar Y_{\cdot\cdot\cdot},
$$
where $\bar Y_{\cdot\cdot\cdot}=\sum_{i,j,k}Y_{ijk}/(abn)$, and $\hat\mu_{i\cdot}=\bar Y_{i\cdot\cdot}$, $\hat\mu_{\cdot j}=\bar Y_{\cdot j\cdot}$.

**Proof** The least squares estimators of the cell means are $\hat\mu_{ij}=\bar Y_{ij\cdot}$ (Theorem 12.2.1), and the parameters of Definition 14.1.2 are linear functions of the cell means; with $n_{ij}=n$, averaging the $\bar Y_{ij\cdot}$ over $j$, over $i$ or over both gives $\bar Y_{i\cdot\cdot}$, $\bar Y_{\cdot j\cdot}$ and $\bar Y_{\cdot\cdot\cdot}$. $\square$

For the bakery data, $\hat\mu=51$, $\hat\alpha=(-7,16,-9)$, $\hat\beta=(-1,1)$, and the interaction estimates are $\pm2$ for the bottom shelf and $\pm1$ for the other two, for example $\widehat{(\alpha\beta)}_{11}=45-44-50+51=2$.

R uses different constraints. The call `lm(sales ~ height * width)` takes the first level of each factor as the baseline, that is, $\alpha_1=0$, $\beta_1=0$, $(\alpha\beta)_{1j}=0$ for all $j$ and $(\alpha\beta)_{i1}=0$ for all $i$; the number of free parameters is the same.

| Common constraints | df | Constraints used by R | df |
|---|---|---|---|
| $\sum_i\alpha_i=0$ | $a-1$ | $\alpha_1=0$ | $a-1$ |
| $\sum_j\beta_j=0$ | $b-1$ | $\beta_1=0$ | $b-1$ |
| $\sum_i(\alpha\beta)_{ij}=0$ for all $j$, $\sum_j(\alpha\beta)_{ij}=0$ for all $i$ | $(a-1)(b-1)$ | $(\alpha\beta)_{1j}=0$ for all $j$, $(\alpha\beta)_{i1}=0$ for all $i$ | $ab-(a+b-1)=(a-1)(b-1)$ |

For the bakery data R reports the intercept $45$ (the cell $(1,1)$), $\hat\alpha_2=20$, $\hat\alpha_3=-5$, $\hat\beta_2=-2$, $\widehat{(\alpha\beta)}_{22}=\widehat{(\alpha\beta)}_{32}=6$, with standard errors $3.215$ for the main effect coefficients and $4.546$ for the interactions; for instance $\hat\mu_{22}=45+20-2+6=69$. The individual $t$-tests of these coefficients compare cells with the baseline and are rarely the questions of interest; in ANOVA we are interested in differences between levels rather than in the predictive ability of the model, and these are tested by the ANOVA table.

## 14.2. The Two-Way ANOVA Table

The total sum of squares splits into four parts, each the sum over all observations of a squared estimated effect:

$$
\begin{aligned}
\mathrm{SSA}&=\sum_{i,j,k}\hat\alpha_i^2=bn\sum_i(\bar Y_{i\cdot\cdot}-\bar Y_{\cdot\cdot\cdot})^2, & \mathrm{SSB}&=\sum_{i,j,k}\hat\beta_j^2=an\sum_j(\bar Y_{\cdot j\cdot}-\bar Y_{\cdot\cdot\cdot})^2,\\
\mathrm{SSAB}&=\sum_{i,j,k}\widehat{(\alpha\beta)}_{ij}^2=n\sum_{i,j}\widehat{(\alpha\beta)}_{ij}^2, & \mathrm{SSE}&=\sum_{i,j,k}(Y_{ijk}-\bar Y_{ij\cdot})^2,
\end{aligned}
$$
and $\mathrm{SSTO}=\sum_{i,j,k}(Y_{ijk}-\bar Y_{\cdot\cdot\cdot})^2=\mathrm{SSA}+\mathrm{SSB}+\mathrm{SSAB}+\mathrm{SSE}$ in a balanced design, because the cross products of the four components sum to zero under the constraints.

| Source | df | SS | MS | $F$ |
|---|---|---|---|---|
| $A$ | $a-1$ | $\mathrm{SSA}$ | $\mathrm{MSA}=\mathrm{SSA}/(a-1)$ | $\mathrm{MSA}/\mathrm{MSE}$ |
| $B$ | $b-1$ | $\mathrm{SSB}$ | $\mathrm{MSB}=\mathrm{SSB}/(b-1)$ | $\mathrm{MSB}/\mathrm{MSE}$ |
| $AB$ | $(a-1)(b-1)$ | $\mathrm{SSAB}$ | $\mathrm{MSAB}=\mathrm{SSAB}/[(a-1)(b-1)]$ | $\mathrm{MSAB}/\mathrm{MSE}$ |
| Error | $ab(n-1)$ | $\mathrm{SSE}$ | $\mathrm{MSE}=\mathrm{SSE}/[ab(n-1)]$ | |
| Total | $abn-1$ | $\mathrm{SSTO}$ | | |

**Theorem 14.2.1 (Expected Mean Squares)** In the balanced two-way factor effects model,

$$
\begin{aligned}
\mathbb{E}[\mathrm{MSE}]&=\sigma^2, & \mathbb{E}[\mathrm{MSA}]&=\sigma^2+\frac{bn}{a-1}\sum_i\alpha_i^2,\\
\mathbb{E}[\mathrm{MSB}]&=\sigma^2+\frac{an}{b-1}\sum_j\beta_j^2, & \mathbb{E}[\mathrm{MSAB}]&=\sigma^2+\frac{n}{(a-1)(b-1)}\sum_{i,j}(\alpha\beta)_{ij}^2.
\end{aligned}
$$
Moreover $\mathrm{SSE}/\sigma^2\sim\chi^2_{ab(n-1)}$, the four sums of squares are independent, and $\mathrm{SSA}/\sigma^2$, $\mathrm{SSB}/\sigma^2$, $\mathrm{SSAB}/\sigma^2$ have $\chi^2$ distributions with $a-1$, $b-1$, $(a-1)(b-1)$ degrees of freedom when the corresponding effects are zero.

The proof follows the one-way case (Theorem 12.2.2), using that the four components are orthogonal projections of $\boldsymbol{Y}$ onto mutually orthogonal subspaces. Each mean square has expectation $\sigma^2$ when its effects vanish and larger otherwise, which gives the three $F$-tests:

| Hypotheses | Statistic | Null distribution |
|---|---|---|
| $H_{0A}\colon\alpha_i=0$ for all $i$; $H_{1A}\colon\alpha_i\ne0$ for at least one $i$ | $F_A=\mathrm{MSA}/\mathrm{MSE}$ | $F_{a-1,\,ab(n-1)}$ |
| $H_{0B}\colon\beta_j=0$ for all $j$; $H_{1B}\colon\beta_j\ne0$ for at least one $j$ | $F_B=\mathrm{MSB}/\mathrm{MSE}$ | $F_{b-1,\,ab(n-1)}$ |
| $H_{0AB}\colon(\alpha\beta)_{ij}=0$ for all $(i,j)$; $H_{1AB}\colon(\alpha\beta)_{ij}\ne0$ for at least one $(i,j)$ | $F_{AB}=\mathrm{MSAB}/\mathrm{MSE}$ | $F_{(a-1)(b-1),\,ab(n-1)}$ |

The $p$-values are computed from these $F$ distributions, and a $p$-value at most $0.05$ declares the effect statistically significant. The interaction is examined first: if it is significant, the main effects must be interpreted with care, and the analysis proceeds with the cell means (for example, comparing the levels of $A$ separately at each level of $B$).

**Example 14.2.1** For the bakery data:

```r
fit <- lm(sales ~ height * width, data = a)
anova(fit)
```

| Source | df | SS | MS | $F$ | $p$ |
|---|---|---|---|---|---|
| height | 2 | 1544 | 772 | 74.71 | $5.8\times10^{-5}$ |
| width | 1 | 12 | 12 | 1.16 | 0.323 |
| height × width | 2 | 24 | 12 | 1.16 | 0.375 |
| Error | 6 | 62 | 10.33 | | |
| Total | 11 | 1642 | | | |

There are $6$ cells, so the model has $6-1=5$ degrees of freedom ($\mathrm{SSA}+\mathrm{SSB}+\mathrm{SSAB}=1580$, $F=30.58$ for the whole model). The interaction is not significant: the effect of the height of the display is similar for the regular and the wide displays. The height affects bread sales, while the width has no apparent effect.

Next we need to explain the height effect, with its three levels bottom, middle and top. We could rerun the analysis as a one-way ANOVA in height and use the methods of [3.3.13](/3.3.13), or, better, compare the heights within the two-factor model, which keeps the width in the error structure. Note how the error degrees of freedom depend on the model: $n_T-a=9$ with height alone, $n_T-a-b+1=8$ with both factors and no interaction, and $n_T-ab=6$ with the interaction. Tukey's method in the additive model gives

```r
mod <- aov(sales ~ height + width, data = a)
TukeyHSD(mod, "height")
```

the differences $\hat\mu_{2\cdot}-\hat\mu_{1\cdot}=23$ with 95% family-wise interval $[16.4,\ 29.6]$, $\hat\mu_{3\cdot}-\hat\mu_{1\cdot}=-2$ with $[-8.6,\ 4.6]$, and $\hat\mu_{3\cdot}-\hat\mu_{2\cdot}=-25$ with $[-31.6,\ -18.4]$: middle shelves sell about 23 to 25 more cases than bottom or top shelves, which do not differ.

## 14.3. Least Squares Means

In a balanced design the marginal mean of a level of $A$ is an equally weighted average over the levels of $B$. In an unbalanced design the raw marginal mean $\bar Y_{i\cdot\cdot}$ weights the cells by their sample sizes, so a difference between two levels of $A$ can reflect an unequal mix of $B$ levels rather than an effect of $A$.

**Definition 14.3.1 (Least Squares Means)** The **least squares means** (LS-means) of the levels of a factor are the means of the fitted model's predictions over a balanced reference grid: for level $i$ of $A$,

$$
\hat\mu_{i\cdot}^{\mathrm{LS}}=\frac1b\sum_{j=1}^b\hat\mu_{ij},
$$
where $\hat\mu_{ij}$ is the mean predicted by the fitted model for cell $(i,j)$ (with covariates, if any, set at reference values such as their means).

LS-means are also called estimated marginal means, predicted (population) margins, predicted means or model-based means. They are used to compare group responses when the data are unbalanced or when covariates come into play, and they are computed by `LSMEANS` in SAS, `margins` in Stata and the package `emmeans` in R. In a balanced design they equal the arithmetic marginal means.

**Example 14.3.1** For the balanced bakery data, the one-way model `lm(sales ~ 0 + height)` and the additive model `lm(sales ~ height + width)` give the same height means $44$, $67$, $42$; only the standard errors and degrees of freedom differ ($1.65$ on $9$ and $1.64$ on $8$ degrees of freedom). Now delete the first observation (47, in cell $(1,1)$). The raw mean of the bottom height becomes $(43+46+40)/3=43$, and the one-way model reports $43$. The additive model has coefficients $41$ (intercept), $24.5$ (height 2), $-0.5$ (height 3) and $3$ (width 2), so its predicted cell means are

| Width \ Height | 1 | 2 | 3 |
|---|---|---|---|
| 1 | 41 | 65.5 | 40.5 |
| 2 | 44 | 68.5 | 43.5 |

and the LS-means are $(41+44)/2=42.5$, $67$ and $42$. The raw mean $43$ gives the wide display, which sells more, two of the three remaining bottom-shelf observations; the LS-mean $42.5$ removes this imbalance. The name "predicted means" comes from this construction: the LS-mean of a level is the average of the model's predictions over the levels of the other factor.

```r
library(emmeans)
fit3 <- lm(sales ~ height + width, data = a[-1, ])
emmeans(fit3, ~ height)                                        # LS-means 42.5, 67, 42
emmeans(aov(sales ~ height + width, data = a[-1, ]),
        pairwise ~ height, adjust = "tukey")                   # Tukey comparisons of LS-means
```

In the model with interaction, `emmeans` averages the fitted cell means $\bar Y_{ij\cdot}$ (here $43$ and $43$ for the bottom shelf) and warns that the results may be misleading because the factor is involved in an interaction: when the interaction is real, an average over the levels of $B$ may not describe any actual condition.

## 14.4. Diagnostics for ANOVA Models

### 14.4.1. Residual Plots

The diagnostics for regression carry over to the ANOVA setting with some modifications. In the one-way model the predicted values are the cell means, $\hat Y_{ij}=\bar Y_{i\cdot}$, and the residuals are the differences between the observations and their cell means, $e_{ij}=Y_{ij}-\bar Y_{i\cdot}$. We look for outliers, variances that depend on the level, and non-normal errors:

- plot the responses $Y$ against the factor levels;
- check independence by a sequence plot of the residuals, when the order of the observations is available and meaningful;
- check normality by a **normal Q–Q plot** of the residuals;
- check equal variances by plotting the residuals against the fitted values (cell means) or the factor levels;
- use additional information, such as the time or place of the measurements, if possible.

**Example 14.4.1** Four brands of rust inhibitor are compared, with $r=4$ and $n=10$ units per brand; the response measures the effectiveness of the inhibitor. A plot of the responses against brand shows means that look different and a common spread. The ANOVA gives $\mathrm{SSTR}=15953$ on $3$ and $\mathrm{SSE}=221$ on $36$ degrees of freedom, $F=866.1$, $p<2\times10^{-16}$.

```r
a1 <- read.table("CH17TA02.txt")
colnames(a1) <- c("eff", "brand", "unit")
a1$brand <- as.factor(a1$brand)
plot(eff ~ brand, data = a1)                # responses against the factor
fit1 <- aov(eff ~ brand, data = a1)
summary(fit1)
par(mfrow = c(2, 2)); plot(fit1); par(mfrow = c(1, 1))   # residual plots
```

The departures from the assumptions are judged as in regression:

- Non-normality: use a normal probability plot. If the variances are unequal, the plot of the ordinary residuals often indicates non-normality falsely, so one should first transform (Section 14.5) and then recheck. Normality is the least important assumption: almost all ANOVA procedures are robust to minor departures from it.
- Non-independence: if the data were obtained in a time sequence, plot the residuals against time. A pattern indicates non-independence: positive serial correlation (adjacent residuals tend to have the same sign) or negative serial correlation (adjacent residuals tend to have opposite signs). Non-independence usually has serious effects on the inferences, making them invalid.
- Extreme values: studentized or studentized deleted residuals classify outliers as before ([3.3.11](/3.3.11)). In the one-way model the **leverage** of $Y_{ij}$, the diagonal element of the **hat matrix**, is $1/n_i$, because the fitted value $\bar Y_{i\cdot}$ gives weight $1/n_i$ to each observation of its level. When the cell sizes are equal, all leverages are equal and no point has more leverage than another.

### 14.4.2. Tests for Equal Variances

Formal tests supplement the plots. For normality there are the **Shapiro–Wilk test**, the **Anderson–Darling test** and the **Kolmogorov–Smirnov test**. For the homogeneity of variance (**homoscedasticity**),

$$
H_0\colon\sigma_1^2=\sigma_2^2=\cdots=\sigma_r^2\qquad\text{versus}\qquad H_1\colon\text{not all }\sigma_i^2\text{ are equal},
$$
several tests are available; this matters because ANOVA results can be sensitive to the homogeneity of variance assumption, and some of the tests are themselves sensitive to the normality assumption. **Bartlett's test** is essentially the **likelihood ratio test** of $H_0$ under normality and is very sensitive to non-normality; the modified **Levene's test** (the **Brown–Forsythe test** of [3.3.5](/3.3.5)) performs a one-way ANOVA on the absolute deviations $\lvert Y_{ij}-\tilde Y_i\rvert$ from the level medians and is robust; Hartley's test is the simplest.

**Definition 14.4.1 (Hartley's Test)** For $r$ levels with equal sample sizes $n_i=n$ and normal errors, **Hartley's test** of equal variances uses

$$
H^*=\frac{\max_is_i^2}{\min_is_i^2},
$$
which under $H_0$ has the distribution $H(r,n-1)$ tabulated by Hartley; $H_0$ is rejected for large $H^*$.

As a quick rule of thumb, a ratio of the largest to the smallest standard deviation above $2$, that is $H^*>4$, is a reason for concern.

**Example 14.4.2** Five types of solder flux are compared, with $n=8$ joints per type; the response is the pull strength, the force in pounds required to break the joint. The scatter plot raises doubts about equal spread.

```r
library(car)
leveneTest(a1$strength, a1$type)            # modified Levene (center = median)
```

The modified Levene test gives $F=2.936$ on $4$ and $35$ degrees of freedom, $p=0.034$, so we reject the hypothesis of equal variances. The sample variances by type are $1.531$, $1.570$, $6.183$, $0.667$, $0.592$, so $H^*=6.183/0.592=10.44$, well above $4$ and above the $5\%$ critical value $H_{0.95}(5,7)\approx9.7$.

Experience from experimental design qualifies these findings. The ANOVA $F$-test is only slightly affected by non-constant variance as long as the sample sizes are equal, and Scheffé's multiple comparison procedure is also fairly robust to unequal variances when the cell sizes are equal; other pairwise comparisons can be greatly affected by unequal variances. Using equal sample sizes minimizes these effects, which is one reason for the importance of balanced designs.

## 14.5. Remedial Measures

The remedies for an ANOVA model parallel those for regression:

- delete outliers, after asking whether their removal matters and whether it is valid;
- use weights (weighted least squares);
- transform the response;
- use nonparametric procedures.

### 14.5.1. Weighted ANOVA

For the solder flux data the assumption of equal variances was rejected, and there are no obvious outliers, so we consider a weighted ANOVA. In weighted regression ([3.3.12](/3.3.12)) we model how the standard deviation depends on the explanatory variable and use weights inversely proportional to the estimated variances. With a factor this is simpler: compute the **sample variance** $s_i^2$ of each level and use the reciprocals $w_{ij}=1/s_i^2$ as weights.

```r
library(plyr)
a2 <- ddply(a1, ~type, summarise, freq = length(strength),
            mean = mean(strength), s2 = var(strength))
a2$wt <- 1 / a2$s2
a3 <- merge(a1, a2, by = "type")
weightedfit <- lm(strength ~ type, data = a3, weights = wt)
anova(weightedfit)
```

The weighted ANOVA gives a treatment sum of squares $324.21$ on $4$ degrees of freedom and a residual sum of squares $35.00$ on $35$, so $F=81.05$ and $p<2.2\times10^{-16}$. The residual mean square is exactly $1$: within level $i$ all weights equal $1/s_i^2$, so the weighted fitted values are still the level means and the weighted error sum of squares is $\sum_i(n_i-1)s_i^2/s_i^2=n_T-r$. The $F$ statistic is therefore the weighted treatment mean square itself, a comparison of the level means in which each level counts according to its precision.

### 14.5.2. Transformations

**Example 14.5.1** A study records the time between computer failures at three locations, over five intervals each:

| Location | Time between failures |
|---|---|
| 1 | 4.41, 100.65, 14.45, 47.13, 85.21 |
| 2 | 8.24, 81.16, 7.35, 12.29, 1.61 |
| 3 | 106.19, 33.83, 78.88, 342.81, 44.33 |

The scatter plot shows a strongly right-skewed distribution (is $342.81$ an outlier, or is the distribution skewed?) and spreads that grow with the mean: the sample variances are $1789$, $1103$ and $16167$. The **Box–Cox transformation** ([3.4.4](/3.4.4), [3.3.6](/3.3.6)) chooses the power $\lambda$ that maximizes the profile likelihood of the one-way model for the transformed response.

```r
library(MASS)
a3 <- read.table("CH18TA05.txt")
colnames(a3) <- c("time", "location", "interval")
bc <- boxcox(time ~ as.factor(location), data = a3, lambda = seq(-2, 2, by = 0.2))
lambda <- bc$x[which.max(bc$y)]             # about 0.10
a3$logtime <- log(a3$time)                  # lambda = 0 is within the confidence interval
```

The maximum is at $\hat\lambda\approx0.10$, and the approximate 95% confidence interval, about $[-0.2,\ 0.4]$, contains $0$, so we can simply use the logarithm. After the transformation the variances are $1.74$, $1.97$ and $0.82$: the spread is much more constant, and the ANOVA can be carried out on $\log Y$.

![Left: time between computer failures by location. Middle: Box-Cox profile log-likelihood with the approximate 95% confidence interval for lambda. Right: the log-transformed times by location.](./plots/box-cox-failures.py)

### 14.5.3. A Nonparametric Test

Nonparametric procedures do not depend on the distribution of the error terms; often the only requirement is that the distributions are continuous. For one-way ANOVA the hypothesis is that the $r$ populations under study have continuous distributions that differ only with respect to location.

**Definition 14.5.1 (Kruskal–Wallis Test)** Rank all $n_T$ observations together from $1$ to $n_T$, and let $\bar R_{i\cdot}$ be the mean rank of the observations at level $i$. The **Kruskal–Wallis test** rejects the hypothesis that all $r$ distributions are identical for large values of

$$
H=\frac{12}{n_T(n_T+1)}\sum_{i=1}^rn_i\Big(\bar R_{i\cdot}-\frac{n_T+1}{2}\Big)^2,
$$
whose null distribution is approximately $\chi^2_{r-1}$ (exact tables exist for small samples).

$H$ is a treatment sum of squares computed from the ranks, divided by the variance $n_T(n_T+1)/12$ of the ranks; for $r=2$ it is equivalent to the two-sided **Wilcoxon rank-sum test** ([3.2.6](/3.2.6)). Because only the ranks are used, the test is insensitive to outliers and to skewness, and it is unchanged by any increasing transformation of the response.

```r
kruskal.test(eff ~ brand, data = a1)        # rust inhibitor data
```

For the rust inhibitor data the Kruskal–Wallis statistic is $33.70$ on $3$ degrees of freedom, $p=2.3\times10^{-7}$, confirming the large differences between the brands found by the $F$-test.

## Summary {#summary}

- The two-way cell means model $Y_{ijk}=\mu_{ij}+\varepsilon_{ijk}$ is a one-way model in the $ab$ cells; the factor effects model $\mu_{ij}=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}$ splits the cell means into main effects and interactions, identified by sum-to-zero constraints (R uses baseline constraints instead).
- The two-way ANOVA table partitions $\mathrm{SSTO}=\mathrm{SSA}+\mathrm{SSB}+\mathrm{SSAB}+\mathrm{SSE}$ with $a-1$, $b-1$, $(a-1)(b-1)$ and $ab(n-1)$ degrees of freedom; each effect is tested against $\mathrm{MSE}$. Examine the interaction (and the interaction plot) before interpreting the main effects.
- Least squares means average the model's predicted cell means over the levels of the other factor; they differ from the raw marginal means in unbalanced designs.
- ANOVA diagnostics use residuals from the cell means; normality matters least and independence most. Equal variances are tested by Bartlett's, the modified Levene and Hartley's tests; balanced designs make the $F$-test robust to unequal variances.
- Remedies are weighted ANOVA with $w=1/s_i^2$, transformations chosen by Box–Cox, and the rank-based Kruskal–Wallis test.
