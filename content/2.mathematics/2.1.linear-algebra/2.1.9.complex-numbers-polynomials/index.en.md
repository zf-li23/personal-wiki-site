---
title: Complex Numbers and Polynomials
source_hash: 14006fedf49a
---

How far a matrix can be simplified depends on how far its characteristic polynomial factors over the given number field. For example, $\lambda^4+1$ is irreducible over $\mathbb{Q}$, factors over $\mathbb{R}$ as $(\lambda^2+\sqrt2\lambda+1)(\lambda^2-\sqrt2\lambda+1)$, and factors over $\mathbb{C}$ into four linear factors $\prod_{k=0}^{3}(\lambda-\mathrm{e}^{\mathrm{i}(2k+1)\pi/4})$; correspondingly, a real matrix with this characteristic polynomial can only be reduced to two $2\times2$ blocks over $\mathbb{R}$, but is diagonalizable over $\mathbb{C}$. Example 8.7.2 of [Chapter 8](/2.1.8) makes the same point. This chapter first introduces complex numbers systematically, the number field over which every polynomial factors completely, together with complex matrices and complex vector spaces; it then studies polynomials in one variable over a general number field $\mathbb{F}$: division with remainder, divisibility, greatest common divisors, irreducible polynomials and factorization; and finally it discusses factorization over $\mathbb{C}$, $\mathbb{R}$ and $\mathbb{Q}$ and the relations between roots and coefficients.

Polynomial theory is used in [Chapter 10](/2.1.10) for minimal polynomials and the generalized eigenspace decomposition: splitting a space into a direct sum of invariant subspaces of a linear transformation rests precisely on coprimality of polynomials and Bézout's identity; deciding whether a matrix is diagonalizable comes down to checking whether its minimal polynomial has repeated roots, which in turn requires only one greatest common divisor computed by the Euclidean algorithm. The matrix functions of [Chapter 11](/2.1.11) are computed with interpolation polynomials. The whole chapter can be read in parallel with the integers: like $\mathbb{Z}$, $\mathbb{F}[x]$ has division with remainder, greatest common divisors and unique factorization, and both are examples of the **polynomial rings** and **integral domains** of discrete mathematics ([1.3.3](/1.3.3)). Polynomial computations also illustrate "standardized solving" throughout: division reduces to synthetic division, the greatest common divisor to repeated division with remainder, and rational roots to finitely many checks.

## 9.1. Complex Numbers

### 9.1.1. Definition and Arithmetic of Complex Numbers

The real matrix $A=\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ ($a,b\in\mathbb{R}$, $b\neq0$) has characteristic polynomial $(\lambda-a)^2+b^2$ with no real roots: in the plane, $A$ is a rotation composed with a scaling and has no invariant direction. To give it eigenvalues we must introduce a number $\mathrm{i}$ with $\mathrm{i}^2=-1$; the eigenvalues are then $a\pm b\mathrm{i}$.

**Definition 9.1.1 (Complex Number)** Introduce a symbol $\mathrm{i}$ with $\mathrm{i}^2=-1$. A number of the form $z=a+b\mathrm{i}$ ($a,b\in\mathbb{R}$) is called a **complex number**; $a=\operatorname{Re}z$ and $b=\operatorname{Im}z$ are called its real part and imaginary part. The set of all complex numbers is written $\mathbb{C}=\{a+b\mathrm{i}\mid a,b\in\mathbb{R}\}$.

Complex numbers are added and multiplied by the rules for polynomials, with $\mathrm{i}^2$ replaced by $-1$:

$$
(a_1+b_1\mathrm{i})\pm(a_2+b_2\mathrm{i})=(a_1\pm a_2)+(b_1\pm b_2)\mathrm{i},\qquad (a_1+b_1\mathrm{i})(a_2+b_2\mathrm{i})=(a_1a_2-b_1b_2)+(a_1b_2+a_2b_1)\mathrm{i}.
$$

**Definition 9.1.2 (Complex Conjugate)** The **complex conjugate** of $z=a+b\mathrm{i}$ is $\bar z=a-b\mathrm{i}$. The real number $|z|=\sqrt{a^2+b^2}$ is called the **modulus** of $z$.

Basic properties of conjugation: $\bar z=z$ if and only if $z\in\mathbb{R}$; $\bar z=-z$ if and only if $z$ is zero or purely imaginary; $\overline{z_1\pm z_2}=\bar z_1\pm\bar z_2$ and $\overline{z_1z_2}=\bar z_1\bar z_2$; $z\bar z=a^2+b^2=|z|^2$. By the last identity, for $z\neq0$ we have $\dfrac1z=\dfrac{\bar z}{|z|^2}$ and $\dfrac{z_1}{z_2}=\dfrac{z_1\bar z_2}{|z_2|^2}$. Thus $\mathbb{C}$ is closed under the four arithmetic operations; it is a **number field**, and in fact the largest one.

### 9.1.2. Geometric Representation and Exponential Form

A complex number $z=a+b\mathrm{i}$ has four common representations:

1. Algebraic form: $z=a+b\mathrm{i}$.
2. Geometric form: the point $(a,b)$ of the plane, or the vector from the origin to $(a,b)$. Addition of complex numbers is vector addition, $\bar z$ is the reflection in the real axis, and $|z|$ is the length of the vector.
3. Polar form: let $r=|z|$ and let $\theta$ be the angle from the positive real axis to the vector $z$; then $\cos\theta=a/r$, $\sin\theta=b/r$, and $z=r(\cos\theta+\mathrm{i}\sin\theta)$.
4. Exponential form: $z=r\mathrm{e}^{\mathrm{i}\theta}$ (see Euler's formula below).

**Definition 9.1.3 (Polar Form of a Complex Number)** Writing a nonzero complex number as $z=r(\cos\theta+\mathrm{i}\sin\theta)$ ($r=|z|>0$) is called the **polar form** of $z$ (also the trigonometric form), and $\theta$ is called an **argument** of $z$. The argument is determined only up to an integer multiple of $2\pi$.

By the angle addition formulas for sine and cosine,

$$
r_1(\cos\theta_1+\mathrm{i}\sin\theta_1)\cdot r_2(\cos\theta_2+\mathrm{i}\sin\theta_2)=r_1r_2\big(\cos(\theta_1+\theta_2)+\mathrm{i}\sin(\theta_1+\theta_2)\big),
$$

that is, the modulus of a product is the product of the moduli and its argument is the sum of the arguments: multiplying by $z_2$ rotates the plane by $\theta_2$ and scales it by the factor $r_2$. This matches the rule "multiply exponentials, add exponents", so we write

$$
\mathrm{e}^{\mathrm{i}\theta}=\cos\theta+\mathrm{i}\sin\theta,
$$

which is called *Euler's formula*. Using power series one can define $\mathrm{e}^z$ for all complex numbers and prove this identity (Complex Analysis, 2.3); here we take it as the definition of $\mathrm{e}^{\mathrm{i}\theta}$. It follows that $\mathrm{e}^{\mathrm{i}\theta_1}\mathrm{e}^{\mathrm{i}\theta_2}=\mathrm{e}^{\mathrm{i}(\theta_1+\theta_2)}$, $(\mathrm{e}^{\mathrm{i}\theta})^n=\mathrm{e}^{\mathrm{i}n\theta}$ (De Moivre's formula), $\mathrm{e}^{\mathrm{i}\theta}=\mathrm{e}^{\mathrm{i}(\theta+2k\pi)}$ ($k\in\mathbb{Z}$), and

$$
\mathrm{e}^{\mathrm{i}\pi}=-1,\qquad \mathrm{e}^{\mathrm{i}\pi/2}=\mathrm{i},\qquad \mathrm{e}^{2k\pi\mathrm{i}}=1\ (k\in\mathbb{Z}).
$$

**Example 9.1.1** Compute $(1+\mathrm{i})^{10}$. Since $1+\mathrm{i}=\sqrt2\mathrm{e}^{\mathrm{i}\pi/4}$, we get $(1+\mathrm{i})^{10}=2^5\mathrm{e}^{\mathrm{i}5\pi/2}=32\mathrm{i}$. The binomial expansion would require 11 terms; the exponential form requires one power of the modulus and one multiple of the argument. Likewise, expanding $(\cos\theta+\mathrm{i}\sin\theta)^2=\cos2\theta+\mathrm{i}\sin2\theta$ and comparing real and imaginary parts gives the double angle formulas $\cos2\theta=\cos^2\theta-\sin^2\theta$ and $\sin2\theta=2\sin\theta\cos\theta$.

### 9.1.3. The Matrix Form of Complex Numbers

**Proposition 9.1.1** The map $T\colon \mathbb{C}\to\mathbb{R}^{2\times2}$, $a+b\mathrm{i}\mapsto\begin{bmatrix}a&-b\\b&a\end{bmatrix}$, is injective and preserves addition and multiplication: $T(z_1+z_2)=T(z_1)+T(z_2)$ and $T(z_1z_2)=T(z_1)T(z_2)$.

**Proof** Injectivity and additivity are clear. For multiplication,

