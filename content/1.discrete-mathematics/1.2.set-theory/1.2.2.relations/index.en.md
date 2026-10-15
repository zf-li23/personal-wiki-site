---
title: Relations
source_hash: ce6508d5f3f2
---

Relations describe connections between the elements of sets. This chapter defines a relation as a set of ordered pairs (see Definition 1.3.4), introduces the representations of relations (matrices and graphs), their operations (inverse, composition, restriction and image), their basic properties (reflexivity, symmetry, antisymmetry and transitivity) and their closures, and then discusses three important kinds of relations: equivalence relations and their correspondence with partitions, compatibility relations and covers, and partial orders and partially ordered sets. The functions of the next chapter are a special kind of relation.

## 2.1. Binary Relations

A set is called a *binary relation*, or simply a relation, if it is empty or all of its elements are **ordered pairs**; relations are commonly denoted by $R$. For a binary relation $R$, we also write $xRy$ for $\langle x, y \rangle \in R$.

**Definition 2.1.1 (Binary Relation from $A$ to $B$)** Let $A$ and $B$ be sets. The binary relation given by any subset of $A \times B$ is called a binary relation from $A$ to $B$. In particular, when $A = B$, any subset of $A \times A$ is called a binary relation on $A$.

**Definition 2.1.2 ($n$-ary Relation)** Let $n \in \mathbb{N}$ with $n > 1$, and let $A_1, A_2, \cdots, A_n$ be $n$ sets. Any subset of $A_1 \times A_2 \times \cdots \times A_n$ is called an **$n$-ary relation** on $A_1, A_2, \cdots, A_n$; it is a set of $n$-tuples.

Let $A$ be a family of sets. The inclusion relation and the proper inclusion relation on $A$ are defined by

$$
\begin{aligned}
R_{\subseteq} &= \{\langle x, y \rangle \mid x \in A \land y \in A \land x \subseteq y\}, \\
R_{\subset} &= \{\langle x, y \rangle \mid x \in A \land y \in A \land x \subset y\}.
\end{aligned}
$$

For example, for any set $A$, the inclusion relation on the **power set** $\mathcal{P}(A)$ is $\{\langle x, y \rangle \mid x \in \mathcal{P}(A) \land y \in \mathcal{P}(A) \land x \subseteq y\}$.

**Definition 2.1.3 (Identity Relation, Universal Relation and Empty Relation)** For every set $A$,

1. the **identity relation** on $A$ is $I_A = \{\langle x, x \rangle \mid x \in A\}$;
2. the **universal relation** (full relation) on $A$ is $E_A = \{\langle x, y \rangle \mid x \in A \land y \in A\} = A \times A$;
3. the empty set $\varnothing$, being a subset of $A \times A$, is called the **empty relation** on $A$.

**Definition 2.1.4 (Domain and Range)** Let $R$ be a binary relation from $A$ to $B$.

1. The set of first coordinates of all ordered pairs in $R$ is called the **domain** of $R$, written $\operatorname{dom}(R) = \{x \mid (\exists y)(\langle x, y \rangle \in R)\}$;
2. the set of second coordinates of all ordered pairs in $R$ is called the **range** of $R$, written $\operatorname{ran}(R) = \{y \mid (\exists x)(\langle x, y \rangle \in R)\}$;
3. the union of the domain and the range of $R$ is called the field of $R$, written $\operatorname{fld}(R) = \operatorname{dom}(R) \cup \operatorname{ran}(R)$.

## 2.2. Relation Matrices and Relation Graphs

**Definition 2.2.1 (Relation Matrix)** Let $X = \{x_1, x_2, \cdots, x_m\}$ and $Y = \{y_1, y_2, \cdots, y_n\}$ be sets, and let $R$ be a relation from $X$ to $Y$. The **relation matrix** of $R$ is the $m \times n$ matrix $M(R) = (r_{ij})_{m \times n}$, where

$$
r_{ij} =
\begin{cases}
1, & \langle x_i, y_j \rangle \in R, \\
0, & \langle x_i, y_j \rangle \notin R,
\end{cases}
\qquad 1 \leq i \leq m,\ 1 \leq j \leq n.
$$

If $R$ is a relation on $X$, its relation matrix is an $m \times m$ square matrix, defined in the same way.

**Definition 2.2.2 (Relation Graph)** Let $X = \{x_1, x_2, \cdots, x_m\}$ and $Y = \{y_1, y_2, \cdots, y_n\}$.

