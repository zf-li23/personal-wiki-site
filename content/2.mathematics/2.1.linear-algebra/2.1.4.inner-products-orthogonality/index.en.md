---
title: Inner Products and Orthogonality
source_hash: e29728dd50e4
---

The first three chapters used only the linear operations on vectors: whether the system $A\boldsymbol{x} = \boldsymbol{b}$ is solvable and how large its solution set is are both answered by the **rank** and the four fundamental subspaces. When $\boldsymbol{b} \notin \mathcal{R}(A)$ and the system has no solution, however, we still want the $\boldsymbol{x}$ that comes "closest", and for that we need to measure lengths and angles. This chapter introduces the inner product on $\mathbb{R}^n$, uses it to define length, angle and orthogonality, and then follows a single theme, "reduce the problem to the orthogonal case": orthonormal bases make coordinates a matter of inner products; Gram–Schmidt orthogonalization turns any basis into an orthonormal one, and in matrix form it is the QR decomposition; orthogonal complements and orthogonal projections give a geometric description of "best approximation"; finally, we solve least squares problems by the normal equations or by the QR decomposition and apply them to data fitting.

This chapter relies on the **LU decomposition** of Chapter 2 and on subspaces, dimension and rank from Chapter 3; orthogonal matrices, the QR decomposition and orthogonal projections underlie the spectral decomposition of real symmetric matrices and the singular value decomposition in Chapter 7. Here we treat only the standard inner product on $\mathbb{R}^n$; general inner product spaces, Euclidean spaces and unitary spaces are the subject of [Chapter 12](/2.1.12). Least squares and orthogonal projection matrices are also the core tools of linear regression in statistics.

## 4.1. Inner Products, Lengths and Angles

**Example 4.1.1 (Best Approximation in the Plane)** Consider the system $\boldsymbol{a}x = \boldsymbol{b}$ with $\boldsymbol{a} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$, $\boldsymbol{b} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$ and $x \in \mathbb{R}$. It clearly has no solution. As the next best thing, we look for $\hat{x}$ that minimizes the length of $\boldsymbol{b} - \hat{x}\boldsymbol{a}$:

$$
\|\boldsymbol{b} - \hat{x}\boldsymbol{a}\| = \min_{x \in \mathbb{R}} \|\boldsymbol{b} - x\boldsymbol{a}\|, \qquad \|\boldsymbol{a}\| = \sqrt{a_1^2 + a_2^2} = \sqrt{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}.
$$

Geometrically, we drop a perpendicular from $\boldsymbol{b}$ to the line $\operatorname{span}(\boldsymbol{a}) = \{x\boldsymbol{a} \mid x \in \mathbb{R}\}$: we decompose $\boldsymbol{b} = \hat{x}\boldsymbol{a} + \boldsymbol{r}$ and require $\boldsymbol{r}$ to be perpendicular to $\boldsymbol{a}$, that is, $0 = \boldsymbol{a}^{\mathsf T}\boldsymbol{r} = \boldsymbol{a}^{\mathsf T}(\boldsymbol{b} - \hat{x}\boldsymbol{a})$. Hence

$$
\hat{x} = \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \frac{8}{5}, \qquad \boldsymbol{r} = \boldsymbol{b} - \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\boldsymbol{a} = \frac{6}{5}\begin{bmatrix} -1 \\ 2 \end{bmatrix}, \qquad \|\boldsymbol{r}\| = \frac{6}{\sqrt{5}}.
$$

Both "length" and "perpendicular" in this example can be expressed through $\boldsymbol{a}^{\mathsf T}\boldsymbol{b}$. We now generalize this to $\mathbb{R}^n$.

### 4.1.1. Inner Products and Lengths

**Definition 4.1.1 (Inner Product)** For vectors $\boldsymbol{a} = [a_i]$, $\boldsymbol{b} = [b_i]$ in $\mathbb{R}^n$, their **inner product** (also called the standard inner product or dot product) is

$$
\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \sum_{i=1}^n a_i b_i \in \mathbb{R}.
$$

**Property 4.1.1** The inner product satisfies:

1. symmetry: $\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \boldsymbol{b}^{\mathsf T}\boldsymbol{a}$;
2. bilinearity: $\boldsymbol{a}^{\mathsf T}(k_1\boldsymbol{b}_1 + k_2\boldsymbol{b}_2) = k_1\boldsymbol{a}^{\mathsf T}\boldsymbol{b}_1 + k_2\boldsymbol{a}^{\mathsf T}\boldsymbol{b}_2$ and $(k_1\boldsymbol{a}_1 + k_2\boldsymbol{a}_2)^{\mathsf T}\boldsymbol{b} = k_1\boldsymbol{a}_1^{\mathsf T}\boldsymbol{b} + k_2\boldsymbol{a}_2^{\mathsf T}\boldsymbol{b}$;
3. positive definiteness: $\boldsymbol{a}^{\mathsf T}\boldsymbol{a} \ge 0$, with $\boldsymbol{a}^{\mathsf T}\boldsymbol{a} = 0$ if and only if $\boldsymbol{a} = \boldsymbol{0}$.

These three properties are the starting point of everything that follows; [Chapter 12](/2.1.12) takes them as axioms to define inner products on general vector spaces.

**Definition 4.1.2 (Length of a Vector)** The **length** (Euclidean norm) of a vector $\boldsymbol{a} \in \mathbb{R}^n$ is

$$
\|\boldsymbol{a}\| = \sqrt{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}.
$$

A vector of length $1$ is called a unit vector. For a nonzero vector $\boldsymbol{a}$, the vector $\boldsymbol{a}/\|\boldsymbol{a}\|$ is a unit vector, called the normalization of $\boldsymbol{a}$; $\|\boldsymbol{a} - \boldsymbol{b}\|$ is called the distance between $\boldsymbol{a}$ and $\boldsymbol{b}$.

**Property 4.1.2** Length satisfies $\|\boldsymbol{a}\| = 0 \iff \boldsymbol{a} = \boldsymbol{0}$, homogeneity $\|k\boldsymbol{a}\| = |k|\,\|\boldsymbol{a}\|$, and the polarization identity

$$
\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \frac{1}{4}\left(\|\boldsymbol{a} + \boldsymbol{b}\|^2 - \|\boldsymbol{a} - \boldsymbol{b}\|^2\right).
$$

The polarization identity shows that the inner product is completely determined by lengths; we will use this to characterize orthogonal matrices (Theorem 4.3.2).

### 4.1.2. The Cauchy–Schwarz Inequality and Angles

**Theorem 4.1.1 (Cauchy–Schwarz Inequality)** For all $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^n$,

$$
|\boldsymbol{a}^{\mathsf T}\boldsymbol{b}| \le \|\boldsymbol{a}\|\,\|\boldsymbol{b}\|,
$$

with equality if and only if $\boldsymbol{a}, \boldsymbol{b}$ are collinear.

**Proof** The case $\boldsymbol{a} = \boldsymbol{0}$ is trivial. Let $\boldsymbol{a} \ne \boldsymbol{0}$. For every $x \in \mathbb{R}$,

$$
0 \le (\boldsymbol{b} - x\boldsymbol{a})^{\mathsf T}(\boldsymbol{b} - x\boldsymbol{a}) = (\boldsymbol{a}^{\mathsf T}\boldsymbol{a})x^2 - 2(\boldsymbol{a}^{\mathsf T}\boldsymbol{b})x + \boldsymbol{b}^{\mathsf T}\boldsymbol{b} = (\boldsymbol{a}^{\mathsf T}\boldsymbol{a})\left(x - \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\right)^2 + \boldsymbol{b}^{\mathsf T}\boldsymbol{b} - \frac{(\boldsymbol{a}^{\mathsf T}\boldsymbol{b})^2}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}.
$$

Taking $x = \boldsymbol{a}^{\mathsf T}\boldsymbol{b}/\boldsymbol{a}^{\mathsf T}\boldsymbol{a}$ gives $(\boldsymbol{a}^{\mathsf T}\boldsymbol{b})^2 \le (\boldsymbol{a}^{\mathsf T}\boldsymbol{a})(\boldsymbol{b}^{\mathsf T}\boldsymbol{b})$. Equality holds if and only if $\boldsymbol{b} - x\boldsymbol{a} = \boldsymbol{0}$ for some $x$, that is, $\boldsymbol{a}, \boldsymbol{b}$ are collinear. $\square$

**Corollary 4.1.1 (Triangle Inequality)** $\|\boldsymbol{a} + \boldsymbol{b}\| \le \|\boldsymbol{a}\| + \|\boldsymbol{b}\|$: the sum of two sides of a triangle is at least the third side. Equality holds if and only if one of $\boldsymbol{a}, \boldsymbol{b}$ is the zero vector, or the two are collinear and point in the same direction.

**Proof** $\|\boldsymbol{a} + \boldsymbol{b}\|^2 = \|\boldsymbol{a}\|^2 + \|\boldsymbol{b}\|^2 + 2\boldsymbol{a}^{\mathsf T}\boldsymbol{b} \le \|\boldsymbol{a}\|^2 + \|\boldsymbol{b}\|^2 + 2\|\boldsymbol{a}\|\,\|\boldsymbol{b}\| = (\|\boldsymbol{a}\| + \|\boldsymbol{b}\|)^2$. Equality requires $\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \|\boldsymbol{a}\|\,\|\boldsymbol{b}\|$, and the equality condition follows from Theorem 4.1.1. $\square$

By the Cauchy–Schwarz inequality, $|\boldsymbol{a}^{\mathsf T}\boldsymbol{b}|/(\|\boldsymbol{a}\|\,\|\boldsymbol{b}\|) \le 1$ for nonzero vectors, so we can define angles.

**Definition 4.1.3 (Angle)** The angle between two nonzero vectors $\boldsymbol{a}, \boldsymbol{b}$ in $\mathbb{R}^n$ is $\arccos \dfrac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\|\boldsymbol{a}\|\,\|\boldsymbol{b}\|} \in [0, \pi]$.

