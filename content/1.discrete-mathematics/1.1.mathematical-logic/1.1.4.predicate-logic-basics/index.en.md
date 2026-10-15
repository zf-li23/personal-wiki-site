---
title: Basic Concepts of Predicate Logic
source_hash: d45735179c06
---

Propositional logic treats simple propositions as indivisible wholes, so it cannot analyze their internal logical structure (such as the relation between subject and predicate) or quantitative relations (such as "all" and "some"). To overcome these limitations we introduce *predicate logic*. Predicate logic can be viewed as an extension of propositional logic: it introduces **individual terms**, **predicates**, and **quantifiers**, which allow a finer description of the structure of sentences and of reasoning. This chapter deals only with first-order predicate logic, historically also called the restricted predicate calculus; the next chapter treats equivalence and inference in it.

## 4.1. Predicates and Individual Terms

### 4.1.1. Individual Terms

**Definition 4.1.1 (Individual Term)** An object, concrete or abstract, that can exist independently among the things under study is called an **individual term**. In a proposition, an individual term is usually a word denoting an object of thought, and is also called the **subject**.

### 4.1.2. Individual Constants and Individual Variables

**Definition 4.1.2 (Individual Constants and Individual Variables)** An individual term denoting a concrete or specific object is called an **individual constant** and is denoted by a lowercase letter $a, b, c, \cdots$; an individual term denoting an abstract or unspecified object is called an **individual variable** and is denoted by a lowercase letter $x, y, z, \cdots$.

**Definition 4.1.3 (Domain of Discourse)** The range of values of the individual variables is called the **domain of discourse**, or **universe**, and is denoted by $D$; in this course it is always assumed to be nonempty. The domain consisting of all things in the world is called the **universal domain**.

### 4.1.3. Predicates

**Definition 4.1.4 (Predicate)** A word that describes a property of individuals or a relation between individuals is called a **predicate**. An $n$-ary predicate can be viewed as a map from $D^n$ to the set of truth values $\{0, 1\}$.

### 4.1.4. Predicate Constants and Predicate Variables

**Definition 4.1.5 (Predicate Constants and Predicate Variables)** A predicate expressing a specific property or relation is called a **predicate constant**, and a predicate expressing an abstract or unspecified property or relation is called a **predicate variable**. Both are denoted by uppercase letters $P, Q, R, \cdots$, and are distinguished by context.

### 4.1.5. Unary and $n$-ary Predicates

**Definition 4.1.6 (Unary and $n$-ary Predicates)** A predicate describing a property of a single individual is called a **unary predicate** and is written $P(x), Q(x), \cdots$. A predicate describing a relation among several individuals is called a **many-place predicate**; a predicate with $n$ individual variables is called an $n$-ary predicate and is written $P(x_1, x_2, \cdots, x_n)$ ($n \geq 1$).

**Example 4.1.1** $P(x)$: $x$ is a student; this is a unary predicate. $P(x, y)$: $x$ and $y$ are classmates; this is a binary predicate.

In general:

- $P(a)$ means that the individual constant $a$ has the property $P$;
- $P(x)$ means that the individual variable $x$ has the property $P$;
- $P(a, b)$ means that the individual constants $a, b$ stand in the relation $P$;
- $P(x, y)$ means that the individual variables $x, y$ stand in the relation $P$.

### 4.1.6. Predicate Logic and Propositional Logic

**Definition 4.1.7 (Nullary Predicate)** A predicate with no individual variables is called a **nullary predicate**.

A nullary predicate that is a predicate constant is simply a **proposition**. Hence every proposition of **propositional logic** can be represented as a nullary predicate constant, and propositional logic can be regarded as a special case of predicate logic.

## 4.2. Functions and Quantifiers

### 4.2.1. Functions in Predicate Logic

Functions can be introduced into predicate logic: an $n$-ary function is a map from $D^n$ to the domain $D$ (the domain need not be a set of numbers). Function symbols are denoted by lowercase letters $f, g, h, \cdots$. A function applied to individuals yields an individual, so functions are generally not used on their own but appear inside predicates.

**Example 4.2.1** Let $\mathrm{father}(x)$ denote the father of $x$, and $P(x)$ mean that $x$ is a teacher. Then $P(\mathrm{father}(x))$ means "the father of $x$ is a teacher".

### 4.2.2. Quantifiers

**Definition 4.2.1 (Quantifier)** A word expressing a quantitative relation among individuals is called a **quantifier**; it is a restriction or constraint imposed on individual terms. The two main quantifiers are the universal quantifier and the existential quantifier.

### 4.2.3. The Universal Quantifier

**Definition 4.2.2 (Universal Quantifier)** The quantifier corresponding to words such as "all", "every", "any", "each", and "whatever" is called the **universal quantifier** and is written $\forall$. $(\forall x)P(x)$ means that every individual $x$ in the domain has the property $P$.

