---
title: Person-Time Data and Survival Analysis
description: Inference for person-time data and incidence rates (one and two samples, rate ratios and their intervals, number of events); censoring in time-to-event data and the noninformative censoring assumption; survival, hazard and cumulative hazard functions, and the exponential, Weibull and Gompertz models; the life-table method, the Kaplan–Meier estimator, Greenwood's formula and median survival time; the log-rank test and the stratified log-rank test; the Cox proportional hazards model, partial likelihood, interpretation of hazard ratios and checking proportional hazards (log-log plots, Schoenfeld residuals, time-varying effects); Weibull regression and accelerated failure time models; competing risks and the cumulative incidence function; sample size based on the number of events. Illustrated by the Veterans Administration lung cancer chemotherapy trial (veteran) and the NLST screening trial.
source_hash: 2c11a7b91b51
---

In the earlier chapters the outcome was measured at a single moment: birth weight, FEV, whether the birth weight was low. Many biomedical questions, however, ask "how long": how long a patient survives after chemotherapy, whether screening postpones death from lung cancer, when the risk of myocardial infarction in former smokers falls to that of nonsmokers. The outcome of **time-to-event data** ([7.7.1](/7.7.1) Section 1.4) is the time until an event occurs. It has two features: times are positive and right-skewed, and they are often subject to **censoring**: a patient still alive when the study ends tells us only that the survival time exceeds some value. This chapter first returns to the **person-time** and **incidence rate** defined in [7.7.3](/7.7.3) and turns them into inference tools for comparing two groups, the coarsest summary of event data. It then takes time itself as the outcome: describing it by the survival function and the hazard function, estimating it from censored data by the life table and the Kaplan–Meier estimator, comparing two survival curves by the log-rank test, and adjusting for several prognostic factors at once by the Cox proportional hazards model. The running example is the last data set of the first thread: the veteran trial, in which 137 patients with advanced lung cancer were randomized to standard or test chemotherapy (its structure was introduced in [7.7.1](/7.7.1) Section 1.4). Exponential and Weibull distributions were fitted to it in [7.7.4](/7.7.4) Section 4.6; here we give an analysis that does not depend on a distributional assumption and answer the question of the trial: does the test chemotherapy prolong survival? The mathematical definitions of survival time, the **survival function**, the **hazard function** and the **proportional hazards model**, together with numerical optimization of the likelihood, are in [3.5.4 Example 4.3.4](/3.5.4#ex-4.3.4); the Gompertz–Makeham law of mortality and the biology of aging are in [7.5.37](/7.5.37); as a randomized trial, veteran reappears in [7.7.18](/7.7.18) for the intention-to-treat analysis and the sample size based on the number of events.

## 16.1. Inference for Person-Time and Incidence Rates

### 16.1.1. Inference for Rates

People followed for different lengths of time cannot be compared directly by "proportion who fall ill": someone followed for 1 year has far less chance of falling ill than someone followed for 10 years. [7.7.3](/7.7.3) Definition 3.2.2 adds up the time each person spends disease-free during observation to obtain the person-time $T$, and the incidence rate is $\hat I = d/T$ ($d$ is the number of events). If events occur randomly at a constant rate $I$ per unit of person-time, the number of events is $d \sim \mathrm{Poi}(IT)$ ([7.7.4](/7.7.4) Example 4.3.1). Intervals and tests for one sample were given in [7.7.5](/7.7.5) Formula 5.7.1 and [7.7.6](/7.7.6) Formula 6.7.1; the comparison of two groups follows.

**Formula 16.1.1 (Comparing Two Incidence Rates)** Let the numbers of events and person-times in the two groups be $d_1, T_1$ and $d_2, T_2$. The **rate ratio** $\mathrm{IRR} = I_1/I_2$ is estimated by $(d_1/T_1)/(d_2/T_2)$.

1. Large-sample interval: $\operatorname{Var}(\ln\widehat{\mathrm{IRR}}) \approx 1/d_1 + 1/d_2$, and the 95% interval is $\exp\bigl(\ln\widehat{\mathrm{IRR}} \pm 1.96\sqrt{1/d_1 + 1/d_2}\bigr)$;
2. Conditional test: given the total number of events $d = d_1 + d_2$, under $H_0\colon I_1 = I_2$ we have $d_1 \sim \mathrm{Bin}\bigl(d, T_1/(T_1 + T_2)\bigr)$, and one can use the exact binomial test ([7.7.6](/7.7.6) Formula 6.6.2) or, when $d$ is large, the normal approximation

$$
z = \frac{d_1 - d\,p_0 - 0.5\,\operatorname{sgn}(d_1 - dp_0)}{\sqrt{d\,p_0(1 - p_0)}}, \qquad p_0 = \frac{T_1}{T_1 + T_2}.
$$

The reasoning behind conditioning is the same as for Fisher's exact test ([7.7.9](/7.7.9) Definition 9.2.1): the total number of events reflects only the common rate and carries no information about the difference between the groups; once it is given, which group an event falls in depends only on the proportion of person-time in the two groups and on the rate ratio. The interval depends only on the numbers of events, not on the numbers of people: 50 cases in 100,000 person-years and 50 cases in 1000 person-years give the same precision for the rate ratio.

**Example 16.1.1 (Lung Cancer Deaths in the NLST)** The low-dose CT group and the chest radiography group each had about 26,700 participants. At a median follow-up of 6.5 years, lung cancer deaths were 356 and 443 in the two groups, at rates of 247 and 309 per 100,000 person-years (Aberle et al. 2011), corresponding to about 144,130 and 143,366 person-years.

$$
\widehat{\mathrm{IRR}} = \frac{247}{309} = 0.799, \qquad \mathrm{SE}(\ln\widehat{\mathrm{IRR}}) = \sqrt{\frac{1}{356} + \frac{1}{443}} = 0.0711,
$$
The 95% interval is $\exp(-0.224 \pm 0.139) = (0.70, 0.92)$, $z = -3.15$, $p = 0.0017$; the conditional binomial test ($p_0 = 0.5013$, 356 of 799 deaths in the CT group) gives $p = 0.0016$. The original report gave a relative reduction of 20.0% (95% interval 6.8%–26.7%); its interval was computed differently from the Wald interval here, but the conclusion is the same: screening lowers lung cancer mortality by about one fifth. All-cause mortality was also reduced, by 6.7% (1.2%–13.6%), showing that the fall in lung cancer deaths was not offset by an increase in deaths from other causes.

### 16.1.2. Stratification, Trend and Models

Comparisons of rates are also subject to confounding: when the age compositions of the two groups differ, the crude rate ratio is meaningless. The remedies parallel those for 2×2 tables, covered in [7.7.13](/7.7.13); only the correspondence is listed here:

| Problem | Proportion (cumulative incidence) | Rate (person-time) |
|---|---|---|
| Comparing two groups | Two-proportion z test, chi-square ([7.7.9](/7.7.9)) | Formula 16.1.1 |
| Stratifying by age, etc. | **Mantel–Haenszel test** and $\mathrm{OR}_{\mathrm{MH}}$ ([7.7.13](/7.7.13) Formula 13.6.1) | $\mathrm{RR}_{\mathrm{MH}}$ and the stratified rate-ratio test (same place) |
| Standardization | Direct and indirect standardization ([7.7.13](/7.7.13) Definition 13.5.2) | Same; SMR ([7.7.6](/7.7.6) Definition 6.7.1) |
| Dose response | **Cochran–Armitage trend test** ([7.7.9](/7.7.9) Definition 9.6.1) | **Poisson regression** with dose as a continuous variable ([7.7.14](/7.7.14) Example 14.8.1) |
| Several covariates | Logistic regression ([7.7.14](/7.7.14)) | Poisson regression with an offset ([7.7.14](/7.7.14) Definition 14.8.1) |

Person-time methods compress each person's follow-up into two numbers: whether the event occurred and how long the person was followed. They implicitly assume that the rate is constant during follow-up (or constant within each stratum of time). When the question is precisely "how does the risk change over time" or "what is the probability of still being alive at a given time", time itself must be taken as the outcome, and this is survival analysis. The two are exactly connected: a Poisson regression that divides the time axis into segments and assumes a constant hazard within each segment gives the same estimates as the piecewise exponential survival model.

## 16.2. Features of Survival Data

### 16.2.1. Events, Origin and Censoring

The outcome of survival analysis is the time $T$ from a well-defined origin (diagnosis, randomization, surgery, birth) to a well-defined event (death, recurrence, discharge, virological failure). The definitions of origin and event determine the question itself: survival "from diagnosis" and "from enrollment" differ by the waiting time between diagnosis and enrollment (the variable `diagtime` in veteran), and mixing them in an observational study produces bias (the immortal time bias in [7.7.15](/7.7.15)).

Censoring has several sources: the study ends on a predetermined date (administrative censoring, figure in [7.7.1](/7.7.1)), patients are lost to follow-up, or patients withdraw for reasons unrelated to the study. All of these are **right censoring**: all we know is $T > C$, where $C$ is the censoring time. Less common are left censoring (we know only that the event had already occurred before some time, such as an infected person who had already seroconverted at the first visit) and interval censoring (we know only that the event occurred between two follow-up visits, such as a tumor recurrence found at a 3-monthly checkup). This chapter treats only right censoring.

**Definition 16.2.1 (Noninformative Censoring)** If, at any time $t$, individuals still under observation (without an event and not yet censored) have the same subsequent event hazard as similar individuals censored at $t$, that is, if the censoring time and the survival time are independent given the covariates, the censoring is called **noninformative censoring**.

All the methods in this chapter rely on this assumption. Administrative censoring (the study simply ends that day) usually satisfies it; censoring that results from withdrawal due to worsening illness, or from ending follow-up because of improvement, does not: in the former case the survivors look healthier than they really are and the survival curve is too high. The assumption cannot be tested with the data; it can only be protected by design (as complete follow-up as possible) and by sensitivity analysis (treat all censored individuals as dying at the time of censoring, or all as surviving to the end of the study, and see whether the conclusions change).

### 16.2.2. Why Censored Individuals Cannot Be Dropped

In the veteran trial, 9 of the 137 patients are censored. Consider three wrong approaches:

- Analyze only the 128 patients who died: the censored are those who lived long (the median censoring time of the 9 is 100 days, whereas the median of the 128 death times is 62 days), so dropping them makes survival times too short; the higher the proportion censored, the larger the bias.
- Treat censoring times as death times: again too short, since the true survival times of the censored are all longer.
- Compare only "the proportion dead at 1 year": those censored before 1 year can be counted neither as dead nor as alive.

A correct estimate lets each person contribute information for as long as he or she is observed: a patient censored at day 100 tells us that he survived days 1, 2, ..., 100. This is exactly the starting point of the life table and the Kaplan–Meier estimator.

## 16.3. Survival and Hazard Functions

### 16.3.1. Definitions and Relations

**Definition 16.3.1 (Survival, Hazard and Cumulative Hazard Functions)** Let the survival time $T$ be a continuous nonnegative random variable with density $f$. The function $S(t) = \mathbb{P}(T > t)$ is called the **survival function**; the function

$$
h(t) = \lim_{\Delta \downarrow 0}\frac{\mathbb{P}(t \le T < t + \Delta \mid T \ge t)}{\Delta} = \frac{f(t)}{S(t)}
$$
is called the **hazard function**, the instantaneous rate per unit time at which events occur given survival to $t$; and $H(t) = \int_0^t h(u)\,\mathrm{d}u$ is called the **cumulative hazard function**.

**Theorem 16.3.1** The three determine one another:

$$
h(t) = -\frac{\mathrm{d}}{\mathrm{d}t}\ln S(t), \qquad S(t) = \exp\bigl(-H(t)\bigr) = \exp\Bigl(-\int_0^t h(u)\,\mathrm{d}u\Bigr).
$$

**Proof** Since $f(t) = -S'(t)$, we have $h(t) = -S'(t)/S(t) = -(\ln S)'(t)$; integrating with $S(0) = 1$ gives the second expression. $\square$

The unit of hazard is "per unit time", the same as the incidence rate: a constant hazard $\lambda$ is a constant incidence rate, which is what person-time methods estimate ($\hat\lambda = d/T$ is the **maximum likelihood estimation** of $\lambda$ under the exponential model, [7.7.4](/7.7.4) Section 4.6). A hazard is not a probability and can exceed 1; but over a short interval $\Delta$, $h(t)\Delta$ approximates the conditional probability of an event in that interval. In describing a population, the hazard function is often more biologically meaningful than the survival function: risk is highest in the early period after surgery and then declines; aging makes the risk of death rise exponentially with age in adulthood.

### 16.3.2. Some Parametric Models

| Model | Hazard $h(t)$ | Survival $S(t)$ | Shape of hazard | Use |
|---|---|---|---|---|
| Exponential | $\lambda$ | $\mathrm{e}^{-\lambda t}$ | Constant | Memoryless failure; the implicit model of person-time methods |
| Weibull | $\dfrac{k}{\eta}\Bigl(\dfrac{t}{\eta}\Bigr)^{k-1}$ | $\exp[-(t/\eta)^k]$ | Decreasing for $k < 1$, increasing for $k > 1$ | Postoperative risk ($k < 1$), tumor progression ($k > 1$) |
| Gompertz | $B\mathrm{e}^{\gamma t}$ | $\exp[-B(\mathrm{e}^{\gamma t} - 1)/\gamma]$ | Exponentially increasing | Change of adult mortality with age |
| Log-normal, log-logistic | Rises then falls | — | Unimodal | Onset after infection, rejection after transplantation |

Adult human mortality roughly doubles every 7–8 years, approximately the Gompertz law; adding an age-independent constant $A$ (accidents, infections) gives the **Gompertz–Makeham law** $h(x) = A + B\mathrm{e}^{\gamma x}$ ([7.5.37](/7.5.37) Definition 37.1.2). Such "age-specific" hazard functions are estimated precisely from life tables (Section 16.4).

![Hazard functions and the survival curves they determine (schematic, time in years). A: constant hazard (exponential distribution), decreasing Weibull hazard (shape parameter 0.6), increasing Weibull hazard (shape parameter 2) and exponentially increasing Gompertz hazard. B: the corresponding survival functions $S(t) = \exp(-H(t))$, all four with a median survival time of 5 years: with different hazard shapes, the survival curves behind the same median can be very different. C: $\ln(-\ln S(t)) = \ln H(t)$ plotted against $\ln t$; for the Weibull model this is a straight line whose slope is the shape parameter, and for the exponential model the slope is 1; this is the principle of the log-log plot used in Section 16.7.3 to check proportional hazards](./plots/hazard-shapes.py)

## 16.4. The Life-Table Method

**Definition 16.4.1 (Life Table)** Divide the follow-up time into intervals $[t_{j-1}, t_j)$. Let $n_j$ be the number still under observation at the start of the $j$th interval, and $d_j$ and $c_j$ the numbers of events and censorings in the interval. Taking $n_j' = n_j - c_j/2$ as the effective number at risk (assuming that censored individuals were observed for half an interval on average), the conditional probability of death in the interval and the estimate of the survival function are

$$
\hat q_j = \frac{d_j}{n_j'}, \qquad \hat S(t_j) = \prod_{i \le j}(1 - \hat q_i).
$$
A table arranged in this way is called a **life table**, and this estimation method is called the life-table method or actuarial method.

The life table originated with Graunt's London bills of mortality and Halley's Breslau life table in the 17th century, and is a basic tool of demography and actuarial science: the "current life tables" published by national statistical agencies apply the age-specific death rates of a given year to a hypothetical birth cohort to obtain the life expectancy at birth. In medicine it is used when follow-up is recorded only by interval (annual visits) or when the sample is very large. The product form is the key: the probability of surviving beyond $t_j$ is the product of the conditional probabilities of surviving each interval in turn; each interval needs only those "alive at entry", and censored individuals contribute until they leave.

**Example 16.4.1 (Life Table for veteran)** With intervals of 100 days (merging intervals with few subjects at the end):

| Interval / days | Entering $n_j$ | Deaths $d_j$ | Censored $c_j$ | Effective $n_j'$ | $\hat q_j$ | $\hat S$ at end of interval |
|---|---|---|---|---|---|---|
| 0–100 | 137 | 79 | 5 | 134.5 | 0.587 | 0.413 |
| 100–200 | 53 | 26 | 3 | 51.5 | 0.505 | 0.204 |
| 200–300 | 24 | 10 | 1 | 23.5 | 0.426 | 0.117 |
| 300–400 | 13 | 7 | 0 | 13.0 | 0.538 | 0.054 |
| 400–600 | 6 | 4 | 0 | 6.0 | 0.667 | 0.018 |
| 600–1000 | 2 | 2 | 0 | 2.0 | 1.000 | 0 |

The life-table estimate of 0.413 at 100 days is close to the Kaplan–Meier estimate of 0.418 in the next section. The conditional probability of death in each interval is between 0.4 and 0.7 without an evident trend: roughly, about half of the patients with advanced lung cancer die in every 100 days, close to a constant hazard.

## 16.5. The Kaplan–Meier Estimator

### 16.5.1. The Product-Limit Estimator

If the life-table intervals are shrunk so that the time axis is split only at the times at which events are observed, we obtain an estimate that does not depend on the choice of intervals.

**Definition 16.5.1 (Kaplan–Meier Estimator)** Let the distinct times at which events are observed be $t_{(1)} < t_{(2)} < \cdots < t_{(k)}$, let $n_j$ be the number still at risk just before $t_{(j)}$ ($T \ge t_{(j)}$ and not censored), and let $d_j$ be the number of events at $t_{(j)}$. The function

$$
\hat S(t) = \prod_{j:\,t_{(j)} \le t}\Bigl(1 - \frac{d_j}{n_j}\Bigr)
$$
is called the **Kaplan–Meier estimator** of the survival function, also known as the product-limit estimator. When an event time and a censoring time coincide, the convention is that the censoring occurs after the event.

$\hat S$ is a step function that drops only at event times; censoring does not make it drop but only reduces the number at risk $n_j$ at the next event time, so that the next drop is larger. Without censoring it is the empirical survival function $1 - \hat F(t)$, "the proportion of people who survive beyond $t$". It is the nonparametric **maximum likelihood estimation** of the survival function (Kaplan and Meier 1958) and is consistent under noninformative censoring. After the last observed time, if the last individual was censored, $\hat S$ stops at a positive value and cannot be extrapolated.

**Formula 16.5.1 (Greenwood's Formula)** The variance of the Kaplan–Meier estimator is

$$
\widehat{\operatorname{Var}}\bigl(\hat S(t)\bigr) = \hat S(t)^2\sum_{j:\,t_{(j)} \le t}\frac{d_j}{n_j(n_j - d_j)}.
$$
It is obtained by the **delta method**: $\ln\hat S(t) = \sum_j \ln(1 - \hat q_j)$, the terms are approximately independent, the binomial variance of $\hat q_j = d_j/n_j$ is $q_j(1 - q_j)/n_j$, and hence $\operatorname{Var}(\ln(1 - \hat q_j)) \approx q_j/[n_j(1 - q_j)]$. An interval constructed directly as $\hat S \pm 1.96\,\mathrm{SE}$ can leave $[0, 1]$, so software often computes the interval on the $\ln(-\ln S)$ scale and transforms it back (the log-log interval), which always stays within $(0, 1)$.

**Definition 16.5.2 (Median Survival Time)** The smallest time at which $\hat S(t) \le 0.5$ is called the estimate of the **median survival time**.

Right-skewed survival times are better summarized by the median than by the mean ([7.7.2](/7.7.2)), the more so as censoring makes the sample mean impossible to compute; only when $\hat S$ falls to 0 is the area under the curve an estimate of the mean (otherwise one can estimate only the "restricted mean survival time" up to some time). The interval for the median consists of the times at which the confidence band of $S(t)$ contains 0.5.

### 16.5.2. Survival Curves for veteran

**Example 16.5.1** In the veteran trial there were 69 patients (64 deaths) in the standard chemotherapy group and 68 (64 deaths) in the test chemotherapy group. The Kaplan–Meier estimates for the two groups:

| | 30 days | 90 days | 180 days | 365 days | Median survival time (95% interval) |
|---|---|---|---|---|---|
| Standard | 0.724 | 0.547 | 0.212 | 0.071 | 103 days (54–126) |
| Test | 0.676 | 0.380 | 0.233 | 0.110 | 52 days (43–90) |

The estimate for the standard group at 90 days is 0.547 with Greenwood standard error 0.060; at 180 days it is 0.212 with standard error 0.051. The median survival time of the test group is only half that of the standard group, but after 180 days the curve of the test group is actually higher than that of the standard group: the test group had more early deaths, and also slightly more long-term survivors (the longest survival time was 999 days in the test group and 553 days in the standard group). The two curves cross at about 150 days, and the ratio of medians and the ratio of 1-year survival give opposite impressions: comparison at a single time point can be chosen arbitrarily, and what should be compared is the whole curve (Section 16.6).

![Kaplan–Meier estimates for the Veterans Administration lung cancer chemotherapy trial (137 patients, 128 deaths; Kalbfleisch and Prentice; veteran data of the R package survival). A: the standard and test chemotherapy groups, with shaded 95% pointwise intervals (Greenwood variance, log-log transformation), vertical ticks for censoring, dots marking the median survival times, and the numbers at risk at each time below; the two curves cross at about 150 days, and the log-rank test gives $\chi^2_1 = 0.008$, $p = 0.93$. B: by histologic type of the tumor: small cell and adenocarcinoma have a median survival time of about 51 days, squamous and large cell carcinoma 118 and 156 days, log-rank test $\chi^2_3 = 25.4$](./plots/km-veteran.py)

Grouping by histologic type (panel B) shows a clear difference: the median survival time is 51 days for both small cell carcinoma (48 patients) and adenocarcinoma (27 patients), 118 days for squamous carcinoma (35 patients) and 156 days for large cell carcinoma (27 patients). Cell type is a strong prognostic factor, and randomization has balanced it roughly between the two groups (the standard group has 15 squamous and 39 small cell or adenocarcinoma patients, and the test group 20 and 36: a chance imbalance, which Section 16.7 will adjust for).

## 16.6. The Log-Rank Test

### 16.6.1. Construction

**Definition 16.6.1 (Log-Rank Test)** At each event time $t_{(j)}$ of the pooled data, let the numbers at risk in the two groups be $n_{1j}, n_{2j}$ ($n_j = n_{1j} + n_{2j}$) and the numbers of events $d_{1j}, d_{2j}$ ($d_j = d_{1j} + d_{2j}$). At each time, arrange "group × event or not" as a 2×2 table; under the null hypothesis that the two groups have the same hazard, given the margins, $d_{1j}$ follows a hypergeometric distribution with

$$
E_{1j} = \frac{d_j n_{1j}}{n_j}, \qquad V_j = \frac{d_j n_{1j} n_{2j}(n_j - d_j)}{n_j^2(n_j - 1)}.
$$
Summing over the times, $O_1 = \sum_j d_{1j}$, $E_1 = \sum_j E_{1j}$, $V = \sum_j V_j$, the statistic

$$
X^2_{\mathrm{LR}} = \frac{(O_1 - E_1)^2}{V} \overset{H_0}{\approx} \chi^2_1
$$
is called the **log-rank test**, also known as the Mantel–Cox test. For $K$ groups, the vector of $(O_k - E_k)$ and its covariance matrix form a quadratic form with $K - 1$ degrees of freedom.

It is precisely the **Mantel–Haenszel test** that treats each event time as a stratum ([7.7.13](/7.7.13) Formula 13.6.1, without continuity correction): at each time, the comparison is of who dies first among "those still alive at this moment", and censored individuals remain in the risk set until they leave. The tables at the different times are not independent (the same person appears in many risk sets), but one can show that the differences $d_{1j} - E_{1j}$ are martingale differences, so that the variance of the sum is the sum of the variances. The name log-rank comes from another derivation by Peto: it is equivalent to a linear rank test with scores of the form $-\ln\hat S$.

The log-rank test has the highest power against proportional hazards alternatives (Section 16.7), where the hazard in one group is a fixed multiple of that in the other at all times. When two curves cross, an early positive difference and a late negative difference cancel, and the test may fail to detect an obvious difference. Versions that put more weight on early events (the Gehan–Wilcoxon test weights by $n_j$, the Peto–Prentice test by $\hat S(t)$) are more sensitive to early differences, but the weights should be chosen before looking at the data.

### 16.6.2. veteran: Do the Two Chemotherapies Differ?

**Example 16.6.1** Pooling the two groups gives 97 distinct death times. Computing time by time, the standard group has observed $O_1 = 64$ deaths with expected $E_1 = 64.50$; the test group has $O_2 = 64$, $E_2 = 63.50$. The variance is $V = 30.41$, and

$$
X^2_{\mathrm{LR}} = \frac{(64 - 64.50)^2}{30.41} = 0.0082, \qquad p = 0.93.
$$
The numbers of deaths in the two groups are almost exactly the numbers expected if the two groups had the same hazard: there is no evidence that the test chemotherapy changes survival. This agrees with the crossing curves in the figure: the test group had more deaths in the first 100 days and fewer afterwards, and overall the two cancel. For a randomized trial this is the main conclusion: in the prespecified intention-to-treat analysis ([7.7.18](/7.7.18)), the test chemotherapy showed no superiority over the standard chemotherapy.

### 16.6.3. The Stratified Log-Rank Test

**Formula 16.6.1 (Stratified Log-Rank Test)** Divide the people into $L$ strata by a prognostic factor, compute $O_{1\ell} - E_{1\ell}$ and $V_\ell$ within each stratum, and then combine:

$$
X^2_{\mathrm{strat}} = \frac{\bigl[\sum_\ell (O_{1\ell} - E_{1\ell})\bigr]^2}{\sum_\ell V_\ell} \overset{H_0}{\approx} \chi^2_1.
$$
It compares the two groups within the same stratum and allows entirely different baseline survival curves in the different strata.

**Example 16.6.2** Stratifying by the 4 cell types, $X^2_{\mathrm{strat}} = 0.70$, $p = 0.40$. Stratification adjusts for the chance imbalance in histologic type, and the conclusion is unchanged.

## 16.7. The Cox Proportional Hazards Model

### 16.7.1. The Model and the Hazard Ratio

The log-rank test can only compare groups; it cannot adjust for several continuous or categorical covariates at once, and it does not give the size of the effect. The model proposed by Cox (1972) writes the effect of covariates as a multiplicative factor on the hazard, while making no assumption about how the hazard changes over time.

**Definition 16.7.1 (Proportional Hazards Model and Hazard Ratio)** Let the covariate vector of an individual be $\boldsymbol{x}$. The **proportional hazards model** assumes

$$
h(t \mid \boldsymbol{x}) = h_0(t)\exp(\boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}),
$$
where the baseline hazard $h_0(t)$ is a nonnegative function of unspecified form. The ratio of the hazards of two individuals with covariates $\boldsymbol{x}_1$ and $\boldsymbol{x}_2$,

$$
\mathrm{HR} = \frac{h(t \mid \boldsymbol{x}_1)}{h(t \mid \boldsymbol{x}_2)} = \exp\bigl((\boldsymbol{x}_1 - \boldsymbol{x}_2)^{\mathsf T}\boldsymbol{\beta}\bigr)
$$
does not change with time and is called the **hazard ratio**. In particular, when $x_k$ increases by one unit with the other covariates fixed, the hazard is multiplied by $\mathrm{e}^{\beta_k}$.

The hazard ratio is the extension of the rate ratio to continuous time: if both groups have constant hazards, it is the IRR of Section 16.1. It also approximates the **relative risk** over short periods, but it does not equal the ratio of the cumulative proportions dead at any fixed time. By Theorem 16.3.1, proportional hazards is equivalent to $S(t \mid \boldsymbol{x}_1) = S(t \mid \boldsymbol{x}_2)^{\mathrm{HR}}$, that is, the curves of $\ln(-\ln S)$ are parallel, differing by $\ln\mathrm{HR}$.

### 16.7.2. Partial Likelihood

**Theorem 16.7.1 (Partial Likelihood)** Assume there are no ties (all event times are distinct). Let the $i$th event occur at $t_{(i)}$ in the individual with covariates $\boldsymbol{x}_{(i)}$, and let $R(t_{(i)})$ be the risk set at that time. Under the proportional hazards model, given that "one event occurs in the risk set at $t_{(i)}$", the conditional probability that it occurs in exactly that individual is

$$
\frac{h_0(t_{(i)})\,\mathrm{e}^{\boldsymbol{x}_{(i)}^{\mathsf T}\boldsymbol{\beta}}}{\sum_{l \in R(t_{(i)})} h_0(t_{(i)})\,\mathrm{e}^{\boldsymbol{x}_l^{\mathsf T}\boldsymbol{\beta}}} = \frac{\mathrm{e}^{\boldsymbol{x}_{(i)}^{\mathsf T}\boldsymbol{\beta}}}{\sum_{l \in R(t_{(i)})} \mathrm{e}^{\boldsymbol{x}_l^{\mathsf T}\boldsymbol{\beta}}},
$$
in which the baseline hazard cancels. The product of these conditional probabilities over the event times,

$$
L_{\mathrm{p}}(\boldsymbol{\beta}) = \prod_{i=1}^{k}\frac{\exp(\boldsymbol{x}_{(i)}^{\mathsf T}\boldsymbol{\beta})}{\sum_{l \in R(t_{(i)})}\exp(\boldsymbol{x}_l^{\mathsf T}\boldsymbol{\beta})}
$$
is called the *partial likelihood* of $\boldsymbol{\beta}$.

Cox (1975) proved that $\hat{\boldsymbol{\beta}}$, the maximizer of $L_{\mathrm{p}}$, is consistent and asymptotically normal, with information matrix given by $-\partial^2\ln L_{\mathrm{p}}/\partial\boldsymbol{\beta}\,\partial\boldsymbol{\beta}^{\mathsf T}$, so one can carry out the **Wald test**, the **likelihood ratio test** and the score test just as with an ordinary likelihood; with a single binary covariate the score test is the log-rank test. The partial likelihood uses only the order of events and the risk sets, not the numerical values of the event times: any monotone transformation of time leaves $\hat{\boldsymbol{\beta}}$ unchanged. Mathematically it is identical to the **conditional logistic regression** of matched studies ([7.7.14](/7.7.14) Definition 14.7.1): each risk set is like a matched set, and the "case" is the person who has the event at that time. With ties (several deaths on the same day), the Breslow or Efron approximation is used; the latter is more accurate and is the default of most software. The solution uses **Newton's method** ([3.5.4](/3.5.4)).

After fitting, the baseline cumulative hazard is estimated by the Breslow estimator $\hat H_0(t) = \sum_{t_{(i)} \le t} d_i/\sum_{l \in R(t_{(i)})}\mathrm{e}^{\boldsymbol{x}_l^{\mathsf T}\hat{\boldsymbol{\beta}}}$, and the survival curve for a given covariate combination is $\exp\bigl(-\hat H_0(t)\,\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\hat{\boldsymbol{\beta}}}\bigr)$.

**Example 16.7.1 (Cox Model for veteran)** With test chemotherapy (0/1), Karnofsky score and cell type (squamous as the reference) as covariates (Efron approximation):

| Covariate | $\hat\beta$ | SE | HR (95% interval) | $p$ |
|---|---|---|---|---|
| Test vs standard chemotherapy | 0.262 | 0.201 | 1.30 (0.88, 1.93) | 0.19 |
| Karnofsky score (per point) | −0.0313 | 0.0052 | 0.969 (0.959, 0.979) | $< 10^{-8}$ |
| Small cell vs squamous | 0.825 | 0.269 | 2.28 (1.35, 3.87) | 0.002 |
| Adenocarcinoma vs squamous | 1.154 | 0.295 | 3.17 (1.78, 5.65) | 0.0001 |
| Large cell vs squamous | 0.395 | 0.282 | 1.48 (0.85, 2.58) | 0.16 |

Compared with the model containing only treatment ($\mathrm{HR} = 1.02$, 0.71–1.45), the adjusted treatment HR moves to 1.30, but its interval still contains 1: for the same cell type and performance status, there is also no evidence that the test chemotherapy is better (the point estimate is even slightly worse). For every 10 points higher on the Karnofsky score (0–100, with 100 a completely normal performance status), the hazard of death is multiplied by $\mathrm{e}^{-0.313} = 0.73$ (0.66–0.81); the hazard for adenocarcinoma is more than 3 times that for squamous carcinoma. Compared with the null model, the likelihood ratio is $\chi^2_5 = 61.1$; the concordance index C is 0.74, that is, for a randomly chosen comparable pair of patients the model has a 74% chance of correctly judging who dies first (synonymous with the AUC of logistic regression, [7.7.14](/7.7.14) Section 14.5.3).

:::

In a randomized trial, adjusting for baseline prognostic factors is not meant to remove confounding (randomization has already done so) but to improve precision and correct chance imbalance; the adjustment variables should nevertheless be prespecified in the analysis plan. Unlike in linear regression, adjusting for a strong prognostic factor unrelated to treatment also moves the treatment HR away from 1 in a Cox model: like the odds ratio, the HR is a noncollapsible measure ([7.7.13](/7.7.13) Section 13.6.3).

### 16.7.3. Checking Proportional Hazards

Proportional hazards is a strong assumption: it requires the effect of the covariates to stay constant over the whole follow-up. Three common checks:

1. The log-log plot: plot $\ln(-\ln\hat S(t))$ against $\ln t$ for groups defined by the covariate; under proportional hazards the curves of the groups are parallel (Section 16.7.1).
2. Schoenfeld residuals (Definition 16.7.2): plot the residuals against time to see whether the coefficient drifts over time;
3. Time-varying coefficients: replace $\beta$ by $\beta(t)$, for example by dividing follow-up into periods and estimating one coefficient in each, or by adding an interaction term $x \cdot g(t)$ and testing whether it is 0.

**Definition 16.7.2 (Schoenfeld Residual)** At the $i$th event time, the difference between the covariate of the individual with the event and the risk-weighted mean of the covariates in the risk set,

$$
\boldsymbol{r}_i = \boldsymbol{x}_{(i)} - \frac{\sum_{l \in R(t_{(i)})}\boldsymbol{x}_l\,\mathrm{e}^{\boldsymbol{x}_l^{\mathsf T}\hat{\boldsymbol{\beta}}}}{\sum_{l \in R(t_{(i)})}\mathrm{e}^{\boldsymbol{x}_l^{\mathsf T}\hat{\boldsymbol{\beta}}}}
$$
is called the **Schoenfeld residual**.

The sum of the Schoenfeld residuals over all events is the score of the partial likelihood, which is zero at $\hat{\boldsymbol{\beta}}$. Grambsch and Therneau (1994) showed that the residuals scaled by the information matrix, $\hat{\boldsymbol{\beta}} + k\,\widehat{\operatorname{Var}}(\hat{\boldsymbol{\beta}})\,\boldsymbol{r}_i$ ($k$ the number of events), have expectation approximately $\boldsymbol{\beta}(t_{(i)})$: plotting them against time and smoothing shows how the coefficient changes over time; testing proportional hazards by their correlation with time (or a transformation of time) is what `cox.zph` in R and `proportional_hazard_test` in lifelines do.

**Example 16.7.2 (The Effect of the Karnofsky Score Weakens over Time)** For the model of Example 16.7.1, a Schoenfeld residual test with time transformed by Kaplan–Meier gives, for the Karnofsky score, $\chi^2_1 = 7.98$, $p = 0.005$; for adenocarcinoma $p = 0.03$, for large cell carcinoma $p = 0.05$, for treatment $p = 1.00$. The residual plot (panel A of the figure below) shows that the Karnofsky coefficient is about −0.05 in the first several tens of days and near 0 after 100 days; in the log-log plot (panel B) the curves of the three score groups converge over time instead of being parallel. Dividing follow-up at day 90 and estimating a separate Karnofsky coefficient in each period (the other covariates unchanged):

| Period | Deaths | HR per 10 points (95% interval) | $p$ |
|---|---|---|---|
| 0–90 days | 73 | 0.63 (0.56, 0.72) | $< 10^{-12}$ |
| After 90 days | 55 | 1.06 (0.87, 1.29) | 0.58 |

Biologically this is natural: performance status at enrollment predicts near-term death, since bedridden patients die within weeks, whereas for patients who survive 3 months the score at enrollment is out of date. The HR of 0.73 in Example 16.7.1 is some kind of average of these two periods; it underestimates the early effect and invents a late effect. The effect of treatment does not violate proportional hazards, but the crossing of the two KM curves (Example 16.5.1) reminds us that an "average HR" is not always a good summary.

![Checking the proportional hazards assumption for the Karnofsky score in the veteran trial (137 patients, 128 deaths). A: scaled Schoenfeld residuals for the Karnofsky score from a Cox model (treatment, Karnofsky score, cell type; Breslow approximation), each point a death, with time in days on a log scale; the orange line is a moving average of 25 neighboring points, and the dashed line is the time-invariant coefficient −0.031. The coefficient is about −0.05 early and tends to 0 after 100 days. B: $\ln(-\ln\hat S(t))$ against $\ln t$ for the Karnofsky score groups 0–49, 50–69 and 70–99; under proportional hazards the three curves should be parallel, but in fact they converge over time](./plots/schoenfeld-karno.py)

:::

When proportional hazards is violated, the options are to stratify by the variable (each stratum has its own baseline hazard, and no coefficient is estimated for it), to include a time-varying coefficient in the model (as above), or to switch to a measure that does not require proportional hazards: the difference in restricted mean survival time, or the accelerated failure time model of Section 16.8.

## 16.8. Parametric Survival Models

### 16.8.1. Accelerated Failure Time Models

The Cox model makes no assumption about the shape of the baseline hazard, at the price that it cannot be extrapolated directly and does not directly say "how much longer people live". A parametric model assumes a distribution family, and the **likelihood function** can handle censoring at the same time: individuals with events contribute the density $f(t_i)$ and censored individuals contribute $S(c_i)$,

$$
L(\boldsymbol{\theta}) = \prod_{i:\,\text{event}} f(t_i \mid \boldsymbol{\theta}) \prod_{i:\,\text{censored}} S(c_i \mid \boldsymbol{\theta}) = \prod_i h(t_i)^{\delta_i}S(t_i),
$$
where $\delta_i$ is the event indicator. For the exponential model it reduces to $\lambda^d\mathrm{e}^{-\lambda T}$, and the maximum likelihood estimate $\hat\lambda = d/T$ is exactly the incidence rate of person-time methods.

**Definition 16.8.1 (Accelerated Failure Time Model)** Let $\ln T = \mu + \boldsymbol{x}^{\mathsf T}\boldsymbol{\gamma} + \sigma W$, where $W$ is an error with a fixed distribution (extreme-value, normal and logistic errors give Weibull, log-normal and log-logistic survival times respectively). Equivalently, $S(t \mid \boldsymbol{x}) = S_0\bigl(t\,\mathrm{e}^{-\boldsymbol{x}^{\mathsf T}\boldsymbol{\gamma}}\bigr)$: the covariates stretch the time scale by a factor of $\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\boldsymbol{\gamma}}$. Such a model is called an **accelerated failure time model**, and $\mathrm{e}^{\gamma_k}$ is called the time ratio.

