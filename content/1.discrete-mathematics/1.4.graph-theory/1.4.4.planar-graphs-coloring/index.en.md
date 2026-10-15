---
title: Planar Graphs and Graph Coloring
source_hash: ef436d4fef10
---

Problems such as wiring printed circuit boards and drawing maps require a graph to be drawn in the plane without crossing edges; this is the problem of planar graphs. In this chapter we first introduce planar graphs, faces and Euler's formula, and derive from it an upper bound on the number of edges of a planar graph. We then present the two basic nonplanar graphs $K_5$ and $K_{3,3}$, Kuratowski's theorem characterizing planar graphs, and the ideas behind planarity testing. Finally we discuss dual graphs and, starting from map coloring, the coloring of graphs: the five color theorem, bounds on the chromatic number, and the chromatic polynomial.

## 4.1. Basic Concepts of Planar Graphs

### 4.1.1. Definition of a Planar Graph

**Definition 4.1.1 (Planar Graph)** If a graph $G$ can be drawn in the plane so that no two edges meet except at their endpoints, we say that $G$ is **embeddable in the plane**, or that $G$ is **planar**. Such a drawing of a planar graph in the plane (an embedding) is called a **plane graph**; following common usage, we also call it a **planar graph** when no confusion can arise.

**Definition 4.1.2 (Face)** Let $G$ be a plane graph. A region bounded by edges of $G$ whose interior contains no vertex and no edge is called a **face** (or region) of $G$, and the edges surrounding the face form its **boundary**. The infinite region outside $G$ is called the **unbounded face** (outer face), and all other faces are **interior faces**. Two faces sharing a boundary edge are said to be **adjacent**; otherwise they are **nonadjacent**. The number of edges in the boundary of a face is called the **length** of the face; if both sides of an edge (for example, a **cut edge**) lie in the same face, the edge is counted twice in the boundary of that face.

Since every edge is counted exactly twice in the face lengths (once for each of two faces, or twice for the same face), the lengths of all faces sum to $2m$.

### 4.1.2. Euler's Formula

The numbers of vertices, edges and faces of a connected plane graph satisfy a simple relation, known as *Euler's formula for planar graphs*.

