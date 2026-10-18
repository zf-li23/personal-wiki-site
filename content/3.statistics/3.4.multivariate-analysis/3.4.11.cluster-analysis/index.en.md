---
title: Cluster Analysis
description: Hierarchical clustering with different linkages, k-means and its variants, choosing the number of clusters, Gaussian mixture models fitted by the EM algorithm, and model selection by BIC.
---

Discriminant analysis ([3.4.10](/3.4.10)) learns a classification rule from observations whose groups are known. Cluster analysis asks the same question without the labels: given only the measurements, are there natural groups, and which observations belong together? It is the basic tool of unsupervised learning. This chapter covers the three main families of methods: hierarchical clustering, which builds a tree of nested groups from a matrix of distances; partitioning methods such as $k$-means, which minimize a within-cluster criterion; and model-based clustering, which fits a mixture of **multivariate normal distributions** by the EM algorithm and turns the choice of the number of clusters into a model-selection problem. Model-based clustering is the unsupervised counterpart of the normal-theory discriminant analysis of the previous chapter: the model is the same, but the labels are missing. Distances between observations ([3.4.1](/3.4.1)) and **multidimensional scaling** ([3.4.6](/3.4.6)) for visualization are used throughout.

## 11.1. Introduction

Take the iris data again and suppose the species labels have been lost: can the four measurements alone reveal the groups? Or consider an imaging study of about 2000 subjects in which about 12000 of the 47473 voxels in the brain are activated, falling into 26 anatomical regions. Two questions arise: how are the 26 regions related, and can a region of interest, such as the insula, be divided into functionally different subregions? The first question groups variables (regions), the second groups units (voxels); cluster analysis handles both.

A cluster is a collection of objects that are similar (or related) to one another within the same group and dissimilar (or unrelated) to the objects in other groups. *Cluster analysis* (also called clustering, data segmentation, or community detection in networks) finds similarities between objects from their measured characteristics and groups similar objects into clusters, so that intra-cluster distances are small and inter-cluster distances are large. There are no predefined classes: clustering is *unsupervised learning*, learning from observations, whereas discriminant analysis is *supervised learning*, learning from labeled examples.

Cluster analysis is used in two ways:

- for understanding, as a stand-alone tool to gain insight into the distribution of the data, for instance grouping related documents for browsing, or genes and proteins with similar functions;
- for summarization, as a preprocessing step that reduces a large data set to a few representative groups for subsequent analysis.

The major approaches are:

| Approach | Idea | Typical methods |
|---|---|---|
| Hierarchical | create a hierarchical decomposition of the data using some criterion | AGNES, DIANA, BIRCH, CHAMELEON |
| Partitioning | construct partitions and evaluate them by some criterion | $k$-means, $k$-medoids, CLARANS |
| Model-based | hypothesize a model for each cluster and find the best fit | Gaussian mixtures fitted by EM, SOM, COBWEB |

## 11.2. Hierarchical Clustering

### 11.2.1. Agglomerative and Divisive Clustering

*Hierarchical clustering* produces a set of nested clusters organized as a tree. The tree is displayed as a *dendrogram*, a tree diagram that records the sequence of merges or splits: the leaves are the observations, and the height at which two branches join is the distance between the clusters being merged. There are two main types.

- Agglomerative: start with each point as its own cluster, and at each step merge the closest pair of clusters, until only one cluster (or $k$ clusters) is left.
- Divisive: start with one all-inclusive cluster, and at each step split a cluster, until each cluster contains one point (or there are $k$ clusters).

Agglomerative clustering is far more common, and it is the subject of the rest of this section. To quantify closeness it works with a distance (or dissimilarity) matrix, and two choices must be made: the distance between points, and the distance between clusters, which is defined from the distances between points.

### 11.2.2. Distances Between Points

The distance between points should fit the type of data: the Euclidean distance (or the Mahalanobis distance) for numerical data; $1 - r$, with $r$ the correlation, when the shape of a profile matters more than its level; the Jaccard or Hamming distance for binary or categorical data. For text and other sparse high-dimensional data, the angle between vectors is a natural measure.

**Definition 11.2.1 (Cosine Similarity)** The **cosine similarity** of two nonzero vectors $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^p$ is

$$
\cos(\boldsymbol{a}, \boldsymbol{b}) = \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\|\boldsymbol{a}\|\,\|\boldsymbol{b}\|} \in [-1, 1],
$$
and $1 - \cos(\boldsymbol{a}, \boldsymbol{b}) \in [0, 2]$ is the corresponding dissimilarity.

For example, a document can be represented by the vector of (weighted) frequencies of the words of a vocabulary; most entries are $0$, and the cosine similarity compares the proportions of words regardless of the lengths of the documents. For centered vectors the cosine similarity is the correlation.

### 11.2.3. Distances Between Clusters

**Definition 11.2.2 (Linkage)** Let $d(\boldsymbol{x}, \boldsymbol{y})$ be a distance between points, and let $A, B$ be disjoint clusters with $\lvert A\rvert, \lvert B\rvert$ points and centroids (mean vectors) $\boldsymbol{m}_A, \boldsymbol{m}_B$. The distance between $A$ and $B$ is defined by a *linkage*:

1. **single linkage** (minimum): $d(A, B) = \min_{\boldsymbol{x}\in A, \boldsymbol{y}\in B} d(\boldsymbol{x}, \boldsymbol{y})$, the distance between the closest pair;
2. **complete linkage** (maximum): $d(A, B) = \max_{\boldsymbol{x}\in A, \boldsymbol{y}\in B} d(\boldsymbol{x}, \boldsymbol{y})$, the distance between the farthest pair;
3. **average linkage** (group average): $d(A, B) = \frac{1}{\lvert A\rvert\lvert B\rvert}\sum_{\boldsymbol{x}\in A}\sum_{\boldsymbol{y}\in B} d(\boldsymbol{x}, \boldsymbol{y})$;
4. **centroid linkage**: $d(A, B) = \|\boldsymbol{m}_A - \boldsymbol{m}_B\|$, the distance between the centroids;
5. **Ward's method**: $d(A, B)$ is the increase in the within-cluster sum of squared errors caused by merging $A$ and $B$ (see below).