- $(\forall x)P(x)$ is true if and only if $P(x)$ is true for every $x \in D$;
- $(\forall x)P(x)$ is false if and only if there is at least one $x_0 \in D$ such that $P(x_0)$ is false.

### 4.2.4. The Existential Quantifier

**Definition 4.2.3 (Existential Quantifier)** The quantifier corresponding to words such as "there exists", "there is", "some", and "certain" is called the **existential quantifier** and is written $\exists$. $(\exists x)P(x)$ means that some individual $x$ in the domain has the property $P$.

- $(\exists x)P(x)$ is true if and only if there is at least one $x_0 \in D$ such that $P(x_0)$ is true;
- $(\exists x)P(x)$ is false if and only if $P(x)$ is false for every $x \in D$.

### 4.2.5. Bound and Free Variables

**Definition 4.2.4 (Bound and Free Variables)** In the formulas $(\forall x)A$ and $(\exists x)A$, $A$ is called the **scope** of the respective quantifier. Within the scope of a quantifier, an occurrence of the variable with the same name as the quantifier's variable is called a **bound occurrence**; a variable that occurs bound is called a **bound variable**, and a variable that occurs in a formula other than in a bound occurrence is called a **free variable**.

**Example 4.2.2** In $(\forall x)P(x) \lor Q(y)$, $x$ is a bound variable and $y$ is a free variable; in $(\forall x)(P(x) \to Q(x, y))$, $x$ is a bound variable and $y$ is a free variable.

**Remark 4.2.1**

1. *Renaming of bound variables*: a bound variable may be renamed, provided the new name does not occur in its scope; for example, $(\forall x)P(x)$ and $(\forall y)P(y)$ are equivalent;
2. A predicate formula with no free variables expresses a proposition;
3. Prefixing an $n$-ary predicate $P(x_1, \cdots, x_n)$ with $k$ quantifiers that bind $k$ distinct variables among them yields an $(n - k)$-ary predicate.

## 4.3. Well-Formed Formulas

### 4.3.1. First-Order Predicate Logic

**Definition 4.3.1 (First-Order Predicate Logic)** Predicate logic in which quantifiers apply only to individual variables, and neither to propositional variables nor to predicate variables, and in which "predicates of predicates" are not considered, is called **first-order logic** (first-order predicate logic, or the restricted predicate calculus), to distinguish it from higher-order predicate logic.

**Example 4.3.1** In $(\forall p)(p \to Q(x))$ the quantifier applies to the propositional variable $p$, and in $(\exists Q)(Q(x) \to P(x))$ the quantifier applies to the predicate variable $Q$; neither is a formula of first-order logic.

### 4.3.2. The Symbols of First-Order Logic

1. Individual constants: $a, b, c, \cdots$;
2. Individual variables: $x, y, z, \cdots$;
3. Propositional variables: $p, q, r, \cdots$;
4. Predicate symbols: $P, Q, R, \cdots$;
5. Function symbols: $f, g, h, \cdots$;
6. Connectives: $\lnot, \land, \lor, \to, \leftrightarrow$;
7. Quantifier symbols: $\forall, \exists$;
8. Parentheses and comma: $($, $)$, and $,$.

### 4.3.3. Well-Formed Formulas

**Definition 4.3.2 (Well-Formed Formula)** The **well-formed formulas** (predicate formulas) of predicate logic are defined recursively as follows:

1. Propositional constants, propositional variables, and atomic predicate formulas (predicate formulas of the form $P(x_1, \cdots, x_n)$, containing no connectives or quantifiers) are well-formed formulas, collectively called **atomic formulas**;
2. If $A$ is a well-formed formula, then so is $(\lnot A)$;
3. If $A$ and $B$ are well-formed formulas, the free variables of $A$ are not bound in $B$, and the free variables of $B$ are not bound in $A$, then $(A \land B)$, $(A \lor B)$, $(A \to B)$, and $(A \leftrightarrow B)$ are well-formed formulas (the outermost parentheses may be omitted);
4. If $A$ is a well-formed formula, then so are $(\forall x)A$ and $(\exists x)A$;
5. A string is a well-formed formula only if it is obtained by finitely many applications of rules 1–4.

## 4.4. Formalizing Natural-Language Sentences

The process of translating natural-language sentences into formulas of predicate logic is called formalization.

### 4.4.1. The Basic Method

1. Analyze the structure of the sentence and identify the individual terms, predicates, quantifiers, and logical relations;
2. Choose suitable predicate symbols and function symbols;
3. Combine them into a formula using quantifiers and connectives.