**Theorem 4.1.1 (Euler's Formula)** Let $G$ be a connected plane graph with $n$ vertices, $m$ edges and $d$ faces. Then

$$
d = m - n + 2.
$$

**Proof** Since $G$ is connected, it has a **spanning tree** $T$. $T$ has $n-1$ edges and no cycle, so it has only one face (the unbounded face). Following the embedding of $G$, add back the $m - (n-1)$ chords one at a time. The two endpoints of each chord are already joined by a path in the current graph, and the chord forms a cycle with this path, so it splits the face containing it into two and increases the number of faces by $1$. Hence $d = 1 + (m - n + 1) = m - n + 2$. $\square$

**Corollary 4.1.1** If a plane graph $G$ has $k$ connected components, then

$$
n - m + d = k + 1.
$$

**Corollary 4.1.2** Every plane graph $G$ satisfies

$$
n - m + d \ge 2.
$$

### 4.1.3. Bounds on the Numbers of Edges and Faces

**Theorem 4.1.2** Let $G$ be a connected plane graph without **cut edges** in which every face has length at least $t$ ($t \ge 3$). Then

$$
m \le \frac{t(n-2)}{t-2}.
$$

**Proof** Let $G$ have $d$ faces. The face lengths sum to $2m$, and each is at least $t$, so $t d \le 2m$. Substituting Euler's formula $d = m - n + 2$ gives

$$
t(m - n + 2) \le 2m \;\Longrightarrow\; (t-2)m \le t(n-2) \;\Longrightarrow\; m \le \frac{t(n-2)}{t-2}. \qquad \square
$$

## 4.2. Maximal Planar Graphs

### 4.2.1. Definition and Basic Properties

**Definition 4.2.1 (Maximal Planar Graph)** Let $G$ be a simple planar graph with $n \ge 3$. If adding an edge $(v_i, v_j)$ between any two nonadjacent vertices $v_i, v_j$ of $G$ makes it nonplanar, then $G$ is called a **maximal planar graph** (also called a triangulation).

Maximal planar graphs have the following properties:

1. $G$ is connected.
2. $G$ has no cut edge.
3. Every face of $G$ has length $3$; that is, every face is a triangle.
4. $3d = 2m$: every edge lies on exactly two faces, and every face has exactly $3$ boundary edges.

### 4.2.2. Numbers of Edges and Faces of Maximal Planar Graphs

**Theorem 4.2.1** A maximal planar graph $G$ satisfies

$$
m = 3n - 6, \qquad d = 2n - 4.
$$

**Proof** From $3d = 2m$ and Euler's formula $d = m - n + 2$ we get $2m = 3(m - n + 2)$, that is, $m = 3n - 6$; substituting gives $d = (3n - 6) - n + 2 = 2n - 4$. $\square$

**Corollary 4.2.1** A simple planar graph $G$ with $n \ge 3$ vertices satisfies

$$
m \le 3n - 6, \qquad d \le 2n - 4.
$$

**Proof** Keep adding edges to $G$ while preserving simplicity and planarity, until a maximal planar graph $G'$ is reached. Adding edges does not decrease the number of edges or faces, so by Theorem 4.2.1, $m \le m(G') = 3n - 6$ and $d \le d(G') = 2n - 4$. $\square$

**Theorem 4.2.2** Every simple planar graph $G$ has a vertex of degree less than $6$.

**Proof** The claim is obvious for $n \le 2$, so let $n \ge 3$. Suppose, for contradiction, that every vertex has degree at least $6$. Then $2m = \sum d(v_i) \ge 6n$, that is, $m \ge 3n$; but Corollary 4.2.1 gives $m \le 3n - 6$, a contradiction. $\square$

**Example 4.2.1** $K_7$ is not planar: for $K_7$ we have $n = 7$ and $m = 21$, while $3n - 6 = 15 < 21$, so the necessary condition of Corollary 4.2.1 fails.

## 4.3. Nonplanar Graphs

### 4.3.1. Two Basic Nonplanar Graphs

**Definition 4.3.1 (Nonplanar Graph)** A graph that cannot be embedded in the plane (that is, a graph that is not planar) is called a **nonplanar graph**.

If the vertex set of a graph $G$ can be split into two disjoint subsets $X$ and $Y$ such that every edge has one endpoint in $X$ and the other in $Y$, then $G$ is called a *bipartite graph*, written $G = (X, Y, E)$. If, moreover, every vertex of $X$ is joined to every vertex of $Y$ by exactly one edge, with $|X| = r$ and $|Y| = s$, then $G$ is called a *complete bipartite graph*, written $K_{r,s}$.

The following two graphs are the most basic nonplanar graphs:

- $K_5$ (the **complete graph** on $5$ vertices) is a nonplanar graph with the fewest vertices.
- $K_{3,3}$ (the complete bipartite graph with $3$ vertices in each part) is a nonplanar graph with the fewest edges ($9$).

**Theorem 4.3.1** $K_5$ is nonplanar.

**Proof** For $K_5$ we have $n = 5$ and $m = 10$. If it were planar, Corollary 4.2.1 would give $m \le 3n - 6 = 9$, a contradiction. $\square$

**Theorem 4.3.2** $K_{3,3}$ is nonplanar.

**Proof** For $K_{3,3}$ we have $n = 6$ and $m = 9$. If it were planar, Euler's formula would give $d = m - n + 2 = 5$. But a bipartite graph contains no odd cycle, in particular no triangle, so every face has length at least $4$; hence $4d \le 2m$, that is, $20 \le 18$, a contradiction. $\square$

### 4.3.2. Kuratowski's Theorem

**Definition 4.3.2 ($K$-Type Graph)** The graphs obtained from $K_5$ or $K_{3,3}$ by inserting arbitrarily many vertices of degree $2$ into their edges (that is, the subdivisions of $K_5$ and $K_{3,3}$) are called **graphs of type $K^{(1)}$** and **graphs of type $K^{(2)}$** respectively, and collectively **$K$-type graphs**.

**Theorem 4.3.3 (Kuratowski's Theorem)** A graph $G$ is planar if and only if $G$ contains no $K$-type subgraph, that is, no subgraph obtained from $K_5$ or $K_{3,3}$ by inserting vertices of degree $2$.

*Kuratowski's theorem* is of great theoretical value, but using it directly to decide planarity requires a great deal of computation, so practical planarity testing algorithms are needed.

## 4.4. Planarity Testing

### 4.4.1. Preprocessing

To decide whether a graph $G$ is planar, one can first simplify it as follows:

1. Disconnected graphs: test each **connected component** separately. $G$ is planar if all its connected components are.
2. Loops: delete all **loops**; loops do not affect planarity.
3. Cut vertices: split the graph at its cut vertices (vertices whose deletion increases the number of connected components; see Definition 6.1.2) into subgraphs without cut vertices (blocks; see Definition 6.1.3), and test each block separately.
4. Vertices of degree $2$: delete a vertex of degree $2$ together with its two incident edges, and add an edge between its two neighbors (series reduction). The original graph is planar if and only if the new graph is.
5. Multiple edges: replace **multiple edges** by a single edge.

After repeatedly applying steps 4 and 5:

- If $m < 9$ or $n < 5$, then $G$ is planar.
- If $m > 3n - 6$, then $G$ is nonplanar.
- Otherwise further testing is needed, for example with the DMP algorithm.

### 4.4.2. The DMP Algorithm

The DMP algorithm (Demoucron–Malgrange–Pertuiset algorithm) is a practical planarity testing algorithm: first draw a cycle of the graph in the plane, then embed the remaining parts of the graph step by step into faces already drawn; if at some step no embedding is possible, the graph is nonplanar. We omit the details.

## 4.5. Dual Graphs

### 4.5.1. Definition of the Dual Graph

**Definition 4.5.1 (Dual Graph)** Let $G$ be a plane graph. The graph $G^*$ satisfying the following conditions is called the **dual graph** (geometric dual) of $G$:

1. Place a vertex $v_i^*$ inside each face $f_i$ of $G$.
2. For each common boundary edge $e_k$ of faces $f_i$ and $f_j$, draw an edge $e_k^* = (v_i^*, v_j^*)$ that crosses $e_k$ exactly once.
3. If both sides of an edge $e_k$ lie in the same face $f_i$ (for example, if $e_k$ is a **cut edge**), draw a loop $e_k^*$ at $v_i^*$ that crosses $e_k$ exactly once.

**Property 4.5.1** Every plane graph $G$ has a dual graph $G^*$, and $G^*$ is unique up to isomorphism.

**Property 4.5.2** $G^*$ is connected.

**Property 4.5.3** If $G$ is a connected plane graph, then $(G^*)^* \cong G$.

**Property 4.5.4** The numbers of vertices, edges and faces of a connected plane graph $G$ and of its dual $G^*$ are related by

$$
m = m^*, \qquad d = n^*, \qquad n = d^*.
$$

**Property 4.5.5** Let $C$ be a cycle of a plane graph $G$, and let $S^*$ be the set of edges $e_i^*$ of $G^*$ corresponding to the edges $e_i$ of $C$. Then $S^*$ is a **cut set** of $G^*$.

**Theorem 4.5.1** $G$ has a dual graph if and only if $G$ is planar.

**Proof** Sufficiency follows from Property 4.5.1. Necessity is proved by contradiction: if $G$ is nonplanar, it contains a $K$-type subgraph, and an analysis of the duals of $K_5$ and $K_{3,3}$ leads to a contradiction (using inequalities between degrees and numbers of edges). $\square$

**Remark** For geometric duals, necessity follows directly from the definition. The real content of Theorem 4.5.1 is a statement about Whitney duals (combinatorial duals): if there is a graph $G^*$ whose edges correspond bijectively to those of $G$ in such a way that the cycles of $G$ correspond exactly to the cut sets of $G^*$, then $G$ is planar. The proof idea above refers to duals in this sense.

### 4.5.2. The Four Color Problem and Dual Graphs

Regard the countries on a map as faces, place a vertex inside each country, and join the vertices of neighboring countries by edges; this gives the dual graph of the map. The problem of coloring a map thus becomes the problem of coloring the vertices of a planar graph: color the vertices with as few colors as possible so that adjacent vertices receive different colors. The four color problem (four color conjecture) asserts that the vertices of every planar graph can be colored with $4$ colors. The conjecture was proved in 1976 by Appel and Haken with the help of a computer and is now known as the *four color theorem*.

**Theorem 4.5.2 (Five Color Theorem)** Every planar graph $G$ without loops is $5$-colorable; that is, its vertices can be colored with $5$ colors so that adjacent vertices receive different colors.

**Proof** Deleting multiple edges does not affect colorings, so we may assume that $G$ is a simple planar graph. We use induction on the number of vertices $n$; the case $n \le 5$ is obvious. By Theorem 4.2.2, $G$ has a vertex $v$ of degree at most $5$. By the induction hypothesis, $G - v$ has a $5$-coloring.

If the neighbors of $v$ use fewer than $5$ colors (in particular, if $d(v) \le 4$), give $v$ a remaining color.

Otherwise $d(v) = 5$. Let $v_1, \dots, v_5$ be the neighbors of $v$ in the cyclic order around $v$ in the plane, colored $c_1, \dots, c_5$ respectively. Consider the subgraph $H_{13}$ of $G - v$ induced by the vertices colored $c_1$ or $c_3$:

- If $v_1$ and $v_3$ lie in different connected components of $H_{13}$, interchange the colors $c_1$ and $c_3$ in the component containing $v_1$. The coloring remains proper, $v_1$ now has color $c_3$, and color $c_1$ becomes free for $v$.
- If $v_1$ and $v_3$ lie in the same connected component of $H_{13}$, there is a path from $v_1$ to $v_3$ whose colors alternate between $c_1$ and $c_3$; together with $v$ it forms a cycle that separates $v_2$ from $v_4$, one lying inside and the other outside. Hence in the subgraph $H_{24}$ induced by the vertices colored $c_2$ or $c_4$, the vertices $v_2$ and $v_4$ lie in different connected components (any path joining them would have to cross the cycle, whose vertices are colored $c_1$ or $c_3$, apart from $v$). Interchange $c_2$ and $c_4$ in the component containing $v_2$; then color $c_2$ becomes free for $v$. $\square$

**Remark** Planar graphs in general need $4$ colors; $3$ colors do not always suffice. For example, $K_4$ is planar but has chromatic number $4$.

## 4.6. Chromatic Number and Chromatic Polynomial

### 4.6.1. Definition of the Chromatic Number

**Definition 4.6.1 (Chromatic Number)** For a graph $G$, the minimum number of colors needed to color the vertices so that adjacent vertices receive different colors is called the **chromatic number** of $G$, written $\gamma(G)$.

**Definition 4.6.2 (Chromatic Index)** For a graph $G$, the minimum number of colors needed to color the edges so that adjacent edges receive different colors is called the **chromatic index** of $G$, written $\beta(G)$.

### 4.6.2. Chromatic Numbers of Common Graphs

| Graph $G$ | Chromatic number $\gamma(G)$ |
|---|---|
| Empty graph $N_n$ | $1$ |
| Complete graph $K_n$ | $n$ |
| $K_n - e$ ($n \ge 2$, $e$ an edge) | $n-1$ |
| Bipartite graph with at least one edge | $2$ |
| Cycle of even length | $2$ |
| Cycle of odd length | $3$ |
| Tree ($n \ge 2$) | $2$ |

**Theorem 4.6.1** Let $G$ be a graph with at least one edge. Then $\gamma(G) = 2$ if and only if $G$ contains no cycle of odd length.

**Proof** Necessity: a cycle of odd length needs $3$ colors, so if $G$ contains an odd cycle, then $\gamma(G) \ge 3$.

Sufficiency: since each connected component can be colored separately, we may assume that $G$ is connected. Take a **spanning tree** $T$ of $G$ and $2$-color $T$ according to the parity of the distance in $T$ from a fixed vertex. Each chord $(u, v)$ forms a cycle with the path from $u$ to $v$ in $T$; by hypothesis this cycle has even length, so the path from $u$ to $v$ in $T$ has odd length, and $u, v$ receive different colors. Thus this coloring is also a proper coloring of $G$, and $\gamma(G) = 2$. $\square$

### 4.6.3. Upper Bounds on the Chromatic Number

Let $d_0 = \max_{v \in V} d(v)$ denote the maximum degree of $G$.

**Theorem 4.6.2** Every graph $G$ without loops satisfies $\gamma(G) \le d_0 + 1$.

**Proof** By induction on the number of vertices $n$. The claim holds for $n = 1$. Suppose it holds for graphs with $n-1$ vertices. Take any $v \in V(G)$ and let $G' = G - v$. The maximum degree $d_0'$ of $G'$ satisfies $d_0' \le d_0$, so by the induction hypothesis $\gamma(G') \le d_0' + 1 \le d_0 + 1$. When $v$ is put back, it has at most $d_0$ neighbors, which use at most $d_0$ colors, so one of the $d_0 + 1$ colors is still available for $v$. $\square$

**Theorem 4.6.3** Every graph $G$ without loops satisfies

$$
\gamma(G) \le 1 + \max_{G'} \delta(G'),
$$

where $G'$ ranges over the induced subgraphs of $G$ and $\delta(G')$ denotes the minimum degree of $G'$.

**Proof** Let $\gamma(G) = k$, and let $H$ be an induced subgraph with $\gamma(H) = k$ and as few vertices as possible. For each vertex $v$ of $H$, the minimality of $H$ implies that $H - v$ can be colored with $k-1$ colors. If $d_H(v) < k-1$, the neighbors of $v$ use at most $k-2$ colors, so $v$ can receive a remaining color, giving a $(k-1)$-coloring of $H$, a contradiction. Hence $d_H(v) \ge k-1$ for every vertex of $H$, that is, $\delta(H) \ge k-1$. Therefore

$$
k \le 1 + \delta(H) \le 1 + \max_{G'} \delta(G'). \qquad \square
$$

### 4.6.4. Recursive Computation of the Chromatic Number

**Definition 4.6.3** Let $v_i, v_j$ be two nonadjacent vertices of a simple graph $G$, and define

- $\overline{G_{ij}} = G + (v_i, v_j)$, the graph obtained by adding an edge between $v_i$ and $v_j$;
- $G_{ij}$, the simple graph obtained by merging $v_i$ and $v_j$ into a new vertex $v_{ij}$ that inherits all adjacencies of both (keeping only one copy of any multiple edges).

**Theorem 4.6.4** Let $v_i, v_j$ be two nonadjacent vertices of a simple graph $G$. Then

$$
\gamma(G) = \min\left\{ \gamma(\overline{G_{ij}}),\ \gamma(G_{ij}) \right\}.
$$

**Proof** In any proper coloring of $G$, either $v_i$ and $v_j$ have different colors, in which case it is also a proper coloring of $\overline{G_{ij}}$, or they have the same color, in which case it corresponds to a proper coloring of $G_{ij}$. Conversely, proper colorings of $\overline{G_{ij}}$ and of $G_{ij}$ both give proper colorings of $G$. $\square$

This theorem yields a recursive method for computing the chromatic number: force $v_i, v_j$ to receive different colors (by adding an edge) or the same color (by merging), compute the chromatic numbers in the two cases, and take the smaller.

### 4.6.5. The Chromatic Polynomial

**Definition 4.6.4 (Chromatic Polynomial)** For a simple graph $G$, the number of ways to color the vertices of $G$ with $t$ colors so that adjacent vertices receive different colors is denoted $f(G, t)$ and called the **chromatic polynomial** of $G$. One can show (by the recursion of Theorem 4.6.7 below) that $f(G, t)$ is a polynomial of degree $n$ in $t$; $f(G, t) = 0$ for positive integers $t < \gamma(G)$, and $\gamma(G)$ is the smallest positive integer $t$ with $f(G, t) > 0$.

Chromatic polynomials of common graphs:

- Empty graph $N_n$: $f(N_n, t) = t^n$.
- Complete graph $K_n$: $f(K_n, t) = t(t-1)\cdots(t-n+1)$.
- A tree $T_n$ on $n$ vertices ($n \ge 1$): $f(T_n, t) = t(t-1)^{n-1}$.
- If $G$ has $p$ connected components $G_1, \dots, G_p$, then $f(G, t) = \prod_{i=1}^p f(G_i, t)$.

**Theorem 4.6.7** Let $v_i, v_j$ be two nonadjacent vertices of a simple graph $G$. Then

$$
f(G, t) = f(\overline{G_{ij}}, t) + f(G_{ij}, t).
$$

This recursion follows the same idea as Theorem 4.6.4: the colorings of $G$ split into two classes according to whether $v_i, v_j$ receive different colors or the same color, corresponding to the colorings of $\overline{G_{ij}}$ and of $G_{ij}$ respectively. Applying it repeatedly eventually expresses $f(G, t)$ as a sum of chromatic polynomials of complete graphs.

### 4.6.6. Summary

- The chromatic number is the minimum number of colors needed for adjacent vertices to receive different colors; for common graphs it can be written down directly.
- Upper bounds on the chromatic number: $\gamma(G) \le d_0 + 1$, and the sharper bound $1 + \max \delta(G')$.
- The chromatic number can be computed recursively by adding edges and merging vertices.
- The chromatic polynomial $f(G, t)$ counts the colorings with $t$ colors and satisfies the same recursion.
