---
title: Basic Principles and Simple Comparative Experiments
description: The basic principles of experimental design (randomization, replication, blocking, representativeness) with examples of their violation; comparative experiments and how they differ from surveys; tests for one and two normal populations, pooled and Welch t-tests, paired versus unpaired analyses and the bias of the pooled variance under pairing; the advantages of balanced designs; power, sample size and R's power.t.test; and the critique of a real comparative experiment.
---

According to Fisher, a good experimental design does two things: it makes the experiment efficient, and it reduces the experimental error, the variation in the responses caused by factors other than the treatments. This chapter has two themes. The first is the set of basic principles by which designs achieve this: randomization, replication and blocking, together with the representativeness of the experimental material. The second is the simplest experiment to which they apply, the comparison of two treatments. The statistical tools for that comparison, the $Z$- and $t$-tests for one and two normal populations, were developed in [3.2.5](/3.2.5); here we collect them from the point of view of design. The questions are now which analysis the design calls for (paired or unpaired, equal or unequal variances), why equal sample sizes are preferable, and how large the experiment must be. The comparison of more than two treatments, the analysis of variance, follows in [3.8.3](/3.8.3).

## 2.1. The Basic Principles of Experimental Design

### 2.1.1. Sources of Experimental Error

The **experimental error** of an experiment ([3.8.1](/3.8.1)) has three typical sources:

- the inherent variability of the experimental material to which the treatments are applied (plots of land, animals, batches of raw material);
- a lack of uniformity in the way the experiment is conducted (different operators, instruments, days);
- a lack of representativeness of the sample of units for the population under study.

The principles below deal with these sources in different ways. Randomization does not reduce the error but makes sure that it does not bias the comparison; replication makes it possible to measure the error and to average it down; blocking removes a known source of it from the comparison; representativeness determines to which population the conclusions apply.

### 2.1.2. Randomization

Suppose that three two-level factors $A$, $B$, $C$ are studied in the eight runs of a $2^3$ factorial design, and that two operators share the work: Peter makes the four runs with $A$ low and John the four runs with $A$ high.

| Run | $A$ | $B$ | $C$ | Operator |
|:-:|:-:|:-:|:-:|:-:|
| 1 | low | low | low | Peter |
| 2 | low | low | high | Peter |
| 3 | low | high | low | Peter |
| 4 | low | high | high | Peter |
| 5 | high | low | low | John |
| 6 | high | low | high | John |
| 7 | high | high | low | John |
| 8 | high | high | high | John |

If the responses at the high level of $A$ are larger, we cannot tell whether this is the effect of $A$ or of John: the two effects are inseparable.

**Definition 2.1.1 (Confounding)** Two factors (or a factor and another variable) are subject to **confounding**, or are confounded, when their effects on the response cannot be separated, because in the data the levels of one change together with the levels of the other. A variable that is not included in the design or the analysis but affects the response, and may be associated with the factors, is a **lurking variable**.

Operators, the order of the runs, the day, the position in an oven, the batch of raw material: an experiment is full of variables that might matter and that nobody plans to study. Some are known and can be measured or controlled, many are not. The protection against all of them at once is to let chance decide.

**Definition 2.1.2 (Randomization)** **Randomization** is the use of a chance mechanism (such as a random number generator) to allocate the treatments to the experimental units and to determine the order in which the individual runs are made, in such a way that every possible allotment of the treatments has the same probability.

Randomization has three advantages.

1. It protects against lurking variables. A lurking variable cannot be systematically associated with a treatment chosen by a random mechanism; its effect is spread over all treatments and becomes part of the experimental error, where it is averaged out.
2. It removes the influence of subjective bias in the assignment of treatments. An experimenter who chooses the units for the new treatment, however honest, may unconsciously choose the more promising ones.
3. It ensures the validity of statistical inference. The probability statements of a test (its level, its $p$-value) assume that the errors behave like independent random variables; randomization is what makes this assumption reasonable. In Fisher's words, the purpose of randomization is to guarantee the validity of the test of significance, which is based on an estimate of error made possible by replication.

Randomization is used for uncontrollable, unknown or unmeasurable factors; factors that are known and controllable are better handled by blocking (Section 2.1.4) or by holding them constant.

**Example 2.1.1** In 2004, Conrads and coauthors processed over $200$ serum samples by mass spectrometry and reported that a pattern of serum proteins, evaluated on part of these samples, identified ovarian cancer with $100\%$ sensitivity ($65$ of $65$ cancers) and $100\%$ specificity ($43$ of $43$ controls), concluding that the method was ready for a large clinical study. Their own scatter plots of the total intensity of the spectra against the sample number tell a different story: the quality of the measurements deteriorated steadily as the runs went on, and the cancer samples had been run mainly on the first day while the controls were run on the following days. In a setting where something was clearly changing over time, the order of the runs was confounded with the disease status. A classifier that separates the groups perfectly may then be detecting the day of measurement rather than the cancer. Randomizing the run order (or running cancers and controls alternately within each day) would have made this impossible. The figure below simulates the situation: a measurement with no difference at all between cancers and controls, but with a drift over the run order, gives a highly significant "difference" when the cancers are run first and none when the order is randomized.

![Simulated serum measurements against run order with a downward drift and no true group difference: left, cancers run first and controls afterward, the cancer group appears higher with a very small p-value; right, the same samples in random order, the groups overlap and the difference is not significant](./plots/randomization_drift.py)

### 2.1.3. Replication

**Definition 2.1.3 (Replication and Repetition)** **Replication** means an independent repeat run of each treatment (treatment combination): each replicate applies the treatment to a different experimental unit and goes through the whole procedure again. **Repetition** means repeated measurements on the same experimental unit, or repeated runs in which only the measurement step is repeated.

Two replications of a treatment involve two experimental units. If a fertilizer is applied to three similar fields and the yield of each is recorded, the three responses are replicates; if it is applied to one field whose yield is measured three times, the three responses are repetitions. Repetition shows how precise the measurement process is (how close the results are to each other); only replication shows how much the response varies from unit to unit, which is the variation against which treatment differences must be judged.

Replication has three purposes:

1. it makes it possible to estimate the experimental error, by the sample standard deviation of the replicates; without this estimate no test or confidence interval is possible;
2. it reduces the variance of the estimates: a treatment mean based on $n$ replicates has variance $\sigma^2/n$;
3. it increases the power to detect a real difference between treatments.