Ward's method measures the cost of a merge by the within-cluster sum of squared errors. For a partition into clusters $C_1, \dots, C_K$ with centers $\boldsymbol{m}_1, \dots, \boldsymbol{m}_K$, the error of a point is its distance to the center of its cluster, and

$$
\mathrm{SSE} = \sum_{i=1}^K\sum_{\boldsymbol{x}\in C_i}\|\boldsymbol{x} - \boldsymbol{m}_i\|^2.
$$
Ward's method merges the pair of clusters that increases the SSE least, that is, it compares $\mathrm{SSE}_{A\cup B} - \mathrm{SSE}_A - \mathrm{SSE}_B$ over all pairs. A short computation (the decomposition of the total sum of squares about the merged centroid into within and between parts) gives

$$
\mathrm{SSE}_{A\cup B} - \mathrm{SSE}_A - \mathrm{SSE}_B = \frac{\lvert A\rvert\,\lvert B\rvert}{\lvert A\rvert + \lvert B\rvert}\|\boldsymbol{m}_A - \boldsymbol{m}_B\|^2,
$$
a centroid distance weighted by the cluster sizes, which penalizes merging two large clusters.

### 11.2.4. The Agglomerative Algorithm

**Algorithm 11.2.1 (Agglomerative Hierarchical Clustering)** Given $n$ points, a distance between points and a linkage:

1. let each data point be a cluster;
2. compute the $n \times n$ distance matrix;
3. repeat: merge the two closest clusters, and update the distance matrix by computing the distances from the new cluster to the others;
4. until only a single cluster remains.

The dendrogram draws the merges in order, each at the height of the distance at which it happened. To obtain $k$ clusters, cut the dendrogram with a horizontal line that crosses exactly $k$ vertical branches; the clusters are the subtrees below the cut. The number of clusters need not be fixed in advance: any number can be read off by cutting at a different level.

**Example 11.2.1** Cluster the six points $(0,0)$, $(1,2)$, $(2,1)$, $(4,1)$, $(5.2,0)$, $(5,3)$ with the Euclidean distance and centroid linkage.

1. The closest pair is $(1,2)$ and $(2,1)$, at distance $\sqrt2 \approx 1.414$; they merge into a cluster with centroid $(1.5, 1.5)$.
2. Next, $(4,1)$ and $(5.2,0)$, at distance $\sqrt{2.44} \approx 1.562$, merge with centroid $(4.6, 0.5)$.
3. The closest pair is now $(0,0)$ and the centroid $(1.5,1.5)$, at distance $\approx 2.121$; the new cluster of three points has centroid $(1, 1)$.
4. Then $(5,3)$ joins the cluster with centroid $(4.6, 0.5)$, at distance $\approx 2.532$; the new centroid is $(4.73, 1.33)$.
5. Finally the two clusters merge at distance $\lVert(1,1) - (4.73,1.33)\rVert \approx 3.748$; the centroid of all six points is $(2.87, 1.17)$.

Cutting the dendrogram between heights $2.53$ and $3.75$ gives two clusters, $\{(0,0), (1,2), (2,1)\}$ and $\{(4,1), (5.2,0), (5,3)\}$. Note that the centroid of a merged cluster is the weighted mean of the two centroids, not their midpoint.

![The six points of the example (left) and the dendrogram of agglomerative clustering with centroid linkage (right); the dashed line cuts the tree into two clusters.](./plots/six-point-dendrogram.py)

### 11.2.5. Comparing Linkages

The linkages produce clusters of different shapes.

| Linkage | Strengths | Weaknesses |
|---|---|---|
| single | handles irregularly shaped (non-elliptical) clusters fairly naturally | sensitive to noise and outliers, which produce "chaining": long straggly clusters joined through intermediate points |
| complete | less sensitive to noise and outliers; compact clusters | clusters are biased toward globular shapes and may violate closeness (a point may be much closer to some points of a neighboring cluster than to its own), which shows as breaking large clusters |
| average | a compromise between single and complete linkage: globular clusters like complete linkage, less sensitive to noise than single linkage | |
| Ward | similar to average linkage when the dissimilarity is the squared distance; a hierarchical analogue of $k$-means, sometimes used to initialize $k$-means | biased toward globular clusters of similar size |

**Example 11.2.2** For the iris data with the Euclidean distance (in R, `hclust(dist(iris[, -5]), method)` followed by `cutree(res, k = 3)`), single linkage separates setosa but chains all the versicolor and virginica flowers except two outlying points into one cluster, so its three clusters have sizes $50$, $98$ and $2$. Complete, average and Ward linkage give dendrograms with more balanced branches and also separate setosa. Average and Ward linkage split the remaining flowers roughly along the species, with about $15$ virginica flowers grouped with versicolor, while complete linkage breaks the versicolor flowers into two parts, the "breaking large clusters" weakness.

![Dendrograms of the iris data (Euclidean distance) under four linkages. Single linkage shows chaining; the other three show a clear setosa branch and two further groups.](./plots/iris-linkage-dendrograms.py)

**Example 11.2.3** In the imaging study, the 26 brain regions were clustered using $1 - r$ (with $r$ the correlation of activation across 1709 subjects) and average linkage. Cutting the tree at six clusters groups regions that are activated together, for instance the left and right parts of the same structure, and the putamen with the pallidum.

### 11.2.6. Strengths, Limitations and Extensions

