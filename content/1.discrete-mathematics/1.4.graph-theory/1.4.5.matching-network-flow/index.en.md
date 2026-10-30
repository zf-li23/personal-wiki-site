---
title: Matching and Network Flow
source_hash: 43e171afa191
---

Matching problems and network flow problems are two classes of graph-theoretic problems with rich practical backgrounds: the former include job assignment and marriage problems, the latter the transportation of goods and the routing of communication traffic. In this chapter we first discuss maximum matchings in bipartite graphs, complete matchings (Hall's theorem) and optimal matchings; we then treat maximum flows in networks, the max-flow min-cut theorem and the algorithms based on it; and finally we explain the connection between the two classes of problems. Both rest on the same idea: improve the current solution along an "augmenting" path until no such path exists; when none exists, one can exhibit a dual quantity of the same value (a minimum cover of a bipartite graph, a minimum cut of a network), which proves optimality. Matchings in bipartite graphs can be phrased in terms of the **adjacency matrix** of [Chapter 1](/1.4.1), and flow conservation is a linear equation in the **incidence matrix**; Menger's theorem in [Chapter 6](/1.4.6) can also be derived from the max-flow min-cut theorem.

## 5.1. Maximum Matchings in Bipartite Graphs

### 5.1.1. Basic Notions of Matching

**Definition 5.1.1 (Matching)** Let $M$ be a set of edges of a graph $G$. If no two edges of $M$ share a vertex, then $M$ is called a **matching** in $G$. The vertices incident with edges of $M$ are said to be **saturated** (by $M$), and the remaining vertices are **unsaturated**.

**Definition 5.1.2 (Maximum Matching)** A matching $M$ in a graph $G = (V, E)$ is called a **maximum matching** of $G$ if $|M| \ge |M'|$ for every matching $M'$ in $G$.

**Definition 5.1.3 (Alternating Path)** Given a matching $M$ in $G$, a path in $G$ whose edges alternately belong and do not belong to $M$ is called an **alternating path** (with respect to $M$).

**Definition 5.1.4 (Augmenting Path)** Let $P$ be an alternating path in $G$ with respect to a matching $M$. If both ends of $P$ are unsaturated by $M$, then $P$ is called an **augmenting path**. In this case neither end edge of $P$ belongs to $M$, the set $M' = M \oplus P$ (the symmetric difference of $M$ and the edge set of $P$) is again a matching in $G$, and $|M'| = |M| + 1$.

**Example 5.1.1** Let $G = (X, Y, E)$ be the bipartite graph with $X = \{x_1, \dots, x_5\}$, $Y = \{y_1, \dots, y_5\}$ and neighborhoods

$$
\Gamma(x_1) = \{y_1, y_2\},\quad \Gamma(x_2) = \{y_1\},\quad \Gamma(x_3) = \{y_2, y_3, y_4, y_5\},\quad \Gamma(x_4) = \{y_3\},\quad \Gamma(x_5) = \{y_1\}.
$$

Take the matching $M = \{x_1y_1, x_3y_2\}$, which saturates $x_1, x_3, y_1, y_2$. Then $P = x_2y_1x_1y_2x_3y_3$ is an alternating path: $x_2y_1, x_1y_2, x_3y_3 \notin M$ and $y_1x_1, y_2x_3 \in M$. Both of its ends $x_2, y_3$ are unsaturated, so $P$ is an augmenting path, and $M \oplus P = \{x_2y_1, x_1y_2, x_3y_3\}$ has one edge more than $M$: the edges of $P$ that were in $M$ leave it, and the others enter.

![Example 5.1.1: a matching M (blue edges; unsaturated vertices grey); an augmenting path P (edges of M blue, the others red) whose ends x2, y3 are both unsaturated; M ⊕ P swaps the roles of the two kinds of edges on P and has one edge more](./plots/augmenting-path.py)

### 5.1.2. A Characterization of Maximum Matchings

**Theorem 5.1.1 (Berge's Theorem)** A matching $M$ in $G$ is a maximum matching if and only if $G$ has no augmenting path with respect to $M$.

**Proof** Necessity: if there were an augmenting path $P$, then $M \oplus P$ would be a larger matching, a contradiction.

Sufficiency: suppose there is no augmenting path but $M$ is not a maximum matching, and take a maximum matching $M'$, so $|M'| > |M|$. Consider the subgraph $G'$ formed by the edge set $M' \oplus M$. Each vertex of $G'$ is incident with at most one edge of $M$ and at most one edge of $M'$, so its degree is at most $2$. Hence every connected component of $G'$ is either a cycle of even length whose edges alternate between $M$ and $M'$ (with equally many edges of each), or a path whose edges alternate between $M$ and $M'$. Since $|M'| > |M|$, some path component has more edges of $M'$ than of $M$; both of its end edges belong to $M'$, and both of its ends are unsaturated by $M$. This is an augmenting path with respect to $M$, a contradiction. $\square$

![The proof of Berge's theorem: in the symmetric difference of two matchings M (blue) and M' (red) every vertex has degree at most 2, so its components are alternating even cycles and alternating paths; a path with more red than blue edges is an augmenting path for M. An edge in both matchings (violet) disappears from the symmetric difference](./plots/berge.py)

Theorem 5.1.1 is known as *Berge's theorem*. It holds for all graphs and underlies all maximum matching algorithms.

### 5.1.3. The Hungarian Algorithm

The *Hungarian algorithm* is the classical algorithm for maximum matchings in **bipartite graphs**. Starting from some initial matching, it repeatedly looks for augmenting paths to enlarge the matching. The algorithm marks the vertices of $X$ with three labels: $0$ for an unsaturated vertex not yet searched, $1$ for a saturated vertex, and $2$ for an unsaturated vertex from which it has been established that no augmenting path starts.

**Algorithm 5.1.1 (Hungarian Algorithm)** Input: a bipartite graph $G = (X, Y, E)$ and an initial matching $M$ (possibly empty). Output: a maximum matching $M$.

1. Label every saturated vertex of $X$ with $1$ and all others with $0$.
2. If every vertex of $X$ has a nonzero label, $M$ is a maximum matching; stop. Otherwise choose a vertex $x_0 \in X$ labeled $0$.
3. Set $X_0 \leftarrow \{x_0\}$ and $Y_0 \leftarrow \varnothing$.
4. If $\Gamma(X_0) \subseteq Y_0$, there is no augmenting path starting at $x_0$; label $x_0$ with $2$ and go to step 2. Otherwise choose any $y \in \Gamma(X_0) \setminus Y_0$:
   - if $y$ is saturated, say $(y, z) \in M$, set $X_0 \leftarrow X_0 \cup \{z\}$ and $Y_0 \leftarrow Y_0 \cup \{y\}$, and go to step 4;
   - if $y$ is unsaturated, an augmenting path $P$ from $x_0$ to $y$ has been found; set $M \leftarrow M \oplus P$, label $x_0$ with $1$, and go to step 2.

Step 4 in effect grows an alternating tree rooted at $x_0$: the vertices of $Y_0$ are saturated and their partners have been put into $X_0$, so the path in the tree from $x_0$ to any vertex is an alternating path, and as soon as an unsaturated $y$ is met, the path in the tree from $x_0$ to $y$ is an augmenting path.

**Example 5.1.2** We run the Hungarian algorithm on the bipartite graph of Example 5.1.1, starting from $M = \{x_1y_1, x_3y_2\}$ and choosing $y$ in order of index. The vertices $x_1, x_3$ are labeled $1$, and $x_2, x_4, x_5$ are labeled $0$.

1. $x_0 = x_2$: $y_1$ is saturated, and its partner $x_1$ joins $X_0$; $y_2$ is saturated, and its partner $x_3$ joins $X_0$; $y_3$ is unsaturated, giving the augmenting path $x_2y_1x_1y_2x_3y_3$ (the path $P$ of Example 5.1.1) and $M = \{x_2y_1, x_1y_2, x_3y_3\}$.
2. $x_0 = x_4$: $y_3$ is saturated, so $x_3$ joins $X_0$; $y_2$ is saturated, so $x_1$ joins; $y_1$ is saturated, so $x_2$ joins; $y_4$ is unsaturated, giving the augmenting path $x_4y_3x_3y_4$ and $M = \{x_2y_1, x_1y_2, x_4y_3, x_3y_4\}$.
3. $x_0 = x_5$: $y_1$ is saturated, so $x_2$ joins, giving $X_0 = \{x_5, x_2\}$ and $Y_0 = \{y_1\}$; now $\Gamma(X_0) = \{y_1\} \subseteq Y_0$, and $x_5$ is labeled $2$.

All vertices of $X$ now have nonzero labels, and the maximum matching has $4$ edges. The set $A = \{x_2, x_5\}$ found in step 3 has $|\Gamma(A)| = 1 < 2$, so by Hall's theorem below (Theorem 5.2.1) $G$ has no complete matching from $X$ to $Y$: when the Hungarian algorithm fails, it produces exactly a violation of Hall's condition.

![The two searches of Example 5.1.2 after the first augmentation: the alternating tree from x4 (green edges, matching edges blue) reaches the unsaturated vertex y4, and the non-matching edges of the augmenting path are red; from x5 only y1 and its partner x2 can be reached, Γ(X0) = Y0, and x5 is labeled 2; the resulting maximum matching has 4 edges](./plots/hungarian.py)

The following program carries out the same process by depth-first search: `augment(x)` tries the neighbors $y$ of $x$ in turn, and if $y$ is unsaturated, or the partner of $y$ can recursively find another augmenting path, it flips the matching along this path.

```python
# Maximum bipartite matching by augmenting paths (Example 5.1.2)
adj = {"x1": ["y1", "y2"], "x2": ["y1"], "x3": ["y2", "y3", "y4", "y5"],
       "x4": ["y3"], "x5": ["y1"]}
mate = {"x1": "y1", "y1": "x1", "x3": "y2", "y2": "x3"}  # initial matching M


def augment(x, seen):
    """Search an alternating tree from x; flip an augmenting path if one is found."""
    for y in adj[x]:
        if y in seen:
            continue
        seen.add(y)
        if y not in mate or augment(mate[y], seen):  # y free, or its partner can move
            mate[x], mate[y] = y, x
            return True
    return False


for x in ["x2", "x4", "x5"]:  # the unsaturated vertices of X, in order
    seen = set()
    if augment(x, seen):
        print(x, "-> augmented")
    else:
        print(x, "-> no augmenting path; Y0 =", sorted(seen))
matching = sorted((x, mate[x]) for x in adj if x in mate)
print("maximum matching:", matching, "size", len(matching))
```

```text
x2 -> augmented
x4 -> augmented
x5 -> no augmenting path; Y0 = ['y1']
maximum matching: [('x1', 'y2'), ('x2', 'y1'), ('x3', 'y4'), ('x4', 'y3')] size 4
```

Each search from a vertex $x$ examines every edge at most once, so the algorithm runs in $O(nm)$ time; the Hopcroft–Karp algorithm augments along many shortest augmenting paths at once in each phase and reduces this to $O(m\sqrt{n})$.

## 5.2. Complete Matchings

### 5.2.1. Definition and Hall's Theorem

**Definition 5.2.1 (Complete Matching)** Let $M$ be a matching in a **bipartite graph** $G = (X, Y, E)$. If $|M| = |X|$, that is, every vertex of $X$ is saturated, then $M$ is called a **complete matching** from $X$ to $Y$. If $|M| = |X| = |Y|$, then $M$ is called a **perfect matching**.

For $A \subseteq X$, let $\Gamma(A)$ denote the set of all neighbors of vertices in $A$, that is, the union of their **neighborhoods**.

**Theorem 5.2.1 (Hall's Theorem)** A bipartite graph $G = (X, Y, E)$ has a complete matching from $X$ to $Y$ if and only if $|\Gamma(A)| \ge |A|$ for every subset $A$ of $X$.

**Proof** Necessity: if there is a complete matching, the vertices of $A$ are matched to $|A|$ distinct vertices of $Y$, all of which belong to $\Gamma(A)$; hence $|\Gamma(A)| \ge |A|$.

Sufficiency: suppose the condition holds but there is no complete matching. Take a maximum matching $M$; then $X$ contains an unsaturated vertex $x_0$. Let $Z$ be the set of all vertices reachable from $x_0$ by alternating paths with respect to $M$ (including $x_0$), and let $X' = Z \cap X$ and $Y' = Z \cap Y$. Since $M$ is a maximum matching, Theorem 5.1.1 shows that there is no augmenting path, so every vertex of $Y'$ is saturated and its partner in $M$ belongs to $X' \setminus \{x_0\}$; conversely, every vertex of $X' \setminus \{x_0\}$ is reached from $Y'$ along an edge of $M$. Hence $|Y'| = |X'| - 1$. Moreover, every neighbor of a vertex in $X'$ is reachable by an alternating path, so $\Gamma(X') = Y'$ and $|\Gamma(X')| = |X'| - 1 < |X'|$, contradicting the condition. $\square$

*Hall's marriage theorem*, as Hall's theorem is also called, has the following interpretation: think of $X$ as a group of people and $Y$ as the available partners, with $x$ adjacent to $y$ meaning that $x$ is willing to choose $y$. Everyone can be given a distinct partner if and only if, for every $k$, any $k$ people are together willing to choose at least $k$ partners.

**Corollary 5.2.1** Let $k \ge 1$. If in a bipartite graph $G = (X, Y, E)$ every vertex $x \in X$ has $d(x) \ge k$ and every vertex $y \in Y$ has $d(y) \le k$, then there is a complete matching from $X$ to $Y$.

**Proof** For any $A \subseteq X$, at least $k|A|$ edges are incident with $A$, and their other endpoints all lie in $\Gamma(A)$. Each vertex of $\Gamma(A)$ is incident with at most $k$ edges, so $k|\Gamma(A)| \ge k|A|$, that is, $|\Gamma(A)| \ge |A|$. The claim follows from Hall's theorem. $\square$

### 5.2.2. Maximum Matchings and Minimum Covers

Let $A$ be the adjacency matrix of a bipartite graph $G = (X, Y, E)$, with $|X|$ rows and $|Y|$ columns and $a_{ij} = 1$ if and only if $x_i$ is adjacent to $y_j$. (This is the block of the adjacency matrix of [Chapter 1](/1.4.1) with rows $X$ and columns $Y$, also called the biadjacency matrix; the adjacency matrix of the whole graph is $\begin{bmatrix} O & A \\ A^{\mathsf T} & O \end{bmatrix}$.) A matching corresponds to a set of nonzero entries of $A$ lying in distinct rows and distinct columns, so the number of edges $r$ of a maximum matching is the maximum number of nonzero entries of $A$ in distinct rows and distinct columns.

**Definition 5.2.2 (Minimum Cover Number)** If some rows and columns of a matrix $A$ are chosen so that every nonzero entry of $A$ lies in one of the chosen rows or columns, we say that these rows and columns cover the nonzero entries of $A$. The minimum total number of rows and columns in such a cover is called the **minimum cover number** of $A$, denoted $s$.

Rows correspond to vertices of $X$, columns to vertices of $Y$, and nonzero entries to edges, so $s$ is also the minimum number of vertices that must be chosen so that every edge of $G$ has at least one chosen endpoint.

**Theorem 5.2.3 (König's Theorem)** Let $r$ be the number of edges of a maximum matching of a bipartite graph $G$, and $s$ the minimum cover number of its adjacency matrix. Then $r = s$.

**Proof** $s \ge r$: each row or column covers at most one of the $r$ nonzero entries lying in distinct rows and distinct columns, so at least $r$ rows and columns are needed to cover them.

$r \ge s$: let a minimum cover consist of $c$ rows and $d$ columns, $s = c + d$, with the rows corresponding to $X_c \subseteq X$ and the columns to $Y_d \subseteq Y$. For every $S \subseteq X_c$, the set $S$ has at least $|S|$ neighbors in $Y \setminus Y_d$; otherwise, replacing the rows of $S$ in the cover by the columns of these neighbors would still give a cover, with fewer rows and columns, contradicting minimality. By Hall's theorem there is a matching between $X_c$ and $Y \setminus Y_d$ that saturates $X_c$, of size $c$. Similarly, there is a matching of size $d$ between $Y_d$ and $X \setminus X_c$. These two matchings use disjoint sets of vertices, and together they form a matching of $G$ of size $c + d = s$; hence $r \ge s$. $\square$

In the language of graphs, *König's theorem* states that in a bipartite graph the number of edges of a maximum matching equals the minimum number of vertices needed to cover all edges.

**Example 5.2.1** The bipartite graph of Example 5.1.1 has a maximum matching with $r = 4$ edges (Example 5.1.2). The row of $x_3$ together with the columns of $y_1, y_2, y_3$ cover all nonzero entries of the adjacency matrix, so $s = 4 = r$. In terms of vertices: the set $\{x_3, y_1, y_2, y_3\}$ contains at least one endpoint of every edge.

![Example 5.2.1: the biadjacency matrix of Example 5.1.1. The four circled nonzero entries lie in distinct rows and columns and form a maximum matching; the shaded row and three columns cover all nonzero entries, so the cover number is also 4](./plots/konig.py)

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

![A blossom in a general graph: the augmenting path r s b c1 c2 c3 c4 w from the unsaturated vertex r (matching edges blue, others red) runs around the odd cycle b c1 c2 c3 c4; a search that goes from b directly to c4 never reaches w. After the blossom is shrunk to a single vertex B, the augmenting path r s B w is plain to see](./plots/blossom.py)

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

In matrix form: let $B$ be the **incidence matrix** of $N$ ([Chapter 1](/1.4.1), with $1$ at the tail and $-1$ at the head) and $\boldsymbol{f}$ the column vector of edge flows. The $i$-th component of $B\boldsymbol{f}$ is the outflow minus the inflow at vertex $i$, so conditions 2 and 3 together read

$$
B\boldsymbol{f} = W(\boldsymbol{e}_s - \boldsymbol{e}_t), \qquad \boldsymbol{0} \le \boldsymbol{f} \le \boldsymbol{c},
$$

where $\boldsymbol{c}$ is the capacity vector and the inequalities hold componentwise. The maximum flow problem is therefore a linear program. Every square submatrix of $B$ has determinant $0$ or $\pm 1$ ([Chapter 3](/1.4.3)), and it follows that when all capacities are integers there is a maximum flow with integer values.

### 5.5.3. Cuts and Their Capacities

**Definition 5.5.2 (Cut)** Let $S$ be a subset of the vertex set $V$ with $s \in S$ and $t \in \overline{S} = V \setminus S$. The set of all directed edges $(i, j)$ from $S$ to $\overline{S}$ ($i \in S$, $j \in \overline{S}$) is called an **s–t cut** of $N$, written $(S, \overline{S})$; its capacity is

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

The figure below gives a small example. If we alternate between $s\,a\,b\,t$ and $s\,b\,a\,t$ (the latter using $(a, b)$ as a backward edge), each augmentation adds only $1$, and $200$ augmentations are needed to reach the maximum flow $200$; choosing the shortest flow augmenting paths $s\,a\,t$ and $s\,b\,t$ takes two. This is exactly the improvement made by the Edmonds–Karp algorithm.

![A bad choice for the Ford–Fulkerson algorithm: augmenting alternately along s-a-b-t and s-b-a-t (violet: a backward edge whose flow decreases) adds only 1 per round, 200 rounds in all; Edmonds–Karp chooses the shortest flow augmenting paths s-a-t and s-b-t and reaches the maximum flow 200 in two rounds (edges are labeled flow/capacity)](./plots/ford-fulkerson-zigzag.py)

## 5.7. The Edmonds–Karp Algorithm for Maximum Flow

The Edmonds–Karp algorithm improves the Ford–Fulkerson algorithm by always choosing a shortest flow augmenting path (one with the fewest edges), which guarantees polynomial running time.

### 5.7.1. Description of the Algorithm

The algorithm is essentially the Ford–Fulkerson algorithm, except that the labeling procedure uses **breadth-first search**, that is, vertices are scanned in the order in which they were labeled ("first labeled, first scanned"). This guarantees that the flow augmenting path found from $s$ to $t$ has the fewest possible edges.

**Example 5.7.1** A network $N$ has source $s$, sink $t$, intermediate vertices $a, b, c, d$, and capacities

$$
c_{sa} = 2,\ c_{sc} = 6,\ c_{ab} = 9,\ c_{ad} = 6,\ c_{cb} = 4,\ c_{cd} = 1,\ c_{bt} = 2,\ c_{dt} = 9.
$$

Starting from the zero flow, we label by breadth-first search (examining the neighbors of a vertex in alphabetical order):

1. $a, c$ are labeled from $s$, $b, d$ from $a$, and $t$ from $b$: augment along $s\,a\,b\,t$ by $\delta = \min\{2, 9, 2\} = 2$, giving value $2$.
2. $(s, a)$ is saturated, so $c$ is labeled from $s$; $b, d$ are labeled from $c$; $a$ is labeled from $b$ through the backward edge $(a, b)$, with label $(b^-, 2)$; and $t$ is labeled from $d$: augment along $s\,c\,d\,t$ by $1$, giving value $3$.
3. Now $(c, d)$ is saturated too, so $d$ can be labeled only from $a$, and $a$ only from $b$ through the backward edge: augment along $s\,c\,b\,a\,d\,t$ by $\delta = \min\{5, 4, 2, 6, 8\} = 2$; the flow on the backward edge $(a, b)$ drops from $2$ to $0$, and the value becomes $5$.
4. Only $c$ (from $s$) and $b$ (from $c$) can be labeled; $t$ cannot, and the algorithm stops.

The labeled set $S = \{s, b, c\}$ gives the cut $(S, \overline{S}) = \{(s, a), (c, d), (b, t)\}$ of capacity $2 + 1 + 2 = 5$, equal to the maximum flow value, as Theorem 5.5.2 asserts. The edge $(a, b)$, directed from $\overline{S}$ to $S$, carries flow $0$, in agreement with the proof of that theorem. Round 3 shows what backward edges are for: round 1 sent $2$ units along $a \to b \to t$ and blocked the exit of $b$; round 3 "sends them back" to $a$ and reroutes them along $a \to d \to t$, freeing $b \to t$ for the flow coming from $c$.

![The Edmonds–Karp algorithm on Example 5.7.1. Each of the first three panels is one round: the breadth-first labels in green (origin with sign, and the amount that can be added), the forward edges of the shortest flow augmenting path in red, the backward edge in violet, and the edges labeled flow/capacity after the augmentation. In the last panel t cannot be labeled; the labeled vertices (amber) form S, and the three red edges form a minimum cut of capacity 5](./plots/edmonds-karp.py)

```python
# Edmonds-Karp: breadth-first labeling, augment along shortest paths (Example 5.7.1)
from collections import deque

cap = {("s", "a"): 2, ("s", "c"): 6, ("a", "b"): 9, ("a", "d"): 6, ("c", "b"): 4,
       ("c", "d"): 1, ("b", "t"): 2, ("d", "t"): 9}
flow = {e: 0 for e in cap}
nodes = {u for e in cap for u in e}


def bfs_label():  # first labeled, first scanned; label[v] = (u, "+" or "-")
    label, queue = {"s": None}, deque(["s"])
    while queue:
        u = queue.popleft()
        for v in sorted(nodes - label.keys()):
            if (u, v) in cap and flow[u, v] < cap[u, v]:
                label[v] = (u, "+")
            elif (v, u) in cap and flow[v, u] > 0:
                label[v] = (u, "-")
            else:
                continue
            queue.append(v)
    return label


value = 0
while "t" in (label := bfs_label()):
    path, v = [], "t"
    while v != "s":  # trace the labels back from t
        u, sign = label[v]
        path.append(((u, v), sign))  # step u -> v
        v = u
    path.reverse()
    delta = min(cap[e] - flow[e] if s == "+" else flow[e[::-1]] for e, s in path)
    for e, s in path:  # e = (u, v) is the arc (u, v) if s is "+", the arc (v, u) if "-"
        if s == "+":
            flow[e] += delta
        else:
            flow[e[::-1]] -= delta
    value += delta
    walk = "s" + "".join(f" {s}{e[1]}" for e, s in path)  # + forward edge, - backward edge
    print(f"path {walk:16s} delta {delta}  value {value}")
print("S =", sorted(label), "cut capacity", sum(c for (i, j), c in cap.items() if i in label and j not in label))
```

```text
path s +a +b +t       delta 2  value 2
path s +c +d +t       delta 1  value 3
path s +c +b -a +d +t delta 2  value 5
S = ['b', 'c', 's'] cut capacity 5
```

In the output, $+v$ means that $v$ is reached through a forward edge and $-v$ that it is reached through a backward edge.

### 5.7.2. Complexity

**Theorem 5.7.1** If the Edmonds–Karp algorithm always augments along a currently shortest flow augmenting path, then the number of augmentations is at most $\frac{m(n+2)}{2}$, where $n = |V|$ and $m = |E|$.

**Proof** (sketch) Let $\lambda^k(u, v)$ be the length of a shortest path from $u$ to $v$ after the $k$-th augmentation, computed using only edges along which the flow can be increased (unsaturated forward edges and backward edges with positive flow). One can show that $\lambda^k(s, v)$ is nondecreasing in $k$. In each augmentation at least one edge becomes a bottleneck (it determines the increment $\delta$, and after the augmentation the flow can no longer be increased along it). Between two occasions on which the same edge becomes a bottleneck, the distance from $s$ to its endpoint increases by at least $2$; since distances do not exceed $n$, each edge becomes a bottleneck at most about $n/2 + 1$ times. Hence the total number of augmentations is at most $m(n/2 + 1) = \frac{m(n+2)}{2}$. $\square$

Each shortest flow augmenting path is found by breadth-first search in $O(m)$ time, so the Edmonds–Karp algorithm runs in $O(nm^2)$ time.

## 5.8. Minimum-Cost Flow

Suppose that, in addition, each edge $(i, j)$ of a flow network carries a cost $a_{ij} \ge 0$ per unit of flow. The *minimum-cost flow* problem asks, among all feasible flows of a given value $W$, for one minimizing the total cost $\sum a_{ij} f_{ij}$. A common method is to start from the zero flow and repeatedly augment along a flow augmenting path that is shortest with respect to cost (forward edges having length $a_{ij}$ and backward edges length $-a_{ij}$), until the flow value reaches $W$; augmenting all the way to a maximum flow gives a *minimum-cost maximum flow*.

## 5.9. The Connection Between Matching and Network Flow

The maximum matching problem for a **bipartite graph** can be transformed into a maximum flow problem: add a source $s$ and a sink $t$, add an edge of capacity $1$ from $s$ to each vertex of $X$ and from each vertex of $Y$ to $t$, and turn each edge of the bipartite graph into a directed edge of capacity $1$ from $X$ to $Y$. In an integral maximum flow, the original edges carrying flow $1$ form a maximum matching, and the maximum flow value equals the number of edges of a maximum matching. On this network every flow augmenting path of the Ford–Fulkerson algorithm corresponds exactly to an augmenting path in the bipartite graph, and the Hungarian algorithm is a special case. Similarly, by assigning costs to the edges, the optimal matching problem can be transformed into a minimum-cost maximum flow problem.

![The bipartite graph of Example 5.1.1 as a network with unit capacities: the red arcs carry flow 1 and form an integral maximum flow of value 4, whose red arcs from X to Y are a maximum matching](./plots/matching-flow.py)

## Summary

- Matchings:

  | Problem | Key result | Algorithm |
  | :-- | :-- | :-- |
  | Maximum matching in a bipartite graph | Berge's theorem (Theorem 5.1.1): $M$ is maximum if and only if there is no augmenting path | The Hungarian algorithm (Algorithm 5.1.1), repeatedly replacing $M$ by $M \oplus P$ along an augmenting path |
  | Complete matching | Hall's theorem (Theorem 5.2.1): $\lvert\Gamma(A)\rvert \ge \lvert A\rvert$ for every $A \subseteq X$; a degree condition in Corollary 5.2.1 | — |
  | Maximum matching and covers | König's theorem (Theorem 5.2.3): the size of a maximum matching equals the minimum cover number of the adjacency matrix | — |
  | Optimal matching (maximum-weight perfect matching) | Labels with $l(x_i) + l(y_j) \ge c_{ij}$; a perfect matching on the tight edges is optimal (Theorem 5.3.1) | The Kuhn–Munkres algorithm (Algorithm 5.3.1) |
  | Maximum matching in a general graph | Still based on augmenting paths, but odd cycles must be handled | Edmonds' blossom algorithm (Section 5.4) |

- Network flows: a feasible flow satisfies the capacity constraints, flow conservation and equality of the flow out of the source and into the sink; every flow value is at most the capacity of every cut (Theorem 5.5.1), and the maximum flow value equals the minimum cut capacity (Theorem 5.5.2).
- Maximum-flow algorithms:

  | Algorithm | Augmentation | Complexity |
  | :-- | :-- | :-- |
  | Ford–Fulkerson labeling algorithm (Algorithm 5.6.1) | Any flow augmenting path (unsaturated forward edges, backward edges with positive flow) | Terminates for integer capacities, but the number of steps may be of the order of the maximum flow value; may fail to terminate for irrational capacities |
  | Edmonds–Karp algorithm (Section 5.7) | Shortest augmenting paths found by breadth-first search | At most $\frac{m(n+2)}{2}$ augmentations (Theorem 5.7.1), $O(nm^2)$ in total |
  | Minimum-cost flow (Section 5.8) | Augment along shortest augmenting paths with costs as lengths | — |

- The connection between the two problems (Section 5.9): after adding a source, a sink and unit capacities to a bipartite graph, the size of a maximum matching equals the value of an integer maximum flow, and the Hungarian algorithm amounts to running the Ford–Fulkerson algorithm on this network; optimal matchings correspond to minimum-cost maximum flows. Flow conservation reads $B\boldsymbol{f} = W(\boldsymbol{e}_s - \boldsymbol{e}_t)$ with $B$ the incidence matrix, so maximum flow is a linear program.
