---
title: "Single-Factor Experiments: Multiple Comparisons"
description: What to do after a significant ANOVA F-test; the multiplicity problem, the family-wise error rate and the false discovery rate; Fisher's LSD, the Benjamini–Hochberg procedure, the Bonferroni correction, Tukey's HSD and Tukey–Kramer, Scheffé's method for all contrasts, and Dunnett's comparisons with a control; their critical values, power and software output.
---

The ANOVA $F$-test of [3.8.3](/3.8.3) answers the first question about a single-factor experiment: are the treatment means all equal? For the plasma etching experiment the answer was a clear no ($F_0 = 66.8$, $p = 2.9\times10^{-9}$). The second question is which means differ, and by how much. Answering it requires many comparisons on the same data, and each comparison is another chance of a false positive; this chapter is about how to keep that risk under control without giving away too much power. We first make the multiplicity problem precise through two error rates, the **family-wise error rate** and the **false discovery rate**, then study the standard procedures one by one, Fisher's LSD, Benjamini–Hochberg, Bonferroni, Tukey, Scheffé and Dunnett, and finally compare their critical values and decide which to use when. The regression course met several of these methods briefly ([3.3.13](/3.3.13)) and the multivariate course the false discovery rate ([3.4.12](/3.4.12)); here they are developed together, with the statistics, the error rate each one controls and the software output that reports it.

Throughout, the model is the single-factor model $Y_{ij} = \mu_i + \varepsilon_{ij}$, $\varepsilon_{ij} \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$, $i = 1, \dots, a$, $j = 1, \dots, n_i$, with $N = \sum_in_i$, and $\mathrm{MS}_{\mathrm{E}}$ on $N - a$ degrees of freedom is the estimate of $\sigma^2$. For the etching data $a = 4$, $n = 5$, the level means are $551.2$, $587.4$, $625.4$, $707.0$ for $160$, $180$, $200$, $220\,\mathrm{W}$, and $\mathrm{MS}_{\mathrm{E}} = 333.7$ on $16$ degrees of freedom.

## 4.1. The Multiple Comparisons Problem

After rejecting $H_0\colon \mu_1 = \cdots = \mu_a$, the natural follow-up is to test, for every pair of levels,

$$
H_0\colon \mu_i = \mu_j \quad\text{versus}\quad H_1\colon \mu_i \ne \mu_j,\qquad 1 \le i < j \le a,
$$
which is $m = \binom a2$ tests; for the etching experiment $m = \binom42 = 6$. More generally, *multiple comparisons* are the inferences about several comparisons of treatment means (pairs, contrasts, comparisons with a control) made on the same data, and multiple comparison procedures are the methods that adjust these inferences for their number.

If every one of $m$ tests is carried out at level $\alpha$, the probability of at least one false rejection grows quickly with $m$. For $m$ independent tests of true null hypotheses,

$$
\mathbb{P}(\text{at least one false positive}) = 1 - \mathbb{P}(\text{no rejection}) = 1 - (1 - \alpha)^m,
$$
which is $0.26$ for $m = 6$ and $0.64$ for $m = 20$ at $\alpha = 0.05$: among twenty tests of true hypotheses we should expect to find "something significant". The pairwise tests of an ANOVA are not independent, since they share the means and $\mathrm{MS}_{\mathrm{E}}$, but the inflation is of the same kind (Section 4.3 computes it exactly).

![The probability of at least one false positive among m independent tests at level 0.05, 1 - 0.95^m, against m, compared with the same probability when each test is carried out at the Bonferroni level 0.05/m.](./plots/fwer-growth.py)

The danger is greatest when the comparisons are not chosen in advance. The sound practice is to state a hypothesis about an underlying effect before the analysis and then carry out a single test for it. *Data dredging* (also called data snooping or data fishing) does the opposite: it performs many tests on the data and reports only those that come back significant, so that patterns are presented as statistically significant when there is no real underlying effect. Comparing the largest with the smallest sample mean because they look different is a hidden multiple comparison of all pairs, and must be judged as such.

To describe what can go wrong, classify the $m$ hypotheses $H_{0,1}, \dots, H_{0,m}$ by whether they are true and whether they are rejected:

| $H_{0,i}$ | Accepted | Rejected | Total |
|---|---|---|---|
| True | $U$ | $V$ | $m_0$ |
| False | $T$ | $S$ | $m - m_0$ |
| Total | $m - R$ | $R$ | $m$ |

Only $m$ and $R$, the number of rejections ("discoveries"), are observed. $V$ is the number of false rejections (**type I errors**), $T$ the number of missed effects (**type II errors**), and $S$ the number of correct discoveries.

## 4.2. Family-Wise Error Rate and False Discovery Rate

**Definition 4.2.1 (Family-Wise Error Rate)** The **family-wise error rate** of a multiple testing procedure is the probability of at least one type I error among the tests of the family:

$$
\mathrm{FWER} = \mathbb{P}(V \ge 1).
$$
A procedure controls the FWER at level $\alpha$ if $\mathrm{FWER} \le \alpha$ whatever the configuration of true and false hypotheses (strong control); it controls it in the weak sense if this holds when all null hypotheses are true, $\mathrm{FWER} = \mathbb{P}(\text{reject at least one } H_{0,i} \mid \text{all } H_{0,i} \text{ true})$.

"Family-wise" means "simultaneously". With $a = 4$ there are six hypotheses $\mu_i = \mu_k$; under the global null hypothesis $\mu_1 = \cdots = \mu_4$, a study makes an error if any of the six is falsely rejected. Imagine repeating the study $100$ times. Testing only $\mu_1 = \mu_2$ at level $0.05$, a false rejection occurs in about $5$ of the $100$ studies. Testing all six with FWER $= 0.05$, a false rejection of any of the six occurs in about $5$ of the $100$ studies: the error budget is spent on the family, not on each comparison. The **comparisonwise error rate** ([3.3.13](/3.3.13)), the type I error rate of each comparison by itself, is what an unadjusted test controls.

When many hypotheses are tested and a few false discoveries are acceptable, FWER control is too strict. Benjamini and Hochberg (1995) proposed controlling instead the expected proportion of false discoveries among the rejections.

**Definition 4.2.2 (False Discovery Rate)** The **false discovery rate** is

$$
\mathrm{FDR} = \mathbb{E}\Bigl[\frac{V}{\max(R, 1)}\Bigr],
$$
the expected proportion of false discoveries among the rejected hypotheses, where the ratio is taken as $0$ when nothing is rejected.

**Proposition 4.2.1** For every procedure $\mathrm{FDR} \le \mathrm{FWER}$, with equality when all null hypotheses are true ($m_0 = m$). Hence controlling the FWER at level $\alpha$ implies controlling the FDR at level $\alpha$, and FWER control is the stricter requirement.

**Proof** If $V = 0$ then $V/\max(R, 1) = 0$; if $V \ge 1$ then $R \ge V \ge 1$ and $V/R \le 1$. Thus $V/\max(R, 1) \le \boldsymbol{1}_{\{V \ge 1\}}$, and taking expectations, $\mathrm{FDR} \le \mathbb{P}(V \ge 1) = \mathrm{FWER}$. If $m_0 = m$, every rejection is false, $V = R$, and $V/\max(R, 1) = \boldsymbol{1}_{\{V \ge 1\}}$ exactly. $\square$

When many hypotheses are false, $S$ tends to be large, the ratio $V/R$ is much smaller than $\boldsymbol{1}_{\{V \ge 1\}}$, and FDR control allows many more rejections. Which rate to control depends on the cost of a false positive relative to a missed effect.

- An exploratory study of a new anticancer drug records many endpoints: metabolic rate, the number and size of measurable lesions, the status of non-target lesions, tumor markers, gene expression at baseline biopsy, and so on. The goal is to find promising signals for later confirmation; a few false leads among many findings are tolerable, while missing a real effect is costly. Controlling the FDR keeps the power that makes discovery possible.
- A diagnostic protocol for a very dangerous disease consists of several tests, and a patient is declared healthy only if every test says so. A single false positive in the sense of "declared healthy" may send a sick patient home, with possibly fatal consequences. Here even one error is unacceptable, and the FWER must be controlled.

In general, FWER control suits confirmatory studies with a few planned comparisons, where any false claim is serious; FDR control suits screening with many hypotheses (genes, voxels, endpoints), where the discoveries will be followed up.

## 4.3. Fisher's Least Significant Difference

### 4.3.1. From Multiple t-Tests to the LSD

For one pair $(i, j)$, the two-sample $t$-test of [3.8.2](/3.8.2) uses only the data of groups $i$ and $j$:

$$
t_0 = \frac{\bar y_{i\cdot} - \bar y_{j\cdot}}{s_p\sqrt{\frac{1}{n_i} + \frac{1}{n_j}}} \sim t_{n_i + n_j - 2},\qquad s_p^2 = \frac{(n_i - 1)s_i^2 + (n_j - 1)s_j^2}{n_i + n_j - 2}.
$$
Under the ANOVA model all $a$ groups have the same variance, so a better estimate of $\sigma^2$ is $\mathrm{MS}_{\mathrm{E}}$, which pools all $N$ observations.

