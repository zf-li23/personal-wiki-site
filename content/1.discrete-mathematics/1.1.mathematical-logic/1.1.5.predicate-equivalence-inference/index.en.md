---
title: Equivalence and Inference in Predicate Logic
source_hash: c171bbb512c5
---

Much of this chapter can be learned by analogy with propositional logic: the notions of equivalence, normal forms, rules of inference, and resolution are all carried over from [1.1.2](/1.1.2), and what is new is how to handle quantifiers. For the same reason, this chapter also serves as a review of propositional logic.

## 5.1. Equivalences

### 5.1.1. Definition of Equivalence

Equivalence in predicate logic is based on validity (Definition 4.6.1).

**Definition 5.1.1 (Logical Equivalence)** Let $A$ and $B$ be formulas of first-order logic. If $A \leftrightarrow B$ is a **valid formula**, then $A$ and $B$ are said to be **logically equivalent**, written $A = B$ or $A \Leftrightarrow B$.

### 5.1.2. Quantifier Negation Laws

The quantifier negation laws describe how a quantifier and a negation sign can change places. They are among the most basic equivalence transformations of predicate logic and express **De Morgan's laws** for quantifiers and negation.

**Formula 5.1.1 (Quantifier Negation Laws)**

$$
\begin{aligned}
\lnot (\forall x)P(x) & = (\exists x)\lnot P(x) \\
\lnot (\exists x)P(x) & = (\forall x)\lnot P(x)
\end{aligned}
$$

The two formulas are duals of each other. Their meaning is intuitive: "not every individual satisfies $P$" is equivalent to "some individual does not satisfy $P$", and "no individual satisfies $P$" is equivalent to "every individual fails to satisfy $P$".

