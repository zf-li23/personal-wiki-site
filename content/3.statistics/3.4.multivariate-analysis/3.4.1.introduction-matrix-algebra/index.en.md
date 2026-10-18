---
title: Introduction and Matrix Algebra
description: Multivariate data and the goals of multivariate analysis; the data matrix and random samples of vectors; Euclidean and Mahalanobis distance and the expectation of quadratic forms; exploratory graphics; the geometry of matrix operations, spectral decomposition, square root matrices, SVD, the extended Cauchy–Schwarz inequality and the maximization lemma; vector and matrix calculus.
---

Almost every data set collected in practice records several variables on each individual, and these variables are usually correlated. Multivariate statistical analysis studies such data jointly rather than one variable at a time. This chapter lays two foundations for the course. The first is statistical: how multivariate data are organized and modeled, how the distance between two observations should account for different scales and for correlation (the Mahalanobis distance), and how to explore the data graphically. The second is algebraic: the matrix tools used throughout the course, presented with their geometric meaning. The matrix theory itself was developed in linear algebra ([2.1](/2.1)), in particular the spectral decomposition and the singular value decomposition of [2.1.7](/2.1.7); here we collect what is needed, interpret it geometrically and add the inequalities and the matrix calculus required for estimation. The descriptive statistics of a sample and the multivariate normal distribution follow in [3.4.2](/3.4.2).

## 1.1. Multivariate Data and the Goals of Multivariate Analysis

Multivariate data arise in every discipline: a medical record, a credit card application, an image, a shopping receipt all describe one unit by many measurements. Typical questions are the following.

- Are there differences? For example, the average change in the expression levels of many genes after a treatment.
- What are the key features? From the scores of a personality questionnaire, how to divide people into groups and what characterizes each group.
- What are the key connections? Which features of whole-brain functional connectivity (thousands of synchronization scores between pairs of brain regions) are associated with which emotional and behavioral scores of adolescents; which abilities measured in a recruitment test are associated with which aspects of later job performance.
- How to predict or recommend? "Customers who bought this also bought…".
- Who wrote it? Whether the novel *Dream of the Red Chamber* has one author or several, studied through the frequencies of function words in each chapter.
- How to classify? Diagnosing the type of a disease from blood tests and images; deciding whether to grant a loan from a client's age, income, education and repayment history.

From the point of view of applications, the methods of the course fall into a few groups; from the point of view of the model $f(\boldsymbol{x})$, the first group concerns the mean vector $\boldsymbol{\mu}$ and most of the others concern the covariance matrix $\Sigma$.

| Goal | Methods | Chapters |
|---|---|---|
| Inference on means | Hotelling's $T^2$, comparison of mean vectors | [3.4.3](/3.4.3), [3.4.4](/3.4.4) |
| Dimension reduction (unsupervised) | principal components, multidimensional scaling, factor analysis, canonical correlation | [3.4.5](/3.4.5), [3.4.6](/3.4.6), [3.4.8](/3.4.8), [3.4.9](/3.4.9) |
| Prediction and classification (supervised) | multivariate regression, discriminant analysis | [3.4.7](/3.4.7), [3.4.10](/3.4.10) |
| Clustering (unsupervised) | hierarchical and partitioning methods | [3.4.11](/3.4.11) |

Statistics enters whenever a problem involves uncertainty, which is to say in nearly every real problem. Two tensions run through the course: between science and engineering, that is, between interpretability and predictive accuracy, and correspondingly between simple and complex models. The classical methods of this course are on the interpretable side; [3.4.12](/3.4.12) discusses extensions.

## 1.2. Organization and Modeling of Multivariate Data

### 1.2.1. The Data Matrix

Suppose $p$ variables are measured on each of $n$ items (individuals, experimental units). Let $x_{jk}$ be the value of the $k$-th variable on the $j$-th item.

**Definition 1.2.1 (Data Matrix)** The $n \times p$ array

$$
X = \begin{bmatrix} x_{11} & x_{12} & \cdots & x_{1p} \\ x_{21} & x_{22} & \cdots & x_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ x_{n1} & x_{n2} & \cdots & x_{np} \end{bmatrix} = \begin{bmatrix} \boldsymbol{x}_1^{\mathsf T} \\ \boldsymbol{x}_2^{\mathsf T} \\ \vdots \\ \boldsymbol{x}_n^{\mathsf T} \end{bmatrix}
$$
is called the **data matrix**. Its rows correspond to items and its columns to variables; the $j$-th row $\boldsymbol{x}_j^{\mathsf T} = (x_{j1}, \dots, x_{jp})$ is the $j$-th multivariate observation.

Writing the data as a matrix makes matrix operations available for every computation, and it matches the way data are stored (a table of monitoring stations by pollutants, say). Throughout the course we use the following conventions. The index $j = 1, \dots, n$ runs over items and $k$ (or $i$) $= 1, \dots, p$ over variables. Before the data are observed, the entries are random variables $X_{jk}$ and the rows are random vectors $\boldsymbol{X}_j = (X_{j1}, \dots, X_{jp})^{\mathsf T}$; the observed values are $x_{jk}$ and $\boldsymbol{x}_j$. The data matrix is written $X$ in both cases, since the context always makes clear whether it is regarded as random or observed. Thus the observed data are a realization of a matrix of random variables, and we ask what the joint distribution of its entries is: what population distribution generated the rows, what assumptions are reasonable, and which unknown parameters describe it.

### 1.2.2. Random Samples

**Definition 1.2.2 (Random Sample)** Random vectors $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ form a **random sample** from a $p$-dimensional distribution with density $f(\boldsymbol{x}) = f(x_1, \dots, x_p)$ if

1. $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ are mutually independent, and
2. each $\boldsymbol{X}_j$ has the same joint distribution with density $f$.

That is, the rows of the data matrix are iid. Under this assumption the joint density of the whole sample is

$$
f(\boldsymbol{x}_1)f(\boldsymbol{x}_2)\cdots f(\boldsymbol{x}_n), \qquad f(\boldsymbol{x}_j) = f(x_{j1}, x_{j2}, \dots, x_{jp}),
$$
where $f$ may be specified parametrically or left nonparametric. Independence is assumed only between items: the $p$ measurements on the same item are in general correlated, and modeling this correlation is the main subject of the course.

The population quantities that summarize $f$ are the mean vector and the **covariance matrix** of a **random vector** $\boldsymbol{X} = (X_1, \dots, X_p)^{\mathsf T}$:

