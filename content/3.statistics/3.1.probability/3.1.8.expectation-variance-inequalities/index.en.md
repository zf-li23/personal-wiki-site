---
title: Expectation, Variance and Inequalities
source_hash: 561dc46634f1
---

A distribution describes a random variable completely, but many problems call for summarizing it by one or two numbers: when comparing two investment products, people look first at the "average return" and the "risk"; when a game is interrupted and the stakes must be divided, we need to know how much each player "can expect to win". This chapter introduces the two most important numerical characteristics: the expectation, which describes the center of a distribution, and the variance, which describes how concentrated the distribution is around its expectation. The expectation has three complementary interpretations: algebraically it is a weighted average, physically it is the center of mass of the distribution, and in optimization terms it is the best constant prediction in the mean-square sense. Linearity of expectation reduces many complicated computations to simple ones (breaking a big problem into small ones). The chapter closes with several basic probability inequalities (Markov, Chebyshev, Cauchy–Schwarz and Jensen), which bound probabilities and expectations without detailed knowledge of the distribution and are the tools behind limit theorems such as the law of large numbers ([3.1.12](/3.1.12)). We use the common distributions of [3.1.4](/3.1.4) and the random vectors of [3.1.6](/3.1.6) and [3.1.7](/3.1.7); conditional expectation and covariance are treated in [3.1.9](/3.1.9) and [3.1.10](/3.1.10).

## 8.1. Definition of Expectation

We begin with a historical problem. Two players of equal skill agree that whoever first wins 5 rounds takes the whole stake of 100 gold coins. The game is interrupted when player A has won 4 rounds and player B has won 3. How should the stake be divided? Dividing it in the ratio $4:3$ of rounds won ignores what could still happen. The idea in the correspondence between Pascal and Fermat in 1654 is this: two more rounds would certainly decide the game, and B wins only by winning both, which has probability $\frac{1}{4}$. So A's gain $X$ is 100 with probability $\frac{3}{4}$ and 0 with probability $\frac{1}{4}$, A's "expected gain" is $100 \times \frac{3}{4} + 0 \times \frac{1}{4} = 75$, and the stake should be divided $3:1$. Averaging the values of a random variable with their probabilities as weights gives the expectation.

**Definition 8.1.1 (Expectation)** Let the discrete random variable $X$ have mass function $\mathbb{P}(X = x_j)$, $j = 1, 2, \dots$. If $\sum_{j=1}^{\infty} \lvert x_j \rvert \mathbb{P}(X = x_j) < \infty$, then

$$
\mathbb{E}X = \sum_{j=1}^{\infty} x_j \mathbb{P}(X = x_j)
$$
is called the **expectation** (or mean) of $X$. Let the continuous random variable $X$ have density $f(x)$. If $\int_{-\infty}^{\infty} \lvert x \rvert f(x)\,\mathrm{d}x < \infty$, then

$$
\mathbb{E}X = \int_{-\infty}^{\infty} x f(x)\,\mathrm{d}x
$$
is called the expectation (or mean) of $X$.

Absolute convergence is required so that the sum of the series does not depend on the order of summation, and hence the expectation depends only on the distribution. A random variable taking finitely many values always has an expectation. The expectation is written $\mathbb{E}X$ or $\mathbb{E}(X)$. If $\mathbb{P}(X = x_j)$ is regarded as a mass placed at the position $x_j$, then $\mathbb{E}X$ is the center of mass of these masses; in the continuous case the density plays the role of a linear mass density.

### 8.1.1. Expectations of Common Distributions

**Example 8.1.1** If $X \sim \mathrm{Ber}(p)$, then $\mathbb{E}X = 1 \cdot p + 0 \cdot (1 - p) = p$. In particular, for an event $A$ the indicator function satisfies $\boldsymbol{1}_A \sim \mathrm{Ber}(\mathbb{P}(A))$, so

$$
\mathbb{E}\boldsymbol{1}_A = \mathbb{P}(A).
$$
This identity is the bridge between probability and expectation: a probability is the expectation of an indicator.

**Example 8.1.2** If $X \sim \mathrm{Bin}(n, p)$, then $\mathbb{E}X = np$.

**Proof** Using $j\binom{n}{j} = n\binom{n-1}{j-1}$ and the normalization of the binomial mass function,

$$
\mathbb{E}X = \sum_{j=0}^n j\binom{n}{j}p^j(1 - p)^{n-j} = np\sum_{j=1}^n \binom{n-1}{j-1}p^{j-1}(1 - p)^{n-j} = np\sum_{k=0}^{n-1}\binom{n-1}{k}p^k(1 - p)^{n-1-k} = np. \qquad \square
$$
Intuitively, $n$ trials with success probability $p$ each yield $np$ successes on average; Example 8.2.4 gives a simpler proof by linearity of expectation.

**Example 8.1.3** If $X \sim \mathrm{Poi}(\lambda)$, then by normalization $\mathbb{E}X = \sum_{k=1}^{\infty} k\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda} = \lambda\sum_{k=1}^{\infty}\frac{\lambda^{k-1}}{(k - 1)!}\mathrm{e}^{-\lambda} = \lambda$.

**Example 8.1.4** Let $X \sim \mathrm{Geo}(p)$ with $\mathbb{P}(X = k) = p q^{k-1}$ ($k \ge 1$, $q = 1 - p$). Differentiating a power series term by term,

$$
\mathbb{E}X = \sum_{k=1}^{\infty} k p q^{k-1} = p\Big(\sum_{k=0}^{\infty} q^k\Big)' = \frac{p}{(1 - q)^2} = \frac{1}{p}.
$$
With success probability $p$, the first success takes $1/p$ trials on average. Example 9.2.3 gives another computation using conditional expectation.

**Example 8.1.5** If $X \sim \mathrm{U}(a, b)$, then $\mathbb{E}X = \int_a^b \frac{x}{b - a}\,\mathrm{d}x = \frac{a + b}{2}$, the midpoint of the interval.

**Example 8.1.6** Let $X \sim \Gamma(\alpha, \lambda)$ with density $f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-\lambda x}$ ($x > 0$). With $t = \lambda x$,

