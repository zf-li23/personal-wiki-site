---
title: Matrices and Systems of Linear Equations
source_hash: 0c4cfac9b207
---

Linear algebra studies linear relations among variables in many dimensions. Single-variable calculus deals with nonlinear functions of one variable; linear algebra deals with functions $\boldsymbol{y} = A\boldsymbol{x}$ whose inputs and outputs are vectors but whose rule is linear. Multivariable calculus ([2.2](/2.2)) combines the two, and its central technique is precisely local linearization. This chapter starts from vectors and linear operations in $\mathbb{R}^m$ and introduces linear maps and the matrices that represent them. The most basic problem of linear algebra, solving a system of linear equations, asks for the preimage of a given image. We reduce a system to echelon form by elementary operations, which yields a standard procedure for solving it (Gaussian elimination and Gauss–Jordan elimination) together with a criterion for solvability. Finally, the sum, scalar multiple and composition of maps lead to the linear operations on matrices, the transpose and matrix multiplication.

The linear maps of this chapter are special cases of the **linear maps** between **vector spaces** over a field in [1.3.3](/1.3.3#sec-3.6.3); here we work only in $\mathbb{R}^n$ and postpone general vector spaces to [Chapter 8](/2.1.8). The next chapter describes each step of elimination by a matrix multiplication and discusses inverse matrices and the LU decomposition; [Chapter 3](/2.1.3) uses the language of subspaces to settle completely the structure of the solution set.

## 1.1. Vectors and Linear Operations

A plane vector $\boldsymbol{a} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$ can be added to another vector and multiplied by a real number, and every plane vector can be written as a combination $x_1\boldsymbol{e}_1 + x_2\boldsymbol{e}_2$ of $\boldsymbol{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\boldsymbol{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$. These notions and operations generalize verbatim to $m$ dimensions.

**Definition 1.1.1 ($m$-Dimensional Vector)** Let $a_1, a_2, \dots, a_m \in \mathbb{R}$. The ordered $m$-tuple

$$
\boldsymbol{a} = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_m \end{bmatrix}
$$

is called an $m$-dimensional (real) vector, and $a_i$ is called the $i$-th component, or coordinate, of $\boldsymbol{a}$. The set of all $m$-dimensional real vectors is denoted by $\mathbb{R}^m$. The vector $\boldsymbol{a}$ is also called a column vector, and $\boldsymbol{a}^{\mathsf T} = [a_1\ a_2\ \cdots\ a_m]$ is called a row vector, where the superscript $\mathsf T$ denotes the transpose. Vectors with complex components are complex vectors, and the set of all $m$-dimensional complex vectors is denoted by $\mathbb{C}^m$.

Vectors are denoted by bold lowercase letters. Two vectors are equal if all their corresponding components are equal.

**Definition 1.1.2 (Linear Operations on Vectors)** Addition and scalar multiplication on $\mathbb{R}^m$ are defined by

$$
\begin{bmatrix} a_1 \\ \vdots \\ a_m \end{bmatrix} + \begin{bmatrix} b_1 \\ \vdots \\ b_m \end{bmatrix} := \begin{bmatrix} a_1 + b_1 \\ \vdots \\ a_m + b_m \end{bmatrix}, \qquad
k\begin{bmatrix} a_1 \\ \vdots \\ a_m \end{bmatrix} := \begin{bmatrix} ka_1 \\ \vdots \\ ka_m \end{bmatrix}, \quad k \in \mathbb{R}.
$$

Together they are called the linear operations on vectors.

The set $\mathbb{R}^m$ is closed under the linear operations; together with these two operations it is called a linear space or **vector space**. Vectors of different dimensions (such as vectors in $\mathbb{R}^m$ and in $\mathbb{R}^n$ with $m \ne n$) cannot be added. We also define the **inner product** of two vectors $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^m$,

$$
\boldsymbol{a} \cdot \boldsymbol{b} = a_1b_1 + a_2b_2 + \cdots + a_mb_m = \sum_{j=1}^m a_jb_j \in \mathbb{R},
$$

which is related to geometric properties such as length, angle and orthogonality; these are discussed in [Chapter 4](/2.1.4).

**Property 1.1.1 (Rules for the Linear Operations)** For all $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c} \in \mathbb{R}^m$ and $k, \ell \in \mathbb{R}$:

1. associativity of addition: $(\boldsymbol{a} + \boldsymbol{b}) + \boldsymbol{c} = \boldsymbol{a} + (\boldsymbol{b} + \boldsymbol{c})$;
2. commutativity of addition: $\boldsymbol{a} + \boldsymbol{b} = \boldsymbol{b} + \boldsymbol{a}$;
3. zero vector: $\boldsymbol{0} = [0\ \cdots\ 0]^{\mathsf T}$ satisfies $\boldsymbol{a} + \boldsymbol{0} = \boldsymbol{a}$, and $0\boldsymbol{a} = \boldsymbol{0}$;
4. negative vector: $-\boldsymbol{a} = [-a_1\ \cdots\ -a_m]^{\mathsf T}$ satisfies $\boldsymbol{a} + (-\boldsymbol{a}) = \boldsymbol{0}$, and $(-1)\boldsymbol{a} = -\boldsymbol{a}$;
5. unit scalar: $1\boldsymbol{a} = \boldsymbol{a}$;
6. associativity of scalar multiplication: $(k\ell)\boldsymbol{a} = k(\ell\boldsymbol{a})$;
7. distributivity over scalar addition: $(k + \ell)\boldsymbol{a} = k\boldsymbol{a} + \ell\boldsymbol{a}$;
8. distributivity over vector addition: $k(\boldsymbol{a} + \boldsymbol{b}) = k\boldsymbol{a} + k\boldsymbol{b}$.

Negative vectors allow us to define subtraction, $\boldsymbol{a} - \boldsymbol{b} = \boldsymbol{a} + (-\boldsymbol{b})$. These eight rules guarantee that vectors can be manipulated formally like numbers, for example $2(\boldsymbol{a} + 4\boldsymbol{b}) - \boldsymbol{a} + 3\boldsymbol{b} = \boldsymbol{a} + 11\boldsymbol{b}$; they are exactly the concrete form of the vector space axioms ([Definition 3.6.1](/1.3.3#def-3.6.1)) in [1.3.3](/1.3.3).

**Definition 1.1.3 (Linear Combination and Linear Representation)** Given vectors $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ in $\mathbb{R}^m$ and numbers $k_1, \dots, k_n \in \mathbb{R}$, the vector $k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n$ is called a **linear combination** of these vectors. If $\boldsymbol{b} \in \mathbb{R}^m$ can be written as $\boldsymbol{b} = k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n$, we say that $\boldsymbol{b}$ can be linearly represented by (or is a linear combination of) $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$. The vectors

$$
\boldsymbol{e}_1 = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix}, \quad \boldsymbol{e}_2 = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix}, \quad \dots, \quad \boldsymbol{e}_m = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}
$$

are called the standard coordinate vectors of $\mathbb{R}^m$, and $\boldsymbol{e}_i$ is the $i$-th standard coordinate vector.

Every $\boldsymbol{x} \in \mathbb{R}^m$ is a linear combination of the standard coordinate vectors: $\boldsymbol{x} = x_1\boldsymbol{e}_1 + x_2\boldsymbol{e}_2 + \cdots + x_m\boldsymbol{e}_m$. Note that the bold symbols $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ denote $n$ vectors, as opposed to the components $a_1, \dots, a_m$ of a single vector.

## 1.2. Linear Maps

First recall the notion of a **map** (a function in [1.2.3](/1.2.3)). Let $X$ and $Y$ be sets. If a rule $f$ assigns to each element $x$ of $X$ a unique element $f(x)$ of $Y$, then $f\colon X \to Y$ is called a map. The set $X$ is the **domain** of $f$ and $Y$ is its codomain; $y = f(x)$ is called the image of $x$, and $x$ a preimage of $y$; the set $f(X) = \{f(x) \mid x \in X\} \subseteq Y$ is called the image or **range** of $f$. Two maps $f, g\colon X \to Y$ are equal if and only if $f(x) = g(x)$ for all $x \in X$. Every element of $X$ has exactly one image, but an element of $Y$ need not have a preimage, and when it has one, the preimage need not be unique. A map whose domain and codomain coincide is called a transformation of $X$; the **identity map** $\mathrm{id}_X$ sends each $x$ to itself.

**Definition 1.2.1 (Linear Map)** A map $f\colon \mathbb{R}^n \to \mathbb{R}^m$ satisfying the superposition principle is called a linear map from $\mathbb{R}^n$ to $\mathbb{R}^m$; a linear map from $\mathbb{R}^n$ to itself is called a **linear transformation** of $\mathbb{R}^n$. The superposition principle consists of the following two properties:

1. additivity: $f(\boldsymbol{x} + \boldsymbol{x}') = f(\boldsymbol{x}) + f(\boldsymbol{x}')$ for all $\boldsymbol{x}, \boldsymbol{x}' \in \mathbb{R}^n$;
2. homogeneity: $f(k\boldsymbol{x}) = kf(\boldsymbol{x})$ for all $\boldsymbol{x} \in \mathbb{R}^n$ and $k \in \mathbb{R}$.

The two properties can be combined into $f(k\boldsymbol{x} + \ell\boldsymbol{y}) = kf(\boldsymbol{x}) + \ell f(\boldsymbol{y})$. Taking $k = 0$ gives $f(\boldsymbol{0}_n) = \boldsymbol{0}_m$: a linear map sends the zero vector to the zero vector. The identity transformation $\mathrm{id}\colon \boldsymbol{x} \mapsto \boldsymbol{x}$ is a linear transformation.

**Example 1.2.1** Among maps $f\colon \mathbb{R} \to \mathbb{R}$, $f(x) = 3x$ and $f(x) = 0$ are linear, while $f(x) = x + 1$, $f(x) = x^2$, $f(x) = |x|$ and $f(x) = 1$ are not. By homogeneity, every linear map $\mathbb{R} \to \mathbb{R}$ has the form $f(x) = f(1)\,x$, that is, it is a proportional function.

**Example 1.2.2 (Transformations of the Plane)**

- A translation $T_{\boldsymbol{a}}\colon \boldsymbol{x} \mapsto \boldsymbol{x} + \boldsymbol{a}$ ($\boldsymbol{a} \ne \boldsymbol{0}$) is not a linear transformation, because $T_{\boldsymbol{a}}(\boldsymbol{0}) = \boldsymbol{a} \ne \boldsymbol{0}$.
- The rotation $R_\theta$ counterclockwise about the origin through the angle $\theta$ is a linear transformation. It sends $\boldsymbol{e}_1, \boldsymbol{e}_2$ to $[\cos\theta\ \sin\theta]^{\mathsf T}$ and $[-\sin\theta\ \cos\theta]^{\mathsf T}$ respectively, so by linearity

  $$
  R_\theta\left(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}\right) = x_1R_\theta(\boldsymbol{e}_1) + x_2R_\theta(\boldsymbol{e}_2) = x_1\begin{bmatrix} \cos\theta \\ \sin\theta \end{bmatrix} + x_2\begin{bmatrix} -\sin\theta \\ \cos\theta \end{bmatrix}.
  $$

  Thus the rotation is completely determined by the images of the standard coordinate vectors.
