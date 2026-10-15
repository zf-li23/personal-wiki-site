---
title: Sets
source_hash: c94c3904abd1
---

This chapter introduces the basic language of set theory: how sets are described, the relations between sets, the operations on sets and the laws they obey, and the cardinality of finite sets; it closes with a brief introduction to the ZF axioms of set theory. The relations, functions and cardinal numbers of the later chapters are all built on these notions: ordered pairs and Cartesian products give the definition of a relation, and the cardinality of finite sets is extended to arbitrary sets in Chapter 4.

## 1.1. The Notion of a Set and Its Notation

A *set* is the most basic mathematical notion and admits no rigorous definition; it is usually described as follows: a set is a collection, regarded as a single whole, of definite and distinguishable objects, and each object that makes up a set is called an *element* (or member) of the set. Cantor's original formulation reads, in P. E. B. Jourdain's 1915 translation:

> By an "aggregate" (Menge) we are to understand any collection into a whole M of definite and separate objects m of our intuition or our thought. These objects are called the "elements" of M.

Between an element and a set there is the relation of membership: an object either belongs to the set or does not. If $a$ belongs to the set $A$, we write $a \in A$; otherwise we write $a \notin A$. In the axiomatic system adopted in this course, the elements of sets are themselves sets, and $A \notin A$ for every set $A$ (see Theorem 1.7.6).

There are two ways to describe a set. *Roster notation* (also called listing notation) lists all elements of the set, as in $\{1, 2, 3\}$. *Set-builder notation* (also called predicate notation) uses a **predicate** to characterize the elements of the set. In general, if $P(x)$ is a predicate, then $\{x \mid P(x)\}$ or $\{x : P(x)\}$ denotes the set of all $x$ for which $P(x)$ is true; that is, $a$ belongs to this set if and only if $P(a)$ is true.

## 1.2. Relations Between Sets and Special Sets

**Definition 1.2.1 (Equality of Sets)** Two sets $A$ and $B$ are equal if and only if they have the same elements. If $A$ and $B$ are equal, we write $A = B$; otherwise we write $A \neq B$. In symbols,

$$
\begin{aligned}
A = B &\Leftrightarrow (\forall x)(x \in A \leftrightarrow x \in B), \\
A \neq B &\Leftrightarrow (\exists x)\lnot(x \in A \leftrightarrow x \in B).
\end{aligned}
$$

**Definition 1.2.2 (Subset)** Let $A$ and $B$ be sets. If every element of $A$ is an element of $B$, then $A$ is called a **subset** of $B$, and we also say that $B$ includes $A$, written $A \subseteq B$. In symbols,

$$
A \subseteq B \Leftrightarrow (\forall x)(x \in A \to x \in B).
$$

**Theorem 1.2.1** Two sets are equal if and only if each is a subset of the other:

$$
A = B \Leftrightarrow (A \subseteq B \land B \subseteq A).
$$

**Theorem 1.2.2** For all sets $A$, $B$ and $C$, inclusion has the following properties:

1. $A \subseteq A$ (reflexivity);
2. $(A \subseteq B \land B \subseteq A) \Rightarrow A = B$ (antisymmetry);
3. $(A \subseteq B \land B \subseteq C) \Rightarrow A \subseteq C$ (transitivity).

**Definition 1.2.3 (Proper Subset)** For any two sets $A$ and $B$, if $A \subseteq B$ and $A \neq B$, then $A$ is called a **proper subset** of $B$, and we say that $B$ properly includes $A$, written $A \subset B$. In symbols,

$$
A \subset B \Leftrightarrow (A \subseteq B \land A \neq B).
$$

**Definition 1.2.4 (Disjoint Sets)** Two sets $A$ and $B$ are **disjoint** if they have no element in common. In symbols,

$$
A \text{ and } B \text{ are disjoint} \Leftrightarrow \lnot(\exists x)(x \in A \land x \in B).
$$

**Definition 1.2.5 (Empty Set)** The set that has no elements is called the **empty set** and is denoted by $\varnothing$. In symbols,

$$
\varnothing = \{x \mid x \neq x\}.
$$

**Theorem 1.2.3** The empty set is a subset of every set: $\varnothing \subseteq A$ for every set $A$.