Agglomerative clustering does not require the number of clusters in advance, since any number can be obtained by cutting the dendrogram at the proper level, and the dendrogram displays the relations among objects intuitively, as in the phylogenetic trees that biologists use to show the evolutionary relations among species.

Its limitations are computational and statistical.

- It needs $O(n^2)$ space for the distance matrix, and the straightforward algorithm needs $O(n^3)$ time: there are $n$ steps, and at each step a matrix of size $n^2$ is searched and updated.
- A merge, once made, cannot be undone.
- No objective function is directly minimized.
- Depending on the linkage, it is sensitive to noise and outliers, has difficulty with clusters of different sizes and non-convex shapes, or breaks large clusters.

**Remark 11.2.1** The cubic running time is not intrinsic. Single linkage clustering is equivalent to building a minimum spanning tree of the complete graph weighted by the distances, which Prim's algorithm does in $O(n^2)$ time. For complete, average and Ward linkage the naive algorithm repeats much of its work, and the nearest-neighbor chain algorithm also reaches $O(n^2)$.

Extensions address these limitations: BIRCH (1996) summarizes the data in a CF-tree (clustering feature tree) and adjusts the subclusters incrementally, running in $O(n)$ time; CHAMELEON (1999) uses dynamic modeling to merge clusters and can handle complex shapes.

## 11.3. Partitioning Clustering: k-Means

### 11.3.1. The Algorithm

*Partitioning clustering* divides the data into non-overlapping subsets (clusters) such that each object is in exactly one subset. The most commonly used partitioning method is $k$-means.

**Algorithm 11.3.1 (k-Means Clustering)** Given $n$ points and the number of clusters $k$:

1. choose $k$ initial centroids;
2. repeat: assign each point to the cluster of its nearest centroid, and update the centroid of each cluster to the mean of its points;
3. until the assignments no longer change.

To apply $k$-means we must specify the number of clusters $k$, the distance between points (Euclidean as standard; correlation-based distances are also used), and the initial centroids. Common choices for the initialization are: $k$ randomly chosen data points; the cluster means of a hierarchical clustering of a sample of the data; or one random point followed by $k-1$ further points, each as far away as possible from the previous ones (for instance the leader algorithm, which requires each new center to be at least a distance $d$ from the earlier ones). The result can depend strongly on the initial values, so in practice $k$-means is run from many random starts and the solution with the smallest SSE is kept.

### 11.3.2. The Objective

Let $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ be the data, $\boldsymbol{\mu}_1, \dots, \boldsymbol{\mu}_k$ the cluster centroids, and $c_i \in \{1, \dots, k\}$ the cluster of $\boldsymbol{x}_i$. The total SSE

$$
J(c, \boldsymbol{\mu}) = \sum_{i=1}^n\|\boldsymbol{x}_i - \boldsymbol{\mu}_{c_i}\|^2
$$
is the objective that $k$-means minimizes, and Algorithm 11.3.1 is coordinate descent on it:

1. optimize $c$ given $\boldsymbol{\mu}$: $c_i = \arg\min_j\|\boldsymbol{x}_i - \boldsymbol{\mu}_j\|^2$ (the assignment step);
2. optimize $\boldsymbol{\mu}$ given $c$: $\boldsymbol{\mu}_j = \arg\min_{\boldsymbol{\mu}}\sum_{i : c_i = j}\|\boldsymbol{x}_i - \boldsymbol{\mu}\|^2$, which is the mean of the points in cluster $j$ (the update step).

**Proposition 11.3.1** Each step of Algorithm 11.3.1 does not increase $J$, and the algorithm terminates after finitely many iterations at a partition that cannot be improved by either step alone. This is a local minimum of $J$; the global minimum is not guaranteed.

**Proof** The assignment step minimizes $J$ over $c$ with $\boldsymbol{\mu}$ fixed, and the update step minimizes it over $\boldsymbol{\mu}$ with $c$ fixed, because $\sum_{i\in C}\|\boldsymbol{x}_i - \boldsymbol{\mu}\|^2 = \sum_{i\in C}\|\boldsymbol{x}_i - \bar{\boldsymbol{x}}_C\|^2 + \lvert C\rvert\,\|\bar{\boldsymbol{x}}_C - \boldsymbol{\mu}\|^2$ is smallest at the cluster mean $\bar{\boldsymbol{x}}_C$. Hence $J$ is nonincreasing. There are finitely many partitions, and (breaking ties consistently) no partition can recur once $J$ has strictly decreased, so the assignments stop changing after finitely many iterations. $\square$

### 11.3.3. Choosing k

Choosing $k$ is a matter of balance: with too few clusters many points are far from their centroid; with too many, adding clusters barely reduces the average distance. The SSE alone cannot decide, since it decreases as $k$ increases and is $0$ when every point is its own cluster. Common approaches are the following.

1. The *elbow method*: plot the minimal SSE against $k$; it falls rapidly up to some $k$ and changes little afterwards, and the turning point of the curve is chosen as $k$.
2. An empirical rule of thumb: $k \approx \sqrt{n/2}$ for $n$ points, for instance $k = 10$ for $n = 200$.
3. The silhouette coefficient (Definition 11.3.1): choose the $k$ that maximizes the average silhouette over all points.
4. The *gap statistic* (Tibshirani, Walther and Hastie, 2001): compare $\ln\mathrm{SSE}_k$ with its expectation under a reference distribution without clusters, and choose the $k$ where the gap is large (in R, `cluster::clusGap`).
5. Cross-validation: divide the data into $m$ parts, use $m-1$ parts to obtain a clustering and the remaining part to test its quality (for instance the SSE of the held-out points with respect to the fitted centroids), repeat $m$ times for each $k$, and choose the $k$ with the best overall quality.