- The reflection $H_\theta$ in the line $\ell_\theta: x_2\cos\theta - x_1\sin\theta = 0$ through the origin (which makes the angle $\theta$ with the $x_1$-axis) is a linear transformation; a reflection in a line not through the origin is not linear.

The rotation example illustrates a general rule. Let $f\colon \mathbb{R}^n \to \mathbb{R}^m$ be a linear map and put $\boldsymbol{a}_i = f(\boldsymbol{e}_i) \in \mathbb{R}^m$. For $\boldsymbol{x} = x_1\boldsymbol{e}_1 + \cdots + x_n\boldsymbol{e}_n$,

$$
f(\boldsymbol{x}) = x_1f(\boldsymbol{e}_1) + \cdots + x_nf(\boldsymbol{e}_n) = x_1\boldsymbol{a}_1 + \cdots + x_n\boldsymbol{a}_n,
$$

so $f$ is completely determined by the images of the standard coordinate vectors.

**Theorem 1.2.1 (A Linear Map Is Determined by the Images of the Standard Coordinate Vectors)** For any $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n \in \mathbb{R}^m$ there is a unique linear map $f\colon \mathbb{R}^n \to \mathbb{R}^m$ such that $f(\boldsymbol{e}_i) = \boldsymbol{a}_i$ ($i = 1, \dots, n$).

**Proof** Existence: define $f(\boldsymbol{x}) = x_1\boldsymbol{a}_1 + \cdots + x_n\boldsymbol{a}_n$. By the rules for vector operations, $f(k\boldsymbol{x} + \ell\boldsymbol{y}) = \sum_i (kx_i + \ell y_i)\boldsymbol{a}_i = kf(\boldsymbol{x}) + \ell f(\boldsymbol{y})$, so $f$ is linear, and $f(\boldsymbol{e}_i) = \boldsymbol{a}_i$. Uniqueness: if linear maps $f, g$ satisfy $f(\boldsymbol{e}_i) = g(\boldsymbol{e}_i)$, then for every $\boldsymbol{x}$, $f(\boldsymbol{x}) = \sum_i x_if(\boldsymbol{e}_i) = \sum_i x_ig(\boldsymbol{e}_i) = g(\boldsymbol{x})$, hence $f = g$. $\square$

## 1.3. Matrices and Matrix–Vector Products

Writing $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ side by side in a table gives a complete "numerical representation" of a linear map.

**Definition 1.3.1 (Matrix)** A rectangular array of $mn$ real numbers $a_{ij}$ ($i = 1, \dots, m$; $j = 1, \dots, n$) arranged in $m$ rows and $n$ columns,

$$
A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} = [a_{ij}]_{m \times n},
$$

is called an $m \times n$ **matrix**, and $a_{ij}$ is called the $(i, j)$ entry of $A$. When $m = n$, $A$ is called a square matrix of order $n$. Two matrices are equal if they have the same numbers of rows and columns and all their corresponding entries are equal. The set of all real $m \times n$ matrices is denoted by $\mathbb{R}^{m \times n}$.

Matrices are denoted by capital letters; when a double subscript is ambiguous we separate the indices by a comma, as in $a_{i,j-1}$. An $m$-dimensional column vector is an $m \times 1$ matrix, and an $n$-dimensional row vector is a $1 \times n$ matrix. A matrix can be viewed either as $n$ column vectors placed side by side or as $m$ row vectors stacked on top of one another:

$$
A = [\boldsymbol{a}_1\ \boldsymbol{a}_2\ \cdots\ \boldsymbol{a}_n] = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T} \\ \vdots \\ \tilde{\boldsymbol{a}}_m^{\mathsf T} \end{bmatrix}, \qquad \boldsymbol{a}_j = \begin{bmatrix} a_{1j} \\ \vdots \\ a_{mj} \end{bmatrix} \in \mathbb{R}^m, \quad \tilde{\boldsymbol{a}}_i^{\mathsf T} = [a_{i1}\ \cdots\ a_{in}].
$$

**Definition 1.3.2 (Standard Matrix)** Let $f\colon \mathbb{R}^n \to \mathbb{R}^m$ be a linear map and $\boldsymbol{a}_i = f(\boldsymbol{e}_i)$ ($i = 1, \dots, n$). The $m \times n$ matrix $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ is called the **standard matrix** of $f$, that is, the matrix of $f$ with respect to the standard coordinate vectors.

