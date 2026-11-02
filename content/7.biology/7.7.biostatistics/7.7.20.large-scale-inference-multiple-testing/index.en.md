---
title: "Large-Scale Inference: Multiple Testing, False Discovery Rates and Count Models"
description: Thousands of simultaneous tests; the p-value histogram; the family-wise error rate and the Bonferroni, Šidák and Holm methods, the GWAS threshold of 5×10⁻⁸; the false discovery rate, the Benjamini–Hochberg procedure with its proof, and the Benjamini–Yekutieli procedure for dependent tests; Storey's π₀ and q-values; the two-groups model, local false discovery rate and empirical Bayes; variance shrinkage in small samples and the moderated t statistic; Poisson and negative binomial models for counts, the dispersion parameter and its shrinkage; size factors and TMM normalization; negative binomial generalized linear models, paired designs, Wald and likelihood ratio tests, independent filtering and shrinkage of fold changes; the zero-inflation debate; the problem of gene correlation in enrichment analysis. Illustrated by the airway RNA-seq data.
source_hash: 0aea6d812e17
---

[7.7.19](/7.7.19) looked at the structure among the 8 airway samples: treatment is the largest source of variation, with donor almost as large. The next question is gene by gene: which genes does dexamethasone change? One test per gene means about 20,000 simultaneous tests. This raises two problems that did not appear in the earlier chapters. The first is multiplicity: even if no gene had truly changed, 20,000 tests at level 0.05 would yield about 1000 "significant" results ([7.7.6](/7.7.6) Section 6.8.4 already raised this problem). The second is that each gene carries too little information: with only 4 samples per group, the variance estimate for a single gene is highly unstable; yet measuring 20,000 genes at once offers an opportunity to "borrow strength" across genes. The first half of this chapter presents the general theory of multiple testing (family-wise error rate, false discovery rate, q-values and local false discovery rate), which is equally used for GWAS ([7.4.25](/7.4.25)), proteomics and metabolomics ([7.9.9](/7.9.9)), CRISPR screens and brain imaging; the second half covers statistical models for RNA-seq counts: the negative binomial distribution, shrinkage of the dispersion parameter, normalization and the negative binomial generalized linear model. The experiment and complete workflow of differential expression are in [7.9.2](/7.9.2); this chapter is its statistical principle, with numbers consistent with that chapter (pydeseq2, design `~ cell + dex`).

## 20.1. Thousands of Tests

### 20.1.1. The Four Outcomes of Testing

Suppose $m$ null hypotheses $H_1, \dots, H_m$ are tested simultaneously, of which $m_0$ are true (these genes have not changed) and $m_1 = m - m_0$ are false. A decision rule rejects $R$ of them:

| | Not rejected | Rejected | Total |
|---|---|---|---|
| Null hypothesis true | $U$ | $V$ (false discoveries) | $m_0$ |
| Null hypothesis false | $T$ | $S$ (true discoveries) | $m_1$ |
| Total | $m - R$ | $R$ | $m$ |

$m$ and $R$ are observed, while $V$, $S$ and the others are unobservable. A single test controls $\mathbb{P}(\text{reject} \mid H_0)$; multiple testing must control some quantity involving $V$: the probability of at least one false discovery (Section 20.2) or the proportion of false discoveries among all discoveries (Section 20.3).

### 20.1.2. The p-Value Histogram

**Property 20.1.1** If the test statistic $T$ has a continuous distribution function under $H_0$, the $p$-value under $H_0$ follows $\mathrm{U}(0, 1)$.

**Proof** Let large values reject and $F$ be the distribution function of $T$ under $H_0$, so $p = 1 - F(T)$. Then $\mathbb{P}(p \le u) = \mathbb{P}(F(T) \ge 1 - u) = 1 - (1 - u) = u$, since $F(T) \sim \mathrm{U}(0, 1)$ (the probability integral transform). $\square$

The histogram of $m$ $p$-values is therefore the sum of two parts: the $p$-values of the $m_0$ true null hypotheses form a flat "floor", and those of the $m_1$ non-null hypotheses pile up near 0 (figure below). This plot is the first diagnostic for any large-scale testing:

- The height of the floor estimates $m_0$ (Section 20.3.3);
- A histogram that rises near $p = 1$, or bulges in the middle, indicates a wrongly specified null distribution (variance overestimated, conservative tests for discrete data, pairing ignored);
- A histogram tilted entirely toward 0 with no clear floor may mean that the null distribution is too narrow (batch or correlation ignored), or that a great many genes really have changed.

**Example 20.1.1 (p-Values in airway)** Among the 18,899 genes that passed independent filtering (Section 20.7.4), 5567 have $p < 0.05$. If none had changed, about 945 would be expected; from the floor of the histogram about 65% of the genes are estimated to be unchanged, among which about 618 are expected to have $p < 0.05$: even with such a strong treatment effect, about one ninth of the "list of genes with $p < 0.05$" are false discoveries. The histogram is flat near $p = 1$ without an upturn: there is no obvious error in the model (negative binomial, dispersion shrinkage, paired design).