When an individual variable is quantified several times, the order and combination of the quantifiers determine the meaning of the formula. Quantifiers bind more tightly than connectives, and in a sequence of quantifiers the scope of each quantifier contains the quantifiers to its right:

$$
\begin{aligned}
(\forall x)(\forall y)P(x, y) & = (\forall x)((\forall y)P(x, y)) \\
(\forall x)(\exists y)P(x, y) & = (\forall x)((\exists y)P(x, y)) \\
(\exists x)(\forall y)P(x, y) & = (\exists x)((\forall y)P(x, y)) \\
(\exists x)(\exists y)P(x, y) & = (\exists x)((\exists y)P(x, y))
\end{aligned}
$$

Quantifiers of the same kind can be interchanged, for example $(\forall x)(\forall y)P(x, y) = (\forall y)(\forall x)P(x, y)$; but quantifiers of different kinds generally cannot, as interchanging them changes the meaning.

**Example** Let $P(x, y)$ mean "$x$ is a friend of $y$". Then $(\forall y)(\exists x)P(x, y)$ says "for every $y$ there is some $x$ who is a friend of $y$" (everyone has a friend), whereas $(\exists x)(\forall y)P(x, y)$ says "there is an $x$ who is a friend of every $y$" (someone is everybody's friend). The two have different meanings.

### 4.4.2. Key Principles and Examples

- The universal quantifier goes with implication: a sentence of the form "all … are …" is expressed as $(\forall x)(\cdots \to \cdots)$;
- The existential quantifier goes with conjunction: a sentence of the form "some … are …" is expressed as $(\exists x)(\cdots \land \cdots)$.

**Example** All rational numbers are real numbers. Let $P(x)$: $x$ is a rational number, and $Q(x)$: $x$ is a real number. The correct formalization is $(\forall x)(P(x) \to Q(x))$; $(\forall x)(P(x) \land Q(x))$ is wrong, since it says that everything is both a rational number and a real number.

**Example** Some real numbers are rational. The correct formalization is $(\exists x)(Q(x) \land P(x))$; $(\exists x)(Q(x) \to P(x))$ is wrong, since it is true as soon as there is any individual that is not a real number.

### 4.4.3. Characteristic Predicates and the Effect of the Domain

The symbolic expression of a proposition depends on the domain. When the domain is the universal domain, an additional predicate is needed to restrict the range of individuals under discussion.

**Definition 4.4.1 (Characteristic Predicate)** A predicate used to restrict the range of individuals under discussion is called a **characteristic predicate**.

Characteristic predicates are added as follows:

- after a universal quantifier, the characteristic predicate serves as the antecedent and is joined by **implication**;
- after an existential quantifier, the characteristic predicate is joined to the other predicates by **conjunction**.

**Example 4.4.1** All humans breathe (the domain is the universal domain). Let $M(x)$: $x$ is a human, and $F(x)$: $x$ breathes. The formalization is $(\forall x)(M(x) \to F(x))$.

**Example 4.4.2** Some people write with their left hand (the domain is the universal domain). Let $M(x)$: $x$ is a human, and $G(x)$: $x$ writes with the left hand. The formalization is $(\exists x)(M(x) \land G(x))$.

### 4.4.4. Other Common Patterns

- "No …": usually equivalent to "all … are not …";
- Uniqueness: first express existence, then express that every individual satisfying the condition is equal to it.

**Example 4.4.3** No irrational number is rational. Let $A(x)$: $x$ is an irrational number, and $B(x)$: $x$ is a rational number. The formalization is $\lnot (\exists x)(A(x) \land B(x))$, or equivalently $(\forall x)(A(x) \to \lnot B(x))$.

**Example 4.4.4** "There is a unique $x$ satisfying $P(x)$" is formalized as $(\exists x)\big(P(x) \land (\forall y)(P(y) \to x = y)\big)$.

### 4.4.5. A Formal Description of the Natural Numbers

In this section the domain is the set of natural numbers, and we formalize sentences describing basic properties of the natural numbers. These formulas can serve as axioms for the set of natural numbers. Let:

- the predicate $E(x, y)$ mean $x = y$;
- the function $f(x)$ denote the successor of $x$, that is, $f(x) = x + 1$;
- the function $g(x)$ denote the predecessor of $x$, that is, $g(x) = x - 1$.

**Example 4.4.5** Every number has exactly one successor.

"Exactly one" expresses existence and uniqueness: first assert that some $y$ is the successor of $x$, then assert that every individual $z$ that is a successor of $x$ equals this $y$. The formalization is

$$
(\forall x)(\exists y)\Big(E(y, f(x)) \land (\forall z)\big(E(z, f(x)) \to E(y, z)\big)\Big)
$$

That is: for every $x$ there is a $y$ equal to $f(x)$ ($y$ is the successor of $x$), and for every $z$, if $z$ also equals $f(x)$, then $y$ equals $z$.

**Example 4.4.6** There is no number whose successor is 0. That is, there is no number $x$ such that $0$ is the successor of $x$; the formalization is

$$
\lnot (\exists x)E(0, f(x)) \quad \text{or equivalently} \quad (\forall x)\lnot E(0, f(x))
$$

**Example 4.4.7** Every number other than 0 has exactly one predecessor. "Other than 0" can be written as "if $x \neq 0$, then …", and the rest has the same structure as Example 4.4.5. The formalization is

$$
(\forall x)\Big(\lnot E(x, 0) \to (\exists y)\Big(E(y, g(x)) \land (\forall z)\big(E(z, g(x)) \to E(y, z)\big)\Big)\Big)
$$

That is: for every $x$, if $x$ is not equal to 0, then there is a $y$ equal to $g(x)$ ($y$ is the predecessor of $x$), and for every $z$, if $z$ also equals $g(x)$, then $y$ equals $z$.

## 4.5. Formulas over Finite Domains

### 4.5.1. Universal and Existential Quantifiers over a Finite Domain

When the domain $D$ is a finite set $\{a_1, a_2, \cdots, a_k\}$, quantifiers can be converted into the **conjunction** and **disjunction** of propositional logic:

$$
\begin{aligned}
(\forall x)P(x) & = P(a_1) \land P(a_2) \land \cdots \land P(a_k) \\
(\exists x)P(x) & = P(a_1) \lor P(a_2) \lor \cdots \lor P(a_k)
\end{aligned}
$$

Thus the universal quantifier $\forall$ generalizes conjunction $\land$, and the existential quantifier $\exists$ generalizes disjunction $\lor$.

- Uses of finite domains: when a predicate formula is hard to understand, expanding it into a propositional formula over a small finite domain (such as $\{1, 2\}$) helps build intuition;
- Limitations of infinite domains: over an infinite domain, a predicate formula generally cannot be converted into a propositional formula.

## 4.6. Validity and the Decision Problem

An *interpretation* of a predicate formula consists of a nonempty domain, together with specific meanings for the individual constants, functions, and predicates in it, and values for the free variables.

### 4.6.1. Valid Formulas

**Definition 4.6.1 (Valid Formula)** A predicate formula $A$ that is true under every interpretation is called a **valid formula** (or universally valid formula).

**Example 4.6.1** $(\forall x)(P(x) \lor \lnot P(x))$ is valid (the law of excluded middle).

### 4.6.2. Unsatisfiable Formulas

**Definition 4.6.2 (Unsatisfiable Formula)** A predicate formula $A$ that is false under every interpretation is called an **unsatisfiable formula**, or a contradiction.

**Example 4.6.2** $(\exists x)(P(x) \land \lnot P(x))$ is unsatisfiable.

### 4.6.3. Satisfiable Formulas

**Definition 4.6.3 (Satisfiable Formula)** A predicate formula $A$ that is true under at least one interpretation is called a **satisfiable formula**.

Every valid formula is satisfiable, but a satisfiable formula need not be valid.

**Example 4.6.3** $(\exists x)P(x)$ is satisfiable (over any nonempty domain, let $P$ be true of some individual), but it is not valid.

### 4.6.4. Validity over Finite Domains

The validity and satisfiability of a formula may depend on the number of individuals in the domain.

**Property 4.6.1** Let $k \geq 1$.

- If a formula is valid (or satisfiable) over some domain with $k$ elements, then it is valid (or satisfiable) over every domain with $k$ elements;
- If a formula is valid over domains with $k$ elements, then it is also valid over domains with $k - 1$ elements ($k \geq 2$);
- If a formula is satisfiable over domains with $k$ elements, then it is also satisfiable over domains with $k + 1$ elements.

### 4.6.5. The Decision Problem for Predicate Logic

The *decision problem* for predicate logic asks, for an arbitrary given predicate formula, whether it is valid. Predicate logic would have the property of **decidability** if there were an *effective method*, that is, a mechanical procedure that terminates in finitely many steps, for deciding of every formula whether it is valid.

### 4.6.6. Results on the Decision Problem

**Theorem 4.6.1** First-order logic is undecidable: there is no effective method that decides, for every predicate formula, whether it is valid.

**Theorem 4.6.2** The following classes of formulas are decidable:

- formulas containing only unary predicate variables;
- formulas of the form $(\forall x_1)(\forall x_2)\cdots(\forall x_n)P(x_1, x_2, \cdots, x_n)$ and $(\exists x_1)(\exists x_2)\cdots(\exists x_n)P(x_1, x_2, \cdots, x_n)$, where $P$ contains no quantifiers and no other free variables;
- predicate formulas over a finite domain (which can be decided by enumerating all interpretations).