**Definition 11.3.1 (Silhouette Coefficient)** For a clustering and a dissimilarity $d$, let $C(i)$ be the cluster of point $i$. Let

$$
a(i) = \frac{1}{\lvert C(i)\rvert - 1}\sum_{j\in C(i), j\ne i} d(i, j)
$$
be the average dissimilarity of $i$ to the other points of its cluster, and

$$
b(i) = \min_{C \ne C(i)}\frac{1}{\lvert C\rvert}\sum_{j\in C} d(i, j)
$$
the average dissimilarity to the closest cluster other than its own. The **silhouette coefficient** of point $i$ is

$$
s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}} \in [-1, 1].
$$

A value close to $1$ means that the point is much closer to its own cluster than to the next one; a value near $0$ means it lies between two clusters; a negative value suggests that it is in the wrong cluster.

**Example 11.3.1** For the iris data, `kmeans(iris[, -5], 3)` finds three clusters, but different random initial values can give different partitions. To visualize the result, project the four-dimensional data onto two dimensions by classical multidimensional scaling (`cmdscale`) and color the points by cluster; compared with the species, setosa forms its own cluster while versicolor and virginica are partly mixed.

**Example 11.3.2** In the imaging study, the 650 voxels of the insula were clustered by $k$-means with the correlation distance, using the cluster means of an average-linkage hierarchical clustering as initial centers. The within-group SSE, plotted against the number of clusters, shows an elbow at $k = 3$, and the three subregions turn out to be associated with different functions: inhibition and reaction time, goal-directed cognition, and emotion (such as seeing disgusted faces).

### 11.3.4. Strengths, Limitations and Extensions

$k$-means is efficient: its cost is $O(tkn)$ for $n$ objects, $k$ clusters and $t$ iterations, and normally $k, t \ll n$. Its limitations are:

1. it is sensitive to outliers, since a mean can be pulled far by a single point;
2. it has problems when the clusters have different sizes, different densities or non-convex shapes, because it implicitly looks for spherical clusters of similar spread;
3. $k$ must be specified in advance, and the result depends on the initial values.

Variants address some of these.

- $k$-modes replaces the means of the clusters by modes, so that it can handle categorical data.
- $k$-medoids uses medoids instead of centroids: the medoid of a cluster is the observation with the smallest total distance to the other members. It is computed by the same alternating algorithm, but the center is always one of the observations, which is useful, for example, when the features are $0$ or $1$, and it reduces the sensitivity to outliers. PAM (Partitioning Around Medoids; Kaufman and Rousseeuw, 1987) implements it; in R, `cluster::pam` uses the Euclidean distance, not its square. CLARA (1990) applies PAM to samples of large data sets, and CLARANS (Ng and Han, 1994) uses randomized search.

## 11.4. Model-Based Clustering

### 11.4.1. Gaussian Mixture Models

Hierarchical clustering, $k$-means and similar algorithms are largely heuristic and not based on formal models, so formal inference is not possible. This is not necessarily a disadvantage, since clustering is largely exploratory, but model-based clustering offers an alternative. It assumes that the observations come from a mixture of two or more components, each describing one cluster by a density function and an associated prior probability, or weight, in the mixture. In principle any probability model can be used; typically the components are multivariate normal.

**Definition 11.4.1 (Gaussian Mixture Model)** Let $Y \sim \mathrm{Mult}(1, \boldsymbol{\pi})$ be a latent label taking the value $l \in \{1, \dots, k\}$ with probability $\pi_l$, $\sum_l\pi_l = 1$, and let $\boldsymbol{X} \mid Y = l \sim \mathcal{N}_p(\boldsymbol{\mu}_l, \Sigma_l)$. The distribution of $\boldsymbol{X}$, with density

$$
f(\boldsymbol{x}) = \sum_{l=1}^k\pi_l\,\phi(\boldsymbol{x}; \boldsymbol{\mu}_l, \Sigma_l),
$$
where $\phi(\cdot\,; \boldsymbol{\mu}, \Sigma)$ is the $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ density, is a **Gaussian mixture model** (GMM); $\pi_l$ are the mixing proportions.

This is the model of QDA (of LDA if all $\Sigma_l$ are equal) in [3.4.10](/3.4.10), with the priors $\pi_l$ and the group densities $\phi(\cdot\,; \boldsymbol{\mu}_l, \Sigma_l)$; the difference is that the labels $Y_i$ are lost and only the $n \times p$ data matrix of $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ is observed. The goal is to estimate $\boldsymbol{\pi}$ and $(\boldsymbol{\mu}_l, \Sigma_l)$, $1 \le l \le k$, and then to assign each observation to the component with the largest posterior probability. Because each observation receives a probability of membership in each cluster rather than a single label, model-based clustering is called *soft clustering*, while hierarchical clustering and $k$-means are *hard clustering*.

The **likelihood function** of $\boldsymbol{\theta} = (\boldsymbol{\pi}, \boldsymbol{\mu}_1, \dots, \boldsymbol{\mu}_k, \Sigma_1, \dots, \Sigma_k)$ is

$$
L(\boldsymbol{\theta}) = \prod_{i=1}^n\sum_{l=1}^k\pi_l\,\phi(\boldsymbol{x}_i; \boldsymbol{\mu}_l, \Sigma_l) = \text{const}\cdot\prod_{i=1}^n\sum_{l=1}^k\pi_l\lvert\Sigma_l\rvert^{-1/2}\exp\left\{-\frac12(\boldsymbol{x}_i-\boldsymbol{\mu}_l)^{\mathsf T}\Sigma_l^{-1}(\boldsymbol{x}_i-\boldsymbol{\mu}_l)\right\},
$$
and the **log-likelihood function** is

