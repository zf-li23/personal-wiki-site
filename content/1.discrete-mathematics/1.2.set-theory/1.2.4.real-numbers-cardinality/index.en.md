---
title: The Real Numbers and Cardinality
source_hash: 7b4f50d471f2
---

This chapter first constructs the integers, the rational numbers and the real numbers in turn within set theory, and then uses **bijections** to compare the sizes of arbitrary sets: it introduces equinumerosity, finite and infinite sets, cardinal numbers with their arithmetic and comparison, and finally discusses countable sets and the continuum hypothesis. The cardinality of finite sets from Chapter 1 (Definition 1.6.1) is extended here to arbitrary sets.

## 4.1. The Set of Real Numbers

**Definition 4.1.1 (Integers)** For the set $\mathbb{N}$ of natural numbers, let

$$
\begin{aligned}
\mathbb{Z}_+ &= \mathbb{N} - \{0\}, \\
\mathbb{Z}_- &= \{\langle 0, n \rangle \mid n \in \mathbb{Z}_+\}, \\
\mathbb{Z} &= \mathbb{Z}_- \cup \{0\} \cup \mathbb{Z}_+.
\end{aligned}
$$

The elements of $\mathbb{Z}_+$ are called positive integers, the elements of $\mathbb{Z}_-$ negative integers, and the elements of $\mathbb{Z}$ **integers**.

**Definition 4.1.2 (Negatives)** The negative of an integer is defined by

$$
\begin{aligned}
-n &= \langle 0, n \rangle, \quad n \in \mathbb{Z}_+, \\
-0 &= 0, \\
-\langle 0, n \rangle &= n, \quad n \in \mathbb{Z}_+.
\end{aligned}
$$

**Definition 4.1.3 (Order of the Integers)** Define the relation $\leq$ (less than or equal to) on $\mathbb{Z}$ as follows: for all $x, y \in \mathbb{Z}$, $x \leq y$ if and only if

$$
(x \in \mathbb{N} \land y \in \mathbb{N} \land x \leq y) \lor (x \in \mathbb{Z}_- \land y \in \mathbb{N}) \lor (x \in \mathbb{Z}_- \land y \in \mathbb{Z}_- \land -y \leq -x),
$$

where $\leq$ for $x, y \in \mathbb{N}$ is the order of the natural numbers (Definition 1.7.5). Define the relation $<$ (less than) on $\mathbb{Z}$ by setting, for all $x, y \in \mathbb{Z}$,

$$
x < y \Leftrightarrow (x \leq y \land x \neq y).
$$

**Definition 4.1.4 (The Relation $\approx$ on $Q_1$)** For the set $\mathbb{Z}$ of integers, let

$$
Q_1 = \mathbb{Z} \times (\mathbb{Z} - \{0\}) = \{\langle a, b \rangle \mid a \in \mathbb{Z} \land b \in \mathbb{Z} \land b \neq 0\};
$$

$Q_1$ is called the set of fractions over $\mathbb{Z}$. For $\langle a, b \rangle \in Q_1$ we may write $a/b$ in place of $\langle a, b \rangle$. Define the relation $\approx$ on $Q_1$ by setting, for all $a/b \in Q_1$ and $c/d \in Q_1$,

$$
a/b \approx c/d \Leftrightarrow a \cdot d = b \cdot c,
$$

where $\cdot$ is multiplication on $\mathbb{Z}$ and $=$ is equality on $\mathbb{Z}$.

**Theorem 4.1.1** The relation $\approx$ on $Q_1$ is an **equivalence relation**.

**Definition 4.1.5 (Rational Numbers)** Let $\mathbb{Q} = Q_1/{\approx}$, the quotient set of $Q_1$ by the equivalence relation $\approx$. The elements of $\mathbb{Q}$ are called **rational numbers**. An element $[\langle a, b \rangle]_{\approx}$ of $\mathbb{Q}$ is usually written $a/b$, customarily with $a$ and $b$ coprime integers and $b > 0$.

**Definition 4.1.6 (Order of the Rational Numbers)** Define the relation $\leq$ on $\mathbb{Q}$ by setting, for all $a/b, c/d \in \mathbb{Q}$ (with $b > 0$ and $d > 0$),

$$
a/b \leq c/d \Leftrightarrow a \cdot d \leq b \cdot c.
$$

Positive denominators are essential: $1/2 \leq 1/1$, but if these are written as $1/2$ and $(-1)/(-1)$, then $1 \cdot (-1) \leq 2 \cdot (-1)$ fails.