**Definition 4.1.4 (Orthogonality)** Vectors $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^n$ are called **orthogonal** (perpendicular) if $\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = 0$; we write $\boldsymbol{a} \perp \boldsymbol{b}$.

The zero vector is orthogonal to every vector; nonzero vectors $\boldsymbol{a}, \boldsymbol{b}$ are orthogonal if and only if the angle between them is $\pi/2$.

**Theorem 4.1.2 (Pythagorean Theorem)** If $\boldsymbol{a} \perp \boldsymbol{b}$, then $\|\boldsymbol{a} \pm \boldsymbol{b}\|^2 = \|\boldsymbol{a}\|^2 + \|\boldsymbol{b}\|^2$.

**Proof** $\|\boldsymbol{a} \pm \boldsymbol{b}\|^2 = \boldsymbol{a}^{\mathsf T}\boldsymbol{a} + \boldsymbol{b}^{\mathsf T}\boldsymbol{b} \pm 2\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \|\boldsymbol{a}\|^2 + \|\boldsymbol{b}\|^2$. $\square$

## 4.2. Orthonormal Bases and Gram–Schmidt Orthogonalization

### 4.2.1. Orthogonal Projection onto a Line

Let $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^n$ with $\boldsymbol{a} \ne \boldsymbol{0}$. As in Example 4.1.1, we decompose $\boldsymbol{b} = \hat{x}\boldsymbol{a} + \boldsymbol{r}$ with $\boldsymbol{a} \perp \boldsymbol{r}$ and obtain

$$
\hat{x} = \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}, \qquad \boldsymbol{r} = \boldsymbol{b} - \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\boldsymbol{a}.
$$

The vector $\dfrac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\boldsymbol{a}$ is called the orthogonal projection of $\boldsymbol{b}$ onto the line $\operatorname{span}(\boldsymbol{a})$, and $\boldsymbol{r}$ is orthogonal to $\boldsymbol{a}$. Section 4.4 generalizes this to orthogonal projection onto an arbitrary subspace.

**Proposition 4.2.1** Let $\boldsymbol{a} \ne \boldsymbol{0}$. Then $\left\|\boldsymbol{b} - \dfrac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\boldsymbol{a}\right\| = \min\limits_{x \in \mathbb{R}} \|\boldsymbol{b} - x\boldsymbol{a}\|$.

**Proof** By the completed square in the proof of Theorem 4.1.1, $\|\boldsymbol{b} - x\boldsymbol{a}\|^2$ is a quadratic function of $x$ that attains its minimum at $x = \boldsymbol{a}^{\mathsf T}\boldsymbol{b}/\boldsymbol{a}^{\mathsf T}\boldsymbol{a}$. $\square$

### 4.2.2. Orthogonal Sets and Orthonormal Bases

**Definition 4.2.1 (Orthogonal Set)** Let $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ be vectors in $\mathbb{R}^n$. If they are all nonzero and pairwise orthogonal, they form an **orthogonal set**; if, moreover, they are all unit vectors, they form an **orthonormal set**.

**Proposition 4.2.2** An orthogonal set is **linearly independent**.

**Proof** Suppose $k_1\boldsymbol{a}_1 + \cdots + k_r\boldsymbol{a}_r = \boldsymbol{0}$. Taking the inner product of both sides with $\boldsymbol{a}_i$ and using pairwise orthogonality gives $k_i\|\boldsymbol{a}_i\|^2 = 0$; since $\boldsymbol{a}_i \ne \boldsymbol{0}$, $k_i = 0$ ($i = 1, \dots, r$). $\square$

**Definition 4.2.2 (Orthonormal Basis)** Let $M$ be a subspace of $\mathbb{R}^n$. A basis of $M$ that is an orthogonal set is called an **orthogonal basis** of $M$; a basis that is an orthonormal set is called an **orthonormal basis** of $M$.

The **standard basis** $\boldsymbol{e}_1, \dots, \boldsymbol{e}_n$ is an orthonormal basis of $\mathbb{R}^n$. By Proposition 4.2.2, any orthogonal set of $r$ vectors in an $r$-dimensional subspace $M$ is an orthogonal basis of $M$. The advantage of an orthonormal basis is that coordinates require only inner products: finding coordinates with respect to a general basis means solving a linear system, whereas with respect to an orthogonal basis $\boldsymbol{q}_1, \dots, \boldsymbol{q}_n$ we obtain $x_i$ simply by taking the inner product of $\boldsymbol{a} = \sum_j x_j\boldsymbol{q}_j$ with $\boldsymbol{q}_i$:

$$
\boldsymbol{a} = \frac{\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}}{\boldsymbol{q}_1^{\mathsf T}\boldsymbol{q}_1}\boldsymbol{q}_1 + \frac{\boldsymbol{q}_2^{\mathsf T}\boldsymbol{a}}{\boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_2}\boldsymbol{q}_2 + \cdots + \frac{\boldsymbol{q}_n^{\mathsf T}\boldsymbol{a}}{\boldsymbol{q}_n^{\mathsf T}\boldsymbol{q}_n}\boldsymbol{q}_n,
$$

that is, $\boldsymbol{a}$ is the sum of its orthogonal projections onto the lines $\operatorname{span}(\boldsymbol{q}_i)$; for an orthonormal basis the coefficients are just $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}$.

**Theorem 4.2.1 (Existence of Orthonormal Bases)** Every nonzero subspace $M$ of $\mathbb{R}^n$ has an orthogonal basis, and hence an orthonormal basis.

**Proof** We use induction on $\dim M$. If $\dim M = 1$, any nonzero vector forms an orthogonal basis. Suppose the claim holds for $r$-dimensional subspaces, and let $M$ be an $(r+1)$-dimensional subspace with basis $\boldsymbol{a}_1, \dots, \boldsymbol{a}_{r+1}$. By the induction hypothesis, $N = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$ has an orthogonal basis $\boldsymbol{q}_1, \dots, \boldsymbol{q}_r$, so $\boldsymbol{q}_1, \dots, \boldsymbol{q}_r, \boldsymbol{a}_{r+1}$ is also a basis of $M$. Set $\boldsymbol{q}_{r+1} = \boldsymbol{a}_{r+1} + k_1\boldsymbol{q}_1 + \cdots + k_r\boldsymbol{q}_r$ and require it to be orthogonal to each $\boldsymbol{q}_i$; taking the inner product with $\boldsymbol{q}_i$ gives $0 = \boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_{r+1} + k_i\|\boldsymbol{q}_i\|^2$, so

$$
\boldsymbol{q}_{r+1} = \boldsymbol{a}_{r+1} - \frac{\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_{r+1}}{\|\boldsymbol{q}_1\|^2}\boldsymbol{q}_1 - \cdots - \frac{\boldsymbol{q}_r^{\mathsf T}\boldsymbol{a}_{r+1}}{\|\boldsymbol{q}_r\|^2}\boldsymbol{q}_r.
$$

Since $\boldsymbol{a}_{r+1} \notin N$, we have $\boldsymbol{q}_{r+1} \ne \boldsymbol{0}$, so $\boldsymbol{q}_1, \dots, \boldsymbol{q}_{r+1}$ is an orthogonal basis of $M$. Normalizing each vector yields an orthonormal basis. $\square$

**Theorem 4.2.2 (Extension of Orthonormal Bases)** Let $M \subseteq N$ be subspaces of $\mathbb{R}^n$. Then every orthonormal basis of $M$ can be extended to an orthonormal basis of $N$.

**Proof** Let $\boldsymbol{q}_1, \dots, \boldsymbol{q}_r$ be an orthonormal basis of $M$. By the basis extension theorem of Chapter 3, it extends to a basis $\boldsymbol{q}_1, \dots, \boldsymbol{q}_r, \boldsymbol{a}_{r+1}, \dots, \boldsymbol{a}_s$ of $N$. Applying the construction from the proof of Theorem 4.2.1 to the remaining vectors in turn (the first $r$ vectors are already pairwise orthogonal and remain unchanged) and then normalizing gives an orthonormal basis of $N$ containing $\boldsymbol{q}_1, \dots, \boldsymbol{q}_r$. $\square$

### 4.2.3. Gram–Schmidt Orthogonalization

The proof of Theorem 4.2.1 is itself an algorithm: starting from an arbitrary basis, subtract from each vector its projections onto the orthogonal vectors already obtained.

**Algorithm 4.2.1 (Gram–Schmidt Process)** Input: a basis $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ of an $r$-dimensional subspace $M \subseteq \mathbb{R}^n$. Output: an orthonormal basis $\boldsymbol{q}_1, \dots, \boldsymbol{q}_r$ of $M$.

1. Orthogonalize: compute in turn
   $$
   \begin{aligned}
   \tilde{\boldsymbol{q}}_1 &= \boldsymbol{a}_1, \\
   \tilde{\boldsymbol{q}}_2 &= \boldsymbol{a}_2 - \frac{\tilde{\boldsymbol{q}}_1^{\mathsf T}\boldsymbol{a}_2}{\|\tilde{\boldsymbol{q}}_1\|^2}\tilde{\boldsymbol{q}}_1, \\
   &\ \ \vdots \\
   \tilde{\boldsymbol{q}}_r &= \boldsymbol{a}_r - \frac{\tilde{\boldsymbol{q}}_1^{\mathsf T}\boldsymbol{a}_r}{\|\tilde{\boldsymbol{q}}_1\|^2}\tilde{\boldsymbol{q}}_1 - \frac{\tilde{\boldsymbol{q}}_2^{\mathsf T}\boldsymbol{a}_r}{\|\tilde{\boldsymbol{q}}_2\|^2}\tilde{\boldsymbol{q}}_2 - \cdots - \frac{\tilde{\boldsymbol{q}}_{r-1}^{\mathsf T}\boldsymbol{a}_r}{\|\tilde{\boldsymbol{q}}_{r-1}\|^2}\tilde{\boldsymbol{q}}_{r-1};
   \end{aligned}
   $$
