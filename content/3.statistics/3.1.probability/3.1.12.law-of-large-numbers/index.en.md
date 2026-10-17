---
title: The Law of Large Numbers
source_hash: ab060845b5b6
---

Developing a vaccine requires a clinical trial: $n$ subjects are recruited at random, and we set $X_i = 1$ if the vaccine is effective for the $i$-th subject and $X_i = 0$ otherwise, where $X_1, X_2, \dots$ are i.i.d. with $\mathbb{P}(X_i = 1) = p$. We can only observe the proportion of effective cases in the trial, $\frac{1}{n}\sum_{i=1}^{n} X_i$ (the **sample mean**), whereas what we want to know is the proportion $p = \mathbb{E}X_1$ in the whole population (the population mean). Can the sample mean reliably estimate the population mean? The *law of large numbers* answers this question: under quite general conditions, the arithmetic mean of i.i.d. random variables converges to their expectation as $n \to \infty$. It is the mathematical form of "relative frequencies stabilize at probabilities", it links the randomness of a single trial with the regularity of many repetitions, and it is the theoretical basis of statistical inference ([3.2](/3.2)) and of stochastic simulation.

This chapter first introduces two modes of convergence that describe limits of sequences of random variables, then presents the weak and the strong law of large numbers, and finally discusses applications to relative frequencies, empirical distributions and the Monte Carlo method. It uses Chebyshev's inequality (Corollary 8.5.1) from [3.1.8](/3.1.8) and the limits of sequences of events from [3.1.2](/3.1.2); the relations among the various modes of convergence are discussed systematically in [3.1.14](/3.1.14).

## 12.1. Two Modes of Convergence

Convergence $a_n \to a$ of a sequence of numbers is a deterministic notion. A random variable $Y_n$ is a function of the sample point $\omega$, and "$Y_n \to Y$" can have different meanings depending on how the randomness is removed first. The two definitions below apply to general sequences of random variables, not only to the law of large numbers.

**Definition 12.1.1 (Convergence in Probability)** Let $Y_n, Y$ be random variables on the same probability space. If for every $\varepsilon > 0$

$$
\lim_{n \to \infty} \mathbb{P}(\lvert Y_n - Y \rvert \ge \varepsilon) = 0,
$$
we say that $Y_n$ converges to $Y$ in probability (**convergence in probability**), written $Y_n \xrightarrow{p} Y$.

Writing $A_n = \{\omega\colon \lvert Y_n(\omega) - Y(\omega) \rvert < \varepsilon\}$, we have $\mathbb{P}(\lvert Y_n - Y \rvert \ge \varepsilon) = \mathbb{P}(A_n^{\mathsf c}) = 1 - \mathbb{P}(A_n)$, so $Y_n \xrightarrow{p} Y$ is equivalent to $\lim_{n \to \infty} \mathbb{P}(A_n) = 1$ for every $\varepsilon > 0$.

**Definition 12.1.2 (Almost Sure Convergence)** If

$$
\mathbb{P}\left(\lim_{n \to \infty} Y_n = Y\right) = 1,
$$
we say that $Y_n$ converges to $Y$ almost surely (**almost sure convergence**), also called convergence with probability $1$ or almost everywhere, written $Y_n \xrightarrow{\text{a.s.}} Y$ or $Y_n \to Y$ a.s.

By the definition of the limit of a sequence, $\lim_n a_n = a$ if and only if for every $\varepsilon > 0$ there is an $n$ such that $\lvert a_k - a \rvert < \varepsilon$ for all $k \ge n$. Hence, for fixed $\varepsilon > 0$,

$$
\left\{\lim_{n \to \infty} Y_n = Y\right\} \subset \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} \{\lvert Y_k - Y \rvert < \varepsilon\} = \liminf_{n \to \infty} A_n,
$$
and the event on the left is the intersection of the right-hand side over all $\varepsilon = 1/m$ ($m = 1, 2, \dots$). Therefore $Y_n \xrightarrow{\text{a.s.}} Y$ implies $\mathbb{P}(\liminf_n A_n) = 1$ for every $\varepsilon > 0$.

The two modes of convergence remove randomness, turning the problem into one about sequences of numbers, in different ways:

- Convergence in probability first computes, for each fixed $n$, the probability $\mathbb{P}(A_n^{\mathsf c})$, which removes the randomness, and then asks whether this sequence of numbers tends to $0$. The limit is outermost: the probability of a deviation larger than $\varepsilon$ may never be $0$, as long as it tends to $0$.
- Almost sure convergence first fixes an outcome $\omega$, asks whether the sequence $Y_n(\omega)$ converges, and then requires that the set of outcomes for which it does not converge has probability $0$. The limit is innermost.