**Definition 1.2.6 (Universal Set)** In a given problem, the set of all objects under consideration is called the **universal set** and is denoted by $E$. Equivalently, if all sets occurring in a particular problem are subsets of some set, that set is called the universal set. Formally,

$$
E = \{x \mid x = x\}.
$$

The universal set is relative: different problems have different universal sets, and even a single problem may be studied with different universal sets. The formula above is only a formal expression; by Theorem 1.7.5 there is no set having all sets as elements, so a universal set is always fixed relative to a specific problem.

## 1.3. Operations on Sets

**Definition 1.3.1 (Basic Set Operations)** For sets $A$ and $B$, the basic set operations are union, intersection, difference (relative complement), absolute complement and symmetric difference, defined as follows:

1. **Union**: $A \cup B = \{x \mid x \in A \lor x \in B\}$;
2. **Intersection**: $A \cap B = \{x \mid x \in A \land x \in B\}$;
3. **Set difference**: $A - B = \{x \mid x \in A \land x \notin B\}$, also called the relative complement of $B$ in $A$;
4. **Complement**: $A^{\mathsf c} = E - A = \{x \mid x \in E \land x \notin A\}$, where $E$ is the universal set; the complement of $A$ is also called the absolute complement of $A$, that is, the relative complement of $A$ in $E$;
5. **Symmetric difference**: $A \oplus B = (A - B) \cup (B - A) = \{x \mid (x \in A \land x \notin B) \lor (x \notin A \land x \in B)\}$.

**Definition 1.3.2 (Generalized Union and Generalized Intersection)** Let $A$ be a set. The set of all elements of elements of $A$ is called the **generalized union** of $A$, written $\bigcup A$. Let $A$ be a nonempty set. The set of all objects that belong to every element of $A$ is called the **generalized intersection** of $A$, written $\bigcap A$. In symbols,

$$
\begin{aligned}
\bigcup A &= \{x \mid (\exists z)(z \in A \land x \in z)\}, \\
\bigcap A &= \{x \mid (\forall z)(z \in A \to x \in z)\}.
\end{aligned}
$$

The generalized union of the empty set also makes sense: $\bigcup \varnothing = \varnothing$. But $\bigcap \varnothing$ is not a set (by the formula above it would contain every set), so it is left undefined.

**Definition 1.3.3 (Power Set)** Let $A$ be a set. The set of all subsets of $A$ is called the **power set** of $A$, written $\mathcal{P}(A)$. In symbols,

$$
\mathcal{P}(A) = \{x \mid x \subseteq A\}.
$$

For every set $A$ we have $\varnothing \subseteq A$ and $A \subseteq A$, hence $\varnothing \in \mathcal{P}(A)$ and $A \in \mathcal{P}(A)$.

A pair formed by two objects $x$ and $y$ (possibly $x = y$) arranged in a given order is called an *ordered pair* and is written $\langle x, y \rangle$; $x$ is its first coordinate and $y$ its second coordinate. Ordered pairs have the following properties:

1. if $x \neq y$, then $\langle x, y \rangle \neq \langle y, x \rangle$;
2. $\langle x, y \rangle = \langle u, v \rangle$ if and only if $x = u$ and $y = v$.

**Definition 1.3.4 (Ordered Pair)** In terms of sets, the ordered pair $\langle x, y \rangle$ is defined by

$$
\langle x, y \rangle = \{\{x\}, \{x, y\}\}.
$$

**Definition 1.3.5 ($n$-Tuple)** Let $n \in \mathbb{N}$ with $n > 1$, and let $x_1, x_2, \cdots, x_n$ be $n$ objects. The **$n$-tuple** $\langle x_1, x_2, \cdots, x_n \rangle$ is defined as follows: for $n = 2$, it is the ordered pair $\langle x_1, x_2 \rangle$; for $n > 2$,

$$
\langle x_1, x_2, \cdots, x_n \rangle = \langle \langle x_1, x_2, \cdots, x_{n-1} \rangle, x_n \rangle.
$$

**Definition 1.3.6 (Cartesian Product)** Let $A$ and $B$ be sets. The set of all ordered pairs whose first coordinate lies in $A$ and whose second coordinate lies in $B$ is called the **Cartesian product** of $A$ and $B$, written $A \times B$. In symbols,

$$
A \times B = \{\langle x, y \rangle \mid x \in A \land y \in B\}.
$$

