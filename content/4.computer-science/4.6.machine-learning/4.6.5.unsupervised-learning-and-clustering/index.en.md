---
title: Unsupervised Learning and Clustering
description: The task of unsupervised learning; the goal of clustering and similarity measures for various data types; k-means initialization (k-means++) and large-scale variants (mini-batch); k-medoids clustering (PAM, CLARA, CLARANS); divisive hierarchical clustering; choosing the number of clusters and evaluating clusterings; DBSCAN.
source_hash: 1ba8a47b362e
---

The learning in the preceding chapters had a "teacher" in the sense that every training example came with a class or a target value. This chapter turns to unlabeled data and its most basic task, clustering, which groups similar objects together. The statistical theory of clustering was covered in [3.4.11](/3.4.11), which presents **hierarchical clustering**, **k-means clustering** with its objective function and convergence, the **silhouette coefficient**, and the **Gaussian mixture model** fitted by the **EM algorithm**. Here we only summarize these topics and concentrate on what machine learning uses frequently but the statistics course does not develop: similarity measures for various data types, the initialization of k-means and its variants for large data, k-medoids clustering (PAM, CLARA, CLARANS) in which a cluster is represented by an actual object, divisive hierarchical clustering, the evaluation of clusterings, and the density-based method DBSCAN, which finds clusters of arbitrary shape. The distance measures are those of instance-based learning in [4.6.4](/4.6.4).

## 5.1. Unsupervised Learning

**Supervised learning** learns from labeled examples $(x_i, y_i)$ and is concerned with the conditional distribution $P(Y \mid X)$: $X$ is an example described by features and is usually complex, whereas $Y$ is a class or a target value and is comparatively simple. **Unsupervised learning** has only the examples $x_1, \dots, x_n$ without labels and is concerned with the joint distribution $P(X) = P(X_1, \dots, X_d)$ of $X$ itself, that is, with the structure of the data. Between the two lies *semi-supervised learning*, which learns $P(Y \mid X)$ from a small amount of labeled data together with a large amount of unlabeled data; it is useful when labels are expensive and unlabeled data are cheap (medical images, speech, web pages).

The structure of data carries a great deal of information: if we shuffle the pixel positions of a photograph at random, every pixel keeps its color value, yet the image becomes meaningless. Unlabeled data can be used for the following tasks:

| Task | What it does | Examples |
|---|---|---|
| Clustering | Divide the data into groups when no classes are predefined | Customer segmentation, news aggregation |
| Dimensionality reduction | Reduce the number of variables to consider | **Principal component analysis** ([3.4.5](/3.4.5)), **multidimensional scaling** ([3.4.6](/3.4.6)) |
| Outlier detection | Identify errors, noise, or new signals not seen in training | Fraud detection, equipment failure |
| Density estimation | Describe the distribution of the data | **Kernel density estimation**, **Gaussian mixture model** |
| Representation learning | Discover latent regularities in the data to serve as features for later tasks | Self-supervised pretraining ([4.7.7](/4.7.7)) |

## 5.2. Clustering and Similarity

### 5.2.1. The Goal of Clustering

**Clustering** puts similar objects into the same class (a cluster), so that objects in the same cluster resemble one another and objects in different clusters differ markedly: birds of a feather flock together. A good clustering has small within-cluster distances and large between-cluster distances. The central issue is therefore the definition of similarity: between objects and, where needed, between clusters. A clustering method consists of three parts: the unlabeled data, a similarity or distance measure, and a clustering algorithm.

Clustering results are classified along two dimensions:

- In **hard clustering** each object belongs to exactly one cluster; in **soft clustering** an object may belong to several clusters to different degrees (for example, the posterior probabilities given by a Gaussian mixture model).
- Hierarchical clustering produces a tree of clusters (a **dendrogram**), which lets us interpret the data at different granularities; nonhierarchical clustering (**partitioning clustering**) produces only one flat partition.

Clustering has a wide range of applications: in biology, grouping homologous sequences into gene families and inferring population structure from genetic data; in image processing, organizing photo albums by person; in business, discovering distinct customer groups; on the web, aggregating news about the same event and finding similar users and access patterns in access logs.

### 5.2.2. Data Types and Similarity

An example is a vector $x \in D_1 \times D_2 \times \cdots \times D_d$, and the domain of each component can be one of the following:

| Type | Domain | Examples |
|---|---|---|
| Real | $D = \mathbb{R}$ | Height, temperature |
| Binary | $D = \{v_1, v_2\}$ | Sex |
| Nominal (unordered) | $D = \{v_1, \dots, v_M\}$ | Day of the week, city |
| Ordinal | $D \subseteq \mathbb{R}$ or ordered $\{v_1, \dots, v_M\}$ | Rank, "small, medium, large" |

Similarity and distance vary in opposite directions, and are often converted into each other by $\operatorname{sim} = 1/(1 + d)$ or $\operatorname{sim} = \mathrm{e}^{-d}$.

1. Real-valued data: the inner product $\langle x, y\rangle$, the **cosine similarity**, and kernel-based similarity $\exp(-\|x - y\|^2 / 2\sigma^2)$; for distances we use the Minkowski distance $\big(\sum_j \lvert x_j - y_j\rvert^p\big)^{1/p}$ of [4.6.4](/4.6.4), where $p = 1, 2, \infty$ give the Manhattan, Euclidean and Chebyshev distances. When the components have different units we standardize them first, and when they are correlated we can use the **Mahalanobis distance**.
2. Binary and nominal data: the simplest choice is "1 if equal and 0 if different", $\operatorname{sim}(x_j, y_j) = \boldsymbol{1}\{x_j = y_j\}$, whose average over all components is the simple matching coefficient. For sparse binary data (shopping baskets, the words occurring in a document) the Jaccard coefficient $\lvert A \cap B\rvert / \lvert A \cup B\rvert$ is common; it ignores the components where both are 0. We can also exploit semantic attributes of the values, for example defining the similarity of two cities by their geographic distance or the difference in population, or simply supply a similarity matrix.
3. Ordinal data: normalize the values to $[0, 1]$ according to their order (the minimum becomes 0, the maximum 1, and the rest are interpolated at equal spacing; for instance, "small, medium, large, extra large" become $0, 0.33, 0.67, 1$), and then use a real-valued measure; a similarity matrix can also be used.

**Example 5.2.1** A similarity matrix for size grades (only the upper triangle is shown):

| | Tiny | Little | Small | Medium | Large | Huge |
|---|---|---|---|---|---|---|
| Tiny | 1.0 | 0.8 | 0.7 | 0.5 | 0.2 | 0.0 |
| Little | | 1.0 | 0.9 | 0.7 | 0.3 | 0.1 |
| Small | | | 1.0 | 0.7 | 0.3 | 0.2 |
| Medium | | | | 1.0 | 0.5 | 0.3 |
| Large | | | | | 1.0 | 0.8 |
| Huge | | | | | | 1.0 |

A similarity matrix should be symmetric with ones on the diagonal, but it does not require the assumption of linear interpolation: the similarity of Little and Small (0.9) can be far higher than that of Medium and Large (0.5), which equally spaced normalization cannot express.