$$
\ell(\boldsymbol{\theta}) = \sum_{i=1}^n\ln f(\boldsymbol{x}_i; \boldsymbol{\theta}) = \sum_{i=1}^n\ln\sum_{l=1}^k f(\boldsymbol{x}_i \mid Y_i = l; \boldsymbol{\mu}_l, \Sigma_l)\,\mathbb{P}(Y_i = l; \boldsymbol{\pi}).
$$
The sum inside the logarithm couples all the parameters, and the **maximum likelihood estimation** of these parameters is difficult to carry out directly.

### 11.4.2. The Idea: Two Clusters in One Dimension

Consider observations $x_1, \dots, x_n$ from a mixture of $k = 2$ normal distributions with unknown means and variances, and call the two components $A$ ($Y = 1$) and $B$ ($Y = 2$).

If we knew the cluster of each observation, estimation would be trivial. Suppose $n = 10$ and the first five observations belong to $A$. With the indicators $\boldsymbol{1}_{\{Y_i = 1\}}$ (equal to $1$ for $i \le 5$ and $0$ for $i > 5$),

$$
\hat\pi_1 = \frac{n_1}{n} = \frac{5}{10}, \qquad \hat\mu_1 = \frac{\sum_i\boldsymbol{1}_{\{Y_i=1\}}x_i}{\sum_i\boldsymbol{1}_{\{Y_i=1\}}} = \frac{x_1 + \cdots + x_5}{5}, \qquad \hat\sigma_1^2 = \frac{\sum_i\boldsymbol{1}_{\{Y_i=1\}}(x_i - \hat\mu_1)^2}{\sum_i\boldsymbol{1}_{\{Y_i=1\}}},
$$
and similarly for $B$.

If we do not know the clusters but know the parameters of the two normal distributions, we can compute, for each point, how likely it is to belong to $A$ or $B$, by **Bayes' theorem**:

$$
\gamma_{i1} = \mathbb{P}(Y = 1 \mid X = x_i) = \frac{\pi_1 f_1(x_i)}{\pi_1 f_1(x_i) + \pi_2 f_2(x_i)}, \qquad f_1(x_i) = \frac{1}{\sqrt{2\pi\sigma_1^2}}\exp\left\{-\frac{(x_i-\mu_1)^2}{2\sigma_1^2}\right\},
$$
and $\gamma_{i2} = 1 - \gamma_{i1}$. Suppose these posterior probabilities are $0.9, 0.8, 0.7, 0.6, 0.6, 0.3, 0.2, 0.2, 0.2, 0.1$ for $Y = 1$. Replacing the unknown indicators by these probabilities gives weighted estimates:

$$
\hat\pi_1 = \frac{\sum_i\gamma_{i1}}{n} = \frac{4.6}{10}, \qquad \hat\mu_1 = \frac{0.9x_1 + 0.8x_2 + \cdots + 0.1x_{10}}{4.6}, \qquad \hat\sigma_1^2 = \frac{0.9(x_1-\hat\mu_1)^2 + \cdots + 0.1(x_{10}-\hat\mu_1)^2}{4.6}.
$$

The two steps feed each other: the parameters (cluster features, at the population level) give the membership probabilities, and the membership probabilities (point features, at the sample level) give the parameters. Iterating them is the EM algorithm.

### 11.4.3. The EM Algorithm for Gaussian Mixtures

In general, with $k$ clusters in $p$ dimensions, collect the membership probabilities in the $n \times k$ matrix $\Gamma = [\gamma_{il}]$, $\gamma_{il} = \mathbb{P}(Y_i = l \mid \boldsymbol{X}_i = \boldsymbol{x}_i)$.

**Algorithm 11.4.1 (EM for Gaussian Mixtures)** Initialize $\hat{\boldsymbol{\pi}}^{(0)}$, $\hat{\boldsymbol{\mu}}_l^{(0)}$, $\hat\Sigma_l^{(0)}$. For $t = 0, 1, 2, \dots$ until convergence:

1. (expectation step) for $i = 1, \dots, n$ and $l = 1, \dots, k$,
   $$
   \hat\gamma_{il}^{(t+1)} = \mathbb{P}\bigl(Y_i = l \mid \boldsymbol{X}_i = \boldsymbol{x}_i; \hat{\boldsymbol{\pi}}^{(t)}, \hat{\boldsymbol{\mu}}^{(t)}, \hat\Sigma^{(t)}\bigr) = \frac{\hat\pi_l^{(t)}\phi(\boldsymbol{x}_i; \hat{\boldsymbol{\mu}}_l^{(t)}, \hat\Sigma_l^{(t)})}{\sum_{j=1}^k\hat\pi_j^{(t)}\phi(\boldsymbol{x}_i; \hat{\boldsymbol{\mu}}_j^{(t)}, \hat\Sigma_j^{(t)})};
   $$
2. (maximization step) for $l = 1, \dots, k$,
   $$
   \hat\pi_l^{(t+1)} = \frac{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}}{n}, \qquad \hat{\boldsymbol{\mu}}_l^{(t+1)} = \frac{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}\boldsymbol{x}_i}{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}}, \qquad \hat\Sigma_l^{(t+1)} = \frac{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}(\boldsymbol{x}_i - \hat{\boldsymbol{\mu}}_l^{(t+1)})(\boldsymbol{x}_i - \hat{\boldsymbol{\mu}}_l^{(t+1)})^{\mathsf T}}{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}},
   $$
   that is, a weighted proportion, a weighted average and a weighted covariance matrix, all with weights $\hat\gamma_{il}^{(t+1)}$.

Compare these updates with the estimates in discriminant analysis, where the labels are observed:

| | Hard: observed $Y$ (QDA) | Soft: guessed $Y$ (clustering) |
|---|---|---|
| proportion | $\hat\pi_l = \frac1n\sum_i\boldsymbol{1}_{\{Y_i=l\}}$ | $\hat\pi_l = \frac1n\sum_i\hat\gamma_{il}$ |
| mean | $\hat{\boldsymbol{\mu}}_l = \frac{\sum_i\boldsymbol{1}_{\{Y_i=l\}}\boldsymbol{x}_i}{\sum_i\boldsymbol{1}_{\{Y_i=l\}}}$ | $\hat{\boldsymbol{\mu}}_l = \frac{\sum_i\hat\gamma_{il}\boldsymbol{x}_i}{\sum_i\hat\gamma_{il}}$ |
| covariance | $\hat\Sigma_l = \frac{\sum_i\boldsymbol{1}_{\{Y_i=l\}}(\boldsymbol{x}_i-\hat{\boldsymbol{\mu}}_l)(\boldsymbol{x}_i-\hat{\boldsymbol{\mu}}_l)^{\mathsf T}}{\sum_i\boldsymbol{1}_{\{Y_i=l\}}}$ | $\hat\Sigma_l = \frac{\sum_i\hat\gamma_{il}(\boldsymbol{x}_i-\hat{\boldsymbol{\mu}}_l)(\boldsymbol{x}_i-\hat{\boldsymbol{\mu}}_l)^{\mathsf T}}{\sum_i\hat\gamma_{il}}$ |

The quantities in $\Gamma$ are not really parameters: they are estimates of the unobserved random labels $Y_i$. If $Y$ had been observed, each row of $\Gamma$ would be zero except for a single $1$, and the estimates of $\pi_l, \boldsymbol{\mu}_l, \Sigma_l$ would be exactly those of QDA. The EM algorithm simply replaces the unobserved $Y$ with a guess. In the limit where all components have the covariance matrix $\sigma^2 I$ with $\sigma \to 0$, the posterior probabilities become $0$ or $1$ (each point is assigned to the nearest mean) and EM reduces to $k$-means.

### 11.4.4. The General EM Algorithm

Algorithm 11.4.1 is a special case of the *EM algorithm* (expectation–maximization), a general method for maximum likelihood with missing data. The original target is to maximize

$$
\ell(\boldsymbol{\theta}) = \sum_{i=1}^n\ln\sum_{l=1}^k f(\boldsymbol{x}_i \mid Y_i = l; \boldsymbol{\theta})\,\mathbb{P}(Y_i = l; \boldsymbol{\theta}).
$$
Reformulate it with the missing indicators $\delta_{il} = \boldsymbol{1}_{\{Y_i = l\}}$: if they were observed, the complete-data log-likelihood would be

$$
\ell(\boldsymbol{\delta}, \boldsymbol{\theta}) = \sum_{i=1}^n\ln\prod_{l=1}^k\bigl[\pi_l f_l(\boldsymbol{x}_i; \boldsymbol{\mu}_l, \Sigma_l)\bigr]^{\delta_{il}} = \sum_{i=1}^n\sum_{l=1}^k\delta_{il}\bigl[\ln\pi_l + \ln f_l(\boldsymbol{x}_i; \boldsymbol{\mu}_l, \Sigma_l)\bigr],
$$
which separates into simple terms. Since $\boldsymbol{\delta}$ is unknown, EM alternates two steps, with $\boldsymbol{\theta}^{(t)} = (\boldsymbol{\pi}^{(t)}, \boldsymbol{\mu}^{(t)}, \Sigma^{(t)})$ the current value:

1. E-step: compute $\mathbb{E}[\boldsymbol{\delta} \mid \boldsymbol{\theta}^{(t)}, \boldsymbol{X}]$, which gives $\gamma^{(t+1)}$, and hence
   $$
   B(\boldsymbol{\theta}; \boldsymbol{\theta}^{(t)}) = \mathbb{E}_{\boldsymbol{\delta}\mid\boldsymbol{\theta}^{(t)}, \boldsymbol{X}}\bigl[\ell(\boldsymbol{\delta}, \boldsymbol{\theta})\bigr] = \sum_{i=1}^n\sum_{l=1}^k\gamma_{il}^{(t+1)}\bigl[\ln\pi_l + \ln f_l(\boldsymbol{x}_i; \boldsymbol{\mu}_l, \Sigma_l)\bigr];
   $$
2. M-step: $\boldsymbol{\theta}^{(t+1)} = \arg\max_{\boldsymbol{\theta}} B(\boldsymbol{\theta}; \boldsymbol{\theta}^{(t)})$.

For the Gaussian mixture, maximizing $B$ gives exactly the weighted estimates of Algorithm 11.4.1. Why does maximizing $B$ increase $\ell$? The function $B$ has three properties: its argmax is easy to compute; up to a constant it is a lower bound of $\ell$; and the bound is tight at the current value.

**Theorem 11.4.1 (Ascent Property of EM)** For every $\boldsymbol{\theta}$, $\ell(\boldsymbol{\theta}) \ge \tilde B(\boldsymbol{\theta}, \boldsymbol{\theta}^{(t)})$, where

$$
\tilde B(\boldsymbol{\theta}, \boldsymbol{\theta}^{(t)}) = \ell(\boldsymbol{\theta}^{(t)}) + \sum_{l=1}^k\mathbb{P}(Y = l \mid \boldsymbol{x}, \boldsymbol{\theta}^{(t)})\ln\frac{f(\boldsymbol{x} \mid Y = l, \boldsymbol{\theta})\,\mathbb{P}(Y = l \mid \boldsymbol{\theta})}{\mathbb{P}(Y = l \mid \boldsymbol{x}, \boldsymbol{\theta}^{(t)})\,f(\boldsymbol{x} \mid \boldsymbol{\theta}^{(t)})}
$$
(written for $n = 1$; for $n > 1$ sum over $i$ outside the logarithms), with equality at $\boldsymbol{\theta} = \boldsymbol{\theta}^{(t)}$. Moreover $\tilde B(\boldsymbol{\theta}, \boldsymbol{\theta}^{(t)}) - B(\boldsymbol{\theta}; \boldsymbol{\theta}^{(t)})$ does not depend on $\boldsymbol{\theta}$, so the M-step maximizes $\tilde B$, and consequently $\ell(\boldsymbol{\theta}^{(t+1)}) \ge \ell(\boldsymbol{\theta}^{(t)})$.