Replication also ensures that the results are generally true and not just a product of the special circumstances of one particular run. When the treatments are levels of a quantitative factor and a regression model is fitted, replicates at the same level allow the residual sum of squares to be split as

$$
\mathrm{SSE}=\mathrm{SSPE}+\mathrm{SSLF},
$$

into a **pure error sum of squares**, which measures the experimental error and does not depend on the model, and a **lack-of-fit sum of squares**, which measures how far the level means are from the fitted model ([3.3.6](/3.3.6)). This is the formal version of the distinction between experimental error and lack-of-fit error made in [3.8.1](/3.8.1).

### 2.1.4. Blocking

Some sources of variation are known in advance and can be controlled, even though they are of no interest in themselves: batches of raw material, days of the week, operators, machines.

**Definition 2.1.4 (Nuisance Factor, Block and Blocking)** A **nuisance factor** is a factor that probably affects the response but is not of interest in the experiment. A **block** is a collection of experimental units that are relatively homogeneous, typically the units sharing one level of a nuisance factor. **Blocking** (local control, error control) is the technique of dividing the experimental units into blocks and running and comparing the treatments within each block, so that the variation between blocks is removed from the treatment comparisons.

Each level of the nuisance factor becomes a block, and the design is divided into groups of runs made within the blocks. Blocking reduces the extraneous error and therefore increases the efficiency of the design. It is effective when the variation between blocks is larger than the variation within blocks; blocking a factor that does not matter only costs degrees of freedom. The principles combine in the rule

> Block what you can, and randomize what you cannot.

Known nuisance factors are blocked, and within each block the treatments are randomized to protect against the unknown ones. Local control in the broad sense also includes balancing and the grouping of units. It should not be confused with a control in the sense of a control group, a treatment that receives no active treatment and serves as a baseline for the others. The paired design of Section 2.3.3 is the simplest blocked design; the randomized complete block design and its relatives are treated in later chapters of this course.

### 2.1.5. Representativeness

The fourth principle concerns the experimental material: each treatment should be applied to units that are representative of the population to which the conclusions are meant to apply. An experiment on healthy young men says little about elderly women, and a laboratory process that works on pure reagents may fail on industrial raw material. Representativeness, randomization, replication and blocking together are the principles of design:

| Principle | Purpose | How | Consequence of violating it |
|---|---|---|---|
| Representativeness | conclusions apply to the population of interest | choose units like those about which inferences are made | correct conclusions about the wrong population |
| Randomization | protection against unanticipated factors and subjective bias; valid inference | random allocation of treatments and random run order | confounding with lurking variables (operator, run order) |
| Replication | estimate of the error; precision; power | independent repeat runs on different units | no error estimate, or a too small one from repetitions |
| Blocking | remove known nuisance variation so that treatment effects stand out | compare treatments within homogeneous blocks | treatment differences hidden in large error |

## 2.2. Comparative Experiments

**Definition 2.2.1 (Comparative Experiment)** An experiment is a **comparative experiment** when its object is the comparison of treatments rather than the determination of absolute values. Such an experiment has a number of experimental units and a number of alternative treatments; one treatment is applied to each unit and one or more observations are made, and the assignment of treatments to units is under the experimenter's control. A comparative experiment with two treatments (two levels of a single factor) is a **simple comparative experiment**.

In an agricultural trial of crop varieties, for example, the aim is to compare the varieties, not to determine the absolute yield per acre that a variety will give under given conditions; the comparison is much more stable from season to season than the absolute values. A/B testing of two versions of a web page is a simple comparative experiment in this sense: the version shown to each user is assigned at random.

The last condition of the definition separates experiments from surveys. Suppose we want to know whether secondary school students in a region play computer games frequently or not, or whether students in region $A$ play more often than those in region $B$. Both studies compare something, but neither is a comparative experiment: the "treatments" (the region) are not assigned to the units by the investigator, and the students are only observed. These are planned surveys, that is, observational studies, and their comparisons are descriptive, not causal.

What can be compared depends on the type of data. Qualitative data are placed in categories (nominal or ordinal); quantitative data are measured and are discrete or continuous.

| Type of data | What can be compared | Example |
|---|---|---|
| discrete (counts, categories) | proportions | Is the percentage of on-time deliveries the same for suppliers A and B? |
| continuous | means | Is the average production volume the same for all three shifts? |
| continuous | variation | Do the results of the group using the new method vary less than those using the old method? |
| continuous | shapes of distributions | How does the distribution of cycle time differ between methods? |

## 2.3. Tests for Normal Populations

This section collects the standard tests; their derivations, power functions and optimality are in [3.2.5](/3.2.5). Throughout, $z_\alpha$, $t_{\nu,\alpha}$, $\chi^2_{\nu,\alpha}$ and $F_{\nu_1,\nu_2,\alpha}$ denote upper $\alpha$ quantiles, so that for example $\mathbb{P}(T>t_{\nu,\alpha})=\alpha$ for $T\sim t_\nu$.

### 2.3.1. One Population

Let $X_1,\dots,X_n$ be a random sample from $\mathcal{N}(\mu,\sigma^2)$, with sample mean $\bar X$ and sample variance $s^2=\sum(X_i-\bar X)^2/(n-1)$. For $H_0\colon\mu=\mu_0$ the test statistic is

$$
Z_0=\frac{\bar X-\mu_0}{\sigma/\sqrt n}\ \ (\sigma \text{ known}),\qquad t_0=\frac{\bar X-\mu_0}{s/\sqrt n}\ \ (\sigma \text{ unknown}),
$$

with $Z_0\sim\mathcal{N}(0,1)$ and $t_0\sim t_{n-1}$ under $H_0$. The rejection regions are:

| Alternative | **Z-test** | **t-test** |
|---|---|---|
| $H_1\colon\mu\ne\mu_0$ | $\lvert Z_0\rvert>z_{\alpha/2}$ | $\lvert t_0\rvert>t_{n-1,\alpha/2}$ |
| $H_1\colon\mu<\mu_0$ | $Z_0<-z_\alpha$ | $t_0<-t_{n-1,\alpha}$ |
| $H_1\colon\mu>\mu_0$ | $Z_0>z_\alpha$ | $t_0>t_{n-1,\alpha}$ |