1. If $R$ is a relation from $X$ to $Y$, the **relation graph** of $R$ is the directed graph $G(R) = (V, E)$ with vertex set $V = X \cup Y$, in which the directed edge $e_{ij}$ from $x_i$ to $y_j$ belongs to $E$ if and only if $\langle x_i, y_j \rangle \in R$.
2. If $R$ is a relation on $X$, its relation graph is the special case of the above with vertex set $X$.

## 2.3. Inverse, Composition, Restriction and Image of Relations

**Definition 2.3.1 (Inverse, Composition, Restriction and Image of Relations)** For a relation $R$ from $X$ to $Y$ and a relation $S$ from $Y$ to $Z$, define:

1. the inverse $R^{-1}$ of $R$ is the relation from $Y$ to $X$ given by
   $$
   R^{-1} = \{\langle y, x \rangle \mid \langle x, y \rangle \in R\};
   $$
2. the **composition** $S \circ R$ of $R$ and $S$ (called the left composition in some books) is the relation from $X$ to $Z$ given by
   $$
   S \circ R = \{\langle x, z \rangle \mid (\exists y)(\langle x, y \rangle \in R \land \langle y, z \rangle \in S)\};
   $$
3. for any set $A$, the **restriction** $R \upharpoonright A$ of $R$ to $A$ is the relation from $A$ to $Y$ given by
   $$
   R \upharpoonright A = \{\langle x, y \rangle \mid \langle x, y \rangle \in R \land x \in A\};
   $$
4. the image $R[A]$ of $A$ under $R$ is the set
   $$
   R[A] = \{y \mid (\exists x)(x \in A \land \langle x, y \rangle \in R)\}.
   $$

The relation matrix of a composition can be computed by the Boolean product of matrices. Let $A$ be a finite set with $|A| = n$, and let $R$ and $S$ be relations on $A$ with relation matrices the $n \times n$ square matrices $M(R) = (r_{ij})$ and $M(S) = (s_{ij})$. Then

$$
M(S \circ R) = M(R) \cdot M(S) = (w_{ij})_{n \times n}, \qquad w_{ij} = \bigvee_{k=1}^{n} (r_{ik} \land s_{kj}),
$$

where $\cdot$ denotes the Boolean product (like ordinary matrix multiplication, but with multiplication replaced by $\land$ and addition by $\lor$). Note the order of the factors: $S \circ R$ applies $R$ first and then $S$, so the corresponding product has $M(R)$ on the left and $M(S)$ on the right.

**Theorem 2.3.1 (Properties of the Inverse)** For a relation $R$ from $X$ to $Y$ and a relation $S$ from $Y$ to $Z$,

$$
\begin{aligned}
\operatorname{dom}(R^{-1}) &= \operatorname{ran}(R), & \operatorname{ran}(R^{-1}) &= \operatorname{dom}(R), \\
(R^{-1})^{-1} &= R, & (S \circ R)^{-1} &= R^{-1} \circ S^{-1}.
\end{aligned}
$$

**Theorem 2.3.2 (Associativity of Composition)** For a relation $Q$ from $X$ to $Y$, a relation $S$ from $Y$ to $Z$ and a relation $R$ from $Z$ to $W$,

$$
(R \circ S) \circ Q = R \circ (S \circ Q).
$$

**Theorem 2.3.3 (Further Properties of Composition)** For relations $R_2, R_3$ from $X$ to $Y$ and a relation $R_1$ from $Y$ to $Z$,

$$
\begin{aligned}
R_1 \circ (R_2 \cup R_3) &= R_1 \circ R_2 \cup R_1 \circ R_3, \\
R_1 \circ (R_2 \cap R_3) &\subseteq R_1 \circ R_2 \cap R_1 \circ R_3;
\end{aligned}
$$

and for a relation $R_3$ from $X$ to $Y$ and relations $R_1, R_2$ from $Y$ to $Z$,

$$
\begin{aligned}
(R_1 \cup R_2) \circ R_3 &= R_1 \circ R_3 \cup R_2 \circ R_3, \\
(R_1 \cap R_2) \circ R_3 &\subseteq R_1 \circ R_3 \cap R_2 \circ R_3.
\end{aligned}
$$

