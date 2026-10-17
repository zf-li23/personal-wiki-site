---
title: Functions of Random Vectors, Order Statistics and Quantiles
source_hash: 48be28e18eea
---

[3.1.5](/3.1.5) dealt with the distribution of a function $g(X)$ of one random variable: in general one first finds the distribution function of $g(X)$ and then differentiates, and when $g$ is monotone or piecewise monotone the density of $g(X)$ can be written down directly from that of $X$. This chapter extends both routes to functions $g(X_1, \dots, X_n)$ of random vectors. The general method is still "find the distribution function first"; the most important special cases are the distribution of a sum (the convolution formula) and the joint density of several functions (the change-of-variables formula). As applications we derive the relations between the normal distribution and the three main distributions of statistics ($\chi^2$, $t$ and $F$), and study a special class of functions, the order statistics, which describe extremes such as the minimum and maximum of a sample. Finally we define the $p$-quantile of an arbitrary distribution function (its generalized inverse), which is both the source of critical values in statistical inference and a way to generate random numbers from any distribution using uniform ones. The chapter relies on the joint densities, marginal densities and independence criteria of [3.1.6](/3.1.6); the sampling distributions of statistical inference ([3.2](/3.2)) are built on it.

## 7.1. Distributions of Functions of Random Vectors

Let the distribution of $\boldsymbol{X} = (X_1, \dots, X_n)$ be known and let $Z = g(\boldsymbol{X})$. There are two ways to describe $Z$:

1. The general method: compute $F_Z(z) = \mathbb{P}(g(\boldsymbol{X}) \le z)$ from the joint distribution of $\boldsymbol{X}$, that is, the probability that $\boldsymbol{X}$ falls in the region $\{\boldsymbol{x} \mid g(\boldsymbol{x}) \le z\}$, and then differentiate to get a density or take differences to get a mass function, as needed.
2. Special cases: for sums, differences, quotients and invertible transformations there are formulas that pass directly from density to density.

Often both methods apply to the same problem, and we simply choose the one that is easier to compute.

### 7.1.1. The General Method: Distribution Function First

**Example 7.1.1** Let $(X, Y)$ be uniformly distributed on the unit square $(0, 1)^2$ (by Corollary 6.3.1, $X$ and $Y$ are then independent and both $\mathrm{U}(0, 1)$). Find the density of $Z = Y/X$.

**Solution** $\mathbb{P}(Z \le z)$ is the area of the part of the square below the line $y = zx$. For $0 \le z \le 1$ this part is the triangle with vertices $(0, 0)$, $(1, 0)$, $(1, z)$; for $z > 1$ it is the square minus the triangle with vertices $(0, 0)$, $(0, 1)$, $(1/z, 1)$. Hence

$$
F_Z(z) = \begin{cases} 0, & z < 0, \\ z/2, & 0 \le z \le 1, \\ 1 - \dfrac{1}{2z}, & z > 1, \end{cases} \qquad f_Z(z) = \begin{cases} 1/2, & 0 < z \le 1, \\ \dfrac{1}{2z^2}, & z > 1, \\ 0, & z \le 0. \end{cases}
$$

**Example 7.1.2** Let $X, Y$ be independent, both $\mathcal{N}(0, 1)$. Find the distribution of $Z = \sqrt{X^2 + Y^2}$.

**Solution** The joint density of $(X, Y)$ is $f(x, y) = \frac{1}{2\pi}\exp\big(-\frac{x^2 + y^2}{2}\big)$. For $z \ge 0$, using polar coordinates $x = r\cos\theta$, $y = r\sin\theta$,

$$
F_Z(z) = \int_{\{x^2 + y^2 \le z^2\}} \frac{1}{2\pi} \exp\Big( -\frac{x^2 + y^2}{2} \Big) \mathrm{d}x\,\mathrm{d}y = \frac{1}{2\pi} \int_0^{2\pi} \mathrm{d}\theta \int_0^z r\mathrm{e}^{-r^2/2}\,\mathrm{d}r = \int_0^z r\mathrm{e}^{-r^2/2}\,\mathrm{d}r.
$$
Differentiating gives $f_Z(z) = z\mathrm{e}^{-z^2/2}$ for $z \ge 0$, so $Z$ has the Rayleigh distribution. When shooting at the origin $(0, 0)$, the point of impact $(X, Y)$ is often modeled by a bivariate normal distribution, and $Z$ is then the distance from the point of impact to the target (the miss distance).

### 7.1.2. Distributions of Sums and Differences

**Theorem 7.1.1** If $(X, Y)$ is a discrete random vector, then $Z = X + Y$ has mass function

$$
\mathbb{P}(Z = z) = \sum_x \mathbb{P}(X = x, Y = z - x).
$$
In particular, if $X, Y$ are independent,

$$
\mathbb{P}(Z = z) = \sum_x \mathbb{P}(X = x)\,\mathbb{P}(Y = z - x),
$$
that is, the mass function of $Z$ is the discrete **convolution** of the mass functions of $X$ and $Y$.

For example, if $X \sim \mathrm{Bin}(n, p)$ and $Y \sim \mathrm{Bin}(m, p)$ are independent, Vandermonde's identity $\sum_k \binom{n}{k}\binom{m}{z - k} = \binom{n + m}{z}$ gives $X + Y \sim \mathrm{Bin}(n + m, p)$ (which can also be seen directly as the number of successes in $n + m$ independent trials); similarly, if $X \sim \mathrm{Poi}(\lambda)$ and $Y \sim \mathrm{Poi}(\mu)$ are independent, the binomial theorem gives $X + Y \sim \mathrm{Poi}(\lambda + \mu)$.

**Theorem 7.1.2 (Convolution Formula)** If $(X, Y)$ has joint density $f(x, y)$, then $Z = X + Y$ has density

$$
f_Z(z) = \int_{-\infty}^{\infty} f(x, z - x)\,\mathrm{d}x = \int_{-\infty}^{\infty} f(z - y, y)\,\mathrm{d}y.
$$
In particular, if $X, Y$ are independent,

$$
f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z - x)\,\mathrm{d}x =: (f_X * f_Y)(z).
$$

**Proof** For any $a < b$, by Fubini's theorem and the substitution $y = z - x$ in the inner integral,

