---
title: Limits
source_hash: 12c6ed7419ee
---

The limit is the basic language of calculus: a derivative is the limit of difference quotients, a definite integral is the limit of sums, and the sum of a series is the limit of its partial sums. This chapter begins with the simplest case, the limit of a sequence, and uses the $\varepsilon$-$N$ language to make "arbitrarily close" precise; it establishes the properties of limits, the arithmetic rules and several existence theorems (the squeeze theorem, the monotone convergence theorem and the Cauchy criterion). It then extends these results to the six kinds of limit processes for functions and proves the two fundamental limits. Finally, it compares how fast limit processes proceed by means of orders of infinitesimals, which leads to the most commonly used technique for computing limits, the substitution of equivalent infinitesimals.

This chapter relies on the **least-upper-bound property** (from which the monotone convergence theorem follows) and on the **punctured neighborhood**, both from [Chapter 1](/2.2.1). The proof of sufficiency in the Cauchy criterion requires the Bolzano–Weierstrass theorem and is deferred to [Chapter 3](/2.2.3#sec-3.2). The various modes of convergence of sequences of random variables in probability theory ([3.1](/3.1)) are all built on the limits of sequences studied here.

## 2.1. Definition and Properties of Limits of Sequences

### 2.1.1. Definition of the Limit of a Sequence

**Definition 2.1.1 (Sequence)** A list of numbers $a_1, a_2, \dots, a_n, \dots$ indexed by the positive integers in order is called a **sequence**, written $\{a_n\}$ for short; $a_n$ is called the general term. A sequence may be regarded as a function $f(n) = a_n$ defined on $\mathbb{N}_+$.

Consider how the following sequences behave as $n$ grows:

$$
a_n = \frac{(-1)^n}{n}, \qquad b_n = \frac{n - 1}{n}, \qquad c_n = 2^n, \qquad d_n = \frac{(-1)^{n+1}}{\sqrt n}.
$$
The terms $a_n$ and $d_n$ get arbitrarily close to $0$, $b_n$ gets arbitrarily close to $1$, and $c_n$ grows without bound. "Arbitrarily close" must not be read as "closer and closer": the distance from $a_n$ to $0$ decreases monotonically, while $d_n$ jumps from one side of $0$ to the other, yet both approach $0$. The precise meaning of "$a_n$ gets arbitrarily close to $A$" is that the distance $|a_n - A|$ can be made as small as we please: however small a positive number $\varepsilon$ is given (say one ten-thousandth), from some term on, all terms lie within distance $\varepsilon$ of $A$.

**Definition 2.1.2 (Limit of a Sequence)** Let $\{a_n\}$ be a sequence and $A$ a constant. If for every $\varepsilon > 0$ there exists $N \in \mathbb{N}_+$ such that

$$
|a_n - A| < \varepsilon
$$
whenever $n > N$, then $A$ is called the limit of the sequence $\{a_n\}$, written $\lim\limits_{n \to \infty} a_n = A$ or $a_n \to A$ ($n \to \infty$), and the sequence $\{a_n\}$ is said to converge to $A$. A sequence that has no limit is called a **divergent sequence**.

- $\varepsilon$ is arbitrary, and $N$ depends on $\varepsilon$ but is not unique: it suffices to find one $N$ that works, and then every larger $N$ works as well.
- Geometric meaning: however small $\varepsilon > 0$ is, all terms from the $(N + 1)$-th on lie in the neighborhood $N(A, \varepsilon)$, and only finitely many terms lie outside it.
- Contrast with a limit point: that every neighborhood of $A$ contains infinitely many terms of the sequence does not guarantee $a_n \to A$. For example, the subsequences of $(-1)^n$ tend to $1$ and $-1$, every neighborhood of $\pm1$ contains infinitely many terms, and yet the sequence diverges. The limit requires that only finitely many terms lie outside the neighborhood.
- In the definition, $\varepsilon > 0$ may be restricted to values in $(0, 1)$; $|a_n - A| < \varepsilon$ may be replaced by $|a_n - A| < M\varepsilon$ ($M$ a positive constant) or by $|a_n - A| \leq \varepsilon$; and $n > N$ may be replaced by $n \geq N$. All of these variants are equivalent to the original definition.

![Geometric meaning of the ε-N definition: for n > N, all terms of the sequence a_n = 1 + (-1)^n/n lie in the band (1 − ε, 1 + ε); the smaller ε is, the larger N must be.](./plots/epsilon-n-band.py)

**Algorithm 2.1.1 (Verifying the Limit of a Sequence from the Definition)** To verify $\lim\limits_{n \to \infty} a_n = A$:

1. Given $\varepsilon > 0$, transform $|a_n - A|$ and enlarge it suitably to obtain a simple upper bound $g(n)$ that decreases monotonically to $0$ as $n$ grows, so that $|a_n - A| \leq g(n)$ (when enlarging, one may first assume that $n$ exceeds some fixed number);
2. Solve the inequality $g(n) < \varepsilon$ to obtain a sufficient condition $n > X(\varepsilon)$;
3. Take $N = \lfloor X \rfloor$ (or any larger positive integer); then $|a_n - A| \leq g(n) < \varepsilon$ for $n > N$.

Finding $N$ is not the same as solving the inequality $|a_n - A| < \varepsilon$: only a sufficient condition is needed, and enlarging is precisely what makes the inequality easy to solve.

**Example 2.1.1** Prove that $\lim\limits_{n \to \infty} \frac{2n + 1}{n + 1} = 2$ and $\lim\limits_{n \to \infty} \frac{2n^2 + 1}{n^2 + 2n - 1} = 2$.

**Proof** First limit: $\left|\frac{2n+1}{n+1} - 2\right| = \frac{1}{n+1} < \frac1n$. Given $\varepsilon > 0$, take $N = \left\lfloor \frac1\varepsilon \right\rfloor$; then $\frac1n < \varepsilon$ for $n > N$. Second limit: for $n \geq 1$ we have $n^2 + 2n - 1 \geq n^2$, so

$$
\left|\frac{2n^2 + 1}{n^2 + 2n - 1} - 2\right| = \frac{4n - 3}{n^2 + 2n - 1} < \frac{4n}{n^2} = \frac4n,
$$
and $N = \left\lfloor \frac4\varepsilon \right\rfloor$ works. $\square$

**Example 2.1.2** Prove that $\lim\limits_{n \to \infty} q^n = 0$ ($|q| < 1$).

**Proof** The case $q = 0$ is obvious. Let $0 < |q| < 1$ and $\varepsilon \in (0, 1)$. Then $|q^n - 0| = |q|^n < \varepsilon \iff n\ln|q| < \ln\varepsilon \iff n > \frac{\ln\varepsilon}{\ln|q|}$ (note that $\ln|q| < 0$). Take $N = \left\lfloor \frac{\ln\varepsilon}{\ln|q|} \right\rfloor$. $\square$

**Example 2.1.3** Let $a > 1$. Prove that $\lim\limits_{n \to \infty} \sqrt[n]{a} = 1$.

**Proof** We have $a - 1 = \bigl(\sqrt[n]a - 1\bigr)\bigl(1 + a^{1/n} + a^{2/n} + \cdots + a^{(n-1)/n}\bigr)$, and every term in the second factor is $\geq 1$, so

$$
0 < \sqrt[n]a - 1 \leq \frac{a - 1}{n}.
$$
Given $\varepsilon > 0$, take $N = \left\lfloor \frac{a - 1}{\varepsilon} \right\rfloor$. For $0 < a < 1$, apply this result to $\frac1a$ and take reciprocals (see §2.2.1 for the arithmetic rules). $\square$

**Example 2.1.4** Prove that $\lim\limits_{n \to \infty} \sqrt[n]{n} = 1$.

**Proof** Write $\sqrt[n]n = 1 + t_n$ with $t_n \geq 0$. By the binomial theorem, for $n \geq 2$,

$$
n = (1 + t_n)^n \geq \binom n2 t_n^2 = \frac{n(n-1)}{2}t_n^2, \quad\text{so}\quad 0 \leq t_n \leq \sqrt{\frac{2}{n - 1}}.
$$
Given $\varepsilon > 0$, the inequality $\sqrt{\frac2{n-1}} < \varepsilon$ holds as soon as $n > \frac2{\varepsilon^2} + 1$, so take $N = \left\lfloor \frac2{\varepsilon^2} \right\rfloor + 1$. $\square$

**Example 2.1.5** Let $a > 1$. Prove that $\lim\limits_{n \to \infty} \frac{n}{a^n} = 0$.

**Proof** Write $a = 1 + b$ with $b > 0$. For $n \geq 2$, $a^n \geq \binom n2 b^2$, so $0 < \frac{n}{a^n} \leq \frac{2}{(n - 1)b^2}$; take $N = \left\lfloor \frac{2}{\varepsilon b^2} \right\rfloor + 1$. $\square$

The same method (expanding up to the $b^{k+1}$ term) proves $\lim\limits_{n \to \infty} \frac{n^k}{a^n} = 0$ ($a > 1$, $k \in \mathbb{N}_+$): exponential growth beats any polynomial growth. Examples 2.1.2–2.1.5 give the four most frequently used basic limits:

$$
\lim_{n \to \infty} q^n = 0 \ (|q| < 1), \qquad \lim_{n \to \infty} \sqrt[n]a = 1 \ (a > 0), \qquad \lim_{n \to \infty} \sqrt[n]n = 1, \qquad \lim_{n \to \infty} \frac{n^k}{a^n} = 0 \ (a > 1).
$$

**Example 2.1.6** Prove that $\lim\limits_{n \to \infty} \arctan n = \frac\pi2$.

**Proof** Let $\varepsilon \in (0, 1)$. The inequality $\left|\arctan n - \frac\pi2\right| = \frac\pi2 - \arctan n < \varepsilon$ is equivalent to $\tan\left(\frac\pi2 - \arctan n\right) < \tan\varepsilon$, that is, $\cot(\arctan n) = \frac1n < \tan\varepsilon$. Take $N = \left\lfloor \frac1{\tan\varepsilon} \right\rfloor$. $\square$

Similarly, $\lim\limits_{n \to \infty} \arctan(-n) = -\frac\pi2$, $\lim\limits_{n \to \infty} \operatorname{arccot} n = 0$ and $\lim\limits_{n \to \infty} \operatorname{arccot}(-n) = \pi$.

The definition immediately yields the following equivalences, which reduce a general limit problem to a problem of "tending to $0$":

$$
\lim_{n \to \infty} a_n = 0 \iff \lim_{n \to \infty} |a_n| = 0; \qquad
\lim_{n \to \infty} a_n = A \iff \lim_{n \to \infty} (a_n - A) = 0 \iff \lim_{n \to \infty} |a_n - A| = 0.
$$

**Example 2.1.7** If $\lim\limits_{n \to \infty} a_n = A$, then $\lim\limits_{n \to \infty} \frac{a_1 + a_2 + \cdots + a_n}{n} = A$.

**Proof** Let $b_n = a_n - A$. Then $b_n \to 0$ and $\frac{a_1 + \cdots + a_n}{n} - A = \frac{b_1 + \cdots + b_n}{n}$, so it suffices to treat the case $A = 0$. Given $\varepsilon > 0$, there exists $N_1$ such that $|b_n| < \varepsilon$ for $n > N_1$. Hence, for $n > N_1$,

$$
\left|\frac{b_1 + \cdots + b_n}{n}\right| \leq \frac{|b_1 + \cdots + b_{N_1}|}{n} + \frac{n - N_1}{n}\varepsilon < \frac{|b_1 + \cdots + b_{N_1}|}{n} + \varepsilon.
$$
Once $N_1$ is fixed, the numerator of the first term is a constant, so there exists $N_2$ such that the first term is less than $\varepsilon$ for $n > N_2$. With $N = \max\{N_1, N_2\}$, the expression is less than $2\varepsilon$ for $n > N$. $\square$

The "split estimate" in this proof is a common technique: the first finitely many terms are controlled because their numerator is fixed while the denominator tends to infinity, and the remaining terms are controlled by the definition of the limit. The converse fails: $a_n = (-1)^n$ diverges, yet its arithmetic means tend to $0$.

### 2.1.2. Properties of Limits of Sequences

**Theorem 2.1.1 (Uniqueness)** The limit of a convergent sequence is unique.

**Proof** Suppose $a_n \to A$, $a_n \to B$ and $A \ne B$. Take $\varepsilon = \frac12|A - B| > 0$. There exist $N_1, N_2$ such that $|a_n - A| < \varepsilon$ for $n > N_1$ and $|a_n - B| < \varepsilon$ for $n > N_2$. For $n > \max\{N_1, N_2\}$,

$$
|A - B| \leq |a_n - A| + |a_n - B| < 2\varepsilon = |A - B|,
$$
a contradiction. $\square$

**Theorem 2.1.2 (Boundedness)** A convergent sequence is bounded: if $\lim\limits_{n \to \infty} a_n = A$, then there exists $M > 0$ such that $|a_n| \leq M$ for all $n \in \mathbb{N}_+$.

**Proof** For $\varepsilon = 1$ there exists $N$ such that $|a_n - A| < 1$, hence $|a_n| < |A| + 1$, for $n > N$. Let $M = \max\{|a_1|, \dots, |a_N|, |A| + 1\}$. $\square$

Boundedness is necessary but not sufficient for convergence: $(-1)^n$ is bounded but divergent.

**Theorem 2.1.3 (Finitely Many Terms Do Not Matter)** Adding, deleting or changing finitely many terms of a sequence changes neither its convergence nor its limit.

The limit of a sequence describes the behavior of the terms for large $n$, so when discussing convergence we may consider only "sufficiently large $n$."

**Theorem 2.1.4 (Sign Preservation)** Let $\lim\limits_{n \to \infty} a_n = A$.

1. If $A > 0$ ($A < 0$), then $a_n > 0$ ($a_n < 0$) for all sufficiently large $n$;
2. If $a_n \geq 0$ ($a_n \leq 0$) for all sufficiently large $n$, then $A \geq 0$ ($A \leq 0$).

**Proof** 1. Let $A > 0$ and take $\varepsilon = \frac A2$. There exists $N$ such that $|a_n - A| < \frac A2$ for $n > N$, whence $a_n > A - \frac A2 = \frac A2 > 0$. 2. This is the contrapositive of 1. $\square$

In conclusion 2, $\geq$ cannot be replaced by $>$: $a_n = \frac1n > 0$, but the limit $0$ is not positive. Passing to the limit may turn a strict inequality into an equality.

**Theorem 2.1.5 (Order Preservation)** Let $\lim\limits_{n \to \infty} a_n = A$ and $\lim\limits_{n \to \infty} b_n = B$.

1. If there exists $N$ such that $a_n \leq b_n$ for all $n > N$, then $A \leq B$;
2. If $A < B$, then there exists $N$ such that $a_n < b_n$ for all $n > N$;
3. If $A < B$, then there exists $N$ such that $a_n < B$ for all $n > N$.

**Proof** Applying Theorem 2.1.4 to $b_n - a_n \to B - A$ (for the arithmetic rules see Theorem 2.2.1) gives 1 and 2; taking $b_n \equiv B$ in 2 gives 3. $\square$

### 2.1.3. Subsequences

**Definition 2.1.3 (Subsequence)** Let $\{a_n\}$ be a sequence and let $n_1 < n_2 < \cdots < n_j < \cdots$ be a strictly increasing sequence of positive integers. The sequence $\{a_{n_j}\}_{j=1}^\infty$ is called a **subsequence** of $\{a_n\}$.

A subsequence has two features: it contains infinitely many terms of the original sequence, and it keeps their original order. Since $n_j$ is strictly increasing, $n_j \geq j$.

**Theorem 2.1.6** $\lim\limits_{n \to \infty} a_n = A$ if and only if every subsequence of $\{a_n\}$ converges and has limit $A$.

**Proof** Necessity: given $\varepsilon > 0$, there exists $N$ such that $|a_n - A| < \varepsilon$ for $n > N$. For any subsequence and $j > N$, we have $n_j \geq j > N$, so $|a_{n_j} - A| < \varepsilon$. Sufficiency: $\{a_n\}$ is a subsequence of itself. $\square$

Negating the definition shows what the theorem is good for:

$$
\lim_{n \to \infty} a_n \ne A \iff \exists \varepsilon_0 > 0,\ \text{there is a subsequence } \{a_{n_j}\} \text{ with } |a_{n_j} - A| \geq \varepsilon_0 \ (j = 1, 2, \dots),
$$
that is, infinitely many terms lie outside $N(A, \varepsilon_0)$. Theorem 2.1.6 is therefore often used to prove divergence: exhibit two subsequences with different limits, or one divergent subsequence.

**Example 2.1.8** $a_n = \cos(n\pi) = (-1)^n$ diverges: $a_{2k} = 1 \to 1$ and $a_{2k+1} = -1 \to -1$.

**Theorem 2.1.7** $\lim\limits_{n \to \infty} a_n = A$ if and only if $\lim\limits_{k \to \infty} a_{2k} = A$ and $\lim\limits_{k \to \infty} a_{2k+1} = A$.

**Proof** Necessity follows from Theorem 2.1.6. Sufficiency: given $\varepsilon > 0$, there exist $K_1$ with $|a_{2k} - A| < \varepsilon$ for $k > K_1$ and $K_2$ with $|a_{2k+1} - A| < \varepsilon$ for $k > K_2$. Let $N = 2\max\{K_1, K_2\} + 1$. Then $|a_n - A| < \varepsilon$ for every $n > N$, whether $n$ is even or odd. $\square$

### 2.1.4. Infinitesimals, Infinitely Large Quantities and Unbounded Sequences

**Definition 2.1.4 (Infinitesimal)** If $\lim\limits_{n \to \infty} a_n = 0$, then $\{a_n\}$ is called an **infinitesimal** (an infinitesimal sequence).

For example, $\frac1n$ and $q^n$ ($|q| < 1$) are infinitesimals. An infinitesimal is a sequence tending to $0$, not a "very small number."

**Definition 2.1.5 (Infinitely Large Quantity)** If for every $M > 0$ there exists $N \in \mathbb{N}_+$ such that $|a_n| > M$ for all $n > N$, then $\{a_n\}$ is called an **infinitely large quantity** (an infinitely large sequence), written $a_n \to \infty$ ($n \to \infty$). If $|a_n| > M$ is replaced by $a_n > M$ ($a_n < -M$), then $\{a_n\}$ is said to tend to positive (negative) infinity, written $a_n \to +\infty$ ($-\infty$).

For example, $n + 1 \to +\infty$, $-n^2 \to -\infty$ and $(-1)^n n \to \infty$. An infinitely large sequence is divergent; the notation $\lim a_n = \infty$ merely indicates a particular way of diverging. If $a_n \ne 0$, then

$$
\{a_n\} \text{ is infinitely large} \iff \left\{\frac1{a_n}\right\} \text{ is an infinitesimal},
$$
because $|a_n| > M$ is equivalent to $\left|\frac1{a_n}\right| < \frac1M$, and $M$ being arbitrarily large is the same as $\frac1M$ being arbitrarily small.

**Definition 2.1.6 (Unbounded Sequence)** If for every $M > 0$ there is some term $a_k$ with $|a_k| > M$, then $\{a_n\}$ is called an **unbounded sequence**.

An infinitely large sequence requires all terms with $n > N$ to exceed $M$ in absolute value; an unbounded sequence requires only some term to do so. Hence every infinitely large sequence is unbounded, but not conversely: the sequence $a_n = n + (-1)^n n$, whose even terms are $2n$ and odd terms are $0$, and the sequence $b_n = n^{(-1)^n}$, whose even terms are $n$ and odd terms are $\frac1n$, are both unbounded but not infinitely large. One can show that every unbounded sequence has a subsequence tending to $\infty$ (choose successively terms with $|a_{n_j}| > j$ and $n_j > n_{j-1}$).

## 2.2. Arithmetic of Limits of Sequences and Sufficient Conditions for Existence

### 2.2.1. Arithmetic Rules for Limits of Sequences

**Theorem 2.2.1 (Arithmetic Rules)** Let $\lim\limits_{n \to \infty} a_n = A$ and $\lim\limits_{n \to \infty} b_n = B$. Then

1. $\lim\limits_{n \to \infty} c\,a_n = cA$ ($c$ a constant);
2. $\lim\limits_{n \to \infty} (a_n \pm b_n) = A \pm B$;
3. $\lim\limits_{n \to \infty} a_nb_n = AB$;
4. $\lim\limits_{n \to \infty} \frac{a_n}{b_n} = \frac AB$ ($B \ne 0$);
5. $\lim\limits_{n \to \infty} a_n^m = A^m$ ($m \in \mathbb{Z}$; for $m < 0$ we require $A \ne 0$);
6. $\lim\limits_{n \to \infty} \sqrt[m]{a_n} = \sqrt[m]{A}$ ($m \in \mathbb{N}_+$; for even $m$ we require $a_n \geq 0$).

**Proof** 3. By Theorem 2.1.2 there exists $M > 0$ with $|a_n| \leq M$. Given $\varepsilon > 0$, there exists $N$ such that for $n > N$

$$
|a_n - A| < \frac{\varepsilon}{2(1 + |B|)}, \qquad |b_n - B| < \frac{\varepsilon}{2M},
$$
and hence

$$
|a_nb_n - AB| \leq |a_n|\,|b_n - B| + |B|\,|a_n - A| < M \cdot \frac{\varepsilon}{2M} + |B| \cdot \frac{\varepsilon}{2(1 + |B|)} < \varepsilon.
$$
The denominator is $1 + |B|$ rather than $|B|$ so that the argument also works when $B = 0$.

4. By 3, it suffices to show $\frac1{b_n} \to \frac1B$. As in the proof of sign preservation, $|b_n| > \frac{|B|}2$ for sufficiently large $n$, so $\left|\frac1{b_n} - \frac1B\right| = \frac{|b_n - B|}{|b_n|\,|B|} < \frac{2}{B^2}|b_n - B|$, which can be made arbitrarily small.

6. Let $A > 0$ (the case $A = 0$ follows directly from the definition, and for $A < 0$ with $m$ odd consider $-a_n$); by sign preservation we may assume $a_n > 0$. Using $x^m - y^m = (x - y)(x^{m-1} + x^{m-2}y + \cdots + y^{m-1})$,

$$
\left|\sqrt[m]{a_n} - \sqrt[m]{A}\right| = \frac{|a_n - A|}{a_n^{\frac{m-1}m} + a_n^{\frac{m-2}m}A^{\frac1m} + \cdots + A^{\frac{m-1}m}} \leq \frac{|a_n - A|}{A^{\frac{m-1}m}},
$$
and the right-hand side tends to $0$. Parts 1, 2 and 5 are similar. $\square$

Note that the theorem assumes that both $\{a_n\}$ and $\{b_n\}$ converge. Convergence of $a_n \pm b_n$ does not imply that $a_n$ and $b_n$ converge separately; and a sum whose number of terms grows with $n$ (such as $\sum_{k=1}^n \frac{1}{n^2 + k}$) cannot be handled by taking limits term by term.

**Example 2.2.1 (Limits of Rational Expressions)** Let $a_0 \ne 0$, $b_0 \ne 0$ and $k, l \in \mathbb{N}$. Then

$$
\lim_{n \to \infty} \frac{a_0n^k + a_1n^{k-1} + \cdots + a_k}{b_0n^l + b_1n^{l-1} + \cdots + b_l} = \begin{cases} \dfrac{a_0}{b_0}, & k = l, \\[1ex] 0, & k < l, \\[0.5ex] \infty, & k > l. \end{cases}
$$
Divide numerator and denominator by $n^{\max\{k, l\}}$ and use $\frac1{n^j} \to 0$ together with the arithmetic rules. For example, $\lim\limits_{n \to \infty} \frac{n^2 - n + 1}{2n^2 + 3n - 2} = \lim\limits_{n \to \infty} \frac{1 - \frac1n + \frac1{n^2}}{2 + \frac3n - \frac2{n^2}} = \frac12$.

**Example 2.2.2** Find the limits:

$$
\text{(1)}\ \lim_{n \to \infty} \Bigl(1 - \frac1{2^2}\Bigr)\Bigl(1 - \frac1{3^2}\Bigr)\cdots\Bigl(1 - \frac1{n^2}\Bigr); \qquad
\text{(2)}\ \lim_{n \to \infty} \frac{5^n + 4^n}{5^{n+1} + 4^{n+1}}; \qquad
\text{(3)}\ \lim_{n \to \infty} \frac{1 + a + \cdots + a^n}{1 + b + \cdots + b^n} \ (|a|, |b| < 1).
$$

**Solution** (1) $1 - \frac1{k^2} = \frac{(k-1)(k+1)}{k \cdot k}$; in the product, adjacent factors cancel, leaving $\frac12 \cdot \frac{n+1}{n} \to \frac12$. (2) Dividing numerator and denominator by $5^n$ gives $\frac{1 + (4/5)^n}{5 + 4(4/5)^n} \to \frac15$. (3) By the formula for geometric sums, the numerator equals $\frac{1 - a^{n+1}}{1 - a} \to \frac1{1-a}$ and the denominator tends to $\frac1{1-b}$, so the limit is $\frac{1 - b}{1 - a}$.

### 2.2.2. Sufficient Conditions for the Existence of Limits of Sequences

So far we have either guessed the limit $A$ and then verified it, or obtained it from known limits by the arithmetic rules. For many sequences, such as $\left(1 + \frac1n\right)^n$, there is no way to guess the limit in advance, and we need criteria for existence that do not involve the value of the limit.

#### 2.2.2.1. The Squeeze Theorem

**Theorem 2.2.2 (Squeeze Theorem)** Let the sequences $\{a_n\}$, $\{b_n\}$, $\{c_n\}$ satisfy $a_n \leq b_n \leq c_n$ (for sufficiently large $n$) and $\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} c_n = A$. Then $\lim\limits_{n \to \infty} b_n = A$.