Here composition of relations is taken to bind more tightly than the set operations. The two inclusions cannot in general be replaced by equalities. For example, take $X = Y = Z = \{a, b\}$, $R_1 = \{\langle a, a \rangle, \langle b, a \rangle\}$, $R_2 = \{\langle a, a \rangle\}$ and $R_3 = \{\langle a, b \rangle\}$; then $R_2 \cap R_3 = \varnothing$, whereas $R_1 \circ R_2 \cap R_1 \circ R_3 = \{\langle a, a \rangle\}$.

**Theorem 2.3.4 (Properties of Images under a Relation)** For a relation $R$ from $X$ to $Y$, sets $A, B$ and a family of sets $\mathcal{A}$,

$$
\begin{aligned}
R[A \cup B] &= R[A] \cup R[B], \\
R\left[\textstyle\bigcup \mathcal{A}\right] &= \textstyle\bigcup \{R[B] \mid B \in \mathcal{A}\}, \\
R[A \cap B] &\subseteq R[A] \cap R[B], \\
R\left[\textstyle\bigcap \mathcal{A}\right] &\subseteq \textstyle\bigcap \{R[B] \mid B \in \mathcal{A}\} \quad (\mathcal{A} \neq \varnothing), \\
R[A] - R[B] &\subseteq R[A - B].
\end{aligned}
$$

## 2.4. Properties of Relations

**Definition 2.4.1 (Reflexivity and Irreflexivity)** Let $R$ be a relation on a set $A$. If $xRx$ for every element $x$ of $A$, then $R$ is said to be reflexive on $A$, or $R$ is called a **reflexive relation** on $A$; if there is no element $x$ of $A$ with $xRx$, then $R$ is said to be irreflexive on $A$, or $R$ is called an **irreflexive relation**. In symbols,

$$
\begin{aligned}
R \text{ is reflexive on } A &\Leftrightarrow (\forall x)(x \in A \rightarrow \langle x, x \rangle \in R), \\
R \text{ is irreflexive on } A &\Leftrightarrow (\forall x)(x \in A \rightarrow \langle x, x \rangle \notin R).
\end{aligned}
$$

**Definition 2.4.2 (Symmetry and Antisymmetry)** Let $R$ be a relation on a set $A$. If for all $x, y$ in $A$, $xRy$ always implies $yRx$, then $R$ is said to be symmetric, or $R$ is called a **symmetric relation** on $A$; if $xRy$ and $yRx$ together always imply $x = y$, then $R$ is said to be antisymmetric, or $R$ is called an **antisymmetric relation** on $A$. In symbols,

$$
\begin{aligned}
R \text{ is symmetric} &\Leftrightarrow (\forall x)(\forall y)((x \in A \land y \in A \land \langle x, y \rangle \in R) \rightarrow \langle y, x \rangle \in R), \\
R \text{ is antisymmetric} &\Leftrightarrow (\forall x)(\forall y)((x \in A \land y \in A \land \langle x, y \rangle \in R \land \langle y, x \rangle \in R) \rightarrow x = y).
\end{aligned}
$$

An equivalent definition of antisymmetry is

$$
R \text{ is antisymmetric} \Leftrightarrow (\forall x)(\forall y)((x \in A \land y \in A \land \langle x, y \rangle \in R \land x \neq y) \rightarrow \langle y, x \rangle \notin R).
$$

**Definition 2.4.3 (Transitivity)** Let $R$ be a relation on a set $A$. If $xRy$ and $yRz$ always imply $xRz$, then $R$ is said to be transitive, or $R$ is called a **transitive relation** on $A$. In symbols,

$$
R \text{ is transitive} \Leftrightarrow (\forall x)(\forall y)(\forall z)((x, y, z \in A \land \langle x, y \rangle \in R \land \langle y, z \rangle \in R) \rightarrow \langle x, z \rangle \in R).
$$

**Theorem 2.4.1 (Preservation of Reflexivity)** If $R_1, R_2$ are reflexive relations on $A$, then $R_1^{-1}$, $R_1 \cap R_2$ and $R_1 \cup R_2$ are also reflexive relations on $A$.

**Theorem 2.4.2 (Preservation of Symmetry)** If $R_1, R_2$ are symmetric relations on $A$, then $R_1^{-1}$, $R_1 \cap R_2$ and $R_1 \cup R_2$ are also symmetric relations on $A$.

**Theorem 2.4.3 (Preservation of Transitivity)** If $R_1, R_2$ are transitive relations on $A$, then $R_1^{-1}$ and $R_1 \cap R_2$ are transitive relations on $A$, but $R_1 \cup R_2$ need not be transitive.

