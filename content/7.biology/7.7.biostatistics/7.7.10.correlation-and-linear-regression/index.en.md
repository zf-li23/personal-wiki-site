---
title: Correlation and Linear Regression
description: Scatter plots and the meaning and pitfalls of Pearson's correlation coefficient (Anscombe's quartet); the t test for the correlation coefficient, Fisher's z-transformation and comparison of two correlations; least squares for simple linear regression, the meaning of the slope and regression toward the mean; inference for the slope, the ANOVA table, the coefficient of determination, confidence intervals for the mean and prediction intervals for an individual; residual diagnostics and log transformation; standard curves and inverse prediction; multiple linear regression, partial regression coefficients and confounding; dummy variables and interaction terms; model selection, collinearity and influential points; partial correlation. The running example is children's FEV against height and smoking, with the DNase ELISA standard curve as the laboratory example.
source_hash: 247e6db38640
---

The preceding chapters compared "groups": the FEV of two groups of children, tooth growth at three doses. In many problems, however, the independent variable is continuous: how does FEV change with height? What is the relationship between optical density and DNase concentration? Can a mother's weight predict her baby's birth weight? The association between two continuous variables is described by the **correlation coefficient**; predicting one variable from another while controlling for the influence of other variables is the business of regression. This chapter starts from the scatter plot and Pearson's correlation coefficient and treats inference for the correlation coefficient; it then covers simple linear regression (least squares, inference, prediction, diagnostics), its commonest use in the laboratory, the standard curve and inverse prediction, and finally multiple linear regression. The main thread returns to the question posed in [7.7.1](/7.7.1): among the 654 children in East Boston the FEV of smokers is actually higher ([7.7.7](/7.7.7) Example 7.3.2), and this is caused by age and body size; multiple regression lets us for the first time "adjust" for these variables within one model, and the coefficient of smoking then becomes negative. The mathematics of regression (properties of the least-squares estimators, the matrix form, the derivation of diagnostic statistics) is treated fully in [3.3](/3.3); here we give only results, conditions and uses in biomedicine. Nonlinear standard curves and enzyme-kinetic fitting are in [7.7.11](/7.7.11), and analysis of variance as a special case of regression is in [7.7.12](/7.7.12).

## 10.1. Scatter Plots and the Correlation Coefficient

### 10.1.1. Pearson's Correlation Coefficient

The first step in analyzing two continuous variables is always a scatter plot: it shows the direction of the association, its form (a line or a curve), its strength, whether there are outliers, and whether several distinct groups are mixed together.

**Formula 10.1.1 (Pearson's Correlation Coefficient)** The sample correlation coefficient of $n$ pairs of observations $(x_i, y_i)$ is

$$
r = \frac{\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)}{\sqrt{\sum_{i=1}^n (x_i - \bar x)^2 \sum_{i=1}^n (y_i - \bar y)^2}} = \frac{s_{xy}}{s_x s_y},
$$
where $s_{xy}$ is the sample **covariance** and $s_x, s_y$ are the sample standard deviations. $-1 \le r \le 1$, and $\lvert r\rvert = 1$ if and only if all points lie on a straight line.

$r$ estimates the population **correlation coefficient** $\rho = \operatorname{Cov}(X, Y)/\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}$ ([3.1.10](/3.1.10)). It is a standardized covariance: it has no units, is unchanged by linear transformations of $x$ or $y$ (such as converting inches to centimeters), and is unchanged when $x$ and $y$ are interchanged. It measures the strength of linear association: $r^2$ is the proportion of the variation in $y$ that can be explained by a linear function of $x$ (Section 10.4).

**Example 10.1.1 (FEV)** Among the 654 children, the correlation of FEV with height is $r = 0.868$, with age $r = 0.756$, and between height and age $r = 0.792$. Height has more linear explanatory power for FEV ($r^2 = 0.754$) than age ($0.572$): lung size is more directly determined by body size.

:::

By convention $\lvert r\rvert < 0.3$ is often called weak, $0.3$–$0.7$ moderate and $> 0.7$ strong, but this grading is only a habit: in biomedicine an association with $r = 0.3$ may be important (blood pressure and later cardiovascular events), and $r = 0.95$ may still be insufficient (agreement between two measurement methods, [7.7.11](/7.7.11), Section 11.3).

### 10.1.2. Pitfalls of the Correlation Coefficient

The same $r$ can come from entirely different relationships. Anscombe (1973) constructed four data sets of 11 points each in which the means and variances of $x$ and $y$, the correlation coefficient (0.816) and the least-squares line ($y = 3.00 + 0.500x$) are all the same:

![Anscombe's quartet: the four data sets have identical means, variances, correlation coefficient (r = 0.82) and least-squares line, yet the relationships are entirely different. I: roughly linear; II: a smooth curve; III: a linear relationship plus one outlier; IV: all x equal except one point, so the correlation is produced entirely by that single point](./plots/anscombe.py)

Several principles for the use of the correlation coefficient follow:

| Pitfall | What happens | Remedy |
|---|---|---|
| Nonlinearity | A strong curved relationship can have a small $r$ (such as a U-shaped dose response) | Draw the scatter plot first; for monotone relationships use **Spearman's rank correlation coefficient** ([7.7.8](/7.7.8)) |
| Outliers and influential points | A single point can create or erase a correlation (panels III and IV) | Check the data; report the result without the point; use rank correlation |
| Pooling heterogeneous groups | Two groups each unrelated may appear "correlated" when pooled because their means differ, or the reverse | Plot and compute by group (confounding in Section 10.7) |
| Restricted range | Computed only among children 150–160 cm tall, $r$ is greatly reduced | State the range of the sample; values of $r$ from different ranges are not comparable |
| Correlation is not agreement | If one method always reads twice the other, $r = 1$ | Use Bland–Altman analysis for method comparison ([7.7.11](/7.7.11)) |
| Correlation is not causation | Ice cream sales are positively correlated with drownings (both depend on temperature) | Study design and causal inference ([7.7.15](/7.7.15)) |

## 10.2. Inference for Correlation

### 10.2.1. Testing $\rho = 0$

Suppose $(X, Y)$ has a bivariate normal distribution. Under $H_0\colon \rho = 0$,

$$
t = \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}} \sim t_{n-2}.
$$
This statistic is identical to the t statistic for the regression slope in Section 10.4: testing "no linear correlation" and testing "the slope is 0" are the same test. For FEV and height, $t = 0.868\sqrt{652}/\sqrt{1 - 0.868^2} = 44.7$ and $p < 10^{-100}$.

A small p-value shows only that $\rho \ne 0$, not that the correlation is strong: with $n = 1000$, $r = 0.07$ is already significant at the 0.05 level. A report of a correlation should give $r$ and its confidence interval, not the p-value alone.