**Definition 4.3.1 (Fisher's Least Significant Difference)** **Fisher's least significant difference** method tests $H_0\colon \mu_i = \mu_j$ by

$$
t_0 = \frac{\bar y_{i\cdot} - \bar y_{j\cdot}}{\sqrt{\mathrm{MS}_{\mathrm{E}}\bigl(\frac{1}{n_i} + \frac{1}{n_j}\bigr)}} \sim t_{N-a}\quad\text{under } H_0,
$$
and rejects when $\lvert t_0\rvert > t_{N-a,\alpha/2}$, that is, when $\lvert\bar y_{i\cdot} - \bar y_{j\cdot}\rvert$ exceeds the least significant difference

$$
\mathrm{LSD} = t_{N-a,\alpha/2}\sqrt{\mathrm{MS}_{\mathrm{E}}\Bigl(\frac{1}{n_i} + \frac{1}{n_j}\Bigr)}\qquad\Bigl(= t_{N-a,\alpha/2}\sqrt{2\mathrm{MS}_{\mathrm{E}}/n}\ \text{if balanced}\Bigr).
$$

The LSD test differs from running $m$ separate two-sample $t$-tests in two ways. The standard error uses the pooled variance of all $a$ groups instead of the two groups being compared, and the reference distribution has $N - a$ degrees of freedom instead of $n_i + n_j - 2$. Both changes are consequences of the common-variance assumption and both make the test more powerful: the variance estimate is more precise and the critical value smaller. (If the variances are unequal, the pooled $\mathrm{MS}_{\mathrm{E}}$ can be badly wrong for a particular pair, which is one reason to check the assumption, [3.8.5](/3.8.5).) For the etching data, comparing $160$ and $180\,\mathrm{W}$, the two-sample $t$-test gives $t_0 = 3.10$ on $8$ degrees of freedom, $p = 0.015$; the LSD test gives $t_0 = 36.2/\sqrt{333.7 \times 2/5} = 36.2/11.55 = 3.13$ on $16$ degrees of freedom, $p = 0.0064$.

### 4.3.2. The LSD as a General Linear Test

The LSD test is the general linear test ([3.8.3](/3.8.3)) of the single restriction $\mu_i = \mu_j$ within the full means model. The reduced model forces the two means to be equal, and in the geometric picture of [3.8.3](/3.8.3) it is a subspace $\omega_{ij}$ of the model space $\Omega$ of dimension $a - 1$, so $\Omega \ominus \omega_{ij}$ is one-dimensional, spanned by the vector $\boldsymbol{v}$ with entries $1/n_i$ in group $i$, $-1/n_j$ in group $j$ and $0$ elsewhere. The reduction in the error sum of squares is the squared length of the projection of $\boldsymbol{y}$ onto $\boldsymbol{v}$:

$$
\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F) = \frac{(\boldsymbol{v}^{\mathsf T}\boldsymbol{y})^2}{\boldsymbol{v}^{\mathsf T}\boldsymbol{v}} = \frac{(\bar y_{i\cdot} - \bar y_{j\cdot})^2}{\frac{1}{n_i} + \frac{1}{n_j}},
$$
so that

$$
F = \frac{[\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F)]/1}{\mathrm{MS}_{\mathrm{E}}(F)} = \frac{(\bar y_{i\cdot} - \bar y_{j\cdot})^2}{\mathrm{MS}_{\mathrm{E}}\bigl(\frac{1}{n_i} + \frac{1}{n_j}\bigr)} = t_0^2 \sim F_{1,N-a}.
$$
The overall ANOVA $F$-test compares $\Omega$ with $\omega$ ($a - 1$ degrees of freedom); each LSD test compares $\Omega$ with a hyperplane $\omega_{ij}$ (one degree of freedom).

### 4.3.3. The LSD Does Not Control the Error Rate

The LSD method makes no adjustment for the number of comparisons. Each test has level $\alpha$, so it controls the comparisonwise error rate, but neither the FWER nor the FDR: under the global null hypothesis all rejections are false, FDR $=$ FWER (Proposition 4.2.1), and for $a = 4$, $N - a = 16$, the probability that at least one of the six LSD tests rejects is

$$
\mathbb{P}\Bigl(\max_{i<j}\lvert t_{ij}\rvert > t_{16,0.025}\Bigr) = \mathbb{P}\bigl(Q_{4,16} > \sqrt2 \times 2.120\bigr) = 0.19,
$$
where $Q_{4,16}$ has the studentized range distribution of Section 4.6; for $a = 6$ it is $0.34$. In exchange, the LSD has the smallest critical value and therefore the highest power of all the methods in this chapter.

A common safeguard is the protected LSD: the pairwise tests are made only if the overall $F$-test is significant. Under the global null hypothesis the pairwise tests are then reached with probability $\alpha$, so the FWER is controlled in the weak sense; but once some means differ, the overall test is passed easily and the protection disappears for the remaining equal means. The protected LSD is therefore not a strong FWER procedure in general. The LSD is appropriate for a single planned comparison, or as an initial screen whose findings will be confirmed.

### 4.3.4. Software Output

R computes all unadjusted pairwise tests with the pooled standard deviation by `pairwise.t.test`:

```r
pairwise.t.test(etch.rate$rate, etch.rate$RF, p.adjust.method = "none")
```

```text
	Pairwise comparisons using t tests with pooled SD 

data:  etch.rate$rate and etch.rate$RF 

    160     180     200    
180 0.0064  -       -      
200 8.4e-06 0.0046  -      
220 3.7e-10 1.7e-08 2.7e-06

P value adjustment method: none 
```

Every pair differs at the $0.05$ level. Commercial packages print the same information with the standard errors: the standard error of each level mean is $\sqrt{\mathrm{MS}_{\mathrm{E}}/n} = 18.27/\sqrt5 = 8.17$, and that of each difference of means is $\sqrt{2\mathrm{MS}_{\mathrm{E}}/n} = 18.27\sqrt{2/5} = 11.55$; with $t_{16,0.025} = 2.120$ the least significant difference is $2.120 \times 11.55 = 24.5$, and all six observed differences ($36.2$ to $155.8$) exceed it.

## 4.4. Controlling the FDR: The Benjamini–Hochberg Procedure

Suppose $m$ null hypotheses $H_{0,1}, \dots, H_{0,m}$ (the global null is their intersection $\bigcap_iH_{0,i}$) are tested with statistics whose $p$-values $p_1, \dots, p_m$ are uniformly distributed on $(0, 1)$ under their own null hypotheses.

**Algorithm 4.4.1 (Benjamini–Hochberg Procedure)** Fix $\alpha \in (0, 1)$.

1. Order the $p$-values, $p_{(1)} \le p_{(2)} \le \cdots \le p_{(m)}$.
2. Let $i_0$ be the largest $i$ for which $p_{(i)} \le \frac{i}{m}\alpha$ (if there is none, reject nothing).
3. Reject $H_{0,(1)}, \dots, H_{0,(i_0)}$.

Graphically, plot $p_{(i)}$ against $i$ and draw the line $y = \alpha x/m$; all hypotheses up to the last $p$-value below the line are rejected, even those whose own $p$-values lie above it. The threshold starts at the Bonferroni level $\alpha/m$ and rises to $\alpha$. The adjusted $p$-values reported by software are $\tilde p_{(i)} = \min_{k \ge i}\min\bigl(1, \frac{m}{k}p_{(k)}\bigr)$, and $H_{0,(i)}$ is rejected when $\tilde p_{(i)} \le \alpha$.

**Theorem 4.4.1** If the $p$-values are independent, the Benjamini–Hochberg procedure satisfies

$$
\mathrm{FDR} = \frac{m_0}{m}\alpha \le \alpha.
$$

**Proof** If $m_0 = 0$ then $V = 0$ and $\mathrm{FDR} = 0$. Let $m_0 \ge 1$, let $\mathcal{H}_0$ be the set of indices of true null hypotheses, and $V_i = \boldsymbol{1}\{H_{0,i} \text{ rejected}\}$. Then $V/\max(1, R) = \sum_{i\in\mathcal{H}_0}X_i$ with

$$
X_i = \frac{V_i}{\max(1, R)} = \sum_{k=1}^m\frac{V_i}{k}\boldsymbol{1}\{R = k\} = \sum_{k=1}^m\frac{\boldsymbol{1}\{p_i \le \frac{k}{m}\alpha\}}{k}\boldsymbol{1}\{R = k\},
$$
because when exactly $k$ hypotheses are rejected, $H_{0,i}$ is among them if and only if $p_i \le \frac{k}{m}\alpha$. Let $R(p_i \to 0)$ be the number of rejections when $p_i$ is replaced by $0$ and the other $p$-values are unchanged. On the event $p_i \le \frac km\alpha$ we have $R = k$ if and only if $R(p_i \to 0) = k$: with $N_j$ the number of $p$-values not exceeding $\frac jm\alpha$, the procedure rejects $R = \max\{j\colon N_j \ge j\}$ hypotheses, and moving $p_i$ to $0$ leaves $N_j$ unchanged for every $j \ge k$, so the largest $j \ge k$ with $N_j \ge j$ is the same in both cases. Hence

$$
X_i = \sum_{k=1}^m\frac{\boldsymbol{1}\{p_i \le \frac{k}{m}\alpha\}}{k}\boldsymbol{1}\{R(p_i \to 0) = k\}.
$$
$R(p_i \to 0)$ depends only on the other $p$-values, which are independent of $p_i \sim \mathrm{U}(0, 1)$. Conditioning on them,