The interpretation of a time ratio is very direct: $\mathrm{e}^{\gamma} = 1.5$ means that all quantiles (including the median survival time) are extended to 1.5 times.

**Theorem 16.8.1** The Weibull model is both a proportional hazards model and an accelerated failure time model: if $T$ given covariates $\boldsymbol{x}$ follows a Weibull distribution with shape parameter $k$ and scale $\eta_0\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\boldsymbol{\gamma}}$, then $h(t \mid \boldsymbol{x}) = h_0(t)\exp(-k\,\boldsymbol{x}^{\mathsf T}\boldsymbol{\gamma})$, that is, $\boldsymbol{\beta} = -k\boldsymbol{\gamma}$.

**Proof** $H(t \mid \boldsymbol{x}) = (t/\eta_0)^k\mathrm{e}^{-k\boldsymbol{x}^{\mathsf T}\boldsymbol{\gamma}} = H_0(t)\mathrm{e}^{-k\boldsymbol{x}^{\mathsf T}\boldsymbol{\gamma}}$; differentiate with respect to $t$. $\square$

**Example 16.8.1 (Weibull Regression for veteran)** Fitting a Weibull accelerated failure time model with the same covariates as Example 16.7.1: the shape parameter is $\hat k = 1.075$ (0.944–1.224), not significantly different from 1 (the exponential distribution); the coefficient of the Karnofsky score is $\hat\gamma = 0.0291$ (SE 0.0046), so that each 10 points higher extends survival time to $\mathrm{e}^{0.291} = 1.34$ times (1.22–1.46); the time ratios of adenocarcinoma, small cell carcinoma and large cell carcinoma relative to squamous carcinoma are 0.33, 0.45 and 0.68; for the test chemotherapy it is 0.81 ($p = 0.25$). By Theorem 16.8.1 the HR for Karnofsky should be $\exp(-1.075 \times 0.0291) = 0.969$, in exact agreement with the Cox estimate.

