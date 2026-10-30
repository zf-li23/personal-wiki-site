---
title: Trees
source_hash: bbf489509565
---

Trees are among the most important notions in graph theory and have wide applications in computer science (file systems, coding, searching, games and more). In the mid-nineteenth century the British mathematician Cayley studied the enumeration of trees and used it to count the isomers of chemical compounds, one of the earliest applications of trees. In this chapter we first give the definition of a tree and several equivalent characterizations. We then return to the incidence matrix $B$, the adjacency matrix $A$ and the degree matrix $D$ of [1.4.1](/1.4.1) and study spanning trees algebraically: the rank and the minors of the incidence matrix characterize spanning trees, the Laplacian matrix $L = D - A = BB^{\mathsf T}$ counts them (the matrix-tree theorem and Cayley's formula), and the cycle and cut-set matrices determine and are determined by the incidence matrix. Next we discuss how to generate spanning trees, and finally two optimization problems involving trees: Huffman trees and minimum spanning trees. In [1.4.6](/1.4.6) the eigenvalues of the Laplacian matrix will also measure how well a graph is connected.

## 3.1. Definitions

### 3.1.1. Definition and Basic Properties of Trees

**Definition 3.1.1 (Tree)** A connected graph containing no cycle is called a **tree**, usually denoted $T$. The edges of a tree are called its **branches**, and a vertex of degree $1$ is called a **leaf**.

![Left: a tree with 7 vertices and 6 edges, the green vertices being its leaves; middle: a forest of two trees, which is disconnected and hence not a tree; right: a connected graph containing the cycle abcd (red), which is not a tree](./plots/tree-examples.py)

**Definition 3.1.2 (Cut Edge)** Let $e$ be an edge of a graph $G$. If $G - e$ has more **connected components** than $G$, then $e$ is called a **cut edge** of $G$.

**Theorem 3.1.1** An edge $e = (u, v)$ is a cut edge if and only if $e$ lies on no cycle of $G$.

**Proof** Necessity: if $e$ lies on a cycle, the rest of the cycle is a path from $u$ to $v$ in $G - e$, so $u$ and $v$ remain in the same connected component, deleting $e$ does not increase the number of components, and $e$ is not a cut edge.

Sufficiency: if $e$ is not a cut edge, then $G - e$ has as many connected components as $G$, so $u$ and $v$ are still in the same component of $G - e$. Hence $G - e$ contains a path $P(u, v)$, and $P(u, v)$ together with $e$ forms a cycle. $\square$

![The cut edges (red) are exactly the edges lying on no cycle: cd, eh and fg are cut edges, while the edges of the triangles abc and def lie on cycles and are not](./plots/cut-edges.py)

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

![Left: a graph G with 5 vertices and 7 edges and a spanning tree T (blue, branches e1, e2, e3, e5), the dashed edges being the chords e4, e6, e7; middle: the fundamental cycle {e4, e1, e2, e3} formed by the chord e4 and the path in T joining its ends; right: deleting the branch e2 splits T into {v1, v2, v5} and {v3, v4} (orange), and the edges joining the two parts form the fundamental cut set {e2, e4, e6} (Section 3.4)](./plots/spanning-tree-cotree.py)

## 3.2. The Reduced Incidence Matrix and Its Properties

To study trees algebraically, we first examine the linear dependence and the rank of the incidence matrix of a connected directed graph. Throughout this section, $B$ denotes the **incidence matrix** of a directed graph without loops (defined in [1.4.1](/1.4.1)): $b_{ij} = 1$ means that $v_i$ is the tail of $e_j$, and $b_{ij} = -1$ that $v_i$ is its head.

### 3.2.1. Definition of the Reduced Incidence Matrix

**Definition 3.2.1 (Reduced Incidence Matrix)** Deleting from the incidence matrix of a connected directed graph $G = (V, E)$ the row corresponding to any one vertex $v_k$ gives an $(n-1) \times m$ matrix $B_k$, called a **reduced incidence matrix** of $G$.

### 3.2.2. The Rank of the Incidence Matrix

**Theorem 3.2.1** The incidence matrix $B$ of a directed graph $G$ has rank $\operatorname{rank}(B) < n$.

**Proof** Each column of $B$ contains exactly one $1$ and one $-1$, so the sum of the $n$ row vectors is the zero vector. The rows are linearly dependent, and the rank is less than $n$. $\square$

**Theorem 3.2.2** Let $B_0$ be any $k \times k$ square submatrix of the incidence matrix $B$ of a directed graph $G$. Then $\det B_0$ is $0$, $1$ or $-1$.

**Proof** By induction on $k$; the case $k = 1$ is obvious. For general $k$: if $B_0$ has a zero column, then $\det B_0 = 0$. If every column of $B_0$ has two nonzero entries, then each column consists of exactly one $1$ and one $-1$, the rows sum to the zero vector, and $\det B_0 = 0$. Otherwise some column of $B_0$ has a single nonzero entry $\pm 1$; expanding along that column, $\det B_0$ equals $\pm$ the determinant of a $(k-1) \times (k-1)$ submatrix, and the induction hypothesis gives the claim. $\square$

A matrix with this property (every square submatrix has determinant $0$ or $\pm 1$) is called a *totally unimodular matrix*; this is why determinants can "count" spanning trees in Section 3.3.

**Theorem 3.2.3** If $B$ is the incidence matrix of a connected directed graph $G$, then $\operatorname{rank}(B) = n-1$.

**Proof** Let the row vector $\boldsymbol{x} = (x_1, \dots, x_n)$ satisfy $\boldsymbol{x}B = \boldsymbol{0}$. For each edge $e = (v_i, v_j)$, the component of $\boldsymbol{x}B$ corresponding to $e$ is $x_i - x_j$, so adjacent vertices have equal values of $x_i$; since $G$ is connected, $x_1 = x_2 = \cdots = x_n$. Thus the solution space of $\boldsymbol{x}B = \boldsymbol{0}$ is one-dimensional, and $\operatorname{rank}(B) = n - 1$. $\square$

The same argument shows that if $G$ has $c$ connected components, then $\boldsymbol{x}B = \boldsymbol{0}$ if and only if $\boldsymbol{x}$ is constant on each component, and $\operatorname{rank}(B) = n - c$.

**Theorem 3.2.4** The reduced incidence matrix $B_k$ of a connected directed graph $G$ has rank $\operatorname{rank}(B_k) = n-1$; that is, the $n-1$ rows of $B_k$ are linearly independent.

**Proof** If a nontrivial linear combination of the rows of $B_k$ were zero, then setting the coefficient $x_k = 0$ would give a solution $\boldsymbol{x}$ of $\boldsymbol{x}B = \boldsymbol{0}$ whose components are not all equal, contradicting the proof of Theorem 3.2.3. $\square$

### 3.2.3. Reduced Incidence Matrices and Circuits

**Theorem 3.2.5** Let $B_k$ be a reduced incidence matrix of a connected directed graph $G$, and let $C$ be a circuit in $G$. Then the columns of $B_k$ corresponding to the edges of $C$ are linearly dependent.

**Proof** The circuit $C$ contains a cycle, so it suffices to prove the claim for cycles. Let $C$ be a cycle with $l$ vertices and $l$ edges. In $B$, the columns of these $l$ edges have nonzero entries only in the rows of the $l$ vertices of $C$, and this part forms the incidence matrix $B(C)$ of $C$ itself, an $l \times l$ matrix. Since $C$ is a connected graph, Theorem 3.2.3 gives $\operatorname{rank}(B(C)) = l - 1 < l$, so these $l$ columns are linearly dependent. The corresponding columns of $B_k$ are obtained by deleting one component and remain linearly dependent. $\square$

**Corollary 3.2.2** Let $H$ be a subgraph of a connected directed graph $G$. If $H$ contains a cycle, then the columns of the reduced incidence matrix of $G$ corresponding to the edges of $H$ are linearly dependent.

### 3.2.4. Reduced Incidence Matrices and Spanning Trees

**Theorem 3.2.6** Let $B_k$ be a reduced incidence matrix of a connected directed graph $G$. An $(n-1) \times (n-1)$ submatrix of $B_k$ has nonzero determinant if and only if the edges corresponding to its columns form a spanning tree of $G$.

**Proof** Necessity: if an $(n-1) \times (n-1)$ submatrix has nonzero determinant, its $n-1$ columns are linearly independent, so by Corollary 3.2.2 these edges contain no cycle. They are $n-1$ edges on $n$ vertices without a cycle, so by Theorem 3.1.2 they form a tree, that is, a spanning tree of $G$.

Sufficiency: suppose these $n-1$ edges form a spanning tree $T$. The submatrix is then exactly the reduced incidence matrix of $T$ obtained by deleting the row of $v_k$. Since $T$ is a connected directed graph on $n$ vertices, Theorem 3.2.4 shows that this matrix has rank $n-1$, so its determinant is nonzero. $\square$

## 3.3. Counting Spanning Trees

The number of spanning trees of a connected graph $G$ can be computed as a **determinant**. The argument has three steps: the Binet–Cauchy theorem expands $\det(B_k B_k^{\mathsf T})$ as the sum of the squares of all $(n-1) \times (n-1)$ minors of $B_k$; by Section 3.2, each squared minor is $1$ if it corresponds to a spanning tree and $0$ otherwise; and finally $BB^{\mathsf T}$ turns out to be the Laplacian matrix, which depends only on the graph.

### 3.3.1. The Binet–Cauchy Theorem

**Theorem 3.3.1 (Binet–Cauchy Theorem)** Let $A = (a_{ij})_{m \times n}$ and $B = (b_{ij})_{n \times m}$ with $m \le n$. Then

$$
\det(AB) = \sum_S \det A_S \cdot \det B_S,
$$

where $S$ runs over all $\binom{n}{m}$ subsets of $\{1, \dots, n\}$ with $m$ elements, $A_S$ is the $m \times m$ submatrix of $A$ formed by the columns in $S$, and $B_S$ is the $m \times m$ submatrix of $B$ formed by the rows in $S$.

**Proof** Let $\boldsymbol{a}_k$ be the $k$-th column of $A$. Then the $j$-th column of $AB$ is $\sum_k b_{kj}\boldsymbol{a}_k$, and multilinearity of the determinant in the columns gives

$$
\det(AB) = \sum_{k_1, \dots, k_m} b_{k_1 1} b_{k_2 2} \cdots b_{k_m m} \det(\boldsymbol{a}_{k_1}, \dots, \boldsymbol{a}_{k_m}).
$$

Terms with a repeated index vanish. Group the terms whose index set $\{k_1, \dots, k_m\}$ equals a given $S = \{s_1 < \dots < s_m\}$: writing $k_j = s_{\sigma(j)}$, we have $\det(\boldsymbol{a}_{k_1}, \dots, \boldsymbol{a}_{k_m}) = \operatorname{sgn}(\sigma) \det A_S$, and $\sum_\sigma \operatorname{sgn}(\sigma) \prod_j b_{s_{\sigma(j)} j} = \det B_S$. $\square$

For $m > n$ we have $\operatorname{rank}(AB) \le n < m$ and $\det(AB) = 0$; for $m = n$ the theorem reduces to $\det(AB) = \det A \det B$.

### 3.3.2. The Laplacian Matrix

Recall the three matrices of a graph from [1.4.1](/1.4.1): the **adjacency matrix** $A$, the **incidence matrix** $B$ and the degree matrix $D$ formed by the vertex degrees. The following matrix ties them together.

**Definition 3.3.1 (Laplacian Matrix)** Let $G$ be an undirected graph without loops (multiple edges allowed) with vertices $v_1, \dots, v_n$. Let $D = \operatorname{diag}(d(v_1), \dots, d(v_n))$ be the degree matrix and $A$ the adjacency matrix, where $a_{ij}$ is the number of edges between $v_i$ and $v_j$. The $n \times n$ matrix

$$
L = D - A
$$
is called the **Laplacian matrix** of $G$; that is, $l_{ii} = d(v_i)$ and $l_{ij} = -a_{ij}$ for $i \ne j$. The Laplacian matrix of a directed graph is that of the undirected graph obtained by ignoring directions.

**Theorem 3.3.2** Let $G$ be an undirected graph without loops. Orient each edge arbitrarily and let $B$ be the incidence matrix of the resulting directed graph. Then

$$
BB^{\mathsf T} = L.
$$

In particular, $BB^{\mathsf T}$ does not depend on the orientation.

**Proof** $(BB^{\mathsf T})_{ii} = \sum_k b_{ik}^2$ is the number of edges incident with $v_i$, that is, $d(v_i)$. For $i \ne j$, only edges incident with both $v_i$ and $v_j$ contribute to $(BB^{\mathsf T})_{ij} = \sum_k b_{ik} b_{jk}$; such an edge has its tail at one end and its head at the other, so it contributes $1 \cdot (-1) = -1$, and the sum is $-a_{ij}$. $\square$

If one uses the incidence matrix of the undirected graph (entries $0, 1$) instead, the same computation gives $D + A$; it is precisely the signs in the directed incidence matrix that turn the off-diagonal entries into $-a_{ij}$.

**Theorem 3.3.3 (Basic Properties of the Laplacian Matrix)** Let $G$ be an undirected graph without loops, with $c$ connected components $G_1, \dots, G_c$ on the vertex sets $V_1, \dots, V_c$, and let $L$ be its Laplacian matrix.

1. For every $\boldsymbol{x} = (x_1, \dots, x_n)^{\mathsf T} \in \mathbb{R}^n$,
   $$
   \boldsymbol{x}^{\mathsf T} L \boldsymbol{x} = \sum_{(v_i, v_j) \in E} (x_i - x_j)^2,
   $$
   where each edge is counted once. Hence $L$ is a symmetric **positive semidefinite matrix**, and its eigenvalues are nonnegative real numbers, which we write as $0 = \lambda_1 \le \lambda_2 \le \cdots \le \lambda_n$.
2. $L\boldsymbol{1} = \boldsymbol{0}$, that is, every row of $L$ sums to $0$, and $0$ is an eigenvalue of $L$.
3. The multiplicity of the **eigenvalue** $0$ equals the number $c$ of connected components, $\operatorname{rank}(L) = n - c$, and the null space $\mathcal{N}(L)$ is spanned by the indicator vectors $\boldsymbol{1}_{V_1}, \dots, \boldsymbol{1}_{V_c}$ of the components. In particular, $G$ is connected if and only if $\lambda_2 > 0$.

**Proof** (1) By Theorem 3.3.2, $\boldsymbol{x}^{\mathsf T} L \boldsymbol{x} = \boldsymbol{x}^{\mathsf T} B B^{\mathsf T} \boldsymbol{x} = \|B^{\mathsf T}\boldsymbol{x}\|^2$, and the component of $B^{\mathsf T}\boldsymbol{x}$ corresponding to an edge $e = (v_i, v_j)$ is $x_i - x_j$. The eigenvalues of a real symmetric positive semidefinite matrix are nonnegative real numbers.

(2) The $i$-th row sums to $d(v_i) - \sum_j a_{ij} = 0$.

(3) $L$ is real symmetric and hence orthogonally diagonalizable, so the multiplicity of the eigenvalue $0$ is $\dim \mathcal{N}(L)$. If $L\boldsymbol{x} = \boldsymbol{0}$, then $\boldsymbol{x}^{\mathsf T}L\boldsymbol{x} = 0$, and by (1) $x_i = x_j$ at the two ends of every edge; thus $\boldsymbol{x}$ is constant on each component and is a linear combination of $\boldsymbol{1}_{V_1}, \dots, \boldsymbol{1}_{V_c}$. Conversely, such an $\boldsymbol{x}$ satisfies $B^{\mathsf T}\boldsymbol{x} = \boldsymbol{0}$, so $L\boldsymbol{x} = B(B^{\mathsf T}\boldsymbol{x}) = \boldsymbol{0}$. The $c$ indicator vectors have pairwise disjoint supports and are linearly independent, so $\dim \mathcal{N}(L) = c$. $\square$

Property (3) agrees with the remark after Theorem 3.2.3: $\operatorname{rank}(L) = \operatorname{rank}(BB^{\mathsf T}) = \operatorname{rank}(B) = n - c$. "The multiplicity of the zero eigenvalue equals the number of components" is our first example of reading graph structure off a spectrum. For a connected graph, the larger the second smallest eigenvalue $\lambda_2$, the "harder" the graph is to disconnect; in [1.4.6](/1.4.6) $\lambda_2$ is called the algebraic connectivity and compared with the vertex and edge connectivities.

**Example 3.3.1** Let $G$ be the graph obtained from $K_4$ by deleting the edge $v_2v_4$ (top left in the figure below), with edges $e_1 = v_1v_2$, $e_2 = v_2v_3$, $e_3 = v_3v_4$, $e_4 = v_4v_1$, $e_5 = v_1v_3$. Orienting them as $v_1 \to v_2$, $v_2 \to v_3$, $v_3 \to v_4$, $v_4 \to v_1$, $v_1 \to v_3$ gives

$$
B = \begin{bmatrix}
1 & 0 & 0 & -1 & 1 \\
-1 & 1 & 0 & 0 & 0 \\
0 & -1 & 1 & 0 & -1 \\
0 & 0 & -1 & 1 & 0
\end{bmatrix}, \qquad
BB^{\mathsf T} = \begin{bmatrix}
3 & -1 & -1 & -1 \\
-1 & 2 & -1 & 0 \\
-1 & -1 & 3 & -1 \\
-1 & 0 & -1 & 2
\end{bmatrix} = D - A = L.
$$

The eigenvalues of $L$ are $0, 2, 4, 4$; the eigenvalue $0$ is simple, in agreement with the connectedness of $G$.

### 3.3.3. The Matrix-Tree Theorem

**Theorem 3.3.4** Let $B_k$ be a reduced incidence matrix of a connected directed graph $G$. Then the number of distinct spanning trees of $G$ is $\det(B_k B_k^{\mathsf T})$.

**Proof** By the Binet–Cauchy theorem,

$$
\det(B_k B_k^{\mathsf T}) = \sum_S \det B_S \cdot \det B_S^{\mathsf T} = \sum_S (\det B_S)^2,
$$

where $B_S$ ranges over all $(n-1) \times (n-1)$ submatrices of $B_k$. By Theorem 3.2.6, $\det B_S \ne 0$ if and only if the corresponding edges form a spanning tree, and by Theorem 3.2.2, $\det B_S \in \{0, \pm 1\}$. Hence $(\det B_S)^2 = 1$ exactly when the edges form a spanning tree and $0$ otherwise, and the sum is the number of spanning trees. $\square$

Orienting each edge of a connected undirected graph $G$ arbitrarily gives a connected directed graph $G'$. As edge sets, the spanning trees of $G'$ correspond bijectively to those of $G$ (spanning trees ignore directions), so Theorem 3.3.4 also counts the spanning trees of undirected graphs. Combined with Theorem 3.3.2, the result can be stated in terms of $L$ alone, independently of the orientation:

**Theorem 3.3.5 (Matrix-Tree Theorem)** Let $G$ be an undirected graph without loops on $n \ge 2$ vertices, let $L$ be its Laplacian matrix with eigenvalues $0 = \lambda_1 \le \lambda_2 \le \cdots \le \lambda_n$, and let $L^{(k)}$ be the $(n-1) \times (n-1)$ matrix obtained from $L$ by deleting the $k$-th row and the $k$-th column. Then the number of spanning trees of $G$ is

$$
\tau(G) = \det L^{(k)} = \frac{1}{n}\lambda_2 \lambda_3 \cdots \lambda_n
$$

for every $k$.

**Proof** If $G$ is disconnected, then $\tau(G) = 0$; by Theorem 3.3.3, $\operatorname{rank}(L) = n - c \le n - 2$, so all $(n-1) \times (n-1)$ minors of $L$ vanish and $\lambda_2 = 0$, and the identity holds.

Let $G$ be connected. Choose an orientation, with incidence matrix $B$. Deleting the $k$-th row of $B$ amounts to deleting the $k$-th row and column of $BB^{\mathsf T}$, so by Theorem 3.3.2, $B_k B_k^{\mathsf T} = L^{(k)}$, and Theorem 3.3.4 gives $\tau(G) = \det L^{(k)}$.

The eigenvalue form: compare the coefficients of $\lambda$ in the characteristic polynomial $\det(\lambda I - L) = \lambda(\lambda - \lambda_2)\cdots(\lambda - \lambda_n)$. On the right it is $(-1)^{n-1}\lambda_2\cdots\lambda_n$; on the left it is $(-1)^{n-1}\sum_{k=1}^n \det L^{(k)}$ (the sum of the principal minors of order $n-1$), which equals $(-1)^{n-1} n\,\tau(G)$. $\square$

**Remark** The proof combines three facts: the factorization $L = BB^{\mathsf T}$ (Theorem 3.3.2) turns the counting problem into a problem about $B$; the Binet–Cauchy theorem expands $\det(B_kB_k^{\mathsf T})$ into one term for each set of $n-1$ edges; and total unimodularity (Theorem 3.2.2) together with Theorem 3.2.6 makes each term equal to $1$ exactly when those $n-1$ edges form a spanning tree. Moreover, for connected $G$ we have $\operatorname{rank}(L) = n - 1$ and $L\boldsymbol{1} = \boldsymbol{0}$, from which one deduces that the adjugate of $L$ equals $\tau(G)\,\boldsymbol{1}\boldsymbol{1}^{\mathsf T}$: every cofactor of $L$ (not only the diagonal ones) equals $\tau(G)$. This is Kirchhoff's matrix-tree theorem, which originated in the analysis of electrical networks.

**Remark** Spanning trees that contain, or avoid, a given edge $e$ can also be counted: the spanning trees avoiding $e$ are exactly the spanning trees of $G - e$, and the spanning trees containing $e$ correspond bijectively to the spanning trees of the graph obtained by contracting $e$ (merging its two endpoints). Hence $\tau(G) = \tau(G - e) + \tau(G / e)$, where $G / e$ denotes the graph obtained by contracting $e$.

**Example 3.3.2** Continuing Example 3.3.1, deleting the first row and column of $L$ gives

$$
\tau(G) = \det \begin{bmatrix} 2 & -1 & 0 \\ -1 & 3 & -1 \\ 0 & -1 & 2 \end{bmatrix} = 2 \cdot 5 - (-1)(-2) = 8;
$$

from the eigenvalues, $\tau(G) = \frac{1}{4} \cdot 2 \cdot 4 \cdot 4 = 8$. Directly: there are $\binom{5}{3} = 10$ ways to choose $3$ of the $5$ edges, and removing the two triangles $\{e_1, e_2, e_5\}$ and $\{e_3, e_4, e_5\}$ leaves exactly $8$ spanning trees.

![Top left: the graph G obtained from K4 by deleting the edge v2v4; the other eight panels: all 8 spanning trees of G (blue), in agreement with det L^(1) = 8 from the matrix-tree theorem](./plots/kite-spanning-trees.py)

The following program counts spanning trees by the matrix-tree theorem (with exact Gaussian elimination over the rationals), compares the result with an enumeration of all sets of $n-1$ edges, and checks Cayley's formula of Section 3.3.4 for complete graphs.

```python
from fractions import Fraction
from itertools import combinations

def laplacian(n, edges):
    L = [[0] * n for _ in range(n)]
    for u, v in edges:            # L = D - A, multiple edges counted
        L[u][u] += 1; L[v][v] += 1
        L[u][v] -= 1; L[v][u] -= 1
    return L

def det(M):
    # exact Gaussian elimination over the rationals
    M = [[Fraction(x) for x in row] for row in M]
    n, d = len(M), Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return 0
        if p != c:
            M[c], M[p], d = M[p], M[c], -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return int(d)

def count_trees(n, edges, k=0):
    # matrix-tree theorem: delete row and column k of L
    L = laplacian(n, edges)
    return det([[L[i][j] for j in range(n) if j != k] for i in range(n) if i != k])

def is_tree(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False      # this edge closes a cycle
        parent[ru] = rv
    return True

# K4 minus the edge v2v4 (vertices v1..v4 -> 0..3)
kite = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
brute = sum(is_tree(4, T) for T in combinations(kite, 3))
print("K4 - e:", count_trees(4, kite), "brute force:", brute)
for n in range(2, 8):
    Kn = list(combinations(range(n), 2))
    print(f"K{n}:", count_trees(n, Kn), "n^(n-2) =", n ** (n - 2))
```

```text
K4 - e: 8 brute force: 8
K2: 1 n^(n-2) = 1
K3: 3 n^(n-2) = 3
K4: 16 n^(n-2) = 16
K5: 125 n^(n-2) = 125
K6: 1296 n^(n-2) = 1296
K7: 16807 n^(n-2) = 16807
```

### 3.3.4. Cayley's Formula

A tree whose vertices carry the labels $1, 2, \dots, n$ is called a *labeled tree*; two labeled trees are the same if they have the same edge set (isomorphic trees with different edge sets count as different). The labeled trees on $n$ vertices are exactly the spanning trees of the complete graph $K_n$.

**Theorem 3.3.6 (Cayley's Formula)** There are $n^{n-2}$ labeled trees on the vertex set $\{1, 2, \dots, n\}$; that is, $\tau(K_n) = n^{n-2}$.

**Proof** (by the matrix-tree theorem) The Laplacian matrix of $K_n$ is $L = nI - J$, where $J$ is the all-ones matrix. The eigenvalues of $J = \boldsymbol{1}\boldsymbol{1}^{\mathsf T}$ are $n$ (eigenvector $\boldsymbol{1}$) and $0$ (with multiplicity $n-1$), so the eigenvalues of $L$ are $0$ and $n$ (with multiplicity $n-1$). By Theorem 3.3.5, $\tau(K_n) = \frac{1}{n} n^{n-1} = n^{n-2}$. $\square$

![All 16 labeled trees on the vertex set {1, 2, 3, 4}: 4 stars (orange, centered at 1, 2, 3, 4) and 12 paths (blue, 4!/2 = 12), in agreement with Cayley's formula 4^2 = 16; without labels there are only two kinds, the star and the path](./plots/cayley-four.py)

Cayley's formula also has a bijective proof, which encodes each labeled tree as a sequence of length $n-2$.

**Definition 3.3.2 (Prüfer Sequence)** Let $T$ be a tree on the vertex set $\{1, \dots, n\}$, $n \ge 3$. Repeat $n-2$ times: delete the leaf with the smallest label and record its neighbor. The recorded sequence $(p_1, \dots, p_{n-2})$ is called the **Prüfer sequence** of $T$.

**Example 3.3.3** Let $T$ have the edges $15, 25, 53, 36, 64, 37$ ($n = 7$). We delete the leaves $1, 2, 4, 5, 6$ in turn and record $5, 5, 6, 3, 3$; the vertices $3$ and $7$ remain, and the Prüfer sequence is $(5, 5, 6, 3, 3)$. Vertex $3$ has degree $3$ and occurs twice in the sequence; the leaves $1, 2, 4, 7$ do not occur.

![The encoding in Example 3.3.3: at each step the leaf with the smallest label (red) is deleted and its neighbor (blue) is recorded; after five steps two vertices remain, and the Prüfer sequence is (5, 5, 6, 3, 3)](./plots/prufer-steps.py)

**Theorem 3.3.7** The map "labeled tree $\mapsto$ Prüfer sequence" is a bijection from the set of labeled trees on $\{1, \dots, n\}$ to $\{1, \dots, n\}^{n-2}$, and a vertex $v$ occurs exactly $d(v) - 1$ times in the Prüfer sequence of $T$.

**Proof** Occurrences: each time $v$ is recorded, one of its neighbors is deleted. If $v$ is one of the last two vertices, all of its neighbors except the other end of the last edge have been deleted, that is, $d(v) - 1$ of them; if $v$ is deleted as a leaf at some step, it has a single neighbor left at that moment, so $d(v) - 1$ neighbors were deleted before. In both cases $v$ is recorded exactly $d(v) - 1$ times.

Consequently the leaves of $T$ are exactly the vertices that do not occur in the sequence, and the first deleted leaf $b_1$ is the smallest label not occurring in $(p_1, \dots, p_{n-2})$; $T$ contains the edge $b_1p_1$, and $T - b_1$ is a tree on $\{1, \dots, n\} \setminus \{b_1\}$ with Prüfer sequence $(p_2, \dots, p_{n-2})$. By induction on $n$ (the case $n = 3$ is checked directly), $T - b_1$ is uniquely determined by $(p_2, \dots, p_{n-2})$, hence $T$ is uniquely determined by its sequence, and the map is injective.

Conversely, given any sequence $(p_1, \dots, p_{n-2})$, decode it: at step $i$ take the smallest label $b_i$ that is not yet used and does not occur among $p_i, \dots, p_{n-2}$, add the edge $b_ip_i$ and mark $b_i$ as used; finally join the two remaining unused vertices. The same induction shows that the result is a tree whose Prüfer sequence is the given one, so the map is surjective. $\square$

By Theorem 3.3.7, the number of labeled trees equals the number $n^{n-2}$ of sequences of length $n-2$ with entries in $\{1, \dots, n\}$, which is a second proof of Cayley's formula. Decoding Example 3.3.3 joins $1$ to $5$, $2$ to $5$, $4$ to $6$, $5$ to $3$, $6$ to $3$, and finally $3$ to $7$. The bijection also gives a finer count:

**Corollary 3.3.1** Let the positive integers $d_1, \dots, d_n$ satisfy $\sum_i d_i = 2n - 2$. Then the number of labeled trees in which vertex $i$ has degree $d_i$ ($i = 1, \dots, n$) is

$$
\frac{(n-2)!}{(d_1 - 1)!\,(d_2 - 1)! \cdots (d_n - 1)!}.
$$

**Proof** By Theorem 3.3.7, these trees correspond bijectively to the sequences of length $n-2$ in which $i$ occurs exactly $d_i - 1$ times, and their number is the multinomial coefficient above. $\square$

For example, $n = 4$ and the degree sequence $(3, 1, 1, 1)$ give $2!/2! = 1$, the star centered at $1$.

```python
def prufer_encode(n, edges):
    adj = {v: set() for v in range(1, n + 1)}
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    seq = []
    for _ in range(n - 2):
        leaf = min(v for v in adj if len(adj[v]) == 1)   # smallest leaf
        (nb,) = adj.pop(leaf)
        adj[nb].discard(leaf)
        seq.append(nb)                                   # record its neighbour
    return seq

def prufer_decode(seq):
    n = len(seq) + 2
    left = {v: seq.count(v) for v in range(1, n + 1)}   # remaining occurrences
    used, edges = set(), []
    for i, x in enumerate(seq):
        leaf = min(v for v in left if v not in used and left[v] == 0)
        edges.append((leaf, x))
        used.add(leaf); left[x] -= 1
    u, v = [w for w in left if w not in used]           # the last two vertices
    return edges + [(u, v)]

tree = [(1, 5), (2, 5), (5, 3), (3, 6), (6, 4), (3, 7)]
code = prufer_encode(7, tree)
print("Pruefer sequence:", code)
print("decoded edges:   ", prufer_decode(code))
```

```text
Pruefer sequence: [5, 5, 6, 3, 3]
decoded edges:    [(1, 5), (2, 5), (4, 6), (5, 3), (6, 3), (3, 7)]
```

### 3.3.5. Counting Arborescences

**Definition 3.3.3 (Arborescence)** Let $T$ be a directed tree (a directed graph that is a tree when directions are ignored). If some vertex $v_0$ of $T$ has in-degree $0$ and every other vertex has in-degree $1$, then $T$ is called an **arborescence** (or out-tree) rooted at $v_0$, also called a **rooted tree**.

**Theorem 3.3.8** The number of arborescences rooted at $v_k$ in a connected directed graph $G$ is $\det(\bar{B}_k B_k^{\mathsf T})$, where $\bar{B}_k$ is the matrix obtained from $B_k$ by replacing every entry $1$ with $0$.

**Proof** By the Binet–Cauchy theorem, $\det(\bar{B}_k B_k^{\mathsf T}) = \sum_S \det \bar{B}_S \cdot \det B_S$, where $B_S$ ranges over the $(n-1) \times (n-1)$ submatrices of $B_k$ and $\bar{B}_S$ is the corresponding submatrix of $\bar{B}_k$. If the corresponding edges do not form a spanning tree, then $\det B_S = 0$. If they form a spanning tree that is not an arborescence rooted at $v_k$, then the heads of the $n-1$ edges cannot be exactly the $n-1$ vertices other than $v_k$, so some vertex $v \ne v_k$ is the head of no edge; the row of $v$ in $\bar{B}_S$ is then zero, and $\det \bar{B}_S = 0$. If they form an arborescence rooted at $v_k$, then ordering rows and columns simultaneously by matching each edge with its head, and ordering vertices by their distance from the root, turns $B_S$ into a triangular matrix with all diagonal entries $-1$ and $\bar{B}_S$ into a diagonal matrix with all diagonal entries $-1$. The two determinants are equal and equal to $\pm 1$, so their product is $1$. Summing gives the number of arborescences. $\square$

**Remark** The same computation as in Theorem 3.3.2 gives $\bar{B}B^{\mathsf T} = D^- - A^{\mathsf T}$, where $D^-$ is the diagonal matrix of in-degrees and $A$ is the adjacency matrix of the directed graph ($a_{ij}$ being the number of arcs from $v_i$ to $v_j$): $(\bar{B}B^{\mathsf T})_{ii}$ counts the arcs entering $v_i$, and $(\bar{B}B^{\mathsf T})_{ij} = -a_{ji}$ for $i \ne j$. The matrix $\bar{B}_k B_k^{\mathsf T}$ is this "directed Laplacian" with the $k$-th row and column deleted, so Theorem 3.3.8 is the directed form of the matrix-tree theorem (due to Tutte).

**Example 3.3.4** Let the directed graph $G$ have the arcs $v_1 \to v_2$, $v_1 \to v_3$, $v_2 \to v_3$, $v_3 \to v_2$. The in-degrees are $d^-(v_1) = 0$ and $d^-(v_2) = d^-(v_3) = 2$, and

$$
D^- - A^{\mathsf T} = \begin{bmatrix} 0 & 0 & 0 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{bmatrix}.
$$

Deleting the first row and column gives $\det \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} = 3$: there are exactly $3$ arborescences rooted at $v_1$.

![Example 3.3.4: the directed graph G (left) and all 3 of its arborescences rooted at v1 (blue): every non-root vertex has exactly one entering arc](./plots/arborescences.py)

## 3.4. Cycle Matrices and Cut-Set Matrices

### 3.4.1. Cycle Matrices

**Definition 3.4.1 (Cycle Matrix)** Assign an arbitrary orientation to each cycle (directions of edges ignored) of a connected directed graph $G$. The **cycle matrix** $C_e$ of $G$ has one row for each cycle of $G$ and one column for each edge, with entries

$$
c_{ij} = \begin{cases}
1, & e_j \in C_i \text{ and its direction agrees with the orientation of } C_i, \\
-1, & e_j \in C_i \text{ and its direction is opposite to the orientation of } C_i, \\
0, & e_j \notin C_i.
\end{cases}
$$

**Definition 3.4.2 (Fundamental Cycle)** Fix a spanning tree $T$ of a connected directed graph $G$. Each chord $e$, together with the unique path in $T$ joining its endpoints, forms a cycle, called the **fundamental cycle** of $e$; its orientation is taken to agree with $e$. The matrix formed by all $m-n+1$ fundamental cycles is called the **fundamental cycle matrix** $C_f$ of $G$. If the edges are ordered with the chords first and the branches last, and the fundamental cycles are ordered like their chords, then $C_f = (I \mid C_{f12})$.

**Theorem 3.4.1** If the incidence matrix $B$ and the cycle matrix $C_e$ of a connected directed graph $G$ use the same ordering of edges, then $B C_e^{\mathsf T} = O$.

**Proof** The $(i, j)$ entry of $B C_e^{\mathsf T}$ is $\sum_k b_{ik} c_{jk}$, and only edges that are incident with $v_i$ and belong to the cycle $C_j$ contribute. If $C_j$ does not pass through $v_i$, the sum is $0$. If $C_j$ passes through $v_i$, exactly two of its edges are incident with $v_i$: following the orientation of the cycle, one enters $v_i$ and one leaves it. For the edge leaving $v_i$: if its direction agrees with the cycle, $v_i$ is its tail and $b c = 1 \cdot 1$; if its direction is opposite, $v_i$ is its head and $b c = (-1)(-1)$. Either way it contributes $1$. Similarly, the edge entering $v_i$ always contributes $-1$. The two contributions cancel. $\square$

**Corollary** A reduced incidence matrix $B_k$ and a fundamental cycle matrix $C_f$ (with the same ordering of edges) satisfy $B_k C_f^{\mathsf T} = O$.

**Theorem 3.4.2** The cycle matrix of a connected directed graph $G$ has rank $m-n+1$.

**Proof** $C_e$ contains the rows of $C_f$, and the $m-n+1$ rows of $C_f = (I \mid C_{f12})$ are linearly independent, so $\operatorname{rank}(C_e) \ge m-n+1$. On the other hand, $B C_e^{\mathsf T} = O$ and Sylvester's rank inequality give $\operatorname{rank}(B) + \operatorname{rank}(C_e) - m \le \operatorname{rank}(B C_e^{\mathsf T}) = 0$, which together with $\operatorname{rank}(B) = n-1$ yields $\operatorname{rank}(C_e) \le m-n+1$. $\square$

**Theorem 3.4.3** Let $C$ be the cycle matrix formed by any $m-n+1$ linearly independent cycles of a connected directed graph $G$. An $(m-n+1) \times (m-n+1)$ submatrix of $C$ has nonzero determinant if and only if the edges corresponding to its columns form the cotree of some spanning tree of $G$.

Proof sketch: use the standard form $(I \mid C_{f12})$ of the fundamental cycle matrix and elementary row operations, as in Theorem 3.2.6.

**Theorem 3.4.4** Let the reduced incidence matrix $B_k$ and the fundamental cycle matrix $C_f$ of a connected directed graph $G$ use the same ordering of edges (chords first, branches last), with $C_f = (I \mid C_{f12})$ and $B_k = (B_{11} \mid B_{12})$, where $B_{12}$ corresponds to the branches. Then

$$
C_{f12} = -B_{11}^{\mathsf T} \left(B_{12}^{-1}\right)^{\mathsf T}.
$$

**Proof** By Theorem 3.2.6, $B_{12}$ is an invertible square matrix. From $B_k C_f^{\mathsf T} = O$ we get

$$
(B_{11} \mid B_{12}) \begin{bmatrix} I \\ C_{f12}^{\mathsf T} \end{bmatrix} = B_{11} + B_{12} C_{f12}^{\mathsf T} = O,
$$

so $C_{f12}^{\mathsf T} = -B_{12}^{-1} B_{11}$, and transposing gives the claim. $\square$

### 3.4.2. Cut-Set Matrices

**Definition 3.4.4 (Cut Set)** Let $S$ be a set of edges of a directed graph $G = (V, E)$. If $G' = (V, E \setminus S)$ has exactly one more connected component than $G$, while for every proper subset $S'$ of $S$ the graph $G'' = (V, E \setminus S')$ has the same number of connected components as $G$, then $S$ is called a **cut set** of $G$. A cut set divides the vertices of some connected component into two parts, and its orientation may be specified as pointing from one part to the other.

**Definition 3.4.5 (Cut-Set Matrix)** The **cut-set matrix** $S_e$ of a connected directed graph $G$ has one row for each cut set of $G$ and one column for each edge: $s_{ij} = 1$ if $e_j \in S_i$ and its direction agrees with the orientation of the cut set, $s_{ij} = -1$ if $e_j \in S_i$ and its direction is opposite, and $s_{ij} = 0$ if $e_j \notin S_i$.

**Definition 3.4.6 (Fundamental Cut Set)** Let $T$ be a spanning tree of a connected graph $G$ and $e_i$ a branch of $T$. Deleting $e_i$ from $T$ splits $T$ into two connected components, and all edges of $G$ joining these two parts form a cut set $S_i$. This $S_i$ contains exactly one branch, $e_i$, all its other edges being chords, and its orientation is taken to agree with $e_i$. We call $S_i$ the **fundamental cut set** of $G$ with respect to $T$ corresponding to the branch $e_i$.

**Definition 3.4.7 (Fundamental Cut-Set Matrix)** Given a spanning tree $T$ of a connected directed graph $G$, the matrix formed by all $n-1$ fundamental cut sets with respect to $T$ is called the **fundamental cut-set matrix** $S_f$. If the edges are ordered with the chords first and the branches last, and the fundamental cut sets are ordered like their branches, then $S_f = (S_{f11} \mid I)$, where $I$ corresponds to the branches.

**Theorem 3.4.5** If the cycle matrix $C_e$ and the cut-set matrix $S_e$ of a connected directed graph $G$ use the same ordering of edges, then $S_e C_e^{\mathsf T} = O$.

The reason is that whenever a cycle crosses from one side of a cut set to the other, it must cross back again: among the edges common to the cycle and the cut set, those agreeing with the orientation of the cut set and those opposite to it cancel exactly when counted along the orientation of the cycle.

**Theorem 3.4.6** The cut-set matrix of a connected directed graph $G$ has rank $n-1$.

**Theorem 3.4.7** Let $S$ be the cut-set matrix formed by any $n-1$ linearly independent cut sets of a connected directed graph $G$. An $(n-1) \times (n-1)$ submatrix of $S$ has nonzero determinant if and only if the edges corresponding to its columns form a spanning tree of $G$.

**Theorem 3.4.8** Let $S_f$ and $C_f$ be the fundamental cut-set matrix and the fundamental cycle matrix of a connected directed graph $G$ with respect to the same spanning tree $T$, with the same ordering of edges, $S_f = (S_{f11} \mid I)$ and $C_f = (I \mid C_{f12})$. Then $S_{f11} = -C_{f12}^{\mathsf T}$.

**Proof** By Theorem 3.4.5, $S_f C_f^{\mathsf T} = O$, that is,

$$
(S_{f11} \mid I) \begin{bmatrix} I \\ C_{f12}^{\mathsf T} \end{bmatrix} = S_{f11} + C_{f12}^{\mathsf T} = O,
$$

so $S_{f11} = -C_{f12}^{\mathsf T}$. $\square$

**Corollary 3.4.1** Let the reduced incidence matrix $B_k$ and the fundamental cut-set matrix $S_f$ of a connected directed graph $G$ use the same ordering of edges, with $B_k = (B_{11} \mid B_{12})$ and $S_f = (S_{f11} \mid I)$. Then $S_{f11} = B_{12}^{-1} B_{11}$.

**Proof** By Theorem 3.4.4, $C_{f12}^{\mathsf T} = -B_{12}^{-1} B_{11}$; by Theorem 3.4.8, $S_{f11} = -C_{f12}^{\mathsf T} = B_{12}^{-1} B_{11}$. $\square$

**Example 3.4.1** Take the graph $G$ of the figure in Section 3.1.3 (vertices $v_1, \dots, v_5$, edges $e_1 = v_1v_2$, $e_2 = v_2v_3$, $e_3 = v_3v_4$, $e_4 = v_4v_1$, $e_5 = v_1v_5$, $e_6 = v_5v_3$, $e_7 = v_2v_5$) and the spanning tree $T = \{e_1, e_2, e_3, e_5\}$. Ignoring directions, the three fundamental cycles and the four fundamental cut sets are

| Chord | Fundamental cycle | | Branch | Fundamental cut set |
| :-- | :-- | :-- | :-- | :-- |
| $e_4$ | $\{e_4, e_1, e_2, e_3\}$ | | $e_1$ | $\{e_1, e_4, e_6, e_7\}$ |
| $e_6$ | $\{e_6, e_1, e_2, e_5\}$ | | $e_2$ | $\{e_2, e_4, e_6\}$ |
| $e_7$ | $\{e_7, e_1, e_5\}$ | | $e_3$ | $\{e_3, e_4\}$ |
| | | | $e_5$ | $\{e_5, e_6, e_7\}$ |

This shows the combinatorial content of Theorem 3.4.8: a chord $e$ belongs to the fundamental cut set of a branch $b$ if and only if $b$ belongs to the fundamental cycle of $e$ (for instance, the fundamental cycle of $e_4$ contains $e_1, e_2, e_3$, and $e_4$ occurs exactly in $S_{e_1}, S_{e_2}, S_{e_3}$). Moreover, every cycle and every cut set share an even number of edges (for instance, $\{e_4, e_1, e_2, e_3\} \cap \{e_2, e_4, e_6\} = \{e_2, e_4\}$), which is $S_e C_e^{\mathsf T} = O$ with the signs ignored.

## 3.5. Generating Spanning Trees

In this section we discuss how to generate further spanning trees starting from a known one.

### 3.5.1. Distance Between Trees and Elementary Tree Transformations

**Definition 3.5.1 (Distance Between Trees and Elementary Tree Transformation)** Let $t_1, t_2$ be two spanning trees of a connected graph $G$. If exactly $k$ edges of $t_1$ do not belong to $t_2$, then $d(t_1, t_2) = k$ is called the **distance** between the two trees. If $t_1$ and $t_2$ are at distance $1$, with $t_1 \setminus t_2 = \{e\}$ and $t_2 \setminus t_1 = \{e'\}$, then $t_2 = t_1 \oplus \{e, e'\}$ is called an **elementary tree transformation** from $t_1$ to $t_2$.

Below, $S_e(t)$ denotes the fundamental cut set of $G$ with respect to the spanning tree $t$ corresponding to the branch $e$.

**Theorem 3.5.1** Let $t_1$ and $t_2$ be spanning trees of $G$ at distance $1$, with $t_1 \setminus t_2 = \{e\}$ and $t_2 \setminus t_1 = \{b\}$. Then $b \in S_e(t_1)$. Conversely, if $b \in S_e(t_1)$ and $b \ne e$, then $t_1 \oplus \{e, b\}$ is a spanning tree.

**Proof** Deleting $e$ from $t_1$ leaves two connected components, and $S_e(t_1)$ consists exactly of the edges of $G$ joining them. Since $t_2 = t_1 - e + b$ is connected, $b$ must join the two parts, that is, $b \in S_e(t_1)$. Conversely, if $b \in S_e(t_1)$ and $b \ne e$, then $t_1 - e + b$ is connected and has $n-1$ edges, so by Theorem 3.1.2 it is a spanning tree. $\square$

**Theorem 3.5.2** Given a spanning tree $t_0$ of $G$ and a branch $e$ of it, let $t_1, t_2, \dots, t_p$ be all the spanning trees of $G$ with $t_0 \setminus t_i = \{e\}$ and $d(t_0, t_i) = 1$, and let $t_i \setminus t_0 = \{b_i\}$. Then $S_e(t_0) = \{e, b_1, b_2, \dots, b_p\}$. Conversely, for every $b \in S_e(t_0)$ with $b \ne e$, the tree $t_0 \oplus \{e, b\}$ is one of these spanning trees.

**Theorem 3.5.3** Let $t_0 = \{e_1, e_2, \dots, e_{n-1}\}$ be a reference spanning tree of $G$, and let

$$
T^{e_i} = \{\, t_0 \oplus \{e_i, b\} \mid b \in S_{e_i}(t_0),\ b \ne e_i \,\}.
$$

Then the spanning trees of $G$ at distance $1$ from $t_0$ are exactly the members of $T^{e_1} \cup T^{e_2} \cup \cdots \cup T^{e_{n-1}}$, and these sets are pairwise disjoint.

For instance, in Example 3.4.1 the four fundamental cut sets of the reference tree $T$ contain $3, 2, 1, 2$ chords, so there are $3 + 2 + 1 + 2 = 8$ spanning trees at distance $1$ from $T$.

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

Applying the identity $\mathrm{WPL}(T) = \mathrm{WPL}(T') + w_1 + w_2$ from the proof repeatedly shows that the WPL equals the sum of the weights of all internal (non-leaf) vertices.

**Example 3.6.1** Five characters have frequencies $2, 3, 5, 7, 11$. Huffman's algorithm merges $2 + 3 = 5$, $5 + 5 = 10$, $7 + 10 = 17$ and $11 + 17 = 28$ in turn, giving the tree in the figure below, with $\mathrm{WPL} = 5 + 10 + 17 + 28 = 60$. Labeling the left and right edges below each internal vertex with $0$ and $1$, the $0$–$1$ string read from the root to a leaf is the code of that character. Since no codeword is a prefix of another, this is a prefix code and can be decoded unambiguously. A fixed-length code would need $3$ bits per character, for a total length of $3 \times 28 = 84$.

![The Huffman tree of Example 3.6.1: green vertices are the leaves (the character frequencies), white internal vertices carry the merged weights, and the 0s and 1s on the edges give the prefix code 11→1, 7→01, 5→001, 2→0000, 3→0001, with WPL = 60](./plots/huffman.py)

## 3.7. Minimum Spanning Trees

### 3.7.1. Problem Statement

Given a **weighted graph** $G = (V, E)$ (assumed connected), a spanning tree of minimum total weight is called a *minimum spanning tree*. Typical applications include the design of water supply networks and communication networks.

**Example 3.7.1** We illustrate all the algorithms below on one weighted graph: vertices $a, b, c, d, e, f$ and edges with weights $ab: 4$, $af: 2$, $bf: 5$, $bc: 6$, $cf: 1$, $ce: 3$, $ef: 8$, $cd: 7$, $de: 9$ (see the first panel of the two figures below).

### 3.7.2. Kruskal's Algorithm (Cycle Avoidance)

The idea of *Kruskal's algorithm* is to sort the edges by weight in increasing order and examine them in turn, adding an edge if it does not create a cycle and discarding it otherwise, until $n-1$ edges have been chosen.

**Algorithm 3.7.1 (Kruskal's Algorithm)**

1. Set $T \leftarrow \varnothing$ and sort the edges of $E$ by weight in nondecreasing order.
2. While $\lvert T\rvert < n-1$ and $E \ne \varnothing$: remove the currently shortest edge $e$ from $E$, setting $E \leftarrow E \setminus \{e\}$; if $T \cup \{e\}$ contains no cycle, set $T \leftarrow T \cup \{e\}$.
3. If $\lvert T\rvert < n-1$, then $G$ is disconnected; otherwise $T$ is a minimum spanning tree.

**Theorem 3.7.1** A spanning tree $T = (V, E')$ of a connected weighted graph $G$ is a minimum spanning tree if and only if, for every chord $e \in E \setminus E'$, the fundamental cycle $C^e \subseteq E' \cup \{e\}$ of $e$ satisfies $w(e) \ge w(a)$ for all $a \in C^e$ with $a \ne e$.

This theorem guarantees the correctness of Kruskal's algorithm: every edge $e$ discarded by the algorithm forms a cycle with previously chosen edges of weight at most $w(e)$, and the edges not yet examined when the algorithm stops have weights no smaller than those of all chosen edges, so the final tree satisfies the condition of Theorem 3.7.1.

In Example 3.7.1, Kruskal's algorithm adds $cf(1)$, $af(2)$, $ce(3)$ and $ab(4)$; $bf(5)$ closes a cycle with $ab, af$, and $bc(6)$ closes a cycle with $ab, af, cf$, so both are discarded; after $cd(7)$ is added there are $5$ edges and the algorithm stops. The minimum spanning tree has weight $1 + 2 + 3 + 4 + 7 = 17$; the edges $ef(8)$ and $de(9)$ need not be examined.

![Kruskal's algorithm on Example 3.7.1: the first seven edges are examined in increasing order of weight; blue edges are the chosen branches, and red dashed edges are discarded because they close a cycle; once the fifth edge is chosen (last panel), the result is a minimum spanning tree of weight 17](./plots/kruskal-steps.py)

### 3.7.3. Prim's Algorithm

The idea of *Prim's algorithm* is to grow the tree from a single vertex: at each step, among the edges joining the set $U$ of chosen vertices to the set $V \setminus U$ of unchosen vertices, add a shortest one to the tree.

**Algorithm 3.7.2 (Prim's Algorithm)**

1. Set $U \leftarrow \{v_1\}$ and $T \leftarrow \varnothing$.
2. While $U \ne V$: choose $u \in U$ and $v \in V \setminus U$ with $w(u, v)$ minimal; set $T \leftarrow T \cup \{(u, v)\}$ and $U \leftarrow U \cup \{v\}$; and update, for each $x \in V \setminus U$, its shortest distance to $U$.

**Theorem 3.7.3** Let $U$ be a nonempty proper subset of the vertex set of a connected weighted graph $G$, and let $e$ be an edge of minimum weight among the edges with one endpoint in $U$ and the other in $V \setminus U$. Then $G$ has a minimum spanning tree containing $e$. If such a minimum-weight edge is unique, then every minimum spanning tree of $G$ contains $e$.

**Proof** Let $T$ be a minimum spanning tree not containing $e$. Then $T + e$ contains a unique cycle. Having crossed from the $U$ side to the $V \setminus U$ side along $e$, this cycle must return to $U$, so it contains another edge $e'$ with one endpoint in $U$ and the other in $V \setminus U$, and $w(e) \le w(e')$. Replacing $e'$ by $e$ gives a spanning tree $T' = T + e - e'$ with $w(T') \le w(T)$, so $T'$ is also a minimum spanning tree, and it contains $e$. If the minimum-weight edge is unique, then $w(e) < w(e')$ and $w(T') < w(T)$, contradicting the minimality of $T$; hence every minimum spanning tree contains $e$. $\square$

**Theorem 3.7.4** Prim's algorithm produces a minimum spanning tree of a connected weighted graph $G$.

Proof sketch: by induction on the number of chosen edges, using Theorem 3.7.3 to show that at every step the chosen edge set is contained in some minimum spanning tree.

In Example 3.7.1, starting from $a$, Prim's algorithm adds $af(2)$, $fc(1)$, $ce(3)$, $ab(4)$ and $cd(7)$, giving the same tree as Kruskal's algorithm (when all edge weights are distinct the minimum spanning tree is unique; see the questions).

![Prim's algorithm on Example 3.7.1, starting from a: orange vertices form the chosen set U, dashed edges are the current edges joining U to the other vertices, the red one is the shortest of them and is added in this step, and blue edges are the chosen branches](./plots/prim-steps.py)

The following program runs both algorithms on Example 3.7.1. Kruskal's algorithm uses a union–find structure to test whether the two ends are already connected (that is, whether the edge would close a cycle); for brevity, Prim's algorithm scans all edges at each step, in $O(nm)$ time, which an array of the distances of the vertices to $U$ improves to $O(n^2)$.

```python
edges = [("a", "b", 4), ("a", "f", 2), ("b", "f", 5), ("b", "c", 6), ("c", "f", 1),
         ("c", "e", 3), ("e", "f", 8), ("c", "d", 7), ("d", "e", 9)]
V = sorted({x for e in edges for x in e[:2]})

def kruskal(V, edges):
    root = {v: v for v in V}                 # union-find forest
    def find(x):
        while root[x] != x:
            x = root[x]
        return x
    T = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        ru, rv = find(u), find(v)
        print(f"  {u}{v} ({w}):", "add" if ru != rv else "reject (cycle)")
        if ru != rv:
            root[ru] = rv
            T.append((u, v, w))
        if len(T) == len(V) - 1:
            return T

def prim(V, edges, start):
    U, T = {start}, []
    while len(U) < len(V):
        # lightest edge with exactly one endpoint in U
        u, v, w = min((e for e in edges if (e[0] in U) != (e[1] in U)), key=lambda e: e[2])
        T.append((u, v, w))
        U |= {u, v}
    return T

print("Kruskal:")
K = kruskal(V, edges)
print("  tree:", [u + v for u, v, _ in K], "weight", sum(w for *_, w in K))
P = prim(V, edges, "a")
print("Prim from a:", [u + v for u, v, _ in P], "weight", sum(w for *_, w in P))
```

```text
Kruskal:
  cf (1): add
  af (2): add
  ce (3): add
  ab (4): add
  bf (5): reject (cycle)
  bc (6): reject (cycle)
  cd (7): add
  tree: ['cf', 'af', 'ce', 'ab', 'cd'] weight 17
Prim from a: ['af', 'cf', 'ce', 'ab', 'cd'] weight 17
```

### 3.7.4. Cycle Breaking

For hand computation one can also start from the graph $G$ itself (assumed connected) and repeatedly find a cycle and delete an edge of maximum weight on it, until no cycle remains; the result is a minimum spanning tree. In Example 3.7.1 we delete $de(9)$ on the cycle $cde$, $ef(8)$ on the cycle $cef$, $bc(6)$ on the cycle $bcf$ and $bf(5)$ on the cycle $abf$; the remaining $5$ edges form the minimum spanning tree found above.

### 3.7.5. Comparison of Algorithms

| Algorithm | Complexity | Best suited for |
|---|---|---|
| Kruskal's algorithm | $O(m \log m)$ (dominated by sorting) | Sparse graphs |
| Prim's algorithm | $O(n^2)$ | Dense graphs |
| Cycle breaking | — | Hand computation |

**Remark** To find a maximum spanning tree, simply sort the edges by weight in decreasing order; all other steps are the same.

## 3.8. Maximum Branchings

**Definition 3.8.1 (Branching)** A subgraph of a directed graph that contains no cycle (directions ignored) and in which every vertex has **in-degree** at most $1$ is called a **branching**.

A branching is exactly a union of pairwise disjoint arborescences. The problem of finding a branching of maximum total weight in a weighted directed graph is called the maximum branching problem. It can be viewed as a generalization of the minimum spanning tree problem to directed graphs and is usually solved by Edmonds' algorithm (also known as the Chu–Liu/Edmonds algorithm).

## Summary

- A tree is a connected graph without cycles (Definition 3.1.1). Theorem 3.1.2 gives six equivalent characterizations: connected and acyclic; connected with every edge a cut edge; connected with $n-1$ edges; $n-1$ edges and acyclic; a unique path between any two vertices; acyclic, but adding any edge creates exactly one cycle. A nontrivial tree has at least two leaves (Theorem 3.1.3). Every connected graph has a spanning tree, with $n-1$ branches and $m-n+1$ chords (Definition 3.1.3).
- Algebraic characterization: the incidence matrix and the reduced incidence matrix $B_k$ of a connected directed graph both have rank $n-1$ (Theorems 3.2.3 and 3.2.4), and every square submatrix has determinant $0$ or $\pm 1$ (Theorem 3.2.2); an $(n-1) \times (n-1)$ submatrix of $B_k$ is nonsingular if and only if the corresponding edges form a spanning tree (Theorem 3.2.6).
- The Laplacian matrix $L = D - A = BB^{\mathsf T}$ (Definition 3.3.1, Theorem 3.3.2) is symmetric positive semidefinite with $L\boldsymbol{1} = \boldsymbol{0}$, and the multiplicity of its zero eigenvalue equals the number of connected components (Theorem 3.3.3); its second smallest eigenvalue $\lambda_2$ is the algebraic connectivity of 1.4.6.
- Counting spanning trees: by the Binet–Cauchy theorem (Theorem 3.3.1), the number of spanning trees is $\det(B_k B_k^{\mathsf T})$ (Theorem 3.3.4), which is the matrix-tree theorem (Theorem 3.3.5)

  $$
  \tau(G) = \det L^{(k)} = \frac{1}{n}\lambda_2 \cdots \lambda_n;
  $$

  in particular $\tau(K_n) = n^{n-2}$ (Cayley's formula, Theorem 3.3.6), which also follows from the Prüfer bijection (Theorem 3.3.7) and refines to a count by degree sequence (Corollary 3.3.1). The number of arborescences rooted at $v_k$ is $\det(\bar{B}_k B_k^{\mathsf T})$ (Theorem 3.3.8).
- The three matrices compared ($G$ a connected directed graph, edges in the same order):

  | Matrix | Rows | Rank | Nonsingular maximal square submatrices correspond to | Orthogonality |
  | :-- | :-- | :-- | :-- | :-- |
  | Reduced incidence matrix $B_k$ | The $n-1$ vertices left after deleting one | $n-1$ (Theorem 3.2.4) | Spanning trees (Theorem 3.2.6) | $B_k C_f^{\mathsf T} = O$ |
  | Cycle matrices $C_e$, $C_f$ | Cycles (the fundamental cycle matrix $C_f$ has the $m-n+1$ fundamental cycles) | $m-n+1$ (Theorem 3.4.2) | Cotrees (Theorem 3.4.3) | $B C_e^{\mathsf T} = O$ (Theorem 3.4.1) |
  | Cut-set matrices $S_e$, $S_f$ | Cut sets (the fundamental cut-set matrix $S_f$ has the $n-1$ fundamental cut sets) | $n-1$ (Theorem 3.4.6) | Spanning trees (Theorem 3.4.7) | $S_e C_e^{\mathsf T} = O$ (Theorem 3.4.5) |

  Once a spanning tree is fixed, both $C_f$ and $S_f$ can be computed from $B_k$ (Theorems 3.4.4 and 3.4.8, Corollary 3.4.1; Example 3.4.1).
- Generating spanning trees: two spanning trees at distance $1$ differ by one elementary tree transformation, and the edge brought in must lie in the fundamental cut set of the branch taken out (Theorems 3.5.1 and 3.5.2); this lists all neighbors of a reference tree without repetition (Theorem 3.5.3).
- Two optimization problems:

  | Problem | Method | Correctness | Complexity |
  | :-- | :-- | :-- | :-- |
  | Optimal binary tree (minimum WPL) | Huffman's algorithm (Algorithm 3.6.1): repeatedly merge the two lightest vertices | Theorem 3.6.1 | $O(n \log n)$ (with a heap) |
  | Minimum spanning tree | Kruskal's algorithm (Algorithm 3.7.1): add edges in increasing order of weight, never closing a cycle | Theorem 3.7.1 | $O(m \log m)$, suited to sparse graphs |
  | Minimum spanning tree | Prim's algorithm (Algorithm 3.7.2): grow from one vertex, each time adding the lightest edge leaving the chosen part | Theorems 3.7.3 and 3.7.4 | $O(n^2)$, suited to dense graphs |
  | Minimum spanning tree | Cycle-breaking method: repeatedly delete the heaviest edge on a cycle | — | Hand computation |
  | Maximum branching (digraphs) | Edmonds' algorithm (Chu–Liu/Edmonds) | — | — |

## Questions

1. Find the number of spanning trees of the cycle $C_n$ on $n$ vertices, and verify the case $n = 4$ by the matrix-tree theorem.

   **Answer** Deleting any one edge of $C_n$ leaves a path, which is a spanning tree; conversely, a spanning tree has $n-1$ edges and so misses exactly one edge. Hence $\tau(C_n) = n$. For $n = 4$, deleting the first row and column of $L$ gives $\begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix}$, whose determinant is $2 \cdot 3 - 1 \cdot 2 = 4$.
2. Prove that $\tau(K_n - e) = (n-2)\,n^{n-3}$ for any edge $e$ of $K_n$, and compare with Example 3.3.2.

   **Answer** By symmetry, every edge of $K_n$ lies in the same number of spanning trees. The $n^{n-2}$ spanning trees of $K_n$ have $n-1$ edges each, and $K_n$ has $\binom{n}{2}$ edges, so each edge lies in $n^{n-2}(n-1)/\binom{n}{2} = 2n^{n-3}$ spanning trees. The spanning trees avoiding $e$ are exactly those of $K_n - e$, so there are $n^{n-2} - 2n^{n-3} = (n-2)n^{n-3}$ of them. For $n = 4$ this is $2 \cdot 4 = 8$, in agreement with Example 3.3.2.
3. A labeled tree on $\{1, \dots, n\}$ is chosen uniformly at random. What is the probability that vertex $1$ is a leaf, and what is its limit as $n \to \infty$?

   **Answer** By Theorem 3.3.7, vertex $1$ is a leaf if and only if it does not occur in the Prüfer sequence; there are $(n-1)^{n-2}$ such sequences, so the probability is $\left(1 - \frac{1}{n}\right)^{n-2} \to \mathrm{e}^{-1} \approx 0.368$.
4. Prove that if the edge weights of a connected weighted graph $G$ are pairwise distinct, then $G$ has a unique minimum spanning tree.

   **Answer** Suppose $T \ne T'$ are both minimum spanning trees, and let $e$ be the lightest edge of the symmetric difference $T \mathbin{\triangle} T'$; say $e \in T$. Then $T' + e$ contains a unique cycle, which must contain an edge $f$ not in $T$ (otherwise $T$ would contain a cycle); thus $f \in T' \setminus T$ and $w(f) > w(e)$. Then $T' + e - f$ is a spanning tree of smaller weight, contradicting the minimality of $T'$.
5. Why does Huffman's algorithm always produce a prefix code? Find the WPL of the Huffman tree for the weights $1, 1, 2, 4$.

   **Answer** Codewords correspond to paths from the root to leaves; if one codeword were a prefix of another, one leaf would lie on the path from the root to another leaf, which is impossible since leaves have no descendants. For the weights $1, 1, 2, 4$ we merge $1 + 1 = 2$, $2 + 2 = 4$ and $4 + 4 = 8$, so $\mathrm{WPL} = 2 + 4 + 8 = 14$ (the leaf depths are $3, 3, 2, 1$: $3 + 3 + 4 + 4 = 14$).
