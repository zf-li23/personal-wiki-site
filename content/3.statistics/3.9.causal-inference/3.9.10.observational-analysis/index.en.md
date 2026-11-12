---
title: "Analyzing Observational Studies: Blocking, Weighting, and Matching Estimators"
description: The analysis phase of an observational study under a regular assignment mechanism. The lottery data; the bias of the difference in means under a linear outcome model and its reduction by blocking; blocking combined with regression within blocks, for the average effect and the effect on the treated, and its variance; blocking as weighting with a coarsened propensity score; the minimum wage data and matching estimators without and with replacement, with multiple matches, their bias and bias-corrected matching; the common linear structure of all estimators and the conditional variance; the complete design-and-analysis workflow.
---

After the design phase of [3.9.9](/3.9.9) we have a sample, possibly trimmed, in which the treated and control units are arranged in blocks with similar propensity scores or in matched sets with similar covariates. The analysis phase now uses the outcomes to estimate the average causal effect. All estimators of this chapter rest on unconfoundedness, the assumption of a **regular assignment mechanism** ([3.9.8](/3.9.8)), and they differ in how they remove the remaining differences in the covariates. The message of the chapter is that design and analysis complement each other: blocking or matching removes most of the imbalance, so that a regression adjustment within blocks or matched pairs only has to correct small differences and no longer depends much on its functional form. We first study blocking estimators on the lottery data (§10.1–10.2), connect blocking to weighting (§10.3), study matching estimators on the minimum wage data (§10.4), and close with the variance of all these estimators (§10.5) and the full workflow (§10.6).

As in [3.9.8](/3.9.8), the units are a random sample from a super-population, $\mu_w(x) = \mathbb{E}[Y_i(w) \mid X_i = x]$ and $\sigma_w^2(x) = \operatorname{Var}(Y_i(w) \mid X_i = x)$ denote the conditional means and variances of the potential outcomes, and under unconfoundedness $\mu_w(x) = \mathbb{E}[Y_i^{\mathrm{obs}} \mid W_i = w, X_i = x]$.

## 10.1. The Lottery Data

**Example 10.1.1 (Lottery Winners and Labor Supply)** Imbens, Rubin and Sacerdote (2001) studied the effect of unearned income on economic behavior, including labor supply, consumption and savings. They surveyed people who had played the Massachusetts lottery. The treated units are the "winners", who had won large sums of money paid out in yearly installments; the controls are the "losers", who had also played but won only small prizes. The outcome considered here is the average annual labor earnings in the six years after winning, in thousands of dollars, and the covariates include the number of tickets bought, education, whether the person was working at the time of winning, and earnings in the years before winning.

Winning is random among those who play, but the analysis sample is not a randomized experiment: survey response differed between winners and losers, and the two groups differ in covariates such as the number of tickets bought, which is related both to the chance of winning and to income. Under unconfoundedness given the covariates, the analysis follows the design of [3.9.9](/3.9.9). The propensity score is estimated by logistic regression with the three-step selection of [3.9.8](/3.9.8), and the sample of 496 units is trimmed to the units with $0.0891 \le \hat e(X_i) \le 0.9109$:

| | $\hat e(X_i) < 0.0891$ | $0.0891 \le \hat e(X_i) \le 0.9109$ | $\hat e(X_i) > 0.9109$ | All |
|---|---|---|---|---|
| Losers | 82 | 172 | 5 | 259 |
| Winners | 4 | 151 | 82 | 237 |
| All | 86 | 323 | 87 | 496 |

The trimming threshold $0.0891$ is the one given by the variance-minimizing rule of [3.9.9](/3.9.9). The remaining 323 units are divided into five blocks of 80, 40, 41, 81 and 81 units by the recursive splitting of Algorithm 9.4.1.

:::

## 10.2. Blocking Estimators

### 10.2.1. The Bias of the Difference in Means

To see what blocking achieves, assume for the moment a linear model for the conditional means of the potential outcomes, with a constant average effect,

$$
\mu_w(x) = \mathbb{E}\bigl[Y_i(w) \mid X_i = x\bigr] = \alpha + \tau_{\mathrm{sp}}w + x\boldsymbol{\beta}, \qquad w = 0, 1.
$$

**Theorem 10.2.1 (Bias of the Difference in Means)** Under unconfoundedness and the linear model, the difference-in-means estimator $\hat\tau^{\mathrm{dif}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$ has conditional bias

$$
\mathbb{E}\bigl[\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr] = (\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta},
$$
where $\bar X_{\mathrm{t}}$ and $\bar X_{\mathrm{c}}$ are the covariate means of the treated and control units.

**Proof** Write

$$
\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} = \left(\frac{1}{N_{\mathrm{t}}}\sum_{i=1}^{N}W_iY_i(1) - \frac{1}{N}\sum_{i=1}^{N}Y_i(1)\right) - \left(\frac{1}{N_{\mathrm{c}}}\sum_{i=1}^{N}(1 - W_i)Y_i(0) - \frac{1}{N}\sum_{i=1}^{N}Y_i(0)\right).
$$
The units are independent, so the conditional expectation of $Y_i(w)$ given $(\boldsymbol{X}, \boldsymbol{W})$ depends only on $(X_i, W_i)$, and by unconfoundedness $\mathbb{E}[Y_i(w) \mid X_i, W_i] = \mathbb{E}[Y_i(w) \mid X_i] = \mu_w(X_i)$. For the first bracket, a treated unit contributes $(\frac{1}{N_{\mathrm{t}}} - \frac{1}{N})\mu_1(X_i) = \frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}\mu_1(X_i)$ and a control unit contributes $-\frac{1}{N}\mu_1(X_i)$, so its conditional expectation is