**Definition 1.3.7 ($n$-Fold Cartesian Product)** Let $n \in \mathbb{N}$ with $n > 1$, and let $A_1, A_2, \cdots, A_n$ be $n$ sets. Their **$n$-fold Cartesian product**, written $A_1 \times A_2 \times \cdots \times A_n$, is defined by

$$
A_1 \times A_2 \times \cdots \times A_n = \{\langle x_1, x_2, \cdots, x_n \rangle \mid x_1 \in A_1 \land x_2 \in A_2 \land \cdots \land x_n \in A_n\}.
$$

The precedence of set operations is fixed as follows:

- Generalized union, generalized intersection, power set and absolute complement ($\bigcup A, \bigcap A, \mathcal{P}(A), A^{\mathsf c}$) are operations of the first kind; union, intersection, symmetric difference, Cartesian product and relative complement ($\cup, \cap, \oplus, \times, -$) are operations of the second kind.
- Operations of the first kind take precedence over those of the second kind; operations of the second kind take precedence over set relations ($=, \subseteq, \subset, \in$); and all of these take precedence over the logical connectives ($\lnot, \land, \lor, \to, \leftrightarrow, \Rightarrow$).
- Expressions inside parentheses are evaluated first. Within the same pair of parentheses, operations of equal precedence are evaluated from right to left for operations of the first kind and from left to right otherwise.

## 1.4. Diagrams of Sets

The *Venn diagram* is named after the English logician J. Venn (1834–1923), who in his *Symbolic Logic* (1881) used overlapping regions to illustrate the relations between classes; the method of depicting relations between sets and set operations by such figures now bears his name. A large rectangle represents the universal set (it is sometimes omitted for simplicity); inside it, circles (or other closed curves) are drawn, the points inside a circle represent the elements of the corresponding set, different circles represent different sets, and shaded regions represent the sets produced by operations. Venn diagrams are vivid and easy to understand, but they lack a rigorous theoretical basis, so they may be used for illustration but not for proofs.

## 1.5. Properties of Set Operations and Their Proofs

**Theorem 1.5.1 (Set Identities)** For all sets $A$, $B$ and $C$, the following identities hold:

1. Commutative laws: $A \cup B = B \cup A$, $A \cap B = B \cap A$.
2. Associative laws: $(A \cup B) \cup C = A \cup (B \cup C)$, $(A \cap B) \cap C = A \cap (B \cap C)$.
3. Distributive laws: $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$, $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$.
4. Idempotent laws: $A \cup A = A$, $A \cap A = A$.
5. Absorption laws: $A \cup (A \cap B) = A$, $A \cap (A \cup B) = A$.
6. **De Morgan's laws**:
   $$
   \begin{aligned}
   A - (B \cup C) &= (A - B) \cap (A - C), & A - (B \cap C) &= (A - B) \cup (A - C), \\
   (B \cup C)^{\mathsf c} &= B^{\mathsf c} \cap C^{\mathsf c}, & (B \cap C)^{\mathsf c} &= B^{\mathsf c} \cup C^{\mathsf c}.
   \end{aligned}
   $$
7. Identity laws: $A \cup \varnothing = A$, $A \cap E = A$.
8. Domination laws: $A \cup E = E$, $A \cap \varnothing = \varnothing$.
9. Complement laws: $A \cup A^{\mathsf c} = E$ (excluded middle), $A \cap A^{\mathsf c} = \varnothing$ (contradiction).
10. Complements of $\varnothing$ and $E$: $\varnothing^{\mathsf c} = E$, $E^{\mathsf c} = \varnothing$.
11. Double complement law: $(A^{\mathsf c})^{\mathsf c} = A$.

**Theorem 1.5.2 (Properties of Set Difference)** For all sets $A$, $B$ and $C$,

$$
\begin{aligned}
A - B &= A - (A \cap B), \\
A - B &= A \cap B^{\mathsf c}, \\
A \cup (B - A) &= A \cup B, \\
A \cap (B - C) &= (A \cap B) - C.
\end{aligned}
$$

**Theorem 1.5.3 (Properties of Symmetric Difference)** For all sets $A$, $B$ and $C$,