$$
\mathbb{E}[X_i \mid p_{-i}] = \sum_{k=1}^m\frac{\mathbb{P}(p_i \le \frac km\alpha)}{k}\boldsymbol{1}\{R(p_i \to 0) = k\} = \frac{\alpha}{m}\sum_{k=1}^m\boldsymbol{1}\{R(p_i \to 0) = k\} = \frac{\alpha}{m},
$$
since $R(p_i \to 0) \ge 1$ takes exactly one value. By the law of total expectation $\mathbb{E}X_i = \alpha/m$, and $\mathrm{FDR} = \sum_{i\in\mathcal{H}_0}\mathbb{E}X_i = m_0\alpha/m$. $\square$

The bound $\mathrm{FDR} \le \alpha$ remains valid under positive dependence of the test statistics (Benjamini and Yekutieli, 2001), which covers the pairwise comparisons of an ANOVA. A different proof of the theorem is given in [3.4.12](/3.4.12).

For the etching data the six unadjusted $p$-values of Section 4.3.4 can be processed by hand or by `p.adjust`:

```r
# Obtain p-values for each pairwise comparison
pairwise_p <- pairwise.t.test(etch.rate$rate, etch.rate$RF,
                              p.adjust.method = "none")$p.value
p <- pairwise_p[lower.tri(pairwise_p, diag = TRUE)]
# Step 1: sort the p-values
sorted_p <- sort(p); ranked_p <- rank(p)
# Step 2: find the largest i such that p_(i) <= (i/m) * alpha
m <- length(p); critical_values <- (1:m / m) * 0.05
valid_indices <- sorted_p <= critical_values
if (any(valid_indices)) {
  largest_i <- max(which(valid_indices))
  threshold <- sorted_p[largest_i]
  # Step 3: determine significant hypotheses
  significant_pairs <- p <= threshold
} else {
  significant_pairs <- rep(FALSE, length(p))
}
significant_pairs
pairwise.t.test(etch.rate$rate, etch.rate$RF, p.adjust.method = "BH")
```

```text
> pairwise_p
             160          180          200
180 6.416224e-03           NA           NA
200 8.438627e-06 4.624381e-03           NA
220 3.728559e-10 1.693894e-08 2.683834e-06
> significant_pairs
[1] TRUE TRUE TRUE TRUE TRUE TRUE

	Pairwise comparisons using t tests with pooled SD 

data:  etch.rate$rate and etch.rate$RF 

    160     180     200    
180 0.0064  -       -      
200 1.3e-05 0.0055  -      
220 2.2e-09 5.1e-08 5.4e-06

P value adjustment method: BH 
```

The largest $p$-value, $0.0064$, is below its threshold $\frac66 \times 0.05$, so all six hypotheses are rejected. The adjusted values show the rule: the second largest, $0.0046$, becomes $\frac65 \times 0.0046 = 0.0055$; the smallest, $3.7\times10^{-10}$, becomes $6 \times 3.7\times10^{-10} = 2.2\times10^{-9}$.

The difference between the error rates is clearest in large-scale testing. In the following simulation, each of $1000$ replications performs $m = 1000$ one-sided $z$-tests, $800$ of true null hypotheses and $200$ with effect size $2.5$, at $\alpha = 0.05$, with no correction, with BH and with Bonferroni. Without correction the average false discovery proportion is about $0.20$ and every replication contains false positives (FWER $= 1$); BH holds the FDR at about $0.04 = \frac{m_0}{m}\alpha$, but at least one false positive still occurs in about $98\%$ of the replications; Bonferroni makes the FWER about $0.04$ and the FDR almost zero. The price appears in the power: the proportion of the $200$ real effects detected is about $0.80$, $0.47$ and $0.08$ respectively.

![Simulation of 1000 replications of 1000 one-sided z-tests, 80% of them true nulls, at alpha = 0.05. Left: distribution of the false discovery proportion without correction, with Benjamini-Hochberg and with Bonferroni. Right: average FDR, FWER and power of the three procedures.](./plots/fdr-fwer-simulation.py)

## 4.5. Controlling the FWER: The Bonferroni Correction

Define the event $A_{ij} = \bigl\{\lvert t_{ij}\rvert > t_{N-a,\alpha/(2m)}\bigr\}$, where $t_{ij}$ is the LSD statistic of the pair $(i, j)$. By the Bonferroni inequality (the first step of inclusion–exclusion),

$$
\mathbb{P}\Bigl(\bigcup_{(i,j)\colon\mu_i = \mu_j}A_{ij}\Bigr) \le \sum_{(i,j)\colon\mu_i = \mu_j}\mathbb{P}(A_{ij}) \le m\cdot\frac{\alpha}{m} = \alpha.
$$
So testing each of the $m$ comparisons at level $\alpha/m$ (the **Bonferroni correction**) controls the FWER at level $\alpha$ in the strong sense, whatever the dependence between the tests. Equivalently, the Bonferroni-adjusted $p$-values are $\min(1, mp_i)$, and those below $\alpha$ are significant. For $m = 20$ independent tests the per-test level is $0.05/20 = 0.0025$ and the FWER is $1 - (1 - 0.0025)^{20} = 0.0488$. For independent tests the exact per-test level is $1 - (1 - \alpha)^{1/m} = 0.00256$ (the **Šidák correction**), barely larger: Bonferroni loses very little when the tests are independent.

```r
pairwise.t.test(etch.rate$rate, etch.rate$RF, p.adjust.method = "bonferroni")
```

```text
	Pairwise comparisons using t tests with pooled SD 

data:  etch.rate$rate and etch.rate$RF 

    160     180     200    
180 0.038   -       -      
200 5.1e-05 0.028   -      
220 2.2e-09 1.0e-07 1.6e-05

P value adjustment method: bonferroni 
```

Each entry is six times the unadjusted value: $6 \times 0.0064 = 0.038$, $6 \times 0.0046 = 0.028$, $6 \times 8.4\times10^{-6} = 5.1\times10^{-5}$. This constant ratio is how a Bonferroni adjustment is recognized in an output. All six pairs remain significant at $0.05$.

The price of FWER control is power: making false positives rarer makes false negatives more common. The following code simulates $1000$ one-sided tests, $900$ of true null hypotheses and $100$ with a shift of $3$ standard deviations:

```r
x <- c(rnorm(900), rnorm(100, mean = 3))
p <- pnorm(x, lower.tail = F)
test <- p > 0.05
summary(test[1:900]); summary(test[901:1000])
```

```text
   Mode   FALSE    TRUE 
logical      46     854 
   Mode   FALSE    TRUE 
logical      88      12 
```

In this run $46$ of the $900$ true null hypotheses were rejected at level $0.05$ and $12$ of the $100$ real effects were missed. Repeating the count at several levels and with the two corrections gave the following proportions of type I errors (among the $900$ true nulls) and of type II errors (among the $100$ false nulls):

| Type I error rate, $\alpha =$ | 0.0001 | 0.001 | 0.01 | 0.025 | 0.05 | 0.1 |
|---|---|---|---|---|---|---|
| Uncorrected | 0.0011 | 0.0022 | 0.0144 | 0.0344 | 0.0511 | 0.1056 |
| Bonferroni | 0 | 0 | 0 | 0.0011 | 0.0011 | 0.0011 |
| BH | 0 | 0 | 0.0011 | 0.0022 | 0.0033 | 0.0122 |

| Type II error rate, $\alpha =$ | 0.0001 | 0.001 | 0.01 | 0.025 | 0.05 | 0.1 |
|---|---|---|---|---|---|---|
| Uncorrected | 0.70 | 0.45 | 0.20 | 0.13 | 0.12 | 0.07 |
| Bonferroni | 1 | 0.94 | 0.87 | 0.80 | 0.77 | 0.70 |
| BH | 1 | 0.81 | 0.57 | 0.39 | 0.30 | 0.20 |

At every level the corrections nearly eliminate type I errors, Bonferroni most thoroughly, and both increase type II errors, Bonferroni far more than BH. The Bonferroni correction requires no independence assumption, which is its great advantage; its disadvantage is that it is conservative when the number of tests is large or when the test statistics are positively correlated, because the union bound then overestimates the probability of the union. For the pairwise comparisons of an ANOVA the statistics are correlated in a known way, and using that structure gives a more powerful method, Tukey's.

## 4.6. Tukey's Honestly Significant Difference

### 4.6.1. The Studentized Range

**Definition 4.6.1 (Studentized Range)** Let $W_1, \dots, W_k$ be a sample and $s$ an estimate of their standard deviation with $\nu$ degrees of freedom. The **studentized range** is the difference between the largest and the smallest value measured in units of $s$:

$$
q = \frac{W_{\max} - W_{\min}}{s}.
$$
When $W_1, \dots, W_k \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma^2)$ and $\nu s^2/\sigma^2 \sim \chi^2_\nu$ independently of the $W_i$, the distribution of $q$ does not depend on $\mu$ or $\sigma$; it is the **studentized range distribution** $Q_{k,\nu}$ ([3.3.13](/3.3.13)), with upper $\alpha$ quantile $q_{k,\nu,\alpha}$.

In Tukey's test the sample consists of the $a$ treatment means. If each of $a$ normal populations with the same $\mathcal{N}(\mu, \sigma^2)$ is sampled $n$ times, then