By Theorem 1.2.1, linear maps $\mathbb{R}^n \to \mathbb{R}^m$ correspond one-to-one to $m \times n$ matrices: each linear map is completely determined by its standard matrix, and each matrix determines a unique linear map. The linear map corresponding to a matrix $A$ is denoted by $T_A\colon \mathbb{R}^n \to \mathbb{R}^m$, $T_A(\boldsymbol{x}) = A\boldsymbol{x}$ (the product $A\boldsymbol{x}$ is defined below).

**Definition 1.3.3 (Product of a Matrix and a Vector)** The product of an $m \times n$ matrix $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ and an $n$-dimensional column vector $\boldsymbol{x}$ is defined by

$$
A\boldsymbol{x} = x_1\boldsymbol{a}_1 + x_2\boldsymbol{a}_2 + \cdots + x_n\boldsymbol{a}_n = \begin{bmatrix} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \\ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n \end{bmatrix} = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{x} \\ \vdots \\ \tilde{\boldsymbol{a}}_m^{\mathsf T}\boldsymbol{x} \end{bmatrix}.
$$

Thus a linear map can be written as $f(\boldsymbol{x}) = T_A(\boldsymbol{x}) = A\boldsymbol{x}$. There are two ways to view the product:

- Column view: $A\boldsymbol{x}$ is a linear combination of the columns of $A$, with the components of $\boldsymbol{x}$ as coefficients; the number of columns of $A$ must equal the dimension of $\boldsymbol{x}$.
- Row view: the $i$-th component of $A\boldsymbol{x}$ is the inner product $\tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{x}$ of the $i$-th row with $\boldsymbol{x}$, and depends only on the $i$-th row of $A$. In particular, the inner product of two vectors of the same dimension is the product of a row vector and a column vector: $\boldsymbol{a} \cdot \boldsymbol{b} = \boldsymbol{a}^{\mathsf T}\boldsymbol{b}$.

**Proposition 1.3.1 (Distributive Law)** Let $A$ be an $m \times n$ matrix. For all $\boldsymbol{x}_1, \boldsymbol{x}_2 \in \mathbb{R}^n$ and $k_1, k_2 \in \mathbb{R}$, $A(k_1\boldsymbol{x}_1 + k_2\boldsymbol{x}_2) = k_1(A\boldsymbol{x}_1) + k_2(A\boldsymbol{x}_2)$.

This is merely the matrix form of the statement "$T_A$ is a linear map".

**Example 1.3.1** The $3 \times 2$ matrix $\begin{bmatrix} 2 & 0 \\ 1 & 1 \\ 0 & 1 \end{bmatrix}$ maps $\mathbb{R}^2$ onto the plane in $\mathbb{R}^3$ spanned by its two columns; the $2 \times 3$ matrix $\begin{bmatrix} 1 & 0 & 3 \\ 1 & 2 & 2 \end{bmatrix}$ maps $\mathbb{R}^3$ to $\mathbb{R}^2$; the $1 \times 2$ matrix $[1\ \ 1]$ maps $\mathbb{R}^2$ to $\mathbb{R}$, namely by taking the inner product with $[1\ 1]^{\mathsf T}$. In general, every $\boldsymbol{a} \in \mathbb{R}^n$ gives a linear map $\mathbb{R}^n \to \mathbb{R}$, $\boldsymbol{x} \mapsto \boldsymbol{a}^{\mathsf T}\boldsymbol{x}$.

## 1.4. Linear Transformations of the Plane and Special Square Matrices

By Definition 1.3.2, the standard matrix of a linear transformation of the plane is obtained by placing the images of $\boldsymbol{e}_1, \boldsymbol{e}_2$ side by side. The common ones are summarized below ($k, \ell \in \mathbb{R}$):

