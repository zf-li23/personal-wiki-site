---
title: "Curve Fitting: Standard Curves, Nonlinear Regression and Dose Response"
description: The three elements of a fit (parameters, their errors, goodness of fit); least squares as maximum likelihood under normal errors; weighted least squares, chi-square fitting and the Q value, replicates and the lack-of-fit test; Deming regression and Bland–Altman agreement analysis when both coordinates have error; Gauss–Newton and Levenberg–Marquardt iteration, starting values, asymptotic intervals, profile intervals and joint confidence regions for nonlinear least squares; the four-parameter logistic standard curve for ELISA, the quantification range and inverse prediction for unknown samples; dose-response curves, EC50 and relative potency, the extra-sum-of-squares F test of parallelism; correlated errors and over-interpretation; the F test and AIC for model comparison. The examples are the DNase ELISA and Puromycin enzyme kinetics.
source_hash: 14d163612015
---

Most quantitative relationships in the laboratory are not straight lines: the optical density of an ELISA saturates in an S shape with concentration, the rate of an enzymatic reaction approaches a limit with substrate concentration according to the Michaelis–Menten equation, and the effect of a drug changes with dose according to the Hill equation. [7.7.10](/7.7.10) showed that forcing such relationships straight (using only a "linear range", or using a Lineweaver–Burk plot) produces systematic bias and distortion of the errors. This chapter explains how to fit mechanistically meaningful nonlinear models directly, and how to answer the three questions of a fit: what are the parameters, how uncertain are they, and does the model agree with the data. The first two sections set up the general framework (least squares and maximum likelihood, weighting and $\chi^2$); Section 11.3 treats the case in which both variables have error (method comparison); Section 11.4 covers the algorithms and intervals of nonlinear least squares; Sections 11.5 and 11.6 are the two commonest applications, standard curves and dose-response curves; and the chapter ends with correlated errors and model comparison. The examples are two laboratory data sets from main thread 4: the ELISA of rat serum DNase (whose duplicate wells were used in [7.7.2](/7.7.2)) and the enzyme kinetics of puromycin-treated and untreated cells (Puromycin). For the principle of ELISA see [7.1.7](/7.1.7); for the Michaelis–Menten equation and the biochemistry of enzyme kinetics see [6.3.17](/6.3.17) and [7.1.9](/7.1.9); for the Hill equation see [7.1.7](/7.1.7); the mathematics of nonlinear regression and iterative algorithms is in [3.3.6](/3.3.6) and [3.5.5](/3.5.5).

## 11.1. The Three Elements of a Fit

Fitting data to a model $y = f(x; \boldsymbol{\theta})$ with adjustable parameters condenses the data into a few meaningful numbers. A complete fitting result has three parts:

1. the parameter estimates $\hat{\boldsymbol{\theta}}$ (such as $V_{\max}$, $K_{\mathrm{M}}$, $\mathrm{EC}_{50}$);
2. the errors of the parameters: standard errors, confidence intervals, and the correlations among the parameters;
3. the goodness of fit: whether the model can describe the data, and whether the residuals are only random error.

A fit that gives parameters without errors and goodness of fit is incomplete: the parameters may be meaningless (the model is wrong) or extremely imprecise (the data are insufficient to determine them).

Why is least squares a reasonable criterion? Suppose the $i$-th observation is $y_i = f(x_i; \boldsymbol{\theta}) + \varepsilon_i$, where the $\varepsilon_i$ are independent $\mathcal{N}(0, \sigma_i^2)$ and the $\sigma_i$ are known.

**Theorem 11.1.1 (Least Squares Is Maximum Likelihood)** Under the model above, the **maximum likelihood estimation** of $\boldsymbol{\theta}$ gives the $\boldsymbol{\theta}$ that minimizes

$$
\chi^2(\boldsymbol{\theta}) = \sum_{i=1}^{N} \left(\frac{y_i - f(x_i; \boldsymbol{\theta})}{\sigma_i}\right)^2.
$$
If all the $\sigma_i$ are equal, this is the ordinary least-squares estimate.

**Proof** The likelihood function is $L(\boldsymbol{\theta}) = \prod_i (2\pi\sigma_i^2)^{-1/2}\exp\{-(y_i - f(x_i; \boldsymbol{\theta}))^2/(2\sigma_i^2)\}$, so $-\ln L = \tfrac12\chi^2(\boldsymbol{\theta}) + \text{constant}$, and maximizing $L$ is equivalent to minimizing $\chi^2$. $\square$

This equivalence shows the conditions under which least squares applies: the errors are independent, normal, and of known or equal variance. When the errors have heavy tails (occasional bubbles, pipetting mistakes), a few large residuals dominate the sum of squares and a robust fit (such as minimizing the absolute residuals, [3.3.12](/3.3.12)) is preferable; when the errors are correlated, the standard errors of least squares can no longer be trusted (Section 11.7). Note that normality of the errors is needed only for inference (intervals and tests); the estimation of the parameters itself does not require it.

## 11.2. Weighted Least Squares and $\chi^2$ Fitting

### 11.2.1. Weighting

When observations differ in precision, the more precise ones should count for more: **weighted least squares** with weights $w_i = 1/\sigma_i^2$ ([3.3.12](/3.3.12)) minimizes the $\chi^2$ of Theorem 11.1.1. The commonest situation in laboratory assays is an error that grows with the signal: the standard deviation of optical density, fluorescence or counts is often roughly proportional to some power of the mean, $\sigma_i \propto \mu_i^{\theta}$ ($\theta = 1$ is a constant coefficient of variation). The 11 runs of the DNase data contain 88 pairs of duplicate wells, and the slope of the log–log regression of the duplicate standard deviation on the mean is about 0.64: the higher the optical density, the greater the absolute error but the smaller the relative error (CV) ([7.7.2](/7.7.2) Example 2.2.2).

When $\sigma_i$ is unknown it can be estimated from replicate measurements, or a variance function can be assumed and estimated iteratively during the fit (iteratively reweighted least squares). Without weighting the parameter estimates remain unbiased and merely less efficient, but the standard errors and prediction intervals are wrong at both the high and low ends of the signal.

### 11.2.2. $\chi^2$ Goodness of Fit and the Q Value

When the $\sigma_i$ are known and the model is correct, the minimum $\chi^2$ has a **chi-square distribution** with $\nu = N - M$ degrees of freedom ($M$ is the number of parameters; exact for linear models and approximate for nonlinear ones).

**Formula 11.2.1 (Goodness of Fit)** The goodness-of-fit probability

$$
Q = \mathbb{P}\left(\chi^2_\nu \ge \chi^2_{\min}\right)
$$
is the probability that "when the model is correct, random error alone gives a fit this bad or worse". A normal fit has $\chi^2_{\min} \approx \nu$ (that is, $\chi^2_{\min}/\nu \approx 1$).

When $Q$ is very small (say $< 0.001$) there are three possibilities: the model is wrong; the $\sigma_i$ have been underestimated (the true errors are larger than claimed); or the errors are not normal (outliers inflate $\chi^2$, which is very common in practice, so a $Q$ slightly below 0.001 is often still acceptable). A $Q$ too close to 1 ($\chi^2_{\min} \ll \nu$) is also suspicious: the $\sigma_i$ have been overestimated, or the data have been "trimmed".

