---
title: Invariant Subspaces and the Jordan Canonical Form
source_hash: 8a88e0afdcd3
---

[Chapter 6](/2.1.6) posed the classification problem for **matrix similarity**: find the simplest representative of $\{P^{-1}AP \mid P \text{ invertible}\}$. A **diagonalizable matrix** can be brought to diagonal form, but a defective one cannot, and Chapter 6 only stated the answer (Theorem 6.10.1): every complex square matrix is similar to a **Jordan canonical form**, which is unique up to the order of the blocks. This chapter gives a complete proof of that theorem and organizes the computation of the Jordan form and of a Jordan basis into a standard procedure.

The same problem can be phrased in two ways. Let $V$ be an $n$-dimensional complex space, and let the **linear transformation** $T\colon V \to V$ have matrix $A$ with respect to the basis $v_1, \dots, v_n$, that is, $(Tv_1, \dots, Tv_n) = (v_1, \dots, v_n)A$.

| Language of linear transformations | Language of matrices |
|---|---|
| Find a new basis $w_1, \dots, w_n$ in which the matrix of $T$ is as simple as possible | Find an invertible $P$ with $(w_1, \dots, w_n) = (v_1, \dots, v_n)P$ |
| The matrix of $T$ in the new basis is $J$ | $J = P^{-1}AP$ |
| Induction on $\dim V$: decompose $V$ into a direct sum of invariant subspaces | Induction on the order: reduce to a block diagonal matrix |

The proof proceeds in three steps: Schur's theorem makes $A$ similar to an upper triangular matrix; the decomposition into generalized eigenspaces turns this into a block diagonal matrix in which each block has a single eigenvalue; finally, the decomposition of a nilpotent transformation into cyclic subspaces turns each block into Jordan blocks. Every step uses only operations that can be carried out mechanically: finding the roots of the characteristic polynomial (the theory of polynomials of [Chapter 9](/2.1.9)), computing ranks by elimination, and solving linear systems. In particular, the Jordan form itself is determined by a sequence of ranks $\operatorname{rank}\left((A - \mu I)^k\right)$, without computing $P$ first. The Jordan form of this chapter is the basis for computing matrix functions $f(A) = Pf(J)P^{-1}$ in the [next chapter](/2.1.11).

## 10.1. Direct Sums of Subspaces

[Chapter 8](/2.1.8) treated sums and direct sums of two subspaces; the proof of the Jordan form requires decomposing a space into several subspaces.

**Definition 10.1.1 (Direct Sum)** Let $V_1, \dots, V_k$ be subspaces of a complex space $V$. The set

$$
V_1 + \cdots + V_k = \{v_1 + \cdots + v_k \mid v_i \in V_i\}
$$

is called their sum; it is again a subspace. If every vector of the sum can be written as $v_1 + \cdots + v_k$ ($v_i \in V_i$) in only one way, the sum is called a direct sum and is denoted $V_1 \oplus \cdots \oplus V_k$.

**Theorem 10.1.1** The following conditions for $V_1 + \cdots + V_k$ to be a direct sum are equivalent:

1. $\dim V_1 + \cdots + \dim V_k = \dim(V_1 + \cdots + V_k)$;
2. the disjoint union of bases of $V_1, \dots, V_k$ is a basis of $V_1 + \cdots + V_k$;
3. the zero vector has a unique representation: if $0 = v_1 + \cdots + v_k$ with $v_i \in V_i$, then $v_1 = \cdots = v_k = 0$;
4. for every $i$, $V_i \cap \sum_{j \ne i} V_j = \{0\}$.

**Proof** Direct sum $\Leftrightarrow$ 3: subtracting two representations gives a representation of the zero vector. 3 $\Leftrightarrow$ 2: the union of bases of the $V_i$ always spans the sum, and condition 3 says exactly that it is linearly independent. 2 $\Leftrightarrow$ 1: the union of the bases has $\sum \dim V_i$ elements, and it is a basis of the sum if and only if this number equals the dimension of the sum. 3 $\Leftrightarrow$ 4: if $0 \ne v \in V_i \cap \sum_{j\ne i} V_j$, write $v = \sum_{j \ne i} v_j$; then $0 = -v + \sum_{j\ne i} v_j$ is a nontrivial representation of the zero vector, and conversely. $\square$

For $k = 2$ condition 4 reads $V_1 \cap V_2 = \{0\}$. For $k \ge 3$, however, pairwise trivial intersections are not enough: three distinct lines in $\mathbb{C}^2$ meet pairwise only in zero, yet their sum is not direct.

**Example 10.1.1** In $\mathbb{C}^3$, let $V_1$ be the $xOy$ plane and $V_2$ the $yOz$ plane. Then $V_1 + V_2 = \mathbb{C}^3$, but $\dim V_1 + \dim V_2 = 4 > 3$, so the sum is not direct; indeed, $(0, 1, 0)$ lies in both.

**Example 10.1.2** Let $A = \begin{bmatrix} 1 & 3 & 2 \\ 1 & 7 & 2 \\ -2 & -14 & -4 \end{bmatrix}$. A basis of $\mathcal{N}(A^{\mathsf T})$ is $\boldsymbol{\alpha}_1 = (0, 2, 1)^{\mathsf T}$, and a basis of the **column space** $\mathcal{R}(A)$ is $\boldsymbol{\alpha}_2 = (1, 1, -2)^{\mathsf T}$, $\boldsymbol{\alpha}_3 = (3, 7, -14)^{\mathsf T}$. The three vectors are linearly independent, so condition 2 gives $\mathbb{C}^3 = \mathcal{N}(A^{\mathsf T}) \oplus \mathcal{R}(A)$. For real matrices this always holds ($\mathcal{N}(A^{\mathsf T})$ is the **orthogonal complement** of $\mathcal{R}(A)$, [Chapter 4](/2.1.4)); for complex matrices the complement of $\mathcal{R}(A)$ is $\mathcal{N}(A^{\mathsf H})$, and $\mathcal{N}(A^{\mathsf T}) \cap \mathcal{R}(A)$ may be nonzero (for $A = \begin{bmatrix} 1 & \mathrm{i} \\ \mathrm{i} & -1 \end{bmatrix}$ both equal $\operatorname{span}\{(1, \mathrm{i})^{\mathsf T}\}$). The reason is the complex inner product of [Chapter 12](/2.1.12).

## 10.2. Invariant Subspaces

First let us see what it means for $A$ to be similar to a block diagonal matrix. If $A \in \mathbb{C}^{3\times 3}$ and $P^{-1}AP = \begin{bmatrix} b_{11} & 0 & 0 \\ 0 & b_{22} & b_{23} \\ 0 & b_{32} & b_{33} \end{bmatrix}$ with $P = (\boldsymbol{p}_1, \boldsymbol{p}_2, \boldsymbol{p}_3)$, comparing the columns of $AP = PB$ gives

$$
A\boldsymbol{p}_1 = b_{11}\boldsymbol{p}_1, \qquad A\boldsymbol{p}_2 = b_{22}\boldsymbol{p}_2 + b_{32}\boldsymbol{p}_3, \qquad A\boldsymbol{p}_3 = b_{23}\boldsymbol{p}_2 + b_{33}\boldsymbol{p}_3.
$$

Hence both $V_1 = \operatorname{span}\{\boldsymbol{p}_1\}$ and $V_2 = \operatorname{span}\{\boldsymbol{p}_2, \boldsymbol{p}_3\}$ are mapped into themselves by $A$, and $\mathbb{C}^3 = V_1 \oplus V_2$. Simplifying a matrix means finding such subspaces.

**Definition 10.2.1 (Invariant Subspace)** Let $T\colon V \to V$ be a linear transformation and $W \subseteq V$ a subspace. If $T(w) \in W$ for every $w \in W$, then $W$ is called a $T$-invariant subspace of $V$. In this case the restriction $T|_W\colon W \to W$ of $T$ to $W$ is a linear transformation of $W$.

The notion of an **invariant subspace** already appeared in representation theory ([1.3.6](/1.3.6)), where a subspace is required to be invariant under a whole family of transformations at once; here we consider a single transformation.

**Example 10.2.1** Let $T\colon \mathbb{C}^2 \to \mathbb{C}^2$, $(x, y)^{\mathsf T} \mapsto (y, x)^{\mathsf T}$. The $x$-axis is not $T$-invariant: $(1, 0)^{\mathsf T} \mapsto (0, 1)^{\mathsf T}$. On the other hand, for any $A \in \mathbb{C}^{n\times n}$ and $T(\boldsymbol{x}) = A\boldsymbol{x}$, both $\mathcal{R}(A)$ and $\mathcal{N}(A)$ are $T$-invariant: $\boldsymbol{y} = A\boldsymbol{x} \Rightarrow A\boldsymbol{y} = A(A\boldsymbol{x}) \in \mathcal{R}(A)$, and $A\boldsymbol{x} = \boldsymbol{0} \Rightarrow A(A\boldsymbol{x}) = \boldsymbol{0}$.

