---
title: Experiments with More Than One Factor
description: One-factor-at-a-time versus full factorial designs; interaction and the parallel-lines rule; the means model and the main-effect–interaction model of a two-factor completely randomized design, parameter counting, balance and orthogonality; the two-way ANOVA with expected mean squares and the battery life example; interpreting main effects in the presence of interaction; unreplicated experiments, the additive model, the randomized complete block design and Tukey's one-degree-of-freedom test for nonadditivity; the three-way ANOVA and the soft drink bottling example.
---

The previous chapters studied experiments with a single factor. Most real processes depend on several factors at once, and moving from one factor to two brings a genuinely new phenomenon: the effect of one factor may depend on the level of the other. This interaction is the analogue, for designed experiments, of product terms in a regression model ([3.3.10](/3.3.10)), and just as correlated predictors complicate the interpretation of regression coefficients, interaction complicates the interpretation of main effects. Moving from two factors to many brings a practical problem: the number of runs grows multiplicatively, which makes efficiency of the design a central concern.

This chapter develops the two-factor factorial experiment from the point of view of design. We first compare the one-factor-at-a-time strategy with the full factorial design, then build the models of a two-factor completely randomized design, explain why balance and randomization matter for estimation, and derive the two-way analysis of variance. We then treat experiments without replication, where the interaction cannot be separated from the error, which leads to the additive model, the randomized complete block design and Tukey's test for nonadditivity. The chapter ends with three factors. The two-way models and the ANOVA table were introduced from the regression side in [3.3.14](/3.3.14), together with least squares means and diagnostics for ANOVA models; here they are rederived in the notation of the preceding chapters, and the topics specific to experimental design are added.

## 6.1. Experiments with Two Factors

A two-factor experiment has a **factor** $A$ with $a$ levels, a factor $B$ with $b$ levels, and a response $Y$. The goals are to evaluate the effects of $A$ and $B$ on $Y$ and to find the best combination of levels. Two strategies are common.

### 6.1.1. One Factor at a Time versus Factorial Designs

**Definition 6.1.1 (One-Factor-at-a-Time)** The **one-factor-at-a-time** (OFAT) strategy starts from a baseline combination of levels, varies one factor over its levels while all other factors are held fixed, fixes that factor at its best level, and then varies the next factor in the same way.

With two factors and one run per combination, OFAT needs only $a+b-1$ runs: $a$ runs for factor $A$ at the baseline level of $B$, and $b-1$ further runs for $B$ at the chosen level of $A$. It is intuitive and economical, and it is still widely used. Its fundamental weakness is that it assumes, without being able to check, that the best level of one factor does not depend on the levels of the others. When the factors interact, OFAT explores only two lines through the factor space and can settle on a combination far from the optimum; and because the effect of $A$ is observed at one level of $B$ only, the experiment cannot estimate the interaction at all.

The alternative is to run all combinations. A **full factorial design** ([3.8.1](/3.8.1)) tests every combination of factor levels; if some combinations are skipped, the design is not a full factorial. With two factors and $n$ replicates per combination it needs $abn$ runs, arranged as in the following table, where $y_{ijk}$ is the $k$-th observation at level $i$ of $A$ and level $j$ of $B$:

| | $B=1$ | $B=2$ | $\cdots$ | $B=b$ |
|---|---|---|---|---|
| $A=1$ | $y_{111},\dots,y_{11n}$ | $y_{121},\dots,y_{12n}$ | $\cdots$ | $y_{1b1},\dots,y_{1bn}$ |
| $\vdots$ | $\vdots$ | $\vdots$ | | $\vdots$ |
| $A=a$ | $y_{a11},\dots,y_{a1n}$ | $y_{a21},\dots,y_{a2n}$ | $\cdots$ | $y_{ab1},\dots,y_{abn}$ |

For example, a pharmaceutical company studies the solubility of a drug compound at two temperatures ($20^\circ\mathrm{C}$ and $30^\circ\mathrm{C}$) and two pH levels ($5$ and $7$). The $2\times2$ factorial design runs all four combinations, which allows the company to compare solubility across temperatures (the main effect of $A$), across pH levels (the main effect of $B$), and to detect whether the effect of temperature depends on the pH (the interaction).

| | One factor at a time | Full factorial design |
|---|---|---|
| Runs (one per combination) | $a+b-1$ | $ab$ (with $n$ replicates, $abn$) |
| Main effects | each estimated at a single level of the other factor | each estimated averaged over all levels of the other factor |
| Interaction | cannot be estimated | estimated and tested |
| Optimum | may be missed when the factors interact | all combinations are observed |
| Validity of conclusions | only along the lines explored | over the whole experimental region |
| Efficiency | each observation informs one comparison | every observation is used for every main effect |

The last line deserves comment. In a factorial design each observation contributes to the estimate of every main effect: the main effect of $A$ is estimated from all $abn$ observations, averaged over $B$. To estimate the effect of $A$ with the same precision, OFAT needs separate replicated runs for each factor. So even when there is no interaction, the factorial design is more efficient; when there is interaction, it is the only one of the two that gives correct conclusions. The price is the number of runs, which grows as the product of the numbers of levels; with many factors this leads to fractional factorial designs, the subject of later chapters.

![A response surface with interaction between A and B (contours). Left: the one-factor-at-a-time strategy varies A with B at its baseline, keeps the best A, then varies B, and settles on a combination with response 60 while the optimum 70 lies elsewhere. Right: the 3 x 3 factorial design observes all combinations](./plots/ofat-vs-factorial.py)

### 6.1.2. Interaction

Two factors $A$ and $B$ are said to have a two-way **interaction** if the effect of factor $A$ changes with the level of factor $B$ (equivalently, the effect of $B$ changes with the level of $A$). This is the interaction effect met in regression; Section 6.2 gives the precise definition in terms of the cell means.

The **interaction plot** displays the mean response at each combination against the levels of one factor, with one line (trace) for each level of the other factor. The effect of $A$ at a given level of $B$ is read off as the vertical change along the corresponding line. Hence the parallel-lines rule:

$$
\text{no interaction}\iff\text{the lines of the interaction plot are parallel}.
$$
Without interaction, changing $B$ shifts the whole profile of $A$ up or down by a constant. Nonparallel lines mean interaction; lines that cross mean that even the direction of the effect of $A$ depends on $B$. The rule holds exactly for the true means $\mu_{ij}$. Lines drawn through sample means are never exactly parallel, because each cell mean carries sampling error, so the plot is an exploratory tool, and whether a departure from parallelism is real is decided by the $F$-test for interaction (Section 6.3).

![Four interaction patterns in a 2 x 2 factorial: parallel lines (no interaction); interaction with both effects in the same direction; crossing lines; and pure interaction, where both marginal means of A and of B are equal although each factor has a strong effect at each level of the other](./plots/interaction-patterns.py)

For quantitative factors the interaction has a geometric meaning. Consider the regression model with two predictors and their product,

$$
Y_i=\beta_0+\beta_1X_{1i}+\beta_2X_{2i}+\beta_3X_{1i}X_{2i}+\varepsilon_i .
$$
Why model interaction as a product term? Without interaction, the response is a linear combination of the regressors, $\beta_0+\beta_1X_1+\beta_2X_2$, a plane, and the slope with respect to $X_1$ is the same constant $\beta_1$ for every value of $X_2$. Interaction means that the relationship between one regressor and the response is different for different values of the other, so the slopes become functions, $\beta_1=\beta_1(X_2)$ and $\beta_2=\beta_2(X_1)$. The simplest departure lets the slopes depend linearly on the other variable, $\beta_1(X_2)=\gamma_0+\gamma_1X_2$ and $\beta_2(X_1)=\delta_0+\delta_1X_1$. Substituting,

$$
Y=\beta_0+(\gamma_0+\gamma_1X_2)X_1+(\delta_0+\delta_1X_1)X_2+\varepsilon=\beta_0+\gamma_0X_1+\delta_0X_2+(\gamma_1+\delta_1)X_1X_2+\varepsilon,
$$
which is the product model with $\beta_3=\gamma_1+\delta_1$; only the sum $\gamma_1+\delta_1$ is identified. Conversely, the product model can be read either way: $Y=(\beta_0+\beta_2X_2)+(\beta_1+\beta_3X_2)X_1+\varepsilon$, a line in $X_1$ whose intercept and slope change linearly with $X_2$. Geometrically, the response surface is no longer a plane but a twisted surface (a hyperbolic paraboloid): its sections at fixed $X_2$ are straight lines with different slopes. So including the interaction in a factorial experiment with quantitative factors amounts to allowing a form of curvature, a twist, in the corresponding response surface model, although each one-dimensional section remains linear.

### 6.1.3. Example: The Battery Life Experiment

An engineer is designing a battery for use in a device that will be subjected to extreme variations in temperature. The only design parameter she can select is the plate material, with three possible choices. The temperature cannot be controlled in the field, but it can be controlled in the laboratory for testing. Four batteries are tested at each combination of plate material ($A$, $a=3$) and temperature ($B$: $15$, $70$, $125\,^\circ\mathrm{F}$, $b=3$), and all $36$ tests are run in random order. The response is the effective life in hours:

| Material | $15^\circ\mathrm{F}$ | $70^\circ\mathrm{F}$ | $125^\circ\mathrm{F}$ |
|---|---|---|---|
| 1 | 130, 155, 74, 180 | 34, 40, 80, 75 | 20, 70, 82, 58 |
| 2 | 150, 188, 159, 126 | 136, 122, 106, 115 | 25, 70, 58, 45 |
| 3 | 138, 110, 168, 160 | 174, 120, 150, 139 | 96, 104, 82, 60 |

Two questions are asked. What effects do the material type and the temperature have on the life of the battery? And is there a choice of material that gives uniformly long life regardless of temperature, that is, a robust product?

The cell means are

| Material | $15^\circ\mathrm{F}$ | $70^\circ\mathrm{F}$ | $125^\circ\mathrm{F}$ | $\bar y_{i\cdot\cdot}$ |
|---|---|---|---|---|
| 1 | 134.75 | 57.25 | 57.50 | 83.17 |
| 2 | 155.75 | 119.75 | 49.50 | 108.33 |
| 3 | 144.00 | 145.75 | 85.50 | 125.08 |
| $\bar y_{\cdot j\cdot}$ | 144.83 | 107.58 | 64.17 | $\bar y_{\cdot\cdot\cdot}=105.53$ |

Boxplots by factor show that life decreases with temperature and that material 3 tends to give longer life, but boxplots by one factor average over the other and cannot reveal interaction. The interaction plot can.

```r
interaction.plot(x.factor = Battery$Temp, trace.factor = Battery$Type,
                 response = Battery$Life, xlab = 'Temperature',
                 ylab = 'Average life', trace.label = 'Material Type', bty = 'L')
```

![Battery life: cell means of the three materials against temperature, with error bars of plus and minus one standard error of a cell mean computed from the error mean square](./plots/battery-interaction.py)

The lines are clearly not parallel. All materials lose life at high temperature, but material 1 loses most of it already between $15$ and $70^\circ\mathrm{F}$, while material 3 keeps its life up to $70^\circ\mathrm{F}$; between $15$ and $70^\circ\mathrm{F}$ the effect of temperature thus depends strongly on the material. From the exploratory analysis the interaction looks fairly pronounced; Section 6.3 tests it.

## 6.2. Models for the Two-Factor Factorial

### 6.2.1. The Means Model and the Completely Randomized Design

The simplest model treats each of the $ab$ combinations as a treatment.

**Definition 6.2.1 (Two-Way Means Model)** The means model of a two-factor factorial experiment is

$$
Y_{ijk}=\mu_{ij}+\varepsilon_{ijk},\qquad i=1,\dots,a,\quad j=1,\dots,b,\quad k=1,\dots,n,\qquad \varepsilon_{ijk}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
where $\mu_{ij}$ is the mean response at level $i$ of $A$ and level $j$ of $B$.

This is the one-way **cell means model** with $ab$ treatments. The design that realizes it is a **completely randomized design** with $ab$ treatments ([3.8.3](/3.8.3)): the $abn$ runs are made in random order, or equivalently the $abn$ experimental units are allocated to the treatment combinations completely at random. This is what makes the errors independent and protects the comparisons against lurking variables (Section 6.2.4). The two-factor effects model familiar from regression is thus, in the language of design, the model of a factorial design carried out as a CRD.

As in the one-way case, means and contrasts of the $\mu_{ij}$ describe the effects. The mean response at level $i$ of $A$, averaged over all levels of $B$, and the corresponding quantities for $B$ are

$$
\bar\mu_{i\cdot}=\frac1b\sum_{j=1}^b\mu_{ij},\qquad \bar\mu_{\cdot j}=\frac1a\sum_{i=1}^a\mu_{ij},\qquad \mu=\bar\mu_{\cdot\cdot}=\frac{1}{ab}\sum_{i,j}\mu_{ij}.
$$
We write $\bar\mu_{i\cdot}=\mu+\alpha_i$ and $\bar\mu_{\cdot j}=\mu+\beta_j$: the **main effects** $\alpha_i$ of $A$ and $\beta_j$ of $B$ are the deviations of the marginal means from the overall mean, and by construction $\sum_i\alpha_i=\sum_j\beta_j=0$.

### 6.2.2. The Interaction Terms

The effect of changing factor $A$ from level $i_1$ to level $i_2$ is $\mu_{i_2j_1}-\mu_{i_1j_1}$ if $B$ is fixed at level $j_1$, and $\mu_{i_2j_2}-\mu_{i_1j_2}$ if $B$ is fixed at level $j_2$. If the two are equal, that is,

$$
\mu_{i_2j_1}-\mu_{i_1j_1}-\mu_{i_2j_2}+\mu_{i_1j_2}=0,
$$
the levels $(i_1,i_2)$ of $A$ do not interact with the levels $(j_1,j_2)$ of $B$; in the interaction plot, the segments of the two traces between $i_1$ and $i_2$ are parallel. If this holds for all $i_1,i_2,j_1,j_2$, the factors $A$ and $B$ have no interaction.

**Definition 6.2.2 (Interaction Terms)** The interaction terms of factors $A$ and $B$ are

$$
(\alpha\beta)_{ij}=\mu_{ij}-\mu-\alpha_i-\beta_j=\mu_{ij}-\bar\mu_{i\cdot}-\bar\mu_{\cdot j}+\bar\mu_{\cdot\cdot}.
$$
Some texts write $\gamma_{ij}$; the symbol $(\alpha\beta)_{ij}$ is a single parameter, not a product.

**Proposition 6.2.1** The factors $A$ and $B$ have no interaction if and only if $(\alpha\beta)_{ij}=0$ for all $i,j$.

**Proof** Averaging the four-term expression over the other indices gives

$$
\mu_{ij}-\bar\mu_{i\cdot}-\bar\mu_{\cdot j}+\bar\mu_{\cdot\cdot}=\frac{1}{ab}\sum_{l=1}^a\sum_{m=1}^b\big(\mu_{ij}-\mu_{im}-\mu_{lj}+\mu_{lm}\big).
$$
If there is no interaction, every term of the sum is zero, so $(\alpha\beta)_{ij}=0$. Conversely, if all $(\alpha\beta)_{ij}=0$, then $\mu_{ij}=\mu+\alpha_i+\beta_j$ and $\mu_{i_2j_1}-\mu_{i_1j_1}=\alpha_{i_2}-\alpha_{i_1}=\mu_{i_2j_2}-\mu_{i_1j_2}$ for all levels. $\square$

So every cell mean decomposes as

$$
\mu_{ij}=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij},
$$
the overall mean, adjusted by the main effect of each factor and by an interaction that is what the additive part $\mu+\alpha_i+\beta_j$ cannot explain. Each observation, correspondingly, is a sum of five pieces, each corresponding to a meaningful partition of the data, like parts added on an assembly line: a benchmark (the grand mean), the effect of the material type, the effect of the temperature, the interaction effect and the residual error. Section 6.3 estimates these pieces and partitions the variation of the data in the same way.

### 6.2.3. The Main-Effect–Interaction Model

**Definition 6.2.3 (Main-Effect–Interaction Model)** The main-effect–interaction model (two-way **factor effects model**) of a two-factor factorial design is

$$
Y_{ijk}=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}+\varepsilon_{ijk},\qquad \varepsilon_{ijk}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
with the constraints

$$
\sum_{i=1}^a\alpha_i=0,\qquad \sum_{j=1}^b\beta_j=0,\qquad \sum_{j=1}^b(\alpha\beta)_{ij}=0\ \text{for all }i,\qquad \sum_{i=1}^a(\alpha\beta)_{ij}=0\ \text{for all }j.
$$

The first two constraints hold by definition of the main effects. The others follow from Definition 6.2.2.

**Proposition 6.2.2** With the interaction terms defined by Definition 6.2.2, $\sum_{j=1}^b(\alpha\beta)_{ij}=0$ for every $i$, and $\sum_{i=1}^a(\alpha\beta)_{ij}=0$ for every $j$.

**Proof** Summing over $j$, $\sum_j(\alpha\beta)_{ij}=\sum_j\mu_{ij}-b\bar\mu_{i\cdot}-\sum_j\bar\mu_{\cdot j}+b\bar\mu_{\cdot\cdot}=b\bar\mu_{i\cdot}-b\bar\mu_{i\cdot}-b\bar\mu_{\cdot\cdot}+b\bar\mu_{\cdot\cdot}=0$. The sum over $i$ is analogous. $\square$

**Proposition 6.2.3** The main-effect–interaction model has $1+a+b+ab+1=(a+1)(b+1)+1$ parameters ($\mu$, the $\alpha_i$, the $\beta_j$, the $(\alpha\beta)_{ij}$ and $\sigma^2$), $a+b+1$ independent constraints, and therefore $ab+1$ free parameters, the same number as the means model ($ab$ cell means and $\sigma^2$).

