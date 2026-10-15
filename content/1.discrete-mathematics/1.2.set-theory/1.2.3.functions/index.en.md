---
title: Functions
source_hash: 884a0e3a724b
---

A function is a special kind of **binary relation**: each element of the domain corresponds to exactly one element of the range. Building on the theory of relations from the previous chapter, this chapter defines functions together with injections, surjections and bijections, discusses composition and inverses of functions and the compatibility of functions, then uses the language of functions to introduce open and closed sets of real numbers, and finally passes from characteristic functions to fuzzy subsets. Bijections are the basic tool of the next chapter for comparing the sizes of sets (equinumerosity and cardinal numbers).

## 3.1. Functions and the Axiom of Choice

**Definition 3.1.1 (Function)** Let $f$ be a relation from a set $A$ to a set $B$ satisfying the following conditions:

1. for every $x \in \operatorname{dom}(f)$ there is a unique $y \in \operatorname{ran}(f)$ such that $xfy$;
2. $\operatorname{dom}(f) = A$.

Then $f$ is called a **function** from $A$ to $B$, or we say that $f$ maps $A$ into $B$ (some books also speak of a total function, a map or a transformation), written $f: A \rightarrow B$. In this case, if $xfy$, we write $f: x \mapsto y$ or $f(x) = y$.

The two conditions on a function can be written as

$$
\begin{aligned}
& (\forall x)(\forall y_1)(\forall y_2)((xfy_1 \land xfy_2) \rightarrow y_1 = y_2), \\
& (\forall x)(x \in A \rightarrow (\exists y)(y \in B \land xfy)).
\end{aligned}
$$

**Definition 3.1.2 (The Set of Functions from $A$ to $B$)** For sets $A$ and $B$, the set of all functions from $A$ to $B$ is written ${}^{A}B$ (some books write $B^A$); that is,

$$
{}^{A}B = \{f \mid f: A \rightarrow B\}.
$$

If $A$ and $B$ are finite sets with $|A| = m$ and $|B| = n$, then $|{}^{A}B| = n^m$.

**Definition 3.1.3 (Image and Preimage)** Let $f: A \rightarrow B$, $A_1 \subseteq A$ and $B_1 \subseteq B$. The **image** $f[A_1]$ of $A_1$ under $f$ and the **preimage** (inverse image) $f^{-1}[B_1]$ of $B_1$ under $f$ are defined by

$$
\begin{aligned}
f[A_1] &= \{y \mid (\exists x)(x \in A_1 \land y = f(x))\}, \\
f^{-1}[B_1] &= \{x \mid x \in A \land f(x) \in B_1\}.
\end{aligned}
$$

$f[A]$ is called the image of the function $f$.

**Definition 3.1.4 (Surjection, Injection and Bijection)** Let $f: A \rightarrow B$.

1. If $\operatorname{ran}(f) = B$, then $f$ is said to be surjective, or a **surjection**, or to map $A$ onto $B$;
2. if $f(x_1) \neq f(x_2)$ for all $x_1, x_2 \in A$ with $x_1 \neq x_2$, then $f$ is said to be injective, or an **injection**, or one-to-one;
3. if $f$ is both surjective and injective, then $f$ is said to be bijective, or a one-to-one correspondence between $A$ and $B$, or simply a **bijection**.

**Example 3.1.1** Let $f, g, h: \mathbb{N} \rightarrow \mathbb{N}$ with $f(n) = 2n$, $g(n) = \lfloor n/2 \rfloor$ and $h(n) = n + (-1)^n$ (which swaps $0$ and $1$, $2$ and $3$, and so on). Then $f$ is injective but not surjective (the odd numbers are not in its range); $g$ is surjective but not injective ($g(0) = g(1) = 0$); and $h$ is bijective.

**Definition 3.1.5 (Constant Function)** Let $f: A \rightarrow B$. If there is a $y \in B$ such that $f(x) = y$ for all $x \in A$, that is, $f[A] = \{y\}$, then $f$ is called a **constant function**.

**Definition 3.1.6 (Identity Function)** The identity relation $I_A: A \rightarrow A$ on $A$ is called the **identity function** on $A$. For every $x \in A$, $I_A(x) = x$.

**Definition 3.1.7 (Monotone Function)** Let $f: \mathbb{R} \rightarrow \mathbb{R}$. If $x \leq y \rightarrow f(x) \leq f(y)$ for all $x, y \in \mathbb{R}$, then $f$ is called **monotonically increasing**; if $x < y \rightarrow f(x) < f(y)$, then $f$ is called **strictly increasing**. Monotonically decreasing and strictly decreasing functions are defined similarly.