**Property 10.2.1** Let $T\colon V \to V$ be a linear transformation.

1. $\{0\}$, $V$, the **kernel** $\mathcal{N}(T)$ and the **image** $\mathcal{R}(T)$ are $T$-invariant subspaces; more generally, for every $a \in \mathbb{C}$ and positive integer $k$, $\mathcal{N}\big((T - a\,\mathrm{id})^k\big)$ and $\mathcal{R}\big((T - a\,\mathrm{id})^k\big)$ are $T$-invariant ($T$ commutes with $T - a\,\mathrm{id}$).
2. The **eigenspace** $V_{\lambda_0} = \mathcal{N}(T - \lambda_0 \mathrm{id})$ of an eigenvalue $\lambda_0$ is $T$-invariant.
3. The one-dimensional invariant subspaces are exactly the subspaces spanned by an **eigenvector**: if $W = \operatorname{span}\{w_0\}$ is invariant, then $T(w_0) = \lambda_0 w_0$.
4. Every nonzero $T$-invariant subspace $W$ of a complex space $V$ contains an eigenvector of $T$.

**Proof** We prove only 4. Choose a basis $\alpha_1, \dots, \alpha_r$ of $W$. By invariance, $(T\alpha_1, \dots, T\alpha_r) = (\alpha_1, \dots, \alpha_r)B$, where $B$ is the matrix of $T|_W$. By the **fundamental theorem of algebra**, $B$ has an eigenvalue $\lambda_0$ with an eigenvector $\boldsymbol{x} = (x_1, \dots, x_r)^{\mathsf T} \ne \boldsymbol{0}$. Let $v = x_1\alpha_1 + \cdots + x_r\alpha_r \in W$; then $v \ne 0$ and

$$
T(v) = (T\alpha_1, \dots, T\alpha_r)\boldsymbol{x} = (\alpha_1, \dots, \alpha_r)B\boldsymbol{x} = \lambda_0 (\alpha_1, \dots, \alpha_r)\boldsymbol{x} = \lambda_0 v. \qquad \square
$$

Property 4 depends on the complex field: the rotation $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ of a real space has no one-dimensional invariant subspace.

**Theorem 10.2.1** Let $V$ be an $n$-dimensional complex space, $T\colon V \to V$ a linear transformation and $V_1$ a $T$-invariant subspace.

1. There is a subspace $V_2$ with $V = V_1 \oplus V_2$ (extend a basis of $V_1$ to a basis of $V$).
2. Let $v_1, \dots, v_r$ be a basis of $V_1$ and $w_1, \dots, w_{n-r}$ a basis of $V_2$. Then the matrix of $T$ with respect to the basis $v_1, \dots, v_r, w_1, \dots, w_{n-r}$ has the form $\begin{bmatrix} B_{11} & B_{12} \\ O & B_{22} \end{bmatrix}$, where $B_{11}$ is the $r \times r$ matrix of $T|_{V_1}$.
3. If $V_2$ is also $T$-invariant, then $B_{12} = O$ and the matrix is a **block diagonal matrix**.

Consequently, $A$ is similar to a block upper triangular matrix $\Leftrightarrow$ it has a nontrivial invariant subspace; $A$ is similar to a block diagonal matrix $\Leftrightarrow$ the space decomposes as a direct sum of two invariant subspaces.

**Example 10.2.2** Let $A = \begin{bmatrix} 4 & -5 & 2 \\ 5 & -7 & 3 \\ 6 & -9 & 4 \end{bmatrix}$ and $T(\boldsymbol{x}) = A\boldsymbol{x}$. The subspace $\mathcal{N}(A)$ is $T$-invariant with basis $(1, 2, 3)^{\mathsf T}$. Extend it to the basis $(1, 2, 3)^{\mathsf T}, \boldsymbol{e}_2, \boldsymbol{e}_3$ of $\mathbb{C}^3$ and compute the coordinates of the images of the basis vectors in this basis:

$$
A\begin{bmatrix}1\\2\\3\end{bmatrix} = \boldsymbol{0}, \quad A\boldsymbol{e}_2 = \begin{bmatrix}-5\\-7\\-9\end{bmatrix} = -5\begin{bmatrix}1\\2\\3\end{bmatrix} + 3\boldsymbol{e}_2 + 6\boldsymbol{e}_3, \quad A\boldsymbol{e}_3 = \begin{bmatrix}2\\3\\4\end{bmatrix} = 2\begin{bmatrix}1\\2\\3\end{bmatrix} - \boldsymbol{e}_2 - 2\boldsymbol{e}_3,
$$

so $P = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 3 & 0 & 1 \end{bmatrix}$ gives $P^{-1}AP = \begin{bmatrix} 0 & -5 & 2 \\ 0 & 3 & -1 \\ 0 & 6 & -2 \end{bmatrix}$, whose upper left $1 \times 1$ block corresponds to $\mathcal{N}(A)$.

## 10.3. Schur's Theorem

Applying Theorem 10.2.1 repeatedly, each time splitting off a one-dimensional invariant subspace (an eigenvector), brings a matrix to upper triangular form.

**Theorem 10.3.1 (Schur Triangularization Theorem)** Let $A \in \mathbb{C}^{n\times n}$ with $\det(\lambda I_n - A) = (\lambda - \mu_1)^{n_1} \cdots (\lambda - \mu_s)^{n_s}$, where $\mu_1, \dots, \mu_s$ are distinct. Then there is an invertible $P$ such that $P^{-1}AP = U$ is an **upper triangular matrix** whose diagonal entries are $n_1$ copies of $\mu_1$, $n_2$ copies of $\mu_2$, …, $n_s$ copies of $\mu_s$ (in any prescribed order). Neither $P$ nor $U$ is unique.

**Proof** Induction on $n$; the case $n = 1$ is trivial. Take an eigenvector $\boldsymbol{p}_1$ of $A$ for $\mu_1$, extend it to a basis $\boldsymbol{p}_1, \dots, \boldsymbol{p}_n$ of $\mathbb{C}^n$, and let $P_1 = (\boldsymbol{p}_1, \dots, \boldsymbol{p}_n)$. Then $P_1^{-1}AP_1 = \begin{bmatrix} \mu_1 & \boldsymbol{\alpha}^{\mathsf T} \\ \boldsymbol{0} & A_1 \end{bmatrix}$, and the characteristic polynomial of $A_1$ is $\det(\lambda I - A)/(\lambda - \mu_1)$. By the induction hypothesis there is an invertible $Q$ such that $Q^{-1}A_1Q$ is upper triangular. Let $P = P_1 \begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & Q \end{bmatrix}$; then

$$
P^{-1}AP = \begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & Q^{-1} \end{bmatrix}\begin{bmatrix} \mu_1 & \boldsymbol{\alpha}^{\mathsf T} \\ \boldsymbol{0} & A_1 \end{bmatrix}\begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & Q \end{bmatrix} = \begin{bmatrix} \mu_1 & \boldsymbol{\alpha}^{\mathsf T}Q \\ \boldsymbol{0} & Q^{-1}A_1Q \end{bmatrix}
$$

is upper triangular. At each step we may choose which eigenvalue to take first, so the order of the diagonal entries can be prescribed. $\square$

[Chapter 6](/2.1.6) used the same result to prove the **Cayley–Hamilton theorem** (Theorem 6.9.2); Section 10.6 gives another proof. Schur's theorem here is unrelated to **Schur's lemma** in representation theory ([1.3.6](/1.3.6)). The proof is itself an algorithm that reduces the dimension step by step:

**Algorithm 10.3.1 (Schur Triangularization)** Input: $A \in \mathbb{C}^{n\times n}$.

1. Find an eigenvalue $\mu$ of $A$ and an eigenvector $\boldsymbol{p}_1$ (finding polynomial roots, solving a homogeneous system).
2. Extend $\boldsymbol{p}_1$ to a basis of $\mathbb{C}^n$, form $P_1$, and compute $P_1^{-1}AP_1 = \begin{bmatrix} \mu & \ast \\ \boldsymbol{0} & A_1 \end{bmatrix}$.
3. Repeat these steps for the matrix $A_1$ of order $n - 1$ to obtain $Q$, and set $P = P_1\operatorname{diag}(1, Q)$; stop when $A_1$ has order $1$.

**Example 10.3.1** For the matrix $A$ of Example 10.2.2, $\det(\lambda I_3 - A) = \lambda^2(\lambda - 1)$.

