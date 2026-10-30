---
title: Introduction and Basic Concepts
source_hash: da4f92026fc8
---

This chapter is the starting point of the graph theory course. We first explain where graph theory sits within discrete mathematics and how it began, then introduce the basic notions of graphs, vertex degrees, subgraphs, graph operations and isomorphism, and finally describe several algebraic representations of graphs used in computers (the adjacency matrix, the incidence matrix, edge lists, forward stars and so on). The walks and circuits, trees, planarity, matchings and connectivity discussed in later chapters are all built on these concepts and representations. The adjacency matrix $A$, the incidence matrix $B$ and the degree matrix $D$ in particular will return again and again: [Chapter 2](/1.4.2) counts walks with powers of $A$, [Chapter 3](/1.4.3) counts spanning trees with $B$ and the Laplacian matrix $L = D - A$, and [Chapter 6](/1.4.6) measures connectivity with the eigenvalues of $L$.

## 1.1. Overview of Discrete Mathematics

Discrete mathematics studies relations among separate, distinct objects. Its main subject is the structure of discrete quantities and the relations among them, and the objects it deals with usually consist of finitely or countably many elements.

Discrete mathematics has four main parts: [mathematical logic](/1.1), [set theory](/1.2), graph theory and [algebraic structures](/1.3). It fits the nature of computer science well and is one of the important theoretical foundations of the field.

## 1.2. Overview of Graph Theory

Graph theory is the branch of mathematics whose objects of study are graphs. We often represent things or phenomena by points and the connections between them by directed or undirected edges; the result is a graph in the sense of graph theory.

- The earliest written record of graph theory is a paper by Euler from 1736. Its original problem, the *Seven Bridges of Königsberg*, had a concrete practical background, and Euler's study of it is regarded as the beginning of graph theory.
- Early graph theory was closely tied to mathematical puzzles (such as the around-the-world puzzle, river-crossing puzzles and the three utilities problem). Since the twentieth century its applications have spread to physics, chemistry, operations research, game theory, computer networks, sociology, linguistics and many other fields.
- The aim of studying graph theory is to master its basic concepts, methods, main theorems and algorithms, and to develop the ability to turn practical problems into graph-theoretic ones.
- The proof techniques used most often in graph theory are proof by contradiction and proof by construction.

## 1.3. Basic Concepts and Definitions

### 1.3.1. Definition of a Graph

**Definition 1.3.1 (Graph)** A pair $G = (V(G), E(G))$ is called a **graph**, where $V(G)$ is a nonempty set, called the **vertex set**, whose elements are the **vertices** of $G$, and $E(G)$ is a set of edges between vertices of $V(G)$, called the **edge set**. We usually write $G = (V, E)$ for short, and write $n = |V|$ for the number of vertices and $m = |E|$ for the number of edges.

- If $V$ and $E$ are both finite, $G$ is called a **finite graph**; otherwise it is an **infinite graph**. This course deals only with finite graphs.
- If all edges of a graph are directed, the graph is a **directed graph**; if all are undirected, it is an **undirected graph**; if it has both directed and undirected edges, it is a **mixed graph**.
- An edge is written $e_k = (v_i, v_j)$. For a directed edge, $v_i$ is its **tail** and $v_j$ its **head**; $v_i$ is a **predecessor** of $v_j$, and $v_j$ is a **successor** of $v_i$. For an undirected edge, $v_i$ and $v_j$ are its **endpoints**. Two vertices joined by an edge are called **adjacent vertices**.
- An edge whose two endpoints coincide is a **loop**. Several edges joining the same pair of vertices are **multiple edges**, and a graph with multiple edges is a **multigraph**.

Older texts sometimes call vertices *nodes*; we use "vertex" throughout.

![Four kinds of graphs: an undirected graph, a directed graph, a mixed graph (two undirected edges and three arcs), and a multigraph with three parallel edges $da$, two parallel edges $ab$ and a loop at $c$.](./plots/graph-types.py)