When $\sigma$ is unknown but replicate measurements exist, the residual sum of squares can be divided into two parts: the **pure error sum of squares** between replicate observations at the same $x$, and the **lack-of-fit sum of squares** of the deviation of the model from the mean at each $x$ ([3.3.6](/3.3.6)). The ratio of their mean squares is the $F$ statistic of the lack-of-fit test, which does not require $\sigma$ to be known in advance.

**Example 11.2.1 (Are the Duplicates Giving Too Small an Error?)** The 16 wells of DNase run 1 were fitted with the four-parameter logistic model of Section 11.5; the residual sum of squares is 0.004707 (12 degrees of freedom). The pure-error sum of squares of the duplicate wells at the 8 concentrations is 0.000875 (8 degrees of freedom; the standard deviation of the duplicates is about 0.0105). Treating the duplicate variance as the known $\sigma^2$, $\chi^2_{\min} = 0.004707/0.0001093 = 43.1$, $\nu = 12$ and $Q = 2 \times 10^{-5}$; the lack-of-fit test gives $F = (0.003833/4)/(0.000875/8) = 8.77$ and $p = 0.005$. Does this show that the four-parameter model is wrong? The residual plot shows no systematic pattern, and the same model fits well in all 11 runs. The more reasonable explanation is the second one: the two duplicate wells were loaded from the same dilution, so their difference contains only pipetting and reading error, whereas the residuals of the standard curve also contain the error of preparing the dilution series. Duplicates are **technical replicates** and underestimate the error relevant to the estimation of concentration. This example shows that the conclusions of $Q$ and the lack-of-fit test depend on what "error" means: the estimate of error must come from replication at the same level as the variation of interest ([7.7.12](/7.7.12), Section 12.7).

## 11.3. Error in Both Coordinates: Method Comparison

### 11.3.1. Regression Dilution and Deming Regression

Ordinary least squares assumes that $x$ has no error. If $x$ is itself a measurement with error (two instruments measuring the same samples), ignoring the error in $x$ biases the slope toward 0: if the observed $x = \xi + \delta$ with $\operatorname{Var}(\delta) = \sigma_\delta^2$, the limit of the least-squares slope is $\beta_1 \cdot \operatorname{Var}(\xi)/(\operatorname{Var}(\xi) + \sigma_\delta^2)$. This is called regression dilution, and it is also common in epidemiology: using a single measurement of blood pressure to study the relationship between blood pressure and stroke underestimates the true association ([7.7.17](/7.7.17)).

**Definition 11.3.1 (Deming Regression)** Let $x_i = \xi_i + \delta_i$ and $y_i = \beta_0 + \beta_1\xi_i + \varepsilon_i$, where $\delta_i$ and $\varepsilon_i$ are independent with variances $\sigma_\delta^2$ and $\sigma_\varepsilon^2$, and the ratio $\lambda = \sigma_\varepsilon^2/\sigma_\delta^2$ is known. The estimate that minimizes $\sum[(y_i - \beta_0 - \beta_1\xi_i)^2 + \lambda(x_i - \xi_i)^2]$ is called **Deming regression**, and its slope is

$$
b_1 = \frac{s_{yy} - \lambda s_{xx} + \sqrt{(s_{yy} - \lambda s_{xx})^2 + 4\lambda s_{xy}^2}}{2 s_{xy}},
$$
where $s_{xx}, s_{yy}, s_{xy}$ are the sample variances and covariance and $b_0 = \bar y - b_1\bar x$. For $\lambda = 1$ it is the line that minimizes the perpendicular distances to the line (orthogonal regression).

$\lambda$ is usually obtained from replicate measurements by each of the two methods. Deming regression answers the question "does the new method have a proportional bias (slope $\ne 1$) or a constant bias (intercept $\ne 0$) relative to the reference method?".

### 11.3.2. Agreement: The Bland–Altman Plot

The commonest mistake in comparing two measurement methods is to report their correlation coefficient. Correlation measures whether the two rise and fall together, not whether they give the same numbers: if one method always reads twice the other, $r = 1$; the wider the range of concentrations of the samples, the higher $r$, regardless of how good the methods are. The clinical question is: if the new method replaces the old, how much will individual readings differ?

**Definition 11.3.2 (Bland–Altman Plot)** For each individual compute the difference $d_i = y_i - x_i$ between the two methods and the mean $m_i = (x_i + y_i)/2$; draw a scatter plot with $m_i$ on the horizontal axis and $d_i$ on the vertical axis, and draw the mean difference $\bar d$ (the bias) and $\bar d \pm 1.96 s_d$. This plot is called a **Bland–Altman plot**, and $\bar d \pm 1.96 s_d$ are the 95% **limits of agreement**.

If the differences are approximately normal and do not vary with the mean, about 95% of individuals have a difference between the two methods within the limits of agreement. Whether the limits are acceptable is decided by clinical meaning ("interchangeable if within 10 mmHg") and not by a statistical test. When the differences grow with the mean (proportional error), the plot is made after a log transformation and the limits become ratios. The bias and the limits are themselves subject to sampling error, and their confidence intervals should be reported.

**Example 11.3.1 (Automatic Blood Pressure Monitor)** In [7.7.1](/7.7.1) Example 1.1.1, at site C an automatic blood pressure monitor was compared with manual measurement in 98 people; the mean difference between the two was 14.0 mmHg with standard deviation 11.7. The 95% limits of agreement are $14.0 \pm 1.96 \times 11.7 = (-8.9, 36.9)$ mmHg: the automatic monitor reads 14 mmHg higher on average, and the individual differences range from reading nearly 9 mmHg low to reading 37 mmHg high. Correcting only the mean bias is not enough; the range of individual differences is too wide, and the two methods are not interchangeable.

:::

The figure below is a simulated method comparison: 100 patients are each measured once by the reference method and the new method, the standard deviation of the measurement error is 12 for both, and the new method reads 5 above the truth. The ordinary least-squares slope is 0.90 (diluted by the error of the reference method) and Deming regression ($\lambda = 1$) gives 1.00; the correlation of the two methods is 0.89, whereas the Bland–Altman plot shows a bias of 4.4 and limits of agreement $(-30.2, 38.9)$: the correlation is high yet individual readings can differ by more than 30.

![Comparison of two measurement methods (simulation: 100 patients, true values uniform on 80–200, measurement-error standard deviation 12 for both methods, new method 5 too high). A: new method against reference method, dotted line the identity line; the ordinary least-squares slope 0.90 is diluted by the error of the reference method, and the Deming regression slope is 1.00. B: Bland–Altman plot: the difference against the mean of the two methods, solid line the mean difference (bias 4.4), dashed lines the 95% limits of agreement (−30.2 and 38.9)](./plots/method-comparison.py)

## 11.4. Nonlinear Least Squares

### 11.4.1. Iterative Algorithms

When the model is nonlinear in the parameters (such as $K_{\mathrm{M}}$ in $v = V_{\max}[\ce{S}]/(K_{\mathrm{M}} + [\ce{S}])$), the least squares of **nonlinear regression** ([3.3.6](/3.3.6)) has no explicit solution and must be iterated from starting values. Write the residual $r_i(\boldsymbol{\theta}) = y_i - f(x_i; \boldsymbol{\theta})$ and the Jacobian matrix $J_{ij} = \partial f(x_i; \boldsymbol{\theta})/\partial\theta_j$. Linearizing $f$ about the current value turns the minimization of the residual sum of squares into a linear least-squares problem; this is the **Gauss–Newton method**. It converges quickly near the solution, but far from the solution the linearization is unreliable and it may diverge. The **Levenberg–Marquardt method** ([3.5.5](/3.5.5)) interpolates adaptively between a Gauss–Newton step and a gradient-descent step:

**Algorithm 11.4.1 (Levenberg–Marquardt)** Input: the model $f$, the data, a starting value $\boldsymbol{\theta}_0$ and an initial damping $\lambda = 10^{-3}$.

1. Compute the residuals $\boldsymbol{r}$, the Jacobian $J$ and $S(\boldsymbol{\theta}) = \boldsymbol{r}^{\mathsf T}\boldsymbol{r}$.
2. Solve $(J^{\mathsf T}J + \lambda \operatorname{diag}(J^{\mathsf T}J))\,\boldsymbol{\delta} = J^{\mathsf T}\boldsymbol{r}$.
3. If $S(\boldsymbol{\theta} + \boldsymbol{\delta}) < S(\boldsymbol{\theta})$: accept, $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} + \boldsymbol{\delta}$ and $\lambda \leftarrow \lambda/10$; otherwise reject, $\lambda \leftarrow 10\lambda$, and return to step 2.
4. Repeat steps 1–3 until the relative decrease in $S$ or the step length is smaller than a given tolerance.

When $\lambda$ is very small step 2 is a Gauss–Newton step, and when $\lambda$ is very large it is a small step along the negative gradient. Each iteration costs forming $J$ ($N \times M$) and solving an $M \times M$ linear system, that is $O(NM^2 + M^3)$; after convergence, $(J^{\mathsf T}J)^{-1}s^2$ with $\lambda$ taken as 0 gives the approximate covariance matrix of the parameters.

**Example 11.4.1 (Puromycin)** Treloar (1974) measured the initial rate (radioactive counts, counts/min/min) of an enzymatic reaction in puromycin-treated cells against substrate concentration (ppm), at 6 concentrations in duplicate, 12 reactions in all; the untreated cells have 11 reactions. For the treated group, fit the Michaelis–Menten equation (the **Michaelis–Menten equation**, with the **Michaelis constant** $K_{\mathrm{M}}$):

- From the starting value $(V_{\max}, K_{\mathrm{M}}) = (195.8, 0.0484)$ given by the Lineweaver–Burk line, the residual sums of squares of the Gauss–Newton method are 1207.9, 1195.60, 1195.450, 1195.449, converging in 4 steps.
- From the starting value $(100, 1.0)$ far from the solution, the Gauss–Newton method jumps to negative parameters at the first step and then diverges; the residual sums of squares of the Levenberg–Marquardt method are 110 764, 74 872, 51 939, 2396, 1382, 1201, 1195.5, reaching the same solution at the 8th step.

The converged result is $\hat V_{\max} = 212.7$ (standard error 6.95) and $\hat K_{\mathrm{M}} = 0.0641$ ppm (0.0083), with residual standard deviation $s = 10.9$ (10 degrees of freedom). For the untreated group: $\hat V_{\max} = 160.3$ (6.48), $\hat K_{\mathrm{M}} = 0.0477$ (0.0078), $s = 9.8$.

:::

Choice of starting values: read rough parameter values from the structure of the model, with $V_{\max}$ the largest observed rate and $K_{\mathrm{M}}$ the concentration at which the rate reaches half of it; or use the result of a linearization (Lineweaver–Burk or Hanes plot). Different starting values converging to different solutions, or iterations that do not converge, often indicate that the model is too complex or that the data are insufficient to determine the parameters.

### 11.4.2. Why Linearization Is Bad

![Michaelis–Menten fit of the Puromycin data (Treloar 1974; R datasets::Puromycin): initial rate (counts/min/min) against substrate concentration (ppm) in puromycin-treated and untreated cells. A: nonlinear least-squares fitted curves (solid); the dashed line is the curve corresponding to the Lineweaver–Burk line of the treated group, which underestimates the plateau. B: double-reciprocal plot of the treated group; the vertical bars show the size, after transformation to 1/v, of a rate error of one residual standard deviation (about 11 counts/min/min): very small at high concentrations and very large at the two lowest concentrations, which therefore dominate the fit of the line](./plots/puromycin-mm.py)

The **Lineweaver–Burk plot** ([7.7.10](/7.7.10), Section 10.6) applies ordinary least squares to $1/v$ against $1/[\ce{S}]$, which amounts to assuming a constant error in $1/v$. If the error in $v$ is constant ($\sigma \approx 11$), the error in $1/v$ is about $\sigma/v^2$: at $v = 50$ it is 16 times larger than at $v = 200$, and these least reliable points have the highest leverage because $1/[\ce{S}]$ is largest there. The Lineweaver–Burk line of the treated group gives $V_{\max} = 195.8$ and $K_{\mathrm{M}} = 0.0484$, and with these parameters the residual sum of squares on the original scale is 1920.6, 60% larger than the 1195.4 of the least-squares solution. The Hanes plot ($[\ce{S}]/v$ against $[\ce{S}]$) distorts less (216.2 and 0.0679) but likewise has no correct error model. Linearized plots were necessary in the days before computers; today they are suitable only for displaying data, diagnosing mechanism (such as the type of inhibition) and providing starting values.

### 11.4.3. Intervals for the Parameters

There are two kinds of interval for the parameters of a nonlinear model:

- The asymptotic (Wald) interval $\hat\theta_j \pm t_{N-M,\alpha/2}\operatorname{se}(\hat\theta_j)$, with the standard error from $(J^{\mathsf T}J)^{-1}s^2$. It assumes that the model is approximately linear within the confidence region.
- The profile interval: fix $\theta_j$ at a value, reminimize over the other parameters, and obtain the profile $S_j(\theta_j)$ of the residual sum of squares; all $\theta_j$ satisfying

$$
S_j(\theta_j) \le S(\hat{\boldsymbol{\theta}})\left(1 + \frac{F_{1, N-M, \alpha}}{N - M}\right)
$$
form the interval (the least-squares form of the **profile likelihood**, [3.5.4](/3.5.4)). It does not depend on the linear approximation, can be asymmetric, and is invariant under reparametrization ($K_{\mathrm{M}}$ or $\ln K_{\mathrm{M}}$).

The joint confidence region for two or more parameters is given by $S(\boldsymbol{\theta}) \le S(\hat{\boldsymbol{\theta}})[1 + \frac{p}{N - M}F_{p, N-M, \alpha}]$. When the $\sigma_i$ are known, the equivalent statement is that $\Delta\chi^2 = \chi^2(\boldsymbol{\theta}) - \chi^2_{\min}$ does not exceed a quantile of $\chi^2_p$:

| Confidence level | $p = 1$ | $p = 2$ | $p = 3$ |
|---|---|---|---|
| 68.3% | 1.00 | 2.30 | 3.53 |
| 90% | 2.71 | 4.61 | 6.25 |
| 95% | 3.84 | 5.99 | 7.81 |
| 99% | 6.63 | 9.21 | 11.3 |

$p$ is the number of parameters of simultaneous interest and not the total number of model parameters: when only $K_{\mathrm{M}}$ is of interest the $p = 1$ bound is used, and the other parameters are optimized away in the profile.

**Example 11.4.2** The 95% intervals for the treated group:

| Parameter | Estimate | Wald interval | Profile interval |
|---|---|---|---|
| $V_{\max}$ | 212.7 | $(197.2, 228.2)$ | $(197.4, 229.3)$ |
| $K_{\mathrm{M}}$ | 0.0641 | $(0.0457, 0.0826)$ | $(0.0470, 0.0861)$ |

