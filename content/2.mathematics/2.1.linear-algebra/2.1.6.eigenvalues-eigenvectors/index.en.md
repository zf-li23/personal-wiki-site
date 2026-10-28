---
title: Eigenvalues and Eigenvectors
source_hash: 2cb9bf76e49b
---

The previous chapters studied a single linear map $\boldsymbol{x} \mapsto A\boldsymbol{x}$: its range, its zeros (solution sets) and best approximation. This chapter studies the iteration of a linear transformation: how does $A^t\boldsymbol{x}$ behave for large $t$, and are there directions that stay fixed? The key is the equation $A\boldsymbol{x} = \lambda\boldsymbol{x}$: if we can find $n$ linearly independent vectors along each of which $A$ acts merely as a stretch, then in this basis $A$ is a diagonal matrix, and $A^t$ becomes transparent.

The chapter proceeds as follows. Two examples motivate the eigenvalue problem and, with it, the passage to complex numbers; we use the **determinant** to define the characteristic polynomial and compute eigenvalues and eigenvectors; we discuss properties of eigenvalues (the circle theorem, trace and determinant); we study when a matrix is diagonalizable (algebraic and geometric multiplicity); finally we introduce similarity, prove that every square matrix is similar to an upper triangular matrix, derive the Cayley–Hamilton theorem from this, and state the Jordan canonical form. This chapter relies on the **rank** and **dimension** of Chapter 3 and the determinant of Chapter 5; Chapter 7 applies its results to real symmetric matrices (spectral decomposition and orthogonal diagonalization), [Chapter 10](/2.1.10) proves the Jordan canonical form, and [Chapter 11](/2.1.11) uses it to define matrix functions. Eigenvalues are also the central tool behind graph spectra, Markov chains and population models.

## 6.1. Motivation

**Example 6.1.1 (Migration)** Consider the linear transformation of $\mathbb{R}^2$

$$
A\colon \boldsymbol{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \mapsto A\boldsymbol{x} = \begin{bmatrix} 0.6 & 0.1 \\ 0.4 & 0.9 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix},
$$

which describes the movement of population between two regions over one year: each year $40\%$ of the people in region 1 move to region 2, and $10\%$ of the people in region 2 move to region 1. What does the population distribution look like after a long time? Is there a stable distribution? The two questions can be stated as:

1. the limit of $A^t$ ($t \in \mathbb{N}$) as $t \to \infty$;
2. whether there is $\boldsymbol{x} \ne \boldsymbol{0}$ with $A\boldsymbol{x} = \boldsymbol{x}$.

Consider question 2 first: $A\boldsymbol{x} = \boldsymbol{x}$ means $(I_2 - A)\boldsymbol{x} = \boldsymbol{0}$, and $I_2 - A = \begin{bmatrix} 0.4 & -0.1 \\ -0.4 & 0.1 \end{bmatrix}$ does not have full rank, with $\mathcal{N}(I_2 - A) = \operatorname{span}(\boldsymbol{x}_1)$, $\boldsymbol{x}_1 = \begin{bmatrix} 0.2 \\ 0.8 \end{bmatrix}$; so a stable distribution exists.

Now question 1. If we can also find $\boldsymbol{x}_2$, linearly independent of $\boldsymbol{x}_1$, with $A\boldsymbol{x}_2 = k\boldsymbol{x}_2$, then every $\boldsymbol{x} = \ell_1\boldsymbol{x}_1 + \ell_2\boldsymbol{x}_2$ satisfies $A^t\boldsymbol{x} = \ell_1\boldsymbol{x}_1 + \ell_2k^t\boldsymbol{x}_2$. The equation $(kI_2 - A)\boldsymbol{x}_2 = \boldsymbol{0}$ has a nonzero solution if and only if

$$
\det(kI_2 - A) = \begin{vmatrix} k - 0.6 & -0.1 \\ -0.4 & k - 0.9 \end{vmatrix} = k^2 - 1.5k + 0.5 = 0,
$$

which has the two roots $1$ and $0.5$. Taking $k = 0.5$ gives $\boldsymbol{x}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$. Hence $A^t\boldsymbol{x} = \ell_1\boldsymbol{x}_1 + 0.5^t\ell_2\boldsymbol{x}_2 \to \ell_1\boldsymbol{x}_1$. In matrix form: with $X = [\boldsymbol{x}_1\ \boldsymbol{x}_2]$ and $\Lambda = \operatorname{diag}(1, 0.5)$ we have $AX = X\Lambda$, $A = X\Lambda X^{-1}$ and

$$
A^t = X\Lambda^tX^{-1} = \begin{bmatrix} 0.2 & 1 \\ 0.8 & -1 \end{bmatrix}\begin{bmatrix} 1 & \\ & 0.5^t \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 0.8 & -0.2 \end{bmatrix} = \begin{bmatrix} 0.2 + 0.8 \cdot 0.5^t & 0.2 - 0.2 \cdot 0.5^t \\ 0.8 - 0.8 \cdot 0.5^t & 0.8 + 0.2 \cdot 0.5^t \end{bmatrix} \to \begin{bmatrix} 0.2 & 0.2 \\ 0.8 & 0.8 \end{bmatrix}.
$$

For every initial distribution $\boldsymbol{x}$, $A^t\boldsymbol{x} \to (x_1 + x_2)\boldsymbol{x}_1$: the total population is preserved, and in the long run it splits $1 : 4$ between the two regions.

The key here is the system $A\boldsymbol{x} = \lambda\boldsymbol{x}$, in which $\lambda$ is not a given parameter but a number, to be determined from $A$, for which the system has a nonzero solution. The equation says that the image $A\boldsymbol{x}$ of $\boldsymbol{x}$ is collinear with $\boldsymbol{x}$.

**Example 6.1.2 (Isometries of the Plane)** By Example 4.3.1, the isometries of $\mathbb{R}^2$ come in two kinds, reflections and rotations:

$$
H_\theta = \begin{bmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{bmatrix}, \qquad R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix},
$$

where $H_\theta$ is the reflection across the line making the angle $\theta$ with the $x_1$-axis. For the reflection, $\det(\lambda I_2 - H_\theta) = \lambda^2 - 1$, so $\lambda = \pm 1$, and the corresponding solutions are $\begin{bmatrix} \cos\theta \\ \sin\theta \end{bmatrix}$ (the direction of the mirror line, fixed) and $\begin{bmatrix} -\sin\theta \\ \cos\theta \end{bmatrix}$ (the normal direction, reversed), in agreement with geometric intuition. For the rotation,

$$
\det(\lambda I_2 - R_\theta) = \begin{vmatrix} \lambda - \cos\theta & \sin\theta \\ -\sin\theta & \lambda - \cos\theta \end{vmatrix} = \lambda^2 - 2\lambda\cos\theta + 1,
$$

so $\lambda = \cos\theta \pm \mathrm{i}\sin\theta$. When $\theta = k\pi$ ($k \in \mathbb{Z}$) we get the double root $\lambda = (-1)^k$ and $\lambda I_2 - R_\theta = O$, so every vector satisfies $R_\theta\boldsymbol{x} = (-1)^k\boldsymbol{x}$; when $\theta \ne k\pi$ neither root is real, and no real vector satisfies $R_\theta\boldsymbol{x} \parallel \boldsymbol{x}$: a rotation indeed has no invariant direction. For the equation to always have solutions, we must regard $R_\theta$ as a linear transformation of $\mathbb{C}^2$.

### 6.1.1. Complex Matrices and Complex Vectors

For a square matrix $A$ of order $n$, $A\boldsymbol{x} = \lambda\boldsymbol{x}$ has a nonzero solution if and only if

$$
0 = \det(\lambda I_n - A) = \begin{vmatrix} \lambda - a_{11} & -a_{12} & \cdots & -a_{1n} \\ -a_{21} & \lambda - a_{22} & \cdots & -a_{2n} \\ \vdots & \vdots & & \vdots \\ -a_{n1} & -a_{n2} & \cdots & \lambda - a_{nn} \end{vmatrix}.
$$

By the complete expansion of the determinant (Theorem 5.7.1), the right-hand side is a polynomial of degree $n$ in $\lambda$ with leading coefficient $1$. Finding the roots of a polynomial inevitably involves complex numbers, so unless stated otherwise, this chapter considers vectors and matrices over the complex numbers $\mathbb{C}$. Matrix operations, linear systems, subspaces, bases and dimension, determinants and the other notions and results for real matrices carry over verbatim to complex matrices. Inner products and orthogonality are the exception: the inner product of complex vectors $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{C}^n$ must be defined as $\boldsymbol{a}^{\mathsf H}\boldsymbol{b} = \overline{\boldsymbol{a}}^{\mathsf T}\boldsymbol{b}$; see [Chapter 12](/2.1.12).

For $a, b \in \mathbb{R}$, the conjugate of the complex number $a + b\mathrm{i}$ is $\overline{a + b\mathrm{i}} = a - b\mathrm{i}$. Conjugation preserves addition and multiplication: $\overline{z + w} = \bar{z} + \bar{w}$ and $\overline{zw} = \bar{z}\,\bar{w}$. The conjugate $\bar{A}$ of a complex matrix is taken entrywise, and again $\overline{AB} = \bar{A}\,\bar{B}$. Complex numbers and complex vector spaces are treated systematically in [Chapter 9](/2.1.9).

