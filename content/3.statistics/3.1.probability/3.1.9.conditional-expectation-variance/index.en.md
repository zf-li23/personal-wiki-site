---
title: Conditional Expectation and Conditional Variance
source_hash: d1e39675aaca
---

The previous chapter summarized a random variable by its expectation. When partial information is available, for instance that an event $A$ has occurred or that another random variable $Y$ has been observed, the average should be computed from the conditional distribution instead of the unconditional one; this is the conditional expectation. Knowing a person's foot length, we may ask for their average height; knowing that someone can climb over a wall, we may ask the same question. This chapter first reviews the forms that conditional probability takes for events and for random variables (the multiplication rule, the law of total probability and Bayes' theorem), and then defines the conditional expectation $\mathbb{E}(X \mid A)$ given an event and the conditional expectation $\mathbb{E}(X \mid Y)$ given a random variable. The latter is itself a random variable; it satisfies the law of iterated expectations $\mathbb{E}[\mathbb{E}(X \mid Y)] = \mathbb{E}X$, which greatly simplifies computations in hierarchical models, and it is the best predictor of $X$ from $Y$ in the mean-square sense. Finally we define the conditional variance and prove the law of total variance. The chapter uses the conditional distributions of [3.1.6](/3.1.6) and the expectation of [3.1.8](/3.1.8); the idea of conditional expectation runs through statistics, for example in linear regression ([3.3](/3.3)), the Rao–Blackwell theorem ([3.2.3](/3.2.3)) and the EM algorithm.

## 9.1. Conditional Probability Revisited

Conditional probability has already appeared in several forms: the conditional probability $\mathbb{P}(A \mid B)$ given an event ([3.1.2](/3.1.2)), the conditional distribution $\mathbb{P}(X \in \cdot \mid A)$ of a random variable given an event, and the conditional distribution given a random variable ([3.1.6](/3.1.6)). Let $\mathbb{P}(A) > 0$. The conditional probability mass function of $X$ given $A$ is $p_{X|A}(x) = \mathbb{P}(\{X = x\} \cap A)/\mathbb{P}(A)$; in the continuous case, if there is a function $f_{X|A} \ge 0$ such that $\mathbb{P}(X \in B \mid A) = \int_B f_{X|A}(x)\,\mathrm{d}x$ for every Borel set $B$, then $f_{X|A}$ is called the conditional density of $X$ given $A$. In particular, for $A = \{X \in C\}$ we have $f_{X|A}(x) = f_X(x)\boldsymbol{1}_C(x)/\mathbb{P}(X \in C)$.

The three basic rules take exactly parallel forms in all these settings (here $A_1, \dots, A_n$ is a partition of $\Omega$ and all conditional probabilities involved are assumed to be defined):

| | Events | $X$ given an event | $X$ given a random variable $Y$ |
|---|---|---|---|
| Multiplication rule | $\mathbb{P}(A \cap B) = \mathbb{P}(B)\mathbb{P}(A \mid B)$ | $\mathbb{P}(\{X = x\} \cap A) = \mathbb{P}(A)p_{X\mid A}(x)$; $f_X(x)\boldsymbol{1}_C(x) = \mathbb{P}(X \in C)f_{X\mid\{X\in C\}}(x)$ | $p_{X,Y}(x, y) = p_Y(y)p_{X\mid Y}(x \mid y)$; $f(x, y) = f_Y(y)f_{X\mid Y}(x \mid y)$ |
| Law of total probability | $\mathbb{P}(B) = \sum_i \mathbb{P}(A_i)\mathbb{P}(B \mid A_i)$ | $p_X(x) = \sum_i \mathbb{P}(A_i)p_{X\mid A_i}(x)$; $f_X(x) = \sum_i \mathbb{P}(A_i)f_{X\mid A_i}(x)$ | $p_X(x) = \sum_y p_Y(y)p_{X\mid Y}(x \mid y)$; $f_X(x) = \int f_Y(y)f_{X\mid Y}(x \mid y)\,\mathrm{d}y$ |
| Bayes' theorem | $\mathbb{P}(A_i \mid B) = \dfrac{\mathbb{P}(A_i)\mathbb{P}(B \mid A_i)}{\sum_j \mathbb{P}(A_j)\mathbb{P}(B \mid A_j)}$ | Analogous | See below |

Bayes' theorem for random variables splits into four cases according to whether $X$ and $Y$ are discrete or continuous. The formulas have the same shape; only mass functions and densities are interchanged:

1. $X, Y$ both discrete: $p_{X|Y}(x \mid y) = \dfrac{p_X(x)p_{Y|X}(y \mid x)}{p_Y(y)}$, $p_Y(y) = \sum_x p_X(x)p_{Y|X}(y \mid x)$. Example: $X \in \{0, 1\}$ indicates whether an aircraft is present and $Y \in \{0, 1\}$ whether the radar raises an alarm.
2. $X, Y$ both continuous: $f_{X|Y}(x \mid y) = \dfrac{f_X(x)f_{Y|X}(y \mid x)}{f_Y(y)}$, $f_Y(y) = \int f_X(x)f_{Y|X}(y \mid x)\,\mathrm{d}x$. Example: $X$ is a continuous signal, $Y$ an observation with measurement error, and $f_{Y|X}$ the noise model.
3. $X$ discrete, $Y$ continuous: $p_{X|Y}(x \mid y) = \dfrac{p_X(x)f_{Y|X}(y \mid x)}{f_Y(y)}$, $f_Y(y) = \sum_x p_X(x)f_{Y|X}(y \mid x)$. Example: $X$ indicates whether a patient has a certain disease and $Y$ is the white blood cell concentration.
4. $X$ continuous, $Y$ discrete: $f_{X|Y}(x \mid y) = \dfrac{f_X(x)p_{Y|X}(y \mid x)}{p_Y(y)}$, $p_Y(y) = \int f_X(x)p_{Y|X}(y \mid x)\,\mathrm{d}x$. Example: $X$ is height and $Y$ is shoe size.

**Example 9.1.1** A faulty minting machine produces coins whose probability of heads is a random variable $P$ with density $f_P(p) = p\mathrm{e}^p$ ($0 \le p \le 1$). A coin made by this machine is tossed repeatedly and independently. Find (1) the probability of heads on one toss; (2) the conditional density of $P$ given that the first toss is heads; (3) the probability that the second toss is heads given that the first one is.

**Solution** Let $A$ and $B$ be the events that the first and the second toss are heads. Given $P = p$, the tosses are independent with probability of heads $p$.

(1) By the law of total probability (case 4), $\mathbb{P}(A) = \int_0^1 p \cdot p\mathrm{e}^p\,\mathrm{d}p = \big[\mathrm{e}^p(p^2 - 2p + 2)\big]_0^1 = \mathrm{e} - 2 \approx 0.718$.

(2) By Bayes' theorem, $f_{P|A}(p) = \dfrac{f_P(p)\mathbb{P}(A \mid P = p)}{\mathbb{P}(A)} = \dfrac{p^2\mathrm{e}^p}{\mathrm{e} - 2}$, $0 \le p \le 1$.

(3) Apply the law of total probability once more under the conditional probability $\mathbb{P}(\cdot \mid A)$, with the distribution of $P$ replaced by the posterior distribution from (2):

$$
\mathbb{P}(B \mid A) = \int_0^1 \mathbb{P}(B \mid P = p, A)f_{P|A}(p)\,\mathrm{d}p = \int_0^1 p\cdot\frac{p^2\mathrm{e}^p}{\mathrm{e} - 2}\,\mathrm{d}p = \frac{6 - 2\mathrm{e}}{\mathrm{e} - 2} \approx 0.784.
$$
This exceeds $\mathbb{P}(B) = \mathrm{e} - 2$: the two tosses are independent given $P$ but not unconditionally, since heads on the first toss raises our estimate of $P$.

## 9.2. Conditional Expectation Given an Event

### 9.2.1. Definition and Computation

Replacing the distribution in the definition of expectation by the conditional distribution given $A$ yields the conditional expectation given $A$: it is the expectation of $X$ under the probability measure $\mathbb{P}_A(\cdot) = \mathbb{P}(\cdot \mid A)$.

**Definition 9.2.1** Let $\mathbb{P}(A) > 0$. In the discrete case, if $\sum_i \lvert x_i \rvert\mathbb{P}(X = x_i \mid A) < \infty$, the conditional expectation of $X$ given that $A$ occurs is

$$
\mathbb{E}(X \mid A) = \sum_i x_i\,\mathbb{P}(X = x_i \mid A);
$$
in the continuous case, if $\int \lvert x \rvert f_{X|A}(x)\,\mathrm{d}x < \infty$, it is $\mathbb{E}(X \mid A) = \int_{-\infty}^{\infty} x f_{X|A}(x)\,\mathrm{d}x$.

**Theorem 9.2.1** If $\mathbb{P}(A) > 0$ and $\mathbb{E}(X \mid A)$ exists, then

$$
\mathbb{E}(X \mid A) = \frac{\mathbb{E}(X\boldsymbol{1}_A)}{\mathbb{P}(A)}.
$$

**Proof** First let $X \ge 0$. Since $\mathbb{E}(X \mid A)$ is the expectation of $X$ under $\mathbb{P}_A$, Theorem 8.2.3 gives

$$
\mathbb{E}(X \mid A) = \int_0^{\infty}\mathbb{P}(X > x \mid A)\,\mathrm{d}x = \frac{1}{\mathbb{P}(A)}\int_0^{\infty}\mathbb{P}(\{X > x\} \cap A)\,\mathrm{d}x = \frac{1}{\mathbb{P}(A)}\int_0^{\infty}\mathbb{P}(X\boldsymbol{1}_A > x)\,\mathrm{d}x = \frac{\mathbb{E}(X\boldsymbol{1}_A)}{\mathbb{P}(A)},
$$
where we used $\{X > x\} \cap A = \{X\boldsymbol{1}_A > x\}$ for $x \ge 0$. In general, decompose $X$ into its positive and negative parts, $X = X^+ - X^-$ with $X^+ = X\boldsymbol{1}\{X \ge 0\}$ and $X^- = -X\boldsymbol{1}\{X < 0\}$, apply the formula to each and subtract. $\square$