**Definition 3.1.8 ($n$-ary Operation)** For a set $A$ and $n \in \mathbb{N}$, a function $f: A^n \rightarrow A$ is called an **$n$-ary operation** on $A$, where $A^n$ is the $n$-fold Cartesian product of $A$.

**Definition 3.1.9 (Functional)** Let $A, B, C$ be sets and let ${}^{B}C$ be the set of all functions from $B$ to $C$. A function $F: A \rightarrow {}^{B}C$ is called a **functional** (sometimes a function $G: {}^{B}C \rightarrow A$ is also called a functional).

**Definition 3.1.10 (Characteristic Function of a Set)** Let $E$ be the universal set. For every $A \subseteq E$, the **characteristic function** (also called the indicator function) $\chi_A$ of $A$ is defined by

$$
\chi_A: E \rightarrow \{0, 1\}, \qquad \chi_A(a) =
\begin{cases}
1, & a \in A, \\
0, & a \notin A.
\end{cases}
$$

**Definition 3.1.11 (Canonical Map)** Let $R$ be an equivalence relation on $A$, and let $g: A \rightarrow A/R$ be given by $g(a) = [a]_R$. Then $g$ is called the **canonical map** (or natural map) from $A$ to the quotient set $A/R$.

**Axiom of choice** (first form). For every relation $R$ there is a function $f$ such that

$$
f \subseteq R \quad \text{and} \quad \operatorname{dom}(f) = \operatorname{dom}(R).
$$