1. commutative law: $A \oplus B = B \oplus A$;
2. associative law: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
3. distributive law: $A \cap (B \oplus C) = (A \cap B) \oplus (A \cap C)$;
4. identity law: $A \oplus \varnothing = A$;
5. inverse law: $A \oplus A = \varnothing$;
6. cancellation law: $A \oplus (A \oplus B) = B$.

**Theorem 1.5.4 (Properties of Inclusion)** For all sets $A$, $B$, $C$ and $D$,

$$
\begin{aligned}
A \subseteq B &\Rightarrow A \cup C \subseteq B \cup C, \\
A \subseteq B &\Rightarrow A \cap C \subseteq B \cap C, \\
(A \subseteq B) \land (C \subseteq D) &\Rightarrow A \cup C \subseteq B \cup D, \\
(A \subseteq B) \land (C \subseteq D) &\Rightarrow A \cap C \subseteq B \cap D, \\
(A \subseteq B) \land (C \subseteq D) &\Rightarrow A - D \subseteq B - C, \\
C \subseteq D &\Rightarrow A - D \subseteq A - C.
\end{aligned}
$$

**Theorem 1.5.5 (Properties of Power Sets, I)** For all sets $A$ and $B$,

$$
\begin{aligned}
A \subseteq B &\Leftrightarrow \mathcal{P}(A) \subseteq \mathcal{P}(B), \\
A = B &\Leftrightarrow \mathcal{P}(A) = \mathcal{P}(B).
\end{aligned}
$$

**Theorem 1.5.6 (Properties of Power Sets, II)** For all sets $A$ and $B$,

$$
\mathcal{P}(A) \in \mathcal{P}(B) \Rightarrow A \in B.
$$

**Theorem 1.5.7 (Properties of Power Sets, III)** For all sets $A$ and $B$,

$$
\begin{aligned}
\mathcal{P}(A) \cap \mathcal{P}(B) &= \mathcal{P}(A \cap B), \\
\mathcal{P}(A) \cup \mathcal{P}(B) &\subseteq \mathcal{P}(A \cup B).
\end{aligned}
$$

**Theorem 1.5.8 (Properties of Power Sets, IV)** For all sets $A$ and $B$,

$$
\mathcal{P}(A - B) \subseteq (\mathcal{P}(A) - \mathcal{P}(B)) \cup \{\varnothing\}.
$$

**Definition 1.5.1 (Transitive Set)** A set $A$ is called a **transitive set** if every element of an element of $A$ is an element of $A$. In symbols,

$$
A \text{ is a transitive set} \Leftrightarrow (\forall x)(\forall y)((x \in y \land y \in A) \to x \in A).
$$

**Theorem 1.5.9 (Properties of Transitive Sets, I)** For every set $A$, $A$ is a transitive set $\Leftrightarrow A \subseteq \mathcal{P}(A)$.

**Theorem 1.5.10 (Properties of Transitive Sets, II)** For every set $A$, $A$ is a transitive set $\Leftrightarrow \mathcal{P}(A)$ is a transitive set.

**Theorem 1.5.11 (Properties of Generalized Unions and Intersections, I)** For families of sets $A$ and $B$,

$$
\begin{aligned}
A \subseteq B &\Rightarrow \textstyle\bigcup A \subseteq \bigcup B, \\
A \subseteq B &\Rightarrow \textstyle\bigcap B \subseteq \bigcap A \quad (A \neq \varnothing).
\end{aligned}
$$

**Theorem 1.5.12 (Properties of Generalized Unions and Intersections, II)** For families of sets $A$ and $B$,

$$
\begin{aligned}
\textstyle\bigcup (A \cup B) &= \left(\textstyle\bigcup A\right) \cup \left(\textstyle\bigcup B\right), \\
\textstyle\bigcap (A \cup B) &= \left(\textstyle\bigcap A\right) \cap \left(\textstyle\bigcap B\right) \quad (A \neq \varnothing,\ B \neq \varnothing).
\end{aligned}
$$

**Theorem 1.5.13 (Generalized Union of a Power Set)** For every set $A$,

$$
\textstyle\bigcup \mathcal{P}(A) = A.
$$

**Theorem 1.5.14 (Properties of Transitive Sets, III)** If $A$ is a transitive set, then $\bigcup A$ is a transitive set.

