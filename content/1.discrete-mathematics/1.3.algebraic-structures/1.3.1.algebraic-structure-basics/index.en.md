---
title: Fundamentals of Algebraic Structures
source_hash: 9058eadae890
---

Algebraic structures are "sets equipped with operations": we do not care what the elements are, only which laws the operations obey. Addition of integers, multiplication of matrices, composition of permutations, and intersection and union of sets look unrelated, yet they obey the same laws of associativity, identity elements and inverses. If we isolate these laws and study them on their own, every conclusion we reach applies at once to all objects that satisfy them.

This chapter is the common language of the whole course; each later chapter adds specific axioms to the framework set up here. A single operation that can be "undone" gives a group (Chapter 2); two operations, addition and multiplication, linked by the distributive law give rings and fields (Chapter 3); two operations derived from an order relation give lattices and Boolean algebras (Chapter 4); a non-associative bracket operation on a vector space gives a Lie algebra (Chapter 5); and representation theory (Chapter 6) uses homomorphisms to realize these abstract structures as matrices. We first review **sets**, maps and **equivalence relations** (discussed in more detail in [Set Theory](/1.2)), then introduce algebraic operations, algebraic systems, identity elements and inverses, and finally compare algebraic systems by homomorphisms and isomorphisms and build quotient algebras from congruence relations. The quotient algebra is the common prototype of the quotient groups, quotient rings and quotient Lie algebras of the later chapters.

## 1.1. Sets and Maps

### 1.1.1. Basic Notions

Let $S$ be any set. If an element $a$ belongs to $S$ we write $a \in S$; otherwise we write $a \notin S$. The number of distinct elements of $S$ is called the **cardinal number** (or cardinality) of $S$ and is denoted $|S|$.

Once a set $S$ is given, it determines another set $\mathcal{P}(S)$: the set of all subsets of $S$, called the **power set** of $S$. When $S$ is finite, the cardinality of $\mathcal{P}(S)$ is $2^{|S|}$.

An element $A$ of $\mathcal{P}(S)$, that is, a subset of $S$, can be described as

$$
A = \{x \in S \mid P(x)\},
$$

where $P$ stands for some property; $A$ is then the set of elements of $S$ having property $P$.

Intersection and union distribute over each other:

$$
A \cap (B \cup C) = (A \cap B) \cup (A \cap C), \qquad A \cup (B \cap C) = (A \cup B) \cap (A \cup C).
$$

### 1.1.2. Definition of a Map

**Definition 1.1.1** Let $S$ and $T$ be two given sets. If there is a rule $f$ that assigns to every element $x \in S$ a unique element $y \in T$, then $f$ is called a **map** from $S$ to $T$, written $f: S \to T$ and $y = f(x)$ (or $f: x \mapsto y$). The set $S$ is called the domain of $f$ and $T$ its codomain (some texts call it the range); $y$ is called the image of $x$, and $x$ a preimage of $y$.

By definition:

- every element of $S$ has an image in $T$;
- an element of $T$ need not have a preimage in $S$;
- the set of images of all elements of $S$ is called the image of $f$ and is denoted $f(S)$; clearly $f(S) \subseteq T$.

### 1.1.3. Equality of Maps

**Definition 1.1.2** Let $f: A_1 \to B_1$ and $g: A_2 \to B_2$ be maps. We say that $f$ and $g$ are **equal maps**, written $f = g$, if and only if $A_1 = A_2$, $B_1 = B_2$, and $f(x) = g(x)$ for every $x \in A_1$.

### 1.1.4. Injections, Surjections and Bijections

**Definition 1.1.3** Let $f$ be a map from $A$ to $B$.

1. If for all $a_i, a_j \in A$, $a_i \neq a_j$ implies $f(a_i) \neq f(a_j)$, then $f$ is called an **injection** (a one-to-one map) from $A$ to $B$;
2. if $f(A) = B$, then $f$ is called a **surjection** from $A$ onto $B$;
3. if $f$ is both injective and surjective, it is called a **bijection** (a one-to-one correspondence) between $A$ and $B$.

