---
title: "Exploring High-Dimensional Data: Distances, Clustering and Principal Components"
description: The shape of modern biomedical data (omics matrices, imaging, EEG, single cells, wearables) and the p ≫ n phenomenon; transformation and normalization of count data; distances and similarities (Euclidean, Manhattan, Canberra, correlation, Mahalanobis, Jaccard); hierarchical clustering, the Lance–Williams formula, cophenetic correlation and heatmaps; k-means and the choice of the number of clusters; principal component analysis, scree plots and biplots; batch effects and confounding; uses and misreadings of t-SNE and UMAP. Illustrated by the airway RNA-seq data.
source_hash: 49d25bbf11d5
---

The data in the earlier chapters had "few variables and many individuals": 5 variables on 654 children, 10 variables on 189 newborns. Omics data turn this shape upside down: the airway experiment has only 8 samples, but each sample has read counts for about 60,000 genes (the "individuals × variables" data matrix of [7.7.1](/7.7.1)). When the variables far outnumber the individuals ($p \gg n$), the first step is not testing but looking: which samples resemble which? Does the main variation in the data come from treatment, donor or sequencing batch? Is any sample mislabeled? This chapter presents the use and pitfalls, in biomedical data, of three kinds of tools that answer these questions: distances, clustering and principal components. Their mathematics has been given in multivariate statistics: **principal component analysis** ([3.4.5](/3.4.5)), **multidimensional scaling** ([3.4.6](/3.4.6)), **hierarchical clustering** and **k-means clustering** ([3.4.11](/3.4.11)); here we only state results where they are used and link to them. The airway data of thread 5 run through the chapter: this chapter looks at the structure of the samples, [7.7.20](/7.7.20) tests differential expression gene by gene on the same data, and [7.7.21](/7.7.21) explains why 8 samples cannot build a prediction model; the complete workflow of the experiment and analysis is in [7.9.2](/7.9.2).

## 19.1. The Shape of Modern Biological Data

### 19.1.1. Some Kinds of Data

| Data | One observation unit | Typical dimensions | Statistical features | See |
|---|---|---|---|---|
| Bulk transcriptome (RNA-seq) | Sample × gene counts | $n$ from a few to a few hundred, $p \approx 2\times10^4$–$6\times10^4$ | Counts, mean–variance dependence, overdispersion | This chapter, [7.7.20](/7.7.20), [7.9.2](/7.9.2) |
| Single-cell transcriptome | Cell × gene | $10^4$–$10^6$ cells, only a few thousand genes detected per cell | Extremely sparse, most counts are 0 | [7.7.20](/7.7.20) Section 20.8, [7.9.5](/7.9.5) |
| Genotype (GWAS) | Individual × SNP | $n$ up to $10^5$–$10^6$, $p \approx 10^6$–$10^7$ | Discrete values 0/1/2, adjacent loci linked | [7.4.25](/7.4.25), [7.8.13](/7.8.13) |
| Protein structure | Three-dimensional coordinates of atoms | Thousands of atoms per chain | Overall translation and rotation do not change the meaning; hierarchy atom → residue → chain | [7.8.17](/7.8.17) |
| Magnetic resonance imaging | Voxel × signal intensity | About $10^6$ voxels in one brain scan | Adjacent voxels highly correlated (not independent); registration needed across individuals | [7.6.13](/7.6.13) |
| EEG | Channel × time | A few dozen channels, hundreds of samples per second | Low signal-to-noise ratio, temporally correlated, nonstationary | [7.16](/7.16) |
| Wearable devices | Person × time series (heart rate, steps, sleep) | Tens of thousands of readings per person per day | High frequency, missingness not at random (periods when the device is not worn), within-subject correlation | [7.7.17](/7.7.17) |

What they have in common is that each individual yields far more numbers than there are individuals, and these numbers have structure (genes co-regulated, voxels spatially adjacent, time points correlated with the neighbors). The two premises of classical methods, fewer variables than individuals and independent observations, both fail.

### 19.1.2. Two Phenomena of High-Dimensional Space

The **curse of dimensionality** ([4.6.4](/4.6.4)) shows up in exploratory analysis as two concrete phenomena (figure below).

First, distances tend to become equal. For random points that are independent and identically distributed in $p$ dimensions, the ratio of the farthest to the nearest distance to a given point tends to 1 as $p$ increases: for $p = 1$ the farthest distance is about 100 times the nearest, and for $p = 10^4$ they differ by only about 3%. If all dimensions are independent noise, a "nearest neighbor" is meaningless. Omics data can still be clustered because their variation is concentrated in a few directions (a few biological programs change hundreds or thousands of genes at once); restricting the analysis to highly variable genes or to the first few principal components is precisely meant to remove the dimensions that contribute only noise.

Second, the sample covariance matrix is singular. The rank of the sample covariance matrix of $n$ observations is at most $n - 1$; when $p > n$ it is not invertible, and the **Mahalanobis distance** ([3.4.1](/3.4.1)), Hotelling's $T^2$ and linear discriminant analysis cannot be computed directly. Even when all variables are independent and the true eigenvalues are all 1, the sample eigenvalues spread out: for $n = 20$ and $p = 50$ the largest sample eigenvalue is 6.3, while 31 are 0. The first few sample principal components therefore always "explain" a considerable proportion of the variance even if the data have no structure whatsoever; a scree plot must be read against what is expected for structureless data (Section 19.6.3).

![Two properties of high-dimensional data (simulation, seed 0). A: concentration of distances: 100 points from a $p$-dimensional standard normal or uniform distribution, the difference between the farthest and the nearest distance to a query point divided by the nearest distance (median of 20 replications) tends to 0 as the dimension increases. B: eigenvalues of the sample covariance matrix of $n = 20$ observations of $p = 50$ independent standard normal variables: the population eigenvalues are all 1 (dashed line), the sample eigenvalues spread from 6.3 down to 0, with 31 exactly 0 (rank at most $n - 1 = 19$)](./plots/high-dim.py)

## 19.2. Preprocessing: Transformation and Normalization

### 19.2.1. Why Counts Are Transformed

