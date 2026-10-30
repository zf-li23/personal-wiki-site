---
title: Graph Connectivity
source_hash: 97137064a7ff
---

[Chapter 2](/1.4.2) defined **connected graphs** and **connected components**, distinguishing only between "connected" and "disconnected". Applications such as communication networks, transportation planning and circuit design call for a finer measure of how well a graph is connected: if some nodes or links fail, does the network remain connected? In this chapter we introduce vertex connectivity and edge connectivity, establish Whitney's inequality relating them to the minimum degree, present Menger's theorem, which characterizes connectivity, together with its connection to the network flows of [Chapter 5](/1.4.5), and discuss $k$-connected graphs. We then return to the matrices that run through this course — the adjacency matrix $A$, incidence matrix $B$ and degree matrix $D$ of [Chapter 1](/1.4.1), and the Laplacian matrix $L = D - A = BB^{\mathsf T}$ of [Chapter 3](/1.4.3) — and use the second smallest eigenvalue of $L$ (the algebraic connectivity) as an algebraic measure of connectedness, with its eigenvector splitting the graph in two. Finally we discuss applications of connectivity to network design and the wide diameter.

## 6.1. Vertex Connectivity and Edge Connectivity

### 6.1.1. Vertex Cuts and Cut Vertices

To measure connectivity we must first make precise what it means to destroy it: deleting some vertices or edges increases the number of connected components.

**Definition 6.1.1 (Vertex Cut)** Let $G = (V, E)$ be a connected undirected graph and $\varnothing \ne V' \subset V$. If $G - V'$ is disconnected, but the graph remains connected after deleting any proper subset of $V'$, then $V'$ is called a **vertex cut** of $G$. A vertex cut with $k$ vertices is called a **$k$-vertex cut**. The vertex cuts of a graph may have different sizes.

**Definition 6.1.2 (Cut Vertex)** If $\{v\}$ is a vertex cut of $G$, that is, deleting the vertex $v$ disconnects the graph, then $v$ is called a **cut vertex** (or articulation point) of $G$.

**Example 6.1.1** In a **tree** with $n \ge 3$ vertices, every vertex that is not a **leaf** is a cut vertex. The **complete graph** $K_n$ has no cut vertex, since deleting a vertex leaves $K_{n-1}$, which is still connected.

**Definition 6.1.3 (Block)** A connected graph without cut vertices is called a **nonseparable graph**. A maximal connected subgraph of a graph $G$ that has no cut vertex (of its own) is called a **block** of $G$.

### 6.1.2. Edge Cuts and Bridges

**Definition 6.1.4 (Edge Cut)** Let $G = (V, E)$ be a connected undirected graph and $\varnothing \ne E' \subseteq E$. If $G - E'$ is disconnected, but the graph remains connected after deleting any proper subset of $E'$, then $E'$ is called an **edge cut** of $G$; this is the **cut set** of Definition 3.4.4 in the undirected setting. An edge cut with $k$ edges is called a **$k$-edge cut**.

**Definition 6.1.5 (Bridge)** If $\{e\}$ is an edge cut of $G$, that is, deleting the edge $e$ disconnects the graph, then $e$ is called a **bridge** of $G$, which is the same as a **cut edge**.

By Theorem 3.1.1, an edge is a bridge if and only if it lies on no **cycle** of $G$.

**Example 6.1.2** In a tree, every edge is a bridge. The **cycle** $C_n$ with $n \ge 3$ vertices has no bridge, since deleting any edge leaves the **path** $P_n$ with $n$ vertices, which is still connected.

**Example 6.1.3** The graph on the left of the figure below is assembled from the triangle $abc$, the edge $cd$, the quadrilateral $defg$ and the triangle $fhi$. Its cut vertices are $c$, $d$ and $f$, and its only bridge is $cd$; the edges of the triangles $abc$, $fhi$ and of the quadrilateral $defg$ lie on cycles and are not bridges. Pulling the graph apart at its cut vertices gives the four blocks on the right: $\{a, b, c\}$, $\{c, d\}$, $\{d, e, f, g\}$ and $\{f, h, i\}$. Neighboring blocks share exactly one cut vertex, and a bridge together with its two ends forms a block by itself.

![Left: the cut vertices c, d, f (red rings) and the bridge cd (red edge); right: the four blocks obtained by pulling the graph apart at its cut vertices; no block has a cut vertex, and neighboring blocks share one cut vertex](./plots/cut-vertices-blocks.py)

### 6.1.3. Definitions of Vertex Connectivity and Edge Connectivity

**Definition 6.1.6 (Vertex Connectivity)** The **vertex connectivity** $\kappa(G)$ of a graph $G$ is the minimum number of vertices whose deletion makes $G$ disconnected or trivial (a graph with a single vertex). If $G$ is disconnected or trivial, then $\kappa(G) = 0$. When $G$ is connected and not complete, $\kappa(G)$ is the size of a smallest vertex cut; for complete graphs, $\kappa(K_n) = n-1$.

**Definition 6.1.7 (Edge Connectivity)** The **edge connectivity** $\lambda(G)$ of a graph $G$ is the minimum number of edges whose deletion makes $G$ disconnected. If $G$ is disconnected or trivial, then $\lambda(G) = 0$. When $G$ is connected and nontrivial, $\lambda(G)$ is the size of a smallest edge cut.

**Remark** Vertex connectivity is often simply called the connectivity of the graph. $\kappa(G) = 0$ means that $G$ is disconnected or trivial, and $\kappa(G) \ge 1$ is (nontrivial) connectedness in the usual sense.

**Example 6.1.4**

- The complete graph $K_n$ ($n \ge 2$): $\kappa(K_n) = \lambda(K_n) = n-1$. Deleting the $n-1$ edges at any vertex isolates that vertex; on the other hand, if the vertices are split into two parts of sizes $p$ and $n-p$ ($1 \le p \le n-1$), there are $p(n-p) \ge n-1$ edges between the parts, so fewer than $n-1$ edges cannot disconnect $K_n$.
- A tree $T$ ($n \ge 2$): $\kappa(T) = \lambda(T) = 1$, since a tree has bridges; for $n \ge 3$ it also has cut vertices.
- The cycle $C_n$ ($n \ge 3$): $\kappa(C_n) = \lambda(C_n) = 2$. Deleting any single vertex or edge leaves a path, which is still connected; deleting two nonadjacent vertices (for $n = 3$, deleting two vertices leaves a trivial graph) or any two edges disconnects the graph.
- The **complete bipartite graph** $K_{r,s}$ ($1 \le r \le s$): its minimum degree is $r$, and $\kappa(K_{r,s}) = \lambda(K_{r,s}) = r$. Deleting the side with $r$ vertices leaves $s$ mutually nonadjacent vertices.
- The Petersen graph is the classic example of a $3$-regular graph (every vertex has degree $3$); its vertex connectivity and edge connectivity are both $3$.

