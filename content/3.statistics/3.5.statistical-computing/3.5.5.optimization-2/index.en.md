---
title: Optimization II
description: Newton's method and its quadratic convergence, the secant method, Fisher scoring and iteratively reweighted least squares, damped and quasi-Newton methods (Davidon, BFGS, DFP), trust regions, Gauss–Newton and Levenberg–Marquardt for nonlinear regression, gradient descent with line searches and stochastic gradients, and the conjugate direction and conjugate gradient methods.
---

[3.5.4](/3.5.4) set up the framework of numerical optimization: optimization versus root finding, the three elements of an iterative algorithm, the order of convergence, and methods that need no derivatives or only bracket a root. This chapter turns to methods that exploit derivatives. They fall into three families. Newton-type methods use second-order information and converge fast near the solution, but each step is expensive and they can fail far from it; gradient descent uses only first derivatives, so each step is cheap but convergence is slow; conjugate direction methods lie in between. Along the way the general methods meet statistics: Newton's method for the likelihood equation becomes Fisher scoring, which for **generalized linear models** ([3.3.6](/3.3.6)) is iteratively reweighted least squares, and the Gauss–Newton method is Fisher scoring for **nonlinear regression**. The linear algebra of [3.5.3](/3.5.3) (Cholesky factorization, Gram–Schmidt orthogonalization) is used throughout, and the EM algorithm of the next chapter ([3.5.6](/3.5.6)) is another ascent method for **maximum likelihood estimation**.

Two questions should be settled before choosing a method: are we seeking roots or extreme values, and are we maximizing or minimizing? Below $g$ denotes the objective function; when we look for a root of the derivative we write $f = g'$. For a function of a vector $\boldsymbol{x}$, $\nabla g$ is the gradient and $\nabla^2 g$ the **Hessian matrix** $\frac{\partial^2 g}{\partial\boldsymbol{x}\,\partial\boldsymbol{x}^{\mathsf T}}$.

## 5.1. Newton–Raphson and Related Methods

### 5.1.1. Newton's Method

The Babylonian method computes $\sqrt a$ by the iteration

$$
x_{n+1} = \frac12\left(x_n + \frac{a}{x_n}\right) = x_n - \frac{x_n^2 - a}{2x_n},
$$
which is exactly $x_{n+1} = x_n - f(x_n)/f'(x_n)$ for $f(x) = x^2 - a$: a special case of Newton's method. Historically, I. Newton (1669) used successive algebraic corrections for polynomials only; J. Raphson (1690) simplified them into an iteration; T. Simpson (1740) gave the modern formula and applied it to optimization.

Start with a univariate $g$ whose derivative $f = g'$ is continuously differentiable, and suppose $g''(x^*) \ne 0$ at the solution $x^*$. At iteration $t$, approximate $g'(x^*)$ by the linear Taylor expansion around $x^{(t)}$:

$$
0 = g'(x^*) \approx g'(x^{(t)}) + (x^* - x^{(t)})\,g''(x^{(t)}).
$$
Since $g'$ is approximated by its tangent line at $x^{(t)}$, it is natural to approximate the root of $g'$ by the root of the tangent line.

**Definition 5.1.1 (Newton's Method)** To solve $g'(x) = 0$, **Newton's method** (the Newton–Raphson method) starts from $x^{(0)}$ and iterates

$$
x^{(t+1)} = x^{(t)} - \frac{g'(x^{(t)})}{g''(x^{(t)})} = x^{(t)} + h^{(t)}. \tag{5.1}
$$
For $g\colon \mathbb{R}^p \to \mathbb{R}$ the update is $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \bigl[\nabla^2 g(\boldsymbol{x}^{(t)})\bigr]^{-1}\nabla g(\boldsymbol{x}^{(t)})$.

**Example 5.1.1** For $g(x) = \frac{\log x}{1 + x}$ the increment is

$$
h^{(t)} = \frac{(x^{(t)} + 1)\bigl(1 + 1/x^{(t)} - \log x^{(t)}\bigr)}{3 + 4/x^{(t)} + 1/(x^{(t)})^2 - 2\log x^{(t)}}.
$$
Starting from $x^{(0)} = 3$, Newton's method finds $x^{(4)} = 3.59112$ after four steps; by comparison, the bisection method does not determine the first five decimal places correctly until iteration 19.

**Theorem 5.1.1 (Quadratic Convergence of Newton's Method)** Let $f$ be twice continuously differentiable near a simple root $x^*$ ($f(x^*) = 0$, $f'(x^*) \ne 0$), and let $x^{(t+1)} = x^{(t)} - f(x^{(t)})/f'(x^{(t)})$. If $x^{(0)}$ is close enough to $x^*$, then $x^{(t)} \to x^*$, and the errors $\varepsilon^{(t)} = x^{(t)} - x^*$ satisfy

$$
\lim_{t\to\infty}\frac{\varepsilon^{(t+1)}}{(\varepsilon^{(t)})^2} = \frac{f''(x^*)}{2f'(x^*)} \triangleq c,
$$
so Newton's method has (at least) quadratic order of convergence, $\alpha = 2$.

**Proof** By **Taylor's formula** with the Lagrange remainder, for some $\xi_t$ between $x^{(t)}$ and $x^*$,

$$
0 = f(x^*) = f(x^{(t)}) + (x^* - x^{(t)})f'(x^{(t)}) + \frac{(x^* - x^{(t)})^2}{2}f''(\xi_t).
$$
Dividing by $f'(x^{(t)})$ gives $x^* - \bigl(x^{(t)} - f(x^{(t)})/f'(x^{(t)})\bigr) = -\frac{(\varepsilon^{(t)})^2}{2}\frac{f''(\xi_t)}{f'(x^{(t)})}$, that is,

$$
\varepsilon^{(t+1)} = \frac{f''(\xi_t)}{2f'(x^{(t)})}(\varepsilon^{(t)})^2.
$$
Choose $\delta > 0$ and $C$ with $\lvert f''(\xi)/(2f'(x))\rvert \le C$ for $\lvert x - x^*\rvert, \lvert\xi - x^*\rvert \le \delta$ and $C\delta < 1$. If $\lvert\varepsilon^{(0)}\rvert \le \delta$, then $\lvert\varepsilon^{(t+1)}\rvert \le C\delta\lvert\varepsilon^{(t)}\rvert$, so the errors stay in the interval and tend to zero; then $\xi_t \to x^*$ and the ratio tends to $c$. $\square$

The following R function uses a forward difference with step $h$ instead of the exact derivative $f'$ (strictly speaking, this is a discrete version of Newton's method, see Section 5.1.4.3):

```r
newton <- function(f, x0 = 1, N = 20, h = .01, tol = 1E-12, ...) {
  i <- 1; x1 <- x0
  p <- numeric(N)
  while (i <= N) {
    df.dx <- (f(x0 + h, ...) - f(x0, ...)) / h   # forward-difference derivative
    x1 <- (x0 - (f(x0, ...) / df.dx))
    p[i] <- x1
    i <- i + 1
    if (abs(x1 - x0) < tol) break
    x0 <- x1
  }
  return(list(root = p[i - 1], process = p[1:(i - 1)], nit = i - 1))
}
f <- function(x) (1 + 1/x - log(x)) / (1 + x)^2   # g'(x) for g(x) = log(x)/(1 + x)
newton(f, x0 = 1, N = 50)
```

```text
$root
[1] 3.591121

$process
 [1] 1.506261 2.107604 2.736086 3.258855 3.533365 3.589484
 [7] 3.591130 3.591121 3.591121 3.591121 3.591121 3.591121

$nit
[1] 12
```

For a multivariate $g$, the same Taylor argument gives the update of Definition 5.1.1. One never computes the inverse of the Hessian; each iteration solves a linear system.

**Algorithm 5.1.1 (Basic Newton)** Choose an initial guess $\boldsymbol{x}^{(0)}$ and a tolerance $\varepsilon$. For $t = 0, 1, \dots$: if $\lVert\nabla g(\boldsymbol{x}^{(t)})\rVert \le \varepsilon$, stop; otherwise solve $\nabla^2 g(\boldsymbol{x}^{(t)})\,\boldsymbol{h}^{(t)} = -\nabla g(\boldsymbol{x}^{(t)})$ and set $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} + \boldsymbol{h}^{(t)}$.

At a maximum the matrix $-\nabla^2 g$ is positive definite, and at a minimum $\nabla^2 g$ is; the system is then solved by the **Cholesky decomposition** $LL^{\mathsf T}$ of that matrix ([3.5.3](/3.5.3)), with about $p^3/3$ flops. Newton's method converges quadratically to a local maximum $\boldsymbol{x}^*$ if the Hessian is negative definite at $\boldsymbol{x}^*$ and the iteration starts close enough to the solution (and likewise to a local minimum with a positive definite Hessian).

**Example 5.1.2 (Himmelblau's Function)** The multimodal function

$$
g(x, y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
$$
is used to test optimization algorithms. It has one local maximum at $(-0.270845, -0.923039)$ and four local minima with value $0$: $(3, 2)$, $(-2.805118, 3.131312)$, $(-3.779310, -3.283186)$ and $(3.584428, -1.848126)$. Newton's method from $(-2, -2)$:

```r
g <- function(x) ((x[1]^2) + x[2] - 11)^2 + (x[1] + (x[2]^2) - 7)^2
g.prime <- function(x) {
  g.prime.da <- (4*x[1]^3) + (4*x[1]*x[2]) - (42*x[1]) + (2*x[2]^2) - 14
  g.prime.db <- (2*x[1]^2) - (26*x[2]) - 22 + (4*x[1]*x[2]) + (4*x[2]^3)
  matrix(c(g.prime.da, g.prime.db), ncol = 1)
}
g.2prime <- function(x) {
  g.2prime.da2 <- (12*x[1]^2) + (4*x[2]) - 42
  g.2prime.db2 <- (12*x[2]^2) + (4*x[1]) - 26
  g.2prime.dadb <- 4*(x[1] + x[2])
  matrix(c(g.2prime.da2, g.2prime.dadb,
           g.2prime.dadb, g.2prime.db2), nrow = 2, byrow = TRUE)
}
x <- c(-2, -2)
itr <- 40
x.values <- matrix(0, itr + 1, 2)
x.values[1, ] <- x
for (i in 1:itr) {
  x <- x - solve(g.2prime(x)) %*% g.prime(x)   # better: solve(g.2prime(x), g.prime(x))
  x.values[i + 1, ] <- x
}
x; g(x); g.prime(x)
```

The iteration ends at $\boldsymbol{x} = (3, 2)$ with $g(\boldsymbol{x}) = 0$ and $\nabla g(\boldsymbol{x}) = \boldsymbol{0}$. The path is drawn on a contour plot with `contour(x1, x2, z, nlevels = 20)` over a grid and `segments()` between successive rows of `x.values` (the grid vectors passed to `contour` must be increasing). Note that the Hessian at the starting point, $\begin{bmatrix} -2 & -16 \\ -16 & 14\end{bmatrix}$, is indefinite: Newton's method looks for a stationary point of any kind, and here it happens to reach a minimum.

### 5.1.2. The Secant Method

When the derivative of $f = g'$ is difficult to compute, the secant method of [3.5.4](/3.5.4) replaces $g''(x^{(t)})$ in Eq. (5.1) by the difference quotient $\frac{g'(x^{(t)}) - g'(x^{(t-1)})}{x^{(t)} - x^{(t-1)}}$:

$$
x^{(t+1)} = x^{(t)} - g'(x^{(t)})\,\frac{x^{(t)} - x^{(t-1)}}{g'(x^{(t)}) - g'(x^{(t-1)})}, \qquad t \ge 1.
$$
It requires two starting points $x^{(0)}, x^{(1)}$ and approximates $g'$ locally by the secant line through the last two iterates; the root of that line, $x^{(t+1)}$, is used with $x^{(t)}$ to produce the next approximation.

**Theorem 5.1.2 (Order of the Secant Method)** For a simple root $x^*$ of a smooth $f$, the secant iteration $x^{(t+1)} = x^{(t)} - f(x^{(t)})\frac{x^{(t)} - x^{(t-1)}}{f(x^{(t)}) - f(x^{(t-1)})}$ satisfies $\lvert\varepsilon^{(t+1)}\rvert \approx c\,\lvert\varepsilon^{(t)}\rvert^{\alpha}$ with $\alpha = \frac{1 + \sqrt5}{2} \approx 1.618$: the convergence is superlinear.

**Proof** (heuristic) Write $f(x^* + \varepsilon) \approx f'(x^*)\varepsilon + \frac{f''(x^*)}{2}\varepsilon^2 = f'(x^*)\varepsilon(1 + M\varepsilon)$ with $M = \frac{f''(x^*)}{2f'(x^*)}$. Then

$$
\varepsilon^{(t+1)} \approx \varepsilon^{(t)} - \frac{\varepsilon^{(t)}(1 + M\varepsilon^{(t)})(\varepsilon^{(t)} - \varepsilon^{(t-1)})}{\varepsilon^{(t)}(1 + M\varepsilon^{(t)}) - \varepsilon^{(t-1)}(1 + M\varepsilon^{(t-1)})} = \frac{M\varepsilon^{(t)}\varepsilon^{(t-1)}}{1 + M(\varepsilon^{(t)} + \varepsilon^{(t-1)})} \approx M\varepsilon^{(t)}\varepsilon^{(t-1)}.
$$
If $\lvert\varepsilon^{(t+1)}\rvert \approx c\lvert\varepsilon^{(t)}\rvert^\alpha$, then $\lvert\varepsilon^{(t-1)}\rvert \approx c_1\lvert\varepsilon^{(t)}\rvert^{1/\alpha}$, and comparing exponents in $c\lvert\varepsilon^{(t)}\rvert^\alpha \approx \lvert M\rvert c_1\lvert\varepsilon^{(t)}\rvert^{1 + 1/\alpha}$ gives $\alpha = 1 + 1/\alpha$, i.e. $\alpha^2 - \alpha - 1 = 0$. $\square$

The secant method needs only first derivatives, but numerically it is less stable than Newton's method: as $x^{(t)}$ and $x^{(t-1)}$ approach each other, the difference quotient subtracts nearly equal numbers and suffers from cancellation ([3.5.1](/3.5.1)).

### 5.1.3. Fisher Scoring

#### 5.1.3.1. General Form

The MLE $\hat\theta$ is a solution of the likelihood equation $l'(\theta) = 0$, where $l$ is the **log-likelihood function**. Newton's method for this equation is

$$
\theta^{(t+1)} = \theta^{(t)} - \frac{l'(\theta^{(t)})}{l''(\theta^{(t)})} = \theta^{(t)} + J(\theta^{(t)})^{-1}l'(\theta^{(t)}), \qquad J(\theta) \triangleq -l''(\theta).
$$
The quantity $J(\hat\theta) > 0$ determines the sharpness of the peak of the likelihood around its maximum. Under the usual regularity conditions the **Fisher information** ([3.2.3](/3.2.3)) satisfies $I(\theta) = \mathbb{E}[l'(\theta)^2] = \operatorname{Var}\bigl(l'(\theta)\bigr) = -\mathbb{E}[l''(\theta)] = \mathbb{E}[J(\theta)]$, so usually $I(\hat\theta) \approx J(\hat\theta)$.

**Definition 5.1.2 (Observed Information and Fisher Scoring)** For a log-likelihood $l(\boldsymbol{\theta})$, the matrix $J(\boldsymbol{\theta}) = -\nabla^2 l(\boldsymbol{\theta})$ is the **observed information**. **Fisher scoring** (the method of scoring) replaces it in Newton's method by the expected (Fisher) information $I(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\theta}}[J(\boldsymbol{\theta})]$ of the whole sample:

$$
\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} + I(\boldsymbol{\theta}^{(t)})^{-1}\nabla l(\boldsymbol{\theta}^{(t)}). \tag{5.2}
$$

The two methods are thus

$$
\text{Newton–Raphson: } \boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} + J(\boldsymbol{\theta}^{(t)})^{-1}\nabla l(\boldsymbol{\theta}^{(t)}), \qquad \text{Fisher scoring: } \boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} + I(\boldsymbol{\theta}^{(t)})^{-1}\nabla l(\boldsymbol{\theta}^{(t)}),
$$
where $\nabla l$ is the **score function** of the sample. Fisher scoring is also called iteratively reweighted least squares, for reasons explained in Section 5.1.3.3.

#### 5.1.3.2. Relation to Newton's Method

Recall the (scaled) **exponential family** ([3.2.2](/3.2.2))

$$
f(y \mid \theta) = \exp\left\{\frac{y\theta - b(\theta)}{a(\phi)} + c(y, \phi)\right\},
$$
where $\theta$ is the natural (canonical) parameter and $\phi$ the dispersion parameter. For one observation, $l(\theta) = \frac{y\theta - b(\theta)}{a(\phi)} + c(y, \phi)$ and $\frac{\partial l}{\partial\theta} = \frac{y - b'(\theta)}{a(\phi)}$. Since the score has mean zero, $\mathbb{E}(Y) = b'(\theta)$; since $\frac{\partial^2 l}{\partial\theta^2} = -\frac{b''(\theta)}{a(\phi)}$ and $\operatorname{Var}\bigl(\frac{\partial l}{\partial\theta}\bigr) = -\mathbb{E}\bigl(\frac{\partial^2 l}{\partial\theta^2}\bigr)$, also $\operatorname{Var}(Y) = b''(\theta)a(\phi)$. Moreover

$$
J(\theta) = -\frac{\partial^2 l}{\partial\theta^2} = \frac{b''(\theta)}{a(\phi)} = I(\theta) \triangleq I_1(\theta)
$$
does not depend on $y$, so it equals its expectation, the information in a single observation.

**Proposition 5.1.1** For an exponential family in its canonical parameter, the method of scoring and the method of Newton–Raphson coincide. With $n$ i.i.d. observations, $I(\theta) = nI_1(\theta)$ and

$$
\theta^{(t+1)} = \theta^{(t)} + \frac{I_1(\theta^{(t)})^{-1}l'(\theta^{(t)})}{n} = \theta^{(t)} + \frac{l'(\theta^{(t)})\,a(\phi)}{n\,b''(\theta^{(t)})}.
$$

The normal distribution with unknown mean, the Bernoulli, the Poisson and the gamma distributions are exponential families; the Cauchy and Student's $t$ distributions are not.

The identity of the two methods holds only for the canonical parameter. The Bernoulli density, for example, is $f(x \mid p) = p^x(1 - p)^{1 - x} = \exp\bigl\{x\log\frac{p}{1 - p} + \log(1 - p)\bigr\}$, with canonical parameter $\theta = \log\frac{p}{1 - p}$, whereas $\mu = p$ is the mean. Parametrize by the mean, $\theta = g(\mu)$. Then

$$
\frac{\partial l}{\partial\mu} = \frac{y - b'(g(\mu))}{a(\phi)}\,g'(\mu), \qquad J(\mu) = \frac{1}{a(\phi)}\Bigl[b''(g(\mu))\bigl(g'(\mu)\bigr)^2 + b'(g(\mu))g''(\mu) - y\,g''(\mu)\Bigr].
$$
The observed information depends on $y$, but because $\mathbb{E}(Y) = b'(\theta)$, the last two terms cancel in expectation, $\mathbb{E}\bigl[b'(g(\mu))g''(\mu) - Yg''(\mu)\bigr] = g''(\mu)\,\mathbb{E}\bigl[b'(g(\mu)) - Y\bigr] = 0$, and

$$
I(\mu) = \mathbb{E}[J(\mu)] = \frac{1}{a(\phi)}b''(g(\mu))\bigl(g'(\mu)\bigr)^2.
$$
This is why the method of scoring is usually simpler than Newton's method.

**Example 5.1.3 (Cauchy Location)** Let $x_1, \dots, x_{20}$ be an i.i.d. sample from the **Cauchy distribution** with density $f(x; \theta) = \frac{1}{\pi[1 + (x - \theta)^2]}$. Then

$$
l(\theta) = -\sum_{i=1}^{20}\log\bigl(1 + (x_i - \theta)^2\bigr) - n\log\pi, \qquad s(\theta) = \sum_{i=1}^{20}\frac{2(x_i - \theta)}{1 + (x_i - \theta)^2}, \qquad J(\theta) = 2\sum_{i=1}^{20}\frac{1 - (x_i - \theta)^2}{\bigl(1 + (x_i - \theta)^2\bigr)^2}.
$$
The expected information is

$$
I(\theta) = nI_1(\theta) = \frac{2n}{\pi}\int_{-\infty}^{+\infty}\frac{1 - (x - \theta)^2}{\bigl(1 + (x - \theta)^2\bigr)^3}\,\mathrm{d}x = \frac{n}{2}.
$$
Indeed, $\frac{1 - x^2}{(1 + x^2)^3} = \frac{2}{(1 + x^2)^3} - \frac{1}{(1 + x^2)^2}$, and the substitution $x = \tan u$ gives $\int_0^{+\infty}\frac{\mathrm{d}x}{(1 + x^2)^3} = \int_0^{\pi/2}\cos^4u\,\mathrm{d}u = \frac{3\pi}{16}$ and $\int_0^{+\infty}\frac{\mathrm{d}x}{(1 + x^2)^2} = \int_0^{\pi/2}\cos^2u\,\mathrm{d}u = \frac{\pi}{4}$, so the integral is $2\bigl(2\cdot\frac{3\pi}{16} - \frac{\pi}{4}\bigr) = \frac{\pi}{4}$. The two updates are

$$
\text{Newton–Raphson: } \theta^{(t+1)} = \theta^{(t)} + \frac{s(\theta^{(t)})}{J(\theta^{(t)})}, \qquad \text{Fisher scoring: } \theta^{(t+1)} = \theta^{(t)} + \frac{4}{n}\sum_{i=1}^{20}\frac{x_i - \theta^{(t)}}{1 + (x_i - \theta^{(t)})^2}.
$$

The function `mle` of the package stats4 takes as its first argument a function that evaluates the negative log-likelihood $-l(\theta)$, and minimizes it by a call to the general-purpose optimizer `optim`:

```r
x <- c(1.77, -0.23, 2.76, 3.80, 3.47, 56.75, -1.34, 4.24, -2.44, 3.29,
       3.71, -2.40, 4.53, -0.07, -1.05, -13.87, -2.53, -1.75, 0.27, 43.21)
mlogL <- function(theta) {
  # minus log-likelihood (up to a constant)
  sum(log(1 + (x - theta)^2))
}
library(stats4)
mle(mlogL, start = list(theta = 0))
```

```text
Coefficients:
     theta
-0.1922857
```

The log-likelihood of these data has a global maximum at $\hat\theta = -0.19229$, a local maximum at $2.8175$ and further stationary points near the outliers $43.21$ and $56.75$. Running both iterations from different starting values (30 iterations each) shows how much the starting value matters:

| $\theta^{(0)}$ | $-11$ | $-1$ | $0$ | $1.5$ | $4$ | $4.7$ | $7$ | $8$ | $38$ | $\bar x = 5.106$ |
|---|---|---|---|---|---|---|---|---|---|---|
| Newton–Raphson | diverges | $-0.1923$ | $-0.1923$ | $1.7136$ (min) | $2.8175$ | $-0.1923$ | $41.04$ (min) | diverges | $42.80$ | $54.88$ (min) |
| Fisher scoring | $-0.2833$ | $-0.1923$ | $-0.1923$ | $-0.1902$ | $2.8177$ | $2.8177$ | $2.8179$ | $2.8182$ | $36.35$ | $2.8177$ |

Newton's method converges quickly when it converges, but may go to a local minimum or diverge; Fisher scoring always moves uphill here, because $I(\theta) = n/2 > 0$, but it converges only linearly, and after 30 steps several runs are still a little away from the stationary point. The sample mean is a poor starting value for Cauchy data.

![Left: the Cauchy log-likelihood with the global maximum at -0.1923; Newton's method from 1.5 converges to the local minimum 1.71 and from 7 to the minimum near 41, while Fisher scoring from 7 climbs to the local maximum 2.82. Right: errors from the start -1 on a log scale; Newton's method converges quadratically in five steps, Fisher scoring linearly.](./plots/cauchy-newton-scoring.py)

#### 5.1.3.3. Iteratively Reweighted Least Squares

For a $p$-dimensional parameter the multivariate Taylor argument gives the Newton update $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - [\nabla^2 g(\boldsymbol{x}^{(t)})]^{-1}\nabla g(\boldsymbol{x}^{(t)})$ and Fisher scoring (5.2), with the **Fisher information matrix** $I(\boldsymbol{\theta})$. Before using them on regression models, we compare them.

- In many cases $I(\boldsymbol{\theta})$ is easier to calculate, and it is always positive (semi)definite. This generally stabilizes the algorithm: the scoring direction is an ascent direction.
- At convergence, $J(\boldsymbol{\theta}^{(t)}) \approx J(\hat{\boldsymbol{\theta}}) \approx I(\hat{\boldsymbol{\theta}})$ can be used to assess the uncertainty of $\hat{\boldsymbol{\theta}}$: since $\hat{\boldsymbol{\theta}} \overset{\cdot}{\sim} \mathcal{N}_d\bigl(\boldsymbol{\theta}, I(\boldsymbol{\theta})^{-1}\bigr)$ and $(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta})^{\mathsf T}I(\hat{\boldsymbol{\theta}})(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}) \overset{\cdot}{\sim} \chi^2_d$, we estimate $\operatorname{Cov}(\hat{\boldsymbol{\theta}}) \approx J(\boldsymbol{\theta}^{(t)})^{-1}$.
- For exponential family models the two are almost equivalent: if $(\theta_1, \dots, \theta_p)$ are natural parameters, then $J(\boldsymbol{\theta}) = I(\boldsymbol{\theta})$ and the methods coincide; otherwise scoring is simpler.
- Both share the same asymptotic properties, and either may be easier for a particular problem. Generally, Newton's method converges faster when both converge, while the radius of convergence of Fisher scoring is often larger; Fisher scoring makes rapid improvements initially, while Newton's method gives better refinements near the end.

Now consider **logistic regression**. With the linear predictor $\eta = \beta_0 + \beta_1x_1 + \cdots + \beta_{p-1}x_{p-1}$, instead of $Y \mid \boldsymbol{X} = \boldsymbol{x}_i \sim \mathcal{N}(\eta_i, \sigma^2)$ we assume $Y \mid \boldsymbol{X} = \boldsymbol{x}_i \sim \mathrm{Ber}(p_i)$. A **link function** $g$ maps the mean $\mu = \mathbb{E}(Y \mid \boldsymbol{X}) \in (0, 1)$ to $\eta \in \mathbb{R}$: $\eta = g(\mu)$, $\mu = g^{-1}(\eta)$; here

$$
g(p) = \operatorname{logit}(p) = \log\frac{p}{1 - p} = \eta, \qquad p = g^{-1}(\eta) = \frac{\mathrm{e}^\eta}{1 + \mathrm{e}^\eta}.
$$
In general a **generalized linear model** assumes $g\bigl(\mathbb{E}(Y_i \mid \boldsymbol{x}_i)\bigr) = \boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}$ for responses from an exponential family. For logistic regression, $Y_i \mid \boldsymbol{x}_i \sim \mathrm{Ber}(p_i)$ independently, and $f(y \mid p) = \exp\{y\log\frac{p}{1 - p} + \log(1 - p)\}$ has the **natural parameter** $\theta = \log\frac{p}{1 - p}$. With the logit link the natural parameter is linear in the covariates, $\theta_i = g(p_i) = \boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}$, and $b(\theta_i) = -\log(1 - p_i) = \log(1 + \mathrm{e}^{\theta_i})$, $b'(\theta) = \frac{\mathrm{e}^\theta}{1 + \mathrm{e}^\theta} = p$. With $\boldsymbol{y} = (y_1, \dots, y_n)^{\mathsf T}$, $\boldsymbol{p} = (p_1, \dots, p_n)^{\mathsf T}$ and the design matrix $X$,

$$
l(\boldsymbol{\beta}) = \sum_{i=1}^n\bigl[y_i\theta_i - b(\theta_i)\bigr] = \boldsymbol{y}^{\mathsf T}X\boldsymbol{\beta} - \boldsymbol{b}(X\boldsymbol{\beta})^{\mathsf T}\boldsymbol{1},
$$
$$
\nabla l(\boldsymbol{\beta}) = X^{\mathsf T}(\boldsymbol{y} - \boldsymbol{p}), \qquad \nabla^2 l(\boldsymbol{\beta}) = -\left(\frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}\boldsymbol{\theta}}\frac{\mathrm{d}\boldsymbol{\theta}}{\mathrm{d}\boldsymbol{\beta}}\right)^{\mathsf T}X = -X^{\mathsf T}WX,
$$
where $W = \frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}\boldsymbol{\theta}}$ is diagonal with entries $\frac{\mathrm{d}p_i}{\mathrm{d}\theta_i} = \frac{\mathrm{e}^{\theta_i}}{(1 + \mathrm{e}^{\theta_i})^2} = p_i(1 - p_i)$.

