---
title: Subspaces, Dimension and Rank
source_hash: bebaf87a8777
---

The solvability criterion of [Chapter 1](/2.1.1) tells us whether a linear system has a solution and whether the solution is unique, but not what the solution set looks like when the solution is not unique. This chapter looks at $A\boldsymbol{x} = \boldsymbol{b}$ from the column point of view: the system is solvable exactly when $\boldsymbol{b}$ is a linear combination of the columns of $A$. Around the notion of linear combination we raise four questions in turn. Which vectors can a given set of vectors produce (subspaces and spans)? Is the representation unique (linear independence)? Which vectors are essential (maximal linearly independent subsets and bases)? Which quantity stays unchanged under transformations (rank and dimension)? Once these are answered, the rank of a matrix unifies the results of the previous two chapters: the solution set is a particular solution plus the null space, the null space has dimension $n - \operatorname{rank}(A)$, and the dimensions of the four fundamental subspaces are completely determined by the rank.

This chapter works only in $\mathbb{R}^m$; [Chapter 8](/2.1.8) extends these notions to general vector spaces, with essentially the same proofs. The orthogonality relations among the four fundamental subspaces are discussed in [Chapter 4](/2.1.4).

## 3.1. Images and Preimages under a Linear Map

A matrix $A$ determines the linear map $T_A\colon \mathbb{R}^n \to \mathbb{R}^m$, $\boldsymbol{x} \mapsto A\boldsymbol{x}$. Existence and uniqueness of solutions of $A\boldsymbol{x} = \boldsymbol{b}$ correspond directly to properties of the images and preimages of this map.

**Proposition 3.1.1** Let $A$ be an $m \times n$ matrix.

1. $T_A$ is an **injection** if and only if the homogeneous system $A\boldsymbol{x} = \boldsymbol{0}_m$ has only the zero solution $\boldsymbol{0}_n$;
2. $T_A$ is a **surjection** if and only if the system $A\boldsymbol{x} = \boldsymbol{b}$ is solvable for every $\boldsymbol{b} \in \mathbb{R}^m$.

**Proof** Statement 1: $T_A$ is injective if $A\boldsymbol{x}_1 = A\boldsymbol{x}_2$ implies $\boldsymbol{x}_1 = \boldsymbol{x}_2$, that is, if $A(\boldsymbol{x}_1 - \boldsymbol{x}_2) = \boldsymbol{0}$ implies $\boldsymbol{x}_1 - \boldsymbol{x}_2 = \boldsymbol{0}$. Statement 2 is the definition of a surjection. $\square$

Thus, to decide whether a linear map is injective, it suffices to check whether the preimage of the zero vector is unique. This leads to two sets:

$$
\mathcal{R}(A) = \{A\boldsymbol{x} \mid \boldsymbol{x} \in \mathbb{R}^n\} \subseteq \mathbb{R}^m, \qquad \mathcal{N}(A) = \{\boldsymbol{x} \in \mathbb{R}^n \mid A\boldsymbol{x} = \boldsymbol{0}\} \subseteq \mathbb{R}^n.
$$

$\mathcal{R}(A)$ is the **range** of $T_A$, that is, the set of all linear combinations of the columns of $A$; $\mathcal{N}(A)$ is the solution set of the homogeneous system $A\boldsymbol{x} = \boldsymbol{0}$. Always $\boldsymbol{0}_m \in \mathcal{R}(A)$ and $\boldsymbol{0}_n \in \mathcal{N}(A)$; the system $A\boldsymbol{x} = \boldsymbol{b}$ is solvable if and only if $\boldsymbol{b} \in \mathcal{R}(A)$.

**Proposition 3.1.2** Let $A$ be an $m \times n$ matrix. Then $T_A$ is surjective if and only if $\mathcal{R}(A) = \mathbb{R}^m$, and $T_A$ is injective if and only if $\mathcal{N}(A) = \{\boldsymbol{0}\}$.

**Example 3.1.1** For $A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$,

$$
\mathcal{R}(A) = \left\{ x_1\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + x_2\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} + x_3\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} \right\} = \left\{ \begin{bmatrix} x_1 \\ x_2 \\ 0 \end{bmatrix} \;\middle|\; x_1, x_2 \in \mathbb{R} \right\}, \qquad
\mathcal{N}(A) = \left\{ k\begin{bmatrix} -1 \\ -1 \\ 1 \end{bmatrix} \;\middle|\; k \in \mathbb{R} \right\}.
$$

$T_A$ is neither injective nor surjective. Both sets are closed under the linear operations, which leads to the notion of a subspace; and every vector in them is a linear combination of finitely many vectors, which leads to the notion of a basis.

## 3.2. Subspaces

**Definition 3.2.1 (Subspace)** Let $M$ be a nonempty subset of $\mathbb{R}^m$. If $M$ is closed under addition and scalar multiplication, that is, $\boldsymbol{a} + \boldsymbol{b} \in M$ and $k\boldsymbol{a} \in M$ for all $\boldsymbol{a}, \boldsymbol{b} \in M$ and $k \in \mathbb{R}$, then $M$ is called a (linear) **subspace** of $\mathbb{R}^m$.

The two conditions can be combined into: $k\boldsymbol{a} + \ell\boldsymbol{b} \in M$ for all $\boldsymbol{a}, \boldsymbol{b} \in M$ and $k, \ell \in \mathbb{R}$. Taking $k = 0$ shows that every subspace contains the zero vector. $\{\boldsymbol{0}\}$ and $\mathbb{R}^m$ are subspaces of $\mathbb{R}^m$, called the trivial subspaces; all others are nontrivial subspaces.

**Example 3.2.1** None of the following sets is a subspace: the first quadrant of $\mathbb{R}^2$ (not closed under scalar multiplication); the union of the $x_1$-axis and the $x_2$-axis in $\mathbb{R}^2$ (not closed under addition); the plane $x_1 + x_2 + x_3 = 1$ in $\mathbb{R}^3$ (it does not contain the zero vector); the cone $x_1^2 + x_2^2 = x_3^2$ in $\mathbb{R}^3$ (not closed under addition). The nontrivial subspaces of $\mathbb{R}^2$ are exactly the lines through the origin, and the nontrivial subspaces of $\mathbb{R}^3$ are exactly the lines and planes through the origin (as follows from the dimension theory of Section 3.6).

**Definition 3.2.2 (Column Space and Null Space)** For an $m \times n$ matrix $A$, $\mathcal{R}(A)$ is called the **column space** of $A$ and $\mathcal{N}(A)$ the **null space** of $A$ (also the solution space of $A\boldsymbol{x} = \boldsymbol{0}$).

**Proposition 3.2.1** $\mathcal{R}(A)$ is a subspace of $\mathbb{R}^m$, and $\mathcal{N}(A)$ is a subspace of $\mathbb{R}^n$.

**Proof** For $\boldsymbol{b}_1 = A\boldsymbol{x}_1$ and $\boldsymbol{b}_2 = A\boldsymbol{x}_2 \in \mathcal{R}(A)$, $k_1\boldsymbol{b}_1 + k_2\boldsymbol{b}_2 = A(k_1\boldsymbol{x}_1 + k_2\boldsymbol{x}_2) \in \mathcal{R}(A)$. For $\boldsymbol{x}_1, \boldsymbol{x}_2 \in \mathcal{N}(A)$, $A(k_1\boldsymbol{x}_1 + k_2\boldsymbol{x}_2) = k_1A\boldsymbol{x}_1 + k_2A\boldsymbol{x}_2 = \boldsymbol{0}$. $\square$

The solution set of a nonhomogeneous system $A\boldsymbol{x} = \boldsymbol{b}$ ($\boldsymbol{b} \ne \boldsymbol{0}$) does not contain the zero vector and is not a subspace.

## 3.3. Span and Linear Dependence

**Definition 3.3.1 (Span)** Let $S: \boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ be a list of vectors in $\mathbb{R}^m$. The set of all its linear combinations,

