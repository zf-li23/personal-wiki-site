---
title: Probability Generating, Moment Generating and Characteristic Functions
source_hash: 06870578d35e
---

Mass functions, densities and distribution functions describe a random variable through "the probability of each point or each interval". This chapter introduces another complete description of a distribution: transform the distribution into a function and work with that function instead. All three transforms are expectations of a function $h(X)$: the probability generating function takes $h(X) = s^X$, the moment generating function $\mathrm{e}^{sX}$, and the characteristic function $\mathrm{e}^{\mathrm{i}tX}$. Their common advantages come from the properties of the exponential: the distribution of a sum of independent random variables (a convolution, [3.1.7](/3.1.7)) becomes a product of transforms, and a sum of a random number of random variables becomes a composition; moreover, moments can be read off from derivatives, and the transform determines the distribution uniquely. The three tools apply in increasing generality: the probability generating function only to random variables with nonnegative integer values, the moment generating function when $\mathrm{e}^{sX}$ is integrable near $0$, and the characteristic function to every random variable. At the end of the chapter we introduce convergence in distribution and the continuity theorem, the main tools for the law of large numbers ([3.1.12](/3.1.12)) and the central limit theorem ([3.1.13](/3.1.13)) that follow. The characteristic function is essentially the Fourier transform of the distribution, which connects it with the Fourier analysis of [2.5](/2.5).

## 11.1. Probability Generating Functions

The probability generating function encodes the mass function $p_0, p_1, p_2, \dots$ of a nonnegative integer-valued random variable as the coefficients of a power series, so that probabilities, expectations and variances can be computed with the tools of calculus.

**Definition 11.1.1 (Probability Generating Function)** Let $X$ be a random variable taking nonnegative integer values. The function

$$
g(s) = \mathbb{E}(s^X) = \sum_{j=0}^{\infty} s^j\, \mathbb{P}(X = j), \quad s \in [-1, 1]
$$
is called the **probability generating function** (PGF) of $X$, with the convention $0^0 = 1$.

Since $\sum_j \lvert s^j \rvert \mathbb{P}(X = j) \le \sum_j \mathbb{P}(X = j) = 1$, the series converges absolutely on $[-1, 1]$, and $g(1) = 1$. Inside $(-1, 1)$ the probability generating function can be differentiated term by term any number of times.

**Property 11.1.1** Let $g(s)$ be the probability generating function of $X$ and $g^{(k)}(s)$ its $k$-th derivative (at $s = 1$ understood as the left derivative, i.e., the limit as $s \uparrow 1$, which may be $+\infty$). Then

1. $\mathbb{P}(X = k) = \dfrac{g^{(k)}(0)}{k!}$, $k = 0, 1, \dots$;
2. $\mathbb{E}X = g^{(1)}(1)$;
3. if $\mathbb{E}X^2 < \infty$, then $\operatorname{Var}(X) = g^{(2)}(1) + g^{(1)}(1) - [g^{(1)}(1)]^2$;
4. if $X_1, \dots, X_n$ are independent and $g_i(s) = \mathbb{E}(s^{X_i})$ is the probability generating function of $X_i$, then $Y = X_1 + \cdots + X_n$ has probability generating function

$$
g_Y(s) = g_1(s) g_2(s) \cdots g_n(s), \quad s \in [-1, 1].
$$

**Proof** 1. Differentiating term by term,

$$
\frac{g^{(k)}(0)}{k!} = \frac{1}{k!} \sum_{j=k}^{\infty} \frac{\mathrm{d}^k}{\mathrm{d}s^k} s^j\, \mathbb{P}(X = j) \Bigg|_{s=0} = \mathbb{P}(X = k).
$$

