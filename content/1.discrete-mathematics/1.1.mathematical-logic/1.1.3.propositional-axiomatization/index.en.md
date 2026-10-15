---
title: Axiomatization of Propositional Logic
source_hash: 9f5826efc8d6
---

What is the most economical way to present a formal science? Euclid's *Elements* perhaps offers one answer: Book I opens with 23 definitions, 5 postulates, and 5 common notions, and every book that follows is filled with propositions, each of which can be proved from the axioms and the propositions before it. This is an axiomatic deductive system. An axiomatic system of logic must discard every notion that is not made explicit, truth values included, and prescribe only the derivability relations between strings of symbols. So let us now forget all the equivalence laws and rules of inference of the previous two chapters and enter a universe defined by Russell's axiom system alone. At the end we present another system, better suited to computers: Wang's algorithm.

## 3.1. The Structure of an Axiomatic System

**Definition 3.1.1 (Axiomatic System)** An **axiomatic system** consists of the following components:

1. Primitive symbols: the set of all symbols allowed in the system;
2. Formation rules: rules for building legitimate sequences of symbols (formulas) from the primitive symbols;
3. *Axioms*: carefully chosen, most basic formulas (tautologies, in propositional logic) that serve as the basis for deriving all other theorems;
4. Transformation rules: the rules of inference prescribed by the system;
5. Theorems: the formulas derived from the axioms by the transformation rules, together with their proofs.

## 3.2. Russell's Axiom System

We now define Russell's axiom system for propositional logic. First, certain formulas are stipulated to be tautologies; these are the axioms. Then a few rules are used to generate further tautologies, the theorems. It is rather as if God first declared "through two distinct points one, and only one, straight line can be drawn …" to be true, and after enough such pronouncements, mortals could see for themselves that "the angles of a triangle sum to 180 degrees" is true as well.

### 3.2.1. Primitive Symbols

- Propositional variables: uppercase letters $P, Q, R, \cdots$;
- Connectives: $\lnot, \lor$;
- Parentheses: $($ and $)$;
- The assertion sign: $\vdash$.

The assertion sign is written before a formula to indicate that the formula is a theorem (a tautology) of the system. $\vdash A$ is like "God said: '$A$!'"

### 3.2.2. Formation Rules

1. Every propositional variable is a well-formed formula;
2. If $A$ and $B$ are well-formed formulas, then $(A \lor B)$ is a well-formed formula;
3. If $A$ is a well-formed formula, then $\lnot A$ is a well-formed formula;
4. A string is a well-formed formula only if it is obtained by finitely many applications of the rules above.

### 3.2.3. Definitions

The system has only two connectives, $\lnot$ and $\lor$. They already form a **functionally complete set** (Theorem 2.4.1; but since this axiomatic system starts from scratch, in principle we do not yet know this inside the system). The other connectives can be defined as abbreviations, which makes formulas easier to write:

**Definition 3.2.1** $A \to B$ is defined as $\lnot A \lor B$.

**Definition 3.2.2** $A \land B$ is defined as $\lnot (\lnot A \lor \lnot B)$.

**Definition 3.2.3** $A \leftrightarrow B$ is defined as $(A \to B) \land (B \to A)$.

### 3.2.4. Axioms