## 6.2. Roots of Polynomials

This section only states the facts about polynomials needed later; the systematic theory of polynomials is in [Chapter 9](/2.1.9).

**Theorem 6.2.1** A polynomial of degree $n \ge 1$ in one variable with complex coefficients has at least one root in $\mathbb{C}$.

This is the **fundamental theorem of algebra**; its proof requires tools from analysis or topology and is not given here.

**Corollary 6.2.1** A polynomial $p(x)$ of degree $n$ in one variable with complex coefficients has exactly $n$ roots in $\mathbb{C}$, counted with multiplicity. If $x_1, \dots, x_s$ are all the distinct roots of $p(x)$, then

$$
p(x) = a_0(x - x_1)^{n_1}(x - x_2)^{n_2}\cdots(x - x_s)^{n_s}, \qquad n_1 + \cdots + n_s = n;
$$

$n_i$ is called the multiplicity of the root $x_i$, and $x_i$ is called a root of multiplicity $n_i$ of $p(x)$.

**Proof** Let $p(x) = a_0x^n + a_1x^{n-1} + \cdots + a_n$. By Theorem 6.2.1 there is a root $x_1$. From

$$
p(x) = p(x) - p(x_1) = a_0(x^n - x_1^n) + a_1(x^{n-1} - x_1^{n-1}) + \cdots + a_{n-1}(x - x_1)
$$

and $x^k - x_1^k = (x - x_1)(x^{k-1} + x^{k-2}x_1 + \cdots + x_1^{k-1})$ we get $p(x) = (x - x_1)q(x)$ with $q$ a polynomial of degree $n-1$. Repeating this step for $q$ gives the result. $\square$

**Theorem 6.2.2** Let the $n$ roots (counted with multiplicity) of the complex polynomial $p(x) = a_0x^n + a_1x^{n-1} + \cdots + a_n$ ($a_0 \ne 0$) be $x_1, \dots, x_n$. Then for $k = 1, \dots, n$,

$$
(-1)^k\frac{a_k}{a_0} = \sum_{1 \le i_1 < \cdots < i_k \le n} x_{i_1}x_{i_2}\cdots x_{i_k}.
$$

In particular, $-\dfrac{a_1}{a_0} = x_1 + \cdots + x_n$ and $(-1)^n\dfrac{a_n}{a_0} = x_1x_2\cdots x_n$.

These relations between roots and coefficients are known as **Vieta's formulas**.

**Proof** Expanding $p(x) = a_0(x - x_1)\cdots(x - x_n)$, the coefficient of $x^{n-k}$ is $a_0(-1)^k\sum_{i_1 < \cdots < i_k}x_{i_1}\cdots x_{i_k}$; comparing with $a_k$ gives the result. $\square$

**Proposition 6.2.1** If $a + b\mathrm{i}$ is a root of a polynomial $p(x)$ with real coefficients, then $\overline{a + b\mathrm{i}} = a - b\mathrm{i}$ is also a root, with the same multiplicity.

**Proof** Let $p(x) = \sum_k a_kx^{n-k}$ with $a_k \in \mathbb{R}$. Conjugation preserves addition and multiplication, so $p(\bar{z}) = \sum_k a_k\bar{z}^{\,n-k} = \overline{\sum_k a_kz^{n-k}} = \overline{p(z)}$, and $p(z) = 0$ implies $p(\bar{z}) = 0$. Taking conjugates of both sides of the factorization $p(x) = a_0\prod(x - x_i)^{n_i}$ and using the uniqueness of the factorization shows that $z$ and $\bar{z}$ have the same multiplicity. $\square$

## 6.3. Eigenvalues and Eigenvectors

### 6.3.1. Definitions

**Definition 6.3.1 (Eigenvalues and Eigenvectors)** Let $A$ be a square matrix of order $n$. If for a complex number $\lambda \in \mathbb{C}$ there is a nonzero vector $\boldsymbol{x} \in \mathbb{C}^n$ with $A\boldsymbol{x} = \lambda\boldsymbol{x}$, then $\lambda$ is called an **eigenvalue** of $A$ (over $\mathbb{C}$), $\boldsymbol{x}$ an **eigenvector** of $A$ belonging to the eigenvalue $\lambda$, and the pair $(\lambda, \boldsymbol{x})$ an **eigenpair** of $A$. If $\lambda \in \mathbb{R}$ and $\boldsymbol{x} \in \mathbb{R}^n$, they are called an eigenvalue, eigenvector and eigenpair of $A$ over $\mathbb{R}$.

Only square matrices have eigenvalues and eigenvectors. The zero vector is not an eigenvector; if $\boldsymbol{x}$ is an eigenvector, then so is $k\boldsymbol{x}$ for every $k \ne 0$, belonging to the same eigenvalue, so what matters are linearly independent eigenvectors. $(\lambda_0, \boldsymbol{x}_0)$ is an eigenpair if and only if $\boldsymbol{x}_0$ is a nonzero vector in $\mathcal{N}(\lambda_0I_n - A)$.

**Proposition 6.3.1** A number $\lambda_0$ is an eigenvalue of $A$ if and only if $\det(\lambda_0I_n - A) = 0$. In particular, $0$ is an eigenvalue of $A$ if and only if $A$ is not invertible; if $\lambda_0$ is not an eigenvalue of $A$, then $\lambda_0I_n - A$ is invertible.

**Proof** $(\lambda_0I_n - A)\boldsymbol{x} = \boldsymbol{0}$ has a nonzero solution if and only if $\lambda_0I_n - A$ is not invertible, if and only if its determinant is zero (Theorem 5.2.1). $\square$

**Definition 6.3.2 (Characteristic Polynomial)** The **characteristic polynomial** of a square matrix $A$ of order $n$ is $p_A(\lambda) = \det(\lambda I_n - A)$, a polynomial of degree $n$ in $\lambda$ with leading coefficient $1$.

Thus $\lambda_0$ is an eigenvalue of $A$ if and only if it is a root of $p_A$. By Corollary 6.2.1, a square matrix of order $n$ has exactly $n$ eigenvalues over $\mathbb{C}$ (counted with multiplicity), but over $\mathbb{R}$ it may have none at all (the rotation in Example 6.1.2).

**Definition 6.3.3 (Eigenspace)** Let $\lambda_0$ be an eigenvalue of $A$. The null space $\mathcal{N}(\lambda_0I_n - A)$ is called the **eigenspace** of $A$ belonging to $\lambda_0$.

The set of eigenvectors belonging to $\lambda_0$ is $\mathcal{N}(\lambda_0I_n - A) \setminus \{\boldsymbol{0}\}$, which is nonempty; a basis of $\mathcal{N}(\lambda_0I_n - A)$ is a maximal set of linearly independent eigenvectors belonging to $\lambda_0$.

### 6.3.2. Computation

**Algorithm 6.3.1 (Computing Eigenvalues and Eigenvectors)** Input: a square matrix $A$ of order $n$.

1. Compute the characteristic polynomial $p_A(\lambda) = \det(\lambda I_n - A)$;
2. find all roots of $p_A(\lambda)$; these are all the eigenvalues of $A$;
3. for each distinct eigenvalue $\lambda_i$, use Gaussian elimination to find a basis $\boldsymbol{x}_{i,1}, \dots, \boldsymbol{x}_{i,r_i}$ of the solution space $\mathcal{N}(\lambda_iI_n - A)$ of the homogeneous system $(\lambda_iI_n - A)\boldsymbol{x} = \boldsymbol{0}$; these are linearly independent eigenvectors belonging to $\lambda_i$.

This is the standard procedure for hand computation. Numerical computation does not find the roots of the characteristic polynomial (the roots are very sensitive to perturbations of the coefficients); instead it computes eigenvalues directly by algorithms such as the QR iteration, which belongs to numerical linear algebra. Conversely, finding the roots of a polynomial can be reduced to finding the eigenvalues of its companion matrix (Section 6.4.4).

**Example 6.3.1** Find the eigenvalues and eigenvectors of $A = \begin{bmatrix} 7 & -5 & 5 \\ -2 & 3 & -2 \\ -10 & 10 & -8 \end{bmatrix}$.

The characteristic polynomial is

$$
p_A(\lambda) = \begin{vmatrix} \lambda - 7 & 5 & -5 \\ 2 & \lambda - 3 & 2 \\ 10 & -10 & \lambda + 8 \end{vmatrix} = (\lambda - 2)(\lambda^2 + 1),
$$

so the eigenvalues are $\lambda_1 = 2$, $\lambda_2 = \mathrm{i}$ and $\lambda_3 = -\mathrm{i}$. Solving $(\lambda_iI_3 - A)\boldsymbol{x} = \boldsymbol{0}$:

