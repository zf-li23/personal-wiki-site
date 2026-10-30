---
title: Planar Graphs and Graph Coloring
source_hash: 74d21996742b
---

Problems such as wiring printed circuit boards and drawing maps require a graph to be drawn in the plane without crossing edges; this is the problem of planar graphs. In this chapter we first introduce planar graphs, faces and Euler's formula, and derive from it an upper bound on the number of edges of a planar graph. We then present the two basic nonplanar graphs $K_5$ and $K_{3,3}$, Kuratowski's theorem characterizing planar graphs, and the ideas behind planarity testing. Finally we discuss dual graphs and, starting from map coloring, the coloring of graphs: the five color theorem, bounds on the chromatic number, greedy coloring, and the chromatic polynomial. The proof of Euler's formula reuses the spanning trees and chords of [Chapter 3](/1.4.3), and duality, which matches the cycles of one graph with the cut sets of another, is the geometric form in the plane of the relation between the cycle matrix and the cut-set matrix studied there.

## 4.1. Basic Concepts of Planar Graphs

### 4.1.1. Definition of a Planar Graph

**Definition 4.1.1 (Planar Graph)** If a graph $G$ can be drawn in the plane so that no two edges meet except at their endpoints, we say that $G$ is **embeddable in the plane**, or that $G$ is **planar**. Such a drawing of a planar graph in the plane (an embedding) is called a **plane graph**; following common usage, we also call it a **planar graph** when no confusion can arise.

The same graph may be drawn with crossings or without them: being planar is a property of the graph itself, while a plane graph is one particular crossing-free drawing.

![Two drawings of the complete graph K4: on the left the two diagonals (red) cross; on the right one diagonal is moved outside and the other drawn inside the triangle (blue), so there is no crossing and K4 is planar](./plots/planar-embedding.py)

**Definition 4.1.2 (Face)** Let $G$ be a plane graph. A region bounded by edges of $G$ whose interior contains no vertex and no edge is called a **face** (or region) of $G$, and the edges surrounding the face form its **boundary**. The infinite region outside $G$ is called the **unbounded face** (outer face), and all other faces are **interior faces**. Two faces sharing a boundary edge are said to be **adjacent**; otherwise they are **nonadjacent**. The number of edges in the boundary of a face is called the **length** of the face; if both sides of an edge (for example, a **cut edge**) lie in the same face, the edge is counted twice in the boundary of that face.

Since every edge is counted exactly twice in the face lengths (once for each of two faces, or twice for the same face), the lengths of all faces sum to $2m$.

**Example 4.1.1** Let $G$ have vertices $v_1, \dots, v_5$ and the $6$ edges $v_1v_2, v_2v_3, v_3v_4, v_4v_1, v_1v_3, v_3v_5$, drawn in the plane as below. It has $3$ faces: the triangles $f_1 = v_1v_2v_3$ and $f_2 = v_1v_3v_4$ have length $3$; the boundary of the outer face $f_0$ consists of the $4$ edges of the square and the cut edge $v_3v_5$, which has $f_0$ on both sides and is counted twice, so $f_0$ has length $6$. The three lengths sum to $3 + 3 + 6 = 12 = 2m$.

![The plane graph of Example 4.1.1: two interior faces f1, f2 and the outer face f0; the red cut edge v3v5 has the face f0 on both sides and is counted twice in the boundary of f0](./plots/faces.py)

### 4.1.2. Euler's Formula

The numbers of vertices, edges and faces of a connected plane graph satisfy a simple relation, known as *Euler's formula for planar graphs*.

