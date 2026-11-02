---
title: Descriptive Statistics and Data Display
description: Measures of location (mean, median, mode, geometric mean), measures of spread (range, interquartile range, standard deviation, coefficient of variation, MAD), quantiles and medical reference intervals, skewness and kurtosis, z-scores, frequency tables and statistical graphics (histograms, stem-and-leaf plots, box plots, QQ plots), and the identification and handling of outliers, illustrated with the FEV and birthwt data.
source_hash: 2f6b5d6c0edb
---

When we receive a dataset, the first step is not to run a test but to look at it: where the data are concentrated, how widely they are spread, what shape the distribution has, and whether any values are implausible. Descriptive statistics answers these questions with a few numbers and a few graphs. It determines all later choices: whether skewed data are summarized by the median or the mean, whether to take logarithms, whether methods based on the normal distribution can be used; it is also the best opportunity to discover data entry errors and unexpected patterns. This chapter follows the two datasets introduced in [7.7.1](/7.7.1): the lung function (FEV) of 654 children and the birth weight (birthwt) of 189 newborns, with antibody titers and ELISA replicate wells as laboratory examples. In the FEV plots we see for the first time the source of the paradox "smoking children have better lung function". The mathematical properties of sample moments, order statistics and the empirical distribution function are in [3.2.1](/3.2.1); this chapter treats their use, and their pitfalls, with biomedical data.

## 2.1. Measures of Location

A measure of location (central tendency) represents the "typical value" of the data by one number. Let $x_1, \dots, x_n$ be a sample and $x_{(1)} \le \cdots \le x_{(n)}$ the sorted values (the order statistics).

### 2.1.1. The Arithmetic Mean

The **sample mean** $\bar x = \frac{1}{n}\sum_{i=1}^n x_i$ is the most common measure of location, often called simply the mean. It is the "center of gravity" of the data: the deviations sum to zero, $\sum_i (x_i - \bar x) = 0$; it is also the value of $c$ that minimizes the sum of squared deviations $\sum_i (x_i - c)^2$. The mean uses every observation, is convenient algebraically (the mean of two pooled groups is the average of the two group means weighted by sample size), and is an unbiased estimator of the population mean. Its disadvantage is sensitivity to extreme values: changing a single observation to an arbitrarily large value makes the mean arbitrarily large. In the language of robust statistics, the breakdown point of the mean is 0.

The mean of the FEV data is $2.637\,\mathrm{L}$, and the mean birth weight in birthwt is $2945\,\mathrm{g}$.

### 2.1.2. The Median

The **sample median** is the value in the middle of the ordered data: $x_{((n+1)/2)}$ for odd $n$, and the average $\frac12\bigl(x_{(n/2)} + x_{(n/2+1)}\bigr)$ of the two middle values for even $n$. It depends only on the ordering of the data and is insensitive to extreme values: to push the median arbitrarily far one must change half of the data (breakdown point 0.5). The price is that it is almost unaffected by data other than the middle values, so when the data are approximately normal its sampling fluctuation is larger than that of the mean ([7.7.8](/7.7.8) discusses efficiency). The median of FEV is $2.548\,\mathrm{L}$ and the median birth weight is $2977\,\mathrm{g}$.

The median is the natural summary of ordinal data (pain scores, tumor stages) and also suits skewed continuous data (length of hospital stay, income, survival time). The median lethal dose $\mathrm{LD}_{50}$ in pharmacology is the median of the distribution of lethal doses ([7.7.14](/7.7.14)).

### 2.1.3. The Mode

**Definition 2.1.1 (Mode)** The value that occurs most often in a sample is the **mode**.

The mode may not exist (every value occurs once) or may not be unique (several values tie for the highest count). A distribution with one peak is called unimodal, and one with two peaks bimodal. The mode is best suited to nominal variables (the most common blood group) and to discrete variables with few values: in birthwt, the mode of the number of first-trimester visits `ftv` is 0 (100 mothers made no visit at all). Observed values of a continuous variable almost never repeat, so one can only speak of the peaks of a histogram or a density curve.

### 2.1.4. The Geometric Mean and the Harmonic Mean

Much laboratory data change by multiples: antibody titers and minimum inhibitory concentrations (MIC) are measured by serial dilution and take the values $1{:}4, 1{:}8, 1{:}16, \dots$; bacterial counts, viral loads and gene expression levels span several orders of magnitude. For such data "a difference of a factor of two" is more meaningful than "a difference of so many units".

**Definition 2.1.2 (Geometric Mean and Harmonic Mean)** The **geometric mean** of positive numbers $x_1, \dots, x_n$ is

$$
G = \sqrt[n]{x_1 x_2 \cdots x_n} = \exp\Bigl(\frac1n \sum_{i=1}^n \ln x_i\Bigr),
$$
the antilogarithm of the arithmetic mean of the logarithms. The **harmonic mean** is the reciprocal of the arithmetic mean of the reciprocals, $H = n \big/ \sum_{i=1}^n x_i^{-1}$.

For positive numbers we always have $H \le G \le \bar x$, with equality if and only if all $x_i$ are equal (the arithmetic–geometric–harmonic mean inequality); the more spread out the data, the further apart the three means are:

| Data | Arithmetic mean | Geometric mean | Harmonic mean |
|---|---|---|---|
| 10, 10, 10, 10 | 10 | 10.00 | 10.00 |
| 9, 10, 10, 11 | 10 | 9.97 | 9.95 |
| 5, 10, 10, 15 | 10 | 9.31 | 8.57 |
| 1, 2, 18, 19 | 10 | 5.11 | 2.49 |

**Example 2.1.1 (Antibody titers)** The serum antibody titers of 112 children one month after vaccination were: 1 child 1:4, 3 children 1:8, 15 children 1:16, 32 children 1:32, 43 children 1:64, 11 children 1:128, 5 children 1:256, 2 children 1:512. Taking logarithms to base 2 (the $\log_2$ of the reciprocal titers are 2, 3, …, 9),

