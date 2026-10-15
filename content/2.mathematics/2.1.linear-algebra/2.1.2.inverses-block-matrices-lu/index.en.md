---
title: Inverse Matrices, Block Matrices and the LU Decomposition
source_hash: 9d404f8f7431
---

The previous chapter reduced the solution of linear systems to elimination. This chapter restates elimination in terms of matrix multiplication: every elementary row operation is multiplication on the left by an elementary matrix, so the question "can the matrix be eliminated to the identity?" becomes the question "is the matrix invertible?", and computing an inverse and solving a system are essentially the same problem. We then view matrices as made of blocks, which obey the same rules of computation as entries; block elimination yields the Schur complement and the Sherman–Morrison–Woodbury formula, which show that the inverse of a matrix after a low-rank modification can be updated cheaply. Finally, we record the whole process of Gaussian elimination as a matrix factorization $A = LU$, together with its variants, the $LDU$ and $PLU$ decompositions. Factoring once and reusing the factors many times is a typical instance of the "standardized solution" approach of numerical linear algebra.

The notions about maps used in this chapter (**injection**, **surjection**, **bijection**, left and right inverses) come from [1.2.3](/1.2.3), and the **equivalence relation** from [1.2.2](/1.2.2). The invertible matrices form the **general linear group** of 1.3. [Chapter 3](/2.1.3) will use the rank to extend the invertibility conditions of this chapter to general $m \times n$ matrices.

## 2.1. Elementary Matrices

The three types of elementary row operations used in elimination are all linear transformations of $\mathbb{R}^n$. By Definition 1.3.2, their standard matrices are obtained by applying the same operation to the columns of $I_n$, that is, to $I_n$ itself.

**Definition 2.1.1 (Elementary Matrix)** A matrix obtained from the identity matrix $I_n$ by a single elementary operation is called an **elementary matrix**. There are three types:

1. the interchange matrix $P_{ij}$: interchange rows $i$ and $j$ of $I_n$ (equivalently, columns $i$ and $j$);
2. the scaling matrix $E_{ii;k}$ ($k \ne 0$): multiply row $i$ of $I_n$ by $k$ (equivalently, column $i$ by $k$);
3. the replacement matrix $E_{ji;k}$: add $k$ times row $i$ of $I_n$ to row $j$ (equivalently, add $k$ times column $j$ to column $i$), that is, $E_{ji;k} = I_n + k\boldsymbol{e}_j\boldsymbol{e}_i^{\mathsf T}$.

For $n = 3$, for example,

$$
P_{12} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \qquad
E_{22;k} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & k & 0 \\ 0 & 0 & 1 \end{bmatrix}, \qquad
E_{31;k} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ k & 0 & 1 \end{bmatrix}.
$$

The transpose of an elementary matrix is an elementary matrix of the same type: $P_{ij}^{\mathsf T} = P_{ij}$, $E_{ii;k}^{\mathsf T} = E_{ii;k}$, $E_{ji;k}^{\mathsf T} = E_{ij;k}$.

**Proposition 2.1.1 (Rows on the Left, Columns on the Right)** Let $T$ be the matrix obtained from $I_m$ by some elementary row operation. Then for every $m \times n$ matrix $A$, $TA$ is the result of applying the same row operation to $A$. Let $T$ be the matrix obtained from $I_n$ by some elementary column operation. Then $AT$ is the result of applying the same column operation to $A$.

**Proof** $T$ is the standard matrix of the row operation (a linear transformation), so $TA = [T\boldsymbol{a}_1\ \cdots\ T\boldsymbol{a}_n]$ applies this transformation to every column of $A$, which is the same as applying the row operation to $A$. For columns: $AT = (T^{\mathsf T}A^{\mathsf T})^{\mathsf T}$, where $T^{\mathsf T}$ is obtained from $I_n$ by the corresponding elementary row operation, and a row operation on $A^{\mathsf T}$ is a column operation on $A$. $\square$

For example, $P_{ij}A$ interchanges rows $i$ and $j$ of $A$, and $AP_{ij}$ interchanges columns $i$ and $j$; $E_{ji;k}A$ adds $k$ times row $i$ of $A$ to row $j$, and $AE_{ji;k}$ adds $k$ times column $j$ of $A$ to column $i$. Thus Gauss(–Jordan) elimination on $A$ amounts to finding elementary matrices $E_1, \dots, E_t$ such that $E_t\cdots E_2E_1A$ is in (reduced) row echelon form.

**Example 2.1.1** Written as matrix multiplications, the elimination of Example 1.6.1 is

$$
\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & \frac12 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ -2 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 & 8 \\ 2 & 4 & 22 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 5 \\ 0 & 1 & 3 \end{bmatrix},
$$

with the factors $E_{21;-2}$, $E_{22;1/2}$, $E_{12;-1}$ applied in turn.

In the row picture, each multiplication by an elementary matrix replaces the lines of the system by other lines while leaving their intersection point fixed (Theorem 1.6.1): elimination gradually turns the two slanted lines into the lines $x_1 = 5$ and $x_2 = 3$ parallel to the coordinate axes, from which the solution can be read off.

![The row picture at each step of the elimination in Example 2.1.1: elementary row operations change the lines but keep their intersection point (5, 3); scaling does not change the line itself, and at the end the two lines are parallel to the coordinate axes](./plots/elimination-row-picture.py)

## 2.2. Invertible Maps and Invertible Matrices

**Definition 2.2.1 (Invertible Map)** Let $f\colon X \to Y$ be a map. If there is a map $g\colon Y \to X$ such that $f \circ g = \mathrm{id}_Y$ and $g \circ f = \mathrm{id}_X$, then $f$ is said to be invertible, and $g$ is called an inverse of $f$.

**Proposition 2.2.1** The inverse of an invertible map is unique; it is denoted by $f^{-1}$.

**Proof** If $g$ and $h$ are both inverses of $f$, then $g = \mathrm{id}_X \circ g = (h \circ f) \circ g = h \circ (f \circ g) = h \circ \mathrm{id}_Y = h$. $\square$