A contrast worth noting: without covariates, the Weibull fit of [7.7.4](/7.7.4) Section 4.6 gave $\hat k = 0.85 < 1$, as if the hazard fell over time; after adjusting for Karnofsky score and cell type, $\hat k \approx 1$. A declining population hazard does not mean that every individual's hazard is declining: patients with poor performance status and high-hazard adenocarcinoma die first, and the average hazard of the remaining population naturally falls. Unmeasured individual differences ("frailty") always make the population hazard function flatter than the individual ones, which is also a place for care in interpreting "change of hazard over time".

## 16.9. Competing Risks

**Definition 16.9.1 (Competing Risks and the Cumulative Incidence Function)** If an individual may experience one of several mutually exclusive events (such as death from the cancer under study or death from other causes), and the occurrence of one makes the others no longer possible, these events are called **competing risks**. The cause-specific hazard of event type $k$ is $h_k(t) = \lim_{\Delta \downarrow 0}\mathbb{P}(t \le T < t + \Delta,\ \text{cause} = k \mid T \ge t)/\Delta$; the probability of an event of type $k$ by time $t$,

$$
F_k(t) = \mathbb{P}(T \le t,\ \text{cause} = k) = \int_0^t h_k(u)\,S(u)\,\mathrm{d}u
$$
is called the **cumulative incidence function** of type-$k$ events, where $S(u) = \exp\bigl(-\sum_k\int_0^u h_k\bigr)$ is the overall survival function (no event of any type).