$$
\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X} = \begin{bmatrix} \mathbb{E}X_1 \\ \vdots \\ \mathbb{E}X_p \end{bmatrix} = \begin{bmatrix} \mu_1 \\ \vdots \\ \mu_p \end{bmatrix}, \qquad \Sigma = \operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}] = \begin{bmatrix} \sigma_{11} & \cdots & \sigma_{1p} \\ \vdots & \ddots & \vdots \\ \sigma_{p1} & \cdots & \sigma_{pp} \end{bmatrix},
$$
where $\sigma_{ik} = \operatorname{Cov}(X_i, X_k) = \mathbb{E}[(X_i - \mu_i)(X_k - \mu_k)]$ and $\sigma_{kk} = \operatorname{Var}(X_k)$ (see [3.1.15](/3.1.15) for the rules of calculation).

**Example 1.2.1** The gross weight of municipal solid waste generated per year was recorded as follows.

| Year | 1960 | 1970 | 1980 | 1990 | 1995 | 2000 | 2003 |
|---|---|---|---|---|---|---|---|
| $x_1$ (paper) | 29.2 | 44.3 | 55.2 | 72.7 | 81.7 | 87.7 | 83.1 |
| $x_2$ (plastics) | 0.4 | 2.9 | 6.8 | 17.1 | 18.9 | 24.7 | 26.7 |

These seven rows should not be treated as a random sample. They are successive years of one time series with a clear upward trend, so the observations are neither independent nor identically distributed. Whether the random sampling assumption is plausible must be checked against how the data were collected before any of the methods below are applied.

### 1.2.3. Two Geometric Pictures

The data matrix can be viewed in two ways.

- As $n$ points in $p$-dimensional space: each row $\boldsymbol{x}_j$ is a point of $\mathbb{R}^p$; for $p = 2$ or $3$ this is the scatter plot, which shows the location and the variability of the points.
- As $p$ vectors in $n$-dimensional space: each column is a vector of $\mathbb{R}^n$ holding the $n$ measurements of one variable. Lengths and angles of these vectors correspond to variances and correlations ([3.4.2](/3.4.2)).

For example, for $X = \begin{bmatrix} 4 & 1 \\ 5 & 2 \\ 3 & 5 \end{bmatrix}$ (sales in units of 100 yuan and number of books for three bookstores), the first picture consists of the three points $\boldsymbol{x}_1 = (4, 1)^{\mathsf T}$, $\boldsymbol{x}_2 = (5, 2)^{\mathsf T}$, $\boldsymbol{x}_3 = (3, 5)^{\mathsf T}$ in the plane. Is $\boldsymbol{x}_1$ more similar to $\boldsymbol{x}_2$ or to $\boldsymbol{x}_3$? The answer depends on how distance is measured, which is the subject of the next section.

## 1.3. Statistical Distance

### 1.3.1. From Euclidean to Statistical Distance

Many applications compare two individuals, so we need a distance or a similarity between two multivariate observations $P = (x_1, \dots, x_p)$ and $Q = (y_1, \dots, y_p)$. The Euclidean distance

$$
d(P, Q) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + \cdots + (x_p - y_p)^2}
$$
gives every coordinate the same weight. This makes little sense when the variables are measured in different units or on different scales: changing the unit of one variable (meters to centimeters) changes which points are close.

If the variables are independent (or at least uncorrelated), the natural remedy is to standardize each coordinate, $x_k - y_k \mapsto (x_k - y_k)/\sqrt{s_{kk}}$, where $s_{kk}$ is the sample variance of the $k$-th variable:

$$
d(P, Q) = \sqrt{\frac{(x_1 - y_1)^2}{s_{11}} + \frac{(x_2 - y_2)^2}{s_{22}} + \cdots + \frac{(x_p - y_p)^2}{s_{pp}}}.
$$
Points at constant distance $c$ from the origin now form an ellipse with semi-axes $c\sqrt{s_{11}}$ and $c\sqrt{s_{22}}$ along the coordinate axes. A point that is far out along a direction of small spread is more unusual than a point equally far along a direction of large spread.

If instead the variables are correlated, say $x_2$ tends to increase with $x_1$, then the cloud of points is an ellipse whose axes are tilted, and an ellipse aligned with the coordinate axes no longer describes it: two points $P$ and $Q$ on such an axis-aligned ellipse may be very different in how typical they are. The remedy is to rotate the coordinate system by an angle $\theta$ so that the new axes $\tilde x_1, \tilde x_2$ follow the axes of the cloud,

$$
\tilde x_1 = x_1\cos\theta + x_2\sin\theta, \qquad \tilde x_2 = -x_1\sin\theta + x_2\cos\theta,
$$
and to standardize in the new coordinates, where the variables are uncorrelated:

$$
d(O, P) = \sqrt{\frac{\tilde x_1^2}{\tilde s_{11}} + \frac{\tilde x_2^2}{\tilde s_{22}}} = \sqrt{a_{11}x_1^2 + 2a_{12}x_1x_2 + a_{22}x_2^2}
$$
for suitable constants $a_{11}, a_{12}, a_{22}$ determined by $\theta$, $\tilde s_{11}$ and $\tilde s_{22}$. The cross term $2a_{12}x_1x_2$ takes care of the nonzero correlation. In $p$ dimensions,

$$
d(P, Q) = \sqrt{\sum_{k=1}^{p} a_{kk}(x_k - y_k)^2 + 2\sum_{i < k} a_{ik}(x_i - y_i)(x_k - y_k)},
$$
that is, $d^2(P, Q) = (\boldsymbol{x} - \boldsymbol{y})^{\mathsf T}A(\boldsymbol{x} - \boldsymbol{y})$ is a **quadratic form** in $\boldsymbol{x} - \boldsymbol{y}$ with a symmetric matrix $A = (a_{ik})$. Section 1.6 shows that the right choice is $A = \Sigma^{-1}$.

### 1.3.2. The Mahalanobis Distance

**Definition 1.3.1 (Mahalanobis Distance)** The **Mahalanobis distance** of an observation $\boldsymbol{x} = (x_1, \dots, x_p)^{\mathsf T}$ from a population (or a set of observations) with mean $\boldsymbol{\mu} = (\mu_1, \dots, \mu_p)^{\mathsf T}$ and positive definite covariance matrix $\Sigma$ is

$$
d(\boldsymbol{x}, \boldsymbol{\mu}) = \|\boldsymbol{x} - \boldsymbol{\mu}\|_{\Sigma} = \sqrt{(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})}.
$$
As a dissimilarity between two random vectors $\boldsymbol{x}$ and $\boldsymbol{y}$ from the same distribution with covariance matrix $\Sigma$, it is