The $100(1-\alpha)\%$ **confidence interval** for $\mu$ is $\bar X\pm t_{n-1,\alpha/2}\,s/\sqrt n$. Every $t$-statistic has the same structure, an estimate minus its hypothesized value divided by the **standard error** of the estimate. The test of zero slope in simple linear regression ([3.3.3](/3.3.3)) is $t_0=b_1/s(b_1)$ with $s(b_1)=s/\sqrt{S_{XX}}$ and $n-2$ degrees of freedom; the statistic $(b_1-\beta_1)/s(b_1)$ is its pivotal form, used for confidence intervals.

For the variance, $H_0\colon\sigma^2=\sigma_0^2$ is tested with

$$
\chi_0^2=\frac{(n-1)s^2}{\sigma_0^2}\overset{H_0}{\sim}\chi^2_{n-1},
$$

and against $H_1\colon\sigma^2\ne\sigma_0^2$ it is rejected when $\chi_0^2>\chi^2_{n-1,\alpha/2}$ or $\chi_0^2<\chi^2_{n-1,1-\alpha/2}$. This test, unlike the $t$-test, is sensitive to departures from normality.

### 2.3.2. Two Independent Populations

Let $X_{11},\dots,X_{1n_1}$ and $X_{21},\dots,X_{2n_2}$ be independent random samples from $\mathcal{N}(\mu_1,\sigma_1^2)$ and $\mathcal{N}(\mu_2,\sigma_2^2)$ (or from any populations for which the central limit theorem makes the sample means approximately normal), and test $H_0\colon\mu_1-\mu_2=\Delta_0$. The estimator of $\mu_1-\mu_2$ is $\bar X_1-\bar X_2$, with

$$
\operatorname{Var}(\bar X_1-\bar X_2)=\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}.
$$

The three cases differ in what is known about the variances.

Variances known. The statistic

$$
Z_0=\frac{\bar X_1-\bar X_2-\Delta_0}{\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}}\overset{H_0}{\sim}\mathcal{N}(0,1)
$$

is compared with $z_{\alpha/2}$ (two-sided) or $z_\alpha$ (one-sided).

Variances unknown and equal. With $\sigma_1^2=\sigma_2^2=\sigma^2$, the variance of the difference is $\sigma^2(1/n_1+1/n_2)$ and $\sigma^2$ is estimated from both samples.

**Definition 2.3.1 (Pooled Variance and Two-Sample t-Test)** The **pooled variance** of two samples is

$$
s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}=\frac{\mathrm{SSE}_1+\mathrm{SSE}_2}{n_1+n_2-2},
$$
where $\mathrm{SSE}_i=\sum_j(X_{ij}-\bar X_i)^2$. The **two-sample t-test** (pooled $t$-test) of $H_0\colon\mu_1-\mu_2=\Delta_0$ uses

$$
t_0=\frac{\bar X_1-\bar X_2-\Delta_0}{s_p\sqrt{1/n_1+1/n_2}}\overset{H_0}{\sim}t_{n_1+n_2-2},
$$
and rejects when $\lvert t_0\rvert>t_{n_1+n_2-2,\alpha/2}$ against $\mu_1-\mu_2\ne\Delta_0$, when $t_0>t_{n_1+n_2-2,\alpha}$ against $\mu_1-\mu_2>\Delta_0$, and when $t_0<-t_{n_1+n_2-2,\alpha}$ against $\mu_1-\mu_2<\Delta_0$.

The corresponding confidence interval is $\bar X_1-\bar X_2\pm t_{n_1+n_2-2,\alpha/2}\,s_p\sqrt{1/n_1+1/n_2}$.

Variances unknown and unequal. Without $\sigma_1^2=\sigma_2^2$ there is no exact test of this form: this is the **Behrens–Fisher problem**. The standard approximate solution is **Welch's t-test**, which estimates each variance separately,

$$
t_0^*=\frac{\bar X_1-\bar X_2-\Delta_0}{\sqrt{s_1^2/n_1+s_2^2/n_2}},
$$

and refers $t_0^*$ to a $t$-distribution with the degrees of freedom given by the following approximation.

**Definition 2.3.2 (Satterthwaite Approximation)** The **Satterthwaite approximation** (Welch–Satterthwaite equation) approximates the distribution of the linear combination $\hat V=s_1^2/n_1+s_2^2/n_2$ of independent mean squares by a scaled $\chi^2$ distribution, $\nu\hat V/V\overset{\cdot}{\sim}\chi^2_\nu$ with $V=\mathbb{E}\hat V$, and matches the variances to obtain

$$
\nu=\frac{\left(s_1^2/n_1+s_2^2/n_2\right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1-1}+\dfrac{(s_2^2/n_2)^2}{n_2-1}}.
$$

The degrees of freedom $\nu$ lie between $\min(n_1,n_2)-1$ and $n_1+n_2-2$ and are usually not an integer. The same device will give approximate intervals for variance components in later chapters. In R both tests are computed by

```r
t.test(x, y = NULL, alternative = c("two.sided", "less", "greater"),
       mu = 0, paired = FALSE, var.equal = FALSE, conf.level = 0.95, ...)
```

where `mu` is $\Delta_0$. The default `var.equal = FALSE` gives Welch's test; `var.equal = TRUE` gives the pooled test, and `paired = TRUE` the paired test of Section 2.3.3.

Welch's test can give a comfortable feeling that the comparison of means makes sense even when the variances are wildly different. It should not. Unequal variances are an important finding in their own right: if two samples show large differences in variance, this is usually much more important than any difference in means, and a treatment that gives a higher mean yield is often of little interest if it also has a much higher error variance. The analyst must investigate the variances along with the means, usually with diagnostic plots and tests of homogeneity of variance.

For two variances, $H_0\colon\sigma_1^2=\sigma_2^2$ is tested with

$$
F_0=\frac{s_1^2}{s_2^2}\overset{H_0}{\sim}F_{n_1-1,\,n_2-1},
$$

rejecting against $\sigma_1^2\ne\sigma_2^2$ when $F_0>F_{n_1-1,n_2-1,\alpha/2}$ or $F_0<F_{n_1-1,n_2-1,1-\alpha/2}$. Like the $\chi^2$ test, this **F-test** is sensitive to non-normality.

The pooled $t$-test assumes that the two samples are independent, that the populations have equal variances and that they are normal. When the samples are small and the data are skewed, the $t$-test should not be trusted; the **Wilcoxon rank-sum test** ([3.2.6](/3.2.6)) needs only independence and equal spread (it tests for a shift between two distributions of the same shape).

### 2.3.3. Paired Comparisons