**Theorem 1.5.15 (Properties of Transitive Sets, IV)** If every element of a set $A$ is a transitive set, then $\bigcup A$ is a transitive set.

**Theorem 1.5.16 (Properties of Transitive Sets, V)** If $A$ is a nonempty transitive set, then $\bigcap A = \varnothing$; in particular, $\bigcap A$ is a transitive set.

The equality $\bigcap A = \varnothing$ relies on the axiom of regularity: by Theorem 1.7.8 a nonempty transitive set $A$ contains $\varnothing$, so $\bigcap A \subseteq \varnothing$.

**Theorem 1.5.17 (Properties of Transitive Sets, VI)** If $A$ is a nonempty set every element of which is a transitive set, then $\bigcap A$ is a transitive set.

**Theorem 1.5.18 (Ordered Pairs and Power Sets)** If $A$ is a set, $x \in A$ and $y \in A$, then $\langle x, y \rangle \in \mathcal{P}(\mathcal{P}(A))$.

**Theorem 1.5.19 (Distributivity of the Cartesian Product over Union and Intersection)** For all sets $A$, $B$ and $C$,

$$
\begin{aligned}
A \times (B \cup C) &= (A \times B) \cup (A \times C), \\
A \times (B \cap C) &= (A \times B) \cap (A \times C), \\
(B \cup C) \times A &= (B \times A) \cup (C \times A), \\
(B \cap C) \times A &= (B \times A) \cap (C \times A).
\end{aligned}
$$

**Theorem 1.5.20 (Cartesian Products and Inclusion, I)** For all sets $A$, $B$ and $C$ with $C \neq \varnothing$,

$$
A \subseteq B \Leftrightarrow A \times C \subseteq B \times C \Leftrightarrow C \times A \subseteq C \times B.
$$

**Theorem 1.5.21 (Cartesian Products and Inclusion, II)** For all nonempty sets $A$, $B$ and all sets $C$, $D$,

$$
A \times B \subseteq C \times D \Leftrightarrow (A \subseteq C \land B \subseteq D).
$$

The nonemptiness hypothesis cannot be dropped: if $A = \varnothing$, then $A \times B = \varnothing \subseteq C \times D$ always holds, whereas $B \subseteq D$ need not.

## 1.6. Cardinality of Finite Sets

**Definition 1.6.1 (Cardinality of a Finite Set)** If there is an $n \in \mathbb{N}$ such that there is a bijection between the set $A$ and the set $\{x \mid x \in \mathbb{N} \land x < n\} = \{0, 1, \cdots, n - 1\}$ (that is, the two sets are equinumerous; see Definition 4.2.1), we say that the cardinality of $A$ is $n$ and write $|A| = n$ or $\operatorname{card}(A) = n$. The cardinality of the empty set $\varnothing$ is $0$.

**Definition 1.6.2 (Finite Set)** If there is an $n \in \mathbb{N}$ such that $n$ is the cardinality of the set $A$, then $A$ is called a **finite set**; if there is no such $n$, then $A$ is called an **infinite set**.

**Theorem 1.6.1 (Cardinality of a Power Set)** For every finite set $A$,

$$
|\mathcal{P}(A)| = 2^{|A|}.
$$

**Theorem 1.6.2 (Cardinality of a Cartesian Product)** For finite sets $A$ and $B$,

$$
|A \times B| = |A| \cdot |B|.
$$

**Theorem 1.6.3 (Cardinality and the Basic Operations)** For finite sets $A$ and $B$,

$$
\begin{aligned}
|A \cup B| &\leq |A| + |B|, \\
|A \cap B| &\leq \min(|A|, |B|), \\
|A - B| &\geq |A| - |B|, \\
|A \oplus B| &= |A| + |B| - 2|A \cap B|.
\end{aligned}
$$

**Theorem 1.6.4 (Inclusion–Exclusion Principle)** For finite sets $A$ and $B$,

$$
|A \cup B| = |A| + |B| - |A \cap B|.
$$

The *inclusion–exclusion principle* extends to $n$ sets: if $n \in \mathbb{N}$, $n > 1$, and $A_1, A_2, \cdots, A_n$ are finite sets, then

