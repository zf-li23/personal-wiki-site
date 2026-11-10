---
title: Robust Estimation and Density Estimation
description: Robust estimation (outliers and the MAD rule, the influence function, the breakdown point, the bootstrap for robust estimators, M-estimators and the Huber loss) and nonparametric density estimation (histograms, the naive and kernel estimators, bandwidth selection, boundary bias and local polynomial estimation, k-nearest-neighbor density estimation).
---

The methods of the previous chapters are the classical part of nonparametric statistics: permutation and rank tests, developed from the 1930s to the 1960s, that give exact inference for small and moderate samples under weak assumptions. Since the 1980s cheap computation has added a second, modern part, whose aim is less to test a hypothesis than to extract the features of a data set (its center, its shape, the trend in a scatter plot) without forcing it into a parametric family. The last two chapters of the course survey this part. This chapter treats two problems in one variable: estimating a center or a scale when a few observations are wrong (robust estimation), and estimating a whole density (density estimation). [3.6.14](/3.6.14) turns to regression curves.

The two halves share two ideas that run through the whole course. The first is robustness: the median, which the sign test of [3.6.3](/3.6.3) and the estimators of [3.6.5](/3.6.5) are built on, is insensitive to outliers, and here we measure that insensitivity with the influence function and the breakdown point. The second is the bias–variance trade-off of smoothing: a histogram's bin width, a kernel estimator's bandwidth and the number of neighbors $k$ all decide how much the estimate averages over nearby data, and each trades a systematic error against a random one. Kernel density estimation was introduced in [3.2.3](/3.2.3), and the bootstrap has its own chapter [3.5.7](/3.5.7); we recall what is needed and concentrate on what is new.

## 13.1. Robust Estimation

### 13.1.1. When Assumptions Break Down

"Distribution-free" does not mean "assumption-free" ([3.6.1](/3.6.1)): the rank methods still assume independence, a common center, symmetry or a shift model. Real data violate assumptions in typical ways:

- a few observations break the pattern of the rest;
- measurement or recording errors (a misplaced decimal point, mixed units);
- atypical units (a sick animal in a feeding trial, a faulty machine);
- data pooled from sources of different reliability.

A method is called robust if its conclusions change little under such departures. Three requirements are usually made of it: the influence of any small group of observations is limited; the method still works reasonably when the model fails; and it loses little efficiency when the model holds. The sample mean meets the third requirement but not the first; the sample median meets the first two but loses efficiency at the normal ([3.6.5](/3.6.5): asymptotic relative efficiency $2/\pi\approx0.64$). The M-estimators of Section 13.1.6 aim for all three.

### 13.1.2. Outliers and the MAD Rule

An **outlier** ([3.3.6](/3.3.6)) is an observation that is extremely inconsistent with the rest of the data in the context of the problem. Context matters: counts of insects on plants naturally contain a few very large values, which are a feature of the distribution rather than errors. Two rules guide the treatment of an outlier. If it is clearly an error, correct or remove it (and report that you did). If it is a valid but extreme value, keep it and use methods that it cannot dominate.

To detect outliers we need a center and a scale that the outliers themselves cannot distort. The mean and the standard deviation fail here: one gross error inflates the standard deviation so much that the error no longer looks extreme. Worse, several outliers can hide one another, the *masking effect*: with two large errors, each looks unremarkable when the scale has been inflated by the other. The robust alternatives are the median and the following measure of spread.

**Definition 13.1.1 (Median Absolute Deviation)** The **median absolute deviation** of $x_1,\dots,x_n$ is the median of the absolute deviations from the sample median,

$$
\operatorname{MAD}=\operatorname*{median}_{1\le i\le n}\,\lvert x_i-\operatorname*{median}(x_1,\dots,x_n)\rvert.
$$

For a normal population the population MAD equals $z_{0.25}\,\sigma\approx0.6745\,\sigma$, because $\mathbb{P}(\lvert X-\mu\rvert\le0.6745\,\sigma)=1/2$. The scaled version $1.4826\,\operatorname{MAD}$ (with $1.4826=1/0.6745$) is therefore a **consistent estimator** of $\sigma$ for normal data, and it is what R's `mad()` returns by default (`constant = 1.4826`).

The *MAD rule* flags an observation $x^*$ as a possible outlier when

$$
\frac{\lvert x^*-\operatorname{median}\rvert}{\operatorname{MAD}}>5 .
$$

The threshold $5$ refers to the unscaled MAD. Since $\operatorname{MAD}\approx0.6745\,\sigma$ for normal data, it corresponds to $\lvert x^*-\mu\rvert>5\times0.6745\,\sigma\approx3.4\,\sigma$, which a normal observation exceeds with probability about $0.0008$. An equally common form uses the scaled MAD and the threshold $3$ (or $3.5$): $\lvert x^*-\operatorname{median}\rvert/(1.4826\,\operatorname{MAD})>3$, a robust version of the "three-sigma rule". Both rules are screening devices: a flagged value is a value to investigate, not one to delete automatically.

**Example 13.1.1 (MAD Rule)** The $40$ observations

$$
\begin{aligned}
&6.1,\ 4.7,\ 4.1,\ 4.6,\ 6.0,\ 5.5,\ 4.6,\ 5.8,\ 5.6,\ 5.0,\ 5.9,\ 4.9,\ 3.9,\ 4.9,\ 4.0,\ 3.1,\ 4.9,\ 6.1,\ 3.1,\ 4.3,\\
&4.9,\ 6.0,\ 1.4,\ 3.9,\ 6.1,\ 5.3,\ 2.7,\ 6.9,\ 5.2,\ 3.8,\ 8.2,\ 8.5,\ 8.1,\ 4.9,\ 8.4,\ 8.4,\ 7.3,\ 3.4,\ 10.7,\ 4.7
\end{aligned}
$$