The Hessian does not depend on $\boldsymbol{y}$, so $-\nabla^2 l(\boldsymbol{\beta}) = X^{\mathsf T}WX = \mathbb{E}[-\nabla^2 l(\boldsymbol{\beta})] = I(\boldsymbol{\beta})$, and Fisher scoring is the same as Newton's method. For GLMs this is always true when the link function makes the natural parameter a linear function of the covariates (the canonical link, $\eta \equiv \theta$). The Newton update is

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \bigl(X^{\mathsf T}W^{(t)}X\bigr)^{-1}X^{\mathsf T}(\boldsymbol{y} - \boldsymbol{p}^{(t)}), \qquad W^{(t)} = \operatorname{diag}\bigl\{p_i^{(t)}(1 - p_i^{(t)})\bigr\},
$$
with $\boldsymbol{p}^{(t)} = \boldsymbol{p}(\boldsymbol{\beta}^{(t)})$. How can it be computed with any least squares software? Recall that **weighted least squares** for $W^{1/2}\boldsymbol{Y} = W^{1/2}X\boldsymbol{\beta} + W^{1/2}\boldsymbol{\varepsilon}$ gives $\hat{\boldsymbol{\beta}} = (X^{\mathsf T}WX)^{-1}X^{\mathsf T}W\boldsymbol{Y}$ ([3.3.12](/3.3.12)). Rewriting,

$$
\boldsymbol{\beta}^{(t+1)} = \bigl(X^{\mathsf T}W^{(t)}X\bigr)^{-1}\bigl(X^{\mathsf T}W^{(t)}X\boldsymbol{\beta}^{(t)} + X^{\mathsf T}(\boldsymbol{y} - \boldsymbol{p}^{(t)})\bigr) = \bigl(X^{\mathsf T}W^{(t)}X\bigr)^{-1}X^{\mathsf T}W^{(t)}\boldsymbol{z}^{(t)}, \tag{5.3}
$$
with the working (adjusted dependent) response $\boldsymbol{z}^{(t)} = X\boldsymbol{\beta}^{(t)} + (W^{(t)})^{-1}(\boldsymbol{y} - \boldsymbol{p}^{(t)})$. This response is a linearization of the link applied to the data: $z = g(y) \approx g(p) + (y - p)g'(p) = \theta + (y - p)\frac{\mathrm{d}\theta}{\mathrm{d}p}$, and for the logit link $\frac{\mathrm{d}\theta}{\mathrm{d}p} = \frac{1}{p(1 - p)}$.

**Algorithm 5.1.2 (Iteratively Reweighted Least Squares)** Iteratively reweighted least squares (IRLS) computes the MLE in a GLM by repeated weighted least squares. Set $\boldsymbol{\beta}^{(0)}$; for logistic regression ($\boldsymbol{\mu} = \boldsymbol{p}$) each iteration is:

1. fix $\boldsymbol{\beta}^{(t)}$ and compute $p_i^{(t)} = g^{-1}(\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}^{(t)})$;
2. compute the weights $W^{(t)} = \operatorname{diag}\{p_i^{(t)}(1 - p_i^{(t)})\}$;
3. compute the adjusted dependent responses $z_i^{(t)} = \boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}^{(t)} + (y_i - p_i^{(t)})/W^{(t)}_{ii}$;
4. regress $\boldsymbol{z}^{(t)}$ on $X$ with weights $W^{(t)}$ to obtain $\boldsymbol{\beta}^{(t+1)}$, in R `lm(z ~ X - 1, weights = w)`.

Repeat until convergence.

A common starting value is $\boldsymbol{\mu}^{(0)} = \boldsymbol{y}$, that is, $\boldsymbol{\beta}^{(0)}$ from the regression of $g(\boldsymbol{y})$ on $X$. This is not applicable to logistic regression, since $\operatorname{logit}(0)$ and $\operatorname{logit}(1)$ are infinite; there one starts from $\boldsymbol{\beta}^{(0)} = \boldsymbol{0}$ ($p_i = 1/2$), or, as `glm` does, from $\mu_i^{(0)} = (y_i + 1/2)/2$.

```r
irls_logit <- function(X, y, tol = 1e-10, maxit = 50) {
  beta <- rep(0, ncol(X))
  for (it in 1:maxit) {
    eta <- drop(X %*% beta)
    p <- 1 / (1 + exp(-eta))
    w <- p * (1 - p)                       # weights W
    z <- eta + (y - p) / w                 # working response
    beta_new <- coef(lm(z ~ X - 1, weights = w))
    if (max(abs(beta_new - beta)) < tol) break
    beta <- beta_new
  }
  list(coef = beta_new, iterations = it)
}
# agrees with glm(y ~ X - 1, family = binomial), which also uses IRLS
```

**Remark 5.1.1** The same derivation works for any exponential family response and any link: Fisher scoring for a GLM with mean $\mu_i = g^{-1}(\eta_i)$ and variance $\operatorname{Var}(Y_i) = a(\phi)V(\mu_i)$ is the weighted regression (5.3) with

$$
w_i = \frac{1}{V(\mu_i)\,g'(\mu_i)^2}, \qquad z_i = \eta_i + (y_i - \mu_i)\,g'(\mu_i);
$$
the dispersion $a(\phi)$ cancels. For Poisson regression with the log link, $w_i = \mu_i$ and $z_i = \eta_i + (y_i - \mu_i)/\mu_i$. For a canonical link, IRLS is also Newton's method; for other links it is Fisher scoring.

### 5.1.4. Variants of Newton's Method

#### 5.1.4.1. Drawbacks of Newton's Method

Speed is not the only factor to consider. Newton's method can diverge where a slow bracketing method such as bisection would succeed: an iterate may land where the tangent is nearly flat and be thrown far away, or the iterates may oscillate. Starting values are critical, as the Cauchy log-likelihood of Example 5.1.3 shows. The basic algorithm (solve $\nabla^2 g(\boldsymbol{x}^{(t)})\boldsymbol{h}^{(t)} = -\nabla g(\boldsymbol{x}^{(t)})$) has the following problems:

- it needs derivatives, which may be expensive or impossible to compute;
- it needs the solution of a linear system in each iteration, which is demanding for large problems;
- it converges only when started close enough to the solution;
- the Hessian $\nabla^2 g(\boldsymbol{x}^{(t)})$ may be singular, so that the linear system cannot be solved;
- it is not guaranteed to walk uphill (or downhill);
- the step length matters even when the step direction is good.

Note that if $A$ is a **positive definite matrix**, then $A^{-1}$ exists and is again positive definite (its eigenvalues are the reciprocals of those of $A$). This is used repeatedly below.

#### 5.1.4.2. Descent Directions and the Step Length

Consider minimization. Along a direction $\boldsymbol{d}$,

$$
g(\boldsymbol{x}^{(t)} + \alpha\boldsymbol{d}) = g(\boldsymbol{x}^{(t)}) + \alpha\boldsymbol{d}^{\mathsf T}\nabla g(\boldsymbol{x}^{(t)}) + \frac12\alpha^2\boldsymbol{d}^{\mathsf T}\nabla^2 g(\boldsymbol{x}^{(t)})\boldsymbol{d} + o(\alpha^2\lVert\boldsymbol{d}\rVert_2^2).
$$
The Newton step $\alpha^{(t)}\boldsymbol{d}^{(t)} = -[\nabla^2 g(\boldsymbol{x}^{(t)})]^{-1}\nabla g(\boldsymbol{x}^{(t)})$ is the exact minimizer of $g$ if $g$ is quadratic. Otherwise, inserting it into the quadratic part gives the predicted change

$$
\bigl(\alpha^{(t)}\boldsymbol{d}^{(t)}\bigr)^{\mathsf T}\nabla g + \frac12\bigl(\alpha^{(t)}\boldsymbol{d}^{(t)}\bigr)^{\mathsf T}\nabla^2 g\,\bigl(\alpha^{(t)}\boldsymbol{d}^{(t)}\bigr) = -\frac12\nabla g(\boldsymbol{x}^{(t)})^{\mathsf T}\bigl[\nabla^2 g(\boldsymbol{x}^{(t)})\bigr]^{-1}\nabla g(\boldsymbol{x}^{(t)}),
$$
which is an increase if the Hessian is negative definite and a decrease if it is positive definite.

**Definition 5.1.3 (Descent Direction)** At a point $\boldsymbol{x} \in \mathbb{R}^n$, a direction $\boldsymbol{d} \in \mathbb{R}^n$ is called a **descent direction** if there exists $\bar\alpha > 0$ such that $g(\boldsymbol{x} + \alpha\boldsymbol{d}) < g(\boldsymbol{x})$ for all $\alpha \in (0, \bar\alpha)$.

**Proposition 5.1.2** At any point $\boldsymbol{x}$ where $\nabla g(\boldsymbol{x}) \ne \boldsymbol{0}$ and $\nabla^2 g(\boldsymbol{x}) \succ 0$, the Newton direction $-[\nabla^2 g(\boldsymbol{x})]^{-1}\nabla g(\boldsymbol{x})$ is a descent direction.

**Proof** Any $\boldsymbol{d}$ with $\boldsymbol{d}^{\mathsf T}\nabla g(\boldsymbol{x}) < 0$ is a descent direction, since $g(\boldsymbol{x} + \alpha\boldsymbol{d}) = g(\boldsymbol{x}) + \alpha\boldsymbol{d}^{\mathsf T}\nabla g(\boldsymbol{x}) + o(\alpha)$. For the Newton direction, $\boldsymbol{d}^{\mathsf T}\nabla g(\boldsymbol{x}) = -\nabla g(\boldsymbol{x})^{\mathsf T}[\nabla^2 g(\boldsymbol{x})]^{-1}\nabla g(\boldsymbol{x}) < 0$ because the inverse of a positive definite matrix is positive definite. $\square$

So Newton's method does not guarantee descent in every iteration, but for a strictly **convex function** the Newton direction is always a descent direction: if we make a small enough step, we do get the decrease. This suggests controlling the step length.

**Definition 5.1.4 (Damped Newton Method)** Newton's method combined with backtracking, the **damped Newton method**, iterates

$$
\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\bigl[\nabla^2 g(\boldsymbol{x}^{(t)})\bigr]^{-1}\nabla g(\boldsymbol{x}^{(t)}),
$$
where $\alpha^{(t)}$ is found by backtracking: attempt a step with $\alpha = 1$; if it goes uphill, reduce (for example halve) $\alpha$; continue halving until a sufficiently small step is found to be downhill.

When evaluating and using the Hessian is impractical or costly, we replace it by an approximation $M^{(t)} \approx \nabla^2 g(\boldsymbol{x}^{(t)})$, which gives the modified Newton method (method of deflected gradients)

$$
\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\bigl(M^{(t)}\bigr)^{-1}\nabla g(\boldsymbol{x}^{(t)}).
$$
By the proof of Proposition 5.1.2, any positive definite $M^{(t)}$ ensures descent for a sufficiently small $\alpha^{(t)}$. With $M^{(t)} = I$ this is gradient descent, $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\nabla g(\boldsymbol{x}^{(t)})$ (Section 5.2). A modified Newton method thus requires two choices at each step: the step length and the approximation of the Hessian.

#### 5.1.4.3. The Discrete Newton Method

The analogue of the one-dimensional secant method approximates the Hessian by differences of gradients:

$$
M_{ij}^{(t)} = \frac{g_i'\bigl(\boldsymbol{x}^{(t)} + h_{ij}^{(t)}\boldsymbol{e}_j\bigr) - g_i'(\boldsymbol{x}^{(t)})}{h_{ij}^{(t)}},
$$
where $g_i'(\boldsymbol{x}) = \partial g(\boldsymbol{x})/\partial x_i$ is the $i$th component of $\nabla g$, $\boldsymbol{e}_j$ is the $j$th standard basis vector of $\mathbb{R}^p$, and $h_{ij}^{(t)}$ are constants. Taking $h_{ij}^{(t)} = h$ for all $(i, j)$ and $t$ leads to linear convergence, while $h_{ij}^{(t)} = x_j^{(t)} - x_j^{(t-1)}$ for all $i$ gives superlinear convergence. If $M^{(t)}$ is not symmetric, use $\frac12\bigl(M^{(t)} + (M^{(t)})^{\mathsf T}\bigr)$. The method is computationally burdensome: each iteration needs $p$ extra gradient evaluations.

#### 5.1.4.4. Quasi-Newton Methods

**Definition 5.1.5 (Secant Condition and Quasi-Newton Methods)** Write $\boldsymbol{z}^{(t)} = \boldsymbol{x}^{(t+1)} - \boldsymbol{x}^{(t)}$ and $\boldsymbol{y}^{(t)} = \nabla g(\boldsymbol{x}^{(t+1)}) - \nabla g(\boldsymbol{x}^{(t)})$. A matrix $M^{(t+1)}$ satisfies the **secant condition** (quasi-Newton condition) if

$$
\nabla g(\boldsymbol{x}^{(t+1)}) - \nabla g(\boldsymbol{x}^{(t)}) = M^{(t+1)}\bigl(\boldsymbol{x}^{(t+1)} - \boldsymbol{x}^{(t)}\bigr), \quad\text{i.e.}\quad \boldsymbol{y}^{(t)} = M^{(t+1)}\boldsymbol{z}^{(t)}.
$$
Methods that generate $M^{(t+1)}$ from $M^{(t)}$ in a manner that requires few calculations, satisfies the secant condition, and learns about the curvature of $g$ in the direction of the most recent step are called **quasi-Newton methods**.

The iteration alternates two steps: use $M^{(t)}$ to update $\boldsymbol{x}^{(t)}$ to $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}(M^{(t)})^{-1}\nabla g(\boldsymbol{x}^{(t)})$, then learn the curvature and update $M^{(t)}$ to $M^{(t+1)}$, which is used in $\boldsymbol{x}^{(t+2)} = \boldsymbol{x}^{(t+1)} - \alpha^{(t+1)}(M^{(t+1)})^{-1}\nabla g(\boldsymbol{x}^{(t+1)})$.