By [Theorem 3.2.8 of 1.2.3](/1.2.3#thm-3.2.8) (for $X \ne \varnothing$): $f$ is an **injection** if and only if there is a $g$ with $g \circ f = \mathrm{id}_X$ ($g$ is a **left inverse** of $f$); $f$ is a **surjection** if and only if there is a $g$ with $f \circ g = \mathrm{id}_Y$ (a **right inverse**); and $f$ is a **bijection** (a one-to-one correspondence) if and only if $f$ is invertible.

**Definition 2.2.2 (Invertible Linear Transformation)** Let $T_A$ and $T_B$ be linear transformations of $\mathbb{R}^n$. If $T_A \circ T_B = T_B \circ T_A = \mathrm{id}$, then $T_A$ and $T_B$ are called invertible transformations, and $T_B = T_A^{-1}$ is the inverse transformation of $T_A$.

**Proposition 2.2.2** If $T_A\colon \mathbb{R}^n \to \mathbb{R}^n$ is an invertible linear transformation, then the inverse map $T_A^{-1}$ is also a linear transformation.

**Proof** Let $\boldsymbol{y} = T_A(\boldsymbol{x})$, $\boldsymbol{y}' = T_A(\boldsymbol{x}')$ and $k \in \mathbb{R}$. Since $T_A$ is linear, $T_A(\boldsymbol{x} + \boldsymbol{x}') = \boldsymbol{y} + \boldsymbol{y}'$ and $T_A(k\boldsymbol{x}) = k\boldsymbol{y}$, so $T_A^{-1}(\boldsymbol{y} + \boldsymbol{y}') = \boldsymbol{x} + \boldsymbol{x}' = T_A^{-1}(\boldsymbol{y}) + T_A^{-1}(\boldsymbol{y}')$ and $T_A^{-1}(k\boldsymbol{y}) = k\boldsymbol{x} = kT_A^{-1}(\boldsymbol{y})$. $\square$

Translating into standard matrices gives the definition of an invertible matrix.

**Definition 2.2.3 (Invertible Matrix)** Let $A$ be a square matrix of order $n$. If there is a square matrix $B$ of order $n$ such that $AB = BA = I_n$, then $A$ is called an **invertible matrix** (nonsingular matrix), and $B$ is called the **inverse matrix** of $A$, denoted by $A^{-1}$. A square matrix that is not invertible is called a **singular matrix**.

If an inverse exists, it is unique: if $B$ and $\tilde{B}$ are both inverses of $A$, then $B = BI_n = B(A\tilde{B}) = (BA)\tilde{B} = \tilde{B}$. The linear transformation $T_A\colon \boldsymbol{x} \mapsto A\boldsymbol{x}$ is invertible if and only if the matrix $A$ is invertible, and in that case the standard matrix of $T_A^{-1}$ is $A^{-1}$, that is, $T_A^{-1} = T_{A^{-1}}$. For a positive integer $k$ and an invertible matrix $A$, negative powers are defined by $A^{-k} = (A^{-1})^k$.

**Example 2.2.1**

- $I_n$ is invertible with $I_n^{-1} = I_n$; the zero matrix is not invertible, because $OB = O \ne I_n$.
- Every elementary matrix is invertible, and its inverse corresponds to the inverse operation (Proposition 1.6.1): $P_{ij}^{-1} = P_{ij}$, $E_{ii;k}^{-1} = E_{ii;1/k}$, $E_{ji;k}^{-1} = E_{ji;-k}$. For example, $\begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}^{-1} = \begin{bmatrix} 1 & 0 \\ -k & 1 \end{bmatrix}$.
- A diagonal matrix $D = \operatorname{diag}(d_1, \dots, d_n)$ is invertible if and only if all its diagonal entries are nonzero, and then $D^{-1} = \operatorname{diag}(d_1^{-1}, \dots, d_n^{-1})$. If some $d_i = 0$, then for every $B$ the $i$-th row of $DB$ is zero, so $DB$ cannot equal $I_n$.

**Proposition 2.2.3 (Properties of Invertible Matrices)** Let $A$ and $B$ be invertible matrices of order $n$. Then

1. $A^{-1}$ is invertible and $(A^{-1})^{-1} = A$;
2. $A^{\mathsf T}$ is invertible and $(A^{\mathsf T})^{-1} = (A^{-1})^{\mathsf T}$, which is denoted by $A^{-\mathsf T}$;
3. $AB$ is invertible and $(AB)^{-1} = B^{-1}A^{-1}$.

**Proof** Statement 1 follows from the symmetry of the definition. Statement 2: $(A^{-1})^{\mathsf T}A^{\mathsf T} = (AA^{-1})^{\mathsf T} = I$ and $A^{\mathsf T}(A^{-1})^{\mathsf T} = (A^{-1}A)^{\mathsf T} = I$. Statement 3: $(B^{-1}A^{-1})(AB) = B^{-1}B = I$ and $(AB)(B^{-1}A^{-1}) = AA^{-1} = I$. $\square$

More generally, $(A_1A_2\cdots A_k)^{-1} = A_k^{-1}\cdots A_2^{-1}A_1^{-1}$, and in particular $A^{-k} = (A^{-1})^k = (A^k)^{-1}$. Therefore the real invertible matrices of order $n$ form a **group** under matrix multiplication, the **general linear group** $\mathrm{GL}(n, \mathbb{R})$.

## 2.3. Criteria for Invertibility and Computing Inverses

**Theorem 2.3.1 (Equivalent Conditions for Invertibility)** For a square matrix $A$ of order $n$, the following are equivalent:

1. $A$ is invertible;
2. for every $\boldsymbol{b} \in \mathbb{R}^n$, the linear system $A\boldsymbol{x} = \boldsymbol{b}$ has a unique solution;
3. the homogeneous linear system $A\boldsymbol{x} = \boldsymbol{0}$ has only the zero solution;
4. a row echelon form of $A$ has $n$ pivots;
5. the reduced row echelon form of $A$ is $I_n$;
6. $A$ is a product of finitely many elementary matrices.

**Proof** We prove the implications in a cycle. $1 \Rightarrow 2$: if $A$ is invertible, then $\boldsymbol{x} \mapsto A\boldsymbol{x}$ is an invertible transformation and hence a bijection, so every $\boldsymbol{b}$ has exactly one preimage ($\boldsymbol{x} = A^{-1}\boldsymbol{b}$). $2 \Rightarrow 3$: take $\boldsymbol{b} = \boldsymbol{0}$. $3 \Rightarrow 4$: by Corollary 1.8.1, there is only the zero solution if and only if the number of pivots equals $n$. $4 \Rightarrow 5$: when a square matrix of order $n$ has $n$ pivots, every column is a pivot column, and its reduced form is $I_n$. $5 \Rightarrow 6$: there are elementary matrices $E_1, \dots, E_t$ with $E_t\cdots E_1A = I_n$, so $A = E_1^{-1}\cdots E_t^{-1}$, and the inverse of an elementary matrix is again elementary. $6 \Rightarrow 1$: elementary matrices are invertible, and a product of invertible matrices is invertible (Proposition 2.2.3). $\square$

**Proposition 2.3.1** Let $A$ and $B$ be square matrices of order $n$.

1. If $BA = I_n$ or $AB = I_n$, then $A$ and $B$ are both invertible, with $A^{-1} = B$ and $B^{-1} = A$;
2. $AB$ is invertible if and only if $A$ and $B$ are both invertible.

**Proof** 1. If $BA = I_n$, then $A\boldsymbol{x} = \boldsymbol{0}$ implies $\boldsymbol{x} = BA\boldsymbol{x} = \boldsymbol{0}$, so $A$ is invertible by Theorem 2.3.1, and $B = BAA^{-1} = A^{-1}$; if $AB = I_n$, apply the same argument to $B$. 2. Necessity: if $AB$ is invertible, then $B\boldsymbol{x} = \boldsymbol{0}$ implies $AB\boldsymbol{x} = \boldsymbol{0}$, hence $\boldsymbol{x} = \boldsymbol{0}$, and $B$ is invertible; then $A = (AB)B^{-1}$ is invertible as well. Sufficiency is Proposition 2.2.3. $\square$

So for square matrices it suffices to verify an inverse on one side. This fails for maps in general (an injection has a left inverse but need not have a right inverse); what is special about square matrices is that condition 3 (injectivity) in Theorem 2.3.1 already implies condition 2 (bijectivity).

The proof of Theorem 2.3.1 also gives a method for computing the inverse: if $E_t\cdots E_1A = I_n$ and $E = E_t\cdots E_1$, then $E = A^{-1}$. Applying the same elementary row operations to $I_n$ produces $E$.

**Algorithm 2.3.1 (Gauss–Jordan Inversion)** Place $A$ and $I_n$ side by side in the $n \times 2n$ matrix $[A\ I_n]$, and reduce the left half to reduced row echelon form by Gauss–Jordan elimination. If the left half becomes $I_n$, then

$$
E[A\ I_n] = [I_n\ E] = [I_n\ A^{-1}];
$$

if the left half has fewer than $n$ pivots, $A$ is not invertible. The same method solves the matrix equation $AX = B$: $[A\ B] \to [I_n\ A^{-1}B]$.

**Example 2.3.1** Compute the inverse of $A = \begin{bmatrix} 1 & 1 \\ 2 & 4 \end{bmatrix}$:

$$
\begin{bmatrix} 1 & 1 & 1 & 0 \\ 2 & 4 & 0 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 1 & 0 \\ 0 & 2 & -2 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 1 & 0 \\ 0 & 1 & -1 & \frac12 \end{bmatrix} \to
\begin{bmatrix} 1 & 0 & 2 & -\frac12 \\ 0 & 1 & -1 & \frac12 \end{bmatrix},
\qquad A^{-1} = \begin{bmatrix} 2 & -\frac12 \\ -1 & \frac12 \end{bmatrix}.
$$

Inversion costs about $2n^3$ floating-point operations, three times as much as Gaussian elimination (see the figure in Section 2.10). Therefore, to solve $A\boldsymbol{x} = \boldsymbol{b}$ one should not first compute $A^{-1}$ and then $A^{-1}\boldsymbol{b}$; one should eliminate directly or use the LU decomposition.

The structure of triangular matrices is preserved under multiplication and inversion, which is the basis of the LU decomposition.

**Property 2.3.1** The product of two upper triangular matrices of order $n$ is upper triangular, and its diagonal entries are the products of the corresponding diagonal entries of the factors. The same holds for lower triangular and for unit upper (lower) triangular matrices.

**Proof** Let $U = [u_{ij}]$ and $V = [v_{ij}]$ be upper triangular. A term of $(UV)_{ik} = \sum_j u_{ij}v_{jk}$ can be nonzero only if $i \le j \le k$. Hence $(UV)_{ik} = 0$ for $i > k$, and for $i = k$ only $u_{ii}v_{ii}$ remains. $\square$

**Proposition 2.3.2 (Inverse of a Triangular Matrix)** An upper triangular matrix is invertible if and only if its diagonal entries are all nonzero. In that case its inverse is also upper triangular, and its diagonal entries are the reciprocals of the corresponding diagonal entries of the original matrix. The same holds for lower triangular matrices.

**Proof** Let $U$ be an upper triangular matrix of order $n$. If its diagonal entries are all nonzero, $U$ itself is an echelon form with $n$ pivots and is invertible by Theorem 2.3.1; the $j$-th column of $U^{-1}$ is the solution of $U\boldsymbol{x} = \boldsymbol{e}_j$, and back substitution gives $x_n = \cdots = x_{j+1} = 0$ and $x_j = 1/u_{jj}$, so $U^{-1}$ is upper triangular with diagonal entries $1/u_{jj}$. Conversely, if some $u_{kk} = 0$, then the first $k$ columns of $U$ have nonzero entries only in the first $k-1$ rows, so the homogeneous system $[\boldsymbol{u}_1\ \cdots\ \boldsymbol{u}_k]\boldsymbol{y} = \boldsymbol{0}$ really has only $k-1$ equations and, by Corollary 1.8.2, a nonzero solution $\boldsymbol{y}$; then $\boldsymbol{x} = [\boldsymbol{y}^{\mathsf T}\ \boldsymbol{0}^{\mathsf T}]^{\mathsf T} \ne \boldsymbol{0}$ satisfies $U\boldsymbol{x} = \boldsymbol{0}$, and $U$ is not invertible. For lower triangular matrices, take transposes. $\square$

**Definition 2.3.1 (Permutation Matrix)** A matrix obtained from the identity matrix by a sequence of row interchanges, that is, a product of interchange matrices, is called a **permutation matrix**.

**Proposition 2.3.3** Permutation matrices have the following properties:

1. a matrix obtained from the identity matrix by a sequence of column interchanges is also a permutation matrix;
2. a permutation matrix is exactly a matrix obtained by rearranging the rows (or columns) of the identity matrix in some order; every row and every column contains exactly one $1$;
3. there are $n!$ permutation matrices of order $n$, in one-to-one correspondence with the **permutations** of $n$ elements;
4. a product of permutation matrices is a permutation matrix;
5. a permutation matrix $P$ is invertible, and $P^{-1} = P^{\mathsf T}$ is again a permutation matrix.

**Proof** Interchanging columns gives the same matrix as interchanging the corresponding rows ($P_{ij}$ is symmetric), so 1 holds. Every arrangement can be obtained by a sequence of interchanges, so 2 and 3 hold. Statement 4 follows from the definition. For 5: the columns of $P$ are the distinct vectors $\boldsymbol{e}_{\sigma(1)}, \dots, \boldsymbol{e}_{\sigma(n)}$, and the $(i, j)$ entry of $P^{\mathsf T}P$ is $\boldsymbol{e}_{\sigma(i)}^{\mathsf T}\boldsymbol{e}_{\sigma(j)}$, so $P^{\mathsf T}P = I_n$; the rows of $P^{\mathsf T}$ are the columns of $P$, again an arrangement of the rows of $I_n$. $\square$

**Definition 2.3.2 (Diagonally Dominant Matrix)** A square matrix $A = [a_{ij}]_{n \times n}$ is called a (row) **diagonally dominant matrix** if $|a_{ii}| > \sum_{j \ne i}|a_{ij}|$ for every $i = 1, \dots, n$.

**Proposition 2.3.4** A diagonally dominant matrix is invertible.

**Proof** It suffices to show that $A\boldsymbol{x} = \boldsymbol{0}$ has only the zero solution. Suppose to the contrary that $\boldsymbol{x} \ne \boldsymbol{0}$ satisfies $A\boldsymbol{x} = \boldsymbol{0}$. Take a component $x_i$ of largest absolute value; we may assume $|x_i| = 1$, so that $|x_j| \le 1$. From the $i$-th equation $a_{ii}x_i = -\sum_{j \ne i}a_{ij}x_j$,

$$
|a_{ii}| = |a_{ii}x_i| = \Bigl|\sum_{j \ne i}a_{ij}x_j\Bigr| \le \sum_{j \ne i}|a_{ij}||x_j| \le \sum_{j \ne i}|a_{ij}| < |a_{ii}|,
$$

a contradiction. $\square$

Diagonally dominant matrices arise frequently in the discretization of differential equations; their invertibility can be checked from the sizes of the entries alone, without elimination.

## 2.4. Row Equivalence and Equivalence Relations

**Definition 2.4.1 (Row Equivalence)** If a matrix $A$ can be transformed into a matrix $B$ by a sequence of elementary row operations, then $A$ and $B$ are said to be row equivalent; this relation is called **row equivalence**.

**Proposition 2.4.1** Two $m \times n$ matrices $A$ and $B$ are row equivalent if and only if there is an invertible matrix $P$ of order $m$ such that $PA = B$.

**Proof** $A$ can be transformed into $B$ by a sequence of elementary row operations if and only if there are elementary matrices $P_1, \dots, P_s$ of order $m$ with $P_s\cdots P_1A = B$; by Theorem 2.3.1, the invertible matrices are exactly the products of elementary matrices. $\square$

Row equivalence is an **equivalence relation** on $\mathbb{R}^{m \times n}$: $A = I_mA$ (reflexivity); $PA = B \Rightarrow A = P^{-1}B$ (symmetry); $PA = B$, $QB = C \Rightarrow (QP)A = C$ (transitivity). In general, for an equivalence relation on a set $S$, the elements equivalent to an element $a$ form the **equivalence class** of $a$; two different equivalence classes are disjoint, and $S$ is the disjoint union of all equivalence classes. A process that replaces an element by an equivalent one is called an equivalence transformation; a property shared by all elements of each equivalence class is called an invariant of the relation; and an element of an equivalence class that has the simplest form and the best properties is called a normal form (canonical form).

For row equivalence, elementary row operations are the equivalence transformations; homogeneous systems with row equivalent coefficient matrices (or systems with row equivalent augmented matrices) have the same solution set, which is an invariant; and the reduced row echelon form is the normal form, called the normal form under row equivalence ([Chapter 3](/2.1.3) proves that it is unique). From this point of view, Gauss–Jordan elimination reduces the augmented matrix to its normal form under row equivalence and reads off the invariant, the solution set of the system, directly from the normal form. Introducing an equivalence relation and then simplifying the problem by equivalence transformations is a method that runs through this whole course: later we will meet equivalence of matrices ([Chapter 3](/2.1.3)), similarity ([Chapter 6](/2.1.6)) and congruence ([Chapter 7](/2.1.7)).

## 2.5. Block Matrices

In matrix computations we often write a matrix as column vectors or row vectors placed side by side. Let $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_m]$ be an $\ell \times m$ matrix with rows $\tilde{\boldsymbol{a}}_i^{\mathsf T}$, and let $B$ be an $m \times n$ matrix with columns $\boldsymbol{b}_k$ and rows $\tilde{\boldsymbol{b}}_j^{\mathsf T}$. Then

$$
AB = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{b}_1 & \cdots & \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{b}_n \\ \vdots & & \vdots \\ \tilde{\boldsymbol{a}}_\ell^{\mathsf T}\boldsymbol{b}_1 & \cdots & \tilde{\boldsymbol{a}}_\ell^{\mathsf T}\boldsymbol{b}_n \end{bmatrix} = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_m]\begin{bmatrix} \tilde{\boldsymbol{b}}_1^{\mathsf T} \\ \vdots \\ \tilde{\boldsymbol{b}}_m^{\mathsf T} \end{bmatrix} = \boldsymbol{a}_1\tilde{\boldsymbol{b}}_1^{\mathsf T} + \cdots + \boldsymbol{a}_m\tilde{\boldsymbol{b}}_m^{\mathsf T}.
$$