1. Take the eigenvector $\boldsymbol{p}_1 = (1, 1, 1)^{\mathsf T}$ for $\mu = 1$ and extend it to the basis $\boldsymbol{p}_1, \boldsymbol{e}_2, \boldsymbol{e}_3$. From $A\boldsymbol{e}_2 = (-5, -7, -9)^{\mathsf T} = -5\boldsymbol{p}_1 - 2\boldsymbol{e}_2 - 4\boldsymbol{e}_3$ and $A\boldsymbol{e}_3 = (2, 3, 4)^{\mathsf T} = 2\boldsymbol{p}_1 + \boldsymbol{e}_2 + 2\boldsymbol{e}_3$ we get $P_1 = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}$ and $P_1^{-1}AP_1 = \begin{bmatrix} 1 & -5 & 2 \\ 0 & -2 & 1 \\ 0 & -4 & 2 \end{bmatrix}$.
2. $A_1 = \begin{bmatrix} -2 & 1 \\ -4 & 2 \end{bmatrix}$ has the eigenvector $\boldsymbol{q}_1 = (1, 2)^{\mathsf T}$ ($A_1\boldsymbol{q}_1 = \boldsymbol{0}$); extending to $\boldsymbol{q}_1, \boldsymbol{e}_2$ gives $Q = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$ and $Q^{-1}A_1Q = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$.
3. $P = P_1\operatorname{diag}(1, Q) = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 2 & 1 \end{bmatrix}$ and $P^{-1}AP = \begin{bmatrix} 1 & -1 & 2 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$.

[Chapter 12](/2.1.12) strengthens Schur's theorem: $P$ can be chosen to be unitary.

## 10.4. Generalized Eigenvectors and Generalized Eigenspaces

The eigenvectors of a defective matrix do not span the whole space, so the notion of an eigenvector has to be extended. Throughout, let $A \in \mathbb{C}^{n\times n}$ with $\det(\lambda I_n - A) = (\lambda - \mu_1)^{n_1}\cdots(\lambda - \mu_s)^{n_s}$, the $\mu_i$ distinct.

**Definition 10.4.1** Let $\lambda_0 \in \mathbb{C}$. A nonzero vector $\boldsymbol{v} \in \mathbb{C}^n$ with $(A - \lambda_0 I_n)^k \boldsymbol{v} = \boldsymbol{0}$ for some $k \ge 1$ is called a **generalized eigenvector** of $A$ for $\lambda_0$; for $k = 1$ it is an eigenvector. The set consisting of the zero vector and all generalized eigenvectors for $\lambda_0$ is called the **generalized eigenspace** of $\lambda_0$:

$$
G_{\lambda_0} = \{\boldsymbol{v} \in \mathbb{C}^n \mid (A - \lambda_0 I_n)^k \boldsymbol{v} = \boldsymbol{0} \text{ for some } k \ge 1\}.
$$

Writing $N_{\lambda_0, k} = \mathcal{N}\left((A - \lambda_0 I_n)^k\right)$, we have

$$
V_{\lambda_0} = N_{\lambda_0, 1} \subseteq N_{\lambda_0, 2} \subseteq \cdots \subseteq \mathbb{C}^n, \qquad G_{\lambda_0} = \bigcup_{k \ge 1} N_{\lambda_0, k}, \qquad \dim N_{\lambda_0, k} = n - \operatorname{rank}\left((A - \lambda_0 I_n)^k\right).
$$

**Property 10.4.1**

1. $G_{\lambda_0}$ is a subspace (if $(A - \lambda_0 I)^{k_1}\boldsymbol{v}_1 = \boldsymbol{0} = (A - \lambda_0 I)^{k_2}\boldsymbol{v}_2$, then $(A - \lambda_0 I)^{k_1 + k_2}(\boldsymbol{v}_1 + \boldsymbol{v}_2) = \boldsymbol{0}$), and it is $A$-invariant ($A$ commutes with $(A - \lambda_0 I)^k$).
2. If $N_{\lambda_0, l} = N_{\lambda_0, l+1}$ for some $l$, then $N_{\lambda_0, l} = N_{\lambda_0, l+1} = N_{\lambda_0, l+2} = \cdots = G_{\lambda_0}$.
3. Hence the chain stabilizes after finitely many steps; the smallest index $l$ at which it stabilizes is determined by the rank sequence: $N_{\lambda_0, k} = N_{\lambda_0, k+1} \Leftrightarrow \operatorname{rank}\left((A - \lambda_0 I)^k\right) = \operatorname{rank}\left((A - \lambda_0 I)^{k+1}\right)$.

**Proof** 2: Let $\boldsymbol{v} \in N_{\lambda_0, l+2}$. Then $(A - \lambda_0 I)^{l+1}\left((A - \lambda_0 I)\boldsymbol{v}\right) = \boldsymbol{0}$, that is, $(A - \lambda_0 I)\boldsymbol{v} \in N_{\lambda_0, l+1} = N_{\lambda_0, l}$, so $(A - \lambda_0 I)^{l+1}\boldsymbol{v} = \boldsymbol{0}$ and $\boldsymbol{v} \in N_{\lambda_0, l+1}$. Induction finishes the argument. Since the dimensions of the $N_{\lambda_0,k}$ are at most $n$, strict growth cannot continue forever, which gives 3. $\square$

**Example 10.4.1** Let $A = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 2 \end{bmatrix}$, so $\det(\lambda I_4 - A) = (\lambda - 1)^3(\lambda - 2)$. Since $\operatorname{rank}(A - I) = 2 > \operatorname{rank}\left((A - I)^2\right) = 1 = \operatorname{rank}\left((A - I)^3\right)$,

$$
N_{1,1} \subsetneq N_{1,2} = N_{1,3} = \cdots = G_1, \qquad \dim N_{1,1} = 2, \quad \dim G_1 = 3,
$$

and the chain stabilizes at $l = 2$. Note that $\dim G_1$ equals the algebraic multiplicity $3$ of the eigenvalue $1$; this is no coincidence.

## 10.5. The Generalized Eigenspace Decomposition Theorem

We first collect a few simple facts about polynomials in a matrix. For $g(x) = a_kx^k + \cdots + a_0 \in \mathbb{C}[x]$, write $g(A) = a_kA^k + \cdots + a_1A + a_0I_n$.

**Lemma 10.5.1** Let $f, g \in \mathbb{C}[x]$, $A \in \mathbb{C}^{n\times n}$, and let $P$ be invertible.

1. $f(A)g(A) = g(A)f(A)$;
2. $P^{-1}f(A)P = f(P^{-1}AP)$ (because $P^{-1}A^kP = (P^{-1}AP)^k$);
3. if $A\boldsymbol{v} = \lambda_0 \boldsymbol{v}$, then $g(A)\boldsymbol{v} = g(\lambda_0)\boldsymbol{v}$.

**Lemma 10.5.2** Generalized eigenvectors belonging to distinct eigenvalues are linearly independent: if $\boldsymbol{v}_i \in G_{\mu_i}$ ($i = 1, \dots, s$) and $\boldsymbol{v}_1 + \cdots + \boldsymbol{v}_s = \boldsymbol{0}$, then every $\boldsymbol{v}_i = \boldsymbol{0}$.

**Proof** Suppose $c_1\boldsymbol{v}_1 + \cdots + c_s\boldsymbol{v}_s = \boldsymbol{0}$ with nonzero $\boldsymbol{v}_i \in G_{\mu_i}$; fix $i$ and let us show $c_i = 0$. Choose $K$ so large that $(A - \mu_j I)^K \boldsymbol{v}_j = \boldsymbol{0}$ for all $j$, and let $g(x) = \prod_{j \ne i}(x - \mu_j)^K$. Then $g(A)\boldsymbol{v}_j = \boldsymbol{0}$ ($j \ne i$), hence $c_i g(A)\boldsymbol{v}_i = \boldsymbol{0}$. Let $k$ be the smallest positive integer with $(A - \mu_i I)^k \boldsymbol{v}_i = \boldsymbol{0}$; then $\boldsymbol{w} = (A - \mu_i I)^{k-1}\boldsymbol{v}_i \ne \boldsymbol{0}$ is an eigenvector. Applying $(A - \mu_i I)^{k-1}$ and commuting the factors gives $c_i g(A)\boldsymbol{w} = c_i g(\mu_i)\boldsymbol{w} = \boldsymbol{0}$. Since $g(\mu_i) \ne 0$, we get $c_i = 0$. $\square$

**Theorem 10.5.1 (Generalized Eigenspace Decomposition)** Let $A \in \mathbb{C}^{n\times n}$ with $\det(\lambda I_n - A) = (\lambda - \mu_1)^{n_1}\cdots(\lambda - \mu_s)^{n_s}$, the $\mu_i$ distinct. Then

