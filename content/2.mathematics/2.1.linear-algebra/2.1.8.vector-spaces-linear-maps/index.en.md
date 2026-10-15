---
title: Vector Spaces and Linear Maps
source_hash: 3dec4e6c1ef3
---

The first seven chapters work in $\mathbb{R}^n$: vectors are arrays of numbers and linear maps are matrices. But linearity is far more widespread. Solutions of a homogeneous linear differential equation can be added and scaled; polynomials, matrices and functions can all be combined linearly; differentiation, transposition, taking the trace, and evaluation at given points all obey the superposition principle. This chapter abstracts the notions of $\mathbb{R}^n$ into vector spaces and linear maps over a number field, so that all of the preceding theory applies to such objects.

This chapter is the turning point of the course. Sections 8.1–8.3 carry subspaces, linear dependence, bases and dimension over to general vector spaces (the arguments are those of [Chapter 3](/2.1.3), but no longer rely on the concrete form of matrices) and add intersections, sums and direct sums of subspaces. Sections 8.4–8.7 form the core of the chapter: once a basis is fixed, abstract vectors become coordinates, linear maps become matrices, composition becomes **matrix multiplication**, and kernels and images become **null spaces** and **column spaces**; changing bases changes the matrix of a linear map by an equivalence and the matrix of a linear transformation by a similarity. All earlier results on matrices thus become properties of linear maps themselves, and "simplifying a matrix" becomes "choosing a good basis for a linear map". The following chapters pursue exactly this program: [Chapter 10](/2.1.10) looks for a basis in which the matrix of a linear transformation is as simple as possible (the Jordan canonical form), [Chapter 12](/2.1.12) requires that basis to be orthonormal, and [Chapter 13](/2.1.13) studies the congruence of bilinear forms under change of basis. Section 8.8 introduces dual spaces, which explain the meaning of the transpose $A^{\mathsf T}$ and are the starting point for the bilinear forms and tensors of Chapter 13. The abstract definition here agrees with that of a **vector space** over a field in discrete mathematics ([1.3.3](/1.3.3)), except that the scalars are taken from a number field.

Notation: from this chapter on, a general number field is denoted $\mathbb{F}$; abstract vector spaces are denoted by italic capitals $V, W$, and their elements (including the zero vector $0$) by plain italic letters $v, w$, not bold; only column vectors in $\mathbb{F}^n$ are bold, including the coordinates of abstract vectors with respect to a basis (such as $\hat{\boldsymbol{x}}\in\mathbb{F}^n$). Whether a symbol is bold thus signals whether the object is a concrete array or an abstract vector.

## 8.1. Number Fields and Vector Spaces

**Definition 8.1.1 (Number Field)** Let $\mathbb{F}$ be a subset of the set $\mathbb{C}$ of complex numbers that contains at least one nonzero complex number and is closed under the four arithmetic operations of addition, subtraction, multiplication and division (by nonzero numbers). Then $\mathbb{F}$ is called a **number field**.

Since $\mathbb{F}$ contains a nonzero number $a$, it contains $a-a=0$ and $a/a=1$, and hence all rational numbers: every number field contains $\mathbb{Q}$. Common number fields are the rational numbers $\mathbb{Q}$, the real numbers $\mathbb{R}$ and the complex numbers $\mathbb{C}$; the natural numbers $\mathbb{N}$ and the integers $\mathbb{Z}$ are not number fields (they are not closed under subtraction or division). $\mathbb{Q}(\sqrt2)=\{a+b\sqrt2\mid a,b\in\mathbb{Q}\}$ is also a number field; more examples appear in [Chapter 9](/2.1.9). Gaussian elimination uses only the four arithmetic operations, so a linear system over a number field $\mathbb{F}$ that has a solution has a solution in $\mathbb{F}$; likewise the rank, invertibility and so on of a matrix do not change when $\mathbb{F}$ is regarded as a subfield of a larger number field.

**Definition 8.1.2 (Vector Space)** Let $V$ be a nonempty set and $\mathbb{F}$ a number field. Suppose $V$ carries an addition (to any $a,b\in V$ corresponds a unique element $a+b$ of $V$) and a scalar multiplication (to any $a\in V$ and $k\in \mathbb{F}$ corresponds a unique element $ka$ of $V$) such that for all $a,b,c\in V$ and $k,\ell\in \mathbb{F}$ the following eight axioms hold. Then $V$ is called a **vector space** (or linear space) over $\mathbb{F}$, and its elements are called vectors:

1. associativity of addition: $(a+b)+c=a+(b+c)$;
2. commutativity of addition: $a+b=b+a$;
3. zero: there is $0\in V$ with $a+0=a$ for every $a$; $0$ is called the zero vector;
4. negatives: for every $a$ there is $b\in V$ with $a+b=0$; $b$ is called the negative of $a$ and written $-a$;
5. unit scalar: $1a=a$;
6. associativity of scalar multiplication: $(k\ell)a=k(\ell a)$;
7. distributivity over scalar addition: $(k+\ell)a=ka+\ell a$;
8. distributivity over vector addition: $k(a+b)=ka+kb$.

In the language of algebraic systems, the first four axioms say that $(V,+)$ is an abelian group. Subtraction is defined by $a-b=a+(-b)$.

**Proposition 8.1.1** In a vector space:

1. the zero vector is unique;
2. the negative of each vector is unique;
3. cancellation: $a+b=a+c$ implies $b=c$;
4. transposition: $a+b=c$ implies $a=c-b$;
5. $0a=0$, $(-1)a=-a$, $k0=0$;
6. cancelling a scalar: $ka=b$ with $k\neq0$ implies $a=\frac1kb$.

**Proof** 1: if $0,\tilde{0}$ are both zero vectors, then $\tilde{0}=\tilde{0}+0=0$. 2: if $b,c$ are both negatives of $a$, then $b=b+(a+c)=(b+a)+c=c$. 3, 4: add $-a$ or $-b$ to both sides. 5: $0a=(0+0)a=0a+0a$, so $0a=0$ by cancellation; $(-1)a+a=0a=0$, so $(-1)a=-a$; $k0+ka=k(0+a)=ka$, so $k0=0$ by cancellation. 6: $a=(\frac1kk)a=\frac1k(ka)=\frac1kb$. $\square$

Common vector spaces (with the usual addition and scalar multiplication):

| Space | Elements | Remarks |
|---|---|---|
| $\mathbb{F}^m$ | ordered $m$-tuples of numbers | space of arrays; operations as in $\mathbb{R}^m$ |
| $\mathbb{F}^{m\times n}$ | $m\times n$ matrices | matrix space |
| function space | real-valued functions on a domain $D$ | $(f+g)(x)=f(x)+g(x)$, $(kf)(x)=kf(x)$ |
| $C(D)$ | continuous functions on $D$ | a subspace of the function space |
| $C^\infty(D)$ | infinitely differentiable (smooth) functions on $D$ | a subspace of $C(D)$ |
| $\mathbb{F}[x]$ | polynomials with coefficients in $\mathbb{F}$ (including the zero polynomial) | polynomial space; as a ring, the **polynomial ring** |
| $\mathbb{F}[x]_n$ | polynomials of degree less than $n$ (including the zero polynomial) | a subspace of $\mathbb{F}[x]$ |
| $\mathbb{C}$ | complex numbers | a vector space both over $\mathbb{C}$ and over $\mathbb{R}$ |
| $\mathbb{R}$ | real numbers | a vector space both over $\mathbb{R}$ and over $\mathbb{Q}$ |
| $\operatorname{Hom}(U,V)$ | linear maps from $U$ to $V$ | see §8.4 |

The last rows show that the same set gives different vector spaces over different number fields, possibly of different dimensions (§8.3).

## 8.2. Intersections, Sums and Direct Sums of Subspaces

**Definition 8.2.1 (Subspace)** Let $V$ be a vector space over a number field $\mathbb{F}$ and $M$ a nonempty subset of $V$. If $M$ is itself a vector space under the addition and scalar multiplication of $V$, then $M$ is called a (linear) **subspace** of $V$.

**Proposition 8.2.1** A nonempty subset $M$ of a vector space $V$ is a subspace if and only if $M$ is closed under addition and scalar multiplication.

**Proof** Necessity is clear. Sufficiency: of the eight axioms, all except those for the zero and negatives hold for all elements of $V$ and hence for those of $M$; and for any $a\in M$ we have $0=0a\in M$ and $-a=(-1)a\in M$. $\square$

For example, the column space $\mathcal{R}(A)$ of a matrix $A\in \mathbb{F}^{m\times n}$ is a subspace of $\mathbb{F}^m$ and the null space $\mathcal{N}(A)$ is a subspace of $\mathbb{F}^n$; the upper triangular matrices of order $n$ and the symmetric matrices of order $n$ each form a subspace of $\mathbb{F}^{n\times n}$; and $\mathbb{F}[x]_n$ is a subspace of $\mathbb{F}[x]$.

**Definition 8.2.2 (Intersection and Sum of Subspaces)** Let $M_1,M_2$ be subspaces of a vector space $V$. The set $M_1\cap M_2=\{x\mid x\in M_1,\ x\in M_2\}$ is called the intersection of $M_1$ and $M_2$, and the set $M_1+M_2=\{m_1+m_2\mid m_1\in M_1,\ m_2\in M_2\}$ is called the sum of $M_1$ and $M_2$, the **sum of subspaces**.

By Proposition 8.2.1 one easily checks that $M_1\cap M_2$ and $M_1+M_2$ are subspaces, and that $M_1+M_2$ is the smallest subspace containing both $M_1$ and $M_2$. The union $M_1\cup M_2$ is in general not a subspace: the union of two distinct lines through the origin in $\mathbb{R}^2$ is not closed under addition. In matrix terms, for $A\in \mathbb{F}^{m\times n}$, $B\in \mathbb{F}^{m\times p}$ and $C\in \mathbb{F}^{q\times n}$,

