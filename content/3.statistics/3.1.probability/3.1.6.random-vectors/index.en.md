---
title: Distributions of Random Vectors
source_hash: 2d2d537b3953
---

The previous chapters studied a single random variable: its distribution is fully described by its distribution function and computed with a probability mass function in the discrete case and a density in the continuous case ([3.1.4](/3.1.4), [3.1.5](/3.1.5)). In practice we often observe several quantities in the same experiment, such as the height and weight of a person or the scores of two dice. Knowing the distribution of each quantity separately is then not enough; we also need to know how they vary together. This chapter extends distribution functions, mass functions and densities to random vectors. We first define joint and marginal distributions, then treat discrete and continuous random vectors in turn and give criteria for independence; next we introduce the most important continuous random vector, the bivariate normal distribution; finally we define conditional distributions, which describe the distribution of one component when the value of another is known. Two contrasts run through the chapter: the whole versus the part (joint versus marginal), and the passage between distribution functions on one side and mass functions and densities on the other. The chapter is the basis for functions of random vectors ([3.1.7](/3.1.7)), conditional expectation ([3.1.9](/3.1.9)), covariance ([3.1.10](/3.1.10)) and the multivariate normal distribution ([3.1.15](/3.1.15)).

## 6.1. Random Vectors and Joint Distributions

**Definition 6.1.1 (Random Vector)** If $X_1, \dots, X_n$ are random variables on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$, then $\boldsymbol{X} = (X_1, \dots, X_n)$ is called an $n$-dimensional **random vector** on $(\Omega, \mathcal{F}, \mathbb{P})$.

A random vector maps each sample point $\omega$ to the point $\boldsymbol{X}(\omega) = (X_1(\omega), \dots, X_n(\omega))$ of $\mathbb{R}^n$. For $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$ we write $\boldsymbol{x} \le \boldsymbol{y}$ to mean $x_j \le y_j$ for $j = 1, \dots, n$.

**Definition 6.1.2 (Joint Distribution Function)** Let $\boldsymbol{X} = (X_1, \dots, X_n)$ be a random vector. The function of $n$ variables on $\mathbb{R}^n$

$$
F(x_1, \dots, x_n) = \mathbb{P}(X_1 \le x_1, \dots, X_n \le x_n), \quad \text{i.e. } F(\boldsymbol{x}) = \mathbb{P}(\boldsymbol{X} \le \boldsymbol{x}),
$$
is called the **joint distribution function** of $\boldsymbol{X}$, or simply its distribution function or joint distribution.

As in one dimension, a joint distribution function is nondecreasing and right-continuous in each variable; $F \to 0$ when any one $x_j \to -\infty$, and $F \to 1$ when all $x_j \to +\infty$.

**Example 6.1.1** Let $F(x, y)$ be the joint distribution function of $(X, Y)$, and let $a < b$, $c < d$. For the rectangle $D = \{(x, y) \mid a < x \le b,\ c < y \le d\}$, adding and subtracting probabilities gives

$$
\mathbb{P}((X, Y) \in D) = \mathbb{P}(a < X \le b,\ c < Y \le d) = F(b, d) - F(b, c) - F(a, d) + F(a, c).
$$
A joint distribution function therefore also satisfies $F(b, d) - F(b, c) - F(a, d) + F(a, c) \ge 0$. This condition does not follow from monotonicity in each variable; it is specific to distribution functions of two or more variables.

**Definition 6.1.3 (Marginal Distribution)** Let $1 \le k < n$ and let $S_k = \{i_1, \dots, i_k\} \subset \{1, \dots, n\}$ be a set of indices. The joint distribution function of $\boldsymbol{X}_{S_k} = (X_{i_1}, \dots, X_{i_k})$,

$$
F_{S_k}(x_{i_1}, \dots, x_{i_k}) = \mathbb{P}(X_{i_1} \le x_{i_1}, \dots, X_{i_k} \le x_{i_k}) = \mathbb{P}(X_j \le x_j,\ j \in S_k;\ X_t < \infty,\ t \notin S_k)
$$
is called a $k$-dimensional **marginal distribution** of $F(x_1, \dots, x_n)$.

An $n$-dimensional distribution function has $2^n - 2$ marginal distributions. In two dimensions,

$$
F_X(x) = \mathbb{P}(X \le x, Y < \infty) = F(x, +\infty), \qquad F_Y(y) = F(+\infty, y).
$$
Thus a marginal distribution function is obtained from the joint distribution function simply by setting the unwanted components to $+\infty$; no integration is needed (integration is needed for densities, see §6.3).

**Remark 6.1.1** The joint distribution determines all marginal distributions, but not conversely: knowing the distributions of $X$ and $Y$ separately does not in general determine the joint distribution of $(X, Y)$. For example, let $X \sim \mathcal{N}(0,1)$ and take either $Y = X$ or $Y \sim \mathcal{N}(0,1)$ independent of $X$; the marginals are the same, but the joint distributions are completely different. The important case in which the marginals do determine the joint distribution is independence: by the definition in [3.1.3](/3.1.3), $X_1, \dots, X_n$ are independent if and only if

$$
F(x_1, \dots, x_n) = F_1(x_1) F_2(x_2) \cdots F_n(x_n), \quad \forall (x_1, \dots, x_n) \in \mathbb{R}^n,
$$
where $F_i$ is the distribution function of $X_i$. The next two sections restate this criterion in terms of mass functions and densities.

## 6.2. Discrete Random Vectors

### 6.2.1. Joint and Marginal Mass Functions

**Definition 6.2.1 (Discrete Random Vector)** If $X_1, \dots, X_n$ are all discrete random variables, $\boldsymbol{X} = (X_1, \dots, X_n)$ is called a **discrete random vector**. If the distinct values of $\boldsymbol{X}$ are

$$
\boldsymbol{x}(j_1, \dots, j_n) = (x_1(j_1), \dots, x_n(j_n)), \quad j_1, \dots, j_n \ge 1,
$$
then