1. $\lambda_1 = 2$: $2I_3 - A = \begin{bmatrix} -5 & 5 & -5 \\ 2 & -1 & 2 \\ 10 & -10 & 10 \end{bmatrix}$, eigenvector $\boldsymbol{x}_1 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$; $(2, \boldsymbol{x}_1)$ is an eigenpair of $A$ over $\mathbb{R}$;
2. $\lambda_2 = \mathrm{i}$: $\mathrm{i}I_3 - A = \begin{bmatrix} -7 + \mathrm{i} & 5 & -5 \\ 2 & -3 + \mathrm{i} & 2 \\ 10 & -10 & 8 + \mathrm{i} \end{bmatrix}$, eigenvector $\boldsymbol{x}_2 = \begin{bmatrix} -\frac{1}{2} \\ \frac{3 + \mathrm{i}}{10} \\ 1 \end{bmatrix}$;
3. $\lambda_3 = -\mathrm{i}$: eigenvector $\boldsymbol{x}_3 = \overline{\boldsymbol{x}_2} = \begin{bmatrix} -\frac{1}{2} \\ \frac{3 - \mathrm{i}}{10} \\ 1 \end{bmatrix}$ (see Proposition 6.4.1).

**Example 6.3.2**

1. A **diagonal matrix** $D = \operatorname{diag}(d_1, \dots, d_n)$ has the diagonal entries $d_1, \dots, d_n$ as its eigenvalues, and the standard basis $\boldsymbol{e}_1, \dots, \boldsymbol{e}_n$ gives $n$ linearly independent eigenvectors. $I_n$ has only the eigenvalue $1$, and every nonzero vector is an eigenvector.
2. The eigenvalues of a **triangular matrix** are its diagonal entries ($\lambda I_n - T$ is again triangular). The number of eigenvectors, however, can differ: $\begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix}$ has eigenvalues $1, 2$ with eigenvectors $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$, giving two one-dimensional eigenspaces; $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ has only the eigenvalue $1$ and only one linearly independent eigenvector, $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
3. The rotation $R_\theta$: for $\theta = k\pi$ the eigenvalue is $(-1)^k$ and the eigenspace is all of $\mathbb{C}^2$; for $\theta \ne k\pi$ there are two complex eigenvalues $\cos\theta \pm \mathrm{i}\sin\theta$ with eigenvectors $\begin{bmatrix} 1 \\ \mp\mathrm{i} \end{bmatrix}$.

In the left panel of the figure below, the real matrix has eigenvalues $2.5$ and $1$: the unit circle becomes an ellipse, a general vector $\boldsymbol{x}$ changes direction under the transformation, and only the vectors along the two eigendirections are merely stretched. On the right, $0.9R_{\pi/6}$ has a pair of conjugate complex eigenvalues $0.9\,\mathrm{e}^{\pm\mathrm{i}\pi/6}$: every vector is turned by $\pi/6$ and shortened by the factor $0.9$, there is no real invariant direction, and the iterates $B^t\boldsymbol{x}_0$ shrink to the origin along a spiral. The argument of a complex eigenvalue is the angle of rotation, and its modulus is the scaling factor.

![Left: A = [2 1; 0.5 1.5] maps the unit circle to an ellipse; the gray arrows point from x to Ax, and only the vectors along the two eigendirections keep their direction. Right: B = 0.9 R_{π/6} rotates and shortens every vector and has no real eigenvector; the orbit B^t x_0 is a shrinking spiral](./plots/eigen-directions.py)

## 6.4. Properties of Eigenvalues

### 6.4.1. The Circle Theorem

The approximate location of the eigenvalues can be estimated directly from the entries of the matrix.

**Theorem 6.4.1 (Gershgorin Circle Theorem)** For a square matrix $A = [a_{ij}]$ of order $n$, define $n$ discs in the complex plane,

$$
G_i(A) = \Big\{z \in \mathbb{C} \;\Big|\; |z - a_{ii}| \le \sum_{j \ne i}|a_{ij}|\Big\}, \qquad i = 1, \dots, n.
$$

Then every eigenvalue of $A$ lies in one of the discs, that is, all eigenvalues lie in $G_1(A) \cup \cdots \cup G_n(A)$.

**Proof** Let $\lambda_0$ be an eigenvalue; then $\lambda_0I_n - A$ is not invertible. If $\lambda_0$ lay in none of the discs, we would have $|\lambda_0 - a_{ii}| > \sum_{j \ne i}|a_{ij}|$ for every $i$, so $\lambda_0I_n - A$ would be a (strictly) **diagonally dominant matrix** and hence invertible (Chapter 2), a contradiction. $\square$

**Remark 6.4.1** A finer result (whose proof uses the continuous dependence of eigenvalues on the entries of the matrix): if the union of $k$ of the discs is disjoint from the remaining $n - k$ discs, then this union contains exactly $k$ eigenvalues (counted with multiplicity). Applying Theorem 6.4.1 to $A^{\mathsf T}$, one can also use column sums instead of row sums. In the figure below, the four discs are pairwise disjoint and each contains exactly one eigenvalue; the matrix is

$$
A = \begin{bmatrix} 6 & 1 & 0.5 & 0 \\ 0.5 & 2 & 0 & 0.5 \\ 1 & 1 & -3 & 1 \\ 0 & 0.5 & 0.5 & 3 + 2.5\mathrm{i} \end{bmatrix}.
$$

![Gershgorin discs and eigenvalues of a complex matrix of order 4: the four discs are pairwise disjoint, and each contains exactly one eigenvalue](./plots/gershgorin-discs.py)

### 6.4.2. Algebraic Multiplicity and Conjugate Eigenvalues

**Definition 6.4.1 (Algebraic Multiplicity)** Let $\lambda_0$ be an eigenvalue of a square matrix $A$ of order $n$. If $\lambda_0$ is a root of multiplicity $n_0$ of the characteristic polynomial $p_A(\lambda)$, then $n_0$ is called the **algebraic multiplicity** (or simply the multiplicity) of $\lambda_0$, and $\lambda_0$ is called an eigenvalue of multiplicity $n_0$ of $A$. An eigenvalue of multiplicity $1$ is called a **simple eigenvalue**.

**Proposition 6.4.1** If a real square matrix $A$ of order $n$ has a non-real eigenvalue $\lambda_0$, then $\overline{\lambda_0}$ is also an eigenvalue of $A$, with the same algebraic multiplicity. Moreover, if $\boldsymbol{x}_0$ is an eigenvector belonging to $\lambda_0$, then $\overline{\boldsymbol{x}_0}$ is an eigenvector belonging to $\overline{\lambda_0}$.

**Proof** $p_A$ is a polynomial with real coefficients, so the claim about eigenvalues follows from Proposition 6.2.1. Conjugating $A\boldsymbol{x}_0 = \lambda_0\boldsymbol{x}_0$ and using $\bar{A} = A$ gives $A\overline{\boldsymbol{x}_0} = \overline{\lambda_0}\,\overline{\boldsymbol{x}_0}$. $\square$

The eigenvalues $\pm\mathrm{i}$ in Example 6.3.1 and $\cos\theta \pm \mathrm{i}\sin\theta$ of the rotation in Example 6.3.2 are such conjugate pairs, and the corresponding eigenvectors are conjugate as well.

### 6.4.3. Trace and Determinant

**Theorem 6.4.2** Let $A = [a_{ij}]$ be a square matrix of order $n$. Then its characteristic polynomial has the form

$$
p_A(\lambda) = \lambda^n - \operatorname{tr}(A)\lambda^{n-1} + \cdots + (-1)^n\det A,
$$

where $\operatorname{tr}(A) = a_{11} + \cdots + a_{nn}$ is the **trace** of $A$.

**Proof** In the complete expansion of $\det(\lambda I_n - A)$, each term is a product of $n$ entries from different rows and different columns, and only the diagonal entries contain $\lambda$. To obtain $\lambda^{n-1}$, at least $n-1$ diagonal entries must be chosen, and the remaining entry, lying in a different row and column from all of them, must also be a diagonal entry. So the $\lambda^{n-1}$ term comes only from $(\lambda - a_{11})\cdots(\lambda - a_{nn})$, with coefficient $-(a_{11} + \cdots + a_{nn})$. The constant term is $p_A(0) = \det(-A) = (-1)^n\det A$. $\square$

**Corollary 6.4.1** If the $n$ eigenvalues of $A$ (counted with multiplicity) are $\lambda_1, \dots, \lambda_n$, then

$$
\lambda_1 + \lambda_2 + \cdots + \lambda_n = \operatorname{tr}(A), \qquad \lambda_1\lambda_2\cdots\lambda_n = \det A.
$$

**Proof** By Theorem 6.4.2 and Vieta's formulas (Theorem 6.2.2). $\square$

These two identities are often used in exercises to determine unknown parameters or to check computations. For example, in Example 6.3.1, $2 + \mathrm{i} - \mathrm{i} = 2 = 7 + 3 - 8$ and $2 \cdot \mathrm{i} \cdot (-\mathrm{i}) = 2 = \det A$.

**Property 6.4.1** Let $(\lambda_0, \boldsymbol{x})$ be an eigenpair of $A$.

1. For every positive integer $k$, $(\lambda_0^k, \boldsymbol{x})$ is an eigenpair of $A^k$; more generally, for every polynomial $f$, $(f(\lambda_0), \boldsymbol{x})$ is an eigenpair of $f(A)$; for example, $(1 + \lambda_0, \boldsymbol{x})$ is an eigenpair of $I_n + A$;
2. if $A$ is invertible, then $\lambda_0 \ne 0$ and $(\lambda_0^{-1}, \boldsymbol{x})$ is an eigenpair of $A^{-1}$;
3. if a polynomial $f$ satisfies $f(A) = O$, then every eigenvalue of $A$ is a root of $f$ (such an $f$ is called an annihilating polynomial of $A$; see [Chapter 10](/2.1.10)).