1. $\dim G_{\mu_i} = n_i$, that is, the dimension of a generalized eigenspace equals the **algebraic multiplicity**;
2. $G_{\mu_i} = \mathcal{N}\left((A - \mu_i I_n)^{n_i}\right)$;
3. $\mathbb{C}^n = G_{\mu_1} \oplus \cdots \oplus G_{\mu_s}$.

**Proof** 1, 2: Take $\mu_1$ as an example. By Schur's theorem there is $P$ with $P^{-1}AP = \begin{bmatrix} B_{11} & B_{12} \\ O & B_{22} \end{bmatrix}$, where $B_{11}$ is an upper triangular matrix of order $n_1$ with all diagonal entries equal to $\mu_1$, and $B_{22}$ is upper triangular with no diagonal entry equal to $\mu_1$. Then

$$
P^{-1}(A - \mu_1 I)^k P = \begin{bmatrix} C_{11}^k & \ast \\ O & C_{22}^k \end{bmatrix}, \qquad C_{11} = B_{11} - \mu_1 I, \quad C_{22} = B_{22} - \mu_1 I,
$$

where $C_{11}$ is strictly upper triangular, so $C_{11}^{n_1} = O$, and $C_{22}$ is invertible. For $k \ge n_1$ the right-hand side has the form $\begin{bmatrix} O & \ast \\ O & C_{22}^k \end{bmatrix}$ and rank $n - n_1$. Therefore $\dim N_{\mu_1, k} = n_1$ for all $k \ge n_1$, the chain has already stabilized at $k = n_1$, and $G_{\mu_1} = N_{\mu_1, n_1}$ has dimension $n_1$.

3: By Lemma 10.5.2 the zero vector has a unique representation in $G_{\mu_1} + \cdots + G_{\mu_s}$, so the sum is direct (condition 3 of Theorem 10.1.1); its dimension is $n_1 + \cdots + n_s = n$, so it is all of $\mathbb{C}^n$. $\square$

Putting the bases of the generalized eigenspaces together into a new basis gives the matrix form.

**Theorem 10.5.2** Under the hypotheses of Theorem 10.5.1, let $\boldsymbol{v}_{i1}, \dots, \boldsymbol{v}_{in_i}$ be a basis of $G_{\mu_i}$ and $P = (\boldsymbol{v}_{11}, \dots, \boldsymbol{v}_{1n_1}, \dots, \boldsymbol{v}_{s1}, \dots, \boldsymbol{v}_{sn_s})$. Then

$$
P^{-1}AP = \operatorname{diag}(A_1, \dots, A_s), \qquad A(\boldsymbol{v}_{i1}, \dots, \boldsymbol{v}_{in_i}) = (\boldsymbol{v}_{i1}, \dots, \boldsymbol{v}_{in_i})A_i,
$$

where $A_i$ is a matrix of order $n_i$ with the single eigenvalue $\mu_i$: $\det(\lambda I_{n_i} - A_i) = (\lambda - \mu_i)^{n_i}$.

**Proof** The block diagonal form comes from the invariance of $G_{\mu_i}$ (Theorem 10.2.1). If $A_i$ has an eigenvalue $\lambda_0$ with eigenvector $\boldsymbol{x}$, then $\boldsymbol{w} = (\boldsymbol{v}_{i1}, \dots, \boldsymbol{v}_{in_i})\boldsymbol{x} \in G_{\mu_i}$ is nonzero and $A\boldsymbol{w} = \lambda_0 \boldsymbol{w}$. From $(A - \mu_i I)^{n_i}\boldsymbol{w} = \boldsymbol{0}$ and part 3 of Lemma 10.5.1, $(\lambda_0 - \mu_i)^{n_i}\boldsymbol{w} = \boldsymbol{0}$, so $\lambda_0 = \mu_i$. $\square$

**Corollary 10.5.1** $A$ is diagonalizable $\Leftrightarrow$ $\mathbb{C}^n = V_{\mu_1} \oplus \cdots \oplus V_{\mu_s}$ $\Leftrightarrow$ the algebraic multiplicity of every eigenvalue equals its **geometric multiplicity** $\Leftrightarrow$ $G_{\mu_i} = V_{\mu_i}$ for every $i$.

**Example 10.5.1** Let $A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 2 & -5 & 4 \end{bmatrix}$ (a **companion matrix**), with $\det(\lambda I_3 - A) = (\lambda - 1)^2(\lambda - 2)$. Then

$$
G_1 = \mathcal{N}\left((A - I)^2\right) = \mathcal{N}\begin{bmatrix} 1 & -2 & 1 \\ 2 & -4 & 2 \\ 4 & -8 & 4 \end{bmatrix} = \operatorname{span}\left\{\begin{bmatrix}2\\1\\0\end{bmatrix}, \begin{bmatrix}1\\0\\-1\end{bmatrix}\right\}, \qquad G_2 = \mathcal{N}(A - 2I) = \operatorname{span}\left\{\begin{bmatrix}1\\2\\4\end{bmatrix}\right\}.
$$

Let $P = \begin{bmatrix} 2 & 1 & 1 \\ 1 & 0 & 2 \\ 0 & -1 & 4 \end{bmatrix}$. From $A(2,1,0)^{\mathsf T} = (1, 0, -1)^{\mathsf T}$ and $A(1, 0, -1)^{\mathsf T} = (0, -1, -2)^{\mathsf T} = -(2,1,0)^{\mathsf T} + 2(1,0,-1)^{\mathsf T}$ we obtain

$$
P^{-1}AP = \begin{bmatrix} A_1 & \\ & A_2 \end{bmatrix}, \qquad A_1 = \begin{bmatrix} 0 & -1 \\ 1 & 2 \end{bmatrix}, \quad A_2 = (2).
$$

The characteristic polynomial of $A_1$ is $(\lambda - 1)^2$, in agreement with Theorem 10.5.2.

## 10.6. The Cayley–Hamilton Theorem and the Minimal Polynomial

**Definition 10.6.1** Let $g \in \mathbb{C}[x]$. If $g(A) = O$, then $g$ is called an **annihilating polynomial** of $A$.

**Theorem 10.6.1 (Cayley–Hamilton Theorem)** Let $f(\lambda) = \det(\lambda I_n - A) = \lambda^n + a_1\lambda^{n-1} + \cdots + a_n$ be the **characteristic polynomial** of $A$. Then $f(A) = A^n + a_1A^{n-1} + \cdots + a_nI_n = O$.

**Proof** By Theorem 10.5.2, $P^{-1}AP = B = \operatorname{diag}(A_1, \dots, A_s)$, where $A_i$ has the single eigenvalue $\mu_i$. By Schur's theorem, $A_i - \mu_i I$ is similar to a strictly upper triangular matrix, so $(A_i - \mu_i I)^{n_i} = O$. Hence

$$
P^{-1}f(A)P = f(B) = (B - \mu_1 I)^{n_1}\cdots(B - \mu_s I)^{n_s}
$$

is block diagonal, and its $i$-th diagonal block is the matrix $\prod_j (A_i - \mu_j I)^{n_j}$ of order $n_i$. These factors commute, and one of them is $(A_i - \mu_i I)^{n_i} = O$; so every diagonal block is zero and $f(A) = O$. $\square$

The characteristic polynomial is an annihilating polynomial of degree $n$. An annihilating polynomial of the lowest degree carries more information.

**Definition 10.6.2** The monic annihilating polynomial of $A$ of the lowest degree is called the **minimal polynomial** of $A$ and is denoted $m_A(x)$.

**Property 10.6.1**

1. If $g(A) = O$, then $m_A \mid g$. In particular, $m_A$ divides the characteristic polynomial.
2. $m_A$ is unique.
3. Similar matrices have the same minimal polynomial.
4. If $A = \operatorname{diag}(A_1, \dots, A_s)$, then $m_A$ is the monic least common multiple of $m_{A_1}, \dots, m_{A_s}$.
5. If $\det(\lambda I_n - A) = \prod_{i=1}^s (\lambda - \mu_i)^{n_i}$, then $m_A(x) = \prod_{i=1}^s (x - \mu_i)^{m_i}$, where $1 \le m_i \le n_i$ and $m_i$ is the smallest $l$ with $N_{\mu_i, l} = G_{\mu_i}$, that is, the index at which the rank sequence $\operatorname{rank}\left((A - \mu_i I)^k\right)$ first stops decreasing.
6. $A$ is diagonalizable $\Leftrightarrow$ $m_A$ has no **multiple roots**.

**Proof** 1: Apply **division with remainder**: $g = qm_A + r$ with $\deg r < \deg m_A$. Substituting $A$ gives $r(A) = O$, and since $m_A$ has the lowest degree, $r = 0$. 2: Two monic minimal polynomials divide each other, hence are equal. 3: If $B = P^{-1}AP$, then $m_A(B) = P^{-1}m_A(A)P = O$, so $m_B \mid m_A$; likewise $m_A \mid m_B$. 4: $g(A) = \operatorname{diag}(g(A_1), \dots, g(A_s))$, so $g(A) = O \Leftrightarrow$ every $m_{A_i} \mid g$.