$$
\mathbb{P}(a < Z \le b) = \int_{\mathbb{R}^2} \boldsymbol{1}\{a < x + y \le b\} f(x, y)\,\mathrm{d}x\,\mathrm{d}y = \int_{\mathbb{R}} \int_{a - x}^{b - x} f(x, y)\,\mathrm{d}y\,\mathrm{d}x = \int_{\mathbb{R}} \int_a^b f(x, z - x)\,\mathrm{d}z\,\mathrm{d}x = \int_a^b \int_{\mathbb{R}} f(x, z - x)\,\mathrm{d}x\,\mathrm{d}z,
$$
so $\int_{\mathbb{R}} f(x, z - x)\,\mathrm{d}x$ is a density of $Z$. Exchanging the roles of $x$ and $y$ gives the second form. $\square$

**Theorem 7.1.3** If $(X, Y)$ has joint density $f(x, y)$, then $V = X - Y$ has density

$$
f_V(v) = \int_{-\infty}^{\infty} f(x, x - v)\,\mathrm{d}x;
$$
if $X, Y$ are independent, $f_V(v) = \int_{-\infty}^{\infty} f_X(x) f_Y(x - v)\,\mathrm{d}x$.

It suffices to write $V = X + (-Y)$ and apply the convolution formula to the joint density $f(x, -y)$ of $(X, -Y)$. This technique of reducing a problem to a known result (subtraction to addition, multiplication to division) is common when finding distributions of functions.

**Example 7.1.3** Let $X, Y$ be independent, both $\mathrm{U}(0, 1)$. Find the density of $Z = X + Y$.

**Solution** $Z$ takes values in $(0, 2)$, and $f_X(x) = f_Y(x) = \boldsymbol{1}\{0 < x < 1\}$. By the convolution formula, with $t = z - x$,

$$
f_Z(z) = \int_{-\infty}^{\infty} \boldsymbol{1}\{0 < x < 1\}\boldsymbol{1}\{0 < z - x < 1\}\,\mathrm{d}x = \int_{z-1}^{z} \boldsymbol{1}\{0 < t < 1\}\,\mathrm{d}t = \begin{cases} z, & 0 < z \le 1, \\ 2 - z, & 1 < z < 2, \\ 0, & \text{otherwise}, \end{cases}
$$
the triangular distribution. The sum of two uniform variables is no longer uniform: values in the middle can be obtained in more ways.

**Example 7.1.4** Let $X_1, X_2, \dots, X_n$ be independent and identically distributed, all $\mathrm{U}(-1, 1)$, and let $S_n = X_1 + \cdots + X_n$. Repeated use of the convolution formula gives

$$
f_{S_2}(x) = \begin{cases} \dfrac{2 - \lvert x \rvert}{4}, & \lvert x \rvert \le 2, \\ 0, & \lvert x \rvert > 2, \end{cases} \qquad f_{S_3}(x) = \begin{cases} \dfrac{3 - x^2}{8}, & \lvert x \rvert \le 1, \\ \dfrac{(3 - \lvert x \rvert)^2}{16}, & 1 \le \lvert x \rvert \le 3, \\ 0, & \lvert x \rvert > 3, \end{cases}
$$
and in general (by induction on $n$)

$$
f_{S_n}(x) = \begin{cases} \dfrac{1}{2^n (n - 1)!} \displaystyle\sum_{k=0}^{\lfloor (n + x)/2 \rfloor} (-1)^k \binom{n}{k} (n + x - 2k)^{n-1}, & \lvert x \rvert \le n, \\ 0, & \lvert x \rvert > n. \end{cases}
$$
$f_{S_2}$ is piecewise linear, $f_{S_3}$ already consists of three parabolic pieces joined smoothly, and as $n$ grows $f_{S_n}$ rapidly approaches the normal density $\mathcal{N}(0, n/3)$ (where $n/3$ is the variance of $S_n$, see [3.1.8](/3.1.8)). This is an intuitive manifestation of the **central limit theorem** ([3.1.13](/3.1.13)): the superposition of many small independent quantities is approximately normally distributed.

![Exact densities of the independent sums S_n of U(-1,1) variables (solid) and the normal approximations N(0, n/3) (dashed)](./plots/uniform-sums.py)

**Example 7.1.5** If $X \sim \Gamma(\alpha_1, \lambda)$ and $Y \sim \Gamma(\alpha_2, \lambda)$ are independent, then $X + Y \sim \Gamma(\alpha_1 + \alpha_2, \lambda)$.

**Proof** For $z > 0$, by the convolution formula and the substitution $x = zt$,

$$
f_{X+Y}(z) = \int_0^z \frac{\lambda^{\alpha_1}}{\Gamma(\alpha_1)} x^{\alpha_1 - 1}\mathrm{e}^{-\lambda x} \cdot \frac{\lambda^{\alpha_2}}{\Gamma(\alpha_2)} (z - x)^{\alpha_2 - 1}\mathrm{e}^{-\lambda(z - x)}\,\mathrm{d}x = \frac{\lambda^{\alpha_1 + \alpha_2}}{\Gamma(\alpha_1)\Gamma(\alpha_2)} z^{\alpha_1 + \alpha_2 - 1}\mathrm{e}^{-\lambda z} \int_0^1 t^{\alpha_1 - 1}(1 - t)^{\alpha_2 - 1}\,\mathrm{d}t.
$$
The last integral is the **beta function** $\mathrm{B}(\alpha_1, \alpha_2) = \frac{\Gamma(\alpha_1)\Gamma(\alpha_2)}{\Gamma(\alpha_1 + \alpha_2)}$, and substituting it gives the density of $\Gamma(\alpha_1 + \alpha_2, \lambda)$. $\square$

In particular, the sum of $n$ independent $\mathrm{Exp}(\lambda) = \Gamma(1, \lambda)$ variables has distribution $\Gamma(n, \lambda)$.

**Example 7.1.6** If $(X, Y)$ has joint density $f(x, y)$, then $Z = X/Y$ has density $f_Z(z) = \int_{-\infty}^{\infty} \lvert y \rvert f(zy, y)\,\mathrm{d}y$. In particular, if $X, Y$ are independent and both $\mathcal{N}(0, 1)$, then $Z$ has the Cauchy distribution.

**Solution** We have $\mathbb{P}(Y = 0) = 0$. Splitting according to the sign of $Y$ (law of total probability),

$$
F_Z(z) = \mathbb{P}(X \le zY, Y > 0) + \mathbb{P}(X \ge zY, Y < 0) = \int_0^{\infty} \int_{-\infty}^{zy} f(x, y)\,\mathrm{d}x\,\mathrm{d}y + \int_{-\infty}^{0} \int_{zy}^{\infty} f(x, y)\,\mathrm{d}x\,\mathrm{d}y.
$$
Differentiating in $z$ gives $f_Z(z) = \int_0^{\infty} y f(zy, y)\,\mathrm{d}y - \int_{-\infty}^0 y f(zy, y)\,\mathrm{d}y = \int_{\mathbb{R}} \lvert y \rvert f(zy, y)\,\mathrm{d}y$. Inserting the standard normal density,