| Transformation | Action | Standard matrix |
|---|---|---|
| Rotation $R_\theta$ | rotates counterclockwise about the origin through $\theta$ | $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ |
| Reflection $H_\theta$ | reflects in the line $\ell_\theta$ | $\begin{bmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{bmatrix}$ |
| Swap | interchanges the two components (reflection in the line $x_2 = x_1$) | $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ |
| Stretch | multiplies the $x_1$-direction by $k$ and the $x_2$-direction by $\ell$ | $\begin{bmatrix} k & 0 \\ 0 & \ell \end{bmatrix}$ |
| Projection | projects onto the $x_1$-axis (a stretch with $\ell = 0$) | $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ |
| Shear $S_k$ | $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \mapsto \begin{bmatrix} x_1 + kx_2 \\ x_2 \end{bmatrix}$ | $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$ |

A shear turns the square spanned by $\boldsymbol{e}_1, \boldsymbol{e}_2$ into a parallelogram of the same area. The figure below shows the effect of these transformations on a grid and on the unit square:

![The effect of several linear transformations of the plane on a grid (blue) and on the unit square (orange); the red arrows are the images of the standard coordinate vectors](./plots/plane-transformations.py)

An example in three dimensions: for a fixed $\boldsymbol{a} \in \mathbb{R}^3$, the cross product $\boldsymbol{b} \mapsto \boldsymbol{a} \times \boldsymbol{b} = [a_2b_3 - a_3b_2\ \ a_3b_1 - a_1b_3\ \ a_1b_2 - a_2b_1]^{\mathsf T}$ is a linear transformation of $\mathbb{R}^3$ with standard matrix

$$
\begin{bmatrix} 0 & -a_3 & a_2 \\ a_3 & 0 & -a_1 \\ -a_2 & a_1 & 0 \end{bmatrix}.
$$

The entries of a square matrix whose row and column indices agree are called its diagonal entries. The following classes of square matrices have a simple structure and play a key role in solving systems (zero entries are often left blank).

**Definition 1.4.1 (Special Square Matrices)**

1. The square matrix of order $n$ whose diagonal entries are all $1$ and whose other entries are all $0$ is called the **identity matrix** of order $n$, denoted by $I_n = [\boldsymbol{e}_1\ \cdots\ \boldsymbol{e}_n]$.
2. A square matrix whose off-diagonal entries are all $0$ is called a **diagonal matrix**, denoted by $D = \operatorname{diag}(d_1, \dots, d_n)$.
3. A square matrix $U = [u_{ij}]$ whose entries below the diagonal are all $0$ is called upper triangular; a square matrix $L = [\ell_{ij}]$ whose entries above the diagonal are all $0$ is called lower triangular; a matrix of either kind is called a **triangular matrix**. If in addition the diagonal entries are all $0$, the matrix is strictly upper (lower) triangular; if the diagonal entries are all $1$, it is unit upper (lower) triangular.

Geometrically, $I_n\boldsymbol{x} = \boldsymbol{x}$ is the identity transformation; $D\boldsymbol{x} = [d_1x_1\ \cdots\ d_nx_n]^{\mathsf T}$ stretches along the coordinate axes; a unit upper triangular matrix is a shear of $\mathbb{R}^n$. The products of triangular matrices with a vector are

$$
U\boldsymbol{x} = \begin{bmatrix} u_{11}x_1 + u_{12}x_2 + \cdots + u_{1n}x_n \\ u_{22}x_2 + \cdots + u_{2n}x_n \\ \vdots \\ u_{nn}x_n \end{bmatrix}, \qquad
L\boldsymbol{x} = \begin{bmatrix} \ell_{11}x_1 \\ \ell_{21}x_1 + \ell_{22}x_2 \\ \vdots \\ \ell_{n1}x_1 + \ell_{n2}x_2 + \cdots + \ell_{nn}x_n \end{bmatrix}.
$$

## 1.5. Systems of Linear Equations

The most basic and most common application of linear algebra is solving systems of linear equations.

**Definition 1.5.1 (System of Linear Equations)** Given an $m \times n$ matrix $A = [a_{ij}]$ and $\boldsymbol{b} \in \mathbb{R}^m$, the system of equations in the unknowns $x_1, \dots, x_n$

$$
\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1, \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2, \\ \quad\vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m, \end{cases}
\qquad \text{i.e.} \qquad A\boldsymbol{x} = \boldsymbol{b},
$$

is called a **system of linear equations**; $A$ is its coefficient matrix and $\boldsymbol{b}$ its right-hand side. The number of equations $m$ need not equal the number of unknowns $n$.

There are three geometric pictures of solving a linear system:

- The map picture: find the preimage $\boldsymbol{x}$ of a given vector $\boldsymbol{b}$ under the linear map $T_A$.
- The row picture: the $i$-th equation $\tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{x} = b_i$ is an $(n-1)$-dimensional (affine) hyperplane in $\mathbb{R}^n$, and solving the system means finding the intersection of $m$ hyperplanes.
- The column picture: $A\boldsymbol{x} = x_1\boldsymbol{a}_1 + \cdots + x_n\boldsymbol{a}_n = \boldsymbol{b}$, and solving the system means finding a linear combination of the columns equal to $\boldsymbol{b}$.

For the system $x_1 + x_2 = 8$, $2x_1 + 4x_2 = 22$ of Example 1.6.1, the last two pictures are shown below: in the row picture the two lines meet at $(5, 3)$; in the column picture $\boldsymbol{b} = [8\ 22]^{\mathsf T}$ is exactly $5\boldsymbol{a}_1 + 3\boldsymbol{a}_2$.

![Two pictures of the same system. Left: the row picture, where each equation is a line and the solution is the intersection point (5, 3). Right: the column picture, where the solution gives the coefficients of a combination of the columns, b = 5a₁ + 3a₂](./plots/row-column-pictures.py)

A linear system has only three possibilities: no solution, exactly one solution, or infinitely many solutions (Theorem 1.7.2).

When the coefficient matrix is one of the special square matrices, the system is easy to solve: the solution of $I_n\boldsymbol{x} = \boldsymbol{b}$ is $\boldsymbol{x} = \boldsymbol{b}$; the solution of $D\boldsymbol{x} = \boldsymbol{b}$ is $x_i = b_i / d_i$ when all diagonal entries are nonzero; and a triangular system can be solved for one unknown at a time.

**Algorithm 1.5.1 (Back Substitution)** Let $U$ be an upper triangular matrix of order $n$ with nonzero diagonal entries. To solve $U\boldsymbol{x} = \boldsymbol{b}$, first compute $x_n = b_n / u_{nn}$; then for $i = n-1, \dots, 1$ compute in turn

$$
x_i = \frac{1}{u_{ii}}\left(b_i - \sum_{j=i+1}^n u_{ij}x_j\right).
$$

This method, which solves from the bottom up, from $x_n$ to $x_1$, is called back substitution.

**Algorithm 1.5.2 (Forward Substitution)** Let $L$ be a lower triangular matrix of order $n$ with nonzero diagonal entries. To solve $L\boldsymbol{x} = \boldsymbol{b}$, first compute $x_1 = b_1 / \ell_{11}$; then for $i = 2, \dots, n$ compute in turn

$$
x_i = \frac{1}{\ell_{ii}}\left(b_i - \sum_{j=1}^{i-1} \ell_{ij}x_j\right).
$$

In both algorithms the $i$-th unknown costs at most $n-1$ multiplications and additions or subtractions and one division, about $n^2$ floating-point operations in total. For a general coefficient matrix we would like to reduce it to triangular form first, which is exactly what elimination does.

## 1.6. Elementary Operations

**Example 1.6.1** Solve $\begin{cases} x_1 + x_2 = 8, \\ 2x_1 + 4x_2 = 22. \end{cases}$ We perform three operations in turn: add $-2$ times the first equation to the second, which gives $2x_2 = 6$; multiply the second equation by $\frac12$, which gives $x_2 = 3$; add $-1$ times the second equation to the first, which gives $x_1 = 5$. Only the coefficients and the right-hand sides take part in the computation. Writing them side by side as one matrix, the process can be abbreviated as

$$
\begin{bmatrix} 1 & 1 & 8 \\ 2 & 4 & 22 \end{bmatrix} \to \begin{bmatrix} 1 & 1 & 8 \\ 0 & 2 & 6 \end{bmatrix} \to \begin{bmatrix} 1 & 1 & 8 \\ 0 & 1 & 3 \end{bmatrix} \to \begin{bmatrix} 1 & 0 & 5 \\ 0 & 1 & 3 \end{bmatrix},
$$

and the unique solution is $x_1 = 5$, $x_2 = 3$. The coefficient matrix first becomes upper triangular and then becomes the identity matrix.

**Example 1.6.2** Solve $\begin{cases} 2x_2 - x_3 = 1, \\ x_1 - x_2 + x_3 = 0, \\ 2x_1 - 2x_2 + 3x_3 = 1. \end{cases}$ The first equation does not contain $x_1$, so we first interchange the first two equations and then eliminate:

$$
\begin{bmatrix} 0 & 2 & -1 & 1 \\ 1 & -1 & 1 & 0 \\ 2 & -2 & 3 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 1 & 0 \\ 0 & 2 & -1 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 1 & 0 \\ 0 & 1 & -\frac12 & \frac12 \\ 0 & 0 & 1 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix},
$$

and the unique solution is $\boldsymbol{x} = [0\ 1\ 1]^{\mathsf T}$.

**Definition 1.6.1 (Elementary Operations)** The three types of elementary operations on a linear system are: interchange (swap the positions of two equations), scaling (multiply both sides of an equation by a nonzero constant $k$) and replacement (add $k$ times one equation to another). Correspondingly, the three types of **elementary row operations** (column operations) on a matrix are: interchange two rows (columns); multiply a row (column) by a nonzero constant $k$; add $k$ times one row (column) to another. The $m \times (n+1)$ matrix $[A\ \boldsymbol{b}]$ (also written $[A \mid \boldsymbol{b}]$) obtained by placing the coefficient matrix and the right-hand side side by side is called the **augmented matrix** of the system.

Performing elementary operations on a linear system is equivalent to performing elementary row operations on its augmented matrix.

**Proposition 1.6.1** Every elementary operation is invertible, and its inverse is an elementary operation of the same type: an interchange is its own inverse; the inverse of scaling by $k$ is scaling by $\frac1k$; the inverse of a replacement with parameter $k$ is the replacement with parameter $-k$.

**Theorem 1.6.1 (Elementary Operations Preserve Solutions)** The system obtained from a linear system by one elementary operation has the same solutions as the original system.

**Proof** Suppose that one elementary operation turns $A\boldsymbol{x} = \boldsymbol{b}$ into $\tilde{A}\boldsymbol{x} = \tilde{\boldsymbol{b}}$. Every equation of the new system is a combination of the original equations, so every solution of the original system satisfies the new one. By Proposition 1.6.1, $\tilde{A}\boldsymbol{x} = \tilde{\boldsymbol{b}}$ can be turned back into $A\boldsymbol{x} = \boldsymbol{b}$ by one elementary operation, so by the same argument every solution of the new system solves the original one. $\square$

## 1.7. Echelon Forms and Elimination

Not every square matrix can be reduced to the identity matrix, and a system need not be square. We first look at two examples and then describe the target shape in general.

**Example 1.7.1** Solve $\begin{cases} 2x_3 + x_4 = 1, \\ x_1 - x_2 + 4x_3 = 0. \end{cases}$ We perform an interchange, a scaling and a replacement on the augmented matrix:

$$
\begin{bmatrix} 0 & 0 & 2 & 1 & 1 \\ 1 & -1 & 4 & 0 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 4 & 0 & 0 \\ 0 & 0 & 2 & 1 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 4 & 0 & 0 \\ 0 & 0 & 1 & \frac12 & \frac12 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 0 & -2 & -2 \\ 0 & 0 & 1 & \frac12 & \frac12 \end{bmatrix}.
$$

The system becomes $x_1 - x_2 - 2x_4 = -2$, $x_3 + \frac12x_4 = \frac12$, that is,

$$
x_1 = -2 + x_2 + 2x_4, \qquad x_3 = \tfrac12 - \tfrac12x_4, \qquad x_2, x_4 \in \mathbb{R}.
$$

