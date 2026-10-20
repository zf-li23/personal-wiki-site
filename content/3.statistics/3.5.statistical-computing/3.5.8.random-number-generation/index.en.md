---
title: Random Number Generation
description: Pseudorandom number generators (linear congruential generators, full-period conditions, lattice structure, the Mersenne Twister, randomness tests) and the generation of non-uniform variates by discrete inversion, the inverse transform, rejection sampling, conditioning, uniform sampling under the graph of a density, transformations, ratio of uniforms, sums and mixtures.
---

Every simulation in this course, from the **Monte Carlo method** ([3.1.12](/3.1.12)) and the **bootstrap** ([3.5.7](/3.5.7)) to the Markov chain Monte Carlo of [3.5.9](/3.5.9), consumes random numbers. This chapter explains how a deterministic computer produces them and how they are turned into samples from a given distribution. It has two parts. The first constructs uniform pseudorandom numbers: what "random" means for a sequence, the linear congruential generator, its period and its lattice structure, and the modern Mersenne Twister. The second generates random variates from other distributions: discrete distributions, the inverse transform method (whose theory is in [3.1.7](/3.1.7)), rejection sampling and its variants, and transformation methods, including the **Box–Muller transform** and multivariate normal sampling via the **Cholesky decomposition** ([3.5.3](/3.5.3)). Throughout, "random number" means a $\mathrm{U}(0,1)$ variate and "random variate" a draw from any other distribution. The guiding questions are how a deterministic algorithm can fake randomness, which general sampling methods exist for an arbitrary (possibly complicated, without closed-form distribution function) target, and where their efficiency bottlenecks lie.

## 8.1. Uniform Pseudorandom Numbers

### 8.1.1. Random and Pseudorandom Numbers

> In a sense, there is no such thing as a random number; for example, is 2 a random number? Rather, we speak of a sequence of independent random numbers with a specified distribution. (D. E. Knuth, *The Art of Computer Programming*, Vol. 2)

Each number of such a sequence is obtained merely by chance, has nothing to do with the other numbers, and has a specified probability of falling in any given range. Physical devices can produce such sequences: dice, cards, numbered balls, spinning discs, electric noise circuits (the ERNIE machine that draws the British Premium Bonds), counting gamma rays, or published tables of random digits. Their disadvantages are extra hardware, low speed and, above all, no reproducibility.

**Definition 8.1.1 (Pseudorandom Number Generator)** A **pseudorandom number generator** (PRNG), also called a deterministic random bit generator, is a deterministic algorithm that, started from an initial value $x_0$ called the **seed**, outputs a sequence of numbers that can be used in place of an i.i.d. sequence of truly random numbers: the sequence is deterministic and reproducible, yet it passes statistical tests of randomness.

A generator on a finite state space eventually repeats. The output sequence consists of an initial segment (the tail) followed by a cycle; the length of the cycle is the period of the generator from that seed. PRNGs are fast and reproducible, which makes them the kernel of Monte Carlo simulation, of the computations of Bayesian analysis, and of electronic games and cryptography. Together with theory and experiment, simulation has become a third approach to the natural sciences.

A generator of uniform pseudorandom numbers is the essential building block: its output is assumed to be an i.i.d. $\mathrm{U}(0,1)$ sequence, and all other distributions are obtained by transforming it. The validity of every transformation method depends strongly on this assumption.

### 8.1.2. Linear Congruential Generators

**Definition 8.1.2 (Linear Congruential Generator)** The **linear congruential generator** (LCG), proposed by D. H. Lehmer in 1949, produces integers by the recursion

$$
X_{i+1}\equiv aX_i+c \pmod m,\qquad i=0,1,\dots,
$$
with multiplier $a$, increment $c$, modulus $m$ and seed $X_0$. Then $X_i\in\{0,1,\dots,m-1\}$, and the random numbers are $R_i=X_i/m$. If $c=0$ the generator is called a **multiplicative congruential generator** (MCG).

**Example 8.1.1** For $m=8$, $a=5$, $c=1$, $X_0=5$:

$$
X_1\equiv5\cdot5+1=26\equiv2,\quad X_2\equiv11\equiv3,\quad X_3\equiv16\equiv0,\quad X_4\equiv1,
$$
and then $X_5=6$, $X_6=7$, $X_7=4$, $X_8=5$, $X_9=2$. The random numbers are $R_1,\dots,R_9=0.25,\ 0.375,\ 0,\ 0.125,\ 0.75,\ 0.875,\ 0.5,\ 0.625,\ 0.25$. The sequence "looks" random, but $X_i$ can only take the $m$ values $0,1,\dots,m-1$, and it repeats after $8$ steps.

Three observations hold in general.

- The sequence is periodic. The integers $X_i$ are nonnegative and bounded by $m$, so the sequence repeats in a cycle of period at most $m$. Generating more numbers than the period does not produce new points.
- It may produce $0$ (and an MCG stays at $0$ forever once it reaches it), whereas random numbers should lie in the open interval $(0,1)$.
- Successive pairs $(R_i,R_{i+1})$ always fall on a lattice; whether the lattice is fine or coarse depends on $a$.

The LCG achieves its full period if its cycle length is $m$ (for every seed).

**Theorem 8.1.1 (Hull–Dobell Theorem)** The LCG has full period $m$ if and only if:

1. $\gcd(m,c)=1$;
2. every prime $q$ dividing $m$ also divides $a-1$;
3. if $4\mid m$, then $4\mid a-1$.

**Theorem 8.1.2** For an MCG, $X_i\equiv a^iX_0\pmod m$, and the maximum possible period is $m-1$; it is attained when $m$ is prime and $a$ is a primitive root modulo $m$. If $m=2^n$ with $n\ge3$, the period is at most $2^{n-2}$, which is achieved when $X_0$ is odd and $a\equiv3$ or $5\pmod 8$.

The formula $X_i\equiv a^iX_0$ follows by induction: $X_{i+1}\equiv aX_i\equiv a\cdot a^iX_0$. It also allows the generator to jump ahead: $a^k \bmod m$ is computed by repeated squaring.

**Example 8.1.2** For $X_{i+1}\equiv11X_i+5\pmod{16}$ with $X_0=1$, the maximum possible period is $m=16$. Conditions 1 ($\gcd(16,5)=1$) and 2 (the prime $2$ divides $a-1=10$) hold, but $4\mid16$ while $4\nmid10$, so condition 3 fails and the full period is not achieved. Indeed the sequence is $0,5,12,9,8,13,4,1,0,\dots$, of period $8$.

**Example 8.1.3** Well-known LCGs:

- RANDU, $X_{i+1}\equiv65539X_i\pmod{2^{31}}$ (an MCG), was widely adopted in the 1960s because it ran fast. Its two-dimensional lattice is acceptable, but its three-dimensional one is not: since $65539=2^{16}+3$,

  $$
  a^2=(2^{16}+3)^2=2^{32}+6\cdot2^{16}+9\equiv6(2^{16}+3)-9=6a-9\pmod{2^{31}},
  $$
  so $X_{i+2}\equiv6X_{i+1}-9X_i$ and $9R_i-6R_{i+1}+R_{i+2}$ is an integer. As it lies strictly between $-6$ and $10$, all triples $(R_i,R_{i+1},R_{i+2})$ fall on just $15$ parallel planes. This discovery cast doubt on Monte Carlo results obtained with RANDU in the 1960s and 1970s.
- $X_{i+1}\equiv16807X_i\pmod{2^{31}-1}$, proposed by Lewis, Goodman and Miller (1969) for the IBM System/360. The modulus is a prime and $16807=7^5$ is a primitive root, so the period is $2^{31}-2$. Because of its performance in empirical tests and its ease of implementation, Park and Miller (1988) proposed it as the minimal standard against which other generators should be compared; it was built into operating systems, the IMSL library, MATLAB and many simulation packages.

More generally, Marsaglia (1968) showed that the $d$-tuples $(R_i,\dots,R_{i+d-1})$ of any LCG lie on at most $(d!\,m)^{1/d}$ parallel hyperplanes. With $m=2^{31}$ and $d=10$ this is only about $39$, so LCGs are unsuitable for high-dimensional Monte Carlo.

![Lattice structure of LCGs. Left and middle: the successive pairs of the full-period generators with m = 101 and a = 3 (three lines) or a = 12 (a finer lattice). Right: RANDU triples projected on the normal (9, -6, 1) of its planes take only 15 values, whereas Mersenne Twister triples spread continuously.](./plots/lcg-lattice.py)

### 8.1.3. Testing Pseudorandom Numbers

"Pseudo" means that generating numbers by a known method removes the potential for true randomness. Possible departures from ideal randomness are:

- the numbers are not uniformly distributed, or take discrete instead of continuous values, or have a mean or variance that is too high or too low;
- the numbers are dependent: autocorrelation, runs of numbers successively higher or lower than their neighbors, several numbers above the mean followed by several below it.

Generators are therefore subjected to statistical tests of two kinds.

- Tests of uniformity, $H_0\colon R_i\sim\mathrm{U}(0,1)$ against $H_1\colon R_i\not\sim\mathrm{U}(0,1)$, for example the chi-square goodness-of-fit test on a partition of $[0,1)$ or the Kolmogorov–Smirnov test.
- Tests of independence, $H_0$: the $R_i$ are independent, against $H_1$: they are not, for example runs tests, autocorrelation tests and the serial test (chi-square test on $d$-tuples in $[0,1)^d$).

Failing to reject $H_0$ means only that no evidence of non-uniformity or dependence has been detected. Batteries such as Diehard and TestU01 combine hundreds of such tests.

### 8.1.4. The Mersenne Twister

The Mersenne Twister (Matsumoto and Nishimura, 1998) is the benchmark of modern pseudorandom generators. Its state is a vector of $19937$ bits (624 words of 32 bits); each step "twists" the state by shifts, exclusive-or operations and a linear transformation over $\mathbb{F}_2$, and outputs a tempered 32-bit number. Its period is the Mersenne prime $2^{19937}-1$, far beyond the $2^{31}-1$ of an LCG.

- High-dimensional structure: it is equidistributed in up to $623$ dimensions (at 32-bit accuracy), so it avoids the coarse low-dimensional lattices of LCGs.
- Statistical quality: it passes almost all standard randomness tests (such as Diehard).
- Speed: although complex, it is efficient after optimization. It is the default generator of R, MATLAB and Python's `random` module; NumPy's legacy `RandomState` uses it, while NumPy's newer `Generator` defaults to PCG64.

It is not suitable for cryptography: its output is a linear function of the state, which can be reconstructed from $624$ consecutive outputs.

```r
RNGkind()        # "Mersenne-Twister" "Inversion" "Rejection"
set.seed(2024)   # the seed makes a simulation reproducible
runif(3)
?.Random.seed    # details about the state of the default generator
```

## 8.2. Discrete Distributions and the Inverse Transform

From now on we assume that a generator of i.i.d. $\mathrm{U}(0,1)$ numbers is available, `runif` in R. The baseline task, drawing a simple random sample from a finite population, already requires a discrete uniform distribution; R's `sample` does this, and for every standard distribution R provides four functions:

```r
sample(0:1, size = 10, replace = TRUE)          # toss some coins
sample(1:100, size = 6, replace = FALSE)        # choose some lottery numbers
sample(letters)                                 # a random permutation of a-z
x <- sample(1:3, size = 100, replace = TRUE, prob = c(.2, .3, .5))
table(x)                                        # one run gave 14, 31, 55

dbinom(x, size, prob, log = FALSE)              # probability mass function or density
pbinom(q, size, prob, lower.tail = TRUE)        # cumulative distribution function
qbinom(p, size, prob, lower.tail = TRUE)        # quantile function
rbinom(n, size, prob)                           # random generator
```

### 8.2.1. Discrete Distributions

**Lemma 8.2.1** Let $U\sim\mathrm{U}(0,1)$ and $n\in\mathbb{N}_+$, and let $X=\lfloor nU\rfloor$. Then $X$ is uniformly distributed on $\{0,1,\dots,n-1\}$.

**Proof** For $k=0,1,\dots,n-1$,
$\mathbb{P}(X=k)=\mathbb{P}(\lfloor nU\rfloor=k)=\mathbb{P}(nU\in[k,k+1))=\mathbb{P}(U\in[k/n,(k+1)/n))=1/n$. $\square$

**Lemma 8.2.2** Let $p\in[0,1]$, $U\sim\mathrm{U}(0,1)$ and $E=\{U\le p\}$. Then $\mathbb{P}(E)=p$; in particular $\boldsymbol{1}_E\sim\mathrm{Ber}(p)$.

**Lemma 8.2.3** Let $A=\{a_i\mid i\in I\}$ with $I=\{1,\dots,n\}$ or $I=\mathbb{N}_+$ and $a_i\ne a_j$ for $i\ne j$, and let $p_i\ge0$ with $\sum_{i\in I}p_i=1$. Let $U\sim\mathrm{U}(0,1)$ and

$$
K=\min\Bigl\{k\in I\Bigm|\sum_{i=1}^kp_i\ge U\Bigr\}.
$$
Then $X=a_K$ satisfies $\mathbb{P}(X=a_k)=p_k$ for all $k\in I$.

**Proof** $\mathbb{P}(X=a_k)=\mathbb{P}(K=k)=\mathbb{P}\bigl(\sum_{i=1}^{k-1}p_i<U\le\sum_{i=1}^kp_i\bigr)=p_k$. $\square$

This is the inverse transform for a discrete distribution: $K$ is the generalized inverse of the distribution function evaluated at $U$. Ordering the values by decreasing $p_i$ reduces the expected number of comparisons.