### 10.2.2. Fisher's z-Transformation

When $\rho \ne 0$ the sampling distribution of $r$ is skewed (more so the closer $\rho$ is to $\pm 1$) and its variance also depends on $\rho$, so the normal approximation cannot be used directly. R. A. Fisher found a transformation that makes it approximately normal with stable variance:

**Definition 10.2.1 (Fisher z-Transformation)** Let $r$ be the sample correlation coefficient of $n$ pairs of observations from a bivariate normal population. The quantity

$$
z = \operatorname{artanh} r = \frac12 \ln\frac{1 + r}{1 - r}
$$
is called the **Fisher z-transformation** of $r$. For large $n$, $z$ is approximately $\mathcal{N}\bigl(\operatorname{artanh}\rho,\ 1/(n - 3)\bigr)$.

This gives a confidence interval for $\rho$ (compute the interval on the $z$ scale and transform back with $\tanh$) and a test of $H_0\colon \rho = \rho_0$ with $Z = (z - z_0)\sqrt{n - 3}$. When $\lvert r\rvert$ is small, $z \approx r$; when $r$ is close to 1 the two differ greatly ($z = 2.00$ for $r = 0.964$).

**Example 10.2.1** For FEV and height, $z = \operatorname{artanh} 0.868 = 1.325$ with standard error $1/\sqrt{651} = 0.0392$; the 95% interval on the $z$ scale is $1.325 \pm 1.96 \times 0.0392$, which transforms back to $\rho \in (0.848, 0.886)$. The interval is asymmetric about $r$, longer on the side toward 0.

**Example 10.2.2 (Weights of Fathers and Sons)** Suppose the weights of 100 fathers and their eldest sons are measured and $r = 0.38$. If a polygenic model predicts a correlation of 0.5 between first-degree relatives, are the data consistent with it? $z = 0.400$, $z_0 = \operatorname{artanh} 0.5 = 0.549$, $Z = (0.400 - 0.549)\sqrt{97} = -1.47$, and the two-sided $p = 0.14$: we do not reject $\rho = 0.5$. The 95% interval for $\rho$ is $(0.20, 0.54)$, which contains 0.5 and also shows that 100 pairs estimate $\rho$ rather crudely.

### 10.2.3. Comparing Two Correlation Coefficients

To test the difference between the correlation coefficients $r_1, r_2$ of two independent samples (sizes $n_1, n_2$):

$$
Z = \frac{z_1 - z_2}{\sqrt{1/(n_1 - 3) + 1/(n_2 - 3)}} \ \overset{H_0}{\approx}\ \mathcal{N}(0, 1).
$$

**Example 10.2.3 (Familial Correlation of Blood Pressure)** Imagine a study comparing the correlation of blood pressure between mothers and children: $r_1 = 0.35$ for 1000 pairs of children raised by their biological mothers and $r_2 = 0.06$ for 100 pairs raised by adoptive mothers. A stronger correlation in the biological group would suggest a genetic contribution. $z_1 = 0.365$, $z_2 = 0.060$, $Z = 0.305/\sqrt{1/997 + 1/97} = 2.87$, and $p = 0.004$. Note that one must not test the two groups separately (biological group $p < 10^{-29}$, adopted group $p = 0.55$) and then say "one is significant and the other is not, so they differ": contrasting two p-values is not a test of the difference, and the adopted group is nonsignificant mainly because it has only 100 pairs.

:::

Two correlation coefficients computed on the same individuals (such as FEV with height and FEV with age, which share FEV) are not independent, and a method that takes the covariance between the correlation coefficients into account (such as the Steiger test) must be used instead of the formula above.

## 10.3. Simple Linear Regression

### 10.3.1. The Model and Least Squares

Correlation is symmetric; regression is asymmetric: it regards one variable $y$ (the dependent variable, response) as a function of another variable $x$ (the independent variable, predictor) plus random error.

**Formula 10.3.1 (Simple Linear Regression)** The **simple linear regression model** ([3.3.2](/3.3.2)) is

$$
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \qquad \varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2), \quad i = 1, \dots, n.
$$
The method of **least squares** chooses $b_0, b_1$ to minimize the residual sum of squares $\mathrm{SSE} = \sum (y_i - b_0 - b_1 x_i)^2$; the solution is

$$
b_1 = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^2} = r\,\frac{s_y}{s_x}, \qquad b_0 = \bar y - b_1 \bar x;
$$
$\sigma$ is estimated (the standard error of estimate) by $s = \sqrt{\mathrm{SSE}/(n - 2)}$.

The assumptions of the model can be listed as four: the mean of $y$ is a linear function of $x$ (linearity), the observations are independent (independence), $y$ is normal given $x$ (normality), and the variance does not change with $x$ (equal variance). $x$ is regarded as fixed and free of measurement error; when $x$ also has error the slope is underestimated ([7.7.11](/7.7.11), Section 11.3).

Meaning of the slope $b_1$: for each unit increase in $x$, the mean of $y$ changes by $b_1$ units. It describes the average trend in the population, not the law of change for each individual; the cross-sectional slope "each 1 cm of height goes with 0.052 L more FEV" compares children of different heights and not the change in the same child after growing 1 cm (which requires longitudinal data, [7.7.17](/7.7.17)).

**Example 10.3.1 (FEV and Height)** With height converted from inches to centimeters, the least-squares line for the 654 children is

$$
\widehat{\mathrm{FEV}} = -5.433 + 0.0520 \times \text{height (cm)},
$$
with $s = 0.431$ L. For each 10 cm of height, FEV is on average 0.52 L higher. The intercept $-5.43$ L is the "FEV" at height 0 and has no practical meaning: the regression line can be used only within the range of the data (117–188 cm), and extrapolation beyond it has no basis. Check: $b_1 = r s_y/s_x = 0.868 \times 0.867/14.49 = 0.0520$.

### 10.3.2. Regression, Correlation and Regression Toward the Mean

From $b_1 = r s_y/s_x$ the regression line can be written in standardized variables ($z$-scores):

$$
\frac{\hat y - \bar y}{s_y} = r\,\frac{x - \bar x}{s_x}.
$$
When $x$ is 1 standard deviation above the mean, the predicted $y$ is only $r$ standard deviations above the mean. Unless $\lvert r\rvert = 1$, the prediction is always "closer to the mean" than $x$: this is the **regression toward the mean** that Galton found in the 1880s when studying the heights of parents and children ([3.3.1](/3.3.1)): very tall parents have children who are tall on average, but not as tall as the parents; hence the word "regression". It is a necessary statistical phenomenon for any two variables that are not perfectly correlated and not the effect of heredity or any biological mechanism; predicting the parents from the children's heights would "regress" in the same way.