The unknowns $x_2, x_4$ can take arbitrary values, and $x_1, x_3$ are determined by them and the right-hand side; after the operations, the columns of $x_1, x_3$ form an identity matrix. In vector form the solution set is

$$
\left\{ \begin{bmatrix} -2 \\ 0 \\ \frac12 \\ 0 \end{bmatrix} + a\begin{bmatrix} 1 \\ 1 \\ 0 \\ 0 \end{bmatrix} + b\begin{bmatrix} 2 \\ 0 \\ -\frac12 \\ 1 \end{bmatrix} \;\middle|\; a, b \in \mathbb{R} \right\}.
$$

**Example 1.7.2** Solve $\begin{cases} x_1 + x_2 - 3x_3 = -1, \\ 2x_1 + x_2 - 2x_3 = 1, \\ x_1 + x_2 + x_3 = 3, \\ x_1 + 2x_2 - 3x_3 = 0. \end{cases}$ Starting from the variable with the smallest index, we eliminate downward in the augmented matrix:

$$
\begin{bmatrix} 1 & 1 & -3 & -1 \\ 2 & 1 & -2 & 1 \\ 1 & 1 & 1 & 3 \\ 1 & 2 & -3 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & -3 & -1 \\ 0 & -1 & 4 & 3 \\ 0 & 0 & 4 & 4 \\ 0 & 1 & 0 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & -3 & -1 \\ 0 & -1 & 4 & 3 \\ 0 & 0 & 4 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix}.
$$

Back substitution gives $x_3 = 1$, $x_2 = 1$, $x_1 = 1$. Alternatively, we may scale each pivot to $1$ and eliminate upward, starting from the last pivot:

$$
\begin{bmatrix} 1 & 1 & -3 & -1 \\ 0 & 1 & -4 & -3 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 0 & 2 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix},
$$

and read off the solution $x_1 = x_2 = x_3 = 1$ directly. If the right-hand side of the fourth equation is changed to $3$, the same elimination produces the last row $[0\ 0\ 0\ 3]$, that is, the contradictory equation $0 = 3$, and the system has no solution.

**Definition 1.7.1 (Row Echelon Form)** A row whose entries are all zero is called a zero row, and any other row a nonzero row; the first nonzero entry from the left in a nonzero row is called the **pivot** of that row. A matrix is said to be in **row echelon form** if all zero rows lie below all nonzero rows and the column indices of the pivots increase strictly with the row index. The number of nonzero rows is called the number of pivots (or steps) of the echelon form; the columns containing pivots are called **pivot columns**, and the others free columns.

**Definition 1.7.2 (Reduced Row Echelon Form)** A matrix in row echelon form is in **reduced row echelon form** if all its pivots equal $1$ and every entry of a pivot column other than the pivot is $0$. The reduced row echelon form obtained from a matrix $A$ is denoted by $\operatorname{rref}(A)$.

Writing $\bullet$ for a pivot and $\star$ for a number that may be nonzero, the two shapes look like

$$
\begin{bmatrix} \bullet & \star & \star & \star & \star & \star \\ 0 & 0 & \bullet & \star & \star & \star \\ 0 & 0 & 0 & \bullet & \star & \star \\ 0 & 0 & 0 & 0 & 0 & \bullet \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix},
\qquad
\begin{bmatrix} 1 & \star & 0 & 0 & \star & 0 \\ 0 & 0 & 1 & 0 & \star & 0 \\ 0 & 0 & 0 & 1 & \star & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}.
$$

In a row echelon form, the entries where the pivot rows meet the pivot columns form an upper triangular matrix with nonzero diagonal entries; in the reduced row echelon form they form an identity matrix.

**Definition 1.7.3 (Pivot Variables and Free Variables)** After the augmented matrix of a system has been reduced to row echelon form, the unknowns corresponding to pivot columns are called pivot variables (basic variables), and those corresponding to free columns are called **free variables**. The expression of the pivot variables in terms of the free variables and the right-hand side is called the general solution of the system.

The free variables can take arbitrary values. The choice of pivot variables is in general not unique; usually we choose them starting from the variable with the smallest index.

**Theorem 1.7.1** Every matrix can be reduced to row echelon form using only interchanges and replacements; every matrix can be reduced to reduced row echelon form by elementary row operations.

**Proof** We prove the first statement by induction on the number of rows $m$. For $m = 1$, a $1 \times n$ matrix is automatically in row echelon form. Suppose every $(m-1) \times n$ matrix can be reduced to row echelon form, and consider an $m \times n$ matrix $A$:

1. If $a_{11} \ne 0$, add $-a_{i1}/a_{11}$ times row 1 to row $i$ ($2 \le i \le m$), which makes every entry of the first column except $a_{11}$ zero. Rows $2$ to $m$ and columns $2$ to $n$ form an $(m-1) \times (n-1)$ matrix, which by the induction hypothesis can be reduced to row echelon form (these row operations do not affect the zeros already created in the first column); hence $A$ has been reduced to row echelon form.
2. If $a_{11} = 0$ but the first column has a nonzero entry $a_{i1}$, interchange rows $1$ and $i$ and proceed as in case 1.
3. If the first column is entirely zero, take the first nonzero column from the left (column $j$) and apply the same argument to the matrix formed by columns $j$ to $n$; if the matrix is entirely zero, it is already in row echelon form.

For the second statement, first reduce to row echelon form, scale every pivot to $1$, and then, starting from the last pivot, use replacements to make the entries above each pivot zero. During upward elimination the entries to the left of a pivot in its row are all zero, so the zeros obtained earlier are not destroyed. $\square$

**Theorem 1.7.2 (Solvability Criterion)** Reduce the augmented matrix $[A\ \boldsymbol{b}]$ to row echelon form (which reduces $A$ to row echelon form at the same time). Let $r$ be the number of pivots of the echelon form of $A$, and $n$ the number of unknowns. Then

1. if the echelon form of $[A\ \boldsymbol{b}]$ has more than $r$ pivots (in which case it has exactly $r+1$), the system has no solution;
2. if the echelon form of $[A\ \boldsymbol{b}]$ has exactly $r$ pivots, the system is solvable, and:
   - it has a unique solution when $r = n$;
   - it has infinitely many solutions when $r < n$.

**Proof** By Theorem 1.6.1, the system corresponding to the echelon form has the same solutions as the original system. If the augmented matrix has $r+1$ pivots, its row $r+1$ is $[0\ \cdots\ 0\ c]$ with $c \ne 0$, which corresponds to the contradictory equation $0 = c$. Otherwise the zero rows correspond to the identities $0 = 0$ and can be discarded; there remain $r$ equations, in each of which the coefficient of the pivot variable (the pivot) is nonzero. When $r = n$ there are no free variables, the coefficient matrix is upper triangular with nonzero diagonal entries, and back substitution gives the unique solution. When $r < n$ the free variables can take arbitrary values, and each choice of values determines the pivot variables uniquely by back substitution, so there are infinitely many solutions. $\square$

For two equations in two unknowns, the three conclusions of the criterion are evident in the row picture: the two lines intersect, are parallel, or coincide.

![The three cases for two equations in two unknowns: the lines meet in a point (unique solution), are parallel (no solution; elimination produces a contradictory equation) or coincide (infinitely many solutions, with one free variable)](./plots/solution-cases.py)

By Theorems 1.7.1 and 1.7.2, a linear system can be solved by an entirely standard procedure:

**Algorithm 1.7.1 (Gaussian Elimination)** Input: a linear system $A\boldsymbol{x} = \boldsymbol{b}$.

1. Write down the augmented matrix $[A\ \boldsymbol{b}]$.
2. Process the columns from left to right: choose a nonzero entry of the current column as the pivot and, if necessary, move it to the current row by an interchange; use replacements to make all entries below the pivot zero; move on to the next row and the next column. The result is a row echelon form.
3. Decide by the solvability criterion whether a solution exists.
4. If it does, take the free variables as parameters and compute the pivot variables by back substitution.