$$
\operatorname{span}(S) = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n) = \{k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n \mid k_1, \dots, k_n \in \mathbb{R}\},
$$

is called the **span** of $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ (the set spanned by them), and $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ are called a spanning set for it.

**Proposition 3.3.1** $\operatorname{span}(S)$ is a subspace of $\mathbb{R}^m$; if all vectors of $S$ belong to some subspace $M$, then $\operatorname{span}(S) \subseteq M$.

Hence $\operatorname{span}(S)$ is the smallest subspace containing $S$. For $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$, $\mathcal{R}(A) = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n)$.

**Definition 3.3.2 (Linear Dependence and Linear Independence)** Let $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ be vectors in $\mathbb{R}^m$. If there are numbers $k_1, \dots, k_n$, not all zero, such that $k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n = \boldsymbol{0}$, then the vectors are said to be **linearly dependent**; otherwise, that is, if $k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n = \boldsymbol{0}$ always implies $k_1 = \cdots = k_n = 0$, they are said to be **linearly independent**.

With $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$,

$$
\boldsymbol{a}_1, \dots, \boldsymbol{a}_n\ \text{linearly independent} \iff \text{the representation of } \boldsymbol{0} \text{ is unique} \iff A\boldsymbol{x} = \boldsymbol{0}\ \text{has only the zero solution} \iff \mathcal{N}(A) = \{\boldsymbol{0}\},
$$

and linear dependence is equivalent to $A\boldsymbol{x} = \boldsymbol{0}$ having a nonzero solution. Directly from the definition: a list containing the zero vector is linearly dependent; every sublist of a linearly independent list is linearly independent; and every extension of a linearly dependent list is linearly dependent.

**Example 3.3.1** Let $A = [\boldsymbol{a}\ \boldsymbol{b}]$ with $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^2$.

1. If $\boldsymbol{a}, \boldsymbol{b}$ are linearly independent (not collinear), then $\mathcal{R}(A) = \mathbb{R}^2$, $\mathcal{N}(A) = \{\boldsymbol{0}\}$, and $A$ is invertible.
2. If $\boldsymbol{a}, \boldsymbol{b}$ are linearly dependent but not both zero, say $\boldsymbol{a} \ne \boldsymbol{0}$ and $\boldsymbol{b} = k\boldsymbol{a}$, then $\mathcal{R}(A) = \operatorname{span}(\boldsymbol{a})$ and $\mathcal{N}(A) = \operatorname{span}([k\ \ {-1}]^{\mathsf T})$, both lines through the origin.
3. If $\boldsymbol{a} = \boldsymbol{b} = \boldsymbol{0}$, then $\mathcal{R}(A) = \{\boldsymbol{0}\}$ and $\mathcal{N}(A) = \mathbb{R}^2$.

In all three cases the "dimensions" of $\mathcal{R}(A)$ and $\mathcal{N}(A)$ add up to $2$, a special case of Theorem 3.11.1.

**Proposition 3.3.2** In $\mathbb{R}^m$, if $n > m$, then any $n$ vectors are linearly dependent.

**Proof** Let $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$. The homogeneous system $A\boldsymbol{x} = \boldsymbol{0}$ has $m$ equations and $n > m$ unknowns, so it has a nonzero solution by Corollary 1.8.2. $\square$

**Proposition 3.3.3** Suppose $\boldsymbol{b}$ is a linear combination of $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$. Then the representation is unique if and only if $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ are linearly independent.

**Proof** Let $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ and $A\boldsymbol{x}_0 = \boldsymbol{b}$. If the vectors are linearly dependent, there is $\boldsymbol{y} \ne \boldsymbol{0}$ with $A\boldsymbol{y} = \boldsymbol{0}$, and $A(\boldsymbol{x}_0 + \boldsymbol{y}) = \boldsymbol{b}$ is another representation. Conversely, if $A\boldsymbol{x}_0 = A\boldsymbol{x}_1 = \boldsymbol{b}$ with $\boldsymbol{x}_0 \ne \boldsymbol{x}_1$, then $A(\boldsymbol{x}_0 - \boldsymbol{x}_1) = \boldsymbol{0}$ shows that the vectors are linearly dependent. $\square$

**Proposition 3.3.4** Let $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ be linearly independent. Then for every vector $\boldsymbol{b}$:

1. $\boldsymbol{b}$ is a linear combination of $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ if and only if $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n, \boldsymbol{b}$ are linearly dependent;
2. $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n, \boldsymbol{b}$ are linearly independent if and only if $\boldsymbol{b}$ is not a linear combination of $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$.

**Proof** Statement 2 is the contrapositive of statement 1. If $\boldsymbol{b} = \sum k_i\boldsymbol{a}_i$, then $\sum k_i\boldsymbol{a}_i - \boldsymbol{b} = \boldsymbol{0}$ is a linear relation whose coefficients are not all zero (the coefficient of $\boldsymbol{b}$ is $-1$). Conversely, suppose $\sum k_i\boldsymbol{a}_i + k\boldsymbol{b} = \boldsymbol{0}$ with coefficients not all zero. If $k = 0$, this contradicts the linear independence of $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$; so $k \ne 0$ and $\boldsymbol{b} = -\sum (k_i/k)\boldsymbol{a}_i$. $\square$

The proposition says that adding to a linearly independent list a vector that it cannot represent yields again a linearly independent list. This is the key to the sifting method and to the basis extension theorem below.

## 3.4. Bases of Subspaces

**Definition 3.4.1 (Basis)** Let $M$ be a subspace of $\mathbb{R}^m$. If vectors $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ in $M$ satisfy (1) $M = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n)$, that is, every vector of $M$ is a linear combination of them, and (2) $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ are linearly independent, then $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ are called a **basis** of $M$.

By Proposition 3.3.3, condition (2) can be replaced by "every vector of $M$ has a unique representation"; by Proposition 3.3.2, a basis of a subspace of $\mathbb{R}^m$ cannot contain more than $m$ vectors.

**Proposition 3.4.1** Let $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_m]$ be a square matrix of order $m$. Then $\boldsymbol{a}_1, \dots, \boldsymbol{a}_m$ form a basis of $\mathbb{R}^m$ if and only if $A$ is invertible.

**Proof** If they form a basis, they are linearly independent, so $A\boldsymbol{x} = \boldsymbol{0}$ has only the zero solution and $A$ is invertible by Theorem 2.3.1. Conversely, if $A$ is invertible, then $A\boldsymbol{x} = \boldsymbol{0}$ has only the zero solution (linear independence), and $A\boldsymbol{x} = \boldsymbol{b}$ is solvable for every $\boldsymbol{b}$ (they span $\mathbb{R}^m$). $\square$

**Definition 3.4.2 (Standard Basis)** By Proposition 3.4.1 (with $A = I_m$), the standard coordinate vectors $\boldsymbol{e}_1, \dots, \boldsymbol{e}_m$ form a basis of $\mathbb{R}^m$, called the **standard basis** of $\mathbb{R}^m$.

## 3.5. Maximal Linearly Independent Subsets and the Rank of a List of Vectors

Does every subspace of $\mathbb{R}^m$ have a basis, and how do we find one? Consider first $\operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n)$, that is, the column space $\mathcal{R}(A)$: a basis can be picked out from the spanning vectors.

**Definition 3.5.1 (Linear Representation of One List by Another)** Let $S$ and $T$ be two lists of vectors in $\mathbb{R}^m$. If every vector of $S$ is a linear combination of the vectors of $T$, we say that $S$ can be linearly represented by $T$.

**Definition 3.5.2 (Maximal Linearly Independent Subset)** Let $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ be a sublist of $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$. If (1) $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ are linearly independent and (2) $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ can be linearly represented by $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$, then $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ is called a **maximal linearly independent subset** of $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$.

By definition, a maximal linearly independent subset is precisely a basis of $\operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n)$.