A common error is to treat deaths from other causes as censoring and estimate "the probability of death from cancer" by $1 - \hat S_{\mathrm{KM}}(t)$. A competing event is not noninformative censoring: a person who dies of heart disease will never die of cancer, whereas KM treats him as someone who "might still die of cancer in the future had he not died of heart disease". $1 - \hat S_{\mathrm{KM}}$ estimates a probability in a hypothetical world with no other cause of death, and always overestimates the actual cumulative incidence. The nonparametric estimator of the cumulative incidence function (the Aalen–Johansen estimator) multiplies, at each event time, the overall survival function by the conditional probability of that cause: $\hat F_k(t) = \sum_{t_{(j)} \le t}\hat S(t_{(j-1)})\,d_{kj}/n_j$. The $\hat F_k$ of all causes and the overall survival function always sum to 1.

![Competing risks (simulation, seed 0). 500 patients have two mutually exclusive causes of death with constant cause-specific hazards of 0.10 per year (cause 1, such as death from cancer) and 0.15 per year (cause 2, other causes), plus administrative censoring uniformly distributed between 5 and 15 years. A: three curves for cause 1: $1 - $ the Kaplan–Meier estimate treating deaths from cause 2 as censoring (gray) and the quantity it estimates, $1 - \mathrm{e}^{-0.10t}$ (gray dashed), the Aalen–Johansen estimate of the cumulative incidence function (orange) and the true cumulative incidence function $0.4(1 - \mathrm{e}^{-0.25t})$ (orange dashed); the former treats a probability in a hypothetical world without other causes of death as reality, overestimating by about 0.27 at 10 years. B: the cumulative incidence functions of the two causes stacked with the overall survival probability, summing to 1 at every time](./plots/competing-risks.py)