Draw $Y_1(\omega), Y_2(\omega), \dots$ as one curve for each $\omega$ (see the figure). Convergence in probability "looks vertically at cross-sections first": for a given $n$, the probability of the curves lying outside the $\varepsilon$-band tends to $0$ as $n$ grows. Almost sure convergence "looks horizontally along each curve first": almost every curve eventually enters and stays within any narrow band (different curves may enter at different times).

Since $\mathbb{P}(\liminf_n A_n) = \lim_{n} \mathbb{P}\left(\bigcap_{k \ge n} A_k\right) \le \liminf_{n} \mathbb{P}(A_n)$ (continuity of probability, Theorem 2.2.1), almost sure convergence implies convergence in probability; the converse fails, and a counterexample is given in [3.1.14](/3.1.14).

![Twenty sample paths of the sample mean M_n for tosses of a fair coin, together with the band p +- 0.03; each curve corresponds to one omega](./plots/sample-mean-paths.py)

## 12.2. The Weak Law of Large Numbers

**Theorem 12.2.1 (Weak Law of Large Numbers)** Let $\{X_n\}$ be a sequence of i.i.d. random variables with $\operatorname{Var}(X_1) < \infty$. Then for every $\varepsilon > 0$,

$$
\lim_{n \to \infty} \mathbb{P}\left(\left\lvert \frac{1}{n}\sum_{i=1}^{n} X_i - \mathbb{E}X_1 \right\rvert \ge \varepsilon\right) = 0,
$$
that is, $\dfrac{1}{n}\displaystyle\sum_{k=1}^{n} X_k \xrightarrow{p} \mathbb{E}X_1$.

**Proof** Let $M_n = \frac{1}{n}\sum_{i=1}^{n} X_i$. Since the $X_i$ are identically distributed, $\mathbb{E}M_n = \mathbb{E}X_1$; since they are i.i.d., $\operatorname{Var}(M_n) = \frac{1}{n^2} \cdot n\operatorname{Var}(X_1) = \frac{\operatorname{Var}(X_1)}{n}$. By Chebyshev's inequality (Corollary 8.5.1),

$$
\mathbb{P}(\lvert M_n - \mathbb{E}X_1 \rvert \ge \varepsilon) = \mathbb{P}(\lvert M_n - \mathbb{E}M_n \rvert \ge \varepsilon) \le \frac{\operatorname{Var}(M_n)}{\varepsilon^2} = \frac{\operatorname{Var}(X_1)}{n\varepsilon^2} \to 0, \quad n \to \infty. \quad \square
$$

The theorem says that for large $n$ we can assert with high confidence (but not with certainty) that $\frac{1}{n}\sum X_i$ is close to $\mathbb{E}X_1$. The proof also yields the quantitative bound $\frac{\operatorname{Var}(X_1)}{n\varepsilon^2}$, which can be used to choose the sample size.

**Example 12.2.1** Let $p$ be the proportion of the population for whom the vaccine is effective. Draw $n$ people at random and let $X_i$ indicate whether the vaccine is effective for the $i$-th person; the proportion of effective cases in the sample is $M_n = (X_1 + \cdots + X_n)/n$. The law of large numbers tells us that the population mean $p$ can be learned from the sample mean $M_n$. How large must the sample be to ensure that the probability of an error of at least 3% is at most 5%?

**Solution** We want $\mathbb{P}(\lvert M_n - p \rvert \ge 0.03) \le 0.05$. By the proof of Theorem 12.2.1 and $\operatorname{Var}(X_1) = p(1 - p) \le \frac{1}{4}$,

$$
\mathbb{P}(\lvert M_n - p \rvert \ge 0.03) \le \frac{\operatorname{Var}(X_1)}{n(0.03)^2} \le \frac{1}{4n(0.03)^2} \le 0.05,
$$
which gives $n \ge 5555.6$, so $n = 5556$ suffices. This estimate does not depend on the value of $p$ and needs no large-sample approximation, but it is rather conservative: the central limit theorem requires only about $1068$ people ([3.1.13](/3.1.13), Example 13.2.1).

## 12.3. Deeper Results

The hypotheses of Theorem 12.2.1 (i.i.d., finite variance) can be weakened, and its conclusion (convergence in probability) can be strengthened.

### 12.3.1. Weakening the Hypotheses

