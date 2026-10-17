---
title: Probability Models and Their Properties
description: Random phenomena and the development of probability theory; sample spaces, events and the axioms of probability; classical and geometric probability models and the Bertrand paradox; properties derived from the axioms (inclusion–exclusion, the Boole and Bonferroni inequalities); counting in the four kinds of random sampling and in random allocation.
source_hash: 40f6f419b9a8
---

Probability theory studies the quantitative laws of random phenomena. This chapter first explains what a probability model consists of: the sample space of an experiment and a probability satisfying three axioms. The two most basic models are the classical model, with finitely many equally likely outcomes, and the geometric model, which assigns probability in proportion to volume; the Bertrand paradox warns that "equally likely" must be made precise before anything can be computed. We then derive from the axioms a series of identities and inequalities for probabilities, which serve as the basic tools for computation and proof throughout the course. Finally we discuss counting in the classical model: the four sampling schemes (with or without replacement, ordered or unordered) and their correspondence with "placing particles into boxes". The next chapter, [3.1.2](/3.1.2), makes the intuitive models of this chapter rigorous as probability spaces and introduces conditional probability. The set operations used here are reviewed in discrete mathematics, [1.2.1](/1.2.1).

## 1.1. Random Phenomena and Probability Theory

### 1.1.1. Reasoning under Uncertainty

Randomness is everywhere: the motion of elementary particles, the combination of genetic factors and the behavior of people in society all involve uncertainty. Many everyday judgments can only be made precise from a probabilistic point of view, for example:

- Why are many sports (ball games, diving) decided over several rounds?
- Why do investors usually choose a portfolio instead of putting everything into the product with the highest expected return?
- Smoking is harmful to health, so why are some smokers still in robust health?
- A doctor says that only one in ten patients with a certain disease survives, and then adds: "You are lucky, because the last nine patients I treated all died." What is wrong with this consolation?

Making decisions in an uncertain environment (whether to switch doors in a television game show, how to monitor battery life on a production line) requires a language in which one can calculate. There are two basic ways of acquiring knowledge: deduction, which derives theorems from axioms (Euclidean geometry, Newtonian mechanics), and induction, which extracts regularities from data (Mendel's laws of inheritance, Kepler's laws of planetary motion). Probability theory is a deductive mathematical theory: it derives the laws of random phenomena from the axioms of probability. Statistics is an inductive method: it uses probability models to infer the unknown from data. This course lays the foundation for later statistics courses (such as [3.2](/3.2) Statistical Inference), and it is also an independent tool for analyzing random problems.

### 1.1.2. A Brief History

Probability theory originated in the analysis of gambling problems, grew into a mathematical discipline over more than two centuries, and received its axiomatic foundation from measure theory in the 1930s.

| Year | Event |
|---|---|
| 1654 | Pascal and Fermat solve the "problem of points" (how to divide the stakes fairly when a game is interrupted) by different methods in their correspondence; this is usually regarded as the birth of probability theory |
| 1657 | Huygens publishes *De ratiociniis in ludo aleae* (On Reasoning in Games of Chance), the first systematic work on probability, which discusses mathematical expectation |
| 1713 | Jacob Bernoulli's posthumous *Ars Conjectandi* (The Art of Conjecturing) appears, containing the first law of large numbers |
| 1733 | de Moivre derives the normal curve as an approximation to the binomial distribution |
| 1763 | Bayes's posthumous "An Essay towards Solving a Problem in the Doctrine of Chances" is published |
| 1809 | Gauss obtains the normal distribution in his study of measurement errors and gives a probabilistic justification of least squares |
| 1812 | Laplace publishes *Théorie analytique des probabilités*, the principal work on probability of the nineteenth century |
| 1837 | Poisson publishes his research on the probability of judgments, introducing the Poisson distribution and promoting the term "law of large numbers" |
| 1867 | Chebyshev publishes "On Mean Values", proving the law of large numbers with Chebyshev's inequality |
| 1889 | Bertrand poses the Bertrand paradox in *Calcul des probabilités*, exposing the limits of the classical definition |
| 1900 | Hilbert's sixth problem calls for the axiomatization of physics, including probability theory |
| 1906 | Markov introduces Markov chains |
| 1909 | Borel proves the strong law of large numbers |
| 1922 | Lindeberg gives the Lindeberg condition for the central limit theorem |
| 1933 | Kolmogorov publishes *Grundbegriffe der Wahrscheinlichkeitsrechnung* (Foundations of the Theory of Probability), building an axiomatic system for probability on measure theory |