Expanding over a finite domain $\{a_1, a_2, \cdots, a_n\}$ ([Section 4.5](/1.1.4#sec-4.5)) shows that the first equivalence is just De Morgan's law of propositional logic:

$$
\begin{aligned}
\lnot (\forall x)P(x) & = \lnot (P(a_1) \land P(a_2) \land \cdots \land P(a_n)) \\
& = \lnot P(a_1) \lor \lnot P(a_2) \lor \cdots \lor \lnot P(a_n) \\
& = (\exists x)\lnot P(x)
\end{aligned}
$$

**Example 5.1.1** "Not all animals are cats." Let $A(x)$: $x$ is an animal, and $B(x)$: $x$ is a cat. The sentence is $\lnot (\forall x)(A(x) \to B(x))$. By the quantifier negation laws,

$$
\begin{aligned}
\lnot (\forall x)(A(x) \to B(x)) & = (\exists x)\lnot (A(x) \to B(x)) \\
& = (\exists x)\lnot (\lnot A(x) \lor B(x)) \\
& = (\exists x)(A(x) \land \lnot B(x))
\end{aligned}
$$

The transformed formula says "there is something that is an animal but not a cat", which agrees with the original sentence.

## 5.2. Quantifier Distribution Laws

The quantifier distribution laws describe how quantifiers distribute over the connectives. They are key tools for transforming and simplifying predicate formulas.

### 5.2.1. Distribution over Disjunction and Conjunction

When the formula in the scope of a quantifier contains a propositional variable unrelated to the quantified variable, the quantifier can be "pulled out".

**Formula 5.2.1** Let $q$ be a propositional variable not involving the individual variable $x$. Then

$$
\begin{aligned}
(\forall x)(P(x) \lor q) & = (\forall x)P(x) \lor q \\
(\exists x)(P(x) \lor q) & = (\exists x)P(x) \lor q \\
(\forall x)(P(x) \land q) & = (\forall x)P(x) \land q \\
(\exists x)(P(x) \land q) & = (\exists x)P(x) \land q
\end{aligned}
$$

More generally, $q$ may be replaced by any formula in which $x$ has no free occurrence. The same applies to $p, q$ in the remaining formulas of this section.

### 5.2.2. Distribution over Implication

Distribution over implication is special: it matters whether the variable occurs in the antecedent or in the consequent.

**Formula 5.2.2** Let $p, q$ be propositional variables not involving the individual variable $x$. Then

$$
\begin{aligned}
(\forall x)(P(x) \to q) & = (\exists x)P(x) \to q \\
(\exists x)(P(x) \to q) & = (\forall x)P(x) \to q \\
(\forall x)(p \to Q(x)) & = p \to (\forall x)Q(x) \\
(\exists x)(p \to Q(x)) & = p \to (\exists x)Q(x)
\end{aligned}
$$

The pattern is this: when a quantifier applies to a whole implication, if $x$ occurs only in the antecedent, the quantifier switches type when distributed (universal becomes existential, and existential becomes universal); if $x$ occurs only in the consequent, the quantifier stays the same. The reason is that $P(x) \to q = \lnot P(x) \lor q$, so the antecedent carries a hidden negation.

### 5.2.3. Universal over Conjunction, Existential over Disjunction

When both predicates contain the quantified variable, the universal quantifier distributes over conjunction and the existential quantifier distributes over disjunction.

**Formula 5.2.3**

$$
\begin{aligned}
(\forall x)(P(x) \land Q(x)) & = (\forall x)P(x) \land (\forall x)Q(x) \\
(\exists x)(P(x) \lor Q(x)) & = (\exists x)P(x) \lor (\exists x)Q(x)
\end{aligned}
$$

### 5.2.4. Cases with Implication Only

Conversely, distributing the universal quantifier over disjunction, or the existential quantifier over conjunction, does not give an equivalence, only an implication:

**Formula 5.2.4**

$$
\begin{aligned}
(\forall x)P(x) \lor (\forall x)Q(x) & \Rightarrow (\forall x)(P(x) \lor Q(x)) \\
(\exists x)(P(x) \land Q(x)) & \Rightarrow (\exists x)P(x) \land (\exists x)Q(x)
\end{aligned}
$$

**Example 5.2.1** Let the domain be all people, $P(x)$: $x$ is an honors student, and $Q(x)$: $x$ is an athlete. $(\forall x)(P(x) \lor Q(x))$ says "everyone is either an honors student or an athlete"; $(\forall x)P(x) \lor (\forall x)Q(x)$ says "either everyone is an honors student, or everyone is an athlete". The truth of the former does not imply the truth of the latter: some people may be honors students and the others athletes.

### 5.2.5. Renaming and Distribution of Several Quantifiers

By renaming variables, quantifiers involving different individual variables can be merged or regrouped.

**Formula 5.2.5**

$$
\begin{aligned}
(\forall x)(\forall y)(P(x) \lor Q(y)) & = (\forall x)P(x) \lor (\forall x)Q(x) \\
(\exists x)(\exists y)(P(x) \land Q(y)) & = (\exists x)P(x) \land (\exists x)Q(x)
\end{aligned}
$$

## 5.3. Normal Forms

Normal forms are standard forms of predicate formulas; they are important for the **decision problem** and for theorem proving, resolution in particular.

### 5.3.1. Prenex Normal Form

**Definition 5.3.1 (Prenex Normal Form)** Let $A$ be a formula of first-order logic. If all quantifiers of $A$ stand at the far left of the formula, none of them is preceded by a negation sign, and their **scopes** all extend to the end of the formula, then $A$ is said to be in **prenex normal form**. The general form of a prenex normal form is

$$
(Q_1 x_1)(Q_2 x_2) \cdots (Q_n x_n) M(x_1, x_2, \cdots, x_n)
$$

where each $Q_i$ ($1 \leq i \leq n$) is $\forall$ or $\exists$, and $M$ is a quantifier-free formula called the **matrix** of the formula.

**Theorem 5.3.1 (Prenex Normal Form Theorem)** Every formula of first-order logic is equivalent to some formula in prenex normal form.

Prenex normal forms are not unique: the order of the quantifiers and equivalent transformations of the matrix can both lead to different forms.

### 5.3.2. Converting to Prenex Normal Form

A formula can be converted to prenex normal form by the following mechanical steps:

1. Eliminate connectives: use $A \to B = \lnot A \lor B$ and $A \leftrightarrow B = (A \to B) \land (B \to A)$ to remove $\to$ and $\leftrightarrow$ from the formula;
2. Move negations inward: use the quantifier negation laws (Formula 5.1.1) and **De Morgan's laws** to move negation signs down to the atomic predicate formulas;
3. Rename variables: use **renaming of bound variables** so that variables bound by different quantifiers have different names, distinct also from the free variables, to avoid confusion; renaming bound variables does not change the meaning of a formula;
4. Move quantifiers to the left: use the quantifier distribution laws ([Section 5.2](#sec-5.2)) to move the quantifiers one by one to the far left of the formula.

**Example 5.3.1** Find a prenex normal form of $\lnot \big((\forall x)(\exists y)P(a, x, y) \to (\exists x)(\lnot (\forall y)Q(y, b) \to R(x))\big)$.

$$
\begin{aligned}
& \lnot \big((\forall x)(\exists y)P(a, x, y) \to (\exists x)(\lnot (\forall y)Q(y, b) \to R(x))\big) \\
={} & (\forall x)(\exists y)P(a, x, y) \land \lnot (\exists x)(\lnot (\forall y)Q(y, b) \to R(x)) \\
={} & (\forall x)(\exists y)P(a, x, y) \land (\forall x)\big(\lnot (\forall y)Q(y, b) \land \lnot R(x)\big) \\
={} & (\forall x)(\exists y)P(a, x, y) \land (\forall x)\big((\exists y)\lnot Q(y, b) \land \lnot R(x)\big) \\
={} & (\forall x)\big((\exists y)P(a, x, y) \land (\exists z)\lnot Q(z, b) \land \lnot R(x)\big) \\
={} & (\forall x)(\exists y)(\exists z)\big(P(a, x, y) \land \lnot Q(z, b) \land \lnot R(x)\big)
\end{aligned}
$$

The steps use, in order: $\lnot (A \to B) = A \land \lnot B$; the quantifier negation laws together with $\lnot (A \to B) = A \land \lnot B$; the quantifier negation laws; distribution of the universal quantifier over conjunction (Formula 5.2.3), renaming the second $y$ to $z$; and moving the quantifiers to the left (Formula 5.2.1).

### 5.3.3. Skolem Normal Form

Prenex normal forms provide the basis for further standardization. The two most important refinements are the prenex form containing only universal quantifiers and the prenex form in which all existential quantifiers precede all universal quantifiers; they play special roles in deciding unsatisfiability and validity, respectively.

**Definition 5.3.2 (Skolem Normal Form)** Starting from a prenex normal form of a formula $A$ of first-order logic, the formula obtained by placing all existential quantifiers to the left of all universal quantifiers, or by keeping only the universal quantifiers and eliminating the existential ones, is called a **Skolem normal form** of $A$.

A formula $A$ and its Skolem normal form are in general not equivalent; they agree only in a certain sense (see [Section 5.3.4](#sec-5.3.4) and [Section 5.3.5](#sec-5.3.5) below).

The key to eliminating existential quantifiers is:

- *Skolem constants*: if an existential quantifier is not preceded by any universal quantifier, replace the variable it binds by a new constant. For example, $(\exists y)P(y)$ becomes $P(c)$;
- *Skolem functions*: if an existential quantifier is preceded by universal quantifiers, replace the variable it binds by a new function $f(x_1, \cdots, x_n)$ of these universally quantified variables. For example, $(\forall x)(\exists y)P(x, y)$ becomes $(\forall x)P(x, f(x))$.

**Example 5.3.2** Find the Skolem normal form, containing only universal quantifiers, of $(\exists x)(\forall y)(\forall z)(\exists u)(\forall v)(\exists w)P(x, y, z, u, v, w)$.

1. Eliminate $(\exists x)$: it is not preceded by any universal quantifier, so replace $x$ by a constant $a$;
2. Eliminate $(\exists u)$: it is preceded by $(\forall y)(\forall z)$, so replace $u$ by a function $f(y, z)$;
3. Eliminate $(\exists w)$: it is preceded by $(\forall y)(\forall z)(\forall v)$, so replace $w$ by a function $g(y, z, v)$.

The result is $(\forall y)(\forall z)(\forall v)P(a, y, z, f(y, z), v, g(y, z, v))$.

### 5.3.4. $\exists$-Prenex Normal Form

**Definition 5.3.3 ($\exists$-Prenex Normal Form)** A prenex normal form of the shape $(\exists x_1)\cdots(\exists x_i)(\forall x_{i+1})\cdots(\forall x_n)M$, that is, one in which all existential quantifiers precede all universal quantifiers and there is at least one existential quantifier, is called an **$\exists$-prenex normal form**.

**Theorem 5.3.2** Every formula $A$ of first-order logic can be converted into a corresponding $\exists$-prenex normal form, and $A$ is valid if and only if its $\exists$-prenex normal form is valid.

### 5.3.5. $\forall$-Prenex Normal Form

**Definition 5.3.4 ($\forall$-Prenex Normal Form)** A prenex normal form containing only universal quantifiers is called a **$\forall$-prenex normal form**. It can be obtained by eliminating the existential quantifiers through the introduction of Skolem constants and Skolem functions.

**Theorem 5.3.3** Every formula $A$ of first-order logic can be converted into a corresponding $\forall$-prenex normal form, and $A$ is unsatisfiable if and only if its $\forall$-prenex normal form is unsatisfiable.

A formula is in general not equivalent to its $\forall$-prenex normal form, but the two agree with respect to unsatisfiability, which is exactly what resolution ([Section 5.6](#sec-5.6)) needs.

## 5.4. Basic Inference Formulas

In first-order logic, the form of inference from premises $A_1, A_2, \cdots, A_n$ to a conclusion $B$ is $A_1 \land A_2 \land \cdots \land A_n \to B$. If it is valid, the inference is said to be correct, and we write $A_1 \land A_2 \land \cdots \land A_n \Rightarrow B$. The basic inference formulas are certain valid implications that underlie the inference calculus of predicate logic.

Besides the inference formulas of propositional logic ([1.1.2](/1.1.2#sec-2.8)), predicate logic has the following basic inference formulas:

| No. | Inference | Remark |
| :-: | :-- | :-- |
| 1 | $(\forall x)P(x) \lor (\forall x)Q(x) \Rightarrow (\forall x)(P(x) \lor Q(x))$ | Formula 5.2.4 |
| 2 | $(\exists x)(P(x) \land Q(x)) \Rightarrow (\exists x)P(x) \land (\exists x)Q(x)$ | Formula 5.2.4 |
| 3 | $(\forall x)(P(x) \to Q(x)) \Rightarrow (\forall x)P(x) \to (\forall x)Q(x)$ | |
| 4 | $(\forall x)(P(x) \to Q(x)) \Rightarrow (\exists x)P(x) \to (\exists x)Q(x)$ | |
| 5 | $(\forall x)(P(x) \leftrightarrow Q(x)) \Rightarrow (\forall x)P(x) \leftrightarrow (\forall x)Q(x)$ | |
| 6 | $(\forall x)(P(x) \leftrightarrow Q(x)) \Rightarrow (\exists x)P(x) \leftrightarrow (\exists x)Q(x)$ | |
| 7 | $(\forall x)(P(x) \to Q(x)) \land (\forall x)(Q(x) \to R(x)) \Rightarrow (\forall x)(P(x) \to R(x))$ | Syllogism in predicate logic |
| 8 | $(\forall x)(P(x) \to Q(x)) \land P(a) \Rightarrow Q(a)$ | Universal instantiation |
| 9 | $(\forall x)(\forall y)P(x, y) \Rightarrow (\exists x)(\forall y)P(x, y)$ | |
| 10 | $(\exists x)(\forall y)P(x, y) \Rightarrow (\forall y)(\exists x)P(x, y)$ | The converse fails |

**Remark 5.4.1** The converse of No. 10 does not hold. $(\forall y)(\exists x)P(x, y)$ says "for every $y$ there is an $x$ such that $P(x, y)$", and this $x$ may depend on $y$ (different $y$ may have different $x$); $(\exists x)(\forall y)P(x, y)$ says "there is an $x$ such that $P(x, y)$ holds for all $y$", and this $x$ is one and the same for all $y$. Clearly the latter is stronger than the former.

## 5.5. Inference Calculus

Every **rule of inference** of propositional logic ([1.1.2](/1.1.2#sec-2.9)) remains available in predicate logic; the inference calculus of predicate logic adds rules for handling quantifiers, yielding a workable system of formal derivation.

### 5.5.1. Quantifier Rules

The quantifier rules are the core of the inference calculus of predicate logic. There are four of them:

| Rule | Form | Conditions |
| :-- | :-- | :-- |
| Universal instantiation (UI) | $\dfrac{(\forall x)P(x)}{P(y)}$ or $\dfrac{(\forall x)P(x)}{P(c)}$ | $y$ is any individual variable that does not occur bound in $P(x)$, and $c$ is any individual constant; all free occurrences of $x$ must be replaced |
| Universal generalization (UG) | $\dfrac{P(y)}{(\forall x)P(x)}$ | $P(y)$ is true for every individual $y$ in the domain; $x$ does not occur bound in $P(y)$ |
| Existential instantiation (EI) | $\dfrac{(\exists x)P(x)}{P(c)}$ | $c$ is a specific individual constant for which $P$ is true, and it is new (it has not appeared earlier in the proof and does not occur in $P(x)$); $P(x)$ contains no other free individual variables |
| Existential generalization (EG) | $\dfrac{P(c)}{(\exists x)P(x)}$ | $c$ is a specific individual constant; $x$ does not occur in $P(c)$ |

UI and EI remove a quantifier ("instantiation"); UG and EG introduce one ("generalization").

**Remark 5.5.1** In UI, the variable $y$ replacing $x$ must not be a variable already bound in $P(x)$; otherwise errors arise. For example, $(\forall x)(\exists y)(x < y)$ is true over the reals, but replacing $x$ by $y$ would wrongly yield $(\exists y)(y < y)$, which is false over the reals. The reason is that the $y$ used to replace $x$ is already bound by $\exists y$ in $P(x) = (\exists y)(x < y)$.

**Remark 5.5.2** EI requires $c$ to be a new constant and $P(x)$ to contain no other free variables; otherwise $c$ might depend on those variables, or be confused with individuals already in use.

### 5.5.2. The General Procedure

1. Formalize: symbolize the natural-language premises and conclusion as predicate formulas;
2. Remove quantifiers: use UI and EI to eliminate the quantifiers in the premises, obtaining propositions or formulas with only free variables;
3. Reason propositionally: with no quantifiers present, derive results using the rules of inference and inference formulas of propositional logic;
4. Introduce quantifiers: use UG and EG to attach the required quantifiers to the intermediate or final conclusions.

**Example 5.5.1** Prove the syllogism "All men are mortal; Socrates is a man; therefore Socrates is mortal."

Let $P(x)$: $x$ is a man, $Q(x)$: $x$ is mortal, and $s$: Socrates. We must prove $(\forall x)(P(x) \to Q(x)) \land P(s) \Rightarrow Q(s)$.

**Proof**

| Step | Formula | Justification |
| :-: | :-- | :-- |
| 1 | $(\forall x)(P(x) \to Q(x))$ | Premise |
| 2 | $P(s) \to Q(s)$ | 1, UI (replace $x$ by $s$) |
| 3 | $P(s)$ | Premise |
| 4 | $Q(s)$ | 2, 3, modus ponens |

$\square$

## 5.6. Resolution in Predicate Logic

Resolution is a method suited to automated theorem proving by machine; it extends the **resolution** of propositional logic ([1.1.2](/1.1.2#sec-2.10)) to predicate logic.

### 5.6.1. The Basic Idea

Proving $A_1 \land A_2 \land \cdots \land A_n \Rightarrow B$ is equivalent to proving that $G = A_1 \land A_2 \land \cdots \land A_n \land \lnot B$ is an **unsatisfiable formula**. Resolution establishes the unsatisfiability of $G$ by deriving the empty clause $\square$.

### 5.6.2. The Steps of Resolution

**Algorithm 5.6.1 (Resolution in Predicate Logic)**

1. Form the formula $G = A_1 \land A_2 \land \cdots \land A_n \land \lnot B$;
2. Convert to Skolem normal form: first bring $G$ into prenex normal form, then eliminate all existential quantifiers to obtain a $\forall$-prenex normal form $G^*$, and convert its matrix into **conjunctive normal form**. By Theorem 5.3.3, $G$ and $G^*$ agree with respect to unsatisfiability;
3. Form the clause set: drop all universal quantifiers of $G^*$ (all variables in the formula are now implicitly universally quantified), and collect the conjuncts of the matrix (the **clauses**, that is, simple disjunctions) into a clause set $S$;
4. Derive by resolution: resolve clauses in $S$, add the **resolvents** to $S$, and repeat until the empty clause $\square$ is produced. The empty clause represents a contradiction, and the proof is complete.

Resolution in predicate logic requires *unification*: finding a substitution (such as $\{x / a\}$) that turns some pair of literals in two clauses into a complementary pair; this pair is then eliminated and the remaining parts are joined by disjunction to give the resolvent.

**Example 5.6.1** Let $C_1 = P(x) \lor Q(x)$ and $C_2 = \lnot P(a) \lor R(y)$. After applying the substitution $\{x / a\}$ to $C_1$, $P(a)$ and $\lnot P(a)$ form a complementary pair, and resolution yields $Q(a) \lor R(y)$.

The heart of resolution in predicate logic is the handling of atomic formulas containing variables: unification finds a substitution that makes atomic formulas complementary, and then the resolution rule is applied. This lets resolution handle inferences involving quantifiers and lays the foundation for automated theorem proving. Resolution in predicate logic is complete: if $G$ is unsatisfiable, the empty clause can always be derived in finitely many steps; but if $G$ is satisfiable, the process may never terminate. This is consistent with the undecidability of first-order logic (Theorem 4.6.1).

## Summary

| Topic | Key results |
| :-- | :-- |
| Logical equivalence (Definition 5.1.1) | $A \leftrightarrow B$ is valid, written $A = B$ |
| Quantifier negation laws (Formula 5.1.1) | $\lnot (\forall x)P(x) = (\exists x)\lnot P(x)$, $\lnot (\exists x)P(x) = (\forall x)\lnot P(x)$ |
| Extending and shrinking the scope (Formulas 5.2.1 and 5.2.2) | A part not involving $x$ can be moved out of the quantifier; if $x$ occurs only in the antecedent of an implication, the quantifier flips when moved |
| Distribution of quantifiers (Formulas 5.2.3 and 5.2.4) | $\forall$ distributes over $\land$ and $\exists$ over $\lor$; for $\forall$ over $\lor$ and $\exists$ over $\land$ only a one-way implication holds |
| Prenex normal form (Definition 5.3.1, Theorem 5.3.1) | Every formula has an equivalent prenex normal form: eliminate $\to, \leftrightarrow$, move negations inward, rename variables if needed, then move the quantifiers to the far left |
| Skolem normal forms (Definitions 5.3.2–5.3.4) | The $\exists$-prenex normal form preserves validity (Theorem 5.3.2) and the $\forall$-prenex normal form preserves unsatisfiability (Theorem 5.3.3), but neither is equivalent to the original formula |
| Inference (Sections 5.4 and 5.5) | Basic inference formulas plus the four quantifier rules UI, UG, EI, EG: remove quantifiers, reason propositionally, then reintroduce quantifiers |
| Resolution (Algorithm 5.6.1) | Convert the premises and the negated conclusion into a clause set of a $\forall$-prenex normal form and resolve using unification; an unsatisfiable set always yields the empty clause, while for a satisfiable one the process may not terminate |