The first form is "row times column" (inner products); the second is "column times row" ($AB$ written as a sum of $m$ outer products $\boldsymbol{a}_j\tilde{\boldsymbol{b}}_j^{\mathsf T}$). With vectors as the basic units, the rule of multiplication has the same form as the rule for entries. Going further, we cut a matrix horizontally and vertically into blocks:

**Definition 2.5.1 (Block Matrix)** Dividing a matrix by horizontal and vertical lines into submatrices (blocks) and regarding it as a matrix whose entries are these blocks gives a **block matrix** (partitioned matrix). Partition $A$ into $r \times s$ blocks and $B$ into $s \times t$ blocks:

$$
A = \begin{bmatrix} A_{11} & \cdots & A_{1s} \\ \vdots & & \vdots \\ A_{r1} & \cdots & A_{rs} \end{bmatrix}, \qquad B = \begin{bmatrix} B_{11} & \cdots & B_{1t} \\ \vdots & & \vdots \\ B_{s1} & \cdots & B_{st} \end{bmatrix},
$$

where $A_{ij}$ is an $\ell_i \times m_j$ matrix and $B_{jk}$ is an $m_j \times n_k$ matrix.

**Proposition 2.5.1 (Block Operations)** With the partitions above, the $(i, k)$ block of $AB$ is $\sum_{j=1}^s A_{ij}B_{jk}$, and the $(j, i)$ block of $A^{\mathsf T}$ is $A_{ij}^{\mathsf T}$.

