---
title: Latin Squares and Related Designs
description: Blocking in two directions with the Latin square design (randomization, model, ANOVA, the rocket propellant example, advantages and limitations); replicated Latin squares in three cases; crossover designs as replicated Latin squares, carryover effects and designs balanced for them; orthogonal Latin squares, their existence and construction, and the Graeco-Latin square design.
---

The randomized complete block design of [3.8.7](/3.8.7) removes one source of nuisance variability by comparing the treatments within homogeneous blocks. Often there are two such sources at once: the runs of an experiment may use different batches of raw material and be made by different operators, or a tester may have several positions and need to be set up several times. Blocking on all combinations of two nuisance factors with a complete block for each combination would multiply the number of runs; the Latin square design controls both with the same number of runs as a single-factor experiment with $p$ replicates, by a clever restriction of the arrangement. The price is a strong assumption: the treatment and the two blocking factors must not interact.

This chapter develops the Latin square design and its relatives. Section 8.1 defines Latin squares, explains how they are randomized, and derives the analysis of variance from the additive three-factor model. Section 8.2 treats replicated Latin squares, which increase the error degrees of freedom; how they are analyzed depends on whether the levels of the blocking factors are reused in each replicate. Section 8.3 shows that the **crossover design** of clinical trials, already met in [3.6.8](/3.6.8), is a replicated Latin square, and adds carryover effects to the model. Section 8.4 adds a third blocking factor by superimposing two orthogonal Latin squares, a combinatorial object with a famous history, whose construction uses **finite fields** ([1.3.3](/1.3.3)). The ANOVA tools are those of [3.8.3](/3.8.3) and [3.8.6](/3.8.6): the Latin square model is the **additive model** with one more factor, and its sums of squares separate for the same reason of orthogonality.

## 8.1. The Latin Square Design

### 8.1.1. Two Nuisance Factors

The abrasion resistance of rubber-covered fabric is tested by measuring the loss in weight $Y$ over a period of time on a wear tester. Four materials $A$, $B$, $C$, $D$ are to be compared. The tester has four positions, which may wear the fabric differently, and it has to be set up four times (four applications), which may also differ. There is one treatment factor (material) and two **nuisance factors** (position and application), each with four levels. A full factorial in the three factors would need $4^3=64$ runs, but only $16$ specimens can be tested: one per position in each of the four applications. The design used assigns the materials as follows:

| Application \ Position | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | C | D | B | A |
| 2 | A | B | D | C |
| 3 | D | C | A | B |
| 4 | B | A | C | D |

Each material is tested once in each application and once in each position. So every application is a complete block for the materials, and so is every position: the design blocks in two directions at once. Differences between applications and differences between positions both cancel from the comparison of the material means.

### 8.1.2. Latin Squares and Their Randomization

**Definition 8.1.1 (Latin Square)** A **Latin square** of order $p$ is a $p\times p$ array of $p$ symbols (Latin letters) in which each symbol appears exactly once in each row and exactly once in each column. A Latin square is a **standard Latin square** if its first row and its first column are in the natural order $A, B, C, \dots$.

The simplest Latin square of each order is the cyclic one, whose row $i$ is the first row shifted $i-1$ places to the left; it is a standard square. The numbers of Latin squares grow quickly with the order:

| Order $p$ | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| Standard squares | 1 | 4 | 56 | 9408 |
| All Latin squares | 12 | 576 | 161280 | 812851200 |

Every Latin square of order $p$ can be brought to a unique standard square by permuting its columns so that the first row is in natural order and then permuting rows $2,\dots,p$ so that the first column is in natural order. Counting the permutations gives the relation $L_p=p!\,(p-1)!\,S_p$ between the number $L_p$ of all squares and the number $S_p$ of standard squares; for example $576=24\cdot6\cdot4$.

**Definition 8.1.2 (Latin Square Design)** A **Latin square design** compares $p$ treatments in the presence of two blocking factors, each with $p$ levels, called rows and columns. All $p^2$ combinations of the levels of the blocking factors are run once, and the treatments are assigned to them according to a Latin square, so that each treatment appears once in each row and once in each column. The randomization is restricted to preserve this structure (Proposition 8.1.1).

The design has three factors with the same number $p$ of levels and $N=p^2$ runs, a $1/p$ fraction of the $p^3$ factorial. Its features follow from the definition: two sources of nuisance variability are controlled simultaneously; the treatment assignment is balanced with respect to both nuisance factors; and the analysis is valid only if the three factors do not interact (Section 8.1.6). In industrial experimentation it is used less often than the RCBD, because two nuisance factors with exactly as many levels as there are treatments are not always available, but in agriculture (rows and columns of a field), in experiments over days and operators, and in crossover trials (Section 8.3) it is a standard design.

The ideal randomization would choose the square at random from the set of all Latin squares of the given order. A more practical scheme is the following.

1. Select a standard Latin square of order $p$ at random.
2. Randomly permute its columns.
3. Randomly permute its rows.
4. Assign the treatments to the Latin letters at random.

**Proposition 8.1.1** If the standard square in step 1 is chosen uniformly from all $S_p$ standard squares and the permutations in steps 2–4 are chosen uniformly and independently, the resulting square is uniformly distributed over all $L_p$ Latin squares of order $p$. So the practical scheme realizes the ideal randomization.

**Proof** The procedure chooses one of $S_p\,(p!)^3$ equally likely tuples (standard square, column, row and letter permutations). Fix a Latin square $L$ and count the tuples that produce it. Undoing the steps, we choose the letter relabeling ($p!$ ways) and which row of $L$ comes from the first row of the standard square ($p$ ways). The column permutation is then determined, since it must put that row in natural order, and so is the row permutation, since the first column of a standard square is in natural order and the entries of a column are distinct. The result is a standard square. Hence every $L$ is produced by exactly $p\cdot p!$ tuples, the same number for every $L$, and $L$ is uniform; incidentally $L_p=S_p(p!)^3/(p\cdot p!)=p!\,(p-1)!\,S_p$. $\square$

If instead one always starts from the same standard square (say the cyclic one), the design is restricted to the squares that can be reached from it by permutations of rows, columns and letters, which for $p\ge4$ is only part of all Latin squares. For the validity of the analysis this matters little, and many published plans do so; the R package `agricolae` generates randomized Latin squares directly:

```r
library(agricolae)
trt <- LETTERS[1:4]       # a vector of treatment labels, not a function
design3 <- design.lsd(trt, seed = 543)
book3 <- design3$book     # field book: plot, row, col, trt
print(design3$sketch)
```

```text
     [,1] [,2] [,3] [,4]
[1,] "B"  "C"  "A"  "D" 
[2,] "D"  "A"  "C"  "B" 
[3,] "C"  "D"  "B"  "A" 
[4,] "A"  "B"  "D"  "C" 
```

The field book `book3` lists the $16$ plots with their row, column and treatment (plot $101$ is row $1$, column $1$, treatment $B$, and so on), in the form in which the experiment is run and the data recorded.

### 8.1.3. The Model and Its Analysis

Let $y_{ijk}$ be the observation in row $i$, column $k$, which received treatment $j$. Only $p^2$ of the $p^3$ index triples occur: the Latin square determines $j$ from $(i,k)$.

**Definition 8.1.3 (Latin Square Model)** The effects model of a Latin square design is the completely additive model

$$
Y_{ijk}=\mu+\alpha_i+\tau_j+\beta_k+\varepsilon_{ijk},\qquad i,j,k\in\{1,\dots,p\},\quad \varepsilon_{ijk}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
where $(i,j,k)$ ranges over the $p^2$ cells of the square, $\alpha_i$ is the row effect, $\tau_j$ the treatment effect and $\beta_k$ the column effect, with $\sum_i\alpha_i=\sum_j\tau_j=\sum_k\beta_k=0$. The three factors do not interact.