**Definition 4.1.7 (Basic Function)** If $f\colon \mathbb{N} \to \mathbb{Q}$ satisfies the conditions

1. $(\exists x)(x \in \mathbb{Q} \land (\forall n)(n \in \mathbb{N} \to f(n) \leq x))$;
2. $(\exists n)(n \in \mathbb{N} \land (\forall m)(\forall i)((m \in \mathbb{N} \land i \in \mathbb{N} \land n \leq m \leq i) \to f(m) \leq f(i)))$,

that is, $f$ is bounded above and nondecreasing from some term on, then $f$ is called a basic function, or a bounded nondecreasing function. When $f$ is a basic function, the sequence of its values

$$
f(0), f(1), f(2), \cdots, f(n), \cdots
$$

is called a basic sequence, sometimes written $r_0, r_1, r_2, \cdots, r_n, \cdots$. In what follows, $B$ denotes the set of all basic functions, and $BF(f)$ means that $f$ is a basic function.

**Theorem 4.1.2** If $f\colon \mathbb{N} \to \mathbb{Q}$ is constant, then $f$ is a basic function. That is, for every $r \in \mathbb{Q}$, the sequence $r, r, r, \cdots$ is a basic sequence.

**Theorem 4.1.3** There are basic functions that are not constant.

**Definition 4.1.8 (Equivalence of Basic Functions)** On the set $B$ of basic functions, define the relation $\sim$ as follows: for all $f, g \in B$, $f \sim g$ if and only if

$$
(\forall \varepsilon)((\varepsilon \in \mathbb{Q} \land \varepsilon > 0) \to (\exists n)(n \in \mathbb{N} \land (\forall m)((m \in \mathbb{N} \land n \leq m) \to |f(m) - g(m)| < \varepsilon))).
$$

Intuitively, $f \sim g$ means that the sequences given by $f$ and $g$ have the same limit.

**Theorem 4.1.4** The relation $\sim$ on $B$ is an equivalence relation.

**Theorem 4.1.5** If $f\colon \mathbb{N} \to \mathbb{Q}$ and $g\colon \mathbb{N} \to \mathbb{Q}$ are both constant and $f \sim g$, then $f = g$.

**Definition 4.1.9 (Real Numbers)** Let $\mathbb{R} = B/{\sim}$, the quotient set of $B$ by the equivalence relation $\sim$. The elements of $\mathbb{R}$ are called **real numbers**, and $\mathbb{R}$ is called the set of real numbers.

By Theorem 4.1.5, the constant sequences of distinct rational numbers $r$ lie in distinct **equivalence classes**, so the rational numbers may be regarded as particular real numbers.

**Definition 4.1.10 (Order of Basic Functions)** Define the relation $<_B$ on $B$ as follows: for all $f, g \in B$, $f <_B g$ if and only if

$$
(\exists \varepsilon)(\varepsilon \in \mathbb{Q} \land \varepsilon > 0 \land (\exists n)(n \in \mathbb{N} \land (\forall m)((m \in \mathbb{N} \land n \leq m) \to g(m) - f(m) > \varepsilon))).
$$

Further, define $f \leq_B g$ if and only if $f <_B g$ or $f \sim g$.

**Definition 4.1.11 (Order of the Real Numbers)** Define the relations $\leq_{\mathbb{R}}$ (less than or equal to) and $<_{\mathbb{R}}$ (less than) on $\mathbb{R}$ by setting, for all $f, g \in B$,

$$
\begin{aligned}
[f]_\sim \leq_{\mathbb{R}} [g]_\sim &\Leftrightarrow f \leq_B g, \\
[f]_\sim <_{\mathbb{R}} [g]_\sim &\Leftrightarrow f <_B g.
\end{aligned}
$$

## 4.2. Equinumerosity

**Definition 4.2.1 (Equinumerosity)** For sets $A$ and $B$, if there is a bijection from $A$ to $B$, then $A$ and $B$ are said to be **equinumerous**, written $A \approx B$; otherwise $A$ and $B$ are not equinumerous, written $A \not\approx B$.

**Theorem 4.2.1** For every set $A$,

$$
\mathcal{P}(A) \approx {}^{A}2,
$$

where $2 = \{0, 1\}$ and ${}^{A}2$ is the set of all functions from $A$ to $\{0, 1\}$.

Sending each subset $B \subseteq A$ to its characteristic function $\chi_B$ (Definition 3.1.10) gives a bijection from $\mathcal{P}(A)$ to ${}^{A}2$.