Block multiplication requires the row partition of $B$ to match the column partition of $A$, and in each term $A_{ij}B_{jk}$ the left block must stay on the left (blocks do not commute); in the transpose, the positions of the blocks are interchanged and each block is transposed as well. Both rules can be verified by comparing entries. Linear operations on block matrices are evident; partitioning is just another way of writing matrix operations. For example, with $2 \times 2$ blocks,

$$
\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}\begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{bmatrix} = \begin{bmatrix} A_{11}B_{11} + A_{12}B_{21} & A_{11}B_{12} + A_{12}B_{22} \\ A_{21}B_{11} + A_{22}B_{21} & A_{21}B_{12} + A_{22}B_{22} \end{bmatrix}, \qquad
\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}^{\mathsf T} = \begin{bmatrix} A_{11}^{\mathsf T} & A_{21}^{\mathsf T} \\ A_{12}^{\mathsf T} & A_{22}^{\mathsf T} \end{bmatrix}.
$$

**Example 2.5.1** The same matrix can be partitioned in many ways. For

$$
M = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 2 & 2 \\ 0 & 0 & 2 & 2 \end{bmatrix},
$$

cutting after the first two rows and columns gives $\begin{bmatrix} A & O \\ O & B \end{bmatrix}$ with $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ and $B = 2A$; cutting after the first row and column does not reveal this diagonal structure. A good partition exposes the structure of the matrix.

**Definition 2.5.2 (Block Diagonal Matrix)** If a matrix $A$ is partitioned as

$$
A = \begin{bmatrix} A_1 & & & \\ & A_2 & & \\ & & \ddots & \\ & & & A_s \end{bmatrix},
$$

with all off-diagonal blocks equal to zero matrices, then $A$ is called a **block diagonal matrix**, and $A_1, \dots, A_s$ are its diagonal blocks. The diagonal blocks need not be diagonal matrices, nor even square.

Partition $\boldsymbol{x}$ into $\boldsymbol{x}_1, \dots, \boldsymbol{x}_s$ according to the column partition of $A$. Then $A\boldsymbol{x} = [(A_1\boldsymbol{x}_1)^{\mathsf T}\ \cdots\ (A_s\boldsymbol{x}_s)^{\mathsf T}]^{\mathsf T}$: a block diagonal matrix acts independently on each block. When the diagonal blocks are all invertible square matrices, $A$ is invertible, and $A^{-1} = \operatorname{diag}(A_1^{-1}, \dots, A_s^{-1})$ (verify by multiplying).

## 2.6. Elementary Block Matrices and the Schur Complement

Elimination can also be carried out block by block. We consider only $2 \times 2$ partitions, with blocks of orders $n_1$ and $n_2$. By analogy with the three types of elementary matrices, there are three types of elementary block matrices:

| Type | Matrix | Inverse | Left multiplication of $\begin{bmatrix} A_1 \\ A_2 \end{bmatrix}$ | Right multiplication of $[B_1\ B_2]$ |
|---|---|---|---|---|
| Block interchange | $\begin{bmatrix} O & I_{n_2} \\ I_{n_1} & O \end{bmatrix}$ | $\begin{bmatrix} O & I_{n_1} \\ I_{n_2} & O \end{bmatrix}$ | $\begin{bmatrix} A_2 \\ A_1 \end{bmatrix}$ | $[B_2\ B_1]$ |
| Block scaling ($P$ invertible) | $\begin{bmatrix} I_{n_1} & O \\ O & P \end{bmatrix}$ | $\begin{bmatrix} I_{n_1} & O \\ O & P^{-1} \end{bmatrix}$ | $\begin{bmatrix} A_1 \\ PA_2 \end{bmatrix}$ | $[B_1\ B_2P]$ |
| Block replacement | $\begin{bmatrix} I_{n_1} & M \\ O & I_{n_2} \end{bmatrix}$ | $\begin{bmatrix} I_{n_1} & -M \\ O & I_{n_2} \end{bmatrix}$ | $\begin{bmatrix} A_1 + MA_2 \\ A_2 \end{bmatrix}$ | $[B_1\ \ B_1M + B_2]$ |

In the block interchange matrix, the positions of $I_{n_1}$ and $I_{n_2}$ are determined by the partition of the matrix being multiplied.

**Example 2.6.1 (Block Upper Triangular Matrix)** Let $A = \begin{bmatrix} A_{11} & A_{12} \\ O & A_{22} \end{bmatrix}$ with $A_{11}, A_{22}$ square. Then $A$ is invertible if and only if $A_{11}$ and $A_{22}$ are both invertible, in which case

$$
\begin{bmatrix} A_{11} & A_{12} \\ O & A_{22} \end{bmatrix}^{-1} = \begin{bmatrix} A_{11}^{-1} & -A_{11}^{-1}A_{12}A_{22}^{-1} \\ O & A_{22}^{-1} \end{bmatrix}.
$$