![Vertex and edge connectivity of five common graphs: the complete graph K5, a tree (red rings mark its cut vertices, the non-leaf vertices), the cycle C6, the complete bipartite graph K2,3 (blue: the smaller side, whose deletion disconnects the graph) and the Petersen graph](./plots/connectivity-examples.py)

## 6.2. Whitney's Inequality

The quantitative relation between vertex connectivity and edge connectivity was established by Whitney in 1932 and is known as *Whitney's inequality*. Let $\delta(G)$ denote the minimum degree of the vertices of $G$.

**Theorem 6.2.1 (Whitney's Inequality)** Every graph $G$ satisfies

$$
\kappa(G) \le \lambda(G) \le \delta(G).
$$

**Proof** If $G$ is disconnected or trivial, then $\kappa(G) = \lambda(G) = 0$ and the claim holds. Assume now that $G$ is connected and $n \ge 2$.

First we show $\lambda(G) \le \delta(G)$. Let $v$ be a vertex of minimum degree, $d(v) = \delta(G)$. Deleting all $\delta(G)$ edges incident with $v$ isolates $v$ and disconnects the graph, so $\lambda(G) \le \delta(G)$.

Next we show $\kappa(G) \le \lambda(G)$. Let $S$ be a minimum edge cut of $G$, $|S| = \lambda(G)$. Deleting $S$ splits the vertices into two parts $X$ and $Y = V \setminus X$, and $S$ consists of all edges between $X$ and $Y$. There are two cases:

1. Every vertex of $X$ is adjacent to every vertex of $Y$. Then $\lambda(G) = |S| = |X||Y| \ge n - 1$, while always $\kappa(G) \le n-1$, so the claim holds.
2. Some $x \in X$ and $y \in Y$ are nonadjacent. For each edge of $S$, take its endpoint in $X$ if that endpoint is not $x$; otherwise (the edge has the form $(x, y')$ with $y' \in Y$, and $y' \ne y$) take its endpoint $y'$ in $Y$. Let $T$ be the set of vertices so chosen. Then $|T| \le |S|$ and $x, y \notin T$. Every path from $x$ to $y$ in $G$ uses some edge of $S$, and that edge always has an endpoint in $T$, which is neither $x$ nor $y$; hence $x$ and $y$ are disconnected in $G - T$. Therefore $\kappa(G) \le |T| \le |S| = \lambda(G)$. $\square$

**Example 6.2.1** If $G$ is a $3$-regular graph, then $\delta(G) = 3$, so $\kappa(G) \le \lambda(G) \le 3$. The Petersen graph satisfies $\kappa = \lambda = \delta = 3$, so both inequalities in Whitney's inequality hold with equality.

**Example 6.2.2** Both inequalities in Whitney's inequality can be strict. Join two copies of $K_4$ (on the vertices $a, b, c, d$ and $e, f, g, h$) by the two edges $de$ and $df$, giving a graph $G$ on $8$ vertices. Deleting $d$ separates $\{a, b, c\}$ from $\{e, f, g, h\}$, so $\kappa(G) = 1$; deleting any single edge leaves the graph connected, while deleting $de$ and $df$ disconnects it, so $\lambda(G) = 2$; every vertex has degree at least $3$, so $\delta(G) = 3$. Hence $\kappa(G) < \lambda(G) < \delta(G)$. We shall use this graph again in Section 6.5.

![The graph of Example 6.2.2: two copies of K4 joined by the edges de and df. Left: deleting the cut vertex d (dashed: its incident edges); middle: the minimum edge cut {de, df}; right: the vertex a of minimum degree with its three edges](./plots/kappa-lambda-delta.py)

The engineering meaning of Whitney's inequality is that a network's ability to withstand node failures ($\kappa$) is no greater than its ability to withstand link failures ($\lambda$), which in turn is no greater than the number of connections of its weakest node ($\delta$). When $\kappa < \lambda$, deleting a few nodes disconnects the network more easily than deleting the same number of links; when $\lambda < \delta$, the network contains a "bottleneck" set of edges that is weaker than the connections of any single node.

## 6.3. Menger's Theorem

*Menger's theorem*, proved by Menger in 1927, is one of the central results of connectivity theory. It relates connectivity to the number of disjoint paths between two vertices.

### 6.3.1. Two Forms of the Theorem

**Definition 6.3.1 (Internally Disjoint and Edge-Disjoint Paths)** Let $x$ and $y$ be two distinct vertices of a graph $G$.

- Two paths from $x$ to $y$ are said to be **internally disjoint** if they have no common vertex other than the ends $x$ and $y$.
- Two paths from $x$ to $y$ are said to be **edge-disjoint** if they have no common edge (they may share vertices).

A family of paths is called internally disjoint (edge-disjoint) if its members are pairwise internally disjoint (edge-disjoint).

**Theorem 6.3.1 (Menger's Theorem, Vertex Form)** Let $x$ and $y$ be two distinct nonadjacent vertices of a finite undirected graph $G$. Then the maximum number of internally disjoint paths between $x$ and $y$ equals the minimum number of vertices (other than $x$ and $y$ themselves) whose deletion disconnects $x$ from $y$.

**Theorem 6.3.2 (Menger's Theorem, Edge Form)** Let $x$ and $y$ be two distinct vertices of a finite undirected graph $G$. Then the maximum number of edge-disjoint paths between $x$ and $y$ equals the minimum number of edges whose deletion disconnects $x$ from $y$.

One half of each theorem, "$\le$", is obvious: every path must lose at least one inner vertex (one edge), so separating $x$ from $y$ requires deleting at least as many vertices (edges) as there are disjoint paths. The substance of the theorem is that equality is always attained.

**Example 6.3.1** In the figure below, $x$ and $y$ are joined by the three internally disjoint paths $xady$, $xbey$ and $xcfy$; on the other hand, deleting $\{a, b, c\}$ isolates $x$ from $y$. Both numbers equal $3$, in accordance with Theorem 6.3.1: there is no fourth internally disjoint path, and no two vertices whose deletion separates $x$ from $y$.

![An example of Menger's theorem. Left: three internally disjoint x–y paths (three colors); right: the set {a, b, c} of size 3 (red) separates x from y; the dashed edges are deleted together with these vertices](./plots/menger.py)

### 6.3.2. Menger's Theorem and Connectivity

**Corollary 6.3.1 (Whitney)** Let $G$ be a graph with $n \ge k+1$ vertices. Then $G$ is $k$-vertex-connected ($\kappa(G) \ge k$) if and only if any two distinct vertices of $G$ are joined by at least $k$ internally disjoint paths.

**Proof** Sufficiency: if any two vertices are joined by $k$ internally disjoint paths, then after deleting fewer than $k$ vertices, each pair of remaining vertices is still joined by at least one of these paths, so the graph remains connected and $\kappa(G) \ge k$.

Necessity: suppose $\kappa(G) \ge k$. For nonadjacent vertices $x, y$, at least $k$ vertices must be deleted to disconnect them, so by Theorem 6.3.1 they are joined by $k$ internally disjoint paths. For adjacent vertices $x, y$, let $e = (x, y)$; we first show that $\kappa(G - e) \ge k - 1$. Otherwise there is a vertex set $T$ with $|T| \le k-2$ such that $(G - e) - T$ is disconnected (since $n \ge k+1$, at least $3$ vertices remain, so the graph is not trivial). Since $|T| < k$, the graph $G - T$ is connected, so $e$ is a bridge of $G - T$: the graph $(G - e) - T$ has exactly two components $X \ni x$ and $Y \ni y$, joined in $G - T$ only by $e$. Together they have at least $3$ vertices; say $|X| \ge 2$. Then deleting $T \cup \{x\}$ separates $X \setminus \{x\}$ from $Y$, and $|T \cup \{x\}| \le k - 1$, contradicting $\kappa(G) \ge k$. Thus $x, y$ are nonadjacent in $G - e$ and at least $k-1$ vertices must be deleted to disconnect them; Theorem 6.3.1 gives $k-1$ internally disjoint paths, and together with the edge $e$ itself there are $k$. $\square$

Similarly, Theorem 6.3.2 shows that $G$ is $k$-edge-connected ($\lambda(G) \ge k$) if and only if any two distinct vertices of $G$ are joined by at least $k$ edge-disjoint paths.

### 6.3.3. Menger's Theorem and Network Flows

Menger's theorem is closely related to the **max-flow min-cut theorem** (Theorem 5.5.2); each can be derived from the other. Take the edge form as an example: replace each edge of the undirected graph by two oppositely directed edges of capacity $1$, and take $x$ as the source and $y$ as the sink. Then the maximum flow value is the maximum number of edge-disjoint paths between $x$ and $y$, and the minimum cut capacity is the minimum number of edges whose deletion disconnects $x$ from $y$. For the vertex form, we additionally split each vertex $v$ other than $x, y$ into two vertices $v_{\mathrm{in}}$ and $v_{\mathrm{out}}$ joined by an edge $(v_{\mathrm{in}}, v_{\mathrm{out}})$ of capacity $1$; edges that entered $v$ now enter $v_{\mathrm{in}}$, edges that left $v$ now leave $v_{\mathrm{out}}$, and these directed edges coming from edges of the original graph receive capacity $\infty$ (or a sufficiently large number). Then each vertex carries at most one unit of flow, so the maximum flow value is the maximum number of internally disjoint paths; and a cut of finite capacity can consist only of edges of the form $(v_{\mathrm{in}}, v_{\mathrm{out}})$, so the minimum cut capacity is the minimum number of vertices whose deletion disconnects $x$ from $y$.

![Turning internally disjoint paths into unit flows. Left: an undirected graph; right: each inner vertex u, v is split into an arc of capacity 1 (red), and every edge of the original graph becomes two opposite arcs of infinite capacity](./plots/vertex-splitting.py)

## 6.4. $k$-Connected Graphs

### 6.4.1. Definition of $k$-Connectivity

**Definition 6.4.1 ($k$-Connected Graph)** Let $k \ge 1$ be an integer. A graph $G$ with $\kappa(G) \ge k$ is said to be **$k$-vertex-connected**, or simply a **$k$-connected graph**; if $\lambda(G) \ge k$, it is said to be **$k$-edge-connected**. Since $\kappa(G) \le n-1$, a $k$-connected graph has at least $k+1$ vertices.

- The $1$-connected graphs are exactly the nontrivial connected graphs.
- The $2$-connected graphs are exactly the connected graphs with $n \ge 3$ vertices and no cut vertex.
- A $k$-connected graph remains connected after deleting any fewer than $k$ vertices; a $k$-edge-connected graph remains connected after deleting any fewer than $k$ edges.

### 6.4.2. A Characterization of $2$-Connected Graphs

**Theorem 6.4.1** Let $G$ be a connected graph with $n \ge 3$ vertices. The following statements are equivalent:

1. $G$ is $2$-connected, that is, it has no cut vertex;
2. any two vertices of $G$ are joined by at least two internally disjoint paths;
3. any two vertices of $G$ lie on a common cycle.

**Proof** (1)→(2): by Corollary 6.3.1. (2)→(3): two internally disjoint paths together form a cycle through the two vertices. (3)→(1): if any two vertices lie on a common cycle, then after deleting any single vertex, any two of the remaining vertices are still joined by a path (a broken cycle still leaves a path between them); so there is no cut vertex, and since $n \ge 3$, $G$ is $2$-connected. $\square$

### 6.4.3. Minimally $k$-Connected Graphs

**Definition 6.4.2 (Minimally $k$-Connected Graph)** A $k$-connected graph $G$ that is no longer $k$-connected after deleting any edge is called a **minimally $k$-connected graph**.

Minimally $k$-connected graphs are among the objects studied in extremal graph theory. For example, Halin (1969) proved that every minimally $k$-connected graph has a vertex of degree $k$; Mader went further, proving that such graphs have many vertices of degree $k$, and gave an upper bound on their number of edges.

### 6.4.4. Connectivity of Complete Graphs

The complete graph $K_n$ ($n \ge 2$) satisfies $\kappa(K_n) = \lambda(K_n) = \delta(K_n) = n-1$, so $K_n$ is $(n-1)$-connected and has the highest connectivity among graphs on $n$ vertices. But it has $\frac{1}{2}n(n-1)$ edges, which is often too costly in practical network design.

### 6.4.5. Computing Connectivity

By Menger's theorem, $\kappa(G)$ and $\lambda(G)$ can be computed by solving maximum flow problems between suitable pairs of vertices, so both can be found in polynomial time. Since $\kappa$ and $\lambda$ are integers, they only answer "how few must be deleted"; the next section gives a continuous measure from the point of view of matrices.

## 6.5. Algebraic Connectivity

Vertex and edge connectivity only look at the weakest spot: a long path and a star both have $\kappa = 1$, yet the former is much more loosely knit. Spectral graph theory describes the shape of a graph by the eigenvalues of its matrices. In this section we return to the adjacency matrix $A$, incidence matrix $B$ and degree matrix $D = \operatorname{diag}(d(v_1), \dots, d(v_n))$ of [Chapter 1](/1.4.1), and to the **Laplacian matrix** of the matrix-tree theorem in [Chapter 3](/1.4.3),

$$
L = D - A = BB^{\mathsf T},
$$

where $B$ is the incidence matrix with respect to an arbitrary orientation of the edges (the column of an edge $e = (u, v)$ has $1$ in row $u$ and $-1$ in row $v$). Throughout this section $G$ is a simple undirected graph with $n$ vertices numbered $1, \dots, n$; a vector $\boldsymbol{x} \in \mathbb{R}^n$ is viewed as an assignment of a real number $x_v$ to each vertex, and $\boldsymbol{1}$ is the all-ones vector. To avoid confusion with the edge connectivity $\lambda(G)$, we denote the eigenvalues of $L$ by $\mu$.

### 6.5.1. The Quadratic Form and Spectrum of the Laplacian

**Proposition 6.5.1** For every $\boldsymbol{x} \in \mathbb{R}^n$,

$$
\boldsymbol{x}^{\mathsf T}L\boldsymbol{x} = \sum_{(u, v) \in E} (x_u - x_v)^2 .
$$

Hence $L$ is a real symmetric **positive semidefinite matrix**, its eigenvalues can be ordered as $0 = \mu_1 \le \mu_2 \le \cdots \le \mu_n$, and $L\boldsymbol{1} = \boldsymbol{0}$.

**Proof** $\boldsymbol{x}^{\mathsf T}L\boldsymbol{x} = \boldsymbol{x}^{\mathsf T}BB^{\mathsf T}\boldsymbol{x} = \|B^{\mathsf T}\boldsymbol{x}\|^2$, and the component of $B^{\mathsf T}\boldsymbol{x}$ belonging to the edge $e = (u, v)$ is $x_u - x_v$, which gives the identity. It is nonnegative, so $L$ is positive semidefinite ([Proposition 7.3.2](/2.1.7#thm-7.3.2)) and its eigenvalues are nonnegative. Each row of $L$ sums to $d(v) - d(v) = 0$, so $L\boldsymbol{1} = \boldsymbol{0}$ and $0$ is the smallest eigenvalue. $\square$

The quadratic form $\sum_{(u,v) \in E}(x_u - x_v)^2$ can be read as the potential energy of a spring system: each edge is a spring pulling the values at its two ends together. The next proposition shows that the multiplicity of the eigenvalue $0$ is exactly the number of mutually disconnected pieces of the graph.

**Proposition 6.5.2** The multiplicity of the eigenvalue $0$ of $L$ equals the number of connected components of $G$.

**Proof** By Proposition 6.5.1, $L\boldsymbol{x} = \boldsymbol{0}$ implies $\boldsymbol{x}^{\mathsf T}L\boldsymbol{x} = 0$, that is, $x_u = x_v$ at the two ends of every edge; conversely, $B^{\mathsf T}\boldsymbol{x} = \boldsymbol{0}$ implies $L\boldsymbol{x} = B(B^{\mathsf T}\boldsymbol{x}) = \boldsymbol{0}$. Thus $L\boldsymbol{x} = \boldsymbol{0}$ if and only if $\boldsymbol{x}$ is constant along every edge, that is, constant on each connected component. If the components of $G$ have vertex sets $V_1, \dots, V_c$, the null space of $L$ is spanned by $\boldsymbol{1}_{V_1}, \dots, \boldsymbol{1}_{V_c}$ and has dimension $c$. Since $L$ is real symmetric, it is orthogonally diagonalizable, and the multiplicity of an eigenvalue equals the dimension of its eigenspace. $\square$

### 6.5.2. Algebraic Connectivity and the Rayleigh Quotient

**Definition 6.5.1 (Algebraic Connectivity)** Let $G$ have $n \ge 2$ vertices. The second smallest eigenvalue $\mu_2$ of the Laplacian matrix of $G$ is called the **algebraic connectivity** of $G$ and is denoted by $a(G)$. The notion was introduced by Fiedler in 1973.

**Theorem 6.5.1 (Fiedler)** $a(G) > 0$ if and only if $G$ is connected.

**Proof** By Proposition 6.5.2, $\mu_2 > 0$ if and only if the eigenvalue $0$ is simple, if and only if $G$ has a single connected component. $\square$

Thus $a(G)$, like $\kappa(G)$, vanishes for disconnected graphs, and its size measures further "how firmly" the graph holds together. Its variational characterization comes from [Theorem 7.2.1](/2.1.7#thm-7.2.1) (the extremal characterization of the eigenvalues of a real symmetric matrix).

**Theorem 6.5.2 (Rayleigh Quotient Characterization of Algebraic Connectivity)** For a graph $G$ with $n \ge 2$ vertices,

$$
a(G) = \min_{\substack{\boldsymbol{x} \ne \boldsymbol{0} \\ \boldsymbol{x} \perp \boldsymbol{1}}} \frac{\boldsymbol{x}^{\mathsf T}L\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}} = \min_{\substack{\boldsymbol{x} \ne \boldsymbol{0} \\ \sum_v x_v = 0}} \frac{\sum_{(u, v) \in E}(x_u - x_v)^2}{\sum_{v} x_v^2},
$$

and the minimum is attained exactly at the eigenvectors of $L$ belonging to $a(G)$.

**Proof** Order the eigenvalues of $L$ decreasingly as in [Theorem 7.2.1](/2.1.7#thm-7.2.1). The smallest eigenvalue $0$ has the unit eigenvector $\boldsymbol{q}_n = \boldsymbol{1}/\sqrt{n}$, and the second to last is $\mu_2$. Take $i = n-1$ there: $\operatorname{span}(\boldsymbol{q}_1, \dots, \boldsymbol{q}_{n-1})$ is the **orthogonal complement** of $\boldsymbol{q}_n$, namely $\{\boldsymbol{x} : \boldsymbol{x} \perp \boldsymbol{1}\}$, and the minimum of the **Rayleigh quotient** on it is $\mu_2$. If $\boldsymbol{x} \perp \boldsymbol{1}$ attains the minimum, expanding $\boldsymbol{x}$ in eigenvectors shows that it can only have components belonging to $\mu_2$. Finally, Proposition 6.5.1 rewrites the numerator. $\square$

Intuitively: we assign to the vertices numbers with mean $0$ and sum of squares $1$, keeping adjacent numbers as close as possible. If the graph has a "bottleneck", we can give positive values on one side and negative values on the other, so that only a few edges are stretched; the Rayleigh quotient, and hence $a(G)$, is then small.

**Example 6.5.1** Laplacian eigenvalues of some families of graphs:

| Graph | Laplacian eigenvalues | $a(G)$ | $\kappa(G)$ |
|---|---|---|---|
| $K_n$ | $0$, $n$ (multiplicity $n-1$) | $n$ | $n-1$ |
| path $P_n$ | $2 - 2\cos\frac{k\pi}{n}$, $k = 0, \dots, n-1$ | $2\left(1 - \cos\frac{\pi}{n}\right)$ | $1$ |
| cycle $C_n$ | $2 - 2\cos\frac{2k\pi}{n}$, $k = 0, \dots, n-1$ | $2\left(1 - \cos\frac{2\pi}{n}\right)$ | $2$ |
| star $K_{1,s}$ ($s \ge 2$) | $0$, $1$ (multiplicity $s-1$), $s+1$ | $1$ | $1$ |
| $K_{r,s}$ ($1 \le r \le s$, $s \ge 2$) | $0$, $r$ (multiplicity $s-1$), $s$ (multiplicity $r-1$), $r+s$ | $r$ | $r$ |
| Petersen graph | $0$, $2$ (multiplicity $5$), $5$ (multiplicity $4$) | $2$ | $3$ |

For $K_n$: $L = nI_n - J$ ($J$ the all-ones matrix), and $J\boldsymbol{x} = \boldsymbol{0}$ for $\boldsymbol{x} \perp \boldsymbol{1}$, so $L\boldsymbol{x} = n\boldsymbol{x}$. For $C_n$ (vertices $0, 1, \dots, n-1$ adjacent in cyclic order): $x_j = \cos\frac{2k\pi j}{n}$ satisfies $(L\boldsymbol{x})_j = 2x_j - x_{j-1} - x_{j+1} = \left(2 - 2\cos\frac{2k\pi}{n}\right)x_j$, and so does the sine, which gives all eigenvalues. For $P_n$ the eigenvectors are $x_j = \cos\frac{k\pi(j - 1/2)}{n}$ ($j = 1, \dots, n$), which can be checked in the same way.

$a(P_n) \approx \pi^2/n^2$ tends to $0$ as $n$ grows, whereas $\kappa(P_n) = 1$ stays fixed: the algebraic connectivity also reflects the "size" and "slenderness" of a graph. In general, Mohar (1991) proved that a connected graph satisfies $a(G) \ge \frac{4}{n \operatorname{diam}(G)}$, where $\operatorname{diam}(G)$ is the diameter (the maximum distance between two vertices): a graph of small diameter cannot have very small algebraic connectivity.

![All Laplacian eigenvalues (gray dots) of several graphs, with the algebraic connectivity a(G) (red dot) and the vertex connectivity κ(G) (blue tick). In every row the red dot lies on or to the left of the blue tick; for K3,5 and the star K1,7, a(G) equals κ(G)](./plots/laplacian-spectra.py)

### 6.5.3. Fiedler's Inequality

We now prove that the algebraic connectivity does not exceed the vertex connectivity, which extends Whitney's inequality by one more link on the left. The key point is that deleting a vertex decreases $a(G)$ by at most $1$.

**Lemma 6.5.1** Let $G$ have $n \ge 3$ vertices and let $v$ be a vertex of $G$. Then $a(G) \le a(G - v) + 1$.

**Proof** Let $\boldsymbol{y} \in \mathbb{R}^{n-1}$ be a unit eigenvector of the Laplacian of $G - v$ belonging to $a(G - v)$; by Theorem 6.5.2, $\sum_u y_u = 0$ and $\sum_{(u,w) \in E(G - v)}(y_u - y_w)^2 = a(G - v)$. Extend it to $\boldsymbol{x} \in \mathbb{R}^n$ by $x_v = 0$ and $x_u = y_u$ otherwise. Then $\boldsymbol{x} \perp \boldsymbol{1}$, $\boldsymbol{x}^{\mathsf T}\boldsymbol{x} = 1$, and

$$
\boldsymbol{x}^{\mathsf T}L_G\boldsymbol{x} = \sum_{(u,w) \in E(G - v)}(y_u - y_w)^2 + \sum_{u \in N(v)} (y_u - 0)^2 \le a(G - v) + \sum_{u \ne v} y_u^2 = a(G - v) + 1 .
$$

By Theorem 6.5.2, $a(G) \le \boldsymbol{x}^{\mathsf T}L_G\boldsymbol{x} \le a(G - v) + 1$. $\square$

**Theorem 6.5.3 (Fiedler's Inequality)** If $G$ is not a complete graph, then $a(G) \le \kappa(G)$. Combined with Whitney's inequality (Theorem 6.2.1),

$$
a(G) \le \kappa(G) \le \lambda(G) \le \delta(G).
$$

**Proof** If $G$ is disconnected, then $a(G) = 0 = \kappa(G)$ by Theorem 6.5.1. Let $G$ be connected and not complete. Then $G$ has nonadjacent vertices $x, y$, and deleting all other vertices separates them, so vertex cuts exist. Take a minimum vertex cut $S = \{v_1, \dots, v_k\}$, $k = \kappa(G)$. Since $G - S$ is disconnected, it has at least $2$ vertices, so every graph in the process of deleting $v_1, \dots, v_k$ one at a time has at least $3$ vertices, and Lemma 6.5.1 applies repeatedly:

$$
a(G) \le a(G - v_1) + 1 \le \cdots \le a(G - S) + k = 0 + \kappa(G),
$$

where the last step uses Theorem 6.5.1. $\square$

Complete graphs violate this inequality: $a(K_n) = n > n - 1 = \kappa(K_n)$. What holds for all graphs is the following comparison with the minimum degree; its proof only substitutes a vector "concentrated at one vertex" into the Rayleigh quotient.

**Proposition 6.5.3 (Fiedler)** For a graph $G$ with $n \ge 2$ vertices, $a(G) \le \frac{n}{n-1}\,\delta(G)$.

**Proof** Let $d(v) = \delta(G)$ and take $\boldsymbol{x} = \boldsymbol{e}_v - \frac{1}{n}\boldsymbol{1}$. Then $\boldsymbol{x} \perp \boldsymbol{1}$ and $\boldsymbol{x}^{\mathsf T}\boldsymbol{x} = \left(1 - \frac1n\right)^2 + \frac{n-1}{n^2} = \frac{n-1}{n}$. The values of $\boldsymbol{x}$ differ only across the edges at $v$, by $1$, so $\boldsymbol{x}^{\mathsf T}L\boldsymbol{x} = d(v)$. Theorem 6.5.2 gives $a(G) \le \frac{n}{n-1}d(v)$. $\square$

Equality holds for $K_n$: $a(K_n) = n = \frac{n}{n-1}(n-1)$. The same idea gives a lower bound on the size of edge cuts:

**Proposition 6.5.4** For every nonempty proper subset $S$ of $V$, let $\partial S$ be the set of edges with one end in $S$ and the other in $V \setminus S$. Then

$$
|\partial S| \ge a(G)\,\frac{|S|\,|V \setminus S|}{n}.
$$

**Proof** Let $s = |S|$ and take $\boldsymbol{x} = \boldsymbol{1}_S - \frac{s}{n}\boldsymbol{1}$, that is, the value $1 - \frac{s}{n}$ on $S$ and $-\frac{s}{n}$ elsewhere. Then $\boldsymbol{x} \perp \boldsymbol{1}$; only the edges of $\partial S$ have different values at their ends (differing by $1$), so $\boldsymbol{x}^{\mathsf T}L\boldsymbol{x} = |\partial S|$; and $\boldsymbol{x}^{\mathsf T}\boldsymbol{x} = s\left(1 - \frac{s}{n}\right)^2 + (n - s)\frac{s^2}{n^2} = \frac{s(n-s)}{n}$. The claim follows from Theorem 6.5.2. $\square$

In particular, splitting $n$ (even) vertices into two equal halves cuts at least $a(G)\,n/4$ edges. A graph of large algebraic connectivity has no "bottleneck": every way of splitting the vertices into two large parts cuts many edges. A family of graphs of bounded degree whose algebraic connectivity stays away from $0$ is called a family of expander graphs; such graphs achieve strong connectivity with very few edges and are a theoretical tool for building highly fault-tolerant networks.

**Example 6.5.2** For the graph of Example 6.2.2 (two copies of $K_4$ joined by $de$ and $df$), a numerical computation (see the code in Section 6.5.4) gives $a(G) \approx 0.628$, so

$$
a(G) \approx 0.628 < \kappa(G) = 1 < \lambda(G) = 2 < \delta(G) = 3,
$$

with every link of the chain strict. If the two copies are joined by the single edge $de$ instead, $\kappa$ and $\lambda$ both equal $1$, while $a(G)$ drops to $3 - \sqrt{7} \approx 0.354$: the algebraic connectivity distinguishes "joined by one edge" from "joined by two edges sharing the vertex $d$", whereas the vertex connectivity does not.

### 6.5.4. The Fiedler Vector and Graph Bisection

**Definition 6.5.2 (Fiedler Vector)** An eigenvector of the Laplacian of a connected graph $G$ belonging to $a(G)$ is called a **Fiedler vector** of $G$.

Splitting the $n$ vertices into two halves so as to cut as few edges as possible is the *graph bisection* problem, which arises in task partitioning for parallel computing, circuit layout and image segmentation, and is NP-hard in general. The Fiedler vector is its continuous relaxation: if only $x_v = \pm 1$ is allowed ($1$ on $S$ and $-1$ elsewhere), then

$$
\sum_{(u,v) \in E}(x_u - x_v)^2 = 4|\partial S|, \qquad \sum_v x_v = 0 \iff |S| = \frac{n}{2},
$$

so the bisection problem minimizes the Rayleigh quotient of Theorem 6.5.2 over these vectors. Relaxing to arbitrary real vectors, the optimum is the Fiedler vector. Splitting the vertices by the signs of the components of the Fiedler vector (or at their median) is called *spectral bisection*. The following theorem guarantees that both parts obtained in this way are connected.

**Theorem 6.5.4 (Fiedler, 1975)** Let $G$ be connected and let $\boldsymbol{x}$ be a Fiedler vector of $G$. Then the subgraphs induced by $\{v : x_v \ge 0\}$ and by $\{v : x_v \le 0\}$ are both connected.

The proof uses the Perron–Frobenius theory of nonnegative matrices and is omitted here.

**Example 6.5.3** The figure below shows the Fiedler vectors of three graphs on $10$ vertices:

- The path $P_{10}$: the components $x_j \propto \cos\frac{\pi(j - 1/2)}{10}$ vary monotonically from one end to the other, and the signs cut the path in the middle (one edge cut).
- The cycle $C_{10}$: $a(C_{10})$ is a double eigenvalue, so the Fiedler vector is not unique; every rotation of $\cos\frac{2\pi j}{10}$ is one. Each of them splits the cycle into two equal arcs (two edges cut); by symmetry nothing determines where the cut falls.
- Two copies of $K_5$ joined by an edge: the components are nearly constant within each clique and change sign exactly at the bridge between them; $a(G) \approx 0.298$ is small, reflecting the single bottleneck.

![Fiedler vectors of three graphs on 10 vertices. Top: vertex colors show the components (blue negative, red positive, gray near zero); bottom: the component at each vertex. For the path and the cycle the components follow a cosine; for two cliques joined by an edge they are nearly constant within each clique and change sign at the bridge](./plots/fiedler-vectors.py)

Computing the Laplacian spectrum and the Fiedler vector of the graph of Example 6.2.2 with numpy, and bisecting by sign:

```python
import numpy as np

# Two copies of K4 joined by the edges d-e and d-f
V = "abcdefgh"
E = [("a", "b"), ("a", "c"), ("a", "d"), ("b", "c"), ("b", "d"), ("c", "d"),
     ("e", "f"), ("e", "g"), ("e", "h"), ("f", "g"), ("f", "h"), ("g", "h"),
     ("d", "e"), ("d", "f")]
idx = {v: i for i, v in enumerate(V)}
n = len(V)

# Oriented incidence matrix B (n x m): +1 at the tail, -1 at the head
B = np.zeros((n, len(E)))
for k, (u, v) in enumerate(E):
    B[idx[u], k], B[idx[v], k] = 1, -1
L = B @ B.T                      # Laplacian L = D - A
A = np.diag(np.diag(L)) - L      # adjacency matrix
assert np.allclose(A, A.T) and set(np.unique(A)) <= {0, 1}

mu, Q = np.linalg.eigh(L)        # eigenvalues in increasing order
a, x = mu[1], Q[:, 1]            # algebraic connectivity, Fiedler vector
x = x if x[0] > 0 else -x        # fix the sign for a stable printout
print("spectrum:", " ".join(f"{m:.3f}" for m in abs(mu)))
print(f"a(G) = {a:.4f}")
print("Fiedler vector:", " ".join(f"{v}={t:+.3f}" for v, t in zip(V, x)))

# Rayleigh quotient check: sum over edges of (x_u - x_v)^2 equals a(G)
print(f"Rayleigh quotient: {sum((x[idx[u]] - x[idx[v]]) ** 2 for u, v in E):.4f}")

# Spectral bisection by the sign of the Fiedler vector
S = [v for v in V if x[idx[v]] >= 0]
cut = [(u, v) for u, v in E if (u in S) != (v in S)]
print("part S:", "".join(S), " cut edges:", cut)
```

```text
spectrum: 0.000 0.628 4.000 4.000 4.000 4.000 5.000 6.372
a(G) = 0.6277
Fiedler vector: a=+0.406 b=+0.406 c=+0.406 d=+0.151 e=-0.278 f=-0.278 g=-0.406 h=-0.406
Rayleigh quotient: 0.6277
part S: abcd  cut edges: [('d', 'e'), ('d', 'f')]
```

The eigenvalue $0$ is simple (the graph is connected), and $a(G) \approx 0.628 \le \kappa(G) = 1$, in accordance with Theorem 6.5.3. The cut vertex $d$ has the component closest to $0$: it sits at the bottleneck. The two parts $\{a, b, c, d\}$ and $\{e, f, g, h\}$ obtained from the signs are each connected (Theorem 6.5.4), and the edges cut are exactly the minimum edge cut $\{de, df\}$. By Proposition 6.5.4, every four-four split cuts at least $0.628 \times 16/8 \approx 1.26$ edges, hence at least $2$, so this bisection is optimal. In practice, the normalized-cut image segmentation of Shi and Malik (2000) and spectral clustering, which uses the first few eigenvectors, both extend this idea.

## 6.6. Applications of Connectivity to Network Design

### 6.6.1. Fault Tolerance of Reliable Communication Networks

In the design of communication networks, the network topology is commonly modeled by a graph: processors are vertices and communication links are edges. An ideal network should have low vertex degrees, small diameter, symmetry, high connectivity and strong fault tolerance.

$k$-connectivity is a key measure of fault tolerance: if the network topology is $k$-connected, then even if $k-1$ nodes fail simultaneously, the network remains connected and messages can still be passed among the remaining nodes. Designing a reliable communication network requires a trade-off between connectivity (fault tolerance) and number of edges (cost): given the number of vertices $n$ and the connectivity $k$, construct a $k$-connected graph with as few edges as possible. The *Harary graph* $H_{k,n}$ is exactly such a graph, and it is one of the most economical topologies meeting a given fault-tolerance requirement.

### 6.6.2. Constraints from Minimum Degree and Number of Edges

By Whitney's inequality $\kappa(G) \le \lambda(G) \le \delta(G)$, the minimum degree limits the connectivity: for $G$ to be $k$-connected we need $\delta(G) \ge k$, that is, every vertex must have degree at least the target connectivity. By the **handshaking lemma**, this forces $m \ge \lceil kn/2 \rceil$. Harary proved that this lower bound is attained for $2 \le k < n$: the Harary graph $H_{k,n}$ is $k$-connected and has exactly $\lceil kn/2 \rceil$ edges. Hence the minimum number of edges of a $k$-connected graph on $n$ vertices is $\lceil kn/2 \rceil$.

The Harary graph is constructed as follows. Place the vertices $0, 1, \dots, n-1$ on a circle.

- For even $k$, join each vertex to the $k/2$ nearest vertices on either side, that is, $i$ is adjacent to $i \pm 1, \dots, i \pm k/2 \pmod n$;
- for odd $k$ and even $n$, add to $H_{k-1,n}$ all "diameters" joining $i$ and $i + n/2$ ($0 \le i < n/2$);
- for odd $k$ and odd $n$, add to $H_{k-1,n}$ the edges joining $i$ and $i + \frac{n-1}{2} \pmod n$ ($0 \le i \le \frac{n-1}{2}$).

$H_{2,n}$ is the cycle $C_n$.

![The Harary graphs H(2,8), H(3,8), H(4,8), H(5,8) for n = 8, with 8, 12, 16, 20 edges, that is, ⌈8k/2⌉; red: the "diameters" added when k is odd](./plots/harary.py)

### 6.6.3. Survivable Network Design

An important problem in network design is to find a minimum-cost subgraph that meets given connectivity requirements. A classical model is the $k$-edge-connected spanning subgraph problem ($k$-ECSS): in a **weighted graph** $G$, find a $k$-edge-connected **spanning subgraph** of minimum total weight. In high-reliability settings such as wireless sensor networks and cloud computing infrastructure, deployment cost and network survivability must be optimized together.

## 6.7. Wide Distance and Wide Diameter

When large amounts of information are transmitted, the bandwidth of a single path is often insufficient, and the information must be sent in packets: it is split into several packets that travel in parallel along several internally disjoint paths between the source and the destination. This leads to the notions of wide distance and wide diameter, which combine connectivity with diameter and measure both the fault tolerance and the communication efficiency of a network.

### 6.7.1. Containers

**Definition 6.7.1 (Container)** Let $x$ and $y$ be two distinct vertices of a graph $G$ and $w$ a positive integer. A set $C_w(x, y)$ of $w$ internally disjoint paths from $x$ to $y$ in $G$ is called a **$w$-container** between $x$ and $y$, or simply a **container**, and $w$ is called its **width**. The **length** $l(C_w(x, y))$ of the container is the length of its longest path. By Corollary 6.3.1, when $w \le \kappa(G)$, any two vertices are joined by a $w$-container.

### 6.7.2. $w$-Wide Distance

**Definition 6.7.2 ($w$-Wide Distance)** The minimum length of a $w$-container between $x$ and $y$ is called the **$w$-wide distance** between $x$ and $y$; these quantities are collectively called *wide distance*. The $1$-wide distance is the ordinary distance, that is, the length of a shortest path between $x$ and $y$.

The $w$-wide distance reflects the best communication delay achievable when transmitting along $w$ paths in parallel: the total delay of a parallel transmission is determined by the longest of its paths.

### 6.7.3. $w$-Wide Diameter

**Definition 6.7.3 ($w$-Wide Diameter)** The maximum of the $w$-wide distances over all pairs of vertices of a graph $G$ is called the **$w$-wide diameter** of $G$; these quantities are collectively called *wide diameter*. The $1$-wide diameter is the ordinary diameter of the graph, that is, the maximum distance over all pairs of vertices.

**Example 6.7.1** The vertices of the $3$-dimensional cube graph $Q_3$ are the $0$-$1$ strings of length $3$, two strings being adjacent when they differ in exactly one position; it is $3$-regular, $\kappa(Q_3) = 3$, and its diameter is $3$. Take $x = 000$ and $y = 011$ (at distance $2$). The two paths through $001$ and $010$ both have length $2$, but the third neighbor $100$ of $x$ is at distance $3$ from $y$, so a third path has length at least $4$, for example $000 \to 100 \to 101 \to 111 \to 011$. Hence the $3$-wide distance between $x$ and $y$ is $4$, larger than their distance $2$. Checking all pairs shows that the $3$-wide diameter of $Q_3$ is $4$; in general, the $n$-wide diameter of the $n$-dimensional cube $Q_n$ is $n+1$.

![A 3-container in the cube Q3 between 000 and 011 (violet): two paths of length 2 (blue, green) and one of length 4 (orange); the container has length 4](./plots/container.py)

In the evaluation of interconnection networks, the $w$-wide diameter is an important measure, capturing both the fault tolerance of the network (through $w$) and its transmission efficiency (through the diameter): when some nodes or links fail, the remaining disjoint paths can still be used for transmission. The wide diameters of common network topologies such as generalized Petersen graphs and Harary graphs have been studied in depth, providing a theoretical basis for the design of practical interconnection networks.

## Summary

- Vertex cuts and edge cuts: minimal sets of vertices or edges whose deletion destroys connectivity; cut vertices and bridges are special cases; pulling a graph apart at its cut vertices gives its blocks.
- Vertex connectivity $\kappa(G)$ and edge connectivity $\lambda(G)$: the minimum numbers of vertices and of edges whose deletion makes the graph disconnected (or trivial); they are the two quantitative measures of how well a graph is connected.
- Menger's theorem (Theorems 6.3.1 and 6.3.2): the maximum number of internally disjoint (edge-disjoint) paths between two vertices equals the minimum number of vertices (edges) whose deletion separates them; $k$-connectivity is equivalent to any two vertices being joined by $k$ internally disjoint paths (Corollary 6.3.1). It is unified with the max-flow min-cut theorem.
- $k$-connected graphs: graphs with connectivity at least $k$; a graph is $2$-connected if and only if it is connected, has $n \ge 3$ vertices and no cut vertex, which is in turn equivalent to any two vertices lying on a common cycle (Theorem 6.4.1).
- Algebraic connectivity: the quadratic form of the Laplacian $L = D - A = BB^{\mathsf T}$ is $\sum_{E}(x_u - x_v)^2$ (Proposition 6.5.1), and the multiplicity of the eigenvalue $0$ is the number of components (Proposition 6.5.2); the second smallest eigenvalue $a(G)$ is the minimum of the Rayleigh quotient on $\boldsymbol{1}^\perp$ (Theorem 6.5.2), and $a(G) > 0$ if and only if $G$ is connected.
- The chain of inequalities: for graphs that are not complete,

  $$
  a(G) \le \kappa(G) \le \lambda(G) \le \delta(G)
  $$

  (Whitney's inequality is Theorem 6.2.1, Fiedler's inequality is Theorem 6.5.3); for all graphs $a(G) \le \frac{n}{n-1}\delta(G)$, and every edge cut satisfies $|\partial S| \ge a(G)|S||V \setminus S|/n$.
- Fiedler vector: the continuous relaxation of the bisection problem; the two parts given by its signs are each connected (Theorem 6.5.4), which is the starting point of spectral bisection and spectral clustering.
- Network design: connectivity is the central measure of the fault tolerance of reliable communication networks; Harary graphs have the fewest edges, $\lceil kn/2 \rceil$, for a given number of vertices and given connectivity.
- Wide distance and wide diameter: combining connectivity with diameter, they describe the communication delay of parallel transmission along several disjoint paths.