$$
\begin{aligned}
|A_1 \cup A_2 \cup \cdots \cup A_n| ={} & \sum_{1 \leq i \leq n} |A_i| - \sum_{1 \leq i < j \leq n} |A_i \cap A_j| + \sum_{1 \leq i < j < k \leq n} |A_i \cap A_j \cap A_k| \\
& - \cdots + (-1)^{n-1} |A_1 \cap A_2 \cap \cdots \cap A_n|.
\end{aligned}
$$

**Example 1.6.1** How many integers from $1$ to $100$ are divisible by $2$, $3$ or $5$? Let $A_d$ be the set of those integers divisible by $d$. Then

$$
\begin{aligned}
|A_2 \cup A_3 \cup A_5| &= (50 + 33 + 20) - (16 + 10 + 6) + 3 \\
&= 103 - 32 + 3 = 74.
\end{aligned}
$$

## 1.7. Axiomatic Set Theory

An axiomatic set theory extends the **axiomatic system** of **first-order logic**: it consists of the axioms of first-order logic together with a number of set-theoretic axioms. From it one can derive all theorems of first-order logic as well as the concepts and theorems of set theory, and in principle it rules out the set-theoretic paradoxes. A basic idea of axiomatic set theory is that "every element of a set is a set": the only objects of study are sets, and all other objects (ordered pairs, numbers, letters and so on) must be defined as sets.

*Zermelo–Fraenkel set theory* (ZF), proposed by the German mathematicians E. Zermelo and A. Fraenkel, is the best-known axiomatic set theory. We list ten axioms below (the first nine form ZF; adding the axiom of choice gives ZFC). They are not independent of one another; for instance, the axiom of pairing and the axiom schema of separation can be derived from the others.

1. *Axiom of extensionality*: two sets are equal if and only if they have exactly the same elements.
   $$
   (\forall x)(\forall y)((\forall z)(z \in x \leftrightarrow z \in y) \to x = y)
   $$
2. *Empty set axiom*: there is a set with no elements (the empty set $\varnothing$).
   $$
   (\exists x)(\forall y)(y \notin x)
   $$
3. *Axiom of pairing*: for any sets $x$ and $y$, there is a set $z$ whose elements are exactly $x$ and $y$.
   $$
   (\forall x)(\forall y)(\exists z)(\forall u)(u \in z \leftrightarrow (u = x \lor u = y))
   $$
4. *Axiom of union*: for any set $x$, there is a set $y$ whose elements are exactly the elements of the elements of $x$.
   $$
   (\forall x)(\exists y)(\forall z)(z \in y \leftrightarrow (\exists u)(z \in u \land u \in x))
   $$
5. *Axiom schema of separation* (also called the subset axiom schema): for any formula $P(z)$ and any set $x$, there is a set $y$ whose elements are exactly those elements of $x$ for which $P(z)$ is true.
   $$
   (\forall x)(\exists y)(\forall z)(z \in y \leftrightarrow (z \in x \land P(z)))
   $$
6. *Axiom of power set*: for any set $x$, there is a set $y$ whose elements are exactly the subsets of $x$.
   $$
   (\forall x)(\exists y)(\forall z)(z \in y \leftrightarrow (\forall u)(u \in z \to u \in x))
   $$
7. *Axiom of regularity*: every nonempty set $x$ has an element that is disjoint from $x$.
   $$
   (\forall x)(x \neq \varnothing \to (\exists y)(y \in x \land x \cap y = \varnothing))
   $$
8. *Axiom of infinity*: there is a set that contains $\varnothing$ and, together with each of its elements $y$, also contains $y \cup \{y\}$; such a set therefore contains all natural numbers (see Definition 1.7.4).
   $$
   (\exists x)(\varnothing \in x \land (\forall y)(y \in x \to y \cup \{y\} \in x))
   $$
9. *Axiom schema of replacement*: for any formula $P(x, y)$, if for every $x$ there is a unique $y$ such that $P(x, y)$ is true, then for every set $t$ there is a set $s$ whose elements are exactly the $y$ corresponding to the elements $x$ of $t$.
   $$
   (\forall x)(\exists ! y)P(x, y) \to (\forall t)(\exists s)(\forall u)(u \in s \leftrightarrow (\exists z)(z \in t \land P(z, u)))
   $$
   Here $(\exists ! y)$ means "there exists a unique $y$".