$$
\mathcal{R}(A)+\mathcal{R}(B)=\mathcal{R}\big([A\ B]\big),\qquad \mathcal{N}(A)\cap\mathcal{N}(C)=\mathcal{N}\left(\begin{bmatrix}A\\C\end{bmatrix}\right).
$$

**Definition 8.2.3 (Direct Sum)** Let $M_1,M_2$ be subspaces of a vector space $V$ and $M=M_1+M_2$. If every vector $m\in M$ has a unique decomposition $m=m_1+m_2$ with $m_1\in M_1$ and $m_2\in M_2$, then $M$ is called the **direct sum** of $M_1$ and $M_2$, written $M=M_1\oplus M_2$.

**Theorem 8.2.1** For two subspaces $M_1,M_2$ of a vector space $V$ the following are equivalent:

1. $M_1+M_2$ is a direct sum;
2. the zero vector decomposes uniquely: $0=m_1+m_2$ with $m_i\in M_i$ implies $m_1=m_2=0$;
3. $M_1\cap M_2=\{0\}$.

**Proof** (cyclic) $1\Rightarrow2$: clear. $2\Rightarrow3$: for $m\in M_1\cap M_2$, $0=m+(-m)$ with $m\in M_1$ and $-m\in M_2$, so $m=0$. $3\Rightarrow1$: if $m=m_1+m_2=m_1'+m_2'$, then $m_1-m_1'=m_2'-m_2\in M_1\cap M_2=\{0\}$. $\square$

**Example 8.2.1** Let $\mathcal{U},\mathcal{L}$ be the sets of upper and lower triangular matrices of order $n$, let $\mathcal{S}$ consist of every **symmetric matrix** of order $n$, and let $\mathcal{K}$ consist of every **skew-symmetric matrix** of order $n$; all are subspaces of $\mathbb{F}^{n\times n}$. $\mathcal{U}\cap\mathcal{L}$ consists of the diagonal matrices, and $\mathcal{U}+\mathcal{L}=\mathbb{F}^{n\times n}$, but this sum is not direct. Every square matrix decomposes uniquely as $A=\frac12(A+A^{\mathsf T})+\frac12(A-A^{\mathsf T})$, and $\mathcal{S}\cap\mathcal{K}=\{O\}$, so $\mathbb{F}^{n\times n}=\mathcal{S}\oplus\mathcal{K}$.

The decomposition $\mathbb{R}^n=M\oplus M^\perp$ of [Chapter 4](/2.1.4) is another example of a direct sum. Direct sums of several subspaces and decompositions of a space under a linear transformation are treated in [Chapter 10](/2.1.10).

## 8.3. Linear Dependence, Bases and Dimension

### 8.3.1. Linear Combinations and Linear Dependence

**Definition 8.3.1 (Linear Representation)** Let $V$ be a vector space over a number field $\mathbb{F}$, $a_1,\dots,a_n\in V$ and $k_1,\dots,k_n\in \mathbb{F}$. The vector $k_1a_1+\cdots+k_na_n$ is called a **linear combination** of $a_1,\dots,a_n$. If a vector $b$ equals some linear combination of $a_1,\dots,a_n$, we say that $b$ can be linearly represented by $a_1,\dots,a_n$; if every vector of a list $b_1,\dots,b_m$ can be linearly represented by $a_1,\dots,a_n$, we say that the former list can be linearly represented by the latter; two lists that can be linearly represented by each other are called linearly equivalent.

Imitating the product of a matrix and a vector, we introduce the formal notation

$$
k_1a_1+\cdots+k_na_n=(a_1,\dots,a_n)\begin{bmatrix}k_1\\\vdots\\k_n\end{bmatrix},\qquad (b_1,\dots,b_m)=(a_1,\dots,a_n)\begin{bmatrix}k_{11}&\cdots&k_{1m}\\\vdots&&\vdots\\k_{n1}&\cdots&k_{nm}\end{bmatrix}.
$$

Here $(a_1,\dots,a_n)$ is not a genuine matrix (the $a_i$ may be polynomials or functions), but it obeys the distributive and associative laws with respect to matrix multiplication, $(a_1,\dots,a_n)(K\boldsymbol{x})=\big((a_1,\dots,a_n)K\big)\boldsymbol{x}$ and $(a_1,\dots,a_n)(KL)=\big((a_1,\dots,a_n)K\big)L$, as one verifies by expanding. All computations in this chapter use this notation.

**Definition 8.3.2 (Span and Linear Dependence)** The set of all linear combinations of a list $a_1,\dots,a_n$ is a subspace of $V$, called the subspace **spanned** by the list and written $\operatorname{span}(a_1,\dots,a_n)$. If there are $k_1,\dots,k_n\in \mathbb{F}$, not all zero, with $k_1a_1+\cdots+k_na_n=0$, the list is called **linearly dependent**; if $k_1a_1+\cdots+k_na_n=0$ implies $k_1=\cdots=k_n=0$, the list is called **linearly independent**.

In the formal notation, linear independence means $(a_1,\dots,a_n)\boldsymbol{k}=0\Rightarrow\boldsymbol{k}=\boldsymbol{0}$. Consequently, if a list is linearly independent, every vector it represents is represented in only one way.

**Proposition 8.3.1** Let $a_1,\dots,a_s$ be linearly independent. Then for any vector $b$, the list $a_1,\dots,a_s,b$ is linearly dependent if and only if $b$ can be linearly represented by $a_1,\dots,a_s$.

**Proof** Sufficiency is clear. Necessity: let $k_1a_1+\cdots+k_sa_s+kb=0$ with coefficients not all zero. If $k=0$, this contradicts the independence of the $a_i$; so $k\neq0$ and $b=-\frac1k(k_1a_1+\cdots+k_sa_s)$. $\square$

Accordingly, starting from the first nonzero vector of a list and checking each subsequent vector in turn, keeping it if it cannot be represented by the vectors already kept, this sifting procedure produces a linearly independent sublist that represents the whole list.

**Lemma 8.3.1** If the list $b_1,\dots,b_t$ can be linearly represented by $a_1,\dots,a_s$ and $t>s$, then $b_1,\dots,b_t$ is linearly dependent.

**Proof** Write $(b_1,\dots,b_t)=(a_1,\dots,a_s)K$ with $K$ an $s\times t$ matrix. The homogeneous system $K\boldsymbol{k}=\boldsymbol{0}$ has fewer equations than unknowns and so a nonzero solution $\boldsymbol{k}$, and then $(b_1,\dots,b_t)\boldsymbol{k}=(a_1,\dots,a_s)(K\boldsymbol{k})=0$. $\square$

Lemma 8.3.1 reduces a question about a general vector space to a homogeneous linear system over the number field, a technique used again and again in this chapter. It immediately implies that two linearly equivalent lists that are each linearly independent have the same number of vectors.

**Definition 8.3.3 (Maximal Linearly Independent Subset and Rank)** A sublist $a_{i_1},\dots,a_{i_r}$ of a list $S:a_1,\dots,a_s$ is called a **maximal linearly independent subset** of $S$ if it is linearly independent and $S$ can be linearly represented by it. Any two maximal linearly independent subsets of $S$ are linearly equivalent and hence contain the same number of vectors; this number is called the **rank** of the list $S$, written $\operatorname{rank}(S)$. A list consisting only of zero vectors has rank zero by convention.

### 8.3.2. Bases and Dimension

**Definition 8.3.4 (Basis and Dimension)** Let $V$ be a vector space over a number field $\mathbb{F}$. A linearly independent list in $V$ by which every vector of $V$ can be linearly represented is called a **basis** of $V$. If a basis of $V$ contains $n$ vectors, $V$ is called an $n$-dimensional vector space and its **dimension** is $n$, written $\dim V=n$. If $V$ contains arbitrarily many linearly independent vectors, $V$ is called infinite-dimensional; otherwise $V$ is a **finite-dimensional vector space**. The zero space $\{0\}$ has dimension $0$ by convention.

By Lemma 8.3.1, any two bases of a finite-dimensional space contain the same number of vectors, so the dimension is well defined; when the field needs emphasis we write $\dim_{\mathbb{F}}V$.

**Proposition 8.3.2 (Criterion for a Basis)** Let $\dim V=n$ and $a_1,\dots,a_n\in V$. If $a_1,\dots,a_n$ is linearly independent, or if $V=\operatorname{span}(a_1,\dots,a_n)$, then it is a basis of $V$.

**Proof** Suppose the list is linearly independent. For any $b\in V$, the $n+1$ vectors $a_1,\dots,a_n,b$ can be represented by a basis of $V$ ($n$ vectors), so by Lemma 8.3.1 they are linearly dependent, and by Proposition 8.3.1 $b$ is represented by the $a_i$. Suppose the list spans $V$. Its maximal linearly independent subset is a basis of $V$, and by the uniqueness of dimension it consists of all $n$ vectors. $\square$

**Theorem 8.3.1 (Basis Extension Theorem)** In a finite-dimensional vector space $V$, any $r$ linearly independent vectors can be extended to a basis of $V$. Consequently, any basis of a subspace $M$ of a finite-dimensional space $V$ can be extended to a basis of $V$; $\dim M\le\dim V$, with equality if and only if $M=V$.

**Proof** If $a_1,\dots,a_r$ is not a basis, some $b\in V$ cannot be represented by these vectors, and by Proposition 8.3.1 $a_1,\dots,a_r,b$ is linearly independent. Repeat this step; since a linearly independent list in $V$ has at most $\dim V$ vectors, the process stops after finitely many steps. $\square$

**Theorem 8.3.2 (Dimension Formula)** Let $M_1,M_2$ be subspaces of a finite-dimensional vector space $V$. Then

$$
\dim(M_1+M_2)=\dim M_1+\dim M_2-\dim(M_1\cap M_2).
$$