$$
f_Z(z) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \lvert y \rvert \mathrm{e}^{-(1 + z^2)y^2/2}\,\mathrm{d}y = \frac{1}{\pi} \int_0^{\infty} y\mathrm{e}^{-(1 + z^2)y^2/2}\,\mathrm{d}y = \frac{1}{\pi(1 + z^2)}, \quad z \in \mathbb{R}.
$$

### 7.1.3. Joint Densities of Several Functions

Let $\boldsymbol{X} = (X_1, \dots, X_n)$ have joint density $f(\boldsymbol{x})$ and let $Y_1 = g_1(\boldsymbol{X}), \dots, Y_n = g_n(\boldsymbol{X})$ be $n$ functions; we want the joint density of $\boldsymbol{Y} = (Y_1, \dots, Y_n)$. Recall the one-dimensional result ([3.1.5](/3.1.5)): if $\mathbb{P}(Y \in D) = 1$, $\{Y = y\} = \bigcup_{i=1}^n \{X = h_i(y)\}$ for $y \in D$, each $h_i$ is an invertible, continuously differentiable map from $D$ onto its range $D_i$, and $D_1, \dots, D_n$ are pairwise disjoint, then $f_Y(y) = \sum_{i=1}^n f(h_i(y))\lvert h_i'(y) \rvert$ for $y \in D$. The two-dimensional case is entirely analogous, with the derivative replaced by the **Jacobian determinant**.

**Theorem 7.1.4** Let $(X, Y)$ have joint density $f(x, y)$, let $U = u(X, Y)$, $V = v(X, Y)$, and let $D$ be a region in the plane with $\mathbb{P}((U, V) \in D) = 1$. Suppose there are functions $x_i = x_i(u, v)$, $y_i = y_i(u, v)$ ($i = 1, \dots, n$) on $D$ such that

1. $\{U = u, V = v\} = \bigcup_{i=1}^n \{X = x_i(u, v), Y = y_i(u, v)\}$ for $(u, v) \in D$;
2. $\Delta_i\colon (u, v) \mapsto (x_i(u, v), y_i(u, v))$ is an invertible map from $D$ onto its range $D_i$ with continuous partial derivatives, and its Jacobian determinant $J_i(u, v) = \dfrac{\partial(x_i, y_i)}{\partial(u, v)} \ne 0$ for $(u, v) \in D$;
3. $D_1, \dots, D_n$ are pairwise disjoint.

Then $(U, V)$ has joint density

$$
g(u, v) = \begin{cases} \displaystyle\sum_{i=1}^n f\big(x_i(u, v), y_i(u, v)\big) \lvert J_i(u, v) \rvert, & (u, v) \in D, \\ 0, & (u, v) \notin D. \end{cases}
$$

Here

$$
\frac{\partial(x, y)}{\partial(u, v)} = \det\begin{bmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[2mm] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{bmatrix}.
$$
Whether the matrix has $x, y$ along the rows and $u, v$ along the columns (numerator layout) or is transposed (denominator layout), the determinant is the same, so the formula does not depend on the layout convention. In computations, when it is easier to solve for $(u, v)$ in terms of $(x, y)$, one can use $\dfrac{\partial(x, y)}{\partial(u, v)} = \Big(\dfrac{\partial(u, v)}{\partial(x, y)}\Big)^{-1}$. The theorem extends directly to $n$ dimensions. The proof is the change of variables in multiple integrals: for a region $B$ in $D$, $\mathbb{P}((U, V) \in B) = \sum_i \mathbb{P}((X, Y) \in \Delta_i(B)) = \sum_i \int_{\Delta_i(B)} f\,\mathrm{d}x\,\mathrm{d}y = \int_B \sum_i f(x_i, y_i)\lvert J_i \rvert\,\mathrm{d}u\,\mathrm{d}v$.

**Example 7.1.7** Let $X, Y$ be independent, both $\mathcal{N}(0, 1)$, and let $(R, \Theta)$ be given by the polar transformation $X = R\cos\Theta$, $Y = R\sin\Theta$. Find the joint density of $(R, \Theta)$.

**Solution** Let $D = \{(r, \theta) \mid r > 0, \theta \in [0, 2\pi)\}$; then $\mathbb{P}((R, \Theta) \in D) = 1$. The map $x = r\cos\theta$, $y = r\sin\theta$ is an invertible transformation of $D$ onto $D_1 = \mathbb{R}^2 \setminus \{(0, 0)\}$, $\{R = r, \Theta = \theta\} = \{X = x, Y = y\}$, and $\frac{\partial(x, y)}{\partial(r, \theta)} = r > 0$. By Theorem 7.1.4,

$$
g(r, \theta) = f(r\cos\theta, r\sin\theta) \cdot r = \frac{1}{2\pi} \cdot r\mathrm{e}^{-r^2/2}, \quad (r, \theta) \in D.
$$
By Corollary 6.3.1, $R$ and $\Theta$ are independent with densities $g_R(r) = r\mathrm{e}^{-r^2/2}$ ($r > 0$) and $g_\Theta(\theta) = \frac{1}{2\pi}\boldsymbol{1}_{[0, 2\pi)}(\theta)$: $R$ has the Rayleigh distribution (in agreement with Example 7.1.2) and $\Theta \sim \mathrm{U}(0, 2\pi)$.

**Theorem 7.1.5** If the $n$-dimensional random vectors $\boldsymbol{X}$ and $\boldsymbol{Y}$ have the same distribution and $\boldsymbol{g}\colon \mathbb{R}^n \to \mathbb{R}^m$ is measurable, then $\boldsymbol{g}(\boldsymbol{X})$ and $\boldsymbol{g}(\boldsymbol{Y})$ have the same distribution.

Indeed, $\mathbb{P}(\boldsymbol{g}(\boldsymbol{X}) \in B) = \mathbb{P}(\boldsymbol{X} \in \boldsymbol{g}^{-1}(B)) = \mathbb{P}(\boldsymbol{Y} \in \boldsymbol{g}^{-1}(B)) = \mathbb{P}(\boldsymbol{g}(\boldsymbol{Y}) \in B)$.

**Example 7.1.8 (Box–Muller Method)** Let $U, V$ be independent, both $\mathrm{U}(0, 1)$, and put

$$
X = \sqrt{-2\ln U}\cos(2\pi V), \qquad Y = \sqrt{-2\ln U}\sin(2\pi V).
$$
Then $X, Y$ are independent and both $\mathcal{N}(0, 1)$.

**Proof** $R' = \sqrt{-2\ln U}$ satisfies $\mathbb{P}(R' > r) = \mathbb{P}(U < \mathrm{e}^{-r^2/2}) = \mathrm{e}^{-r^2/2}$, so it has the Rayleigh distribution; $\Theta' = 2\pi V \sim \mathrm{U}(0, 2\pi)$, and $R'$ and $\Theta'$ are independent. By Example 7.1.7, $(R', \Theta')$ has the same distribution as $(R, \Theta)$, so by Theorem 7.1.5, $(R'\cos\Theta', R'\sin\Theta')$ has the same distribution as $(R\cos\Theta, R\sin\Theta) = (X_0, Y_0)$, a pair of independent standard normal variables. $\square$