If $A_{11}$ is not invertible, take a nonzero solution of $A_{11}\boldsymbol{x}_1 = \boldsymbol{0}$; then $A\begin{bmatrix} \boldsymbol{x}_1 \\ \boldsymbol{0} \end{bmatrix} = \boldsymbol{0}$. If $A_{11}$ is invertible but $A_{22}$ is not, take a nonzero solution of $A_{22}\boldsymbol{y} = \boldsymbol{0}$; then $A\begin{bmatrix} -A_{11}^{-1}A_{12}\boldsymbol{y} \\ \boldsymbol{y} \end{bmatrix} = \boldsymbol{0}$. In both cases $A$ is not invertible. If both are invertible, perform block Gauss–Jordan elimination on $[A\ I]$: first multiply on the left by $\operatorname{diag}(A_{11}^{-1}, A_{22}^{-1})$ to turn the diagonal blocks into identity matrices, then multiply on the left by $\begin{bmatrix} I & -A_{11}^{-1}A_{12} \\ O & I \end{bmatrix}$ to clear the upper right block; this gives the formula above. Note that the order of block multiplication cannot be changed. Block lower triangular matrices are handled in the same way.

A general $2 \times 2$ block matrix can first be eliminated to block triangular form.

**Definition 2.6.1 (Schur Complement)** Let $A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}$ with $A_{11}, A_{22}$ square. If $A_{11}$ is invertible, $A_{22} - A_{21}A_{11}^{-1}A_{12}$ is called the **Schur complement** of $A_{11}$ in $A$; if $A_{22}$ is invertible, $A_{11} - A_{12}A_{22}^{-1}A_{21}$ is called the Schur complement of $A_{22}$ in $A$.

The Schur complement is exactly the block left over after block elimination:

$$
\begin{bmatrix} I & O \\ -A_{21}A_{11}^{-1} & I \end{bmatrix}\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} = \begin{bmatrix} A_{11} & A_{12} \\ O & A_{22} - A_{21}A_{11}^{-1}A_{12} \end{bmatrix}, \tag{2.1}
$$

$$
\begin{bmatrix} I & -A_{12}A_{22}^{-1} \\ O & I \end{bmatrix}\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} = \begin{bmatrix} A_{11} - A_{12}A_{22}^{-1}A_{21} & O \\ A_{21} & A_{22} \end{bmatrix}. \tag{2.2}
$$

**Proposition 2.6.1** In the notation of Definition 2.6.1, if $A_{11}$ is invertible, then $A$ is invertible if and only if $S = A_{22} - A_{21}A_{11}^{-1}A_{12}$ is invertible, in which case

$$
A^{-1} = \begin{bmatrix} I & -A_{11}^{-1}A_{12} \\ O & I \end{bmatrix}\begin{bmatrix} A_{11}^{-1} & O \\ O & S^{-1} \end{bmatrix}\begin{bmatrix} I & O \\ -A_{21}A_{11}^{-1} & I \end{bmatrix} = \begin{bmatrix} A_{11}^{-1} + A_{11}^{-1}A_{12}S^{-1}A_{21}A_{11}^{-1} & -A_{11}^{-1}A_{12}S^{-1} \\ -S^{-1}A_{21}A_{11}^{-1} & S^{-1} \end{bmatrix}. \tag{2.3}
$$

If $A_{22}$ is invertible, then $A$ is invertible if and only if $T = A_{11} - A_{12}A_{22}^{-1}A_{21}$ is invertible, in which case

$$
A^{-1} = \begin{bmatrix} I & O \\ -A_{22}^{-1}A_{21} & I \end{bmatrix}\begin{bmatrix} T^{-1} & O \\ O & A_{22}^{-1} \end{bmatrix}\begin{bmatrix} I & -A_{12}A_{22}^{-1} \\ O & I \end{bmatrix} = \begin{bmatrix} T^{-1} & -T^{-1}A_{12}A_{22}^{-1} \\ -A_{22}^{-1}A_{21}T^{-1} & A_{22}^{-1} + A_{22}^{-1}A_{21}T^{-1}A_{12}A_{22}^{-1} \end{bmatrix}. \tag{2.4}
$$

**Proof** We prove only the first statement. The first factor on the left of Eq. (2.1) is invertible, so $A$ is invertible if and only if the block upper triangular matrix on the right is invertible, which by Example 2.6.1 happens if and only if $A_{11}$ and $S$ are both invertible. Invert both sides of Eq. (2.1) and use Example 2.6.1 to write the inverse of the block upper triangular matrix as

$$
\begin{bmatrix} A_{11} & A_{12} \\ O & S \end{bmatrix}^{-1} = \begin{bmatrix} I & -A_{11}^{-1}A_{12} \\ O & I \end{bmatrix}\begin{bmatrix} A_{11}^{-1} & O \\ O & S^{-1} \end{bmatrix};
$$

this gives the factored form of Eq. (2.3), and multiplying out the three factors gives the right-hand side. $\square$

## 2.7. The Sherman–Morrison–Woodbury Formula

When $A_{11}$, $A_{22}$ and both Schur complements are invertible, Eqs. (2.3) and (2.4) are two expressions for the same $A^{-1}$. Comparing the upper left blocks gives

$$
(A_{11} - A_{12}A_{22}^{-1}A_{21})^{-1} = A_{11}^{-1} + A_{11}^{-1}A_{12}(A_{22} - A_{21}A_{11}^{-1}A_{12})^{-1}A_{21}A_{11}^{-1}. \tag{2.5}
$$

This formula gives the inverse of an invertible matrix $A_{11}$ after a correction term $-A_{12}A_{22}^{-1}A_{21}$ has been added. Taking $A_{11} = A$, $A_{12} = U$, $A_{21} = -V$ and $A_{22} = C^{-1}$ gives the usual form:

**Theorem 2.7.1 (Woodbury Formula)** Let $A$ be an invertible matrix of order $n$, $C$ an invertible matrix of order $k$, and $U$, $V$ matrices of sizes $n \times k$ and $k \times n$ respectively. If $C^{-1} + VA^{-1}U$ is invertible, then $A + UCV$ is invertible and

$$
(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1}.
$$

**Proof** Let $M = \begin{bmatrix} A & U \\ -V & C^{-1} \end{bmatrix}$. The Schur complement of $A$ in $M$ is $C^{-1} + VA^{-1}U$, so $M$ is invertible by Proposition 2.6.1; $C^{-1}$ is invertible and its Schur complement in $M$ is $A + UCV$, so by Proposition 2.6.1 again this matrix is invertible too. Thus all the conditions for Eq. (2.5) hold, and substituting gives the formula. $\square$

This formula is also called the Sherman–Morrison–Woodbury formula. Its value lies in the case $k \ll n$: if $A^{-1}$ is known and $A$ undergoes a modification of rank at most $k$, we only need to invert a matrix of order $k$ instead of inverting a matrix of order $n$ from scratch. The case $k = 1$ is the most frequently used:

**Theorem 2.7.2 (Sherman–Morrison Formula)** Let $A$ be an invertible matrix of order $n$ and $\boldsymbol{u}, \boldsymbol{v} \in \mathbb{R}^n$. Then $A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T}$ is invertible if and only if $1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u} \ne 0$, in which case

$$
(A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T})^{-1} = A^{-1} - \frac{A^{-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1}}{1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}}.
$$

**Proof** Consider $M = \begin{bmatrix} A & \boldsymbol{u} \\ -\boldsymbol{v}^{\mathsf T} & 1 \end{bmatrix}$. The Schur complement of $A$ is the number $1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}$, and the Schur complement of the lower right entry $1$ is $A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T}$. By Proposition 2.6.1, the invertibility of either one is equivalent to the invertibility of $M$, which proves the condition. The formula can be verified directly: with $\beta = 1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}$,

$$
(A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T})\left(A^{-1} - \frac{A^{-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1}}{\beta}\right) = I + \boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1} - \frac{\boldsymbol{u}(1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u})\boldsymbol{v}^{\mathsf T}A^{-1}}{\beta} = I. \qquad \square
$$