This is the tenth axiom of **Zermelo–Fraenkel set theory** listed in [Section 1.7](/1.2.1#sec-1.7). Intuitively, for each $x$ in $\operatorname{dom}(R)$ we can simultaneously "choose" an element $f(x)$ of $\{y \mid xRy\}$.

## 3.2. Composition and Inverses of Functions

Composition of functions is composition of relations (Definition 2.3.1), and the inverse of a function is its inverse as a relation.

**Theorem 3.2.1 (Composition of Functions)** Let $g: A \rightarrow B$ and $f: B \rightarrow C$. Then

1. $f \circ g$ is a function $f \circ g: A \rightarrow C$;
2. $(f \circ g)(x) = f(g(x))$ for every $x \in A$.

**Theorem 3.2.2 (Properties of Composition, I)** Let $g: A \rightarrow B$ and $f: B \rightarrow C$.

1. If $f$ and $g$ are surjective, then $f \circ g$ is surjective;
2. if $f$ and $g$ are injective, then $f \circ g$ is injective;
3. if $f$ and $g$ are bijective, then $f \circ g$ is bijective.

**Theorem 3.2.3 (Properties of Composition, II)** Let $g: A \rightarrow B$ and $f: B \rightarrow C$.

1. If $f \circ g$ is surjective, then $f$ is surjective;
2. if $f \circ g$ is injective, then $g$ is injective;
3. if $f \circ g$ is bijective, then $f$ is surjective and $g$ is injective.

**Proof** (1) For any $z \in C$, since $f \circ g$ is surjective there is an $x \in A$ with $f(g(x)) = z$, so $g(x) \in B$ is a preimage of $z$ under $f$; hence $f$ is surjective. (2) If $g(x_1) = g(x_2)$, then $(f \circ g)(x_1) = (f \circ g)(x_2)$, and since $f \circ g$ is injective, $x_1 = x_2$; hence $g$ is injective. (3) follows from (1) and (2). $\square$

These conclusions cannot be strengthened: take $A = C = \{0\}$, $B = \{0, 1\}$, $g(0) = 0$ and $f(0) = f(1) = 0$. Then $f \circ g = I_{\{0\}}$ is a bijection, but $f$ is not injective and $g$ is not surjective.

**Theorem 3.2.4** If $f: A \rightarrow B$, then $f = f \circ I_A = I_B \circ f$.

**Theorem 3.2.5 (Inverse of a Function)** If $f: A \rightarrow B$ is bijective, then $f^{-1}$ is a function $f^{-1}: B \rightarrow A$.

**Definition 3.2.1 (Inverse Function)** If $f: A \rightarrow B$ is bijective, then $f^{-1}: B \rightarrow A$ is called the inverse function of $f$.

**Theorem 3.2.6** If $f: A \rightarrow B$ is bijective, then $f^{-1}: B \rightarrow A$ is bijective.

**Theorem 3.2.7** If $f: A \rightarrow B$ is bijective, then $f^{-1}(f(x)) = x$ for every $x \in A$ and $f(f^{-1}(y)) = y$ for every $y \in B$; that is, $f^{-1} \circ f = I_A$ and $f \circ f^{-1} = I_B$.

**Definition 3.2.2 (Left Inverse and Right Inverse)** Let $f: A \rightarrow B$ and $g: B \rightarrow A$. If $g \circ f = I_A$, then $g$ is called a **left inverse** of $f$; if $f \circ g = I_B$, then $g$ is called a **right inverse** of $f$.

**Theorem 3.2.8** Let $f: A \rightarrow B$ with $A \neq \emptyset$. Then

1. $f$ has a left inverse if and only if $f$ is injective;
2. $f$ has a right inverse if and only if $f$ is surjective;
3. $f$ has both a left inverse and a right inverse if and only if $f$ is bijective;
4. if $f$ is bijective, then its left inverse equals its right inverse (both equal $f^{-1}$).

The necessity in (1) and (2) follows at once from Theorem 3.2.3. Sufficiency in (1): fix $a_0 \in A$ and let $g(y) = f^{-1}(y)$ for $y \in \operatorname{ran}(f)$ (uniquely determined because $f$ is injective) and $g(y) = a_0$ for $y \notin \operatorname{ran}(f)$; this is where $A \neq \emptyset$ is used. Sufficiency in (2) requires choosing, for each $y \in B$, an element of the nonempty set $f^{-1}[\{y\}]$ as $g(y)$, which needs the **axiom of choice**. (4): if $g$ is a left inverse and $h$ a right inverse, then $g = g \circ I_B = g \circ (f \circ h) = (g \circ f) \circ h = I_A \circ h = h$.

## 3.3. Properties of Functions

**Definition 3.3.1 (Compatible Functions)** Let $f: A \rightarrow B$ and $g: C \rightarrow D$. If $f(x) = g(x)$ for every $x \in A \cap C$, then $f$ and $g$ are said to be **compatible**.

**Definition 3.3.2 (Compatible Sets of Functions)** Let $\mathcal{C}$ be a set of functions. If any two functions in $\mathcal{C}$ are compatible, then $\mathcal{C}$ is said to be compatible.

**Theorem 3.3.1** Let $f: A \rightarrow B$ and $g: C \rightarrow D$. Then $f$ and $g$ are compatible if and only if $f \cup g$ is a function.

**Theorem 3.3.2** Let $f: A \rightarrow B$ and $g: C \rightarrow D$. Then $f$ and $g$ are compatible if and only if

$$
f \upharpoonright (A \cap C) = g \upharpoonright (A \cap C).
$$

**Theorem 3.3.3** Let $\mathcal{C}$ be a set of functions. If $\mathcal{C}$ is compatible and $F = \bigcup \mathcal{C}$, then $F$ is a function $F: \operatorname{dom}(F) \rightarrow \operatorname{ran}(F)$, and

$$
\operatorname{dom}(F) = \textstyle\bigcup \{\operatorname{dom}(f) \mid f \in \mathcal{C}\}.
$$

**Definition 3.3.3 (Compatibility of a Relation with a Function)** Let $R$ be an equivalence relation on $A$ and $f: A \rightarrow A$. If $\langle x, y \rangle \in R \Rightarrow \langle f(x), f(y) \rangle \in R$ for all $x, y \in A$, then the relation $R$ and the function $f$ are said to be compatible.

**Theorem 3.3.4** Let $R$ be an equivalence relation on $A$ and $f: A \rightarrow A$. If $R$ and $f$ are compatible, then there is a unique function $F: A/R \rightarrow A/R$ with $F([x]_R) = [f(x)]_R$; if $R$ and $f$ are not compatible, then no such function $F$ exists.

Compatibility guarantees that the definition of $F$ does not depend on the choice of representatives. For example, let $R$ be congruence modulo $3$ on $\mathbb{Z}$. The function $f(x) = x + 1$ is compatible with $R$ and induces $F([x]) = [x + 1]$; but $f(x) = \lfloor x/2 \rfloor$ is not compatible with $R$, because $0 R 3$ while $f(0) = 0$ and $f(3) = 1$ are not congruent.

## 3.4. Open Sets and Closed Sets

**Definition 3.4.1 (Distance)** On the set $\mathbb{R}$ of real numbers, define $\rho: \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}$ by $\rho(\langle x, y \rangle) = |x - y|$, where $|x - y|$ is the absolute value of $x - y$; $\rho$ is called the **distance function** on $\mathbb{R}$. For every $\langle x, y \rangle \in \mathbb{R} \times \mathbb{R}$, $\rho(\langle x, y \rangle)$ is called the distance between $x$ and $y$, also written $\rho(x, y) = |x - y|$.