$$
d(\boldsymbol{x}, \boldsymbol{y}) = \sqrt{(\boldsymbol{x} - \boldsymbol{y})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{y})}.
$$
Its square is also called the generalized squared interpoint distance.

The distance was introduced in 1936 by the Indian statistician P. C. Mahalanobis (1893–1972), prompted by the problem of measuring the similarity of skulls from several measurements. If the axes of the data ellipsoid are rescaled to unit variance, the Mahalanobis distance becomes the ordinary Euclidean distance in the transformed space (Section 1.6.4). It is therefore unitless and scale-invariant, and it takes the correlations of the data into account. In practice $\boldsymbol{\mu}$ and $\Sigma$ are replaced by the sample mean $\bar{\boldsymbol{x}}$ and the sample covariance matrix $S$, giving $(\boldsymbol{x} - \bar{\boldsymbol{x}})^{\mathsf T}S^{-1}(\boldsymbol{x} - \bar{\boldsymbol{x}})$. Applications include outlier detection, classification ([3.4.10](/3.4.10)) and clustering ([3.4.11](/3.4.11)).

Both the Euclidean distance ($A = I$) and the Mahalanobis distance ($A = \Sigma^{-1}$) are square roots of quadratic forms $Q(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$ with $A$ symmetric. A first way to compare them is to compute their expected values.

![Left: a correlated sample with the Euclidean circle and the Mahalanobis ellipse through the point P; Q is closer to the center in Euclidean distance but much farther in Mahalanobis distance. Right: after whitening (rotation onto the principal axes and rescaling to unit variance) the ellipse becomes a circle and the Mahalanobis distance is the Euclidean distance.](./plots/mahalanobis-geometry.py)

### 1.3.3. Expectation of Quadratic Forms

**Theorem 1.3.1** Let $\boldsymbol{Z}$ be a random vector with finite mean $\boldsymbol{\mu}_Z$ and finite covariance matrix $\Sigma_Z$, and let $A$ be a constant symmetric matrix. Then

$$
\mathbb{E}[\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}] = \operatorname{tr}(A\Sigma_Z) + \boldsymbol{\mu}_Z^{\mathsf T}A\boldsymbol{\mu}_Z.
$$

**Proof** A scalar equals its own **trace**, the trace is linear (so it commutes with expectation) and $\operatorname{tr}(BC) = \operatorname{tr}(CB)$. Using also $\mathbb{E}[\boldsymbol{Z}\boldsymbol{Z}^{\mathsf T}] = \Sigma_Z + \boldsymbol{\mu}_Z\boldsymbol{\mu}_Z^{\mathsf T}$,

$$
\begin{aligned}
\mathbb{E}[\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}] &= \mathbb{E}[\operatorname{tr}(\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z})] = \mathbb{E}[\operatorname{tr}(A\boldsymbol{Z}\boldsymbol{Z}^{\mathsf T})] = \operatorname{tr}(A\,\mathbb{E}[\boldsymbol{Z}\boldsymbol{Z}^{\mathsf T}]) \\
&= \operatorname{tr}(A\Sigma_Z) + \operatorname{tr}(A\boldsymbol{\mu}_Z\boldsymbol{\mu}_Z^{\mathsf T}) = \operatorname{tr}(A\Sigma_Z) + \boldsymbol{\mu}_Z^{\mathsf T}A\boldsymbol{\mu}_Z. \quad \square
\end{aligned}
$$

**Corollary 1.3.1 (Expected Squared Euclidean Distance)** If the $p$-dimensional random vector $\boldsymbol{X}$ has finite mean $\boldsymbol{\mu}$ and finite covariance matrix $\Sigma$, then

$$
\mathbb{E}\|\boldsymbol{X} - \boldsymbol{\mu}\|^2 = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}I(\boldsymbol{X} - \boldsymbol{\mu})] = \operatorname{tr}\Sigma = \sum_{k=1}^{p}\sigma_{kk}.
$$

This follows from Theorem 1.3.1 with $\boldsymbol{Z} = \boldsymbol{X} - \boldsymbol{\mu}$ (mean $\boldsymbol{0}$) and $A = I$. The expected squared Euclidean distance is the total variance, dominated by the variables with the largest variances.

**Corollary 1.3.2 (Expected Squared Mahalanobis Distance)** Under the same assumptions, with $\Sigma$ positive definite,

$$
\mathbb{E}\|\boldsymbol{X} - \boldsymbol{\mu}\|_{\Sigma}^2 = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu})] = \operatorname{tr}(\Sigma^{-1}\Sigma) = p.
$$
If $\boldsymbol{X}$ and $\boldsymbol{Y}$ are independent and identically distributed with mean $\boldsymbol{\mu}$ and covariance matrix $\Sigma$, then $\mathbb{E}\|\boldsymbol{X} - \boldsymbol{Y}\|_{\Sigma}^2 = 2p$.

**Proof** The first statement is Theorem 1.3.1 with $A = \Sigma^{-1}$. For the second, $\boldsymbol{Z} = \boldsymbol{X} - \boldsymbol{Y}$ has mean $\boldsymbol{0}$, and its covariance matrix has entries

$$
\operatorname{Cov}(X_i - Y_i, X_k - Y_k) = \operatorname{Cov}(X_i, X_k) - \operatorname{Cov}(Y_i, X_k) - \operatorname{Cov}(X_i, Y_k) + \operatorname{Cov}(Y_i, Y_k) = 2\sigma_{ik},
$$
because the cross covariances vanish by independence and $\operatorname{Cov}(Y_i, Y_k) = \sigma_{ik}$ because the distributions are equal. Hence $\operatorname{Cov}(\boldsymbol{X} - \boldsymbol{Y}) = 2\Sigma$ and $\mathbb{E}[\boldsymbol{Z}^{\mathsf T}\Sigma^{-1}\boldsymbol{Z}] = \operatorname{tr}(\Sigma^{-1} \cdot 2\Sigma) = 2p$. $\square$

The entrywise computation in the proof is worth doing once; afterwards one should write directly $\operatorname{Cov}(\boldsymbol{X} - \boldsymbol{Y}) = \operatorname{Cov}(\boldsymbol{X}) + \operatorname{Cov}(\boldsymbol{Y}) = 2\Sigma$, exactly as in one dimension. Unlike the Euclidean distance, the expected squared Mahalanobis distance does not depend on the scales or the correlations of the variables: each of the $p$ standardized, decorrelated directions contributes $1$.