Kolmogorov's axiomatic system treats events as sets, probability as a measure, mathematical expectation as an integral and independence of random variables as an analogue of orthogonality of functions, and thereby turns probability theory into a deductive mathematical discipline. This chapter and the next present the elementary part of that system.

## 1.2. Probability Models

A probability model has two ingredients: a sample space describing all possible outcomes of an experiment, and a probability assigned to sets of outcomes (events).

### 1.2.1. The Sample Space

**Definition 1.2.1 (Sample Space)** Every probability model is associated with an experiment, which produces an outcome. The set of all possible outcomes of the experiment is called the **sample space**, denoted $\Omega$; its elements are called sample points and denoted $\omega$.

The outcomes in a sample space must be mutually exclusive (exactly one of them occurs in each run of the experiment) and collectively exhaustive (no outcome outside the sample space can occur); there may be finitely or infinitely many of them. There is no restriction on what constitutes an experiment, but a probability model involves a single experiment: tossing a coin three times in succession is one experiment, whose sample space has $2^3=8$ outcomes, not three experiments.

The same experiment can be modeled in different ways depending on the question of interest. In choosing $\Omega$ one should include enough detail while avoiding unnecessary complication.

**Example 1.2.1** Two games both consist of ten successive coin tosses. In game one, player A wins one yuan for every head. In game two, A wins money on every toss: one yuan per toss up to and including the first head, then two yuan per toss until the second head, and in general the amount won per toss doubles after each head. The payoff of game one depends only on the number of heads among the ten tosses, so we may take $\Omega=\{0,1,\dots,10\}$; the payoff of game two also depends on the order in which the heads appear, so the sample space must consist of all $2^{10}$ sequences of heads and tails.

**Example 1.2.2 (Sequential Models)** Many experiments have a sequential character, such as rolling a four-sided die twice or observing a stock over five days. The sample space of two rolls of a four-sided die is

$$
\Omega=\{(i,j)\colon i,j\in\{1,2,3,4\}\},
$$
with 16 outcomes. It can also be described by a sequential tree diagram: the root branches into 4 according to the result of the first roll, each branch splits into 4 according to the second roll, and the 16 leaves correspond to the 16 outcomes.

**Example 1.2.3 (A Continuous Sample Space)** A and B agree to meet at a certain time, and each arrives with a delay between 0 and 1 hour. Taking the two delays as coordinates, the sample space is the unit square

$$
\Omega=\{(x,y)\colon 0\le x\le1,\ 0\le y\le1\}=[0,1]\times[0,1].
$$

### 1.2.2. Events and the Axioms of Probability

**Definition 1.2.2 (Event)** A subset of the sample space, that is, a set of outcomes of the experiment, is called an **event**. If the outcome $\omega$ of the experiment lies in $A$, we say that the event $A$ occurs; otherwise $A$ does not occur. $\Omega$ is called the sure event and $\varnothing$ the impossible event; an event $\{\omega\}$ consisting of a single sample point is called an elementary event.

Relations and operations on events are exactly the relations and operations on sets: $A\cup B$ means that at least one of $A$ and $B$ occurs, $A\cap B$ (also written $AB$) that both occur, $A^{\mathsf c}$ that $A$ does not occur, and $A\subset B$ that the occurrence of $A$ implies that of $B$; if $A\cap B=\varnothing$, the events $A$ and $B$ are called mutually exclusive (disjoint). **De Morgan's laws** $(\bigcup_iA_i)^{\mathsf c}=\bigcap_iA_i^{\mathsf c}$ and $(\bigcap_iA_i)^{\mathsf c}=\bigcup_iA_i^{\mathsf c}$ are used constantly in computing the probability that "at least one occurs".

A probability assigns a number to each event, describing our degree of belief that the event occurs, from "impossible" (0) to "completely certain" (1). It must satisfy the following axioms.

**Definition 1.2.3 (Probability Model)** A **probability model** consists of a sample space $\Omega$ and a function $\mathbb{P}$ defined on events; $\mathbb{P}(A)$ is called the probability of the event $A$, and $\mathbb{P}$ satisfies the **axioms of probability**:

1. Nonnegativity: $\mathbb{P}(A)\ge0$ for every event $A$;
2. Normalization: $\mathbb{P}(\Omega)=1$;
3. **Countable additivity**: if $A_1,A_2,\dots$ are pairwise disjoint events, then
$$
\mathbb{P}\Big(\bigcup_{i=1}^\infty A_i\Big)=\sum_{i=1}^\infty\mathbb{P}(A_i).
$$

