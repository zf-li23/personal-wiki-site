---
title: Categorical Data Analysis
description: "Methods for counts in contingency tables. Paired symmetry (McNemar, Bowker, Cochran's Q); independence and homogeneity with Pearson's chi-squared and the likelihood ratio G-squared; exact tests for sparse tables (Fisher, Fisher–Freeman–Halton) and the role of fixed margins; stratified 2×2×k tables, the odds ratio, the Mantel–Haenszel test and common odds ratio and the homogeneity assumption; ordered categories with the WMW test and ridit analysis; and log-linear models for multi-way tables as Poisson GLMs, with hierarchical likelihood ratio tests and the interpretation of interactions as conditional odds ratios."
---

Categorical data are counts: the number of units falling into each combination of the categories of one or more variables. Many of the rank methods of this course can be seen as methods for such tables. A two-sample comparison of an ordinal response is a two-row table with ordered columns; McNemar's test ([3.6.8](/3.6.8)) and Cochran's $Q$ test ([3.6.11](/3.6.11)) analyze tables of paired binary responses; Mood's median test ([3.6.9](/3.6.9)) is a test for a $2\times2$ table. This chapter treats categorical data in their own right. The chi-squared tests of independence and homogeneity were introduced in 3.2.6; here we extend them in six directions: paired (square) tables, the likelihood ratio statistic, exact tests for sparse tables, stratified tables with a confounder, ordered categories, and models for tables with three or more variables.

The common thread is the same as in the rest of the course. Exact tests are permutation tests that condition on the margins of the table, just as rank tests condition on the observed ranks; large-sample tests replace the exact distribution by a chi-squared approximation, which fails when the table is sparse. And the choice of method depends on the design (paired or independent, stratified or not) and on the scale of the variables (nominal or ordinal).

## 12.1. Contingency Tables

A **contingency table** displays the counts of units cross-classified by one or more categorical variables: a one-way table for a single variable, a two-way $r\times c$ table for two variables (rows by columns), a three-way or multi-way table for more. The variables are of two kinds. A **nominal variable** has categories with no natural order (blood type, marital status), and in a regression model it is coded by indicator (one-hot) variables. An **ordinal variable** has ordered categories (severity of a side effect, level of education, satisfaction), and its order carries information that a good analysis should use, for instance through scores or ranks.

Continuous data can also be written as a contingency table. The calculator times of Example 9.1.1, sorted and labelled by group, form a $2\times N$ table with one observation per column, in which the columns are ordered by time; the WMW test is a test on this ordered table. Conversely, an ordinal response with few categories gives a two-way table with many ties, and the rank tests apply with midranks (Section 12.6).

Tables arise from different sampling schemes. A single sample cross-classified by two variables gives counts with a multinomial distribution over all $rc$ cells (the question is independence). Independent samples from $r$ populations, each classified by one variable, give a product of $r$ multinomial distributions with fixed row totals (the question is homogeneity: are the column distributions the same in every row?). Paired measurements on the same units give a square table whose rows and columns are the two measurements (the question is symmetry or marginal homogeneity). The first two lead to the same test statistics; the third needs different ones.

## 12.2. Paired Data: Tests of Symmetry

**Example 12.2.1 (Side Effects of Two Formulations)** Each of $158$ patients received an old and a new formulation of a drug, and the severity of side effects was recorded for both:

| Old \ New | None | Slight | Severe | Total |
|---|---|---|---|---|
| None | 83 | 4 | 3 | 90 |
| Slight | 17 | 22 | 5 | 44 |
| Severe | 4 | 9 | 11 | 24 |
| Total | 104 | 35 | 19 | 158 |

The table is square, with the same categories for rows and columns, and each patient is counted once. Is there a difference in side-effect severity between the formulations?
:::

The diagonal counts patients with the same severity under both formulations; they carry no information about a difference. Under the null hypothesis of no difference, a patient is as likely to move from category $i$ (old) to category $j$ (new) as from $j$ to $i$.

