---
title: Regular Expressions and Regular Languages
description: Syntax and semantics of regular expressions, operator precedence and derived operations; comparison with practical regex; the inductive definition of regular languages; methods for designing regular expressions; algebraic laws, the concretization test for laws, and Arden's lemma.
source_hash: 5cd16cd20d26
---

The simplest class of **grammars** (type 3) in Chapter 2 generates the regular languages. This chapter describes these languages from another angle: starting from single symbols and using only three operations, union, concatenation, and **Kleene closure**, we construct languages, and the algebraic expressions we write down are regular expressions. They are the most common way, besides finite automata, to describe regular languages, and they are the mathematical core of the **regular expressions** ([4.2.11](/4.2.11)) familiar to programmers; most constructs of practical regular expressions can be reduced to these three operations. This chapter defines regular expressions and their languages, practices designing expressions for given languages, and then discusses the algebraic laws of regular expressions. Chapter 4 introduces finite automata, and Chapter 5 proves that the two describe the same family of languages.

## 3.1. Regular Expressions

[§1.3](/4.8.1#sec-1.3) defined three operations on languages: union $L \cup M$, concatenation $LM$, and **Kleene closure** $L^*$. Starting from the simplest languages $\varnothing$, $\{\varepsilon\}$, and $\{a\}$ and applying these three operations repeatedly, we can write down many languages. A regular expression is an expression that records such a construction; it has a syntax (how the expression is written) and a semantics (which language it denotes).

**Definition 3.1.1 (Regular Expression)** The **regular expressions** over an alphabet $\Sigma$ are defined inductively as follows:

1. Basis: $\varepsilon$ and $\varnothing$ are regular expressions; for each $a \in \Sigma$, $a$ is a regular expression.
2. Induction: if $E$ and $F$ are regular expressions, then so are $E + F$, $EF$, $E^*$, and $(E)$.

**Definition 3.1.2 (Language of a Regular Expression)** The language $L(E)$ denoted by a regular expression $E$ is defined by induction on the structure of $E$:

$$
\begin{gathered}
L(\varepsilon) = \{\varepsilon\}, \qquad L(\varnothing) = \varnothing, \qquad L(a) = \{a\},\\
L(E + F) = L(E) \cup L(F), \qquad L(EF) = L(E)L(F), \qquad L(E^*) = L(E)^*, \qquad L((E)) = L(E).
\end{gathered}
$$

To reduce parentheses, the precedence of the operations from highest to lowest is: closure $^*$, concatenation, union $+$; operators of the same kind associate from left to right. For example, $01^* + 1$ is $(0(1^*)) + 1$ and denotes $\{1, 0, 01, 011, \dots\}$, whereas $(01)^* + 1$ denotes $\{1, \varepsilon, 01, 0101, \dots\}$.

Common derived notations are $E^+ = EE^*$ (one or more times), $E^? = \varepsilon + E$ (optional), and $E^n = EE \cdots E$ ($n$ copies of $E$ concatenated, $E^0 = \varepsilon$). None of them adds expressive power; they are only abbreviations.

**Example 3.1.1** Let $\Sigma = \{0, 1\}$.

- $(0 + 1)^*$ denotes $\Sigma^*$, and $(0 + 1)^n$ denotes $\Sigma^n$.
- $1^*0(0 + 1)^*$ denotes the strings containing at least one 0: before the first 0 there are only 1s, and after it anything.
- $(0 + 1)^*00(0 + 1)^*$ denotes the strings containing the substring 00.
- $\varnothing^*$ denotes $\{\varepsilon\}$; $0\varnothing$ denotes $\varnothing$.

Practical regular expressions (the notation of libraries such as C++ `<regex>` and Python `re` in [4.2.11](/4.2.11)) correspond to the formal definition here as follows:

- Union: the formal definition writes $E + F$, while the practical notation uses a vertical bar, `a|b`. Note that `+` in the practical notation means "one or more times", that is, the $E^+$ here; the two must not be confused.
- Concatenation and closure: the same notation, `ab` and `a*`.
- Character classes `[abc]`, `[0-9]` and the wildcard `.` are unions of finitely many symbols; for example `[0-9]` is $0 + 1 + \cdots + 9$. Counted repetition `a{2,4}` is $aa(\varepsilon + a)(\varepsilon + a)$, and `?` is $\varepsilon + E$. All of these reduce to the three basic operations, so the expressive power is unchanged.
- The anchors `^` and `$` denote positions in the match; the formal definition asks whether the whole string belongs to the language, which amounts to always adding anchors at both ends (Python's `re.fullmatch`).
- Backreferences (for example `(a*)b\1`, which requires the two runs of $a$ to have equal length) go beyond the regular languages: the language $\{a^n b a^n\}$ described by `(a*)b\1` is not regular (Chapter 6). Matching with backreferences is NP-complete, which is one reason why practical engines generally use backtracking algorithms (matching algorithms are discussed again in Chapter 5).

## 3.2. Regular Languages

**Definition 3.2.1 (Regular Language)** The **regular languages** over an alphabet $\Sigma$ are defined inductively: $\varnothing$, $\{\varepsilon\}$, and each $\{a\}$ ($a \in \Sigma$) are regular languages; if $L$ and $M$ are regular languages, then so are $L \cup M$, $LM$, and $L^*$; and only languages obtained in this way are regular.

Comparing Definitions 3.1.1 and 3.1.2 immediately shows that $L$ is a regular language if and only if there is a **regular expression** $E$ with $L = L(E)$. Every finite language is regular: $\{w_1, \dots, w_k\} = L(w_1 + \cdots + w_k)$, where each $w_i$ is a concatenation of symbols (use $\varnothing$ for the empty language).

The name "regular" comes from the regular events that Kleene introduced in 1951 while studying models of neural networks. Chapters 4 and 5 will prove that these are exactly the languages recognized by finite automata, and the **regular grammars** (type 3) of Chapter 2 also generate exactly this class; the equivalence of the three descriptions is the core of the theory of regular languages.

## 3.3. Designing Regular Expressions

To write a **regular expression** for a language, a common approach is to find the "skeleton" that must appear and then fill the arbitrary parts between the skeleton pieces with closures such as $(0 + 1)^*$; when the conditions are complicated, write each case separately and take the union; positional conditions (the $k$th symbol from the end) are expressed with the fixed-length $(0 + 1)^n$. In all the examples below the **alphabet** is $\{0, 1\}$, and each expression has been checked by program against all strings of length at most 10.

**Example 3.3.1** Strings containing the substring 000: the skeleton is 000 with anything on both sides, $(0 + 1)^*000(0 + 1)^*$. Strings ending in 01: $(0 + 1)^*01$.

**Example 3.3.2** Nonempty strings whose first and last symbols are equal: distinguish the cases where both are 0, both are 1, and length 1:

$$
0(0 + 1)^*0 + 1(0 + 1)^*1 + 0 + 1.
$$
Strings whose first and last symbols differ are $0(0 + 1)^*1 + 1(0 + 1)^*0$, whose length is naturally at least 2.

**Example 3.3.3 (Positional Conditions)** Strings whose fifth symbol from the end is 1: $(0 + 1)^*1(0 + 1)^4$. Strings with at least one 1 among the first five positions: the first 1 occurs at position $k \le 5$, preceded by $k - 1 \le 4$ zeros, and we write $(\varepsilon + 0)$ for "an optional 0":

$$
(\varepsilon + 0)^4 1 (0 + 1)^*.
$$
Here $(\varepsilon + 0)^4$ denotes $\{\varepsilon, 0, 00, 000, 0000\}$; this trick of using $\varepsilon$ to express "at most $k$ times" is very common.

**Example 3.3.4 (Forbidden Substrings)** Strings not containing the substring 11: every 1 must be immediately followed by a 0 unless it is the last symbol. So the string is a concatenation of 0s and 10s, possibly with one extra 1 at the end:

$$
(0 + 10)^*(\varepsilon + 1).
$$

**Example 3.3.5 (Parity of a Count)** Strings with an even number of 0s: cut the string after every second 0; each piece has the form $1^*01^*0$, and a final piece $1^*$ remains, so the expression is $(1^*01^*0)^*1^*$.

**Example 3.3.6** Strings in which every pair of adjacent 00 occurs before any pair of adjacent 11. The technique is to split the string into two parts: the left part allows 00 and contains no 11, and the right part allows 11 and contains no 00. By Example 3.3.4 the left part is $(0 + 10)^*(\varepsilon + 1)$, and symmetrically the right part is $(1 + 01)^*(\varepsilon + 0)$, so

$$
(0 + 10)^*(\varepsilon + 1)(1 + 01)^*(\varepsilon + 0).
$$
For any string satisfying the condition, cutting just before the first 1 of the first 11 gives such a decomposition (if there is no 11, the whole string goes into the left part). Conversely, a new 00 or 11 may appear at the seam of the two parts, but a new 00 must lie before all 11s of the right part, and a new 11 must lie after all 00s of the left part, so the condition still holds.

There is no universal recipe for designing regular expressions. When the conditions interleave (for example "an odd number of occurrences of the substring 01"), it is often more reliable to draw a finite automaton first and then convert it with the algorithms of Chapter 5.

## 3.4. Algebraic Laws of Regular Expressions

Two **regular expressions** $E$ and $F$ are called equivalent, written $E = F$, if $L(E) = L(F)$. Equivalent expressions may replace each other, and an algebraic law is an equation that remains true under any substitution for the subexpressions (regarded as variables) occurring in it.

**Theorem 3.4.1** For any regular expressions $L, M, N$:

| Name | Law |
|---|---|
| Commutativity and associativity of union | $L + M = M + L$, $(L + M) + N = L + (M + N)$ |
| Associativity of concatenation | $(LM)N = L(MN)$ |
| Identities | $\varnothing + L = L$, $\varepsilon L = L\varepsilon = L$ |
| Annihilators | $\varnothing L = L\varnothing = \varnothing$ |
| Distributivity | $L(M + N) = LM + LN$, $(M + N)L = ML + NL$ |
| Idempotence | $L + L = L$ |
| Closure | $(L^*)^* = L^*$, $\varnothing^* = \varepsilon$, $\varepsilon^* = \varepsilon$, $L^+ = LL^* = L^*L$, $L^* = L^+ + \varepsilon$ |

Concatenation is not commutative in general: $01 \ne 10$. Some of these laws come directly from properties of set operations (commutativity, associativity, and idempotence of union), others from concatenation of strings (identities, associativity). Take distributivity as an example:

**Proof** (left distributivity) $w \in L(L(M + N))$ if and only if $w = xy$ with $x \in L(L)$ and $y \in L(M) \cup L(N)$; if and only if $w = xy$ with $x \in L(L)$ and $y \in L(M)$, or $x \in L(L)$ and $y \in L(N)$; if and only if $w \in L(LM) \cup L(LN)$. $\square$

Proving laws one by one like this is tedious, and for a conjectured equation one often first needs to decide whether it is true at all. The next theorem reduces "holds for all languages" to "holds for one concrete expression".

**Theorem 3.4.2 (Concretization Test)** Let $E$ and $F$ be regular expressions with variables $L_1, \dots, L_m$. Replace each $L_i$ by a distinct new symbol $a_i$, obtaining variable-free concrete expressions $C$ and $D$. Then $E = F$ holds for all languages $L_1, \dots, L_m$ if and only if $L(C) = L(D)$.

**Proof** Substitute an arbitrary tuple of languages $S_1, \dots, S_m$ for the variables. Define $\sigma(a_i) = S_i$, extend it to strings by $\sigma(\varepsilon) = \{\varepsilon\}$ and $\sigma(xy) = \sigma(x)\sigma(y)$, and then to languages by $\sigma(K) = \bigcup_{x \in K}\sigma(x)$. We first prove that after the substitution the language of $E$ equals $\sigma(L(C))$, by induction on the structure of $E$. For $E$ equal to $\varepsilon$ or $\varnothing$ this is obvious; for $E = L_i$ both sides are $S_i$. For $E = E_1 + E_2$, $\sigma$ preserves unions, $\sigma(L(C_1) \cup L(C_2)) = \sigma(L(C_1)) \cup \sigma(L(C_2))$; for $E = E_1E_2$, $\sigma(xy) = \sigma(x)\sigma(y)$ gives $\sigma(L(C_1)L(C_2)) = \sigma(L(C_1))\sigma(L(C_2))$; for $E = E_1^*$ similarly $\sigma(L(C_1)^*) = \sigma(L(C_1))^*$. The claim follows from the induction hypothesis.

Hence if $L(C) = L(D)$, then for any substitution the languages of $E$ and $F$ both equal $\sigma(L(C)) = \sigma(L(D))$, and the law holds. Conversely, if the law holds for all languages, take $S_i = \{a_i\}$; then $\sigma$ is the identity, and $L(C) = L(D)$. $\square$

**Example 3.4.1**

- Verify $(L + M)^* = (L^*M^*)^*$: concretized, $(a + b)^* = (a^*b^*)^*$; both sides are the set of all strings over $\{a, b\}$, so the law holds.
- Verify $LL^* = L^*L$: $aa^*$ and $a^*a$ both denote $\{a^n \mid n \ge 1\}$, so it holds.
- Test $L + ML = (L + M)L$: concretized, $a + ba$ and $(a + b)a$; $aa \in L((a + b)a)$ but $aa \notin L(a + ba)$, so this is not a law.

By Chapter 6, whether two variable-free regular expressions are equivalent is decidable, so Theorem 3.4.2 gives an algorithm for deciding any candidate law. Note that the method applies only to expressions built from union, concatenation, and closure; if intersection is introduced, the concretization test fails. For example, $L \cap M \cap N = L \cap M$ becomes $\varnothing = \varnothing$ after concretization, yet it is clearly not a law.

**Theorem 3.4.3 (Arden's Lemma)** Let $A$ and $B$ be languages with $\varepsilon \notin A$. Then the equation $X = AX \cup B$ has the unique solution $X = A^*B$.

**Proof** $A^*B$ is a solution: $A(A^*B) \cup B = (A^+ \cup \{\varepsilon\})B = A^*B$. Let $X$ be any solution. Repeated substitution gives $X = A^{n+1}X \cup (A^n \cup \cdots \cup A \cup \{\varepsilon\})B$ for all $n$, so $A^*B \subseteq X$. Conversely, take any $w \in X$ and let $n = \lvert w\rvert$: since $\varepsilon \notin A$, the strings in $A^{n+1}X$ have length at least $n + 1$, so $w$ is not among them and must belong to $(A^n \cup \cdots \cup \{\varepsilon\})B \subseteq A^*B$. $\square$

Arden's lemma is the basis of another method for converting finite automata into regular expressions: introduce an unknown language $X_q$ for each state $q$ (the strings leading from $q$ to an accepting state), write a system of linear equations according to the transitions, and eliminate the unknowns one by one with Arden's lemma (Chapter 5).

## Summary

| Topic | Key points |
|---|---|
| Regular expressions (Definitions 3.1.1, 3.1.2) | Built inductively from $\varepsilon$, $\varnothing$, $a$ by union $+$, concatenation and closure $^*$; precedence: closure > concatenation > union; $E^+$, $E^?$, $E^n$ are abbreviations |
| Practical regexes | The bar in `a\|b` is union and `+` is $E^+$; character classes and counted repetition reduce to the three basic operations; backreferences go beyond regular languages |
| Regular languages (Definition 3.2.1) | The languages obtained from the basic languages by union, concatenation and closure, exactly those denoted by regular expressions; every finite language is regular |
| Design techniques | Find the skeleton and fill both sides (Example 3.3.1), union of cases (Example 3.3.2), positional conditions (Example 3.3.3), forbidden substrings (Example 3.3.4), cutting by counts (Example 3.3.5), splitting the string into a left and a right part (Example 3.3.6) |
| Algebraic laws (Theorem 3.4.1) | Commutativity, associativity and idempotence of union; associativity and distributivity of concatenation; identities $\varnothing$, $\varepsilon$ and annihilator $\varnothing$; closure laws; concatenation is not commutative |
| Concretization test (Theorem 3.4.2) | Replace the variables by distinct symbols: a candidate law holds if and only if the concrete expressions are equivalent; fails for expressions with intersection |
| Arden's lemma (Theorem 3.4.3) | If $\varepsilon \notin A$, the unique solution of $X = AX \cup B$ is $A^*B$; used to convert automata into regular expressions |

## Questions

1. Write regular expressions for the following languages (alphabet $\{0, 1\}$): (1) every 0 is immediately followed by at least one 1; (2) the number of 0s is divisible by 3; (3) at least three 1s, and the third symbol from the end is 1; (4) even length and no substring 00.
2. Simplify: $(\varepsilon + 1)(\varepsilon + 1)^*$, $\varnothing^* + 0^*$, $(0^*1^*)^*0$.
3. Use the concretization test to decide whether each of the following equations is a law: (1) $(L^*)^* = L^*$; (2) $(LM)^* = L^*M^*$; (3) $(L + M)^* = L^*(ML^*)^*$; (4) $L^*M = M + L^*LM$.
4. Prove that when $\varepsilon \in A$, the solution in Arden's lemma is not unique.
