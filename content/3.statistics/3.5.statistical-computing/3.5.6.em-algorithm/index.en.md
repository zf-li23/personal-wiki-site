---
title: The EM Algorithm
description: Latent variables and complete data, the E-step and the M-step, the ascent property via Jensen's inequality and the decomposition into the evidence lower bound and a Kullback–Leibler divergence, worked examples (two coins, heights, a genetic linkage multinomial), generalized and variational EM, the rate of convergence and Louis's acceleration, and EM for Gaussian and two-component mixtures.
---

Observed data are often incomplete: values are missing, labels are hidden, or the model is most naturally described through quantities we never see. The likelihood of the observed data then contains a sum or an integral inside the logarithm and has no closed-form maximizer, and Newton-type methods ([3.5.5](/3.5.5)) need derivatives of this awkward function and can be unstable in high dimensions. The **EM algorithm**, introduced for Gaussian mixtures in [3.4.11](/3.4.11), turns such problems into a sequence of easy ones: the E-step completes the data by a conditional expectation given the current parameter, and the M-step maximizes the completed log-likelihood. This chapter develops the general theory: why each iteration increases the likelihood (Jensen's inequality, or the decomposition of the log-likelihood into the evidence lower bound and a **Kullback–Leibler divergence**), how fast it converges and how to accelerate it (Louis's method, linked to the observed and complete information), and two extensions, generalized EM and variational EM, that lead toward approximate Bayesian inference ([3.7](/3.7)). The last part applies EM to mixture models. Throughout, EM is a method for computing the MLE of [3.2.3](/3.2.3), nothing more.

## 6.1. Basic Principles of the EM Algorithm

### 6.1.1. Latent Variables

**Example 6.1.1 (One Coin)** A coin has $\mathbb{P}(H) = \theta$ and $\mathbb{P}(T) = 1 - \theta$. To estimate $\theta$ we flip it $n$ times and get $h$ heads and $n - h$ tails. The likelihood is binomial, $L(\theta) = \binom{n}{h}\theta^h(1 - \theta)^{n-h}$; differentiating and setting the derivative to zero gives the maximum likelihood estimate $\hat\theta = h/n$, the natural estimate.

**Example 6.1.2 (Two Coins, Complete Data)** Now there are two coins $A$ and $B$, and the goal is to estimate $\theta_A$ and $\theta_B$. Five times, one of the coins is chosen, $Z_i \in \{A, B\}$, $i = 1, \dots, 5$, and tossed 10 times:

| Round $i$ | Coin $Z_i$ | Result |
|---|---|---|
| 1 | $B$ | 5 H, 5 T |
| 2 | $A$ | 9 H, 1 T |
| 3 | $A$ | 8 H, 2 T |
| 4 | $B$ | 4 H, 6 T |
| 5 | $A$ | 7 H, 3 T |

The likelihood (without binomial coefficients) is the product of the five rounds,

$$
L(\boldsymbol{\theta}) = \theta_B^5(1 - \theta_B)^5\cdot\theta_A^9(1 - \theta_A)\cdot\theta_A^8(1 - \theta_A)^2\cdot\theta_B^4(1 - \theta_B)^6\cdot\theta_A^7(1 - \theta_A)^3 = \theta_A^{24}(1 - \theta_A)^6\,\theta_B^9(1 - \theta_B)^{11},
$$
so the MLE is the proportion of heads for each coin,

$$
\hat\theta_A = \frac{\#\text{heads using }A}{\#\text{flips using }A} = \frac{24}{24 + 6} = 0.8, \qquad \hat\theta_B = \frac{\#\text{heads using }B}{\#\text{flips using }B} = \frac{9}{9 + 11} = 0.45.
$$

What if we do not know the identities of the coins used in each round? The likelihood becomes $\theta_{Z_1}^5(1 - \theta_{Z_1})^5\,\theta_{Z_2}^9(1 - \theta_{Z_2})\cdots$ with unknown $Z_i$, and $\arg\max_{\boldsymbol{\theta}}L(\boldsymbol{\theta})$ cannot be computed in one step: this is a missing data problem. With complete data the MLE is a frequency; with the coin labels missing, the observed-data likelihood contains the unknown $Z$ and is hard to maximize directly. The way out is to treat the unknown $Z$ as a random variable and to complete the data by weighting with its posterior probabilities.

**Definition 6.1.1 (Latent Variables and Complete Data)** In the EM framework, $X$ is the observed variable (the observed values of the sample) and $Z$ is a **latent variable** (hidden variable), such as the class label of an observation, which influences the data but is not observed. The observed data $X$ are the **incomplete data**, and $Y = (X, Z)$ are the **complete data**. With $\theta$ the parameter to be estimated, the observed-data log-likelihood is $\ell(\theta; x) = \log p(x \mid \theta)$ and the complete-data log-likelihood is $\ell_c(\theta; x, Z) = \log p(x, Z \mid \theta)$.

Observed variables are directly measurable: the waveform of a speech recording, whether it is raining today, whether the smoke alarm went off. Hidden variables (also called latent factors) influence the data but are not trivial to measure: the phonemes that produce the recording, the probability of rain today given rain yesterday, whether the smoke alarm is malfunctioning. The complete data $Y = (X, Z)$ are the data we wish we had.

Consider the inverse problem: given $(\theta_A, \theta_B) = (0.6, 0.5)$ and equal prior probabilities $\mathbb{P}(Z_i = A) = \mathbb{P}(Z_i = B) = 1/2$, the first round shows 5 H and 5 T. By **Bayes' theorem** the coin used was $A$ with probability

$$
\mathbb{P}(Z_1 = A \mid x_1) = \frac{\mathbb{P}(x_1 \mid Z_1 = A)\,\mathbb{P}(Z_1 = A)}{\mathbb{P}(x_1 \mid Z_1 = A)\,\mathbb{P}(Z_1 = A) + \mathbb{P}(x_1 \mid Z_1 = B)\,\mathbb{P}(Z_1 = B)} = \frac{0.6^5\times0.4^5}{0.6^5\times0.4^5 + 0.5^5\times0.5^5} \approx 0.45,
$$
and $B$ with probability $0.55$. The EM algorithm iterates between such posterior probabilities of the hidden labels and the estimates of the parameters.

### 6.1.2. The Algorithm

Recall the **conditional expectation**. In regression, $Y = f(X) + \varepsilon$ with $\mathbb{E}\varepsilon = 0$ gives $\mathbb{E}(Y \mid X) = f(X)$. For a discrete random variable $Z$ with distribution $P_Z$, $\mathbb{E}[Z] = \sum_z z\mathbb{P}_Z(z)$ and $\mathbb{E}[h(Z)] = \sum_z\mathbb{P}_Z(z)h(z)$; given a particular value $X = x$, $\mathbb{E}[h(Z) \mid x] = \sum_z\mathbb{P}_{Z\mid X}(z \mid x)h(z)$. Here we need

$$
\mathbb{E}_{Z\mid x, \hat\theta^{(t)}}\bigl[\log \mathbb{P}(x, Z \mid \theta)\bigr] = \sum_z\mathbb{P}_{Z\mid X}(z \mid x, \hat\theta^{(t)})\log \mathbb{P}(x, z \mid \theta):
$$
first we infer from the observed data $x$ the probability of the unobserved $z$, $\mathbb{P}_{Z\mid X}(z \mid x, \theta = \hat\theta^{(t)})$, and then take the expectation of the complete-data log-likelihood under it.

**Definition 6.1.2 (EM Algorithm)** Make an initial estimate $\hat\theta^{(0)}$ of $\theta$ and repeat until convergence:

1. E-step: compute the **Q-function**
   $$
   Q(\theta \mid \hat\theta^{(t)}) \triangleq \mathbb{E}_{Z\mid x, \hat\theta^{(t)}}\bigl[\log \mathbb{P}(x, Z \mid \theta)\bigr] = \sum_z\mathbb{P}_{Z\mid X}(z \mid x, \theta = \hat\theta^{(t)})\log \mathbb{P}(x, z \mid \theta),
   $$
   the expected complete-data log-likelihood under the posterior distribution of the latent variable at the current parameter;
2. M-step: $\hat\theta^{(t+1)} = \arg\max_\theta Q(\theta \mid \hat\theta^{(t)})$.

A typical stopping criterion is $\lVert\hat\theta^{(t+1)} - \hat\theta^{(t)}\rVert < \varepsilon$. For continuous $Z$ the sum is an integral. In practice the data are $x_1, \dots, x_n$, assumed i.i.d., and the expectation is summed over the points: $Q(\theta \mid \theta^{(t)}) = \sum_{i=1}^n\sum_z\mathbb{P}_{Z\mid X}(z \mid x_i, \theta^{(t)})\log \mathbb{P}(x_i, z \mid \theta)$.

**Example 6.1.3 (Two Coins, Hidden Labels)** Initialize $\theta_A^{(0)} = 0.6$ and $\theta_B^{(0)} = 0.5$ and compute, as above, the posterior probabilities $w_{iA} = \mathbb{P}(Z_i = A \mid x_i, \boldsymbol{\theta}^{(0)})$ for all five rounds. In the E-step they give the expected numbers of heads and tails attributed to each coin:

| Round $i$ | Result | $w_{iA}$ | $w_{iB}$ | Expected for coin $A$ | Expected for coin $B$ |
|---|---|---|---|---|---|
| 1 | 5 H, 5 T | 0.45 | 0.55 | 2.2 H, 2.2 T | 2.8 H, 2.8 T |
| 2 | 9 H, 1 T | 0.80 | 0.20 | 7.2 H, 0.8 T | 1.8 H, 0.2 T |
| 3 | 8 H, 2 T | 0.73 | 0.27 | 5.9 H, 1.5 T | 2.1 H, 0.5 T |
| 4 | 4 H, 6 T | 0.35 | 0.65 | 1.4 H, 2.1 T | 2.6 H, 3.9 T |
| 5 | 7 H, 3 T | 0.65 | 0.35 | 4.5 H, 1.9 T | 2.5 H, 1.1 T |
| Total | | | | 21.3 H, 8.6 T | 11.7 H, 8.4 T |

Formally, with $x_i$ heads in $n_i = 10$ tosses, the complete-data log-likelihood is (up to the constant from the prior $1/2$)

$$
\log \mathbb{P}(x, Z \mid \boldsymbol{\theta}) = \sum_{i=1}^5\bigl[x_i\log\theta_{Z_i} + (n_i - x_i)\log(1 - \theta_{Z_i})\bigr],
$$
and its conditional expectation weights each round by $w_{iA}$ and $w_{iB} = 1 - w_{iA}$:

$$
\begin{aligned}
Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(0)}) &= 0.45\bigl[5\log\theta_A + 5\log(1 - \theta_A)\bigr] + 0.55\bigl[5\log\theta_B + 5\log(1 - \theta_B)\bigr] \\
&\quad + 0.80\bigl[9\log\theta_A + \log(1 - \theta_A)\bigr] + 0.20\bigl[9\log\theta_B + \log(1 - \theta_B)\bigr] + \cdots \\
&= 21.3\log\theta_A + 8.6\log(1 - \theta_A) + 11.7\log\theta_B + 8.4\log(1 - \theta_B),
\end{aligned}
$$
a decoupled objective. The M-step maximizes it, which is the complete-data MLE with expected counts:

$$
\theta_A^{(1)} = \frac{21.3}{21.3 + 8.6} = 0.71, \qquad \theta_B^{(1)} = \frac{11.7}{11.7 + 8.4} = 0.58.
$$
Repeating the two steps, the estimates converge to $(\hat\theta_A, \hat\theta_B) \approx (0.797, 0.520)$, reached to three decimals after about ten iterations.

### 6.1.3. Convergence

Write $p$ for densities and integrals for sums. The difficulty of maximum likelihood with latent variables is the logarithm of a sum, $\log p(x \mid \theta) = \log\sum_zp(x, z \mid \theta)$. For any distribution $H(z)$ (a probability mass function, $H(z) \ge 0$, $\sum_zH(z) = 1$, positive where $p(x, z \mid \theta) > 0$), by **Jensen's inequality** for the concave logarithm,

$$
\log p(x \mid \theta) = \log\sum_zH(z)\frac{p(x, z \mid \theta)}{H(z)} = \log\mathbb{E}_{z\sim H}\left[\frac{p(x, z \mid \theta)}{H(z)}\right] \ge \mathbb{E}_{z\sim H}\left[\log\frac{p(x, z \mid \theta)}{H(z)}\right] = \sum_zH(z)\log\frac{p(x, z \mid \theta)}{H(z)}.
$$
Equality holds in Jensen's inequality iff the random variable is constant, i.e. iff $p(x, z \mid \theta)/H(z) = c$ for all $z$. Then $\sum_zp(x, z \mid \theta) = c\sum_zH(z) = c$, so

$$
H(z) = \frac{p(x, z \mid \theta)}{\sum_{z'}p(x, z' \mid \theta)} = p(z \mid x, \theta),
$$
the posterior distribution of the latent variable (in the continuous case $h(z) = f(x, z \mid \theta)/\int f(x, z \mid \theta)\,\mathrm{d}z = f_{Z\mid X}(z \mid x, \theta)$). Maximizing $\log p(x \mid \theta)$ thus becomes maximizing $\mathbb{E}_{Z\mid x}\bigl[\log\frac{p(x, Z \mid \theta)}{p(Z \mid x, \theta)}\bigr]$ with the posterior at the current parameter. Taking $H(z) = p(z \mid x, \hat\theta^{(t)})$ defines the surrogate function

$$
g_t(\theta) = \sum_zp(z \mid x, \hat\theta^{(t)})\log\frac{p(x, z \mid \theta)}{p(z \mid x, \hat\theta^{(t)})} = Q(\theta \mid \hat\theta^{(t)}) - \sum_zp(z \mid x, \hat\theta^{(t)})\log p(z \mid x, \hat\theta^{(t)}),
$$
which satisfies $g_t(\theta) \le \log p(x \mid \theta)$ for all $\theta$ and $g_t(\hat\theta^{(t)}) = \log p(x \mid \hat\theta^{(t)})$. The second term does not depend on $\theta$, so maximizing $g_t$ is the M-step.

**Theorem 6.1.1 (Ascent Property of EM)** Each EM iteration does not decrease the observed-data likelihood: $p(x \mid \hat\theta^{(t+1)}) \ge p(x \mid \hat\theta^{(t)})$.

**Proof** Since $\hat\theta^{(t+1)} = \arg\max_\theta g_t(\theta)$, $g_t(\hat\theta^{(t+1)}) \ge g_t(\hat\theta^{(t)})$. Hence

$$
\log p(x \mid \hat\theta^{(t+1)}) \ge g_t(\hat\theta^{(t+1)}) \ge g_t(\hat\theta^{(t)}) = \log p(x \mid \hat\theta^{(t)}). \qquad\square
$$

The same result can be organized around a decomposition of the log-likelihood that holds for every distribution $q(z)$:

$$
\begin{aligned}
\ell(\theta) = \log p(x \mid \theta) &= \int q(z)\log p(x \mid \theta)\,\mathrm{d}z = \int q(z)\log\frac{p(x, z \mid \theta)}{p(z \mid x, \theta)}\,\mathrm{d}z = \int q(z)\log\frac{p(x, z \mid \theta)\,q(z)}{p(z \mid x, \theta)\,q(z)}\,\mathrm{d}z \\
&= \int q(z)\log\frac{p(x, z \mid \theta)}{q(z)}\,\mathrm{d}z + \int q(z)\log\frac{q(z)}{p(z \mid x, \theta)}\,\mathrm{d}z \triangleq F(q, \theta) + \operatorname{KL}\bigl(q \,\Vert\, p(\cdot \mid x, \theta)\bigr).
\end{aligned}
$$

**Definition 6.1.3 (Evidence Lower Bound)** For a distribution $q$ of the latent variable, the functional

