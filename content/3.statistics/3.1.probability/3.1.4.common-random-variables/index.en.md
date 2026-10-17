---
title: Common Random Variables
description: Discrete random variables and probability mass functions; the Bernoulli, binomial, geometric, Pascal, negative binomial, hypergeometric, negative hypergeometric and Poisson distributions; continuous random variables and probability densities; the uniform, exponential and normal distributions; the beta, gamma, Weibull, chi-squared, t, Cauchy and F distributions; relations between distributions.
source_hash: 546d92cb2079
---

The previous chapter, [3.1.3](/3.1.3), introduced random variables. This chapter presents the two most important classes of them: discrete random variables, which take finitely or countably many values and are described by probability mass functions, and continuous random variables, which have a probability density whose integrals give probabilities. Each common distribution comes from a typical random experiment: the number of successes in independent repeated trials (binomial distribution), the number of trials needed for the first success (geometric distribution), the number of defectives in sampling without replacement (hypergeometric distribution), the number of occurrences of a rare event (Poisson distribution), the lifetime of a component that does not age (exponential distribution), and the accumulation of many small errors (normal distribution). Understanding these experiments explains the relations between the distributions: the binomial distribution can be approximated by the Poisson distribution, the hypergeometric distribution by the binomial distribution, and both the geometric and the exponential distributions are memoryless. The next chapter, [3.1.5](/3.1.5), treats both classes uniformly through distribution functions and discusses distributions of functions of random variables; their expectations and variances are given in [3.1.8](/3.1.8).

## 4.1. Discrete Random Variables

### 4.1.1. Probability Mass Functions

**Definition 4.1.1 (Discrete Random Variable)** If a random variable $X$ takes only finitely many values $x_1,\dots,x_m$ or countably many values $x_1,x_2,\dots$, then $X$ is called a **discrete random variable**.

For example, roll a four-sided die twice and let $X$ be the larger of the two results; then $X$ maps the 16 sample points onto $\{1,2,3,4\}$ and is a discrete random variable.

**Definition 4.1.2 (Probability Mass Function)** Let $X$ be a discrete random variable. The probabilities

$$
\mathbb{P}(X=x_k)=p_k,\qquad k\ge1
$$
are called the probability distribution of $X$, and $\{p_k\}$ is called the **probability mass function** (PMF) of $X$.

When the probability mass function $\{p_k\}$ has no evident pattern, the distribution is often written as a table

$$
\begin{array}{c|cccc}
X & x_1 & x_2 & x_3 & \cdots\\
\hline
\mathbb{P} & p_1 & p_2 & p_3 & \cdots
\end{array}
$$

A probability mass function satisfies $p_k\ge0$ and $\sum_kp_k=1$ (by countable additivity, since $\bigcup_k\{X=x_k\}=\Omega$); conversely, every sequence satisfying these two conditions is the probability mass function of some discrete random variable. For every Borel set $A$, $\mathbb{P}(X\in A)=\sum_{k\colon x_k\in A}p_k$.

### 4.1.2. The Bernoulli Distribution

Any experiment in which we only record success or failure (whether a product is acceptable, whether a person is healthy, whether a telephone is on standby) can be described by a random variable with $X=1$ (success) and $X=0$ (failure).

**Definition 4.1.3 (Bernoulli Distribution)** If $X$ takes only the values 0 and 1 with $\mathbb{P}(X=1)=p=1-\mathbb{P}(X=0)$, then $X$ is said to have the **Bernoulli distribution** (two-point distribution), written $X\sim\mathrm{Ber}(p)$ (also $\mathrm{Bin}(1,p)$). Its probability mass function is

$$
\begin{array}{c|cc}
X & 0 & 1\\
\hline
\mathbb{P} & 1-p & p
\end{array}
$$

The indicator $\boldsymbol{1}_A$ of an event $A$ has the distribution $\mathrm{Ber}(\mathbb{P}(A))$. Independent repeated trials with only two outcomes and the same success probability $p$ in each trial are called Bernoulli trials.

### 4.1.3. The Binomial Distribution

**Example 4.1.1** Suppose an experiment $S$ succeeds with probability $p$ and is repeated independently $n$ times. Let $X$ be the number of successes; find $\mathbb{P}(X=k)$. Let $A_j$ be the event that trial $j$ succeeds; then $A_1,\dots,A_n$ are mutually independent and $\mathbb{P}(A_j)=p$. There are $\binom nk$ ways to select $k$ of the $n$ trials; for the $i$-th selection, say trials $j_1,\dots,j_k$, let

$$
B_i=A_{j_1}\cap\cdots\cap A_{j_k}\cap A_{j_{k+1}}^{\mathsf c}\cap\cdots\cap A_{j_n}^{\mathsf c}
$$
be the event that trials $j_1,\dots,j_k$ succeed and the others fail. The $B_i$ are mutually exclusive, $\{X=k\}=\bigcup_{i=1}^{\binom nk}B_i$, and by independence $\mathbb{P}(B_i)=p^k(1-p)^{n-k}$. By finite additivity,

$$
\mathbb{P}(X=k)=\sum_{i=1}^{\binom nk}\mathbb{P}(B_i)=\binom nkp^k(1-p)^{n-k}.
$$
This is precisely the $(k+1)$-st term of the binomial expansion $1=\{p+(1-p)\}^n=\sum_{k=0}^n\binom nkp^k(1-p)^{n-k}$, hence the name "binomial distribution".

**Definition 4.1.4 (Binomial Distribution)** If a random variable $X$ has the distribution

$$
\mathbb{P}(X=k)=\binom nkp^k(1-p)^{n-k},\qquad k=0,1,\dots,n,
$$
where $p\in(0,1)$, then $X$ is said to have the **binomial distribution**, written $X\sim\mathrm{Bin}(n,p)$.