**Theorem 4.2.2** For all sets $A$, $B$ and $C$,

1. $A \approx A$;
2. if $A \approx B$, then $B \approx A$;
3. if $A \approx B$ and $B \approx C$, then $A \approx C$.

The following theorem, *Cantor's theorem*, shows that infinite sets also differ in size: the set of real numbers is "larger" than the set of natural numbers, and every set is "smaller" than its power set.

**Theorem 4.2.3 (Cantor's Theorem)**

1. $\mathbb{N} \not\approx \mathbb{R}$;
2. $A \not\approx \mathcal{P}(A)$ for every set $A$.

**Proof** (2) Let $f\colon A \to \mathcal{P}(A)$ be any function, and let

$$
D = \{x \mid x \in A \land x \notin f(x)\} \in \mathcal{P}(A).
$$

If there were an $a \in A$ with $f(a) = D$, then $a \in D \Leftrightarrow a \notin f(a) \Leftrightarrow a \notin D$, a contradiction. Hence $D \notin \operatorname{ran}(f)$, so $f$ is not a **surjection**, let alone a bijection.

(1) We use the diagonal argument. Let $f\colon \mathbb{N} \to \mathbb{R}$ be any function. For each $n$, if $f(n) \in [0, 1)$, write it as a decimal $0.a_{n0}a_{n1}a_{n2}\cdots$ (not ending in an infinite string of $9$s, so that this expansion is unique); otherwise set $a_{nn} = 0$. Let $b_n = 5$ if $a_{nn} \neq 5$ and $b_n = 4$ if $a_{nn} = 5$, and put $b = 0.b_0b_1b_2\cdots \in [0, 1)$. For each $n$, if $f(n) \in [0, 1)$, then $b$ and $f(n)$ differ in the $n$th decimal digit (no digit of $b$ is $0$ or $9$, so its decimal expansion is also unique), hence $b \neq f(n)$; if $f(n) \notin [0, 1)$, then clearly $b \neq f(n)$. Therefore $b \notin \operatorname{ran}(f)$, so $f$ is not surjective, and $\mathbb{N} \not\approx \mathbb{R}$. $\square$

## 4.3. Finite and Infinite Sets

**Definition 4.3.1 (Finite and Infinite Sets)** A set $A$ is finite if and only if there is an $n \in \mathbb{N}$ with $n \approx A$. A set $A$ is infinite if and only if it is not finite, that is, there is no $n \in \mathbb{N}$ with $n \approx A$.

Here the **natural number** $n$ is, by Definition 1.7.4, the set $\{0, 1, \cdots, n - 1\}$, so this agrees with Definition 1.6.2.

**Theorem 4.3.1** No natural number is equinumerous to a proper subset of itself.

**Corollary 4.3.1** No finite set is equinumerous to a proper subset of itself.

**Corollary 4.3.2** Every set that is equinumerous to a proper subset of itself is infinite. Both $\mathbb{N}$ and $\mathbb{R}$ are infinite sets.

For example, $f(n) = n + 1$ is a bijection from $\mathbb{N}$ to its **proper subset** $\mathbb{N} - \{0\}$.

**Corollary 4.3.3** Every finite set is equinumerous to exactly one natural number.

## 4.4. Cardinal Numbers

**Definition 4.4.1 (Cardinal Number)** For any sets $A$ and $B$, their **cardinal numbers** are denoted by $\operatorname{card}(A)$ and $\operatorname{card}(B)$, and

$$
\operatorname{card}(A) = \operatorname{card}(B) \Leftrightarrow A \approx B.
$$

$\operatorname{card}(A)$ is sometimes written $|A|$ or $\#(A)$. For a finite set $A$ and $n \in \mathbb{N}$, if $A \approx n$, then $\operatorname{card}(A) = n$.

The cardinal number of the set $\mathbb{N}$ of natural numbers is not a natural number, since $\mathbb{N}$ is not equinumerous to any natural number. Following Cantor, $\operatorname{card}(\mathbb{N})$ is denoted by $\aleph_0$, read "aleph-null". One can prove that

$$
\operatorname{card}(\mathbb{Z}) = \operatorname{card}(\mathbb{Q}) = \operatorname{card}(\mathbb{N} \times \mathbb{N}) = \aleph_0.
$$

For instance, $f(\langle m, n \rangle) = \dfrac{(m + n)(m + n + 1)}{2} + m$ is a bijection from $\mathbb{N} \times \mathbb{N}$ to $\mathbb{N}$ (it numbers the pairs diagonal by diagonal, according to the value of $m + n$).

The cardinal number of the set $\mathbb{R}$ of real numbers is neither a natural number nor $\aleph_0$ (since $\mathbb{N} \not\approx \mathbb{R}$). It is usually denoted by $\aleph$ (or $\mathfrak{c}$) and called the cardinality of the continuum. One can prove that

$$
\operatorname{card}([0, 1]) = \operatorname{card}((0, 1)) = \operatorname{card}(\mathbb{R}_+) = \aleph = 2^{\aleph_0}.
$$

Some textbooks denote $\operatorname{card}(\mathbb{R})$ by $\aleph_1$. However, $\aleph_1$ usually denotes the least cardinal greater than $\aleph_0$, and "$\operatorname{card}(\mathbb{R}) = \aleph_1$" is precisely the continuum hypothesis of Section 4.7, so it cannot serve as a definition.

## 4.5. Cardinal Arithmetic

**Definition 4.5.1 (Operations on Cardinals)** For any cardinals $k$ and $l$, choose sets $K$ and $L$ with $\operatorname{card}(K) = k$ and $\operatorname{card}(L) = l$, and define

1. $k + l = \operatorname{card}(K \cup L)$, provided $K \cap L = \varnothing$;
2. $k \cdot l = \operatorname{card}(K \times L)$;
3. $k^l = \operatorname{card}({}^{L}K)$, where ${}^{L}K$ is the set of all functions from $L$ to $K$.

These definitions do not depend on the choice of $K$ and $L$, and for the sum disjoint $K$ and $L$ can always be found (for example, by replacing them with $K \times \{0\}$ and $L \times \{1\}$). By Theorem 4.2.1, $\operatorname{card}(\mathcal{P}(A)) = 2^{\operatorname{card}(A)}$.

**Theorem 4.5.1** For all cardinals $k$, $l$ and $m$,

1. $k + l = l + k$, $k \cdot l = l \cdot k$;
2. $k + (l + m) = (k + l) + m$, $k \cdot (l \cdot m) = (k \cdot l) \cdot m$;
3. $k \cdot (l + m) = k \cdot l + k \cdot m$;
4. $k^{l + m} = k^l \cdot k^m$;
5. $(k \cdot l)^m = k^m \cdot l^m$;
6. $(k^l)^m = k^{l \cdot m}$.

## 4.6. Comparing Cardinals

**Definition 4.6.1 (Order of Cardinals)** Let $K$ and $L$ be sets with $\operatorname{card}(K) = k$ and $\operatorname{card}(L) = l$. If there is an injection from $K$ to $L$, then we say that $L$ dominates $K$, written $K \preceq L$, and that the cardinal $k$ is at most the cardinal $l$, written $k \leq l$.

**Definition 4.6.2** For cardinals $k$ and $l$, if $k \leq l$ and $k \neq l$, then $k$ is said to be less than $l$, written $k < l$.

By Cantor's theorem and Theorem 4.2.1, $k < 2^k$ for every cardinal $k$.

**Theorem 4.6.1** For all cardinals $k$, $l$ and $m$,

1. $k \leq k$;
2. if $k \leq l$ and $l \leq m$, then $k \leq m$;
3. if $k \leq l$ and $l \leq k$, then $k = l$;
4. $k \leq l$ or $l \leq k$.

Item 3 is the *Schröder–Bernstein theorem*: if there are an **injection** from $K$ to $L$ and an injection from $L$ to $K$, then there is a bijection from $K$ to $L$. Its proof does not need the **axiom of choice**, whereas item 4 (the comparability of cardinals) is equivalent to the axiom of choice.

**Example 4.6.1** $\operatorname{card}((0, 1)) = \operatorname{card}([0, 1])$. The map $f(x) = x$ is an injection from $(0, 1)$ to $[0, 1]$, and $g(x) = \dfrac{x + 1}{3}$ is an injection from $[0, 1]$ to $[1/3, 2/3] \subseteq (0, 1)$; the Schröder–Bernstein theorem then gives the result without constructing a bijection explicitly.

**Theorem 4.6.2** For all cardinals $k$, $l$ and $m$, if $k \leq l$, then

1. $k + m \leq l + m$;
2. $k \cdot m \leq l \cdot m$;
3. $k^m \leq l^m$;
4. $m^k \leq m^l$, provided $k \neq 0$ or $m \neq 0$.

The hypothesis of item 4 cannot be dropped: for $k = m = 0$ and $l = 1$ we have $m^k = 0^0 = 1$ but $m^l = 0^1 = 0$.

**Theorem 4.6.3** For cardinals $k$ and $l$, if $k \leq l$, $k \neq 0$ and $l$ is an infinite cardinal, then

$$
k + l = k \cdot l = l = \max(k, l).
$$

**Theorem 4.6.4**

1. $\mathbb{N} \preceq K$ for every infinite set $K$;
2. $\aleph_0 \leq k$ for every infinite cardinal $k$.

That is, $\aleph_0$ is the least infinite cardinal.

## 4.7. Countable Sets and the Continuum Hypothesis

**Definition 4.7.1 (Countable Set)** A set $K$ is called a **countable set** if $\operatorname{card}(K) \leq \aleph_0$.

The countable sets comprise the finite sets and the sets of cardinality $\aleph_0$; the latter are also called countably infinite, and their elements can be arranged in an infinite sequence $a_0, a_1, a_2, \cdots$.

**Theorem 4.7.1 (Properties of Countable Sets)**

1. Every subset of a countable set is countable;
2. the union and the **Cartesian product** of two countable sets are countable;
3. if $K$ is an infinite set, then $\mathcal{P}(K)$ is uncountable;
4. a countable union of countable sets is countable; that is, if $A$ is a countable set whose elements are all countable sets, then $\bigcup A$ is countable.

The proof of item 4 requires fixing an enumeration of each member set, which uses the **axiom of choice**.

The familiar cardinals, in increasing order, are

$$
0 < 1 < \cdots < n < \cdots < \aleph_0 < \aleph < 2^{\aleph} < \cdots.
$$

The *continuum hypothesis*: there is no cardinal $k$ such that

$$
\aleph_0 < k < 2^{\aleph_0}.
$$

In ZFC it is equivalent to $2^{\aleph_0} = \aleph_1$, and also to the statement that every infinite subset of $\mathbb{R}$ is equinumerous either to $\mathbb{N}$ or to $\mathbb{R}$. Gödel (1940) proved that the continuum hypothesis cannot be refuted in ZFC, and Cohen (1963) proved that it cannot be proved in ZFC either: on the basis of the existing **axiomatic system**, it can be shown neither true nor false.

## Summary

- The construction of the number systems (Section 4.1) starts from $\mathbb{N}$: $\mathbb{Z}$ consists of the positive integers and negative integers of the form $\langle 0, n\rangle$ (Definition 4.1.1); $\mathbb{Q} = Q_1/{\approx}$ is a quotient set of pairs of integers (Definition 4.1.5); and $\mathbb{R} = B/{\sim}$ consists of equivalence classes of basic functions, that is, sequences of rationals that are bounded above and eventually nondecreasing (Definition 4.1.9).
- Equinumerosity (Definition 4.2.1) compares the sizes of sets by bijections. Cantor's theorem (Theorem 4.2.3) gives $\mathbb{N} \not\approx \mathbb{R}$ and $A \not\approx \mathcal{P}(A)$, proved by the diagonal argument and by the set $D = \{x \in A \mid x \notin f(x)\}$, respectively.
- A finite set is not equinumerous to any of its proper subsets (Corollary 4.3.1), and a set equinumerous to a proper subset must be infinite (Corollary 4.3.2).
- Cardinal numbers (Definition 4.4.1) and their operations (Definition 4.5.1) obey the usual arithmetic laws (Theorem 4.5.1); the sum and product of infinite cardinals equal the larger one (Theorem 4.6.3).

  | Cardinal | Examples |
  | :-- | :-- |
  | $\aleph_0$, the smallest infinite cardinal (Theorem 4.6.4) | $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{N} \times \mathbb{N}$ |
  | $\aleph = 2^{\aleph_0}$ | $\mathbb{R}$, $[0, 1]$, $(0, 1)$, $\mathcal{P}(\mathbb{N})$ |
  | $2^{\aleph}$ | $\mathcal{P}(\mathbb{R})$ |

- The order of cardinals (Definition 4.6.1) is defined by injections; its antisymmetry is the Schröder–Bernstein theorem (Theorem 4.6.1), the most common tool for proving that two sets are equinumerous. By Cantor's theorem, $k < 2^k$ for every cardinal $k$.
- Subsets, finite unions and Cartesian products of countable sets (Definition 4.7.1) are countable (Theorem 4.7.1). The continuum hypothesis asserts that there is no cardinal strictly between $\aleph_0$ and $2^{\aleph_0}$; it is independent of ZFC.