### 1.1.5. Composition of Maps

**Definition 1.1.4** Let $A$, $B$, $C$ be sets and let $f: A \to B$ and $g: B \to C$ be maps. Then $f$ and $g$ determine a map $h: A \to C$, $a \mapsto g(f(a))$, called the **composition** of $f$ and $g$ and written $h = gf$ (or $g \circ f$); that is,

$$
h(a) = (gf)(a) = g(f(a)).
$$

Composition of maps is in general not commutative, but it is associative: if $\alpha: A \to B$, $\beta: B \to C$ and $\gamma: C \to D$, then

$$
\gamma(\beta\alpha) = (\gamma\beta)\alpha.
$$

### 1.1.6. Identity Maps

The map $I_A: A \to A$, $a \mapsto a$, is called the **identity map** on $A$.

**Theorem 1.1.1** Let $f$ be a map from $A$ to $B$, and let $I_A$ and $I_B$ be the identity maps on $A$ and $B$. Then

$$
I_B f = f, \quad f I_A = f.
$$

### 1.1.7. Invertible Maps

**Definition 1.1.5** Let $f: A \to B$ and $g: B \to A$ be maps. If $gf = I_A$, then $f$ is called a **left invertible map** and $g$ a **right invertible map**; $g$ is called a left inverse of $f$, and $f$ a right inverse of $g$. If in addition $fg = I_B$, then $f$ and $g$ are both called **invertible maps**, and $g$ is called the inverse of $f$.

**Theorem 1.1.2** Let $A$ be a nonempty set and $f$ a map from $A$ to $B$. Then:

- $f$ is left invertible if and only if $f$ is injective;
- $f$ is right invertible if and only if $f$ is surjective.

**Corollary**: A map $f: A \to B$ is invertible if and only if $f$ is a bijection.

**Theorem 1.1.3** Let $f$ be a map from $A$ to $B$, and let $g, h: B \to A$ satisfy $gf = I_A$ and $fh = I_B$. Then $g = h$. Consequently the inverse of an invertible map is unique; it is denoted $f^{-1}$.

**Proof**: $g = g I_B = g(fh) = (gf)h = I_A h = h$. $\square$

## 1.2. Equivalence Relations

### 1.2.1. Binary Relations

**Definition 1.2.1** Any subset $R$ of the **Cartesian product** $A \times B$ of sets $A$ and $B$ is called a **binary relation** between $A$ and $B$. If $(a, b) \in R$, where $a \in A$ and $b \in B$, we write $aRb$. When $A = B$, $R$ is called a binary relation on $A$.

### 1.2.2. Definition of an Equivalence Relation

**Definition 1.2.2 (Equivalence Relation)** Let $R$ be a binary relation on a set $A$. If

1. **reflexivity**: $aRa$ for all $a \in A$;
2. **symmetry**: for all $a, b \in A$, $aRb$ implies $bRa$;
3. **transitivity**: for all $a, b, c \in A$, $aRb$ and $bRc$ imply $aRc$,

then $R$ is called an equivalence relation on $A$; it is usually denoted by $\sim$.

### 1.2.3. Equivalence Classes

Let $\sim$ be an equivalence relation on a set $A$. For any $a \in A$, the set of all elements equivalent to $a$ is called the **equivalence class** of $a$ and is denoted $\bar{a}$:

$$
\bar{a} = \{x \in A \mid x \sim a\}.
$$

The element $a$ is called a representative of this class.

Equivalence classes have the following properties:

1. $a \in \bar{a}$;
2. if $b, c \in \bar{a}$, then $b \sim c$ (any two elements of the same class are equivalent);
3. if $b \in \bar{a}$ and $b \sim x$, then $x \in \bar{a}$ (an element equivalent to a member of the class also lies in the class).