Thus a conditional expectation can be computed from an unconditional one, without first finding the conditional distribution.

**Example 9.2.1** Let $X \sim \mathrm{Exp}(\lambda)$ and $a > 0$. Then $\mathbb{E}(X \mid X > a) = a + \frac{1}{\lambda}$.

**Proof** By Theorem 9.2.1 and integration by parts,

$$
\mathbb{E}(X \mid X > a) = \frac{\mathbb{E}(X\boldsymbol{1}\{X > a\})}{\mathbb{P}(X > a)} = \mathrm{e}^{\lambda a}\int_a^{\infty} x\lambda\mathrm{e}^{-\lambda x}\,\mathrm{d}x = \mathrm{e}^{\lambda a}\Big(a + \frac{1}{\lambda}\Big)\mathrm{e}^{-\lambda a} = a + \frac{1}{\lambda}.
$$
The result also follows directly from the memorylessness of the exponential distribution: given $X > a$, the excess $X - a$ is again $\mathrm{Exp}(\lambda)$, so $\mathbb{E}(X \mid X > a) = a + \mathbb{E}(X - a \mid X > a) = a + \frac{1}{\lambda}$. $\square$

**Example 9.2.2** Let $X \sim \mathrm{Exp}(\lambda)$ and $Y \sim \mathrm{Exp}(\mu)$ be independent. Compute $\mathbb{E}(X \mid X < Y)$.

**Solution** Integrating over $y$ first, $\mathbb{E}(X\boldsymbol{1}\{X < Y\}) = \int_0^{\infty} x\,\mathbb{P}(Y > x)\lambda\mathrm{e}^{-\lambda x}\,\mathrm{d}x = \int_0^{\infty} x\lambda\mathrm{e}^{-(\lambda + \mu)x}\,\mathrm{d}x = \frac{\lambda}{(\lambda + \mu)^2}$, while $\mathbb{P}(X < Y) = \int_0^{\infty}\mathrm{e}^{-\mu x}\lambda\mathrm{e}^{-\lambda x}\,\mathrm{d}x = \frac{\lambda}{\lambda + \mu}$. By Theorem 9.2.1,

$$
\mathbb{E}(X \mid X < Y) = \frac{\lambda/(\lambda + \mu)^2}{\lambda/(\lambda + \mu)} = \frac{1}{\lambda + \mu}.
$$
This is exactly the expectation of $\min\{X, Y\} \sim \mathrm{Exp}(\lambda + \mu)$. Indeed, $X = \min\{X, Y\}$ on $\{X < Y\}$, and $\min\{X, Y\}$ is independent of the event $\{X < Y\}$.

### 9.2.2. The Law of Total Expectation

The unconditional expectation is a weighted average of the conditional expectations in the various cases; this extends the law of total probability from probabilities to expectations.

**Theorem 9.2.2 (Law of Total Expectation)** Let $A_1, \dots, A_n$ be a partition of $\Omega$ with $\mathbb{P}(A_i) > 0$, and let $\mathbb{E}\lvert X \rvert < \infty$. Then

$$
\mathbb{E}X = \sum_{i=1}^n \mathbb{P}(A_i)\,\mathbb{E}(X \mid A_i).
$$

**Proof** By Theorem 9.2.1 the right-hand side equals $\sum_i \mathbb{E}(X\boldsymbol{1}_{A_i}) = \mathbb{E}\big(X\sum_i\boldsymbol{1}_{A_i}\big) = \mathbb{E}X$. Alternatively, multiply the law of total probability $p_X(x) = \sum_i \mathbb{P}(A_i)p_{X|A_i}(x)$ by $x$, sum over $x$ and interchange the order of summation. $\square$

The formula holds for countable partitions as well. To compute the average score of a class, one may first compute the average of each group and then average these with weights proportional to the group sizes; this is the law of total expectation.

**Example 9.2.3** Let $X \sim \mathrm{Geo}(p)$. Find $\mathbb{E}X$ by the law of total expectation.

**Solution** Take the partition $A_1 = \{X = 1\}$, $A_2 = \{X > 1\}$. By memorylessness, $X - 1$ given $X > 1$ is again $\mathrm{Geo}(p)$, so $\mathbb{E}(X \mid X > 1) = 1 + \mathbb{E}X$. Hence

$$
\mathbb{E}X = 1\cdot p + (1 + \mathbb{E}X)(1 - p),
$$
and $\mathbb{E}X = 1/p$. This method, conditioning on the outcome of the first step, is called first-step analysis; it often turns the computation of an expectation into solving an equation.