**Proof** Take a basis $a_1,\dots,a_r$ of $M_1\cap M_2$ and extend it to a basis $a_1,\dots,a_r,b_1,\dots,b_s$ of $M_1$ and to a basis $a_1,\dots,a_r,c_1,\dots,c_t$ of $M_2$. It suffices to show that these $r+s+t$ vectors form a basis of $M_1+M_2$. They clearly span $M_1+M_2$. If $\sum k_ia_i+\sum\ell_jb_j+\sum m_lc_l=0$, then $v=-\sum m_lc_l=\sum k_ia_i+\sum\ell_jb_j\in M_1\cap M_2$, so $v$ is a linear combination of $a_1,\dots,a_r$; the independence of the $a_i,c_l$ gives $m_l=0$ and $v=0$, and then the independence of the $a_i,b_j$ shows that the remaining coefficients vanish. $\square$

**Corollary 8.3.1** Let $M_1,M_2$ be finite-dimensional subspaces. Then $M_1+M_2$ is a direct sum if and only if $\dim(M_1+M_2)=\dim M_1+\dim M_2$; in that case the union of bases of $M_1$ and $M_2$ is a basis of $M_1\oplus M_2$.

The dimension formula has the same form as the inclusion–exclusion principle for sets, but it holds only for two subspaces: the analogous formula for three subspaces is false in general (three distinct lines in $\mathbb{R}^2$).

### 8.3.3. Examples

**Example 8.3.1** The choice of number field affects the dimension:

- $\mathbb{R}$ as a vector space over $\mathbb{R}$ has any nonzero real number as a basis and dimension $1$; as a vector space over $\mathbb{Q}$, the numbers $1,\pi,\dots,\pi^n$ are linearly independent for every $n$ ($\pi$ is transcendental, i.e., not a root of any nonzero polynomial with rational coefficients), so it is infinite-dimensional.
- $\mathbb{C}$ as a vector space over $\mathbb{R}$ has the basis $1,\mathrm{i}$, so $\dim_{\mathbb{R}}\mathbb{C}=2$; as a vector space over $\mathbb{C}$, $\dim_{\mathbb{C}}\mathbb{C}=1$.

**Example 8.3.2** Spaces of arrays and matrices: $\boldsymbol{e}_1,\dots,\boldsymbol{e}_m$ is a basis of $\mathbb{F}^m$, and $\dim \mathbb{F}^m=m$. Let $E_{ij}$ be the $m\times n$ matrix with $(i,j)$ entry $1$ and all other entries $0$; then $\{E_{ij}\}$ is a basis of $\mathbb{F}^{m\times n}$, and $\dim \mathbb{F}^{m\times n}=mn$. In Example 8.2.1, $\dim\mathcal{U}=\dim\mathcal{L}=\dim\mathcal{S}=\frac{n(n+1)}2$, $\dim\mathcal{K}=\frac{n(n-1)}2$ and $\dim(\mathcal{U}\cap\mathcal{L})=n$, consistent with the dimension formula: $\dim(\mathcal{U}+\mathcal{L})=n(n+1)-n=n^2$ and $\dim\mathcal{S}+\dim\mathcal{K}=n^2$.

**Example 8.3.3** In $\mathbb{F}[x]_n$, the polynomials $1,x,\dots,x^{n-1}$ are linearly independent. Suppose $k_0+k_1x+\cdots+k_{n-1}x^{n-1}=0$ (the zero polynomial on the right, i.e., the function is identically zero). Substituting $n$ distinct numbers $\lambda_1,\dots,\lambda_n$ gives the homogeneous system

$$
\begin{bmatrix}1&\lambda_1&\cdots&\lambda_1^{n-1}\\\vdots&\vdots&&\vdots\\1&\lambda_n&\cdots&\lambda_n^{n-1}\end{bmatrix}\begin{bmatrix}k_0\\\vdots\\k_{n-1}\end{bmatrix}=\boldsymbol{0},
$$

whose coefficient matrix is a **Vandermonde matrix** and hence invertible, so all $k_i$ vanish. Therefore $1,x,\dots,x^{n-1}$ is a basis of $\mathbb{F}[x]_n$ and $\dim \mathbb{F}[x]_n=n$; since $n$ is arbitrary, $\mathbb{F}[x]$, $C^\infty(D)$, $C(D)$ and the function space are all infinite-dimensional.

**Example 8.3.4** In $C^\infty(\mathbb{R})$, for distinct real numbers $\lambda_1,\lambda_2$, the functions $\mathrm{e}^{\lambda_1x},\mathrm{e}^{\lambda_2x}$ are linearly independent. Suppose $k_1\mathrm{e}^{\lambda_1x}+k_2\mathrm{e}^{\lambda_2x}=0$ (the zero function). Differentiating gives $k_1\lambda_1\mathrm{e}^{\lambda_1x}+k_2\lambda_2\mathrm{e}^{\lambda_2x}=0$, that is,

$$
\begin{bmatrix}\mathrm{e}^{\lambda_1x}&\mathrm{e}^{\lambda_2x}\\\lambda_1\mathrm{e}^{\lambda_1x}&\lambda_2\mathrm{e}^{\lambda_2x}\end{bmatrix}\begin{bmatrix}k_1\\k_2\end{bmatrix}=\boldsymbol{0},
$$

and the **determinant** of the coefficient matrix, $\mathrm{e}^{(\lambda_1+\lambda_2)x}(\lambda_2-\lambda_1)$, is nonzero, so $k_1=k_2=0$. For distinct real numbers $\lambda_1,\dots,\lambda_n$, differentiating $n-1$ times yields a coefficient determinant equal to $\mathrm{e}^{(\lambda_1+\cdots+\lambda_n)x}$ times a Vandermonde determinant, so in the same way $\mathrm{e}^{\lambda_1x},\dots,\mathrm{e}^{\lambda_nx}$ are linearly independent. This method (the Wronskian matrix) is used in [Chapter 11](/2.1.11) to test linear dependence of vector-valued functions.

## 8.4. Linear Maps

**Definition 8.4.1 (Linear Map)** Let $U,V$ be vector spaces over a number field $\mathbb{F}$. A map $f\colon U\to V$ that preserves addition and scalar multiplication, that is,

1. additivity: $f(a+b)=f(a)+f(b)$ for all $a,b\in U$;
2. homogeneity: $f(ka)=kf(a)$ for all $a\in U$ and $k\in \mathbb{F}$,

is called a **linear map** from $U$ to $V$, also called a homomorphism. The set of all linear maps from $U$ to $V$ is written $\operatorname{Hom}(U,V)$.

Linear maps are exactly the **homomorphisms** between vector spaces viewed as algebraic systems. Every $f\in\operatorname{Hom}(U,V)$ satisfies $f(0_U)=0_V$; a **function** $f\colon U\to V$ is a linear map if and only if $f(ka+\ell b)=kf(a)+\ell f(b)$ for all $a,b\in U$ and $k,\ell\in \mathbb{F}$.

**Definition 8.4.2 (Operations on Linear Maps)** For $f,g\in\operatorname{Hom}(U,V)$ and $k\in \mathbb{F}$, define $f+g\colon x\mapsto f(x)+g(x)$ and $kf\colon x\mapsto kf(x)$. For $f\in\operatorname{Hom}(U,V)$ and $g\in\operatorname{Hom}(V,W)$, define the composition $g\circ f\colon U\to W$, $x\mapsto g(f(x))$, also called the product of $g$ and $f$ and written $gf$.

$f+g$, $kf$ and $gf$ are again linear maps, and $\operatorname{Hom}(U,V)$ is a vector space under addition and scalar multiplication (its zero is the zero map). Composition is associative and distributes over addition, but is not commutative in general.

**Definition 8.4.3 (Kernel and Image)** For $f\in\operatorname{Hom}(U,V)$, the set $\mathcal{N}(f)=\{a\in U\mid f(a)=0\}$ is called the **kernel** of $f$, and the set $\mathcal{R}(f)=\{f(a)\mid a\in U\}$ the image of $f$.

**Proposition 8.4.1** Let $f\in\operatorname{Hom}(U,V)$. Then $\mathcal{N}(f)$ is a subspace of $U$ and $\mathcal{R}(f)$ is a subspace of $V$; $f$ is an **injection** if and only if $\mathcal{N}(f)=\{0\}$, and a **surjection** if and only if $\mathcal{R}(f)=V$.

**Proof** The subspace properties follow directly from linearity. If $f$ is injective, $f(a)=0=f(0)$ implies $a=0$; conversely, if $\mathcal{N}(f)=\{0\}$, then $f(a)=f(b)$ gives $f(a-b)=0$, so $a=b$. The characterization of surjectivity is the definition. $\square$

**Definition 8.4.4 (Eigenvalues of a Linear Transformation)** A linear map from a vector space $U$ to itself is called a **linear transformation** of $U$. Let $f\in\operatorname{Hom}(U,U)$. If $\lambda\in \mathbb{F}$ and a nonzero vector $x\in U$ satisfy $f(x)=\lambda x$, then $\lambda$ is called an **eigenvalue** of $f$, $x$ an **eigenvector** of $f$ belonging to $\lambda$, and $(\lambda,x)$ an eigenpair of $f$; the kernel $\mathcal{N}(\lambda\,\mathrm{id}-f)$ is called the **eigenspace** of $f$ belonging to $\lambda$, where $\mathrm{id}$ is the **identity map**.

**Proposition 8.4.2** Eigenvectors of a linear transformation belonging to distinct eigenvalues are linearly independent.

**Proof** Let $x_1,\dots,x_k$ belong to the distinct eigenvalues $\lambda_1,\dots,\lambda_k$; we use induction on $k$. Suppose $c_1x_1+\cdots+c_kx_k=0$. Applying $f$ to both sides and subtracting $\lambda_k$ times the original equation gives $c_1(\lambda_1-\lambda_k)x_1+\cdots+c_{k-1}(\lambda_{k-1}-\lambda_k)x_{k-1}=0$. By the induction hypothesis $c_i(\lambda_i-\lambda_k)=0$, so $c_1=\cdots=c_{k-1}=0$, and then $x_k\neq 0$ gives $c_k=0$. $\square$