The asymmetry of regression is also seen here: the regression line of $y$ on $x$ differs from that of $x$ on $y$ unless $\lvert r\rvert = 1$. In the FEV data the slope of the regression of height on FEV is 14.5 cm/L, not $1/0.0520 = 19.2$ cm/L. Which variable goes on the left depends on the research question: to predict FEV, regress FEV on height.

The consequences of regression toward the mean are everywhere in medicine: patients enrolled for "blood pressure above a certain value" will on average have lower pressure at the second measurement even if nothing is done ([7.7.7](/7.7.7), Section 7.1.3); "the worst class improves the most after tutoring" is the same. Distinguishing a true effect from regression toward the mean requires a randomized controlled comparison.

## 10.4. Inference for Regression

### 10.4.1. Testing the Slope and the ANOVA Table

Under the model of Formula 10.3.1, the **standard error** of $b_1$ is $\operatorname{se}(b_1) = s/\sqrt{\sum (x_i - \bar x)^2}$, and

$$
t = \frac{b_1 - \beta_1}{\operatorname{se}(b_1)} \sim t_{n-2}.
$$
The test of $H_0\colon \beta_1 = 0$ is the same as the correlation test of Section 10.2.1. A $100(1-\alpha)\%$ confidence interval for $\beta_1$ is $b_1 \pm t_{n-2, \alpha/2}\operatorname{se}(b_1)$.

The total variation can be decomposed into a part explained by the regression and a residual part:

$$
\underbrace{\sum (y_i - \bar y)^2}_{\mathrm{SST}} = \underbrace{\sum (\hat y_i - \bar y)^2}_{\mathrm{SSR}} + \underbrace{\sum (y_i - \hat y_i)^2}_{\mathrm{SSE}},
$$
and the **coefficient of determination** $R^2 = \mathrm{SSR}/\mathrm{SST}$ is the proportion of the variation in $y$ explained by the regression; in simple regression $R^2 = r^2$. Writing the decomposition as an **ANOVA table**:

| Source | Degrees of freedom | Sum of squares | Mean square | $F$ |
|---|---|---|---|---|
| Regression | 1 | $\mathrm{SSR}$ | $\mathrm{MSR} = \mathrm{SSR}$ | $\mathrm{MSR}/\mathrm{MSE}$ |
| Residual | $n - 2$ | $\mathrm{SSE}$ | $\mathrm{MSE} = s^2$ | |
| Total | $n - 1$ | $\mathrm{SST}$ | | |

In simple regression $F = t^2$ and the two tests are equivalent; in multiple regression the $F$ test is of all slopes being 0 simultaneously (Section 10.7).

**Example 10.4.1** FEV on height: $b_1 = 0.05196$, $\operatorname{se}(b_1) = 0.00116$, $t = 44.7$, and the 95% interval is $(0.0497, 0.0542)$ L/cm.

| Source | Degrees of freedom | Sum of squares | Mean square | $F$ |
|---|---|---|---|---|
| Height | 1 | 369.99 | 369.99 | 1994.7 |
| Residual | 652 | 120.93 | 0.1855 | |
| Total | 653 | 490.92 | | |

$R^2 = 369.99/490.92 = 0.754$: height explains three quarters of the variation in FEV.

### 10.4.2. Confidence Interval for the Mean and Prediction Interval for an Individual

At $x = x_0$ the regression line gives $\hat y_0 = b_0 + b_1 x_0$. It can answer two different questions:

**Formula 10.4.1 (Confidence Interval and Prediction Interval)** At $x_0$,

$$
\text{confidence interval for the mean response } \beta_0 + \beta_1 x_0 \text{:}\quad \hat y_0 \pm t_{n-2,\alpha/2}\, s\sqrt{\frac1n + \frac{(x_0 - \bar x)^2}{\sum (x_i - \bar x)^2}},
$$

$$
\text{prediction interval for a new individual } y_0 \text{:}\quad \hat y_0 \pm t_{n-2,\alpha/2}\, s\sqrt{1 + \frac1n + \frac{(x_0 - \bar x)^2}{\sum (x_i - \bar x)^2}}.
$$

The former describes the uncertainty of "what is the mean FEV of children 160 cm tall" and tends to 0 as $n$ grows; the latter describes "what will the FEV of one child 160 cm tall be", in which the "1" is the variation of an individual about the mean and does not disappear however large the sample. Both are narrowest at $x_0 = \bar x$ and wider toward either end (these are pointwise intervals; for simultaneous bands for the whole line see the **confidence band**, [3.3.4](/3.3.4)). The width depends on the confidence level, the residual standard deviation $s$, the sample size and the distance of $x_0$ from $\bar x$.

**Example 10.4.2** At a height of 160 cm the estimated mean FEV is 2.881 L with 95% confidence interval $(2.846, 2.916)$; for one child 160 cm tall, the 95% **prediction interval** for FEV is $(2.03, 3.73)$ L. At 140 cm these are 1.842, $(1.793, 1.890)$ and $(0.99, 2.69)$. Normal reference values of lung function are precisely such prediction intervals: the 2.5th to 97.5th percentiles of FEV in normal persons of given height (and age and sex) (the reference interval of [7.7.2](/7.7.2)).

![FEV and height of 654 children (East Boston, Tager et al. 1979; public version Kahn 2005). A: the least-squares line, the 95% confidence band for the mean FEV (narrow) and the 95% prediction band for a single child (wide); the prediction band is too wide for short children and too narrow for tall children, which does not match the scatter of the data. B: regression of log FEV on height, back-transformed to the original scale: the fitted curve bends upward and the prediction band widens with height, in agreement with the data](./plots/fev-height-bands.py)

## 10.5. Model Checking

### 10.5.1. Residual Plots

All four assumptions of the model are checked with residuals (**regression diagnostics**, [3.3.5](/3.3.5)). The three most useful plots are:

- The **residual plot** of residuals against fitted values: it should be a horizontal band around 0. Curvature indicates that linearity fails, and a funnel shape indicates that the variance changes with the mean.
- The **normal Q–Q plot** of the residuals: it checks normality; for inference, mild non-normality does not matter in large samples (**central limit theorem**), while heavy tails and outliers do.
- Residuals plotted against time, measurement order or batch: they check independence.

Linear regression is differently sensitive to the four assumptions: if linearity is wrong, the meaning of the slope is wrong; unequal variance distorts the standard errors and prediction intervals (prediction intervals are most affected); normality mainly affects small samples and prediction intervals; and violation of independence (repeated measurements on the same individual, members of the same family) badly underestimates the standard errors and has the most serious consequences (pseudoreplication in [7.7.12](/7.7.12), and [7.7.17](/7.7.17)).

### 10.5.2. Log Transformation of FEV

