---
title: Basic Concepts of Propositions
source_hash: 9bd289019bb1
---

The core of mathematical logic is the symbolization of logical reasoning. This chapter starts with the simplest case, *propositional logic*: we first explain what a proposition is, then introduce the connectives that combine propositions, define the legitimate formulas and their truth tables, and finally present tautologies and the substitution rule. The next chapter builds on this to discuss equivalence between formulas, normal forms, and inference.

## 1.1. Propositions

The basic elements of logical reasoning are propositions.

**Definition 1.1.1 (Proposition)** A declarative sentence that can be judged true or false, and is either true or false, is called a **proposition**.

**Definition 1.1.2 (Truth Value)** The outcome of the judgment expressed by a proposition is called its **truth value**. It is either true or false, written 1 or 0 respectively. A proposition whose truth value is true is called a **true proposition**, and one whose truth value is false is called a **false proposition**.

Every proposition has a unique truth value: it cannot be neither true nor false, nor both true and false. The truth value may, however, be unknown for the time being, that is, "undetermined".

**Example 1.1.1** A conjecture that has not yet been proved is a proposition whose truth value is undetermined. "$x$ is greater than $y$", without further conditions, may be true or false; it has no unique truth value and is not a proposition. "I am lying" cannot be judged true or false, so it is not a proposition either.

Symbolization of propositions: we denote propositions by lowercase letters $p, q, r, \cdots$.

**Remark 1.1.1** Many textbooks use uppercase letters for propositions; we use lowercase letters instead, to avoid confusion with the $P$ of probability. To distinguish compound propositions from simple ones, a compound proposition is sometimes also written with an uppercase letter.

## 1.2. Propositional Connectives

Once propositions are symbolized, we can define operations on them, that is, ways of compounding propositions. *Logical connectives* are the operators of these propositional operations.

**Definition 1.2.1 (Simple and Compound Propositions)** A proposition that cannot be decomposed into simpler propositions, that is, one containing no connectives, is called a **simple proposition** or an **atomic proposition**. A proposition built from simple propositions by means of connectives is called a **compound proposition**. A compound proposition also has a definite truth value, which depends on the truth values of the simple propositions it contains.

**Definition 1.2.2 (Propositional Constants and Propositional Variables)** A simple proposition with a fixed truth value is called a **propositional constant**; a simple proposition whose truth value may vary is called a **propositional variable**. When discussing formulas, we usually need not distinguish between propositions and propositional variables.

We now introduce the five commonly used logical connectives:

- *Negation* $\lnot$: a unary connective meaning "it is not the case that". The negation of $p$ is written $\lnot p$ and read "not $p$".
- *Conjunction* $\land$: a binary connective meaning "and". The conjunction of $p$ and $q$ is written $p \land q$ and read "$p$ and $q$".
- *Disjunction* $\lor$: a binary connective meaning "or". The disjunction of $p$ and $q$ is written $p \lor q$ and read "$p$ or $q$".
- *Implication* $\to$: a binary connective meaning "if … then …". The implication from $p$ to $q$ is written $p \to q$ and read "if $p$, then $q$". Do not confuse it with the symbol $\Rightarrow$ for tautological implication (see [1.1.2](/1.1.2#sec-2.7)).
- *Biconditional* $\leftrightarrow$: a binary connective meaning "if and only if". The biconditional of $p$ and $q$ is written $p \leftrightarrow q$ and read "$p$ if and only if $q$". Do not confuse it with the symbol $\Leftrightarrow$ for logical equivalence (see [1.1.2](/1.1.2#sec-2.1)).

Of the four binary connectives, only implication has a direction. In $p \to q$, $p$ is called the antecedent and $q$ the consequent; the antecedent is a sufficient condition for the consequent, and the consequent is a necessary condition for the antecedent. An implication is false only when its antecedent is true and its consequent is false.

**Remark 1.2.1 (The Strange Implication)** When the antecedent is false, the implication is always true, which gives implication some counterintuitive properties. Its meaning does not fully coincide with natural-language connectives of inference such as "if … then …" or "because … therefore …"; the closest is in fact "whenever … , …". Moreover, these natural-language connectives often suggest some intrinsic link between antecedent and consequent, whereas in mathematical logic the antecedent and the consequent may be entirely unrelated. For example, "Because China's national football team won the 2022 World Cup, I got full marks in discrete mathematics", read as an implication, is a true proposition in mathematical logic.

## 1.3. Well-Formed Formulas

Not every string of propositional variables and connectives is meaningful; $p q \to$, for instance, is not. The meaningful strings are given by the following recursive definition.

**Definition 1.3.1 (Well-Formed Formula)** A **well-formed formula**, also called a **propositional formula** or simply a **formula**, is defined recursively by the following rules:

1. A single propositional variable is a well-formed formula, called an **atomic propositional formula**;
2. If $A$ is a well-formed formula, then so is $\lnot A$;
3. If $A$ and $B$ are well-formed formulas, then so are $(A \land B)$, $(A \lor B)$, $(A \to B)$, and $(A \leftrightarrow B)$ (the outermost parentheses may be omitted);
4. A string is a well-formed formula only if it is obtained by finitely many applications of the three rules above.

Well-formed formulas are denoted by uppercase letters $A, B, C, \cdots$. The notation $A(p_1, \cdots, p_n)$ denotes a well-formed formula $A$ that depends on the propositional variables $p_1, \cdots, p_n$.

**Definition 1.3.2 (Truth Assignment)** Assigning a truth value to each of the propositional variables $p_1, \cdots, p_n$ occurring in a formula $A$ is called a **truth assignment** (also an interpretation) for $A$. An assignment under which the formula takes the value 1 is called a **satisfying assignment**, and one under which it takes the value 0 is called a **falsifying assignment**.

**Definition 1.3.3 (Subformula)** If $A$ is part of a formula $\Phi(A)$ and $A$ is itself a well-formed formula, then $A$ is called a **subformula** of $\Phi(A)$.

## 1.4. Truth Tables

A *truth table* lists the values of a formula under all truth assignments: it enumerates all combinations of values of the propositional variables $p_1, \cdots, p_n$ and computes the truth value of the formula row by row. By convention, the assignments start from $00\cdots0$ and increase by binary addition up to $11\cdots1$. For a complicated formula, the truth values of its subformulas can also be listed in separate columns, following the order of evaluation.

In principle, the truth table is a universal tool for studying the properties of formulas. With $n$ propositional variables, however, a truth table has $2^n$ rows, so it is easy to write down only when there are few variables.

The truth tables of the basic compound propositions built with the five common connectives are as follows:

| $p$ | $q$ | $\lnot p$ | $p \land q$ | $p \lor q$ | $p \to q$ | $p \leftrightarrow q$ |
| :-: | :-: | :-------: | :---------: | :--------: | :-------: | :-------------------: |
|  0  |  0  |     1     |      0      |     0      |     1     |           1           |
|  0  |  1  |     1     |      0      |     1      |     1     |           0           |
|  1  |  0  |     0     |      0      |     1      |     0     |           0           |
|  1  |  1  |     0     |      1      |     1      |     1     |           1           |

## 1.5. Tautologies and the Substitution Rule

**Definition 1.5.1 (Tautology)** A formula that is true under every truth assignment is called a **tautology**, or an **identically true formula**; equivalently, the last column of its truth table consists entirely of 1s.

**Definition 1.5.2 (Contradiction)** A formula that is false under every truth assignment is called a **contradiction**, or an **identically false formula**; equivalently, the last column of its truth table consists entirely of 0s.

**Definition 1.5.3 (Satisfiable Formula)** A formula that is not a contradiction, that is, one with at least one satisfying assignment, is called a **satisfiable formula**. Every tautology is also satisfiable.

**Remark 1.5.1** If the word "tautology" seems hard to remember, think of its literal meaning, "saying the same thing again". Like the awkward remark "this cup is really quite a cup", a tautology is "empty talk" that is always right.

Tautologies are the basis of inference, and the following *substitution rule* is a frequently used rule of inference.

**Theorem 1.5.1 (Substitution Rule)** If every occurrence of some propositional variable $p$ in a tautology $A$ is replaced by one and the same well-formed formula $B$, the result is again a tautology. This substitution is written $A\dfrac{p}{B}$.

The tautology obtained by substitution is more complex. One can therefore first list some simple tautologies and then approach the desired conclusion step by step through substitution.

## 1.6. Polish Notation

In the well-formed formulas introduced so far, each connective is written between its two operands; this is called *infix notation*. It needs parentheses to fix the order of evaluation and matches human reading habits, but for a computer, processing such formulas requires repeated scanning or a stack for matching parentheses. **Polish notation**, by contrast, needs no parentheses, and a formula can be parsed in a single left-to-right scan.

**Definition 1.6.1 (Polish Notation)** An expression in which each operator is written before its operands is said to be in **Polish notation**, or **prefix notation**; an expression in which each operator is written after its operands is said to be in **reverse Polish notation**, or **postfix notation**.

Store a propositional formula as a tree: the leaves are propositional variables and the internal nodes are connectives (a negation node has only one child). Infix, prefix, and postfix expressions then correspond to the in-order, pre-order, and post-order traversals of this tree, respectively.

**Example 1.6.1** For the same formula:

| Notation | Expression |
| :-- | :-- |
| Infix | $\lnot p \land q$ |
| Prefix | $\land \lnot p q$ |
| Postfix | $p \lnot q \land$ |

Thus in converting between notations, the order of the propositional variables never changes; only the positions of the connectives move. The conversion can proceed from the outside in or from the inside out, but it is best to stick to one method; after a few exercises the pattern becomes clear.
