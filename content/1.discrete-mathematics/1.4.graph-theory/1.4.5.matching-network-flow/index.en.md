---
title: Matching and Network Flow
source_hash: 7690bc3c1f06
---

Matching problems and network flow problems are two classes of graph-theoretic problems with rich practical backgrounds: the former include job assignment and marriage problems, the latter the transportation of goods and the routing of communication traffic. In this chapter we first discuss maximum matchings in bipartite graphs, complete matchings (Hall's theorem) and optimal matchings; we then treat maximum flows in networks, the max-flow min-cut theorem and the algorithms based on it; and finally we explain the connection between the two classes of problems.

## 5.1. Maximum Matchings in Bipartite Graphs

### 5.1.1. Basic Notions of Matching

**Definition 5.1.1 (Matching)** Let $M$ be a set of edges of a graph $G$. If no two edges of $M$ share a vertex, then $M$ is called a **matching** in $G$. The vertices incident with edges of $M$ are said to be **saturated** (by $M$), and the remaining vertices are **unsaturated**.

**Definition 5.1.2 (Maximum Matching)** A matching $M$ in a graph $G = (V, E)$ is called a **maximum matching** of $G$ if $|M| \ge |M'|$ for every matching $M'$ in $G$.

**Definition 5.1.3 (Alternating Path)** Given a matching $M$ in $G$, a path in $G$ whose edges alternately belong and do not belong to $M$ is called an **alternating path** (with respect to $M$).

**Definition 5.1.4 (Augmenting Path)** Let $P$ be an alternating path in $G$ with respect to a matching $M$. If both ends of $P$ are unsaturated by $M$, then $P$ is called an **augmenting path**. In this case neither end edge of $P$ belongs to $M$, the set $M' = M \oplus P$ (the symmetric difference of $M$ and the edge set of $P$) is again a matching in $G$, and $|M'| = |M| + 1$.

### 5.1.2. A Characterization of Maximum Matchings

**Theorem 5.1.1 (Berge's Theorem)** A matching $M$ in $G$ is a maximum matching if and only if $G$ has no augmenting path with respect to $M$.

**Proof** Necessity: if there were an augmenting path $P$, then $M \oplus P$ would be a larger matching, a contradiction.

Sufficiency: suppose there is no augmenting path but $M$ is not a maximum matching, and take a maximum matching $M'$, so $|M'| > |M|$. Consider the subgraph $G'$ formed by the edge set $M' \oplus M$. Each vertex of $G'$ is incident with at most one edge of $M$ and at most one edge of $M'$, so its degree is at most $2$. Hence every connected component of $G'$ is either a cycle of even length whose edges alternate between $M$ and $M'$ (with equally many edges of each), or a path whose edges alternate between $M$ and $M'$. Since $|M'| > |M|$, some path component has more edges of $M'$ than of $M$; both of its end edges belong to $M'$, and both of its ends are unsaturated by $M$. This is an augmenting path with respect to $M$, a contradiction. $\square$

Theorem 5.1.1 is known as *Berge's theorem*. It holds for all graphs and underlies all maximum matching algorithms.

### 5.1.3. The Hungarian Algorithm

The *Hungarian algorithm* is the classical algorithm for maximum matchings in **bipartite graphs**. Starting from some initial matching, it repeatedly looks for augmenting paths to enlarge the matching. The algorithm marks the vertices of $X$ with three labels: $0$ for an unsaturated vertex not yet searched, $1$ for a saturated vertex, and $2$ for an unsaturated vertex from which it has been established that no augmenting path starts.

**Algorithm 5.1.1 (Hungarian Algorithm)** Input: a bipartite graph $G = (X, Y, E)$ and an initial matching $M$ (possibly empty). Output: a maximum matching $M$.

1. Label every saturated vertex of $X$ with $1$ and all others with $0$.
2. If every vertex of $X$ has a nonzero label, $M$ is a maximum matching; stop. Otherwise choose a vertex $x_0 \in X$ labeled $0$.
3. Set $X_0 \leftarrow \{x_0\}$ and $Y_0 \leftarrow \varnothing$.
4. If $\Gamma(X_0) \subseteq Y_0$, there is no augmenting path starting at $x_0$; label $x_0$ with $2$ and go to step 2. Otherwise choose any $y \in \Gamma(X_0) - Y_0$:
   - if $y$ is saturated, say $(y, z) \in M$, set $X_0 \leftarrow X_0 \cup \{z\}$ and $Y_0 \leftarrow Y_0 \cup \{y\}$, and go to step 4;
   - if $y$ is unsaturated, an augmenting path $P$ from $x_0$ to $y$ has been found; set $M \leftarrow M \oplus P$, label $x_0$ with $1$, and go to step 2.

## 5.2. Complete Matchings

### 5.2.1. Definition and Hall's Theorem

**Definition 5.2.1 (Complete Matching)** Let $M$ be a matching in a **bipartite graph** $G = (X, Y, E)$. If $|M| = |X|$, that is, every vertex of $X$ is saturated, then $M$ is called a **complete matching** from $X$ to $Y$. If $|M| = |X| = |Y|$, then $M$ is called a **perfect matching**.

For $A \subseteq X$, let $\Gamma(A)$ denote the set of all neighbors of vertices in $A$, that is, the union of their **neighborhoods**.

**Theorem 5.2.1 (Hall's Theorem)** A bipartite graph $G = (X, Y, E)$ has a complete matching from $X$ to $Y$ if and only if $|\Gamma(A)| \ge |A|$ for every subset $A$ of $X$.

**Proof** Necessity: if there is a complete matching, the vertices of $A$ are matched to $|A|$ distinct vertices of $Y$, all of which belong to $\Gamma(A)$; hence $|\Gamma(A)| \ge |A|$.

Sufficiency: suppose the condition holds but there is no complete matching. Take a maximum matching $M$; then $X$ contains an unsaturated vertex $x_0$. Let $Z$ be the set of all vertices reachable from $x_0$ by alternating paths with respect to $M$ (including $x_0$), and let $X' = Z \cap X$ and $Y' = Z \cap Y$. Since $M$ is a maximum matching, Theorem 5.1.1 shows that there is no augmenting path, so every vertex of $Y'$ is saturated and its partner in $M$ belongs to $X' - \{x_0\}$; conversely, every vertex of $X' - \{x_0\}$ is reached from $Y'$ along an edge of $M$. Hence $|Y'| = |X'| - 1$. Moreover, every neighbor of a vertex in $X'$ is reachable by an alternating path, so $\Gamma(X') = Y'$ and $|\Gamma(X')| = |X'| - 1 < |X'|$, contradicting the condition. $\square$

*Hall's marriage theorem*, as Hall's theorem is also called, has the following interpretation: think of $X$ as a group of people and $Y$ as the available partners, with $x$ adjacent to $y$ meaning that $x$ is willing to choose $y$. Everyone can be given a distinct partner if and only if, for every $k$, any $k$ people are together willing to choose at least $k$ partners.

**Corollary 5.2.1** Let $k \ge 1$. If in a bipartite graph $G = (X, Y, E)$ every vertex $x \in X$ has $d(x) \ge k$ and every vertex $y \in Y$ has $d(y) \le k$, then there is a complete matching from $X$ to $Y$.

**Proof** For any $A \subseteq X$, at least $k|A|$ edges are incident with $A$, and their other endpoints all lie in $\Gamma(A)$. Each vertex of $\Gamma(A)$ is incident with at most $k$ edges, so $k|\Gamma(A)| \ge k|A|$, that is, $|\Gamma(A)| \ge |A|$. The claim follows from Hall's theorem. $\square$

### 5.2.2. Maximum Matchings and Minimum Covers

Let $A$ be the adjacency matrix of a bipartite graph $G = (X, Y, E)$, with $|X|$ rows and $|Y|$ columns and $a_{ij} = 1$ if and only if $x_i$ is adjacent to $y_j$. A matching corresponds to a set of nonzero entries of $A$ lying in distinct rows and distinct columns, so the number of edges $r$ of a maximum matching is the maximum number of nonzero entries of $A$ in distinct rows and distinct columns.

**Definition 5.2.2 (Minimum Cover Number)** If some rows and columns of a matrix $A$ are chosen so that every nonzero entry of $A$ lies in one of the chosen rows or columns, we say that these rows and columns cover the nonzero entries of $A$. The minimum total number of rows and columns in such a cover is called the **minimum cover number** of $A$, denoted $s$.

Rows correspond to vertices of $X$, columns to vertices of $Y$, and nonzero entries to edges, so $s$ is also the minimum number of vertices that must be chosen so that every edge of $G$ has at least one chosen endpoint.

**Theorem 5.2.3 (König's Theorem)** Let $r$ be the number of edges of a maximum matching of a bipartite graph $G$, and $s$ the minimum cover number of its adjacency matrix. Then $r = s$.

**Proof** $s \ge r$: each row or column covers at most one of the $r$ nonzero entries lying in distinct rows and distinct columns, so at least $r$ rows and columns are needed to cover them.

$r \ge s$: let a minimum cover consist of $c$ rows and $d$ columns, $s = c + d$, with the rows corresponding to $X_c \subseteq X$ and the columns to $Y_d \subseteq Y$. For every $S \subseteq X_c$, the set $S$ has at least $|S|$ neighbors in $Y - Y_d$; otherwise, replacing the rows of $S$ in the cover by the columns of these neighbors would still give a cover, with fewer rows and columns, contradicting minimality. By Hall's theorem there is a matching between $X_c$ and $Y - Y_d$ that saturates $X_c$, of size $c$. Similarly, there is a matching of size $d$ between $Y_d$ and $X - X_c$. These two matchings use disjoint sets of vertices, and together they form a matching of $G$ of size $c + d = s$; hence $r \ge s$. $\square$

In the language of graphs, *König's theorem* states that in a bipartite graph the number of edges of a maximum matching equals the minimum number of vertices needed to cover all edges.

## 5.3. Optimal Matchings and Their Algorithms

**Definition 5.3.1 (Optimal Matching)** Suppose every edge of a bipartite graph $G$ has a weight. Among all complete matchings of $G$, one with maximum (or minimum) total weight is called an **optimal matching**.

### 5.3.1. The Maximum Weight Matching Algorithm (Kuhn–Munkres Algorithm)

The problem considered here is the following: given an $n \times n$ profit matrix $C = (c_{ij})$, find a permutation $\pi$ of $\{1, \dots, n\}$ maximizing $\sum_i c_{i, \pi(i)}$. This amounts to finding a perfect matching of maximum total weight in the complete bipartite graph $K_{n,n}$, where the edge $(x_i, y_j)$ has weight $c_{ij}$.

**Algorithm 5.3.1 (Kuhn–Munkres Algorithm)**

1. Initialization: set $l(x_i) = \max_j c_{ij}$ and $l(y_j) = 0$, and form the matrix $B = (b_{ij})$ with $b_{ij} = l(x_i) + l(y_j) - c_{ij} \ge 0$.
2. Find a minimum cover of the zero entries of $B$, and let $r$ be its size. If $r = n$, then $B$ has $n$ zero entries in distinct rows and distinct columns, and the corresponding matching is a maximum weight matching, with total weight $\sum_i l(x_i) + \sum_j l(y_j)$; stop. Otherwise let $\delta$ be the smallest uncovered entry; set $b_{ij} \leftarrow b_{ij} + \delta$ for entries whose row and column are both covered, $b_{ij} \leftarrow b_{ij} - \delta$ for uncovered entries, and leave all other entries unchanged.
3. Update the labels accordingly: if the row of $x_i$ is uncovered, set $l(x_i) \leftarrow l(x_i) - \delta$; if the column of $y_j$ is covered, set $l(y_j) \leftarrow l(y_j) + \delta$. Clear the cover and go to step 2.

**Theorem 5.3.1** The matching produced by the Kuhn–Munkres algorithm is a maximum weight matching.

**Proof** The algorithm maintains $b_{ij} = l(x_i) + l(y_j) - c_{ij} \ge 0$, that is, $l(x_i) + l(y_j) \ge c_{ij}$. Hence every perfect matching $\pi$ satisfies

$$
\sum_i c_{i, \pi(i)} \le \sum_i l(x_i) + \sum_j l(y_j).
$$

At termination, the matching corresponding to the $n$ zero entries of $B$ in distinct rows and distinct columns attains equality, so its total weight is maximal. Moreover, each update decreases $\sum_i l(x_i) + \sum_j l(y_j)$ by $\delta(n - r) > 0$; when the $c_{ij}$ are integers, every $\delta$ is a positive integer, and since this sum is bounded below, the algorithm terminates after finitely many steps. $\square$

To find a minimum weight matching, replace $c_{ij}$ by $K - c_{ij}$ (with $K$ a sufficiently large constant) and find a maximum weight matching; alternatively, modify the algorithm directly, using the row minima as initial labels and adjusting the signs accordingly.

## 5.4. Maximum Cardinality Matching

The maximum cardinality matching problem asks for a matching with as many edges as possible in a general graph (not necessarily bipartite). A general graph may contain cycles of odd length, so the Hungarian algorithm cannot be applied directly. Edmonds' blossom algorithm (1965) shrinks odd cycles (called blossoms) and, still based on the search for augmenting paths, finds a maximum matching of a general graph in polynomial time.

## 5.5. Flow Networks

### 5.5.1. Definition of a Flow Network

**Definition 5.5.1 (Flow Network)** A **flow network** $N$ is a connected directed graph without loops such that:

- there is exactly one vertex $s$ of in-degree zero, called the **source**;
- there is exactly one vertex $t$ of out-degree zero, called the **sink**;
- each edge $(i, j)$ has a nonnegative real weight $c_{ij}$, called the **capacity** of the edge; if there is no edge between $i$ and $j$, we set $c_{ij} = 0$.

### 5.5.2. Feasible Flows and Maximum Flows

In a flow network $N$, assign to each edge $(i, j)$ a nonnegative real number $f_{ij}$, called the flow on that edge. If $\{f_{ij}\}$ satisfies

1. the capacity constraints: $0 \le f_{ij} \le c_{ij}$;
2. flow conservation: $\sum_j f_{ij} = \sum_k f_{ki}$ for all $i \ne s, t$;
3. equal flow at source and sink: $\sum_j f_{sj} = \sum_k f_{kt} = W$,

then $\{f_{ij}\}$ is called a *feasible flow* on $N$, that is, a *network flow*, and $W$ is called its value. A feasible flow of maximum value is called a *maximum flow*.

### 5.5.3. Cuts and Their Capacities

**Definition 5.5.2 (Cut)** Let $S$ be a subset of the vertex set $V$ with $s \in S$ and $t \in \overline{S} = V - S$. The set of all directed edges $(i, j)$ from $S$ to $\overline{S}$ ($i \in S$, $j \in \overline{S}$) is called an **s–t cut** of $N$, written $(S, \overline{S})$; its capacity is

$$
C(S, \overline{S}) = \sum_{(i, j) \in (S, \overline{S})} c_{ij}.
$$

**Theorem 5.5.1** The maximum flow value of a network does not exceed the minimum capacity of a cut:

$$
\max W \le \min C(S, \overline{S}).
$$

**Proof** For any feasible flow $f$ and any cut $(S, \overline{S})$, add the outflow $W$ of $s$ to the conservation equations of the other vertices of $S$. The flows on edges inside $S$ cancel, and we obtain the net flow across the cut:

$$
W = \sum_{i \in S,\, j \in \overline{S}} (f_{ij} - f_{ji}) \le \sum_{i \in S,\, j \in \overline{S}} f_{ij} \le \sum_{i \in S,\, j \in \overline{S}} c_{ij} = C(S, \overline{S}).
$$

Since $f$ and the cut are arbitrary, the claim follows. $\square$

**Theorem 5.5.2 (Max-Flow Min-Cut Theorem)** The maximum flow value of a network equals the minimum capacity of a cut:

$$
\max W = \min C(S, \overline{S}).
$$

**Proof** Let $f$ be a maximum flow, and define $S$ as follows: $s \in S$; if $x \in S$ and either $(x, y)$ is an unsaturated edge ($f_{xy} < c_{xy}$) or $(y, x)$ is an edge with positive flow ($f_{yx} > 0$), then $y \in S$. If $t \in S$, there would be a flow augmenting path from $s$ to $t$ (see Definition 5.6.1) along which the flow could be increased, contradicting the maximality of $f$; so $t \notin S$ and $(S, \overline{S})$ is a cut. By the construction of $S$, for all $x \in S$ and $y \in \overline{S}$ we have $f_{xy} = c_{xy}$ and $f_{yx} = 0$. Therefore

$$
W = \sum_{i \in S,\, j \in \overline{S}} (f_{ij} - f_{ji}) = \sum_{i \in S,\, j \in \overline{S}} c_{ij} = C(S, \overline{S}).
$$

Together with Theorem 5.5.1 this gives equality, and this $(S, \overline{S})$ is a minimum cut. $\square$

The *max-flow min-cut theorem* was proved by Ford and Fulkerson in 1956. Its proof also gives a method for finding a maximum flow: as long as a flow augmenting path exists, augment the flow along it; when no flow augmenting path remains, the current flow is maximum.

## 5.6. The Ford–Fulkerson Labeling Algorithm for Maximum Flow

The Ford–Fulkerson algorithm is based on the idea of flow augmenting paths and consists of two parts: a labeling procedure and an augmentation procedure.

### 5.6.1. Flow Augmenting Paths

**Definition 5.6.1 (Flow Augmenting Path)** Let $f$ be a feasible flow on a flow network $N$, and let $P$ be a path from $s$ to $t$ (ignoring the directions of edges). The edges of $P$ directed along $P$ are called **forward edges**, and those directed against it **backward edges**; their sets are denoted $P^+$ and $P^-$. If every forward edge satisfies $f_{ij} < c_{ij}$ and every backward edge satisfies $f_{ij} > 0$, then $P$ is called a **flow augmenting path** with respect to $f$.

The amount by which the flow can be increased along $P$ is

$$
\delta = \min\left\{ \min_{(i, j) \in P^+} (c_{ij} - f_{ij}),\ \min_{(i, j) \in P^-} f_{ij} \right\} > 0:
$$

increasing the flow on every forward edge by $\delta$ and decreasing the flow on every backward edge by $\delta$ gives another feasible flow, whose value is larger by $\delta$.

### 5.6.2. Description of the Algorithm

The algorithm labels vertices with pairs $(u^\pm, \delta_v)$: $u$ indicates that the label comes from vertex $u$, the superscript $+$ that it was obtained via a forward edge $(u, v)$, the superscript $-$ that it was obtained via a backward edge $(v, u)$, and $\delta_v$ is the amount by which the flow from $s$ to $v$ can currently be increased.

**Algorithm 5.6.1 (Ford–Fulkerson Labeling Algorithm)** Input: a flow network $N$ and an initial feasible flow $f$ (usually the zero flow). Output: a maximum flow $f$.

Labeling procedure:

1. Label $s$ with $(-, \infty)$.
2. Choose any labeled vertex $u$, and for each unlabeled vertex $v$:
   - if $(u, v)$ is an edge with $f(u, v) < c(u, v)$, label $v$ with $(u^+, \delta_v)$, where $\delta_v = \min\{\delta_u,\ c(u, v) - f(u, v)\}$;
   - if $(v, u)$ is an edge with $f(v, u) > 0$, label $v$ with $(u^-, \delta_v)$, where $\delta_v = \min\{\delta_u,\ f(v, u)\}$.
3. If $t$ has been labeled, go to the augmentation procedure; otherwise repeat step 2. If no further vertex can be labeled, the current flow is maximum; stop.

Augmentation procedure:

4. Set $v \leftarrow t$ and $\delta \leftarrow \delta_t$.
5. If the label of $v$ is $(u^+, \delta_v)$, set $f(u, v) \leftarrow f(u, v) + \delta$; if the label of $v$ is $(u^-, \delta_v)$, set $f(v, u) \leftarrow f(v, u) - \delta$.
6. If $u = s$, erase all labels and go to step 1; otherwise set $v \leftarrow u$ and go to step 5.

At termination, the set of labeled vertices is exactly the set $S$ in the proof of Theorem 5.5.2, and $(S, \overline{S})$ is a minimum cut.

### 5.6.3. Complexity

The number of steps of the Ford–Fulkerson algorithm depends on the capacities. If all capacities are integers, each augmentation increases the flow by at least $1$ and the algorithm terminates after finitely many steps, but the number of steps may be of the same order as the maximum flow value, which can be very large. If capacities are irrational, the algorithm may fail to terminate, and the flow value need not even converge to the maximum.

## 5.7. The Edmonds–Karp Algorithm for Maximum Flow

The Edmonds–Karp algorithm improves the Ford–Fulkerson algorithm by always choosing a shortest flow augmenting path (one with the fewest edges), which guarantees polynomial running time.

### 5.7.1. Description of the Algorithm

The algorithm is essentially the Ford–Fulkerson algorithm, except that the labeling procedure uses **breadth-first search**, that is, vertices are scanned in the order in which they were labeled ("first labeled, first scanned"). This guarantees that the flow augmenting path found from $s$ to $t$ has the fewest possible edges.

### 5.7.2. Complexity

**Theorem 5.7.1** If the Edmonds–Karp algorithm always augments along a currently shortest flow augmenting path, then the number of augmentations is at most $\frac{m(n+2)}{2}$, where $n = |V|$ and $m = |E|$.

**Proof** (sketch) Let $\lambda^k(u, v)$ be the length of a shortest path from $u$ to $v$ after the $k$-th augmentation, computed using only edges along which the flow can be increased (unsaturated forward edges and backward edges with positive flow). One can show that $\lambda^k(s, v)$ is nondecreasing in $k$. In each augmentation at least one edge becomes a bottleneck (it determines the increment $\delta$, and after the augmentation the flow can no longer be increased along it). Between two occasions on which the same edge becomes a bottleneck, the distance from $s$ to its endpoint increases by at least $2$; since distances do not exceed $n$, each edge becomes a bottleneck at most about $n/2 + 1$ times. Hence the total number of augmentations is at most $m(n/2 + 1) = \frac{m(n+2)}{2}$. $\square$

Each shortest flow augmenting path is found by breadth-first search in $O(m)$ time, so the Edmonds–Karp algorithm runs in $O(nm^2)$ time.

## 5.8. Minimum-Cost Flow

Suppose that, in addition, each edge $(i, j)$ of a flow network carries a cost $a_{ij} \ge 0$ per unit of flow. The *minimum-cost flow* problem asks, among all feasible flows of a given value $W$, for one minimizing the total cost $\sum a_{ij} f_{ij}$. A common method is to start from the zero flow and repeatedly augment along a flow augmenting path that is shortest with respect to cost (forward edges having length $a_{ij}$ and backward edges length $-a_{ij}$), until the flow value reaches $W$; augmenting all the way to a maximum flow gives a *minimum-cost maximum flow*.

## 5.9. The Connection Between Matching and Network Flow

The maximum matching problem for a **bipartite graph** can be transformed into a maximum flow problem: add a source $s$ and a sink $t$, add an edge of capacity $1$ from $s$ to each vertex of $X$ and from each vertex of $Y$ to $t$, and turn each edge of the bipartite graph into a directed edge of capacity $1$ from $X$ to $Y$. In an integral maximum flow, the original edges carrying flow $1$ form a maximum matching, and the maximum flow value equals the number of edges of a maximum matching. Similarly, by assigning costs to the edges, the optimal matching problem can be transformed into a minimum-cost maximum flow problem.