$$
\mathbb{E}X = \int_0^{\infty} \frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha}\mathrm{e}^{-\lambda x}\,\mathrm{d}x = \frac{1}{\lambda\Gamma(\alpha)}\int_0^{\infty} t^{(\alpha+1)-1}\mathrm{e}^{-t}\,\mathrm{d}t = \frac{\Gamma(\alpha + 1)}{\lambda\Gamma(\alpha)} = \frac{\alpha}{\lambda}.
$$
For $\alpha = 1$, $\Gamma(1, \lambda) = \mathrm{Exp}(\lambda)$ and $\mathbb{E}X = 1/\lambda$: the parameter $\lambda$ is a rate, and the mean is its reciprocal.

**Example 8.1.7** If the expectation of $X$ exists and its density is symmetric about $x = \mu$, that is, $f(\mu + x) = f(\mu - x)$, then $\mathbb{E}X = \mu$.

**Proof** The function $g(t) = t f(t + \mu)$ is odd and $\int \lvert g \rvert < \infty$, so

$$
\mathbb{E}X = \int_{-\infty}^{\infty} \mu f(x)\,\mathrm{d}x + \int_{-\infty}^{\infty}(x - \mu)f(x)\,\mathrm{d}x = \mu + \int_{-\infty}^{\infty} t f(t + \mu)\,\mathrm{d}t = \mu. \qquad \square
$$
In particular $\mathbb{E}X = \mu$ for $X \sim \mathcal{N}(\mu, \sigma^2)$. This is the center-of-mass intuition at work. The condition that the expectation exist cannot be dropped: the Cauchy density is symmetric about $0$, but the Cauchy distribution has no expectation (Example 8.2.7).

### 8.1.2. Expectations of General Random Variables

**Example 8.1.8** Toss a fair coin. On heads you receive 0.5 yuan; on tails you spin a prize wheel and receive an amount distributed as $\mathrm{U}(0, 1)$. The final amount $X$ is neither discrete nor continuous: its distribution function has a jump of height $\frac{1}{2}$ at 0.5 and otherwise has density $\frac{1}{2}\boldsymbol{1}_{(0,1)}(x)$. Computing the discrete and continuous parts separately by the definition and adding,

$$
\mathbb{E}X = 0.5 \times \frac{1}{2} + \int_0^1 x \cdot \frac{1}{2}\,\mathrm{d}x = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}.
$$

In general (stated for reference), if $X$ has distribution function $F$, the expectation can be defined uniformly as $\mathbb{E}X = \int_{\mathbb{R}} x\,\mathrm{d}F(x)$ (a Lebesgue–Stieltjes integral). If $F = F_1 + F_2$, where $F_1(x) = \int_{-\infty}^x f_0(s)\,\mathrm{d}s$ has a density and $F_2$ jumps only at countably many points $x_j$, with jump heights $\mathbb{P}(X = x_j)$, then, provided $\int \lvert x \rvert f_0(x)\,\mathrm{d}x + \sum_j \lvert x_j \rvert\mathbb{P}(X = x_j) < \infty$,

$$
\mathbb{E}X = \int_{-\infty}^{\infty} x f_0(x)\,\mathrm{d}x + \sum_j x_j\,\mathbb{P}(X = x_j) = \int x\,\mathrm{d}F_1(x) + \int x\,\mathrm{d}F_2(x).
$$
This shows that the expectation depends only on the distribution: identically distributed random variables have the same expectation (when it exists).

## 8.2. Expectations of Functions of Random Vectors and Properties of Expectation

### 8.2.1. Expectations of Functions of Random Vectors

To compute $\mathbb{E}\cos X$ for $X \sim \mathrm{U}(0, \pi/2)$, one approach is to find the density of $Y = \cos X$ first and then compute $\mathbb{E}Y$ from the definition. This step is in fact unnecessary. Take a discrete example: if $X$ takes the values $-1, 1, 2$ and $Y = X^2$ takes the values $1, 4$, then

$$
\mathbb{E}Y = 1 \cdot \mathbb{P}(Y = 1) + 4 \cdot \mathbb{P}(Y = 4) = 1 \cdot [\mathbb{P}(X = -1) + \mathbb{P}(X = 1)] + 4 \cdot \mathbb{P}(X = 2) = \sum_{x} g(x)\mathbb{P}(X = x),
$$
so the weighted average of $g(X)$ can be computed directly from the distribution of $X$.

**Theorem 8.2.1** Let the random vector $\boldsymbol{X} = (X_1, \dots, X_n)$ have joint distribution function $F(\boldsymbol{x})$, and let $g(\boldsymbol{x})$ be a real function. If $\int_{\mathbb{R}^n} \lvert g(\boldsymbol{x}) \rvert\,\mathrm{d}F(\boldsymbol{x}) < \infty$, then the expectation of $Y = g(\boldsymbol{X})$ exists and

$$
\mathbb{E}g(\boldsymbol{X}) = \int_{\mathbb{R}^n} g(\boldsymbol{x})\,\mathrm{d}F(\boldsymbol{x}).
$$
Concretely, $\mathbb{E}g(\boldsymbol{X}) = \sum_{\boldsymbol{x}} g(\boldsymbol{x})\mathbb{P}(\boldsymbol{X} = \boldsymbol{x})$ if $\boldsymbol{X}$ is discrete, and $\mathbb{E}g(\boldsymbol{X}) = \int_{\mathbb{R}^n} g(\boldsymbol{x})f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$ if $\boldsymbol{X}$ has joint density $f$.

The convenience of this theorem is that the expectation of $g(\boldsymbol{X})$ can be computed without first deriving the distribution of $g(\boldsymbol{X})$.

**Example 8.2.1** If $X \sim \mathrm{U}(0, \pi/2)$, then $\mathbb{E}\cos X = \int_0^{\pi/2} \frac{2}{\pi}\cos x\,\mathrm{d}x = \frac{2}{\pi}$.

**Example 8.2.2** Let $X \sim \mathcal{N}(0, 1)$ and let $\alpha$ be a constant. Compute $\mathbb{E}\lvert X \rvert^\alpha$.

**Solution** For $\alpha > -1$, with $x = \sqrt{2t}$,