$$
p_{j_1, \dots, j_n} = \mathbb{P}(\boldsymbol{X} = \boldsymbol{x}(j_1, \dots, j_n)), \quad j_1, \dots, j_n \ge 1
$$
is called the **joint probability mass function** of $\boldsymbol{X}$.

A joint mass function satisfies $p_{j_1, \dots, j_n} \ge 0$ and $\sum_{j_1, \dots, j_n} p_{j_1, \dots, j_n} = 1$. In two dimensions, when $p_{ij} = \mathbb{P}(X = x_i, Y = y_j)$ follows no simple formula, it is usually displayed as a table:

| $p_{ij}$ | $y_1$ | $y_2$ | $\cdots$ | $y_n$ | $\cdots$ | $p_i$ |
|---|---|---|---|---|---|---|
| $x_1$ | $p_{11}$ | $p_{12}$ | $\cdots$ | $p_{1n}$ | $\cdots$ | $p_1$ |
| $x_2$ | $p_{21}$ | $p_{22}$ | $\cdots$ | $p_{2n}$ | $\cdots$ | $p_2$ |
| $\vdots$ | $\vdots$ | $\vdots$ | | $\vdots$ | | $\vdots$ |
| $q_j$ | $q_1$ | $q_2$ | $\cdots$ | $q_n$ | $\cdots$ | $1$ |

Here $p_i = \sum_j p_{ij}$ is the row sum and $q_j = \sum_i p_{ij}$ the column sum. By countable additivity, $\{p_i\}$ and $\{q_j\}$ are the mass functions of $X$ and $Y$. For example, roll a red and a black fair four-sided die and let $X$ and $Y$ be their scores; then all 16 entries $p_{ij}$ equal $1/16$, and all row and column sums equal $1/4$.

**Definition 6.2.2 (Marginal Probability Mass Function)** Let the discrete random vector $\boldsymbol{X}$ have joint mass function $p_{j_1, \dots, j_n}$ and let $1 \le k < n$. Then

$$
\mathbb{P}(X_1 = x_1(j_1), \dots, X_k = x_k(j_k)) = \sum_{j_{k+1}, \dots, j_n} p_{j_1, \dots, j_n}, \quad j_1, \dots, j_k \ge 1
$$
is called the **marginal probability mass function** of $(X_1, \dots, X_k)$. The marginal mass function of any other group of components is obtained in the same way by summing over the remaining indices.

### 6.2.2. Criteria for Independence

**Theorem 6.2.1** Let the discrete random vector $\boldsymbol{X} = (X_1, \dots, X_n)$ have joint mass function $p_{j_1, \dots, j_n}$. Then $X_1, \dots, X_n$ are independent if and only if, for every $(x_1(j_1), \dots, x_n(j_n))$,

$$
\mathbb{P}(X_1 = x_1(j_1), \dots, X_n = x_n(j_n)) = \prod_{i=1}^n \mathbb{P}(X_i = x_i(j_i)).
$$

**Corollary 6.2.1** Let the distinct values of the discrete random vector $(X, Y)$ be $(x_i, y_j)$, $i, j \ge 1$. Then $X, Y$ are independent if and only if, for every $(x_i, y_j)$,

$$
\mathbb{P}(X = x_i, Y = y_j) = \mathbb{P}(X = x_i)\,\mathbb{P}(Y = y_j).
$$

**Proof** Sufficiency: for any $x, y \in \mathbb{R}$, by countable additivity of probability,

$$
\begin{aligned}
\mathbb{P}(X \le x, Y \le y) &= \sum_{i: x_i \le x} \sum_{j: y_j \le y} \mathbb{P}(X = x_i, Y = y_j) = \sum_{i: x_i \le x} \sum_{j: y_j \le y} \mathbb{P}(X = x_i)\,\mathbb{P}(Y = y_j) \\
&= \Big(\sum_{i: x_i \le x} \mathbb{P}(X = x_i)\Big)\Big(\sum_{j: y_j \le y} \mathbb{P}(Y = y_j)\Big) = \mathbb{P}(X \le x)\,\mathbb{P}(Y \le y).
\end{aligned}
$$
Necessity: the singletons $\{x_i\}$ and $\{y_j\}$ are Borel sets, so by the properties of independent random variables ([3.1.3](/3.1.3)) the events $\{X = x_i\}$ and $\{Y = y_j\}$ are independent, whence $\mathbb{P}(X = x_i, Y = y_j) = \mathbb{P}(X = x_i)\,\mathbb{P}(Y = y_j)$. One can also avoid this property: $\mathbb{P}(X = x_i, Y = y_j) = \lim_{h \downarrow 0} \mathbb{P}(x_i - h < X \le x_i,\ y_j - h < Y \le y_j)$, and the rectangle formula of Example 6.1.1 turns the product form of the joint distribution function into the product form of the mass function. $\square$

Theorem 6.2.1 is proved in the same way.

### 6.2.3. The Multinomial Distribution

**Definition 6.2.3 (Multinomial Distribution)** Let $A_1, \dots, A_r$ be a complete system of events for an experiment $S$, with $p_i = \mathbb{P}(A_i)$ and $\sum_{i=1}^r p_i = 1$. Perform $n$ independent repetitions of $S$ and let $X_i$ be the number of times $A_i$ occurs. Then (by induction on $r$)

$$
\mathbb{P}(X_1 = k_1, \dots, X_r = k_r) = \frac{n!}{k_1! \cdots k_r!}\, p_1^{k_1} \cdots p_r^{k_r}, \quad k_i \ge 0,\ \sum_{i=1}^r k_i = n.
$$
We say that $(X_1, \dots, X_r)$ has the **multinomial distribution** and write $(X_1, \dots, X_r) \sim \mathrm{Mult}(n, \boldsymbol{p})$, where $\boldsymbol{p} = (p_1, \dots, p_r)^{\mathsf T}$.