By Example 4.1.1, if the random variables $X_1,\dots,X_n$ are mutually independent and each has the distribution $\mathrm{Ber}(p)$, then $S=X_1+\cdots+X_n\sim\mathrm{Bin}(n,p)$. Consequently, if $X\sim\mathrm{Bin}(n,p)$ and $Y\sim\mathrm{Bin}(m,p)$ are independent, then $X+Y\sim\mathrm{Bin}(m+n,p)$: $X+Y$ can be viewed as the number of successes in $m+n$ independent repeated trials.

![Probability mass functions (line plots) of the binomial distribution Bin(n, p) for p = 0.2, 0.5, 0.8 and n from 3 to 30](./plots/binomial-pmf.py)

The figure shows that the probability mass function first increases and then decreases, with its peak near $np$. Write $b(k;n,p)=\mathbb{P}(X=k)$. Then

$$
\frac{b(k;n,p)}{b(k-1;n,p)}=\frac{(n-k+1)p}{k(1-p)}=1+\frac{(n+1)p-k}{k(1-p)}.
$$
Hence for $k<(n+1)p$ we have $b(k;n,p)>b(k-1;n,p)$, so $b(k;n,p)$ increases with $k$; for $k>(n+1)p$, $b(k;n,p)$ decreases with $k$; and for $k=(n+1)p$ the two terms are equal. This proves:

**Theorem 4.1.1 (Most Probable Value of the Binomial Distribution)** The most probable value $k_0$ of the binomial distribution, that is, an integer with $b(k_0;n,p)=\max_{0\le k\le n}b(k;n,p)$, exists, and

$$
k_0=\begin{cases}(n+1)p\ \text{and}\ (n+1)p-1, & (n+1)p\ \text{an integer},\\ \lfloor(n+1)p\rfloor, & (n+1)p\ \text{not an integer}.\end{cases}
$$
That is, if $(n+1)p$ is an integer, $b((n+1)p;n,p)$ and $b((n+1)p-1;n,p)$ are both maximal terms; otherwise $b(\lfloor(n+1)p\rfloor;n,p)$ is the unique maximal term. $b(k_0;n,p)$ is called the central term of the binomial distribution.

**Example 4.1.2** A shooter fires 9 shots at the same target; the shots are independent, each hitting with probability $0.3$. Find the probability of more than two hits and the most probable number of hits. Let $X$ be the number of hits; then $X\sim\mathrm{Bin}(9,0.3)$ and

$$
\mathbb{P}(X>2)=1-\sum_{k=0}^2\binom9k(0.3)^k(0.7)^{9-k}=1-0.4628=0.5372.
$$
Moreover $(n+1)p=10\times0.3=3$ is an integer, so the most probable number of hits is 3 or 2.

### 4.1.4. The Geometric Distribution

**Example 4.1.3** A shooter fires at a target until it is hit; each shot hits with probability $p>0$, and the shots are independent. Let $X$ be the number of shots up to and including the first hit; find $\mathbb{P}(X=k)$. Let $A_j$ be the event that shot $j$ misses. By independence,

$$
\mathbb{P}(X=k)=\mathbb{P}(A_1\cap\cdots\cap A_{k-1}\cap A_k^{\mathsf c})=(1-p)^{k-1}p,\qquad k=1,2,\dots
$$
Note that $\mathbb{P}(X<\infty)=\sum_{k=1}^\infty(1-p)^{k-1}p=1$: if one keeps shooting, the target is eventually hit; independent repeated trials, carried on indefinitely, eventually succeed.

**Definition 4.1.5 (Geometric Distribution)** If a random variable $X$ has the distribution

$$
\mathbb{P}(X=k)=(1-p)^{k-1}p,\qquad k=1,2,\dots,
$$
where $0<p\le1$, then $X$ is said to have the **geometric distribution** with parameter $p$, written $X\sim\mathrm{Geo}(p)$.

The name comes from the **geometric series**: the probability mass function is a geometric progression with ratio $1-p$. A characteristic feature of the geometric distribution is that, given failures in the first $k$ trials, the number $X-k$ of further trials needed has the same distribution as $X$, as if the past failures had been "forgotten".

**Theorem 4.1.2 (Memorylessness of the Geometric Distribution)** A random variable $X$ with positive integer values has the geometric distribution $\mathrm{Geo}(p)$ if and only if, for every $k\ge1$ (with $\mathbb{P}(X>k)>0$),

$$
\mathbb{P}(X=k+1\mid X>k)=\mathbb{P}(X=1).
$$
This property is called *memorylessness*.

**Proof** Necessity. By the definition of conditional probability,

$$
\mathbb{P}(X=k+1\mid X>k)=\frac{\mathbb{P}(X=k+1)}{\mathbb{P}(X>k)}=\frac{(1-p)^kp}{\sum_{j=k+1}^\infty(1-p)^{j-1}p}=\frac{(1-p)^kp}{(1-p)^k}=p=\mathbb{P}(X=1).
$$
Sufficiency. Let $p=\mathbb{P}(X=1)$ and $r_k=\mathbb{P}(X>k)$, so that $r_0=1$. Since $\{X=k+1\}=\{X>k\}\setminus\{X>k+1\}$,

$$
p=\mathbb{P}(X=k+1\mid X>k)=\frac{r_k-r_{k+1}}{r_k}=1-\frac{r_{k+1}}{r_k},
$$
so $r_{k+1}=(1-p)r_k=\cdots=(1-p)^{k+1}r_0=(1-p)^{k+1}$. Therefore $\mathbb{P}(X=k)=r_{k-1}-r_k=(1-p)^{k-1}p$. $\square$

Equivalently, $\mathbb{P}(X>m+k\mid X>m)=\mathbb{P}(X>k)$ for all positive integers $m,k$.

### 4.1.5. The Pascal and Negative Binomial Distributions