For example, on $A = \{a, b, c\}$ both $R_1 = \{\langle a, b \rangle\}$ and $R_2 = \{\langle b, c \rangle\}$ are transitive, but $R_1 \cup R_2$ contains $\langle a, b \rangle$ and $\langle b, c \rangle$ without containing $\langle a, c \rangle$, so it is not transitive.

**Theorem 2.4.4 (Preservation of Antisymmetry)** If $R_1, R_2$ are antisymmetric relations on $A$, then $R_1^{-1}$ and $R_1 \cap R_2$ are antisymmetric relations on $A$, but $R_1 \cup R_2$ need not be antisymmetric.

For example, $R_1 = \{\langle a, b \rangle\}$ and $R_2 = \{\langle b, a \rangle\}$ are both antisymmetric, whereas $R_1 \cup R_2$ is not.

**Theorem 2.4.5 (Characterizations of Symmetry and Antisymmetry)** Let $R$ be a relation on $A$. Then

1. $R$ is symmetric $\Leftrightarrow R = R^{-1}$;
2. $R$ is antisymmetric $\Leftrightarrow R \cap R^{-1} \subseteq I_A$.

## 2.5. Closures of Relations

**Definition 2.5.1 (Powers of a Relation)** Let $R$ be a relation on $A$ and $n \in \mathbb{N}$. The $n$th power of $R$ is defined by

$$
\begin{aligned}
R^0 &= I_A = \{\langle x, x \rangle \mid x \in A\}, \\
R^{n+1} &= R^n \circ R \quad (n \geq 0).
\end{aligned}
$$

**Theorem 2.5.1 (Powers of a Relation on a Finite Set Repeat)** Let $A$ be a finite set with $|A| = n$, and let $R$ be a relation on $A$. Then there are natural numbers $s$ and $t$ with $s \neq t$ such that $R^s = R^t$.

This is because there are only $2^{n^2}$ distinct relations on $A$, while the sequence $R^0, R^1, R^2, \cdots$ has infinitely many terms.

**Theorem 2.5.2 (Laws of Powers)** Let $R$ be a relation on $A$, and let $m$ and $n$ be natural numbers. Then

$$
R^m \circ R^n = R^{m+n}, \qquad (R^m)^n = R^{mn}.
$$

**Theorem 2.5.3 (Periodicity of the Powers of a Relation on a Finite Set)** Let $A$ be a finite set and $R$ a relation on $A$. If there are natural numbers $s$ and $t$ with $s < t$ such that $R^s = R^t$, then

1. $R^{s+k} = R^{t+k}$ for $k \in \mathbb{N}$;
2. $R^{s+lp+i} = R^{s+i}$ for $l, i \in \mathbb{N}$, where $p = t - s$;
3. with $B = \{R^0, R^1, \cdots, R^{t-1}\}$, every power of $R$ is an element of $B$; that is, $R^q \in B$ for every $q \in \mathbb{N}$.

**Definition 2.5.2 (Closures)** Let $R$ be a relation on a nonempty set $A$. The **reflexive closure** (**symmetric closure**, **transitive closure**) of $R$ is the relation $R'$ on $A$ satisfying the following conditions:

1. $R'$ is reflexive (symmetric, transitive);
2. $R \subseteq R'$;
3. for every reflexive (symmetric, transitive) relation $R''$ on $A$ that includes $R$, we have $R' \subseteq R''$.

The reflexive closure of $R$ is written $r(R)$, the symmetric closure $s(R)$ and the transitive closure $t(R)$. They are, respectively, the smallest reflexive (symmetric, transitive) relations that include $R$.

**Theorem 2.5.4 (Properties of Closures, I)** For a relation $R$ on a nonempty set $A$,

1. $R$ is reflexive $\Leftrightarrow r(R) = R$;
2. $R$ is symmetric $\Leftrightarrow s(R) = R$;
3. $R$ is transitive $\Leftrightarrow t(R) = R$.

**Theorem 2.5.5 (Properties of Closures, II)** For relations $R_1, R_2$ on a nonempty set $A$, if $R_1 \subseteq R_2$, then

$$
r(R_1) \subseteq r(R_2), \qquad s(R_1) \subseteq s(R_2), \qquad t(R_1) \subseteq t(R_2).
$$