$$
\frac{N_{\mathrm{c}}}{N}\left(\frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\mu_1(X_i) - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\mu_1(X_i)\right) = \frac{N_{\mathrm{c}}}{N}\Bigl[(\alpha + \tau_{\mathrm{sp}} + \bar X_{\mathrm{t}}\boldsymbol{\beta}) - (\alpha + \tau_{\mathrm{sp}} + \bar X_{\mathrm{c}}\boldsymbol{\beta})\Bigr] = \frac{N_{\mathrm{c}}}{N}(\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta}.
$$
In the same way, the second bracket has conditional expectation $\frac{N_{\mathrm{t}}}{N}(\bar X_{\mathrm{c}} - \bar X_{\mathrm{t}})\boldsymbol{\beta}$. Subtracting,

$$
\mathbb{E}\bigl[\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr] = \frac{N_{\mathrm{c}}}{N}(\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta} - \frac{N_{\mathrm{t}}}{N}(\bar X_{\mathrm{c}} - \bar X_{\mathrm{t}})\boldsymbol{\beta} = (\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta}. \qquad \square
$$

The bias is the product of the covariate imbalance and the effect of the covariates on the outcome, the same structure as the **omitted variable bias** of regression ([3.3.10](/3.3.10)). In a completely randomized experiment $\mathbb{E}[\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}}] = 0$ and the bias averages out; in an observational study it can be large. The estimator ignores the block structure built in the design, and pays for it.

### 10.2.2. Blocking

The basic blocking (subclassification) estimator analyzes each block as a completely randomized experiment and averages the block estimates with the block proportions $q(j) = N(j)/N$ as weights, exactly as the stratified estimator of [3.9.7](/3.9.7):

$$
\hat\tau^{\mathrm{strat}} = \sum_{j=1}^{J}q(j)\,\hat\tau^{\mathrm{dif}}(j), \qquad \hat\tau^{\mathrm{dif}}(j) = \bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - \bar Y_{\mathrm{c}}^{\mathrm{obs}}(j).
$$
Applying Theorem 10.2.1 within each block gives:

**Corollary 10.2.1 (Bias of the Blocking Estimator)** Under the assumptions of Theorem 10.2.1,

$$
\mathbb{E}\bigl[\hat\tau^{\mathrm{dif}}(j) - \tau_{\mathrm{fs}}(j) \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr] = \bigl(\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j)\bigr)\boldsymbol{\beta}, \qquad \mathbb{E}\bigl[\hat\tau^{\mathrm{strat}} - \tau_{\mathrm{fs}} \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr] = \left(\sum_{j=1}^{J}q(j)\bigl(\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j)\bigr)\right)\boldsymbol{\beta},
$$
where $\tau_{\mathrm{fs}}(j)$ is the average effect in block $j$, and $\tau_{\mathrm{fs}} = \sum_j q(j)\tau_{\mathrm{fs}}(j)$.

Because the blocks were constructed to balance the covariates, the within-block differences $\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j)$ are much smaller than the overall difference, and so is the bias. The bias does not vanish: blocks have finite width, and within a block the treated units still tend to have somewhat higher propensity scores and hence somewhat different covariates.

### 10.2.3. Blocking and Regression

The remaining within-block imbalance is small, so a regression within each block can remove it without relying much on the linear form. In block $j$ fit the local linear model

$$
Y_i^{\mathrm{obs}} = \alpha(j) + \tau(j)W_i + X_i\boldsymbol{\beta}(j) + \varepsilon_i
$$
by least squares on the units of the block,

$$
\bigl(\hat\alpha(j), \hat\tau^{\mathrm{adj}}(j), \hat{\boldsymbol{\beta}}(j)\bigr) = \arg\min_{\alpha, \tau, \boldsymbol{\beta}}\sum_{i=1}^{N}B_i(j)\bigl(Y_i^{\mathrm{obs}} - \alpha - \tau W_i - X_i\boldsymbol{\beta}\bigr)^2,
$$
and combine the block estimates:

$$
\hat\tau^{\mathrm{strat,adj}} = \sum_{j=1}^{J}q(j)\,\hat\tau^{\mathrm{adj}}(j), \qquad \hat\tau_{\mathrm{t}}^{\mathrm{strat,adj}} = \sum_{j=1}^{J}\frac{N_{\mathrm{t}}(j)}{N_{\mathrm{t}}}\,\hat\tau^{\mathrm{adj}}(j).
$$
The second version, with the proportion of treated units in each block as weight, estimates a different estimand, the **average treatment effect on the treated**. If the linear model holds within each block, the regression removes the bias $(\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j))\boldsymbol{\beta}$ entirely; if it holds only approximately, the error is a misspecification error times a small imbalance, a second-order quantity. This is why regression, unreliable on the raw sample of an observational study ([3.9.8](/3.9.8), §8.3.2), becomes reliable after blocking. The coefficients $\boldsymbol{\beta}(j)$ may also differ between blocks, which allows the effect of the covariates to vary with the propensity score.

### 10.2.4. The Variance

Within block $j$, the variance of the difference in means is estimated by the Neyman formula of [3.9.4](/3.9.4), $\widehat{\operatorname{Var}}(j) = s_{\mathrm{c}}^2(j)/N_{\mathrm{c}}(j) + s_{\mathrm{t}}^2(j)/N_{\mathrm{t}}(j)$, and for the regression estimate by the usual (preferably heteroskedasticity-robust) least squares variance of $\hat\tau^{\mathrm{adj}}(j)$. The blocks are disjoint and the estimates are conditionally independent, so