**Example 4.1.4** A shooter fires at a target until it has been hit $r$ times; each shot hits with probability $p\in(0,1)$, independently. Let $X$ be the number of shots fired when shooting stops. $X=k$ if and only if shot $k$ hits and exactly $r-1$ of the first $k-1$ shots hit, so $\mathbb{P}(X=k)=\binom{k-1}{r-1}(1-p)^{k-r}p^r$, $k=r,r+1,\dots$.

**Definition 4.1.6 (Pascal Distribution)** If a random variable $X$ has the distribution

$$
\mathbb{P}(X=k)=\binom{k-1}{r-1}(1-p)^{k-r}p^r,\qquad k=r,r+1,\dots,
$$
then $X$ is said to have the **Pascal distribution**, written $X\sim\mathrm{Pascal}(r,p)$. For $r=1$ the Pascal distribution is the geometric distribution.

In Example 4.1.4, let $Y=X-r$; then $Y$ is the number of failures (misses) when shooting stops.

**Definition 4.1.7 (Negative Binomial Distribution)** If a random variable $Y$ has the distribution

$$
\mathbb{P}(Y=k)=\binom{k+r-1}{r-1}(1-p)^kp^r,\qquad k=0,1,\dots,\tag{4.1}
$$
then $Y$ is said to have the **negative binomial distribution**, written $Y\sim\mathrm{NB}(r,p)$.

The name has two sources. The first is the binomial expansion with a negative exponent: for $\lvert x\rvert<1$,

$$
(1-x)^{-r}=\sum_{k=0}^\infty\frac{(-r)(-r-1)\cdots(-r-k+1)}{k!}(-x)^k=\sum_{k=0}^\infty\binom{k+r-1}{r-1}x^k;
$$
setting $x=1-p$ and multiplying by $p^r$ gives $1=\sum_{k=0}^\infty\binom{k+r-1}{r-1}(1-p)^kp^r$, which also verifies that Eq. (4.1) is indeed a probability mass function. The second is that the experiment runs "the other way round" from the binomial one: the binomial distribution fixes the number of trials $n$ and takes the number of successes as the random variable, while the negative binomial distribution fixes the number of successes $r$ and takes the number of trials needed (minus $r$) as the random variable.

**Example 4.1.5** To examine the scrap rate $p$ of a factory's products, there are two schemes. One is to draw $n$ products with replacement and count the scrap among them, which leads to the binomial distribution. The other is to fix a natural number $r$ in advance and sample products one by one with replacement until the $r$-th scrap item is found, recording the number $X\sim\mathrm{NB}(r,p)$ of acceptable products examined. When $p$ is small, $X$ tends to take large values, and vice versa, so $X$ can also be used to study $p$.

### 4.1.6. The Hypergeometric and Negative Hypergeometric Distributions

**Definition 4.1.8 (Hypergeometric Distribution)** In a population of $N$ elements, $M$ are red and $N-M$ are black. Draw $n$ elements at random (without replacement). The number $X$ of red elements drawn has the distribution

$$
\mathbb{P}(X=k)=\frac{\binom Mk\binom{N-M}{n-k}}{\binom Nn},\qquad k=0,1,\dots,\min\{n,M\},
$$
and $X$ is said to have the **hypergeometric distribution**, written $X\sim\mathrm{H}(n,M,N)$. Here we use the convention $\binom lm=0$ for $m>l$, so the probability is zero for $k<n-(N-M)$.

The hypergeometric distribution is used in quality inspection (if exactly $M$ of $N$ products are defective and $n$ are drawn at random, the number of defectives drawn has the distribution $\mathrm{H}(n,M,N)$) and in capture–recapture models (estimating the number of fish in a lake). If there are very many products, drawing without replacement should make little difference compared with drawing with replacement; with replacement, the number of defectives is $\tilde X\sim\mathrm{Bin}(n,p_N)$, where $p_N=M/N$ is the defective rate.

**Theorem 4.1.3 (Binomial Approximation to the Hypergeometric Distribution)** Let $X_N\sim\mathrm{H}(n,M,N)$ with $n$ fixed and $M/N\to p$ as $N\to\infty$. Then for each $m=0,1,\dots,n$,

$$
\lim_{N\to\infty}\mathbb{P}(X_N=m)=\binom nmp^m(1-p)^{n-m}.
$$

**Proof** Expanding the binomial coefficients,

$$
\mathbb{P}(X_N=m)=\binom nm\cdot\frac{M(M-1)\cdots(M-m+1)}{N^m}\cdot\frac{(N-M)\cdots(N-M-n+m+1)}{N^{n-m}}\cdot\frac{N^n}{N(N-1)\cdots(N-n+1)}.
$$
As $N\to\infty$, each of the $m$ fractions in the second factor tends to $p$, each of the $n-m$ fractions in the third factor tends to $1-p$, and the last factor tends to 1. $\square$

In practice, for large $N$, computing $\binom Nn$, $\binom Mm$ and $\binom{N-M}{n-m}$ takes far more effort than computing $\binom nm$, while the sample size $n$ is usually not large; so for large $N$ and $M$ the approximation $\mathrm{H}(n,M,N)\approx\mathrm{Bin}(n,M/N)$ is often more convenient.

**Definition 4.1.9 (Negative Hypergeometric Distribution)** From the population above, draw elements one at a time without replacement until $r$ red elements have been drawn ($1\le r\le M$). The number $X$ of black elements drawn by then has the distribution

$$
\mathbb{P}(X=k)=\frac{\binom{k+r-1}k\binom{N-k-r}{M-r}}{\binom NM},\qquad k=0,1,\dots,N-M,
$$
and $X$ is said to have the **negative hypergeometric distribution**, written $X\sim\mathrm{NH}(r,M,N)$.