**Algorithm 1.7.2 (Gauss–Jordan Elimination)** Reduce the augmented matrix to reduced row echelon form by elementary row operations (first eliminate downward as in Algorithm 1.7.1, then scale the pivots to $1$ and eliminate upward), and move the free variables to the right-hand side; this gives the general solution of the system.

Elimination is the basic method by which computers solve linear systems (numerical linear algebra). For a square matrix of order $n$, downward elimination takes about $\frac23n^3$ floating-point operations and back substitution only about $n^2$; Gauss–Jordan elimination, which also clears the entries above the pivots, takes about $n^3$. Numerical computation therefore usually uses Gaussian elimination followed by back substitution, and the next chapter organizes this process as the LU decomposition. Here is an exact-arithmetic implementation of Gauss–Jordan elimination:

```python
from fractions import Fraction

def rref(rows):
    """Gauss-Jordan elimination with exact arithmetic; returns (R, pivot_columns)."""
    R = [[Fraction(x) for x in row] for row in rows]
    m, n = len(R), len(R[0])
    pivots, r = [], 0                      # r = index of the next pivot row
    for j in range(n):
        p = next((i for i in range(r, m) if R[i][j] != 0), None)
        if p is None:                      # no pivot in column j: a free column
            continue
        R[r], R[p] = R[p], R[r]            # swap rows
        R[r] = [x / R[r][j] for x in R[r]] # scale the pivot to 1
        for i in range(m):                 # eliminate above and below the pivot
            if i != r and R[i][j] != 0:
                R[i] = [a - R[i][j] * b for a, b in zip(R[i], R[r])]
        pivots.append(j)
        r += 1
        if r == m:
            break
    return R, pivots

# Example 1.7.2: rows of R are [1,0,0,1], [0,1,0,1], [0,0,1,1], [0,0,0,0]
R, pivots = rref([[1, 1, -3, -1], [2, 1, -2, 1], [1, 1, 1, 3], [1, 2, -3, 0]])
print(pivots)  # [0, 1, 2]
```

## 1.8. Homogeneous Systems

**Definition 1.8.1 (Homogeneous Linear System)** A linear system $A\boldsymbol{x} = \boldsymbol{b}$ is called a **homogeneous linear system** if $\boldsymbol{b} = \boldsymbol{0}$, and nonhomogeneous if $\boldsymbol{b} \ne \boldsymbol{0}$. The vector $\boldsymbol{x} = \boldsymbol{0}$ is always a solution of a homogeneous system, called the zero or trivial solution; any other solution (if one exists) is called a nonzero or nontrivial solution.

If $\boldsymbol{x}$ is a nonzero solution of $A\boldsymbol{x} = \boldsymbol{0}$, then every $k\boldsymbol{x}$ ($k \in \mathbb{R}$) is also a solution, so a homogeneous system with a nonzero solution has infinitely many solutions. The augmented matrix $[A\ \boldsymbol{0}]$ always has the same number of pivots as $A$, so elimination only needs to be performed on the coefficient matrix. Applying the solvability criterion to homogeneous systems gives:

**Corollary 1.8.1** Let $r$ be the number of pivots of an echelon form of $A$ and $n$ the number of unknowns. The homogeneous linear system $A\boldsymbol{x} = \boldsymbol{0}$ has only the zero solution if and only if $r = n$, and has a nonzero solution if and only if $r < n$.

**Corollary 1.8.2** A homogeneous linear system with fewer equations than unknowns always has a nonzero solution.

**Proof** The number of pivots does not exceed the number of equations $m$, and $m < n$, so $r \le m < n$; the claim follows from Corollary 1.8.1. $\square$

**Example 1.8.1** Solve the homogeneous linear system

$$
\begin{cases} x_1 + x_2 - 3x_4 - x_5 = 0, \\ x_1 - x_2 + 2x_3 - x_4 = 0, \\ 4x_1 - 2x_2 + 6x_3 + 3x_4 - 4x_5 = 0, \\ 2x_1 + 4x_2 - 2x_3 + 4x_4 - 7x_5 = 0. \end{cases}
$$

Eliminate in the coefficient matrix:

$$
\begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 1 & -1 & 2 & -1 & 0 \\ 4 & -2 & 6 & 3 & -4 \\ 2 & 4 & -2 & 4 & -7 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 0 & -2 & 2 & 2 & 1 \\ 0 & -6 & 6 & 15 & 0 \\ 0 & 2 & -2 & 10 & -5 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 0 & -2 & 2 & 2 & 1 \\ 0 & 0 & 0 & 9 & -3 \\ 0 & 0 & 0 & 12 & -4 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 0 & -2 & 2 & 2 & 1 \\ 0 & 0 & 0 & 9 & -3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}.
$$

There are $3 < 5$ pivots, so there are infinitely many solutions; the pivot variables are $x_1, x_2, x_4$ and the free variables are $x_3, x_5$. Continuing to the reduced row echelon form

$$
\begin{bmatrix} 1 & 0 & 1 & 0 & -\frac76 \\ 0 & 1 & -1 & 0 & -\frac56 \\ 0 & 0 & 0 & 1 & -\frac13 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix},
$$

and moving terms across, we obtain the general solution $x_1 = -x_3 + \frac76x_5$, $x_2 = x_3 + \frac56x_5$, $x_4 = \frac13x_5$, where $x_3, x_5 \in \mathbb{R}$.

## 1.9. Linear Operations on Matrices and the Transpose

Linear maps can be added, multiplied by scalars and composed; the operations on matrices are defined by the principle that "the standard matrix follows the map".

**Definition 1.9.1 (Linear Operations on Maps)** Let $T_A, T_B\colon \mathbb{R}^n \to \mathbb{R}^m$ be linear maps and $k \in \mathbb{R}$. The maps

$$
T_A + T_B\colon \boldsymbol{x} \mapsto T_A(\boldsymbol{x}) + T_B(\boldsymbol{x}), \qquad kT_A\colon \boldsymbol{x} \mapsto kT_A(\boldsymbol{x})
$$

are called the sum of $T_A$ and $T_B$ and the scalar multiple of $T_A$ by $k$, respectively.

It is easy to check that $T_A + T_B$ and $kT_A$ are again linear maps, and that $(kT_A + \ell T_B)(\boldsymbol{x}) = kT_A(\boldsymbol{x}) + \ell T_B(\boldsymbol{x})$ for all $k, \ell$. The set of all linear maps $\mathbb{R}^n \to \mathbb{R}^m$ is closed under these two operations and satisfies the same eight rules as Property 1.1.1 (the zero element being the zero map); it is itself a linear space ([Chapter 8](/2.1.8)).

**Definition 1.9.2 (Linear Operations on Matrices)** Let $A = [a_{ij}]_{m \times n}$, $B = [b_{ij}]_{m \times n}$ and $k \in \mathbb{R}$. Define

$$
A + B = [a_{ij} + b_{ij}]_{m \times n}, \qquad kA = [ka_{ij}]_{m \times n}.
$$

The matrix all of whose entries are $0$ is called the zero matrix, denoted by $O_{m \times n}$ or $O$; $-A = (-1)A$ is called the negative of $A$, and $A - B = A + (-B)$.

The standard matrices of $T_A + T_B$ and $kT_A$ are $A + B$ and $kA$ respectively (compare the images of $\boldsymbol{e}_j$ column by column), that is, $T_A + T_B = T_{A+B}$ and $kT_A = T_{kA}$. Matrix addition and scalar multiplication also satisfy the eight rules, so $\mathbb{R}^{m \times n}$ is a linear space as well. The identity of maps $(kT_A + \ell T_B)(\boldsymbol{x}) = kT_A(\boldsymbol{x}) + \ell T_B(\boldsymbol{x})$ immediately gives:

**Proposition 1.9.1** The product of a matrix and a vector is distributive over the linear operations on matrices: $(kA + \ell B)\boldsymbol{x} = k(A\boldsymbol{x}) + \ell(B\boldsymbol{x})$.

**Definition 1.9.3 (Transpose of a Matrix)** The $n \times m$ matrix obtained by interchanging the rows and columns of an $m \times n$ matrix $A$ is called the **transpose** of $A$, denoted by $A^{\mathsf T}$; that is, the $(j, i)$ entry of $A^{\mathsf T}$ is $a_{ij}$:

$$
A^{\mathsf T} = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]^{\mathsf T} = \begin{bmatrix} \boldsymbol{a}_1^{\mathsf T} \\ \vdots \\ \boldsymbol{a}_n^{\mathsf T} \end{bmatrix}.
$$

The transpose generalizes the transpose of a vector and satisfies $(A^{\mathsf T})^{\mathsf T} = A$, $(A + B)^{\mathsf T} = A^{\mathsf T} + B^{\mathsf T}$ and $(kA)^{\mathsf T} = kA^{\mathsf T}$.

**Definition 1.9.4 (Symmetric and Skew-Symmetric Matrices)** A matrix satisfying $A = A^{\mathsf T}$ is called a **symmetric matrix**; a matrix satisfying $A = -A^{\mathsf T}$ is called a **skew-symmetric matrix** (antisymmetric matrix).

Symmetric and skew-symmetric matrices are necessarily square; the diagonal entries of a skew-symmetric matrix satisfy $a_{ii} = -a_{ii}$ and are therefore all $0$.

**Proposition 1.9.2** Every square matrix $A$ can be written uniquely as the sum of a symmetric matrix $B$ and a skew-symmetric matrix $C$:

$$
A = B + C, \qquad B = \tfrac12(A + A^{\mathsf T}), \quad C = \tfrac12(A - A^{\mathsf T}).
$$

**Proof** One checks directly that $B^{\mathsf T} = B$, $C^{\mathsf T} = -C$ and $B + C = A$. Uniqueness: if $A = B + C$ with $B$ symmetric and $C$ skew-symmetric, then $A^{\mathsf T} = B - C$; adding and subtracting the two equations gives the formulas for $B$ and $C$. $\square$

## 1.10. Matrix Multiplication

**Definition 1.10.1 (Composition of Maps)** Let $f\colon X \to Y$ and $g\colon Y \to Z$ be maps. The map $h\colon X \to Z$, $x \mapsto g(f(x))$ is called the composition of $g$ and $f$, written $h = g \circ f$.

For $g \circ f$ to be defined, the domain of $g$ must be the codomain of $f$. Composition is associative: for $f\colon X \to Y$, $g\colon Y \to Z$ and $h\colon Z \to W$ we have $h \circ (g \circ f) = (h \circ g) \circ f$, because both sides send $x$ to $h(g(f(x)))$.

**Proposition 1.10.1** Let $T_B\colon \mathbb{R}^n \to \mathbb{R}^m$ and $T_A\colon \mathbb{R}^m \to \mathbb{R}^\ell$ be linear maps. Then $T_A \circ T_B\colon \mathbb{R}^n \to \mathbb{R}^\ell$ is also a linear map. Moreover, for linear maps $T_B, T_{B'}\colon \mathbb{R}^n \to \mathbb{R}^m$, $T_A, T_{A'}\colon \mathbb{R}^m \to \mathbb{R}^\ell$ and $k \in \mathbb{R}$,

$$
(T_A + T_{A'}) \circ T_B = T_A \circ T_B + T_{A'} \circ T_B, \quad T_A \circ (T_B + T_{B'}) = T_A \circ T_B + T_A \circ T_{B'}, \quad k(T_A \circ T_B) = (kT_A) \circ T_B = T_A \circ (kT_B).
$$

**Proof** Linearity: $(T_A \circ T_B)(k\boldsymbol{x} + \ell\boldsymbol{x}') = T_A(kT_B(\boldsymbol{x}) + \ell T_B(\boldsymbol{x}')) = k(T_A \circ T_B)(\boldsymbol{x}) + \ell(T_A \circ T_B)(\boldsymbol{x}')$. The first distributive law: $((T_A + T_{A'}) \circ T_B)(\boldsymbol{x}) = T_A(T_B(\boldsymbol{x})) + T_{A'}(T_B(\boldsymbol{x}))$; the second distributive law uses the additivity of $T_A$, and the identity for scalar multiples uses the homogeneity of $T_A$. $\square$

What is the standard matrix of the composition $T_A \circ T_B$? Let $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_m]$ be an $\ell \times m$ matrix and $B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_n]$ an $m \times n$ matrix. Then its $j$-th column is $T_A(T_B(\boldsymbol{e}_j)) = A\boldsymbol{b}_j$.

**Definition 1.10.2 (Matrix Multiplication)** The product of an $\ell \times m$ matrix $A$ and an $m \times n$ matrix $B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_n]$ is the $\ell \times n$ matrix

$$
AB = A[\boldsymbol{b}_1\ \boldsymbol{b}_2\ \cdots\ \boldsymbol{b}_n] = [A\boldsymbol{b}_1\ A\boldsymbol{b}_2\ \cdots\ A\boldsymbol{b}_n].
$$

Thus $AB$ is the standard matrix of $T_A \circ T_B$, that is, $T_A \circ T_B = T_{AB}$, and

$$
(AB)\boldsymbol{x} = A(B\boldsymbol{x}).
$$

Computing $AB$ requires the number of columns of $A$ to equal the number of rows of $B$ (corresponding to the requirement that the domain of $T_A$ be the codomain of $T_B$); $AB$ has as many rows as $A$ and as many columns as $B$. If the rows of $A$ are $\tilde{\boldsymbol{a}}_1^{\mathsf T}, \dots, \tilde{\boldsymbol{a}}_\ell^{\mathsf T}$, then

$$
AB = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{b}_1 & \cdots & \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{b}_n \\ \vdots & & \vdots \\ \tilde{\boldsymbol{a}}_\ell^{\mathsf T}\boldsymbol{b}_1 & \cdots & \tilde{\boldsymbol{a}}_\ell^{\mathsf T}\boldsymbol{b}_n \end{bmatrix} = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T}B \\ \vdots \\ \tilde{\boldsymbol{a}}_\ell^{\mathsf T}B \end{bmatrix}, \qquad c_{ik} = \tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{b}_k = \sum_{j=1}^m a_{ij}b_{jk}.
$$

The $k$-th column $A\boldsymbol{b}_k$ of $AB$ is determined by $A$ and the $k$-th column of $B$ alone; the $i$-th row $\tilde{\boldsymbol{a}}_i^{\mathsf T}B$ is determined by the $i$-th row of $A$ and $B$ alone. By the entrywise formula, computing $AB$ takes $\ell mn$ multiplications, and the product of two square matrices of order $n$ costs about $2n^3$ floating-point operations.

**Example 1.10.1** For $\boldsymbol{x} \in \mathbb{R}^2$, first rotate counterclockwise through $90^\circ$, $B = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$, and then interchange the two components, $A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$. The standard matrix of the composition is

$$
AB = [A\boldsymbol{b}_1\ A\boldsymbol{b}_2] = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix},
$$

the reflection in the $x_1$-axis.

**Proposition 1.10.2 (Rules for Matrix Multiplication)** Whenever the products are defined:

1. associativity: $A(BC) = (AB)C$, so we may write $ABC$ without parentheses;
2. distributivity: $(A + B)C = AC + BC$ and $A(B + C) = AB + AC$;
3. compatibility with scalar multiplication: $k(AB) = (kA)B = A(kB)$;
4. transposes: $\boldsymbol{a}^{\mathsf T}\boldsymbol{x} = \boldsymbol{x}^{\mathsf T}\boldsymbol{a}$, $(A\boldsymbol{x})^{\mathsf T} = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}$ and $(AB)^{\mathsf T} = B^{\mathsf T}A^{\mathsf T}$.