**Proof** 1. $A^k\boldsymbol{x} = A^{k-1}(\lambda_0\boldsymbol{x}) = \cdots = \lambda_0^k\boldsymbol{x}$, and taking linear combinations gives $f(A)\boldsymbol{x} = f(\lambda_0)\boldsymbol{x}$. 2. Multiply both sides of $A\boldsymbol{x} = \lambda_0\boldsymbol{x}$ on the left by $\lambda_0^{-1}A^{-1}$. 3. By 1, $\boldsymbol{0} = f(A)\boldsymbol{x} = f(\lambda_0)\boldsymbol{x}$, and $\boldsymbol{x} \ne \boldsymbol{0}$, so $f(\lambda_0) = 0$. $\square$

For example, a *nilpotent matrix*, that is, a square matrix with $A^k = O$ for some positive integer $k$, has only the eigenvalue $0$; the eigenvalues of an idempotent matrix ($A^2 = A$) can only be $0$ or $1$.

**Example 6.4.1 (Eigenvalues of a Rank-One Matrix)** Let $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^n$ be nonzero, $n \ge 2$. Find the eigenvalues of $A = \boldsymbol{a}\boldsymbol{b}^{\mathsf T}$.

We have $A\boldsymbol{x} = (\boldsymbol{b}^{\mathsf T}\boldsymbol{x})\boldsymbol{a}$. Hence $\mathcal{N}(A) = \operatorname{span}(\boldsymbol{b})^\perp$ is $(n-1)$-dimensional, so $0$ is an eigenvalue with eigenspace $\operatorname{span}(\boldsymbol{b})^\perp$; also $A\boldsymbol{a} = (\boldsymbol{b}^{\mathsf T}\boldsymbol{a})\boldsymbol{a}$. By Corollary 6.4.1, the sum of the eigenvalues is $\operatorname{tr}(\boldsymbol{a}\boldsymbol{b}^{\mathsf T}) = \boldsymbol{b}^{\mathsf T}\boldsymbol{a}$, and $0$ accounts for at least $n-1$ of them (the geometric multiplicity does not exceed the algebraic multiplicity; see Theorem 6.6.1 in Section 6.6), so $p_A(\lambda) = \lambda^{n-1}(\lambda - \boldsymbol{b}^{\mathsf T}\boldsymbol{a})$. There are two cases:

- $\boldsymbol{b}^{\mathsf T}\boldsymbol{a} \ne 0$: the eigenvalues are $\boldsymbol{b}^{\mathsf T}\boldsymbol{a}$ (eigenspace $\operatorname{span}(\boldsymbol{a})$) and $0$ with multiplicity $n-1$ (eigenspace $\operatorname{span}(\boldsymbol{b})^\perp$);
- $\boldsymbol{b}^{\mathsf T}\boldsymbol{a} = 0$: the only eigenvalue is $0$, with algebraic multiplicity $n$, while the eigenspace $\operatorname{span}(\boldsymbol{b})^\perp$ is only $(n-1)$-dimensional (in this case $\boldsymbol{a}$ also lies in it, and $A^2 = O$).

### 6.4.4. Companion Matrices

**Definition 6.4.2 (Companion Matrix)** For a monic polynomial $p(\lambda) = \lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_1\lambda + c_0$, the matrix

$$
C_p = \begin{bmatrix} 0 & 1 & & & \\ & 0 & 1 & & \\ & & \ddots & \ddots & \\ & & & 0 & 1 \\ -c_0 & -c_1 & \cdots & -c_{n-2} & -c_{n-1} \end{bmatrix}
$$

is called the **companion matrix** of $p$.

**Proposition 6.4.2** The characteristic polynomial of $C_p$ is $p(\lambda)$; if $\lambda_0$ is an eigenvalue of $C_p$, then $\boldsymbol{y} = [1\ \lambda_0\ \lambda_0^2\ \cdots\ \lambda_0^{n-1}]^{\mathsf T}$ is an eigenvector belonging to $\lambda_0$.

**Proof** Expand $\det(\lambda I_n - C_p)$ along row $n$, which is $[c_0\ \cdots\ c_{n-2}\ \ \lambda + c_{n-1}]$; the submatrices belonging to the cofactors are all triangular, and a computation gives $p(\lambda)$. For $\boldsymbol{y}$, the first $n-1$ components of $C_p\boldsymbol{y}$ are $\lambda_0, \dots, \lambda_0^{n-1}$, that is, $\lambda_0 y_1, \dots, \lambda_0 y_{n-1}$; the last component is $-\sum_{k=0}^{n-1}c_k\lambda_0^k = \lambda_0^n = \lambda_0y_n$ (because $p(\lambda_0) = 0$). $\square$

By the Abel–Ruffini theorem, there is no general formula for the roots of polynomials of degree five or higher, that is, the roots cannot in general be expressed by finitely many additions, subtractions, multiplications, divisions and radicals. Eigenvalues can therefore in general only be computed numerically; conversely, the roots of any polynomial can be obtained by computing the eigenvalues of its companion matrix, which is exactly what `numpy.roots` does.

## 6.5. Diagonalization

### 6.5.1. Diagonalizability and the Eigendecomposition

**Definition 6.5.1 (Diagonalizable Matrix)** If for a square matrix $A$ of order $n$ there is an invertible matrix $X$ such that $X^{-1}AX = \Lambda$ is diagonal, then $A$ is called a **diagonalizable matrix** (over $\mathbb{C}$), and $X$ is said to diagonalize $A$. If $A, X, \Lambda$ are all real, $A$ is said to be diagonalizable over $\mathbb{R}$. When $A$ is diagonalizable, the factorization $A = X\Lambda X^{-1}$ is called the **eigendecomposition** of $A$.

Some texts also call the factorization $A = X\Lambda X^{-1}$ of a general diagonalizable matrix a spectral decomposition (the set of all eigenvalues is also called the spectrum). On this site, **spectral decomposition** refers exclusively to the orthogonal (unitary) diagonalization $A = Q\Lambda Q^{\mathsf T}$ of a real symmetric (or normal) matrix, see [Chapter 7](/2.1.7); the general case is called the eigendecomposition, to keep the two apart.

The eigendecomposition reduces powers of a matrix to powers of a diagonal matrix: if $A = X\Lambda X^{-1}$, then $A^t = X\Lambda^tX^{-1}$, and if $A$ is invertible, $A^{-1} = X\Lambda^{-1}X^{-1}$. For every $\boldsymbol{x} \in \mathbb{C}^n$, write $\boldsymbol{x} = X\boldsymbol{k}$ (so that $\boldsymbol{k}$ is the coordinate vector of $\boldsymbol{x}$ with respect to the basis formed by the columns of $X$); then $A^t\boldsymbol{x} = X\Lambda^t\boldsymbol{k}$: in a basis of eigenvectors, $A$ acts by multiplying each coordinate by the corresponding eigenvalue.

**Theorem 6.5.1** A square matrix $A$ of order $n$ is diagonalizable if and only if $A$ has $n$ linearly independent eigenvectors. In that case the diagonal entries of $\Lambda$ are the eigenvalues of $A$, and the columns of $X$ are the corresponding $n$ linearly independent eigenvectors.

**Proof** Sufficiency: if $A\boldsymbol{x}_i = \lambda_i\boldsymbol{x}_i$ ($i = 1, \dots, n$) with $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ linearly independent, let $X = [\boldsymbol{x}_1\ \cdots\ \boldsymbol{x}_n]$ and $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$; then $X$ is invertible and $AX = X\Lambda$. Necessity: if $X^{-1}AX = \Lambda$, then $A[\boldsymbol{x}_1\ \cdots\ \boldsymbol{x}_n] = [\lambda_1\boldsymbol{x}_1\ \cdots\ \lambda_n\boldsymbol{x}_n]$, that is, $A\boldsymbol{x}_i = \lambda_i\boldsymbol{x}_i$, and the invertibility of $X$ shows that the $\boldsymbol{x}_i$ are linearly independent and nonzero. $\square$

### 6.5.2. Eigenvectors Belonging to Distinct Eigenvalues

**Theorem 6.5.2** Eigenvectors of a square matrix belonging to distinct eigenvalues are linearly independent.

**Proof** Let $A\boldsymbol{x}_i = \lambda_i\boldsymbol{x}_i$ with $\boldsymbol{x}_i \ne \boldsymbol{0}$ ($i = 1, \dots, r$), where $\lambda_1, \dots, \lambda_r$ are pairwise distinct, and suppose $k_1\boldsymbol{x}_1 + \cdots + k_r\boldsymbol{x}_r = \boldsymbol{0}$. Multiplying on the left by $A^i$ ($i = 1, \dots, r-1$) gives $k_1\lambda_1^i\boldsymbol{x}_1 + \cdots + k_r\lambda_r^i\boldsymbol{x}_r = \boldsymbol{0}$. In matrix form, these $r$ equations read

$$
[k_1\boldsymbol{x}_1\ k_2\boldsymbol{x}_2\ \cdots\ k_r\boldsymbol{x}_r]\begin{bmatrix} 1 & \lambda_1 & \cdots & \lambda_1^{r-1} \\ 1 & \lambda_2 & \cdots & \lambda_2^{r-1} \\ \vdots & \vdots & & \vdots \\ 1 & \lambda_r & \cdots & \lambda_r^{r-1} \end{bmatrix} = O.
$$