The two kinds of interval differ little, and the profile interval of $K_{\mathrm{M}}$ is skewed to the right. The correlation of the two estimates is 0.77: when $V_{\max}$ is estimated high, $K_{\mathrm{M}}$ must also be high to fit the data at low concentrations. The joint confidence region is therefore a tilted, slightly curved region (figure below), which the two separate intervals cannot describe. The regions of the treated and untreated groups overlap in the $K_{\mathrm{M}}$ direction and separate in the $V_{\max}$ direction, suggesting that puromycin treatment mainly changes $V_{\max}$ (for the formal comparison see Example 11.6.2).

![The joint 95% confidence region of (V_max, K_M) for the Puromycin data (Treloar 1974; R datasets::Puromycin): the solid curve is given by the residual sum of squares S(V, K) ≤ S_min[1 + p/(n − p)·F(p, n − p; 0.95)] (p = 2) and is somewhat banana-shaped; the dashed curve is the ellipse of the linear (Wald) approximation. The regions of the treated and untreated groups overlap in the K_M direction and do not overlap in the V_max direction](./plots/puromycin-region.py)

## 11.5. Standard Curves: The Four-Parameter Logistic Model

### 11.5.1. The Model

The signal of an immunoassay (ELISA, chemiluminescence, multiplex bead assay) is S-shaped in the analyte concentration: close to the background at low concentrations and saturated at high concentrations, when the antibody or substrate is exhausted. On a logarithmic concentration axis it is roughly symmetric, and the most commonly used model is:

**Definition 11.5.1 (Four-Parameter Logistic Model)** The model

$$
y = d + \frac{a - d}{1 + (x/c)^b}
$$
is called the **four-parameter logistic model**, abbreviated 4PL. Here $a$ is the response as $x \to 0$ (the lower asymptote, the background), $d$ is the response as $x \to \infty$ (the upper asymptote, saturation), $c$ is the concentration at which the response is exactly $(a + d)/2$ (the inflection point on the logarithmic concentration axis), and $b$ is the slope factor (the Hill slope).

The function $y = d + (a - d)/(1 + \mathrm{e}^{b(\ln x - \ln c)})$ of $\ln x$ is symmetric about the inflection point. When the curve is asymmetric on the log axis (the low and high ends curve to different degrees), an asymmetry parameter $g$ is added, $y = d + (a - d)/[1 + (x/c)^b]^g$, called the five-parameter logistic model (5PL), which returns to 4PL when $g = 1$. With the lower asymptote fixed at 0 it is a three-parameter model. The parameter $c$ is estimated on the log scale (the sampling distribution of $\log c$ is closer to normal) and the interval is transformed back.

### 11.5.2. Fitting, Model Selection and Inverse Prediction

**Example 11.5.1 (DNase ELISA)** For run 1, with duplicate wells at each of 8 concentrations (0.049–12.5 ng/mL), the 4PL fit is: lower asymptote $-0.008$ (95% interval $-0.045$ to $0.030$), upper asymptote 2.38 (2.14–2.62), inflection concentration $c = 4.51$ ng/mL (3.61–5.64), slope $b = 0.94$ (0.83–1.05), and residual standard deviation 0.020. The lower asymptote does not differ from 0; for the three-parameter model (lower asymptote 0) the residual sum of squares increases only from 0.004707 to 0.004790, with extra-sum-of-squares $F = 0.21$ and $p = 0.66$; the five-parameter model brings no improvement either ($F = 0.05$, $p = 0.82$). The interval for the upper asymptote is wide because the optical density at the highest concentration (1.72) is still far from the plateau: in these data $c$ and $d$ are estimated mainly by extrapolation.

The concentration is deduced from the mean optical density $\bar y_0$ of the two duplicate wells of an unknown sample by

$$
\hat x_0 = c\left(\frac{a - d}{\bar y_0 - d} - 1\right)^{1/b}.
$$
Its uncertainty comes from the parameters of the standard curve (their covariance matrix) and the measurement error of the sample itself, combined with the **delta method** ([3.1.14](/3.1.14)): $\operatorname{Var}(\hat x_0) \approx \boldsymbol{g}^{\mathsf T}\Sigma\boldsymbol{g} + (\partial\hat x_0/\partial\bar y_0)^2 s^2/m$, where $\boldsymbol{g}$ is the gradient of $\hat x_0$ with respect to the parameters, $\Sigma$ is the covariance matrix of the parameters and $m$ is the number of duplicate wells. The bootstrap can also be used ([7.7.5](/7.7.5)).

| Optical density of the unknown sample | Estimated concentration / (ng/mL) | 95% interval | CV |
|---|---|---|---|
| 0.10 | 0.177 | 0.123–0.254 | 16.6% |
| 0.50 | 1.13 | 1.02–1.24 | 4.4% |
| 1.50 | 8.03 | 7.48–8.62 | 3.2% |

For the sample with optical density 0.50, the line of [7.7.10](/7.7.10) Example 10.6.1 gives 1.21 ng/mL and 4PL gives 1.13 ng/mL: at low concentrations the line has already departed from the curve.

### 11.5.3. The Quantification Range

The precision of an estimated concentration varies with concentration: in the middle of the curve the slope is steep and a small error in signal causes only a small error in concentration; at the ends the curve is flat and the same signal error corresponds to a wide range of concentration. Plotting the CV of the back-calculated concentration against concentration gives the precision profile of the assay.

**Definition 11.5.2 (Precision Profile and Quantification Range)** The curve of the coefficient of variation of the back-calculated concentration as a function of concentration is called the **precision profile** of the assay. On the precision profile, the interval of concentrations for which the CV of the back-calculated concentration does not exceed a specified value (immunoassays often use 20%) and which lies within the range of the standards is called the quantification range of the assay; its lower end is the **lower limit of quantification** (LLOQ) and its upper end the upper limit of quantification.

The difference between the **limit of quantification** ([6.4.1](/6.4.1)) and the **limit of detection**: the limit of detection is the lowest concentration distinguishable from the blank ("is it there?"), usually back-calculated from the mean blank signal plus 3 standard deviations; the lower limit of quantification is the lowest concentration at which a numerical value can be given with acceptable precision ("how much?"), and is always higher than the limit of detection. The precision profile of DNase run 1 (panel B below) crosses 20% at about 0.145 ng/mL, and the quantification range is about 0.15–12.5 ng/mL; concentrations above the highest standard are extrapolations and are not reported even if the CV is still small: the sample should be diluted and measured again. These data have no blank wells, so the limit of detection cannot be estimated by definition; if the residual standard deviation of the fit is used in place of the standard deviation of the blank, "lower asymptote + 3s" corresponds to about 0.09 ng/mL, which can serve only as a rough reference.

![The four-parameter logistic standard curve of DNase ELISA run 1 (Davidian and Giltinan 1995; R datasets::DNase). A: the fitted curve and its 95% confidence band on the log concentration axis; the back-calculated concentrations and 95% intervals (delta method) of three unknown samples with optical densities 0.10, 0.50 and 1.50 (means of two duplicate wells). B: the precision profile: the coefficient of variation of the back-calculated concentration against concentration; above 20% (dotted line) the assay can no longer quantify. C: the fitted curves of all 11 independent runs (run 1 highlighted); the inflection concentrations lie between 3.7 and 5.0 ng/mL: a standard curve belongs to its own plate and run](./plots/dnase-4pl.py)