**Proof** From $a_n - A \leq b_n - A \leq c_n - A$ we get $|b_n - A| \leq \max\{|a_n - A|, |c_n - A|\}$. Given $\varepsilon > 0$, there exists $N$ such that $|a_n - A| < \varepsilon$ and $|c_n - A| < \varepsilon$ for $n > N$, and then $|b_n - A| < \varepsilon$. $\square$

**Example 2.2.3** Find the limits of the following sequences:

$$
\text{(1)}\ x_n = \sqrt{n + 1} - \sqrt n; \quad \text{(2)}\ x_n = \sum_{k=1}^n \frac{1}{n^2 + k}; \quad \text{(3)}\ x_n = \frac{5^n}{n!}; \quad \text{(4)}\ x_n = \sqrt[n]{a_1^n + a_2^n + \cdots + a_m^n} \ (a_i > 0).
$$

**Solution** (1) $0 < x_n = \frac{1}{\sqrt{n+1} + \sqrt n} < \frac1{\sqrt n} \to 0$, so $x_n \to 0$.

(2) Each term lies between $\frac1{n^2 + n}$ and $\frac1{n^2 + 1}$, so $\frac{n}{n^2 + n} \leq x_n \leq \frac{n}{n^2 + 1}$; both bounds tend to $0$, so $x_n \to 0$.