For $r = 2$ this is the binomial distribution. The coefficient $\frac{n!}{k_1! \cdots k_r!}$ counts the ways of splitting the $n$ trials into $r$ groups of sizes $k_1, \dots, k_r$.

**Property 6.2.1** Let $(X_1, \dots, X_r) \sim \mathrm{Mult}(n, \boldsymbol{p})$, let $1 \le m < r$, and let $j_1, \dots, j_m$ be distinct indices. Then the marginal distribution of $(X_{j_1}, \dots, X_{j_m})$ is

$$
\mathbb{P}(X_{j_1} = k_1, \dots, X_{j_m} = k_m) = \frac{n!}{k_1! \cdots k_m!\, k!}\, p_{j_1}^{k_1} \cdots p_{j_m}^{k_m}\, q^{k},
$$
where $k = n - \sum_{i=1}^m k_i \ge 0$ and $q = 1 - \sum_{i=1}^m p_{j_i}$. In particular $X_j \sim \mathrm{Bin}(n, p_j)$.

The reason is that after merging the remaining events into the single event "none of $A_{j_1}, \dots, A_{j_m}$ occurs" (of probability $q$), the vector $(X_{j_1}, \dots, X_{j_m}, n - \sum_i X_{j_i})$ is again multinomial. The components of a multinomial vector are not independent: their sum is always $n$. Covariances between components are computed in [3.1.10](/3.1.10).

## 6.3. Continuous Random Vectors

### 6.3.1. Joint and Marginal Densities

**Definition 6.3.1 (Continuous Random Vector)** Let $\boldsymbol{X} = (X_1, \dots, X_n)$ be a random vector. If there is a nonnegative integrable function $f(\boldsymbol{x}) = f(x_1, \dots, x_n)$ on $\mathbb{R}^n$ such that for every box $D = \{(x_1, \dots, x_n) \mid a_i < x_i \le b_i,\ 1 \le i \le n\}$ in $\mathbb{R}^n$

$$
\mathbb{P}(\boldsymbol{X} \in D) = \int_D f(x_1, \dots, x_n)\,\mathrm{d}x_1 \cdots \mathrm{d}x_n =: \int_D f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x},
$$
then $\boldsymbol{X}$ is called a **continuous random vector**, and $f$ is called the **joint density** (joint probability density function, or simply the density) of $\boldsymbol{X}$.

**Theorem 6.3.1** If $f$ is the joint density of $\boldsymbol{X}$, then for every $n$-dimensional Borel set $B$,

$$
\mathbb{P}(\boldsymbol{X} \in B) = \int_B f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}.
$$
In particular $\int_{\mathbb{R}^n} f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} = \mathbb{P}(\boldsymbol{X} \in \mathbb{R}^n) = 1$.

A joint density is not unique: changing $f$ on a null set leaves all integrals unchanged. Multiple integrals are evaluated with the following tool (we only need to use it; the proof belongs to real analysis).