2. Normalize: $\boldsymbol{q}_i = \tilde{\boldsymbol{q}}_i / \|\tilde{\boldsymbol{q}}_i\|$ ($i = 1, \dots, r$).

Step $i$ subtracts from $\boldsymbol{a}_i$ its orthogonal projections onto the directions $\tilde{\boldsymbol{q}}_1, \dots, \tilde{\boldsymbol{q}}_{i-1}$, leaving the part $\tilde{\boldsymbol{q}}_i$ that is orthogonal to all of them. At every step the three sets of vectors

$$
\{\tilde{\boldsymbol{q}}_1, \dots, \tilde{\boldsymbol{q}}_{i-1}, \tilde{\boldsymbol{q}}_i\}, \qquad \{\tilde{\boldsymbol{q}}_1, \dots, \tilde{\boldsymbol{q}}_{i-1}, \boldsymbol{a}_i\}, \qquad \{\boldsymbol{a}_1, \dots, \boldsymbol{a}_{i-1}, \boldsymbol{a}_i\}
$$

span the same subspace, so $\operatorname{span}(\boldsymbol{q}_1, \dots, \boldsymbol{q}_i) = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_i)$ for every $i$. This property, that the first $i$ vectors span the same subspace, is exactly why $R$ is upper triangular in the next section.

**Example 4.2.1** Use Gram–Schmidt orthogonalization to turn the basis $\boldsymbol{a}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$, $\boldsymbol{a}_2 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$, $\boldsymbol{a}_3 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ of $\mathbb{R}^3$ into an orthonormal basis.

$$
\tilde{\boldsymbol{q}}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \quad
\tilde{\boldsymbol{q}}_2 = \boldsymbol{a}_2 - \frac{2}{3}\tilde{\boldsymbol{q}}_1 = \frac{1}{3}\begin{bmatrix} 1 \\ 1 \\ -2 \end{bmatrix}, \quad
\tilde{\boldsymbol{q}}_3 = \boldsymbol{a}_3 - \frac{1}{3}\tilde{\boldsymbol{q}}_1 - \frac{1/3}{2/3}\tilde{\boldsymbol{q}}_2 = \frac{1}{2}\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}.
$$

Normalizing gives $\boldsymbol{q}_1 = \dfrac{1}{\sqrt{3}}\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$, $\boldsymbol{q}_2 = \dfrac{1}{\sqrt{6}}\begin{bmatrix} 1 \\ 1 \\ -2 \end{bmatrix}$, $\boldsymbol{q}_3 = \dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$. The result depends on the order of the vectors: orthogonalizing in the order $\boldsymbol{a}_3, \boldsymbol{a}_2, \boldsymbol{a}_1$ yields the standard basis $\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}_3$.

## 4.3. Orthogonal Matrices and the QR Decomposition

### 4.3.1. Orthogonal Matrices

Let $\boldsymbol{q}_1, \dots, \boldsymbol{q}_n$ be an orthonormal basis of $\mathbb{R}^n$ and $Q = [\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$. The $(i, j)$ entry of $Q^{\mathsf T}Q$ is $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{q}_j$, so $Q^{\mathsf T}Q = I_n$.

**Definition 4.3.1 (Orthogonal Matrix)** A square matrix $Q$ of order $n$ with $Q^{\mathsf T}Q = I_n$ is called an **orthogonal matrix** of order $n$.

**Theorem 4.3.1** For a square matrix $Q$ of order $n$, the following are equivalent:

1. $Q$ is an orthogonal matrix, that is, $Q^{\mathsf T}Q = I_n$;
2. $Q$ is invertible and $Q^{-1} = Q^{\mathsf T}$;
3. $QQ^{\mathsf T} = I_n$;
4. $Q^{\mathsf T}$ is an orthogonal matrix;
5. $Q$ is invertible and $Q^{-1}$ is an orthogonal matrix;
6. the columns of $Q$ form an orthonormal basis of $\mathbb{R}^n$;
7. the rows of $Q$ (transposed) form an orthonormal basis of $\mathbb{R}^n$.

**Proof** For square matrices, $BA = I_n$ already implies that $A$ is an **invertible matrix** with $A^{-1} = B$ (Chapter 2), so 1 ⇔ 2 ⇔ 3; 3 is the definition of 4, and 2 and 4 together give 5; 1 ⇔ 6 is the computation before the definition, and 3 ⇔ 7 likewise. $\square$

By Theorem 4.3.1, inverting an orthogonal matrix only requires transposing it; this is the most important computational advantage of orthogonal matrices. The product of two orthogonal matrices of order $n$ is again orthogonal: $(Q_1Q_2)^{\mathsf T}(Q_1Q_2) = Q_2^{\mathsf T}Q_1^{\mathsf T}Q_1Q_2 = I_n$.

**Theorem 4.3.2** For a square matrix $Q$ of order $n$, the following are equivalent:

1. $Q$ is an orthogonal matrix;
2. $Q$ preserves length: $\|Q\boldsymbol{x}\| = \|\boldsymbol{x}\|$ for all $\boldsymbol{x} \in \mathbb{R}^n$;
3. $Q$ preserves inner products: $(Q\boldsymbol{x})^{\mathsf T}(Q\boldsymbol{y}) = \boldsymbol{x}^{\mathsf T}\boldsymbol{y}$ for all $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$.

**Proof** We prove the implications in a cycle. 1 ⇒ 2: $\|Q\boldsymbol{x}\|^2 = \boldsymbol{x}^{\mathsf T}Q^{\mathsf T}Q\boldsymbol{x} = \|\boldsymbol{x}\|^2$. 2 ⇒ 3: by the polarization identity (Property 4.1.2),

$$
\boldsymbol{x}^{\mathsf T}\boldsymbol{y} = \frac{1}{4}\left(\|\boldsymbol{x} + \boldsymbol{y}\|^2 - \|\boldsymbol{x} - \boldsymbol{y}\|^2\right) = \frac{1}{4}\left(\|Q\boldsymbol{x} + Q\boldsymbol{y}\|^2 - \|Q\boldsymbol{x} - Q\boldsymbol{y}\|^2\right) = (Q\boldsymbol{x})^{\mathsf T}(Q\boldsymbol{y}).
$$

3 ⇒ 1: the $(i, j)$ entry of $Q^{\mathsf T}Q$ is $\boldsymbol{e}_i^{\mathsf T}Q^{\mathsf T}Q\boldsymbol{e}_j = (Q\boldsymbol{e}_i)^{\mathsf T}(Q\boldsymbol{e}_j) = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{e}_j$, so $Q^{\mathsf T}Q = I_n$. $\square$

Since they preserve lengths and inner products, orthogonal matrices also preserve angles; geometrically, the corresponding **linear transformation** is a "rigid motion" (a composition of rotations and reflections). Conversely, an angle-preserving transformation need not be orthogonal: $2Q$, for instance, preserves angles but not lengths.

**Example 4.3.1 (Orthogonal Matrices of Order 2)** Let $Q = [\boldsymbol{q}_1\ \boldsymbol{q}_2]$ be an orthogonal matrix of order $2$, so that $\boldsymbol{q}_1, \boldsymbol{q}_2$ is an orthonormal basis of $\mathbb{R}^2$. Write $\boldsymbol{q}_1 = \begin{bmatrix} \cos\theta \\ \sin\theta \end{bmatrix}$ and $\boldsymbol{q}_2 = \begin{bmatrix} \cos\varphi \\ \sin\varphi \end{bmatrix}$. From $\boldsymbol{q}_1 \perp \boldsymbol{q}_2$ we get $\cos(\theta - \varphi) = 0$, that is, $\theta - \varphi = (k + \frac{1}{2})\pi$ with $k \in \mathbb{Z}$. Depending on the parity of $k$, an orthogonal matrix of order $2$ has one of only two forms:

$$
R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}, \qquad
H_{\theta/2} = \begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}.
$$

$R_\theta$ is the rotation by the angle $\theta$, and $H_{\theta/2}$ is the reflection across the line $\ell_{\theta/2}$ through the origin that makes the angle $\theta/2$ with the $x_1$-axis. They satisfy

$$
R_{\theta - \varphi} = H_{\theta/2}H_{\varphi/2}, \qquad H_{(\theta + \varphi)/2} = R_\theta H_{\varphi/2} = H_{\varphi/2}R_{-\theta},
$$

so every orthogonal matrix of order $2$ is a product of at most two reflections. Let $\boldsymbol{v} = \begin{bmatrix} -\sin(\theta/2) \\ \cos(\theta/2) \end{bmatrix}$ be the unit normal vector of $\ell_{\theta/2}$. The projection of $\boldsymbol{w}$ onto $\operatorname{span}(\boldsymbol{v})$ is $(\boldsymbol{v}^{\mathsf T}\boldsymbol{w})\boldsymbol{v}$, and subtracting it twice gives the reflected vector: $H_{\theta/2}\boldsymbol{w} = \boldsymbol{w} - 2(\boldsymbol{v}^{\mathsf T}\boldsymbol{w})\boldsymbol{v} = (I_2 - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T})\boldsymbol{w}$, that is, $H_{\theta/2} = I_2 - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}$.

### 4.3.2. Givens Rotations and Householder Reflections

Rotations and reflections of the plane both generalize to $\mathbb{R}^n$.

**Definition 4.3.2 (Givens Rotation)** The rotation by the angle $\theta$ in the $\boldsymbol{e}_i$–$\boldsymbol{e}_j$ plane that leaves all other coordinates unchanged is called a **Givens rotation**. Its matrix $G_{\theta;i,j}$ differs from $I_n$ only where rows $i, j$ meet columns $i, j$:

$$
(G_{\theta;i,j})_{ii} = (G_{\theta;i,j})_{jj} = \cos\theta, \qquad (G_{\theta;i,j})_{ij} = -\sin\theta, \qquad (G_{\theta;i,j})_{ji} = \sin\theta.
$$

That is, $\boldsymbol{x} = G_{\theta;i,j}\boldsymbol{w}$ satisfies $\begin{bmatrix} x_i \\ x_j \end{bmatrix} = R_\theta\begin{bmatrix} w_i \\ w_j \end{bmatrix}$ and $x_k = w_k$ ($k \ne i, j$). $G_{\theta;i,j}$ preserves length, so it is an orthogonal matrix. A suitable choice of $\theta$ makes the $j$-th component of $\boldsymbol{w}$ zero, so a sequence of Givens rotations can eliminate the entries below the diagonal of a matrix one by one.

**Definition 4.3.3 (Householder Reflection)** Let $\boldsymbol{v} \in \mathbb{R}^n$ be a unit vector and $\mathcal{N}(\boldsymbol{v}^{\mathsf T})$ the hyperplane with normal vector $\boldsymbol{v}$. The reflection across this hyperplane,

$$
H_{\boldsymbol{v}} = I_n - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T},
$$

is called a **Householder reflection** (Householder transformation).

Decompose $\boldsymbol{w}$ orthogonally as $\boldsymbol{w} = (I_n - \boldsymbol{v}\boldsymbol{v}^{\mathsf T})\boldsymbol{w} + \boldsymbol{v}\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$: the first part lies in the hyperplane $\mathcal{N}(\boldsymbol{v}^{\mathsf T})$ and the second is the projection of $\boldsymbol{w}$ onto $\operatorname{span}(\boldsymbol{v})$. The reflection keeps the first part and reverses the second, which gives $H_{\boldsymbol{v}}\boldsymbol{w}$. $H_{\boldsymbol{v}}$ is a **symmetric matrix**, and $H_{\boldsymbol{v}}^{\mathsf T}H_{\boldsymbol{v}} = H_{\boldsymbol{v}}^2 = I_n - 4\boldsymbol{v}\boldsymbol{v}^{\mathsf T} + 4\boldsymbol{v}(\boldsymbol{v}^{\mathsf T}\boldsymbol{v})\boldsymbol{v}^{\mathsf T} = I_n$, so it is an orthogonal matrix.

**Proposition 4.3.1** Let $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$ have the same length with $\boldsymbol{x} \ne \boldsymbol{y}$, and let $\boldsymbol{v} = \dfrac{\boldsymbol{y} - \boldsymbol{x}}{\|\boldsymbol{y} - \boldsymbol{x}\|}$. Then $H_{\boldsymbol{v}}\boldsymbol{x} = \boldsymbol{y}$.

**Proof** Write $\boldsymbol{w} = \boldsymbol{y} - \boldsymbol{x}$. Since $\|\boldsymbol{x}\| = \|\boldsymbol{y}\|$, we have $\|\boldsymbol{w}\|^2 = 2\|\boldsymbol{x}\|^2 - 2\boldsymbol{y}^{\mathsf T}\boldsymbol{x} = -2\boldsymbol{w}^{\mathsf T}\boldsymbol{x}$. Hence

$$
H_{\boldsymbol{v}}\boldsymbol{x} = \boldsymbol{x} - \frac{2(\boldsymbol{w}^{\mathsf T}\boldsymbol{x})}{\|\boldsymbol{w}\|^2}\boldsymbol{w} = \boldsymbol{x} + \boldsymbol{w} = \boldsymbol{y}. \qquad \square
$$

In particular, taking $\boldsymbol{y} = \mp\|\boldsymbol{x}\|\boldsymbol{e}_1$, a single Householder reflection zeros out all components of $\boldsymbol{x}$ except the first. The idea is the same as in Gaussian elimination with row-addition operations, except that the transformations used are orthogonal matrices.

### 4.3.3. The QR Decomposition