The simplest choice is a rank-one correction, *Davidon's update* (the symmetric rank-one update):

$$
M^{(t+1)} = M^{(t)} + \frac{\boldsymbol{v}^{(t)}(\boldsymbol{v}^{(t)})^{\mathsf T}}{(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}, \qquad \boldsymbol{v}^{(t)} = \boldsymbol{y}^{(t)} - M^{(t)}\boldsymbol{z}^{(t)}.
$$
It satisfies the secant condition: $M^{(t+1)}\boldsymbol{z}^{(t)} = M^{(t)}\boldsymbol{z}^{(t)} + \boldsymbol{v}^{(t)} = \boldsymbol{y}^{(t)}$. Backtracking is normally used, and the denominator $(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}$ must be monitored: when it is close to zero the update is skipped. If $M^{(t)}$ is positive definite, $M^{(t+1)}$ is symmetric but not necessarily positive definite, since $(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}$ can be negative.

The most popular update is a rank-two correction $M^{(t+1)} = M^{(t)} + a\,\boldsymbol{v}\boldsymbol{v}^{\mathsf T} + b\,\boldsymbol{u}\boldsymbol{u}^{\mathsf T}$ that keeps $M^{(t+1)}$ close to $M^{(t)}$ while satisfying the secant condition and remaining positive definite. Choosing $\boldsymbol{u} = \boldsymbol{y}^{(t)}$ and $\boldsymbol{v} = M^{(t)}\boldsymbol{z}^{(t)}$, the secant condition $M^{(t)}\boldsymbol{z}^{(t)} + a\boldsymbol{v}(\boldsymbol{v}^{\mathsf T}\boldsymbol{z}^{(t)}) + b\,\boldsymbol{y}^{(t)}\bigl((\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}\bigr) = \boldsymbol{y}^{(t)}$ holds with $a = -1/\bigl((\boldsymbol{z}^{(t)})^{\mathsf T}M^{(t)}\boldsymbol{z}^{(t)}\bigr)$ and $b = 1/\bigl((\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}\bigr)$.

**Definition 5.1.6 (BFGS Update)** The **BFGS update** (Broyden, Fletcher, Goldfarb and Shanno, 1970) is

$$
M^{(t+1)} = M^{(t)} - \frac{M^{(t)}\boldsymbol{z}^{(t)}\bigl(M^{(t)}\boldsymbol{z}^{(t)}\bigr)^{\mathsf T}}{(\boldsymbol{z}^{(t)})^{\mathsf T}M^{(t)}\boldsymbol{z}^{(t)}} + \frac{\boldsymbol{y}^{(t)}(\boldsymbol{y}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}. \tag{5.4}
$$

**Theorem 5.1.3 (BFGS Preserves Positive Definiteness)** Let $M^{(t)}$ be positive definite. Then $M^{(t+1)}$ in Eq. (5.4) is positive definite if and only if the *curvature condition* $(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$ holds.

**Proof** Write $M = M^{(t)}$, $\boldsymbol{z} = \boldsymbol{z}^{(t)}$, $\boldsymbol{y} = \boldsymbol{y}^{(t)}$. The update satisfies the secant condition: $M^{(t+1)}\boldsymbol{z} = M\boldsymbol{z} - M\boldsymbol{z} + \boldsymbol{y} = \boldsymbol{y}$. Necessity: if $M^{(t+1)} \succ 0$, then $\boldsymbol{y}^{\mathsf T}\boldsymbol{z} = \boldsymbol{z}^{\mathsf T}M^{(t+1)}\boldsymbol{z} > 0$. Sufficiency: for $\boldsymbol{x} \ne \boldsymbol{0}$,

$$
\boldsymbol{x}^{\mathsf T}M^{(t+1)}\boldsymbol{x} = \left(\boldsymbol{x}^{\mathsf T}M\boldsymbol{x} - \frac{(\boldsymbol{x}^{\mathsf T}M\boldsymbol{z})^2}{\boldsymbol{z}^{\mathsf T}M\boldsymbol{z}}\right) + \frac{(\boldsymbol{x}^{\mathsf T}\boldsymbol{y})^2}{\boldsymbol{y}^{\mathsf T}\boldsymbol{z}}.
$$
By the Cauchy–Schwarz inequality for the inner product $\langle\boldsymbol{u}, \boldsymbol{v}\rangle_M = \boldsymbol{u}^{\mathsf T}M\boldsymbol{v}$, i.e. $(\boldsymbol{x}^{\mathsf T}M\boldsymbol{z})^2 = \bigl((M^{1/2}\boldsymbol{x})^{\mathsf T}M^{1/2}\boldsymbol{z}\bigr)^2 \le \lVert M^{1/2}\boldsymbol{x}\rVert_2^2\lVert M^{1/2}\boldsymbol{z}\rVert_2^2$, the first bracket is nonnegative, with equality only if $\boldsymbol{x} = c\boldsymbol{z}$; the second term is nonnegative, and for $\boldsymbol{x} = c\boldsymbol{z}$ it equals $c^2\boldsymbol{y}^{\mathsf T}\boldsymbol{z} > 0$. $\square$

The curvature condition is more reasonable to require than $(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$. When $g$ is convex, $(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} = \bigl(\nabla g(\boldsymbol{x}^{(t+1)}) - \nabla g(\boldsymbol{x}^{(t)})\bigr)^{\mathsf T}(\boldsymbol{x}^{(t+1)} - \boldsymbol{x}^{(t)}) \ge 0$, and it is approximately $(\boldsymbol{z}^{(t)})^{\mathsf T}\nabla^2 g\,\boldsymbol{z}^{(t)}$; by contrast $(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} = (\boldsymbol{z}^{(t)})^{\mathsf T}\bigl(M^{(t+1)} - M^{(t)}\bigr)\boldsymbol{z}^{(t)} \approx 0$ may have either sign. For strongly convex functions the curvature condition always holds.

**Definition 5.1.7 (Strongly Convex Function)** For $\alpha > 0$, a function $f$ is **strongly convex** with parameter $\alpha$ ($\alpha$-strongly convex) if $f(\boldsymbol{x}) - \frac{\alpha}{2}\lVert\boldsymbol{x}\rVert_2^2$ is convex on $\operatorname{dom}(f)$; for twice differentiable $f$ this is equivalent to $\nabla^2 f(\boldsymbol{x}) \succeq \alpha I$, i.e. $\nabla^2 f(\boldsymbol{x}) - \alpha I \succeq 0$, for all $\boldsymbol{x}$.

**Lemma 5.1.1** If $f$ is differentiable and $\alpha$-strongly convex, then for all $\boldsymbol{x}, \boldsymbol{y} \in \operatorname{dom}(f)$,

$$
f(\boldsymbol{y}) - f(\boldsymbol{x}) \ge \nabla f(\boldsymbol{x})^{\mathsf T}(\boldsymbol{y} - \boldsymbol{x}) + \frac{\alpha}{2}\lVert\boldsymbol{y} - \boldsymbol{x}\rVert_2^2.
$$
Adding this inequality to the one with $\boldsymbol{x}$ and $\boldsymbol{y}$ exchanged gives $\bigl(\nabla f(\boldsymbol{y}) - \nabla f(\boldsymbol{x})\bigr)^{\mathsf T}(\boldsymbol{y} - \boldsymbol{x}) \ge \alpha\lVert\boldsymbol{y} - \boldsymbol{x}\rVert_2^2 > 0$ for $\boldsymbol{y} \ne \boldsymbol{x}$, so $(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$ for every step. If $g$ is not strongly convex, the curvature condition has to be enforced explicitly, for example by skipping the update or by a line search that guarantees it.

**Example 5.1.4 (BFGS for Himmelblau's Function)** Minimize the function of Example 5.1.2 from $(-4, 0)$, starting with $M^{(0)} = I$ and backtracking by halving:

```r
x <- c(-4, 0)
M <- diag(x = 1, ncol = 2, nrow = 2)
itr <- 40
epsilon <- 1e-10
x.values <- matrix(0, itr + 1, 2)
x.values[1, ] <- x
alpha.default <- 1
alpha <- alpha.default
for (i in 1:itr) {
  hessian.inv <- solve(M)
  xt <- x - alpha * hessian.inv %*% g.prime(x)
  # reduce alpha until a correct step is reached
  while (g(xt) > g(x)) {
    alpha <- alpha / 2
    xt <- x - alpha * hessian.inv %*% g.prime(x)
  }
  x.values[i + 1, ] <- xt
  z <- xt - x
  y <- g.prime(xt) - g.prime(x)
  M.old <- M
  M <- M - ((M %*% z %*% t(M %*% z)) / ((t(z) %*% M %*% z)[1])) +
    ((y %*% t(y)) / ((t(z) %*% y)[1]))
  if (abs((t(y) %*% z)[1]) < epsilon) { M <- M.old }   # skip a degenerate update
  alpha <- alpha.default
  x <- xt
}
x; g(x); g.prime(x)
```

The result is again $\boldsymbol{x} = (3, 2)$ with $g(\boldsymbol{x}) = 0$ and $\nabla g(\boldsymbol{x}) = \boldsymbol{0}$. The `[1]` matters: `t(z) %*% M %*% z` is a $1\times1$ matrix, and dividing a $2\times2$ matrix by it stops with the error "non-conformable arrays". From $(-2, -2)$, basic Newton reaches the minimum $(3, 2)$ while BFGS reaches $(-3.779310, -3.283186)$: different methods started at the same point may find different local optima.

![Contours of Himmelblau's function (on a log scale) with its four local minima and the local maximum. Newton's method from (-2, -2) crosses the central hill and converges to (3, 2); BFGS with backtracking from (-2, -2) descends to (-3.779, -3.283), and from (-4, 0) to (3, 2).](./plots/himmelblau-newton-bfgs.py)

The R function `optim` minimizes by default. Consider

```r
f <- function(x) { -((x[1]^2) + x[2] - 11)^2 - (x[1] + (x[2]^2) - 7)^2 }
optim(c(0, 0), fn = f, method = "BFGS")
optim(c(0, 0), fn = f)   # default: Nelder-Mead
```

```text
$par                                $par
[1] -2.213808e+12 -2.645398e+14     [1] -0.2711202 -0.9233435
$value                              $value
[1] -4.897384e+57                   [1] -181.6165
$counts                             $counts
function gradient                   function gradient
       4        4                         53       NA
$convergence                        $convergence
[1] 0                               [1] 0
```

Minimizing $f = -g$ means maximizing Himmelblau's function $g$, which is unbounded above. BFGS (left) correctly follows $f$ down to $-\infty$, yet reports convergence code $0$; Nelder–Mead (right) stops at the only local maximum of $g$, $(-0.2711, -0.9233)$ with $g = 181.6165$. The lesson is not that one method "works" and the other does not, but that the problem has no global maximum, and that a convergence code of $0$ does not certify a solution. To maximize with `optim`, minimize $-g$ or use `control = list(fnscale = -1)`.

The quasi-Newton update above still solves a linear system with $M$ in every iteration (`solve(M)`), at a cost of $O(p^3)$; that is the line to improve. Since the BFGS update is $M^{(t+1)} = A - \frac{M^{(t)}\boldsymbol{z}^{(t)}(M^{(t)}\boldsymbol{z}^{(t)})^{\mathsf T}}{(\boldsymbol{z}^{(t)})^{\mathsf T}M^{(t)}\boldsymbol{z}^{(t)}}$ with $A = M^{(t)} + \frac{\boldsymbol{y}^{(t)}(\boldsymbol{y}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}$, applying the **Sherman–Morrison formula** $(A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T})^{-1} = A^{-1} - \frac{A^{-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1}}{1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}}$ twice gives the update of $H = M^{-1}$ directly:

$$
H^{(t+1)} = \left(I - \frac{\boldsymbol{z}^{(t)}(\boldsymbol{y}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}\right)H^{(t)}\left(I - \frac{\boldsymbol{y}^{(t)}(\boldsymbol{z}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}\right) + \frac{\boldsymbol{z}^{(t)}(\boldsymbol{z}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}},
$$
which costs only $O(p^2)$ per iteration; $(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$ for strictly convex $g$.

**Definition 5.1.8 (DFP Update)** The **DFP update** (Davidon–Fletcher–Powell, also called the variable metric method) corrects the inverse Hessian approximation by the sum of two symmetric rank-one matrices:

$$
H^{(t+1)} = H^{(t)} - \frac{H^{(t)}\boldsymbol{y}^{(t)}\bigl(H^{(t)}\boldsymbol{y}^{(t)}\bigr)^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}H^{(t)}\boldsymbol{y}^{(t)}} + \frac{\boldsymbol{z}^{(t)}(\boldsymbol{z}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}. \tag{5.5}
$$

DFP and BFGS are dual: Eq. (5.5) is Eq. (5.4) with $M \leftrightarrow H$ and $\boldsymbol{y} \leftrightarrow \boldsymbol{z}$. The secant condition $\boldsymbol{y}^{(t)} = M^{(t+1)}\boldsymbol{z}^{(t)}$ becomes $H^{(t+1)}\boldsymbol{y}^{(t)} = \boldsymbol{z}^{(t)}$, which (5.5) satisfies: $H^{(t+1)}\boldsymbol{y}^{(t)} = H^{(t)}\boldsymbol{y}^{(t)} - H^{(t)}\boldsymbol{y}^{(t)} + \boldsymbol{z}^{(t)}$. By the dual of Theorem 5.1.3, $H^{(t+1)}$ remains positive definite if $H^{(t)}$ is and $(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$. DFP was the first quasi-Newton method; in practice BFGS is preferred, being more robust with inexact line searches. Davidon's rank-one update is less popular than both, because it can lose positive definiteness and its denominator can vanish.

**Algorithm 5.1.3 (Quasi-Newton Method)** Initial step: select a positive definite matrix $H^{(0)}$ (for example $I$) and an initial estimate $\boldsymbol{x}^{(0)}$ of $\boldsymbol{x}^*$; set $t = 0$. Iterative step:

1. compute $\nabla g(\boldsymbol{x}^{(t)})$ and the direction $\boldsymbol{d}^{(t)} = -H^{(t)}\nabla g(\boldsymbol{x}^{(t)})$;
2. compute $\alpha^{(t)} = \arg\min_\alpha g(\boldsymbol{x}^{(t)} + \alpha\boldsymbol{d}^{(t)})$, or choose it by backtracking;
3. set $\boldsymbol{z}^{(t)} = \alpha^{(t)}\boldsymbol{d}^{(t)}$ and $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} + \boldsymbol{z}^{(t)}$.

Update step: compute $\nabla g(\boldsymbol{x}^{(t+1)})$ and $\boldsymbol{y}^{(t)} = \nabla g(\boldsymbol{x}^{(t+1)}) - \nabla g(\boldsymbol{x}^{(t)})$, and then $H^{(t+1)}$ by DFP or by the inverse BFGS formula. Replace $t$ by $t + 1$ and repeat until convergence.

### 5.1.5. Applications in Nonlinear Regression

#### 5.1.5.1. Trust Region Methods

Consider $\min_x (x^2 - 1)^2$. Since $g'(0) = 0$, a line search started at $0$ cannot progress, although $0$ is a local maximum. Approximate $g$ at $0$ by the quadratic $m(s) = g(0) + g'(0)s + g''(0)s^2/2 = 1 - 2s^2$; to justify the approximation, pick $\Delta > 0$ and require $\lvert s\rvert \le \Delta$. Either solution $s = \pm\Delta$ escapes the stationary point. That is the principle of trust regions.

Iterative optimization algorithms solve much easier subproblems. In line search methods the subproblems are easier because they are one-dimensional. In trust-region methods the subproblems are $n$-dimensional but based on a simpler objective, a linear or quadratic model, which is trusted in a simple region, a ball of specified radius in a specified norm. Conceptually, an $n$-dimensional unconstrained problem is replaced by a constrained one. The replacement pays off because the subproblem need not be solved to high accuracy (an approximate solution is enough), and because the model function belongs to a class for which highly effective specialized algorithms exist.

**Definition 5.1.9 (Trust-Region Method)** From $g(\boldsymbol{x}^{(k)} + \boldsymbol{s}) = g(\boldsymbol{x}^{(k)}) + \boldsymbol{s}^{\mathsf T}\nabla g(\boldsymbol{x}^{(k)}) + \frac12\boldsymbol{s}^{\mathsf T}H(\boldsymbol{x}^{(k)} + \tau\boldsymbol{s})\boldsymbol{s}$ for some $\tau \in [0, 1]$, build the quadratic model

$$
m^{(k)}(\boldsymbol{s}) = g(\boldsymbol{x}^{(k)}) + \boldsymbol{s}^{\mathsf T}\nabla g(\boldsymbol{x}^{(k)}) + \frac12\boldsymbol{s}^{\mathsf T}B^{(k)}\boldsymbol{s},
$$
with $m^{(k)}(\boldsymbol{s}) - g(\boldsymbol{x}^{(k)} + \boldsymbol{s}) = O(\lVert\boldsymbol{s}\rVert^2)$; $B^{(k)}$ can be the Hessian $H(\boldsymbol{x}^{(k)})$. A **trust-region method** chooses the step by solving the trust-region subproblem

$$
\min_{\boldsymbol{s}}\ m^{(k)}(\boldsymbol{s}) \quad\text{subject to}\quad \lVert\boldsymbol{s}\rVert \le \Delta^{(k)},
$$
accepts $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)}$ if the decrease promised by the model is inherited by $g(\boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)})$, and otherwise sets $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)}$ and improves the model or shrinks the region.

A line search method first picks a descent direction $\boldsymbol{d}^{(k)}$ and then a step size $\alpha^{(k)}$ to reduce $g(\boldsymbol{x}^{(k)} + \alpha\boldsymbol{d}^{(k)})$; a trust-region method first picks the size of the region and then the step $\boldsymbol{s}^{(k)}$, direction and length together. If $B^{(k)} \succ 0$ and the unconstrained minimizer $\boldsymbol{s}^* = -(B^{(k)})^{-1}\nabla g(\boldsymbol{x}^{(k)})$ satisfies $\lVert\boldsymbol{s}^*\rVert \le \Delta^{(k)}$, then $\boldsymbol{s}^{(k)} = \boldsymbol{s}^*$. Thus with $B^{(k)} = H(\boldsymbol{x}^{(k)})$ the trust-region step is the Newton step only when the Hessian is positive definite and the Newton step lies inside the region; otherwise the trust-region step lies on the boundary of the region, is shorter, and points in a different direction (between the Newton direction and $-\nabla g$). In particular, when the Hessian is indefinite the subproblem still has a solution, and the trust-region step can exploit directions of negative curvature, where Newton's method would head for a saddle point or a maximum.

**Algorithm 5.1.4 (Basic Trust Region)** Initialization: set $k = 0$ and $\Delta^{(0)} > 0$; choose the starting point $\boldsymbol{x}^{(0)}$ by an educated guess; fix $\eta_v \in (0, 1)$ (typically $0.9$), $\eta_s \in (0, \eta_v)$ (typically $0.1$), $\gamma_i \ge 1$ (typically $2$) and $\gamma_d \in (0, 1)$ (typically $0.5$). Until convergence repeat:

1. build a model $m^{(k)}(\boldsymbol{s})$ approximating $g(\boldsymbol{x}^{(k)} + \boldsymbol{s})$;
2. solve the trust-region subproblem approximately to find $\boldsymbol{s}^{(k)}$ with $m^{(k)}(\boldsymbol{s}^{(k)}) < g(\boldsymbol{x}^{(k)})$ and $\lVert\boldsymbol{s}^{(k)}\rVert \le \Delta^{(k)}$, and compute the quality of the reduction, the ratio of the actual to the predicted reduction,
   $$
   \rho^{(k)} = \frac{g(\boldsymbol{x}^{(k)}) - g(\boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)})}{m^{(k)}(\boldsymbol{0}) - m^{(k)}(\boldsymbol{s}^{(k)})};
   $$