$$
T(z_1)T(z_2)=\begin{bmatrix}a_1&-b_1\\b_1&a_1\end{bmatrix}\begin{bmatrix}a_2&-b_2\\b_2&a_2\end{bmatrix}=\begin{bmatrix}a_1a_2-b_1b_2&-(a_1b_2+a_2b_1)\\a_1b_2+a_2b_1&a_1a_2-b_1b_2\end{bmatrix}=T(z_1z_2).\ \square
$$

So $T$ is an injective **ring homomorphism**, and $\mathbb{C}$ is isomorphic to the subfield $\left\{\begin{bmatrix}a&-b\\b&a\end{bmatrix}\right\}$ of the ring of real $2\times2$ matrices (see also Example 8.4.1 of [Chapter 8](/2.1.8)). Under this correspondence, $\mathrm{i}$ corresponds to the rotation by $90^\circ$, $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$, whose square is $-I$; $\bar z$ corresponds to the **transpose**; $|z|^2$ corresponds to the **determinant**; and the polar form corresponds to

$$
T(r\mathrm{e}^{\mathrm{i}\theta})=r\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix},
$$

the product of the scaling matrix $rI$ and a rotation matrix, which is exactly the geometric meaning of complex multiplication. Extending $z=r\mathrm{e}^{\mathrm{i}\theta}$ to matrices gives the polar decomposition $A=R\mathrm{e}^{\mathrm{i}M}$ of [Chapter 13](/2.1.13) ($R$ positive semidefinite, $\mathrm{e}^{\mathrm{i}M}$ unitary); the matrix $\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ is the prototype of the real normal matrices of order 2 in [Chapter 12](/2.1.12).

### 9.1.4. Powers and Roots of Complex Numbers

For a real number $\alpha$ and $z=r\mathrm{e}^{\mathrm{i}\theta}\neq0$, since $z=r\mathrm{e}^{\mathrm{i}(\theta+2k\pi)}$, we define

$$
z^\alpha=r^\alpha \mathrm{e}^{\mathrm{i}\alpha(\theta+2k\pi)},\qquad k\in\mathbb{Z}.
$$

This may have several values:

- if $\alpha\in\mathbb{Z}$, then $\mathrm{e}^{2\mathrm{i}\alpha k\pi}=1$, and $z^\alpha=r^\alpha \mathrm{e}^{\mathrm{i}\alpha\theta}$ has a single value;
- if $\alpha=q/p$ ($p>0$, $p,q$ coprime), then $z^\alpha=r^\alpha \mathrm{e}^{\mathrm{i}(q\theta+2qk\pi)/p}$ is periodic in $k$ with period $p$ and has exactly $p$ values ($k=0,1,\dots,p-1$);
- if $\alpha\notin\mathbb{Q}$, different $k$ give different values, and $z^\alpha$ has infinitely many values. For example, $\mathrm{i}=\mathrm{e}^{\mathrm{i}(\pi/2+2k\pi)}$, so $\mathrm{i}^\pi=\mathrm{e}^{\mathrm{i}(\pi^2/2+2k\pi^2)}$, $k\in\mathbb{Z}$.

The systematic treatment of multivalued functions (branches, Riemann surfaces) belongs to complex analysis. The most important case is the roots of $1$.

**Definition 9.1.4 (Root of Unity)** Each of the $n$ complex roots $\omega_k=\mathrm{e}^{2k\pi\mathrm{i}/n}$ ($k=0,1,\dots,n-1$) of the equation $z^n=1$ is called an $n$-th **root of unity**.

Let $\omega=\omega_1=\mathrm{e}^{2\pi\mathrm{i}/n}$; then $\omega_k=\omega^k$, the $n$-th roots of unity are the vertices of a regular $n$-gon inscribed in the unit circle, and $x^n-1=\prod_{k=0}^{n-1}(x-\omega^k)$. They satisfy:

- $\bar\omega_k=\omega_{n-k}$ (since $|\omega_k|=1$, $\bar\omega_k=\omega_k^{-1}$);
- for $n\ge2$, $1+\omega+\omega^2+\cdots+\omega^{n-1}=0$: since $\omega\neq1$, the geometric series sums to $\frac{1-\omega^n}{1-\omega}=0$; geometrically, the vertex vectors of a regular polygon sum to zero.

The left panel of the figure below illustrates the geometry of multiplication: multiplying by $w=1.3\,\mathrm{e}^{\mathrm{i}\pi/6}$ rotates the whole plane about the origin by $30^\circ$ and enlarges it by the factor $1.3$, without changing the shape of figures. The right panel shows the 8th roots of unity: they are the vertices of a regular octagon, and adding them head to tail in order returns to the origin.

![Left: a figure S multiplied repeatedly by w = 1.3 e^{iπ/6}, each time rotated by 30° and enlarged by 1.3. Right: the 8th roots of unity ω^k form a regular octagon inscribed in the unit circle, and the polygonal path of partial sums 1 + ω + ⋯ + ω^k (drawn scaled by 0.35) returns to the origin](./plots/complex-multiplication-roots-of-unity.py)

## 9.2. Complex Matrices and Complex Vector Spaces

The conjugate of a complex matrix $A=[a_{ij}]\in\mathbb{C}^{m\times n}$ is $\bar A=[\bar a_{ij}]$. Separating real and imaginary parts of the entries, $A=U+\mathrm{i}V$ ($U,V$ real matrices), we have $\bar A=U-\mathrm{i}V$; $A$ is real if and only if $\bar A=A$; and $\overline{z_1z_2}=\bar z_1\bar z_2$ gives $\overline{AB}=\bar A\bar B$. For example,

$$
\begin{bmatrix}1-\mathrm{i}&2\mathrm{i}\\3+\mathrm{i}&4\end{bmatrix}=\begin{bmatrix}1&0\\3&4\end{bmatrix}+\mathrm{i}\begin{bmatrix}-1&2\\1&0\end{bmatrix}.
$$

**Definition 9.2.1 (Conjugate Transpose)** The **conjugate transpose** (also called the Hermitian adjoint) of a complex matrix $A$ is $A^{\mathsf H}=\bar A^{\mathsf T}=\overline{A^{\mathsf T}}$.

The conjugate transpose satisfies $(A^{\mathsf H})^{\mathsf H}=A$, $(A+B)^{\mathsf H}=A^{\mathsf H}+B^{\mathsf H}$, $(kA)^{\mathsf H}=\bar kA^{\mathsf H}$ and $(AB)^{\mathsf H}=B^{\mathsf H}A^{\mathsf H}$; for a real matrix it is just the transpose. It plays over the complex field the role that the transpose plays over the reals, the key point being that for a complex vector $\boldsymbol{x}=[x_i]\neq\boldsymbol{0}$,

$$
\boldsymbol{x}^{\mathsf H}\boldsymbol{x}=\sum_i\bar x_ix_i=\sum_i|x_i|^2>0,
$$

whereas $\boldsymbol{x}^{\mathsf T}\boldsymbol{x}$ can vanish (e.g., $\boldsymbol{x}=[1\ \mathrm{i}]^{\mathsf T}$). This is why the standard inner product on $\mathbb{C}^n$ is taken to be $\langle\boldsymbol{x},\boldsymbol{y}\rangle=\boldsymbol{y}^{\mathsf H}\boldsymbol{x}$; see [Chapter 12](/2.1.12). The proof in [Chapter 7](/2.1.7) that the eigenvalues of a real symmetric matrix are real uses exactly this inequality.

**Definition 9.2.2 (Complex Vector Space)** A vector space over the complex field $\mathbb{C}$ (Definition 8.1.2 of [Chapter 8](/2.1.8) with $\mathbb{F}=\mathbb{C}$) is called a **complex vector space**.

A complex vector space can also be regarded as a real vector space by allowing only real scalars, and then its dimension doubles: $\dim_{\mathbb{C}}\mathbb{C}=1$ (basis $1$) and $\dim_{\mathbb{R}}\mathbb{C}=2$ (basis $1,\mathrm{i}$); $\dim_{\mathbb{C}}\mathbb{C}^2=2$, whereas as a real space $\mathbb{C}^2$ has the basis $[1\ 0]^{\mathsf T},[0\ 1]^{\mathsf T},[\mathrm{i}\ 0]^{\mathsf T},[0\ \mathrm{i}]^{\mathsf T}$ and $\dim_{\mathbb{R}}\mathbb{C}^2=4$. In general $\dim_{\mathbb{R}}V=2\dim_{\mathbb{C}}V$.

Linear transformations of complex vector spaces relate to matrices exactly as in Chapter 8: $T\colon \mathbb{C}^n\to\mathbb{C}^n$ is a linear transformation if and only if $T(\boldsymbol{x})=A\boldsymbol{x}$ for some $A\in\mathbb{C}^{n\times n}$; with respect to a basis $\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_n$, $T(\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_n)=(\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_n)A$, where the $k$-th column of $A$ is the coordinate vector of $T(\boldsymbol{\alpha}_k)$; and after the change of basis $(\boldsymbol{\beta}_1,\dots,\boldsymbol{\beta}_n)=(\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_n)P$ the matrix becomes $P^{-1}AP$ (Theorem 8.7.3). Thus a linear transformation corresponds to a similarity class $\{P^{-1}AP\mid P\text{ invertible}\}$, and "deciding whether two matrices are similar" means "deciding whether one linear transformation has two bases giving these matrices" (Theorem 8.7.4).