Describing Gaussian elimination by matrix multiplication gives the **LU decomposition**; describing Gram–Schmidt orthogonalization in the same way gives another matrix factorization. Let $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ be invertible, and apply Algorithm 4.2.1 to its columns to obtain the orthogonal basis $\tilde{\boldsymbol{q}}_1, \dots, \tilde{\boldsymbol{q}}_n$ and the orthonormal basis $\boldsymbol{q}_1, \dots, \boldsymbol{q}_n$. Since $\boldsymbol{a}_i$ is a linear combination of $\tilde{\boldsymbol{q}}_1, \dots, \tilde{\boldsymbol{q}}_i$, setting $\tilde{Q} = [\tilde{\boldsymbol{q}}_1\ \cdots\ \tilde{\boldsymbol{q}}_n]$ and $Q = [\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$ we have

$$
A = \tilde{Q}\tilde{R}, \qquad
\tilde{R} = \begin{bmatrix}
1 & \dfrac{\tilde{\boldsymbol{q}}_1^{\mathsf T}\boldsymbol{a}_2}{\|\tilde{\boldsymbol{q}}_1\|^2} & \cdots & \dfrac{\tilde{\boldsymbol{q}}_1^{\mathsf T}\boldsymbol{a}_n}{\|\tilde{\boldsymbol{q}}_1\|^2} \\
 & 1 & \cdots & \dfrac{\tilde{\boldsymbol{q}}_2^{\mathsf T}\boldsymbol{a}_n}{\|\tilde{\boldsymbol{q}}_2\|^2} \\
 & & \ddots & \vdots \\
 & & & 1
\end{bmatrix}.
$$

Normalization reads $\tilde{Q} = Q\operatorname{diag}(\|\tilde{\boldsymbol{q}}_i\|)$, so $A = Q\operatorname{diag}(\|\tilde{\boldsymbol{q}}_i\|)\tilde{R} = QR$, where $Q$ is an orthogonal matrix and $R = \operatorname{diag}(\|\tilde{\boldsymbol{q}}_i\|)\tilde{R}$ is upper triangular with positive diagonal entries; the $(i, j)$ entry of $R$ ($i < j$) is $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$, and its diagonal entries are $\|\tilde{\boldsymbol{q}}_i\|$.

**Theorem 4.3.3 (QR Decomposition of an Invertible Matrix)** Let $A$ be an invertible matrix of order $n$. Then there is a unique factorization $A = QR$ in which $Q$ is an orthogonal matrix and $R$ is upper triangular with positive diagonal entries.

**Proof** Existence follows from the construction above. Uniqueness: if $A = Q_1R_1 = Q_2R_2$, then $U = Q_2^{-1}Q_1 = R_2R_1^{-1}$ is both an orthogonal matrix and an upper triangular matrix with positive diagonal entries. Of $U^{\mathsf T} = U^{-1}$, the left side is lower triangular and the right side upper triangular, so $U$ is diagonal; then $U^{\mathsf T}U = I_n$ together with the positive diagonal gives $U = I_n$, that is, $Q_1 = Q_2$ and $R_1 = R_2$. $\square$

To extend the QR decomposition to $m \times n$ matrices, we introduce the following notion.

**Definition 4.3.4 (Matrix with Orthonormal Columns)** An $m \times n$ matrix $Q$ with $Q^{\mathsf T}Q = I_n$ is called a **matrix with orthonormal columns**.

$Q$ has orthonormal columns if and only if its columns form an orthonormal set in $\mathbb{R}^m$. Such a matrix has **full rank** $n$ (full column rank), so $m \ge n$.

**Theorem 4.3.4 (QR Decomposition)** Let $A$ be an $m \times n$ matrix with $m \ge n$. Then:

1. there exist an $m \times n$ matrix $Q_1$ with orthonormal columns and an upper triangular matrix $R_1$ of order $n$ with nonnegative diagonal entries such that $A = Q_1R_1$;
2. moreover, there exist an orthogonal matrix $Q = [Q_1\ Q_2]$ of order $m$ (whose columns extend those of $Q_1$) and an $m \times n$ matrix $R = \begin{bmatrix} R_1 \\ O \end{bmatrix}$ such that $A = QR$.

$A = QR$ is called the **QR decomposition** of $A$, and $A = Q_1R_1$ its reduced QR decomposition.

**Proof** We use induction on $n$. For $n = 1$: if $\boldsymbol{a}_1 \ne \boldsymbol{0}$, take $Q_1 = \boldsymbol{a}_1/\|\boldsymbol{a}_1\|$ and $R_1 = \|\boldsymbol{a}_1\|$; if $\boldsymbol{a}_1 = \boldsymbol{0}$, take any unit vector as $Q_1$ and $R_1 = 0$. Suppose the claim holds for $m \times (n-1)$ matrices, write $A = [A_0\ \boldsymbol{a}_n]$, and let $A_0 = Q_0R_0$.

- If $\boldsymbol{a}_n \notin \mathcal{R}(Q_0)$, then by Gram–Schmidt orthogonalization there is $\boldsymbol{r}_n$ such that $\tilde{\boldsymbol{q}}_n = \boldsymbol{a}_n - Q_0\boldsymbol{r}_n \ne \boldsymbol{0}$ is orthogonal to the columns of $Q_0$; set $\boldsymbol{q}_n = \tilde{\boldsymbol{q}}_n/\|\tilde{\boldsymbol{q}}_n\|$.
- If $\boldsymbol{a}_n \in \mathcal{R}(Q_0)$, then $\boldsymbol{a}_n = Q_0\boldsymbol{r}_n$; take any unit vector $\boldsymbol{q}_n$ orthogonal to the columns of $Q_0$ and set $\|\tilde{\boldsymbol{q}}_n\| = 0$.

In both cases

$$
A = [Q_0R_0\ \ Q_0\boldsymbol{r}_n + \|\tilde{\boldsymbol{q}}_n\|\boldsymbol{q}_n] = [Q_0\ \boldsymbol{q}_n]\begin{bmatrix} R_0 & \boldsymbol{r}_n \\ \boldsymbol{0}^{\mathsf T} & \|\tilde{\boldsymbol{q}}_n\| \end{bmatrix} = Q_1R_1.
$$

By Theorem 4.2.2, the columns of $Q_1$ extend to an orthonormal basis of $\mathbb{R}^m$, giving $Q = [Q_1\ Q_2]$ with $A = Q_1R_1 = [Q_1\ Q_2]\begin{bmatrix} R_1 \\ O \end{bmatrix}$. $\square$

If $A$ has full column rank, Gram–Schmidt orthogonalization applied directly to its columns yields $Q_1, R_1$ with all diagonal entries of $R_1$ positive ($R_1$ is invertible); in this case the reduced QR decomposition is unique (the proof is the same as for Theorem 4.3.3).

**Example 4.3.2** Find the QR decomposition of $A = [\boldsymbol{a}_1\ \boldsymbol{a}_2\ \boldsymbol{a}_3] = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$.

By Example 4.2.1, $A = \tilde{Q}\tilde{R}$, where

$$
\tilde{Q} = \begin{bmatrix} 1 & \frac{1}{3} & \frac{1}{2} \\ 1 & \frac{1}{3} & -\frac{1}{2} \\ 1 & -\frac{2}{3} & 0 \end{bmatrix}, \quad
\tilde{R} = \begin{bmatrix} 1 & \frac{2}{3} & \frac{1}{3} \\ 0 & 1 & \frac{1}{2} \\ 0 & 0 & 1 \end{bmatrix}, \quad
\|\tilde{\boldsymbol{q}}_1\| = \sqrt{3},\ \|\tilde{\boldsymbol{q}}_2\| = \frac{\sqrt{6}}{3},\ \|\tilde{\boldsymbol{q}}_3\| = \frac{\sqrt{2}}{2}.
$$

Hence $A = QR$ with

$$
Q = \begin{bmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & -\frac{2}{\sqrt{6}} & 0 \end{bmatrix}, \qquad
R = \begin{bmatrix} \sqrt{3} & \frac{2}{\sqrt{3}} & \frac{1}{\sqrt{3}} \\ 0 & \frac{\sqrt{6}}{3} & \frac{1}{\sqrt{6}} \\ 0 & 0 & \frac{1}{\sqrt{2}} \end{bmatrix}.
$$

### 4.3.4. Computing the QR Decomposition

**Algorithm 4.3.1 (Gram–Schmidt QR)** Input: an $m \times n$ matrix $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ of full column rank. Output: the reduced QR decomposition $A = Q_1R_1$. For $j = 1, \dots, n$:

1. compute $r_{ij} = \boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$ ($i = 1, \dots, j-1$);
2. compute $\tilde{\boldsymbol{q}}_j = \boldsymbol{a}_j - \sum_{i<j} r_{ij}\boldsymbol{q}_i$, $r_{jj} = \|\tilde{\boldsymbol{q}}_j\|$ and $\boldsymbol{q}_j = \tilde{\boldsymbol{q}}_j / r_{jj}$.

The modified Gram–Schmidt algorithm is mathematically equivalent; it only replaces $\boldsymbol{a}_j$ in step 1 by "the current vector, from which the earlier projections have already been subtracted": as soon as a $\boldsymbol{q}_i$ is obtained, its component is removed from all subsequent vectors. The total cost is about $2mn^2$ floating-point operations.

**Algorithm 4.3.2 (Householder QR)** Input: an $m \times n$ matrix $A$ ($m \ge n$). For $j = 1, \dots, n$: let $\boldsymbol{x}$ be the vector formed by components $j$ through $m$ of column $j$ of the current matrix; construct, as in Proposition 4.3.1, the Householder reflection that maps $\boldsymbol{x}$ to $-\operatorname{sgn}(x_1)\|\boldsymbol{x}\|\boldsymbol{e}_1$ (this sign avoids cancellation in the subtraction $\boldsymbol{y} - \boldsymbol{x}$), and apply it to rows $j$ through $m$ of the current matrix. After $n$ steps we obtain an upper triangular $R$ with $H_n\cdots H_1A = R$, that is, $A = QR$ with $Q = H_1H_2\cdots H_n$.

In exact arithmetic the three algorithms produce the same factorization, but in floating-point arithmetic they differ greatly. The figure below computes $\|I - Q^{\mathsf T}Q\|_2$, the departure of the computed $Q$ from having orthonormal columns, for $60 \times 30$ matrices of varying condition number $\kappa(A)$ (the ratio of the largest to the smallest singular value; see [Chapter 7](/2.1.7)). The error of classical Gram–Schmidt grows roughly like $\varepsilon\kappa(A)^2$ (where $\varepsilon \approx 10^{-16}$ is the machine precision of double precision), and orthogonality is completely lost by $\kappa(A) \approx 10^8$; modified Gram–Schmidt grows roughly like $\varepsilon\kappa(A)$; the Householder method stays at machine precision throughout. This is why numerical software (such as LAPACK and `numpy.linalg.qr`) uses Householder reflections.

![Loss of orthogonality of three QR algorithms versus the condition number: classical Gram–Schmidt is worst, modified Gram–Schmidt is in between, and Householder stays at machine precision](./plots/qr-orthogonality-loss.py)

## 4.4. Orthogonal Complements and Orthogonal Projections

Section 4.2 projected vectors onto a line; we now generalize this to arbitrary subspaces and thereby answer the question posed at the beginning of the chapter: when $\boldsymbol{b} \notin \mathcal{R}(A)$, which vector of $\mathcal{R}(A)$ is closest to $\boldsymbol{b}$?

### 4.4.1. Orthogonal Subspaces and Orthogonal Complements

If $\boldsymbol{r}$ is orthogonal to each of $\boldsymbol{a}_1, \dots, \boldsymbol{a}_s$, then by bilinearity $\boldsymbol{r}$ is orthogonal to every vector in $\operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_s)$. For example, every solution of the homogeneous system $A\boldsymbol{x} = \boldsymbol{0}$ is orthogonal to every row of $A$, so every vector in the **null space** $\mathcal{N}(A)$ is orthogonal to every vector in the **row space** $\mathcal{R}(A^{\mathsf T})$.

**Definition 4.4.1 (Orthogonal Subspaces)** Let $M, N$ be subspaces of $\mathbb{R}^n$. If every vector of $M$ is orthogonal to every vector of $N$, we say that $M$ and $N$ are orthogonal and write $M \perp N$. If $\operatorname{span}(\boldsymbol{a}) \perp M$, we say that the vector $\boldsymbol{a}$ is orthogonal to $M$ and write $\boldsymbol{a} \perp M$.

**Definition 4.4.2 (Orthogonal Complement)** For a subspace $M$ of $\mathbb{R}^n$, the set $M^\perp = \{\boldsymbol{a} \in \mathbb{R}^n \mid \boldsymbol{a} \perp M\}$ is called the **orthogonal complement** of $M$.

By definition, if $M \perp N$ then $M \subseteq N^\perp$ and $N \subseteq M^\perp$; if $M \subseteq N$ then $N^\perp \subseteq M^\perp$. $M^\perp$ is a subspace: $\boldsymbol{0} \in M^\perp$, and if $\boldsymbol{a}_1, \boldsymbol{a}_2 \in M^\perp$, then for every $\boldsymbol{b} \in M$ we have $(k_1\boldsymbol{a}_1 + k_2\boldsymbol{a}_2)^{\mathsf T}\boldsymbol{b} = k_1\boldsymbol{a}_1^{\mathsf T}\boldsymbol{b} + k_2\boldsymbol{a}_2^{\mathsf T}\boldsymbol{b} = 0$.

**Theorem 4.4.1** For a subspace $M$ of $\mathbb{R}^n$:

1. $M \cap M^\perp = \{\boldsymbol{0}\}$;
2. $\dim M^\perp = n - \dim M$;
3. $(M^\perp)^\perp = M$;
4. every $\boldsymbol{a} \in \mathbb{R}^n$ has a unique decomposition $\boldsymbol{a} = \boldsymbol{a}_1 + \boldsymbol{a}_2$ with $\boldsymbol{a}_1 \in M$ and $\boldsymbol{a}_2 \in M^\perp$.

**Proof** 1. If $\boldsymbol{a} \in M \cap M^\perp$, then $\boldsymbol{a} \perp \boldsymbol{a}$, so $\boldsymbol{a}^{\mathsf T}\boldsymbol{a} = 0$ and $\boldsymbol{a} = \boldsymbol{0}$.

2. Take an orthonormal basis $\boldsymbol{q}_1, \dots, \boldsymbol{q}_r$ of $M$ and extend it to an orthonormal basis $\boldsymbol{q}_1, \dots, \boldsymbol{q}_n$ of $\mathbb{R}^n$ (Theorem 4.2.2); then $\operatorname{span}(\boldsymbol{q}_{r+1}, \dots, \boldsymbol{q}_n) \subseteq M^\perp$. Conversely, for $\boldsymbol{a} \in M^\perp$, $\boldsymbol{a} = \sum_{i=1}^n (\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_i = \sum_{i=r+1}^n (\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_i$. Therefore $M^\perp = \operatorname{span}(\boldsymbol{q}_{r+1}, \dots, \boldsymbol{q}_n)$ and $\dim M^\perp = n - r$.

3. $M \subseteq (M^\perp)^\perp$, and by 2, $\dim (M^\perp)^\perp = n - \dim M^\perp = \dim M$, so the two are equal.

4. Existence: take $\boldsymbol{a}_1 = \sum_{i=1}^r (\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_i \in M$ and $\boldsymbol{a}_2 = \boldsymbol{a} - \boldsymbol{a}_1$; then $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_2 = 0$ ($i \le r$), that is, $\boldsymbol{a}_2 \in M^\perp$. Uniqueness: if $\boldsymbol{a} = \boldsymbol{a}_1 + \boldsymbol{a}_2 = \boldsymbol{a}_1' + \boldsymbol{a}_2'$, then $\boldsymbol{a}_1 - \boldsymbol{a}_1' = \boldsymbol{a}_2' - \boldsymbol{a}_2 \in M \cap M^\perp = \{\boldsymbol{0}\}$. $\square$

### 4.4.2. Orthogonality of the Four Fundamental Subspaces

**Theorem 4.4.2** Let $A$ be an $m \times n$ matrix. Then:

1. $\mathcal{R}(A^{\mathsf T})^\perp = \mathcal{N}(A)$ and $\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf T})$;
2. $\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A)$ and $\mathcal{R}(A^{\mathsf T}A) = \mathcal{R}(A^{\mathsf T})$; $\mathcal{N}(AA^{\mathsf T}) = \mathcal{N}(A^{\mathsf T})$ and $\mathcal{R}(AA^{\mathsf T}) = \mathcal{R}(A)$.

**Proof** 1. $\boldsymbol{x} \in \mathcal{N}(A)$ if and only if $\boldsymbol{x}$ is orthogonal to every row of $A$, if and only if $\boldsymbol{x} \perp \mathcal{R}(A^{\mathsf T})$. Applying this to $A^{\mathsf T}$ gives the second identity.

2. Clearly $\mathcal{N}(A) \subseteq \mathcal{N}(A^{\mathsf T}A)$. Conversely, if $A^{\mathsf T}A\boldsymbol{x} = \boldsymbol{0}$, then $\|A\boldsymbol{x}\|^2 = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}A\boldsymbol{x} = 0$, so $A\boldsymbol{x} = \boldsymbol{0}$. Hence $\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A)$. Moreover $\mathcal{R}(A^{\mathsf T}A) \subseteq \mathcal{R}(A^{\mathsf T})$, and by the **rank–nullity theorem**, $\operatorname{rank}(A^{\mathsf T}A) = n - \dim\mathcal{N}(A^{\mathsf T}A) = n - \dim\mathcal{N}(A) = \operatorname{rank}(A) = \operatorname{rank}(A^{\mathsf T})$, so $\mathcal{R}(A^{\mathsf T}A) = \mathcal{R}(A^{\mathsf T})$. Replacing $A$ by $A^{\mathsf T}$ gives the remaining two identities. $\square$