**Example 10.5.1** The residuals of the linear model of FEV on height (Example 10.3.1) have two problems (panel A below): they spread out as the fitted value grows (dividing the children into thirds by height, the residual standard deviations are 0.29, 0.37 and 0.59 L), and the smooth curve is slightly U-shaped, a quadratic term in height being highly significant ($p = 6 \times 10^{-14}$). Physiologically, lung volume is proportional to the cube of height, and FEV grows in proportion to height rather than by a fixed amount; a variance that increases with the mean is characteristic of data of the **log-normal distribution** type. Using instead

$$
\ln \mathrm{FEV} = -2.271 + 0.02052 \times \text{height (cm)}, \qquad s = 0.151,
$$
the residual standard deviations in the three height groups are 0.145, 0.141 and 0.164, and the residual plot has no systematic curvature (panel B below); $R^2$ rises from 0.754 to 0.796. The slope on the log scale has a direct interpretation: each 1 cm of height goes with an average FEV higher by $\mathrm{e}^{0.0205} - 1 = 2.1\%$, and each 10 cm with $\mathrm{e}^{0.205} - 1 = 22.8\%$. The back-transformed prediction interval widens with height (panel B of the figure above): at 175 cm it is $(2.78, 5.03)$ L, which matches the actual scatter of tall children better than the $(2.81, 4.51)$ of the linear model.

The two ends of the Q–Q plot (panel C below) deviate slightly, and the Shapiro–Wilk test on the 654 observations is accordingly significant ($p < 10^{-5}$), but such a deviation has no practical effect on inference for the slope. Do not abandon regression because a normality test is "significant" in a large sample: judge the size and direction of the departure from a graph.

![Residual diagnostics for the regression of FEV on height (654 children, Tager et al. 1979; public version Kahn 2005). A: residuals of the linear model against fitted values; the scatter widens as the fitted value increases and the smooth curve (orange) bends slightly. B: residuals of the log model; the scatter is essentially constant. C: normal Q–Q plot of the standardized residuals of the log model. D: leverage and studentized residuals of the full log model (age, height, sex, smoking), with point area proportional to Cook's distance; the dashed line is leverage 2p/n and the dotted lines are ±3; the point with the largest Cook's distance is a child recorded as 8 years old and 171 cm tall](./plots/fev-diagnostics.py)

:::

Commonly used transformations: logarithms for right-skewed positive quantities (concentrations, titers, FEV); square roots for counts; the logit or arcsine square root for proportions. The transformation can be chosen systematically by the **Box–Cox transformation** ([3.4.4](/3.4.4)), but the best transformation often comes from understanding the mechanism ("changing proportionally" means logarithm).

### 10.5.3. Outliers and Influential Points

An **outlier** is a point with an especially large residual; a point with high **leverage** is an observation whose $x$ is far from the others; points that are both have the greatest influence on the fit, measured by **Cook's distance** ([3.3.6](/3.3.6)). In panel D above the observation with the largest Cook's distance is a child recorded as 8 years old, 171 cm (67.5 in) tall and with FEV 1.72 L: such a height is extremely rare at 8 years, and the FEV is far below that of children of the same height, so it is probably a data-entry error. The principles of handling it: check the original records; if an error can be confirmed, correct or delete it; if not, keep it and report whether the conclusion changes without it (here, without it the coefficient of smoking is still $-0.0461$, with $p$ changing from 0.028 to 0.026). A point must not be deleted merely because it "looks bad".

## 10.6. Standard Curves and Inverse Prediction

The commonest use of linear regression in the laboratory is the **calibration curve** (the standard curve, [6.4.1](/6.4.1)): standards of known concentration are measured to give a signal (absorbance, fluorescence, peak area), the signal is fitted against concentration, and the concentration of an unknown sample is then deduced from its signal. The direction of regression is then the opposite of the direction of use: we fit the regression of $y$ (signal) on $x$ (concentration) but in use we find $x$ from $y$; this is **inverse prediction** ([3.3.6](/3.3.6)).

**Formula 10.6.1 (Inverse Prediction)** Suppose the standard curve $y = b_0 + b_1 x$ has been fitted from $n$ standards, and an unknown sample measured $m$ times (replicate wells) has mean signal $\bar y_0$. The estimate of the concentration is

$$
\hat x_0 = \frac{\bar y_0 - b_0}{b_1},
$$
with approximate standard error

$$
\operatorname{se}(\hat x_0) \approx \frac{s}{\lvert b_1\rvert}\sqrt{\frac1m + \frac1n + \frac{(\bar y_0 - \bar y)^2}{b_1^2 \sum (x_i - \bar x)^2}},
$$
and an approximate 95% interval is $\hat x_0 \pm t_{n-2,0.025}\operatorname{se}(\hat x_0)$. The approximation is good when $g = t^2 s^2/(b_1^2 \sum (x_i - \bar x)^2)$ is much smaller than 1 (the slope is estimated precisely); otherwise the exact Fieller interval is used.

The three terms correspond to three sources of uncertainty: the measurement error of the unknown sample itself ($1/m$, smaller with more replicates), the position of the standard curve ($1/n$) and its slope (the last term, which is smallest when $\bar y_0$ falls in the middle of the range of standard signals).

**Example 10.6.1 (DNase ELISA)** In the rat serum DNase ELISA used in [7.7.2](/7.7.2), run 1 had duplicate wells at each of 8 concentrations from 0.049 to 12.5 ng/mL. Fitting a line to the lowest 5 concentrations (0.049–1.56 ng/mL, 10 wells) gives

$$
\mathrm{OD} = 0.041 + 0.380 \times \text{concentration (ng/mL)}, \qquad r^2 = 0.980, \quad s = 0.033.
$$
An unknown sample whose two wells have mean optical density 0.50 has $\hat x_0 = (0.50 - 0.041)/0.380 = 1.21$ ng/mL; $g = 0.013$, and the approximate 95% interval is $(1.04, 1.38)$ ng/mL. But the residual plot (panel B below) shows a systematic bias: the residuals are negative at both ends and positive in the middle, and the optical density has already begun to curve in this range. $r^2 = 0.98$ does not show that a line is appropriate: the $r^2$ of a standard curve is almost always high and is not a tool for checking linearity. With the four-parameter logistic model for the whole curve ([7.7.11](/7.7.11) Example 11.5.1), the estimate for the same sample is 1.13 ng/mL: the line overestimates by about 7%.

![A linear standard curve and inverse prediction: duplicate wells at the lowest 5 concentrations of run 1 of the rat serum DNase ELISA (Davidian and Giltinan 1995; R datasets::DNase). A: the least-squares line, the 95% prediction band for the mean of two wells, and the inverse prediction for an unknown sample with optical density 0.50 (arrow) with its 95% interval on the concentration axis. B: residuals: the line is systematically too low at both ends, indicating that the response has already started to curve](./plots/standard-curve-linear.py)

:::

