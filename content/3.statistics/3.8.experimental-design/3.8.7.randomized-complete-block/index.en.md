---
title: Randomized Complete Block Designs
description: The blocking principle and the randomized complete block design; the additive block model, least squares estimates, the ANOVA with expected mean squares and the vascular graft example; whether to test blocks, residual analysis and multiple comparisons; relative efficiency with respect to the completely randomized design; random blocks; missing values; the generalized complete block design with replicates, the block-by-treatment interaction as the error term, and the mixed model.
---

Of the three basic principles of experimental design in [3.8.2](/3.8.2), randomization and replication have been at work in every chapter so far; this chapter is about the third, **blocking**. Many experiments are run on material that is not homogeneous: batches of raw material, test specimens, fields, days, operators. If the experimental units are assigned to treatments completely at random, the differences between batches or days end up in the error, which then hides the treatment effects. Blocking takes these differences out of the error by comparing the treatments within groups of similar units. The simplest blocked design, the randomized complete block design, was introduced in [3.8.6](/3.8.6) as an example of the **additive model**; here we develop it fully: the model and its analysis of variance, the question of whether the blocks should be tested, multiple comparisons, its efficiency relative to the completely randomized design, random blocks, missing observations, and the extension to blocks that contain several replicates of each treatment, which leads to the first mixed model of the course. The next chapter, [3.8.8](/3.8.8), controls two nuisance factors at once with Latin squares.

The notation is that of [3.8.3](/3.8.3) and [3.8.6](/3.8.6): $a$ treatments indexed by $i$, $b$ blocks indexed by $j$, $N=ab$ observations, dots for summation and bars for averages, $Y_{ij}$ in models and $y_{ij}$ in data. All quantiles are upper quantiles: $F_{\nu_1,\nu_2,\alpha}$ is the point with probability $\alpha$ above it.

## 7.1. The Blocking Principle

### 7.1.1. Nuisance Factors

Recall from Definition 2.1.4 of [3.8.2](/3.8.2) that a **nuisance factor** is a factor that probably affects the response but is of no interest to the experimenter. Typical examples are batches of raw material, operators, pieces of test equipment, time (shifts, days) and the experimental units themselves when they are heterogeneous. In the model $y=\mu+\varepsilon$ with $\varepsilon\sim\mathcal{N}(0,\sigma^2)$ the effect of an unaccounted nuisance factor is part of $\sigma^2$, the unexplained variation; much industrial experimentation involves blocking, or should, to reduce it. Failure to block is one of the most common flaws in the design of experiments.

Blocking originated in agricultural field trials. To compare several varieties of a crop (or levels of a fertilizer), one takes a section of land, divides it into plots and assigns the varieties to the plots at random. A large number of plots, however, tends to be very heterogeneous: fertility, moisture and drainage change across the field, and in a completely random assignment some varieties will by chance land on better soil. The remedy is to group neighboring plots, which are similar, into blocks, and to compare all varieties within each block. In general, a **block** is a set of homogeneous experimental units, and typically it is one level of the nuisance factor: one batch, one day, one strip of land.

### 7.1.2. How to Handle a Nuisance Variable

Which technique deals with a nuisance variable depends on two questions: is the source of variation known, and can it be controlled?

| The nuisance variable is | Technique | How it works |
|---|---|---|
| known and controllable | blocking | run all treatments within each level of the variable (a block may also be a combination of several variables, such as "machine and day") |
| known, measurable but not controllable | **analysis of covariance** | measure the variable (a covariate) on each unit and remove its effect by regression |
| unknown and uncontrollable | **randomization** | the variable becomes a **lurking variable**; random assignment balances its effect over the treatments on average |

The principles combine in the rule of [3.8.2](/3.8.2): block what you can, randomize what you cannot. Blocking does not replace randomization; within each block the treatments are still randomized.

## 7.2. The Randomized Complete Block Design

### 7.2.1. The Hardness Testing Example

We wish to determine whether four different tips produce different mean hardness readings on a Rockwell hardness tester. The machine presses the tip into a metal test coupon, and the hardness is read from the depth of the depression. A completely randomized design would assign each tip to a number of coupons at random. The coupons, however, may come from different heats of metal and differ in hardness; that variation would enter the error and blur the comparison of the tips. Since the coupons are large enough to take four tests each, a better design tests all four tips on each coupon: each coupon is a block, and within a coupon the order in which the tips are tested is randomized. With $b=4$ coupons one possible randomization is

| Coupon 1 | Coupon 2 | Coupon 3 | Coupon 4 |
|---|---|---|---|
| tip 3 | tip 3 | tip 2 | tip 1 |
| tip 1 | tip 4 | tip 1 | tip 4 |
| tip 4 | tip 2 | tip 3 | tip 2 |
| tip 2 | tip 1 | tip 4 | tip 3 |

The experiment has a two-way structure, treatments by blocks, and its defining feature is that each block sees each treatment exactly once. The variability between blocks may be large, but the variability within a block should be relatively small, and the treatments are compared within blocks. The blocks are a restriction on randomization: all runs within a block are randomized, but not across blocks. Each block contains a complete replicate of the basic experiment, so the block size equals the number of treatments.

**Definition 7.2.1 (Randomized Complete Block Design)** In a **randomized complete block design** (RCBD) with $a$ treatments and $b$ blocks, each block consists of $a$ experimental units, every treatment is applied to exactly one unit in every block, and the treatments are assigned to the units at random, separately and independently in each block. There are $(a!)^b$ equally likely randomizations.

In the terminology of causal inference, the RCBD is a [stratified randomized experiment](/3.9.2#def-2.4.7) in which every stratum contains one unit per treatment; the **paired design** of [3.8.2](/3.8.2) is the RCBD with $a=2$ (Section 7.3.6).

### 7.2.2. The Model

**Definition 7.2.2 (Effects Model of the RCBD)** The effects model of the randomized complete block design is

$$
Y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij},\qquad i=1,\dots,a,\quad j=1,\dots,b,\qquad \sum_{i=1}^a\tau_i=0,\quad \sum_{j=1}^b\beta_j=0,
$$
where $\mu$ is the overall mean, $\tau_i$ is the effect of the $i$-th treatment, $\beta_j$ is the effect of the $j$-th block, and the errors $\varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$.

This is the additive model of Definition 6.4.1 in [3.8.6](/3.8.6), with $\tau_i$ for the treatment factor and $\beta_j$ for the block factor, and like every ANOVA model it is a general linear model: a linear regression on the indicator variables of the treatments and the blocks. Its assumption that treatments and blocks do not interact is a design assumption: the treatment effects are the same in every block, and the error term reflects how the treatment differences vary from one block to another. The treatment means are $\mu_i=\mu+\tau_i$, and the hypotheses of interest are

$$
H_0\colon\tau_1=\tau_2=\cdots=\tau_a=0\qquad\text{versus}\qquad H_1\colon\tau_i\ne0\ \text{for at least one }i,
$$
equivalently $H_0\colon\mu_1=\cdots=\mu_a$. The blocks enter the model only to remove their variability.

### 7.2.3. Least Squares Estimation

**Proposition 7.2.1** Under the constraints $\sum_i\tau_i=\sum_j\beta_j=0$, the least squares estimates in the RCBD model are

$$
\hat\mu=\bar y_{\cdot\cdot},\qquad \hat\tau_i=\bar y_{i\cdot}-\bar y_{\cdot\cdot},\qquad \hat\beta_j=\bar y_{\cdot j}-\bar y_{\cdot\cdot},
$$
the fitted values are $\hat y_{ij}=\bar y_{i\cdot}+\bar y_{\cdot j}-\bar y_{\cdot\cdot}$, and the residuals are $e_{ij}=y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot}$.

**Proof** Minimize $L=\sum_{i,j}(y_{ij}-\mu-\tau_i-\beta_j)^2$. Setting the derivatives with respect to $\mu$, $\tau_i$ and $\beta_j$ to zero gives the normal equations

$$
ab\,\mu+b\sum_i\tau_i+a\sum_j\beta_j=y_{\cdot\cdot},\qquad b\mu+b\tau_i+\sum_j\beta_j=y_{i\cdot},\qquad a\mu+\sum_i\tau_i+a\beta_j=y_{\cdot j}.
$$
These $1+a+b$ equations have rank $a+b-1$ (the treatment equations and the block equations each sum to the first equation), so two constraints are needed. With $\sum_i\tau_i=\sum_j\beta_j=0$ the first equation gives $\hat\mu=\bar y_{\cdot\cdot}$, the second $\hat\tau_i=\bar y_{i\cdot}-\hat\mu$ and the third $\hat\beta_j=\bar y_{\cdot j}-\hat\mu$. Since $L$ is a convex quadratic, this solution is the minimum. $\square$

Every block contains every treatment once, so the treatment and block indicator columns are orthogonal after centering: $\hat\tau_i$ does not depend on the blocks, and $\hat\beta_j$ does not depend on the treatments. A contrast of treatment means $\sum_ic_i\mu_i$ with $\sum_ic_i=0$ is estimated by $\sum_ic_i\bar y_{i\cdot}$, in which the block effects cancel, with variance $\sigma^2\sum_ic_i^2/b$. In particular $\operatorname{Var}(\bar Y_{i\cdot}-\bar Y_{k\cdot})=2\sigma^2/b$.

## 7.3. Analysis of Variance

### 7.3.1. The Partition of the Total Sum of Squares

Writing $y_{ij}-\bar y_{\cdot\cdot}=(\bar y_{i\cdot}-\bar y_{\cdot\cdot})+(\bar y_{\cdot j}-\bar y_{\cdot\cdot})+(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})$, squaring and summing, the cross products vanish (each is a sum of products of a row pattern, a column pattern and a doubly centered array), and

$$
\underbrace{\sum_{i=1}^a\sum_{j=1}^b(y_{ij}-\bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{T}}}
=\underbrace{b\sum_{i=1}^a(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{Tr}}}
+\underbrace{a\sum_{j=1}^b(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{Blocks}}}
+\underbrace{\sum_{i=1}^a\sum_{j=1}^b(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{E}}},
$$
that is, $\mathrm{SS}_{\mathrm{T}}=\sum_{i,j}(y_{ij}-\hat\mu)^2$, $\mathrm{SS}_{\mathrm{Tr}}=b\sum_i\hat\tau_i^2$, $\mathrm{SS}_{\mathrm{Blocks}}=a\sum_j\hat\beta_j^2$ and $\mathrm{SS}_{\mathrm{E}}=\sum_{i,j}(y_{ij}-\hat\mu-\hat\tau_i-\hat\beta_j)^2$. The degrees of freedom split in the same way,