$$
\widehat{\operatorname{Var}}\bigl(\hat\tau^{\mathrm{strat}}\bigr) = \sum_{j=1}^{J}q(j)^2\,\widehat{\operatorname{Var}}(j), \qquad \widehat{\operatorname{Var}}\bigl(\hat\tau_{\mathrm{t}}^{\mathrm{strat,adj}}\bigr) = \sum_{j=1}^{J}\left(\frac{N_{\mathrm{t}}(j)}{N_{\mathrm{t}}}\right)^2\widehat{\operatorname{Var}}\bigl(\hat\tau^{\mathrm{adj}}(j)\bigr),
$$
and similarly for $\hat\tau^{\mathrm{strat,adj}}$. These formulas treat the blocks as fixed and ignore the estimation of the propensity score; §10.5 discusses the variance more generally.

### 10.2.5. Results for the Lottery Data

**Example 10.2.1 (Blocking and Regression for the Lottery Data)** Within the five blocks, the difference in means and the regression estimate with four covariates (number of tickets, education, working at the time of winning, earnings in the year before winning) give:

| Block | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $N(j)$ | 80 | 40 | 41 | 81 | 81 |
| $\hat\tau^{\mathrm{dif}}(j)$ (s.e.) | $-10.82$ ($4.70$) | $2.07$ ($5.10$) | $-1.17$ ($4.97$) | $-9.43$ ($3.23$) | $-2.89$ ($3.59$) |
| $\hat\tau^{\mathrm{adj}}(j)$ (s.e.) | $-6.21$ ($4.01$) | $-6.51$ ($3.86$) | $-4.81$ ($3.87$) | $-5.88$ ($1.82$) | $-2.56$ ($2.39$) |

The adjustment changes the block estimates considerably and makes them much more homogeneous. Two things follow: the covariates do affect the outcome (earnings in the year before winning has a coefficient between $0.6$ and $0.85$ in every block), and within the blocks there remain enough differences in the covariates for the adjustment to matter. The overall estimates, for different samples, numbers of blocks and covariate sets, are:

| Covariates in the regression | Full sample, 1 block | Trimmed, 1 block | Trimmed, 2 blocks | Trimmed, 5 blocks |
|---|---|---|---|---|
| none | $-6.2$ ($1.4$) | $-6.6$ ($1.7$) | $-6.0$ ($1.9$) | $-5.7$ ($2.0$) |
| four covariates | $-2.8$ ($0.9$) | $-4.0$ ($1.1$) | $-5.6$ ($1.2$) | $-5.1$ ($1.2$) |
| all covariates | $-5.1$ ($1.0$) | $-5.3$ ($1.1$) | $-6.4$ ($1.1$) | $-5.7$ ($1.1$) |

On the full sample without blocks, the estimate ranges from $-6.2$ to $-2.8$ depending on which covariates enter the regression: the answer is driven by the specification. After trimming and blocking into five blocks the three specifications give $-5.7$, $-5.1$ and $-5.7$. Both trimming and blocking greatly reduce the sensitivity to the regression specification, and the combination of trimming, blocking and regression gives a credible estimate: winning a large prize reduces annual labor earnings by about $5000$ to $6000$ dollars over the following years.

:::

## 10.3. Weighting Estimators and Their Relation to Blocking

The **Horvitz–Thompson estimator** of [3.9.8](/3.9.8) (Definition 8.3.1) weights each unit by the inverse of the probability of the treatment it received, $1/e(X_i)$ for treated and $1/(1 - e(X_i))$ for control units. With the true propensity score it is unbiased; with an estimated one, **inverse probability weighting** is consistent if the propensity score model is correct. The blocking estimator turns out to be a weighting estimator in disguise.

**Theorem 10.3.1 (Blocking as Weighting)** The basic blocking estimator can be written as

$$
\hat\tau^{\mathrm{strat}} = \frac{1}{N}\sum_{i=1}^{N}W_i\lambda_i^{\mathrm{strat}}Y_i^{\mathrm{obs}} - \frac{1}{N}\sum_{i=1}^{N}(1 - W_i)\lambda_i^{\mathrm{strat}}Y_i^{\mathrm{obs}}, \qquad \lambda_i^{\mathrm{strat}} = \begin{cases} \sum_{j}B_i(j)\,\dfrac{1}{1 - \tilde e(j)}, & W_i = 0, \\[2ex] \sum_{j}B_i(j)\,\dfrac{1}{\tilde e(j)}, & W_i = 1, \end{cases}
$$
where $\tilde e(j) = N_{\mathrm{t}}(j)/N(j)$ is the proportion of treated units in block $j$. It is therefore the weighting estimator with the propensity score replaced by the block-wise coarsened propensity score $\tilde e(j)$.

**Proof** In block $j$,

$$
q(j)\,\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) = \frac{N(j)}{N}\cdot\frac{1}{N_{\mathrm{t}}(j)}\sum_{i:W_i = 1}B_i(j)Y_i^{\mathrm{obs}} = \frac{1}{N}\sum_{i=1}^{N}W_iB_i(j)\frac{N(j)}{N_{\mathrm{t}}(j)}Y_i^{\mathrm{obs}},
$$
and similarly $q(j)\bar Y_{\mathrm{c}}^{\mathrm{obs}}(j) = \frac{1}{N}\sum_i(1 - W_i)B_i(j)\frac{N(j)}{N_{\mathrm{c}}(j)}Y_i^{\mathrm{obs}}$. Summing over $j$, and using $N(j)/N_{\mathrm{t}}(j) = 1/\tilde e(j)$ and $N(j)/N_{\mathrm{c}}(j) = 1/(1 - \tilde e(j))$, gives the formula. $\square$