The factor on the right is a **Vandermonde matrix**, invertible by Theorem 5.4.1, so $k_i\boldsymbol{x}_i = \boldsymbol{0}$ and hence $k_i = 0$. $\square$

**Corollary 6.5.1** A square matrix of order $n$ with $n$ distinct eigenvalues is diagonalizable.

The condition is not necessary: $I_n$ has the single eigenvalue $1$ of multiplicity $n$, yet it is itself diagonal.

## 6.6. Geometric Multiplicity and Conditions for Diagonalizability

### 6.6.1. Geometric Multiplicity

**Definition 6.6.1 (Geometric Multiplicity)** Let $\lambda_0$ be an eigenvalue of a square matrix $A$ of order $n$. The dimension $n - \operatorname{rank}(\lambda_0I_n - A)$ of the eigenspace $\mathcal{N}(\lambda_0I_n - A)$ is called the **geometric multiplicity** of $\lambda_0$.

The geometric multiplicity is the maximal number of linearly independent eigenvectors belonging to $\lambda_0$; it is at least $1$.

**Theorem 6.6.1** The geometric multiplicity of an eigenvalue of a square matrix does not exceed its algebraic multiplicity.

**Proof** Let $\lambda_0$ have geometric multiplicity $r$, and let $\boldsymbol{x}_1, \dots, \boldsymbol{x}_r$ be a basis of $\mathcal{N}(\lambda_0I_n - A)$. Extend it to a basis $\boldsymbol{x}_1, \dots, \boldsymbol{x}_r, \boldsymbol{y}_{r+1}, \dots, \boldsymbol{y}_n$ of $\mathbb{C}^n$, and write $X_0 = [\boldsymbol{x}_1\ \cdots\ \boldsymbol{x}_r]$, $Y = [\boldsymbol{y}_{r+1}\ \cdots\ \boldsymbol{y}_n]$, so that $X = [X_0\ Y]$ is invertible. Since $AX_0 = \lambda_0X_0$,

$$
AX = [X_0\ Y]\begin{bmatrix} \lambda_0I_r & M_{12} \\ O & M_{22} \end{bmatrix} = XM.
$$

$A$ and $M = X^{-1}AX$ have the same characteristic polynomial: $\det(\lambda I_n - M) = \det(X^{-1}(\lambda I_n - A)X) = \det(\lambda I_n - A)$. Since $M$ is block upper triangular, $\det(\lambda I_n - M) = (\lambda - \lambda_0)^r\det(\lambda I_{n-r} - M_{22})$, so the algebraic multiplicity of $\lambda_0$ is at least $r$. $\square$

**Definition 6.6.2 (Semisimple and Defective Eigenvalues)** An eigenvalue whose geometric multiplicity equals its algebraic multiplicity is called a **semisimple eigenvalue**; an eigenvalue whose geometric multiplicity is less than its algebraic multiplicity is called a **defective eigenvalue**.

Both multiplicities of a simple eigenvalue are $1$, so a simple eigenvalue is always semisimple.

### 6.6.2. Equivalent Conditions for Diagonalizability

**Theorem 6.6.2**

1. A square matrix $A$ of order $n$ is diagonalizable if and only if all its eigenvalues are semisimple;
2. a real square matrix $A$ of order $n$ is diagonalizable over $\mathbb{R}$ if and only if all its eigenvalues are real and semisimple.

**Proof** 1. Let $\lambda_1, \dots, \lambda_s$ be all the distinct eigenvalues of $A$, with geometric multiplicities $m_1, \dots, m_s$ and algebraic multiplicities $n_1, \dots, n_s$, so that $\sum_i n_i = n$.

Necessity: if $A$ is diagonalizable, it has $n$ linearly independent eigenvectors; if $k_i$ of them belong to $\lambda_i$, these all lie in $\mathcal{N}(\lambda_iI_n - A)$, so $k_i \le m_i \le n_i$; since $\sum k_i = n = \sum n_i$, we get $k_i = m_i = n_i$.

Sufficiency: if $m_i = n_i$, choose a basis in each eigenspace, giving $\sum m_i = n$ eigenvectors in total. They are linearly independent: if some linear combination of them is zero, group the terms belonging to the same eigenvalue into $\boldsymbol{u}_i \in \mathcal{N}(\lambda_iI_n - A)$, so that $\sum\boldsymbol{u}_i = \boldsymbol{0}$; by Theorem 6.5.2 the nonzero $\boldsymbol{u}_i$ cannot be linearly dependent, so every $\boldsymbol{u}_i = \boldsymbol{0}$, and the linear independence of each basis shows that all coefficients vanish. By Theorem 6.5.1, $A$ is diagonalizable.

2. If $A = X\Lambda X^{-1}$ with $X, \Lambda$ real, then the eigenvalues (the diagonal entries of $\Lambda$) are all real, and by 1 they are semisimple. Conversely, if all eigenvalues are real, then $\lambda_iI_n - A$ is a real matrix whose rank over $\mathbb{R}$ equals its rank over $\mathbb{C}$ (elimination uses only real arithmetic), so each eigenspace has a basis of real vectors, and the sufficiency argument in 1 yields a real $X$. $\square$

**Proposition 6.6.1 (Diagonalization of Block Diagonal Matrices)** A **block diagonal matrix** $A = \operatorname{diag}(A_1, \dots, A_r)$ (with square diagonal blocks $A_i$) is diagonalizable if and only if every $A_i$ is diagonalizable.

**Proof** It suffices to prove the case $r = 2$. Sufficiency: if $X_i^{-1}A_iX_i = D_i$ is diagonal, let $X = \operatorname{diag}(X_1, X_2)$; then $X^{-1}AX = \operatorname{diag}(D_1, D_2)$. Necessity: $p_A(\lambda) = p_{A_1}(\lambda)p_{A_2}(\lambda)$. For any eigenvalue $\lambda_0$ of $A$, let its algebraic multiplicities as an eigenvalue of $A_1, A_2$ be $n_{01}, n_{02}$ (set to $0$ if it is not an eigenvalue) and its geometric multiplicities $m_{01}, m_{02}$. Then the algebraic multiplicity of $\lambda_0$ as an eigenvalue of $A$ is $n_{01} + n_{02}$, and since $\operatorname{rank}(\lambda_0I - A) = \operatorname{rank}(\lambda_0I - A_1) + \operatorname{rank}(\lambda_0I - A_2)$, its geometric multiplicity is $m_{01} + m_{02}$. Because $A$ is diagonalizable, $m_{01} + m_{02} = n_{01} + n_{02}$; together with $m_{01} \le n_{01}$ and $m_{02} \le n_{02}$ this gives $m_{01} = n_{01}$ and $m_{02} = n_{02}$, so the eigenvalues of $A_1, A_2$ are all semisimple. $\square$

**Example 6.6.1**

1. $I_n$ has only the eigenvalue $1$, with algebraic and geometric multiplicity both $n$; $1$ is a semisimple eigenvalue.
2. The row-addition matrix $E_{21;k} = \begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}$ ($k \ne 0$) has only the eigenvalue $1$, with algebraic multiplicity $2$ and geometric multiplicity $1$; $1$ is a defective eigenvalue, and $E_{21;k}$ is not diagonalizable. Geometrically, a shear has only one invariant direction.

**Definition 6.6.3 (Jordan Block)** The square matrix of order $n$

$$
J_n(\lambda) = \begin{bmatrix} \lambda & 1 & & \\ & \lambda & \ddots & \\ & & \ddots & 1 \\ & & & \lambda \end{bmatrix}
$$

is called the **Jordan block** of order $n$ for $\lambda$.

$J_n(\lambda)$ has only the eigenvalue $\lambda$, with algebraic multiplicity $n$; $\lambda I_n - J_n(\lambda)$ has rank $n-1$, so the geometric multiplicity is $1$. For $n > 1$, $\lambda$ is a defective eigenvalue and $J_n(\lambda)$ is not diagonalizable. Section 6.10 explains that Jordan blocks are the "building blocks" of non-diagonalizable matrices.

**Property 6.6.1**

1. An idempotent matrix ($A^2 = A$) is diagonalizable and is similar to $\operatorname{diag}(I_r, O)$, where $r = \operatorname{rank}(A)$;
2. let $\boldsymbol{v}$ be a unit vector; then there is an orthogonal matrix $Q$ with $Q^{-1}H_{\boldsymbol{v}}Q = \operatorname{diag}(-1, 1, \dots, 1)$, where $H_{\boldsymbol{v}} = I_n - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}$ is a **Householder reflection**.