$$
\mathbb{E}\lvert X \rvert^\alpha = \frac{2}{\sqrt{2\pi}}\int_0^{\infty} x^\alpha\mathrm{e}^{-x^2/2}\,\mathrm{d}x = \frac{2^{\alpha/2}}{\sqrt{\pi}}\int_0^{\infty} t^{\frac{\alpha+1}{2}-1}\mathrm{e}^{-t}\,\mathrm{d}t = \sqrt{\frac{2^\alpha}{\pi}}\,\Gamma\Big(\frac{\alpha + 1}{2}\Big).
$$
In particular (using $\Gamma(1/2) = \sqrt{\pi}$), $\mathbb{E}X^2 = 1$ and $\mathbb{E}\lvert X \rvert = \sqrt{2/\pi}$; for $\alpha \le -1$ the integral diverges near $0$ and $\mathbb{E}\lvert X \rvert^\alpha = \infty$.

**Example 8.2.3** If $(X, Y)$ is uniformly distributed on the unit disk $D = \{x^2 + y^2 \le 1\}$, then

$$
\mathbb{E}X = \int_{\mathbb{R}^2} x\cdot\frac{1}{\pi}\boldsymbol{1}_D(x, y)\,\mathrm{d}x\,\mathrm{d}y = \frac{1}{\pi}\int_{-1}^{1}\Big(\int_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}} x\,\mathrm{d}x\Big)\mathrm{d}y = 0,
$$
and likewise $\mathbb{E}Y = 0$: the center of mass is the center of the disk.

### 8.2.2. Properties of Expectation

In general $\mathbb{E}g(X) \ne g(\mathbb{E}X)$, but equality holds for linear functions.

**Theorem 8.2.2** Let $\mathbb{E}\lvert X \rvert < \infty$, $\mathbb{E}\lvert Y \rvert < \infty$, and let $a, b, c$ be real numbers. Then

1. $\mathbb{E}c = c$;
2. $\lvert \mathbb{E}X \rvert \le \mathbb{E}\lvert X \rvert$;
3. (linearity) $\mathbb{E}(aX + bY) = a\mathbb{E}X + b\mathbb{E}Y$;
4. (monotonicity) if $X \le Y$ a.s., then $\mathbb{E}X \le \mathbb{E}Y$;
5. if $X$ and $Y$ are independent, then $\mathbb{E}(XY) = \mathbb{E}X \cdot \mathbb{E}Y$.

**Proof** We treat the case where $(X, Y)$ has a joint density $f$; in the discrete case integrals are replaced by sums. Items 1 and 2 follow directly from the definition. Item 3: by Theorem 8.2.1,

$$
\mathbb{E}(aX + bY) = \int\!\!\int (ax + by)f(x, y)\,\mathrm{d}x\,\mathrm{d}y = a\int x f_X(x)\,\mathrm{d}x + b\int y f_Y(y)\,\mathrm{d}y = a\mathbb{E}X + b\mathbb{E}Y,
$$
where splitting the integral is justified by the integrability implied by $\lvert ax + by \rvert \le \lvert a \rvert\lvert x \rvert + \lvert b \rvert\lvert y \rvert$. Item 4: $Y - X \ge 0$ a.s., a nonnegative random variable has nonnegative expectation, and item 3 finishes the argument. Item 5: by Theorem 6.3.3, $f(x, y) = f_X(x)f_Y(y)$, and Fubini's theorem gives $\mathbb{E}(XY) = \int x f_X(x)\,\mathrm{d}x \int y f_Y(y)\,\mathrm{d}y$ (after checking integrability with $\lvert xy \rvert$). $\square$

Linearity requires no independence at all, which makes it the most powerful computational tool: write a complicated random variable as a sum of simple ones, often indicators.

**Example 8.2.4** If $X \sim \mathrm{Bin}(n, p)$, then $X$ has the same distribution as $X_1 + \cdots + X_n$, where $X_i \sim \mathrm{Ber}(p)$ is the indicator that the $i$-th trial succeeds. By linearity $\mathbb{E}X = np$. Similarly, by Example 7.1.5, $\Gamma(k, \lambda)$ (with $k$ a positive integer) is the distribution of a sum of $k$ independent $\mathrm{Exp}(\lambda)$ variables, so its expectation is $k/\lambda$.

**Example 8.2.5 (Quality Inspection)** Among $N$ products, $M$ are good. If $n$ products are drawn at random without replacement, how many good ones do we expect?

**Solution** The number $X$ of good products drawn has the hypergeometric distribution $\mathrm{H}(n, M, N)$, $\mathbb{P}(X = k) = \binom{M}{k}\binom{N-M}{n-k}\big/\binom{N}{n}$, and computing from the definition is tedious. Let $X_k$ be the indicator that the $k$-th draw is good; then $X = X_1 + \cdots + X_n$. By the fairness of drawing lots, each $X_k \sim \mathrm{Ber}(M/N)$ (although the $X_k$ are not independent), so by linearity

$$
\mathbb{E}X = \mathbb{E}X_1 + \cdots + \mathbb{E}X_n = n\frac{M}{N}.
$$

**Example 8.2.6 (A Typing Robot)** A robot types on a keyboard with only the $N = 26$ lowercase letters, choosing each letter independently and uniformly at random. How many keystrokes does it need on average to type $k$ distinct letters?

**Solution** Let $S_k$ be the keystroke on which the $k$-th new letter appears, $S_0 = 0$, and let $X_k = S_k - S_{k-1}$ be the waiting time for the $k$-th new letter. After $k - 1$ distinct letters have appeared, each keystroke produces a new letter with probability $p_k = \frac{N - k + 1}{N}$, so $X_k \sim \mathrm{Geo}(p_k)$ and $\mathbb{E}X_k = \frac{N}{N - k + 1}$. Since $S_k = X_1 + \cdots + X_k$,