$$
ab-1=(a-1)+(b-1)+(a-1)(b-1).
$$
For hand computation the totals are used:

$$
\mathrm{SS}_{\mathrm{T}}=\sum_{i,j}y_{ij}^2-\frac{y_{\cdot\cdot}^2}{N},\qquad \mathrm{SS}_{\mathrm{Tr}}=\frac1b\sum_iy_{i\cdot}^2-\frac{y_{\cdot\cdot}^2}{N},\qquad \mathrm{SS}_{\mathrm{Blocks}}=\frac1a\sum_jy_{\cdot j}^2-\frac{y_{\cdot\cdot}^2}{N},
$$
and the error sum of squares is obtained by subtraction, $\mathrm{SS}_{\mathrm{E}}=\mathrm{SS}_{\mathrm{T}}-\mathrm{SS}_{\mathrm{Tr}}-\mathrm{SS}_{\mathrm{Blocks}}$.

Compared with the one-way ANOVA of [3.8.3](/3.8.3) on the same $N$ observations, the treatment sum of squares is unchanged, and the one-way error sum of squares $\mathrm{SS}_{\mathrm{Blocks}}+\mathrm{SS}_{\mathrm{E}}$ with $a(b-1)$ degrees of freedom is split into the part due to blocks, with $b-1$ degrees of freedom, and the residual.

### 7.3.2. Expected Mean Squares and the F-Test

**Theorem 7.3.1** In the RCBD model with fixed treatment and block effects,

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+\frac{b\sum_{i=1}^a\tau_i^2}{a-1},\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{Blocks}}]=\sigma^2+\frac{a\sum_{j=1}^b\beta_j^2}{b-1},\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2,
$$
where $\mathrm{MS}_{\mathrm{Tr}}=\mathrm{SS}_{\mathrm{Tr}}/(a-1)$, $\mathrm{MS}_{\mathrm{Blocks}}=\mathrm{SS}_{\mathrm{Blocks}}/(b-1)$ and $\mathrm{MS}_{\mathrm{E}}=\mathrm{SS}_{\mathrm{E}}/[(a-1)(b-1)]$. Moreover $\mathrm{SS}_{\mathrm{Tr}}$, $\mathrm{SS}_{\mathrm{Blocks}}$ and $\mathrm{SS}_{\mathrm{E}}$ are independent, $\mathrm{SS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{(a-1)(b-1)}$, and under $H_0\colon\tau_1=\cdots=\tau_a=0$, $\mathrm{SS}_{\mathrm{Tr}}/\sigma^2\sim\chi^2_{a-1}$, so that

$$
F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\ \overset{H_0}{\sim}\ F_{a-1,(a-1)(b-1)} .
$$

**Proof** Substituting the model, $\bar Y_{i\cdot}-\bar Y_{\cdot\cdot}=\tau_i+(\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot\cdot})$, because the block effects average to $\bar\beta=0$ in every treatment mean. The $\bar\varepsilon_{i\cdot}$ are independent $\mathcal{N}(0,\sigma^2/b)$, so $\mathbb{E}\sum_i(\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot\cdot})^2=(a-1)\sigma^2/b$, the cross term has expectation zero, and $\mathbb{E}[\mathrm{SS}_{\mathrm{Tr}}]=b\sum_i\tau_i^2+(a-1)\sigma^2$. The block mean square is handled in the same way. The residual is $Y_{ij}-\bar Y_{i\cdot}-\bar Y_{\cdot j}+\bar Y_{\cdot\cdot}=\varepsilon_{ij}-\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot j}+\bar\varepsilon_{\cdot\cdot}$, free of all parameters. In $\mathbb{R}^{ab}$ the four components of $\boldsymbol{\varepsilon}$, the grand mean, the row effects, the column effects and the doubly centered residual, are its orthogonal projections onto subspaces of dimensions $1$, $a-1$, $b-1$ and $(a-1)(b-1)$. By Cochran's theorem ([3.8.3](/3.8.3)) the squared lengths divided by $\sigma^2$ are independent $\chi^2$ variables with these degrees of freedom (noncentral for the treatment and block components when the effects are nonzero), which gives all the claims. $\square$

Under $H_0$ both $\mathrm{MS}_{\mathrm{Tr}}$ and $\mathrm{MS}_{\mathrm{E}}$ estimate $\sigma^2$; under $H_1$ the treatment mean square is larger. We reject $H_0$ when $F_0>F_{a-1,(a-1)(b-1),\alpha}$. The analysis is summarized in the ANOVA table:

| Source | Sum of squares | df | Mean square | $\mathbb{E}[\mathrm{MS}]$ | $F_0$ |
|---|---|---|---|---|---|
| Treatments | $\mathrm{SS}_{\mathrm{Tr}}$ | $a-1$ | $\mathrm{SS}_{\mathrm{Tr}}/(a-1)$ | $\sigma^2+\frac{b\sum\tau_i^2}{a-1}$ | $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}$ |
| Blocks | $\mathrm{SS}_{\mathrm{Blocks}}$ | $b-1$ | $\mathrm{SS}_{\mathrm{Blocks}}/(b-1)$ | $\sigma^2+\frac{a\sum\beta_j^2}{b-1}$ | |
| Error | $\mathrm{SS}_{\mathrm{E}}$ | $(a-1)(b-1)$ | $\mathrm{SS}_{\mathrm{E}}/[(a-1)(b-1)]$ | $\sigma^2$ | |
| Total | $\mathrm{SS}_{\mathrm{T}}$ | $N-1$ | | | |

### 7.3.3. Example: The Vascular Graft Experiment

**Example 7.3.1** A medical device manufacturer produces vascular grafts (artificial veins) by extruding billets of polytetrafluoroethylene resin combined with a lubricant into tubes. Some tubes contain small, hard protrusions on the outer surface, called flicks, which are a cause of rejection. The product engineer suspects that the extrusion pressure affects the occurrence of flicks and intends to investigate four pressures, $8500$, $8700$, $8900$ and $9100\,\mathrm{psi}$. The resin is manufactured in batches, and there may be significant batch-to-batch variation. The response is the yield, the percentage of tubes in a production run that contain no flicks. Each batch of resin is large enough for four production runs, so the engineer runs all four pressures, in random order, on each of six batches: an RCBD with $a=4$ treatments and $b=6$ blocks.

| Pressure (psi) | Batch 1 | 2 | 3 | 4 | 5 | 6 | $y_{i\cdot}$ | $\bar y_{i\cdot}$ |
|---|---|---|---|---|---|---|---|---|
| 8500 | 90.3 | 89.2 | 98.2 | 93.9 | 87.4 | 97.9 | 556.9 | 92.82 |
| 8700 | 92.5 | 89.5 | 90.6 | 94.7 | 87.0 | 95.8 | 550.1 | 91.68 |
| 8900 | 85.5 | 90.8 | 89.6 | 86.2 | 88.0 | 93.4 | 533.5 | 88.92 |
| 9100 | 82.5 | 89.5 | 85.6 | 87.4 | 78.9 | 90.7 | 514.6 | 85.77 |
| $y_{\cdot j}$ | 350.8 | 359.0 | 364.0 | 362.2 | 341.3 | 377.8 | $y_{\cdot\cdot}=2155.1$ | |

With $\sum y_{ij}^2=193999.31$ and $y_{\cdot\cdot}^2/N=2155.1^2/24=193519.00$,

$$
\begin{aligned}
\mathrm{SS}_{\mathrm{T}}&=193999.31-193519.00=480.31,\\
\mathrm{SS}_{\mathrm{Tr}}&=\tfrac16(556.9^2+550.1^2+533.5^2+514.6^2)-193519.00=178.17,\\
\mathrm{SS}_{\mathrm{Blocks}}&=\tfrac14(350.8^2+359.0^2+\cdots+377.8^2)-193519.00=192.25,\\
\mathrm{SS}_{\mathrm{E}}&=480.31-178.17-192.25=109.89 .
\end{aligned}
$$
In R the data frame has the columns `PSI`, `Block` and `Yield`, the first two as factors, and the formula `Yield ~ .` uses all other columns as additive terms:

```r
graft <- data.frame(
  PSI   = factor(rep(c(8500, 8700, 8900, 9100), each = 6)),
  Block = factor(rep(1:6, times = 4)),
  Yield = c(90.3, 89.2, 98.2, 93.9, 87.4, 97.9,
            92.5, 89.5, 90.6, 94.7, 87.0, 95.8,
            85.5, 90.8, 89.6, 86.2, 88.0, 93.4,
            82.5, 89.5, 85.6, 87.4, 78.9, 90.7))
graft.aov <- aov(Yield ~ ., graft)
summary(graft.aov)
```

```text
            Df Sum Sq Mean Sq F value Pr(>F)   
PSI          3    178    59.4    8.11 0.0019 **
Block        5    192    38.5    5.25 0.0055 **
Residuals   15    110     7.3                  
```

The columns are those of the ANOVA table: $\mathrm{MS}_{\mathrm{Tr}}=178.17/3=59.39$, $\mathrm{MS}_{\mathrm{Blocks}}=192.25/5=38.45$, $\mathrm{MS}_{\mathrm{E}}=109.89/15=7.33$, and $F_0=59.39/7.33=8.11$. Since $F_{3,15,0.05}=3.29<8.11$ ($p=0.0019$), we conclude that the extrusion pressure affects the mean yield. The ratio $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}=5.25$ indicates that the resin batches differ considerably, so blocking was worthwhile; Section 7.3.4 explains why this is a descriptive statement rather than a test.

:::

![The vascular graft data. Left: the yield of each batch across the four pressures, with the pressure means; the profiles are shifted up and down by batch but decline with pressure in a similar way. Right: the yields grouped by batch, with the batch means and the grand mean](./plots/graft-data.py)

The plot shows why the design helps. The batch profiles lie at quite different heights, from a mean of $85.3$ for batch 5 to $94.5$ for batch 6, but within each batch the yield tends to fall as the pressure increases. In a completely randomized design these batch differences would be part of the error; in the RCBD they are removed by $\mathrm{SS}_{\mathrm{Blocks}}$ (Section 7.5).

### 7.3.4. Should the Blocks Be Tested?

