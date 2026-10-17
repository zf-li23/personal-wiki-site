---
title: The Central Limit Theorem
source_hash: db8f40c1275a
---

The **law of large numbers** ([3.1.12](/3.1.12)) states that the sample mean $M_n = (X_1 + \cdots + X_n)/n$ converges to the population mean $\mu$, but it says nothing about how fast it converges or how the error $M_n - \mu$ is distributed. Simulation shows that the speed depends on the spread of the distribution: a variable taking the values $\pm 10$ converges much more slowly than one taking the values $\pm 1$; yet once the error is magnified by $\sqrt{n}$ and divided by the standard deviation, the distribution of $\sqrt{n}\,(M_n - \mu)/\sigma$ settles down. To what does it settle? The central limit theorem gives the answer: whatever the original distribution, as long as its variance is finite, the standardized sum exhibits **convergence in distribution** to the standard normal distribution. This explains why the normal distribution is so ubiquitous in nature and in statistics (the superposition of many independent random effects is approximately normal), and it provides a single tool for determining sample sizes, approximating probabilities and constructing confidence intervals.

The proofs in this chapter rely on the **characteristic function** of [3.1.11](/3.1.11) and the continuity theorem (Theorem 11.3.6). The relations among the various modes of convergence are discussed in [3.1.14](/3.1.14), and the central limit theorem for random vectors in [3.1.15](/3.1.15).

## 13.1. The Basic Theorem

Recall convergence in distribution (Definition 11.3.3): if $Y_n$ and $Y$ have distribution functions $F_n(x)$ and $F(x)$, then $Y_n \xrightarrow{d} Y$ means that $\lim_{n \to \infty} F_n(x) = F(x)$ at every continuity point $x$ of $F(x)$. When the limit is the standard normal distribution, $\Phi$ is continuous everywhere, and convergence in distribution simply means $\mathbb{P}(Y_n \le x) \to \Phi(x)$ for all $x$.

**Theorem 13.1.1 (Central Limit Theorem)** Let $\{X_n\}$ be a sequence of independent and identically distributed random variables with mean $\mu$ and variance $0 < \sigma^2 < \infty$, and let $S_n = X_1 + \cdots + X_n$. Then

$$
\frac{S_n - \mathbb{E}(S_n)}{\sqrt{\operatorname{Var}(S_n)}} = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1).
$$

This theorem is also called the Lindeberg–Lévy central limit theorem. In terms of the sample mean $M_n = S_n/n$, it reads equivalently

$$
\frac{M_n - \mathbb{E}(M_n)}{\sqrt{\operatorname{Var}(M_n)}} = \frac{\sqrt{n}\,(M_n - \mu)}{\sigma} \xrightarrow{d} \mathcal{N}(0, 1).
$$
Hence, for large $n$, it supplies the approximate distributions

$$
S_n \overset{\cdot}{\sim} \mathcal{N}(n\mu, n\sigma^2), \qquad M_n \overset{\cdot}{\sim} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right).
$$
The first is often used to explain phenomena (the superposition of many iid random effects is approximately normal); the second is the foundation of statistical inference ([3.2](/3.2)). Note that $S_n$ itself does not converge: "approximately distributed as" is only a restatement, for fixed $n$, of the limit statement about the standardized quantity.

**Proof** Let $Y_k = (X_k - \mu)/\sigma$. Then the $Y_k$ are iid with $\mathbb{E}Y_k = 0$ and $\operatorname{Var}(Y_k) = 1$, and

