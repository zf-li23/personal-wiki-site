---
title: Independence and Random Variables
description: Independence and conditional independence of two events, mutual and pairwise independence of a collection of events, the second part of the Borel–Cantelli lemma, the gambler's ruin; the definition of random variables, Borel sets and measurable functions; mutual independence of random variables, i.i.d. sequences and independence of their functions.
source_hash: 3ee97af0dc97
---

The conditional probability of the previous chapter, [3.1.2](/3.1.2), describes how information about one event affects another. This chapter first treats the case of "no effect", the independence of events. It looks simple, but several details are easily confused: independence versus mutual exclusiveness, independence versus conditional independence, mutual versus pairwise independence. Independence reduces many computations to multiplication, and the gambler's ruin model shows how the law of total probability works together with recursion. The second half of the chapter introduces random variables: by turning the outcomes of an experiment into numbers, they let us describe random phenomena with functions, operations and distributions, and we extend independence to random variables. The next chapter, [3.1.4](/3.1.4), presents the common discrete and continuous random variables, and [3.1.5](/3.1.5) describes random variables uniformly by their distribution functions.

## 3.1. Independence of Events

### 3.1.1. Independence of Two Events

**Example 3.1.1** A biased coin lands heads with probability $p$ and is tossed three times. In a tree-diagram model, the branch probabilities of every toss are $p$ and $1-p$, regardless of the earlier results. Let $H_i$ and $T_i$ denote heads and tails on toss $i$. Then $\mathbb{P}(H_2\mid H_1)=\mathbb{P}(H_2\mid T_1)=p$, and by the law of total probability $\mathbb{P}(H_2)=\mathbb{P}(H_2\mid H_1)\mathbb{P}(H_1)+\mathbb{P}(H_2\mid T_1)\mathbb{P}(T_1)=p$. That is, the result of the first toss does not change the probability of heads on the second.

Intuitively, if the occurrence of an event $B$ brings no new information about an event $A$, that is, $\mathbb{P}(A\mid B)=\mathbb{P}(A)$, we call $A$ and $B$ independent. Rewriting this as a product gives a definition that is symmetric and does not require $\mathbb{P}(B)>0$.

**Definition 3.1.1 (Independence)** Let $(\Omega,\mathcal{F},\mathbb{P})$ be a probability space and $A,B\in\mathcal{F}$. If

$$
\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B),
$$
then $A$ and $B$ are said to be **mutually independent**, or simply **independent**.

The definition is symmetric in $A$ and $B$ and also applies when $\mathbb{P}(B)=0$; when $\mathbb{P}(B)>0$ it is equivalent to $\mathbb{P}(A\mid B)=\mathbb{P}(A)$. By definition, the impossible event $\varnothing$ and the sure event $\Omega$ are independent of every event; more generally, every event of probability 0 or 1 is independent of every event.

**Property 3.1.1** If $A$ and $B$ are independent, then so are $A$ and $B^{\mathsf c}$, $A^{\mathsf c}$ and $B$, and $A^{\mathsf c}$ and $B^{\mathsf c}$.

**Proof** $A=(A\cap B)\cup(A\cap B^{\mathsf c})$ is a disjoint union, so

$$
\mathbb{P}(A\cap B^{\mathsf c})=\mathbb{P}(A)-\mathbb{P}(A\cap B)=\mathbb{P}(A)-\mathbb{P}(A)\mathbb{P}(B)=\mathbb{P}(A)\mathbb{P}(B^{\mathsf c}).
$$
Applying this result to $(A,B^{\mathsf c})$ and to $(B^{\mathsf c},A)$ gives the other two. $\square$

**Remark 3.1.1** Independence and mutual exclusiveness are entirely different concepts. If $A\cap B=\varnothing$ with $\mathbb{P}(A)>0$ and $\mathbb{P}(B)>0$, then $\mathbb{P}(A\cap B)=0\ne\mathbb{P}(A)\mathbb{P}(B)$, so $A$ and $B$ are certainly not independent: knowing that $A$ occurs tells us that $B$ does not.

When do independent events arise? A single experiment can contain independent events (for a fair die, "the result is even" and "the result is at most 2" are independent); unrelated experiments all the more produce independent events.

