---
title: Representation Theory
source_hash: 879ba06b155b
---

*Representation theory* is the end point of the main line of this course. Cayley's theorem (Theorem 2.4.4) says that every group can be realized as a transformation group of some set; representation theory asks for more: to realize a group (or a Lie algebra) by linear transformations of a vector space, that is, by transformations preserving vector addition and scalar multiplication, which become matrices once a basis is chosen. Abstract group operations then turn into matrix multiplication, structural questions turn into questions of linear algebra, and the whole toolkit of **eigenvalues**, traces and direct sum decompositions becomes available. The groups $SO(3)$ and $\mathfrak{so}(3)$ of the previous chapter already consist of matrices; this chapter extends that situation to general groups and Lie algebras.

Abstractly, a representation is just a **homomorphism** (Definition 1.4.3): a group representation is a group homomorphism into the group $\operatorname{GL}(V)$ of invertible linear transformations, and a Lie algebra representation is a Lie algebra homomorphism into the general linear Lie algebra $\mathfrak{gl}(V)$. This chapter uses **group actions**, **conjugacy classes** and homomorphisms from Chapter 2; **vector spaces** over a field and $\operatorname{GL}(V)$ from Chapter 3 (Section 3.6.3); **Lie algebras**, the **matrix exponential** and $\mathfrak{sl}(2)$ from Chapter 5; and invariant subspaces, eigenvalues and traces from linear algebra ([Linear Algebra](/2.1)). Representation theory is used extensively in physics and chemistry: in quantum mechanics, symmetries act through representations of groups on the state space, and molecular spectroscopy and crystallography use the character tables of point groups to analyze vibrational modes and selection rules.

## 6.1. Group Representations

### 6.1.1. Definition of a Group Representation

**Definition 6.1.1** Let $G$ be a group, $V$ a vector space over a field $F$, and $\operatorname{GL}(V)$ the group of all invertible linear transformations of $V$ under composition (the **general linear group** of $V$; see Section 3.6.3). A group homomorphism $\rho: G \to \operatorname{GL}(V)$ is called a (linear) **representation** of $G$ on $V$; $V$ is called the **representation space**, and the dimension of $V$ is called the **dimension** of the representation.

When $V$ is $n$-dimensional and a basis is fixed, the elements of $\operatorname{GL}(V)$ are invertible matrices of order $n$, so a representation $\rho$ assigns an invertible matrix to each element of $G$; that is, it is a homomorphism $G \to \operatorname{GL}(n, F)$. The homomorphism condition $\rho(gh) = \rho(g)\rho(h)$ ensures that the group operation agrees with matrix multiplication; by Theorem 2.7.3, $\rho(e) = I_V$ and $\rho(g^{-1}) = \rho(g)^{-1}$.

**Example 6.1.1** Some basic representations:

- the *trivial representation*: $\rho(g) = 1$ (the identity transformation of a one-dimensional space) for all $g \in G$;
- the *sign representation*: $\operatorname{sgn}: S_n \to \operatorname{GL}(1, \mathbb{R}) = \mathbb{R} \setminus \{0\}$, sending even permutations to $1$ and odd permutations to $-1$ (Section 2.7.1);
- for a matrix Lie group $G \subseteq \operatorname{GL}(n, \mathbb{C})$ (Definition 5.5.1), the inclusion map is a representation of $G$ on $\mathbb{C}^n$, called the *defining representation*; for example, $SO(3)$ acts on $\mathbb{R}^3$ by rotations.