| Axiom | Formula | Name |
| :-: | :-- | :-- |
| 1 | $\vdash (P \lor P) \to P$ | Tautology |
| 2 | $\vdash P \to (P \lor Q)$ | $\lor$-introduction |
| 3 | $\vdash (P \lor Q) \to (Q \lor P)$ | Commutativity of disjunction |
| 4 | $\vdash (Q \to R) \to ((P \lor Q) \to (P \lor R))$ | No. 15 of the [basic inference formulas](/1.1.2#sec-2.8) |

These formulas are theorems of the system by stipulation, but intuitively we can also see that they are tautologies. The question is: among so many tautologies, why choose these four as axioms? The most important reason, of course, is that there are few of them. Yet four is not the minimum, since there are axiom systems for propositional logic with only three axioms; so the choice was probably also influenced by how conveniently other important tautologies can be derived from them.

### 3.2.5. Transformation Rules

These rules are all old acquaintances; we met each of them among the rules of inference in [1.1.2](/1.1.2#sec-2.9):

- The **substitution rule**: if $\vdash A$, then $\vdash A\dfrac{\pi}{B}$, where $\pi$ is a propositional variable in $A$, $B$ is any well-formed formula, and every occurrence of $\pi$ must be replaced;
- The **replacement rule**: the two sides of Definitions 3.2.1–3.2.3 may replace each other;
- **Modus ponens**: if $\vdash A$ and $\vdash A \to B$, then $\vdash B$.

### 3.2.6. Theorems

A proof of a theorem must rest on the axioms or on previously proved theorems, and each step of the proof (each transformation of symbols) must follow a transformation rule. Let us begin!

**Theorem 3.2.1** $\vdash (Q \to R) \to ((P \to Q) \to (P \to R))$.

**Theorem 3.2.2** $\vdash P \to P$.

**Theorem 3.2.3** $\vdash P \lor \lnot P$.

**Theorem 3.2.4** $\vdash P \to \lnot \lnot P$.

**Proof** In the derivation below, line 3 is Theorem 3.2.1, line 9 is Theorem 3.2.2, line 13 is Theorem 3.2.3, and line 15 is Theorem 3.2.4.

| Step | Formula | Justification |
| :-: | :-- | :-- |
| 1 | $\vdash (Q \to R) \to ((P \lor Q) \to (P \lor R))$ | Axiom 4 |
| 2 | $\vdash (Q \to R) \to ((\lnot P \lor Q) \to (\lnot P \lor R))$ | 1, substitution $\dfrac{P}{\lnot P}$ |
| 3 | $\vdash (Q \to R) \to ((P \to Q) \to (P \to R))$ | 2, replacement by Definition 3.2.1 |
| 4 | $\vdash P \to (P \lor Q)$ | Axiom 2 |
| 5 | $\vdash P \to (P \lor P)$ | 4, substitution $\dfrac{Q}{P}$ |
| 6 | $\vdash (P \lor P) \to P$ | Axiom 1 |
| 7 | $\vdash ((P \lor P) \to P) \to ((P \to (P \lor P)) \to (P \to P))$ | 3, substitution $\dfrac{Q}{P \lor P}, \dfrac{R}{P}$ |
| 8 | $\vdash (P \to (P \lor P)) \to (P \to P)$ | 6, 7, modus ponens |
| 9 | $\vdash P \to P$ | 5, 8, modus ponens |
| 10 | $\vdash \lnot P \lor P$ | 9, replacement by Definition 3.2.1 |
| 11 | $\vdash (P \lor Q) \to (Q \lor P)$ | Axiom 3 |
| 12 | $\vdash (\lnot P \lor P) \to (P \lor \lnot P)$ | 11, substitution $\dfrac{P}{\lnot P}, \dfrac{Q}{P}$ |
| 13 | $\vdash P \lor \lnot P$ | 10, 12, modus ponens |
| 14 | $\vdash \lnot P \lor \lnot \lnot P$ | 13, substitution $\dfrac{P}{\lnot P}$ |
| 15 | $\vdash P \to \lnot \lnot P$ | 14, replacement by Definition 3.2.1 |

$\square$

As we can see, proofs in Russell's axiom system are quite laborious. Given an arbitrary tautology and asked to prove it in Russell's system, one would likely need real inspiration and time; an exam on this material would probably supply some already proved theorems to work with.

At this point some questions naturally arise. Can Russell's axiom system derive every tautology? And if we keep deriving formulas without the help of truth tables, could some step suddenly produce a formula that is not a tautology? Fortunately, Russell's axiom system is both sound and complete.

## 3.3. Completeness of the Axiomatic System and the Deduction Theorem

This section states results only, without proofs.

**Definition 3.3.1 (Soundness and Completeness)** An axiomatic system is called **sound** if every theorem of it is a tautology, and (semantically) **complete** if every tautology is a theorem of it.

**Definition 3.3.2 (Consistency)** An axiomatic system is called **consistent** if there is no formula $A$ such that both $\vdash A$ and $\vdash \lnot A$.

**Theorem 3.3.1** Russell's axiom system is sound, consistent, and complete: a formula is a theorem of the system if and only if it is a tautology.

Whether a given formula is a tautology can always be decided in finitely many steps by a truth table; hence the propositional calculus has the property of *decidability*.

**Theorem 3.3.2 (Deduction Theorem)** Let $\Gamma$ be a set of formulas. If $B$ can be derived from the formulas in $\Gamma$ together with $A$ as premises (without applying the substitution rule to the premises), written $\Gamma, A \vdash B$, then $\Gamma \vdash A \to B$.

The *deduction theorem* is the counterpart, within the axiomatic system, of the **conditional proof** rule of 1.1.2, and it can greatly simplify proofs in the axiomatic system. Besides Russell's axiom system, there are other axiomatic systems with these properties.

## 3.4. Wang Hao's Algorithm

> Author's note: I am not very interested in Wang's algorithm, and it strays rather far from the main line of logic, so the summary in this section was prepared with the help of AI tools. Please read it critically.

*Wang's algorithm* is another formal system for propositional logic, one that makes theorem proving automatic and is better suited to computer implementation. It has only one axiom, but uses the five common connectives directly; it defines sequents, together with five left rules and five right rules, ten transformation rules in all.

### 3.4.1. The Basic Idea

Write the theorem to be proved as a sequent, then apply the transformation rules repeatedly, eliminating one connective at a time, until one or more sequents without connectives are obtained. If all the connective-free sequents are axioms, the theorem is proved; otherwise it is not a theorem.

### 3.4.2. Sequents

**Definition 3.4.1 (Sequent)** Let $\alpha = A_1, \cdots, A_m$ and $\beta = B_1, \cdots, B_n$ be lists of formulas (finite sequences of formulas, possibly empty). Then $\alpha \Rightarrow \beta$ is called a **sequent**; $\alpha$ is called its **antecedent** and $\beta$ its **succedent**.

The sequent $\alpha \Rightarrow \beta$ means: whenever all the formulas in $\alpha$ are true, at least one formula in $\beta$ is true. In other words, the formulas of the antecedent are joined by conjunction and those of the succedent by disjunction:

$$
\bigwedge_{i=1}^{m} A_i \Rightarrow \bigvee_{j=1}^{n} B_j
$$

By convention, an empty antecedent is true and an empty succedent is false. The $\Rightarrow$ here is the same symbol as for tautological implication (Definition 2.7.1), and its meaning agrees: a sequent holds if and only if $\bigwedge_i A_i \to \bigvee_j B_j$ is a tautology.

### 3.4.3. The Axiom

Wang's algorithm has a single axiom: if the lists $\alpha$ and $\beta$ consist of propositional variables only, then $\alpha \Rightarrow \beta$ is an axiom if and only if $\alpha$ and $\beta$ have at least one propositional variable in common.

### 3.4.4. Transformation Rules

The transformation rules are divided into left rules (for the antecedent) and right rules (for the succedent), and each rule eliminates one connective. Below, $\alpha, \beta, \gamma$ are lists of formulas and $X, Y$ are formulas; "if … then …" means that the lower sequent can be obtained from the upper sequent (or sequents).

The left rules are:

| Rule | If | Then |
| :-- | :-- | :-- |
| $\lnot \Rightarrow$ | $\alpha, \beta \Rightarrow X, \gamma$ | $\alpha, \lnot X, \beta \Rightarrow \gamma$ |
| $\land \Rightarrow$ | $X, Y, \alpha, \beta \Rightarrow \gamma$ | $\alpha, X \land Y, \beta \Rightarrow \gamma$ |
| $\lor \Rightarrow$ | $X, \alpha, \beta \Rightarrow \gamma$ and $Y, \alpha, \beta \Rightarrow \gamma$ | $\alpha, X \lor Y, \beta \Rightarrow \gamma$ |
| $\to \Rightarrow$ | $Y, \alpha, \beta \Rightarrow \gamma$ and $\alpha, \beta \Rightarrow X, \gamma$ | $\alpha, X \to Y, \beta \Rightarrow \gamma$ |
| $\leftrightarrow \Rightarrow$ | $X, Y, \alpha, \beta \Rightarrow \gamma$ and $\alpha, \beta \Rightarrow X, Y, \gamma$ | $\alpha, X \leftrightarrow Y, \beta \Rightarrow \gamma$ |

The right rules are:

| Rule | If | Then |
| :-- | :-- | :-- |
| $\Rightarrow \lnot$ | $X, \alpha \Rightarrow \beta, \gamma$ | $\alpha \Rightarrow \beta, \lnot X, \gamma$ |
| $\Rightarrow \land$ | $\alpha \Rightarrow X, \beta, \gamma$ and $\alpha \Rightarrow Y, \beta, \gamma$ | $\alpha \Rightarrow \beta, X \land Y, \gamma$ |
| $\Rightarrow \lor$ | $\alpha \Rightarrow X, Y, \beta, \gamma$ | $\alpha \Rightarrow \beta, X \lor Y, \gamma$ |
| $\Rightarrow \to$ | $X, \alpha \Rightarrow Y, \beta, \gamma$ | $\alpha \Rightarrow \beta, X \to Y, \gamma$ |
| $\Rightarrow \leftrightarrow$ | $X, \alpha \Rightarrow Y, \beta, \gamma$ and $Y, \alpha \Rightarrow X, \beta, \gamma$ | $\alpha \Rightarrow \beta, X \leftrightarrow Y, \gamma$ |

These rules can be understood from the meaning of a sequent. For example, $\lnot X$ being true in the antecedent means that $X$ is false, so $X$ can be moved to the succedent; $X \to Y$ being true in the antecedent means that "$Y$ is true" or "$X$ is false", so the proof splits into two cases.

### 3.4.5. The Proof Procedure

**Algorithm 3.4.1 (Wang Hao's Algorithm)**

1. Write a sequent: write the theorem to be proved, $A_1 \land \cdots \land A_n \to B$, as the sequent $A_1, \cdots, A_n \Rightarrow B$ (to prove that $A$ is a theorem, write $\Rightarrow A$);
2. Apply the transformation rules backward: starting from this sequent, find the sequents from which it can be obtained, and eliminate all connectives step by step until only connective-free sequents remain;
3. Check the axiom: if all the connective-free sequents are axioms, the original theorem is proved; otherwise the original formula is not a theorem.

**Example 3.4.1** Use Wang's algorithm to prove $(P \to Q) \to (\lnot Q \to \lnot P)$.

| Step | Sequent | Justification |
| :-: | :-- | :-- |
| 1 | $\Rightarrow (P \to Q) \to (\lnot Q \to \lnot P)$ | To be proved |
| 2 | $P \to Q \Rightarrow \lnot Q \to \lnot P$ | From 1, $\Rightarrow \to$ |
| 3 | $\lnot Q, P \to Q \Rightarrow \lnot P$ | From 2, $\Rightarrow \to$ |
| 4 | $P, \lnot Q, P \to Q \Rightarrow$ | From 3, $\Rightarrow \lnot$ |
| 5 | $P, P \to Q \Rightarrow Q$ | From 4, $\lnot \Rightarrow$ |
| 6 | $Q, P \Rightarrow Q$ | From 5, $\to \Rightarrow$ (first branch); axiom |
| 7 | $P \Rightarrow P, Q$ | From 5, $\to \Rightarrow$ (second branch); axiom |

Lines 6 and 7 contain no connectives and have a propositional variable in common on both sides, so both are axioms, and the original formula is proved.

### 3.4.6. Features of Wang Hao's Algorithm

- Sound and complete: every formula proved by Wang's algorithm is a tautology, and every tautology of propositional logic can be proved by it;
- Mechanical: each application of a transformation rule eliminates one connective, so the derivation necessarily ends in finitely many steps with the verdict "theorem" or "not a theorem"; it can therefore be implemented on a computer, making theorem proving automatic;
- Goal-directed: the transformation rules are applied backward from the conclusion to be proved, and each step depends only on the connectives in the current sequent; there is no need to search for suitable substitutions as in Russell's axiom system.

One chapter of such abstract material is enough. Next we turn to a more concrete language: predicate logic.