$$
\frac{S_n - \mathbb{E}(S_n)}{\sqrt{\operatorname{Var}(S_n)}} = \frac{1}{\sqrt{n}}\sum_{k=1}^{n} \frac{X_k - \mu}{\sigma} = \frac{1}{\sqrt{n}}\sum_{k=1}^{n} Y_k.
$$
Computing $\mathbb{P}\left(\frac{1}{\sqrt{n}}\sum Y_k \le x\right)$ directly would require an $n$-fold convolution, which is hardly feasible; we use characteristic functions instead. Let $\varphi(t) = \mathbb{E}\mathrm{e}^{\mathrm{i}tY_1}$. By Property 11.3.1, $\varphi'(0) = \mathrm{i}\,\mathbb{E}Y_1 = 0$ and $\varphi''(0) = \mathrm{i}^2\mathbb{E}Y_1^2 = -1$, so by Eq. (11.1),

$$
\varphi(t) = \varphi(0) + \varphi'(0)t + \frac{1}{2}\varphi''(0)t^2 + o(t^2) = 1 - \frac{t^2}{2} + o(t^2), \quad t \to 0.
$$
Since the $Y_k$ are iid, the characteristic function of $\frac{1}{\sqrt{n}}\sum_{k=1}^{n} Y_k$ is

$$
\varphi_n(t) = \mathbb{E}\exp\left(\mathrm{i}t\,\frac{Y_1 + \cdots + Y_n}{\sqrt{n}}\right) = \left[\varphi\left(\frac{t}{\sqrt{n}}\right)\right]^n = \left(1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right)\right)^n \to \mathrm{e}^{-t^2/2}, \quad n \to \infty,
$$
where, for fixed $t$, $t/\sqrt{n} \to 0$; the limit is of the form "$1^\infty$" and we use $(1 + a_n/n)^n \to \mathrm{e}^a$ whenever $a_n \to a$ (which also holds for complex $a_n$). Since $\mathrm{e}^{-t^2/2}$ is the characteristic function of $\mathcal{N}(0, 1)$ (Example 11.3.6), the continuity theorem (Theorem 11.3.6) gives the result. $\square$

Standardizing "without loss of generality" to mean $0$ and variance $1$, as in the proof, simplifies the computation considerably. The same method proves Khinchin's law of large numbers: as long as $\mathbb{E}\lvert X_1 \rvert < \infty$, we have $\varphi_{X_1}(t) = 1 + \mathrm{i}\mu t + o(t)$, so the characteristic function of $M_n$ is $[\varphi_{X_1}(t/n)]^n \to \mathrm{e}^{\mathrm{i}\mu t}$, that is, $M_n \xrightarrow{d} \mu$; and convergence in distribution to a constant is equivalent to convergence in probability ([3.1.14](/3.1.14)).

![Exact densities of the standardized sums (S_n - n)/sqrt(n) for Exp(1) (n = 1, 2, 5, 30) approaching the standard normal density](./plots/clt-exponential.py)

## 13.2. Applications

Every application of the central limit theorem rests on the approximation

$$
\mathbb{P}\left(c_1 \le \frac{\sqrt{n}}{\sigma}\left(\frac{S_n}{n} - \mu\right) \le c_2\right) \approx \Phi(c_2) - \Phi(c_1) = \alpha.
$$
Of the three quantities $n$, $c$ (the endpoints) and $\alpha$ (the probability), any two determine the third: given $c$ and $\alpha$, find $n$ (the sample size); given $n$ and $\alpha$, find $c$ (the quantiles); given $n$ and $c$, find $\alpha$ (an approximate probability).

**Example 13.2.1 (Sample Size)** Suppose a vaccine is effective for a proportion $\mu$ of the population. We sample $n$ people at random, and $X_i$ indicates whether the vaccine is effective for the $i$-th person. How large must the sample be to guarantee, with probability 95%, that the proportion $M_n = (X_1 + \cdots + X_n)/n$ of effective cases in the sample differs from $\mu$ by less than 3%?

**Solution** We seek $n$ with $\mathbb{P}(\lvert M_n - \mu \rvert < 0.03) \ge 0.95$. Let $\sigma = \sqrt{\operatorname{Var}(X_1)} = \sqrt{\mu(1 - \mu)} \le \frac{1}{2}$ and $Z \sim \mathcal{N}(0, 1)$. Then