3. if $\rho^{(k)} \ge \eta_v$ (very successful step), set $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)}$ and $\Delta^{(k+1)} = \gamma_i\Delta^{(k)}$; else if $\rho^{(k)} \ge \eta_s$ (successful step), set $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)}$ and $\Delta^{(k+1)} = \Delta^{(k)}$; else (unsuccessful step) set $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)}$ and $\Delta^{(k+1)} = \gamma_d\Delta^{(k)}$;
4. increase $k$ by $1$.

#### 5.1.5.2. Nonlinear Regression and the Gauss–Newton Method

Suppose we have observed the temperature in a town over several years. In view of seasonal effects and global warming we postulate the model $T(t) = a\sin(\omega t + \phi) + bt$ for the temperature on day $t$, and we must find the parameters $a, \omega, \phi, b$ that best fit the data $(t_i, T_i)$, $i = 1, \dots, n$, to predict future temperatures:

$$
\min_{a, \omega, \phi, b}\ \sum_{i=1}^n\bigl(T_i - a\sin(\omega t_i + \phi) - bt_i\bigr)^2.
$$
In general, nonlinear regression ([3.3.6](/3.3.6)) considers data $(\boldsymbol{x}_i, y_i)$ and a curve $y = f(\boldsymbol{x}; \boldsymbol{\beta})$ with unknown $\boldsymbol{\beta} \in \mathbb{R}^p$,

$$
y_i = f(\boldsymbol{x}_i; \boldsymbol{\beta}) + \varepsilon_i, \qquad r_i(\boldsymbol{\beta}) = y_i - f(\boldsymbol{x}_i; \boldsymbol{\beta}), \qquad S(\boldsymbol{\beta}) = \sum_{i=1}^n r_i(\boldsymbol{\beta})^2 = \lVert\boldsymbol{r}(\boldsymbol{\beta})\rVert^2,
$$
and chooses $\boldsymbol{\beta}$ to minimize $S$; when $\varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$, the MLE is the least squares estimate, $\hat{\boldsymbol{\beta}}_{\mathrm{MLE}} = \hat{\boldsymbol{\beta}}_{\mathrm{OLS}} = \arg\min_{\boldsymbol{\beta}}S(\boldsymbol{\beta})$. The minimum usually occurs where the gradient vanishes, $\frac{\partial S}{\partial\beta_j} = 2\sum_i r_i\frac{\partial r_i}{\partial\beta_j} = 0$, $j = 1, \dots, p$, but these equations typically have no closed-form solution, and we turn to Newton's method, the Nelder–Mead method, and so on.

In this subsection $J = J(\boldsymbol{\beta})$ denotes the $n\times p$ Jacobian matrix of $\boldsymbol{f}(\boldsymbol{\beta}) = \bigl(f(\boldsymbol{x}_1; \boldsymbol{\beta}), \dots, f(\boldsymbol{x}_n; \boldsymbol{\beta})\bigr)^{\mathsf T}$, with entries $\partial f(\boldsymbol{x}_i; \boldsymbol{\beta})/\partial\beta_j$, so that $\nabla\boldsymbol{r} = -J$. Then

$$
\nabla S(\boldsymbol{\beta}) = -2J(\boldsymbol{\beta})^{\mathsf T}\boldsymbol{r}(\boldsymbol{\beta}), \qquad \nabla^2 S(\boldsymbol{\beta}) = 2J(\boldsymbol{\beta})^{\mathsf T}J(\boldsymbol{\beta}) - 2\sum_{i=1}^n r_i(\boldsymbol{\beta})\nabla^2 f(\boldsymbol{x}_i; \boldsymbol{\beta}),
$$
and Newton's method reads

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \Bigl[J^{\mathsf T}J - \sum_{i=1}^n r_i\nabla^2 f(\boldsymbol{x}_i; \boldsymbol{\beta}^{(t)})\Bigr]^{-1}J^{\mathsf T}\boldsymbol{r}(\boldsymbol{\beta}^{(t)}).
$$
For Fisher scoring with Gaussian errors, write $\tau = \sigma^{-2}$; omitting constants, $l(\boldsymbol{\beta}, \tau) = \frac n2\log\tau - \frac\tau2 S(\boldsymbol{\beta})$, so

$$
\nabla l(\boldsymbol{\beta}, \tau) = \begin{bmatrix}\tau J^{\mathsf T}\boldsymbol{r} \\ \frac{n}{2\tau} - \frac12S(\boldsymbol{\beta})\end{bmatrix}, \qquad \nabla^2 l(\boldsymbol{\beta}, \tau) = \begin{bmatrix}\tau\sum_i r_i\nabla^2 f_i - \tau J^{\mathsf T}J & J^{\mathsf T}\boldsymbol{r} \\ \boldsymbol{r}^{\mathsf T}J & -\frac n2\tau^{-2}\end{bmatrix},
$$
where $f_i = f(\boldsymbol{x}_i; \boldsymbol{\beta})$. Since $\mathbb{E}[\boldsymbol{r}(\boldsymbol{\beta})] = \boldsymbol{0}$, the information matrix of $\boldsymbol{y}$ is

$$
I_n(\boldsymbol{\beta}, \tau) = \mathbb{E}[-\nabla^2 l(\boldsymbol{\beta}, \tau)] = \begin{bmatrix}\tau J^{\mathsf T}J & \boldsymbol{0} \\ \boldsymbol{0}^{\mathsf T} & \frac n2\tau^{-2}\end{bmatrix},
$$
and the scoring update for $\boldsymbol{\beta}$ is $\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + (J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r}$, evaluated at $\boldsymbol{\beta}^{(t)}$ (the factor $\tau$ cancels). If the steps are too large, one uses backtracking, $\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \alpha^{(t)}(J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r}$.

The same update arises without any distributional assumption. Newton's method approximates $S(\boldsymbol{\beta})$ by a Taylor series; the Gauss–Newton method focuses on $f$ and linearizes it directly:

$$
y_i \approx f(\boldsymbol{x}_i; \boldsymbol{\beta}^{(t)}) + \nabla f(\boldsymbol{x}_i; \boldsymbol{\beta}^{(t)})^{\mathsf T}(\boldsymbol{\beta} - \boldsymbol{\beta}^{(t)}) + \varepsilon_i, \quad\text{i.e.}\quad \boldsymbol{r}^{(t)} \approx J^{(t)}(\boldsymbol{\beta} - \boldsymbol{\beta}^{(t)}) + \boldsymbol{\varepsilon},
$$
with $\boldsymbol{r}^{(t)} = \boldsymbol{r}(\boldsymbol{\beta}^{(t)})$ and $J^{(t)} = J(\boldsymbol{\beta}^{(t)})$, whose rows are $\nabla f(\boldsymbol{x}_i; \boldsymbol{\beta}^{(t)})^{\mathsf T}$. This is a linear regression of the residuals on the Jacobian.

**Definition 5.1.10 (Gauss–Newton Method)** For the nonlinear least squares problem $\min_{\boldsymbol{\beta}}\lVert\boldsymbol{y} - \boldsymbol{f}(\boldsymbol{\beta})\rVert^2$, the **Gauss–Newton method** iterates

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \bigl[(J^{(t)})^{\mathsf T}J^{(t)}\bigr]^{-1}(J^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)}, \tag{5.6}
$$
that is, the new guess is $\boldsymbol{\beta}^{(t)}$ plus the least squares coefficients of the regression of $\boldsymbol{r}^{(t)}$ on $J^{(t)}$ without intercept, $\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \texttt{lm}(\boldsymbol{r}^{(t)} \sim J^{(t)} - 1)$.

The Gauss–Newton method can thus be seen in three ways: as Newton's method with the awkward second-order term $\sum_i r_i\nabla^2 f_i$ dropped from the Hessian; as Fisher scoring, which obtains the same formula from $\mathbb{E}[\boldsymbol{r}(\boldsymbol{\beta})] = \boldsymbol{0}$ under the normality assumption; and as successively minimizing linear least squares models $\min_{\boldsymbol{\beta}}\lVert\boldsymbol{r}(\boldsymbol{\beta}^{(t)}) - J(\boldsymbol{\beta}^{(t)})(\boldsymbol{\beta} - \boldsymbol{\beta}^{(t)})\rVert^2$ of the nonlinear least squares problem. It requires no Hessian and works best when $f$ is not severely nonlinear.

**Proposition 5.1.3** If $J(\boldsymbol{\beta}^{(t)})$ has full column rank, the Gauss–Newton step is a descent direction for $S$ at every non-stationary point.

**Proof** With $\boldsymbol{d} = (J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r}$, which exists because $J^{\mathsf T}J \succ 0$,

$$
\boldsymbol{d}^{\mathsf T}\nabla S(\boldsymbol{\beta}^{(t)}) = -2\bigl[(J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r}\bigr]^{\mathsf T}J^{\mathsf T}\boldsymbol{r} = -2\boldsymbol{r}^{\mathsf T}J(J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r} = -2\boldsymbol{r}^{\mathsf T}P_J\boldsymbol{r},
$$
where $P_J$ is the **orthogonal projection matrix** onto the column space of $J$. Since $\boldsymbol{r}^{\mathsf T}P_J\boldsymbol{r} = \lVert P_J\boldsymbol{r}\rVert^2 \ge 0$, with equality iff $J^{\mathsf T}\boldsymbol{r} = \boldsymbol{0}$, i.e. iff $\nabla S = \boldsymbol{0}$, the directional derivative is negative at every non-stationary point. $\square$

Compared with the alternatives:

| | Newton's method | Gauss–Newton |
|---|---|---|
| Derivatives | requires second derivatives of $f$, i.e. $\nabla^2 S$ | first derivatives only |
| Direction | not always a descent direction ($\nabla^2 S$ need not be positive definite) | a descent direction if $J$ has full column rank |
| Speed | fast (quadratic) near a local minimum | similar to Newton if $\sum_i r_i(\boldsymbol{\beta}^*)\nabla^2 f_i(\boldsymbol{\beta}^*)$ is small, i.e. if $f$ is nearly linear around $\boldsymbol{\beta}^*$ or the residuals are small |

Unlike Fisher scoring, Gauss–Newton requires no normality assumption for the errors.

**Theorem 5.1.4 (Local Convergence of Gauss–Newton)** Let $M$ be a local Lipschitz constant of $J$ near a minimizer $\boldsymbol{\beta}^*$ at which $J(\boldsymbol{\beta}^*)$ has full column rank, with smallest singular value $\sigma_{\min}$, and let $\boldsymbol{\varepsilon}^{(t)} = \boldsymbol{\beta}^{(t)} - \boldsymbol{\beta}^*$. Then, for $\boldsymbol{\beta}^{(t)}$ close to $\boldsymbol{\beta}^*$, approximately

$$
\lVert\boldsymbol{\varepsilon}^{(t+1)}\rVert \lesssim \frac{M\lVert\boldsymbol{r}(\boldsymbol{\beta}^*)\rVert}{\sigma_{\min}^2}\lVert\boldsymbol{\varepsilon}^{(t)}\rVert + O(\lVert\boldsymbol{\varepsilon}^{(t)}\rVert^2).
$$

Hence the convergence is locally linear if $M\lVert\boldsymbol{r}(\boldsymbol{\beta}^*)\rVert < \sigma_{\min}^2$, and quadratic for zero-residual problems; there are no safeguards if $\lVert\boldsymbol{r}(\boldsymbol{\beta}^*)\rVert$ is large relative to the smallest singular values of $J(\boldsymbol{\beta}^*)$. Further problems may be encountered: $J^{\mathsf T}J$ is often ill-conditioned (its **condition number** is the square of that of $J$, so the step is better computed from a QR decomposition of $J$, [3.5.3](/3.5.3)), and far from $\boldsymbol{\beta}^*$ the iteration map may not be contractive.

**Example 5.1.5 (Fitting a Population Model)** Flour beetles in all stages of development were counted over 154 days with a carefully controlled food supply. An elementary model for population growth is **logistic growth**,

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\left(1 - \frac NK\right),
$$
where $N$ is the population size, $t$ time, $K$ the carrying capacity of the environment and $r$ the maximum possible growth rate (the net effect of reproduction and mortality). Separating variables, $r\,\mathrm{d}t = \frac{K\,\mathrm{d}N}{N(K - N)} = \bigl(\frac1N - \frac{1}{N - K}\bigr)\mathrm{d}N$, and the population size at time $t$ is

$$
N_t = f(t) = \frac{KN_0}{N_0 + (K - N_0)\exp(-rt)}, \qquad N_0 = f(0).
$$
If $N_0 < K$, then $N_t$ increases to $K$ and never exceeds it. With $N_0 = 2$ we estimate $r$ and $K$ by Gauss–Newton, with

$$
\frac{\partial N}{\partial r} = \frac{tKN_0(K - N_0)\exp(-rt)}{\bigl(N_0 + (K - N_0)\exp(-rt)\bigr)^2}, \qquad \frac{\partial N}{\partial K} = \frac{N_0^2\bigl(1 - \exp(-rt)\bigr)}{\bigl(N_0 + (K - N_0)\exp(-rt)\bigr)^2}.
$$
Given the current guesses of $r$ and $K$: (1) compute $\nabla f(t_i)$ to form $J$; (2) compute the residuals $x_i^{(k)} = N_{t_i} - f(t_i; r^{(k)}, K^{(k)})$ between the counts and the current predictions; (3) regress the residuals on $J$, which gives the updates of $r$ and $K$; (4) iterate until $\lVert\nabla S\rVert$, or $\lVert\boldsymbol{x}^{\mathsf T}J\rVert$, falls below a tolerance.

```r
t <- c(0, 8, 28, 41, 63, 79, 97, 117, 135, 154)
Nt <- c(2, 47, 192, 256, 768, 896, 1120, 896, 1184, 1024)
plot(t, Nt, type = 'p', pch = 20)
N0 <- Nt[1]
f <- function(t, r, K) K*N0/(N0 + (K - N0)*exp(-r*t))
dr <- function(t, r, K) {
  t*K*N0*(K - N0)*exp(-r*t)/(N0 + (K - N0)*exp(-r*t))^2
}
dK <- function(t, r, K) {
  (N0)^2*(1 - exp(-r*t))/(N0 + (K - N0)*exp(-r*t))^2
}
rt <- .1; Kt <- 1000          # f is increasing, so choose a large starting Kt
xt <- Nt - f(t, r = rt, K = Kt)                       # residuals
Jt <- cbind(mapply(dr, t = t, r = rt, K = Kt),
            mapply(dK, t = t, r = rt, K = Kt))        # Jacobian
grad <- sum((t(xt) %*% Jt)^2)
i <- 0
while (i <= 500 & grad > 1e-20) {   # stop on the gradient, not on sum(xt^2)
  lmod <- summary(lm(xt ~ Jt - 1))  # no intercept
  deltr <- lmod$coef[1]; deltK <- lmod$coef[2]
  rt <- rt + deltr; Kt <- Kt + deltK
  xt <- Nt - f(t, r = rt, K = Kt)
  Jt <- cbind(mapply(dr, t = t, r = rt, K = Kt),
              mapply(dK, t = t, r = rt, K = Kt))
  grad <- sum((t(xt) %*% Jt)^2)
  i <- i + 1
}
rt; Kt
```