$$
q = \frac{\bar y_{\max} - \bar y_{\min}}{\sqrt{\mathrm{MS}_{\mathrm{E}}/n}} \sim Q_{a,N-a},
$$
where $\bar y_{\max}$ is the largest and $\bar y_{\min}$ the smallest of the sample means, and $\mathrm{MS}_{\mathrm{E}}$ is the pooled sample variance with $N - a$ degrees of freedom. The range of more means is larger, so $q_{a,\nu,\alpha}$ increases with $a$.

![Densities of the studentized range distribution with nu = 16 degrees of freedom for k = 2, 3, 4 and 6 means; the upper 5% quantiles are marked.](./plots/studentized-range.py)

For $k = 2$ the density is largest at $0$, while for $k \ge 3$ it vanishes there. The reason is that with two means the range is the absolute value of their difference:

$$
q = \frac{\lvert\bar y_1 - \bar y_2\rvert}{s/\sqrt n} = \sqrt2\,\frac{\lvert\bar y_1 - \bar y_2\rvert}{s\sqrt{2/n}} = \sqrt2\lvert t\rvert.
$$
Under the null hypothesis $\bar y_1 - \bar y_2 \sim \mathcal{N}(0, 2\sigma^2/n)$, whose absolute value has a half-normal distribution, and $\lvert t\rvert$ has a folded $t$ density, which is decreasing on $(0, \infty)$ with its maximum at $0$. With three or more means, the range is near $0$ only if all the means nearly coincide, which is unlikely. The identity $q = \sqrt2\lvert t\rvert$ also shows that for $k = 2$ Tukey's test is the ordinary $t$-test: $q_{2,\nu,\alpha}/\sqrt2 = t_{\nu,\alpha/2}$. In R, `qtukey(p = .95, nmeans = 2, df = 8)/sqrt(2)` and `qt(p = .975, df = 8)` both return $2.306$.

### 4.6.2. Tukey's Test

Tukey's test (also called Tukey's range test, the honestly significant difference test, or **Tukey's HSD**) tests every pair $H_0\colon \mu_i = \mu_j$ against $H_1\colon \mu_i \ne \mu_j$ in a balanced experiment with the statistic

$$
q_0 = \frac{\lvert\bar y_{i\cdot} - \bar y_{j\cdot}\rvert}{\sqrt{\mathrm{MS}_{\mathrm{E}}/n}} = \sqrt2\lvert t_{ij}\rvert,
$$
and rejects when $q_0 > q_{a,N-a,\alpha}$, that is, when $\lvert\bar y_{i\cdot} - \bar y_{j\cdot}\rvert > \mathrm{HSD} = q_{a,N-a,\alpha}\sqrt{\mathrm{MS}_{\mathrm{E}}/n}$. Equivalently, the simultaneous confidence intervals are

$$
\bar y_{i\cdot} - \bar y_{j\cdot} \pm q_{a,N-a,\alpha}\sqrt{\frac{\mathrm{MS}_{\mathrm{E}}}{n}},\qquad 1 \le i < j \le a.
$$

**Theorem 4.6.1** In a balanced single-factor experiment, Tukey's intervals cover all differences $\mu_i - \mu_j$ simultaneously with probability exactly $1 - \alpha$. In particular Tukey's test controls the FWER at level $\alpha$ in the strong sense, with equality under the global null hypothesis:

$$
\mathbb{P}\Bigl(\text{conclude } \mu_i \ne \mu_j \text{ for at least one pair} \Bigm| H_0\colon \mu_1 = \cdots = \mu_a\Bigr) = \mathbb{P}\Bigl(\max_{i,j}\frac{\lvert\bar y_{i\cdot} - \bar y_{j\cdot}\rvert}{\sqrt{\mathrm{MS}_{\mathrm{E}}/n}} > q_{a,N-a,\alpha}\Bigr) = \mathbb{P}\Bigl(\frac{\bar y_{\max} - \bar y_{\min}}{\sqrt{\mathrm{MS}_{\mathrm{E}}/n}} > q_{a,N-a,\alpha}\Bigr) = \alpha.
$$

**Proof** Let $W_i = \bar Y_{i\cdot} - \mu_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2/n)$, independent of $\mathrm{MS}_{\mathrm{E}}$. All intervals cover if and only if $\lvert W_i - W_j\rvert \le q_{a,N-a,\alpha}\sqrt{\mathrm{MS}_{\mathrm{E}}/n}$ for all pairs, that is, if and only if $(W_{\max} - W_{\min})/\sqrt{\mathrm{MS}_{\mathrm{E}}/n} \le q_{a,N-a,\alpha}$, an event of probability $1 - \alpha$ by Definition 4.6.1. A false rejection of some true $\mu_i = \mu_j$ means that the interval for that pair misses $\mu_i - \mu_j = 0$, so it implies non-coverage, and the FWER is at most $\alpha$ for every configuration of the means. Under the global null hypothesis $W_i - W_j = \bar Y_{i\cdot} - \bar Y_{j\cdot}$ and the events coincide. $\square$

The $p$-value of a Tukey comparison is therefore $\mathbb{P}\bigl(Q_{a,N-a} \ge \sqrt2\lvert t_{ij}\rvert\bigr)$, where $t_{ij}$ is the LSD statistic; it is not $2\mathbb{P}(t_{N-a} \ge \lvert t_{ij}\rvert)$, which is the unadjusted $p$-value.

For the etching data, $q_{4,16,0.05} = 4.046$, so $\mathrm{HSD} = 4.046 \times 8.17 = 33.05$, and all six differences exceed it.

```r
mod <- aov(rate ~ RF, data = etch.rate)
TukeyHSD(mod)
plot(TukeyHSD(mod))
```

```text
  Tukey multiple comparisons of means
    95% family-wise confidence level

Fit: aov(formula = rate ~ RF, data = etch.rate)

$RF
         diff        lwr       upr     p adj
180-160  36.2   3.145624  69.25438 0.0294279
200-160  74.2  41.145624 107.25438 0.0000455
220-160 155.8 122.745624 188.85438 0.0000000
200-180  38.0   4.945624  71.05438 0.0215995
220-180 119.6  86.545624 152.65438 0.0000001
220-200  81.6  48.545624 114.65438 0.0000146
```

Each row gives the estimated difference `diff` $= \bar y_{i\cdot} - \bar y_{j\cdot}$, the simultaneous 95% limits `lwr` and `upr` $= \mathrm{diff} \mp 33.05$, and the Tukey-adjusted $p$-value `p adj`. For $180$ versus $160\,\mathrm{W}$, $t_{ij} = 3.133$ and $p = \mathbb{P}(Q_{4,16} \ge 4.431) = 0.029$, compared with the unadjusted $0.0064$ and the Bonferroni $0.038$: Tukey's adjustment is milder than Bonferroni's, because it accounts for the correlation of the six comparisons. No interval contains $0$, so all four power levels differ from one another.

![Simultaneous 95% intervals for the six pairwise differences of the etching means: Tukey's intervals compared with the individual LSD intervals.](./plots/tukey-intervals.py)

### 4.6.3. Unequal Sample Sizes: The Tukey–Kramer Method

The studentized range argument needs equal sample sizes, since the means must have a common variance. For unbalanced data the standard error of each difference is used instead.

**Definition 4.6.2 (Tukey–Kramer Method)** The **Tukey–Kramer method** gives the intervals

$$
\bar y_{i\cdot} - \bar y_{j\cdot} \pm \frac{q_{a,N-a,\alpha}}{\sqrt2}\sqrt{\mathrm{MS}_{\mathrm{E}}\Bigl(\frac{1}{n_i} + \frac{1}{n_j}\Bigr)},\qquad 1 \le i < j \le a,
$$
and declares $\mu_i \ne \mu_j$ when the interval excludes $0$.

For $n_i = n$ this is Tukey's interval, since $\frac{q}{\sqrt2}\sqrt{2\mathrm{MS}_{\mathrm{E}}/n} = q\sqrt{\mathrm{MS}_{\mathrm{E}}/n}$. For unequal sample sizes the coverage is no longer exactly $1 - \alpha$, but it is at least $1 - \alpha$ (Hayter, 1984), so the method is slightly conservative. `TukeyHSD` in R applies the Tukey–Kramer formula automatically when the design is unbalanced.

## 4.7. Scheffé's Method for All Contrasts

### 4.7.1. From Pairwise Comparisons to Contrasts

Pairwise differences are not the only questions of interest. In the etching experiment we might ask whether the average rate at the two lowest settings differs from the rate at $200\,\mathrm{W}$, $H_0\colon (\mu_1 + \mu_2)/2 = \mu_3$, or compare $(\mu_1 + \mu_3)/2$ with $\mu_4$. Such questions are **contrasts** ([3.3.13](/3.3.13)): linear combinations $C = \sum_{i=1}^a c_i\mu_i$ with $\sum_ic_i = 0$. A consumer testing group comparing the gas mileage of five cars, a Ford Escape (hybrid), a Toyota Camry, a Toyota Prius (hybrid), a Honda Accord and a Honda Civic (hybrid), with $n$ prescribed test runs each, might define the following contrasts of the means $\mu_1, \dots, \mu_5$:

| Question | $c_1$ | $c_2$ | $c_3$ | $c_4$ | $c_5$ |
|---|---|---|---|---|---|
| $C_1$: American brand vs foreign brands | 4 | −1 | −1 | −1 | −1 |
| $C_2$: Toyota vs Honda | 0 | −1 | −1 | 1 | 1 |
| $C_3$: hybrid vs non-hybrid | 2 | −3 | 2 | −3 | 2 |
| $C_4$: within Toyota | 0 | −1 | 1 | 0 | 0 |
| $C_5$: within Honda | 0 | 0 | 0 | −1 | 1 |

A contrast is estimated by $\hat C = \sum_ic_i\bar y_{i\cdot}$ with $\operatorname{Var}(\hat C) = \sigma^2\sum_ic_i^2/n_i$, and the $t$-statistic of $H_0\colon C = 0$ is

$$
t_0(C) = \frac{\hat C}{\operatorname{se}(\hat C)} = \frac{\sum_ic_i\bar y_{i\cdot}}{\sqrt{\mathrm{MS}_{\mathrm{E}}\sum_ic_i^2/n_i}},\qquad t_0(C)^2 = \frac{\mathrm{SS}_C}{\mathrm{MS}_{\mathrm{E}}},\quad \mathrm{SS}_C = \frac{\bigl(\sum_ic_i\bar y_{i\cdot}\bigr)^2}{\sum_ic_i^2/n_i},
$$
where $\mathrm{SS}_C$ is the **contrast sum of squares**. For one contrast chosen in advance, $\lvert t_0(C)\rvert > t_{N-a,\alpha/2}$ is a valid test. If the contrasts are suggested by the data, or if there is no limit on how many will be examined, the family is the set of all contrasts, which is infinite, and neither Bonferroni nor Tukey applies.

### 4.7.2. Scheffé's Test

**Theorem 4.7.1 (Scheffé's Method)** For a contrast $C = \sum_ic_i\mu_i$, let

$$
F_0(C) = \frac{t_0(C)^2}{a - 1} = \frac{\bigl(\sum_ic_i\bar y_{i\cdot}\bigr)^2}{(a - 1)\,\mathrm{MS}_{\mathrm{E}}\sum_ic_i^2/n_i}.
$$
The test that rejects $H_0\colon C = 0$ when $F_0(C) > F_{a-1,N-a,\alpha}$, equivalently when $\lvert\hat C\rvert > \sqrt{(a - 1)F_{a-1,N-a,\alpha}}\operatorname{se}(\hat C)$, controls the FWER at level $\alpha$ over the family of all contrasts. Under the global null hypothesis,

$$
\sup_C F_0(C) = F_0 = \frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}},
$$
the ANOVA $F$ statistic, and the supremum is attained by $c_i \propto n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$.