Dots and bars have the usual meaning: $y_{i\cdot\cdot}$, $y_{\cdot j\cdot}$, $y_{\cdot\cdot k}$ are the totals of row $i$, treatment $j$ and column $k$, each a sum of $p$ observations; $y_{\cdot\cdot\cdot}$ is the grand total, and $\bar y_{i\cdot\cdot}=y_{i\cdot\cdot}/p$, $\bar y_{\cdot\cdot\cdot}=y_{\cdot\cdot\cdot}/N$.

The key property of the design is that the three factors are mutually orthogonal: each pair of them forms a complete two-way layout with one observation per cell (every row meets every column once, every row contains every treatment once, every column contains every treatment once). The analysis is therefore the analysis of the RCBD with one more blocking factor.

**Theorem 8.1.1 (ANOVA for the Latin Square)** In the model of Definition 8.1.3:

1. The least squares estimates are $\hat\mu=\bar y_{\cdot\cdot\cdot}$, $\hat\alpha_i=\bar y_{i\cdot\cdot}-\bar y_{\cdot\cdot\cdot}$, $\hat\tau_j=\bar y_{\cdot j\cdot}-\bar y_{\cdot\cdot\cdot}$, $\hat\beta_k=\bar y_{\cdot\cdot k}-\bar y_{\cdot\cdot\cdot}$, and the residuals are $e_{ijk}=y_{ijk}-\bar y_{i\cdot\cdot}-\bar y_{\cdot j\cdot}-\bar y_{\cdot\cdot k}+2\bar y_{\cdot\cdot\cdot}$.
2. The total sum of squares splits into orthogonal parts,

   $$
   \mathrm{SS}_{\mathrm{T}}=\mathrm{SS}_{\mathrm{Rows}}+\mathrm{SS}_{\mathrm{Columns}}+\mathrm{SS}_{\mathrm{Tr}}+\mathrm{SS}_{\mathrm{E}},\qquad p^2-1=(p-1)+(p-1)+(p-1)+(p-2)(p-1),
   $$
   with $\mathrm{SS}_{\mathrm{Tr}}=p\sum_j(\bar y_{\cdot j\cdot}-\bar y_{\cdot\cdot\cdot})^2=\frac1p\sum_jy_{\cdot j\cdot}^2-\frac{y_{\cdot\cdot\cdot}^2}{N}$, $\mathrm{SS}_{\mathrm{Rows}}$ and $\mathrm{SS}_{\mathrm{Columns}}$ defined in the same way from the row and column totals, $\mathrm{SS}_{\mathrm{T}}=\sum y_{ijk}^2-y_{\cdot\cdot\cdot}^2/N$, and $\mathrm{SS}_{\mathrm{E}}=\sum e_{ijk}^2$ (in practice obtained by subtraction).
3. $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+\frac{p\sum_j\tau_j^2}{p-1}$, similarly for rows and columns, and $\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2$ with $\mathrm{MS}_{\mathrm{E}}=\mathrm{SS}_{\mathrm{E}}/[(p-2)(p-1)]$.
4. Under $H_0\colon\tau_1=\cdots=\tau_p=0$,

   $$
   F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\sim F_{p-1,(p-2)(p-1)},
   $$
   and $H_0$ is rejected at level $\alpha$ when $F_0>F_{p-1,(p-2)(p-1),\alpha}$.

**Proof** Write the observations as a vector $\boldsymbol{y}\in\mathbb{R}^{p^2}$, one coordinate per cell. Let $\mathcal{V}_R$ be the space of vectors whose value depends only on the row, $u_i$, with $\sum_iu_i=0$; define $\mathcal{V}_T$ (treatments, values $v_j$) and $\mathcal{V}_C$ (columns, values $w_k$) in the same way. Each has dimension $p-1$ and is orthogonal to the constant vector $\boldsymbol{1}$. They are mutually orthogonal: for $u\in\mathcal{V}_R$ and $v\in\mathcal{V}_T$, the inner product is $\sum_{\text{cells}}u_iv_j=\sum_iu_i\sum_jv_j=0$, because row $i$ contains each treatment $j$ exactly once; the other two pairs are similar. The mean vector of the model lies in $\operatorname{span}\{\boldsymbol{1}\}\oplus\mathcal{V}_R\oplus\mathcal{V}_T\oplus\mathcal{V}_C$, a space of dimension $3p-2$, and the least squares fit is the orthogonal projection onto it, which is the sum of the projections onto the four orthogonal pieces. The projection onto $\mathcal{V}_T$ has value $\bar y_{\cdot j\cdot}-\bar y_{\cdot\cdot\cdot}$ in every cell of treatment $j$ (it is the one-way fit by treatment, centered), and similarly for rows and columns; this gives part 1, and the Pythagorean theorem gives part 2, with error dimension $p^2-(3p-2)=(p-1)(p-2)$. By **Cochran's theorem** ([3.8.3](/3.8.3)) the four squared lengths are independent, and each divided by $\sigma^2$ is a noncentral $\chi^2$ variable with the corresponding degrees of freedom and noncentrality equal to the squared length of the projection of the mean vector divided by $\sigma^2$. The mean vector projects onto $\mathcal{V}_T$ as $\tau_j$, with squared length $p\sum_j\tau_j^2$, and onto the error space as $\boldsymbol{0}$. This gives the expected mean squares in part 3 and, under $H_0$, the central $F$ distribution in part 4. $\square$

| Source | Sum of squares | df | Mean square | $F_0$ |
|---|---|---|---|---|
| Treatments | $\frac1p\sum_jy_{\cdot j\cdot}^2-\frac{y_{\cdot\cdot\cdot}^2}{N}$ | $p-1$ | $\frac{\mathrm{SS}_{\mathrm{Tr}}}{p-1}$ | $\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}$ |
| Rows | $\frac1p\sum_iy_{i\cdot\cdot}^2-\frac{y_{\cdot\cdot\cdot}^2}{N}$ | $p-1$ | $\frac{\mathrm{SS}_{\mathrm{Rows}}}{p-1}$ | |
| Columns | $\frac1p\sum_ky_{\cdot\cdot k}^2-\frac{y_{\cdot\cdot\cdot}^2}{N}$ | $p-1$ | $\frac{\mathrm{SS}_{\mathrm{Columns}}}{p-1}$ | |
| Error | by subtraction | $(p-2)(p-1)$ | $\frac{\mathrm{SS}_{\mathrm{E}}}{(p-2)(p-1)}$ | |
| Total | $\sum y_{ijk}^2-\frac{y_{\cdot\cdot\cdot}^2}{N}$ | $p^2-1$ | | |

As in the RCBD, the ratios $\mathrm{MS}_{\mathrm{Rows}}/\mathrm{MS}_{\mathrm{E}}$ and $\mathrm{MS}_{\mathrm{Columns}}/\mathrm{MS}_{\mathrm{E}}$ can be computed, but rows and columns are not assigned at random, so they only indicate whether blocking in each direction was worthwhile. Treatment means are compared with the multiple comparison methods of [3.8.4](/3.8.4), using $\mathrm{MS}_{\mathrm{E}}$ with $(p-2)(p-1)$ degrees of freedom and $p$ observations per treatment mean; the residuals $e_{ijk}$ are checked as in [3.8.5](/3.8.5).

### 8.1.4. Example: The Rocket Propellant Problem

**Example 8.1.1** An experimenter studies the effect of five formulations of a rocket propellant used in aircrew escape systems on the observed burning rate. Each formulation is mixed from a batch of raw material that is only large enough for five formulations to be tested, and the formulations are prepared by several operators who differ substantially in skill and experience. Batches and operators are two nuisance factors, each with five levels. The appropriate design tests each formulation exactly once in each batch of raw material and has each formulation prepared exactly once by each of the five operators: a $5\times5$ Latin square (here the cyclic one, with formulations $A$–$E$). The observed burning rates are

| Batch \ Operator | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | $A=24$ | $B=20$ | $C=19$ | $D=24$ | $E=24$ |
| 2 | $B=17$ | $C=24$ | $D=30$ | $E=27$ | $A=36$ |
| 3 | $C=18$ | $D=38$ | $E=26$ | $A=27$ | $B=21$ |
| 4 | $D=26$ | $E=31$ | $A=26$ | $B=23$ | $C=22$ |
| 5 | $E=22$ | $A=30$ | $B=20$ | $C=29$ | $D=31$ |