## 1.4. Exploratory Data Analysis

An important step in the analysis of any data set is *exploratory data analysis* (EDA), including the graphical display of the data. Graphical displays may suggest a plausible model for the data, assess the validity of model assumptions, detect outliers, or suggest normalizing transformations. One looks for location, spread, skewness, outliers and subgroups of each variable, and for the relationships between variables.

### 1.4.1. Displays of a Single Variable

**Definition 1.4.1 (Boxplot)** Let $Q_1$, $Q_2$ and $Q_3$ be the lower quartile, the median and the upper quartile of a sample, and $\mathrm{IQR} = Q_3 - Q_1$ the interquartile range. The **boxplot** draws a box from $Q_1$ to $Q_3$ with a line at the median (often also a mark at the mean), and whiskers from the box to the most extreme observations within the normal range $[Q_1 - 1.5\,\mathrm{IQR},\ Q_3 + 1.5\,\mathrm{IQR}]$; observations outside this range are plotted individually as potential outliers.

**Example 1.4.1** If a sample has median $8$, $Q_1 = 4$ and $Q_3 = 10$, then $\mathrm{IQR} = 6$ and the normal range is $[4 - 9,\ 10 + 9] = [-5, 19]$. The upper whisker ends at $\min(19, \max_j x_j)$ and the lower whisker at $\max(-5, \min_j x_j)$.

Side-by-side boxplots compare groups. For the fuel efficiency of American, Japanese and European cars, they show at once that Japanese cars are more efficient (the box of the American cars lies below that of the Japanese cars, and the least efficient Japanese car beats about half of the American cars) and that one very fuel-efficient car (a diesel Volkswagen) is an outlier. A boxplot shows location, spread, skewness and outliers, but it cannot show multimodality or subclusters.

A histogram approximates the density, so it shows multimodality and subclusters as well. It is not unique: its appearance depends on the bin width $h$ and the origin. For data from a normal distribution with standard deviation $\sigma$, the bin width minimizing the asymptotic mean integrated squared error is

$$
h_{\mathrm{opt}} = \left(\frac{24\sqrt{\pi}}{n}\right)^{1/3}\sigma \approx 3.49\,\sigma n^{-1/3}.
$$
For categorical variables, bar charts and pie charts are used instead.

### 1.4.2. Displays of Several Variables

For several variables one looks at the attributes of each variable and at the relationships between variables.

| Display | What it shows |
|---|---|
| Scatter plot of two variables | subgroups, outliers, positive or negative dependence |
| Scatter plot matrix (all pairs of variables, with histograms or densities on the diagonal) | all pairwise relationships at once |
| Three-dimensional scatter plot (rotatable) | structure involving three variables |
| Correlation heatmap | the correlation matrix as colors; reordering the variables can reveal blocks of correlated variables |
| Radar chart, star plot | each item as a polygon or star whose rays are the (scaled) variables; compares items or group profiles |
| Chernoff faces | each variable controls one feature of a cartoon face |
| Andrews curves | each item as a curve, below |
| Growth curves | repeated measurements over time, one curve per item |

The Andrews curve of an observation $\boldsymbol{x} = (x_1, \dots, x_p)^{\mathsf T}$ is the function

$$
f_{\boldsymbol{x}}(t) = \frac{x_1}{\sqrt{2}} + x_2\sin t + x_3\cos t + x_4\sin 2t + x_5\cos 2t + \cdots, \qquad -\pi \le t \le \pi.
$$
By orthogonality of the trigonometric functions, the $L^2$ distance between two curves is proportional to the Euclidean distance between the observations, so similar items give similar curves.

![Scatter plot matrix of a simulated four-variable data set with two groups: the diagonal shows the histogram of each variable, the off-diagonal panels show all pairwise scatter plots. The groups overlap in every single variable but separate clearly in some pairs.](./plots/scatterplot-matrix.py)

In the classical data on old Swiss 1000-franc bank notes (six size measurements on genuine and counterfeit notes), a scatter plot of two of the measurements separates the genuine from the counterfeit notes far better than either measurement alone. This is the typical situation that motivates multivariate methods.

## 1.5. Vectors and Matrices: A Geometric View

From here on we review the matrix tools of the course, with the emphasis on understanding algebra through geometry.

### 1.5.1. Length, Angle and Projection

For $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$, the **inner product** is $\boldsymbol{x}^{\mathsf T}\boldsymbol{y} = x_1y_1 + \cdots + x_ny_n$, the length is $L_{\boldsymbol{x}} = \sqrt{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$, and the angle $\theta$ between nonzero vectors satisfies

$$
\cos\theta = \frac{\boldsymbol{x}^{\mathsf T}\boldsymbol{y}}{L_{\boldsymbol{x}}L_{\boldsymbol{y}}} = \frac{\boldsymbol{x}^{\mathsf T}\boldsymbol{y}}{\sqrt{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}\sqrt{\boldsymbol{y}^{\mathsf T}\boldsymbol{y}}}.
$$
The **orthogonal projection** of $\boldsymbol{x}$ onto the line spanned by $\boldsymbol{y} \ne \boldsymbol{0}$ is

$$
\frac{\boldsymbol{x}^{\mathsf T}\boldsymbol{y}}{\boldsymbol{y}^{\mathsf T}\boldsymbol{y}}\,\boldsymbol{y} = \frac{\boldsymbol{x}^{\mathsf T}\boldsymbol{y}}{L_{\boldsymbol{y}}}\cdot\frac{\boldsymbol{y}}{L_{\boldsymbol{y}}},
$$
with signed length $\boldsymbol{x}^{\mathsf T}\boldsymbol{y}/L_{\boldsymbol{y}} = L_{\boldsymbol{x}}\cos\theta$. For example, the projection of $(3, 2)^{\mathsf T}$ onto $(4, 0)^{\mathsf T}$ is $(3, 0)^{\mathsf T}$.

### 1.5.2. Matrices as Maps

An $m \times k$ matrix $A = [\boldsymbol{a}_1, \dots, \boldsymbol{a}_k]$ maps $\boldsymbol{x} \in \mathbb{R}^k$ to $A\boldsymbol{x} = x_1\boldsymbol{a}_1 + \cdots + x_k\boldsymbol{a}_k \in \mathbb{R}^m$, a linear combination of its columns. The basic operations (transpose, sum, scalar multiple, product, trace, determinant, rank, inverse, partition into blocks, eigenvalues and eigenvectors) are those of [2.1](/2.1); recall that in general $AB \ne BA$. Special matrices that occur constantly are the **symmetric matrix** (every covariance matrix, population or sample, is symmetric), the **diagonal matrix** $\operatorname{diag}(d_1, \dots, d_p)$, which rescales each coordinate axis separately, and the **identity matrix** $I$, with $IA = AI = A$.

### 1.5.3. Orthogonal Matrices

A square matrix $P$ is an **orthogonal matrix** if its rows, viewed as vectors, are mutually perpendicular unit vectors, that is, $PP^{\mathsf T} = I$. Equivalently $P^{-1} = P^{\mathsf T}$, so also $P^{\mathsf T}P = I$ and the columns are orthonormal as well. We usually write an orthogonal matrix by its columns, $P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_p]$ with $\boldsymbol{e}_i^{\mathsf T}\boldsymbol{e}_k = 0$ for $i \ne k$ and $\boldsymbol{e}_i^{\mathsf T}\boldsymbol{e}_i = 1$.