Combined with the dimension formulas of Chapter 3, the four fundamental subspaces pair up as orthogonal complements (let $\operatorname{rank}(A) = r$):

| Subspace | Ambient space | Dimension | Orthogonal complement |
|---|---|---|---|
| **column space** $\mathcal{R}(A)$ | $\mathbb{R}^m$ | $r$ | $\mathcal{N}(A^{\mathsf T})$ |
| **left null space** $\mathcal{N}(A^{\mathsf T})$ | $\mathbb{R}^m$ | $m - r$ | $\mathcal{R}(A)$ |
| row space $\mathcal{R}(A^{\mathsf T})$ | $\mathbb{R}^n$ | $r$ | $\mathcal{N}(A)$ |
| null space $\mathcal{N}(A)$ | $\mathbb{R}^n$ | $n - r$ | $\mathcal{R}(A^{\mathsf T})$ |

Consequently, $A\boldsymbol{x} = \boldsymbol{b}$ is solvable if and only if $\boldsymbol{b} \in \mathcal{R}(A) = \mathcal{N}(A^{\mathsf T})^\perp$, that is, $\boldsymbol{b}$ is orthogonal to every solution of $A^{\mathsf T}\boldsymbol{y} = \boldsymbol{0}$.

### 4.4.3. Orthogonal Projection onto a Subspace

Let $M$ be a subspace of $\mathbb{R}^n$. By Theorem 4.4.1, every $\boldsymbol{a} \in \mathbb{R}^n$ decomposes uniquely as $\boldsymbol{a} = \boldsymbol{a}_1 + \boldsymbol{a}_2$ with $\boldsymbol{a}_1 \in M$ and $\boldsymbol{a}_2 \in M^\perp$. By uniqueness, the decomposition of $\boldsymbol{a} + \boldsymbol{b}$ is the sum of the two decompositions and that of $k\boldsymbol{a}$ is $k$ times that of $\boldsymbol{a}$, so $\boldsymbol{a} \mapsto \boldsymbol{a}_1$ is a linear transformation. Taking an orthonormal basis $\boldsymbol{q}_1, \dots, \boldsymbol{q}_r$ of $M$ and setting $Q_r = [\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_r]$, we have

$$
\boldsymbol{a}_1 = (\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_1 + \cdots + (\boldsymbol{q}_r^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_r = (\boldsymbol{q}_1\boldsymbol{q}_1^{\mathsf T} + \cdots + \boldsymbol{q}_r\boldsymbol{q}_r^{\mathsf T})\boldsymbol{a} = Q_rQ_r^{\mathsf T}\boldsymbol{a}.
$$

**Definition 4.4.3 (Orthogonal Projection)** The linear transformation $P_M\colon \boldsymbol{a} \mapsto \boldsymbol{a}_1$ is called the **orthogonal projection** onto the subspace $M$, and $\boldsymbol{a}_1 = P_M(\boldsymbol{a})$ is called the orthogonal projection of the vector $\boldsymbol{a}$ onto $M$. Its matrix is $P_M = Q_rQ_r^{\mathsf T}$, where the columns of $Q_r$ form any orthonormal basis of $M$.

$P_M$ is determined by $M$ alone and does not depend on the choice of orthonormal basis (because the decomposition is unique). By definition:

- $I_n = P_M + P_{M^\perp}$, that is, $\boldsymbol{a} = P_M(\boldsymbol{a}) + P_{M^\perp}(\boldsymbol{a})$;
- $\boldsymbol{a} \in M$ if and only if $P_M(\boldsymbol{a}) = \boldsymbol{a}$; $\boldsymbol{a} \in M^\perp$ if and only if $P_M(\boldsymbol{a}) = \boldsymbol{0}$.

**Theorem 4.4.3 (Best Approximation)** Let $\boldsymbol{a}_1 = P_M(\boldsymbol{a})$. Then $\|\boldsymbol{a} - \boldsymbol{a}_1\| = \min\limits_{\boldsymbol{x} \in M} \|\boldsymbol{a} - \boldsymbol{x}\|$, and the minimum is attained only at $\boldsymbol{x} = \boldsymbol{a}_1$.

**Proof** For every $\boldsymbol{x} \in M$, $\boldsymbol{a} - \boldsymbol{x} = (\boldsymbol{a} - \boldsymbol{a}_1) + (\boldsymbol{a}_1 - \boldsymbol{x})$ with $\boldsymbol{a} - \boldsymbol{a}_1 \in M^\perp$ and $\boldsymbol{a}_1 - \boldsymbol{x} \in M$. By the Pythagorean theorem, $\|\boldsymbol{a} - \boldsymbol{x}\|^2 = \|\boldsymbol{a} - \boldsymbol{a}_1\|^2 + \|\boldsymbol{a}_1 - \boldsymbol{x}\|^2 \ge \|\boldsymbol{a} - \boldsymbol{a}_1\|^2$, with equality if and only if $\boldsymbol{x} = \boldsymbol{a}_1$. $\square$

### 4.4.4. Orthogonal Projection Matrices

The most common case is projection onto the column space of a matrix: $M = \mathcal{R}(A)$ and $M^\perp = \mathcal{N}(A^{\mathsf T})$.

**Definition 4.4.4 (Orthogonal Projection Matrix)** The matrix $P_{\mathcal{R}(A)}$ of the orthogonal projection onto the column space $\mathcal{R}(A)$ is called the **orthogonal projection matrix** of $A$, written $P_A$ for short.

Thus $I - P_A = P_{\mathcal{N}(A^{\mathsf T})}$; when $A$ is invertible, $\mathcal{R}(A) = \mathbb{R}^n$ and $P_A = I_n$. If the columns of $Q_r$ form an orthonormal basis of $\mathcal{R}(A)$, then $P_A = Q_rQ_r^{\mathsf T}$ and $\mathcal{R}(P_A) = \mathcal{R}(Q_r) = \mathcal{R}(A)$, so $P_A$ is also the orthogonal projection matrix of itself.

**Theorem 4.4.4** A square matrix $P$ of order $n$ is an orthogonal projection matrix if and only if $P^2 = P^{\mathsf T} = P$.

**Proof** Necessity: $P = Q_rQ_r^{\mathsf T}$ with $Q_r$ having orthonormal columns, so $P^{\mathsf T} = P$ and $P^2 = Q_r(Q_r^{\mathsf T}Q_r)Q_r^{\mathsf T} = P$.

Sufficiency: suppose $P^2 = P^{\mathsf T} = P$; we show that $P$ is the orthogonal projection matrix of itself. For every $\boldsymbol{x}$, $\boldsymbol{x} = P\boldsymbol{x} + (I_n - P)\boldsymbol{x}$ with $P\boldsymbol{x} \in \mathcal{R}(P)$, and $P^{\mathsf T}(I_n - P)\boldsymbol{x} = (P - P^2)\boldsymbol{x} = \boldsymbol{0}$, that is, $(I_n - P)\boldsymbol{x} \in \mathcal{N}(P^{\mathsf T}) = \mathcal{R}(P)^\perp$. By uniqueness of the decomposition, this is the decomposition belonging to the orthogonal projection onto $\mathcal{R}(P)$, so $P = P_{\mathcal{R}(P)}$. $\square$

The condition $P^2 = P$ says "projecting twice is the same as projecting once", and $P^{\mathsf T} = P$ says "the projection is along the perpendicular direction"; matrices satisfying only the first condition are oblique projections.

## 4.5. Least Squares Problems

### 4.5.1. Least Squares Solutions and the Normal Equations

**Definition 4.5.1 (Least Squares Problem)** Let $A$ be an $m \times n$ matrix and $\boldsymbol{b} \in \mathbb{R}^m$. The vector $\boldsymbol{r} = \boldsymbol{b} - A\boldsymbol{x}$ is called the residual. The problem of finding $\boldsymbol{x}$ that minimizes the length of the residual,

$$
\min_{\boldsymbol{x} \in \mathbb{R}^n} \|\boldsymbol{r}\| = \min_{\boldsymbol{x} \in \mathbb{R}^n} \|\boldsymbol{b} - A\boldsymbol{x}\|,
$$

is called a **least squares problem**, and its solutions are called least squares solutions of the linear system $A\boldsymbol{x} = \boldsymbol{b}$.

"Squares" refers to $\|\boldsymbol{b} - A\boldsymbol{x}\|^2$, the sum of the squared errors of the individual equations. As $\boldsymbol{x}$ varies, $A\boldsymbol{x}$ ranges over $\mathcal{R}(A)$, so by Theorem 4.4.3, $\boldsymbol{x}_0$ is a least squares solution if and only if $A\boldsymbol{x}_0 = P_A\boldsymbol{b}$; since $P_A\boldsymbol{b} \in \mathcal{R}(A)$, a least squares solution always exists.

**Theorem 4.5.1** $\boldsymbol{x}$ is a least squares solution of $A\boldsymbol{x} = \boldsymbol{b}$ if and only if

$$
A^{\mathsf T}A\boldsymbol{x} = A^{\mathsf T}\boldsymbol{b}. \tag{4.1}
$$

**Proof** Necessity: $\boldsymbol{r} = \boldsymbol{b} - A\boldsymbol{x} = \boldsymbol{b} - P_A\boldsymbol{b} \in \mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf T})$, that is, $A^{\mathsf T}(\boldsymbol{b} - A\boldsymbol{x}) = \boldsymbol{0}$. Sufficiency: if $A^{\mathsf T}A\boldsymbol{x} = A^{\mathsf T}\boldsymbol{b}$, then $\boldsymbol{b} - A\boldsymbol{x} \in \mathcal{N}(A^{\mathsf T}) = \mathcal{R}(A)^\perp$; also $\boldsymbol{b} - P_A\boldsymbol{b} \in \mathcal{R}(A)^\perp$, and subtracting gives $P_A\boldsymbol{b} - A\boldsymbol{x} \in \mathcal{R}(A) \cap \mathcal{R}(A)^\perp = \{\boldsymbol{0}\}$, that is, $A\boldsymbol{x} = P_A\boldsymbol{b}$. $\square$