**Proof** Since $\sum_ic_i = 0$, $\hat C = \sum_ic_i\bar y_{i\cdot} = \sum_ic_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$ with $\bar y_{\cdot\cdot} = \sum_in_i\bar y_{i\cdot}/N$. By the **Cauchy–Schwarz inequality** applied to the vectors $(c_i/\sqrt{n_i})$ and $(\sqrt{n_i}(\bar y_{i\cdot} - \bar y_{\cdot\cdot}))$,

$$
\hat C^2 = \Bigl(\sum_i\frac{c_i}{\sqrt{n_i}}\sqrt{n_i}(\bar y_{i\cdot} - \bar y_{\cdot\cdot})\Bigr)^2 \le \sum_i\frac{c_i^2}{n_i}\cdot\sum_in_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2 = \sum_i\frac{c_i^2}{n_i}\cdot\mathrm{SS}_{\mathrm{Tr}},
$$
with equality when $c_i/\sqrt{n_i} \propto \sqrt{n_i}(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$, which is a contrast. Hence

$$
t_0(C)^2 = \frac{\hat C^2}{\mathrm{MS}_{\mathrm{E}}\sum_ic_i^2/n_i} \le \frac{\mathrm{SS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}} = (a - 1)F_0,\qquad\text{so } F_0(C) \le F_0 \text{ for every contrast}.
$$
Under the global null hypothesis $F_0 \sim F_{a-1,N-a}$, so

$$
\mathrm{FWER} = \mathbb{P}\Bigl(F_0(C) > F_{a-1,N-a,\alpha} \text{ for some } C\Bigr) = \mathbb{P}\bigl(F_0 > F_{a-1,N-a,\alpha}\bigr) = \alpha.
$$
For an arbitrary configuration of the means, apply the same argument to $\bar y_{i\cdot} - \mu_i$ in place of $\bar y_{i\cdot}$: the quantity $\sum_in_i\bigl((\bar y_{i\cdot} - \mu_i) - \overline{(\bar y - \mu)}\bigr)^2/((a - 1)\mathrm{MS}_{\mathrm{E}})$ has the $F_{a-1,N-a}$ distribution and bounds $(\hat C - C)^2/((a - 1)\widehat{\operatorname{Var}}(\hat C))$ for every contrast simultaneously, so the intervals

$$
\hat C \pm \sqrt{(a - 1)F_{a-1,N-a,\alpha}}\sqrt{\mathrm{MS}_{\mathrm{E}}\sum_i\frac{c_i^2}{n_i}}
$$
cover all contrasts with probability $1 - \alpha$, and a false rejection of any true $C = 0$ has probability at most $\alpha$. $\square$

The proof establishes the exact relation between Scheffé's method and the ANOVA $F$-test. If the $F$-test does not reject, then $F_0(C) \le F_0 \le F_{a-1,N-a,\alpha}$ for every contrast, and no contrast is significant by Scheffé's method. If the $F$-test rejects, then the maximizing contrast $c_i \propto n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$ is significant; but this contrast may be one of no practical interest, and in particular no pairwise difference need be significant. Scheffé's method is in this sense "equivalent" to the $F$-test: the $F$-test rejects exactly when some contrast is Scheffé-significant. The method is valid for all possible contrasts of the means, and for that reason it is quite conservative for any small family.

For the etching data, $H_0\colon (\mu_1 + \mu_2)/2 = \mu_3$ has $\boldsymbol{c} = (0.5, 0.5, -1, 0)$:

```r
a <- 4; n1 <- n2 <- n3 <- n4 <- 5
N <- sum(n1 + n2 + n3 + n4)
df1 <- a - 1; df2 <- N - a
# Estimate
fit <- lm(rate ~ 0 + RF, data = etch.rate)
c <- c(0.5, 0.5, -1, 0)
est <- sum(c * coef(fit))
var <- sum(c^2 * diag(vcov(fit)))
F0 <- est^2 / var / (a - 1)
# p-value
1 - pf(F0, df1 = df1, df2 = df2)    # 0.00047
```

Here $\hat C = (551.2 + 587.4)/2 - 625.4 = -56.1$, $\widehat{\operatorname{Var}}(\hat C) = 333.7 \times 1.5/5 = 100.1$, $F_0(C) = 56.1^2/100.1/3 = 10.48$, and $p = \mathbb{P}(F_{3,16} > 10.48) = 0.00047$: the rate at $200\,\mathrm{W}$ exceeds the average of the two lower settings, even after accounting for all possible contrasts.

### 4.7.3. Scheffé's Theorem

The method extends to any linear model $\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, $\boldsymbol{\varepsilon} \sim \mathcal{N}_n(\boldsymbol{0}, \sigma^2I)$, with $X$ of rank $r$. A linear combination $\Psi = \boldsymbol{c}^{\mathsf T}\boldsymbol{\beta}$ is an **estimable function** if there is a $\boldsymbol{d}$ with $\mathbb{E}[\boldsymbol{d}^{\mathsf T}\boldsymbol{Y}] = \Psi$ for all $\boldsymbol{\beta}$; its least squares estimator $\hat\Psi = \boldsymbol{d}^{\mathsf T}\boldsymbol{y}$ (with $\boldsymbol{d}$ in the column space of $X$) has variance $\sigma^2\boldsymbol{d}^{\mathsf T}\boldsymbol{d}$, estimated by $\widehat{\operatorname{Var}}(\hat\Psi) = \hat\sigma^2\boldsymbol{d}^{\mathsf T}\boldsymbol{d}$. Contrasts in the effects model are estimable.

**Theorem 4.7.2 (Scheffé's Theorem)** Let $\mathcal{L}$ be a $q$-dimensional space of estimable functions. Then

$$
\hat\Psi \pm \sqrt{qF_{q,n-r,\alpha}}\sqrt{\widehat{\operatorname{Var}}(\hat\Psi)} = \hat\Psi \pm \hat\sigma\sqrt{qF_{q,n-r,\alpha}}\sqrt{\boldsymbol{d}^{\mathsf T}\boldsymbol{d}}
$$
are $100(1 - \alpha)\%$ simultaneous confidence intervals for all $\Psi \in \mathcal{L}$.

The proof is the Cauchy–Schwarz argument of Theorem 4.7.1 in a $q$-dimensional space. For the contrasts of a single-factor experiment $q = a - 1$ and $n - r = N - a$, and the theorem gives the intervals above. Another special case is familiar from regression: in $\boldsymbol{y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ with $X$ of size $n \times p$ and full rank, take $\Psi = \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$ for all $\boldsymbol{x} \in \mathbb{R}^p$, so $q = p$. Then $\boldsymbol{d} = X(X^{\mathsf T}X)^{-1}\boldsymbol{x}$, $\boldsymbol{d}^{\mathsf T}\boldsymbol{d} = \boldsymbol{x}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}$, and

$$
\boldsymbol{x}^{\mathsf T}\hat{\boldsymbol{\beta}} \pm \hat\sigma\sqrt{pF_{p,n-p,\alpha}}\sqrt{\boldsymbol{x}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}}
$$
is a simultaneous band for the whole regression surface. For simple linear regression $p = 2$, $\hat\mu_x = \boldsymbol{x}^{\mathsf T}\hat{\boldsymbol{\beta}}$ and $\operatorname{Var}(\hat\mu_x) = \sigma^2\bigl(\frac1n + \frac{(x - \bar X)^2}{\sum_i(X_i - \bar X)^2}\bigr)$, and the band is the Working–Hotelling **confidence band** $\hat\mu_x \pm W s(\hat\mu_x)$ with $W = \sqrt{2F_{2,n-2,\alpha}}$ of [3.3.4](/3.3.4).

## 4.8. Dunnett's Test: Comparisons with a Control

### 4.8.1. Several Treatments and One Control

The general methods of Tukey and Scheffé consider all pairwise comparisons, or all contrasts. Often, however, one level is a control (a standard treatment, a placebo, the current process setting), and the only comparisons of interest are those of each new treatment with the control. With $m = a - 1$ such comparisons instead of $\binom a2$, the general methods give unnecessarily wide intervals. Dunnett's test uses the joint distribution of exactly these $m$ comparisons.

As an example, four types of blankets $b_0$, $b_1$, $b_2$, $b_3$ were tested on surgical patients to assess their recovery times; $b_0$ is the standard blanket already in use in hospitals. Patients were allocated randomly to the four treatments, and the outcome is the recovery time in minutes. The data are the `recovery` data set of the R package `multcomp`:

```r
data("recovery", package = "multcomp")
summary(recovery)
```

```text
 blanket    minutes     
 b0:20   Min.   : 5.00  
 b1: 3   1st Qu.:12.00  
 b2: 3   Median :13.00  
 b3:15   Mean   :13.49  
         3rd Qu.:16.00  
         Max.   :19.00  
```

The group sizes differ considerably ($n_0 = 20$, $n_1 = n_2 = 3$, $n_3 = 15$, $N = 41$). Box plots show approximately normal observations with similar group variances, and blanket $b_2$ seems to reduce the mean recovery time compared with $b_0$. We want to make such a claim while controlling the FWER. The model is the unbalanced one-way layout $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$, $i = 0, 1, 2, 3$, $j = 1, \dots, n_i$, with independent $\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$, and the natural question is whether any of $b_1$, $b_2$, $b_3$ reduces the recovery time. This calls for three one-sided hypotheses,

$$
H_i\colon \mu_i \ge \mu_0 \quad\text{versus}\quad K_i\colon \mu_i < \mu_0,\qquad i = 1, 2, 3,
$$
not for the global hypothesis $\mu_0 = \mu_1 = \mu_2 = \mu_3$ of ANOVA. Rejecting any $H_i$ shows, at the family-wise level $\alpha$, that at least one new blanket is better than the standard. This many-to-one problem was solved by Dunnett (1955).

### 4.8.2. The Test Statistic and Its Distribution

Let group $0$ be the control and $1, \dots, m$ the treatments. The comparisons are based on the $m$ pairwise $t$-statistics

$$
t_i = \frac{\bar y_i - \bar y_0}{s\sqrt{\frac{1}{n_i} + \frac{1}{n_0}}},\qquad i = 1, \dots, m,\qquad s^2 = \frac{1}{\nu}\sum_{i=0}^m\sum_{j=1}^{n_i}(y_{ij} - \bar y_i)^2,\quad \nu = N - (m + 1).
$$
Each $t_i$ has a $t_\nu$ distribution when $\mu_i = \mu_0$, but they are dependent: they share $s$, and every difference contains $\bar y_0$. Since $\operatorname{Cov}(\bar y_i - \bar y_0, \bar y_j - \bar y_0) = \operatorname{Var}(\bar y_0) = \sigma^2/n_0$ for $i \ne j$,

$$
\operatorname{Corr}(\bar y_i - \bar y_0, \bar y_j - \bar y_0) = \frac{1/n_0}{\sqrt{\bigl(\frac{1}{n_i} + \frac{1}{n_0}\bigr)\bigl(\frac{1}{n_j} + \frac{1}{n_0}\bigr)}} = \sqrt{\frac{n_i}{n_i + n_0}}\sqrt{\frac{n_j}{n_j + n_0}} = \rho_{ij}.
$$
In the balanced case $n_0 = n_1 = \cdots = n_m$, $\rho_{ij} = 0.5$ for all $i \ne j$.

**Definition 4.8.1 (Multivariate t-Distribution)** Let $\boldsymbol{Z} \sim \mathcal{N}_m(\boldsymbol{0}, R)$, where $R$ is a correlation matrix, and $V \sim \chi^2_\nu$ independent of $\boldsymbol{Z}$. The distribution of $\boldsymbol{T} = \boldsymbol{Z}/\sqrt{V/\nu}$ is the $m$-variate **multivariate t-distribution** with $\nu$ degrees of freedom and correlation matrix $R$.

Under $\mu_0 = \mu_1 = \cdots = \mu_m$, the vector $\boldsymbol{t} = (t_1, \dots, t_m)$ has the $m$-variate $t$-distribution with $\nu$ degrees of freedom and correlation matrix $R = (\rho_{ij})$: each coordinate is a standardized normal difference divided by the common $s/\sigma$, and $\nu s^2/\sigma^2 \sim \chi^2_\nu$ independently.

**Definition 4.8.2 (Dunnett's Test)** **Dunnett's test** compares $m$ treatments with a control through the joint distribution of $t_1, \dots, t_m$: for the one-sided alternatives $\mu_i < \mu_0$, the adjusted $p$-value of the $i$-th comparison is

$$
p_i = \mathbb{P}\Bigl(\min_{k=1,\dots,m}T_k \le t_i\Bigr),
$$
and for two-sided alternatives $p_i = \mathbb{P}\bigl(\max_k\lvert T_k\rvert \ge \lvert t_i\rvert\bigr)$, where $\boldsymbol{T}$ has the multivariate $t$-distribution above. Equivalently, $H_i$ is rejected when $t_i < -d_{m,\nu,\alpha}$ (one-sided) or $\lvert t_i\rvert > \lvert d\rvert_{m,\nu,\alpha}$ (two-sided), where the critical values satisfy $\mathbb{P}(\min_kT_k > -d_{m,\nu,\alpha}) = 1 - \alpha$ and $\mathbb{P}(\max_k\lvert T_k\rvert \le \lvert d\rvert_{m,\nu,\alpha}) = 1 - \alpha$.

In essence, the one-sided Dunnett test takes the minimum (or the maximum, depending on the direction of the alternative) of the $m$ pairwise $t$-tests and refers it to its exact null distribution; this controls the FWER at level $\alpha$ exactly, by the same argument as Tukey's test with the range replaced by the minimum. By the symmetry of the multivariate $t$-distribution, $\mathbb{P}(\min_iT_i \le t) = 1 - \mathbb{P}(T_1 > t, \dots, T_m > t) = 1 - \mathbb{P}(T_1 < -t, \dots, T_m < -t)$, one minus a multivariate $t$ distribution function, which is computed numerically, for example by `1 - mnormt::pmt(rep(-t, m), mean = rep(0, m), S = R, df = nu)`.

### 4.8.3. The multcomp Package

The package `multcomp` performs Dunnett's test, and many other simultaneous tests, through the function `glht` (general linear hypotheses). Fit the ANOVA model with `aov`, then specify the comparisons:

```r
mod <- aov(minutes ~ blanket, data = recovery)
library("multcomp")
mc <- glht(mod,
           linfct = mcp(blanket = "Dunnett"),
           alternative = "less")
summary(mc)
summary(mc, test = adjusted(type = "bonferroni"))
```

`mcp(blanket = "Dunnett")` defines the contrast matrix

$$
C = \begin{bmatrix} -1 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ -1 & 0 & 0 & 1 \end{bmatrix}
$$
acting on $(\mu_0, \mu_1, \mu_2, \mu_3)$, whose estimates have covariance matrix $C\operatorname{diag}(\sigma^2/n_0, \dots, \sigma^2/n_3)C^{\mathsf T}$, the source of the correlations $\rho_{ij}$. The two summaries are:

```text
	 Simultaneous Tests for General Linear Hypotheses

Multiple Comparisons of Means: Dunnett Contrasts

Fit: aov(formula = minutes ~ blanket, data = recovery)

Linear Hypotheses:
             Estimate Std. Error t value  Pr(<t)    
b1 - b0 >= 0  -2.1333     1.6038  -1.330  0.2411    
b2 - b0 >= 0  -7.4667     1.6038  -4.656  <0.001 ***
b3 - b0 >= 0  -1.6667     0.8848  -1.884  0.0925 .  
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
(Adjusted p values reported -- single-step method)
```

```text
	 Simultaneous Tests for General Linear Hypotheses

Multiple Comparisons of Means: Dunnett Contrasts

Fit: aov(formula = minutes ~ blanket, data = recovery)

Linear Hypotheses:
             Estimate Std. Error t value  Pr(<t)    
b1 - b0 >= 0  -2.1333     1.6038  -1.330   0.287    
b2 - b0 >= 0  -7.4667     1.6038  -4.656 6.1e-05 ***
b3 - b0 >= 0  -1.6667     0.8848  -1.884   0.101    
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
(Adjusted p values reported -- bonferroni method)
```

Each line states the null hypothesis (`b1 - b0 >= 0`, that is, $\mu_1 \ge \mu_0$), the estimate $\bar y_i - \bar y_0$, its standard error $s\sqrt{1/n_i + 1/n_0}$ with $s = 2.59$ and $\nu = 41 - 4 = 37$ (for $b_1$: $2.59\sqrt{1/3 + 1/20} = 1.604$), and $t_i$. The single-step $p$-values are the Dunnett probabilities $\mathbb{P}(\min_kT_k \le t_i)$ under the correlation matrix with $\rho_{12} = 0.13$, $\rho_{13} = \rho_{23} = 0.24$. The Bonferroni $p$-values are $3\,\mathbb{P}(t_{37} \le t_i)$, computed in R as `pt(c(-1.330, -4.656, -1.884), df = nu) * 3`. They are uniformly larger ($0.287$ against $0.241$, $0.101$ against $0.0925$), because Bonferroni ignores the positive correlation of the three comparisons. Only blanket $b_2$ reduces the mean recovery time significantly.

Simultaneous confidence intervals are obtained with `confint`:

```r
ci <- confint(mc, level = 0.95)
plot(ci, xlab = "Minutes")
```

```text
	 Simultaneous Confidence Intervals

Multiple Comparisons of Means: Dunnett Contrasts

Fit: aov(formula = minutes ~ blanket, data = recovery)

Quantile = 2.1829
95% family-wise confidence level
 

Linear Hypotheses:
             Estimate lwr     upr    
b1 - b0 >= 0 -2.1333     -Inf  1.3676
b2 - b0 >= 0 -7.4667     -Inf -3.9657
b3 - b0 >= 0 -1.6667     -Inf  0.2647
```

`Quantile = 2.1829` is the one-sided Dunnett critical value $d_{3,37,0.05}$, the $0.95$ quantile of $\max_k(-T_k)$, computed by `mvtnorm::qmvt(p = .95, tail = "lower.tail", corr = R, df = nu)`. The upper limits are estimate $+\,2.1829 \times$ standard error, for example $-7.4667 + 2.1829 \times 1.6038 = -3.966$. With 95% family-wise confidence, blanket $b_2$ shortens the mean recovery time by at least $3.97$ minutes, about $4$; the intervals for $b_1$ and $b_3$ contain $0$.

## 4.9. Comparing and Choosing the Methods

### 4.9.1. Critical Values and Power

For the pairwise comparisons $H_0\colon \mu_i = \mu_j$ in a balanced experiment, every method computes the same statistic $t_0 = (\bar y_{i\cdot} - \bar y_{j\cdot})/\sqrt{2\mathrm{MS}_{\mathrm{E}}/n}$ and differs only in the critical value $c$ it is compared with:

| Method | Statistic | Rejection region | Error rate controlled | Family |
|---|---|---|---|---|
| Fisher's LSD | $t_0$ | $\lvert t_0\rvert > t_{N-a,\alpha/2}$ | comparisonwise only | — |
| Benjamini–Hochberg | $p$-values of $t_0$ | step-up rule, Algorithm 4.4.1 | FDR | any $m$ tests |
| Bonferroni | $t_0$ | $\lvert t_0\rvert > t_{N-a,\alpha/(2m)}$ | FWER | any $m$ comparisons |
| Tukey (HSD) | $q_0 = \sqrt2\lvert t_0\rvert$ | $q_0 > q_{a,N-a,\alpha}$ | FWER, exact | all $\binom a2$ pairs |
| Scheffé | $F_0 = t_0^2/(a - 1)$ | $F_0 > F_{a-1,N-a,\alpha}$ | FWER | all contrasts |
| Dunnett | $t_i$ vs control | $\lvert t_i\rvert > \lvert d\rvert_{a-1,N-a,\alpha}$ | FWER, exact | $a - 1$ comparisons with a control |

On the scale of $\lvert t_0\rvert$ the critical values are $t_{N-a,\alpha/2}$, $t_{N-a,\alpha/(2m)}$, $q_{a,N-a,\alpha}/\sqrt2$ and $\sqrt{(a - 1)F_{a-1,N-a,\alpha}}$. For the etching experiment, $a = 4$ and $N - a = 16$:

| Method | Critical value for $\lvert t_0\rvert$ | Least significant difference $c\sqrt{2\mathrm{MS}_{\mathrm{E}}/n}$ |
|---|---|---|
| LSD | $t_{16,0.025} = 2.120$ | 24.5 |
| Dunnett (two-sided, 3 comparisons) | $2.593$ | 30.0 |
| Tukey | $q_{4,16,0.05}/\sqrt2 = 4.046/\sqrt2 = 2.861$ | 33.1 |
| Bonferroni ($m = 6$) | $t_{16,0.05/12} = 3.008$ | 34.8 |
| Scheffé | $\sqrt{3F_{3,16,0.05}} = \sqrt{3 \times 3.239} = 3.117$ | 36.0 |

A smaller critical value means more rejections and more power. For all pairwise comparisons the order is LSD (no adjustment, highest power), then Tukey (exact FWER control for this family), then Bonferroni (valid but conservative, since it ignores the correlations), then Scheffé (protects an infinite family it does not need here). The order of Tukey and Bonferroni holds for every $a \ge 3$; for $a = 2$ all four coincide with the $t$-test. Dunnett's critical value is below Tukey's because it protects only $a - 1$ comparisons.

![Critical values on the |t| scale for all pairwise comparisons at alpha = 0.05 with 16 error degrees of freedom, as functions of the number of levels a: LSD, Tukey, Bonferroni and Scheffe.](./plots/critical-values.py)

### 4.9.2. Which Method When

The choice depends on the family of comparisons, which should be decided before looking at the data.

- Only one comparison, or a preliminary screening experiment: Fisher's LSD, which always uses the same measuring stick, the unadjusted $t$-test. It is not really a multiple comparison procedure.
- A few planned comparisons or contrasts: Bonferroni, slightly conservative but valid for any family of fixed size.
- All pairwise comparisons, and nothing else: Tukey's HSD (Tukey–Kramer if unbalanced).
- Comparisons not specified in advance, of any kind, including contrasts suggested by the data: Scheffé, which protects against all of them.
- Several treatments compared with a control: Dunnett.
- Many hypotheses in a screening study, where a controlled proportion of false discoveries is acceptable: Benjamini–Hochberg.

The R functions are:

```r
aov(y ~ treatment, data = dataframe)                        # the ANOVA fit
pairwise.t.test(y, treatment, p.adjust.method = "none")      # Fisher's LSD
pairwise.t.test(y, treatment, p.adjust.method = "bonferroni")
pairwise.t.test(y, treatment, p.adjust.method = "BH")        # "BH", also called "fdr"
TukeyHSD(aov(y ~ treatment, data = dataframe))
library(agricolae)
LSD.test(fit, "treatment", group = FALSE, console = TRUE)    # fit: an lm or aov model
scheffe.test(fit, "treatment", group = FALSE, console = TRUE)
library(multcomp)
summary(glht(fit, linfct = mcp(treatment = "Dunnett")))
```

`pairwise.t.test` is used instead of repeated calls of `t.test` because it computes every comparison with the pooled standard deviation $\sqrt{\mathrm{MS}_{\mathrm{E}}}$ and $N - a$ degrees of freedom, as the LSD requires; `t.test` would use only the two groups compared.

### 4.9.3. Reading Software Output

Software output often does not say in words which adjustment was made, but the numbers do. Compare the adjusted $p$-values with the unadjusted ones for the same data.

- If every adjusted value is $m$ times the unadjusted one (capped at $1$), the method is Bonferroni: for the etching data $0.0064 \to 0.038$, $0.0046 \to 0.028$, a ratio of $6$.
- If the ratio is $m/k$ for the $k$-th smallest $p$-value (with ties resolved by taking running minima from the top), it is Benjamini–Hochberg: the largest $p$-value is unchanged ($0.0064$), the second largest is multiplied by $6/5$ ($0.0046 \to 0.0055$).
- If the adjusted values are smaller than Bonferroni's but larger than the raw ones, with no constant ratio, and the output reports intervals for all pairs with a common half-width, the method is Tukey: $0.0064 \to 0.029$, $8.4\times10^{-6} \to 4.5\times10^{-5}$.
- If only the comparisons with one level appear, possibly with one-sided hypotheses and a "single-step" multivariate $t$ adjustment, it is Dunnett.

Finally, the conclusions of pairwise comparisons are not transitive. If $A$ and $B$ do not differ significantly, and $B$ and $C$ do not differ significantly, nothing follows about $A$ and $C$: "not significant" means that the data cannot distinguish the means, not that they are equal, and the two small differences can add up to a significant one.

## Summary

| Method | Critical value for $\lvert t_0\rvert$ ($a = 4$, $\nu = 16$) | Controls | Power for pairs | Use when |
|---|---|---|---|---|
| LSD (Definition 4.3.1) | $t_{\nu,\alpha/2}$ (2.120) | comparisonwise rate only; neither FWER nor FDR | highest | one planned comparison, screening |
| BH (Algorithm 4.4.1) | data-dependent, between $\alpha/m$ and $\alpha$ on the $p$ scale | FDR $= m_0\alpha/m$ (Theorem 4.4.1) | high | many tests, discoveries followed up |
| Bonferroni | $t_{\nu,\alpha/(2m)}$ (3.008) | FWER, any dependence | lower | a few planned comparisons |
| Tukey (Theorem 4.6.1) | $q_{a,\nu,\alpha}/\sqrt2$ (2.861) | FWER, exact for all pairs | second after LSD | all pairwise comparisons |
| Tukey–Kramer (Definition 4.6.2) | same, with $\sqrt{1/n_i + 1/n_j}$ | FWER, conservative | | all pairs, unbalanced |
| Scheffé (Theorem 4.7.1) | $\sqrt{(a - 1)F_{a-1,\nu,\alpha}}$ (3.117) | FWER for all contrasts | lowest for pairs | unplanned contrasts |
| Dunnett (Definition 4.8.2) | $\lvert d\rvert_{a-1,\nu,\alpha}$ (2.593) | FWER, exact for comparisons with control | high for its family | treatments vs a control |

- $\mathrm{FDR} \le \mathrm{FWER}$, with equality under the global null hypothesis (Proposition 4.2.1); FWER control is stricter, FDR control more powerful when many hypotheses are false.
- The LSD uses $\mathrm{MS}_{\mathrm{E}}$ and $N - a$ degrees of freedom, unlike the two-sample $t$-test, and it is the general linear test of $\mu_i = \mu_j$.
- Tukey's $p$-value is $\mathbb{P}(Q_{a,N-a} \ge \sqrt2\lvert t_{ij}\rvert)$; for two means $q = \sqrt2\lvert t\rvert$.
- Scheffé and ANOVA: $\sup_CF_0(C) = F_0$, so the $F$-test rejects if and only if some contrast is Scheffé-significant, which need not be a pairwise difference. Scheffé's theorem (Theorem 4.7.2) also yields the Working–Hotelling band.
- Bonferroni-adjusted $p$-values are $m$ times the raw ones; BH-adjusted are $m/k$ times; Tukey's lie between the raw and Bonferroni values.

## Questions

1. Twenty independent tests are carried out, each at level $0.05$, and all null hypotheses are true. What is the probability of at least one type I error? Which per-test level keeps the FWER at $0.05$, by Bonferroni and exactly?

   **Answer** $1 - 0.95^{20} = 0.64$. Bonferroni uses $0.05/20 = 0.0025$, giving FWER $1 - 0.9975^{20} = 0.0488$; the exact level for independent tests solves $1 - (1 - x)^{20} = 0.05$, $x = 1 - 0.95^{1/20} = 0.00256$ (Šidák).

2. Is it more stringent to control the FDR or the FWER at the same level $\alpha$? Under what condition do the two coincide?

   **Answer** Controlling the FWER. Since $V/\max(R, 1) \le \boldsymbol{1}_{\{V \ge 1\}}$, $\mathrm{FDR} \le \mathrm{FWER}$ for every procedure, so FWER $\le \alpha$ implies FDR $\le \alpha$ but not conversely. They coincide when all null hypotheses are true, because then $V = R$.

3. For the etching data, compare the two-sample $t$-test and the LSD test of $\mu_{160} = \mu_{180}$. The two groups have $s_1 = 20.02$ and $s_2 = 16.74$.

   **Answer** Two-sample: $s_p^2 = (20.02^2 + 16.74^2)/2 = 340.5$, $t_0 = 36.2/\sqrt{340.5 \times 2/5} = 3.10$ on $8$ degrees of freedom, $p = 0.015$. LSD: $\mathrm{MS}_{\mathrm{E}} = 333.7$ pools all four groups, $t_0 = 36.2/11.55 = 3.13$ on $16$ degrees of freedom, $p = 0.0064$. The statistics are similar because $s_p^2 \approx \mathrm{MS}_{\mathrm{E}}$; the main gain is in the degrees of freedom ($t_{16,0.025} = 2.120$ against $t_{8,0.025} = 2.306$). Neither adjusts for multiplicity.

4. In a balanced experiment with $a = 4$ levels and $N - a = 16$, the LSD statistic of one pair is $t_{ij} = 3.133$. Compute the unadjusted, the Bonferroni and the Tukey $p$-values.

   **Answer** Unadjusted: $2\mathbb{P}(t_{16} \ge 3.133) = 0.0064$. Bonferroni: $6 \times 0.0064 = 0.038$. Tukey: $q_0 = \sqrt2 \times 3.133 = 4.431$ and $\mathbb{P}(Q_{4,16} \ge 4.431) = 0.029$ (R: `ptukey(4.431, 4, 16, lower.tail = FALSE)`). These are the $180$ versus $160\,\mathrm{W}$ values of the outputs in this chapter.

5. Three drugs were each given to $7$ patients; the means are $5.54$, $5.03$, $5.93$ and $\mathrm{MS}_{\mathrm{E}} = 0.25$ on $18$ degrees of freedom. Using only these summary statistics, carry out all pairwise comparisons by the LSD, Bonferroni, Tukey and Scheffé methods at $\alpha = 0.05$.

   **Answer** The standard error of a difference is $\sqrt{0.25 \times 2/7} = 0.267$. Critical values for $\lvert t_0\rvert$: LSD $t_{18,0.025} = 2.101$; Bonferroni $t_{18,0.05/6} = 2.639$; Tukey $q_{3,18,0.05}/\sqrt2 = 3.609/\sqrt2 = 2.552$; Scheffé $\sqrt{2F_{2,18,0.05}} = \sqrt{2 \times 3.555} = 2.666$. The least significant differences are $0.561$, $0.705$, $0.682$ and $0.713$. The observed differences are $\lvert\bar y_1 - \bar y_2\rvert = 0.51$, $\lvert\bar y_1 - \bar y_3\rvert = 0.39$, $\lvert\bar y_2 - \bar y_3\rvert = 0.90$. All four methods find only drug 3 better than drug 2; drug 1 cannot be distinguished from either. Raw data are not needed: every method uses only the means, the $n_i$ and $\mathrm{MS}_{\mathrm{E}}$.

6. Soil–water fluxes were measured for three grades of soil: grade 1: $-1.184$, $-1.103$, $-0.8278$; grade 2: $-0.2395$, $-0.1065$, $0.24059$, $0.35347$; grade 3: $0.49103$, $0.51998$, $1.6347$. Why does Tukey's HSD in its original form not apply, and what does the Tukey–Kramer method conclude?

   **Answer** The sample sizes ($3, 4, 3$) are unequal, so the means have different variances and the range of the means is not studentized range distributed. The means are $-1.038$, $0.062$, $0.882$; $\mathrm{SS}_{\mathrm{E}} = 1.156$ on $7$ degrees of freedom, $\mathrm{MS}_{\mathrm{E}} = 0.165$ (the ANOVA gives $F_0 = 16.9$, $p = 0.002$). With $q_{3,7,0.05}/\sqrt2 = 4.165/\sqrt2 = 2.945$, the Tukey–Kramer intervals are: grade 2 − grade 1: $1.100 \pm 2.945 \times 0.310 = [0.19, 2.01]$; grade 3 − grade 1: $1.920 \pm 2.945 \times 0.332 = [0.94, 2.90]$; grade 3 − grade 2: $0.820 \pm 2.945 \times 0.310 = [-0.09, 1.73]$. Grade 1 differs from both other grades; grades 2 and 3 cannot be distinguished. (Grade 3 also has a much larger spread than grade 1, $s = 0.65$ against $0.19$, so the common-variance assumption deserves a check.)

7. In the etching experiment, $160\,\mathrm{W}$ is the power currently in use. Which method should be used to decide whether the three new settings change the etch rate, and what is the conclusion?

   **Answer** Dunnett's test with $160\,\mathrm{W}$ as the control, two-sided since the direction of a change is not specified: $m = 3$, $\nu = 16$, balanced so $\rho_{ij} = 0.5$, and $\lvert d\rvert_{3,16,0.05} = 2.593$. The critical difference is $2.593 \times 11.55 = 30.0$, and the differences from the control are $36.2$, $74.2$ and $155.8$, all larger: each new setting changes the mean etch rate (all increase it). Tukey's or Scheffé's critical differences ($33.1$, $36.0$) would be larger, because they protect families the question does not need.

8. Apply the Benjamini–Hochberg procedure at $\alpha = 0.05$ to the six $p$-values $0.001$, $0.008$, $0.039$, $0.041$, $0.042$, $0.60$, and compare with Bonferroni.

   **Answer** The thresholds $\frac i6 \times 0.05$ are $0.0083$, $0.0167$, $0.025$, $0.0333$, $0.0417$, $0.05$. Going down from the largest: $0.60 > 0.05$, $0.042 > 0.0417$, $0.041 > 0.0333$, $0.039 > 0.025$, $0.008 \le 0.0167$; so $i_0 = 2$ and the first two hypotheses are rejected. Bonferroni compares every $p$-value with $0.05/6 = 0.0083$ and rejects both $0.001$ and $0.008$ as well; here the two agree, although the three $p$-values near $0.04$ come close to the BH line.

9. The overall ANOVA $F$-test of an experiment is not significant at level $\alpha$. Can Scheffé's method find a significant contrast? If the $F$-test is significant, must Scheffé's method find a significant pairwise difference?

   **Answer** No, and no. Every contrast satisfies $F_0(C) \le F_0$ (Theorem 4.7.1), so if $F_0 \le F_{a-1,N-a,\alpha}$ no contrast exceeds the Scheffé critical value. If $F_0$ is significant, the contrast with $c_i \propto n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})$ is Scheffé-significant, but a pairwise difference is a particular contrast with $F_0(C)$ possibly well below $F_0$, so it need not be significant.