A few points of practice: every plate has its own standard curve (panel C above: the standard deviation of the inflection concentration across the 11 runs is 0.44 ng/mL, a coefficient of variation of about 11%; the differences among runs are a **batch effect**, which [7.7.17](/7.7.17) uses to illustrate variance components); standards and samples are diluted in the same matrix; duplicate wells serve to detect pipetting mistakes and not to estimate the between-assay error (Example 11.2.1); when the error grows with the signal, weighting can be used (Section 11.2), but in the DNase example weighting changes the estimates of the upper asymptote and the inflection concentration a great deal (the inflection point changes from 4.5 to 5.6 ng/mL), whereas the back-calculated concentration within the quantification range hardly changes (0.50 corresponds to 1.13 and 1.11 ng/mL): extrapolated parameters are unstable and interpolated results are robust.

## 11.6. Dose-Response Curves and $\mathrm{EC}_{50}$

### 11.6.1. The Hill Equation and $\mathrm{EC}_{50}$

The dose-response curves of pharmacology and toxicology are the same model as standard curves: the **Hill equation** ([7.1.7](/7.1.7)) $E = E_0 + (E_{\max} - E_0)\,x^n/(\mathrm{EC}_{50}^n + x^n)$ is 4PL, $n$ is the Hill slope (the counterpart of the **Hill coefficient** in receptor binding) and $\mathrm{EC}_{50}$ is the $c$ of 4PL. The fitting of $\mathrm{EC}_{50}$ and $\mathrm{LC}_{50}$ from malformation and mortality rates in developmental toxicology ([7.5.38](/7.5.38)) uses the methods of this section; when the response is dichotomous (dead or alive), fitting according to the binomial distribution is more appropriate (the logit and probit models of [7.7.14](/7.7.14)).

**Definition 11.6.1 (Half-Maximal Effective Concentration)** On a dose-response curve, the concentration that produces an effect halfway between the maximum effect and baseline is called the **half-maximal effective concentration**, denoted $\mathrm{EC}_{50}$; the concentration at which an inhibitor produces half of the inhibition is denoted $\mathrm{IC}_{50}$.

$\mathrm{EC}_{50}$ is defined relative to the fitted upper and lower asymptotes. If the curve does not reach a plateau (the effect is still rising at the highest dose), both $E_{\max}$ and $\mathrm{EC}_{50}$ rest on extrapolation and the interval will be very wide; $\mathrm{EC}_{50}$ should then not be reported, or the asymptotes should be fixed by the controls (0%, 100%) before fitting, with that stated. The doses should be roughly equally spaced on the log scale and cover the whole range from no effect to maximum effect, with the doses in the middle the most informative.

### 11.6.2. Comparing Two Curves: Relative Potency

When comparing the potency of a test preparation with that of a reference (a bioassay), if the two have the same active ingredient and differ only in concentration, the test preparation is equivalent to a dilution or concentration of the reference, and the two curves should be parallel on the log dose axis: the same shape, merely displaced left or right.

**Definition 11.6.2 (Relative Potency)** If the dose-response curves of the test preparation and the reference are parallel on the log dose axis, that is $f_{\text{test}}(x) = f_{\text{reference}}(\rho x)$, then $\rho$ is called the **relative potency** of the test preparation with respect to the reference. In 4PL it equals the ratio of the $\mathrm{EC}_{50}$ values: $\rho = c_{\text{reference}}/c_{\text{test}}$.

Whether the two curves are parallel is tested by comparing nested models: in the full model each curve has 4 parameters (8 in all), while in the constrained model the two share the upper and lower asymptotes and the slope and differ only in $c$ (5 in all).

**Formula 11.6.1 (Extra-Sum-of-Squares F Test)** Let the residual sums of squares of the reduced model ($M_0$ parameters) and the full model ($M_1$ parameters) be $S_0 \ge S_1$, and let there be $N$ observations. Then

$$
F = \frac{(S_0 - S_1)/(M_1 - M_0)}{S_1/(N - M_1)}
$$
is approximately $F_{M_1 - M_0,\, N - M_1}$ when the reduced model holds. This is the extension to nonlinear models of the **extra sum of squares** and the **general linear test** in linear models ([3.3.9](/3.3.9), [3.3.4](/3.3.4)).

When parallelism is rejected, the relative potency has no single value (it varies with the response level), which shows that the two preparations act differently, and a "potency ratio" should not be reported.

**Example 11.6.1 (A Simulated Bioassay)** The reference and the test preparation are each measured 3 times at each of 8 equally spaced log doses (the response is a percentage of the control, residual standard deviation 5); the true ratio of the $\mathrm{EC}_{50}$ values is 2.5 and the slopes are the same. The residual sums of squares of the parallel model and of the separate fits are 1432.7 and 1343.8, $F = 0.88$ (3 and 40 degrees of freedom), $p = 0.46$, so parallelism holds; the $\mathrm{EC}_{50}$ of the test preparation is 2.49 times that of the reference (95% interval 1.99–3.10), that is, the potency of the test preparation is $1/2.49 = 0.40$ of the reference. For another test preparation with half the slope, the parallelism test gives $F = 9.2$, $p = 9 \times 10^{-5}$: the curves cross and cannot be described by a single potency ratio.

![Relative potency of two dose-response curves (simulated data: the test preparation and the reference each at 8 doses, 3 replicates per dose, residual standard deviation 5). A: parallel 4PL curves sharing the upper and lower asymptotes and the slope; the horizontal distance between the two curves on the log dose axis is the logarithm of the relative potency (ratio of EC50 2.49). B: separate fits for a test preparation with a flatter slope and the reference: the curves are not parallel, and the extra-sum-of-squares F test of parallelism rejects (p < 0.001)](./plots/relative-potency.py)

**Example 11.6.2 (What Did Puromycin Change?)** Put the 23 reactions of the treated and untreated groups in one model: the full model has $V_{\max}$ and $K_{\mathrm{M}}$ for each group (4 parameters), with residual sum of squares 2055.1; the model with a shared $K_{\mathrm{M}}$ (3 parameters) has 2240.9; the model in which the two groups are identical (2 parameters) has 7276.5.

- Shared $K_{\mathrm{M}}$ against the full model: $F = (2240.9 - 2055.1)/(2055.1/19) = 1.72$ with $(1, 19)$ degrees of freedom, $p = 0.21$; there is no evidence that $K_{\mathrm{M}}$ differs.
- Identical groups against shared $K_{\mathrm{M}}$: $F = (7276.5 - 2240.9)/(2240.9/20) = 44.9$ with $(1, 20)$ degrees of freedom, $p = 1.6 \times 10^{-6}$; $V_{\max}$ differs.

The model with a shared $K_{\mathrm{M}}$ gives $K_{\mathrm{M}} = 0.058$ ppm (standard error 0.006), $V_{\max} = 208.6$ for the treated group, and 42.0 lower for the untreated group (standard error 6.3). Conclusion: puromycin treatment raised the maximal rate, and no effect on $K_{\mathrm{M}}$ could be detected. Note that this is the conclusion of a comparison of two models; "the difference in $K_{\mathrm{M}}$ is not significant" does not prove that $K_{\mathrm{M}}$ is the same, and the interval for the difference in $K_{\mathrm{M}}$ is still rather wide.

## 11.7. Correlated Errors and Over-Interpretation