**Example 9.2.1** Decide whether $A=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}$ and $B=\begin{bmatrix}0&0&0\\1&0&0\\2&3&0\end{bmatrix}$ are similar. Both have characteristic polynomial $\lambda^3$ and neither is diagonalizable, so eigenvalues do not settle the question. Let $T(\boldsymbol{x})=A\boldsymbol{x}$; then $T(\boldsymbol{e}_1)=\boldsymbol{0}$, $T(\boldsymbol{e}_2)=\boldsymbol{e}_1$, $T(\boldsymbol{e}_3)=\boldsymbol{e}_2$. $A$ and $B$ are similar if and only if there is a basis $\boldsymbol{\beta}_1,\boldsymbol{\beta}_2,\boldsymbol{\beta}_3$ in which $T$ has matrix $B$, that is,

$$
T(\boldsymbol{\beta}_1)=\boldsymbol{\beta}_2+2\boldsymbol{\beta}_3,\qquad T(\boldsymbol{\beta}_2)=3\boldsymbol{\beta}_3,\qquad T(\boldsymbol{\beta}_3)=\boldsymbol{0}.
$$

Working backward from the last equation: take $\boldsymbol{\beta}_3=\boldsymbol{e}_1$; from $T(\boldsymbol{\beta}_2)=3\boldsymbol{e}_1$ take $\boldsymbol{\beta}_2=3\boldsymbol{e}_2$; from $T(\boldsymbol{\beta}_1)=3\boldsymbol{e}_2+2\boldsymbol{e}_1$ take $\boldsymbol{\beta}_1=2\boldsymbol{e}_2+3\boldsymbol{e}_3$. The change-of-basis matrix

$$
P=[\boldsymbol{\beta}_1\ \boldsymbol{\beta}_2\ \boldsymbol{\beta}_3]=\begin{bmatrix}0&0&1\\2&3&0\\3&0&0\end{bmatrix}
$$

is invertible ($\det P=-9$), so $B=P^{-1}AP$ and $A$ and $B$ are similar. This method of "working backward along the action of $T$ to obtain a chain of vectors" is developed into Jordan chains in [Chapter 10](/2.1.10), where we shall also see that similarity can be decided by comparing just the sequence of numbers $\operatorname{rank}(A-\lambda I)^k$.

**Example 9.2.2** Let $A=\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ and $T(\boldsymbol{x})=A\boldsymbol{x}$. Give $\mathbb{C}^2$ the standard inner product, so that $\boldsymbol{e}_1,\boldsymbol{e}_2$ is an orthonormal basis. Let $\boldsymbol{v}_1=\frac1{\sqrt2}[1\ {-\mathrm{i}}]^{\mathsf T}$ and $\boldsymbol{v}_2=\frac1{\sqrt2}[1\ \mathrm{i}]^{\mathsf T}$. Then $\boldsymbol{v}_1^{\mathsf H}\boldsymbol{v}_1=\boldsymbol{v}_2^{\mathsf H}\boldsymbol{v}_2=1$ and $\boldsymbol{v}_2^{\mathsf H}\boldsymbol{v}_1=0$, so this is also an orthonormal basis, and $A\boldsymbol{v}_1=(a+b\mathrm{i})\boldsymbol{v}_1$, $A\boldsymbol{v}_2=(a-b\mathrm{i})\boldsymbol{v}_2$. Hence the matrix of $T$ with respect to the orthonormal basis $\boldsymbol{v}_1,\boldsymbol{v}_2$ is $\operatorname{diag}(a+b\mathrm{i},a-b\mathrm{i})$: the real matrix $A$ cannot be diagonalized over $\mathbb{R}$, but it can be diagonalized over $\mathbb{C}$ by a "complex orthogonal matrix" (a unitary matrix).

This points to several goals of the advanced part of linear algebra, all of which extend properties of complex numbers to matrices:

| Complex numbers | Matrices | Chapter |
|---|---|---|
| Complete factorization of polynomials over $\mathbb{C}$ | Simplest form under similarity: the Jordan canonical form | [Chapter 10](/2.1.10) |
| Functions such as $\mathrm{e}^z$ | Matrix functions $\mathrm{e}^A$, systems of linear differential equations | [Chapter 11](/2.1.11) |
| Orthonormal bases of $\mathbb{R}^n$, orthogonal matrices, orthogonal similarity, real symmetric matrices | Orthonormal bases of $\mathbb{C}^n$, unitary matrices, unitary similarity, normal matrices | [Chapter 12](/2.1.12) |
| Real numbers $\bar z=z$, polar form $z=r\mathrm{e}^{\mathrm{i}\theta}$ | Hermitian matrices $A^{\mathsf H}=A$, polar decomposition $A=R\mathrm{e}^{\mathrm{i}M}$ | [Chapter 13](/2.1.13) |

## 9.3. Polynomials in One Variable and Division with Remainder

### 9.3.1. Polynomials over a Number Field

The coefficients of a polynomial are taken from a **number field** $\mathbb{F}$ (Definition 8.1.1 of [Chapter 8](/2.1.8)). Besides $\mathbb{Q},\mathbb{R},\mathbb{C}$ there are many intermediate number fields. For example, $\mathbb{Q}(\sqrt2)=\{a+b\sqrt2\mid a,b\in\mathbb{Q}\}$ is a number field: it is clearly closed under addition, subtraction and multiplication, and for $a+b\sqrt2\neq0$ we have $\dfrac1{a+b\sqrt2}=\dfrac{a-b\sqrt2}{a^2-2b^2}\in\mathbb{Q}(\sqrt2)$ ($a^2-2b^2\neq0$ because $\sqrt2$ is irrational). But $\{a+b\sqrt2+c\sqrt3\mid a,b,c\in\mathbb{Q}\}$ is not a number field, since $\sqrt2\cdot\sqrt3=\sqrt6$ does not belong to it; adding $\sqrt6$ gives $\mathbb{Q}(\sqrt2,\sqrt3)=\{a+b\sqrt2+c\sqrt3+d\sqrt6\}$, which is a number field (closure under multiplication is checked by expanding; to invert an element, first multiply by its "conjugate" with the sign of $\sqrt3$ changed, which yields an element of $\mathbb{Q}(\sqrt2)$, and then use the formula above). The positive reals and the integers are not number fields.

**Definition 9.3.1 (Polynomial)** Let $\mathbb{F}$ be a number field and $x$ an indeterminate. An expression of the form $f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$ ($a_i\in \mathbb{F}$) is called a **polynomial** (in one variable) over $\mathbb{F}$. When $a_n\neq0$, $a_nx^n$ is called the leading term, $a_n$ the leading coefficient, and $n$ the degree of $f$, written $\deg f$; $a_0$ is called the constant term. A polynomial with leading coefficient $1$ is called a **monic polynomial**. The polynomial whose coefficients are all zero is called the zero polynomial, and its degree is left undefined. The set of all polynomials over $\mathbb{F}$ is written $\mathbb{F}[x]$.

Two polynomials are equal when all their corresponding coefficients are equal. Numbers in $\mathbb{F}$ can be substituted for $x$, and so can square matrices over $\mathbb{F}$: for $f(x)=x^2+2x-3$ and a square matrix $A$, $f(A)=A^2+2A-3I$. The latter is the starting point of matrix functions (Chapter 11).

Addition and multiplication in $\mathbb{F}[x]$ follow the usual rules: if $f=\sum_{i=0}^na_ix^i$ and $g=\sum_{j=0}^mb_jx^j$, then $fg=\sum_{l=0}^{n+m}\big(\sum_{i+j=l}a_ib_j\big)x^l$. For nonzero polynomials (whenever defined)

$$
\deg(f+g)\le\max\{\deg f,\deg g\},\qquad \deg(fg)=\deg f+\deg g,
$$

the latter because the leading term of $fg$ is $a_nb_mx^{n+m}$ with $a_nb_m\neq0$. Hence $\mathbb{F}[x]$ has no zero divisors and is an integral domain, and only the nonzero constants are invertible, just as only $\pm1$ are invertible in $\mathbb{Z}$. $\mathbb{F}[x]$ is also an infinite-dimensional vector space over $\mathbb{F}$ (Example 8.3.3 of Chapter 8).

### 9.3.2. Division with Remainder and Divisibility

Polynomials generally cannot be divided: $(x^2+1)\div(x+2)$ is not a polynomial. Imitating $9=4\times2+1$ for integers, we have division with remainder.

**Theorem 9.3.1 (Division with Remainder)** Let $f,g\in \mathbb{F}[x]$ with $g\neq0$. Then there are unique $q,r\in \mathbb{F}[x]$ such that

$$
f=qg+r,\qquad r=0\ \text{or}\ \deg r<\deg g.
$$

$q$ and $r$ are called the quotient and the remainder of $f$ divided by $g$.

**Proof** Existence: if $f=0$ or $\deg f<\deg g$, take $q=0$, $r=f$. Otherwise let the leading terms of $f,g$ be $a_nx^n$ and $b_mx^m$ ($n\ge m$); then $f_1=f-\frac{a_n}{b_m}x^{n-m}g$ is zero or of degree less than $n$, and induction on $\deg f$ completes the argument. Uniqueness: if $q_1g+r_1=q_2g+r_2$, then $(q_1-q_2)g=r_2-r_1$; if $q_1\neq q_2$, the left side has degree $\ge\deg g$ while the right side is zero or of degree $<\deg g$, a contradiction. So $q_1=q_2$ and $r_1=r_2$. $\square$