**Algorithm 3.5.1 (Sifting Method)** Input: vectors $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$, not all zero. Examine $\boldsymbol{a}_1, \boldsymbol{a}_2, \dots$ in turn: if the current vector is not a linear combination of the vectors already selected (for the first nonzero vector, this means it is nonzero), select it; otherwise discard it. Output the selected sublist.

By Proposition 3.3.4, the selected vectors are linearly independent at every step; every discarded vector is a linear combination of vectors already selected, so all the vectors can be represented by the output sublist. Hence:

**Proposition 3.5.1** Every finite list of vectors, not all zero, has a maximal linearly independent subset, and the sifting method produces one.

**Example 3.5.1** Take $\boldsymbol{a}_1 = [1\ {-1}\ 0]^{\mathsf T}$, $\boldsymbol{a}_2 = [1\ 0\ {-1}]^{\mathsf T}$, $\boldsymbol{a}_3 = [0\ 1\ {-1}]^{\mathsf T}$: $\boldsymbol{a}_1 \ne \boldsymbol{0}$ is selected; $\boldsymbol{a}_2$ is not a multiple of $\boldsymbol{a}_1$ and is selected; $\boldsymbol{a}_3 = -\boldsymbol{a}_1 + \boldsymbol{a}_2$ is discarded. So $\boldsymbol{a}_1, \boldsymbol{a}_2$ is a maximal linearly independent subset. In fact any two of these vectors form a maximal linearly independent subset, so maximal linearly independent subsets are in general not unique.

The sifting method must decide a linear representation, that is, solve a system, at every step; Section 3.7 gives a method that needs only one elimination. To compare different maximal linearly independent subsets, we first discuss linear representations between lists of vectors.

**Proposition 3.5.2** Let $S: \boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ and $T: \boldsymbol{b}_1, \dots, \boldsymbol{b}_p$ be lists of vectors in $\mathbb{R}^m$. The following are equivalent:

1. $S$ can be linearly represented by $T$;
2. there is a $p \times n$ matrix $U$ such that $[\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n] = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_p]\,U$;
3. $\operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n) \subseteq \operatorname{span}(\boldsymbol{b}_1, \dots, \boldsymbol{b}_p)$.

**Proof** $1 \Rightarrow 2$: write $\boldsymbol{a}_j = u_{1j}\boldsymbol{b}_1 + \cdots + u_{pj}\boldsymbol{b}_p = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_p][u_{1j}\ \cdots\ u_{pj}]^{\mathsf T}$ and let $U = [u_{ij}]_{p \times n}$. $2 \Rightarrow 3$: every $\boldsymbol{c} \in \operatorname{span}(S)$ can be written as $\boldsymbol{c} = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]\boldsymbol{x} = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_p](U\boldsymbol{x}) \in \operatorname{span}(T)$. $3 \Rightarrow 1$: obvious. $\square$

**Proposition 3.5.3 (Transitivity)** If a list $S$ can be linearly represented by $T$, and $T$ by $R$, then $S$ can be linearly represented by $R$.

**Proof** Let $A, B, C$ be the matrices whose columns are the three lists. By Proposition 3.5.2 there are $U, V$ with $A = BU$ and $B = CV$, so $A = C(VU)$. $\square$

**Proposition 3.5.4** Suppose $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ can be linearly represented by $\boldsymbol{b}_1, \dots, \boldsymbol{b}_p$.

1. If $n > p$, then $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ are linearly dependent;
2. if $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ are linearly independent, then $n \le p$.

**Proof** Statement 2 is the contrapositive of statement 1. Let $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ and $B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_p]$; then $A = BC$ for a $p \times n$ matrix $C$. When $n > p$, the system $C\boldsymbol{x} = \boldsymbol{0}$ has more unknowns than equations and hence a nonzero solution $\boldsymbol{k}$, and $A\boldsymbol{k} = BC\boldsymbol{k} = \boldsymbol{0}$. $\square$

Intuitively, a linearly dependent list contains "redundant" vectors as far as spanning is concerned: when $n$ vectors are linearly dependent, their maximal linearly independent subsets contain fewer than $n$ vectors.

**Definition 3.5.3 (Linear Equivalence)** Two lists of vectors are said to be linearly equivalent if each can be linearly represented by the other. If a list is linearly equivalent to a single vector, the vectors of the list are said to be collinear.

**Example 3.5.2** Let $\boldsymbol{u} \in \mathbb{R}^m$ and $\boldsymbol{v} \in \mathbb{R}^n$ be nonzero vectors. Then

$$
\boldsymbol{u}\boldsymbol{v}^{\mathsf T} = [v_1\boldsymbol{u}\ \ v_2\boldsymbol{u}\ \cdots\ v_n\boldsymbol{u}] = \begin{bmatrix} u_1\boldsymbol{v}^{\mathsf T} \\ \vdots \\ u_m\boldsymbol{v}^{\mathsf T} \end{bmatrix};
$$

its columns are collinear with $\boldsymbol{u}$, and its rows (after transposition) are collinear with $\boldsymbol{v}$.

**Proposition 3.5.5** Linear equivalence of lists of vectors is an **equivalence relation**; two lists $S, T$ are linearly equivalent if and only if $\operatorname{span}(S) = \operatorname{span}(T)$.

**Proof** Reflexivity and symmetry follow from the definition, and transitivity is Proposition 3.5.3. The second statement follows from $1 \Leftrightarrow 3$ in Proposition 3.5.2. $\square$

The span is an invariant of this equivalence relation. A list is linearly equivalent to each of its maximal linearly independent subsets, so any two maximal linearly independent subsets are linearly equivalent to each other.

**Proposition 3.5.6** If linearly independent lists $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ and $\boldsymbol{b}_1, \dots, \boldsymbol{b}_p$ are linearly equivalent, then $n = p$.

**Proof** Apply statement 2 of Proposition 3.5.4 in both directions to get $n \le p$ and $p \le n$. $\square$

Therefore any two maximal linearly independent subsets of a list contain the same number of vectors.

**Definition 3.5.4 (Rank of a List of Vectors)** The number of vectors in any maximal linearly independent subset of a list $S$ is called the **rank** of $S$, denoted by $\operatorname{rank}(S)$. The rank of a list consisting only of zero vectors is defined to be zero.

The rank of a list of vectors is also an invariant of linear equivalence.

## 3.6. Existence and Extension of Bases, and Dimension

The sifting method picks a basis out of a spanning set. For a general subspace we can instead add vectors one at a time.

**Theorem 3.6.1 (Existence of Bases)** Let $M$ be a subspace of $\mathbb{R}^m$ with $M \ne \{\boldsymbol{0}\}$. Then $M$ has a basis, and the number of vectors in it is at most $m$.

**Proof** Take any nonzero vector $\boldsymbol{a}_1 \in M$. If $M = \operatorname{span}(\boldsymbol{a}_1)$, then $\boldsymbol{a}_1$ is a basis; otherwise take $\boldsymbol{a}_2 \in M \setminus \operatorname{span}(\boldsymbol{a}_1)$, and by Proposition 3.3.4, $\boldsymbol{a}_1, \boldsymbol{a}_2$ are linearly independent. If $M = \operatorname{span}(\boldsymbol{a}_1, \boldsymbol{a}_2)$, we have a basis; otherwise take $\boldsymbol{a}_3 \in M \setminus \operatorname{span}(\boldsymbol{a}_1, \boldsymbol{a}_2)$, and so on. The list obtained at every step is linearly independent, so by Proposition 3.3.2 it has at most $m$ vectors; the process therefore stops after at most $m$ steps, producing linearly independent $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ ($r \le m$) with $M = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$. $\square$

Hence every subspace of $\mathbb{R}^m$ is spanned by finitely many vectors and is the column space of some matrix: $M = \mathcal{R}([\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_r])$, and $\{\boldsymbol{0}\} = \mathcal{R}(O)$. Any two bases of $M$ are linearly equivalent and both linearly independent, so by Proposition 3.5.6 they contain the same number of vectors.