A first look plots the burning rate against each of the three factors in turn (the data frame `Rocket` holds the table above, with columns `Batch`, `Operator`, `Treat` and `Rate`; it is defined in the R source of the figure):

```r
par(mfcol = c(1, 3))
plot(Rate ~ Operator + Batch + Treat, Rocket, las = 1)
par(mfcol = c(1, 1))
```

![Rocket propellant Latin square: burning rates against batch, operator and formulation, with the level means; the formulation means spread most, the operator means less, the batch means least](./plots/rocket-factors.py)

The formulation totals are $143$, $101$, $112$, $149$, $130$ (means $28.6$, $20.2$, $22.4$, $29.8$, $26.0$ for $A$–$E$), the batch totals $111$, $134$, $130$, $128$, $132$ and the operator totals $107$, $143$, $121$, $130$, $134$; the grand total is $y_{\cdot\cdot\cdot}=635$ with $N=25$ and $\sum y_{ijk}^2=16805$. Hence $y_{\cdot\cdot\cdot}^2/N=16129$, $\mathrm{SS}_{\mathrm{T}}=676$,

$$
\mathrm{SS}_{\mathrm{Tr}}=\frac{143^2+101^2+112^2+149^2+130^2}{5}-16129=330,
$$
and in the same way $\mathrm{SS}_{\mathrm{Batches}}=68$, $\mathrm{SS}_{\mathrm{Operators}}=150$, so $\mathrm{SS}_{\mathrm{E}}=676-330-68-150=128$ on $(5-2)(5-1)=12$ degrees of freedom. In R:

```r
summary(aov(Rate ~ Treat + Batch + Operator, Rocket))
```

```text
          Df Sum Sq Mean Sq F value  Pr(>F)   
Treat      4    330   82.50   7.734 0.00254 **
Batch      4     68   17.00   1.594 0.23906   
Operator   4    150   37.50   3.516 0.04037 * 
Residuals 12    128   10.67                   
```

The formulations differ significantly in mean burning rate ($F_0=7.73$, $p=0.0025$). The operators differ too, so blocking on operators was useful. There is no strong evidence of a difference between batches of raw material; we were unnecessarily concerned about this source of variability. To see which formulations differ, **Tukey's method** ([3.8.4](/3.8.4)) with $q_{0.05}(5,12)=4.51$ gives the minimum significant difference $4.51\sqrt{10.67/5}=6.59$ between two formulation means. Ordered, the means are $D=29.8$, $A=28.6$, $E=26.0$, $C=22.4$, $B=20.2$: $D$ exceeds $B$ and $C$, and $A$ exceeds $B$ ($A-C=6.2$ falls just short); $E$ is not distinguished from any formulation.

:::

### 8.1.5. Was Blocking on Batches Necessary?

Since the batch effect is not significant, it is tempting to drop batches from the model and analyze the data as an RCBD with operators as blocks:

```r
summary(aov(Rate ~ Treat + Operator, Rocket))
```

```text
          Df Sum Sq Mean Sq F value  Pr(>F)   
Treat      4    330   82.50   6.735 0.00224 **
Operator   4    150   37.50   3.061 0.04738 * 
Residuals 16    196   12.25                   
```

The batch sum of squares and its $4$ degrees of freedom are pooled into the error: $196=68+128$ on $16=4+12$ df. Because $\mathrm{MS}_{\mathrm{Batches}}=17.0$ exceeds $\mathrm{MS}_{\mathrm{E}}=10.67$, pooling increases the error mean square to $12.25$, but the extra degrees of freedom lower the critical value, and here the $p$-value for treatments happens to be slightly smaller. Both analyses lead to the same conclusion. Still, the analysis should follow the design that was run. The batches were a recognized potential source of variability when the experiment was planned, and the treatments were randomized subject to the Latin square restriction; deciding after looking at the data which blocking factors to keep is a form of data snooping that distorts the error rate. Blocking on batches of raw material is usually a good idea: if batches had differed, the Latin square would have protected the comparison, and when they do not, the cost is only $4$ error degrees of freedom. The ratio $12.25/10.67\approx1.15$ estimates how much larger the error variance per observation would have been without the batch blocking; a design that achieves the same precision with fewer runs is more efficient (compare the efficiency of the RCBD relative to the CRD in [3.8.7](/3.8.7)).

### 8.1.6. Advantages and Limitations

When two kinds of heterogeneity, due either to the nature or to the arrangement of the experimental units, can be identified, the Latin square is an effective design for separating both sources of variation from the experimental error, at a cost of only $p^2$ runs. The disadvantages are the reverse side of this economy.

- Severe design constraints: the treatment and both blocking factors must have the same number of levels, and all $p^2$ row–column combinations must be available.
- No interactions are allowed: the design is valid only if there are no interactions among rows, columns and treatments. Because the Latin square is a $1/p$ fraction of the $p^3$ factorial, interactions cannot be estimated, and they are mixed with the main effects and the error. For example, a row-by-column interaction with $(p-1)^2$ degrees of freedom shares the contrasts that the analysis attributes to treatments ($p-1$ df) and to error ($(p-1)(p-2)$ df). If such an interaction is present, $\mathrm{MS}_{\mathrm{E}}$ is inflated and the treatment comparisons are biased.
- Small squares have few error degrees of freedom: the error has $(p-2)(p-1)$ degrees of freedom: $0$ for $p=2$, $2$ for $p=3$, $6$ for $p=4$, $12$ for $p=5$. With $p=3$ the critical value is $F_{2,2,0.05}=19.0$, so only very large treatment effects can be detected, and $\sigma^2$ is estimated very poorly. Squares smaller than $4\times4$ are therefore generally not used alone; they are replicated (Section 8.2).
- Large squares are rarely useful: beyond $p\approx10$ the two blocking factors must have many levels, and the blocks (rows and columns with $p$ units each) are no longer homogeneous, which defeats their purpose.

## 8.2. Replicated Latin Squares

### 8.2.1. Three Cases of Replication

The small number of error degrees of freedom makes it frequently desirable to replicate a Latin square. Consider a factory producing a product with $4$ machines and $4$ operators. Our interest is in the average time needed to produce each unit of the product, and the treatment is one of four production protocols. We call the rows of the square the machines and the columns the operators, and we replicate the Latin square $n=3$ times, once a week. The treatments are the same in each replicate; the question is whether the levels of the blocking factors remain the same across the replicated squares. There are three cases.

| Case | Rows | Columns | Example |
|---|---|---|---|
| 1 | the same in every replicate | the same in every replicate | the same machines and operators each week |
| 2 | new levels in each replicate | the same in every replicate | three factories with different machines, the same (traveling) operators |
| 3 | new levels in each replicate | new levels in each replicate | three factories, each with its own machines and operators |

In Case 2 and Case 3 the factor whose levels change is a **nested factor** ([3.8.1](/3.8.1)): "machine 1" of factory 1 and "machine 1" of factory 2 are different machines, and the machine effect is defined only within its replicate. We write $\alpha_{i(l)}$ for the effect of row $i$ within replicate $l$. Let $y_{ijkl}$ be the observation in row $i$, with treatment $j$, in column $k$, in replicate $l$; there are $N=np^2$ observations, and $\gamma_l$ denotes the effect of replicate $l$ (week or factory).

### 8.2.2. Case 1: Both Blocking Factors Reused

If the same machines and operators are used every week, rows, columns and treatments have the same parameters in all replicates, as in a single Latin square, and the replicate is one more additive factor:

$$
Y_{ijkl}=\mu+\alpha_i+\tau_j+\beta_k+\gamma_l+\varepsilon_{ijkl}.
$$
Each row, column and treatment total is now a sum of $np$ observations:

| Source | Sum of squares | df | Mean square | $F_0$ |
|---|---|---|---|---|
| Treatments (protocol) | $\frac{1}{np}\sum_{j=1}^py_{\cdot j\cdot\cdot}^2-\frac{y_{\cdot\cdot\cdot\cdot}^2}{N}$ | $p-1$ | $\frac{\mathrm{SS}_{\mathrm{Tr}}}{p-1}$ | $\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}$ |
| Rows (machine) | $\frac{1}{np}\sum_{i=1}^py_{i\cdot\cdot\cdot}^2-\frac{y_{\cdot\cdot\cdot\cdot}^2}{N}$ | $p-1$ | $\frac{\mathrm{SS}_{\mathrm{Rows}}}{p-1}$ | |
| Columns (operator) | $\frac{1}{np}\sum_{k=1}^py_{\cdot\cdot k\cdot}^2-\frac{y_{\cdot\cdot\cdot\cdot}^2}{N}$ | $p-1$ | $\frac{\mathrm{SS}_{\mathrm{Columns}}}{p-1}$ | |
| Replicates (week) | $\frac{1}{p^2}\sum_{l=1}^ny_{\cdot\cdot\cdot l}^2-\frac{y_{\cdot\cdot\cdot\cdot}^2}{N}$ | $n-1$ | $\frac{\mathrm{SS}_{\mathrm{Rep}}}{n-1}$ | |
| Error | by subtraction | $(p-1)[n(p+1)-3]$ | $\frac{\mathrm{SS}_{\mathrm{E}}}{(p-1)[n(p+1)-3]}$ | |
| Total | $\sum_{i,j,k,l}y_{ijkl}^2-\frac{y_{\cdot\cdot\cdot\cdot}^2}{N}$ | $np^2-1$ | | |

The error degrees of freedom are $np^2-1-3(p-1)-(n-1)=(p-1)[n(p+1)-3]$; they grow very rapidly when Latin squares are replicated. In the factory example a single square has $6$ error df, while three replicates have $3\cdot12=36$.

### 8.2.3. Case 2: One Blocking Factor Nested in Replicates

Suppose the replicates are three factories: the machines are different in each factory, but the operators stay the same. The machines are nested in the replicates (factories), and the model is

$$
Y_{ijkl}=\mu+\alpha_{i(l)}+\tau_j+\beta_k+\gamma_l+\varepsilon_{ijkl}.
$$
The machine sum of squares is now computed within each factory and pooled:

$$
\mathrm{SS}_{\mathrm{Rows(Rep)}}=\frac1p\sum_{l=1}^n\sum_{i=1}^py_{i\cdot\cdot l}^2-\sum_{l=1}^n\frac{y_{\cdot\cdot\cdot l}^2}{p^2},
$$
with $n(p-1)$ degrees of freedom: $p-1$ for the machines of each of the $n$ factories. The remaining lines are as in Case 1:

| Source | df |
|---|---|
| Treatments (protocol) | $p-1$ |
| Rows within replicates (machine within factory) | $n(p-1)$ |
| Columns (operator) | $p-1$ |
| Replicates (factory) | $n-1$ |
| Error | $(p-1)(np-2)$ |
| Total | $np^2-1$ |

Together, the replicates and the nested rows account for the $np-1$ degrees of freedom among the $np$ distinct machines: $np-1=n(p-1)+(n-1)$. In the factory example the error has $3\cdot10=30$ df. The roles of rows and columns can of course be exchanged, with model $Y_{ijkl}=\mu+\alpha_i+\tau_j+\beta_{k(l)}+\gamma_l+\varepsilon_{ijkl}$.

### 8.2.4. Case 3: Both Blocking Factors Nested in Replicates

If the three factories have different machines and different operators, both blocking factors are nested within the replicates:

$$
Y_{ijkl}=\mu+\alpha_{i(l)}+\tau_j+\beta_{k(l)}+\gamma_l+\varepsilon_{ijkl}.
$$
Both $\mathrm{SS}_{\mathrm{Rows(Rep)}}$ and $\mathrm{SS}_{\mathrm{Columns(Rep)}}=\frac1p\sum_l\sum_ky_{\cdot\cdot kl}^2-\sum_ly_{\cdot\cdot\cdot l}^2/p^2$ have $n(p-1)$ degrees of freedom, and the error has

$$
np^2-1-(p-1)-2n(p-1)-(n-1)=(p-1)[n(p-1)-1]
$$
degrees of freedom, $3\cdot8=24$ in the example. In effect, the $n$ squares are analyzed separately for rows and columns and combined for treatments. This case also provides a comparison of the factories, through $\mathrm{SS}_{\mathrm{Rep}}$ on $n-1$ df.

### 8.2.5. Comparison of the Three Cases

| Case | Model | Error df | Example ($p=4$, $n=3$) |
|---|---|---|---|
| 1 | $\mu+\alpha_i+\tau_j+\beta_k+\gamma_l$ | $(p-1)[n(p+1)-3]$ | $36$ |
| 2 | $\mu+\alpha_{i(l)}+\tau_j+\beta_k+\gamma_l$ or $\mu+\alpha_i+\tau_j+\beta_{k(l)}+\gamma_l$ | $(p-1)(np-2)$ | $30$ |
| 3 | $\mu+\alpha_{i(l)}+\tau_j+\beta_{k(l)}+\gamma_l$ | $(p-1)[n(p-1)-1]$ | $24$ |

Every nested factor uses $(n-1)(p-1)$ more degrees of freedom than the corresponding crossed one, since its effects are estimated separately in each replicate. The choice between the cases is not a matter of analysis but of fact: it depends on whether the levels of a blocking factor are physically the same units in all replicates. Analyzing a Case 3 experiment as Case 1 would treat different machines that share a label as the same machine.

Replicating Latin squares also allows some interactions to be estimated that cannot be estimated from a single Latin square. The most useful is the treatment-by-replicate interaction, with $(p-1)(n-1)$ degrees of freedom taken from the error: it asks whether the treatment effects are the same in every replicate. In Case 3 the replicates are different factories with their own machines and operators, so this is a meaningful question (do the protocols rank the same in every factory?); in Case 1 the replicates are only weeks, and the interaction measures the consistency of the protocol effects over time.

## 8.3. Crossover Designs

### 8.3.1. Crossover Designs as Replicated Latin Squares

A **crossover design** ([3.6.8](/3.6.8)) uses the same experimental unit for several treatments in successive periods. The typical example is a clinical trial: there are subjects (human or animal) on whom a set of drugs is to be tested. Each subject receives every treatment, in an order determined by the design, so the treatments are compared within subjects. The main worry is **carryover effects**, residual effects of the treatment of one period on the response in the next, which a **washout period** between the periods is meant to remove.

The subjects are one blocking factor, and the periods (the order of treatment) are another. With $p$ treatments and $p$ periods, a group of $p$ subjects whose treatment sequences form a Latin square has each treatment once in each period and once for each subject. With more subjects, several such squares are used, and the result is a replicated Latin square. For two treatments and $10$ subjects, five $2\times2$ squares are used:

| Subject | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Period 1 | A | B | A | B | B | A | A | B | A | B |
| Period 2 | B | A | B | A | A | B | B | A | B | A |

Each square (subjects $1$–$2$, $3$–$4$, …) contains the sequences $AB$ and $BA$. The order (rows) is the same in all squares, while the subjects (columns) are different people in each square: this is Case 2 with the columns nested in the replicates.

| Source | df | df for this example |
|---|---|---|
| Replicates (squares) | $n-1$ | $4$ |
| Columns: subjects within squares | $n(p-1)$ | $5$ |
| Rows: order | $p-1$ | $1$ |
| Treatments: A vs. B | $p-1$ | $1$ |
| Error | $(p-1)(np-2)$ | $8$ |
| Total | $np^2-1$ | $19$ |

### 8.3.2. Example: The Dairy Cow Feeding Experiment

**Example 8.3.1** Three diets $A$, $B$ and $C$ are given to $6$ cows in three periods of six weeks each, after which the weight of the milk production is measured. In between the treatments a washout period is implemented; but since the whole experiment must be completed within one lactation, the total time available for treatment periods plus rest periods is limited. The treatments are the diets provided for the cows, and the cows and the periods are the blocking factors. The design uses two $3\times3$ Latin squares, cows $1$–$3$ and cows $4$–$6$:

| Period \ Cow | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | $A=38$ | $B=109$ | $C=124$ | $A=86$ | $B=75$ | $C=101$ |
| 2 | $B=25$ | $C=86$ | $A=72$ | $C=76$ | $A=35$ | $B=63$ |
| 3 | $C=15$ | $A=39$ | $B=27$ | $B=46$ | $C=34$ | $A=1$ |

![Dairy cow crossover experiment: milk yield of each cow over the three periods, marked by diet; yields fall steeply from period to period in both squares](./plots/diet-crossover.py)

The periods are common to both squares and the cows are nested in the squares, so this is Case 2 (with the columns nested). If we were not concerned about residual effects, the model would be

$$
Y_{ijk}=\mu+\alpha_i+\tau_j+\beta_k+\varepsilon_{ijk},\qquad i=1,2,3\ (\text{period}),\quad j=1,2,3\ (\text{diet}),\quad k=1,\dots,6\ (\text{cow}),
$$
where the cow effects $\beta_k$ absorb the square effect: the $6$ cows have $5$ df, $n(p-1)+(n-1)=4+1$.

```r
summary(aov(Yield ~ ., Diet))
```

```text
          Df Sum Sq Mean Sq F value   Pr(>F)    
Treat      2   2277    1138   11.05  0.00499 ** 
Period     2  11480    5740   55.70 2.02e-05 ***
Cow        5   5781    1156   11.22  0.00187 ** 
Residuals  8    824     103                     
```

The error has $(p-1)(np-2)=2\cdot4=8$ df. The diets differ significantly; the unadjusted diet means are $45.2$, $57.5$ and $72.7$ for $A$, $B$, $C$. The period effect is very large: milk production declines over the lactation, so blocking on periods is essential.

The period, meaning the order, is assumed the same across squares. What if some of the cows went through the experiment in spring and the others in summer or fall? Then the period effect has more meaning than simply the order, the period effect in the first square need not be the same as in the second, and we should move from Case 2 to Case 3 to estimate separate period effects within each square:

```r
Diet$Square <- factor(rep(c(1, 2), each = 3))
summary(aov(Yield ~ Treat + Cow + Square/Period, Diet))
```

```text
              Df Sum Sq Mean Sq F value  Pr(>F)   
Treat          2   2277  1138.4   8.376 0.01834 * 
Cow            5   5781  1156.2   8.507 0.01072 * 
Square:Period  4  11489  2872.3  21.134 0.00111 **
Residuals      6    815   135.9                   
```

The formula `Square/Period` expands to `Square + Square:Period`, periods nested in squares. The `Square` term itself does not appear: it is already contained in `Cow`, because the cows are nested in the squares. Periods within squares take $n(p-1)=2\cdot(3-1)=4$ df, and the error has $(p-1)[n(p-1)-1]=6$ df. The two period patterns are nearly the same here ($\mathrm{SS}$ $11489$ against $11480$), so the extra $2$ df buy almost nothing, and the conclusions about the diets are unchanged.

:::

### 8.3.3. Carryover Effects

What if the treatment a cow was given first is a really bad treatment? Its effect could carry over into the next period and hurt the second treatment, if the washout period is not long enough. The measurement at one point is then not a direct reflection of the current treatment, but may also be influenced by the previous treatment. The remedy is to adjust the treatment means for the residual effects, by adding to the model a source called the residual treatment: the treatment received in the previous period, with an extra level `0` for period $1$, where there is no previous treatment.

| Cow | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Residual treatment in period 2 | $A$ | $B$ | $C$ | $A$ | $B$ | $C$ |
| Residual treatment in period 3 | $B$ | $C$ | $A$ | $C$ | $A$ | $B$ |

The factor `ResTrt` has four levels ($0$, $A$, $B$, $C$), but level $0$ occurs exactly in period $1$, so once periods are in the model it contributes only $4-1-1=2$ degrees of freedom: the differences among the carryover effects of $A$, $B$ and $C$. With carryover, the model becomes $Y=\mu+\alpha_{\text{period}}+\tau_{\text{direct}}+\beta_{\text{cow}}+\lambda_{\text{previous treatment}}+\varepsilon$.

Direct and carryover effects are not orthogonal: which cow received which diet before which other diet is tied to the treatment assignment. The **sequential sums of squares** ([3.3.9](/3.3.9)) therefore depend on the order in which the terms enter the model, and we must decide which **extra sum of squares** answers which question.

```r
anova(lm(Yield ~ Period + Cow + Treat + ResTrt, Diet))
anova(lm(Yield ~ Period + Cow + ResTrt + Treat, Diet))
```

```text
           Df Sum Sq Mean Sq F value    Pr(>F)    
Period      2  11480    5740 165.380 5.66e-06 ***
Cow         5   5781    1156  33.313  0.000265 ***
Treat       2   2277    1138  32.799  0.000589 ***
ResTrt      2    616     308   8.877  0.016117 *  
Residuals   6    208      35                      
```

In the first order, $\mathrm{SS}(\text{Treat}\mid\text{Period},\text{Cow})=2276.8$ is the direct effect unadjusted for carryover, and $\mathrm{SS}(\text{ResTrt}\mid\text{Period},\text{Cow},\text{Treat})=616.2$ is the carryover adjusted for the direct effects. In the second order, $\mathrm{SS}(\text{ResTrt}\mid\text{Period},\text{Cow})=38.4$ and $\mathrm{SS}(\text{Treat}\mid\text{Period},\text{Cow},\text{ResTrt})=2854.6$. The residual sum of squares, $208.25$ on $6$ df ($\mathrm{MS}_{\mathrm{E}}=34.7$), is the same in both.

- To test for carryover effects, use the carryover adjusted for the direct treatment effects (first order): $F_0=308.1/34.7=8.88$ on $(2,6)$ df, $p=0.016$. There is evidence of carryover, so the washout periods were not long enough.
- To test for treatment effects with any carryover removed, use the direct effects adjusted for carryover (second order): $F_0=1427.3/34.7=41.1$ on $(2,6)$ df, $p=0.0003$. The diets differ, and adjusted for carryover the differences are even larger: the estimated direct effects of $A$, $B$, $C$ (relative to their average) are $-16.0$, $-2.3$ and $18.3$, against the unadjusted $-13.3$, $-0.9$ and $14.2$.

The $F$ value $32.8$ for `Treat` in the first table, computed from the unadjusted sum of squares, is not the right test of the direct effects when carryover is present. The price of the carryover model is that the error is left with only $6$ degrees of freedom. Note also that adjusting for carryover is possible only because the design is balanced in a special way (Section 8.3.4); and that a preliminary test for carryover is no substitute for an adequate washout period (compare the two-stage procedure discussed in [3.6.8](/3.6.8)).

### 8.3.4. Designs Balanced for Carryover Effects

A single $3\times3$ Latin square used as a crossover design, say subject sequences $ABC$, $BCA$, $CAB$, contains the ordered pairs ($A$ then $B$, …) $AB$, $BC$, $CA$, each twice, but never $BA$, $CB$ or $AC$. Then the carryover of $A$ always acts on $B$, and the carryover effect of $A$ cannot be distinguished from a peculiarity of $B$ following $A$. In the dairy experiment the second square (sequences $ACB$, $BAC$, $CBA$) supplies the missing pairs, and in the combined design all six ordered pairs of treatments occur twice and only twice. The two squares are in fact orthogonal (Section 8.4). This is an additional level of balance, for carryover effects.

**Definition 8.3.1 (Balance for Carryover Effects)** A crossover design in which every treatment is preceded equally often by each of the other treatments is **balanced for carryover effects**. A Latin square with this property, in which every ordered pair of distinct treatments occurs exactly once in consecutive periods of the same subject, is called a **Williams design**.

The statistical analysis is easier for a balanced design: the direct and carryover effects are still not orthogonal, but every direct treatment difference is estimated with the same precision, and the adjustments are simple. Balance with respect to residual effects can be achieved as follows.

