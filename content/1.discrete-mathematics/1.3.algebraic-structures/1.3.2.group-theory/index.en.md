---
title: Group Theory
source_hash: 288666e3817d
---

A group is an algebraic system with a single binary operation that can be "undone". It is the basic language of symmetry: the symmetries of an object (the transformations preserving its structure) always form a group under composition. The previous chapter gave the general definitions of **algebraic systems**, **identity elements**, **inverse elements** and **homomorphisms**; this chapter develops these notions concretely for the most important class of systems.

We start from semigroups, where only associativity is required, and add an identity element and then inverses to arrive at groups. We then discuss subgroups, cyclic groups and permutation groups, use cosets to prove Lagrange's theorem and introduce group actions, construct quotient groups from normal subgroups, and finally use the fundamental homomorphism theorem to relate homomorphic images to quotient groups; this is the form that Theorem 1.4.4, "homomorphic images are quotient algebras", takes for groups. Groups underlie all the later chapters: the addition of a ring is an abelian group (Chapter 3), Lie algebras arise from continuous transformation groups (Chapter 5), and representation theory studies how groups act on vector spaces (Chapter 6).

## 2.1. Semigroups

### 2.1.1. Definition of a Semigroup

**Definition 2.1.1 (Semigroup)** Let $S$ be a nonempty set and $\cdot$ a binary operation on $S$. If $\cdot$ satisfies the **associative law**, that is, $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c \in S$, then the algebraic system $(S, \cdot)$ is called a semigroup.

For example:

- $(\mathbb{R}, +)$ is a semigroup, since addition is associative.
- $(M_n(\mathbb{R}), \cdot)$ (the set of real $n \times n$ matrices under matrix multiplication) is a semigroup.
- $(\mathbb{Z}_n, +)$ (addition modulo $n$) is a semigroup.
- $(\mathbb{R}, -)$ is not a semigroup, since subtraction is not associative.

### 2.1.2. Monoids

**Definition 2.1.2** If a semigroup $(M, \cdot)$ has an identity element $e$, then $(M, \cdot)$ is called a **monoid**; it is sometimes written as the triple $(M, \cdot, e)$.

For example:

- $(\mathbb{R}, +)$ is a monoid with identity $0$.
- $(M_n(\mathbb{R}), \cdot)$ is a monoid whose identity is the identity matrix $I_n$.
- $(\mathbb{Z}_n, +)$ is a monoid with identity $\bar{0}$.
- Let $\Sigma$ be an alphabet (for instance the DNA alphabet $\{\mathrm{A}, \mathrm{C}, \mathrm{G}, \mathrm{T}\}$) and $\Sigma^*$ the set of all finite strings over $\Sigma$. Then $\Sigma^*$ is a monoid under concatenation of strings, with the empty string as identity. It is a basic object of the theory of formal languages and automata; concatenation is not commutative, and no nonempty string has an inverse.

### 2.1.3. Commutative Monoids

**Definition 2.1.3** Let $(M, \cdot, e)$ be a monoid. If $\cdot$ satisfies the **commutative law** (that is, $a \cdot b = b \cdot a$ for all $a, b \in M$), then $M$ is called a **commutative monoid**.

For example:

- $(\mathbb{R}, +)$ is a commutative monoid.
- $(\mathbb{Z}_n, +)$ is a commutative monoid.
- For $n \ge 2$, $(M_n(\mathbb{R}), \cdot)$ is not a commutative monoid.

### 2.1.4. Cyclic Monoids

**Definition 2.1.4** Let $(M, \cdot, e)$ be a monoid (with the convention $g^0 = e$). If there is an element $g \in M$ such that every $a \in M$ can be written as a power $a = g^m$ of $g$ ($m$ a nonnegative integer), then $(M, \cdot, e)$ is called a **cyclic monoid**, and $g$ is called a **generator** of $M$.

**Theorem 2.1.1** Every cyclic monoid is a commutative monoid.

**Proof**: Let $g$ be a generator. For any $a, b \in M$ we have $a = g^m$ and $b = g^n$ ($m, n \ge 0$). By the laws of exponents (Theorem 1.3.1), $ab = g^m g^n = g^{m+n} = g^n g^m = ba$. $\square$

### 2.1.5. Subsemigroups and Submonoids

**Definition 2.1.5** Let $(S, \cdot)$ be a semigroup and $T$ a nonempty subset of $S$. If $T$ is closed under $\cdot$, then $(T, \cdot)$ is called a **subsemigroup** of $(S, \cdot)$.

**Definition 2.1.6** Let $(M, \cdot, e)$ be a monoid and $T \subseteq M$. If $T$ is closed under $\cdot$ and $e \in T$, then $(T, \cdot, e)$ is called a **submonoid** of $(M, \cdot, e)$.

### 2.1.6. Homomorphisms of Semigroups

Homomorphisms, monomorphisms, epimorphisms and isomorphisms of semigroups are special cases of Definitions 1.4.3, 1.4.5 and 1.4.2: maps $f\colon A \to B$ with $f(a \cdot b) = f(a) * f(b)$. By Theorem 1.4.2, an epimorphism carries associativity and the identity element over to the image, so we have:

**Theorem 2.1.2** Let $f$ be an epimorphism from the algebraic system $(A, \cdot)$ onto $(B, *)$, let $S$ be a nonempty subset of $A$, and let $f(S) = \{f(a) \mid a \in S\}$. Then:

1. if $(S, \cdot)$ is a semigroup, so is $(f(S), *)$;
2. if $(S, \cdot)$ is a monoid, so is $(f(S), *)$.

**Corollary**: Homomorphic images of semigroups, monoids and subsemigroups are again semigroups, monoids and subsemigroups.

Note that a homomorphism between monoids need not send the identity to the identity (it is only guaranteed to send it to the identity of the image $f(M)$; see the remark after Theorem 1.4.2). For groups this holds automatically (Theorem 2.7.3).

## 2.2. Basic Properties of Groups

### 2.2.1. Definition of a Group

**Definition 2.2.1 (Group)** Let $G$ be a nonempty set and $\cdot$ a binary operation on $G$. If the algebraic system $(G, \cdot)$ satisfies

1. the **associative law**: $(ab)c = a(bc)$ for all $a, b, c \in G$;
2. existence of an identity: there is $e \in G$ such that $ae = ea = a$ for all $a \in G$;
3. invertibility of every element: for every $a \in G$ there is $a^{-1} \in G$ with $aa^{-1} = a^{-1}a = e$,

then $(G, \cdot)$ is called a group, also written $(G, \cdot, e)$.

**Definition 2.2.2** Equivalently, Definition 2.2.1 can be stated as follows: a group is a monoid in which every element is invertible.

By Theorems 1.3.2 and 1.3.3, the identity of a group and the inverse of each element are unique; by Section 1.3.6, both the left and the right **cancellation laws** hold in a group.