In the setting of the figure, the true probability of death from cause 1 at 10 years is $\frac{0.10}{0.25}(1 - \mathrm{e}^{-2.5}) = 0.367$, whereas $1 - \mathrm{e}^{-0.10 \times 10} = 0.632$: the difference is greatest in elderly patients and in populations with many other causes of death. There are two kinds of regression models: the cause-specific hazard Cox model (treating other events as censoring, answering "does this factor affect the hazard of this cause", suited to etiologic studies) and the Fine–Gray subdistribution hazard model (modeling the cumulative incidence function directly, suited to prediction and decisions). They answer different questions and can reach conclusions in different directions: a treatment that lowers cardiovascular death may increase the cumulative incidence of cancer because it lets people live longer.

## 16.10. Sample Size for Survival Studies

The statistical information in a survival study comes from events, not from the number of people: a study with 80 deaths among 100 people estimates an HR better than a study with 20 deaths among 10,000 people.

**Formula 16.10.1 (Schoenfeld's Formula)** For two groups randomized 1:1 with proportional hazards, the number of events required for a two-sided level-$\alpha$ log-rank test to detect a hazard ratio $\mathrm{HR}$ with power $1 - \beta$ is

$$
d = \frac{4(z_{\alpha/2} + z_\beta)^2}{(\ln\mathrm{HR})^2};
$$
for an allocation ratio $p : (1 - p)$, replace the 4 in the numerator by $1/[p(1 - p)]$. The number of people needed is $n = d/\mathbb{P}(\text{event})$, the latter determined by the expected baseline survival curve, the accrual period and the follow-up period.

Derivation: the variance of $\ln\widehat{\mathrm{HR}}$ is approximately $1/(d\,p(1-p))$ ($4/d$ for 1:1); substituting into the same argument as [7.7.7](/7.7.7) Formula 7.6.1 gives the result. As in the formula for comparing means, the required number of events is inversely proportional to the square of the log of the effect: for HR = 0.58, 80% power needs 106 events, for 0.75 it needs 380 and for 0.80 it needs 631.

**Example 16.10.1 (Power of veteran)** The veteran trial has 128 deaths. Solving $d = 128$, the hazard ratio detectable with 80% power is $\exp(2 \times 2.802/\sqrt{128}) = 1.64$ (or its reciprocal 0.61). If the true HR of the test chemotherapy is 1.5, the power is only $\Phi\bigl(\sqrt{128}\,\ln 1.5/2 - 1.96\bigr) = 0.63$. So the conclusion of "no difference" can rule out only very large effects: the interval 0.88–1.93 for the adjusted HR in Example 16.7.1 includes clinically important harm as well as a sizable benefit. Designing by the number of events and timing interim analyses by the number of events is the general practice in the design of clinical trials in [7.7.18](/7.7.18).

## 16.11. Computing with Python

```python
import numpy as np
import pandas as pd
from scipy import stats
from lifelines import KaplanMeierFitter, CoxPHFitter, WeibullAFTFitter
from lifelines.statistics import logrank_test, multivariate_logrank_test, proportional_hazard_test

# rate ratio from person-time (Example 16.1.1, NLST)
d1, T1, d2, T2 = 356, 356 / 247e-5, 443, 443 / 309e-5
irr, se = (d1 / T1) / (d2 / T2), np.sqrt(1 / d1 + 1 / d2)
print(irr, np.exp(np.log(irr) + np.array([-1.96, 1.96]) * se))     # 0.80 (0.70, 0.92)
print(stats.binomtest(d1, d1 + d2, T1 / (T1 + T2)).pvalue)          # 0.0016

vet = pd.read_csv("veteran.csv")       # trt 1 standard / 2 test; status 1 = death
vet["test"] = vet.trt - 1
for c in ["smallcell", "adeno", "large"]:                            # squamous is the reference
    vet[c] = (vet.celltype == c).astype(int)

# Kaplan-Meier with log(-log) Greenwood intervals (Example 16.5.1)
for arm, g in vet.groupby("trt"):
    km = KaplanMeierFitter().fit(g.time, g.status)
    print(arm, km.median_survival_time_, km.survival_function_at_times([90, 180, 365]).values)

# log-rank tests (Example 16.6.1) and the 3-df test across cell types
s, t = vet[vet.trt == 1], vet[vet.trt == 2]
print(logrank_test(s.time, t.time, s.status, t.status).test_statistic)         # 0.0082
print(multivariate_logrank_test(vet.time, vet.celltype, vet.status).p_value)   # 1.3e-5

# Cox model, Efron ties (Example 16.7.1) and the Schoenfeld test (Example 16.7.2)
cols = ["time", "status", "test", "karno", "smallcell", "adeno", "large"]
cox = CoxPHFitter().fit(vet[cols], "time", "status")
cox.print_summary()                                   # HR(test) 1.30, HR(karno) 0.969 per point
print(proportional_hazard_test(cox, vet[cols], time_transform="km").summary)   # karno p = 0.005

# Weibull accelerated failure time model (Example 16.8.1)
aft = WeibullAFTFitter().fit(vet[cols], "time", "status")
print(np.exp(aft.params_))                            # time ratios; rho_ is the shape 1.075

# events needed (Formula 16.10.1)
z = stats.norm.ppf
print(4 * (z(0.975) + z(0.80)) ** 2 / np.log(0.75) ** 2)    # 380 events
```

The `CoxPHFitter` of lifelines uses the Efron approximation for ties by default, consistent with R's `survival::coxph`; use `strata=["celltype"]` for a stratified Cox model, and `CoxTimeVaryingFitter` with long-format data in "start–stop" form for time-varying coefficients (the segments of Example 16.7.2). Use `AalenJohansenFitter` for the cumulative incidence function with competing risks.

## Summary

- Person-time data: $\hat I = d/T$; the variance of the log of the rate ratio $\widehat{\mathrm{IRR}}$ of two groups is $1/d_1 + 1/d_2$, and the conditional test is $d_1 \sim \mathrm{Bin}(d, T_1/(T_1 + T_2))$ (Formula 16.1.1); the NLST lung cancer mortality rate ratio is 0.80 (0.70–0.92, Example 16.1.1). Stratification, standardization and trend follow [7.7.13](/7.7.13) and [7.7.14](/7.7.14).
- Survival data: definitions of the origin and the event, right censoring; all methods rely on noninformative censoring (Definition 16.2.1); dropping censored individuals or treating censoring as events both underestimate survival.
- The three functions (Definition 16.3.1, Theorem 16.3.1): $h = f/S = -(\ln S)'$, $S = \mathrm{e}^{-H}$; exponential (constant), Weibull (monotone, shape $k$), Gompertz (exponentially increasing).
- Estimating the survival curve:

  | Method | Formula | Key points |
  |---|---|---|
  | Life table (Definition 16.4.1) | $\hat q_j = d_j/(n_j - c_j/2)$, $\hat S = \prod(1 - \hat q_j)$ | Interval data, large samples; population life tables |
  | Kaplan–Meier estimator (Definition 16.5.1) | $\hat S(t) = \prod_{t_{(j)} \le t}(1 - d_j/n_j)$ | Drops only at event times; nonparametric MLE |
  | Greenwood's formula (Formula 16.5.1) | $\hat S^2\sum d_j/[n_j(n_j - d_j)]$ | log-log interval |
  | Median survival time (Definition 16.5.2) | Smallest $t$ with $\hat S(t) \le 0.5$ | veteran: 103 versus 52 days |

- Comparison: the log-rank test (Definition 16.6.1) is the MH test stratified by event time, based on $\sum(O - E)$; for the two chemotherapies in veteran $\chi^2 = 0.008$, $p = 0.93$ (Example 16.6.1), and stratified by cell type still $p = 0.40$ (Formula 16.6.1). Power is low when the curves cross.
- The Cox model (Definition 16.7.1): $h_0(t)\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}}$, the hazard ratio $\mathrm{e}^\beta$ does not change with time; the partial likelihood (Theorem 16.7.1) eliminates the baseline hazard and has the same form as conditional logistic regression. veteran: HR 0.73 per 10 Karnofsky points, 3.17 for adenocarcinoma versus squamous, 1.30 (0.88–1.93) for treatment.
- Checking proportional hazards: log-log plots, Schoenfeld residuals (Definition 16.7.2), time-varying coefficients; the effect of Karnofsky is only in the first 90 days (HR 0.63 versus 1.06, Example 16.7.2).
- Parametric models: the censored likelihood $\prod h^{\delta}S$; the time ratio of the accelerated failure time model (Definition 16.8.1); Weibull is both, with $\boldsymbol{\beta} = -k\boldsymbol{\gamma}$ (Theorem 16.8.1); unmeasured heterogeneity makes the population hazard appear to fall.
- Competing risks (Definition 16.9.1): use the cumulative incidence function, not $1 - \mathrm{KM}$; at 10 years, 0.37 versus 0.63.
- Sample size depends on the number of events: $d = 4(z_{\alpha/2} + z_\beta)^2/(\ln\mathrm{HR})^2$ (Formula 16.10.1); the 128 deaths in veteran can detect only an HR of 1.64 with 80% power.

