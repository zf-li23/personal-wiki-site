---
title: Trees
source_hash: 16975a047083
---

Trees are among the most important notions in graph theory and have wide applications in computer science (file systems, coding, searching, games and more). In the mid-nineteenth century the British mathematician Cayley studied the enumeration of trees and used it to count the isomers of chemical compounds, one of the earliest applications of trees. In this chapter we first give the definition of a tree and several equivalent characterizations. We then study spanning trees algebraically by means of the incidence matrix, the cycle matrix and the cut-set matrix, including how to count and generate spanning trees. Finally we discuss two optimization problems involving trees: Huffman trees and minimum spanning trees.

## 3.1. Definitions

### 3.1.1. Definition and Basic Properties of Trees

**Definition 3.1.1 (Tree)** A connected graph containing no cycle is called a **tree**, usually denoted $T$. The edges of a tree are called its **branches**, and a vertex of degree $1$ is called a **leaf**.

**Definition 3.1.2 (Cut Edge)** Let $e$ be an edge of a graph $G$. If $G - e$ has more **connected components** than $G$, then $e$ is called a **cut edge** of $G$.

**Theorem 3.1.1** An edge $e = (u, v)$ is a cut edge if and only if $e$ lies on no cycle of $G$.

**Proof** Necessity: if $e$ lies on a cycle, the rest of the cycle is a path from $u$ to $v$ in $G - e$, so $u$ and $v$ remain in the same connected component, deleting $e$ does not increase the number of components, and $e$ is not a cut edge.

Sufficiency: if $e$ is not a cut edge, then $G - e$ has as many connected components as $G$, so $u$ and $v$ are still in the same component of $G - e$. Hence $G - e$ contains a path $P(u, v)$, and $P(u, v)$ together with $e$ forms a cycle. $\square$

Since a tree contains no cycle, Theorem 3.1.1 shows that every edge of a tree is a cut edge. Trees are thus "minimally" connected graphs: deleting any edge disconnects them.

### 3.1.2. Equivalent Definitions of Trees

**Theorem 3.1.2** Let $T$ be a graph with $n \ge 2$ vertices. The following statements are equivalent:

1. $T$ is connected and has no cycle (that is, $T$ is a tree).
2. $T$ is connected and every edge is a cut edge.
3. $T$ is connected and has $n-1$ edges.
4. $T$ has $n-1$ edges and no cycle.
5. Any two vertices of $T$ are joined by a unique path.
6. $T$ has no cycle, but adding an edge between any two nonadjacent vertices creates exactly one cycle.

**Proof** We prove (1)→(2)→(3)→(4)→(5)→(6)→(1).

(1)→(2): this follows directly from Theorem 3.1.1.

(2)→(3): we use induction on the number of vertices $n$, also allowing $n = 1$ (then there are no edges and the claim holds). Suppose the claim holds for graphs with fewer than $n$ vertices. Take any edge $e$. Since $e$ is a cut edge, $T - e$ has exactly two connected components $T_1$ and $T_2$; each is still connected and each of its edges is a cut edge (an edge of $T_i$ lies on no cycle of $T$, hence on no cycle of $T_i$). By the induction hypothesis $m(T_1) = n(T_1) - 1$ and $m(T_2) = n(T_2) - 1$, so $m(T) = m(T_1) + m(T_2) + 1 = n(T) - 1$.

(3)→(4): suppose, for contradiction, that $T$ contains a cycle, and take a cycle with $k$ vertices and $k$ edges. Since $T$ is connected, the remaining $n-k$ vertices can be attached one at a time to the part already built, each by a different edge, so at least $n-k$ further edges are needed. The total number of edges is then at least $k + (n-k) = n$, contradicting $m = n-1$.

(4)→(5): first, existence. Suppose $T$ has $p$ connected components with $n_1, \dots, n_p$ vertices. Each component is connected and has no cycle, so by (1)→(3), already proved, it has $n_i - 1$ edges. Hence $n - 1 = \sum_i (n_i - 1) = n - p$, so $p = 1$: $T$ is connected and any two vertices are joined by a path. Next, uniqueness: if two vertices were joined by two different paths, their union would contain a cycle, contradicting the absence of cycles.

(5)→(6): if $T$ contained a cycle, any two vertices on it would be joined by two different paths, contradicting (5); so $T$ has no cycle. After adding an edge $e$ between nonadjacent vertices $u, v$, every cycle of the new graph contains $e$ (since $T$ has none), and removing $e$ from such a cycle leaves a path from $u$ to $v$ in $T$. That path is unique, so there is exactly one cycle.