Instead of each unit's own estimated score, blocking uses the average assignment rate in its block. This explains its robustness: a treated unit with $\hat e(X_i) = 0.01$ in a block where 10% of the units are treated receives weight $10$, not $100$. The price is the residual bias within blocks, which the regression adjustment of §10.2.3 removes.

The weights of different estimators can be compared directly. In the trimmed lottery sample ($N_{\mathrm{c}} = 172$, $N_{\mathrm{t}} = 151$), the normalized weights of the weighting estimator have a maximum of $9.68$ among the controls, so a single unit counts almost ten times as much as an average one; in the full sample the maximum is $41.7$ and the standard deviation of the control weights $2.69$, a sign of the covariate imbalance and the reason why weighting on the untrimmed sample is sensitive to the propensity score model. Blocking with regression and matching with regression have weights with standard deviation around $1$ in the trimmed sample (their weights can even be negative, because regression extrapolates slightly within blocks or pairs).

## 10.4. Matching Estimators

### 10.4.1. The Minimum Wage Data

**Example 10.4.1 (Fast-Food Employment in New Jersey and Pennsylvania)** Card and Krueger (1994) studied the effect of the increase of the state minimum wage in New Jersey in 1992, using employment at fast-food restaurants in New Jersey and in neighboring eastern Pennsylvania, where the minimum wage did not change. The unit is a restaurant, the treated units are the New Jersey restaurants and the controls the Pennsylvania restaurants; the outcome is the number of employees after the increase. The covariates are the number of employees before the increase, the starting wage, the average time until the first raise and the chain (Burger King, KFC, Roy Rogers or Wendy's). Card and Krueger compared the changes in employment between the two states, a difference-in-differences design; here we use the data only to illustrate matching estimators, under the assumption that assignment is unconfounded given the covariates. To make the mechanics visible, consider a small subsample of 20 restaurants with two covariates, the chain $X_{i1}$ (0 for Burger King, 1 for KFC) and initial employment $X_{i2}$:

| Unit | State | Chain | Initial empl. | Final empl. | Unit | State | Chain | Initial empl. | Final empl. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | NJ | BK | 22.5 | 40.0 | 11 | PA | BK | 20.0 | 19.5 |
| 2 | NJ | KFC | 14.0 | 12.5 | 12 | PA | BK | 13.5 | 21.0 |
| 3 | NJ | BK | 37.5 | 20.0 | 13 | PA | BK | 19.0 | 11.0 |
| 4 | NJ | KFC | 9.0 | 3.5 | 14 | PA | BK | 12.0 | 17.0 |
| 5 | NJ | KFC | 8.0 | 5.5 | 15 | PA | BK | 32.5 | 22.5 |
| 6 | PA | BK | 10.5 | 15.0 | 16 | PA | BK | 16.0 | 20.0 |
| 7 | PA | KFC | 13.8 | 17.0 | 17 | PA | KFC | 11.0 | 14.0 |
| 8 | PA | KFC | 8.5 | 10.5 | 18 | PA | KFC | 4.5 | 6.5 |
| 9 | PA | BK | 25.5 | 18.5 | 19 | PA | BK | 12.5 | 31.5 |
| 10 | PA | BK | 17.0 | 12.5 | 20 | PA | BK | 8.0 | 8.0 |

The first five units are treated ($\mathbb{I}_{\mathrm{t}} = \{1, \dots, 5\}$), the other fifteen controls ($\mathbb{I}_{\mathrm{c}} = \{6, \dots, 20\}$). The estimand is the effect on the treated, the average over the New Jersey restaurants of $Y_i(1) - Y_i(0)$.

:::

### 10.4.2. Matching without Replacement

**Definition 10.4.1 (Matching Estimator)** Given, for each treated unit $i$, a matched control $m_i^{\mathrm{c}}$ (or a set $\mathcal{M}_i^{\mathrm{c}}$ of $M$ controls), the **matching estimator** of the average effect on the treated imputes the missing control outcome of each treated unit by the outcome of its match:

$$
\hat\tau_{\mathrm{t}}^{\mathrm{match}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\hat\tau_i^{\mathrm{match}}, \qquad \hat\tau_i^{\mathrm{match}} = Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}} = Y_i(1) - Y_{m_i^{\mathrm{c}}}(0).
$$

In nearest available matching without replacement, the treated units are taken in a fixed order, and each is matched to the closest control among those not yet used. The result depends on the order and on the distance. In Example 10.4.1 with the distance $d^2 = (x_1 - x_1')^2 + (x_2 - x_2')^2$ and the order $1, \dots, 5$, the matches are units 11, 7, 15, 8 and 20, the unit-level estimates are $20.5$, $-4.5$, $-2.5$, $-7$ and $-2.5$, and $\hat\tau_{\mathrm{t}}^{\mathrm{match}} = 0.8$. Two changes illustrate the arbitrariness:

- With the order $1, 2, 3, 5, 4$, unit 5 takes control 8 (another KFC restaurant with 8.5 employees) and unit 4 gets control 20, a Burger King. The average happens to stay $0.8$, but two of the five pairs change.
- With the distance $100(x_1 - x_1')^2 + (x_2 - x_2')^2$, which practically requires exact matching on the chain, unit 5 is matched to control 17 (KFC, 11 employees) instead of 20 (Burger King, 8 employees), and the estimate becomes $-0.4$.

The choice of distance expresses a judgment about which covariates matter most, and the Mahalanobis distance of [3.9.9](/3.9.9) is a default that standardizes the covariates and accounts for their correlation.

### 10.4.3. Matching with Replacement and Multiple Matches

With replacement, each treated unit is matched to its closest control, $m_i^{\mathrm{c}} = \arg\min_{i' \in \mathbb{I}_{\mathrm{c}}}\lVert X_i - X_{i'}\rVert$, regardless of whether that control has been used already. Let $L(i)$ be the number of times unit $i$ is used as a match. Then