Taking $A = I$: $I + \boldsymbol{u}\boldsymbol{v}^{\mathsf T}$ is invertible if and only if $1 + \boldsymbol{v}^{\mathsf T}\boldsymbol{u} \ne 0$, and then $(I + \boldsymbol{u}\boldsymbol{v}^{\mathsf T})^{-1} = I - \dfrac{\boldsymbol{u}\boldsymbol{v}^{\mathsf T}}{1 + \boldsymbol{v}^{\mathsf T}\boldsymbol{u}}$.

**Remark 2.7.1** If the lower right entry of $M$ is replaced by a nonzero number $a$, the same argument shows that $A + \frac1a\boldsymbol{u}\boldsymbol{v}^{\mathsf T}$ is invertible if and only if $a + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u} \ne 0$, in which case

$$
\left(A + \frac1a\boldsymbol{u}\boldsymbol{v}^{\mathsf T}\right)^{-1} = A^{-1} - \frac{A^{-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1}}{a + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}}.
$$

This is not a new result, only Theorem 2.7.2 applied to $\frac1a\boldsymbol{u}$ and $\boldsymbol{v}$; the condition $a \ne 0$ is needed for $\frac1a$ to make sense.

**Example 2.7.1 (Perturbing a Single Entry)** Let $A$ be invertible and change its $(1, 1)$ entry from $a_{11}$ to $a_{11} + \delta$; the new matrix is $A + \delta\boldsymbol{e}_1\boldsymbol{e}_1^{\mathsf T}$. By Theorem 2.7.2 it is invertible if and only if $1 + \delta\,\boldsymbol{e}_1^{\mathsf T}A^{-1}\boldsymbol{e}_1 \ne 0$. Hence the new matrix is invertible whenever $|\delta| < 1/|\boldsymbol{e}_1^{\mathsf T}A^{-1}\boldsymbol{e}_1|$ (if $\boldsymbol{e}_1^{\mathsf T}A^{-1}\boldsymbol{e}_1 = 0$, it is invertible for every $\delta$), and

$$
(A + \delta\boldsymbol{e}_1\boldsymbol{e}_1^{\mathsf T})^{-1} = A^{-1} - \frac{\delta}{1 + \delta\,\boldsymbol{e}_1^{\mathsf T}A^{-1}\boldsymbol{e}_1}A^{-1}\boldsymbol{e}_1\boldsymbol{e}_1^{\mathsf T}A^{-1}.
$$

The change in the inverse depends only on the first column $A^{-1}\boldsymbol{e}_1$ and the first row $\boldsymbol{e}_1^{\mathsf T}A^{-1}$ of $A^{-1}$. In general, if the $(i, j)$ entry changes by $\delta$,

$$
(A + \delta\boldsymbol{e}_i\boldsymbol{e}_j^{\mathsf T})^{-1} = A^{-1} - \frac{\delta}{1 + \delta\,\boldsymbol{e}_j^{\mathsf T}A^{-1}\boldsymbol{e}_i}A^{-1}\boldsymbol{e}_i\boldsymbol{e}_j^{\mathsf T}A^{-1},
$$

and the change depends only on the $i$-th column and the $j$-th row of $A^{-1}$. Updating the inverse in this way costs only $O(n^2)$ operations, whereas inverting again costs about $2n^3$.

## 2.8. The LU Decomposition

Suppose that Gaussian elimination on a square matrix $A$ of order $n$ requires no row interchanges (elimination without pivoting). Then downward elimination consists of successive multiplications on the left by replacement matrices:

$$
(E_{n,n-1})\cdots(E_{n2}\cdots E_{32})(E_{n1}\cdots E_{31}E_{21})A = U,
$$

where $E_{ji}$ ($j > i$) adds some multiple of row $i$ to row $j$ and is unit lower triangular, and $U$, the row echelon form of $A$, is upper triangular. By Property 2.3.1 and Proposition 2.3.2, products and inverses of unit lower triangular matrices are again unit lower triangular. Denoting the product of these replacement matrices by $L^{-1}$, we have $L^{-1}A = U$, that is, $A = LU$.

**Definition 2.8.1 (LU Decomposition)** Writing a square matrix $A$ as $A = LU$, where $L$ is unit lower triangular and $U$ is upper triangular, is called an **LU decomposition** of $A$.

**Theorem 2.8.1** If a square matrix $A$ of order $n$ can be reduced to row echelon form using replacements only (elimination without row interchanges), then there are a unit lower triangular matrix $L$ of order $n$ and an upper triangular matrix $U$ of order $n$ such that $A = LU$.

Since $L$ is always invertible, $A$ is invertible if and only if $U = L^{-1}A$ is invertible. With an LU decomposition, the system $A\boldsymbol{x} = \boldsymbol{b}$ reduces to two triangular systems

$$
L\boldsymbol{y} = \boldsymbol{b}\ \ (\text{forward substitution}), \qquad U\boldsymbol{x} = \boldsymbol{y}\ \ (\text{back substitution}).
$$

Not every square matrix has an LU decomposition. For example, $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ \ell & 1 \end{bmatrix}\begin{bmatrix} u_{11} & u_{12} \\ 0 & u_{22} \end{bmatrix}$ forces $u_{11} = 0$, and then the lower left entry is $\ell u_{11} = 0 \ne 1$, a contradiction.

**Example 2.8.1** A singular matrix may also have an LU decomposition:

$$
\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 3 & 0 \end{bmatrix} = \begin{bmatrix} 1 & & & \\ 0 & 1 & & \\ 0 & 2 & 1 & \\ 0 & 3 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}.
$$

Here the last two rows of $U$ are zero, the $(4, 3)$ entry of $L$ can be chosen arbitrarily, and the decomposition is not unique.

## 2.9. Existence and Uniqueness of the LU Decomposition of an Invertible Matrix

**Definition 2.9.1 (Leading Principal Submatrix)** The upper left $k \times k$ block of a square matrix $A$ is called the $k$-th **leading principal submatrix** of $A$, denoted by $A_k$ ($k = 1, \dots, n$).

**Theorem 2.9.1 (LU Decomposition of an Invertible Matrix)** An invertible matrix $A$ of order $n$ has an LU decomposition if and only if all its leading principal submatrices are invertible. In that case the LU decomposition of $A$ is unique.

**Proof** Necessity: let $A = LU$. Then $L$ and $U$ are both invertible, and their diagonal entries are all nonzero. For each $k$, partition

$$
A = \begin{bmatrix} L_{11} & O \\ L_{21} & L_{22} \end{bmatrix}\begin{bmatrix} U_{11} & U_{12} \\ O & U_{22} \end{bmatrix} = \begin{bmatrix} L_{11}U_{11} & L_{11}U_{12} \\ L_{21}U_{11} & L_{21}U_{12} + L_{22}U_{22} \end{bmatrix},
$$

where $L_{11}$ and $U_{11}$ are triangular matrices of order $k$ with nonzero diagonal entries, hence invertible. Therefore the $k$-th leading principal submatrix $A_k = L_{11}U_{11}$ is invertible.

Sufficiency: induction on $n$. For $n = 1$, $A = [a] = [1][a]$. Suppose the statement holds for order $n-1$, and partition $A$ as $A = \begin{bmatrix} A_{n-1} & \boldsymbol{x} \\ \boldsymbol{y}^{\mathsf T} & a \end{bmatrix}$. $A_{n-1}$ is invertible, and its leading principal submatrices are also leading principal submatrices of $A$, hence invertible; by the induction hypothesis $A_{n-1} = L_1U_1$ with $L_1, U_1$ invertible. By block elimination,

$$
A = \begin{bmatrix} I_{n-1} & \boldsymbol{0} \\ \boldsymbol{y}^{\mathsf T}A_{n-1}^{-1} & 1 \end{bmatrix}\begin{bmatrix} A_{n-1} & \boldsymbol{x} \\ \boldsymbol{0}^{\mathsf T} & a - \boldsymbol{y}^{\mathsf T}A_{n-1}^{-1}\boldsymbol{x} \end{bmatrix} = \begin{bmatrix} L_1 & \boldsymbol{0} \\ \boldsymbol{y}^{\mathsf T}U_1^{-1} & 1 \end{bmatrix}\begin{bmatrix} U_1 & L_1^{-1}\boldsymbol{x} \\ \boldsymbol{0}^{\mathsf T} & a - \boldsymbol{y}^{\mathsf T}A_{n-1}^{-1}\boldsymbol{x} \end{bmatrix},
$$

