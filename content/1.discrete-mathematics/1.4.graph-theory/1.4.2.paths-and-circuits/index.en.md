---
title: Paths and Cycles
source_hash: 0f250b5abca0
---

Walks, paths and cycles are the most basic structures in graph theory. In this chapter we first define walks, closed walks and connectivity in directed and undirected graphs, and present matrix methods and search methods for deciding whether a walk exists. We then discuss two classical traversal problems and the conditions under which they can be solved: Eulerian circuits, which traverse every edge, and Hamiltonian cycles, which visit every vertex. Finally we turn to optimization problems involving paths: the traveling salesman problem, shortest paths, critical paths and the Chinese postman problem.

## 2.1. Walks, Trails, Paths and Cycles

### 2.1.1. Walks in Directed Graphs

**Definition 2.1.1 (Directed Walk)** Let $G = (V, E)$ be a directed graph and $P = (e_{i_1}, e_{i_2}, \dots, e_{i_q})$ a sequence of edges of $G$. If for $k = 1, 2, \dots, q-1$ the head of $e_{i_k}$ is the tail of $e_{i_{k+1}}$, then $P$ is called a **directed walk** in $G$. If, in addition, the head of $e_{i_q}$ is the tail of $e_{i_1}$, then $P$ is called a **closed directed walk** in $G$.

- **Directed trail** (**directed circuit**): no edge occurs more than once in $P$.
- **Directed path** (**directed cycle**): no vertex occurs more than once in $P$ (for a closed walk, the coincidence of the first and last vertex does not count as a repetition). Every directed path is a directed trail.

### 2.1.2. Walks in Undirected Graphs

**Definition 2.1.2 (Walk)** Let $G = (V, E)$ be an undirected graph and $P = (v_{i_1}, e_{i_1}, v_{i_2}, e_{i_2}, \dots, e_{i_{q-1}}, v_{i_q})$ an alternating sequence of vertices and edges. If for every $k$ the vertices $v_{i_k}$ and $v_{i_{k+1}}$ are the two endpoints of $e_{i_k}$, then $P$ is called a **walk** (or chain) in $G$; if $v_{i_q} = v_{i_1}$, then $P$ is called a **closed walk** in $G$.

- **Trail**, **circuit**: a walk, respectively a closed walk, in which no edge is repeated.
- **Path**, **cycle**: a walk, respectively a closed walk, in which no vertex is repeated (for a closed walk, the coincidence of the first and last vertex does not count as a repetition). Every path is a trail.

### 2.1.3. Connected Graphs and Connected Components

**Definition 2.1.3 (Connected Graph)** An undirected graph $G$ is called a **connected graph** if any two of its vertices are joined by a walk; otherwise it is a **disconnected graph**. A directed graph $G$ is called **connected** if it is connected when the directions of its edges are ignored.

**Definition 2.1.4 (Connected Component)** A connected subgraph $H$ of $G$ that is not a proper subgraph of any connected subgraph of $G$ is called a **maximal connected subgraph** of $G$, or a **connected component**.

Clearly every connected component of $G$ is an **induced subgraph** of $G$, and $G$ is connected if and only if it has exactly one connected component. If $G$ has two connected components, then after a suitable numbering both its **adjacency matrix** and its **incidence matrix** are block diagonal.

### 2.1.4. A Sufficient Condition for Connectivity

**Example 2.1.1** Let $G$ be a **simple graph**. Prove that $G$ is connected whenever $m > \frac{1}{2}(n-1)(n-2)$.

**Proof** We argue by contradiction. Suppose $G$ is disconnected. Then $V(G)$ splits into two nonempty parts with no edge between them: the vertex set $V_1$ of some connected component $G_1$, and the set $V_2$ of the remaining vertices. Let $n_i = |V_i|$ and let $m_i$ be the number of edges with both endpoints in $V_i$ ($i = 1, 2$); then $n_1 + n_2 = n$ and $m_1 + m_2 = m$. Since $G$ is simple,

$$
m_1 \le \frac{1}{2}n_1(n_1-1), \qquad m_2 \le \frac{1}{2}n_2(n_2-1).
$$

Moreover $1 \le n_1, n_2 \le n-1$, so

$$
m \le \frac{1}{2}(n-1)(n_1-1) + \frac{1}{2}(n-1)(n_2-1) = \frac{1}{2}(n-1)(n-2),
$$

a contradiction. Hence $G$ is connected. $\square$

### 2.1.5. Summary

