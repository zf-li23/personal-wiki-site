---
title: Instance-Based Learning
description: Parametric and nonparametric methods; instance-based (lazy) learning; the nearest neighbor rule, Voronoi diagrams and the Cover–Hart bound; distance measures, attribute normalization and weighting, choice of k and tie breaking for k-nearest neighbors; the curse of dimensionality; nearest neighbor queries with k-d trees and approximate nearest neighbor search (LSH, HNSW, IVF-PQ, FAISS); distance-weighted k-nearest neighbors, kernel regression and locally weighted regression.
source_hash: f0e83e0cad70
---

The methods of the preceding chapters all follow a "three-step" path: estimate the characteristics of the problem, make a model assumption (a linear function, normal noise, conditional independence, and so on), and then find the optimal parameters. This chapter introduces a method that does not take this path: it builds no explicit model and only stores the training examples; when a new example must be predicted, it finds the training examples most similar to it and answers with their outputs. This is the idea that "birds of a feather flock together": thinking as recall and analogy. The most typical method is $k$-nearest neighbors, which already appeared in multivariate analysis in the statistics courses ([3.4.12](/3.4.12)); this chapter discusses its design choices systematically (the distance, the treatment of attributes, the choice of $k$) as well as its two fundamental difficulties: distances lose their meaning in high-dimensional spaces (the curse of dimensionality), and the computational cost at prediction time. The latter leads to the k-d tree ([4.3.7](/4.3.7)) and to the approximate nearest neighbor search that underlies vector retrieval today. Finally, the idea of "weighting by distance" is extended to regression, giving kernel regression and locally weighted regression, the machine learning view of nonparametric regression in statistics ([3.3.12](/3.3.12), to be discussed systematically in [Nonparametric Statistics](/3.6)).

## 4.1. Basic Concepts

### 4.1.1. Parametric and Nonparametric Methods

A parametric method fixes a particular functional form (such as a linear function), and learning means estimating the finitely many parameters in it. It is simple and easy to estimate and interpret, but if the true distribution of the data does not conform to the assumed form, there is a large bias. A nonparametric method makes far fewer assumptions about the functional form, and the estimate is driven by the data; the complexity of the model grows with the amount of data, at the cost of needing more data and computation. Instance-based learning is the most typical nonparametric method.

### 4.1.2. Instance-Based Learning

**Definition 4.1.1 (Instance-Based Learning)** In training, only the training examples are stored and no global approximation to the target function is constructed; whenever a new example must be predicted, the stored examples similar to it are retrieved and the prediction is made locally from them. Such methods are called **instance-based learning**; since they postpone computation until query time, they are also called **lazy learning**.

It is also called memory-based learning, example-based learning or similarity-based learning, and in the context of reasoning, case-based reasoning. In contrast to lazy learning, methods such as linear regression, naive Bayes and neural networks construct a global model during training and are called eager learning.

From the instance-based viewpoint, a concept $c$ can be represented by three things: a set of examples $\{e_1, e_2, \dots\}$, a similarity function $f$ and a threshold $\theta$. An instance $a$ belongs to $c$ if and only if it is sufficiently similar to some example $e_j$ in $c$: $f(e_j, a) > \theta$. "Find the ten images most similar to this image" and "find all similar gene fragments between two genomes" are problems of this kind.

## 4.2. Nearest Neighbors and k-Nearest Neighbors

### 4.2.1. The Nearest Neighbor Rule

Similarity corresponds to distance: the smaller the distance, the more similar. The simplest rule is to classify a new example $\boldsymbol{x}_q$ into the class of the training example nearest to it, called the nearest neighbor rule (1-NN).

**Example 4.2.1** Credit is assessed with two features: $L$ is the number of late payments per year, and $R$ is the ratio of income to expenses. The ratings of 8 customers are known (G for good, P for poor):

| Customer | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| $L$ | 0 | 25 | 5 | 20 | 30 | 11 | 7 | 15 |
| $R$ | 1.2 | 0.4 | 0.7 | 0.8 | 0.85 | 1.2 | 1.15 | 0.8 |
| Rating | G | P | G | P | P | G | G | P |

What are the ratings of the new customers I $(6, 1.15)$, J $(22, 0.45)$ and K $(15, 1.2)$? Using the Euclidean distance directly, the nearest neighbor of I is G (distance $1.0$), so I is rated good; the nearest neighbor of J is D (distance about $2.03$), so J is rated poor; the nearest neighbor of K is H (distance $0.4$), so K is rated poor. But the range of $L$ ($0$ to $30$) is much larger than that of $R$ ($0.4$ to $1.2$), and the distance is determined almost entirely by $L$. After scaling both features to $[0,1]$ by their ranges, the nearest neighbor of I is still G, that of J becomes B (still rated poor), and that of K becomes F (distance about $0.13$), so K is rated good: K has a moderate number of late payments but an income-to-expense ratio as high as the good customers. The definition of the distance directly determines the answer; we return to this in Sec. 4.2.4.