- If the number of treatments is even, a suitable single Latin square suffices.
- If the number of treatments is odd, two Latin squares are required for balance.

**Proposition 8.3.1** Let $p$ be even and label the treatments $0,1,\dots,p-1$. Let the first subject receive the sequence $0,1,p-1,2,p-2,3,\dots,p/2$ (alternately counting up from the start and down from the end), and let subject $s$ receive that sequence with $s-1$ added modulo $p$, for $s=1,\dots,p$. The result is a Latin square balanced for carryover effects.

**Proof** The rows (periods) and columns (subjects) are Latin because the columns are cyclic shifts of one permutation. The consecutive differences of the first sequence, modulo $p$, are $1,-2,3,-4,\dots,\pm(p-1)$, which are congruent to $1,p-2,3,p-4,\dots$; for even $p$ these $p-1$ values are exactly the nonzero residues $1,\dots,p-1$, each once. Adding $s-1$ to the whole sequence preserves the differences, so the ordered pair $(a,b)$ with $b-a\equiv d$ occurs in subject $s$ where $a$ is followed by $a+d$; for each difference $d$ the $p$ subjects give the $p$ pairs $(a,a+d)$, one for each $a$. Hence every ordered pair of distinct treatments occurs exactly once. $\square$

For four treatments the construction gives, with $A,B,C,D$ for $0,1,2,3$:

| Period \ Subject | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | A | B | C | D |
| 2 | B | C | D | A |
| 3 | D | A | B | C |
| 4 | C | D | A | B |

The subject sequences $ABDC$, $BCAD$, $CDBA$, $DACB$ contain all $12$ ordered pairs once. For an odd number of treatments, one takes such a sequence and its mirror image, each with all its cyclic shifts; with five treatments this gives two $5\times5$ squares and $10$ subjects, and every ordered pair occurs twice, as in the dairy experiment with three treatments.

### 8.3.5. Disadvantages of Crossover Trials

Besides their benefits (each subject is its own control, so fewer subjects are needed), crossover trials have disadvantages:

- carryover effects, and period-by-treatment interaction;
- an increased burden on the individual patient, who receives all treatments;
- they are only possible for certain indications, chronic and stable conditions;
- drop-outs and missing values are more of a problem than in parallel group studies, since a subject who leaves after one period destroys the balance;
- the analysis is more complex;
- they are unsuitable for drugs with irreversible effects or very long half-lives;
- the interpretation of side effects may be complex.

Byron Jones and Michael G. Kenward, *Design and Analysis of Cross-Over Trials* (3rd ed., Chapman & Hall, 2014) is the standard reference; efficient designs for many settings can be generated with the R package `Crossover` (J. A. John, K. G. Russell and D. Whitaker, *Statistics in Medicine* 23 (2004), 2645–2658).

## 8.4. Graeco-Latin Squares

### 8.4.1. A Third Nuisance Factor

Return to the four machines, four operators and four production protocols of Section 8.2, and suppose that the $16$ runs of a Latin square must be completed in one week of four working days, four runs a day. A natural schedule runs machine $i$ with operator $i+d-1$ (modulo $4$) on day $d$, that is, one "diagonal" of the square per day. With the cyclic square

| Machine \ Operator | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | A | B | C | D |
| 2 | B | C | D | A |
| 3 | C | D | A | B |
| 4 | D | A | B | C |

Monday gets protocols $A,C,A,C$, Tuesday $B,D,B,D$, Wednesday $C,A,C,A$ and Thursday $D,B,D,B$. The treatments have become confounded with the days, an instance of **confounding** ([3.8.2](/3.8.2)): if days of the week are not all the same, the difference between $\{A,C\}$ and $\{B,D\}$ cannot be separated from the difference between Monday–Wednesday and Tuesday–Thursday. Two blocking factors are not enough; the day of the week must be included in the design as a third one.

A complete factorial in machine, operator, protocol and day would need $4^4=256$ runs. Conducting the entire Latin square on each day, that is, replicating it four times, would require $16\times4=64$ observations instead of $16$. What we need is a design in which each day sees each protocol, each machine and each operator exactly once: a Graeco-Latin square.

### 8.4.2. Orthogonal Latin Squares

**Definition 8.4.1 (Orthogonal Latin Squares)** Two Latin squares of order $p$ are **orthogonal Latin squares** if, when they are superimposed, each of the $p^2$ ordered pairs of symbols (one from each square) appears exactly once. A **Graeco-Latin square** (also called an Euler square) is the superposition of two orthogonal Latin squares, the symbols of the first written as Latin letters and those of the second as Greek letters. A set of Latin squares of order $p$ that are pairwise orthogonal is a set of **mutually orthogonal Latin squares**.

For example, the following $4\times4$ Graeco-Latin square superimposes a Latin square in $A,B,C,D$ and an orthogonal one in $\alpha,\beta,\gamma,\delta$; each Latin letter meets each Greek letter exactly once:

| Row \ Column | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | $A\alpha$ | $B\beta$ | $C\gamma$ | $D\delta$ |
| 2 | $B\delta$ | $A\gamma$ | $D\beta$ | $C\alpha$ |
| 3 | $C\beta$ | $D\alpha$ | $A\delta$ | $B\gamma$ |
| 4 | $D\gamma$ | $C\delta$ | $B\alpha$ | $A\beta$ |

![A 4 x 4 Latin square, an orthogonal mate in Greek letters, and their superposition, the Graeco-Latin square in which every Latin-Greek pair occurs exactly once](./plots/latin-squares.py)

Not every Latin square has an orthogonal mate. The cyclic square of even order has none, which is why the diagonal schedule above failed for every assignment of days. How many mutually orthogonal squares can there be?

**Theorem 8.4.1** A set of mutually orthogonal Latin squares of order $p\ge2$ contains at most $p-1$ squares.

**Proof** Renaming the symbols of a square does not affect orthogonality, so we may assume that every square of the set has first row $1,2,\dots,p$. Consider the cell in row $2$, column $1$. Its entry in each square differs from $1$, because column $1$ already has $1$ in row $1$. Its entries in two different squares are different: if both were $s$, the pair $(s,s)$ would occur in cell $(2,1)$ and also in cell $(1,s)$, where both first rows have $s$, contradicting orthogonality. So the entries of cell $(2,1)$ in the squares of the set are distinct elements of $\{2,\dots,p\}$, and there are at most $p-1$ squares. $\square$

**Theorem 8.4.2** If $q$ is a prime power, there are $q-1$ mutually orthogonal Latin squares of order $q$.

**Proof** Let $\mathbb{F}_q$ be the **finite field** with $q$ elements ([1.3.3](/1.3.3)); index the rows and columns by its elements. For each $\lambda\in\mathbb{F}_q\setminus\{0\}$ define the square $L_\lambda(x,y)=\lambda x+y$. For fixed $x$ the map $y\mapsto\lambda x+y$ is a bijection, and for fixed $y$ so is $x\mapsto\lambda x+y$ (since $\lambda\ne0$), so $L_\lambda$ is a Latin square. For $\lambda\ne\mu$ and any pair of symbols $(s,t)$, the system $\lambda x+y=s$, $\mu x+y=t$ has the unique solution $x=(s-t)/(\lambda-\mu)$, $y=s-\lambda x$, so the pair $(s,t)$ occurs in exactly one cell: $L_\lambda$ and $L_\mu$ are orthogonal. $\square$

For a prime $p$ the field is just arithmetic modulo $p$, and $L_\lambda(x,y)=\lambda x+y \bmod p$. For $p=4$ one uses $\mathbb{F}_4$, not arithmetic modulo $4$ (which is not a field); the three squares it gives include the Latin square of the table above.

Euler studied these squares in 1782 through the problem of the $36$ officers: six regiments each send six officers of six different ranks; can they be arranged in a $6\times6$ square so that each row and each column contains one officer of each rank and one of each regiment? This asks for a Graeco-Latin square of order $6$. Euler could not find one and conjectured that none exists for any order $p\equiv2\pmod4$. Tarry confirmed in 1900, by exhaustive search, that there is no Graeco-Latin square of order $6$; but Bose, Shrikhande and Parker showed in 1959–1960 that Euler's conjecture is otherwise false.