$$
\mathbb{E}S_k = \sum_{j=1}^k \frac{N}{N - j + 1} = N\sum_{m=N-k+1}^{N}\frac{1}{m}.
$$
In particular $\mathbb{E}S_N = N\big(1 + \frac{1}{2} + \cdots + \frac{1}{N}\big) \approx N(\ln N + \gamma)$, where $\gamma \approx 0.577$ is Euler's constant, while for large $N$, $\mathbb{E}S_{N/2} = N\sum_{m=N/2+1}^{N}\frac{1}{m} \approx N\ln 2 \approx 0.693N$. So typing half of the letters is fairly easy, typing all of them much harder: the last few letters take a long time. For instance, with 50 distinct symbols on the keyboard, typing all of them takes $50 \times (1 + \frac{1}{2} + \cdots + \frac{1}{50}) \approx 225$ keystrokes on average, while typing 25 of them takes only about 34. This is the coupon collector problem.

**Example 8.2.7** If $X \sim t_1$, the Cauchy distribution, then $\mathbb{E}X$ does not exist. By Example 7.1.6, $X$ has the same distribution as $Z/W$ with $Z, W$ independent and both $\mathcal{N}(0, 1)$, but we cannot conclude $\mathbb{E}X = \mathbb{E}Z/\mathbb{E}W$: the properties of expectation say nothing about quotients. By definition,

$$
\int_{-\infty}^{\infty}\frac{\lvert x \rvert}{\pi(1 + x^2)}\,\mathrm{d}x = \frac{2}{\pi}\int_0^{\infty}\frac{x}{1 + x^2}\,\mathrm{d}x = \infty,
$$
so the requirement of absolute convergence fails and the expectation does not exist (although the density is symmetric about $0$).

**Example 8.2.8** If $\mathbb{E}\lvert X \rvert = 0$, then $X = 0$ a.s.

**Proof** For each $n$, $\mathbb{P}(\lvert X \rvert > 1/n) = \mathbb{E}\boldsymbol{1}\{n\lvert X \rvert > 1\} \le \mathbb{E}\big(n\lvert X \rvert\boldsymbol{1}\{n\lvert X \rvert > 1\}\big) \le n\mathbb{E}\lvert X \rvert = 0$. By continuity of probability,

$$
\mathbb{P}(\lvert X \rvert > 0) = \mathbb{P}\Big(\bigcup_{n=1}^{\infty}\{\lvert X \rvert > 1/n\}\Big) = \lim_{n\to\infty}\mathbb{P}(\lvert X \rvert > 1/n) = 0. \qquad \square
$$

### 8.2.3. Other Formulas for the Expectation

**Theorem 8.2.3** Let $X \ge 0$. If $X$ is a continuous random variable (or in general),

$$
\mathbb{E}X = \int_0^{\infty}\mathbb{P}(X > x)\,\mathrm{d}x;
$$
if $X$ takes only nonnegative integer values, then $\mathbb{E}X = \sum_{k=1}^{\infty}\mathbb{P}(X \ge k) = \sum_{k=0}^{\infty}\mathbb{P}(X > k)$. More generally, for $r \ge 1$, $\mathbb{E}X^r = \int_0^{\infty} r x^{r-1}\mathbb{P}(X > x)\,\mathrm{d}x$.

**Proof** Let $X$ have density $f$. By $x^r = \int_0^x r t^{r-1}\,\mathrm{d}t$ and Fubini's theorem (the integrand is nonnegative),

$$
\mathbb{E}X^r = \int_0^{\infty}\Big(\int_0^x r t^{r-1}\,\mathrm{d}t\Big)f(x)\,\mathrm{d}x = \int_0^{\infty} r t^{r-1}\Big(\int_t^{\infty}f(x)\,\mathrm{d}x\Big)\mathrm{d}t = \int_0^{\infty} r t^{r-1}\mathbb{P}(X > t)\,\mathrm{d}t.
$$
In the integer-valued case, split each term $k\mathbb{P}(X = k)$ of $\mathbb{E}X = \sum_k k\mathbb{P}(X = k)$ into $k$ copies of $\mathbb{P}(X = k)$ and re-sum by columns. $\square$

For example, if $X \sim \mathrm{Geo}(p)$, then $\mathbb{P}(X \ge k) = q^{k-1}$ and $\mathbb{E}X = \sum_{k\ge1}q^{k-1} = 1/p$; if $X \sim \mathrm{Exp}(\lambda)$, then $\mathbb{E}X = \int_0^{\infty}\mathrm{e}^{-\lambda x}\,\mathrm{d}x = 1/\lambda$.

**Example 8.2.9** A segment $[0, 1]$ is broken at a point $X$ chosen uniformly at random. Find the expected length of the piece $L$ that contains a fixed point $p_0 \in (0, 1)$.

**Solution** If $X < p_0$, the piece containing $p_0$ is the right one and $L = 1 - X$; if $X \ge p_0$, it is the left one and $L = X$. By Theorem 8.2.1,

$$
\mathbb{E}L = \int_0^{p_0}(1 - x)\,\mathrm{d}x + \int_{p_0}^1 x\,\mathrm{d}x = p_0 - \frac{p_0^2}{2} + \frac{1 - p_0^2}{2} = \frac{1}{2} + p_0(1 - p_0).
$$
This exceeds the average length $\frac{1}{2}$ of the two pieces (and is largest, $\frac{3}{4}$, when $p_0$ is the midpoint): the longer piece is more likely to contain $p_0$. Such length-biased sampling is common in problems such as waiting times for buses.

### 8.2.4. The Expectation as an Optimizer

**Theorem 8.2.4** If $\mathbb{E}X = \mu$ and $\mathbb{E}X^2 < \infty$, then

$$
\mathbb{E}(X - \mu)^2 \le \mathbb{E}(X - c)^2, \quad \forall c \in \mathbb{R},
$$
that is, $\mathbb{E}X = \operatorname*{argmin}_{c\in\mathbb{R}}\mathbb{E}(X - c)^2$.

**Proof** $\mathbb{E}(X - c)^2 = \mathbb{E}(X - \mu)^2 + 2(\mu - c)\mathbb{E}(X - \mu) + (\mu - c)^2 = \mathbb{E}(X - \mu)^2 + (\mu - c)^2$. $\square$

So if we "predict" a random variable $X$ by a constant $c$ and measure the quality of the prediction by the mean squared error $\mathbb{E}(X - c)^2$, the best constant predictor is the expectation. [3.1.9](/3.1.9) extends this result to predicting $X$ by a function of another random variable. The expectation is not the only reasonable numerical characteristic: with absolute error instead, the best constant becomes the median.