**Definition 4.5.2 (Normal Equations)** The system (4.1) is called the **normal equations** of $A\boldsymbol{x} = \boldsymbol{b}$.

The lecture slides call the approach of "finding least squares solutions by solving the normal equations" the "regularization method"; to avoid confusion with regularization in statistics and machine learning (such as ridge regression), this site calls it the normal equations method. The normal equations have a clear geometric meaning: the residual $\boldsymbol{b} - A\boldsymbol{x}$ is orthogonal to every column of $A$.

**Property 4.5.1** Structure of the least squares solutions:

1. If $A$ has full column rank, then $A^{\mathsf T}A$ is invertible ($\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A) = \{\boldsymbol{0}\}$) and the least squares solution is unique: $\boldsymbol{x}_0 = (A^{\mathsf T}A)^{-1}A^{\mathsf T}\boldsymbol{b}$. In this case $A\boldsymbol{x}_0 = P_A\boldsymbol{b}$ holds for every $\boldsymbol{b}$, so
   $$
   P_A = A(A^{\mathsf T}A)^{-1}A^{\mathsf T};
   $$
2. If $A$ does not have full column rank and $\boldsymbol{x}_0$ is one least squares solution, then the set of all least squares solutions is $\{\boldsymbol{x}_0 + \boldsymbol{x}_1 \mid \boldsymbol{x}_1 \in \mathcal{N}(A)\}$ (the solution set of the normal equations, by $\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A)$). The one of minimal length is given by the Moore–Penrose pseudoinverse; see [Chapter 7](/2.1.7).

### 4.5.2. The Normal Equations Method and the Orthogonalization Method

When $A$ has full column rank, $A^{\mathsf T}A$ is symmetric positive definite ([Chapter 7](/2.1.7)) and has an $LDL^{\mathsf T}$ decomposition with positive diagonal entries (the symmetric case of the LDU decomposition of Chapter 2), so the normal equations reduce to three triangular or diagonal systems.

**Algorithm 4.5.1 (Normal Equations Method)** Let $A$ have full column rank.

1. Compute $C = A^{\mathsf T}A$ and $\boldsymbol{d} = A^{\mathsf T}\boldsymbol{b}$;
2. compute the factorization $C = LDL^{\mathsf T}$ ($L$ unit lower triangular, $D$ diagonal);
3. solve the lower triangular system $L\boldsymbol{z} = \boldsymbol{d}$ by forward substitution;
4. solve the diagonal system $D\boldsymbol{y} = \boldsymbol{z}$;
5. solve the upper triangular system $L^{\mathsf T}\boldsymbol{x} = \boldsymbol{y}$ by **back substitution**.

Another approach uses the QR decomposition. Let $A$ have full column rank and $A = QR = [Q_1\ Q_2]\begin{bmatrix} R_1 \\ O \end{bmatrix} = Q_1R_1$. Since orthogonal matrices preserve length,

$$
\|\boldsymbol{b} - A\boldsymbol{x}\|^2 = \|Q^{\mathsf T}(\boldsymbol{b} - QR\boldsymbol{x})\|^2 = \left\|\begin{bmatrix} Q_1^{\mathsf T}\boldsymbol{b} \\ Q_2^{\mathsf T}\boldsymbol{b} \end{bmatrix} - \begin{bmatrix} R_1 \\ O \end{bmatrix}\boldsymbol{x}\right\|^2 = \|Q_1^{\mathsf T}\boldsymbol{b} - R_1\boldsymbol{x}\|^2 + \|Q_2^{\mathsf T}\boldsymbol{b}\|^2.
$$

The second term does not depend on $\boldsymbol{x}$, and the first vanishes when $R_1\boldsymbol{x} = Q_1^{\mathsf T}\boldsymbol{b}$, so the least squares solution satisfies the upper triangular system $R_1\boldsymbol{x} = Q_1^{\mathsf T}\boldsymbol{b}$, and the minimal residual is $\|Q_2^{\mathsf T}\boldsymbol{b}\|$. From the projection point of view, $P_A = Q_1Q_1^{\mathsf T}$, and $A\boldsymbol{x}_0 = P_A\boldsymbol{b}$ reads $Q_1R_1\boldsymbol{x}_0 = Q_1Q_1^{\mathsf T}\boldsymbol{b}$; multiplying both sides on the left by $Q_1^{\mathsf T}$ gives the same equation.

**Algorithm 4.5.2 (Orthogonalization Method)** Let $A$ have full column rank.

1. Compute the reduced QR decomposition $A = Q_1R_1$;
2. compute $\boldsymbol{c} = Q_1^{\mathsf T}\boldsymbol{b}$;
3. solve the upper triangular system $R_1\boldsymbol{x} = \boldsymbol{c}$ by back substitution.

In practice one should solve the system $R_1\boldsymbol{x} = \boldsymbol{c}$ rather than first computing $R_1^{-1}$. When $A$ does not have full column rank, suitable column interchanges (QR decomposition with column pivoting) make the first $r$ columns of $Q_1$ an orthonormal basis of $\mathcal{R}(A)$.

Comparison of the two methods: the normal equations method is cheaper (the main cost is forming $A^{\mathsf T}A$, about $mn^2$ floating-point operations), but $\kappa(A^{\mathsf T}A) = \kappa(A)^2$, so rounding errors are amplified; the orthogonalization method (with Householder QR, about $2mn^2 - \frac{2}{3}n^3$ floating-point operations) works directly on $A$, is numerically more stable, and is the standard approach in numerical software.

**Example 4.5.1** Find the least squares solution of $A\boldsymbol{x} = \boldsymbol{b}$, where $A = [\boldsymbol{a}_1\ \boldsymbol{a}_2] = \begin{bmatrix} 1 & 1 \\ 2 & 1 \\ 1 & 3 \end{bmatrix}$ and $\boldsymbol{b} = \begin{bmatrix} 0 \\ 3 \\ 5 \end{bmatrix}$.

Normal equations method: $A^{\mathsf T}A = \begin{bmatrix} 6 & 6 \\ 6 & 11 \end{bmatrix}$ and $A^{\mathsf T}\boldsymbol{b} = \begin{bmatrix} 11 \\ 18 \end{bmatrix}$, which give $\boldsymbol{x} = \begin{bmatrix} 13/30 \\ 7/5 \end{bmatrix}$.

Orthogonalization method: Gram–Schmidt orthogonalization of $\boldsymbol{a}_1, \boldsymbol{a}_2$ gives $\tilde{\boldsymbol{q}}_1 = \boldsymbol{a}_1$ and $\tilde{\boldsymbol{q}}_2 = \boldsymbol{a}_2 - \frac{6}{6}\tilde{\boldsymbol{q}}_1 = \begin{bmatrix} 0 \\ -1 \\ 2 \end{bmatrix}$, so

$$
Q_1 = \begin{bmatrix} \frac{1}{\sqrt{6}} & 0 \\ \frac{2}{\sqrt{6}} & -\frac{1}{\sqrt{5}} \\ \frac{1}{\sqrt{6}} & \frac{2}{\sqrt{5}} \end{bmatrix}, \quad
R_1 = \begin{bmatrix} \sqrt{6} & \sqrt{6} \\ 0 & \sqrt{5} \end{bmatrix}, \quad
Q_1^{\mathsf T}\boldsymbol{b} = \begin{bmatrix} 11/\sqrt{6} \\ 7/\sqrt{5} \end{bmatrix}.
$$