RNA-seq counts range from 0 to hundreds of thousands, and the variance increases with the mean (Poisson part $\mu$, biological part $\alpha\mu^2$, [7.7.20](/7.7.20) Section 20.5). Distances or principal components computed on raw counts are determined by the few genes with the highest expression; after taking logarithms they are dominated instead by the many genes with small counts and large relative fluctuation. Three commonly used scales:

- Normalized counts $K_{ij}/s_j$ ($s_j$ the size factor, [7.7.20](/7.7.20) Section 20.6): corrects only for sequencing depth and does not change the mean–variance relation.
- $\log_2(K_{ij}/s_j + 1)$: the pseudocount of 1 avoids taking the logarithm of 0, but when counts are small the $+1$ is of the same order as the Poisson noise itself, and the variance of low-expression genes is inflated.
- The **variance-stabilizing transformation** ([3.3.6](/3.3.6)): choose a transformation $g$ such that $\operatorname{Var}[g(K)]$ is approximately independent of the mean. For negative binomial counts with $\operatorname{Var}(K) = \mu + \alpha\mu^2$, the delta method gives $g(\mu) = \int \mathrm{d}\mu/\sqrt{\mu + \alpha\mu^2}$, which approximates $\log_2$ for large $\mu$ and compresses differences for small $\mu$. The `vst` of DESeq2 and pydeseq2 computes it using the fitted dispersion trend; the "regularized log" (rlog) has the same purpose.

**Example 19.2.1 (The Scale Changes the Structure of airway)** On each scale we select the 500 genes with the largest variance and perform principal component analysis (figure below). The median of the mean counts of the genes selected on the normalized-count scale is 9776, and the first principal component (42%) is determined mainly by a few very highly expressed genes such as *FN1* and *DCN*; the genes selected on the $\log_2(x + 1)$ scale have a median mean count of only 25, and the first principal component (31%) separates the two samples of donor N080611 from the others, with treatment receding to second place; the genes selected after variance stabilization have a median count of 242, and the first principal component (39%) is the dexamethasone treatment. The same data on three scales give different "main structures of the data"; for count data, the variance-stabilized scale is the closest to the requirement that "every gene be equally trustworthy".

![The effect of scale on principal component analysis (airway RNA-seq: 4 airway smooth muscle cell lines × dexamethasone treatment or not; Himes et al. 2014, GEO GSE52778, Bioconductor airway). On each scale the 500 genes with the largest variance are taken and centered by gene. A: normalized counts; B: $\log_2$(normalized counts + 1); C: variance-stabilizing transformation (pydeseq2 vst). Color is treatment and shape is cell line. D: mean normalized counts of the 500 genes selected on each scale (log axis): the raw scale selects only genes with very high expression, and $\log_2(x+1)$ selects many noisy genes with low expression](./plots/transform-pca.py)

### 19.2.2. Centering and Standardizing by Variable