**Proof** The constraints are $1$ on the $\alpha_i$, $1$ on the $\beta_j$, $a$ row constraints and $b$ column constraints on the interactions. The row and column constraints are dependent: both sets imply $\sum_{i,j}(\alpha\beta)_{ij}=0$, and this is the only dependence, so they contribute $a+b-1$ independent constraints, for a total of $1+1+(a+b-1)=a+b+1$. Subtracting, $(a+1)(b+1)+1-(a+b+1)=ab+1$. $\square$

The free parameters split as $1$ for $\mu$, $a-1$ for $A$, $b-1$ for $B$, $(a-1)(b-1)$ for the interaction, and $1$ for $\sigma^2$; these are the degrees of freedom of the two-way ANOVA table below.

### 6.2.4. Estimation, Randomization and Balance

**Proposition 6.2.4** In a balanced two-factor design ($n$ observations per cell), the least squares estimates under the constraints of Definition 6.2.3 are

$$
\hat\mu=\bar y_{\cdot\cdot\cdot},\qquad \hat\alpha_i=\bar y_{i\cdot\cdot}-\bar y_{\cdot\cdot\cdot},\qquad \hat\beta_j=\bar y_{\cdot j\cdot}-\bar y_{\cdot\cdot\cdot},\qquad \widehat{(\alpha\beta)}_{ij}=\bar y_{ij\cdot}-\bar y_{i\cdot\cdot}-\bar y_{\cdot j\cdot}+\bar y_{\cdot\cdot\cdot},
$$
and the fitted value of every observation in cell $(i,j)$ is the cell mean $\hat y_{ijk}=\bar y_{ij\cdot}$.

**Proof** The least squares estimates of the means model are the cell means, $\hat\mu_{ij}=\bar y_{ij\cdot}$, since the cells are separate one-way groups. The parameters of the effects model are linear functions of the cell means (Definitions 6.2.2 and 6.2.3), and with equal cell sizes the averages of the $\bar y_{ij\cdot}$ over $j$, over $i$ and over both are $\bar y_{i\cdot\cdot}$, $\bar y_{\cdot j\cdot}$ and $\bar y_{\cdot\cdot\cdot}$. $\square$

For the battery data, $\hat\mu=105.53$, $\hat\alpha=(-22.36,\ 2.81,\ 19.56)$ for the three materials, $\hat\beta=(39.31,\ 2.06,\ -41.36)$ for the three temperatures, and for instance $\widehat{(\alpha\beta)}_{12}=57.25-83.17-107.58+105.53=-27.97$: at $70^\circ\mathrm{F}$, material 1 lasts about 28 hours less than its main effect and the temperature effect predict.

Why should the design be a CRD? Suppose the true model contains, besides the factors, variables $Z$ that are not measured and may not even be suspected (ambient humidity, the order of testing, the batch of electrolyte):

$$
\boldsymbol{Y}=X\boldsymbol{\beta}+Z\boldsymbol{\gamma}+\boldsymbol{\varepsilon}.
$$
If we fit $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$, the least squares estimator $\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ has

$$
\mathbb{E}[\hat{\boldsymbol{\beta}}]=(X^{\mathsf T}X)^{-1}X^{\mathsf T}(X\boldsymbol{\beta}+Z\boldsymbol{\gamma})=\boldsymbol{\beta}+(X^{\mathsf T}X)^{-1}X^{\mathsf T}Z\boldsymbol{\gamma},
$$
an omitted-variable bias that vanishes when the columns of $Z$ are orthogonal to those of $X$ (after centering). We cannot control $Z$, but we control $X$: which unit receives which treatment, and in which order the runs are made. Assigning the treatments completely at random makes the treatment indicators statistically independent of every $Z$, so that $X^{\mathsf T}Z$ (centered) is zero on average over the randomization and small in any particular experiment. Randomization is the best general way of making $X$ and $Z$ as orthogonal as possible: it is the principle of [3.8.2](/3.8.2), seen through the regression formula.

Balance plays the corresponding role for the factors themselves. A factorial design is balanced if each combination of factor levels is replicated the same number of times. Balance makes the factors themselves orthogonal. Think of the levels of $A$ and $B$ assigned to a run as two random variables, the run being chosen at random from the $N$ runs. Then the proportion of runs in cell $(i,j)$ is $n_{ij}/N$, and $A$ and $B$ are independent if and only if

$$
\frac{n_{ij}}{N}=\frac{n_{i\cdot}}{N}\cdot\frac{n_{\cdot j}}{N},\qquad\text{that is,}\qquad n_{ij}N=n_{i\cdot}n_{\cdot j}\quad\text{for all }i,j,
$$
where $n_{i\cdot}=\sum_jn_{ij}$ and $n_{\cdot j}=\sum_in_{ij}$. When $n_{ij}=n$ for all cells, $n_{i\cdot}=bn$, $n_{\cdot j}=an$ and $N=abn$, and the relation holds: balance implies independence. (Proportional frequencies are the general condition; balance is the most important special case.) For a $2\times2$ design with indicator variables $x_1$, $x_2$ and $80$ runs, three allocations illustrate this:

| Cell counts $n_{ij}$ | $(x_1,x_2)=(0,0),(0,1),(1,0),(1,1)$ | Correlation of $x_1$ and $x_2$ | Consequence |
|---|---|---|---|
| balanced | $20,20,20,20$ | $r=0$ | orthogonal factors |
| only two cells used | $40,0,0,40$ | $r=1$ | $x_1$, $x_2$ and $x_1x_2$ completely confounded |
| unbalanced | $20,20,10,30$ | $r\approx0.26$ | if $x_1=1$, then $x_2=1$ is more likely |

With balance, the advantages are simple parameter estimates (Proposition 6.2.4) and a unique decomposition of the variation into parts for $A$, $B$ and $AB$. In an unbalanced design the main concern is therefore multicollinearity: the indicator columns of $A$, $B$ and $AB$ are correlated, so the variation explained by one factor overlaps with that explained by another, the sums of squares depend on the order in which the effects are entered (sequential sums of squares, [3.3.9](/3.3.9)), and the estimates are less precise. The estimators remain unbiased and consistent; it is their separation and interpretation that suffer.

Imbalance also affects averages. In a balanced design the overall mean of two groups is the same whether one averages all scores or averages the two group means. With the scores $5,6,7,9,10$ (mean $7.4$) and $8,9,12,7,14$ (mean $10$), both give $8.7$. If the first group has only the scores $5,6$ (mean $5.5$), the mean of all seven scores is the weighted mean $(2\cdot5.5+5\cdot10)/7=8.71$, while the unweighted mean of the group means is $(5.5+10)/2=7.75$. In multifactor designs the analogous unweighted averages of the fitted cell means are the **least squares means** of [3.3.14](/3.3.14); they answer "what is the effect of $A$ averaged equally over the levels of $B$" regardless of how many observations each cell happens to have.

## 6.3. The Two-Way Analysis of Variance

### 6.3.1. Hypotheses and the Partition of the Sum of Squares

In the main-effect–interaction model of a balanced design, three hypotheses are tested:

$$
\begin{aligned}
&H_0^A\colon\alpha_1=\cdots=\alpha_a=0 &&\text{(no main effect of }A),\\
&H_0^B\colon\beta_1=\cdots=\beta_b=0 &&\text{(no main effect of }B),\\
&H_0^{AB}\colon(\alpha\beta)_{ij}=0\text{ for all }i,j &&\text{(no interaction)},
\end{aligned}
$$
each against the alternative that at least one of the parameters is nonzero. The deviation of an observation from the grand mean splits into estimated effects and a residual,

$$
y_{ijk}-\bar y_{\cdot\cdot\cdot}=(\bar y_{i\cdot\cdot}-\bar y_{\cdot\cdot\cdot})+(\bar y_{\cdot j\cdot}-\bar y_{\cdot\cdot\cdot})+(\bar y_{ij\cdot}-\bar y_{i\cdot\cdot}-\bar y_{\cdot j\cdot}+\bar y_{\cdot\cdot\cdot})+(y_{ijk}-\bar y_{ij\cdot}).
$$
Squaring and summing over all observations, the six cross products vanish in a balanced design (each involves a sum of deviations that is zero by the constraints), and