**Theorem 8.2.5** Let $\mathbb{E}\lvert X \rvert < \infty$ and let $m$ be a median of $X$ (a number with $\mathbb{P}(X \le m) \ge \frac{1}{2}$ and $\mathbb{P}(X \ge m) \ge \frac{1}{2}$, such as $F^{-1}(1/2)$). Then $m = \operatorname*{argmin}_{c\in\mathbb{R}}\mathbb{E}\lvert X - c \rvert$.

**Proof** Let $c > m$. For $x \le m$, $\lvert x - c \rvert - \lvert x - m \rvert = c - m$; for $x > m$, $\lvert x - c \rvert - \lvert x - m \rvert \ge -(c - m)$ by the triangle inequality. Hence

$$
\mathbb{E}\lvert X - c \rvert - \mathbb{E}\lvert X - m \rvert \ge (c - m)\big[\mathbb{P}(X \le m) - \mathbb{P}(X > m)\big] \ge 0,
$$
since $\mathbb{P}(X \le m) \ge \frac{1}{2} \ge \mathbb{P}(X > m)$. The case $c < m$ is symmetric and uses $\mathbb{P}(X \ge m) \ge \frac{1}{2}$. $\square$

The median always exists and is insensitive to extreme values, which is why it is widely used for social statistics such as income. In probability and statistics, however, the expectation is more important, because it has good mathematical properties such as linearity, whereas the median may not be unique and is not additive.

## 8.3. Variance

### 8.3.1. Definition and Computation

Two random variables with the same expectation can be spread out very differently. In investment, for example, two products with the same average return may carry very different risks.

**Definition 8.3.1 (Variance)** If the expectation $\mu = \mathbb{E}X$ of a random variable $X$ is finite, $\mathbb{E}(X - \mu)^2$ is called the **variance** of $X$, written $\operatorname{Var}(X)$ or $\sigma_X^2$. When $\operatorname{Var}(X) < \infty$ we say that $X$ has finite variance. $\sigma_X = \sqrt{\operatorname{Var}(X)}$ is called the **standard deviation** of $X$.

The variance measures how concentrated $X$ is around its expectation, and the standard deviation has the same units as $X$. Expanding the square and using linearity of expectation gives the computational formula

$$
\operatorname{Var}(X) = \mathbb{E}X^2 - (\mathbb{E}X)^2.
$$
For integer-valued distributions it is often easier to compute the factorial moment $\mathbb{E}[X(X - 1)]$ than $\mathbb{E}X^2$, and then use $\mathbb{E}X^2 = \mathbb{E}[X(X - 1)] + \mathbb{E}X$.

**Example 8.3.1** Variances of common distributions.

- $X \sim \mathrm{Ber}(p)$: $X^2 = X$, so $\operatorname{Var}(X) = p - p^2 = pq$.
- $X \sim \mathrm{Poi}(\lambda)$: $\mathbb{E}[X(X - 1)] = \sum_{k\ge2}k(k - 1)\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda} = \lambda^2$, so $\mathbb{E}X^2 = \lambda^2 + \lambda$ and $\operatorname{Var}(X) = \lambda$.
- $X \sim \mathrm{Geo}(p)$: $\mathbb{E}[X(X - 1)] = \sum_{j\ge1}j(j - 1)pq^{j-1} = pq\big(\sum_{j\ge0}q^j\big)'' = \frac{2pq}{(1 - q)^3} = \frac{2q}{p^2}$, so $\mathbb{E}X^2 = \frac{2q}{p^2} + \frac{1}{p}$ and $\operatorname{Var}(X) = \frac{2q}{p^2} + \frac{1}{p} - \frac{1}{p^2} = \frac{q}{p^2}$.
- $X \sim \mathrm{U}(a, b)$: $\mathbb{E}X^2 = \frac{b^3 - a^3}{3(b - a)} = \frac{a^2 + ab + b^2}{3}$ and $\operatorname{Var}(X) = \frac{(b - a)^2}{12}$.
- $X \sim \Gamma(\alpha, \lambda)$: computing as in Example 8.1.6, $\mathbb{E}X^2 = \frac{\Gamma(\alpha + 2)}{\lambda^2\Gamma(\alpha)} = \frac{\alpha(\alpha + 1)}{\lambda^2}$ and $\operatorname{Var}(X) = \frac{\alpha}{\lambda^2}$; in particular $\mathrm{Exp}(\lambda)$ has variance $\frac{1}{\lambda^2}$.
- $X \sim \mathcal{N}(\mu, \sigma^2)$: with $t = (x - \mu)/\sigma$, $\operatorname{Var}(X) = \frac{\sigma^2}{\sqrt{2\pi}}\int t^2\mathrm{e}^{-t^2/2}\,\mathrm{d}t = \sigma^2$ (Example 8.2.2).
- $X \sim \mathrm{Bin}(n, p)$: $\operatorname{Var}(X) = npq$, immediate from item 4 of Theorem 8.3.1 below, since $X$ is a sum of $n$ independent $\mathrm{Ber}(p)$ variables.

The two parameters of the normal distribution are its expectation and variance, and the expectation and variance of a Poisson distribution are equal; this is the intuitive meaning of the parameters of the common distributions.

**Theorem 8.3.1** Let $\mathbb{E}X = \mu$ and $\operatorname{Var}(X) < \infty$. Then

1. $\operatorname{Var}(aX + b) = a^2\operatorname{Var}(X)$ for $a, b \in \mathbb{R}$;
2. $\operatorname{Var}(X) = \mathbb{E}(X - \mu)^2 \le \mathbb{E}(X - c)^2$ for all $c \in \mathbb{R}$;
3. $\operatorname{Var}(X) = 0 \iff X = \mu$ a.s.;
4. if $X_1, \dots, X_n$ are independent with finite variances, then $\operatorname{Var}\big(\sum_{k=1}^n X_k\big) = \sum_{k=1}^n \operatorname{Var}(X_k)$.