$$
\hat\tau_{\mathrm{t}}^{\mathrm{repl}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}}\bigr) = \frac{1}{N_{\mathrm{t}}}\sum_{i=1}^{N}\Bigl(W_iY_i^{\mathrm{obs}} - (1 - W_i)L(i)Y_i^{\mathrm{obs}}\Bigr).
$$
The order no longer matters and every match is the best available, so the bias is smaller; but controls used many times get large weights $L(i)$, which increases the variance. In Example 10.4.1 both units 4 and 5 are matched to control 8, which is used twice, and the estimate is $(20.5 - 4.5 - 2.5 - 7 - 5)/5 = 0.3$.

Allowing $M$ matches per treated unit, with $\mathcal{M}_i^{\mathrm{c}}$ the set of the $M$ closest controls,

$$
\hat\tau_{\mathrm{t}}^{\mathrm{match},M} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\left(Y_i(1) - \frac{1}{M}\sum_{j \in \mathcal{M}_i^{\mathrm{c}}}Y_j(0)\right).
$$
If the matched controls are all distinct and, given the covariates, the outcomes have variances $\sigma_{\mathrm{t}}^2$ and $\sigma_{\mathrm{c}}^2$, the conditional variance is

$$
\operatorname{Var}\bigl(\hat\tau_{\mathrm{t}}^{\mathrm{match},M} \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr) = \frac{1}{N_{\mathrm{t}}}\left(\sigma_{\mathrm{t}}^2 + \frac{\sigma_{\mathrm{c}}^2}{M}\right).
$$
With $\sigma_{\mathrm{c}}^2 = \sigma_{\mathrm{t}}^2 = \sigma^2$, the proportional reduction relative to a single match is

$$
\frac{\operatorname{Var}(\hat\tau_{\mathrm{t}}^{\mathrm{match},1}) - \operatorname{Var}(\hat\tau_{\mathrm{t}}^{\mathrm{match},M})}{\operatorname{Var}(\hat\tau_{\mathrm{t}}^{\mathrm{match},1})} = \frac{2\sigma^2 - \sigma^2(1 + 1/M)}{2\sigma^2} = \frac{M - 1}{2M},
$$
which is 25% for $M = 2$, 33% for $M = 3$ and tends to 50% as $M \to \infty$: the treated outcome's own variance can never be reduced by more matches. The gains diminish quickly, while the additional matches are worse and add bias, so small values of $M$ (one to four) are usual.

### 10.4.4. The Bias of Matching and Bias Correction

Unless matches are exact, matching leaves a bias. For a treated unit $i$ with match $m_i^{\mathrm{c}}$, let $D_i = X_i - X_{m_i^{\mathrm{c}}}$ be the matching discrepancy ($D_i = 0$ for an exact match). Then

$$
\mathbb{E}\bigl[\hat\tau_i^{\mathrm{match}} \bigm| W_i = 1, X_i, X_{m_i^{\mathrm{c}}}\bigr] = \mu_1(X_i) - \mu_0(X_{m_i^{\mathrm{c}}}) = \tau(X_i) + \bigl(\mu_0(X_i) - \mu_0(X_{m_i^{\mathrm{c}}})\bigr),
$$
where $\tau(x) = \mu_1(x) - \mu_0(x)$. The unit-level bias is $B_i = \mu_0(X_i) - \mu_0(X_{m_i^{\mathrm{c}}})$, zero for an exact match and small when $D_i$ is small and $\mu_0$ is smooth. With many continuous covariates the discrepancies shrink slowly as the sample grows (Abadie and Imbens 2006), and the bias can dominate the variance in large samples. The remedy is to estimate the bias and subtract it.

**Definition 10.4.2 (Bias-Corrected Matching Estimator)** With an estimate $\hat\mu_0$ of the control regression function, impute $\hat Y_i(0) = Y_{m_i^{\mathrm{c}}}(0) + \hat\mu_0(X_i) - \hat\mu_0(X_{m_i^{\mathrm{c}}})$. The **bias-corrected matching estimator** is

$$
\hat\tau_{\mathrm{t}}^{\mathrm{adj}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\bigl(Y_i(1) - \hat Y_i(0)\bigr) = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\bigl(Y_i(1) - Y_{m_i^{\mathrm{c}}}(0) - \hat B_i\bigr).
$$

With a linear model the estimated bias is $\hat B_i = D_i\hat{\boldsymbol{\beta}}$, and the estimators differ in how $\hat{\boldsymbol{\beta}}$ is obtained:

1. Difference regression. Assume $\mu_0(x) = \alpha + x\boldsymbol{\beta}$ and $\mu_1(x) = \tau + \mu_0(x)$. Then $Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}} = \tau + D_i\boldsymbol{\beta} + \nu_i$, where $\nu_i = (Y_i(1) - \mu_1(X_i)) - (Y_{m_i^{\mathrm{c}}}(0) - \mu_0(X_{m_i^{\mathrm{c}}}))$ has mean zero given $\boldsymbol{X}$ and $\boldsymbol{W}$. Regressing the pair differences on the discrepancies over the treated units,

   $$
   \hat{\boldsymbol{\beta}}_{\mathrm{d}} = \left(\sum_{i:W_i = 1}(D_i - \bar D)^{\mathsf T}(D_i - \bar D)\right)^{-1}\sum_{i:W_i = 1}(D_i - \bar D)^{\mathsf T}\bigl(Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}}\bigr),
   $$
   gives $\hat\tau_{\mathrm{t}}^{\mathrm{adj,d}} = \hat\tau_{\mathrm{t}}^{\mathrm{match}} - \bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}}$, the regression intercept.