Derivation: line up all $N$ elements in order; the $\binom NM$ possible sets of positions of the red elements are equally likely. $X=k$ if and only if the $r$-th red element is in position $k+r$, that is, exactly $r-1$ red elements lie among the first $k+r-1$ positions ($\binom{k+r-1}{r-1}=\binom{k+r-1}k$ ways) and exactly $M-r$ red elements lie among the last $N-k-r$ positions ($\binom{N-k-r}{M-r}$ ways). As in Theorem 4.1.3, $\mathrm{NH}(r,M,N)$ tends to $\mathrm{NB}(r,p)$ as $N\to\infty$ and $M/N\to p$.

### 4.1.7. The Poisson Distribution

**Definition 4.1.10 (Poisson Distribution)** If a random variable $X$ has the distribution

$$
\mathbb{P}(X=k)=\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda},\qquad k=0,1,2,\dots,
$$
where $\lambda$ is a positive constant, then $X$ is said to have the **Poisson distribution** with parameter $\lambda$, written $X\sim\mathrm{Poi}(\lambda)$.

By the **Taylor series** of $\mathrm{e}^\lambda$, $\sum_k\lambda^k\mathrm{e}^{-\lambda}/k!=1$. The Poisson distribution describes the number of occurrences of a rare event per unit time (or per unit area or volume): the number of traffic accidents on a stretch of highway in a year, the number of customers arriving at a market in a day, the number of telephone calls received by an office in a day, the total number of students arriving late for class at a university in a day, the number of raindrops on a sheet of paper, and so on. The parameter $\lambda$ is the average number of occurrences (see [3.1.8](/3.1.8)).

**Example 4.1.6 (Radioactive Decay)** In 1910 Rutherford and Geiger observed the emission of $\alpha$ particles by the radioactive element polonium: they made $N=2608$ observations of 7.5 seconds each and counted 10094 $\alpha$ particles in total. Let $X$ be the number of $\alpha$ particles emitted in 7.5 seconds and $m_k$ the number of observations in which $k$ particles were counted. Take $\lambda=10094/2608\approx3.87$ (the average number of $\alpha$ particles emitted in 7.5 seconds) and $Y\sim\mathrm{Poi}(3.87)$:

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | $\ge10$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $m_k$ | 57 | 203 | 383 | 525 | 532 | 408 | 273 | 139 | 45 | 27 | 16 |
| $m_k/N$ | 0.022 | 0.078 | 0.147 | 0.201 | 0.204 | 0.156 | 0.105 | 0.053 | 0.017 | 0.010 | 0.006 |
| $\mathbb{P}(Y=k)$ | 0.021 | 0.081 | 0.156 | 0.201 | 0.195 | 0.151 | 0.097 | 0.054 | 0.026 | 0.011 | 0.007 |

The frequency of the event $\{X=k\}$ in the 2608 repeated observations is essentially $\mathbb{P}(Y=k)$. Why does this regularity hold? Divide $t=7.5$ seconds into $n$ equal pieces of $\delta_n=t/n$ seconds each, and for sufficiently large $n$ assume:

1. at most one $\alpha$ particle is emitted in each interval $\delta_n$, and one is emitted with probability $p_n=\mu\delta_n=\mu t/n$, where $\mu$ is a positive constant;
2. emissions in different small intervals are independent.

Under these assumptions the number of particles emitted is $X\sim\mathrm{Bin}(n,p_n)$. Letting $n\to\infty$, Theorem 4.1.4 below (with $\lambda=\mu t$) gives $X\sim\mathrm{Poi}(\lambda)$.

**Theorem 4.1.4 (Poisson Limit Theorem)** If $np_n\to\lambda>0$ as $n\to\infty$, then for each $k=0,1,2,\dots$,

$$
\lim_{n\to\infty}\binom nkp_n^k(1-p_n)^{n-k}=\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda}.
$$

**Proof** Let $\lambda_n=np_n$. Then

$$
\binom nkp_n^k(1-p_n)^{n-k}=\frac{\lambda_n^k}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\Big(1-\frac{\lambda_n}n\Big)^{n}\cdot\Big(1-\frac{\lambda_n}n\Big)^{-k}.
$$
As $n\to\infty$, the second and the last factors tend to 1, and by $\lim_{x\to0}(1+x)^{1/x}=\mathrm{e}$ the third factor tends to $\mathrm{e}^{-\lambda}$. $\square$

So if $n$ is large, $p$ is small and $np\approx\lambda$ is a moderate constant, $\mathrm{Bin}(n,p)$ can be approximated by $\mathrm{Poi}(\lambda)$; when $n$ cannot be determined (for example, the number of vehicles on a road) and only the average number of occurrences is known, the Poisson distribution is the one to use.

![Left: probability mass functions of the Poisson distribution Poi(λ) for λ = 1, …, 6; middle: Bin(n, 3/n) approaches Poi(3) as n increases; right: frequencies of α-particle counts in the Rutherford–Geiger experiment compared with Poi(3.87)](./plots/poisson-approximation.py)

## 4.2. Continuous Random Variables

### 4.2.1. Probability Densities

Random variables such as measurement errors, component lifetimes and heights can take any value in an interval, and every single point has probability zero; they must be described by "the density of probability along the real line".

**Definition 4.2.1 (Continuous Random Variable)** Let $X$ be a random variable. If there is a nonnegative function $f(x)$ such that for all $a<b$

$$
\mathbb{P}(a<X\le b)=\int_a^bf(x)\,\mathrm{d}x,
$$
then $X$ is called a **continuous random variable**, and $f(x)$ is called the **probability density function** (PDF), or simply the density, of $X$.

**Property 4.2.1** Let $f(x)$ be the probability density of $X$. Then

1. $\int_{-\infty}^\infty f(x)\,\mathrm{d}x=1$;
2. for every Borel set $A$, $\mathbb{P}(X\in A)=\int_Af(x)\,\mathrm{d}x$;
3. for every $a\in\mathbb{R}$, $\mathbb{P}(X=a)=0$, and hence $\mathbb{P}(a<X\le b)=\mathbb{P}(a\le X\le b)=\mathbb{P}(a<X<b)$.