**Theorem 2.5.6 (Properties of Closures, III)** For relations $R_1, R_2$ on a nonempty set $A$,

$$
\begin{aligned}
r(R_1) \cup r(R_2) &= r(R_1 \cup R_2), \\
s(R_1) \cup s(R_2) &= s(R_1 \cup R_2), \\
t(R_1) \cup t(R_2) &\subseteq t(R_1 \cup R_2).
\end{aligned}
$$

**Theorem 2.5.7 (Construction of the Reflexive Closure)** For a relation $R$ on a nonempty set $A$,

$$
r(R) = R \cup I_A.
$$

**Theorem 2.5.8 (Construction of the Symmetric Closure)** For a relation $R$ on a nonempty set $A$,

$$
s(R) = R \cup R^{-1}.
$$

**Theorem 2.5.9 (Construction of the Transitive Closure)** For a relation $R$ on a nonempty set $A$,

$$
t(R) = R \cup R^2 \cup R^3 \cup \cdots = \bigcup_{i=1}^{\infty} R^i.
$$

**Theorem 2.5.10 (Finite Construction of the Transitive Closure)** Let $A$ be a nonempty finite set with $|A| = n$, and let $R$ be a relation on $A$. Then there is a positive integer $k \leq n$ such that

$$
t(R) = R \cup R^2 \cup \cdots \cup R^k.
$$

**Example 2.5.1** Let $A = \{a, b, c\}$ and $R = \{\langle a, b \rangle, \langle b, c \rangle, \langle c, a \rangle\}$. Then

$$
\begin{aligned}
R^2 &= \{\langle a, c \rangle, \langle b, a \rangle, \langle c, b \rangle\}, \\
R^3 &= \{\langle a, a \rangle, \langle b, b \rangle, \langle c, c \rangle\} = I_A,
\end{aligned}
$$

so $t(R) = R \cup R^2 \cup R^3 = A \times A$, with $k = 3 = n$. Moreover $R^4 = R^3 \circ R = R$, that is, $R^1 = R^4$, so the sequence of powers is periodic with period $p = 3$ (Theorem 2.5.3).

**Theorem 2.5.11 (Closures Inheriting Several Properties, I)** For a relation $R$ on a nonempty set $A$,

1. if $R$ is reflexive, then $s(R)$ and $t(R)$ are reflexive;
2. if $R$ is symmetric, then $r(R)$ and $t(R)$ are symmetric;
3. if $R$ is transitive, then $r(R)$ is transitive.

Note that $s(R)$ need not be transitive when $R$ is: $R = \{\langle a, b \rangle\}$ is transitive, but $s(R) = \{\langle a, b \rangle, \langle b, a \rangle\}$ does not contain $\langle a, a \rangle$ and so is not transitive.

**Theorem 2.5.12 (Closures Inheriting Several Properties, II)** For a relation $R$ on a nonempty set $A$,

1. $rs(R) = sr(R)$;
2. $rt(R) = t r(R)$;
3. $st(R) \subseteq ts(R)$,

where $rs(R) = r(s(R))$, and similarly for the others.

## 2.6. Equivalence Relations and Partitions

**Definition 2.6.1 (Equivalence Relation)** Let $R$ be a relation on a nonempty set $A$. If $R$ is reflexive, symmetric and transitive, then $R$ is called an **equivalence relation** on $A$.

**Definition 2.6.2 (Equivalence Class)** Let $R$ be an equivalence relation on a nonempty set $A$. For every $x \in A$, the set

$$
[x]_R = \{y \mid y \in A \land xRy\}
$$

is called the **equivalence class** of $x$ with respect to $R$, or simply the equivalence class of $x$; it may also be written $[x]$ or $\overline{x}$.

**Theorem 2.6.1 (Properties of Equivalence Classes)** Let $R$ be an equivalence relation on a nonempty set $A$. For all $x, y \in A$,

1. $[x]_R \neq \varnothing$ and $[x]_R \subseteq A$, that is, $[x]_R$ is a nonempty subset of $A$;
2. if $xRy$, then $[x]_R = [y]_R$;
3. if $\langle x, y \rangle \notin R$, then $[x]_R \cap [y]_R = \varnothing$;
4. $\bigcup \{[x]_R \mid x \in A\} = A$.

**Definition 2.6.3 (Quotient Set)** Let $R$ be an equivalence relation on a nonempty set $A$. The set whose elements are all the equivalence classes of $R$ is called the **quotient set** of $A$ by $R$, written $A/R$; that is,