5: By 3, 4 and Theorem 10.5.2, $m_A = m_B$ is the least common multiple of the $m_{A_i}$. Since $(A_i - \mu_i I)^{n_i} = O$, part 1 gives $m_{A_i} = (x - \mu_i)^{m_i}$, where $m_i \le n_i$ is the smallest $k$ with $(A_i - \mu_i I)^k = O$; the $m_{A_i}$ are pairwise **coprime**, so their least common multiple is their product. Finally, $A_j - \mu_i I$ ($j \ne i$) is invertible, so

$$
\operatorname{rank}\left((A - \mu_i I)^k\right) = \operatorname{rank}\left((A_i - \mu_i I)^k\right) + \sum_{j \ne i} n_j,
$$

and the index at which the rank sequence stops decreasing is the index at which $(A_i - \mu_i I)^k$ first becomes zero (the ranks of the powers of a nilpotent matrix decrease strictly until they reach zero, by part 2 of Property 10.4.1), namely $m_i$.

6: By Corollary 10.5.1, $A$ is diagonalizable $\Leftrightarrow$ $G_{\mu_i} = N_{\mu_i, 1}$ $\Leftrightarrow$ all $m_i = 1$. $\square$

**Example 10.6.1** The characteristic polynomial of $A = \operatorname{diag}(1, 1, 2)$ is $(x - 1)^2(x - 2)$ and its minimal polynomial is $(x - 1)(x - 2)$; the minimal polynomial of $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ is $(x - 1)^2$, which has a multiple root, so this matrix is not diagonalizable.

**Example 10.6.2** If $A^2 = I_n$, then $x^2 - 1 = (x - 1)(x + 1)$ is an annihilating polynomial; $m_A$ divides it and therefore has no multiple roots, so $A$ is diagonalizable. Similarly, every complex matrix satisfying $A^2 = A$ (a projection) or $A^k = I$ is diagonalizable.

To decide diagonalizability we only have to check whether one polynomial has multiple roots, and this in turn can be decided via $\gcd(m_A, m_A')$ (the **greatest common divisor** of [Chapter 9](/2.1.9)), without computing a single eigenvector.

## 10.7. Nilpotent Transformations and Cyclic Subspaces

By Theorem 10.5.2 it suffices to simplify each block $A_i$ with a single eigenvalue. Since $A_i - \mu_iI$ is nilpotent, the problem reduces to finding the simplest form of a nilpotent transformation.

**Definition 10.7.1** Let $V$ be an $n$-dimensional complex space and $T\colon V \to V$ a linear transformation. If there is $m \ge 1$ with $T^m = O$ but $T^{m-1} \ne O$, then $T$ is called a **nilpotent transformation** and $m$ is called the **index of nilpotency** of $T$. If $m = \dim V$, then $T$ is called a **cyclic transformation**.

In this course, a "cyclic transformation" always means a nilpotent transformation whose index of nilpotency equals the dimension. In the general literature, a cyclic operator is any linear transformation for which some vector $v$ has $v, Tv, T^2v, \dots$ spanning $V$; for nilpotent transformations the two notions agree.

**Property 10.7.1** Let $A$ be the matrix of $T$ with respect to some basis.

1. $T$ is nilpotent $\Leftrightarrow$ $A$ is a **nilpotent matrix**; the indices of nilpotency agree, and $m_A(x) = x^m$;
2. $T$ is nilpotent $\Leftrightarrow$ the only eigenvalue of $T$ is $0$;
3. if $T$ is nilpotent, then $T^n = O$, that is, the index of nilpotency is at most $n$.

**Proof** 1: The matrix of $T^k$ is $A^k$. 2: By Schur's theorem, $A$ is similar to an upper triangular $U$, and the diagonal entries of $U^k$ are $\lambda_i^k$; if $A^k = O$, then all $\lambda_i = 0$; conversely, an upper triangular matrix with zero diagonal satisfies $U^n = O$. 3: By 2, the characteristic polynomial is $\lambda^n$; now apply the Cayley–Hamilton theorem. $\square$

**Example 10.7.1** Let $T\colon \mathbb{C}^4 \to \mathbb{C}^4$, $(z_1, z_2, z_3, z_4)^{\mathsf T} \mapsto (0, z_1, z_2, z_3)^{\mathsf T}$. Then $T^3 \ne O$ and $T^4 = O$; the index of nilpotency is $4 = \dim \mathbb{C}^4$, so $T$ is cyclic, and $\boldsymbol{e}_1, T\boldsymbol{e}_1 = \boldsymbol{e}_2, T^2\boldsymbol{e}_1 = \boldsymbol{e}_3, T^3\boldsymbol{e}_1 = \boldsymbol{e}_4$ form a basis. By contrast, $(z_1, \dots, z_5)^{\mathsf T} \mapsto (0, z_1, 0, z_3, 0)^{\mathsf T}$ satisfies $T^2 = O$; it is nilpotent but not cyclic.

**Definition 10.7.2** Let $T\colon V \to V$ be nilpotent, $v \ne 0$, and let $k$ be the smallest positive integer with $T^kv = 0$. The subspace $C_v = \operatorname{span}\{T^{k-1}v, T^{k-2}v, \dots, Tv, v\}$ is called the **cyclic subspace** generated by $v$, and $T^{k-1}v, \dots, Tv, v$ is called the **cyclic basis** of $C_v$.

**Property 10.7.2**

1. $T^{k-1}v, \dots, Tv, v$ are linearly independent, and $\dim C_v = k$;
2. $C_v$ is a $T$-invariant subspace, $T|_{C_v}$ is a cyclic transformation, and its matrix with respect to the cyclic basis is

$$
J_{0,k} = \begin{bmatrix} 0 & 1 & & \\ & 0 & \ddots & \\ & & \ddots & 1 \\ & & & 0 \end{bmatrix}_{k \times k};
$$

3. call $C_v$ maximal if there is no $w$ with $C_v \subsetneq C_w$. Then $C_v$ is maximal $\Leftrightarrow$ $v \notin \mathcal{R}(T)$.

**Proof** 1: Suppose $c_1T^{k-1}v + \cdots + c_{k-1}Tv + c_kv = 0$. Applying $T^{k-1}$ gives $c_kT^{k-1}v = 0$, so $c_k = 0$; applying $T^{k-2}$ then gives $c_{k-1} = 0$, and so on. 2: $T(T^{k-1}v) = 0$ and $T(T^jv) = T^{j+1}v$; the $(j+1)$-th column of the matrix is the coordinate vector of the $j$-th basis vector. 3: If $v = Tw$, then $C_v \subsetneq C_w$. Conversely, let $v \notin \mathcal{R}(T)$ and $C_v \subseteq C_w$ with $\dim C_w = l$. Write $v = a_0w + a_1Tw + \cdots + a_{l-1}T^{l-1}w$; since $v \notin \mathcal{R}(T)$, $a_0 \ne 0$, so $T^{l-1}v = a_0T^{l-1}w \ne 0$ and $\dim C_v \ge l$. Hence $C_v = C_w$. $\square$

$J_{0,k}$ is the **Jordan block** with eigenvalue $0$. The textbook and the lecture slides call it a "cyclic matrix", but in standard usage that name (circulant matrix) refers to a different class of matrices, in which each row is a cyclic shift of the previous one; on this site $J_{0,k}$ is called a nilpotent Jordan block or a shift matrix.

**Example 10.7.2** For $A = J_{0,4}$, the vector $\boldsymbol{v} = \boldsymbol{e}_4 \notin \mathcal{R}(A)$ generates the maximal subspace $C_{\boldsymbol{e}_4} = \mathbb{C}^4$, whereas $\boldsymbol{w} = \boldsymbol{e}_3 = A\boldsymbol{e}_4 \in \mathcal{R}(A)$ generates $C_{\boldsymbol{e}_3} = \operatorname{span}\{\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}_3\} \subsetneq C_{\boldsymbol{e}_4}$.

## 10.8. Cyclic Decomposition of a Nilpotent Transformation

This section is the heart of the Jordan theorem: the space of a nilpotent transformation always decomposes into a direct sum of maximal cyclic subspaces. The proof uses the **rank–nullity theorem** $\dim V = \dim \mathcal{R}(T) + \dim \mathcal{N}(T)$. By it, if $T$ is nilpotent, then $\mathcal{N}(T) \ne \{0\}$, hence $\dim \mathcal{R}(T) < \dim V$, which makes induction on the dimension possible.

**Theorem 10.8.1** Let $V$ be an $n$-dimensional complex space and $T\colon V \to V$ nilpotent. Then there are $v_1, \dots, v_t \in V$ with