**Theorem 12.3.1 (Markov's Law of Large Numbers)** Let $\{X_n\}$ be a sequence of random variables with finite variances (neither independence nor identical distribution is required). If

$$
\frac{1}{n^2}\operatorname{Var}\left(\sum_{k=1}^{n} X_k\right) \to 0,
$$
then $\dfrac{1}{n}\displaystyle\sum_{k=1}^{n} (X_k - \mathbb{E}X_k) \xrightarrow{p} 0$.

The proof is identical to that of Theorem 12.2.1: apply Chebyshev's inequality to $\frac{1}{n}\sum_k (X_k - \mathbb{E}X_k)$. If $\{X_n\}$ are pairwise uncorrelated with uniformly bounded variances, the condition is automatically satisfied.

Dropping the assumption of finite variance and requiring only a finite first moment, the conclusion still holds.

**Theorem 12.3.2 (Khinchin's Law of Large Numbers)** Let $\{X_n\}$ be i.i.d. with $\mathbb{E}\lvert X_1 \rvert < \infty$. Then

$$
\frac{1}{n}\sum_{k=1}^{n} X_k \xrightarrow{p} \mathbb{E}X_1.
$$

Chebyshev's inequality is no longer applicable here, but the theorem can be proved with characteristic functions ([3.1.14](/3.1.14)). For i.i.d. sequences the most general form of the weak law is as follows (the proof is beyond the scope of this course).

**Theorem 12.3.3** Let $\{X_n\}$ be a sequence of i.i.d. random variables. There exists a sequence of real numbers $\{a_n\}$ such that

$$
\frac{1}{n}\sum_{k=1}^{n} X_k - a_n \xrightarrow{p} 0
$$
if and only if $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$. In this case one may take $a_n = \mathbb{E}(X_1\boldsymbol{1}_{\{\lvert X_1 \rvert < n\}})$.

The conditions are related by $\operatorname{Var}(X_1) < \infty \Rightarrow \mathbb{E}\lvert X_1 \rvert < \infty \Rightarrow n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$. For the second implication, $n\mathbb{P}(\lvert X_1 \rvert \ge n) \le \mathbb{E}(\lvert X_1 \rvert \boldsymbol{1}_{\{\lvert X_1 \rvert \ge n\}}) \to 0$ (dominated convergence). When $\mathbb{E}\lvert X_1 \rvert < \infty$ we have $a_n \to \mathbb{E}X_1$, and Theorem 12.3.3 reduces to Theorem 12.3.2; but when $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$ the expectation $\mathbb{E}X_1$ need not exist, and then the sample mean does not converge to an "expectation"; it only gets closer and closer to $a_n$.

### 12.3.2. Strengthening the Conclusion: The Strong Law of Large Numbers

**Theorem 12.3.4 (Strong Law of Large Numbers)** Let $\{X_n\}$ be a sequence of i.i.d. random variables.

1. If $\mathbb{E}\lvert X_1 \rvert < \infty$, then $\dfrac{1}{n}\displaystyle\sum_{k=1}^{n} X_k \xrightarrow{\text{a.s.}} \mathbb{E}X_1$.
2. Conversely, if $\dfrac{1}{n}\displaystyle\sum_{k=1}^{n} X_k \xrightarrow{\text{a.s.}} C$ for a finite constant $C$, then $\mathbb{E}\lvert X_1 \rvert < \infty$ and $C = \mathbb{E}X_1$.

That is, $\mathbb{P}\left(\lim_{n \to \infty} \frac{1}{n}\sum_{k=1}^{n} X_k = \mathbb{E}X_1\right) = 1$, and $\mathbb{E}\lvert X_1 \rvert < \infty$ is necessary and sufficient. (This is Kolmogorov's strong law of large numbers; its proof is beyond the scope of this course.)

**Example 12.3.1** In Example 12.2.1, the strong law tells us that as $n$ increases, the sample mean $M_n$ almost surely approaches the population mean $p$: for almost every sequence of trials, the proportion of effective cases eventually settles near $p$.

For i.i.d. sequences the weak and strong laws compare as follows:

| | Weak law | Strong law |
|---|---|---|
| Condition (necessary and sufficient) | $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$ | $\mathbb{E}\lvert X_1 \rvert < \infty$ |
| Conclusion | $\frac{1}{n}\sum X_k - a_n \xrightarrow{p} 0$ | $\frac{1}{n}\sum X_k \xrightarrow{\text{a.s.}} \mathbb{E}X_1$ |
| Intuition | The chance that the sample mean is close to the population mean keeps growing | With more and more samples, the sample mean almost surely approaches the population mean |

The conditions differ in strength, and so do the conclusions. When $\mathbb{E}\lvert X_1 \rvert < \infty$ both laws hold, and there is no contradiction: the strong law together with "almost sure convergence implies convergence in probability" gives $\frac{1}{n}\sum X_k \xrightarrow{p} \mathbb{E}X_1$, which Khinchin's law also gives directly. The two laws differ only when $\mathbb{E}\lvert X_1 \rvert = \infty$ but $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$, as in the next example.

**Example 12.3.2** Let $X, X_1, X_2, \dots$ be i.i.d. with

$$
\mathbb{P}(X = m) = \mathbb{P}(X = -m) = \frac{C}{2m^2 \ln m}, \quad m = 3, 4, \dots,
$$
where $C$ is a normalizing constant. Then $\bar X_n = \frac{1}{n}\sum_{k=1}^{n} X_k$ obeys the weak law of large numbers ($\bar X_n \xrightarrow{p} 0$) but not the strong law.

**Solution** For $n \ge 4$,

$$
\begin{aligned}
n\mathbb{P}(\lvert X \rvert \ge n) &= Cn\sum_{m=n}^{\infty} \frac{1}{m^2 \ln m} \le \frac{Cn}{\ln n}\sum_{m=n}^{\infty} \frac{1}{m^2} \le \frac{Cn}{\ln n}\sum_{m=n}^{\infty} \frac{1}{m(m-1)} \\
&= \frac{Cn}{\ln n}\sum_{m=n}^{\infty}\left(\frac{1}{m-1} - \frac{1}{m}\right) = \frac{C}{\ln n} \cdot \frac{n}{n-1} \to 0,
\end{aligned}
$$
so Theorem 12.3.3 gives $\bar X_n - a_n \xrightarrow{p} 0$, and by symmetry $a_n = \mathbb{E}(X\boldsymbol{1}_{\{\lvert X \rvert < n\}}) = 0$, that is, $\bar X_n \xrightarrow{p} 0$. On the other hand,

$$
\mathbb{E}X^+ = \mathbb{E}X^- = \sum_{m=3}^{\infty} m \cdot \frac{C}{2m^2 \ln m} = \frac{C}{2}\sum_{m=3}^{\infty} \frac{1}{m \ln m} = \infty,
$$
so $\mathbb{E}\lvert X \rvert = \infty$, and by item 2 of Theorem 12.3.4, $\bar X_n$ does not converge almost surely to any finite constant.

At the other extreme is the Cauchy distribution: $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to \frac{2}{\pi} \ne 0$, so even the weak law fails. In fact, by characteristic functions (Example 11.3.7), $\bar X_n$ has characteristic function $[\mathrm{e}^{-\lvert t \rvert/n}]^n = \mathrm{e}^{-\lvert t \rvert}$, so $\bar X_n$ has the same distribution as $X_1$ and does not concentrate no matter how large $n$ is.

![Running means of standard normal and standard Cauchy samples: the former settles at 0, the latter keeps making large jumps and never converges](./plots/cauchy-vs-normal-means.py)

## 12.4. Classical Applications

### 12.4.1. Relative Frequency and Probability

How can we determine the probability that a biased coin lands heads? Let $X_n \sim \mathrm{Ber}(p)$ indicate whether the event occurs in the $n$-th trial; this special case of the law of large numbers is called Bernoulli's law of large numbers:

$$
\frac{1}{n}\sum_{k=1}^{n} X_k \xrightarrow{p} p \quad \text{(also almost surely, by the strong law)}.
$$
The law of large numbers shows that relative frequencies stabilize at probabilities. This justifies determining probabilities by relative frequencies and is the foundation of the frequentist school of statistics.

### 12.4.2. The Empirical Distribution

**Example 12.4.1** Let $\{X_j\}$ be an i.i.d. sequence on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with distribution function $F(x)$, and let $x_j = X_j(\omega)$ denote the observed values in one realization. Then, with probability $1$, the observed sequence $\{x_j\}$ determines $F(x)$.

**Proof** For any fixed $x \in \mathbb{R}$, let $g(X_j) = \boldsymbol{1}_{\{X_j \le x\}}$. Then $\{g(X_j)\}$ is i.i.d. with $\mathbb{E}g(X_1) = \mathbb{P}(X_1 \le x) = F(x)$. By the strong law of large numbers,

$$
F_n(x) := \frac{1}{n}\sum_{j=1}^{n} \boldsymbol{1}_{\{X_j \le x\}} \xrightarrow{\text{a.s.}} F(x),
$$
that is, with probability $1$, $\lim_n \frac{1}{n}\sum_{j=1}^{n} \boldsymbol{1}_{\{x_j \le x\}} = F(x)$. $\square$

$F_n(x)$ is the **empirical distribution function** of [3.2](/3.2). We have only proved almost sure convergence for each fixed $x$; the stronger **Glivenko–Cantelli theorem** asserts that $\sup_x \lvert F_n(x) - F(x) \rvert \xrightarrow{\text{a.s.}} 0$.

### 12.4.3. The Monte Carlo Method

The *Monte Carlo method*, also called stochastic simulation, was introduced by von Neumann, Ulam and others in the 1940s while developing nuclear weapons: express the quantity to be computed as the expectation of some random variable, and approximate it by the sample mean of a large number of independent simulations. By the strong law of large numbers the approximation converges with probability $1$; by the central limit theorem the error is of order $1/\sqrt{n}$, independently of the dimension of the problem. It is a cornerstone of statistical computing and is especially suited to problems that are hard or impossible to solve analytically.

**Example 12.4.2 (Computing $\pi$)** Throw points $(U_j, V_j)$ independently and uniformly into the square $[-1, 1]^2$ and let $I_j = \boldsymbol{1}_{\{U_j^2 + V_j^2 \le 1\}}$. Then $\mathbb{E}I_j = \mathbb{P}(I_j = 1) = \frac{\pi}{4}$, and by the strong law of large numbers, $\hat\pi_n = 4 \cdot \frac{1}{n}\sum_{j=1}^{n} I_j \xrightarrow{\text{a.s.}} \pi$.

**Example 12.4.3 (Hit-or-Miss Integration)** Let $0 \le f(x) \le c$ for $a \le x \le b$; we want to estimate $\int_a^b f(x)\,\mathrm{d}x$. Throw $n$ points $(X_j, Y_j)$ independently and uniformly into the rectangle $A = [a, b] \times [0, c]$, and let $I_j$ indicate whether the $j$-th point falls into the region $B = \{(x, y)\colon 0 \le y \le f(x)\}$ under the curve. Then, with probability $1$,

$$
\frac{1}{n}\sum_{j=1}^{n} I_j \to \mathbb{E}I_j = \mathbb{P}(I_j = 1) = \frac{\int_a^b f(x)\,\mathrm{d}x}{c(b - a)}, \qquad \text{hence} \quad \int_a^b f(x)\,\mathrm{d}x \approx c(b - a)\frac{1}{n}\sum_{j=1}^{n} I_j.
$$

![Monte Carlo estimation of pi: on the left, 2000 random points; on the right, the estimate 4 * (fraction inside the circle) as a function of the number of points n](./plots/monte-carlo-pi.py)

The idea of the law of large numbers appears in many other places. In random forests in machine learning, the law of large numbers guarantees that as the number of trees grows, the generalization error converges to a constant rather than growing without bound, so adding trees does not cause overfitting. In stochastic processes, the ergodic theorem states that under suitable conditions the time average along a single trajectory converges to the space average over the state space; it extends the law of large numbers to dependent sequences.

## Summary

- Convergence in probability $Y_n \xrightarrow{p} Y$: $\mathbb{P}(\lvert Y_n - Y \rvert \ge \varepsilon) \to 0$ for all $\varepsilon > 0$; almost sure convergence $Y_n \xrightarrow{\text{a.s.}} Y$: $\mathbb{P}(\lim Y_n = Y) = 1$. The latter implies the former.
- Weak law of large numbers (Theorem 12.2.1): i.i.d. with finite variance $\Rightarrow$ $\frac{1}{n}\sum X_k \xrightarrow{p} \mathbb{E}X_1$. The proof rests on $\operatorname{Var}(M_n) = \operatorname{Var}(X_1)/n$ and Chebyshev's inequality, and it also gives a conservative estimate of the sample size.
- Extensions: Markov's law drops the i.i.d. assumption, Khinchin's law requires only $\mathbb{E}\lvert X_1 \rvert < \infty$; for i.i.d. sequences the weak law holds if and only if $n\mathbb{P}(\lvert X_1 \rvert \ge n) \to 0$.
- Strong law of large numbers (Theorem 12.3.4): for i.i.d. sequences, $\frac{1}{n}\sum X_k \xrightarrow{\text{a.s.}} \mathbb{E}X_1$ if and only if $\mathbb{E}\lvert X_1 \rvert < \infty$.
- Applications: learning the population mean from the sample mean (estimating probabilities by relative frequencies, the empirical distribution function, the Monte Carlo method); sample-size calculations (the law of large numbers combined with Chebyshev's inequality). Statistics "learns the unknown (the population mean) from the known (the sample mean)", probability theory shows how "law (necessity) governs phenomena (chance)", and the law of large numbers is the bridge between the two.