## Questions

1. A cohort followed 2000 exposed individuals for 9500 person-years with 38 cases, and 1800 unexposed individuals for 9000 person-years with 18 cases. Find the rate ratio, its 95% interval and the $p$-value of the conditional test (normal approximation).

   **Answer** $\hat I_1 = 38/9500 = 4.0$ and $\hat I_2 = 18/9000 = 2.0$ (per 1000 person-years), $\widehat{\mathrm{IRR}} = 2.00$. $\mathrm{SE}(\ln\widehat{\mathrm{IRR}}) = \sqrt{1/38 + 1/18} = 0.2862$, and the interval is $\exp(0.693 \pm 0.561) = (1.14, 3.50)$. Conditional test: $d = 56$, $p_0 = 9500/18\,500 = 0.5135$, the expected number is $28.76$, the variance is $56 \times 0.5135 \times 0.4865 = 13.99$, $z = (38 - 28.76 - 0.5)/3.740 = 2.34$, and the two-sided $p = 0.019$. The interval depends only on the two numbers of events, 38 and 18.

2. The survival times (months) of 6 patients are 3, 5+, 6, 6, 8+, 12 (+ denotes censoring). Write down the Kaplan–Meier estimate, the Greenwood standard error at 6 months and the median survival time.

   **Answer** At event time 3: $n = 6$, $d = 1$, $\hat S = 5/6 = 0.833$. One patient is censored at 5 months. At time 6: $n = 4$, $d = 2$, $\hat S = 0.833 \times 2/4 = 0.417$. Censoring at 8 months. At time 12: $n = 1$, $d = 1$, $\hat S = 0$. At 6 months $\sum d_j/[n_j(n_j - d_j)] = 1/(6 \times 5) + 2/(4 \times 2) = 0.0333 + 0.25 = 0.2833$, $\mathrm{SE} = 0.417 \times \sqrt{0.2833} = 0.222$. The median survival time is the first time at which $\hat S \le 0.5$, namely 6 months. Note that because of the censoring, the drop at month 6 is by half, not by "2 of 6", a third.