- Directed graphs: directed walks and closed directed walks; directed trails (circuits) and directed paths (cycles).
- Undirected graphs: walks (chains) and closed walks; trails and circuits, paths and cycles.
- Connected graphs and connected components (maximal connected subgraphs).

## 2.2. Deciding the Existence of Walks

To decide whether two given vertices of a graph $G$ are joined by a walk, or lie on a closed walk, the usual tools are the adjacency matrix method and search methods.

### 2.2.1. The Adjacency Matrix Method

Let $A = (a_{ij})_{n \times n}$ be the **adjacency matrix** of $G$; $a_{ij} = 1$ means that there is an edge from $v_i$ to $v_j$, that is, a walk of length $1$. Consider $A^2 = (a_{ij}^{(2)})_{n \times n}$:

$$
a_{ij}^{(2)} = \sum_{k=1}^{n} a_{ik} a_{kj},
$$

so $a_{ij}^{(2)} \ne 0$ if and only if there is a $k$ with $a_{ik} = a_{kj} = 1$, that is, $v_j$ can be reached from $v_i$ along $2$ edges, and $a_{ij}^{(2)}$ is exactly the number of such walks. In general, the entry $a_{ij}^{(l)}$ of $A^l = (a_{ij}^{(l)})$ is the number of walks from $v_i$ to $v_j$ with $l$ edges (repeated vertices and edges allowed). Let

$$
P = A + A^2 + \cdots + A^n.
$$

If $p_{ij} = t$, then there are $t$ walks of length at most $n$ from $v_i$ to $v_j$. Since two vertices joined by a walk are always joined by a walk of length at most $n$, it suffices to go up to $A^n$. This method requires $n$ matrix multiplications and takes $O(n^4)$ time.

In practice we often only need to know whether a walk exists. We can then use logical operations (Boolean matrix multiplication) instead:

$$
a_{ij}^{(l)} = \bigvee_{k=1}^{n} \left( a_{ik}^{(l-1)} \land a_{kj} \right), \qquad l = 2, 3, \dots, n,
$$

and set $P = A \lor A^2 \lor \cdots \lor A^n$, called the *reachability matrix*: $p_{ij} = 1$ if and only if there is a walk from $v_i$ to $v_j$. From the viewpoint of [set theory](/1.2), if $A$ is regarded as the relation matrix of a binary relation on the vertex set, then the reachability matrix is the relation matrix of the **transitive closure** of that relation.

### 2.2.2. Warshall's Algorithm