**Proof** 1. $\operatorname{Var}(aX + b) = \mathbb{E}(aX + b - a\mu - b)^2 = a^2\mathbb{E}(X - \mu)^2$. 2. This is Theorem 8.2.4. 3. Apply Example 8.2.8 to $(X - \mu)^2$. 4. With $\mu_k = \mathbb{E}X_k$,

$$
\operatorname{Var}\Big(\sum_k X_k\Big) = \mathbb{E}\Big(\sum_k (X_k - \mu_k)\Big)^2 = \sum_k \mathbb{E}(X_k - \mu_k)^2 + \sum_{j\ne k}\mathbb{E}[(X_j - \mu_j)(X_k - \mu_k)],
$$
and by item 5 of Theorem 8.2.2 the cross terms vanish under independence: $\mathbb{E}[(X_j - \mu_j)(X_k - \mu_k)] = \mathbb{E}(X_j - \mu_j)\,\mathbb{E}(X_k - \mu_k) = 0$. $\square$

The independence assumption in item 4 can be weakened to pairwise uncorrelatedness; the cross terms are exactly the covariances of [3.1.10](/3.1.10).

**Example 8.3.2 (The Matching Problem)** Someone writes $n$ letters and puts them at random into $n$ envelopes addressed to $n$ different people. Let $X$ be the number of letters that go into the correct envelope. Find $\mathbb{E}X$ and $\operatorname{Var}(X)$.

**Solution** Let $I_k$ be the indicator that the $k$-th letter is in the correct envelope, so $X = \sum_{k=1}^n I_k$. We have $\mathbb{P}(I_k = 1) = \frac{1}{n}$ and, for $j \ne k$, $\mathbb{P}(I_j = I_k = 1) = \frac{1}{n(n - 1)}$. Hence $\mathbb{E}X = n \cdot \frac{1}{n} = 1$,

$$
\mathbb{E}X^2 = \sum_k \mathbb{E}I_k^2 + \sum_{j\ne k}\mathbb{E}(I_jI_k) = n\cdot\frac{1}{n} + n(n - 1)\cdot\frac{1}{n(n - 1)} = 2,
$$
and $\operatorname{Var}(X) = 2 - 1 = 1$. The $I_k$ are not independent, yet linearity of expectation applies all the same; both the expectation and the variance are independent of $n$, consistent with the fact that $X$ is approximately $\mathrm{Poi}(1)$ for large $n$.

**Example 8.3.3** Expectations and variances of the three main distributions of statistics.

1. $X \sim \chi^2_n$: $X$ has the same distribution as $Z_1^2 + \cdots + Z_n^2$ (Theorem 7.1.6), and $\mathbb{E}Z_i^2 = 1$, $\mathbb{E}Z_i^4 = 3$ (Example 8.2.2 with $\alpha = 4$), so $\mathbb{E}X = n$ and $\operatorname{Var}(X) = n(3 - 1) = 2n$.
2. $T \sim t_n$: for $n \ge 2$ the expectation exists and $\mathbb{E}T = 0$ by symmetry; for $n \ge 3$, $T = Z/\sqrt{X/n}$ and independence give $\operatorname{Var}(T) = \mathbb{E}Z^2 \cdot n\mathbb{E}X^{-1} = \frac{n}{n - 2}$, where $\mathbb{E}X^{-1} = \frac{1}{n - 2}$ is obtained by integrating directly against the density of $\chi^2_n = \Gamma(n/2, 1/2)$. For $n = 1$ the expectation does not exist (Example 8.2.7), and for $n = 2$ the variance is infinite.
3. $F \sim F_{m,n}$: for $n \ge 3$, $\mathbb{E}F = \mathbb{E}\frac{X}{m}\cdot\mathbb{E}\frac{n}{Y} = 1\cdot\frac{n}{n - 2} = \frac{n}{n - 2}$.

The methods used here are to reduce the expectation, through the relation between these distributions and the normal distribution, to the expectation of a product of independent variables, or to use the normalization of a density (rearranging the integral into another density).

### 8.3.2. Standardization

**Definition 8.3.2 (Standardization)** Let $0 < \operatorname{Var}(X) < \infty$ and put

$$
Y = \frac{X - \mathbb{E}X}{\sqrt{\operatorname{Var}(X)}}.
$$
Then $\mathbb{E}Y = 0$ and $\operatorname{Var}(Y) = 1$, and $Y$ is called the **standardization** of $X$.

In particular, $\frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$ when $X \sim \mathcal{N}(\mu, \sigma^2)$. Standardization removes location and scale, so that random variables with different units or orders of magnitude can be compared, for example ranks in two exams with different score distributions.

### 8.3.3. Expectations and Variances of Common Distributions

| Distribution | Expectation | Variance |
|---|---|---|
| $\mathrm{Ber}(p)$ | $p$ | $p(1 - p)$ |
| $\mathrm{Bin}(n, p)$ | $np$ | $np(1 - p)$ |
| $\mathrm{Poi}(\lambda)$ | $\lambda$ | $\lambda$ |
| $\mathrm{Geo}(p)$ | $1/p$ | $(1 - p)/p^2$ |
| $\mathrm{H}(n, M, N)$ | $nM/N$ | $n\frac{M}{N}\big(1 - \frac{M}{N}\big)\frac{N - n}{N - 1}$ |
| $\mathrm{U}(a, b)$ | $(a + b)/2$ | $(b - a)^2/12$ |
| $\mathrm{Exp}(\lambda)$ | $1/\lambda$ | $1/\lambda^2$ |
| $\Gamma(\alpha, \lambda)$ | $\alpha/\lambda$ | $\alpha/\lambda^2$ |
| $\mathrm{Beta}(\alpha, \beta)$ | $\frac{\alpha}{\alpha + \beta}$ | $\frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}$ |
| $\mathcal{N}(\mu, \sigma^2)$ | $\mu$ | $\sigma^2$ |
| $\chi^2_n$ | $n$ | $2n$ |
| $t_n$ | $0$ ($n \ge 2$) | $\frac{n}{n - 2}$ ($n \ge 3$) |