The blocking factor is by definition of no interest. Should we nevertheless test $H_0\colon\beta_1=\cdots=\beta_b=0$, for example to state that the resin batches differ significantly?

Generally, no. The block factor is included to reduce the error variation due to the nuisance factor, not to test its effect, and the analysis of the treatments is valid whether or not the blocks differ. Comparing $\mathrm{MS}_{\mathrm{Blocks}}$ with $\mathrm{MS}_{\mathrm{E}}$ can be helpful to confirm that the blocking was effective, that is, that the blocks explain variation that would otherwise be part of the experimental error. If the ratio is small, blocking cost $b-1$ error degrees of freedom for nothing, and the design was actually less efficient than a CRD would have been (Section 7.5.2); this is useful when planning the next experiment.

Stronger conclusions about the blocks are generally not possible, whichever way the block factor is viewed:

- as a classification factor (batches, coupons, golfers), its observed levels are not a random sample from a defined population, and they were not assigned at random to anything; a difference between blocks cannot be attributed to any particular cause;
- as an experimental factor, there is an asymmetry between treatments and blocks: the treatments are randomized within blocks and replicated in every block, whereas the blocks themselves are neither randomized nor replicated, so the randomization argument that justifies the $F$-test for treatments does not apply to blocks.

So the ratio $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}$, often printed with a $p$-value by software, is at best an approximate guide to the usefulness of blocking, as already noted in the comparison table of Section 6.4.4 of [3.8.6](/3.8.6). For random blocks, the hypothesis $H_0\colon\sigma_\beta^2=0$ is meaningful (Section 7.6).

### 7.3.5. Residual Analysis

Model adequacy checking is as important for the RCBD as for the one-way design ([3.8.5](/3.8.5)). The residuals $e_{ij}=y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot}$ are plotted against the fitted values, on a **normal probability plot**, and against the treatments and the blocks; a plot against the run order, when it is known, checks the independence assumption. In R the basic plots are

```r
par(mfcol = c(2, 2))
plot(graft.aov)
par(mfcol = c(1, 1))
```

![Residual diagnostics for the vascular graft RCBD: residuals against the fitted values, normal probability plot of the standardized residuals, and residuals by pressure and by batch](./plots/graft-residuals.py)

For the graft data the normality and constant variance assumptions look satisfied: the normal plot is close to a straight line and the spread of the residuals is similar across fitted values. Residuals by factor give additional information about constant variance and possible outliers; there are no clear differences in spread between the pressures or the batches. The residuals of an RCBD sum to zero in every row and every column, so in each block the $a$ residuals have only $a-1$ degrees of freedom; with $a=4$ this leaves little room for patterns within a block. A curved pattern in the plot against the fitted values would suggest a treatment-by-block interaction, which can be checked formally by **Tukey's test for nonadditivity** (Definition 6.4.3 in [3.8.6](/3.8.6)).

### 7.3.6. The Paired t-Test as a Special Case

**Proposition 7.3.1** For $a=2$ treatments, the RCBD $F$-statistic equals the square of the **paired t-test** statistic: with $d_j=y_{1j}-y_{2j}$, $\bar d$ and $s_d$ their mean and standard deviation,

$$
F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}=\left(\frac{\bar d}{s_d/\sqrt b}\right)^2=t_0^2,
$$
and $F_{1,b-1,\alpha}=t_{b-1,\alpha/2}^2$, so the two tests are identical.

**Proof** With $a=2$, $\bar y_{1\cdot}-\bar y_{\cdot\cdot}=\bar d/2$ and $\bar y_{2\cdot}-\bar y_{\cdot\cdot}=-\bar d/2$, so $\mathrm{SS}_{\mathrm{Tr}}=b\,\bar d^2/2$ on one degree of freedom. The block mean is $\bar y_{\cdot j}=(y_{1j}+y_{2j})/2$, so the residuals are $e_{1j}=y_{1j}-\bar y_{\cdot j}-\bar d/2=(d_j-\bar d)/2$ and $e_{2j}=-(d_j-\bar d)/2$. Hence $\mathrm{SS}_{\mathrm{E}}=\frac12\sum_j(d_j-\bar d)^2=\frac{(b-1)s_d^2}{2}$ on $b-1$ degrees of freedom, $\mathrm{MS}_{\mathrm{E}}=s_d^2/2$, and $F_0=b\bar d^2/s_d^2=t_0^2$. $\square$

The discussion "paired or unpaired?" of [3.8.2](/3.8.2) is therefore the discussion "RCBD or CRD?" for two treatments: the pairs are blocks of size two, and the advantage of pairing is exactly the efficiency gain of blocking studied in Section 7.5.

## 7.4. Multiple Comparisons

When the $F$-test rejects $H_0$, the **multiple comparisons** methods of [3.8.4](/3.8.4) apply to the treatment means with two changes: the number of observations per treatment is the number of blocks $b$, and the error mean square and its degrees of freedom are those of the RCBD, $\mathrm{MS}_{\mathrm{E}}$ with $(a-1)(b-1)$ degrees of freedom. For comparing treatments $i$ and $k$,

$$
\mathrm{LSD}=t_{(a-1)(b-1),\alpha/2}\sqrt{\frac{2\mathrm{MS}_{\mathrm{E}}}{b}},\qquad \mathrm{HSD}=q_{a,(a-1)(b-1),\alpha}\sqrt{\frac{\mathrm{MS}_{\mathrm{E}}}{b}},
$$
and the Bonferroni method compares the unadjusted $t$-test $p$-values with $\alpha/m$, $m=\binom a2$. Using the smaller error of the blocked analysis is the point: the comparisons inherit the precision gained by blocking.

For the graft experiment, $\mathrm{MS}_{\mathrm{E}}=7.326$ with $15$ degrees of freedom and $b=6$, so the standard error of a difference is $\sqrt{2\times7.326/6}=1.563$, $\mathrm{LSD}=2.131\times1.563=3.33$ and $\mathrm{HSD}=4.076\sqrt{7.326/6}=4.50$. Tukey's intervals are obtained with

```r
TukeyHSD(graft.aov, "PSI") -> ci
plot(ci, las = 1, cex.axis = .75)
```

which gives the following differences, simultaneous $95\%$ intervals and adjusted $p$-values, together with the unadjusted (LSD) and Bonferroni-adjusted $p$-values computed from the same $\mathrm{MS}_{\mathrm{E}}$:

| Comparison | Difference | Tukey interval | Tukey $p$ | Bonferroni $p$ | LSD $p$ |
|---|---|---|---|---|---|
| 8700 − 8500 | $-1.13$ | $(-5.64,\ 3.37)$ | 0.885 | 1.000 | 0.479 |
| 8900 − 8500 | $-3.90$ | $(-8.40,\ 0.60)$ | 0.101 | 0.148 | 0.025 |
| 9100 − 8500 | $-7.05$ | $(-11.55,\ -2.55)$ | 0.002 | 0.002 | 0.0004 |
| 8900 − 8700 | $-2.77$ | $(-7.27,\ 1.74)$ | 0.325 | 0.582 | 0.097 |
| 9100 − 8700 | $-5.92$ | $(-10.42,\ -1.41)$ | 0.009 | 0.011 | 0.002 |
| 9100 − 8900 | $-3.15$ | $(-7.65,\ 1.35)$ | 0.226 | 0.373 | 0.062 |

Tukey's method and the Bonferroni correction both find that $9100\,\mathrm{psi}$ gives a lower yield than $8500$ and $8700\,\mathrm{psi}$; the LSD, which makes no adjustment for multiplicity, also declares $8900$ different from $8500$. The power increases from Bonferroni to Tukey to LSD, and the protection against false positives decreases in the same order. Since the HSD is larger than the LSD, any pair that Tukey's method declares different is also declared different by the LSD, but not conversely.

Two practical remarks on software. First, `pairwise.t.test(Yield, PSI)` in R uses the pooled standard deviation of a one-way analysis of `Yield` on `PSI`, that is, the error mean square $15.11$ with $20$ degrees of freedom that ignores the blocks. Without adjustment it is therefore not the LSD of the RCBD, and with `p.adjust.method = "bonferroni"` it gives, for example, $p=0.03$ instead of $0.002$ for $9100-8500$. The correct LSD uses the blocked $\mathrm{MS}_{\mathrm{E}}$:

```r
MSE   <- summary(graft.aov)[[1]][3, 3]   # 7.33
df    <- summary(graft.aov)[[1]][3, 1]   # 15
means <- tapply(graft$Yield, graft$PSI, mean)
pairs <- combn(means, 2)
dpair <- pairs[1, ] - pairs[2, ]
t     <- dpair / sqrt(MSE * 2 / 6)
p     <- 2 * (1 - pt(abs(t), df = df))
rbind(combn(4, 2), p)
```

```text
     [,1]    [,2]    [,3]    [,4]    [,5]   [,6]
  1.00000 1.00000 1.00000 2.00000 2.00000 3.0000
  2.00000 3.00000 4.00000 3.00000 4.00000 4.0000
p 0.47946 0.02471 0.00041 0.09696 0.00179 0.0621
```

Here `combn(4, 2)` lists the six pairs of treatment indices. Second, the package `agricolae` performs the LSD directly from the fitted model, so that the correct error term is used automatically:

```r
library(agricolae)
LSD.test(graft.aov, trt = "PSI", group = FALSE, console = TRUE)
```

```text
Study: graft.aov ~ "PSI"

LSD t Test for Yield 

Mean Square Error:  7.32575 

PSI,  means and individual ( 95 %) CI

        Yield      std r      LCL      UCL  Min  Max
8500 92.81667 4.577081 6 90.46148 95.17185 87.4 98.2
8700 91.68333 3.304189 6 89.32815 94.03852 87.0 95.8
8900 88.91667 2.966760 6 86.56148 91.27185 85.5 93.4
9100 85.76667 4.445072 6 83.41148 88.12185 78.9 90.7

Alpha: 0.05 ; DF Error: 15
Critical Value of t: 2.13145 

Comparison between treatments means

            difference pvalue signif.        LCL       UCL
8500 - 8700   1.133333 0.4795         -2.1974047  4.464071
8500 - 8900   3.900000 0.0247       *  0.5692620  7.230738
8500 - 9100   7.050000 0.0004     ***  3.7192620 10.380738
8700 - 8900   2.766667 0.0970       . -0.5640714  6.097405
8700 - 9100   5.916667 0.0018      **  2.5859286  9.247405
8900 - 9100   3.150000 0.0621       . -0.1807380  6.480738
```