have mean $5.40$, standard deviation $1.85$, median $4.95$ and $\operatorname{MAD}=1.05$ (scaled: $1.56$). The largest value gives $\lvert10.7-4.95\rvert/1.05=5.48>5$ and is flagged; the next most extreme values, $8.5$ and $1.4$, give $3.38$ and are not. With the scaled MAD and threshold $3$ the same single value is flagged ($5.48/1.4826=3.69$). By the classical rule with mean and standard deviation, $10.7$ is only $2.87$ standard deviations from the mean and would pass unnoticed: the outlier has inflated the scale that should expose it. The group of five values between $8.1$ and $8.5$ is not flagged by either rule; it may be a second cluster rather than a set of errors, a question for the histograms of Section 13.2.

:::

### 13.1.3. The Influence Function

How much can one observation move an estimator? For a sample $x_1,\dots,x_n$ and an estimator $\hat\theta$, add a new observation $z$ and record the change,

$$
\hat\theta(x_1,\dots,x_n,z)-\hat\theta(x_1,\dots,x_n),
$$

as a function of $z$. Multiplied by $n+1$, this is the *sensitivity curve* of $\hat\theta$ at the sample; [3.6.5](/3.6.5) drew such curves for the mean, the median and the Hodges–Lehmann estimator of the heart-rate data. The population version replaces the sample by a distribution and the added point by an infinitesimal contamination.

**Definition 13.1.2 (Influence Function)** Let the estimator be a functional $T(F)$ of the distribution (so that $\hat\theta=T(F_n)$ with $F_n$ the **empirical distribution function**), and let $\delta_z$ be the point mass at $z$. The **influence function** of $T$ at $F$ is

$$
\operatorname{IF}(z;T,F)=\lim_{\varepsilon\downarrow0}\frac{T\bigl((1-\varepsilon)F+\varepsilon\delta_z\bigr)-T(F)}{\varepsilon},
$$
where the limit exists. Its supremum $\gamma^*=\sup_z\lvert\operatorname{IF}(z;T,F)\rvert$ is the *gross-error sensitivity*. An estimator with $\gamma^*<\infty$ is said to have a bounded influence function.

$\operatorname{IF}(z;T,F)$ is the derivative of the estimator in the direction of a contamination at $z$: a fraction $\varepsilon$ of gross errors at $z$ changes $T$ by about $\varepsilon\operatorname{IF}(z;T,F)$. With $\varepsilon=1/(n+1)$ and $F=F_n$ this is the sensitivity curve divided by $n+1$, which is why the two curves look alike. The influence function also gives the asymptotic variance: under regularity conditions $\sqrt n\,(T(F_n)-T(F))\xrightarrow{d}\mathcal{N}\bigl(0,\mathbb{E}_F[\operatorname{IF}(X;T,F)^2]\bigr)$, the functional analogue of the **Delta method**.

**Example 13.1.2 (Mean and Median)** For the mean $T(F)=\int x\,\mathrm{d}F(x)=\mu$,

$$
T\bigl((1-\varepsilon)F+\varepsilon\delta_z\bigr)=(1-\varepsilon)\mu+\varepsilon z,\qquad\operatorname{IF}(z;T,F)=z-\mu .
$$

The influence is unbounded: a single observation moved far enough moves the mean as far as we like. For the median $T(F)=F^{-1}(1/2)=\theta$ of a distribution with density $f$, $f(\theta)>0$, contamination at $z>\theta$ moves the median to the point $\theta_\varepsilon$ with $(1-\varepsilon)F(\theta_\varepsilon)=1/2$; differentiating at $\varepsilon=0$ gives $-F(\theta)+f(\theta)\,\theta'_0=0$, so $\theta_0'=1/(2f(\theta))$. With the symmetric argument for $z<\theta$,

$$
\operatorname{IF}(z;\operatorname{median},F)=\frac{\operatorname{sgn}(z-\theta)}{2f(\theta)} .
$$

The influence is bounded: an observation affects the median only through the side of $\theta$ on which it falls, however extreme it is. Both influence functions square-integrate to the familiar asymptotic variances, $\sigma^2$ for the mean and $1/(4f(\theta)^2)$ for the median ([3.6.5](/3.6.5)).

### 13.1.4. The Breakdown Point

The influence function describes the effect of an infinitesimal contamination. The breakdown point asks the opposite, global question: how large a fraction of the data can be arbitrarily bad before the estimator becomes useless?

**Definition 13.1.3 (Breakdown Point)** Let $\boldsymbol{x}=(x_1,\dots,x_n)$ be a sample and $\hat\theta$ an estimator. Replace any $m$ of the observations by arbitrary values, giving a corrupted sample $\boldsymbol{x}'$. The (finite-sample, replacement) **breakdown point** of $\hat\theta$ at $\boldsymbol{x}$ is

$$
\varepsilon_n^*(\hat\theta,\boldsymbol{x})=\min\Big\{\frac mn\colon\sup_{\boldsymbol{x}'}\lvert\hat\theta(\boldsymbol{x}')-\hat\theta(\boldsymbol{x})\rvert=\infty\Big\},
$$
the smallest fraction of replaced observations that can carry the estimate beyond all bounds. Its limit as $n\to\infty$ is the asymptotic breakdown point. (For a scale estimator, breakdown also includes being driven to $0$.)

The breakdown points of the common estimators follow from counting:

| Estimator | Breakdown point | Reason |
|---|---|---|
| mean, standard deviation | $1/n\to0$ | one value moves them arbitrarily |
| $\alpha$-trimmed mean | $\approx\alpha$ | the $\lfloor\alpha n\rfloor$ largest and smallest values are discarded |
| interquartile range | $\approx1/4$ | the upper quartile breaks when a quarter of the data is replaced |
| median, MAD | $\lceil n/2\rceil/n\to1/2$ | the middle order statistics stay among the good data until half are replaced |
| Hodges–Lehmann estimator | $1-1/\sqrt2\approx0.293$ | the median of the Walsh averages breaks when half of them are contaminated (Question 1) |