Key points for a linear standard curve: the standards should cover the range of the unknown samples, with no extrapolation; check linearity within the range used (inspect the residuals, or use a lack-of-fit test with the replicates, [7.7.11](/7.7.11), Section 11.2); run a standard curve of its own on every plate and in every assay; and report an interval for the concentration of the unknown sample. When the variance of the signal increases with concentration, use **weighted least squares** ([7.7.11](/7.7.11), Section 11.2).

Another common use of linearization is to turn a nonlinear relationship into a straight line for fitting. The **Lineweaver–Burk plot** of enzyme kinetics ([6.3.17](/6.3.17)) rewrites the Michaelis–Menten equation $v = V_{\max}[\ce{S}]/(K_{\mathrm{M}} + [\ce{S}])$ as $1/v = 1/V_{\max} + (K_{\mathrm{M}}/V_{\max})(1/[\ce{S}])$ and regresses $1/v$ on $1/[\ce{S}]$. For the Puromycin data (cells treated with puromycin, 12 reactions) this gives $V_{\max} = 195.8$ and $K_{\mathrm{M}} = 0.048$ ppm, with regression $r^2 = 0.86$; direct nonlinear fitting gives $V_{\max} = 212.7$ and $K_{\mathrm{M}} = 0.064$ ppm. The difference arises from the distortion of the errors by the reciprocal transformation: at low concentrations $v$ is small, the error of $1/v$ is magnified many times, and the two least precise points dominate the line. Linearization can give rough starting values for the parameters, but the parameters should be estimated by nonlinear regression ([7.7.11](/7.7.11), Section 11.4).

## 10.7. Multiple Linear Regression

### 10.7.1. The Model and Partial Regression Coefficients

**Formula 10.7.1 (Multiple Linear Regression)** The **multiple linear regression model** ([3.3.7](/3.3.7)) is

$$
y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_p x_{ip} + \varepsilon_i, \qquad \varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2),
$$
with parameters estimated by least squares; the t test for $\beta_j$ has $n - p - 1$ degrees of freedom, and the overall F test that all slopes are 0 simultaneously has $(p, n - p - 1)$ degrees of freedom.

$\beta_j$ is a **partial regression coefficient**: the mean change in $y$ for each unit increase in $x_j$ when the other independent variables are held fixed. "Held fixed" is a comparison within the model, not a control in an experiment: the coefficient compares individuals who have the same values of the other variables and differ only in $x_j$. This is the meaning of "adjustment".

### 10.7.2. Smoking and FEV: Confounding

**Example 10.7.1 (Multiple Regression for FEV)** Adding age, height and sex (sex = 1 for male) step by step, the coefficient of smoking (smoke = 1 for current smoker) changes as follows:

| Model | Coefficient of smoking | 95% interval | $p$ | $R^2$ |
|---|---|---|---|---|
| FEV ~ smoking | $+0.711$ L | $(0.495, 0.927)$ | $2 \times 10^{-10}$ | 0.060 |
| FEV ~ age + smoking | $-0.209$ L | $(-0.368, -0.050)$ | 0.010 | 0.577 |
| FEV ~ age + height + sex + smoking | $-0.087$ L | $(-0.204, 0.029)$ | 0.14 | 0.775 |
| ln FEV ~ age + height + sex + smoking | $-0.0461$ | $(-0.0871, -0.0050)$ | 0.028 | 0.811 |

With smoking as the only independent variable, the regression is the two-sample t test (the coefficient 0.711 L is the difference between the two group means, [7.7.7](/7.7.7) Example 7.3.2). After age is added the coefficient changes from positive to negative: among children of the same age, the FEV of smokers is on average 0.21 L lower. Adding height and sex and modeling on the log scale (Example 10.5.1), the final model is

$$
\ln \widehat{\mathrm{FEV}} = -1.944 + 0.0234\,\text{age} + 0.01685\,\text{height (cm)} + 0.0293\,\text{male} - 0.0461\,\text{smoking}.
$$
With the same age, height and sex, the FEV of smokers is on average $\mathrm{e}^{-0.0461} = 0.955$ times that of nonsmokers, that is 4.5% lower (95% interval 0.5%–8.3%). This is an estimate, from the East Boston data, of the damage smoking does to lung function, consistent with the conclusions of many longitudinal studies. Refitting with only the 439 children aged 9 and over (all the smokers fall in this age range) gives a coefficient of $-0.050$ ($p = 0.018$), and the conclusion is unchanged.

What has happened here is confounding: age (and height, which is related to it) both affects FEV and is related to smoking, since it is the older children who smoke. Without adjustment for age the "effect" of smoking contains the effect of age, and even has the opposite direction. This is the same phenomenon as **Simpson's paradox** in [7.7.3](/7.7.3) and [3.3.10](/3.3.10). The general definition of confounding, how to decide which variables to adjust for (for example, height lies partly on the pathway "smoking → growth → FEV", and adjusting for it may remove part of the true effect), and what adjustment can and cannot achieve are discussed in [7.7.13](/7.7.13) and [7.7.15](/7.7.15). Regression adjustment can deal only with measured confounders; in **observational studies** unmeasured confounding (such as family socioeconomic status or parental smoking) may remain.

![Smoking and FEV confounded by age (654 children, Tager et al. 1979; public version Kahn 2005). A: FEV against age (jittered); the 65 smokers, all aged 9 or over, are in orange. The two parallel lines are the model FEV = b0 + b1·age + b2·smoking, and their vertical distance is the effect of smoking after adjustment for age (−0.21 L). B: the coefficient of smoking and its 95% interval as covariates are added: +0.71 L unadjusted, negative after adjustment for age; the last row is the model on the log scale, converted to a relative difference in FEV (−4.5%)](./plots/fev-confounding.py)

### 10.7.3. Dummy Variables

Categorical independent variables are represented by **dummy variables**: a variable with $k$ categories is represented by $k - 1$ variables taking the values 0/1, the uncoded category is the reference group, and each coefficient is the difference between that category and the reference group. In the example above, sex and smoking are both dichotomous variables, and the coefficients are the differences between the two categories after adjustment for the other variables. Race (white, black, other) uses two dummy variables (black = 1, other = 1, white as reference). A regression with only categorical independent variables is analysis of variance: one-way analysis of variance is a regression with $k - 1$ dummy variables, and the F test in the ANOVA table is the test that these $k - 1$ coefficients are all 0 simultaneously ([7.7.12](/7.7.12)).

Do not code a multicategory variable directly as 1, 2, 3 and enter it as a continuous variable: that amounts to assuming the three categories are equally spaced and linear, unless the categories are themselves ordered, equally spaced dose levels (in which case it can serve as a trend test, [7.7.12](/7.7.12), Section 12.4).

### 10.7.4. Interaction Terms