The existence proof is just long division: each step uses the leading term to cancel the leading term of the current dividend. The whole process uses only the four arithmetic operations in $\mathbb{F}$, so the quotient and remainder lie in $\mathbb{F}[x]$ and do not change when $\mathbb{F}$ is replaced by a larger number field; the number of multiplications is about $(\deg f-\deg g+1)(\deg g+1)$.

**Example 9.3.1** $6x^4-9x^2+18=(6x^2+9)(x^2-3)+45$; $x^5-x^3+3x^2-1=(x^2+2)(x^3-3x+2)+(x^2+6x-5)$.

**Definition 9.3.2 (Divisibility)** Let $f,g\in \mathbb{F}[x]$. If there is $h\in \mathbb{F}[x]$ with $f=gh$, we say that $g$ **divides** $f$, written $g\mid f$, and call $g$ a factor of $f$. For $g\neq0$, $g\mid f$ if and only if the remainder of $f$ divided by $g$ is zero.

Basic properties of divisibility:

- if $f\mid g$ and $g\mid f$ ($f,g\neq0$), then $f=cg$ for a nonzero constant $c$ (we then call $f,g$ associates): from $f=gh$ and $g=fk$ we get $f=fkh$, so $\deg(kh)=0$;
- if $f\mid g_1$ and $f\mid g_2$, then $f\mid g_1h_1+g_2h_2$ for all $h_1,h_2\in \mathbb{F}[x]$;
- divisibility does not change when the number field is enlarged: if $f,g\in \mathbb{F}[x]$ and $\mathbb{F}\subseteq \mathbb{K}$, then $g\mid f$ in $\mathbb{K}[x]$ if and only if $g\mid f$ in $\mathbb{F}[x]$ (the result of division with remainder does not depend on the field).

## 9.4. The Remainder Theorem, Synthetic Division and Interpolation

### 9.4.1. The Remainder Theorem and Synthetic Division

When the divisor is a linear polynomial $x-a$, the remainder is a constant. Substituting $x=a$ into $f(x)=q(x)(x-a)+r$ gives $r=f(a)$.

**Theorem 9.4.1 (Remainder Theorem)** Let $f\in \mathbb{F}[x]$ and $a\in \mathbb{F}$. Then the remainder of $f$ divided by $x-a$ is $f(a)$. In particular, $(x-a)\mid f$ if and only if $f(a)=0$.

Let $f=a_nx^n+\cdots+a_1x+a_0$ and $q=b_{n-1}x^{n-1}+\cdots+b_0$. Comparing coefficients on both sides of $f=q(x-a)+r$ gives recurrences for the quotient and remainder:

**Algorithm 9.4.1 (Synthetic Division)** Input: $f=a_nx^n+\cdots+a_0$ and $a\in \mathbb{F}$.

1. $b_{n-1}=a_n$;
2. for $k=n-1,n-2,\dots,1$, compute $b_{k-1}=a_k+ab_k$;
3. $r=a_0+ab_0$.

Output: the quotient $q=b_{n-1}x^{n-1}+\cdots+b_0$ and the remainder $r=f(a)$. By hand one arranges three rows: the first row holds the coefficients of $f$, the third row produces the $b_k$ one at a time from left to right, and each $b_k$ times $a$ is written in the second row under the next column and added to the first row.

As an evaluation algorithm, synthetic division is Horner's method:

$$
f(a)=\big(\cdots\big((a_na+a_{n-1})a+a_{n-2}\big)a+\cdots+a_1\big)a+a_0,
$$

which needs only $n$ multiplications and $n$ additions. Computing each term $a_ka^k$ separately takes about $\frac{n(n+1)}2$ multiplications, and even accumulating the powers $a^k=a\cdot a^{k-1}$ takes $2n-1$. One can prove that for a general polynomial, $n$ multiplications is the minimum (Ostrowski, Pan).

**Example 9.4.1** Divide $f=4x^4-6x^3+x+\frac12$ by $x+\frac12=x-(-\frac12)$:

| | $4$ | $-6$ | $0$ | $1$ | $\frac12$ |
|---|---|---|---|---|---|
| $\times(-\frac12)$ | | $-2$ | $4$ | $-2$ | $\frac12$ |
| | $4$ | $-8$ | $4$ | $-1$ | $1$ |

So $q=4x^3-8x^2+4x-1$ and $r=f(-\frac12)=1$.

**Example 9.4.2 (Expansion in Powers of $x-a$)** Write $f=x^4-2x^3+3$ as $\sum_kb_k(x-2)^k$. From $f=(x-2)q_1+b_0$, $q_1=(x-2)q_2+b_1$, and so on, repeated synthetic division by $x-2$ yields the remainders $b_0=3$, $b_1=8$, $b_2=12$, $b_3=6$, $b_4=1$ in turn, that is,

$$
x^4-2x^3+3=(x-2)^4+6(x-2)^3+12(x-2)^2+8(x-2)+3.
$$

By Taylor's formula, $b_k=f^{(k)}(2)/k!$; these are the coordinates of $f$ with respect to the basis $1,x-2,\dots,(x-2)^{n-1}$ in Example 8.5.2 of [Chapter 8](/2.1.8), but here we need neither derivatives nor the inverse of a change-of-basis matrix, only $\frac{n(n+1)}2$ multiplications.

```python
from fractions import Fraction

def synthetic_division(coeffs, a):
    """Divide f by (x - a); coeffs = [a_n, ..., a_1, a_0].
    Returns (quotient coefficients, remainder f(a)). Uses n multiplications."""
    b = [coeffs[0]]
    for c in coeffs[1:]:
        b.append(c + a * b[-1])
    return b[:-1], b[-1]

def taylor_shift(coeffs, a):
    """Coefficients of f in powers of (x - a), lowest degree first,
    by repeated synthetic division (n(n+1)/2 multiplications)."""
    out = []
    while coeffs:
        coeffs, rem = synthetic_division(coeffs, a)
        out.append(rem)
    return out

f = [4, -6, 0, 1, Fraction(1, 2)]          # 4x^4 - 6x^3 + x + 1/2
print(synthetic_division(f, Fraction(-1, 2)))   # quotient [4, -8, 4, -1], remainder 1
print(taylor_shift([1, -2, 0, 0, 3], 2))   # [3, 8, 12, 6, 1]
```

### 9.4.2. Roots and Multiple Roots

If $a\in \mathbb{F}$ satisfies $f(a)=0$, then $a$ is called a root (zero) of $f$ in $\mathbb{F}$. Roots depend on the field: $x^2+1\in\mathbb{Q}[x]$ has no root in $\mathbb{Q}$. By the remainder theorem, $a$ is a root if and only if $(x-a)\mid f$.

**Definition 9.4.1 (Multiple Root)** Let $f\neq0$, $a\in \mathbb{F}$ and $k\ge1$. If $(x-a)^k\mid f$ but $(x-a)^{k+1}\nmid f$, then $a$ is called a root of multiplicity $k$ of $f$; for $k=1$ it is called a simple root, and for $k\ge2$ a **multiple root**.

**Proposition 9.4.1**

1. A polynomial of degree $n$ has at most $n$ roots in $\mathbb{F}$ (counted with multiplicity).
2. If $\deg f\le n$, $\deg g\le n$ and $f(x_i)=g(x_i)$ at $n+1$ distinct numbers, then $f=g$.
3. $a$ is a multiple root of $f$ if and only if $f(a)=f'(a)=0$. Here $f'$ is the formal derivative: $(\sum a_kx^k)'=\sum ka_kx^{k-1}$.

**Proof** 1: induction on $n$. If $a$ is a root, $f=(x-a)f_1$ with $\deg f_1=n-1$, and every other root of $f$ is a root of $f_1$ (for $b\neq a$, $(b-a)f_1(b)=0$ implies $f_1(b)=0$). 2: if $h=f-g$ were nonzero, it would have degree $\le n$ and $n+1$ roots, contradicting 1. 3: write $f=(x-a)^kg$ with $g(a)\neq0$ and $k\ge1$; then $f'=(x-a)^{k-1}\big(kg+(x-a)g'\big)$, and $kg(a)+0\neq0$, so $f'(a)=0$ if and only if $k\ge2$. $\square$

### 9.4.3. Interpolation

Given $n+1$ points $(a_0,b_0),\dots,(a_n,b_n)$ in $\mathbb{F}$ with distinct $a_i$, we seek a polynomial $L$ of degree at most $n$ with $L(a_i)=b_i$. By part 2 of Proposition 9.4.1 there is at most one such $L$. There are two ways to establish existence:

1. Solve a linear system: substituting $L=c_0+c_1x+\cdots+c_nx^n$ gives a system whose coefficient matrix is a **Vandermonde matrix**, which is invertible ([Chapter 5](/2.1.5)); this is the existence and uniqueness of **polynomial interpolation**. But solving it by Gaussian elimination takes $O(n^3)$ operations, and Vandermonde matrices are usually very ill-conditioned.
2. Construct it directly by the Lagrange formula below, which takes only $O(n^2)$ operations.