**Theorem 4.1.1 (Euler's Formula)** Let $G$ be a connected plane graph with $n$ vertices, $m$ edges and $d$ faces. Then

$$
d = m - n + 2.
$$

**Proof** Since $G$ is connected, it has a **spanning tree** $T$. $T$ has $n-1$ edges and no cycle, so it has only one face (the unbounded face). Following the embedding of $G$, add back the $m - (n-1)$ chords one at a time. The two endpoints of each chord are already joined by a path in the current graph, and the chord forms a cycle with this path, so it splits the face containing it into two and increases the number of faces by $1$. Hence $d = 1 + (m - n + 1) = m - n + 2$. $\square$

![The proof of Euler's formula on the graph of Example 4.1.1: a spanning tree (blue) has a single face; each chord added back (red) closes a cycle and splits one face into two](./plots/euler-formula.py)

Each of the $m - n + 1$ chords added back in the proof closes a **fundamental cycle** ([Chapter 3](/1.4.3)), so the number of interior faces of a connected plane graph, $d - 1 = m - n + 1$, equals the rank of its cycle matrix.

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

Both proofs use a bound on the number of edges: $K_5$ has one edge more than the $3n - 6 = 9$ allowed for a maximal planar graph, and $K_{3,3}$ one edge more than the $2n - 4 = 8$ allowed for a triangle-free planar graph (Theorem 4.1.2 with $t = 4$). In both cases this one edge is all that goes wrong: deleting any edge leaves a planar graph, and the figure shows drawings of each with a single crossing.

![Drawings of K5 and K3,3 with a single crossing each; deleting the red edge leaves a plane graph. K5 has more than 3n − 6 edges, and K3,3 more than the bound 2n − 4 for triangle-free planar graphs](./plots/k5-k33.py)

### 4.3.2. Kuratowski's Theorem

**Definition 4.3.2 ($K$-Type Graph)** The graphs obtained from $K_5$ or $K_{3,3}$ by inserting arbitrarily many vertices of degree $2$ into their edges (that is, the subdivisions of $K_5$ and $K_{3,3}$) are called **graphs of type $K^{(1)}$** and **graphs of type $K^{(2)}$** respectively, and collectively **$K$-type graphs**.

**Theorem 4.3.3 (Kuratowski's Theorem)** A graph $G$ is planar if and only if $G$ contains no $K$-type subgraph, that is, no subgraph obtained from $K_5$ or $K_{3,3}$ by inserting vertices of degree $2$.

*Kuratowski's theorem* is of great theoretical value, but using it directly to decide planarity requires a great deal of computation, so practical planarity testing algorithms are needed.

**Example 4.3.1** The Petersen graph (an outer cycle on $5$ vertices and an inner pentagram, joined by $5$ "spokes"; its connectivity is studied in [Chapter 6](/1.4.6)) is not planar.

**Proof** First method (edge bound): the Petersen graph is connected and has no cut edge, with $n = 10$, $m = 15$, and its shortest cycles have length $5$. If it were planar, every face would have length at least $5$, and Theorem 4.1.2 would give $m \le \frac{5(10-2)}{5-2} = \frac{40}{3} < 15$, a contradiction.

Second method (Kuratowski's theorem): after deleting the two dashed edges in the figure below, the $3$ blue and the $3$ red vertices have degree $3$ and the other $4$ vertices have degree $2$. Suppressing the vertices of degree $2$, every blue vertex is joined to every red vertex, which gives $K_{3,3}$. Hence the Petersen graph contains a subgraph of type $K^{(2)}$ and, by Theorem 4.3.3, is not planar. $\square$

![A subdivision of K3,3 in the Petersen graph: the blue and red vertices form the two parts of K3,3, the white vertices are degree-2 vertices inserted into its edges, and the two grey dashed edges are not used](./plots/kuratowski.py)

The Petersen graph contains no subdivision of $K_5$ (all its vertices have degree $3$, whereas a subdivision of $K_5$ needs $5$ vertices of degree $4$), so neither $K_5$ nor $K_{3,3}$ can be dropped from Kuratowski's theorem.

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

**Example 4.5.1** The plane graph $G$ of Example 4.1.1 has $3$ faces, so its dual $G^*$ has $3$ vertices $f_0^*, f_1^*, f_2^*$. The edge $v_1v_3$ separates $f_1$ from $f_2$ and gives the edge $f_1^*f_2^*$; the edges $v_1v_2$ and $v_2v_3$ separate $f_1$ from $f_0$ and give two parallel edges; $v_3v_4$ and $v_4v_1$ give two parallel edges between $f_2^*$ and $f_0^*$; and the cut edge $v_3v_5$, with $f_0$ on both sides, gives a loop at $f_0^*$. In general, then, a dual graph is not simple.

![The plane graph G of Example 4.1.1 (black) and its dual G* (red vertices and dashed edges): one dual vertex in each face, and each edge crossed exactly once by a dual edge; the cut edge v3v5 corresponds to the loop at f0*](./plots/dual.py)

**Property 4.5.1** Every plane graph $G$ has a dual graph $G^*$, and $G^*$ is unique up to isomorphism.

**Property 4.5.2** $G^*$ is connected.

**Property 4.5.3** If $G$ is a connected plane graph, then $(G^*)^* \cong G$.

**Property 4.5.4** The numbers of vertices, edges and faces of a connected plane graph $G$ and of its dual $G^*$ are related by

$$
m = m^*, \qquad d = n^*, \qquad n = d^*.
$$

**Property 4.5.5** Let $C$ be a cycle of a plane graph $G$, and let $S^*$ be the set of edges $e_i^*$ of $G^*$ corresponding to the edges $e_i$ of $C$. Then $S^*$ is a **cut set** of $G^*$.

In Example 4.5.1 we have $n^* = 3 = d$, $m^* = 6 = m$, and $G^*$ has $d^* = m^* - n^* + 2 = 5 = n$ faces, as Property 4.5.4 predicts. The three edges of the cycle $v_1v_2v_3$ correspond to the three edges at $f_1^*$, whose deletion separates $f_1^*$ from the rest: a cut set. For connected plane graphs the converse of Property 4.5.5 also holds (cut sets of $G^*$ correspond to cycles of $G$), so with the same order of edges and compatible orientations, the cycle matrix of $G$ is the cut-set matrix of $G^*$ ([Chapter 3](/1.4.3)): duality interchanges cycles and cut sets.

**Theorem 4.5.1** $G$ has a dual graph if and only if $G$ is planar.

**Proof** Sufficiency follows from Property 4.5.1. Necessity is proved by contradiction: if $G$ is nonplanar, it contains a $K$-type subgraph, and an analysis of the duals of $K_5$ and $K_{3,3}$ leads to a contradiction (using inequalities between degrees and numbers of edges). $\square$

**Remark** For geometric duals, necessity follows directly from the definition. The real content of Theorem 4.5.1 is a statement about Whitney duals (combinatorial duals): if there is a graph $G^*$ whose edges correspond bijectively to those of $G$ in such a way that the cycles of $G$ correspond exactly to the cut sets of $G^*$, then $G$ is planar. The proof idea above refers to duals in this sense.

### 4.5.2. The Four Color Problem and Dual Graphs

Regard the countries on a map as faces, place a vertex inside each country, and join the vertices of neighboring countries by edges; this gives the dual graph of the map. The problem of coloring a map thus becomes the problem of coloring the vertices of a planar graph: color the vertices with as few colors as possible so that adjacent vertices receive different colors. The four color problem (four color conjecture) asserts that the vertices of every planar graph can be colored with $4$ colors. The conjecture was proved in 1976 by Appel and Haken with the help of a computer and is now known as the *four color theorem*.

Four colors are sometimes necessary. In the map below the central country is surrounded by five others, and the dual graph is the wheel $W_5$ (one vertex joined to every vertex of a cycle of length $5$): the outer cycle is odd and needs $3$ colors, and the central vertex, adjacent to all of them, needs a fourth.

![A map of six countries and its dual graph: the central country is surrounded by an odd number of countries, the dual graph is the wheel W5, and four colors are needed](./plots/map-coloring.py)

The proof of the four color theorem requires a computer to check more than a thousand "unavoidable configurations". The five color theorem below has a short proof, and its argument of swapping two colors along a "Kempe chain" is also the starting point of the proof of the four color theorem.

**Theorem 4.5.2 (Five Color Theorem)** Every planar graph $G$ without loops is $5$-colorable; that is, its vertices can be colored with $5$ colors so that adjacent vertices receive different colors.

**Proof** Deleting multiple edges does not affect colorings, so we may assume that $G$ is a simple planar graph. We use induction on the number of vertices $n$; the case $n \le 5$ is obvious. By Theorem 4.2.2, $G$ has a vertex $v$ of degree at most $5$. By the induction hypothesis, $G - v$ has a $5$-coloring.

If the neighbors of $v$ use fewer than $5$ colors (in particular, if $d(v) \le 4$), give $v$ a remaining color.

Otherwise $d(v) = 5$. Let $v_1, \dots, v_5$ be the neighbors of $v$ in the cyclic order around $v$ in the plane, colored $c_1, \dots, c_5$ respectively. Consider the subgraph $H_{13}$ of $G - v$ induced by the vertices colored $c_1$ or $c_3$:

- If $v_1$ and $v_3$ lie in different connected components of $H_{13}$, interchange the colors $c_1$ and $c_3$ in the component containing $v_1$. The coloring remains proper, $v_1$ now has color $c_3$, and color $c_1$ becomes free for $v$.
- If $v_1$ and $v_3$ lie in the same connected component of $H_{13}$, there is a path from $v_1$ to $v_3$ whose colors alternate between $c_1$ and $c_3$; together with $v$ it forms a cycle that separates $v_2$ from $v_4$, one lying inside and the other outside. Hence in the subgraph $H_{24}$ induced by the vertices colored $c_2$ or $c_4$, the vertices $v_2$ and $v_4$ lie in different connected components (any path joining them would have to cross the cycle, whose vertices are colored $c_1$ or $c_3$, apart from $v$). Interchange $c_2$ and $c_4$ in the component containing $v_2$; then color $c_2$ becomes free for $v$. $\square$

![The two cases in the proof of the five color theorem (colors 1–5 are blue, red, green, amber and violet). Left: the 1–3 chain from v1 (blue edges) does not reach v3; swapping colors 1 and 3 on it gives v1 color 3 and frees color 1 for v. Right: a 1–3 chain joins v1 to v3; together with v it forms a cycle (blue) that encloses v2 and leaves v4 outside, so the 2–4 chain from v2 (red) cannot reach v4, and swapping colors 2 and 4 on it suffices](./plots/five-color.py)

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
| Even cycle $C_{2k}$ | $2$ |
| Odd cycle $C_{2k+1}$ | $3$ |
| Tree ($n \ge 2$) | $2$ |

**Theorem 4.6.1** Let $G$ be a graph with at least one edge. Then $\gamma(G) = 2$ if and only if $G$ contains no odd cycle.

**Proof** Necessity: an odd cycle needs $3$ colors, so if $G$ contains an odd cycle, then $\gamma(G) \ge 3$.

Sufficiency: since each connected component can be colored separately, we may assume that $G$ is connected. Take a **spanning tree** $T$ of $G$ and $2$-color $T$ according to the parity of the distance in $T$ from a fixed vertex. Each chord $(u, v)$ forms a cycle with the path from $u$ to $v$ in $T$; by hypothesis this cycle has even length, so the path from $u$ to $v$ in $T$ has odd length, and $u, v$ receive different colors. Thus this coloring is also a proper coloring of $G$, and $\gamma(G) = 2$. $\square$

### 4.6.3. Upper Bounds on the Chromatic Number

Let $d_0 = \max_{v \in V} d(v)$ denote the maximum degree of $G$.

**Theorem 4.6.2** Every graph $G$ without loops satisfies $\gamma(G) \le d_0 + 1$.

**Proof** By induction on the number of vertices $n$. The claim holds for $n = 1$. Suppose it holds for graphs with $n-1$ vertices. Take any $v \in V(G)$ and let $G' = G - v$. The maximum degree $d_0'$ of $G'$ satisfies $d_0' \le d_0$, so by the induction hypothesis $\gamma(G') \le d_0' + 1 \le d_0 + 1$. When $v$ is put back, it has at most $d_0$ neighbors, which use at most $d_0$ colors, so one of the $d_0 + 1$ colors is still available for $v$. $\square$

This proof is the *greedy coloring* algorithm: arrange the vertices in some order and give each vertex in turn the smallest color not used by its already colored neighbors. It never uses more than $d_0 + 1$ colors, but the number it actually uses depends on the order. Ordering the vertices by decreasing degree (the Welsh–Powell algorithm) is a common rule of thumb, but it does not guarantee an optimal coloring either. Indeed, for $k \ge 3$ deciding whether a graph is $k$-colorable is NP-complete, and no polynomial-time algorithm for the chromatic number is known.

**Example 4.6.1** The crown graph is obtained from $K_{4,4}$ by deleting a perfect matching: its vertices are $x_1, \dots, x_4, y_1, \dots, y_4$, and $x_i$ is adjacent to $y_j$ if and only if $i \ne j$. It is bipartite, so $\gamma = 2$. Greedy coloring in the order $x_1, x_2, x_3, x_4, y_1, \dots, y_4$ uses $2$ colors. In the interleaved order $x_1, y_1, x_2, y_2, \dots$, however, $x_1$ and $y_1$ are nonadjacent and both receive color $1$, $x_2$ and $y_2$ are both adjacent to color $1$ and receive color $2$, and so on, for $4$ colors in all. In general, a bad order uses $k$ colors on $K_{k,k}$ minus a perfect matching, whose chromatic number is always $2$. All vertices have degree $3$, so the Welsh–Powell ordering does not help here.

![Two greedy colorings of the crown graph (K4,4 minus a perfect matching): the interleaved order uses 4 colors, the order with all x before all y only 2](./plots/greedy-coloring.py)

```python
# Greedy (sequential) coloring of the crown graph of Example 4.6.1
from itertools import product

xs, ys = ["x1", "x2", "x3", "x4"], ["y1", "y2", "y3", "y4"]
adj = {v: set() for v in xs + ys}
for x, y in product(xs, ys):
    if x[1] != y[1]:  # x_i ~ y_j for i != j
        adj[x].add(y)
        adj[y].add(x)


def greedy(order):
    """Give each vertex the smallest color not used by its colored neighbors."""
    color = {}
    for v in order:
        used = {color[u] for u in adj[v] if u in color}
        color[v] = next(c for c in range(1, len(order) + 1) if c not in used)
    return color


for order in ([v for p in zip(xs, ys) for v in p], xs + ys):
    color = greedy(order)
    print(" ".join(f"{v}:{color[v]}" for v in order), "->", max(color.values()), "colors")
```

```text
x1:1 y1:1 x2:2 y2:2 x3:3 y3:3 x4:4 y4:4 -> 4 colors
x1:1 x2:1 x3:1 x4:1 y1:2 y2:2 y3:2 y4:2 -> 2 colors
```

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

**Example 4.6.2** We compute the chromatic polynomial of the $4$-cycle $C_4 = v_1v_2v_3v_4$. The vertices $v_1, v_3$ are nonadjacent. Adding the edge $(v_1, v_3)$ gives $K_4$ minus an edge: $v_1$ is adjacent to $v_3$, and $v_2$, $v_4$ are both adjacent to $v_1$ and $v_3$ but not to each other; coloring $v_1, v_3, v_2, v_4$ in turn gives $t(t-1)(t-2)^2$ colorings. Merging $v_1$ and $v_3$ gives a path on $3$ vertices, a tree, with $t(t-1)^2$ colorings. Hence

$$
f(C_4, t) = t(t-1)(t-2)^2 + t(t-1)^2 = t(t-1)(t^2 - 3t + 3) = t^4 - 4t^3 + 6t^2 - 3t.
$$

Since $f(C_4, 1) = 0$ and $f(C_4, 2) = 2 > 0$, we get $\gamma(C_4) = 2$, in agreement with Theorem 4.6.1.

![Theorem 4.6.7 applied to C4: colorings with v1, v3 colored differently correspond to the graph with the added edge (red), those with v1, v3 colored alike to the merged graph (the red circle is the merged vertex)](./plots/chromatic-recursion.py)

The following program computes chromatic polynomials by the recursion of Theorem 4.6.7 (until only complete graphs remain). It confirms Example 4.6.2 and computes the polynomial of the wheel $W_5$, the dual graph of the map above: $f(W_5, 3) = 0$ and $f(W_5, 4) = 120$, so $\gamma(W_5) = 4$. The number of branches grows exponentially with the number of edges, so the method is suitable only for small graphs.

```python
# Chromatic polynomial by the recursion of Theorem 4.6.7: f(G) = f(G + uv) + f(G with u, v merged)
from itertools import combinations


def poly_mul(p, q):  # coefficient lists, lowest degree first
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def chromatic(vertices, edges):
    edges = {frozenset(e) for e in edges}
    pair = next((p for p in combinations(sorted(vertices), 2) if frozenset(p) not in edges), None)
    if pair is None:  # complete graph K_n: t(t-1)...(t-n+1)
        f = [1]
        for k in range(len(vertices)):
            f = poly_mul(f, [-k, 1])
        return f
    u, v = pair
    added = chromatic(vertices, edges | {frozenset(pair)})
    merged = {frozenset(u if x == v else x for x in e) for e in edges}  # v is renamed to u
    contracted = chromatic(vertices - {v}, merged)
    return [a + b for a, b in zip(added, contracted + [0])]


c4 = chromatic({1, 2, 3, 4}, [(1, 2), (2, 3), (3, 4), (4, 1)])
w5 = chromatic(set(range(6)), [(0, k) for k in range(1, 6)] + [(k, k % 5 + 1) for k in range(1, 6)])
print("C4 coefficients (t^0, t^1, ...):", c4)
print("W5 coefficients:", w5)
print("W5 colorings with t = 3, 4:", [sum(a * t**i for i, a in enumerate(w5)) for t in (3, 4)])
```

```text
C4 coefficients (t^0, t^1, ...): [0, -3, 6, -4, 1]
W5 coefficients: [0, -30, 79, -80, 40, -10, 1]
W5 colorings with t = 3, 4: [0, 120]
```

## Summary

- Basic relations for planar graphs:

  | Result | Statement | Use |
  | :-- | :-- | :-- |
  | Euler's formula (Theorem 4.1.1) | $n - m + d = 2$ for a connected plane graph; $n - m + d = k + 1$ with $k$ components (Corollary 4.1.1) | The basic relation among vertices, edges and faces |
  | Bound on edges (Theorem 4.1.2) | $m \le \frac{t(n-2)}{t-2}$ if there is no cut edge and every face has boundary length $\ge t$ | Bipartite graphs allow $t = 4$; the same argument shows that $K_{3,3}$ is nonplanar (Theorem 4.3.2) |
  | Maximal planar graphs (Theorem 4.2.1) | $m = 3n - 6$, $d = 2n - 4$; $m \le 3n - 6$ for every simple planar graph (Corollary 4.2.1) | A necessary condition for planarity, ruling out $K_5$ and $K_7$ (Theorem 4.3.1, Example 4.2.1) |
  | Minimum degree (Theorem 4.2.2) | A simple planar graph has a vertex of degree less than $6$ | The induction step of the five color theorem |
  | Kuratowski's theorem (Theorem 4.3.3) | Planar if and only if there is no $K$-type subgraph | A complete characterization of planar graphs |

- Planarity testing (Section 4.4): after splitting into components, deleting loops and multiple edges, splitting at cut vertices into blocks and reducing series vertices, a graph with $m < 9$ or $n < 5$ is planar and one with $m > 3n - 6$ is nonplanar; the remaining cases are handled by the DMP algorithm, which embeds the graph step by step.
- Dual graphs: every plane graph has a dual (Property 4.5.1), with $m = m^*$, $d = n^*$, $n = d^*$ (Property 4.5.4); cycles of $G$ correspond to cut sets of $G^*$ (Property 4.5.5), and the cycle matrix of a connected plane graph is the cut-set matrix of its dual. Coloring the faces of a map thus becomes coloring the vertices of the dual graph, and the five color theorem (Theorem 4.5.2) states that every loopless planar graph is $5$-colorable.
- Coloring:

  | Result | Statement |
  | :-- | :-- |
  | Two-colorable graphs (Theorem 4.6.1) | $\gamma(G) = 2$ if and only if $G$ has an edge and no odd cycle |
  | Upper bounds (Theorems 4.6.2 and 4.6.3) | $\gamma(G) \le d_0 + 1$, and the sharper $\gamma(G) \le 1 + \max_{G'} \delta(G')$ |
  | Greedy coloring (Example 4.6.1) | Give each vertex in turn the smallest available color: at most $d_0 + 1$ colors; the result depends on the order, and computing the chromatic number is NP-hard |
  | Recursive computation (Theorem 4.6.4) | $\gamma(G) = \min\{\gamma(\overline{G_{ij}}), \gamma(G_{ij})\}$: add an edge between, or merge, two nonadjacent vertices |
  | Chromatic polynomial (Definition 4.6.4, Theorem 4.6.7) | $f(G, t) = f(\overline{G_{ij}}, t) + f(G_{ij}, t)$, eventually a sum of chromatic polynomials of complete graphs; $\gamma(G)$ is the least positive integer $t$ with $f(G, t) > 0$ |