**Definition 2.3.3 (Paired Design and Paired t-Test)** In a **paired design** the experimental units come in $n$ pairs of similar units (or each unit is used twice), and the two treatments are applied one to each member of the pair, in random order. With the paired differences $d_j=y_{1j}-y_{2j}$, $j=1,\dots,n$, the **paired t-test** of $H_0\colon\mu_1-\mu_2=\Delta_0$ is the one-sample $t$-test applied to the differences:

$$
t_0=\frac{\bar d-\Delta_0}{s_d/\sqrt n}\overset{H_0}{\sim}t_{n-1},\qquad s_d^2=\frac{1}{n-1}\sum_{j=1}^n(d_j-\bar d)^2.
$$

Typical pairs are twins, the two arms or eyes of a subject, two halves of a specimen, or the same subject before and after. The paired design is a simple example of blocking: each pair is a block, a relatively homogeneous set of units, and the treatments are randomized only within the block, which is a restriction on complete randomization. It is the special case with two treatments of the randomized complete block design.

The models make the difference precise. For the unpaired design,

$$
Y_{ij}=\mu+\tau_i+\varepsilon_{ij},\qquad i=1,2,\ j=1,\dots,n,
$$

where $\tau_i$ is the effect of treatment $i$ with $\tau_1+\tau_2=0$ and $\varepsilon_{ij}$ are independent errors with mean $0$ and variance $\sigma_i^2$. For the paired design,

$$
Y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij},\qquad \sum_{j=1}^n\beta_j=0,
$$

where $\beta_j$ is the effect of the $j$-th pair. In the paired model $d_j=\tau_1-\tau_2+\varepsilon_{1j}-\varepsilon_{2j}$: the pair effect $\beta_j$ cancels, $\mathbb{E}[d_j]=\mu_1-\mu_2$ with $\mu_i=\mu+\tau_i$, and $s_d^2$ is an unbiased estimator of $\sigma_d^2=\operatorname{Var}(d_j)$. This cancellation is the whole benefit of pairing.

When data come from a paired design, should they be analyzed as paired or unpaired? Take $n_1=n_2=n$ and equal variances $\sigma^2$. Even if $\sigma^2$ were known, $\sigma_d^2$ usually is not, and in the most common case neither is known. The two statistics are

$$
t_{\text{unpaired}}=\frac{\bar X_1-\bar X_2-\Delta_0}{s_p\sqrt{2/n}}\sim t_{2n-2},\qquad
t_{\text{paired}}=\frac{\bar X_1-\bar X_2-\Delta_0}{s_d/\sqrt n}\sim t_{n-1},
$$

with $s_p^2=(\mathrm{SSE}_1+\mathrm{SSE}_2)/(2n-2)$ and $s_d^2=\mathrm{SSE}_d/(n-1)$, where the sum of squares of the differences is

$$
\mathrm{SSE}_d=\sum_{j=1}^n\bigl(X_{1j}-X_{2j}-(\bar X_1-\bar X_2)\bigr)^2=\mathrm{SSE}_1+\mathrm{SSE}_2-2\sum_{j=1}^n(X_{1j}-\bar X_1)(X_{2j}-\bar X_2).
$$

The numerators are the same; the estimate $\bar d=\bar X_1-\bar X_2$ of the difference does not depend on the analysis. The denominators differ: if the members of a pair are positively correlated, the cross-product term is positive and $s_d^2$ is much smaller than $2s_p^2$. The price of pairing is the loss of degrees of freedom, $n-1$ instead of $2n-2$, which makes the critical value larger. Pairing pays when the pairs really are homogeneous; with unrelated "pairs" it only loses degrees of freedom. If the design was paired, however, the unpaired analysis is not merely less powerful but wrong, because its variance estimate is biased.

**Proposition 2.3.1** Let $n_1=n_2=n$. Under the unpaired model with $\sigma_1^2=\sigma_2^2=\sigma^2$, $s_p^2=(s_1^2+s_2^2)/2$ is an unbiased estimator of $\sigma^2$. Under the paired model with $\operatorname{Var}(\varepsilon_{ij})=\sigma^2$,

$$
\mathbb{E}[s_p^2]=\sigma^2+\frac{1}{n-1}\sum_{j=1}^n\beta_j^2,
$$

so $s_p^2$ overestimates the error variance by the variation between pairs, and the unpaired test is conservative and loses power.

**Proof** The first statement is the unbiasedness of each $s_i^2$. Under the paired model $\bar Y_{1\cdot}=\mu+\tau_1+\bar\varepsilon_{1\cdot}$ because $\sum_j\beta_j=0$, so

$$
\mathrm{SSE}_1=\sum_{j=1}^n(Y_{1j}-\bar Y_{1\cdot})^2=\sum_{j=1}^n\bigl(\beta_j+\varepsilon_{1j}-\bar\varepsilon_{1\cdot}\bigr)^2.
$$

Expanding, the cross terms $2\beta_j(\varepsilon_{1j}-\bar\varepsilon_{1\cdot})$ have mean zero and $\mathbb{E}\sum_j(\varepsilon_{1j}-\bar\varepsilon_{1\cdot})^2=(n-1)\sigma^2$, hence $\mathbb{E}[\mathrm{SSE}_1]=\sum_j\beta_j^2+(n-1)\sigma^2$ and $\mathbb{E}[s_1^2]=\sigma^2+\sum_j\beta_j^2/(n-1)$. The same holds for $s_2^2$, and averaging gives the result. $\square$

**Example 2.3.1** In a treatment–control study on ten pairs of twins, one twin of each pair received drug 1 and the other drug 2, assigned at random, and a response was measured:

| Pair | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Drug 1 | 3 | 3 | 4 | 8 | 3 | 2 | 9 | 5 | 4 | 7 |
| Drug 2 | 3 | 5 | 3 | 8 | 2 | 4 | 9 | 4 | 5 | 6 |
| $d_j$ | 0 | $-2$ | 1 | 0 | 1 | $-2$ | 0 | 1 | $-1$ | 1 |

The means are $\bar y_1=4.8$ and $\bar y_2=4.9$, so the estimate of $\mu_1-\mu_2$ is $\bar d=-0.1$ under either analysis. The sums of squares are $\mathrm{SSE}_1=51.6$, $\mathrm{SSE}_2=44.9$, the cross-product sum is $41.8$ and $\mathrm{SSE}_d=51.6+44.9-2(41.8)=12.9$. Hence