2. Control regression. Estimate $\boldsymbol{\beta}$ by regressing the outcomes of the matched control units on their covariates.
3. Separate regressions. Estimate $\mu_0$ and $\mu_1$ by separate regressions in the matched control and treated samples, allowing the effect to vary with the covariates.

In all three the regression is local: it uses only the matched sample, in which the covariate distributions are similar, and it only corrects the small differences $D_i$. As with blocking and regression, misspecification of the linear model now has only a second-order effect.

**Example 10.4.2 (Results for the Minimum Wage Data)** For the full data set, matching with replacement gives the following estimates of the effect of the minimum wage increase on employment, in employees per restaurant:

| Estimand | Method | $M$ | Distance | Estimate |
|---|---|---|---|---|
| New Jersey | regression, no covariates | | | $-0.22$ |
| New Jersey | regression with covariates | | | $1.35$ |
| New Jersey | matching | 1 | Mahalanobis | $0.89$ |
| New Jersey | matching | 4 | Mahalanobis | $1.01$ |
| New Jersey | matching | 1 | Euclidean | $0.93$ |
| New Jersey | matching | 1 | exact on chain, Mahalanobis on others | $0.92$ |
| Pennsylvania | matching | 1 | Mahalanobis | $0.63$ |
| All | matching | 1 | Mahalanobis | $0.84$ |
| New Jersey | bias-corrected (difference regression) | 1 | Mahalanobis | $0.51$ |

The matching estimates are robust to minor changes in the implementation: the number of matches, the distance and exact matching on the chain change the estimate little. Mahalanobis and Euclidean distances give similar results here because the covariates are nearly uncorrelated. None of the estimates suggests that the higher minimum wage reduced employment at these restaurants; this agrees with Card and Krueger's finding, although their analysis was based on changes over time rather than on matching.

:::

## 10.5. The Variance of the Estimators

All the estimators of this and the previous chapters are weighted averages of the observed outcomes,

$$
\hat\tau = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\lambda_iY_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\lambda_iY_i^{\mathrm{obs}}, \qquad \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\lambda_i = \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\lambda_i = 1,
$$
with weights $\lambda_i = \lambda(W_i, X_i, \boldsymbol{W}_{(-i)}, \boldsymbol{X}_{(-i)})$ that depend on the treatments and covariates but not on the outcomes:

| Estimator | Weight $\lambda_i$ |
|---|---|
| difference in means | $1$ |
| weighting | $\frac{N_{\mathrm{t}}}{e(X_i)}\Big/\sum_{j:W_j = 1}\frac{1}{e(X_j)}$ for treated, $\frac{N_{\mathrm{c}}}{1 - e(X_i)}\Big/\sum_{j:W_j = 0}\frac{1}{1 - e(X_j)}$ for controls |
| subclassification | $\sum_jB_i(j)\frac{N(j)/N}{N_{\mathrm{t}}(j)/N_{\mathrm{t}}}$ for treated, $\sum_jB_i(j)\frac{N(j)/N}{N_{\mathrm{c}}(j)/N_{\mathrm{c}}}$ for controls |
| matching (effect on all units) | determined by how often each unit is used as a match |
| regression | a linear function of $X_i$, possibly negative |

Write $\mu_i = \mu_{W_i}(X_i)$ and $\sigma_i^2 = \sigma_{W_i}^2(X_i)$. Conditionally on $(\boldsymbol{X}, \boldsymbol{W})$ the outcomes are independent, so

$$
\hat\tau = \left(\frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\lambda_i\mu_i - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\lambda_i\mu_i\right) + \left(\frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\lambda_i(Y_i^{\mathrm{obs}} - \mu_i) - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\lambda_i(Y_i^{\mathrm{obs}} - \mu_i)\right)
$$
and

$$
\operatorname{Var}\bigl(\hat\tau \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr) = \frac{1}{N_{\mathrm{t}}^2}\sum_{i:W_i = 1}\lambda_i^2\sigma_i^2 + \frac{1}{N_{\mathrm{c}}^2}\sum_{i:W_i = 0}\lambda_i^2\sigma_i^2.
$$
The first bracket is the conditional mean of the estimator, whose deviation from the estimand is the bias; the second has the variance above. The formula explains the weight comparison of §10.3: the variance grows with $\sum\lambda_i^2$, so a few large weights inflate it. To estimate it we need $\sigma_i^2$. A simple and general method matches within the same treatment group: for unit $i$ find the unit $j(i)$ with the same treatment and the closest covariates, and use $\hat\sigma_i^2 = \frac{1}{2}(Y_i^{\mathrm{obs}} - Y_{j(i)}^{\mathrm{obs}})^2$, which is approximately unbiased because $\mathbb{E}[(Y_i - Y_{j})^2] \approx 2\sigma^2_{W_i}(X_i)$ when $X_i \approx X_j$. Plugging in gives $\widehat{\operatorname{Var}}(\hat\tau \mid \boldsymbol{X}, \boldsymbol{W})$, the variance conditional on the covariates, appropriate for the average effect in the sample; the super-population variance adds the variance of the conditional average effect $\tau(X_i)$. The naive **bootstrap** is not valid for matching estimators with a fixed number of matches (Abadie and Imbens 2008), because resampling changes the matching structure in a way that does not mimic the sampling distribution; the matching-based variance estimator avoids this problem.

## 10.6. The Complete Workflow

The three chapters on regular assignment mechanisms combine into one workflow:

| Stage | Step | Tools | Chapter |
|---|---|---|---|
| Design | estimate the propensity score | logistic regression, three-step covariate selection | [3.9.8](/3.9.8) |
| Design | assess balance | normalized differences, log ratios of standard deviations, Mahalanobis distance, linearized propensity score, overlap | [3.9.9](/3.9.9) |
| Design | improve balance | trimming (if necessary); blocking on the propensity score or matching on the Mahalanobis or propensity score distance | [3.9.9](/3.9.9) |
| Analysis | estimate the effect | weighting; blocking with regression within blocks; matching with regression (bias correction) | this chapter |
| Analysis | inference | variance of the linear estimators, confidence intervals and tests | this chapter |

The most important elements are the propensity score as a measure of balance, blocking and matching to improve it, and regression adjustment within blocks or matched sets to remove what remains. The figure compares the estimators on simulated data with a nonlinear outcome model.

![Sampling distributions over 300 simulated observational studies (N = 1000, two covariates, a nonlinear control outcome and a constant effect of 2) of the difference in means, linear regression, normalized inverse probability weighting with a logistic propensity score, blocking into five propensity score quintiles with and without regression within blocks, nearest-neighbor matching with replacement for the effect on the treated, and bias-corrected matching. Simulated data](./plots/estimator_comparison.py)

The difference in means is far off. Linear regression and plain blocking still carry a bias, the first because the linear model is wrong, the second because five blocks leave residual imbalance. Weighting is nearly unbiased but has the largest variance. Blocking with regression within blocks is nearly unbiased and the most precise: each regression only has to correct a small imbalance, so the misspecification hardly matters. Matching has a small bias from inexact matches, which the bias correction reduces.

## Summary

- Bias of the difference in means (Theorem 10.2.1): under unconfoundedness and $\mu_w(x) = \alpha + \tau w + x\boldsymbol{\beta}$, $\mathbb{E}[\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} \mid \boldsymbol{X}, \boldsymbol{W}] = (\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta}$; after blocking it shrinks to $\sum_jq(j)(\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j))\boldsymbol{\beta}$ (Corollary 10.2.1).
- Blocking with regression: $\hat\tau^{\mathrm{strat,adj}} = \sum_jq(j)\hat\tau^{\mathrm{adj}}(j)$ (average effect) or $\sum_j\frac{N_{\mathrm{t}}(j)}{N_{\mathrm{t}}}\hat\tau^{\mathrm{adj}}(j)$ (effect on the treated); variance $\sum_jq(j)^2\widehat{\operatorname{Var}}(j)$. The lottery data show that trimming and blocking make the estimate insensitive to the regression specification.
- Blocking is weighting with the coarsened score $\tilde e(j) = N_{\mathrm{t}}(j)/N(j)$ (Theorem 10.3.1), hence more stable than weighting with $\hat e(X_i)$.
- **Matching estimators** (effect on the treated):

  | Variant | Bias | Variance | Note |
  |---|---|---|---|
  | without replacement | larger, depends on order | smaller | result depends on the match order |
  | with replacement | smaller | larger (weights $L(i)$) | order irrelevant |
  | $M$ matches | larger | reduced by $(M - 1)/(2M)$ at most 50% | $\sigma_{\mathrm{c}} = \sigma_{\mathrm{t}}$ |
  | bias-corrected | $\hat B_i = D_i\hat{\boldsymbol{\beta}}$ removed | about the same | local regression on the matched sample |

- All estimators are linear in $Y^{\mathrm{obs}}$, $\hat\tau = \frac{1}{N_{\mathrm{t}}}\sum_{W_i = 1}\lambda_iY_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{W_i = 0}\lambda_iY_i^{\mathrm{obs}}$, with conditional variance $\sum\lambda_i^2\sigma_i^2/N_w^2$; $\sigma_i^2$ is estimated by matching within treatment groups.

## Questions

1. Prove Theorem 10.2.1 for $N = 3$ with units 1 and 2 treated and unit 3 control, writing out each term.

   **Answer** $\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} = \frac{1}{2}(Y_1(1) + Y_2(1)) - Y_3(0) - \frac{1}{3}\sum_{i}(Y_i(1) - Y_i(0))$. Taking conditional expectations with $\mu_w(x) = \alpha + \tau w + x\boldsymbol{\beta}$: the $Y(1)$ terms give $\frac{1}{6}(\mu_1(X_1) + \mu_1(X_2)) - \frac{1}{3}\mu_1(X_3) = \frac{1}{3}(\bar X_{\mathrm{t}} - X_3)\boldsymbol{\beta}$ and the $Y(0)$ terms give $-\frac{2}{3}\mu_0(X_3) + \frac{1}{3}(\mu_0(X_1) + \mu_0(X_2)) = \frac{2}{3}(\bar X_{\mathrm{t}} - X_3)\boldsymbol{\beta}$, the constants $\alpha$, $\tau$ cancelling in each group. The sum is $(\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta}$ with $\bar X_{\mathrm{c}} = X_3$; the weights $N_{\mathrm{c}}/N = 1/3$ and $N_{\mathrm{t}}/N = 2/3$ are those of the proof.
2. Show that if the linear model of Theorem 10.2.1 holds and regression is applied to the whole sample, the regression estimator is conditionally unbiased. Why, then, is regression on the raw sample not recommended?

   **Answer** Under the model with a common $\boldsymbol{\beta}$, $Y_i^{\mathrm{obs}} = \alpha + \tau_{\mathrm{sp}}W_i + X_i\boldsymbol{\beta} + \varepsilon_i$ with $\mathbb{E}[\varepsilon_i \mid \boldsymbol{X}, \boldsymbol{W}] = 0$, so least squares is conditionally unbiased for $\tau_{\mathrm{sp}}$. The problem is that the model is only an approximation: when $\bar X_{\mathrm{t}}$ and $\bar X_{\mathrm{c}}$ differ much, the estimate depends on the model in regions where one group has no data, and small misspecifications (a quadratic term, an interaction) produce large biases, as the lottery data show ($-6.2$ to $-2.8$ on the full sample).