$$
A/R = \{[x]_R \mid x \in A\}.
$$

**Definition 2.6.4 (Partition)** Let $A$ be a nonempty set. A **partition** of $A$ is a set $\pi$ satisfying the following conditions; the elements of $\pi$ are called the **blocks** of the partition:

1. $(\forall x)(x \in \pi \rightarrow x \subseteq A)$;
2. $\varnothing \notin \pi$;
3. $\bigcup \pi = A$;
4. $(\forall x)(\forall y)((x \in \pi \land y \in \pi \land x \neq y) \rightarrow x \cap y = \varnothing)$.

**Theorem 2.6.2 (The Partition Induced by an Equivalence Relation)** For an equivalence relation $R$ on a nonempty set $A$, the quotient set $A/R$ is a partition of $A$, called the partition of $A$ induced by $R$ and written $\pi_R$.

**Theorem 2.6.3 (The Equivalence Relation Induced by a Partition)** For a partition $\pi$ of a nonempty set $A$, let

$$
R_\pi = \{\langle x, y \rangle \mid (\exists z)(z \in \pi \land x \in z \land y \in z)\}.
$$

Then $R_\pi$ is an equivalence relation on $A$, called the equivalence relation on $A$ induced by the partition $\pi$.

**Theorem 2.6.4 (One-to-One Correspondence Between Partitions and Equivalence Relations)** For a partition $\pi$ of a nonempty set $A$ and an equivalence relation $R$ on $A$, $\pi$ induces $R$ if and only if $R$ induces $\pi$; that is, $R_\pi = R \Leftrightarrow A/R = \pi$.

**Example 2.6.1** On $A = \{1, 2, \cdots, 8\}$ define $xRy \Leftrightarrow x \equiv y \pmod 3$. Then $R$ is an equivalence relation, and the quotient set

$$
A/R = \{\{1, 4, 7\}, \{2, 5, 8\}, \{3, 6\}\}
$$

is a partition of $A$; conversely, the equivalence relation induced by this partition according to Theorem 2.6.3 is exactly $R$.

## 2.7. Compatibility Relations and Covers

**Definition 2.7.1 (Compatibility Relation)** For a relation $R$ on a nonempty set $A$, if $R$ is reflexive and symmetric, then $R$ is called a **compatibility relation** on $A$.

**Definition 2.7.2 (Compatibility Class)** Let $R$ be a compatibility relation on a nonempty set $A$. If $C \subseteq A$ and $xRy$ for any two elements $x$ and $y$ of $C$, then $C$ is called a compatibility class generated by $R$, or simply a **compatibility class**. This condition can also be written as

$$
(\forall x)(\forall y)((x \in C \land y \in C) \rightarrow xRy).
$$

**Definition 2.7.3 (Maximal Compatibility Class)** Let $R$ be a compatibility relation on a nonempty set $A$. A compatibility class that is not a proper subset of any compatibility class is called a **maximal compatibility class** and is written $C_R$. A maximal compatibility class $C_R$ has the following properties:

$$
\begin{aligned}
& (\forall x)(\forall y)((x \in C_R \land y \in C_R) \rightarrow xRy), \\
& (\forall x)(x \in A - C_R \rightarrow (\exists y)(y \in C_R \land \lnot xRy)).
\end{aligned}
$$

That is, any two elements of $C_R$ are compatible, and every element outside $C_R$ is incompatible with some element of $C_R$.

**Theorem 2.7.1 (Existence of Maximal Compatibility Classes)** Let $R$ be a compatibility relation on a nonempty finite set $A$. If $C$ is a compatibility class, then there is a maximal compatibility class $C_R$ with $C \subseteq C_R$.

**Definition 2.7.4 (Cover)** Let $A$ be a nonempty set. A **cover** of $A$ is a set $\Omega$ satisfying the following conditions; the elements of $\Omega$ are called the **blocks** of $\Omega$:

1. $(\forall x)(x \in \Omega \rightarrow x \subseteq A)$;
2. $\varnothing \notin \Omega$;
3. $\bigcup \Omega = A$.

A partition is a cover whose blocks are pairwise disjoint.

**Theorem 2.7.2 (Complete Cover)** For a compatibility relation $R$ on a nonempty set $A$, the set of all maximal compatibility classes is a cover of $A$, called the complete cover of $A$ and written $C_R(A)$; moreover, $C_R(A)$ is unique.