(3) From $(n!)^2 = \prod_{k=1}^n k(n + 1 - k) \geq n^n$ (each factor satisfies $k(n+1-k) \geq n$) we get $n! \geq n^{n/2}$, so $0 < x_n \leq \frac{5^n}{n^{n/2}} = \left(\frac{25}{n}\right)^{n/2}$; for $n > 50$ the right-hand side is $\leq 2^{-n/2} \to 0$, so $x_n \to 0$.

(4) Let $a = \max\{a_1, \dots, a_m\}$. Then $a^n \leq a_1^n + \cdots + a_m^n \leq m a^n$, so $a \leq x_n \leq \sqrt[n]m\, a$. By Example 2.1.3, $\sqrt[n]m \to 1$, hence $x_n \to a = \max\{a_1, \dots, a_m\}$.

**Example 2.2.4** Let $a_n > 0$ and $\lim\limits_{n \to \infty} \frac{a_{n+1}}{a_n} = q < 1$. Then $\lim\limits_{n \to \infty} a_n = 0$.

**Proof** Choose $\varepsilon_0 > 0$ such that $r = q + \varepsilon_0 < 1$. There exists $N$ such that $\frac{a_{n+1}}{a_n} < r$ for $n \geq N$, so for $n > N$ we have $0 < a_n < r a_{n-1} < \cdots < r^{n-N}a_N$. The right-hand side equals $\frac{a_N}{r^N} r^n \to 0$, and by the squeeze theorem $a_n \to 0$. $\square$

This immediately gives $\frac{n^k}{a^n} \to 0$ ($a > 1$), $\frac{a^n}{n!} \to 0$ and similar results, since the ratios tend to $\frac1a$ and $0$, respectively. This is the germ of the ratio test in [Chapter 8](/2.2.8).

**Example 2.2.5** Find the area $S$ of the region $D$ bounded by the curve $y = x^2$, the line $x = 1$ and the $x$-axis.

**Solution** Divide $[0, 1]$ into $n$ equal parts. On the $k$-th subinterval $\left[\frac{k-1}n, \frac kn\right]$, the area $S_k$ of the thin strip lies between the areas of two rectangles: $\frac1n\left(\frac{k-1}n\right)^2 \leq S_k \leq \frac1n\left(\frac kn\right)^2$. Summing and using $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}6$,

$$
\frac{(n - 1)n(2n - 1)}{6n^3} \leq S \leq \frac{n(n + 1)(2n + 1)}{6n^3}.
$$
Both bounds tend to $\frac13$, so by the squeeze theorem ($S$ being a constant) $S = \frac13$. This is exactly the idea behind the definite integral $\int_0^1 x^2\,\mathrm{d}x$ of [Chapter 7](/2.2.7).

#### 2.2.2.2. The Monotone Convergence Theorem

**Theorem 2.2.3 (Monotone Convergence Theorem)** Every bounded monotonic sequence converges. More precisely:

1. If $\{a_n\}$ is nondecreasing and bounded above, then $\lim\limits_{n \to \infty} a_n = \sup\{a_n\}$;
2. If $\{a_n\}$ is nonincreasing and bounded below, then $\lim\limits_{n \to \infty} a_n = \inf\{a_n\}$.

**Proof** We prove only 1. By the **least-upper-bound property**, $A = \sup\{a_n\}$ exists. Given $\varepsilon > 0$, by the characterization of suprema (Theorem 1.1.4) there exists $N$ with $a_N > A - \varepsilon$. Since $\{a_n\}$ is nondecreasing, $A - \varepsilon < a_N \leq a_n \leq A$ for all $n > N$, that is, $|a_n - A| < \varepsilon$. $\square$

The monotone convergence theorem asserts only that the limit exists; it does not give its value. Its power lies in not requiring the limit to be known in advance, and we now use it to define Euler's number.

**Example 2.2.6** The sequence $a_n = \left(1 + \frac1n\right)^n$ is strictly increasing and bounded above by $3$, hence convergent.

**Proof** By the binomial theorem,

$$
a_n = 1 + \sum_{k=1}^n \binom nk \frac1{n^k} = 1 + \sum_{k=1}^n \frac1{k!}\Bigl(1 - \frac1n\Bigr)\Bigl(1 - \frac2n\Bigr)\cdots\Bigl(1 - \frac{k-1}n\Bigr).
$$
When $n$ is replaced by $n + 1$, each factor $1 - \frac jn$ increases to $1 - \frac j{n+1}$, and an extra $(n + 1)$-th term (a positive number) appears, so $a_n < a_{n+1}$. Moreover, each factor is less than $1$, so

$$
a_n < 1 + \sum_{k=1}^n \frac1{k!} \leq 1 + 1 + \sum_{k=2}^n \frac1{k(k-1)} = 2 + \sum_{k=2}^n \Bigl(\frac1{k-1} - \frac1k\Bigr) = 3 - \frac1n < 3.
$$
By the monotone convergence theorem, $\{a_n\}$ converges. $\square$