A partial regression coefficient assumes that the effect of $x_j$ is the same at every value of the other variables. If we suspect that the harm of smoking increases with age (that is, with years of smoking), a product term can be added:

$$
\ln \mathrm{FEV} = \beta_0 + \beta_1\,\text{age} + \beta_2\,\text{smoking} + \beta_3\,(\text{age} \times \text{smoking}) + \beta_4\,\text{height} + \beta_5\,\text{male} + \varepsilon,
$$
so that the effect of smoking is $\beta_2 + \beta_3 \times \text{age}$ and varies with age. In the FEV data $\hat\beta_3 = -0.0117$ (each year of age lowers the effect of smoking by a further 1.2% or so), with 95% interval $(-0.028, 0.005)$ and $p = 0.17$: the direction fits "the longer the smoking, the greater the harm", but the data from 65 smokers are insufficient to confirm it. With an interaction term the main term $\beta_2$ means "the effect of smoking at age = 0" and is meaningless to interpret alone; centering age (subtracting the mean) makes the main term "the effect at the mean age". A systematic discussion of interaction (effect modification) is in [7.7.12](/7.7.12), Section 12.5, and [7.7.13](/7.7.13).

## 10.8. Model Selection and Diagnostics

### 10.8.1. Which Variables to Choose

The purpose of the study determines the model:

- To estimate the effect of an exposure (smoking on FEV): decide beforehand, from subject-matter knowledge, which confounders to adjust for (age, height, sex), and write down the model before looking at the data. Do not add or remove covariates according to p-values.
- To predict (building a reference equation for FEV): choose the variables that predict well, and evaluate by cross-validation ([7.7.21](/7.7.21)).

**Stepwise regression** ([3.3.11](/3.3.11)) adds and removes variables automatically according to p-values, and is recommended for neither purpose: when the same data are used both to select variables and to test them, the selected coefficients are too large, the standard errors too small and the p-values too optimistic; the results are very unstable from sample to sample; and it may delete important confounders. The modern alternatives are to fix the model beforehand or to use penalized methods such as the lasso with cross-validation ([7.7.21](/7.7.21)). A rough rule of thumb is to have at least 10–20 observations per parameter to be estimated, otherwise the model will overfit.

### 10.8.2. Collinearity

When the independent variables are highly correlated (**multicollinearity**, [3.3.10](/3.3.10)), their partial regression coefficients are hard to estimate separately, the standard errors become large and the signs of the coefficients may defy common sense, but the overall prediction is not worse. The **variance inflation factor** of $x_j$,

$$
\mathrm{VIF}_j = \frac{1}{1 - R_j^2}
$$
($R_j^2$ is the coefficient of determination of the regression of $x_j$ on the other independent variables), is the factor by which $\operatorname{Var}(b_j)$ is inflated by collinearity. In the FEV model the correlation between age and height is 0.79, and the VIFs are 3.0 and 2.8 for age and height, 1.06 for sex and 1.21 for smoking: collinearity is present but not severe (the usual warning thresholds are 5 or 10). If height were entered in the model in both centimeters and inches, the VIF would be infinite: the two variables are exactly collinear and the model cannot be estimated.

### 10.8.3. A Diagnostic Checklist

After fitting a multiple regression, check in turn: residual plots against the fitted values and against each independent variable (linearity and equal variance), the Q–Q plot, influential points (Cook's distance, DFBETAS) and the VIFs; for the main estimated coefficients, check that the conclusion is robust to removing influential points or changing to a log scale. In panel D of the diagnostic figure above, 34 of the 654 observations have a Cook's distance above the commonly used $4/n$ and 3 have an absolute studentized residual above 3; removing any one of them does not change the conclusion for smoking.

## 10.9. Partial Correlation

An association between two variables may arise from a third variable on which both depend. The **partial correlation coefficient** ([3.3.9](/3.3.9)) is the correlation between two variables after controlling for other variables: regress $x$ and $y$ each on the control variable $z$, and the correlation coefficient of the two sets of residuals is the partial correlation $r_{xy \cdot z}$ of $x$ and $y$ given $z$; its t test is equivalent to the t test for the corresponding coefficient in multiple regression.

**Example 10.9.1** The simple correlation of FEV with age is 0.756, and after controlling for height the partial correlation falls to 0.227 ($p = 4 \times 10^{-9}$): most of the correlation between age and FEV is that "older children are taller", but among children of the same height the older ones still have slightly higher FEV (maturation of the lungs). After controlling for age, height and sex, the partial correlation of smoking with log FEV is $-0.086$ ($p = 0.028$), the same test as that of the coefficient of smoking in Example 10.7.1.

:::

The size of a partial correlation indicates only the strength of linear association and, again, is meaningful only if the model (linearity, correct choice of control variables) holds. For monotone but nonlinear associations use **Spearman's rank correlation coefficient** ([7.7.8](/7.7.8); for FEV and height $r_s = 0.888$, slightly higher than Pearson's 0.868 because the relationship curves upward).

## 10.10. Computing in Python

```python
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor

fev = pd.read_csv("fev.csv")
fev["hcm"] = fev["height"] * 2.54          # inches -> cm
fev["lfev"] = np.log(fev["fev"])

# correlation, its t test and the Fisher z interval (Examples 10.1.1, 10.2.1)
r, p = stats.pearsonr(fev["hcm"], fev["fev"])
z, se = np.arctanh(r), 1 / np.sqrt(len(fev) - 3)
print(r, np.tanh(z - 1.96 * se), np.tanh(z + 1.96 * se))   # 0.868, 0.848, 0.886

# comparing two independent correlations (Example 10.2.3)
z1, z2 = np.arctanh(0.35), np.arctanh(0.06)
Z = (z1 - z2) / np.sqrt(1 / 997 + 1 / 97)
print(Z, 2 * stats.norm.sf(Z))                              # 2.87, 0.004

# simple linear regression, ANOVA table, CI and prediction interval (Examples 10.3.1, 10.4.1, 10.4.2)
m = smf.ols("fev ~ hcm", data=fev).fit()
print(m.params, m.bse, m.rsquared)                          # -5.433, 0.0520; se 0.00116; 0.754
new = pd.DataFrame({"hcm": [140, 160]})
print(m.get_prediction(new).summary_frame(alpha=0.05))      # mean_ci_*: CI of the mean; obs_ci_*: prediction interval

# log scale (Example 10.5.1)
ml = smf.ols("lfev ~ hcm", data=fev).fit()
print(100 * (np.exp(ml.params["hcm"]) - 1))                 # 2.07 % per cm

# multiple regression and confounding (Example 10.7.1)
for f in ["fev ~ smoke", "fev ~ age + smoke", "fev ~ age + hcm + sex + smoke", "lfev ~ age + hcm + sex + smoke"]:
    fit = smf.ols(f, data=fev).fit()
    print(f, fit.params["smoke"], fit.conf_int().loc["smoke"].values, fit.pvalues["smoke"])

# interaction (10.7.4), VIF (10.8.2), influence (10.5.3)
mi = smf.ols("lfev ~ age * smoke + hcm + sex", data=fev).fit()
print(mi.params["age:smoke"], mi.pvalues["age:smoke"])     # -0.0117, 0.17
mf = smf.ols("lfev ~ age + hcm + sex + smoke", data=fev).fit()
X = mf.model.exog
print([variance_inflation_factor(X, j) for j in range(1, X.shape[1])])   # 3.02, 2.83, 1.06, 1.21
cook = mf.get_influence().cooks_distance[0]
print(fev.iloc[np.argmax(cook)])                            # the 8-year-old recorded as 67.5 in

# inverse prediction from a linear standard curve (Example 10.6.1)
dn = pd.read_csv("dnase.csv")
std = dn[(dn.run == 1) & (dn.conc < 1.6)]
lr = stats.linregress(std["conc"], std["density"])
x0 = (0.50 - lr.intercept) / lr.slope                       # 1.21 ng/mL
```