**Proof** (1) The events $A_n=\{X\in(-n,n]\}$ increase and $\bigcup_nA_n=\Omega$. By the continuity of probability (Theorem 2.2.1 in [3.1.2](/3.1.2)),

$$
\int_{-\infty}^\infty f(x)\,\mathrm{d}x=\lim_{n\to\infty}\int_{-n}^nf(x)\,\mathrm{d}x=\lim_{n\to\infty}\mathbb{P}(A_n)=\mathbb{P}\Big(\bigcup_{n=1}^\infty A_n\Big)=1.
$$
(2) requires measure theory (two probability measures that agree on all intervals agree on all Borel sets) and is omitted here. (3) For every $\varepsilon>0$, $\mathbb{P}(X=a)\le\mathbb{P}(a-\varepsilon<X\le a)=\int_{a-\varepsilon}^af(x)\,\mathrm{d}x\to0$ as $\varepsilon\downarrow0$. $\square$

Conversely, every function with $f\ge0$ and $\int_{-\infty}^\infty f(x)\,\mathrm{d}x=1$ is the density of some continuous random variable. Several points deserve attention:

- A density is not a probability, and $f(x)$ may exceed 1; $f(x)\,\delta$ is approximately the probability that $X$ falls in $(x,x+\delta]$.
- A density need not be bounded. For example, $f(x)=\dfrac1{2\sqrt x}$ for $x\in(0,1]$ (and 0 elsewhere) is a density, yet $\lim_{x\downarrow0}f(x)=+\infty$.
- A density is not unique: changing $f$ at finitely many (or even countably many) points does not affect the integrals.
- "Continuous random variable" does not mean that $X(\omega)$ is a continuous function of $\omega$: the sample space $\Omega$ carries no topology, so continuity makes no sense there. It means that the distribution function of $X$ is absolutely continuous (see [3.1.5](/3.1.5)).

### 4.2.2. The Uniform Distribution

**Definition 4.2.2 (Uniform Distribution)** For $a<b$, if the probability density of $X$ is

$$
f(x)=\begin{cases}\dfrac1{b-a}, & x\in(a,b),\\ 0, & x\notin(a,b),\end{cases}
$$
then $X$ is said to have the **uniform distribution** on the interval $(a,b)$, written $X\sim\mathrm{U}(a,b)$.

By Property 4.2.1 (3), writing the interval $(a,b)$ as $(a,b]$, $[a,b)$ or $[a,b]$ does not change the distribution. The density can also be written with an indicator function as $f(x)=\frac1{b-a}\boldsymbol{1}_{(a,b)}(x)$. For a subinterval $(c,d)$ of $(a,b)$, $\mathbb{P}(c<X<d)=\frac{d-c}{b-a}$ depends only on the length of the subinterval; this is exactly the geometric probability of [3.1.1](/3.1.1).

More generally, for a Borel set $A$ in $\mathbb{R}^r$ with volume $0<m(A)=\int_A1\,\mathrm{d}x<\infty$, if $X$ has the density $f(x)=\frac1{m(A)}\boldsymbol{1}_A(x)$, then $X$ is said to have the uniform distribution on $A$, written $X\sim\mathrm{U}(A)$. In this case $\mathbb{P}(X\in B)=m(A\cap B)/m(A)$ for every Borel set $B$.

### 4.2.3. The Exponential Distribution

**Definition 4.2.3 (Exponential Distribution)** For a positive constant $\lambda$, if the probability density of $X$ is

$$
f(x)=\begin{cases}\lambda\mathrm{e}^{-\lambda x}, & x\ge0,\\ 0, & x<0,\end{cases}
$$
then $X$ is said to have the **exponential distribution** with parameter $\lambda$, written $X\sim\mathrm{Exp}(\lambda)$.

The exponential distribution describes the waiting time until some event occurs, the service life of an instrument, and the like. The probability that $X$ exceeds a value decreases exponentially as the value grows: for $a\ge0$, $\mathbb{P}(X>a)=\int_a^\infty\lambda\mathrm{e}^{-\lambda y}\,\mathrm{d}y=\mathrm{e}^{-\lambda a}$. $\lambda$ is called the rate parameter and $1/\lambda$ is the mean lifetime; another common parametrization is $f(x)=\frac1\theta\mathrm{e}^{-x/\theta}\boldsymbol{1}_{(0,\infty)}(x)$, where $\theta=1/\lambda$ is the scale parameter. If $X\sim\mathrm{Exp}(\lambda)$, then $\lambda X\sim\mathrm{Exp}(1)$ (see the linear transformations in [3.1.5](/3.1.5)). When $\mathbb{P}(X<0)=0$, $X$ is called a nonnegative random variable.

**Theorem 4.2.1 (Memorylessness of the Exponential Distribution)** Let $X$ be a continuous nonnegative random variable. Then $X$ has an exponential distribution if and only if $X$ is memoryless, that is, for all $s,t\ge0$,

$$
\mathbb{P}(X>s+t\mid X>s)=\mathbb{P}(X>t).\tag{4.2}
$$

**Proof** Necessity. If $X\sim\mathrm{Exp}(\lambda)$, then $\mathbb{P}(X>x)=\mathrm{e}^{-\lambda x}$ and

$$
\mathbb{P}(X>s+t\mid X>s)=\frac{\mathbb{P}(X>s+t,\,X>s)}{\mathbb{P}(X>s)}=\frac{\mathrm{e}^{-\lambda(s+t)}}{\mathrm{e}^{-\lambda s}}=\mathrm{e}^{-\lambda t}=\mathbb{P}(X>t).
$$
Sufficiency. Let $G(x)=\mathbb{P}(X>x)$. Then $G$ is nonincreasing and right-continuous, $G(0)=1$ (since $X$ is continuous and nonnegative, $\mathbb{P}(X=0)=0$), and $G(x)\to0$ as $x\to\infty$. By Eq. (4.2), $G(s+t)=G(s)G(t)$ for all $s,t\ge0$. Hence $G(1)=G(1/n)^n$ and $G(m/n)=G(1)^{m/n}$. Write $G(1)=\mathrm{e}^{-\lambda}$; since $G(x)\to0$, we have $G(1)<1$. If $G(1)=0$, then $G(1/n)=0$ for all $n$, and right-continuity gives $G(0)=0$, a contradiction. So $0<\lambda<\infty$, and $G(x)=\mathrm{e}^{-\lambda x}$ for all positive rational $x$, which extends to all $x\ge0$ by monotonicity. Finally, for $0\le a<b$,