The variance of the hypergeometric distribution can be computed with the covariances of [3.1.10](/3.1.10); the moments of the beta distribution follow directly from beta function integrals, for example $\mathbb{E}X = \frac{\mathrm{B}(\alpha + 1, \beta)}{\mathrm{B}(\alpha, \beta)} = \frac{\alpha}{\alpha + \beta}$, which gives $\mathbb{E}U_{(k)} = \frac{k}{n + 1}$ (Example 7.2.3).

## 8.4. Moments

Expectation and variance are special cases of a more general class of numerical characteristics.

**Definition 8.4.1 (Moments)** Let $X$ be a random variable and $m$ a positive integer. If $\mathbb{E}\lvert X \rvert^m < \infty$, then $\mathbb{E}X^m$ is called the $m$-th **raw moment** of $X$ and $\mathbb{E}(X - \mathbb{E}X)^m$ the $m$-th **central moment** of $X$. For $m > 2$ these are collectively called higher moments.

The first raw moment is the expectation and the second central moment is the variance. If the moment of order $k$ exists, so does every moment of order $0 < j \le k$: from $\lvert x \rvert^j \le 1 + \lvert x \rvert^k$ (consider $\lvert x \rvert \le 1$ and $\lvert x \rvert > 1$ separately) we get $\mathbb{E}\lvert X \rvert^j \le 1 + \mathbb{E}\lvert X \rvert^k < \infty$.

**Definition 8.4.2 (Skewness and Kurtosis)** Let $X$ have a finite fourth moment, $\mu = \mathbb{E}X$ and $\sigma^2 = \operatorname{Var}(X) > 0$. The quantities

$$
\frac{\mathbb{E}(X - \mu)^3}{\sigma^3} = \mathbb{E}\Big(\frac{X - \mu}{\sigma}\Big)^3, \qquad \frac{\mathbb{E}(X - \mu)^4}{\sigma^4} - 3 = \mathbb{E}\Big(\frac{X - \mu}{\sigma}\Big)^4 - 3
$$
are called the **skewness** and the **kurtosis** of $X$ (the latter also the excess kurtosis).

Skewness and kurtosis are moments of the standardized variable and do not depend on location or scale. Skewness measures asymmetry: a symmetric distribution has skewness $0$, and a distribution with a long right tail has positive skewness. Kurtosis measures how heavy the tails are relative to the normal distribution: subtracting 3 makes the kurtosis of the normal distribution $0$ (since $\mathbb{E}Z^4 = 3$). For example, $\mathrm{Exp}(\lambda)$ has skewness 2 and kurtosis 6; $\mathrm{U}(a, b)$ has kurtosis $-1.2$; and $t_\nu$ ($\nu > 4$) has kurtosis $\frac{6}{\nu - 4} > 0$.

![Skewness and kurtosis: the left panel compares a symmetric and a right-skewed distribution, the right panel compares symmetric distributions with lighter and heavier tails (all standardized to mean 0 and variance 1)](./plots/skewness-kurtosis.py)

## 8.5. Probability Inequalities

When only some moments are known rather than the whole distribution, the following inequalities bound probabilities and expectations. They are not always sharp, but they are extremely useful in theoretical derivations: by focusing on the essential quantities and applying inequalities judiciously, one can balance accuracy against computational complexity.