**Proof** Associativity can be proved in three ways. First, $(AB)C$ and $A(BC)$ are the standard matrices of $(T_A \circ T_B) \circ T_C$ and $T_A \circ (T_B \circ T_C)$, and composition of maps is associative. Second, let $C = [\boldsymbol{c}_1\ \cdots\ \boldsymbol{c}_p]$; by $(AB)\boldsymbol{x} = A(B\boldsymbol{x})$,

$$
A(BC) = [A(B\boldsymbol{c}_1)\ \cdots\ A(B\boldsymbol{c}_p)] = [(AB)\boldsymbol{c}_1\ \cdots\ (AB)\boldsymbol{c}_p] = (AB)C.
$$

Third, compare the $(i, s)$ entries: both sides equal $\sum_{j=1}^m\sum_{k=1}^n a_{ij}b_{jk}c_{ks}$. Rules 2 and 3 follow by translating Proposition 1.10.1 into standard matrices. Rule 4: $\boldsymbol{a}^{\mathsf T}\boldsymbol{x} = \sum_j a_jx_j = \boldsymbol{x}^{\mathsf T}\boldsymbol{a}$; the $i$-th component of $(A\boldsymbol{x})^{\mathsf T}$ is $\tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{x} = \boldsymbol{x}^{\mathsf T}\tilde{\boldsymbol{a}}_i$, and $A^{\mathsf T} = [\tilde{\boldsymbol{a}}_1\ \cdots\ \tilde{\boldsymbol{a}}_\ell]$, so $(A\boldsymbol{x})^{\mathsf T} = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}$; finally, the $k$-th row of $(AB)^{\mathsf T}$ is $(A\boldsymbol{b}_k)^{\mathsf T} = \boldsymbol{b}_k^{\mathsf T}A^{\mathsf T}$, which is exactly the $k$-th row of $B^{\mathsf T}A^{\mathsf T}$. $\square$

For a positive integer $k$, the $k$-th power of a square matrix $A$ is defined by $A^k = \underbrace{AA\cdots A}_{k\ \text{factors}}$, with the convention $A^0 = I$. For a polynomial $f(x) = a_0 + a_1x + \cdots + a_px^p$, the matrix polynomial is defined by $f(A) = a_0I + a_1A + \cdots + a_pA^p$.

**Example 1.10.2** For $\boldsymbol{u}, \boldsymbol{v} \in \mathbb{R}^n$, $A = \boldsymbol{u}\boldsymbol{v}^{\mathsf T}$ is a square matrix of order $n$. By associativity, $\boldsymbol{v}^{\mathsf T}\boldsymbol{u}$ is a number and can be pulled out:

$$
A^k = \boldsymbol{u}(\boldsymbol{v}^{\mathsf T}\boldsymbol{u})(\boldsymbol{v}^{\mathsf T}\boldsymbol{u})\cdots(\boldsymbol{v}^{\mathsf T}\boldsymbol{u})\boldsymbol{v}^{\mathsf T} = (\boldsymbol{v}^{\mathsf T}\boldsymbol{u})^{k-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}.
$$

Matrix multiplication differs from multiplication of numbers in three main respects:

- It is not commutative in general. $AB$ and $BA$ need not both be defined; when both are defined, they have the same size only if $A$ and $B$ are square matrices of the same order; and even then they may differ:

  $$
  \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \qquad \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}.
  $$

  In $AB$ we say that $B$ is multiplied on the left by $A$, or that $A$ is multiplied on the right by $B$; if $AB = BA$, we say that $A$ and $B$ commute.
- The cancellation law fails in general: $AB = AC$ and $A \ne O$ do not imply $B = C$. For example, $AB = AC = O$ for $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$, $B = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$, $C = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$. Cancellation requires $A$ to be invertible (next chapter).
- There are zero divisors: the product of two nonzero matrices can be the zero matrix, so $AB = O$ does not imply $A = O$ or $B = O$.

**Example 1.10.3** $I_mA = A = AI_n$; $kI_n$ is called a scalar matrix, and $(kI_n)A = kA$. The composition of two rotations of the plane is again a rotation, $R_{\theta_1}R_{\theta_2} = R_{\theta_1 + \theta_2} = R_{\theta_2}R_{\theta_1}$, and comparing the entries of both sides gives the angle-addition formulas of trigonometry. A reflection composed with itself is the identity: $H_\theta^2 = I_2$, which can be verified directly using $\cos^2 2\theta + \sin^2 2\theta = 1$.

Finally, we define a frequently used numerical characteristic.

**Definition 1.10.3 (Trace)** The sum of the diagonal entries of a square matrix $A = [a_{ij}]_{n \times n}$ is called the **trace** of $A$, written $\operatorname{tr}(A) = a_{11} + a_{22} + \cdots + a_{nn}$.

**Property 1.10.1** The trace is linear: $\operatorname{tr}(kA + \ell B) = k\operatorname{tr}(A) + \ell\operatorname{tr}(B)$; also $\operatorname{tr}(A^{\mathsf T}) = \operatorname{tr}(A)$. If $A$ and $B$ are $m \times n$ and $n \times m$ matrices respectively, then $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.

**Proof** The first two statements follow directly from the definition. $AB$ is a square matrix of order $m$ and $BA$ one of order $n$, and

$$
\operatorname{tr}(AB) = \sum_{i=1}^m\sum_{j=1}^n a_{ij}b_{ji} = \sum_{j=1}^n\sum_{i=1}^m b_{ji}a_{ij} = \operatorname{tr}(BA). \qquad \square
$$

## Summary

This chapter established the correspondence "linear map $\leftrightarrow$ matrix" and turned the solution of linear systems into a standard procedure.

| Category | Content |
|---|---|
| Definitions | $m$-dimensional vectors and linear operations (Definitions 1.1.1, 1.1.2); linear combinations, standard coordinate vectors (Definition 1.1.3); linear maps and linear transformations (Definition 1.2.1); matrices, standard matrices, matrix–vector products (Definitions 1.3.1–1.3.3); identity, diagonal and triangular matrices (Definition 1.4.1); linear systems (Definition 1.5.1); elementary operations and augmented matrices (Definition 1.6.1); row echelon form, reduced row echelon form, pivot and free variables (Definitions 1.7.1–1.7.3); homogeneous linear systems (Definition 1.8.1); linear operations on matrices, transpose, symmetric and skew-symmetric matrices (Definitions 1.9.2–1.9.4); matrix multiplication (Definition 1.10.2); trace (Definition 1.10.3) |
| Theorems | A linear map is uniquely determined by the images of the standard coordinate vectors (Theorem 1.2.1); elementary operations preserve solutions (Theorem 1.6.1); every matrix can be reduced to (reduced) row echelon form (Theorem 1.7.1); solvability criterion (Theorem 1.7.2); a homogeneous system with fewer equations than unknowns has a nonzero solution (Corollary 1.8.2); symmetric–skew-symmetric decomposition (Proposition 1.9.2); rules for matrix multiplication (Proposition 1.10.2); $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ (Property 1.10.1) |
| Algorithms | Back and forward substitution (Algorithms 1.5.1, 1.5.2, about $n^2$ operations); Gaussian elimination (Algorithm 1.7.1, about $\frac23n^3$); Gauss–Jordan elimination (Algorithm 1.7.2, about $n^3$) |

| View | $A\boldsymbol{x}$ | $AB$ |
|---|---|---|
| Column | linear combination of the columns $\sum_j x_j\boldsymbol{a}_j$ | $[A\boldsymbol{b}_1\ \cdots\ A\boldsymbol{b}_n]$ |
| Row | $i$-th component $\tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{x}$ | $i$-th row $\tilde{\boldsymbol{a}}_i^{\mathsf T}B$ |
| Entry | $\sum_j a_{ij}x_j$ | $c_{ik} = \sum_j a_{ij}b_{jk}$ |
| Map | $T_A(\boldsymbol{x})$ | $T_A \circ T_B = T_{AB}$ |