$$
s_p=\sqrt{\frac{96.5}{18}}=2.32,\qquad s_d=\sqrt{\frac{12.9}{9}}=1.20.
$$

The responses vary much more between pairs (from $2$ to $9$) than within them, and the twins' responses are strongly correlated ($r=0.87$). The two analyses give:

| | Standard error of $\bar d$ | $t_0$ | df | Critical value $t_{\nu,0.025}$ | 95% confidence interval for $\mu_1-\mu_2$ |
|---|---|---|---|---|---|
| Unpaired | $s_p\sqrt{2/10}=1.035$ | $-0.097$ | 18 | 2.101 | $-0.1\pm2.17=(-2.28,\ 2.08)$ |
| Paired | $s_d/\sqrt{10}=0.379$ | $-0.264$ | 9 | 2.262 | $-0.1\pm0.86=(-0.96,\ 0.76)$ |

Neither test finds a difference between the drugs ($p=0.92$ and $p=0.80$), but the conclusions are not equally informative: the paired interval is less than half as wide despite the larger critical value, because pairing removed the large variation between the twin pairs. The paired analysis is the correct one for this design.

![Twin data: left, the responses to drug 1 and drug 2 as two independent groups, which overlap almost completely; right, the same data with the two members of each twin pair joined by a line, showing that the differences within pairs are small compared with the differences between pairs](./plots/paired_vs_unpaired.py)

### 2.3.4. Balanced Designs

**Definition 2.3.4 (Balanced Design)** A design is a **balanced design** if every treatment (treatment combination) has the same number of replicates.

For a fixed total number of runs, a balanced design is the best choice for several reasons.

1. It gives the smallest variance of the estimated difference and hence the largest power (Proposition 2.3.2).
2. The test statistic is less sensitive to small departures from the assumption of equal variances (Proposition 2.3.3).
3. In designs with several factors, balance makes the factors orthogonal, so the variation can be decomposed into the contributions of the individual factors without confounding ([3.8.6](/3.8.6)).

**Proposition 2.3.2** For a fixed total $N=n_1+n_2$, $\operatorname{Var}(\bar Y_1-\bar Y_2)=\sigma^2(1/n_1+1/n_2)$ is minimized by $n_1=n_2=N/2$, and the power of the pooled two-sample $t$-test against any fixed $\mu_1-\mu_2\ne\Delta_0$ is then maximal.

**Proof** By the inequality between the arithmetic and harmonic means, $\frac1{n_1}+\frac1{n_2}\ge\frac{4}{n_1+n_2}=\frac4N$, with equality if and only if $n_1=n_2$. Under the alternative, $t_0$ has a noncentral $t$-distribution with $N-2$ degrees of freedom, whatever the split, and noncentrality parameter $\delta=(\mu_1-\mu_2-\Delta_0)/\bigl(\sigma\sqrt{1/n_1+1/n_2}\bigr)$; the power is increasing in $\lvert\delta\rvert$, which is largest when $1/n_1+1/n_2$ is smallest. $\square$

**Proposition 2.3.3** Let the two samples have variances $\sigma_1^2,\sigma_2^2$, not necessarily equal. The pooled estimate of $\operatorname{Var}(\bar Y_1-\bar Y_2)$ has expectation

$$
\mathbb{E}\left[s_p^2\left(\frac1{n_1}+\frac1{n_2}\right)\right]=\frac{(n_1-1)\sigma_1^2+(n_2-1)\sigma_2^2}{n_1+n_2-2}\left(\frac1{n_1}+\frac1{n_2}\right),
$$

which equals the true variance $\sigma_1^2/n_1+\sigma_2^2/n_2$ when $n_1=n_2$, for any $\sigma_1^2,\sigma_2^2$. When $n_1\ne n_2$ it underestimates the true variance if the smaller sample has the larger variance, and overestimates it if the smaller sample has the smaller variance.

**Proof** The expectation follows from $\mathbb{E}[s_i^2]=\sigma_i^2$; write $N=n_1+n_2$. With $n_1=n_2=n$ it is $\frac{\sigma_1^2+\sigma_2^2}{2}\cdot\frac2n=\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{n}$. In general, subtracting $\sigma_1^2/n_1+\sigma_2^2/n_2=(n_2\sigma_1^2+n_1\sigma_2^2)/(n_1n_2)$ and using $N(n_1-1)-(N-2)n_2=(N-1)(n_1-n_2)$, the bias is

$$
\mathbb{E}\left[s_p^2\left(\frac1{n_1}+\frac1{n_2}\right)\right]-\left(\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}\right)=\frac{(N-1)(n_1-n_2)(\sigma_1^2-\sigma_2^2)}{(N-2)\,n_1n_2}.
$$

It is negative exactly when the smaller sample has the larger variance. $\square$

The consequences are easy to see by simulation. The first pair of R simulations below compares the power of the pooled $t$-test for $\mu_1-\mu_2=10$ and $\sigma=9$ with $40$ observations split $5{:}35$ and $20{:}20$; the second pair compares the actual level of the pooled and Welch tests when $H_0$ is true but the group of $5$ has standard deviation $15$ and the group of $35$ has standard deviation $3$.

```r
# Loss of power in an unbalanced design (equal variances)
set.seed(515); m <- 10^5
pv.u <- replicate(m, t.test(rnorm(5, 100, 9), rnorm(35, 110, 9), var.eq = TRUE)$p.val)
mean(pv.u < .05)
#[1] 0.61952
set.seed(515)
pv.b <- replicate(m, t.test(rnorm(20, 100, 9), rnorm(20, 110, 9), var.eq = TRUE)$p.val)
mean(pv.b < .05)
#[1] 0.92743

# Distortion of the significance level (H0 true, unequal variances, unbalanced)
set.seed(515); m <- 10^5
pv.p <- replicate(m, t.test(rnorm(5, 100, 15), rnorm(35, 100, 3), var.eq = TRUE)$p.val)
mean(pv.p < .05)
#[1] 0.44354
set.seed(515)
pv.w <- replicate(m, t.test(rnorm(5, 100, 15), rnorm(35, 100, 3))$p.val)
mean(pv.w < .05)
#[1] 0.05119
```

With the same $40$ runs the balanced design has power $0.93$ against $0.62$ for the unbalanced one, in agreement with the noncentral $t$ calculation (noncentrality $3.51$ against $2.32$). When the small group has the large variance, the pooled test rejects a true null hypothesis $44\%$ of the time instead of $5\%$, as Proposition 2.3.3 predicts, while Welch's test keeps the level ($0.051$). With $n_1=n_2$ the pooled test would have been nearly unaffected by the unequal variances.