Orthogonal matrices preserve lengths and angles, and they act as changes of orthonormal coordinate systems. If $\boldsymbol{x}$ is the coordinate vector of a point in the original system and the axes are rotated anticlockwise by $\theta$, the coordinates of the same point in the rotated system are

$$
P\boldsymbol{x}, \qquad P = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix};
$$
for instance $\boldsymbol{x} = (\cos\phi, \sin\phi)^{\mathsf T}$ becomes $P\boldsymbol{x} = (\cos(\phi - \theta), \sin(\phi - \theta))^{\mathsf T}$. In general the rows of $P$ are the new axes expressed in the old coordinates, and the entries of $P\boldsymbol{x}$ are the projections of $\boldsymbol{x}$ onto them. The orthogonal matrix $\begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}$ (determinant $-1$) also changes coordinates: its new axes are $(\cos\theta, \sin\theta)^{\mathsf T}$ and $(\sin\theta, -\cos\theta)^{\mathsf T}$, the system rotated by $\theta$ with its second axis reversed.

## 1.6. Spectral Decomposition and Positive Definite Matrices

### 1.6.1. Spectral Decomposition

A $k \times k$ symmetric matrix $A$ has $k$ real eigenvalue–eigenvector pairs $(\lambda_1, \boldsymbol{e}_1), \dots, (\lambda_k, \boldsymbol{e}_k)$, and the eigenvectors can be chosen to be unit vectors that are mutually perpendicular, so that $\{\boldsymbol{e}_1, \dots, \boldsymbol{e}_k\}$ is an **orthonormal basis** and $P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_k]$ is orthogonal. The eigenvectors are unique (up to sign) unless two or more eigenvalues are equal.

**Theorem 1.6.1 (Spectral Decomposition)** Let $A$ be a $k \times k$ symmetric matrix with orthonormal eigenvectors $\boldsymbol{e}_1, \dots, \boldsymbol{e}_k$ and eigenvalues $\lambda_1, \dots, \lambda_k$, and let $P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_k]$, $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_k)$. Then

$$
A = P\Lambda P^{\mathsf T} = \sum_{i=1}^{k}\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T} = \lambda_1\boldsymbol{e}_1\boldsymbol{e}_1^{\mathsf T} + \lambda_2\boldsymbol{e}_2\boldsymbol{e}_2^{\mathsf T} + \cdots + \lambda_k\boldsymbol{e}_k\boldsymbol{e}_k^{\mathsf T}.
$$

This is the **spectral decomposition** of [2.1.7](/2.1.7). The matrix form follows by stacking the $k$ equations $A\boldsymbol{e}_i = \lambda_i\boldsymbol{e}_i$ side by side: the left sides form $[A\boldsymbol{e}_1, \dots, A\boldsymbol{e}_k] = AP$ and the right sides $[\lambda_1\boldsymbol{e}_1, \dots, \lambda_k\boldsymbol{e}_k] = P\Lambda$, so $AP = P\Lambda$ and $A = P\Lambda P^{-1} = P\Lambda P^{\mathsf T}$. Multiplying out $P \cdot \Lambda P^{\mathsf T}$ column by row gives the sum of rank-one matrices $\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$. Treating vectors and matrices formally like scalars in this way, while keeping track of dimensions, is the habit the course tries to build.

### 1.6.2. Geometric Interpretation

The map $\boldsymbol{x} \mapsto A\boldsymbol{x} = P\Lambda P^{\mathsf T}\boldsymbol{x}$ (read from right to left) is a composition of three steps: $P^{\mathsf T}$ expresses $\boldsymbol{x}$ in the coordinate system of the eigenvectors (a rotation, possibly with a reflection), $\Lambda$ stretches the $i$-th new axis by the factor $\lambda_i$ (and flips it if $\lambda_i < 0$), and $P$ returns to the original coordinates.

**Example 1.6.1** For $A = \begin{bmatrix} 1 & -5 \\ -5 & 1 \end{bmatrix}$, the eigenvalues are $6$ and $-4$ with unit eigenvectors $\frac{1}{\sqrt{2}}(1, -1)^{\mathsf T}$ and $\frac{1}{\sqrt{2}}(1, 1)^{\mathsf T}$, so

$$
A = P\Lambda P^{\mathsf T}, \qquad P^{\mathsf T} = \begin{bmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}, \qquad \Lambda = \begin{bmatrix} 6 & 0 \\ 0 & -4 \end{bmatrix}.
$$
Applied to a cloud of points $B$ (an $n \times 2$ data matrix), the three steps are visible one by one: $B_2^{\mathsf T} = P^{\mathsf T}B^{\mathsf T}$ rotates the cloud by $45^\circ$, $B_3^{\mathsf T} = \Lambda B_2^{\mathsf T}$ stretches the first axis six-fold and the second four-fold with a reflection, and $B_4^{\mathsf T} = PB_3^{\mathsf T} = AB^{\mathsf T}$ rotates back.

### 1.6.3. Positive Definite Matrices, Inverses and Square Roots

Let $A$ be a $k \times k$ symmetric matrix. If $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} \ge 0$ for all $\boldsymbol{x}$, the matrix and the quadratic form are called nonnegative definite, a **positive semidefinite matrix**; if $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} > 0$ for all $\boldsymbol{x} \ne \boldsymbol{0}$, a **positive definite matrix** ([2.1.7](/2.1.7)). These are the matrices that define distances. By the spectral decomposition, with $y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{x}$,