10. *Axiom of choice*: for every relation $R$, there is a function $F$ such that $F$ is a subset of $R$ and $F$ has the same domain as $R$.
    $$
    (\forall \text{relation } R)(\exists \text{function } F)(F \subseteq R \land \operatorname{dom}(F) = \operatorname{dom}(R))
    $$

**Theorem 1.7.1 (Existence of Intersections)** For all sets $A$ and $B$, the intersection $A \cap B$ is a set.

**Theorem 1.7.2 (Existence of Differences)** For all sets $A$ and $B$, the difference $A - B$ is a set.

**Theorem 1.7.3 (Existence of Generalized Intersections)** For every nonempty set $A$, the generalized intersection $\bigcap A$ is a set.

**Theorem 1.7.4 (Existence of Cartesian Products)** For all sets $A$ and $B$, the Cartesian product $A \times B$ is a set.

**Theorem 1.7.5 (Nonexistence of a Universal Set)** There is no set $A$ such that every set is an element of $A$.

**Definition 1.7.1 ($\in$-Minimal Element)** For sets $A$ and $B$, if $A \in B$ and $A \cap B = \varnothing$, then $A$ is called an **$\in$-minimal element** of $B$. The axiom of regularity asserts precisely that every nonempty set has an $\in$-minimal element.

**Theorem 1.7.6 (Basic Properties of Sets, I)** For every set $A$, $A \notin A$.

**Theorem 1.7.7 (Basic Properties of Sets, II)** For all sets $A$ and $B$, $\lnot(A \in B \land B \in A)$.

**Theorem 1.7.8 (Properties of Transitive Sets, VII)** Every nonempty transitive set $A$ satisfies $\varnothing \in A$.

**Definition 1.7.2 (Ill-Founded Set)** If a set $A$ contains a sequence of sets $A_0, A_1, \cdots, A_n, \cdots$ (each $A_n \in A$) such that

$$
\cdots \in A_{n+1} \in A_n \in A_{n-1} \in \cdots \in A_2 \in A_1 \in A_0,
$$

then $A$ is called an ill-founded set.

**Theorem 1.7.9 (Properties of Ill-Founded Sets, I)** The existence of an ill-founded set contradicts the axiom of regularity: if $A$ is ill-founded, the nonempty set $\{A_0, A_1, \cdots\}$ has no $\in$-minimal element. Hence there are no ill-founded sets in ZF.

**Theorem 1.7.10 (Properties of Ill-Founded Sets, II)** If a nonempty set $A$ is not ill-founded, then $A$ satisfies the conclusion of the axiom of regularity, that is, $A$ has an $\in$-minimal element.

**Definition 1.7.3 (Predecessor and Successor)** For every set $A$, define $A^+ = A \cup \{A\}$; $A^+$ is called the **successor** of $A$, and $A$ is called the **predecessor** of $A^+$.

**Definition 1.7.4 (Natural Numbers via Successors)** The set $0 = \varnothing$ is a **natural number**; if the set $n$ is a natural number, then the set $n + 1 = n^+$ is also a natural number; and the natural numbers are exactly the sets obtained in this way. Thus $1 = \{0\}$, $2 = \{0, 1\}$, and in general $n = \{0, 1, \cdots, n - 1\}$.

**Definition 1.7.5 (Order of the Natural Numbers)** For all natural numbers $m$ and $n$,

$$
\begin{aligned}
m < n &\Leftrightarrow m \in n \Leftrightarrow n > m, \\
m \leq n &\Leftrightarrow m \subseteq n \Leftrightarrow n \geq m.
\end{aligned}
$$

Since $n = \{0, 1, \cdots, n - 1\}$, for natural numbers we have $m \subseteq n \Leftrightarrow (m \in n \lor m = n)$, so the two definitions are consistent.

**Definition 1.7.6 (Trichotomy of a Set)** A set $A$ has the property of **trichotomy** if for all $A_1 \in A$ and $A_2 \in A$ exactly one of the following holds:

$$
A_1 \in A_2, \quad A_1 = A_2, \quad A_2 \in A_1.
$$

**Theorem 1.7.11 (Trichotomy of the Natural Numbers)** The set $\mathbb{N}$ has the property of trichotomy, and so does every natural number; that is,

$$
(\forall m)(\forall n)(m \in \mathbb{N} \land n \in \mathbb{N} \to m < n \lor m = n \lor m > n).
$$