**Example 8.4.1 (Examples of Linear Maps)**

- For $A\in \mathbb{F}^{m\times n}$, left multiplication $L_A\colon \mathbb{F}^{n\times p}\to \mathbb{F}^{m\times p}$, $X\mapsto AX$, and right multiplication $R_A\colon \mathbb{F}^{\ell\times m}\to \mathbb{F}^{\ell\times n}$, $X\mapsto XA$, are linear maps.
- The **transpose** $\mathbb{F}^{m\times n}\to \mathbb{F}^{n\times m}$, $A\mapsto A^{\mathsf T}$, and the **trace** $\mathbb{F}^{n\times n}\to \mathbb{F}$, $A\mapsto\operatorname{tr}(A)$, are linear maps.
- Evaluation at $n$ distinct points, $C(\mathbb{R})\to\mathbb{R}^n$, $f\mapsto[f(x_i)]$, is a linear map; the interpolation problem asks whether its restriction to $\mathbb{R}[x]_n$ is bijective (Example 8.3.3 shows that it is).
- Symmetrization $S\colon \mathbb{F}^{n\times n}\to \mathbb{F}^{n\times n}$, $A\mapsto\frac12(A+A^{\mathsf T})$, is a linear transformation; $\mathcal{N}(S)$ and $\mathcal{R}(S)$ are the subspaces of skew-symmetric and symmetric matrices respectively. Since $S^2=S$, its eigenvalues satisfy $\lambda^2=\lambda$ and can only be $1,0$, with eigenspaces $\mathcal{N}(\mathrm{id}-S)=\mathcal{R}(S)$ and $\mathcal{N}(S)$.
- On $C^\infty(\mathbb{R})$, the differentiation operator $D=\frac{\mathrm{d}}{\mathrm{d}x}$ is a linear transformation, and $\mathcal{N}(D)$ is the subspace of constant functions. From $(\lambda\,\mathrm{id}-D)f=0$, i.e., $f'=\lambda f$, we get $f=k\mathrm{e}^{\lambda x}$; so every real number $\lambda$ is an eigenvalue of $D$, with eigenvector $\mathrm{e}^{\lambda x}$. Together with Proposition 8.4.2, this gives another proof of Example 8.3.4.
- $V=\left\{\begin{bmatrix}a&-b\\b&a\end{bmatrix}\,\middle|\,a,b\in\mathbb{R}\right\}$ is a subspace of $\mathbb{R}^{2\times2}$, and $\mathbb{C}\to V$, $a+b\mathrm{i}\mapsto\begin{bmatrix}a&-b\\b&a\end{bmatrix}$, is a bijective linear map between vector spaces over $\mathbb{R}$ that also preserves multiplication ([Chapter 9](/2.1.9)).
- For an invertible matrix $T\in \mathbb{F}^{n\times n}$, $\boldsymbol{x}\mapsto T\boldsymbol{x}$ is an invertible linear transformation of $\mathbb{F}^n$.

## 8.5. Isomorphisms and Coordinates

**Definition 8.5.1 (Isomorphism)** Let $U,V$ be vector spaces over a number field $\mathbb{F}$. If there is a bijective $f\in\operatorname{Hom}(U,V)$, then $U$ and $V$ are said to be (linearly) isomorphic, and $f$ is called an **isomorphism** from $U$ to $V$. An isomorphism from $U$ to itself is called an **automorphism** of $U$.

**Proposition 8.5.1** If $f\colon U\to V$ and $g\colon V\to W$ are isomorphisms, then so are $gf\colon U\to W$ and $f^{-1}\colon V\to U$. Hence isomorphism of vector spaces is an **equivalence relation**.

**Proof** $gf$ is a linear bijection. $f^{-1}$ is a bijection, and we need only check that it is linear: for $x_1,x_2\in V$, let $a_i=f^{-1}(x_i)$; from $f(k_1a_1+k_2a_2)=k_1x_1+k_2x_2$ we get $f^{-1}(k_1x_1+k_2x_2)=k_1f^{-1}(x_1)+k_2f^{-1}(x_2)$. Reflexivity of the isomorphism relation comes from the identity map, and symmetry and transitivity from the two facts above. $\square$

The automorphisms of $\mathbb{F}^n$ given by invertible matrices of order $n$ form, under composition, the **general linear group**. Since isomorphism is an equivalence relation, we ask for its invariants and canonical forms. Coordinates provide the answer.

**Definition 8.5.2 (Coordinates)** Let $e_1,\dots,e_n$ be a basis of an $n$-dimensional vector space $V$. Every $x\in V$ can be written uniquely as $x=x_1e_1+\cdots+x_ne_n=(e_1,\dots,e_n)\hat{\boldsymbol{x}}$; the ordered array $\hat{\boldsymbol{x}}=[x_1\ \cdots\ x_n]^{\mathsf T}\in \mathbb{F}^n$ is called the **coordinate vector** of $x$ with respect to this basis.

Coordinates depend on the order of the basis vectors: swapping two basis vectors swaps the corresponding coordinates. This gives the coordinate map

$$
\sigma_{e_1,\dots,e_n}\colon V\to \mathbb{F}^n,\quad x\mapsto\hat{\boldsymbol{x}},\qquad \sigma^{-1}_{e_1,\dots,e_n}\colon \mathbb{F}^n\to V,\quad\hat{\boldsymbol{x}}\mapsto(e_1,\dots,e_n)\hat{\boldsymbol{x}}.
$$

**Theorem 8.5.1** The coordinate map $\sigma_{e_1,\dots,e_n}\colon V\to \mathbb{F}^n$ is an isomorphism. Consequently, two finite-dimensional vector spaces over a number field $\mathbb{F}$ are isomorphic if and only if they have the same dimension: dimension is a complete invariant of isomorphism, and $\mathbb{F}^n$ is the canonical form of $n$-dimensional spaces.

**Proof** $\sigma$ is a bijection, and $kx+\ell y=(e_1,\dots,e_n)(k\hat{\boldsymbol{x}}+\ell\hat{\boldsymbol{y}})$ gives $\sigma(kx+\ell y)=k\sigma(x)+\ell\sigma(y)$. So every $n$-dimensional space is isomorphic to $\mathbb{F}^n$, and hence any two are isomorphic. Conversely, if $f\colon U\to V$ is an isomorphism and $e_1,\dots,e_n$ is a basis of $U$, then $f(e_1),\dots,f(e_n)$ is linearly independent ($f$ is injective) and spans $V$ ($f$ is surjective), so it is a basis of $V$ and $\dim V=n$. $\square$

An isomorphism preserves linear operations and therefore every property expressed solely in terms of linear operations. In particular:

**Corollary 8.5.1** Fix a basis of an $n$-dimensional vector space $V$ and let $a_1,\dots,a_m$ have coordinate vectors $\hat{\boldsymbol{a}}_1,\dots,\hat{\boldsymbol{a}}_m$. Then $a_1,\dots,a_m$ is linearly independent in $V$ if and only if $\hat{\boldsymbol{a}}_1,\dots,\hat{\boldsymbol{a}}_m$ is linearly independent in $\mathbb{F}^n$; more generally, the **rank** of the list equals the rank of the coordinate matrix $[\hat{\boldsymbol{a}}_1\ \cdots\ \hat{\boldsymbol{a}}_m]$.

This is "standardized solving" in abstract spaces: deciding linear dependence of polynomials, matrices or functions, or finding a maximal linearly independent subset, reduces to Gaussian elimination on the coordinate matrix. For example, the coordinate matrix of $1+x,\ x+x^2,\ 1-x^2$ with respect to the basis $1,x,x^2$, namely $\begin{bmatrix}1&0&1\\1&1&0\\0&1&-1\end{bmatrix}$, has rank $2$ (the third column is the first minus the second), so these polynomials are linearly dependent, with $1-x^2=(1+x)-(x+x^2)$.

### 8.5.1. Change of Basis and Change of Coordinates

Coordinates depend on the choice of basis. Let $e_1,\dots,e_n$ and $t_1,\dots,t_n$ be two bases of $V$; each $t_j$ can be linearly represented by $e_1,\dots,e_n$:

$$
(t_1,\dots,t_n)=(e_1,\dots,e_n)T,\qquad T=\begin{bmatrix}t_{11}&\cdots&t_{1n}\\\vdots&&\vdots\\t_{n1}&\cdots&t_{nn}\end{bmatrix}.
$$

This is the change-of-basis formula, and $T$ is called the *change-of-basis matrix* from the basis $e_1,\dots,e_n$ to the basis $t_1,\dots,t_n$; its $j$-th column is the coordinate vector of $t_j$ with respect to the old basis. If $a\in V$ has coordinate vectors $\boldsymbol{x}$ and $\boldsymbol{y}$ with respect to the two bases, then

$$
a=(e_1,\dots,e_n)\boldsymbol{x}=(t_1,\dots,t_n)\boldsymbol{y}=(e_1,\dots,e_n)(T\boldsymbol{y}),
$$

and the uniqueness of coordinates gives the change-of-coordinates formula $\boldsymbol{x}=T\boldsymbol{y}$, $\boldsymbol{y}=T^{-1}\boldsymbol{x}$. Note the directions: the basis changes by $T$, the coordinates by $T^{-1}$. For example, in $\mathbb{R}^2$ take $\boldsymbol{t}_1=2\boldsymbol{e}_1+\boldsymbol{e}_2$ and $\boldsymbol{t}_2=\boldsymbol{e}_1+2\boldsymbol{e}_2$, i.e., $T=\begin{bmatrix}2&1\\1&2\end{bmatrix}$; the vector $\boldsymbol{a}=[4\ 5]^{\mathsf T}$ has coordinate vector $\boldsymbol{y}=T^{-1}\boldsymbol{a}=[1\ 2]^{\mathsf T}$ with respect to the new basis, that is, $\boldsymbol{a}=\boldsymbol{t}_1+2\boldsymbol{t}_2$.