**Theorem 3.6.2 (Basis Extension Theorem)** Let $M, N$ be subspaces of $\mathbb{R}^m$ with $M \ne \{\boldsymbol{0}\}$ and $M \subseteq N$. Then every basis of $M$ can be extended to a basis of $N$. In particular, every basis of a subspace of $\mathbb{R}^m$ can be extended to a basis of $\mathbb{R}^m$.

**Proof** Let $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ be a basis of $M$. If $N = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$, it is also a basis of $N$; otherwise take $\boldsymbol{a}_{r+1} \in N \setminus \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$, and by Proposition 3.3.4 the extended list is linearly independent. Continuing as in the proof of Theorem 3.6.1, we obtain a basis of $N$ after finitely many steps. $\square$

Note the direction: one must start from a basis of $M$ in order to extend it; a basis of $N$ chosen first is in general unrelated to $M$ (none of its vectors need lie in $M$).

**Definition 3.6.1 (Dimension)** The number of vectors in any basis of a subspace $M$ is called the **dimension** of $M$, denoted by $\dim M$. We define $\dim\{\boldsymbol{0}\} = 0$. A subspace of dimension $r$ is called an $r$-dimensional subspace.

**Proposition 3.6.1**

1. $\dim\mathbb{R}^m = m$;
2. if $M$ is a subspace of $\mathbb{R}^m$, then $\dim M \le m$;
3. if $M \subseteq N$ are subspaces of $\mathbb{R}^m$, then $\dim M \le \dim N$; if moreover $\dim M = \dim N$, then $M = N$.

**Proof** Statement 1 follows from the standard basis, and statement 2 from Theorem 3.6.1. Statement 3: extending a basis of $M$ to a basis of $N$ (Theorem 3.6.2) gives $\dim M \le \dim N$; when the dimensions are equal, no vector needs to be added, so the basis of $M$ already spans $N$ and $M = N$. (The case $M = \{\boldsymbol{0}\}$ is trivial.) $\square$

The converse of statement 3 is false: $\dim M \le \dim N$ does not imply $M \subseteq N$, as two different lines through the origin in $\mathbb{R}^2$ show.

When the dimension is known, one condition fewer needs to be checked to decide whether a list of vectors is a basis.

**Proposition 3.6.2 (Criterion for a Basis)** Let $M$ be an $r$-dimensional subspace of $\mathbb{R}^m$ and $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ be $r$ vectors in $M$.

1. If $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ are linearly independent, they form a basis of $M$;
2. if $M = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$, they form a basis of $M$.

In general, of the three conditions (i) $\dim M = r$, (ii) the vectors $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ in $M$ are linearly independent and (iii) $M = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$, any two imply the third.

**Proof** 1. $\operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r) \subseteq M$, and both have dimension $r$, so they are equal by Proposition 3.6.1. 2. If $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ were linearly dependent, then $\dim M = \operatorname{rank}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r) < r$, a contradiction. Finally, (ii) and (iii) together are the definition of a basis, which implies (i). $\square$

## 3.7. The Rank of a Matrix and Bases of the Column Space

**Definition 3.7.1 (Rank of a Matrix)** The dimension $\dim\mathcal{R}(A)$ of the column space of a matrix $A$ is called the **rank** of $A$, denoted by $\operatorname{rank}(A)$.

$\operatorname{rank}(A)$ is the rank of the list of columns of $A$. Finding a maximal linearly independent subset of the columns by the sifting method requires deciding linear relations many times. Observe, however, that the linear relations among the columns are exactly the solutions of $A\boldsymbol{x} = \boldsymbol{0}$, and the solution set is an invariant of row equivalence (Section 2.4); hence elementary row operations do not change the linear relations among the columns.

**Proposition 3.7.1** Let $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ and $B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_n]$ be row equivalent. Then

1. a sublist $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ is linearly independent if and only if the corresponding sublist $\boldsymbol{b}_{i_1}, \dots, \boldsymbol{b}_{i_r}$ is linearly independent;
2. $\boldsymbol{a}_j = k_1\boldsymbol{a}_{i_1} + \cdots + k_r\boldsymbol{a}_{i_r}$ if and only if $\boldsymbol{b}_j = k_1\boldsymbol{b}_{i_1} + \cdots + k_r\boldsymbol{b}_{i_r}$ (with the same coefficients);
3. $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ is a maximal linearly independent subset of the columns of $A$ if and only if $\boldsymbol{b}_{i_1}, \dots, \boldsymbol{b}_{i_r}$ is a maximal linearly independent subset of the columns of $B$.

**Proof** By Proposition 2.4.1 there is an invertible matrix $P$ with $B = PA$, that is, $\boldsymbol{b}_j = P\boldsymbol{a}_j$. Let $A_1 = [\boldsymbol{a}_{i_1}\ \cdots\ \boldsymbol{a}_{i_r}]$ and $B_1 = PA_1$. 1. $A_1\boldsymbol{x} = \boldsymbol{0}$ if and only if $PA_1\boldsymbol{x} = \boldsymbol{0}$. 2. If $\boldsymbol{a}_j = A_1\boldsymbol{k}$, then $\boldsymbol{b}_j = PA_1\boldsymbol{k} = B_1\boldsymbol{k}$; for the converse multiply on the left by $P^{-1}$. 3. Follows from the first two statements. $\square$

**Theorem 3.7.1** Reduce $A$ to row echelon form (or reduced row echelon form). Then

1. the columns of $A$ corresponding to the pivot columns form a maximal linearly independent subset of the columns of $A$, that is, a basis of $\mathcal{R}(A)$, and $\operatorname{rank}(A)$ equals the number of pivots;
2. the coefficients expressing each free column of $A$ in this basis are the first $r$ entries of the corresponding column of the reduced row echelon form.

**Proof** Let $R = \operatorname{rref}(A)$ have $r$ pivots. Then the pivot columns of $R$ are $\boldsymbol{e}_1, \dots, \boldsymbol{e}_r$ in order, which are linearly independent; since the last $m - r$ rows of $R$ are zero, each free column is $[c_1\ \cdots\ c_r\ 0\ \cdots\ 0]^{\mathsf T} = c_1\boldsymbol{e}_1 + \cdots + c_r\boldsymbol{e}_r$. So the pivot columns of $R$ form a maximal linearly independent subset of the columns of $R$. By Proposition 3.7.1 these conclusions hold for the corresponding columns of $A$. A row echelon form and the reduced row echelon form have their pivot columns in the same positions. $\square$

**Corollary 3.7.1** The reduced row echelon form of a matrix is unique.

**Proof** Let $R, R'$ both be reduced row echelon forms of $A$. Then $R$ and $R'$ are row equivalent, so by Proposition 3.7.1 their columns satisfy the same linear relations. In a reduced row echelon form, column $j$ is a pivot column if and only if it is not a linear combination of the preceding columns (a pivot column is a new $\boldsymbol{e}_k$, while the preceding columns all lie in $\operatorname{span}(\boldsymbol{e}_1, \dots, \boldsymbol{e}_{k-1})$; a free column is a combination of the preceding pivot columns). So $R$ and $R'$ have their pivot columns in the same positions, and these columns are $\boldsymbol{e}_1, \dots, \boldsymbol{e}_r$ in order in both. Each free column has a unique representation in terms of the pivot columns (Proposition 3.3.3), and its entries are exactly the coefficients, which are the same in $R$ and $R'$. Hence $R = R'$. $\square$

Thus the normal form under row equivalence (Section 2.4) is unique, and two $m \times n$ matrices are row equivalent if and only if they have the same reduced row echelon form.

**Algorithm 3.7.1 (Maximal Linearly Independent Subset of the Columns)** Input: $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$.

1. Reduce $A$ to reduced row echelon form $R$ by elementary row operations (to find only the rank, a row echelon form suffices);
2. if the pivot columns are $j_1 < \cdots < j_r$, then $\boldsymbol{a}_{j_1}, \dots, \boldsymbol{a}_{j_r}$ is a maximal linearly independent subset and $\operatorname{rank}(A) = r$;
3. if column $j$ of $R$ is $[c_1\ \cdots\ c_r\ 0\ \cdots\ 0]^{\mathsf T}$, then $\boldsymbol{a}_j = c_1\boldsymbol{a}_{j_1} + \cdots + c_r\boldsymbol{a}_{j_r}$.