Back substitution gives $x_2 = 7/5$ and $x_1 = 11/6 - 7/5 = 13/30$, in agreement with the normal equations method. The minimal residual is $\boldsymbol{r} = \boldsymbol{b} - A\boldsymbol{x} = \frac{11}{30}\begin{bmatrix} -5 \\ 2 \\ 1 \end{bmatrix}$, which is orthogonal to both $\boldsymbol{a}_1$ and $\boldsymbol{a}_2$.

The figure below shows Example 4.1.1 and this example side by side: projecting onto a line and projecting onto a column space are the same operation. The vector $A\boldsymbol{x}_0$ given by the least squares solution is the foot of the perpendicular from $\boldsymbol{b}$ to the plane $\mathcal{R}(A)$, and the residual is perpendicular to the whole plane.

![Left: in Example 4.1.1, the orthogonal projection of b onto the line span(a), with the residual r perpendicular to a; right: in Example 4.5.1, the orthogonal projection P_A b = A x_0 of b onto the column space R(A), with the residual r perpendicular to the plane R(A)](./plots/projection-geometry.py)

### 4.5.3. Data Fitting

An important application of least squares is data fitting. Suppose the variables $y$ and $t$ are related by some law $y = f(t)$ of unknown form, and measurements give data points $(t_1, y_1), \dots, (t_m, y_m)$. Assume that $f$ is a linear combination of known simple functions $f_1, \dots, f_n$:

$$
f(t) = x_1f_1(t) + x_2f_2(t) + \cdots + x_nf_n(t);
$$

determining $f$ then means finding the coefficients $x_1, \dots, x_n$. Let

$$
\boldsymbol{f}_j = \begin{bmatrix} f_j(t_1) \\ \vdots \\ f_j(t_m) \end{bmatrix}, \quad
A = [\boldsymbol{f}_1\ \cdots\ \boldsymbol{f}_n] = \begin{bmatrix} f_1(t_1) & \cdots & f_n(t_1) \\ \vdots & & \vdots \\ f_1(t_m) & \cdots & f_n(t_m) \end{bmatrix}, \quad
\boldsymbol{b} = \begin{bmatrix} y_1 \\ \vdots \\ y_m \end{bmatrix};
$$

then the conditions $f(t_i) = y_i$ ($i = 1, \dots, m$) are exactly $A\boldsymbol{x} = \boldsymbol{b}$. There are usually more data points than parameters ($m > n$), the measurements contain errors, and the chosen functional form is only an approximation, so this system generally has no solution, and we look for a least squares solution instead. Note that $f$ may be nonlinear in $t$: as long as it is linear in the unknown coefficients $\boldsymbol{x}$, the problem is a linear least squares problem. Common choices:

| Fit | Functional form | Basis functions $f_j$ |
|---|---|---|
| linear fit | $f(t) = kt + a$ | $t,\ 1$ |
| quadratic fit | $f(t) = at^2 + bt + c$ | $t^2,\ t,\ 1$ |
| polynomial fit | $f(t) = a_nt^n + \cdots + a_1t + a_0$ | $t^n, \dots, t, 1$ |

For polynomial fitting, $A$ is the **Vandermonde matrix** of Chapter 5 (its first $n+1$ columns).

**Example 4.5.2 (Simple Linear Fit)** Given data $(t_1, y_1), \dots, (t_m, y_m)$, fit $y = kt + a$. Write $\boldsymbol{t} = [t_i]$, $\boldsymbol{1} = [1\ \cdots\ 1]^{\mathsf T}$ and $\boldsymbol{b} = [y_i]$; then $A = [\boldsymbol{t}\ \boldsymbol{1}]$ and $\boldsymbol{x} = \begin{bmatrix} k \\ a \end{bmatrix}$. As long as the $t_i$ are not all equal, $A$ has full column rank and the least squares solution is unique. The normal equations are

$$
\begin{bmatrix} \boldsymbol{t}^{\mathsf T}\boldsymbol{t} & \boldsymbol{1}^{\mathsf T}\boldsymbol{t} \\ \boldsymbol{1}^{\mathsf T}\boldsymbol{t} & m \end{bmatrix}\begin{bmatrix} k \\ a \end{bmatrix} = \begin{bmatrix} \boldsymbol{t}^{\mathsf T}\boldsymbol{b} \\ \boldsymbol{1}^{\mathsf T}\boldsymbol{b} \end{bmatrix},
$$

with solution

$$
k = \frac{1}{c}\left(\boldsymbol{t}^{\mathsf T}\boldsymbol{b} - \frac{1}{m}(\boldsymbol{1}^{\mathsf T}\boldsymbol{t})(\boldsymbol{1}^{\mathsf T}\boldsymbol{b})\right), \qquad
a = \frac{1}{cm}\left((\boldsymbol{t}^{\mathsf T}\boldsymbol{t})(\boldsymbol{1}^{\mathsf T}\boldsymbol{b}) - (\boldsymbol{1}^{\mathsf T}\boldsymbol{t})(\boldsymbol{t}^{\mathsf T}\boldsymbol{b})\right), \qquad
c = \boldsymbol{t}^{\mathsf T}\boldsymbol{t} - \frac{1}{m}(\boldsymbol{1}^{\mathsf T}\boldsymbol{t})^2.
$$

In terms of the means $\bar{t} = \frac{1}{m}\sum t_i$ and $\bar{y} = \frac{1}{m}\sum y_i$, this is $k = \dfrac{\sum (t_i - \bar{t})(y_i - \bar{y})}{\sum (t_i - \bar{t})^2}$ and $a = \bar{y} - k\bar{t}$, the coefficient formulas of simple linear regression in statistics; the fitted line always passes through the point $(\bar{t}, \bar{y})$.

**Remark 4.5.1** When the fitting function is nonlinear in the parameters, a transformation can sometimes turn the problem into a linear one. For example, taking logarithms of $y = a\mathrm{e}^{bt}$ gives $\ln y = \ln a + bt$, a linear fit to the data $(t_i, \ln y_i)$; and $y = a/(t + b)$ can be written as $1/y = t/a + b/a$. However, what is then minimized is the sum of squared errors of the transformed problem, whose solution generally differs from the least squares solution of the original problem; when the optimum of the original problem is needed, one must use iterative methods for nonlinear least squares.

The figure below fits the same data with a line and with a parabola using the QR decomposition (Algorithm 4.5.2); the vertical segments are the components of the residual. The quadratic fit has a markedly smaller residual sum of squares.

![Linear and quadratic fits to the same data; the red vertical segments show the residuals](./plots/least-squares-fit.py)

## Summary {#summary}

The core of this chapter is orthogonalization: once we have an orthonormal basis, coordinates, projections and least squares all require nothing more than inner products.

| Concept or result | Content | Location |
|---|---|---|
| Inner product, length, angle | $\boldsymbol{a}^{\mathsf T}\boldsymbol{b}$; $\Vert \boldsymbol{a}\Vert = \sqrt{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}$; $\arccos\frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\Vert \boldsymbol{a}\Vert \Vert \boldsymbol{b}\Vert }$ | Section 4.1 |
| Cauchy–Schwarz, triangle inequality, Pythagorean theorem | $\vert \boldsymbol{a}^{\mathsf T}\boldsymbol{b}\vert \le \Vert \boldsymbol{a}\Vert \Vert \boldsymbol{b}\Vert$ | Theorem 4.1.1, Corollary 4.1.1, Theorem 4.1.2 |
| Orthonormal bases | exist and can be extended; coordinates are $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}$ | Theorem 4.2.1, Theorem 4.2.2 |
| Orthogonal matrices | $Q^{\mathsf T}Q = I$; $Q^{-1} = Q^{\mathsf T}$; preserve length and inner products | Theorem 4.3.1, Theorem 4.3.2 |
| Givens rotations / Householder reflections | plane rotation $G_{\theta;i,j}$; reflection $H_{\boldsymbol{v}} = I - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}$ | Definition 4.3.2, Definition 4.3.3 |
| QR decomposition | $A = QR = Q_1R_1$; unique for invertible $A$ | Theorem 4.3.3, Theorem 4.3.4 |
| Orthogonal complements | $\dim M^\perp = n - \dim M$; $\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf T})$; $\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A)$ | Theorem 4.4.1, Theorem 4.4.2 |
| Orthogonal projections | $P_M = Q_rQ_r^{\mathsf T}$; best approximation; $P^2 = P^{\mathsf T} = P$ | Theorem 4.4.3, Theorem 4.4.4 |
| Least squares | $A\boldsymbol{x}_0 = P_A\boldsymbol{b}$ ⇔ $A^{\mathsf T}A\boldsymbol{x}_0 = A^{\mathsf T}\boldsymbol{b}$; for full column rank $P_A = A(A^{\mathsf T}A)^{-1}A^{\mathsf T}$ | Theorem 4.5.1, Property 4.5.1 |

| Algorithm | Input → output | Key point |
|---|---|---|
| Gram–Schmidt process (Algorithm 4.2.1) | a basis → an orthonormal basis | subtract projections onto the directions already found, then normalize |
| Gram–Schmidt QR (Algorithm 4.3.1) | $A$ of full column rank → $Q_1R_1$ | $r_{ij} = \boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$; the modified version is numerically better |
| Householder QR (Algorithm 4.3.2) | $A$ → $QR$ | eliminate column by column with reflections; numerically stable, the standard in software |
| Normal equations method (Algorithm 4.5.1) | $A, \boldsymbol{b}$ → least squares solution | $A^{\mathsf T}A = LDL^{\mathsf T}$, then three triangular/diagonal solves |
| Orthogonalization method (Algorithm 4.5.2) | $A, \boldsymbol{b}$ → least squares solution | $R_1\boldsymbol{x} = Q_1^{\mathsf T}\boldsymbol{b}$; more stable than the normal equations |