**Theorem 1.2.1** Let $\sim$ be an equivalence relation on $A$. For any $a, b \in A$, if $\bar{b} \neq \bar{a}$, then $\bar{b} \cap \bar{a} = \varnothing$.

**Theorem 1.2.2** Let $\{\bar{a}_i\}_{i \in I}$ be all the (pairwise distinct) equivalence classes of an equivalence relation $\sim$ on $A$. Then

$$
\bigcup_{i \in I} \bar{a}_i = A, \quad \bar{a}_i \cap \bar{a}_j = \varnothing \ (i \neq j);
$$

that is, the equivalence relation $\sim$ determines a **partition** of $A$: $A$ is divided into nonempty, pairwise disjoint subsets.

### 1.2.4. Quotient Sets and the Canonical Map

The set of all equivalence classes of $\sim$ is called the family of equivalence classes and is denoted $\overline{A}$:

$$
\overline{A} = \{\bar{a} \mid a \in A\}.
$$

To indicate that this family is determined by $\sim$, we usually write it as $A/{\sim}$ and call it the **quotient set** of $A$ by $\sim$.

Once the quotient set $A/{\sim}$ is fixed, each $a \in A$ belongs to exactly one equivalence class $\bar{a}$. The map $\gamma: A \to A/{\sim}$, $a \mapsto \bar{a}$, is called the **canonical map** from $A$ to $A/{\sim}$. The canonical map is surjective.

### 1.2.5. Partitions and Equivalence Relations

**Theorem 1.2.3** A partition of a set $A$ determines an equivalence relation on $A$.

**Proof**: Let $\{A_i\}_{i \in I}$ be a partition of $A$: each $A_i$ is nonempty, they are pairwise disjoint, and $\bigcup_{i \in I} A_i = A$. Define the relation

$$
R = \{(x, y) \mid x \in A_i \text{ and } y \in A_i \text{ for some } i \in I\}.
$$

Every $x \in A$ lies in some $A_i$, so $xRx$; the definition of $R$ is symmetric in $x$ and $y$, so $R$ is symmetric; if $xRy$ and $yRz$, then $x, y \in A_i$ and $y, z \in A_j$, and since $y \in A_i \cap A_j$ while the blocks are pairwise disjoint, $i = j$, hence $xRz$. Therefore $R$ is an equivalence relation, and its equivalence classes are exactly the sets $A_i$. $\square$

## 1.3. Algebraic Systems

### 1.3.1. Algebraic Operations

**Definition 1.3.1** Let $A$ be a nonempty set. A map $f: A^2 \to A$ from $A^2 = A \times A$ to $A$ is called a **binary algebraic operation** on $A$, or simply a **binary operation**.

**Definition 1.3.2** Let $A$ be a nonempty set. A map $f: A^n \to A$ is called an **$n$-ary algebraic operation** on $A$, or simply an **$n$-ary operation**.

Binary operations are usually written in infix form: $f(a, b)$ is written $a \cdot b$ or $ab$.

### 1.3.2. Definition of an Algebraic System

**Definition 1.3.3 (Algebraic System)** Let $A$ be a nonempty set and let $f_1, f_2, \dots, f_s$ be operations on $A$ of arities $k_1, k_2, \dots, k_s$ (positive integers). The system consisting of the set $A$ and the operations $f_1, f_2, \dots, f_s$ is called an algebraic system (or **algebraic structure**), or simply an **algebra**, and is written $(A, f_1, f_2, \dots, f_s)$. When $A$ is a finite set, the system is called a **finite algebraic system**.

For example:

- $(\mathbb{R}, +, \cdot)$ is an algebraic system, where $\mathbb{R}$ is the set of real numbers with ordinary addition and multiplication.
- $(M_n(\mathbb{R}), \cdot)$ is an algebraic system, where $M_n(\mathbb{R})$ is the set of all real $n \times n$ matrices with ordinary matrix multiplication.
- Let $\mathbb{Z}_n = \{\bar{0}, \bar{1}, \dots, \overline{n-1}\}$ be the set of equivalence classes of integers under congruence modulo $n$, and define $\bar{i} + \bar{j} = \overline{i + j}$ on $\mathbb{Z}_n$ (add, then take the remainder modulo $n$). Then $(\mathbb{Z}_n, +)$ is an algebraic system; this operation is called addition modulo $n$. Similarly, $\bar{i} \cdot \bar{j} = \overline{ij}$ is called multiplication modulo $n$. Both operations are independent of the choice of representatives; see Section 1.4.8.
- For a set $S$, $(\mathcal{P}(S), \cup, \cap)$ is an algebraic system with two binary operations; it reappears in Chapter 4 as the basic example of a lattice and a Boolean algebra.

In this course a binary operation is generally written $\cdot$ (often omitted); other symbols such as $+$ are used only to distinguish two operations on the same set.

### 1.3.3. Laws of Operations

Let $(X, \cdot)$ be an algebraic system with a binary operation $\cdot$.

If $x_i \cdot x_j = x_j \cdot x_i$ for all $x_i, x_j \in X$, we say that $\cdot$ satisfies the *commutative law*.

If $(x_i \cdot x_j) \cdot x_k = x_i \cdot (x_j \cdot x_k)$ for all $x_i, x_j, x_k \in X$, we say that $\cdot$ satisfies the *associative law*.

In an algebraic system satisfying the associative law, a product of several elements does not depend on how it is parenthesized, so we can define positive integer powers: $x^1 = x$, $x^{n+1} = x^n \cdot x$.

If $X$ carries another binary operation $+$ and for all $x, y, z \in X$

$$
x \cdot (y + z) = x \cdot y + x \cdot z, \qquad (y + z) \cdot x = y \cdot x + z \cdot x,
$$

we say that $\cdot$ satisfies the *distributive law* over $+$. The distributive law is what ties two operations together; it is central to both rings (Chapter 3) and distributive lattices (Chapter 4).

**Theorem 1.3.1 (Laws of Exponents)** If the binary operation $\cdot$ of $(X, \cdot)$ satisfies the associative law, then for every $x \in X$ and all positive integers $m$, $n$:

1. $x^m \cdot x^n = x^{m+n}$;
2. $(x^m)^n = x^{mn}$.

### 1.3.4. Identity Elements

**Definition 1.3.4 (Identity Element)** Let $V = (X, \cdot)$ be an algebraic system. If there is $e_L \in X$ such that $e_L \cdot x = x$ for every $x \in X$, then $e_L$ is called a **left identity** of $X$ with respect to $\cdot$; similarly, an element $e_R$ with $x \cdot e_R = x$ for every $x \in X$ is called a **right identity**. An element that is both a left and a right identity is called an identity element.

**Theorem 1.3.2** If an algebraic system $V = (X, \cdot)$ has both a left identity $e_L$ and a right identity $e_R$, then $e_L = e_R$; this element, denoted $e$, is the unique identity element of $X$.

**Proof**: $e_L = e_L \cdot e_R = e_R$. If $e'$ is also an identity element, then $e' = e' \cdot e = e$. $\square$

For example:

- the identity element of $(\mathbb{R}, +)$ is $0$;
- the identity element of $(\mathbb{R}, \cdot)$ is $1$;
- $0$ is a right identity of $(\mathbb{R}, -)$ (since $x - 0 = x$), but $(\mathbb{R}, -)$ has no left identity.

### 1.3.5. Inverse Elements

**Definition 1.3.5 (Inverse Element)** Let $V = (X, \cdot)$ be an algebraic system with identity element $e$, and let $x \in X$.

- If there is $x' \in X$ with $x' \cdot x = e$, then $x$ is called **left invertible** and $x'$ is called a **left inverse** of $x$;
- if there is $x'' \in X$ with $x \cdot x'' = e$, then $x$ is called **right invertible** and $x''$ is called a **right inverse** of $x$;
- if $x$ is both left and right invertible, it is called an **invertible element**; an element that is both a left and a right inverse of $x$ is called an inverse of $x$.