$$
\overline{\log_2 x} = \frac{1\times2 + 3\times3 + 15\times4 + 32\times5 + 43\times6 + 11\times7 + 5\times8 + 2\times9}{112} = \frac{624}{112} = 5.571,
$$
the geometric mean is $G = 2^{5.571} = 47.6$, reported as a mean titer of about 1:48. The arithmetic mean is 69.3, pulled up by a few high titers and not representative of a typical child; the median is 64 (1:64). The figure below shows that on the log scale the dilutions are equally spaced, the distribution is nearly symmetric, and the geometric mean falls right at the center.

![Antibody titers of 112 children after vaccination. A: on the linear scale the distribution is right-skewed, and the arithmetic mean (69.3) is pulled up by a few high titers. B: on the $\log_2$ scale the dilutions are equally spaced and the distribution is approximately symmetric; the mean of the $\log_2$ titers is 5.57, whose antilogarithm is the geometric mean 47.6 (about 1:48)](./plots/geometric-mean.py)

The geometric mean is appropriate when the data are approximately log-normally distributed (approximately normal after taking logarithms, [7.7.4](/7.7.4)) or change by multiples; it cannot be used directly when the data contain zeros or negative numbers. The harmonic mean is used to average quantities of the "rate" type; its most common use is to summarize the "average sample size" when the groups have unequal sizes (the Tukey–Kramer method in [7.7.12](/7.7.12)).

### 2.1.5. Choosing a Measure of Location

| Data | Recommended | Reason |
|---|---|---|
| Symmetric, approximately normal continuous variables (birth weight, height) | Mean (with the standard deviation) | Uses all the information and is convenient for inference |
| Skewed continuous variables (length of stay, the high end of FEV, income) | Median (with the interquartile range) | Unaffected by the long tail |
| Multiplicative, log-normal (titers, concentrations, cell counts) | Geometric mean (with the geometric standard deviation or an interval on the log scale) | Symmetric on the log scale |
| Ordinal variables | Median | The mean requires equal spacing |
| Nominal variables | Mode, proportion in each category | Only categories |

In a right-skewed distribution mean > median > mode, and in a left-skewed distribution the order is reversed (figure below). The mean of FEV (2.637) is slightly larger than the median (2.548), indicating mild right skew; the mean birth weight (2945) is slightly smaller than the median (2977), mild left skew, because a few premature babies have very low weights.

![The positions of the mode, median and mean in left-skewed, symmetric and right-skewed distributions (densities of Beta distributions, computed exactly). The long tail of a right-skewed distribution pulls the mean to the right of the median, and the median lies to the right of the mode; in a left-skewed distribution the order is reversed](./plots/skew-location.py)

## 2.2. Measures of Spread

Two sets of data may have the same mean and completely different spread. Measures of spread describe how widely the data are scattered.

### 2.2.1. Range and Interquartile Range

The **range** $R = x_{(n)} - x_{(1)}$ is simple to compute, but it is determined by the two most extreme values only and increases with sample size (the larger the sample, the more likely extreme values are drawn), so ranges from samples of different sizes cannot be compared. The range of FEV is $5.793 - 0.791 = 5.002\,\mathrm{L}$.

**Definition 2.2.1 (Interquartile Range)** The difference between the third and the first quartile, $\mathrm{IQR} = Q_3 - Q_1$, is the **interquartile range**; it is the extent covered by the middle 50% of the data.

The interquartile range is unaffected by the 25% of data at each end and is the companion measure of spread to the median. For FEV, $Q_1 = 1.98$, $Q_3 = 3.12$ and $\mathrm{IQR} = 1.14\,\mathrm{L}$ (the computation of quartiles is in Section 2.3).

### 2.2.2. Variance and Standard Deviation

The **variance** and the **standard deviation** measure spread around the mean:

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar x)^2, \qquad s = \sqrt{s^2}.
$$

The numerator $\sum_i (x_i - \bar x)^2$ is called the sum of squared deviations from the mean (corrected sum of squares). The denominator is $n-1$ rather than $n$ because the deviations $x_i - \bar x$ are subject to the constraint $\sum_i (x_i - \bar x) = 0$, so only $n-1$ of them can vary freely (the degrees of freedom are $n-1$); the **sample variance** defined this way is an unbiased estimator of the population variance $\sigma^2$ ([3.2.3](/3.2.3)), whereas dividing by $n$ is systematically too small. The standard deviation has the same unit as the original data and is therefore easier to interpret than the variance: for FEV $s = 0.867\,\mathrm{L}$, and for birth weight $s = 729\,\mathrm{g}$.

Two useful properties: if $y_i = a x_i + b$ then $\bar y = a\bar x + b$ and $s_y = \lvert a\rvert s_x$. Converting height from inches to centimeters ($a = 2.54$): in the FEV data the mean height $61.14\,\mathrm{in} = 155.3\,\mathrm{cm}$ and the standard deviation $5.70\,\mathrm{in} = 14.5\,\mathrm{cm}$; a shift ($b$) does not change the spread.

The formula $\sum_i (x_i - \bar x)^2 = \sum_i x_i^2 - n\bar x^2$, commonly used in hand calculation, is numerically unstable: when the mean is much larger than the standard deviation (as for birth weight in g), subtracting two large numbers loses significant digits. Software uses the two-pass algorithm, which first finds the mean and then the deviations, or other stable algorithms.

### 2.2.3. Robust Measures of Spread

**Definition 2.2.2 (Mean Absolute Deviation and Median Absolute Deviation)** The quantity $\frac1n\sum_i \lvert x_i - \bar x\rvert$ is the **mean absolute deviation**; the median of the absolute deviations, $\operatorname{MAD} = \operatorname{median}_i \lvert x_i - \operatorname{median}(x)\rvert$, is the **median absolute deviation**.