$$
F(q, \theta) = \int q(z)\log\frac{p(x, z \mid \theta)}{q(z)}\,\mathrm{d}z = \mathbb{E}_q\bigl[\log p(x, Z \mid \theta)\bigr] - \mathbb{E}_q\bigl[\log q(Z)\bigr]
$$
is the **evidence lower bound** (ELBO).

The Kullback–Leibler divergence $\operatorname{KL}(q \Vert p) = \int q(z)\log\frac{q(z)}{p(z)}\,\mathrm{d}z$, or relative entropy, measures how one distribution differs from a reference distribution. It is nonnegative, so $F(q, \theta) \le \log p(x \mid \theta)$, the evidence: in the earlier notation, $F(q, \theta) = \mathbb{E}_q\bigl[\log\frac{p(x, Z \mid \theta)}{q(Z)}\bigr] \le \log\mathbb{E}_q\bigl[\frac{p(x, Z \mid \theta)}{q(Z)}\bigr] = \log p(x \mid \theta)$.

**Lemma 6.1.1** For densities $p$ and $q$, $\operatorname{KL}(q \Vert p) \ge 0$, with equality iff $q = p$ almost everywhere.

**Proof** Use $\ln x \le x - 1$ for all $x > 0$, with equality only at $x = 1$:

$$
-\operatorname{KL}(q \Vert p) = \int q(z)\log\frac{p(z)}{q(z)}\,\mathrm{d}z \le \int q(z)\left(\frac{p(z)}{q(z)} - 1\right)\mathrm{d}z = \int p(z)\,\mathrm{d}z - \int q(z)\,\mathrm{d}z \le 0,
$$
the integrals being over the set where $q > 0$. $\square$

In this language, the E-step sets $q$ to the posterior, which makes the KL term zero, and the M-step maximizes $F$ in $\theta$:

$$
\ell(\hat\theta^{(t)}) \overset{\text{E-step}}{=} F(\hat q^{(t+1)}, \hat\theta^{(t)}) \overset{\text{M-step}}{\le} F(\hat q^{(t+1)}, \hat\theta^{(t+1)}) \overset{\text{KL} \ge 0}{\le} \ell(\hat\theta^{(t+1)}), \qquad \hat q^{(t+1)} = p(\cdot \mid x, \hat\theta^{(t)}).
$$
The ascent property shows that as long as we can improve the expectation of the complete-data log-likelihood, EM improves our model of the observed variable $x$. EM iteratively maximizes a surrogate function, the ELBO, that touches the log-likelihood at the current value, an instance of the minorization–maximization principle.

![EM for the mixing proportion alpha of a two-component normal mixture (100 simulated points). The solid curve is the observed log-likelihood; each dashed curve is the lower bound obtained from the E-step at the current value (dot), which touches the log-likelihood there; the M-step jumps to the maximizer of the bound (triangle), and the log-likelihood at the new value lies above the bound (arrow).](./plots/em-lower-bound.py)

Consequently the observed likelihood increases monotonically; if $\ell(\theta)$ is bounded above, the sequence $\ell(\hat\theta^{(t)})$ converges, and under mild regularity conditions $\hat\theta^{(t)}$ converges to a stationary point, possibly only a local maximum (or a saddle point). Compared with Newton's method, EM is more stable and more tolerant of the starting value: it does not break down through discontinuities or singular matrices, since it never needs the Hessian of $\ell$.

### 6.1.4. Examples

**Example 6.1.4 (Height Distributions)** Suppose the heights of males and females follow normal distributions, $x_m \sim \mathcal{N}(\mu_m, \sigma_m^2)$ and $x_f \sim \mathcal{N}(\mu_f, \sigma_f^2)$, with $\mu_m, \mu_f$ unknown and the $\sigma$'s known. If we select $n_m$ males and $n_f$ females at random and record their heights $\{x_{m,i}\}_{i=1}^{n_m}$ and $\{x_{f,i}\}_{i=1}^{n_f}$, the likelihood

$$
L(\mu_m, \mu_f) = (2\pi\sigma_m^2)^{-n_m/2}(2\pi\sigma_f^2)^{-n_f/2}\exp\left\{-\frac{\sum_i(x_{m,i} - \mu_m)^2}{2\sigma_m^2} - \frac{\sum_i(x_{f,i} - \mu_f)^2}{2\sigma_f^2}\right\}
$$
is maximized by solving $\nabla\ell(\mu_m, \mu_f) = \boldsymbol{0}$: $\hat\mu_m = \bar x_m$, $\hat\mu_f = \bar x_f$. Now suppose we have 100 records (50 males and 50 females) of heights, but without gender: the height $X$ is observed, the gender $Z$ is hidden, with prior $\mathbb{P}(Z = \mathrm{m}) = 0.5$. Initialize $\mu_m^{(0)}, \mu_f^{(0)}$ and let $\hat\theta^{(t)} = (\hat\mu_m^{(t)}, \hat\mu_f^{(t)})$. The E-step computes the posterior probabilities

$$
w_i^{(t)} = \mathbb{P}(Z_i = \mathrm{m} \mid x_i; \hat\theta^{(t)}) = \frac{\varphi_m(x_i)}{\varphi_m(x_i) + \varphi_f(x_i)}, \qquad \mathbb{P}(Z_i = \mathrm{f} \mid x_i; \hat\theta^{(t)}) = 1 - w_i^{(t)},
$$
where $\varphi_m, \varphi_f$ are the two normal densities at the current means (the equal priors cancel), and hence $Q(\theta \mid \hat\theta^{(t)})$; the M-step maximizes $Q$, which gives weighted means,

$$
\hat\mu_m^{(t+1)} = \frac{\sum_iw_i^{(t)}x_i}{\sum_iw_i^{(t)}}, \qquad \hat\mu_f^{(t+1)} = \frac{\sum_i(1 - w_i^{(t)})x_i}{\sum_i(1 - w_i^{(t)})}.
$$
This is a mixture of normal distributions with hidden indicator $Z_i = \boldsymbol{1}_{\{X_i \sim \mathcal{N}_k\}}$ of the component; its full treatment follows in Section 6.3.

**Example 6.1.5 (A Multinomial Distribution)** 197 animals are distributed multinomially into four categories with cell probabilities $\bigl(\frac12 + \frac\theta4, \frac{1 - \theta}{4}, \frac{1 - \theta}{4}, \frac\theta4\bigr)$ for some unknown $\theta \in [0, 1]$; the observed counts are $\boldsymbol{x} = (x_1, x_2, x_3, x_4) = (125, 18, 20, 34)$. Estimate $\theta$. The density of the observed data is that of a **multinomial distribution**,

$$
P_X(\boldsymbol{x} \mid \theta) = \frac{n!}{x_1!\,x_2!\,x_3!\,x_4!}\left(\frac12 + \frac\theta4\right)^{x_1}\left(\frac14 - \frac\theta4\right)^{x_2}\left(\frac14 - \frac\theta4\right)^{x_3}\left(\frac\theta4\right)^{x_4},
$$
with log-likelihood $\ell(\theta; \boldsymbol{x}) = c + x_1\log(2 + \theta) + (x_2 + x_3)\log(1 - \theta) + x_4\log\theta$. Split the first category into two cells with probabilities $\frac12$ and $\frac\theta4$, of which we only observe the sum $x_1 = x_{11} + x_{12}$. The complete data have density

$$
P_Y\bigl((x_{11}, x_{12}, x_2, x_3, x_4) \mid \theta\bigr) = \frac{n!}{x_{11}!\,x_{12}!\,x_2!\,x_3!\,x_4!}\left(\frac12\right)^{x_{11}}\left(\frac\theta4\right)^{x_{12}}\left(\frac{1 - \theta}{4}\right)^{x_2}\left(\frac{1 - \theta}{4}\right)^{x_3}\left(\frac\theta4\right)^{x_4},
$$
and log-likelihood $\ell_c(\theta) \propto (x_{12} + x_4)\log\theta + (x_2 + x_3)\log(1 - \theta)$, the log-likelihood of a binomial experiment. The latent variable is $Z = X_{12}$. Given the observed data, it is binomial,