For example, $(\mathbb{Z}, +)$, $(\mathbb{Z}_n, +)$ and $(\mathbb{R}_+, \cdot)$ are groups. The set $\operatorname{GL}(n, \mathbb{R})$ of invertible real matrices of order $n$ is a group under matrix multiplication, called the *general linear group* (for invertible matrices see [Linear Algebra](/2.1.2#def-2.2.3)); $(M_n(\mathbb{R}), \cdot)$, on the other hand, is only a monoid, because singular matrices are not invertible.

**Definition 2.2.3 (Abelian Group)** If the operation of a group $G$ satisfies the commutative law ($ab = ba$ for all $a, b \in G$), then $G$ is called a commutative group, or an **abelian group**.

### 2.2.2. Equivalent Definitions of a Group

**Theorem 2.2.1** Let the semigroup $(G, \cdot)$ have a left identity $e$, and suppose every $a \in G$ has a left inverse $a^{-1} \in G$ with $a^{-1}a = e$. Then $G$ is a group.

**Proof**: We first show that $a^{-1}$ is also a right inverse of $a$. Let $b$ be a left inverse of $a^{-1}$, that is, $ba^{-1} = e$. Then

$$
aa^{-1} = e(aa^{-1}) = (ba^{-1})(aa^{-1}) = b(a^{-1}a)a^{-1} = b(ea^{-1}) = ba^{-1} = e.
$$

Next we show that $e$ is also a right identity:

$$
ae = a(a^{-1}a) = (aa^{-1})a = ea = a.
$$

Hence $G$ is a group. $\square$

**Theorem 2.2.2** Let $(G, \cdot)$ be a semigroup. If for any two elements $a, b$ of $G$ the equations $ax = b$ and $ya = b$ both have solutions in $G$, then $G$ is a group.

### 2.2.3. Basic Properties of Groups

**Theorem 2.2.3** Let $G$ be a group. Then for all $a, b \in G$:

1. $(a^{-1})^{-1} = a$;
2. $(ab)^{-1} = b^{-1}a^{-1}$.

**Proof**: From $aa^{-1} = a^{-1}a = e$, $a$ is the inverse of $a^{-1}$, which gives 1. From $(ab)(b^{-1}a^{-1}) = a(bb^{-1})a^{-1} = e$ and $(b^{-1}a^{-1})(ab) = e$, statement 2 follows by uniqueness of inverses (Theorem 1.3.3). $\square$

### 2.2.4. Order of an Element

**Definition 2.2.4** Let $a$ be an element of a group $G$. If there is a positive integer $k$ with $a^k = e$, then the least such positive integer $k$ is called the **order** (or period) of $a$, written $O(a)$, and $a$ is called an **element of finite order**; if there is no such positive integer, $a$ is called an **element of infinite order**, and we write $O(a) = \infty$.

For additive groups, $a^k = e$ is to be read as $ka = 0$ (the additive notation of Section 1.3.5). For example, in $(\mathbb{Z}_6, +)$ we have $O(\bar{1}) = 6$, $O(\bar{2}) = 3$ and $O(\bar{3}) = 2$; in $\operatorname{GL}(2, \mathbb{R})$ the matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ of the counterclockwise rotation by $90^\circ$ has order $4$.

**Theorem 2.2.4** Let $a$ be an element of order $r$ in a group $G$ and let $k$ be an integer. Then:

1. $a^k = e$ if and only if $r \mid k$;
2. $O(a) = O(a^{-1})$;
3. if $G$ is finite, then $r \le |G|$.

### 2.2.5. Subgroups

**Definition 2.2.5 (Subgroup)** Let $H$ be a nonempty subset of a group $G$. If $H$ is itself a group under the operation of $G$, then $H$ is called a subgroup of $G$, written $H \le G$. The subgroups $G$ and $\{e\}$ are called the **trivial subgroups** of $G$. If $H \le G$ and $H \neq G$, then $H$ is called a **proper subgroup** of $G$, written $H < G$.

**Theorem 2.2.5** Let $H \le G$. Then the identity of $H$ is the identity $e$ of $G$, and the inverse of an element of $H$ in $H$ is its inverse in $G$. Consequently, a nonempty subset $H$ of $G$ is a subgroup if and only if:

1. $H$ is closed under the operation of $G$: $ab \in H$ for all $a, b \in H$;
2. $e \in H$;
3. $a^{-1} \in H$ for every $a \in H$ (where $a^{-1}$ is the inverse of $a$ in $G$).

**Theorem 2.2.6** A nonempty subset $H$ of $G$ is a subgroup of $G$ if and only if $ab^{-1} \in H$ for all $a, b \in H$.

**Theorem 2.2.7** If $A \le G$ and $B \le G$, then $A \cap B \le G$ and $A \cap B \le A$.

## 2.3. Cyclic Groups and Isomorphisms of Groups

### 2.3.1. Definition of a Cyclic Group

**Definition 2.3.1 (Cyclic Group)** If a group $G$ contains an element $a$ such that every element of $G$ is an (integer) power of $a$, that is, $G = \{a^k \mid k \in \mathbb{Z}\}$, then $G$ is called a cyclic group, written $G = \langle a \rangle$, and $a$ is called a **generator** of $G$. Here $a^0 = e$ and $a^{-k} = (a^{-1})^k$.

### 2.3.2. Generators of a Cyclic Group

**Theorem 2.3.1** Let $G = \langle a \rangle$. Then:

1. if $O(a) = \infty$, $G$ has exactly two generators, $a$ and $a^{-1}$;
2. if $O(a) = n$, then $a^k$ is a generator if and only if $\gcd(k, n) = 1$, so $G$ has $\varphi(n)$ generators, where $\varphi(n)$ is Euler's totient function (the number of positive integers not exceeding $n$ that are coprime to $n$).

For example, the generators of $\mathbb{Z}_6$ are $\bar{1}$ and $\bar{5}$, $\varphi(6) = 2$ in all.

### 2.3.3. Subgroups of a Cyclic Group

**Theorem 2.3.2** Let $G = \langle a \rangle$ be a cyclic group. Then:

1. every subgroup of $G$ is cyclic;
2. if $G$ is infinite, every subgroup $H \neq \{e\}$ of $G$ is infinite; if $G$ is finite with $|G| = n$ and $a^k$ is the least positive power of $a$ lying in the subgroup $H$, then $k \mid n$, $H = \langle a^k \rangle$ and $|H| = n/k$.

**Theorem 2.3.3** Let $G$ be a cyclic group of order $n$. Then for each positive divisor $d$ of $n$, $G$ has exactly one subgroup of order $d$.

### 2.3.4. Isomorphisms of Groups

An isomorphism of groups is an isomorphism in the sense of Definition 1.4.2: a bijection $f\colon G \to G'$ with $f(ab) = f(a) * f(b)$; we write $G \cong G'$. Isomorphic groups are the same group in the abstract sense.

**Example 2.3.1** Let $G = (\mathbb{R}_+, \cdot)$ (the multiplicative group of positive reals) and $G' = (\mathbb{R}, +)$, and let $f\colon x \mapsto \ln x$. Then $f$ is a bijection and

$$
f(xy) = \ln(xy) = \ln x + \ln y = f(x) + f(y),
$$

so $G \cong G'$.

### 2.3.5. Classification of Cyclic Groups up to Isomorphism

**Theorem 2.3.4** Let $G$ be a cyclic group with generator $a$. Then:

1. if $O(a) = \infty$, then $G \cong (\mathbb{Z}, +)$;
2. if $O(a) = n$, then $G \cong (\mathbb{Z}_n, +)$.

**Corollary**: Any two cyclic groups of the same order are isomorphic.

## 2.4. Transformation Groups and Permutation Groups: Cayley's Theorem

### 2.4.1. Transformations and Bijective Transformations

Let $A$ be a nonempty set. A **map** from $A$ to $A$ is called a transformation of $A$. A transformation that is a **bijection** is called a bijective transformation. The set of all transformations of $A$ is denoted $M(A)$; if $|A| = n$, then $|M(A)| = n^n$.

### 2.4.2. Transformation Groups

**Definition 2.4.1** The group formed by all bijective transformations of a nonempty set $A$ under the product (composition) of transformations is called the **group of bijective transformations** of $A$ (also known as the symmetric group on $A$) and is denoted $E(A)$. A subgroup of $E(A)$ is called a **transformation group**.

### 2.4.3. Permutations and Symmetric Groups

When $A$ is a finite set with $|A| = n$, a bijective transformation of $A$ is called a *permutation* of degree $n$. The set of all permutations of degree $n$ is denoted $S_n$; it has $n!$ elements. The product $\sigma\tau$ of permutations means "first $\tau$, then $\sigma$", in agreement with composition of maps.

**Definition 2.4.2 (Symmetric Group)** $S_n$ is a group under the product of permutations, called the **symmetric group of degree $n$**. A subgroup of $S_n$ is called a **permutation group of degree $n$**.

**Example 2.4.1** Label the vertices of an equilateral triangle $1, 2, 3$. There are $6$ rigid motions of the plane that map the triangle to itself: the three rotations through $0^\circ$, $120^\circ$ and $240^\circ$, and the three reflections in the axes of symmetry. Each motion permutes the three vertices, and every permutation in $S_3$ is realized by exactly one motion, so the symmetry group of the equilateral triangle is isomorphic to $S_3$: the rotation through $120^\circ$ corresponds to the cycle $(1\ 2\ 3)$, and the reflection in the axis through vertex $1$ corresponds to $(2\ 3)$. This group is not commutative: performing $(2\ 3)$ first and then $(1\ 2\ 3)$ gives $(1\ 2\ 3)(2\ 3) = (1\ 2)$, whereas $(2\ 3)(1\ 2\ 3) = (1\ 3)$.

![The six symmetries of an equilateral triangle and the Cayley table of $S_3$. Top: where the numbered vertices go under each symmetry; $r$ is the rotation by $120^\circ$ (the cycle $(1\ 2\ 3)$) and $s_i$ the reflection in the axis through vertex $i$ (dashed). Bottom: row $x$, column $y$ holds $xy$ (first $y$, then $x$); every element occurs once in each row and column, and the table is not symmetric about its diagonal because the group is not commutative](./plots/triangle-s3.py)

This is exactly how chemistry describes the symmetry of molecules: the ammonia molecule $\ce{NH3}$ is a trigonal pyramid, and its symmetry operations (rotations about the central axis and reflections in three mirror planes) form the point group $C_{3\mathrm{v}}$, which is isomorphic to the $S_3$ above.

### 2.4.4. Cycles and Transpositions

Let $i_1, i_2, \dots, i_l$ be $l$ distinct elements. If a permutation $\sigma$ satisfies $\sigma(i_1) = i_2$, $\sigma(i_2) = i_3$, …, $\sigma(i_l) = i_1$ and fixes all other elements, then $\sigma$ is called a *cyclic permutation* (or simply cycle) of length $l$, written $(i_1\ i_2\ \cdots\ i_l)$. A cycle of length $2$ is called a *transposition*. Two cycles with no element in common are called disjoint.

**Theorem 2.4.1** Disjoint cycles commute.

**Theorem 2.4.2** Every permutation in $S_n$ can be written as a product of disjoint cycles, and this representation is unique up to the order of the factors and the omission of cycles of length $1$.

**Lemma 2.4.1** Every cycle can be written as a product of transpositions (not uniquely); for example,

$$
(1\ 2\ 3\ 4) = (2\ 3)(3\ 4)(4\ 1) = (1\ 4)(1\ 3)(1\ 2).
$$

In computational biology, when the genomes of two species are compared, the order of genes (or conserved segments) along a chromosome can be viewed as a permutation, and genome rearrangements such as inversions and translocations amount to multiplying it by permutations of particular types. The rearrangement distance problem, "transform one gene order into another with as few inversions as possible", is formulated in the language of permutation groups.

### 2.4.5. Parity of Permutations

**Definition 2.4.3** Let $i_1 i_2 \cdots i_n$ be an arrangement of $1, 2, \dots, n$. If $k < l$ and $i_k > i_l$, the pair $i_k i_l$ is called an **inversion**. The total number of inversions in the arrangement is called its **number of inversions**.

**Lemma 2.4.2** Let $\sigma \in S_n$ with $\sigma(j) = i_j$ ($j = 1, \dots, n$). Whenever $\sigma$ is written as a product of transpositions, the number of transpositions has the same parity as the number of inversions of the arrangement $i_1 i_2 \cdots i_n$.

The parity of a permutation is therefore well defined: a permutation that is a product of an odd number of transpositions is called an *odd permutation*, and one that is a product of an even number of transpositions is called an *even permutation*.

**Theorem 2.4.3** The set of all even permutations in the symmetric group $S_n$ is a subgroup under the product of permutations, denoted $A_n$ and called the *alternating group*. For $n \ge 2$, $|A_n| = \frac{1}{2} n!$.

### 2.4.6. Cayley's Theorem

**Theorem 2.4.4 (Cayley's Theorem)** Every group $G$ is isomorphic to a transformation group.

**Proof**: For each $a \in G$ define the transformation $f_a\colon x \mapsto ax$ of $G$. Each $f_a$ is a bijective transformation with inverse $f_{a^{-1}}$, and $f_a f_b = f_{ab}$. Hence $\bar{G} = \{f_a \mid a \in G\}$ is a subgroup of $E(G)$, that is, a transformation group. The map $\varphi\colon a \mapsto f_a$ preserves the operation; and if $f_a = f_b$, then $a = f_a(e) = f_b(e) = b$. So $\varphi$ is an isomorphism from $G$ onto $\bar{G}$. $\square$

**Corollary**: A finite group $G$ of order $n$ is isomorphic to a subgroup of $S_n$; that is, every finite group is isomorphic to a permutation group.

## 2.5. Cosets and Lagrange's Theorem

### 2.5.1. Left and Right Cosets

**Definition 2.5.1 (Coset)** Let $H$ be a subgroup of a group $G$. For any $a \in G$, the set $aH = \{ah \mid h \in H\}$ is called a **left coset** of $H$ in $G$; similarly, the set $Ha = \{ha \mid h \in H\}$ is called a **right coset**.

### 2.5.2. Properties of Left Cosets

**Theorem 2.5.1** Let $H \le G$. Left cosets have the following properties:

1. $H = eH$ and $a \in aH$;
2. $|aH| = |H|$; that is, each left coset is related to $H$ by **equinumerosity**, via the bijection $h \mapsto ah$;
3. $a \in H \iff aH = H$;
4. $xH = aH$ for every $x \in aH$; that is, any element of a coset can serve as its representative;
5. $aH = bH \iff a \in bH \iff b^{-1}a \in H$;
6. if $aH \neq bH$, then $aH \cap bH = \varnothing$.

### 2.5.3. Coset Decomposition and Index

Properties 5 and 6 show that the relation "$a \sim b \iff b^{-1}a \in H$" is an **equivalence relation** on $G$ (Definition 1.2.2) and that the left coset $aH$ is precisely the **equivalence class** of $a$. By Theorem 1.2.2, the left cosets form a **partition** of $G$; the **quotient set** $G/{\sim}$ is denoted $G/H$.

**Theorem 2.5.2** Let $G$ be a finite group and $H \le G$. Then there are $a_1, \dots, a_k \in G$ such that

$$
G = a_1 H \cup a_2 H \cup \cdots \cup a_k H,
$$

where the cosets are pairwise disjoint.

**Definition 2.5.2** The number of left cosets of a subgroup $H$ in a group $G$ is called the **index** of $H$ in $G$, written $[G:H]$. (The map $aH \mapsto Ha^{-1}$ is a bijection between left and right cosets, so counting right cosets gives the same number.)

![Cosets and the quotient group. A: the subgroup $H = \{0, 3\}$ splits $\mathbb{Z}_6$ into three cosets of equal size, $H$, $1 + H$ and $2 + H$ (one colour each), and $6 = 3 \times 2$ as Lagrange's theorem requires. B: the cosets, added as sets, form the quotient group $\mathbb{Z}_6/H$, whose table is that of $\mathbb{Z}_3$](./plots/z6-cosets.py)

### 2.5.4. Lagrange's Theorem

**Theorem 2.5.3 (Lagrange's Theorem)** Let $G$ be a finite group and $H \le G$. Then

$$
|G| = [G:H] \cdot |H|;
$$

that is, the order of a subgroup divides the order of the group.

**Proof**: By Theorem 2.5.2, $G$ is the union of $[G:H]$ pairwise disjoint left cosets, and by Theorem 2.5.1 each left coset has $|H|$ elements. $\square$

**Corollary 2.5.1** Let $G$ be a finite group of order $n$. Then the order of every element $a \in G$ divides $n$, and $a^n = e$.

**Corollary 2.5.2** A group $G$ of prime order $p$ is cyclic.

**Corollary 2.5.3** Let $A, B$ be finite subgroups of a group $G$ and $AB = \{ab \mid a \in A, b \in B\}$. Then

$$
|AB| = \frac{|A| \cdot |B|}{|A \cap B|}.
$$

Note that in general $AB$ is only a subset of $G$, not necessarily a subgroup.

### 2.5.5. Group Actions and Orbits

Groups most often appear as a family of transformations of some set; for example, the symmetry group of Example 2.4.1 acts on the vertices of the triangle. Abstracting this situation gives the notion of a group action.

**Definition 2.5.3 (Group Action)** Let $G$ be a group and $A$ a nonempty set. If a map $G \times A \to A$, $(g, x) \mapsto g \cdot x$, satisfies

1. $e \cdot x = x$ for every $x \in A$;
2. $g \cdot (h \cdot x) = (gh) \cdot x$ for all $g, h \in G$ and $x \in A$,

then we say that $G$ acts on $A$.

By conditions 1 and 2, the transformation $\sigma_g\colon x \mapsto g \cdot x$ determined by each $g$ is a bijective transformation (with inverse $\sigma_{g^{-1}}$), and $g \mapsto \sigma_g$ is a homomorphism from $G$ to the group of bijective transformations $E(A)$; conversely, every homomorphism $G \to E(A)$ defines a group action. The proof of Cayley's theorem uses precisely the action of $G$ on itself by left multiplication, $g \cdot x = gx$.

**Definition 2.5.4 (Orbit and Stabilizer)** Let a group $G$ act on a set $A$ and let $x \in A$. The set $G \cdot x = \{g \cdot x \mid g \in G\}$ is called the **orbit** of $x$, and $G_x = \{g \in G \mid g \cdot x = x\}$ is called the **stabilizer** of $x$.

The relation "$y = g \cdot x$ for some $g \in G$" is an equivalence relation on $A$ (reflexivity comes from $e$, symmetry from inverses, transitivity from condition 2), and its equivalence classes are the orbits; so $A$ is partitioned into pairwise disjoint orbits. It is easy to check that $G_x \le G$.

**Theorem 2.5.4 (Orbit–Stabilizer Theorem)** Let a finite group $G$ act on a set $A$ and let $x \in A$. Then

$$
|G \cdot x| = [G : G_x];
$$

in particular, the length of every orbit divides $|G|$.

**Proof**: For $g, h \in G$, $g \cdot x = h \cdot x \iff (h^{-1}g) \cdot x = x \iff h^{-1}g \in G_x \iff gG_x = hG_x$ (property 5 of Theorem 2.5.1). Hence $gG_x \mapsto g \cdot x$ is a bijection from the set of left cosets of $G_x$ onto the orbit $G \cdot x$. $\square$

**Example 2.5.1** In Example 2.4.1, the symmetry group of the triangle acting on the three vertices has a single orbit (any vertex can be moved to any other), and the stabilizer of vertex $1$ is $\{e, (2\ 3)\}$. Check: $|G \cdot 1| = 3 = 6/2 = [G : G_1]$. For a molecule, the symmetry group acts on the atoms, and atoms in the same orbit are equivalent under symmetry, such as the three hydrogen atoms of $\ce{NH3}$.

## 2.6. Normal Subgroups and Quotient Groups

### 2.6.1. Definition of a Normal Subgroup

**Definition 2.6.1 (Normal Subgroup)** Let $H$ be a subgroup of $G$. If $aH = Ha$ for every $a \in G$, then $H$ is called a normal subgroup (or **invariant subgroup**) of $G$, written $H \triangleleft G$. In this case there is no need to distinguish left and right cosets; both are simply called **cosets**.

Every subgroup of an abelian group is normal; $\{e\}$ and $G$ are always normal subgroups of $G$.

### 2.6.2. Equivalent Conditions for Normality

**Theorem 2.6.1** Let $H \le G$. The following conditions are equivalent:

1. $H \triangleleft G$;
2. $gHg^{-1} = H$ for every $g \in G$;
3. $gHg^{-1} \subseteq H$ for every $g \in G$;
4. $ghg^{-1} \in H$ for all $g \in G$ and $h \in H$.

**Definition 2.6.2 (Conjugate)** Let $a, b \in G$. If there is $g \in G$ with $b = gag^{-1}$, then $a$ and $b$ are said to be **conjugate**. Conjugacy is an equivalence relation on $G$; its equivalence classes are called **conjugacy classes**.

Condition 4 of Theorem 2.6.1 says that a normal subgroup is a union of complete conjugacy classes. In $S_n$, two permutations are conjugate if and only if their decompositions into disjoint cycles have the same multiset of cycle lengths (the same cycle type). For example, $S_3$ has three conjugacy classes: $\{e\}$, the three transpositions, and the two $3$-cycles. Conjugacy classes play a key role in the character theory of Chapter 6.

### 2.6.3. Properties of Normal Subgroups

**Theorem 2.6.2** Let $A, B$ be subgroups of $G$.

1. If $A \triangleleft G$ and $B \triangleleft G$, then $A \cap B \triangleleft G$ and $AB \triangleleft G$;
2. if $A \triangleleft G$ and $B \le G$, then $A \cap B \triangleleft B$ and $AB \le G$.

### 2.6.4. Quotient Groups

**Theorem 2.6.3** Let $H \triangleleft G$ and let $G/H = \{gH \mid g \in G\}$ be the set of all cosets of $H$. Then $G/H$ is a group under coset multiplication

$$
(aH)(bH) = abH,
$$

called the *quotient group* of $G$ by $H$.

**Proof**: We first show that coset multiplication does not depend on the choice of representatives. If $aH = a'H$ and $bH = b'H$, then $a' = ah_1$ and $b' = bh_2$ with $h_1, h_2 \in H$, so

$$
a'b' = ah_1bh_2 = ab\,(b^{-1}h_1b)\,h_2 \in abH,
$$

where we used normality, $b^{-1}h_1b \in H$; hence $a'b'H = abH$. Associativity is inherited from $G$, the identity is $H = eH$, and the inverse of $aH$ is $a^{-1}H$. $\square$

For finite groups, Lagrange's theorem gives $|G/H| = [G:H] = |G|/|H|$.

In the language of Chapter 1, the proof above verifies exactly that, when $H$ is normal, the coset relation "$a \sim b \iff aH = bH$" is a **congruence relation** on $(G, \cdot)$ (Definition 1.4.7), and $G/H$ is the corresponding **quotient algebra** (Theorem 1.4.3). Conversely, one can show that every congruence relation on a group arises in this way from a normal subgroup (the congruence class of the identity). Normal subgroups are therefore exactly the subgroups of a group that one can "divide by".

For example, $A_3 = \{e, (1\ 2\ 3), (1\ 3\ 2)\} \triangleleft S_3$, and $S_3/A_3$ is a group of order $2$ whose two elements are "rotations" and "reflections" (Example 2.4.1); but $H = \{e, (2\ 3)\}$ is not normal, because $(1\ 2)(2\ 3)(1\ 2) = (1\ 3) \notin H$.

## 2.7. Homomorphisms of Groups and the Fundamental Homomorphism Theorem

### 2.7.1. Definition of a Group Homomorphism

A group homomorphism is a homomorphism in the sense of Definition 1.4.3: a map $f\colon G_1 \to G_2$ with $f(ab) = f(a)f(b)$ (the right-hand side being computed in $G_2$); monomorphisms, epimorphisms and isomorphisms are as in Definition 1.4.5. We write $G_1 \sim G_2$ when there is an epimorphism from $G_1$ onto $G_2$, and call $G_2$ a **homomorphic image** of $G_1$.

For example, the determinant $\det\colon \operatorname{GL}(n, \mathbb{R}) \to (\mathbb{R} \setminus \{0\}, \cdot)$ is an epimorphism ($\det(AB) = \det A \det B$); the sign map $\operatorname{sgn}\colon S_n \to (\{1, -1\}, \cdot)$, sending even permutations to $1$ and odd permutations to $-1$, is a homomorphism; and $k \mapsto \bar{k}$ is an epimorphism from $(\mathbb{Z}, +)$ onto $(\mathbb{Z}_n, +)$.

### 2.7.2. Basic Properties of Homomorphisms

**Lemma 2.7.1** If $H \triangleleft G$, then the **canonical map** $\gamma\colon a \mapsto aH$ is an epimorphism from $G$ onto $G/H$.

**Theorem 2.7.1** If $f$ is a homomorphism from $G_1$ to $G_2$ and $g$ is a homomorphism from $G_2$ to $G_3$, then $gf$ is a homomorphism from $G_1$ to $G_3$.

**Theorem 2.7.2** Let $G$ be a group and $(G', \cdot)$ an algebraic system with a binary operation. If $f\colon G \to G'$ is surjective and preserves the operation, then $G'$ is also a group, and $G \sim G'$. In other words, a homomorphic image of a group under an epimorphism is again a group.

**Theorem 2.7.3** Let $f$ be a homomorphism from $G$ to $G'$ and let $e'$ be the identity of $G'$. Then:

1. $f(e) = e'$ (the image of the identity is the identity);
2. $f(a^{-1}) = (f(a))^{-1}$ for every $a \in G$;
3. if $H \le G$, then $f(H) \le G'$ and $H \sim f(H)$.

### 2.7.3. The Kernel of a Homomorphism

**Definition 2.7.2 (Kernel)** Let $f\colon G \to G'$ be a homomorphism and $e'$ the identity of $G'$. The set $K = \{a \in G \mid f(a) = e'\}$ is called the kernel of $f$, written $\ker f$.

**Theorem 2.7.4** $\ker f$ is a normal subgroup of $G$.

**Proof**: For $a, b \in K$, $f(ab^{-1}) = f(a)f(b)^{-1} = e'$, so $ab^{-1} \in K$, and $K \le G$ by Theorem 2.2.6. Moreover, for any $g \in G$ and $k \in K$, $f(g^{-1}kg) = f(g)^{-1}f(k)f(g) = f(g)^{-1}f(g) = e'$, so $g^{-1}kg \in K$, and $K \triangleleft G$ by Theorem 2.6.1. $\square$

### 2.7.4. Kernels and Cosets

**Theorem 2.7.5** Let $f$ be a homomorphism from $G$ to $G'$ and $K = \ker f$. Then for all $a, b \in G$,

$$
f(a) = f(b) \iff b \in aK \iff aK = bK.
$$

That is, elements of the same coset have the same image, and elements of different cosets have different images.

**Theorem 2.7.6** Let $f$ be a homomorphism from $G$ to $G'$. Then $f$ is a monomorphism if and only if $\ker f = \{e\}$.

### 2.7.5. The Fundamental Homomorphism Theorem

**Theorem 2.7.7 (Fundamental Homomorphism Theorem)** Let $G$ be a group. Then:

1. every quotient group of $G$ is a homomorphic image of $G$;
2. conversely, if $f$ is an epimorphism from $G$ onto $G'$ and $K = \ker f$, then $G' \cong G/K$.

**Proof**: Statement 1 is Lemma 2.7.1. For 2, define $\varphi\colon G/K \to G'$ by $\varphi(aK) = f(a)$. By Theorem 2.7.5, $aK = bK \iff f(a) = f(b)$, so $\varphi$ does not depend on the choice of representatives and is injective; since $f$ is surjective, so is $\varphi$; and $\varphi(aK \cdot bK) = \varphi(abK) = f(ab) = f(a)f(b) = \varphi(aK)\varphi(bK)$. Hence $\varphi$ is an isomorphism. $\square$

In other words, up to isomorphism the homomorphic images of a group $G$ are exactly its quotient groups: a homomorphic image is isomorphic to the quotient group by the kernel. This is a concrete instance of Theorem 1.4.4: the equivalence classes of the congruence relation $\sim_f$ determined by $f$ are exactly the cosets of $\ker f$ (Theorem 2.7.5).

For instance, in the examples above, $\ker \operatorname{sgn} = A_n$, so $S_n / A_n \cong \{1, -1\}$ ($n \ge 2$); $\ker \det = \operatorname{SL}(n, \mathbb{R})$ (the matrices of determinant $1$), so $\operatorname{GL}(n, \mathbb{R}) / \operatorname{SL}(n, \mathbb{R}) \cong (\mathbb{R} \setminus \{0\}, \cdot)$; and the kernel of the epimorphism from $(\mathbb{Z}, +)$ onto $\mathbb{Z}_n$ is $n\mathbb{Z}$, so $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$.

## 2.8. Direct Products of Groups

**Definition 2.8.1 (Direct Product)** Let $G_1, G_2$ be groups. On the **Cartesian product** $G_1 \times G_2 = \{(g_1, g_2) \mid g_1 \in G_1, g_2 \in G_2\}$ define the operation $(g_1, g_2)(h_1, h_2) = (g_1 h_1, g_2 h_2)$. Then $G_1 \times G_2$ is a group under this operation, called the **direct product** of $G_1$ and $G_2$. Its identity is $(e_1, e_2)$, and the inverse of $(g_1, g_2)$ is $(g_1^{-1}, g_2^{-1})$.

For example, $\mathbb{Z}_2 \times \mathbb{Z}_3 \cong \mathbb{Z}_6$ (the element $(\bar{1}, \bar{1})$ has order $6$ and is a generator), whereas $\mathbb{Z}_2 \times \mathbb{Z}_2$ is not cyclic (every non-identity element has order $2$).

![The two groups of order 4. Left: the cyclic group $\mathbb{Z}_4$, whose elements have orders $1, 4, 2, 4$. Right: the Klein four-group $V = \mathbb{Z}_2 \times \mathbb{Z}_2$, in which every element is its own inverse (the diagonal is all $e$) and the product of any two non-identity elements is the third. $\mathbb{Z}_4$ has an element of order 4 and $V$ does not, so they are not isomorphic](./plots/z4-klein.py)

![The groups of order at most 8 up to isomorphism, 14 in all: a prime order admits only the cyclic group (Lagrange's theorem); order 4 gives $\mathbb{Z}_4$ or the Klein four-group according to whether an element of order 4 exists; order 6 gives $\mathbb{Z}_6$ and the non-abelian $S_3$; order 8 gives three abelian groups (by the structure theorem for finite abelian groups) and two non-abelian ones, the dihedral group $D_4$ and the quaternion group $Q_8$](./plots/groups-up-to-8.py)

## Summary

| Topic | Key concepts and theorems |
|------|----------------|
| Semigroups | associative law, semigroup, monoid, cyclic monoid, subsemigroup, homomorphism |
| Groups | definition of a group, abelian group, order of an element, subgroups and the subgroup criteria |
| Cyclic groups | generators, structure of subgroups, classification up to isomorphism ($\mathbb{Z}$ or $\mathbb{Z}_n$) |
| Transformation and permutation groups | transformations, bijective transformations, symmetric group $S_n$, cycle decomposition, parity, alternating group $A_n$, Cayley's theorem |
| Cosets and Lagrange's theorem | properties of left cosets, coset decomposition, index, Lagrange's theorem and its corollaries, group actions, the orbit–stabilizer theorem |
| Normal subgroups and quotient groups | equivalent conditions for normality, conjugacy classes, construction of quotient groups (the coset relation is a congruence) |
| Homomorphisms and the fundamental theorem | properties of homomorphisms, kernel, the kernel is a normal subgroup, fundamental homomorphism theorem (homomorphic images are isomorphic to quotient groups) |
| Direct products | direct product of two groups |

Group theory is one of the core subjects of abstract algebra. In computer science, the discrete logarithm in finite cyclic groups underlies public-key cryptography such as the Diffie–Hellman key exchange, and permutation groups are used to analyze sorting, shuffling and the symmetries of graphs. In chemistry and structural biology, point groups describe the symmetry of molecules, and many viral capsids have icosahedral symmetry, whose rotation group is isomorphic to the alternating group $A_5$ of order $60$.

A group has only one operation. The integers, however, have both addition and multiplication: $(\mathbb{Z}, +)$ is a cyclic group, and multiplication turns it into a richer structure. The next chapter studies two operations linked by the distributive law, namely rings and fields; the subgroups, normal subgroups, quotient groups and fundamental homomorphism theorem of this chapter all have point-by-point counterparts there.