**Theorem 6.3.2 (Fubini's Theorem)** Let $D$ be a region in $\mathbb{R}^n$ and let $\varphi$ be a function on $D$ that is either nonnegative or absolutely integrable (its absolute value has a finite integral). Then the $n$-fold integral $\int_D \varphi(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$ can be computed as an iterated integral, and the order of integration may be interchanged.

Let $1 \le k < n$ and let $D_k$ be a box in $\mathbb{R}^k$. By Fubini's theorem,

$$
\mathbb{P}((X_1, \dots, X_k) \in D_k) = \mathbb{P}(\boldsymbol{X} \in D_k \times \mathbb{R}^{n-k}) = \int_{D_k} \left( \int_{\mathbb{R}^{n-k}} f(x_1, \dots, x_n)\,\mathrm{d}x_{k+1} \cdots \mathrm{d}x_n \right) \mathrm{d}x_1 \cdots \mathrm{d}x_k.
$$
The function in parentheses is exactly the joint density of $(X_1, \dots, X_k)$, which leads to the following definition.

**Definition 6.3.2 (Marginal Density)** Let $f$ be the joint density of $\boldsymbol{X}$ and let $1 \le k < n$. The function

$$
f_{1, \dots, k}(x_1, \dots, x_k) = \int_{\mathbb{R}^{n-k}} f(x_1, \dots, x_n)\,\mathrm{d}x_{k+1} \cdots \mathrm{d}x_n
$$
is called the **marginal density** of $(X_1, \dots, X_k)$. The marginal density of any group of components $(X_{j_1}, \dots, X_{j_k})$ is obtained in the same way by integrating the joint density over the remaining $n - k$ variables.

The two-dimensional case is the most common: if $(X, Y)$ has joint density $f(x, y)$, then

$$
f_X(x) = \int_{-\infty}^{\infty} f(x, y)\,\mathrm{d}y, \qquad f_Y(y) = \int_{-\infty}^{\infty} f(x, y)\,\mathrm{d}x.
$$

**Example 6.3.1** Let $(X, Y)$ be uniformly distributed on the unit disk $D = \{(x, y) \mid x^2 + y^2 \le 1\}$. Find the densities of $X$ and $Y$.

**Solution** The joint density of $(X, Y)$ is $f(x, y) = \frac{1}{\pi} \boldsymbol{1}_D(x, y)$. $X$ takes values only in $[-1, 1]$, and for $\lvert x \rvert \le 1$,

$$
f_X(x) = \frac{1}{\pi} \int_{-\infty}^{\infty} \boldsymbol{1}\{x^2 + y^2 \le 1\}\,\mathrm{d}y = \frac{1}{\pi} \int_{-\infty}^{\infty} \boldsymbol{1}\{\lvert y \rvert \le \sqrt{1 - x^2}\}\,\mathrm{d}y = \frac{2}{\pi}\sqrt{1 - x^2},
$$
while $f_X(x) = 0$ for $\lvert x \rvert > 1$. Likewise $f_Y(y) = \frac{2}{\pi}\sqrt{1 - y^2}$ for $\lvert y \rvert \le 1$. The marginal distributions are no longer uniform.

### 6.3.2. Criteria for Independence

**Theorem 6.3.3** Suppose that for each $i$ ($1 \le i \le n$) the random variable $X_i$ has density $f_i(x_i)$. Then $X_1, \dots, X_n$ are independent if and only if the random vector $\boldsymbol{X} = (X_1, \dots, X_n)$ has joint density

$$
f(x_1, \dots, x_n) = f_1(x_1) f_2(x_2) \cdots f_n(x_n), \quad (x_1, \dots, x_n) \in \mathbb{R}^n.
$$

**Proof** Sufficiency: for any $(x_1, \dots, x_n) \in \mathbb{R}^n$, Fubini's theorem gives

$$
\mathbb{P}(X_1 \le x_1, \dots, X_n \le x_n) = \int_{-\infty}^{x_1} \cdots \int_{-\infty}^{x_n} \prod_{i=1}^n f_i(t_i)\,\mathrm{d}t_1 \cdots \mathrm{d}t_n = \prod_{i=1}^n \int_{-\infty}^{x_i} f_i(t_i)\,\mathrm{d}t_i = \prod_{i=1}^n \mathbb{P}(X_i \le x_i),
$$
so $X_1, \dots, X_n$ are independent.

Necessity: let $X_1, \dots, X_n$ be independent. For every box $D = \{a_i < x_i \le b_i,\ 1 \le i \le n\}$ in $\mathbb{R}^n$, independence and Fubini's theorem give

$$
\mathbb{P}(\boldsymbol{X} \in D) = \prod_{i=1}^n \mathbb{P}(a_i < X_i \le b_i) = \prod_{i=1}^n \int_{a_i}^{b_i} f_i(t_i)\,\mathrm{d}t_i = \int_D f_1(t_1) \cdots f_n(t_n)\,\mathrm{d}t_1 \cdots \mathrm{d}t_n,
$$
so $f_1(x_1) \cdots f_n(x_n)$ is a joint density of $\boldsymbol{X}$. $\square$

In practice the following factorization criterion is often used; it avoids computing marginal densities.

**Corollary 6.3.1** Let $(X, Y)$ have joint density $f(x, y)$. If there are nonnegative functions $g$ and $h$ such that $f(x, y) = g(x) h(y)$ for all $(x, y) \in \mathbb{R}^2$, then $X$ and $Y$ are independent, with $f_X = g / \int g$ and $f_Y = h / \int h$.

**Proof** From $1 = \int\!\!\int f = \int g \cdot \int h$ we get $c = \int g \in (0, \infty)$ and $\int h = 1/c$. Hence $f_X(x) = \int f(x, y)\,\mathrm{d}y = g(x)/c$, $f_Y(y) = c\,h(y)$ and $f(x, y) = f_X(x) f_Y(y)$, so $X$ and $Y$ are independent by Theorem 6.3.3. $\square$

**Remark 6.3.1** When using the factorization criterion, the density must be written out in full, including its support (the indicator function). In Example 6.3.1 the uniform density on the unit disk is the constant $\frac{1}{\pi}$ inside the disk and may seem to factor, but the complete density is $\frac{1}{\pi}\boldsymbol{1}\{x^2 + y^2 \le 1\}$, and the indicator cannot be written as a function of $x$ times a function of $y$; so $X, Y$ are not independent, and indeed $f_X(x) f_Y(y) \ne f(x, y)$. In contrast, if $f(x, y) = \lambda\mu\,\mathrm{e}^{-\lambda x - \mu y} \boldsymbol{1}\{x > 0\} \boldsymbol{1}\{y > 0\}$, the support is a product set, the density factors, and $X \sim \mathrm{Exp}(\lambda)$ and $Y \sim \mathrm{Exp}(\mu)$ are independent.

**Example 6.3.2 (Buffon's Needle Problem)** A plane is ruled with parallel lines at distance $a$ apart, and a needle of length $L$ ($L < a$) is dropped on it at random. Find the probability that the needle crosses a line.

**Solution** Let $X$ be the distance from the midpoint of the needle to the nearest line and $\Theta$ the angle between the needle and the lines. "At random" is interpreted as $X \sim \mathrm{U}(0, a/2)$ and $\Theta \sim \mathrm{U}(0, \pi/2)$ independent, with joint density $\frac{4}{\pi a}$ on $(0, a/2) \times (0, \pi/2)$. The needle crosses a line if and only if $X \le \frac{L}{2}\sin\Theta$, so

$$
\mathbb{P}\Big(X \le \frac{L}{2}\sin\Theta\Big) = \frac{4}{\pi a} \int_0^{\pi/2} \int_0^{\frac{L}{2}\sin\theta} \mathrm{d}x\,\mathrm{d}\theta = \frac{4}{\pi a} \cdot \frac{L}{2} \int_0^{\pi/2} \sin\theta\,\mathrm{d}\theta = \frac{2L}{\pi a}.
$$
(If $\Theta$ is taken as the angle between the needle and the normal to the lines, $\sin$ is replaced by $\cos$ and the result is the same.) This gives the classical method of estimating $\pi$ by a random experiment.

### 6.3.3. Joint Distribution Functions and Joint Densities

Given a joint density $f(x, y)$, the joint distribution function is

$$
F(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f(u, v)\,\mathrm{d}v\,\mathrm{d}u.
$$
Conversely, $f(x, y) = \dfrac{\partial^2 F(x, y)}{\partial x \partial y}$ at continuity points of $f$.

**Example 6.3.3** If $\dfrac{\partial F}{\partial x}$, $\dfrac{\partial F}{\partial y}$, $\dfrac{\partial^2 F}{\partial x \partial y}$ and $\dfrac{\partial^2 F}{\partial y \partial x}$ are continuous in a neighborhood of $(x, y)$, then the rectangle formula of Example 6.1.1 and the mean value theorem give

$$
\lim_{\substack{\Delta x \downarrow 0 \\ \Delta y \downarrow 0}} \frac{\mathbb{P}(x - \Delta x < X \le x,\ y - \Delta y < Y \le y)}{\Delta x\,\Delta y} = \frac{\partial^2 F(x, y)}{\partial x \partial y} = \frac{\partial^2 F(x, y)}{\partial y \partial x}.
$$
So the joint density can be read as "the probability of a small rectangle near $(x, y)$ divided by its area", and this infinitesimal viewpoint is useful in deriving formulas. More generally, there is the following criterion (stated for reference).

**Theorem 6.3.4** Let $(X, Y)$ have a continuous joint distribution function $F(x, y)$. Put $f(x, y) = \dfrac{\partial^2 F(x, y)}{\partial x \partial y}$ where this mixed partial derivative exists and $f(x, y) = 0$ elsewhere. If $\int_{\mathbb{R}^2} f(x, y)\,\mathrm{d}x\,\mathrm{d}y = 1$, then $f$ is a joint density of $(X, Y)$.

The condition that the integral equal $1$ cannot be dropped, as the next two examples show.

**Example 6.3.4** If the distribution functions of $X$ and $Y$ are both continuous, then their joint distribution function $F(x, y)$ is continuous.

**Proof** For any $(x_0, y_0)$ and $\varepsilon > 0$ there is $\delta > 0$ such that $\lvert F_X(x) - F_X(x_0) \rvert < \varepsilon/2$ and $\lvert F_Y(y) - F_Y(y_0) \rvert < \varepsilon/2$ whenever $\lvert x - x_0 \rvert < \delta$ and $\lvert y - y_0 \rvert < \delta$. For such $(x, y)$,

$$
\begin{aligned}
\lvert F(x, y) - F(x_0, y_0) \rvert &\le \lvert F(x, y) - F(x_0, y) \rvert + \lvert F(x_0, y) - F(x_0, y_0) \rvert \\
&\le \mathbb{P}(x \wedge x_0 < X \le x \vee x_0) + \mathbb{P}(y \wedge y_0 < Y \le y \vee y_0) \\
&= \lvert F_X(x) - F_X(x_0) \rvert + \lvert F_Y(y) - F_Y(y_0) \rvert < \varepsilon. \qquad \square
\end{aligned}
$$

**Example 6.3.5** There is a random vector $(X, Y)$ with a continuous joint distribution function that is not a continuous random vector. Let $X \sim \mathrm{U}(0, 1)$ and $Y = X$. Then

$$
F(x, y) = \mathbb{P}(X \le \min\{x, y\}) = \begin{cases} 0, & \min\{x, y\} \le 0, \\ \min\{x, y\}, & 0 < \min\{x, y\} \le 1, \\ 1, & \min\{x, y\} > 1 \end{cases}
$$
is continuous. If $(X, Y)$ had a joint density $f$, then, writing $D$ for the line $y = x$, we would have $1 = \mathbb{P}(X = Y) = \mathbb{P}((X, Y) \in D) = \int_D f(x, y)\,\mathrm{d}x\,\mathrm{d}y = 0$ (a line has zero area), a contradiction. Here the mixed partial derivative of $F$ exists and is continuous (equal to $0$) off finitely many lines, but its integral is $0$, not $1$.

This also answers a natural question: a random vector formed by two continuous random variables $X_1, X_2$ need not be a continuous random vector; and even when $(X_1, X_2)$ has a joint density, it cannot be recovered from the two marginal densities alone (Remark 6.1.1) unless the components are known to be independent.

## 6.4. The Bivariate Normal Distribution

We start with a special case. Let $(X, Y)$ have joint density

$$
f(x, y) = \frac{1}{2\pi} \exp\left( -\frac{x^2 + y^2}{2} \right) = \frac{1}{\sqrt{2\pi}} \mathrm{e}^{-x^2/2} \cdot \frac{1}{\sqrt{2\pi}} \mathrm{e}^{-y^2/2}.
$$
By Corollary 6.3.1, $X \sim \mathcal{N}(0, 1)$ and $Y \sim \mathcal{N}(0, 1)$ are independent. A general bivariate normal distribution must allow different means and variances for the two components as well as dependence between them, which requires five parameters.

**Definition 6.4.1 (Bivariate Normal Distribution)** Let $\mu_1, \mu_2$ be constants, $\sigma_1, \sigma_2$ positive constants, and $\rho \in (-1, 1)$. If the random vector $(X, Y)$ has joint density

$$
f(x, y) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1 - \rho^2}} \exp\left\{ -\frac{1}{2(1 - \rho^2)} \left[ \frac{(x - \mu_1)^2}{\sigma_1^2} - \frac{2\rho(x - \mu_1)(y - \mu_2)}{\sigma_1\sigma_2} + \frac{(y - \mu_2)^2}{\sigma_2^2} \right] \right\},
$$
then $(X, Y)$ is said to have the **bivariate normal distribution**, written $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$.

With $\boldsymbol{x} = (x, y)^{\mathsf T}$, $\boldsymbol{\mu} = (\mu_1, \mu_2)^{\mathsf T}$ and

$$
\Sigma = \begin{pmatrix} \sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}, \qquad \lvert \Sigma \rvert = \det\Sigma = \sigma_1^2\sigma_2^2(1 - \rho^2) > 0,
$$
the density takes a form entirely analogous to the univariate normal density $\frac{1}{\sqrt{2\pi\sigma^2}}\exp\{-\frac{(x - \mu)^2}{2\sigma^2}\}$:

$$
f(\boldsymbol{x}) = \frac{1}{2\pi\lvert\Sigma\rvert^{1/2}} \exp\left\{ -\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) \right\}.
$$
The contour lines $(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) = c^2$ of the density are ellipses centered at $\boldsymbol{\mu}$; they are circles when $\rho = 0$ and $\sigma_1 = \sigma_2$, and for $\rho > 0$ the major axis tilts toward the direction of $y = x$. We shall see that $\mu_1, \mu_2$ are the expectations of the components, $\sigma_1^2, \sigma_2^2$ their variances, $\rho$ their correlation coefficient ([3.1.10](/3.1.10)) and $\Sigma$ the covariance matrix; the general multivariate case is treated in [3.1.15](/3.1.15).

![Density surfaces and contour lines of the bivariate normal distribution: left column rho = 0, right column rho = 0.75 (sigma1 = sigma2 = 1)](./plots/bivariate-normal.py)

**Property 6.4.1** If $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$, then $X \sim \mathcal{N}(\mu_1, \sigma_1^2)$ and $Y \sim \mathcal{N}(\mu_2, \sigma_2^2)$.

**Proof** Put $u = \frac{x - \mu_1}{\sigma_1}$ and $v = \frac{y - \mu_2}{\sigma_2}$. The quadratic form in brackets is $u^2 - 2\rho uv + v^2 = (v - \rho u)^2 + (1 - \rho^2)u^2$, so