A breakdown point of $1/2$ is the best possible for an estimator that treats all observations alike (equivariant under shifts): with more than half of the data bad, nothing distinguishes the good part from the bad. Note that the influence function and the breakdown point measure different things. The Hodges–Lehmann estimator has a bounded influence function and a smaller breakdown point than the median, but it is far more efficient at the normal ($3/\pi\approx0.955$ against $2/\pi$, [3.6.5](/3.6.5)).

### 13.1.5. The Bootstrap for Robust Estimators

Robust estimators rarely have simple formulas for their standard errors: the variance of the median involves the unknown density at the median, and that of a trimmed mean or an M-estimator involves the shape of $F$. The **nonparametric bootstrap** ([Algorithm 7.2.1](/3.5.7#alg-7.2.1) in [3.5.7](/3.5.7)) avoids the formulas by replacing $F$ with the empirical distribution function:

1. draw $B$ **bootstrap samples** of size $n$ with replacement from the data;
2. compute the estimator on each bootstrap sample;
3. use the **bootstrap distribution** of these $B$ values to estimate the standard error, to form confidence intervals ([3.5.7](/3.5.7), Section 7.3.3) or, after transforming the data so that $H_0$ holds, to carry out a test (Section 7.3.4 there).

The bootstrap itself makes no hypothesis; it estimates the sampling distribution of a statistic. It is the natural companion of robust estimation, because it lets us use the estimator best suited to the data without needing its variance formula.

**Example 13.1.3 (Bootstrap Standard Errors)** For the $40$ observations of Example 13.1.1, $B=10\,000$ bootstrap samples give standard errors of $0.29$ for the median, $0.29$ for the mean (the formula $s/\sqrt n$ gives $0.29$ too) and $0.29$ for the Huber estimate of Section 13.1.6. A $95\%$ percentile interval for the median is $[4.70,5.85]$. The bootstrap distribution of the median takes only $41$ distinct values, because a median of $40$ values is an average of two order statistics of the sample: for medians of small or discrete samples the bootstrap distribution is lumpy, and the bootstrap can be unreliable ([3.5.7](/3.5.7), Section 7.2.3).

### 13.1.6. M-Estimators and the Huber Loss

The mean minimizes $\sum_i(x_i-\theta)^2$, the median minimizes $\sum_i\lvert x_i-\theta\rvert$, and a **maximum likelihood estimator** of a location parameter minimizes $\sum_i-\log f(x_i-\theta)$. The general form keeps the structure and chooses the loss to suit the purpose.

**Definition 13.1.4 (M-Estimator)** Let $\rho$ be a loss function, usually even with a minimum at $0$, and $s$ a scale. An **M-estimator** of location is a minimizer

$$
\hat\theta=\operatorname*{arg\,min}_\theta\sum_{i=1}^n\rho\Big(\frac{x_i-\theta}{s}\Big),
$$
or, with $\psi=\rho'$, a solution of the estimating equation $\sum_{i=1}^n\psi\bigl((x_i-\theta)/s\bigr)=0$. In regression, $x_i-\theta$ is replaced by the residual $y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}$.

The name stands for "maximum likelihood type": with $\rho=-\log f$ the M-estimator is the MLE, and least squares is the M-estimator with $\rho(t)=t^2/2$, the MLE under normal errors. The idea of robust M-estimation is to choose a $\rho$ that grows more slowly than $t^2$, so that large residuals are downweighted. The scale $s$ is needed because otherwise the estimate would depend on the units of the data; it is estimated robustly first, usually by $1.4826\,\operatorname{MAD}$.

**Definition 13.1.5 (Huber Loss)** For a constant $k>0$, the **Huber loss** is

$$
\rho_k(t)=\begin{cases}t^2/2, & \lvert t\rvert\le k,\\ k\lvert t\rvert-k^2/2, & \lvert t\rvert>k,\end{cases}\qquad\psi_k(t)=\rho_k'(t)=\max\bigl(-k,\min(k,t)\bigr).
$$

The Huber loss is quadratic for small residuals and linear for large ones, and the two pieces join with a continuous derivative at $\pm k$. For small errors it behaves like least squares (efficient); for large errors it behaves like the $L_1$ loss of the median and of **least absolute deviations** regression (insensitive to outliers). Its derivative $\psi_k$ is the identity clipped at $\pm k$: a residual contributes in proportion to its size up to $k$ scale units and no more.

![Loss functions (A) and their derivatives $\psi$ (B) for the squared loss of the mean, the absolute loss of the median and the Huber loss with $k = 1.345$; the dotted lines mark $\pm k$. By Theorem 13.1.1 the influence function of an M-estimator has the shape of $\psi$.](./plots/robust-loss.py)

The estimating equation can be rewritten as a weighted mean. With weights $w_i=\psi(t_i)/t_i$ at the standardized residuals $t_i=(x_i-\theta)/s$, it reads $\sum_iw_i(x_i-\theta)=0$, so $\hat\theta=\sum_iw_ix_i/\sum_iw_i$. For the Huber loss $w(t)=\min(1,k/\lvert t\rvert)$: observations within $k$ scale units get full weight, those further out get weight inversely proportional to their distance. Starting from the median and alternating between computing the weights and the weighted mean is **iteratively reweighted least squares**, the algorithm of robust regression in [3.3.12](/3.3.12) (R: `MASS::rlm`, `MASS::huber`).

**Theorem 13.1.1 (Influence Function of an M-Estimator)** Let $\theta=T(F)$ solve $\mathbb{E}_F\,\psi\bigl((X-\theta)/s\bigr)=0$ with the scale $s$ held fixed, and suppose $\psi$ is differentiable with $\mathbb{E}_F\,\psi'\bigl((X-\theta)/s\bigr)\ne0$. Then

$$
\operatorname{IF}(z;T,F)=\frac{s\,\psi\bigl((z-\theta)/s\bigr)}{\mathbb{E}_F\,\psi'\bigl((X-\theta)/s\bigr)} .
$$

**Proof** Write $F_\varepsilon=(1-\varepsilon)F+\varepsilon\delta_z$ and $\theta_\varepsilon=T(F_\varepsilon)$, so that

$$
(1-\varepsilon)\,\mathbb{E}_F\,\psi\Big(\frac{X-\theta_\varepsilon}s\Big)+\varepsilon\,\psi\Big(\frac{z-\theta_\varepsilon}s\Big)=0 .
$$

Differentiate with respect to $\varepsilon$ at $\varepsilon=0$. The first term contributes $-\mathbb{E}_F\psi((X-\theta)/s)=0$ and $-\frac1s\mathbb{E}_F\psi'((X-\theta)/s)\,\theta_0'$, the second $\psi((z-\theta)/s)$. Setting the sum to zero and solving for $\theta'_0=\operatorname{IF}(z;T,F)$ gives the formula. $\square$

The influence function of an M-estimator is thus proportional to $\psi$: bounded if and only if $\psi$ is bounded. The mean ($\psi(t)=t$) has unbounded influence; the Huber estimator has gross-error sensitivity proportional to $k$. (The median fits the theorem with $\psi=\operatorname{sgn}$ if $\mathbb{E}\psi'$ is read as $2f(\theta)/s$, the derivative of $\mathbb{E}\operatorname{sgn}(X-\theta)$, which recovers Example 13.1.2.) The constant $k$ tunes the compromise between efficiency and robustness: $k\to\infty$ gives the mean, $k\to0$ the median, and the usual choice $k=1.345$ gives $95\%$ asymptotic efficiency relative to the mean when the data are normal, while keeping a bounded influence function. With the MAD as preliminary scale, the Huber location estimator also has breakdown point $1/2$.

**Example 13.1.4 (Huber Estimate)** For the data of Example 13.1.1, with $s=1.4826\times1.05=1.557$ and $k=1.345$, iterating the weighted mean from the median converges to $\hat\theta=5.25$, between the median $4.95$ and the mean $5.40$. The value $10.7$, $3.5$ scale units above the estimate, receives weight $1.345/3.5\approx0.38$; the cluster near $8.3$ is downweighted less. In R:

```r
library(MASS)
huber(x, k = 1.345)     # location and MAD scale: mu = 5.25, s = 1.557
```

:::

M-estimation carries over to regression with the same loss functions (`rlm(y ~ x)`), and there it protects against outlying responses. It does not protect against outlying values of the predictors: a single high-**leverage** point can still determine the fitted line, as for the median regression of [3.6.10](/3.6.10), and the breakdown point of a regression M-estimator is $1/n$. Estimators with a high breakdown point in regression, such as least median of squares ([3.3.12](/3.3.12)) and the Theil–Sen estimator of [3.6.14](/3.6.14), pay with heavier computation or lower efficiency.

## 13.2. Density Estimation

### 13.2.1. The Problem

The eruptions of the Old Faithful geyser in Yellowstone National Park are a classic data set (R: `faithful`): $272$ eruptions, each with its duration and the waiting time until the next eruption. A histogram of the waiting times shows two clear peaks, near $55$ and $80$ minutes: short waits follow short eruptions and long waits follow long ones. No standard parametric family has this shape. A mixture of two normals would fit, but only because we have looked at the data; in general we want to recover the shape of a distribution without fixing its form in advance.

Let $X_1,\dots,X_n$ be a random sample from a continuous distribution with unknown density $f$. A parametric approach assumes $f(x)=f(x;\theta)$ of known form and estimates $\theta$; a nonparametric approach estimates $f$ itself. Every nonparametric density estimator averages the data over a neighborhood of each point, and the size of the neighborhood, controlled by a smoothing parameter, decides the balance in the **bias–variance trade-off**: a large neighborhood oversmooths (large bias, small variance), a small one undersmooths (small bias, large variance).

### 13.2.2. Histograms

**Definition 13.2.1 (Histogram)** Partition the range of the data into bins $(a_j,a_{j+1}]$, $a_1<a_2<\dots<a_{k+1}$, and let $n_j$ be the number of observations in the $j$-th bin. The **histogram** density estimate is

$$
\hat f(x)=\frac{n_j}{n\,(a_{j+1}-a_j)},\qquad x\in(a_j,a_{j+1}] .
$$
With equal bins of width $2h$, $\hat f(x)=\frac1{2nh}\sum_{i=1}^n\boldsymbol{1}\{X_i\in\text{the bin containing }x\}$, a step function.

The histogram is a density (nonnegative, total area $1$), and for fixed bins $n_j\sim\mathrm{Bin}(n,p_j)$ with $p_j=\int_{a_j}^{a_{j+1}}f$, so its bias and variance are easy to analyze: $\hat f(x)$ estimates the average of $f$ over the bin, which differs from $f(x)$ by $O(h)$ when $f$ has a slope, while its variance is about $f(x)/(2nh)$. Wide bins mean large bias and small variance, narrow bins small bias and large variance. Balancing the two terms gives an optimal bin width of order $n^{-1/3}$ (for example Scott's rule $3.49\,s\,n^{-1/3}$), with an integrated squared error of order $n^{-2/3}$; R's `hist()` uses Sturges' rule of about $\lceil\log_2n+1\rceil$ bins, which is often too coarse for large $n$.

The deeper defects are structural. The estimate is discontinuous, although the density usually is not, and it depends on the origin of the bin grid as well as on the bin width. The figure below shows the $40$ observations of Example 13.1.1 in four histograms: with bins of width $2$ the data look unimodal and skewed, with bins of width $0.5$ a separate group near $8.3$ appears, and shifting the origin by half a bin changes the picture again. A histogram is best regarded as an exploratory tool; the estimators below remove the dependence on the grid.

![The same 40 observations in four histograms: bin width 2 with origins 0 and 1 (top), bin width 0.5 with origins 0 and 0.25 (bottom). The rug marks the observations.](./plots/histogram-bins.py)

### 13.2.3. From the Naive Estimator to the Kernel Estimator

The density is the limit $f(x)=\lim_{h\to0}\frac1{2h}\mathbb{P}(x-h<X<x+h)$. Replacing the probability by the fraction of observations gives the *naive estimator*

$$
\hat f(x)=\frac{\#\{i\colon X_i\in(x-h,x+h)\}}{2nh}=\frac1{nh}\sum_{i=1}^nw\Big(\frac{x-X_i}h\Big),\qquad w(u)=\tfrac12\boldsymbol{1}\{\lvert u\rvert<1\}.
$$

Instead of a fixed grid, the window $(x-h,x+h)$ slides with the point $x$ at which we estimate, so the origin of the grid has disappeared. The naive estimator is a sum of boxes of width $2h$ centered at the observations; it is still not continuous, since it jumps whenever $x\pm h$ crosses an observation. Replacing the box $w$ by a smooth bump gives the **kernel density estimator** of [3.2.3](/3.2.3) ([Definition 3.6.1](/3.2.3#def-3.6.1) there, due to Rosenblatt and Parzen),

$$
\hat f_h(x)=\frac1n\sum_{i=1}^nK_h(x-X_i)=\frac1{nh}\sum_{i=1}^nK\Big(\frac{x-X_i}h\Big),\qquad K_h(u)=\frac1hK\Big(\frac uh\Big),
$$

where the **kernel function** $K$ is usually a symmetric density and $h>0$ is the **bandwidth**. The kernel estimator inherits the smoothness of $K$ (with a Gaussian kernel it is infinitely differentiable), is a density whenever $K$ is, and does not depend on any grid. The kernel determines the shape of the bumps and the bandwidth their width. Each observation now contributes with a weight that decreases with its distance from $x$, whereas the naive estimator counts all observations in the window equally.

**Example 13.2.1 (Three Observations)** Take $X_1=30$, $X_2=32$, $X_3=33$, bandwidth $h=5$ and the Epanechnikov kernel $K(u)=\frac34(1-u^2)\boldsymbol{1}\{\lvert u\rvert\le1\}$. Each observation contributes $\frac1{15}K((x-X_i)/5)$, a parabola of half-width $5$; for example at $x=32$,

$$
\hat f(32)=\frac1{15}\Bigl[K(0.4)+K(0)+K(-0.2)\Bigr]=\frac1{15}\cdot\frac34\,(0.84+1+0.96)=0.140 .
$$

| $x$ | $25$ | $28$ | $30$ | $31$ | $32$ | $33$ | $35$ | $38$ |
|---|---|---|---|---|---|---|---|---|
| $\hat f(x)$ | $0$ | $0.060$ | $0.124$ | $0.138$ | $0.140$ | $0.130$ | $0.074$ | $0$ |

The estimate vanishes outside $[25,38]$, where no observation is within $h$ of $x$, and it is smooth inside, peaking between the observations.

:::

[3.2.3](/3.2.3) lists the common kernels: uniform (which gives back the naive estimator, not the histogram), triangular, Epanechnikov, biweight, triweight and Gaussian. Practical experience and theory agree that they give similar estimates for a suitable $h$: the Epanechnikov kernel is optimal for the asymptotic mean integrated squared error, and the others lose only a few percent. Kernels that are allowed to be negative, such as the fourth-order kernel $K(u)=\frac38(3-5u^2)\boldsymbol{1}\{\lvert u\rvert\le1\}$, which integrates to $1$ and has $\int u^2K(u)\,\mathrm{d}u=0$, reduce the bias for very smooth densities from $O(h^2)$ to $O(h^4)$ at the price of an estimate that can be negative.

### 13.2.4. Choosing the Bandwidth

The choice of $h$ matters much more than that of $K$. As [3.2.3](/3.2.3) shows, the pointwise bias is about $\frac{h^2}2m_2(K)f''(x)$ and the variance about $f(x)R(K)/(nh)$, where $m_2(K)=\int u^2K$ and $R(g)=\int g^2$. A small $h$ follows the sample closely and gives a jagged, high-variance estimate; a large $h$ flattens real features such as the two modes of the geyser data. The bandwidth minimizing the asymptotic mean integrated squared error is of order $n^{-1/5}$ and depends on the unknown curvature $R(f'')$. Practical selectors estimate this quantity:

- Normal reference rule. If $f$ is normal with standard deviation $\sigma$ and $K$ is Gaussian, the optimal bandwidth is $(4/3)^{1/5}\sigma n^{-1/5}\approx1.06\,\sigma n^{-1/5}$; replacing $\sigma$ by $s$ gives $h=1.06\,s\,n^{-1/5}$. Silverman's more robust variant $h=0.9\min(s,\widehat{\mathrm{IQR}}/1.34)\,n^{-1/5}$ is the default `bw.nrd0` of R's `density()`. Both are fast but assume a roughly normal shape, so they tend to oversmooth multimodal data.
- Sheather–Jones plug-in. Estimate $R(f'')$ by a kernel estimate of $f''$ with a pilot bandwidth chosen in the same way, and solve the resulting equation for $h$. It adapts to non-normal and multimodal shapes and is widely recommended, but it is not R's default; it is requested by `density(x, bw = "SJ")`.
- Cross-validation chooses $h$ to minimize an unbiased estimate of the integrated squared error (`bw.ucv`); it is less stable than the plug-in rules.

For the waiting times, $s=13.6$, $\widehat{\mathrm{IQR}}/1.34=17.9$ and $n^{-1/5}=0.326$, so R's default bandwidth is $0.9\times13.6\times0.326=3.99$:

```r
x <- faithful$waiting
fit <- density(x)            # Gaussian kernel, bw = bw.nrd0(x)
fit
plot(fit)
lines(density(x, bw = "SJ"), lty = 2)
```

```text
Call:
	density.default(x = x)

Data: x (272 obs.);	Bandwidth 'bw' = 3.988
```

![Density estimates for bimodal waiting times ($n = 272$, simulated from a two-component normal mixture close to the one fitted to the Old Faithful waiting times; the R companion uses the real data `faithful$waiting`). A: Gaussian kernel estimates with $h = 1$ (undersmoothed), the rule-of-thumb bandwidth and $h = 10$ (oversmoothed) over a histogram. B: the kernel estimate, the local linear estimate of Section 13.2.5 (which dips below zero beyond the data) and the k-nearest-neighbor estimate with $k = 50$ of Section 13.2.6 (rough at the peaks, heavy in the tails).](./plots/kde-geyser.py)

### 13.2.5. Boundary Bias and Local Polynomial Estimation

The kernel estimator places a symmetric bump at every observation. When the density is supported on a half-line, such as incomes, survival times or concentrations, $X\ge0$, the bumps of the observations near $0$ spill over into the negative axis, where there are no data, and the estimate near $0$ is too small.

**Definition 13.2.2 (Boundary Bias)** **Boundary bias** is the systematic error of a smoothing estimator near the edge of the support of the data, which arises because the smoothing window extends beyond the edge, where there are no observations, so that the estimate is formed from one side only.

**Proposition 13.2.1 (Kernel Estimator at a Hard Boundary)** Let $f$ vanish on $(-\infty,0)$ and be continuous on $[0,\infty)$ with $f(0)>0$, and let $K$ be a symmetric density on $[-1,1]$. For $x=ch$ with $0\le c<1$, as $h\to0$,

$$
\mathbb{E}\hat f_h(ch)\to f(0)\int_{-1}^cK(u)\,\mathrm{d}u ;
$$
in particular $\mathbb{E}\hat f_h(0)\to f(0)/2$.

**Proof** With the substitution $u=(x-y)/h$,

$$
\mathbb{E}\hat f_h(x)=\int_0^\infty\frac1hK\Big(\frac{x-y}h\Big)f(y)\,\mathrm{d}y=\int_{-1}^{x/h}K(u)\,f(x-hu)\,\mathrm{d}u ,
$$
because $y\ge0$ means $u\le x/h=c$. As $h\to0$, $f(x-hu)\to f(0)$ uniformly on the range of integration, which gives the limit. $\square$

So the kernel estimator is not even consistent at the boundary: it estimates half the density at $0$, and within a distance $h$ of the boundary its bias is of order $1$ rather than $h^2$. Several corrections exist: reflecting the data at the boundary (estimate with the sample $\pm X_i$ and double the result on $[0,\infty)$), special boundary kernels, transforming the data (for example by a logarithm) and estimating on the transformed scale, and local polynomial fitting. The last idea is the most general, and it is the one that [3.6.14](/3.6.14) develops for regression.

The *local polynomial density estimator* bins the data on a fine grid of width $\delta$ starting at the boundary, treats the bin heights $n_j/(n\delta)$ as responses at the bin centers, and at each $x$ fits a low-degree polynomial (usually a line) to them by weighted least squares with kernel weights $K_h(\cdot-x)$; the value of the local fit at $x$ is the estimate. In the interior a local line through symmetric data reproduces the kernel estimate to first order. At the boundary the data are one-sided, but the local slope extrapolates the trend of the density into the edge instead of averaging it with the empty region, and the bias returns to order $h^2$. Unconstrained, the local polynomial can overshoot near an edge and even produce negative values; and where there is no real truncation, as at the two ends of the geyser data, it only adds such artifacts (panel B of the geyser figure). Its real use is for data with a sharp, genuine boundary. In R it is available as `KernSmooth::locpoly(x, bandwidth = h, degree = 1)`, which uses exactly this binned construction.

![Boundary bias at a hard boundary: $500$ observations from $\mathrm{Exp}(1)$. The kernel estimate ($h = 0.3$) leaks mass below $0$ and is far below the true density near the origin, as Proposition 13.2.1 predicts; the local linear estimate, computed from data binned on $[0, \infty)$, follows the density up to the boundary.](./plots/boundary-bias.py)

### 13.2.6. k-Nearest-Neighbor Density Estimation

A fixed bandwidth is a compromise between regions of high and low density. In the tails of a long-tailed distribution a bandwidth suited to the center leaves isolated bumps around single observations, while a bandwidth suited to the tails blurs the center. The **k-nearest neighbors** idea ([3.4.12](/3.4.12)) adapts the window to the data instead: fix the number of observations in the window and let its width vary.

**Definition 13.2.3 (k-Nearest-Neighbor Density Estimation)** Let $d_k(x)$ be the distance from $x$ to the $k$-th nearest of the observations $X_1,\dots,X_n$. In **k-nearest-neighbor density estimation**, $f$ is estimated by

$$
\hat f(x)=\frac{k}{2n\,d_k(x)} ;
$$
more generally, with a kernel $K$, $\hat f(x)=\frac1{n\,d_k(x)}\sum_{i=1}^nK\Big(\frac{x-X_i}{d_k(x)}\Big)$, a kernel estimator with the local bandwidth $h=d_k(x)$.

The motivation is the same as for the naive estimator: an interval of half-width $d$ around $x$ has probability about $2d\,f(x)$, and the interval of half-width $d_k(x)$ contains a fraction $k/n$ of the data; equating the two gives the formula. (Some authors use $k-1$ in place of $k$; the difference is negligible for moderate $k$.) The window widens automatically where the data are sparse, which suppresses the isolated bumps in the tails, and narrows where they are dense. The price is threefold:

- $d_k(x)$ is continuous but has corners, so the estimate is rough, with spikes in dense regions (panel B of the geyser figure, at the peaks);
- far from the data $d_k(x)\approx\lvert x\rvert$, so $\hat f(x)\approx k/(2n\lvert x\rvert)$ decays too slowly: the estimate has heavy, artificial tails, and its integral is infinite (Question 5), so it is not a density;
- like every smoother it needs a smoothing parameter: small $k$ undersmooths, large $k$ oversmooths. For consistency $k\to\infty$ and $k/n\to0$.

Its proper use is for strongly inhomogeneous, long-tailed data, such as large insurance claims or extreme precipitation, where most observations crowd near the lower end and a few lie far out. The following R functions implement both forms (the second with the Epanechnikov kernel) and compare them with a kernel and a local polynomial estimate of the geyser data:

```r
library(KernSmooth)
x <- faithful$waiting
n <- length(x)
k <- 50                                   # number of neighbors

knn_density <- function(t, data, k) {
  sapply(t, function(t0) {
    dk <- sort(abs(data - t0))[k]         # distance to the k-th neighbor
    k / (2 * length(data) * dk)
  })
}
kernel_epanechnikov <- function(u) 0.75 * (1 - u^2) * (abs(u) <= 1)
generalized_knn_density <- function(t, data, k) {
  sapply(t, function(t0) {
    dk <- sort(abs(data - t0))[k]
    sum(kernel_epanechnikov((t0 - data) / dk)) / (length(data) * dk)
  })
}

x_grid <- seq(30, 110, length.out = 200)
kde_est <- bkde(x, bandwidth = dpik(x))          # binned kernel estimate, plug-in bandwidth
locpoly_est <- locpoly(x, bandwidth = dpik(x))   # local linear density estimate
knn_est <- knn_density(x_grid, x, k)
plot(c(30, 110), c(0, 0.05), type = "n", xlab = "Waiting Time", ylab = "Density")
lines(kde_est$x, kde_est$y, lty = 1, lwd = 2, col = 2)
lines(locpoly_est$x, locpoly_est$y, lty = 2, lwd = 2, col = 4)
lines(x_grid, knn_est, lty = 3, lwd = 2, col = 3)
legend("topleft", legend = c("KDE", "Local Polynomial", "Basic k-NN"),
       lty = 1:3, lwd = 2, col = c(2, 4, 3), bty = "n")
```

For the geyser data the fixed-bandwidth kernel estimate is the best of the three: the data are abundant over the whole range and the density decays gently at both ends, so one bandwidth suits everything. The local polynomial estimate shows edge artifacts at both ends, and the k-NN estimate is spiky at the peaks and much too large outside the range of the data.

### 13.2.7. Choosing a Density Estimator

| Estimator | Idea | Weaknesses | Best suited to |
|---|---|---|---|
| histogram | count in fixed bins | depends on bin width and origin; discontinuous | a first look at the data |
| kernel estimator (fixed $h$) | a smooth bump at each observation, all of the same width | boundary bias at a hard edge; isolated bumps in sparse tails | smooth densities without hard edges and with data throughout the range (the geyser data) |
| local polynomial | a low-degree polynomial fitted locally to the binned data | overshoot and possibly negative values near an edge without real truncation | densities with a hard boundary (survival times, $X\ge0$) |
| k-nearest neighbors | window widened until it holds $k$ observations | rough in dense regions; heavy artificial tails; not a density | strongly inhomogeneous, long-tailed data |

In all four the smoothing parameter (bin width, $h$, $k$) controls the bias–variance trade-off, and its choice matters more than any other.

## Summary

- Robust methods limit the influence of a few bad observations, work when the model fails and lose little efficiency when it holds. The median and the **median absolute deviation** (Definition 13.1.1) are the robust center and scale; $1.4826\,\operatorname{MAD}$ estimates $\sigma$ for normal data. MAD rule: flag $\lvert x-\operatorname{median}\rvert/\operatorname{MAD}>5$ (unscaled MAD, about $3.4\sigma$), or the scaled MAD with threshold $3$ (Example 13.1.1).
- **Influence function** (Definition 13.1.2): the effect of an infinitesimal contamination at $z$; mean $z-\mu$ (unbounded), median $\operatorname{sgn}(z-\theta)/(2f(\theta))$ (bounded) (Example 13.1.2).
- **Breakdown point** (Definition 13.1.3): the smallest fraction of bad data that can ruin the estimate: mean $0$, trimmed mean $\alpha$, IQR $1/4$, Hodges–Lehmann $0.293$, median and MAD $1/2$ (the maximum).
- The **nonparametric bootstrap** gives standard errors and intervals for robust estimators without formulas; for medians of small samples its distribution is lumpy (Example 13.1.3).
- **M-estimators** (Definition 13.1.4) minimize $\sum\rho((x_i-\theta)/s)$; their influence function is proportional to $\psi=\rho'$ (Theorem 13.1.1). The **Huber loss** (Definition 13.1.5) is quadratic up to $k$ and linear beyond; $k=1.345$ gives $95\%$ efficiency at the normal with bounded influence; computed by IRLS (Example 13.1.4). In regression, M-estimators do not protect against leverage points.
- Density estimation trades bias against variance through a smoothing parameter. The **histogram** (Definition 13.2.1) depends on bin width and origin; the naive estimator removes the origin; the **kernel density estimator** removes the discontinuity. Bandwidth: normal reference $1.06\,s\,n^{-1/5}$, R's default $0.9\min(s,\mathrm{IQR}/1.34)n^{-1/5}$ (geyser: $3.99$), Sheather–Jones plug-in for multimodal data.
- **Boundary bias** (Definition 13.2.2): at a hard boundary the kernel estimate tends to $f(0)/2$ (Proposition 13.2.1); local polynomial fitting corrects it but can overshoot or go negative.
- **k-nearest-neighbor density estimation** (Definition 13.2.3): $k/(2n\,d_k(x))$, adaptive in sparse tails, rough in dense regions, not integrable. Which estimator to use: Section 13.2.7.

## Questions

1. Show that the asymptotic breakdown point of the Hodges–Lehmann estimator is $1-1/\sqrt2\approx0.293$.

   **Answer** Suppose a fraction $\varepsilon$ of the $n$ observations is replaced by arbitrarily large values. A Walsh average $(X_i+X_j)/2$ is contaminated if at least one of $X_i,X_j$ is bad, and can then be made arbitrarily large. Of the roughly $n^2/2$ Walsh averages, the good ones are those with both indices among the $(1-\varepsilon)n$ good observations, about $(1-\varepsilon)^2n^2/2$. The median of the Walsh averages can be carried away exactly when at least half of them are contaminated, that is, when $(1-\varepsilon)^2\le1/2$, or $\varepsilon\ge1-1/\sqrt2\approx0.293$. The same counting gives the breakdown point of the Theil–Sen slope in [3.6.14](/3.6.14).
2. For normal data, what fraction of good observations does the MAD rule flag (a) with the unscaled MAD and threshold $5$, (b) with the scaled MAD and threshold $3$? Why is a rule with a small false-alarm rate still not a license to delete flagged values?

   **Answer** For large $n$ the median and MAD are close to $\mu$ and $0.6745\sigma$. (a) The rule flags $\lvert X-\mu\rvert>5\times0.6745\sigma=3.37\sigma$, probability $2(1-\Phi(3.37))\approx0.0008$. (b) It flags $\lvert X-\mu\rvert>3\sigma$, probability $0.0027$. In a sample of $1000$ good observations, rule (b) flags about three of them, so a flagged value is not necessarily an error; moreover, in non-normal populations (counts of insects, incomes) extreme values are an expected part of the distribution. A flag calls for checking the record and the context; deleting values without a reason biases the estimates and understates the variability.
3. Use Theorem 13.1.1 to find the influence function of the Huber location estimator when $F$ is $\mathcal{N}(\theta,\sigma^2)$ and $s=\sigma$. What is its gross-error sensitivity for $k=1.345$?

   **Answer** With $t=(z-\theta)/\sigma$, $\psi_k(t)=\max(-k,\min(k,t))$ and $\psi_k'(t)=\boldsymbol{1}\{\lvert t\rvert<k\}$, so $\mathbb{E}\psi_k'((X-\theta)/\sigma)=\mathbb{P}(\lvert Z\rvert<k)=2\Phi(k)-1$. Hence $\operatorname{IF}(z)=\sigma\psi_k((z-\theta)/\sigma)/(2\Phi(k)-1)$: linear in $z$ within $k\sigma$ of $\theta$, constant beyond. For $k=1.345$, $2\Phi(1.345)-1=0.821$, so $\gamma^*=1.345\sigma/0.821\approx1.64\,\sigma$. For comparison, the median has $\gamma^*=1/(2f(\theta))=\sqrt{\pi/2}\,\sigma\approx1.25\,\sigma$ (smaller, but at an efficiency of $0.64$), and the mean has $\gamma^*=\infty$.
4. In histograms of the same data with different bin widths, which component of the error grows with the bin width and which grows as the bins become narrower? Is the naive estimator a continuous function of $x$?

   **Answer** Wider bins average $f$ over a larger interval, so the bias grows (features such as modes are flattened) while the variance falls, since each bin holds more observations. Narrower bins have small bias and large variance (jagged, dominated by single observations). The naive estimator is not continuous: it counts the observations in the open window $(x-h,x+h)$, and this count jumps by one whenever $x-h$ or $x+h$ passes an observation. It is a step function, like the histogram, though its steps are not tied to a fixed grid; a continuous kernel $K$ removes the jumps.
5. Show that the k-nearest-neighbor estimate $\hat f(x)=k/(2n\,d_k(x))$ has infinite integral. What does this mean in practice?

   **Answer** Let $M=\max_i\lvert X_i\rvert$. For $\lvert x\rvert>M$ every observation lies within distance $\lvert x\rvert+M$ of $x$, so $d_k(x)\le\lvert x\rvert+M$ and $\hat f(x)\ge k/(2n(\lvert x\rvert+M))$. Since $\int^\infty\mathrm{d}x/(x+M)=\infty$, the integral of $\hat f$ diverges. In practice the estimate is useful only for describing the shape of the density within the range of the data; it cannot be used as a probability density (for example, for computing tail probabilities or for simulation), and far outside the data it is much too large, as panel B of the geyser figure shows.
6. A sample of $200$ waiting times until a repair is nonnegative, and many values are close to $0$. A colleague's kernel density estimate shows the mode at about $0.3$ hours and a density near $0$ of only half its maximum. Should one conclude that very short waiting times are rare?

   **Answer** No. By Proposition 13.2.1 a kernel estimate tends to half the true density at a hard boundary and is biased downward within about one bandwidth of it, so an apparent mode at a distance of the order of $h$ from $0$ may be an artifact of the boundary bias: a monotonically decreasing density such as the exponential produces exactly this picture (the boundary-bias figure). One should use a boundary-corrected estimate (reflection, a local linear estimate, or an estimate on the log scale) or look at the empirical distribution function near $0$, which has no smoothing bias; only if the mode persists is it a feature of the data.