**Definition 3.4.2 (Neighborhood)** Let $x_0 \in \mathbb{R}$, and let $\varepsilon \in \mathbb{R}$ with $\varepsilon > 0$. The **$\varepsilon$-neighborhood** of $x_0$ is the set

$$
\{x \mid x \in \mathbb{R} \land \rho(x_0, x) < \varepsilon\}.
$$

**Definition 3.4.3 (Limit Point)** Let $A \subseteq \mathbb{R}$ and $x_0 \in \mathbb{R}$. If every $\varepsilon$-neighborhood of $x_0$ contains an element of $A$ different from $x_0$, then $x_0$ is called a **limit point** (or accumulation point) of $A$. The condition can be written as

$$
(\forall \varepsilon)((\varepsilon \in \mathbb{R} \land \varepsilon > 0) \rightarrow (\exists x)(x \in A \land x \neq x_0 \land \rho(x, x_0) < \varepsilon)).
$$

**Theorem 3.4.1** Let $A \subseteq \mathbb{R}$ and $x_0 \in \mathbb{R}$. Then $x_0$ is a limit point of $A$ if and only if there is a sequence $\{x_n\}$ of pairwise distinct points of $A$, all different from $x_0$ (that is, $x_n \in A$, $x_n \neq x_0$, and $m \neq n \rightarrow x_m \neq x_n$), such that $\lim_{n \to \infty} x_n = x_0$.

**Theorem 3.4.2** Every bounded infinite set $A \subseteq \mathbb{R}$ has a limit point.

**Definition 3.4.4 (Isolated Point)** Let $A \subseteq \mathbb{R}$ and $x_0 \in A$. If $x_0$ is not a limit point of $A$, then $x_0$ is called an **isolated point** of $A$.

**Definition 3.4.5 (Derived Set and Closed Set)** Let $A \subseteq \mathbb{R}$. The set of all limit points of $A$ is called the **derived set** of $A$, written $A'$. If $A' \subseteq A$, then $A$ is called a **closed set**.

**Theorem 3.4.3** For every $A \subseteq \mathbb{R}$, the derived set $A'$ is closed; that is, $(A')' \subseteq A'$.

**Theorem 3.4.4** The intersection of any family of closed sets is closed, and the union of finitely many closed sets is closed.

**Definition 3.4.6 (Interior Point)** Let $A \subseteq \mathbb{R}$ and $x_0 \in \mathbb{R}$. If some $\varepsilon$-neighborhood of $x_0$ consists entirely of elements of $A$, then $x_0$ is called an **interior point** of $A$. The condition can be written as

$$
(\exists \varepsilon)(\varepsilon \in \mathbb{R} \land \varepsilon > 0 \land (\forall x)((x \in \mathbb{R} \land \rho(x, x_0) < \varepsilon) \rightarrow x \in A)).
$$

**Definition 3.4.7 (Open Set)** Let $A \subseteq \mathbb{R}$. If every element of $A$ is an interior point of $A$, then $A$ is called an **open set**.

**Theorem 3.4.5** The union of any family of open sets is open, and the intersection of finitely many open sets is open.

The word "finitely" cannot be dropped: the intersection of the open sets $(-1/n, 1/n)$ ($n = 1, 2, \cdots$) is $\{0\}$, which is not open, and the union of the closed sets $[1/n, 1]$ is $(0, 1]$, which is not closed.

**Theorem 3.4.6** Let $A \subseteq \mathbb{R}$.

1. If $A$ is open, then $\mathbb{R} - A$ is closed;
2. if $A$ is closed, then $\mathbb{R} - A$ is open.

## 3.5. Fuzzy Subsets

**Theorem 3.5.1 (Properties of Characteristic Functions)** Let $E$ be the **domain of discourse** (the universal set), $A \subseteq E$ and $B \subseteq E$; let $+$, $-$ and $\cdot$ denote arithmetic addition, subtraction and multiplication, and let $\bar{A} = E - A$ be the absolute complement of $A$. Then (items 5–8 hold for every $x \in E$):