$$
\mathbb{P}(a<X\le b)=G(a)-G(b)=\mathrm{e}^{-\lambda a}-\mathrm{e}^{-\lambda b}=\int_a^b\lambda\mathrm{e}^{-\lambda y}\,\mathrm{d}y,
$$
that is, $X\sim\mathrm{Exp}(\lambda)$. $\square$

From the point of view of reliability, the probability per unit time that a component fails, given that it is still working at time $t$ (the failure rate), is

$$
\lim_{\Delta t\to0}\frac{\mathbb{P}(t<X\le t+\Delta t\mid X>t)}{\Delta t}=\lim_{\Delta t\to0}\frac{1-\mathrm{e}^{-\lambda\Delta t}}{\Delta t}=\lambda,
$$
independent of $t$. Memorylessness thus says that the failure rate of the component is always the constant $\lambda$. The exponential distribution describes the lifetime of a component that does not age. Since "no aging" is impossible, this is only an approximation, but for some long-lived components aging is negligible in the early stage, and the exponential distribution describes the lifetime in that stage quite accurately. The relation between the geometric and exponential distributions is discussed in [3.1.5](/3.1.5).

### 4.2.4. The Normal Distribution

The normal distribution has three origins. First, de Moivre (1733) and Laplace (1812) discovered that if $X_n\sim\mathrm{Bin}(n,p)$, then

$$
\lim_{n\to\infty}\mathbb{P}\bigg(\frac{X_n-np}{\sqrt{np(1-p)}}\le x\bigg)=\int_{-\infty}^x\frac1{\sqrt{2\pi}}\mathrm{e}^{-t^2/2}\,\mathrm{d}t,
$$
which is the de Moivre–Laplace **central limit theorem** ([3.1.13](/3.1.13)). Second, measurement errors in astronomy: Simpson tried to describe errors by a triangular distribution and Laplace (1774) by the density $\frac\theta2\mathrm{e}^{-\theta\lvert x\rvert}$; Gauss (1809) assumed that an observation is $X=\theta+\varepsilon$ ($\theta$ the unknown true value, $\varepsilon$ a random error) and required the **maximum likelihood estimator** of $\theta$ to be exactly the average of the observations, which led him to the normal distribution. For this reason the normal distribution is also called the Gaussian distribution. Third, the normal distribution also arose in the study of Brownian motion; experience shows that many quality characteristics of products and many physiological measurements of organisms follow the normal distribution exactly or approximately, and the sum of a large number of i.i.d. random variables is also approximately normal.

**Definition 4.2.4 (Normal Distribution)** If the density of $X$ is

$$
f(x)=\frac1{\sigma\sqrt{2\pi}}\exp\Big\{-\frac{(x-\mu)^2}{2\sigma^2}\Big\},\qquad x\in\mathbb{R},\tag{4.3}
$$
where $\mu\in\mathbb{R}$ and $\sigma>0$, then $X$ is said to have the **normal distribution** (Gaussian distribution) with parameters $(\mu,\sigma^2)$, written $X\sim\mathcal{N}(\mu,\sigma^2)$. In particular, when $X\sim\mathcal{N}(0,1)$, $X$ is said to have the **standard normal distribution**, whose density is denoted

$$
\varphi(x)=\frac1{\sqrt{2\pi}}\exp\Big\{-\frac{x^2}2\Big\},\qquad x\in\mathbb{R}.
$$

$\varphi$ is indeed a density: in polar coordinates,

$$
\Big(\int_{-\infty}^\infty\varphi(x)\,\mathrm{d}x\Big)^2=\frac1{2\pi}\int_{-\infty}^\infty\int_{-\infty}^\infty\mathrm{e}^{-(x^2+y^2)/2}\,\mathrm{d}x\,\mathrm{d}y=\frac1{2\pi}\int_0^{2\pi}\mathrm{d}\theta\int_0^\infty r\mathrm{e}^{-r^2/2}\,\mathrm{d}r=1,
$$
which is the **Gaussian integral**. The substitution $y=(x-\mu)/\sigma$ shows that $f$ in Eq. (4.3) is also a density. The normal density is bell-shaped, which is why the normal distribution is also called the bell-shaped distribution, and it has the following properties:

1. $f(x)$ is symmetric about $x=\mu$;
2. $f(\mu)=(\sigma\sqrt{2\pi})^{-1}$ is the maximum; the smaller $\sigma$, the higher and narrower the peak;
3. $f(x)$ has inflection points at $x=\mu\pm\sigma$.

The normal distribution has many excellent theoretical properties (for instance, linear combinations of independent normal variables are normal, and among distributions with a given variance it has maximal entropy) and holds a special place in probability and statistics. The standard normal distribution function $\Phi$ and the "$3\sigma$ rule" are discussed in [3.1.5](/3.1.5), and the multivariate generalization in [3.1.15](/3.1.15).

![Densities of common continuous distributions: the exponential, normal, beta and gamma distributions (rate λ = 1)](./plots/continuous-densities.py)

## 4.3. Other Continuous Distributions

The distributions in this section will be used in later chapters (distributions of functions of random variables, order statistics, sampling distributions); they are collected here for reference.

### 4.3.1. The Beta and Gamma Distributions

**Definition 4.3.1 (Beta Distribution)** Let $\alpha,\beta$ be positive constants. If the density of $X$ is