The standard errors of least squares assume that the residuals are mutually independent. Time series, spatial data, repeated measurements on the same individual and derived quantities computed from the same set of raw data all violate this assumption. The most typical laboratory example is the mean squared displacement (MSD) in single-particle tracking, see [7.6.23](/7.6.23): the MSD of a trajectory at time lags $\tau$ and $\tau + 1$ is computed from almost the same displacements, so the MSD at adjacent lags are highly correlated. When a straight line is fitted to the MSD curve of one trajectory, the residuals deviate smoothly to one side, and the ordinary least-squares standard error severely underestimates the true uncertainty.

**Example 11.7.1 (Simulated Brownian Motion)** Simulate 200 two-dimensional Brownian trajectories (diffusion coefficient $D = 1$, 1000 steps each), compute the time-averaged MSD of each trajectory at lags 1–100, and fit $\mathrm{MSD} = 4D\tau$. The mean of the 200 values of $\hat D$ is 1.01 and their standard deviation is 0.219, whereas the median of the ordinary least-squares standard errors reported by the individual fits is only 0.0044, 50 times too small. If one compared the $D$ of two trajectories on this basis, almost any difference would be "significant". The correct approach: fit only the first few lags (the information lies mainly at short lags), estimate the error from the variation between independent trajectories or independent trajectory segments, or use estimators that take the correlation structure into account (generalized least squares, likelihood methods).

![Correlated residuals make ordinary standard errors too small (simulation): 200 two-dimensional Brownian trajectories (D = 1, 1000 steps). For each trajectory the time-averaged mean squared displacement (MSD) is computed at lags 1–100 and fitted by least squares with MSD = 4D·lag. A: MSD curves of 20 trajectories: adjacent lags share almost the same displacements, and each curve deviates smoothly from the true value (dashed). B: histogram of the 200 estimates of D (standard deviation 0.219), far wider than the range claimed by the ordinary least-squares standard error of a single fit (horizontal bar: mean ± 1.96 times the median standard error 0.0044)](./plots/msd-correlated.py)

:::

Another kind of over-interpretation is to treat a descriptive fit as a mechanism. [7.6.23](/7.6.23) discussed that a power-law exponent fitted to the overall MSD over one or two orders of magnitude (an "anomalous diffusion exponent of 0.7") is only a description: fractional Brownian motion, continuous-time random walks and diffusion among obstacles can all give the same exponent. A good fit shows only that the model can describe the data, not that it is the only model that can. Distinguishing mechanisms requires data for which the models make different predictions (the time-averaged MSD of single trajectories, the distribution of displacements, the velocity autocorrelation, perturbation experiments). Likewise, a good 4PL fit does not show that binding follows a cooperative mechanism, and a Hill slope $b = 0.94$ is not the number of binding sites.

## 11.8. Model Comparison

### 11.8.1. Nested Models

When one model is a special case of another (some parameters fixed: 3PL is 4PL with $a = 0$, and a shared $K_{\mathrm{M}}$ is the full model with $K_{\mathrm{M},1} = K_{\mathrm{M},2}$), use the extra-sum-of-squares F test of Formula 11.6.1 or, equivalently, the **likelihood ratio test**. When the parameter being tested lies on the boundary of the parameter space (such as a variance component equal to 0 or a mixing proportion equal to 0), the null distribution of the test statistic is no longer the usual $F$ or $\chi^2$ and needs correction.

### 11.8.2. Information Criteria

Models that are not nested (Michaelis–Menten against a substrate-inhibition model, 4PL against a Weibull-type curve) are compared by the **Akaike information criterion** ([3.4.11](/3.4.11)). In a least-squares fit with normal errors,

$$
\mathrm{AIC} = N\ln(S/N) + 2(M + 1),
$$
where $S$ is the residual sum of squares and the $M + 1$ counts the error variance. For small samples use the corrected $\mathrm{AIC_c} = \mathrm{AIC} + 2K(K + 1)/(N - K - 1)$ ($K = M + 1$). The smaller the AIC the better; models differing by less than 2 need not be distinguished.

**Example 11.8.1** DNase run 1 ($N = 16$):

| Model | Parameters | Residual sum of squares | AIC | $\mathrm{AIC_c}$ |
|---|---|---|---|---|
| 3PL (lower asymptote 0) | 3 | 0.004790 | $-121.8$ | $-118.2$ |
| 4PL | 4 | 0.004707 | $-120.1$ | $-114.1$ |
| 5PL | 5 | 0.004684 | $-118.2$ | $-108.8$ |

The three models fit almost equally well, and $\mathrm{AIC_c}$ prefers the simplest, 3PL. For the three models for the two Puromycin groups (Example 11.6.2): the full model 113.33, shared $K_{\mathrm{M}}$ 113.32, identical groups 138.41, in agreement with the conclusions of the F tests.

:::

The principles of model selection are the same as in [7.7.10](/7.7.10), Section 10.8: prefer mechanistic models; keep the number of parameters small relative to the data; report the selection process; and do not try dozens of curves on the same data and report the best. More flexible nonparametric curves (splines, Gaussian process regression) are suitable for describing shape but do not give biologically meaningful parameters.

## 11.9. Computing in Python

```python
import numpy as np
import pandas as pd
from scipy import optimize, stats

# Michaelis-Menten by nonlinear least squares (Examples 11.4.1, 11.4.2)
pu = pd.read_csv("puromycin.csv")
tr = pu[pu.state == "treated"]
S, v = tr["conc"].to_numpy(), tr["rate"].to_numpy()

def mm(S, V, K):
    return V * S / (K + S)

lb = stats.linregress(1 / S, 1 / v)                      # Lineweaver-Burk, for starting values only
p0 = [1 / lb.intercept, lb.slope / lb.intercept]         # (195.8, 0.0484)
p, cov = optimize.curve_fit(mm, S, v, p0=p0)             # Levenberg-Marquardt by default
se = np.sqrt(np.diag(cov))
print(p, se)                                             # (212.7, 0.0641), se (6.95, 0.0083)

# profile interval for K_M
n, rss = len(v), ((v - mm(S, *p)) ** 2).sum()
thr = rss * (1 + stats.f.ppf(0.95, 1, n - 2) / (n - 2))
Ks = np.linspace(0.02, 0.15, 2001)
prof = [((v - mm(S, (v * S / (k + S)).sum() / ((S / (k + S)) ** 2).sum(), k)) ** 2).sum() for k in Ks]
print(Ks[np.array(prof) <= thr][[0, -1]])                # (0.047, 0.086)

# treated vs untreated: shared K_M? (Example 11.6.2)
X = (pu["conc"].to_numpy(), (pu["state"] == "untreated").to_numpy(float))
y = pu["rate"].to_numpy()
full = lambda X, V, dV, K, dK: (V + dV * X[1]) * X[0] / (K + dK * X[1] + X[0])
shared = lambda X, V, dV, K: (V + dV * X[1]) * X[0] / (K + X[0])
pf, _ = optimize.curve_fit(full, X, y, p0=[210, -50, 0.06, 0])
ps, _ = optimize.curve_fit(shared, X, y, p0=[210, -50, 0.06])
S1, S0 = ((y - full(X, *pf)) ** 2).sum(), ((y - shared(X, *ps)) ** 2).sum()
F = (S0 - S1) / (S1 / (len(y) - 4))
print(F, stats.f.sf(F, 1, len(y) - 4))                   # 1.72, 0.21

# four-parameter logistic standard curve and inverse prediction (Example 11.5.1)
dn = pd.read_csv("dnase.csv")
r1 = dn[dn.run == 1]
x, yod = r1["conc"].to_numpy(), r1["density"].to_numpy()

def fourpl(x, a, d, logc, b):                            # a: bottom, d: top, logc: log10 of c
    return d + (a - d) / (1 + 10 ** (b * (np.log10(x) - logc)))

q, qcov = optimize.curve_fit(fourpl, x, yod, p0=[0, 2, 0.6, 1])
print(q, 10 ** q[2])                                     # c = 4.51 ng/mL

def inverse(y0, a, d, logc, b):
    return 10 ** logc * ((a - d) / (y0 - d) - 1) ** (1 / b)

print(inverse(0.50, *q))                                 # 1.13 ng/mL
```