where the first factor on the right is unit lower triangular and the second is upper triangular (the last equality can be verified by multiplying out).

Uniqueness: let $A = L_1U_1 = L_2U_2$, with all four factors invertible. Then $L_2^{-1}L_1 = U_2U_1^{-1}$. The left side is unit lower triangular and the right side is upper triangular, so both sides equal the identity matrix, and $L_1 = L_2$, $U_1 = U_2$. $\square$

## 2.10. Computing the LU Decomposition

The LU decomposition is just another record of Gaussian elimination: $U = L^{-1}A$ is a row echelon form of $A$. The most direct algorithm computes $L^{-1}$ along the way.

**Algorithm 2.10.1 (Two-Step Method)**

1. Perform elimination without row interchanges on $[A\ I]$ (using only replacements that add multiples of upper rows to lower rows) to obtain $[U\ L^{-1}]$;
2. perform Gauss–Jordan elimination on $[L^{-1}\ I]$ to obtain $[I\ L]$.

**Example 2.10.1** For $A = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 2 & 3 & 4 \\ 1 & 3 & 6 & 10 \\ 1 & 4 & 10 & 20 \end{bmatrix}$, the first step gives

$$
U = \begin{bmatrix} 1 & 1 & 1 & 1 \\ & 1 & 2 & 3 \\ & & 1 & 3 \\ & & & 1 \end{bmatrix}, \qquad L^{-1} = \begin{bmatrix} 1 & & & \\ -1 & 1 & & \\ 1 & -2 & 1 & \\ -1 & 3 & -3 & 1 \end{bmatrix},
$$

and the second step gives $L = \begin{bmatrix} 1 & & & \\ 1 & 1 & & \\ 1 & 2 & 1 & \\ 1 & 3 & 3 & 1 \end{bmatrix}$. Here $U = L^{\mathsf T}$, because $A$ is symmetric and the diagonal entries of $U$ are all $1$ (see Corollary 2.11.1); for a general symmetric matrix we only have $U = DL^{\mathsf T}$, where $D$ is the diagonal part of $U$.

The two-step method performs elimination twice. Exploiting the structure of $L^{-1}$, we can do it in one pass. Without row interchanges, let $L_j^{-1} = E_{nj}\cdots E_{j+1,j}$ ($j = 1, \dots, n-1$) be the product of the replacement matrices used in the $j$-th step of elimination:

$$
L_j^{-1} = \begin{bmatrix} 1 & & & & & \\ & \ddots & & & & \\ & & 1 & & & \\ & & -\ell_{j+1,j} & 1 & & \\ & & \vdots & & \ddots & \\ & & -\ell_{nj} & & & 1 \end{bmatrix}.
$$

Only its $j$-th column has nonzero off-diagonal entries; such a matrix is called an elementary unit lower triangular matrix (a Gauss transformation). Multiplying on the left by $L_j^{-1}$ adds $-\ell_{ij}$ times row $j$ to row $i$ ($i > j$). Let $\boldsymbol{\ell}_j = [0\ \cdots\ 0\ \ell_{j+1,j}\ \cdots\ \ell_{nj}]^{\mathsf T}$ (with the first $j$ components zero). Then

$$
L_j^{-1} = I_n - \boldsymbol{\ell}_j\boldsymbol{e}_j^{\mathsf T}, \qquad L_j = I_n + \boldsymbol{\ell}_j\boldsymbol{e}_j^{\mathsf T},
$$

where the latter can be verified directly from $\boldsymbol{e}_j^{\mathsf T}\boldsymbol{\ell}_j = 0$. The elimination $L_{n-1}^{-1}\cdots L_2^{-1}L_1^{-1}A = U$ gives $A = LU$ with

$$
L = L_1L_2\cdots L_{n-1} = (I_n + \boldsymbol{\ell}_1\boldsymbol{e}_1^{\mathsf T})\cdots(I_n + \boldsymbol{\ell}_{n-1}\boldsymbol{e}_{n-1}^{\mathsf T}) = I_n + \boldsymbol{\ell}_1\boldsymbol{e}_1^{\mathsf T} + \cdots + \boldsymbol{\ell}_{n-1}\boldsymbol{e}_{n-1}^{\mathsf T} = \begin{bmatrix} 1 & & & \\ \ell_{21} & 1 & & \\ \vdots & \vdots & \ddots & \\ \ell_{n1} & \ell_{n2} & \cdots & 1 \end{bmatrix}.
$$

When the product is expanded, every cross term $\boldsymbol{\ell}_i\boldsymbol{e}_i^{\mathsf T}\boldsymbol{\ell}_j\boldsymbol{e}_j^{\mathsf T}$ ($i < j$) contains the factor $\boldsymbol{e}_i^{\mathsf T}\boldsymbol{\ell}_j = 0$. In other words, the entries of $L$ are exactly the multipliers used during elimination, and no extra computation is needed. Note the order: the entries of $L^{-1} = L_{n-1}^{-1}\cdots L_1^{-1}$ are not $-\ell_{ij}$ (in Example 2.10.1 the $(3, 1)$ entry of $L^{-1}$ is $1$, not $-1$).

**Algorithm 2.10.2 (LU Decomposition in One Pass)** Input: a square matrix $A$ of order $n$; set $A^{(1)} = A$. For $j = 1, \dots, n-1$:

1. if the pivot $a_{jj}^{(j)} = 0$, elimination without row interchanges cannot proceed (a row interchange is needed; see Section 2.11);
2. for $i = j+1, \dots, n$, compute the multiplier $\ell_{ij} = a_{ij}^{(j)} / a_{jj}^{(j)}$ and subtract $\ell_{ij}$ times row $j$ from row $i$, which gives $A^{(j+1)}$.

At the end, $U = A^{(n)}$, and $L$ is the unit lower triangular matrix whose strictly lower triangular part consists of the $\ell_{ij}$. In practice the multiplier $\ell_{ij}$ is stored in the position that has just been eliminated to zero, so no extra storage is needed.

**Example 2.10.2** For the matrix of Example 2.10.1:

$$
A^{(2)} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ & 1 & 2 & 3 \\ & 2 & 5 & 9 \\ & 3 & 9 & 19 \end{bmatrix}\ (\ell_{21} = \ell_{31} = \ell_{41} = 1), \quad
A^{(3)} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ & 1 & 2 & 3 \\ & & 1 & 3 \\ & & 3 & 10 \end{bmatrix}\ (\ell_{32} = 2,\ \ell_{42} = 3), \quad
A^{(4)} = U\ (\ell_{43} = 3),
$$

and reading off the lower triangular part of $L$ column by column as $(1, 1, 1)$, $(2, 3)$, $(3)$ reproduces Example 2.10.1.

Step $j$ of Algorithm 2.10.2 updates $(n-j)^2$ entries, each with one multiplication and one subtraction, for a total of about $\frac23n^3$ floating-point operations; afterwards each system costs only two triangular solves, about $2n^2$. The left panel of the figure below compares the costs of several computations; the right panel shows that when many right-hand sides $\boldsymbol{b}$ must be solved with the same coefficient matrix, "factor once, substitute many times" is far cheaper than eliminating anew each time.

![Left: floating-point operation counts of the LU decomposition, of the two triangular solves and of Gauss–Jordan inversion (gray lines are the asymptotic formulas); right: total cost of solving for k right-hand sides when n = 200](./plots/lu-operation-counts.py)

## 2.11. The LDU and PLU Decompositions

Factoring the diagonal entries out of $U$ in the LU decomposition gives a more symmetric form.