**Theorem 8.4.3 (Bose–Shrikhande–Parker)** A Graeco-Latin square of order $p$ exists for every $p\ge3$ except $p=6$.

For design this means: when planning a Graeco-Latin square design, do not have $6$ treatments; add one, or drop one.

### 8.4.3. The Graeco-Latin Square Design

**Definition 8.4.2 (Graeco-Latin Square Design)** A **Graeco-Latin square design** arranges $p^2$ runs by a Graeco-Latin square of order $p$: four factors, each with $p$ levels, are assigned to the rows, the columns, the Latin letters and the Greek letters. Typically one factor is the treatment and the other three are blocking factors, but other combinations, such as two treatment factors and two blocking factors, are possible. All factors must have the same number of levels.

In the production example, the rows are the machines and the columns the operators (as before), the Greek letters the days, and the Latin letters are assigned to the protocols as before. The model is

$$
Y_{ijkl}=\mu+\alpha_i+\tau_j+\beta_k+\omega_l+\varepsilon_{ijkl},\qquad \varepsilon_{ijkl}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
with row effect $\alpha_i$, Latin letter (treatment) effect $\tau_j$, column effect $\beta_k$ and Greek letter effect $\omega_l$, all summing to zero; only the $p^2$ index combinations of the square occur. Because the Greek square is orthogonal to the Latin square and both are Latin, all four factors are mutually orthogonal in the sense of the proof of Theorem 8.1.1, and the analysis is the same with one more line:

| Source | df | Sum of squares |
|---|---|---|
| Rows | $p-1$ | $p\sum_i(\bar y_{i\cdot\cdot\cdot}-\bar y_{\cdot\cdot\cdot\cdot})^2$ |
| Latin letters (treatments) | $p-1$ | $p\sum_j(\bar y_{\cdot j\cdot\cdot}-\bar y_{\cdot\cdot\cdot\cdot})^2$ |
| Columns | $p-1$ | $p\sum_k(\bar y_{\cdot\cdot k\cdot}-\bar y_{\cdot\cdot\cdot\cdot})^2$ |
| Greek letters | $p-1$ | $p\sum_l(\bar y_{\cdot\cdot\cdot l}-\bar y_{\cdot\cdot\cdot\cdot})^2$ |
| Error | $(p-3)(p-1)$ | by subtraction |
| Total | $p^2-1$ | $\sum(y_{ijkl}-\bar y_{\cdot\cdot\cdot\cdot})^2$ |

The treatments are tested by $F_0=\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}\sim F_{p-1,(p-3)(p-1)}$ under $H_0$. The design is highly efficient, controlling three nuisance factors with only $N=p^2$ observations, but the error degrees of freedom are even fewer than for the Latin square: $0$ for $p=3$, $3$ for $p=4$, $8$ for $p=5$. So a $3\times3$ Graeco-Latin square leaves nothing to estimate $\sigma^2$, and small Graeco-Latin squares need replication or a prior estimate of the error. The same caveat about interactions applies, with greater force.

One could go even farther and superimpose more than two mutually orthogonal Latin squares. Such a design is called a *hyper-Graeco-Latin square*: with $m$ mutually orthogonal squares, $m+2$ factors are studied in $p^2$ runs, and the error has $(p-1)(p-1-m)$ degrees of freedom. With the maximum $m=p-1$ of Theorem 8.4.1, $p+1$ factors exhaust all $p^2-1$ degrees of freedom. RCBD controls one blocking factor, the Latin square two, the Graeco-Latin square three, and hyper-Graeco-Latin squares in principle more, but they are rarely used. They reappear as orthogonal arrays in fractional factorial designs.

In R, `agricolae` generates randomized Graeco-Latin squares:

```r
library(agricolae)
trt1 <- LETTERS[1:4]
trt2 <- 1:4
design4 <- design.graeco(trt1, trt2, seed = 543)
book4 <- design4$book     # plot, row, col, trt1, trt2
print(design4$sketch)
```

```text
     [,1]  [,2]  [,3]  [,4] 
[1,] "D 2" "B 4" "A 3" "C 1"
[2,] "B 3" "D 1" "C 2" "A 4"
[3,] "A 1" "C 3" "D 4" "B 2"
[4,] "C 4" "A 2" "B 1" "D 3"
```

Each letter and each number appears once in every row and every column, and each of the $16$ letter–number pairs appears exactly once.

## Summary {#summary}

| Design | Blocking factors | Runs | Error df | Requirement |
|---|---|---|---|---|
| RCBD ([3.8.7](/3.8.7)) | 1 | $ab$ | $(a-1)(b-1)$ | no treatment-by-block interaction |
| Latin square (Theorem 8.1.1) | 2 | $p^2$ | $(p-2)(p-1)$ | all factors with $p$ levels; no interactions |
| Replicated Latin square, Case 1 / 2 / 3 | 2 + replicate | $np^2$ | $(p-1)[n(p+1)-3]$ / $(p-1)(np-2)$ / $(p-1)[n(p-1)-1]$ | blocking levels reused / one nested / both nested |
| Graeco-Latin square | 3 | $p^2$ | $(p-3)(p-1)$ | an orthogonal pair of order $p$ (any $p\ge3$ except $6$) |
| Hyper-Graeco-Latin ($m$ squares) | $m+1$ | $p^2$ | $(p-1)(p-1-m)$ | $m\le p-1$ mutually orthogonal squares |

- A Latin square of order $p$ has each of $p$ symbols once in every row and column (Definition 8.1.1). The design blocks in two directions and is a $1/p$ fraction of the $p^3$ factorial (Definition 8.1.2). Randomize by choosing a random standard square and permuting rows, columns and letters at random, which gives a uniformly random square (Proposition 8.1.1).
- The model $y_{ijk}=\mu+\alpha_i+\tau_j+\beta_k+\varepsilon_{ijk}$ is completely additive. Rows, columns and treatments are mutually orthogonal, so $\mathrm{SS}_{\mathrm{T}}=\mathrm{SS}_{\mathrm{Rows}}+\mathrm{SS}_{\mathrm{Columns}}+\mathrm{SS}_{\mathrm{Tr}}+\mathrm{SS}_{\mathrm{E}}$, and $F_0=\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}\sim F_{p-1,(p-2)(p-1)}$ (Theorem 8.1.1).
- Rocket propellant example (Example 8.1.1): formulations differ ($p=0.0025$), operators differ, batches do not; keep the blocking factors the design used.
- Pros: two sources of heterogeneity removed from the error with $p^2$ runs. Cons: equal numbers of levels, no interactions allowed, few error df for $p\le4$.
- Replication: Case 1, the same rows and columns; Case 2, one blocking factor nested in replicates ($n(p-1)$ df); Case 3, both nested. Replication increases the error df and allows the treatment-by-replicate interaction to be estimated.
- A crossover design is a replicated Latin square with subjects and periods as blocking factors (Example 8.3.1: Case 2, or Case 3 if the periods differ between squares). Carryover is modeled by the previous treatment. Test the carryover adjusted for direct effects, and the direct effects adjusted for carryover. Williams designs balance the carryover: one square for even $p$ (Proposition 8.3.1), two for odd $p$.
- Orthogonal Latin squares: each pair of symbols appears once when superimposed (Definition 8.4.1). There are at most $p-1$ mutually orthogonal squares (Theorem 8.4.1), exactly $q-1$ for a prime power $q$ via $L_\lambda(x,y)=\lambda x+y$ over $\mathbb{F}_q$ (Theorem 8.4.2). A Graeco-Latin square exists for all $p\ge3$ except $6$ (Theorem 8.4.3).

## Questions

