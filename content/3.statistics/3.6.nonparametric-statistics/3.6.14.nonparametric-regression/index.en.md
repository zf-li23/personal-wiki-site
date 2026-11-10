---
title: Nonparametric Regression
description: Estimating a regression function without a parametric form, from strong to weak constraints. The Theil–Sen estimator (pairwise slopes, Kendall's tau, breakdown point 29.3%, median-unbiasedness), isotonic regression and the pool adjacent violators algorithm, Nadaraya–Watson kernel regression and its boundary bias, local linear regression and LOESS (tricube weights, robustness iterations, span and degree), smoothing splines and the roughness penalty, and how to choose among them.
---

Spearman's and Kendall's rank correlations ([3.6.8](/3.6.8)) measure how strongly two variables are associated, without assuming linearity or normality. They do not say what the relation looks like or predict $Y$ from $X$. This chapter extends the rank-based and local ideas of the course from association to the trend itself: we estimate an unknown function $g$ in

$$
Y_i=g(X_i)+\varepsilon_i,\qquad i=1,\dots,n,
$$

where the errors $\varepsilon_i$ are independent with center $0$, without assuming that $g$ belongs to a parametric family. This is **nonparametric regression** ([3.3.12](/3.3.12)). The methods are arranged by the strength of the constraint they place on $g$: the Theil–Sen estimator keeps a straight line but makes it robust; isotonic regression assumes only that $g$ is monotone; kernel regression, local linear regression (LOESS) and smoothing splines assume only that $g$ is smooth. The smoothers are the regression analogues of the density estimators of [3.6.13](/3.6.13), and they share the same issues: a smoothing parameter that trades bias against variance, and a boundary bias that local fitting removes. Quantile regression ([3.6.10](/3.6.10)) is the related method for conditional quantiles; the machine-learning view of the same local methods is in [4.6.4](/4.6.4).

## 14.1. From Rank Correlation to Nonparametric Regression

A correlation coefficient summarizes association by one number; a regression function describes the whole relation. The goals for the methods of this chapter are those of the rest of the course: no assumption of normality, no assumption of a particular functional form, and robustness to a few aberrant observations. Each method makes some assumption about $g$, and the choice among them is a choice of assumption:

| Method | Assumption on $g$ | Section |
|---|---|---|
| Theil–Sen | linear | 14.2 |
| isotonic regression | monotone | 14.3 |
| kernel regression (Nadaraya–Watson) | smooth | 14.4 |
| local linear regression, LOESS | smooth | 14.5 |
| smoothing spline | smooth, with a penalty on curvature | 14.6 |

## 14.2. The Theil–Sen Estimator

### 14.2.1. Definition

Least squares chooses the line that makes the residuals uncorrelated with $X$ in Pearson's sense; one gross error can rotate it arbitrarily, because its breakdown point is $1/n$ ([3.6.13](/3.6.13)). The Theil–Sen estimator replaces the average of squared residuals by medians of slopes.

**Definition 14.2.1 (Theil–Sen Estimator)** For data $(x_i,y_i)$, $i=1,\dots,n$, let $S_{ij}=(y_j-y_i)/(x_j-x_i)$ be the slopes of the lines through pairs of points with $x_i<x_j$. The **Theil–Sen estimator** of the slope is their median, and the intercept is the median of the shifted responses,

$$
\hat\beta=\operatorname*{median}_{i<j}S_{ij},\qquad\hat\alpha=\operatorname*{median}_{1\le i\le n}\bigl(y_i-\hat\beta x_i\bigr).
$$

(The slope was proposed by Theil in 1950 and studied by Sen in 1968, who allowed ties in $x$ by omitting pairs with $x_i=x_j$. Some software, such as `scipy.stats.theilslopes`, uses the intercept $\operatorname{median}(y)-\hat\beta\operatorname{median}(x)$ instead.)

With $n$ points there are up to $\binom n2$ slopes, so the computation is $O(n^2)$ by brute force (faster algorithms exist). The estimator uses only the order of the slopes, which is why it inherits the robustness of the median and its connection to Kendall's $\tau$.

**Theorem 14.2.1 (Properties of the Theil–Sen Estimator)** Let the $x_i$ be distinct.

1. $\hat\beta$ is the slope $b$ for which the residuals $e_i(b)=y_i-bx_i$ have zero **Kendall's tau** with $x$: the number of concordant pairs of $(x_i,e_i(b))$ equals the number of discordant pairs.
2. Its asymptotic breakdown point is $1-1/\sqrt2\approx0.293$.
3. If $Y_i=\alpha+\beta x_i+\varepsilon_i$ with $\varepsilon_1,\dots,\varepsilon_n$ i.i.d. from a continuous distribution symmetric about $0$, then $\hat\beta-\beta$ has a distribution symmetric about $0$, so $\hat\beta$ is median-unbiased: $\mathbb{P}(\hat\beta<\beta)=\mathbb{P}(\hat\beta>\beta)=1/2$.

**Proof** 1. For $x_i<x_j$, $e_j(b)-e_i(b)=(y_j-y_i)-b(x_j-x_i)$, so $(x_j-x_i)(e_j(b)-e_i(b))>0$ if and only if $S_{ij}>b$. The pair is therefore concordant exactly when its slope exceeds $b$ and discordant exactly when its slope is below $b$, and Kendall's tau of $(x,e(b))$ is zero exactly when as many slopes lie above $b$ as below it, that is, when $b$ is a median of the slopes.

2. Suppose a fraction $\varepsilon$ of the points is replaced by arbitrary values. A slope is contaminated if at least one of its two points is bad: there are about $\varepsilon(1-\varepsilon)n^2$ good–bad pairs and $\varepsilon^2n^2/2$ bad–bad pairs, out of about $n^2/2$ in all. The median can be carried away when half of the slopes are contaminated,

$$
\varepsilon(1-\varepsilon)n^2+\frac{\varepsilon^2n^2}2\ge\frac12\cdot\frac{n^2}2\iff\varepsilon^2-2\varepsilon+\frac12\le0,
$$
whose smaller root is $\varepsilon=1-1/\sqrt2$.

3. $S_{ij}-\beta=(\varepsilon_j-\varepsilon_i)/(x_j-x_i)$, so $\hat\beta-\beta$ is the median of these quantities, a fixed function $m(\varepsilon_1,\dots,\varepsilon_n)$ with $m(-\boldsymbol{\varepsilon})=-m(\boldsymbol{\varepsilon})$. By symmetry $-\boldsymbol{\varepsilon}$ has the same distribution as $\boldsymbol{\varepsilon}$, so $\hat\beta-\beta=m(\boldsymbol{\varepsilon})$ has the same distribution as $-(\hat\beta-\beta)$. Since the errors are continuous, $\mathbb{P}(\hat\beta=\beta)=0$, and the two remaining probabilities are equal. $\square$

Each slope $S_{ij}$ is symmetric about $\beta$ whenever the errors are i.i.d. (because $\varepsilon_j-\varepsilon_i$ is), but that alone does not make the median of the dependent slopes symmetric; the symmetry of the error distribution is what makes the joint argument work. Part 1 is the rank analogue of least squares: least squares makes the Pearson correlation between residuals and $x$ zero, Theil–Sen makes Kendall's tau zero. It also gives a confidence interval: inverting Kendall's test of $\tau(x,e(b))=0$ over $b$, exactly as the Wilcoxon interval of [3.6.4](/3.6.4) inverts the signed-rank test over the Walsh averages, gives an interval between two order statistics of the slopes. The breakdown point $29.3\%$ is the same as that of the Hodges–Lehmann estimator ([3.6.13](/3.6.13), Question 1), for the same reason.

### 14.2.2. Examples

**Example 14.2.1 (Ranks of Nine Athletes)** Nine athletes are ranked in the $100\,\mathrm{m}$ sprint ($x$) and in the long jump ($y$):

| Athlete | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| $x$ (100 m rank) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| $y$ (long jump rank) | 1 | 2 | 7 | 6 | 3 | 8 | 9 | 5 | 4 |

The $\binom92=36$ pairwise slopes are, in order,

$$
-4,-3,-2.5,-2,-1.5,-1.33,-1,-1,-0.5,-0.4,-0.4,-0.25,\ 0.25,0.29,0.33,0.33,0.375,0.5,0.5,0.5,0.57,0.67,1,1,1,1,1.33,1.4,1.4,1.5,1.67,2,3,3,5,5 .
$$

Twelve are negative and $24$ positive, so Kendall's $\tau=(24-12)/36=1/3$. The median of the $36$ slopes (the average of the $18$th and $19$th) is $\hat\beta=0.5$, and the shifted responses $y_i-0.5x_i$ are $0.5,1,5.5,4,0.5,5,5.5,1,-0.5$, with median $\hat\alpha=1$: the Theil–Sen line is $\hat y=1+0.5x$. Least squares gives $\hat y=2.75+0.45x$, and Pearson's (here equal to Spearman's) correlation is $0.45$. Dropping athlete 9 (last in the sprint but fourth in the long jump) changes the least squares slope to $0.75$ and the correlation to $0.63$, and the Theil–Sen slope to $0.83$.

Because the data are ranks, no observation can be a gross outlier, and both lines move by similar amounts when a point is removed: with $n=9$ every point matters. The strength of Theil–Sen shows when a few responses are far off, as in the next example.

**Example 14.2.2 (Gross Errors)** Thirty points are generated from $y=2+0.8x+\varepsilon$, $\varepsilon\sim\mathcal{N}(0,1)$. On the clean data the least squares slope is $0.77$ and the Theil–Sen slope $0.79$. When the three points with the largest $x$ are replaced by values near $0.5$, as if a recording device had failed at the end of the run, the least squares slope drops to $0.25$, while the Theil–Sen slope is $0.65$. The contamination ($10\%$ of the points) is below the breakdown point, so the Theil–Sen line is biased but stays close to the truth; it is not unaffected, because the bad points are clustered at one end and all pull in the same direction.

![Least squares and Theil–Sen lines for 30 points from $y = 2 + 0.8x + \varepsilon$. A: clean data. B: the three points with the largest $x$ replaced by gross errors (red); the least squares line is rotated, the Theil–Sen line much less.](./plots/theil-sen.py)

## 14.3. Isotonic Regression

### 14.3.1. The Problem

Sometimes the only thing we are prepared to assume is the direction of the relation: the response to a drug does not decrease with the dose, the probability of failure does not decrease with age, the growth of a plant does not decrease with time. A straight line is then too restrictive, and a polynomial may violate the monotonicity we know to hold.

**Definition 14.3.1 (Isotonic Regression)** Let $x_1<x_2<\dots<x_n$ with responses $y_1,\dots,y_n$. The **isotonic regression** of $y$ is the solution of

$$
\min_{m_1,\dots,m_n}\sum_{i=1}^n\bigl(y_i-m_i\bigr)^2\quad\text{subject to}\quad m_1\le m_2\le\dots\le m_n ,
$$
the least squares fit among all nondecreasing functions, $m_i=m(x_i)$. (With weights $w_i$, minimize $\sum_iw_i(y_i-m_i)^2$.)

The constraint set is a closed convex cone and the objective is strictly convex, so the solution exists and is unique. It is a step function, constant on blocks of consecutive points, and on each block it equals the mean of the responses in the block. It is computed by a simple algorithm.

**Algorithm 14.3.1 (Pool Adjacent Violators Algorithm)** (PAVA) Start with each observation as a block with value $y_i$.

1. Scan the blocks from left to right.
2. When a block has a larger value than the block to its right (an adjacent violator), pool the two into one block whose value is the (weighted) mean of their responses.
3. After pooling, compare the new block with the block to its left and pool again if they violate the order; repeat until the order holds there.
4. Continue the scan; when the right end is reached, the block values are the isotonic regression.

Each pooling reduces the number of blocks by one, so there are at most $n-1$ poolings and the algorithm runs in $O(n)$ time. The result can also be written as a min–max formula, $\hat m_i=\max_{s\le i}\min_{t\ge i}\bar y_{s:t}$, where $\bar y_{s:t}$ is the mean of $y_s,\dots,y_t$; that pooling preserves optimality follows from it, or from the Karush–Kuhn–Tucker conditions of the quadratic program.

**Example 14.3.1 (Pooling)** For $y=(10,20,12,30)$ at $x=1,2,3,4$: $10\le20$ is fine; $20>12$ is a violation, so the two are pooled into a block with value $(20+12)/2=16$; the sequence $10,16,16,30$ is nondecreasing, and $\hat m=(10,16,16,30)$.

For $y=(1,3,2,4,3.5,2.5,5)$ the backward check matters. Pooling $3,2$ gives $2.5,2.5$; next, $4>3.5$ gives the block $\{4,3.5\}$ with value $3.75$; then $3.75>2.5$ pools $\{4,3.5,2.5\}$ into $3.33$, which is not below the preceding block $2.5$, so no further pooling is needed; finally $5$ is fine. The isotonic regression is $(1,2.5,2.5,3.33,3.33,3.33,5)$.

:::

### 14.3.2. A Temperature Series

**Example 14.3.2 (Annual Mean Temperatures)** The figure below shows $80$ simulated annual mean temperatures between 1900 and 2025: an increasing trend $14+1.2\,(x-1900)/(40+x-1900)$, a slow oscillation of amplitude $0.15$ and noise with standard deviation $0.08$ (the model of the R code below). If physical reasoning tells us that the long-term level does not decrease, isotonic regression estimates it without any assumption about the shape of the increase. PAVA produces $17$ steps. Long horizontal stretches appear where the series oscillates: within such a stretch some years are colder than earlier ones, the violations are pooled, and the stretch is summarized by its mean. Jumps appear where the new values are so high that no earlier plateau can absorb them.

The plateaus have to be read with care. A plateau says that within that stretch the data give no evidence of a further increase, either because the level was really flat or because noise and oscillations mask a slow rise. In real records some plateaus are meaningful (observed global temperatures rose little between the 1940s and the 1970s, a period of growing aerosol emissions), but the step function cannot distinguish a real pause from noise, and it cannot show a temporary decrease at all: isotonic regression treats every decrease as noise to be averaged out.

```r
set.seed(42)
x <- seq(1900, 2025, length.out = 80)
true_trend <- 14 + 1.2 * (x - 1900) / (40 + (x - 1900))
y <- true_trend + sin(x / 2) * 0.15 + rnorm(length(x), sd = 0.08)
iso <- isoreg(x, y)              # PAVA; iso$yf holds the fitted values in the order of x
plot(iso)
```

:::

![Isotonic regression (PAVA, red steps) and Nadaraya–Watson kernel regression (blue, Gaussian kernel, the `ksmooth` bandwidth 15) for 80 simulated annual mean temperatures; the dotted line is the trend without the oscillation. The steps never decrease; the kernel curve also shows the local dips.](./plots/isotonic-kernel.py)

The estimator is consistent for a monotone $g$ (at rate $n^{-1/3}$ at a point where $g'>0$), needs no smoothing parameter, and is unaffected by any monotone change of scale of $x$, since only the order of the $x_i$ enters. Its weaknesses are the steps, which are artificial when $g$ is smooth, a bias at the two ends (the first and last blocks are pulled toward the data at the extremes, the "spiking" problem), and the assumption itself: if $g$ is not monotone, the fit is badly wrong.

## 14.4. Kernel Regression

### 14.4.1. The Nadaraya–Watson Estimator

Many relations are smooth but neither linear nor monotone: dose–response curves with a plateau or a toxic decline, growth curves, the acquisition of a skill, ecological patterns along a gradient. The simplest smoother estimates $g(x_0)$ by averaging the responses of the observations near $x_0$, giving more weight to nearer ones.

**Definition 14.4.1 (Kernel Regression)** Let $K$ be a kernel function and $h>0$ a bandwidth, $K_h(u)=K(u/h)/h$. The Nadaraya–Watson **kernel regression** estimator of $g(x_0)$ is

$$
\hat g(x_0)=\frac{\sum_{i=1}^nK_h(X_i-x_0)\,Y_i}{\sum_{i=1}^nK_h(X_i-x_0)} ,
$$
a weighted mean of the $Y_i$ with weights $K_h(X_i-x_0)$.

The estimator arises by plugging kernel density estimates into $g(x)=\mathbb{E}[Y\mid X=x]=\int yf(x,y)\,\mathrm{d}y/f_X(x)$: a product kernel estimate of the joint density in the numerator and the kernel density estimate of $f_X$ ([3.6.13](/3.6.13)) in the denominator give exactly this ratio. It is a *linear smoother*: $\hat g(x_0)=\sum_il_i(x_0)Y_i$ with weights $l_i(x_0)\ge0$ that sum to $1$ and do not depend on the $Y_i$.

The steps of a fit are: order the data by $x$; choose a kernel (Gaussian, Epanechnikov, tricube) and a bandwidth; at each point $x_0$ of a grid, compute the weights and the weighted mean; join the values. The bandwidth plays the same role as in density estimation. A small $h$ averages over few observations: the curve is wiggly, with small bias and large variance. A large $h$ averages over many: the curve is smooth, with small variance and large bias, and as $h\to\infty$ it tends to the constant $\bar Y$. The kernel matters much less. Unlike the line and the step function, the kernel estimate can follow any smooth shape: in the temperature series it shows both the slower rise after mid-century and local dips that the isotonic fit must average out.

In R, `ksmooth` computes the estimator. Its `bandwidth` argument is scaled so that the quartiles of the kernel lie at $\pm0.25\,\mathrm{bandwidth}$; for the normal kernel the standard deviation is therefore $0.25\times\mathrm{bandwidth}/0.6745\approx0.37\,\mathrm{bandwidth}$, about $5.6$ years for `bandwidth = 15`.

```r
kernel_fit <- ksmooth(x, y, kernel = "normal", bandwidth = 15, x.points = x)
plot(x, y)
lines(x, isoreg(x, y)$yf, type = "s", col = "red")    # isotonic regression
lines(kernel_fit, col = "blue")                       # Nadaraya-Watson
```

### 14.4.2. Boundary Bias

At the edges of the design the symmetric kernel window is cut off: near the smallest $x$ there are observations only to the right. If $g$ is increasing there, all the observations in the window have larger means than $g(x_0)$, and the local average overestimates $g$ at the left end; at the right end it underestimates. The fitted curve is flattened toward the interior at both ends, exactly where, in a time series, the initial baseline and the current state are of greatest interest. This is the **boundary bias** of [3.6.13](/3.6.13) in regression form.

**Proposition 14.4.1 (Bias of the Nadaraya–Watson Estimator)** Let the design have a density $f$ that is positive and continuous on $[a,b]$, let $g$ be twice continuously differentiable, and let $K$ be a symmetric density, $\mu_j^+=\int_0^\infty u^jK(u)\,\mathrm{d}u$. As $h\to0$ and $nh\to\infty$:

1. at an interior point, $\mathbb{E}\hat g(x_0)-g(x_0)\approx h^2m_2(K)\Bigl(\frac12g''(x_0)+\frac{g'(x_0)f'(x_0)}{f(x_0)}\Bigr)$, where $m_2(K)=\int u^2K$;
2. at the left end point $x_0=a$, $\mathbb{E}\hat g(a)-g(a)\approx h\,g'(a)\,\mu_1^+/\mu_0^+$, which is of order $h$.

**Proof** (Sketch.) Replacing the sums by their expectations, $\mathbb{E}\hat g(x_0)\approx\int K_h(t-x_0)g(t)f(t)\,\mathrm{d}t\big/\int K_h(t-x_0)f(t)\,\mathrm{d}t$. Substitute $t=x_0+hu$ and expand $g(x_0+hu)=g(x_0)+hug'(x_0)+\frac12h^2u^2g''(x_0)+\cdots$ and $f(x_0+hu)=f(x_0)+huf'(x_0)+\cdots$. In the interior the integrals run over all $u$, the terms with odd powers of $u$ vanish by symmetry, and collecting the terms of order $h^2$ gives part 1. At $x_0=a$ only $u\ge0$ contributes, the first-order term no longer vanishes, and the ratio is $g(a)+hg'(a)\mu_1^+/\mu_0^++O(h^2)$. $\square$

For the Gaussian kernel $\mu_1^+/\mu_0^+=\sqrt{2/\pi}\approx0.80$, so the bias at the boundary is about $0.80\,h\,g'(a)$. In the temperature series the trend has slope $0.03$ per year at 1900 and the kernel standard deviation is $5.6$ years, which predicts a bias of $0.80\times5.6\times0.03\approx0.13$; the fit gives $14.12$ at 1900 against a trend value of $14.00$. Part 1 shows a second weakness, present even in the interior: the term $g'f'/f$ makes the bias depend on the design density, so the estimate is distorted wherever the $x_i$ thin out.

## 14.5. Local Linear Regression and LOESS

### 14.5.1. Local Polynomials

The Nadaraya–Watson estimate is the minimizer $a$ of $\sum_iK_h(X_i-x_0)(Y_i-a)^2$: it fits a constant locally. The remedy for its bias is to fit a line instead.

**Definition 14.5.1 (Local Polynomial Regression)** For a point $x_0$, a kernel $K$, a bandwidth $h$ and a degree $p$, let $\hat\beta_0,\dots,\hat\beta_p$ minimize the locally weighted residual sum of squares

$$
\sum_{i=1}^nK_h(X_i-x_0)\Bigl(Y_i-\sum_{j=0}^p\beta_j(X_i-x_0)^j\Bigr)^2 .
$$
**Local polynomial regression** estimates $g(x_0)$ by $\hat g(x_0)=\hat\beta_0$ (and $g^{(j)}(x_0)$ by $j!\,\hat\beta_j$). The case $p=1$ is **local linear regression**; $p=0$ is the Nadaraya–Watson estimator.

The fit is a **weighted least squares** problem at each $x_0$, solved afresh as $x_0$ moves. The local slope $\hat\beta_1$ acts as a trend compensator: on the side of the boundary where data are missing, the fitted line extrapolates the trend of the data that are present instead of averaging it away.

**Theorem 14.5.1 (Local Linear Weights)** Write $w_i=K_h(X_i-x_0)$ and $S_k=\sum_iw_i(X_i-x_0)^k$. The local linear estimate is the linear smoother

$$
\hat g(x_0)=\sum_{i=1}^nl_i(x_0)Y_i,\qquad l_i(x_0)=\frac{w_i\bigl(S_2-(X_i-x_0)S_1\bigr)}{S_0S_2-S_1^2},
$$
whose weights satisfy $\sum_il_i(x_0)=1$ and $\sum_il_i(x_0)(X_i-x_0)=0$. Consequently it reproduces linear functions exactly, and its bias is $\frac12h^2g''(x_0)\,c(x_0)+o(h^2)$, of order $h^2$ both in the interior (where $c=m_2(K)$) and at the boundary (where $c$ is a constant depending on the truncated kernel), with no term involving the design density.

**Proof** The normal equations of the weighted least squares problem with regressors $1$ and $X_i-x_0$ give $\hat\beta_0=(S_2T_0-S_1T_1)/(S_0S_2-S_1^2)$ with $T_k=\sum_iw_i(X_i-x_0)^kY_i$, which is the stated formula. Then $\sum_il_i=(S_2S_0-S_1^2)/(S_0S_2-S_1^2)=1$ and $\sum_il_i(X_i-x_0)=(S_2S_1-S_1S_2)/(S_0S_2-S_1^2)=0$. If $g(x)=c_0+c_1(x-x_0)$, then $\hat g(x_0)=\sum_il_ig(X_i)=c_0=g(x_0)$ for noiseless data, so the expectation of $\hat g(x_0)$ is exact for every linear $g$, whether or not the window is symmetric. For a smooth $g$, expanding $g(X_i)$ to second order, the constant and linear terms are reproduced and only the quadratic remainder, of order $h^2$ inside a window of width $O(h)$, contributes to the bias. $\square$

The weights $l_i(x_0)$ can be negative near the boundary: this is how the local line extrapolates. The price of the correction is a larger variance at the edges, since the local slope is estimated from one-sided data. A local quadratic ($p=2$) also removes the curvature term in the interior bias and follows peaks and valleys better, but its variance at the boundary is larger still.

### 14.5.2. LOESS

The local linear idea was turned into a practical, robust procedure by Cleveland (1979, LOWESS for scatterplot smoothing) and Cleveland and Devlin (1988, LOESS for one or more predictors), the smoothers behind the curves added to residual plots in [3.3](/3.3).

**Definition 14.5.2 (Locally Weighted Regression)** **Locally weighted regression** (LOESS, LOWESS) estimates $g(x_0)$ by a local polynomial fit of degree $1$ or $2$ with

1. a nearest-neighbor window: for the span $\alpha\in(0,1]$, the $q=\lceil\alpha n\rceil$ observations nearest to $x_0$ are used, and $d_q(x_0)$ is the distance to the farthest of them;
2. tricube weights $w_i(x_0)=W\bigl(\lvert X_i-x_0\rvert/d_q(x_0)\bigr)$ with $W(u)=(1-u^3)^3$ for $0\le u<1$ and $W(u)=0$ for $u\ge1$;
3. optionally, robustness iterations that downweight observations with large residuals (Algorithm 14.5.1).

**Algorithm 14.5.1 (Robust LOESS)**

1. Compute the local fit at every $X_i$ with the tricube weights, and the residuals $e_i=Y_i-\hat g(X_i)$.
2. Let $s=\operatorname{median}_i\lvert e_i\rvert$ and compute robustness weights $r_i=B\bigl(e_i/(6s)\bigr)$ with the bisquare function $B(u)=(1-u^2)^2$ for $\lvert u\rvert<1$, $B(u)=0$ otherwise: residuals larger than six median absolute residuals get weight $0$, small residuals weight near $1$.
3. Refit with the weights $w_i(x_0)\,r_i$ and recompute the residuals.
4. Repeat steps 2–3 a few times (two or three iterations usually suffice).

The robustness step is an M-estimation with the bisquare $\psi$, computed by iteratively reweighted least squares as for the Huber estimator of [3.6.13](/3.6.13), and applied locally. The choice of the tricube weight has three reasons. Its support is compact, so each local fit involves only the $q$ neighbors (fast, and an outlier far from $x_0$ has exactly zero weight there, whereas a Gaussian kernel gives every point some weight). It decreases smoothly to zero, with continuous first and second derivatives at the edge of the window, so observations enter and leave the window gradually and the fitted curve is smooth. And it is nearly flat near the center, so the closest neighbors count almost equally.

The two tuning parameters are the degree and the span. Degree $1$ fits local lines: it corrects the boundary bias and stays relatively smooth. Degree $2$ fits local parabolas: it follows peaks and valleys better, but is more variable, especially at the boundaries. A larger span gives a smoother curve (more bias, less variance), a smaller span more local detail (less bias, more variance). The span can be chosen by eye for exploration or by **cross-validation** (or its generalized version) for estimation. Because the window contains a fixed fraction of the data, the effective bandwidth widens where the $x_i$ are sparse, as for the k-nearest-neighbor density estimate.

In R, `loess(y ~ x, span = 0.75, degree = 2)` is the default call; it does not iterate for robustness unless `family = "symmetric"` is given (then four iterations), while the older `lowess(x, y, f = 2/3, iter = 3)` fits local lines with three robustness iterations by default.

**Example 14.5.1 (Boundary Correction)** For the temperature series, a local linear LOESS fit with span $0.25$ and the Nadaraya–Watson fit of Section 14.4 agree in the interior. At the left end the trend value is $14.00$; Nadaraya–Watson gives $14.12$ and LOESS $14.04$. At the right end, where the trend has flattened, both are close to the trend value $14.91$ (Nadaraya–Watson $14.89$, LOESS $14.91$).

```r
nw_fit <- ksmooth(x, y, kernel = "normal", bandwidth = 15, x.points = x)
loess_fit <- loess(y ~ x, span = 0.25, degree = 1)    # local linear fit
loess_pred <- predict(loess_fit, newdata = data.frame(x = x))
plot(x, y)
lines(nw_fit, col = "blue")
lines(x, loess_pred, col = "red")
```

:::

![Boundary bias of kernel regression for the simulated temperature series: Nadaraya–Watson (local constant, blue) and local linear LOESS with tricube weights, span 0.25 (red), compared with the smooth trend (dotted). A: the whole series. B: the first 25 years, where the local constant fit is flattened toward the interior and the local line follows the trend.](./plots/boundary-loess.py)

## 14.6. Smoothing Splines

The smoothers so far control smoothness through the size of a window. A different approach controls it through a penalty, without any window.

**Definition 14.6.1 (Smoothing Spline)** For $\lambda>0$, the **smoothing spline** is the function $\hat m$ that minimizes, over all twice differentiable $m$ with $\int m''^2<\infty$,

$$
\sum_{i=1}^n\bigl(Y_i-m(X_i)\bigr)^2+\lambda\int\bigl(m''(x)\bigr)^2\,\mathrm{d}x .
$$

The first term measures the fit and the second the roughness of the curve, its total squared curvature; $\lambda$ sets the exchange rate between them. At the extremes:

- $\lambda\to0$: the penalty vanishes and, if the $X_i$ are distinct, the solution interpolates the data (the interpolating natural cubic spline, the smoothest interpolant): extreme overfitting.
- $\lambda\to\infty$: any curvature becomes infinitely expensive, the solution must have $m''=0$, so it is a straight line, and among lines it minimizes the residual sum of squares: the least squares line.

A remarkable fact, due to Reinsch (1967), is that the minimizer over this infinite-dimensional space is a natural **cubic spline** with knots at the distinct values $X_i$: cubic between consecutive knots, with continuous second derivative and linear beyond the extreme knots. The problem therefore reduces to a finite one, a penalized least squares problem for the spline coefficients, and the fitted values are a linear smoother $\hat{\boldsymbol{y}}=S_\lambda\boldsymbol{y}$. The trace of $S_\lambda$ is the effective degrees of freedom of the fit, decreasing from $n$ (interpolation) to $2$ (the line); R's `smooth.spline` chooses $\lambda$ by generalized cross-validation unless told otherwise.

![Smoothing splines for the simulated temperature series with three values of the penalty $\lambda$ (time in years): $\lambda = 0.5$ follows the oscillation and the noise, $\lambda = 500$ gives a smooth trend, $\lambda = 10^7$ is indistinguishable from the least squares line (dotted).](./plots/smoothing-spline.py)

The roughness penalty connects nonparametric regression with the **regularization** of modern statistics: **ridge regression** ([3.3.12](/3.3.12)) penalizes the size of the coefficients, the smoothing spline penalizes the curvature of the function, and both are **penalized likelihood** methods for normal errors. The same idea extends to generalized additive models, to more predictors (thin-plate splines) and to other penalties.

## 14.7. Choosing a Regression Method

| Method | Constraint on $g$ | Strengths | Weaknesses | Typical use |
|---|---|---|---|---|
| Theil–Sen (Definition 14.2.1) | linear | robust (breakdown $29.3\%$); linked to Kendall's $\tau$; median-unbiased under symmetric errors | only linear trends; not robust to many clustered outliers | linear trend in data with outliers (environmental trend analysis) |
| isotonic regression (Definition 14.3.1) | monotone | no smoothing parameter; invariant to monotone rescaling of $x$ | steps; cannot show a temporary decrease; spiking at the ends | dose–response, calibration, monotone trends known on scientific grounds |
| Nadaraya–Watson (Definition 14.4.1) | smooth | simple; any shape | boundary bias of order $h$; bias depends on the design density | smooth curves away from the edges, evenly spaced data |
| local linear, LOESS (Definitions 14.5.1, 14.5.2) | smooth | boundary bias of order $h^2$; adapts to the design; robust version available | choice of span and degree; larger variance at the edges | exploratory smoothing, residual plots, curves whose ends matter |
| smoothing spline (Definition 14.6.1) | smooth | no window; $\lambda$ by cross-validation; links to regularization | less local; not robust to outliers | smooth estimation with automatic tuning |

The order of the table is the order of decreasing constraint. A stronger constraint gives a more stable estimate when it is right and a misleading one when it is wrong, which is the bias–variance trade-off once again. Every smoother has a parameter that sets this balance: the bandwidth $h$, the span $\alpha$, the penalty $\lambda$ (and the number of neighbors $k$ or the bin width in [3.6.13](/3.6.13)). When interest lies in the spread or the tails of $Y$ given $x$ rather than its center, quantile regression ([3.6.10](/3.6.10)) is the appropriate tool.

## Summary

- Nonparametric regression estimates $g$ in $Y=g(X)+\varepsilon$ under assumptions of decreasing strength: linear, monotone, smooth.
- **Theil–Sen estimator** (Definition 14.2.1): median of the pairwise slopes; it makes Kendall's $\tau$ between residuals and $x$ zero, has breakdown point $1-1/\sqrt2\approx29.3\%$, and is median-unbiased under symmetric i.i.d. errors (Theorem 14.2.1). Athletes: $\hat y=1+0.5x$, $\tau=1/3$ (Example 14.2.1); three gross errors in thirty points rotate least squares to slope $0.25$, Theil–Sen to $0.65$, against $0.8$ (Example 14.2.2).
- **Isotonic regression** (Definition 14.3.1): least squares under monotonicity; a step function of block means, computed by the **pool adjacent violators algorithm** (Algorithm 14.3.1) in $O(n)$; $(10,20,12,30)\mapsto(10,16,16,30)$ (Example 14.3.1). Plateaus pool local violations and cannot show real decreases.
- **Kernel regression** (Definition 14.4.1): a locally weighted mean; bandwidth controls the bias–variance trade-off; **boundary bias** of order $h$, about $0.80\,h\,g'$ for the Gaussian kernel, and a design-dependent interior bias (Proposition 14.4.1).
- **Local linear regression** (Definition 14.5.1): a local line instead of a local mean; its weights reproduce linear functions, so the bias is of order $h^2$ also at the boundary (Theorem 14.5.1). **LOESS** (Definition 14.5.2, Algorithm 14.5.1): nearest-neighbor span, tricube weights, degree 1 or 2, bisquare robustness iterations.
- **Smoothing spline** (Definition 14.6.1): least squares plus $\lambda\int m''^2$; a natural cubic spline; $\lambda\to0$ interpolates, $\lambda\to\infty$ gives the least squares line; a form of regularization.
- Choice: Section 14.7.

## Questions

1. For the athletes of Example 14.2.1, verify that Kendall's $\tau$ between $x$ and the residuals $y_i-0.5x_i$ is nearly zero, and explain why it is not exactly zero.

   **Answer** By Theorem 14.2.1, the pair $(i,j)$ is concordant for $(x,e(b))$ when $S_{ij}>b$ and discordant when $S_{ij}<b$. With $b=0.5$, $17$ slopes are smaller than $0.5$, $16$ larger and $3$ equal to it. So there are $16$ concordant and $17$ discordant pairs and $3$ pairs with tied residuals: $\tau_a=(16-17)/36\approx-0.028$ (software reports the tie-corrected $\tau_b\approx-0.029$). It cannot be exactly zero: for $b$ just below $0.5$ there are $19$ slopes above and $17$ below ($\tau=2/36$), for $b$ just above $0.5$ there are $16$ above and $20$ below ($\tau=-4/36$), so $\tau(b)$ jumps over $0$ at $b=0.5$. The estimating equation "$\tau=0$" is solved in the sense of a sign change, as the median of a discrete set solves "as many values above as below" only approximately when values are tied.
2. Apply PAVA to $y=(5,3,4,2,6)$ at $x=1,\dots,5$.

   **Answer** $5>3$: pool into $\{5,3\}$ with value $4$. Next $4$: the block value $4$ is not larger, so $4$ stays a block of its own. Next $2$: $4>2$, pool $\{4,2\}$ into $3$; now the preceding block $\{5,3\}$ has value $4>3$, so pool again: $\{5,3,4,2\}$ has value $3.5$. Finally $6>3.5$ is fine. The isotonic regression is $(3.5,3.5,3.5,3.5,6)$, with residual sum of squares $1.5^2+0.5^2+0.5^2+1.5^2+0=5$.
3. Suppose $g(x)=\alpha+\beta x$ is linear, the design is uniform on $[0,1]$ and the kernel is Gaussian. What are the approximate biases of the Nadaraya–Watson and local linear estimates at $x_0=0$, $x_0=0.5$ and $x_0=1$?

   **Answer** Local linear: zero at every point, since its weights reproduce linear functions exactly (Theorem 14.5.1). Nadaraya–Watson in the interior: by Proposition 14.4.1 the bias is $h^2m_2(K)(g''/2+g'f'/f)=0$, because $g''=0$ and the uniform design has $f'=0$; so at $0.5$ there is essentially no bias. At $x_0=0$ the bias is about $+0.80\,h\beta$, and at $x_0=1$ about $-0.80\,h\beta$ (the mirror image): the curve is flattened toward the interior at both ends. For $\beta=1$ and $h=0.1$ that is $\pm0.08$, a sizable error for a straight line that least squares would fit without bias.
4. Show that as $\lambda\to\infty$ the smoothing spline tends to the least squares line.

   **Answer** Let $L$ be the least squares line and $\hat m_\lambda$ the smoothing spline. Since $L''=0$, the objective at $L$ is $\mathrm{RSS}(L)$, so $\mathrm{RSS}(\hat m_\lambda)+\lambda\int\hat m_\lambda''^2\le\mathrm{RSS}(L)$. Hence $\int\hat m_\lambda''^2\le\mathrm{RSS}(L)/\lambda\to0$: the curvature of the spline disappears. Decompose $\hat m_\lambda$ into its least squares linear part and the rest; the rest is controlled by $\int\hat m_\lambda''^2$ and tends to $0$ at the data points, so $\hat m_\lambda$ tends to some line, and since $\mathrm{RSS}(\hat m_\lambda)\le\mathrm{RSS}(L)$, which is the smallest residual sum of squares of any line, the limit must be $L$ (the least squares line is unique when the $X_i$ are not all equal).
5. For each situation, choose a method from Section 14.7 and state the assumption it makes. (a) Annual counts of a bird species at a monitoring site over $25$ years, with two years in which the count was misrecorded; the question is whether there is a linear trend. (b) The proportion of animals responding at six increasing doses of a drug. (c) A scatter plot of residuals against fitted values from a regression, to look for curvature. (d) Air pollution recorded hourly, where the most recent level is of main interest.

   **Answer** (a) Theil–Sen (with Kendall's test for the trend): a linear trend, errors independent; robust to the two misrecorded counts, which least squares would let rotate the line. (b) Isotonic regression (weighted by the numbers of animals): the response does not decrease with dose; no shape beyond that, and no smoothing parameter to choose with only six points. (c) LOESS (local linear or quadratic, with robustness iterations): only smoothness, and the robust version keeps single large residuals from creating spurious bumps. (d) A local linear fit, LOESS or local linear kernel regression: the quantity of interest is at the right boundary, where the Nadaraya–Watson estimate is biased toward earlier values and a local line follows the recent trend.