**Theorem 2.7.3 (The Compatibility Relation Determined by a Cover)** For a cover $\Omega = \{A_1, A_2, \cdots, A_n\}$ of a nonempty set $A$, the relation determined by $\Omega$,

$$
R = A_1 \times A_1 \cup A_2 \times A_2 \cup \cdots \cup A_n \times A_n,
$$

is a compatibility relation on $A$.

Different covers may determine the same compatibility relation. For example, on $A = \{1, 2, 3\}$ the covers $\Omega_1 = \{\{1, 2\}, \{2, 3\}\}$ and $\Omega_2 = \{\{1, 2\}, \{2, 3\}, \{2\}\}$ determine the same compatibility relation. Hence compatibility relations and covers are not in one-to-one correspondence the way equivalence relations and partitions are; what corresponds uniquely to a compatibility relation $R$ is the complete cover $C_R(A)$.

## 2.8. Partial Orders

**Definition 2.8.1 (Partial Order)** For a relation $R$ on a nonempty set $A$, if $R$ is reflexive, antisymmetric and transitive, then $R$ is called a **partial order** on $A$.

When no confusion can arise, a partial order $R$ is usually written $\leq$; we write $x \leq y$ when $xRy$, read "$x$ is less than or equal to $y$". A partial order is also called a weak partial order or simply an order.

**Definition 2.8.2 (Strict Partial Order)** For a relation $R$ on a nonempty set $A$, if $R$ is irreflexive and transitive, then $R$ is called a **strict partial order** on $A$.

When no confusion can arise, a strict partial order $R$ is usually written $<$; we write $x < y$ when $xRy$, read "$x$ is less than $y$".

**Theorem 2.8.1** If $R$ is a strict partial order on $A$, then $R$ is antisymmetric.

**Theorem 2.8.2** If $R$ is a strict partial order on $A$, then $R \cup I_A$ is a partial order on $A$.

**Theorem 2.8.3** If $R$ is a partial order on $A$, then $R - I_A$ is a strict partial order on $A$.

**Definition 2.8.3 (Partially Ordered Set)** A set $A$ together with a relation $R$ on $A$ is called a structure. A set $A$ together with a partial order $R$ on $A$ is called a partially ordered structure, or a **partially ordered set** (**poset**), written $(A, R)$.

**Definition 2.8.4 (Covering Relation)** Let $(A, \leq)$ be a poset. If $x, y \in A$, $x \leq y$, $x \neq y$, and there is no $z \in A$ with $x \leq z \leq y$, $z \neq x$ and $z \neq y$, then we say that $y$ covers $x$. The **covering relation** on $A$ is defined by

$$
\operatorname{cov} A = \{\langle x, y \rangle \mid x \in A \land y \in A \land y \text{ covers } x\}.
$$

A finite poset can be represented by a *Hasse diagram* drawn from its covering relation: each element is drawn as a point, and whenever $y$ covers $x$, the point $y$ is placed above $x$ and the two are joined by a line segment.

**Definition 2.8.5 (Least, Greatest, Minimal and Maximal Elements)** Let $(A, \leq)$ be a poset and $B \subseteq A$.

1. If $y \in B \land (\forall x)(x \in B \rightarrow y \leq x)$, then $y$ is called the **least element** of $B$;
2. if $y \in B \land (\forall x)(x \in B \rightarrow x \leq y)$, then $y$ is called the **greatest element** of $B$;
3. if $y \in B \land (\forall x)((x \in B \land x \leq y) \rightarrow x = y)$, then $y$ is called a **minimal element** of $B$;
4. if $y \in B \land (\forall x)((x \in B \land y \leq x) \rightarrow x = y)$, then $y$ is called a **maximal element** of $B$.

A least (greatest) element, if it exists, is unique and is necessarily a minimal (maximal) element; the converse fails.

**Definition 2.8.6 (Upper Bound, Lower Bound, Supremum and Infimum)** Let $(A, \leq)$ be a poset and $B \subseteq A$.

1. If $y \in A \land (\forall x)(x \in B \rightarrow x \leq y)$, then $y$ is called an **upper bound** of $B$;
2. if $y \in A \land (\forall x)(x \in B \rightarrow y \leq x)$, then $y$ is called a **lower bound** of $B$;
3. let $C = \{y \mid y \text{ is an upper bound of } B\}$; the least element of $C$ is called the **supremum**, or least upper bound, of $B$;
4. let $C = \{y \mid y \text{ is a lower bound of } B\}$; the greatest element of $C$ is called the **infimum**, or greatest lower bound, of $B$.