The mean absolute deviation is intuitive, but absolute values are inconvenient algebraically and it is rarely used for inference. The MAD has breakdown point 0.5 and is a robust alternative to the standard deviation: for normal data $1.4826 \times \operatorname{MAD}$ estimates $\sigma$ ($1.4826 = 1/\Phi^{-1}(0.75)$), and the robust $z$-score used for outliers is often $(x - \operatorname{median})/(1.4826\,\operatorname{MAD})$. The MAD of FEV is $0.571\,\mathrm{L}$, and $1.4826 \times 0.571 = 0.846\,\mathrm{L}$ is close to $s = 0.867\,\mathrm{L}$; when the data are contaminated by gross errors, the two differ greatly.

### 2.2.4. Coefficient of Variation and Assay Precision

Standard deviations of variables with different units, or with widely different means, cannot be compared directly. The **sample coefficient of variation** $\mathrm{CV} = s/\bar x$ (often expressed as a percentage) is a dimensionless relative spread and is meaningful only for positive variables on a ratio scale.

**Example 2.2.1** For 40 seven-year-old children in a region, the mean height is $121.48\,\mathrm{cm}$ with a standard deviation of $4.65\,\mathrm{cm}$, and the mean weight is $22.18\,\mathrm{kg}$ with a standard deviation of $2.35\,\mathrm{kg}$. The $\mathrm{CV}$ of height is $4.65/121.48 = 3.83\%$ and that of weight is $2.35/22.18 = 10.60\%$: the relative variation of weight among children of the same age is about 3 times that of height.

The coefficient of variation is the standard measure of the precision of laboratory assays. The CV between replicate wells of the same sample on the same plate is called the intra-assay (within-plate) CV, and the CV between measurements on different days or in different batches is the inter-assay CV; immunoassays such as ELISA usually require an intra-assay CV < 10% and an inter-assay CV < 15%.

**Example 2.2.2 (Replicate wells of an ELISA)** The DNase data are an ELISA for rat serum DNase: 11 independent runs, each with 8 concentrations and two replicate wells per concentration. For each of the 88 pairs of replicate wells we compute the CV between the two wells; the median CV at each concentration lies between 0.8% and 1.8%, rising to 7.4% at the lowest concentration (0.049 ng/mL), and a few pairs exceed 20%. At the low end the optical density is close to the background; the absolute error is unchanged while the signal is small, so the relative error grows: this is the origin of the detection limit ([7.7.11](/7.7.11)).

![Precision of an ELISA (DNase data: 11 independent runs, 8 concentrations, two replicate wells per concentration; Davidian and Giltinan 1995). A: optical density against concentration in run 1; the two points at each concentration are replicate wells. B: the between-well CV of all 88 pairs of replicates; the median CV is 1%–2% at most concentrations and rises to about 7% at the lowest concentration, where the signal is close to the background](./plots/assay-precision.py)

### 2.2.5. Standard Deviation and Standard Error

The standard deviation describes variation between individuals, whereas the **standard error** $\mathrm{SE} = s/\sqrt n$ describes the sampling error of the sample mean as an estimate of the population mean ([7.7.4](/7.7.4)). As the sample size grows, the standard deviation settles near $\sigma$ while the standard error tends to 0. They answer different questions: describing the characteristics of the subjects ("the birth weight of the newborns was $2945 \pm 729\,\mathrm{g}$") calls for the standard deviation; reporting the precision of an estimate calls for the standard error or, better, a confidence interval ("mean weight $2945\,\mathrm{g}$, 95% confidence interval 2840–3049 g"). Using the smaller standard error in place of the standard deviation to "beautify" the spread is a common error in papers; figure and table legends must state what the error bars are.

### 2.2.6. Spread of Categorical Variables

A nominal variable has no mean or variance, but we can still ask whether the categories are evenly distributed. Let the proportions of $k$ categories be $p_1, \dots, p_k$; the index of qualitative variation

$$
D = \frac{k}{k-1}\Bigl(1 - \sum_{j=1}^k p_j^2\Bigr)
$$
is 0 when all individuals belong to one category and 1 when all category frequencies are equal. In birthwt the frequencies of the mother's race are 96, 26, 67 ($k = 3$) and $D = 0.90$: the three categories are quite dispersed. The quantity $1 - \sum p_j^2$ is the Simpson diversity index in ecology and the expected heterozygosity at a locus in population genetics.

## 2.3. Quantiles and Reference Intervals

### 2.3.1. Percentiles

Quantiles cut the ordered data in given proportions. The $p$th percentile $P_p$ is the value below which about $p\%$ of the data lie; $P_{25} = Q_1$, $P_{50}$ = the median and $P_{75} = Q_3$ are called the quartiles, and there are also tertiles, quintiles and deciles.

**Definition 2.3.1 (Sample Percentile)** Let $x_{(1)} \le \cdots \le x_{(n)}$ and $0 < p < 100$. If $np/100$ is not an integer, let $k$ be the largest integer not exceeding it; the $p$th **sample percentile** is $x_{(k+1)}$. If $np/100 = k$ is an integer, it is $\frac12\bigl(x_{(k)} + x_{(k+1)}\bigr)$.

This definition is the inverse of the empirical distribution function (averaging at the jumps), and for $p = 50$ it gives the usual median. For small samples, different software uses different interpolation rules and gives slightly different quartiles:

| Quartiles of FEV | $Q_1$ | Median | $Q_3$ |
|---|---|---|---|
| Definition 2.3.1 (R `type = 2`, the SAS default, NumPy `averaged_inverted_cdf`) | 1.979 | 2.548 | 3.120 |
| Linear interpolation (the default of R, NumPy, pandas and Excel; R `type = 7`) | 1.981 | 2.548 | 3.119 |
| `median_unbiased` (R `type = 8`) | 1.978 | 2.548 | 3.120 |

With $n = 654$ the differences are in the third decimal place; with a dozen observations they can be noticeable. There is no right or wrong among these differences, but a report should be consistent and, where necessary, state the algorithm.