**Theorem 1.3.3** Let the algebraic system $V = (X, \cdot)$ have an identity element $e$ and satisfy the associative law. If $x \in X$ has a left inverse $x'$ and a right inverse $x''$, then $x' = x''$; it is the unique inverse of $x$, denoted $x^{-1}$, and

$$
(x^{-1})^{-1} = x.
$$

**Proof**: $x' = x' e = x'(x x'') = (x' x) x'' = e x'' = x''$. The same argument shows that every left inverse equals every right inverse, so the inverse is unique. Since $x^{-1} x = x x^{-1} = e$, $x$ is the inverse of $x^{-1}$. $\square$

When the operation is written $+$ and is commutative, we use additive notation: the identity element is written $0$ and called the zero element; the inverse of $x$ is written $-x$ and called its negative; and the $n$th power of $x$ is written as the multiple $nx = x + x + \cdots + x$. For example, the zero element of $(\mathbb{Z}_n, +)$ is $\bar{0}$, and the negative of $\bar{1}$ is $\overline{n-1}$. The group-theoretic theorems of Chapter 2 are stated in multiplicative notation; to apply them to groups written additively, one only has to translate in this way. Addition in the rings of Chapter 3 uses additive notation.

### 1.3.6. Cancellation Laws

Let the algebraic system $V = (X, \cdot)$ have an identity element and satisfy the associative law. If $a \in X$ is invertible, then for all $b, c \in X$

$$
ab = ac \Rightarrow b = c, \qquad ba = ca \Rightarrow b = c;
$$

these are the *cancellation laws*. For instance, $ab = ac$ gives $b = (a^{-1}a)b = a^{-1}(ab) = a^{-1}(ac) = c$. Hence if every element of $V$ is invertible, cancellation holds throughout $V$.

Associativity cannot be dropped here: in a system without the associative law, cancellation may fail even if every element has an inverse.

## 1.4. Isomorphisms and Homomorphisms

### 1.4.1. Algebraic Systems of the Same Type

**Definition 1.4.1** Let $V_1 = (X, o_1, o_2, \dots, o_r)$ and $V_2 = (Y, \bar{o}_1, \bar{o}_2, \dots, \bar{o}_r)$ be algebraic systems. If for each $i$ both $o_i$ and $\bar{o}_i$ are $k_i$-ary operations, then $V_1$ and $V_2$ are said to be **of the same type**.

### 1.4.2. Isomorphisms

**Definition 1.4.2 (Isomorphism)** Let $(X, \cdot)$ and $(Y, *)$ be algebraic systems of the same type and let $f: X \to Y$ be a bijection. If $f(a \cdot b) = f(a) * f(b)$ for all $a, b \in X$, then $f$ is called an **isomorphism** from $(X, \cdot)$ to $(Y, *)$, and $(X, \cdot)$ and $(Y, *)$ are said to be isomorphic, written $X \cong Y$.

Isomorphic algebraic systems differ only in the "names" of their elements; their operations obey exactly the same laws.

### 1.4.3. Homomorphisms

**Definition 1.4.3 (Homomorphism)** Let $(X, \cdot)$ and $(Y, *)$ be algebraic systems of the same type and let $f: X \to Y$ be a map. If $f(a \cdot b) = f(a) * f(b)$ for all $a, b \in X$, then $f$ is called a **homomorphism** from $(X, \cdot)$ to $(Y, *)$.

An isomorphism is precisely a bijective homomorphism.

The definitions above treat a single binary operation. If $V_1 = (X, o_1, \dots, o_r)$ and $V_2 = (Y, \bar{o}_1, \dots, \bar{o}_r)$ are of the same type, a homomorphism $f$ must preserve each pair of corresponding operations: for each $k_i$-ary operation $o_i$,

$$
f(o_i(a_1, \dots, a_{k_i})) = \bar{o}_i(f(a_1), \dots, f(a_{k_i})).
$$