## 2.4. Power and Sample Size

### 2.4.1. Errors and Power

A test can make two kinds of mistakes: a **type I error** (a false alarm, rejecting a true $H_0$), whose probability is controlled at the **level of significance** $\alpha$, and a **type II error** (a missed detection, accepting a false $H_0$), whose probability we write $\beta$. The **power** of the test, $\eta=1-\beta$, is the probability of rejecting $H_0$ when a specified alternative is true; as a function of the parameter it is the **power function** ([3.2.5](/3.2.5)). A good rejection region keeps the type I error probability at most $\alpha$ (usually $0.05$ or $0.01$) and makes the power as large as possible; a most powerful test maximizes the probability of detection for a given probability of false alarm.

In theory there are four ways of increasing the power of a test of $\mu=\mu_0$ against $\mu=\mu_1$:

1. increase $\alpha$;
2. consider an alternative $\mu_1$ further from $\mu_0$: a larger difference $\delta=\mu_1-\mu_0$ is easier to detect;
3. decrease the standard deviation $\sigma$;
4. increase the sample size $n$.

In practice the first two are usually not available: we do not want more type I errors, and the difference $\delta$ that matters is fixed by the subject before the data are collected. Decreasing $\sigma$ and increasing $n$ can be hard or expensive. What the experimenter can do is to keep a close eye on the experimental procedure, which reduces the part of $\sigma$ due to sloppy execution, and to use a better design: blocking, of which the paired design is the simplest form, removes a known source of variation from $\sigma$.

The power of a given test is computed in three steps:

1. state $H_0$ and $H_1$;
2. find the condition for rejecting $H_0$ at level $\alpha$: the critical value of the test statistic, transformed if convenient to the original scale (for example to a critical value of $\bar X$);
3. compute the probability of that event under $H_1$.

### 2.4.2. Sample Size

Choosing the sample size is one of the most important decisions in designing an experiment: we typically want to detect a difference that matters, say $80\%$ or $90\%$ of the time, with a $5\%$ test. For the two-sided $Z$-test of $H_0\colon\mu=\mu_0$ with known $\sigma$, $Z_0=(\bar X-\mu_0)/(\sigma/\sqrt n)$ is $\mathcal{N}(0,1)$ under $H_0$ and $\mathcal{N}\bigl((\mu-\mu_0)\sqrt n/\sigma,\,1\bigr)$ when the mean is $\mu$, so the power is

$$
\eta(\mu)=\Phi\!\left(-z_{\alpha/2}-\frac{\mu-\mu_0}{\sigma/\sqrt n}\right)+1-\Phi\!\left(z_{\alpha/2}-\frac{\mu-\mu_0}{\sigma/\sqrt n}\right).
$$

For $\delta=\mu-\mu_0>0$ the first term is negligible, and setting $\eta=1-\beta$ gives the sample size

$$
n\approx\left(\frac{(z_{\alpha/2}+z_\beta)\,\sigma}{\delta}\right)^2.
$$

For two independent groups of $n$ each, the variance of $\bar X_1-\bar X_2$ is $2\sigma^2/n$, and the sample size per group is twice this value. For the $t$-test the same reasoning holds with $\sigma$ estimated: under the alternative $t_0$ has a **noncentral t-distribution** ([3.3.3](/3.3.3)) with $n-1$ degrees of freedom (one sample) and **noncentrality parameter** $(\mu-\mu_0)/(\sigma/\sqrt n)$, and

$$
\eta(\mu)=T\bigl(-t_{n-1,\alpha/2}\bigr)+1-T\bigl(t_{n-1,\alpha/2}\bigr),
$$

where $T$ is the distribution function of that noncentral $t$-distribution. Because the degrees of freedom depend on $n$, the equation $\eta=1-\beta$ is solved numerically; the $Z$ formula gives a slightly too small starting value. The left panel of the figure below shows the two distributions of the statistic and the areas $\alpha$ and $\beta$; the right panel shows how the power grows with $n$.

![Left: density of the two-sample t statistic under H0 (central t with 18 degrees of freedom) and under H1 (noncentral t), with the two-sided 5% rejection region shaded under H0 (alpha) and the acceptance region shaded under H1 (beta); right: power of the two-sided two-sample t-test at level 0.05 against the number of observations per group, for standardized differences 0.5, 1 and 1.5](./plots/power_t.py)

The relation between power, sample size and effect size is displayed graphically in two ways. A **power curve** plots the power against $n$ for a given standardized effect size $d=\delta/\sigma$ (right panel above).

**Definition 2.4.1 (Operating Characteristic Curve)** For a given sample size $n$, the **operating characteristic curve** (OC curve) of a test plots the probability $\beta$ of accepting $H_0$ against a parameter that measures how far the null hypothesis is from the truth, such as the standardized difference $d$.

The OC curve is the complement of the power function, $\beta=1-\eta$. Families of OC curves for several $n$, published for the common tests, allow the sample size to be read off: choose the smallest $n$ whose curve is below the desired $\beta$ at the difference $d$ that matters.

In R, `power.t.test` performs these computations for the one-sample, two-sample and paired $t$-tests. Exactly one of the arguments `n`, `delta`, `sd`, `power` and `sig.level` must be `NULL` (`power` is `NULL` by default), and that one is computed from the others:

```r
power.t.test(n = 20, delta = .01)
power.t.test(n = 20, delta = .01, strict = TRUE)
```

```text
     Two-sample t test power calculation         Two-sample t test power calculation

              n = 20                                      n = 20
          delta = 0.01                                delta = 0.01
             sd = 1                                      sd = 1
      sig.level = 0.05                            sig.level = 0.05
          power = 0.02685744                          power = 0.0501089
    alternative = two.sided                     alternative = two.sided

NOTE: n is number in *each* group           NOTE: n is number in *each* group
```

Here `delta` $=\mu_1-\mu_2$, `sd` $=\sigma$ (default $1$), and `n` is the number of observations in each group, not the total. By default the power of the two-sided test counts only the rejections in the tail on the side of `delta`, which is accurate unless `delta` is close to $0$; `strict = TRUE` adds the probability of rejecting in the opposite tail. With the tiny difference $0.01$ the difference is visible: one tail alone gives about $\alpha/2=0.027$, both tails give about $\alpha=0.050$, as they must for an alternative that is practically $H_0$.