## Summary

- The division of labor between correlation and regression: the correlation coefficient $r$ (Formula 10.1.1) is symmetric and unitless and measures only linear association; regression (Formula 10.3.1) has a direction, its slope has units, and it is used for prediction and adjustment. Draw the scatter plot first: the same $r$ can be a line, a curve, one outlier or one leverage point (Anscombe's quartet).
- Inference for correlation: the t test of $\rho = 0$ (the same as the test of the slope); the interval for $\rho$, the test of $\rho = \rho_0$ and the comparison of two independent correlation coefficients all use the Fisher z-transformation (Definition 10.2.1, Examples 10.2.1–10.2.3). Contrasting two p-values is not a test of the difference.
- Simple regression: $b_1 = r s_y/s_x$; regression toward the mean is a necessary consequence of imperfect correlation; the ANOVA table and $R^2 = r^2$; the confidence interval for the mean and the prediction interval for an individual (Formula 10.4.1) answer different questions, and the latter does not become narrower even in large samples.
- Diagnostics: residual plots check linearity and equal variance, the Q–Q plot checks normality, and the design determines independence; FEV grows in proportion to height, and the log model (+2.1% per centimeter) has better residuals; suspicious influential points are first checked against the original records.
- Standard curves: regress signal on concentration and deduce concentration from signal (inverse prediction, Formula 10.6.1); the interval includes three errors (replicates, position of the standard curve and slope); a high $r^2$ does not mean linearity, so look at the residuals; linearizations such as Lineweaver–Burk distort the errors, and parameters should be estimated by nonlinear regression.
- Multiple regression (Formula 10.7.1): a partial regression coefficient is a comparison "at the same values of the other variables". The FEV thread: the coefficient of smoking goes from the unadjusted $+0.71$ L to $-4.5\%$ after adjustment for age, height and sex (Example 10.7.1), which is confounding; an interaction term lets an effect vary with another variable; dummy variables put categorical variables into regression, with analysis of variance a special case.
- Model selection: when estimating an effect, fix the adjustment variables beforehand and do not use stepwise regression; judge collinearity by the VIF; partial correlation is the correlation after controlling for other variables.

## Questions

1. A study reports a correlation coefficient of 0.85 between the per capita intake of a food and the colon cancer mortality of 20 countries, and concludes that "this food causes colon cancer". Point out at least three problems.

   **Answer** (1) This is an ecological correlation at the country level and cannot be carried over to individuals (the ecological fallacy, [7.7.15](/7.7.15)): that countries with high intake have high mortality does not show that people who eat more have higher mortality. (2) Correlation is not causation: in wealthy countries intake, life expectancy, diagnostic capacity, obesity and physical inactivity are all high together, and any of these could be a common cause. (3) With only 20 points, one or two extreme countries can produce a very high $r$, so one should first look at the scatter plot and at the result without influential points. (4) If 20 foods were tested and only the strongest reported, there is also the problem of multiple comparisons ([7.7.20](/7.7.20)).

2. In the FEV data take only children 150–160 cm tall. How does the correlation between FEV and height change, and why? What about the regression slope?

   **Answer** The correlation coefficient falls greatly (the variance of height in this range is small while the scatter of FEV about the regression line is unchanged; in $r^2 = 1 - s^2/s_y^2$, $s_y^2$ becomes smaller and $s^2$ stays the same). The slope does not change systematically: if the linear relationship holds over the whole range, restricting the range of $x$ merely makes the estimate of the slope less precise ($\operatorname{se}(b_1) = s/\sqrt{\sum(x_i - \bar x)^2}$ becomes larger) without making it biased. This shows that the correlation coefficient depends on the range of $x$ in the sample, so studies with different ranges are not comparable; the slope describes the relationship itself better.

3. A study obtains a sample correlation coefficient $r = 0.964$ between two measures in 14 subjects. Use the Fisher z-transformation to find a 95% confidence interval for $\rho$.

   **Answer** $z = \operatorname{artanh} 0.964 = 2.000$ with standard error $1/\sqrt{14 - 3} = 0.3015$; the interval on the $z$ scale is $2.000 \pm 1.96 \times 0.3015 = (1.409, 2.591)$, and transforming back $\rho \in (\tanh 1.409, \tanh 2.591) = (0.887, 0.989)$. Note that the normal quantile 1.96 is used here, not the $t_{12}$ quantile: the approximate distribution of $z$ is normal, and its variance $1/(n - 3)$ is known and need not be estimated. The interval is very asymmetric about 0.964.

4. In Example 10.4.2 the confidence interval for the mean FEV at a height of 160 cm is about 0.07 L wide and the prediction interval about 1.7 L wide. If the sample size is increased to 6540, about how wide will the two intervals become?

   **Answer** The half-width of the confidence interval for the mean is proportional to $s\sqrt{1/n + (x_0 - \bar x)^2/\sum(x_i - \bar x)^2}$, and both terms shrink as $1/n$, so the width shrinks by a factor of about $\sqrt{10}$, to about 0.022 L. The half-width of the prediction interval is determined mainly by the "1" in $s\sqrt{1 + \cdots}$ and tends to $\pm 1.96 s = \pm 0.84$ L as $n$ grows, so the width stays at about 1.7 L, almost unchanged. The variation between individuals does not decrease because the study is larger.

5. Using the log model of Example 10.5.1, $\ln \mathrm{FEV} = -2.271 + 0.02052 \times \text{height}$, (a) predict the FEV of a child 150 cm tall (in the sense of a geometric mean); (b) what is the ratio of FEV for children 170 cm and 150 cm tall? (c) Why is the back-transformed $\mathrm{e}^{\hat y}$ an estimate of the median rather than the mean?

   **Answer** (a) $\ln \widehat{\mathrm{FEV}} = -2.271 + 0.02052 \times 150 = 0.807$ and $\mathrm{e}^{0.807} = 2.24$ L. (b) $\mathrm{e}^{0.02052 \times 20} = \mathrm{e}^{0.410} = 1.51$: a child 20 cm taller has about 1.5 times the FEV, independent of the starting point, which is what "proportional" means in the log model. (c) If $\ln Y \sim \mathcal{N}(\mu, \sigma^2)$, then $\mathrm{e}^\mu$ is the median (and also the geometric mean) of $Y$, while the mean is $\mathrm{e}^{\mu + \sigma^2/2}$; here $\sigma \approx 0.151$ and the mean is higher by about $\mathrm{e}^{0.0114} - 1 = 1.1\%$, a very small difference, but it cannot be ignored when $\sigma$ is large (as for concentration data).

6. A linear ELISA standard curve $\mathrm{OD} = 0.05 + 0.40 \times$ concentration is fitted from 6 concentrations in duplicate ($n = 12$), with $s = 0.02$, mean standard concentration 1.0, $\sum (x_i - \bar x)^2 = 8.0$ and mean standard OD 0.45. A sample is measured in 2 wells with mean OD 0.85. Find the concentration and its approximate 95% interval; what if only 1 well is measured?

   **Answer** $\hat x_0 = (0.85 - 0.05)/0.40 = 2.00$. The standard error is $\frac{0.02}{0.40}\sqrt{1/2 + 1/12 + (0.85 - 0.45)^2/(0.16 \times 8)} = 0.05\sqrt{0.5 + 0.0833 + 0.125} = 0.05 \times 0.8416 = 0.0421$; with $t_{10, 0.025} = 2.228$ the interval is $2.00 \pm 0.094$, that is $(1.91, 2.09)$. With only 1 well the quantity under the root is $1 + 0.0833 + 0.125 = 1.208$, the standard error is 0.0550 and the interval is $(1.88, 2.12)$. Replicates reduce the first term; when the sample falls in the middle of the standards ($\bar y_0$ close to 0.45) the third term is smallest. Check: $g = 2.228^2 \times 0.02^2/(0.16 \times 8) = 0.0016$, so the approximate formula is usable.

7. In the FEV data the coefficient of smoking for predicting FEV alone is $+0.71$ L, and after adjustment for age it is $-0.21$ L. (a) Sketch what a scatter plot producing such a sign reversal looks like; (b) state the two conditions a confounder must satisfy; (c) if height is adjusted for as well, someone says "height is a result of smoking's effect on growth and should not be adjusted for"; what do you think?

   **Answer** (a) With age on the horizontal axis and FEV on the vertical axis: each group lies along a rising line, the line for smokers slightly below that for nonsmokers, but the smokers are concentrated at the upper right (older ages); viewed pooled, the mean FEV of smokers is higher (panel A of the figure after Example 10.7.1 shows this). (b) The confounder is related to the outcome (age affects FEV, and not only through smoking) and to the exposure (older children are more likely to smoke), and it is not a result of the exposure (age is not affected by smoking). (c) The statement has merit: if smoking slows growth in height, height lies partly on the causal pathway from smoking to FEV (a mediator), and adjusting for it removes the part of the effect of smoking that acts through growth, so that the direct effect "at the same height" is estimated, biased toward 0. In practice the effect of adolescent smoking on height is very small, while the relationship of height to FEV is very strong and largely determined before smoking begins, so height is usually adjusted for; a more rigorous analysis states which effect is being estimated and compares the results with and without adjustment (the causal diagrams of [7.7.15](/7.7.15)).

8. A researcher uses stepwise regression to select 5 "significant" predictors of length of hospital stay for 60 patients from 40 candidate variables, and reports their p-values (all < 0.01) and $R^2 = 0.45$. Evaluate this result.

   **Answer** 60 observations are nowhere near enough for 40 candidate variables (about 10–20 observations are needed per parameter), and in such a situation stepwise regression almost inevitably selects some variables purely by chance. Because the same data are used to select variables and to test them, the reported p-values ignore the selection process and are badly too small; $R^2$ would fall sharply in new data (overfitting). Even if all 40 variables were unrelated to the outcome, stepwise selection could often find a few with "$p < 0.01$". One should limit the variables to a few chosen beforehand from knowledge, or use the lasso with cross-validation and validate in an independent sample ([7.7.21](/7.7.21)), and describe the selection process in the report.

9. A study measured daily salt intake and systolic blood pressure in 30 subjects; the regression slope was 2.1 mmHg/g (95% interval 0.3–3.9) and $R^2 = 0.15$. (a) Does the low $R^2$ show that salt and blood pressure are unrelated? (b) Can one say on this basis that "eating 5 g less salt a day lowers blood pressure by about 10 mmHg"?

   **Answer** (a) No. $R^2 = 0.15$ says that salt intake explains only 15% of the individual variation in blood pressure (which is affected by heredity, age, weight and many other factors), and the interval for the slope excludes 0, showing that an association exists; a low $R^2$ is not inconsistent with a significant slope. (b) No. The slope is a comparison between different individuals in a cross-section: people who eat more salt have blood pressure higher by 2.1 mmHg/g on average, but they may also differ in other respects (weight, diet, age), that is, confounding; the effect of reducing salt intake in the same person must be estimated from an intervention trial. In addition the interval is wide (0.3–3.9 mmHg/g, which for 5 g is 1.5–19.5 mmHg), so even if the effect is causal its size is very uncertain.

10. (Design question) You are to build a normal reference equation for FEV in children aged 8–14, to be used for judging whether a child's lung function is abnormal. Explain how to choose the sample, build the model and express the results.

    **Answer** Sample: draw healthy children without respiratory disease who do not smoke from the target population (by region and school), with a sample large enough to estimate the tails of the distribution in each age and sex group (hundreds to thousands); the exclusion criteria are fixed beforehand; measurements follow a uniform standardized protocol (the same spirometer, trained technicians, the best of repeated measurements). Model: take log FEV as the outcome (Example 10.5.1: proportional relationship, variance increasing with the mean); the independent variables are height (with splines, or the logarithm of height, if nonlinear), age and sex, and their interactions (boys and girls develop at different times); check the residuals for equal variance and normality, and if necessary let the residual standard deviation also be modeled on height (the current GLI equations do this). Presentation: give the predicted mean and the distribution of the residuals, express a child's measured value as a z-score or percentile, and take the 5th percentile ($z = -1.645$) as the "lower limit of normal" instead of a fixed percentage of the predicted value; state the range over which the equation applies and do not extrapolate. Smoking children should not enter the sample used to build the reference equation: they are precisely the ones the equation is meant to detect.