Ring homomorphisms (Definition 3.3.1), which preserve both addition and multiplication, and lattice homomorphisms (Definition 4.4.2), which preserve both join and meet, are of this kind. The theorems of this section hold equally for several operations; the proofs need only be checked operation by operation.

### 1.4.4. Subalgebras

**Definition 1.4.4** Let $(X, \cdot)$ be an algebraic system and $R$ a nonempty subset of $X$. If $R$ is **closed** under $\cdot$ (that is, $a, b \in R$ implies $a \cdot b \in R$), then $(R, \cdot)$ is called a **subalgebra** (or subsystem) of $(X, \cdot)$.

**Theorem 1.4.1** Let $f: X \to Y$ be a homomorphism from the algebraic system $(X, \cdot)$ to $(Y, *)$. Then $(f(X), *)$ is a subalgebra of $(Y, *)$, and $f(X)$ is called the *homomorphic image* of $X$ under $f$.

**Proof**: $f(X)$ is nonempty, and for $f(a), f(b) \in f(X)$ we have $f(a) * f(b) = f(a \cdot b) \in f(X)$. $\square$

### 1.4.5. Monomorphisms and Epimorphisms

**Definition 1.4.5** Let $f: X \to Y$ be a homomorphism from the algebraic system $(X, \cdot)$ to $(Y, *)$.

- If $f$ is injective, $f$ is called a **monomorphism** (an injective homomorphism);
- if $f$ is surjective, $f$ is called an **epimorphism**, written $X \sim Y$; in this case $Y = f(X)$ is a homomorphic image of $X$.

### 1.4.6. Basic Properties of Homomorphisms

**Theorem 1.4.2** Let $(X, \cdot)$ and $(Y, *)$ be algebraic systems in which $\cdot$ and $*$ are binary operations, and let $f: X \to Y$ be an epimorphism from $(X, \cdot)$ to $(Y, *)$. Then:

1. if $\cdot$ satisfies the commutative (associative) law, so does $*$;
2. if $(X, \cdot)$ has an identity element $e$, then $f(e)$ is the identity element of $(Y, *)$;
3. if $(X, \cdot)$ has an identity element and every $x \in X$ has an inverse $x^{-1}$, then every element $f(x) \in Y$ has the inverse $f(x^{-1})$.

Surjectivity cannot be dropped: in general, for instance, the image $f(e)$ of the identity is only guaranteed to be the identity element of $f(X)$.

### 1.4.7. Endomorphisms and Automorphisms

**Definition 1.4.6** A homomorphism $f: X \to X$ from an algebraic system $(X, \cdot)$ to itself is called an **endomorphism**; if $f$ is moreover an isomorphism, it is called an **automorphism**.

The automorphisms of a system form a group under composition (Chapter 2). This group describes the "symmetries" of the system: the ways of renaming its elements that leave the whole operational structure unchanged.

### 1.4.8. Congruence Relations and Quotient Algebras

The quotient set $A/{\sim}$ of Section 1.2 is just a set. If the equivalence relation is compatible with the operation, the quotient set inherits the operation; this is the basic method for building new algebraic systems from known ones.

**Definition 1.4.7 (Congruence Relation)** Let $(X, \cdot)$ be an algebraic system and $\sim$ an equivalence relation on $X$. If for all $a, a', b, b' \in X$, $a \sim a'$ and $b \sim b'$ always imply $a \cdot b \sim a' \cdot b'$, then $\sim$ is called a congruence relation on $(X, \cdot)$.

For example, congruence of integers modulo $n$: if $a \equiv a'$ and $b \equiv b' \pmod n$, then $a + b \equiv a' + b'$ and $ab \equiv a'b' \pmod n$, so it is a congruence relation on both $(\mathbb{Z}, +)$ and $(\mathbb{Z}, \cdot)$.

**Theorem 1.4.3** Let $\sim$ be a congruence relation on $(X, \cdot)$. Then

$$
\bar{a} \cdot \bar{b} = \overline{a \cdot b}
$$