Three remarks on the axioms. First, there is no need for an additional axiom $\mathbb{P}(A)\le1$: it follows from the three axioms (Corollary 1.3.1). Second, if additivity were required only for two (and hence finitely many) disjoint events, problems on infinite sample spaces could not be handled; Example 1.2.4 shows why countable additivity is needed. Third, can every subset of the sample space be assigned a probability? For continuous sample spaces the answer is no: events must be restricted to a family of subsets with suitable closure properties, the σ-algebra of [3.1.2](/3.1.2).

**Example 1.2.4** Let $\Omega=\{1,2,\dots\}$ and $\mathbb{P}(\{n\})=2^{-n}$, $n=1,2,\dots$. What is the probability that the outcome is even? By countable additivity,

$$
\mathbb{P}(\{2,4,6,\dots\})=\mathbb{P}(\{2\})+\mathbb{P}(\{4\})+\cdots=\frac1{2^2}+\frac1{2^4}+\cdots=\frac{1/4}{1-1/4}=\frac13.
$$
With finite additivity alone, this probability could not be computed from the probabilities of the elementary events.

### 1.2.3. Discrete Models and the Classical Model

When the sample space consists of finitely (or countably) many outcomes, additivity implies that the probability of any event is the sum of the probabilities of its outcomes: $\mathbb{P}(A)=\sum_{\omega\in A}\mathbb{P}(\{\omega\})$.

**Example 1.2.5** Roll a fair four-sided die twice (Example 1.2.2); each of the 16 outcomes has probability $1/16$. Denote the results of the first and second rolls by $X$ and $Y$. Then

$$
\mathbb{P}\big((X,Y)=(1,1)\text{ or }(1,2)\big)=\frac2{16},\quad\mathbb{P}(X=1)=\frac4{16},\quad\mathbb{P}(X+Y\text{ is odd})=\frac8{16},\quad\mathbb{P}\big(\min(X,Y)=2\big)=\frac5{16}.
$$
The last event consists of $(2,2),(2,3),(2,4),(3,2),(4,2)$.

**Definition 1.2.4 (Classical Probability Model)** If the sample space $\Omega$ consists of $n$ equally likely outcomes, that is, each elementary event has probability $1/n$, then for every event $A$,

