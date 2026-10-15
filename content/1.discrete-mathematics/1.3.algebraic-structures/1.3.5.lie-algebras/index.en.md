---
title: Lie Algebras
source_hash: 7392063cefe2
---

Most of the groups in Chapter 2 are finite, such as the $6$ symmetries of an equilateral triangle (Example 2.4.1). Symmetries such as rotations and rigid motions of space, however, vary continuously: one can rotate about an axis through any angle, and all rotations together form a "smooth" infinite group. Such groups are hard to study directly. The idea of the Norwegian mathematician Sophus Lie in the 1870s was to look only at the "infinitesimal transformations" near the identity: they form a vector space, and the noncommutativity of the group leaves on this space a bilinear operation, the **Lie bracket**. The resulting structure is a Lie algebra, which can be viewed as the linearization of a continuous group; such continuous groups are now called *Lie groups*.

This chapter uses the following material from earlier chapters: groups, **subgroups** and **homomorphisms** (Chapter 2); **fields** and **vector spaces** over a field (Chapter 3, in particular Definition 3.6.1); and matrices, traces and determinants from linear algebra ([Linear Algebra](/2.1)). The lattices of Chapter 4 are not used directly. Compared with the earlier structures, the new feature of a Lie algebra is that its operation does not satisfy the **associative law**; the Jacobi identity takes its place. We first define Lie algebras, then introduce subalgebras, ideals, quotient algebras and homomorphisms in parallel with groups and rings, then present the basic examples and outline the classification of complex simple Lie algebras, and finally use the matrix exponential to explain the connection between Lie groups and Lie algebras. In the next chapter, representation theory will "represent" both groups and Lie algebras as linear transformations of vector spaces.

## 5.1. Definition of a Lie Algebra

### 5.1.1. Vector Spaces

A Lie algebra is first of all a vector space. All vector spaces in this chapter are over some field $F$ (usually $\mathbb{R}$ or $\mathbb{C}$), as in Definition 3.6.1: $(V, +)$ is an **abelian group** with a scalar multiplication satisfying the distributive and associative laws. Subspaces, bases, dimension, linear maps and matrix representations from linear algebra ([Linear Algebra: Linear Spaces and Linear Maps](/2.1.8)) are used here as usual.

Notation used throughout this chapter: $M_n(F)$ denotes the set of all $n \times n$ matrices over $F$; $\operatorname{End}(V)$ denotes the set of all linear transformations of $V$, which becomes $M_n(F)$ ($n = \dim V$) once a basis is fixed; and $\operatorname{tr}$ denotes the trace of a matrix, which satisfies $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ ([trace of a matrix](/2.1.1)).

For matrices, the most natural operation that "measures noncommutativity" is the *commutator* $[A, B] = AB - BA$: $[A, B] = 0$ if and only if $A$ and $B$ commute. The commutator is linear in each of $A$ and $B$ and satisfies $[A, A] = 0$, but it is not associative (for instance, taking $A = B$ gives $[[A, B], C] = 0$, while $[A, [B, C]]$ is in general nonzero). The axioms of a Lie algebra are abstracted precisely from these properties of the commutator.

### 5.1.2. The Lie Bracket