This gives a way to generate normal random numbers from uniform ones.

**Example 7.1.9** Let $X, Y$ be independent, both $\mathcal{N}(0, 1)$. Find the joint density of $U = X/Y$ and $V = X^2 + Y^2$.

**Solution** Let $D = \{(u, v) \mid u \in \mathbb{R}, v > 0\}$. Solving $u = x/y$, $v = x^2 + y^2$ gives two inverse branches $y = \pm\sqrt{v/(1 + u^2)}$, $x = uy$, which map $D$ onto the upper and lower half-planes respectively. Both Jacobian determinants have absolute value $\frac{1}{2(1 + u^2)}$ (the reciprocal of $\frac{\partial(u, v)}{\partial(x, y)} = -\frac{2(x^2 + y^2)}{y^2} = -2(1 + u^2)$), and $f(x, y) = \frac{1}{2\pi}\mathrm{e}^{-v/2}$ takes the same value on both branches. By Theorem 7.1.4,

$$
g(u, v) = 2 \cdot \frac{1}{2\pi}\mathrm{e}^{-v/2} \cdot \frac{1}{2(1 + u^2)} = \frac{1}{\pi(1 + u^2)} \cdot \frac{1}{2}\mathrm{e}^{-v/2}, \quad u \in \mathbb{R},\ v > 0.
$$
Hence $U$ and $V$ are independent, $U$ has the Cauchy distribution (in agreement with Example 7.1.6), and $V \sim \mathrm{Exp}(1/2)$.

### 7.1.4. The Three Main Distributions of Statistics

The three distributions used most often in statistical inference are all built from independent normal random variables. Their densities were given in [3.1.4](/3.1.4); here we restate the definitions and use the methods of this chapter to derive their relation to the normal distribution.

**Definition 7.1.1 (Chi-Square Distribution)** Let $\nu > 0$. If $X$ has density

$$
f(x) = \frac{1}{2^{\nu/2}\Gamma(\nu/2)} x^{\nu/2 - 1}\mathrm{e}^{-x/2}, \quad x > 0,
$$
then $X$ is said to have the **chi-square distribution** with $\nu$ degrees of freedom, written $X \sim \chi^2_\nu$.

Comparison with the gamma density shows that $\chi^2_\nu = \Gamma(\nu/2, 1/2)$; in particular $\chi^2_2 = \mathrm{Exp}(1/2)$.

**Theorem 7.1.6** If $Z_1, \dots, Z_n \overset{\text{iid}}{\sim} \mathcal{N}(0, 1)$, then $Z_1^2 + \cdots + Z_n^2 \sim \chi^2_n$. More generally, if $X \sim \chi^2_m$ and $Y \sim \chi^2_n$ are independent, then $X + Y \sim \chi^2_{m+n}$.

**Proof** First find the distribution of $Z_1^2$. For $y > 0$, $\mathbb{P}(Z_1^2 \le y) = \Phi(\sqrt{y}) - \Phi(-\sqrt{y})$, and differentiation gives

$$
f_{Z_1^2}(y) = \frac{1}{\sqrt{y}}\varphi(\sqrt{y}) = \frac{1}{\sqrt{2\pi}} y^{-1/2}\mathrm{e}^{-y/2},
$$
which is exactly the density of $\chi^2_1 = \Gamma(1/2, 1/2)$ (since $\Gamma(1/2) = \sqrt{\pi}$). The variables $Z_1^2, \dots, Z_n^2$ are independent, so by the additivity in Example 7.1.5 their sum has distribution $\Gamma(n/2, 1/2) = \chi^2_n$. The second statement also follows from Example 7.1.5. $\square$

The $\chi^2$ distribution was introduced by Karl Pearson in his work on goodness-of-fit tests (the $\chi^2$ test).

**Definition 7.1.2 (t-Distribution)** Let $\nu > 0$. If $X$ has density

$$
f(x) = \frac{\Gamma\big(\frac{\nu + 1}{2}\big)}{\sqrt{\nu\pi}\,\Gamma\big(\frac{\nu}{2}\big)} \Big(1 + \frac{x^2}{\nu}\Big)^{-\frac{\nu + 1}{2}}, \quad x \in \mathbb{R},
$$
then $X$ is said to have Student's **t-distribution** with $\nu$ degrees of freedom, written $X \sim t_\nu$.

**Theorem 7.1.7** If $Z \sim \mathcal{N}(0, 1)$ and $X \sim \chi^2_n$ are independent, then $T = \dfrac{Z}{\sqrt{X/n}} \sim t_n$.

**Proof** Apply Theorem 7.1.4 to the transformation $t = z/\sqrt{x/n}$, $w = x$ ($x > 0$); the inverse transformation $z = t\sqrt{w/n}$, $x = w$ has Jacobian determinant $\sqrt{w/n}$. The joint density of $(T, W)$ is

$$
g(t, w) = \frac{1}{\sqrt{2\pi}}\mathrm{e}^{-t^2 w/(2n)} \cdot \frac{w^{n/2 - 1}\mathrm{e}^{-w/2}}{2^{n/2}\Gamma(n/2)} \cdot \sqrt{\frac{w}{n}}, \quad w > 0.
$$
Integrate over $w$; as a function of $w$ the integrand is the kernel of the $\Gamma\big(\frac{n + 1}{2}, \frac{1}{2}(1 + \frac{t^2}{n})\big)$ density, so