![The coordinates of one vector a with respect to two bases: (4, 5) in the standard basis on the left and (1, 2) in the basis t_1, t_2 on the right; the grid lines are the coordinate lines of each system, and the dashed lines decompose a along the basis vectors](./plots/change-of-basis-coordinates.py)

**Proposition 8.5.2** Let $e_1,\dots,e_n$ be a basis of $V$, $T\in \mathbb{F}^{n\times n}$ and $(t_1,\dots,t_n)=(e_1,\dots,e_n)T$. Then $t_1,\dots,t_n$ is a basis of $V$ if and only if $T$ is invertible.

**Proof** By Corollary 8.5.1, the $t_j$ are linearly independent if and only if their coordinate vectors, the columns of $T$, are linearly independent, i.e., $T$ is invertible. $\square$

**Algorithm 8.5.1 (Change-of-Basis Matrices in $\mathbb{F}^n$)** Let two bases of $\mathbb{F}^n$ be arranged as the columns of invertible matrices $A$ and $B$. The change-of-basis matrix $T$ satisfies $B=AT$, that is, $T=A^{-1}B$. Apply **Gauss–Jordan elimination** to $[A\ B]$:

$$
[A\ \ B]\ \longrightarrow\ [I\ \ A^{-1}B]=[I\ \ T].
$$

If the two bases span the same $m$-dimensional subspace of $\mathbb{F}^n$, so that $A,B$ are $n\times m$ matrices of full column rank, elimination gives $[A\ B]\to\begin{bmatrix}I_m&T\\O&O\end{bmatrix}$; in terms of the **Moore–Penrose pseudoinverse**, $T=A^+B=(A^{\mathsf T}A)^{-1}A^{\mathsf T}B$ (over the real field).

**Example 8.5.1** $\mathbb{F}^{2\times2}$ has the basis $E_{11},E_{12},E_{21},E_{22}$, in which $A=\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}$ has coordinate vector $\boldsymbol{a}=[a_{11}\ a_{12}\ a_{21}\ a_{22}]^{\mathsf T}$. Another basis $E_{11},E_{22},E_{12}+E_{21},E_{12}-E_{21}$ consists of symmetric and skew-symmetric matrices (the direct sum decomposition of Example 8.2.1); the change-of-basis matrix and the new coordinates are

$$
T=\begin{bmatrix}1&0&0&0\\0&0&1&1\\0&0&1&-1\\0&1&0&0\end{bmatrix},\qquad \tilde{\boldsymbol{a}}=\Big[a_{11}\ \ a_{22}\ \ \tfrac{a_{12}+a_{21}}2\ \ \tfrac{a_{12}-a_{21}}2\Big]^{\mathsf T},
$$

and one checks that $\boldsymbol{a}=T\tilde{\boldsymbol{a}}$.