From the viewpoint of [set theory](/1.2), a directed graph $G = (V, E)$ without multiple edges is exactly a **binary relation** $E \subseteq V \times V$ on the vertex set $V$, and the [adjacency matrix](#sec-1.4.1) introduced below is the relation matrix of this relation. An undirected graph without multiple edges or loops corresponds to an irreflexive, symmetric relation on $V$.

### 1.3.2. Degree of a Vertex

**Definition 1.3.2 (Degree)** In a graph $G = (V, E)$, the number of edges incident with a vertex $v$ is called the **degree** of $v$, written $d(v)$. If $v$ carries loops, each loop contributes $2$ to $d(v)$.

- In a directed graph, the number of edges with tail $v$ is the **out-degree** of $v$, written $d^+(v)$, and the number of edges with head $v$ is the **in-degree** of $v$, written $d^-(v)$. Clearly $d^+(v) + d^-(v) = d(v)$.

For example, in the digraph $D$ of Example 1.4.1 in Section 1.4 we have $d^+(v_1) = 2$, $d^-(v_1) = 0$, $d^+(v_2) = 1$ and $d^-(v_2) = 2$; ignoring directions, the four vertices have degrees $2, 3, 3, 2$, whose sum $10 = 2 \times 5$ agrees with the handshaking lemma below.

### 1.3.3. Simple Graphs, Empty Graphs and Complete Graphs

**Definition 1.3.3 (Simple Graph)** An undirected graph with no loops and at most one edge between any two vertices is called a **simple graph**.

- A simple graph with no edges at all is an **empty graph**; the empty graph on $n$ vertices is denoted $N_n$.
- A simple graph in which every two vertices are adjacent is a **complete graph**; the complete graph on $n$ vertices is denoted $K_n$. Every vertex of $K_n$ has degree $n-1$.

![The empty graph $N_4$ and the complete graphs $K_3$, $K_4$, $K_5$. $K_n$ has $\frac{1}{2}n(n-1)$ edges: 3, 6 and 10 here.](./plots/special-graphs.py)

### 1.3.4. Basic Properties of Graphs

**Property 1.3.1 (Handshaking Lemma)** Let $G = (V, E)$ be a graph with $n$ vertices and $m$ edges. Then the sum of the degrees of the vertices equals twice the number of edges:

$$
\sum_{v \in V} d(v) = 2m
$$

**Proof** Every edge (loops included) contributes exactly $1$ to the degree of each of its two endpoints (a loop contributes $2$ to the degree of its single endpoint), so the degree sum is twice the number of edges. $\square$

The name *handshaking lemma* comes from an intuitive interpretation: when a group of people shake hands, each handshake involves two hands, so the total number of handshakes counted over all people must be even.

**Property 1.3.2** In any graph, the number of vertices of odd degree is even.

**Proof** By Property 1.3.1, the degree sum $2m$ is even. The sum of the degrees of the even-degree vertices is even, so the sum of the degrees of the odd-degree vertices is even as well, and hence the number of odd-degree vertices is even. $\square$

**Property 1.3.3** In a directed graph, the sum of the out-degrees of all vertices equals the sum of their in-degrees, and both equal the number of edges $m$.

**Property 1.3.4** $K_n$ has $\dfrac{1}{2}n(n-1)$ edges.

**Property 1.3.5** Every simple graph with $n \ge 2$ vertices has two vertices of the same degree.

**Proof** In a simple graph the degree of every vertex lies in $\{0, 1, \dots, n-1\}$, but a vertex of degree $0$ and a vertex of degree $n-1$ cannot both exist (the latter is adjacent to all other vertices). Hence the $n$ degrees take at most $n-1$ distinct values, and by the pigeonhole principle two vertices have the same degree. $\square$

### 1.3.5. Weighted Graphs

**Definition 1.3.4 (Weighted Graph)** If each edge $e_k = (v_i, v_j)$ of a graph $G = (V, E)$ is assigned a real number $w_k$, called the **weight** of the edge, then $G$ is called a **weighted graph**. If all weights are positive real numbers, $G$ is a **positively weighted graph**.

### 1.3.6. Subgraphs and Related Notions

**Definition 1.3.5 (Subgraph)** Given a graph $G = (V, E)$, a graph $G' = (V', E')$ with $V' \subseteq V$ and $E' \subseteq E$ is called a **subgraph** of $G$.

- If $V' = V$, then $G'$ is a **spanning subgraph** of $G$.
- If $E'$ consists of exactly those edges of $G$ with both endpoints in $V'$, then $G'$ is the subgraph of $G$ **induced** by $V'$, or an **induced subgraph** for short.
- $G$ itself and the empty graph are the **trivial subgraphs** of $G$.

![A graph $G$ and three kinds of subgraphs. A subgraph only needs its vertices and edges to come from $G$; a spanning subgraph keeps every vertex; the subgraph induced by $\{a, b, d, e\}$ keeps all five edges of $G$ with both ends in that set, namely $ab$, $de$, $ad$, $be$, $ae$.](./plots/subgraphs.py)

### 1.3.7. Operations on Graphs

**Definition 1.3.6 (Graph Operations)** Given two graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$, the following three graphs are called the **union**, the **intersection** and the **symmetric difference** of $G_1$ and $G_2$ (the last keeps what the two graphs do not share):

$$
\begin{aligned}
G_1 \cup G_2 &= (V_1 \cup V_2,\; E_1 \cup E_2), \\
G_1 \cap G_2 &= (V_1 \cap V_2,\; E_1 \cap E_2), \\
G_1 \oplus G_2 &= (V_1 \cup V_2,\; E_1 \oplus E_2),
\end{aligned}
$$

- Deleting a subgraph $H$ from $G$ means deleting the edges of $H$; the result is written $G - H$.
- Deleting a vertex $v$ from $G$ together with all edges incident with it gives the graph $G - v$; deleting an edge $e$ (but keeping its endpoints) gives the graph $G - e$. $G - v$ is an induced subgraph and $G - e$ is a spanning subgraph.
- For a simple graph $G$ on $n$ vertices, $K_n - G$ is called the **complement graph** (or simply the complement) of $G$, written $\overline{G}$: two vertices are adjacent in $\overline{G}$ if and only if they are not adjacent in $G$.

![Union, intersection and symmetric difference. $G_1$ (blue) is a 4-cycle and $G_2$ (red) contains vertex 5; their only common edge is $23$ (green), so $G_1 \cap G_2$ has just this edge and $G_1 \oplus G_2$ drops it while keeping all the others.](./plots/operations.py)

![Two complements: the complement of the path $P_4$ is again $P_4$ ($c\,a\,d\,b$), and the complement of the 5-cycle $C_5$ is a pentagram, again a 5-cycle. A graph isomorphic to its complement is called self-complementary.](./plots/complement.py)

### 1.3.8. Neighborhoods

**Definition 1.3.7 (Neighborhood)** For an undirected graph $G$, the set $\Gamma(v) = \{u \mid (v, u) \in E\}$ is called the **neighborhood** of a vertex $v$. For a directed graph $G$, the sets $\Gamma^+(v)$ and $\Gamma^-(v)$ below are called the **out-neighborhood** (set of successors) and the **in-neighborhood** (set of predecessors) of $v$:

$$
\Gamma^+(v) = \{u \mid (v, u) \in E\}, \qquad \Gamma^-(v) = \{u \mid (u, v) \in E\}.
$$

![The out-neighborhood $\Gamma^+(v) = \{c, d, e\}$ and the in-neighborhood $\Gamma^-(v) = \{a, b, e\}$ of a vertex $v$ in a digraph; $e$ belongs to both. $|\Gamma^+(v)| = d^+(v)$ holds only when there are no multiple edges or loops.](./plots/neighborhoods.py)

### 1.3.9. Graph Isomorphism

**Definition 1.3.8 (Graph Isomorphism)** Two graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are isomorphic, written $G_1 \cong G_2$, if there is a **bijection** $f\colon V_1 \to V_2$ such that $(u, v) \in E_1$ if and only if $(f(u), f(v)) \in E_2$. For multigraphs we further require that corresponding pairs of vertices be joined by the same number of edges.

Isomorphic graphs differ only in the names of their vertices or in the way they are drawn; their structure is identical. Having the same number of vertices, the same number of edges and the same degree sequence is necessary for isomorphism, but not sufficient. In the figure below, the first two graphs are two drawings of $K_{3,3}$, and the identity map $i \mapsto i$ is an isomorphism; the last two graphs both have 6 vertices, 6 edges and every degree equal to 2, but $C_6$ is connected while $2K_3$ (two disjoint triangles) is not, so they are not isomorphic.

![Left pair: two drawings of the same graph $K_{3,3}$ (with the same edge set). Right pair: $C_6$ and $2K_3$ share the degree sequence $(2,2,2,2,2,2)$ but are not isomorphic.](./plots/isomorphism.py)

### 1.3.10. Summary

- Graphs, finite graphs, infinite graphs; directed, undirected and mixed graphs
- Adjacent vertices, tail, head, predecessor, successor, endpoints; loops, multiple edges, multigraphs
- Degree, out-degree, in-degree; the handshaking lemma
- Simple graphs, empty graphs, complete graphs; weights, weighted graphs, positively weighted graphs
- Subgraphs, spanning subgraphs, induced subgraphs, trivial subgraphs
- Union, intersection and symmetric difference of graphs, complements; graph isomorphism

## 1.4. Algebraic Representations of Graphs

### 1.4.1. Adjacency Matrix

The *adjacency matrix* of a directed graph $G$ is the $n \times n$ matrix $A = [a_{ij}]_{n \times n}$ with

$$
a_{ij} = \begin{cases}
1, & (v_i, v_j) \in E, \\
0, & \text{otherwise}.
\end{cases}
$$

The adjacency matrix of an undirected graph is defined in the same way; since $a_{ij} = a_{ji}$, it is symmetric. An adjacency matrix can represent loops but not multiple edges.

**Example 1.4.1** Throughout this section we illustrate the representations on one digraph $D$ with vertices $v_1, \dots, v_4$ and edges $e_1 = (v_1, v_2)$, $e_2 = (v_1, v_3)$, $e_3 = (v_2, v_3)$, $e_4 = (v_3, v_4)$, $e_5 = (v_4, v_2)$. Its adjacency matrix is

$$
A = \begin{bmatrix} 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \end{bmatrix};
$$

the sum of row $i$ is $d^+(v_i)$, and the sum of column $j$ is $d^-(v_j)$.

![The digraph $D$ of Example 1.4.1 (left) and the undirected graph obtained by ignoring directions, with the degrees of its vertices (right).](./plots/example-digraph.py)

### 1.4.2. Weight Matrix

A weighted graph is often represented by its weight matrix $A = [a_{ij}]_{n \times n}$, where

$$
a_{ij} = \begin{cases}
w_{ij}, & (v_i, v_j) \in E, \\
0, & \text{otherwise}.
\end{cases}
$$

A weight matrix can likewise represent loops but not multiple edges.

### 1.4.3. Incidence Matrix

Once the vertices and edges have been numbered, the *incidence matrix* of a directed graph $G$ is the $n \times m$ matrix $B = [b_{ij}]_{n \times m}$ with

$$
b_{ij} = \begin{cases}
1, & e_j = (v_i, v_k) \in E \quad (v_i \text{ is the tail of } e_j), \\
-1, & e_j = (v_k, v_i) \in E \quad (v_i \text{ is the head of } e_j), \\
0, & \text{otherwise}.
\end{cases}
$$

The incidence matrix of an undirected graph $G$ is also an $n \times m$ matrix, with

$$
b_{ij} = \begin{cases}
1, & e_j \text{ is incident with } v_i, \\
0, & \text{otherwise}.
\end{cases}
$$

Incidence matrices have the following properties:

- Directed graphs: every column has exactly two nonzero entries, $1$ and $-1$; the number of nonzero entries in row $i$ equals the degree of $v_i$, the number of $1$s being its out-degree and the number of $-1$s its in-degree.
- Undirected graphs: every column has exactly two $1$s; the number of $1$s in row $i$ equals the degree of $v_i$.
- An incidence matrix can represent multiple edges but not loops.

The incidence matrix of $D$ in Example 1.4.1 is

$$
B = \begin{bmatrix} 1 & 1 & 0 & 0 & 0 \\ -1 & 0 & 1 & 0 & -1 \\ 0 & -1 & -1 & 1 & 0 \\ 0 & 0 & 0 & -1 & 1 \end{bmatrix};
$$

in each column, the $1$ sits in the row of the tail and the $-1$ in the row of the head.

### 1.4.4. Edge List

An edge list consists of two $m$-dimensional vectors $A$ and $B$: if $e_k = (v_i, v_j)$, then $A(k) = i$ and $B(k) = j$. If $G$ is weighted, a third $m$-dimensional vector $Z$ is added, with $Z(k) = w_k$ the weight of $e_k$. An edge list is essentially a compressed form of the incidence matrix, and it overcomes the incidence matrix's inability to represent loops. In Example 1.4.1, $A = (1, 1, 2, 3, 4)$ and $B = (2, 3, 3, 4, 2)$.

### 1.4.5. Forward Star

A forward star stores the successors of each vertex contiguously. For a directed graph it consists of an $(n+1)$-dimensional vector $A$ and an $m$-dimensional vector $B$: $B$ lists the indices of the successors of $v_1, v_2, \dots, v_n$ in turn, $A(i)$ is the position in $B$ of the first successor of $v_i$, and by convention $A(n+1) = m+1$. For a weighted graph, an $m$-dimensional vector $Z$ stores the weights of the corresponding edges.

A forward star satisfies

$$
d^+(v_i) = A(i+1) - A(i), \qquad A(i) = \sum_{j=1}^{i-1} d^+(v_j) + 1,
$$

and $B(A(i)), B(A(i)+1), \dots, B(A(i+1)-1)$ are exactly the successors of $v_i$. In effect, a forward star is obtained by compressing the rows of the adjacency matrix. In Example 1.4.1, $A = (1, 3, 4, 5, 6)$ and $B = (2, 3, 3, 4, 2)$: the successors of $v_1$ are $B(1), B(2) = 2, 3$, and $d^+(v_1) = A(2) - A(1) = 2$.

In the forward star of an undirected graph, $B$ lists the neighbors of each vertex, so every edge appears twice and $B$ has dimension $2m$; correspondingly, $Z$ also has dimension $2m$.

### 1.4.6. Reverse Star

A reverse star is the opposite of a forward star: it stores the predecessors of each vertex contiguously, and in effect is obtained by compressing the columns of the adjacency matrix of a directed graph.

### 1.4.7. Adjacency List

An adjacency list represents a graph by singly linked lists: each vertex has its own list, whose nodes record the successors of that vertex one by one, each node holding three fields, namely the vertex index, the weight of the edge and the address of the next node.

### 1.4.8. The Degree Matrix and the Three Matrices

The adjacency matrix records vertex–vertex relations and the incidence matrix vertex–edge relations; adding the diagonal matrix of degrees gives the three matrices that run through the later chapters.

**Definition 1.4.1 (Degree Matrix)** Let $G$ have vertices $v_1, \dots, v_n$. The diagonal matrix $D = \operatorname{diag}(d(v_1), \dots, d(v_n))$ is called the **degree matrix** of $G$. For a digraph one can also define the out-degree matrix $D^+ = \operatorname{diag}(d^+(v_i))$ and the in-degree matrix $D^- = \operatorname{diag}(d^-(v_i))$, so that $D = D^+ + D^-$.

With the all-ones vector $\boldsymbol{1}$, degrees become matrix operations: in a digraph the entries of $A\boldsymbol{1}$ are the out-degrees and those of $A^{\mathsf T}\boldsymbol{1}$ the in-degrees; in a simple undirected graph the entries of $A\boldsymbol{1}$ are the degrees, and $\boldsymbol{1}^{\mathsf T}A\boldsymbol{1} = \sum_v d(v) = 2m$, which is exactly the handshaking lemma (Property 1.3.1).

**Property 1.4.1** Let $G$ be a directed graph without loops, $B$ its incidence matrix, $A_{\mathrm{u}}$ the adjacency matrix of the undirected graph obtained by ignoring directions (where $(A_{\mathrm{u}})_{ik}$ is the number of edges between $v_i$ and $v_k$), and $D$ its degree matrix. Then

$$
BB^{\mathsf T} = D - A_{\mathrm{u}}.
$$

**Proof** $(BB^{\mathsf T})_{ik} = \sum_{j=1}^m b_{ij}b_{kj}$. For $i = k$, $b_{ij}^2 = 1$ exactly when $e_j$ is incident with $v_i$, so the sum is $d(v_i)$. For $i \ne k$, $b_{ij}b_{kj} \ne 0$ exactly when $e_j$ joins $v_i$ and $v_k$; then one factor is $1$ and the other $-1$, so the product is $-1$, and the sum is minus the number of edges between $v_i$ and $v_k$. $\square$

The matrix $D - A_{\mathrm{u}}$ depends only on the undirected graph, not on the directions given to its edges; it is the **Laplacian matrix** $L$. For an undirected graph $G$, any orientation gives an incidence matrix $B$ with $L = D - A = BB^{\mathsf T}$. [Chapter 3](/1.4.3) counts spanning trees with its cofactors (the matrix-tree theorem), and [Chapter 6](/1.4.6) uses its second smallest eigenvalue to measure how robustly a graph is connected.

**Example 1.4.2** For the digraph $D$ of Example 1.4.1 the degree matrix is $\operatorname{diag}(2, 3, 3, 2)$, and a direct computation gives

$$
BB^{\mathsf T} = \begin{bmatrix} 2 & -1 & -1 & 0 \\ -1 & 3 & -1 & -1 \\ -1 & -1 & 3 & -1 \\ 0 & -1 & -1 & 2 \end{bmatrix} = D - A_{\mathrm{u}};
$$

every row sums to $0$, that is, $L\boldsymbol{1} = \boldsymbol{0}$.

![The three matrices of Example 1.4.1: the adjacency matrix $A$ (vertex by vertex), the incidence matrix $B$ (vertex by edge, $1$ at the tail and $-1$ at the head), and $BB^{\mathsf T}$, which equals the degree matrix minus the undirected adjacency matrix $A + A^{\mathsf T}$.](./plots/matrices.py)

The following program starts from the edge list, builds the adjacency matrix, the incidence matrix and the forward star, and checks the handshaking lemma and Property 1.4.1:

```python
# Directed example graph of 1.4: vertices v1..v4, edges e1..e5 as (tail, head)
n = 4
edges = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 2)]
m = len(edges)

# adjacency matrix A (n x n) and incidence matrix B (n x m)
A = [[0] * n for _ in range(n)]
B = [[0] * m for _ in range(n)]
for j, (u, v) in enumerate(edges):
    A[u - 1][v - 1] = 1
    B[u - 1][j], B[v - 1][j] = 1, -1

# degree matrix D of the underlying undirected graph, and L = D - A - A^T
deg = [sum(abs(x) for x in row) for row in B]
L = [[(deg[i] if i == k else 0) - A[i][k] - A[k][i] for k in range(n)] for i in range(n)]
BBt = [[sum(B[i][j] * B[k][j] for j in range(m)) for k in range(n)] for i in range(n)]

# forward star: successors of v1, v2, ... stored contiguously in FB, FA(i) points into FB
FA, FB = [1], []
for i in range(1, n + 1):
    FB += [v for (u, v) in edges if u == i]
    FA.append(len(FB) + 1)

print("A =", A)
print("B =", B)
print("degrees:", deg, " sum =", sum(deg), "= 2m =", 2 * m)
print("L = D - A_u =", L)
print("B B^T == L:", BBt == L)
print("forward star  A:", FA, " B:", FB)
```

```text
A = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
B = [[1, 1, 0, 0, 0], [-1, 0, 1, 0, -1], [0, -1, -1, 1, 0], [0, 0, 0, -1, 1]]
degrees: [2, 3, 3, 2]  sum = 10 = 2m = 10
L = D - A_u = [[2, -1, -1, 0], [-1, 3, -1, -1], [-1, -1, 3, -1], [0, -1, -1, 2]]
B B^T == L: True
forward star  A: [1, 3, 4, 5, 6]  B: [2, 3, 3, 4, 2]
```

## Summary

- A graph $G = (V, E)$ consists of a vertex set and an edge set (Definition 1.3.1); Section 1.3.10 lists the basic terminology of this chapter. The most frequently used counting result is the handshaking lemma $\sum_{v} d(v) = 2m$ (Property 1.3.1), which implies that the number of vertices of odd degree is even (Property 1.3.2); in a digraph the sum of out-degrees equals the sum of in-degrees (Property 1.3.3).
- Subgraphs, spanning subgraphs and induced subgraphs (Definition 1.3.5), graph operations (Definition 1.3.6) and isomorphism (Definition 1.3.8) form the basic language in which later chapters describe the structure of graphs.
- Representations of graphs in a computer (Section 1.4):

  | Representation | Size | Features |
  | :-- | :-- | :-- |
  | Adjacency matrix, weight matrix | $n \times n$ | Fastest test of adjacency; can represent loops but not multiple edges |
  | Incidence matrix | $n \times m$ | One column per edge; cannot represent loops |
  | Edge list | $2m$ (plus $m$ for weights) | A compressed form of the incidence matrix that can represent loops |
  | Forward star, reverse star | $(n+1) + m$ | Compress the rows and columns of the adjacency matrix, respectively; $d^+(v_i) = A(i+1) - A(i)$ |
  | Adjacency list | $n$ linked lists | One singly linked list per vertex, recording its direct successors in turn |

- The three matrices (Section 1.4.8): the adjacency matrix $A$, the incidence matrix $B$ and the degree matrix $D$ (Definition 1.4.1) satisfy $BB^{\mathsf T} = D - A_{\mathrm{u}} = L$ (Property 1.4.1). Later chapters use $A^k$ (Chapter 2, counting walks), the cofactors of $L$ (Chapter 3, the matrix-tree theorem) and the eigenvalues of $L$ (Chapter 6, algebraic connectivity).

Judging by size, sparse graphs ($m$ much smaller than $n^2$) are best stored as edge lists, forward stars or adjacency lists, while dense graphs, or applications that test adjacency frequently, call for the adjacency matrix.