**Algorithm 2.2.1 (Warshall's Algorithm)** Warshall's algorithm computes the reachability matrix directly in $O(n^3)$ time:

```text
Begin
    P ← A
    for i ← 1 to n
        for j ← 1 to n
            for k ← 1 to n
                p_{jk} ← p_{jk} ∨ (p_{ji} ∧ p_{ik})
End
```

**Theorem 2.2.1** Warshall's algorithm produces the reachability matrix of $G$.

**Proof** Let $P^{(i)}$ be the matrix after the $i$-th iteration of the outer loop, with $P^{(0)} = A$. We show by induction on $i$ that $p_{jk}^{(i)} = 1$ if and only if there is a walk from $v_j$ to $v_k$ all of whose internal vertices (the vertices other than its first and last) belong to $\{v_1, \dots, v_i\}$.

For $i = 0$ the set of allowed internal vertices is empty, so such walks are just edges and the claim holds. Suppose the claim holds for $i-1$. A path from $v_j$ to $v_k$ whose internal vertices lie in $\{v_1, \dots, v_i\}$ either avoids $v_i$ (corresponding to $p_{jk}^{(i-1)} = 1$) or passes through $v_i$ exactly once; in the latter case it splits into two pieces $v_j \to v_i$ and $v_i \to v_k$, each with internal vertices in $\{v_1, \dots, v_{i-1}\}$ (corresponding to $p_{ji}^{(i-1)} = p_{ik}^{(i-1)} = 1$). Therefore

$$
p_{jk}^{(i)} = p_{jk}^{(i-1)} \lor \left( p_{ji}^{(i-1)} \land p_{ik}^{(i-1)} \right).
$$

During the $i$-th iteration the entries of row $i$ and column $i$ do not change (for example, $p_{ji} \leftarrow p_{ji} \lor (p_{ji} \land p_{ii}) = p_{ji}$), so the in-place updates of the algorithm agree with this formula. For $i = n$ the internal vertices are no longer restricted, and $P^{(n)}$ is the reachability matrix. $\square$

### 2.2.3. Search Methods

- *Breadth-first search* (BFS): starting from a source vertex $v_0$, first visit all successors of $v_0$ (the first layer), then the successors of those vertices (the second layer), and so on, until the target vertex is found or every reachable vertex has been visited. Visited vertices are labeled to avoid repetition. A forward star is a convenient representation for BFS, which runs in $O(n+m)$ time.
- *Depth-first search* (DFS): starting from $v_0$, choose any successor $v_1$ and record its predecessor, then choose an unvisited successor $v_2$ of $v_1$, and so on; when no further step is possible, backtrack to the predecessor and continue exploring other branches. DFS also runs in $O(n+m)$ time.

### 2.2.4. Summary

- Adjacency matrix method: compute the reachability matrix from matrix powers or by Warshall's algorithm.
- Search methods: BFS and DFS, suitable for testing connectivity and finding paths.

## 2.3. Eulerian Trails and Circuits

### 2.3.1. Definition and Historical Background

**Definition 2.3.1 (Eulerian Circuit)** In a connected undirected graph $G = (V, E)$, a circuit containing every edge is called an **Eulerian circuit** of $G$; a trail containing every edge is called an **Eulerian trail** of $G$.

The problem of the **Seven Bridges of Königsberg** asks whether one can start somewhere, cross each bridge exactly once and return to the starting point. Regarding the four land masses as vertices and the seven bridges as edges gives a **multigraph** with $4$ vertices and $7$ edges, and the question becomes whether this graph has an Eulerian circuit. The four vertices have degrees $5, 3, 3, 3$, so by Theorem 2.3.1 below the answer is no.

### 2.3.2. Existence of Eulerian Circuits

**Theorem 2.3.1** A connected undirected graph $G$ has an Eulerian circuit if and only if every vertex of $G$ has even degree.

**Proof** Necessity: let $C$ be an Eulerian circuit of $G$; it traverses every edge exactly once. Each time the walk along $C$ passes through a vertex $v$, it enters along one edge and leaves along another (at the starting vertex, pair the first departure with the final arrival). Thus the edges incident with $v$ are paired off, and $d(v)$ is even.

Sufficiency: suppose every vertex has even degree. Start at any vertex $v_0$ and repeatedly move along an edge not yet used. Since all degrees are even, whenever we arrive at a vertex $v \ne v_0$ there is still an unused edge by which to leave $v$, so the walk can only get stuck at $v_0$; since $G$ is finite, it must eventually return to $v_0$, producing a circuit $C$. If $C$ contains all edges, it is an Eulerian circuit. Otherwise let $G_1 = G - C$; every vertex of $G_1$ still has even degree (although $G_1$ may be disconnected). Since $G$ is connected, some vertex $v_i$ on $C$ has nonzero degree in $G_1$. Starting from $v_i$ we obtain in the same way a circuit $C_1$ in $G_1$, and splicing $C_1$ into $C$ at $v_i$ yields a longer circuit. Repeating this process, since there are finitely many edges, we eventually obtain a circuit containing all edges, that is, an Eulerian circuit. $\square$

**Corollary 2.3.1** If a connected undirected graph $G$ has exactly $2$ vertices of odd degree, then $G$ has an Eulerian trail whose ends are these two vertices (but no Eulerian circuit).

**Proof** Let the two odd vertices be $v_i$ and $v_j$. Adding a new edge $(v_i, v_j)$ gives a graph $G'$ in which every vertex has even degree, so by Theorem 2.3.1 $G'$ has an Eulerian circuit $C$. Removing the new edge $(v_i, v_j)$ from $C$ gives an Eulerian trail of $G$ from $v_i$ to $v_j$. $\square$

**Example 2.3.1** If a connected graph $G = (V, E)$ has $k \ge 2$ vertices of odd degree, then $E(G)$ can be partitioned into $k/2$ trails.

**Proof** By Property 1.3.2, $k$ is even. Add $k/2$ new edges among the $k$ odd vertices so that each odd vertex is incident with exactly one new edge, obtaining $G'$. Every vertex of $G'$ has even degree, so $G'$ has an Eulerian circuit $C$. No two of the $k/2$ new edges share an endpoint, so no two of them are consecutive on $C$. Removing them cuts $C$ into $k/2$ pieces, each of which is a trail in $G$, and these trails together cover every edge of $G$ exactly once. $\square$

### 2.3.3. The Directed Case

**Corollary 2.3.2** A connected directed graph $G$ has a directed Eulerian circuit (a directed circuit containing every edge) if and only if the **out-degree** of each vertex equals its **in-degree**, that is, $d^+(v) = d^-(v)$ for all $v$. The proof is similar to that of Theorem 2.3.1 and is left as an exercise.

## 2.4. Hamiltonian Paths and Cycles

### 2.4.1. Definition and Historical Background

**Definition 2.4.1 (Hamiltonian Cycle)** A cycle of an undirected graph $G$ passing through every vertex is called a **Hamiltonian cycle** of $G$, or $H$ cycle for short; a path passing through every vertex is called a **Hamiltonian path**, or $H$ path for short.

An Eulerian circuit traverses all edges (it is a circuit), whereas a Hamiltonian cycle visits all vertices (it is a cycle). Deleting **multiple edges** and **loops** does not affect the existence of an $H$ cycle, so one usually studies only **simple graphs**. Unlike the Eulerian case, no simple necessary and sufficient condition is known for a general graph to have an $H$ cycle; below we give several sufficient conditions.

### 2.4.2. A Sufficient Condition for Hamiltonian Paths

**Theorem 2.4.1** Let $G$ be a simple graph on $n$ vertices. If $d(v_i) + d(v_j) \ge n-1$ for any two vertices $v_i, v_j$ of $G$, then $G$ has a Hamiltonian path.

**Proof** We proceed in three steps.

Step 1: $G$ is connected. Otherwise take two distinct connected components $H_1$ and $H_2$ of $G$, with $n_1$ and $n_2$ vertices respectively, so that $n_1 + n_2 \le n$. For $v_i \in H_1$ and $v_j \in H_2$ we have $d(v_i) \le n_1 - 1$ and $d(v_j) \le n_2 - 1$, so $d(v_i) + d(v_j) \le n - 2$, contradicting the hypothesis.

Step 2: let $P = (v_{i_1}, v_{i_2}, \dots, v_{i_l})$ be a maximal path in $G$, that is, all neighbors of its ends $v_{i_1}$ and $v_{i_l}$ lie on $P$ (otherwise $P$ could be extended). If $l = n$, then $P$ is already an $H$ path. Assume now that $l < n$; we first show that there is a cycle through all $l$ vertices of $P$.

If $v_{i_1}$ and $v_{i_l}$ are adjacent, this is obvious. Otherwise let the neighbors of $v_{i_1}$ be $v_{i_{j_1}}, \dots, v_{i_{j_k}}$, where $k = d(v_{i_1})$ and $2 \le j_1 < \dots < j_k \le l-1$. If $v_{i_l}$ is adjacent to some $v_{i_{j_r - 1}}$, then

$$
v_{i_1} v_{i_2} \cdots v_{i_{j_r - 1}} v_{i_l} v_{i_{l-1}} \cdots v_{i_{j_r}} v_{i_1}
$$

is the required cycle. If $v_{i_l}$ is adjacent to none of the $k$ vertices $v_{i_{j_1 - 1}}, \dots, v_{i_{j_k - 1}}$, then its neighbors lie among the remaining $l - 1 - k$ vertices of $P$, so $d(v_{i_l}) \le l - 1 - k$ and hence

$$
d(v_{i_1}) + d(v_{i_l}) \le l - 1 \le n - 2,
$$

contradicting the hypothesis. Therefore a cycle $C$ through all vertices of $P$ exists.

Step 3: since $G$ is connected and $l < n$, some vertex $v_t$ not on $C$ is adjacent to a vertex $v_{i_q}$ on $C$. Deleting from $C$ one of the edges incident with $v_{i_q}$ gives a path with $l$ vertices ending at $v_{i_q}$; appending the edge $(v_{i_q}, v_t)$ gives a path with $l+1$ vertices, contradicting the maximality of $P$. Hence $l = n$ and $P$ is an $H$ path. $\square$

### 2.4.3. Sufficient Conditions for Hamiltonian Cycles

**Lemma 2.4.1** Let $G$ be a simple graph with $n \ge 3$ vertices that has an $H$ path but no $H$ cycle, and let $v_1, v_n$ be the ends of the $H$ path. Then $d(v_1) + d(v_n) \le n-1$.

**Proof** The argument is the same as in Step 2 of the proof of Theorem 2.4.1 (with $l = n$): if $d(v_1) + d(v_n) \ge n$, we can construct a cycle through all vertices, that is, an $H$ cycle, a contradiction. $\square$

**Corollary 2.4.1** Let $G$ be a simple graph on $n \ge 3$ vertices. If $d(v_i) + d(v_j) \ge n$ for any two vertices $v_i, v_j$ of $G$, then $G$ has a Hamiltonian cycle.

**Proof** By Theorem 2.4.1, $G$ has an $H$ path; let $v_1, v_n$ be its ends. If $G$ had no $H$ cycle, Lemma 2.4.1 would give $d(v_1) + d(v_n) \le n-1$, contradicting the hypothesis. $\square$

**Corollary 2.4.2** Let $G$ be a simple graph on $n \ge 3$ vertices. If every vertex of $G$ has degree at least $n/2$, then $G$ has an $H$ cycle. This follows at once from Corollary 2.4.1.

### 2.4.4. The Closure of a Graph

**Lemma 2.4.2** Let $G$ be a simple graph on $n \ge 3$ vertices, and let $v_i, v_j$ be nonadjacent vertices with $d(v_i) + d(v_j) \ge n$. Then $G$ has an $H$ cycle if and only if $G + (v_i, v_j)$ has an $H$ cycle.

**Proof** Necessity is obvious. Sufficiency: suppose $G + (v_i, v_j)$ has an $H$ cycle but $G$ has none. Then the $H$ cycle must use the edge $(v_i, v_j)$, and deleting this edge gives an $H$ path in $G$ with ends $v_i, v_j$. By Lemma 2.4.1, $d(v_i) + d(v_j) \le n-1$, a contradiction. $\square$

**Definition 2.4.2 (Hamiltonian Closure)** Let $G$ be a simple graph. If $G$ has nonadjacent vertices $v_i, v_j$ with $d(v_i) + d(v_j) \ge n$, let $G' = G + (v_i, v_j)$; repeat this process on $G'$ until no such pair of vertices remains. The resulting graph is called the **Hamiltonian closure** (or simply the closure) of $G$ and is denoted $C(G)$.

**Lemma 2.4.3** The closure $C(G)$ of a simple graph $G$ is unique; it does not depend on the order in which edges are added.

**Proof** Let $C_1(G)$ and $C_2(G)$ be closures obtained by two orders, where $C_1(G)$ arises by adding the edges $e_1, e_2, \dots, e_p$ in turn and $L_2$ is the set of edges added to obtain $C_2(G)$. If some $e_r \notin L_2$, take the one with the smallest index, say $e_{i+1} = (u, v)$, and let $H = G + \{e_1, \dots, e_i\}$. Since $e_1, \dots, e_i \in L_2$, $H$ is a subgraph of $C_2(G)$; and since $e_{i+1}$ was added to $H$, we have $d_H(u) + d_H(v) \ge n$, so $d(u) + d(v) \ge n$ in $C_2(G)$ as well. But $u$ and $v$ are not adjacent in $C_2(G)$, contradicting the fact that $C_2(G)$ is a closure. Hence $\{e_1, \dots, e_p\} \subseteq L_2$. By symmetry $L_2 \subseteq \{e_1, \dots, e_p\}$, so $C_1(G) = C_2(G)$. $\square$

**Theorem 2.4.2** A simple graph $G$ with $n \ge 3$ vertices has a Hamiltonian cycle if and only if its closure $C(G)$ has a Hamiltonian cycle.

**Proof** By Lemma 2.4.2, no edge addition changes whether an $H$ cycle exists; by Lemma 2.4.3, the closure is uniquely determined. $\square$

**Corollary 2.4.3** Let $G$ be a simple graph on $n \ge 3$ vertices. If $C(G)$ is complete, then $G$ has an $H$ cycle.

### 2.4.5. Summary

- Sufficient condition for an $H$ path in $G$: the degrees of any two vertices sum to at least $n-1$.
- Sufficient conditions for an $H$ cycle ($n \ge 3$): the degrees of any two vertices sum to at least $n$, or the minimum degree is at least $n/2$.
- The closure gives a practical test for $H$ cycles: $G$ has an $H$ cycle if and only if $C(G)$ has one.

## 2.5. The Traveling Salesman Problem

### 2.5.1. Problem Statement and Complexity

The *traveling salesman problem* (TSP) is the following: given $n$ cities and the distances between every two of them (that is, a positively weighted complete graph), find a shortest closed tour that visits every city exactly once and returns to the start, in other words a shortest $H$ cycle.

The complete graph $K_n$ ($n \ge 3$) has $\frac{1}{2}(n-1)!$ distinct $H$ cycles. By Stirling's formula $n! \approx \sqrt{2\pi n}\left(\frac{n}{\mathrm{e}}\right)^n$, this number grows faster than any exponential: for $n = 26$ there are already about $7.8 \times 10^{24}$ of them, and even a supercomputer would need an extremely long time to enumerate them one by one. Exhaustive enumeration is therefore infeasible.

### 2.5.2. Branch and Bound

The basic idea of *branch and bound* is as follows:

1. Sort the edges in increasing order of weight.
2. Search for $H$ cycles depth-first in this order, using the length of the shortest cycle found so far as the bound.
3. During the search, if the length of the current partial path is already at least the bound, prune: do not explore this branch further.
4. Update the bound whenever a shorter cycle is found, until the search terminates.

Pruning can reduce the amount of computation drastically, but the worst-case complexity of branch and bound is still $O(n!)$.

### 2.5.3. An Approximation Algorithm: Cheapest Insertion

When the edge weights satisfy the *triangle inequality*, that is, $w(i, j) \le w(i, k) + w(k, j)$ for all $i, j, k$, the cheapest insertion algorithm finds an approximate solution in polynomial time.

**Algorithm 2.5.1 (Cheapest Insertion)** Start with a subtour consisting of a single vertex. At each step, among all vertices not yet on the tour and all positions where they could be inserted, choose the vertex and position that increase the tour length the least, and insert that vertex there. Repeat until every vertex is on the tour.

**Theorem 2.5.1** Suppose the edge weights of a positively weighted complete graph satisfy the triangle inequality. Let $O_n$ be the length of an optimal tour and $T_n$ the length of the tour produced by cheapest insertion. Then $\dfrac{T_n}{O_n} < 2$. (Proof omitted.)

### 2.5.4. Summary

- TSP is NP-hard, and exhaustive enumeration is infeasible.
- Branch and bound is a common exact method; its efficiency relies on pruning.
- Under the triangle inequality, cheapest insertion finds in polynomial time a tour shorter than twice the optimum.

## 2.6. Shortest Paths

### 2.6.1. Types of Problems

Shortest path problems fall into three types:

1. Shortest paths between two given vertices.
2. Shortest paths from one vertex to all other vertices (single-source shortest paths).
3. Shortest paths between all pairs of vertices.

Solving the second type also solves the first, and the third can be handled by solving the second once for each vertex. Depending on the edge weights, there are three further cases: all weights are positive real numbers (positively weighted graphs); all weights equal $1$; weights are arbitrary real numbers but the graph has no cycle of negative length.

### 2.6.2. Dijkstra's Algorithm for Positively Weighted Graphs

**Lemma 2.6.1** In a positively weighted graph $G$, if $P(i)$ is a shortest path from $v_1$ to $v_i$ and $v_j \in P(i)$, then the part $P(j)$ of $P(i)$ from $v_1$ to $v_j$ is a shortest path from $v_1$ to $v_j$.

**Lemma 2.6.2** In a positively weighted graph, a shortest path $P(i)$ is longer than any of its proper initial parts $P(j)$ ($v_j \ne v_i$).

These two lemmas show that the shortest path lengths can be determined vertex by vertex, in increasing order of distance from $v_1$. This is the idea behind *Dijkstra's algorithm*.

**Algorithm 2.6.1 (Dijkstra's Algorithm)** Compute the shortest path lengths from a source vertex $v_1$ to all other vertices of a positively weighted graph. Each vertex $v$ carries a label $\pi(v)$, the length of the shortest walk from $v_1$ to $v$ known so far; labels are either temporary or permanent. The vertex that most recently received a permanent label is called the working vertex.

1. Initialization: set $\pi(v_1) = 0$ as a permanent label and make $v_1$ the working vertex; give every other vertex the temporary label $\pi(v) = \infty$.
2. Let $u$ be the working vertex. For each successor $v$ of $u$ with a temporary label, if $\pi(u) + w(u, v) < \pi(v)$, set $\pi(v) \leftarrow \pi(u) + w(u, v)$.
3. Among all vertices with temporary labels, choose one with the smallest $\pi$, make its label permanent and make it the new working vertex.
4. If every vertex has a permanent label (or the target vertex has one), stop; otherwise go to step 2.

At termination, the permanent label of each vertex is the length of a shortest path from $v_1$ to it. With an array implementation the algorithm runs in $O(n^2)$ time; with a priority queue (heap) this drops to $O(m \log n)$.

### 2.6.3. Graphs with Unit Weights

When all edge weights equal $1$, single-source shortest paths can be found by breadth-first search: expand layer by layer from the source, and the layer at which a vertex is first reached is its shortest path length. If the graph is stored as a forward star or adjacency list, this takes $O(n+m)$ time.

### 2.6.4. Ford's Algorithm for Arbitrary Real Weights

When edge weights may be negative (but the graph has no cycle of negative length), Dijkstra's algorithm may fail: a negative edge may give a shorter walk to a vertex that has already received a permanent label. In this case we can use Ford's algorithm, also known as the *Bellman–Ford algorithm*.

**Algorithm 2.6.2 (Ford's Algorithm)** Let $v_1$ be the source vertex.

1. Initialization: $\pi(1) = 0$ and $\pi(i) = \infty$ ($i = 2, 3, \dots, n$).
2. For $i = 2, 3, \dots, n$ in turn, update
   $$
   \pi(i) \leftarrow \min\left\{ \pi(i),\ \min_{j \in \Gamma^{-}(i)} \big( \pi(j) + w_{ji} \big) \right\}.
   $$
3. If no $\pi(i)$ changed during this round, stop; otherwise go to step 2.

We now explain why the algorithm is correct. On the one hand, every finite value $\pi(s)$ during the algorithm is the length of some walk from $v_1$ to $v_s$; since there is no cycle of negative length, it is at least the shortest path length. On the other hand, at termination $\pi(s) \le \pi(j) + w_{js}$ holds for every edge $(v_j, v_s)$. For any walk $\mu = (v_1, v_{t_h}, \dots, v_{t_1}, v_s)$ from $v_1$ to $v_s$, applying this inequality edge by edge along $\mu$ gives $\pi(s) \le w(\mu)$. Therefore at termination $\pi(s)$ is exactly the length of a shortest path from $v_1$ to $v_s$.

Next, convergence. After the $k$-th round, $\pi(s)$ is at most the length of the shortest walk with at most $k$ edges. Without cycles of negative length, a shortest path has at most $n-1$ edges, so $\pi$ stops changing after at most $n-1$ rounds, and one more round confirms termination; the complexity is $O(nm)$. Conversely, if some label still changes in round $n$, the graph contains a cycle of negative length.

### 2.6.5. Summary

- Positively weighted graphs: Dijkstra's algorithm, $O(n^2)$.
- Unit weights: BFS, $O(n+m)$.
- Arbitrary real weights (no negative cycles): Ford's algorithm, $O(nm)$.

## 2.7. Critical Paths

### 2.7.1. Background

A project consists of a number of tasks with precedence constraints among them. A manager wants to know:

- What is the minimum time needed to complete the whole project?
- Which tasks are critical, that is, would delay the whole project if they were delayed?

### 2.7.2. PT Graphs

A PT graph (potential task graph) describes a project by a directed graph:

- Vertices represent tasks.
- Directed edges represent precedence: if task $v$ can start only after task $u$ has been completed, there is a directed edge $(u, v)$.
- Edge weights represent durations: the weight of the edge $(u, v)$ is the duration of task $u$.

A PT graph has the following features:

- All edges leaving the same vertex have the same weight, namely the duration of the task represented by that vertex.
- There is no directed cycle; otherwise the tasks could not be scheduled.
- There is a vertex of in-degree $0$ (the start) and a vertex of out-degree $0$ (the finish).

### 2.7.3. The Longest Path (Critical Path) Algorithm

The minimum completion time of the project equals the length of a longest path in the PT graph from the start vertex to the finish vertex. Since a PT graph has no directed cycles, its vertices can be renumbered so that every edge goes from a vertex with a smaller number to one with a larger number; this is called *topological sorting*. We can then compute recursively in the order of the numbering. From the viewpoint of [set theory](/1.2), the reachability relation of a PT graph is a **partial order** on the vertex set, and topological sorting extends it to a **total order**.

**Lemma 2.7.1** A directed graph $G$ without directed cycles has a vertex of in-degree $0$ and a vertex of out-degree $0$.

**Proof** Take a maximal directed path in $G$. If its first vertex had a predecessor, that predecessor would either lie on the path (creating a directed cycle) or not lie on it (so the path could be extended backward); both are impossible, so the first vertex has in-degree $0$. Similarly, the last vertex has out-degree $0$. $\square$

**Lemma 2.7.2** If $G$ has no directed cycles, its vertices can be renumbered as $v_1', v_2', \dots, v_n'$ so that $i < j$ for every edge $(v_i', v_j') \in E(G)$.

**Proof** By Lemma 2.7.1, choose a vertex of in-degree $0$, number it $v_1'$ and delete it. The remaining graph still has no directed cycles, so choose a vertex of in-degree $0$ in it and number it $v_2'$, and so on. The tail of every edge is deleted before its head, so the numbering has the required property. $\square$

**Algorithm 2.7.1 (Critical Path Algorithm)**

1. Sort the vertices topologically as $v_1', v_2', \dots, v_n'$, where $v_1'$ is the start vertex and $v_n'$ the finish vertex.
2. Set $\pi(v_1') = 0$.
3. For $j = 2, 3, \dots, n$, compute
   $$
   \pi(v_j') = \max_{v_i' \in \Gamma^{-}(v_j')} \big( \pi(v_i') + w(v_i', v_j') \big).
   $$
4. $\pi(v_j')$ is the earliest start time of task $v_j'$, and $\pi(v_n')$ is the minimum completion time of the whole project; a path attaining the maximum (traced back from $v_n'$ through predecessors attaining the maximum) is a *critical path*.

Both the topological sort and the recursion scan each edge a constant number of times, so the algorithm runs in $O(n+m)$ time.

### 2.7.4. Slack of a Task

Let $\pi(v_n')$ be the minimum completion time of the project, and let $\pi(v_i', v_n')$ be the length of a longest path from $v_i'$ to the finish vertex $v_n'$. To avoid delaying the project, task $v_i'$ must start no later than

$$
\tau(v_i') = \pi(v_n') - \pi(v_i', v_n'),
$$

which is called its latest start time. The slack of task $v_i'$ is the difference between its latest and earliest start times:

$$
t(v_i') = \tau(v_i') - \pi(v_i') \ge 0.
$$

Tasks on a critical path satisfy $\pi(v_i') = \tau(v_i')$, that is, they have zero slack; these are exactly the critical tasks.

### 2.7.5. PERT Graphs

A PERT graph (program evaluation and review technique) is the reverse of a PT graph: directed edges represent tasks and vertices represent events, and the edge weights are the task durations. Critical paths are found in the same way as for PT graphs, with the obvious adjustments.

## 2.8. The Chinese Postman Problem

The *Chinese postman problem* was posed by the Chinese mathematician Guan Meigu: a postman leaves the post office, walks along every street in his district at least once and returns to the post office; how should he choose his route to minimize the total distance? In a connected weighted undirected graph, this asks for a shortest closed walk that traverses every edge at least once. If every vertex has even degree, any Eulerian circuit is optimal. Otherwise some edges must be traversed more than once: the problem reduces to pairing up the odd vertices and adding duplicate edges along shortest paths between paired vertices so that the total added length is minimal, and then finding an Eulerian circuit in the new graph. The problem thus combines Eulerian circuits with shortest paths.

## Summary

| Problem | Criterion or algorithm | Result and complexity |
| :-- | :-- | :-- |
| Is there a walk between two vertices? | Powers of the adjacency matrix, Warshall's algorithm (Algorithm 2.2.1), BFS / DFS | Warshall's algorithm yields the reachability matrix (Theorem 2.2.1) in $O(n^3)$ |
| Eulerian circuit | Connected with all degrees even (Theorem 2.3.1); exactly two odd vertices give an Eulerian trail (Corollary 2.3.1); in a digraph every in-degree must equal the out-degree (Corollary 2.3.2) | Necessary and sufficient, easy to check |
| Hamiltonian path and cycle | Degree sums $\ge n-1$ give a Hamiltonian path (Theorem 2.4.1); degree sums $\ge n$ or minimum degree $\ge n/2$ give a Hamiltonian cycle (Corollaries 2.4.1 and 2.4.2); $G$ has a Hamiltonian cycle if and only if its Hamiltonian closure $C(G)$ does (Theorem 2.4.2) | No simple necessary and sufficient condition; mainly sufficient conditions are used |
| Traveling salesman problem | Branch and bound; under the triangle inequality, the cheapest-insertion algorithm (Algorithm 2.5.1) | NP-hard; cheapest insertion has approximation ratio below 2 (Theorem 2.5.1) |
| Single-source shortest paths | Positive weights: Dijkstra's algorithm (Algorithm 2.6.1); unit weights: BFS; arbitrary real weights without negative cycles: Ford's algorithm (Algorithm 2.6.2) | $O(n^2)$, $O(n+m)$, $O(nm)$ |
| Critical path | Topological sort, then the longest-path recurrence (Algorithm 2.7.1) | $O(n+m)$; tasks with zero slack are the critical tasks |
| Chinese postman problem | Pair up the odd vertices, duplicate edges along shortest paths, then find an Eulerian circuit (Section 2.8) | Combines Eulerian circuits with shortest paths |

The Eulerian and Hamiltonian problems look alike but differ sharply in difficulty: the former depends only on vertex degrees and has a simple necessary and sufficient condition; the latter still has no simple one.