```text
[1] 0.1179586
[1] 1033.515
```

The stopping rule uses the gradient $J^{\mathsf T}\boldsymbol{r}$ rather than the residual sum of squares, which does not tend to zero for a model that does not fit exactly. The residuals here are large, and the iteration converges linearly, as Theorem 5.1.4 predicts. R's `nls` uses the Gauss–Newton algorithm by default.

#### 5.1.5.3. The Levenberg–Marquardt–Fletcher Method

Similarly to **ridge regression** (Tikhonov regularization) for linear least squares, K. Levenberg (1944) proposed to modify the Gauss–Newton update.

**Definition 5.1.11 (Levenberg–Marquardt Method)** The **Levenberg–Marquardt method** (damped least squares) iterates

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \bigl[(J^{(t)})^{\mathsf T}J^{(t)} + \lambda^{(t)}I_p\bigr]^{-1}(J^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)}, \tag{5.7}
$$
where $\lambda^{(t)} > 0$ is a damping factor.

As $\lambda \to 0^+$ the step tends to the Gauss–Newton step, which converges quickly but may diverge; as $\lambda \to \infty$ it tends to $\lambda^{-1}J^{\mathsf T}\boldsymbol{r} = -\frac{1}{2\lambda}\nabla S$, a short gradient descent step, which converges slowly but is more stable. Because $\lambda I_p$ treats all parameters alike, the parameters (or predictors) should be standardized. Levenberg used a fixed $\lambda$. To control the trade-off between quick convergence and numerical stability, D. Marquardt (1963) let the damping factor vary between iterations: when convergence is stable, it is decreased, $\lambda^{(t+1)} \leftarrow \lambda^{(t)}/\nu$, to exploit the fast Gauss–Newton rate; when divergence is observed, it is increased, $\lambda^{(t+1)} \leftarrow \lambda^{(t)}\nu$, to restore stability.

The method is a trust-region method. The Gauss–Newton step minimizes the model $m^{(t)}(\boldsymbol{s}) = \boldsymbol{r}^{\mathsf T}\boldsymbol{r} - 2\boldsymbol{s}^{\mathsf T}J^{\mathsf T}\boldsymbol{r} + \boldsymbol{s}^{\mathsf T}J^{\mathsf T}J\boldsymbol{s}$ of $S(\boldsymbol{\beta}^{(t)} + \boldsymbol{s})$, all quantities evaluated at $\boldsymbol{\beta}^{(t)}$; the Marquardt step (5.7) minimizes $\boldsymbol{s}^{\mathsf T}(J^{\mathsf T}J + \lambda^{(t)}I_p)\boldsymbol{s} - 2\boldsymbol{s}^{\mathsf T}J^{\mathsf T}\boldsymbol{r} + \boldsymbol{r}^{\mathsf T}\boldsymbol{r}$, and it is also the solution of the Gauss–Newton model subject to a constraint $\lVert\Delta\boldsymbol{\beta}^{(t)}\rVert \le \Delta^{(t)}$, with $\lambda^{(t)}$ the Lagrange multiplier; adjusting $\lambda$ is adjusting the radius of the trust region.

If the damping factor is large, the curvature information in $J^{\mathsf T}J$ is hardly used. R. Fletcher (1971) proposed a further improvement,

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \bigl[J^{\mathsf T}J + \lambda\operatorname{diag}(J^{\mathsf T}J)\bigr]^{-1}J^{\mathsf T}\boldsymbol{r},
$$
where $\operatorname{diag}(J^{\mathsf T}J)$ is the diagonal matrix of the diagonal entries of $J^{\mathsf T}J$. Scaling each gradient component by the curvature encourages larger movement in the directions where the gradient is small; this can be viewed as a preconditioning step for ill-conditioned problems, and makes the method invariant to rescaling the parameters. The result is the Levenberg–Marquardt–Fletcher (LMF) algorithm.

## 5.2. Gradient Descent

### 5.2.1. General Form

For a univariate $f$, we reduce $f(x)$ by moving in the direction opposite to the sign of the derivative: for $f(x) = x^2/2$, $f'(x) > 0$ and $f$ increases for $x > 0$, while $f'(x) < 0$ and $f$ decreases for $x < 0$. We use $f'(x)$ to follow the function downhill. In several variables, for a step $\boldsymbol{h}^{(t)}$, $f(\boldsymbol{x}^{(t+1)}) - f(\boldsymbol{x}^{(t)}) \approx (\boldsymbol{h}^{(t)})^{\mathsf T}\nabla f(\boldsymbol{x}^{(t)})$: the **gradient** is the direction of steepest ascent, and the negative gradient at the current point is the direction of steepest descent. The function decreases fastest if one goes from $\boldsymbol{x}^{(t)}$ in the direction of $-\nabla f(\boldsymbol{x}^{(t)})$ (A. Cauchy, 1847).

**Definition 5.2.1 (Gradient Descent)** **Gradient descent** iterates

$$
\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\nabla f(\boldsymbol{x}^{(t)}), \tag{5.8}
$$
with step sizes $\alpha^{(t)} > 0$; for maximization, $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} + \alpha^{(t)}\nabla f(\boldsymbol{x}^{(t)})$ (gradient ascent).

At each iteration consider the expansion

$$
f(\boldsymbol{y}) \approx f(\boldsymbol{x}) + \nabla f(\boldsymbol{x})^{\mathsf T}(\boldsymbol{y} - \boldsymbol{x}) + \frac12(\boldsymbol{y} - \boldsymbol{x})^{\mathsf T}\nabla^2 f(\boldsymbol{x})(\boldsymbol{y} - \boldsymbol{x}) \approx f(\boldsymbol{x}) + \nabla f(\boldsymbol{x})^{\mathsf T}(\boldsymbol{y} - \boldsymbol{x}) + \frac{1}{2\alpha}\lVert\boldsymbol{y} - \boldsymbol{x}\rVert_2^2,
$$
a quadratic approximation that replaces the Hessian $\nabla^2 f(\boldsymbol{x})$ by $\frac1\alpha I$. Choosing the next point $\boldsymbol{y} = \boldsymbol{x}^+$ to minimize it, $\boldsymbol{y} - \boldsymbol{x} = -\alpha\nabla f(\boldsymbol{x})$, gives exactly $\boldsymbol{x}^+ = \boldsymbol{x} - \alpha\nabla f(\boldsymbol{x})$. This unifies the three methods: Newton–Raphson, Fisher scoring and gradient descent all step to the optimum of a local quadratic model of the objective, and they differ only in the curvature matrix of the model: the actual Hessian (observed information), its expectation (Fisher information), or a multiple of the identity.

**Algorithm 5.2.1 (Gradient Descent)** Choose an initial guess $\boldsymbol{x}^{(0)}$ and a tolerance $\varepsilon$. For $t = 0, 1, \dots$: set $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\nabla f(\boldsymbol{x}^{(t)})$; stop if $\lVert\boldsymbol{x}^{(t+1)} - \boldsymbol{x}^{(t)}\rVert \le \varepsilon$ or $\lVert\nabla f(\boldsymbol{x}^{(t)})\rVert \le \varepsilon$.

The step size rules are: a fixed step, $\alpha^{(t)}$ constant; backtracking line search; and exact line search, which minimizes $h(\alpha) \triangleq f\bigl(\boldsymbol{x}^{(t)} - \alpha\nabla f(\boldsymbol{x}^{(t)})\bigr)$ over $\alpha$.

### 5.2.2. Three Line Search Methods

#### 5.2.2.1. Exact Line Search

**Definition 5.2.2 (Exact Line Search)** A **line search** chooses the step size along a given direction; the **exact line search** takes $\alpha^{(t)} = \arg\min_{\alpha \ge 0}f\bigl(\boldsymbol{x}^{(t)} - \alpha\nabla f(\boldsymbol{x}^{(t)})\bigr)$.

Since $\alpha$ minimizes $f$ along the line, by the chain rule

$$
0 = \frac{\mathrm{d}}{\mathrm{d}\alpha}f(\boldsymbol{x}^{(t+1)}) = \nabla f(\boldsymbol{x}^{(t+1)})^{\mathsf T}\frac{\mathrm{d}}{\mathrm{d}\alpha}\boldsymbol{x}^{(t+1)} = -\nabla f(\boldsymbol{x}^{(t+1)})^{\mathsf T}\nabla f(\boldsymbol{x}^{(t)}):
$$
successive gradients are orthogonal, and the path zig-zags toward the minimum.

For the quadratic $f(\boldsymbol{x}) = \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x} + c$ with $A \succ 0$, $\nabla f(\boldsymbol{x}) = A\boldsymbol{x} - \boldsymbol{b}$ and the minimizer solves $A\boldsymbol{x}^* = \boldsymbol{b}$. The error $\boldsymbol{e}^{(t)} = \boldsymbol{x}^{(t)} - \boldsymbol{x}^*$ indicates how far we are from the solution; the residual $\boldsymbol{r}^{(t)} = \boldsymbol{b} - A\boldsymbol{x}^{(t)} = -\nabla f(\boldsymbol{x}^{(t)})$ indicates how far we are from $\boldsymbol{b}$. Note that $\boldsymbol{r}^{(t)} = -A\boldsymbol{e}^{(t)}$ (the residual is the error transformed into the space of $\boldsymbol{b}$) and, more importantly, the residual is the direction of steepest descent, $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} + \alpha^{(t)}\boldsymbol{r}^{(t)}$. The orthogonality condition gives the step:

$$
0 = (\boldsymbol{r}^{(t+1)})^{\mathsf T}\boldsymbol{r}^{(t)} = \bigl(\boldsymbol{b} - A(\boldsymbol{x}^{(t)} + \alpha^{(t)}\boldsymbol{r}^{(t)})\bigr)^{\mathsf T}\boldsymbol{r}^{(t)} = (\boldsymbol{r}^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)} - \alpha^{(t)}(\boldsymbol{r}^{(t)})^{\mathsf T}A\boldsymbol{r}^{(t)} \quad\Longrightarrow\quad \alpha^{(t)} = \frac{(\boldsymbol{r}^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)}}{(\boldsymbol{r}^{(t)})^{\mathsf T}A\boldsymbol{r}^{(t)}}.
$$

#### 5.2.2.2. Backtracking Line Search

Exact minimization along the line is usually unnecessary. Consider $h(\alpha) = f(\boldsymbol{x} + \alpha\Delta\boldsymbol{x})$ with $\Delta\boldsymbol{x} = -\nabla f(\boldsymbol{x})$. Its tangent line at $\alpha = 0$ is $y = f(\boldsymbol{x}) + \alpha\nabla f(\boldsymbol{x})^{\mathsf T}\Delta\boldsymbol{x}$, because $\frac{\mathrm{d}}{\mathrm{d}\alpha}f(\boldsymbol{x} + \alpha\Delta\boldsymbol{x}) = \nabla f(\boldsymbol{x} + \alpha\Delta\boldsymbol{x})^{\mathsf T}\Delta\boldsymbol{x}$. A step is acceptable when $h$ lies below a flattened version of this line.

**Definition 5.2.3 (Backtracking Line Search)** Fix $0 < \beta < 1$ (usually in $(0.1, 0.8)$) and $0 < c \le 1/2$. At each iteration, start with $\alpha = 1$ and update $\alpha \leftarrow \beta\alpha$ until the **Armijo condition**

$$
f\bigl(\boldsymbol{x}^{(k)} - \alpha\nabla f(\boldsymbol{x}^{(k)})\bigr) \le f(\boldsymbol{x}^{(k)}) - c\,\alpha\lVert\nabla f(\boldsymbol{x}^{(k)})\rVert_2^2
$$
holds; this is **backtracking line search**. The right-hand side is the line $\tilde h(\alpha) = f(\boldsymbol{x}) + c\,\alpha\nabla f(\boldsymbol{x})^{\mathsf T}\Delta\boldsymbol{x}$, the tangent with its slope reduced by the factor $c$.

The rule adapts the step size, is simple, and tends to work well in practice.

#### 5.2.2.3. Fixed Step Size

The simplest rule takes $\alpha^{(t)} = \alpha$ for all $t$. The algorithm can diverge if $\alpha$ is too big and can be slow if $\alpha$ is too small; for $f(\boldsymbol{x}) = (10x_1^2 + x_2^2)/2$, with $L = 10$ the largest eigenvalue of the Hessian, steps $\alpha > 2/L$ diverge and $\alpha = 1/L$ is about right.

![Six methods on f(x) = (10 x1^2 + x2^2)/2 from (2, 20). Top: fixed step 0.35 diverges, fixed step 0.01 is still far from the minimum after 100 steps, fixed step 0.1 = 1/L moves straight down after one step. Bottom: backtracking with beta = 0.8 and exact line search both zig-zag; the conjugate gradient method reaches the minimum in two steps.](./plots/gradient-descent-step-sizes.py)

**Example 5.2.1** Maximize $f(x) = 6x - x^3$ by steepest ascent with a fixed step:

```r
fun0 <- function(x) return(- x^3 + 6*x)   # target function
grd0 <- function(x) return(- 3*x^2 + 6)   # gradient
# steepest ascent algorithm
Steepest_Ascent <- function(x, fun = fun0, grd = grd0, step = 0.01, kmax = 1000,
                            tol1 = 1e-6, tol2 = 1e-4) {
  diff <- 2*x   # use a large value to get into the following "while" loop
  k <- 0        # count iterations
  while (any(abs(diff) > tol1*(abs(x) + tol2)) & k <= kmax) {   # stopping criterion
    g_x <- grd(x)        # gradient at x
    diff <- step * g_x   # difference used in the stopping criterion
    x <- x + diff        # update x
    k <- k + 1           # update iteration
  }
  f_x <- fun(x)
  return(list(iteration = k, x = x, f_x = f_x, g_x = g_x))
}
Steepest_Ascent(x = 2, step = 0.01)
Steepest_Ascent(x = 1, step = -0.01)
```

```text
$iteration                    $iteration
[1] 117                       [1] 159
$x                            $x
[1] 1.414228                  [1] -1.414199
$f_x                          $f_x
[1] 5.656854                  [1] -5.656854
$g_x                          $g_x
[1] -0.0001380379             [1] 0.0001370128
```

With a positive step the iteration climbs to the local maximum $x = \sqrt2$, $f = 4\sqrt2 = 5.656854$. With a negative step it moves against the gradient, i.e. it performs gradient descent, and finds the local minimum $x = -\sqrt2$. Both points are stationary; the sign of the step decides which kind is found. (Since $f$ is unbounded in both directions, neither is a global optimum.)

### 5.2.3. Convergence

If the step size is small enough, gradient descent decreases $f$. Assume that $f\colon \mathbb{R}^n \to \mathbb{R}$ is convex and differentiable and that $\nabla f$ satisfies the **Lipschitz condition** with constant $L > 0$,

$$
\lVert\nabla f(\boldsymbol{x}) - \nabla f(\boldsymbol{y})\rVert_2 \le L\lVert\boldsymbol{x} - \boldsymbol{y}\rVert_2 \quad\text{for all }\boldsymbol{x}, \boldsymbol{y}.
$$
This is a fairly weak assumption, satisfied by least squares and logistic regression (and locally by deep neural networks). For $C^2$ functions it means $\nabla^2 f(\boldsymbol{x}) \preceq LI$ for all $\boldsymbol{x}$: the eigenvalues of the Hessian are bounded above by $L$. For least squares $f(\boldsymbol{\beta}) = \frac12\lVert\boldsymbol{y} - X\boldsymbol{\beta}\rVert^2$ the smallest such $L$ is the largest eigenvalue of $X^{\mathsf T}X$.

**Theorem 5.2.1 (Convergence of Gradient Descent)** Under these assumptions, with $\boldsymbol{x}^*$ a minimizer:

1. gradient descent with a fixed step size $\alpha \le 1/L$ satisfies $f(\boldsymbol{x}^{(t)}) - f(\boldsymbol{x}^*) \le \dfrac{\lVert\boldsymbol{x}^{(0)} - \boldsymbol{x}^*\rVert_2^2}{2\alpha t}$;
2. gradient descent with backtracking line search ($c = 1/2$) satisfies $f(\boldsymbol{x}^{(t)}) - f(\boldsymbol{x}^*) \le \dfrac{\lVert\boldsymbol{x}^{(0)} - \boldsymbol{x}^*\rVert_2^2}{2\alpha_{\min}t}$ with $\alpha_{\min} = \min\{1, \beta/L\}$;
3. gradient descent with exact line search for $f(\boldsymbol{x}) = \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x} + c$, $A \succ 0$, satisfies
$$
\frac{f(\boldsymbol{x}^{(t)}) - f(\boldsymbol{x}^*)}{f(\boldsymbol{x}^{(0)}) - f(\boldsymbol{x}^*)} = \frac{(\boldsymbol{e}^{(t)})^{\mathsf T}A\boldsymbol{e}^{(t)}}{(\boldsymbol{e}^{(0)})^{\mathsf T}A\boldsymbol{e}^{(0)}} \le \left(\frac{\kappa(A) - 1}{\kappa(A) + 1}\right)^{2t},
$$
where $\boldsymbol{e}^{(t)} = \boldsymbol{x}^{(t)} - \boldsymbol{x}^*$ and $\kappa(A) = \lambda_{\max}/\lambda_{\min}$ is the condition number of $A$.

**Proof** (of item 3, sketch) The equality follows from $f(\boldsymbol{x}) - f(\boldsymbol{x}^*) = \frac12\boldsymbol{e}^{\mathsf T}A\boldsymbol{e}$, since $A\boldsymbol{x}^* = \boldsymbol{b}$. Since $A$ is symmetric, it has orthonormal eigenvectors $\boldsymbol{v}_i$ with **eigenvalues** $\lambda_i$; write $\boldsymbol{e}^{(t)} = \sum_i c_i\boldsymbol{v}_i$, so $\boldsymbol{r}^{(t)} = -A\boldsymbol{e}^{(t)} = -\sum_i c_i\lambda_i\boldsymbol{v}_i$ and

$$
(\boldsymbol{e}^{(t)})^{\mathsf T}A\boldsymbol{e}^{(t)} = \sum_i c_i^2\lambda_i, \qquad (\boldsymbol{r}^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)} = \sum_i c_i^2\lambda_i^2, \qquad (\boldsymbol{r}^{(t)})^{\mathsf T}A\boldsymbol{r}^{(t)} = \sum_i c_i^2\lambda_i^3.
$$
From $\boldsymbol{e}^{(t+1)} = \boldsymbol{e}^{(t)} + \alpha^{(t)}\boldsymbol{r}^{(t)}$ and the exact step $\alpha^{(t)} = \frac{\boldsymbol{r}^{\mathsf T}\boldsymbol{r}}{\boldsymbol{r}^{\mathsf T}A\boldsymbol{r}}$,