**Example 3.1.2** Let $\Omega_1=\{\mu_1,\dots,\mu_n\}$ and $\Omega_2=\{\eta_1,\dots,\eta_m\}$ be the sample spaces of unrelated experiments $S_1$ and $S_2$, each with equally likely sample points. Regard the two experiments together as one experiment with sample space $\Omega=\Omega_1\times\Omega_2$, whose $nm$ sample points are equally likely. For $A\subset\Omega_1$ and $B\subset\Omega_2$, the events "the outcome of $S_1$ lies in $A$" and "the outcome of $S_2$ lies in $B$" are $A\times\Omega_2$ and $\Omega_1\times B$, and

$$
\mathbb{P}\big((A\times\Omega_2)\cap(\Omega_1\times B)\big)=\frac{\#A\cdot\#B}{nm}=\frac{\#A}n\cdot\frac{\#B}m=\mathbb{P}(A\times\Omega_2)\,\mathbb{P}(\Omega_1\times B),
$$
so the two events are independent.

### 3.1.2. Conditional Independence

**Definition 3.1.2 (Conditional Independence)** Let $(\Omega,\mathcal{F},\mathbb{P})$ be a probability space and $A,B,C\in\mathcal{F}$ with $\mathbb{P}(C)>0$. If

$$
\mathbb{P}(A\cap B\mid C)=\mathbb{P}(A\mid C)\mathbb{P}(B\mid C),
$$
then $A$ and $B$ are said to be **conditionally independent** given $C$.

Conditional independence is simply independence under the probability measure $\mathbb{P}_C=\mathbb{P}(\cdot\mid C)$. Independence and conditional independence do not imply each other, as the next two examples show.

**Example 3.1.3 (Independent but Not Conditionally Independent)** Toss a fair coin twice; the four outcomes are equally likely. Let $H_1$ be "the first toss is heads", $H_2$ "the second toss is heads" and $D$ "the two tosses differ". $H_1$ and $H_2$ are independent, but

$$
\mathbb{P}(H_1\mid D)=\mathbb{P}(H_2\mid D)=\frac12,\qquad\mathbb{P}(H_1\cap H_2\mid D)=0,
$$
so $\mathbb{P}(H_1\cap H_2\mid D)\ne\mathbb{P}(H_1\mid D)\mathbb{P}(H_2\mid D)$, and $H_1$ and $H_2$ are not conditionally independent given $D$.

**Example 3.1.4 (Conditionally Independent but Not Independent)** There are two biased coins $A$ and $B$, which land heads with probabilities $0.9$ and $0.1$. One of them is chosen with equal probability and tossed twice. Given that coin $A$ was chosen, the two tosses are independent: $\mathbb{P}(H_1\cap H_2\mid A)=0.81=\mathbb{P}(H_1\mid A)\mathbb{P}(H_2\mid A)$. Without knowing which coin was chosen, the law of total probability gives

$$
\mathbb{P}(H_1)=\mathbb{P}(H_2)=\frac12(0.9+0.1)=\frac12,\qquad\mathbb{P}(H_1\cap H_2)=\frac12(0.81+0.01)=0.41\ne\frac14,
$$
so the two tosses are not independent: $\mathbb{P}(H_2\mid H_1)=0.82$, since a head on the first toss makes us more confident that coin $A$ was chosen.

### 3.1.3. Independence of a Collection of Events

Intuitively, "a collection of events is mutually independent" means that information about any of the events does not change the probabilities of the others, for example $\mathbb{P}\big(A_1\cap(A_2^{\mathsf c}\cup A_3)\mid A_5\cap A_6^{\mathsf c}\big)=\mathbb{P}\big(A_1\cap(A_2^{\mathsf c}\cup A_3)\big)$.

**Definition 3.1.3 (Mutual Independence)** Let $(\Omega,\mathcal{F},\mathbb{P})$ be a probability space and $A_1,\dots,A_n\in\mathcal{F}$. If for every nonempty subset $S$ of $\{1,\dots,n\}$

$$
\mathbb{P}\Big(\bigcap_{i\in S}A_i\Big)=\prod_{i\in S}\mathbb{P}(A_i),
$$
then $A_1,\dots,A_n$ are said to be **mutually independent**. A sequence of events $A_1,A_2,\dots$ is called mutually independent if every finite subcollection is mutually independent.

The definition requires $2^n-n-1$ equations to hold simultaneously.

**Definition 3.1.4 (Pairwise Independence)** Let $A_1,\dots,A_n\in\mathcal{F}$. If $\mathbb{P}(A_i\cap A_j)=\mathbb{P}(A_i)\mathbb{P}(A_j)$ for all $i\ne j$, then $A_1,\dots,A_n$ are said to be **pairwise independent**.

Mutual independence implies pairwise independence, but not conversely.

**Example 3.1.5 (Bernstein's Tetrahedron)** Paint one face of a fair regular tetrahedron red, yellow and blue, and paint the other three faces red, yellow and blue respectively. Let $A$, $B$ and $C$ be the events that, in one throw of the tetrahedron, the face touching the table contains red, yellow and blue, respectively. Then

$$
\mathbb{P}(A)=\mathbb{P}(B)=\mathbb{P}(C)=\frac12,\qquad\mathbb{P}(A\cap B)=\mathbb{P}(B\cap C)=\mathbb{P}(A\cap C)=\frac14,
$$
so $A,B,C$ are pairwise independent; but $\mathbb{P}(A\cap B\cap C)=\frac14\ne\frac18=\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)$, so they are not mutually independent.

Conversely, requiring the product formula only for the intersection of all the events is not enough either. For example, roll two fair dice and let $A=\{$the first die shows 1, 2 or 3$\}$, $B=\{$the first die shows 3, 4 or 5$\}$ and $C=\{$the sum of the two dice is 9$\}$. Then $\mathbb{P}(A\cap B\cap C)=\frac1{36}=\frac12\cdot\frac12\cdot\frac19$, but $\mathbb{P}(A\cap B)=\frac16\ne\frac14$. This is why Definition 3.1.3 must require the product formula for every nonempty subset $S$.

**Theorem 3.1.1** If $A_1,\dots,A_n$ are mutually independent, then replacing any number of them by their complements yields $n$ events that are still mutually independent.

**Proof** It suffices to treat the replacement of $A_1$ by $A_1^{\mathsf c}$; the general case follows by repeating the argument. For subsets $S$ not containing 1, the product formula is unchanged. For a subset $S=\{1\}\cup S'$ containing 1, let $B=\bigcap_{i\in S'}A_i$; then