**Theorem 2.11.1 (LDU Decomposition)** If an invertible matrix $A$ of order $n$ has an LU decomposition, then there is a unique triple of a unit lower triangular matrix $L$, a diagonal matrix $D$ with nonzero diagonal entries and a unit upper triangular matrix $U$, all of order $n$, such that $A = LDU$; this is called the LDU decomposition of $A$.

**Proof** Existence: let $A = L\tilde{U}$; $\tilde{U}$ is invertible and its diagonal entries are nonzero. Put $D = \operatorname{diag}(\tilde{u}_{11}, \dots, \tilde{u}_{nn})$ and $U = D^{-1}\tilde{U}$ (that is, scale the pivots of the echelon form to $1$ by row scalings). Then $U$ is unit upper triangular and $A = LDU$. Uniqueness: let $A = L_1D_1U_1 = L_2D_2U_2$. Then $L_2^{-1}L_1 = D_2U_2U_1^{-1}D_1^{-1}$; the left side is unit lower triangular and the right side upper triangular, so both equal $I$ and $L_1 = L_2$. Then $D_2^{-1}D_1 = U_2U_1^{-1}$; the left side is diagonal and the right side unit upper triangular, so both equal $I$, and $D_1 = D_2$, $U_1 = U_2$. $\square$

**Corollary 2.11.1** If a symmetric matrix $A$ has an LDU decomposition $A = LDU$, then $U = L^{\mathsf T}$, that is, $A = LDL^{\mathsf T}$.

**Proof** $A = A^{\mathsf T} = U^{\mathsf T}DL^{\mathsf T}$ is also an LDU decomposition of $A$ ($U^{\mathsf T}$ is unit lower triangular and $L^{\mathsf T}$ is unit upper triangular), so $L = U^{\mathsf T}$ by uniqueness. $\square$

Thus in the LU decomposition of a symmetric matrix the upper triangular factor is $DL^{\mathsf T}$; only when all pivots equal $1$ ($D = I$) do we have $U = L^{\mathsf T}$. For a symmetric matrix we need only compute $L$ and $D$, which roughly halves the work; this is also the starting point of the Cholesky decomposition in [Chapter 7](/2.1.7).

A general invertible matrix may run into a zero pivot during elimination without row interchanges, and then rows must be interchanged.

**Example 2.11.1** Eliminating $A = \begin{bmatrix} 1 & -1 & 1 \\ -1 & 1 & 0 \\ 2 & -1 & 2 \end{bmatrix}$, after the replacements of the first step the $(2, 2)$ position is zero, and rows 2 and 3 must be interchanged:

$$
A \xrightarrow{\text{replacement}} \begin{bmatrix} 1 & -1 & 1 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix} \xrightarrow{\text{interchange}} \begin{bmatrix} 1 & -1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}.
$$

If the interchange is applied to $A$ first, only replacements are needed: $P_{23}A = \begin{bmatrix} 1 & -1 & 1 \\ 2 & -1 & 2 \\ -1 & 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & & \\ 2 & 1 & \\ -1 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & -1 & 1 \\ & 1 & 0 \\ & & 1 \end{bmatrix}$, and hence $A = P_{23}LU$.

**Theorem 2.11.2 (PLU Decomposition)** For every invertible matrix $A$ of order $n$ there are a permutation matrix $P$, a unit lower triangular matrix $L$ and an upper triangular matrix $U$ with nonzero diagonal entries, all of order $n$, such that $A = PLU$.

**Proof** Induction on $n$; the case $n = 1$ is obvious. Suppose the statement holds for order $n-1$. Since $A$ is invertible, its first column is not entirely zero; take $a_{i1} \ne 0$ and let $P_1 = P_{1i}$ ($P_1 = I$ if $i = 1$). Then $P_1A = \begin{bmatrix} a & \boldsymbol{w}^{\mathsf T} \\ \boldsymbol{v} & A' \end{bmatrix}$ with $a \ne 0$. Block elimination gives

$$
P_1A = \begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{v}/a & I \end{bmatrix}\begin{bmatrix} a & \boldsymbol{w}^{\mathsf T} \\ \boldsymbol{0} & S \end{bmatrix}, \qquad S = A' - \frac{\boldsymbol{v}\boldsymbol{w}^{\mathsf T}}{a}.
$$

By Proposition 2.6.1 the Schur complement $S$ is invertible, and by the induction hypothesis $S = P'L'U'$. Multiplying out verifies

$$
P_1A = \begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & P' \end{bmatrix}\begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ P'^{\mathsf T}\boldsymbol{v}/a & L' \end{bmatrix}\begin{bmatrix} a & \boldsymbol{w}^{\mathsf T} \\ \boldsymbol{0} & U' \end{bmatrix},
$$

(using $P'P'^{\mathsf T} = I$). Hence $A = PLU$, where $P = P_1^{\mathsf T}\operatorname{diag}(1, P')$ is a permutation matrix (Proposition 2.3.3), $L$ is unit lower triangular and $U$ is upper triangular with nonzero diagonal entries. $\square$

The proof only requires the pivot to be nonzero at each step. In numerical computation one chooses at each step the entry of largest absolute value in the current column as the pivot (partial pivoting) in order to limit the growth of rounding errors; numerical software such as `scipy.linalg.lu` computes exactly this PLU decomposition.

## Summary

The main thread of this chapter is "elimination = multiplication on the left by elementary matrices": invertibility, inversion and the LU decomposition are all consequences of this point of view.

| Category | Content |
|---|---|
| Definitions | Elementary matrices $P_{ij}, E_{ii;k}, E_{ji;k}$ (Definition 2.1.1); invertible maps and invertible linear transformations (Definitions 2.2.1, 2.2.2); invertible matrices, inverse matrices, singular matrices (Definition 2.2.3); permutation matrices (Definition 2.3.1); diagonally dominant matrices (Definition 2.3.2); row equivalence (Definition 2.4.1); block matrices, block diagonal matrices (Definitions 2.5.1, 2.5.2); Schur complement (Definition 2.6.1); LU decomposition (Definition 2.8.1); leading principal submatrices (Definition 2.9.1) |
| Theorems | Rows on the left, columns on the right (Proposition 2.1.1); properties of invertible matrices (Proposition 2.2.3); six equivalent conditions for invertibility (Theorem 2.3.1); a one-sided inverse is an inverse (Proposition 2.3.1); products and inverses of triangular matrices (Property 2.3.1, Proposition 2.3.2); diagonally dominant matrices are invertible (Proposition 2.3.4); row equivalence $\Leftrightarrow PA = B$ (Proposition 2.4.1); block inversion (Proposition 2.6.1); the Woodbury and Sherman–Morrison formulas (Theorems 2.7.1, 2.7.2); existence and uniqueness of the LU decomposition of an invertible matrix (Theorem 2.9.1); LDU decomposition (Theorem 2.11.1); $A = LDL^{\mathsf T}$ for symmetric matrices (Corollary 2.11.1); PLU decomposition (Theorem 2.11.2) |
| Algorithms | Gauss–Jordan inversion $[A\ I] \to [I\ A^{-1}]$ (Algorithm 2.3.1, about $2n^3$ operations); the two-step method (Algorithm 2.10.1) and the one-pass method (Algorithm 2.10.2, about $\frac23n^3$ operations, then about $2n^2$ per right-hand side) for the LU decomposition |

| Decomposition | Form | Existence | Uniqueness |
|---|---|---|---|
| LU | $A = LU$, $L$ unit lower triangular, $U$ upper triangular | elimination without row interchanges is possible; for invertible $A$, if and only if all leading principal submatrices are invertible | unique for invertible $A$ |
| LDU | $A = LDU$, $L$ and $U$ unit triangular, $D$ diagonal | $A$ invertible with an LU decomposition | unique; $U = L^{\mathsf T}$ for symmetric $A$ |
| PLU | $A = PLU$, $P$ a permutation matrix | every invertible matrix | not unique in general |