3. A trimmed sample has two blocks. Block 1: 60 controls, 20 treated, $\hat\tau^{\mathrm{dif}}(1) = 1.0$ with variance estimate $0.10$; block 2: 20 controls, 40 treated, $\hat\tau^{\mathrm{dif}}(2) = 2.5$ with variance estimate $0.12$. Compute $\hat\tau^{\mathrm{strat}}$, the estimate of the effect on the treated, and their standard errors.

   **Answer** $q = (80/140, 60/140) = (0.571, 0.429)$: $\hat\tau^{\mathrm{strat}} = 0.571 + 1.071 = 1.64$, variance $0.571^2 \times 0.10 + 0.429^2 \times 0.12 = 0.0327 + 0.0221 = 0.0547$, s.e. $0.234$. Treated weights $(20/60, 40/60)$: $\hat\tau_{\mathrm{t}} = 0.333 + 1.667 = 2.0$, variance $0.111 \times 0.10 + 0.444 \times 0.12 = 0.0644$, s.e. $0.254$. The effect on the treated is larger because the treated are concentrated in the block with the larger effect.
4. Using Theorem 10.3.1, compute the weights of a treated and a control unit in block 1 of Question 3, and compare them with Horvitz–Thompson weights if the individual estimated propensity scores in that block range from $0.05$ to $0.45$.

   **Answer** $\tilde e(1) = 20/80 = 0.25$, so treated units get $1/0.25 = 4$ and controls $1/0.75 = 1.33$. With individual scores, treated units get $1/\hat e$ between $2.2$ and $20$, and controls $1/(1 - \hat e)$ between $1.05$ and $1.8$. Blocking replaces the extreme weight $20$ by the block average, trading the small within-block bias for a much smaller variance.
5. In Example 10.4.1, verify the estimate $0.3$ of matching with replacement, and compute the weights $L(i)$ of the controls.

   **Answer** The closest controls (Euclidean distance) are: unit 1 (BK, 22.5) to 11 (BK, 20.0); unit 2 (KFC, 14.0) to 7 (KFC, 13.8); unit 3 (BK, 37.5) to 15 (BK, 32.5); units 4 (KFC, 9.0) and 5 (KFC, 8.0) both to 8 (KFC, 8.5). The differences are $40 - 19.5 = 20.5$, $12.5 - 17 = -4.5$, $20 - 22.5 = -2.5$, $3.5 - 10.5 = -7$, $5.5 - 10.5 = -5$, with mean $1.5/5 = 0.3$. $L(8) = 2$, $L(7) = L(11) = L(15) = 1$, and the other controls have $L(i) = 0$.
6. Derive the variance reduction $(M - 1)/(2M)$ and explain why it cannot exceed 50%. Under what circumstances is the assumption that the matched controls are distinct violated, and what happens then?

   **Answer** With distinct controls the average of $M$ control outcomes has conditional variance $\sigma^2/M$, so $\operatorname{Var}(\hat\tau_{\mathrm{t}}^{\mathrm{match},M}) = (\sigma^2 + \sigma^2/M)/N_{\mathrm{t}}$, and the reduction relative to $2\sigma^2/N_{\mathrm{t}}$ is $(1 - 1/M)/2$. The treated outcome contributes $\sigma^2/N_{\mathrm{t}}$ regardless of $M$, half of the single-match variance, so the reduction is below 50%. With replacement, the same control is often used by several treated units (large $L(i)$), the control terms are correlated, and the variance is larger than the formula states; it is given by the general formula $\sum\lambda_i^2\sigma_i^2/N_{\mathrm{c}}^2$ with $\lambda_i \propto L(i)$.
7. Show that the difference-regression bias correction gives $\hat\tau_{\mathrm{t}}^{\mathrm{adj,d}} = \hat\tau_{\mathrm{t}}^{\mathrm{match}} - \bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}}$, and interpret the correction.

   **Answer** Regressing $\Delta Y_i = Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}}$ on $(1, D_i)$ over the treated gives slope $\hat{\boldsymbol{\beta}}_{\mathrm{d}}$ and intercept $\overline{\Delta Y} - \bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}} = \hat\tau_{\mathrm{t}}^{\mathrm{match}} - \bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}}$. The same value results from averaging $\Delta Y_i - D_i\hat{\boldsymbol{\beta}}_{\mathrm{d}}$. The intercept is the predicted pair difference at zero discrepancy, that is, for exact matches; $\bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}}$ estimates the average bias $\frac{1}{N_{\mathrm{t}}}\sum B_i$ caused by systematic discrepancies.
8. Explain why the variance estimate $\hat\sigma_i^2 = \frac{1}{2}(Y_i^{\mathrm{obs}} - Y_{j(i)}^{\mathrm{obs}})^2$ uses a match within the same treatment group, and what would go wrong if one used the match in the other group.

   **Answer** Within the same group, $Y_i$ and $Y_{j(i)}$ are independent with nearly the same mean $\mu_{W_i}(X_i)$ and variances $\sigma_{W_i}^2$, so $\mathbb{E}[(Y_i - Y_{j(i)})^2] \approx 2\sigma_{W_i}^2(X_i)$. A match in the other group has mean $\mu_{1 - W_i}(X_i)$, so the squared difference also contains the squared unit-level effect $\tau(X_i)^2$ and the variance of the other potential outcome; the estimate would be biased upward by the treatment effect and would not estimate $\sigma_{W_i}^2$.