$$
X_{12} \mid \boldsymbol{x} \sim \mathrm{Bin}\left(x_1, \frac{\theta/4}{1/2 + \theta/4}\right) = \mathrm{Bin}\left(x_1, \frac{\theta}{2 + \theta}\right).
$$
In the E-step we infer from $\boldsymbol{x}$ the distribution of the unobserved $x_{12}$ and take the expectation; since $\ell_c$ is linear in $x_{12}$, this replaces $x_{12}$ by its conditional mean:

$$
Q(\theta \mid \hat\theta^{(t)}) = \bigl(x_{12}^{(t)} + x_4\bigr)\log\theta + (x_2 + x_3)\log(1 - \theta), \qquad x_{12}^{(t)} = \frac{\hat\theta^{(t)}}{2 + \hat\theta^{(t)}}x_1.
$$
The M-step maximizes this with respect to $\theta$:

$$
\hat\theta^{(t+1)} = \arg\max_\theta Q(\theta \mid \hat\theta^{(t)}) = \frac{x_{12}^{(t)} + x_4}{x_{12}^{(t)} + x_2 + x_3 + x_4}.
$$

```r
emfun <- function(th0, maxit = 1000, releps = 1e-09) {
  i <- 0; th1 <- th0; th0 <- th1 + 1
  while ((i != maxit) & (abs(th1 - th0) > releps * abs(th0))) {
    i <- i + 1; th0 <- th1
    x12 <- (125 * th1) / (2 + th1)                  # E-step
    th1 <- (x12 + 34) / (x12 + 34 + 18 + 20)        # M-step
    print(c(tht = th0, thtplus = th1, iter = i))
  }
  return(list(nit = i, theta_hat = th1))
}
emfun(0.5)
```

```text
$nit
[1] 11

$theta_hat
[1] 0.6268215
```

(The trace printed at each iteration is omitted.) In all three examples the pattern is the same: the E-step fills in the missing data by posterior weights or conditional expectations, and the M-step computes the complete-data MLE.

![The genetic linkage multinomial. Left: the observed log-likelihood with the EM iterates from theta_0 = 0.05, which climb monotonically to the MLE 0.6268215. Right: the errors on a log scale decrease geometrically, with ratio 0.1328, the fraction of missing information at the MLE (Section 6.2.3).](./plots/multinomial-em-convergence.py)

Some questions and answers about the method:

- Can EM guarantee convergence to the global maximum? No, it may stop at a local maximum; in practice it is run from several starting values.
- When is EM most helpful? When the missing data can be defined as latent variables and the MLE for the complete data is easy to obtain. Hidden variables are introduced either to simplify the likelihood (the more common case, as in Example 6.1.5) or to account for actually missing data.
- When is EM not very helpful? When the E-step is slow, for example when the data dimension or the proportion of missing data is large; a large proportion of missing information also makes EM converge slowly.

## 6.2. Extensions of the EM Algorithm

### 6.2.1. Generalized EM

By the decomposition $\log p(x \mid \theta) = F(q, \theta) + \operatorname{KL}\bigl(q \Vert p(\cdot \mid x, \theta)\bigr)$, when $q(z) = p(z \mid x, \hat\theta^{(t)})$ is easy to get, EM computes and maximizes $F(q, \theta)$. EM is in fact coordinate ascent on $F$: it alternately maximizes over $q$ and over $\theta$.

**Definition 6.2.1 (Generalized EM)** The **generalized EM algorithm** (GEM) alternates

1. E-step: $\hat q^{(t+1)} = \arg\min_q\operatorname{KL}\bigl(q \Vert p(\cdot \mid x, \hat\theta^{(t)})\bigr) = \arg\max_qF(q, \hat\theta^{(t)})$;
2. M-step: choose $\hat\theta^{(t+1)}$ with $F(\hat q^{(t+1)}, \hat\theta^{(t+1)}) \ge F(\hat q^{(t+1)}, \hat\theta^{(t)})$, for example $\hat\theta^{(t+1)} = \arg\max_\theta F(\hat q^{(t+1)}, \theta) = \arg\max_\theta\int\hat q^{(t+1)}(z)\log p(x, z \mid \theta)\,\mathrm{d}z$.

The M-step thus need not maximize $Q$; it only has to increase it, $Q(\hat\theta^{(t+1)} \mid \hat\theta^{(t)}) \ge Q(\hat\theta^{(t)} \mid \hat\theta^{(t)})$, which is useful when $Q$ has no closed-form maximizer and the M-step itself needs a numerical optimizer (one Newton step, say). The proof of Theorem 6.1.1 goes through unchanged: $\ell(\hat\theta^{(t+1)}) \ge F(\hat q^{(t+1)}, \hat\theta^{(t+1)}) \ge F(\hat q^{(t+1)}, \hat\theta^{(t)}) = \ell(\hat\theta^{(t)})$.

**Remark 6.2.1** Suppose the maximizers are unique. Can the two steps be switched, $\hat\theta^{(t+1)} = \arg\max_\theta F(\hat q^{(t)}, \theta)$ followed by $\hat q^{(t+1)} = \arg\max_qF(q, \hat\theta^{(t+1)})$? Yes: alternating maximization produces the same sequence of pairs, and the switched order only starts the alternation from an initial $q$ instead of an initial $\theta$.

If $q$ is hard to obtain, or $F(q, \theta)$ is hard to compute, one turns to variational EM (below) or to Monte Carlo EM, which approximates the expectation in the E-step by an average over simulated values of $Z$.

### 6.2.2. Variational Inference

When the posterior $p(z \mid x, \theta)$ is intractable, we cannot make the KL term zero, but we can still maximize the ELBO over a restricted, tractable family of distributions $q$; the gap $\operatorname{KL}(q \Vert p)$ then measures the quality of the approximation.

**Definition 6.2.2 (Mean-Field Approximation)** The **mean-field approximation** enforces independence among all latent variables given $x$, approximating the posterior by a factorized distribution

$$
q(z) = \prod_iq_i(z_i).
$$

This assumption allows us to compute the update for each latent variable in isolation, and it has been successful in many problems. Fix $j$ and consider $F$ as a function of $q_j$. With $q$ factorized,

$$
F(q, \theta) = \int\prod_iq_i(z_i)\log p(x, z \mid \theta)\,\mathrm{d}z - \sum_i\int q_i(z_i)\log q_i(z_i)\,\mathrm{d}z_i.
$$
The first term is $\int q_j(z_j)\,\mathbb{E}_{-j}\bigl[\log p(x, z_{-j}, z_j \mid \theta)\bigr]\mathrm{d}z_j$, where $\mathbb{E}_{-j}$ is the expectation over $z_{-j} = (z_i)_{i\ne j}$ under $\prod_{i\ne j}q_i$. Denote

$$
q_j^*(z_j) = \frac1C\exp\Bigl\{\mathbb{E}_{-j}\bigl[\log p(x, z_{-j}, z_j \mid \theta)\bigr]\Bigr\}, \qquad C = \int\exp\Bigl\{\mathbb{E}_{-j}\bigl[\log p(x, z_{-j}, z_j \mid \theta)\bigr]\Bigr\}\mathrm{d}z_j.
$$
Then

$$
F(q, \theta) = -\operatorname{KL}(q_j \Vert q_j^*) + \sum_{i\ne j}H(q_i) + \log C,
$$
where $H(q_i) = -\int q_i\log q_i$ is the entropy and $C$ does not depend on $q_j$. Since the KL divergence is nonnegative, the ELBO is maximized over $q_j$ when $\operatorname{KL}(q_j \Vert q_j^*) = 0$, which happens when $q_j = q_j^*$.

**Definition 6.2.3 (Variational EM)** The **variational EM algorithm** (VBEM, variational Bayesian EM) replaces the exact E-step by the mean-field maximization of the ELBO:

1. E-step: evaluate $q_j^*(z_j) = \frac1C\exp\bigl\{\mathbb{E}_{-j}[\log p(x, z_{-j}, z_j \mid \theta)]\bigr\}$ for all $j$, and set $\hat q^{(t+1)}(z) = \prod_jq_j^*(z_j)$;
2. M-step: $\hat\theta^{(t+1)} = \arg\max_\theta F(\hat q^{(t+1)}, \theta)$.

In the fully Bayesian version, $\theta$ is itself treated as a latent variable with a **prior distribution** and receives its own factor of $q$. Because each $q_j^*$ depends on the other factors, the E-step is computed by coordinate ascent:

**Algorithm 6.2.1 (Coordinate Ascent Variational Inference)** Input: a model $p(x, z)$ and a data set $x$. Output: a mean-field variational density $q(z) = \prod_{j=1}^mq_j(z_j)$ and the ELBO $F(q, \theta)$.

1. Initialize $q_j(z_j)$, $j = 1, \dots, m$, for example by the corresponding marginals.
2. While the ELBO has not converged, i.e. while $\lvert F(q^{(k+1)}, \theta) - F(q^{(k)}, \theta)\rvert \ge \varepsilon$: for $j = 1, \dots, m$ set $q_j(z_j) = q_j^*(z_j) = \frac1C\exp\bigl\{\mathbb{E}_{-j}[\log p(x, z_{-j}, z_j \mid \theta)]\bigr\}$; then compute $q(z) = \prod_jq_j(z_j)$ and
   $$
   F(q, \theta) = \int q(z)\log\frac{p(x, z \mid \theta)}{q(z)}\,\mathrm{d}z = \mathbb{E}_q\bigl[\log p(x, z)\bigr] - \mathbb{E}_q\bigl[\log q(z)\bigr].
   $$
3. Return $q(z)$ and $F(q, \theta)$.

Since each update moves along a single coordinate (a single factor $q_j$), the ELBO climbs step by step in function space.

**Example 6.2.1 (Two Sources)** One-dimensional observations $x$ (say, the locations of incidents) come from two sources with known centers $\mu_1$ and $\mu_2$. For a particular observation $x$, which source produced it? The latent variable $z = (z_1, z_2)$ is a one-hot code: $z = (1, 0)$ for the first source and $(0, 1)$ for the second, and we want the approximate posterior $q(z_1, z_2)$. In the true posterior, $z_1$ and $z_2$ are mutually exclusive and highly dependent ($z_1 + z_2 = 1$), but the mean-field approximation assumes $q(z_1, z_2) = q_1(z_1)q_2(z_2)$, with $z_1, z_2 \in \{0, 1\}$. Suppose that, after simplification, the joint log-probability has the cross-term structure common in exponential families,

$$
\log p(x, z_1, z_2 \mid \theta) = 2.2z_1 + 2.2z_2 - 4.5z_1z_2 + \text{const}.
$$
Initialize $q_2 = \mathrm{Ber}(0.5)$, so $\mathbb{E}_2[z_2] = 0.5$.

- Update $q_1$: replace $z_2$ by its current expectation, $\mathbb{E}_{-1}[\log p] = 2.2z_1 + 2.2(0.5) - 4.5z_1(0.5) + \text{const} = -0.05z_1 + \text{const}$, so $q_1^*(z_1) \propto \exp\{-0.05z_1\}$: $q_1^*(0) \propto 1$, $q_1^*(1) \propto \mathrm{e}^{-0.05} \approx 0.9512$, $C = 1.9512$, and $q_1(1) = 0.9512/1.9512 \approx 0.4875$, $\mathbb{E}_1[z_1] \approx 0.4875$.
- Update $q_2$: $\mathbb{E}_{-2}[\log p] = (2.2 - 4.5\times0.4875)z_2 + \text{const} \approx 0.00625z_2 + \text{const}$, so $q_2^*(1) \propto \mathrm{e}^{0.00625} \approx 1.0063$, $C = 2.0063$, and $q_2(1) \approx 0.5016$.

After this first sweep, $q_1(1) = 0.4875$ and $q_2(1) = 0.5016$, and the four joint states have probabilities $q(0, 0) \approx 0.2554$, $q(1, 0) \approx 0.2430$, $q(0, 1) \approx 0.2571$ and $q(1, 1) \approx 0.2445$: starting from the balanced value $0.5$, the four states are still almost equally likely, though the exclusion term $-4.5z_1z_2$ has begun to push $q(1, 1)$ below $1/4$. The ELBO is the expected energy plus the entropy:

$$
\mathbb{E}_q[\log p] = 2.2q_1(1) + 2.2q_2(1) - 4.5q_1(1)q_2(1) = 1.0725 + 1.1035 - 1.1004 = 1.0756,
$$
$$
H(q_1) = -\bigl(0.4875\log0.4875 + 0.5125\log0.5125\bigr) \approx 0.6929, \qquad H(q_2) \approx 0.6931,
$$
so $F^{(1)} = 1.0756 + 1.3860 = 2.4616$ (up to the constant). The algorithm then returns to the head of the while loop with the updated $q_1, q_2$, computes $F^{(2)}$, and continues while $F^{(k+1)} - F^{(k)} \ge \varepsilon$. Continuing the sweeps, the factors move away from the symmetric start and converge to $q_1(1) \approx 0.220$, $q_2(1) \approx 0.770$, with $F \approx 2.482$. The probability of the impossible state falls to $q(1, 1) \approx 0.169$, but stays far above its exact posterior value $0.045$ (computed from the four unnormalized weights $\mathrm{e}^0, \mathrm{e}^{2.2}, \mathrm{e}^{2.2}, \mathrm{e}^{-0.1}$), and $F$ stays below $\log p(x) = \log(1 + 2\mathrm{e}^{2.2} + \mathrm{e}^{-0.1}) \approx 2.993$: a factorized $q$ cannot express "exactly one of $z_1, z_2$", and the KL gap measures the loss.

In summary: when the posterior $p$ cannot be computed exactly, we look for the closest approximating distribution $q$ (generalized EM); the optimization is over functions $q$, too large a space, so we introduce the mean-field assumption of independent factors (VBEM); and coordinate ascent updates the factors in turn until convergence.

**Example 6.2.2 (A Toy Example without Data)** Approximate a bivariate normal $p(z) = \mathcal{N}(z \mid \boldsymbol{\mu}, \Lambda^{-1})$ with mean $\boldsymbol{\mu} = (\mu_1, \mu_2)^{\mathsf T}$ and precision matrix $\Lambda = \begin{bmatrix}\Lambda_{11} & \Lambda_{12} \\ \Lambda_{21} & \Lambda_{22}\end{bmatrix}$ by $q(z) = q_1(z_1)q_2(z_2)$. Then

$$
\begin{aligned}
\log q_1^*(z_1) &= \mathbb{E}_{q_2(z_2)}\bigl[\log p(z)\bigr] + \text{const} = \mathbb{E}_{q_2(z_2)}\left[-\frac12(z_1 - \mu_1)^2\Lambda_{11} - (z_1 - \mu_1)\Lambda_{12}(z_2 - \mu_2)\right] + \text{const} \\
&= -\frac12z_1^2\Lambda_{11} + z_1\mu_1\Lambda_{11} - z_1\Lambda_{12}\bigl(\mathbb{E}[z_2] - \mu_2\bigr) + \text{const}.
\end{aligned}
$$
Completing the square, $q_1^*(z_1) = \mathcal{N}(z_1 \mid m_1, \Lambda_{11}^{-1})$ with $\mathbb{E}[z_1] \triangleq m_1 = \mu_1 - \Lambda_{11}^{-1}\Lambda_{12}(\mathbb{E}[z_2] - \mu_2)$, and by symmetry $q_2^*(z_2) = \mathcal{N}(z_2 \mid m_2, \Lambda_{22}^{-1})$ with $m_2 = \mu_2 - \Lambda_{22}^{-1}\Lambda_{21}(\mathbb{E}[z_1] - \mu_1)$. The two equations have the solution $\mathbb{E}[z_1] = \mu_1$, $\mathbb{E}[z_2] = \mu_2$, which gives the closed form