### 2.3.2. The Five-Number Summary and the Box Plot

Tukey's five-number summary (minimum, $Q_1$, median, $Q_3$, maximum) describes location, spread and skewness with five numbers, and the **box plot** is its graphical form: the box extends from $Q_1$ to $Q_3$, the line in the box is the median, the two whiskers extend outward to the farthest observations within $1.5\,\mathrm{IQR}$ of the box, and more distant points are drawn individually (Section 2.7). If the upper whisker and the upper half of the box are longer than the lower, the distribution is right-skewed; otherwise left-skewed. FEV by smoking status:

| FEV / L | Minimum | $Q_1$ | Median | $Q_3$ | Maximum |
|---|---|---|---|---|---|
| Nonsmokers (589) | 0.791 | 1.920 | 2.465 | 3.048 | 5.793 |
| Smokers (65) | 1.694 | 2.795 | 3.169 | 3.751 | 4.872 |

### 2.3.3. Medical Reference Intervals

The "normal range" on a clinical laboratory report comes from the distribution in a healthy population.

**Definition 2.3.2 (Reference Interval)** The middle 95% (from the 2.5th to the 97.5th percentile) of the distribution of an index measured in a well-defined healthy reference population is the **reference interval** (reference range) of that index.

There are two methods of estimation: the nonparametric method takes the sample $P_{2.5}$ and $P_{97.5}$ directly, requires no assumption on the shape of the distribution but needs many reference individuals (clinical laboratory guidelines recommend at least 120 per partition); the parametric method takes $\bar x \pm 1.96\,s$ when the data (or their logarithms) are approximately normal. There are several easy misunderstandings: by definition 5% of healthy people fall outside the interval, and a person undergoing 20 independent tests has a probability of $1 - 0.95^{20} = 64\%$ that at least one is "abnormal"; and "within the reference interval" does not mean free of disease. In addition, reference values often vary with age, sex and height and must be given by partition or by regression (the reference equations of lung function are regressions of FEV on age, height and sex, [7.7.10](/7.7.10)).

**Example 2.3.1** In the FEV data there are 76 nonsmoking 10-year-old children, with mean FEV $2.666\,\mathrm{L}$ and standard deviation $0.533\,\mathrm{L}$. The nonparametric 95% reference interval is 1.67–3.80 L, and the normal method gives $2.666 \pm 1.96 \times 0.533$, that is 1.62–3.71 L; the data are mildly right-skewed (skewness 0.45), and the normal method on the log scale gives 1.76–3.89 L. The 76 children are fewer than the recommended 120, and the differences among the three methods reflect the imprecise estimation of the endpoints; actual reference equations for lung function are based on tens of thousands of healthy people.

## 2.4. The Shape of a Distribution

### 2.4.1. Skewness and Kurtosis

**Skewness** measures the asymmetry of a distribution:

$$
g_1 = \frac{\frac1n\sum_i (x_i - \bar x)^3}{\bigl[\frac1n\sum_i (x_i - \bar x)^2\bigr]^{3/2}},
$$
which is 0 for a symmetric distribution, positive for right skew (a long right tail) and negative for left skew. **Kurtosis** measures the heaviness of the tails: $\frac1n\sum_i (x_i-\bar x)^4 \big/ \bigl[\frac1n\sum_i (x_i-\bar x)^2\bigr]^2$ equals 3 for the normal distribution, so one usually reports the excess kurtosis, with 3 subtracted, which is 0 for the normal distribution; a positive value means heavier tails than the normal (more extreme values) and a negative value lighter tails.

The literature and software follow two conventions for kurtosis: some report the value without subtracting 3 (3 for the normal), others report the excess kurtosis (0 for the normal); `scipy.stats.kurtosis` gives the excess kurtosis by default and the value without subtracting 3 with `fisher=False`. When reading results, first check which one is used. For FEV the skewness is 0.66 and the excess kurtosis is 0.30 (3.30 without subtracting 3); for birth weight the skewness is $-0.21$ and the excess kurtosis is $-0.11$, close to normal. Skewness and kurtosis themselves have large sampling fluctuation and are only a rough guide in small samples; the shape is judged mainly from graphs (Section 2.6).

### 2.4.2. Common Distribution Shapes

Besides the symmetric bell shape, biomedical data commonly show: right-skewed distributions (concentrations, incubation periods, length of stay, counts); left-skewed distributions (indices with an upper bound, such as scores close to the maximum or the gestational age of term births); bimodal distributions (two subpopulations mixed together, such as the heights of men and women combined, or drug concentrations in fast and slow metabolizers); J-shaped and U-shaped distributions (age-specific mortality is high in infancy and old age and low in between). A bimodal shape often suggests subpopulations that should be analyzed separately.

### 2.4.3. The z-score

**Definition 2.4.1 (z-score)** The **z-score** (standard score) of an observation $x$ relative to reference data with mean $\bar x$ and standard deviation $s$ is $z = (x - \bar x)/s$, the number of standard deviations by which $x$ deviates from the mean.

The $z$-score is dimensionless and can compare the relative positions of observations of different dimensions and distributions in their respective groups. Pediatricians evaluate growth by the $z$-scores of height-for-age and weight-for-age (the World Health Organization growth standards define stunting as $z < -2$), and the T-score in a bone density report is a $z$-score relative to young adult reference values. If the reference distribution is approximately normal, $z$ can be converted into a percentile ([7.7.4](/7.7.4)).

**Example 2.4.1** A nonsmoking 10-year-old girl has an FEV of $1.80\,\mathrm{L}$. Relative to the reference group of Example 2.3.1, $z = (1.80 - 2.666)/0.533 = -1.63$; if the distribution is approximately normal, about 5% of children of her age are below her. She is still within the 95% reference interval but close to its lower limit, and should be judged together with her height (a short child has small lungs).

### 2.4.4. The Log Transformation