The `std` column is the ordinary standard deviation of the six observations at each pressure, which includes the batch variation; the individual intervals `LCL`, `UCL` use $\bar y_{i\cdot}\pm t_{15,0.025}\sqrt{\mathrm{MS}_{\mathrm{E}}/b}=\bar y_{i\cdot}\pm2.131\times1.105$. The comparison intervals are the differences $\pm\mathrm{LSD}=\pm3.33$.

## 7.5. Comparison with the Completely Randomized Design

### 7.5.1. Ignoring the Blocks

Suppose the graft data had been analyzed as if they came from a **completely randomized design**, ignoring the batches:

```text
          Df Sum Sq Mean Sq F value Pr(>F)  
PSI        3  178.2   59.39   3.931 0.0234 *
Residuals 20  302.1   15.11                 
```

The treatment sum of squares is the same, $178.2$, because the treatments are orthogonal to the blocks: every pressure is run once in every batch, so the batch differences affect all pressure means equally. But the error sum of squares now contains the batch variation, $302.1=192.3+109.9$. The error has $20$ degrees of freedom instead of $15$, yet the error mean square is about twice as large, $15.11$ instead of $7.33$, so the $F$-statistic drops from $8.11$ to $3.93$. Here the result is still significant at the $5\%$ level, but with a slightly smaller effect or larger batch variation the pressure effect would have gone undetected. The comparison of Tukey intervals makes the same point:

![Tukey 95% simultaneous intervals for the six pairwise differences of the pressure means, computed from the RCBD error mean square and from the one-way error mean square that ignores the batches; ignoring the blocks makes every interval about 50% wider](./plots/blocking-intervals.py)

### 7.5.2. Relative Efficiency

The CRD and the RCBD differ in how the randomization is carried out: in a CRD the $ab$ units are all assigned at random, in an RCBD the treatments are randomized within each block. The model of the RCBD is a two-way model with one observation per cell, and blocking pays off when the error variance within blocks, $\sigma^2_{\mathrm{RCBD}}$, is smaller than the error variance $\sigma^2_{\mathrm{CRD}}$ among all units. The **relative efficiency** of two designs compares these variances.

**Definition 7.5.1 (Relative Efficiency of an RCBD)** The relative efficiency of a randomized complete block design with respect to a completely randomized design with the same number of observations is

$$
\mathrm{RE}=\frac{\sigma^2_{\mathrm{CRD}}}{\sigma^2_{\mathrm{RCBD}}} .
$$
Since the variance of a treatment comparison is proportional to $\sigma^2/r$ with $r$ replicates per treatment, a CRD needs $\mathrm{RE}$ times as many replicates as the RCBD to estimate the treatment differences with the same precision.

A rough estimate uses the error mean squares of the two analyses of the same data:

$$
\widehat{\mathrm{RE}}=\frac{\mathrm{MS}_{\mathrm{E}}^{\mathrm{CRD}}}{\mathrm{MS}_{\mathrm{E}}^{\mathrm{RCBD}}}=\frac{15.11}{7.33}=2.06 .
$$
A CRD would thus require about $106\%$ more observations to obtain the same precision as the RCBD.

A more careful estimate (Yates, Cochran and Cox) asks what the error variance would have been had the same units been randomized without blocking. In that case the error would contain the block variation and the within-block variation, but the treatment degrees of freedom would also have been error degrees of freedom; replacing them by $\mathrm{MS}_{\mathrm{E}}$,

$$
\hat\sigma^2_{\mathrm{CRD}}=\frac{(b-1)\mathrm{MS}_{\mathrm{Blocks}}+b(a-1)\mathrm{MS}_{\mathrm{E}}}{ab-1}=\frac{5\times38.45+18\times7.326}{23}=14.09 .
$$
Fisher's correction for the different error degrees of freedom of the two designs, $f_{\mathrm{RCBD}}=(a-1)(b-1)$ and $f_{\mathrm{CRD}}=a(b-1)$, multiplies the ratio by

$$
\frac{(f_{\mathrm{RCBD}}+1)(f_{\mathrm{CRD}}+3)}{(f_{\mathrm{RCBD}}+3)(f_{\mathrm{CRD}}+1)}=\frac{16\times23}{18\times21}=0.974,
$$
which accounts for the loss of information from estimating $\sigma^2$ with fewer degrees of freedom. The resulting estimate is $\widehat{\mathrm{RE}}=0.974\times14.09/7.326=1.87$: blocking by batch roughly halved the number of runs needed. The estimate exceeds one exactly when $\mathrm{MS}_{\mathrm{Blocks}}>\mathrm{MS}_{\mathrm{E}}$ (apart from the small correction), which is the precise sense in which blocking is effective when the variation between blocks exceeds the variation within blocks. When the blocks do not differ, the RCBD loses $b-1$ error degrees of freedom and is slightly less efficient than the CRD.

The consequences of not blocking when we should have are thus clear: the unexplained error is larger, and the test of the treatment effect is less powerful.

### 7.5.3. Randomizing the Two Designs in R

The package `agricolae` generates the randomized field book of either design:

```r
library(agricolae)
trt <- levels(graft$PSI)
# Completely randomized design: 6 replicates of each of the 4 pressures
design  <- design.crd(trt, r = rep(6, 4), seed = 777)
book1   <- design$book
# Randomized complete block design: 6 blocks
design2 <- design.rcbd(trt, r = 6, seed = 999)
book2   <- design2$book
design2$sketch
```

```text
     [,1]   [,2]   [,3]   [,4]  
[1,] "8900" "8500" "8700" "9100"
[2,] "8700" "9100" "8900" "8500"
[3,] "9100" "8900" "8700" "8500"
[4,] "9100" "8500" "8700" "8900"
[5,] "9100" "8700" "8500" "8900"
[6,] "8500" "8700" "8900" "9100"
```

Each row of the sketch is a block, and each block contains a random permutation of the four pressures. The field book `book2` lists the same plan with plot numbers ($101,\dots,104$ in block 1, $201,\dots$ in block 2), whereas `book1` lists the $24$ runs of the CRD in a single random sequence, in which a pressure may occur several times in a row and the replicates of a pressure are spread arbitrarily over the batches.

## 7.6. Random Blocks

The blocks of an experiment are often a sample of the possible blocks: the six resin batches are a sample of all the batches the plant will ever produce, and the conclusions about the pressures are meant to hold for future batches. It is then natural to treat the block effects as random, as in the **random-effects model** of [3.8.5](/3.8.5).

**Definition 7.6.1 (RCBD with Random Blocks)** In the RCBD model with random blocks,

$$
Y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij},\qquad \sum_{i=1}^a\tau_i=0,\qquad \beta_j\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma_\beta^2),\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
with the $\beta_j$ independent of the $\varepsilon_{ij}$; the treatments are fixed and the blocks are random.

The moments of the observations are

$$
\mathbb{E}[Y_{ij}]=\mu+\tau_i,\qquad \operatorname{Var}(Y_{ij})=\sigma_\beta^2+\sigma^2,\qquad \operatorname{Cov}(Y_{ij},Y_{i'j})=\sigma_\beta^2\ (i\ne i'),\qquad \operatorname{Cov}(Y_{ij},Y_{i'j'})=0\ (j\ne j').
$$
Observations in the same block are correlated, with **intraclass correlation coefficient** $\rho=\sigma_\beta^2/(\sigma_\beta^2+\sigma^2)$; observations in different blocks are independent. The variances $\sigma_\beta^2$ and $\sigma^2$ are the **variance components**.

**Theorem 7.6.1** In the RCBD with random blocks,

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+\frac{b\sum_{i=1}^a\tau_i^2}{a-1},\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{Blocks}}]=\sigma^2+a\sigma_\beta^2,\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2 .
$$
The statistic for testing no treatment effects is $F_0=\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}\sim F_{a-1,(a-1)(b-1)}$ under $H_0$, exactly the same as with fixed blocks, and $H_0\colon\sigma_\beta^2=0$ is tested by $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}\sim F_{b-1,(a-1)(b-1)}$ under that hypothesis.

**Proof** The treatment means $\bar Y_{i\cdot}=\mu+\tau_i+\bar\beta+\bar\varepsilon_{i\cdot}$ all contain the same random $\bar\beta$, which cancels in $\bar Y_{i\cdot}-\bar Y_{\cdot\cdot}=\tau_i+\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot\cdot}$; so $\mathrm{SS}_{\mathrm{Tr}}$ is the same function of the errors as with fixed blocks. The residuals $\varepsilon_{ij}-\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot j}+\bar\varepsilon_{\cdot\cdot}$ do not involve the $\beta_j$ at all. The block means are $\bar Y_{\cdot j}=\mu+\beta_j+\bar\varepsilon_{\cdot j}$, independent $\mathcal{N}(\mu,\sigma_\beta^2+\sigma^2/a)$, so $\mathrm{SS}_{\mathrm{Blocks}}/(\sigma^2+a\sigma_\beta^2)=a\sum_j(\bar Y_{\cdot j}-\bar Y_{\cdot\cdot})^2/(\sigma^2+a\sigma_\beta^2)\sim\chi^2_{b-1}$, as in Theorem 5.3.1 of [3.8.5](/3.8.5). Conditionally on the $\beta_j$ the three sums of squares are independent with the distributions of Theorem 7.3.1; the conditional distributions of $\mathrm{SS}_{\mathrm{Tr}}$ and $\mathrm{SS}_{\mathrm{E}}$ do not depend on the $\beta_j$, which gives the independence and the null distributions unconditionally. $\square$

Treating the blocks as random therefore does not change the test for a treatment effect. The ANOVA estimator of the block variance component equates $\mathrm{MS}_{\mathrm{Blocks}}$ to its expectation:

$$
\hat\sigma_\beta^2=\frac{\mathrm{MS}_{\mathrm{Blocks}}-\mathrm{MS}_{\mathrm{E}}}{a}=\frac{38.45-7.33}{4}=7.78
$$
for the graft experiment, so the batch-to-batch variance is about as large as the run-to-run variance $\hat\sigma^2=7.33$ within a batch, and $\hat\rho\approx0.5$. The same model is fitted by **restricted maximum likelihood** with the `lme4` package; `0 + PSI` asks for one mean per pressure instead of an intercept and contrasts:

```r
library(lme4)
summary(lmer(Yield ~ 0 + PSI + (1 | Block), data = graft))
```