**Definition 2.2.1 (Euler's Number)** The limit

$$
\mathrm{e} = \lim_{n \to \infty} \Bigl(1 + \frac1n\Bigr)^n \approx 2.71828
$$
is called **Euler's number** (the natural constant). The logarithm to the base $\mathrm{e}$ is called the natural logarithm and is written $\ln x$.

One shows similarly that $b_n = \left(1 + \frac1n\right)^{n+1}$ is strictly decreasing and also tends to $\mathrm{e}$. Hence for all $n \in \mathbb{N}_+$

$$
\Bigl(1 + \frac1n\Bigr)^n < \mathrm{e} < \Bigl(1 + \frac1n\Bigr)^{n+1}, \qquad\text{and taking logarithms,}\qquad \frac{1}{n + 1} < \ln\Bigl(1 + \frac1n\Bigr) < \frac1n. \tag{2.1}
$$
Inequality (2.1) reappears in the study of series: it shows that $1 + \frac12 + \cdots + \frac1n - \ln n$ is monotonic and bounded ([Chapter 5](/2.2.5)).

**Example 2.2.7** Let $a > 0$ and $a_n = \underbrace{\sqrt{a + \sqrt{a + \cdots + \sqrt a}}}_{n \text{ radicals}}$. Prove that $\{a_n\}$ converges and find its limit.

**Solution** The sequence satisfies the recursion $a_1 = \sqrt a$, $a_{n+1} = \sqrt{a + a_n}$. Monotonicity: $a_2 = \sqrt{a + \sqrt a} > a_1$; if $a_n > a_{n-1}$, then $a_{n+1} = \sqrt{a + a_n} > \sqrt{a + a_{n-1}} = a_n$. Boundedness: $a_1 < \sqrt a + 1$; if $a_n < \sqrt a + 1$, then $a_{n+1} < \sqrt{a + \sqrt a + 1} < \sqrt{a + 2\sqrt a + 1} = \sqrt a + 1$. By the monotone convergence theorem, $a_n \to k$. Taking limits on both sides of the recursion (the left-hand side is a subsequence, so its limit is also $k$) gives $k = \sqrt{a + k}$, that is, $k^2 - k - a = 0$. Since $k > 0$,

$$
\lim_{n \to \infty} a_n = \frac{1 + \sqrt{1 + 4a}}{2}.
$$

**Example 2.2.8** Let $a_1 = \sqrt2$ and $a_n = \sqrt{2a_{n-1}}$ ($n \geq 2$). Then $a_n$ is strictly increasing (by induction: $a_n > a_{n-1} \implies a_{n+1} = \sqrt{2a_n} > \sqrt{2a_{n-1}} = a_n$) and $a_n < 2$ (by induction: $a_n < 2 \implies a_{n+1} < \sqrt4 = 2$), so it converges. If $k$ is the limit, then $k = \sqrt{2k}$ and $k \geq a_1 > 0$ give $k = 2$.

**Algorithm 2.2.1 (Limit of a Recursive Sequence $a_{n+1} = f(a_n)$)**

1. Prove by induction that $\{a_n\}$ is monotonic (compare $a_2$ with $a_1$, then propagate using the monotonicity of $f$);
2. Prove by induction that $\{a_n\}$ is bounded (the bound is usually the guessed limit, or a slightly larger number);
3. By the monotone convergence theorem, $a_n \to k$; taking limits on both sides of the recursion gives the equation $k = f(k)$ (this requires $f$ to be continuous; see [Chapter 3](/2.2.3));
4. Solve the equation, and discard inadmissible roots using sign and order preservation (for example $k \geq a_1$).

Existence of the limit must be proved before step 3: for instance, with $a_1 = 2$ and $a_{n+1} = a_n^2$, assuming a limit $k$ outright gives $k = k^2$, whereas the sequence actually tends to $+\infty$.

#### 2.2.2.3. The Cauchy Criterion

The monotone convergence theorem applies only to monotonic sequences. We would like a convergence criterion that applies to every sequence and still does not involve the value of the limit. The terms of a convergent sequence get closer and closer to each other; the Cauchy criterion says that, conversely, "terms getting closer and closer to each other" is enough to guarantee convergence.

**Definition 2.2.2 (Cauchy Sequence)** Let $\{x_n\}$ be a sequence. If for every $\varepsilon > 0$ there exists $N \in \mathbb{N}_+$ such that $|x_n - x_m| < \varepsilon$ for all $m, n > N$, then $\{x_n\}$ is called a **Cauchy sequence** (or fundamental sequence). Equivalently: for every $\varepsilon > 0$ there exists $N$ such that $|x_{n+p} - x_n| < \varepsilon$ for all $n > N$ and all $p \in \mathbb{N}_+$.

For example, $\left\{\frac1n\right\}$, $\left\{\frac1{2^n}\right\}$ and $\{q^n\}$ ($|q| < 1$) are Cauchy sequences, while $\{n\}$ and $\{(-1)^n\}$ are not. The negation is used to prove divergence:

$$
\{x_n\} \text{ is not a Cauchy sequence} \iff \exists \varepsilon_0 > 0,\ \forall j \in \mathbb{N}_+,\ \exists n_j > j,\ p_j \in \mathbb{N}_+,\ |x_{n_j + p_j} - x_{n_j}| \geq \varepsilon_0.
$$

**Theorem 2.2.4 (Cauchy Criterion)** A sequence $\{x_n\}$ converges if and only if $\{x_n\}$ is a Cauchy sequence.

**Proof** Necessity: let $x_n \to A$. Given $\varepsilon > 0$, there exists $N$ such that $|x_n - A| < \frac\varepsilon2$ for $n > N$, and then $|x_n - x_m| \leq |x_n - A| + |x_m - A| < \varepsilon$ for $m, n > N$.

The proof of sufficiency requires the Bolzano–Weierstrass theorem; see Theorem 3.2.3 in [Chapter 3](/2.2.3#sec-3.2). $\square$

The Cauchy criterion is yet another formulation of the **completeness of the real numbers**: in the rational numbers, a sequence of rationals approximating $\sqrt2$ (such as $1, 1.4, 1.41, 1.414, \dots$) is a Cauchy sequence but has no limit in $\mathbb{Q}$. In [1.2.4](/1.2.4#sec-4.1) the real numbers are constructed precisely as equivalence classes of rational Cauchy sequences.

**Example 2.2.9** Prove that $x_n = \sum_{k=1}^n \frac{\sin k}{k^2}$ converges.

**Proof** For all $n, p \in \mathbb{N}_+$,

$$
|x_{n+p} - x_n| = \left|\sum_{k=n+1}^{n+p} \frac{\sin k}{k^2}\right| \leq \sum_{k=n+1}^{n+p} \frac1{k^2} < \sum_{k=n+1}^{n+p} \frac1{(k-1)k} = \frac1n - \frac1{n+p} < \frac1n.
$$
Given $\varepsilon > 0$, take $N = \left\lfloor \frac1\varepsilon \right\rfloor$; then $|x_{n+p} - x_n| < \varepsilon$ for $n > N$ and all $p$. Thus $\{x_n\}$ is a Cauchy sequence and therefore converges. $\square$

**Example 2.2.10** Prove that $a_n = \sum_{k=1}^n \frac{(-1)^{k-1}}{k}$ converges.

**Proof** For all $n, p$,

$$
|a_{n+p} - a_n| = \left|\frac1{n+1} - \frac1{n+2} + \frac1{n+3} - \cdots + \frac{(-1)^{p-1}}{n+p}\right|.
$$
This is an alternating sum whose terms decrease in absolute value. Pairing from the first term, $\left(\frac1{n+1} - \frac1{n+2}\right) + \left(\frac1{n+3} - \frac1{n+4}\right) + \cdots$, every pair is nonnegative, so the sum is $\geq 0$; pairing from the second term, $\frac1{n+1} - \left(\frac1{n+2} - \frac1{n+3}\right) - \cdots$, shows that the sum is $\leq \frac1{n+1}$. Hence $|a_{n+p} - a_n| \leq \frac1{n+1}$, and given $\varepsilon > 0$ we may take $N = \left\lfloor \frac1\varepsilon \right\rfloor$. $\square$

**Example 2.2.11** Prove that $a_n = \sum_{k=1}^n \frac1k$ diverges.

**Proof** Take $\varepsilon_0 = \frac12$. For every $j \in \mathbb{N}_+$, take $n_j = j$ and $p_j = j$; then

$$
|a_{2j} - a_j| = \sum_{k=j+1}^{2j} \frac1k \geq j \cdot \frac1{2j} = \frac12 = \varepsilon_0.
$$
Thus $\{a_n\}$ is not a Cauchy sequence and therefore diverges. Since $\{a_n\}$ is strictly increasing, the monotone convergence theorem shows that it is unbounded above, that is, $a_n \to +\infty$. $\square$

Examples 2.2.10 and 2.2.11 are the prototypes of the alternating series and the harmonic series of [Chapter 8](/2.2.8).

## 2.3. Limits of Functions: Concepts and Properties

Extending the idea of the limit of a sequence to functions gives the *limit of a function*. The variable $n$ of a sequence can only tend to $+\infty$, whereas the variable $x$ of a function can vary in six ways: $x \to +\infty$, $x \to -\infty$, $x \to \infty$, $x \to x_0$, $x \to x_0^-$ and $x \to x_0^+$.

### 2.3.1. Limits of Functions at Infinity

**Definition 2.3.1 (Limit as $x \to +\infty$)** Let $f$ be defined on $(a, +\infty)$ and $A \in \mathbb{R}$. If for every $\varepsilon > 0$ there exists $X > 0$ such that $|f(x) - A| < \varepsilon$ whenever $x > X$, then the limit of $f$ as $x$ tends to $+\infty$ is said to be $A$, written $\lim\limits_{x \to +\infty} f(x) = A$ or $f(x) \to A$ ($x \to +\infty$).

Compared with the limit of a sequence, the only difference is that $N \in \mathbb{N}_+$ is replaced by a real number $X$ and $n > N$ by $x > X$. Replacing $x > X$ by $x < -X$ gives the definition of $\lim\limits_{x \to -\infty} f(x) = A$.

**Definition 2.3.2 (Limit as $x \to \infty$)** Let $f$ be defined on $\{x \mid |x| > a\}$ and $A \in \mathbb{R}$. If for every $\varepsilon > 0$ there exists $X > 0$ such that $|f(x) - A| < \varepsilon$ whenever $|x| > X$, we write $\lim\limits_{x \to \infty} f(x) = A$.

Clearly $\lim\limits_{x \to \infty} f(x) = A \iff \lim\limits_{x \to +\infty} f(x) = A$ and $\lim\limits_{x \to -\infty} f(x) = A$. For example, $\lim\limits_{x \to \infty} \arctan x$ does not exist, because the limits in the two directions are $\pm\frac\pi2$ (Example 2.3.1).

**Example 2.3.1** Prove that $\lim\limits_{x \to +\infty} \arctan x = \frac\pi2$ and $\lim\limits_{x \to -\infty} \arctan x = -\frac\pi2$.

**Proof** Let $\varepsilon \in (0, 1)$. Then $\left|\arctan x - \frac\pi2\right| = \frac\pi2 - \arctan x < \varepsilon \iff \arctan x > \frac\pi2 - \varepsilon \iff x > \tan\left(\frac\pi2 - \varepsilon\right)$, so $X = \tan\left(\frac\pi2 - \varepsilon\right)$ works. The second limit follows because $\arctan$ is odd. $\square$

Similarly, $\lim\limits_{x \to +\infty} \operatorname{arccot} x = 0$ and $\lim\limits_{x \to -\infty} \operatorname{arccot} x = \pi$.

**Example 2.3.2** Prove that $\lim\limits_{x \to \infty} \frac{x^2 - 1}{x^2 + 1} = 1$.

**Proof** $\left|\frac{x^2 - 1}{x^2 + 1} - 1\right| = \frac2{x^2 + 1} < \frac2{x^2}$. Given $\varepsilon > 0$, the inequality $\frac2{x^2} < \varepsilon$ holds as soon as $|x| > \sqrt{2/\varepsilon}$, so take $X = \sqrt{2/\varepsilon}$. $\square$

Verifying $\lim\limits_{x \to \infty} f(x) = A$ works as in Algorithm 2.1.1: enlarge $|f(x) - A|$ to the form $k|x|^{-m}$ ($k, m > 0$) and take $X = (k/\varepsilon)^{1/m}$.

### 2.3.2. Limits of Functions at a Point

**Definition 2.3.3 (Limit as $x \to x_0$)** Let $f$ be defined on some punctured neighborhood of $x_0$ and $A \in \mathbb{R}$. If for every $\varepsilon > 0$ there exists $\delta > 0$ such that

$$
|f(x) - A| < \varepsilon
$$
whenever $0 < |x - x_0| < \delta$ (that is, $x \in N^*(x_0, \delta)$), then the limit of $f(x)$ as $x \to x_0$ is said to be $A$, written $\lim\limits_{x \to x_0} f(x) = A$ or $f(x) \to A$ ($x \to x_0$).

The condition $0 < |x - x_0|$ excludes $x = x_0$: the limit of a function at a point does not depend on the value of the function at that point ($f$ need not even be defined at $x_0$), nor on its values outside some neighborhood of the point.

![Geometric meaning of the ε-δ definition: when x lies in the punctured δ-neighborhood of x_0 (vertical band), f(x) lies in the ε-neighborhood of A (horizontal band); the value f(x_0) does not affect the limit.](./plots/epsilon-delta.py)

**Definition 2.3.4 (One-Sided Limits)** Let $f$ be defined on $(x_0 - \rho, x_0)$ and $A \in \mathbb{R}$. If for every $\varepsilon > 0$ there exists $\delta > 0$ such that $|f(x) - A| < \varepsilon$ whenever $x_0 - \delta < x < x_0$, then $A$ is called the left-hand limit of $f$ at $x_0$, written $\lim\limits_{x \to x_0^-} f(x) = A$ or $f(x_0 - 0) = A$. Replacing the condition by $x_0 < x < x_0 + \delta$ gives the right-hand limit $\lim\limits_{x \to x_0^+} f(x) = f(x_0 + 0)$. Left-hand and right-hand limits are collectively called **one-sided limits**.

The definitions immediately give

$$
\lim_{x \to x_0} f(x) = A \iff \lim_{x \to x_0^-} f(x) = A \ \text{and}\ \lim_{x \to x_0^+} f(x) = A.
$$
The limit of a piecewise function at a breakpoint usually requires computing the left-hand and right-hand limits separately.

**Example 2.3.3** Verify: (1) $\lim\limits_{x \to x_0} \cos x = \cos x_0$ and $\lim\limits_{x \to x_0} \sin x = \sin x_0$; (2) $\lim\limits_{x \to 1} \ln x = 0$; (3) $\lim\limits_{x \to 0} a^x = 1$ ($a > 0$).

**Proof** (1) Using $|\sin t| \leq |t|$,

$$
|\cos x - \cos x_0| = 2\left|\sin\frac{x + x_0}{2}\right|\left|\sin\frac{x - x_0}{2}\right| \leq 2\left|\sin\frac{x - x_0}2\right| \leq |x - x_0|,
$$
so given $\varepsilon > 0$ we may take $\delta = \varepsilon$; the case of $\sin x$ is similar.

(2) Given $\varepsilon > 0$, $|\ln x| < \varepsilon \iff \mathrm{e}^{-\varepsilon} < x < \mathrm{e}^\varepsilon \iff \mathrm{e}^{-\varepsilon} - 1 < x - 1 < \mathrm{e}^\varepsilon - 1$. Take $\delta = \min\{\mathrm{e}^\varepsilon - 1, 1 - \mathrm{e}^{-\varepsilon}\}$.

(3) Let $a > 1$ (for $0 < a < 1$ use $a^x = 1/(1/a)^x$; the case $a = 1$ is obvious). Given $\varepsilon \in (0, 1)$, $|a^x - 1| < \varepsilon \iff \log_a(1 - \varepsilon) < x < \log_a(1 + \varepsilon)$. Take $\delta = \min\{\log_a(1 + \varepsilon), -\log_a(1 - \varepsilon)\}$. $\square$

**Example 2.3.4** Prove that $\lim\limits_{x \to 1^-} \arcsin x = \frac\pi2$.

**Proof** Let $\frac12 \leq x < 1$ and put $t = \frac\pi2 - \arcsin x \in \left(0, \frac\pi3\right]$. Since $t < \tan t$ for $0 < t < \frac\pi2$,

$$
\frac\pi2 - \arcsin x < \tan t = \cot(\arcsin x) = \frac{\sqrt{1 - x^2}}{x} \leq 2\sqrt{(1 - x)(1 + x)} \leq 2\sqrt2\sqrt{1 - x}.
$$
Given $\varepsilon > 0$, the right-hand side is less than $\varepsilon$ as soon as $1 - x < \frac{\varepsilon^2}8$. With $\delta = \min\left\{\frac{\varepsilon^2}8, \frac12\right\}$, we get $\left|\arcsin x - \frac\pi2\right| < \varepsilon$ for $1 - \delta < x < 1$. $\square$

Similarly, $\lim\limits_{x \to -1^+} \arcsin x = -\frac\pi2$. The inequality used in the proof,

$$
\sin x < x < \tan x, \quad x \in \Bigl(0, \frac\pi2\Bigr), \tag{2.2}
$$
comes from comparing the areas of triangles and a sector in the unit circle (see the proof in Example 2.4.3).

**Example 2.3.5** Find $\lim\limits_{x \to 1} \frac{x^2 - 1}{x^2 - x}$.

**Solution** For $x \ne 1$, $\frac{x^2 - 1}{x^2 - x} = \frac{x + 1}{x} = 1 + \frac1x$, so we guess that the limit is $2$. Verification: $\left|1 + \frac1x - 2\right| = \frac{|x - 1|}{|x|}$. If we restrict to $|x - 1| < \frac12$, then $x > \frac12$ and the expression is $< 2|x - 1|$. Given $\varepsilon > 0$, take $\delta = \min\left\{\frac12, \frac\varepsilon2\right\}$; then $\left|\frac{x^2 - 1}{x^2 - x} - 2\right| < \varepsilon$ for $0 < |x - 1| < \delta$.

Here "first restricting $x$ to a fixed neighborhood of $x_0$" is a common device when enlarging: it gives definite bounds for factors such as the denominator, and at the end $\delta$ is taken to be the smaller of the two restrictions. In general, enlarge $|f(x) - A|$ to $k|x - x_0|^m$ ($k, m > 0$) and take $\delta = (\varepsilon/k)^{1/m}$ (and then the minimum with the earlier restriction).

The same language describes functions tending to infinity. For example,

$$
\lim_{x \to x_0} f(x) = \infty \iff \forall M > 0,\ \exists \delta > 0,\ 0 < |x - x_0| < \delta \implies |f(x)| > M;
$$

$$
\lim_{x \to \infty} f(x) = +\infty \iff \forall M > 0,\ \exists X > 0,\ |x| > X \implies f(x) > M.
$$
Combining the six processes of the independent variable with the four outcomes $f(x) \to A, \infty, +\infty, -\infty$ gives the definitions of all 24 kinds of limits, which the reader can write out one by one. As with sequences, $\lim f(x) = \infty$ is a special case of a limit that does not exist.

### 2.3.3. Properties of Limits of Functions

Limits of functions come in six forms, and $x \to \square$ is often used to stand for any one of them. The properties below are stated and proved for $x \to x_0$; analogous results hold for the other five forms ("punctured neighborhood of $x_0$" being replaced by "$(X, +\infty)$," "left side of $x_0$" and so on).

**Property 2.3.1 (Uniqueness)** If the limit of a function exists, it is unique.

**Property 2.3.2 (Local Boundedness)** If $\lim\limits_{x \to x_0} f(x)$ exists, then $f$ is bounded on some punctured neighborhood of $x_0$: there exist $\delta > 0$ and $M > 0$ such that $|f(x)| \leq M$ for $x \in N^*(x_0, \delta)$.

**Proof** Let $A$ be the limit. For $\varepsilon = 1$ there exists $\delta > 0$ such that $|f(x) - A| < 1$, hence $|f(x)| < |A| + 1$, for $x \in N^*(x_0, \delta)$. $\square$

Unlike the case of sequences, boundedness here is only local: $\lim\limits_{x \to 1} \frac1x = 1$, but $\frac1x$ is unbounded on $(0, 1)$.

**Property 2.3.3 (Local Sign Preservation)**

1. If $\lim\limits_{x \to x_0} f(x) > 0$ ($< 0$), then there exists $\delta > 0$ such that $f(x) > 0$ ($< 0$) for $x \in N^*(x_0, \delta)$;
2. If $f$ is nonnegative (nonpositive) on some punctured neighborhood of $x_0$ and $\lim\limits_{x \to x_0} f(x)$ exists, then $\lim\limits_{x \to x_0} f(x) \geq 0$ ($\leq 0$).

The following theorem connects limits of functions with limits of sequences, so that results about limits of sequences can be transferred to limits of functions.

**Theorem 2.3.6 (Heine's Theorem)** $\lim\limits_{x \to x_0} f(x) = A$ if and only if $\lim\limits_{n \to \infty} f(x_n) = A$ for every sequence $\{x_n\}$ in the domain of $f$ satisfying $x_n \to x_0$ and $x_n \ne x_0$ ($n \in \mathbb{N}_+$).

**Proof** Necessity: given $\varepsilon > 0$, there exists $\delta > 0$ such that $|f(x) - A| < \varepsilon$ whenever $0 < |x - x_0| < \delta$. For this $\delta$ there exists $N$ such that $|x_n - x_0| < \delta$ for $n > N$; since also $x_n \ne x_0$, we get $|f(x_n) - A| < \varepsilon$.

Sufficiency (by contradiction): if $\lim\limits_{x \to x_0} f(x) = A$ fails, then there exists $\varepsilon_0 > 0$ such that for every $\delta > 0$ some $x \in N^*(x_0, \delta)$ satisfies $|f(x) - A| \geq \varepsilon_0$. Taking $\delta = 1, \frac12, \dots, \frac1n, \dots$ in turn, we obtain $x_n \in N^*\left(x_0, \frac1n\right)$ with $|f(x_n) - A| \geq \varepsilon_0$. Then $x_n \to x_0$ and $x_n \ne x_0$, but $f(x_n) \not\to A$, a contradiction. $\square$

Heine's theorem, also known as the sequential criterion for limits, holds equally for the other five limit processes; for example, $\lim\limits_{x \to +\infty} f(x) = A$ if and only if $f(x_n) \to A$ for every sequence $x_n \to +\infty$. Its most common use is to prove that a limit of a function does not exist: construct two sequences $x_n \to x_0$ and $y_n \to x_0$ ($x_n, y_n \ne x_0$) with $\lim f(x_n) \ne \lim f(y_n)$, or one sequence for which $\lim f(x_n)$ does not exist.

**Example 2.3.6** Prove that $\lim\limits_{x \to 0} \sin\frac1x$ does not exist.

**Proof** Take $x_n = \frac1{2n\pi}$ and $y_n = \frac1{2n\pi + \frac\pi2}$. Both tend to $0$ and are different from $0$, but $\sin\frac1{x_n} = 0 \to 0$ while $\sin\frac1{y_n} = 1 \to 1$. By Heine's theorem, the limit does not exist. $\square$

## 2.4. Rules for Limits of Functions

### 2.4.1. Arithmetic Rules for Limits of Functions

**Theorem 2.4.1 (Arithmetic Rules)** Let $\lim\limits_{x \to \square} f(x) = A$ and $\lim\limits_{x \to \square} g(x) = B$. Then

1. $\lim\limits_{x \to \square} c f(x) = cA$ ($c \in \mathbb{R}$);
2. $\lim\limits_{x \to \square} [f(x) \pm g(x)] = A \pm B$;
3. $\lim\limits_{x \to \square} f(x)g(x) = AB$;
4. $\lim\limits_{x \to \square} \frac{f(x)}{g(x)} = \frac AB$ ($B \ne 0$);
5. $\lim\limits_{x \to \square} f(x)^k = A^k$ ($k \in \mathbb{Q}$, $A > 0$).

The proof can imitate that of Theorem 2.2.1, or the results can be obtained directly from those for sequences by Heine's theorem.

**Example 2.4.1** Find the limits ($m, n \in \mathbb{N}_+$):

$$
\text{(1)}\ \lim_{x \to 0} \frac{(1 + mx)^n - (1 + nx)^m}{x^2}; \qquad
\text{(2)}\ \lim_{x \to 1} \frac{x^m - 1}{x^n - 1}; \qquad
\text{(3)}\ \lim_{x \to 1} \frac{x^{n+1} - (n + 1)x + n}{(x - 1)^2}; \qquad
\text{(4)}\ \lim_{x \to +\infty} \frac{\sqrt{x + \sqrt{x + \sqrt x}}}{\sqrt{x + 1}}.
$$

**Solution** (1) Expand by the binomial theorem up to the $x^2$ term: $(1 + mx)^n = 1 + nmx + \binom n2 m^2x^2 + x^3(\cdots)$ and $(1 + nx)^m = 1 + mnx + \binom m2 n^2x^2 + x^3(\cdots)$. After subtraction the linear terms cancel, and

$$
\lim_{x \to 0} \frac{(1 + mx)^n - (1 + nx)^m}{x^2} = \frac{n(n-1)m^2 - m(m-1)n^2}{2} = \frac{mn(n - m)}{2}.
$$

(2) Cancel the common factor $x - 1$: $\frac{x^m - 1}{x^n - 1} = \frac{1 + x + \cdots + x^{m-1}}{1 + x + \cdots + x^{n-1}} \to \frac mn$.

(3) $x^{n+1} - (n+1)x + n = x(x^n - 1) - n(x - 1) = (x - 1)\bigl[(x - 1) + (x^2 - 1) + \cdots + (x^n - 1)\bigr]$ (pair off the terms of $x(1 + x + \cdots + x^{n-1}) - n$), and cancelling one factor $x - 1$,

$$
\lim_{x \to 1} \frac{(x - 1) + (x^2 - 1) + \cdots + (x^n - 1)}{x - 1} = 1 + 2 + \cdots + n = \frac{n(n + 1)}{2}.
$$

(4) Divide numerator and denominator by $\sqrt x$: $\frac{\sqrt{1 + \sqrt{1/x + 1/x^{3/2}}}}{\sqrt{1 + 1/x}} \to 1$.

**Example 2.4.2 (Limits of Exponential and Logarithmic Functions)** Let $a > 0$, $x_0 \in \mathbb{R}$ and $y_0 > 0$. Then $\lim\limits_{x \to x_0} a^x = a^{x_0}$ and $\lim\limits_{x \to y_0} \ln x = \ln y_0$.

**Proof** By Example 2.3.3, $\lim\limits_{t \to 0} a^t = 1$, so $a^x - a^{x_0} = a^{x_0}(a^{x - x_0} - 1) \to 0$ ($x \to x_0$). Similarly, $\ln x - \ln y_0 = \ln\frac{x}{y_0}$, and $\frac{x}{y_0} \to 1$ as $x \to y_0$, so $\ln\frac x{y_0} \to 0$ by Example 2.3.3 and the theorem on limits of composite functions (§2.4.4). $\square$

### 2.4.2. The Squeeze Theorem

**Theorem 2.4.2 (Squeeze Theorem)** Let $f, g, h$ satisfy $f(x) \leq h(x) \leq g(x)$ on some punctured neighborhood $N^*(x_0, \delta_0)$ of $x_0$, and $\lim\limits_{x \to x_0} f(x) = \lim\limits_{x \to x_0} g(x) = A$. Then $\lim\limits_{x \to x_0} h(x) = A$.

**Proof** Given $\varepsilon > 0$, there exist $\delta_1, \delta_2 > 0$ such that $|f(x) - A| < \varepsilon$ for $0 < |x - x_0| < \delta_1$ and $|g(x) - A| < \varepsilon$ for $0 < |x - x_0| < \delta_2$. With $\delta = \min\{\delta_0, \delta_1, \delta_2\}$, for $0 < |x - x_0| < \delta$ we have $|h(x) - A| \leq \max\{|f(x) - A|, |g(x) - A|\} < \varepsilon$. $\square$

The squeeze theorem holds equally for the other five limit processes. A typical application is "infinitesimal times bounded": $|x\sin\frac1x| \leq |x|$, so $\lim\limits_{x \to 0} x\sin\frac1x = 0$, although $\sin\frac1x$ itself has no limit (Example 2.3.6).

![Left: sin(1/x) oscillates infinitely often near 0 and has different limits along two sequences. Right: x sin(1/x) is squeezed between −|x| and |x| and tends to 0 by the squeeze theorem.](./plots/sin-one-over-x.py)

**Example 2.4.3 (The First Fundamental Limit)** Prove that $\lim\limits_{x \to 0} \frac{\sin x}{x} = 1$.

**Proof** First consider the right-hand limit. Let $0 < x < \frac\pi2$. In the unit circle take the sector $OAB$ with central angle $x$ ($B$ on the $x$-axis), and let the tangent line at $B$ meet the extension of $OA$ at $C$. The areas of triangle $OAB$, sector $OAB$ and triangle $OBC$ increase in this order:

$$
\frac{\sin x}{2} < \frac x2 < \frac{\tan x}{2}.
$$
This is inequality (2.2). Dividing by $\frac{\sin x}2$ and taking reciprocals gives $\cos x < \frac{\sin x}{x} < 1$. By Example 2.3.3, $\cos x \to 1$, and by the squeeze theorem $\lim\limits_{x \to 0^+} \frac{\sin x}x = 1$. Since $\frac{\sin x}x$ is an even function, the left-hand limit is also $1$. $\square$

From this we obtain

$$
\lim_{x \to 0} \frac{\tan x}{x} = \lim_{x \to 0} \frac{\sin x}{x} \cdot \frac{1}{\cos x} = 1, \qquad
\lim_{x \to 0} \frac{\arcsin x}{x} = \lim_{y \to 0} \frac{y}{\sin y} = 1, \qquad
\lim_{x \to 0} \frac{\arctan x}{x} = \lim_{y \to 0} \frac{y}{\tan y} = 1,
$$
where in the last two we set $y = \arcsin x$ and $y = \arctan x$ ($y \to 0$ as $x \to 0$; we use Theorem 2.4.4 on limits of composite functions).

### 2.4.3. Limits of Monotonic Functions

The function version of the monotone convergence theorem (Theorem 2.2.3) states that a monotonic function has one-sided limits at every point.

**Theorem 2.4.3 (One-Sided Limits of Monotonic Functions)**

1. If $f$ is nondecreasing on $(a, x_0]$, then $\lim\limits_{x \to x_0^-} f(x)$ exists and equals $\sup\limits_{a < x < x_0} f(x) \leq f(x_0)$;
2. If $f$ is nondecreasing on $[x_0, b)$, then $\lim\limits_{x \to x_0^+} f(x)$ exists and equals $\inf\limits_{x_0 < x < b} f(x) \geq f(x_0)$;
3. If $f$ is monotonic and bounded on $(a, +\infty)$, then $\lim\limits_{x \to +\infty} f(x)$ exists; if $f$ is monotonic and bounded on $(-\infty, b)$, then $\lim\limits_{x \to -\infty} f(x)$ exists.

For nonincreasing functions, the supremum and infimum in 1 and 2 are interchanged and the inequalities are reversed.

**Proof** 1. On $(a, x_0)$, $f$ is bounded above by $f(x_0)$, so by the least-upper-bound property $A = \sup\limits_{a < x < x_0} f(x)$ exists and $A \leq f(x_0)$. Given $\varepsilon > 0$, $A - \varepsilon$ is not an upper bound, so there exists $x_1 \in (a, x_0)$ with $f(x_1) > A - \varepsilon$. By monotonicity, $A - \varepsilon < f(x_1) \leq f(x) \leq A$ for all $x \in (x_1, x_0)$. Taking $\delta = x_0 - x_1$ gives $\lim\limits_{x \to x_0^-} f(x) = A$. Parts 2 and 3 are similar. $\square$

Consequently, if $f$ is nondecreasing on $(a, b)$, then $f(x_0 - 0) \leq f(x_0) \leq f(x_0 + 0)$ for every $x_0 \in (a, b)$; for nonincreasing $f$ the inequalities are reversed. A monotonic function can only have "jumps," a fact used in [Chapter 3](/2.2.3) when discussing points of discontinuity.

**Example 2.4.4 (The Second Fundamental Limit)** Prove that $\lim\limits_{x \to \infty} \left(1 + \frac1x\right)^x = \mathrm{e}$.

**Proof** First let $x \to +\infty$. Put $n = \lfloor x \rfloor$; then $n \leq x < n + 1$, $n \to +\infty$, and

$$
\Bigl(1 + \frac1{n + 1}\Bigr)^n \leq \Bigl(1 + \frac1x\Bigr)^x \leq \Bigl(1 + \frac1n\Bigr)^{n+1}.
$$
Here the right-hand side equals $\left(1 + \frac1n\right)^n\left(1 + \frac1n\right)$ and the left-hand side equals $\left(1 + \frac1{n+1}\right)^{n+1}\left(1 + \frac1{n+1}\right)^{-1}$. By Definition 2.2.1, both sides, as sequences in the integer $n$, tend to $\mathrm{e}$: given $\varepsilon > 0$, there exists $N_0$ such that both sides lie in $(\mathrm{e} - \varepsilon, \mathrm{e} + \varepsilon)$ for every integer $n > N_0$. Hence for $x > N_0 + 1$ we have $n = \lfloor x \rfloor > N_0$, and the quantity $\left(1 + \frac1x\right)^x$ squeezed in between also lies in this interval; that is, $\lim\limits_{x \to +\infty} \left(1 + \frac1x\right)^x = \mathrm{e}$.

Now let $x \to -\infty$ and put $z = -x \to +\infty$:

$$
\Bigl(1 + \frac1x\Bigr)^x = \Bigl(1 - \frac1z\Bigr)^{-z} = \Bigl(\frac{z}{z - 1}\Bigr)^z = \Bigl(1 + \frac1{z - 1}\Bigr)^{z-1}\Bigl(1 + \frac1{z-1}\Bigr) \to \mathrm{e}. \qquad \square
$$

Rewriting gives the following frequently used forms:

$$
\lim_{x \to 0} (1 + x)^{1/x} = \mathrm{e}, \qquad \lim_{x \to \infty} \Bigl(1 - \frac1x\Bigr)^x = \frac1{\mathrm{e}}, \qquad \lim_{x \to 0} (1 - x)^{1/x} = \frac1{\mathrm{e}}.
$$

### 2.4.4. Limits of Composite Functions

**Theorem 2.4.4 (Limit of a Composite Function)** Let $\lim\limits_{t \to t_0} g(t) = x_0$ and $\lim\limits_{x \to x_0} f(x) = A$, and suppose $g(t) \ne x_0$ on some punctured neighborhood of $t_0$. Then $\lim\limits_{t \to t_0} f(g(t)) = A$.

**Proof** Given $\varepsilon > 0$, there exists $\eta > 0$ such that $|f(x) - A| < \varepsilon$ whenever $0 < |x - x_0| < \eta$. For this $\eta$ there exists $\delta > 0$ such that $|g(t) - x_0| < \eta$ whenever $0 < |t - t_0| < \delta$; since also $g(t) \ne x_0$, we have $0 < |g(t) - x_0| < \eta$, and therefore $|f(g(t)) - A| < \varepsilon$. $\square$

This theorem justifies "substitution" in computing limits: setting $x = g(t)$, we have $\lim\limits_{t \to t_0} f(g(t)) = \lim\limits_{x \to x_0} f(x)$. The condition $g(t) \ne x_0$ cannot be dropped: let $f(x) = 1$ ($x \ne 0$), $f(0) = 0$ and $g(t) \equiv 0$; then $\lim\limits_{x \to 0} f(x) = 1$, whereas $f(g(t)) \equiv 0$. If, however, $f$ satisfies $\lim\limits_{x \to x_0} f(x) = f(x_0)$ at $x_0$ (that is, $f$ is continuous there; see [Chapter 3](/2.2.3)), then the condition can be dropped and the conclusion reads $\lim\limits_{t \to t_0} f(g(t)) = f\bigl(\lim\limits_{t \to t_0} g(t)\bigr)$.

**Corollary 2.4.1 (Limits of Functions of the Form $u^v$)** Let $\lim\limits_{x \to x_0} u(x) = a > 0$ and $\lim\limits_{x \to x_0} v(x) = b$. Then $\lim\limits_{x \to x_0} u(x)^{v(x)} = a^b$.

**Proof** $u(x)^{v(x)} = \mathrm{e}^{v(x)\ln u(x)}$. By Example 2.4.2 and the theorem on limits of composite functions, $\ln u(x) \to \ln a$, so $v(x)\ln u(x) \to b\ln a$; applying the theorem once more together with the limit of $\mathrm{e}^y$, we get $\mathrm{e}^{v(x)\ln u(x)} \to \mathrm{e}^{b\ln a} = a^b$. $\square$

**Example 2.4.5** Compute: (1) $\lim\limits_{x \to +\infty} \arcsin\frac{x - 1}{x + 1}$; (2) $\lim\limits_{x \to 0} \frac{\sin(\tan x)}{\sin x}$; (3) $\lim\limits_{x \to x_0} x^p$ ($x_0 > 0$).

**Solution** (1) Let $u = \frac{x - 1}{x + 1} \to 1^-$; since $\lim\limits_{u \to 1^-} \arcsin u = \frac\pi2$ (Example 2.3.4), the limit is $\frac\pi2$.

(2) $\frac{\sin(\tan x)}{\sin x} = \frac{\sin(\tan x)}{\tan x} \cdot \frac{1}{\cos x}$. Let $u = \tan x$; as $x \to 0$ we have $u \to 0$ and $u \ne 0$, so the first factor tends to $1$, and the limit is $1$.

(3) $x^p = \mathrm{e}^{p\ln x} \to \mathrm{e}^{p\ln x_0} = x_0^p$.

When $u(x) \to 1$ and $v(x) \to \infty$, the expression $u^v$ is an indeterminate form of type $1^\infty$; Corollary 2.4.1 does not apply, and we need the second fundamental limit.

**Algorithm 2.4.1 (Limits of Type $1^\infty$)** Let $u(x) \to 1$ and $v(x) \to \infty$.

1. Write $u^v = \Bigl[\bigl(1 + (u - 1)\bigr)^{\frac1{u-1}}\Bigr]^{v(u - 1)}$;
2. The expression in brackets tends to $\mathrm{e}$ (by the second fundamental limit and the theorem on limits of composite functions);
3. If $\lim v(x)\bigl(u(x) - 1\bigr) = c$, then $\lim u^v = \mathrm{e}^c$ by Corollary 2.4.1.

**Example 2.4.6** Compute:

$$
\text{(1)}\ \lim_{x \to 0} (1 + 2\sin x)^{\csc x}; \quad
\text{(2)}\ \lim_{x \to 0} (\cos 2x)^{1/x^2}; \quad
\text{(3)}\ \lim_{x \to \infty} \Bigl(\frac2{x^2} + \cos\frac1x\Bigr)^{x^2}; \quad
\text{(4)}\ \lim_{x \to \pi/4} (\tan x)^{\tan 2x}.
$$

**Solution** (1) $v(u - 1) = \csc x \cdot 2\sin x = 2$, so the limit is $\mathrm{e}^2$.

(2) $\cos 2x - 1 = -2\sin^2 x$ and $v(u - 1) = -\frac{2\sin^2 x}{x^2} \to -2$, so the limit is $\mathrm{e}^{-2}$.

(3) Let $t = \frac1x \to 0$. Then $v(u - 1) = \frac{2t^2 + \cos t - 1}{t^2} = 2 - \frac{2\sin^2(t/2)}{t^2} \to 2 - \frac12 = \frac32$, so the limit is $\mathrm{e}^{3/2}$.

(4) $\tan 2x = \frac{2\tan x}{1 - \tan^2 x}$, so $v(u - 1) = \frac{2\tan x(\tan x - 1)}{(1 - \tan x)(1 + \tan x)} = -\frac{2\tan x}{1 + \tan x} \to -1$, and the limit is $\mathrm{e}^{-1}$.

**Example 2.4.7** For $x \in \mathbb{R}$, find $\lim\limits_{n \to \infty} \underbrace{\sin\sin\cdots\sin}_{n \text{ times}} x$.

**Solution** Let $a_n$ denote the $n$-fold composite, so that $a_n = \sin a_{n-1}$. If $0 < x \leq \pi$, then $a_1 = \sin x \in (0, 1]$, and from $0 < \sin t < t$ ($t > 0$) induction gives $0 < a_n < a_{n-1}$; thus $\{a_n\}$ is strictly decreasing and bounded below by $0$, and it converges to some $\alpha \geq 0$. By Heine's theorem and $\lim\limits_{t \to \alpha} \sin t = \sin\alpha$, taking limits on both sides of $a_n = \sin a_{n-1}$ gives $\alpha = \sin\alpha$, which forces $\alpha = 0$. If $\pi < x < 2\pi$, then $a_1 \in [-1, 0)$, and since $\sin$ is odd, again $a_n \to 0$; if $x = k\pi$, then $a_n \equiv 0$. By periodicity, the limit is $0$ for every $x$.

## 2.5. Infinitesimals and Comparison of Orders

### 2.5.1. Infinitesimals and Infinitely Large Quantities

**Definition 2.5.1 (Infinitesimal)** If $\lim\limits_{x \to \square} f(x) = 0$, then $f(x)$ is called an **infinitesimal** as $x \to \square$.

For example, $x^2$, $\sin x$ and $x\sin\frac1x$ are infinitesimals as $x \to 0$; $\frac1x$ and $\frac1{\ln|x|}$ are infinitesimals as $x \to \infty$; and $\mathrm{e}^{-x}$ is an infinitesimal as $x \to +\infty$. To call a function an infinitesimal, one must specify the limit process of the independent variable.

**Definition 2.5.2 (Infinitely Large Quantity)** If $f(x)$ ($-f(x)$, $|f(x)|$) grows without bound as $x \to \square$, that is, $\lim\limits_{x \to \square} f(x) = +\infty$ ($-\infty$, $\infty$), then $f(x)$ is called a positive infinitely large quantity (a negative infinitely large quantity, an **infinitely large quantity**) as $x \to \square$.

For example, $\frac1x$ is positive infinitely large as $x \to 0^+$, negative infinitely large as $x \to 0^-$ and infinitely large as $x \to 0$. Unboundedness must be distinguished from being infinitely large: as $x \to +\infty$, $x\sin x$ is unbounded (it takes the value $2n\pi + \frac\pi2$ at $x = 2n\pi + \frac\pi2$) but not infinitely large (it takes the value $0$ at $x = n\pi$).

**Property 2.5.1 (Operations on Infinitesimals and Infinitely Large Quantities)** For a common limit process $x \to \square$:

1. The sum, difference and product of two infinitesimals are infinitesimals, and the product of a constant and an infinitesimal is an infinitesimal;
2. The product of two infinitely large quantities is infinitely large, and the product of a nonzero constant and an infinitely large quantity is infinitely large;
3. $f(x)$ is an infinitesimal (with $f(x) \ne 0$) if and only if $\frac1{f(x)}$ is infinitely large;
4. The product of an infinitesimal and a bounded function is an infinitesimal.

The sum of two infinitely large quantities need not be infinitely large ($x$ and $-x$), and the product of an infinitesimal and an infinitely large quantity can be anything ($x^2 \cdot \frac1x$, $x \cdot \frac1x$, $x \cdot \frac1{x^2}$): these indeterminate forms are left to L'Hôpital's rule in [Chapter 5](/2.2.5).

### 2.5.2. Comparison of Orders

Although they all tend to $0$, the functions $x$, $x^2$ and $\sin x$ do so at different rates. We compare the rates by the limit of their ratios.

**Definition 2.5.3 (Order of an Infinitesimal)** Let $f(x)$ and $g(x)$ be infinitesimals as $x \to \square$, with $g(x) \ne 0$.

1. If $\lim\limits_{x \to \square} \frac{f(x)}{g(x)} = c \ne 0$, then $f$ and $g$ are called **infinitesimals of the same order** as $x \to \square$; in particular, if $c = 1$, then $f$ and $g$ are called **equivalent infinitesimals**, written $f(x) \sim g(x)$ ($x \to \square$).
2. If $\lim\limits_{x \to \square} \frac{f(x)}{g(x)} = 0$, then $f$ is called a **higher-order infinitesimal** than $g$ as $x \to \square$, written $f(x) = o\bigl(g(x)\bigr)$ ($x \to \square$).

For example, as $x \to 0$, $\sin x \sim x$, $1 - \cos x$ and $x^2$ are of the same order, and $x^2 = o(x)$. The notation $o(g)$ stands for "some infinitesimal of higher order than $g$," not for a definite function; hence $o(x) - o(x) = o(x)$, not $0$. Equivalent and higher-order infinitesimals are related by

$$
f(x) \sim g(x) \iff f(x) = g(x) + o\bigl(g(x)\bigr) \quad (x \to \square), \tag{2.3}
$$
because $\frac fg \to 1$ is equivalent to $\frac{f - g}{g} \to 0$. Eq. (2.3) writes equivalence as "principal part plus a higher-order remainder," which is the idea behind Taylor's formula in [Chapter 5](/2.2.5).

**Example 2.5.1** Prove that, as $x \to 0$, $\ln(1 + x) \sim x$, $\mathrm{e}^x - 1 \sim x$ and $a^x - 1 \sim x\ln a$ ($a > 0$, $a \ne 1$).

**Proof** By Corollary 2.4.1 and $(1 + x)^{1/x} \to \mathrm{e}$, we have $\frac{\ln(1 + x)}{x} = \ln(1 + x)^{1/x} \to \ln\mathrm{e} = 1$. Let $u = \mathrm{e}^x - 1$; then $x = \ln(1 + u)$, and $u \to 0$ with $u \ne 0$ as $x \to 0$, so $\frac{\mathrm{e}^x - 1}{x} = \frac{u}{\ln(1 + u)} \to 1$. Finally, $\frac{a^x - 1}{x\ln a} = \frac{\mathrm{e}^{x\ln a} - 1}{x\ln a} \to 1$. $\square$

From this and §2.4.2 we obtain the commonly used equivalent infinitesimals ($x \to 0$):

| Infinitesimal | Equivalent to | Infinitesimal | Equivalent to |
|---|---|---|---|
| $\sin x$, $\tan x$ | $x$ | $\ln(1 + x)$ | $x$ |
| $\arcsin x$, $\arctan x$ | $x$ | $\mathrm{e}^x - 1$ | $x$ |
| $1 - \cos x$ | $\frac12 x^2$ | $a^x - 1$ | $x\ln a$ |
| $(1 + x)^\alpha - 1$ ($\alpha \in \mathbb{R}$, $\alpha \ne 0$) | $\alpha x$ | $\sqrt[k]{1 + x} - 1$ | $\frac xk$ |

Here $(1 + x)^\alpha - 1 = \mathrm{e}^{\alpha\ln(1 + x)} - 1 \sim \alpha\ln(1 + x) \sim \alpha x$ holds for every real $\alpha \ne 0$; in the table, $x$ may be replaced by any function $u(x)$ tending to $0$; for example, $\sin x^2 \sim x^2$ as $x \to 0$.

**Theorem 2.5.1 (Substitution of Equivalent Infinitesimals)** Let $f(x) \sim g(x)$ as $x \to \square$. Then

$$
\lim_{x \to \square} f(x)h(x) = \lim_{x \to \square} g(x)h(x), \qquad \lim_{x \to \square} \frac{h(x)}{f(x)} = \lim_{x \to \square} \frac{h(x)}{g(x)};
$$
that is, if the limit on one side exists (or is $\infty$), then so does the limit on the other side, and they are equal.

**Proof** $f(x)h(x) = \frac{f(x)}{g(x)} \cdot g(x)h(x)$ and $\frac fg \to 1$, so the first identity follows from the arithmetic rules; the second is similar. $\square$

Thus, in computing limits, an infinitesimal factor in a product or quotient may be replaced by a simpler equivalent infinitesimal. Terms in a sum or difference, however, may not be replaced at will: the substitution is valid only for whole factors.

**Example 2.5.2** Compute $\lim\limits_{x \to 0} \frac{\tan x - \sin x}{x^3}$.

**Solution** First write the numerator as a product, $\tan x - \sin x = \tan x\,(1 - \cos x)$, and then substitute for the factors:

$$
\lim_{x \to 0} \frac{\tan x\,(1 - \cos x)}{x^3} = \lim_{x \to 0} \frac{x \cdot \frac12x^2}{x^3} = \frac12.
$$
Replacing both $\tan x$ and $\sin x$ directly by $x$ would give the wrong answer $0$: the principal part of $\tan x - \sin x$ is $\frac12x^3$, and the higher-order terms discarded by such a substitution are exactly what determine the result.

**Example 2.5.3** Compute $\lim\limits_{x \to 0} \frac{\sqrt[3]{1 + x^4} - \sqrt[4]{1 - 2x^4}}{\tan x\,\sin x\,(1 - \cos x)}$.

**Solution** The denominator is $\sim x \cdot x \cdot \frac12x^2 = \frac12x^4$. Split the numerator into two parts, each of which has a limit:

$$
\lim_{x \to 0} \frac{\sqrt[3]{1 + x^4} - 1}{\frac12x^4} + \lim_{x \to 0} \frac{1 - \sqrt[4]{1 - 2x^4}}{\frac12x^4} = \frac{\frac13}{\frac12} + \frac{\frac12}{\frac12} = \frac23 + 1 = \frac53.
$$
Here the numerator is first split by the arithmetic rules (both resulting limits exist), and only then is each factor in each fraction replaced by an equivalent one; this is why the computation is correct.

Infinitely large quantities can also be compared by order: let $f$ and $g$ be infinitely large as $x \to \square$; if $\lim\frac fg = c \ne 0$, then $f$ and $g$ are infinitely large quantities of the same order; if $\lim\frac fg = 0$, then $g$ is an infinitely large quantity of higher order than $f$. By the examples in §2.2, as $n \to \infty$,

$$
\ln n \ll n^\alpha \ (\alpha > 0) \ll a^n \ (a > 1) \ll n! \ll n^n,
$$
where $f \ll g$ means that $g$ is infinitely large of higher order than $f$ (for the proof of $\frac{\ln n}{n^\alpha} \to 0$ see [Chapter 5](/2.2.5)).

## Summary

| Topic | Key points |
|---|---|
| Limit of a sequence | $\forall \varepsilon > 0$, $\exists N$, $n > N \implies \lvert a_n - A \rvert < \varepsilon$; only finitely many terms lie outside the neighborhood |
| Limit of a function | $\forall \varepsilon > 0$, $\exists \delta > 0$, $0 < \lvert x - x_0 \rvert < \delta \implies \lvert f(x) - A \rvert < \varepsilon$; independent of $f(x_0)$; six processes |
| Properties | Uniqueness, (local) boundedness, (local) sign preservation, order preservation; passing to the limit may turn $>$ into $\geq$ |
| Subsequences and Heine's theorem | Convergence $\iff$ every subsequence (every $x_n \to x_0$) tends to the same limit; often used to prove nonexistence |
| Arithmetic rules | Require the limit of each part to exist; a sum whose number of terms grows with $n$ cannot be handled term by term |
| Existence criteria | Squeeze theorem; monotone convergence theorem (every bounded monotonic sequence converges); Cauchy criterion (convergent $\iff$ Cauchy sequence) |
| Basic limits | $q^n \to 0$, $\sqrt[n]a \to 1$, $\sqrt[n]n \to 1$, $\frac{n^k}{a^n} \to 0$; $\frac{\sin x}x \to 1$, $\left(1 + \frac1x\right)^x \to \mathrm{e}$ |
| Composites and $u^v$ | Substitution requires $g(t) \ne x_0$ (or $f$ continuous); $u^v \to a^b$ ($a > 0$); type $1^\infty$: $\lim u^v = \mathrm{e}^{\lim v(u - 1)}$ |
| Orders of infinitesimals | Same order, equivalent ($\sim$), higher order ($o$); $f \sim g \iff f = g + o(g)$ |
| Equivalent substitution | Only for factors of products and quotients; standard table: $\sin x, \tan x, \ln(1 + x), \mathrm{e}^x - 1 \sim x$, $1 - \cos x \sim \frac12x^2$, $(1 + x)^\alpha - 1 \sim \alpha x$ |
| Methods | Algorithm 2.1.1 ($\varepsilon$-$N$ verification), Algorithm 2.2.1 (recursive sequences), Algorithm 2.4.1 (type $1^\infty$) |