$$
(\boldsymbol{e}^{(t+1)})^{\mathsf T}A\boldsymbol{e}^{(t+1)} = \boldsymbol{e}^{\mathsf T}A\boldsymbol{e} + 2\alpha\boldsymbol{r}^{\mathsf T}A\boldsymbol{e} + \alpha^2\boldsymbol{r}^{\mathsf T}A\boldsymbol{r} = \boldsymbol{e}^{\mathsf T}A\boldsymbol{e} - \frac{(\boldsymbol{r}^{\mathsf T}\boldsymbol{r})^2}{\boldsymbol{r}^{\mathsf T}A\boldsymbol{r}},
$$
so the ratio $\omega^2 \triangleq \frac{(\boldsymbol{e}^{(t+1)})^{\mathsf T}A\boldsymbol{e}^{(t+1)}}{(\boldsymbol{e}^{(t)})^{\mathsf T}A\boldsymbol{e}^{(t)}} = 1 - \frac{(\sum_i c_i^2\lambda_i^2)^2}{(\sum_i c_i^2\lambda_i)(\sum_i c_i^2\lambda_i^3)}$. In two dimensions, with $\lambda_1 = \kappa$, $\lambda_2 = 1$ and $\mu = c_2/c_1$, this is $\omega^2 = 1 - \frac{(\kappa^2 + \mu^2)^2}{(\kappa + \mu^2)(\kappa^3 + \mu^2)}$; holding $\kappa$ fixed, basic calculus shows that $\omega^2$ is largest when $\mu^2 = \kappa^2$, where

$$
\omega^2 = 1 - \frac{4\kappa^4}{\kappa(\kappa + 1)\cdot\kappa^2(\kappa + 1)} = \left(\frac{\kappa - 1}{\kappa + 1}\right)^2.
$$
In $n$ dimensions the same bound follows from the Kantorovich inequality. Iterating gives the claim. $\square$

The eigenvalues matter. If all eigenvalues are equal, $\lambda_i \equiv \lambda$, then $\boldsymbol{r}^{(t)} = -\lambda\boldsymbol{e}^{(t)}$, $\alpha^{(t)} = 1/\lambda$ and $\boldsymbol{e}^{(t+1)} = \boldsymbol{e}^{(t)} + \frac1\lambda(-\lambda\boldsymbol{e}^{(t)}) = \boldsymbol{0}$: gradient descent converges on the first iteration. The more the eigenvalues differ, the slower the convergence.

What is the order of convergence? The bounds in items 1 and 2 decrease like $1/t$: the ratio of successive bounds, $\frac{t - 1}{t}$, tends to $1$, which is slower than any linear rate (sublinear convergence). Under strong convexity, $\mu I \preceq \nabla^2 f \preceq LI$, the convergence is linear, with a factor depending on the condition number $L/\mu$, as item 3 shows for quadratics.

**Theorem 5.2.2 (Global Convergence of Steepest Descent)** Suppose that $f\colon \mathbb{R}^n \to \mathbb{R}$ is continuously differentiable on the set $S = \{\boldsymbol{x} \in \mathbb{R}^n\colon f(\boldsymbol{x}) \le f(\boldsymbol{x}^{(0)})\}$, and that $S$ is closed and bounded. Then every cluster point $\bar{\boldsymbol{x}}$ of the sequence $\{\boldsymbol{x}^{(t)}\}$ generated by gradient descent with exact line search satisfies $\nabla f(\bar{\boldsymbol{x}}) = \boldsymbol{0}$.

**Proof** The iterates stay in $S$, since $f$ decreases. By the **Bolzano–Weierstrass theorem** at least one cluster point exists; let $\bar{\boldsymbol{x}}$ be one, and, passing to a subsequence, assume $\boldsymbol{x}^{(t)} \to \bar{\boldsymbol{x}}$. Suppose, for contradiction, that $\nabla f(\bar{\boldsymbol{x}}) \ne \boldsymbol{0}$, and let $\bar{\boldsymbol{d}} = -\nabla f(\bar{\boldsymbol{x}})$. Then there is $\bar\alpha > 0$ with $\delta \triangleq f(\bar{\boldsymbol{x}}) - f(\bar{\boldsymbol{x}} + \bar\alpha\bar{\boldsymbol{d}}) > 0$. Let $\boldsymbol{d}^{(t)} = -\nabla f(\boldsymbol{x}^{(t)})$. Since $\boldsymbol{d}^{(t)} \to \bar{\boldsymbol{d}}$, also $\boldsymbol{x}^{(t)} + \bar\alpha\boldsymbol{d}^{(t)} \to \bar{\boldsymbol{x}} + \bar\alpha\bar{\boldsymbol{d}}$, and by continuity, for $t$ sufficiently large,

$$
f(\boldsymbol{x}^{(t)} + \bar\alpha\boldsymbol{d}^{(t)}) \le f(\bar{\boldsymbol{x}} + \bar\alpha\bar{\boldsymbol{d}}) + \frac\delta2 = f(\bar{\boldsymbol{x}}) - \frac\delta2.
$$
However, since $f(\boldsymbol{x}^{(t)})$ decreases to $f(\bar{\boldsymbol{x}})$ and $\alpha^{(t)}$ minimizes $f$ along the line,

$$
f(\bar{\boldsymbol{x}}) < f(\boldsymbol{x}^{(t)} + \alpha^{(t)}\boldsymbol{d}^{(t)}) \le f(\boldsymbol{x}^{(t)} + \bar\alpha\boldsymbol{d}^{(t)}) \le f(\bar{\boldsymbol{x}}) - \frac\delta2,
$$
a contradiction. Thus $\nabla f(\bar{\boldsymbol{x}}) = \boldsymbol{0}$. $\square$

### 5.2.4. Advantages and Disadvantages

Advantages of the gradient method:

- every iteration is inexpensive and requires only gradients, not second derivatives;
- it can be very fast for smooth objective functions that are well-conditioned and strongly convex;
- it is stable: if minimum points exist, the method is guaranteed to locate them, possibly only after infinitely many iterations; many methods switch to steepest descent steps when they do not make sufficient progress.

Disadvantages:

- it is often slow (linear): performing the line search can be time-consuming, while a fixed small step size can yield poor convergence; if the eigenvalues of the Hessian at $\boldsymbol{x}^*$ differ by several orders of magnitude, a very large number of iterations may be required;
- it is not scale invariant: changing the inner product on $\mathbb{R}^n$ changes the notion of gradient. For example, $f(x) = 4x^2$ from $x = 1/2$ and $\tilde f(z) = z^2$ from $z = 1$ describe the same problem with $z = 2x$, but gradient descent with the same step size produces different sequences in the two parametrizations (the factors per step are $1 - 8\alpha$ and $1 - 2\alpha$), whereas Newton's method solves both in one step;
- it cannot handle non-differentiable functions.

#### 5.2.4.1. Steepest Descent

Gradient descent is the special case of steepest descent in which the norm is Euclidean.

**Definition 5.2.4 (Steepest Descent Direction)** For a norm $\lVert\cdot\rVert$ with dual norm $\lVert\boldsymbol{z}\rVert_* = \sup_{\lVert\boldsymbol{x}\rVert \le 1}\boldsymbol{z}^{\mathsf T}\boldsymbol{x}$, a normalized steepest descent direction is

$$
\Delta\boldsymbol{x}_{\mathrm{nsd}} = \arg\min_{\lVert\boldsymbol{v}\rVert \le 1}\nabla f(\boldsymbol{x})^{\mathsf T}\boldsymbol{v},
$$
a step of unit norm with the largest decrease in the linear approximation of $f$; it satisfies $\nabla f(\boldsymbol{x})^{\mathsf T}\Delta\boldsymbol{x}_{\mathrm{nsd}} = -\lVert\nabla f(\boldsymbol{x})\rVert_*$. The unnormalized steepest descent direction is $\Delta\boldsymbol{x}_{\mathrm{sd}} = \lVert\nabla f(\boldsymbol{x})\rVert_*\Delta\boldsymbol{x}_{\mathrm{nsd}} = \arg\min_{\boldsymbol{v}}\bigl(\nabla f(\boldsymbol{x})^{\mathsf T}\boldsymbol{v} + \frac12\lVert\boldsymbol{v}\rVert^2\bigr)$, and the **steepest descent method** moves along $\Delta\boldsymbol{x}_{\mathrm{sd}}$.

Indeed, for $\boldsymbol{v} = k\Delta\boldsymbol{x}_{\mathrm{nsd}}$ the objective is $-k\lVert\nabla f(\boldsymbol{x})\rVert_* + \frac12k^2$, minimized at $k = \lVert\nabla f(\boldsymbol{x})\rVert_*$. For the $\ell_p$ norms, the dual of $\lVert\cdot\rVert_p$ is $\lVert\cdot\rVert_q$ with $\frac1p + \frac1q = 1$, by Hölder's inequality $\sum_i x_iy_i \le \lVert\boldsymbol{x}\rVert_p\lVert\boldsymbol{y}\rVert_q$:

- for $p = 2$, $\Delta\boldsymbol{x}_{\mathrm{nsd}} = -\nabla f(\boldsymbol{x})/\lVert\nabla f(\boldsymbol{x})\rVert_2$ and $\Delta\boldsymbol{x}_{\mathrm{sd}} = -\nabla f(\boldsymbol{x})$: gradient descent;
- for $p = 1$, choose $i$ with $\lvert\partial f(\boldsymbol{x})/\partial x_i\rvert = \max_j\lvert\partial f(\boldsymbol{x})/\partial x_j\rvert = \lVert\nabla f(\boldsymbol{x})\rVert_\infty$; then $\Delta\boldsymbol{x}_{\mathrm{nsd}} = -\operatorname{sgn}\bigl(\partial f(\boldsymbol{x})/\partial x_i\bigr)\boldsymbol{e}_i$ and $\Delta\boldsymbol{x}_{\mathrm{sd}} = -\frac{\partial f(\boldsymbol{x})}{\partial x_i}\boldsymbol{e}_i$: a coordinate descent step along the coordinate with the largest partial derivative (compare the coordinate descent of [3.5.4](/3.5.4)).

When is the negative gradient not the truly steepest direction? When the rate of change differs greatly along different directions, which is read off the Hessian. Define the *energy norm* $\lVert\boldsymbol{x}\rVert_A = (\boldsymbol{x}^{\mathsf T}A\boldsymbol{x})^{1/2}$ for $A \succ 0$. It is the natural norm for the quadratic approximation $f(\boldsymbol{x}) \approx f(\boldsymbol{x}^*) + \frac12(\boldsymbol{x} - \boldsymbol{x}^*)^{\mathsf T}A(\boldsymbol{x} - \boldsymbol{x}^*)$ with $A = \nabla^2 f(\boldsymbol{x}^*)$, since minimizing $f(\boldsymbol{x}^{(t)})$ is then equivalent to minimizing $\lVert\boldsymbol{e}^{(t)}\rVert_A$. Its dual norm is $\lVert\cdot\rVert_{A^{-1}}$, because $\boldsymbol{x}^{\mathsf T}\boldsymbol{y} = (A^{1/2}\boldsymbol{x})^{\mathsf T}(A^{-1/2}\boldsymbol{y}) \le \lVert\boldsymbol{x}\rVert_A\lVert\boldsymbol{y}\rVert_{A^{-1}}$. Hence

$$
\Delta\boldsymbol{x}_{\mathrm{nsd}} = \arg\min_{\lVert\boldsymbol{v}\rVert_A \le 1}\nabla f(\boldsymbol{x})^{\mathsf T}\boldsymbol{v} = -\frac{A^{-1}\nabla f(\boldsymbol{x})}{\lVert\nabla f(\boldsymbol{x})\rVert_{A^{-1}}}, \qquad \Delta\boldsymbol{x}_{\mathrm{sd}} = \lVert\nabla f(\boldsymbol{x})\rVert_{A^{-1}}\Delta\boldsymbol{x}_{\mathrm{nsd}} = -A^{-1}\nabla f(\boldsymbol{x}).
$$
With $A = \nabla^2 f(\boldsymbol{x})$ this is the Newton step: Newton's method is steepest descent in the norm $\lVert\cdot\rVert_{\nabla^2 f(\boldsymbol{x})}$.

#### 5.2.4.2. Stochastic Gradient Descent

For least squares, $f(\boldsymbol{\beta}) = \lVert\boldsymbol{Y} - X\boldsymbol{\beta}\rVert^2 = \sum_{i=1}^n r_i^2$. With 10,000 data points and 10 features, each gradient needs the derivative of every $r_i$ with respect to every $\beta_j$, in effect $10{,}000 \times 10 = 100{,}000$ computations per iteration; with the common 1,000 iterations this is $10^8$ computations, slow on huge data.

**Definition 5.2.5 (Stochastic Gradient Descent)** For an objective $f(\boldsymbol{\beta}) = \sum_{i=1}^n f_i(\boldsymbol{\beta})$, **stochastic gradient descent** (SGD) picks at each iteration one data point $i$ at random from the whole data set and updates $\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} - \alpha^{(t)}\nabla f_i(\boldsymbol{\beta}^{(t)})$. If at each step a small random subset $B$ of points is used instead, $\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} - \alpha^{(t)}\frac{n}{\lvert B\rvert}\sum_{i \in B}\nabla f_i(\boldsymbol{\beta}^{(t)})$, the method is called **mini-batch gradient descent**.

SGD reduces the computations enormously and easily handles new data points without starting from the very beginning. Since $n\nabla f_i$ with a random $i$ is an unbiased estimate of $\nabla f$, the iterates move in the right direction on average, but noisily; for convergence the step sizes must decrease, for example with $\sum_t\alpha^{(t)} = \infty$ and $\sum_t(\alpha^{(t)})^2 < \infty$. Mini-batches strike a balance between the accuracy of full gradient descent and the speed of SGD.

## 5.3. Conjugate Direction Methods

### 5.3.1. Conjugate Direction Methods

#### 5.3.1.1. Background

Steepest descent is slow; Newton's method is fast but needs the inverse of the Hessian. Conjugate direction methods lie between them: they aim to accelerate the convergence of steepest descent while avoiding the high computational cost of Newton's method. They were originally developed for the quadratic problem

$$
\min_{\boldsymbol{x} \in \mathbb{R}^n}\ \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x}, \qquad A \succ 0,
$$
which is equivalent to solving $A\boldsymbol{x} = \boldsymbol{b}$. A conjugate direction method solves this problem in at most $n$ iterations; it can be applied to systems too large for direct methods such as the Cholesky decomposition, and it is the standard algorithm for large, sparse, symmetric (or Hermitian) positive definite systems; it can also seek minima of nonlinear functions.

Recall steepest descent for this $f$: start at $\boldsymbol{x}^{(0)}$, take steps $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\nabla f(\boldsymbol{x}^{(t)})$, and stop when close enough to $\boldsymbol{x}^*$; the error is $\boldsymbol{e}^{(t)} = \boldsymbol{x}^{(t)} - \boldsymbol{x}^*$ and the residual $\boldsymbol{r}^{(t)} = \boldsymbol{b} - A\boldsymbol{x}^{(t)} = -A\boldsymbol{e}^{(t)} = -\nabla f(\boldsymbol{x}^{(t)})$. The exact line search makes $\nabla f(\boldsymbol{x}^{(t+1)}) \perp \nabla f(\boldsymbol{x}^{(t)})$, but it often takes steps in the same directions as earlier steps. Change notation to the general update $\boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k$, so that $\boldsymbol{x}_{k+1} = \boldsymbol{x}_{k-1} + \alpha_{k-1}\boldsymbol{d}_{k-1} + \alpha_k\boldsymbol{d}_k = \cdots$. Suppose we pick a set of search directions and in each direction take exactly one step, of just the right length, so that after $n$ steps we are done. Then each step must be optimal along all previous directions as well, i.e. the first-order optimality condition

$$
0 = \frac{\mathrm{d}}{\mathrm{d}\alpha_i}f(\boldsymbol{x}_{k+1}) = \boldsymbol{d}_i^{\mathsf T}\nabla f(\boldsymbol{x}_{k+1}) = \boldsymbol{d}_i^{\mathsf T}A\boldsymbol{e}_{k+1}, \qquad i \le k,
$$
must hold: the new requirement is that $\boldsymbol{e}_{k+1}$ be $A$-orthogonal to the $\boldsymbol{d}_i$.

#### 5.3.1.2. $A$-Conjugacy

**Definition 5.3.1 ($A$-Conjugate Directions)** Let $A$ be a symmetric matrix. Vectors $\boldsymbol{d}_1, \boldsymbol{d}_2, \dots, \boldsymbol{d}_k$ are **conjugate directions** with respect to $A$ ($A$-conjugate, $A$-orthogonal, or orthogonal with respect to $A$) if

$$
\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_j = 0 \qquad \text{for all } i \ne j.
$$

In most applications $A$ is positive definite. If $A = O$, any two vectors are conjugate; if $A = I$, conjugacy is the usual orthogonality. In general, $A$-conjugate vectors are orthogonal after the transformation $\boldsymbol{d} \mapsto A^{1/2}\boldsymbol{d}$, which stretches the elliptic contours of $f$ into circles.

#### 5.3.1.3. Properties of $A$-Conjugacy

**Lemma 5.3.1 (Linear Independence)** Let $A$ be positive definite. If nonzero vectors $\boldsymbol{d}_1, \dots, \boldsymbol{d}_k$ are $A$-conjugate, then they are linearly independent.

**Proof** If, say, $\boldsymbol{d}_k = \alpha_1\boldsymbol{d}_1 + \cdots + \alpha_{k-1}\boldsymbol{d}_{k-1}$, then $0 < \boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k = \boldsymbol{d}_k^{\mathsf T}A(\alpha_1\boldsymbol{d}_1 + \cdots + \alpha_{k-1}\boldsymbol{d}_{k-1}) = 0$, a contradiction. $\square$

For the quadratic problem with $A \succ 0$, the unique minimizer $\boldsymbol{x}^*$ is also the unique solution of $A\boldsymbol{x} = \boldsymbol{b}$. Let $\boldsymbol{d}_0, \dots, \boldsymbol{d}_{n-1}$ be nonzero and $A$-conjugate. They are linearly independent, so $\boldsymbol{x}^* = \alpha_0\boldsymbol{d}_0 + \cdots + \alpha_{n-1}\boldsymbol{d}_{n-1}$, and multiplying by $\boldsymbol{d}_i^{\mathsf T}A$ gives $\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{x}^* = \alpha_i\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i$, hence

$$
\alpha_i = \frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{x}^*}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i} = \frac{\boldsymbol{d}_i^{\mathsf T}\boldsymbol{b}}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}, \qquad \boldsymbol{x}^* = \sum_{i=0}^{n-1}\frac{\boldsymbol{d}_i^{\mathsf T}\boldsymbol{b}}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}\boldsymbol{d}_i.
$$
Newton's method requires a matrix inversion; given conjugate directions, we only need inner products. The expansion can be read as the result of an iterative process of $n$ steps, where at the $i$th step $\alpha_i\boldsymbol{d}_i$ is added. Another motivation: writing $\boldsymbol{x} - \boldsymbol{x}_0 = \sum_{i=0}^{n-1}\alpha_i\boldsymbol{d}_i$, the cross terms $\alpha_i\alpha_j\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_j$ vanish and

$$
f(\boldsymbol{x}) = c + \sum_{i=0}^{n-1}\left[\frac12\alpha_i^2\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i + \alpha_i\boldsymbol{d}_i^{\mathsf T}(A\boldsymbol{x}_0 - \boldsymbol{b})\right]
$$
separates into $n$ one-dimensional optimization problems.