## 2.5. Designing a Simple Comparative Experiment

Blood plasma is prepared by spinning a tube of fresh blood in a centrifuge until the blood cells settle at the bottom. An experiment was planned to assess the difference, for metabolomic analyses, between processing plasma from EDTA-preserved whole blood at room temperature ($24\,^\circ\mathrm{C}$) and at $4\,^\circ\mathrm{C}$. The investigators who preferred $4\,^\circ\mathrm{C}$ wanted to reduce protease and peptidase activity; the proponents of room temperature wanted to prevent platelet activation and contamination by platelet proteins. The design was:

1. four healthy male subjects;
2. blood was drawn from each arm, beginning in all cases with the right arm, giving five $6\,\mathrm{ml}$ EDTA tubes from each arm;
3. the first tube from each arm (tubes 1 and 6) was discarded; tubes 2, 4, 7 and 9 were processed to plasma at $24\,^\circ\mathrm{C}$ and tubes 3, 5, 8 and 10 at $4\,^\circ\mathrm{C}$;
4. the $24\,^\circ\mathrm{C}$ samples were spun on one centrifuge model and the $4\,^\circ\mathrm{C}$ samples on another.

Judged by the principles of Section 2.1, each step has a problem.

1. Representativeness and replication: four healthy men are a small and narrow sample of the population whose blood will be analyzed in practice (women, older and sick people); the conclusions extend at most to healthy men, and with four subjects the variation between subjects is poorly estimated. The subjects do serve as blocks, which is good: both temperatures are compared within each subject.
2. Randomization of the order: the right arm is always drawn first, so arm and time of drawing are the same thing. This is harmless for the temperature comparison only because both temperatures appear in both arms; it would be better to randomize which arm is drawn first.
3. Systematic instead of random allocation: within each arm the tubes alternate, and the $24\,^\circ\mathrm{C}$ tube always precedes the $4\,^\circ\mathrm{C}$ tube (2 before 3, 4 before 5). Any trend over the drawing sequence is partly confounded with temperature. The tubes within each arm should be allocated to the temperatures at random.
4. Confounding with equipment: each temperature has its own centrifuge, so the effect of temperature cannot be separated from the effect of the centrifuge. This is the most serious flaw, because it is complete: no analysis can undo it. Both temperatures should be processed on the same centrifuge (or each centrifuge should process both temperatures in a balanced, randomized way).

These points lead to a set of practical guidelines for designing a statistical experiment.

- Understand the objectives and the constraints clearly; state what quantities are to be estimated and which hypotheses are to be tested.
- Consider designs tailored to the aims of the experiment that satisfy all ethical, physical and financial constraints.
- Evaluate the proposed design before running it: can the objectives be achieved, will the estimates have sufficient precision, and will the tests have adequate power? In particular, there should be an adequate number of replicates, the treatments should be allocated to the units at random, extraneous factors should be reduced as far as possible, and known ones should be handled by blocking where possible.

## Summary

- A good design is efficient and keeps the experimental error small. Its principles are summarized in the table of Section 2.1.5: representativeness, randomization (Definition 2.1.2) against **confounding** with lurking variables (Definition 2.1.1), replication rather than repetition (Definition 2.1.3), and blocking of nuisance factors (Definition 2.1.4): block what you can, randomize what you cannot.
- A comparative experiment (Definition 2.2.1) compares treatments that the experimenter assigns; comparisons of groups that are only observed, such as regions in a survey, are not comparative experiments.
- Choosing the two-sample analysis:

  ```mermaid
  flowchart TD
    A["Two treatments: how were the units assigned?"] --> B["Paired design (pairs or blocks of two)"]
    A --> C["Two independent samples"]
    B --> B1["Paired t-test on d_j: t = d-bar / (s_d / sqrt n), df n - 1"]
    C --> D{"Variances"}
    D -->|known| D1["Z-test with sigma_1^2/n_1 + sigma_2^2/n_2"]
    D -->|unknown, equal| D2["Pooled t-test with s_p, df n_1 + n_2 - 2"]
    D -->|unknown, unequal| D3["Welch t-test, Satterthwaite df"]
    C --> E["Small, skewed samples: Wilcoxon rank-sum test"]
  ```

- Paired versus unpaired analysis of a paired design (Example 2.3.1):

  | | Unpaired | Paired |
  |---|---|---|
  | Estimate of $\mu_1-\mu_2$ | $\bar X_1-\bar X_2$ | $\bar d=\bar X_1-\bar X_2$ (the same) |
  | Standard error | $s_p\sqrt{2/n}$ | $s_d/\sqrt n$ |
  | Degrees of freedom | $2n-2$ | $n-1$ |
  | Under the paired model | $s_p^2$ biased upward by $\sum\beta_j^2/(n-1)$ (Proposition 2.3.1) | $s_d^2$ unbiased for $\sigma_d^2$ |
  | Pays off when | units are homogeneous | pairs are homogeneous and differ from each other |

- Balanced designs minimize the variance of a comparison and maximize the power for a given number of runs (Proposition 2.3.2), and make the pooled $t$-test robust to unequal variances (Proposition 2.3.3).
- Power increases with $\alpha$, the difference to be detected, the sample size and a smaller $\sigma$; in practice better procedures and blocking are the available levers. The sample size for a $Z$-test is $n\approx\bigl((z_{\alpha/2}+z_\beta)\sigma/\delta\bigr)^2$ per sample (twice that per group for two groups); for $t$-tests use the noncentral $t$-distribution, power curves, OC curves (Definition 2.4.1) or `power.t.test`, where `n` is per group.

## Questions

1. To estimate the mean height of the $1000$ students of a school with $20$ classes of $50$, we can (1) randomly choose $2$ classes and measure all $100$ of their students, or (2) number all students and randomly choose $100$. Which scheme is better, and why? Relate the answer to the difference between replication and repetition.

   **Answer** Scheme 2, a simple random sample. In scheme 1 (cluster sampling) the students of a class share age, background and environment, so the $100$ heights carry much less information than $100$ independent ones: in the extreme case the sample is effectively two observations, one per class, and the variance of the estimate is driven by the variation between classes, which two clusters estimate poorly. The situation is like an experiment with two experimental units each measured many times: the measurements within a unit are closer to repetitions than to replicates.