$$
f_X(x) = \int_{-\infty}^{\infty} f(x, y)\,\mathrm{d}y = \frac{\mathrm{e}^{-u^2/2}}{\sqrt{2\pi}\,\sigma_1} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi(1 - \rho^2)}} \exp\left\{ -\frac{(v - \rho u)^2}{2(1 - \rho^2)} \right\} \mathrm{d}v = \frac{1}{\sqrt{2\pi}\,\sigma_1} \exp\left\{ -\frac{(x - \mu_1)^2}{2\sigma_1^2} \right\},
$$
where we used that the integrand is the density of $\mathcal{N}(\rho u, 1 - \rho^2)$ and integrates to $1$. The case of $Y$ is symmetric. $\square$

Hence the marginal distributions do not depend on $\rho$: different values of $\rho$ give random vectors with the same marginals but different joint distributions, another instance of Remark 6.1.1.

**Theorem 6.4.1** If $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$, then $X, Y$ are independent if and only if $\rho = 0$.

**Proof** By Property 6.4.1, $X, Y$ are independent if and only if $f(x, y) = f_X(x) f_Y(y)$ for all $(x, y)$ (both sides are continuous, so equality almost everywhere is equality everywhere). When $\rho = 0$ the exponent of $f$ splits as $-\frac{(x - \mu_1)^2}{2\sigma_1^2} - \frac{(y - \mu_2)^2}{2\sigma_2^2}$, the equality holds, and $X, Y$ are independent. Conversely, if $X, Y$ are independent, comparing the two sides at $(x, y) = (\mu_1, \mu_2)$ gives

$$
\frac{1}{2\pi\sigma_1\sigma_2\sqrt{1 - \rho^2}} = \frac{1}{2\pi\sigma_1\sigma_2},
$$
that is, $\sqrt{1 - \rho^2} = 1$ and $\rho = 0$. $\square$

## 6.5. Conditional Distributions

The joint distribution carries the complete information. Many questions, however, ask how the distribution of one component changes once the value of another is known: for instance, what is the distribution of weight $X$ given height $Y = y$? This is the conditional distribution.

### 6.5.1. Discrete Conditional Distributions

**Definition 6.5.1 (Conditional Probability Mass Function)** Let $(X, Y)$ be a discrete random vector with joint mass function $p_{ij} = \mathbb{P}(X = x_i, Y = y_j)$, and let $p_i = \mathbb{P}(X = x_i)$ and $q_j = \mathbb{P}(Y = y_j)$ be the marginal mass functions of $X$ and $Y$. For each $j$ with $q_j > 0$,

$$
\mathbb{P}(X = x_i \mid Y = y_j) = \frac{\mathbb{P}(X = x_i, Y = y_j)}{\mathbb{P}(Y = y_j)} = \frac{p_{ij}}{q_j}, \quad i = 1, 2, \dots
$$
is called the **conditional probability mass function** of $X$ given $Y = y_j$.

For fixed $j$, the numbers $\{p_{ij}/q_j\}_i$ are nonnegative and sum to $1$, so they do form a mass function: the $j$-th column of the joint table divided by its column sum. In the example of the two four-sided dice, $\mathbb{P}(X = 3 \mid Y = 2) = \frac{1/16}{1/4} = \frac{1}{4} = \mathbb{P}(X = 3)$. By the multiplication rule for conditional probabilities, $p_{ij} = q_j\,\mathbb{P}(X = x_i \mid Y = y_j)$: the marginal and the conditional distributions together determine the joint distribution.

**Theorem 6.5.1** Discrete random variables $X, Y$ are independent if and only if, for all $i, j$ with $q_j > 0$,

$$
\mathbb{P}(X = x_i \mid Y = y_j) = \mathbb{P}(X = x_i).
$$

This is equivalent to $p_{ij} = p_i q_j$ in Corollary 6.2.1: independence means that knowing the value of $Y$ does not change the distribution of $X$.

**Example 6.5.1** A shooter fires independently at a target, hitting it each time with probability $p = 1 - q$. Let $S_n$ be the number of the shot on which the target is hit for the $n$-th time. Find the conditional distributions of $(X, Y) = (S_1, S_2)$.

**Solution** The event $\{S_1 = i, S_2 = j\}$ means that among the first $j$ shots exactly the $i$-th and the $j$-th hit, so the joint distribution is

$$
\mathbb{P}(X = i, Y = j) = p^2 q^{j-2}, \quad j > i \ge 1.
$$
The marginal distributions are