**Proof** Write $q_l = \mathbb{P}(Y = l \mid \boldsymbol{x}, \boldsymbol{\theta}^{(t)})$, a probability distribution over $l$. Then

$$
\begin{aligned}
\ell(\boldsymbol{\theta}) - \ell(\boldsymbol{\theta}^{(t)}) &= \ln\left(\sum_{l=1}^k q_l\,\frac{f(\boldsymbol{x} \mid Y = l, \boldsymbol{\theta})\,\mathbb{P}(Y = l \mid \boldsymbol{\theta})}{q_l}\right) - \ln f(\boldsymbol{x} \mid \boldsymbol{\theta}^{(t)}) \\
&\ge \sum_{l=1}^k q_l\ln\frac{f(\boldsymbol{x} \mid Y = l, \boldsymbol{\theta})\,\mathbb{P}(Y = l \mid \boldsymbol{\theta})}{q_l} - \ln f(\boldsymbol{x} \mid \boldsymbol{\theta}^{(t)}) = \tilde B(\boldsymbol{\theta}, \boldsymbol{\theta}^{(t)}) - \ell(\boldsymbol{\theta}^{(t)}),
\end{aligned}
$$
by **Jensen's inequality** for the concave logarithm, using $\sum_l q_l = 1$ to move $\ln f(\boldsymbol{x}\mid\boldsymbol{\theta}^{(t)})$ inside the sum. At $\boldsymbol{\theta} = \boldsymbol{\theta}^{(t)}$ the ratio inside the logarithm equals $1$ for every $l$ by Bayes' theorem, so $\tilde B(\boldsymbol{\theta}^{(t)}, \boldsymbol{\theta}^{(t)}) = \ell(\boldsymbol{\theta}^{(t)})$. The $\boldsymbol{\theta}$-dependent part of $\tilde B$ is $\sum_l q_l\ln\bigl(f(\boldsymbol{x}\mid Y=l,\boldsymbol{\theta})\,\mathbb{P}(Y=l\mid\boldsymbol{\theta})\bigr) = B(\boldsymbol{\theta}; \boldsymbol{\theta}^{(t)})$. Hence $\ell(\boldsymbol{\theta}^{(t+1)}) \ge \tilde B(\boldsymbol{\theta}^{(t+1)}, \boldsymbol{\theta}^{(t)}) \ge \tilde B(\boldsymbol{\theta}^{(t)}, \boldsymbol{\theta}^{(t)}) = \ell(\boldsymbol{\theta}^{(t)})$. $\square$

The EM algorithm is a special case of the minorization–maximization (MM) principle: maximize a simple lower bound that touches the objective at the current point. It is widely used throughout statistics, and it is particularly useful when some hidden data would make the problem easy. By Theorem 11.4.1 the likelihood never decreases, so it converges for a bounded likelihood, but only to a local maximum (or a stationary point); in practice it is started from several initial values or from a good initial clustering.

### 11.4.5. Model Selection and Implementation

Model-based clustering is implemented in R by the function `Mclust` of the package mclust (Scrucca et al., 2016): the initialization uses hierarchical clustering, the optimization uses the EM algorithm, and the number of clusters is chosen by BIC. Because the clustering is now a statistical model, choosing the number of clusters (and the form of the covariance matrices) is a model-selection problem, and any model-selection criterion, such as AIC, BIC or a likelihood ratio, can be used.

**Definition 11.4.2 (Information Criteria)** Let $L$ be the maximized likelihood of a model with $m$ free parameters fitted to $n$ observations. The **Bayesian information criterion** and the **Akaike information criterion** are

$$
\mathrm{BIC} = -2\ln L + m\ln n, \qquad \mathrm{AIC} = -2\ln L + 2m.
$$
Among candidate models, the one with the smaller criterion is preferred.

Both criteria penalize the fit $-2\ln L$ by the number of parameters; BIC penalizes more heavily when $\ln n > 2$ and therefore chooses smaller models. Note that some textbooks and mclust use the reversed sign, $2\ln L - m\ln n$, so that the higher the BIC, the better.

**Remark 11.4.1 (Why AIC Targets Prediction)** Let the data $\boldsymbol{y}$ come from $f(\cdot \mid \theta_0)$ and let $\hat\theta$ be the maximum likelihood estimate from $\boldsymbol{y}$. AIC aims at how well the fitted model $f(\cdot \mid \hat\theta)$ predicts new data $\boldsymbol{y}^{\mathrm{new}}$ from the same distribution, that is, at the expected value of $\ln f(\boldsymbol{y}^{\mathrm{new}} \mid \hat\theta)$. Intuitively, on new data the true model predicts better than the fitted one, $\ln f(\boldsymbol{y}^{\mathrm{new}}\mid\hat\theta) < \ln f(\boldsymbol{y}^{\mathrm{new}}\mid\theta_0)$; on average the true model fits $\boldsymbol{y}^{\mathrm{new}}$ and $\boldsymbol{y}$ equally well; and on the data used for fitting, the fitted model beats the true one, $\ln f(\boldsymbol{y}\mid\theta_0) < \ln f(\boldsymbol{y}\mid\hat\theta)$, which is overfitting. Hence the observable $\ln f(\boldsymbol{y}\mid\hat\theta) = \ln L$ overstates the predictive quality $\ln f(\boldsymbol{y}^{\mathrm{new}}\mid\hat\theta)$, and the correction $\mathbb{E}[\ln f(\boldsymbol{y}\mid\hat\theta) - \ln f(\boldsymbol{y}^{\mathrm{new}}\mid\hat\theta)]$ is asymptotically $m$, the number of parameters, which gives AIC after multiplying by $-2$. BIC instead approximates $-2$ times the log **marginal likelihood**, the quantity used for Bayesian model comparison ([3.2.7](/3.2.7)).