$$
V = C_{v_1} \oplus \cdots \oplus C_{v_t}
$$

and $v_1, \dots, v_t \notin \mathcal{R}(T)$ (all the cyclic subspaces are maximal).

**Proof** First a remark: if $V = C_{x_1} \oplus \cdots \oplus C_{x_t}$, then $T$ acts as a shift on each $C_{x_i}$, and $\mathcal{N}(T)$ is spanned by the first vectors of the cyclic bases (eigenvectors of $T$), so $\dim \mathcal{N}(T) = t$.

We use induction on $n$. For $n = 1$, $T = O$ and $V = C_v$ for any $v \ne 0$. Assume the statement holds for spaces of dimension less than $n$. If $T = O$, take any basis $w_1, \dots, w_n$ of $V$; then $V = C_{w_1} \oplus \cdots \oplus C_{w_n}$. Now let $T \ne O$ and $V_1 = \mathcal{R}(T)$; this is an invariant subspace with $0 < \dim V_1 < n$, and $T|_{V_1}$ is nilpotent. By the induction hypothesis,

$$
V_1 = C_{u_1} \oplus \cdots \oplus C_{u_s}, \qquad u_i \notin T(V_1) = \mathcal{R}(T^2).
$$

Let $\dim C_{u_i} = b_i$. Since $u_i \in \mathcal{R}(T)$, choose $v_i$ with $Tv_i = u_i$. The cyclic basis of $C_{v_i}$ is then $T^{b_i}v_i, \dots, Tv_i, v_i$, so $\dim C_{v_i} = b_i + 1$; moreover $v_i \notin \mathcal{R}(T)$ (otherwise $u_i \in \mathcal{R}(T^2)$).

The vectors $T^{b_i - 1}u_i = T^{b_i}v_i$ ($i = 1, \dots, s$) lie in $\mathcal{N}(T) \cap \mathcal{R}(T)$, and by the remark above they form a basis of $\mathcal{N}(T|_{V_1}) = \mathcal{N}(T) \cap \mathcal{R}(T)$. Extend them to a basis $T^{b_1}v_1, \dots, T^{b_s}v_s, w_1, \dots, w_r$ of $\mathcal{N}(T)$; then $w_j \notin \mathcal{R}(T)$ (otherwise $w_j \in \mathcal{N}(T) \cap \mathcal{R}(T)$, contradicting the choice of the extension). We show that

$$
\mathcal{B} = \{T^jv_i \mid 1 \le i \le s, 0 \le j \le b_i\} \cup \{w_1, \dots, w_r\}
$$

is a basis of $V$, so that $V = C_{v_1} \oplus \cdots \oplus C_{v_s} \oplus C_{w_1} \oplus \cdots \oplus C_{w_r}$ (with $\dim C_{w_j} = 1$).

Counting: $\sum_i (b_i + 1) + r = \dim V_1 + s + r = \dim \mathcal{R}(T) + \dim \mathcal{N}(T) = n$. Linear independence: suppose $\sum_{i,j} c_{ij}T^jv_i + \sum_k d_kw_k = 0$. Applying $T$ gives $\sum_i \sum_{j < b_i} c_{ij}T^ju_i = 0$, and $\{T^ju_i\}$ is a basis of $V_1$, so $c_{ij} = 0$ for $j < b_i$. What remains, $\sum_i c_{ib_i}T^{b_i}v_i + \sum_k d_kw_k = 0$, is a combination of a basis of $\mathcal{N}(T)$, so all coefficients vanish. $\square$

The proof is a bottom-up construction: first decompose $\mathcal{R}(T)$, then extend each cyclic basis "one step up", and finally fill in with the remaining directions of $\mathcal{N}(T)$.

**Corollary 10.8.1** In Theorem 10.8.1,

1. the number of cyclic subspaces is $t = \dim \mathcal{N}(T)$, the geometric multiplicity of the eigenvalue $0$;
2. the largest dimension of a cyclic subspace equals the index of nilpotency of $T$.

## 10.9. Existence and Structure of the Jordan Canonical Form

Translating Theorem 10.8.1 into the language of matrices, each cyclic basis corresponds to a nilpotent Jordan block.

**Theorem 10.9.1** Let $A \in \mathbb{C}^{n\times n}$ be nilpotent. Then there is an invertible $P$ with

$$
P^{-1}AP = J = \operatorname{diag}(J_{0,b_1}, \dots, J_{0,b_t}),
$$

where $t = \dim \mathcal{N}(A) = n - \operatorname{rank}(A)$. The matrix $J$ is called the Jordan canonical form of the nilpotent matrix $A$, and $P$ is obtained by arranging the cyclic bases of the cyclic subspaces one after another.

**Definition 10.9.1** Let $\mu \in \mathbb{C}$. If $\boldsymbol{v} \ne \boldsymbol{0}$ satisfies $(A - \mu I)^k\boldsymbol{v} = \boldsymbol{0}$ but $(A - \mu I)^{k-1}\boldsymbol{v} \ne \boldsymbol{0}$, then the vectors $(A - \mu I)^{k-1}\boldsymbol{v}, (A - \mu I)^{k-2}\boldsymbol{v}, \dots, (A - \mu I)\boldsymbol{v}, \boldsymbol{v}$ are called a **Jordan chain** of $A$ of length $k$ for $\mu$; the first vector is an eigenvector and the others are generalized eigenvectors. A basis consisting of Jordan chains for which $P^{-1}AP$ is a Jordan canonical form is called a **Jordan basis**.

**Definition 10.9.2 (Jordan Block)** The matrix of order $k$

$$
J_{\lambda,k} = \lambda I_k + J_{0,k} = \begin{bmatrix} \lambda & 1 & & \\ & \lambda & \ddots & \\ & & \ddots & 1 \\ & & & \lambda \end{bmatrix}
$$

is called the Jordan block of order $k$ for $\lambda$ (written $J_k(\lambda)$ in Chapter 6). Both its characteristic polynomial and its minimal polynomial are $(x - \lambda)^k$.

Comparing the columns of $AP = PJ$ shows that a Jordan block $J_{\mu,k}$ of order $k$ in $J$ corresponds exactly to a Jordan chain of length $k$ in $P$. For example, if $J = \operatorname{diag}(J_{1,2}, J_{1,1}, J_{2,2})$ and $P = (\boldsymbol{p}_1, \dots, \boldsymbol{p}_5)$, then $(A - I)\boldsymbol{p}_1 = \boldsymbol{0}$, $(A - I)\boldsymbol{p}_2 = \boldsymbol{p}_1$, $(A - I)\boldsymbol{p}_3 = \boldsymbol{0}$, $(A - 2I)\boldsymbol{p}_4 = \boldsymbol{0}$, $(A - 2I)\boldsymbol{p}_5 = \boldsymbol{p}_4$: the three chains are $\boldsymbol{p}_1, \boldsymbol{p}_2$; $\boldsymbol{p}_3$; and $\boldsymbol{p}_4, \boldsymbol{p}_5$.

**Theorem 10.9.2 (Jordan Canonical Form)** Let $A \in \mathbb{C}^{n\times n}$ with $\det(\lambda I_n - A) = (\lambda - \mu_1)^{n_1}\cdots(\lambda - \mu_s)^{n_s}$, the $\mu_i$ distinct. Then there is an invertible $P$ with

$$
P^{-1}AP = J = \operatorname{diag}(J_{\mu_1}, \dots, J_{\mu_s}), \qquad J_{\mu_i} = \operatorname{diag}(J_{\mu_i, m_{i1}}, \dots, J_{\mu_i, m_{it_i}}),
$$

where $J_{\mu_i}$ has order $n_i$, $m_{i1} \ge \cdots \ge m_{it_i} \ge 1$, and the number of blocks for $\mu_i$ is $t_i = n - \operatorname{rank}(A - \mu_iI)$, the geometric multiplicity of $\mu_i$. Up to the order of the Jordan blocks, $J$ is uniquely determined by $A$.

**Proof** Existence: by Theorem 10.5.2, $\mathbb{C}^n = G_{\mu_1} \oplus \cdots \oplus G_{\mu_s}$, and $A - \mu_iI$ is a nilpotent transformation of $G_{\mu_i}$. Applying Theorem 10.9.1 to it yields a basis of $G_{\mu_i}$ in which the matrix of $(A - \mu_iI)|_{G_{\mu_i}}$ is a direct sum of nilpotent Jordan blocks; hence the matrix of $A|_{G_{\mu_i}}$ is $J_{\mu_i}$. The number of blocks is $\dim \mathcal{N}\big((A - \mu_iI)|_{G_{\mu_i}}\big) = \dim V_{\mu_i}$. Uniqueness follows from Theorem 10.9.3 below: the number of blocks of each order is determined by ranks, and ranks are invariant under similarity. $\square$