2. $g^{(1)}(1) = \sum_{j=0}^{\infty} j\, \mathbb{P}(X = j) = \mathbb{E}X$ (by Abel's theorem the left derivative converges to this series as $s \uparrow 1$; if the series diverges, both sides are $+\infty$).

3. Similarly $g^{(2)}(1) = \sum_j j(j-1) \mathbb{P}(X = j) = \mathbb{E}[X(X-1)]$, so

$$
g^{(2)}(1) + g^{(1)}(1) - [g^{(1)}(1)]^2 = \mathbb{E}[X(X-1)] + \mathbb{E}X - (\mathbb{E}X)^2 = \mathbb{E}X^2 - (\mathbb{E}X)^2 = \operatorname{Var}(X).
$$

4. The random variables $s^{X_1}, \dots, s^{X_n}$ are independent, and the expectation of a product of independent random variables is the product of the expectations: $\mathbb{E}(s^{X_1 + \cdots + X_n}) = \prod_i \mathbb{E}(s^{X_i})$. $\square$

By property 1, the probability generating function and the mass function determine each other: given the generating function, the coefficients can be read off by differentiation or Taylor expansion. Property 4 is what makes generating functions most useful: to find the distribution of an independent sum, there is no need to compute a convolution; one multiplies the generating functions and recognizes the distribution from the form of the product.

### 11.1.1. Generating Functions of Common Distributions

**Example 11.1.1 (Binomial Distribution)** For $X \sim \mathrm{Bin}(n, p)$ and $q = 1 - p$,

$$
g(s) = \sum_{j=0}^{n} s^j \binom{n}{j} p^j q^{n-j} = (q + sp)^n.
$$
Application: if $X_1, \dots, X_m$ are independent with $X_i \sim \mathrm{Bin}(n_i, p)$, then $Y = X_1 + \cdots + X_m$ has generating function $(q + sp)^{n_1 + \cdots + n_m}$, so $Y \sim \mathrm{Bin}(n_1 + \cdots + n_m, p)$.

**Example 11.1.2 (Poisson Distribution)** For $X \sim \mathrm{Poi}(\lambda)$,

$$
g(s) = \sum_{k=0}^{\infty} s^k \frac{\lambda^k}{k!} \mathrm{e}^{-\lambda} = \mathrm{e}^{\lambda(s-1)}.
$$
Application: if $X_1, \dots, X_m$ are independent with $X_i \sim \mathrm{Poi}(\lambda_i)$, then $X_1 + \cdots + X_m \sim \mathrm{Poi}(\lambda_1 + \cdots + \lambda_m)$.

**Example 11.1.3 (Geometric and Pascal Distributions)** For $X \sim \mathrm{Geo}(p)$ (with values $1, 2, \dots$),

$$
g(s) = \sum_{k=1}^{\infty} s^k p q^{k-1} = \frac{sp}{1 - sq}.
$$
Let $X_1, \dots, X_m$ be independent $\mathrm{Geo}(p)$. Then $S_m = X_1 + \cdots + X_m$ has generating function $g_m(s) = \left(\dfrac{sp}{1 - sq}\right)^m$. Expanding with the negative binomial series $(1 - x)^{-m} = \sum_{j \ge 0} \binom{m + j - 1}{m - 1} x^j$,

$$
g_m(s) = (sp)^m \sum_{j=0}^{\infty} \binom{m + j - 1}{m - 1} (sq)^j = \sum_{k=m}^{\infty} \binom{k - 1}{m - 1} p^m q^{k-m} s^k,
$$
and reading off the coefficients gives the Pascal distribution $\mathrm{Pascal}(m, p)$:

$$
\mathbb{P}(S_m = k) = \binom{k - 1}{m - 1} p^m q^{k-m}, \quad k = m, m+1, \dots
$$
This agrees with the direct computation of "the number of trials needed for the $m$-th success".

### 11.1.2. Sums of a Random Number of Random Variables

The total amount an insurer pays out in a year is the sum of a random number of individual claims, the number of claims itself being random. Generating functions handle the distribution of such random sums most neatly.

**Theorem 11.1.1** Suppose that

1. $\{X_j\}$ is a sequence of i.i.d. nonnegative integer-valued random variables, and $X_1$ has probability generating function $g_X(s) = \sum_{k=0}^{\infty} p_k s^k$, $p_k = \mathbb{P}(X_1 = k)$;
2. $N$ is a random variable with positive integer values and probability generating function $g_N(s) = \sum_{n=1}^{\infty} s^n \mathbb{P}(N = n)$;
3. $N$ and $\{X_j\}$ are independent.

Then $W = X_1 + X_2 + \cdots + X_N$ has probability generating function

$$
g_W(s) = g_N(g_X(s)).
$$

**Proof** By the law of total expectation (Theorem 9.2.2),

$$
\begin{aligned}
g_W(s) = \mathbb{E}(s^W) &= \sum_{n=1}^{\infty} \mathbb{E}(s^W \mid N = n)\, \mathbb{P}(N = n) = \sum_{n=1}^{\infty} \mathbb{E}(s^{X_1 + \cdots + X_n} \mid N = n)\, \mathbb{P}(N = n) \\
&= \sum_{n=1}^{\infty} \mathbb{E}(s^{X_1 + \cdots + X_n})\, \mathbb{P}(N = n) = \sum_{n=1}^{\infty} [g_X(s)]^n\, \mathbb{P}(N = n) = g_N(g_X(s)),
\end{aligned}
$$
where the third equality uses the independence of $N$ and $\{X_j\}$, and the fourth uses item 4 of Property 11.1.1. $\square$

The result remains true if $N$ may take the value $0$ (with the convention $W = 0$ in that case).

**Example 11.1.4** A hen lays $N \sim \mathrm{Poi}(\lambda)$ eggs, and each egg hatches independently with probability $p$. Then the number $W$ of eggs that hatch satisfies $W \sim \mathrm{Poi}(\lambda p)$.

**Solution** Let $X_i = 1$ or $0$ according as the $i$-th egg hatches or not. Then $W = X_1 + \cdots + X_N$, where the $\{X_i\}$ are i.i.d. and independent of $N$. With $g_X(s) = q + ps$ and $g_N(s) = \mathrm{e}^{\lambda(s-1)}$, Theorem 11.1.1 gives

$$
g_W(s) = g_N(g_X(s)) = \mathrm{e}^{\lambda((q + ps) - 1)} = \mathrm{e}^{\lambda p(s-1)}.
$$
This is the generating function of $\mathrm{Poi}(\lambda p)$, and since the generating function determines the mass function, $W \sim \mathrm{Poi}(\lambda p)$. This phenomenon is called *thinning* of the Poisson distribution.

![Poisson thinning: of N ~ Poi(10) eggs, each hatches with probability p = 0.3; simulated frequencies of W compared with the mass function of Poi(3)](./plots/poisson-thinning.py)

### 11.1.3. Generating Functions of Random Vectors

**Definition 11.1.2** Let $(X, Y)$ be a two-dimensional random vector with nonnegative integer values and joint mass function $p_{ik} = \mathbb{P}(X = i, Y = k)$, $i, k = 0, 1, 2, \dots$. The function

$$
g(s, t) = \mathbb{E}(s^X t^Y) = \sum_{i=0}^{\infty} \sum_{k=0}^{\infty} p_{ik}\, s^i t^k, \quad s, t \in [-1, 1]
$$
is called the probability generating function of $(X, Y)$.

**Property 11.1.2** Let $g(s, t)$ be the probability generating function of $(X, Y)$ and $g_X$, $g_Y$ those of $X$ and $Y$. Then

1. $\lvert g(s, t) \rvert \le g(1, 1) = 1$ for $\lvert s \rvert \le 1$, $\lvert t \rvert \le 1$;
2. for nonnegative integers $a, b, c$, $g_{aX + bY + c}(s) = s^c g(s^a, s^b)$;
3. $X$ and $Y$ are independent if and only if $g(s, t) = g_X(s) g_Y(t)$ for all $s, t$;
4. $g(s, 1) = g_X(s)$ and $g(1, t) = g_Y(t)$;
5. $p_{ik} = \dfrac{1}{i!\,k!} \dfrac{\partial^{i+k} g(s, t)}{\partial s^i\, \partial t^k}\Big|_{s=t=0}$, $i, k = 0, 1, 2, \dots$;
6. if $\mathbb{E}X, \mathbb{E}Y < \infty$, then $\mathbb{E}X = \dfrac{\partial g}{\partial s}\Big|_{s=t=1}$ and $\mathbb{E}Y = \dfrac{\partial g}{\partial t}\Big|_{s=t=1}$;
7. if $\mathbb{E}X^2, \mathbb{E}Y^2 < \infty$, then

$$
\mathbb{E}X^2 = \frac{\partial^2 g}{\partial s^2}\Big|_{s=t=1} + \frac{\partial g}{\partial s}\Big|_{s=t=1}, \quad \mathbb{E}Y^2 = \frac{\partial^2 g}{\partial t^2}\Big|_{s=t=1} + \frac{\partial g}{\partial t}\Big|_{s=t=1}, \quad \mathbb{E}(XY) = \frac{\partial^2 g}{\partial s\, \partial t}\Big|_{s=t=1}.
$$

In item 3, the "if" direction follows directly from independence; for the "only if" direction, note that the coefficients of the product $g_X(s) g_Y(t)$ are $\mathbb{P}(X = i)\mathbb{P}(Y = k)$, and by item 5 equal generating functions give equal joint mass functions.

## 11.2. Moment Generating Functions

Probability generating functions apply only to nonnegative integer-valued random variables. Replacing $s^X$ by $\mathrm{e}^{sX}$ (that is, setting $s = \mathrm{e}^u$) yields the moment generating function, which applies to general random variables.

**Definition 11.2.1 (Moment Generating Function)** For a random variable $X$, the function

$$
M_X(s) = \mathbb{E}(\mathrm{e}^{sX})
$$
is called the **moment generating function** (MGF) of $X$. In the discrete case $M_X(s) = \sum_j \mathrm{e}^{s x_j}\, \mathbb{P}(X = x_j)$, and in the continuous case $M_X(s) = \int_{-\infty}^{\infty} \mathrm{e}^{sx} f_X(x)\,\mathrm{d}x$. We say that $M_X(s)$ exists at $s$ only if $\mathbb{E}(\mathrm{e}^{sX}) < \infty$.

$M_X(0) = 1$ always exists, but for $s \ne 0$ the value may be $+\infty$. The name comes from the following observation: if $M_X$ exists in a neighborhood of $0$, the Taylor expansion of $\mathrm{e}^x$ gives

$$
M_X(s) = \mathbb{E} \sum_{n=0}^{\infty} \frac{(sX)^n}{n!} = \sum_{n=0}^{\infty} \frac{\mathbb{E}X^n}{n!} s^n,
$$
so the moments are exactly the coefficients of the expansion (multiplied by $n!$).

**Property 11.2.1** Let $M(s)$ be the moment generating function of $X$ and $M^{(k)}(s)$ its $k$-th derivative. Then

1. $Y = aX + b$ has moment generating function $M_Y(s) = \mathrm{e}^{sb} M(sa)$;
2. if $M(s)$ exists in a neighborhood of $0$, then $\mathbb{E}X^k = M^{(k)}(0)$, $k = 1, 2, \dots$;
3. $M(0) = 1$, and if $X$ takes only nonnegative integer values, then $\mathbb{P}(X = 0) = \lim_{s \to -\infty} M(s)$;
4. uniqueness: if there is $a > 0$ such that $M(s) < \infty$ for all $s \in [-a, a]$, then $M(s)$ uniquely determines the distribution function of $X$;
5. if $X_1, \dots, X_n$ are independent, then $Y = X_1 + \cdots + X_n$ has moment generating function $M_Y(s) = M_{X_1}(s) \cdots M_{X_n}(s)$.

Item 3: if $X$ takes nonnegative integer values, $M(s) = \sum_k \mathrm{e}^{sk} \mathbb{P}(X = k)$, and as $s \to -\infty$ every term except the one with $k = 0$ tends to $0$. The proof of item 4 is beyond the scope of this course; note that it requires the moment generating function to be finite in a neighborhood of $0$, and finiteness at $s = 0$ alone is not enough.

**Example 11.2.1** A discrete random variable $X$ takes the values $2, 3, 5$ with probabilities $\frac{1}{2}, \frac{1}{6}, \frac{1}{3}$. Find $M(s)$, $\mathbb{E}X$ and $\mathbb{E}X^2$.

**Solution** $M(s) = \frac{1}{2}\mathrm{e}^{2s} + \frac{1}{6}\mathrm{e}^{3s} + \frac{1}{3}\mathrm{e}^{5s}$, so

$$
\mathbb{E}X = M^{(1)}(0) = \frac{1}{2} \cdot 2 + \frac{1}{6} \cdot 3 + \frac{1}{3} \cdot 5 = \frac{19}{6}, \qquad \mathbb{E}X^2 = M^{(2)}(0) = \frac{1}{2} \cdot 4 + \frac{1}{6} \cdot 9 + \frac{1}{3} \cdot 25 = \frac{71}{6}.
$$

**Example 11.2.2 (Exponential Distribution)** Let $X \sim \mathrm{Exp}(\lambda)$ with density $f(x) = \lambda \mathrm{e}^{-\lambda x}\boldsymbol{1}_{\{x \ge 0\}}$. For $s < \lambda$,

$$
M(s) = \lambda \int_0^{\infty} \mathrm{e}^{sx} \mathrm{e}^{-\lambda x}\,\mathrm{d}x = \frac{\lambda}{\lambda - s} = \left(1 - \frac{s}{\lambda}\right)^{-1},
$$
while for $s \ge \lambda$ the integral is $+\infty$. Hence $\mathbb{E}X = M^{(1)}(0) = \frac{\lambda}{(\lambda - s)^2}\big|_{s=0} = \frac{1}{\lambda}$ and $\mathbb{E}X^2 = M^{(2)}(0) = \frac{2\lambda}{(\lambda - s)^3}\big|_{s=0} = \frac{2}{\lambda^2}$. Alternatively, expanding $(1 - s/\lambda)^{-1} = \sum_n s^n/\lambda^n$ gives $\mathbb{E}X^n = n!/\lambda^n$ directly.

**Example 11.2.3 (A Mixture Distribution)** A bank has three tellers whose service times are exponentially distributed: two fast tellers with parameter $\lambda = 6$ and one slow teller with parameter $\lambda = 4$. A customer chooses one of the tellers at random with equal probability. Find the moment generating function of the service time.

**Solution** By the law of total probability, the service time $X$ has density $f_X(x) = \left[\frac{2}{3} \cdot 6\mathrm{e}^{-6x} + \frac{1}{3} \cdot 4\mathrm{e}^{-4x}\right] \boldsymbol{1}_{\{x \ge 0\}}$. For $s < 4$,

$$
M_X(s) = \int_0^{\infty} \mathrm{e}^{sx} \left[\frac{2}{3} \cdot 6\mathrm{e}^{-6x} + \frac{1}{3} \cdot 4\mathrm{e}^{-4x}\right] \mathrm{d}x = \frac{2}{3} \cdot \frac{6}{6 - s} + \frac{1}{3} \cdot \frac{4}{4 - s}.
$$
Conversely, by uniqueness, if the moment generating function of $X$ has the form $p_1 \frac{\lambda_1}{\lambda_1 - s} + p_2 \frac{\lambda_2}{\lambda_2 - s}$ with $p_1 + p_2 = 1$, then $X$ is the mixture of $\mathrm{Exp}(\lambda_1)$ and $\mathrm{Exp}(\lambda_2)$ with weights $p_1, p_2$, and its density is $p_1 f_{X_1}(x) + p_2 f_{X_2}(x)$.

**Example 11.2.4 (Normal Distribution)** Let $X \sim \mathcal{N}(\mu_1, \sigma_1^2)$ and $Y \sim \mathcal{N}(\mu_2, \sigma_2^2)$ be independent. Find the distribution of $Z = X + Y$.

**Solution** If $V \sim \mathcal{N}(0, 1)$, completing the square gives

$$
M_V(s) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \mathrm{e}^{sx - x^2/2}\,\mathrm{d}x = \mathrm{e}^{s^2/2} \cdot \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \mathrm{e}^{-(x - s)^2/2}\,\mathrm{d}x = \mathrm{e}^{s^2/2}.
$$
Since $W = \mu + \sigma V \sim \mathcal{N}(\mu, \sigma^2)$, item 1 of Property 11.2.1 gives $M_W(s) = \mathrm{e}^{\mu s + \sigma^2 s^2/2}$. Then by item 5,

$$
M_Z(s) = M_X(s) M_Y(s) = \exp\left\{(\mu_1 + \mu_2)s + \frac{(\sigma_1^2 + \sigma_2^2)s^2}{2}\right\},
$$
which is finite for all $s$ and is the moment generating function of $\mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$. By item 4, $Z \sim \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$: a sum of independent normal random variables is again normal.

As a by-product we obtain all moments of the standard normal distribution: $M_V(s) = \mathrm{e}^{s^2/2} = \sum_{k=0}^{\infty} \frac{s^{2k}}{2^k k!}$, and comparing coefficients with $\sum_n \frac{\mathbb{E}V^n}{n!} s^n$ gives $\mathbb{E}V^{2k-1} = 0$ and $\mathbb{E}V^{2k} = \frac{(2k)!}{2^k k!} = (2k-1)!!$. For example, $\mathbb{E}V^4 = 3$.

### 11.2.1. Sums of a Random Number of Random Variables

**Theorem 11.2.1** Let $X_1, X_2, \dots$ be i.i.d. with common moment generating function $M_X(s)$, let $N$ be a positive integer-valued random variable independent of $\{X_j\}$, and let $W = X_1 + \cdots + X_N$. Then

$$
M_W(s) = \mathbb{E}\left[(M_X(s))^N\right] = \sum_{n=1}^{\infty} (M_X(s))^n\, \mathbb{P}(N = n).
$$

**Proof** By independence, $\mathbb{E}(\mathrm{e}^{sW} \mid N = n) = \mathbb{E}(\mathrm{e}^{sX_1} \cdots \mathrm{e}^{sX_n}) = (M_X(s))^n$, and by the law of iterated expectations (Theorem 9.3.1), $M_W(s) = \mathbb{E}[\mathbb{E}(\mathrm{e}^{sW} \mid N)] = \mathbb{E}[(M_X(s))^N]$. $\square$

Compare with $M_N(s) = \sum_n (\mathrm{e}^s)^n \mathbb{P}(N = n)$: $M_W$ is obtained from $M_N$ by replacing $\mathrm{e}^s$ with $M_X(s)$. This is the same statement as "replace $s$ in $g_N$ by $g_X(s)$" in Theorem 11.1.1.

**Example 11.2.5** Xiao Ming walks along a street full of bookstores looking for a certain book. Each store has the book with probability $p$, independently of the others; the time he spends in each store is $\mathrm{Exp}(\lambda)$, independent of everything else; and he keeps going until he finds the book. Find the distribution of the total time $W$ spent in bookstores.

**Solution** The number of stores visited is $N \sim \mathrm{Geo}(p)$, the time spent in each store is $X_i \sim \mathrm{Exp}(\lambda)$, and $W = X_1 + \cdots + X_N$. For $s < \lambda$, $M_X(s) = \frac{\lambda}{\lambda - s}$, while $M_N(s) = \frac{p\mathrm{e}^s}{1 - (1 - p)\mathrm{e}^s}$, so

$$
M_W(s) = \frac{p M_X(s)}{1 - (1 - p) M_X(s)} = \frac{p\lambda}{p\lambda - s}, \quad s < p\lambda,
$$
that is, $W \sim \mathrm{Exp}(p\lambda)$. By contrast, a sum $X_1 + \cdots + X_n$ with a fixed number of terms has moment generating function $\left(\frac{\lambda}{\lambda - s}\right)^n$ and follows $\Gamma(n, \lambda)$.

### 11.2.2. Moment Generating Functions of Random Vectors; Limitations

**Definition 11.2.2** Let $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ be a random vector. The function

$$
M_{\boldsymbol{X}}(\boldsymbol{s}) = \mathbb{E}\left(\mathrm{e}^{\boldsymbol{s}^{\mathsf T}\boldsymbol{X}}\right) = \mathbb{E}\left(\mathrm{e}^{s_1 X_1 + \cdots + s_n X_n}\right), \quad \boldsymbol{s} = (s_1, \dots, s_n)^{\mathsf T} \in \mathbb{R}^n
$$
is called the (multivariate) moment generating function of $\boldsymbol{X}$.

The limitation of moment generating functions is that they may fail to exist. For the standard Cauchy distribution (density $\frac{1}{\pi(1 + x^2)}$) and any $s > 0$,

$$
\mathbb{E}\mathrm{e}^{sX} = \int_{-\infty}^{\infty} \frac{\mathrm{e}^{sx}}{\pi(1 + x^2)}\,\mathrm{d}x \ge \int_0^{\infty} \frac{\mathrm{e}^{sx}}{\pi(1 + x^2)}\,\mathrm{d}x = +\infty,
$$
because the integrand tends to infinity as $x \to +\infty$; the case $s < 0$ is similar. So the moment generating function of the Cauchy distribution is finite only at $s = 0$, and neither the uniqueness property nor the computation of moments in Property 11.2.1 is available.

**Remark 11.2.1** Two points about moments and moment generating functions are easily misunderstood.

- All moments may exist while the moment generating function does not. For example, if $X \sim \mathcal{N}(\mu, \sigma^2)$, then $Y = \mathrm{e}^X$ (the lognormal distribution) has finite moments $\mathbb{E}Y^n = \mathrm{e}^{n\mu + n^2\sigma^2/2}$ of all orders, but $\mathbb{E}\mathrm{e}^{sY} = +\infty$ for every $s > 0$.
- Two random variables may have identical moments of all orders and still have different distributions. For example, let $X_1$ have density $f_1(x) = \frac{1}{\sqrt{2\pi}\,x} \mathrm{e}^{-(\ln x)^2/2}\boldsymbol{1}_{\{x > 0\}}$ (standard lognormal) and $X_2$ have density $f_2(x) = f_1(x)[1 + \sin(2\pi \ln x)]$; all their moments coincide, but their distributions differ. The moment sequence determines the distribution only when the moment generating function exists in a neighborhood of $0$.

## 11.3. Characteristic Functions

Replacing the real number $s$ in the moment generating function by the purely imaginary number $\mathrm{i}t$ makes the integrand $\mathrm{e}^{\mathrm{i}tX}$ have modulus $1$, so the expectation exists for every random variable and every $t$. This is the characteristic function, the most widely applicable of the three tools.

**Definition 11.3.1 (Characteristic Function)** For a random variable $X$, the function

$$
\varphi(t) = \mathbb{E}(\mathrm{e}^{\mathrm{i}tX}) = \mathbb{E}\cos(tX) + \mathrm{i}\,\mathbb{E}\sin(tX), \quad t \in \mathbb{R}
$$
is called the **characteristic function** (CF) of $X$, where $\mathrm{i} = \sqrt{-1}$.

If $X$ has density $f$, then $\varphi(t) = \int_{-\infty}^{\infty} \mathrm{e}^{\mathrm{i}tx} f(x)\,\mathrm{d}x$, the Fourier transform of the density (up to a sign convention).

**Property 11.3.1** Let $\varphi(t) = \mathbb{E}(\mathrm{e}^{\mathrm{i}tX})$. Then

1. $\lvert \varphi(t) \rvert \le \varphi(0) = 1$ and $\varphi(-t) = \overline{\varphi(t)}$;
2. $\varphi(t)$ is uniformly continuous on $(-\infty, \infty)$: $\lvert \varphi(t + h) - \varphi(t) \rvert \le \mathbb{E}\lvert \mathrm{e}^{\mathrm{i}hX} - 1 \rvert$, where the right-hand side does not depend on $t$ and tends to $0$ as $h \to 0$;
3. if $\mathbb{E}\lvert X \rvert^k < \infty$, then $\varphi^{(k)}(t) = \mathrm{i}^k \mathbb{E}(X^k \mathrm{e}^{\mathrm{i}tX})$, and in particular $\varphi^{(k)}(0) = \mathrm{i}^k \mathbb{E}X^k$;
4. for constants $a, b$, $\varphi_{aX + b}(t) = \mathrm{e}^{\mathrm{i}tb} \varphi_X(at)$;
5. if $X_k$ has characteristic function $\varphi_k(t)$ and $X_1, \dots, X_n$ are independent, then $Y = X_1 + \cdots + X_n$ has characteristic function $\varphi_Y(t) = \prod_{k=1}^{n} \varphi_k(t)$.

Item 1 follows from $\lvert \mathrm{e}^{\mathrm{i}tX} \rvert = 1$ and $\mathrm{e}^{-\mathrm{i}tX} = \overline{\mathrm{e}^{\mathrm{i}tX}}$. Item 2: $\lvert \mathrm{e}^{\mathrm{i}(t+h)X} - \mathrm{e}^{\mathrm{i}tX} \rvert = \lvert \mathrm{e}^{\mathrm{i}hX} - 1 \rvert \le 2$, so by the dominated convergence theorem the expectation tends to $0$ as $h \to 0$. Item 3 is differentiation under the expectation, justified by the integrability of $\lvert X^k \mathrm{e}^{\mathrm{i}tX} \rvert = \lvert X \rvert^k$.

### 11.3.1. Characteristic Functions of Common Distributions

**Example 11.3.1 (Binomial Distribution)** For $X \sim \mathrm{Bin}(n, p)$: $\varphi(t) = \sum_{j=0}^{n} \mathrm{e}^{\mathrm{i}tj} \binom{n}{j} p^j q^{n-j} = (q + p\mathrm{e}^{\mathrm{i}t})^n$.

**Example 11.3.2 (Poisson Distribution)** For $X \sim \mathrm{Poi}(\lambda)$: $\varphi(t) = \sum_{k=0}^{\infty} \mathrm{e}^{\mathrm{i}tk} \frac{\lambda^k}{k!} \mathrm{e}^{-\lambda} = \mathrm{e}^{\lambda(\mathrm{e}^{\mathrm{i}t} - 1)}$.

**Example 11.3.3 (Geometric Distribution)** For $X \sim \mathrm{Geo}(p)$: $\varphi(t) = \sum_{k=1}^{\infty} \mathrm{e}^{\mathrm{i}tk} p q^{k-1} = \dfrac{p\mathrm{e}^{\mathrm{i}t}}{1 - q\mathrm{e}^{\mathrm{i}t}}$.

**Example 11.3.4 (Uniform Distribution)** For $X \sim \mathrm{U}(a, b)$: $\varphi(t) = \dfrac{\mathrm{e}^{\mathrm{i}tb} - \mathrm{e}^{\mathrm{i}ta}}{\mathrm{i}t(b - a)}$ ($t \ne 0$). In particular, the characteristic function of $\mathrm{U}(-c, c)$ is $\dfrac{\sin(ct)}{ct}$.

**Example 11.3.5 (Exponential Distribution)** For $X \sim \mathrm{Exp}(\lambda)$: $\varphi(t) = \left(1 - \dfrac{\mathrm{i}t}{\lambda}\right)^{-1}$. Compared with the moment generating function $(1 - s/\lambda)^{-1}$ of Example 11.2.2, it is formally obtained by replacing $s$ with $\mathrm{i}t$.

**Example 11.3.6 (Normal Distribution)** The characteristic function of $X \sim \mathcal{N}(\mu, \sigma^2)$ is

$$
\varphi(t) = \exp\left(\mathrm{i}\mu t - \frac{1}{2}\sigma^2 t^2\right).
$$

**Solution** (i) First consider $\mathcal{N}(0, 1)$. Formally treating $\mathrm{i}$ as a constant and completing the square, $\varphi(t) = \mathrm{e}^{-t^2/2} \cdot \frac{1}{\sqrt{2\pi}} \int \mathrm{e}^{-(x - \mathrm{i}t)^2/2}\,\mathrm{d}x = \mathrm{e}^{-t^2/2}$; making this step rigorous requires contour integration from complex analysis. Here is a derivation that uses only real analysis. By symmetry,

$$
\varphi(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \cos(tx)\, \mathrm{e}^{-x^2/2}\,\mathrm{d}x,
$$
and differentiating under the integral sign and integrating by parts,

$$
\varphi'(t) = -\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x \sin(tx)\, \mathrm{e}^{-x^2/2}\,\mathrm{d}x = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \sin(tx)\,\mathrm{d}\mathrm{e}^{-x^2/2} = -\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} t\cos(tx)\, \mathrm{e}^{-x^2/2}\,\mathrm{d}x = -t\varphi(t).
$$
Hence $\frac{\mathrm{d}}{\mathrm{d}t}\left[\varphi(t)\mathrm{e}^{t^2/2}\right] = [\varphi'(t) + t\varphi(t)]\mathrm{e}^{t^2/2} = 0$, so $\varphi(t)\mathrm{e}^{t^2/2} \equiv \varphi(0) = 1$, i.e., $\varphi(t) = \mathrm{e}^{-t^2/2}$.

(ii) Let $Y \sim \mathcal{N}(\mu, \sigma^2)$. Then $Y = \mu + \sigma X$ with $X \sim \mathcal{N}(0, 1)$, and item 4 of Property 11.3.1 gives $\mathbb{E}\mathrm{e}^{\mathrm{i}tY} = \mathrm{e}^{\mathrm{i}t\mu} \mathbb{E}\mathrm{e}^{\mathrm{i}t\sigma X} = \exp\left(\mathrm{i}\mu t - \frac{1}{2}\sigma^2 t^2\right)$. $\square$

By item 5, if $X_1, \dots, X_m$ are independent with $X_j \sim \mathcal{N}(\mu_j, \sigma_j^2)$, then $X_1 + \cdots + X_m \sim \mathcal{N}\left(\sum_j \mu_j, \sum_j \sigma_j^2\right)$.

The next two computations require complex analysis or rather involved integration techniques; the results may be used without proof.

**Example 11.3.7 (Cauchy Distribution)** The characteristic function of the standard Cauchy distribution (density $f(x) = \frac{1}{\pi(1 + x^2)}$, $x \in \mathbb{R}$) is $\varphi(t) = \mathrm{e}^{-\lvert t \rvert}$. It is not differentiable at $t = 0$, consistent with the fact that the Cauchy distribution has no expectation.

**Example 11.3.8 (Laplace Distribution)** The characteristic function of the Laplace distribution with density $f(x) = \frac{1}{2}\mathrm{e}^{-\lvert x \rvert}$ is $\varphi(t) = \dfrac{1}{1 + t^2}$.

Examples 11.3.7 and 11.3.8 are dual to each other: the Fourier transform of the Laplace density is a Cauchy-type function, and vice versa.

![Characteristic functions of several symmetric distributions: N(0,1), U(-1,1), Laplace and standard Cauchy; the characteristic function of a symmetric distribution is real and even](./plots/characteristic-functions.py)

The three transforms are compared below ($q = 1 - p$; "—" means not applicable or nonexistent):

| Distribution | PGF $g(s)$ | MGF $M(s)$ | CF $\varphi(t)$ |
|---|---|---|---|
| $\mathrm{Bin}(n, p)$ | $(q + ps)^n$ | $(q + p\mathrm{e}^s)^n$ | $(q + p\mathrm{e}^{\mathrm{i}t})^n$ |
| $\mathrm{Poi}(\lambda)$ | $\mathrm{e}^{\lambda(s - 1)}$ | $\mathrm{e}^{\lambda(\mathrm{e}^s - 1)}$ | $\mathrm{e}^{\lambda(\mathrm{e}^{\mathrm{i}t} - 1)}$ |
| $\mathrm{Geo}(p)$ | $\dfrac{ps}{1 - qs}$ | $\dfrac{p\mathrm{e}^s}{1 - q\mathrm{e}^s}$, $s < -\ln q$ | $\dfrac{p\mathrm{e}^{\mathrm{i}t}}{1 - q\mathrm{e}^{\mathrm{i}t}}$ |
| $\mathrm{U}(a, b)$ | — | $\dfrac{\mathrm{e}^{sb} - \mathrm{e}^{sa}}{s(b - a)}$ | $\dfrac{\mathrm{e}^{\mathrm{i}tb} - \mathrm{e}^{\mathrm{i}ta}}{\mathrm{i}t(b - a)}$ |
| $\mathrm{Exp}(\lambda)$ | — | $\dfrac{\lambda}{\lambda - s}$, $s < \lambda$ | $\left(1 - \dfrac{\mathrm{i}t}{\lambda}\right)^{-1}$ |
| $\mathcal{N}(\mu, \sigma^2)$ | — | $\mathrm{e}^{\mu s + \sigma^2 s^2/2}$ | $\mathrm{e}^{\mathrm{i}\mu t - \sigma^2 t^2/2}$ |
| Standard Cauchy | — | — (finite only at $s = 0$) | $\mathrm{e}^{-\lvert t \rvert}$ |

### 11.3.2. Characteristic Functions and Distribution Functions

The characteristic function can stand in for the distribution function because the two determine each other, and the distribution function can be recovered explicitly from the characteristic function.

**Theorem 11.3.1 (Inversion Formula)** Let $\varphi(t)$ be the characteristic function and $F(x)$ the distribution function of $X$. If $F$ is continuous at $a$ and $b$ ($a < b$), then

$$
F(b) - F(a) = \frac{1}{2\pi} \lim_{T \to \infty} \int_{-T}^{T} \frac{\mathrm{e}^{-\mathrm{i}ta} - \mathrm{e}^{-\mathrm{i}tb}}{\mathrm{i}t} \varphi(t)\,\mathrm{d}t.
$$

**Corollary 11.3.1 (Uniqueness Theorem)** The characteristic function and the distribution function of a random variable determine each other uniquely: two random variables have the same characteristic function if and only if they have the same distribution.

**Proof** That the distribution function determines the characteristic function is the definition itself. Conversely, the continuity points of $F$ are dense in $\mathbb{R}$ (there are at most countably many discontinuities), and by Theorem 11.3.1, $\varphi$ determines the difference of $F$ at any two continuity points. Letting $a \to -\infty$ through continuity points gives $F(b)$ at every continuity point $b$, and right continuity then gives $F$ everywhere. $\square$

**Theorem 11.3.2** If the characteristic function of $X$ satisfies $\int_{\mathbb{R}} \lvert \varphi(t) \rvert\,\mathrm{d}t < \infty$, then $X$ has a continuous density

$$
f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \mathrm{e}^{-\mathrm{i}tx} \varphi(t)\,\mathrm{d}t.
$$

This is the probabilistic version of the **Fourier inversion theorem**. For example, $\int \mathrm{e}^{-\lvert t \rvert}\,\mathrm{d}t < \infty$ and Example 11.3.7 allow one to verify the Cauchy density; conversely, the characteristic function $\frac{1}{1 + t^2}$ of the Laplace distribution yields the characteristic function of the Cauchy distribution. The proofs of these two theorems require a fair amount of analysis and are not required here; what matters is the conclusion of Corollary 11.3.1: once we compute the characteristic function of a random variable and recognize the distribution it belongs to, the distribution of that random variable is determined.

### 11.3.3. Characteristic Functions and Moments

**Theorem 11.3.3** If $\mathbb{E}\lvert X \rvert^n < \infty$, then the characteristic function of $X$ satisfies

$$
\varphi(t) = \sum_{m=0}^{n} \frac{\mathbb{E}[(\mathrm{i}tX)^m]}{m!} + o(t^n), \quad t \to 0.
$$
In particular, if $\mathbb{E}X^2 < \infty$, then

$$
\varphi(t) = 1 + \mathrm{i}t\,\mathbb{E}X - \frac{1}{2}t^2\,\mathbb{E}X^2 + o(t^2). \tag{11.1}
$$

This combines item 3 of Property 11.3.1 with Taylor's formula. Note that $\mathbb{E}\lvert X \rvert^n < \infty$ implies that all lower moments are finite: by **Jensen's inequality** (or by $\lvert x \rvert^m \le 1 + \lvert x \rvert^n$ for $m \le n$), the existence of a higher moment implies that of the lower ones. Eq. (11.1) is the starting point of the proof of the central limit theorem ([3.1.13](/3.1.13)).

### 11.3.4. Mixture Distributions and Characteristic Functions of Random Vectors

**Theorem 11.3.4 (Mixture Distributions)** Let the distribution functions $F_1(x), \dots, F_m(x)$ have characteristic functions $\varphi_1(t), \dots, \varphi_m(t)$, and let $\lambda_k \ge 0$ with $\sum_{k=1}^{m} \lambda_k = 1$. Then the mixture distribution $\sum_{k=1}^{m} \lambda_k F_k$ has characteristic function $\sum_{k=1}^{m} \lambda_k \varphi_k(t)$.

For an example of a mixture, see Example 11.2.3. Note that $Y \sim \sum_k \lambda_k F_k$ means "$Y$ takes, with probability $\lambda_k$, the value of $X_k$, whose distribution is $F_k$"; no independence among $X_1, \dots, X_m$ is required, and $Y$ is in general not the linear combination $\sum_k \lambda_k X_k$.

**Definition 11.3.2** Let $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ be a random vector. The function

$$
\varphi(\boldsymbol{t}) = \mathbb{E}\left(\mathrm{e}^{\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{X}}\right), \quad \boldsymbol{t} = (t_1, \dots, t_n)^{\mathsf T} \in \mathbb{R}^n
$$
is called the characteristic function of $\boldsymbol{X}$.

As in one dimension, the characteristic function of a random vector and its joint distribution function determine each other uniquely. This yields a characteristic-function criterion for independence.

**Theorem 11.3.5** Let $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ be a random vector and $\varphi_k(t_k)$ the characteristic function of $X_k$. Then $X_1, \dots, X_n$ are independent if and only if

$$
\varphi(\boldsymbol{t}) = \varphi_1(t_1) \varphi_2(t_2) \cdots \varphi_n(t_n), \quad \boldsymbol{t} \in \mathbb{R}^n.
$$

**Proof** Necessity: $\mathrm{e}^{\mathrm{i}t_1 X_1}, \dots, \mathrm{e}^{\mathrm{i}t_n X_n}$ are independent, so the expectation of their product is the product of their expectations. Sufficiency: take independent $Y_1, \dots, Y_n$ with $Y_k$ distributed as $X_k$. Then $(Y_1, \dots, Y_n)$ also has characteristic function $\prod_k \varphi_k(t_k)$, so by uniqueness $\boldsymbol{X}$ and $(Y_1, \dots, Y_n)^{\mathsf T}$ have the same distribution, and therefore $X_1, \dots, X_n$ are independent. $\square$

**Example 11.3.9** Let $X$ have the standard Cauchy distribution and $Y = aX$ with $a > 0$. Then $\varphi_{X+Y}(t) = \varphi_X(t)\varphi_Y(t)$, yet $X$ and $Y$ are not independent.

**Solution** $\varphi_X(t) = \mathrm{e}^{-\lvert t \rvert}$, $\varphi_Y(t) = \mathbb{E}\mathrm{e}^{\mathrm{i}(at)X} = \mathrm{e}^{-a\lvert t \rvert}$, and $\varphi_{X+Y}(t) = \mathbb{E}\mathrm{e}^{\mathrm{i}t(1 + a)X} = \mathrm{e}^{-(1 + a)\lvert t \rvert} = \varphi_X(t)\varphi_Y(t)$.

The example shows that the characteristic function of a sum being the product of the characteristic functions does not imply independence; to decide independence one must use the joint characteristic function $\varphi(t_1, t_2)$ of Theorem 11.3.5.

We now have three sets of tools, each of which captures all the information about a random variable: for discrete random variables, the mass function, the distribution function and the characteristic function; for continuous random variables, the density, the distribution function and the characteristic function; for general random variables, the distribution function and the characteristic function. Correspondingly, independence has three equivalent criteria.

**Corollary 11.3.2** Let the random vectors $\boldsymbol{X}_1$, $\boldsymbol{X}_2$ have joint distribution function, joint density (if it exists) and joint characteristic function $F(\boldsymbol{x}_1, \boldsymbol{x}_2)$, $f(\boldsymbol{x}_1, \boldsymbol{x}_2)$ and $\varphi(\boldsymbol{t}_1, \boldsymbol{t}_2)$, with marginal distribution functions, densities and characteristic functions $F_i$, $f_i$, $\varphi_i$. Then $\boldsymbol{X}_1$ and $\boldsymbol{X}_2$ are independent if and only if any one of the following holds:

1. $F(\boldsymbol{x}_1, \boldsymbol{x}_2) = F_1(\boldsymbol{x}_1) F_2(\boldsymbol{x}_2)$;
2. $f(\boldsymbol{x}_1, \boldsymbol{x}_2) = f_1(\boldsymbol{x}_1) f_2(\boldsymbol{x}_2)$ (continuous case);
3. $\varphi(\boldsymbol{t}_1, \boldsymbol{t}_2) = \varphi_1(\boldsymbol{t}_1) \varphi_2(\boldsymbol{t}_2)$.

### 11.3.5. Characteristic Functions and Convergence in Distribution

Another important use of characteristic functions is to decide whether the distributions of a sequence of random variables converge. We first define convergence in distribution, which is discussed in detail in [3.1.13](/3.1.13) and [3.1.14](/3.1.14).

**Definition 11.3.3 (Convergence in Distribution)** Let $X$ have distribution function $F(x)$ and $X_n$ have distribution function $F_n(x)$. If

$$
\lim_{n \to \infty} F_n(x) = F(x)
$$
at every continuity point $x$ of $F(x)$, we say that $X_n$ converges to $X$ in distribution (**convergence in distribution**), written $X_n \xrightarrow{d} X$; we also say that $F_n$ converges weakly to $F$ (**weak convergence**), written $F_n \xrightarrow{w} F$.

Convergence is required only at continuity points of $F$ because requiring it at jump points would be too strict: $X_n \equiv 1/n$ should "converge" to $X \equiv 0$, yet $F_n(0) = 0 \not\to F(0) = 1$.

**Theorem 11.3.6 (Continuity Theorem)** Let $X_n$ have characteristic function $\varphi_n(t)$ and $X$ have characteristic function $\varphi(t)$. Then $X_n \xrightarrow{d} X$ if and only if

$$
\lim_{n \to \infty} \varphi_n(t) = \varphi(t), \quad \forall t \in \mathbb{R}.
$$

This is one of the most frequently used and most important theorems of probability theory: to prove convergence in distribution it suffices to prove pointwise convergence of characteristic functions, and since the characteristic function of an independent sum is a product, this is far easier than working with distribution functions. There is also a version that does not require the limiting distribution to be known in advance.

**Theorem 11.3.7** If the characteristic functions $\varphi_n(\boldsymbol{t})$ of random vectors $\boldsymbol{X}_n$ converge pointwise to a function $\varphi(\boldsymbol{t})$ that is continuous at $\boldsymbol{t} = \boldsymbol{0}$, then $\varphi(\boldsymbol{t})$ is the characteristic function of some random vector $\boldsymbol{X}$, and $\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_n \xrightarrow{d} \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ for every constant vector $\boldsymbol{a}$ of the same dimension as $\boldsymbol{X}$.

This theorem links the multivariate and the univariate cases; its consequences and applications are in [3.1.14](/3.1.14). When the uniqueness condition (item 4 of Property 11.2.1) holds, probability generating functions and moment generating functions can also replace characteristic functions in the continuity theorem.

## Summary

The three transforms compared ($X_1, X_2, \dots$ independent; in random sums the $\{X_i\}$ are i.i.d. and independent of $N$):

| | Probability generating function | Moment generating function | Characteristic function |
|---|---|---|---|
| Definition | $g(s) = \mathbb{E}s^X = \sum_k p_k s^k$ | $M(s) = \mathbb{E}\mathrm{e}^{sX} = \sum_n \frac{\mathbb{E}X^n}{n!}s^n$ | $\varphi(t) = \mathbb{E}\mathrm{e}^{\mathrm{i}tX} = \sum_n \frac{\mathbb{E}X^n}{n!}(\mathrm{i}t)^n$ |
| Scope | Nonnegative integer values | Random variables with $M$ finite near $0$ | All random variables |
| Uniqueness | One-to-one with the mass function | Determines the distribution if finite in a neighborhood of $0$ | One-to-one with the distribution function |
| Moments | $\mathbb{E}X = g'(1)$, $\mathbb{E}X(X-1) = g''(1)$ | $\mathbb{E}X^k = M^{(k)}(0)$ | $\mathbb{E}X^k = \varphi^{(k)}(0)/\mathrm{i}^k$ |
| Independent sum $\sum X_i$ | $\prod g_i(s)$ | $\prod M_i(s)$ | $\prod \varphi_i(t)$ |
| $aX + b$ | $s^b g(s^a)$ ($a, b$ nonnegative integers) | $\mathrm{e}^{sb}M(as)$ | $\mathrm{e}^{\mathrm{i}tb}\varphi(at)$ |
| Random sum $X_1 + \cdots + X_N$ | $g_N(g_X(s))$ | $\mathrm{e}^s \to M_X(s)$ in $M_N$ | $\mathrm{e}^{\mathrm{i}t} \to \varphi_X(t)$ in $\varphi_N$ |
| Two dimensions | $\mathbb{E}(s^X t^Y)$ | $\mathbb{E}(\mathrm{e}^{sX + tY})$ | $\mathbb{E}(\mathrm{e}^{\mathrm{i}t_1X + \mathrm{i}t_2Y})$ |

The basic strategy with these tools is: from known transforms (such as $g_X$ and $g_N$), obtain the transform of the unknown random variable by products or compositions; then, by uniqueness, read off the mass function by differentiation or Taylor expansion, or recognize the distribution and its parameters directly from the form of the transform. In solving problems, choose the simplest tool that does the job: probability generating functions for nonnegative integer-valued problems, moment generating functions for moments when they exist, and characteristic functions in general and for limit problems.