**Definition 5.1.2 (Lie Algebra)** Let $\mathfrak{g}$ be a vector space over a field $F$. If $\mathfrak{g}$ carries an operation $[\cdot\,, \cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$, called the **Lie bracket**, satisfying the following three axioms, then $\mathfrak{g}$ is called a Lie algebra:

1. **bilinearity**: for all $x, y, z \in \mathfrak{g}$ and $a, b \in F$,
   $$
   [ax + by, z] = a[x, z] + b[y, z], \quad [x, ay + bz] = a[x, y] + b[x, z];
   $$
2. the **alternating property**: for every $x \in \mathfrak{g}$,
   $$
   [x, x] = 0;
   $$
3. the **Jacobi identity**: for all $x, y, z \in \mathfrak{g}$,
   $$
   [x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.
   $$

The dimension of $\mathfrak{g}$ as a vector space is called the dimension of the Lie algebra. In the language of Chapter 1, a Lie algebra is an algebraic system: in addition to addition and scalar multiplication it has a binary operation $[\cdot\,, \cdot]$, and the distributive law is contained in bilinearity.

The alternating property and bilinearity imply antisymmetry, $[x, y] = -[y, x]$: expand $0 = [x + y, x + y] = [x, y] + [y, x]$. This holds over a field of any characteristic. Conversely, if $F$ does not have characteristic $2$ (for the **characteristic of a field**, see Definition 3.5.4), antisymmetry gives $[x, x] = -[x, x]$ and hence $[x, x] = 0$, so the two axioms are equivalent.

The Lie bracket is in general not associative; the Jacobi identity plays the role of associativity. Writing $\operatorname{ad} x: y \mapsto [x, y]$ and using antisymmetry, the Jacobi identity can be rewritten as

$$
\operatorname{ad} x\,([y, z]) = [\operatorname{ad} x\,(y), z] + [y, \operatorname{ad} x\,(z)],
$$

that is, $\operatorname{ad} x$ satisfies the Leibniz rule with respect to the bracket ($\operatorname{ad} x$ is a derivation).

### 5.1.3. Abelian Lie Algebras

**Definition 5.1.3 (Abelian Lie Algebra)** If $[x, y] = 0$ for all $x, y \in \mathfrak{g}$, then $\mathfrak{g}$ is called an abelian Lie algebra.

Any vector space with the zero bracket is an abelian Lie algebra, and every one-dimensional Lie algebra is abelian. Abelian Lie algebras are the simplest Lie algebras; in a general Lie algebra, $[x, y]$ measures how far $x$ and $y$ are from commuting.

## 5.2. Subalgebras, Ideals and Homomorphisms

This section runs exactly parallel to Sections 2.2, 2.6 and 2.7 on groups and Sections 3.2 and 3.3 on rings: substructures, substructures one can take quotients by, homomorphisms and the fundamental homomorphism theorem.

### 5.2.1. Subalgebras

**Definition 5.2.1** Let $\mathfrak{g}$ be a Lie algebra and $\mathfrak{h} \subseteq \mathfrak{g}$ a linear subspace. If $\mathfrak{h}$ is closed under the Lie bracket (that is, $[x, y] \in \mathfrak{h}$ for all $x, y \in \mathfrak{h}$), then $\mathfrak{h}$ is called a **Lie subalgebra** of $\mathfrak{g}$.

### 5.2.2. Ideals

**Definition 5.2.2** Let $\mathfrak{g}$ be a Lie algebra and $\mathfrak{i} \subseteq \mathfrak{g}$ a linear subspace. If $[x, y] \in \mathfrak{i}$ for all $x \in \mathfrak{g}$ and $y \in \mathfrak{i}$, then $\mathfrak{i}$ is called an **ideal** of $\mathfrak{g}$, written $\mathfrak{i} \triangleleft \mathfrak{g}$.

By antisymmetry, $[y, x] = -[x, y]$ also lies in $\mathfrak{i}$, so for Lie algebras there is no need to distinguish left and right ideals. Like **normal subgroups** in group theory and ideals in ring theory, the ideals of a Lie algebra are the basis for constructing quotient structures. Two important ideals are:

- the *center* $Z(\mathfrak{g}) = \{x \in \mathfrak{g} \mid [x, y] = 0 \text{ for all } y \in \mathfrak{g}\}$; $\mathfrak{g}$ is abelian if and only if $Z(\mathfrak{g}) = \mathfrak{g}$;
- the *derived algebra* $[\mathfrak{g}, \mathfrak{g}]$, the subspace spanned by all brackets $[x, y]$; $\mathfrak{g}$ is abelian if and only if $[\mathfrak{g}, \mathfrak{g}] = \{0\}$.

**Theorem 5.2.1** If $\mathfrak{i}$ is an ideal of a Lie algebra $\mathfrak{g}$, then the quotient space $\mathfrak{g}/\mathfrak{i}$ is a Lie algebra under the operation

$$
[x + \mathfrak{i}, y + \mathfrak{i}] = [x, y] + \mathfrak{i},
$$

called the *quotient Lie algebra*.

Here the quotient space $\mathfrak{g}/\mathfrak{i}$ is the **quotient group** of the additive group $(\mathfrak{g}, +)$ by the subgroup $\mathfrak{i}$ (Theorem 2.6.3), with scalar multiplication $a(x + \mathfrak{i}) = ax + \mathfrak{i}$; it is a vector space of dimension $\dim \mathfrak{g} - \dim \mathfrak{i}$. The bracket does not depend on the choice of representatives: if $x' = x + u$ and $y' = y + v$ ($u, v \in \mathfrak{i}$), then $[x', y'] - [x, y] = [x, v] + [u, y] + [u, v] \in \mathfrak{i}$. In the terms of Chapter 1, "$x \sim y \iff x - y \in \mathfrak{i}$" is a **congruence relation** with respect to addition, scalar multiplication and the Lie bracket; bilinearity, the alternating property and the Jacobi identity are all inherited from $\mathfrak{g}$.

### 5.2.3. Lie Algebra Homomorphisms

**Definition 5.2.3** Let $\mathfrak{g}_1$ and $\mathfrak{g}_2$ be Lie algebras over the same field and $\varphi: \mathfrak{g}_1 \to \mathfrak{g}_2$ a **linear map**. If $\varphi([x, y]_{\mathfrak{g}_1}) = [\varphi(x), \varphi(y)]_{\mathfrak{g}_2}$ for all $x, y \in \mathfrak{g}_1$, then $\varphi$ is called a **Lie algebra homomorphism**; if $\varphi$ is moreover bijective, it is called a **Lie algebra isomorphism**.

**Theorem 5.2.2** Let $\varphi: \mathfrak{g}_1 \to \mathfrak{g}_2$ be a Lie algebra homomorphism. Then $\ker \varphi = \{x \in \mathfrak{g}_1 \mid \varphi(x) = 0\}$ is an ideal of $\mathfrak{g}_1$, and the image $\varphi(\mathfrak{g}_1)$ is a subalgebra of $\mathfrak{g}_2$.

**Proof**: $\ker \varphi$ is the kernel of a linear map and hence a subspace. For $x \in \mathfrak{g}_1$ and $y \in \ker \varphi$, $\varphi([x, y]) = [\varphi(x), 0] = 0$, so $[x, y] \in \ker \varphi$. The image is a subspace, and $[\varphi(x), \varphi(y)] = \varphi([x, y])$ again lies in the image. $\square$

**Theorem 5.2.3 (Fundamental Homomorphism Theorem for Lie Algebras)** Let $\varphi: \mathfrak{g}_1 \to \mathfrak{g}_2$ be a surjective Lie algebra homomorphism. Then

$$
\mathfrak{g}_1 / \ker \varphi \cong \mathfrak{g}_2,
$$

with the isomorphism given by $x + \ker \varphi \mapsto \varphi(x)$.

**Proof**: As for Theorem 2.7.7: the map does not depend on representatives and is a linear bijection (a result of linear algebra on quotient spaces, which is also the fundamental homomorphism theorem for the additive groups); moreover $[x + \ker \varphi, y + \ker \varphi] = [x, y] + \ker \varphi \mapsto \varphi([x, y]) = [\varphi(x), \varphi(y)]$, so it preserves brackets. $\square$

At this point the thread "homomorphism, kernel, quotient, fundamental homomorphism theorem" is exactly the same for groups, rings and Lie algebras; all are special cases of Theorem 1.4.4.

## 5.3. Classification of Complex Simple Lie Algebras (Overview)

A simple group is a group whose only normal subgroups are the trivial ones, $\{e\}$ and $G$; examples are the cyclic groups $\mathbb{Z}_p$ of prime order and the **alternating group** $A_5$. By the fundamental homomorphism theorem, a simple group has no nontrivial homomorphic images; simple groups are the "atoms" from which general groups are built. Lie algebras have an entirely analogous notion.

**Definition 5.3.1 (Simple Lie Algebra)** If a Lie algebra $\mathfrak{g}$ is not abelian and has no ideals other than $\{0\}$ and $\mathfrak{g}$, then $\mathfrak{g}$ is called a simple Lie algebra.

**Definition 5.3.2 (Semisimple Lie Algebra)** If a finite-dimensional Lie algebra $\mathfrak{g}$ has no nonzero abelian ideals, then $\mathfrak{g}$ is called a semisimple Lie algebra.

Over a field of characteristic $0$, the finite-dimensional semisimple Lie algebras are exactly the direct sums of finitely many simple Lie algebras. Simple Lie algebras play the same role in Lie theory as simple groups in group theory.

Using the root space decomposition, the finite-dimensional complex simple Lie algebras can be completely classified: each is isomorphic to a member of one of four infinite series of *classical Lie algebras*, or to one of the five *exceptional Lie algebras* $G_2, F_4, E_6, E_7, E_8$ (of dimensions $14, 52, 78, 133, 248$). The classical Lie algebras are listed in the table below (the matrix Lie algebras are described in Section 5.4; $\mathfrak{so}(m, \mathbb{C})$ is the Lie algebra of complex skew-symmetric matrices of order $m$, and $\mathfrak{sp}(2l, \mathbb{C})$ is the Lie algebra of matrices satisfying $X^{\mathsf{T}} J + J X = 0$, where $J = \begin{pmatrix} 0 & I_l \\ -I_l & 0 \end{pmatrix}$):

| Type | Name | Matrix realization | Dimension |
| :--- | :--- | :--- | :--- |
| $A_l \ (l \ge 1)$ | special linear Lie algebra | $\mathfrak{sl}(l+1, \mathbb{C})$ | $l(l+2)$ |
| $B_l \ (l \ge 2)$ | odd orthogonal Lie algebra | $\mathfrak{so}(2l+1, \mathbb{C})$ | $l(2l+1)$ |
| $C_l \ (l \ge 3)$ | symplectic Lie algebra | $\mathfrak{sp}(2l, \mathbb{C})$ | $l(2l+1)$ |
| $D_l \ (l \ge 4)$ | even orthogonal Lie algebra | $\mathfrak{so}(2l, \mathbb{C})$ | $l(2l-1)$ |

The restrictions on $l$ avoid repetitions: in low rank there are the isomorphisms $B_1 \cong C_1 \cong A_1$, $C_2 \cong B_2$ and $D_3 \cong A_3$, while $D_2 = \mathfrak{so}(4, \mathbb{C})$ is not simple (it is isomorphic to $\mathfrak{sl}(2, \mathbb{C}) \oplus \mathfrak{sl}(2, \mathbb{C})$).

## 5.4. Examples of Lie Algebras

### 5.4.1. The Cross Product in Three-Dimensional Space

**Example 5.4.1** Let $\mathfrak{g} = \mathbb{R}^3$ with the Lie bracket given by the cross product of vectors:

$$
[\boldsymbol{u}, \boldsymbol{v}] = \boldsymbol{u} \times \boldsymbol{v}.
$$

The cross product is bilinear, satisfies $\boldsymbol{u} \times \boldsymbol{u} = \boldsymbol{0}$ and the Jacobi identity, so $(\mathbb{R}^3, \times)$ is a Lie algebra. In the standard basis, $[\boldsymbol{e}_1, \boldsymbol{e}_2] = \boldsymbol{e}_3$, $[\boldsymbol{e}_2, \boldsymbol{e}_3] = \boldsymbol{e}_1$ and $[\boldsymbol{e}_3, \boldsymbol{e}_1] = \boldsymbol{e}_2$. This is the vector form of the Lie algebra $\mathfrak{so}(3)$ of the three-dimensional rotation group $SO(3)$ (see Example 5.4.4 and Section 5.5): $\boldsymbol{u}$ represents an infinitesimal rotation about the axis $\boldsymbol{u}$, and the cross product captures the noncommutativity of two infinitesimal rotations.

### 5.4.2. Matrix Lie Algebras

**Example 5.4.2** Let $\mathfrak{gl}(n, F)$ be the set of all $n \times n$ matrices over a field $F$, with the Lie bracket given by the matrix **commutator**

$$
[A, B] = AB - BA.
$$

Then $(\mathfrak{gl}(n, F), [\cdot\,, \cdot])$ is a Lie algebra, called the *general linear Lie algebra*; it is the typical example of a matrix Lie algebra. The Jacobi identity can be checked by direct expansion: the twelve terms of $[A, [B, C]] + [B, [C, A]] + [C, [A, B]]$ cancel in pairs. More generally, every associative algebra (such as the ring $\operatorname{End}(V)$) becomes a Lie algebra under the commutator; $\operatorname{End}(V)$ with the commutator is denoted $\mathfrak{gl}(V)$.

**Example 5.4.3** The set of matrices of trace zero,

$$
\mathfrak{sl}(n, F) = \{A \in \mathfrak{gl}(n, F) \mid \operatorname{tr}(A) = 0\},
$$

is a subalgebra of $\mathfrak{gl}(n, F)$, called the *special linear Lie algebra*. In fact, $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ shows that every commutator has trace zero, so $\mathfrak{sl}(n, F)$ is even an ideal of $\mathfrak{gl}(n, F)$. It is the kernel of the trace map $\operatorname{tr}: \mathfrak{gl}(n, F) \to F$ (regarding $F$ as a one-dimensional abelian Lie algebra, $\operatorname{tr}$ is a Lie algebra homomorphism), so by Theorem 5.2.3, $\mathfrak{gl}(n, F)/\mathfrak{sl}(n, F) \cong F$.

**Example 5.4.4** The Lie algebra $\mathfrak{so}(3)$ of the three-dimensional rotation group $SO(3)$ consists of all real $3 \times 3$ skew-symmetric matrices, with the matrix commutator as bracket. The map

$$
\boldsymbol{u} = (u_1, u_2, u_3) \mapsto \hat{u} = \begin{pmatrix} 0 & -u_3 & u_2 \\ u_3 & 0 & -u_1 \\ -u_2 & u_1 & 0 \end{pmatrix}
$$

satisfies $\hat{u}\boldsymbol{v} = \boldsymbol{u} \times \boldsymbol{v}$ and $[\hat{u}, \hat{v}] = \widehat{\boldsymbol{u} \times \boldsymbol{v}}$, so it is a Lie algebra isomorphism from $(\mathbb{R}^3, \times)$ onto $\mathfrak{so}(3)$: the matrix form and the cross-product form can be converted into each other.

**Example 5.4.5** $\mathfrak{sl}(2, F)$ is three-dimensional. Take the basis

$$
e = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad f = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad h = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
$$

A direct computation gives

$$
[h, e] = 2e, \qquad [h, f] = -2f, \qquad [e, f] = h.
$$

That is, $e$ and $f$ are eigenvectors of $\operatorname{ad} h$ (with eigenvalues $2$ and $-2$). For $F = \mathbb{C}$, $\mathfrak{sl}(2, \mathbb{C})$ is the smallest simple Lie algebra ($A_1$ in the table), and its representation theory (Example 6.2.2) is the prototype of the whole theory.

## 5.5. Lie Groups and Lie Algebras

This section explains how Lie algebras arise from continuous groups. To avoid differential geometry, we consider only groups of matrices.

### 5.5.1. The Matrix Exponential

For $X \in M_n(\mathbb{C})$, define the *matrix exponential*

$$
e^X = \exp(X) = \sum_{k=0}^{\infty} \frac{X^k}{k!} = I + X + \frac{X^2}{2!} + \cdots;
$$

the series converges for every $X$. It has the following properties (compared with the real exponential function, the difference is that a commutativity condition is needed):

**Theorem 5.5.1** For all $X, Y \in M_n(\mathbb{C})$ and every invertible matrix $P$:

1. if $XY = YX$, then $e^{X+Y} = e^X e^Y$; in particular, $e^X$ is invertible with $(e^X)^{-1} = e^{-X}$;
2. $e^{PXP^{-1}} = P e^X P^{-1}$;
3. $\det(e^X) = e^{\operatorname{tr} X}$;
4. $t \mapsto e^{tX}$ is a group homomorphism from $(\mathbb{R}, +)$ to $\operatorname{GL}(n, \mathbb{C})$, and $\dfrac{\mathrm{d}}{\mathrm{d}t} e^{tX} = X e^{tX}$.

Property 4 shows that $\{e^{tX} \mid t \in \mathbb{R}\}$ is a subgroup, called the *one-parameter subgroup* generated by $X$; $X$ is its "velocity" at $t = 0$. Property 3 can be proved using the Jordan canonical form ([Linear Algebra](/2.1.10)) and property 2: the exponential of an upper triangular matrix is again upper triangular, with diagonal entries $e^{\lambda_i}$.

### 5.5.2. Matrix Lie Groups

**Definition 5.5.1 (Matrix Lie Group)** Let $G$ be a subgroup of the **general linear group** $\operatorname{GL}(n, \mathbb{C})$. If every sequence of matrices in $G$ that converges to an invertible matrix $A$ has $A \in G$, then $G$ is called a matrix Lie group.

Common matrix Lie groups include:

- $\operatorname{GL}(n, \mathbb{R})$, and $\operatorname{SL}(n, \mathbb{R}) = \{A \mid \det A = 1\}$ (the kernel of $\det$; see Section 2.7.5);
- the orthogonal group $O(n) = \{R \in M_n(\mathbb{R}) \mid R^{\mathsf{T}} R = I\}$ and the special orthogonal group $SO(n) = \{R \in O(n) \mid \det R = 1\}$ (for orthogonal matrices see [Linear Algebra](/2.1.4)); $SO(3)$ is the group of all rotations of three-dimensional space about the origin;
- the unitary group $U(n) = \{U \in M_n(\mathbb{C}) \mid U^* U = I\}$ and $SU(n) = \{U \in U(n) \mid \det U = 1\}$.

All of these groups are infinite but depend on only finitely many continuous parameters; for example, a rotation in $SO(3)$ is determined by the direction of its axis ($2$ parameters) and its angle ($1$ parameter).

**Definition 5.5.2** The Lie algebra of a matrix Lie group $G$ is

$$
\mathfrak{g} = \{X \in M_n(\mathbb{C}) \mid e^{tX} \in G \text{ for all } t \in \mathbb{R}\},
$$

that is, the set of "velocities" of all one-parameter subgroups of $G$.

**Theorem 5.5.2** The Lie algebra $\mathfrak{g}$ of a matrix Lie group $G$ is a real vector space closed under the commutator, and hence a Lie subalgebra of $\mathfrak{gl}(n, \mathbb{C})$ (regarded as a real Lie algebra).

**Proof** (sketch): Closure under scalar multiplication is obvious. Closure under addition follows from the Lie product formula $e^{X+Y} = \lim_{m \to \infty} (e^{X/m} e^{Y/m})^m$ and the closedness condition in Definition 5.5.1. For the bracket, let $X, Y \in \mathfrak{g}$. By property 2 of Theorem 5.5.1, $e^{s \cdot e^{tX} Y e^{-tX}} = e^{tX} e^{sY} e^{-tX} \in G$, so $e^{tX} Y e^{-tX} \in \mathfrak{g}$ for all $t$. Its derivative with respect to $t$ at $t = 0$ is $XY - YX$, and the derivative of a curve lying in a subspace again lies in that subspace; hence $[X, Y] \in \mathfrak{g}$. $\square$

The relation between the Lie bracket and the noncommutativity of the group can be seen from the following expansion: for small $t$,

$$
e^{tX} e^{tY} e^{-tX} e^{-tY} = I + t^2 [X, Y] + O(t^3).
$$

The left-hand side is the group "commutator" $aba^{-1}b^{-1}$, which equals $I$ if and only if $a$ and $b$ commute; the second-order term on the right is exactly the Lie bracket.

Theorem 5.5.1 lets us compute where the earlier examples come from:

- the Lie algebra of $\operatorname{GL}(n, \mathbb{R})$ is $\mathfrak{gl}(n, \mathbb{R})$;
- since $\det(e^{tX}) = e^{t \operatorname{tr} X}$, the Lie algebra of $\operatorname{SL}(n, \mathbb{R})$ is $\mathfrak{sl}(n, \mathbb{R})$;
- since $(e^{tX})^{\mathsf{T}} e^{tX} = I$ holds for all $t$ if and only if $X^{\mathsf{T}} = -X$ (necessity follows by differentiating at $t = 0$, sufficiency from $(e^{tX})^{\mathsf{T}} = e^{tX^{\mathsf{T}}} = e^{-tX}$), the Lie algebras of $O(n)$ and $SO(n)$ are both the algebra $\mathfrak{so}(n)$ of skew-symmetric matrices.

We have $\dim \mathfrak{so}(3) = 3$, in agreement with the $3$ continuous parameters of $SO(3)$: the dimension of the Lie algebra is the number of parameters of the Lie group.

**Example 5.5.1** Let $\boldsymbol{u}$ be a unit vector and $\hat{u}$ as in Example 5.4.4. Then $\hat{u}^3 = -\hat{u}$, and summing the series directly gives *Rodrigues' rotation formula*

$$
e^{\theta \hat{u}} = I + \sin\theta\, \hat{u} + (1 - \cos\theta)\, \hat{u}^2,
$$

which is exactly the matrix of the rotation through angle $\theta$ about the axis $\boldsymbol{u}$. Thus a vector $\theta\boldsymbol{u}$ in $\mathfrak{so}(3)$ (a "rotation vector") yields a rotation via the exponential map, and every rotation arises in this way. This is why molecular simulation and structural biology often parameterize molecular orientations by rotation vectors or by unit quaternions (which correspond to $SU(2)$).

**Example 5.5.2** The rigid motions $\boldsymbol{x} \mapsto R\boldsymbol{x} + \boldsymbol{t}$ of three-dimensional space ($R \in SO(3)$, $\boldsymbol{t} \in \mathbb{R}^3$) form the group $SE(3)$. In homogeneous coordinates $(\boldsymbol{x}, 1)$ a rigid motion can be written as the $4 \times 4$ matrix

$$
\begin{pmatrix} R & \boldsymbol{t} \\ \boldsymbol{0}^{\mathsf{T}} & 1 \end{pmatrix},
$$

so $SE(3)$ is a matrix Lie group in $\operatorname{GL}(4, \mathbb{R})$. Its Lie algebra consists of the matrices $\begin{pmatrix} \hat{\omega} & \boldsymbol{v} \\ \boldsymbol{0}^{\mathsf{T}} & 0 \end{pmatrix}$ ($\boldsymbol{\omega}, \boldsymbol{v} \in \mathbb{R}^3$) and has dimension $6$, corresponding to the $3$ rotational and $3$ translational degrees of freedom of a rigid body. Molecular docking searches $SE(3)$ for the pose of a ligand relative to a receptor; protein structure models such as AlphaFold2 represent the backbone of each residue as a local coordinate frame, that is, as an element of $SE(3)$.

## Summary

| Topic | Key concepts |
|------|----------|
| Definition | vector spaces over a field; bilinearity, alternating property and Jacobi identity of the Lie bracket; antisymmetry; $\operatorname{ad} x$ is a derivation |
| Substructures and homomorphisms | Lie subalgebras, ideals (center, derived algebra), quotient Lie algebras, Lie algebra homomorphisms, the kernel is an ideal, fundamental homomorphism theorem |
| Classification | simple and semisimple Lie algebras, the classical series $A_l, B_l, C_l, D_l$ of complex simple Lie algebras and the exceptional Lie algebras |
| Examples | cross product $(\mathbb{R}^3, \times) \cong \mathfrak{so}(3)$, $\mathfrak{gl}(n, F)$, $\mathfrak{sl}(n, F)$, the basis $e, f, h$ of $\mathfrak{sl}(2, F)$ |
| Lie groups | matrix exponential, one-parameter subgroups, matrix Lie groups ($\operatorname{GL}$, $\operatorname{SL}$, $O(n)$, $SO(n)$, $SE(3)$), the Lie algebra of a Lie group, group commutators and the Lie bracket |

We have seen in this chapter that the rotation group $SO(3)$ consists of matrices from the outset, with matrix multiplication as its group operation, and that $\mathfrak{so}(3)$ also consists of matrices, with the commutator as its bracket. The next chapter extends this practice of "realizing by matrices" to arbitrary groups and Lie algebras: a representation is a homomorphism into $\operatorname{GL}(V)$ or $\mathfrak{gl}(V)$.