**Example 3.7.1** For the coefficient matrix of Example 1.8.1,

$$
A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_5] = \begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 1 & -1 & 2 & -1 & 0 \\ 4 & -2 & 6 & 3 & -4 \\ 2 & 4 & -2 & 4 & -7 \end{bmatrix}, \qquad
\operatorname{rref}(A) = \begin{bmatrix} 1 & 0 & 1 & 0 & -\frac76 \\ 0 & 1 & -1 & 0 & -\frac56 \\ 0 & 0 & 0 & 1 & -\frac13 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}.
$$

The pivot columns are columns $1, 2, 4$, so $\boldsymbol{a}_1, \boldsymbol{a}_2, \boldsymbol{a}_4$ is a maximal linearly independent subset, $\operatorname{rank}(A) = 3$, and

$$
\boldsymbol{a}_3 = \boldsymbol{a}_1 - \boldsymbol{a}_2, \qquad \boldsymbol{a}_5 = -\tfrac76\boldsymbol{a}_1 - \tfrac56\boldsymbol{a}_2 - \tfrac13\boldsymbol{a}_4.
$$

Computer algebra systems perform exact computations by the same method. In numerical computation, however, one must be careful: rounding in floating-point arithmetic turns a pivot that is "exactly zero" into a tiny nonzero number, so deciding the rank by elimination is unreliable. Numerical software uses singular values instead ([Chapter 7](/2.1.7)) together with a tolerance:

```python
import numpy as np
import sympy as sp

A = sp.Matrix([[1, 1, 0, -3, -1],
               [1, -1, 2, -1, 0],
               [4, -2, 6, 3, -4],
               [2, 4, -2, 4, -7]])
R, pivots = A.rref()           # exact Gauss-Jordan elimination
print(pivots)                  # (0, 1, 3): columns a1, a2, a4
print(A.rank())                # 3

# A perturbation of size 1e-12 makes the matrix "exactly" full rank,
# while a tolerance-based numerical rank still reports 3
B = np.array(A.tolist(), dtype=float)
B[3, 4] += 1e-12
print(np.linalg.matrix_rank(B), np.linalg.matrix_rank(B, tol=1e-8))  # 4 3
```

## 3.8. The Row Space and Full Rank

**Definition 3.8.1 (Row Space)** Let $A$ be an $m \times n$ matrix. The subspace $\mathcal{R}(A^{\mathsf T})$ of $\mathbb{R}^n$ (spanned by the transposed rows of $A$) is called the **row space** of $A$.

The rows of $A$ correspond to the equations of the system $A\boldsymbol{x} = \boldsymbol{0}$, and the dimension $\operatorname{rank}(A^{\mathsf T})$ of the row space measures the number of "effective" equations.

**Example 3.8.1** Reduce the matrix $A$ of Example 3.7.1 to a row echelon form $B$, recording which combination of the original rows each row is ($\tilde{\boldsymbol{a}}_i^{\mathsf T}$ is the $i$-th row of $A$):

$$
B = \begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 0 & -2 & 2 & 2 & 1 \\ 0 & 0 & 0 & 9 & -3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
\begin{matrix} \tilde{\boldsymbol{a}}_1^{\mathsf T} \\ \tilde{\boldsymbol{a}}_2^{\mathsf T} - \tilde{\boldsymbol{a}}_1^{\mathsf T} \\ \tilde{\boldsymbol{a}}_3^{\mathsf T} - 3\tilde{\boldsymbol{a}}_2^{\mathsf T} - \tilde{\boldsymbol{a}}_1^{\mathsf T} \\ \tilde{\boldsymbol{a}}_4^{\mathsf T} - \frac43\tilde{\boldsymbol{a}}_3^{\mathsf T} + 5\tilde{\boldsymbol{a}}_2^{\mathsf T} - \frac53\tilde{\boldsymbol{a}}_1^{\mathsf T} \end{matrix}
$$

The zero row gives $\tilde{\boldsymbol{a}}_4 = \frac53\tilde{\boldsymbol{a}}_1 - 5\tilde{\boldsymbol{a}}_2 + \frac43\tilde{\boldsymbol{a}}_3$: the fourth equation of Example 1.8.1 is "redundant".

**Proposition 3.8.1** If $A$ and $B$ are row equivalent, then $\mathcal{R}(A^{\mathsf T}) = \mathcal{R}(B^{\mathsf T})$. In particular, the nonzero rows (transposed) of a row echelon form of $A$ form a basis of $\mathcal{R}(A^{\mathsf T})$, and $\operatorname{rank}(A^{\mathsf T})$ equals the number of pivots.

**Proof** Let $B = PA$ with $P$ invertible. Then $B^{\mathsf T} = A^{\mathsf T}P^{\mathsf T}$, and Proposition 3.5.2 gives $\mathcal{R}(B^{\mathsf T}) \subseteq \mathcal{R}(A^{\mathsf T})$; the reverse inclusion follows from $A = P^{-1}B$. The nonzero rows of an echelon form span the row space, and they are linearly independent: if $\sum_i k_i\tilde{\boldsymbol{b}}_i = \boldsymbol{0}$, look at the column of the first pivot, where only row 1 is nonzero, to get $k_1 = 0$; then look at the column of the second pivot to get $k_2 = 0$, and so on. $\square$

In Example 3.8.1, the three nonzero rows of $B$ form a basis of the row space; since $\tilde{\boldsymbol{a}}_4$ is a combination of the first three rows, $\tilde{\boldsymbol{a}}_1, \tilde{\boldsymbol{a}}_2, \tilde{\boldsymbol{a}}_3$ form a basis as well. Combining this with Theorem 3.7.1 immediately gives:

**Theorem 3.8.1** For an $m \times n$ matrix $A$, $\operatorname{rank}(A^{\mathsf T}) = \operatorname{rank}(A)$, and both equal the number of pivots of a row echelon form of $A$. Consequently $\operatorname{rank}(A) \le \min\{m, n\}$.

Note that $\mathcal{R}(A) \subseteq \mathbb{R}^m$ and $\mathcal{R}(A^{\mathsf T}) \subseteq \mathbb{R}^n$ are subspaces of different spaces; they merely have the same dimension.

**Definition 3.8.2 (Full Rank)** Let $A$ be an $m \times n$ matrix. If $\operatorname{rank}(A) = n$ (the columns are linearly independent), $A$ is said to have **full column rank**; if $\operatorname{rank}(A) = m$, $A$ is said to have **full row rank**; if $\operatorname{rank}(A) = m = n$, $A$ is said to have **full rank**.

A matrix of full column rank satisfies $n \le m$ (a "tall" matrix), a matrix of full row rank satisfies $m \le n$ (a "wide" matrix), and a matrix of full rank is necessarily square; a square matrix of full row rank or of full column rank has full rank.

**Proposition 3.8.2** Let $A$ be an $m \times n$ matrix and $T_A\colon \boldsymbol{x} \mapsto A\boldsymbol{x}$. Then

1. $T_A$ is surjective if and only if $A$ has full row rank;
2. $T_A$ is injective if and only if $A$ has full column rank;
3. $T_A$ is a **bijection** if and only if $A$ has full rank.

**Proof** 1. Surjectivity means $\mathcal{R}(A) = \mathbb{R}^m$; since $\mathcal{R}(A) \subseteq \mathbb{R}^m$, by Proposition 3.6.1 this is equivalent to $\dim\mathcal{R}(A) = m$. 2. Injectivity means that $A\boldsymbol{x} = \boldsymbol{0}$ has only the zero solution, that is, the columns are linearly independent, that is, $\operatorname{rank}(A) = n$. 3. Follows from the first two. $\square$