$$
\mathbb{P}(\lvert M_n - \mu \rvert < 0.03) = \mathbb{P}\left(\left\lvert \frac{M_n - \mu}{\sigma/\sqrt{n}} \right\rvert < \frac{0.03\sqrt{n}}{\sigma}\right) \approx \mathbb{P}\left(\lvert Z \rvert < \frac{0.03\sqrt{n}}{\sigma}\right) \ge \mathbb{P}(\lvert Z \rvert < 0.06\sqrt{n}).
$$
Setting $\mathbb{P}(\lvert Z \rvert < 0.06\sqrt{n}) = 0.95$, that is, $0.06\sqrt{n} = z_{0.025} = 1.96$, gives $n = (1.96/0.06)^2 \approx 1067.1$, so $n = 1068$ suffices.

The same problem solved with Chebyshev's inequality (Example 12.2.1) requires $5556$ people. The two methods have the same goal: the Chebyshev bound holds exactly for every $n$ but is very conservative, while the central limit theorem gives a large-sample approximation that is more accurate when it applies. In practice, unless the sample is quite small, the central limit theorem is preferred.

**Example 13.2.2 (Theoretical Approximation)** Sometimes the distribution of a partial sum is complicated to compute or has no simple closed form. Let $\{X_n\}$ be iid $\mathrm{U}(-1, 1)$. The density of $S_n = X_1 + \cdots + X_n$ is

$$
f_{S_n}(x) = \begin{cases} \dfrac{1}{2^n (n-1)!}\displaystyle\sum_{k=0}^{\lfloor (n+x)/2 \rfloor} (-1)^k \binom{n}{k}(n + x - 2k)^{n-1}, & \lvert x \rvert \le n, \\ 0, & \lvert x \rvert > n. \end{cases}
$$
Since $\mu = 0$ and $\sigma^2 = \frac{1}{3}$, the central limit theorem gives $S_n \overset{\cdot}{\sim} \mathcal{N}\left(0, \frac{n}{3}\right)$, and for $n = 10$ the two curves are already almost indistinguishable. The approximation simplifies computations enormously.

![Exact density of the sum S_n of independent U(-1, 1) variables (solid) and the normal approximation N(0, n/3) (dashed), n = 2, 4, 10](./plots/uniform-sum-density.py)

**Example 13.2.3** Poincaré is said to have always bought his bread at the same bakery. The baker claimed that each loaf weighed 1000 g on average, give or take 50 g. Poincaré weighed every loaf he bought over a year and found that the average always lay between 940 g and 960 g. If the baker's claim were true, then $\mu = 1000$, $\sigma = 50$ and $M_n \overset{\cdot}{\sim} \mathcal{N}(1000, 50^2/n)$; for $n = 30$,

$$
\mathbb{P}(940 \le M_n \le 960) = \mathbb{P}\left(\frac{940 - 1000}{50/\sqrt{n}} \le \frac{M_n - 1000}{50/\sqrt{n}} \le \frac{960 - 1000}{50/\sqrt{n}}\right) \approx \Phi(-4.38) - \Phi(-6.57) \approx 6 \times 10^{-6}.
$$
An event of such small probability did occur, so the baker's claim is not credible, and Poincaré complained to the bakery. He kept weighing afterwards and found that the weights now had almost no mass below 950 g but a long right tail, like a bell curve with its left half cut off: the baker was still making light loaves and simply handed the heavier ones to him. Bread weight is affected by many factors (the amounts of flour, water and yeast, the temperature, and so on) and by the central limit theorem should be approximately normal, so the abnormal shape of the distribution is itself evidence of cheating.

## 13.3. Theoretical Extensions

If the $X_k$ are independent but not identically distributed, is the sum still approximately normal? The answer is yes, provided that no single term dominates.