2. In the regression of the offspring's seed size on the parent's seed size in Galton's sweet pea data, one may either take the median offspring size for each parent size and fit a line through these points, or fit the regression to all the data. Which is better?

   **Answer** Fit all the data. With equal numbers of offspring per parent size and means instead of medians, the least squares line is the same either way, but averaging first throws away the variation of the replicates around their mean: the residual variance, the standard errors, the tests and the pure error part of the lack-of-fit test ([3.3.6](/3.3.6)) all need it. With unequal numbers at different $X$, the averages also have unequal variances and an unweighted fit to them is not efficient. Medians make the situation worse, since they are not even linear in the data.
3. To compare two keyboards A and B for typing efficiency, six manuscripts are typed by the same typist, each manuscript once on each keyboard. Three plans are proposed for the order within manuscripts $1,\dots,6$: (i) A then B for every manuscript; (ii) AB, BA, AB, BA, AB, AB; (iii) AB, BA, AB, BA, AB, BA. Which is best, and which principles are involved?

   **Answer** Plan (iii). Manuscripts differ in difficulty, so each manuscript is a block, and comparing the keyboards within manuscripts removes that variation. Within a manuscript the second typing benefits from familiarity with the text (or suffers from fatigue). In plan (i) this order effect is completely confounded with the keyboard; plan (ii) puts A first four times out of six, so the order effect is only partly balanced; plan (iii) puts each keyboard first three times, balancing the order effect. Better still, decide at random which three manuscripts get the order AB, and if two computers are used, make sure that each keyboard is used equally on both.
4. Is each of the following a comparative experiment? (a) A survey of whether secondary school students in a region play computer games frequently. (b) A survey comparing how often students in region A and region B play. (c) An online shop shows each visitor one of two page layouts, chosen at random, and compares the purchase rates.

   **Answer** (a) No: nothing is compared and nothing is assigned; it is a descriptive survey. (b) No: there is a comparison, but the region is not assigned to the students by the investigator, so this is an observational comparison (a planned survey) and differences may be due to anything else that differs between the regions. (c) Yes: an A/B test, a simple comparative experiment in which the treatments are randomized to the units.
5. For $n=502$ men aged 18–24, the reported weight had mean $77.0\,\mathrm{kg}$ (standard deviation $13.1$), the measured weight mean $78.0\,\mathrm{kg}$ (standard deviation $14.0$), and the difference reported minus measured had mean $-1.0$ and standard deviation $4.1$. Test at level $0.05$ whether the men report their weight correctly on average. What goes wrong if the two columns are treated as independent samples?

   **Answer** Each man gives both values, so the data are paired: $t_0=\bar d/(s_d/\sqrt n)=-1.0/(4.1/\sqrt{502})=-5.46$ with $501$ degrees of freedom, far beyond $t_{501,0.025}=1.965$; on average the men under-report their weight. The 95% confidence interval is $-1.0\pm1.965\times0.183=(-1.36,-0.64)\,\mathrm{kg}$. Treating the columns as independent gives the standard error $\sqrt{13.1^2/502+14.0^2/502}=0.856$ and $t_0=-1.17$, not significant: the huge variation of weight between men swamps the small, consistent difference within men. The estimate $-1.0$ is the same; the question "is the difference of the means significant" is answered correctly only with the variance of the differences.
6. Ten pairs of identical twins are used to compare two diets; the weight gains are

   | Pair | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
   |---|---|---|---|---|---|---|---|---|---|---|
   | Diet 1 | 5.1 | 6.3 | 4.0 | 7.2 | 5.8 | 6.6 | 4.9 | 5.5 | 6.9 | 5.0 |
   | Diet 2 | 4.6 | 5.6 | 3.9 | 6.4 | 5.5 | 5.7 | 4.4 | 5.4 | 6.0 | 4.3 |

   Estimate the difference of the means and give its 95% confidence interval with the paired and with the unpaired analysis. Which is appropriate?

   **Answer** The differences are $0.5,0.7,0.1,0.8,0.3,0.9,0.5,0.1,0.9,0.7$, so $\bar d=0.55$ and $s_d=0.303$. Paired: standard error $0.303/\sqrt{10}=0.0957$, $t_0=5.74$ with $9$ degrees of freedom ($p<0.001$), interval $0.55\pm2.262\times0.0957=(0.33,\ 0.77)$. Unpaired: $s_1=1.015$, $s_2=0.824$, $s_p=0.925$, standard error $0.925\sqrt{0.2}=0.414$, $t_0=1.33$ with $18$ degrees of freedom ($p=0.20$), interval $0.55\pm2.101\times0.414=(-0.32,\ 1.42)$. The design is paired (twins), so the paired analysis is appropriate: the twins' weight gains are highly correlated, and the unpaired analysis, whose $s_p^2$ is inflated by the variation between pairs (Proposition 2.3.1), misses a clear difference.
7. Two treatments are to be compared with a two-sided two-sample $t$-test at $\alpha=0.05$. The standard deviation is $\sigma=0.5$, and a difference of $2.0$ should be detected with probability $0.95$. How many observations per group are needed? Give the R call.

   **Answer** The standardized difference is $d=2.0/0.5=4$. The normal approximation gives $n\approx2(z_{0.025}+z_{0.05})^2/d^2=2(1.960+1.645)^2/16=1.62$ per group, which is too optimistic for a $t$-test with so few degrees of freedom. With the noncentral $t$-distribution, $n=2$ per group gives power $0.56$, $n=3$ gives $0.948$ and $n=4$ gives $0.996$, so $4$ observations per group are needed. In R, `power.t.test(delta = 2, sd = 0.5, power = 0.95)` returns `n = 3.016`, which is rounded up to $4$ per group.
8. Explain why, with $40$ runs available, the experimenter should use $20$ runs per treatment rather than $5$ and $35$, even if the second treatment is cheaper to run.

   **Answer** With equal variances, the standard error of the difference is proportional to $\sqrt{1/n_1+1/n_2}$, which is $0.316$ for $20{:}20$ and $0.478$ for $5{:}35$; the noncentrality parameter is about $1.5$ times larger in the balanced design, and in the simulation of Section 2.3.4 the power rises from $0.62$ to $0.93$. Moreover, if the variances are unequal, the balanced design keeps the pooled $t$-test approximately valid (Proposition 2.3.3), while the unbalanced design can make its actual level as large as $0.44$. Unequal allocation is justified only by different costs or variances, and then the optimal ratio is $n_1/n_2=\sigma_1/\sigma_2\cdot\sqrt{c_2/c_1}$ rather than an arbitrary split.