**Theorem 5.3.1 (Conjugate Direction Theorem)** Let $\boldsymbol{d}_0, \dots, \boldsymbol{d}_{n-1}$ be nonzero $A$-conjugate vectors, $A \succ 0$, and let $\boldsymbol{x}_0 \in \mathbb{R}^n$ be an arbitrary starting point. With the update rule $\boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k$, the gradient $\boldsymbol{g}_k \triangleq \nabla f(\boldsymbol{x}_k) = A\boldsymbol{x}_k - \boldsymbol{b}$ and

$$
\alpha_k = -\frac{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k} = \frac{\boldsymbol{d}_k^{\mathsf T}\boldsymbol{r}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k},
$$
after $n$ steps $\boldsymbol{x}_n = \boldsymbol{x}^*$.

**Proof** Since the $\boldsymbol{d}_i$ are independent, $\boldsymbol{x}^* - \boldsymbol{x}_0 = \alpha_0'\boldsymbol{d}_0 + \cdots + \alpha_{n-1}'\boldsymbol{d}_{n-1}$ for some coefficients $\alpha_i'$, and by the update rule $\boldsymbol{x}_k = \boldsymbol{x}_0 + \alpha_0\boldsymbol{d}_0 + \cdots + \alpha_{k-1}\boldsymbol{d}_{k-1}$. It is therefore enough to show $\alpha_k' = \alpha_k$. Multiplying the first expansion by $\boldsymbol{d}_k^{\mathsf T}A$ gives $\alpha_k' = \frac{\boldsymbol{d}_k^{\mathsf T}A(\boldsymbol{x}^* - \boldsymbol{x}_0)}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k}$. By conjugacy $\boldsymbol{d}_k^{\mathsf T}A(\boldsymbol{x}_k - \boldsymbol{x}_0) = 0$, so

$$
\boldsymbol{d}_k^{\mathsf T}A(\boldsymbol{x}^* - \boldsymbol{x}_0) = \boldsymbol{d}_k^{\mathsf T}A(\boldsymbol{x}^* - \boldsymbol{x}_k) = -\boldsymbol{d}_k^{\mathsf T}(A\boldsymbol{x}_k - \boldsymbol{b}) = -\boldsymbol{d}_k^{\mathsf T}\boldsymbol{g}_k,
$$
and $\alpha_k' = -\frac{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k} = \alpha_k$. $\square$

Geometrically, $\boldsymbol{e}_0 = \boldsymbol{x}_0 - \boldsymbol{x}^* = -\sum_{i=0}^{n-1}\alpha_i\boldsymbol{d}_i$, and each step of the method eliminates one of these $A$-orthogonal components.

**Theorem 5.3.2 (Expanding Subspace Theorem)** Let $\boldsymbol{d}_0, \dots, \boldsymbol{d}_{n-1}$ be nonzero $A$-conjugate vectors in $\mathbb{R}^n$, $\boldsymbol{x}_0 \in \mathbb{R}^n$ arbitrary, $\boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k$ with $\alpha_k$ as in Theorem 5.3.1, and $\mathcal{B}_k = \operatorname{span}\{\boldsymbol{d}_0, \dots, \boldsymbol{d}_{k-1}\} \subset \mathbb{R}^n$. Then

$$
\boldsymbol{x}_k = \arg\min_{\boldsymbol{x} = \boldsymbol{x}_{k-1} + \alpha\boldsymbol{d}_{k-1},\ \alpha \in \mathbb{R}}\ \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x} = \arg\min_{\boldsymbol{x} \in \boldsymbol{x}_0 + \mathcal{B}_k}\ \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x}.
$$

**Proof** Since $\boldsymbol{x}_0 + \mathcal{B}_k$ contains the line $\boldsymbol{x}_{k-1} + \alpha\boldsymbol{d}_{k-1}$, it is enough to show that $\boldsymbol{x}_k$ minimizes $f$ over $\boldsymbol{x}_0 + \mathcal{B}_k$. As $f$ is strictly convex, it suffices that $\boldsymbol{g}_k = \nabla f(\boldsymbol{x}_k) \perp \mathcal{B}_k$: then for every $\boldsymbol{x} \ne \boldsymbol{x}_k$ in $\boldsymbol{x}_0 + \mathcal{B}_k$,

$$
f(\boldsymbol{x}) = f(\boldsymbol{x}_k) + \boldsymbol{g}_k^{\mathsf T}(\boldsymbol{x} - \boldsymbol{x}_k) + \frac12(\boldsymbol{x} - \boldsymbol{x}_k)^{\mathsf T}A(\boldsymbol{x} - \boldsymbol{x}_k) > f(\boldsymbol{x}_k) + \boldsymbol{g}_k^{\mathsf T}(\boldsymbol{x} - \boldsymbol{x}_k) = f(\boldsymbol{x}_k).
$$
We prove $\boldsymbol{g}_k \perp \mathcal{B}_k$ by induction. For $k = 0$, $\mathcal{B}_0 = \{\boldsymbol{0}\}$. Assume $\boldsymbol{g}_k \perp \mathcal{B}_k$. Since $\boldsymbol{g}_{k+1} = A(\boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k) - \boldsymbol{b} = \boldsymbol{g}_k + \alpha_kA\boldsymbol{d}_k$,

$$
\boldsymbol{d}_k^{\mathsf T}\boldsymbol{g}_{k+1} = \boldsymbol{d}_k^{\mathsf T}\boldsymbol{g}_k - \frac{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k}\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k = 0, \qquad \boldsymbol{d}_i^{\mathsf T}\boldsymbol{g}_{k+1} = \boldsymbol{d}_i^{\mathsf T}\boldsymbol{g}_k + \alpha_k\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_k = 0 \quad (i < k),
$$
so $\boldsymbol{g}_{k+1} \perp \mathcal{B}_{k+1}$. $\square$

The subspaces $\mathcal{B}_k$ form an increasing sequence, $\mathcal{B}_{k+1} \supset \mathcal{B}_k$, and $\boldsymbol{g}_k \perp \boldsymbol{d}_i$ for $i < k$ (the first-order optimality condition $\boldsymbol{d}_i^{\mathsf T}\nabla f(\boldsymbol{x}_{k+1}) = 0$, $i \le k$). Since $\boldsymbol{x}_k$ minimizes $f$ over $\boldsymbol{x}_0 + \mathcal{B}_k$, $\boldsymbol{x}_n$ minimizes $f$ over $\boldsymbol{x}_0 + \mathcal{B}_n = \mathbb{R}^n$. In terms of the energy norm, minimizing $f$ is minimizing $\lVert\boldsymbol{e}\rVert_A^2 = \sum_i\alpha_i^2\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i$, a sum of separate terms; because $\boldsymbol{d}_k$ is orthogonal to $\mathcal{B}_k$ in the energy inner product, $\boldsymbol{x}_{k+1}$ is found by minimizing $f$ along $\boldsymbol{d}_k$ and adding the result to $\boldsymbol{x}_k$.

**Theorem 5.3.3 (DFP Is a Conjugate Direction Method)** Let $f$ be quadratic with positive definite Hessian $A$, and run the DFP method (Algorithm 5.1.3 with the update (5.5)) with exact line search; write $\boldsymbol{z}_i = \boldsymbol{x}_{i+1} - \boldsymbol{x}_i$ for the steps and $\boldsymbol{g}_i = \nabla f(\boldsymbol{x}_i)$. Then, for $k \le n$,

1. the search vectors are conjugate, $\boldsymbol{z}_i^{\mathsf T}A\boldsymbol{z}_j = 0$ for $0 \le i < j < k$;
2. $H_kA\boldsymbol{z}_i = \boldsymbol{z}_i$ for $0 \le i < k$: the secant equation holds not only along the most recent direction but along all previous ones.

Consequently the method terminates in at most $n$ steps with $H_n = A^{-1}$, the $k$th direction lies in $\operatorname{span}\{H_0\boldsymbol{g}_0, \dots, H_0\boldsymbol{g}_{k-1}\}$, and $\boldsymbol{g}_i^{\mathsf T}H_0\boldsymbol{g}_j = 0$ for $i \ne j$.

**Proof** (sketch) Here $\boldsymbol{y}_i = \boldsymbol{g}_{i+1} - \boldsymbol{g}_i = A\boldsymbol{z}_i$, $\boldsymbol{z}_i = -\alpha_iH_i\boldsymbol{g}_i$, exact line search gives $\boldsymbol{z}_i^{\mathsf T}\boldsymbol{g}_{i+1} = 0$, and the secant equation gives $\boldsymbol{z}_i = H_{i+1}\boldsymbol{y}_i = H_{i+1}A\boldsymbol{z}_i$. For $k = 1$ the claims hold: $H_1A\boldsymbol{z}_0 = \boldsymbol{z}_0$ and $0 = \boldsymbol{z}_0^{\mathsf T}\boldsymbol{g}_1 = \boldsymbol{z}_0^{\mathsf T}AH_1\boldsymbol{g}_1 = -\boldsymbol{z}_0^{\mathsf T}A\boldsymbol{z}_1/\alpha_1$. For the induction step, $\boldsymbol{g}_k = \boldsymbol{g}_{i+1} + A(\boldsymbol{z}_{i+1} + \cdots + \boldsymbol{z}_{k-1})$, so $\boldsymbol{z}_i^{\mathsf T}\boldsymbol{g}_k = \boldsymbol{z}_i^{\mathsf T}\boldsymbol{g}_{i+1} = 0$ for $i < k$, and then $0 = \boldsymbol{z}_i^{\mathsf T}AH_k\boldsymbol{g}_k = -\boldsymbol{z}_i^{\mathsf T}A\boldsymbol{z}_k/\alpha_k$; moreover $\boldsymbol{y}_k^{\mathsf T}H_kA\boldsymbol{z}_i = \boldsymbol{y}_k^{\mathsf T}\boldsymbol{z}_i = \boldsymbol{z}_k^{\mathsf T}A\boldsymbol{z}_i = 0$, so both correction terms of (5.5) annihilate $A\boldsymbol{z}_i$ and $H_{k+1}A\boldsymbol{z}_i = H_kA\boldsymbol{z}_i = \boldsymbol{z}_i$. Finally, $n$ independent vectors with $H_nA\boldsymbol{z}_i = \boldsymbol{z}_i$ force $H_nA = I$. $\square$

#### 5.3.1.4. Constructing Conjugate Directions by Gram–Schmidt

**Lemma 5.3.2 (Gram–Schmidt Conjugation)** Let $\boldsymbol{v}_0, \boldsymbol{v}_1, \dots, \boldsymbol{v}_{n-1}$ be linearly independent and $A \succ 0$, and define recursively

$$
\boldsymbol{d}_k = \boldsymbol{v}_k - \sum_{i=0}^{k-1}\beta_{ki}\boldsymbol{d}_i, \qquad \beta_{ki} = \frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{v}_k}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}.
$$
Then $\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_k = 0$ for all $j \ne k$.

**Proof** By induction over $k$; for $k = 0$ there is nothing to prove. Assume $\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_h = 0$ for all $j \ne h$ in $\{0, \dots, k - 1\}$. For $j < k$, only the term $i = j$ of the sum survives:

$$
\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_k = \boldsymbol{d}_j^{\mathsf T}A\boldsymbol{v}_k - \sum_{i=0}^{k-1}\frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{v}_k}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_i = \boldsymbol{d}_j^{\mathsf T}A\boldsymbol{v}_k - \boldsymbol{d}_j^{\mathsf T}A\boldsymbol{v}_k = 0.
$$
The linear independence of the $\boldsymbol{v}_i$ guarantees that no $\boldsymbol{d}_i$ is zero (each $\boldsymbol{d}_k$ is $\boldsymbol{v}_k$ plus a combination of $\boldsymbol{v}_0, \dots, \boldsymbol{v}_{k-1}$), hence $\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i > 0$ for all $i$. $\square$

This is the **Gram–Schmidt process** in the inner product $\langle\boldsymbol{u}, \boldsymbol{v}\rangle_A = \boldsymbol{u}^{\mathsf T}A\boldsymbol{v}$, starting from two (or more) linearly independent vectors.

#### 5.3.1.5. Conjugate Directions and Gaussian Elimination

Gram–Schmidt conjugation has a drawback: it requires holding all previous vectors $\boldsymbol{d}_i$ ($i < k$) in memory, so as $k \to n$ the method needs $O(n^2)$ memory (and $O(n^3)$ operations). If $\boldsymbol{v}_k = \boldsymbol{e}_k$, the axial unit vectors, the conjugate direction method is **Gaussian elimination**. For this reason conjugate directions saw little use until the discovery of the conjugate gradient method.

Consider $n = 2$, a symmetric $A = \begin{bmatrix}a_{11} & a_{12} \\ a_{21} & a_{22}\end{bmatrix}$ ($a_{21} = a_{12}$), $\boldsymbol{x}_0 = \boldsymbol{0}$, $\boldsymbol{v}_0 = \boldsymbol{e}_1$ and $\boldsymbol{v}_1 = \boldsymbol{e}_2$. Gram–Schmidt conjugation gives

$$
\boldsymbol{d}_0 = \boldsymbol{e}_1, \qquad \boldsymbol{d}_1 = \boldsymbol{e}_2 - \frac{\boldsymbol{e}_1^{\mathsf T}A\boldsymbol{e}_2}{\boldsymbol{e}_1^{\mathsf T}A\boldsymbol{e}_1}\boldsymbol{e}_1 = \begin{bmatrix}l \\ 1\end{bmatrix}, \qquad l \triangleq -\frac{a_{12}}{a_{11}},
$$
and $\boldsymbol{d}_1^{\mathsf T}\boldsymbol{b} = lb_1 + b_2$, $\boldsymbol{d}_1^{\mathsf T}A\boldsymbol{d}_1 = a_{22} + 2la_{12} + l^2a_{11} = la_{12} + a_{22}$, so

$$
\boldsymbol{x}^* = \frac{\boldsymbol{d}_0^{\mathsf T}\boldsymbol{b}}{\boldsymbol{d}_0^{\mathsf T}A\boldsymbol{d}_0}\boldsymbol{d}_0 + \frac{\boldsymbol{d}_1^{\mathsf T}\boldsymbol{b}}{\boldsymbol{d}_1^{\mathsf T}A\boldsymbol{d}_1}\boldsymbol{d}_1 = \frac{b_1}{a_{11}}\begin{bmatrix}1 \\ 0\end{bmatrix} + \frac{lb_1 + b_2}{la_{12} + a_{22}}\begin{bmatrix}l \\ 1\end{bmatrix}.
$$
Gaussian elimination with the multiplier $l = -a_{21}/a_{11}$ transforms the augmented matrix $\begin{bmatrix}a_{11} & a_{12} & b_1 \\ a_{21} & a_{22} & b_2\end{bmatrix}$ into $\begin{bmatrix}a_{11} & a_{12} & b_1 \\ 0 & a_{22} + la_{12} & b_2 + lb_1\end{bmatrix}$, and back substitution gives $x_2 = \frac{lb_1 + b_2}{la_{12} + a_{22}}$ and $x_1 = \frac{b_1 - a_{12}x_2}{a_{11}} = \frac{b_1}{a_{11}} + lx_2$: the same solution. In general, the second row after the first elimination step is $A_2^{(2)} = A_2^{(1)} - \frac{A_{2,1}^{(1)}}{A_{1,1}^{(1)}}A_1^{(1)}$, and since $A_i^{(1)} = \boldsymbol{e}_i^{\mathsf T}A$ and $A_{i,j}^{(1)} = \boldsymbol{e}_i^{\mathsf T}A\boldsymbol{e}_j$,

$$
A_2^{(2)} = \left(\boldsymbol{e}_2 - \frac{\boldsymbol{e}_1^{\mathsf T}A\boldsymbol{e}_2}{\boldsymbol{e}_1^{\mathsf T}A\boldsymbol{e}_1}\boldsymbol{e}_1\right)^{\mathsf T}A = \boldsymbol{d}_1^{\mathsf T}A, \qquad A^{(2)} = \begin{bmatrix}\boldsymbol{d}_0^{\mathsf T} \\ \boldsymbol{d}_1^{\mathsf T}\end{bmatrix}A = L_1A, \qquad \boldsymbol{b}^{(2)} = L_1\boldsymbol{b}:
$$
the eliminated matrix is produced by the conjugate Gram–Schmidt algorithm. Comparing the method of orthogonal directions with that of conjugate directions along the axial unit vectors, performing conjugate directions (including conjugate gradients) amounts to performing orthogonal directions in a stretched (scaled) space.

### 5.3.2. The Conjugate Gradient Method

#### 5.3.2.1. Quadratic Problems

By the expanding subspace theorem, $\boldsymbol{g}_k \perp \mathcal{B}_k$, so a nonzero gradient $\boldsymbol{g}_k$ is linearly independent of the previous directions and can produce a new search direction. Choosing $\boldsymbol{v}_k = -\boldsymbol{g}_k$ in Gram–Schmidt conjugation turns out to require only $O(n)$ storage.

**Lemma 5.3.3 (Orthogonality)** Choose $\boldsymbol{d}_0 = -\nabla f(\boldsymbol{x}_0)$ and for $k = 1, \dots, n - 1$ let

$$
\boldsymbol{d}_k = -\nabla f(\boldsymbol{x}_k) - \sum_{i=0}^{k-1}\beta_{ki}\boldsymbol{d}_i, \qquad \beta_{ki} = \frac{\boldsymbol{d}_i^{\mathsf T}A\bigl(-\nabla f(\boldsymbol{x}_k)\bigr)}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i},
$$
with $\boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k$ and $\alpha_k$ as in Theorem 5.3.1. Then $\nabla f(\boldsymbol{x}_j)^{\mathsf T}\nabla f(\boldsymbol{x}_k) = 0$ and $\boldsymbol{d}_j^{\mathsf T}\nabla f(\boldsymbol{x}_k) = 0$ for $j < k$.

**Proof** Note that $\nabla f(\boldsymbol{x}_k) = A\boldsymbol{x}_k - \boldsymbol{b}$ for all $k$. By induction over $k$ we prove $\boldsymbol{d}_j^{\mathsf T}\nabla f(\boldsymbol{x}_k) = 0$ for all $j < k$. This is vacuous for $k = 0$. Assume it holds for $k$. Then for $j < k$,

$$
\boldsymbol{d}_j^{\mathsf T}\nabla f(\boldsymbol{x}_{k+1}) = \boldsymbol{d}_j^{\mathsf T}\bigl(A(\boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k) - \boldsymbol{b}\bigr) = \boldsymbol{d}_j^{\mathsf T}\nabla f(\boldsymbol{x}_k) + \alpha_k\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_k = 0,
$$
since $\boldsymbol{d}_k$ is $A$-conjugate to the earlier directions by construction (Lemma 5.3.2); and $\boldsymbol{d}_k^{\mathsf T}\nabla f(\boldsymbol{x}_{k+1}) = 0$ is the first-order optimality condition of the line search $\min_\alpha f(\boldsymbol{x}_k + \alpha\boldsymbol{d}_k)$ defining $\boldsymbol{x}_{k+1}$. Next, the definition of $\boldsymbol{d}_k$ implies $\operatorname{span}(\boldsymbol{d}_0, \dots, \boldsymbol{d}_k) = \operatorname{span}\bigl(\nabla f(\boldsymbol{x}_0), \dots, \nabla f(\boldsymbol{x}_k)\bigr)$ for all $k$. For $j < k$ there are therefore $c_0, \dots, c_j$ with $\nabla f(\boldsymbol{x}_j) = \sum_{i=0}^jc_i\boldsymbol{d}_i$, and