is a well-defined binary operation on the quotient set $X/{\sim}$, and the canonical map $\gamma: a \mapsto \bar{a}$ is an epimorphism from $(X, \cdot)$ onto $(X/{\sim}, \cdot)$. The system $(X/{\sim}, \cdot)$ is called the *quotient algebra* of $X$ by $\sim$.

**Proof**: If $\bar{a} = \bar{a}'$ and $\bar{b} = \bar{b}'$, that is, $a \sim a'$ and $b \sim b'$, then by the congruence property $a \cdot b \sim a' \cdot b'$, that is, $\overline{a \cdot b} = \overline{a' \cdot b'}$; so the result does not depend on the choice of representatives. The map $\gamma$ is surjective (Section 1.2.4), and $\gamma(a \cdot b) = \overline{a \cdot b} = \bar{a} \cdot \bar{b} = \gamma(a) \cdot \gamma(b)$. $\square$

By Theorem 1.4.2, a quotient algebra automatically inherits the commutative and associative laws, the identity element ($\bar{e}$) and inverses (the inverse of $\bar{a}$ is $\overline{a^{-1}}$) of the original system. The system $(\mathbb{Z}_n, +)$ is exactly the quotient algebra of $(\mathbb{Z}, +)$ by congruence modulo $n$.

Conversely, every homomorphism gives rise to a congruence relation:

**Theorem 1.4.4** Let $f: X \to Y$ be a homomorphism from $(X, \cdot)$ to $(Y, *)$. Define $a \sim_f b \iff f(a) = f(b)$ on $X$. Then $\sim_f$ is a congruence relation, and $\varphi: \bar{a} \mapsto f(a)$ is an isomorphism from the quotient algebra $X/{\sim_f}$ onto the homomorphic image $f(X)$.

**Proof**: Clearly $\sim_f$ is reflexive, symmetric and transitive. If $f(a) = f(a')$ and $f(b) = f(b')$, then $f(a \cdot b) = f(a) * f(b) = f(a') * f(b') = f(a' \cdot b')$, so $\sim_f$ is a congruence relation. By the definition of $\sim_f$, $\bar{a} = \bar{b} \iff f(a) = f(b)$, so $\varphi$ does not depend on representatives and is injective; it is clearly surjective onto $f(X)$; and $\varphi(\bar{a} \cdot \bar{b}) = \varphi(\overline{a \cdot b}) = f(a \cdot b) = f(a) * f(b) = \varphi(\bar{a}) * \varphi(\bar{b})$. $\square$

Together, Theorems 1.4.3 and 1.4.4 say that, up to isomorphism, the homomorphic images of an algebraic system are exactly its quotient algebras. The "fundamental homomorphism theorems" of later chapters are all concrete instances of this result; they differ only in which substructure determines the congruence relation: a normal subgroup for groups (Theorem 2.7.7), an ideal for rings (Theorem 3.3.3), and again an ideal for Lie algebras (Theorem 5.2.3).

## Summary

| Topic | Key concepts |
|------|----------|
| Sets and maps | injection, surjection, bijection, composition, invertible map |
| Equivalence relations | reflexivity, symmetry, transitivity, equivalence class, quotient set, partition |
| Algebraic systems | algebraic operation, identity element, inverse element, cancellation law |
| Laws of operations | commutative, associative and distributive laws; additive notation (zero element, negative) |
| Isomorphism and homomorphism | systems of the same type, isomorphism, homomorphism, subalgebra, properties of epimorphisms, automorphism |
| Quotient algebras | congruence relation, quotient algebra, isomorphism between homomorphic images and quotient algebras |

The next chapter starts from systems with a single binary operation: requiring only associativity gives semigroups, adding an identity element gives monoids, and finally requiring every element to be invertible gives groups. The uniqueness of the identity (Theorem 1.3.2) and of inverses (Theorem 1.3.3), the cancellation laws and the properties of homomorphisms (Theorem 1.4.2) from this chapter are all used there directly.