$$
\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} = \sum_{i=1}^{k}\lambda_i(\boldsymbol{e}_i^{\mathsf T}\boldsymbol{x})^2 = \sum_{i=1}^{k}\lambda_iy_i^2,
$$
so $A$ is positive definite if and only if every eigenvalue is positive, and nonnegative definite if and only if every eigenvalue is nonnegative. When all $\lambda_i \ge 0$, $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} = \sum_i(\sqrt{\lambda_i}y_i)^2$ is a squared Euclidean length in rotated and rescaled coordinates.

**Definition 1.6.1 (Square Root Matrix)** Let $A = P\Lambda P^{\mathsf T} = \sum_{i=1}^{k}\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$ be symmetric and nonnegative definite. The matrix

$$
A^{1/2} = P\Lambda^{1/2}P^{\mathsf T} = \sum_{i=1}^{k}\sqrt{\lambda_i}\,\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}, \qquad \Lambda^{1/2} = \operatorname{diag}(\sqrt{\lambda_1}, \dots, \sqrt{\lambda_k}),
$$
is called the **square root matrix** of $A$.

**Property 1.6.1** Let $A$ be symmetric positive definite, $A = P\Lambda P^{\mathsf T}$ with all $\lambda_i > 0$. Then

1. $A^{-1} = P\Lambda^{-1}P^{\mathsf T} = \sum_{i=1}^{k}\frac{1}{\lambda_i}\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$;
2. $(A^{1/2})^{\mathsf T} = A^{1/2}$ and $A^{1/2}A^{1/2} = A$;
3. $(A^{1/2})^{-1} = P\Lambda^{-1/2}P^{\mathsf T} = \sum_{i=1}^{k}\frac{1}{\sqrt{\lambda_i}}\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$, written $A^{-1/2}$;
4. $A^{1/2}A^{-1/2} = A^{-1/2}A^{1/2} = I$ and $A^{-1/2}A^{-1/2} = A^{-1}$.

All four follow from $P^{\mathsf T}P = I$: for example $A^{1/2}A^{1/2} = P\Lambda^{1/2}P^{\mathsf T}P\Lambda^{1/2}P^{\mathsf T} = P\Lambda P^{\mathsf T} = A$. The same pattern defines any function of a symmetric matrix through its eigenvalues.

### 1.6.4. Geometric Interpretation of the Mahalanobis Distance

We now derive the Mahalanobis distance from the requirement in Section 1.3.1: find new coordinates in which the data are spherical, so that the Euclidean distance becomes appropriate. Assume without loss of generality that the mean is $\boldsymbol{0}$, and let $\Sigma = P\Lambda P^{\mathsf T}$ be the spectral decomposition of the covariance matrix of $\boldsymbol{X}$.

We look for $\boldsymbol{Y}$ with $\operatorname{Cov}(\boldsymbol{Y}) = I$ (data distributed on spheres rather than ellipsoids) and a rotation $\tilde P$ and rescaling $\tilde\Lambda$ (diagonal, positive) with $\boldsymbol{X} = \tilde P\tilde\Lambda\boldsymbol{Y}$. Then

$$
\Sigma = \operatorname{Cov}(\boldsymbol{X}) = \tilde P\tilde\Lambda\operatorname{Cov}(\boldsymbol{Y})\tilde\Lambda\tilde P^{\mathsf T} = \tilde P\tilde\Lambda^2\tilde P^{\mathsf T},
$$
so by uniqueness of the spectral decomposition we may take $\tilde P = P$ and $\tilde\Lambda = \Lambda^{1/2}$: the rotation is given by the eigenvectors of $\Sigma$ and the scales by the square roots of its eigenvalues. The squared Euclidean length in the new coordinates is

$$
\boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} = \boldsymbol{X}^{\mathsf T}P\Lambda^{-1/2}\Lambda^{-1/2}P^{\mathsf T}\boldsymbol{X} = \boldsymbol{X}^{\mathsf T}P\Lambda^{-1}P^{\mathsf T}\boldsymbol{X} = \boldsymbol{X}^{\mathsf T}\Sigma^{-1}\boldsymbol{X},
$$
which is the squared Mahalanobis distance. In practice $\Sigma$ is estimated by the sample covariance matrix $S = \hat P\hat\Lambda\hat P^{\mathsf T}$, the rotation is given by $\hat P$, and the distance used is $\boldsymbol{x}^{\mathsf T}S^{-1}\boldsymbol{x}$.

**Remark 1.6.1** Why does the rotation $P^{\mathsf T}$ turn a tilted ellipse into one aligned with the axes? A tilted ellipse means that the components are correlated, $\sigma_{12} \ne 0$. After the rotation,

$$
\operatorname{Cov}(P^{\mathsf T}\boldsymbol{X}) = P^{\mathsf T}\Sigma P = P^{\mathsf T}P\Lambda P^{\mathsf T}P = \Lambda
$$
is diagonal: the new coordinates are uncorrelated, and the ellipse is aligned with the new axes. The rescaling $\Lambda^{-1/2}$ then gives every axis unit variance and turns the ellipse into a circle. The essential point is that the matrix used in the distance is the covariance matrix of the very data being measured.

## 1.7. Singular Value Decomposition and Matrix Inequalities

### 1.7.1. Singular Value Decomposition

**Theorem 1.7.1 (Singular Value Decomposition)** Let $A$ be an $m \times k$ real matrix. There exist an $m \times m$ orthogonal matrix $U$ and a $k \times k$ orthogonal matrix $V$ such that

$$
A = U\Lambda V^{\mathsf T},
$$
where $\Lambda$ is $m \times k$ with $(i, i)$ entry $\lambda_i \ge 0$ for $i = 1, \dots, \min(m, k)$ and all other entries zero. The positive $\lambda_i$ are the **singular values** of $A$.

This is the **singular value decomposition** of [2.1.7](/2.1.7). From it, $AA^{\mathsf T} = U\Lambda\Lambda^{\mathsf T}U^{\mathsf T}$ and $A^{\mathsf T}A = V\Lambda^{\mathsf T}\Lambda V^{\mathsf T}$ are the spectral decompositions of the two symmetric matrices: the columns of $U$ and $V$ are their eigenvectors and the squared singular values $\lambda_i^2$ their nonzero eigenvalues. Geometrically, a general matrix acts on the data by $A\boldsymbol{x} = U(\Lambda(V^{\mathsf T}\boldsymbol{x}))$: change to the coordinates given by $V$, stretch each axis by $\lambda_i$ (dropping or adding dimensions when $m \ne k$), and rotate by $U$ into the target space. Unlike the spectral decomposition, the coordinate systems before and after the stretching differ.

### 1.7.2. The Extended Cauchy–Schwarz Inequality