Principal component analysis always centers by variable (gene). Whether to divide further by the standard deviation (that is, to analyze the correlation matrix instead of the covariance matrix, [Theorem 5.2.4](/3.4.5#thm-5.2.4)) depends on whether the scales of the variables are comparable:

- Variables with different units (age, blood pressure, cholesterol): standardization is necessary, otherwise the variables with large units dominate.
- Gene expression on the same scale: usually not standardized, since genes with large variation should rightly have a large weight; standardization would give low-variance genes that contain only noise the same importance as genes related to treatment. Screening genes by variance before standardizing is a compromise: after standardizing the top 500 genes of airway, the first two principal components explain 41% and 27% of the variance, with essentially the same structure as without standardization.

The **z-scores** ([7.7.2](/7.7.2)) computed by gene in a heatmap (Section 19.4.3) are only for display and do not change the distance used in clustering.

## 19.3. Distances and Similarities

### 19.3.1. The Distance Matrix

The input of clustering and multidimensional scaling is not the data themselves but the pairwise dissimilarities between individuals.

**Definition 19.3.1 (Distance Matrix)** Let $d$ be a dissimilarity between individuals: $d(x, y) \ge 0$, $d(x, x) = 0$, $d(x, y) = d(y, x)$. The $n \times n$ matrix $D = (d_{ij})$ of $n$ individuals, with $d_{ij} = d(x_i, x_j)$, is called the **distance matrix**. If $d$ also satisfies the triangle inequality, it is a metric.

There are only $n(n-1)/2$ distinct distances among $n$ individuals; the 8 airway samples give 28 numbers, computed from vectors of dimension 500. The distance matrix turns a $p$-dimensional problem into an $n$-dimensional one, which is the natural starting point for exploring samples when $p \gg n$.

### 19.3.2. Commonly Used Distances

Let $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^p$ be the observation vectors of two individuals.

| Distance | Formula | Features and use |
|---|---|---|
| **Euclidean distance** ([4.6.4](/4.6.4)) | $\bigl(\sum_k (x_k - y_k)^2\bigr)^{1/2}$ | Most commonly used; affected by scale and outliers |
| **Manhattan distance** (city-block distance, absolute-value distance) | $\sum_k \lvert x_k - y_k\rvert$ | Less sensitive to a single large difference than the Euclidean distance |
| **Chebyshev distance** | $\max_k \lvert x_k - y_k\rvert$ | Looks only at the variable with the largest difference |
| **Minkowski distance** | $\bigl(\sum_k \lvert x_k - y_k\rvert^q\bigr)^{1/q}$ | $q = 1, 2, \infty$ give the three above |
| Canberra distance | $\sum_k \dfrac{\lvert x_k - y_k\rvert}{\lvert x_k\rvert + \lvert y_k\rvert}$ | Each variable is scaled by its own size; suited to nonnegative data; sensitive to values near 0 |
| **Mahalanobis distance** ([3.4.1](/3.4.1)) | $\bigl((\boldsymbol{x} - \boldsymbol{y})^{\mathsf T} S^{-1}(\boldsymbol{x} - \boldsymbol{y})\bigr)^{1/2}$ | Removes the effects of scale and of correlation between variables; needs an invertible covariance matrix $S$, not usable when $p \ge n$ |
| Cosine distance | $1 - \dfrac{\boldsymbol{x}^{\mathsf T}\boldsymbol{y}}{\lVert\boldsymbol{x}\rVert\,\lVert\boldsymbol{y}\rVert}$ | Obtained from the **cosine similarity** ([Definition 11.2.1](/3.4.11#def-11.2.1)); looks only at direction, not length |
| Correlation distance | $1 - r(\boldsymbol{x}, \boldsymbol{y})$ | See Definition 19.3.2 |
| **Jaccard distance** | $1 - \lvert A \cap B\rvert/\lvert A \cup B\rvert$ | Binary data (presence of a mutation, a species, a gene detected) |

The relation of the first three to the Minkowski distance means that "absolute-value distance" and "city-block distance" need not be separate: both are the Minkowski distance with $q = 1$, the Manhattan distance.

**Definition 19.3.2 (Correlation Distance)** When the sample Pearson **correlation coefficient** of two observation vectors is $r(\boldsymbol{x}, \boldsymbol{y})$, $d = 1 - r$ is called their **correlation distance**.

The correlation distance compares "shape": two genes that rise and fall together in the 8 samples have a correlation distance close to 0 even if the expression of one is 100 times that of the other. It is therefore a common choice for clustering genes (finding co-expressed gene modules), while for clustering samples the Euclidean distance is more often used. The relation between the two is:

**Property 19.3.1** Center $\boldsymbol{x}, \boldsymbol{y}$ over their own $p$ components and divide by the sample standard deviation to obtain $\tilde{\boldsymbol{x}}, \tilde{\boldsymbol{y}}$; then

$$
\lVert\tilde{\boldsymbol{x}} - \tilde{\boldsymbol{y}}\rVert^2 = 2(p - 1)\bigl[1 - r(\boldsymbol{x}, \boldsymbol{y})\bigr].
$$

**Proof** $\lVert\tilde{\boldsymbol{x}}\rVert^2 = \lVert\tilde{\boldsymbol{y}}\rVert^2 = p - 1$ and $\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{y}} = (p - 1)r$; expand $\lVert\tilde{\boldsymbol{x}} - \tilde{\boldsymbol{y}}\rVert^2 = \lVert\tilde{\boldsymbol{x}}\rVert^2 + \lVert\tilde{\boldsymbol{y}}\rVert^2 - 2\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{y}}$. $\square$

So the correlation distance is "standardize each individual first, then compute the Euclidean distance", and the two give the same ordering. The correlation distance does not satisfy the triangle inequality, but $\sqrt{2(1 - r)}$ does.

**Example 19.3.1 (Sample Distances in airway)** On the 500 genes with the largest variation after variance stabilization, the pairwise Euclidean distances among the 8 samples range from 29.0 to 52.5 (panel A of the figure below). The closest pair is the untreated samples of two donors (N61311 and N052611, 29.0), followed by the treated samples of two donors (N052611 and N061011, 30.8); the distance between before and after treatment of the same donor is 32.5–36.8; the farthest is the untreated sample of one donor and the treated sample of another (for example N080611 untreated and N061011 treated, 52.5). Both treatment and donor are at work, with treatment slightly stronger. The correlation coefficients between samples are between 0.585 and 0.870, and the correlation distances 0.13–0.42, giving the same order of near and far as the Euclidean distance.

### 19.3.3. Choosing a Distance

The choice of distance matters more than the choice of clustering method, since it determines what "similar" means:

- First ask whether similarity means similar level (Euclidean), the same pattern (correlation) or sharing the same set of features (Jaccard).
- When variables have different units, standardize first, or use the Canberra or Mahalanobis distance; when variables are highly correlated, the Euclidean distance counts the same information repeatedly (10 correlated genes amount to counting the difference of one gene 10 times), which the Mahalanobis distance or a preliminary principal component analysis can avoid.
- Whether "joint absence" counts as similarity for binary variables depends on the problem: two people both lacking a rare mutation does not show they are similar, so use the Jaccard rather than the simple matching coefficient.
- Between microbial communities the Bray–Curtis dissimilarity and the UniFrac distance are commonly used ([7.8.14](/7.8.14)).

## 19.4. Hierarchical Clustering

### 19.4.1. Agglomerative Algorithms and Linkages

**Hierarchical clustering** ([Algorithm 11.2.1](/3.4.11#alg-11.2.1)) starts with each individual as its own cluster and merges the two closest clusters at each step until only one remains; the history of merges is drawn as a **dendrogram**, and cutting horizontally at some height gives a number of clusters. The distance between clusters is specified by the linkage ([Definition 11.2.2](/3.4.11#def-11.2.2)): **single linkage** takes the closest pair of points in the two clusters, **complete linkage** the farthest pair, **average linkage** the average over all pairs, **centroid linkage** the distance between the centroids, and **Ward's method** the increase of the within-cluster sum of squares caused by the merge. These rules can be unified in one recurrence, so that only the distance matrix is needed and one need not return to the raw data.

**Formula 19.4.1 (Lance–Williams Formula)** Let clusters $i$ and $j$ be merged into $k = i \cup j$, and let $n_i, n_j, n_h$ be the sizes of the clusters. The distance between the new cluster and any other cluster $h$ is

$$
d_{hk} = \alpha_i d_{hi} + \alpha_j d_{hj} + \beta d_{ij} + \gamma\lvert d_{hi} - d_{hj}\rvert,
$$
where

| Method | $\alpha_i$ | $\beta$ | $\gamma$ |
|---|---|---|---|
| Single linkage | $1/2$ | 0 | $-1/2$ |
| Complete linkage | $1/2$ | 0 | $1/2$ |
| Average linkage | $n_i/(n_i + n_j)$ | 0 | 0 |
| Centroid linkage ($d$ the squared Euclidean distance) | $n_i/(n_i + n_j)$ | $-n_in_j/(n_i + n_j)^2$ | 0 |
| Ward's method ($d$ the squared Euclidean distance) | $(n_i + n_h)/(n_i + n_j + n_h)$ | $-n_h/(n_i + n_j + n_h)$ | 0 |

($\alpha_j$ is obtained by replacing $i$ with $j$.) The rows for single and complete linkage can be verified directly: $\tfrac12(d_{hi} + d_{hj}) \mp \tfrac12\lvert d_{hi} - d_{hj}\rvert$ are the $\min$ and the $\max$ respectively. The median method, the flexible-beta method and McQuitty's method are also special cases of this formula, with different coefficients.

A naive implementation scans the whole distance matrix at every step, with total time $O(n^3)$; a priority queue lowers it to $O(n^2\log n)$, and single linkage (equivalent to finding a minimum spanning tree) and Ward's method have $O(n^2)$ algorithms. In any case, storing the distance matrix needs $O(n^2)$ memory: the distance matrix of 100,000 single cells has $5\times10^9$ numbers, so hierarchical clustering is infeasible at this scale, and single-cell analysis uses community detection on a nearest-neighbor graph instead ([7.9.5](/7.9.5)).

### 19.4.2. The Effect of the Linkage

Different linkages can give entirely different classifications of the same data (figure below). Single linkage joins two clusters as soon as there is a chain of closely spaced points (the "chaining effect"), which suits finding elongated or irregularly shaped clusters but often yields one large cluster plus a few isolated points; complete linkage favors compact clusters of similar diameter; Ward's method favors spherical clusters of similar size and variance; average linkage lies in between. There is no right or wrong among them, only whether they fit the way the data were generated: in the simulation below, Ward's method comes closest to the three groups that generated the data. In practice several linkages are often examined together, and only structures on which they agree are credible.

![Clustering of the same set of points by four linkages (simulation, seed 0): a compact group of 40 points, an elongated group of 60 points and a sparse group of 25 points, with a thin bridge of 8 points between the first two groups; Euclidean distance, the tree cut into three clusters, the cluster sizes in the titles. A: single linkage chains along the thin bridge into one large cluster of 108 points and separates only one isolated point of the sparse group. B, C: complete and average linkage merge the end of the elongated group near the bridge (10 points) into the compact group. D: Ward's method recovers the three groups that generated the data, with points on the bridge assigned to the two sides. The bottom row shows the dendrograms, with dashed lines at the cutting heights (the vertical scales differ between panels)](./plots/linkage-compare.py)

### 19.4.3. Dendrograms and Heatmaps

**Definition 19.4.1 (Cophenetic Correlation Coefficient)** In a dendrogram, the height at which two individuals are first merged into the same cluster is called their cophenetic distance. The Pearson correlation coefficient between the cophenetic distances of all pairs of individuals and the corresponding distances in the original distance matrix is called the **cophenetic correlation coefficient**.

It measures how well the dendrogram preserves the original distances: the closer to 1, the more faithful the tree. The order of the leaves of a dendrogram has a great deal of freedom (the two branches of each internal node can be swapped, so $n$ leaves can be drawn in $2^{n-1}$ ways), and two leaves adjacent horizontally are not necessarily similar; only the heights of the merges are meaningful.

**Definition 19.4.2 (Heatmap)** A plot in which each element of a data matrix (or distance matrix) is drawn as a colored cell, with the color intensity representing the value, and in which the rows and columns are usually reordered by the result of hierarchical clustering and accompanied by dendrograms on the sides, is called a **heatmap**.

The heatmap is the most common figure in omics papers. Three things to watch when reading a heatmap: what the color represents (raw values, values centered by gene or z-scores); whether the color scale is symmetric and whether it is truncated (when truncated at $\pm2$, all cells with $\lvert z\rvert > 2$ have the same color); and that the order of rows and columns comes from clustering, which in turn depends on the distance and the linkage.

**Example 19.4.1 (Hierarchical Clustering of airway)** For the distance matrix of Example 19.3.1, all linkages agree on the first few merges: first the untreated samples of two donors (height 29.0) and then the treated samples of two donors (30.8). But they disagree when cut into two clusters (panel A below): average linkage and Ward's method split into {the treated samples of N61311, N052611 and N061011} and the other 5 samples, that is, broadly by treatment, with only the treated sample of donor N080611 falling on the untreated side; single and complete linkage first split off the two samples of donor N080611. The cophenetic correlation coefficients of the four trees are 0.63–0.66: the structure of 8 samples cannot be fully expressed by one tree, since treatment and donor are two crossed factors and a tree can represent only nesting. Panel B below is a heatmap of the 40 genes with the greatest variation: Y-chromosome genes (*RPS4Y1*, *DDX3Y*, *USP9Y*, *KDM5D* and others) and *XIST* form two modules, showing that donor N061011 is female and the other three are male; *ZBTB16*, *KLF15*, *FKBP5*, *SPARCL1* and others are raised in treated samples, and they are classical glucocorticoid target genes ([7.9.2](/7.9.2) Section 2.7.2).

![Sample distances and clustering of the airway experiment (Himes et al. 2014, GEO GSE52778, Bioconductor airway; the 500 genes with the largest variation after pydeseq2 vst). A: pairwise Euclidean distances among the 8 samples, arranged in the leaf order of average-linkage hierarchical clustering, with the dendrogram above. B: heatmap of the 40 genes with the largest variation standardized by gene (z-scores, color scale truncated at ±2), genes clustered by average linkage on the correlation distance, sample order as in A. dex: dexamethasone treated; ctrl: untreated](./plots/airway-heatmap.py)

## 19.5. k-Means and the Choice of the Number of Clusters

### 19.5.1. k-Means

**k-means clustering** ([Algorithm 11.3.1](/3.4.11#alg-11.3.1)) is given the number of clusters $k$ in advance and alternates between assigning each point to the nearest cluster center and updating the cluster centers to the within-cluster means, so that the within-cluster sum of squares

$$
W(k) = \sum_{c=1}^{k}\sum_{i \in C_c}\lVert\boldsymbol{x}_i - \bar{\boldsymbol{x}}_c\rVert^2
$$
decreases monotonically until convergence. The computation per iteration is $O(nkp)$, and it can handle hundreds of thousands of individuals, its main advantage over hierarchical clustering. It converges to a local optimum, and the result depends on the initial centers: in practice k-means++ initialization (drawing the next center with probability proportional to the squared distance to the centers already chosen) is used, and the result with the smallest $W(k)$ among several dozen random starts is taken. It implicitly assumes clusters that are spherical and of similar size, the same objective as Ward's method; k-means is the limit, as the variance tends to 0, of a **Gaussian mixture model** ([Definition 11.4.1](/3.4.11#def-11.4.1)) with spherical clusters of equal variance, and the latter gives the probability that each point belongs to each cluster and can use an information criterion to choose the number of clusters.

### 19.5.2. The Number of Clusters

The question of "how many clusters are there" in data often has no unique answer (cell types can be divided at different granularities), but there are several commonly used guides:

- The elbow method: plot $W(k)$ against $k$ and look for an elbow where the decrease clearly slows down. $W(k)$ always decreases with $k$, and the elbow is often unclear.
- The **silhouette coefficient** ([Definition 11.3.1](/3.4.11#def-11.3.1)): compare the average distance $a(i)$ from each point to its own cluster with the average distance $b(i)$ to the nearest other cluster, $s(i) = [b(i) - a(i)]/\max\{a(i), b(i)\}$; the larger the average over all points, the clearer the classification. Above 0.5 the structure is usually considered clear, and below 0.25 weak or artificial.
- The Calinski–Harabasz index (the pseudo-$F$ statistic in SAS output): $\dfrac{B(k)/(k - 1)}{W(k)/(n - k)}$, with $B(k)$ the between-cluster sum of squares, an analogue of the $F$ of analysis of variance; larger is better.
- The **gap statistic**: compare $\log W(k)$ with its expectation simulated under a structureless reference distribution (a uniform distribution on the same range as the data) and take the $k$ with the largest gap; it can answer "$k = 1$, no clustering structure", which the earlier indices cannot.
- Stability: re-cluster after resampling individuals or adding noise to the variables; only clusters that appear stably are credible.

**Example 19.5.1** k-means on the 8 airway samples: for $k = 2$ the split is into 4 treated and 4 untreated samples, with mean silhouette coefficient 0.214; for $k = 3$ the two samples of donor N080611 are split off, with silhouette coefficient 0.211; for $k = 4$ it is 0.115. The silhouette coefficient of the grouping by treatment is 0.214, and by donor 0.099. All values are below 0.25: the structure of the 8 samples is "the superposition of two effects, treatment and donor", not mutually separated clusters. This points to a key message of the chapter: clustering looks for clusters, and if the variation in the data is continuous or consists of several crossed factors, principal component analysis describes it better than clustering.

## 19.6. Principal Component Analysis

### 19.6.1. The Method

**Principal component analysis** ([3.4.5](/3.4.5)) looks for the orthogonal directions that maximize the variance of the projection. For the $n \times p$ data matrix $X$ centered by variable, take the **singular value decomposition** ([3.4.6](/3.4.6) Section 6.1.3)

$$
X = UDV^{\mathsf T},
$$
where the $k$th column of $V$ gives the loadings (the coefficients of the variables) of the $k$th **principal component**, the $k$th column of $UD$ gives the principal component scores of the individuals, the variance of the $k$th principal component is $d_k^2/(n - 1)$, and its proportion of the total variance is $d_k^2/\sum_l d_l^2$. When $p \gg n$ the singular value decomposition is used instead of forming the $p \times p$ covariance matrix (for the 500 genes of airway it is $500 \times 500$, and for all genes of order $2\times10^4$); there are at most $n - 1$ nonzero principal components. The computation is $O(np\min(n, p))$, and for data on the scale of single cells a truncated or randomized singular value decomposition that finds only the first few components is used.

### 19.6.2. Scree Plots and Biplots

A **scree plot** ([3.4.5](/3.4.5) Section 5.4.1) plots the proportion of variance explained by each principal component in order. Commonly used rules for how many principal components to keep: a cumulative proportion of 70%–90%; for the correlation matrix, keep components with eigenvalue greater than 1 (Kaiser's criterion, not applicable to the covariance matrix); the "elbow" of the scree plot; parallel analysis, comparing with the eigenvalues of structureless data (for example with each variable randomly permuted independently); and cross-validated comparison of reconstruction error. The phenomena of Section 19.1.2 show that the proportion itself cannot be taken at face value when $p \gg n$.

**Definition 19.6.1 (Biplot)** From the first two terms of the singular value decomposition, $X \approx \sum_{k=1}^{2} d_k\boldsymbol{u}_k\boldsymbol{v}_k^{\mathsf T}$, take $G = [\boldsymbol{u}_1, \boldsymbol{u}_2]\operatorname{diag}(d_1, d_2)^{c}$ and $H = [\boldsymbol{v}_1, \boldsymbol{v}_2]\operatorname{diag}(d_1, d_2)^{1-c}$ ($0 \le c \le 1$), and draw on the same plot the rows of $G$ as points (individuals) and the rows of $H$ as arrows (variables); this is called a **biplot**.

$GH^{\mathsf T}$ is the best rank-2 approximation of $X$ ([Theorem 5.6.1](/3.4.5#thm-5.6.1)), so the approximate value of individual $i$ on variable $j$ equals the inner product of point $i$ and arrow $j$: a point on the side to which an arrow points has a high value of that variable. For $c = 1$ the points are the principal component scores, and distances between individuals approximate the original Euclidean distances; for $c = 0$ the lengths of the arrows approximate the standard deviations of the variables and the cosines of the angles between arrows approximate the correlation coefficients between variables. When $p$ is large, only the arrows of the variables with the largest loadings are drawn.

### 19.6.3. Principal Components of airway

**Example 19.6.1** Principal component analysis of the 500 genes with the largest variation after variance stabilization in airway (figure below). The first four principal components explain 38.8%, 27.1%, 17.5% and 13.4% of the variance, a total of 96.9%, and the remaining three about 3% together: nearly all the variation of the 8 samples lies in a 4-dimensional space, consistent with the design: treatment has 1 degree of freedom and donor 3, exactly 4 together. The first principal component separates treated from untreated samples, and the two samples of the same donor move in almost the same direction and distance along the first principal component (arrows in panel B); the genes with the largest loadings are *ZBTB16*, *SPARCL1*, *GPX3*, *STEAP4*, *SAMHD1*, *FKBP5* and *KLF15*, which are exactly the most significantly differentially expressed genes in [7.9.2](/7.9.2) (the loading of *VCAM1* is negative, as it is suppressed by dexamethasone). The second principal component separates donors N080611 and N061011, with the largest loadings from *XIST* (negative) and *RPS4Y1*, *DDX3Y* and *USP9Y* (positive): the female donor N061011 has *XIST* counts of about 3000–3900 and almost 0 for the Y-chromosome genes, and the other three male donors are exactly the opposite. The third and fourth principal components distinguish the remaining donors.

This example illustrates both the use and the limits of principal component analysis. Use: one sees at a glance that the treatment effect is the largest, that the donor effect is almost equally large (the second to fourth principal components together 58%), and that there is no outlying sample; it also reminds us to treat the donor as a pairing factor in the analysis ([7.7.20](/7.7.20) Section 20.7; ignoring the pairing loses many detections, [7.9.2](/7.9.2) Section 2.7.2). Limits: principal components are statistical directions and do not necessarily correspond to a single biological factor; the second principal component is sex because the largest difference between donors happens to be sex. Testing "whether treatment changes a given gene" still requires gene-by-gene models ([7.7.20](/7.7.20)).

![Principal component analysis of the airway samples (Himes et al. 2014, GEO GSE52778, Bioconductor airway; the 500 genes with the largest variation after pydeseq2 vst, centered by gene). A: scree plot, the proportion of variance explained by each principal component and the cumulative proportion. B: scores on the first two principal components, color for treatment and shape for cell line (donor), with arrows from the untreated to the treated sample of the same donor. C: loading plot (the variable half of a biplot): gray dots are the loadings of the 500 genes, and arrows mark the 4 genes with the largest loadings on the first and on the second principal component](./plots/airway-pca.py)

The relation of principal component analysis to **multidimensional scaling**: classical multidimensional scaling of a Euclidean distance matrix gives coordinates identical to the principal component scores ([Algorithm 6.2.1](/3.4.6#alg-6.2.1) and [Theorem 6.2.1](/3.4.6#thm-6.2.1)). Multidimensional scaling on other distances (Bray–Curtis, UniFrac, correlation distance) is called **principal coordinates analysis** in ecology and is the standard plot for comparing microbial communities ([7.8.14](/7.8.14)).

## 19.7. Batch Effects and Confounding

A **batch effect** ([7.9.2](/7.9.2) Definition 2.2.2) is a systematic difference caused by technical factors other than treatment: the date of RNA extraction, reagent lot, sequencing lane, operator. In omics data it is often larger than the biological effect, and principal component analysis is the first-choice tool for discovering it: color the principal component scores by each known technical variable and see which one aligns with the first few principal components.

Whether a batch effect is harmful depends on the design (figure below). If both treated and control groups are present in every batch (a balanced design), treatment and batch are two factors that can be estimated separately: in principal component analysis they fall on different components, and in a statistical model, including batch as a factor (like the donor in airway) adjusts for it. If the treated group is entirely in one batch and the control group entirely in another, treatment is in complete **confounding** with batch: no analysis can tell the two apart, and panel B (with a treatment effect) and panel C (without a treatment effect) are almost the same on the principal component plot. No statistical remedy then exists, and batch correction (such as ComBat, [7.9.2](/7.9.2) Section 2.8) removes the treatment effect together with the batch. The only remedy is at the design stage: allocate the samples of each group to the batches by **randomization** and record every technical variable (a direct application in omics of the block design of [7.7.12](/7.7.12)).

![Looking at batch effects with principal component analysis (simulation, seed 0): 2000 genes on the log scale, 4 untreated and 4 treated samples, with a noise standard deviation of 0.4 per gene; treatment raises 200 genes by 1.0, and batch raises another 300 genes by 0.8. Circles are batch 1 and squares batch 2. A: balanced design (2 samples of each group in each batch): the first principal component is treatment and the second is batch, so the two are separable. B: complete confounding (all untreated in batch 1, all treated in batch 2): one principal component contains both effects. C: the same confounding but with no treatment effect at all: the principal component plot is almost the same as B, and the data themselves cannot distinguish a treatment effect from a batch effect](./plots/batch-pca.py)

In genetics the same problem appears as **population stratification**: when cases and controls differ in ancestry, every SNP whose frequency differs between the two populations will show an "association" with the disease. The first few principal components of the genotype matrix reflect ancestry, and adding them as covariates in association tests is standard practice in GWAS ([7.4.25](/7.4.25) Section 25.3.3); this is the same idea as putting batch or donor into the model.

## 19.8. A Glimpse of Nonlinear Dimension Reduction

Principal component analysis is linear: it can find only linear subspaces of the data. In single-cell data, cells lie along differentiation trajectories on curved low-dimensional manifolds, and the first two principal components can hardly display dozens of cell types. **t-distributed stochastic neighbor embedding** (t-SNE, see [3.4.6](/3.4.6) Section 6.4) and UMAP (uniform manifold approximation and projection) preserve the neighbor relations of high-dimensional space in two dimensions: t-SNE represents the degree to which "$j$ is a neighbor of $i$" by probabilities and makes these probabilities in two dimensions agree as far as possible with those in high dimensions; UMAP constructs a weighted $k$-nearest-neighbor graph in high dimensions and, in two dimensions, finds the layout that minimizes the cross-entropy of this graph. In practice both are run on the first 30–50 principal components, not on the original tens of thousands of genes.

Their plots are very intuitive but easily misread:

- They preserve only local neighbor relations: points within a cluster are close, but the distance between two clusters on the plot does not represent how different they are, and the size and density of a cluster do not represent how large the variation within it is.
- The result depends on parameters (perplexity for t-SNE; number of neighbors and minimum distance for UMAP) and on the random seed; the same data with different parameters can give plots that look different.
- Even uniform noise can be drawn as several seemingly separate clumps, and the "clusters" on the plot must be validated by clustering and marker genes.

Hence t-SNE and UMAP are used for display, not for computation: clustering is performed in principal component space or on the nearest-neighbor graph, and trajectories and distances are computed in the original space or in principal component space ([7.9.5](/7.9.5), [7.9.7](/7.9.7)).

## 19.9. Computing with Python

```python
import numpy as np
import pandas as pd
from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

vst = pd.read_csv("airway_vst.csv", index_col=0)            # genes x samples, variance-stabilized (pydeseq2: dds.vst())
meta = pd.read_csv("airway_coldata.csv", index_col=0)

top = vst.loc[vst.var(axis=1).sort_values(ascending=False).index[:500]]
X = top.T.values                                             # samples x genes

# distances and hierarchical clustering (Example 19.3.1, Example 19.4.1)
d = pdist(X, metric="euclidean")                             # also "cityblock", "chebyshev", "canberra", "correlation", "jaccard"
print(pd.DataFrame(squareform(d), index=top.columns, columns=top.columns).round(1))
for method in ["single", "complete", "average", "ward"]:
    Z = hierarchy.linkage(X, method)                         # ward and centroid need raw data (Euclidean)
    coph, _ = hierarchy.cophenet(Z, d)
    print(method, hierarchy.fcluster(Z, 2, "maxclust"), round(coph, 3))

# k-means and silhouettes (Example 19.5.1)
for k in (2, 3, 4):
    km = KMeans(n_clusters=k, n_init=50, random_state=0).fit(X)
    print(k, km.labels_, round(silhouette_score(X, km.labels_), 3))

# principal components (Example 19.6.1)
pca = PCA().fit(X)                                           # centers each gene; scale=False by default
print(pca.explained_variance_ratio_.round(3))                # 0.388 0.271 0.175 0.134 ...
scores = pca.transform(X)[:, :2]
loadings = pd.Series(pca.components_[0], index=top.index)
print(loadings.abs().sort_values(ascending=False).head(10))
```

## Summary

- Omics, imaging, EEG and wearable data all have $p \gg n$ and structure among the variables; in high dimensions distances tend to equalize, the sample covariance matrix is singular (rank $\le n - 1$), and the first few sample principal components "explain" a large amount of variance even in structureless data (Section 19.1).
- Count data first undergo a variance-stabilizing transformation: raw counts are dominated by extremely highly expressed genes and $\log_2(x + 1)$ by the noise of low-expression genes; the main structure of airway changes with the scale (Example 19.2.1). Variables with different units are standardized, while gene expression on the same scale is generally not.
- The distance matrix (Definition 19.3.1) is the input of clustering and multidimensional scaling. Euclidean, Manhattan and Chebyshev are special cases of the Minkowski distance; the correlation distance (Definition 19.3.2) is "standardize each individual, then compute the Euclidean distance" (Property 19.3.1); the Mahalanobis distance is unusable when $p \ge n$; use Jaccard for binary data.
- Hierarchical clustering: the linkages are unified in the Lance–Williams formula (Formula 19.4.1); single linkage chains, complete linkage is compact, Ward's method is balanced; $O(n^2)$ memory limits the scale. The cophenetic correlation coefficient (Definition 19.4.1) measures the faithfulness of the tree; the color, scale and order of a heatmap (Definition 19.4.2) must be explained.
- k-means: $O(nkp)$, k-means++ and multiple starts; choose the number of clusters by the silhouette coefficient, Calinski–Harabasz, the gap statistic and stability. All the silhouette coefficients of airway are below 0.25 (Example 19.5.1): a structure of crossed factors is better described by principal components.
- Principal component analysis is computed by the singular value decomposition, with scree plots and biplots (Definition 19.6.1) as aids to interpretation. airway: PC1 39% is dexamethasone (*ZBTB16*, *FKBP5*, *KLF15* and others), PC2 27% is donor sex (*XIST* and Y-chromosome genes), and the first four components together give 97%, consistent with 1 + 3 degrees of freedom of the design (Example 19.6.1).
- Batch effects can be adjusted for in a balanced design and cannot be rescued when completely confounded with treatment; allocate batches by randomization. Principal component correction for population stratification in GWAS is the same idea (Section 19.7).
- t-SNE and UMAP preserve only local neighbors: distances between clusters and cluster sizes carry no meaning, and parameters and seeds change the appearance; use them for display, not for inference (Section 19.8).

## Questions

1. The 3 indicators of two patients are $\boldsymbol{x} = (1, 4, 2)$ and $\boldsymbol{y} = (3, 1, 2)$. Compute the Euclidean, Manhattan, Chebyshev and Canberra distances.

   **Answer** The differences are $(-2, 3, 0)$. Euclidean $\sqrt{4 + 9 + 0} = \sqrt{13} = 3.61$; Manhattan $2 + 3 + 0 = 5$; Chebyshev $\max = 3$; Canberra $2/4 + 3/5 + 0/4 = 0.5 + 0.6 + 0 = 1.1$.

2. The expression of two genes in 5 samples is $\boldsymbol{x} = (1, 2, 3, 4, 5)$ and $\boldsymbol{y} = (10, 20, 30, 40, 50)$. What are their Euclidean distance and correlation distance? Which should be chosen for clustering genes, and why? Then verify with Property 19.3.1: what is the Euclidean distance after standardizing the two?

   **Answer** The Euclidean distance is $\sqrt{81 + 324 + 729 + 1296 + 2025} = \sqrt{4455} = 66.7$, very large; the correlation coefficient is $r = 1$, so the correlation distance is 0. When looking for co-regulated genes, the concern is the pattern of "rising and falling together" and not the expression level, so the correlation distance should be chosen; by Euclidean distance these two perfectly synchronized genes would be separated because their expression differs by 10-fold. After standardization the two are identical, with distance $\sqrt{2(5 - 1)(1 - 1)} = 0$, consistent with Property 19.3.1.

3. The distances among 4 points are $d_{12} = 1$, $d_{13} = 4$, $d_{14} = 6$, $d_{23} = 3$, $d_{24} = 5$, $d_{34} = 2$. Perform hierarchical clustering with single linkage and with complete linkage, and write down each merge and its height.

   **Answer** At the first step both methods merge $\{1, 2\}$ (height 1). Single linkage: $d(\{1,2\}, 3) = \min(4, 3) = 3$, $d(\{1,2\}, 4) = \min(6, 5) = 5$, $d_{34} = 2$, so $\{3, 4\}$ is merged (height 2); $d(\{1,2\},\{3,4\}) = \min(4, 6, 3, 5) = 3$, and the last merge is at height 3. Complete linkage: $d(\{1,2\}, 3) = 4$, $d(\{1,2\}, 4) = 6$, $d_{34} = 2$, so $\{3, 4\}$ is merged (height 2); $d(\{1,2\},\{3,4\}) = \max = 6$, and the last merge is at height 6. The topology is the same, and the height of the last merge differs. Check complete linkage with the Lance–Williams formula: $d_{\{3,4\},\{1,2\}}$ follows from $d(\{1,2\},3) = 4$ and $d(\{1,2\},4) = 6$ as $\tfrac12(4 + 6) + \tfrac12\lvert 4 - 6\rvert = 6$.

4. Use the Lance–Williams formula to show that under average linkage the distance between the new cluster $k = i \cup j$ and cluster $h$ equals the average of the distances over all pairs of points between $k$ and $h$.

   **Answer** Let $d_{hi}$ be the average of the $n_hn_i$ pairwise distances between $h$ and $i$, so that the sum of the pairwise distances is $n_hn_id_{hi}$; likewise for $h$ and $j$. The sum of the pairwise distances between $k$ and $h$ is $n_hn_id_{hi} + n_hn_jd_{hj}$, the number of pairs is $n_h(n_i + n_j)$, and the average is $\frac{n_i}{n_i + n_j}d_{hi} + \frac{n_j}{n_i + n_j}d_{hj}$, exactly the case $\alpha_i = n_i/(n_i + n_j)$, $\beta = \gamma = 0$ of Formula 19.4.1.

5. A study performs principal component analysis on 20,000 genes of 6 patients, and the first principal component explains 35% of the variance; the authors conclude that "the data have strong structure". Is this reasoning correct? How can it be tested?

   **Answer** Not necessarily. With $n = 6$ there are at most 5 nonzero principal components, so even if the data have no structure at all, the first principal component explains on average more than about $1/5$ of the variance, and because of the spreading of sample eigenvalues (Section 19.1.2) often clearly more. One should compare with structureless data: independently permute each gene at random across the 6 patients (destroying the structure shared between samples while keeping the distribution of each gene), repeat several hundred times to obtain the null distribution of the variance proportion of the first principal component (parallel analysis); only if the observed value clearly exceeds it is there structure. One should also check whether the first principal component corresponds to known variables (treatment, batch, sex).

6. A laboratory processed 6 control samples on Monday and 6 drug-treated samples on Wednesday, and in the principal component analysis of the RNA-seq the first principal component separates the two groups completely. A reviewer finds the conclusion unreliable, and the authors reply that "we corrected for batch with ComBat". Evaluate this reply and say how the study should be designed.

   **Answer** Treatment is completely confounded with batch (date): the first principal component may be the drug effect or the date effect, and the data cannot tell them apart (Section 19.7, panels B and C). ComBat needs to know the batches and estimates batch parameters within each batch; under confounding the batch parameters and the treatment effect are not identifiable, and the correction either removes nothing or removes the treatment effect along with it. The only remedy is to repeat the experiment: process half controls and half treated samples each day (a block design), randomize the order of processing, and include date as a factor in the model.

7. For the airway data, k-means ($k = 2$) separates the samples by treatment, while single-linkage hierarchical clustering first splits off the two samples of donor N080611. Are the two results contradictory? Which one is "right"?

   **Answer** They are not contradictory; they answer different questions. k-means (the same objective as Ward's method) looks for the two clusters that minimize the within-cluster sum of squares, and the treatment effect explains the most variance (PC1 39%), so it splits by treatment. Single linkage looks only at the closest pair of points: the two samples of N080611 are far from all other samples (the minimum distance to the other samples is 34.0, while among the other samples there are closer chains), so they are joined last. Both are real features of the data: treatment is the largest source of variation, and N080611 is the most "distinctive" donor. Since treatment and donor are crossed, any single partition can express only part of the structure, and the principal component plot (Example 19.6.1) is more complete.

8. On a single-cell UMAP plot the T-cell cluster and B-cell cluster are far apart, while two myeloid subclusters are adjacent; on another plot drawn with different parameters the T-cell cluster looks much larger than the B-cell cluster. Can one conclude that "the transcriptome difference between T cells and B cells is greater than that between the two myeloid subclusters" and that "T cells have greater transcriptional heterogeneity"?

   **Answer** Neither can be concluded directly. UMAP preserves only local neighbor relations, and the distance between clusters on the plot and the size and density of the clusters do not faithfully reflect distances and variation in high dimensions (Section 19.8), and they change with the parameters. To compare the sizes of differences, compute the distances between cluster centers or the number of differentially expressed genes in principal component space or in the original expression space; to compare heterogeneity, compute the average distance of cells to the cluster center within each cluster or the variance within each cluster. A UMAP plot is used only to display clusters determined by clustering and marker genes.

9. (Analysis design) A study collects the blood transcriptomes (20,000 genes) and 12 clinical indicators (age, body mass index, lung function FEV1, eosinophil count, IgE and so on) of 300 asthma patients, hoping to find "asthma subtypes". Write a reasonable exploratory analysis plan and point out at least three possible pitfalls.

   **Answer** Plan: (1) Quality control: color principal component plots by sequencing batch, blood draw time and RNA quality, look for outlying samples and batch effects, and where necessary include batch in later models or correct for it when the design is balanced. (2) Transformation: apply a variance-stabilizing transformation to counts and select the 1000–2000 genes with the largest variation; the clinical indicators have different units, so analyze them separately after standardization. (3) Dimension reduction and clustering: principal component analysis on the genes, clustering on the first 10–20 principal components by Ward's method or k-means, choosing the number of clusters by silhouette coefficient, gap statistic and resampling stability, and comparing different distances and linkages. (4) Interpretation: compare the clinical indicators and differentially expressed genes of the clusters ([7.7.20](/7.7.20)), and replicate in an independent cohort. Pitfalls: clusters may reflect technical factors (batch, the cell composition of blood, for example the proportion of eosinophils itself changes the whole-blood transcriptome) rather than disease mechanisms; "one can always find clusters", since a clustering algorithm gives clusters even for structureless data, so a comparison with a null model is needed; defining subtypes by clustering on the same data and then comparing the subtypes by tests gives meaningless $p$-values (post-selection inference); the choice of the number of clusters and of the method is arbitrary, and conclusions should be robust to these choices.

10. Prove that for a centered data matrix $X$, the sample variance of the first principal component score is $d_1^2/(n - 1)$, and that the principal component scores are uncorrelated with one another.

    **Answer** The score matrix is $T = XV = UD$. The columns of $T$ are centered (as $X$ is centered). The sample covariance matrix is $T^{\mathsf T}T/(n - 1) = DU^{\mathsf T}UD/(n - 1) = D^2/(n - 1)$, since $U^{\mathsf T}U = I$. It is a diagonal matrix: the scores are uncorrelated, and the variance of the $k$th score is $d_k^2/(n - 1)$, which for $k = 1$ is the claim.