**Theorem 10.9.3** Let $A$ be as in Theorem 10.9.2 and $d \ge 1$. Among the Jordan blocks of $A$ for $\mu_i$,

$$
\text{number of blocks of order} \ge d = \operatorname{rank}\left((A - \mu_iI)^{d-1}\right) - \operatorname{rank}\left((A - \mu_iI)^d\right),
$$

$$
\text{number of blocks of order} = d = \operatorname{rank}\left((A - \mu_iI)^{d-1}\right) - 2\operatorname{rank}\left((A - \mu_iI)^d\right) + \operatorname{rank}\left((A - \mu_iI)^{d+1}\right),
$$

where $(A - \mu_iI)^0 = I$. In particular, a nilpotent matrix $A$ has $n - \operatorname{rank}(A)$ Jordan blocks, the largest block has order equal to the index of nilpotency, and the number of blocks of order $d$ is $\operatorname{rank}(A^{d-1}) + \operatorname{rank}(A^{d+1}) - 2\operatorname{rank}(A^d)$.

**Proof** $\operatorname{rank}\left((A - \mu_iI)^k\right) = \operatorname{rank}\left((J - \mu_iI)^k\right)$. In $J - \mu_iI$ the blocks for $\mu_j$ ($j \ne i$) are invertible and always contribute rank $n_j$; the blocks for $\mu_i$ become nilpotent blocks, and $\operatorname{rank}(J_{0,b}^k) = \max(b - k, 0)$. Hence

$$
\operatorname{rank}\left((A - \mu_iI)^k\right) = \sum_{j \ne i} n_j + \sum_{l=1}^{t_i} \max(m_{il} - k, 0).
$$

Subtracting the cases $k = d$ and $k = d - 1$, each block of order $\ge d$ contributes exactly $1$ and every other block contributes $0$, which gives the first formula. The second formula is the difference of the first one for $d$ and $d + 1$. $\square$

**Corollary 10.9.1**

1. In the minimal polynomial $m_A(x) = \prod (x - \mu_i)^{m_i}$, the exponent $m_i$ equals the order of the largest Jordan block for $\mu_i$;
2. two complex square matrices of order $n$ are similar $\Leftrightarrow$ they have the same eigenvalues and $\operatorname{rank}\left((A - \mu I)^k\right) = \operatorname{rank}\left((B - \mu I)^k\right)$ for every eigenvalue $\mu$ and every $k$.

Thus deciding similarity and finding the Jordan form both reduce to computing ranks, that is, to elimination.

**Example 10.9.1** Let $A = (\boldsymbol{0}, \boldsymbol{e}_1, \boldsymbol{0}, 2\boldsymbol{e}_2, \boldsymbol{0}, \boldsymbol{e}_3) \in \mathbb{C}^{6\times 6}$ (given by its columns). Then $A^2 = (\boldsymbol{0}, \boldsymbol{0}, \boldsymbol{0}, 2\boldsymbol{e}_1, \boldsymbol{0}, \boldsymbol{0})$, $A^3 = O$, $\operatorname{rank}(A) = 3$, $\operatorname{rank}(A^2) = 1$ and $\operatorname{rank}(A^3) = 0$. The numbers of blocks of order $\ge 1, \ge 2, \ge 3$ are $6 - 3 = 3$, $3 - 1 = 2$ and $1 - 0 = 1$, so $J = \operatorname{diag}(J_{0,3}, J_{0,2}, J_{0,1})$.

If each Jordan chain is drawn as a column, with the eigenvector at the bottom of the chain, we obtain the dot diagram on the right of the figure below: the number of dots in row $d$ is the number of blocks of order $\ge d$, that is, the difference of two consecutive terms of the rank sequence. The column lengths of the dot diagram give the Jordan form, its row lengths give the rank sequence, and each determines the other.

![The nilpotent matrix of Example 10.9.1. Left: the rank sequence r_k = rank(A^k); each drop equals the number of Jordan blocks of order at least k. Right: the corresponding three Jordan chains (of orders 3, 2, 1); arrows indicate applying A, and the number of dots in row d equals r_{d-1} - r_d](./plots/rank-sequence-dot-diagram.py)

**Example 10.9.2** Let $A = \begin{bmatrix} 1 & 2 & 2 & 0 & 0 \\ 2 & 1 & 2 & 0 & 0 \\ 2 & 2 & 1 & 0 & 0 \\ 0 & 0 & 0 & 5 & 0 \\ 0 & 0 & 0 & 2 & 5 \end{bmatrix}$, so $\det(\lambda I_5 - A) = (\lambda + 1)^2(\lambda - 5)^3$. Since $\operatorname{rank}(A + I) = 3$, there are $5 - 3 = 2$ blocks for $-1$, and as the algebraic multiplicity of $-1$ is $2$, these are two blocks of order $1$. Since $\operatorname{rank}(A - 5I) = 3$, there are also $2$ blocks for $5$, with total order $3$, which forces $2 + 1$. Therefore $J = \operatorname{diag}(-1, -1, J_{5,2}, 5)$.

**Example 10.9.3** Let $n \ge 2$; we find the Jordan form of $J_{0,n}^2$. All eigenvalues of $J_{0,n}^2$ are $0$ and $\operatorname{rank}(J_{0,n}^2) = n - 2$, so there are two blocks. $J_{0,n}^k$ vanishes for $k \ge n$. For $n = 2m$, $(J_{0,n}^2)^m = O \ne (J_{0,n}^2)^{m-1}$, so the minimal polynomial is $x^m$, the largest block has order $m$, and the Jordan form is $\operatorname{diag}(J_{0,m}, J_{0,m})$; for $n = 2m + 1$ the minimal polynomial is $x^{m+1}$ and the Jordan form is $\operatorname{diag}(J_{0,m+1}, J_{0,m})$. Intuitively, $J_{0,n}^2$ splits into the two chains $\boldsymbol{e}_n \mapsto \boldsymbol{e}_{n-2} \mapsto \cdots$ and $\boldsymbol{e}_{n-1} \mapsto \boldsymbol{e}_{n-3} \mapsto \cdots$ of even and odd indices.

## 10.10. Computing a Jordan Basis

The Jordan form requires only ranks, whereas a Jordan basis $P$ requires constructing the Jordan chains one by one. In doing so one must make sure that the different chains together are linearly independent; this is the only delicate point of the computation.

**Algorithm 10.10.1 (Jordan Canonical Form and Jordan Basis)** Input: $A \in \mathbb{C}^{n\times n}$.

1. Eigenvalues: find the roots $\mu_1, \dots, \mu_s$ of the characteristic polynomial and their algebraic multiplicities $n_1, \dots, n_s$.
2. Block structure: for each $\mu_i$, compute $r_k = \operatorname{rank}\left((A - \mu_iI)^k\right)$ for $k = 1, 2, \dots$ until $r_k = n - n_i$; the number of blocks of order $\ge k$ is $r_{k-1} - r_k$ (with $r_0 = n$). This gives $J$.
3. Jordan chains (top-down): let $N_k = \mathcal{N}\left((A - \mu_iI)^k\right)$ and let $m_i$ be the order of the largest block. For $k = m_i, m_i - 1, \dots, 1$, choose vectors $\boldsymbol{y}$ in $N_k$, as many as there are blocks of order $k$, such that together with a basis of $N_{k-1}$ and the images $(A - \mu_iI)^{j-k}\boldsymbol{y}'$ of the vectors $\boldsymbol{y}'$ already chosen at higher levels ($j > k$) they are linearly independent. Each $\boldsymbol{y}$ generates a chain $(A - \mu_iI)^{k-1}\boldsymbol{y}, \dots, (A - \mu_iI)\boldsymbol{y}, \boldsymbol{y}$.
4. Assembly: arrange all chains into $P$ in the order of the blocks of $J$ (each chain starting with its eigenvector); then $P^{-1}AP = J$.

Step 1 is root finding, step 2 is a sequence of eliminations, and step 3 consists of solving homogeneous linear systems and checking linear independence (again a rank computation). The independence condition in step 3 cannot be dropped: if the top vectors are chosen badly, the eigenvectors of different chains coincide and $P$ is singular (see Example 10.10.2). For small matrices one often proceeds bottom-up instead: take the eigenvector at the bottom of a chain from $\mathcal{N}(A - \mu_iI) \cap \mathcal{R}\left((A - \mu_iI)^{k-1}\right)$, and then extend the chain upward by successively solving $(A - \mu_iI)\boldsymbol{x} = $ (the previous vector).

