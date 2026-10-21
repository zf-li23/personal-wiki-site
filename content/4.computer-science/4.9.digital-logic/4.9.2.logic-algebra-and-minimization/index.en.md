---
title: Logic Algebra and Minimization
description: Basic and compound operations of logic algebra, gate symbols and the completeness of NAND; basic identities, the substitution, complementation and duality rules, and Shannon expansion; minterms, maxterms and canonical forms; algebraic, Karnaugh-map (with don't-cares) and Quine–McCluskey minimization, with a Python implementation and its complexity.
source_hash: 9d24e769bc66
---

The inputs and outputs of a digital circuit are binary signals, and how the output depends on the inputs is described by logic algebra. Logic algebra is the two-element case $\{0, 1\}$ of **Boolean algebra** from discrete mathematics, and its operations correspond one to one with the connectives of propositional logic: AND corresponds to **conjunction**, OR to **disjunction**, and NOT to negation. This chapter rewrites these existing mathematical tools in the language of circuit designers (operations correspond to gates, expressions to circuits), and focuses on one engineering problem: a logic function has infinitely many expressions, so how do we find the one that uses the fewest gates and the fewest gate inputs? This is the minimization of logic functions, and the chapter presents three methods: the algebraic method, which relies on identities; the Karnaugh-map method, which relies on a diagram; and the Quine–McCluskey tabular method, which can be programmed. The results of minimization become actual circuits in [Logic Gates](/4.9.3) and [Combinational Logic Circuits](/4.9.4).

Conventions of this chapter: variables $A, B, C, \dots$ take the value $0$ or $1$; $AB$ or $A\cdot B$ denotes AND, $A + B$ denotes OR, $\overline{A}$ denotes NOT, and $A \oplus B$ denotes **exclusive or**; the precedence of the operations is NOT, then AND, then OR. When numbering **minterms**, the first variable is the most significant bit (consistent with most English textbooks; some textbooks take $A$ as the least significant bit, which the reader should keep in mind when comparing).

## 2.1. Basic Operations of Logic Algebra

### 2.1.1. Logic Algebra and Logic Functions

**Definition 2.1.1 (Logic Algebra)** On the set $\{0, 1\}$ define the three operations AND ($\cdot$), OR ($+$) and NOT ($\overline{\phantom{A}}$) by the following tables; the resulting algebraic system $(\{0,1\}, +, \cdot, \overline{\phantom{A}}, 0, 1)$ is called **switching algebra**, also called logic algebra. It is the nontrivial **Boolean algebra** with the fewest elements.

| $A$ | $B$ | $A\cdot B$ | $A + B$ | $\overline{A}$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

Logic algebra was proposed by Boole in 1847 to study reasoning; in 1938 Shannon pointed out in his master's thesis that it can be used to analyze relay switching circuits, and since then it has been the mathematical foundation of digital circuit design. Compared with ordinary algebra, the variables of logic algebra take only the two values $0$ and $1$, we have $1 + 1 = 1$, and there is no subtraction or division.

**Definition 2.1.2 (Logic Function)** A mapping $F\colon \{0,1\}^n \to \{0,1\}$ is called an $n$-variable **Boolean function**. Two Boolean functions are equal if they take the same value for all $2^n$ inputs.

A logic function can be represented by a **truth table** (which lists the output for all $2^n$ inputs; it is unique but grows exponentially with $n$), a logic expression (compact but not unique), a logic diagram (the connections of gates), a waveform diagram (the inputs and outputs as functions of time), or hardware description language code. The truth table of $n$ variables has $2^n$ rows and the output of each row can be $0$ or $1$, so there are $2^{2^n}$ Boolean functions of $n$ variables in all. The $16$ functions for $n = 2$ are:

| Function | $AB=00$ | $01$ | $10$ | $11$ | Name and expression |
|---|---|---|---|---|---|
| $F_0$ | 0 | 0 | 0 | 0 | Constant $0$ |
| $F_1$ | 0 | 0 | 0 | 1 | AND $AB$ |
| $F_2$ | 0 | 0 | 1 | 0 | Inhibition $A\overline{B}$ |
| $F_3$ | 0 | 0 | 1 | 1 | $A$ |
| $F_4$ | 0 | 1 | 0 | 0 | Inhibition $\overline{A}B$ |
| $F_5$ | 0 | 1 | 0 | 1 | $B$ |
| $F_6$ | 0 | 1 | 1 | 0 | XOR $A \oplus B$ |
| $F_7$ | 0 | 1 | 1 | 1 | OR $A + B$ |
| $F_8$ | 1 | 0 | 0 | 0 | **NOR** $\overline{A + B}$ |
| $F_9$ | 1 | 0 | 0 | 1 | XNOR $A \odot B = \overline{A \oplus B}$ |
| $F_{10}$ | 1 | 0 | 1 | 0 | $\overline{B}$ |
| $F_{11}$ | 1 | 0 | 1 | 1 | Implication $A + \overline{B}$ |
| $F_{12}$ | 1 | 1 | 0 | 0 | $\overline{A}$ |
| $F_{13}$ | 1 | 1 | 0 | 1 | Implication $\overline{A} + B$ |
| $F_{14}$ | 1 | 1 | 1 | 0 | **NAND** $\overline{AB}$ |
| $F_{15}$ | 1 | 1 | 1 | 1 | Constant $1$ |

### 2.1.2. Compound Operations and Logic Gates

A circuit that implements a logic operation is called a *logic gate*, or simply a gate. Besides the three basic operations AND, OR and NOT, the commonly used compound operations are:

| Operation | Expression | Output is $1$ when |
|---|---|---|
| **NAND** | $\overline{AB}$ | Not all inputs are $1$ |
| **NOR** | $\overline{A + B}$ | All inputs are $0$ |
| AND-OR-INVERT | $\overline{AB + CD}$ | Both product terms are $0$ |
| **Exclusive or** | $A \oplus B = A\overline{B} + \overline{A}B$ | The inputs differ |
| XNOR | $A \odot B = AB + \overline{A}\,\overline{B}$ | The inputs are equal |

![Distinctive-shape symbols of common gates (IEEE Std 91): AND, OR, NOT, buffer, NAND, NOR, XOR, XNOR; a small circle denotes inversion](./plots/gate-symbols.py)

The figure shows the distinctive-shape symbols in common use in the United States and internationally. The Chinese national standard GB/T 4728.12 and IEC 60617 use rectangular symbols, writing `&` (AND), `≥1` (OR), `=1` (XOR) and `1` (buffer) inside the box, with a small circle or small triangle at the output denoting inversion; the two sets of symbols have the same meaning.

XOR has several properties that are used repeatedly in arithmetic circuits: $A \oplus 0 = A$, $A \oplus 1 = \overline{A}$, $A \oplus A = 0$; it satisfies the **commutative law** and the **associative law**, and $\overline{A \oplus B} = \overline{A} \oplus B = A \oplus \overline{B}$. The XOR $A_1 \oplus \cdots \oplus A_n$ of several variables equals $1$ if and only if the number of $1$s among them is odd, which is the **parity check** ([§1.3.4](/4.9.1#sec-1.3.4)).

**Theorem 2.1.1** $\{\text{NAND}\}$ and $\{\text{NOR}\}$ are each a **functionally complete set**: any logic function can be implemented using only **NAND gates** (or only **NOR gates**).

**Proof** From the truth table we can write the AND-OR expression of any logic function ([§2.3](#sec-2.3)), so it suffices to express AND, OR and NOT using NAND:

$$
\overline{A} = \overline{A\cdot A},\qquad AB = \overline{\overline{AB}\cdot\overline{AB}},\qquad A + B = \overline{\overline{A}\cdot\overline{B}} = \overline{\overline{A\cdot A}\cdot\overline{B\cdot B}} .
$$
The case of NOR follows by duality ([§2.2.2](#sec-2.2.2)). $\square$

This theorem has practical significance: in CMOS technology, NAND and NOR gates are the simplest gates ([Logic Gates and Their Electrical Characteristics](/4.9.3)), and an AND or OR gate actually needs an extra inverter after a NAND or NOR gate.

## 2.2. Basic Identities and Rules

### 2.2.1. Basic Identities

All identities of logic algebra can be proved by perfect induction: check that both sides are equal for every combination of values of the variables (that is, compare truth tables). In the identities below, the left and right columns are duals of each other ([§2.2.2](#sec-2.2.2)).

| Name | Identity | Dual |
|---|---|---|
| Identity and null laws | $A \cdot 0 = 0$, $A \cdot 1 = A$ | $A + 1 = 1$, $A + 0 = A$ |
| Complement law | $A\overline{A} = 0$ | $A + \overline{A} = 1$ |
| Idempotent law | $AA = A$ | $A + A = A$ |
| Involution law | $\overline{\overline{A}} = A$ | |
| Commutative law | $AB = BA$ | $A + B = B + A$ |
| Associative law | $(AB)C = A(BC)$ | $(A + B) + C = A + (B + C)$ |
| **Distributive law** | $A(B + C) = AB + AC$ | $A + BC = (A + B)(A + C)$ |
| **De Morgan's laws** | $\overline{AB} = \overline{A} + \overline{B}$ | $\overline{A + B} = \overline{A}\cdot\overline{B}$ |
| Absorption law | $A(A + B) = A$ | $A + AB = A$ |
| | $A(\overline{A} + B) = AB$ | $A + \overline{A}B = A + B$ |
| | $(A + B)(A + \overline{B}) = A$ | $AB + A\overline{B} = A$ |
| Consensus law | $(A + B)(\overline{A} + C)(B + C) = (A + B)(\overline{A} + C)$ | $AB + \overline{A}C + BC = AB + \overline{A}C$ |

Note that the second distributive law $A + BC = (A + B)(A + C)$ does not hold in ordinary algebra; it is specific to logic algebra. **De Morgan's laws** hold for any number of variables: $\overline{A_1A_2\cdots A_n} = \overline{A_1} + \cdots + \overline{A_n}$.

**Theorem 2.2.1 (Consensus Theorem)** $AB + \overline{A}C + BC = AB + \overline{A}C$, and more generally $AB + \overline{A}C + BCD = AB + \overline{A}C$.

**Proof** $BC = BC(A + \overline{A}) = ABC + \overline{A}BC$; the first term is absorbed by $AB$ and the second by $\overline{A}C$. The general form is similar: $BCD = ABCD + \overline{A}BCD$. $\square$

$BC$ is called the *consensus* term of $AB$ and $\overline{A}C$: when one product term contains $A$ and the other contains $\overline{A}$, the product of the remaining factors after removing $A$ and $\overline{A}$ is the consensus term, and it is redundant. A consensus term can be deleted in minimization, but in [Races and Hazards](/4.9.4) we shall see that it is sometimes added deliberately to eliminate a hazard.

### 2.2.2. Substitution, Complementation and Duality Rules

**Substitution rule** In an equation, if the same variable on both sides is replaced by the same logic function, the equation still holds. For example, substituting $B + C$ for $B$ in $\overline{A + B} = \overline{A}\,\overline{B}$ gives $\overline{A + B + C} = \overline{A}\,\overline{B}\,\overline{C}$. This holds because a variable can take any value in the first place.

**Theorem 2.2.2 (Complementation Theorem)** In an expression of a logic function $F$, replace every $\cdot$ by $+$ and every $+$ by $\cdot$, every $0$ by $1$ and every $1$ by $0$, and every uncomplemented variable by its complement and vice versa; the resulting expression is $\overline{F}$. During the transformation the original order of operations must be preserved (add parentheses where necessary), and a long bar spanning several variables stays unchanged, with only the expression under it being transformed.

**Proof** We use induction on the structure of the expression, applying De Morgan's laws once at each step: $\overline{G + H} = \overline{G}\cdot\overline{H}$, $\overline{GH} = \overline{G} + \overline{H}$, $\overline{\overline{G}} = G$. $\square$

**Example 2.2.1**
- For $F = A\overline{B} + \overline{C}D$, we have $\overline{F} = (\overline{A} + B)(C + \overline{D})$.
- For $F = A + BC$, we have $\overline{F} = \overline{A}(\overline{B} + \overline{C})$; writing it as $\overline{A}\,\overline{B} + \overline{C}$ changes the order of operations and is a common mistake.
- For $F = \overline{A\overline{B}} + C$, we have $\overline{F} = \overline{\overline{A} + B}\cdot\overline{C}$, which simplifies to $A\overline{B}\,\overline{C}$.

**Definition 2.2.1 (Dual)** The expression obtained from an expression $F$ by interchanging $\cdot$ and $+$ and interchanging $0$ and $1$, leaving the variables unchanged (and the order of operations preserved as well), is called the **dual formula** of $F$ and is denoted $F^{*}$.

This is the same concept as the **dual formula** in propositional logic. By the complementation theorem, $F^{*}(A_1, \dots, A_n) = \overline{F(\overline{A_1}, \dots, \overline{A_n})}$, so the dual depends only on the function itself and not on which expression is used; moreover $(F^{*})^{*} = F$.

**Theorem 2.2.3 (Duality Theorem)** If two logic expressions are equal, $F = G$, then their duals are also equal: $F^{*} = G^{*}$.

**Proof** $F = G$ holds for all inputs. Substituting the complement of each variable for the variable in the equation and then complementing both sides gives $\overline{F(\overline{A_1},\dots)} = \overline{G(\overline{A_1},\dots)}$, that is, $F^{*} = G^{*}$. $\square$

Hence for the identities of §2.2.1 it suffices to prove one column, and the other column follows from the duality theorem. For example, $A + \overline{A}B = A + B$ immediately gives $A(\overline{A} + B) = AB$.

### 2.2.3. Expansion Theorem

**Theorem 2.2.4 (Shannon Expansion)** For any logic function $F$ and any variable $A$ in it,

$$
F(A, B, \dots) = A\cdot F(1, B, \dots) + \overline{A}\cdot F(0, B, \dots),
$$
and dually

$$
F(A, B, \dots) = \bigl(A + F(0, B, \dots)\bigr)\bigl(\overline{A} + F(1, B, \dots)\bigr).
$$

**Proof** Substitute $A = 1$ and $A = 0$ respectively; both sides agree in each case. $\square$

$F(1, B, \dots)$ and $F(0, B, \dots)$ are called the cofactors of $F$ with respect to $A$. The expansion theorem decomposes an $n$-variable function into two $(n-1)$-variable functions, with the select signal $A$ deciding which one is output; this is exactly the function of a 2-to-1 multiplexer, and it is the basis for implementing arbitrary functions with multiplexers ([Combinational Logic Circuits](/4.9.4)). Expanding repeatedly over all the variables gives the canonical sum of products of the next section; drawing the expansion as a tree and merging identical subtrees gives the binary decision diagram (BDD), one of the basic data structures with which modern logic synthesis and formal verification tools represent logic functions.

## 2.3. Canonical Forms of Logic Functions

### 2.3.1. Minterms and Maxterms

**Definition 2.3.1 (Minterms and Maxterms)** In a logic function of $n$ variables, a product term that contains all $n$ variables, each appearing exactly once in either uncomplemented or complemented form, is called a **minterm** (the same as the minterm of propositional logic); a sum term satisfying the same condition is called a **maxterm**. Writing an uncomplemented variable as $1$ and a complemented variable as $0$ gives, in the order of the variables, an $n$-bit binary number $i$, and the corresponding minterm and maxterm are denoted $m_i$ and $M_i$, respectively.

For example, among the three variables $A, B, C$ we have $m_5 = A\overline{B}C$ ($101$) and $M_5 = \overline{A} + B + \overline{C}$: the maxterm $M_i$ is the sum term that is $0$ in row $i$, written with the complemented variable wherever the variable is $1$. Properties of minterms and maxterms:

1. $n$ variables have $2^n$ minterms and $2^n$ maxterms.
2. For each minterm $m_i$ there is exactly one input (namely the binary number $i$) that makes it $1$; for each maxterm $M_i$, exactly this one input makes it $0$.
3. The product of any two distinct minterms is $0$, and the sum of all minterms is $1$; dually, the sum of any two distinct maxterms is $1$, and the product of all maxterms is $0$.
4. $M_i = \overline{m_i}$; that is, the maxterm and the minterm with the same index are complements of each other.

### 2.3.2. Canonical Sum of Products and Canonical Product of Sums

**Theorem 2.3.1** Any logic function $F$ can be uniquely expressed as a sum of some minterms, and also uniquely as a product of some maxterms:

$$
F = \sum_{F(i) = 1} m_i = \prod_{F(i) = 0} M_i .
$$

**Proof** Applying **Shannon expansion** repeatedly over all variables of $F$ gives $F = \sum_i F(i)\, m_i$, where the coefficient $F(i) \in \{0,1\}$ is the output of row $i$ of the truth table, so it is uniquely determined by the truth table. Writing the canonical sum of products of $\overline{F}$ and complementing it, De Morgan's laws and property 4 give the canonical product of sums. $\square$

**Definition 2.3.2 (Canonical Sum of Products and Canonical Product of Sums)** The form of a logic function as a sum of minterms is called its **canonical sum of products**, and the form as a product of maxterms is called its **canonical product of sums**.

The index sets used by the two are complementary; they are the **principal disjunctive normal form** and the **principal conjunctive normal form** of discrete mathematics. The canonical forms are read directly from the truth table: rows with output $1$ correspond to minterms and rows with output $0$ correspond to maxterms.

**Example 2.3.1** $F(A, B, C) = AB + \overline{A}C$. $AB$ covers $110, 111$ and $\overline{A}C$ covers $001, 011$, so

$$
F = \sum m(1, 3, 6, 7) = \prod M(0, 2, 4, 5), \qquad \overline{F} = \sum m(0, 2, 4, 5).
$$
The algebraic method gives the same result: $AB = AB(C + \overline{C}) = ABC + AB\overline{C}$ and $\overline{A}C = \overline{A}BC + \overline{A}\,\overline{B}C$.

The canonical forms are unique and suitable for deciding whether two functions are equal, but they are usually long: a function of $n$ variables may need as many as $2^{n-1}$ minterms (for example, the parity function of $n$ variables), so minimization is needed.

## 2.4. Algebraic Minimization

The goal of minimization depends on the implementation. For a circuit implemented in two levels with AND and OR gates, the goal is the minimal sum of products.

**Definition 2.4.1 (Minimal Sum of Products)** An AND-OR expression of a logic function that satisfies (1) the number of product terms is the smallest, and (2) subject to that, the number of variables in each product term is the smallest, is called a **minimal sum of products** of the function. The minimal product of sums is defined dually.

Condition (1) minimizes the number of AND gates, and condition (2) minimizes the number of gate inputs. The minimal sum of products need not be unique.

The algebraic method applies the identities of §2.2.1 repeatedly. There are five commonly used techniques:

| Technique | Basis | Example |
|---|---|---|
| Combining terms | $AB + A\overline{B} = A$ | $A\overline{B}C + A\overline{B}\,\overline{C} = A\overline{B}$ |
| Absorption | $A + AB = A$ | $\overline{A}B + \overline{A}BCD = \overline{A}B$ |
| Eliminating literals | $A + \overline{A}B = A + B$ | $AB + \overline{A}C + \overline{B}C = AB + \overline{AB}\,C = AB + C$ |
| Eliminating terms | Consensus theorem | $AB + \overline{A}C + BCD = AB + \overline{A}C$ |
| Adding terms | $A = A(B + \overline{B})$ or $A = A + A$ | Expand first and then combine with other terms; see Example 2.4.1 |

**Example 2.4.1** Minimize $F = A\overline{B} + B\overline{C} + \overline{B}C + \overline{A}B$. Add the factors $A + \overline{A}$ to $\overline{B}C$ and $C + \overline{C}$ to $\overline{A}B$, and then combine:

$$
\begin{aligned}
F &= A\overline{B} + B\overline{C} + \overline{B}C(A + \overline{A}) + \overline{A}B(C + \overline{C})\\
&= A\overline{B} + B\overline{C} + A\overline{B}C + \overline{A}\,\overline{B}C + \overline{A}BC + \overline{A}B\overline{C}\\
&= (A\overline{B} + A\overline{B}C) + (B\overline{C} + \overline{A}B\overline{C}) + (\overline{A}\,\overline{B}C + \overline{A}BC)\\
&= A\overline{B} + B\overline{C} + \overline{A}C .
\end{aligned}
$$
Another way of adding terms gives $F = A\overline{C} + \overline{B}C + \overline{A}B$, which also has three terms with two variables each. Both results are minimal sums of products, which shows that the minimal form is not unique, and also that the algebraic method depends on skill and makes it hard to confirm that a result is already minimal.

The minimal product of sums can be obtained dually: for example, $(A + B)(A + \overline{B})(B + C) = A(B + C)$. Alternatively, find the minimal sum of products of $\overline{F}$ first and then use the complementation theorem to obtain the minimal product of sums of $F$.

## 2.5. Karnaugh-Map Minimization

### 2.5.1. Karnaugh Maps

The core operation of the algebraic method is combining "adjacent" minterms: when two minterms differ in only one variable, $XA + X\overline{A} = X$ eliminates that variable. If the minterms are arranged in a diagram so that minterms differing in one variable are adjacent in the diagram, combining can be done by eye.

**Definition 2.5.1 (Karnaugh Map)** Divide the $n$ variables into two groups used as rows and columns, with the values of rows and columns both arranged in Gray code order (such as $00, 01, 11, 10$), so that each cell corresponds to a minterm; the resulting grid is called a **Karnaugh map** (Karnaugh, 1953).

![Layouts of three-variable and four-variable Karnaugh maps: rows and columns are arranged in Gray code, and each cell is labeled with its minterm index](./plots/kmap-layout.py)

Because the rows and columns are arranged in **Gray code**, geometrically adjacent cells differ in only one variable; the leftmost and rightmost cells of the same row, and the topmost and bottommost cells of the same column, are also adjacent (think of the map as a torus), and the four corners of a four-variable map are adjacent as well. $2^k$ cells forming a rectangle, with every two cells adjacent in the above sense, can be combined into one product term that eliminates $k$ variables: the variables retained are those whose values do not change across these cells.

To enter a logic function into a Karnaugh map, put $1$ in the cell of each minterm and $0$ in the others. If a general sum of products is given, all cells of the block corresponding to each product term are filled with $1$.

### 2.5.2. Implicants and the Minimization Procedure

**Definition 2.5.2 (Implicant)** A product term $P$ is called an **implicant** of $F$ if $F$ is necessarily $1$ whenever $P$ equals $1$ (on a Karnaugh map, $P$ is a rectangular block containing only $1$s). If $P$ is no longer an implicant after removing any one variable, $P$ is called a **prime implicant** (on a Karnaugh map, a block that cannot be enlarged further). If some minterm is covered by only one prime implicant, that prime implicant is called an **essential prime implicant**.

**Theorem 2.5.1 (Quine)** Every product term in a minimal sum of products is a prime implicant.

**Proof** If some product term in a minimal expression is not a prime implicant, one variable can be removed from it while it remains an implicant; the function is unchanged but the number of variables decreases, contradicting minimality. $\square$

Minimization therefore has two steps: find all prime implicants, and then select the fewest of them that cover all the $1$s; the essential prime implicants must be selected. On a Karnaugh map the procedure is:

1. Draw the map and fill in the $1$s.
2. Circle all the largest blocks that can be circled (the prime implicants). A block has $1, 2, 4, 8, \dots$ cells and must be a rectangle, which may wrap around edges and corners.
3. First select the essential prime implicants: the blocks containing a $1$ that is covered by only one block.
4. Cover the remaining $1$s with the fewest of the other blocks. Each block must contain at least one $1$ not covered by the other selected blocks; otherwise the block is redundant.
5. Write each block as a product term and add them to get the minimal sum of products.

![Two examples of Karnaugh-map minimization: in the left map the four two-cell blocks are all essential prime implicants, and the large middle block BD, although a prime implicant, is redundant; the right map is the BCD value test with don't-care terms](./plots/kmap-examples.py)

**Example 2.5.1** $F(A,B,C,D) = \sum m(3, 4, 5, 7, 9, 13, 14, 15)$ (left map). There are five prime implicants: $\overline{A}B\overline{C}$, $\overline{A}CD$, $A\overline{C}D$, $ABC$ and $BD$. Each of the first four covers a $1$ belonging only to itself ($m_4, m_3, m_9, m_{14}$), so they are essential prime implicants; they already cover all four cells of $BD$, so the largest block $BD$ is redundant:

$$
F = \overline{A}B\overline{C} + \overline{A}CD + A\overline{C}D + ABC .
$$
"Circle the largest blocks first" is only a rule of thumb for finding prime implicants; the selection should start from the essential prime implicants.

The complement function and the product of sums can be obtained from the $0$s: circle the $0$s on the Karnaugh map and apply the same rules to obtain the minimal sum of products of $\overline{F}$; complementing it (complementation theorem) gives the minimal product of sums of $F$. For $F = \sum m(1,3,6,7)$ of Example 2.3.1, the $0$s are at $m_0, m_2, m_4, m_5$; circling $\overline{A}\,\overline{C}$ ($m_0, m_2$) and $A\overline{B}$ ($m_4, m_5$) gives $\overline{F} = \overline{A}\,\overline{C} + A\overline{B}$, so $F = (A + C)(\overline{A} + B)$.

### 2.5.3. Don't-Care Terms

**Definition 2.5.3 (Don't-Care Term)** If for some input combinations the output of the function may be either $0$ or $1$, the minterms corresponding to these input combinations are called **don't-care terms**; they are written as $\times$ (or X) in truth tables and Karnaugh maps and as $\sum d(\cdots)$ in expressions.

Don't-care terms have two sources: these input combinations never occur in normal operation (constraint terms, such as $1010$–$1111$ in the **BCD** code); or they do occur, but the output is then ignored by the following stage. In minimization a don't-care term may be treated as $1$ and included in a block to enlarge it, or treated as $0$ and left out; but blocks must not be added merely to circle don't-care terms.

**Example 2.5.2** The input $ABCD$ is the 8421 code of a decimal digit ($A$ is the most significant bit), and $F = 1$ when the value $x \ge 5$ and $F = 0$ otherwise. Then

$$
F = \sum m(5, 6, 7, 8, 9) + \sum d(10, 11, 12, 13, 14, 15).
$$
As in the right map, treating the don't-care terms as $1$ lets us circle an $8$-cell block $A$ and two $4$-cell blocks $BD$ and $BC$, giving $F = A + BD + BC$. Without using the don't-care terms, the minimal expression is $A\overline{B}\,\overline{C} + \overline{A}BD + \overline{A}BC$, in which every AND gate has more inputs.

Karnaugh maps are suitable for functions of at most $4$ variables; for $5$ or $6$ variables two or four four-variable maps must be stacked and the adjacency is no longer intuitive, and more variables can only be left to computers. When minimizing multiple-output functions (several outputs for the same inputs), we also try to find product terms that can be shared by several outputs; a single output may then fail to be minimal, but the whole circuit is the cheapest. Such problems are handled by the methods of the next section and by logic synthesis tools.

## 2.6. The Quine–McCluskey Method

### 2.6.1. Finding All Prime Implicants

A Karnaugh map relies on the human eye to recognize adjacency. In the language of indices, two minterms are adjacent if and only if their binary indices differ in exactly one bit; in that case the numbers of $1$s in the two indices differ by exactly $1$. Hence if the minterms are grouped by the number of $1$s in their indices, only adjacent groups need to be compared.

**Algorithm 2.6.1 (Quine–McCluskey Algorithm)** Input: the indices of the minterms (and don't-care terms) of a function. Output: a minimal sum of products.

1. Write all minterms and don't-care terms in binary and group them by the number of $1$s, forming Table I.
2. Compare every pair of terms in adjacent groups; if they differ in exactly one bit, merge them into one term, record that bit as `-`, write it into the next table, and put a √ on the two terms that took part in the merge. In the next table only terms with `-` in the same positions can be merged. Repeat this step until no more merges are possible. The terms without √ in all the tables are exactly all the prime implicants.
3. Build a cover table of prime implicants against minterms (don't-care terms are not listed). A column covered by only one prime implicant determines an essential prime implicant; select these and delete the columns they cover.
4. Simplify the cover table: if the (remaining) minterms covered by a prime implicant $P$ are a subset of those covered by $Q$, delete row $P$ (row dominance); if the column of a minterm $m$ contains the column of $m'$ (every prime implicant covering $m'$ also covers $m$), delete column $m$ (column dominance). New essential terms (secondary essential prime implicants) may appear after the deletion; return to step 3.
5. If the table is still not empty (a cyclic cover table), find a minimum cover by exhaustive search or Petrick's method.

**Example 2.6.1** Minimize $F(A,B,C,D) = \sum m(2, 4, 6, 8, 9, 10, 12, 13, 15)$.

Table I is grouped by the number of $1$s, Table II is the result of one round of merging, and Table III is the result of two rounds:

| Group | Table I | Table II | Table III |
|---|---|---|---|
| 1 | $m_2$ `0010` √, $m_4$ `0100` √, $m_8$ `1000` √ | (2,6) `0-10`, (2,10) `-010`, (4,6) `01-0`, (4,12) `-100`, (8,9) `100-` √, (8,10) `10-0`, (8,12) `1-00` √ | (8,9,12,13) `1-0-` |
| 2 | $m_6$ `0110` √, $m_9$ `1001` √, $m_{10}$ `1010` √, $m_{12}$ `1100` √ | (9,13) `1-01` √, (12,13) `110-` √ | |
| 3 | $m_{13}$ `1101` √ | (13,15) `11-1` | |
| 4 | $m_{15}$ `1111` √ | | |

((8,9,12,13) can be obtained either by merging (8,9) with (12,13) or by merging (8,12) with (9,13); it is recorded only once.) The seven terms without √ are all the prime implicants:

$$
\begin{aligned}
&P_1 = \overline{A}C\overline{D}\ (2,6),\quad P_2 = \overline{B}C\overline{D}\ (2,10),\quad P_3 = \overline{A}B\overline{D}\ (4,6),\quad P_4 = B\overline{C}\,\overline{D}\ (4,12),\\
&P_5 = A\overline{B}\,\overline{D}\ (8,10),\quad P_6 = ABD\ (13,15),\quad P_7 = A\overline{C}\ (8,9,12,13).
\end{aligned}
$$

### 2.6.2. Selecting Prime Implicants

The cover table of Example 2.6.1 (△ means covers):

| | $m_2$ | $m_4$ | $m_6$ | $m_8$ | $m_9$ | $m_{10}$ | $m_{12}$ | $m_{13}$ | $m_{15}$ |
|---|---|---|---|---|---|---|---|---|---|
| $P_1$ | △ | | △ | | | | | | |
| $P_2$ | △ | | | | | △ | | | |
| $P_3$ | | △ | △ | | | | | | |
| $P_4$ | | △ | | | | | △ | | |
| $P_5$ | | | | △ | | △ | | | |
| $P_6$ | | | | | | | | △ | △ |
| $P_7$ | | | | △ | △ | | △ | △ | |

- $m_9$ is covered only by $P_7$ and $m_{15}$ only by $P_6$, so $P_6$ and $P_7$ are essential prime implicants; delete the $m_8, m_9, m_{12}, m_{13}, m_{15}$ that they cover.
- The remaining minterms are $m_2, m_4, m_6, m_{10}$. $P_4$ has only $m_4$ left and is dominated by $P_3$; $P_5$ has only $m_{10}$ left and is dominated by $P_2$; delete these two rows.
- Now $m_4$ is covered only by $P_3$ and $m_{10}$ only by $P_2$; select $P_2$ and $P_3$, which also cover $m_2$ and $m_6$, so $P_1$ is redundant.

$$
F = A\overline{C} + ABD + \overline{A}B\overline{D} + \overline{B}C\overline{D} .
$$

Selecting prime implicants is in general a set cover problem: choose the fewest rows of the cover table to cover all columns. For a cyclic cover table, in which every column is covered by at least two rows and no dominance relation exists, Petrick's method writes "at least one row must be chosen for each column" as a product of sums $\prod_m \sum_{P \ni m} P$, expands it into a sum of products, and takes the product term with the fewest factors (and then the fewest literals); it is still essentially exhaustive search.

### 2.6.3. Implementation and Complexity

Every step of the Q-M method is a mechanical comparison and marking, which suits programming. The implementation below represents a product term as a pair `(value, mask)`: the bits that are $1$ in `mask` are the eliminated variables, and `value` holds the values of the other bits.

```python
from itertools import combinations


def prime_implicants(n, ones, dcs=()):
    """Return all prime implicants as (value, mask) pairs; mask bits are eliminated."""
    current = {(m, 0) for m in set(ones) | set(dcs)}
    primes = set()
    while current:
        merged, used = set(), set()
        groups = {}                      # (mask, number of ones) -> terms
        for v, msk in current:
            groups.setdefault((msk, bin(v).count("1")), []).append((v, msk))
        for (msk, k), terms in groups.items():
            for v1, _ in terms:
                for v2, _ in groups.get((msk, k + 1), []):
                    diff = v1 ^ v2
                    if diff & (diff - 1) == 0:      # exactly one bit differs
                        merged.add((v1 & ~diff, msk | diff))
                        used |= {(v1, msk), (v2, msk)}
        primes |= current - used         # terms that merged with nothing are prime
        current = merged
    return primes


def covers(term, m):
    v, msk = term
    return (m & ~msk) == v


def minimum_cover(primes, ones):
    """Essential prime implicants first, then the smallest set of the rest (exhaustive)."""
    ones = set(ones)
    chosen = set()
    for m in ones:
        cands = [p for p in primes if covers(p, m)]
        if len(cands) == 1:
            chosen.add(cands[0])
    left = {m for m in ones if not any(covers(p, m) for p in chosen)}
    rest = [p for p in primes - chosen if any(covers(p, m) for m in left)]
    for k in range(len(rest) + 1):
        for combo in combinations(rest, k):
            if all(any(covers(p, m) for p in combo) for m in left):
                return chosen | set(combo)


def to_str(term, names):
    v, msk = term
    n = len(names)
    lits = []
    for i, name in enumerate(names):
        bit = 1 << (n - 1 - i)
        if not msk & bit:
            lits.append(name if v & bit else name + "'")
    return "".join(lits) or "1"


ones = [2, 4, 6, 8, 9, 10, 12, 13, 15]
pis = prime_implicants(4, ones)
print(sorted(to_str(p, "ABCD") for p in pis))
print(sorted(to_str(p, "ABCD") for p in minimum_cover(pis, ones)))
print(sorted(to_str(p, "ABCD") for p in
             minimum_cover(prime_implicants(4, [5, 6, 7, 8, 9], range(10, 16)), [5, 6, 7, 8, 9])))
```

```text
["A'BD'", "A'CD'", "AB'D'", 'ABD', "AC'", "B'CD'", "BC'D'"]
["A'BD'", 'ABD', "AC'", "B'CD'"]
['A', 'BC', 'BD']
```

The output uses `'` for complement; the three lines are the seven prime implicants of Example 2.6.1, its minimal expression, and the result of Example 2.5.2, which agree with the hand computation.

The costs of the two steps are very different. The time to find the prime implicants is polynomial in the truth-table size $2^n$: measured on this machine for random functions (each minterm present with probability $1/2$),

| Variables $n$ | Minterms | Prime implicants | Time |
|---|---|---|---|
| 8 | 133 | 128 | < 1 ms |
| 10 | 518 | 605 | 11 ms |
| 12 | 2007 | 2854 | 52 ms |
| 14 | 8185 | 14124 | 0.8 s |

The number of prime implicants itself grows exponentially with $n$ and can reach the order of $3^n/n$ in the worst case (each variable has three states in a product term: uncomplemented, complemented, or absent). The minimum cover of the second step is the set cover problem, which is **NP-hard**; even when the input is the complete truth table, the decision problem of finding a minimal sum of products is **NP-complete** (Masek, 1979). The exhaustive search above is infeasible when there are many prime implicants, so the Q-M method is suitable only for functions with not too many variables. This is a direct example of **time complexity** analysis in circuit design.

Industrial two-level minimization tools (such as Espresso from Berkeley) use a heuristic "expand, irredundant, reduce" iteration, which does not guarantee a minimal result but is much faster. Today logic synthesis for FPGAs and ASICs targets multilevel logic, representing functions by and-inverter graphs (AIGs), BDDs and so on and applying local rewriting (as in the ABC tool) instead of pursuing two-level minimality; FPGAs with a lookup-table structure do not even need minimization down to gates ([Programmable Logic and HDL](/4.9.9)). Hand minimization with Karnaugh maps is still useful: it is a basic skill for understanding circuit structure, analyzing races and hazards, and designing small control logic.

## Summary

| Topic | Key points |
|---|---|
| Operations | AND, OR, NOT; NAND and NOR are each complete; XOR is the parity function |
| Identities | Second distributive law $A + BC = (A+B)(A+C)$; absorption; De Morgan's laws; consensus theorem |
| Rules | Substitution; complementation (swap operations, constants and variables, preserving order); duality (swap only operations and constants) |
| Expansion | $F = AF\vert_{A=1} + \overline{A}F\vert_{A=0}$, the basis of multiplexers and BDDs |
| Canonical forms | $F = \sum m_i = \prod M_j$, with complementary indices, uniquely determined by the truth table |
| Karnaugh maps | **Gray code** ordering makes adjacent cells differ in one variable; circle prime implicants, selecting the essential ones first; use don't-care terms as needed |
| Q-M method | Group by number of $1$s and merge to find prime implicants, then solve the cover table; the latter is the **NP-hard** set cover problem |
