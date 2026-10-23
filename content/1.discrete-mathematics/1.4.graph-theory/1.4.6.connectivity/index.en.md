---
title: Graph Connectivity
source_hash: 291f2fb9b5b7
---

Chapter 2 used walks to define **connected graphs** and **connected components**, distinguishing only between "connected" and "disconnected". Applications such as communication networks, transportation planning and circuit design call for a finer measure of how well a graph is connected: if some nodes or links fail, does the network remain connected? In this chapter we introduce vertex connectivity and edge connectivity, establish Whitney's inequality relating them to the minimum degree, present Menger's theorem, which characterizes connectivity, together with its connection to network flows, and discuss $k$-connected graphs and applications of connectivity to network design.

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

By Theorem 3.1.1, an edge is a bridge if and only if it lies on no cycle of $G$.

**Example 6.1.2** In a tree, every edge is a bridge. The **cycle** $C_n$ with $n \ge 3$ vertices has no bridge, since deleting any edge leaves the **path** $P_n$ with $n$ vertices, which is still connected.

### 6.1.3. Definitions of Vertex Connectivity and Edge Connectivity

**Definition 6.1.6 (Vertex Connectivity)** The **vertex connectivity** $\kappa(G)$ of a graph $G$ is the minimum number of vertices whose deletion makes $G$ disconnected or trivial (a graph with a single vertex). If $G$ is disconnected or trivial, then $\kappa(G) = 0$. When $G$ is connected and not complete, $\kappa(G)$ is the size of a smallest vertex cut; for complete graphs, $\kappa(K_n) = n-1$.

**Definition 6.1.7 (Edge Connectivity)** The **edge connectivity** $\lambda(G)$ of a graph $G$ is the minimum number of edges whose deletion makes $G$ disconnected. If $G$ is disconnected or trivial, then $\lambda(G) = 0$. When $G$ is connected and nontrivial, $\lambda(G)$ is the size of a smallest edge cut.

**Remark** Vertex connectivity is often simply called the connectivity of the graph. $\kappa(G) = 0$ means that $G$ is disconnected or trivial, and $\kappa(G) \ge 1$ is (nontrivial) connectedness in the usual sense.

**Example 6.1.3**

- The complete graph $K_n$ ($n \ge 2$): $\kappa(K_n) = \lambda(K_n) = n-1$. Deleting the $n-1$ edges at any vertex isolates that vertex; on the other hand, if the vertices are split into two parts of sizes $p$ and $n-p$ ($1 \le p \le n-1$), there are $p(n-p) \ge n-1$ edges between the parts, so fewer than $n-1$ edges cannot disconnect $K_n$.
- A tree $T$ ($n \ge 2$): $\kappa(T) = \lambda(T) = 1$, since a tree has bridges; for $n \ge 3$ it also has cut vertices.
- The cycle $C_n$ ($n \ge 3$): $\kappa(C_n) = \lambda(C_n) = 2$. Deleting any single vertex or edge leaves a path, which is still connected; deleting two nonadjacent vertices (for $n = 3$, deleting two vertices leaves a trivial graph) or any two edges disconnects the graph.
- The complete bipartite graph $K_{r,s}$ ($1 \le r \le s$): its minimum degree is $r$, and $\kappa(K_{r,s}) = \lambda(K_{r,s}) = r$.
- The Petersen graph is the classic example of a $3$-regular graph (every vertex has degree $3$); its vertex connectivity and edge connectivity are both $3$.

## 6.2. Whitney's Inequality

The quantitative relation between vertex connectivity and edge connectivity was established by Whitney in 1932 and is known as *Whitney's inequality*. Let $\delta(G)$ denote the minimum degree of the vertices of $G$.