When components of different types are mixed, we can compute a similarity in $[0,1]$ for each component by the methods above and then take a weighted average (Gower's coefficient).

## 5.3. k-Means Clustering

### 5.3.1. The Algorithm and Its Convergence

**k-means clustering** ([3.4.11](/3.4.11#alg-11.3.1)) alternates two steps: given the cluster assignment, update the center of each cluster to the mean $g_1, \dots, g_k$ of its objects; given the centers, assign each object to the nearest center. Let the binary indicator $r_{iv} \in \{0, 1\}$ express whether object $u_i$ belongs to cluster $v$ (exactly one $r_{iv} = 1$ for each $i$); the algorithm minimizes

$$
J(r, g) = \sum_{i=1}^n \sum_{v=1}^k r_{iv}\,\|u_i - g_v\|^2 .
$$
The assignment step minimizes $J$ over $r$ with $g$ fixed, and the update step minimizes $J$ over $g$ with $r$ fixed (the optimum is the cluster mean), so $J$ is nonincreasing; since there are only finitely many partitions, the algorithm converges in finitely many steps, but only convergence to a local minimum is guaranteed ([3.4.11](/3.4.11#prop-11.3.1)). Finding the global minimum of $J$ is NP-hard, even in the plane. The characteristics of k-means can be summarized as follows: a vector space model, minimization of the within-cluster sum of squared Euclidean distances, iterative solution, hard clustering, nonhierarchical.

Each iteration costs $O(nkd)$ ($d$ is the dimension). k-means is also used for tasks other than clustering, such as image compression (color quantization): cluster the $(R, G, B)$ values of all pixels (without positions) into $k$ clusters and redraw every pixel in the color of its cluster center, so the image needs only $k$ colors.

### 5.3.2. Initialization: k-means++

The result of k-means depends strongly on the initial centers. If $k$ objects are chosen at random as initial centers, two centers may fall into the same true cluster, and the algorithm is then stuck in a poor local minimum; requiring the initial seeds to be pairwise farther apart than a threshold $d_{\min}$ is a naive remedy. k-means++ of Arthur and Vassilvitskii (2007) seeds randomly in proportion to the squared distance, which spreads the seeds without letting outliers dominate:

**Algorithm 5.3.1 (k-means++)** Let $D(u)$ be the distance from object $u$ to the nearest of the centers already chosen.

1. Choose the first center uniformly at random from the data;
2. Choose the next center $u$ with probability $D(u)^2 / \sum_{u'} D(u')^2$;
3. Repeat step 2 until $k$ centers are chosen, and then run the usual k-means iterations.

It can be shown that the objective value obtained with k-means++ seeding satisfies $\mathbb{E}[J] \le 8(\ln k + 2)\,J_{\mathrm{opt}}$ in expectation, so the seeding alone is already an $O(\log k)$-approximation. It is the default initialization of `KMeans` in scikit-learn; in practice one still runs the algorithm from several initializations (`n_init`) and keeps the result with the smallest $J$.

### 5.3.3. Large-Scale Data

With a large amount of data, every iteration must scan all $n$ objects. Common improvements include the following.

- Mini-batch k-means (Sculley, 2010): at each step take only a random mini-batch $B$ (say 1024 objects), assign each object $u$ in it to its nearest center $g$, let $v_g$ be the cumulative number of objects assigned to that center, and update $g \leftarrow (1 - \eta)\,g + \eta\,u$ with learning rate $\eta = 1/v_g$. This amounts to **stochastic gradient descent** on $J$, in the same spirit as **mini-batch gradient descent**; the cost per step is independent of $n$, and the objective value is usually only slightly worse than that of full k-means.
- Skipping unnecessary distance computations with the **triangle inequality** (Elkan, 2003): if $d(g, g') \ge 2\,d(u, g)$, then $g'$ cannot be closer than $g$; the result is exactly that of the original algorithm but much faster.
- Cluster a random sample first and then assign the remaining objects to the nearest centers; this idea is also used by CLARA below.

### 5.3.4. Limitations

k-means works well when the data form a few compact, well-separated "clouds". It implicitly looks for spherical clusters of similar size and spread, so it does poorly on clusters of nonconvex shape or of very different sizes or densities, and it is very sensitive to noise and outliers: a single point far from all clusters can pull a cluster mean off center. The next two sections address these two problems: k-medoids clustering makes the method more robust to outliers, and DBSCAN handles clusters of arbitrary shape.

## 5.4. k-Medoids Clustering

### 5.4.1. Medoids

The mean is easily pulled off by outliers and is meaningful only for vector data. k-medoids clustering represents a cluster by one of its actual objects.

**Definition 5.4.1 (k-Medoids Clustering)** Given $n$ objects and an arbitrary dissimilarity $d$, the **medoid** of a cluster $C$ is the object $m \in C$ that minimizes $\sum_{u \in C} d(u, m)$. **k-medoids clustering** selects $k$ objects $m_1, \dots, m_k$ as medoids and assigns each object to the nearest medoid so as to minimize the total cost

$$
\operatorname{cost}(m_1, \dots, m_k) = \sum_{i=1}^n \min_{1 \le v \le k} d(u_i, m_v).
$$

Compared with k-means, k-medoids clustering has three advantages: the centers are always real objects, which eases interpretation; it needs only the dissimilarity matrix and so applies to nominal data, strings, objects in graphs, and anything else for which a dissimilarity can be defined; and its cost is a sum of distances rather than of squared distances, so the influence of outliers is much smaller. The most naive algorithm copies the alternation of k-means: choose $k$ representative objects at random, assign the other objects to the nearest representative, then in each cluster choose anew the object with the smallest cost as the center, and repeat until nothing changes. This alternation is fast but easily stops in a poor local minimum.

### 5.4.2. PAM

**Algorithm 5.4.1 (PAM)** PAM (Partitioning Around Medoids; Kaufman and Rousseeuw, 1987) has two phases.

1. BUILD: first choose the object with the smallest total cost, and then greedily add, one at a time, the object that lowers the total cost most, until there are $k$ medoids.
2. SWAP: for every pair (medoid $m$, nonmedoid $h$), compute the total cost after replacing $m$ by $h$; if the best replacement lowers the cost, perform it, and repeat until no replacement lowers the cost.

A randomized version of SWAP is also used: at each step a nonmedoid $O_{\mathrm{random}}$ is chosen at random and exchanged with a medoid, and the exchange is kept if the cost decreases and otherwise not. For example, in an instance with $k = 2$, the current total cost under the Manhattan distance is 20 and the total cost after a random exchange is 26, so the exchange is not made.

The partition at which the SWAP phase stops is a local optimum in the sense that no exchange of a single medoid improves it; only by enumerating all $\binom{n}{k}$ combinations of medoids can we guarantee the global optimum. In a naive implementation each round evaluates $k(n-k)$ exchanges, and each exchange needs $O(n-k)$ time to recompute the cost, for a total of $O(k(n-k)^2)$, much slower than k-means, so the original PAM is suitable only for small data sets. FastPAM of Schubert and Rousseeuw (2021) reduces the cost per round by about a factor of $k$ by sharing computation, with the same result.

Below is a direct implementation of PAM. The data are two clusters of 20 points each, plus one distant outlier:

```python
import numpy as np


def pam(D, k, max_iter=100):
    """PAM (BUILD + SWAP) on a precomputed dissimilarity matrix D."""
    n = D.shape[0]
    # BUILD: greedily add the medoid that lowers the total cost most
    medoids = [int(np.argmin(D.sum(axis=1)))]
    while len(medoids) < k:
        nearest = D[:, medoids].min(axis=1)
        gains = [np.maximum(nearest - D[:, c], 0).sum() if c not in medoids else -1
                 for c in range(n)]
        medoids.append(int(np.argmax(gains)))
    cost = D[:, medoids].min(axis=1).sum()
    # SWAP: try every (medoid, non-medoid) pair, apply the best improving swap
    for _ in range(max_iter):
        best = (cost, None, None)
        for i in range(k):
            for h in range(n):
                if h in medoids:
                    continue
                trial = medoids[:i] + [h] + medoids[i + 1:]
                c = D[:, trial].min(axis=1).sum()
                if c < best[0]:
                    best = (c, i, h)
        if best[1] is None:
            break
        cost, i, h = best
        medoids[i] = h
    labels = D[:, medoids].argmin(axis=1)
    return medoids, labels, cost


rng = np.random.default_rng(0)
X = np.vstack([rng.normal([0, 0], 0.5, (20, 2)),
               rng.normal([4, 4], 0.5, (20, 2)),
               [[30.0, 30.0]]])                      # one gross outlier
D = np.abs(X[:, None, :] - X[None, :, :]).sum(axis=2)  # Manhattan distance
medoids, labels, cost = pam(D, k=2)
print("medoids:", X[medoids].round(2).tolist())
print("cluster sizes:", np.bincount(labels).tolist(), "total cost:", round(cost, 2))

# k-means (Lloyd) on the same data for comparison
centers = X[[0, 20]].copy()
for _ in range(100):
    lab = ((X[:, None, :] - centers) ** 2).sum(axis=2).argmin(axis=1)
    centers = np.array([X[lab == j].mean(axis=0) for j in range(2)])
print("k-means centers:", centers.round(2).tolist())
```

```text
medoids: [[4.21, 4.35], [-0.23, 0.11]]
cluster sizes: [21, 20] total cost: 81.32
k-means centers: [[-0.14, 0.07], [5.43, 5.33]]
```

The outlier is assigned to the upper-right cluster, but the medoid stays near $(4, 4)$; the cluster mean of k-means, in contrast, is pulled by it to $(5.4, 5.3)$.

### 5.4.3. CLARA and CLARANS

**Algorithm 5.4.2 (CLARA)** CLARA (Clustering LARge Applications; Kaufman and Rousseeuw, 1990) is designed for large samples:

1. Draw a small random sample from the data (the original authors suggest $40 + 2k$ objects) and run PAM on the sample to obtain $k$ medoids;
2. Assign all objects to the nearest medoid and compute the total cost on the whole data;
3. Repeat the sampling several times (for example 5 times) and take the set of medoids with the smallest total cost as the result.

The cost of CLARA is linear in $n$ for each draw, but if the optimal medoids are not drawn into any sample, they cannot be found. CLARANS (Ng and Han, 1994) does not fix a sample but performs a randomized local search on the graph whose nodes are all combinations of $k$ medoids: two combinations are adjacent if they differ in exactly one medoid. Starting from one combination, it examines at most `maxneighbor` random neighbors, moves to one as soon as it has a lower cost, and declares a local minimum if none does; this is repeated `numlocal` times and the best result is kept. It is more flexible than CLARA and usually more accurate.

## 5.5. Hierarchical Clustering

### 5.5.1. Agglomerative Clustering

Agglomerative (bottom-up) hierarchical clustering was discussed in detail in [3.4.11](/3.4.11#alg-11.2.1): every object starts as its own cluster, and the two most similar clusters $c_i, c_j$ are merged repeatedly, replaced by $c_i \cup c_j$ with the similarities between the new cluster and the others recomputed, until $k$ clusters remain ($k$ may be 1). The similarity between clusters is determined by the linkage: **single linkage** takes the most similar pair of points in the two clusters, **complete linkage** the least similar pair, and **average linkage** the average over all pairs. The merging process is recorded as a dendrogram, and cutting it at different heights gives clusterings of different granularities.

A classical example clusters six Italian cities (Turin, Milan, Florence, Rome, Naples, Bari) with the Euclidean distance and single linkage: in each round we find the two closest clusters in the distance matrix and merge them, and then update the matrix by single linkage (the distance from the new cluster to any other is the smaller of the two old distances); the matrix shrinks by one row and one column each round, and after five rounds we obtain the complete dendrogram.

Hierarchical clustering is common in scientific data analysis. For example, Mesgarani et al. (2014) recorded the responses of electrodes on the superior temporal gyrus of epilepsy patients to different English phonemes and clustered electrodes and phonemes hierarchically; they found that phonemes first split into two large groups, obstruents and sonorants, and are then subdivided by manner of articulation, with the electrodes grouped accordingly: the auditory cortex encodes speech in units of articulatory features.

### 5.5.2. Divisive Clustering

Divisive (top-down) hierarchical clustering starts from a single cluster containing all objects and splits one cluster into two at each step. The most common method is DIANA (DIvisive ANAlysis; Kaufman and Rousseeuw, 1990):

**Algorithm 5.5.1 (DIANA)** Repeat the following steps until every cluster contains a single object (or there are $k$ clusters):

1. Choose the cluster $C$ with the largest diameter (the largest within-cluster dissimilarity);
2. In $C$, find the object with the largest average dissimilarity to the other objects and let it form a "splinter group" by itself, with the remaining objects of $C$ forming the "old group";
3. For each object $u$ in the old group, compute the difference between its average dissimilarity to the other objects of the old group and its average dissimilarity to the splinter group; if the largest difference is positive, move the corresponding object into the splinter group, and repeat this step until no object is closer to the splinter group;
4. Replace $C$ by the splinter group and the old group.

The two approaches compare as follows:

| | Divisive | Agglomerative |
|---|---|---|
| Information used | Each split can use global information about the whole cluster | Each merge looks only at local information between two clusters |
| Granularity | Can stop after the top few levels for a coarse division | Must merge all the way to the end to obtain the top-level structure |
| Implementation | Finding the best split is complicated and often relies on partitioning clustering (for example, k-means with $k = 2$ at each step, called bisecting k-means) | Merging close clusters is simple and needs no other algorithm |
| Correcting errors | Once separated, clusters are never merged again | Once merged, clusters are never separated again |

Hierarchical clustering lets us observe the data at different granularities and works with any definition of similarity, hence with any attribute type; its drawbacks are that the stopping criterion (where to cut the dendrogram) is uncertain and that the computation is expensive (agglomerative clustering needs $O(n^2)$ memory and at least $O(n^2)$ time), so it is hard to apply directly to large data sets.

## 5.6. Number of Clusters and Clustering Quality

### 5.6.1. Choosing the Number of Clusters

The number of clusters $k$ is best determined by the problem itself: for example, clothes are grouped into the three sizes S, M, L, so $k = 3$. Only when the data are not sparse and no dimension is noticeably noisy is it appropriate to let the data alone determine $k$. Data-driven methods all examine how the within-cluster dissimilarity $W_k$ (such as the objective $J$ of k-means) varies with $k$; $W_k$ decreases monotonically in $k$ and equals 0 at $k = n$, so we cannot simply take its minimum.

- The **elbow method**: $W_k$ drops sharply up to the true number of clusters and changes slowly afterwards; take the bend of the curve.
- The **gap statistic**: cluster reference data without cluster structure (for example, uniformly distributed over the range of the data) with the same algorithm, compare $\ln W_k$ with its expected value on the reference data, and take the $k$ with a large gap.
- The **silhouette coefficient**: take the $k$ that maximizes the average silhouette coefficient over all objects. It depends only on dissimilarities, so it also applies to k-medoids and hierarchical clustering.
- Model-based clustering selects $k$ with an information criterion such as BIC ([3.4.11](/3.4.11#def-11.4.2)).

![Choosing k on data with four clusters. Left: the data. Middle: the within-cluster sum of squares W_k of k-means, with an elbow at k = 4. Right: the average silhouette coefficient, maximal at k = 4](./plots/choose-k.py)

### 5.6.2. Evaluating Clustering Results

Evaluating a clustering is harder than evaluating a classifier because there is usually no correct answer. The evaluation measures fall into two groups:

- Internal measures use only the data themselves: the within-cluster sum of squares, the average silhouette coefficient, the Davies–Bouldin index (smaller is better), and the Calinski–Harabasz index (the ratio of between-cluster to within-cluster scatter, larger is better). Most of them favor convex, spherical clusters.
- External measures compare the clustering with known classes (used to evaluate algorithms on labeled data): purity, the adjusted Rand index (ARI, which equals 1 when two partitions agree exactly, has expectation 0 for random partitions, and does not depend on the cluster labels), and normalized mutual information (NMI).

In the end we must return to the application: a clustering may give "surprising" results, such as seriously unbalanced cluster sizes, disagreement with conventional human categories, or clusters that are hard to interpret. Such results are not necessarily wrong, but they call for checking the preprocessing, the similarity measure and the choice of algorithm against domain knowledge.

## 5.7. Density-Based Clustering: DBSCAN

Both k-means and k-medoids clustering regard a cluster as a lump around a center; they cannot find clusters of arbitrary shape such as rings or crescents, and they force every noise point into some cluster. Density-based methods regard a cluster as a region of high density separated from others by regions of low density.

**Definition 5.7.1 (DBSCAN)** Given a radius $\varepsilon > 0$ and an integer $\mathrm{minPts}$, the $\varepsilon$-neighborhood of an object $p$ is $N_\varepsilon(p) = \{q : d(p, q) \le \varepsilon\}$ (including $p$ itself). **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise; Ester et al., 1996) defines a cluster as the set of all objects density-reachable from some core point; objects of a cluster that are not core points are called **boundary points**, and objects belonging to no cluster are called **noise points**. Here:

- if $\lvert N_\varepsilon(p)\rvert \ge \mathrm{minPts}$, $p$ is a **core point**;
- if $q \in N_\varepsilon(p)$ and $p$ is a core point, $q$ is **directly density-reachable** from $p$; if there is a chain of objects $p = p_1, p_2, \dots, p_m = q$ in which each is directly density-reachable from the previous one, $q$ is **density-reachable** from $p$;
- if $p, q$ are both density-reachable from some object $o$, then $p, q$ are **density-connected**. Any two objects in the same cluster are density-connected.

The algorithm is simple: take an unassigned core point, search the graph from it (breadth-first or depth-first), and put all density-reachable objects into a new cluster; after all core points are processed, the remaining objects are noise. DBSCAN does not need the number of clusters, finds clusters of arbitrary shape, and identifies noise; apart from boundary points, which may be adjacent to two clusters, the result does not depend on the order in which objects are processed. The main computation is the neighborhood query, which is fast on low-dimensional data with a spatial index such as the **k-d tree** and $O(n^2)$ in the worst case.

Empirical choices of the parameters: take $\mathrm{minPts}$ at least the dimension plus one, usually 4 or 5 for two-dimensional data; $\varepsilon$ can be read from the $k$-distance plot, in which the distance of each object to its $(\mathrm{minPts} - 1)$-th nearest neighbor is sorted in decreasing order and plotted, and the value at the pronounced bend of the curve is taken. The main weakness of DBSCAN is that it has only one global density threshold: when the clusters differ greatly in density, no single $\varepsilon$ suits all of them. HDBSCAN (Campello et al., 2013) builds a hierarchy of densities over all $\varepsilon$ and selects the most stable clusters from it, which alleviates this problem, and it has been available in scikit-learn since version 1.3.

![Two interleaved half-moons with background noise. Left: k-means (k = 2) cuts the data in half along a straight line. Right: DBSCAN finds the two crescents (filled markers are core points, open markers are boundary points) and labels the scattered points as noise (crosses)](./plots/kmeans-vs-dbscan.py)

## 5.8. Practice

The clustering algorithms in scikit-learn share a uniform interface: after `fit`, the cluster labels are read from `labels_` (DBSCAN uses $-1$ for noise). The example below selects $k$ with the elbow method and the silhouette coefficient, compares mini-batch with full k-means, and compares k-means with DBSCAN on crescent-shaped data:

```python
import numpy as np
from sklearn.cluster import DBSCAN, KMeans, MiniBatchKMeans
from sklearn.datasets import make_blobs, make_moons
from sklearn.metrics import adjusted_rand_score, silhouette_score

# choose k for k-means by inertia (elbow) and silhouette
X, y = make_blobs(n_samples=600, centers=4, cluster_std=1.0, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f"k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}")

# mini-batch k-means on a large data set
Xbig, _ = make_blobs(n_samples=200_000, centers=4, random_state=0)
mbk = MiniBatchKMeans(n_clusters=4, batch_size=1024, n_init=3, random_state=0).fit(Xbig)
km = KMeans(n_clusters=4, n_init=3, random_state=0).fit(Xbig)
print(f"inertia: mini-batch {mbk.inertia_:.0f}, full {km.inertia_:.0f}")

# non-convex clusters: k-means vs DBSCAN
Xm, ym = make_moons(n_samples=400, noise=0.06, random_state=0)
km_labels = KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(Xm)
db_labels = DBSCAN(eps=0.2, min_samples=5).fit_predict(Xm)
print("ARI k-means:", round(adjusted_rand_score(ym, km_labels), 3))
print("ARI DBSCAN: ", round(adjusted_rand_score(ym, db_labels), 3),
      "clusters:", len(set(db_labels) - {-1}), "noise points:", int((db_labels == -1).sum()))
```

```text
k=2  inertia=  2922.1  silhouette=0.463
k=3  inertia=  1682.3  silhouette=0.467
k=4  inertia=  1043.8  silhouette=0.500
k=5  inertia=   918.9  silhouette=0.436
k=6  inertia=   809.7  silhouette=0.402
inertia: mini-batch 358349, full 358327
ARI k-means: 0.274
ARI DBSCAN:  1.0 clusters: 2 noise points: 0
```

The within-cluster sum of squares (`inertia_`) decreases more slowly after $k = 4$, and the silhouette coefficient is largest at $k = 4$; both point to the true number of clusters. On 200,000 points, the objective value of mini-batch k-means differs from that of the full algorithm by less than one part in ten thousand. On the crescent data, the ARI of k-means is only 0.27, whereas DBSCAN recovers the two clusters exactly.

## Summary

| Method | Cluster representative | Required input | Cluster shape | Outliers | Scale |
|---|---|---|---|---|---|
| k-means | Mean | Vectors, $k$ | Convex, spherical, similar size | Sensitive | Large (larger with mini-batch) |
| k-medoids (PAM) | Medoid (a real object) | Any dissimilarity, $k$ | Convex | Robust | Small; CLARA and CLARANS for large data |
| Hierarchical clustering | Dendrogram | Any dissimilarity, linkage | Depends on linkage | Single linkage is sensitive | Small ($O(n^2)$) |
| DBSCAN | Density-connected regions | Dissimilarity, $\varepsilon$, $\mathrm{minPts}$ | Arbitrary | Labeled as noise | Medium to large (with a spatial index) |
| Gaussian mixture (EM) | Probability model | Vectors, $k$ | Ellipsoidal, soft clustering | Sensitive | Medium |

The result of clustering depends on three choices, the similarity, the algorithm and the number of clusters, and there is no answer that fits all cases: determine the similarity from the data type, choose the algorithm according to the shape of the clusters and the noise, and then check the result with internal measures, external measures and domain knowledge.