$$
f_T(t) = \frac{1}{\sqrt{2\pi n}\,2^{n/2}\Gamma(n/2)} \int_0^{\infty} w^{\frac{n+1}{2} - 1}\mathrm{e}^{-\frac{w}{2}(1 + t^2/n)}\,\mathrm{d}w = \frac{\Gamma\big(\frac{n + 1}{2}\big)}{\sqrt{n\pi}\,\Gamma\big(\frac{n}{2}\big)}\Big(1 + \frac{t^2}{n}\Big)^{-\frac{n + 1}{2}}. \qquad \square
$$

The $t$-distribution was introduced by W. S. Gosset under the pseudonym Student. It is symmetric about $0$ ($T \sim t_\nu$ implies $-T \sim t_\nu$), and its tails decay like a power, so it is heavier-tailed than the normal distribution; for large $\nu$, $t_\nu$ is close to the standard normal distribution (proved later with the law of large numbers, [3.1.12](/3.1.12)); for $\nu = 1$, $t_1$ is the Cauchy distribution (Example 7.1.6).

**Definition 7.1.3 (F-Distribution)** Let $m, n$ be positive integers. If $X$ has density

$$
f(x) = \frac{\Gamma\big(\frac{m + n}{2}\big) m^{m/2} n^{n/2}}{\Gamma\big(\frac{m}{2}\big)\Gamma\big(\frac{n}{2}\big)} \cdot \frac{x^{m/2 - 1}}{(mx + n)^{(m + n)/2}}, \quad x > 0,
$$
then $X$ is said to have the **F-distribution** with $(m, n)$ degrees of freedom, written $X \sim F_{m,n}$.

**Theorem 7.1.8** If $X \sim \chi^2_m$ and $Y \sim \chi^2_n$ are independent, then $F = \dfrac{X/m}{Y/n} \sim F_{m,n}$. In particular, if $X_1, \dots, X_m, Y_1, \dots, Y_n \overset{\text{iid}}{\sim} \mathcal{N}(0, 1)$, then $\dfrac{\frac{1}{m}\sum_i X_i^2}{\frac{1}{n}\sum_j Y_j^2} \sim F_{m,n}$.

The proof is the same as for Theorem 7.1.7: apply Theorem 7.1.4 to $(F, W) = \big(\frac{X/m}{Y/n}, Y\big)$ and integrate over $W$. The definition also shows that $1/F \sim F_{n,m}$ when $F \sim F_{m,n}$, and $T^2 \sim F_{1,n}$ when $T \sim t_n$. The $F$-distribution was introduced by R. A. Fisher (1924) and plays an important role in the analysis of variance and in linear regression. The expectations and variances of the three distributions are computed in [3.1.8](/3.1.8), and their role in sampling from normal populations is discussed in [3.2.2](/3.2.2) of statistical inference.

## 7.2. Order Statistics

### 7.2.1. Definition

**Definition 7.2.1 (Order Statistics)** Let $X_1, X_2, \dots, X_n$ be random variables on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$. For each $\omega \in \Omega$, arrange $X_1(\omega), \dots, X_n(\omega)$ in increasing order as

$$
X_{(1)}(\omega) \le X_{(2)}(\omega) \le \cdots \le X_{(n)}(\omega).
$$
Then $X_{(1)}, X_{(2)}, \dots, X_{(n)}$ are called the **order statistics** of $X_1, \dots, X_n$. In particular $X_{(1)} = \min\{X_1, \dots, X_n\}$ and $X_{(n)} = \max\{X_1, \dots, X_n\}$.

**Example 7.2.1** A province has three 100-meter sprinters, and $X_i$ is the time (in seconds) of the $i$-th sprinter. Let the sample space be $\Omega = \{\omega_1, \omega_2, \omega_3\}$, where $\omega_k$ stands for the $k$-th training session; $X_{(i)}$ is the time of the sprinter ranked $i$-th:

| Session | $X_1$ | $X_2$ | $X_3$ | $X_{(1)}$ | $X_{(2)}$ | $X_{(3)}$ |
|---|---|---|---|---|---|---|
| $\omega_1$ | 11.3 | 11.6 | 11.0 | 11.0 | 11.3 | 11.6 |
| $\omega_2$ | 11.0 | 11.5 | 11.8 | 11.0 | 11.5 | 11.8 |
| $\omega_3$ | 12.0 | 11.9 | 12.2 | 11.9 | 12.0 | 12.2 |

Note that $X_{(1)}$ may come from different sprinters for different $\omega$: the order statistics are functions of $(X_1, \dots, X_n)$, but none of them is a fixed component.

### 7.2.2. Distributions of Order Statistics

From now on let $X_1, \dots, X_n$ be independent and identically distributed with common distribution function $F(x)$ and density $f(x)$. Then $\mathbb{P}(X_i = X_j) = 0$ for $i \ne j$, so the order statistics are almost surely strictly increasing.

**Property 7.2.1** $(X_{(1)}, \dots, X_{(n)})$ has joint density

$$
g(x_1, \dots, x_n) = \begin{cases} n!\displaystyle\prod_{i=1}^n f(x_i), & x_1 < x_2 < \cdots < x_n, \\ 0, & \text{otherwise}. \end{cases}
$$

**Proof** For each permutation $\sigma$ of $\{1, \dots, n\}$ let $A_\sigma = \{X_{\sigma(1)} < X_{\sigma(2)} < \cdots < X_{\sigma(n)}\}$; these $n!$ events are pairwise disjoint and their union has probability $1$. On $A_\sigma$, $(X_{(1)}, \dots, X_{(n)}) = (X_{\sigma(1)}, \dots, X_{\sigma(n)})$. For $B \subset \{x_1 < \cdots < x_n\}$,

$$
\mathbb{P}((X_{(1)}, \dots, X_{(n)}) \in B) = \sum_\sigma \mathbb{P}((X_{\sigma(1)}, \dots, X_{\sigma(n)}) \in B) = n! \int_B \prod_{i=1}^n f(x_i)\,\mathrm{d}\boldsymbol{x},
$$
because $(X_{\sigma(1)}, \dots, X_{\sigma(n)})$ has the same joint density $\prod f(x_i)$ as $(X_1, \dots, X_n)$. $\square$

To obtain marginal densities by integrating the joint density, we need the following integral formula.

**Property 7.2.2** For $-\infty \le a < b \le \infty$,

$$
\int_{a < x_1 < \cdots < x_k < b} f(x_1) \cdots f(x_k)\,\mathrm{d}x_1 \cdots \mathrm{d}x_k = \frac{(F(b) - F(a))^k}{k!}.
$$

**Proof** Induction on $k$. The case $k = 1$ holds. Assume the formula for $k - 1$; by Fubini's theorem,