**Example 9.2.4 (Gambler's Ruin)** A gambler starts with capital $a$ and resolves to stop as soon as he has won $b$ more; he must also stop when he is ruined. Each game is won with probability $\frac{1}{2}$, independently of the others, and each game wins or loses 1 unit. Find the expected number of games played until he stops.

**Solution** Let $m_i$ be the expected number of remaining games when the gambler holds $i$ units, so $m_0 = m_{a+b} = 0$. Conditioning on the outcome of the first game gives, for $0 < i < a + b$,

$$
m_i = \frac{1}{2}(1 + m_{i-1}) + \frac{1}{2}(1 + m_{i+1}),
$$
that is, the second difference is $(m_{i+1} - m_i) - (m_i - m_{i-1}) = -2$. Hence $m_i$ is a quadratic function of $i$, and the boundary conditions give $m_i = i(a + b - i)$; the required expected number of games is $m_a = ab$. (We have tacitly assumed that $m_i$ is finite; a more careful argument establishes this.)

## 9.3. Conditional Expectation Given a Random Variable

### 9.3.1. Definition

**Definition 9.3.1** In the discrete case, if $\sum_i \lvert x_i \rvert\mathbb{P}(X = x_i \mid Y = y) < \infty$, the conditional expectation of $X$ given $Y = y$ is

$$
\mathbb{E}(X \mid Y = y) = \sum_i x_i\,\mathbb{P}(X = x_i \mid Y = y);
$$
in the continuous case, if $\int \lvert x \rvert f_{X|Y}(x \mid y)\,\mathrm{d}x < \infty$, it is $\mathbb{E}(X \mid Y = y) = \int_{-\infty}^{\infty} x f_{X|Y}(x \mid y)\,\mathrm{d}x$.

$\mathbb{E}(X \mid Y = y)$ is a function of $y$. Substituting the random variable $Y$ for $y$ produces a new random variable.

**Definition 9.3.2 (Conditional Expectation)** Let $(X, Y)$ be a random vector with $\mathbb{E}\lvert X \rvert < \infty$, and let $m(y) = \mathbb{E}(X \mid Y = y)$. The random variable $m(Y)$ is called the **conditional expectation** of $X$ given $Y$ and is denoted $\mathbb{E}(X \mid Y)$.

To compute $\mathbb{E}(X \mid Y)$, treat $Y$ as a fixed value $y$, compute $m(y) = \mathbb{E}(X \mid Y = y)$, and then replace $y$ by $Y$ in the result. Since $\mathbb{E}(\cdot \mid Y = y)$ is simply an expectation under the conditional distribution, it has all the properties of expectation (linearity, monotonicity and so on). As long as the relevant expectations are well defined, $X$ and $Y$ need not both be discrete or both be continuous (compare the four cases of Bayes' theorem in §9.1), and $Y$ may also be a random vector.

**Example 9.3.1** Let $X, Y$ be i.i.d. $\mathrm{Poi}(\lambda)$. Find $\mathbb{E}(X + Y \mid X)$ and $\mathbb{E}(X \mid X + Y)$.

**Solution** Given $X = x$, independence implies that the conditional distribution of $Y$ is still $\mathrm{Poi}(\lambda)$, so $\mathbb{E}(X + Y \mid X = x) = x + \lambda$ and $\mathbb{E}(X + Y \mid X) = X + \lambda$.

Given $X + Y = n$, using $X + Y \sim \mathrm{Poi}(2\lambda)$ we get, for $0 \le k \le n$,

$$
\mathbb{P}(X = k \mid X + Y = n) = \frac{\mathbb{P}(X = k)\mathbb{P}(Y = n - k)}{\mathbb{P}(X + Y = n)} = \frac{\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda}\frac{\lambda^{n-k}}{(n-k)!}\mathrm{e}^{-\lambda}}{\frac{(2\lambda)^n}{n!}\mathrm{e}^{-2\lambda}} = \binom{n}{k}\Big(\frac{1}{2}\Big)^n,
$$
that is, $X \mid X + Y = n \sim \mathrm{Bin}(n, 1/2)$. Hence $\mathbb{E}(X \mid X + Y = n) = n/2$ and $\mathbb{E}(X \mid X + Y) = \frac{X + Y}{2}$. The second result can also be seen by symmetry: $\mathbb{E}(X \mid X + Y) = \mathbb{E}(Y \mid X + Y)$, and the two add up to $\mathbb{E}(X + Y \mid X + Y) = X + Y$.

**Example 9.3.2 (Height and Foot Length)** Let $X$ and $Y$ be the height and the foot length of an adult. It is common to model $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$. Find $\mathbb{E}(X \mid Y)$.

**Solution** By Example 6.5.2, given $Y = y$ we have $X \sim \mathcal{N}\big(\mu_1 + \rho\frac{\sigma_1}{\sigma_2}(y - \mu_2), (1 - \rho^2)\sigma_1^2\big)$, so

$$
\mathbb{E}(X \mid Y = y) = \mu_1 + \rho\frac{\sigma_1}{\sigma_2}(y - \mu_2), \qquad \mathbb{E}(X \mid Y) = \mu_1 + \rho\frac{\sigma_1}{\sigma_2}(Y - \mu_2).
$$
From the length $y$ of a footprint left at a crime scene, $\mathbb{E}(X \mid Y = y)$ gives an estimate of the suspect's height. The linear regression model of statistics rests on exactly this idea of conditional expectation ([3.3](/3.3)).

**Example 9.3.3** Let $X, Y$ be independent $\mathrm{Exp}(\lambda)$ and $Z = X + Y$. Find the conditional density $f_{X|Z}(x \mid z)$ and $\mathbb{E}(X^2 \mid Z)$.

**Solution** Applying Theorem 7.1.4 to the transformation $(x, z) = (x, x + y)$ (whose Jacobian determinant is 1), the joint density of $(X, Z)$ is $f(x, z) = \lambda\mathrm{e}^{-\lambda x}\cdot\lambda\mathrm{e}^{-\lambda(z - x)} = \lambda^2\mathrm{e}^{-\lambda z}$ for $0 < x < z$. Note the support: on $0 < x < z$ the joint density does not depend on $x$. Since $Z \sim \Gamma(2, \lambda)$ with $f_Z(z) = \lambda^2 z\mathrm{e}^{-\lambda z}$,

$$
f_{X|Z}(x \mid z) = \frac{\lambda^2\mathrm{e}^{-\lambda z}}{\lambda^2 z\mathrm{e}^{-\lambda z}} = \frac{1}{z}, \quad 0 < x < z,
$$
that is, $X \mid Z = z \sim \mathrm{U}(0, z)$. Therefore $\mathbb{E}(X^2 \mid Z = z) = z^2/3$ and $\mathbb{E}(X^2 \mid Z) = Z^2/3$.

### 9.3.2. The Law of Iterated Expectations

The conditional expectation $\mathbb{E}(X \mid Y)$ is "the average within each group when the population is grouped by $Y$". Suppose that in some population the foot lengths 24, 25 and 26 cm occur with proportions 0.1, 0.6 and 0.3, and the average heights of the three groups are 165, 175 and 180 cm. Then $\mathbb{E}(X \mid Y)$ takes the values 165, 175, 180 with probabilities 0.1, 0.6, 0.3, and the average height of the whole population is the weighted average of the group averages, $165 \times 0.1 + 175 \times 0.6 + 180 \times 0.3 = 175.5$ cm. This is the content of the following theorem.

**Theorem 9.3.1 (Law of Iterated Expectations)** Let $X, Y$ be random variables with $\mathbb{E}\lvert X \rvert < \infty$. Then

$$
\mathbb{E}[\mathbb{E}(X \mid Y)] = \mathbb{E}X.
$$

**Proof** Discrete case: write $m(y) = \mathbb{E}(X \mid Y = y)$ and interchange the order of summation (justified by absolute convergence):

$$
\mathbb{E}[\mathbb{E}(X \mid Y)] = \sum_y m(y)p_Y(y) = \sum_y\Big(\sum_x x\,p_{X|Y}(x \mid y)\Big)p_Y(y) = \sum_x x\sum_y p_{X,Y}(x, y) = \sum_x x\,p_X(x) = \mathbb{E}X.
$$
In the continuous case replace sums by integrals and use $f_{X|Y}(x \mid y)f_Y(y) = f(x, y)$ together with Fubini's theorem. $\square$

Theorem 9.2.2 is the special case in which $Y$ takes $n$ values ($Y = i$ if and only if $A_i$ occurs); both are referred to as the law of total expectation, also known as the tower property. It is especially useful in hierarchical models (such as Bayesian networks): first compute conditionally on the upper-level variables, then average over them.

**Example 9.3.4 (Escape Room)** A player is lost in an escape room with three doors. The first door leads to a tunnel that reaches the exit after 3 hours; the second leads to a tunnel that returns to the starting point after 5 hours; the third leads to a tunnel that returns to the starting point after 7 hours. Each time he chooses one of the three doors with equal probability (he does not remember which doors he has tried). Find the expected time until he reaches the exit.

**Solution** Let $X$ be the time needed to reach the exit and $Y$ the number of the door chosen first, with $\mathbb{P}(Y = i) = \frac{1}{3}$. After returning to the starting point the situation is exactly as at the beginning, so

$$
\mathbb{E}(X \mid Y = 1) = 3, \quad \mathbb{E}(X \mid Y = 2) = 5 + \mathbb{E}X, \quad \mathbb{E}(X \mid Y = 3) = 7 + \mathbb{E}X.
$$
By the law of total expectation, $\mathbb{E}X = \frac{1}{3}[3 + (5 + \mathbb{E}X) + (7 + \mathbb{E}X)]$, whence $\mathbb{E}X = 15$ hours.

**Example 9.3.5** Continuing Example 6.5.3: $Y \sim \Gamma(\alpha, \lambda)$, and given $Y = y$, $X \sim \mathrm{Exp}(y)$. Find $\mathbb{E}(X \mid Y)$, $\mathbb{E}(Y \mid X)$ and $\mathbb{E}X$.

**Solution** Given $Y = y$, $\mathbb{E}(X \mid Y = y) = \int_0^{\infty} x\cdot y\mathrm{e}^{-xy}\,\mathrm{d}x = \frac{1}{y}$, so $\mathbb{E}(X \mid Y) = \frac{1}{Y}$.

By Example 6.5.3, $f_X(x) = \frac{\alpha\lambda^\alpha}{(x + \lambda)^{\alpha+1}}$, so given $X = x$,

$$
f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)} = \frac{(x + \lambda)^{\alpha+1}}{\Gamma(\alpha + 1)}y^{\alpha}\mathrm{e}^{-(x + \lambda)y}, \quad y > 0,
$$
which is the density of $\Gamma(\alpha + 1, x + \lambda)$. Hence $\mathbb{E}(Y \mid X = x) = \frac{\alpha + 1}{x + \lambda}$ and $\mathbb{E}(Y \mid X) = \frac{\alpha + 1}{X + \lambda}$. This is precisely a conjugate update in Bayesian inference: after a lifetime $x$ is observed, the distribution of the environmental index is updated from $\Gamma(\alpha, \lambda)$ to $\Gamma(\alpha + 1, \lambda + x)$.