**Theorem 9.4.2 (Lagrange Interpolation Polynomial)** Let

$$
L_i(x)=\prod_{j\neq i}\frac{x-a_j}{a_i-a_j}=\frac{(x-a_0)\cdots(x-a_{i-1})(x-a_{i+1})\cdots(x-a_n)}{(a_i-a_0)\cdots(a_i-a_{i-1})(a_i-a_{i+1})\cdots(a_i-a_n)}.
$$

Then $L_i(a_j)=\delta_{ij}$, and $L(x)=b_0L_0(x)+b_1L_1(x)+\cdots+b_nL_n(x)$ is the unique polynomial of degree at most $n$ with $L(a_i)=b_i$, called the Lagrange interpolation polynomial.

**Proof** The numerator of $L_i$ vanishes at $a_j$ ($j\neq i$) and equals the denominator at $a_i$, so $L_i(a_j)=\delta_{ij}$ and $L(a_j)=\sum_ib_i\delta_{ij}=b_j$; and $\deg L\le n$. Uniqueness was shown above. $\square$

$L_0,\dots,L_n$ is a basis of $\mathbb{F}[x]_{n+1}$, and the coordinates of $L$ with respect to it are $(b_0,\dots,b_n)$; moreover, $L_0,\dots,L_n$ are precisely the preimages of the standard basis vectors $\boldsymbol{e}_i$ under the evaluation map $p\mapsto(p(a_0),\dots,p(a_n))$ of Chapter 8. In the language of remainders, the interpolation problem asks for $L$ of degree $\le n$ whose remainder on division by $x-a_i$ is $b_i$ ($i=0,\dots,n$), a special case of the Chinese remainder theorem for polynomials. [Chapter 11](/2.1.11) also requires derivative values to match, leading to Hermite interpolation, which is used to compute matrix functions.

Although the interpolation polynomial is unique, how well it approximates a function depends on the choice of nodes. Interpolating $f(x)=\frac1{1+25x^2}$ on $[-1,1]$ at equispaced nodes, the oscillations near the two ends of the interval grow more violent as the degree increases, and the interpolation polynomials do not converge to $f$; this is called the *Runge phenomenon*. With the Chebyshev nodes $\cos\frac{(2k+1)\pi}{2n+2}$ ($k=0,\dots,n$), which cluster toward the ends, the interpolation polynomials converge uniformly to $f$.

![Lagrange interpolation of the Runge function 1/(1+25x^2): on the left, with equispaced nodes, the oscillations near the endpoints grow as the degree increases; on the right, with Chebyshev nodes, the interpolation polynomials converge to the function as the degree increases](./plots/lagrange-runge.py)

**Example 9.4.3** Find the monic quadratic polynomial $f$ that leaves remainder $1$ on division by $x-1$ and remainder $2$ on division by $x-2$. By the remainder theorem $f(1)=1$ and $f(2)=2$, so $f(x)-x$ is the monic quadratic with roots $1,2$: $f=x+(x-1)(x-2)=x^2-2x+2$.

## 9.5. Greatest Common Divisors and the Euclidean Algorithm

**Definition 9.5.1 (Greatest Common Divisor)** Let $f,g\in \mathbb{F}[x]$. If $d\in \mathbb{F}[x]$ satisfies $d\mid f$ and $d\mid g$, and every common factor of $f,g$ divides $d$, then $d$ is called a **greatest common divisor** of $f$ and $g$.

If $d,d'$ are both greatest common divisors, then $d\mid d'$ and $d'\mid d$, so they differ only by a nonzero constant factor. When $f,g$ are not both zero, $(f,g)$ denotes the greatest common divisor with leading coefficient $1$; $(f,0)$ is $f$ divided by its leading coefficient, and $(0,0)=0$. Existence is provided by the Euclidean algorithm, which rests on the following lemma.

**Lemma 9.5.1** If $f=qg+r$, then $f,g$ and $g,r$ have the same common factors, so $(f,g)=(g,r)$.

**Proof** This follows from $r=f-qg$, $f=qg+r$ and the combination property of divisibility. $\square$

**Algorithm 9.5.1 (Euclidean Algorithm)** Input: $f,g\in \mathbb{F}[x]$ with $g\neq0$. Let $r_{-1}=f$ and $r_0=g$; for $k=0,1,2,\dots$, as long as $r_k\neq0$, divide with remainder: $r_{k-1}=q_{k+1}r_k+r_{k+1}$. Since $\deg r_0>\deg r_1>\deg r_2>\cdots$, after finitely many steps $r_{s+1}=0$. By Lemma 9.5.1,

$$
(f,g)=(g,r_1)=(r_1,r_2)=\cdots=(r_{s-1},r_s)=(r_s,0),
$$

so the last nonzero remainder $r_s$ divided by its leading coefficient is $(f,g)$.

**Example 9.5.1** Find the greatest common divisor of $f=x^4+x^3-x^2-2x+1$ and $g=x^3+2x^2-3$:

$$
\begin{aligned}
f&=(x-1)g+(x^2+x-2),\\
g&=(x+1)(x^2+x-2)+(x-1),\\
x^2+x-2&=(x+2)(x-1),
\end{aligned}
$$

so $(f,g)=x-1$.

The Euclidean algorithm uses only the four arithmetic operations in $\mathbb{F}$, so the greatest common divisor does not depend on the choice of field: for $f,g\in\mathbb{Q}[x]$, the greatest common divisor in $\mathbb{Q}[x]$ is the same as in $\mathbb{C}[x]$. This matters: we can decide whether two polynomials have a common root without knowing their roots.

