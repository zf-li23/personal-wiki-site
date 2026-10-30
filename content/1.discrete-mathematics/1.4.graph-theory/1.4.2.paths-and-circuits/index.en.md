---
title: Walks, Paths and Circuits
source_hash: 11a808ba7be7
---

Walks, paths and circuits are the most basic structures in graph theory. In this chapter we first define walks, trails and paths, and their closed versions, in directed and undirected graphs, and discuss connectivity; we then use the adjacency matrix of [Chapter 1](/1.4.1) to count walks and decide reachability, and present two search methods. Next we study the strongly connected components of a digraph, directed acyclic graphs and topological sorting. We then discuss two classical traversal problems and the conditions under which they can be solved: Eulerian circuits, which traverse every edge, and Hamiltonian cycles, which visit every vertex. Finally we turn to optimization problems involving paths: the traveling salesman problem, shortest paths, critical paths and the Chinese postman problem.

## 2.1. Walks, Trails and Paths

When we move along edges from one vertex to another, there are three levels of strictness, depending on whether vertices and edges may be repeated; when the first and last vertex coincide, we obtain the three corresponding closed versions. The table gives the overall picture; precise definitions follow in Sections 2.1.1 and 2.1.2.

| Name | Repeated vertices | Repeated edges | Closed version |
| :-- | :-- | :-- | :-- |
| walk | allowed | allowed | closed walk |
| trail | allowed | not allowed | circuit (closed trail) |
| path | not allowed | not allowed | cycle (closed path) |

Every path is a trail and every trail is a walk; every cycle is a circuit and every circuit is a closed walk. The number of edges of a walk (repeated edges counted with multiplicity) is its length. The terminology varies between textbooks: in particular, "circuit" is used by some authors for what we call a closed walk, and "path" by some for what we call a walk, so definitions must be checked when reading other sources.

![Six kinds of objects in the same graph; the numbers on the edges give the order of traversal. Top row: the walk $a\,b\,e\,b\,c$ uses the edge $be$ twice; the trail $d\,e\,b\,a\,e\,f$ repeats no edge but visits the vertex $e$ twice; the path $d\,a\,b\,c\,f$ repeats no vertex either. Bottom row: the corresponding closed versions, the closed walk $a\,b\,e\,b\,a$, the circuit $a\,b\,e\,c\,f\,e\,d\,a$ (visiting $e$ twice) and the cycle $a\,b\,e\,d\,a$.](./plots/walk-types.py)

### 2.1.1. Walks in Directed Graphs

**Definition 2.1.1 (Directed Walk)** Let $G = (V, E)$ be a directed graph and $P = (e_{i_1}, e_{i_2}, \dots, e_{i_q})$ a sequence of edges of $G$. If for $k = 1, 2, \dots, q-1$ the head of $e_{i_k}$ is the tail of $e_{i_{k+1}}$, then $P$ is called a **directed walk** of length $q$ in $G$. If, in addition, the head of $e_{i_q}$ is the tail of $e_{i_1}$, then $P$ is called a **closed directed walk** in $G$.

- Directed trail (directed circuit): no edge occurs more than once in $P$.
- Directed path (directed cycle): no vertex occurs more than once in $P$ (for a closed walk, the coincidence of the first and last vertex does not count as a repetition). Every directed path is a directed trail.

### 2.1.2. Walks in Undirected Graphs

**Definition 2.1.2 (Walk)** Let $G = (V, E)$ be an undirected graph and $P = (v_{i_1}, e_{i_1}, v_{i_2}, e_{i_2}, \dots, e_{i_{q-1}}, v_{i_q})$ an alternating sequence of vertices and edges. If for every $k$ the vertices $v_{i_k}$ and $v_{i_{k+1}}$ are the two endpoints of $e_{i_k}$, then $P$ is called a **walk** (or chain) in $G$; if $v_{i_q} = v_{i_1}$, then $P$ is called a **closed walk** in $G$.

- **Trail**, **circuit**: a walk, respectively a closed walk, in which no edge is repeated (a circuit is a closed trail).
- **Path**, **cycle**: a walk, respectively a closed walk, in which no vertex is repeated (for a closed walk, the coincidence of the first and last vertex does not count as a repetition). Every path is a trail.

In an undirected graph a cycle of length $1$ is a loop and a cycle of length $2$ consists of two parallel edges, so every cycle in a simple graph has length at least $3$. In a simple graph a walk is determined by its sequence of vertices, and we often write it simply as $v_{i_1} v_{i_2} \cdots v_{i_q}$.

**Property 2.1.1** If there is a walk (directed or undirected) from $u$ to $v$, then there is a path from $u$ to $v$; moreover, a shortest walk from $u$ to $v$ is a path.

**Proof** Take a shortest walk from $u$ to $v$. If it visited some vertex $x$ twice, deleting the closed walk between the two visits would give a shorter walk from $u$ to $v$, a contradiction. Hence a shortest walk repeats no vertex and is a path. $\square$

Thus "there is a walk" and "there is a path" mean the same thing; in a graph with $n$ vertices, a path has length at most $n-1$ and a cycle has length at most $n$.

### 2.1.3. Connected Graphs and Connected Components

**Definition 2.1.3 (Connected Graph)** An undirected graph $G$ is called a **connected graph** if any two of its vertices are joined by a walk; otherwise it is a **disconnected graph**. A directed graph $G$ is called **connected** (or weakly connected) if it is connected when the directions of its edges are ignored.

**Definition 2.1.4 (Connected Component)** A connected subgraph $H$ of $G$ that is not a proper subgraph of any connected subgraph of $G$ is called a **maximal connected subgraph** of $G$, or a **connected component**.

"There is a walk between $u$ and $v$" is an equivalence relation on the vertex set (reflexive by the walk of length $0$, symmetric by walking backward, transitive by concatenating walks), and the connected components are the subgraphs induced by its equivalence classes. Clearly every connected component of $G$ is an **induced subgraph** of $G$, and $G$ is connected if and only if it has exactly one connected component. If $G$ has several connected components, then after numbering the vertices of each component consecutively, both its **adjacency matrix** and its **incidence matrix** are block diagonal.

![A graph with three connected components (left); with the vertices numbered component by component, its adjacency matrix is block diagonal (right, gray entries are 1).](./plots/components.py)

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

The bound is sharp: $K_{n-1}$ together with an isolated vertex has exactly $\frac{1}{2}(n-1)(n-2)$ edges and is disconnected.

### 2.1.5. Summary

- Directed graphs: directed walks and closed directed walks; directed trails (circuits) and directed paths (cycles).
- Undirected graphs: walks (chains) and closed walks; trails and circuits, paths and cycles. A walk always contains a path between its ends (Property 2.1.1).
- Connected graphs and connected components (maximal connected subgraphs).

## 2.2. Counting and Detecting Walks

To decide whether two given vertices of a graph $G$ are joined by a walk, the usual tools are the adjacency matrix method and search methods. The adjacency matrix method rests on the observation that matrix multiplication counts walks.

### 2.2.1. Powers of the Adjacency Matrix

**Theorem 2.2.1** Let $A$ be the **adjacency matrix** of a graph $G$ (a digraph, or an undirected graph in which each edge is regarded as two opposite arcs), and let $k \ge 1$. Then the $(i, j)$ entry $a_{ij}^{(k)}$ of $A^k$ is the number of walks of length $k$ from $v_i$ to $v_j$.

**Proof** By induction on $k$. For $k = 1$, the walks of length $1$ are the edges, and $a_{ij}^{(1)} = a_{ij}$. Suppose the claim holds for $k-1$. Classify the walks of length $k$ from $v_i$ to $v_j$ by their next-to-last vertex $v_l$: each class consists of a walk of length $k-1$ from $v_i$ to $v_l$ followed by the edge $(v_l, v_j)$, and contains $a_{il}^{(k-1)} a_{lj}$ walks. Summing over $l$,