**Definition 4.2.1 (Voronoi Diagram)** Let $S = \{\boldsymbol{x}_1, \dots, \boldsymbol{x}_n\}$ be a finite set of points in Euclidean space. The Voronoi cell of $\boldsymbol{x}_i$ is the set of points closer to $\boldsymbol{x}_i$ than to any other point of $S$, $\{\boldsymbol{x}\colon d(\boldsymbol{x}, \boldsymbol{x}_i) \le d(\boldsymbol{x}, \boldsymbol{x}_j)\ \forall j\}$; all the cells form a partition of the space, called the **Voronoi diagram** of $S$.

The decision regions of 1-NN are the Voronoi diagram of the training examples: every point in a cell is assigned the class of the cell's center, and the decision boundary consists of the cell boundaries between examples of different classes. Almost every point has exactly one nearest example; points on cell boundaries are equidistant from two or more examples, and these points form a set of measure zero.

The nearest neighbor rule is so simple, yet its asymptotic performance has a beautiful bound. Let $R^*$ be the error rate of the **Bayes classifier**, the **optimum error rate** ([3.4.10](/3.4.10)), which no classifier can fall below.

**Theorem 4.2.1 (Cover–Hart)** Suppose there are $c$ classes and the number of training examples $n \to \infty$. Under suitable regularity conditions, the asymptotic error rate $R$ of 1-NN satisfies

$$
R^* \le R \le R^*\Bigl(2 - \frac{c}{c-1}R^*\Bigr) \le 2R^*.
$$