**Theorem 9.5.1 (Bézout's Identity)** Let $f,g\in \mathbb{F}[x]$. Then there are $u,v\in \mathbb{F}[x]$ such that

$$
(f,g)=uf+vg.
$$

**Proof** In Algorithm 9.5.1, $r_s=r_{s-2}-q_sr_{s-1}$, and $r_{s-1}=r_{s-3}-q_{s-1}r_{s-2}$, and so on; substituting successively from the bottom up writes $r_s$ as a combination of $f$ and $g$, and we then divide by the leading coefficient of $r_s$. The case $f=g=0$ is trivial. $\square$

**Algorithm 9.5.2 (Extended Euclidean Algorithm)** In Algorithm 9.5.1, maintain $u_k,v_k$ with $r_k=u_kf+v_kg$: $u_{-1}=1$, $v_{-1}=0$, $u_0=0$, $v_0=1$, and at each step $u_{k+1}=u_{k-1}-q_{k+1}u_k$, $v_{k+1}=v_{k-1}-q_{k+1}v_k$. Finally $r_s=u_sf+v_sg$. This gives the same result as back-substitution but does not require storing all the quotients.

**Example 9.5.2** For Example 9.5.1, using the second and then the first equation,

$$
x-1=g-(x+1)(x^2+x-2)=g-(x+1)\big(f-(x-1)g\big)=-(x+1)f+x^2g.
$$

**Example 9.5.3** Let $f=x^4+2x^3-x^2-4x-2$ and $g=x^4+x^3-x^2-2x-2$. Then $f=g+(x^3-2x)$, $g=(x+1)(x^3-2x)+(x^2-2)$ and $x^3-2x=x(x^2-2)$, so $(f,g)=x^2-2$, and

$$
x^2-2=g-(x+1)(f-g)=-(x+1)f+(x+2)g.
$$

$u,v$ are not unique: $u'=u+\frac gd$, $v'=v-\frac fd$ ($d=(f,g)\neq0$) also satisfy $u'f+v'g=d$. Also, $uf+vg=h$ does not in general imply that $h$ is a greatest common divisor (e.g., $1\cdot x+(-1)\cdot x=0$), but it does when $h=1$; this is the coprimality criterion of the next section. In the language of 1.3.3, $\{uf+vg\mid u,v\in \mathbb{F}[x]\}$ is an **ideal** of $\mathbb{F}[x]$, and Bézout's identity says that it is generated by $(f,g)$: every ideal of $\mathbb{F}[x]$ is generated by a single polynomial.

## 9.6. Coprimality

**Definition 9.6.1 (Coprime Polynomials)** If $(f,g)=1$, then $f$ and $g$ are said to be **coprime**.

For example, $x-c_1$ and $x-c_2$ are coprime when $c_1\neq c_2$: $\frac{1}{c_2-c_1}\big((x-c_1)-(x-c_2)\big)=1$.

**Theorem 9.6.1** $f,g$ are coprime if and only if there are $u,v\in \mathbb{F}[x]$ with $uf+vg=1$.

**Proof** Necessity is Bézout's identity. Sufficiency: if $c\mid f$ and $c\mid g$, then $c\mid uf+vg=1$, so $c$ is a nonzero constant and $(f,g)=1$. $\square$

**Proposition 9.6.1** Let $f,g,h,f_1,f_2\in \mathbb{F}[x]$.

1. If $f_1\mid g$, $f_2\mid g$ and $(f_1,f_2)=1$, then $f_1f_2\mid g$;
2. if $(f,g)=1$ and $f\mid gh$, then $f\mid h$;
3. if $d=(f,g)\neq0$, then $\big(\frac fd,\frac gd\big)=1$;
4. if $t$ is monic, then $(tf,tg)=t\,(f,g)$;
5. if $(f_1,g)=(f_2,g)=1$, then $(f_1f_2,g)=1$.

**Proof** 1: $g=f_1q_1=f_2q_2$, and from $uf_1+vf_2=1$, $g=ugf_1+vgf_2=uf_2q_2f_1+vf_1q_1f_2$ is divisible by $f_1f_2$. 2: from $uf+vg=1$, $h=ufh+vgh$, and both terms are divisible by $f$. 3: divide $d=uf+vg$ by $d$ to get $u\frac fd+v\frac gd=1$. 4: from $d=uf+vg$ we get $td=u(tf)+v(tg)$, and $td$ is a monic common factor of $tf,tg$ divisible by every common factor, hence their greatest common divisor. 5: multiply $u_1f_1+v_1g=1$ and $u_2f_2+v_2g=1$ to get $(u_1u_2)f_1f_2+(u_1f_1v_2+v_1u_2f_2+v_1v_2g)g=1$. $\square$

**Example 9.6.1** Prove that $x^3-1\mid x^{3k}-1$. We have $x^3-1=(x-1)(x-\omega)(x-\omega^2)$ with $\omega=\mathrm{e}^{2\pi\mathrm{i}/3}$, and the three factors are pairwise coprime. $f=x^{3k}-1$ satisfies $f(1)=0$, $f(\omega)=\omega^{3k}-1=0$ and $f(\omega^2)=0$, so by the remainder theorem each factor divides $f$, and by part 1 of Proposition 9.6.1 so does their product. Since divisibility does not depend on the field, this holds in $\mathbb{Q}[x]$ as well.

**Example 9.6.2** If $(f,g)=1$, then $(fh,g)=(h,g)$ for every $h$. Let $d=(fh,g)$ and $d_1=(h,g)$. Since $d_1\mid h$ and $d_1\mid g$, we have $d_1\mid fh$ and hence $d_1\mid d$. Conversely, $(d,f)$ divides both $f$ and $g$ (because $d\mid g$), so $(d,f)=1$; from $d\mid fh$ and part 2 of Proposition 9.6.1, $d\mid h$, and hence $d\mid d_1$. Both are monic, so $d=d_1$.

## 9.7. Irreducible Polynomials and Factorization

**Definition 9.7.1 (Irreducible Polynomial)** Let $f\in \mathbb{F}[x]$ with $\deg f\ge1$. If there are no $f_1,f_2\in \mathbb{F}[x]$ with $\deg f_1\ge1$, $\deg f_2\ge1$ and $f=f_1f_2$, then $f$ is called an **irreducible polynomial** over $\mathbb{F}$; otherwise $f$ is reducible over $\mathbb{F}$.

Irreducible polynomials are the "primes" among polynomials: their only factors are nonzero constants $c$ and $cf$. Linear polynomials are always irreducible. Irreducibility depends on the field: $x^2-2$ is irreducible over $\mathbb{Q}$, while over $\mathbb{R}$, $x^2-2=(x-\sqrt2)(x+\sqrt2)$.

**Proposition 9.7.1** Let $p\in \mathbb{F}[x]$ be irreducible over $\mathbb{F}$.

1. For a nonzero constant $c$, $cp$ is also irreducible;
2. if $\mathbb{F}\subseteq \mathbb{K}$ are number fields and $p\in \mathbb{F}[x]$ is irreducible over $\mathbb{K}$, then it is irreducible over $\mathbb{F}$;
3. for every $g\in \mathbb{F}[x]$, either $(p,g)=1$ or $p\mid g$;
4. if $p\mid gh$, then $p\mid g$ or $p\mid h$.

**Proof** 1 and 2 follow from the definition. 3: $(p,g)$ is a monic factor of $p$, so it is either $1$ or $p$ divided by its leading coefficient. 4: if $p\nmid g$, then $(p,g)=1$ by 3, and $p\mid h$ by part 2 of Proposition 9.6.1. $\square$

**Theorem 9.7.1 (Unique Factorization Theorem)** Let $f\in \mathbb{F}[x]$ with $\deg f\ge1$. Then

1. $f$ can be written as a product of finitely many irreducible polynomials over $\mathbb{F}$;
2. if $f=p_1p_2\cdots p_s=q_1q_2\cdots q_t$ are two such factorizations, then $s=t$ and, after suitable reordering, $p_i=c_iq_i$ with nonzero constants $c_i$.

**Proof** Existence: induction on $\deg f$. If $f$ is irreducible we are done; otherwise $f=f_1f_2$ with $1\le\deg f_i<\deg f$, and we apply the induction hypothesis to $f_1,f_2$. Uniqueness: induction on $s$. Since $p_1\mid q_1\cdots q_t$, part 4 of Proposition 9.7.1 (extended to several factors) shows that $p_1$ divides some $q_j$, say $j=1$; as $q_1$ is irreducible, $q_1=c_1'p_1$. Cancelling $p_1$ gives $p_2\cdots p_s=c_1'q_2\cdots q_t$, and we apply the induction hypothesis. $\square$

Pulling out the leading coefficient of each irreducible factor and combining equal factors gives the standard factorization of $f$:

$$
f=c\,p_1^{e_1}p_2^{e_2}\cdots p_s^{e_s},
$$

where $c$ is the leading coefficient of $f$, the $p_i$ are distinct monic irreducible polynomials, and $e_i\ge1$ is called the multiplicity of $p_i$. If $f=c\prod p_i^{e_i}$ and $g=c'\prod p_i^{f_i}$ ($e_i,f_i\ge0$), then $(f,g)=\prod p_i^{\min\{e_i,f_i\}}$. Computing the greatest common divisor from standard factorizations, however, requires factoring first, which is itself hard; the Euclidean algorithm needs no factorization.

Theorem 9.7.1 says that $\mathbb{F}[x]$, like $\mathbb{Z}$, has unique factorization. In the language of ring theory ([1.3.3](/1.3.3)): $p$ is irreducible if and only if the ideal $(p)$ it generates is maximal, if and only if the quotient ring $\mathbb{F}[x]/(p)$ is a field; for example, $\mathbb{R}[x]/(x^2+1)\cong\mathbb{C}$. The remaining question is: given $f$, how do we decide whether it is irreducible over $\mathbb{F}$? The answer depends heavily on $\mathbb{F}$.

## 9.8. Factorization over the Complex, Real and Rational Fields

### 9.8.1. Polynomials with Complex Coefficients

**Theorem 9.8.1 (Fundamental Theorem of Algebra)** Every polynomial of degree at least $1$ with complex coefficients has at least one root in $\mathbb{C}$.

This theorem was already used in [Chapter 6](/2.1.6) to guarantee that complex matrices have eigenvalues. Its proof requires tools from analysis (the shortest proof uses Liouville's theorem from complex analysis) and is not given here. The remainder theorem and induction immediately give:

**Corollary 9.8.1** The irreducible polynomials in $\mathbb{C}[x]$ are exactly the linear polynomials. Every polynomial of degree $n$ with complex coefficients factors as

$$
f=c(x-\lambda_1)^{n_1}(x-\lambda_2)^{n_2}\cdots(x-\lambda_s)^{n_s},\qquad n_1+\cdots+n_s=n,
$$

with the $\lambda_i$ distinct, so $f$ has exactly $n$ roots in $\mathbb{C}$ (counted with multiplicity).

**Proposition 9.8.1** Let $f\in \mathbb{F}[x]$ with $\deg f\ge1$. Then $f$ has no multiple roots in $\mathbb{C}$ if and only if $(f,f')=1$.

**Proof** If $a\in\mathbb{C}$ is a multiple root, then by part 3 of Proposition 9.4.1, $x-a$ is a common factor of $f$ and $f'$, so $(f,f')\neq1$. Conversely, if $d=(f,f')$ has degree $\ge1$, then by the fundamental theorem of algebra $d$ has a complex root $a$, and $f(a)=f'(a)=0$, so $a$ is a multiple root. $\square$

Since the greatest common divisor does not depend on the field, testing for multiple roots requires only the Euclidean algorithm applied to $f$ and $f'$ in $\mathbb{F}[x]$, without finding any roots. [Chapter 10](/2.1.10) uses this to decide whether a matrix is diagonalizable: a matrix is diagonalizable if and only if its minimal polynomial has no multiple roots.

### 9.8.2. Polynomials with Real Coefficients

**Lemma 9.8.1** Let $f\in\mathbb{R}[x]$ and $z\in\mathbb{C}$. If $f(z)=0$, then $f(\bar z)=0$, and $z$ and $\bar z$ have the same multiplicity.

**Proof** The coefficients of $f$ are real, so conjugating $f(z)=\sum a_kz^k=0$ gives $f(\bar z)=\sum a_k\bar z^k=0$. Multiplicity: induction on $\deg f$. Let $z\notin\mathbb{R}$ be a root. Then $g=(x-z)(x-\bar z)$ is a real polynomial, and its two linear factors are coprime and both divide $f$, so $g\mid f$; division with remainder takes place in $\mathbb{R}[x]$, so the quotient $h=f/g$ again has real coefficients. The multiplicities of $z$ and $\bar z$ in $f$ each exceed those in $h$ by $1$, and the induction hypothesis applied to $h$ finishes the proof. $\square$

If $z=a+b\mathrm{i}$ with $b\neq0$, then

$$
(x-z)(x-\bar z)=x^2-(z+\bar z)x+z\bar z=x^2-2ax+(a^2+b^2)
$$

is a real quadratic with discriminant $-4b^2<0$, irreducible over $\mathbb{R}$. Hence, by Corollary 9.8.1:

**Theorem 9.8.2** The irreducible polynomials in $\mathbb{R}[x]$ are exactly the linear polynomials and the quadratic polynomials $ax^2+bx+c$ with negative discriminant ($b^2-4ac<0$). Every polynomial with real coefficients factors as

$$
f=c\prod_{i=1}^s(x-a_i)^{n_i}\prod_{j=1}^t(x^2+p_jx+q_j)^{m_j},\qquad p_j^2-4q_j<0.
$$

**Proof** Induction on $\deg f$. If $f$ has a real root $a$, split off $x-a$; otherwise take a complex root $z\notin\mathbb{R}$. By Lemma 9.8.1, $\bar z$ is also a root, and $(x-z)(x-\bar z)$ divides $f$ in $\mathbb{C}[x]$ (the two factors being coprime); since it is a real polynomial and divisibility does not depend on the field, it also divides $f$ in $\mathbb{R}[x]$. $\square$

In particular, a real polynomial of odd degree always has a real root, so a real matrix of odd order always has a real eigenvalue.

**Example 9.8.1** Is $x^4+2$ reducible over $\mathbb{R}$? Its complex roots are $\sqrt[4]2\,\mathrm{e}^{\mathrm{i}(2k+1)\pi/4}$ ($k=0,1,2,3$), which come in conjugate pairs. Combining each conjugate pair: $\mathrm{e}^{\mathrm{i}\pi/4}$ and $\mathrm{e}^{-\mathrm{i}\pi/4}$ give $x^2-2\sqrt[4]2\cos\frac\pi4\,x+\sqrt2=x^2-2^{3/4}x+\sqrt2$, and the other pair gives $x^2+2^{3/4}x+\sqrt2$, so

$$
x^4+2=\big(x^2-2^{3/4}x+\sqrt2\big)\big(x^2+2^{3/4}x+\sqrt2\big).
$$

The real factorization of $\lambda^4+1$ in the introduction is obtained in the same way. We see that every real polynomial of degree $\ge3$ is reducible.

### 9.8.3. Polynomials with Rational Coefficients

The situation in $\mathbb{Q}[x]$ is completely different: as we shall see, there are irreducible polynomials of every degree. Multiplying $f\in\mathbb{Q}[x]$ by a common multiple of the denominators of its coefficients turns it into a polynomial with integer coefficients without changing its roots or its reducibility, so it suffices to consider integer polynomials.

**Theorem 9.8.3 (Rational Root Theorem)** Let $f=a_nx^n+\cdots+a_1x+a_0\in\mathbb{Z}[x]$ with $a_n\neq0$. If a fraction $\frac rs$ in lowest terms ($r,s\in\mathbb{Z}$ coprime) is a root of $f$, then $r\mid a_0$ and $s\mid a_n$.

**Proof** From $f(\frac rs)=0$, multiplying by $s^n$ gives $a_nr^n+a_{n-1}r^{n-1}s+\cdots+a_1rs^{n-1}+a_0s^n=0$. Every term except the first is divisible by $s$, so $s\mid a_nr^n$; as $s$ and $r$ are coprime, $s\mid a_n$. Similarly $r\mid a_0s^n$, so $r\mid a_0$. $\square$

Finding rational roots thus takes only finitely many checks. For example, the only possible rational roots of $2x^3-3x^2-3x+2$ are $\pm1,\pm2,\pm\frac12$; substituting each (by synthetic division) yields the roots $-1,\frac12,2$, so $2x^3-3x^2-3x+2=(x+1)(2x-1)(x-2)$. As another example, the only possible rational roots of $x^5-12x^3+36x+12$ are $\pm1,\pm2,\pm3,\pm4,\pm6,\pm12$, and checking shows that none of them is a root, so it has no rational root.

A quadratic or cubic polynomial that is reducible must have a linear factor and hence a root; so it is irreducible over $\mathbb{F}$ if and only if it has no root in $\mathbb{F}$. For example, the only possible rational roots of $x^3-3x-1$ are $\pm1$, and $f(1)=-3$, $f(-1)=1$, so it is irreducible over $\mathbb{Q}$. For polynomials of degree four or more, however, having no rational root does not imply irreducibility: $(x^2-2)^2\in\mathbb{Q}[x]$ has no rational root but is obviously reducible. This calls for the following tools.

**Definition 9.8.1 (Primitive Polynomial)** An integer polynomial $g$ whose coefficients have greatest common divisor $\pm1$ is called a **primitive polynomial**.

Every nonzero rational polynomial can be written as $f=rg$ with $r\in\mathbb{Q}$ and $g$ primitive: first multiply by a common multiple of the denominators to get an integer polynomial, then pull out the greatest common divisor of the coefficients. This representation is unique up to sign (if $r_1g_1=r_2g_2$, then $r_1=\pm r_2$ and $g_1=\pm g_2$). For example, $4x^3+3x+2$ is primitive, while $8x^3+6x+4=2(4x^3+3x+2)$ is not.

**Theorem 9.8.4 (Gauss's Lemma)** The product of two primitive polynomials is primitive.

**Proof** Let $f=\sum a_ix^i$ and $g=\sum b_jx^j$ be primitive. If $h=fg$ were not primitive, some prime $p$ would divide all coefficients of $h$. Since $f$ is primitive, $p$ does not divide all of its coefficients; let $a_i$ be the first coefficient not divisible by $p$ ($p\mid a_0,\dots,a_{i-1}$), and similarly let $b_j$ be the first coefficient of $g$ not divisible by $p$. The coefficient of $x^{i+j}$ in $h$ is

$$
c_{i+j}=a_ib_j+(a_{i-1}b_{j+1}+a_{i-2}b_{j+2}+\cdots)+(a_{i+1}b_{j-1}+a_{i+2}b_{j-2}+\cdots),
$$

and every term in the parentheses contains one of $a_0,\dots,a_{i-1}$ or $b_0,\dots,b_{j-1}$ and is divisible by $p$; since also $p\mid c_{i+j}$, we get $p\mid a_ib_j$, so $p\mid a_i$ or $p\mid b_j$, a contradiction. $\square$

**Corollary 9.8.2** A nonzero integer polynomial $f$ factors in $\mathbb{Q}[x]$ into two polynomials of lower degree if and only if it factors in $\mathbb{Z}[x]$ into two integer polynomials of lower degree.

**Proof** Sufficiency is clear. Necessity: let $f=gh$ with $g,h\in\mathbb{Q}[x]$ and $\deg g,\deg h<\deg f$. Write $f=r_ff_1$, $g=r_gg_1$, $h=r_hh_1$ with $f_1,g_1,h_1$ primitive and $r_f\in\mathbb{Z}$ ($f$ has integer coefficients). Then $r_ff_1=r_gr_h\,g_1h_1$; by Gauss's lemma $g_1h_1$ is primitive, and by uniqueness of the representation $r_gr_h=\pm r_f\in\mathbb{Z}$, so $f=(\pm r_fg_1)h_1$ is a factorization over the integers. $\square$

**Theorem 9.8.5 (Eisenstein's Criterion)** Let $f=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0\in\mathbb{Z}[x]$. If there is a prime $p$ such that

1. $p\nmid a_n$;
2. $p\mid a_{n-1},\dots,a_1,a_0$;
3. $p^2\nmid a_0$,

then $f$ is irreducible over $\mathbb{Q}$.

**Proof** Suppose $f$ were reducible over $\mathbb{Q}$. By Corollary 9.8.2, $f=(b_lx^l+\cdots+b_0)(c_mx^m+\cdots+c_0)$ with $b_i,c_j\in\mathbb{Z}$, $l,m\ge1$ and $l+m=n$. Since $a_0=b_0c_0$, $p\mid a_0$ and $p^2\nmid a_0$, the prime $p$ divides exactly one of $b_0,c_0$; say $p\mid b_0$ and $p\nmid c_0$. From $a_n=b_lc_m$ and $p\nmid a_n$ we get $p\nmid b_l$. Let $b_k$ be the first $b$ not divisible by $p$ ($0<k\le l<n$). Then $a_k=b_kc_0+b_{k-1}c_1+\cdots+b_0c_k$, where every term on the right except $b_kc_0$ is divisible by $p$, while $p\nmid b_kc_0$; hence $p\nmid a_k$, contradicting condition 2. $\square$

**Example 9.8.2**

- For every $n\ge1$, $x^n+2$ is irreducible over $\mathbb{Q}$ (take $p=2$). So $\mathbb{Q}[x]$ has irreducible polynomials of every degree, in sharp contrast to $\mathbb{C}[x]$ and $\mathbb{R}[x]$.
- For the earlier $x^5-12x^3+36x+12$, take $p=3$: $3\nmid1$, $3$ divides $-12,36,12$, and $9\nmid12$, so it is irreducible over $\mathbb{Q}$. Having no rational root only shows that it has no linear factor; Eisenstein's criterion further excludes quadratic factors.
- Sometimes a substitution is needed first. Let $p$ be prime and $\Phi_p(x)=x^{p-1}+x^{p-2}+\cdots+x+1=\frac{x^p-1}{x-1}$ (its roots are the $p-1$ $p$-th roots of unity other than $1$). Setting $x=y+1$,
  $$
  \Phi_p(y+1)=\frac{(y+1)^p-1}{y}=y^{p-1}+\binom p1y^{p-2}+\cdots+\binom p{p-2}y+\binom p{p-1},
  $$
  where $p$ divides $\binom pi$ ($1\le i\le p-1$) and $p^2\nmid\binom p{p-1}=p$; so $\Phi_p(y+1)$ is irreducible, and hence $\Phi_p(x)$ is irreducible over $\mathbb{Q}$ (the substitution $f(x)\mapsto f(y+1)$ preserves products and degrees).

The irreducible polynomials over the three fields compare as follows:

| Field | Irreducible polynomials | How to decide |
|---|---|---|
| $\mathbb{C}$ | exactly the linear polynomials | fundamental theorem of algebra |
| $\mathbb{R}$ | linear polynomials; quadratics with negative discriminant | complex roots come in conjugate pairs |
| $\mathbb{Q}$ | exist in every degree | rational root theorem (excludes only linear factors), Gauss's lemma, Eisenstein's criterion |

## 9.9. Relations Between Roots and Coefficients

**Theorem 9.9.1 (Vieta's Formulas)** Let $f=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0\in \mathbb{F}[x]$ with $a_n\neq0$, and let $x_1,\dots,x_n$ be its $n$ roots in $\mathbb{C}$ (counted with multiplicity). Then

$$
\begin{aligned}
x_1+x_2+\cdots+x_n&=-\frac{a_{n-1}}{a_n},\\
\sum_{1\le i<j\le n}x_ix_j&=\frac{a_{n-2}}{a_n},\\
&\ \ \vdots\\
\sum_{1\le i_1<\cdots<i_k\le n}x_{i_1}x_{i_2}\cdots x_{i_k}&=(-1)^k\frac{a_{n-k}}{a_n},\\
&\ \ \vdots\\
x_1x_2\cdots x_n&=(-1)^n\frac{a_0}{a_n}.
\end{aligned}
$$

**Proof** By Corollary 9.8.1, $f=a_n(x-x_1)\cdots(x-x_n)$; expand the right side and compare the coefficients of $x^{n-k}$. $\square$

The left sides are the elementary symmetric polynomials of the roots. Applying Vieta's formulas to the characteristic polynomial $\det(\lambda I-A)$ gives the facts of [Chapter 6](/2.1.6) that the sum of the eigenvalues is the trace and their product is the determinant. Every symmetric polynomial in the roots can be written as a polynomial in the elementary symmetric polynomials (the fundamental theorem of symmetric polynomials), and can therefore be expressed directly in terms of the coefficients without finding the roots. The most important example is the discriminant.

**Definition 9.9.1 (Discriminant)** Let $f$ be a monic polynomial with roots $x_1,\dots,x_n$ in $\mathbb{C}$. The number

$$
D(f)=\prod_{1\le i<j\le n}(x_i-x_j)^2
$$

is called the **discriminant** of $f$.

$D(f)$ is a symmetric polynomial in the roots and hence a polynomial in the coefficients; $D(f)=0$ if and only if $f$ has a multiple root (consistent with Proposition 9.8.1). $D(f)$ is the square of a Vandermonde determinant: with $V=[x_j^{i-1}]_{n\times n}$, $D(f)=(\det V)^2=\det(VV^{\mathsf T})$, and the $(i,j)$ entry of $VV^{\mathsf T}$ is the power sum $s_{i+j-2}=\sum_kx_k^{i+j-2}$, which can be computed recursively from Vieta's formulas.

**Example 9.9.1** For the quadratic $x^2+bx+c$, $x_1+x_2=-b$ and $x_1x_2=c$, so $D=(x_1-x_2)^2=(x_1+x_2)^2-4x_1x_2=b^2-4c$. For a general $ax^2+bx+c$, $(x_1-x_2)^2=\frac{b^2-4ac}{a^2}$. With real coefficients: if $D>0$ there are two distinct real roots, if $D=0$ a double real root, and if $D<0$ a pair of conjugate complex roots.

**Example 9.9.2 (Discriminant of a Cubic)** Let $f=x^3+qx+r\in\mathbb{R}[x]$ (every cubic can be brought to this form by the shift $x\mapsto x-\frac{a_2}3$), with roots $x_1,x_2,x_3$. By Vieta's formulas, $x_1+x_2+x_3=0$, $\sum x_ix_j=q$ and $x_1x_2x_3=-r$. The power sums are $s_0=3$, $s_1=0$, $s_2=s_1^2-2q=-2q$; and from $x_k^3=-qx_k-r$ we get $s_3=-qs_1-3r=-3r$ and $s_4=-qs_2-rs_1=2q^2$. Therefore

$$
D=\det\begin{bmatrix}3&0&-2q\\0&-2q&-3r\\-2q&-3r&2q^2\end{bmatrix}=-4q^3-27r^2.
$$

The number of real roots is determined by the sign of $D$:

- if $f$ has one real root $c$ and a pair of conjugate complex roots $z,\bar z$ ($z=a+b\mathrm{i}$, $b\neq0$), then $(c-z)(c-\bar z)=|c-z|^2$ and $z-\bar z=2b\mathrm{i}$, so $D=|c-z|^4(2b\mathrm{i})^2=-4b^2|c-z|^4<0$;
- if all three roots are real, then $D\ge0$, with $D=0$ if and only if there is a multiple root.

Since complex roots of a real cubic come in pairs, these are the only two cases. Hence: if $D>0$ there are three distinct real roots, if $D=0$ there is a multiple root (and all roots are real), and if $D<0$ there are one real root and a pair of conjugate complex roots. For example, the discriminant $-4\cdot9^3-27r^2$ of $x^3+9x+r$ is negative for every real $r$, so it always has exactly one real root (which also follows from $f'=3x^2+9>0$, i.e., $f$ is strictly increasing); the discriminant of $x^3-3x-1$ is $108-27=81>0$, so it has three distinct real roots (all irrational, by §9.8.3).

Quadratic, cubic and quartic equations have formulas for their roots, but Abel and Galois proved that the general equation of degree five or higher has no solution in radicals. Consequently, eigenvalues of matrices are not computed by finding the characteristic polynomial and applying a formula, but directly by iterative algorithms (such as the QR algorithm); conversely, numerical software finds the roots of a polynomial precisely by computing the eigenvalues of its **companion matrix** (e.g., `numpy.roots`).

## Summary

The two threads of this chapter: the complex numbers form the number field over which every polynomial factors completely, and complex arithmetic can be realized by real $2\times2$ matrices; $\mathbb{F}[x]$, like the integers, has division with remainder, greatest common divisors and unique factorization, and all its basic operations have standardized algorithms.

| Topic | Core results | Algorithms and cost |
|---|---|---|
| Complex numbers | $z=a+b\mathrm{i}=r\mathrm{e}^{\mathrm{i}\theta}$; multiplication = rotation and scaling; $z\mapsto\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ is an injective ring homomorphism | compute $z^n$ in exponential form |
| Powers and roots | $z^{q/p}$ has $p$ values; $n$-th roots of unity $\mathrm{e}^{2k\pi\mathrm{i}/n}$ sum to zero | — |
| Complex matrices | $A^{\mathsf H}=\bar A^{\mathsf T}$, $\boldsymbol{x}^{\mathsf H}\boldsymbol{x}>0$; complex vector spaces $\dim_{\mathbb{R}}V=2\dim_{\mathbb{C}}V$ | — |
| Division with remainder | $f=qg+r$ unique; divisibility and greatest common divisors do not depend on the field | long division |
| Remainder theorem | $x-a$ divides $f$ with remainder $f(a)$; $a$ is a multiple root ⇔ $f(a)=f'(a)=0$ | synthetic division (Horner's method): $n$ multiplications; expansion in powers of $x-a$: $\frac{n(n+1)}2$ |
| Interpolation | the polynomial of degree $\le n$ through $n+1$ points is unique | Lagrange formula $O(n^2)$; Vandermonde system $O(n^3)$ |
| Greatest common divisor | $(f,g)=uf+vg$ (Bézout); coprime ⇔ $uf+vg=1$ | Euclidean algorithm, extended Euclidean algorithm |
| Factorization | irreducible polynomials are the "primes"; factorization exists and is unique; no multiple roots ⇔ $(f,f')=1$ | multiple roots can be detected without finding roots |
| $\mathbb{C},\mathbb{R},\mathbb{Q}$ | fundamental theorem of algebra; complex roots of real polynomials come in conjugate pairs; rational root theorem, Gauss's lemma, Eisenstein's criterion | rational roots: finitely many checks |
| Roots and coefficients | Vieta's formulas; discriminant $\prod_{i<j}(x_i-x_j)^2$; for $x^3+qx+r$: $D=-4q^3-27r^2$ | power-sum recursion + Vandermonde |