$$
\int_{a < x_1 < \cdots < x_k < b} \prod_{i=1}^k f(x_i)\,\mathrm{d}\boldsymbol{x} = \int_a^b \Big( \int_{a < x_1 < \cdots < x_{k-1} < x_k} \prod_{i=1}^{k-1} f(x_i)\,\mathrm{d}x_1 \cdots \mathrm{d}x_{k-1} \Big) f(x_k)\,\mathrm{d}x_k = \int_a^b \frac{(F(x_k) - F(a))^{k-1}}{(k - 1)!} f(x_k)\,\mathrm{d}x_k = \frac{(F(b) - F(a))^k}{k!}. \qquad \square
$$

The formula can also be understood by symmetry: the probability that $k$ independent identically distributed points all fall in $(a, b)$ is $(F(b) - F(a))^k$, and the arrangements in one fixed order account for $1/k!$ of it.

**Property 7.2.3** $X_{(k)}$ has density

$$
g_k(x) = n\binom{n - 1}{k - 1} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x).
$$

**Proof** Integrate the joint density $g$ over all variables except $x_k$, applying Property 7.2.2 on each side (on the left with $a = -\infty$, $b = c$; on the right with $a = c$, $b = \infty$):

$$
g_k(c) = n! f(c) \int_{x_1 < \cdots < x_{k-1} < c} \prod_{i<k} f(x_i)\,\mathrm{d}x_1 \cdots \mathrm{d}x_{k-1} \cdot \int_{c < x_{k+1} < \cdots < x_n} \prod_{i>k} f(x_i)\,\mathrm{d}x_{k+1} \cdots \mathrm{d}x_n = n! f(c) \frac{F(c)^{k-1}}{(k - 1)!} \cdot \frac{(1 - F(c))^{n-k}}{(n - k)!},
$$
and $\frac{n!}{(k-1)!(n-k)!} = n\binom{n-1}{k-1}$. $\square$

The formula can also be understood infinitesimally: $X_{(k)} \in (x, x + \Delta x]$ is approximately the event that, of the $n$ points, exactly $k - 1$ fall to the left of $x$, one falls in $(x, x + \Delta x]$, and $n - k$ fall to the right (the probability that two or more points fall in the same small interval is $o(\Delta x)$ and can be neglected). By the multinomial distribution its probability is approximately $\frac{n!}{(k-1)!\,1!\,(n-k)!} F(x)^{k-1} \cdot f(x)\Delta x \cdot (1 - F(x))^{n-k}$.

For $k = 1$ and $k = n$ we obtain the densities of the minimum and the maximum, $g_1(x) = n[1 - F(x)]^{n-1} f(x)$ and $g_n(x) = n[F(x)]^{n-1} f(x)$. These can also be found directly from distribution functions, without assuming a density:

$$
\mathbb{P}(X_{(n)} \le x) = \mathbb{P}(X_1 \le x, \dots, X_n \le x) = F(x)^n, \qquad \mathbb{P}(X_{(1)} > x) = [1 - F(x)]^n.
$$

**Property 7.2.4** For $k_1 < k_2$, $(X_{(k_1)}, X_{(k_2)})$ has joint density

$$
g(x, y) = \frac{n!}{(k_1 - 1)!\,(k_2 - k_1 - 1)!\,(n - k_2)!} F(x)^{k_1 - 1}[F(y) - F(x)]^{k_2 - k_1 - 1}[1 - F(y)]^{n - k_2} f(x) f(y)
$$
for $x < y$, and $0$ elsewhere.

The proof is the same as for Property 7.2.3: apply Property 7.2.2 to the joint density on the three ranges to the left of $x$, between $x$ and $y$, and to the right of $y$. Infinitesimally, the real line is divided into five pieces containing $k_1 - 1$, $1$, $k_2 - k_1 - 1$, $1$ and $n - k_2$ points respectively.

**Property 7.2.5** The joint distribution function of $(X_{(1)}, \dots, X_{(n)})$ is continuous.

**Proof** By Example 6.3.4 it suffices to show that the distribution function of each $X_{(k)}$ is continuous, that is, $\mathbb{P}(X_{(k)} = x) = 0$. The event $\{X_{(k)} = x\}$ requires at least one $X_j$ to equal $x$, and $\mathbb{P}(X_j = x) = 0$, so $\mathbb{P}(X_{(k)} = x) \le \sum_j \mathbb{P}(X_j = x) = 0$. $\square$

**Example 7.2.2** Each classroom in a building used to have 4 light bulbs; after renovation each has 24. The caretaker feels that bulbs now burn out more easily. Explain why.

**Solution** Assume that the lifetimes of all bulbs are independent, each $\mathrm{Exp}(\lambda)$. Before the renovation the waiting time until the first bulb in a room fails is $X = \min\{X_1, \dots, X_4\}$; afterwards it is $Y = \min\{X_1, \dots, X_{24}\}$. From $\mathbb{P}(X_{(1)} > t) = [1 - F(t)]^n = \mathrm{e}^{-n\lambda t}$ we get $X \sim \mathrm{Exp}(4\lambda)$ and $Y \sim \mathrm{Exp}(24\lambda)$, so

$$
\mathbb{P}(X > t) = \mathrm{e}^{-4\lambda t}, \qquad \mathbb{P}(Y > t) = \mathrm{e}^{-24\lambda t}.
$$
With $\lambda = 1/6000$ (per hour, a mean lifetime of 6000 hours), $\mathbb{P}(X > 400) = 0.7659$ and $\mathbb{P}(X > 200) = 0.8752$, whereas $\mathbb{P}(Y > 400) = 0.2019$ and $\mathbb{P}(Y > 200) = 0.4493$. No individual bulb has become worse, but $Y$ is stochastically much smaller than $X$: what the caretaker notices is the first bulb to fail.

### 7.2.3. Order Statistics of the Uniform Distribution and the Beta Distribution

Recall the beta distribution ([3.1.4](/3.1.4)): for $\alpha, \beta > 0$ its density is

$$
f(x) = \frac{1}{\mathrm{B}(\alpha, \beta)} x^{\alpha - 1}(1 - x)^{\beta - 1}, \quad 0 < x < 1, \qquad \mathrm{B}(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)},
$$
written $\mathrm{Beta}(\alpha, \beta)$. For $\alpha = \beta = 1$ it is $\mathrm{U}(0, 1)$; for $\alpha = 2, \beta = 1$ the density is the straight line $2x$; for $\alpha = \beta = 1/2$ it is U-shaped; for $\alpha = \beta = 2$ it is an inverted U. In Bayesian statistics the beta distribution is often used as the prior for a probability parameter $p$: it is the conjugate prior of the binomial distribution, and if $X \mid p \sim \mathrm{Bin}(n, p)$ with prior $p \sim \mathrm{Beta}(\alpha, \beta)$, the posterior is $p \mid X \sim \mathrm{Beta}(\alpha + X, \beta + n - X)$ ([3.2.7](/3.2.7)).