$$
\underbrace{\sum_{i,j,k}(y_{ijk}-\bar y_{\cdot\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{T}}}=\underbrace{bn\sum_i(\bar y_{i\cdot\cdot}-\bar y_{\cdot\cdot\cdot})^2}_{\mathrm{SS}_A}+\underbrace{an\sum_j(\bar y_{\cdot j\cdot}-\bar y_{\cdot\cdot\cdot})^2}_{\mathrm{SS}_B}+\underbrace{n\sum_{i,j}(\bar y_{ij\cdot}-\bar y_{i\cdot\cdot}-\bar y_{\cdot j\cdot}+\bar y_{\cdot\cdot\cdot})^2}_{\mathrm{SS}_{AB}}+\underbrace{\sum_{i,j,k}(y_{ijk}-\bar y_{ij\cdot})^2}_{\mathrm{SS}_{\mathrm{E}}},
$$
with the corresponding partition of the degrees of freedom

$$
abn-1=(a-1)+(b-1)+(a-1)(b-1)+ab(n-1).
$$
The error degrees of freedom are $ab(n-1)$ because each of the $ab$ cells contributes $n-1$ degrees of freedom for replication; with $n=1$ there are none (Section 6.4).

For hand calculation, the sums of squares are computed from the totals $y_{i\cdot\cdot}$, $y_{\cdot j\cdot}$, $y_{ij\cdot}$ and $y_{\cdot\cdot\cdot}$:

$$
\begin{aligned}
\mathrm{SS}_{\mathrm{T}}&=\sum_{i,j,k}y_{ijk}^2-\frac{y_{\cdot\cdot\cdot}^2}{abn}, &\mathrm{SS}_A&=\frac{1}{bn}\sum_iy_{i\cdot\cdot}^2-\frac{y_{\cdot\cdot\cdot}^2}{abn}, &\mathrm{SS}_B&=\frac{1}{an}\sum_jy_{\cdot j\cdot}^2-\frac{y_{\cdot\cdot\cdot}^2}{abn},\\
\mathrm{SS}_{\mathrm{Subtotals}}&=\frac1n\sum_{i,j}y_{ij\cdot}^2-\frac{y_{\cdot\cdot\cdot}^2}{abn}, &\mathrm{SS}_{AB}&=\mathrm{SS}_{\mathrm{Subtotals}}-\mathrm{SS}_A-\mathrm{SS}_B, &\mathrm{SS}_{\mathrm{E}}&=\mathrm{SS}_{\mathrm{T}}-\mathrm{SS}_{\mathrm{Subtotals}}.
\end{aligned}
$$

### 6.3.2. Expected Mean Squares and the ANOVA Table

**Theorem 6.3.1** In the balanced two-way main-effect–interaction model with fixed effects:

1. $\mathrm{SS}_A$, $\mathrm{SS}_B$, $\mathrm{SS}_{AB}$ and $\mathrm{SS}_{\mathrm{E}}$ are independent;
2. $\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2$ and $\mathrm{SS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{ab(n-1)}$;
3. $\mathbb{E}[\mathrm{MS}_A]=\sigma^2+\dfrac{bn}{a-1}\sum_i\alpha_i^2$, and if $\alpha_1=\cdots=\alpha_a=0$, then $\mathrm{SS}_A/\sigma^2\sim\chi^2_{a-1}$;
4. $\mathbb{E}[\mathrm{MS}_B]=\sigma^2+\dfrac{an}{b-1}\sum_j\beta_j^2$, and if $\beta_1=\cdots=\beta_b=0$, then $\mathrm{SS}_B/\sigma^2\sim\chi^2_{b-1}$;
5. $\mathbb{E}[\mathrm{MS}_{AB}]=\sigma^2+\dfrac{n}{(a-1)(b-1)}\sum_{i,j}(\alpha\beta)_{ij}^2$, and if all $(\alpha\beta)_{ij}=0$, then $\mathrm{SS}_{AB}/\sigma^2\sim\chi^2_{(a-1)(b-1)}$.

**Proof** The four components of the decomposition in Section 6.3.1 are the orthogonal projections of $\boldsymbol{y}$ onto four mutually orthogonal subspaces of $\mathbb{R}^{abn}$ (orthogonal to the constant vector), of dimensions $a-1$, $b-1$, $(a-1)(b-1)$ and $ab(n-1)$; this is the orthogonality established in Section 6.3.1. By **Cochran's theorem** ([3.8.3](/3.8.3)) the squared lengths are independent, and each divided by $\sigma^2$ is a noncentral $\chi^2$ variable with that many degrees of freedom and noncentrality equal to the squared length of the projection of the mean vector divided by $\sigma^2$. The mean vector has components $\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}$; its projections are the corresponding effects, with squared lengths $bn\sum\alpha_i^2$, $an\sum\beta_j^2$, $n\sum(\alpha\beta)_{ij}^2$ and $0$. Since a $\chi^2_\nu(\lambda)$ variable has mean $\nu+\lambda$, dividing by the degrees of freedom gives the expected mean squares. $\square$

Each mean square has expectation $\sigma^2$ when its effects vanish and larger otherwise, so each hypothesis is tested by comparing the mean square with $\mathrm{MS}_{\mathrm{E}}$, rejecting for large values:

| Source | SS | df | MS | $\mathbb{E}[\mathrm{MS}]$ | $F_0$ |
|---|---|---|---|---|---|
| $A$ | $\mathrm{SS}_A$ | $a-1$ | $\mathrm{MS}_A=\frac{\mathrm{SS}_A}{a-1}$ | $\sigma^2+\frac{bn\sum\alpha_i^2}{a-1}$ | $\frac{\mathrm{MS}_A}{\mathrm{MS}_{\mathrm{E}}}\sim F_{a-1,ab(n-1)}$ |
| $B$ | $\mathrm{SS}_B$ | $b-1$ | $\mathrm{MS}_B=\frac{\mathrm{SS}_B}{b-1}$ | $\sigma^2+\frac{an\sum\beta_j^2}{b-1}$ | $\frac{\mathrm{MS}_B}{\mathrm{MS}_{\mathrm{E}}}\sim F_{b-1,ab(n-1)}$ |
| $AB$ | $\mathrm{SS}_{AB}$ | $(a-1)(b-1)$ | $\mathrm{MS}_{AB}=\frac{\mathrm{SS}_{AB}}{(a-1)(b-1)}$ | $\sigma^2+\frac{n\sum(\alpha\beta)_{ij}^2}{(a-1)(b-1)}$ | $\frac{\mathrm{MS}_{AB}}{\mathrm{MS}_{\mathrm{E}}}\sim F_{(a-1)(b-1),ab(n-1)}$ |
| Error | $\mathrm{SS}_{\mathrm{E}}$ | $ab(n-1)$ | $\mathrm{MS}_{\mathrm{E}}=\frac{\mathrm{SS}_{\mathrm{E}}}{ab(n-1)}$ | $\sigma^2$ | |
| Total | $\mathrm{SS}_{\mathrm{T}}$ | $abn-1$ | | | |

The null distributions in the last column hold under the corresponding hypothesis; $H_0^A$ is rejected at level $\alpha$ when $F_0>F_{a-1,ab(n-1),\alpha}$, and similarly for the others. The three tests share the same denominator $\mathrm{MS}_{\mathrm{E}}$; they are not independent of each other, but each has the stated level.

### 6.3.3. Example: The Battery Life ANOVA

```r
summary(aov(Life ~ Type * Temp, data = Battery))
```

```text
            Df Sum Sq Mean Sq F value   Pr(>F)    
Type         2  10684    5342   7.911  0.00198 ** 
Temp         2  39119   19559  28.968 1.91e-07 ***
Type:Temp    4   9614    2403   3.560  0.01861 *  
Residuals   27  18231     675                     
```

The formula `Type * Temp` expands to `Type + Temp + Type:Temp`, the two main effects and the interaction. The entries can be checked from the totals: with $y_{\cdot\cdot\cdot}=3799$, $N=36$ and $\sum y_{ijk}^2=478547$, $\mathrm{SS}_{\mathrm{T}}=478547-3799^2/36=77646.97$; the material totals $998$, $1300$, $1501$ give $\mathrm{SS}_A=(998^2+1300^2+1501^2)/12-3799^2/36=10683.72$; the temperature totals $1738$, $1291$, $770$ give $\mathrm{SS}_B=39118.72$; the cell totals give $\mathrm{SS}_{\mathrm{Subtotals}}=59416.22$, hence $\mathrm{SS}_{AB}=59416.22-10683.72-39118.72=9613.78$ and $\mathrm{SS}_{\mathrm{E}}=77646.97-59416.22=18230.75$. The degrees of freedom are $a-1=2$, $b-1=2$, $(a-1)(b-1)=4$ and $ab(n-1)=9\cdot3=27$; each mean square is its sum of squares divided by its degrees of freedom; and each $F$ value is the mean square divided by $\mathrm{MS}_{\mathrm{E}}=675.2$, for example $F=2403.4/675.2=3.56$ for the interaction, with $p=\mathbb{P}(F_{4,27}>3.56)=0.019$.

At the 5% level all three effects are significant: the material, the temperature, and their interaction. In particular, the interaction suspected from the interaction plot is real ($F_{4,27,0.05}=2.73$).

### 6.3.4. Main Effects in the Presence of Interaction

A main effect says that there is a difference between the marginal means of a factor regardless of the other factors. If an interaction is significant, the main effects of the factors involved in it are difficult to interpret on their own, because "regardless of the other factor" is then not true: the effect of $A$ depends on $B$. The marginal comparison averages effects that may be large, small or of opposite signs at different levels of $B$.

Two situations should be distinguished. In the first, the interaction makes the main effects nonsensical: in a treatment-versus-control experiment over time, the two groups start at the same value and only the treated group changes, so the main effect of "condition" mixes no difference at the start with a large difference at the end, and the marginal mean of the treated group does not describe the response at any time. In the second, the interaction exists but the main effect is still meaningful: if the treated group is above the control group at every time and the gap merely widens, the statement "treatment increases the response" is true at each level of time, and the main effect summarizes it, though not its size. In practice, a significant interaction calls for examining the interaction plot and comparing the levels of one factor separately at each level of the other, using the cell means and the $\mathrm{MS}_{\mathrm{E}}$ of the full model.

For the battery experiment, the first question (which effects matter) is answered by the ANOVA: material, temperature and their interaction all affect battery life. For the second question, since the effect of material depends on temperature, we compare the materials at each temperature. Tukey's method ([3.8.4](/3.8.4)) for the three cell means at a fixed temperature uses $\mathrm{MS}_{\mathrm{E}}=675.2$ with $27$ degrees of freedom and $n=4$ observations per mean, so two means differ significantly when

$$
\lvert\bar y_{ij\cdot}-\bar y_{i'j\cdot}\rvert>T_{0.05}=q_{3,27,0.05}\sqrt{\frac{\mathrm{MS}_{\mathrm{E}}}{n}}=3.506\sqrt{\frac{675.2}{4}}=45.56 .
$$

| Temperature | Cell means (materials 1, 2, 3) | Significant differences |
|---|---|---|
| $15^\circ\mathrm{F}$ | 134.75, 155.75, 144.00 | none |
| $70^\circ\mathrm{F}$ | 57.25, 119.75, 145.75 | 2 vs 1 ($62.5$), 3 vs 1 ($88.5$); 2 and 3 do not differ ($26.0$) |
| $125^\circ\mathrm{F}$ | 57.50, 49.50, 85.50 | none (largest difference $36.0$) |

At $70^\circ\mathrm{F}$, materials 2 and 3 are both better than material 1; at the extreme temperatures the materials do not differ significantly. Material 3 is never significantly worse than any other material, and it is the best or close to the best at all three temperatures: at the high temperature its mean life is $85.5$ hours against $57.5$ and $49.5$, and it loses no life at all between $15$ and $70^\circ\mathrm{F}$. If a robust battery is wanted, material 3 is the choice. The analysis should, as always, be completed by residual checks ([3.8.5](/3.8.5)).

## 6.4. Experiments without Replication

### 6.4.1. The Problem

Sometimes only one run can be made for each combination of the factors, a full factorial experiment with $n=1$, because runs are expensive or material is limited. Under the full model $y_{ij}=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}+\varepsilon_{ij}$ there are then $ab+1$ free parameters for only $ab$ observations. The model fits every observation exactly, the error sum of squares has $ab(n-1)=0$ degrees of freedom, and we run out of degrees of freedom: $\sigma^2$ is not estimable, and no effect, the interaction included, can be tested. Something must be assumed.

### 6.4.2. The Additive Model

**Definition 6.4.1 (Additive Model)** The **additive model** of a two-factor experiment is the model without interaction,

$$
Y_{ij}=\mu+\alpha_i+\beta_j+\varepsilon_{ij},\qquad \sum_i\alpha_i=\sum_j\beta_j=0,\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
in which the effects of the two factors add. It has $1+(a-1)+(b-1)+1=a+b$ free parameters.

In an unreplicated experiment the additive model leaves $ab-1-(a-1)-(b-1)=(a-1)(b-1)$ degrees of freedom for error: what was the interaction sum of squares now serves as the residual,

$$
\mathrm{SS}_{\mathrm{Res}}=\sum_{i,j}(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2,\qquad \mathrm{MS}_{\mathrm{Res}}=\frac{\mathrm{SS}_{\mathrm{Res}}}{(a-1)(b-1)},
$$
and the ANOVA table is

| Source | SS | df | MS | $F_0$ |
|---|---|---|---|---|
| $A$ | $b\sum_i(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2$ | $a-1$ | $\mathrm{MS}_A$ | $\mathrm{MS}_A/\mathrm{MS}_{\mathrm{Res}}$ |
| $B$ | $a\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2$ | $b-1$ | $\mathrm{MS}_B$ | $\mathrm{MS}_B/\mathrm{MS}_{\mathrm{Res}}$ |
| Residual | $\mathrm{SS}_{\mathrm{Res}}$ | $(a-1)(b-1)$ | $\mathrm{MS}_{\mathrm{Res}}$ | |
| Total | $\sum_{i,j}(y_{ij}-\bar y_{\cdot\cdot})^2$ | $ab-1$ | | |

The validity of the tests rests on the assumption of no interaction. If there is interaction, $\mathbb{E}[\mathrm{MS}_{\mathrm{Res}}]=\sigma^2+\sum_{i,j}(\alpha\beta)_{ij}^2/[(a-1)(b-1)]$ overestimates $\sigma^2$, and the tests of the main effects become conservative. No test for the full interaction is possible: the interaction line of the replicated table has been sacrificed to estimate the error.

**Example 6.4.1** The impurity present in a chemical product is affected by two factors, pressure and temperature. The data from a single replicate of a factorial experiment are

| Temperature ($^\circ\mathrm{F}$) | 25 psi | 30 psi | 35 psi | 40 psi | 45 psi | $y_{i\cdot}$ |
|---|---|---|---|---|---|---|
| 100 | 5 | 4 | 6 | 3 | 5 | 23 |
| 125 | 3 | 1 | 4 | 2 | 3 | 13 |
| 150 | 1 | 1 | 3 | 1 | 2 | 8 |
| $y_{\cdot j}$ | 9 | 6 | 13 | 6 | 10 | $y_{\cdot\cdot}=44$ |

With $a=3$ temperatures and $b=5$ pressures, $\mathrm{SS}_{\mathrm{T}}=166-44^2/15=36.93$, $\mathrm{SS}_A=(23^2+13^2+8^2)/5-44^2/15=23.33$, $\mathrm{SS}_B=(9^2+6^2+13^2+6^2+10^2)/3-44^2/15=11.60$, and $\mathrm{SS}_{\mathrm{Res}}=36.93-23.33-11.60=2.00$ on $(a-1)(b-1)=8$ degrees of freedom:

| Source | SS | df | MS | $F_0$ | $p$ |
|---|---|---|---|---|---|
| Temperature | 23.33 | 2 | 11.67 | 46.67 | $3.9\times10^{-5}$ |
| Pressure | 11.60 | 4 | 2.90 | 11.60 | $0.0021$ |
| Residual | 2.00 | 8 | 0.25 | | |
| Total | 36.93 | 14 | | | |

Both temperature and pressure affect the impurity, provided the additive model is adequate. The interaction plot, with nearly parallel profiles, supports the assumption; Section 6.4.5 gives a formal check.

![Impurity against pressure for the three temperatures in the unreplicated experiment; the profiles are roughly parallel](./plots/impurity-additivity.py)

### 6.4.3. The Randomized Complete Block Design

The most common source of unreplicated two-way data is not a factorial experiment at all but a blocked one. It is often impractical to randomize all runs of an experiment completely: the runs may have to be made on different days, with different batches of raw material or by different operators. Such a **nuisance factor** is handled by **blocking** ([3.8.2](/3.8.2)).

**Definition 6.4.2 (Randomized Complete Block Design)** In a **randomized complete block design** (RCBD), the experimental units are grouped into $b$ **blocks** of homogeneous units, each block contains one unit for each of the $a$ treatments, and the treatments are assigned to the units at random, separately and independently within each block. With one observation per treatment and block, the model is the additive model

$$
Y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij},\qquad i=1,\dots,a,\quad j=1,\dots,b,
$$
with treatment effects $\tau_i$, block effects $\beta_j$, and the assumption that blocks and treatments do not interact.

The aims of the RCBD are to evaluate the effect of the treatment factor on the response while removing the potential effect of the block factor: differences between blocks are taken out of the error, which makes the comparison of treatments more precise when the blocks really differ. A factorial experiment can be run as an RCBD as well, by running each complete replicate of the factorial in its own block. The design and analysis of block designs, their efficiency relative to the CRD, and extensions (generalized block designs, blocks as random effects) are the subject of later chapters; here the RCBD is the typical example of the additive model.

### 6.4.4. The Additive Model in the CRD and the RCBD

The additive model of an unreplicated factorial and the model of an RCBD are the same equation, $y_{ij}=\mu+\alpha_i+\beta_j+\varepsilon_{ij}$, and the ANOVA tables are computed in the same way. But the experiments are run differently, and the interpretation differs.

| | Unreplicated factorial as a CRD | Randomized complete block design |
|---|---|---|
| Factors | two treatment factors $A$ and $B$, both of interest | one treatment factor $A$; the block factor $B$ is a nuisance |
| Randomization | all $ab$ runs in a completely random order | only within each block; blocks are not randomized |
| Meaning of "additive" | an assumption about the treatment factors: they do not interact | a design assumption: the block does not interact with the treatments (the treatment effects are the same in every block) |
| Interaction, if present | a real feature of the process that the experiment cannot separate from the error | treatment-by-block interaction inflates the error |
| Test of $B$ | a valid test of the main effect of $B$ | the $F$ ratio for blocks is only an approximate guide to whether blocking was worthwhile, not a strict test, because blocks were not assigned at random |
| Conclusions | about both factors | about the treatments, valid over the range of blocks used |

So in the factorial setting, additivity is a claim about nature that may be false; in the RCBD it is part of what the experimenter assumes about the nuisance factor in choosing the design, and the blocks are not themselves an object of inference. In both cases Tukey's test below can check the assumption.

### 6.4.5. Tukey's Test for Nonadditivity

Without replication, the full interaction, with its $(a-1)(b-1)$ degrees of freedom, cannot be tested. Tukey (1949) showed how to test a particular, very common form of interaction with a single degree of freedom, leaving the rest for error. The idea is that interaction often arises because the factors act multiplicatively, or because the response is measured on a scale on which the effects are not additive; to a first approximation, the interaction is then proportional to the product of the main effects.

**Definition 6.4.3 (Tukey's Test for Nonadditivity)** In the model

$$
y_{ij}=\mu+\alpha_i+\beta_j+\lambda\alpha_i\beta_j+\varepsilon_{ij},\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
**Tukey's test for nonadditivity** tests $H_0\colon\lambda=0$ (additivity) against $H_1\colon\lambda\ne0$ by

$$
F_0=\frac{\mathrm{SS}_N/1}{\mathrm{SS}_{\mathrm{E}}/(ab-a-b)}\ \overset{H_0}{\sim}\ F_{1,\,ab-a-b},\qquad \mathrm{SS}_N=\frac{\Big[\sum_{i,j}(\bar y_{i\cdot}-\bar y_{\cdot\cdot})(\bar y_{\cdot j}-\bar y_{\cdot\cdot})\,y_{ij}\Big]^2}{\sum_i(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2\,\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2},
$$
where $\mathrm{SS}_{\mathrm{E}}=\mathrm{SS}_{\mathrm{Res}}-\mathrm{SS}_N$ is the residual of the additive model minus the nonadditivity sum of squares; $H_0$ is rejected when $F_0>F_{1,ab-a-b,\alpha}$.

The statistic comes from estimating $\lambda$. Multiplying the model by $\alpha_i\beta_j$ and summing over all $(i,j)$, the terms in $\mu$, $\alpha_i^2\beta_j$ and $\alpha_i\beta_j^2$ vanish because $\sum_i\alpha_i=\sum_j\beta_j=0$, so

$$
\sum_{i,j}\alpha_i\beta_jy_{ij}=\lambda\sum_i\alpha_i^2\sum_j\beta_j^2+\sum_{i,j}\alpha_i\beta_j\varepsilon_{ij},\qquad \lambda\approx\frac{\sum_{i,j}\alpha_i\beta_jy_{ij}}{\sum_i\alpha_i^2\sum_j\beta_j^2}.
$$
Replacing $\alpha_i$ and $\beta_j$ by $\hat\alpha_i=\bar y_{i\cdot}-\bar y_{\cdot\cdot}$ and $\hat\beta_j=\bar y_{\cdot j}-\bar y_{\cdot\cdot}$ gives $\hat\lambda=\sum_{i,j}\hat\alpha_i\hat\beta_jy_{ij}\big/\big(\sum_i\hat\alpha_i^2\sum_j\hat\beta_j^2\big)$, and $\mathrm{SS}_N=\sum_{i,j}(\hat\lambda\hat\alpha_i\hat\beta_j)^2$ is the sum of squares of the fitted nonadditivity term. The total sum of squares then splits into four parts:

$$
\mathrm{SS}_{\mathrm{T}}=\mathrm{SS}_A+\mathrm{SS}_B+\mathrm{SS}_N+\mathrm{SS}_{\mathrm{E}},\qquad ab-1=(a-1)+(b-1)+1+(ab-a-b).
$$

**Theorem 6.4.1** Under the additive model, $\mathrm{SS}_N/\sigma^2\sim\chi^2_1$ and $\mathrm{SS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{ab-a-b}$, and they are independent. Hence $F_0\sim F_{1,ab-a-b}$ under $H_0$.

**Proof** (Outline.) Let $\hat\gamma_{ij}=y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot}$ be the residuals of the additive model, so $\mathrm{SS}_{\mathrm{Res}}=\sum_{i,j}\hat\gamma_{ij}^2$, the squared length of the projection of $\boldsymbol{y}$ onto the $(a-1)(b-1)$-dimensional space $\mathcal{L}$ of arrays with zero row and column sums. For constants $c_i,d_j$ with $\sum_ic_i=\sum_jd_j=0$, not all zero, consider the linear form $f=\sum_{i,j}c_id_j\hat\gamma_{ij}=\sum_{i,j}c_id_jy_{ij}$ (the other terms of $\hat\gamma_{ij}$ cancel because $\sum c_i=\sum d_j=0$). The array $(c_id_j)$ lies in $\mathcal{L}$, $\operatorname{Var}(f)=\sigma^2\sum_ic_i^2\sum_jd_j^2$, and under $H_0$, $\mathbb{E}f=0$. Thus $\mathrm{SS}_f=f^2/(\sum_ic_i^2\sum_jd_j^2)$ is the squared length of the projection of $\boldsymbol{y}$ onto the direction $(c_id_j)$ within $\mathcal{L}$, and $\mathrm{SS}_{\mathrm{Res}}-\mathrm{SS}_f$ is the squared length of the projection onto its orthogonal complement in $\mathcal{L}$. So $\mathrm{SS}_f/\sigma^2$ and $(\mathrm{SS}_{\mathrm{Res}}-\mathrm{SS}_f)/\sigma^2$ are independent central $\chi^2$ variables with $1$ and $(a-1)(b-1)-1=ab-a-b$ degrees of freedom. Tukey's statistic takes $c_i=\hat\alpha_i$ and $d_j=\hat\beta_j$, which are random. But the three sets of linear forms $\hat\alpha_i$, $\hat\beta_j$ and $\hat\gamma_{ij}$ are projections onto mutually orthogonal subspaces, hence independent; the conditional distribution of the $\hat\gamma_{ij}$ given the $\hat\alpha_i$ and $\hat\beta_j$ equals their unconditional distribution. Conditionally on the $\hat\alpha_i,\hat\beta_j$, the argument above applies with $\mathrm{SS}_f=\mathrm{SS}_N$, and since the resulting conditional distribution does not depend on the values of the $\hat\alpha_i,\hat\beta_j$, it is also the unconditional distribution. $\square$

For the impurity data, $\hat\lambda=0.074$, $\mathrm{SS}_N=0.0985$, and $\mathrm{SS}_{\mathrm{E}}=2.00-0.0985=1.9015$ on $15-3-5=7$ degrees of freedom, so

$$
F_0=\frac{0.0985}{1.9015/7}=0.36<F_{1,7,0.05}=5.59 .
$$
In R:

```r
library(additivityTests)
response <- matrix(impurity, nr = nlevels(temp))
tukey.test(response)
```

```text
Tukey test on 5% alpha-level:

Test statistic: 0.3627 
Critival value: 5.591 
The additivity hypothesis cannot be rejected.
```

(`Critival` is a misspelling in the package output.) There is no evidence of nonadditivity, and the additive analysis of Example 6.4.1 stands.

Two remarks put the test in perspective. First, the full model $y_{ijk}=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}+\varepsilon_{ijk}$ allows the whole set of interactions, with $(a-1)(b-1)$ degrees of freedom, whereas Tukey's model allows only a one-degree-of-freedom subset of them, interaction proportional to $\alpha_i\beta_j$. Failure to reject $H_0$ does not prove additivity; it shows only that this particular kind of interaction is not detected. Tukey's test can be applied directly to the randomized block model, where it checks the assumption of no treatment-by-block interaction. Second, when $H_0$ is not rejected, we proceed with the additive model, keeping in mind the difference between the factorial and the block setting described in Section 6.4.4. When it is rejected, a transformation of the response (often a logarithm, which turns multiplicative effects into additive ones) frequently removes the nonadditivity.

The test needs $ab-a-b\ge1$ error degrees of freedom. For a $2\times2$ experiment without replication, $ab-a-b=0$: the three degrees of freedom are used up by $A$, $B$ and the single interaction contrast, which coincides with Tukey's one degree of freedom (with two levels, every interaction is of the form $\lambda\alpha_i\beta_j$). Tukey's test is then not available, and one must simply assume that there is no interaction, or replicate the experiment.

## 6.5. Experiments with Three Factors

With three factors, $A$ with $a$ levels, $B$ with $b$ levels and $C$ with $c$ levels, the goals are again to evaluate the effects of the factors and to find the best combination. The possible effects are the three main effects $A$, $B$, $C$, the three two-factor interactions $AB$, $AC$, $BC$, and the three-factor interaction $ABC$, which says that the two-factor interaction of two of the factors changes with the level of the third. Designs for this situation include OFAT, the full factorial design, and designs such as Latin squares that use fewer runs under additional assumptions. The full factorial design with $n$ replicates, run as a CRD, has the model

$$
Y_{ijkl}=\mu+\alpha_i+\beta_j+\delta_k+(\alpha\beta)_{ij}+(\alpha\delta)_{ik}+(\beta\delta)_{jk}+(\alpha\beta\delta)_{ijk}+\varepsilon_{ijkl},\qquad \varepsilon_{ijkl}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
with every effect summing to zero over each of its indices, and the analysis of variance extends the two-way table:

| Source | df | $\mathbb{E}[\mathrm{MS}]$ (fixed effects) | $F_0$ |
|---|---|---|---|
| $A$ | $a-1$ | $\sigma^2+\frac{bcn\sum\alpha_i^2}{a-1}$ | $\mathrm{MS}_A/\mathrm{MS}_{\mathrm{E}}$ |
| $B$ | $b-1$ | $\sigma^2+\frac{acn\sum\beta_j^2}{b-1}$ | $\mathrm{MS}_B/\mathrm{MS}_{\mathrm{E}}$ |
| $C$ | $c-1$ | $\sigma^2+\frac{abn\sum\delta_k^2}{c-1}$ | $\mathrm{MS}_C/\mathrm{MS}_{\mathrm{E}}$ |
| $AB$ | $(a-1)(b-1)$ | $\sigma^2+\frac{cn\sum(\alpha\beta)_{ij}^2}{(a-1)(b-1)}$ | $\mathrm{MS}_{AB}/\mathrm{MS}_{\mathrm{E}}$ |
| $AC$ | $(a-1)(c-1)$ | $\sigma^2+\frac{bn\sum(\alpha\delta)_{ik}^2}{(a-1)(c-1)}$ | $\mathrm{MS}_{AC}/\mathrm{MS}_{\mathrm{E}}$ |
| $BC$ | $(b-1)(c-1)$ | $\sigma^2+\frac{an\sum(\beta\delta)_{jk}^2}{(b-1)(c-1)}$ | $\mathrm{MS}_{BC}/\mathrm{MS}_{\mathrm{E}}$ |
| $ABC$ | $(a-1)(b-1)(c-1)$ | $\sigma^2+\frac{n\sum(\alpha\beta\delta)_{ijk}^2}{(a-1)(b-1)(c-1)}$ | $\mathrm{MS}_{ABC}/\mathrm{MS}_{\mathrm{E}}$ |
| Error | $abc(n-1)$ | $\sigma^2$ | |
| Total | $abcn-1$ | | |

Each sum of squares is $n$ times the number of observations sharing a given estimated effect, times the sum of the squared estimated effects; for instance $\mathrm{SS}_A=bcn\sum_i(\bar y_{i\cdot\cdot\cdot}-\bar y_{\cdot\cdot\cdot\cdot})^2$. The number of runs, $abcn$, grows quickly; at least two replicates ($n\ge2$) are needed to test the three-factor interaction.

**Example 6.5.1** A soft drink bottler is interested in obtaining more uniform fill heights in the bottles produced by the manufacturing process. The filling machine should fill each bottle to the correct target height, but in practice there is variation around this target, and the bottler would like to understand its sources better and eventually reduce it. The process engineer can control three variables during the filling process: the percent carbonation ($A$, which is difficult to control in production; 3 levels: $10$, $12$, $14\%$), the operating pressure in the filler ($B$; 2 levels: $25$, $30$ psi) and the line speed in bottles produced per minute ($C$; 2 levels: $200$, $250$). Two replicates of the full factorial design are run, so all $3\times2\times2\times2=24$ runs are taken in random order. The response is the average deviation from the target fill height observed in a production run of bottles at each set of conditions (negative values are fill heights below the target):

| Carbonation | 25 psi, 200 | 25 psi, 250 | 30 psi, 200 | 30 psi, 250 | $y_{i\cdot\cdot\cdot}$ |
|---|---|---|---|---|---|
| $10\%$ | $-3,\ -1$ | $-1,\ 0$ | $-1,\ 0$ | $1,\ 1$ | $-4$ |
| $12\%$ | $0,\ 1$ | $2,\ 1$ | $2,\ 3$ | $6,\ 5$ | $20$ |
| $14\%$ | $5,\ 4$ | $7,\ 6$ | $7,\ 9$ | $10,\ 11$ | $59$ |
| $B\times C$ totals $y_{\cdot jk\cdot}$ | $6$ | $15$ | $20$ | $34$ | $y_{\cdot\cdot\cdot\cdot}=75$ |

The pressure totals are $y_{\cdot j\cdot\cdot}=21$ and $54$.

```r
summary(aov(deviation ~ carbonation * pressure * speed, data = Bottle))
```

```text
                           Df Sum Sq Mean Sq F value   Pr(>F)    
carbonation                 2 252.75  126.38 178.412 1.19e-09 ***
pressure                    1  45.38   45.38  64.059 3.74e-06 ***
speed                       1  22.04   22.04  31.118  0.00012 ***
carbonation:pressure        2   5.25    2.63   3.706  0.05581 .  
carbonation:speed           2   0.58    0.29   0.412  0.67149    
pressure:speed              1   1.04    1.04   1.471  0.24859    
carbonation:pressure:speed  2   1.08    0.54   0.765  0.48687    
Residuals                  12   8.50    0.71                     
```

The degrees of freedom follow the general table: $2$, $1$, $1$ for the main effects, $2\cdot1=2$, $2\cdot1=2$ and $1\cdot1=1$ for the two-factor interactions, $2\cdot1\cdot1=2$ for the three-factor interaction, and $abc(n-1)=12$ for error, adding up to $23=abcn-1$. Each $F$ value is the mean square over $\mathrm{MS}_{\mathrm{E}}=0.708$. All three main effects are highly significant. The carbonation–pressure interaction has $p=0.056$, which indicates some interaction; the other interactions are not significant.

![Soft drink bottling: main effect plots for carbonation, pressure and line speed (observations and level means), and the three two-factor interaction plots](./plots/bottling-effects.py)

The plots show that the fill height deviation increases with carbonation, with pressure and with line speed. The carbonation–pressure interaction plot shows that the increase with carbonation is somewhat steeper at the higher pressure: the means at $25$ psi are $-1.25$, $1.00$, $5.50$ for the three carbonation levels, at $30$ psi $0.25$, $4.00$, $9.25$. The other interaction plots have nearly parallel lines.

The results lead to operating recommendations. A high line speed is preferred because it maximizes the production rate, and the carbonation is difficult to control. The low operating pressure ($25$ psi) is then recommended: it gives deviations closer to the target, and it reduces the sensitivity of the fill height to carbonation. At high speed and low pressure, the average fill height deviations for $10$, $12$ and $14\%$ carbonation are $-0.5$, $1.5$ and $6.5$, so the process should run at a low percent carbonation, around $10$–$12\%$, and the variability of the carbonation levels should be controlled; this can ultimately be achieved by improving temperature control during manufacturing. As always, the analysis is not complete without examining the residuals ([3.8.5](/3.8.5)).

When an experiment has one treatment factor but two nuisance factors to control, a full factorial in all three is wasteful. For example, in testing the abrasion resistance of rubber-covered fabric, four materials are compared by the loss in weight over a period of time, but the tester has four positions and must be set up four times (four applications), and both may affect the result. A Latin square design arranges the four materials in a $4\times4$ array of positions and applications so that each material appears once in each row and each column, controlling both sources of nuisance variation with only $16$ runs. Such designs, and their extensions to more nuisance factors, are treated in later chapters.

## Summary {#summary}

The two-way ANOVA for a balanced factorial design run as a CRD (model $y_{ijk}=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}+\varepsilon_{ijk}$, Theorem 6.3.1):

| Source | SS | df | $\mathbb{E}[\mathrm{MS}]$ | $F_0$ |
|---|---|---|---|---|
| $A$ | $bn\sum_i(\bar y_{i\cdot\cdot}-\bar y_{\cdot\cdot\cdot})^2$ | $a-1$ | $\sigma^2+\frac{bn\sum\alpha_i^2}{a-1}$ | $\mathrm{MS}_A/\mathrm{MS}_{\mathrm{E}}$ |
| $B$ | $an\sum_j(\bar y_{\cdot j\cdot}-\bar y_{\cdot\cdot\cdot})^2$ | $b-1$ | $\sigma^2+\frac{an\sum\beta_j^2}{b-1}$ | $\mathrm{MS}_B/\mathrm{MS}_{\mathrm{E}}$ |
| $AB$ | $n\sum_{i,j}(\bar y_{ij\cdot}-\bar y_{i\cdot\cdot}-\bar y_{\cdot j\cdot}+\bar y_{\cdot\cdot\cdot})^2$ | $(a-1)(b-1)$ | $\sigma^2+\frac{n\sum(\alpha\beta)_{ij}^2}{(a-1)(b-1)}$ | $\mathrm{MS}_{AB}/\mathrm{MS}_{\mathrm{E}}$ |
| Error | $\sum_{i,j,k}(y_{ijk}-\bar y_{ij\cdot})^2$ | $ab(n-1)$ | $\sigma^2$ | |
| Total | $\sum_{i,j,k}(y_{ijk}-\bar y_{\cdot\cdot\cdot})^2$ | $abn-1$ | | |

- OFAT needs $a+b-1$ runs but cannot estimate interaction and may miss the optimum; the full factorial needs $abn$ runs, estimates all main effects and interactions, and uses every observation for every main effect.
- No interaction $\iff$ all $(\alpha\beta)_{ij}=0$ $\iff$ parallel lines in the interaction plot of the true means (Proposition 6.2.1). The model has $ab+1$ free parameters (Proposition 6.2.3). With quantitative factors, interaction is a product term that twists the response surface.
- Randomization makes the factors orthogonal to unmeasured variables; balance makes the factors orthogonal to each other ($n_{ij}N=n_{i\cdot}n_{\cdot j}$), so that the sums of squares separate.
- Test the interaction first. If it is significant, compare the levels of one factor at each level of the other, using the cell means and $\mathrm{MS}_{\mathrm{E}}$ of the full model.
- Without replication ($n=1$): assume the additive model (Definition 6.4.1), use the interaction sum of squares as the residual with $(a-1)(b-1)$ df, and check additivity with Tukey's one-degree-of-freedom test ($F_{1,ab-a-b}$, Definition 6.4.3), which is unavailable for $2\times2$.

| Additive model in | CRD (unreplicated factorial) | RCBD |
|---|---|---|
| Factors | two treatment factors | treatment factor and block (nuisance) factor |
| Randomization | all $ab$ runs | within blocks |
| Additivity | assumption about the process | design assumption: no treatment-by-block interaction |
| $F$ for $B$ | valid test | rough indication of the usefulness of blocking |

- Three factors: $7$ effects ($A,B,C,AB,AC,BC,ABC$) with degrees of freedom products of $(\text{levels}-1)$; error $abc(n-1)$.

## Questions

1. A balanced two-factor experiment with $a=3$, $b=4$ and $n=3$ gave $\mathrm{SS}_A=120$, $\mathrm{SS}_B=210$, $\mathrm{SS}_{AB}=96$ and $\mathrm{SS}_{\mathrm{T}}=642$. Complete the ANOVA table and state the conclusions at $\alpha=0.05$.

   **Answer** $\mathrm{SS}_{\mathrm{E}}=642-120-210-96=216$ with $ab(n-1)=24$ df, so $\mathrm{MS}_{\mathrm{E}}=9$. $A$: df $2$, $\mathrm{MS}=60$, $F_0=6.67$; $B$: df $3$, $\mathrm{MS}=70$, $F_0=7.78$; $AB$: df $6$, $\mathrm{MS}=16$, $F_0=1.78$; total df $35$. The critical values are $F_{2,24,0.05}=3.40$, $F_{3,24,0.05}=3.01$ and $F_{6,24,0.05}=2.51$. The interaction is not significant ($p\approx0.15$), and both main effects are significant ($p\approx0.005$ and $p\approx0.0008$), so they can be interpreted as averaged effects.

2. The yield of penicillin $y$ depends on the reaction temperature $A$ ($30$, $35$, $40\,^\circ\mathrm{C}$) and the reaction time $T$ ($30$, $40$, $50$ h). A full factorial experiment with two replicates gave the yields below. Test the main effects and the interaction at $\alpha=0.05$ and choose the best combination.

   | Time \ Temperature | $30^\circ\mathrm{C}$ | $35^\circ\mathrm{C}$ | $40^\circ\mathrm{C}$ |
   |---|---|---|---|
   | 30 h | 10, 12 | 14, 18 | 12, 12 |
   | 40 h | 16, 17 | 20, 24 | 18, 20 |
   | 50 h | 19, 24 | 28, 32 | 16, 18 |

   **Answer** $y_{\cdot\cdot\cdot}=330$, $N=18$, $\sum y^2=6622$, so $\mathrm{SS}_{\mathrm{T}}=6622-330^2/18=572$. Temperature totals $98$, $136$, $96$: $\mathrm{SS}_A=(98^2+136^2+96^2)/6-6050=169.33$. Time totals $78$, $115$, $137$: $\mathrm{SS}_T=296.33$. Cell totals give $\mathrm{SS}_{\mathrm{Subtotals}}=529$, so $\mathrm{SS}_{AT}=529-169.33-296.33=63.33$ and $\mathrm{SS}_{\mathrm{E}}=572-529=43$ on $9$ df, $\mathrm{MS}_{\mathrm{E}}=4.78$. Then $F_A=84.67/4.78=17.72$ ($p=0.0008$), $F_T=148.17/4.78=31.01$ ($p<0.001$), both above $F_{2,9,0.05}=4.26$, and $F_{AT}=15.83/4.78=3.31$ ($p=0.063$) below $F_{4,9,0.05}=3.63$. Both main effects are significant and the interaction is not (though borderline). The yield is highest at $35^\circ\mathrm{C}$ (mean $22.67$) and increases with time (means $13$, $19.17$, $22.83$), so the best combination is $35^\circ\mathrm{C}$ and $50$ h, which also has the largest cell mean, $30$. Given the borderline interaction (at $40^\circ\mathrm{C}$ the yield drops after $40$ h), the conclusion should be confirmed by comparing the cell means directly.

3. Prove that in the main-effect–interaction model the number of free parameters is $ab+1$, and explain why the error has $ab(n-1)$ degrees of freedom.

   **Answer** See Proposition 6.2.3: $(a+1)(b+1)+1$ parameters minus $a+b+1$ independent constraints (the $a$ row and $b$ column constraints on the interactions share one dependence) gives $ab+1$; equivalently, the means model has $ab$ cell means and $\sigma^2$. The fitted values are the $ab$ cell means, so the residuals satisfy one linear constraint (zero sum) in each cell, leaving $n-1$ free residuals per cell and $ab(n-1)$ in total.

4. A process has two factors with $4$ and $5$ levels. How many runs does OFAT need, and how many does a full factorial with $2$ replicates need? Give two reasons why the factorial may be preferred despite the larger number of runs.

   **Answer** OFAT: $a+b-1=8$ runs (without replication). The factorial: $abn=40$ runs. Reasons: the factorial can estimate and test the interaction, and OFAT cannot, so OFAT may settle on a suboptimal combination when the factors interact; and in the factorial every observation contributes to the estimate of each main effect, so the main effects are estimated with replication, averaged over the levels of the other factor, and the conclusions hold over the whole region rather than along two lines.

5. An unreplicated two-factor experiment has two levels of each factor. Can Tukey's test help decide whether interaction is present?

   **Answer** No. With $a=b=2$, $ab-1=3$ degrees of freedom are taken by $A$, $B$ and the one-degree-of-freedom nonadditivity term, leaving $ab-a-b=0$ for error. With two levels per factor, the single interaction contrast is itself of the form $\lambda\alpha_i\beta_j$, so the interaction cannot be separated from the error at all; one must assume it absent or replicate.

6. A wheat variety trial compares $a=5$ varieties in $b=4$ fields, each field divided into $5$ plots with the varieties randomized within each field. Another experiment studies $5$ varieties at $4$ fertilizer levels with one plot per combination, all $20$ combinations randomized over a uniform field. Both are analyzed with the additive model. Explain the differences in interpretation.

   **Answer** The first is an RCBD: the field is a block (nuisance) factor, randomization happens only within fields, additivity is the design assumption that the varieties rank the same in every field, and the $F$ ratio for fields only indicates whether blocking reduced the error. The second is an unreplicated factorial run as a CRD: both variety and fertilizer are treatment factors of interest, additivity is an assumption about the biology (no variety-by-fertilizer interaction) that may well fail, the test for fertilizer is a valid test, and Tukey's test (with $20-5-4=11$ error df) can check the additivity assumption.

7. Why does random assignment of the treatments make the least squares estimates of the treatment effects nearly unbiased, even when unmeasured variables $Z$ affect the response?

   **Answer** With an omitted $Z$, $\mathbb{E}[\hat{\boldsymbol{\beta}}]=\boldsymbol{\beta}+(X^{\mathsf T}X)^{-1}X^{\mathsf T}Z\boldsymbol{\gamma}$, so the bias is driven by the (centered) cross products of the treatment indicators with $Z$. Random assignment makes the treatment received independent of the values of $Z$, so these cross products have expectation zero over the randomization and are small in a given experiment; the bias averages to zero, and its random part is accounted for in the error, which is what the CRD analysis assumes.