**Example 8.5.2** $\mathbb{R}[x]_n$ has the bases $1,x,\dots,x^{n-1}$ and $1,x-x_0,\dots,(x-x_0)^{n-1}$. For $f=a_0+a_1x+\cdots+a_{n-1}x^{n-1}$, Taylor expansion shows that the coordinate vector of $f$ with respect to the latter basis is $\tilde{\boldsymbol{f}}=\Big[f(x_0)\ \ f'(x_0)\ \ \cdots\ \ \frac{f^{(n-1)}(x_0)}{(n-1)!}\Big]^{\mathsf T}$. By the binomial expansion $(x-x_0)^k=\sum_{i=0}^k\binom ki(-x_0)^{k-i}x^i$, the change-of-basis matrix is the upper triangular matrix

$$
T=\begin{bmatrix}1&-x_0&x_0^2&\cdots&(-x_0)^{n-1}\\&1&-2x_0&\cdots&(n-1)(-x_0)^{n-2}\\&&\ddots&\ddots&\vdots\\&&&1&-(n-1)x_0\\&&&&1\end{bmatrix},
$$

whose $(i,k)$ entry (indexed from $0$) is $\binom ki(-x_0)^{k-i}$, and $[a_0\ \cdots\ a_{n-1}]^{\mathsf T}=T\tilde{\boldsymbol{f}}$.

Different bases of the same space have different strengths. The figure below shows three bases of $\mathbb{R}[x]_4$. The monomial basis is the most convenient for computation, but on $[0,1]$ the graphs of $x^2$ and $x^3$ differ little, so coefficients with respect to it are very sensitive to errors (the corresponding Vandermonde matrices are ill-conditioned). In the shifted basis $(x-x_0)^k$ the coordinates are the Taylor coefficients of $f$ at $x_0$ (Example 8.5.2). The Lagrange basis $L_0,\dots,L_3$ with nodes $0,\frac13,\frac23,1$ satisfies $L_i(a_j)=\delta_{ij}$, so the coordinates of a polynomial in this basis are its values at the four nodes (Theorem 9.4.2).

![Three bases of R[x]_4 on [0, 1]: the monomial basis 1, x, x^2, x^3; the shifted basis (x − 1/2)^k; and the Lagrange basis with nodes 0, 1/3, 2/3, 1, where L_i equals 1 at the i-th node (open circles) and 0 at the other nodes (filled circles)](./plots/polynomial-bases.py)

## 8.6. Matrix Representations of Linear Maps

**Proposition 8.6.1** Let $U,V$ be finite-dimensional vector spaces and $e_1,\dots,e_n$ a basis of $U$. Then:

1. every $f\in\operatorname{Hom}(U,V)$ is uniquely determined by the images $f(e_1),\dots,f(e_n)$ of the basis;
2. for any $n$ vectors $a_1,\dots,a_n$ in $V$ there is a unique $f\in\operatorname{Hom}(U,V)$ with $f(e_i)=a_i$.

**Proof** 1: if $f(e_i)=g(e_i)$, then for $a=\sum a_ie_i$ we have $f(a)=\sum a_if(e_i)=\sum a_ig(e_i)=g(a)$. 2: uniqueness follows from 1. Existence: define $f(x_1e_1+\cdots+x_ne_n)=x_1a_1+\cdots+x_na_n$; the uniqueness of coordinates makes $f$ a well-defined map, and the linearity of coordinates makes it linear. $\square$

Writing $f(e_1,\dots,e_n)=(f(e_1),\dots,f(e_n))$, the maps in $\operatorname{Hom}(U,V)$ correspond one-to-one to ordered lists of $n$ vectors in $V$. Choosing a basis of $V$ as well and writing these images in coordinates yields a matrix.

**Definition 8.6.1 (Matrix of a Linear Map)** Let $e_1,\dots,e_n$ and $\eta_1,\dots,\eta_m$ be bases of $U$ and $V$, $f\in\operatorname{Hom}(U,V)$, and $f(e_j)=f_{1j}\eta_1+\cdots+f_{mj}\eta_m$, that is,

$$
f(e_1,\dots,e_n)=(\eta_1,\dots,\eta_m)F,\qquad F=[f_{ij}]_{m\times n}.
$$

The $m\times n$ matrix $F$ is called the matrix of $f$ with respect to the bases $e_1,\dots,e_n;\eta_1,\dots,\eta_m$ (in general, the **matrix of a linear map** with respect to a pair of bases). The $j$-th column of $F$ is the coordinate vector of $f(e_j)$.

For $a=(e_1,\dots,e_n)\hat{\boldsymbol{a}}$, linearity gives $f(a)=(f(e_1),\dots,f(e_n))\hat{\boldsymbol{a}}=(\eta_1,\dots,\eta_m)(F\hat{\boldsymbol{a}})$, that is,

$$
\widehat{f(a)}=F\hat{\boldsymbol{a}}:
$$

in coordinates, a linear map is left multiplication by its matrix. Formally, $f((e_1,\dots,e_n)K)=\big(f(e_1,\dots,e_n)\big)K$ for every $n\times p$ matrix $K$. For a linear map $\mathbb{F}^n\to \mathbb{F}^m$ with the standard bases, the matrix is $[f(\boldsymbol{e}_1)\ \cdots\ f(\boldsymbol{e}_n)]$, which is exactly the definition of [Chapter 1](/2.1.1).

**Theorem 8.6.1** The map $\sigma=\sigma_{e_1,\dots,e_n;\eta_1,\dots,\eta_m}\colon \operatorname{Hom}(U,V)\to \mathbb{F}^{m\times n}$, $f\mapsto F$, is an isomorphism. In particular, $\dim\operatorname{Hom}(U,V)=mn$.

**Proof** $f$ corresponds one-to-one to the list $(f(e_1),\dots,f(e_n))$, and each $f(e_j)$ to its coordinate vector, so $\sigma$ is a bijection. For $\sigma(f)=F$ and $\sigma(g)=G$,

$$
(kf+\ell g)(e_1,\dots,e_n)=k(\eta_1,\dots,\eta_m)F+\ell(\eta_1,\dots,\eta_m)G=(\eta_1,\dots,\eta_m)(kF+\ell G),
$$

so $\sigma(kf+\ell g)=k\sigma(f)+\ell\sigma(g)$. $\square$

**Proposition 8.6.2** Let $U,V,W$ have bases $e_1,\dots,e_n$; $\eta_1,\dots,\eta_m$; $\zeta_1,\dots,\zeta_\ell$, and let $f\in\operatorname{Hom}(U,V)$, $g\in\operatorname{Hom}(V,W)$. Then $\sigma(gf)=\sigma(g)\sigma(f)$: the matrix of a composition is the product of the matrices.

**Proof** Let $f(e_1,\dots,e_n)=(\eta_1,\dots,\eta_m)F$ and $g(\eta_1,\dots,\eta_m)=(\zeta_1,\dots,\zeta_\ell)G$. Then

$$
(gf)(e_1,\dots,e_n)=g\big((\eta_1,\dots,\eta_m)F\big)=\big(g(\eta_1,\dots,\eta_m)\big)F=(\zeta_1,\dots,\zeta_\ell)(GF).\ \square
$$

So the isomorphism $\sigma$ preserves not only linear operations but also multiplication: the algebra of linear maps is identical to the algebra of matrices. This explains why matrix multiplication is defined the way it is, and shows that (when $\dim U=\dim V$) $f$ is invertible if and only if its matrix is, with $\sigma(f^{-1})=\sigma(f)^{-1}$.

**Proposition 8.6.3** Let $F$ be the matrix of $f\in\operatorname{Hom}(U,V)$ with respect to the bases $e_1,\dots,e_n;\eta_1,\dots,\eta_m$. Then the coordinate maps restrict to isomorphisms $\mathcal{N}(f)\to\mathcal{N}(F)$ and $\mathcal{R}(f)\to\mathcal{R}(F)$. Hence $\dim\mathcal{N}(f)=\dim\mathcal{N}(F)$, $\dim\mathcal{R}(f)=\operatorname{rank}(F)$, and

$$
\dim\mathcal{N}(f)+\dim\mathcal{R}(f)=\dim U.
$$

**Proof** By $\widehat{f(a)}=F\hat{\boldsymbol{a}}$, $a\in\mathcal{N}(f)$ if and only if $\hat{\boldsymbol{a}}\in\mathcal{N}(F)$; and $b\in\mathcal{R}(f)$ if and only if $\hat{\boldsymbol{b}}=F\hat{\boldsymbol{a}}$ for some $\hat{\boldsymbol{a}}$, i.e., $\hat{\boldsymbol{b}}\in\mathcal{R}(F)$. The last formula is the **rank–nullity theorem** $\dim\mathcal{N}(F)+\operatorname{rank}(F)=n$ for matrices. $\square$

$\dim\mathcal{R}(f)$ is called the rank of $f$; it does not depend on the choice of bases. Consequently, when $\dim U=\dim V<\infty$, a map $f\in\operatorname{Hom}(U,V)$ is injective ⇔ surjective ⇔ bijective; this fails in infinite dimensions, where for example differentiation on $\mathbb{R}[x]$ is surjective but not injective.

**Example 8.6.1** Let $A=[\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]\in \mathbb{F}^{m\times n}$ and $L_A\colon \mathbb{F}^{n\times2}\to \mathbb{F}^{m\times2}$, $X\mapsto AX$. Take the bases $E_{j1}=[\boldsymbol{e}_j\ \boldsymbol{0}]$, $E_{j2}=[\boldsymbol{0}\ \boldsymbol{e}_j]$ ($j=1,\dots,n$) and $F_{i1}=[\boldsymbol{e}_i\ \boldsymbol{0}]$, $F_{i2}=[\boldsymbol{0}\ \boldsymbol{e}_i]$ ($i=1,\dots,m$), each ordered with all first-column matrices before the second-column ones. Since $AE_{j1}=[\boldsymbol{a}_j\ \boldsymbol{0}]$ and $AE_{j2}=[\boldsymbol{0}\ \boldsymbol{a}_j]$, the matrix of $L_A$ is the block diagonal matrix $\begin{bmatrix}A&\\&A\end{bmatrix}$.

**Example 8.6.2** On $V=\operatorname{span}(1,\sin x,\cos x)\subseteq C^\infty(\mathbb{R})$, differentiation $D$ is a linear transformation:

$$
D(1,\sin x,\cos x)=(0,\cos x,-\sin x)=(1,\sin x,\cos x)\begin{bmatrix}0&0&0\\0&0&-1\\0&1&0\end{bmatrix}.
$$

With respect to the basis $1,x,\dots,x^{n-1}$ of $\mathbb{R}[x]_n$, the matrix of $D$ is the matrix of order $n$ with $1,2,\dots,n-1$ on the superdiagonal and zeros elsewhere.

## 8.7. Matrices Under Change of Basis: Equivalence and Similarity

### 8.7.1. Linear Maps: Equivalence

**Theorem 8.7.1** Let $U$ have two bases $e_1,\dots,e_n$ and $t_1,\dots,t_n$ with change-of-basis matrix $T$, and let $V$ have two bases $\eta_1,\dots,\eta_m$ and $s_1,\dots,s_m$ with change-of-basis matrix $S$. If $f\in\operatorname{Hom}(U,V)$ has matrix $F$ with respect to the first pair of bases, then its matrix with respect to the second pair is $\tilde F=S^{-1}FT$.

**Proof** By definition $f(t_1,\dots,t_n)=(s_1,\dots,s_m)\tilde F=(\eta_1,\dots,\eta_m)(S\tilde F)$; on the other hand

$$
f(t_1,\dots,t_n)=f\big((e_1,\dots,e_n)T\big)=\big((\eta_1,\dots,\eta_m)F\big)T=(\eta_1,\dots,\eta_m)(FT).
$$

The uniqueness of coordinates gives $S\tilde F=FT$, and since $S$ is invertible, $\tilde F=S^{-1}FT$. $\square$

So the matrices of one linear map with respect to different bases are related by **matrix equivalence**. The converse also holds:

**Theorem 8.7.2** Let $f\in\operatorname{Hom}(U,V)$ have matrix $F$ with respect to some pair of bases. Then for every matrix $\tilde F$ equivalent to $F$ there are bases of $U,V$ with respect to which $f$ has matrix $\tilde F$. In particular, there are bases of $U,V$ in which the matrix of $f$ is the **rank normal form** $\begin{bmatrix}I_r&O\\O&O\end{bmatrix}$, $r=\operatorname{rank}(F)=\dim\mathcal{R}(f)$.

**Proof** If $\tilde F=PFQ$ with $P,Q$ invertible, take $T=Q$ and $S=P^{-1}$; by Proposition 8.5.2 they determine new bases, and by Theorem 8.7.1 the new matrix is $S^{-1}FT=\tilde F$. $\square$

The bases giving the rank normal form can also be constructed directly: take a basis $t_{r+1},\dots,t_n$ of $\mathcal{N}(f)$ and extend it to a basis $t_1,\dots,t_n$ of $U$; then $s_i=f(t_i)$ ($i\le r$) is a basis of $\mathcal{R}(f)$, which we extend to a basis of $V$. In these bases $f(t_i)=s_i$ ($i\le r$) and $f(t_i)=0$ ($i>r$). Thus for a linear map between two spaces the only invariant is the rank: as long as the bases on the two sides can be chosen independently, a linear map has no further structure.

### 8.7.2. Linear Transformations: Similarity

A linear transformation $f\in\operatorname{Hom}(V,V)$ has the same domain and codomain, so its matrix is taken with the same basis on both sides: $f(e_1,\dots,e_n)=(e_1,\dots,e_n)F$, and the square matrix $F$ of order $n$ is called the matrix of $f$ with respect to this basis.

**Proposition 8.7.1** Let $f\in\operatorname{Hom}(V,V)$ have matrix $F$ with respect to the basis $e_1,\dots,e_n$, and let $x$ have coordinate vector $\hat{\boldsymbol{x}}$. Then $(\lambda,x)$ is an eigenpair of $f$ if and only if $(\lambda,\hat{\boldsymbol{x}})$ is an eigenpair of $F$. Hence $F$ is diagonalizable if and only if $f$ has $n$ linearly independent eigenvectors.

**Proof** $f(x)=(e_1,\dots,e_n)(F\hat{\boldsymbol{x}})$, and by the uniqueness of coordinates $f(x)=\lambda x$ if and only if $F\hat{\boldsymbol{x}}=\lambda\hat{\boldsymbol{x}}$. The last statement follows from Corollary 8.5.1 and the diagonalization criterion of [Chapter 6](/2.1.6). $\square$

Through matrix representations, the eigenvalue problem for a linear transformation of an abstract space becomes the eigenvalue problem for a matrix, and then the problem of finding roots of the **characteristic polynomial** and solving homogeneous linear systems.

**Theorem 8.7.3** Let $T$ be the change-of-basis matrix between two bases of $V$, $(t_1,\dots,t_n)=(e_1,\dots,e_n)T$. If $f\in\operatorname{Hom}(V,V)$ has matrix $F$ with respect to $e_1,\dots,e_n$, then its matrix with respect to $t_1,\dots,t_n$ is $T^{-1}FT$.

**Proof** Take $S=T$ in Theorem 8.7.1. $\square$

**Theorem 8.7.4** Two square matrices $A,B$ of order $n$ over a number field $\mathbb{F}$ are **similar matrices** if and only if they are the matrices of one linear transformation of some $n$-dimensional vector space $V$ with respect to two bases.

**Proof** Sufficiency is Theorem 8.7.3. Necessity: let $B=T^{-1}AT$. Take any basis $e_1,\dots,e_n$ of $V$; by Proposition 8.6.1 there is a linear transformation $f$ with $f(e_1,\dots,e_n)=(e_1,\dots,e_n)A$. Let $(t_1,\dots,t_n)=(e_1,\dots,e_n)T$; this is a basis, and the matrix of $f$ with respect to it is $T^{-1}AT=B$. $\square$

This theorem is the starting point of the following chapters:

- Diagonalizing $A$ means finding a basis $(\boldsymbol{t}_1,\dots,\boldsymbol{t}_n)=(\boldsymbol{e}_1,\dots,\boldsymbol{e}_n)T$ of $\mathbb{F}^n$ in which the matrix $T^{-1}AT$ of $\boldsymbol{x}\mapsto A\boldsymbol{x}$ is diagonal; this basis consists of $n$ linearly independent eigenvectors of $A$.
- Similarity invariants (characteristic polynomial, eigenvalues with their multiplicities, **trace**, **determinant**, rank) are invariants of the linear transformation itself, so one can define the characteristic polynomial, trace and determinant of a linear transformation without reference to a basis.
- When a matrix is not diagonalizable, the natural question is: which basis makes the matrix "simplest"? [Chapter 10](/2.1.10) answers it using direct sum decompositions into invariant subspaces and generalized eigenspaces; the result is the **Jordan canonical form**.

The following computation illustrates "simplification by change of basis": the matrix of differentiation on $\mathbb{R}[x]_4$ with respect to the basis $1,x,x^2,x^3$ has superdiagonal $1,2,3$; after changing to the basis $1,x,\frac{x^2}{2!},\frac{x^3}{3!}$ it becomes a Jordan block with all superdiagonal entries equal to $1$.

```python
import sympy as sp

x = sp.symbols("x")
n = 4

def coords(p):
    """Coordinates of p in the monomial basis 1, x, ..., x^(n-1)."""
    c = sp.Poly(p, x).all_coeffs()[::-1]
    return sp.Matrix(c + [0] * (n - len(c)))

D = lambda p: sp.diff(p, x)
mono = [x**k for k in range(n)]
F = sp.Matrix.hstack(*[coords(D(b)) for b in mono])   # matrix of D in 1, x, x^2, x^3
new = [x**k / sp.factorial(k) for k in range(n)]       # basis 1, x, x^2/2, x^3/6
T = sp.Matrix.hstack(*[coords(b) for b in new])        # transition matrix
print(F)
print(T.inv() * F * T)                                 # matrix of D in the new basis
```

**Example 8.7.1** Consider the symmetrization $S\colon \mathbb{F}^{2\times2}\to \mathbb{F}^{2\times2}$, $A\mapsto\frac12(A+A^{\mathsf T})$, with the basis $E_{11},E_{21},E_{12},E_{22}$. Since $S(E_{11})=E_{11}$, $S(E_{21})=S(E_{12})=\frac12(E_{21}+E_{12})$ and $S(E_{22})=E_{22}$,

$$
S(E_{11},E_{21},E_{12},E_{22})=(E_{11},E_{21},E_{12},E_{22})\begin{bmatrix}1&0&0&0\\0&\frac12&\frac12&0\\0&\frac12&\frac12&0\\0&0&0&1\end{bmatrix}.
$$

This matrix is symmetric and hence diagonalizable, with eigenvalues $0$ (simple) and $1$ (triple) and eigenvectors $[0\ 1\ {-1}\ 0]^{\mathsf T}$ and $[1\ 0\ 0\ 0]^{\mathsf T},[0\ 0\ 0\ 1]^{\mathsf T},[0\ 1\ 1\ 0]^{\mathsf T}$ respectively. Translating back into matrices,

$$
\mathcal{N}(S)=\operatorname{span}\left(\begin{bmatrix}0&-1\\1&0\end{bmatrix}\right),\qquad \mathcal{N}(\mathrm{id}-S)=\mathcal{R}(S)=\operatorname{span}\left(\begin{bmatrix}1&0\\0&0\end{bmatrix},\begin{bmatrix}0&0\\0&1\end{bmatrix},\begin{bmatrix}0&1\\1&0\end{bmatrix}\right),
$$

and with respect to the basis $\begin{bmatrix}1&0\\0&0\end{bmatrix},\begin{bmatrix}0&0\\0&1\end{bmatrix},\begin{bmatrix}0&1\\1&0\end{bmatrix},\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ the matrix of $S$ is $\operatorname{diag}(1,1,1,0)$.

**Example 8.7.2** The matrix of $D$ on $\operatorname{span}(1,\sin x,\cos x)$ in Example 8.6.2 has characteristic polynomial $\lambda(\lambda^2+1)$, whose only real eigenvalue is $0$, so $D$ is not diagonalizable over the real field. If complex coefficients are allowed, $\mathrm{e}^{\mathrm{i}x}=\cos x+\mathrm{i}\sin x$ and $\mathrm{e}^{-\mathrm{i}x}$ are eigenvectors for $\pm\mathrm{i}$, and the matrix of $D$ with respect to the basis $1,\mathrm{e}^{\mathrm{i}x},\mathrm{e}^{-\mathrm{i}x}$ is $\operatorname{diag}(0,\mathrm{i},-\mathrm{i})$. Diagonalizability depends on the number field, which is why [Chapter 9](/2.1.9) discusses complex numbers and the factorization of polynomials.

The various equivalence relations on matrices in this course can all be understood as representations of one object with respect to different bases:

| Relation | Matrix form | Object represented | Choice of bases | Canonical form |
|---|---|---|---|---|
| Equivalence | $S^{-1}FT$ | linear map $U\to V$ | bases of $U,V$ chosen independently | $\operatorname{diag}(I_r,O)$ |
| Similarity | $T^{-1}FT$ | linear transformation $V\to V$ | one basis | Jordan canonical form ([Chapter 10](/2.1.10)) |
| Orthogonal (unitary) similarity | $Q^{\mathsf T}FQ$ | linear transformation of an inner product space | orthonormal basis | diagonal for normal matrices ([Chapter 12](/2.1.12)) |
| Congruence | $T^{\mathsf T}GT$ | bilinear form $V\times V\to \mathbb{F}$ | one basis | $\operatorname{diag}(I_p,-I_q,O)$ in the real symmetric case ([Chapter 7](/2.1.7), [Chapter 13](/2.1.13)) |

## 8.8. Dual Spaces

For fixed $\boldsymbol{u}$, the inner product $\langle\boldsymbol{x},\boldsymbol{u}\rangle$ is a linear function of $\boldsymbol{x}$; the trace is a linear function of matrices; the definite integral is a linear function of continuous functions. Such linear maps "vector ↦ number" themselves form a vector space, dual to the original one, and this is where the transpose finds its explanation.

**Definition 8.8.1 (Linear Functional)** Let $V$ be a vector space over a number field $\mathbb{F}$. A linear map $f\colon V\to \mathbb{F}$ (with $\mathbb{F}$ regarded as a one-dimensional vector space) is called a **linear functional** on $V$.

By Proposition 8.6.1, a linear functional is determined by its values on a basis. For example, if $f\colon \mathbb{R}^2\to\mathbb{R}$ has $f(\boldsymbol{e}_1)=10$ and $f(\boldsymbol{e}_2)=1$, then $f\big([a\ b]^{\mathsf T}\big)=af(\boldsymbol{e}_1)+bf(\boldsymbol{e}_2)=10a+b$. Other examples: the trace on $\mathbb{F}^{n\times n}\to \mathbb{F}$; $C[a,b]\to\mathbb{R}$, $g\mapsto\int_a^bg(x)\,\mathrm{d}x$; $\mathbb{F}[x]\to \mathbb{F}$, $p\mapsto p(c)$; and taking the $i$-th coordinate, $\boldsymbol{x}\mapsto x_i$.

**Definition 8.8.2 (Dual Space)** The set $V^*=\operatorname{Hom}(V,\mathbb{F})$ of linear functionals on $V$ is a vector space over $\mathbb{F}$ under the addition $(f+g)(v)=f(v)+g(v)$ and scalar multiplication $(cf)(v)=cf(v)$; it is called the **dual space** of $V$.

**Example 8.8.1** Every element of $(\mathbb{R}^3)^*$ has the form $f(\boldsymbol{x})=ax_1+bx_2+cx_3$ with $a=f(\boldsymbol{e}_1)$, $b=f(\boldsymbol{e}_2)$, $c=f(\boldsymbol{e}_3)$; so $(\mathbb{R}^3)^*$ can be identified with the set of row vectors $[a\ b\ c]$, and $f(\boldsymbol{x})$ is a row vector times a column vector. In general, linear functionals on $\mathbb{F}^n$ are just $1\times n$ matrices (Theorem 8.6.1).

**Proposition 8.8.1 (Representation of Linear Functionals on $\mathbb{R}^n$)** Let $f$ be a linear functional on $\mathbb{R}^n$. Then there is a unique $\boldsymbol{u}\in\mathbb{R}^n$ such that $f(\boldsymbol{x})=\langle\boldsymbol{x},\boldsymbol{u}\rangle=\boldsymbol{u}^{\mathsf T}\boldsymbol{x}$ for all $\boldsymbol{x}$, namely $\boldsymbol{u}=[f(\boldsymbol{e}_1)\ \cdots\ f(\boldsymbol{e}_n)]^{\mathsf T}$.

**Proof** $f(\boldsymbol{x})=\sum x_if(\boldsymbol{e}_i)=\boldsymbol{u}^{\mathsf T}\boldsymbol{x}$. If $\boldsymbol{u}_1,\boldsymbol{u}_2$ both work, then $\langle\boldsymbol{x},\boldsymbol{u}_1-\boldsymbol{u}_2\rangle=0$ for all $\boldsymbol{x}$, and taking $\boldsymbol{x}=\boldsymbol{u}_1-\boldsymbol{u}_2$ gives $\boldsymbol{u}_1=\boldsymbol{u}_2$. $\square$

In other words, by means of the **inner product**, the map $\boldsymbol{u}\mapsto\langle\cdot,\boldsymbol{u}\rangle$ is an isomorphism from $\mathbb{R}^n$ to $(\mathbb{R}^n)^*$. The proof uses only the orthonormal basis $\boldsymbol{e}_i$, so the same holds in every finite-dimensional inner product space; this is the Riesz representation theorem (for general inner product spaces see [Chapter 12](/2.1.12)). For a general vector space without an inner product, we relate $V$ and $V^*$ through dual bases.

**Definition 8.8.3 (Dual Basis)** Let $e_1,\dots,e_n$ be a basis of $V$. By Proposition 8.6.1 there are unique $f_i\in V^*$ with $f_i(e_j)=\delta_{ij}$ ($i,j=1,\dots,n$); $f_1,\dots,f_n$ is called the **dual basis** of $e_1,\dots,e_n$, often written $e_1^*,\dots,e_n^*$.

$f_i$ is just the function "take the $i$-th coordinate": $f_i(x_1e_1+\cdots+x_ne_n)=x_i$. Hence $x=\sum_if_i(x)e_i$.

**Theorem 8.8.1** The dual basis $f_1,\dots,f_n$ is a basis of $V^*$, and every $f\in V^*$ satisfies $f=\sum_{i=1}^nf(e_i)f_i$. In particular, $\dim V^*=\dim V$.

**Proof** Linear independence: if $c_1f_1+\cdots+c_nf_n=0$ (the zero function), applying both sides to $e_j$ gives $c_j=0$. Spanning: let $g=\sum_if(e_i)f_i$; then $g(e_j)=f(e_j)$ for all $j$, so $g=f$ by Proposition 8.6.1. $\square$

**Theorem 8.8.2 (Change of Dual Basis)** Let $e_1,\dots,e_n$ and $t_1,\dots,t_n$ be two bases of $V$ with $(t_1,\dots,t_n)=(e_1,\dots,e_n)P$, and let their dual bases satisfy $(t_1^*,\dots,t_n^*)=(e_1^*,\dots,e_n^*)Q$. Then $Q=(P^{\mathsf T})^{-1}$.

**Proof** Let $P=[p_{ij}]$ and $Q=[q_{ij}]$, so that $t_k=\sum_ip_{ik}e_i$ and $t_l^*=\sum_jq_{jl}e_j^*$. Then

$$
\delta_{lk}=t_l^*(t_k)=\sum_j\sum_iq_{jl}p_{ik}\,e_j^*(e_i)=\sum_iq_{il}p_{ik}=(Q^{\mathsf T}P)_{lk},
$$

that is, $Q^{\mathsf T}P=I$ and $Q=(P^{-1})^{\mathsf T}=(P^{\mathsf T})^{-1}$. $\square$

The basis changes by $P$, coordinates change by $P^{-1}$, and the dual basis changes by $(P^{\mathsf T})^{-1}$; the "coordinates" of a linear functional (the row vector $[f(e_1)\ \cdots\ f(e_n)]$ of its values on the basis) change by right multiplication by $P$, in step with the basis. In physics the former behavior is called contravariant and the latter covariant.

**Example 8.8.2** Let $v_1,v_2,v_3$ be a basis of $V$. Find the dual basis of $\alpha=v_1$, $\beta=v_1+v_2$, $\gamma=v_1+v_2+v_3$. The change-of-basis matrix and the matrix we need are

$$
P=\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix},\qquad (P^{\mathsf T})^{-1}=\begin{bmatrix}1&0&0\\-1&1&0\\0&-1&1\end{bmatrix},
$$