$$
f(x)=\frac1{\mathrm{B}(\alpha,\beta)}x^{\alpha-1}(1-x)^{\beta-1},\qquad0<x<1,
$$
where $\mathrm{B}(\alpha,\beta)=\dfrac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ is the **beta function**, then $X$ is said to have the **beta distribution** with parameters $(\alpha,\beta)$, written $X\sim\mathrm{Beta}(\alpha,\beta)$.

For $\alpha=\beta=1$ it is the uniform distribution $\mathrm{U}(0,1)$; for $\alpha=2,\beta=1$ the density $2x$ is a straight line; for $\alpha=\beta=1/2$ the density is U-shaped (tending to infinity at both ends); for $\alpha=\beta=2$ the density $6x(1-x)$ is an inverted U. The beta distribution is the distribution of the order statistics of $\mathrm{U}(0,1)$ ([3.1.7](/3.1.7)), and in Bayesian statistics it is often used as the **prior distribution** of a proportion: if $X\mid p\sim\mathrm{Bin}(n,p)$ and $p$ has the prior $\mathrm{Beta}(\alpha,\beta)$, then after observing $X$ the **posterior distribution** of $p$ is $\mathrm{Beta}(\alpha+X,\beta+n-X)$ (see [3.2.7](/3.2.7)).

**Definition 4.3.2 (Gamma Distribution)** Let $\alpha,\lambda$ be positive constants. If the density of $X$ is

$$
f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-\lambda x},\qquad x>0,
$$
then $X$ is said to have the **gamma distribution** with parameters $(\alpha,\lambda)$, written $X\sim\Gamma(\alpha,\lambda)$. Here $\Gamma(\alpha)=\int_0^\infty x^{\alpha-1}\mathrm{e}^{-x}\,\mathrm{d}x$ is the **gamma function**, which satisfies $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$, $\Gamma(n)=(n-1)!$ and $\Gamma(1/2)=\sqrt\pi$.

$\alpha$ is called the shape parameter and $\lambda$ the rate parameter; $1/\lambda$ is the scale parameter. For $\alpha=1$ we obtain the exponential distribution $\mathrm{Exp}(\lambda)$; for positive integer $\alpha$ the distribution is called the *Erlang distribution* and is used in queueing theory (it is the distribution of the sum of $\alpha$ independent $\mathrm{Exp}(\lambda)$ variables, see [3.1.7](/3.1.7)). Studying random variables in physics, biology and economics, Karl Pearson found that many continuous random variables taking only nonnegative values are not normally distributed; the gamma distribution is one type in the Pearson family of distributions he studied. In meteorology, annual, seasonal or monthly precipitation in arid regions is considered to follow a gamma distribution.

### 4.3.2. The Weibull Distribution

**Definition 4.3.3 (Weibull Distribution)** Let $\alpha,\lambda>0$. If the density of $X$ is

$$
f(x)=\lambda\alpha x^{\alpha-1}\exp\{-\lambda x^\alpha\},\qquad x\ge0,
$$
then $X$ is said to have the **Weibull distribution** with parameters $(\alpha,\lambda)$.

We have $\mathbb{P}(X>x)=\exp\{-\lambda x^\alpha\}$. For $\alpha=1$ it is the exponential distribution; for $\alpha=2$ and $\lambda=1/(2\sigma^2)$ it is the *Rayleigh distribution*, with density $f(x;\sigma)=\frac x{\sigma^2}\exp\{-\frac{x^2}{2\sigma^2}\}$, $x\ge0$. The failure rate $\lambda\alpha x^{\alpha-1}$ of the Weibull distribution increases with time for $\alpha>1$ (aging) and decreases for $\alpha<1$, so together with the exponential distribution it plays an important role in reliability analysis.

### 4.3.3. The Chi-Squared, t, Cauchy and F Distributions

These four distributions are the most important sampling distributions in statistical inference; their relations to the normal distribution are proved in [3.1.7](/3.1.7) and [3.2.2](/3.2.2).

**Definition 4.3.4 (Chi-Squared Distribution)** Let $\nu>0$. If the density of $X$ is

$$
f(x)=\frac1{2^{\nu/2}\Gamma(\nu/2)}x^{\nu/2-1}\mathrm{e}^{-x/2},\qquad x>0,
$$
then $X$ is said to have the **chi-squared distribution** with $\nu$ **degrees of freedom** (the parameter), written $X\sim\chi^2_\nu$.

Comparing densities shows that $\chi^2_\nu=\Gamma(\nu/2,1/2)$. If $Z_1,\dots,Z_n\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$, then $Z_1^2+\cdots+Z_n^2\sim\chi^2_n$: the case $n=1$ is Example 5.2.3 in [3.1.5](/3.1.5), and the general case follows from the additivity of the gamma distribution.

**Definition 4.3.5 (t-Distribution)** Let $\nu>0$. If the density of $X$ is

$$
f(x)=\frac{\Gamma\big(\frac{\nu+1}2\big)}{\sqrt{\nu\pi}\,\Gamma\big(\frac\nu2\big)}\Big(1+\frac{x^2}\nu\Big)^{-\frac{\nu+1}2},\qquad x\in\mathbb{R},
$$
then $X$ is said to have Student's **t-distribution** with parameter $\nu$, written $X\sim t_\nu$.

If $Z\sim\mathcal{N}(0,1)$ and $Y\sim\chi^2_n$ are independent, then $T=Z/\sqrt{Y/n}\sim t_n$. The t-distribution is symmetric about 0 ($T\sim t_\nu$ implies $-T\sim t_\nu$) and has heavier tails than the normal distribution; for large $\nu$, $t_\nu$ is very close to the standard normal distribution (this can be proved with the law of large numbers, see [3.1.12](/3.1.12)). The case $\nu=1$ is the Cauchy distribution, which has peculiar properties.

**Definition 4.3.6 (Cauchy Distribution)** If the density of $X$ is