$$
q^*(z) = q_1^*(z_1)q_2^*(z_2) = \mathcal{N}(z_1 \mid \mu_1, \Lambda_{11}^{-1})\,\mathcal{N}(z_2 \mid \mu_2, \Lambda_{22}^{-1}).
$$
The means are exact, but the variances $\Lambda_{11}^{-1} \le (\Lambda^{-1})_{11}$ are too small whenever $z_1$ and $z_2$ are correlated: the mean-field approximation tends to underestimate posterior uncertainty.

### 6.2.3. Louis's Acceleration

EM can be viewed as a fixed-point iteration. Let $M(\theta)$ be the map representing a single joint E-step and M-step, so that $\theta_{n+1} = M(\theta_n)$. Under standard regularity conditions, the MLE $\theta^*$ is a fixed point of this map, $\theta^* = M(\theta^*)$. Near the optimum, a first-order Taylor expansion gives

$$
M(\theta_n) \approx M(\theta^*) + \nabla M(\theta^*)(\theta_n - \theta^*) \quad\Longrightarrow\quad \theta_{n+1} - \theta^* \approx J(\theta^*)(\theta_n - \theta^*),
$$
where $J(\theta) = \nabla M(\theta)$ is the Jacobian matrix of the EM map. It is expressed through three information matrices.

**Definition 6.2.4 (Complete, Observed and Missing Information)** For the model $p(x, z \mid \theta)$ with observed data $x$, define the observed information $I_X(\theta) = -\nabla^2\log p(x \mid \theta)$, the complete information $I_{Z,X}(\theta) = \mathbb{E}_{Z\mid x, \theta}\bigl[-\nabla^2\log p(x, Z \mid \theta)\bigr]$ and the missing information $I_{Z\mid X}(\theta) = \mathbb{E}_{Z\mid x, \theta}\bigl[-\nabla^2\log p(Z \mid x, \theta)\bigr]$. The **missing information principle** (Orchard and Woodbury, 1972; Louis, 1982) states that

$$
I_X(\theta) = I_{Z,X}(\theta) - I_{Z\mid X}(\theta):
$$
observed information equals complete information minus missing information.

It follows by differentiating $\log p(x \mid \theta) = \log p(x, z \mid \theta) - \log p(z \mid x, \theta)$ twice in $\theta$ and averaging over $Z \sim p(\cdot \mid x, \theta)$; the left side does not depend on $z$.

**Theorem 6.2.1 (Rate of Convergence of EM)** Let $\theta^*$ be a local maximum of $\ell$ with $I_X(\theta^*) \succ 0$, and suppose the M-step maximizer is interior and $Q$ is twice differentiable. Then

$$
J(\theta^*) = I_{Z,X}(\theta^*)^{-1}I_{Z\mid X}(\theta^*).
$$
Its eigenvalues lie in $[0, 1)$, so EM converges linearly near $\theta^*$, and the spectral radius $\rho\bigl(J(\theta^*)\bigr) = \max\lvert\lambda_{J(\theta^*)}\rvert$, the largest fraction of missing information, is the rate that controls how fast the error shrinks.