**Theorem 13.3.1 (Lindeberg–Feller Central Limit Theorem)** Let $\{X_n\}$ be a sequence of independent random variables with finite variances $\sigma_k^2 = \operatorname{Var}(X_k)$ such that

$$
B_n^2 = \sum_{k=1}^{n} \sigma_k^2 \to \infty, \qquad \max_{1 \le k \le n} \frac{\sigma_k^2}{B_n^2} \to 0. \tag{13.1}
$$
Then the central limit theorem

$$
\frac{1}{B_n}\sum_{k=1}^{n} (X_k - \mathbb{E}X_k) \xrightarrow{d} \mathcal{N}(0, 1)
$$
holds if and only if the *Lindeberg condition* holds: for every $\varepsilon > 0$,

$$
\lim_{n \to \infty} \frac{1}{B_n^2}\sum_{k=1}^{n} \mathbb{E}\left[(X_k - \mathbb{E}X_k)^2\boldsymbol{1}_{\{\lvert X_k - \mathbb{E}X_k \rvert > \varepsilon B_n\}}\right] = 0.
$$

The second condition in Eq. (13.1) is called the Feller condition; it says that the share of each term's variance in the total variance tends to $0$, and when $B_n \to \infty$ it is equivalent to $\sigma_n^2/B_n^2 \to 0$. The Lindeberg condition implies the Feller condition, since $\sigma_k^2 \le \varepsilon^2 B_n^2 + \mathbb{E}[(X_k - \mathbb{E}X_k)^2\boldsymbol{1}_{\{\lvert X_k - \mathbb{E}X_k \rvert > \varepsilon B_n\}}]$. In the iid case with finite variance, the sum in the Lindeberg condition equals $\frac{1}{\sigma^2}\mathbb{E}[(X_1 - \mu)^2\boldsymbol{1}_{\{\lvert X_1 - \mu \rvert > \varepsilon\sigma\sqrt{n}\}}] \to 0$ (by dominated convergence), so Theorem 13.1.1 is a special case of Theorem 13.3.1. The Lindeberg condition is not easy to verify directly; in practice one uses the following condition, which is stronger but easier to check.

**Corollary 13.3.1 (Lyapunov Central Limit Theorem)** Let $\{X_n\}$ be independent and $B_n^2 = \sum_{k=1}^{n}\operatorname{Var}(X_k)$. If for some $\delta > 0$ the *Lyapunov condition*

$$
\lim_{n \to \infty} \frac{1}{B_n^{2+\delta}}\sum_{k=1}^{n} \mathbb{E}\lvert X_k - \mathbb{E}X_k \rvert^{2+\delta} = 0
$$
holds, then $\frac{1}{B_n}\sum_{k=1}^{n}(X_k - \mathbb{E}X_k) \xrightarrow{d} \mathcal{N}(0, 1)$.

**Proof** On $\{\lvert X_k - \mathbb{E}X_k \rvert > \varepsilon B_n\}$ we have $(X_k - \mathbb{E}X_k)^2 \le \lvert X_k - \mathbb{E}X_k \rvert^{2+\delta}/(\varepsilon B_n)^\delta$, so the sum in the Lindeberg condition is at most $\frac{1}{\varepsilon^\delta B_n^{2+\delta}}\sum_k \mathbb{E}\lvert X_k - \mathbb{E}X_k \rvert^{2+\delta} \to 0$. The conclusion follows from the sufficiency part of Theorem 13.3.1 (which does not need Eq. (13.1)). $\square$

The meaning of these theorems is that the superposition of a large number of "small", mutually independent random effects is approximately normal. Gauss introduced the normal distribution to describe the distribution of observational errors; engineers routinely model noise as Gaussian white noise; the weights of products of the same model and batch are approximately normal. The normal distribution may fairly be called one of the laws of nature.

## 13.4. Finer Points

### 13.4.1. Correction for Discrete Random Variables