$$
f(x)=\frac1{\pi(1+x^2)},\qquad x\in\mathbb{R},
$$
then $X$ is said to have the standard **Cauchy distribution**, also written $X\sim t_1$. More generally, $\mathrm{Cauchy}(\theta)$ has the density $\frac1{\pi(1+(x-\theta)^2)}$.

The density curve of the Cauchy distribution is the witch of Agnesi. Its tails are very heavy: $\int\lvert x\rvert f(x)\,\mathrm{d}x=\infty$, so under the strict definition of expectation it has no expectation ([3.1.8](/3.1.8)). It also has a counterintuitive property: if $Z_1,\dots,Z_n\overset{\text{iid}}{\sim}t_1$, then the sample mean $(Z_1+\cdots+Z_n)/n$ again has the distribution $t_1$ ([3.1.11](/3.1.11)); averaging does not concentrate it, and the law of large numbers fails for it.

**Definition 4.3.7 (F-Distribution)** Let $m,n$ be positive integers. If the density of $X$ is

$$
f(x)=\frac{\Gamma\big(\frac{m+n}2\big)m^{m/2}n^{n/2}x^{m/2-1}}{\Gamma\big(\frac m2\big)\Gamma\big(\frac n2\big)(mx+n)^{(m+n)/2}},\qquad x>0,
$$
then $X$ is said to have the **F-distribution** (Fisher–Snedecor distribution) with parameters $(m,n)$, written $X\sim F_{m,n}$.

If $X_1,\dots,X_m,Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$, then

$$
F=\frac{\frac1m\sum_{i=1}^mX_i^2}{\frac1n\sum_{j=1}^nY_j^2}\sim F_{m,n}.
$$
The F-distribution was introduced in 1924 by the British statistician Fisher and is named after him; it has important applications in the analysis of variance and linear regression.

### 4.3.4. Relations between Distributions

The connections between the distributions can be understood from the experiments behind them:

| Relation | Explanation |
|---|---|
| $\mathrm{Ber}(p)\to\mathrm{Bin}(n,p)$ | Sum of $n$ independent $\mathrm{Ber}(p)$ (fix the number of trials, count successes) |
| $\mathrm{Geo}(p)\to\mathrm{Pascal}(r,p)=r+\mathrm{NB}(r,p)$ | Sum of $r$ independent $\mathrm{Geo}(p)$ (fix the number of successes, count trials) |
| $\mathrm{H}(n,M,N)\to\mathrm{Bin}(n,p)$, $\mathrm{NH}(r,M,N)\to\mathrm{NB}(r,p)$ | $N\to\infty$, $M/N\to p$: sampling without replacement approaches sampling with replacement |
| $\mathrm{Bin}(n,p)\to\mathrm{Poi}(\lambda)$ | $n\to\infty$, $np\to\lambda$: rare events |
| $\mathrm{Bin}(n,p)$, $\mathrm{Poi}(\lambda)\to\mathcal{N}$ | Approximately normal after standardization as $n\to\infty$ or $\lambda\to\infty$ (central limit theorem) |
| $\mathrm{Exp}(\lambda)\to\Gamma(n,\lambda)$ | Sum of $n$ independent $\mathrm{Exp}(\lambda)$ |
| $\mathrm{Geo}(p)$ and $\mathrm{Exp}(\lambda)$ | The only memoryless discrete and continuous distributions; the exponential distribution is a continuous limit of the geometric distribution ([3.1.5](/3.1.5)) |
| $\mathrm{U}(0,1)$ and $\mathrm{Beta}(\alpha,\beta)$ | $\mathrm{Beta}(1,1)=\mathrm{U}(0,1)$; the order statistics of $\mathrm{U}(0,1)$ have beta distributions |
| $\mathcal{N}(0,1)\to\chi^2_n,\ t_n,\ F_{m,n}$ | Sums of squares and ratios of standard normal variables (sampling distributions) |

## Summary

| Distribution | PMF or density | Origin |
|---|---|---|
| $\mathrm{Ber}(p)$ | $\mathbb{P}(X=1)=p$, $\mathbb{P}(X=0)=1-p$ | Success or failure of a single trial |
| $\mathrm{Bin}(n,p)$ | $\binom nkp^k(1-p)^{n-k}$, $k=0,\dots,n$ | Number of successes in $n$ independent repeated trials |
| $\mathrm{Geo}(p)$ | $(1-p)^{k-1}p$, $k=1,2,\dots$ | Number of trials needed for the first success; memoryless |
| $\mathrm{NB}(r,p)$ | $\binom{k+r-1}{r-1}(1-p)^kp^r$, $k=0,1,\dots$ | Number of failures before the $r$-th success |
| $\mathrm{H}(n,M,N)$ | $\binom Mk\binom{N-M}{n-k}/\binom Nn$ | Number of defectives in sampling without replacement |
| $\mathrm{Poi}(\lambda)$ | $\lambda^k\mathrm{e}^{-\lambda}/k!$, $k=0,1,\dots$ | Number of occurrences of a rare event |
| $\mathrm{U}(a,b)$ | $\frac1{b-a}\boldsymbol{1}_{(a,b)}(x)$ | Geometric probability |
| $\mathrm{Exp}(\lambda)$ | $\lambda\mathrm{e}^{-\lambda x}\boldsymbol{1}_{[0,\infty)}(x)$ | Lifetime without aging; memoryless |
| $\mathcal{N}(\mu,\sigma^2)$ | $\frac1{\sigma\sqrt{2\pi}}\mathrm{e}^{-(x-\mu)^2/(2\sigma^2)}$ | Accumulation of many small independent effects |

Among the discrete distributions the most important are the Bernoulli, binomial, geometric and Poisson distributions; among the continuous ones, the uniform, exponential and normal distributions. When studying them, use concrete situations to establish the relations between different distributions, and then use these relations to understand the meaning of each distribution.