Finally, by the law of iterated expectations,

$$
\mathbb{E}X = \mathbb{E}[\mathbb{E}(X \mid Y)] = \mathbb{E}Y^{-1} = \int_0^{\infty}\frac{1}{y}\cdot\frac{\lambda^\alpha}{\Gamma(\alpha)}y^{\alpha-1}\mathrm{e}^{-\lambda y}\,\mathrm{d}y = \begin{cases} \dfrac{\lambda\Gamma(\alpha - 1)}{\Gamma(\alpha)} = \dfrac{\lambda}{\alpha - 1}, & \alpha > 1, \\ \infty, & 0 < \alpha \le 1. \end{cases}
$$
For $\alpha \le 1$ the integral diverges near $y = 0$. The law of iterated expectations is simpler here than integrating against $f_X$ directly.

### 9.3.3. Properties of Conditional Expectation

**Theorem 9.3.2** Let $X, Y$ be random variables and $g(x)$, $h(y)$ real functions, with $\mathbb{E}\lvert X \rvert < \infty$, $\mathbb{E}\lvert g(X) \rvert < \infty$, and let $X_1, \dots, X_n$ have finite expectations. Then

1. $\lvert\mathbb{E}(X \mid Y)\rvert \le \mathbb{E}(\lvert X \rvert \mid Y)$;
2. $[\mathbb{E}(X \mid Y)]^2 \le \mathbb{E}(X^2 \mid Y)$;
3. $\mathbb{E}[h(Y)g(X) \mid Y] = h(Y)\,\mathbb{E}[g(X) \mid Y]$ (provided the left-hand side is defined);
4. $\mathbb{E}[\mathbb{E}(g(X) \mid Y)] = \mathbb{E}g(X)$;
5. if $X$ and $Y$ are independent, then $\mathbb{E}[g(X) \mid Y] = \mathbb{E}g(X)$;
6. $\mathbb{E}\big(c + \sum_{i=1}^n c_iX_i \mid Y\big) = c + \sum_{i=1}^n c_i\mathbb{E}(X_i \mid Y)$;
7. if $X_1 \le X_2$, then $\mathbb{E}(X_1 \mid Y) \le \mathbb{E}(X_2 \mid Y)$.