**Proof** 1. For every $\boldsymbol{x}$, $\boldsymbol{x} = A\boldsymbol{x} + (\boldsymbol{x} - A\boldsymbol{x})$ with $A(A\boldsymbol{x}) = A\boldsymbol{x}$ and $A(\boldsymbol{x} - A\boldsymbol{x}) = \boldsymbol{0}$. So every nonzero vector of $\mathcal{R}(A)$ is an eigenvector belonging to $1$, $\mathcal{N}(A)$ is the eigenspace belonging to $0$, and their dimensions add up to $\operatorname{rank}(A) + (n - \operatorname{rank}(A)) = n$. Bases of $\mathcal{R}(A)$ and $\mathcal{N}(A)$ taken together are linearly independent by the argument of Theorem 6.5.2, giving $n$ linearly independent eigenvectors. 2. $H_{\boldsymbol{v}}\boldsymbol{v} = -\boldsymbol{v}$, and $H_{\boldsymbol{v}}\boldsymbol{w} = \boldsymbol{w}$ for $\boldsymbol{w} \perp \boldsymbol{v}$. Take $\boldsymbol{v}$ as the first column of $Q$ and an orthonormal basis of $\operatorname{span}(\boldsymbol{v})^\perp$ as the remaining columns. $\square$

### 6.6.3. Computing a Diagonalization

**Algorithm 6.6.1 (Diagonalization)** Input: a square matrix $A$ of order $n$.

1. Use Algorithm 6.3.1 to find all distinct eigenvalues $\lambda_1, \dots, \lambda_s$ and their algebraic multiplicities $n_1, \dots, n_s$;
2. for each $\lambda_i$, find a basis of $\mathcal{N}(\lambda_iI_n - A)$; the number of basis vectors is the geometric multiplicity $m_i$;
3. if $m_i < n_i$ for some $i$, then $A$ is not diagonalizable; stop;
4. otherwise, arrange all the basis vectors as the columns of $X$ and the corresponding eigenvalues (each repeated $m_i$ times) as $\Lambda$, giving $A = X\Lambda X^{-1}$.

## 6.7. Application: Matrix Powers and Linear Recurrences

**Example 6.7.1** Find the eigendecomposition of $A = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 2 & 0 \\ -1 & -1 & 3 \end{bmatrix}$ and $A^n$.

$A$ is lower triangular with eigenvalues $1, 2, 3$, which are distinct, so $A$ is diagonalizable. The corresponding eigenvectors are $\boldsymbol{x}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$, $\boldsymbol{x}_2 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$ and $\boldsymbol{x}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$. Let

$$
X = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}, \quad \Lambda = \begin{bmatrix} 1 & & \\ & 2 & \\ & & 3 \end{bmatrix}, \quad X^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix};
$$

then $A = X\Lambda X^{-1}$ and

$$
A^n = X\Lambda^nX^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 1 - 2^n & 2^n & 0 \\ 1 - 2^n & 2^n - 3^n & 3^n \end{bmatrix}.
$$

**Example 6.7.2 (Fibonacci Numbers)** Let $F_0 = 0$, $F_1 = 1$ and $F_{n+1} = F_n + F_{n-1}$ ($n \ge 1$). Find a closed formula for $F_n$.

Let $\boldsymbol{u}_n = \begin{bmatrix} F_n \\ F_{n-1} \end{bmatrix}$; the recurrence becomes

$$
\boldsymbol{u}_{n+1} = \begin{bmatrix} F_{n+1} \\ F_n \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} F_n \\ F_{n-1} \end{bmatrix} = A\boldsymbol{u}_n,
$$

so $\boldsymbol{u}_n = A^{n-1}\boldsymbol{u}_1$ with $\boldsymbol{u}_1 = \boldsymbol{e}_1$. Here $p_A(\lambda) = \lambda^2 - \lambda - 1$, with eigenvalues $\lambda_1 = \frac{1 + \sqrt{5}}{2}$ and $\lambda_2 = \frac{1 - \sqrt{5}}{2}$ and eigenvectors $\boldsymbol{x}_i = \begin{bmatrix} \lambda_i \\ 1 \end{bmatrix}$ (because $\lambda_i^2 = \lambda_i + 1$). With $X = [\boldsymbol{x}_1\ \boldsymbol{x}_2]$ and $X^{-1} = \dfrac{1}{\lambda_1 - \lambda_2}\begin{bmatrix} 1 & -\lambda_2 \\ -1 & \lambda_1 \end{bmatrix}$,

$$
F_n = \boldsymbol{e}_1^{\mathsf T}\boldsymbol{u}_n = \boldsymbol{e}_1^{\mathsf T}X\Lambda^{n-1}X^{-1}\boldsymbol{e}_1 = \frac{1}{\lambda_1 - \lambda_2}[\lambda_1\ \ \lambda_2]\begin{bmatrix} \lambda_1^{n-1} & \\ & \lambda_2^{n-1} \end{bmatrix}\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \frac{\lambda_1^n - \lambda_2^n}{\lambda_1 - \lambda_2} = \frac{1}{\sqrt{5}}\left[\left(\frac{1 + \sqrt{5}}{2}\right)^n - \left(\frac{1 - \sqrt{5}}{2}\right)^n\right].
$$

Since $|\lambda_2| < 1$, $F_n$ is the integer nearest to $\lambda_1^n/\sqrt{5}$, and $F_{n+1}/F_n \to \lambda_1$ (the golden ratio).

In general, if $A$ is diagonalizable, then $A^t\boldsymbol{x} = \sum_i k_i\lambda_i^t\boldsymbol{x}_i$, and for large $t$ the eigenvalue of largest absolute value dominates: if all eigenvalues have absolute value less than $1$, then $A^t\boldsymbol{x} \to \boldsymbol{0}$; if the largest exceeds $1$, then in general $\|A^t\boldsymbol{x}\| \to \infty$. In Example 6.1.1, the eigenvalue $1$ determines the limiting distribution and $0.5$ determines the rate of convergence. The following code checks these two examples:

```python
import numpy as np

# Example 6.1.1: A^t tends to the rank-one matrix [x1 x1] with x1 = (0.2, 0.8)
A = np.array([[0.6, 0.1], [0.4, 0.9]])
print(np.linalg.eigvals(A))              # eigenvalues 0.5 and 1
print(np.linalg.matrix_power(A, 50))     # close to [[0.2, 0.2], [0.8, 0.8]]

# Example 6.7.2: Binet's formula from the eigendecomposition of [[1, 1], [1, 0]]
phi, psi = (1 + 5**0.5) / 2, (1 - 5**0.5) / 2
print([round((phi**n - psi**n) / 5**0.5) for n in range(1, 11)])
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

The figure below shows the iterates $A^t\boldsymbol{x}$ of Example 6.1.1 for several initial distributions. At each step the component belonging to the eigenvalue $0.5$ is halved, so the iterates move along the direction $\boldsymbol{x}_2 = (1, -1)$ (the total population is preserved) toward the eigenline $\operatorname{span}(\boldsymbol{x}_1)$, and the distance to the limit decays like $0.5^t$.

![Migration in Example 6.1.1: on the left, the iterates of each initial distribution converge along the direction x2 to the eigenline span(x1); on the right, the distance to the limit decays like the powers 0.5^t of the second eigenvalue](./plots/migration-iteration.py)

## 6.8. Similarity

### 6.8.1. The Similarity Relation

**Definition 6.8.1 (Similarity)** Square matrices $A, B$ of order $n$ are called **similar matrices** if there is an invertible matrix $X$ such that $X^{-1}AX = B$; we also say that $A$ is similar to $B$.

**Example 6.8.1**

1. A scalar matrix $kI_n$ is similar only to itself: $X^{-1}(kI_n)X = kI_n$.
2. $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ is similar to $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$: $\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}^{-1}\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$.
3. Two diagonal matrices whose diagonal entries differ only by a permutation are similar: for $\Lambda_1 = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ and $\Lambda_2 = \operatorname{diag}(\lambda_{\sigma_1}, \dots, \lambda_{\sigma_n})$, take the **permutation matrix** $P = [\boldsymbol{e}_{\sigma_1}\ \cdots\ \boldsymbol{e}_{\sigma_n}]$; then $P^{-1}\Lambda_1P = \Lambda_2$.

**Proposition 6.8.1** Similarity of square matrices is an **equivalence relation**.

**Proof** Reflexivity: $A = I_n^{-1}AI_n$. Symmetry: $X^{-1}AX = B$ gives $(X^{-1})^{-1}BX^{-1} = A$. Transitivity: $X^{-1}AX = B$ and $Y^{-1}BY = C$ give $(XY)^{-1}A(XY) = C$. $\square$

The corresponding transformation $A \mapsto X^{-1}AX$ is called a similarity transformation. $A$ is diagonalizable if and only if $A$ is similar to a diagonal matrix; if $A, B$ are similar, then $A$ is diagonalizable if and only if $B$ is. If $X^{-1}AX = B$, then $A\boldsymbol{x} = \boldsymbol{b}$ is equivalent to $B(X^{-1}\boldsymbol{x}) = X^{-1}\boldsymbol{b}$: similar matrices represent the same linear transformation with respect to two different bases, and the columns of $X$ form the new basis (see [Chapter 8](/2.1.8) for details).

### 6.8.2. Similarity Invariants

**Theorem 6.8.1** Similar square matrices have the same:

1. rank;
2. characteristic polynomial, and hence the same eigenvalues, algebraic multiplicities of eigenvalues, trace and determinant;
3. geometric multiplicities of eigenvalues.

Moreover, if $(\lambda, \boldsymbol{u})$ is an eigenpair of $A$, then $(\lambda, X^{-1}\boldsymbol{u})$ is an eigenpair of $X^{-1}AX$.

**Proof** 1. Multiplying on the left or right by invertible matrices does not change the rank. 2. $\det(\lambda I_n - X^{-1}AX) = \det(X^{-1}(\lambda I_n - A)X) = \det(\lambda I_n - A)$; the trace and determinant are determined by the eigenvalues (Corollary 6.4.1). 3. $\operatorname{rank}(\lambda I_n - X^{-1}AX) = \operatorname{rank}(X^{-1}(\lambda I_n - A)X) = \operatorname{rank}(\lambda I_n - A)$, so the eigenspaces have the same dimension. Finally, $X^{-1}AX(X^{-1}\boldsymbol{u}) = X^{-1}A\boldsymbol{u} = \lambda X^{-1}\boldsymbol{u}$. $\square$

These invariants do not suffice to decide similarity: $I_2$ and $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ have the same rank, characteristic polynomial, trace and determinant, but $I_2$ is similar only to itself. Adding the geometric multiplicity of every eigenvalue is still not enough (for order at least $4$); a complete invariant is the Jordan canonical form of Section 6.10.

**Corollary 6.8.1** Two diagonal matrices are similar if and only if their diagonal entries agree up to order.

**Proof** Sufficiency is item 3 of Example 6.8.1. Necessity: similar matrices have the same eigenvalues (counted with multiplicity), and the eigenvalues of a diagonal matrix are its diagonal entries. $\square$

When $A$ is diagonalizable, a diagonal matrix similar to it is called the similarity normal form of $A$; it is unique up to the order of the diagonal entries.

## 6.9. Triangularization and the Cayley–Hamilton Theorem

Not every square matrix can be diagonalized, but every square matrix can be brought to upper triangular form by a similarity transformation.

**Theorem 6.9.1** For a square matrix $A$ of order $n$ there is an invertible matrix $X$ such that $X^{-1}AX = T$ is upper triangular, and the diagonal entries of $T$ are the $n$ eigenvalues of $A$ (counted with multiplicity). Moreover, $X$ can be chosen so that the diagonal entries of $T$ appear in any prescribed order.

**Proof** We use induction on $n$; the case $n = 1$ is clear. Suppose the claim holds for square matrices of order $n-1$. Take any eigenpair $(\lambda_1, \boldsymbol{x}_1)$ of $A$, extend $\boldsymbol{x}_1$ to a basis $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ of $\mathbb{C}^n$, and let $X_1 = [\boldsymbol{x}_1\ X_{12}]$. Then

$$
AX_1 = [\lambda_1\boldsymbol{x}_1\ \ AX_{12}] = [\boldsymbol{x}_1\ X_{12}]\begin{bmatrix} \lambda_1 & * \\ \boldsymbol{0} & A_1 \end{bmatrix},
$$

where $A_1$ is a square matrix of order $n-1$. By the induction hypothesis there is an invertible matrix $X_2$ such that $X_2^{-1}A_1X_2 = T_2$ is upper triangular, so

$$
A = X_1\begin{bmatrix} \lambda_1 & * \\ \boldsymbol{0} & X_2T_2X_2^{-1} \end{bmatrix}X_1^{-1} = X_1\begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & X_2 \end{bmatrix}\begin{bmatrix} \lambda_1 & * \\ \boldsymbol{0} & T_2 \end{bmatrix}\begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & X_2 \end{bmatrix}^{-1}X_1^{-1}.
$$

Let $X = X_1\operatorname{diag}(1, X_2)$ and $T = \begin{bmatrix} \lambda_1 & * \\ \boldsymbol{0} & T_2 \end{bmatrix}$; then $X$ is invertible, $T$ is upper triangular and $A = XTX^{-1}$. $T$ is similar to $A$, so they have the same eigenvalues, and the eigenvalues of a triangular matrix are its diagonal entries. Since any eigenvalue may be chosen at each step, the diagonal entries can be put in any prescribed order. $\square$

The proof is itself a dimension-reducing algorithm: take an eigenvector, extend it to a basis, and repeat with the lower right block of order $n-1$. [Chapter 10](/2.1.10) writes it as a constructive algorithm under the name of the **Schur triangularization theorem**, and [Chapter 12](/2.1.12) strengthens $X$ to a unitary matrix.

**Theorem 6.9.2 (Cayley–Hamilton Theorem)** Let $p_A(\lambda)$ be the characteristic polynomial of a square matrix $A$. Then $p_A(A) = O$.

Following a different convention, it is also called the Hamilton–Cayley theorem.

**Proof** By Theorem 6.9.1, $A = XTX^{-1}$ with $T$ upper triangular, so $p_A(A) = Xp_A(T)X^{-1}$ and it suffices to prove $p_A(T) = O$. Let the diagonal entries of $T$ be $\lambda_1, \dots, \lambda_n$ in order; then $p_A(\lambda) = (\lambda - \lambda_1)\cdots(\lambda - \lambda_n)$ and

$$
p_A(T) = (T - \lambda_1I_n)(T - \lambda_2I_n)\cdots(T - \lambda_nI_n),
$$

where $T - \lambda_iI_n$ is upper triangular with $i$-th diagonal entry zero. Let $T_i = (T - \lambda_1I_n)\cdots(T - \lambda_iI_n)$; we show by induction that the first $i$ columns of $T_i$ are zero. The first column of $T_1 = T - \lambda_1I_n$ is zero. Suppose the first $i$ columns of $T_i$ are zero, write $T_i = [O_{n \times i}\ P]$, and partition $T - \lambda_{i+1}I_n$ by rows as $\begin{bmatrix} * \\ Q \end{bmatrix}$, where $Q$ consists of the last $n - i$ rows; since $T - \lambda_{i+1}I_n$ is upper triangular with $(i+1)$-th diagonal entry zero, the first $i + 1$ columns of $Q$ are zero. Hence the first $i+1$ columns of $T_{i+1} = [O\ P]\begin{bmatrix} * \\ Q \end{bmatrix} = PQ$ are zero. Therefore $p_A(T) = T_n = O$. $\square$

**Example 6.9.1** Let $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$, so $p_A(\lambda) = \lambda^2 - 5\lambda - 2$. Then $A^2 - 5A - 2I_2 = O$, that is, $A^2 = 5A + 2I_2$, and

$$
A^3 = 5A^2 + 2A = 27A + 10I_2.
$$

Since $\det A = -2 \ne 0$, $A$ is invertible. From $A(A - 5I_2) = 2I_2$ we get

$$
A^{-1} = \frac{1}{2}(A - 5I_2), \qquad A^{-2} = \frac{1}{4}(A - 5I_2)^2 = \frac{1}{4}(-5A + 27I_2).
$$

Similarly, every power of $A$ (including negative integer powers) can be written as a linear combination of $A$ and $I_2$. In general, for a square matrix of order $n$ and a polynomial $f$, division with remainder by $p_A$, $f = qp_A + r$ with $\deg r < n$, gives $f(A) = r(A)$: the value of any polynomial at $A$ reduces to that of a polynomial of degree less than $n$. This is the starting point for computing matrix functions in [Chapter 11](/2.1.11).

## 6.10. The Jordan Canonical Form

**Theorem 6.10.1 (Jordan Decomposition)** For a square matrix $A$ of order $n$ there is an invertible matrix $X$ such that

$$
X^{-1}AX = J = \begin{bmatrix} J_{n_1}(\lambda_1) & & & \\ & J_{n_2}(\lambda_2) & & \\ & & \ddots & \\ & & & J_{n_r}(\lambda_r) \end{bmatrix},
$$

where $J_{n_i}(\lambda_i)$ is a Jordan block of order $n_i$, $n_1 + \cdots + n_r = n$, and some of $\lambda_1, \dots, \lambda_r$ may coincide. Up to the order of the Jordan blocks, $J$ is uniquely determined by $A$. When $A$ is a real square matrix whose eigenvalues are all real, $X$ can be chosen real. The factorization $A = XJX^{-1}$ is called the Jordan decomposition of $A$, and $J$ is called the **Jordan canonical form** of $A$.

This chapter only states the theorem; its proof and the computation are in [Chapter 10](/2.1.10). A few remarks:

- Each Jordan block contributes exactly one linearly independent eigenvector, so $A$ has $r$ linearly independent eigenvectors; the number of Jordan blocks for $\lambda$ equals the geometric multiplicity of $\lambda$, and the sum of their orders equals the algebraic multiplicity.
- $A$ is diagonalizable if and only if all $n_i = 1$, in which case $J = \Lambda$ and $r = n$.
- Two square matrices are similar if and only if they have the same Jordan canonical form (up to the order of the blocks).
- The Jordan canonical form is extremely unstable under small perturbations of the entries (for example, an arbitrarily small perturbation of $J_n(0)$ may be diagonalizable), so it is a theoretical tool; numerical computation usually replaces it by triangularization under orthogonal (unitary) similarity ([Chapter 12](/2.1.12)) or by the singular value decomposition ([Chapter 7](/2.1.7)).

**Example 6.10.1** Let $A = \begin{bmatrix} 0 & 1 & 0 \\ -1 & 1 & 1 \\ -1 & 0 & 2 \end{bmatrix}$. Then $p_A(\lambda) = (\lambda - 1)^3$, so $A$ has only the eigenvalue $\lambda = 1$, with algebraic multiplicity $3$.

$$
\lambda I_3 - A = \begin{bmatrix} 1 & -1 & 0 \\ 1 & 0 & -1 \\ 1 & 0 & -1 \end{bmatrix}
$$

has rank $2$, so the geometric multiplicity is $1$; $\lambda$ is a defective eigenvalue, $A$ is not diagonalizable, and its Jordan canonical form must consist of a single Jordan block of order $3$. To find $X$, take a nonzero vector $\boldsymbol{x}_3$ with $(A - \lambda I_3)^2\boldsymbol{x}_3 \ne \boldsymbol{0}$, and set $\boldsymbol{x}_2 = (A - \lambda I_3)\boldsymbol{x}_3$ and $\boldsymbol{x}_1 = (A - \lambda I_3)\boldsymbol{x}_2$. Such an $\boldsymbol{x}_3$ exists: by the Cayley–Hamilton theorem $(A - \lambda I_3)^3 = O$, while $\dim\mathcal{N}((A - \lambda I_3)^2) \le 2\dim\mathcal{N}(A - \lambda I_3) = 2 < 3$ (in general $\dim\mathcal{N}(BC) \le \dim\mathcal{N}(B) + \dim\mathcal{N}(C)$). Take

$$
\boldsymbol{x}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}, \quad \boldsymbol{x}_2 = (A - \lambda I_3)\boldsymbol{x}_3 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}, \quad \boldsymbol{x}_1 = (A - \lambda I_3)\boldsymbol{x}_2 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \quad (A - \lambda I_3)\boldsymbol{x}_1 = \boldsymbol{0},
$$

that is, $A\boldsymbol{x}_1 = \lambda\boldsymbol{x}_1$, $A\boldsymbol{x}_2 = \boldsymbol{x}_1 + \lambda\boldsymbol{x}_2$ and $A\boldsymbol{x}_3 = \boldsymbol{x}_2 + \lambda\boldsymbol{x}_3$; $\boldsymbol{x}_1$ is an eigenvector. The vectors $\boldsymbol{x}_1, \boldsymbol{x}_2, \boldsymbol{x}_3$ are linearly independent (if $k_1\boldsymbol{x}_1 + k_2\boldsymbol{x}_2 + k_3\boldsymbol{x}_3 = \boldsymbol{0}$, multiplying on the left by $(A - \lambda I_3)^2$ and then by $A - \lambda I_3$ gives $k_3 = 0$ and $k_2 = 0$, and then $k_1 = 0$). With $X = [\boldsymbol{x}_1\ \boldsymbol{x}_2\ \boldsymbol{x}_3]$,

$$
AX = X\begin{bmatrix} \lambda & 1 & \\ & \lambda & 1 \\ & & \lambda \end{bmatrix} = XJ_3(\lambda), \qquad X^{-1}AX = J_3(1).
$$

## 6.11. Simultaneous Diagonalization

**Definition 6.11.1 (Simultaneous Diagonalization)** Let $A, B$ be square matrices of order $n$. If there is an invertible matrix $X$ such that both $X^{-1}AX = \Lambda_1$ and $X^{-1}BX = \Lambda_2$ are diagonal, then $A, B$ are said to admit **simultaneous diagonalization**.

$A, B$ admit simultaneous diagonalization if and only if there are $n$ linearly independent vectors that are eigenvectors of both $A$ and $B$ (the corresponding eigenvalues may differ).

**Theorem 6.11.1** Let $A, B$ be diagonalizable square matrices of order $n$. Then $A, B$ can be diagonalized simultaneously if and only if $AB = BA$.

**Proof** Necessity: if $X^{-1}AX = \Lambda_1$ and $X^{-1}BX = \Lambda_2$, then, since diagonal matrices commute,

$$
AB = X\Lambda_1X^{-1}X\Lambda_2X^{-1} = X\Lambda_1\Lambda_2X^{-1} = X\Lambda_2\Lambda_1X^{-1} = BA.
$$

Sufficiency: $A$ is diagonalizable, so grouping equal eigenvalues together, there is an invertible $X_1$ with $X_1^{-1}AX_1 = \Lambda_1 = \operatorname{diag}(\lambda_1I_{n_1}, \dots, \lambda_rI_{n_r})$, where $\lambda_1, \dots, \lambda_r$ are pairwise distinct. Let $\tilde{B} = X_1^{-1}BX_1$; then $AB = BA$ gives $\Lambda_1\tilde{B} = \tilde{B}\Lambda_1$. Partition $\tilde{B}$ in the same way as $[\tilde{B}_{ij}]$; comparing $(i, j)$ blocks on both sides gives $\lambda_i\tilde{B}_{ij} = \lambda_j\tilde{B}_{ij}$, so $\tilde{B}_{ij} = O$ for $i \ne j$, that is, $\tilde{B} = \operatorname{diag}(\tilde{B}_{11}, \dots, \tilde{B}_{rr})$. Since $B$ is diagonalizable, so is the similar matrix $\tilde{B}$, and by Proposition 6.6.1 every $\tilde{B}_{ii}$ is diagonalizable: $X_{ii}^{-1}\tilde{B}_{ii}X_{ii} = \Lambda_{ii}$. Let $X_2 = \operatorname{diag}(X_{11}, \dots, X_{rr})$; then

$$
(X_1X_2)^{-1}B(X_1X_2) = X_2^{-1}\tilde{B}X_2 = \operatorname{diag}(\Lambda_{11}, \dots, \Lambda_{rr}), \qquad (X_1X_2)^{-1}A(X_1X_2) = X_2^{-1}\Lambda_1X_2 = \Lambda_1,
$$

the latter because every diagonal block of $\Lambda_1$ is a scalar matrix. So $X_1X_2$ diagonalizes $A$ and $B$ simultaneously. $\square$

The idea of the proof: since $B$ commutes with $A$, $B$ maps each eigenspace of $A$ into itself, so $B$ can be diagonalized within each eigenspace.

## Summary {#summary}

The theme of this chapter is "simplify a square matrix up to similarity": into a diagonal matrix when it is diagonalizable (the eigendecomposition), into an upper triangular matrix in general, and the simplest form is the Jordan canonical form.

| Concept or result | Content | Location |
|---|---|---|
| Eigenvalues, eigenvectors | $A\boldsymbol{x} = \lambda\boldsymbol{x}$, $\boldsymbol{x} \ne \boldsymbol{0}$; $\lambda$ is a root of $p_A(\lambda) = \det(\lambda I - A)$ | Definition 6.3.1, Proposition 6.3.1 |
| Eigenspace | $\mathcal{N}(\lambda_0I - A)$ | Definition 6.3.3 |
| Circle theorem | the eigenvalues lie in $\bigcup_i\{z : \vert z - a_{ii}\vert \le \sum_{j \ne i}\vert a_{ij}\vert\}$ | Theorem 6.4.1 |
| Trace and determinant | $\sum\lambda_i = \operatorname{tr}(A)$, $\prod\lambda_i = \det A$ | Corollary 6.4.1 |
| Eigenvalues of related matrices | $f(A)$ has eigenvalues $f(\lambda)$; $A^{-1}$ has $\lambda^{-1}$; $f(A) = O$ ⇒ $f(\lambda) = 0$ | Property 6.4.1 |
| Companion matrix | characteristic polynomial equal to a given monic polynomial | Proposition 6.4.2 |
| Diagonalizability | ⇔ $n$ linearly independent eigenvectors ⇔ all eigenvalues semisimple | Theorem 6.5.1, Theorem 6.6.2 |
| Distinct eigenvalues | eigenvectors are linearly independent; $n$ distinct eigenvalues ⇒ diagonalizable | Theorem 6.5.2, Corollary 6.5.1 |
| The two multiplicities | $1 \le$ geometric multiplicity $\le$ algebraic multiplicity | Theorem 6.6.1 |
| Similarity invariants | rank, characteristic polynomial, eigenvalues and both multiplicities, trace, determinant | Theorem 6.8.1 |
| Triangularization | every square matrix is similar to an upper triangular matrix whose diagonal entries are the eigenvalues | Theorem 6.9.1 |
| Cayley–Hamilton theorem | $p_A(A) = O$ | Theorem 6.9.2 |
| Jordan canonical form | $X^{-1}AX = \operatorname{diag}(J_{n_1}(\lambda_1), \dots, J_{n_r}(\lambda_r))$, unique up to order | Theorem 6.10.1 |
| Simultaneous diagonalization | two diagonalizable matrices can be diagonalized simultaneously ⇔ they commute | Theorem 6.11.1 |

| Algorithm | Steps | Notes |
|---|---|---|
| Computing eigenvalues and eigenvectors (Algorithm 6.3.1) | find the roots of $p_A$; for each $\lambda_i$ solve $(\lambda_iI - A)\boldsymbol{x} = \boldsymbol{0}$ | hand computation; numerical computation uses the QR iteration |
| Diagonalization (Algorithm 6.6.1) | compare the geometric and algebraic multiplicity of each eigenvalue; assemble $X$ and $\Lambda$ | gives $A = X\Lambda X^{-1}$ and $A^t = X\Lambda^tX^{-1}$ |
| Simplification by the Cayley–Hamilton theorem (Example 6.9.1) | $f = qp_A + r$ ⇒ $f(A) = r(A)$ | computing high powers and inverses |