$$
\nabla f(\boldsymbol{x}_j)^{\mathsf T}\nabla f(\boldsymbol{x}_k) = \sum_{i=0}^jc_i\boldsymbol{d}_i^{\mathsf T}\nabla f(\boldsymbol{x}_k) = 0. \qquad\square
$$

Conjugate means orthogonal here: the search directions are orthogonal with respect to $A$, and the gradients, i.e. the residuals $\boldsymbol{r}_k = \boldsymbol{b} - A\boldsymbol{x}_k$, are orthogonal. The orthogonality of the residuals implies that $\boldsymbol{x}_m$ equals the solution of $A\boldsymbol{x} = \boldsymbol{b}$ for some $m \le n$: if $\boldsymbol{x}_k \ne \boldsymbol{x}^*$ for all $k = 0, 1, \dots, n - 1$, then the nonzero $\boldsymbol{r}_0, \dots, \boldsymbol{r}_{n-1}$ form an orthogonal basis of $\mathbb{R}^n$, and $\boldsymbol{r}_n$, being orthogonal to all of them, is $\boldsymbol{0}$, so $\boldsymbol{x}_n = \boldsymbol{x}^*$.

Why the choice $\boldsymbol{v}_k = \boldsymbol{r}_k$? The residual worked for steepest descent, and the property $\boldsymbol{r}_k \perp \mathcal{B}_k$ guarantees that a nonzero $\boldsymbol{r}_k$ always produces a new, linearly independent search direction $\boldsymbol{d}_k$. Since the $\boldsymbol{d}_k$ are built from the $\boldsymbol{r}_k$, $\mathcal{B}_k = \operatorname{span}\{\boldsymbol{d}_0, \dots, \boldsymbol{d}_{k-1}\} = \operatorname{span}\{\boldsymbol{r}_0, \dots, \boldsymbol{r}_{k-1}\}$; and since $\boldsymbol{r}_k = \boldsymbol{r}_{k-1} - \alpha_{k-1}A\boldsymbol{d}_{k-1}$, $\mathcal{B}_{k+1} = \mathcal{B}_k + A\mathcal{B}_k$. Hence

$$
\mathcal{B}_k = \operatorname{span}\{\boldsymbol{d}_0, A\boldsymbol{d}_0, \dots, A^{k-1}\boldsymbol{d}_0\} = \operatorname{span}\{\boldsymbol{r}_0, A\boldsymbol{r}_0, A^2\boldsymbol{r}_0, \dots, A^{k-1}\boldsymbol{r}_0\},
$$
and if $\boldsymbol{x}_0 = \boldsymbol{0}$, then $\boldsymbol{d}_0 = \boldsymbol{r}_0 = \boldsymbol{b}$ and $\mathcal{B}_k = \operatorname{span}\{\boldsymbol{b}, A\boldsymbol{b}, \dots, A^{k-1}\boldsymbol{b}\}$.

**Definition 5.3.2 (Krylov Subspace)** For a matrix $A$ and a vector $\boldsymbol{v}$, the subspace $\mathcal{K}_k(A, \boldsymbol{v}) = \operatorname{span}\{\boldsymbol{v}, A\boldsymbol{v}, \dots, A^{k-1}\boldsymbol{v}\}$, created by repeatedly applying the matrix to the vector, is a **Krylov subspace**.

This structure reduces the memory. Since $\boldsymbol{r}_{k+1} \perp \mathcal{B}_{k+1} = \mathcal{B}_k + A\mathcal{B}_k$, the vector $\boldsymbol{r}_{k+1}$ is $A$-orthogonal to $\mathcal{B}_k$, i.e. to all previous search directions except $\boldsymbol{d}_k$. Gram–Schmidt conjugation becomes easy: to build $\boldsymbol{d}_{k+1}$ from $\boldsymbol{r}_{k+1}$,

$$
\boldsymbol{d}_{k+1} = \boldsymbol{r}_{k+1} - \sum_{i=0}^k\frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{r}_{k+1}}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}\boldsymbol{d}_i = \boldsymbol{r}_{k+1} - \frac{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{r}_{k+1}}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k}\boldsymbol{d}_k.
$$
With $A\boldsymbol{d}_k = (\boldsymbol{r}_k - \boldsymbol{r}_{k+1})/\alpha_k$ and $\boldsymbol{r}_{k+1}^{\mathsf T}\boldsymbol{r}_k = 0$, $\boldsymbol{d}_k^{\mathsf T}\boldsymbol{r}_{k+1} = 0$,

$$
\frac{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{r}_{k+1}}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k} = \frac{(\boldsymbol{r}_k - \boldsymbol{r}_{k+1})^{\mathsf T}\boldsymbol{r}_{k+1}}{\boldsymbol{d}_k^{\mathsf T}(\boldsymbol{r}_k - \boldsymbol{r}_{k+1})} = -\frac{\boldsymbol{r}_{k+1}^{\mathsf T}\boldsymbol{r}_{k+1}}{\boldsymbol{d}_k^{\mathsf T}\boldsymbol{r}_k}.
$$
Moreover $\boldsymbol{d}_k^{\mathsf T}\boldsymbol{r}_k = \boldsymbol{r}_k^{\mathsf T}\boldsymbol{r}_k$, because $\boldsymbol{d}_k = \boldsymbol{r}_k + (\text{a multiple of }\boldsymbol{d}_{k-1})$ and $\boldsymbol{d}_{k-1}^{\mathsf T}\boldsymbol{r}_k = 0$; equivalently, $\nabla f(\boldsymbol{x}_k)^{\mathsf T}\boldsymbol{d}_k = -\lVert\nabla f(\boldsymbol{x}_k)\rVert^2$. Therefore

$$
\boldsymbol{d}_{k+1} = \boldsymbol{r}_{k+1} + \frac{\boldsymbol{r}_{k+1}^{\mathsf T}\boldsymbol{r}_{k+1}}{\boldsymbol{r}_k^{\mathsf T}\boldsymbol{r}_k}\boldsymbol{d}_k, \quad\text{i.e.}\quad \boldsymbol{d}_k = -\nabla f(\boldsymbol{x}_k) + \frac{\lVert\nabla f(\boldsymbol{x}_k)\rVert^2}{\lVert\nabla f(\boldsymbol{x}_{k-1})\rVert^2}\boldsymbol{d}_{k-1}. \tag{5.9}
$$
This is the conjugate gradient rule for updating the search direction.

**Algorithm 5.3.1 (Conjugate Gradient Method)** The conjugate gradient method (CG; M. Hestenes and E. Stiefel, 1952) for $A\boldsymbol{x} = \boldsymbol{b}$, $A \succ 0$: choose an initial guess $\boldsymbol{x}_0$ and set $\boldsymbol{d}_0 = \boldsymbol{r}_0 = \boldsymbol{b} - A\boldsymbol{x}_0$. For $k = 0, 1, \dots, n - 1$:

$$
\alpha_k = \frac{\boldsymbol{r}_k^{\mathsf T}\boldsymbol{r}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k}, \quad \boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k, \quad \boldsymbol{r}_{k+1} = \boldsymbol{r}_k - \alpha_kA\boldsymbol{d}_k, \quad \boldsymbol{d}_{k+1} = \boldsymbol{r}_{k+1} + \frac{\boldsymbol{r}_{k+1}^{\mathsf T}\boldsymbol{r}_{k+1}}{\boldsymbol{r}_k^{\mathsf T}\boldsymbol{r}_k}\boldsymbol{d}_k,
$$
stopping early if $\boldsymbol{r}_{k+1} = \boldsymbol{0}$; return $\boldsymbol{x}^* = \boldsymbol{x}_n$.

To compute $\boldsymbol{d}_k$ we only need to store two vectors ($\boldsymbol{d}_{k-1}$ and $\boldsymbol{x}_k$, with the residual) and one number ($\lVert\nabla f(\boldsymbol{x}_{k-1})\rVert^2$), overwriting them during the computation. The method terminates in at most $n$ iterations; in practice $\boldsymbol{x}_k$ approximates $\boldsymbol{x}^*$ closely quickly, and the remaining iterations are fine-tuning.

In theory CG takes $n$ iterations, each requiring a few inner products in $\mathbb{R}^n$ and one matrix–vector product $A\boldsymbol{d}_k$. If $A$ is dense, the product costs $n^2$, so the total cost is $n^3$, comparable to a factorization; the gain comes from sparse $A$ and from stopping early. With roundoff error CG can work poorly (or not at all) as a finite method, but for some $A$ (and $\boldsymbol{b}$) it gives a good approximate solution in $\ll n$ iterations.

**Theorem 5.3.4 (Convergence of CG)** The conjugate gradient iterates converge to $\boldsymbol{x}^* = A^{-1}\boldsymbol{b}$ with the error estimate

$$
\lVert\boldsymbol{e}_t\rVert_A \le 2\left(\frac{\sqrt{\kappa(A)} - 1}{\sqrt{\kappa(A)} + 1}\right)^t\lVert\boldsymbol{e}_0\rVert_A, \qquad \kappa(A) = \frac{\lambda_{\max}(A)}{\lambda_{\min}(A)}.
$$

Compare gradient descent with exact line search, for which Theorem 5.2.1 gives $\lVert\boldsymbol{e}_t\rVert_A \le \bigl(\frac{\kappa - 1}{\kappa + 1}\bigr)^t\lVert\boldsymbol{e}_0\rVert_A$: CG replaces $\kappa$ by $\sqrt\kappa$. The bound uses only the extreme eigenvalues; the actual convergence can be much faster when the spectrum of $A$ is clustered rather than spread out. If $A$ has only $m$ distinct eigenvalues, CG terminates after $m$ steps in exact arithmetic. The last panel of the figure in Section 5.2.2.3 shows CG solving a two-dimensional quadratic in two steps, where exact line search zig-zags.

#### 5.3.2.2. Nonquadratic Problems

To minimize a general $f$, use a quadratic approximation with $A = \nabla^2 f(\boldsymbol{x}_k)$: then $\boldsymbol{g}_k = \nabla f = A\boldsymbol{x} - \boldsymbol{b}$ locally, which is similar to Newton's method in that $f$ is approximated by a quadratic function (the exact value $\boldsymbol{b} = \nabla^2 f(\boldsymbol{x}_k)\boldsymbol{x}_k - \nabla f(\boldsymbol{x}_k)$ is not important). Applied to nonquadratic problems, CG methods will not usually terminate within $n$ steps; after $n$ steps we restart the process from the current point and run the algorithm for another $n$ steps, and so on.

The Gram–Schmidt coefficient $\beta_{ki} = \frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{v}_k}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}$ with the local Hessian leads to the method of Daniel (1967):

**Algorithm 5.3.2 (General Conjugate Gradient)** Choose $\boldsymbol{x}_0$ and a tolerance $\varepsilon$; set $\boldsymbol{d}_0 = -\nabla f(\boldsymbol{x}_0)$. While $\lVert\boldsymbol{d}_0\rVert > \varepsilon$: for $k = 0, 1, \dots, n - 1$,

$$
\alpha_k = -\frac{\nabla f(\boldsymbol{x}_k)^{\mathsf T}\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}\nabla^2 f(\boldsymbol{x}_k)\boldsymbol{d}_k}, \qquad \boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k,
$$
and, if $k < n - 1$, $\beta_k = \frac{\nabla f(\boldsymbol{x}_{k+1})^{\mathsf T}\nabla^2 f(\boldsymbol{x}_k)\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}\nabla^2 f(\boldsymbol{x}_k)\boldsymbol{d}_k}$ and $\boldsymbol{d}_{k+1} = -\nabla f(\boldsymbol{x}_{k+1}) + \beta_k\boldsymbol{d}_k$; then restart with $\boldsymbol{x}_0 = \boldsymbol{x}_n$, $\boldsymbol{d}_0 = -\nabla f(\boldsymbol{x}_0)$.

Like Newton's method, it requires no line search and converges in a finite number of steps for a quadratic problem. Its undesirable features are that the Hessian must be evaluated at each step and that it is generally not globally convergent. To avoid the Hessian, line search methods are used.

**Definition 5.3.3 (Fletcher–Reeves and Polak–Ribière Methods)** In Algorithm 5.3.2 replace $\alpha_k$ by a line search, $\alpha_k = \arg\min_\alpha f(\boldsymbol{x}_k + \alpha\boldsymbol{d}_k)$, and $\beta_k$ by a formula in the gradients $\boldsymbol{g}_k = \nabla f(\boldsymbol{x}_k)$ only. The **Fletcher–Reeves method** uses

$$
\beta_k = \frac{\lVert\nabla f(\boldsymbol{x}_{k+1})\rVert^2}{\lVert\nabla f(\boldsymbol{x}_k)\rVert^2} = \frac{\boldsymbol{g}_{k+1}^{\mathsf T}\boldsymbol{g}_{k+1}}{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{g}_k},
$$
and the **Polak–Ribière method** uses

$$
\beta_k = \frac{(\boldsymbol{g}_{k+1} - \boldsymbol{g}_k)^{\mathsf T}\boldsymbol{g}_{k+1}}{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{g}_k}.
$$

In the quadratic case both are identical to the original CG, since then $\boldsymbol{g}_{k+1}^{\mathsf T}\boldsymbol{g}_k = 0$. Experimental evidence seems to favor the Polak–Ribière method: when the iteration stalls and $\boldsymbol{g}_{k+1} \approx \boldsymbol{g}_k$, its $\beta_k$ is close to $0$ and the next direction is close to the steepest descent direction, an automatic restart.

The local convergence for general nonquadratic problems is $n$-step quadratic,

$$
\lVert\boldsymbol{x}_{k+n} - \boldsymbol{x}^*\rVert \le c\lVert\boldsymbol{x}_k - \boldsymbol{x}^*\rVert^2, \qquad k = 0, n, 2n, 3n, \dots,
$$
since one complete $n$-step cycle solves a quadratic problem, similarly to one step of Newton's method. Global convergence of the line search methods is established by noting that a pure steepest descent step is taken every $n$ steps and serves as a spacer step, while the other steps do not increase the objective. The restarting is thus important for the global convergence analysis, since in general one cannot guarantee that the directions $\boldsymbol{d}_k$ generated by the method are descent directions.

## 5.4. Comparison of the Three Classes of Methods

In contrast to gradient descent, conjugate gradient is only slightly more complicated to implement but converges in a finite number of steps on quadratic problems; in contrast to Newton's method, there is no need for matrix inversion. Newton's method uses curvature information to take a more direct route than gradient descent, at the price of second derivatives and linear solves.

| Method | Cost per step (beyond the gradient) | Memory | Convergence | Typical use |
|---|---|---|---|---|
| Newton | $O(n^3)$ (factorize the Hessian) | $O(n^2)$ | quadratic (local) | small, smooth problems |
| Quasi-Newton (BFGS) | $O(n^2)$ | $O(n^2)$ | superlinear | medium size |
| Gradient descent | $O(n)$ | $O(n)$ | linear (often slow) | large, convex problems |
| Conjugate gradient | one matrix–vector product, $O(n^2)$ if dense | $O(n)$ | at most $n$ steps on quadratics, rate in $\sqrt\kappa$ | large, sparse, positive definite systems |
| Stochastic gradient | $O(\lvert B\rvert n)$ per mini-batch | $O(n)$ | sublinear, noisy | very large data sets |

Quasi-Newton methods keep an $n\times n$ matrix in memory, $H^{(t)}$ (the inverse of the approximate Hessian $M^{(t)}$) or $L^{(t)}$ (the Cholesky factor of $M^{(t)}$), i.e. $O(n^2)$ numbers. Steepest descent occupies only $O(n)$ memory at any given time, storing $\boldsymbol{x}_k$ and $\nabla f(\boldsymbol{x}_k)$ and overwriting them, so it copes with much larger $n$. Conjugate gradient also has $O(n)$ memory requirement but converges much faster than steepest descent; it is used when the memory requirement of quasi-Newton methods exceeds the available memory, and to solve positive definite systems of linear equations.

For a linear system $A\boldsymbol{x} = \boldsymbol{b}$, $A \in \mathbb{R}^{n\times n}$, there are three classes of methods:

| | Dense direct (factor–solve) | Sparse direct (factor–solve) | Iterative |
|---|---|---|---|
| Runtime depends on | size only; independent of data, structure or sparsity | size and sparsity pattern; (almost) independent of data | data, size, sparsity, required accuracy |
| Works well for | $n$ up to a few thousand | $n$ up to $10^4$ or $10^5$ (or more) | the only choice for $n = 10^6$ or larger |
| Needs | nothing special | a good heuristic for the ordering | tuning, preconditioning |

The conjugate gradient method is both a direct and an iterative method, and no parameter has to be estimated. Hestenes and Stiefel published it in 1952 as a direct method that finds the exact solution in at most $n$ iterations. Only some 30 years later was its iterative nature seriously appreciated: the convergence analysis shows that $\lVert\boldsymbol{x}_k - \boldsymbol{x}^*\rVert_A$ typically becomes small quite rapidly, so the iteration can stop with $k$ much smaller than $n$. This rapid convergence, at a rate governed by the square root of the condition number, makes CG the method of choice for large, sparse linear systems.

## Summary

- Newton–Raphson: quadratic convergence; needs the gradient and the Hessian; sensitive to the starting value; may diverge when the Hessian is not definite. The secant method replaces the second derivative by a difference quotient and converges superlinearly with order $\approx 1.618$.
- Fisher scoring replaces the observed information by the expected information, which is positive definite; it is more stable and has a larger radius of convergence. For a canonical exponential family (canonical link) it coincides with Newton's method, and for GLMs it is iteratively reweighted least squares.
- Improvements of Newton's method: backtracking line search for the step length; discrete Newton (difference approximations of the Hessian); quasi-Newton updates satisfying the secant condition, Davidon (rank one), BFGS and DFP (rank two, dual to each other, positive definite under the curvature condition), with no Hessian and, in the inverse form, no linear solve. The three line searches are exact, backtracking and fixed step; trust-region methods choose the size of the region first and then the step.
- Nonlinear regression: Gauss–Newton approximates the Hessian through the Jacobian, needs no second derivatives, coincides with Fisher scoring under Gaussian errors, and converges fast when the residuals are small; Levenberg–Marquardt–Fletcher adds damping to interpolate between Gauss–Newton and gradient descent and is robust for ill-conditioned problems.
- Gradient descent: cheap steps, linear (or sublinear) convergence, zig-zagging, sensitivity to the condition number, no scale invariance. Newton's method is steepest descent in the Hessian norm. SGD and mini-batches reduce the cost on large data.
- Conjugate directions: for a quadratic with $A \succ 0$, $A$-conjugate directions give the solution in at most $n$ steps; the gradient is orthogonal to the explored subspace (expanding subspace theorem); Gram–Schmidt constructs conjugate directions, and with the unit vectors this is Gaussian elimination. Conjugate gradient builds the directions from the residuals, needs $O(n)$ storage, converges at a rate in $\sqrt\kappa$ and faster for clustered spectra, and extends to nonquadratic problems by the Fletcher–Reeves and Polak–Ribière methods.