$$
\mathbb{P}(X = i) = \sum_{j=i+1}^{\infty} p^2 q^{j-2} = p q^{i-1}, \qquad \mathbb{P}(Y = j) = \sum_{i=1}^{j-1} p^2 q^{j-2} = (j - 1)p^2 q^{j-2}, \quad j \ge 2.
$$
Hence for fixed $i$,

$$
\mathbb{P}(Y = j \mid X = i) = \frac{p^2 q^{j-2}}{p q^{i-1}} = p q^{j-i-1}, \quad j > i,
$$
so given that the first hit occurs on shot $i$, the additional waiting time $Y - i$ is again $\mathrm{Geo}(p)$; and for fixed $j \ge 2$,

$$
\mathbb{P}(X = i \mid Y = j) = \frac{p^2 q^{j-2}}{(j - 1)p^2 q^{j-2}} = \frac{1}{j - 1}, \quad 1 \le i < j,
$$
so given $S_2 = j$, $S_1$ is uniformly distributed on $\{1, 2, \dots, j - 1\}$. Moreover, with $X_1 = S_1$ and $X_2 = S_2 - S_1$,

$$
\mathbb{P}(X_1 = i, X_2 = j) = \mathbb{P}(S_1 = i, S_2 = i + j) = p^2 q^{i+j-2} = p q^{i-1} \cdot p q^{j-1},
$$
so by Corollary 6.2.1, $X_1$ and $X_2$ are independent and identically distributed, both $\mathrm{Geo}(p)$.

### 6.5.2. Continuous Conditional Distributions

For a continuous random vector $\mathbb{P}(Y = y) = 0$, so the definition of conditional probability cannot be applied directly. The natural approach is to condition first on $\{y - \varepsilon < Y \le y\}$ and then let $\varepsilon \to 0$. Suppose $(X, Y)$ has joint density $f(x, y)$, the marginal density $f_Y(y) = \int f(x, y)\,\mathrm{d}x$ is continuous at $y$ with $f_Y(y) > 0$, and $\partial F(x, y)/\partial y$ exists. Then

$$
\lim_{\varepsilon \to 0} \mathbb{P}(X \le x \mid y - \varepsilon < Y \le y) = \lim_{\varepsilon \to 0} \frac{[F(x, y) - F(x, y - \varepsilon)]/\varepsilon}{[F_Y(y) - F_Y(y - \varepsilon)]/\varepsilon} = \frac{\frac{\partial}{\partial y}\int_{-\infty}^{x}\int_{-\infty}^{y} f(s, t)\,\mathrm{d}t\,\mathrm{d}s}{f_Y(y)} = \frac{\int_{-\infty}^{x} f(s, y)\,\mathrm{d}s}{f_Y(y)}.
$$
This motivates the following definition.

**Definition 6.5.2 (Conditional Distribution Function)** Let the random vector $(X, Y)$ have joint density $f(x, y)$, and let $Y$ have marginal density $f_Y(y)$. If $f_Y(y) > 0$ at a given $y$, then

$$
F_{X|Y}(x \mid y) = \mathbb{P}(X \le x \mid Y = y) = \frac{\int_{-\infty}^{x} f(s, y)\,\mathrm{d}s}{f_Y(y)}, \quad x \in \mathbb{R}
$$
is called the **conditional distribution function** of $X$ given $Y = y$, or simply the conditional distribution, and

$$
f_{X|Y}(x \mid y) = \frac{f(x, y)}{f_Y(y)} = \frac{f(x, y)}{\int_{-\infty}^{\infty} f(x, y)\,\mathrm{d}x}, \quad x \in \mathbb{R}
$$
is called the **conditional density** (conditional probability density) of $X$ given $Y = y$.

Geometrically, the conditional density is the section $x \mapsto f(x, y)$ of the joint density surface along $Y = y$, divided by the area $f_Y(y)$ under it so as to become a density again. Conditional densities and conditional distribution functions are related as in one dimension: for $y$ with $f_Y(y) > 0$,

1. $F_{X|Y}(x \mid y) = \int_{-\infty}^{x} f_{X|Y}(s \mid y)\,\mathrm{d}s$;
2. if $F_{X|Y}(x \mid y)$ is continuous in $x$ and has a continuous derivative except at most at countably many points, then $\frac{\partial}{\partial x} F_{X|Y}(x \mid y)$ (where it exists, and $0$ elsewhere) is a conditional density.

The definition immediately gives the continuous multiplication rule

$$
f(x, y) = f_Y(y)\,f_{X|Y}(x \mid y),
$$
the basic tool for building a joint density from a marginal and a conditional density.

**Theorem 6.5.2** Let $(X, Y)$ have a joint density. Then $X, Y$ are independent if and only if, for $y$ in $\{y \mid f_Y(y) > 0\}$,

$$
f_{X|Y}(x \mid y) = f_X(x), \quad x \in \mathbb{R},
$$
that is, $f(x, y) = f_X(x) f_Y(y)$ (Theorem 6.3.3).

![Conditional densities of the bivariate normal distribution (rho = 0.75): sections of the joint density at different values of y, renormalized; the conditional mean moves linearly with y](./plots/conditional-slices.py)

**Example 6.5.2** Let $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$. Find the conditional density of $Y$ given $X = x$.

**Solution** By Property 6.4.1, $X \sim \mathcal{N}(\mu_1, \sigma_1^2)$. With the notation $u = \frac{x - \mu_1}{\sigma_1}$, $v = \frac{y - \mu_2}{\sigma_2}$ from the proof of Property 6.4.1,

$$
f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)} = \frac{1}{\sigma_2\sqrt{2\pi(1 - \rho^2)}} \exp\left\{ -\frac{(v - \rho u)^2}{2(1 - \rho^2)} \right\} = \frac{1}{\sigma_2\sqrt{2\pi(1 - \rho^2)}} \exp\left\{ -\frac{(y - \mu_{x})^2}{2(1 - \rho^2)\sigma_2^2} \right\},
$$
where $\mu_{x} = \mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1)$. Thus