**Proof** Each identity and inequality is verified for every $y$ under the conditional distribution. Items 1, 2, 6 and 7 are the conditional versions of the properties $\lvert\mathbb{E}X\rvert \le \mathbb{E}\lvert X \rvert$, $(\mathbb{E}X)^2 \le \mathbb{E}X^2$ (Jensen's inequality), linearity and monotonicity of expectation. Item 3: given $Y = y$, $h(Y) = h(y)$ is a constant and can be taken outside the expectation. Item 4 is the law of iterated expectations applied to $g(X)$. Item 5: under independence the conditional distribution of $X$ equals its unconditional distribution (Theorems 6.5.1 and 6.5.2). $\square$

Property 3 says that, given $Y$, functions of $Y$ may be treated as constants. Combined with the law of iterated expectations it is often used to compute expectations of products: $\mathbb{E}[h(Y)X] = \mathbb{E}[h(Y)\mathbb{E}(X \mid Y)]$.

**Example 9.3.6** If $\mathbb{E}X^2 < \infty$ and $\mathbb{E}h^2(Y) < \infty$, then

$$
\mathbb{E}\big[(X - \mathbb{E}(X \mid Y))h(Y)\big] = 0.
$$

**Proof** By the Cauchy–Schwarz inequality, $\mathbb{E}\lvert Xh(Y) \rvert \le \sqrt{\mathbb{E}X^2\,\mathbb{E}h^2(Y)} < \infty$. By property 3 and the law of iterated expectations,

$$
\mathbb{E}[\mathbb{E}(X \mid Y)h(Y)] = \mathbb{E}[\mathbb{E}(Xh(Y) \mid Y)] = \mathbb{E}[Xh(Y)],
$$
and subtracting gives the claim. $\square$

Geometrically, regard random variables with finite variance as vectors with inner product $\mathbb{E}(UV)$. The random variables of the form $h(Y)$ form a subspace, and Example 9.3.6 says that $X - \mathbb{E}(X \mid Y)$ is orthogonal to this subspace: $\mathbb{E}(X \mid Y)$ is the **orthogonal projection** of $X$ onto the space of functions of $Y$. This yields the most important interpretation of conditional expectation.

**Theorem 9.3.3 (Best Predictor)** Let $\mathbb{E}X^2 < \infty$ and $m(Y) = \mathbb{E}(X \mid Y)$. Then for every real function $g(y)$,

$$
\mathbb{E}[X - m(Y)]^2 \le \mathbb{E}[X - g(Y)]^2,
$$
with equality if and only if $g(Y) = m(Y)$ a.s.

**Proof** If $\mathbb{E}g^2(Y) = \infty$, the inequality $b^2 \le 2(a - b)^2 + 2a^2$ gives $\infty = \mathbb{E}g^2(Y) \le 2\mathbb{E}[X - g(Y)]^2 + 2\mathbb{E}X^2$, so the right-hand side is $\infty$ and the inequality holds. Now let $\mathbb{E}g^2(Y) < \infty$. By property 2 and the law of iterated expectations, $\mathbb{E}m^2(Y) \le \mathbb{E}X^2 < \infty$; put $h(Y) = m(Y) - g(Y)$, so that $\mathbb{E}h^2(Y) < \infty$. By Example 9.3.6 the cross term vanishes:

$$
\mathbb{E}[X - g(Y)]^2 = \mathbb{E}[X - m(Y)]^2 + \mathbb{E}[m(Y) - g(Y)]^2 + 2\mathbb{E}\big[(X - m(Y))h(Y)\big] = \mathbb{E}[X - m(Y)]^2 + \mathbb{E}[m(Y) - g(Y)]^2 \ge \mathbb{E}[X - m(Y)]^2.
$$
Equality holds if and only if $\mathbb{E}[m(Y) - g(Y)]^2 = 0$, that is, $g(Y) = m(Y)$ a.s. $\square$

We call $\mathbb{E}(X \mid Y)$ the best predictor of $X$ from $Y$. This generalizes Theorem 8.2.4 (the expectation is the best constant predictor): the more information $Y$ carries, the more predictors are available and the smaller the mean squared error. The trick in the proof, adding and subtracting a term to produce a cross term with zero mean, is a standard technique for expectations of quadratic forms.

**Example 9.3.7** Let $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$. By Example 9.3.2 the best predictor $\mathbb{E}(X \mid Y) = \mu_1 + \rho\frac{\sigma_1}{\sigma_2}(Y - \mu_2)$ is a linear function of $Y$, so for the normal distribution the best predictor coincides with the best linear predictor ([3.1.10](/3.1.10)). For general distributions $\mathbb{E}(X \mid Y)$ may be nonlinear, and the best linear predictor is only an approximation to it.

![A nonlinear case: the dots are simulated samples of (Y, X), the solid curve is the conditional expectation E(X | Y = y) and the dashed line is the best linear predictor](./plots/conditional-mean.py)

**Example 9.3.8** Let $X, Y$ have finite second moments with $\mathbb{E}(X \mid Y) = Y$ and $\mathbb{E}(Y \mid X) = X$. Then $X = Y$ a.s.

**Proof** By property 3 and the law of iterated expectations, $\mathbb{E}(XY) = \mathbb{E}[Y\mathbb{E}(X \mid Y)] = \mathbb{E}Y^2$, and likewise $\mathbb{E}(XY) = \mathbb{E}X^2$. Therefore

$$
\mathbb{E}(X - Y)^2 = \mathbb{E}X^2 - 2\mathbb{E}(XY) + \mathbb{E}Y^2 = 0,
$$
and $X = Y$ a.s. by Example 8.2.8. $\square$

## 9.4. Conditional Variance

### 9.4.1. Definition and the Law of Total Variance

**Definition 9.4.1 (Conditional Variance)** If $\mathbb{E}\big[(X - \mathbb{E}(X \mid Y))^2 \mid Y\big]$ exists, it is called the **conditional variance** of $X$ given $Y$ and is denoted

$$
\operatorname{Var}(X \mid Y) := \mathbb{E}\big[(X - \mathbb{E}(X \mid Y))^2 \mid Y\big].
$$
Correspondingly, $\operatorname{Var}(X \mid Y = y) = \mathbb{E}\big[(X - \mathbb{E}(X \mid Y = y))^2 \mid Y = y\big]$ is the variance of the conditional distribution.

As with the ordinary variance, $\operatorname{Var}(X \mid Y) = \mathbb{E}(X^2 \mid Y) - [\mathbb{E}(X \mid Y)]^2$. Taking the expectation of this quantity and the variance of $\mathbb{E}(X \mid Y)$ gives

$$
\mathbb{E}[\operatorname{Var}(X \mid Y)] = \mathbb{E}X^2 - \mathbb{E}[\mathbb{E}(X \mid Y)]^2, \qquad \operatorname{Var}[\mathbb{E}(X \mid Y)] = \mathbb{E}[\mathbb{E}(X \mid Y)]^2 - (\mathbb{E}X)^2,
$$
and adding the two, the middle terms cancel and we obtain $\operatorname{Var}(X)$.

**Theorem 9.4.1 (Law of Total Variance)** If $\mathbb{E}X^2 < \infty$, then

$$
\operatorname{Var}(X) = \mathbb{E}[\operatorname{Var}(X \mid Y)] + \operatorname{Var}[\mathbb{E}(X \mid Y)].
$$

**Proof** Here is a second proof. Insert $\mathbb{E}(X \mid Y)$ and note that $\mathbb{E}X = \mathbb{E}[\mathbb{E}(X \mid Y)]$:

$$
\operatorname{Var}(X) = \mathbb{E}\big[(X - \mathbb{E}(X \mid Y)) + (\mathbb{E}(X \mid Y) - \mathbb{E}X)\big]^2 = \mathbb{E}[X - \mathbb{E}(X \mid Y)]^2 + \operatorname{Var}[\mathbb{E}(X \mid Y)],
$$
where the cross term vanishes by Example 9.3.6 (with $h(Y) = \mathbb{E}(X \mid Y) - \mathbb{E}X$). Finally, by the law of iterated expectations, $\mathbb{E}[X - \mathbb{E}(X \mid Y)]^2 = \mathbb{E}\big[\mathbb{E}[(X - \mathbb{E}(X \mid Y))^2 \mid Y]\big] = \mathbb{E}[\operatorname{Var}(X \mid Y)]$. $\square$

The total variability splits into "the average variability within groups" and "the variability between group averages". This is the prototype of the sum-of-squares decompositions in the analysis of variance and in linear regression. It also shows that $\operatorname{Var}[\mathbb{E}(X \mid Y)] \le \operatorname{Var}(X)$: replacing a random variable by its conditional expectation keeps the expectation and does not increase the variance, which is the heart of the Rao–Blackwell theorem ([3.2.3](/3.2.3)).

![The law of total variance: for three groups of data, the mean of the within-group variances plus the variance of the group means equals the total variance](./plots/total-variance.py)

**Example 9.4.1 (Sum of a Random Number of Random Variables)** Let $Y$ be the number of students at a university who will take probability theory next year, let $X_i$ be the number of papers that the $i$-th student writes in the following five years, and let $X = X_1 + \cdots + X_Y$ be the total number of papers written by these students. Assume that $X_1, X_2, \dots$ are i.i.d. and independent of $Y$, and that $\mathbb{E}X_1$, $\mathbb{E}Y$, $\operatorname{Var}(X_1)$ and $\operatorname{Var}(Y)$ are known. Find the expectation and variance of $X$.

**Solution** Given $Y = n$, independence implies that $X$ has the same distribution as $X_1 + \cdots + X_n$, so

$$
\mathbb{E}(X \mid Y = n) = n\mathbb{E}X_1, \qquad \operatorname{Var}(X \mid Y = n) = n\operatorname{Var}(X_1),
$$
and therefore $\mathbb{E}(X \mid Y) = Y\mathbb{E}X_1$ and $\operatorname{Var}(X \mid Y) = Y\operatorname{Var}(X_1)$. By the law of iterated expectations and the law of total variance,

$$
\mathbb{E}X = \mathbb{E}Y\cdot\mathbb{E}X_1, \qquad \operatorname{Var}(X) = \mathbb{E}[Y\operatorname{Var}(X_1)] + \operatorname{Var}(Y\mathbb{E}X_1) = \mathbb{E}Y\cdot\operatorname{Var}(X_1) + (\mathbb{E}X_1)^2\operatorname{Var}(Y).
$$
The two terms of the variance come from the randomness of each student's output and from the randomness of the enrollment, respectively.

## Summary

| | Given an event $A$ | Given a random variable $Y$ |
|---|---|---|
| Definition | $\mathbb{E}(X \mid A) = \sum x_i\mathbb{P}(X = x_i \mid A)$ or $\int x f_{X\mid A}(x)\,\mathrm{d}x$ | $\mathbb{E}(X \mid Y) = m(Y)$, $m(y) = \mathbb{E}(X \mid Y = y)$ |
| Computation | $\mathbb{E}(X \mid A) = \mathbb{E}(X\boldsymbol{1}_A)/\mathbb{P}(A)$ | Fix $Y = y$, compute, then replace $y$ by $Y$ |
| From conditional to unconditional | $\mathbb{E}X = \sum_i\mathbb{P}(A_i)\mathbb{E}(X \mid A_i)$ | $\mathbb{E}X = \mathbb{E}[\mathbb{E}(X \mid Y)]$ |
| Meaning | Average given that $A$ has occurred | Best predictor of $X$ from $Y$ (orthogonal projection) |

- Conditional variance $\operatorname{Var}(X \mid Y) = \mathbb{E}(X^2 \mid Y) - [\mathbb{E}(X \mid Y)]^2$; law of total variance $\operatorname{Var}(X) = \mathbb{E}[\operatorname{Var}(X \mid Y)] + \operatorname{Var}[\mathbb{E}(X \mid Y)]$.
- Given $Y$, functions of $Y$ behave as constants: $\mathbb{E}[h(Y)X \mid Y] = h(Y)\mathbb{E}(X \mid Y)$.
- Techniques: first-step analysis (condition on the first step and solve an equation); symmetry (as in $\mathbb{E}(X \mid X + Y) = \frac{X + Y}{2}$); interchanging sums or integrals; adding and subtracting a term in the expectation of a quadratic form to produce a cross term with zero mean.