The covariance matrices of the components can be restricted to reduce the number of parameters. Write the **spectral decomposition** of each covariance matrix as $\Sigma_l = \lambda_l D_l A_l D_l^{\mathsf T}$, where $\lambda_l$ (a scalar) determines the volume of the $l$-th cluster, the diagonal matrix $A_l$ with $\det A_l = 1$ its shape, and the orthogonal matrix $D_l$ its orientation. mclust labels each parameterization with three letters for volume, shape and orientation, each E (equal across clusters), V (variable) or I (identity: spherical shape, or orientation along the coordinate axes). For example:

- EEE: the $k$ clusters have the same volume, shape and orientation (a common $\Sigma$, as in LDA);
- VEI: variable volume, the same shape, orientation along the coordinate axes;
- VVV: volume, shape and orientation all vary (unrestricted $\Sigma_l$, as in QDA).

For spherical shapes the orientation is irrelevant, so the spherical models are EII and VII. The package compares these models over a range of $k$ by BIC.

**Example 11.4.1** For the iris data, `Mclust(iris[, -5], 3)` fits three-component mixtures and selects by BIC the model VEV (variable volume, the same shape, variable orientation). Its three clusters agree with the species much better than those of $k$-means: the elongated, tilted clusters of versicolor and virginica are captured by their separate covariance matrices. As with $k$-means, the result can depend on the initial values.

![Simulated data with three clusters, two of them elongated bands. Left: k-means, which favors compact spherical clusters, cuts across the bands. Middle: a Gaussian mixture with unrestricted covariance matrices fitted by EM recovers the three groups; ellipses show the fitted components. Right: BIC of Gaussian mixtures (lower is better) against the number of components, minimized at k = 3.](./plots/kmeans-vs-gmm.py)

Gaussian mixtures and the EM algorithm have many successful applications, for example statistical modeling of the loads in electric distribution systems and adaptive background subtraction in video. In theory, finite Gaussian mixtures are dense in the set of all densities in the $L^1$ metric (Li and Barron, 1999), so with enough components they can approximate any distribution. Extensions include Bayesian and infinite Gaussian mixtures (Rasmussen, 1999), split-and-merge EM (Ueda et al., 2000), competitive EM (Zhang et al., 2004), and finite mixtures of other distributions (McLachlan et al., 2019).

## 11.5. Discussion

A cluster analysis involves a sequence of choices.

1. Preprocessing: transform the data (normalization, logarithms, principal components, and so on) and check for outliers. Clustering depends on the scale of the variables, unlike LDA ([3.4.10](/3.4.10#sec-10.7.1)), so **standardization** is often needed.
2. The distance between points, according to the type of data: Euclidean or correlation-based for numeric data; Jaccard, Hamming or edit distance for text and categorical data.
3. In hierarchical clustering, the distance between clusters. Each has its own strengths and limitations: single linkage can handle non-elliptical shapes but is sensitive to noise and outliers; complete linkage is more robust to noise and outliers but tends to break large clusters.
4. In $k$-means, the initial centroids. Random choice can be problematic: if there are $10$ real clusters of equal size and we pick $10$ points at random, the chance of picking one centroid from each cluster is only $10!/10^{10} \approx 0.00036$.

Why evaluate the results? To compare clustering algorithms, two sets of clusters or two clusters, and to choose the number of clusters. There are three types of numerical measures.

- External indices (supervised) compare a clustering with prior or expert-specified knowledge, such as known labels, using entropy-based, pair-counting or correlation indices.
- Internal indices (unsupervised) evaluate the goodness of a clustering without external information, for example the SSE, the pseudo-$F$ statistic or the pseudo-$T^2$ statistic.
- Relative indices compare different clusterings directly, usually those obtained from the same algorithm with different parameter settings; an external or internal index, such as the SSE or the entropy, often serves this purpose.

## Summary {#summary}

| | Hierarchical (agglomerative) | $k$-means | Model-based (GMM) |
|---|---|---|---|
| Type | hard | hard | soft |
| Settings | distance between points and between clusters | $k$, initial centroids, distance between points | $k$; $Y \sim \mathrm{Mult}(1, \boldsymbol{\pi})$, $\boldsymbol{X}\mid Y = l \sim \mathcal{N}_p(\boldsymbol{\mu}_l, \Sigma_l)$ |
| Method | repeatedly merge the closest clusters; dendrogram | minimize $J(c, \boldsymbol{\mu})$ by alternating assignment and update | maximize $\ell(\boldsymbol{\pi}, \boldsymbol{\mu}, \Sigma)$ by EM, alternating $\gamma$ and $(\boldsymbol{\pi}, \boldsymbol{\mu}, \Sigma)$ |
| Convergence | deterministic, $n-1$ merges | local minimum of $J$ | local maximum of $\ell$; likelihood never decreases |
| Advantages | no need to specify $k$; displays relations | fast, $O(tkn)$ | formal model; any covariance structure; $k$ chosen by BIC |
| Disadvantages | $O(n^2)$ memory, slow; merges cannot be undone | sensitive to outliers and initial values; spherical clusters; $k$ needed | more parameters; local maxima; relies on the model |

Cluster analysis groups objects by their similarity and is useful both for understanding and for summarizing data; the choice of distance, method and number of clusters, and the evaluation of the result, remain the practical issues in every application.