$$
Y \mid X = x \ \sim\ \mathcal{N}\Big( \mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1),\ (1 - \rho^2)\sigma_2^2 \Big),
$$
and likewise $X \mid Y = y \sim \mathcal{N}\big( \mu_1 + \rho\frac{\sigma_1}{\sigma_2}(y - \mu_2),\ (1 - \rho^2)\sigma_1^2 \big)$. The conditional distribution is again normal; its mean is a linear function of the conditioning value, and its variance $(1 - \rho^2)\sigma_2^2$ does not depend on $x$ and never exceeds the unconditional variance $\sigma_2^2$: knowing $X$ reduces the uncertainty about $Y$, and the more so the larger $\lvert\rho\rvert$ is. For $\rho = 0$ we get $f_{Y|X}(y \mid x) = f_Y(y)$, in agreement with Theorem 6.4.1.

**Example 6.5.3** An index $Y$ of the operating environment of a computer has distribution $\Gamma(\alpha, \lambda)$, with density

$$
f_Y(y) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} y^{\alpha-1} \mathrm{e}^{-\lambda y}, \quad y > 0.
$$
Given $Y = y$, the lifetime $X$ of a piece of software satisfies $X \mid Y = y \sim \mathrm{Exp}(y)$. Find the distribution of $X$.

**Solution** The conditional density of $X$ is $f_{X|Y}(x \mid y) = y\mathrm{e}^{-xy}$ for $x > 0$. By the multiplication rule, the joint density of $(X, Y)$ is

$$
f(x, y) = f_{X|Y}(x \mid y) f_Y(y) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} y^{\alpha} \mathrm{e}^{-y(x + \lambda)}, \quad x, y > 0.
$$
For $x > 0$, substituting $t = y(x + \lambda)$ and using $\Gamma(\alpha + 1) = \alpha\Gamma(\alpha)$,

$$
f_X(x) = \int_0^{\infty} f(x, y)\,\mathrm{d}y = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \frac{1}{(x + \lambda)^{\alpha+1}} \int_0^{\infty} t^{\alpha} \mathrm{e}^{-t}\,\mathrm{d}t = \frac{\alpha\lambda^{\alpha}}{(x + \lambda)^{\alpha+1}}, \quad x > 0.
$$
The tail $\mathbb{P}(X > x) = \big(\frac{\lambda}{x + \lambda}\big)^{\alpha}$ of this distribution decays like a power, more slowly than that of any exponential distribution: randomness in the environment makes the lifetime distribution heavy-tailed.

### 6.5.3. Conditional Distributions of Random Vectors

The definitions extend directly to random vectors (stated for reference). Let $\boldsymbol{X} = (X_1, \dots, X_n)$ and $\boldsymbol{Y} = (Y_1, \dots, Y_m)$, let $(\boldsymbol{X}, \boldsymbol{Y})$ have joint density $f(\boldsymbol{x}, \boldsymbol{y})$, and let $f_{\boldsymbol{Y}}(\boldsymbol{y}) = \int_{\mathbb{R}^n} f(\boldsymbol{x}, \boldsymbol{y})\,\mathrm{d}\boldsymbol{x}$ be the marginal density of $\boldsymbol{Y}$. If $f_{\boldsymbol{Y}}(\boldsymbol{y}) > 0$ at a given $\boldsymbol{y}$, the conditional distribution function and the conditional density of $\boldsymbol{X}$ given $\boldsymbol{Y} = \boldsymbol{y}$ are

$$
F_{\boldsymbol{X}|\boldsymbol{Y}}(\boldsymbol{x} \mid \boldsymbol{y}) = \frac{\int_{\boldsymbol{s} \le \boldsymbol{x}} f(\boldsymbol{s}, \boldsymbol{y})\,\mathrm{d}\boldsymbol{s}}{f_{\boldsymbol{Y}}(\boldsymbol{y})}, \qquad f_{\boldsymbol{X}|\boldsymbol{Y}}(\boldsymbol{x} \mid \boldsymbol{y}) = \frac{f(\boldsymbol{x}, \boldsymbol{y})}{f_{\boldsymbol{Y}}(\boldsymbol{y})}.
$$

The multiplication rule, the law of total probability and Bayes' formula for conditional distributions are collected, together with their versions for events, in [3.1.9](/3.1.9).

## Summary

| Object | Discrete | Continuous |
|---|---|---|
| Joint distribution | Joint mass function $p_{ij} = \mathbb{P}(X = x_i, Y = y_j)$ | Joint density $f(x, y)$, $\mathbb{P}((X, Y) \in B) = \int_B f$ |
| Marginal distribution | Sum over the other indices: $p_i = \sum_j p_{ij}$ | Integrate over the other variables: $f_X(x) = \int f(x, y)\,\mathrm{d}y$ |
| Conditional distribution | $\mathbb{P}(X = x_i \mid Y = y_j) = p_{ij}/q_j$ | $f_{X\mid Y}(x \mid y) = f(x, y)/f_Y(y)$ |
| Independence | $p_{ij} = p_i q_j$ for all $i, j$ | $f(x, y) = f_X(x) f_Y(y)$; factor together with the support |
| Typical example | Multinomial distribution $\mathrm{Mult}(n, \boldsymbol{p})$ | Bivariate normal distribution $\mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$ |

- The joint distribution function $F(x, y)$ exists for every random vector: the marginal distribution functions are $F(x, +\infty)$ and $F(+\infty, y)$, with no integration needed, and the probability of a rectangle is $F(b, d) - F(b, c) - F(a, d) + F(a, c)$.
- The joint distribution determines the marginals, but not conversely; under independence the marginals determine the joint distribution.
- Conditional distribution times marginal distribution gives the joint distribution (the multiplication rule), from which the marginal distribution of the other component can be found (Example 6.5.3).
- The marginal and conditional distributions of a bivariate normal distribution are normal; the components are independent if and only if $\rho = 0$.