**Definition 12.2.1 (Bowker's Test of Symmetry)** For a $k\times k$ table of paired categorical responses with counts $n_{ij}$ (category $i$ on the first measurement, $j$ on the second), **Bowker's test of symmetry** tests $H_0\colon p_{ij}=p_{ji}$ for all $i\ne j$ with

$$
X^2=\sum_{i<j}\frac{(n_{ij}-n_{ji})^2}{n_{ij}+n_{ji}},
$$
which is approximately $\chi^2$ with $k(k-1)/2$ degrees of freedom under $H_0$, provided every $n_{ij}+n_{ji}$ is not too small (a common rule is at least $5$).

Each term compares the two counts of a symmetric pair: conditionally on $n_{ij}+n_{ji}$, $n_{ij}\sim\mathrm{Bin}(n_{ij}+n_{ji},\frac12)$ under $H_0$, and the term is the square of the standardized count. For $k=2$ there is one pair, and $X^2=(n_{12}-n_{21})^2/(n_{12}+n_{21})$ is the uncorrected chi-squared form of **McNemar's test** (Definition 8.3.1).

**Example 12.2.2 (Side Effects, Continued)** The three symmetric pairs give

$$
X^2=\frac{(4-17)^2}{4+17}+\frac{(3-4)^2}{3+4}+\frac{(5-9)^2}{5+9}=8.05+0.14+1.14=9.33,
$$
with $3$ degrees of freedom and $p=0.025$. Symmetry is rejected. The off-diagonal counts below the diagonal (worse with the old formulation, $17+4+9=30$) far exceed those above it ($4+3+5=12$): side effects tend to be less severe with the new formulation. The test itself is two-sided and non-directional; the direction comes from inspecting the table.
:::

Symmetry implies marginal homogeneity (the same distribution of severity under both formulations, here $90,44,24$ against $104,35,19$), but not conversely for $k\ge3$; the Stuart–Maxwell test addresses marginal homogeneity directly. The three paired tests of the course fit together as follows.

| Test | Data | Hypothesis | Relation |
|---|---|---|---|
| McNemar (Definition 8.3.1) | two paired measurements, two categories ($2\times2$) | marginal homogeneity = symmetry of the discordant cells | base case |
| Bowker (Definition 12.2.1) | two paired measurements, $k$ categories ($k\times k$) | symmetry of all off-diagonal pairs | McNemar for $k=2$ |
| Cochran's $Q$ (Definition 11.3.3) | $t$ repeated measurements, two categories ($b\times t$ matrix) | equal success probabilities across conditions | McNemar for $t=2$ |

So McNemar's test extends in two directions: to more categories (Bowker) and to more conditions (Cochran). For an ordinal response measured twice, a signed-rank test on the paired category scores may be more powerful than Bowker's test, which ignores the order.

## 12.3. Independence: Pearson's Chi-Squared and the Likelihood Ratio Test

For an $r\times c$ table with counts $n_{ij}$, row totals $n_{i\cdot}$, column totals $n_{\cdot j}$ and grand total $n$, the expected counts under independence (or homogeneity) are $e_{ij}=n_{i\cdot}n_{\cdot j}/n$, and Pearson's statistic is

$$
\chi^2=\sum_{i=1}^r\sum_{j=1}^c\frac{(n_{ij}-e_{ij})^2}{e_{ij}},
$$
approximately $\chi^2_{(r-1)(c-1)}$ under $H_0$ (3.2.6, the **test of independence** and the **test of homogeneity**). The test assumes independent observations, and the approximation is customarily trusted when all $e_{ij}\ge5$ (less strict rules allow a few cells with $1\le e_{ij}<5$). It detects the existence of an association but not its direction or strength, and in very large samples even trivial departures from independence are significant.

The alternative is the **likelihood ratio test** ([Definition 5.3.1](/3.2.5#def-5.3.1) of 3.2.5).

**Proposition 12.3.1** Under multinomial sampling, the likelihood ratio statistic for independence in an $r\times c$ table is

$$
G^2=-2\log\Lambda=2\sum_{i,j}n_{ij}\log\frac{n_{ij}}{e_{ij}},
$$
with the convention $0\log0=0$, and $G^2\overset{H_0}{\approx}\chi^2_{(r-1)(c-1)}$.

**Proof** The multinomial likelihood is $L(\boldsymbol p)=\frac{n!}{\prod n_{ij}!}\prod_{i,j}p_{ij}^{n_{ij}}$. Without restriction the maximum likelihood estimates are $\hat p_{ij}=n_{ij}/n$, the saturated fit that reproduces the table. Under independence, $p_{ij}=p_{i\cdot}p_{\cdot j}$, the estimates are $\hat p_{i\cdot}=n_{i\cdot}/n$ and $\hat p_{\cdot j}=n_{\cdot j}/n$, so $\hat p_{ij}=e_{ij}/n$. The ratio of the maximized likelihoods is

$$
\Lambda=\prod_{i,j}\Bigl(\frac{e_{ij}/n}{n_{ij}/n}\Bigr)^{n_{ij}}=\prod_{i,j}\Bigl(\frac{e_{ij}}{n_{ij}}\Bigr)^{n_{ij}},
$$
and $-2\log\Lambda$ is the stated expression. The unrestricted model has $rc-1$ free parameters and the independence model $(r-1)+(c-1)$; the difference is $(r-1)(c-1)$, and Wilks' theorem gives the limit. $\square$

The two statistics test the same hypothesis and measure the same discrepancy between the observed counts $n_{ij}$ and the fitted counts $e_{ij}$, with different weights: Pearson's $(O-E)^2/E$, the likelihood ratio $2\,O\log(O/E)$. A Taylor expansion of $O\log(O/E)$ about $O=E$ shows that $G^2=\chi^2+O_p(n^{-1/2})$, so they agree in large samples, and both are unreliable for sparse tables. They come from different estimation principles: Pearson's statistic is the minimum of a chi-squared distance, $G^2$ compares the fitted model with the **saturated model** that fits every count exactly. In moderate samples Pearson's $\chi^2$ is often closer to its limiting distribution; the advantage of $G^2$ is that it is a difference of **deviances** and extends to generalized linear models and nested model comparisons (Section 12.7), where $G^2$ for nested models adds up exactly.

## 12.4. Sparse Tables: Exact Tests

### 12.4.1. Fisher's Exact Test

**Example 12.4.1 (The Lady Tasting Tea)** In Fisher's famous experiment a lady claimed to be able to tell whether the milk or the tea had been poured first into a cup. Fisher prepared $8$ cups, $4$ of each kind, presented them in random order, and asked her to identify the $4$ cups with milk first. Suppose she identified $3$ of them correctly:

| Guess \ Truth | Milk first | Tea first | Total |
|---|---|---|---|
| Milk first | 3 | 1 | 4 |
| Tea first | 1 | 3 | 4 |
| Total | 4 | 4 | 8 |

Does she have the discriminating skill?
:::

Under $H_0$ (no ability), her choice of $4$ cups is a random subset of the $8$, independent of the truth. All margins are fixed by the design, and once the number $X$ of correctly identified milk-first cups is known, the whole table is determined. The number of ways to choose $4$ cups is $\binom84=70$, and

$$
\mathbb{P}(X=x)=\frac{\binom4x\binom4{4-x}}{\binom84},\qquad x=0,\dots,4,
$$
a **hypergeometric distribution**. The one-sided $p$-value for $H_1$ (a positive association between guess and truth) is $\mathbb{P}(X\ge3)=(16+1)/70=0.243$: three correct out of four is quite likely by chance, and there is no evidence of skill. Only all four correct, with probability $1/70=0.014$, would be significant at the $5\%$ level.

**Definition 12.4.1 (Fisher's Exact Test)** For a $2\times2$ table with cell counts $a,b,c,d$, row totals $m=a+b$, $n=c+d$, first column total $k=a+c$ and $N=m+n$, **Fisher's exact test** of independence (or homogeneity) uses the conditional distribution of $a$ given all margins, which under $H_0$ is hypergeometric,

$$
\mathbb{P}(A=x\mid\text{margins})=\frac{\binom mx\binom n{k-x}}{\binom Nk},\qquad\max(0,k-n)\le x\le\min(m,k).
$$
The one-sided $p$-value sums the probabilities of the tables at least as extreme in the direction of $H_1$; the usual two-sided $p$-value sums the probabilities of all tables whose probability does not exceed that of the observed table.

Fisher's test is a permutation test (Definition 1.2.1): it conditions on the observed margins and computes the exact permutation distribution of the cell count, as the rank tests condition on the observed ranks. The conditioning is natural when the margins are fixed by the design, as in the tea experiment. It is also justified when they are not: with two independent binomial samples, the column total $k$ has a distribution that depends on the unknown common success probability, but the conditional distribution of $a$ given $k$ does not, so conditioning removes the nuisance parameter and gives a test that is exact for every value of it. Pearson's chi-squared test needs no fixed margins; its expected counts are computed from the observed margins, but its justification is asymptotic. Because of the discreteness of the conditional distribution, Fisher's test is conservative: its actual size is below the nominal level, sometimes considerably.

### 12.4.2. Tables Larger Than 2 × 2

**Example 12.4.2 (Scarlet Fever)** In a country where scarlet fever is a problem, six districts $A$ to $F$ were chosen. In each district patients were located and asked to state the site where they thought their child's irritation was worst:

| Site \ District | A | B | C | D | E | F | Total |
|---|---|---|---|---|---|---|---|
| Nose | 1 | 1 | 0 | 1 | 8 | 0 | 11 |
| Throat | 0 | 1 | 1 | 1 | 0 | 1 | 4 |
| Ears | 1 | 0 | 0 | 0 | 7 | 1 | 9 |
| Total | 2 | 2 | 1 | 2 | 15 | 2 | 24 |

Is there an association between districts and the sites of greatest perceived irritation? Of the $18$ expected counts, $15$ are below $1$ (the smallest is $0.17$), and the chi-squared approximation cannot be trusted.
:::

**Definition 12.4.2 (Fisher–Freeman–Halton Test)** For an $r\times c$ table, under $H_0$ of independence and conditionally on all row and column totals, the cell counts have the multivariate hypergeometric distribution

$$
\mathbb{P}(N_{ij}=n_{ij},\ \text{all }i,j\mid n_{i\cdot},n_{\cdot j})=\frac{\prod_in_{i\cdot}!\,\prod_jn_{\cdot j}!}{n!\,\prod_{i,j}n_{ij}!}.
$$
The **Fisher–Freeman–Halton test** computes the exact $p$-value as the sum of the probabilities of all tables with the observed margins whose probability does not exceed that of the observed table.

For $2\times2$ tables it is Fisher's exact test. It requires no large-sample approximation and is reliable for sparse tables and zero counts. The number of tables with given margins grows very quickly with the size of the table, so software uses efficient network algorithms or, for large tables, a Monte Carlo approximation: random tables with the observed margins are generated (by permuting one variable against the other) and the proportion with probability at most that of the observed table estimates the $p$-value.

```r
tab <- matrix(c(1, 0, 1,  1, 1, 0,  0, 1, 0,  1, 1, 0,  8, 0, 7,  0, 1, 1), nrow = 3,
              dimnames = list(Site = c("Nose", "Throat", "Ears"), District = LETTERS[1:6]))
fisher.test(tab)                                   # p-value = 0.02613
chisq.test(tab)                                    # X-squared = 14.96, df = 10, p-value = 0.1335
fisher.test(tab, simulate.p.value = TRUE, B = 1e5) # Monte Carlo version
```

For the scarlet fever data the exact test gives $p=0.026$, while the chi-squared test gives $p=0.134$ (with a warning that the approximation may be incorrect) and $G^2=17.33$ gives $p=0.067$. The exact test finds evidence of an association, apparently driven by district $E$, where no child had the throat as the worst site. With so many small expected counts, the asymptotic tests are unreliable, and here they are conservative.

The independence tests of this section treat both variables as nominal: permuting the columns of the table does not change any of the statistics. When a variable is ordinal, they discard information (Section 12.6).

## 12.5. Stratified Tables: The Mantel–Haenszel Method

### 12.5.1. Confounding and the Odds Ratio

**Example 12.5.1 (Two Anti-Cancer Drugs)** Two drugs were compared in two hospitals:

| | Hospital 1: effective | ineffective | total | Hospital 2: effective | ineffective | total |
|---|---|---|---|---|---|---|
| Drug A | 50 | 15 | 65 | 47 | 135 | 182 |
| Drug B | 92 | 90 | 182 | 5 | 60 | 65 |
| Total | 142 | 105 | 247 | 52 | 195 | 247 |

Pooling the hospitals, each drug was effective for $97$ of $247$ patients, a proportion of $0.393$: apparently the drugs are equally effective. Within each hospital, however, drug A does better: $50/65=0.77$ against $92/182=0.51$ in hospital 1, and $47/182=0.26$ against $5/65=0.08$ in hospital 2.
:::

The pooled comparison is misleading because of **confounding** ([3.8.2](/3.8.2)): hospital 2 treats patients with a much lower success rate (perhaps more advanced disease) and gave most of them drug A. This is an instance of **Simpson's paradox** ([3.3.10](/3.3.10)). The comparison of the drugs must be made within hospitals and then combined. A convenient measure of association for this purpose is the odds ratio.

**Definition 12.5.1 (Odds Ratio)** For two groups with success probabilities $p_1$ and $p_2$, the **odds ratio** is

$$
\mathrm{OR}=\frac{p_1/(1-p_1)}{p_2/(1-p_2)} .
$$
For a $2\times2$ table with cells $a,b$ (first row: successes, failures) and $c,d$ (second row), its estimate is $\widehat{\mathrm{OR}}=ad/(bc)$. $\mathrm{OR}=1$ if and only if $p_1=p_2$, that is, if rows and columns are independent.

The odds ratio is symmetric in rows and columns, unchanged by multiplying a row or a column by a constant (so it can be estimated from case–control as well as cohort samples), and its logarithm is the natural parameter of logistic and log-linear models. When the event is rare in both groups, $p/(1-p)\approx p$ and the odds ratio is close to the ratio of probabilities, the **relative risk**. In Example 12.5.1 the hospital-specific odds ratios are $\widehat{\mathrm{OR}}_1=\frac{50\times90}{15\times92}=3.26$ and $\widehat{\mathrm{OR}}_2=\frac{47\times60}{135\times5}=4.18$: in both hospitals drug A has the higher odds of success, by a similar factor, while the pooled odds ratio is exactly $1$.

### 12.5.2. The Mantel–Haenszel Test and Estimator

For $K$ strata (here hospitals), let stratum $k$ have the $2\times2$ table $a_k,b_k,c_k,d_k$ with total $T_k$, row totals $R_{1k}=a_k+b_k$, $R_{2k}=c_k+d_k$ and column totals $C_{1k}=a_k+c_k$, $C_{2k}=b_k+d_k$.

**Definition 12.5.2 (Mantel–Haenszel Test)** The **Mantel–Haenszel test** of conditional independence, $H_0$: the odds ratio is $1$ in every stratum, uses

$$
\chi^2_{\mathrm{MH}}=\frac{\bigl(\sum_k(a_k-\mathbb{E}a_k)\bigr)^2}{\sum_k\operatorname{Var}(a_k)},\qquad
\mathbb{E}a_k=\frac{R_{1k}C_{1k}}{T_k},\qquad\operatorname{Var}(a_k)=\frac{R_{1k}R_{2k}C_{1k}C_{2k}}{T_k^2(T_k-1)},
$$
the mean and variance of the hypergeometric distribution of $a_k$ given the margins of stratum $k$; $\chi^2_{\mathrm{MH}}\overset{H_0}{\approx}\chi^2_1$, and a continuity correction subtracts $\frac12$ from $\lvert\sum_k(a_k-\mathbb{E}a_k)\rvert$ before squaring. The **Mantel–Haenszel estimator** of a common odds ratio is

$$
\widehat{\mathrm{OR}}_{\mathrm{MH}}=\frac{\sum_ka_kd_k/T_k}{\sum_kb_kc_k/T_k}.
$$

The statistic adds up, across strata, the deviations of the observed from the expected count in the first cell, each computed within its stratum with Fisher's conditional distribution, so that comparisons are only made within strata. It is most powerful when the association has the same direction and similar strength in all strata; deviations of opposite sign cancel. The estimator is a weighted average of the stratum-specific odds ratios,

$$
\widehat{\mathrm{OR}}_{\mathrm{MH}}=\sum_kw_k\,\widehat{\mathrm{OR}}_k,\qquad w_k=\frac{b_kc_k/T_k}{\sum_lb_lc_l/T_l},
$$
with weights proportional to $b_kc_k/T_k$, not to the stratum sizes $T_k$; even with equal stratum sizes it is generally not the arithmetic mean of the stratum odds ratios. It is consistent both when the number of strata is fixed and their sizes grow, and when there are many small strata (as in matched pairs, where it reduces to the McNemar estimate $b/c$).

**Example 12.5.2 (Two Drugs, Continued)** In hospital 1, $\mathbb{E}a_1=65\times142/247=37.37$ and $\operatorname{Var}(a_1)=\frac{65\times182\times142\times105}{247^2\times246}=11.75$; in hospital 2, $\mathbb{E}a_2=182\times52/247=38.32$ and $\operatorname{Var}(a_2)=7.99$. Then

$$
\chi^2_{\mathrm{MH}}=\frac{(50-37.37+47-38.32)^2}{11.75+7.99}=23.01,
$$
or $21.94$ with the continuity correction, and $\widehat{\mathrm{OR}}_{\mathrm{MH}}=\frac{50\times90/247+47\times60/247}{15\times92/247+135\times5/247}=3.56$.

```r
x <- array(c(50, 92, 15, 90,  47, 5, 135, 60), dim = c(2, 2, 2))
mantelhaen.test(x)
```

```text
Mantel-Haenszel chi-squared test with continuity correction
Mantel-Haenszel X-squared = 21.944, df = 1, p-value = 2.807e-06
alternative hypothesis: true common odds ratio is not equal to 1
95 percent confidence interval:
 2.080167 6.099585
sample estimates:
common odds ratio
         3.562044
```

After adjusting for the hospital, there is very strong evidence of an association between drug and efficacy: the odds of success with drug A are estimated to be $3.6$ times those with drug B ($95\%$ interval $2.1$ to $6.1$).
:::

### 12.5.3. The Homogeneity Assumption

The common odds ratio is a meaningful summary only if the odds ratios are similar in all strata. If they differ, the stratifying variable is an **effect modifier** (it produces **effect modification**, an **interaction effect** between treatment and stratum on the odds-ratio scale), and a single pooled estimate hides the differences; one should report the stratum-specific odds ratios instead. Homogeneity can be checked by the Breslow–Day test, which compares each $a_k$ with its expected value under the common odds ratio $\widehat{\mathrm{OR}}_{\mathrm{MH}}$ and is approximately $\chi^2_{K-1}$. For the two hospitals it gives $0.18$ on $1$ degree of freedom ($p=0.68$): the odds ratios $3.26$ and $4.18$ are compatible with a common value, and the Mantel–Haenszel summary is appropriate. A nonsignificant Breslow–Day test is weak evidence of homogeneity when the strata are small; the stratum-specific estimates should always be shown. Section 12.7 treats an example in which homogeneity clearly fails.

## 12.6. Ordered Categories

**Example 12.6.1 (Side Effects of Two Drugs)** The numbers of patients showing side effects of increasing severity were, for two independent groups:

| | None | Slight | Moderate | Severe | Fatal | Total |
|---|---|---|---|---|---|---|
| Drug A | 23 | 8 | 9 | 3 | 2 | 45 |
| Drug B | 42 | 8 | 4 | 0 | 0 | 54 |
| Total | 65 | 16 | 13 | 3 | 2 | 99 |

Does one drug tend to cause more severe side effects than the other?
:::

The column categories are ordered. Pearson's chi-squared test ignores the order: it would give the same value if the columns were permuted, and its $(2-1)(5-1)=4$ degrees of freedom spread its power over all patterns of difference. Here the question is directional, and the WMW test for an ordinal response with ties (Section 9.3.5) is appropriate: every patient in a column shares the midrank of that column.

Counting the pairs in which the drug-A patient has the less severe side effect, with ties counted as one half,

$$
U_A=23\bigl(\tfrac12\cdot42+8+4\bigr)+8\bigl(\tfrac12\cdot8+4\bigr)+9\bigl(\tfrac12\cdot4\bigr)=841
$$
out of $45\times54=2430$ pairs; equivalently, the drug-A patient is more severely affected in $2430-841=1589$ pairs (the value R reports as `W`). The tied groups have sizes $65$, $16$, $13$, $3$ and $2$, all of which must enter the tie correction:

$$
z=\frac{841-2430/2}{\sqrt{\dfrac{2430}{12}\Bigl[100-\dfrac{(65^3-65)+(16^3-16)+(13^3-13)+(3^3-3)+(2^3-2)}{99\times98}\Bigr]}}=-3.12,
$$
and the two-sided $p$-value is $0.0018$. (Using only the tied groups of one sample, $42$, $8$, $4$, in the correction, a tempting mistake, gives $z=-2.74$.) There is strong evidence that drug A causes more severe side effects.

```r
lev <- c("None", "Slight", "Moderate", "Severe", "Fatal")
drug_a <- ordered(rep(lev, times = c(23, 8, 9, 3, 2)), levels = lev)
drug_b <- ordered(rep(lev, times = c(42, 8, 4, 0, 0)), levels = lev)
wilcox.test(as.numeric(drug_a), as.numeric(drug_b), exact = FALSE, correct = TRUE)
```

```text
Wilcoxon rank sum test with continuity correction
W = 1589, p-value = 0.001847
```

Ignoring the order, Fisher–Freeman–Halton gives $p=0.0127$ and Pearson's chi-squared $p=0.019$, both larger than the WMW $p$-value. This is the general rule: power is gained by taking the ordering into account. It is not a law, however. When the groups differ in a way that is not a shift along the order, the omnibus test can give a smaller $p$-value. In the extreme case where all $100$ patients on drug A have moderate side effects and on drug B half have none and half die, the WMW statistic is exactly $n_1n_2/2$ ($p=1$), while the chi-squared statistic is $200$ ($p<10^{-40}$). The chi-squared test correctly says that the distributions differ, but its result cannot be read as "one drug causes more severe side effects": in the sense measured by the WMW test, neither does.

### 12.6.1. Ridit Analysis

Ridit analysis (Bross 1958) expresses the same comparison on an interpretable scale. The name comes from "relative to an identified distribution".

**Definition 12.6.1 (Ridit Analysis)** Let a reference group have proportions $\pi_1,\dots,\pi_C$ in ordered categories $1,\dots,C$. The *ridit* of category $j$ is

$$
r_j=\sum_{l<j}\pi_l+\tfrac12\pi_j ,
$$
the proportion of the reference group below category $j$ plus half the proportion in it. In **ridit analysis** each member of a comparison group is assigned the ridit of its category, and the mean ridit $\bar r=\sum_jq_jr_j$ (with $q_j$ the comparison group's proportions) is reported.

The mean ridit of the reference group is $\frac12$. The mean ridit of a comparison group estimates $\mathbb{P}(Y>X)+\frac12\mathbb{P}(Y=X)$, where $Y$ is a random member of the comparison group and $X$ of the reference group: it is the WMW statistic divided by $n_1n_2$. With drug B as reference, the ridits are $0.389$, $0.852$, $0.963$, $1$, $1$, and the mean ridit of drug A is $0.654=1589/2430$: a randomly chosen patient on drug A has more severe side effects than one on drug B with probability $0.65$ (ties counted as one half). Ridit analysis is thus a descriptive presentation of the WMW comparison, and its significance test is the WMW test. When the reference group is the pooled sample instead of one of the groups, the mean ridits of the groups are linear functions of their mean midranks.

For a $2\times C$ table with a binary response in ordered groups, rather than an ordinal response in two groups, the analogous trend test is the **Cochran–Armitage trend test**.

## 12.7. Multi-Way Tables and Log-Linear Models

### 12.7.1. An Example

**Example 12.7.1 (Smoking and Coronary Deaths)** In a prospective study of British male doctors (Doll and Hill 1966; tabulated by Breslow and Day 1987), coronary deaths during the first ten years of follow-up were recorded together with the person-years of observation, by smoking status and age group:

| Age | Smokers: deaths | person-years | Non-smokers: deaths | person-years | Rate ratio |
|---|---|---|---|---|---|
| 35–44 | 32 | 52407 | 2 | 18790 | 5.74 |
| 45–54 | 104 | 43248 | 12 | 10673 | 2.14 |
| 55–64 | 206 | 28612 | 28 | 5710 | 1.47 |
| 65–74 | 186 | 12663 | 28 | 2585 | 1.36 |
| 75–84 | 102 | 5317 | 31 | 1462 | 0.90 |
| Total | 630 | 142247 | 101 | 39220 | 1.72 |

Three questions are of interest. (1) Is the association between smoking and coronary death the same in all age groups? (2) What is the association between smoking and death, adjusted for age? (3) Does age affect the death rate when smoking is held fixed?
:::

The crude death rates are $630/142247=4.43$ and $101/39220=2.58$ per $1000$ person-years, a crude **rate ratio** of $1.72$. Age is a confounder: death rates increase steeply with age for both groups, and the age distributions of smokers and non-smokers differ, so $1.72$ mixes the effects of smoking and age. The age-specific rate ratios (the last column) show more: the ratio is highest in the youngest group, $5.74=(32/52407)/(2/18790)$, and decreases steadily to $0.90$ in the oldest. Most person-years come from young smokers, where the rate ratio is largest but the number of deaths among non-smokers is tiny (two), so the youngest ratio is very imprecise: its $95\%$ interval runs from about $1.4$ to $24$.

![Coronary deaths of British male doctors by age and smoking (Doll and Hill 1966; Breslow and Day 1987). Left: age-specific death rates per $100\,000$ person-years (log scale) for smokers and non-smokers; the curves converge and cross in the oldest group. Right: rate ratios with approximate $95\%$ intervals, decreasing from $5.7$ to $0.9$.](./plots/smoking-rates.py)

A decreasing rate ratio means that age modifies the effect of smoking, and a single Mantel–Haenszel summary would be misleading. We need a framework that can test this formally and describe the structure: log-linear models.

### 12.7.2. Log-Linear Models

A three-way table has cells $(i,j,k)$ for the levels of three variables, here $A$ (age, $5$ levels), $S$ (smoking, $2$) and $D$ (death, $2$), with expected counts $\mu_{ijk}$.

**Definition 12.7.1 (Log-Linear Model)** A **log-linear model** for a multi-way contingency table expresses the logarithms of the expected cell counts as a linear function of main effects and interactions of the classifying variables. For three variables the **saturated model** is

$$
\log\mu_{ijk}=\lambda+\lambda_i^A+\lambda_j^S+\lambda_k^D+\lambda_{ij}^{AS}+\lambda_{ik}^{AD}+\lambda_{jk}^{SD}+\lambda_{ijk}^{ASD},
$$
with identifiability constraints (for example, terms involving a reference level set to $0$); it has as many free parameters as there are cells and reproduces the observed counts exactly. Simpler models set some interaction terms to zero.

The model treats the variables symmetrically: no variable is designated as the response. $\lambda$ is an overall level, $\lambda^A_i,\lambda^S_j,\lambda^D_k$ are main effects that reproduce the one-way margins, the two-factor terms describe pairwise associations, and the three-factor term describes how a pairwise association varies with the level of the third variable. Models are usually required to be hierarchical: if an interaction is in the model, so are all lower-order terms contained in it.

A log-linear model is a **generalized linear model** ([3.3.6](/3.3.6)) with Poisson responses and the log **link function**: the counts are treated as independent Poisson variables with means $\mu_{ijk}$, and $\log\mu_{ijk}$ is linear in the parameters. (Under multinomial or product-multinomial sampling the estimates and likelihood ratio tests are the same, provided the terms corresponding to the fixed margins are in the model.) It is not a linear regression of $\log n_{ijk}$ on the factors, a common misconception:

| | Log-linear model (Poisson GLM) | Linear regression on $\log y$ |
|---|---|---|
| Models | $\log\mathbb{E}[Y]$, the log of the expected count | $\log Y$, the log of the observed count |
| The log is | a link function | a transformation of the data |
| Distribution | Poisson counts, variance equal to the mean | normal errors with constant variance |
| Zero counts | no problem | $\log0$ undefined |
| Coefficients | log rate ratios and log odds ratios | no such interpretation |

The two-factor and three-factor terms have a direct interpretation as conditional log odds ratios.

**Proposition 12.7.1** In the saturated model, the conditional log odds ratio between $S$ and $D$ within level $i$ of $A$ is

$$
\log\mathrm{OR}_{SD\mid i}=\log\frac{\mu_{i22}\mu_{i11}}{\mu_{i21}\mu_{i12}}
=\bigl(\lambda^{SD}_{22}-\lambda^{SD}_{21}-\lambda^{SD}_{12}+\lambda^{SD}_{11}\bigr)+\bigl(\lambda^{ASD}_{i22}-\lambda^{ASD}_{i21}-\lambda^{ASD}_{i12}+\lambda^{ASD}_{i11}\bigr).
$$
With reference-level constraints (level $1$ of each variable as reference), this is $\beta^{SD}+\beta^{ASD}_i$, where $\beta^{SD}=\lambda^{SD}_{22}$ is the log odds ratio in the reference age group and $\beta^{ASD}_i=\lambda^{ASD}_{i22}$ is the difference between the log odds ratio in age group $i$ and that in the reference group. The three-factor interaction is zero if and only if the conditional odds ratios are the same in all age groups.

**Proof** Substitute the model into the double difference $\log\mu_{i22}-\log\mu_{i21}-\log\mu_{i12}+\log\mu_{i11}$. Every term that does not depend on both $j$ and $k$ ($\lambda$, $\lambda^A_i$, $\lambda^S_j$, $\lambda^D_k$, $\lambda^{AS}_{ij}$, $\lambda^{AD}_{ik}$) appears twice with opposite signs and cancels; only the $SD$ and $ASD$ terms remain. Under reference constraints all terms with $j=1$ or $k=1$ or $i=1$ are zero, which gives the second form. $\square$

### 12.7.3. Fitting and Testing by Likelihood Ratios

To fit the model to Example 12.7.1, the data must be arranged as a $5\times2\times2$ table of counts. The deaths are counts, but the person-years are not; the usual device is to treat "person-years minus deaths" as the number of survivors, that is, to regard each person-year as an independent Bernoulli trial for death. Because coronary death is rare (about $2\%$ per person-year in the highest cell), the odds of death are close to the death rate, and the conditional odds ratios agree with the rate ratios of the table to two decimals ($5.74$, $2.14$, $1.47$, $1.36$, $0.90$).

```r
age <- factor(c("35-44", "45-54", "55-64", "65-74", "75-84"))
sd <- c(32, 104, 206, 186, 102); sp <- c(52407, 43248, 28612, 12663, 5317)
nd <- c(2, 12, 28, 28, 31);      np <- c(18790, 10673, 5710, 2585, 1462)
tab <- expand.grid(Age = age, Smoking = factor(c("Smoker", "Non-Smoker")),
                   Death = factor(c("Survived", "Died")))
tab$Freq <- c(sp - sd, np - nd, sd, nd)
saturated <- glm(Freq ~ Age * Smoking * Death, family = poisson, data = tab)
model1 <- glm(Freq ~ Age * Smoking + Age * Death + Smoking * Death, family = poisson, data = tab)
anova(model1, saturated, test = "Chisq")
```

```text
Analysis of Deviance Table
Model 1: Freq ~ Age * Smoking + Age * Death + Smoking * Death
Model 2: Freq ~ Age * Smoking * Death
  Resid. Df Resid. Dev Df Deviance Pr(>Chi)
1         4     12.098
2         0      0.000  4   12.098  0.01664 *
```

The procedure follows the hierarchical principle: test the highest-order interaction first, and simplify the model only if it is not significant.

- Question 1 (is the association the same at all ages?) is the test of the three-factor interaction $\lambda^{ASD}$, the likelihood ratio comparison of the saturated model with the model of no three-factor interaction: $G^2=12.10$ on $4$ degrees of freedom, $p=0.017$ (Pearson's $\chi^2=11.12$, $p=0.025$). The hypothesis of a common odds ratio across age groups is rejected: age modifies the association between smoking and coronary death.
- Question 2 (an age-adjusted overall association) therefore has no single answer. Under the no-three-factor model, the common odds ratio would be $1.43$, but that model does not fit; the association must be reported by age group, as the conditional odds ratios of Proposition 12.7.1.
- Question 3 (an effect of age given smoking) concerns the $AD$ interaction. Age matters overwhelmingly: removing $\lambda^{AD}$ from the no-three-factor model increases the deviance by $898$ on $4$ degrees of freedom. (Strictly, the three-factor interaction being present, $\lambda^{AD}$ cannot be removed alone; but the age-specific death rates of both groups rise more than tenfold from the youngest to the oldest group, and no test is needed to see this.)

The test of homogeneity is the joint likelihood ratio test of the four three-factor parameters, not the Wald test of any single one of them. In the saturated fit (with "Survived" as the modelled category), the coefficient for the oldest age group, `Age75-84:SmokingSmoker:DeathSurvived` $=1.85$, has a Wald $p$-value of $0.015$, and it might be tempting to cite this as the evidence for effect modification. But each such coefficient compares one age group with the youngest, whose estimate rests on two deaths among non-smokers; which coefficient happens to be significant depends on the reference group chosen; and testing them one at a time raises the problem of multiple comparisons. Here the joint test leads to the same conclusion, $p=0.017$, but it is the correct test.

The conditional odds ratios are read from the coefficients by Proposition 12.7.1. In the youngest group, the coefficient `SmokingSmoker:DeathSurvived` $=-1.747$ is the log odds ratio of survival, so the odds ratio of death is $\mathrm{e}^{1.747}=5.74$: in this age group the odds of coronary death for smokers are estimated to be $5.7$ times those for non-smokers. In the oldest group, $-1.747+1.850=0.102$, and the odds ratio of death is $\mathrm{e}^{-0.102}=0.90$. Because the event is rare, these odds ratios are essentially rate ratios; neither is a ratio of risks over a fixed period, and phrases such as "the death risk of smokers is $5.74$ times" are loose.

Why should the effect of smoking decline with age? A likely contribution is selection: the smokers who reach old age without coronary disease may be those who are less susceptible, and competing causes of death remove others; part of the decline may also be the larger absolute death rates at older ages, against which a constant excess risk becomes a smaller ratio. The data cannot distinguish these explanations.

### 12.7.4. A More Natural Model: Poisson Rate Regression

Treating person-years minus deaths as survivors is an approximation. The more natural model treats the deaths $Y$ in each cell as Poisson with mean proportional to the person-years $t$:

$$
\log\mathbb{E}[Y_{ij}]=\log t_{ij}+\beta_0+\alpha_i+\gamma_j+(\alpha\gamma)_{ij},
$$
a **Poisson regression** with the known offset $\log t_{ij}$, in which $\mathrm{e}^{\gamma_2}$ is the rate ratio for smokers in the reference age group and the interaction terms describe how it changes with age. This is the death-rate analogue of the log-linear model (the person-years play the role of the fixed $AS$ margin). Comparing the additive model ($(\alpha\gamma)_{ij}=0$, a common rate ratio) with the saturated one gives a deviance difference of $12.13$ on $4$ degrees of freedom, $p=0.016$, practically the same as before. The additive model would give a common rate ratio of $1.43$ ($95\%$ interval $1.15$ to $1.76$), close to the Mantel–Haenszel rate ratio $1.42$, but it does not fit. A model with a linear trend of the log rate ratio in the age-group index, $\log\mathrm{RR}_i=\gamma+\delta\,(i-1)$, fits well (deviance $1.55$ on $3$ degrees of freedom, $p=0.67$) and gives $\hat\delta=-0.31$ (standard error $0.10$): the rate ratio decreases by a factor of about $\mathrm{e}^{-0.31}=0.73$ per ten years of age. This single-parameter description is more informative, and its test ($p=0.001$) more powerful, than the four-degree-of-freedom test of heterogeneity.

```r
d <- data.frame(age = rep(age, 2), smoke = factor(rep(c("smoker", "non-smoker"), each = 5),
                levels = c("non-smoker", "smoker")), deaths = c(sd, nd), py = c(sp, np))
add <- glm(deaths ~ age + smoke, offset = log(py), family = poisson, data = d)
int <- glm(deaths ~ age * smoke, offset = log(py), family = poisson, data = d)
anova(add, int, test = "Chisq")                    # deviance 12.13 on 4 df, p = 0.016
trend <- glm(deaths ~ age + smoke + I(as.numeric(age) * (smoke == "smoker")),
             offset = log(py), family = poisson, data = d)
anova(add, trend, test = "Chisq")                  # deviance 10.59 on 1 df, p = 0.001
```

The general lesson of this section: a three-way table should first be examined for a three-factor interaction. If there is none, a stratified summary (Mantel–Haenszel, or the common odds ratio of the no-three-factor model) is appropriate. If there is one, the association must be reported stratum by stratum, or modelled as a function of the stratifying variable.

## Summary

- Tables and designs (Section 12.1): one sample cross-classified (independence), several independent samples (homogeneity), paired measurements (symmetry); nominal versus ordinal variables.
- Paired symmetry: McNemar ($2\times2$), Bowker's test $X^2=\sum_{i<j}(n_{ij}-n_{ji})^2/(n_{ij}+n_{ji})$ on $k(k-1)/2$ df (Definition 12.2.1; side effects $X^2=9.33$, $p=0.025$), Cochran's $Q$ for several conditions.
- Independence: Pearson $\chi^2=\sum(O-E)^2/E$ and $G^2=2\sum O\log(O/E)$ (Proposition 12.3.1), both $\chi^2_{(r-1)(c-1)}$, equivalent in large samples, unreliable for sparse tables; $G^2$ extends to nested models.
- Exact tests: Fisher (Definition 12.4.1) conditions on the margins, hypergeometric null distribution, conditioning removes the nuisance parameter; Fisher–Freeman–Halton (Definition 12.4.2) for $r\times c$, Monte Carlo for large tables (scarlet fever: exact $p=0.026$, $\chi^2$ $p=0.134$).
- Stratification: odds ratio $ad/(bc)$ (Definition 12.5.1); Mantel–Haenszel test and common odds ratio (Definition 12.5.2; drugs: $\chi^2_{\mathrm{MH}}=21.94$, $\widehat{\mathrm{OR}}_{\mathrm{MH}}=3.56$, crude OR $=1$); weights $b_kc_k/T_k$; valid summary only under homogeneity (Breslow–Day); otherwise report strata.
- Ordered categories: WMW with midranks and the full tie correction (side effects: $z=-3.12$, $p=0.002$, against $0.013$ ignoring order); ridit analysis (Definition 12.6.1) reports $\mathbb{P}(Y>X)+\frac12\mathbb{P}(Y=X)$.
- Log-linear models (Definition 12.7.1): $\log\mu$ linear in main effects and interactions; Poisson GLM, not `lm(log(y))`; three-factor interaction = conditional odds ratios vary (Proposition 12.7.1) = effect modification. Test it by the likelihood ratio between nested hierarchical models (smoking: $G^2=12.10$, $4$ df, $p=0.017$), not by single Wald coefficients. With person-years, Poisson rate regression with offset $\log t$ is the natural model (same conclusion; rate ratio decreasing with age).

## Questions

1. For Example 12.2.1, the marginal distributions of severity under the old and new formulations are $(90,44,24)$ and $(104,35,19)$. Explain why symmetry implies marginal homogeneity, and give a $3\times3$ table that has homogeneous margins but is not symmetric.

   **Answer** Under symmetry $p_{ij}=p_{ji}$, so the row margin $p_{i\cdot}=\sum_jp_{ij}=\sum_jp_{ji}=p_{\cdot i}$ equals the column margin. The converse fails for $k\ge3$: the table with rows $(0,1,0)$, $(0,0,1)$, $(1,0,0)$ (each count $10$, say) has all row and column totals equal to $10$, but $n_{12}=10\ne n_{21}=0$; patients move in a cycle None $\to$ Slight $\to$ Severe $\to$ None. Bowker's test rejects for such a table, a test of marginal homogeneity (Stuart–Maxwell) does not.
2. In the tea experiment, how many cups out of four must the lady identify correctly for significance at the $5\%$ level, and what is the actual size of the test? How many cups of each kind would be needed for a single error to be compatible with significance at the $5\%$ level?

   **Answer** Only a perfect identification, $x=4$, with $\mathbb{P}(X=4)=1/70=0.014$; $\mathbb{P}(X\ge3)=17/70=0.243$. The test at nominal level $0.05$ has actual size $0.014$: it is very conservative because of the discreteness. With $n$ cups of each kind, $\mathbb{P}(X\ge n-1)=\bigl(1+n^2\bigr)/\binom{2n}{n}$, which is $17/70=0.243$ for $n=4$, $26/252=0.103$ for $n=5$ and $37/924=0.040$ for $n=6$. So six cups of each kind are needed before one error is still significant at the $5\%$ level.
3. Show that $\widehat{\mathrm{OR}}_{\mathrm{MH}}$ is a weighted average of the stratum odds ratios with weights proportional to $b_kc_k/T_k$, and compute the weights for Example 12.5.1.

   **Answer** $\widehat{\mathrm{OR}}_k\cdot b_kc_k/T_k=a_kd_k/T_k$, so $\sum_ka_kd_k/T_k=\sum_k\widehat{\mathrm{OR}}_k\,b_kc_k/T_k$, and dividing by $\sum_lb_lc_l/T_l$ gives the weighted average. For the hospitals, $b_1c_1/T_1=15\times92/247=5.59$ and $b_2c_2/T_2=135\times5/247=2.73$, so the weights are $0.67$ and $0.33$, although the two hospitals have the same size $247$; the estimate is $0.67\times3.26+0.33\times4.18=3.56$, not the arithmetic mean $3.72$.
4. Why is Pearson's chi-squared test for the ordered side-effect table of Example 12.6.1 less powerful than the WMW test against the alternative "drug A causes more severe side effects", and in what situation could it be more powerful?

   **Answer** Under the directional alternative, the evidence is concentrated in one direction: drug A's patients are shifted toward the severe end. The WMW test, essentially a one-degree-of-freedom test for a shift in mean ranks, puts all its power there. Pearson's statistic spreads its power over all $4$ degrees of freedom, that is, over any pattern of differences between the two distributions, including those irrelevant to severity, and its null distribution is correspondingly wider. It can be more powerful when the difference is not a shift along the order, for instance when one drug produces both more mild and more fatal reactions (a difference in spread); then the WMW statistic may be near $n_1n_2/2$, but a significant chi-squared result is not evidence that one drug is more harmful in the sense of ordered severity.
5. In Example 12.7.1, why is the youngest age group a poor choice of reference level for the log-linear model, and how would changing the reference level change the reported Wald tests and the likelihood ratio test of the three-factor interaction?

   **Answer** The reference group's conditional odds ratio rests on only $2$ deaths among non-smokers, so its log odds ratio has a large standard error ($\sqrt{1/32+1/2}\approx0.73$), and every three-factor coefficient, being a difference from it, inherits that imprecision; the individual Wald tests are weak and depend on which group is the reference. Choosing another reference (for example the middle age group, with $28$ deaths among non-smokers) changes the individual coefficients, their standard errors and their $p$-values. The likelihood ratio test compares the same two models (saturated and no three-factor interaction), which do not depend on the parametrization, so $G^2=12.10$ on $4$ df is unchanged.
6. Compare the two ways of analysing the smoking data: the $5\times2\times2$ log-linear model with "person-years minus deaths" as survivors, and the Poisson rate model with offset $\log t$. When would they give noticeably different answers?

   **Answer** The log-linear model treats each person-year as a Bernoulli trial and estimates odds ratios; the rate model treats deaths as Poisson counts in the observed person-time and estimates rate ratios. When the event is rare, $p/(1-p)\approx p\approx$ rate, the binomial and Poisson likelihoods are nearly the same, and the two analyses agree, as here (deviances $12.10$ and $12.13$, odds ratios and rate ratios equal to two decimals). They would differ when the event is common in some cells (say, rates of $20\%$ per unit of time or more), when person-time is not made of comparable units (person-years are not independent trials of identical people), or when interest lies in risks over a fixed period rather than rates; the rate model is the correct model for person-time data in any case.
