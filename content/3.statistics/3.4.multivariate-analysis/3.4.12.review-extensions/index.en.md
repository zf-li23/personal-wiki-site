---
title: Review and Extensions
description: "A compact review of the course (goals, models, solutions and assumptions of each method) and extensions: false discovery rate, correspondence analysis, sparse and logistic PCA, regularized discriminant analysis, logistic regression, k-nearest neighbors, network models and matrix factor models."
---

This chapter first reviews the course as a whole: the questions that multivariate methods answer, a side-by-side comparison of the methods, and the common framework of modeling, solution and evaluation that they share. It then introduces a number of extensions, each of which either solves an old problem better, treats a similar problem with a new method, or handles a new type of data: the false discovery rate for testing many hypotheses at once, correspondence analysis for contingency tables, sparse and logistic versions of principal component analysis, regularized discriminant analysis, logistic regression and $k$-nearest neighbors for classification, and models for networks and matrix-valued time series. The extensions are introductions to problems rather than complete treatments; several of them are developed in later courses such as [Statistical Computing](/3.5), [Nonparametric Statistics](/3.6), [Bayesian Statistics](/3.7) and [Causal Inference](/3.9).

## 12.1. Course Review

### 12.1.1. A Map of Multivariate Analysis

Multivariate methods can be organized by the aspect of the random vector $\boldsymbol{X}$ they study.

| Aspect | Question | Methods |
|---|---|---|
| Location of $\boldsymbol{X}$ | Is the mean vector equal to a given value, or are two mean vectors equal? | one-sample and two-sample tests based on **Hotelling's T²** ([3.4.3](/3.4.3), [3.4.4](/3.4.4)) |
| Variation of $\boldsymbol{X}$ | What are the main directions of variation, and can a few variables or factors explain them? | **principal component analysis** ([3.4.5](/3.4.5)), **multidimensional scaling** ([3.4.6](/3.4.6)), **factor analysis** ([3.4.8](/3.4.8)) |
| Relation of $\boldsymbol{X}_1$ and $\boldsymbol{X}_2$ | How are two sets of variables associated? | **canonical correlation analysis** ([3.4.9](/3.4.9)) |
| Relation of $\boldsymbol{X}$ and a latent $Y$ | Are there unobserved groups? | **cluster analysis**: hierarchical, $k$-means, EM ([3.4.11](/3.4.11)) |
| Relation of $\boldsymbol{X}$ and an observed $Y$, $Y$ continuous | How does $Y$ depend on $\boldsymbol{X}$? | linear regression ([3.4.7](/3.4.7)) |
| Relation of $\boldsymbol{X}$ and an observed $Y$, $Y$ discrete | To which group does a new observation belong? | Fisher's discriminant; minimum ECM rules, LDA and QDA under normality ([3.4.10](/3.4.10)) |

Principal components, multidimensional scaling, factor analysis, canonical correlation and clustering are unsupervised (no response variable is used); regression and discriminant analysis are supervised.

### 12.1.2. The Methods at a Glance

| Method | Goal | Model or objective (population) | Solution | Assumptions and remarks |
|---|---|---|---|---|
| Hotelling's $T^2$ ([3.4.3](/3.4.3)) | test $H_0\colon\boldsymbol{\mu} = \boldsymbol{\mu}_0$; confidence region for $\boldsymbol{\mu}$ | $T^2 = n(\bar{\boldsymbol{x}}-\boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}}-\boldsymbol{\mu}_0)$, $\frac{n-p}{(n-1)p}T^2 \sim F_{p,n-p}$ | ellipsoidal confidence region; simultaneous $T^2$ or Bonferroni intervals | normal population; the likelihood ratio test |
| Two mean vectors ([3.4.4](/3.4.4)) | test $\boldsymbol{\mu}_1 = \boldsymbol{\mu}_2$ (paired or independent samples) | $T^2 = (\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}\bigl[(\tfrac1{n_1}+\tfrac1{n_2})S_{\mathrm{pooled}}\bigr]^{-1}(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)$ | $F$ distribution; $\chi^2_p$ for large samples | equal covariances, or large samples when they differ |
| PCA ([3.4.5](/3.4.5)) | summarize variation by few uncorrelated combinations | $\max\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X})$ subject to $\boldsymbol{a}^{\mathsf T}\boldsymbol{a} = 1$, orthogonal to earlier components | eigenvectors of $\Sigma$ (or of the correlation matrix); analytic | no distributional assumption; not scale invariant |
| MDS and kernel PCA ([3.4.6](/3.4.6)) | low-dimensional configuration from distances; nonlinear structure | preserve given distances; PCA in a feature space defined by a kernel | eigendecomposition of the double-centered distance or kernel matrix | classical MDS with Euclidean distances is PCA |
| Linear regression ([3.4.7](/3.4.7)) | predict a continuous response | $\boldsymbol{Y} = Z\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ | least squares; penalized versions for collinearity | inference under normal errors |
| Factor analysis ([3.4.8](/3.4.8)) | explain covariances by $m < p$ latent factors | $\boldsymbol{X} - \boldsymbol{\mu} = L\boldsymbol{F} + \boldsymbol{\varepsilon}$, $\Sigma = LL^{\mathsf T} + \Psi$ | principal component or maximum likelihood estimation; rotation; factor scores | loadings identified only up to rotation; ML assumes normality |
| CCA ([3.4.9](/3.4.9)) | association between two sets of variables | $\max\operatorname{Corr}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_1, \boldsymbol{b}^{\mathsf T}\boldsymbol{X}_2)$ | eigenvectors of $\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\Sigma_{11}^{-1/2}$; analytic | tests of correlations assume normality |
| Discriminant analysis ([3.4.10](/3.4.10)) | classify into known groups | Fisher: $\max\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}/\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}$; likelihood: minimize the ECM | eigenvectors of $W^{-1}B$; LDA, QDA | equal covariances for LDA; normality for the optimality of LDA and QDA |
| Cluster analysis ([3.4.11](/3.4.11)) | discover unknown groups | linkage-based merging; $\min$ SSE; Gaussian mixture likelihood | iterative: merging, alternating $k$-means steps, EM | choice of distance and $k$; local optima |