**Theorem 8.5.1 (Markov's Inequality)** For a random variable $X$ and $\varepsilon > 0$, $\alpha > 0$,

$$
\mathbb{P}(\lvert X \rvert \ge \varepsilon) \le \frac{\mathbb{E}\lvert X \rvert^\alpha}{\varepsilon^\alpha}.
$$

**Proof** On the event $\{\lvert X \rvert \ge \varepsilon\} = \{\lvert X \rvert^\alpha \ge \varepsilon^\alpha\}$ we have $\lvert X \rvert^\alpha/\varepsilon^\alpha \ge 1$, so

$$
\mathbb{P}(\lvert X \rvert \ge \varepsilon) = \mathbb{E}\boldsymbol{1}\{\lvert X \rvert^\alpha \ge \varepsilon^\alpha\} \le \mathbb{E}\Big(\frac{\lvert X \rvert^\alpha}{\varepsilon^\alpha}\boldsymbol{1}\{\lvert X \rvert^\alpha \ge \varepsilon^\alpha\}\Big) \le \mathbb{E}\frac{\lvert X \rvert^\alpha}{\varepsilon^\alpha}. \qquad \square
$$

The case $\alpha = 1$ is the most common form: the probability that a nonnegative random variable is large is controlled by its expectation, $\mathbb{P}(X \ge \varepsilon) \le \mathbb{E}X/\varepsilon$.

**Corollary 8.5.1 (Chebyshev's Inequality)** If $X$ has finite variance, then for $\varepsilon > 0$,

$$
\mathbb{P}(\lvert X - \mathbb{E}X \rvert \ge \varepsilon) \le \frac{\operatorname{Var}(X)}{\varepsilon^2}.
$$

This is Markov's inequality with $\alpha = 2$ applied to $X - \mathbb{E}X$. It quantifies how concentrated $X$ is around its expectation: for any distribution with finite variance, the probability of falling outside $\mu \pm 2\sigma$ is at most $\frac{1}{4}$, and outside $\mu \pm 3\sigma$ at most $\frac{1}{9}$. For the normal distribution these probabilities are actually about 0.046 and 0.0027, so the Chebyshev bound is a conservative estimate valid for all distributions.

![The Chebyshev bound 1/k^2 compared with the actual tail probabilities P(|X - mu| >= k sigma) of several standardized distributions](./plots/chebyshev-bound.py)

**Example 8.5.1** A fair coin is tossed $N$ times. Use Chebyshev's inequality to bound the probability of at least $\frac{3N}{4}$ heads.

**Solution** The number of heads is $X \sim \mathrm{Bin}(N, 1/2)$, with $\mathbb{E}X = N/2$ and $\operatorname{Var}(X) = N/4$. Then

$$
\mathbb{P}\Big(X \ge \frac{3N}{4}\Big) \le \mathbb{P}\Big(\Big\lvert X - \frac{N}{2}\Big\rvert \ge \frac{N}{4}\Big) \le \frac{N/4}{(N/4)^2} = \frac{4}{N}.
$$
Here the distribution of $X$ is symmetric about $N/2$, so $\mathbb{P}(X - \frac{N}{2} \ge \frac{N}{4}) = \frac{1}{2}\mathbb{P}(\lvert X - \frac{N}{2} \rvert \ge \frac{N}{4})$ and the bound improves to $\frac{2}{N}$; for an asymmetric distribution, however, a one-sided probability is not half of the two-sided one, and the bound cannot be halved in this way.

**Theorem 8.5.2 (Cauchy–Schwarz Inequality)** If $\mathbb{E}X^2 < \infty$ and $\mathbb{E}Y^2 < \infty$, then

$$
\lvert \mathbb{E}(XY) \rvert \le \sqrt{\mathbb{E}X^2\,\mathbb{E}Y^2}.
$$
Equality holds if and only if there are constants $a, b$, not both zero, with $aX + bY = 0$ a.s.

**Proof** Since $\lvert xy \rvert \le \frac{1}{2}(x^2 + y^2)$, $\mathbb{E}(XY)$ exists. For any real $a, b$,

$$
0 \le \mathbb{E}(aX + bY)^2 = a^2\mathbb{E}X^2 + 2ab\,\mathbb{E}(XY) + b^2\mathbb{E}Y^2 = (a, b)\,\Sigma\,(a, b)^{\mathsf T}, \qquad \Sigma = \begin{pmatrix} \mathbb{E}X^2 & \mathbb{E}(XY) \\ \mathbb{E}(XY) & \mathbb{E}Y^2 \end{pmatrix}.
$$
Hence $\Sigma$ is a **positive semidefinite matrix**, and $\det\Sigma = \mathbb{E}X^2\,\mathbb{E}Y^2 - [\mathbb{E}(XY)]^2 \ge 0$, which is the inequality. Equality holds if and only if $\det\Sigma = 0$, if and only if there is a nonzero vector $(a, b)$ with $(a, b)\Sigma(a, b)^{\mathsf T} = 0$, that is, $\mathbb{E}(aX + bY)^2 = 0$, which by Example 8.2.8 is equivalent to $aX + bY = 0$ a.s. $\square$

This is precisely the Cauchy–Schwarz inequality for inner product spaces from linear algebra ([2.1](/2.1)), with the inner product $\langle X, Y \rangle = \mathbb{E}(XY)$. It is the reason why the correlation coefficient of [3.1.10](/3.1.10) has absolute value at most 1.

**Theorem 8.5.3 (Jensen's Inequality)** Let $\psi$ be a **convex function** on $\mathbb{R}$, and let $X$ and $\psi(X)$ have finite expectations. Then

$$
\psi(\mathbb{E}X) \le \mathbb{E}\psi(X).
$$
If $\psi$ is strictly convex, equality holds if and only if $X = \mathbb{E}X$ a.s.

**Proof** A convex function has a right derivative $c = \psi'_+(a)$ at every point $a$, and its graph lies above the supporting line at that point: $\psi(b) - \psi(a) \ge c(b - a)$ for all $b \in \mathbb{R}$. Taking $a = \mathbb{E}X$ and $b = X$ gives $\psi(X) - \psi(\mathbb{E}X) \ge c(X - \mathbb{E}X)$, and taking expectations,

$$
\mathbb{E}\psi(X) - \psi(\mathbb{E}X) \ge c\,\mathbb{E}(X - \mathbb{E}X) = 0.
$$
If $\psi$ is strictly convex, the supporting-line inequality is strict for $b \ne a$; so if the nonnegative random variable $\psi(X) - \psi(\mathbb{E}X) - c(X - \mathbb{E}X)$ has expectation $0$, it is $0$ almost surely (Example 8.2.8), that is, $X = \mathbb{E}X$ a.s. $\square$

For example, $\psi(x) = x^2$ gives $(\mathbb{E}X)^2 \le \mathbb{E}X^2$ (that is, $\operatorname{Var}(X) \ge 0$); $\psi(x) = \lvert x \rvert$ gives $\lvert \mathbb{E}X \rvert \le \mathbb{E}\lvert X \rvert$; and for a positive random variable the concave function $\ln x$ gives $\mathbb{E}\ln X \le \ln\mathbb{E}X$. In statistics, Jensen's inequality is used, for instance, to derive the EM algorithm and to prove the consistency of maximum likelihood estimators.

## Summary

- Expectation: $\mathbb{E}X = \sum x_j\mathbb{P}(X = x_j)$ or $\int x f(x)\,\mathrm{d}x$, with absolute convergence required; three interpretations: weighted average, center of mass, and best constant predictor $\operatorname*{argmin}_c\mathbb{E}(X - c)^2$.
- To compute $\mathbb{E}g(\boldsymbol{X})$, integrate directly against the distribution of $\boldsymbol{X}$; there is no need to find the distribution of $g(\boldsymbol{X})$ first.
- Linearity $\mathbb{E}(c + aX + bY) = c + a\mathbb{E}X + b\mathbb{E}Y$ needs no independence; the product rule $\mathbb{E}(XY) = \mathbb{E}X\,\mathbb{E}Y$ needs independence (or uncorrelatedness).
- Variance: $\operatorname{Var}(X) = \mathbb{E}X^2 - (\mathbb{E}X)^2$; $\operatorname{Var}(aX + b) = a^2\operatorname{Var}(X)$; the variance of a sum of independent variables is the sum of the variances.
- Inequalities: Markov $\mathbb{P}(\lvert X \rvert \ge \varepsilon) \le \mathbb{E}\lvert X \rvert^\alpha/\varepsilon^\alpha$; Chebyshev $\mathbb{P}(\lvert X - \mu \rvert \ge \varepsilon) \le \sigma^2/\varepsilon^2$; Cauchy–Schwarz $\lvert\mathbb{E}XY\rvert \le \sqrt{\mathbb{E}X^2\mathbb{E}Y^2}$; Jensen $\psi(\mathbb{E}X) \le \mathbb{E}\psi(X)$.
- Techniques: use normalization (rearrange an integral into a known density) and symmetry; for discrete distributions use factorial moments and differentiate power series; write counts as sums of indicators (sampling, matching, coupon collecting); exploit relations between random variables (such as $\chi^2_n$ and sums of squared normals) to compute expectations.