The **Cauchy–Schwarz inequality** says that for any $p \times 1$ vectors $\boldsymbol{b}$ and $\boldsymbol{d}$,

$$
(\boldsymbol{b}^{\mathsf T}\boldsymbol{d})^2 \le (\boldsymbol{b}^{\mathsf T}\boldsymbol{b})(\boldsymbol{d}^{\mathsf T}\boldsymbol{d}),
$$
with equality if and only if $\boldsymbol{b} = c\boldsymbol{d}$ (or $\boldsymbol{d} = c\boldsymbol{b}$) for some constant $c$.

**Lemma 1.7.1 (Extended Cauchy–Schwarz Inequality)** Let $\boldsymbol{b}$ and $\boldsymbol{d}$ be $p \times 1$ vectors and $B$ a $p \times p$ positive definite matrix. Then

$$
(\boldsymbol{b}^{\mathsf T}\boldsymbol{d})^2 \le (\boldsymbol{b}^{\mathsf T}B\boldsymbol{b})(\boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d}),
$$
with equality if and only if $\boldsymbol{b} = cB^{-1}\boldsymbol{d}$ (or $\boldsymbol{d} = \boldsymbol{0}$) for some constant $c$.

**Proof** Write $\boldsymbol{b}^{\mathsf T}\boldsymbol{d} = \boldsymbol{b}^{\mathsf T}B^{1/2}B^{-1/2}\boldsymbol{d} = (B^{1/2}\boldsymbol{b})^{\mathsf T}(B^{-1/2}\boldsymbol{d})$ and apply the Cauchy–Schwarz inequality to the vectors $B^{1/2}\boldsymbol{b}$ and $B^{-1/2}\boldsymbol{d}$, whose squared lengths are $\boldsymbol{b}^{\mathsf T}B\boldsymbol{b}$ and $\boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d}$. Equality holds if and only if $B^{1/2}\boldsymbol{b} = cB^{-1/2}\boldsymbol{d}$, that is, $\boldsymbol{b} = cB^{-1}\boldsymbol{d}$. $\square$

**Lemma 1.7.2 (Maximization Lemma)** Let $B$ be a $p \times p$ positive definite matrix and $\boldsymbol{d}$ a given $p \times 1$ vector. Then

$$
\max_{\boldsymbol{x} \ne \boldsymbol{0}}\frac{(\boldsymbol{x}^{\mathsf T}\boldsymbol{d})^2}{\boldsymbol{x}^{\mathsf T}B\boldsymbol{x}} = \boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d},
$$
with the maximum attained at $\boldsymbol{x} = cB^{-1}\boldsymbol{d}$ for any constant $c \ne 0$.

**Proof** By Lemma 1.7.1, $(\boldsymbol{x}^{\mathsf T}\boldsymbol{d})^2 \le (\boldsymbol{x}^{\mathsf T}B\boldsymbol{x})(\boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d})$; divide by $\boldsymbol{x}^{\mathsf T}B\boldsymbol{x} > 0$. The bound is attained exactly when $\boldsymbol{x} = cB^{-1}\boldsymbol{d}$. $\square$

The maximization lemma is the algebraic core of the simultaneous confidence intervals of [3.4.3](/3.4.3) and of discriminant analysis ([3.4.10](/3.4.10)).

**Theorem 1.7.2 (Maximization of Quadratic Forms on the Unit Sphere)** Let $B$ be a $p \times p$ positive definite matrix with eigenvalues $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_p > 0$ and associated normalized eigenvectors $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$. Then

$$
\max_{\boldsymbol{x} \ne \boldsymbol{0}}\frac{\boldsymbol{x}^{\mathsf T}B\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}} = \lambda_1 \ (\text{attained at } \boldsymbol{x} = \boldsymbol{e}_1), \qquad \min_{\boldsymbol{x} \ne \boldsymbol{0}}\frac{\boldsymbol{x}^{\mathsf T}B\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}} = \lambda_p \ (\text{attained at } \boldsymbol{x} = \boldsymbol{e}_p).
$$
Moreover, for $k = 1, \dots, p - 1$,

$$
\max_{\boldsymbol{x} \perp \boldsymbol{e}_1, \dots, \boldsymbol{e}_k}\frac{\boldsymbol{x}^{\mathsf T}B\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}} = \lambda_{k+1} \quad (\text{attained at } \boldsymbol{x} = \boldsymbol{e}_{k+1}).
$$