In particular, a square matrix $A$ is invertible if and only if it has full rank, and $A = O$ if and only if $\operatorname{rank}(A) = 0$. The full-rank conditions also characterize the existence of one-sided inverses, corresponding to the **left inverse** and **right inverse** of a map ([Theorem 3.2.8 of 1.2.3](/1.2.3#thm-3.2.8)):

**Proposition 3.8.3 (One-Sided Inverses)** Let $A$ be an $m \times n$ matrix. $A$ has full column rank if and only if there is an $n \times m$ matrix $B$ with $BA = I_n$; $A$ has full row rank if and only if there is an $n \times m$ matrix $B$ with $AB = I_m$.

**Proof** If $A$ has full column rank, then $\operatorname{rref}(A) = \begin{bmatrix} I_n \\ O \end{bmatrix}$, that is, there is an invertible matrix $P$ with $PA = \begin{bmatrix} I_n \\ O \end{bmatrix}$; taking $B = [I_n\ O]P$ gives $BA = I_n$. Conversely, if $BA = I_n$, then $A\boldsymbol{x} = \boldsymbol{0}$ implies $\boldsymbol{x} = BA\boldsymbol{x} = \boldsymbol{0}$, so $A$ has full column rank. For full row rank, apply the first statement to $A^{\mathsf T}$ and use Theorem 3.8.1. $\square$

**Proposition 3.8.4 (Column Space and Rank of a Product)** Let $A$ and $B$ be $\ell \times m$ and $m \times n$ matrices respectively. Then

1. $\mathcal{R}(AB) \subseteq \mathcal{R}(A)$, and $\mathcal{R}(AB) = \mathcal{R}(A)$ if $B$ is invertible;
2. $\operatorname{rank}(AB) \le \operatorname{rank}(A)$ and $\operatorname{rank}(AB) \le \operatorname{rank}(B)$; $\operatorname{rank}(AB) = \operatorname{rank}(A)$ if $B$ is invertible, and $\operatorname{rank}(AB) = \operatorname{rank}(B)$ if $A$ is invertible.

**Proof** 1. Every column of $AB = [A\boldsymbol{b}_1\ \cdots\ A\boldsymbol{b}_n]$ lies in $\mathcal{R}(A)$. When $B$ is invertible, also $\mathcal{R}(A) = \mathcal{R}((AB)B^{-1}) \subseteq \mathcal{R}(AB)$. 2. Statement 1 gives $\operatorname{rank}(AB) \le \operatorname{rank}(A)$, with equality when $B$ is invertible. By Theorem 3.8.1, $\operatorname{rank}(AB) = \operatorname{rank}(B^{\mathsf T}A^{\mathsf T}) \le \operatorname{rank}(B^{\mathsf T}) = \operatorname{rank}(B)$. When $A$ is invertible, $AB$ and $B$ are row equivalent, and by Proposition 3.7.1 their columns have the same rank. $\square$

From the point of view of maps, the image of $T_A \circ T_B$ is contained in the image of $T_A$. In general $\mathcal{R}(AB) \ne \mathcal{R}(B)$ (the two need not even lie in the same space).

## 3.9. Equivalence and the Rank Normal Form

**Proposition 3.9.1** Let $A$ be an $m \times n$ matrix and $P, Q$ invertible matrices of orders $m$ and $n$ respectively. Then $\operatorname{rank}(PAQ) = \operatorname{rank}(A)$.

**Proof** Apply Proposition 3.8.4 twice. $\square$

Since the invertible matrices are exactly the products of elementary matrices, this shows that the rank is unchanged by both elementary row operations and elementary column operations.

**Definition 3.9.1 (Equivalence of Matrices)** If a matrix $A$ can be transformed into a matrix $B$ by a sequence of elementary row and column operations, then $A$ and $B$ are said to be equivalent; this relation is called **matrix equivalence**.

**Proposition 3.9.2** Two $m \times n$ matrices $A, B$ are equivalent if and only if there are an invertible matrix $P$ of order $m$ and an invertible matrix $Q$ of order $n$ such that $PAQ = B$. Matrix equivalence is an **equivalence relation** on $\mathbb{R}^{m \times n}$; elementary row and column operations are its equivalence transformations, and the rank is an invariant.

**Theorem 3.9.1 (Rank Normal Form)** Let $A$ be an $m \times n$ matrix with $r = \operatorname{rank}(A)$. Then there are an invertible matrix $P$ of order $m$ and an invertible matrix $Q$ of order $n$ such that

$$
PAQ = D_r = \begin{bmatrix} I_r & O \\ O & O \end{bmatrix}.
$$

$D_r$ is called the rank normal form of $A$ (its normal form under equivalence).

**Proof** First reduce $A$ by elementary row operations to its reduced row echelon form $R$, which has $r$ pivot columns $\boldsymbol{e}_1, \dots, \boldsymbol{e}_r$ in order; every free column is a combination of the pivot columns, so column replacements can turn all free columns into zero. Then column interchanges move $\boldsymbol{e}_j$ to column $j$ ($j = 1, \dots, r$), which gives $D_r$. $\square$

**Corollary 3.9.1** Two $m \times n$ matrices are equivalent if and only if they have the same rank. Under equivalence, the $m \times n$ matrices fall into $\min\{m, n\} + 1$ equivalence classes ($r = 0, 1, \dots, \min\{m, n\}$).

**Proof** If the ranks are equal, both matrices are equivalent to the same $D_r$ and hence, by transitivity, to each other; the converse is Proposition 3.9.1. $\square$

So the rank is a complete invariant of matrix equivalence: a single number captures all the information about a matrix that survives multiplication by invertible matrices on the left and on the right. [Chapter 8](/2.1.8) will show that this corresponds to the fact that, with suitably chosen bases of the domain and the codomain, the matrix of a linear map can be brought to $D_r$.

## 3.10. Solution Sets of Linear Systems

Let $A$ be an $m \times n$ matrix with $\operatorname{rank}(A) = r$. The solution set of the homogeneous system $A\boldsymbol{x} = \boldsymbol{0}$ is the null space $\mathcal{N}(A)$. Reducing $A$ to reduced row echelon form gives $r$ pivot columns and $n - r$ free columns; once the values of the free variables are fixed, the pivot variables are uniquely determined. Let $\boldsymbol{k}_i$ ($i = 1, \dots, n - r$) be the solution obtained by setting the $i$-th free variable to $1$ and all other free variables to $0$.

**Theorem 3.10.1** The vectors $\boldsymbol{k}_1, \dots, \boldsymbol{k}_{n-r}$ above form a basis of $\mathcal{N}(A)$. In particular, $\dim\mathcal{N}(A) = n - \operatorname{rank}(A)$.

**Proof** Spanning: clearly $\operatorname{span}(\boldsymbol{k}_1, \dots, \boldsymbol{k}_{n-r}) \subseteq \mathcal{N}(A)$. Take any $\boldsymbol{k} \in \mathcal{N}(A)$, let $c_1, \dots, c_{n-r}$ be its values at the $n - r$ free variables, and put $\boldsymbol{k}' = c_1\boldsymbol{k}_1 + \cdots + c_{n-r}\boldsymbol{k}_{n-r} - \boldsymbol{k}$. Then $\boldsymbol{k}' \in \mathcal{N}(A)$ and all its free-variable components are zero, so $A\boldsymbol{k}' = \boldsymbol{0}$ says that a linear combination of the pivot columns is zero; the pivot columns are linearly independent, so the pivot-variable components of $\boldsymbol{k}'$ are zero as well, and $\boldsymbol{k}' = \boldsymbol{0}$. Linear independence: if $c_1\boldsymbol{k}_1 + \cdots + c_{n-r}\boldsymbol{k}_{n-r} = \boldsymbol{0}$, comparing the components of the $i$-th free variable gives $c_i = 0$. $\square$

**Example 3.10.1** In Example 1.8.1 the free variables are $x_3, x_5$. From the general solution $x_1 = -x_3 + \frac76x_5$, $x_2 = x_3 + \frac56x_5$, $x_4 = \frac13x_5$, taking $(x_3, x_5) = (1, 0)$ and $(0, 1)$ gives

$$
\boldsymbol{k}_1 = \begin{bmatrix} -1 \\ 1 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \qquad \boldsymbol{k}_2 = \begin{bmatrix} \frac76 \\ \frac56 \\ 0 \\ \frac13 \\ 1 \end{bmatrix},
$$

so $\mathcal{N}(A) = \{x_3\boldsymbol{k}_1 + x_5\boldsymbol{k}_2 \mid x_3, x_5 \in \mathbb{R}\}$ and $\dim\mathcal{N}(A) = 2 = 5 - 3$.

Conversely, a basis of the null space determines the nonzero rows of the reduced row echelon form. For example, if the null space of a $4 \times 5$ matrix $A$ has the basis $\boldsymbol{k}_1, \boldsymbol{k}_2$ above, then the vectors of $\mathcal{N}(A)$ have the form $[-c_1 + \frac76c_2\ \ c_1 + \frac56c_2\ \ c_1\ \ \frac13c_2\ \ c_2]^{\mathsf T}$; that is, $x_3 = c_1$ and $x_5 = c_2$ are free variables, and $x_1 + x_3 - \frac76x_5 = 0$, $x_2 - x_3 - \frac56x_5 = 0$, $x_4 - \frac13x_5 = 0$. The coefficients of these three equations are the three nonzero rows of $\operatorname{rref}(A)$ (by Corollary 3.7.1, the reduced row echelon form is uniquely determined by the null space).

The solution set of a nonhomogeneous system is not a subspace, but it is a translate of the null space. Suppose $A\boldsymbol{x} = \boldsymbol{b}$ has a particular solution $\boldsymbol{k}_0$. Then $\boldsymbol{k}$ is a solution if and only if $A(\boldsymbol{k} - \boldsymbol{k}_0) = \boldsymbol{0}$. Hence $\boldsymbol{k} \mapsto \boldsymbol{k} - \boldsymbol{k}_0$ is a bijection from the solution set $\{\boldsymbol{x} \mid A\boldsymbol{x} = \boldsymbol{b}\}$ onto $\mathcal{N}(A)$, with inverse $\boldsymbol{k}' \mapsto \boldsymbol{k}' + \boldsymbol{k}_0$. The system $A\boldsymbol{x} = \boldsymbol{0}$ is called the associated homogeneous system of $A\boldsymbol{x} = \boldsymbol{b}$.

**Theorem 3.10.2 (Solution Set of a Nonhomogeneous System)** Suppose $A\boldsymbol{x} = \boldsymbol{b}$ has a particular solution $\boldsymbol{k}_0$, and let $\boldsymbol{k}_1, \dots, \boldsymbol{k}_{n-r}$ be a basis of $\mathcal{N}(A)$, where $r = \operatorname{rank}(A)$. Then the solution set of $A\boldsymbol{x} = \boldsymbol{b}$ is

$$
\boldsymbol{k}_0 + \mathcal{N}(A) = \{\boldsymbol{k}_0 + c_1\boldsymbol{k}_1 + \cdots + c_{n-r}\boldsymbol{k}_{n-r} \mid c_1, \dots, c_{n-r} \in \mathbb{R}\}.
$$

Geometrically, the solution set of $A\boldsymbol{x} = \boldsymbol{b}$ is obtained by translating the subspace $\mathcal{N}(A)$ through the origin by $\boldsymbol{k}_0$: it is parallel to $\mathcal{N}(A)$ and has the same dimension, but does not pass through the origin. For example, for the system $x_1 + x_2 + x_3 = 1$, $x_1 - x_2 = 0$ we have $\operatorname{rank}(A) = 2$, the null space $\mathcal{N}(A) = \operatorname{span}([1\ 1\ {-2}]^{\mathsf T})$ is a line through the origin in $\mathbb{R}^3$, and one particular solution is $\boldsymbol{k}_0 = [\frac12\ \frac12\ 0]^{\mathsf T}$:

![The solution set of x₁ + x₂ + x₃ = 1, x₁ − x₂ = 0: the line of intersection k₀ + N(A) of the two planes (red) is parallel to the null space N(A) (green, dashed), and the two differ by a particular solution k₀](./plots/solution-set-translate.py)

The solvability criterion of Chapter 1 (Theorem 1.7.2) can be restated in terms of rank:

**Theorem 3.10.3 (Solvability Criterion)** For a linear system $A\boldsymbol{x} = \boldsymbol{b}$ in $n$ unknowns:

1. it has no solution if and only if $\operatorname{rank}(A) < \operatorname{rank}([A\ \boldsymbol{b}])$, that is, $\boldsymbol{b} \notin \mathcal{R}(A)$; it is solvable if and only if $\operatorname{rank}(A) = \operatorname{rank}([A\ \boldsymbol{b}])$, that is, $\boldsymbol{b} \in \mathcal{R}(A)$;
2. it has a unique solution if and only if $\operatorname{rank}(A) = \operatorname{rank}([A\ \boldsymbol{b}]) = n$, that is, it is solvable and $\dim\mathcal{N}(A) = 0$;
3. it has infinitely many solutions if and only if $\operatorname{rank}(A) = \operatorname{rank}([A\ \boldsymbol{b}]) < n$, that is, it is solvable and $\dim\mathcal{N}(A) > 0$.

Putting these results together gives the complete standard procedure for solving a linear system:

**Algorithm 3.10.1 (General Solution of a Linear System)** Input: $A\boldsymbol{x} = \boldsymbol{b}$.

1. Reduce $[A\ \boldsymbol{b}]$ to reduced row echelon form and compare $\operatorname{rank}(A)$ with $\operatorname{rank}([A\ \boldsymbol{b}])$; if they differ, there is no solution, and stop.
2. Set all free variables to $0$ and read off a particular solution $\boldsymbol{k}_0$ (the values of the pivot variables are the corresponding entries of the last column).
3. For each free variable, set it to $1$ and the other free variables to $0$, and replace the right-hand side by zero; this gives the basis vectors $\boldsymbol{k}_i$ of $\mathcal{N}(A)$.
4. The general solution is $\boldsymbol{k}_0 + c_1\boldsymbol{k}_1 + \cdots + c_{n-r}\boldsymbol{k}_{n-r}$.

**Example 3.10.2** Find the solution set of $\begin{cases} x_1 - x_2 + x_4 - x_5 = 1, \\ 2x_1 + x_3 - x_5 = 2, \\ 3x_1 - x_2 - x_3 - x_4 - x_5 = 0. \end{cases}$

$$
[A\ \boldsymbol{b}] = \begin{bmatrix} 1 & -1 & 0 & 1 & -1 & 1 \\ 2 & 0 & 1 & 0 & -1 & 2 \\ 3 & -1 & -1 & -1 & -1 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & 0 & 0 & -\frac12 & -\frac14 & \frac14 \\ 0 & 1 & 0 & -\frac32 & \frac34 & -\frac34 \\ 0 & 0 & 1 & 1 & -\frac12 & \frac32 \end{bmatrix}.
$$

Since $\operatorname{rank}(A) = \operatorname{rank}([A\ \boldsymbol{b}]) = 3 < 5$, there are infinitely many solutions; columns $1, 2, 3$ are pivot columns and $x_4, x_5$ are free variables. The solutions satisfy $x_1 = \frac14 + \frac12x_4 + \frac14x_5$, $x_2 = -\frac34 + \frac32x_4 - \frac34x_5$, $x_3 = \frac32 - x_4 + \frac12x_5$, and the solution set is

$$
\left\{ \begin{bmatrix} \frac14 \\ -\frac34 \\ \frac32 \\ 0 \\ 0 \end{bmatrix} + c_1\begin{bmatrix} \frac12 \\ \frac32 \\ -1 \\ 1 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} \frac14 \\ -\frac34 \\ \frac12 \\ 0 \\ 1 \end{bmatrix} \;\middle|\; c_1, c_2 \in \mathbb{R} \right\},
$$

where the first vector is the particular solution with $x_4 = x_5 = 0$, and the other two form a basis of $\mathcal{N}(A)$.

## 3.11. The Four Fundamental Subspaces and the Dimension Formulas

Three subspaces derived from a matrix have appeared so far: the column space $\mathcal{R}(A)$, the null space $\mathcal{N}(A)$ and the row space $\mathcal{R}(A^{\mathsf T})$. We add a fourth:

**Definition 3.11.1 (Left Null Space)** Let $A$ be an $m \times n$ matrix. The subspace $\mathcal{N}(A^{\mathsf T})$ of $\mathbb{R}^m$ is called the **left null space** of $A$.

A vector $\boldsymbol{y} \in \mathcal{N}(A^{\mathsf T})$ satisfies $\boldsymbol{y}^{\mathsf T}A = (A^{\mathsf T}\boldsymbol{y})^{\mathsf T} = \boldsymbol{0}^{\mathsf T}$, that is, $\boldsymbol{y}$ gives a linear relation among the rows of $A$.

**Theorem 3.11.1 (Rank–Nullity Theorem)** Let $A$ be an $m \times n$ matrix. Then

$$
\dim\mathcal{R}(A) + \dim\mathcal{N}(A) = n, \qquad \dim\mathcal{R}(A^{\mathsf T}) + \dim\mathcal{N}(A^{\mathsf T}) = m.
$$

**Proof** The first formula is Theorem 3.10.1. Applying it to $A^{\mathsf T}$ and using $\operatorname{rank}(A^{\mathsf T}) = \operatorname{rank}(A)$ (Theorem 3.8.1) gives the second. $\square$

The course slides call these two formulas the dimension formulas for the four subspaces. In terms of linear systems: $\dim\mathcal{R}(A)$ is the number of pivot variables and $\dim\mathcal{N}(A)$ the number of free variables, which add up to the total number $n$ of unknowns; $\dim\mathcal{R}(A^{\mathsf T})$ is the number of effective equations and $\dim\mathcal{N}(A^{\mathsf T})$ the number of redundant equations (the nonzero vectors of the left null space are exactly linear relations among the rows, as in Example 3.8.1), which add up to the total number $m$ of equations.

| Subspace | Ambient space | Dimension | A basis (obtained by elimination) |
|---|---|---|---|
| Column space $\mathcal{R}(A)$ | $\mathbb{R}^m$ | $r$ | the pivot columns of $A$ (Algorithm 3.7.1) |
| Null space $\mathcal{N}(A)$ | $\mathbb{R}^n$ | $n - r$ | the solutions with one free variable equal to $1$ in turn (Theorem 3.10.1) |
| Row space $\mathcal{R}(A^{\mathsf T})$ | $\mathbb{R}^n$ | $r$ | the nonzero rows of a row echelon form (Proposition 3.8.1) |
| Left null space $\mathcal{N}(A^{\mathsf T})$ | $\mathbb{R}^m$ | $m - r$ | the null space of $A^{\mathsf T}$, or the combination coefficients recorded for the zero rows during elimination |

For the $4 \times 5$ matrix of Example 3.7.1, the dimensions of the four subspaces are $3, 2, 3, 1$ in turn, and the left null space is spanned by $[-\frac53\ \ 5\ \ {-\frac43}\ \ 1]^{\mathsf T}$ (the zero row of Example 3.8.1). [Chapter 4](/2.1.4) will prove that $\mathcal{N}(A)$ and $\mathcal{R}(A^{\mathsf T})$, as well as $\mathcal{N}(A^{\mathsf T})$ and $\mathcal{R}(A)$, are orthogonal complements of each other; this is the geometric foundation of the method of least squares.

The figure below shows the four fundamental subspaces for the rank-one matrix $A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$. A vector $\boldsymbol{x}$ in the domain can be split as the sum of a vector $\boldsymbol{x}_r$ in the row space and a vector $\boldsymbol{x}_n$ in the null space ([Chapter 4](/2.1.4)); since $A\boldsymbol{x}_n = \boldsymbol{0}$, the image $A\boldsymbol{x} = A\boldsymbol{x}_r$ lies in the column space. All vectors that differ from $\boldsymbol{x}$ by a vector of the null space have the same image, and they form the solution set of $A\boldsymbol{x} = \boldsymbol{b}$.

![The four fundamental subspaces of the rank-one matrix A with rows (1, 2) and (3, 6). Left: the row space and the null space in the domain, with x = x_r + x_n; the dashed line is the solution set x + N(A) of Ax = b. Right: the column space and the left null space in the codomain, where b = Ax lies in the column space. The two pairs of subspaces are perpendicular, as will be proved in Chapter 4](./plots/four-subspaces.py)

## Summary

This chapter answered the question of the structure of solution sets in the language of linear combinations; the central invariant is the rank.

| Category | Content |
|---|---|
| Definitions | Subspace (Definition 3.2.1); column space and null space (Definition 3.2.2); span (Definition 3.3.1); linear dependence and independence (Definition 3.3.2); basis and standard basis (Definitions 3.4.1, 3.4.2); linear representation between lists, maximal linearly independent subset, linear equivalence, rank of a list of vectors (Definitions 3.5.1–3.5.4); dimension (Definition 3.6.1); rank of a matrix (Definition 3.7.1); row space (Definition 3.8.1); full row rank, full column rank, full rank (Definition 3.8.2); equivalence of matrices (Definition 3.9.1); left null space (Definition 3.11.1) |
| Theorems | Injectivity, surjectivity and $\mathcal{N}(A)$, $\mathcal{R}(A)$ (Proposition 3.1.2); $n > m$ vectors are always dependent (Proposition 3.3.2); unique representation $\Leftrightarrow$ linear independence (Proposition 3.3.3); the columns of a square matrix form a basis $\Leftrightarrow$ it is invertible (Proposition 3.4.1); linear representation between lists and the number of vectors (Propositions 3.5.2–3.5.6); existence of bases and basis extension (Theorems 3.6.1, 3.6.2); criterion for a basis (Proposition 3.6.2); row operations preserve linear relations among the columns (Proposition 3.7.1); the pivot columns form a basis of the column space (Theorem 3.7.1); uniqueness of the rref (Corollary 3.7.1); $\operatorname{rank}(A^{\mathsf T}) = \operatorname{rank}(A)$ (Theorem 3.8.1); full rank versus injectivity, surjectivity and one-sided inverses (Propositions 3.8.2, 3.8.3); rank of a product (Proposition 3.8.4); rank normal form (Theorem 3.9.1); a basis of the null space and $\dim\mathcal{N}(A) = n - r$ (Theorem 3.10.1); solution set $= \boldsymbol{k}_0 + \mathcal{N}(A)$ (Theorem 3.10.2); solvability criterion in terms of rank (Theorem 3.10.3); rank–nullity theorem (Theorem 3.11.1) |
| Algorithms | Sifting method (Algorithm 3.5.1); maximal linearly independent subset via the reduced row echelon form (Algorithm 3.7.1); general solution of a linear system (Algorithm 3.10.1) |

| Condition ($A$ is $m \times n$, $r = \operatorname{rank}(A)$) | Map $\boldsymbol{x} \mapsto A\boldsymbol{x}$ | System | Inverse |
|---|---|---|---|
| $r = n$ (full column rank) | injective, $\mathcal{N}(A) = \{\boldsymbol{0}\}$ | $A\boldsymbol{x} = \boldsymbol{b}$ has at most one solution | a left inverse $BA = I_n$ exists |
| $r = m$ (full row rank) | surjective, $\mathcal{R}(A) = \mathbb{R}^m$ | solvable for every $\boldsymbol{b}$ | a right inverse $AB = I_m$ exists |
| $r = m = n$ (full rank) | bijective | a unique solution for every $\boldsymbol{b}$ | invertible |