Let $X_i \overset{\text{iid}}{\sim} \mathrm{Ber}(p)$ and $S_n = X_1 + \cdots + X_n \sim \mathrm{Bin}(n, p)$, say with $n = 36$ and $p = 0.5$. A normal approximation runs into two problems:

- $\mathbb{P}(S_n \le 21) = \mathbb{P}(S_n < 22)$: should $21$ or $22$ be plugged into the normal distribution function? The two give different answers.
- Point probabilities: a continuous distribution assigns probability $0$ to every point, so a naive approximation gives $\mathbb{P}(S_n = 19) \approx 0$, which is clearly wrong.

The remedy is to regard each value $k$ of the discrete variable as a rectangle over the interval $[k - 0.5, k + 0.5]$ and to approximate $\mathbb{P}(S_n = k)$ by the area under the normal density curve over that interval.

**Theorem 13.4.1 (de Moivre–Laplace Theorem)** Let $S_n \sim \mathrm{Bin}(n, p)$ with $n$ large, and let $k \le m$ be nonnegative integers. Then

$$
\mathbb{P}(k \le S_n \le m) \approx \Phi\left(\frac{m - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{k - np}{\sqrt{np(1-p)}}\right).
$$
The corrected form, which is more accurate, is

$$
\mathbb{P}(k \le S_n \le m) \approx \Phi\left(\frac{m + 0.5 - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right).
$$
More importantly, the corrected form can compute point probabilities $\mathbb{P}(S_n = k)$ (take $m = k$).

This is the special case $X_i \sim \mathrm{Ber}(p)$ of Theorem 13.1.1. It was obtained by de Moivre (1733, for $p = \frac{1}{2}$) and Laplace (1812, for general $p$) and is historically the first central limit theorem. Adding and subtracting $0.5$ at the endpoints is called the *continuity correction*, and it applies equally to other integer-valued random variables. For interval probabilities the correction only affects accuracy; for point probabilities it is indispensable.

**Example 13.4.1** Let $S_n \sim \mathrm{Bin}(36, 0.5)$. Find $\mathbb{P}(S_n \le 21)$.

**Solution** The exact value is $\mathbb{P}(S_n \le 21) = \sum_{k=0}^{21}\binom{36}{k}0.5^{36} = 0.8785$. Here $np = 18$ and $\sqrt{np(1-p)} = 3$. Without correction,

$$
\mathbb{P}(S_n \le 21) \approx \Phi\left(\frac{21 - 18}{3}\right) = \Phi(1) = 0.8413;
$$
with the correction,

$$
\mathbb{P}(S_n \le 21) \approx \Phi\left(\frac{21.5 - 18}{3}\right) = \Phi(1.167) = 0.8783,
$$
which agrees almost perfectly with the exact value. Similarly, the point probability is $\mathbb{P}(S_n = 19) = 0.1251$, and the corrected normal approximation is $\Phi\left(\frac{19.5 - 18}{3}\right) - \Phi\left(\frac{18.5 - 18}{3}\right) = 0.1253$.

![PMF of Bin(36, 0.5) and its normal approximation: the continuity correction approximates P(S_n = k) by the area under the normal density over [k - 0.5, k + 0.5]](./plots/continuity-correction.py)

**Example 13.4.2** A district has one small cinema, and a larger one is planned. Analysis suggests that about $n = 1600$ people go to the cinema in the district each day, and that after the new cinema opens about $3/4$ of them will go there. In planning the number of seats, the cinema wants as many seats as possible, subject to the probability that "200 or more seats are empty" being at most 10%. How many seats should it have?

**Solution** Number the daily moviegoers $1, 2, \dots, 1600$ and let $X_i = 1$ if the $i$-th moviegoer goes to the new cinema and $X_i = 0$ otherwise, so that $\mathbb{P}(X_i = 1) = 3/4$. Assuming that the moviegoers decide independently, $X_1, \dots, X_{1600}$ are independent. With $m$ seats we require

$$
\mathbb{P}(X_1 + \cdots + X_{1600} \le m - 200) \le 0.1,
$$
and to make $m$ as large as possible we take equality. Since $np = 1200$ and $\sqrt{np(1-p)} = 10\sqrt{3}$, the corrected approximation requires

$$
\Phi\left(\frac{m - 200 + 0.5 - 1200}{10\sqrt{3}}\right) = 0.1.
$$
Since $\Phi(x) = 0.1$ at $x = -1.2816$, the equation $\frac{m - 1399.5}{10\sqrt{3}} = -1.2816$ gives $m = 1377.3$, so we take $m = 1377$.

### 13.4.2. Conditions of Applicability

The normal approximation becomes more and more accurate as $n \to \infty$, but in practice the sample size $n$ is fixed and finite, and we need to know how large $n$ must be for the approximation to be trustworthy. Unfortunately there is no simple universal rule: it depends on how close the distribution of $X_i$ is to normal, and in particular on whether it is symmetric. For instance, for $X_i \sim \mathrm{U}(-1, 1)$, $n = 10$ is already very good (Example 13.2.2), whereas the skewed $X_i \sim \mathrm{Exp}(\lambda)$ needs a much larger $n$. Moreover, the accuracy of the approximation of $\mathbb{P}(S_n \le c)$ depends on $c$: in general it is better when $c$ is near the mean of $S_n$, and the relative error is larger in the tails.

A quantitative description of the rate of convergence is the Berry–Esseen theorem.

**Theorem 13.4.2 (Berry–Esseen Theorem)** Let $X_1, X_2, \dots$ be iid with $\mathbb{E}X_1 = 0$, $\operatorname{Var}(X_1) = 1$ and $\mathbb{E}\lvert X_1 \rvert^3 < \infty$, let $W_n = (X_1 + \cdots + X_n)/\sqrt{n}$ and $Z \sim \mathcal{N}(0, 1)$. Then

$$
\sup_{x \in \mathbb{R}}\lvert \mathbb{P}(W_n \le x) - \mathbb{P}(Z \le x) \rvert \le \frac{C\,\mathbb{E}\lvert X_1 \rvert^3}{\sqrt{n}},
$$
where $C$ is a constant independent of the distribution (it is known that one may take $C = 0.4748$).

Thus the error is of order $1/\sqrt{n}$, and the larger the third absolute moment (the more skewed or heavy-tailed the distribution), the slower the convergence. The central limit theorem describes the rate of convergence in the law of large numbers, namely that $M_n - \mu$ is of order $\sigma/\sqrt{n}$; the Berry–Esseen theorem in turn describes the rate of convergence in the central limit theorem itself.

The binomial distribution has two approximations, each with its own range of validity.

| | Poisson approximation | Normal approximation |
|---|---|---|
| Condition | $n$ large, $p$ small, $np = \lambda$ moderate | $np(1-p)$ large |
| Conclusion | $\mathrm{Bin}(n, p) \approx \mathrm{Poi}(np)$ | $\mathrm{Bin}(n, p) \approx \mathcal{N}(np, np(1-p))$ |
| Example | $p = 1/100$, $n = 100$ | $\mathrm{Bin}(1600, 0.5)$; $p = 1/10$, $n = 500$ |

When $np$ is fixed and large, both approximations apply, and there is no contradiction: $\mathrm{Poi}(\lambda)$ is the sum of $\lambda$ independent $\mathrm{Poi}(1)$ variables (for integer $\lambda$), so by the central limit theorem $\mathrm{Poi}(\lambda) \approx \mathcal{N}(\lambda, \lambda)$ for large $\lambda$.

**Example 13.4.3 (Stirling's Formula)** The central limit theorem also has theoretical applications. Let $X_1, X_2, \dots$ be iid $\mathrm{Poi}(1)$ and $S_n = \sum_{i=1}^{n} X_i \sim \mathrm{Poi}(n)$, so that $\mathbb{P}(S_n = n) = \mathrm{e}^{-n}\frac{n^n}{n!}$. On the other hand, $\mathbb{E}S_n = \operatorname{Var}(S_n) = n$, and the corrected normal approximation gives

$$
\mathbb{P}(S_n = n) = \mathbb{P}(n - 0.5 < S_n \le n + 0.5) \approx \Phi\left(\frac{0.5}{\sqrt{n}}\right) - \Phi\left(-\frac{0.5}{\sqrt{n}}\right) \approx \frac{1}{\sqrt{2\pi}} \cdot \frac{1}{\sqrt{n}}.
$$
Equating the two expressions yields Stirling's formula $n! \approx \sqrt{2\pi n}\,(n/\mathrm{e})^n$. (The argument is heuristic: a rigorous proof requires a local limit theorem, which guarantees that the relative error of point probabilities tends to $0$.)

**Example 13.4.4** Let $X_1, X_2, \dots$ be independent standard Cauchy random variables and $M_n = (X_1 + \cdots + X_n)/n$. What is the distribution of $M_n$?

**Solution** By Example 11.3.7, the characteristic function of $M_n$ is $[\mathrm{e}^{-\lvert t/n \rvert}]^n = \mathrm{e}^{-\lvert t \rvert}$, so for every $n$, $M_n$ is again standard Cauchy: it neither concentrates nor becomes approximately normal.

Here the central limit theorem (and the law of large numbers) fails, because the theorem requires a finite variance, whereas the Cauchy distribution does not even have a mean. Is the finite-variance condition necessary? For an iid sequence, if there are constants $a_n$ such that $(S_n - a_n)/\sqrt{n}$ converges in distribution to a nondegenerate normal distribution, then $\mathbb{E}X_1^2 < \infty$; so under the $\sqrt{n}$ normalization the condition is necessary. With other normalizing constants, some distributions with infinite variance (for example, those whose density behaves like $\lvert x \rvert^{-3}$ in the tails) can still be approximately normal, while distributions with even heavier tails, such as the Cauchy, have other stable distributions as limits.

## Summary

- Central limit theorem (Theorem 13.1.1): for iid variables with variance $0 < \sigma^2 < \infty$, $\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$, that is, $S_n \overset{\cdot}{\sim} \mathcal{N}(n\mu, n\sigma^2)$ and $M_n \overset{\cdot}{\sim} \mathcal{N}(\mu, \sigma^2/n)$. Proof: standardize, expand the characteristic function to second order, use $(1 - \frac{t^2}{2n} + o(\frac{1}{n}))^n \to \mathrm{e}^{-t^2/2}$, and apply the continuity theorem.
- Relation between the law of large numbers and the central limit theorem: the former says $M_n \to \mu$; the latter says that the deviation $M_n - \mu$ is of order $\sigma/\sqrt{n}$ and approximately normal.
- Applications: from $\mathbb{P}(c_1 \le \frac{\sqrt{n}}{\sigma}(M_n - \mu) \le c_2) \approx \Phi(c_2) - \Phi(c_1)$, any two of the three quantities determine the third (sample size, quantiles, probability).
- Independent, non-identically distributed summands: the Lindeberg–Feller theorem (the Lindeberg condition: no dominant term), with the Lyapunov condition as a convenient sufficient condition.
- For discrete random variables use the continuity correction (endpoints $\pm 0.5$); for point probabilities the correction is mandatory. The accuracy depends on the symmetry and tails of the distribution, with error of order $1/\sqrt{n}$ (Berry–Esseen); with infinite variance (e.g., the Cauchy distribution) the theorem fails.
- Limits of characteristic functions (or of moment generating functions or probability generating functions) identify the limiting distribution of a sequence of random variables.