$$
\sum_{l=1}^{n} a_{il}^{(k-1)} a_{lj} = a_{ij}^{(k)},
$$

which is exactly the $(i, j)$ entry of the product $A^{k-1}A$. $\square$

If multiple edges are allowed and $a_{ij}$ is taken to be the number of edges from $v_i$ to $v_j$, the theorem remains true.

**Corollary 2.2.1** Let $G$ be a simple graph with adjacency matrix $A$. Then

1. $(A^2)_{ii} = d(v_i)$, and for $i \ne j$, $(A^2)_{ij}$ is the number of common neighbors of $v_i$ and $v_j$;
2. $\operatorname{tr}(A^3) = 6t$, where $t$ is the number of triangles (cycles of length $3$) in $G$.

**Proof** A walk $v_i v_l v_j$ of length $2$ corresponds to a common neighbor $v_l$; for $i = j$ it corresponds to a neighbor of $v_i$, of which there are $d(v_i)$. In a simple graph a closed walk of length $3$ is a triangle, and each triangle is counted $6$ times ($3$ starting vertices, $2$ directions). $\square$

**Example 2.2.1** For the digraph $D$ of [Example 1.4.1 of Chapter 1](/1.4.1#sec-1.4.1) (edges $v_1 v_2$, $v_1 v_3$, $v_2 v_3$, $v_3 v_4$, $v_4 v_2$),

$$
A^2 = \begin{bmatrix} 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}, \qquad
A^3 = \begin{bmatrix} 0 & 1 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}.
$$

Here $a_{14}^{(2)} = 1$ corresponds to $v_1 v_3 v_4$ and $a_{14}^{(3)} = 1$ to $v_1 v_2 v_3 v_4$; the diagonal entries $a_{22}^{(3)} = a_{33}^{(3)} = a_{44}^{(3)} = 1$ say that each of $v_2, v_3, v_4$ lies on a closed directed walk of length $3$, namely the directed cycle $v_2 v_3 v_4 v_2$. Ignoring directions, the adjacency matrix $A_{\mathrm{u}} = A + A^{\mathsf T}$ of $D$ satisfies $(A_{\mathrm{u}}^2)_{11} = 2 = d(v_1)$, $(A_{\mathrm{u}}^2)_{14} = 2$ (common neighbors $v_2, v_3$) and $\operatorname{tr}(A_{\mathrm{u}}^3) = 12$, so there are $2$ triangles: $v_1 v_2 v_3$ and $v_2 v_3 v_4$.

![Example 2.2.1: three walks in the digraph $D$ (top) and the matrices $A$, $A^2$, $A^3$ (bottom; the red entries correspond to the walks above).](./plots/walk-counting.py)

### 2.2.2. The Reachability Matrix

By Theorem 2.2.1, if we set

$$
S = A + A^2 + \cdots + A^n,
$$

then $s_{ij}$ is the number of walks of length at most $n$ from $v_i$ to $v_j$. By Property 2.1.1, two vertices joined by a walk are joined by a path of length at most $n-1$ (for $i = j$, the shortest closed directed walk through $v_i$ is a cycle of length at most $n$), so it suffices to go up to $A^n$. This method requires $n$ matrix multiplications and takes $O(n^4)$ time.

In practice we often only need to know whether a walk exists. We can then use logical operations (Boolean matrix multiplication) instead:

$$
a_{ij}^{(l)} = \bigvee_{k=1}^{n} \left( a_{ik}^{(l-1)} \land a_{kj} \right), \qquad l = 2, 3, \dots, n,
$$

and set $P = A \lor A^2 \lor \cdots \lor A^n$, called the *reachability matrix*: $p_{ij} = 1$ if and only if there is a walk (of length at least $1$) from $v_i$ to $v_j$. From the viewpoint of [set theory](/1.2), if $A$ is regarded as the relation matrix of a binary relation on the vertex set, then the reachability matrix is the relation matrix of the **transitive closure** of that relation.

### 2.2.3. Warshall's Algorithm

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

**Theorem 2.2.2** Warshall's algorithm produces the reachability matrix of $G$.

**Proof** Let $P^{(i)}$ be the matrix after the $i$-th iteration of the outer loop, with $P^{(0)} = A$. We show by induction on $i$ that $p_{jk}^{(i)} = 1$ if and only if there is a walk from $v_j$ to $v_k$ all of whose internal vertices (the vertices other than its first and last) belong to $\{v_1, \dots, v_i\}$.

For $i = 0$ the set of allowed internal vertices is empty, so such walks are just edges and the claim holds. Suppose the claim holds for $i-1$. As in Property 2.1.1, if a walk with this property exists, then one exists whose internal vertices are all distinct; it either avoids $v_i$ (corresponding to $p_{jk}^{(i-1)} = 1$) or passes through $v_i$ exactly once in its interior. In the latter case it splits into two pieces $v_j \to v_i$ and $v_i \to v_k$, each with internal vertices in $\{v_1, \dots, v_{i-1}\}$ (corresponding to $p_{ji}^{(i-1)} = p_{ik}^{(i-1)} = 1$). Therefore

$$
p_{jk}^{(i)} = p_{jk}^{(i-1)} \lor \left( p_{ji}^{(i-1)} \land p_{ik}^{(i-1)} \right).
$$

During the $i$-th iteration the entries of row $i$ and column $i$ do not change (for example, $p_{ji} \leftarrow p_{ji} \lor (p_{ji} \land p_{ii}) = p_{ji}$), so the in-place updates of the algorithm agree with this formula. For $i = n$ the internal vertices are no longer restricted, and $P^{(n)}$ is the reachability matrix. $\square$

**Example 2.2.2** Run Warshall's algorithm on the digraph $D$ of Example 2.2.1. Pivoting on $v_1$ adds nothing ($v_1$ has no predecessor); pivoting on $v_2$ adds $v_4 \to v_3$; pivoting on $v_3$ adds $v_1, v_2, v_4 \to v_4$; pivoting on $v_4$ adds $v_2 \to v_2$ and $v_3 \to v_2, v_3$. In the final $P$ the first column is zero and every other entry is $1$: $v_1$ reaches every other vertex, and $v_2, v_3, v_4$ are mutually reachable.