**Example 7.2.3** If $U_1, \dots, U_n \overset{\text{iid}}{\sim} \mathrm{U}(0, 1)$, then $U_{(k)} \sim \mathrm{Beta}(k, n - k + 1)$.

**Proof** Here $F(x) = x$ and $f(x) = 1$ for $0 < x < 1$, so by Property 7.2.3

$$
g_k(x) = \frac{n!}{(k - 1)!\,(n - k)!} x^{k-1}(1 - x)^{n-k} = \frac{x^{k-1}(1 - x)^{n-k}}{\mathrm{B}(k, n - k + 1)}, \quad 0 < x < 1. \qquad \square
$$

The beta distribution can thus be viewed as a generalization of the uniform distribution: beta distributions with integer parameters are exactly the distributions of uniform order statistics. Intuitively, $n$ uniform points divide $(0, 1)$ into $n + 1$ pieces, and the $k$-th point lies "on average" at $\frac{k}{n+1}$ (in [3.1.8](/3.1.8) we compute $\mathbb{E}U_{(k)} = \frac{k}{n+1}$).

![Densities of the order statistics U_(k) of n = 5 independent U(0,1) variables, i.e. Beta(k, 6 - k)](./plots/uniform-order-statistics.py)

## 7.3. Quantiles of Random Variables

### 7.3.1. Definition

Let $X$ be a random variable on $(\Omega, \mathcal{F}, \mathbb{P})$ with distribution function $F(x)$. Intuitively, for $p \in (0, 1)$, a number $x$ is a $p$-quantile of $X$ if

$$
\mathbb{P}(X \le x) \ge p, \qquad \mathbb{P}(X \ge x) \ge 1 - p.
$$
A quantile defined this way need not be unique (if $F$ has a flat piece at height $p$, the whole piece satisfies the conditions). Statistical inference usually does not require uniqueness, as in the question "within what range does the number of heads in 100 tosses of a fair coin fall with probability 95%?"; but statistical computing, such as random number generation, requires a unique definition.

**Definition 7.3.1 (Quantile)** For $p \in (0, 1)$ define

$$
F^{-1}(p) = \inf\{x \mid F(x) \ge p\}.
$$
$F^{-1}(p)$ is called the $p$-**quantile** of $F$ (or of $X$) and is usually denoted $\xi_p$. $\xi_{1/2}$ is called the **median** of $F$ (or of $X$).

Equivalently, $F^{-1}(p) = \sup\{x \mid F(x) < p\}$. $F^{-1}$ is called the quantile function. When $F$ is continuous and strictly increasing it is the ordinary inverse function; in general it is the generalized inverse of $F$: where $F$ jumps, $F^{-1}$ is flat, and where $F$ is flat, $F^{-1}$ jumps. Statistics often uses the upper $\alpha$ quantile $\xi_{1 - \alpha}$; for example, the upper $\alpha$ quantile $z_\alpha = \Phi^{-1}(1 - \alpha)$ of the standard normal distribution satisfies $\mathbb{P}(Z > z_\alpha) = \alpha$ ([3.2.2](/3.2.2)).

![A distribution function F with both jumps and flat pieces (left) and its quantile function F^{-1} (right)](./plots/quantile-function.py)

### 7.3.2. Properties of Quantiles

**Property 7.3.1** Let $F$ be a distribution function. Then

1. $F^{-1}(p)$ is nondecreasing in $p$;
2. $F^{-1}(F(x)) \le x$ for all $x \in \mathbb{R}$ (with $F(x) \in (0, 1)$);
3. $F(F^{-1}(p)) \ge p$ for all $p \in (0, 1)$;
4. $F^{-1}(p) \le t \iff p \le F(t)$;
5. $F^{-1}(p)$ is left-continuous;
6. if $F$ is continuous, then $F(F^{-1}(p)) = p$ for all $p \in (0, 1)$.

**Proof** 1. If $p_1 < p_2$, then $F(t) \ge p_2$ implies $F(t) \ge p_1$, that is, $\{t \mid F(t) \ge p_1\} \supset \{t \mid F(t) \ge p_2\}$; taking infima gives $F^{-1}(p_1) \le F^{-1}(p_2)$.

2. $x \in \{t \mid F(t) \ge F(x)\}$, so $F^{-1}(F(x)) = \inf\{t \mid F(t) \ge F(x)\} \le x$.

3. Since $F$ is nondecreasing, $r \in \{t \mid F(t) \ge p\}$ implies $[r, \infty) \subset \{t \mid F(t) \ge p\}$, so this set (nonempty because $F(t) \to 1 > p$, and bounded below because $F(t) \to 0 < p$) has the form $[a, \infty)$ or $(a, \infty)$ with $a = F^{-1}(p)$. Since $a + 1/n$ belongs to the set, $F(a + 1/n) \ge p$, and letting $n \to \infty$, right-continuity of $F$ gives $F(a) \ge p$. This also shows that the set is the closed interval $[F^{-1}(p), \infty)$, so the infimum is attained.

4. If $F(t) \ge p$, then $t \in \{s \mid F(s) \ge p\}$, so $t \ge F^{-1}(p)$. Conversely, if $F^{-1}(p) \le t$, then monotonicity of $F$ and property 3 give $F(t) \ge F(F^{-1}(p)) \ge p$.

5. Let $p_n \uparrow p$. By property 1, $F^{-1}(p_n)$ is nondecreasing and bounded by $F^{-1}(p)$; let $b \le F^{-1}(p)$ be its limit. For each $n$, $F^{-1}(p_n) \le b$, so $p_n \le F(b)$ by property 4; letting $n \to \infty$ gives $p \le F(b)$, and property 4 again gives $F^{-1}(p) \le b$. Hence $\lim_n F^{-1}(p_n) = F^{-1}(p)$.

6. By property 3, $F(F^{-1}(p)) \ge p$. Suppose $F(a) > p$ at $a = F^{-1}(p)$. By continuity of $F$ there is $\delta > 0$ with $F(a - \delta) \ge p$, and then property 4 gives $a = F^{-1}(p) \le a - \delta$, a contradiction. $\square$