1. What are the error degrees of freedom of a $3\times3$ Latin square design? Why are squares smaller than $4\times4$ generally not used without replication?

   **Answer** $p^2-1=8$ total df, minus $3(p-1)=6$ for rows, columns and treatments, leaves $(p-2)(p-1)=2$. With $2$ error df, $\sigma^2$ is estimated very imprecisely and the critical value $F_{2,2,0.05}=19.0$ is huge, so only very large treatment effects can be detected. A $4\times4$ square has $6$ error df ($F_{3,6,0.05}=4.76$); replicating a $3\times3$ square $n$ times in Case 1 gives $2(4n-3)$ error df, for example $10$ for $n=2$.

2. In the rocket propellant experiment (Example 8.1.1) suppose the observation for batch $1$, operator $1$ ($A=24$) had been lost. Show that the least squares estimate of a missing value in a $p\times p$ Latin square is

   $$
   \hat y=\frac{p\,(y'_{i\cdot\cdot}+y'_{\cdot j\cdot}+y'_{\cdot\cdot k})-2y'_{\cdot\cdot\cdot}}{(p-2)(p-1)},
   $$
   where the primes denote totals of the available observations of the row, treatment and column of the missing cell, and of all observations, and compute it.

   **Answer** Insert $x$ for the missing value and choose $x$ to minimize the error sum of squares. As a function of $x$, $\mathrm{SS}_{\mathrm{E}}(x)=\text{const}+x^2-\frac1p[(R+x)^2+(T+x)^2+(C+x)^2]+\frac{2}{p^2}(G+x)^2$, with $R,T,C,G$ the primed totals (the $\mathrm{SS}_{\mathrm{T}}$ term contributes $x^2-(G+x)^2/p^2$, and each of the three factor sums of squares contributes $(\text{total}+x)^2/p-(G+x)^2/p^2$). Setting the derivative to zero gives $p^2x-p(R+T+C)-3px+2G+2x=0$, i.e. $x(p-1)(p-2)=p(R+T+C)-2G$. Here $R=111-24=87$, $T=143-24=119$, $C=107-24=83$, $G=635-24=611$, so $\hat y=(5\cdot289-2\cdot611)/12=223/12=18.58$. The analysis is then carried out with the error degrees of freedom reduced by one, to $11$ (the treatment sum of squares computed in this way is slightly biased upward; the exact analysis fits the model by least squares to the $24$ available observations, as for missing values in the RCBD, [3.8.7](/3.8.7)).

3. Three diets are compared on $6$ cows in three periods using two $3\times3$ Latin squares (Example 8.3.1). Which case of replicated Latin squares is this? When should it be analyzed as Case 3 instead? What are the treatment and the blocking factors?

   **Answer** The treatment is the diet; the blocking factors are the cows and the periods. The periods (the order) are the same in both squares, while the cows are different animals in each square, so it is Case 2 with the columns nested in the squares: error df $(p-1)(np-2)=8$. If the two squares were run at different times (for example spring and fall), the periods would mean different conditions in each square and should be nested in the squares as well, which is Case 3 with $(p-1)[n(p-1)-1]=6$ error df.

4. An experiment with four protocols must control machines, operators and days, each at four levels. How many runs does the full factorial need, how many does a Latin square replicated on each day need, and how many does a Graeco-Latin square need? How many error degrees of freedom does the Graeco-Latin square leave?

   **Answer** Full factorial: $4^4=256$ runs. A $4\times4$ Latin square run completely on each of the four days: $16\times4=64$ runs. Graeco-Latin square: $16$ runs, with each day containing each protocol, machine and operator once. Its error has $(p-3)(p-1)=3$ df, enough for an $F$-test but with low power ($F_{3,3,0.05}=9.28$); replicating the Graeco-Latin square would be advisable if the runs are affordable.

5. Construct two orthogonal Latin squares of order $5$ and verify that they are orthogonal.

   **Answer** By Theorem 8.4.2 over $\mathbb{F}_5$ (arithmetic modulo $5$), take $L_1(x,y)=x+y$ and $L_2(x,y)=2x+y$, with $x,y\in\{0,\dots,4\}$. Writing $A,\dots,E$ for $0,\dots,4$ in $L_1$ and $\alpha,\dots,\varepsilon$ in $L_2$, the rows of the superposition are $A\alpha\ B\beta\ C\gamma\ D\delta\ E\varepsilon$; $B\gamma\ C\delta\ D\varepsilon\ E\alpha\ A\beta$; $C\varepsilon\ D\alpha\ E\beta\ A\gamma\ B\delta$; $D\beta\ E\gamma\ A\delta\ B\varepsilon\ C\alpha$; $E\delta\ A\varepsilon\ B\alpha\ C\beta\ D\gamma$. A pair $(s,t)$ occurs where $x+y=s$ and $2x+y=t$, that is only at $x=t-s$, $y=2s-t$ (mod $5$), so each of the $25$ pairs occurs exactly once. The squares $L_3$ and $L_4$ complete a set of $4=p-1$ mutually orthogonal squares.

6. A bank wants to study the attractiveness of investment products with three risk levels, three return types and three investment terms under three macroeconomic scenarios, and proposes to use "two orthogonal Latin squares" of order $3$: one with scenarios as rows, risk levels as columns and return types as entries, and one with scenarios as rows, terms as columns and return types as entries. Is this a correct Graeco-Latin square design? Propose a correct one, and state what it can and cannot estimate.

   **Answer** No. A Graeco-Latin square superimposes two squares on the same rows and columns, with different factors as the Latin and the Greek letters. The proposal uses two different column factors and the same factor (return type) for the entries of both squares, so it is not a superposition of anything, and the four factors are not arranged orthogonally in a single set of runs. A correct design: rows = scenario, columns = risk level, Latin letters = return type, Greek letters = term, using a $3\times3$ Graeco-Latin square (for example $L_1=x+y$ and $L_2=2x+y$ modulo $3$), $9$ runs in total. Each pair of factors then appears in all $9$ combinations. But the error has $(p-3)(p-1)=0$ degrees of freedom: the $4\times2=8$ main-effect df use up all $8$ df, so the main effects can be estimated but not tested, and no interaction can be studied. The design has to be replicated (or the four factors studied in a larger factorial) to obtain tests, and it is valid only if the factors do not interact, which is doubtful for risk, return and term of a financial product.

7. Why does a single $3\times3$ Latin square never give a crossover design balanced for carryover effects, while a single $4\times4$ square can?

   **Answer** A subject's sequence of three treatments contains two ordered pairs, so three subjects give six pairs, and balance requires them to be the six ordered pairs $AB,BA,AC,CA,BC,CB$, each once. The six sequences (permutations) are $ABC$ ($AB$, $BC$), $ACB$ ($AC$, $CB$), $BAC$ ($BA$, $AC$), $BCA$ ($BC$, $CA$), $CAB$ ($CA$, $AB$) and $CBA$ ($CB$, $BA$). Suppose $ABC$ is used. The remaining pairs $AC$, $CA$, $CB$, $BA$ must come from two sequences avoiding $AB$ and $BC$; the candidates are $ACB$ and $CBA$, which share $CB$, and $BAC$, which shares $AC$ with $ACB$ and $BA$ with $CBA$. So no choice works, and by relabeling the treatments the same holds for any starting sequence. Hence two squares are needed for $p=3$, and each pair then occurs twice. For even $p$, Proposition 8.3.1 gives a single balanced square, such as $ABDC$, $BCAD$, $CDBA$, $DACB$ for $p=4$.

8. In Case 3 of replicated Latin squares (different machines and operators in each factory), would a treatment-by-factory interaction be a meaningful term? How many degrees of freedom does it have, and where do they come from?

   **Answer** Yes. In Case 3 the factories are different production environments with their own machines and operators, and the interaction asks whether the protocols have the same effects in every factory; a significant interaction would mean that the best protocol depends on the factory. The interaction has $(p-1)(n-1)$ df, $3\cdot2=6$ in the example with $p=4$ and $n=3$, taken from the $(p-1)[n(p-1)-1]=24$ error df, which leaves $18$. Within one square such an interaction is not estimable; it becomes estimable because each treatment is observed $p$ times in each replicate.