1. $(\forall x)(\chi_A(x) = 0) \Leftrightarrow A = \emptyset$;
2. $(\forall x)(\chi_A(x) = 1) \Leftrightarrow A = E$;
3. $(\forall x)(\chi_A(x) \leq \chi_B(x)) \Leftrightarrow A \subseteq B$;
4. $(\forall x)(\chi_A(x) = \chi_B(x)) \Leftrightarrow A = B$;
5. $\chi_{A \cap B}(x) = \chi_A(x) \cdot \chi_B(x)$;
6. $\chi_{A \cup B}(x) = \chi_A(x) + \chi_B(x) - \chi_{A \cap B}(x)$;
7. $\chi_{A - B}(x) = \chi_A(x) - \chi_{A \cap B}(x)$;
8. $\chi_{\bar{A}}(x) = 1 - \chi_A(x)$.

An ordinary subset is completely determined by its characteristic function, which takes values in $\{0, 1\}$. Allowing the values to range over the whole interval $[0, 1]$ gives fuzzy subsets.

**Definition 3.5.1 (Fuzzy Subset and Membership Function)** Let $E$ be a domain of discourse. A **fuzzy subset** $A$ of $E$ is given by a function $\mu_A: E \rightarrow [0, 1]$, where $\mu_A(x)$ expresses the degree to which $x$ belongs to $A$; $\mu_A$ is called the **membership function** of $A$. The set of all fuzzy subsets of $E$ is written $F(E)$.

**Definition 3.5.2 (Operations on Fuzzy Subsets)** Let $E$ be the universal set and $A, B \in F(E)$. The fuzzy subsets $A \cup B$, $A \cap B$ and $\bar{A}$ with the following membership functions are called the union and the intersection of $A$ and $B$ and the absolute complement of $A$, respectively:

$$
\begin{aligned}
\mu_{A \cup B}(x) &= \max(\mu_A(x), \mu_B(x)), \\
\mu_{A \cap B}(x) &= \min(\mu_A(x), \mu_B(x)), \\
\mu_{\bar{A}}(x) &= 1 - \mu_A(x).
\end{aligned}
$$

**Definition 3.5.3 (Cut)** Let $E$ be the universal set, $A \in F(E)$ and $\lambda \in [0, 1]$. The **$\lambda$-cut** $(A)_\lambda$ of $A$ (also written $A_\lambda$) is defined by

$$
(A)_\lambda = \{x \mid x \in E \land \mu_A(x) \geq \lambda\}.
$$

It is an ordinary subset of $E$.

**Theorem 3.5.2** Let $E$ be the universal set, $A, B \in F(E)$ and $\lambda \in [0, 1]$. Then

1. $(A \cup B)_\lambda = A_\lambda \cup B_\lambda$;
2. $(A \cap B)_\lambda = A_\lambda \cap B_\lambda$.

**Theorem 3.5.3** Let $E$ be the universal set, $A \in F(E)$ and $\lambda, \sigma \in [0, 1]$. Then

1. $\lambda \leq \sigma \Rightarrow A_\sigma \subseteq A_\lambda$;
2. $A_0 = E$.

**Theorem 3.5.4 (Decomposition Theorem)** Let $E$ be the universal set, $A \in F(E)$, and let $\chi_{A_\lambda}$ be the characteristic function of the cut $A_\lambda$. Then for every $u \in E$,

$$
\mu_A(u) = \sup_{\lambda \in [0, 1]} \min(\lambda, \chi_{A_\lambda}(u)),
$$

where $\sup$ denotes the **supremum**.

Indeed, when $\lambda \leq \mu_A(u)$ we have $u \in A_\lambda$ and $\min(\lambda, \chi_{A_\lambda}(u)) = \lambda$; when $\lambda > \mu_A(u)$ this value is $0$. Hence the right-hand side equals $\sup\{\lambda \mid \lambda \leq \mu_A(u)\} = \mu_A(u)$. The decomposition theorem shows that a fuzzy subset is determined by the family of all its cuts.

**Definition 3.5.4 (Support, Core, Boundary and Normal Fuzzy Set)** Let $E$ be the universal set and $A \in F(E)$. The set $\operatorname{supp} A = \{u \mid u \in E \land \mu_A(u) > 0\}$ is called the **support** of $A$, the cut $A_1$ is called the core of $A$, and $(\operatorname{supp} A) - A_1$ is called the boundary of $A$. If $A_1 \neq \emptyset$, then $A$ is called a **normal fuzzy set**; if $A_1 = \emptyset$, then $A$ is called a subnormal fuzzy set.

The elements of the core $A_1$ belong to $A$ fully, while the elements of the boundary belong to $A$ only partially.