(6)→(1): it suffices to show that $T$ is connected. If it were not, adding an edge between vertices in two different components would create no cycle, contradicting (6). $\square$

**Theorem 3.1.3** A tree $T$ with $n \ge 2$ vertices has at least two leaves.

**Proof** $T$ is connected and $n \ge 2$, so no vertex has degree $0$. If $T$ had at most one leaf, the other $n-1$ or more vertices would all have degree at least $2$, so $2m = \sum d(v) \ge 2(n-1) + 1 = 2n - 1$; but a tree has $m = n-1$, so $2m = 2n - 2$, a contradiction. $\square$

### 3.1.3. Spanning Trees and Cotrees

**Definition 3.1.3 (Spanning Tree)** If $T$ is a **spanning subgraph** of a graph $G$ and $T$ is a tree, then $T$ is called a **spanning tree** of $G$. The subgraph obtained from $G$ by deleting the edges of $T$ is called the **cotree** of $T$, written $\overline{T}$; the edges of the cotree are called **chords**.

Every connected graph has a spanning tree: keep deleting edges that lie on cycles until no cycle remains. If $G$ is connected, $T$ has $n-1$ branches and the cotree has $m-n+1$ chords.

## 3.2. The Reduced Incidence Matrix and Its Properties

To study trees algebraically, we first examine the linear dependence and the rank of the incidence matrix of a connected directed graph. Throughout this section, $B$ denotes the **incidence matrix** of a directed graph without loops (defined in [Section 1.4.3 of Chapter 1](/1.4.1#sec-1.4.3)).

### 3.2.1. Definition of the Reduced Incidence Matrix

**Definition 3.2.1 (Reduced Incidence Matrix)** Deleting from the incidence matrix of a connected directed graph $G = (V, E)$ the row corresponding to any one vertex $v_k$ gives an $(n-1) \times m$ matrix $B_k$, called a **reduced incidence matrix** of $G$.

### 3.2.2. The Rank of the Incidence Matrix

**Theorem 3.2.1** The incidence matrix $B$ of a directed graph $G$ has rank $\operatorname{rank} B < n$.

**Proof** Each column of $B$ contains exactly one $1$ and one $-1$, so the sum of the $n$ row vectors is the zero vector. The rows are linearly dependent, and the rank is less than $n$. $\square$

**Theorem 3.2.2** Let $B_0$ be any $k \times k$ square submatrix of the incidence matrix $B$ of a directed graph $G$. Then $\det B_0$ is $0$, $1$ or $-1$.

**Proof** By induction on $k$; the case $k = 1$ is obvious. For general $k$: if $B_0$ has a zero column, then $\det B_0 = 0$. If every column of $B_0$ has two nonzero entries, then each column consists of exactly one $1$ and one $-1$, the rows sum to the zero vector, and $\det B_0 = 0$. Otherwise some column of $B_0$ has a single nonzero entry $\pm 1$; expanding along that column, $\det B_0$ equals $\pm$ the determinant of a $(k-1) \times (k-1)$ submatrix, and the induction hypothesis gives the claim. $\square$

**Theorem 3.2.3** If $B$ is the incidence matrix of a connected directed graph $G$, then $\operatorname{rank} B = n-1$.

**Proof** Let the row vector $\boldsymbol{x} = (x_1, \dots, x_n)$ satisfy $\boldsymbol{x}B = \boldsymbol{0}$. For each edge $e = (v_i, v_j)$, the component of $\boldsymbol{x}B$ corresponding to $e$ is $x_i - x_j$, so adjacent vertices have equal values of $x_i$; since $G$ is connected, $x_1 = x_2 = \cdots = x_n$. Thus the solution space of $\boldsymbol{x}B = \boldsymbol{0}$ is one-dimensional, and $\operatorname{rank} B = n - 1$. $\square$

**Theorem 3.2.4** The reduced incidence matrix $B_k$ of a connected directed graph $G$ has rank $\operatorname{rank} B_k = n-1$; that is, the $n-1$ rows of $B_k$ are linearly independent.

**Proof** If a nontrivial linear combination of the rows of $B_k$ were zero, then setting the coefficient $x_k = 0$ would give a solution $\boldsymbol{x}$ of $\boldsymbol{x}B = \boldsymbol{0}$ whose components are not all equal, contradicting the proof of Theorem 3.2.3. $\square$

### 3.2.3. Reduced Incidence Matrices and Cycles

**Theorem 3.2.5** Let $B_k$ be a reduced incidence matrix of a connected directed graph $G$, and let $C$ be a circuit in $G$. Then the columns of $B_k$ corresponding to the edges of $C$ are linearly dependent.

**Proof** The circuit $C$ contains a cycle, so it suffices to prove the claim for cycles. Let $C$ be a cycle with $l$ vertices and $l$ edges. In $B$, the columns of these $l$ edges have nonzero entries only in the rows of the $l$ vertices of $C$, and this part forms the incidence matrix $B(C)$ of $C$ itself, an $l \times l$ matrix. Since $C$ is a connected graph, Theorem 3.2.3 gives $\operatorname{rank} B(C) = l - 1 < l$, so these $l$ columns are linearly dependent. The corresponding columns of $B_k$ are obtained by deleting one component and remain linearly dependent. $\square$

**Corollary 3.2.2** Let $H$ be a subgraph of a connected directed graph $G$. If $H$ contains a cycle, then the columns of the reduced incidence matrix of $G$ corresponding to the edges of $H$ are linearly dependent.

### 3.2.4. Reduced Incidence Matrices and Spanning Trees

**Theorem 3.2.6** Let $B_k$ be a reduced incidence matrix of a connected directed graph $G$. An $(n-1) \times (n-1)$ submatrix of $B_k$ has nonzero determinant if and only if the edges corresponding to its columns form a spanning tree of $G$.

**Proof** Necessity: if an $(n-1) \times (n-1)$ submatrix has nonzero determinant, its $n-1$ columns are linearly independent, so by Corollary 3.2.2 these edges contain no cycle. They are $n-1$ edges on $n$ vertices without a cycle, so by Theorem 3.1.2 they form a tree, that is, a spanning tree of $G$.

Sufficiency: suppose these $n-1$ edges form a spanning tree $T$. The submatrix is then exactly the reduced incidence matrix of $T$ obtained by deleting the row of $v_k$. Since $T$ is a connected directed graph on $n$ vertices, Theorem 3.2.4 shows that this matrix has rank $n-1$, so its determinant is nonzero. $\square$

## 3.3. Counting Spanning Trees

The number of spanning trees of a connected graph $G$ can be computed as a **determinant**.

### 3.3.1. The Binet–Cauchy Theorem

**Theorem 3.3.1 (Binet–Cauchy Theorem)** Let $A = (a_{ij})_{m \times n}$ and $B = (b_{ij})_{n \times m}$ with $m \le n$. Then

$$
\det(AB) = \sum_i A_i B_i,
$$

where $A_i$ is the $m \times m$ determinant formed by some $m$ columns of $A$, $B_i$ is the $m \times m$ determinant formed by the corresponding $m$ rows of $B$, and the sum runs over all $\binom{n}{m}$ choices.

### 3.3.2. Counting Spanning Trees of Connected Directed Graphs

**Theorem 3.3.2** Let $B_k$ be a reduced incidence matrix of a connected directed graph $G$. Then the number of distinct spanning trees of $G$ is $\det(B_k B_k^{\mathsf T})$.

**Proof** By the Binet–Cauchy theorem,

$$
\det(B_k B_k^{\mathsf T}) = \sum_i \det B_i \cdot \det B_i^{\mathsf T} = \sum_i (\det B_i)^2,
$$

where $B_i$ ranges over all $(n-1) \times (n-1)$ submatrices of $B_k$. By Theorem 3.2.6, $\det B_i \ne 0$ if and only if the corresponding edges form a spanning tree, and by Theorem 3.2.2, $\det B_i \in \{0, \pm 1\}$. Hence $(\det B_i)^2 = 1$ exactly when the edges form a spanning tree and $0$ otherwise, and the sum is the number of spanning trees. $\square$

**Remark** Let $D$ be the diagonal matrix of vertex degrees and $A$ the **adjacency matrix** with directions ignored (multiple edges counted with multiplicity). The matrix $L = D - A$ is called the *Laplacian matrix* of $G$. Since $B B^{\mathsf T} = L$, the matrix $B_k B_k^{\mathsf T}$ is obtained from $L$ by deleting the $k$-th row and the $k$-th column. Theorem 3.3.2 can therefore also be stated as follows: the number of spanning trees of $G$ equals the cofactor of any diagonal entry of its Laplacian matrix. This is Kirchhoff's *matrix-tree theorem*.

### 3.3.3. Counting Arborescences

**Definition 3.3.1 (Arborescence)** Let $T$ be a directed tree (a directed graph that is a tree when directions are ignored). If some vertex $v_0$ of $T$ has in-degree $0$ and every other vertex has in-degree $1$, then $T$ is called an **arborescence** (or out-tree) rooted at $v_0$, also called a **rooted tree**.

**Theorem 3.3.3** The number of arborescences rooted at $v_k$ in a connected directed graph $G$ is $\det(\bar{B}_k B_k^{\mathsf T})$, where $\bar{B}_k$ is the matrix obtained from $B_k$ by replacing every entry $1$ with $0$.

**Proof** By the Binet–Cauchy theorem, $\det(\bar{B}_k B_k^{\mathsf T}) = \sum_i \det \bar{B}_i \cdot \det B_i$, where $B_i$ ranges over the $(n-1) \times (n-1)$ submatrices of $B_k$ and $\bar{B}_i$ is the corresponding submatrix of $\bar{B}_k$. If the corresponding edges do not form a spanning tree, then $\det B_i = 0$. If they form a spanning tree that is not an arborescence rooted at $v_k$, then the heads of the $n-1$ edges cannot be exactly the $n-1$ vertices other than $v_k$, so some vertex $v \ne v_k$ is the head of no edge; the row of $v$ in $\bar{B}_i$ is then zero, and $\det \bar{B}_i = 0$. If they form an arborescence rooted at $v_k$, then ordering rows and columns simultaneously by matching each edge with its head, and ordering vertices by their distance from the root, turns $B_i$ into a triangular matrix with all diagonal entries $-1$ and $\bar{B}_i$ into a diagonal matrix with all diagonal entries $-1$. The two determinants are equal and equal to $\pm 1$, so their product is $1$. Summing gives the number of arborescences. $\square$

**Remark** Spanning trees that contain, or avoid, a given edge $e$ can also be counted: the spanning trees avoiding $e$ are exactly the spanning trees of $G - e$, and the spanning trees containing $e$ correspond bijectively to the spanning trees of the graph obtained by contracting $e$ (merging its two endpoints).

### 3.3.4. Counting Spanning Trees of Connected Undirected Graphs

Orienting each edge of a connected undirected graph $G$ arbitrarily gives a connected directed graph $G'$. As edge sets, the spanning trees of $G'$ correspond bijectively to those of $G$, so Theorem 3.3.2 also counts the spanning trees of undirected graphs.

## 3.4. Cycle Matrices and Cut-Set Matrices

### 3.4.1. Cycle Matrices

**Definition 3.4.1 (Cycle Matrix)** Assign an arbitrary orientation to each **cycle** of a connected directed graph $G$. The **cycle matrix** $C_e$ of $G$ has one row for each cycle of $G$ and one column for each edge, with entries

$$
c_{ij} = \begin{cases}
1, & e_j \in C_i \text{ and its direction agrees with the orientation of } C_i, \\
-1, & e_j \in C_i \text{ and its direction is opposite to the orientation of } C_i, \\
0, & e_j \notin C_i.
\end{cases}
$$

**Definition 3.4.2 (Fundamental Cycle)** Fix a spanning tree $T$ of a connected directed graph $G$. Each chord $e$, together with the unique path in $T$ joining its endpoints, forms a cycle, called the **fundamental cycle** of $e$; its orientation is taken to agree with $e$. The matrix formed by all $m-n+1$ fundamental cycles is called the **fundamental cycle matrix** $C_f$ of $G$. If the edges are ordered with the chords first and the branches last, and the fundamental cycles are ordered like their chords, then $C_f = (I \mid C_{f12})$.

**Theorem 3.4.1** If the incidence matrix $B$ and the cycle matrix $C_e$ of a connected directed graph $G$ use the same ordering of edges, then $B C_e^{\mathsf T} = 0$.

**Proof** The $(i, j)$ entry of $B C_e^{\mathsf T}$ is $\sum_k b_{ik} c_{jk}$, and only edges that are incident with $v_i$ and belong to the cycle $C_j$ contribute. If $C_j$ does not pass through $v_i$, the sum is $0$. If $C_j$ passes through $v_i$, exactly two of its edges are incident with $v_i$: following the orientation of the cycle, one enters $v_i$ and one leaves it. For the edge leaving $v_i$: if its direction agrees with the cycle, $v_i$ is its tail and $b c = 1 \cdot 1$; if its direction is opposite, $v_i$ is its head and $b c = (-1)(-1)$. Either way it contributes $1$. Similarly, the edge entering $v_i$ always contributes $-1$. The two contributions cancel. $\square$

**Corollary** A reduced incidence matrix $B_k$ and a fundamental cycle matrix $C_f$ (with the same ordering of edges) satisfy $B_k C_f^{\mathsf T} = 0$.

**Theorem 3.4.2** The cycle matrix of a connected directed graph $G$ has rank $m-n+1$.

**Proof** $C_e$ contains the rows of $C_f$, and the $m-n+1$ rows of $C_f = (I \mid C_{f12})$ are linearly independent, so $\operatorname{rank} C_e \ge m-n+1$. On the other hand, $B C_e^{\mathsf T} = 0$ and Sylvester's rank inequality give $\operatorname{rank} B + \operatorname{rank} C_e - m \le \operatorname{rank}(B C_e^{\mathsf T}) = 0$, which together with $\operatorname{rank} B = n-1$ yields $\operatorname{rank} C_e \le m-n+1$. $\square$

**Theorem 3.4.3** Let $C$ be the cycle matrix formed by any $m-n+1$ linearly independent cycles of a connected directed graph $G$. An $(m-n+1) \times (m-n+1)$ submatrix of $C$ has nonzero determinant if and only if the edges corresponding to its columns form the cotree of some spanning tree of $G$.

Proof sketch: use the standard form $(I \mid C_{f12})$ of the fundamental cycle matrix and elementary row operations, as in Theorem 3.2.6.

**Theorem 3.4.4** Let the reduced incidence matrix $B_k$ and the fundamental cycle matrix $C_f$ of a connected directed graph $G$ use the same ordering of edges (chords first, branches last), with $C_f = (I \mid C_{f12})$ and $B_k = (B_{11} \mid B_{12})$, where $B_{12}$ corresponds to the branches. Then

$$
C_{f12} = -B_{11}^{\mathsf T} \left(B_{12}^{-1}\right)^{\mathsf T}.
$$

**Proof** By Theorem 3.2.6, $B_{12}$ is an invertible square matrix. From $B_k C_f^{\mathsf T} = 0$ we get

$$
(B_{11} \mid B_{12}) \begin{bmatrix} I \\ C_{f12}^{\mathsf T} \end{bmatrix} = B_{11} + B_{12} C_{f12}^{\mathsf T} = 0,
$$

so $C_{f12}^{\mathsf T} = -B_{12}^{-1} B_{11}$, and transposing gives the claim. $\square$

### 3.4.2. Cut-Set Matrices

**Definition 3.4.4 (Cut Set)** Let $S$ be a set of edges of a directed graph $G = (V, E)$. If $G' = (V, E - S)$ has exactly one more connected component than $G$, while for every proper subset $S'$ of $S$ the graph $G'' = (V, E - S')$ has the same number of connected components as $G$, then $S$ is called a **cut set** of $G$. A cut set divides the vertices of some connected component into two parts, and its orientation may be specified as pointing from one part to the other.

**Definition 3.4.5 (Cut-Set Matrix)** The **cut-set matrix** $S_e$ of a connected directed graph $G$ has one row for each cut set of $G$ and one column for each edge: $s_{ij} = 1$ if $e_j \in S_i$ and its direction agrees with the orientation of the cut set, $s_{ij} = -1$ if $e_j \in S_i$ and its direction is opposite, and $s_{ij} = 0$ if $e_j \notin S_i$.

**Definition 3.4.6 (Fundamental Cut Set)** Let $T$ be a spanning tree of a connected graph $G$ and $e_i$ a branch of $T$. Deleting $e_i$ from $T$ splits $T$ into two connected components, and all edges of $G$ joining these two parts form a cut set $S_i$. This $S_i$ contains exactly one branch, $e_i$, all its other edges being chords, and its orientation is taken to agree with $e_i$. We call $S_i$ the **fundamental cut set** of $G$ with respect to $T$ corresponding to the branch $e_i$.

**Definition 3.4.7 (Fundamental Cut-Set Matrix)** Given a spanning tree $T$ of a connected directed graph $G$, the matrix formed by all $n-1$ fundamental cut sets with respect to $T$ is called the **fundamental cut-set matrix** $S_f$. If the edges are ordered with the chords first and the branches last, and the fundamental cut sets are ordered like their branches, then $S_f = (S_{f11} \mid I)$, where $I$ corresponds to the branches.

**Theorem 3.4.5** If the cycle matrix $C_e$ and the cut-set matrix $S_e$ of a connected directed graph $G$ use the same ordering of edges, then $S_e C_e^{\mathsf T} = 0$.

The reason is that whenever a cycle crosses from one side of a cut set to the other, it must cross back again: among the edges common to the cycle and the cut set, those agreeing with the orientation of the cut set and those opposite to it cancel exactly when counted along the orientation of the cycle.

**Theorem 3.4.6** The cut-set matrix of a connected directed graph $G$ has rank $n-1$.

**Theorem 3.4.7** Let $S$ be the cut-set matrix formed by any $n-1$ linearly independent cut sets of a connected directed graph $G$. An $(n-1) \times (n-1)$ submatrix of $S$ has nonzero determinant if and only if the edges corresponding to its columns form a spanning tree of $G$.

**Theorem 3.4.8** Let $S_f$ and $C_f$ be the fundamental cut-set matrix and the fundamental cycle matrix of a connected directed graph $G$ with respect to the same spanning tree $T$, with the same ordering of edges, $S_f = (S_{f11} \mid I)$ and $C_f = (I \mid C_{f12})$. Then $S_{f11} = -C_{f12}^{\mathsf T}$.

**Proof** By Theorem 3.4.5, $S_f C_f^{\mathsf T} = 0$, that is,

$$
(S_{f11} \mid I) \begin{bmatrix} I \\ C_{f12}^{\mathsf T} \end{bmatrix} = S_{f11} + C_{f12}^{\mathsf T} = 0,
$$

so $S_{f11} = -C_{f12}^{\mathsf T}$. $\square$

**Corollary 3.4.1** Let the reduced incidence matrix $B_k$ and the fundamental cut-set matrix $S_f$ of a connected directed graph $G$ use the same ordering of edges, with $B_k = (B_{11} \mid B_{12})$ and $S_f = (S_{f11} \mid I)$. Then $S_{f11} = B_{12}^{-1} B_{11}$.

**Proof** By Theorem 3.4.4, $C_{f12}^{\mathsf T} = -B_{12}^{-1} B_{11}$; by Theorem 3.4.8, $S_{f11} = -C_{f12}^{\mathsf T} = B_{12}^{-1} B_{11}$. $\square$

## 3.5. Generating Spanning Trees

In this section we discuss how to generate further spanning trees starting from a known one.

### 3.5.1. Distance Between Trees and Elementary Tree Transformations

**Definition 3.5.1 (Distance Between Trees and Elementary Tree Transformation)** Let $t_1, t_2$ be two spanning trees of a connected graph $G$. If exactly $k$ edges of $t_1$ do not belong to $t_2$, then $d(t_1, t_2) = k$ is called the **distance** between the two trees. If $t_1$ and $t_2$ are at distance $1$, with $t_1 - t_2 = \{e\}$ and $t_2 - t_1 = \{e'\}$, then $t_2 = t_1 \oplus \{e, e'\}$ is called an **elementary tree transformation** from $t_1$ to $t_2$.

Below, $S_e(t)$ denotes the fundamental cut set of $G$ with respect to the spanning tree $t$ corresponding to the branch $e$.

**Theorem 3.5.1** Let $t_1$ and $t_2$ be spanning trees of $G$ at distance $1$, with $t_1 - t_2 = \{e\}$ and $t_2 - t_1 = \{b\}$. Then $b \in S_e(t_1)$. Conversely, if $b \in S_e(t_1)$ and $b \ne e$, then $t_1 \oplus \{e, b\}$ is a spanning tree.

**Proof** Deleting $e$ from $t_1$ leaves two connected components, and $S_e(t_1)$ consists exactly of the edges of $G$ joining them. Since $t_2 = t_1 - e + b$ is connected, $b$ must join the two parts, that is, $b \in S_e(t_1)$. Conversely, if $b \in S_e(t_1)$ and $b \ne e$, then $t_1 - e + b$ is connected and has $n-1$ edges, so by Theorem 3.1.2 it is a spanning tree. $\square$

**Theorem 3.5.2** Given a spanning tree $t_0$ of $G$ and a branch $e$ of it, let $t_1, t_2, \dots, t_p$ be all the spanning trees of $G$ with $t_0 - t_i = \{e\}$ and $d(t_0, t_i) = 1$, and let $t_i - t_0 = \{b_i\}$. Then $S_e(t_0) = \{e, b_1, b_2, \dots, b_p\}$. Conversely, for every $b \in S_e(t_0)$ with $b \ne e$, the tree $t_0 \oplus \{e, b\}$ is one of these spanning trees.

**Theorem 3.5.3** Let $t_0 = \{e_1, e_2, \dots, e_{n-1}\}$ be a reference spanning tree of $G$, and let

$$
T^{e_i} = \{\, t_0 \oplus \{e_i, b\} \mid b \in S_{e_i}(t_0),\ b \ne e_i \,\}.
$$

Then the spanning trees of $G$ at distance $1$ from $t_0$ are exactly the members of $T^{e_1} \cup T^{e_2} \cup \cdots \cup T^{e_{n-1}}$, and these sets are pairwise disjoint.

## 3.6. Huffman Trees

### 3.6.1. Background and Definitions

When a string is stored in a computer, a fixed-length code may take up a lot of space. A variable-length code designed according to the frequencies of the characters can minimize the total storage length. Such an optimal code corresponds to a **Huffman tree**, an optimal binary tree.

**Definition 3.6.1 (Binary Tree)** An arborescence in which every vertex other than the leaves has out-degree at most $2$ is called a **binary tree**. If all these vertices have out-degree exactly $2$, it is called a **full binary tree**. Note that this is a full binary tree in the sense of the English literature, which differs from a "complete binary tree" in the sense of data structures texts (defined by level-order numbering).

**Definition 3.6.2 (Weighted Binary Tree)** Let $T$ be a full binary tree with root $v_0$. If each leaf $v_i$ is assigned a positive real number $w_i$, then $T$ is called a **weighted binary tree**. Writing $l_i$ for the length (number of edges) of the path from the root to the leaf $v_i$, we call

$$
\mathrm{WPL}(T) = \sum_i w_i l_i
$$

the weighted path length of $T$.

**Definition 3.6.3 (Optimal Binary Tree)** Given the weights of the leaves, many different weighted binary trees can be constructed; one with the smallest WPL is called an **optimal binary tree**, or **Huffman tree**.

### 3.6.2. Huffman's Algorithm

**Algorithm 3.6.1 (Huffman's Algorithm)**

1. Arrange the weights in nondecreasing order: $w_{i_1} \le w_{i_2} \le \dots \le w_{i_n}$.
2. Take the vertices of the two smallest weights $w_{i_1}, w_{i_2}$, and create a new vertex as their parent, with weight $w_{i_1} + w_{i_2}$. Remove $w_{i_1}, w_{i_2}$ from the sequence, insert the new weight, and set $n \leftarrow n-1$.
3. If $n = 1$, stop; otherwise go to step 1.

**Theorem 3.6.1** The binary tree produced by Huffman's algorithm is an optimal binary tree.

**Proof** Let the weights be $w_1 \le w_2 \le \dots \le w_n$. We use induction on $n$; the case $n = 2$ is obvious.

First, there is an optimal tree in which the leaves of weights $w_1, w_2$ are siblings at the deepest level: in any optimal tree, take a pair of sibling leaves at the deepest level and swap their weights with $w_1, w_2$; this does not increase the WPL.

Next, in such an optimal tree $T$, delete the two leaves of weights $w_1, w_2$; their parent becomes a leaf of weight $w_1 + w_2$, giving a tree $T'$ with weights $w_1 + w_2, w_3, \dots, w_n$ and $\mathrm{WPL}(T) = \mathrm{WPL}(T') + w_1 + w_2$. The first step of Huffman's algorithm merges $w_1, w_2$, and the remaining steps are exactly Huffman's algorithm applied to $w_1 + w_2, w_3, \dots, w_n$. By the induction hypothesis the resulting tree $H'$ is optimal, so $\mathrm{WPL}(H') \le \mathrm{WPL}(T')$. Hence the Huffman tree $H$ satisfies $\mathrm{WPL}(H) = \mathrm{WPL}(H') + w_1 + w_2 \le \mathrm{WPL}(T)$, and $H$ is an optimal binary tree. $\square$

## 3.7. Minimum Spanning Trees

### 3.7.1. Problem Statement

Given a **weighted graph** $G = (V, E)$ (assumed connected), a spanning tree of minimum total weight is called a *minimum spanning tree*. Typical applications include the design of water supply networks and communication networks.

### 3.7.2. Kruskal's Algorithm (Cycle Avoidance)

The idea of *Kruskal's algorithm* is to sort the edges by weight in increasing order and examine them in turn, adding an edge if it does not create a cycle and discarding it otherwise, until $n-1$ edges have been chosen.

**Algorithm 3.7.1 (Kruskal's Algorithm)**

1. Set $T \leftarrow \varnothing$ and sort the edges of $E$ by weight in nondecreasing order.
2. While $|T| < n-1$ and $E \ne \varnothing$: remove the currently shortest edge $e$ from $E$, setting $E \leftarrow E - \{e\}$; if $T \cup \{e\}$ contains no cycle, set $T \leftarrow T \cup \{e\}$.
3. If $|T| < n-1$, then $G$ is disconnected; otherwise $T$ is a minimum spanning tree.

**Theorem 3.7.1** A spanning tree $T = (V, E')$ of a connected weighted graph $G$ is a minimum spanning tree if and only if, for every chord $e \in E - E'$, the fundamental cycle $C^e \subseteq E' \cup \{e\}$ of $e$ satisfies $w(e) \ge w(a)$ for all $a \in C^e$ with $a \ne e$.

This theorem guarantees the correctness of Kruskal's algorithm: every edge $e$ discarded by the algorithm forms a cycle with previously chosen edges of weight at most $w(e)$, and the edges not yet examined when the algorithm stops have weights no smaller than those of all chosen edges, so the final tree satisfies the condition of Theorem 3.7.1.

### 3.7.3. Prim's Algorithm

The idea of *Prim's algorithm* is to grow the tree from a single vertex: at each step, among the edges joining the set $U$ of chosen vertices to the set $V - U$ of unchosen vertices, add a shortest one to the tree.

**Algorithm 3.7.2 (Prim's Algorithm)**

1. Set $U \leftarrow \{v_1\}$ and $T \leftarrow \varnothing$.
2. While $U \ne V$: choose $u \in U$ and $v \in V - U$ with $w(u, v)$ minimal; set $T \leftarrow T \cup \{(u, v)\}$ and $U \leftarrow U \cup \{v\}$; and update, for each $x \in V - U$, its shortest distance to $U$.

**Theorem 3.7.3** Let $U$ be a nonempty proper subset of the vertex set of a connected weighted graph $G$, and let $e$ be an edge of minimum weight among the edges with one endpoint in $U$ and the other in $V - U$. Then $G$ has a minimum spanning tree containing $e$. If such a minimum-weight edge is unique, then every minimum spanning tree of $G$ contains $e$.

**Proof** Let $T$ be a minimum spanning tree not containing $e$. Then $T + e$ contains a unique cycle. Having crossed from the $U$ side to the $V - U$ side along $e$, this cycle must return to $U$, so it contains another edge $e'$ with one endpoint in $U$ and the other in $V - U$, and $w(e) \le w(e')$. Replacing $e'$ by $e$ gives a spanning tree $T' = T + e - e'$ with $w(T') \le w(T)$, so $T'$ is also a minimum spanning tree, and it contains $e$. If the minimum-weight edge is unique, then $w(e) < w(e')$ and $w(T') < w(T)$, contradicting the minimality of $T$; hence every minimum spanning tree contains $e$. $\square$

**Theorem 3.7.4** Prim's algorithm produces a minimum spanning tree of a connected weighted graph $G$.

Proof sketch: by induction on the number of chosen edges, using Theorem 3.7.3 to show that at every step the chosen edge set is contained in some minimum spanning tree.

### 3.7.4. Cycle Breaking

For hand computation one can also start from the graph $G$ itself (assumed connected) and repeatedly find a cycle and delete an edge of maximum weight on it, until no cycle remains; the result is a minimum spanning tree.

### 3.7.5. Comparison of Algorithms

| Algorithm | Complexity | Best suited for |
|---|---|---|
| Kruskal's algorithm | $O(m \log m)$ (dominated by sorting) | Sparse graphs |
| Prim's algorithm | $O(n^2)$ | Dense graphs |
| Cycle breaking | — | Hand computation |

**Remark** To find a maximum spanning tree, simply sort the edges by weight in decreasing order; all other steps are the same.

## 3.8. Maximum Branchings

**Definition 3.8.1 (Branching)** A subgraph of a directed graph that contains no cycle and in which every vertex has **in-degree** at most $1$ is called a **branching**.

A branching is exactly a union of pairwise disjoint arborescences. The problem of finding a branching of maximum total weight in a weighted directed graph is called the maximum branching problem. It can be viewed as a generalization of the minimum spanning tree problem to directed graphs and is usually solved by Edmonds' algorithm (also known as the Chu–Liu/Edmonds algorithm).