3. Why does the Kaplan–Meier estimator equal the empirical survival function when there is no censoring? When there is censoring at every time, how does it differ from "number surviving beyond $t$ / total number"?

   **Answer** Without censoring, $n_{j+1} = n_j - d_j$, and the product $\prod_j (n_j - d_j)/n_j$ telescopes to $n_{\text{surviving beyond } t}/n$, that is, $1 - \hat F(t)$. With censoring, censored individuals no longer appear in the denominator after they leave the risk set, whereas "number surviving beyond $t$ / total number" treats those censored before $t$ as dead (they are not in the numerator) and so underestimates survival. KM estimates the conditional survival probability at each time using those actually under observation at that time, so the contribution of censored individuals before they leave is retained.

4. Prove that if the ratio of the hazards of two groups is constantly $\theta$, then $\ln(-\ln S_1(t)) - \ln(-\ln S_2(t)) = \ln\theta$; and explain what the convergence of the log-log curves of the Karnofsky groups in veteran means.

   **Answer** $h_1 = \theta h_2$, and integrating gives $H_1(t) = \theta H_2(t)$; since $S = \mathrm{e}^{-H}$, $-\ln S_1 = \theta(-\ln S_2)$, and taking logarithms gives the constant difference $\ln\theta$. Convergence of the curves means that $\ln(H_{\text{low score}}/H_{\text{high score}})$ decreases over time: the ratio of cumulative hazards is falling, that is, the hazard ratio late is closer to 1 than early. This is consistent with the piecewise estimates of Example 16.7.2 (HR 0.63 per 10 points in the first 90 days and 1.06 afterwards).