![p-value histograms of several sets of tests (40 bins). A: 10,000 tests with all null hypotheses true (simulation, $z \sim \mathcal{N}(0, 1)$, seed 0): the $p$-values are uniformly distributed. B: 10,000 tests of which 10% have an effect (non-null tests with $z \sim \mathcal{N}(3, 1)$): a flat floor plus a peak near 0. C: Wald tests for dexamethasone of the 18,899 genes that passed independent filtering in airway (Himes et al. 2014, GEO GSE52778, Bioconductor airway; pydeseq2, design ~ cell + dex). The dashed line is the null floor estimated by Storey's method ($\lambda = 0.5$), with $\hat\pi_0$ marked](./plots/pvalue-hist.py)

## 20.2. The Family-Wise Error Rate

### 20.2.1. Bonferroni and Šidák

The **family-wise error rate** is $\mathbb{P}(V \ge 1)$, abbreviated FWER ([3.4.12](/3.4.12) [Definition 12.2.1](/3.4.12#def-12.2.1)). The simplest way of controlling it is the **Bonferroni correction** ([3.2.4](/3.2.4)): use level $\alpha/m$ for each test. From $\mathbb{P}(\bigcup_i A_i) \le \sum_i \mathbb{P}(A_i)$,

$$
\operatorname{FWER} \le m_0\cdot\frac{\alpha}{m} \le \alpha,
$$
with no assumption about the dependence between tests. If the tests are independent, $\operatorname{FWER} = 1 - (1 - \alpha')^{m_0}$, and taking $\alpha' = 1 - (1 - \alpha)^{1/m}$ makes it exactly $\alpha$: this is the **Šidák correction**; it is almost the same as $\alpha/m$ (for $m = 20$ and $\alpha = 0.05$, 0.002 56 versus 0.002 50).

### 20.2.2. Holm's Stepwise Method

**Holm's method** ([7.7.12](/7.7.12) Definition 12.3.1) orders the $p$-values from small to large and compares them in turn with $\alpha/m, \alpha/(m - 1), \dots, \alpha/1$, stopping at the first one that fails. It also controls the FWER under arbitrary dependence and uniformly rejects more than Bonferroni (at least as many), so there is no reason to use Bonferroni rather than Holm. If the tests are independent or positively dependent, Hochberg's step-up method, which tests from large to small (reject all hypotheses up to the largest $i$ with $p_{(i)} \le \alpha/(m - i + 1)$), is slightly stronger than Holm.

**Example 20.2.1** In airway, the Bonferroni threshold for the 18,899 genes is $0.05/18\,899 = 2.6\times10^{-6}$, rejecting 1413; Holm rejects 1426 and Šidák 1414. When $m$ is large and the number rejected is relatively small, the improvement of Holm is small: it relaxes the threshold appreciably only after a sizable proportion of the hypotheses has already been rejected. (Applying the Bonferroni correction to all 22,369 tests without filtering rejects 1398, [7.9.2](/7.9.2) Section 2.7.3.)

### 20.2.3. When to Control the FWER

The FWER is suited to settings where "one false positive is very costly": several primary endpoints of a clinical trial ([7.7.18](/7.7.18) Section 18.6), confirmatory subgroup conclusions, and announcing a new susceptibility locus in GWAS. The GWAS threshold of $5\times10^{-8}$ is a Bonferroni threshold: the independent tests of common variants in a European genome number about $10^6$, and $0.05/10^6 = 5\times10^{-8}$ ([7.4.25](/7.4.25) Section 25.3.2). In exploratory screening, finding candidate genes worth further validation, the FWER is too strict: the Bonferroni above retains only 1413 genes, whereas the number of genes changed by dexamethasone in airway is estimated at more than 6000 ($(1 - 0.65)\times18\,899$).

## 20.3. The False Discovery Rate

### 20.3.1. Definition and the Benjamini–Hochberg Procedure

Benjamini and Hochberg (1995) changed the object of control from "at least one false discovery" to "the proportion of false discoveries". The **false discovery rate** (FDR, [3.4.12](/3.4.12) [Definition 12.2.2](/3.4.12#def-12.2.2)) is

$$
\operatorname{FDR} = \mathbb{E}\Bigl[\frac{V}{\max(R, 1)}\Bigr],
$$
the expectation of the false discovery proportion $V/R$ (taken as 0 when nothing is rejected). The **Benjamini–Hochberg procedure** ([3.4.12](/3.4.12) [Algorithm 12.2.1](/3.4.12#alg-12.2.1)) sorts the $p$-values as $p_{(1)} \le \dots \le p_{(m)}$, finds the largest $i = k$ satisfying $p_{(i)} \le \alpha i/m$, and rejects $p_{(1)}, \dots, p_{(k)}$. It is a step-up procedure: it does not matter if some $p_{(i)}$ in the middle exceeds the line $\alpha i/m$; only the position of the last crossing below the line counts.

**Definition 20.3.1 (BH-Adjusted p-Value)** The **BH-adjusted p-value** of the $i$th smallest $p$-value is

$$
\tilde p_{(i)} = \min_{j \ge i}\Bigl\{\min\Bigl(\frac{m\,p_{(j)}}{j},\ 1\Bigr)\Bigr\}.
$$

Rejecting all hypotheses with $\tilde p \le \alpha$ is exactly equivalent to the BH procedure at level $\alpha$. The `padj` in the result tables of DESeq2 and pydeseq2, R's `p.adjust(method = "BH")` and statsmodels' `multipletests(method = "fdr_bh")` all give it.

**Theorem 20.3.1 (Benjamini–Hochberg)** If the $p$-values of the true null hypotheses are independent and distributed as $\mathrm{U}(0, 1)$, and independent of the $p$-values of the non-null hypotheses, then the BH procedure satisfies

$$
\operatorname{FDR} = \frac{m_0}{m}\alpha \le \alpha.
$$

**Proof** Let $i$ be a true null hypothesis. Let $R$ be the number of rejections, and $R^{(i)}$ the number of rejections of the BH procedure after replacing $p_i$ by 0; it depends only on the other $p$-values and is therefore independent of $p_i$. If $H_i$ is rejected, then $p_i \le \alpha R/m$, and replacing $p_i$ by 0 at this point does not change the rejection set, so $R = R^{(i)}$; conversely, if $p_i \le \alpha R^{(i)}/m$, then $H_i$ is rejected and $R = R^{(i)}$. Therefore

$$
\mathbb{E}\Bigl[\frac{\boldsymbol{1}\{H_i\ \text{rejected}\}}{\max(R, 1)}\Bigr]
= \sum_{k=1}^{m}\frac1k\,\mathbb{P}\Bigl(p_i \le \frac{\alpha k}{m},\ R^{(i)} = k\Bigr)
= \sum_{k=1}^{m}\frac1k\cdot\frac{\alpha k}{m}\,\mathbb{P}(R^{(i)} = k) = \frac{\alpha}{m}.
$$
Since $V/\max(R, 1) = \sum_{i\ \text{true}}\boldsymbol{1}\{H_i\ \text{rejected}\}/\max(R, 1)$, summing over the $m_0$ true null hypotheses gives $m_0\alpha/m$. $\square$

The FDR is an expectation: the false discovery proportion in a single analysis can exceed $\alpha$. In the simulation of panel B below, the average false discovery proportion of BH ($\alpha = 0.1$) is 0.092 ($= 0.9 \times 0.1$), while the proportion in a single run lies between 0 and about 0.2; in 99.6% of the replications there is at least one false discovery: it does not control the FWER. In exchange, its power (the proportion of non-null hypotheses detected) is 0.62, whereas Bonferroni has only 0.15. With no correction the power is 0.85, but 35% of the discoveries are false.

**Example 20.3.1 (The BH Procedure in airway)** Among the 18,899 genes, the last intersection of the BH line $0.1\,i/m$ with the sorted $p$-values is at $i = 4691$, corresponding to a $p$-value threshold of 0.0247 (panel A below): there are 4691 differentially expressed genes at FDR 0.1 and 3888 at 0.05, the same as in [7.9.2](/7.9.2) Section 2.7.2. If the proportion of true null hypotheses among these 4691 genes is $\hat\pi_0$, the expected number of false discoveries is about $\hat\pi_0 m \times 0.0247 = 0.654 \times 18\,899 \times 0.0247 = 306$, that is 6.5%, below the nominal 10%: the BH procedure is designed for $\pi_0 = 1$ and is conservative when many genes have truly changed (Section 20.3.3).

![The Bonferroni and Benjamini–Hochberg methods. A: the 18,899 Wald $p$-values of airway (pydeseq2, ~ cell + dex; Himes et al. 2014, Bioconductor airway), sorted and plotted against rank (log–log axes, starting at rank 300): the BH line $\alpha i/m$ ($\alpha = 0.1$) last meets the sorted $p$-values at rank 4691; the Bonferroni threshold $\alpha/m$ ($\alpha = 0.05$) is at rank 1413. B: simulation (seed 0): 500 replications, each with 1000 tests of which 100 are non-null ($z \sim \mathcal{N}(3, 1)$); the proportion of false discoveries among rejections (boxplots, diamonds are means, that is, the FDR) and the power (dots) under four rules](./plots/bh-procedure.py)

### 20.3.2. Dependent Tests

Gene expression is correlated (genes of the same pathway rise and fall together), and adjacent SNPs in GWAS are correlated through linkage disequilibrium. The BH procedure still controls the FDR when the test statistics are positively regression dependent (PRDS, a condition of positive dependence satisfied by one-sided tests of multivariate normal test statistics) (Benjamini and Yekutieli 2001); in practice, extensive simulations on expression data show that BH is also close to the nominal level under general dependence. For arbitrary dependence, the Benjamini–Yekutieli procedure replaces $\alpha$ by $\alpha/\sum_{j=1}^{m}j^{-1}$ (about $\alpha/10.4$ for $m = 18\,899$), at the price of a large loss of power: in airway only 2782 genes at FDR 0.1. Correlation does not change the expectation of the FDR but makes the false discovery proportion fluctuate more: with strong correlation, the false discoveries in one analysis tend to appear, or fail to appear, together as a "whole cluster".

### 20.3.3. π₀ and q-Values

Theorem 20.3.1 shows that BH in fact controls at $\pi_0\alpha$ ($\pi_0 = m_0/m$). If $\pi_0$ can be estimated, the proportion of false discoveries can be estimated more accurately.

**Formula 20.3.1 (Storey's Estimate of $\pi_0$)** Take $\lambda \in (0, 1)$, and use the fact that $p$-values larger than $\lambda$ come mainly from true null hypotheses,

$$
\hat\pi_0(\lambda) = \frac{\#\{i: p_i > \lambda\}}{m(1 - \lambda)}.
$$

A few $p$-values of non-null hypotheses are also larger than $\lambda$, so $\hat\pi_0$ is conservative (too large). As $\lambda$ increases the bias decreases and the variance increases; the qvalue software computes it over a set of $\lambda$ and extrapolates to $\lambda \to 1$ with a smoothing spline. In airway, $\lambda = 0.3, 0.5, 0.7, 0.9$ give 0.671, 0.654, 0.658 and 0.644, quite stable.

**Definition 20.3.2 (q-Value)** For a threshold $t$, estimate the FDR of rejecting all $p \le t$ by $\widehat{\operatorname{FDR}}(t) = \hat\pi_0 m t/\#\{i: p_i \le t\}$. The **q-value** of the test with $p$-value $p_i$ is defined as

$$
q_i = \min_{t \ge p_i}\widehat{\operatorname{FDR}}(t),
$$
the smallest estimated FDR attainable over all thresholds at which this test would just be rejected (Storey 2002; Storey and Tibshirani 2003).

The q-value is to the FDR what the $p$-value is to the type I error rate: the $p$-value is "what proportion of true nulls would be as extreme as this test", and the q-value is "if this test and all more significant ones are called discoveries, what is the estimated proportion of false discoveries among them". When $\hat\pi_0 = 1$ the q-value is the BH-adjusted $p$-value; in general $q_i \approx \hat\pi_0\tilde p_i$. In airway there are 5389 genes with $q < 0.1$ (BH: 4691) and 4368 with $q < 0.05$ (BH: 3888). q-values depend on the estimate of $\hat\pi_0$, and are unreliable when $m$ is small (a few dozen tests) or when the null distribution of the $p$-values is inexact; BH is safer then.

### 20.3.4. The Two-Groups Model and Local False Discovery Rate

The FDR is a property of a region: the proportion of false discoveries among all tests with $p \le t$. A test on the boundary of the region ($p$ exactly equal to $t$) is more likely to be false than a test in the interior. Efron gave a measure for individual tests starting from a simple model.

**Definition 20.3.3 (Two-Groups Model and Local False Discovery Rate)** Suppose the statistic $z_i$ of each test comes with probability $\pi_0$ from the null density $f_0$ and with probability $\pi_1 = 1 - \pi_0$ from the non-null density $f_1$, that is, the marginal density of $z_i$ is

$$
f(z) = \pi_0 f_0(z) + \pi_1 f_1(z),
$$
called the **two-groups model**. By Bayes' formula, the posterior probability that the test is a true null given $z$,

$$
\operatorname{fdr}(z) = \mathbb{P}(\text{null} \mid z) = \frac{\pi_0 f_0(z)}{f(z)}
$$
is called the **local false discovery rate**.

The analogous tail-area quantity $\operatorname{Fdr}(z_0) = \pi_0 F_0(\lvert Z\rvert \ge \lvert z_0\rvert)/F(\lvert Z\rvert \ge \lvert z_0\rvert)$ is the FDR estimated by the BH procedure; it is the average of $\operatorname{fdr}$ over the tail area and is always smaller than the $\operatorname{fdr}$ at the boundary.

**Definition 20.3.4 (Empirical Bayes)** In a model of the form "the parameter $\theta_i$ of each unit $i$ comes from a common prior distribution $g$, and the distribution of the data $x_i$ given $\theta_i$ is known", first estimating the prior $g$ (or its parameters) from the data of all units and then carrying out Bayesian inference for each unit with the estimated prior is called **empirical Bayes**.

The local fdr is an example of empirical Bayes: $f_0$ is the theoretical null distribution ($\mathcal{N}(0, 1)$), $\pi_0$ is estimated from the floor of the $p$-values, and $f$ is estimated from the histogram of all $z$ (Lindsey's method: Poisson regression of the histogram counts on a polynomial in $z$, [7.7.14](/7.7.14)). Thousands of tests are exactly the "big data" needed to estimate a prior; this is the core idea of large-scale inference: turning multiplicity from a burden into information. The variance shrinkage in the next section, the dispersion shrinkage of Section 20.5.4 and the **best linear unbiased prediction** of mixed models in [7.7.17](/7.7.17) are all the same idea.

**Example 20.3.2** In the histogram of Wald statistics for airway (figure below), $\pi_0 f_0$ accounts only for the central part, and the long tails on both sides are non-null genes. There are 4073 genes with $\operatorname{fdr}(z) < 0.2$ (the threshold Efron recommends as "worth reporting"), corresponding to $\lvert z\rvert \gtrsim 2.5$; at the same position the tail-area Fdr is about 0.04. Near the center the estimated $f$ is slightly lower than $\pi_0 f_0$, and the local fdr is truncated to 1: the theoretical null distribution and $\hat\pi_0$ are only approximations, and Efron's "empirical null" method instead estimates the mean and variance of $f_0$ from the shape of the central part.

![Two-groups model and local false discovery rate for the airway Wald statistics (18,899 genes; Himes et al. 2014, Bioconductor airway; pydeseq2, ~ cell + dex). A: histogram of $z$ (the part with $\lvert z\rvert < 6$ is shown and fitted, with another 870 genes outside); the dashed line is $\pi_0 f_0$ with $f_0 = \mathcal{N}(0, 1)$ and $\pi_0 = 0.65$ estimated by Storey's method; the solid line is the mixture density $f$ estimated by Lindsey's method (Poisson regression of the bin counts on a degree-7 polynomial in $z$). B: local fdr$(z) = \pi_0 f_0(z)/f(z)$ and tail-area Fdr$(z)$; 4073 genes have local fdr below 0.2](./plots/local-fdr.py)

### 20.3.5. Choosing a Kind of Control

| Purpose | Control | Method |
|---|---|---|
| Confirming a few hypotheses (clinical endpoints, announcing a GWAS locus) | FWER | Holm; Bonferroni; ordered testing |
| Screening candidates (differential expression, proteomics, CRISPR screens) | FDR | BH; q-values |
| Judging one at a time ("is this gene real?") | Local fdr | Two-groups model |
| Arbitrary dependence, strict FDR required | FDR | Benjamini–Yekutieli |

Whichever is used, the "family" of tests (all genes, the genes within a pathway, or the whole omics platform) must be determined in advance, and the total number of tests reported. If the analysis is adjusted repeatedly on the same data until something is significant, no correction is valid ([7.7.18](/7.7.18) Section 18.9).

## 20.4. Shrinkage of Variances

### 20.4.1. Instability of the Small-Sample t Test

With 3 samples per group, the pooled variance of each gene has only 4 degrees of freedom. $s^2/\sigma^2 \sim \chi^2_4/4$, and the probability that it is less than half the true variance is about 0.26. Among 20,000 genes there will always be thousands whose variance is badly underestimated, and even a tiny difference gives them a large $t$ value; the heavy tails of the $t_4$ distribution, in turn, mean that genes that truly differ need a very large $t$ to be significant. Conversely, ranking by fold change alone ignores genes whose variances truly differ.

### 20.4.2. The Moderated t Statistic

The limma method of Smyth (2004) applies empirical Bayes shrinkage to the variances.

**Definition 20.4.1 (Moderated t Statistic)** Suppose the sample variance $s_g^2$ of gene $g$ has $d$ degrees of freedom, and assume a prior for the true variance with $d_0s_0^2/\sigma_g^2 \sim \chi^2_{d_0}$. After estimating $d_0$ and $s_0^2$ from the $s_g^2$ of all genes, replace $s_g^2$ by the posterior mean

$$
\tilde s_g^2 = \frac{d_0s_0^2 + d\,s_g^2}{d_0 + d}
$$
in computing the $t$ statistic, giving $\tilde t_g = \hat\beta_g/(\tilde s_g\sqrt{c_g})$ ($c_g$ is the variance factor of the coefficient), called the **moderated t statistic**. Under the null hypothesis $\tilde t_g \sim t_{d_0 + d}$.

$\tilde s_g^2$ is a weighted average of the individual variance and the common variance, with the respective degrees of freedom as weights: the prior is worth an extra $d_0$ degrees of freedom of information. $d_0$ and $s_0^2$ are obtained by the method of moments: the mean and variance of $\log s_g^2$ correspond to functions of $\log s_0^2$ and $d_0$ (involving the digamma and trigamma functions). A large $d_0$ means that the variances of the genes are similar and the shrinkage is strong; as $d_0 \to \infty$ it reduces to using one common variance for all genes, and for $d_0 = 0$ it is the ordinary $t$ test.

**Example 20.4.1 (Simulation)** 10,000 genes, 3 samples per group, true variances from a prior with $d_0 = 4$ and $s_0^2 = 0.0625$, and 10% of the genes with a difference of 1.0 (figure below). The data give $\hat d_0 = 4.0$ and $\hat s_0^2 = 0.061$, almost exactly the true values; the variance estimates are pulled toward 0.061, with the small variances enlarged the most. Among the top 1000 genes ranked by $\lvert t\rvert$, 734 truly changed, by fold change 830, and by moderated $t$ 855: the moderated $t$ combines the advantages of both.

![The moderated t statistic (simulation, seed 0): 10,000 genes, 3 samples per group (log scale), true variances from a scaled inverse $\chi^2$ prior with $d_0 = 4$ and $s_0 = 0.25$, and a difference of 1.0 in 10% of the genes. A: sample variance $s^2$ (4 residual degrees of freedom) and the shrunken $\tilde s^2 = (d_0s_0^2 + d\,s^2)/(d_0 + d)$, with $d_0$ and $s_0^2$ estimated from all genes by the moments of $\log s^2$ (the method of limma); the dashed line is $\hat s_0^2$. B: number of truly changed genes among the top genes ranked by ordinary $t$, moderated $t$ or fold change; the dotted line marks 1000 (the number of truly changed genes)](./plots/moderated-t.py)

limma was originally designed for log intensities from microarrays; for RNA-seq, voom first computes precision weights for each observation from the mean–variance trend of $\log$ CPM, and then uses a weighted linear model with the moderated $t$ ([7.9.2](/7.9.2) Section 2.7.1). The negative binomial model below applies the same shrinkage to the dispersion parameter.

## 20.5. Models for Count Data

### 20.5.1. Two Layers of Variation

The number of reads for gene $g$ in an RNA-seq sample comes from two layers of randomness. The first is sampling in sequencing: the library contains a large number of cDNA fragments, sequencing randomly draws tens of millions of them, and given the true proportion $q_{gj}$ of this gene in the sample, the read count is approximately $\mathrm{Poi}(s_jq_{gj})$ ($s_j$ reflects the sequencing depth). The second is biological variation: the true expression $q_{gj}$ itself differs between individuals (donors, mice, culture dishes) under the same condition. With only the first layer the variance equals the mean; with the second, the variance exceeds the mean, which is **overdispersion** ([7.7.9](/7.7.9), [7.7.14](/7.7.14) Section 14.8.3).

### 20.5.2. The Negative Binomial Distribution

If $K \mid \lambda \sim \mathrm{Poi}(\lambda)$ and $\lambda$ has a Gamma distribution with mean $\mu$ and variance $\alpha\mu^2$, the marginal distribution of $K$ is the **negative binomial distribution** ([3.1.4](/3.1.4); [7.7.4](/7.7.4) Section 4.6.3), and by the law of total variance

$$
\operatorname{Var}(K) = \mathbb{E}[\operatorname{Var}(K \mid \lambda)] + \operatorname{Var}(\mathbb{E}[K \mid \lambda]) = \mu + \alpha\mu^2.
$$

**Definition 20.5.1 (Dispersion Parameter)** When the negative binomial distribution is written $\operatorname{Var}(K) = \mu + \alpha\mu^2$, $\alpha \ge 0$ is called the **dispersion parameter**. $\sqrt\alpha$ is the coefficient of variation of the true expression $\lambda$, that is, the biological coefficient of variation; $\alpha = 0$ gives the Poisson distribution. In the notation $\mu + \mu^2/k$ of [7.7.4](/7.7.4), $k = 1/\alpha$; edgeR writes $\alpha$ as $\phi$ ([7.9.2](/7.9.2)).

The coefficient of variation is $\sqrt{\operatorname{Var}(K)}/\mu = \sqrt{1/\mu + \alpha}$: for small counts the Poisson noise ($1/\mu$) dominates, and for large counts the biological variation ($\alpha$) dominates, which deeper sequencing cannot reduce. This is the statistical reason why "more biological replicates are more effective than more depth" ([7.9.2](/7.9.2) Section 2.2.2).

**Example 20.5.1 (The Mean–Variance Relation in airway)** Compute the mean and variance of the normalized counts of each gene in the 4 untreated samples (panel A below). For genes with mean count 1–10, the median ratio of variance to mean is 1.09, close to Poisson; for 10–100 it is 2.2; for 100–1000, 4.3; for 1000–10,000, 16.8; above 10,000, 336. The variance grows with the mean at a rate close to quadratic. The dispersion trend fitted by pydeseq2 is

$$
\alpha(\mu) = 0.0101 + \frac{2.583}{\mu},
$$
and the dispersion of highly expressed genes tends to 0.0101, a biological coefficient of variation of about 10%, which is quite low variation for cultured primary cell lines; population samples (tissue from different patients) usually vary far more.

### 20.5.3. The Negative Binomial Generalized Linear Model

**Definition 20.5.2 (Negative Binomial Generalized Linear Model)** Suppose the count $K_{gj}$ of gene $g$ in sample $j$ follows $\mathrm{NB}$ with mean $\mu_{gj}$ and dispersion parameter $\alpha_g$,

$$
\mu_{gj} = s_jq_{gj}, \qquad \log q_{gj} = \boldsymbol{x}_j^{\mathsf T}\boldsymbol{\beta}_g,
$$
where $s_j$ is the size factor of sample $j$ (Section 20.6) and $\boldsymbol{x}_j$ is the $j$th row of the **design matrix** ([3.2.3](/3.2.3)). This model is called the **negative binomial generalized linear model**.

It is a **generalized linear model** ([3.3.6](/3.3.6)) with log link, and $\log s_j$ enters the linear predictor as an **offset** ([7.7.14](/7.7.14) Section 14.8): the same structure as using person-time as the offset in Poisson regression, except that the variance function is changed from $\mu$ to $\mu + \alpha\mu^2$. Given $\alpha_g$, $\boldsymbol{\beta}_g$ is estimated by maximum likelihood with iteratively reweighted least squares ([7.7.14](/7.7.14) Section 14.3), with weights $\mu/(1 + \alpha\mu)$. The coefficients are in natural-log units, and software reports the $\log_2$ fold change $\beta/\ln 2$.

### 20.5.4. Estimation and Shrinkage of the Dispersion

The dispersion of each gene must be estimated from replicates under the same condition, and airway has only $8 - 5 = 3$ residual degrees of freedom (8 samples, 5 coefficients). The estimate for a single gene is highly unstable:

- The gene-wise estimate: maximize the Cox–Reid adjusted profile likelihood given the mean model (correcting the bias caused by estimating $\boldsymbol{\beta}$, analogous to dividing by $n - p$ in variance estimation). In airway more than half of the gene-wise estimates fall on the lower bound 0: with 3 degrees of freedom it is common for the sample variance to be below the Poisson variance.
- The trend (fitted): regress the gene-wise estimates on the mean to obtain $\alpha(\mu) = a_0 + a_1/\mu$ (Example 20.5.1); fitted by a Gamma-family generalized linear model, iteratively removing outlying genes.
- Shrinkage (MAP): take a log-normal prior centered on the trend, $\log\alpha_g \sim \mathcal{N}(\log\alpha(\mu_g), \sigma_d^2)$, and take the posterior mode. The prior variance $\sigma_d^2$ is obtained from the scatter of the gene-wise estimates around the trend minus the sampling variance (about $\psi_1(\nu/2)$ with $\nu$ degrees of freedom, $\psi_1$ the trigamma function). Genes whose gene-wise estimates are far above the trend (more than 2 prior standard deviations) keep their gene-wise estimates, so as not to shrink away truly highly variable genes and create false positives.

**Example 20.5.2** In airway the median of the gene-wise estimates is at the lower bound, and the median of the shrunken dispersion is 0.033, with the trend at the same position at 0.036 (panel B below). *FKBP5* is an exception: its gene-wise estimate is 0.130, far above the trend (0.011), and 0.130 is retained: the 4 donors respond to dexamethasone with very different intensity (counts 3875–5493 after treatment, 154–601 before).

![Overdispersion of counts (airway RNA-seq; Himes et al. 2014, GEO GSE52778, Bioconductor airway; 8000 genes drawn at random from the 22,369 genes with total reads ≥ 10). A: mean and variance of the normalized counts in the 4 untreated samples (log–log axes); the gray line is the Poisson variance (= mean), and the colored curve is the negative binomial variance $\mu + \alpha(\mu)\mu^2$ with $\alpha(\mu) = 0.0101 + 2.583/\mu$, the dispersion trend fitted by pydeseq2 (design ~ cell + dex); the untreated samples also contain differences between donors. B: dispersion estimates against the mean: the gene-wise (Cox–Reid adjusted maximum likelihood) estimates, the fitted trend, and the final values after shrinkage (maximum a posteriori centered on the trend; genes far above the trend keep their gene-wise estimates). With only 3 residual degrees of freedom, more than half of the gene-wise estimates fall on the lower bound (drawn at the bottom of the plot)](./plots/mean-variance.py)

## 20.6. Normalization

### 20.6.1. Why Dividing by the Total Reads Is Not Enough

Samples differ in sequencing depth, and counts must first be put on the same scale. Dividing directly by the total reads (CPM) assumes that every sample has the same "total RNA output". If treatment raises a few genes extremely high, these genes occupy more of the reads, and the CPM of all the other genes falls and looks as if they were generally suppressed: this is composition bias ([7.9.2](/7.9.2) [Example 2.4.1](/7.9.2#ex-2.4.1)). What normalization has to find is not the total reads but the ratio shown by "the majority of genes that have not changed".

### 20.6.2. Median of Ratios and TMM

**Definition 20.6.1 (Size Factor)** For each gene $g$, take its geometric mean over all samples, $\bar K_g = (\prod_j K_{gj})^{1/n}$, as a pseudo-reference sample; the **size factor** of sample $j$ is

$$
\hat s_j = \operatorname*{median}_{g:\ \bar K_g > 0}\frac{K_{gj}}{\bar K_g},
$$
the median of the ratios of the sample to the reference (Anders and Huber 2010, the median-of-ratios method of DESeq).

The median is robust to a few extremely changed genes: as long as fewer than half of the genes change and the ups and downs roughly balance, the median reflects the ratio of the unchanged genes. Only genes with reads in all samples take part in the calculation.

**Definition 20.6.2 (TMM Normalization)** Choose a reference sample $r$ and, for the genes with reads in both sample $j$ and $r$, compute the log ratio $M_g = \log_2\frac{K_{gj}/N_j}{K_{gr}/N_r}$ and the mean log expression $A_g = \frac12\log_2\frac{K_{gj}}{N_j}\cdot\frac{K_{gr}}{N_r}$ ($N$ the total reads). Remove the genes with the highest and lowest 30% of $M_g$ and the highest and lowest 5% of $A_g$, and take the weighted mean of $M_g$ of the remaining genes with weights equal to the reciprocals of the approximate variances; 2 raised to this power is the normalization factor of sample $j$, and the effective library size is $N_j$ times the normalization factor. This method is called **TMM normalization** (trimmed mean of M-values; Robinson and Oshlack 2010, edgeR).

**Example 20.6.1** The 8 libraries of airway have total counts of 15.2–30.8 million over genes. The median-of-ratios method uses the 18,868 genes with reads in all 8 samples, and gives size factors of 1.024, 0.896, 1.180, 0.670, 1.178, 1.399, 0.921, 0.945; the TMM normalization factors are 0.95–1.06, and the effective library sizes (standardized by the geometric mean) are 1.018, 0.891, 1.168, 0.674, 1.170, 1.395, 0.917, 0.936, with a correlation of 0.9999 with the size factors. In this data set the two methods nearly agree, and the size factors mainly reflect sequencing depth; in data with large differences in composition (different tissues, treatments changing many genes), both differ clearly from the ratio of total reads.

The common assumption of the two methods is that most genes have not changed, or that the changes are symmetric. If the treatment raises global transcription (such as MYC-driven transcriptional amplification), this assumption fails, and spike-in RNA is needed as an external reference.

## 20.7. The Negative Binomial GLM for Differential Expression

### 20.7.1. Design and Pairing

The 8 airway samples come from 4 donors, each with one treated and one untreated sample. The design matrix for the design `~ cell + dex` has 5 columns: the intercept (donor N61311, untreated), 3 donor indicator variables and the treatment indicator:

$$
\log q_{gj} = \beta_{g0} + \beta_{g1}x_{j,\mathrm{N052611}} + \beta_{g2}x_{j,\mathrm{N080611}} + \beta_{g3}x_{j,\mathrm{N061011}} + \beta_{g4}x_{j,\mathrm{dex}}.
$$
$\beta_{g4}$ is the treatment effect compared within the same donor; differences between donors are absorbed by the donor terms and do not enter the error, for the same reason that the paired $t$ test is more efficient than the independent two-sample $t$ test in a **paired design** ([7.7.7](/7.7.7)); it is also the count version of the randomized block design ([7.7.12](/7.7.12)). The design `~ dex`, which ignores pairing, yields only 3422 genes at FDR 0.1, versus 4691 with pairing ([7.9.2](/7.9.2) Section 2.7.2).

### 20.7.2. Wald and Likelihood Ratio Tests

The **Wald test** ([7.7.14](/7.7.14)) compares $z = \hat\beta_{g4}/\operatorname{SE}(\hat\beta_{g4})$ with the standard normal; the **likelihood ratio test** ([3.2.5](/3.2.5)) compares the difference of the deviances of the full model and the reduced model without the treatment term, which under the null hypothesis approximately follows $\chi^2_1$. The Wald test needs only one fitted model and serves for a single coefficient or contrast; the likelihood ratio test can test several coefficients at once (a multilevel factor, a whole curve in a time series, interactions) and is also more reliable when counts are very small.

**Example 20.7.1 (A Single Gene)** The counts of *FKBP5* are: untreated 260, 381, 601, 154, treated 4652, 3875, 5493, 4118 (donors in the order N61311, N052611, N080611, N061011). Fitted with $\alpha = 0.130$, $\hat\beta_4 = 2.805$, that is a $\log_2$ fold change of 4.05 (about 16.5-fold), standard error 0.37 (on the $\log_2$ scale), $z = 10.94$; the likelihood ratio statistic is 91.5 (1 degree of freedom, $p = 1.1\times10^{-21}$). *CRISPLD2* ($\alpha = 0.023$) has a $\log_2$ fold change of 2.63, $z = 16.71$ and likelihood ratio statistic 244.6. The large dispersion makes the test for *FKBP5* less extreme: its fold change is larger but its $z$ is smaller. *TSPAN6* has a $\log_2$ fold change of $-0.38$ ($z = -3.44$, $p = 0.0006$): the change is small, but because the dispersion is only 0.010 it is still significant at FDR 0.1; statistical significance is not biological importance, and the size of the fold change must be judged separately.

**Example 20.7.2 (All Genes)** Testing the treatment term gene by gene with the likelihood ratio test for the 18,899 genes (dispersion at its final value), there are 4668 genes at FDR 0.1, versus 4691 for the Wald test; the two tests agree on 99.9% of the genes, and the 23 extra genes of the Wald test are all near the threshold.

### 20.7.3. Shrinkage of Fold Changes

The maximum likelihood fold change of a low-count gene is very unstable: a gene with 3 reads in the treated group and 0 in the control group has an "infinite" fold change. When genes are ranked by fold change, these are often at the top. Shrinkage estimation gives $\beta_{g4}$ a heavy-tailed prior centered at 0 (apeglm in DESeq2 uses a Cauchy prior), whose scale is determined by the estimates of all genes, and takes the posterior mode: genes with a lot of data hardly change, and genes with little data are pulled toward 0 (the MA plot in [7.9.2](/7.9.2) Section 2.7.3). The shrunken fold changes are used for ranking and plotting; tests are still based on the unshrunken Wald statistics (or on a test of "$\lvert\beta\rvert$ greater than a threshold"). This is again empirical Bayes: the prior comes from all the genes.

### 20.7.4. Independent Filtering

Genes with extremely low counts have almost no power to detect a difference, yet they increase $m$ and make the BH threshold $\alpha i/m$ stricter.

**Definition 20.7.1 (Independent Filtering)** Removing a portion of the tests before multiple testing, on the basis of a statistic that is independent of the test statistic under the null hypothesis (such as the mean normalized count over all samples regardless of group), and applying the FDR correction only to the remaining tests, is called **independent filtering** (Bourgon, Gentleman and Huber 2010).

The filter statistic must not use group information: filtering on "the difference between the two groups" means picking out the significant ones first and then correcting, and the type I error runs out of control. DESeq2 computes the number of BH rejections over a series of mean-count thresholds and takes the threshold with the most rejections. In airway the threshold is a mean normalized count of 3.29, which removes 3470 genes: only 34 of them have $p < 0.05$ (about 174 would be expected under a uniform distribution; the tests of these genes are very conservative because of too few counts), and 18,899 are kept. Without filtering there are 4490 genes at FDR 0.1, and 4691 after filtering.

## 20.8. The Zero-Inflation Debate

More than 90% of the count matrix of single-cell RNA-seq consists of zeros. Some are "truly not expressed" (a cell expresses only the genes it needs, that is, sparsity), and some are "expressed but not detected" (low efficiency of reverse transcription, amplification and capture). Early methods used zero-inflated models: in addition to a negative binomial (or Poisson), a "technical zero" is added with probability $\pi$.

**Definition 20.8.1 (Zero Inflation)** When the proportion of zeros in count data is significantly higher than that predicted by the fitted count distribution (Poisson or negative binomial) at the same mean, the data are said to show **zero inflation**. The zero-inflated negative binomial distribution is $\mathbb{P}(K = 0) = \pi + (1 - \pi)f_{\mathrm{NB}}(0)$, $\mathbb{P}(K = k) = (1 - \pi)f_{\mathrm{NB}}(k)$ ($k \ge 1$).

The negative binomial distribution already has many zeros: $f_{\mathrm{NB}}(0) = (1 + \alpha\mu)^{-1/\alpha}$. With mean 0.5 and $\alpha = 0.5$ it is $1.25^{-2} = 0.64$, more than for a Poisson with the same mean ($\mathrm{e}^{-0.5} = 0.61$). In single cells the average UMI count per gene per cell is often far below 1, and the many zeros are an inevitable result of the low mean. For UMI-based droplet data, the proportion of zeros for each gene agrees with that predicted by a negative binomial from its mean and dispersion, and no extra zero-inflation component is needed (Svensson 2020); zero inflation is more evident in early full-length, non-UMI methods. The current practice is therefore: for UMI data use a (Gamma–)Poisson or negative binomial model with the total UMI count of the cell as the size factor (sctransform, scran, [7.9.5](/7.9.5)); to compare conditions, first sum the counts of the cells of the same cell type in the same sample (pseudobulk, [7.9.5](/7.9.5) [Definition 5.6.1](/7.9.5#def-5.6.1)) and then use the negative binomial generalized linear model of this chapter, with the sample rather than the cell as the unit of replication; cells are pseudoreplicates ([7.7.12](/7.7.12)).

## 20.9. Statistics of Enrichment Analysis

Differential expression yields a list of genes, and a common way to interpret it is to ask whether the genes in some functional set (a pathway, a GO term) are over-represented in the list. **Over-representation analysis** ([7.9.3](/7.9.3)) is computed with the **hypergeometric distribution**: of $N$ background genes, $K$ are in the list, the set has $n$ genes of which $k$ are in the list, and $p = \mathbb{P}(X \ge k)$ with $X$ hypergeometric. It is the one-sided **Fisher's exact test** ([7.7.9](/7.7.9)) of the 2×2 table (in the list or not × in the set or not). An FDR correction is then applied over the thousands of sets tested.

This test treats genes as independent sampling units, whereas genes in the same set are often co-regulated and have correlated expression, so the test is too optimistic. Let the test statistics of the $n$ genes in a set each have variance 1 and mean pairwise correlation $\bar\rho$; the variance of their mean is

$$
\operatorname{Var}(\bar t) = \frac{1}{n}\bigl[1 + (n - 1)\bar\rho\bigr],
$$
and for $n = 100$ and $\bar\rho = 0.05$ the variance is inflated 5.95-fold compared with the independent case. There are two ways to deal with correlation: permute over genes (competitive null hypothesis: genes in the set are no more likely to change than other genes) while accounting for correlation between genes (CAMERA estimates $\bar\rho$ and corrects accordingly), or permute over samples (self-contained null hypothesis: no gene in the set is related to the treatment; the sample permutation of GSEA, [7.9.3](/7.9.3) Section 3.3.3). In addition, long genes and highly expressed genes have higher power to enter the list (detection bias), and the background must be "the genes actually tested and with a chance of entering the list", not the whole genome. Methods and interpretation of enrichment analysis are in [7.9.3](/7.9.3).

## 20.10. Computing with Python

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.multitest import multipletests
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

counts = pd.read_csv("airway_counts.csv", index_col=0)          # genes x samples
meta = pd.read_csv("airway_coldata.csv", index_col=0)[["cell", "dex"]]
meta["dex"] = pd.Categorical(meta["dex"], categories=["untrt", "trt"])
counts = counts[counts.sum(axis=1) >= 10]

# negative binomial GLM ~ cell + dex: size factors, dispersions (gene-wise, trend, MAP), Wald tests
dds = DeseqDataSet(counts=counts.T, metadata=meta, design="~cell + dex")
dds.deseq2()
print(dds.obs["size_factors"].round(3))                           # 1.024 0.896 1.180 0.670 ...
print(dds.uns["trend_coeffs"])                                    # a0 = 0.0101, a1 = 2.583
st = DeseqStats(dds, contrast=["dex", "trt", "untrt"], alpha=0.1)
st.summary()                                                      # BH with independent filtering
res = st.results_df
print((res.padj < 0.1).sum())                                     # 4691

# multiple-testing rules on the filtered p-values (Examples 20.2.1, 20.3.1)
p = res.pvalue[res.padj.notna()]
for method in ["bonferroni", "holm", "sidak", "fdr_bh", "fdr_by"]:
    print(method, multipletests(p, alpha=0.05, method=method)[0].sum())   # 1413 1426 1414 3888 2499

# Storey's pi0 and q-values (Formula 20.3.1, Definition 20.3.2)
pi0 = np.mean(p > 0.5) / 0.5                                      # 0.654
q = np.minimum(1, pi0 * multipletests(p, method="fdr_bh")[1])
print((q < 0.1).sum())                                            # 5389

# one gene by hand: NB GLM with the size factors as offset, Wald and likelihood ratio (Example 20.7.1)
y = counts.loc[gene_id].values                                    # FKBP5
X = pd.get_dummies(meta, drop_first=True).astype(float)
X.insert(0, "const", 1.0)
alpha = dds.var.loc[gene_id, "dispersions"]
off = np.log(dds.obs["size_factors"].values)
full = sm.GLM(y, X, family=sm.families.NegativeBinomial(alpha=alpha), offset=off).fit()
red = sm.GLM(y, X.drop(columns="dex_trt"), family=sm.families.NegativeBinomial(alpha=alpha), offset=off).fit()
print(full.params["dex_trt"] / np.log(2), 2 * (full.llf - red.llf))    # log2 FC 4.05, LR 91.5

# hypergeometric over-representation (20.9): N background genes, K in the list, set of n, k overlap
print(stats.hypergeom.sf(k - 1, N, n, K))
```

## Summary

- Of the four outcomes of $m$ tests only $m$ and $R$ are visible; the $p$-values of true nulls are uniform (Property 20.1.1), and the $p$-value histogram = a flat floor + a peak near 0, the first diagnostic. In airway 5567 genes have $p < 0.05$, of which about 618 are expected to be false (Example 20.1.1).
- FWER: Bonferroni $\alpha/m$ (any dependence), Šidák (independence), Holm is uniformly better; the GWAS threshold $5\times10^{-8}$ is the Bonferroni threshold for about $10^6$ independent tests. airway: Bonferroni 1413, Holm 1426 (Example 20.2.1).
- FDR $= \mathbb{E}[V/\max(R, 1)]$; the BH procedure and BH-adjusted $p$-values (Definition 20.3.1) control it at $\pi_0\alpha$ under independence (Theorem 20.3.1); this still holds under PRDS, and for arbitrary dependence use Benjamini–Yekutieli. airway: 4691 at FDR 0.1, threshold $p \le 0.0247$ (Example 20.3.1); in the simulation BH has FDR 0.092 and power 0.62, Bonferroni power 0.15.
- Storey's $\hat\pi_0$ (Formula 20.3.1, airway 0.65) and q-values (Definition 20.3.2, airway $q < 0.1$: 5389 genes); the two-groups model and local fdr (Definition 20.3.3, airway fdr < 0.2: 4073 genes); empirical Bayes (Definition 20.3.4) turns the many tests into information for estimating the prior.
- Variance shrinkage: the moderated $t$ (Definition 20.4.1) $\tilde s^2 = (d_0s_0^2 + ds^2)/(d_0 + d)$, with null distribution $t_{d_0 + d}$; in the simulation with 3 + 3 samples the top 1000 genes contain 855 true positives, versus 734 for the ordinary $t$ (Example 20.4.1).
- Counts = Poisson sampling + biological variation: negative binomial $\operatorname{Var} = \mu + \alpha\mu^2$, and the square root of the dispersion parameter $\alpha$ (Definition 20.5.1) is the biological coefficient of variation; the airway trend is $0.0101 + 2.583/\mu$ (Example 20.5.1). Negative binomial generalized linear model (Definition 20.5.2): $\log\mu = \log s + \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$, with the size factor as offset. Dispersion: gene-wise (Cox–Reid) → trend → shrinkage centered on the trend (Example 20.5.2).
- Normalization: size factors (Definition 20.6.1, median of ratios) and TMM (Definition 20.6.2) both assume that most genes are unchanged; in airway the two correlate at 0.9999 (Example 20.6.1).
- The paired design `~ cell + dex`: 4691 versus 3422 genes; Wald and likelihood ratio tests nearly agree (4691 versus 4668, Example 20.7.2); shrinkage of fold changes is used for ranking; independent filtering (Definition 20.7.1) removes 3470 low-count genes and raises the detections from 4490 to 4691.
- Zero inflation (Definition 20.8.1): the zeros of UMI data agree with the negative binomial prediction; compare conditions with pseudobulk + negative binomial GLM.
- Enrichment analysis = hypergeometric test = one-sided Fisher's exact test; gene correlation inflates the variance by a factor of $1 + (n - 1)\bar\rho$.

## Questions

1. A study tests 20 independent null hypotheses that are in fact all true, each at $\alpha = 0.05$. What is the probability of at least one false positive? What are the levels per test with the Bonferroni and Šidák corrections?

   **Answer** $1 - 0.95^{20} = 1 - 0.358 = 0.642$. Bonferroni: $0.05/20 = 0.0025$; Šidák: $1 - 0.95^{1/20} = 0.002\,561$. The FWERs are $1 - 0.9975^{20} = 0.0488$ and exactly 0.05 respectively.

2. The $p$-values of 8 tests are 0.001, 0.008, 0.039, 0.041, 0.042, 0.060, 0.074, 0.205. Decide which are rejected using Bonferroni, Holm ($\alpha = 0.05$) and BH ($\alpha = 0.05$), and write the BH-adjusted $p$-values.

   **Answer** The Bonferroni threshold is $0.05/8 = 0.00625$: only 0.001 is rejected. Holm: $0.001 \le 0.05/8$ is rejected; is $0.008 \le 0.05/7 = 0.00714$? No, stop: only 1 is rejected. BH: compare $p_{(i)}$ with $0.05i/8 = 0.00625, 0.0125, 0.01875, 0.025, 0.03125, 0.0375, 0.04375, 0.05$: $p_{(2)} = 0.008 \le 0.0125$, $p_{(3)} = 0.039 > 0.01875$, and $p_{(4)}$ to $p_{(8)}$ all lie above the line, so the largest satisfying $i$ is 2, and the first 2 are rejected. The adjusted $p$-values $m p_{(i)}/i$ are 0.008, 0.032, 0.104, 0.082, 0.0672, 0.080, 0.0846, 0.205; taking cumulative minima from the back gives 0.008, 0.032, 0.0672, 0.0672, 0.0672, 0.080, 0.0846, 0.205. Rejecting those with $\tilde p \le 0.05$ gives the two above, consistently.

3. Explain why controlling the FDR at 0.1 does not mean that "each gene in the list has a 90% probability of being real". Which is more likely to be a false discovery, a gene at the edge of the list or the most significant gene?

   **Answer** The FDR is the expected proportion of false discoveries in the whole list, a statement about the list as a whole. The genes in the list differ in reliability: the most significant genes are almost certainly real, and genes near the threshold are false with a probability far above 10%. The reliability of an individual gene is the local fdr (Definition 20.3.3), which at the threshold is larger than the tail-area Fdr; in airway, when the local fdr falls to 0.2 the corresponding tail-area Fdr is only about 0.04 (Example 20.3.2).

4. Among the $p$-values of 10,000 tests, 2400 are greater than 0.5. Estimate $\pi_0$ by Storey's method and estimate how many null hypotheses are false. If 900 $p$-values are below $t = 0.01$, estimate the FDR.

   **Answer** $\hat\pi_0(0.5) = 2400/(10\,000 \times 0.5) = 0.48$, so about $0.52 \times 10\,000 = 5200$ null hypotheses are estimated to be false. $\widehat{\operatorname{FDR}}(0.01) = 0.48 \times 10\,000 \times 0.01/900 = 48/900 = 0.053$; by BH ($\pi_0 = 1$) the estimate is $100/900 = 0.111$.

5. The normalized counts of a gene are 80, 120, 95, 105 in 4 control samples and 200, 260, 150, 190 in 4 treated samples. (a) Compute the mean and variance of the control group and compare with Poisson; (b) estimate the dispersion parameter $\alpha$ by moments from the control group; (c) what is its approximate biological coefficient of variation?

   **Answer** (a) The mean is 100 and the variance $[(-20)^2 + 20^2 + (-5)^2 + 5^2]/3 = 850/3 = 283.3$, far larger than the mean of 100: overdispersion. (b) From $\operatorname{Var} = \mu + \alpha\mu^2$, $\hat\alpha = (283.3 - 100)/100^2 = 0.0183$. (c) $\sqrt{0.0183} = 0.135$, about 13.5%. Treated group: mean 200, variance $(0 + 3600 + 2500 + 100)/3 = 2066.7$, $\hat\alpha = (2066.7 - 200)/200^2 = 0.047$; with only 4 samples the estimates are very unstable, which is exactly why shrinkage across genes is needed.

6. The counts of 5 genes in two samples are: sample 1: (100, 200, 300, 400, 10,000), sample 2: (100, 200, 300, 400, 30,000). How do the conclusions differ between normalizing by total reads and by the median-of-ratios method?

   **Answer** The total reads are 11,000 and 31,000, a ratio of 2.82; normalizing by it makes the first four genes in sample 2 all drop to about 0.35-fold, looking generally suppressed. Median of ratios: the geometric means of the genes are 100, 200, 300, 400, 17,320; the ratios for sample 1 are 1, 1, 1, 1, 0.577 with median 1; for sample 2 they are 1, 1, 1, 1, 1.732 with median 1. Both size factors are 1: the first four genes are unchanged, and only the fifth gene is raised 3-fold. The latter is the reasonable conclusion: a large increase in one gene should not make other genes "go down" (composition bias, Section 20.6.1).

7. Use the negative binomial variance to show, for a gene with dispersion 0.04, by how much the coefficient of variation of each sample falls if the sequencing depth is increased from reads giving mean 50 to mean 500. What if instead the number of samples per group were increased from 3 to 6?

   **Answer** The coefficient of variation is $\sqrt{1/\mu + \alpha}$: for $\mu = 50$ it is $\sqrt{0.02 + 0.04} = 0.245$; for $\mu = 500$ it is $\sqrt{0.002 + 0.04} = 0.205$, so a 10-fold increase in depth lowers it by only 16%, with a lower limit of $\sqrt{0.04} = 0.2$. The standard error of a group mean is proportional to $1/\sqrt{n}$: increasing the samples from 3 to 6 lowers the standard error to $1/\sqrt2 = 0.707$ times, a reduction of 29%, with no lower limit. When biological variation dominates, adding replicates is more effective than adding depth.

8. An experiment compares two treatments with 2 samples per group; ordinary $t$ tests on 20,000 genes give not a single gene at FDR 0.1. Another analyst using limma obtains 300. Why? When can this shrinkage go wrong?

   **Answer** With 2 samples per group the pooled variance has only 2 degrees of freedom, the tails of the $t_2$ distribution are extremely heavy (the two-sided 0.05 critical value is 4.30), and the variance estimate is extremely unstable, so even a real effect can hardly reach the very small $p$-values needed for FDR 0.1. limma shrinks the variance toward the common value of all genes, which is equivalent to adding $d_0$ degrees of freedom; the null distribution becomes $t_{2 + d_0}$ and the power of the test is greatly increased. The shrinkage assumes that the variances of all genes come from the same prior distribution; if a class of genes truly has variances far larger than the others (genes affected by batch, highly variable stress genes), shrinking them to the common value underestimates their variance and creates false positives. The robust option of limma and the variance trend by expression level (trend) mitigate this problem, and DESeq2 does not shrink genes far above the trend (Section 20.5.4).

9. A researcher first removed the half of the genes with the smallest change, by "the absolute value of the difference of means between the treated and control groups", and then applied BH correction. What is wrong with this? Why is the independent filtering of DESeq2 acceptable?

   **Answer** The filter statistic (difference of means) is highly correlated with the test statistic; almost all the genes removed are nonsignificant, the $p$-values of the genes that remain are no longer uniform under the null hypothesis (too small), and the BH correction computes its threshold with the smaller $m$, so false discoveries run out of control. Independent filtering uses the mean count over all samples without group information; under the null hypothesis it is (approximately) independent of the $t$ or Wald statistic, the $p$-values of the true nulls remaining after filtering are still uniform, and the guarantee of BH still holds (Definition 20.7.1).

10. A list of differentially expressed genes has 400 genes (background 12,000). A pathway has 60 genes, of which 8 are in the list. What is the expected overlap? Judge by the hypergeometric test whether it is enriched; if the mean pairwise correlation of the test statistics of these 60 genes is 0.1, how will a test based on "genes are independent" be biased?

    **Answer** The expected overlap is $400 \times 60/12\,000 = 2$, and 8 are observed, a 4-fold enrichment. $\mathbb{P}(X \ge 8)$ under the hypergeometric distribution with $N = 12\,000$, $K = 400$, $n = 60$ is about $8\times10^{-4}$ (`stats.hypergeom.sf(7, 12000, 400, 60)`), which looks significant. But if these genes are co-regulated, whether they enter the list is correlated: the variance inflation factor is $1 + 59 \times 0.1 = 6.9$, equivalent to only about 9 effectively independent genes, the true uncertainty is much larger than the test assumes, and the $p$-value is too optimistic. A method that accounts for correlation (CAMERA) or a self-contained test with permutation over samples should be used.

11. (Analysis design) A CRISPR knockout screen covers 20,000 genes with 4 sgRNAs per gene, comparing the read counts of each sgRNA before and after drug treatment (3 biological replicates per condition). Design a statistical analysis plan: what model, how to summarize from sgRNAs to genes, and how to control multiplicity?

    **Answer** (1) Count model: the reads of each sgRNA are overdispersed counts, so use a negative binomial model; compute size factors from nontargeting control sgRNAs or the median of ratios over all sgRNAs (once many genes are knocked out the composition may change, so nontargeting controls are safer); shrink the dispersion according to the trend with the mean. (2) The design matrix contains the replicates (pairing) and the condition, and the condition effect is tested (Wald or likelihood ratio). (3) Summarizing to genes: robust rank aggregation of the statistics of the 4 sgRNAs (such as MAGeCK) or a mixed model with sgRNA as a random effect, to prevent one off-target or highly efficient sgRNA from dominating the conclusion. (4) Multiplicity: apply BH with the gene as the unit (using permutation to obtain an empirical null where necessary), report candidates at FDR 0.05–0.1, and check with the distribution of the nontargeting controls whether the null distribution is correct (their $p$-value histogram should be flat). (5) Validation: replication with independent sgRNAs or another perturbation method.