**Theorem 6.2.1 (Whitney's Inequality)** Every graph $G$ satisfies

$$
\kappa(G) \le \lambda(G) \le \delta(G).
$$

**Proof** If $G$ is disconnected or trivial, then $\kappa(G) = \lambda(G) = 0$ and the claim holds. Assume now that $G$ is connected and $n \ge 2$.

First we show $\lambda(G) \le \delta(G)$. Let $v$ be a vertex of minimum degree, $d(v) = \delta(G)$. Deleting all $\delta(G)$ edges incident with $v$ isolates $v$ and disconnects the graph, so $\lambda(G) \le \delta(G)$.

Next we show $\kappa(G) \le \lambda(G)$. Let $S$ be a minimum edge cut of $G$, $|S| = \lambda(G)$. Deleting $S$ splits the vertices into two parts $X$ and $Y = V - X$, and $S$ consists of all edges between $X$ and $Y$. There are two cases:

1. Every vertex of $X$ is adjacent to every vertex of $Y$. Then $\lambda(G) = |S| \ge |X||Y| \ge n - 1$, while always $\kappa(G) \le n-1$, so the claim holds.
2. Some $x \in X$ and $y \in Y$ are nonadjacent. For each edge of $S$, take its endpoint in $X$ if that endpoint is not $x$; otherwise (the edge has the form $(x, y')$ with $y' \in Y$, and $y' \ne y$) take its endpoint $y'$ in $Y$. Let $T$ be the set of vertices so chosen. Then $|T| \le |S|$ and $x, y \notin T$. Every path from $x$ to $y$ in $G$ uses some edge of $S$, and that edge always has an endpoint in $T$, which is neither $x$ nor $y$; hence $x$ and $y$ are disconnected in $G - T$. Therefore $\kappa(G) \le |T| \le |S| = \lambda(G)$. $\square$

**Example 6.2.1** If $G$ is a $3$-regular graph, then $\delta(G) = 3$, so $\kappa(G) \le \lambda(G) \le 3$. The Petersen graph satisfies $\kappa = \lambda = \delta = 3$, so both inequalities in Whitney's inequality hold with equality.

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

### 6.3.2. Menger's Theorem and Connectivity

**Corollary 6.3.1 (Whitney)** Let $G$ be a graph with $n \ge k+1$ vertices. Then $G$ is $k$-vertex-connected ($\kappa(G) \ge k$) if and only if any two distinct vertices of $G$ are joined by at least $k$ internally disjoint paths.

**Proof** Sufficiency: if any two vertices are joined by $k$ internally disjoint paths, then after deleting fewer than $k$ vertices, each pair of remaining vertices is still joined by at least one of these paths, so the graph remains connected and $\kappa(G) \ge k$.

Necessity: suppose $\kappa(G) \ge k$. For nonadjacent vertices $x, y$, at least $k$ vertices must be deleted to disconnect them, so by Theorem 6.3.1 they are joined by $k$ internally disjoint paths. For adjacent vertices $x, y$, let $e = (x, y)$; one can show that $\kappa(G - e) \ge k - 1$. Applying Theorem 6.3.1 to $x, y$ in $G - e$ gives $k-1$ internally disjoint paths, and together with the edge $e$ itself there are $k$. $\square$

Similarly, Theorem 6.3.2 shows that $G$ is $k$-edge-connected ($\lambda(G) \ge k$) if and only if any two distinct vertices of $G$ are joined by at least $k$ edge-disjoint paths.

### 6.3.3. Menger's Theorem and Network Flows

Menger's theorem is closely related to the **max-flow min-cut theorem** (Theorem 5.5.2); each can be derived from the other. Take the edge form as an example: replace each edge of the undirected graph by two oppositely directed edges of capacity $1$, and take $x$ as the source and $y$ as the sink. Then the maximum flow value is the maximum number of edge-disjoint paths between $x$ and $y$, and the minimum cut capacity is the minimum number of edges whose deletion disconnects $x$ from $y$. For the vertex form, we additionally split each vertex $v$ other than $x, y$ into two vertices $v_{\mathrm{in}}$ and $v_{\mathrm{out}}$ joined by an edge $(v_{\mathrm{in}}, v_{\mathrm{out}})$ of capacity $1$; edges that entered $v$ now enter $v_{\mathrm{in}}$, edges that left $v$ now leave $v_{\mathrm{out}}$, and these directed edges coming from edges of the original graph receive capacity $\infty$ (or a sufficiently large number). Then each vertex carries at most one unit of flow, so the maximum flow value is the maximum number of internally disjoint paths; and a cut of finite capacity can consist only of edges of the form $(v_{\mathrm{in}}, v_{\mathrm{out}})$, so the minimum cut capacity is the minimum number of vertices whose deletion disconnects $x$ from $y$.

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

### 6.4.5. Computing Connectivity and an Algebraic Characterization

By Menger's theorem, $\kappa(G)$ and $\lambda(G)$ can be computed by solving maximum flow problems between suitable pairs of vertices, so both can be found in polynomial time.

Connectivity also has an algebraic characterization. Let $D$ be the diagonal matrix of vertex degrees of $G$ and $A$ its adjacency matrix; $L = D - A$ is the **Laplacian matrix** of $G$. The second smallest **eigenvalue** $a(G)$ of $L$ is called the *algebraic connectivity* of $G$, a notion introduced by Fiedler in 1973: $a(G) > 0$ if and only if $G$ is connected, and $a(G) \le \kappa(G)$ when $G$ is not complete.

## 6.5. Applications of Connectivity to Network Design

### 6.5.1. Fault Tolerance of Reliable Communication Networks

In the design of communication networks, the network topology is commonly modeled by a graph: processors are vertices and communication links are edges. An ideal network should have low vertex degrees, small diameter, symmetry, high connectivity and strong fault tolerance.

$k$-connectivity is a key measure of fault tolerance: if the network topology is $k$-connected, then even if $k-1$ nodes fail simultaneously, the network remains connected and messages can still be passed among the remaining nodes. Designing a reliable communication network requires a trade-off between connectivity (fault tolerance) and number of edges (cost): given the number of vertices $n$ and the connectivity $k$, construct a $k$-connected graph with as few edges as possible. The *Harary graph* $H_{k,n}$ is exactly such a graph, and it is one of the most economical topologies meeting a given fault-tolerance requirement.

### 6.5.2. Constraints from Minimum Degree and Number of Edges

By Whitney's inequality $\kappa(G) \le \lambda(G) \le \delta(G)$, the minimum degree limits the connectivity: for $G$ to be $k$-connected we need $\delta(G) \ge k$, that is, every vertex must have degree at least the target connectivity. By the **handshaking lemma**, this forces $m \ge \lceil kn/2 \rceil$. Harary proved that this lower bound is attained for $2 \le k < n$: the Harary graph $H_{k,n}$ is $k$-connected and has exactly $\lceil kn/2 \rceil$ edges. Hence the minimum number of edges of a $k$-connected graph on $n$ vertices is $\lceil kn/2 \rceil$.

### 6.5.3. Survivable Network Design

An important problem in network design is to find a minimum-cost subgraph that meets given connectivity requirements. A classical model is the $k$-edge-connected spanning subgraph problem ($k$-ECSS): in a **weighted graph** $G$, find a $k$-edge-connected **spanning subgraph** of minimum total weight. In high-reliability settings such as wireless sensor networks and cloud computing infrastructure, deployment cost and network survivability must be optimized together.

## 6.6. Wide Distance and Wide Diameter

When large amounts of information are transmitted, the bandwidth of a single path is often insufficient, and the information must be sent in packets: it is split into several packets that travel in parallel along several internally disjoint paths between the source and the destination. This leads to the notions of wide distance and wide diameter, which combine connectivity with diameter and measure both the fault tolerance and the communication efficiency of a network.

### 6.6.1. Containers

**Definition 6.6.1 (Container)** Let $x$ and $y$ be two distinct vertices of a graph $G$ and $w$ a positive integer. A set $C_w(x, y)$ of $w$ internally disjoint paths from $x$ to $y$ in $G$ is called a **$w$-container** between $x$ and $y$, or simply a **container**, and $w$ is called its **width**. The **length** $l(C_w(x, y))$ of the container is the length of its longest path. By Corollary 6.3.1, when $w \le \kappa(G)$, any two vertices are joined by a $w$-container.

### 6.6.2. $w$-Wide Distance

**Definition 6.6.2 ($w$-Wide Distance)** The minimum length of a $w$-container between $x$ and $y$ is called the **$w$-wide distance** between $x$ and $y$; these quantities are collectively called *wide distance*. The $1$-wide distance is the ordinary distance, that is, the length of a shortest path between $x$ and $y$.

The $w$-wide distance reflects the best communication delay achievable when transmitting along $w$ paths in parallel: the total delay of a parallel transmission is determined by the longest of its paths.

### 6.6.3. $w$-Wide Diameter

**Definition 6.6.3 ($w$-Wide Diameter)** The maximum of the $w$-wide distances over all pairs of vertices of a graph $G$ is called the **$w$-wide diameter** of $G$; these quantities are collectively called *wide diameter*. The $1$-wide diameter is the ordinary diameter of the graph, that is, the maximum distance over all pairs of vertices.

In the evaluation of interconnection networks, the $w$-wide diameter is an important measure, capturing both the fault tolerance of the network (through $w$) and its transmission efficiency (through the diameter): when some nodes or links fail, the remaining disjoint paths can still be used for transmission. The wide diameters of common network topologies such as generalized Petersen graphs and Harary graphs have been studied in depth, providing a theoretical basis for the design of practical interconnection networks.

## Summary

- Vertex cuts and edge cuts: minimal sets of vertices or edges whose deletion destroys connectivity; cut vertices and bridges are special cases.
- Vertex connectivity $\kappa(G)$ and edge connectivity $\lambda(G)$: the minimum numbers of vertices and of edges whose deletion makes the graph disconnected (or trivial); they are the two quantitative measures of how well a graph is connected.
- Whitney's inequality $\kappa(G) \le \lambda(G) \le \delta(G)$ relates vertex connectivity, edge connectivity and minimum degree.
- Menger's theorem: the maximum number of internally disjoint (edge-disjoint) paths between two vertices equals the minimum number of vertices (edges) whose deletion separates them; $k$-connectivity is equivalent to any two vertices being joined by $k$ internally disjoint paths. It is unified with the max-flow min-cut theorem.
- $k$-connected graphs: graphs with connectivity at least $k$; a graph is $2$-connected if and only if it is connected, has $n \ge 3$ vertices and no cut vertex, which is in turn equivalent to any two vertices lying on a common cycle.
- Network design: connectivity is the central measure of the fault tolerance of reliable communication networks; Harary graphs have the fewest edges for a given number of vertices and given connectivity.
- Wide distance and wide diameter: combining connectivity with diameter, they describe the communication delay of parallel transmission along several disjoint paths.