Property 4 is the most frequently used property of quantiles: it converts inequalities about $F^{-1}$ into inequalities about $F$.

### 7.3.3. Generating Random Variables

**Theorem 7.3.1 (Inverse Transform Method)** Let $U \sim \mathrm{U}(0, 1)$ and let $F$ be any distribution function. Then $Y = F^{-1}(U)$ has distribution function $F$.

**Proof** By property 4 of Property 7.3.1, for any $y$,

$$
\mathbb{P}(Y \le y) = \mathbb{P}(F^{-1}(U) \le y) = \mathbb{P}(U \le F(y)) = F(y). \qquad \square
$$

**Theorem 7.3.2 (Probability Integral Transform)** If the distribution function $F$ of $X$ is continuous, then $F(X) \sim \mathrm{U}(0, 1)$.

**Proof** For $u \in (0, 1)$, property 4 of Property 7.3.1 gives $\{F(X) \ge u\} = \{X \ge F^{-1}(u)\}$. By continuity of $F$ and property 6,

$$
\mathbb{P}(F(X) \ge u) = 1 - F(F^{-1}(u)) = 1 - u.
$$
Hence $\mathbb{P}(F(X) < u) = u$, and by right-continuity $\mathbb{P}(F(X) \le u) = \lim_{v \downarrow u}\mathbb{P}(F(X) < v) = u$. $\square$

The conclusion fails when $F$ has jumps: for example, if $X$ takes only two values, so does $F(X)$.

**Example 7.3.1** Suppose independent $\mathrm{U}(0, 1)$ random numbers $U, V$ are readily available. How can we generate random numbers with the following distributions: (1) $\mathrm{Exp}(\lambda)$; (2) $\mathcal{N}(0, 1)$; (3) the Cauchy distribution; (4) the empirical distribution function $F_n(x) = \frac{1}{n}\sum_{i=1}^n \boldsymbol{1}\{x_i \le x\}$ of given observations $x_1, \dots, x_n$?

**Solution** (1) $F(x) = 1 - \mathrm{e}^{-\lambda x}$ and $F^{-1}(u) = -\lambda^{-1}\ln(1 - u)$, so take $X = -\lambda^{-1}\ln(1 - U)$ (or $-\lambda^{-1}\ln U$, since $1 - U \sim \mathrm{U}(0, 1)$).

(2) The normal distribution function has no elementary inverse, so we use the Box–Muller method (Example 7.1.8): with $\Theta = 2\pi U$ and $R = \sqrt{-2\ln V}$, the variables $X = R\cos\Theta$ and $Y = R\sin\Theta$ are independent and both $\mathcal{N}(0, 1)$.

(3) By Example 7.1.6, take $Z = X/Y$ with $X, Y$ the independent standard normal numbers generated in (2); or use the inverse transform $Z = \tan(\pi(U - 1/2))$.

(4) $F_n$ is a step function. Let $x_{(1)} \le \cdots \le x_{(n)}$ be the sorted observations; then $F_n^{-1}(u) = x_{(k)}$ for $\frac{k-1}{n} < u \le \frac{k}{n}$, so

$$
\mathbb{P}(F_n^{-1}(U) = x_{(k)}) = \mathbb{P}\Big(\frac{k - 1}{n} < U \le \frac{k}{n}\Big) = \frac{1}{n}, \quad k = 1, \dots, n,
$$
that is, we simply sample from the observations with replacement and with equal probabilities. This is the basic operation of the bootstrap in statistics. Likewise, the Bernoulli distribution $\mathrm{Ber}(p)$ can be generated as $X = \boldsymbol{1}\{U > 1 - p\}$.

**Example 7.3.2** If $X_1, \dots, X_n$ are independent and identically distributed with continuous distribution function $F$, then $T = -2\sum_{i=1}^n \ln F(X_i) \sim \chi^2_{2n}$.

**Proof** By Theorem 7.3.2, $U_i = F(X_i) \sim \mathrm{U}(0, 1)$, and these are independent. $Y_i = -2\ln U_i$ satisfies $\mathbb{P}(Y_i > y) = \mathbb{P}(U_i < \mathrm{e}^{-y/2}) = \mathrm{e}^{-y/2}$ for $y > 0$, so $Y_i \sim \mathrm{Exp}(1/2) = \chi^2_2$. By the additivity in Theorem 7.1.6, $T = \sum_i Y_i \sim \chi^2_{2n}$. $\square$

This result underlies Fisher's method of combining the $p$-values of several independent tests.

## Summary

| Problem | Method | Result |
|---|---|---|
| General $g(\boldsymbol{X})$ | Find $F_Z(z) = \mathbb{P}(g(\boldsymbol{X}) \le z)$, then differentiate | Examples 7.1.1, 7.1.2 |
| $X + Y$ | Convolution formula $f_Z(z) = \int f(x, z - x)\,\mathrm{d}x$ | Additivity of binomial, Poisson and gamma distributions |
| $X - Y$, $X/Y$ | Reduce to known results, or find the distribution function first | $f_{X/Y}(z) = \int \lvert y \rvert f(zy, y)\,\mathrm{d}y$ |
| $(u(X, Y), v(X, Y))$ | Change of variables: $\sum_i f(x_i, y_i)\lvert J_i \rvert$ | Polar coordinates, Box–Muller |
| $X_{(k)}$ | Integrate the joint density $n!\prod f(x_i)$, or argue infinitesimally | $g_k = n\binom{n-1}{k-1}F^{k-1}(1-F)^{n-k}f$ |
| Random number generation | Inverse transform $F^{-1}(U) \sim F$ | $F(X) \sim \mathrm{U}(0, 1)$ for continuous $F$ |

- The three main distributions: $\sum Z_i^2 \sim \chi^2_n$, $Z/\sqrt{X/n} \sim t_n$, $\frac{X/m}{Y/n} \sim F_{m,n}$; $\chi^2_n = \Gamma(n/2, 1/2)$, and $t_1$ is the Cauchy distribution.
- Order statistics of the uniform distribution have beta distributions: $U_{(k)} \sim \mathrm{Beta}(k, n - k + 1)$.
- The $p$-quantile $F^{-1}(p) = \inf\{x \mid F(x) \ge p\}$ always exists and is unique; its key property is $F^{-1}(p) \le t \iff p \le F(t)$.
- Techniques: a joint density that implies independence can be factored and normalized directly; the same problem often admits several solutions, and sometimes finding the distribution function first is simpler than applying a formula (as for the Cauchy density); the infinitesimal argument helps to understand and remember density formulas.