The proof is long (see Duda, Hart and Stork, *Pattern Classification*). Intuitively: when the examples are dense enough, the nearest neighbor of $\boldsymbol{x}_q$ almost coincides with $\boldsymbol{x}_q$, and its class is equivalent to an independent sample drawn from the posterior class distribution at $\boldsymbol{x}_q$; 1-NN errs if and only if the class of $\boldsymbol{x}_q$ itself differs from this independent sample. This is a result of the same kind as the statement in [4.6.3](/4.6.3#sec-3.3.2) that the Gibbs algorithm, which samples from the posterior, has an error rate at most twice the optimum. So with infinitely much data, even the simplest nearest neighbor rule has an error rate no more than twice the optimal value; one can say that half of the information in any classification problem is contained in the nearest neighbor. But this is only an asymptotic conclusion: with finite samples in high-dimensional spaces, the nearest neighbor may be far away (Sec. 4.3).

### 4.2.2. k-Nearest Neighbors

What if the nearest neighbor happens to be noise? The natural remedy is to look at more than one neighbor and let them vote.

**Algorithm 4.2.1 (k-Nearest Neighbors)** Given training examples $(\boldsymbol{x}_i, y_i)$, a distance $d$ and a positive integer $k$. For a query $\boldsymbol{x}_q$, find the $k$ training examples $\boldsymbol{x}_{(1)}, \dots, \boldsymbol{x}_{(k)}$ nearest to it:

- classification: output the class that occurs most often among them, $\hat y_q = \arg\max_{v}\sum_{j=1}^k \boldsymbol{1}(y_{(j)} = v)$;
- regression: output their average, $\hat y_q = \frac{1}{k}\sum_{j=1}^k y_{(j)}$.

This is **k-nearest neighbors** (KNN). For $k = 1$ it is the nearest neighbor rule.

**Example 4.2.2** Predict, from age, income (in thousands) and the number of credit cards held, whether the customer David will respond to a sales offer:

| Customer | Age | Income | Cards | Responded | Distance to David |
|---|---|---|---|---|---|
| John | 35 | 35 | 3 | No | $\sqrt{2^2 + 15^2 + 1^2} \approx 15.17$ |
| Mary | 22 | 50 | 2 | Yes | $\sqrt{15^2 + 0^2 + 0^2} = 15$ |
| Hannah | 63 | 200 | 1 | No | $\approx 152.23$ |
| Tom | 59 | 170 | 1 | No | $\approx 122.00$ |
| Nellie | 25 | 40 | 4 | Yes | $\sqrt{12^2 + 10^2 + 2^2} \approx 15.75$ |
| David | 37 | 50 | 2 | ? | |

The 3 nearest neighbors are Mary (yes), John (no) and Nellie (yes), and the vote gives "yes".

```python
import numpy as np

names = ["John", "Mary", "Hannah", "Tom", "Nellie"]
X = np.array([[35, 35, 3], [22, 50, 2], [63, 200, 1], [59, 170, 1], [25, 40, 4]], dtype=float)
y = np.array(["No", "Yes", "No", "No", "Yes"])
q = np.array([37, 50, 2], dtype=float)                 # David: age, income (K), cards

def knn_predict(X, y, q, k=3):
    d = np.sqrt(((X - q) ** 2).sum(axis=1))           # Euclidean distances to the query
    nn = np.argsort(d)[:k]
    labels, votes = np.unique(y[nn], return_counts=True)
    return labels[np.argmax(votes)], nn, d

lo, hi = X.min(axis=0), X.max(axis=0)                 # min-max scaling fitted on training data
for name, A, b in [("raw", X, q), ("min-max", (X - lo) / (hi - lo), (q - lo) / (hi - lo))]:
    label, nn, d = knn_predict(A, y, b)
    print(f"{name:8}", [(names[i], round(float(d[i]), 2)) for i in nn], "->", label)
```

```text
raw      [('Mary', 15.0), ('John', 15.17), ('Nellie', 15.75)] -> Yes
min-max  [('John', 0.35), ('Mary', 0.37), ('Nellie', 0.73)] -> Yes
```

(Python 3.12, NumPy 2.5.) After normalization the conclusion is unchanged, but the order of the nearest neighbors changes: in the raw distances the number of cards plays almost no role (its values differ by only $1$ to $2$), whereas after normalization it is as important as age and income.

### 4.2.3. Distance Measures

Let $\boldsymbol{x}_i = (x_{i1}, \dots, x_{ip})$ and $\boldsymbol{x}_j = (x_{j1}, \dots, x_{jp})$.

**Definition 4.2.2 (Minkowski Distance)** For $\lambda \ge 1$,

$$
d_\lambda(\boldsymbol{x}_i, \boldsymbol{x}_j) = \Bigl(\sum_{k=1}^p \lvert x_{ik} - x_{jk}\rvert^\lambda\Bigr)^{1/\lambda}
$$
is called the $L_\lambda$ distance or **Minkowski distance**. For $\lambda = 2$ it is the **Euclidean distance**; for $\lambda = 1$ it is the **Manhattan distance** $\sum_k \lvert x_{ik} - x_{jk}\rvert$ (also called the city-block or taxicab distance); and as $\lambda \to \infty$ it is the **Chebyshev distance** $\max_k \lvert x_{ik} - x_{jk}\rvert$ (also called the chessboard distance or $L_\infty$ distance).

Other commonly used distances and similarities:

| Name | Formula | Use |
|---|---|---|
| Weighted Euclidean distance | $\sqrt{\sum_k w_k (x_{ik} - x_{jk})^2}$ | Attributes of different importance (Sec. 4.2.4) |
| **Mahalanobis distance** | $\sqrt{(\boldsymbol{x}_i - \boldsymbol{x}_j)^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_i - \boldsymbol{x}_j)}$ | Correlated attributes with different scales ([3.4.1](/3.4.1)) |
| Canberra distance | $\sum_k \frac{\lvert x_{ik} - x_{jk}\rvert}{\lvert x_{ik}\rvert + \lvert x_{jk}\rvert}$ | Data with values near $0$; sensitive to small differences |
| Bray–Curtis dissimilarity | $\frac{\sum_k \lvert x_{ik} - x_{jk}\rvert}{\sum_k (x_{ik} + x_{jk})}$ | Nonnegative count or abundance data (ecology) |
| Hamming distance | Number of attributes with different values | Categorical attributes |
| **Cosine similarity** | $\frac{x_i^{\mathsf T}\boldsymbol{x}_j}{\|\boldsymbol{x}_i\|\,\|\boldsymbol{x}_j\|}$ | Text, embedding vectors: looks at direction only, not length |

For unit vectors, $\|\boldsymbol{x}_i - \boldsymbol{x}_j\|^2 = 2 - 2\cos\theta$, so after normalizing the vectors to unit length, the Euclidean nearest neighbor and the cosine nearest neighbor coincide. This is commonly used in vector retrieval.

### 4.2.4. Normalizing and Weighting Attributes

The distance between neighbors can be dominated by a single attribute with particularly large values. For example, between John (age 35, annual income 95 thousand) and Rachel (age 41, annual income 215 thousand), if income is measured in dollars the distance is almost exactly the income difference $120\,000$, and age and the number of cards play no role at all. Normalizing the attributes is therefore very important:

- min–max normalization: $x' = \frac{x - \min}{\max - \min} \in [0, 1]$ (the approach of Examples 4.2.1 and 4.2.2);
- **standardization**: $x' = \frac{x - \bar x}{s}$, with mean $0$ and standard deviation $1$, somewhat more robust to outliers than min–max;
- for strongly right-skewed attributes (income, counts), take logarithms first and then normalize.

The normalization parameters (minimum, maximum, mean, standard deviation) must be computed on the training set only and then applied to the test examples; otherwise it is [data leakage](/4.6.2#sec-2.5).

$k$-nearest neighbors has a deeper problem: the classification of an example is based on all attributes, regardless of whether an attribute is relevant to the class. If an example is described by $20$ attributes of which only $2$ are relevant to the class, examples that agree on those $2$ attributes can be far apart in the $20$-dimensional space. The remedy is to weight the attributes by relevance, scaling each dimension in the distance:

$$
d_w(\boldsymbol{x}_i, \boldsymbol{x}_j) = \Bigl(\sum_{k=1}^p w_k (x_{ik} - x_{jk})^2\Bigr)^{1/2}.
$$
$w_k = 0$ deletes the $k$-th attribute, that is, feature selection. One feasible weighting method takes $w_k$ to be the mutual information between the attribute and the class, $I(X_k; Y) = H(X_k) + H(Y) - H(X_k, Y)$, where $H$ is the entropy and $H(X, Y) = -\sum_{x, y} p(x, y)\log p(x, y)$ is the joint entropy; one can also treat $w_k$ as a **hyperparameter** selected by cross-validation, or learn a full linear transformation (metric learning).

### 4.2.5. Choosing k and Breaking Ties

$k$ controls the complexity of the model. For $k = 1$ the decision boundary follows every training example closely and is sensitive to noise; as $k$ increases the boundary becomes smoother and the predictions more stable, but real local structure is smoothed away; for $k = n$ the prediction is always the majority class. This is yet another **bias–variance trade-off**.

![Decision regions of k-nearest neighbors for k = 1, 15 and 75 on the same noisy two-class data; the titles give the 10-fold cross-validation error rates: k = 1 overfits and k = 75 is too smooth](./plots/knn-decision-boundary.py)

- Empirically $k$ is often a small odd number between $3$ and $10$, but the suitable value depends on the number of training examples and the noise level, and a larger $k$ is not necessarily better.
- $k$ should be selected by **cross-validation**. For $k$-nearest neighbors, **leave-one-out cross-validation** needs almost no extra computation: each time, take one example out for validation and find its neighbors among the remaining examples, with no need to "retrain".
- $k$-nearest neighbors is stable: small perturbations in the training examples do not change the result much (decision trees, in contrast, are unstable; see [4.5.6](/4.5.6) and [4.6.6](/4.6.6)).

Ties (for example, an even $k$ in binary classification, or $k = 3$ with the three neighbors belonging to three different classes) can be handled as follows: in binary classification take an odd $k$; look at the $(k+1)$-th neighbor; take the class of the nearest neighbor; choose at random; or output the proportion of each class as the probability (such as $1/3$). A better way is to give nearer neighbors more votes; see Sec. 4.5.

The following code uses scikit-learn on the breast cancer dataset (569 examples, 30 attributes) to compare the effect of normalization, and uses 10-fold cross-validation to select both $k$ and whether to weight by distance.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_breast_cancer(return_X_y=True)            # 569 tumours, 30 features
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

raw = KNeighborsClassifier(n_neighbors=5)
scaled = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
for name, model in [("raw", raw), ("standardized", scaled)]:
    print(f"{name:13} 10-fold CV accuracy: {cross_val_score(model, X_tr, y_tr, cv=10).mean():.3f}")

grid = GridSearchCV(scaled, {"kneighborsclassifier__n_neighbors": range(1, 31, 2),
                             "kneighborsclassifier__weights": ["uniform", "distance"]}, cv=10)
grid.fit(X_tr, y_tr)
print("best:", grid.best_params_, f"CV={grid.best_score_:.3f}")
print(f"test accuracy of the chosen model: {grid.score(X_te, y_te):.3f}")
```

```text
raw           10-fold CV accuracy: 0.944
standardized  10-fold CV accuracy: 0.972
best: {'kneighborsclassifier__n_neighbors': 9, 'kneighborsclassifier__weights': 'uniform'} CV=0.974
test accuracy of the chosen model: 0.951
```

(Python 3.12, scikit-learn 1.9.) Standardization is placed in a `Pipeline`, so that in each fold of the cross-validation the mean and standard deviation are estimated from the training part only. The cross-validation accuracy of the selected configuration ($0.974$) is slightly higher than its accuracy on the test set ($0.951$); this is exactly the optimistic bias from "selecting the best result" discussed in [4.6.2](/4.6.2#sec-2.2.2), together with random fluctuation on the test set.

## 4.3. The Curse of Dimensionality

$k$-nearest neighbors relies on one assumption: near examples are similar. In high-dimensional spaces, even "near" becomes questionable.

**Definition 4.3.1 (Curse of Dimensionality)** As the dimension $d$ of the space increases, the number of examples needed to cover the space grows exponentially, a fixed number of examples becomes extremely sparse, distances between points tend to become equal, and methods that rely on local neighborhoods or distances fail accordingly. These phenomena are collectively called the **curse of dimensionality**.

Some quantitative examples (suppose the data are uniformly distributed in the unit hypercube $[0,1]^d$):

- Neighborhoods are no longer local. To enclose a fraction $r$ of all the data in a small cube, its edge length must be $e_d(r) = r^{1/d}$. For $d = 10$, enclosing $10\%$ of the data requires an edge length of $0.1^{1/10} \approx 0.80$, that is, every coordinate must cover $80\%$ of its range; such a "neighborhood" is no longer local.
- Examples all lie near the boundary. The fraction of the volume of the unit ball in the thin shell of radius greater than $1 - \varepsilon$ is $1 - (1-\varepsilon)^d$, which already exceeds $99\%$ for $d = 100$ and $\varepsilon = 0.05$.
- Distances concentrate. Under fairly general conditions, as $d \to \infty$ the ratio of the distance from a query point to the farthest point to the distance to the nearest point tends to $1$ (Beyer et al., 1999): the nearest neighbor is not much nearer than the other points.
- To keep the same sampling density, the number of examples needed grows exponentially with $d$: the density reached by $100$ points in one dimension requires $100^{10}$ points in ten dimensions.

![Left: the edge length r^(1/d) of the small cube needed to enclose a fraction r of the data in the d-dimensional unit cube. Right: the relative gap between the farthest and the nearest distance from a random query point to 1000 uniformly random points, which rapidly tends to 0 as the dimension grows](./plots/curse-of-dimensionality.py)

The consequences for $k$-nearest neighbors are: the more irrelevant attributes there are, the weaker the meaning of the nearest neighbor; the same error rate needs exponentially more training examples; and the k-d tree of Sec. 4.4 also loses its speedup in high dimensions. The remedy is to reduce the effective dimension: feature selection and attribute weighting (Sec. 4.2.4), dimensionality reduction such as **principal component analysis** ([3.4.5](/3.4.5)), or learning a low-dimensional representation (an embedding) with a neural network and then finding neighbors in the embedding space. The difficulty with real data is usually not as severe as with uniform distributions: data such as images and text, although of very high dimension, often concentrate near a low-dimensional structure (low intrinsic dimension), which is why neighbor-based methods remain effective in practice.

## 4.4. Efficient Nearest Neighbor Search

$k$-nearest neighbors postpones all computation until query time: the naive approach computes, for each query, the distances to all $n$ training examples, at a cost of $O(np)$. When there are many training examples and queries are frequent, this is the main bottleneck. The idea for speeding it up is to check nearby points first and to skip points that cannot be closer than the nearest point found so far.

### 4.4.1. The k-d Tree

The **k-d tree** ([4.3.7](/4.3.7)) recursively partitions the space with hyperplanes perpendicular to the coordinate axes, each node corresponding to an axis-parallel rectangular region. When used for neighbor search, several choices in the construction are usually made heuristically:

- Which dimension to split along: the dimension with the widest range of values (cycling through the dimensions, as in [4.3.7](/4.3.7), also works).
- Where to split: at the median of that dimension. The median rather than the mean is used so that both sides contain the same number of points, the tree stays balanced, and the split is not affected by outliers.
- When to stop: when fewer than $m$ points remain in the region (for example $m = 8$), or the width of the region reaches a lower limit. Each leaf node stores a list of points; each node can also store a tight bounding box of all points beneath it, for more effective pruning.

**Algorithm 4.4.1 (Nearest Neighbor Query in a k-d Tree)** The input is a k-d tree and a query point $q$; maintain the nearest point found so far and its distance $d_{\mathrm{best}}$ (initially $+\infty$). Starting from the root:

1. At an internal node, first recurse into the subtree on the side containing $q$.
2. On reaching a leaf, compute the distance from $q$ to each point in it, and update the nearest point and $d_{\mathrm{best}}$ if necessary.
3. When backtracking, examine the other side of each visited node: if the distance from $q$ to the splitting hyperplane (or to the bounding box of that subtree) is not less than $d_{\mathrm{best}}$, there cannot be a closer point on the other side and the entire subtree is pruned; otherwise the other side must also be searched.

The query for $k$ nearest neighbors is the same, except that the $k$ nearest points are maintained (with a max-heap of size $k$) and the largest distance among them serves as the pruning bound. The implementation below uses this algorithm to answer exact nearest neighbor queries and counts how many distances are actually computed per query.

```python
import numpy as np

LEAF_SIZE = 8

def build(points, idx):
    """Split on the widest dimension at its median until a leaf holds <= LEAF_SIZE points."""
    if len(idx) <= LEAF_SIZE:
        return {"leaf": idx}
    p = points[idx]
    dim = int(np.argmax(p.max(axis=0) - p.min(axis=0)))
    order = idx[np.argsort(p[:, dim])]
    mid = len(order) // 2
    return {"dim": dim, "split": points[order[mid], dim],
            "left": build(points, order[:mid]), "right": build(points, order[mid:])}

def nearest(node, points, q, best):
    """Depth-first search; best = [squared distance, index, visited points]."""
    if "leaf" in node:
        d2 = ((points[node["leaf"]] - q) ** 2).sum(axis=1)
        best[2] += len(d2)
        j = int(np.argmin(d2))
        if d2[j] < best[0]:
            best[0], best[1] = float(d2[j]), int(node["leaf"][j])
        return
    gap = q[node["dim"]] - node["split"]
    near, far = (node["right"], node["left"]) if gap >= 0 else (node["left"], node["right"])
    nearest(near, points, q, best)                    # first the side containing q
    if gap * gap < best[0]:                           # the far side can still hold a closer point
        nearest(far, points, q, best)

rng = np.random.default_rng(0)
n = 20_000
for d in [2, 5, 10, 20]:
    points = rng.random((n, d))
    tree = build(points, np.arange(n))
    visited = []
    for q in rng.random((200, d)):
        best = [np.inf, -1, 0]
        nearest(tree, points, q, best)
        assert best[1] == int(np.argmin(((points - q) ** 2).sum(axis=1)))   # exact answer
        visited.append(best[2])
    print(f"d={d:2}: distance computations per query = {np.mean(visited):7.0f} of {n}")
```

```text
d= 2: distance computations per query =      10 of 20000
d= 5: distance computations per query =     119 of 20000
d=10: distance computations per query =    3642 of 20000
d=20: distance computations per query =   19977 of 20000
```

(Python 3.12, NumPy 2.5.) In low dimensions each query needs to compute only about a dozen distances, of the same order as $\log n$ (Friedman, Bentley and Finkel, 1977); at $d = 10$ nearly a fifth of the points must already be checked, and at $d = 20$ almost all points are checked, which is slower than brute-force search (because of the overhead of traversing the tree). This is a direct manifestation of the curse of dimensionality: in high dimensions the ball of radius $d_{\mathrm{best}}$ around the query point intersects almost all regions, and pruning fails. Empirically, k-d trees are effective only when $n \gg 2^d$. A k-d tree takes $O(n)$ space and $O(n \log n)$ time to build. Ball trees, which use hyperspheres instead of rectangles, perform somewhat better in moderate dimensions; the default `algorithm="auto"` of scikit-learn's `KNeighborsClassifier` chooses among brute force, k-d tree and ball tree according to the dimension and size of the data.

### 4.4.2. Approximate Nearest Neighbors

In high dimensions, exact nearest neighbor search is hard to make much faster than brute force; yet in applications such as image retrieval, recommendation and retrieval-augmented large language models, the data are embedding vectors of hundreds to thousands of dimensions produced by neural networks, at scales of hundreds of millions or even billions. These applications do not need the strict nearest neighbor; finding sufficiently near points is enough.

**Definition 4.4.1 (Approximate Nearest Neighbor)** Let $p^*$ be the nearest neighbor of a query $q$ and $\varepsilon > 0$. If the returned point $p$ satisfies $d(q, p) \le (1 + \varepsilon)\,d(q, p^*)$, then $p$ is called a $(1+\varepsilon)$-**approximate nearest neighbor** of $q$. Neighbor search that relaxes exactness in exchange for query speed is called approximate nearest neighbor search.

In practice a more common quality measure is recall: how many of the $k$ returned points are the true $k$ nearest neighbors. Various methods trade off among recall, queries per second and memory. The main families of methods:

| Method | Idea | Representatives |
|---|---|---|
| Locality-sensitive hashing (LSH) | Design a family of hash functions such that nearby points fall into the same bucket with high probability; search only in the bucket of the query point | Indyk and Motwani (1998); has theoretical guarantees |
| Graph indexes | Connect each point to several of its neighbors in a graph; at query time start from an entry point and greedily walk toward nearer points | HNSW (hierarchical navigable small world graphs, Malkov and Yashunin, 2016); DiskANN for disks; CAGRA for GPUs |
| Inverted files and quantization | First cluster the vectors into several clusters with k-means and search only the nearest few clusters at query time (IVF); then compress each vector into a few dozen bytes with product quantization (PQ) and approximate distances by table lookup | Product quantization of Jégou et al. (2011); IVF-PQ |

FAISS (an open-source library from Meta) is the most commonly used implementation; it provides exact search, IVF, PQ, HNSW and other indexes on CPU and GPU, which can be combined, and its GPU indexes have integrated NVIDIA's cuVS library. When the scale is moderate and memory is sufficient, HNSW is usually the first choice for balancing recall and speed, and hnswlib and many vector databases (as well as the pgvector extension of PostgreSQL) use it as the default index; when the data exceed memory, compressed indexes such as IVF-PQ, or DiskANN, are used. For comparisons of different methods and parameters, see the public ANN-Benchmarks.

## 4.5. Distance-Weighted k-Nearest Neighbors and Kernel Regression

In $k$-nearest neighbors, the $k$ neighbors have equal votes, however far they are from the query point. It is more reasonable to let nearer neighbors contribute more.

**Definition 4.5.1 (Distance-Weighted k-Nearest Neighbors and Kernel Regression)** Take a nonnegative function $K$ that decreases with distance and let the weights be $w_i = K\bigl(d(\boldsymbol{x}_i, \boldsymbol{x}_q)\bigr)$. A weighted vote over the $k$ neighbors of $\boldsymbol{x}_q$ (classification) or the weighted average

$$
\hat y_q = \frac{\sum_i w_i\, y_i}{\sum_i w_i}
$$
(regression) is called **distance-weighted k-nearest neighbors**. When the sums run over all training examples, the regression form is called Nadaraya–Watson **kernel regression**, and $K$ is called the kernel function.

Commonly used weights are $1/d^2$, $\mathrm{e}^{-d}$, $1/(1+d)$, and the Gaussian kernel $w_i = \exp\bigl(-d(\boldsymbol{x}_i, \boldsymbol{x}_q)^2 / K_w^2\bigr)$, where $K_w$ is the kernel width. The weight $1/d^2$ is undefined at $d = 0$: when the query point coincides with a training example, output its value directly, or use $1/(d_0 + d)^2$ instead. After weighting, using all examples (rather than only $k$) is no longer a problem, because the weights of distant examples are almost zero; the role of $k$ is then taken over by the kernel width $K_w$.

The kernel width is very important. If $K_w$ is too small, the estimate depends only on the nearest one or two points, and the curve jitters and fits the noise; if $K_w$ is too large, the estimate approaches the average of all examples and erases the real variation. Choosing a suitable $K_w$ is crucial for all locally weighted learners, and it is usually selected by cross-validation. Kernel regression shares the idea of kernel functions and bandwidth with kernel density estimation in statistics ([3.2.3](/3.2.3)).

## 4.6. Locally Weighted Regression

Kernel regression fits the data with a weighted constant at each query point. Replacing the constant by a linear function gives locally weighted regression: it is regression because it estimates a real-valued target function; local because the estimate depends only on the data near the query point; and weighted because the contribution of each example is determined by its distance to the query point.

**Definition 4.6.1 (Locally Weighted Regression)** For a query point $\boldsymbol{x}_q$, write $\tilde{\boldsymbol{x}} = (1, \boldsymbol{x}^{\mathsf T})^{\mathsf T}$, take weights $w_i = K\bigl(d(\boldsymbol{x}_i, \boldsymbol{x}_q)\bigr)$ (such as $\exp(-d^2/K_w^2)$), and solve

$$
\hat{\boldsymbol{\beta}}(\boldsymbol{x}_q) = \arg\min_{\boldsymbol{\beta}}\ \sum_{i=1}^n w_i\,\bigl(y_i - \boldsymbol{\beta}^{\mathsf T}\tilde{\boldsymbol{x}}_i\bigr)^2,
$$
then predict $\hat y_q = \hat{\boldsymbol{\beta}}(\boldsymbol{x}_q)^{\mathsf T}\tilde{\boldsymbol{x}}_q$. This method is called **locally weighted regression**.

Every query point requires solving a **weighted least squares** problem: let the $i$-th row of $\tilde X$ be $\tilde{\boldsymbol{x}}_i^{\mathsf T}$ and $W = \operatorname{diag}(w_1, \dots, w_n)$; then $\hat{\boldsymbol{\beta}}(\boldsymbol{x}_q) = (\tilde X^{\mathsf T}W\tilde X)^{-1}\tilde X^{\mathsf T}W\boldsymbol{y}$. The main benefit of local linear fitting appears at the boundary of the data and where the slope is large: at the boundary, kernel regression can only average points on one side, so the estimate is pulled toward the interior, whereas local linear fitting can extrapolate along the slope. LOESS / LOWESS in statistics (Cleveland, 1979) is locally weighted linear or quadratic regression; it uses tricube weights and a fixed fraction of neighbors (the span) in place of a fixed kernel width ([3.3.12](/3.3.12)).

![Three instance-based regressions on the same noisy sample: k-nearest neighbor averaging (k = 1 fits the noise, k = 9 is step-like), kernel regression (jittery for small K_w, too smooth and biased at both ends for large K_w), and locally weighted linear regression (smooth with smaller bias at both ends)](./plots/local-regression.py)

The figure above compares the algorithms on a concrete example: global linear regression has a large bias when the function is clearly nonlinear; 1-NN amounts to connecting all the points and fits the noise; the neighbor average with $k = 9$ smooths the noise but is not differentiable and is step-like; kernel regression gives a smooth curve but is sensitive to the kernel width; and locally weighted regression, with a suitable kernel width, is both smooth and better at capturing the trends at both ends.

## 4.7. The Four Elements of Instance-Based Learners

An instance-based (memory-based) learner is determined by four choices:

| Learner | Distance measure | Number of neighbors | Weighting function | How neighbors are used |
|---|---|---|---|---|
| 1-NN | Euclidean distance | 1 | None | Take the neighbor's output |
| $k$-NN | Euclidean distance | $k$ | None | Vote or average |
| Distance-weighted $k$-NN / kernel regression | Scaled Euclidean distance | All or $k$ | $\exp(-d^2/K_w^2)$, etc. | Weighted average |
| Locally weighted regression | Scaled Euclidean distance | All or $k$ | $\exp(-d^2/K_w^2)$, etc. | Fit a local linear model |

The advantages of instance-based methods are: the concept is simple, yet they can approximate arbitrarily complex target functions (such as image classification); averaging over $k$ neighbors makes them fairly robust to noise; predictions can be explained ("because it is similar to these examples"); the information in the training examples is not lost, and no retraining is needed when new data arrive; there are almost no parameters besides $k$ or the kernel width; and leave-one-out cross-validation is almost free.

The disadvantages are: all training examples must be stored, with memory cost $O(np)$; neighbors must be searched at query time, which is computationally expensive, so in the early days these methods were mostly used offline; it is hard to determine a suitable distance function, especially when examples are represented by complex symbolic structures; and irrelevant attributes seriously affect the distance (Sec. 4.2.4, Sec. 4.3).

Today the first two disadvantages are greatly alleviated by approximate nearest neighbor search (Sec. 4.4.2), and the last two are addressed by representation learning: a neural network first maps images, text, users and items to embedding vectors, in the embedding space distances acquire semantics, and neighbor retrieval is then performed on top of it. Image search, the recall stage of recommender systems and retrieval-augmented large language models all work this way; kNN-LM (Khandelwal et al., 2020), which interpolates $k$-nearest neighbor retrieval with the output of a language model, also follows this line. Instance-based learning has therefore not become obsolete but has become a basic component of large-scale systems.

## Summary

- Instance-based learning stores examples, postpones computation, and predicts locally from the examples similar to the query; it is nonparametric lazy learning.
- The decision regions of 1-NN form the Voronoi diagram; its asymptotic error rate is at most twice the Bayes error rate (Cover–Hart).
- Design of $k$-nearest neighbors: the distance (Minkowski, Mahalanobis, cosine, and so on); attributes must be normalized and preferably weighted by relevance; $k$ is selected by cross-validation and controls the bias–variance trade-off.
- Curse of dimensionality: in high dimensions neighborhoods are no longer local and distances concentrate; dimensionality reduction, feature selection or learned embeddings are needed.
- The k-d tree reduces queries to logarithmic cost in low dimensions and fails in high dimensions; large-scale high-dimensional retrieval uses approximate nearest neighbors (LSH, HNSW, IVF-PQ, libraries such as FAISS).
- Distance-weighted $k$-nearest neighbors, kernel regression and locally weighted regression extend "nearer examples matter more" to regression; the kernel width is the most critical hyperparameter.