**Example 2.8.1** In the poset $(\mathcal{P}(\{a, b\}), \subseteq)$, take $B = \{\{a\}, \{b\}\}$. Then $B$ has neither a least nor a greatest element, and $\{a\}$ and $\{b\}$ are both minimal and maximal elements of $B$. The only upper bound of $B$ is $\{a, b\}$ and the only lower bound is $\varnothing$, so the supremum of $B$ is $\{a, b\}$ and the infimum is $\varnothing$.

**Definition 2.8.7 (Comparability)** Let $(A, \leq)$ be a poset and $x, y \in A$. If $x \leq y$ or $y \leq x$, then $x$ and $y$ are said to be **comparable**.

**Definition 2.8.8 (Total Order and Totally Ordered Set)** Let $(A, \leq)$ be a poset. If any two elements $x, y \in A$ are comparable, then $\leq$ is called a **total order** (or linear order) on $A$, and $(A, \leq)$ is called a **totally ordered set**.

**Definition 2.8.9 (Chain and Antichain)** Let $(A, \leq)$ be a poset and $B \subseteq A$.

1. If any two elements $x, y \in B$ are comparable, then $B$ is called a **chain** in $A$, and the number of elements of $B$ is called the length of the chain;
2. if any two distinct elements $x, y \in B$ are incomparable, then $B$ is called an **antichain** in $A$, and the number of elements of $B$ is called the length of the antichain.

**Theorem 2.8.4 (Decomposition Theorem for Posets)** Let $(A, \leq)$ be a finite poset in which the longest chain has length $n$. Then any partition of $A$ into disjoint antichains has at least $n$ antichains, and $A$ can be partitioned into exactly $n$ disjoint antichains.

**Theorem 2.8.5** Let $(A, \leq)$ be a poset with $mn + 1$ elements. Then $A$ contains either an antichain of length $m + 1$ or a chain of length $n + 1$.

**Proof** If $A$ has no chain of length $n + 1$, then the longest chain has length at most $n$, and by Theorem 2.8.4 $A$ can be partitioned into at most $n$ disjoint antichains. When $mn + 1$ elements are distributed among at most $n$ antichains, some antichain receives at least $m + 1$ elements. $\square$

**Definition 2.8.10 (Well-Order and Well-Ordered Set)** Let $(A, \leq)$ be a poset. If every nonempty subset of $A$ has a least element, then $\leq$ is called a **well-order** and $(A, \leq)$ is called a **well-ordered set**.

**Theorem 2.8.6** Every well-ordered set is totally ordered.

**Theorem 2.8.7** Every finite totally ordered set is well-ordered.

**Theorem 2.8.8 (Well-Ordering Theorem)** Every set can be well-ordered.

The *well-ordering theorem* is equivalent to the **axiom of choice**. $(\mathbb{N}, \leq)$ is a well-ordered set, whereas $(\mathbb{Z}, \leq)$ and $(\mathbb{R}, \leq)$ are totally ordered but not well-ordered.

**Definition 2.8.11 (Intervals)** In the totally ordered set $(\mathbb{R}, \leq)$, for $a, b \in \mathbb{R}$ with $a < b$,

1. $[a, b] = \{x \mid x \in \mathbb{R} \land a \leq x \leq b\}$ is called the **closed interval** from $a$ to $b$;
2. $(a, b) = \{x \mid x \in \mathbb{R} \land a < x < b\}$ is called the **open interval** from $a$ to $b$;
3. $[a, b) = \{x \mid x \in \mathbb{R} \land a \leq x < b\}$ and $(a, b] = \{x \mid x \in \mathbb{R} \land a < x \leq b\}$ are both called **half-open intervals** from $a$ to $b$;
4. infinite intervals can also be defined: $(-\infty, a] = \{x \mid x \in \mathbb{R} \land x \leq a\}$, $(-\infty, a) = \{x \mid x \in \mathbb{R} \land x < a\}$, $[a, +\infty) = \{x \mid x \in \mathbb{R} \land a \leq x\}$, $(a, +\infty) = \{x \mid x \in \mathbb{R} \land a < x\}$, $(-\infty, +\infty) = \mathbb{R}$.