$$
\mathbb{P}(A_1^{\mathsf c}\cap B)=\mathbb{P}(B)-\mathbb{P}(A_1\cap B)=\prod_{i\in S'}\mathbb{P}(A_i)-\mathbb{P}(A_1)\prod_{i\in S'}\mathbb{P}(A_i)=\mathbb{P}(A_1^{\mathsf c})\prod_{i\in S'}\mathbb{P}(A_i).\qquad\square
$$

### 3.1.4. Applications of Independence of Events

The most common use of independence is computing the probability that "at least one occurs": pass to complements by De Morgan's laws, which turns the union into an intersection, and then apply the product formula.

**Example 3.1.6** Suppose that in a certain region and period each person carries contraband with probability $0.04\%$, and a new test strip is used to screen 20 people in succession. Find the probability that the strip detects contraband. Let $A_i$ be the event "person $i$ carries contraband"; we may regard $A_1,\dots,A_{20}$ as mutually independent. By Theorem 3.1.1, $A_1^{\mathsf c},\dots,A_{20}^{\mathsf c}$ are also mutually independent, so

$$
\mathbb{P}\Big(\bigcup_{i=1}^{20}A_i\Big)=1-\mathbb{P}\Big(\bigcap_{i=1}^{20}A_i^{\mathsf c}\Big)=1-\prod_{i=1}^{20}\mathbb{P}(A_i^{\mathsf c})=1-(1-0.0004)^{20}\approx0.008.
$$
If 1000 people are screened, this probability becomes $1-0.9996^{1000}\approx33\%$: an event of small probability is almost certain to appear in a large number of independent repetitions.

The same argument proves the second part of the Borel–Cantelli lemma of [3.1.2](/3.1.2).

**Theorem 3.1.2 (Borel–Cantelli Lemma, Second Part)** If the sequence of events $\{A_n\}$ is mutually independent and $\sum_{n=1}^\infty\mathbb{P}(A_n)=\infty$, then $\mathbb{P}(\limsup_{n\to\infty}A_n)=1$.

**Proof** By De Morgan's laws, $(\limsup_nA_n)^{\mathsf c}=\bigcup_{n=1}^\infty\bigcap_{k=n}^\infty A_k^{\mathsf c}$, so by countable subadditivity it suffices to show that $\mathbb{P}(\bigcap_{k=n}^\infty A_k^{\mathsf c})=0$ for each $n$. For $m>n$, independence (Theorem 3.1.1) and the inequality $1-x\le\mathrm{e}^{-x}$ give

$$
\mathbb{P}\Big(\bigcap_{k=n}^\infty A_k^{\mathsf c}\Big)\le\mathbb{P}\Big(\bigcap_{k=n}^mA_k^{\mathsf c}\Big)=\prod_{k=n}^m\big(1-\mathbb{P}(A_k)\big)\le\exp\Big\{-\sum_{k=n}^m\mathbb{P}(A_k)\Big\}.
$$
Letting $m\to\infty$, the right side tends to 0. $\square$

**Example 3.1.7 (Gambler's Ruin)** Gambler A starts with $a$ yuan and resolves to stop as soon as he has won another $b$ yuan. Suppose A wins each round with probability $p=1/2$, the rounds are independent, each round is won or lost for 1 yuan, and A also stops when he has lost everything. Find the probability $q(a)$ that A is ruined.

Let $N=a+b$, let $B_k$ be the event "A, starting with $k$ yuan, is eventually ruined", and let $q(k)=\mathbb{P}(B_k)$, $k=0,1,\dots,N$. The boundary conditions are $q(0)=1$ and $q(N)=0$. Let $A$ denote the event that A wins the next round. Since the rounds are independent, the situation after winning a round is exactly the same as "starting with $k+1$ yuan", so $\mathbb{P}(B_k\mid A)=q(k+1)$, and likewise $\mathbb{P}(B_k\mid A^{\mathsf c})=q(k-1)$. The law of total probability gives the recursion

$$
q(k)=\mathbb{P}(A)\mathbb{P}(B_k\mid A)+\mathbb{P}(A^{\mathsf c})\mathbb{P}(B_k\mid A^{\mathsf c})=\frac12\big[q(k+1)+q(k-1)\big],\qquad1\le k\le N-1.
$$
Hence $q(k+1)-q(k)=q(k)-q(k-1)=\cdots=q(1)-q(0)$, and so $q(n)-1=n[q(1)-1]$. Taking $n=N$ and using $q(N)=0$ gives $q(1)-1=-1/N$, so

$$
q(a)=1-\frac aN=\frac b{a+b}.
$$
With a finite starting capital $a$, the greedier the target $b$, the larger the probability of ruin; if A keeps gambling indefinitely ($b\to\infty$), he is ruined with probability 1.

In general, if each round is won with probability $p\ne1/2$, set $r=(1-p)/p$; the same recursion $q(k)=pq(k+1)+(1-p)q(k-1)$ gives $q(k+1)-q(k)=r[q(k)-q(k-1)]$, and solving yields

$$
q(a)=\frac{r^a-r^N}{1-r^N}.
$$
For $p<1/2$ we have $r>1$, and $q(a)\to1$ as $b\to\infty$; for $p>1/2$ we have $r<1$, and $q(a)\to r^a<1$.

![Gambler's ruin: left, the ruin probability q(k) as a function of the initial capital k for total capital N = 20 (p = 0.45, 0.5, 0.55); right, capital paths of 8 fair games starting from a = 10, stopped on reaching 0 or 20](./plots/gamblers-ruin.py)

## 3.2. Random Variables

### 3.2.1. Why Random Variables

In the gambler's ruin model, if we care whether A has exactly $j$ yuan after round $k$, we can denote this by an event $A_{jk}$; many time points require many symbols, and if we also care about "how many rounds until ruin", describing it by events becomes even more complicated. If instead we let $X_k$ denote "A's capital after round $k$" and $R=\min\{n\colon X_n=0\text{ or }X_n=a+b\}$ the number of rounds played, everything becomes much simpler.

**Example 3.2.1** A person's blood pressure changes constantly; suppose A's systolic pressure ranges over 90–180 mmHg. Let $X$ be the measured systolic pressure of A, so that $X=125$ means a reading of 125 mmHg. Here the sample space of the experiment is $\Omega=[90,180]$, and $X$ is the function $X(\omega)=\omega$ on $\Omega$.

**Example 3.2.2** Draw one card at random from a deck of 52; each point of the sample space represents a card. Let $X$ be the rank of the card drawn; $X$ is a function from the sample space to $\mathbb{N}$, and for example

$$
\{X=3\}\overset{\text{def}}{=}\{\omega\colon X(\omega)=3\}=\{\clubsuit3,\diamondsuit3,\heartsuit3,\spadesuit3\}.
$$
For every $x\in\mathbb{R}$, $\{X\le x\}$ is an event; since the values of $X$ are numbers, we can perform mathematical operations on them.

**Example 3.2.3** Toss a fair coin twice and let $X$ be the number of heads: $\Omega=\{HH,HT,TH,TT\}$, and $X$ takes values in $\{0,1,2\}$. A family plans to have two children, whose sexes are independent and equally likely to be male or female; let $X$ be the number of girls: $\Omega=\{BB,BG,GB,GG\}$, and again $X$ takes values in $\{0,1,2\}$. The experiments differ, but the probability models are identical.

These examples show three advantages of introducing random variables:

- Simplicity: an event only says whether a phenomenon occurs, so describing a more complicated outcome requires many events; a random variable focuses attention on the quantity of interest.
- Quantification: the outcomes of many experiments are numbers in themselves (meter readings, stock prices, temperatures), and others, although not numerical, are closely tied to certain numbers.
- Generality: we care not only about which outcomes occur but about the probabilities with which they occur; different situations can share the same model (Example 3.2.3), just as many houses can be built from one blueprint.

### 3.2.2. Definition

A random variable assigns a number to each possible outcome of the experiment; it is a function from the sample space $\Omega$ to the real line $\mathbb{R}$, whose values may be discrete or continuous. Like a probability it is a map, but with a different domain: a probability is a function from the event field $\mathcal{F}$ to $[0,1]$, whereas a random variable is a function from $\Omega$ to $\mathbb{R}$. The randomness comes from the randomness of the outcome $\omega$; the function $X$ itself is deterministic. Many different random variables can be defined on the same sample space, each a numerical summary of some aspect of the experiment. To be able to compute $\mathbb{P}(X\le x)$ we also require $\{X\le x\}$ to be an event.

**Definition 3.2.1 (Random Variable)** Let $(\Omega,\mathcal{F})$ be a measurable space. A real-valued function $X(\omega)$ on $\Omega$ is called a **random variable** (abbreviated r.v.) on $(\Omega,\mathcal{F})$ if for every $x\in\mathbb{R}$

$$
\{\omega\colon X(\omega)\le x\}\in\mathcal{F}.
$$

By convention, random variables are denoted by capital letters $X,Y,Z,\dots$ (or Greek letters $\xi,\eta,\zeta$), with subscripts $X_1,X_2,\dots$ when more are needed; $\{X\le x\}$ stands for the event $\{\omega\colon X(\omega)\le x\}$, and the argument $\omega$ is written only when necessary. Since the event field is closed under countable operations,

$$
\{X>x\}=\{X\le x\}^{\mathsf c},\quad\{X<x\}=\bigcup_{n=1}^\infty\Big\{X\le x-\frac1n\Big\},\quad\{X\ge x\}=\{X<x\}^{\mathsf c},\quad\{X=x\}=\{X\le x\}\setminus\{X<x\}
$$
are also events. Conversely, the condition "$\{X\le x\}\in\mathcal{F}$" in the definition may be replaced by any one of $\{X>x\}\in\mathcal{F}$, $\{X<x\}\in\mathcal{F}$ or $\{X\ge x\}\in\mathcal{F}$, giving an equivalent definition. If $\Omega$ is countable and $\mathcal{F}=\mathcal{P}(\Omega)$, every real-valued function on $\Omega$ is a random variable.

**Example 3.2.4** Draw 13 cards at random from a deck of 52. Find the probability of exactly 5 clubs. Let $X$ be the number of clubs among the 13 cards; the event of interest is $\{X=5\}$. The sample space $\Omega$ consists of $\binom{52}{13}$ equally likely sample points, each sample point $\omega$ being an unordered hand of 13 cards; $X(\omega)$ is the number of clubs in $\omega$, and $\{X=5\}=\{\omega\colon\omega\text{ contains 5 clubs}\}$. Hence

$$
\mathbb{P}(X=5)=\binom{13}5\binom{39}8\Big/\binom{52}{13}.
$$
Writing out the function $X(\omega)$ does not help much with the computation, so we usually do not care how $X$ is defined on $\Omega$ in detail, but rather with what probabilities it takes its various values. From now on, rather than the original probability space $(\Omega,\mathcal{F},\mathbb{P})$, we shall mostly work with the probability space carried over to the real line by $X$. For this we must determine for which sets $A$ on the real line $\{X\in A\}$ is an event.

**Definition 3.2.2 (Borel Set)** Let $\mathcal{C}$ be the family of all half-open intervals $(a,b]$ in $\mathbb{R}$. The σ-algebra $\mathcal{B}=\sigma(\mathcal{C})$ generated by it is called the Borel σ-algebra on $\mathbb{R}$, and the elements of $\mathcal{B}$ are called **Borel sets**.

All open intervals, closed intervals, singletons and countable sets, as well as their countable unions, intersections and complements, are Borel sets; every set of real numbers met in practice is a Borel set.

**Theorem 3.2.1** Let $X$ be a random variable on a measurable space $(\Omega,\mathcal{F})$. Then for every Borel set $A$,

$$
\{X\in A\}\overset{\text{def}}{=}\{\omega\colon X(\omega)\in A\}\in\mathcal{F}.
$$

**Proof** For $A\subset\mathbb{R}$, write the preimage $X^{-1}(A)=\{\omega\colon X(\omega)\in A\}$ and let $\mathcal{A}=\{A\subset\mathbb{R}\colon X^{-1}(A)\in\mathcal{F}\}$. Preimages preserve set operations:

$$
X^{-1}\Big(\bigcup_iA_i\Big)=\bigcup_iX^{-1}(A_i),\qquad X^{-1}\Big(\bigcap_iA_i\Big)=\bigcap_iX^{-1}(A_i),\qquad X^{-1}(A^{\mathsf c})=\big[X^{-1}(A)\big]^{\mathsf c}.
$$
We first show that $\mathcal{A}$ is a σ-algebra: (a) $X^{-1}(\mathbb{R})=\Omega\in\mathcal{F}$, so $\mathbb{R}\in\mathcal{A}$; (b) if $A\in\mathcal{A}$, then $X^{-1}(A^{\mathsf c})=[X^{-1}(A)]^{\mathsf c}\in\mathcal{F}$, so $A^{\mathsf c}\in\mathcal{A}$; (c) if $A_i\in\mathcal{A}$, then $X^{-1}(\bigcup_iA_i)=\bigcup_iX^{-1}(A_i)\in\mathcal{F}$, so $\bigcup_iA_i\in\mathcal{A}$. Next, $\mathcal{C}\subset\mathcal{A}$, since $X^{-1}((a,b])=\{X\le b\}\setminus\{X\le a\}\in\mathcal{F}$. Since $\mathcal{B}$ is the smallest σ-algebra containing $\mathcal{C}$, we conclude $\mathcal{B}\subset\mathcal{A}$. $\square$

Thus $\mathbb{P}(X\in A)$ is defined for every Borel set $A$; $P_X(A)=\mathbb{P}(X\in A)$ is a probability measure on $(\mathbb{R},\mathcal{B})$, called the distribution of $X$. $(\mathbb{R},\mathcal{B},P_X)$ is the probability space obtained through the map $X$: like sand, the probability has been transported from $\Omega$ to the real line.

### 3.2.3. Functions of Random Variables

**Definition 3.2.3 (Measurable Function)** A real function $g\colon\mathbb{R}\to\mathbb{R}$ is called Borel measurable, or simply a **measurable function**, if $\{x\colon g(x)\le a\}$ is a Borel set for every $a\in\mathbb{R}$. Measurable functions $g\colon\mathbb{R}^n\to\mathbb{R}$ of $n$ variables are defined similarly (with $\mathcal{B}$ replaced by the $n$-dimensional Borel σ-algebra on $\mathbb{R}^n$ generated by the rectangles $(a_1,b_1]\times\cdots\times(a_n,b_n]$).

Continuous functions, step functions, monotone functions and linear combinations of such functions are all measurable.

**Theorem 3.2.2** If $X$ is a random variable on a measurable space $(\Omega,\mathcal{F})$ and $g$ is a measurable function, then $Y=g(X)$ is a random variable on $(\Omega,\mathcal{F})$.

**Proof** For every $a\in\mathbb{R}$, let $B=\{x\colon g(x)\le a\}$; then $B\in\mathcal{B}$, and by Theorem 3.2.1,

$$
\{Y\le a\}=\{\omega\colon g(X(\omega))\le a\}=\{\omega\colon X(\omega)\in B\}=\{X\in B\}\in\mathcal{F}.\qquad\square
$$

In exactly the same way one shows that if $X_1,\dots,X_n$ are random variables on $(\Omega,\mathcal{F})$ and $g$ is a measurable function of $n$ variables, then $g(X_1,\dots,X_n)$ is also a random variable. Unless stated otherwise, all real functions of one or several variables used later in this course are measurable. This gives the usual ways of constructing random variables:

1. Arithmetic operations: $aX+bY$, $XY$, $X/Y$ (where $Y\ne0$), $a,b\in\mathbb{R}$;
2. Limits: $\sup_nX_n$, $\inf_nX_n$, $\limsup_nX_n$, $\liminf_nX_n$, $\lim_nX_n$ (if it exists);
3. Transformations: $\max\{X,Y\}$, $\min\{X,Y\}$, $\sin X$, $\mathrm{e}^X$, $X^+=\max\{X,0\}$, $X^-=\max\{-X,0\}$, $\lvert X\rvert^p$, and so on;
4. Composition of functions.

For example, the indicator function $\boldsymbol{1}_A(\omega)$ of an event $A\in\mathcal{F}$ (equal to 1 for $\omega\in A$ and 0 otherwise) is a random variable, because $\{\boldsymbol{1}_A\le x\}$ can only be $\varnothing$, $A^{\mathsf c}$ or $\Omega$.

## 3.3. Independence of Random Variables

### 3.3.1. Definition

By analogy with independence of events, two random variables should be independent when no information about the value of one changes the probabilities with which the other takes its values. Since random variables are described by the events $\{X\le x\}$, we define:

**Definition 3.3.1 (Independence of Random Variables)** Let $X_1,\dots,X_n$ be random variables on $(\Omega,\mathcal{F},\mathbb{P})$. If for all real numbers $x_1,\dots,x_n$

$$
\mathbb{P}(X_1\le x_1,\dots,X_n\le x_n)=\mathbb{P}(X_1\le x_1)\cdots\mathbb{P}(X_n\le x_n),
$$
then the random variables $X_1,\dots,X_n$ are said to be mutually independent.

Here $\mathbb{P}(X_1\le x_1,\dots,X_n\le x_n)$ is shorthand for $\mathbb{P}(\{X_1\le x_1\}\cap\cdots\cap\{X_n\le x_n\})$. Unlike the case of events, only the product formula for all $n$ random variables is required, not one for each subset separately: the product formulas for subsets follow from the full one, because letting $x_i\to+\infty$ makes the event $\{X_i\le x_i\}$ increase to $\Omega$. For $n=3$, for instance, continuity of probability (Theorem 2.2.1 in [3.1.2](/3.1.2)) gives

$$
\begin{aligned}
\mathbb{P}(X_1\le x_1,X_2\le x_2)&=\mathbb{P}\Big(\bigcup_{m=1}^\infty\{X_1\le x_1,X_2\le x_2,X_3\le m\}\Big)=\lim_{m\to\infty}\mathbb{P}(X_1\le x_1,X_2\le x_2,X_3\le m)\\
&=\mathbb{P}(X_1\le x_1)\mathbb{P}(X_2\le x_2)\lim_{m\to\infty}\mathbb{P}(X_3\le m)=\mathbb{P}(X_1\le x_1)\mathbb{P}(X_2\le x_2).
\end{aligned}
$$
The product formula for events contains no parameter that can be sent to $\Omega$; this is the difference between the two cases.

**Theorem 3.3.1** If $X_1,\dots,X_n$ are mutually independent, then for any Borel sets $A_1,\dots,A_n$ the events $\{X_1\in A_1\},\dots,\{X_n\in A_n\}$ are mutually independent.

The proof requires the monotone class method of measure theory and is omitted here. The theorem shows that independence of random variables really does imply that "all events concerning the individual random variables are independent". For example, if $X$ and $Y$ are independent, then $\mathbb{P}(a<X\le b,\ Y>c)=\mathbb{P}(a<X\le b)\mathbb{P}(Y>c)$.

**Example 3.3.1** Let $X_1,X_2$ be mutually independent, each uniformly distributed on $\{1,\dots,6\}$ (the results of two fair dice). By Theorem 3.3.1, $\mathbb{P}(X_1\text{ is even},\ X_2\ge5)=\frac12\cdot\frac13=\frac16$. But $X_1$ and $S=X_1+X_2$ are not independent: $\mathbb{P}(X_1=1,S=12)=0\ne\mathbb{P}(X_1=1)\mathbb{P}(S=12)=\frac16\cdot\frac1{36}$.

### 3.3.2. Independent Sequences and i.i.d. Random Variables

**Definition 3.3.2 (Independent Sequence)** If the random variables $X_1,\dots,X_n$ are mutually independent for every $n$, the sequence of random variables $\{X_n\}$ is called mutually independent, or an independent sequence.

**Definition 3.3.3 (Independent and Identically Distributed)** If the random variables $X_1,X_2,\dots$ are mutually independent and have the same distribution (that is, the same **distribution function** $F(x)=\mathbb{P}(X_i\le x)$, see [3.1.5](/3.1.5)), they are called **independent and identically distributed** (abbreviated i.i.d.), written $X_1,X_2,\dots\overset{\text{iid}}{\sim}F$.

An i.i.d. sequence is the mathematical model of repeated trials and the model of a simple random sample in statistics ([3.2.1](/3.2.1)); the laws of large numbers and the central limit theorem ([3.1.12](/3.1.12), [3.1.13](/3.1.13)) are both about such sequences.

**Theorem 3.3.2** Let the random variables $X_1,\dots,X_n$ be mutually independent, let $g_1,\dots,g_n$ be measurable functions of one variable, and let $\varphi$ be a measurable function of $k$ variables ($k<n$). Then

1. the random variables $g_1(X_1),\dots,g_n(X_n)$ are mutually independent;
2. the random variables $\varphi(X_1,\dots,X_k),X_{k+1},\dots,X_n$ are mutually independent.

**Proof** (1) For all real $y_1,\dots,y_n$, let $B_i=\{x\colon g_i(x)\le y_i\}$; these are Borel sets. By Theorem 3.3.1,

$$
\mathbb{P}\big(g_1(X_1)\le y_1,\dots,g_n(X_n)\le y_n\big)=\mathbb{P}(X_1\in B_1,\dots,X_n\in B_n)=\prod_{i=1}^n\mathbb{P}(X_i\in B_i)=\prod_{i=1}^n\mathbb{P}\big(g_i(X_i)\le y_i\big).
$$
(2) The proof requires a multivariate extension of Theorem 3.3.1 (the random vector $(X_1,\dots,X_k)$ is independent of $X_{k+1},\dots,X_n$) and is omitted here. $\square$

Theorem 3.3.2 extends as follows: if independent random variables are split into disjoint groups, functions of the different groups are still mutually independent. For example, if $(X_1,X_2)$ and $(X_3,X_4)$ are independent, then $X_2/X_1^2$ and $(X_3+X_4)/2$ are independent.

## Summary

| Topic | Key points |
|---|---|
| Independence of events | $\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B)$; different from mutual exclusiveness; preserved under complements |
| Conditional independence | Independence under $\mathbb{P}(\cdot\mid C)$; neither implies nor is implied by independence |
| Collections of events | Mutual independence requires the product formula for all subsets; pairwise independence does not imply mutual independence |
| Random variables | Functions $\Omega\to\mathbb{R}$ for which $\{X\le x\}$ is an event; $\{X\in A\}$ is an event for every Borel set $A$; compositions with measurable functions are random variables |
| Independence of random variables | $\mathbb{P}(X_1\le x_1,\dots,X_n\le x_n)=\prod\mathbb{P}(X_i\le x_i)$; functions of independent random variables are independent; i.i.d. sequences |

For independence, random variables and independence of random variables, when it is not yet known whether a statement holds, go back to the definition and check it; when it is known to hold, reason directly with the properties. Counterexamples are the usual tool for telling apart subtle differences between concepts (the different notions of independence), analogy for mastering a new concept (from independence of events to independence of random variables), and recursion and induction for random experiments with an indefinite number of steps (the gambler's ruin).