```text
Linear mixed model fit by REML ['lmerMod']
Formula: Yield ~ 0 + PSI + (1 | Block)
   Data: graft

REML criterion at convergence: 112

Scaled residuals: 
     Min       1Q   Median       3Q      Max 
-1.32253 -0.64269  0.01068  0.54202  1.62882 

Random effects:
 Groups   Name        Variance Std.Dev.
 Block    (Intercept) 7.781    2.789   
 Residual             7.326    2.707   
Number of obs: 24, groups:  Block, 6

Fixed effects:
        Estimate Std. Error t value
PSI8500   92.817      1.587   58.49
PSI8700   91.683      1.587   57.78
PSI8900   88.917      1.587   56.04
PSI9100   85.767      1.587   54.05
```

Because the design is balanced and $\mathrm{MS}_{\mathrm{Blocks}}>\mathrm{MS}_{\mathrm{E}}$, the REML estimates $\hat\sigma_\beta^2=7.781$ and $\hat\sigma^2=7.326$ coincide with the ANOVA estimates. The fixed-effect estimates are the pressure means. Their standard error, $1.587=\sqrt{(7.781+7.326)/6}$, is $\sqrt{\operatorname{Var}(\bar Y_{i\cdot})}=\sqrt{(\sigma_\beta^2+\sigma^2)/b}$, larger than the $\sqrt{7.326/6}=1.105$ of the fixed-block analysis: a mean yield at $8500\,\mathrm{psi}$ for the population of batches is uncertain also because only six batches were sampled. Differences of pressure means, in which $\bar\beta$ cancels, have the same standard error $\sqrt{2\sigma^2/b}=1.563$ in both models, so the comparisons of Section 7.4 are unchanged.

The ANOVA-based approach to random blocks has the advantages of explicit formulas and a clear view of the mechanism. Its disadvantages are that $\hat\sigma_\beta^2$ can be negative (whenever $\mathrm{MS}_{\mathrm{Blocks}}<\mathrm{MS}_{\mathrm{E}}$); that for unbalanced designs and several factors the ANOVA decomposition is not unique (it depends on the order of the factors), the sums of squares are not orthogonal and the exact distribution theory fails; and that the formulas become complicated as factors are added. The alternative is likelihood-based estimation, maximum likelihood or REML, which is what `lmer` does.

## 7.7. Missing Values

### 7.7.1. Why a Missing Value Is a Problem

Occasionally an observation in a randomized block design is lost: a test specimen breaks, a run is spoiled, a plot is flooded. A **missing value** destroys the defining feature of the RCBD that every treatment occurs in every block. The treatments are no longer orthogonal to the blocks, and the problem is not just replacing $b$ by the number of observations $n_i$ of each treatment: the identity