$$
\mathbb{P}(A)=\frac{\#A}{n}=\frac{\text{number of outcomes in }A}{n}.
$$
Such a probability model is called the **classical probability model** (discrete uniform probability). Here $\#A$ denotes the number of elements of the set $A$.

The classical model reduces the computation of probabilities to counting; Sections 1.4 and 1.5 are devoted to counting methods.

### 1.2.4. Continuous Models and Geometric Probability

**Example 1.2.6 (The Meeting Problem)** In Example 1.2.3, whoever arrives first waits 15 minutes and leaves if the other has not appeared. What is the probability that the two meet? Define the probability of a subset of $\Omega=[0,1]^2$ to be its area; this satisfies the three axioms of probability. The two meet if and only if their delays differ by at most $1/4$ hour, that is, on

$$
M=\{(x,y)\in\Omega\colon\lvert x-y\rvert\le1/4\},
$$
and the required probability is the area of $M$, $1-(3/4)^2=7/16$ (the square minus two right triangles with legs $3/4$).

![The meeting problem: the area 7/16 of the band M in the unit square is the probability of meeting; the scatter shows 400 simulations, and points falling in M are meetings](./plots/meeting-problem.py)

In general, write $\mathbb{R}^r=\{(x_1,\dots,x_r)\colon x_i\in\mathbb{R}\}$, and for a subset $A$ of $\mathbb{R}^r$ let $m(A)=\int_A\mathrm{d}x_1\cdots\mathrm{d}x_r$ denote its volume (length and area for $r=1,2$).

**Definition 1.2.5 (Geometric Probability)** Suppose the sample space $\Omega\subset\mathbb{R}^r$ has volume $0<m(\Omega)<\infty$ and all outcomes in $\Omega$ are equally likely (the probability of landing in a region depends only on its volume). Then the probability of an event $A\subset\Omega$ is

$$
\mathbb{P}(A)=\frac{m(A)}{m(\Omega)}.
$$
Such a probability model is called **geometric probability** (continuous uniform probability).

In geometric probability every single point has probability zero, so an event of probability zero is not necessarily impossible.

### 1.2.5. Models and Reality: The Bertrand Paradox

**Example 1.2.7 (The Bertrand Paradox)** Choose a chord at random in a circle of radius 1. What is the probability that its length is at least $\sqrt3$? ($\sqrt3$ is the side length of the inscribed equilateral triangle.) Let $A$ denote the event that the chord has length at least $\sqrt3$.

1. Suppose the endpoints of the chord are equally likely to lie anywhere on the circle. Fix one endpoint $x_0$; the position $y$ of the other endpoint (measured by the central angle) is uniform on $[0,2\pi)$, and $A=\{y\colon2\pi/3\le y\le4\pi/3\}$, so $\mathbb{P}(A)=1/3$.
2. Suppose the midpoint of the chord is equally likely to lie anywhere on the radius perpendicular to the chord. The chord has length at least $\sqrt3$ if and only if its midpoint lies within distance $1/2$ of the center, so $\mathbb{P}(A)=1/2$.
3. Suppose the midpoint of the chord is equally likely to lie anywhere in the disk. Then $A$ occurs if and only if the midpoint lies in the concentric disk of radius $1/2$, while $\Omega$ is the whole disk, so $\mathbb{P}(A)=(1/2)^2=1/4$.

![The Bertrand paradox: 120 chords drawn by each of three ways of "choosing a chord at random" (blue chords have length at least √3); the titles give the exact probability and the frequency in 100,000 simulations](./plots/bertrand-paradox.py)

All three answers are correct, because they answer three different questions: "choose a chord at random" does not specify the random mechanism, and different assumptions of equal likelihood lead to different probability models. This is the Bertrand paradox. In modeling we must therefore state clearly what the sample space is and what "equally likely" means; whether a model fits reality must be judged from the actual mechanism of the experiment (or from data).

## 1.3. Properties of Probability

All properties in this section follow from the axioms of probability alone. The basic tools of proof are: decomposing an event into a union of disjoint events and applying countable additivity; induction on the number of events; and passing to complements.

**Property 1.3.1** $\mathbb{P}(\varnothing)=0$.

**Proof** Since $\Omega=\Omega\cup\varnothing\cup\varnothing\cup\cdots$ and these events are pairwise disjoint, countable additivity and normalization give $1=\mathbb{P}(\Omega)=1+\mathbb{P}(\varnothing)+\mathbb{P}(\varnothing)+\cdots$, that is, $\mathbb{P}(\varnothing)+\mathbb{P}(\varnothing)+\cdots=0$. By nonnegativity, $\mathbb{P}(\varnothing)=0$. $\square$

**Property 1.3.2 (Finite Additivity)** If the events $A_1,\dots,A_n$ are pairwise disjoint, then $\mathbb{P}\big(\bigcup_{i=1}^nA_i\big)=\sum_{i=1}^n\mathbb{P}(A_i)$.

**Proof** Let $A_{n+1}=A_{n+2}=\cdots=\varnothing$. Then $\bigcup_{i=1}^nA_i=\bigcup_{i=1}^\infty A_i$ and $A_1,A_2,\dots$ are pairwise disjoint. By countable additivity and Property 1.3.1, $\mathbb{P}(\bigcup_{i=1}^nA_i)=\sum_{i=1}^\infty\mathbb{P}(A_i)=\sum_{i=1}^n\mathbb{P}(A_i)$. $\square$

**Property 1.3.3** For every event $A$, $\mathbb{P}(A^{\mathsf c})=1-\mathbb{P}(A)$.

**Proof** $A\cap A^{\mathsf c}=\varnothing$ and $A\cup A^{\mathsf c}=\Omega$, so by Property 1.3.2, $1=\mathbb{P}(A)+\mathbb{P}(A^{\mathsf c})$. $\square$

**Property 1.3.4** If $A\subset B$, then $\mathbb{P}(B\setminus A)=\mathbb{P}(B)-\mathbb{P}(A)$.

**Proof** $B=A\cup(B\setminus A)$ with $A\cap(B\setminus A)=\varnothing$, so by Property 1.3.2, $\mathbb{P}(B)=\mathbb{P}(A)+\mathbb{P}(B\setminus A)$. $\square$

**Corollary 1.3.1** (1) (Monotonicity) If $A\subset B$, then $\mathbb{P}(A)\le\mathbb{P}(B)$. (2) For every event $A$, $0\le\mathbb{P}(A)\le1$.

**Proof** (1) By Property 1.3.4 and nonnegativity, $\mathbb{P}(B)-\mathbb{P}(A)=\mathbb{P}(B\setminus A)\ge0$. (2) Follows from $A\subset\Omega$ and (1). $\square$

**Property 1.3.5 (Addition Rule)** For any events $A,B$, $\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$.

**Proof** $A\cup B=A\cup(B\setminus A)$, a disjoint union, and $B\setminus A=B\setminus(A\cap B)$ with $A\cap B\subset B$. By Properties 1.3.2 and 1.3.4,

$$
\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}\big(B\setminus(A\cap B)\big)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B).\qquad\square
$$