### 12.1.3. A Common Framework

Most methods of the course follow the same path from population to sample.

- Modeling, at the population level. A hypothesis test starts from $H_0$ and its logic is "if $H_0$ holds, then the statistic behaves in a known way; if the statistic does not behave that way, reject $H_0$". PCA, CCA and discriminant analysis start from an objective to maximize, which has an analytic solution by an eigendecomposition; clustering also starts from an objective, but its solution needs iterative computation.
- Properties of the model or the solution: what the components, factors or discriminants mean, which transformations leave them invariant, how they relate to each other (for example, LDA and CCA in [3.4.10](/3.4.10#sec-10.5.2), classical MDS and PCA).
- Application, at the sample level: estimate the population quantities, and interpret every figure and table.
- Evaluation, including the choice of tuning parameters and model selection. Indices and methods differ in their direction (better interpretation or smaller error) and in their type: parametric criteria such as AIC and BIC, or nonparametric ones such as **cross-validation**.

Throughout, one needs three kinds of ability: algebra (the eigen- and singular value decompositions behind almost every method), geometry (projections, ellipsoids, distances) and numerical computation; and three kinds of task: identifying and modeling a problem, solving it, and interpreting the results.

Factor analysis is a good template for reviewing a method in this way.

| Step | Content |
|---|---|
| Motivation | dimension reduction ($m < p$) and interpretation |
| Model | $\boldsymbol{X} = \boldsymbol{\mu} + L\boldsymbol{F} + \boldsymbol{\varepsilon}$ with $\mathbb{E}\boldsymbol{F} = \boldsymbol{0}$, $\operatorname{Cov}(\boldsymbol{F}) = I$, $\operatorname{Cov}(\boldsymbol{\varepsilon}) = \Psi$ diagonal, $\boldsymbol{F}$ and $\boldsymbol{\varepsilon}$ uncorrelated, which implies $\Sigma = LL^{\mathsf T} + \Psi$ |
| Standardized model | $V^{-1/2}(\boldsymbol{X}-\boldsymbol{\mu}) = L_z\boldsymbol{F} + \boldsymbol{\varepsilon}_z$, $\rho = L_zL_z^{\mathsf T} + \Psi_z$, $L_z = V^{-1/2}L$: the model is scale invariant |
| Goals | population level: $L$ and $\Psi$ (they exist only for some $\Sigma$, and $L$ is unique only up to rotation); unit level: the factor scores $\boldsymbol{F}$ |
| Principal component solution | $\hat L = [\sqrt{\hat\lambda_1}\hat{\boldsymbol{e}}_1, \dots, \sqrt{\hat\lambda_m}\hat{\boldsymbol{e}}_m]$; convenient (earlier columns do not change when $m$ grows) and similar to PCA; but it ignores the structure of the model (for instance that $\Psi$ is diagonal) |
| Maximum likelihood solution | maximize the normal likelihood under the identifiability constraint that $L^{\mathsf T}\Psi^{-1}L$ is diagonal; equivalent for $S$ and $R$; allows a likelihood ratio test of the number of factors; but needs the extra assumption of multivariate normality |

### 12.1.4. Carrying Out a Multivariate Analysis

A data analysis project typically proceeds as follows.

1. Start from the data and the motivating question; explore the data (EDA) before choosing methods.
2. Plan the analysis: preprocessing (EDA, scaling, transformations, outliers), then a combination of methods, for example PCA followed by LDA, PCA followed by clustering, or factor analysis followed by clustering of the factor scores.
3. Interpret each figure and each table, draw conclusions, and discuss limitations.

The summary of such a project should state three things: the data, the question, and the conclusion.

## 12.2. Multiple Testing and the False Discovery Rate

### 12.2.1. The Family-Wise Error Rate

Instead of one hypothesis about a mean vector, $H_0\colon\boldsymbol{\mu}_1 = \boldsymbol{\mu}_2$, we may want to test each coordinate separately, $H_{0j}\colon\mu_{1j} = \mu_{2j}$ for $j = 1, \dots, m$, to find out which variables differ. The simultaneous intervals based on Hotelling's $T^2$ do this for moderate $m$, but the classical tests of this course fail when the number of variables exceeds the sample size. The methods below apply in that setting as well, and the problem of multiple testing arises whenever more than one hypothesis is tested.

Let $p_j$ be the **p-value** of $H_{0j}$; a level-$\alpha$ test rejects $H_{0j}$ when $p_j < \alpha$, so each test has probability $\alpha$ of a **type I error**. When $m$ tests are performed, the probability of at least one type I error is larger than $\alpha$.

**Definition 12.2.1 (Family-Wise Error Rate)** The **family-wise error rate** (FWER) of a multiple testing procedure is the probability of making at least one type I error among the $m$ tests.

The **Bonferroni correction** tests each hypothesis at level $\alpha/m$. By the union bound, if $I_0$ is the set of true null hypotheses,

$$
\mathbb{P}\Bigl(\bigcup_{j\in I_0}\{p_j < \alpha/m\}\Bigr) \le \sum_{j\in I_0}\mathbb{P}(p_j < \alpha/m) \le m\cdot\frac{\alpha}{m} = \alpha,
$$
so the FWER is controlled at level $\alpha$, whatever the dependence among the tests.

**Example 12.2.1** In a gene-expression study of prostate cancer (Efron, *Large-Scale Inference*, 2010), expression levels of $m = 6033$ genes were measured for $n_1 = 52$ prostate cancer patients and $n_2 = 50$ healthy controls, and the scientific question is which genes are differentially expressed. For each gene a two-sample $t$ statistic is computed and transformed into a $z$-value, $z_j = \Phi^{-1}(F_{t,100}(t_j))$, which is standard normal under $H_{0j}$. With the Bonferroni threshold at level $0.05$, only $2$ of the $6033$ genes are declared significant, although the histogram of the $z$-values has visibly heavier tails than the null density: controlling the FWER makes very few discoveries.

### 12.2.2. The False Discovery Rate

Controlling the FWER is conservative. It might not be so bad to make a few type I errors, as long as they are a small proportion of all the rejections. Classify the $m$ tests as follows.

| | $H_0$ true | $H_0$ false | Total |
|---|---|---|---|
| declared significant | $V$ | $S$ | $R$ |
| declared non-significant | $U$ | $T$ | $m - R$ |
| Total | $m_0$ | $m - m_0$ | $m$ |

Only $m$ and $R$ are observed. In this notation $\mathrm{FWER} = \mathbb{P}(V \ge 1)$.

**Definition 12.2.2 (False Discovery Rate)** The false discovery proportion is $Q = V/\max(R, 1)$ (the proportion of false rejections among all rejections, set to $0$ when nothing is rejected), and its expectation

$$
\mathrm{FDR} = \mathbb{E}[Q] = \mathbb{E}\left[\frac{V}{\max(R, 1)}\right]
$$
is the **false discovery rate** (Benjamini and Hochberg, 1995).

Two basic facts relate the FDR to the FWER.

1. If all the null hypotheses are true ($m_0 = m$), then $V = R$, so $Q = \boldsymbol{1}_{\{V\ge1\}}$ and $\mathrm{FDR} = \mathbb{P}(V \ge 1) = \mathrm{FWER}$.
2. In general $Q \le \boldsymbol{1}_{\{V\ge1\}}$, so $\mathrm{FDR} \le \mathrm{FWER}$, and any procedure that controls the FWER also controls the FDR. A procedure that controls only the FDR is less strict and can have higher power. When $m - m_0$ is large, $S$ tends to be large, and the difference between $\mathbb{E}[Q]$ and $\mathbb{P}(V \ge 1)$ is large.

Controlling the FDR at level $\alpha$ is therefore less conservative than controlling the FWER at level $\alpha$: it tolerates several type I errors, as long as they do not account for too high a proportion of the "discoveries" (the rejected null hypotheses).

### 12.2.3. The Benjamini–Hochberg Procedure

**Algorithm 12.2.1 (Benjamini–Hochberg Procedure)** Let $p_{(1)} \le p_{(2)} \le \cdots \le p_{(m)}$ be the ordered p-values and $H_{(i)}$ the corresponding hypotheses, and fix $\alpha \in (0, 1)$.

1. Let $k = \max\{i : p_{(i)} \le \frac{i}{m}\alpha\}$ (and $k = 0$ if no such $i$ exists).
2. Reject $H_{(1)}, \dots, H_{(k)}$.

The thresholds $\frac{i}{m}\alpha$ increase linearly from the Bonferroni threshold $\alpha/m$ to $\alpha$. The procedure is a step-up procedure: it searches from the largest p-value downward and rejects all hypotheses up to the last crossing, even if some smaller p-values lie above their own thresholds.

**Theorem 12.2.1** If the test statistics are independent and the p-values of the true null hypotheses are uniformly distributed on $(0, 1)$, the Benjamini–Hochberg procedure satisfies

$$
\mathrm{FDR} = \frac{m_0}{m}\alpha \le \alpha.
$$
The bound $\mathrm{FDR} \le \alpha$ also holds under a positive dependence condition (Benjamini and Yekutieli, 2001).

**Proof** Let $\alpha_k = \frac{k}{m}\alpha$. For a true null hypothesis $H_i$ and $k = 1, \dots, m$, let $C_k^{(i)}$ be the event, determined by the other $m-1$ p-values, that if $H_i$ is rejected then exactly $k$ hypotheses are rejected in total. For each $i$ these events are disjoint, and one of them occurs, so $\sum_k\mathbb{P}(C_k^{(i)}) = 1$. For the step-up procedure, $\{H_i \text{ rejected and } R = k\} = \{p_i \le \alpha_k\}\cap C_k^{(i)}$. Hence, summing over the $m_0$ true nulls and using independence,

$$
\begin{aligned}
\mathbb{E}[Q] &= \sum_{i\in I_0}\sum_{k=1}^m\frac1k\,\mathbb{P}\bigl(p_i \le \alpha_k,\ C_k^{(i)}\bigr) = \sum_{i\in I_0}\sum_{k=1}^m\frac1k\,\mathbb{P}(p_i \le \alpha_k)\,\mathbb{P}\bigl(C_k^{(i)}\bigr) \\
&= \sum_{i\in I_0}\sum_{k=1}^m\frac1k\cdot\frac{k}{m}\alpha\,\mathbb{P}\bigl(C_k^{(i)}\bigr) = \frac{\alpha}{m}\sum_{i\in I_0}\sum_{k=1}^m\mathbb{P}\bigl(C_k^{(i)}\bigr) = \frac{m_0}{m}\alpha. \qquad \square
\end{aligned}
$$

**Example 12.2.2** For the prostate data, the Benjamini–Hochberg procedure at level $0.05$ makes considerably more discoveries than Bonferroni: $21$ genes instead of $2$. In expectation, at most $5\%$ of these discoveries are false.

![Benjamini-Hochberg procedure on simulated data: 1000 tests, of which 100 have a true effect. Sorted p-values against their rank, the BH line i alpha/m and the Bonferroni threshold alpha/m (log scale); BH rejects all hypotheses up to the last p-value below its line.](./plots/bh-procedure.py)

More recent work extends FDR control in many directions, for example to e-values (Wang and Ramdas, 2022).

## 12.3. Correspondence Analysis

### 12.3.1. Chi-Square Statistics of a Contingency Table

Correspondence analysis treats a new type of data, a two-way **contingency table** of counts. For example, the abundances of five species at three sites are

$$
F = [f_{ij}] = \begin{bmatrix} 45 & 10 & 15 & 0 & 10 \\ 25 & 8 & 10 & 0 & 3 \\ 7 & 15 & 20 & 14 & 12 \end{bmatrix}, \qquad \text{row totals } f_{i+} = 80, 46, 68, \quad \text{column totals } f_{+j} = 77, 33, 45, 14, 25, \quad f_{++} = 194,
$$
with rows Site 1–3 and columns Sp 1–5. Is there an association between sites and species? Pearson's chi-square **test of independence** answers this. Let $r$ and $c$ be the numbers of rows and columns, and define the *correspondence matrix* $P = [p_{ij}]$, $p_{ij} = f_{ij}/f_{++}$, with row masses $p_{i+} = f_{i+}/f_{++}$ and column masses $p_{+j} = f_{+j}/f_{++}$. Then

$$
\chi^2 = \sum_{i=1}^r\sum_{j=1}^c\frac{\bigl(f_{ij} - f_{++}\frac{f_{i+}}{f_{++}}\frac{f_{+j}}{f_{++}}\bigr)^2}{f_{++}\frac{f_{i+}}{f_{++}}\frac{f_{+j}}{f_{++}}} = f_{++}\sum_{i=1}^r\sum_{j=1}^c\frac{(p_{ij} - p_{i+}p_{+j})^2}{p_{i+}p_{+j}},
$$
which under independence has approximately the **chi-square distribution** with $(r-1)(c-1)$ degrees of freedom. For the example, $\chi^2 = 55.25$ on $8$ degrees of freedom, a p-value of about $4\times10^{-9}$: sites and species are clearly associated. Correspondence analysis shows how.

### 12.3.2. Computation

Transform the table into the standardized residuals, whose squares are the contributions to the chi-square statistic,

$$
\bar q_{ij} = \frac{p_{ij} - p_{i+}p_{+j}}{\sqrt{p_{i+}p_{+j}}}, \qquad \bar Q = [\bar q_{ij}] = D_r^{-1/2}(P - \boldsymbol{r}\boldsymbol{c}^{\mathsf T})D_c^{-1/2},
$$
where $D_r = \operatorname{diag}(p_{1+}, \dots, p_{r+})$, $D_c = \operatorname{diag}(p_{+1}, \dots, p_{+c})$, and $\boldsymbol{r}, \boldsymbol{c}$ are the vectors of row and column masses. For the example,

$$
\bar Q = \begin{bmatrix} 0.169 & -0.070 & -0.059 & -0.173 & -0.007 \\ 0.113 & 0.004 & -0.015 & -0.131 & -0.086 \\ -0.276 & 0.072 & 0.076 & 0.295 & 0.079 \end{bmatrix},
$$
and $\chi^2 = f_{++}\sum_{i,j}\bar q_{ij}^2 = f_{++}\|\bar Q\|_{\mathrm{F}}^2$. The matrix $P - \boldsymbol{r}\boldsymbol{c}^{\mathsf T}$ is the covariance matrix $\Sigma_{12}$ between the row-indicator and column-indicator vectors of a single observation drawn from the table, so $\bar Q = D_r^{-1/2}\Sigma_{12}D_c^{-1/2}$ looks like the matrix analyzed in canonical correlation analysis. To extract the relations it contains, take the **singular value decomposition**

$$
\bar Q = U\Lambda V^{\mathsf T}, \qquad U \in \mathbb{R}^{r\times k}, \quad \Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_k), \quad V \in \mathbb{R}^{c\times k},
$$
with $k \le \min(r, c) - 1$ nonzero singular values. The total inertia $\chi^2/f_{++} = \sum_l\lambda_l^2$ is split among the axes; in the example $\lambda_1 = 0.527$ and $\lambda_2 = 0.083$, so the first axis carries $97.6\%$ of the inertia.

**Definition 12.3.1 (Correspondence Analysis)** **Correspondence analysis** (CA) represents the rows and columns of a contingency table by points in a low-dimensional plot, the CA biplot, whose positions show the associations, using the coordinates

| | Scaling 1 | Scaling 2 |
|---|---|---|
| rows (sites) | $F = D_r^{-1/2}U\Lambda$ | $B = D_r^{-1/2}U$ |
| columns (species) | $A = D_c^{-1/2}V$ | $G = D_c^{-1/2}V\Lambda$ |

The data must be nonnegative and frequency-like.

Viewing each row as a profile $(p_{i1}/p_{i+}, \dots, p_{ic}/p_{i+})$, the natural distance between two rows is the *chi-square distance*

$$
D^2(i, i') = \sum_{j=1}^c\frac{1}{p_{+j}}\left(\frac{p_{ij}}{p_{i+}} - \frac{p_{i'j}}{p_{i'+}}\right)^2,
$$
the Euclidean distance between profiles with each column weighted by the inverse of its mass, so that rare species are not swamped by abundant ones. CA preserves the chi-square distances: in scaling 1 the Euclidean distances among the row points $F$ (using all $k$ axes) equal the chi-square distances among the row profiles, and in scaling 2 the same holds for the column points $G$.

- Scaling 1 is appropriate when the main interest is the relations among the sites. The species are placed so that a site lies near the species that are abundant there. In the example, species 1 is closer to sites 1 and 2 than to site 3, because it is more abundant at sites 1 and 2.
- Scaling 2 is appropriate when the main interest is the relations among the species. The sites are placed around the species according to their abundances: species 5 is more abundant at sites 1 and 3 than at site 2, species 1 is more abundant at sites 1 and 2 than at site 3, and species 4, found only at site 3, falls on top of it.

![CA biplots of the sites-by-species table. Left (scaling 1): sites at chi-square distances of one another, with species positioned by their contributions. Right (scaling 2): species at chi-square distances of one another, with sites positioned by species abundances.](./plots/ca-biplots.py)

**Remark 12.3.1 (CA and CCA)** CA can be written as a canonical correlation problem. With $\boldsymbol{X}$ the row indicator and $\boldsymbol{Y}$ the column indicator of a random observation from the table, CA solves

$$
\max_{\|\boldsymbol{a}\| = \|\boldsymbol{b}\| = 1}\operatorname{Corr}\bigl(\boldsymbol{a}^{\mathsf T}D_r^{-1/2}\boldsymbol{X}, \boldsymbol{b}^{\mathsf T}D_c^{-1/2}\boldsymbol{Y}\bigr) = \max_{\|\boldsymbol{a}\| = \|\boldsymbol{b}\| = 1}\boldsymbol{a}^{\mathsf T}D_r^{-1/2}\Sigma_{12}D_c^{-1/2}\boldsymbol{b},
$$
which parallels CCA, $\max_{\|\boldsymbol{a}\| = \|\boldsymbol{b}\| = 1}\boldsymbol{a}^{\mathsf T}\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1/2}\boldsymbol{b}$; here $D_r$ and $D_c$ play the roles of $\Sigma_{11}$ and $\Sigma_{22}$ (they are the covariance matrices of the indicators up to the rank-one term that removes the trivial solution). The singular values of $\bar Q$ are the canonical correlations between the row and column categories. In R, CA is available, for example, in the package vegan.

## 12.4. Extensions of PCA

### 12.4.1. Sparse PCA

Let $X$ be an $n \times p$ data matrix with column means subtracted. PCA can be written in two equivalent ways:

$$
\max_{\boldsymbol{a}}\boldsymbol{a}^{\mathsf T}X^{\mathsf T}X\boldsymbol{a} \ \text{ subject to } \boldsymbol{a}^{\mathsf T}\boldsymbol{a} = 1, \qquad \text{or} \qquad \min_{Y, A}\|X - YA^{\mathsf T}\|_{\mathrm{F}}^2 \ \text{ subject to } A^{\mathsf T}A = I_r,
$$
with $A$ the $p \times r$ matrix of loadings and $Y = XA$ the $n \times r$ matrix of scores. Each principal component usually involves all $p$ variables, which makes it hard to interpret when $p$ is large. The idea of *sparse PCA* is similar to the **Lasso**: add $\ell_1$ penalties,

$$
\min_{Y, A}\|X - YA^{\mathsf T}\|_{\mathrm{F}}^2 + \gamma\sum_{i=1}^n\|\boldsymbol{y}_i\|_1 + \lambda\sum_{j=1}^p\|\boldsymbol{a}_j\|_1,
$$
where $\boldsymbol{y}_i$ are the rows of $Y$ and $\boldsymbol{a}_j$ the rows of $A$. The penalty on $A$ makes the meaning of each component rely on few original variables; the penalty on $Y$ makes each observation's projection rely on few components. An $\ell_1$ penalty produces exact zeros, whereas an $\ell_2$ penalty only makes the coefficients small overall. Different formulations have been proposed, for example by Zou, Hastie and Tibshirani (2006), who use an elastic-net regression formulation, and by d'Aspremont et al. (2007), who use a semidefinite relaxation; in a gene-expression example of the latter, a leading component that involved 500 genes was replaced by a sparse one involving only 14.

### 12.4.2. PCA for Other Data Types

For binary data $x_{ij} \in \{-1, 1\}$, squared error is not a natural loss. *Logistic PCA* replaces it by the logistic loss,

$$
\min_{Y, A}\sum_{i=1}^n\sum_{j=1}^p\ln\Bigl(1 + \exp\Bigl\{-x_{ij}\sum_{k=1}^r y_{ik}A_{jk}\Bigr\}\Bigr),
$$
so that $\sum_k y_{ik}A_{jk}$ is the natural parameter (log-odds) of $x_{ij}$. The general principle is that ordinary PCA is the low-rank fit under the normal model, and other members of the natural exponential family $p(x; \theta) = p_0(x)\exp\{\theta x - G(\theta)\}$ lead to PCA for other data types, with the squared error replaced by the corresponding Bregman divergence, the gap between a convex function $G$ and its linear approximation. Poisson PCA for counts and versions for ordinal data (Rennie and Srebro, 2005) follow the same pattern; categorical principal component analysis instead transforms the categories by linear, polynomial or spline functions before applying PCA.

## 12.5. Extensions of Discriminant Analysis

### 12.5.1. Regularized Discriminant Analysis

LDA uses one pooled covariance matrix and QDA a separate one for each group. *Regularized discriminant analysis* (RDA) is a compromise between them: it shrinks each $\hat\Sigma_k$ toward the pooled covariance matrix $\hat\Sigma$,

$$
\hat\Sigma_k(\alpha) = \alpha\hat\Sigma_k + (1-\alpha)\hat\Sigma, \qquad \alpha \in [0, 1],
$$
and replaces $\hat\Sigma_k$ by $\hat\Sigma_k(\alpha)$ in the quadratic discriminant functions. The tuning parameter $\alpha$ determines whether the covariances are estimated separately ($\alpha = 1$, QDA) or pooled ($\alpha = 0$, LDA). Additionally, $\hat\Sigma$ itself can be shrunk toward a scalar covariance matrix, $\hat\Sigma(\gamma) = \gamma\hat\Sigma + (1-\gamma)\hat\sigma^2 I$, where $\gamma = 1$ gives the pooled covariance and $\gamma = 0$ the scalar one. Replacing $\hat\Sigma_k$ by $\hat\Sigma_k(\alpha, \gamma)$ gives a two-parameter family, with $\alpha$ and $\gamma$ chosen by cross-validation. As a regularization technique, RDA is particularly useful when there are many potentially correlated features, so that the sample covariance matrices are unstable or singular; the simple version $S_{\mathrm{pooled}} + \lambda I_p$ was mentioned in [3.4.10](/3.4.10#sec-10.7.3).

### 12.5.2. Logistic Regression

The Bayes classifier of [3.4.10](/3.4.10#sec-10.3.3) compares the posterior probabilities

$$
\mathbb{P}(\pi_1 \mid \boldsymbol{x}) = \frac{p_1f_1(\boldsymbol{x})}{p_1f_1(\boldsymbol{x}) + p_2f_2(\boldsymbol{x})}, \qquad \mathbb{P}(\pi_2 \mid \boldsymbol{x}) = \frac{p_2f_2(\boldsymbol{x})}{p_1f_1(\boldsymbol{x}) + p_2f_2(\boldsymbol{x})}.
$$
LDA obtains them by modeling the densities $f_i$. Logistic regression models the posterior probabilities directly.

**Definition 12.5.1 (Logistic Regression)** For $K$ groups, the **logistic regression** model specifies, for $k = 1, \dots, K-1$,

$$
\ln\frac{\mathbb{P}(\pi_k \mid \boldsymbol{x})}{\mathbb{P}(\pi_K \mid \boldsymbol{x})} = \beta_{0k} + \boldsymbol{\beta}_k^{\mathsf T}\boldsymbol{x},
$$
equivalently

$$
\mathbb{P}(\pi_k \mid \boldsymbol{x}) = \frac{\exp(\beta_{0k} + \boldsymbol{\beta}_k^{\mathsf T}\boldsymbol{x})}{1 + \sum_{l=1}^{K-1}\exp(\beta_{0l} + \boldsymbol{\beta}_l^{\mathsf T}\boldsymbol{x})}, \quad k < K, \qquad \mathbb{P}(\pi_K \mid \boldsymbol{x}) = \frac{1}{1 + \sum_{l=1}^{K-1}\exp(\beta_{0l} + \boldsymbol{\beta}_l^{\mathsf T}\boldsymbol{x})}.
$$
The parameters are estimated by maximizing the conditional likelihood of the labels given the $\boldsymbol{x}_i$, and a new observation is assigned to the group with the largest fitted probability. For $K = 2$ the model is $\ln\frac{p}{1-p} = \beta_0 + \boldsymbol{\beta}^{\mathsf T}\boldsymbol{x}$ with $p = \mathbb{P}(\pi_1\mid\boldsymbol{x})$.

The two methods are closely related. Under the LDA model, by the proof of Theorem 10.4.1,

$$
\ln\frac{\mathbb{P}(\pi_1 \mid \boldsymbol{x})}{\mathbb{P}(\pi_2 \mid \boldsymbol{x})} = \ln\frac{p_1}{p_2} + (\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}\boldsymbol{x} - \frac12(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1+\boldsymbol{\mu}_2),
$$
which is linear in $\boldsymbol{x}$: the log posterior odds have exactly the logistic form. The difference lies in estimation. LDA estimates the joint distribution of $(\boldsymbol{x}, \text{group})$ and is more efficient when the normal model holds; logistic regression makes no assumption about the distribution of $\boldsymbol{x}$, so it is more robust, and its coefficients have a clear interpretation as log odds ratios. For the iris data, logistic regression separates two species, and with the multiclass model all three, with error rates similar to LDA. Logistic regression is the subject of courses on generalized linear models and categorical data.

### 12.5.3. k-Nearest Neighbors

**Algorithm 12.5.1 (k-Nearest Neighbors)** Given labeled data $(\boldsymbol{x}_i, y_i)$, a distance between points (for example Euclidean) and a number of neighbors $k$ (for example $k = 5$): to classify a new unit $\boldsymbol{x}$, find the $k$ training points nearest to $\boldsymbol{x}$ and assign $\boldsymbol{x}$ to the group that occurs most often among them.

The idea of the $k$-nearest neighbors (KNN) classifier is the proverb "birds of a feather flock together". Because it relies on distances, the variables should be standardized first. The number $k$ controls the flexibility of the rule: $k = 1$ gives a very irregular boundary that follows every training point, while a large $k$ (say $k = 30$) gives a smooth boundary that may miss real structure. It is chosen by prediction accuracy, using cross-validation: for each $k$ in a range, compute the cross-validated prediction error (for example by $10$-fold cross-validation on the training set), choose the $k$ with the smallest validation error ($k = 6$ in an example with the iris data), and finally evaluate the chosen rule once on a separate test set to estimate its error.

KNN is a nonparametric method: it needs no distributional assumption, is simple to implement, and with moderate $k$ it is not much affected by individual outlying training points. Its disadvantages are high computational and storage costs (all training data are kept and searched for every prediction), sensitivity of the prediction error to imbalanced group sizes, no description of the structure of the data, and poor performance in high dimensions, where all points are far from each other.

How do the classifiers compare? In a simulation with $p = 2$ predictors, $g = 2$ groups and six scenarios (normal populations with equal covariance matrices, with and without correlation; $t$-distributed data with a linear boundary; normal populations with unequal correlations; a logistic model with quadratic terms $X_1^2, X_2^2, X_1X_2$; and a more complicated nonlinear boundary), LDA and logistic regression have the smallest test error rates when the true boundary is linear, QDA when it is quadratic, and KNN with $k$ chosen by cross-validation when it is highly nonlinear. No method is best in all situations; the choice should match the shape of the boundary and the amount of data.

## 12.6. Network Analysis

Traditional multivariate data record properties of individual entities (features, covariates). Network data are relational: they record relations between entities. Examples are social media (nodes are users, edges are friendships or followers), biology (genes and proteins, with regulation as edges), neuroscience (brain locations and their connections) and transportation (airports and direct flights). Relations can be observed directly, which is the subject of network analysis, or inferred from node features; here we only introduce the problem of discovering structure in observed relations.

A network on $n$ entities (nodes) with observed relations (edges) is represented by its $n \times n$ **adjacency matrix** $A$, with $A_{ij} = 1$ if there is an edge from $i$ to $j$ and $0$ otherwise. An undirected network ($i$ and $j$ are friends) has $A = A^{\mathsf T}$; a directed one ($i$ sent $j$ an email) need not. More generally an edge can have a weight or a sign; Bayesian networks and probabilistic graphical models use graphs in yet another way, to encode conditional independence.

A binary $A_{ij}$ can be modeled as Bernoulli with $\mathbb{P}(A_{ij} = 1) = P_{ij}$, and the $n \times n$ matrix $P = \mathbb{E}A = [P_{ij}]$ contains all the information. Edges are usually assumed independent given $P$, which is not always realistic but vastly simplifies the analysis. The problem is to estimate $P$ from one observed $A$. Without further assumptions this is hopeless, since each $P_{ij}$ has a sample of size one, so structure must be assumed:

- communities: $P$ has a block structure;
- low rank: $P$ is a low-rank matrix (more general than communities);
- smooth graphons: under some permutation of the nodes, $P$ varies smoothly over its $n \times n$ grid;
- latent variable models: the probability of an edge is a function of latent and/or observed node features.

**Definition 12.6.1 (Stochastic Block Model)** In the **stochastic block model** (SBM; Holland, Laskey and Leinhardt, 1983) for an undirected network with $K$ communities, each node $i$ is independently assigned a community label $c_i \in \{1, \dots, K\}$ with probabilities $\boldsymbol{\pi} = (\pi_1, \dots, \pi_K)$, and given the labels the edges are independent Bernoulli variables with

$$
\mathbb{P}(A_{ij} = 1) = B_{c_ic_j},
$$
where $B$ is a $K \times K$ symmetric matrix of connection probabilities.

This is a model-based clustering of the nodes, the same structure as the Gaussian mixtures of [3.4.11](/3.4.11), with Bernoulli edges in place of normal observations. In matrix form, let $\boldsymbol{z}_i$ be the vector of length $K$ with $Z_{ik} = \boldsymbol{1}_{\{c_i = k\}}$, and arrange them as the rows of the $n \times K$ matrix $Z$. Then

$$
\mathbb{E}A = P = ZBZ^{\mathsf T}
$$
(off the diagonal), a block-constant matrix of rank at most $K$. With two communities, for example, $P$ has two diagonal blocks of within-community probabilities and two off-diagonal blocks of between-community probabilities.

*Community detection* is the problem of recovering $Z$ from $A$ and estimating $B$. If we knew the labels, sorting the nodes by community would display the blocks in $A$; but the labels are unknown, and the observed $A$ shows no visible pattern. Many methods have been developed to fit the SBM, for example variational inference, pseudo-likelihood, spectral methods (clustering the leading eigenvectors of $A$) and belief propagation; they belong to statistical and machine learning. An application is the citation network of statisticians (Ji and Jin, 2016), whose communities correspond to research areas.

How should the number of communities $K$ be chosen? There are many models (the SBM has many extensions) and many fitting methods with tuning parameters. Cross-validation is again the natural answer, but splitting a network into training and test parts is not obvious, since the edges of a node depend on all the others. Network cross-validation (Chen and Lei, 2018) randomly selects $n_1$ nodes and splits the adjacency matrix into blocks $A_{11}, A_{12}, A_{22}$; it fits the model on $(A_{11}, A_{12})$, where the blocks can still be recovered with a slight modification of standard methods, and tests on $A_{22}$. It is designed for block models.

## 12.7. Factor Models for Matrix Time Series

A time series is a sequence of random variables $X_1, X_2, \dots, X_t, \dots$ indexed by discrete time $t$. Traditional time series analysis deals with univariate, multivariate and panel observations, using linear models (ARMA), nonlinear models (threshold, regime-switching, GARCH) and nonparametric models (functional-coefficient, additive, single-index). In the era of big data, many new types of data are observed over time with temporal dependence: transport and social networks, text, images. These are modern time series.

A matrix time series is a sequence of observations $Y_t$ in matrix form observed over time, for example a set of economic indicators for a group of countries, a set of financial characteristics for a group of companies, or the imports and exports among a group of countries, each recorded every quarter. Vectorizing $Y_t$ and applying the factor model of [3.4.8](/3.4.8) would ignore the row and column structure.

**Definition 12.7.1 (Matrix Factor Model)** The **matrix factor model** for an $m \times n$ matrix time series is

$$
Y_t = \Lambda F_t\Gamma^{\mathsf T} + U_t,
$$
where $F_t$ is an $r_1 \times r_2$ latent factor matrix, $\Lambda$ ($m \times r_1$) and $\Gamma$ ($n \times r_2$) are the row and column loading matrices, and $U_t$ is noise. Elementwise,

$$
y_{t,ij} = \sum_{l=1}^{r_1}\sum_{k=1}^{r_2}\lambda_{il}f_{t,lk}\gamma_{jk} + u_{t,ij}.
$$

The model incorporates the structural relations among the rows (through $\Lambda$) and among the columns (through $\Gamma$) with far fewer parameters than a factor model for the vectorized data. Wang, Liu and Chen (2019) studied its identifiability, estimation by eigen-analysis of the squared row and column cross-autocovariance matrices, asymptotic properties as $m, n, T \to \infty$, and empirical applications; Chen, Tsay and Chen (2020) studied constrained matrix factor models. Applied to import–export data, the row and column factors identify trading hubs, and comparing the periods 1983–1987 and 2001–2005 shows how the hubs changed.

## 12.8. Where to Go Next

The extensions of this chapter are of four kinds: the same problem with a better solution (FDR instead of FWER, regularized LDA), a similar problem with a new method (sparse and kernel PCA), a new type of data (correspondence analysis, logistic PCA, matrix factor models, networks), and the same problem from a different perspective (KNN and logistic regression, the machine learning view of classification). They also point to the directions in which multivariate analysis continues.

| Direction | Where it is developed | Examples from this course |
|---|---|---|
| parametric → nonparametric | [Nonparametric Statistics](/3.6) | FDR, KNN |
| linear → nonlinear | statistical learning | kernel PCA, sparse PCA, SVM |
| independent observations → time series | time series analysis | matrix factor models |
| continuous → discrete data | logistic regression, categorical data analysis | correspondence analysis, logistic PCA, logistic regression |
| correlation → causality | [Causal Inference](/3.9) | network analysis |
| priors and posterior inference | [Bayesian Statistics](/3.7) | Bayes classifier, Bayesian Gaussian mixtures |
| algorithms | [Statistical Computing](/3.5) | EM algorithm, SVD, iterative clustering |