5. A researcher wants to compare two operations and finds that the 5-year survival of group A is higher than that of group B (60% versus 50%), but the log-rank test gives $p = 0.40$. Another researcher finds that the median survival time of group A is shorter. Is this possible? How should it be reported?

   **Answer** It is possible: when the survival curves cross (group A has more early deaths but also more long-term survivors, as for an operation with high surgical risk but a high rate of cure), the median survival and the 5-year survival point in opposite directions, and the early and late contributions to the log-rank test cancel (Example 16.5.1 is exactly this situation). One should report the complete KM curves with the numbers at risk and state that proportional hazards does not hold; a prespecified comparison at a single time (such as the difference in 5-year survival), the difference in restricted mean survival time or piecewise HRs are more suitable summaries. Choosing after the fact the time point that favors one's own hypothesis exaggerates the difference.

6. In a Cox model, the coefficient of some gene expression (standardized to a z-score) is $\hat\beta = 0.40$ (SE 0.10). Interpret it; what are the HR and 95% interval for a patient with expression 2 standard deviations higher than the average? Does this tell us how many times the probability of death at 1 year is that of an average patient?

   **Answer** For each standard deviation higher expression, the hazard of death at any time is multiplied by $\mathrm{e}^{0.4} = 1.49$ (95% interval $\mathrm{e}^{0.4 \pm 0.196} = 1.23$–$1.82$). For 2 standard deviations higher: $\mathrm{HR} = \mathrm{e}^{0.8} = 2.23$, with interval $\mathrm{e}^{0.8 \pm 0.392} = (1.50, 3.30)$. The HR is not the ratio of 1-year death probabilities: that is $1 - S_0^{2.23}$ versus $1 - S_0$; if the 1-year survival of the average patient is $S_0 = 0.9$, it is $1 - 0.9^{2.23} = 0.209$ versus 0.10, a ratio of 2.09; if $S_0 = 0.3$, it is $0.932$ versus 0.70, a ratio of only 1.33. A probability has the upper limit 1; a hazard ratio does not.

7. Explain why the population hazard function can fall over time while each individual's hazard is constant. Using an example with two kinds of people, compute the population hazard at $t = 0$ and $t = 2$.

   **Answer** Suppose half of the people have a hazard of 1 (per year) and half 0.2, each constant. The population survival is $S(t) = 0.5\mathrm{e}^{-t} + 0.5\mathrm{e}^{-0.2t}$ and the population hazard is $h(t) = -S'/S = (0.5\mathrm{e}^{-t} + 0.1\mathrm{e}^{-0.2t})/S$. At $t = 0$: $h = 0.6$. At $t = 2$: $S = 0.0677 + 0.3352 = 0.4029$, the numerator is $0.0677 + 0.0670 = 0.1347$, and $h = 0.334$. High-hazard people die first, the proportion of low-hazard people among the survivors rises (83% at $t = 2$), and the population hazard falls toward 0.2. This is why the Weibull shape parameter of veteran is 0.85 without covariates and 1.08 after adjustment (Example 16.8.1).

8. A study compares an antihypertensive drug with placebo for "death from cardiovascular disease" in people aged over 70, and estimates the 10-year probability of cardiovascular death as 30% and 36% using $1 - \mathrm{KM}$. Why might these numbers be too high? What method should be used instead?

   **Answer** In the elderly there are many other causes of death, such as cancer and dementia, which are competing risks for cardiovascular death. Treating them as censoring, $1 - \mathrm{KM}$ estimates the hypothetical probability "if there were no other causes of death" and overestimates the actual cumulative incidence (Definition 16.9.1; 0.63 versus 0.37 in the simulation). The cumulative incidence function (Aalen–Johansen) should be used to describe the actual risk; for etiologic questions (does the drug lower the cause-specific hazard of cardiovascular death) use the cause-specific hazard Cox model, and for prediction use the Fine–Gray model; both should be reported, together with all-cause mortality.

9. (Design question) Design a randomized trial comparing two second-line treatments for lung cancer. The median survival in the control group is expected to be 9 months, and you want to detect HR = 0.75 (median extended to 12 months) with two-sided $\alpha = 0.05$ and 90% power. Accrual lasts 24 months with a further 12 months of follow-up. Estimate the number of events and the number of patients needed, and point out the analyses that must be prespecified.

   **Answer** The number of events is $d = 4(1.96 + 1.282)^2/(\ln 0.75)^2 = 4 \times 10.51/0.0828 = 508$. Under the exponential model the control group has $\lambda_0 = \ln 2/9 = 0.077$ and the test group $0.058$ per month; with uniform accrual over 24 months and a minimum follow-up of 12 months, each person's follow-up lies between 12 and 36 months, and the average probability of death is $1 - \frac{1}{24}\int_{12}^{36}\mathrm{e}^{-\lambda u}\,\mathrm{d}u$: for the control group $1 - (\mathrm{e}^{-0.924} - \mathrm{e}^{-2.773})/(24 \times 0.077) = 1 - (0.397 - 0.0625)/1.848 = 0.819$, for the test group $1 - (\mathrm{e}^{-0.693} - \mathrm{e}^{-2.079})/(24 \times 0.0578) = 1 - (0.500 - 0.125)/1.386 = 0.729$, an average of about 0.774, so the number of patients needed is $508/0.774 \approx 656$; allowing for 10% loss to follow-up this rises to about 730. To be prespecified: the primary endpoint (all-cause death, counted from randomization), the intention-to-treat analysis ([7.7.18](/7.7.18)), analyses triggered by the number of events rather than calendar time, stratification factors (performance score, histologic type) and the stratified log-rank test, the timing and boundaries of interim analyses, and a backup analysis (restricted mean survival time) in case proportional hazards fails.

10. Prove that with a single binary covariate and no ties, the score test statistic of the Cox partial likelihood at $\beta = 0$ is the log-rank statistic (ignoring the tie correction in the variance).

    **Answer** $\ln L_{\mathrm{p}} = \sum_i [x_{(i)}\beta - \ln\sum_{l \in R_i}\mathrm{e}^{x_l\beta}]$. The score is $U(\beta) = \sum_i [x_{(i)} - \sum_{R_i} x_l\mathrm{e}^{x_l\beta}/\sum_{R_i}\mathrm{e}^{x_l\beta}]$, which at $\beta = 0$ is $\sum_i [x_{(i)} - n_{1i}/n_i] = O_1 - E_1$ ($x = 1$ denotes group 1, and $n_{1i}/n_i$ is the expectation $E_{1i}$ when there are no ties). The information is $I(0) = \sum_i [n_{1i}/n_i - (n_{1i}/n_i)^2] = \sum_i n_{1i}n_{2i}/n_i^2$, which is exactly $V_i$ for $d_i = 1$. The score statistic is $U(0)^2/I(0) = (O_1 - E_1)^2/V$, the log-rank statistic.