**Proof** (sketch) The M-step means $\nabla_\theta Q\bigl(M(\theta') \mid \theta'\bigr) = \boldsymbol{0}$ for all $\theta'$. Differentiating in $\theta'$ at $\theta' = \theta^* = M(\theta^*)$,

$$
\nabla^{2}_{\theta\theta}Q(\theta^* \mid \theta^*)\,\nabla M(\theta^*) + \nabla^{2}_{\theta\theta'}Q(\theta^* \mid \theta^*) = O.
$$
Here $\nabla^2_{\theta\theta}Q(\theta^* \mid \theta^*) = -I_{Z,X}(\theta^*)$ by definition. Writing $\log p(x, Z \mid \theta) = \log p(x \mid \theta) + \log p(Z \mid x, \theta)$, the mixed derivative is $\nabla_{\theta'}\mathbb{E}_{Z\mid x, \theta'}\bigl[\nabla_\theta\log p(Z \mid x, \theta)\bigr]$ at $\theta = \theta' = \theta^*$, which equals $\mathbb{E}\bigl[\nabla\log p(Z \mid x, \theta^*)\,\nabla\log p(Z \mid x, \theta^*)^{\mathsf T}\bigr] = I_{Z\mid X}(\theta^*)$ by the information identity for the conditional density. Hence $\nabla M(\theta^*) = I_{Z,X}^{-1}I_{Z\mid X}$. This matrix is similar to $I_{Z,X}^{-1/2}I_{Z\mid X}I_{Z,X}^{-1/2}$, whose eigenvalues lie in $[0, 1)$ because $O \preceq I_{Z\mid X}$ and $I_{Z,X} - I_{Z\mid X} = I_X \succ 0$. $\square$

Here $\theta$ is a column vector. With row vectors, as in Dempster, Laird and Rubin (1977), the Jacobian appears transposed, $I_{Z\mid X}I_{Z,X}^{-1}$, which has the same eigenvalues. In Example 6.1.5, $I_{Z,X}(\hat\theta) = 435.32$, $I_X(\hat\theta) = 377.52$ and $I_{Z\mid X}(\hat\theta) = 57.80$, so the rate is $57.80/435.32 = 0.1328$, exactly the slope seen in the figure there; the standard error of $\hat\theta$ is $I_X(\hat\theta)^{-1/2} = 0.0515$.

The geometric decay suggests extrapolation. Cascading the error recurrence $n$ times gives $\theta_{n+j} - \theta^* \approx J^n(\theta^*)(\theta_j - \theta^*)$, so, for a sufficiently large base iteration $j$, the steps also decay geometrically, $\theta_{n+j+1} - \theta_{n+j} \approx J^n(\theta^*)(\theta_{j+1} - \theta_j)$. Writing $\theta^*$ as a telescoping sum, we can extrapolate the final optimum without infinitely many iterations:

$$
\theta^* = \theta_j + \sum_{k=1}^\infty(\theta_{k+j} - \theta_{k+j-1}) \approx \theta_j + \sum_{k=0}^\infty J^k(\theta^*)(\theta_{j+1} - \theta_j) = \theta_j + \bigl[I - J(\theta^*)\bigr]^{-1}(\theta_{j+1} - \theta_j).
$$
The geometric series converges because the eigenvalues of $J$ are less than one in absolute value. By the missing information principle, $I - J(\theta) = I_{Z,X}(\theta)^{-1}\bigl(I_{Z,X}(\theta) - I_{Z\mid X}(\theta)\bigr) = I_{Z,X}(\theta)^{-1}I_X(\theta)$.

**Algorithm 6.2.2 (Louis's Acceleration)** Given the current estimate $\theta_n$:

1. compute $M(\theta_n)$ by one step of the standard EM algorithm;
2. compute $\bigl[I - J(\theta_n)\bigr]^{-1} = I_X(\theta_n)^{-1}I_{Z,X}(\theta_n)$;
3. set $\theta_{n+1} = \theta_n + \bigl[I - J(\theta_n)\bigr]^{-1}\bigl(M(\theta_n) - \theta_n\bigr)$.

The extra cost relative to a single EM iteration comes down to computing and inverting $I_X(\theta_n)$. Convergence is guaranteed only for $\theta$ in a neighborhood of the optimum $\theta^*$, whose size and nature are typically unknown in applications. With low missingness, $[I - J(\theta_n)]^{-1} \approx I$ and the sequence is similar to the usual EM sequence; with high missingness, $[I - J(\theta_n)]^{-1}$ is large, and the usual EM steps are modified substantially.

**Remark 6.2.2** Near $\theta^*$, the EM step is approximately a scaled gradient step: since $\nabla_\theta Q(\theta \mid \theta_n)$ at $\theta = \theta_n$ equals the observed score $\nabla\ell(\theta_n)$, one Newton step on $Q$ gives $M(\theta_n) - \theta_n \approx I_{Z,X}(\theta_n)^{-1}\nabla\ell(\theta_n)$. The accelerated step is therefore approximately $\theta_n + I_X(\theta_n)^{-1}\nabla\ell(\theta_n)$, Newton's method for $\ell$ ([3.5.5](/3.5.5)). Louis's acceleration trades the stability of EM for the speed of Newton's method, which explains both its fast local convergence and the need to start it near the optimum.

## 6.3. Application: Parameter Estimation in Mixture Models

### 6.3.1. Mixture Models

Mixture models are used widely: in machine learning, computer vision, natural language processing, mixed models in quantitative genetics, item response theory in psychometrics, medical image reconstruction and structural engineering. They serve to cluster data, to unravel superimposed signals (**Gaussian mixture models**, hidden Markov models), to estimate the parameters of compound distributions such as the compound Dirichlet, and to find the best mix of fixed models. Classification learns a rule from labeled data, while clustering looks for groups without labels ([3.4.11](/3.4.11)); EM for a Gaussian mixture is a soft version of **k-means clustering**.

The normal density with mean $\mu$ and variance $\sigma^2$ is $\varphi_{\mu,\sigma}(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\bigl\{-\frac{(x - \mu)^2}{2\sigma^2}\bigr\}$, and in dimension $d$, $\varphi_{\boldsymbol{\mu},\Sigma}(\boldsymbol{x}) = (2\pi)^{-d/2}\lvert\Sigma\rvert^{-1/2}\exp\bigl\{-\frac12(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\bigr\}$. Combining $m$ elementary densities models a complex data distribution.

**Definition 6.3.1 (Finite Mixture Model)** A **finite mixture model** with $m$ components has density

$$
p_\Theta(x) = \sum_{i=1}^m\alpha_i\varphi_{\theta_i}(x), \qquad \alpha_i \ge 0, \quad \sum_{i=1}^m\alpha_i = 1,
$$
with parameter $\Theta = (\alpha_1, \dots, \alpha_m, \theta_1, \dots, \theta_m)$, where the $\alpha_i$ are the mixing proportions and $\varphi_{\theta_i}$ the component densities. When every component is normal, $\theta_k = (\mu_k, \sigma_k)$ (or $(\boldsymbol{\mu}_k, \Sigma_k)$), it is a Gaussian mixture model.

To draw from a mixture, first draw the component label $z$ with $\mathbb{P}(z = k) = \alpha_k$, then draw $x$ from $\varphi_{\theta_z}$.

### 6.3.2. Maximum Likelihood for Gaussian Mixtures

The log-likelihood of $n$ observed data points $x_1, \dots, x_n$ is

$$
\ell(\Theta; \boldsymbol{x}) = \sum_{j=1}^n\log\sum_{i=1}^m\alpha_i\varphi_{\theta_i}(x_j),
$$
the logarithm of a sum, hard to optimize analytically. Instead introduce the $n$ hidden labels $z_1, \dots, z_n$: $z_i = k$ means that $x_i$ is generated by the $k$th Gaussian, $k \in \{1, \dots, m\}$, so that

$$
p_\Theta(x_i \mid z_i = k) = \varphi_{\theta_k}(x_i), \qquad p_\Theta(x_i, z_i = k) = \alpha_k\varphi_{\theta_k}(x_i).
$$

**Algorithm 6.3.1 (EM for Gaussian Mixtures)** Take initial guesses $\hat\Theta$ for the parameters and iterate until convergence:

1. E-step: compute the posterior distribution of $z_i$ given the observations,
   $$
   \Lambda_{i,k} = p_{\hat\Theta}(z_i = k \mid x_i) = \frac{\hat\alpha_k\varphi_{\hat\theta_k}(x_i)}{p_{\hat\Theta}(x_i)} = \frac{\hat\alpha_k\varphi_{\hat\theta_k}(x_i)}{\sum_{j=1}^m\hat\alpha_j\varphi_{\hat\theta_j}(x_i)},
   $$
   and hence $Q(\Theta \mid \hat\Theta) = \sum_{i=1}^n\sum_{k=1}^m\Lambda_{i,k}\log\bigl(\alpha_k\varphi_{\theta_k}(x_i)\bigr)$;
2. M-step: update $\alpha_k, \mu_k, \sigma_k$ for each Gaussian $k = 1, \dots, m$:
   $$
   \hat\alpha_k = \frac1n\sum_{i=1}^n\Lambda_{i,k}, \qquad \hat\mu_k = \frac{\sum_{i=1}^n\Lambda_{i,k}x_i}{\sum_{i=1}^n\Lambda_{i,k}}, \qquad \hat\sigma_k^2 = \frac{\sum_{i=1}^n\Lambda_{i,k}(x_i - \hat\mu_k)^2}{\sum_{i=1}^n\Lambda_{i,k}};
   $$
   for $d$-dimensional data with general covariances, $\hat\Sigma_k = \frac{\sum_i\Lambda_{i,k}(\boldsymbol{x}_i - \hat{\boldsymbol{\mu}}_k)(\boldsymbol{x}_i - \hat{\boldsymbol{\mu}}_k)^{\mathsf T}}{\sum_i\Lambda_{i,k}}$.

The posterior probabilities $\Lambda_{i,k}$ are often called the *responsibilities* of component $k$ for observation $i$. The M-step formulas are weighted versions of the complete-data MLE. For the proportions, maximize $\sum_k\bigl(\sum_i\Lambda_{i,k}\bigr)\log\alpha_k$ subject to $\sum_k\alpha_k = 1$: with a Lagrange multiplier, $\sum_i\Lambda_{i,k}/\alpha_k = \lambda$ for all $k$, and summing over $k$ gives $\lambda = n$. For $\mu_k$ and $\sigma_k^2$, the terms of $Q$ involving component $k$ are a normal log-likelihood with weights $\Lambda_{i,k}$, maximized by the weighted mean and variance. EM is soft clustering ($x_i$ belongs to every component with probability $\Lambda_{i,k}$), while k-means is hard clustering; EM with spherical components of common variance $\sigma^2 \to 0$ reduces to k-means.

If the number of Gaussians $m$ is not known, how can we estimate it? Picking the $m$ that makes $\ell(\Theta \mid x)$ as large as possible does not work: with $m = n$, each data point has its own source, which fits the data perfectly and may not work well for new data points. (In fact, with free variances the likelihood is unbounded already for $m \ge 2$: a component centered at one observation with $\sigma_k \to 0$ sends $\ell \to \infty$. The MLE of a Gaussian mixture is therefore understood as a well-behaved local maximum in the interior of the parameter space.) One can split the points into a training set $T$ and a validation set $V$, fit the parameters on $T$ for each $m$ and measure the likelihood on $V$, although this can still favor large $m$. Or one can use the **Bayesian information criterion** or the **Akaike information criterion** ([3.4.11](/3.4.11)), which pick the simplest of the models that fit: with $p$ free parameters, maximize $\ln L - \frac p2\ln n$ (that is, minimize $\mathrm{BIC} = -2\ln L + p\ln n$), or minimize $\mathrm{AIC} = 2p - 2\ln L$.

### 6.3.3. A Two-Component Normal Mixture

Generate data from a mixture of $\mathcal{N}(1, 2^2)$ with probability $\alpha = 0.4$ and $\mathcal{N}(4, 1)$ with probability $0.6$:

```r
mu1 <- 1
s1 <- 2
mu2 <- 4
s2 <- 1
a0 <- 0.4
n <- 100
set.seed(5288)
z <- rbinom(n, 1, a0)
x <- rnorm(n, mu1 * z + mu2 * (1 - z),
           s1 * z + (1 - z) * s2)
hist(x)
rug(x)
```

If $\mu_1, \sigma_1, \mu_2$ and $\sigma_2$ are known, the only parameter is $\alpha$, and we can visualize the observed-data log-likelihood as a function of $\alpha$ and maximize it directly; this oracle estimate is the gold standard for the comparison:

```r
f <- function(x, a) {
  a * dnorm(x, mu1, s1) + (1 - a) * dnorm(x, mu2, s2)
}
loglike <- Vectorize(
  function(a) {
    sum(log(f(x, a)))
  }
)
curve(loglike, 0.01, 0.95, n = 200, xlab = expression(alpha))
op <- optimize(loglike, c(0.01, 0.95), maximum = TRUE, tol = 1e-8)
op$maximum
```

```text
[1] 0.481365
```

Let $z_i \sim \mathrm{Ber}(\alpha)$: when $z_i = 1$, $x_i$ comes from population 1, and when $z_i = 0$, from population 2. The joint density of the observed and missing data, i.e. the complete-data density, is

$$
p_\Theta(x_i, z_i) = \bigl[\alpha\varphi_{\theta_1}(x_i)\bigr]^{z_i}\bigl[(1 - \alpha)\varphi_{\theta_2}(x_i)\bigr]^{1 - z_i},
$$
and summing out the missing data, $\sum_{z_i=0}^1p_\Theta(x_i, z_i) = \alpha\varphi_{\theta_1}(x_i) + (1 - \alpha)\varphi_{\theta_2}(x_i) = p_\Theta(x_i)$, gives the observed-data density. The usual EM step is $\hat\alpha = \frac1n\sum_i\Lambda_{i,1}$. For the accelerated version we need $I_X$, the negative second derivative of the observed log-likelihood $\sum_i\log p_\Theta(x_i)$, and $I_{Z,X}$, the negative second derivative of the expected complete-data log-likelihood $\sum_i\bigl[\Lambda_{i,1}\log\alpha + (1 - \Lambda_{i,1})\log(1 - \alpha)\bigr]$; the code computes both by symbolic differentiation with `deriv3`, and the accelerated update is $\theta^* = \theta_n + I_{Z,X}(\theta_n)I_X(\theta_n)^{-1}(\theta_{n+1} - \theta_n)$ (in one dimension the order of the factors does not matter).

```r
# usual EM
Lambda <- function(a, x, mu1, mu2, s1, s2) {
  a * dnorm(x, mu1, s1) / (a * dnorm(x, mu1, s1) +
                             (1 - a) * (dnorm(x, mu2, s2)))
}
M <- function(a0) {
  th.est <- Lambda(a0, x, mu1, mu2, s1, s2)
  mean(th.est)
}
# accelerated version
Mstar <- function(a0) {
  a1 <- M(a0)
  thhat <- Lambda(a0, x, mu1, mu2, s1, s2)
  a0 + (Ixz(a0) / Ix(a0)) * (a1 - a0)
}
Ix <- local({
  d <- deriv3(~ log(a * dnorm(x, mu1, s1) + (1 - a) * dnorm(x, mu2, s2)),
              "a", function.arg = TRUE)
  function(a) {
    H <- attr(d(a), "hessian")
    sum(H)   # sum over all data points
  }
})
Ixz <- local({
  d <- deriv3(~ thhat * log(a) + (1 - thhat) * log(1 - a),
              "a", function.arg = TRUE)
  function(a) {
    H <- attr(d(a), "hessian")
    sum(H)
  }
})
a0 <- 0.1
a0star <- 0.1
iter <- 6
EM <- numeric(iter)
Accel <- numeric(iter)
for (i in 1:iter) {
  thhat <- Lambda(a0, x, mu1, mu2, s1, s2)
  a1 <- M(a0)
  a1star <- Mstar(a0star)
  EM[i] <- a1
  Accel[i] <- a1star
  a0 <- a1
  a0star <- a1star
}
results <- data.frame(EM = EM, Accel = Accel,
                      errorEM = abs(EM - op$maximum),
                      errorAccel = abs(Accel - op$maximum))
format(results, scientific = FALSE)
```

```text
         EM     Accel     errorEM         errorAccel
1 0.3248608 0.3767740 0.156504282 0.1045910550708599
2 0.4204913 0.4733833 0.060873761 0.0079816884231566
3 0.4569536 0.4812987 0.024411415 0.0000662878894976
4 0.4714032 0.4813649 0.009961842 0.0000001006214514
5 0.4772680 0.4813650 0.004097023 0.0000000000426954
6 0.4796745 0.4813650 0.001690562 0.0000000001042916
```

The accelerated method's error decreases much faster than that of the standard method: it is close to the MLE $0.481365$ by the fourth iteration, whereas standard EM has not gotten there after six iterations; its error shrinks by a roughly constant factor of about $0.41$ per step. (The last digits of `errorAccel` reflect the tolerance `1e-8` of the reference value `op$maximum`.)

**Remark 6.3.1** In this code the function `Ixz` reads the variable `thhat` from the global environment, where the loop has stored the responsibilities at the standard EM iterate `a0`, not at `a0star`: R looks up free variables in the environment where a function was defined, so the local assignment of `thhat` inside `Mstar` is never seen. The accelerated sequence therefore uses the complete information evaluated at the wrong point; it still converges because both sequences approach the same MLE. A correct version evaluates the responsibilities at the accelerated iterate, for example by passing them as an argument, or by using the closed forms $I_X(\alpha) = \sum_i\frac{(\varphi_1(x_i) - \varphi_2(x_i))^2}{p_\Theta(x_i)^2}$ and $I_{Z,X}(\alpha) = \sum_i\bigl[\frac{\Lambda_{i,1}}{\alpha^2} + \frac{1 - \Lambda_{i,1}}{(1 - \alpha)^2}\bigr]$, as the R code under the following figure does.

![The two-component mixture, with data simulated from the same design by a different random number generator (so the estimate differs from the R output above). Left: histogram of the 100 points, the fitted mixture density and its two weighted components. Right: errors of standard EM and of Louis's acceleration from alpha_0 = 0.1 on a log scale; EM converges linearly, the accelerated iteration reaches the MLE to about 1e-10 in four steps.](./plots/mixture-em-louis.py)

## Summary

- EM computes the MLE when the observed likelihood is hard to optimize but becomes simple after introducing latent variables $Z$; observed data $X$, latent $Z$, complete data $Y = (X, Z)$.
- E-step: from $\hat\theta^{(t)}$ compute the posterior $p(Z \mid X, \hat\theta^{(t)})$ and $Q(\theta \mid \hat\theta^{(t)}) = \mathbb{E}_{Z\mid X, \hat\theta^{(t)}}\log p(X, Z \mid \theta)$. M-step: $\hat\theta^{(t+1)} = \arg\max_\theta Q(\theta \mid \hat\theta^{(t)})$. In the examples, the steps are: write the complete-data likelihood, identify the latent variable, compute its posterior, form $Q$, and derive the update (and iterate it by hand from a given start).
- Convergence: by Jensen's inequality, or by $\log p(x \mid \theta) = F(q, \theta) + \operatorname{KL}(q \Vert p) \ge F(q, \theta)$, the likelihood increases monotonically; EM converges to a stationary point, possibly a local maximum, and is usually more stable than Newton's method.
- Rate: EM is a fixed-point iteration converging linearly with rate equal to the largest fraction of missing information, $J = I_{Z,X}^{-1}I_{Z\mid X}$, from the missing information principle $I_X = I_{Z,X} - I_{Z\mid X}$.
- Extensions: GEM only requires the M-step to increase $Q$ (coordinate ascent on the ELBO); VBEM uses a mean-field factorization when the E-step is intractable; Louis's acceleration extrapolates with $(I - J)^{-1} = I_X^{-1}I_{Z,X}$ and is essentially a Newton step.
- Gaussian mixtures: the E-step computes the responsibilities $\Lambda_{ik}$, the M-step weighted proportions, means and variances; EM is soft clustering, k-means hard clustering; the number of components is chosen by validation or by BIC/AIC.
- Pros: easy to implement, small storage, low cost per iteration, monotone convergence for a bounded likelihood. Cons: linear (possibly slow) convergence, only local optima, and the E-step posterior or the exact M-step maximizer can be hard to find. The method was named and explained in the classic paper of Dempster, Laird and Rubin (1977).