so $\alpha^*=v_1^*-v_2^*$, $\beta^*=v_2^*-v_3^*$ and $\gamma^*=v_3^*$. Check: $\alpha^*(\beta)=1-1=0$, $\beta^*(\beta)=1$, $\beta^*(\gamma)=1-1=0$.

### 8.8.1. The Double Dual

Write $\langle f,v\rangle=f(v)$ for $f\in V^*$ and $v\in V$. This pairing is linear in each variable and nondegenerate:

- if $\langle f,v\rangle=0$ for all $v\in V$, then $f=0$ (by definition);
- if $\langle f,v\rangle=0$ for all $f\in V^*$, then $v=0$ (otherwise extend $v$ to a basis and take the element $f$ of the dual basis corresponding to $v$; then $f(v)=1$).

**Theorem 8.8.3** Let $V$ be a finite-dimensional vector space. Then $\Phi\colon V\to V^{**}$, $v\mapsto\Phi_{v}$, $\Phi_{v}(f)=f(v)$, is an isomorphism.

**Proof** $\Phi_{v}$ is a linear functional on $V^*$, and $\Phi$ is a linear map. By the nondegeneracy of the pairing, $\Phi_{v}=0$ implies $v=0$, so $\Phi$ is injective; moreover $\dim V^{**}=\dim V^*=\dim V$, so by Proposition 8.6.3 $\Phi$ is bijective. $\square$