R's `nls` and `drc` and Python's `lmfit` and `statsmodels` (generalized least squares, weighted least squares) provide fuller output (profile intervals, parallelism tests, weighting); whatever software is used, look at the fitted curve and the residual plot and do not merely read the parameter table.

## Summary

- A fitting result = parameters + errors of the parameters + goodness of fit (Section 11.1); under normal, independent errors of known variance, least squares is maximum likelihood (Theorem 11.1.1), and weighted least squares uses $w_i = 1/\sigma_i^2$.
- Goodness of fit: $\chi^2_{\min} \approx \nu$; a very small $Q$ (Formula 11.2.1) indicates a wrong model, underestimated errors or non-normality. The estimate of error must come from replication at the right level: the DNase duplicates are technical replicates and underestimate the error of the standard curve (Example 11.2.1).
- Method comparison: when $x$ has error the least-squares slope is diluted, and Deming regression (Definition 11.3.1) is used; agreement is judged by the Bland–Altman plot and the limits of agreement (Definition 11.3.2), not by the correlation coefficient (automatic blood pressure monitor: bias 14 mmHg, limits −9 to 37 mmHg, Example 11.3.1).
- Nonlinear least squares: Gauss–Newton is fast near the solution, and Levenberg–Marquardt (Algorithm 11.4.1) is stable from far away; starting values come from the structure of the model or from linearization. Puromycin: $V_{\max} = 212.7 \pm 7.0$, $K_{\mathrm{M}} = 0.064 \pm 0.008$ (Example 11.4.1); Lineweaver–Burk underestimates both and leaves a residual sum of squares 60% larger.
- Parameter intervals: Wald intervals depend on the linear approximation, whereas profile intervals and joint confidence regions are given by contours of the residual sum of squares (the $\Delta\chi^2$ table); when the parameters are correlated, look at the joint region (Example 11.4.2).
- Standard curves: 4PL (Definition 11.5.1); the interval of an inverse prediction combines the errors of the curve and the sample by the delta method; the precision profile gives the quantification range and the lower limit of quantification (Definition 11.5.2; DNase about 0.15–12.5 ng/mL); no extrapolation, one curve per plate.
- Dose response: the Hill equation is 4PL, and $\mathrm{EC}_{50}$ requires the curve to reach a plateau (Definition 11.6.1); relative potency (Definition 11.6.2) is meaningful only for parallel curves, and parallelism and nested models are tested by the extra-sum-of-squares F test (Formula 11.6.1); puromycin changes $V_{\max}$ ($p = 1.6 \times 10^{-6}$), and no change in $K_{\mathrm{M}}$ was detected (Example 11.6.2).
- Correlated errors make ordinary standard errors too small (the MSD fit underestimates by 50 times, Example 11.7.1); a good descriptive fit is not a mechanism. Model comparison: F tests for nested models, AIC for non-nested ones (Example 11.8.1).

## Questions

1. A fit has $\chi^2_{\min} = 52$ with $\nu = 20$ degrees of freedom. (a) Find the approximate order of magnitude of $Q$; (b) list three possible causes and explain how to check each.

   **Answer** (a) $\chi^2_{20}$ has mean 20 and standard deviation $\sqrt{40} = 6.3$, so 52 is about 5 standard deviations above the mean; an exact calculation gives $Q = \mathbb{P}(\chi^2_{20} \ge 52) \approx 1.2 \times 10^{-4}$. (b) Wrong model: look at the plot of the residuals against $x$ for systematic curvature or trend, and try a more reasonable model. Underestimated errors: check the source of the $\sigma_i$, whether they came from technical replicates (such as duplicate wells from the same dilution) and whether between-run and between-day errors were omitted; re-estimate from independent replicates. Non-normal errors or outliers: look at the Q–Q plot of the residuals and see whether one or two residuals contribute most of the $\chi^2$; check those points and, if necessary, compare with a robust fit.

2. Use Theorem 11.1.1 to explain what fit corresponds to maximum likelihood if the error of $y$ is multiplicative ($y = f(x;\boldsymbol{\theta})\,\mathrm{e}^{\varepsilon}$, $\varepsilon \sim \mathcal{N}(0, \sigma^2)$). What is the relationship with "weighting by $1/\mu^2$"?

   **Answer** Taking logarithms, $\ln y = \ln f(x;\boldsymbol{\theta}) + \varepsilon$, the errors on the log scale are independent, normal and of equal variance, so maximum likelihood is ordinary least squares on the log scale: minimize $\sum(\ln y_i - \ln f(x_i;\boldsymbol{\theta}))^2$. When $\sigma$ is small, $\ln y - \ln f \approx (y - f)/f$, which approximates least squares on the original scale with weights $w_i = 1/f(x_i;\boldsymbol{\theta})^2$, that is, an error model with constant coefficient of variation. The two approaches give almost the same estimates when $\sigma$ is small; when $\sigma$ is large or the data contain values near 0, the model on the log scale is more natural.

3. Two glucometers are compared in 50 patients; Pearson's correlation coefficient is 0.98 and the paired t test gives $p = 0.40$. The investigators conclude: "the two instruments agree highly and are interchangeable." Point out two errors in this argument and explain how the analysis should be done.

   **Answer** (1) A high correlation coefficient shows only that the two rise and fall together, not that the readings are the same; the wider the range of the patients' glucose, the higher $r$. (2) A nonsignificant paired t test shows only that the mean difference is not significantly different from 0, not that individual differences are small; when individual differences are large with random direction, the mean difference can be close to 0. One should draw a Bland–Altman plot and give the bias and the 95% limits of agreement (with their confidence intervals), judging interchangeability from the clinically acceptable difference (such as within ±15%); check whether the differences vary with the mean (use the log scale for proportional error); and Deming regression can be used to estimate proportional and constant bias.

4. In Example 11.4.1, suppose a student obtains from the Lineweaver–Burk plot $V_{\max} = 195.8$ and $K_{\mathrm{M}} = 0.0484$ for the treated group and concludes that "the $K_{\mathrm{M}}$ of the puromycin-treated group is 57% larger than that of the untreated group (0.0308 by Lineweaver–Burk)". Is this conclusion reliable?

   **Answer** No. The Lineweaver–Burk estimates are dominated by the two points at the lowest concentration, and $K_{\mathrm{M}}$ is underestimated in both groups (the nonlinear fits give 0.0641 and 0.0477), the extent of the underestimation depends on the random errors at those two points, and the ratio of the two groups is meaningless. The correct comparison is Example 11.6.2: within one nonlinear model, test whether $K_{\mathrm{M}}$ is the same, $F = 1.72$, $p = 0.21$; the data are insufficient to show that $K_{\mathrm{M}}$ differs, whereas the difference in $V_{\max}$ is highly significant. Comparing parameters from linearized estimates mistakes a bias caused by the method for a biological difference.