**Example 8.2.1** The **geometric distribution** $\mathrm{Geo}(p)$, the number $X$ of independent trials with success probability $p$ until the first success, has $p_i=\mathbb{P}(X=i)=(1-p)^{i-1}p$, $i\in\mathbb{N}_+$. With $a_i=i$, $\sum_{i=1}^kp_i=1-(1-p)^k$, and

$$
\sum_{i=1}^kp_i\ge U\iff(1-p)^k\le1-U\iff k\ge\frac{\log(1-U)}{\log(1-p)}.
$$
Hence

$$
X=K=\Bigl\lceil\frac{\log(1-U)}{\log(1-p)}\Bigr\rceil\sim\mathrm{Geo}(p),
$$
where $\lceil\cdot\rceil$ rounds up to the nearest integer. One uniform number replaces a whole sequence of Bernoulli trials; since $1-U\sim\mathrm{U}(0,1)$, $\log U$ can be used instead of $\log(1-U)$.

### 8.2.2. The Inverse Transform Method

By the **probability integral transform**, if $X$ is a continuous random variable with distribution function $F_X$, then $F_X(X)\sim\mathrm{U}(0,1)$. Conversely, define the generalized inverse

$$
F_X^{-1}(u)=\inf\{x\in\mathbb{R}\colon F_X(x)\ge u\},\qquad0<u<1.
$$
Then $F_X^{-1}(U)$ has the same distribution as $X$ for any distribution function ([Theorem 7.3.1 of 3.1.7](/3.1.7#thm-7.3.1)), since

$$
\mathbb{P}(F_X^{-1}(U)\le x)=\mathbb{P}\bigl(\inf\{t\colon F_X(t)\ge U\}\le x\bigr)=\mathbb{P}(U\le F_X(x))=F_X(x).
$$

**Algorithm 8.2.1 (Inverse Transform Method)**

1. Derive the inverse function $F_X^{-1}(u)$.
2. For each random variate required: generate $u$ from $\mathrm{U}(0,1)$ and deliver $x=F_X^{-1}(u)$.

The method (**inverse transform sampling**) is easy to apply provided $F_X^{-1}$ is easy to compute.

**Example 8.2.2** If $F_X(x)=x^3$ on $(0,1)$, then $F_X^{-1}(u)=u^{1/3}$, and the density is $f(x)=3x^2$:

```r
n <- 1000
u <- runif(n)
x <- u^(1/3)
hist(x, prob = TRUE, main = expression(f(x) == 3*x^2))   # density histogram of the sample
y <- seq(0, 1, .01)
lines(y, 3*y^2)                                          # density curve f(x)
```

**Example 8.2.3** The **Rayleigh distribution** with parameter $\sigma>0$ has density $f(x)=\frac{x}{\sigma^2}\mathrm{e}^{-x^2/(2\sigma^2)}$, $x\ge0$. For $a\ge0$,

$$
F(a)=\int_0^a\frac{x}{\sigma^2}\mathrm{e}^{-x^2/(2\sigma^2)}\,\mathrm{d}x=\Bigl[-\mathrm{e}^{-x^2/(2\sigma^2)}\Bigr]_0^a=1-\mathrm{e}^{-a^2/(2\sigma^2)},
$$
and solving $u=F(x)$ gives $x=\sqrt{-2\sigma^2\log(1-u)}$.

The method also applies to discrete distributions (Lemma 8.2.3), but it has two limitations. It needs a closed-form, cheaply invertible distribution function (exponential, uniform, Bernoulli, Rayleigh, Cauchy, ...); for the normal or gamma distributions the inverse must be computed numerically. And distribution functions exist only in one dimension: for distributions on $\mathbb{R}^d$ with $d>1$ more sophisticated methods are required.

## 8.3. Rejection Sampling

*Rejection sampling* (the acceptance–rejection method) is a more advanced and very popular method. It is often used in multi-stage approaches: another method generates samples of approximately the right distribution, and rejection converts them into samples of exactly the target distribution. It works on very general spaces. Its price is that a random and possibly large number of input samples is needed for each output sample, so efficiency is the main concern.

### 8.3.1. Basic Rejection Sampling

We want to generate a random variable $X$ with a complicated density (or probability mass function) $f$, and we can generate a random variable with a simple density $g$.

**Algorithm 8.3.1 (Basic Rejection Sampling)** Input: a probability density $g$ (the *proposal density*) and a function $p$ with values in $[0,1]$ (the acceptance probability). Randomness used: i.i.d. proposals $X_n$ with density $g$ and i.i.d. $U_n\sim\mathrm{U}(0,1)$.

1. For $n=1,2,3,\dots$: generate $X_n$ with density $g$ and $U_n\sim\mathrm{U}(0,1)$.
2. If $U_n\le p(X_n)$, output $X_n$; otherwise discard it.

**Theorem 8.3.1** Let $Z=\int p(x)g(x)\,\mathrm{d}x>0$ and let $X_{N_k}$ be the $k$-th output, $k\in\mathbb{N}_+$. Then:

1. the outputs $X_{N_1},X_{N_2},\dots$ are i.i.d. with density
   $$
   f(x)=\frac1Zp(x)g(x);
   $$
2. each proposal is accepted with probability $Z$, and the number $M_k=N_k-N_{k-1}$ of proposals needed for each output is geometrically distributed with mean $1/Z$.

**Proof** (2) For fixed $n$, $\mathbb{P}(U_n\le p(X_n))=\int p(x)g(x)\,\mathrm{d}x=Z$. Decisions for different $n$ are independent, so the waiting time until the first acceptance is $\mathrm{Geo}(Z)$, with mean $1/Z$.

(1) Let $N_0=0$ and $N_k=\min\{n>N_{k-1}\mid U_n\le p(X_n)\}$. For a set $A$, $\mathbb{P}(U_n\le p(X_n),X_n\in A)=\int_Ap(x)g(x)\,\mathrm{d}x$. By the independence of the pairs $(X_n,U_n)$,

$$
\begin{aligned}
\mathbb{P}(X_{N_k}\in A\mid N_{k-1}=n)&=\sum_{m=1}^\infty\mathbb{P}\bigl(N_k=n+m,\ X_{n+m}\in A\mid N_{k-1}=n\bigr)\\
&=\sum_{m=1}^\infty\mathbb{P}(U_{n+1}>p(X_{n+1}))\cdots\mathbb{P}(U_{n+m-1}>p(X_{n+m-1}))\,\mathbb{P}(U_{n+m}\le p(X_{n+m}),X_{n+m}\in A)\\
&=\sum_{m=1}^\infty(1-Z)^{m-1}\int_Ap(x)g(x)\,\mathrm{d}x=\frac1Z\int_Ap(x)g(x)\,\mathrm{d}x.
\end{aligned}
$$
This does not depend on $n$, so $\mathbb{P}(X_{N_k}\in A)=\frac1Z\int_Ap(x)g(x)\,\mathrm{d}x$. Summing over the cases $N_1=n_1,\dots,N_k=n_k$ in the same way shows $\mathbb{P}(X_{N_1}\in A_1,\dots,X_{N_k}\in A_k)=\prod_{i=1}^k\mathbb{P}(X_{N_i}\in A_i)$, that is, independence. $\square$

The function $p$ is the conditional probability of acceptance given the proposal $X_n=x$, while $Z$ is the marginal (average) acceptance probability: with $I=\boldsymbol{1}\{U_n\le p(X_n)\}$ we have $I\mid X_n=x\sim\mathrm{Ber}(p(x))$ and $I\sim\mathrm{Ber}(Z)$. The algorithm itself never uses the value of $Z$; it only matters for the efficiency, which improves as $Z$ increases.

**Example 8.3.1 (Wigner's Semicircle Distribution)** Wigner's semicircle distribution

$$
f(x)=\frac{2}{\pi R^2}\sqrt{R^2-x^2}\,\boldsymbol{1}_{[-R,R]}(x)
$$
is a scaled beta distribution; it is the limiting distribution of the eigenvalues of many random symmetric matrices as their size tends to infinity. For $R=1$, let $X\sim\mathrm{U}(-1,1)$ and accept $X$ with probability $p(X)=\sqrt{1-X^2}$. Then $g(x)=\frac12\boldsymbol{1}_{[-1,1]}(x)$,

$$
Z=\int p(x)g(x)\,\mathrm{d}x=\frac12\int_{-1}^1\sqrt{1-x^2}\,\mathrm{d}x=\frac\pi4,
$$
and the accepted samples have density $\frac1Zp(x)g(x)=\frac2\pi\sqrt{1-x^2}\,\boldsymbol{1}_{[-1,1]}(x)$.

### 8.3.2. Envelope Rejection Sampling

**Algorithm 8.3.2 (Envelope Rejection Sampling)** Input: a function $f\ge0$ (the target density, possibly non-normalized), a proposal density $g$, and a constant $c>0$ such that $f(x)\le cg(x)$ for all $x$.

1. Generate $X_n$ with density $g$ and $U_n\sim\mathrm{U}(0,1)$.
2. If $U_n\le f(X_n)/(cg(X_n))$, accept and deliver $X_n$; otherwise reject $X_n$ and return to step 1.

This is the basic algorithm with $p(x)=f(x)/(cg(x))$ (and $p(x)=1$ where $g(x)=0$). For a discrete target the correctness can also be read from **Bayes' theorem**: $\mathbb{P}(\text{accept}\mid X=k)=\frac{f(k)}{cg(k)}$, so $\mathbb{P}(\text{accept})=\sum_k\frac{f(k)}{cg(k)}g(k)=\frac1c$ for a normalized $f$, and

$$
\mathbb{P}(X=k\mid\text{accept})=\frac{\mathbb{P}(\text{accept}\mid X=k)\,g(k)}{\mathbb{P}(\text{accept})}=\frac{f(k)/c}{1/c}=f(k).
$$

**Theorem 8.3.2** Let $Z_f=\int f(x)\,\mathrm{d}x$. The outputs of Algorithm 8.3.2 are i.i.d. with the normalized density $\tilde f(x)=f(x)/Z_f$; each proposal is accepted with probability $Z_f/c$, and the number of proposals per output is geometrically distributed with mean $c/Z_f$.

**Proof** Apply Theorem 8.3.1 with $p(x)=f(x)/(cg(x))$: $Z=\int\frac{f(x)}{cg(x)}g(x)\,\mathrm{d}x=\frac1c\int f(x)\,\mathrm{d}x=\frac{Z_f}{c}$ and $\frac1Zp(x)g(x)=\frac{f(x)}{Z_f}$. $\square$

The geometry explains the name. Given $X_n$, the point $(X_n,cg(X_n)U_n)$ is uniformly distributed under the graph of $cg$, the envelope; the proposal is accepted if and only if $f(X_n)\ge cg(X_n)U_n$, that is, if the point falls under the graph of $f$. The algorithm needs $f$ only up to a constant, which is why it is so useful for posterior densities.

**Example 8.3.2** We first sample the half-normal distribution, the **standard normal distribution** conditioned on being positive, with density $f(x)=\sqrt{2/\pi}\,\mathrm{e}^{-x^2/2}$, $x\ge0$, using $\mathrm{Exp}(\lambda)$ proposals $g(x)=\lambda\mathrm{e}^{-\lambda x}$, $x\ge0$. For $x\ge0$,

$$
\frac{f(x)}{g(x)}=\frac{1}{\lambda}\sqrt{\frac2\pi}\exp\Bigl(-\frac{x^2}{2}+\lambda x\Bigr)\le\frac1\lambda\sqrt{\frac2\pi}\exp\Bigl(\frac{\lambda^2}{2}\Bigr)=:c,
$$
with equality at $x=\lambda$. Any $c^*\ge c$ also satisfies $f\le c^*g$, but the cost is proportional to $c$, so $c$ should be as small as possible. The acceptance condition is

$$
U_n\le\frac{f(X_n)}{cg(X_n)}=\exp\Bigl(-\frac12(X_n-\lambda)^2\Bigr).
$$
Minimizing $c(\lambda)$ gives $\lambda=1$ and $c=\sqrt{2\mathrm{e}/\pi}\approx1.315$, an acceptance rate of $1/c\approx0.76$. Finally, standard normal values are obtained by attaching to each accepted $X_n$ a random sign, $+X_n$ or $-X_n$ with probability $1/2$ each.

![Envelope rejection sampling of the half-normal density with Exp(1) proposals. Left: proposals (X, c g(X) U) are uniform under the envelope c g; those under f are accepted. Right: the accepted values with random signs follow N(0, 1).](./plots/rejection-half-normal.py)

The proposal density $g$ is chosen to maximize the efficiency.

- Since $f\le cg$, the support of $g$ must contain the support of $f$.
- The average cost of one sample is the average number of proposals times the cost of one proposal. So $g$ should be easy to sample, and $c/Z_f$ should be small, that is, $g$ should be as close in shape to $f$ as possible.

**Remark 8.3.1** Adaptive rejection sampling (Gilks and Wild, 1992) refines this idea for log-concave densities: the envelope is a piecewise exponential function built from tangents to $\log f$, and every rejected point is used to tighten the envelope, so the acceptance rate tends to $1$. It is used, for example, inside Gibbs samplers ([3.5.9](/3.5.9)).

### 8.3.3. Conditional Distributions

The conditional distribution $P_{X\mid X\in A}$ describes the randomness that remains in $X$ once we know that $X\in A$ has occurred.

**Algorithm 8.3.3 (Sampling a Conditional Distribution)** Input: a set $A$ with $\mathbb{P}(X\in A)>0$, and i.i.d. copies $X_n$ of $X$ (the proposals). For $n=1,2,\dots$: generate $X_n$; if $X_n\in A$, output $X_n$.

**Theorem 8.3.3** The outputs of Algorithm 8.3.3 are i.i.d. with $\mathbb{P}(X_{N_k}\in B)=\mathbb{P}(X\in B\mid X\in A)$ for every $B$, and the number of proposals per output is geometrically distributed with mean $1/\mathbb{P}(X\in A)$.

**Proof** This is basic rejection sampling with $p(x)=\boldsymbol{1}_A(x)$. If $X$ has a density $g$, then $Z=\int\boldsymbol{1}_A(x)g(x)\,\mathrm{d}x=\mathbb{P}(X\in A)$ and

$$
\mathbb{P}(X_{N_k}\in B)=\frac{\int_B\boldsymbol{1}_A(x)g(x)\,\mathrm{d}x}{Z}=\frac{\mathbb{P}(X\in A\cap B)}{\mathbb{P}(X\in A)}=\mathbb{P}(X\in B\mid X\in A). \qquad\square
$$

The method works well when $\mathbb{P}(X\in A)$ is large; the time for one output is proportional to $1/\mathbb{P}(X\in A)$.

**Example 8.3.3 (Truncated Normal Distribution)** To generate $X\sim\mathcal{N}(0,1)$ conditioned on $X\ge a>0$, repeat: generate $X\sim\mathcal{N}(0,1)$; if $X\ge a$, output $X$. The expected number of proposals is $\mathbb{E}(M_k)=1/(1-\Phi(a))$, computed in R by `1/(1-sapply(1:6, pnorm))`:

| $a$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|
| $\mathbb{E}(M_k)$ | $6.3$ | $44$ | $741$ | $31\,574$ | $3\,488\,556$ | $1\,013\,594\,692$ |

The method is slow even for moderate $a$ and impractical for $a\ge5$.

The envelope version is far better. The conditional density is $\tilde f(x)=f(x)/Z_f$ with $f(x)=\exp(-x^2/2)\boldsymbol{1}_{[a,\infty)}(x)$. Use the shifted exponential proposals $X=\tilde X+a$, $\tilde X\sim\mathrm{Exp}(\lambda)$, with density $g(x)=\lambda\mathrm{e}^{-\lambda(x-a)}\boldsymbol{1}_{[a,\infty)}(x)$. Then for $x\ge a$

$$
\frac{f(x)}{g(x)}=\frac1\lambda\exp\Bigl(-\frac{x^2}{2}+\lambda(x-a)\Bigr).
$$
A simple choice is $\lambda=a$, which makes $g$ decay like $f$ at the truncation point; the exponent $-\frac{x^2}{2}+a(x-a)=-\frac{(x-a)^2}{2}-\frac{a^2}{2}$ is maximal at $x=a$, so $c=\frac1a\mathrm{e}^{-a^2/2}$ and the acceptance condition is $U\le\exp(-(X-a)^2/2)$. (The value minimizing $c$ is $\lambda^*=\frac{a+\sqrt{a^2+4}}{2}$, slightly larger than $a$, with almost the same efficiency.) The procedure:

1. generate $\tilde X\sim\mathrm{Exp}(a)$ and $U\sim\mathrm{U}(0,1)$;
2. let $X=\tilde X+a$;
3. if $U\le\exp(-(X-a)^2/2)$, output $X$.

The expected number of proposals is now

$$
\mathbb{E}(M_k)=\frac{c}{Z_f}=\frac{\frac1a\mathrm{e}^{-a^2/2}}{\int_a^\infty\mathrm{e}^{-x^2/2}\,\mathrm{d}x}=\frac{\mathrm{e}^{-a^2/2}}{a\sqrt{2\pi}\,(1-\Phi(a))}:
$$

| $a$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|
| $\mathbb{E}(M_k)$ | $1.53$ | $1.19$ | $1.09$ | $1.06$ | $1.04$ | $1.03$ |

The farther the truncation point, the better the exponential tail matches the normal tail.

### 8.3.4. Uniform Distributions and Densities

**Definition 8.3.1 (Uniform Distribution on a Set)** A random variable $X$ with values in $\mathbb{R}^d$ is uniformly distributed on a set $A\subseteq\mathbb{R}^d$ with volume $0<\lvert A\rvert<\infty$ if $\mathbb{P}(X\in B)=\lvert A\cap B\rvert/\lvert A\rvert$ for all $B\subseteq\mathbb{R}^d$.

**Example 8.3.4** Let $X_n,Y_n\sim\mathrm{U}(-1,1)$ be i.i.d.; the pairs $(X_n,Y_n)$ are uniform on the square $Q=[-1,1]\times[-1,1]$ (if $X\sim\mathrm{U}(a,b)$ and $Y\sim\mathrm{U}(c,d)$ are independent, $(X,Y)$ is uniform on $[a,b]\times[c,d]$, because the joint density is constant there). Keep the pairs with $X_n^2+Y_n^2\le1$. By Theorem 8.3.3 the kept points form an i.i.d. sequence uniformly distributed on the unit disk $D=\{x\in\mathbb{R}^2\colon\lvert x\rvert\le1\}$. The acceptance probability is $\lvert D\rvert/\lvert Q\rvert=\pi/4\approx78.5\%$, and on average $4/\pi\approx1.27$ proposals are needed per point.

**Theorem 8.3.4 (Fundamental Theorem of Simulation)** Let $f\colon\mathbb{R}^d\to[0,\infty)$ be a probability density and

$$
A=\{(x,y)\in\mathbb{R}^d\times[0,\infty)\mid0\le y<f(x)\}\subseteq\mathbb{R}^{d+1}.
$$
Then $\lvert A\rvert=1$, and the following are equivalent:

1. $(X,Y)$ is uniformly distributed on $A$;
2. $X$ has density $f$, and $Y=f(X)U$ with $U\sim\mathrm{U}(0,1)$ independent of $X$.

**Proof** $\lvert A\rvert=\int_{\mathbb{R}^d}\int_0^{f(x)}\mathrm{d}y\,\mathrm{d}x=\int_{\mathbb{R}^d}f(x)\,\mathrm{d}x=1$.

(1) $\Rightarrow$ (2): let $U=Y/f(X)$. For sets $C\subseteq\mathbb{R}^d$ and $D\subseteq\mathbb{R}$, substituting $y=f(x)u$,

$$
\mathbb{P}(X\in C,U\in D)=\Bigl\lvert A\cap\{(x,y)\colon x\in C,\ y/f(x)\in D\}\Bigr\rvert=\int_{\mathbb{R}^d}\int_0^{f(x)}\boldsymbol{1}_C(x)\boldsymbol{1}_D\Bigl(\frac{y}{f(x)}\Bigr)\mathrm{d}y\,\mathrm{d}x=\int_Cf(x)\,\mathrm{d}x\cdot\int_D\boldsymbol{1}_{[0,1]}(u)\,\mathrm{d}u.
$$
So $X$ and $U$ are independent with densities $f$ and $\boldsymbol{1}_{[0,1]}$.

(2) $\Rightarrow$ (1): given $X=x$, $Y=f(x)U\sim\mathrm{U}(0,f(x))$. For $B=C\times D$ with $C\subseteq\mathbb{R}^d$, $D\subseteq[0,\infty)$,

$$
\mathbb{P}((X,Y)\in B)=\int_C\frac{\lvert D\cap[0,f(x)]\rvert}{f(x)}f(x)\,\mathrm{d}x=\int_C\lvert D\cap[0,f(x)]\rvert\,\mathrm{d}x=\lvert A\cap B\rvert.
$$
Rectangles determine the distribution, so $(X,Y)$ is uniform on $A$. $\square$

Sampling from a density is therefore the same as sampling uniformly from the region under its graph, one dimension higher. This is exactly why envelope rejection works: $(X_k,cg(X_k)U_k)$ is uniform under $cg$, and the accepted points are uniform under $f$, so their first coordinates have density $f$.

**Example 8.3.5** To sample $X$ with density $p(x)=2x$, $0\le x\le1$, generate $Y\sim\mathrm{U}(0,1)$ and $U_1\sim\mathrm{U}(0,1)$, and set $U=2U_1$; $(Y,U)$ is uniform on the box $[0,1]\times[0,2]$, which contains the graph since $p(x)\in[0,2]$. The points under the curve $u=2y$ are the ones we want: $X=Y\mid U<2Y$ has density $p$. In terms of envelope rejection, $g=1$ and $f/g=2x\le2=c$, so the mean number of trials per simulated value is $c=2$.

In general, to sample a density $f\colon[a,b]\to\mathbb{R}$ with $f\le M$: let $(X_k,Y_k)$ be i.i.d. uniform on the rectangle $R=[a,b]\times[0,M]$, let $A=\{(x,y)\in R\mid y\le f(x)\}$ and $N=\min\{k\mid(X_k,Y_k)\in A\}$. Then $(X_N,Y_N)$ is uniform on $A$ and $X_N$ has density $f$. When $f$ lives on an unbounded set, replace the rectangle by the region $\{(x,y)\mid0\le y<cg(x)\}$ under an envelope, which is envelope rejection sampling again.

## 8.4. Transformation Methods

### 8.4.1. The General Transformation Theorem

The inverse transform method is a special case of transforming a uniformly distributed random variable; in general we transform random vectors by smooth bijections.

**Theorem 8.4.1 (Transformation of Random Variables)** Let $A,B\subseteq\mathbb{R}^d$ be open sets, $\varphi\colon A\to B$ a bijection that is differentiable with continuous partial derivatives, and $g\colon B\to[0,\infty)$ a probability density. Define

$$
f(x)=g(\varphi(x))\,\lvert\det D\varphi(x)\rvert\,\boldsymbol{1}_A(x),
$$
where $D\varphi=\bigl(\partial\varphi_i/\partial x_j\bigr)$ is the **Jacobian matrix**. Then $f$ is a probability density, and $X$ has density $f$ if and only if $\varphi(X)$ has density $g$.

Equivalently, if $X\sim g$ and $Y=\varphi(X)$, then $f_Y(y)=g(\varphi^{-1}(y))\lvert\det D\varphi^{-1}(y)\rvert$: the key is the **Jacobian determinant** ([3.1.7](/3.1.7)). Many transformations are used in practice; they need not be memorized:

- if $Z\sim\mathcal{N}(0,1)$, then $V=Z^2\sim\chi^2_1$;
- if $U\sim\chi^2_m$ and $V\sim\chi^2_n$ are independent, then $F=\frac{U/m}{V/n}\sim F_{m,n}$;
- if $Z\sim\mathcal{N}(0,1)$ and $V\sim\chi^2_n$ are independent, then $T=Z/\sqrt{V/n}\sim t_n$;
- if $U,V\sim\mathrm{U}(0,1)$ are independent, then $Z_1=\sqrt{-2\log U}\cos(2\pi V)$ and $Z_2=\sqrt{-2\log U}\sin(2\pi V)$ are independent standard normal variables;
- if $U\sim\Gamma(r,\lambda)$ and $V\sim\Gamma(s,\lambda)$ are independent, then $X=U/(U+V)\sim\mathrm{Beta}(r,s)$;
- if $U,V\sim\mathrm{U}(0,1)$ are independent, then $X=\Bigl\lfloor1+\dfrac{\log V}{\log(1-(1-\theta)^U)}\Bigr\rfloor$ has the logarithmic distribution with parameter $\theta$, $\mathbb{P}(X=x)=\dfrac{-\theta^x}{x\log(1-\theta)}$, $x\in\mathbb{N}_+$.

**Example 8.4.1** The standard **Cauchy distribution** is the **t-distribution** with $n=1$:

$$
f(x)=\frac{\Gamma\bigl(\frac{n+1}2\bigr)}{\sqrt{n\pi}\,\Gamma\bigl(\frac n2\bigr)}\Bigl(1+\frac{x^2}{n}\Bigr)^{-(n+1)/2}\overset{n=1}{=}\frac{\Gamma(1)}{\sqrt\pi\,\Gamma(\frac12)}\cdot\frac1{1+x^2}=\frac1{\pi(1+x^2)}.
$$
Hence if $Z_1,Z_2\sim\mathcal{N}(0,1)$ are i.i.d., then $Y=Z_1/Z_2\sim t_1$ is standard Cauchy.

### 8.4.2. The Box–Muller Transform

We want to sample the standard bivariate normal density $g(x,y)=\frac1{2\pi}\exp\bigl(-\frac{x^2+y^2}2\bigr)$. Use polar coordinates $\varphi(r,\theta)=(r\cos\theta,r\sin\theta)$ for $r>0$, $\theta\in(0,2\pi)$. On $A=(0,\infty)\times(0,2\pi)$ the image is $B=\varphi(A)=\mathbb{R}^2\setminus\{(x,0)\mid x\ge0\}$, a set of full measure. The Jacobian matrix is

$$
D\varphi(r,\theta)=\begin{bmatrix}\cos\theta&-r\sin\theta\\ \sin\theta&r\cos\theta\end{bmatrix},\qquad\det D\varphi(r,\theta)=r,
$$
so by Theorem 8.4.1 $(R,\Theta)=\varphi^{-1}(X,Y)$ has density

$$
f(r,\theta)=g(\varphi(r,\theta))\,\lvert\det D\varphi(r,\theta)\rvert=\frac1{2\pi}\cdot r\,\mathrm{e}^{-r^2/2}=f_1(\theta)f_2(r).
$$
Thus $\Theta\sim\mathrm{U}(0,2\pi)$ and $R$ are independent, and $R$ has the Rayleigh distribution with $\sigma=1$, which by Example 8.2.3 is generated as $\sqrt{-2\log(1-U)}$, or equivalently $\sqrt{-2\log U}$.

**Algorithm 8.4.1 (Box–Muller Transform)**

1. Generate $\Theta\sim\mathrm{U}(0,2\pi)$ and $U\sim\mathrm{U}(0,1)$ independently.
2. Let $R=\sqrt{-2\log U}$.
3. Then $(X,Y)=\varphi(R,\Theta)=(R\cos\Theta,R\sin\Theta)$ is standard normally distributed in $\mathbb{R}^2$: $X$ and $Y$ are independent $\mathcal{N}(0,1)$.

This method of converting pairs of uniform samples into pairs of normal samples, the **Box–Muller transform** (Box and Muller, 1958), was met as an example of change of variables in [3.1.7](/3.1.7).

### 8.4.3. The Multivariate Normal Distribution

Let $\boldsymbol{Z}\sim\mathcal{N}_d(\boldsymbol{0},I_d)$, a vector of i.i.d. standard normal variables. To generate $\boldsymbol{X}\sim\mathcal{N}_d(\boldsymbol\mu,\Sigma)$, factor $\Sigma=CC^{\mathsf T}$ and set $\boldsymbol{X}=C\boldsymbol{Z}+\boldsymbol\mu$; then $\boldsymbol{X}$ is normal with mean $\boldsymbol\mu$ and covariance $C I_d C^{\mathsf T}=\Sigma$ (**multivariate normal distribution**, [3.1.15](/3.1.15)).

In practice we transform a whole data matrix at once. Let $M=(Z_{ij})$ be an $n\times d$ matrix of i.i.d. $\mathcal{N}(0,1)$ entries, so that its rows $\boldsymbol{Z}_i^{\mathsf T}$ are independent $\mathcal{N}_d(\boldsymbol 0,I_d)$ vectors. Then the rows of

$$
X=\begin{bmatrix}\boldsymbol{X}_1^{\mathsf T}\\ \vdots\\ \boldsymbol{X}_n^{\mathsf T}\end{bmatrix}=\begin{bmatrix}\boldsymbol{Z}_1^{\mathsf T}C^{\mathsf T}+\boldsymbol\mu^{\mathsf T}\\ \vdots\\ \boldsymbol{Z}_n^{\mathsf T}C^{\mathsf T}+\boldsymbol\mu^{\mathsf T}\end{bmatrix}=MC^{\mathsf T}+\boldsymbol{1}\boldsymbol\mu^{\mathsf T}
$$
are a random sample of size $n$ from $\mathcal{N}_d(\boldsymbol\mu,\Sigma)$.

**Algorithm 8.4.2 (Multivariate Normal Sample)**

1. Generate an $n\times d$ matrix $M$ containing $nd$ independent $\mathcal{N}(0,1)$ variates.
2. Compute a factorization $\Sigma=CC^{\mathsf T}$.
3. Output $X=MC^{\mathsf T}+\boldsymbol{1}\boldsymbol\mu^{\mathsf T}$.

Three factorizations are common.

- **Spectral decomposition**: $\Sigma=P\Lambda P^{\mathsf T}$, and $Q=\Sigma^{1/2}=P\Lambda^{1/2}P^{\mathsf T}$ is symmetric, so $C=C^{\mathsf T}=Q$.
- **Singular value decomposition**: $\Sigma=UDV^{\mathsf T}$ with $U=V=P$ for a symmetric positive semidefinite matrix, and $Q=\Sigma^{1/2}=UD^{1/2}V^{\mathsf T}$ is the same square root.
- **Cholesky decomposition**: R's `chol(Sigma)` returns the upper triangular $Q$ with $\Sigma=Q^{\mathsf T}Q$, so $C=Q^{\mathsf T}$ and $X=MQ+\boldsymbol{1}\boldsymbol\mu^{\mathsf T}$. It is the cheapest of the three.

**Example 8.4.2** Generate $1000$ observations from the bivariate normal distribution with $\boldsymbol\mu=(0,0)^{\mathsf T}$ and $\Sigma=\begin{bmatrix}1&0.9\\0.9&1\end{bmatrix}$ by the spectral method:

```r
rmvn.eigen <- function(n, mu, Sigma) {
  d <- length(mu)
  ev <- eigen(Sigma, symmetric = TRUE)
  lambda <- ev$values
  V <- ev$vectors
  Q <- V %*% diag(sqrt(lambda)) %*% t(V)            # Q = Sigma^(1/2)
  M <- matrix(rnorm(n*d), nrow = n, ncol = d)
  X <- M %*% Q + matrix(mu, n, d, byrow = TRUE)
  X
}
mu <- c(0, 0)
Sigma <- matrix(c(1, .9, .9, 1), nrow = 2, ncol = 2)
X <- rmvn.eigen(1000, mu, Sigma)                     # generate the sample
print(colMeans(X))
print(cor(X))
plot(X, xlab = "x", ylab = "y", pch = 20)

# SVD and Cholesky alternatives for the factor Q
S <- svd(Sigma); Q <- S$u %*% diag(sqrt(S$d)) %*% t(S$v)
Q <- chol(Sigma)                                     # Sigma = t(Q) %*% Q
```

```text
> print(colMeans(X))
[1] -0.001628189  0.023474775
> print(cor(X))
          [,1]      [,2]
[1,] 1.0000000 0.8931007
[2,] 0.8931007 1.0000000
```

The sample means are close to $0$ and the sample correlation is close to $0.9$. Ready-made functions exist, `mvrnorm` in the package `MASS` and `rmvnorm` in `mvtnorm`; the point of the example is that only `rnorm` is needed.

### 8.4.4. The Ratio-of-Uniforms Method

**Theorem 8.4.2 (Ratio of Uniforms)** Let $f\colon\mathbb{R}^d\to[0,\infty)$ satisfy $Z=\int_{\mathbb{R}^d}f(x)\,\mathrm{d}x<\infty$, and let $X=(X_0,X_1,\dots,X_d)$ be uniformly distributed on

$$
A=\Bigl\{(x_0,x_1,\dots,x_d)\Bigm|x_0>0,\ \frac{x_0^{d+1}}{d+1}<f\Bigl(\frac{x_1}{x_0},\dots,\frac{x_d}{x_0}\Bigr)\Bigr\}\subseteq\mathbb{R}_+\times\mathbb{R}^d.
$$
Then $\boldsymbol{Y}=\bigl(\frac{X_1}{X_0},\dots,\frac{X_d}{X_0}\bigr)$ has density $f/Z$ on $\mathbb{R}^d$.

**Proof** Let $B=\{(y_0,y_1,\dots,y_d)\mid0<y_0<f(y_1,\dots,y_d)/Z\}$ and define $\varphi\colon\mathbb{R}_+\times\mathbb{R}^d\to\mathbb{R}_+\times\mathbb{R}^d$ by

$$
\varphi(x_0,x_1,\dots,x_d)=\Bigl(\frac{x_0^{d+1}}{Z(d+1)},\frac{x_1}{x_0},\dots,\frac{x_d}{x_0}\Bigr).
$$
Then $x\in A\iff\varphi(x)\in B$, so $\varphi$ maps $A$ bijectively onto $B$. The Jacobian matrix is lower triangular with diagonal $x_0^d/Z,1/x_0,\dots,1/x_0$, so $\det D\varphi(x)=1/Z$. The density of $X$ is $\boldsymbol{1}_A(x)/\lvert A\rvert$; by Theorem 8.4.1 the density of $\varphi(X)$ is $\frac{\boldsymbol{1}_A(\varphi^{-1}(y))}{\lvert A\rvert}\cdot Z=\frac{Z}{\lvert A\rvert}\boldsymbol{1}_B(y)$, uniform on $B$. By Theorem 8.3.4 applied to the density $f/Z$, the last $d$ coordinates $\boldsymbol{Y}$ of $\varphi(X)$ have density $f/Z$. $\square$

**Example 8.4.3** For the standard Cauchy density $f(x)=\frac1{\pi(1+x^2)}$ and $d=1$,

$$
A=\Bigl\{(x_0,x_1)\Bigm|x_0>0,\ \frac{x_0^2}{2}<\frac{1}{\pi(1+x_1^2/x_0^2)}\Bigr\}=\Bigl\{(x_0,x_1)\Bigm|x_0>0,\ x_0^2+x_1^2<\frac2\pi\Bigr\},
$$
a half-disk in the $(x_0,x_1)$-plane.

1. Generate $(X_0,X_1)$ uniformly on the half-disk $A$, for instance by rejection from the rectangle $(0,r)\times(-r,r)$, $r=\sqrt{2/\pi}$, with acceptance probability $\pi/4$.
2. Return $Y=X_1/X_0$.

Since only the ratio is returned, $A$ can be replaced by a half-disk of any radius. For the general Cauchy density $f(x;x_0,\gamma)=\dfrac{1}{\pi\gamma\bigl(1+((x-x_0)/\gamma)^2\bigr)}$, return $x_0+\gamma Y$.

### 8.4.5. Sums and Mixtures

Sums and mixtures are special types of transformations.

- A **convolution** is the distribution of a sum $S=X_1+\cdots+X_n$ of independent random variables. For an integer $\nu>0$, $\chi^2_\nu$ is the convolution of $\nu$ i.i.d. squared standard normal variables; the Pascal distribution $\mathrm{Pascal}(r,p)$ is the convolution of $r$ i.i.d. $\mathrm{Geo}(p)$ variables (subtracting $r$ gives the **negative binomial distribution** $\mathrm{NB}(r,p)$); the convolution of $r$ independent $\mathrm{Exp}(\lambda)$ variables is $\Gamma(r,\lambda)$. To simulate a convolution, generate $x_1\sim X_1,\dots,x_n\sim X_n$ and deliver $s=x_1+\cdots+x_n$.
- A *mixture distribution* has distribution function $F_X(x)=\sum_{i=1}^m\theta_iF_{X_i}(x)$ with $\theta_i>0$, $\sum_i\theta_i=1$. To simulate it, generate an integer $k\in\{1,\dots,m\}$ with $\mathbb{P}(k=i)=\theta_i$, then deliver $x\sim X_k$. Unlike a convolution, a mixture of two distinct normal distributions is distinctly non-normal, for example bimodal.

**Example 8.4.4** Simulate the mixture $F_X=\sum_{i=1}^5\theta_iF_{X_i}$ with $X_i\sim\Gamma(3,\lambda_i=1/i)$ independent and $\theta_i=i/15$:

```r
n <- 5000
k <- sample(1:5, size = n, replace = TRUE, prob = (1:5)/15)
rate <- 1/k
x <- rgamma(n, shape = 3, rate = rate)
# plot the density of the mixture with the densities of the components
plot(density(x), xlim = c(0, 40), ylim = c(0, .3), lwd = 3, xlab = "x", main = "", col = 2)
for (i in 1:5)
  lines(density(rgamma(n, 3, 1/i)))   # density() computes kernel density estimates
```

![A sample of 5000 values from the mixture of five gamma distributions Gamma(3, rate 1/i) with weights i/15, the mixture density and the five component densities.](./plots/gamma-mixture.py)

## Summary

| Method | Target | Key step | Efficiency and caveats |
|---|---|---|---|
| LCG $X_{i+1}\equiv aX_i+c\pmod m$ | $\mathrm{U}(0,1)$ | $R_i=X_i/m$ | period $\le m$ (Hull–Dobell for $m$); lattice structure in high dimensions |
| Mersenne Twister | $\mathrm{U}(0,1)$ | twisted 19937-bit state | period $2^{19937}-1$; default in R; not cryptographic |
| discrete inversion | any discrete distribution | $K=\min\{k\colon\sum_{i\le k}p_i\ge U\}$ | geometric: $\lceil\log(1-U)/\log(1-p)\rceil$ |
| inverse transform | one-dimensional, invertible $F$ | $x=F^{-1}(u)$ | fast, but needs $F^{-1}$; one dimension only |
| basic rejection | $f\propto pg$ | accept if $U\le p(X)$ | acceptance probability $Z$, mean $1/Z$ trials |
| envelope rejection | any $f\le cg$ (unnormalized) | accept if $U\le f(X)/(cg(X))$ | acceptance $Z_f/c$; choose $g$ close to $f$, $c$ small |
| conditioning | $P_{X\mid X\in A}$ | keep $X\in A$ | mean $1/\mathbb{P}(X\in A)$ trials; use an envelope for small $\mathbb{P}(A)$ |
| uniform under the graph | any density $f$ | $(X,f(X)U)$ uniform on $\{0\le y<f(x)\}$ | the geometry behind rejection |
| transformation | densities via Jacobians | $f_Y(y)=g(\varphi^{-1}(y))\lvert\det D\varphi^{-1}(y)\rvert$ | Box–Muller: $\sqrt{-2\log U}(\cos2\pi V,\sin2\pi V)$ |
| multivariate normal | $\mathcal{N}_d(\boldsymbol\mu,\Sigma)$ | $X=MC^{\mathsf T}+\boldsymbol1\boldsymbol\mu^{\mathsf T}$, $\Sigma=CC^{\mathsf T}$ | Cholesky is cheapest |
| ratio of uniforms | density $f/Z$ | $X$ uniform on $A$, return $X_1/X_0$ | Cauchy: half-disk |
| mixture, convolution | $\sum\theta_iF_i$; sums | pick component, then sample; add | — |