**Example 6.1.2 (Permutation Representation)** For $\sigma \in S_n$, let $\rho(\sigma)$ be the linear transformation sending the standard basis vector $\boldsymbol{e}_i$ to $\boldsymbol{e}_{\sigma(i)}$; its matrix is a permutation matrix (exactly one $1$ in each row and each column). Since $\rho(\sigma)\rho(\tau)\boldsymbol{e}_i = \boldsymbol{e}_{\sigma(\tau(i))} = \rho(\sigma\tau)\boldsymbol{e}_i$, $\rho$ is an $n$-dimensional representation of $S_n$ on $F^n$, called the *permutation representation*. More generally, an action of a group $G$ on a finite set $A$ (Definition 2.5.3) gives an $|A|$-dimensional representation by permuting basis vectors; the $|G|$-dimensional representation given by the action of $G$ on itself by left multiplication (Cayley's theorem) is called the *regular representation*.

**Example 6.1.3** Place the center of an equilateral triangle at the origin. The $6$ symmetries of Example 2.4.1 are then orthogonal transformations of the plane $\mathbb{R}^2$, which gives a two-dimensional representation of $S_3$: $(1\ 2\ 3)$ corresponds to the matrix of the rotation through $120^\circ$, and $(2\ 3)$ to the matrix of the reflection in the axis of symmetry through vertex $1$.

**Definition 6.1.2 (Linear Action)** Let $G$ be a group, $V$ a vector space over a field $F$, and $(g, v) \mapsto g \cdot v$ a map $G \times V \to V$. If for all $g, h \in G$, $v, w \in V$ and $\lambda, \mu \in F$ the following three conditions hold, the map is called a **linear action** of $G$ on $V$, and we say that $G$ acts linearly on $V$:

1. **linearity**: $g \cdot (\lambda v + \mu w) = \lambda(g \cdot v) + \mu(g \cdot w)$ (each $g$ gives a linear transformation of $V$);
2. **compatibility**: $g \cdot (h \cdot v) = (gh) \cdot v$;
3. the **identity axiom**: $e \cdot v = v$.

Conditions 2 and 3 are the definition of a **group action** (Definition 2.5.3), so a linear action is a group action in which every $g$ acts by a linear transformation. Just as a group action is equivalent to a homomorphism into $E(A)$ (Section 2.5.5), linear actions and representations are two ways of saying the same thing: setting $\rho(g)(v) = g \cdot v$, conditions 2 and 3 ensure that $\rho(g)$ is invertible (with inverse $\rho(g^{-1})$) and that $\rho$ is a group homomorphism; conversely, a representation $\rho$ gives a linear action by $g \cdot v = \rho(g)(v)$.

### 6.1.2. Equivalent Representations, Invariant Subspaces and Irreducible Representations

**Definition 6.1.3** Let $\rho_1: G \to \operatorname{GL}(V_1)$ and $\rho_2: G \to \operatorname{GL}(V_2)$ be two representations of a group $G$. If there is a linear isomorphism $\varphi: V_1 \to V_2$ such that $\varphi \circ \rho_1(g) = \rho_2(g) \circ \varphi$ for every $g \in G$, the two representations are called **equivalent**. In the finite-dimensional case, after fixing bases, this means that there is a single invertible matrix $P$ with $\rho_2(g) = P\rho_1(g)P^{-1}$ for all $g$.

Equivalent representations differ only in the choice of basis, just as isomorphic algebraic systems differ only in the names of their elements (Section 1.4.2); for similarity of matrices see [Linear Algebra](/2.1.6). A linear map satisfying $\varphi \circ \rho_1(g) = \rho_2(g) \circ \varphi$ ($\varphi$ need not be invertible) is called a $G$-*equivariant map*; it is a "homomorphism between representations".

**Definition 6.1.4 (Irreducible Representation)** Let $\rho: G \to \operatorname{GL}(V)$ be a representation. A subspace $W \subseteq V$ with $\rho(g)W \subseteq W$ for all $g \in G$ is called an **invariant subspace**. If $V \neq \{0\}$ and $V$ has no invariant subspaces other than $\{0\}$ and $V$, the representation is called irreducible; otherwise (if $V$ has a nontrivial invariant subspace) it is called **reducible**.

The restriction $g \mapsto \rho(g)|_W$ to an invariant subspace $W$ is itself a representation, called a *subrepresentation*; it is the counterpart in representation theory of subgroups, subrings and subalgebras. A one-dimensional representation is always irreducible.

**Definition 6.1.5 (Direct Sum)** Let $\rho_1, \rho_2$ be representations of $G$ on $V_1, V_2$. On the direct sum $V_1 \oplus V_2$, setting $\rho(g)(v_1, v_2) = (\rho_1(g)v_1, \rho_2(g)v_2)$ gives a representation called the **direct sum** of $\rho_1$ and $\rho_2$, written $\rho_1 \oplus \rho_2$. In a suitable basis its matrix is the block diagonal matrix $\begin{pmatrix} \rho_1(g) & 0 \\ 0 & \rho_2(g) \end{pmatrix}$.

Irreducible representations are the building blocks of general representations. For finite groups, the following theorem guarantees that every representation splits into irreducible ones.

**Theorem 6.1.1 (Maschke's Theorem)** Let $G$ be a finite group and suppose that the characteristic of the field $F$ does not divide $|G|$ (for example $F = \mathbb{R}$ or $\mathbb{C}$). Then every invariant subspace of a finite-dimensional representation of $G$ has an invariant complement, and consequently the representation is equivalent to a direct sum of irreducible representations.

The idea of the proof is "averaging over the group": take any complement of $W$ and the corresponding projection $P$; then $\frac{1}{|G|}\sum_{g \in G} \rho(g) P \rho(g)^{-1}$ is again a projection onto $W$ and commutes with every $\rho(g)$, so its kernel is an invariant complement. This requires $|G|$ to be invertible in $F$, which is exactly the condition on the characteristic (Definition 3.5.4).

**Example 6.1.4** The permutation representation of $S_3$ on $\mathbb{R}^3$ (Example 6.1.2) has the two invariant subspaces

$$
W_1 = \{(x, x, x) \mid x \in \mathbb{R}\}, \qquad W_2 = \{(x_1, x_2, x_3) \mid x_1 + x_2 + x_3 = 0\},
$$

and $\mathbb{R}^3 = W_1 \oplus W_2$. On $W_1$ we get the trivial representation. $W_2$ is a two-dimensional irreducible representation: a one-dimensional invariant subspace would be spanned by a common eigenvector of all $\rho(\sigma)$, but the eigenvectors of $(1\ 2)$ on $W_2$ are only the multiples of $(1, -1, 0)$ and $(1, 1, -2)$, and those of $(2\ 3)$ are only the multiples of $(0, 1, -1)$ and $(2, -1, -1)$; there is no common one. In fact $W_2$ is equivalent to the triangle representation of Example 6.1.3: send the projection of $\boldsymbol{e}_i$ onto $W_2$ to the $i$th vertex of the triangle.

## 6.2. Representations of Lie Algebras

Assigning to the elements of a Lie algebra linear transformations of a vector space gives a representation of the Lie algebra. The idea is the same as for groups; only the homomorphism condition becomes preservation of the Lie bracket.

**Definition 6.2.1** Let $\mathfrak{g}$ be a Lie algebra over a field $F$, $V$ a vector space over $F$, and $\mathfrak{gl}(V)$ the Lie algebra of all linear transformations of $V$ with $[X, Y] = XY - YX$ (Example 5.4.2). A Lie algebra homomorphism $\pi: \mathfrak{g} \to \mathfrak{gl}(V)$ is called a **representation** of $\mathfrak{g}$ on $V$; that is, $\pi$ is a linear map with $\pi([x, y]) = \pi(x)\pi(y) - \pi(y)\pi(x)$.

Invariant subspaces, irreducible representations, equivalence and direct sums are defined exactly as for group representations, with "for all $g \in G$" replaced by "for all $x \in \mathfrak{g}$".

**Example 6.2.1 (Adjoint Representation)** For any Lie algebra $\mathfrak{g}$, define $\operatorname{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ by

$$
\operatorname{ad}(x)(y) = [x, y], \quad \forall x, y \in \mathfrak{g}.
$$

Then $\operatorname{ad}$ is a Lie algebra homomorphism, called the *adjoint representation* of $\mathfrak{g}$. Indeed, for any $z \in \mathfrak{g}$,

$$
\operatorname{ad}([x, y])(z) = [[x, y], z], \qquad [\operatorname{ad}(x), \operatorname{ad}(y)](z) = [x, [y, z]] - [y, [x, z]],
$$

and the equality of the two is precisely the Jacobi identity. In other words, the Jacobi identity is equivalent to $\operatorname{ad}$ preserving the Lie bracket. The kernel of $\operatorname{ad}$ is the **center** $Z(\mathfrak{g})$ (Section 5.2.2); the invariant subspaces of the adjoint representation are exactly the ideals of $\mathfrak{g}$, so the adjoint representation is irreducible when $\mathfrak{g}$ is a **simple Lie algebra**.

**Example 6.2.2 (Irreducible Representations of $\mathfrak{sl}(2, \mathbb{C})$)** Let $e, f, h$ be the basis of $\mathfrak{sl}(2, \mathbb{C})$ from Example 5.4.5. For each nonnegative integer $n$, take a basis $v_0, v_1, \dots, v_n$ of an $(n+1)$-dimensional space and set

$$
h\, v_k = (n - 2k)\, v_k, \qquad f\, v_k = v_{k+1}, \qquad e\, v_k = k(n - k + 1)\, v_{k-1},
$$

with the convention $v_{-1} = v_{n+1} = 0$. One checks directly that these three linear transformations satisfy $[h, e] = 2e$, $[h, f] = -2f$ and $[e, f] = h$ (for example, $(ef - fe)v_k = [(k+1)(n-k) - k(n-k+1)]v_k = (n-2k)v_k$), so they define a representation $V(n)$. One can prove that:

- $V(n)$ is irreducible, and every $(n+1)$-dimensional irreducible representation of $\mathfrak{sl}(2, \mathbb{C})$ is equivalent to $V(n)$;
- the eigenvalues of $h$ on $V(n)$ are $n, n-2, \dots, -n$, called *weights*; $e$ raises the weight by $2$ and $f$ lowers it by $2$.

For $n = 1$ we get the defining representation on $\mathbb{C}^2$, and for $n = 2$ the three-dimensional adjoint representation. In quantum mechanics, $V(n)$ is the angular momentum multiplet of spin $j = n/2$, of dimension $2j + 1$, and the eigenvalues of $h/2$ are the magnetic quantum numbers $m = j, j-1, \dots, -j$.

## 6.3. Representations of Lie Groups and of Lie Algebras

Differentiating a representation of a Lie group $G$ gives a representation of its Lie algebra $\mathfrak{g}$; conversely, a representation of the Lie algebra can be lifted, via the exponential map (Section 5.5), to a representation of the Lie group, at least locally, and to a representation of all of $G$ when $G$ is simply connected.

**Theorem 6.3.1** Let $G$ be a Lie group and $\rho: G \to \operatorname{GL}(V)$ a (smooth) representation of $G$ on a finite-dimensional space $V$. Then

$$
\mathrm{d}\rho(X) = \left.\frac{\mathrm{d}}{\mathrm{d}t}\right|_{t=0} \rho(\exp(tX)), \quad X \in \mathfrak{g},
$$

defines a representation $\mathrm{d}\rho: \mathfrak{g} \to \mathfrak{gl}(V)$ of the Lie algebra, and $\rho(\exp(X)) = \exp(\mathrm{d}\rho(X))$; that is, the group representation commutes with the exponential map.

For the defining representation of a matrix Lie group (Example 6.1.1), $\mathrm{d}\rho$ is simply the inclusion of the Lie algebra $\mathfrak{g} \subseteq \mathfrak{gl}(n, \mathbb{C})$.

This shows the value of the Lie algebra as a "linear approximation": it reduces nonlinear problems on the Lie group to problems of linear algebra on the Lie algebra, one of the most widely used techniques in mathematical physics. For example, physics classifies angular momentum through the representations of the Lie algebra $\mathfrak{so}(3)$ of the rotation group $SO(3)$. The complexification of $\mathfrak{so}(3)$ is isomorphic to $\mathfrak{sl}(2, \mathbb{C})$ ($B_1 \cong A_1$ in the table of Section 5.3), so its irreducible representations are the $V(n)$ of Example 6.2.2. Those with $n$ even (integer spin) lift to representations of $SO(3)$; those with $n$ odd (half-integer spin) lift only to representations of the double cover $SU(2)$ of $SO(3)$.

In molecular modeling, the representations of $SO(3)$ and $SE(3)$ (Example 5.5.2) give a precise meaning to "rotation equivariance". A function $\Phi$ of atomic coordinates is called equivariant if $\Phi(\rho_{\text{in}}(g)x) = \rho_{\text{out}}(g)\Phi(x)$, that is, if it is a $G$-equivariant map in the sense introduced after Definition 6.1.3: when the whole molecule is rotated, the predicted energy (trivial representation) stays the same and the predicted forces (defining representation) rotate along with it. Equivariant neural networks for molecules and protein structures construct such maps precisely by decomposing their features into irreducible representations of $SO(3)$.

## 6.4. Characters and Orthogonality Relations

The character is the most important invariant of a group representation; it is given by the traces of the representing matrices.

**Definition 6.4.1 (Character)** Let $\rho: G \to \operatorname{GL}(V)$ be a representation of a finite group $G$ on a finite-dimensional vector space $V$. The function $\chi_\rho: G \to F$, $\chi_\rho(g) = \operatorname{tr}(\rho(g))$ ($g \in G$), is called the **character** of the representation $\rho$.

From the property $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ of the trace ([trace of a matrix](/2.1.1)), $\chi_\rho(e) = \dim V$ and $\chi_\rho(hgh^{-1}) = \chi_\rho(g)$, so a character is constant on each **conjugacy class** (Definition 2.6.2); moreover, equivalent representations have the same character. The character of a direct sum is the sum of the characters: $\chi_{\rho_1 \oplus \rho_2} = \chi_{\rho_1} + \chi_{\rho_2}$.

**Theorem 6.4.1 (Schur's Lemma)** Let $(\rho_1, V_1)$ and $(\rho_2, V_2)$ be irreducible representations of a group $G$, and let $\varphi: V_1 \to V_2$ be a $G$-equivariant linear map, that is, $\varphi \circ \rho_1(g) = \rho_2(g) \circ \varphi$ for every $g \in G$. Then:

1. either $\varphi = 0$ or $\varphi$ is a linear isomorphism; in particular, $\varphi = 0$ if the two representations are not equivalent;
2. if $V_1 = V_2 = V$ is finite-dimensional, $\rho_1 = \rho_2$, and the field $F$ is algebraically closed (such as $\mathbb{C}$), then $\varphi = \lambda I_V$ ($\lambda \in F$) is a scalar transformation.

**Proof**: $\ker \varphi$ is an invariant subspace of $V_1$, and $\varphi(V_1)$ is an invariant subspace of $V_2$. By irreducibility, $\ker \varphi = V_1$ (that is, $\varphi = 0$) or $\ker \varphi = \{0\}$; in the latter case $\varphi(V_1) \neq \{0\}$, so $\varphi(V_1) = V_2$ and $\varphi$ is an isomorphism. This proves 1. For 2, take an eigenvalue $\lambda$ of $\varphi$ (it exists over an algebraically closed field; see [eigenvalues](/2.1.6)). Then $\varphi - \lambda I_V$ is also equivariant and is not an isomorphism, so by 1, $\varphi = \lambda I_V$. $\square$

Schur's lemma expresses the "rigidity" of irreducible representations and is the basis for deriving the orthogonality relations and classifying irreducible representations. It yields the following orthogonality relations.

**Theorem 6.4.2 (Orthogonality Relations for Characters)** Let $G$ be a finite group and let $\chi_i$, $\chi_j$ be the characters of two irreducible representations of $G$ over $\mathbb{C}$. Then

$$
\frac{1}{|G|} \sum_{g \in G} \chi_i(g)\,\overline{\chi_j(g)} =
\begin{cases} 1, & \text{if the two representations are equivalent}, \\ 0, & \text{if the two representations are not equivalent}. \end{cases}
$$

Consequently a complex representation is determined (up to equivalence) by its character.

Denote the left-hand side by $\langle \chi_i, \chi_j \rangle$. By Maschke's theorem, every complex representation $\rho$ is equivalent to a direct sum of irreducible representations, and the number of summands equivalent to the $i$th irreducible representation equals $\langle \chi_\rho, \chi_i \rangle$. Furthermore:

**Theorem 6.4.3** Let $G$ be a finite group. The number of pairwise inequivalent irreducible representations of $G$ over $\mathbb{C}$ equals the number of conjugacy classes of $G$; if their dimensions are $d_1, \dots, d_k$, then

$$
d_1^2 + d_2^2 + \cdots + d_k^2 = |G|.
$$

**Example 6.4.1 (Character Table of $S_3$)** $S_3$ has three conjugacy classes (Section 2.6.2), so it has exactly three irreducible complex representations: the trivial representation $\chi_1$, the sign representation $\chi_2$ and the two-dimensional representation $\chi_3$ of Example 6.1.4; and $1^2 + 1^2 + 2^2 = 6 = |S_3|$. In the two-dimensional representation, a reflection has eigenvalues $1, -1$ and trace $0$, while the rotation through $120^\circ$ has trace $2\cos 120^\circ = -1$. This gives the character table (the first row shows in parentheses the number of elements of each conjugacy class):

| | $e$ ($1$) | transpositions ($3$) | $3$-cycles ($2$) |
| :--- | :---: | :---: | :---: |
| $\chi_1$ (trivial) | $1$ | $1$ | $1$ |
| $\chi_2$ (sign) | $1$ | $-1$ | $1$ |
| $\chi_3$ (two-dimensional) | $2$ | $0$ | $-1$ |

Checking the orthogonality relations: $\langle \chi_3, \chi_3 \rangle = \frac{1}{6}(1 \cdot 4 + 3 \cdot 0 + 2 \cdot 1) = 1$ and $\langle \chi_1, \chi_3 \rangle = \frac{1}{6}(2 + 0 - 2) = 0$. The character of the permutation representation is the number of fixed points of each permutation, $(3, 1, 0)$, and $\langle \chi, \chi_1 \rangle = \frac{1}{6}(3 + 3 + 0) = 1$, $\langle \chi, \chi_2 \rangle = \frac{1}{6}(3 - 3 + 0) = 0$, $\langle \chi, \chi_3 \rangle = \frac{1}{6}(6 + 0 + 0) = 1$, in agreement with the decomposition $\chi = \chi_1 + \chi_3$ of Example 6.1.4.

Since the point group $C_{3v}$ of $\mathrm{NH_3}$ is isomorphic to $S_3$ (Example 2.4.1), the table above is exactly the character table of $C_{3v}$ used in chemistry (where the three irreducible representations are denoted $A_1$, $A_2$ and $E$). Decomposing the representation spanned by the molecular vibrations with it tells which vibrational modes are visible in infrared or Raman spectra.

## 6.5. The Significance of Representation Theory

Representation theory makes the elements of abstract groups and Lie algebras concrete as linear transformations and thereby reveals the internal properties of these structures. Rings also have a representation theory (linear actions of a ring on abelian groups, called modules), which this course does not develop. In mathematics, the study of finite simple groups, Lie groups and algebraic groups relies heavily on representation theory. In physics, the classification of elementary particles and the analysis of atomic spectra are described by representations of groups and Lie algebras: the quantum theory of angular momentum is the representation theory of $SO(3)$ (and $SU(2)$), and the Standard Model of particle physics rests on representations of the gauge group $SU(3) \times SU(2) \times U(1)$.

In chemistry and structural biology, the symmetries of crystals are described by the $32$ crystallographic point groups and the $230$ space groups. Because proteins are built from chiral L-amino acids, protein crystals can belong only to the $65$ space groups whose symmetry operations (rotations, screw axes and translations) all preserve chirality; this is a basic constraint in solving structures by X-ray crystallography. Selection rules in molecular spectroscopy, the identification of symmetry-equivalent atoms, and rotation-equivariant molecular models are all direct applications of groups and their representations. Representation theory is thus one of the most direct bridges between abstract algebra and scientific applications.

## Summary

| Topic | Key concepts |
|------|----------|
| Group representations | a representation is a homomorphism into $\operatorname{GL}(V)$; linear actions; trivial, sign, permutation and regular representations |
| Structure | equivalent representations, $G$-equivariant maps, invariant subspaces, subrepresentations, direct sums, irreducible representations, Maschke's theorem |
| Lie algebra representations | homomorphisms into $\mathfrak{gl}(V)$, the adjoint representation, the irreducible representations $V(n)$ of $\mathfrak{sl}(2, \mathbb{C})$ and their weights |
| Lie groups and Lie algebras | the differential $\mathrm{d}\rho$ of a representation, commuting with the exponential map, angular momentum and spin, rotation equivariance |
| Characters | traces, class functions, Schur's lemma, orthogonality relations, number of irreducible representations equals number of conjugacy classes, character table of $S_3$ |

Looking back at the main line of the whole course: Chapter 1 provides the common language of algebraic systems, homomorphisms and quotient algebras; the groups of Chapter 2 describe symmetry; the rings and fields of Chapter 3 introduce two operations and supply the fields needed for vector spaces; the lattices and Boolean algebras of Chapter 4 start from order relations and connect logic with sets; the Lie algebras of Chapter 5 linearize continuous symmetry; and the representation theory of this chapter uses homomorphisms to realize groups and Lie algebras as matrices, making linear algebra a universal tool for the study of symmetry.