$$
\sum_{i,j}(y_{ij}-\bar y_{\cdot\cdot})^2=b\sum_i(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2+a\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2+\sum_{i,j}(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2
$$
no longer holds, whatever the sums are taken over. A tiny example with $a=2$ treatments and $b=3$ blocks, and $y_{22}$ missing, shows this:

| | Block 1 | Block 2 | Block 3 | $\bar y_{i\cdot}$ |
|---|---|---|---|---|
| Treatment 1 | 1 | 3 | 2 | 2 |
| Treatment 2 | 2 | – | 2 | 2 |
| $\bar y_{\cdot j}$ | 1.5 | 3 | 2 | $\bar y_{\cdot\cdot}=2$ |

Here $\mathrm{SS}_{\mathrm{T}}=1+1+0+0+0=2$, while the formulas give $\mathrm{SS}_{\mathrm{Tr}}=0$, $\mathrm{SS}_{\mathrm{Blocks}}=2[(1.5-2)^2+(3-2)^2+0]=2.5$ and $\mathrm{SS}_{\mathrm{E}}=0.25+0+0+0.25+0=0.5$, whose sum is $3\ne2$. The pattern of block 2, which has only the high observation of treatment 1, makes the treatment means and the block means interdependent.

There are two remedies. The exact analysis fits the model to the incomplete data by least squares, as an unbalanced two-way model. The classical approximate analysis estimates the missing value and then analyzes the completed data as an RCBD.

### 7.7.2. Estimating One Missing Value

**Proposition 7.7.1** Suppose the observation $y_{ij}$ is missing, and let $y'_{i\cdot}$, $y'_{\cdot j}$ and $y'_{\cdot\cdot}$ be the totals of treatment $i$, of block $j$ and of all observations without it. The value $x$ that minimizes the error sum of squares $\mathrm{SS}_{\mathrm{E}}(x)$ of the completed data is

$$
x=\frac{a\,y'_{i\cdot}+b\,y'_{\cdot j}-y'_{\cdot\cdot}}{(a-1)(b-1)} .
$$
It is the fitted value of the cell $(i,j)$ in the least squares fit of the RCBD model to the $ab-1$ available observations, and $\mathrm{SS}_{\mathrm{E}}(x)$ equals the residual sum of squares of that fit.

**Proof** With $x$ in the cell $(i,j)$, write $\mathrm{SS}_{\mathrm{E}}(x)=\min_{\mu,\tau,\beta}Q(x;\mu,\tau,\beta)$, where $Q$ is the sum of squared deviations over all $ab$ cells. Minimizing over $x$ as well, $\min_x\mathrm{SS}_{\mathrm{E}}(x)=\min_{\mu,\tau,\beta}\min_xQ$. For fixed parameters, the only term of $Q$ involving $x$ is $(x-\mu-\tau_i-\beta_j)^2$, which is minimized, and made zero, by $x=\mu+\tau_i+\beta_j$; what remains is the sum of squares over the $ab-1$ available cells. So the joint minimum is attained at the least squares fit to the incomplete data, with $x$ equal to its fitted value, and the minimal $\mathrm{SS}_{\mathrm{E}}$ is the residual sum of squares of that fit. Equivalently, the residual of the imputed cell in the completed analysis is zero, $x=\bar y_{i\cdot}+\bar y_{\cdot j}-\bar y_{\cdot\cdot}$ with the means computed from the completed data:

$$
x=\frac{y'_{i\cdot}+x}{b}+\frac{y'_{\cdot j}+x}{a}-\frac{y'_{\cdot\cdot}+x}{ab}.
$$
Multiplying by $ab$ gives $abx=a(y'_{i\cdot}+x)+b(y'_{\cdot j}+x)-(y'_{\cdot\cdot}+x)$, that is, $(ab-a-b+1)\,x=a\,y'_{i\cdot}+b\,y'_{\cdot j}-y'_{\cdot\cdot}$, and $ab-a-b+1=(a-1)(b-1)$. $\square$

The same formula follows by differentiating $\mathrm{SS}_{\mathrm{E}}(x)=\sum_{i,j}(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2$ directly and solving $\mathrm{d}\,\mathrm{SS}_{\mathrm{E}}/\mathrm{d}x=0$, which is the classical derivation.

**Example 7.7.1** Suppose the observation for $8700\,\mathrm{psi}$ in batch 4 of the graft experiment, $y_{24}=94.7$, had been lost. Then $y'_{2\cdot}=550.1-94.7=455.4$, $y'_{\cdot4}=362.2-94.7=267.5$ and $y'_{\cdot\cdot}=2155.1-94.7=2060.4$, and

$$
x=\frac{4\times455.4+6\times267.5-2060.4}{3\times5}=\frac{1366.2}{15}=91.08 .
$$
The approximate method replaces the missing point by its predicted ("imputed") value from the additive model, and R computes it with `predict`:

```r
vas <- graft
vas[10, 3] <- NA                         # row 10: PSI 8700, Block 4
p <- predict(aov(Yield ~ PSI + Block, vas), newdata = vas[10, ])   # 91.08
vas[10, 3] <- p                          # just replace it
summary(aov(Yield ~ PSI + Block, vas))
```

```text
          Df Sum Sq Mean Sq F value  Pr(>F)   
PSI        3  166.1   55.38   8.169 0.00185 **
Block      5  189.5   37.90   5.591 0.00419 **
Residuals 15  101.7    6.78                   
```

:::

This table needs two corrections before it is used.

1. The error degrees of freedom must be reduced by one for each missing observation: the imputed value contributes nothing to the error, because its residual is zero. The error has $14$ degrees of freedom and $\mathrm{MS}_{\mathrm{E}}=101.7/14=7.26$, not $6.78$.
2. The treatment sum of squares of the completed data is biased upward. The exact sum of squares for treatments adjusted for blocks is smaller by

   $$
   \frac{\bigl[y'_{\cdot j}-(a-1)x\bigr]^2}{a(a-1)}=\frac{(267.5-3\times91.08)^2}{12}=2.75,
   $$
   that is, $166.1-2.7=163.4$, and the exact test is $F_0=(163.4/3)/7.26=7.50$ ($p=0.0031$).

The bias comes from the reduced model. The adjusted treatment sum of squares is the difference between the residual sums of squares of the model with blocks only and of the full model. The second is $\mathrm{SS}_{\mathrm{E}}(x)$ by Proposition 7.7.1. In the first, the imputed $x$ is not the optimal value: under the blocks-only model the best value would be the mean $y'_{\cdot j}/(a-1)$ of the other observations in block $j$, and the residual sum of squares of a group of $a$ observations increases by $\frac{a-1}{a}\bigl(x-y'_{\cdot j}/(a-1)\bigr)^2$ when one of them moves away from the mean of the others. This increase, which is the displayed bias, is added to the treatment sum of squares.

Compared with the complete data ($\mathrm{SS}_{\mathrm{E}}=110$ with $15$ degrees of freedom), the error sum of squares of the completed data is smaller, $101.7$: the imputed value fits the model perfectly, whereas the true observation has a residual. This is always so, since $x$ minimizes $\mathrm{SS}_{\mathrm{E}}$ over all possible values of the missing observation.

### 7.7.3. Several Missing Values and the Exact Analysis

With several missing values, each is estimated by the formula of Proposition 7.7.1, with the current estimates of the others inserted, and the process is iterated until the estimates converge; the error degrees of freedom are reduced by the number of missing values. This iteration of fitting and imputing is an early instance of the **EM algorithm**, and it converges to the least squares fit to the incomplete data.

Today the exact least squares analysis is simply computed. R drops the rows with `NA` and fits the unbalanced additive model; the ANOVA table then lists **sequential sums of squares**, in which each term is adjusted only for the terms before it, so the order of the terms matters:

```r
vas[10, 3] <- NA
summary(aov(Yield ~ PSI + Block, vas))
summary(aov(Yield ~ Block + PSI, vas))
```

```text
            Df Sum Sq Mean Sq F value  Pr(>F)   
PSI          3  164.0   54.67   7.525 0.00308 **
Block        5  189.5   37.90   5.218 0.00653 **
Residuals   14  101.7    7.26                   
1 observation deleted due to missingness

            Df Sum Sq Mean Sq F value  Pr(>F)   
Block        5  190.1   38.02   5.235 0.00645 **
PSI          3  163.4   54.47   7.498 0.00313 **
Residuals   14  101.7    7.26                   
1 observation deleted due to missingness
```

The residual line is the same in both orders and agrees with the corrected approximate analysis: $\mathrm{SS}_{\mathrm{E}}=101.7$ with $14$ degrees of freedom. In the first table, `PSI` is not adjusted for the blocks: its sum of squares $164.0$ compares the pressure means of the incomplete data, in which the $8700\,\mathrm{psi}$ mean lacks batch 4. In the second, `PSI` comes after `Block` and its sum of squares $163.4$ measures the pressure effect after the batch effects have been removed, which is the question of the experiment; it agrees with the corrected value of Example 7.7.1, and $F_0=7.498$. For testing treatments in a block design with missing data, the block term must therefore be entered first, `Yield ~ Block + PSI`.

## 7.8. Generalized Complete Block Designs

### 7.8.1. Blocks Larger Than the Number of Treatments

Why should the block size equal the number of treatments? The reason is homogeneity: the larger a group of units, the more likely it is to be heterogeneous, and a block is useful only if the units within it are similar. But when larger blocks do not increase the variability within a block, there is no need to restrict each block to one unit per treatment, and each treatment can be replicated within each block.

**Definition 7.8.1 (Generalized Complete Block Design)** A **generalized complete block design** (GCBD) with $a$ treatments and $b$ blocks has blocks of $an$ experimental units, $n\ge2$; each treatment is applied to $n$ units in every block, and the treatments are randomized within each block. Its model is

$$
Y_{ijk}=\mu+\tau_i+\beta_j+\gamma_{ij}+\varepsilon_{ijk},\qquad i=1,\dots,a,\quad j=1,\dots,b,\quad k=1,\dots,n,
$$
where $\gamma_{ij}$ is the block-by-treatment interaction and $\varepsilon_{ijk}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$.

Unlike the RCBD, the GCBD has replicates within each treatment-block cell, so the interaction between treatments and blocks can be estimated and tested, and the additivity assumption of the RCBD is no longer needed. The analysis is a two-way ANOVA as in [3.8.6](/3.8.6), with $a-1$, $b-1$, $(a-1)(b-1)$ and $ab(n-1)$ degrees of freedom for treatments, blocks, interaction and error.

**Example 7.8.1** An experiment reported in a golf magazine (2006) aimed to recommend to all readers what tee height to use to drive a golf ball farthest. The treatment factor was the tee height, with three levels:

| Level | Tee height |
|---|---|
| 1 | entire ball below the crown of the driver club-face |
| 2 | half the ball above the crown |
| 3 | bottom of the ball at the top of the club-face |

The response was the distance the ball traveled after the hit. Since golfers differ greatly in their ability to drive, the trials were blocked by golfer, and the order of each golfer's hits was randomized. Hitting more than three balls would not fatigue a golfer and cause more variability in his driving distance, so there was no need to restrict each golfer to three hits. Nine golfers each hit five balls from each of the three tee heights, $15$ balls in total, in a random order: a GCBD with $a=3$ treatments, $b=9$ blocks and $n=5$ replicates, $N=135$ drives.

:::

### 7.8.2. The Block-by-Treatment Interaction as the Error Term

If the interaction between golfer and tee height were significant, the optimal tee height could differ from golfer to golfer. The golfers in the study are only a sample of golfers, so we could not recommend an optimal tee height to the population of all readers on the basis of the particular golfers' preferences. To generalize the conclusions about treatment effects over all experimental units, the average treatment effects should be larger than the differences in treatment effects among blocks. The variation of the treatment effects from block to block, measured by the block-by-treatment interaction, is therefore the correct yardstick, that is, the correct error term for testing the treatment effects:

$$
\text{RCBD: } F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\qquad\Longrightarrow\qquad \text{GCBD: } F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{Tr}\times\mathrm{B}}} .
$$
Section 7.8.4 shows that this is what the expected mean squares of a mixed model require. In the RCBD the two coincide: with one observation per cell, the error of the additive model is the block-by-treatment interaction.

In R, the error strata of `aov` give this test. The data are read from a file in which the first row contains the golfer identifiers and the first column the tee heights:

```r
f <- file.choose()   # choose "golf.txt"
y <- scan(f)
y <- matrix(y, byrow = T, ncol = 10)
golf <- data.frame(cdistance = as.vector(y[-1, -1]),
                   teehgt = as.factor(rep(y[-1, 1], times = 9)),
                   id = as.factor(rep(y[1, -1], each = 15)))
# Test the significance of teehgt
mod1 <- aov(cdistance ~ teehgt + Error(id/teehgt), data = golf)
summary(mod1)
```

```text
Error: id
          Df Sum Sq Mean Sq F value Pr(>F)
Residuals  8 124741   15593               

Error: id:teehgt
          Df Sum Sq Mean Sq F value Pr(>F)  
teehgt     2   1724   862.0   5.854 0.0124 *
Residuals 16   2356   147.3                 
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Error: Within
           Df Sum Sq Mean Sq F value Pr(>F)
Residuals 108   7341   67.97               
```

The term `Error(id/teehgt)` declares two error strata above the individual drives: golfers (`id`), and tee heights within golfers (`id:teehgt`). Each source of variation is tested against the residual of its own stratum. The tee height effect, which varies within golfers, is tested against the golfer-by-tee-height mean square: $F_0=862.0/147.3=5.854$ with $2$ and $16$ degrees of freedom, $p=0.0124$. The `Within` stratum contains the variation among the five drives of a golfer at one tee height, $\mathrm{MS}_{\mathrm{E}}=67.97$ with $9\times3\times4=108$ degrees of freedom.

An equivalent and simpler method averages the replicates. Create a new response, the mean of each block-by-treatment cell, and fit the ordinary RCBD model to these cell means:

```r
cellmeans <- tapply(golf$cdistance, list(golf$id, golf$teehgt), mean)
dim(cellmeans) <- NULL   # same as as.vector
teehgt <- factor(rep(1:3, each = 9))
id     <- factor(rep(1:9, 3))
mod2 <- aov(cellmeans ~ id + teehgt)
summary(mod2)
```

```text
          Df Sum Sq Mean Sq F value   Pr(>F)    
id         8  24948  3118.5 105.888 2.19e-12 ***
teehgt     2    345   172.4   5.854   0.0124 *  
Residuals 16    471    29.5                     
```

The cell means are

| Golfer | Tee 1 | Tee 2 | Tee 3 |
|---|---|---|---|
| 1 | 143.18 | 141.64 | 147.40 |
| 2 | 173.18 | 176.14 | 188.04 |
| 3 | 141.64 | 147.40 | 143.18 |
| 4 | 176.10 | 178.04 | 175.72 |
| 5 | 204.68 | 213.20 | 226.26 |
| 6 | 137.10 | 148.56 | 146.70 |
| 7 | 171.18 | 166.46 | 173.14 |
| 8 | 168.88 | 187.38 | 176.06 |
| 9 | 227.18 | 241.72 | 242.04 |

Every sum of squares of this RCBD is the corresponding sum of squares of the GCBD divided by $n=5$ ($24948=124741/5$, $345=1724/5$, $471=2356/5$), so the $F$-ratio and the $p$-value of the tee heights are exactly those of the error-strata analysis. Averaging the replicates loses nothing for the treatment test, because the within-cell variation does not enter it.

![Golf experiment: the mean driving distance of each golfer at the three tee heights. Left: the golfers differ enormously in level; right: after subtracting each golfer's mean, the profiles still differ, which is the golfer-by-tee-height interaction against which the tee heights are tested](./plots/golf-cell-means.py)

The mean distances for the tee heights and Tukey's comparisons, based on the cell-means model with $\mathrm{MS}=29.5$ on $16$ degrees of freedom, are

```r
model.tables(mod2, type = "means")$tables$teehgt
TukeyHSD(mod2, "teehgt")
```

```text
teehgt
       1        2        3 
171.4578 177.8378 179.8378 

  Tukey multiple comparisons of means
    95% family-wise confidence level

Fit: aov(formula = cellmeans ~ id + teehgt)

$teehgt
    diff        lwr       upr     p adj
2-1 6.38 -0.2211713 12.981171 0.0589879
3-1 8.38  1.7788287 14.981171 0.0124851
3-2 2.00 -4.6011713  8.601171 0.7192035
```

Height 3 drives significantly farther than height 1, height 2 is borderline better than height 1, and heights 2 and 3 do not differ. The recommendation to the readers of the article was to tee the ball up so that at least half of it is above the crown of the driver club-face, in order to maximize the driving distance.

### 7.8.3. Pool or Not to Pool

If the interaction is negligible, the additive model

$$
Y_{ijk}=\mu+\tau_i+\beta_j+\varepsilon_{ijk}
$$
gives a more powerful test of the treatment effects than the test that uses the interaction mean square as the denominator. The interaction mean square then estimates the same experimental error as the error mean square, and pooling the two increases the error degrees of freedom and hence the power of the $F$-test. The usual "pool or not to pool" procedure decides between the two:

1. Test the interaction by $F=\mathrm{MS}_{\mathrm{Tr}\times\mathrm{B}}/\mathrm{MS}_{\mathrm{E}}$ at a higher significance level than usual, typically $\alpha=0.25$, so that pooling happens only when the evidence for interaction is weak.
2. If the interaction is significant, use the interaction mean square as the denominator of the $F$-test for treatments.
3. If it is not significant, fit the additive model and use its default $F$-test, with the pooled error mean square $(\mathrm{SS}_{\mathrm{Tr}\times\mathrm{B}}+\mathrm{SS}_{\mathrm{E}})/[(a-1)(b-1)+ab(n-1)]$.

For the golf experiment, the full two-way ANOVA gives

```r
mod3 <- aov(cdistance ~ id * teehgt, data = golf)
summary(mod3)
```

```text
           Df Sum Sq Mean Sq F value   Pr(>F)    
id          8 124741   15593 229.406  < 2e-16 ***
teehgt      2   1724     862  12.682 1.13e-05 ***
id:teehgt  16   2356     147   2.166   0.0102 *  
Residuals 108   7341      68                     
```

The interaction test has $p=0.0102<0.25$, so the additive model should not be fit, and there is no more powerful $F$-test for the tee heights than the one using the interaction term, $F_0=5.854$. The `teehgt` line of this table, $F=862/67.97=12.68$, uses the within-cell error as the denominator; that would be the right test only if the golfers were the sole golfers of interest (fixed blocks) and the conclusions were restricted to them, which is not the purpose of the study.

The preliminary test makes the final test conditional on its outcome, so its overall significance level is not exactly $\alpha$; the high level $0.25$ for the preliminary test keeps the risk of pooling a real interaction small.

### 7.8.4. The Mixed Model

The tee height can be considered a fixed effect, since the object of the experiment was to determine whether the tee heights cause any difference in driving distance. The golfer, the block factor, can be considered a random effect: there was no interest in comparing the specific golfers used in the experiment, who were a sample of representative golfers. The interaction of golfer and tee height should then also be considered random, since the interaction between a random and a fixed effect is by definition a random effect. Models of this kind have a name.

**Definition 7.8.2 (Mixed Model)** A **mixed model** is a linear model that contains both fixed effects and random effects. In the two-factor mixed model with a **fixed factor** $A$ ($a$ levels), a **random factor** $B$ ($b$ levels) and $n$ replicates,

$$
Y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\varepsilon_{ijk},\qquad \sum_{i=1}^a\tau_i=0,\qquad \beta_j\sim\mathcal{N}(0,\sigma_\beta^2),\quad (\tau\beta)_{ij}\sim\mathcal{N}(0,\sigma_{\tau\beta}^2),\quad \varepsilon_{ijk}\sim\mathcal{N}(0,\sigma^2),
$$
with all random terms mutually independent (in the restricted version of the model, the interaction effects of a block are constrained to sum to zero over $i$, see below). Then $\mathbb{E}[Y_{ijk}]=\mu+\tau_i$ and $\operatorname{Var}(Y_{ijk})=\sigma_\beta^2+\sigma_{\tau\beta}^2+\sigma^2$.

For the golf experiment, $a=3$, $b=9$ and $n=5$, and the expected mean squares are

| Source | df | $\mathbb{E}[\mathrm{MS}]$ | Golf |
|---|---|---|---|
| $A$: tee height ($\tau_i$) | $a-1$ | $\sigma^2+n\sigma_{\tau\beta}^2+\dfrac{bn\sum_i\tau_i^2}{a-1}$ | $\sigma^2+5\sigma_{\tau\beta}^2+\dfrac{9\times5\sum_i\tau_i^2}{2}$, df $2$ |
| $B$: golfer ($\beta_j$) | $b-1$ | $\sigma^2+an\sigma_\beta^2$ | $\sigma^2+3\times5\,\sigma_\beta^2$, df $8$ |
| $AB$: tee height × golfer ($(\tau\beta)_{ij}$) | $(a-1)(b-1)$ | $\sigma^2+n\sigma_{\tau\beta}^2$ | $\sigma^2+5\sigma_{\tau\beta}^2$, df $16$ |
| Error ($\varepsilon_{ijk}$, replicates) | $ab(n-1)$ | $\sigma^2$ | $\sigma^2$, df $(5-1)\times3\times9=108$ |

The rule for constructing an $F$-test is to choose as the denominator the mean square whose expectation equals that of the numerator when the null hypothesis holds. Under $H_0\colon\tau_1=\tau_2=\tau_3=0$ the expectation of $\mathrm{MS}_A$ reduces to $\sigma^2+n\sigma_{\tau\beta}^2$, the expectation of $\mathrm{MS}_{AB}$, so

$$
F_0=\frac{\mathrm{MS}_A}{\mathrm{MS}_{AB}}\ \overset{H_0}{\sim}\ F_{a-1,(a-1)(b-1)},
$$
which is the test of Section 7.8.2. The interaction variance component is tested by $\mathrm{MS}_{AB}/\mathrm{MS}_{\mathrm{E}}$ and estimated by $\hat\sigma_{\tau\beta}^2=(\mathrm{MS}_{AB}-\mathrm{MS}_{\mathrm{E}})/n=(147.3-67.97)/5=15.9$; the block component is estimated by $\hat\sigma_\beta^2=(\mathrm{MS}_B-\mathrm{MS}_{\mathrm{E}})/(an)=(15593-67.97)/15=1035$. The golfers' long-run distances thus vary with a standard deviation of about $32$ distance units, the golfer-specific response to the tee height with a standard deviation of about $4$, and single drives with a standard deviation of about $8$.

The expected mean square of $B$ depends on a convention. The table is that of the restricted mixed model, in which the interaction effects satisfy $\sum_i(\tau\beta)_{ij}=0$ for each block $j$ (with $\operatorname{Var}((\tau\beta)_{ij})=\frac{a-1}{a}\sigma_{\tau\beta}^2$, so that the $AB$ line reads as shown); the hypothesis $H_0\colon\sigma_\beta^2=0$ is then tested by $F_0=\mathrm{MS}_B/\mathrm{MS}_{\mathrm{E}}$. In the unrestricted mixed model of Definition 7.8.2 without the constraint, $\mathbb{E}[\mathrm{MS}_B]=\sigma^2+n\sigma_{\tau\beta}^2+an\sigma_\beta^2$ and the test of $\sigma_\beta^2=0$ is $\mathrm{MS}_B/\mathrm{MS}_{AB}$. The two models give the same test of the fixed effects; they differ only in what the block variance component means (in the restricted model, $\sigma_\beta^2$ is the variance of the block means averaged over the treatments; in the unrestricted model it excludes the interaction part). The `Error(id/teehgt)` analysis in R corresponds to the unrestricted model, and `lmer(cdistance ~ teehgt + (1 | id) + (1 | id:teehgt))` fits it by REML.

For the additive model with random blocks of Section 7.6 ($n=1$, no interaction term), $\mathbb{E}[\mathrm{MS}_{\mathrm{Blocks}}]=\sigma^2+a\sigma_\beta^2$ and the test of $\sigma_\beta^2=0$ is $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}$ (Theorem 7.6.1). Mixed models with several random factors, their estimation by REML and approximate $F$-tests are taken up in later chapters.

## Summary {#summary}

- Blocking removes the variation due to a known, controllable nuisance factor; known but uncontrollable covariates are handled by analysis of covariance, unknown ones by randomization (Section 7.1.2). Block what you can, randomize what you cannot.
- The RCBD (Definition 7.2.1) runs every treatment once in every block and randomizes within blocks. Model $Y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij}$ (Definition 7.2.2), additive by design; estimates $\hat\tau_i=\bar y_{i\cdot}-\bar y_{\cdot\cdot}$, $\hat\beta_j=\bar y_{\cdot j}-\bar y_{\cdot\cdot}$ (Proposition 7.2.1).
- The ANOVA of the RCBD (Theorem 7.3.1):

  | Source | SS | df | $\mathbb{E}[\mathrm{MS}]$ (fixed blocks) | $\mathbb{E}[\mathrm{MS}]$ (random blocks) | $F_0$ |
  |---|---|---|---|---|---|
  | Treatments | $b\sum_i(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2$ | $a-1$ | $\sigma^2+\frac{b\sum\tau_i^2}{a-1}$ | $\sigma^2+\frac{b\sum\tau_i^2}{a-1}$ | $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}$ |
  | Blocks | $a\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2$ | $b-1$ | $\sigma^2+\frac{a\sum\beta_j^2}{b-1}$ | $\sigma^2+a\sigma_\beta^2$ | (not a strict test) |
  | Error | $\sum_{i,j}(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2$ | $(a-1)(b-1)$ | $\sigma^2$ | $\sigma^2$ | |
  | Total | $\sum_{i,j}(y_{ij}-\bar y_{\cdot\cdot})^2$ | $ab-1$ | | | |

- The block $F$-ratio only indicates whether blocking was effective (Section 7.3.4); residual analysis is still required (Section 7.3.5). For $a=2$ the RCBD is the paired design and $F_0=t_0^2$ (Proposition 7.3.1).
- Multiple comparisons use $\mathrm{MS}_{\mathrm{E}}$ with $(a-1)(b-1)$ df and $b$ observations per mean: $\mathrm{LSD}=t_{(a-1)(b-1),\alpha/2}\sqrt{2\mathrm{MS}_{\mathrm{E}}/b}$, $\mathrm{HSD}=q_{a,(a-1)(b-1),\alpha}\sqrt{\mathrm{MS}_{\mathrm{E}}/b}$. A one-way `pairwise.t.test` ignores the blocks.
- CRD versus RCBD: same treatment SS; the CRD error absorbs the block SS. Relative efficiency (Definition 7.5.1) $\approx\mathrm{MS}_{\mathrm{E}}^{\mathrm{CRD}}/\mathrm{MS}_{\mathrm{E}}^{\mathrm{RCBD}}$, more precisely $\hat\sigma^2_{\mathrm{CRD}}=[(b-1)\mathrm{MS}_{\mathrm{Blocks}}+b(a-1)\mathrm{MS}_{\mathrm{E}}]/(ab-1)$ with Fisher's df correction; graft: $2.06$ and $1.87$.
- Random blocks (Definition 7.6.1, Theorem 7.6.1): the same $F$-test for treatments; $\hat\sigma_\beta^2=(\mathrm{MS}_{\mathrm{Blocks}}-\mathrm{MS}_{\mathrm{E}})/a$; standard errors of treatment means include $\sigma_\beta^2$, those of differences do not.
- One missing value: $x=\dfrac{a\,y'_{i\cdot}+b\,y'_{\cdot j}-y'_{\cdot\cdot}}{(a-1)(b-1)}$ (Proposition 7.7.1); subtract one error df per missing value; the treatment SS of the completed data is biased upward by $[y'_{\cdot j}-(a-1)x]^2/[a(a-1)]$. Exact analysis: `Yield ~ Block + PSI` (blocks first).
- GCBD (Definition 7.8.1): $n$ replicates of each treatment per block; with random blocks the treatment test is $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{Tr}\times\mathrm{B}}$ (`Error(block/trt)`, or the RCBD on cell means); pool the interaction into the error only if its preliminary test at $\alpha=0.25$ is not significant.
- Mixed model (Definition 7.8.2), $A$ fixed, $B$ random: $\mathbb{E}[\mathrm{MS}_A]=\sigma^2+n\sigma_{\tau\beta}^2+bn\sum\tau_i^2/(a-1)$, $\mathbb{E}[\mathrm{MS}_{AB}]=\sigma^2+n\sigma_{\tau\beta}^2$, $\mathbb{E}[\mathrm{MS}_B]=\sigma^2+an\sigma_\beta^2$ (restricted) or $\sigma^2+n\sigma_{\tau\beta}^2+an\sigma_\beta^2$ (unrestricted); the denominator of an $F$-test is the mean square with the same expectation under $H_0$.

## Questions

1. In a field trial, the response is the crop yield and the factor of interest is the variety; the field is divided into strips of land that differ in fertility, and each strip is divided into as many plots as there are varieties. Which design and analysis are appropriate: a CRD with simple linear regression, a CRD with a one-way ANOVA, or a design that takes the strips into account?

   **Answer** The strips are blocks (a nuisance factor): randomize the varieties within each strip, which is an RCBD, and analyze with the two-way additive model with varieties and strips (a two-way ANOVA without interaction). A CRD with a one-way ANOVA would be valid but would leave the strip differences in the error; simple linear regression is inappropriate for a qualitative factor.

2. For the vascular graft experiment, describe the experiment as a CRD and as an RCBD (how many factors, is there interaction, how are the runs randomized), and say which you would choose.

   **Answer** CRD: one factor, pressure, with $6$ replicates; the $24$ runs are assigned at random to the material regardless of batch, and the batch differences become part of the error. RCBD: one treatment factor and one block factor, batch; each batch receives all four pressures in random order, and the model is the two-factor additive model, assuming no pressure-by-batch interaction. Since the batches are known to vary and each batch suffices for four runs, the RCBD is preferable; the data confirm it ($\widehat{\mathrm{RE}}\approx1.9$ to $2.1$).

3. A nuisance factor is by definition of no interest. Do we need to test its effect, for example whether the batches differ significantly?

   **Answer** Generally no: the block factor is in the model to reduce the error, and the treatment test is valid either way. A formal test of the blocks is not justified, because the blocks are neither randomized nor replicated. Comparing $\mathrm{MS}_{\mathrm{Blocks}}$ with $\mathrm{MS}_{\mathrm{E}}$ is nevertheless useful as a check of whether the blocking was necessary and effective, which matters for planning future experiments.

4. If Fisher's LSD instead of Tukey's method is used for the pairwise comparisons in the graft experiment, how can the conclusions differ?

   **Answer** Every pair rejected by Tukey's method is also rejected by the LSD, because the HSD $4.50$ exceeds the LSD $3.33$; but a pair not rejected by Tukey may still be rejected by the LSD. This happens for $8900-8500$ (difference $3.90$, between $3.33$ and $4.50$).

5. `pairwise.t.test` also uses a pooled standard deviation. Is `with(graft, pairwise.t.test(Yield, PSI, p.adjust.method = "none"))` Fisher's LSD for the RCBD?

   **Answer** No. It pools the variances of the four pressure groups as in a one-way analysis, so its error mean square is $15.11$ with $20$ degrees of freedom, which includes the batch variation. The LSD of the RCBD uses $\mathrm{MS}_{\mathrm{E}}=7.33$ with $15$ degrees of freedom, as in the code of Section 7.4 or `agricolae::LSD.test` applied to the fitted RCBD model.

6. With random blocks, which hypothesis expresses "blocking is unnecessary", and how is it tested in the additive model $y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij}$: $H_0\colon\beta_1=\cdots=\beta_b=0$ or $H_0\colon\sigma_\beta^2=0$?

   **Answer** $H_0\colon\sigma_\beta^2=0$; with random blocks the individual $\beta_j$ are random variables, not parameters. By Theorem 7.6.1, $\mathbb{E}[\mathrm{MS}_{\mathrm{Blocks}}]=\sigma^2+a\sigma_\beta^2$ and $\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2$, so the test statistic is $F_0=\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}\sim F_{b-1,(a-1)(b-1)}$ under $H_0$. For the graft data $F_0=5.25$, $p=0.0055$.

7. A missing value in an RCBD is replaced by the least squares estimate of Proposition 7.7.1 and the completed data are analyzed. Compared with the error sum of squares that the true (unknown) observation would have given, is the error sum of squares of the completed data generally smaller, larger, or either?

   **Answer** Smaller (or at most equal). The imputed $x$ minimizes $\mathrm{SS}_{\mathrm{E}}$ over all values that could be placed in the cell, and the true observation is one of these values; equality holds only if the true observation happens to equal its fitted value. For the graft data: $101.7$ against $110$.

8. With a missing observation, should the treatments be tested with `summary(aov(Yield ~ PSI + Block, vas))` or with `summary(aov(Yield ~ Block + PSI, vas))`?

   **Answer** With the second. The sequential sum of squares of a term is adjusted only for the terms before it, and the treatment comparison must be adjusted for the blocks, since the blocks are no longer balanced over the treatments. The residual line is the same in both.

9. Verify the missing value formula of Proposition 7.7.1 by differentiating $\mathrm{SS}_{\mathrm{E}}(x)$.

   **Answer** Write the completed-data residuals as linear functions of $x$. The residual of cell $(k,l)$ is $e_{kl}(x)=y_{kl}-\bar y_{k\cdot}-\bar y_{\cdot l}+\bar y_{\cdot\cdot}$, and $x$ enters $\bar y_{i\cdot}$ with weight $1/b$, $\bar y_{\cdot j}$ with weight $1/a$ and $\bar y_{\cdot\cdot}$ with weight $1/(ab)$. Since the residuals of the additive model are the projection of the data onto the interaction space $\mathcal{L}$, $\mathrm{SS}_{\mathrm{E}}(x)=\|P_{\mathcal{L}}(\boldsymbol{y}_0+x\boldsymbol{u})\|^2$, where $\boldsymbol{y}_0$ has $0$ in the cell $(i,j)$ and $\boldsymbol{u}$ is the indicator of that cell. Then $\frac{\mathrm{d}}{\mathrm{d}x}\mathrm{SS}_{\mathrm{E}}=2\langle P_{\mathcal{L}}(\boldsymbol{y}_0+x\boldsymbol{u}),\boldsymbol{u}\rangle=2e_{ij}(x)$, because $P_{\mathcal{L}}$ is symmetric and idempotent. Setting it to zero gives $e_{ij}(x)=0$, that is, $x=\bar y_{i\cdot}+\bar y_{\cdot j}-\bar y_{\cdot\cdot}$ with completed-data means, which rearranges to $x=(a\,y'_{i\cdot}+b\,y'_{\cdot j}-y'_{\cdot\cdot})/[(a-1)(b-1)]$ as in the proof of the proposition. The second derivative $2\|P_{\mathcal{L}}\boldsymbol{u}\|^2=2(a-1)(b-1)/(ab)>0$ confirms a minimum.

10. In the golf experiment ($9$ golfers, each hitting $5$ balls from each of $3$ tee heights in random order), identify $a$, $b$ and $n$ in the model $y_{ijk}=\mu+\tau_i+\beta_j+\gamma_{ij}+\varepsilon_{ijk}$, and explain why the interaction mean square, not the error mean square, is the denominator of the test for tee heights.

    **Answer** $a=3$ tee heights, $b=9$ golfers, $n=5$ drives per golfer and tee height. The golfers are a random sample of the golfers to whom the recommendation is addressed, so the golfer-by-tee-height interaction is random, and $\mathbb{E}[\mathrm{MS}_A]=\sigma^2+n\sigma_{\tau\beta}^2+bn\sum\tau_i^2/(a-1)$. Under $H_0$ this equals $\mathbb{E}[\mathrm{MS}_{AB}]$, not $\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]$; dividing by $\mathrm{MS}_{\mathrm{E}}$ would ignore the golfer-to-golfer variation of the tee height effect and overstate the evidence ($F=12.68$ instead of $5.85$).

11. Four tips are compared on a hardness tester using four coupons as blocks (Section 7.2.1). Suppose the coded readings are

    | Tip | Coupon 1 | Coupon 2 | Coupon 3 | Coupon 4 |
    |---|---|---|---|---|
    | 1 | 9.3 | 9.4 | 9.6 | 10.0 |
    | 2 | 9.4 | 9.3 | 9.8 | 9.9 |
    | 3 | 9.2 | 9.4 | 9.5 | 9.7 |
    | 4 | 9.7 | 9.6 | 10.0 | 10.2 |

    Construct the ANOVA table, test for differences between the tips at $\alpha=0.05$, and compare with the analysis that ignores the coupons.

    **Answer** Tip totals $38.3$, $38.4$, $37.8$, $39.5$; coupon totals $37.6$, $37.7$, $38.9$, $39.8$; $y_{\cdot\cdot}=154.0$, $N=16$. $\mathrm{SS}_{\mathrm{T}}=1.290$, $\mathrm{SS}_{\mathrm{Tr}}=0.385$, $\mathrm{SS}_{\mathrm{Blocks}}=0.825$, $\mathrm{SS}_{\mathrm{E}}=0.080$ on $9$ df, $\mathrm{MS}_{\mathrm{E}}=0.00889$. $F_0=(0.385/3)/0.00889=14.44>F_{3,9,0.05}=3.86$ ($p=0.0009$): the tips differ. Ignoring the coupons, the error is $(0.825+0.080)/12=0.0754$ on $12$ df and $F_0=1.70$ ($p=0.22$): the tip effect would be missed entirely. Here $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}=30.9$, and the refined relative efficiency is about $6.7$.

12. The RCBD with $a=2$ is a paired design. For the first two tips of Question 11, compute the paired $t$-statistic and the RCBD $F$-statistic and check Proposition 7.3.1.

    **Answer** The differences tip 1 minus tip 2 are $-0.1$, $0.1$, $-0.2$, $0.1$, with $\bar d=-0.025$ and $s_d=0.15$, so $t_0=-0.025/(0.15/2)=-0.333$ and $t_0^2=0.111$. The RCBD with these two tips has $\mathrm{SS}_{\mathrm{Tr}}=4\times0.025^2/2=0.00125$ and $\mathrm{SS}_{\mathrm{E}}=3\times0.15^2/2=0.03375$ on $3$ df, so $F_0=0.00125/0.01125=0.111=t_0^2$.