Right-skewed positive data often become nearly symmetric after taking logarithms: the logarithm turns multiplication into addition and multiples into equal differences. In the figure below the skewness of FEV falls from 0.66 to $-0.21$. The mean on the log scale, back-transformed, is the geometric mean (Definition 2.1.2), and a difference on the log scale, back-transformed, is a ratio ("by how many times the FEV of smokers exceeds that of nonsmokers"), an interpretation that is useful in regression ([7.7.10](/7.7.10)). When the data contain zeros (counts, undetected values), $\log(x + c)$ is often used, but the result depends on the choice of $c$ ([7.7.20](/7.7.20) discusses better approaches for count data).

## 2.5. Grouped Data and Frequency Tables

**Definition 2.5.1 (Frequency Table and Histogram)** Dividing the range of a numerical variable into adjacent class intervals and listing for each the number of observations (frequency), the proportion (relative frequency) and the cumulative proportion gives a **frequency table**; adjacent rectangles with the class intervals as bases and areas representing the frequencies (or relative frequencies) form a **histogram**.

To make a frequency table: find the range; choose the number and width of the classes (round numbers; the number of classes is usually 5–20, with Sturges' rule $1 + \log_2 n$ or the Freedman–Diaconis rule, class width $2\,\mathrm{IQR}/n^{1/3}$, as a starting point); specify that each class includes its left endpoint and excludes its right so that each observation falls in exactly one class; count. FEV in classes of 0.5 L:

| FEV / L | Frequency | Relative frequency | Cumulative proportion |
|---|---|---|---|
| [0.5, 1.0) | 3 | 0.5% | 0.5% |
| [1.0, 1.5) | 37 | 5.7% | 6.1% |
| [1.5, 2.0) | 127 | 19.4% | 25.5% |
| [2.0, 2.5) | 147 | 22.5% | 48.0% |
| [2.5, 3.0) | 136 | 20.8% | 68.8% |
| [3.0, 3.5) | 103 | 15.7% | 84.6% |
| [3.5, 4.0) | 49 | 7.5% | 92.0% |
| [4.0, 4.5) | 29 | 4.4% | 96.5% |
| [4.5, 5.0) | 17 | 2.6% | 99.1% |
| [5.0, 5.5) | 3 | 0.5% | 99.5% |
| [5.5, 6.0) | 3 | 0.5% | 100.0% |

When only the frequency table is available without the raw data, class midpoints give an approximation: mean $\approx \sum_j f_j m_j / n$ ($f_j$ the frequency, $m_j$ the class midpoint). The table above gives $2.647\,\mathrm{L}$, which differs by 0.4% from the $2.637\,\mathrm{L}$ of the raw data. The cumulative proportions give approximate quantiles: the median is near the start of the class [2.5, 3.0) (cumulative 48.0%).

When the class widths are unequal, the vertical axis of the histogram must be "frequency / class width" (density); otherwise wide classes look exaggerated. Too few classes hide the shape of the distribution and too many fill it with noise; **kernel density estimation** replaces every observation by a small smooth "bump" and adds them up, giving a smooth curve that does not depend on the starting point of the classes ([3.2.3](/3.2.3)); its bandwidth plays the role of the class width.

## 2.6. Statistical Graphics

### 2.6.1. Seeing the FEV Data at a Glance

![A first look at the FEV data (654 children aged 3–19, East Boston; Tager et al. 1979). A: histogram and kernel density estimate of FEV; the distribution is right-skewed, with the mean (2.64 L) to the right of the median (2.55 L). B: box plots by smoking status with every observation overlaid; the median of the 65 smoking children is higher. C: scatter plot of FEV against age; all the smoking children are older than 9, which explains the difference in B](./plots/fev-overview.py)

The three panels of the figure answer three questions: how is FEV distributed (A), how do the smoking and nonsmoking groups differ (B), and how is FEV related to age (C). Panel B alone would lead one to think that smoking is beneficial; panel C shows that the smokers are all older children, and FEV increases with age. Comparing at the same age in C, the smokers (orange) are not higher than the nonsmokers and are mostly lower. A suitable scatter plot already points to the confounding ([7.7.1](/7.7.1) Example 1.5.1, [7.7.10](/7.7.10)).

### 2.6.2. Graphs for Categorical Data

A bar chart uses bars of equal width that do not touch to show the frequency or proportion of each category and makes comparison easy; when the categories have no order they are sorted by frequency. A pie chart suits only the composition of a few categories; the eye compares angles and areas much less accurately than lengths, so a bar chart should be used when there are many categories. Compositions of several groups are compared with stacked or grouped bar charts. Nightingale's polar area diagram divided the monthly deaths into three categories and used the area of the sectors for the numbers: its persuasiveness came from the data, not from the form.

### 2.6.3. Graphs for Continuous Data

- Histograms and density curves: the shape of the distribution of one variable (panel A above).
- Stem-and-leaf plot: a "textual histogram" for small samples, described below.
- **Box plot**: the five-number summary, convenient for side-by-side comparison of several groups (panel B above).
- Dot plot (strip plot): draws every observation and is the most honest when the sample size is below a few dozen.
- Scatter plot: the relation between two numerical variables (panel C above), with color or shape distinguishing a third variable.
- **Q–Q plot**: comparison with a theoretical distribution (Section 2.6.5).

**Definition 2.6.1 (Stem-and-Leaf Plot)** Splitting each observation into a "stem" of the high-order digits and a "leaf" of the next digit, writing the stems vertically in order to the left of a vertical line and the leaves of each observation in order to the right of the corresponding stem gives a **stem-and-leaf plot**.

The birth weights of the 74 newborns of smoking mothers, with the kilogram digit as stem and the hundred-gram digit as leaf, each stem split into two rows (leaves 0–4 and 5–9):

```text
0 |
0 | 7
1 | 1
1 | 788999
2 | 0011122223333444444444
2 | 5566677789999999
3 | 00000011223333344
3 | 5666667889
4 | 2
```

(Stem 2 and leaf 5 means 2500–2599 g.) The plot shows the shape of the distribution, concentrated in 2.0–3.5 kg and slightly left-skewed, with two very light babies of 709 g and 1135 g at the lower end, and retains every number (to the hundred-gram digit).

### 2.6.4. Do Not Draw Only Bars

The most common figure in biomedical papers is "bar of the mean + error bar". For continuous data this figure hides nearly all the information: the sample size, the shape of the distribution, outliers and bimodality; whether the error bar is a standard deviation or a standard error is often not stated; and only the upper half of the error is drawn, so the reader cannot see the error below. Completely different data (symmetric, skewed, bimodal, with one outlier) can produce the same bar chart. For small samples all the data points should be drawn, and for large samples a box plot or violin plot. Bar charts suit counts and proportions, and the bars are meaningful only when they start from 0.

![Four displays of the same data: the birth weights (birthwt, Hosmer and Lemeshow) of 115 newborns of nonsmoking mothers and 74 newborns of smoking mothers. A: bars of the mean with standard error bars, hiding the spread and the sample size. B: every observation, with the mean ± standard deviation marked. C: box plot (median, quartiles, whiskers of 1.5 IQR). D: violin plot (kernel density) with the median](./plots/display-choice.py)

Panel A makes the two groups look sharply different, whereas B–D show that they overlap broadly: the smoking group is on average $284\,\mathrm{g}$ lighter, yet many children of smoking mothers are heavier than children of nonsmoking mothers. Whether the difference in means exceeds sampling error is the question of [7.7.7](/7.7.7); the degree of overlap between individuals is something a reader who sees only bars cannot know.

### 2.6.5. QQ Plots

Many methods assume approximately normal data. The **normal Q–Q plot** plots the sorted sample values $x_{(i)}$ against the corresponding quantiles of the standard normal distribution $\Phi^{-1}\bigl((i - 0.5)/n\bigr)$: if the data come from a normal distribution the points fall near a straight line, whose intercept and slope estimate the mean and the standard deviation. Systematic curvature indicates the manner of departure: both ends bending upward (convex) means right skew, both ends bending downward means left skew, and an S shape with the ends bending outward means heavy tails.

![Normal QQ plots: sample quantiles against standard normal quantiles. A: birth weight (birthwt, $n = 189$) is close to a straight line. B: FEV ($n = 654$) bends upward at both ends, characteristic of a right-skewed distribution. C: the logarithm of FEV is closer to normal. The reference line passes through the first and third quartiles](./plots/qq-plots.py)

A QQ plot is more useful than a test of normality: with a large sample, a test gives a small p-value for a negligible departure; with a small sample it lacks the power to detect an obvious departure. What matters is not whether the data are "strictly normal" but whether the departure is large enough to affect the conclusions of the method used (the central limit theorem makes many methods based on the mean insensitive to non-normality in large samples, [7.7.4](/7.7.4)).

### 2.6.6. Principles of Graphs and Tables

- A figure must be readable on its own: the axes give the variable and the unit ("FEV / L"), and the legend states the sample size, the meaning of error bars and the source of the data.
- Starting a numerical axis at 0 is a requirement for bar charts; scatter plots and box plots need not start at 0, but do not truncate an axis to exaggerate a difference.
- Do not use three-dimensional bar charts, three-dimensional pie charts or decorative solid effects; they distort comparisons of length and area. Charts with two vertical axes are easily misleading and should be avoided where possible.
- Colors should be distinguishable by people with color vision deficiency and in black-and-white printing; use the same color for the same variable throughout (in this course blue for nonsmokers and controls, orange for smokers and the exposed).
- Tables in academic papers use three horizontal rules: only a top rule, a rule under the header and a bottom rule, with no vertical lines; the table title is above the table and any necessary notes go in the table footnote.

## 2.7. Outliers

**Definition 2.7.1 (Outlier)** An observation that deviates markedly from the bulk of the data and may come from a different mechanism is an **outlier**.

An outlier may come from an entry or measurement error (a weight of 30 kg entered as 300 kg, confusion of units) or may be a genuine and meaningful extreme individual (an exceptionally premature baby, a patient abnormally sensitive to a drug). Common rules for identifying them:

- The box plot rule: points outside $[Q_1 - 1.5\,\mathrm{IQR},\ Q_3 + 1.5\,\mathrm{IQR}]$ are outliers, and points outside $[Q_1 - 3\,\mathrm{IQR},\ Q_3 + 3\,\mathrm{IQR}]$ are extreme outliers. For normal data about 0.7% of the points are flagged by the former, so with a large sample some perfectly normal points are always flagged.
- The $z$-score rule: $\lvert z\rvert > 3$. But outliers themselves inflate $s$ and mask themselves; the robust $z$-score using the median and the MAD is more reliable.
- The generalized extreme studentized deviate (ESD) test: under an assumption of approximate normality, it tests the most extreme values one at a time while controlling the probability of misclassifying normal data as outliers; it can test several outliers without their masking one another.

**Example 2.7.1** For FEV, $Q_1 = 1.981$ and $Q_3 = 3.119$ (linear interpolation), the upper fence is $3.119 + 1.5 \times 1.138 = 4.825\,\mathrm{L}$, and 10 children exceed it (4.83–5.79 L); there are no extreme outliers. The maximum $5.793\,\mathrm{L}$ has $z = 3.64$. These are older, taller boys, entirely plausible given that FEV increases with age and height (panel C above), and should not be deleted: they are "outliers" only because we put children aged 3 and 19 into the same distribution. In the group of smoking mothers the newborn of 709 g is below the lower fence of the box plot (1058 g); it is a genuine very low birth weight infant, one of the most important individuals precisely when studying low birth weight.

The principles for handling outliers: first check the original records; correct or delete values confirmed as errors and say so in the report; keep values that cannot be confirmed as errors, and a sensitivity analysis may be done (analyze once with and once without the value and compare the conclusions), or use methods insensitive to outliers (median, rank methods, [7.7.8](/7.7.8)). Data must never be deleted because the "result becomes more significant" without them.

## 2.8. Descriptive Statistics in Python

```python
import numpy as np
import pandas as pd
from scipy import stats

fev = pd.read_csv("fev.csv")
bwt = pd.read_csv("birthwt.csv")

# location and spread, overall and by group
print(fev["fev"].agg(["count", "mean", "median", "std", "min", "max"]))
print(fev.groupby("smoke")["fev"].describe())        # count, mean, std, quartiles

# quartiles under different definitions
x = fev["fev"].to_numpy()
for method in ["averaged_inverted_cdf", "linear", "median_unbiased"]:
    print(method, np.quantile(x, [0.25, 0.5, 0.75], method=method))

# robust spread and shape
print(stats.iqr(x), stats.median_abs_deviation(x, scale="normal"))
print(stats.skew(x), stats.kurtosis(x))              # kurtosis is excess kurtosis by default
print(stats.skew(np.log(x)))                         # the log transform removes most skewness

# geometric mean of antibody titres
titre = np.repeat([4, 8, 16, 32, 64, 128, 256, 512], [1, 3, 15, 32, 43, 11, 5, 2])
print(stats.gmean(titre))                            # 47.6

# frequency table with 0.5 L bins, left-closed intervals
table = pd.cut(fev["fev"], np.arange(0.5, 6.01, 0.5), right=False).value_counts(sort=False)
print(pd.DataFrame({"n": table, "cum": table.cumsum() / len(fev)}))

# box-plot rule for outliers
q1, q3 = np.quantile(x, [0.25, 0.75])
print(fev[(x < q1 - 1.5 * (q3 - q1)) | (x > q3 + 1.5 * (q3 - q1))])
```

## Summary

| Purpose | Symmetric numerical data | Skewed numerical data | Multiplicative data | Ordinal data | Nominal data |
|---|---|---|---|---|---|
| Location | Mean | Median | Geometric mean (Definition 2.1.2) | Median | Mode (Definition 2.1.1), proportions |
| Spread | Standard deviation | Interquartile range (Definition 2.2.1), MAD (Definition 2.2.2) | Standard deviation on the log scale | Interquartile range | Index of qualitative variation $D$ |
| Graph | Histogram, box plot, QQ plot | Histogram, box plot | Log axis | Bar chart | Bar chart |

- The **sample mean** uses all the data but is sensitive to extreme values (breakdown point 0); the **sample median** is robust (breakdown point 0.5); in a right-skewed distribution mean > median > mode. For titers and concentrations use the geometric mean, the antilogarithm of the mean of the logarithms (Example 2.1.1: 1:48).
- The **sample variance** is unbiased only when divided by $n - 1$; the standard deviation describes variation between individuals, whereas the **standard error** $s/\sqrt n$ describes the precision of the mean, and the two must not be confused. The coefficient of variation compares relative variation and is an index of assay precision (Example 2.2.2: the CV of replicate wells rises at low concentrations).
- Sample percentiles (Definition 2.3.1) can be computed in several ways, with little difference in large samples; the reference interval (Definition 2.3.2) is the middle 95% of a healthy population, needs enough reference individuals and is partitioned by age, sex and so on.
- **Skewness**, **kurtosis** (note whether 3 is subtracted) and the $z$-score (Definition 2.4.1) describe shape and relative position; right-skewed positive data often become symmetric after taking logarithms.
- Frequency tables and histograms (Definition 2.5.1), stem-and-leaf plots (Definition 2.6.1), **box plots** and **normal Q–Q plots** each have their uses; for continuous data draw the distribution rather than only a bar of the mean. The scatter plot of FEV against age first revealed the confounding in the comparison of smokers.
- Outliers (Definition 2.7.1): check first, decide afterwards; genuine extreme values should be kept and a sensitivity analysis done.

## Questions

1. The lengths of stay of 7 patients in a ward are 3, 4, 4, 5, 6, 8, 41 days. Find the mean, median and mode. Which best represents the length of stay of a "typical patient"? Which should hospital managers use to compute the demand for beds?

   **Answer** Mean $= 71/7 = 10.14$ days, median = 5 days, mode = 4 days. The median of 5 days represents the length of stay of a typical patient: one patient who stayed 41 days pulls the mean up to 10 days, and 6 of the 7 are below the mean. But the mean is needed to compute total bed demand (total bed-days = number of patients × mean days), because the long-stay patient really does occupy a bed: the two indices answer different questions.

2. The peak concentrations (ng/mL) of a drug in 8 subjects are 12, 18, 25, 30, 45, 60, 95, 210. Why do pharmacokinetic studies often report the geometric mean? Compute it.

   **Answer** Drug concentrations are approximately log-normally distributed and vary between individuals by multiples, so the arithmetic mean is strongly affected by a few high concentrations. $\sum \ln x_i = 2.485 + 2.890 + 3.219 + 3.401 + 3.807 + 4.094 + 4.554 + 5.347 = 29.797$, the average is $3.725$, and $G = \mathrm{e}^{3.725} = 41.5\,\mathrm{ng/mL}$; the arithmetic mean is $61.9\,\mathrm{ng/mL}$ and the median is $37.5\,\mathrm{ng/mL}$. The geometric mean also makes it easy to compare two formulations: the antilogarithm of the difference of the means on the log scale is the ratio of the geometric means, which is exactly the quantity used in bioequivalence assessment.

3. Two glucose meters measure the same standard solution 10 times: meter A has mean 5.52 mmol/L and standard deviation 0.11; meter B has mean 5.10 mmol/L and standard deviation 0.05. The true value of the standard is 5.50 mmol/L. Compare the precision and accuracy of the two meters.

   **Answer** Precision concerns the spread of repeated measurements: the CV of A is $0.11/5.52 = 2.0\%$ and that of B is $0.05/5.10 = 1.0\%$, so B is more precise. Accuracy concerns the deviation from the true value: A is off by $+0.02$ (0.4%) and B by $-0.40$ ($-7.3\%$), so A is far more accurate. B is a "precise but systematically biased" instrument that can be calibrated; an imprecise instrument cannot be improved by calibration. Both must be reported when describing an assay.

4. Using Definition 2.3.1, find $Q_1$, the median and $Q_3$ of the 9 numbers 2.1, 2.4, 2.8, 3.0, 3.3, 3.5, 3.9, 4.6, 6.2, give the elements of the box plot, and decide whether there are outliers.

   **Answer** $n = 9$. $P_{25}$: $9 \times 0.25 = 2.25$ is not an integer, $k = 2$, so take $x_{(3)} = 2.8$. Median: $4.5$, $k = 4$, so take $x_{(5)} = 3.3$. $P_{75}$: $6.75$, $k = 6$, so take $x_{(7)} = 3.9$. $\mathrm{IQR} = 1.1$, the upper fence is $3.9 + 1.65 = 5.55$ and the lower fence is $2.8 - 1.65 = 1.15$. The value 6.2 exceeds the upper fence and is an outlier (but does not exceed the extreme-outlier fence $3.9 + 3.3 = 7.2$); the upper whisker extends to 4.6 and the lower whisker to 2.1. The distribution is right-skewed: the upper whisker and the upper half of the box are longer than the lower ones.

5. A paper reports "the tumor volumes of two groups of mice were $520 \pm 35$ and $410 \pm 30\,\mathrm{mm^3}$ ($n = 10$), a significant difference", without saying what follows the $\pm$. If it is the standard error, what are the standard deviations? What does this imply for the overlap of the two groups?

   **Answer** If it is the standard error, the standard deviation $= \mathrm{SE}\times\sqrt{10}$: $35 \times 3.16 = 111$ and $30 \times 3.16 = 95\,\mathrm{mm^3}$, respectively. The means differ by 110, only about one standard deviation, so the individuals of the two groups overlap considerably: if approximately normal, about 16% of the mice in the first group are below the mean of the second group ($z = -110/111 = -0.99$), and about 12% of the mice in the second group are above the mean of the first group ($z = 110/95 = 1.16$). If one mistakenly takes $\pm$ to be the standard deviation, the reader would think the two groups hardly overlap. A report must state the meaning of the error bars, and preferably draw the data points of every mouse.

6. The serum total cholesterol of adult men in a region is approximately normal with mean 4.80 mmol/L and standard deviation 0.85 mmol/L. Find the 95% reference interval by the normal method. A man measures 6.80 mmol/L; find his $z$-score. Is he "ill"?

   **Answer** The reference interval is $4.80 \pm 1.96 \times 0.85$, that is 3.13–6.47 mmol/L. $z = (6.80 - 4.80)/0.85 = 2.35$, about the 99th percentile. He is outside the reference interval, but the reference interval describes the statistical distribution in a healthy population and is not a diagnostic criterion: the diagnosis of dyslipidemia uses clinical decision limits determined from cardiovascular risk studies (for example total cholesterol ≥ 6.2 mmol/L is elevated), and treatment decisions require a comprehensive assessment with other risk factors. Statistical "abnormality" and clinical "disease" are two different concepts.

7. Someone says: "My data have a Shapiro–Wilk test $p = 0.43$, so they are normally distributed." Another says: "My 2000 observations give $p = 0.002$, so I cannot use the $t$-test." Evaluate the two statements.

   **Answer** Both are wrong. $p = 0.43$ only says that there is not enough evidence to reject normality; it does not prove normality (the conclusion of a test is not "accept the null hypothesis"; with small samples the power of the test is very low). With $n = 2000$ the test can detect minute departures that are irrelevant to the actual analysis, and because of the central limit theorem the $t$-test is quite robust to moderate non-normality in large samples. One should look at the QQ plot and the histogram, judge the manner and size of the departure (such as severe skewness, heavy tails, outliers), and then decide in light of the sample size and the robustness of the method. For birth weight $p = 0.44$ and the QQ plot is also close to a straight line, and the two agree.

8. The following table gives "mean ± standard deviation" from a study: length of stay $6.2 \pm 8.1$ days, CRP $45 \pm 70\,\mathrm{mg/L}$. Without seeing the raw data, what can you infer about the distributions of these two variables? How should they be reported?

   **Answer** Both variables are nonnegative, yet the standard deviation exceeds the mean: if the distribution were approximately normal, the mean minus one standard deviation would be negative, which is impossible, so the distribution must be severely right-skewed (a few patients stay very long or have very high CRP). Mean ± standard deviation is unsuitable for summarizing such data; one should report the median (interquartile range), such as "length of stay 4 (2–7) days", or take logarithms of CRP and report the geometric mean. $\mathrm{SD} > \text{mean}$ (for a nonnegative variable) is a simple signal of skewness in a paper.

9. (Design question) You are responsible for evaluating the precision of a new ELISA kit. Design the experiment and the data analysis: which samples are needed, how many replicates, and what indices are computed?

   **Answer** Outline: choose quality control samples at 3 levels covering the measuring range (low, medium, high concentration, with the low one near the detection limit). Measure each level in 2 runs per day, with 2–3 replicate wells per run, for about 20 consecutive days (the 20-day protocol commonly used in clinical laboratory guidelines). Analysis: for each level compute the intra-run CV (between replicate wells of the same run), the inter-run CV (between different runs on the same day) and the total CV (including between-day variation); a random-effects analysis of variance can decompose the total variance into between-day, between-run and within-run variance components ([7.7.17](/7.7.17)); plot the CV against concentration and find the lowest concentration at which the CV is below the acceptable limit (such as 20%), which is the lower limit of quantification. The rise of the replicate-well CV at the lowest concentration of the DNase data in Example 2.2.2 is exactly the phenomenon such an analysis is meant to discover.