**Example 10.10.1** Let $A = \begin{bmatrix} 3 & 0 & 8 \\ 3 & -1 & 6 \\ -2 & 0 & -5 \end{bmatrix}$, so $\det(\lambda I - A) = (\lambda + 1)^3$. Since $\operatorname{rank}(A + I) = 1$ and $(A + I)^2 = O$, there are $3 - 1 = 2$ blocks and the largest has order $2$: $J = \operatorname{diag}(J_{-1,2}, -1)$. Bottom-up: the column space of $A + I = \begin{bmatrix} 4 & 0 & 8 \\ 3 & 0 & 6 \\ -2 & 0 & -4 \end{bmatrix}$ is spanned by $(4, 3, -2)^{\mathsf T}$, which also lies in $\mathcal{N}(A + I)$; take $\boldsymbol{p}_1 = (4, 3, -2)^{\mathsf T}$. Solving $(A + I)\boldsymbol{x} = \boldsymbol{p}_1$ gives $\boldsymbol{p}_2 = (1, 0, 0)^{\mathsf T}$. Finally take $\boldsymbol{p}_3 = (0, 1, 0)^{\mathsf T}$ in $\mathcal{N}(A + I)$, independent of $\boldsymbol{p}_1$. Then $P = (\boldsymbol{p}_1, \boldsymbol{p}_2, \boldsymbol{p}_3)$ satisfies $P^{-1}AP = J$.

**Example 10.10.2** Find the Jordan form and a Jordan basis of $A = \begin{bmatrix} 1 & 1 & 1 & 1 & 1 & 1 \\ 0 & 2 & 0 & 1 & 2 & 3 \\ 0 & 0 & 2 & 0 & 1 & -1 \\ 0 & 0 & 0 & 2 & 1 & 2 \\ 0 & 0 & 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 0 & 0 & 2 \end{bmatrix}$.

1. $\det(\lambda I_6 - A) = (\lambda - 1)(\lambda - 2)^5$.
2. Let $N = A - 2I$. Then $\operatorname{rank}(N) = 4$, $\operatorname{rank}(N^2) = 2$ and $\operatorname{rank}(N^3) = 1 = 6 - 5$, where we stop. The numbers of blocks for $2$ of order $\ge 1, \ge 2, \ge 3$ are $6 - 4 = 2$, $4 - 2 = 2$ and $2 - 1 = 1$: one block of order $3$ and one of order $2$, so $J = \operatorname{diag}(1, J_{2,3}, J_{2,2})$.
3. For $\mu = 1$: $\boldsymbol{p}_1 = \boldsymbol{e}_1$. For $\mu = 2$, level $3$: take $\boldsymbol{y} = (-2, 0, 0, 0, 1, 0)^{\mathsf T} \in N_3 \setminus N_2$, with chain $N^2\boldsymbol{y} = (1, 1, 0, 0, 0, 0)^{\mathsf T}$, $N\boldsymbol{y} = (3, 2, 1, 1, 0, 0)^{\mathsf T}$, $\boldsymbol{y}$. Level $2$: $N_2$ is spanned by $N_1 = \operatorname{span}\{(1,1,0,0,0,0)^{\mathsf T}, (1,0,1,0,0,0)^{\mathsf T}\}$ together with $\boldsymbol{e}_4$ and $(3, 0, 0, 0, -2, 1)^{\mathsf T}$. The vector $\boldsymbol{e}_4$ must not be chosen: $\boldsymbol{e}_4 = N\boldsymbol{y} - 2(1,1,0,0,0,0)^{\mathsf T} - (1,0,1,0,0,0)^{\mathsf T}$ lies in $N_1 + \operatorname{span}\{N\boldsymbol{y}\}$, and the bottom of its chain, $N\boldsymbol{e}_4 = N^2\boldsymbol{y}$, coincides with that of the first chain. Take $\boldsymbol{z} = (3, 0, 0, 0, -2, 1)^{\mathsf T}$ instead, with chain $N\boldsymbol{z} = (-4, -1, -3, 0, 0, 0)^{\mathsf T}$, $\boldsymbol{z}$.
4. $P = (\boldsymbol{e}_1, N^2\boldsymbol{y}, N\boldsymbol{y}, \boldsymbol{y}, N\boldsymbol{z}, \boldsymbol{z}) = \begin{bmatrix} 1 & 1 & 3 & -2 & -4 & 3 \\ 0 & 1 & 2 & 0 & -1 & 0 \\ 0 & 0 & 1 & 0 & -3 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & -2 \\ 0 & 0 & 0 & 0 & 0 & 1 \end{bmatrix}$, $\det P = -3 \ne 0$, and $P^{-1}AP = J$.

The Jordan form is the simplest form in theory, but it is unsuitable for floating-point computation: it is not a continuous function of the matrix entries. The code below changes one entry of $J_{0,10}$ by $10^{-10}$; the eigenvalues then jump from all being $0$ to ten distinct numbers of modulus $(10^{-10})^{1/10} = 0.1$, and the Jordan form changes from a single block of order $10$ to a diagonal matrix.

```python
import numpy as np

n, eps = 10, 1e-10
J = np.diag(np.ones(n - 1), k=1)       # nilpotent Jordan block J_{0,10}
Jp = J.copy()
Jp[-1, 0] = eps                         # perturb a single entry by 1e-10
print(np.abs(np.linalg.eigvals(J)).max())    # 0.0
print(np.abs(np.linalg.eigvals(Jp)))         # all about eps**(1/n) = 0.1
```

In general, when the lower left entry of $J_{0,k}$ is perturbed to $\varepsilon$, the characteristic polynomial becomes $\lambda^k - \varepsilon$, whose roots are the $k$ complex $k$-th roots of $\varepsilon$; the eigenvalues move by $\varepsilon^{1/k}$, and the larger the block, the more sensitive they are. For a normal matrix $A$ ([Chapter 12](/2.1.12)), by contrast, every eigenvalue of $A + E$ lies within $\|E\|_2$ of some eigenvalue of $A$ (the Bauer–Fike theorem).

![Left: after the lower left entry of the nilpotent Jordan block of order 10 is changed to ε, the eigenvalues jump from 0 to the circle of radius equal to the tenth root of ε; the three values of ε give radii 0.1, 0.25 and 0.5. Right: the eigenvalue change ε^(1/k) for a Jordan block of order k compared with the bound ε for a normal matrix (logarithmic axes)](./plots/jordan-perturbation.py)

For this reason numerical software computes the Schur form (the unitary triangularization of [Chapter 12](/2.1.12)); the Jordan form is used mainly in theoretical arguments, exact computations and the matrix functions of the [next chapter](/2.1.11).

## Summary

| Object | Content | How to compute |
|---|---|---|
| Direct sum | Definition 10.1.1; four equivalent conditions (Theorem 10.1.1) | Compare dimensions, or check that the union of bases is linearly independent |
| Invariant subspace | Definition 10.2.1; invariant subspace $\Leftrightarrow$ block upper triangular form, invariant complement $\Leftrightarrow$ block diagonal form (Theorem 10.2.1) | Kernels, images, eigenspaces and generalized eigenspaces are invariant |
| Schur's theorem | Every complex square matrix is similar to an upper triangular matrix (Theorem 10.3.1) | Algorithm 10.3.1: take an eigenvector, extend, recurse on the lower right block |
| Generalized eigenspace | $G_\mu = \mathcal{N}\left((A - \mu I)^{n_\mu}\right)$, $\dim G_\mu$ = algebraic multiplicity | Rank sequence $\operatorname{rank}\left((A - \mu I)^k\right)$ |
| Generalized eigenspace decomposition | $\mathbb{C}^n = \bigoplus G_{\mu_i}$; $A$ is similar to a block diagonal matrix whose blocks each have a single eigenvalue (Theorems 10.5.1, 10.5.2) | Concatenate bases of the $\mathcal{N}\left((A - \mu_iI)^{n_i}\right)$ into $P$ |
| Minimal polynomial | $m_A = \prod (x - \mu_i)^{m_i}$, $m_i$ = order of the largest block; diagonalizable $\Leftrightarrow$ no multiple roots (Property 10.6.1) | Index at which the rank sequence stops decreasing |
| Nilpotent transformation | Cyclic decomposition (Theorem 10.8.1); number of blocks $= \dim\mathcal{N}(T)$, largest block = index of nilpotency | Induction on $\mathcal{R}(T)$ |
| Jordan form | Exists and is unique (Theorem 10.9.2); block counting formulas (Theorem 10.9.3); similar $\Leftrightarrow$ same rank sequences | Ranks only |
| Jordan basis | Consists of Jordan chains | Algorithm 10.10.1: choose chain tops top-down, ensuring independence |

The chapter breaks "the simplest form up to similarity" into three standard problems: finding polynomial roots, computing ranks and solving linear systems. Only root finding needs numerical iteration; the block structure is determined entirely by finitely many eliminations. The numerical instability of the Jordan form shows, in turn, that the simplest form in theory need not be a good form for computation; the latter is usually the Schur form obtained by unitary transformations.