The ratio is the **Rayleigh quotient**, and the theorem is [Theorem 7.2.1](/2.1.7#thm-7.2.1) of linear algebra (it holds for any symmetric $B$). In the coordinates $\boldsymbol{y} = P^{\mathsf T}\boldsymbol{x}$ the quotient is $\sum_i\lambda_iy_i^2/\sum_iy_i^2$, a weighted average of the eigenvalues. Theorem 1.7.2 is the basis of principal component analysis ([3.4.5](/3.4.5)): the direction of maximal variance of $\boldsymbol{x}^{\mathsf T}\boldsymbol{X}$ among unit vectors is $\boldsymbol{e}_1$.

## 1.8. Vector and Matrix Calculus

Maximum likelihood estimation for multivariate models requires derivatives with respect to vectors and matrices. Two layouts are in use, and they differ by a transpose.

**Definition 1.8.1 (Numerator and Denominator Layouts)** Let $\boldsymbol{y} = (y_1, \dots, y_q)^{\mathsf T}$ be a function of $\boldsymbol{x} = (x_1, \dots, x_p)^{\mathsf T}$. In the **numerator layout**, $\frac{\partial\boldsymbol{y}}{\partial\boldsymbol{x}}$ is the $q \times p$ matrix with $(i, k)$ entry $\frac{\partial y_i}{\partial x_k}$, arranged by $\boldsymbol{y}$ and $\boldsymbol{x}^{\mathsf T}$; in the **denominator layout**, it is the $p \times q$ matrix with $(k, i)$ entry $\frac{\partial y_i}{\partial x_k}$, arranged by $\boldsymbol{y}^{\mathsf T}$ and $\boldsymbol{x}$. For a scalar function $f$ of a $p \times p$ matrix $A$, the denominator layout gives the $p \times p$ matrix $\frac{\partial f}{\partial A} = \left(\frac{\partial f}{\partial a_{ik}}\right)$.

In the denominator layout, the derivative of a scalar with respect to a column vector is a column vector (the **gradient**). The numerator-layout derivative of $\boldsymbol{y}$ is the **Jacobian matrix** $J_f(\boldsymbol{x})$ of $f\colon \mathbb{R}^p \to \mathbb{R}^q$, the matrix of the total derivative ($q \times p$), and the chain rule reads

$$
J_{f \circ g}(\boldsymbol{x}) = J_f(g(\boldsymbol{x}))\,J_g(\boldsymbol{x}) \quad (\text{numerator layout}), \qquad H_{f \circ g}(\boldsymbol{x}) = H_g(\boldsymbol{x})\,H_f(g(\boldsymbol{x})) \quad (\text{denominator layout}),
$$
where $H = J^{\mathsf T}$ denotes the denominator-layout derivative. The order of the factors reverses with the transpose.

**Example 1.8.1** Let $\boldsymbol{y} = A\boldsymbol{x}$ with $A = \begin{bmatrix} 1 & 3 \\ 0 & 2 \\ 0 & 1 \end{bmatrix}$, that is, $y_1 = x_1 + 3x_2$, $y_2 = 2x_2$, $y_3 = x_2$. In the numerator layout $\frac{\partial\boldsymbol{y}}{\partial\boldsymbol{x}} = \begin{bmatrix} 1 & 3 \\ 0 & 2 \\ 0 & 1 \end{bmatrix} = A$; in the denominator layout $\frac{\partial\boldsymbol{y}}{\partial\boldsymbol{x}} = \begin{bmatrix} 1 & 0 & 0 \\ 3 & 2 & 1 \end{bmatrix} = A^{\mathsf T}$.

Unless stated otherwise we use the denominator layout.

**Property 1.8.1** Let $\boldsymbol{x}$ be a vector and $A$ a constant matrix of compatible size. In the denominator layout,

$$
\frac{\partial A\boldsymbol{x}}{\partial\boldsymbol{x}} = A^{\mathsf T}, \qquad \frac{\partial\boldsymbol{x}^{\mathsf T}A}{\partial\boldsymbol{x}} = A, \qquad \frac{\partial\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}{\partial\boldsymbol{x}} = 2\boldsymbol{x}, \qquad \frac{\partial\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\partial\boldsymbol{x}} = A\boldsymbol{x} + A^{\mathsf T}\boldsymbol{x}.
$$
In particular $\frac{\partial\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\partial\boldsymbol{x}} = 2A\boldsymbol{x}$ for symmetric $A$.

**Example 1.8.2** Let $A$ be symmetric positive definite. By the chain rule (denominator layout) with the inner function $g(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$ and the outer function $\log$,

$$
\frac{\partial}{\partial\boldsymbol{x}}\log(\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}) = \frac{\partial(\boldsymbol{x}^{\mathsf T}A\boldsymbol{x})}{\partial\boldsymbol{x}}\cdot\frac{1}{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}} = \frac{2A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}, \qquad \boldsymbol{x} \ne \boldsymbol{0}.
$$

**Property 1.8.2 (Derivatives of the Determinant and the Trace)** Let $A$ be a $p \times p$ symmetric positive definite matrix and $B$ a $p \times p$ constant matrix. In the denominator layout,

$$
\frac{\partial\det A}{\partial A} = (\det A)A^{-1}, \qquad \frac{\partial\log\det A}{\partial A} = A^{-1}, \qquad \frac{\partial\operatorname{tr}(AB)}{\partial A} = B^{\mathsf T},
$$

$$
\frac{\partial\operatorname{tr}(A^{-1}B)}{\partial A} = -A^{-1}B^{\mathsf T}A^{-1}, \qquad \frac{\partial\operatorname{tr}(B^{\mathsf T}A^{-1}B)}{\partial A} = -A^{-1}BB^{\mathsf T}A^{-1}.
$$

**Remark 1.8.1** These formulas treat the $p^2$ entries of $A$ as free variables; for a general (nonsymmetric) $A$ the first one reads $(\det A)(A^{-1})^{\mathsf T}$, which equals $(\det A)A^{-1}$ when $A$ is symmetric. If the symmetry $a_{ik} = a_{ki}$ is imposed as a constraint, the off-diagonal entries of the derivatives change by a factor, but the equation "derivative $= O$" has the same solutions, which is all that maximum likelihood estimation needs ([3.4.2](/3.4.2)). Matrix calculus is a tool rather than a goal of the course: it lets the multivariate maximum likelihood computation follow the familiar one-dimensional route, and it is good practice with matrix operations, but later chapters use it rarely.

## Summary

- Multivariate data: an $n \times p$ data matrix $X$ whose rows are items and columns are variables; under random sampling the rows $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ are iid with mean vector $\boldsymbol{\mu}$ and covariance matrix $\Sigma$, while the variables within a row are correlated. Two pictures: $n$ points in $\mathbb{R}^p$, or $p$ vectors in $\mathbb{R}^n$.
- The Euclidean distance ignores units and correlations; the Mahalanobis distance $\sqrt{(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})}$ is the Euclidean distance after rotating onto the eigenvectors of $\Sigma$ and rescaling to unit variance. $\mathbb{E}[\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}] = \operatorname{tr}(A\Sigma_Z) + \boldsymbol{\mu}_Z^{\mathsf T}A\boldsymbol{\mu}_Z$; the expected squared Euclidean distance is $\operatorname{tr}\Sigma$ and the expected squared Mahalanobis distance is $p$.
- Exploratory graphics: boxplots and histograms for one variable; scatter plots, scatter plot matrices, heatmaps, star plots, faces and curves for several.
- Matrix tools: orthogonal matrices change coordinates; $A = P\Lambda P^{\mathsf T} = \sum\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$ (rotate, stretch, rotate back); $A^{\pm 1/2} = P\Lambda^{\pm 1/2}P^{\mathsf T}$; $A = U\Lambda V^{\mathsf T}$ for any matrix.
- Inequalities: $(\boldsymbol{b}^{\mathsf T}\boldsymbol{d})^2 \le (\boldsymbol{b}^{\mathsf T}B\boldsymbol{b})(\boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d})$; $\max_{\boldsymbol{x}}(\boldsymbol{x}^{\mathsf T}\boldsymbol{d})^2/\boldsymbol{x}^{\mathsf T}B\boldsymbol{x} = \boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d}$; the Rayleigh quotient ranges over $[\lambda_p, \lambda_1]$.
- Matrix calculus in the denominator layout: $\partial\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}/\partial\boldsymbol{x} = (A + A^{\mathsf T})\boldsymbol{x}$, $\partial\log\det A/\partial A = A^{-1}$, $\partial\operatorname{tr}(A^{-1}B)/\partial A = -A^{-1}B^{\mathsf T}A^{-1}$.