![Example 2.2.2: the matrices $P^{(0)}, \dots, P^{(4)}$ of Warshall's algorithm. The shaded row and column belong to the pivot of the round, and red entries are the $1$s gained in that round.](./plots/warshall.py)

The following program checks Theorem 2.2.1 and Example 2.2.2, and reads off mutual reachability (Section 2.3) from the reachability matrix:

```python
# The digraph D of Section 1.4.1: arcs v1->v2, v1->v3, v2->v3, v3->v4, v4->v2
n = 4
A = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]]


def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


# (A^k)_{ij} counts the walks of length k from v_i to v_j
Ak = A
for k in range(2, 4):
    Ak = matmul(Ak, A)
    print(f"A^{k} =", Ak)

# Warshall: after round i, p_jk = 1 iff a walk j -> k uses only v_1..v_i inside
P = [row[:] for row in A]
for i in range(n):
    for j in range(n):
        for k in range(n):
            P[j][k] = P[j][k] or (P[j][i] and P[i][k])
print("reachability P =", P)
# v_j, v_k are mutually reachable iff p_jk = p_kj = 1 (or j = k)
same = [[int(j == k or (P[j][k] and P[k][j])) for k in range(n)] for j in range(n)]
print("mutual reachability =", same)
```

```text
A^2 = [[0, 0, 1, 1], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]]
A^3 = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
reachability P = [[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
mutual reachability = [[1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
```

### 2.2.4. Search Methods

- *Breadth-first search* (BFS): starting from a source vertex $v_0$, first visit all successors of $v_0$ (the first layer), then the successors of those vertices (the second layer), and so on, until the target vertex is found or every reachable vertex has been visited. Visited vertices are labeled to avoid repetition. A forward star is a convenient representation for BFS, which runs in $O(n+m)$ time.
- *Depth-first search* (DFS): starting from $v_0$, choose any successor $v_1$ and record its predecessor, then choose an unvisited successor $v_2$ of $v_1$, and so on; when no further step is possible, backtrack to the predecessor and continue exploring other branches. DFS also runs in $O(n+m)$ time.

Both searches visit every vertex reachable from $v_0$ and leave behind a search tree recording where each vertex was reached from: in the BFS tree the path from $v_0$ to each vertex is shortest (in number of edges), while the DFS tree goes as deep as possible along each path. In an undirected graph, one search from $v_0$ finds the connected component containing $v_0$. Implementations, running times and correctness proofs of both searches are given in [4.3.10](/4.3.10).

![BFS and DFS from $a$ on the same graph (neighbors visited in alphabetical order). BFS proceeds layer by layer, with the BFS tree in blue; the DFS visiting order is written next to each vertex, with the DFS tree in red. Dashed edges are not in the tree.](./plots/bfs-dfs.py)

### 2.2.5. Summary

- Adjacency matrix method: $A^k$ counts walks of length $k$ (Theorem 2.2.1); the reachability matrix is obtained from Boolean matrix powers or Warshall's algorithm (Theorem 2.2.2).
- Search methods: BFS and DFS, suitable for testing connectivity and finding paths.

## 2.3. Strongly Connected Components and Topological Sorting

Connectivity is richer in digraphs than in undirected graphs: that $u$ can reach $v$ does not mean that $v$ can get back to $u$. Grouping mutually reachable vertices together splits a digraph into strongly connected components, which are linked to one another without any cycle; and digraphs without cycles are exactly those whose vertices can be lined up so that every edge points forward. These results are used for critical paths (Section 2.8) and in the [data structures course](/4.3.11).

### 2.3.1. Strongly Connected Graphs and Components

**Definition 2.3.1 (Strongly Connected Graph)** A digraph $G$ is called a **strongly connected graph** if for any two vertices $u, v$ there is a directed walk from $u$ to $v$ and a directed walk from $v$ to $u$.

If every vertex is considered reachable from itself (by the walk of length $0$), then "$u$ and $v$ are mutually reachable" is an equivalence relation on the vertex set: reflexivity and symmetry are clear, and transitivity follows by concatenating walks.

**Definition 2.3.2 (Strongly Connected Component)** The subgraphs of a digraph $G$ induced by the equivalence classes of mutual reachability are called the **strongly connected components** of $G$. Equivalently, the strongly connected components are the maximal strongly connected subgraphs of $G$.

**Theorem 2.3.1** Let $P$ be the reachability matrix of a digraph $G$. Then $v_i$ and $v_j$ ($i \ne j$) lie in the same strongly connected component if and only if $p_{ij} = p_{ji} = 1$. $G$ is strongly connected if and only if every entry of $P \lor I$ equals $1$, and also if and only if $G$ has a closed directed walk passing through every vertex.

**Proof** The first two statements restate the definitions. If $G$ is strongly connected, concatenating directed walks $v_1 \to v_2 \to \cdots \to v_n \to v_1$ gives a closed directed walk through every vertex; conversely, along such a closed walk every vertex can reach every other. $\square$

The reachability matrix in Example 2.2.2 shows that $D$ has two strongly connected components, $\{v_1\}$ and $\{v_2, v_3, v_4\}$. Every vertex lies in exactly one strongly connected component, but some edges (such as $v_1 v_2$ and $v_1 v_3$ in $D$) lie in none.

### 2.3.2. Directed Acyclic Graphs and the Condensation

**Definition 2.3.3 (Directed Acyclic Graph)** A digraph containing no directed cycle is called a **directed acyclic graph** (DAG).

By the same argument as in Property 2.1.1, a directed acyclic graph contains no closed directed walk of positive length either (a shortest one would be a directed cycle).

**Definition 2.3.4 (Condensation)** Let $C_1, \dots, C_r$ be the strongly connected components of a digraph $G$. The digraph with vertices $C_1, \dots, C_r$, having an edge $(C_s, C_t)$ ($s \ne t$) exactly when $G$ has an edge from some vertex of $C_s$ to some vertex of $C_t$, is called the **condensation** of $G$ and is denoted $G^*$.

**Theorem 2.3.2** The condensation $G^*$ of any digraph is a directed acyclic graph.

**Proof** Suppose $G^*$ had a directed cycle $C_{s_1} C_{s_2} \cdots C_{s_k} C_{s_1}$ ($k \ge 2$). Since the vertices inside each component are mutually reachable, all vertices of the components on this cycle would be mutually reachable and would belong to a single strongly connected component, contradicting the fact that $C_{s_1}, \dots, C_{s_k}$ are distinct. $\square$

Every digraph therefore has a two-level structure: inside each strongly connected component one can go around in circles, while the components themselves form a directed acyclic graph. $G$ is strongly connected if and only if $G^*$ has a single vertex, and $G$ is a directed acyclic graph if and only if every strongly connected component has a single vertex.

**Example 2.3.1** A digraph $G$ has vertices $a, \dots, h$ and edges $ab, bc, ca, bd, de, ef, fd, cg, gh, hg, fh$. Its three strongly connected components are $C_1 = \{a, b, c\}$, $C_2 = \{d, e, f\}$ and $C_3 = \{g, h\}$; the edges $bd$, $cg$, $fh$ join different components, so the condensation has the edges $C_1C_2$, $C_1C_3$, $C_2C_3$ and no directed cycle.

![Example 2.3.1: the three strongly connected components of a digraph (same color for the same component, with the edges inside components drawn thick) and its condensation.](./plots/scc.py)

### 2.3.3. Topological Sorting

**Definition 2.3.5 (Topological Sorting)** An arrangement $v_1', v_2', \dots, v_n'$ of the vertices of a digraph $G$ such that $i < j$ for every edge $(v_i', v_j') \in E(G)$ is called a **topological sorting** of $G$.

From the viewpoint of [set theory](/1.2), the reachability relation of a directed acyclic graph (including each vertex itself) is a **partial order** on the vertex set, and a topological sorting extends it to a **total order** (a linear extension).

**Lemma 2.3.1** A directed acyclic graph $G$ has a vertex of in-degree $0$ and a vertex of out-degree $0$.

**Proof** Take a maximal directed path in $G$. If its first vertex had a predecessor, that predecessor would either lie on the path (creating a directed cycle) or not lie on it (so the path could be extended backward); both are impossible, so the first vertex has in-degree $0$. Similarly, the last vertex has out-degree $0$. $\square$

**Theorem 2.3.3** A digraph $G$ has a topological sorting if and only if $G$ is a directed acyclic graph.

**Proof** Necessity: if $G$ has a topological sorting, the numbers of the vertices strictly increase along every directed walk, which therefore cannot return to its start; so $G$ has no directed cycle.

Sufficiency: by Lemma 2.3.1, choose a vertex of in-degree $0$, number it $v_1'$ and delete it. The remaining graph still has no directed cycle, so choose a vertex of in-degree $0$ in it and number it $v_2'$, and so on. The tail of every edge is deleted before its head, so the numbering has the required property. $\square$

The sufficiency proof of Theorem 2.3.3 is an algorithm.

**Algorithm 2.3.1 (Kahn's Algorithm)** Find a topological sorting of a digraph $G$, or determine that $G$ contains a directed cycle.

1. Compute the in-degree $d^-(v)$ of every vertex and put the vertices of in-degree $0$ into a queue.
2. While the queue is nonempty, remove its first vertex $u$ and output it; for each successor $w$ of $u$, set $d^-(w) \leftarrow d^-(w) - 1$, and if this becomes $0$, put $w$ into the queue.
3. Stop when the queue is empty. If all $n$ vertices have been output, the output sequence is a topological sorting; otherwise $G$ contains a directed cycle.

Each edge is processed once, when its tail is output, so with a forward star the algorithm runs in $O(n+m)$ time. If the algorithm stops early, every remaining vertex has in-degree at least $1$ in the remaining subgraph; starting from any remaining vertex and repeatedly stepping back to one of its predecessors, we must repeat a vertex after finitely many steps, which exhibits a directed cycle. Thus the two outcomes of the algorithm correspond exactly to the two cases of Theorem 2.3.3. A topological sorting is in general not unique: whenever the queue holds several vertices, any of them may be chosen.

**Example 2.3.2** A directed acyclic graph has vertices $a, \dots, f$ and edges $ca, cb, ad, bd, be, df, ef$. Initially only $c$ has in-degree $0$. After $c$ is output, $a$ and $b$ have in-degree $0$; outputting $a$, then $b$ (now $d$ and $e$ have in-degree $0$), then $d$, $e$ and $f$ gives the topological sorting $c, a, b, d, e, f$.

![Example 2.3.2: the six steps of Kahn's algorithm (top). Each step outputs a vertex of in-degree 0 (red) and deletes it; current in-degrees are written next to the vertices. Arranging the vertices in a row in the resulting order (bottom), every edge points to the right.](./plots/topo-sort.py)

### 2.3.4. Kosaraju's Algorithm for Strongly Connected Components

Once Warshall's algorithm has produced the reachability matrix, Theorem 2.3.1 reads off the strongly connected components, but this takes $O(n^3)$ time. Depth-first search does it in linear time. In DFS, a vertex is said to finish when all its successors have been processed and the search is about to backtrack from it; let $f(v)$ be the rank of $v$ in the order of finishing. Let $G^{\mathsf T}$ be the graph obtained by reversing every edge of $G$ (its adjacency matrix is $A^{\mathsf T}$); it has the same strongly connected components as $G$.

**Algorithm 2.3.2 (Kosaraju's Algorithm)**

1. Run depth-first search on $G$ (restarting from an unvisited vertex until all vertices are visited), recording the finishing order $f$.
2. Taking unvisited vertices in decreasing order of $f$, run depth-first search in $G^{\mathsf T}$; the set of vertices visited by each search is one strongly connected component.

**Lemma 2.3.2** Let $C$ and $C'$ be distinct strongly connected components of $G$ such that $G$ has an edge from $C$ to $C'$. With $f(C) = \max_{v \in C} f(v)$, we have $f(C) > f(C')$.

**Proof** Let $x$ be the first vertex of $C \cup C'$ to be visited. If $x \in C$, then when $x$ is visited no vertex of $C \cup C'$ has been visited yet, and all of them can be reached from $x$ through unvisited vertices, so DFS visits and finishes them all before $x$ finishes (the white-path property, see [4.3.10](/4.3.10)); hence $f(C) = f(x) > f(C')$. If $x \in C'$, then all vertices of $C'$ finish before $x$ does, so $f(C') = f(x)$; and $C$ cannot be reached from $C'$ (otherwise the two would be mutually reachable and form a single component), so when $x$ finishes the vertices of $C$ are still unvisited and finish later, giving $f(C) > f(C')$. $\square$

**Theorem 2.3.4** Each search in step 2 of Kosaraju's algorithm visits exactly one strongly connected component, and the components are output in a topological sorting of the condensation.

**Proof** The first search in step 2 starts from the vertex $x$ with the largest $f$; let $C$ be its component. Edges leaving $C$ in $G^{\mathsf T}$ correspond to edges of $G$ entering $C$, which by Lemma 2.3.2 can only come from components with larger $f$; there is no component with $f$ larger than $f(C)$, so in $G^{\mathsf T}$ only $C$ itself is reachable from $x$. Since $C$ is still strongly connected in $G^{\mathsf T}$, this search visits exactly $C$. Removing $C$ and repeating the argument for the remaining components proves the first statement. The components are output in decreasing order of $f(C)$, and by Lemma 2.3.2 every edge $(C, C')$ of the condensation satisfies $f(C) > f(C')$, so $C$ is output before $C'$. $\square$

Each of the two searches takes $O(n+m)$ time, so Kosaraju's algorithm runs in $O(n+m)$ time. Tarjan's algorithm finds all strongly connected components in a single DFS; see [4.3.11](/4.3.11).

For the graph of Example 2.3.1, starting at $a$ and visiting neighbors in alphabetical order, the first DFS finishes the vertices in the order $h, g, c, f, e, d, b, a$. The second pass in $G^{\mathsf T}$ starts from $a$, $d$ and $g$ in turn and yields $\{a, b, c\}$, $\{d, e, f\}$ and $\{g, h\}$, which is the topological sorting $C_1, C_2, C_3$ of the condensation. The following program implements both algorithms:

```python
# Strongly connected components (Kosaraju) and topological sorting (Kahn)
from collections import deque

arcs = [("a", "b"), ("b", "c"), ("c", "a"), ("b", "d"), ("d", "e"), ("e", "f"), ("f", "d"),
        ("c", "g"), ("g", "h"), ("h", "g"), ("f", "h")]
V = sorted({x for arc in arcs for x in arc})
out = {v: sorted(w for u, w in arcs if u == v) for v in V}
inn = {v: sorted(u for u, w in arcs if w == v) for v in V}


def dfs(v, nbr, seen, acc):
    seen.add(v)
    for w in nbr[v]:
        if w not in seen:
            dfs(w, nbr, seen, acc)
    acc.append(v)  # appended when v finishes


finish, seen = [], set()
for v in V:
    if v not in seen:
        dfs(v, out, seen, finish)
print("finishing order:", "".join(finish))
sccs, seen = [], set()
for v in reversed(finish):  # second pass on the reversed graph
    if v not in seen:
        comp = []
        dfs(v, inn, seen, comp)
        sccs.append("".join(sorted(comp)))
print("SCCs in topological order:", sccs)


def kahn(V, arcs):
    indeg = {v: 0 for v in V}
    for _, w in arcs:
        indeg[w] += 1
    queue, order = deque(v for v in V if indeg[v] == 0), []
    while queue:
        u = queue.popleft()
        order.append(u)
        for x, w in arcs:
            if x == u:
                indeg[w] -= 1
                if indeg[w] == 0:
                    queue.append(w)
    return order if len(order) == len(V) else None  # None: there is a directed cycle


dag = [("c", "a"), ("c", "b"), ("a", "d"), ("b", "d"), ("b", "e"), ("d", "f"), ("e", "f")]
print("topological order:", kahn("abcdef", dag))
print("on the graph with cycles:", kahn(V, arcs))
```

```text
finishing order: hgcfedba
SCCs in topological order: ['abc', 'def', 'gh']
topological order: ['c', 'a', 'b', 'd', 'e', 'f']
on the graph with cycles: None
```

### 2.3.5. Summary

- The strongly connected components are the classes of mutual reachability (Definition 2.3.2); they can be read off from the reachability matrix (Theorem 2.3.1) or found in $O(n+m)$ time by Kosaraju's algorithm (Algorithm 2.3.2, Theorem 2.3.4).
- The condensation is always a directed acyclic graph (Theorem 2.3.2); a digraph has a topological sorting if and only if it is a directed acyclic graph (Theorem 2.3.3), and Kahn's algorithm (Algorithm 2.3.1) finds a topological sorting or a directed cycle in $O(n+m)$ time.

## 2.4. Eulerian Trails and Circuits

### 2.4.1. Definition and Historical Background

**Definition 2.4.1 (Eulerian Circuit)** In a connected undirected graph $G = (V, E)$, a circuit containing every edge is called an **Eulerian circuit** of $G$; a trail containing every edge is called an **Eulerian trail** of $G$.

The problem of the **Seven Bridges of Königsberg** asks whether one can start somewhere, cross each bridge exactly once and return to the starting point. Regarding the four land masses as vertices and the seven bridges as edges gives a **multigraph** with $4$ vertices and $7$ edges, and the question becomes whether this graph has an Eulerian circuit. The four vertices have degrees $5, 3, 3, 3$, so by Theorem 2.4.1 below the answer is no; by Corollary 2.4.1, there is not even a route that crosses each bridge once without returning to the start (an Eulerian trail).

![The Seven Bridges of Königsberg: the river, the island A and the three land masses B, C, D (left, schematic), and the corresponding multigraph (right), in which all four vertices have odd degree.](./plots/konigsberg.py)

### 2.4.2. Existence of Eulerian Circuits

**Theorem 2.4.1** A connected undirected graph $G$ has an Eulerian circuit if and only if every vertex of $G$ has even degree.

**Proof** Necessity: let $C$ be an Eulerian circuit of $G$; it traverses every edge exactly once. Each time the walk along $C$ passes through a vertex $v$, it enters along one edge and leaves along another (at the starting vertex, pair the first departure with the final arrival). Thus the edges incident with $v$ are paired off, and $d(v)$ is even.

Sufficiency: suppose every vertex has even degree. Start at any vertex $v_0$ and repeatedly move along an edge not yet used. Since all degrees are even, whenever we arrive at a vertex $v \ne v_0$ there is still an unused edge by which to leave $v$, so the walk can only get stuck at $v_0$; since $G$ is finite, it must eventually return to $v_0$, producing a circuit $C$. If $C$ contains all edges, it is an Eulerian circuit. Otherwise let $G_1 = G - C$; every vertex of $G_1$ still has even degree (although $G_1$ may be disconnected). Since $G$ is connected, some vertex $v_i$ on $C$ has nonzero degree in $G_1$. Starting from $v_i$ we obtain in the same way a circuit $C_1$ in $G_1$, and splicing $C_1$ into $C$ at $v_i$ yields a longer circuit. Repeating this process, since there are finitely many edges, we eventually obtain a circuit containing all edges, that is, an Eulerian circuit. $\square$

The sufficiency proof is Hierholzer's algorithm for finding an Eulerian circuit: repeatedly find circuits and splice them together at common vertices; implemented with a stack, it runs in $O(m)$ time.

**Corollary 2.4.1** If a connected undirected graph $G$ has exactly $2$ vertices of odd degree, then $G$ has an Eulerian trail whose ends are these two vertices (but no Eulerian circuit).

**Proof** Let the two odd vertices be $v_i$ and $v_j$. Adding a new edge $(v_i, v_j)$ gives a graph $G'$ in which every vertex has even degree, so by Theorem 2.4.1 $G'$ has an Eulerian circuit $C$. Removing the new edge $(v_i, v_j)$ from $C$ gives an Eulerian trail of $G$ from $v_i$ to $v_j$. $\square$

Conversely, every vertex other than the two ends of an Eulerian trail has even degree, so a connected graph has an Eulerian trail if and only if it has $0$ or $2$ vertices of odd degree.

**Example 2.4.1** If a connected graph $G = (V, E)$ has $k \ge 2$ vertices of odd degree, then $E(G)$ can be partitioned into $k/2$ trails.

**Proof** By Property 1.3.2, $k$ is even. Add $k/2$ new edges among the $k$ odd vertices so that each odd vertex is incident with exactly one new edge, obtaining $G'$. Every vertex of $G'$ has even degree, so $G'$ has an Eulerian circuit $C$. No two of the $k/2$ new edges share an endpoint, so no two of them are consecutive on $C$. Removing them cuts $C$ into $k/2$ pieces, each of which is a trail in $G$, and these trails together cover every edge of $G$ exactly once. $\square$

### 2.4.3. The Directed Case

**Corollary 2.4.2** A connected directed graph $G$ has a directed Eulerian circuit (a directed circuit containing every edge) if and only if the **out-degree** of each vertex equals its **in-degree**, that is, $d^+(v) = d^-(v)$ for all $v$. The proof is similar to that of Theorem 2.4.1 and is left as an exercise.

## 2.5. Hamiltonian Paths and Cycles

### 2.5.1. Definition and Historical Background

**Definition 2.5.1 (Hamiltonian Cycle)** A cycle of an undirected graph $G$ passing through every vertex is called a **Hamiltonian cycle** of $G$, or $H$ cycle for short; a path passing through every vertex is called a **Hamiltonian path**, or $H$ path for short.

An Eulerian circuit traverses all edges (it is a circuit), whereas a Hamiltonian cycle visits all vertices (it is a cycle). Neither implies the other: two triangles sharing a vertex form a graph in which every degree is even, so it has an Eulerian circuit, but the shared vertex would have to be visited twice, so there is no $H$ cycle; $K_4$ has an $H$ cycle, but all four of its vertices have degree $3$, so it has no Eulerian circuit. Deleting **multiple edges** and **loops** does not affect the existence of an $H$ cycle, so one usually studies only **simple graphs**. Unlike the Eulerian case, no simple necessary and sufficient condition is known for a general graph to have an $H$ cycle (the problem is NP-complete); below we give several sufficient conditions.

![Eulerian circuits and Hamiltonian cycles are independent. Left: two triangles sharing the vertex $c$, with the Eulerian circuit $c\,a\,b\,c\,d\,e\,c$ (numbers give the order) and no $H$ cycle. Middle: $K_4$ has the $H$ cycle $a\,b\,c\,d\,a$ (red), but every degree is 3, so there is no Eulerian circuit. Right: $K_5$ has both.](./plots/euler-hamilton.py)

### 2.5.2. A Sufficient Condition for Hamiltonian Paths

**Theorem 2.5.1** Let $G$ be a simple graph on $n$ vertices. If $d(v_i) + d(v_j) \ge n-1$ for any two vertices $v_i, v_j$ of $G$, then $G$ has a Hamiltonian path.

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

### 2.5.3. Sufficient Conditions for Hamiltonian Cycles

**Lemma 2.5.1** Let $G$ be a simple graph with $n \ge 3$ vertices that has an $H$ path but no $H$ cycle, and let $v_1, v_n$ be the ends of the $H$ path. Then $d(v_1) + d(v_n) \le n-1$.

**Proof** The argument is the same as in Step 2 of the proof of Theorem 2.5.1 (with $l = n$): if $d(v_1) + d(v_n) \ge n$, we can construct a cycle through all vertices, that is, an $H$ cycle, a contradiction. $\square$

**Corollary 2.5.1** Let $G$ be a simple graph on $n \ge 3$ vertices. If $d(v_i) + d(v_j) \ge n$ for any two vertices $v_i, v_j$ of $G$, then $G$ has a Hamiltonian cycle.

**Proof** By Theorem 2.5.1, $G$ has an $H$ path; let $v_1, v_n$ be its ends. If $G$ had no $H$ cycle, Lemma 2.5.1 would give $d(v_1) + d(v_n) \le n-1$, contradicting the hypothesis. $\square$

**Corollary 2.5.2** Let $G$ be a simple graph on $n \ge 3$ vertices. If every vertex of $G$ has degree at least $n/2$, then $G$ has an $H$ cycle. This follows at once from Corollary 2.5.1.

Corollaries 2.5.1 and 2.5.2 are known as Ore's theorem and Dirac's theorem. The hypothesis of Corollary 2.5.1 is in fact needed only for nonadjacent pairs (adjacent pairs are never used in the proof), and this observation is the starting point of the closure method below.

### 2.5.4. The Closure of a Graph

**Lemma 2.5.2** Let $G$ be a simple graph on $n \ge 3$ vertices, and let $v_i, v_j$ be nonadjacent vertices with $d(v_i) + d(v_j) \ge n$. Then $G$ has an $H$ cycle if and only if $G + (v_i, v_j)$ has an $H$ cycle.

**Proof** Necessity is obvious. Sufficiency: suppose $G + (v_i, v_j)$ has an $H$ cycle but $G$ has none. Then the $H$ cycle must use the edge $(v_i, v_j)$, and deleting this edge gives an $H$ path in $G$ with ends $v_i, v_j$. By Lemma 2.5.1, $d(v_i) + d(v_j) \le n-1$, a contradiction. $\square$

**Definition 2.5.2 (Hamiltonian Closure)** Let $G$ be a simple graph. If $G$ has nonadjacent vertices $v_i, v_j$ with $d(v_i) + d(v_j) \ge n$, let $G' = G + (v_i, v_j)$; repeat this process on $G'$ until no such pair of vertices remains. The resulting graph is called the **Hamiltonian closure** (or simply the closure) of $G$ and is denoted $C(G)$.

**Lemma 2.5.3** The closure $C(G)$ of a simple graph $G$ is unique; it does not depend on the order in which edges are added.

**Proof** Let $C_1(G)$ and $C_2(G)$ be closures obtained by two orders, where $C_1(G)$ arises by adding the edges $e_1, e_2, \dots, e_p$ in turn and $L_2$ is the set of edges added to obtain $C_2(G)$. If some $e_r \notin L_2$, take the one with the smallest index, say $e_{i+1} = (u, v)$, and let $H = G + \{e_1, \dots, e_i\}$. Since $e_1, \dots, e_i \in L_2$, $H$ is a subgraph of $C_2(G)$; and since $e_{i+1}$ was added to $H$, we have $d_H(u) + d_H(v) \ge n$, so $d(u) + d(v) \ge n$ in $C_2(G)$ as well. But $u$ and $v$ are not adjacent in $C_2(G)$, contradicting the fact that $C_2(G)$ is a closure. Hence $\{e_1, \dots, e_p\} \subseteq L_2$. By symmetry $L_2 \subseteq \{e_1, \dots, e_p\}$, so $C_1(G) = C_2(G)$. $\square$

**Theorem 2.5.2** A simple graph $G$ with $n \ge 3$ vertices has a Hamiltonian cycle if and only if its closure $C(G)$ has a Hamiltonian cycle.

**Proof** By Lemma 2.5.2, no edge addition changes whether an $H$ cycle exists; by Lemma 2.5.3, the closure is uniquely determined. $\square$

**Corollary 2.5.3** Let $G$ be a simple graph on $n \ge 3$ vertices. If $C(G)$ is complete, then $G$ has an $H$ cycle.

### 2.5.5. Summary

- Sufficient condition for an $H$ path in $G$: the degrees of any two vertices sum to at least $n-1$.
- Sufficient conditions for an $H$ cycle ($n \ge 3$): the degrees of any two vertices sum to at least $n$, or the minimum degree is at least $n/2$.
- The closure gives a practical test for $H$ cycles: $G$ has an $H$ cycle if and only if $C(G)$ has one.

## 2.6. The Traveling Salesman Problem

### 2.6.1. Problem Statement and Complexity

The *traveling salesman problem* (TSP) is the following: given $n$ cities and the distances between every two of them (that is, a positively weighted complete graph), find a shortest closed tour that visits every city exactly once and returns to the start, in other words a shortest $H$ cycle.

The complete graph $K_n$ ($n \ge 3$) has $\frac{1}{2}(n-1)!$ distinct $H$ cycles. By Stirling's formula $n! \approx \sqrt{2\pi n}\left(\frac{n}{\mathrm{e}}\right)^n$, this number grows faster than any exponential: for $n = 26$ there are already about $7.8 \times 10^{24}$ of them, and even a supercomputer would need an extremely long time to enumerate them one by one. Exhaustive enumeration is therefore infeasible.

### 2.6.2. Branch and Bound

The basic idea of *branch and bound* is as follows:

1. Sort the edges in increasing order of weight.
2. Search for $H$ cycles depth-first in this order, using the length of the shortest cycle found so far as the bound.
3. During the search, if the length of the current partial path is already at least the bound, prune: do not explore this branch further.
4. Update the bound whenever a shorter cycle is found, until the search terminates.

Pruning can reduce the amount of computation drastically, but the worst-case complexity of branch and bound is still $O(n!)$.

### 2.6.3. An Approximation Algorithm: Cheapest Insertion

When the edge weights satisfy the *triangle inequality*, that is, $w(i, j) \le w(i, k) + w(k, j)$ for all $i, j, k$, the cheapest insertion algorithm finds an approximate solution in polynomial time.

**Algorithm 2.6.1 (Cheapest Insertion)** Start with a subtour consisting of a single vertex. At each step, among all vertices not yet on the tour and all positions where they could be inserted, choose the vertex and position that increase the tour length the least, and insert that vertex there. Repeat until every vertex is on the tour.

**Theorem 2.6.1** Suppose the edge weights of a positively weighted complete graph satisfy the triangle inequality. Let $O_n$ be the length of an optimal tour and $T_n$ the length of the tour produced by cheapest insertion. Then $\dfrac{T_n}{O_n} < 2$. (Proof omitted.)

### 2.6.4. Summary

- TSP is NP-hard, and exhaustive enumeration is infeasible.
- Branch and bound is a common exact method; its efficiency relies on pruning.
- Under the triangle inequality, cheapest insertion finds in polynomial time a tour shorter than twice the optimum.

## 2.7. Shortest Paths

### 2.7.1. Types of Problems

When the length of a walk is the sum of its edge weights, a shortest walk from $u$ to $v$ is called a shortest path; in a positively weighted graph, by the same argument as in Property 2.1.1, a shortest walk is indeed a path. Shortest path problems fall into three types:

1. Shortest paths between two given vertices.
2. Shortest paths from one vertex to all other vertices (single-source shortest paths).
3. Shortest paths between all pairs of vertices.

Solving the second type also solves the first, and the third can be handled by solving the second once for each vertex. Depending on the edge weights, there are three further cases: all weights are positive real numbers (positively weighted graphs); all weights equal $1$; weights are arbitrary real numbers but the graph has no negative cycle (a directed cycle of negative total weight).

### 2.7.2. Dijkstra's Algorithm for Positively Weighted Graphs

**Lemma 2.7.1** In a positively weighted graph $G$, if $P(i)$ is a shortest path from $v_1$ to $v_i$ and $v_j \in P(i)$, then the part $P(j)$ of $P(i)$ from $v_1$ to $v_j$ is a shortest path from $v_1$ to $v_j$.

**Lemma 2.7.2** In a positively weighted graph, a shortest path $P(i)$ is longer than any of its proper initial parts $P(j)$ ($v_j \ne v_i$).

These two lemmas show that the shortest path lengths can be determined vertex by vertex, in increasing order of distance from $v_1$. This is the idea behind *Dijkstra's algorithm*.

**Algorithm 2.7.1 (Dijkstra's Algorithm)** Compute the shortest path lengths from a source vertex $v_1$ to all other vertices of a positively weighted graph. Each vertex $v$ carries a label $\pi(v)$, the length of the shortest walk from $v_1$ to $v$ known so far; labels are either temporary or permanent. The vertex that most recently received a permanent label is called the working vertex.

1. Initialization: set $\pi(v_1) = 0$ as a permanent label and make $v_1$ the working vertex; give every other vertex the temporary label $\pi(v) = \infty$.
2. Let $u$ be the working vertex. For each successor $v$ of $u$ with a temporary label, if $\pi(u) + w(u, v) < \pi(v)$, set $\pi(v) \leftarrow \pi(u) + w(u, v)$.
3. Among all vertices with temporary labels, choose one with the smallest $\pi$, make its label permanent and make it the new working vertex.
4. If every vertex has a permanent label (or the target vertex has one), stop; otherwise go to step 2.

At termination, the permanent label of each vertex is the length of a shortest path from $v_1$ to it. If, whenever $\pi(v)$ is updated, we record the working vertex $u$ as the predecessor of $v$, then tracing predecessors back recovers the shortest paths themselves, and the predecessor edges form a shortest-path tree rooted at $v_1$. With an array implementation the algorithm runs in $O(n^2)$ time; with a priority queue (heap) this drops to $O(m \log n)$. For an undirected graph, regard each edge as two opposite arcs of the same weight.

**Example 2.7.1** A positively weighted undirected graph has $6$ vertices and the edges $v_1v_2$: 7, $v_1v_3$: 9, $v_1v_6$: 14, $v_2v_3$: 10, $v_2v_4$: 15, $v_3v_4$: 11, $v_3v_6$: 2, $v_4v_5$: 6, $v_5v_6$: 9. Starting from $v_1$, the vertices receive permanent labels in the order $v_1$ (0), $v_2$ (7), $v_3$ (9), $v_6$ (11, via $v_3$, shorter than the direct 14), $v_4$ (20, via $v_3$, shorter than 22 via $v_2$) and $v_5$ (20, via $v_6$).

![Example 2.7.1: the six steps of Dijkstra's algorithm. The red vertex receives its permanent label in this step, blue vertices already have permanent labels, and temporary labels are in parentheses; blue edges are the current predecessor edges, and the last panel shows the shortest-path tree.](./plots/dijkstra.py)

```python
# Dijkstra's algorithm with an array (O(n^2)) on the example of Section 2.7.2
import math

edges = [(1, 2, 7), (1, 3, 9), (1, 6, 14), (2, 3, 10), (2, 4, 15), (3, 4, 11), (3, 6, 2), (4, 5, 6),
         (5, 6, 9)]
n = 6
w = {}
for u, v, c in edges:
    w[u, v] = w[v, u] = c  # undirected: an edge is an arc in both directions

pi = {v: math.inf for v in range(1, n + 1)}
pred, permanent = {}, []
pi[1] = 0
while len(permanent) < n:
    # the temporary label with the smallest value becomes permanent
    u = min((v for v in pi if v not in permanent), key=lambda v: (pi[v], v))
    permanent.append(u)
    for v in pi:
        if v not in permanent and (u, v) in w and pi[u] + w[u, v] < pi[v]:
            pi[v], pred[v] = pi[u] + w[u, v], u

print("order made permanent:", permanent)
for v in range(2, n + 1):
    path, x = [v], v
    while x != 1:
        x = pred[x]
        path.append(x)
    print(f"v{v}: length {pi[v]}, path", "-".join(f"v{y}" for y in reversed(path)))
```

```text
order made permanent: [1, 2, 3, 6, 4, 5]
v2: length 7, path v1-v2
v3: length 9, path v1-v3
v4: length 20, path v1-v3-v4
v5: length 20, path v1-v3-v6-v5
v6: length 11, path v1-v3-v6
```

### 2.7.3. Graphs with Unit Weights

When all edge weights equal $1$, single-source shortest paths can be found by **breadth-first search**: expand layer by layer from the source, and the layer at which a vertex is first reached is its shortest path length. If the graph is stored as a forward star or adjacency list, this takes $O(n+m)$ time.

### 2.7.4. Ford's Algorithm for Arbitrary Real Weights

When edge weights may be negative (but the graph has no negative cycle), Dijkstra's algorithm may fail: a negative edge may give a shorter walk to a vertex that has already received a permanent label. In this case we can use Ford's algorithm, also known as the *Bellman–Ford algorithm*.

**Algorithm 2.7.2 (Ford's Algorithm)** Let $v_1$ be the source vertex.

1. Initialization: $\pi(1) = 0$ and $\pi(i) = \infty$ ($i = 2, 3, \dots, n$).
2. For $i = 2, 3, \dots, n$ in turn, update
   $$
   \pi(i) \leftarrow \min\left\{ \pi(i),\ \min_{j \in \Gamma^{-}(i)} \big( \pi(j) + w_{ji} \big) \right\}.
   $$
3. If no $\pi(i)$ changed during this round, stop; otherwise go to step 2.

We now explain why the algorithm is correct. On the one hand, every finite value $\pi(s)$ during the algorithm is the length of some walk from $v_1$ to $v_s$; since there is no negative cycle, deleting the closed walks contained in a walk never makes it longer, so $\pi(s)$ is at least the shortest path length. On the other hand, at termination $\pi(s) \le \pi(j) + w_{js}$ holds for every edge $(v_j, v_s)$. For any walk $\mu = (v_1, v_{t_h}, \dots, v_{t_1}, v_s)$ from $v_1$ to $v_s$, applying this inequality edge by edge along $\mu$ gives $\pi(s) \le w(\mu)$. Therefore at termination $\pi(s)$ is exactly the length of a shortest path from $v_1$ to $v_s$.

Next, convergence. After the $k$-th round, $\pi(s)$ is at most the length of the shortest walk with at most $k$ edges. Without negative cycles, a shortest path has at most $n-1$ edges, so $\pi$ stops changing after at most $n-1$ rounds, and one more round confirms termination; the complexity is $O(nm)$. Conversely, if some label still changes in round $n$, the graph contains a negative cycle.

### 2.7.5. Summary

- Positively weighted graphs: Dijkstra's algorithm, $O(n^2)$.
- Unit weights: BFS, $O(n+m)$.
- Arbitrary real weights (no negative cycles): Ford's algorithm, $O(nm)$.

## 2.8. Critical Paths

### 2.8.1. Background

A project consists of a number of tasks with precedence constraints among them. A manager wants to know:

- What is the minimum time needed to complete the whole project?
- Which tasks are critical, that is, would delay the whole project if they were delayed?

### 2.8.2. PT Graphs

A PT graph (potential task graph) describes a project by a directed graph:

- Vertices represent tasks.
- Directed edges represent precedence: if task $v$ can start only after task $u$ has been completed, there is a directed edge $(u, v)$.
- Edge weights represent durations: the weight of the edge $(u, v)$ is the duration of task $u$.

A PT graph has the following features:

- All edges leaving the same vertex have the same weight, namely the duration of the task represented by that vertex.
- There is no directed cycle (it is a **directed acyclic graph**); otherwise the tasks could not be scheduled.
- There is a vertex of in-degree $0$ (the start) and a vertex of out-degree $0$ (the finish).

### 2.8.3. The Longest Path (Critical Path) Algorithm

The minimum completion time of the project equals the length of a longest path in the PT graph from the start vertex to the finish vertex. Since a PT graph is a directed acyclic graph, Theorem 2.3.3 guarantees a **topological sorting** of its vertices (found by Algorithm 2.3.1), in which every edge goes from an earlier vertex to a later one, and we can then compute recursively in this order: when a vertex is processed, all its predecessors have already been handled.

**Algorithm 2.8.1 (Critical Path Algorithm)**

1. Sort the vertices topologically as $v_1', v_2', \dots, v_n'$, where $v_1'$ is the start vertex and $v_n'$ the finish vertex.
2. Set $\pi(v_1') = 0$.
3. For $j = 2, 3, \dots, n$, compute
   $$
   \pi(v_j') = \max_{v_i' \in \Gamma^{-}(v_j')} \big( \pi(v_i') + w(v_i', v_j') \big).
   $$
4. $\pi(v_j')$ is the earliest start time of task $v_j'$, and $\pi(v_n')$ is the minimum completion time of the whole project; a path attaining the maximum (traced back from $v_n'$ through predecessors attaining the maximum) is a *critical path*.

Both the topological sort and the recursion scan each edge a constant number of times, so the algorithm runs in $O(n+m)$ time. In a general graph the longest path problem contains the Hamiltonian path problem and is NP-hard; it becomes easy in a directed acyclic graph only because we can recurse along a topological order.

### 2.8.4. Slack of a Task

Let $\pi(v_n')$ be the minimum completion time of the project, and let $\pi(v_i', v_n')$ be the length of a longest path from $v_i'$ to the finish vertex $v_n'$. To avoid delaying the project, task $v_i'$ must start no later than

$$
\tau(v_i') = \pi(v_n') - \pi(v_i', v_n'),
$$

which is called its latest start time. The slack of task $v_i'$ is the difference between its latest and earliest start times:

$$
t(v_i') = \tau(v_i') - \pi(v_i') \ge 0.
$$

Tasks on a critical path satisfy $\pi(v_i') = \tau(v_i')$, that is, they have zero slack; these are exactly the critical tasks. The lengths $\pi(v_i', v_n')$ can be computed recursively in reverse topological order: $\pi(v_n', v_n') = 0$ and $\pi(v_i', v_n') = \max_{v_k' \in \Gamma^+(v_i')} \big( w(v_i', v_k') + \pi(v_k', v_n') \big)$.

**Example 2.8.1** A project has a start $s$, a finish $t$ and tasks $A$ (3 days), $B$ (2 days), $C$ (4 days), $D$ (2 days), $E$ (3 days), with precedences $s \to A, B$; $A \to C, D$; $B \to D$; $C, D \to E$; $E \to t$. Recursing along the topological order $s, A, B, C, D, E, t$ gives the earliest start times $\pi(A) = \pi(B) = 0$, $\pi(C) = 3$, $\pi(D) = \max(0 + 3, 0 + 2) = 3$, $\pi(E) = \max(3 + 4, 3 + 2) = 7$ and $\pi(t) = 10$, so the minimum completion time is $10$ days and the critical path is $s\,A\,C\,E\,t$. The reverse recursion gives the latest start times $\tau(B) = 3$ and $\tau(D) = 5$, while every other task has equal earliest and latest start times: $B$ has slack $3$, $D$ has slack $2$, and $A, C, E$ are the critical tasks.

![The PT graph of Example 2.8.1. Edge weights are the durations of the tail tasks, and each vertex is labeled [earliest start, latest start]; the critical path $s\,A\,C\,E\,t$ of length 10 is in red.](./plots/critical-path.py)

### 2.8.5. PERT Graphs

A PERT graph (program evaluation and review technique) is the reverse of a PT graph: directed edges represent tasks and vertices represent events, and the edge weights are the task durations. Critical paths are found in the same way as for PT graphs, with the obvious adjustments.

## 2.9. The Chinese Postman Problem

The *Chinese postman problem* was posed by the Chinese mathematician Guan Meigu: a postman leaves the post office, walks along every street in his district at least once and returns to the post office; how should he choose his route to minimize the total distance? In a connected weighted undirected graph, this asks for a shortest closed walk that traverses every edge at least once. If every vertex has even degree, any Eulerian circuit is optimal. Otherwise some edges must be traversed more than once: the problem reduces to pairing up the odd vertices and adding duplicate edges along shortest paths between paired vertices so that the total added length is minimal, and then finding an Eulerian circuit in the new graph. The problem thus combines Eulerian circuits with shortest paths.

**Example 2.9.1** A weighted graph has the edges $ab$: 1, $bc$: 3, $cd$: 3, $da$: 2, $bd$: 5, of total length $14$. The only odd vertices are $b$ and $d$, and the shortest path between them is $b\,a\,d$ (length $3$, shorter than both the edge $bd$ and the path through $c$), so the edges $ab$ and $ad$ are traversed twice. In the new graph every degree is even, and the Eulerian circuit $a\,b\,c\,d\,b\,a\,d\,a$ is an optimal postman route, of length $14 + 3 = 17$.

![Example 2.9.1: the odd vertices $b, d$ (left); after duplicating the edges $ab$ and $ad$ along the shortest path $b\,a\,d$ (right, red), every degree is even.](./plots/chinese-postman.py)

## Summary

| Problem | Criterion or algorithm | Result and complexity |
| :-- | :-- | :-- |
| Counting walks | Powers $A^k$ of the adjacency matrix (Theorem 2.2.1) | $(A^k)_{ij}$ is the number of walks of length $k$; $\operatorname{tr}(A^3) = 6 \times$ the number of triangles (Corollary 2.2.1) |
| Is there a walk between two vertices? | Reachability matrix, Warshall's algorithm (Algorithm 2.2.1), BFS / DFS | Warshall's algorithm yields the reachability matrix (Theorem 2.2.2) in $O(n^3)$; search in $O(n+m)$ |
| Strongly connected components | Reachability matrix (Theorem 2.3.1); Kosaraju's algorithm (Algorithm 2.3.2) | The condensation is a DAG (Theorem 2.3.2); $O(n+m)$ |
| Topological sorting | Kahn's algorithm (Algorithm 2.3.1) | Exists if and only if the graph is a DAG (Theorem 2.3.3); $O(n+m)$ |
| Eulerian circuit | Connected with all degrees even (Theorem 2.4.1); exactly two odd vertices give an Eulerian trail (Corollary 2.4.1); in a digraph every in-degree must equal the out-degree (Corollary 2.4.2) | Necessary and sufficient, easy to check |
| Hamiltonian path and cycle | Degree sums $\ge n-1$ give a Hamiltonian path (Theorem 2.5.1); degree sums $\ge n$ or minimum degree $\ge n/2$ give a Hamiltonian cycle (Corollaries 2.5.1 and 2.5.2); $G$ has a Hamiltonian cycle if and only if its Hamiltonian closure $C(G)$ does (Theorem 2.5.2) | No simple necessary and sufficient condition; mainly sufficient conditions are used |
| Traveling salesman problem | Branch and bound; under the triangle inequality, the cheapest-insertion algorithm (Algorithm 2.6.1) | NP-hard; cheapest insertion has approximation ratio below 2 (Theorem 2.6.1) |
| Single-source shortest paths | Positive weights: Dijkstra's algorithm (Algorithm 2.7.1); unit weights: BFS; arbitrary real weights without negative cycles: Ford's algorithm (Algorithm 2.7.2) | $O(n^2)$, $O(n+m)$, $O(nm)$ |
| Critical path | Topological sorting, then the longest-path recurrence (Algorithm 2.8.1) | $O(n+m)$; tasks with zero slack are the critical tasks |
| Chinese postman problem | Pair up the odd vertices, duplicate edges along shortest paths, then find an Eulerian circuit (Section 2.9) | Combines Eulerian circuits with shortest paths |

The Eulerian and Hamiltonian problems look alike but differ sharply in difficulty: the former depends only on vertex degrees and has a simple necessary and sufficient condition; the latter still has no simple one. In this chapter the adjacency matrix served as a counting device ($A^k$ counts walks); in [Chapter 3](/1.4.3) we shall see how the incidence matrix $B$ and the Laplacian matrix $L = BB^{\mathsf T}$ count spanning trees.