Similarly, decomposing the union into disjoint pieces gives $\mathbb{P}(A\cup B\cup C)=\mathbb{P}(A)+\mathbb{P}(A^{\mathsf c}\cap B)+\mathbb{P}(A^{\mathsf c}\cap B^{\mathsf c}\cap C)$.

**Corollary 1.3.2 (Boole's Inequality)** For any events $A_1,\dots,A_n$, $\mathbb{P}\big(\bigcup_{i=1}^nA_i\big)\le\sum_{i=1}^n\mathbb{P}(A_i)$. This property is also called finite subadditivity.

**Proof** By Property 1.3.5, $\mathbb{P}(A\cup B)\le\mathbb{P}(A)+\mathbb{P}(B)$; then induct on $n$. $\square$

**Property 1.3.6 (Inclusion–Exclusion Identity)** For any events $A_1,\dots,A_n$,

$$
\mathbb{P}\Big(\bigcup_{i=1}^nA_i\Big)=\sum_{1\le i\le n}\mathbb{P}(A_i)-\sum_{1\le i<j\le n}\mathbb{P}(A_i\cap A_j)+\sum_{1\le i<j<k\le n}\mathbb{P}(A_i\cap A_j\cap A_k)-\cdots+(-1)^{n-1}\mathbb{P}(A_1\cap\cdots\cap A_n).
$$

**Proof** Induct on $n$; the case $n=2$ is the addition rule. Suppose the statement holds for $n-1$ events. By the addition rule,

$$
\mathbb{P}\Big(\bigcup_{i=1}^nA_i\Big)=\mathbb{P}\Big(\bigcup_{i=1}^{n-1}A_i\Big)+\mathbb{P}(A_n)-\mathbb{P}\Big(\bigcup_{i=1}^{n-1}(A_i\cap A_n)\Big).
$$
Apply the induction hypothesis to the first and third terms on the right (the latter is a union of the $n-1$ events $A_i\cap A_n$): the first term yields the terms for intersections not involving $A_n$, the third yields those involving $A_n$ (with the opposite sign), and together they form exactly the inclusion–exclusion expansion for $n$ events. $\square$

This is the probabilistic form of the **inclusion–exclusion principle** for counting.

**Property 1.3.7 (Bonferroni and Kounias Inequalities)** For any events $A_1,\dots,A_n$,

$$
\sum_{1\le i\le n}\mathbb{P}(A_i)-\sum_{1\le i<j\le n}\mathbb{P}(A_i\cap A_j)\;\le\;\mathbb{P}\Big(\bigcup_{i=1}^nA_i\Big)\;\le\;\min_{1\le k\le n}\Big\{\sum_{1\le i\le n}\mathbb{P}(A_i)-\sum_{i\ne k}\mathbb{P}(A_i\cap A_k)\Big\}.
$$

**Proof** The left inequality (Bonferroni's inequality) is proved by induction on $n$; the case $n=1$ is trivial. By the identity in the preceding proof, the induction hypothesis and Boole's inequality $\mathbb{P}(\bigcup_{i<n}(A_i\cap A_n))\le\sum_{i<n}\mathbb{P}(A_i\cap A_n)$,

$$
\mathbb{P}\Big(\bigcup_{i=1}^nA_i\Big)\ge\sum_{i<n}\mathbb{P}(A_i)-\sum_{i<j<n}\mathbb{P}(A_i\cap A_j)+\mathbb{P}(A_n)-\sum_{i<n}\mathbb{P}(A_i\cap A_n),
$$
which is exactly the left side for $n$ events. For the right inequality (Kounias's inequality), fix $k$; then $\bigcup_iA_i=A_k\cup\bigcup_{i\ne k}(A_i\setminus A_k)$, and Boole's inequality together with Property 1.3.4 gives $\mathbb{P}(\bigcup_iA_i)\le\mathbb{P}(A_k)+\sum_{i\ne k}\big[\mathbb{P}(A_i)-\mathbb{P}(A_i\cap A_k)\big]$. Finally take the minimum over $k$. $\square$

Truncating the inclusion–exclusion identity after the first $m$ sums gives an upper bound when $m$ is odd and a lower bound when $m$ is even; Boole's and Bonferroni's inequalities are the cases $m=1,2$.

**Property 1.3.8 (Countable Subadditivity)** For any sequence of events $A_1,A_2,\dots$, $\mathbb{P}\big(\bigcup_{i=1}^\infty A_i\big)\le\sum_{i=1}^\infty\mathbb{P}(A_i)$.

**Proof** Let $B_1=A_1$ and $B_n=A_n\setminus\bigcup_{i=1}^{n-1}A_i$ for $n\ge2$. Then the $B_n$ are pairwise disjoint, $B_n\subset A_n$, and $\bigcup_{i=1}^\infty A_i=\bigcup_{i=1}^\infty B_i$. By countable additivity and monotonicity, $\mathbb{P}(\bigcup_iA_i)=\sum_i\mathbb{P}(B_i)\le\sum_i\mathbb{P}(A_i)$. $\square$

**Property 1.3.9** For any sequence of events $A_1,A_2,\dots$, $\mathbb{P}\big(\bigcap_{i=1}^\infty A_i\big)\ge1-\sum_{i=1}^\infty\mathbb{P}(A_i^{\mathsf c})$; in particular, $\mathbb{P}(A_1\cap A_2)\ge1-\mathbb{P}(A_1^{\mathsf c})-\mathbb{P}(A_2^{\mathsf c})$.

**Proof** By Property 1.3.3, De Morgan's laws and Property 1.3.8,

$$
\mathbb{P}\Big(\bigcap_{i=1}^\infty A_i\Big)=1-\mathbb{P}\Big(\bigcup_{i=1}^\infty A_i^{\mathsf c}\Big)\ge1-\sum_{i=1}^\infty\mathbb{P}(A_i^{\mathsf c}).
$$
Taking $A_3=A_4=\cdots=\Omega$ and using Property 1.3.1 gives the second statement. $\square$

Property 1.3.9 says that the probability that several "high-probability events" occur simultaneously is still large, provided the sum of the probabilities that they fail is small. The Bonferroni method for constructing simultaneous confidence regions in statistics is based on this inequality.

**Example 1.3.1** Place $n$ distinguishable balls at random into $N$ boxes ($N\le n$), each ball being equally likely to go into each box, with no limit on the number of balls per box. Find the probability that no box is empty. Let $A_i$ be the event that box $i$ is empty. The $k$ specified boxes $i_1<\dots<i_k$ are all empty when all balls go into the remaining $N-k$ boxes, which has probability $\big(\frac{N-k}N\big)^n$. By the inclusion–exclusion identity,

$$
\mathbb{P}(\text{no box is empty})=1-\mathbb{P}\Big(\bigcup_{i=1}^NA_i\Big)=1-\sum_{k=1}^N(-1)^{k-1}\binom Nk\Big(1-\frac kN\Big)^n=\sum_{k=0}^N(-1)^k\binom Nk\Big(1-\frac kN\Big)^n.
$$
Multiplying by $N^n$ gives the number of surjections from an $n$-element set onto an $N$-element set, $\sum_{k=0}^N(-1)^k\binom Nk(N-k)^n$, a classical result of combinatorics.

## 1.4. Random Sampling and Random Allocation

Computations in the classical model come down to counting, and the key to counting is a clear description of the sample space. This section takes "drawing balls from an urn" as the prototype.

### 1.4.1. Permutations and Combinations

- The number of permutations of $n$ distinct objects is $n!$;
- The number of ways to choose $k$ of $n$ distinct objects and arrange them in a row is $P_n^k=n(n-1)\cdots(n-k+1)=\dfrac{n!}{(n-k)!}$;
- The number of ways to choose $k$ of $n$ distinct objects (without regard to order) is $\dbinom nk=\dfrac{n!}{k!\,(n-k)!}$.

For example, calling on students at random in class (one at a time, with repetition allowed), electing a class president and vice-president (no repetition, order matters), and selecting students for a choir (no repetition, order irrelevant) correspond to the different sampling schemes below.

### 1.4.2. Four Sampling Schemes

Consider drawing $n$ times from an urn containing $M$ balls numbered $1,\dots,M$.

**Definition 1.4.1 (Sampling with and without Replacement)** If each ball drawn is returned to the urn before the next draw, the scheme is called **sampling with replacement**; each number $a_i$ drawn can then be any element of $\{1,\dots,M\}$. If balls drawn are never returned (which requires $n\le M$), the scheme is called **sampling without replacement**.

**Definition 1.4.2 (Ordered and Unordered Sampling)** If two samples consisting of the same elements are regarded as different whenever the elements appear in a different order, the scheme is called **ordered sampling**, and a sample is written $(a_1,\dots,a_n)$. If order is disregarded, so that all samples consisting of the same elements are regarded as the same sample, the scheme is called **unordered sampling**, and a sample is written $[a_1,\dots,a_n]$.

For example, $(4,1,2,1)$ and $(1,4,2,1)$ are different elementary events in ordered sampling but the same elementary event $[1,1,2,4]$ in unordered sampling. For $M=3$ and $n=2$, the sample spaces of the four schemes are:

| Replacement | Order | Elementary events | Number |
|---|---|---|---|
| With | Ordered | $(i,j)$, $i,j=1,2,3$ | 9 |
| With | Unordered | $[1,1],[2,2],[3,3],[1,2],[1,3],[2,3]$ | 6 |
| Without | Ordered | $(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)$ | 6 |
| Without | Unordered | $[1,2],[1,3],[2,3]$ | 3 |

In general, the four sample spaces and their sizes are as follows:

| Scheme | Sample space $\Omega$ | $\#\Omega$ |
|---|---|---|
| With replacement, ordered | $\{(a_1,\dots,a_n)\colon a_i\in\{1,\dots,M\}\}$ | $M^n$ |
| With replacement, unordered | $\{[a_1,\dots,a_n]\colon a_i\in\{1,\dots,M\}\}$ | $\dbinom{M+n-1}n$ |
| Without replacement, ordered | $\{(a_1,\dots,a_n)\colon a_k\ne a_l\ (k\ne l),\ a_i\in\{1,\dots,M\}\}$ | $P_M^n$ |
| Without replacement, unordered | $\{[a_1,\dots,a_n]\colon a_k\ne a_l\ (k\ne l),\ a_i\in\{1,\dots,M\}\}$ | $\dbinom Mn$ |

The count for unordered sampling with replacement is derived in Section 1.5.2. Note that the elementary events in the sample space of unordered sampling with replacement are in general not equally likely. For instance, with $M=3$, $n=2$ and successive independent, equally likely draws, $[1,1]$ corresponds only to the ordered outcome $(1,1)$ and has probability $1/9$, whereas $[1,2]$ corresponds to $(1,2)$ and $(2,1)$ and has probability $2/9$. When using the classical model, one should choose a sample space whose outcomes really are equally likely, usually the ordered one.

**Example 1.4.1 (The Birthday Problem)** What is the probability that among $n$ people ($n\le365$) at least two share a birthday? Assume that each person's birthday is independently and equally likely to be any of the 365 days of the year (ignoring leap years). This is ordered sampling with replacement of $n$ days from $N=365$, so $\#\Omega=N^n$; all birthdays being distinct corresponds to ordered sampling without replacement, with $P_N^n$ outcomes. Hence

$$
\mathbb{P}(\text{at least two share a birthday})=1-\frac{P_N^n}{N^n}=1-\prod_{k=1}^{n-1}\Big(1-\frac kN\Big)\approx1-\exp\Big\{-\frac{n(n-1)}{2N}\Big\},
$$
where the approximation uses $1-x\approx\mathrm{e}^{-x}$ (the first two terms of the Taylor expansion of $\mathrm{e}^x$). Already for $n=23$ this probability exceeds $1/2$, a far smaller number of people than intuition suggests.

![The birthday problem: the probability that at least two people share a birthday as a function of the number of people n; the dashed curve is the exponential approximation; the probability first exceeds 1/2 at n = 23](./plots/birthday-problem.py)

### 1.4.3. Random Allocation

Allocating $n$ particles (balls) to $M$ boxes numbered $1,\dots,M$ is another common prototype, which comes from the distribution of $n$ particles over $M$ states in statistical physics. If the particles are distinguishable (numbered $1,\dots,n$), an allocation can be described by an array $(a_1,\dots,a_n)$, where $a_i$ is the number of the box containing particle $i$; if the particles are indistinguishable, an allocation can only be described by $[a_1,\dots,a_n]$. This gives the correspondence:

| Random sampling | Random allocation |
|---|---|
| Ordered sampling | Distinguishable particles |
| Unordered sampling | Indistinguishable particles |
| Sampling with replacement | Each box can hold any number of particles (no exclusion) |
| Sampling without replacement | Each box holds at most one particle (exclusion) |

For example, allocating 2 balls to 3 boxes: with distinguishable balls and no exclusion there are $3^2=9$ allocations; with indistinguishable balls and no exclusion, $\binom{4}{2}=6$; with distinguishable balls and exclusion, $P_3^2=6$; with indistinguishable balls and exclusion, $\binom32=3$.

**Remark 1.4.1** The three statistics of statistical physics correspond exactly to three assumptions of equal likelihood. Taking the $M^n$ allocations of distinguishable particles without exclusion as equally likely gives Maxwell–Boltzmann statistics (classical particles); taking the $\binom{M+n-1}n$ allocations of indistinguishable particles without exclusion as equally likely gives Bose–Einstein statistics (bosons such as photons); taking the $\binom Mn$ allocations of indistinguishable particles with exclusion as equally likely gives Fermi–Dirac statistics (fermions such as electrons, which obey the Pauli exclusion principle). Which model is correct cannot be decided by mathematics, only by experiment, the same lesson as the Bertrand paradox.

## 1.5. Further Remarks on the Classical Model

### 1.5.1. Problem-Solving Techniques

- Do not lose common sense, but do not rely on it too much either: intuition is often wrong (as in the birthday problem), but a result that clearly contradicts common sense should be checked.
- Check with the simplest cases: for example, set $n=1,2$ or $M=2$ and see whether the formula gives the right answer.
- Label the objects: even when the objects in a problem are "identical" (balls of the same color), the outcomes often become equally likely only after labeling.
- Story proofs: find a counting interpretation for each side of an identity and show that both count the same set.

### 1.5.2. Story Proofs

**Example 1.5.1** $\dbinom mn=\dbinom{m-1}{n-1}+\dbinom{m-1}n$. Choose a committee of $n$ people from $m$. Fix one person, A: there are $\binom{m-1}{n-1}$ committees containing A and $\binom{m-1}n$ committees not containing A.

**Example 1.5.2** $\dbinom mn=\sum_{k=n-1}^{m-1}\dbinom k{n-1}$. Choose $n$ numbers from $\{1,\dots,m\}$ and classify the choices by the largest number chosen: the choices whose largest number is $k+1$ ($k=n-1,\dots,m-1$) amount to choosing $n-1$ further numbers from $\{1,\dots,k\}$, in $\binom k{n-1}$ ways.

**Example 1.5.3 (Counting Unordered Samples with Replacement)** In unordered sampling with replacement of $n$ draws from $M$ balls, a sample $[a_1,\dots,a_n]$ is determined by the numbers of times $(k_1,\dots,k_M)$ each ball is drawn, with $k_j\ge0$ and $k_1+\cdots+k_M=n$. Arrange $n$ stars "$\ast$" in a row and divide them into $M$ segments with $M-1$ bars; the number of stars in segment $j$ is $k_j$. Such an arrangement is determined by which $n$ of the $n+M-1$ positions hold stars, so there are $\binom{M+n-1}n$ of them.

**Example 1.5.4 (Multinomial Coefficients)** There are $m$ balls of $r$ colors, $m_j$ of color $j$ ($m_1+\cdots+m_r=m$), and balls of the same color are indistinguishable. The number of distinct arrangements of these $m$ balls is

$$
\binom m{m_1,\dots,m_r}=\frac{m!}{m_1!\,m_2!\cdots m_r!}:
$$
after labeling the balls of each color there are $m!$ arrangements, and each arrangement without labels corresponds to $m_1!\cdots m_r!$ labeled ones. Equivalently, this is the number of ways to put $m$ distinguishable balls into $r$ boxes so that box $j$ receives exactly $m_j$ balls. This number is called a *multinomial coefficient*, because it is the coefficient of $x_1^{m_1}\cdots x_r^{m_r}$ in the expansion of $(x_1+\cdots+x_r)^m$.

## Summary

| Topic | Key points |
|---|---|
| Probability model | Sample space $\Omega$ (mutually exclusive, exhaustive outcomes), events (subsets of $\Omega$), and a probability $\mathbb{P}$ satisfying nonnegativity, normalization and countable additivity |
| Two basic models | Classical model $\mathbb{P}(A)=\#A/\#\Omega$; geometric probability $\mathbb{P}(A)=m(A)/m(\Omega)$; "equally likely" must be specified first (Bertrand paradox) |
| Properties of probability | $\mathbb{P}(\varnothing)=0$, finite additivity, $\mathbb{P}(A^{\mathsf c})=1-\mathbb{P}(A)$, monotonicity, addition rule, inclusion–exclusion identity, Boole / Bonferroni / Kounias inequalities, countable subadditivity |
| Counting | Ordered with replacement $M^n$, unordered with replacement $\binom{M+n-1}n$, ordered without replacement $P_M^n$, unordered without replacement $\binom Mn$; correspondence with random allocation |

The main tools for proving properties of probability are decomposing events into disjoint pieces as countable additivity requires, induction on the number of events, and passing to complements. In computations, make the definitions precise (what the sample space is, what is equally likely), and make good use of techniques for visualizing and simplifying the problem (story proofs, approximations by the Taylor expansion of $\mathrm{e}^x$).