$V$ and $V^*$ have the same dimension and are therefore isomorphic, but the isomorphism depends on a choice of basis (for example $e_i\mapsto e_i^*$, which changes with the basis); by contrast, the definition of $\Phi\colon V\to V^{**}$ involves no basis at all, and $\Phi$ is called the canonical isomorphism. We may therefore regard $V$ as the dual space of $V^*$: $V$ and $V^*$ are dual to each other. For infinite-dimensional spaces $\Phi$ is still injective but in general not surjective.

### 8.8.2. Dual Maps

**Definition 8.8.4 (Dual Map)** Let $f\in\operatorname{Hom}(U,V)$. The map $f^{\mathsf t}\colon V^*\to U^*$, $\varphi\mapsto\varphi\circ f$, is called the **dual map** of $f$.

$f^{\mathsf t}$ is linear and satisfies $\langle f^{\mathsf t}\varphi,u\rangle=\langle\varphi,f(u)\rangle$. Note the reversal of direction: $f$ goes from $U$ to $V$, while $f^{\mathsf t}$ goes from $V^*$ to $U^*$. (The dual map is also often written $f^*$; this text reserves $f^*$ for the adjoint of an operator on an inner product space in [Chapter 12](/2.1.12).)

**Theorem 8.8.4** Let $f\in\operatorname{Hom}(U,V)$ have matrix $F$ with respect to the bases $e_1,\dots,e_n;\eta_1,\dots,\eta_m$. Then the matrix of $f^{\mathsf t}$ with respect to the dual bases $\eta_1^*,\dots,\eta_m^*;e_1^*,\dots,e_n^*$ is $F^{\mathsf T}$.

**Proof** By Theorem 8.8.1, $f^{\mathsf t}(\eta_k^*)=\sum_j\big(f^{\mathsf t}\eta_k^*\big)(e_j)\,e_j^*=\sum_j\eta_k^*\big(f(e_j)\big)e_j^*$. Since $f(e_j)=\sum_lf_{lj}\eta_l$, we have $\eta_k^*(f(e_j))=f_{kj}$; that is, the coordinate vector of $f^{\mathsf t}(\eta_k^*)$ is the $k$-th row of $F$, so the $k$-th column of the matrix of $f^{\mathsf t}$ is the $k$-th row of $F$. $\square$

So the **transpose** of a matrix is the matrix of the dual map. All properties of the matrix transpose thereby acquire coordinate-free interpretations: $(gf)^{\mathsf t}=f^{\mathsf t}g^{\mathsf t}$ corresponds to $(GF)^{\mathsf T}=F^{\mathsf T}G^{\mathsf T}$; $\operatorname{rank}(f^{\mathsf t})=\operatorname{rank}(f)$ corresponds to row rank equals column rank; and the kernel of $f^{\mathsf t}$, the set of linear functionals vanishing on $\mathcal{R}(f)$, corresponds to the orthogonality between $\mathcal{N}(A^{\mathsf T})$ and $\mathcal{R}(A)$. In $\mathbb{R}^n$, identifying linear functionals with vectors via Proposition 8.8.1, the dual map is the special case of the **adjoint operator** in the standard orthonormal basis. The dual space and the pairing $V^*\times V\to \mathbb{F}$ are the starting point for the bilinear forms and tensors of [Chapter 13](/2.1.13).

## Summary

This chapter extends the theory of $\mathbb{R}^n$ to vector spaces over a number field and, by "choosing a basis", translates abstract problems back into matrix problems.

| Topic | Definitions and results | Reduction to matrices |
|---|---|---|
| Number fields and vector spaces | subsets of $\mathbb{C}$ closed under the four operations; eight axioms; $\mathbb{F}^m$, $\mathbb{F}^{m\times n}$, function spaces, $\mathbb{F}[x]_n$ | — |
| Sums and direct sums of subspaces | $M_1+M_2$; direct ⇔ zero decomposes uniquely ⇔ $M_1\cap M_2=\{0\}$ | $\mathcal{R}(A)+\mathcal{R}(B)=\mathcal{R}([A\ B])$ |
| Bases and dimension | Lemma 8.3.1 (a longer list represented by a shorter one is dependent); basis extension; dimension formula $\dim(M_1+M_2)=\dim M_1+\dim M_2-\dim(M_1\cap M_2)$ | homogeneous system $K\boldsymbol{k}=\boldsymbol{0}$ |
| Linear maps | $\operatorname{Hom}(U,V)$; kernel $\mathcal{N}(f)$, image $\mathcal{R}(f)$; injective ⇔ $\mathcal{N}(f)=\{0\}$ | — |
| Isomorphisms and coordinates | the coordinate map $V\to \mathbb{F}^n$ is an isomorphism; dimension is a complete invariant of isomorphism | linear dependence, rank ⇔ rank of the coordinate matrix |
| Change of basis | $(t_i)=(e_i)T$, coordinates $\boldsymbol{x}=T\boldsymbol{y}$ | Algorithm 8.5.1: $[A\ B]\to[I\ T]$ |
| Matrix representation | $f(e_1,\dots,e_n)=(\eta_1,\dots,\eta_m)F$; $\operatorname{Hom}(U,V)\cong \mathbb{F}^{m\times n}$; $\sigma(gf)=\sigma(g)\sigma(f)$; $\dim\mathcal{N}(f)+\dim\mathcal{R}(f)=\dim U$ | $\widehat{f(a)}=F\hat{\boldsymbol{a}}$ |
| Change of basis for maps | linear maps: $S^{-1}FT$ (equivalence, canonical form $\operatorname{diag}(I_r,O)$); linear transformations: $T^{-1}FT$ (similarity) | similar ⇔ matrices of one linear transformation in two bases |
| Dual spaces | $V^*=\operatorname{Hom}(V,\mathbb{F})$; dual basis $f_i(e_j)=\delta_{ij}$, which changes by $(P^{\mathsf T})^{-1}$; $V\cong V^{**}$ canonically | the matrix of the dual map is $F^{\mathsf T}$ |