5. Using the profile intervals of Example 11.4.2 and the $\Delta\chi^2$ bounds in the table, explain why, to report a "95% joint confidence region" for $V_{\max}$ and $K_{\mathrm{M}}$, one cannot simply give the rectangle formed by the two 95% intervals.

   **Answer** Each of the two separate 95% intervals covers the true value with probability 95%, and the probability that the rectangle they form covers both simultaneously is generally not 95% (about $0.95^2 = 90\%$ if the parameters were independent, and more generally determined by the correlation structure). More important, the correlation coefficient of the estimates of $V_{\max}$ and $K_{\mathrm{M}}$ is 0.77, so the joint confidence region is tilted along the diagonal: the upper left and lower right corners of the rectangle ($V_{\max}$ low with $K_{\mathrm{M}}$ high, or the reverse) are in fact incompatible with the data, while the parts of the joint region that extend along the diagonal beyond the rectangle are compatible. The joint region should be given by the contour $S(\boldsymbol{\theta}) \le S_{\min}[1 + \frac{2}{N-2}F_{2,N-2,0.05}]$ (or $\Delta\chi^2 \le 5.99$).

6. The 4PL standard curve of an ELISA has $a = 0.05$, $d = 2.5$, $c = 10$ ng/mL and $b = 1.2$. (a) What is the concentration of a sample with optical density 1.00? (b) How should a sample with optical density 2.45 be handled?

   **Answer** (a) $\hat x_0 = c[(a - d)/(\bar y_0 - d) - 1]^{1/b} = 10 \times [(0.05 - 2.5)/(1.00 - 2.5) - 1]^{1/1.2} = 10 \times (1.6333 - 1)^{0.8333} = 10 \times 0.6333^{0.8333} = 10 \times 0.683 = 6.83$ ng/mL. (b) 2.45 is only 0.05 below the upper asymptote 2.5, and back-calculation gives $10 \times [(-2.45)/(-0.05) - 1]^{0.8333} = 10 \times 48^{0.8333} = 10 \times 25.2 = 252$ ng/mL; but here the curve is extremely flat, an error of 0.02 in optical density changes the estimate by more than a factor of two, and the value is very likely above the highest standard (extrapolation). This value should not be reported: dilute the sample (say 1:20) and measure again so that the signal falls in the middle of the quantification range, then multiply by the dilution factor.

7. In Example 11.6.1 the parallelism test gave $p = 0.46$, and the investigators wrote "the two curves have been shown to be parallel". What is wrong with this sentence? In bioassay guidelines parallelism is often judged by "equivalence"; what does this mean?

   **Answer** Failing to reject the null hypothesis is not proof of the null hypothesis: with few data and large errors the test may be nonsignificant even when the curves are clearly not parallel; conversely, with a lot of data, trivial differences of no biological importance will be "significant". It is more reasonable to specify beforehand the acceptable differences (such as a ratio of slopes between 0.8 and 1.25 and differences of asymptotes within a few percentage points), estimate confidence intervals for these differences, and judge the curves parallel only if the intervals lie entirely within the acceptable range: this is the idea of an equivalence test (two one-sided tests, [7.7.18](/7.7.18)).

8. In the full Puromycin model (each group with its own $V_{\max}$ and $K_{\mathrm{M}}$) one could also fit the two groups separately and do a $z$ test with the two estimates of $V_{\max}$ and their standard errors: $(212.7 - 160.3)/\sqrt{6.95^2 + 6.48^2}$. Compute it and explain how it differs from the F test of Example 11.6.2 in the question it answers.

   **Answer** $z = 52.4/\sqrt{48.3 + 42.0} = 52.4/9.50 = 5.51$, $p \approx 4 \times 10^{-8}$ (with the t distribution and about 19 degrees of freedom, $p$ is about $3 \times 10^{-5}$). It compares $V_{\max}$ on the premise that the $K_{\mathrm{M}}$ of the two groups may differ, using each group's own error estimate. The second F test of Example 11.6.2 compares $V_{\max}$ within the model with a shared $K_{\mathrm{M}}$: the first F test is used to confirm that a shared $K_{\mathrm{M}}$ is compatible with the data, and the test is then done in the simpler model, with fewer parameters and more precise estimates (the standard error of the difference in $V_{\max}$ falls from 9.5 to 6.3); it also assumes that the two groups have equal error variance (pooled residual sum of squares). The two conclusions agree. Because the estimates of $V_{\max}$ and $K_{\mathrm{M}}$ are correlated, whether "$K_{\mathrm{M}}$ is shared" affects the difference in $V_{\max}$: 52.4 when fitted separately and 42.0 when shared.

9. (Design question) You are to determine the $\mathrm{IC}_{50}$ of a new drug by a cell viability assay and compare it with a known drug. Design the doses, replicates and analysis.

   **Answer** Doses: first run a wide-range pilot experiment (say 1 nM–100 µM in 10-fold steps) to find the approximate $\mathrm{IC}_{50}$; the main experiment uses 8–10 doses equally spaced on the log scale (3-fold or half-log steps), covering the plateaus from no inhibition to complete inhibition, with a no-drug control (0% inhibition) and a complete-kill control (100% inhibition) used for normalization or for fixing the asymptotes. Replicates: 3 replicate wells at each dose within the plate (technical replicates, to detect pipetting errors), and the whole experiment repeated independently at least 3 times on different days with different passages of cells (biological replicates); the two drugs are on the same plate and plate positions are randomized to avoid edge effects. Analysis: fit 4PL to each experiment separately (fixing the upper and lower asymptotes if necessary), and check the residuals and whether the curves reach the plateaus; in each experiment test the parallelism of the curves of the two drugs and, if they are parallel, estimate the relative potency and its interval; pool $\log\mathrm{IC}_{50}$ with the independent experiment as the unit (mean and 95% interval, or a mixed model with experiment as a random effect, [7.7.17](/7.7.17)), and do not pool all wells into a single fit, which treats technical replicates as independent observations and gives intervals that are too narrow (Example 11.2.1 and pseudoreplication in [7.7.12](/7.7.12)).

10. Explain why, in Example 11.7.1, the estimates of $D$ still differ greatly between trajectories even though the $R^2$ of the MSD fit of every trajectory exceeds 0.99. What does this imply for a report that "the diffusion coefficient of a protein fell from 0.95 to 0.85 µm²/s after mutation ($p < 0.001$, based on the standard errors of single-trajectory fits)"?

    **Answer** The MSD grows monotonically with lag, and any smoothly curved function can be described by a straight line with a very high $R^2$; $R^2$ measures how much of the variation of the MSD curve across lags the line explains, whereas the uncertainty of $D$ comes from the whole curve being randomly high or low together, which cannot be seen within one trajectory because all the lags share the same displacements. The standard error of a single-trajectory fit treats 100 highly correlated points as independent and underestimates by about 50 times. Implication: to compare diffusion coefficients under two conditions, the trajectory (better, the independent cell and independent experiment) should be the unit of analysis, and the variation among the $\hat D$ of many trajectories should be used for a two-sample comparison (comparing $\log D$ if the distribution of $D$ is skewed, or using a rank test); report the number of trajectories and cells in each condition; with a standard deviation of about 20% for $\hat D$ from a single trajectory, a difference between 0.95 and 0.85 needs quite a large number of trajectories to detect.
