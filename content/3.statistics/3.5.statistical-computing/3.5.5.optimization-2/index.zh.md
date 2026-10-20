---
title: 优化（二）
description: 牛顿法及其二阶收敛、弦截法、Fisher 得分法与迭代重加权最小二乘、阻尼牛顿法与拟牛顿法（Davidon、BFGS、DFP）、置信域法、非线性回归中的 Gauss–Newton 法与 Levenberg–Marquardt 法、带线搜索的梯度下降与随机梯度下降，以及共轭方向法与共轭梯度法。
source_hash: 912d1679d4e3
---

[3.5.4](/3.5.4) 建立了数值优化的框架：优化与求根的关系、迭代算法的三要素、收敛阶，以及无需导数或只需划界的方法。本章转向利用导数的方法，它们分为三类。牛顿型方法利用二阶信息，在解附近收敛很快，但每步代价高，远离解时可能失败；梯度下降只用一阶导数，每步便宜但收敛慢；共轭方向法介于两者之间。这些一般方法在途中与统计相遇：似然方程的牛顿法变为 Fisher 得分法，对**广义线性模型**（[3.3.6](/3.3.6)）它就是迭代重加权最小二乘；Gauss–Newton 法则是**非线性回归**的 Fisher 得分法。[3.5.3](/3.5.3) 的线性代数（Cholesky 分解、Gram–Schmidt 正交化）贯穿全章，下一章的 EM 算法（[3.5.6](/3.5.6)）则是**极大似然估计**的另一种上升算法。

选择方法之前要先弄清两个问题：是求根还是求极值？是求极大还是求极小？下文用 $g$ 表示目标函数；求导函数的根时记 $f = g'$。对向量 $\boldsymbol{x}$ 的函数，$\nabla g$ 是梯度，$\nabla^2 g$ 是 **Hesse 矩阵** $\frac{\partial^2 g}{\partial\boldsymbol{x}\,\partial\boldsymbol{x}^{\mathsf T}}$。

## 5.1. Newton–Raphson 法及相关方法

### 5.1.1. 牛顿法

巴比伦方法用迭代

$$
x_{n+1} = \frac12\left(x_n + \frac{a}{x_n}\right) = x_n - \frac{x_n^2 - a}{2x_n},
$$
计算 $\sqrt a$，它恰是对 $f(x) = x^2 - a$ 的迭代 $x_{n+1} = x_n - f(x_n)/f'(x_n)$：牛顿法的一个特例。历史上，I. Newton（1669）只对多项式做逐次的代数修正；J. Raphson（1690）把它简化为迭代；T. Simpson（1740）给出了现代形式并用于优化。

先看一元函数 $g$，设其导数 $f = g'$ 连续可微，且在解 $x^*$ 处 $g''(x^*) \ne 0$。在第 $t$ 步，用 $x^{(t)}$ 处的线性 Taylor 展开近似 $g'(x^*)$：

$$
0 = g'(x^*) \approx g'(x^{(t)}) + (x^* - x^{(t)})\,g''(x^{(t)}).
$$
既然 $g'$ 被它在 $x^{(t)}$ 处的切线近似，自然用切线的根近似 $g'$ 的根。

**定义 5.1.1（牛顿法）** 为求解 $g'(x) = 0$，**牛顿法**（Newton–Raphson 法）从 $x^{(0)}$ 出发迭代

$$
x^{(t+1)} = x^{(t)} - \frac{g'(x^{(t)})}{g''(x^{(t)})} = x^{(t)} + h^{(t)}. \tag{5.1}
$$
对 $g\colon \mathbb{R}^p \to \mathbb{R}$，更新为 $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \bigl[\nabla^2 g(\boldsymbol{x}^{(t)})\bigr]^{-1}\nabla g(\boldsymbol{x}^{(t)})$。

**例 5.1.1** 对 $g(x) = \frac{\log x}{1 + x}$，增量为

$$
h^{(t)} = \frac{(x^{(t)} + 1)\bigl(1 + 1/x^{(t)} - \log x^{(t)}\bigr)}{3 + 4/x^{(t)} + 1/(x^{(t)})^2 - 2\log x^{(t)}}.
$$
从 $x^{(0)} = 3$ 出发，牛顿法四步即得 $x^{(4)} = 3.59112$；相比之下，二分法要到第 19 次迭代才能确定前五位小数。

**定理 5.1.1（牛顿法的二阶收敛）** 设 $f$ 在单根 $x^*$（$f(x^*) = 0$，$f'(x^*) \ne 0$）附近二阶连续可微，$x^{(t+1)} = x^{(t)} - f(x^{(t)})/f'(x^{(t)})$。若 $x^{(0)}$ 充分接近 $x^*$，则 $x^{(t)} \to x^*$，且误差 $\varepsilon^{(t)} = x^{(t)} - x^*$ 满足

$$
\lim_{t\to\infty}\frac{\varepsilon^{(t+1)}}{(\varepsilon^{(t)})^2} = \frac{f''(x^*)}{2f'(x^*)} \triangleq c,
$$
因此牛顿法（至少）具有二阶收敛阶，$\alpha = 2$。

**证明** 由带 Lagrange 余项的 **Taylor 公式**，存在介于 $x^{(t)}$ 与 $x^*$ 之间的 $\xi_t$，使

$$
0 = f(x^*) = f(x^{(t)}) + (x^* - x^{(t)})f'(x^{(t)}) + \frac{(x^* - x^{(t)})^2}{2}f''(\xi_t).
$$
两边除以 $f'(x^{(t)})$ 得 $x^* - \bigl(x^{(t)} - f(x^{(t)})/f'(x^{(t)})\bigr) = -\frac{(\varepsilon^{(t)})^2}{2}\frac{f''(\xi_t)}{f'(x^{(t)})}$，即

$$
\varepsilon^{(t+1)} = \frac{f''(\xi_t)}{2f'(x^{(t)})}(\varepsilon^{(t)})^2.
$$
取 $\delta > 0$ 与 $C$，使 $\lvert x - x^*\rvert, \lvert\xi - x^*\rvert \le \delta$ 时 $\lvert f''(\xi)/(2f'(x))\rvert \le C$，且 $C\delta < 1$。若 $\lvert\varepsilon^{(0)}\rvert \le \delta$，则 $\lvert\varepsilon^{(t+1)}\rvert \le C\delta\lvert\varepsilon^{(t)}\rvert$，误差始终留在该区间内并趋于零；于是 $\xi_t \to x^*$，比值趋于 $c$。$\square$

下面的 R 函数用步长 $h$ 的前向差分代替精确导数 $f'$（严格说这是牛顿法的离散版本，见 5.1.4.3 节）：

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

对多元 $g$，同样的 Taylor 论证给出定义 5.1.1 的更新。实际中从不计算 Hesse 矩阵的逆，每次迭代解一个线性方程组。

**算法 5.1.1（基本牛顿法）** 选初值 $\boldsymbol{x}^{(0)}$ 与容差 $\varepsilon$。对 $t = 0, 1, \dots$：若 $\lVert\nabla g(\boldsymbol{x}^{(t)})\rVert \le \varepsilon$，停止；否则解 $\nabla^2 g(\boldsymbol{x}^{(t)})\,\boldsymbol{h}^{(t)} = -\nabla g(\boldsymbol{x}^{(t)})$，令 $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} + \boldsymbol{h}^{(t)}$。

在极大值点 $-\nabla^2 g$ 正定，在极小值点 $\nabla^2 g$ 正定；方程组用该矩阵的 **Cholesky 分解** $LL^{\mathsf T}$ 求解（[3.5.3](/3.5.3)），约需 $p^3/3$ 次浮点运算。若在局部极大值点 $\boldsymbol{x}^*$ 处 Hesse 矩阵负定且初值离解足够近，牛顿法二阶收敛到 $\boldsymbol{x}^*$（Hesse 矩阵正定时对局部极小值点同理）。

**例 5.1.2（Himmelblau 函数）** 多峰函数

$$
g(x, y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
$$
常用来测试优化算法。它有一个局部极大值点 $(-0.270845, -0.923039)$ 和四个函数值为 $0$ 的局部极小值点：$(3, 2)$、$(-2.805118, 3.131312)$、$(-3.779310, -3.283186)$、$(3.584428, -1.848126)$。从 $(-2, -2)$ 出发的牛顿法：

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

迭代终止于 $\boldsymbol{x} = (3, 2)$，$g(\boldsymbol{x}) = 0$，$\nabla g(\boldsymbol{x}) = \boldsymbol{0}$。路径可在网格上用 `contour(x1, x2, z, nlevels = 20)` 画等高线，再用 `segments()` 连接 `x.values` 的相邻行（传给 `contour` 的网格向量必须递增）。注意起点处的 Hesse 矩阵 $\begin{bmatrix} -2 & -16 \\ -16 & 14\end{bmatrix}$ 是不定的：牛顿法寻找的是任意类型的驻点，这里只是碰巧到达了极小值点。

### 5.1.2. 弦截法

当 $f = g'$ 的导数难以计算时，[3.5.4](/3.5.4) 的弦截法把式 (5.1) 中的 $g''(x^{(t)})$ 换成差商 $\frac{g'(x^{(t)}) - g'(x^{(t-1)})}{x^{(t)} - x^{(t-1)}}$：

$$
x^{(t+1)} = x^{(t)} - g'(x^{(t)})\,\frac{x^{(t)} - x^{(t-1)}}{g'(x^{(t)}) - g'(x^{(t-1)})}, \qquad t \ge 1.
$$
它需要两个初值 $x^{(0)}, x^{(1)}$，用过最近两个迭代点的割线局部近似 $g'$；割线的根 $x^{(t+1)}$ 与 $x^{(t)}$ 一起产生下一个近似。

**定理 5.1.2（弦截法的收敛阶）** 设 $x^*$ 是光滑函数 $f$ 的单根，弦截迭代 $x^{(t+1)} = x^{(t)} - f(x^{(t)})\frac{x^{(t)} - x^{(t-1)}}{f(x^{(t)}) - f(x^{(t-1)})}$ 满足 $\lvert\varepsilon^{(t+1)}\rvert \approx c\,\lvert\varepsilon^{(t)}\rvert^{\alpha}$，其中 $\alpha = \frac{1 + \sqrt5}{2} \approx 1.618$：超线性收敛。

**证明**（启发式）记 $f(x^* + \varepsilon) \approx f'(x^*)\varepsilon + \frac{f''(x^*)}{2}\varepsilon^2 = f'(x^*)\varepsilon(1 + M\varepsilon)$，$M = \frac{f''(x^*)}{2f'(x^*)}$。于是

$$
\varepsilon^{(t+1)} \approx \varepsilon^{(t)} - \frac{\varepsilon^{(t)}(1 + M\varepsilon^{(t)})(\varepsilon^{(t)} - \varepsilon^{(t-1)})}{\varepsilon^{(t)}(1 + M\varepsilon^{(t)}) - \varepsilon^{(t-1)}(1 + M\varepsilon^{(t-1)})} = \frac{M\varepsilon^{(t)}\varepsilon^{(t-1)}}{1 + M(\varepsilon^{(t)} + \varepsilon^{(t-1)})} \approx M\varepsilon^{(t)}\varepsilon^{(t-1)}.
$$
若 $\lvert\varepsilon^{(t+1)}\rvert \approx c\lvert\varepsilon^{(t)}\rvert^\alpha$，则 $\lvert\varepsilon^{(t-1)}\rvert \approx c_1\lvert\varepsilon^{(t)}\rvert^{1/\alpha}$，比较 $c\lvert\varepsilon^{(t)}\rvert^\alpha \approx \lvert M\rvert c_1\lvert\varepsilon^{(t)}\rvert^{1 + 1/\alpha}$ 的指数得 $\alpha = 1 + 1/\alpha$，即 $\alpha^2 - \alpha - 1 = 0$。$\square$

弦截法只需一阶导数，但数值上不如牛顿法稳定：当 $x^{(t)}$ 与 $x^{(t-1)}$ 彼此接近时，差商要做两个几乎相等的数的减法，产生抵消误差（[3.5.1](/3.5.1)）。

### 5.1.3. Fisher 得分法

#### 5.1.3.1. 一般形式

MLE $\hat\theta$ 是似然方程 $l'(\theta) = 0$ 的解，$l$ 是**对数似然函数**。此方程的牛顿法为

$$
\theta^{(t+1)} = \theta^{(t)} - \frac{l'(\theta^{(t)})}{l''(\theta^{(t)})} = \theta^{(t)} + J(\theta^{(t)})^{-1}l'(\theta^{(t)}), \qquad J(\theta) \triangleq -l''(\theta).
$$
$J(\hat\theta) > 0$ 决定了似然函数在极大值附近峰的陡峭程度。在通常的正则条件下，**Fisher 信息量**（[3.2.3](/3.2.3)）满足 $I(\theta) = \mathbb{E}[l'(\theta)^2] = \operatorname{Var}\bigl(l'(\theta)\bigr) = -\mathbb{E}[l''(\theta)] = \mathbb{E}[J(\theta)]$，所以通常 $I(\hat\theta) \approx J(\hat\theta)$。

**定义 5.1.2（观测信息与 Fisher 得分法）** 对对数似然 $l(\boldsymbol{\theta})$，矩阵 $J(\boldsymbol{\theta}) = -\nabla^2 l(\boldsymbol{\theta})$ 称为**观测信息**。**Fisher 得分法**（得分法）在牛顿法中用整个样本的期望（Fisher）信息 $I(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\theta}}[J(\boldsymbol{\theta})]$ 代替它：

$$
\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} + I(\boldsymbol{\theta}^{(t)})^{-1}\nabla l(\boldsymbol{\theta}^{(t)}). \tag{5.2}
$$

于是两种方法分别是

$$
\text{Newton–Raphson: } \boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} + J(\boldsymbol{\theta}^{(t)})^{-1}\nabla l(\boldsymbol{\theta}^{(t)}), \qquad \text{Fisher scoring: } \boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} + I(\boldsymbol{\theta}^{(t)})^{-1}\nabla l(\boldsymbol{\theta}^{(t)}),
$$
其中 $\nabla l$ 是样本的**得分函数**。Fisher 得分法也称为迭代重加权最小二乘，原因见 5.1.3.3 节。

#### 5.1.3.2. 与牛顿法的关系

回忆（带尺度的）**指数族**（[3.2.2](/3.2.2)）

$$
f(y \mid \theta) = \exp\left\{\frac{y\theta - b(\theta)}{a(\phi)} + c(y, \phi)\right\},
$$
其中 $\theta$ 是自然（典范）参数，$\phi$ 是散布参数。对一个观测，$l(\theta) = \frac{y\theta - b(\theta)}{a(\phi)} + c(y, \phi)$，$\frac{\partial l}{\partial\theta} = \frac{y - b'(\theta)}{a(\phi)}$。由于得分的均值为零，$\mathbb{E}(Y) = b'(\theta)$；又 $\frac{\partial^2 l}{\partial\theta^2} = -\frac{b''(\theta)}{a(\phi)}$ 且 $\operatorname{Var}\bigl(\frac{\partial l}{\partial\theta}\bigr) = -\mathbb{E}\bigl(\frac{\partial^2 l}{\partial\theta^2}\bigr)$，所以 $\operatorname{Var}(Y) = b''(\theta)a(\phi)$。此外

$$
J(\theta) = -\frac{\partial^2 l}{\partial\theta^2} = \frac{b''(\theta)}{a(\phi)} = I(\theta) \triangleq I_1(\theta)
$$
与 $y$ 无关，因而等于它的期望，即单个观测中的信息。

**命题 5.1.1** 对以典范参数表示的指数族，得分法与 Newton–Raphson 法一致。有 $n$ 个独立同分布观测时 $I(\theta) = nI_1(\theta)$，且

$$
\theta^{(t+1)} = \theta^{(t)} + \frac{I_1(\theta^{(t)})^{-1}l'(\theta^{(t)})}{n} = \theta^{(t)} + \frac{l'(\theta^{(t)})\,a(\phi)}{n\,b''(\theta^{(t)})}.
$$

均值未知的正态分布、Bernoulli 分布、Poisson 分布和 Gamma 分布都是指数族；Cauchy 分布和 Student $t$ 分布不是。

两种方法的一致只对典范参数成立。例如 Bernoulli 密度 $f(x \mid p) = p^x(1 - p)^{1 - x} = \exp\bigl\{x\log\frac{p}{1 - p} + \log(1 - p)\bigr\}$ 的典范参数是 $\theta = \log\frac{p}{1 - p}$，而均值是 $\mu = p$。用均值作参数，$\theta = g(\mu)$，则

$$
\frac{\partial l}{\partial\mu} = \frac{y - b'(g(\mu))}{a(\phi)}\,g'(\mu), \qquad J(\mu) = \frac{1}{a(\phi)}\Bigl[b''(g(\mu))\bigl(g'(\mu)\bigr)^2 + b'(g(\mu))g''(\mu) - y\,g''(\mu)\Bigr].
$$
观测信息依赖于 $y$；但由于 $\mathbb{E}(Y) = b'(\theta)$，后两项的期望相消，$\mathbb{E}\bigl[b'(g(\mu))g''(\mu) - Yg''(\mu)\bigr] = g''(\mu)\,\mathbb{E}\bigl[b'(g(\mu)) - Y\bigr] = 0$，从而

$$
I(\mu) = \mathbb{E}[J(\mu)] = \frac{1}{a(\phi)}b''(g(\mu))\bigl(g'(\mu)\bigr)^2.
$$
这就是得分法通常比牛顿法简洁的原因。

**例 5.1.3（Cauchy 位置参数）** 设 $x_1, \dots, x_{20}$ 是来自密度 $f(x; \theta) = \frac{1}{\pi[1 + (x - \theta)^2]}$ 的 **Cauchy 分布**的独立同分布样本。则

$$
l(\theta) = -\sum_{i=1}^{20}\log\bigl(1 + (x_i - \theta)^2\bigr) - n\log\pi, \qquad s(\theta) = \sum_{i=1}^{20}\frac{2(x_i - \theta)}{1 + (x_i - \theta)^2}, \qquad J(\theta) = 2\sum_{i=1}^{20}\frac{1 - (x_i - \theta)^2}{\bigl(1 + (x_i - \theta)^2\bigr)^2}.
$$
期望信息为

$$
I(\theta) = nI_1(\theta) = \frac{2n}{\pi}\int_{-\infty}^{+\infty}\frac{1 - (x - \theta)^2}{\bigl(1 + (x - \theta)^2\bigr)^3}\,\mathrm{d}x = \frac{n}{2}.
$$
事实上 $\frac{1 - x^2}{(1 + x^2)^3} = \frac{2}{(1 + x^2)^3} - \frac{1}{(1 + x^2)^2}$，代换 $x = \tan u$ 得 $\int_0^{+\infty}\frac{\mathrm{d}x}{(1 + x^2)^3} = \int_0^{\pi/2}\cos^4u\,\mathrm{d}u = \frac{3\pi}{16}$ 与 $\int_0^{+\infty}\frac{\mathrm{d}x}{(1 + x^2)^2} = \int_0^{\pi/2}\cos^2u\,\mathrm{d}u = \frac{\pi}{4}$，故积分为 $2\bigl(2\cdot\frac{3\pi}{16} - \frac{\pi}{4}\bigr) = \frac{\pi}{4}$。两种更新为

$$
\text{Newton–Raphson: } \theta^{(t+1)} = \theta^{(t)} + \frac{s(\theta^{(t)})}{J(\theta^{(t)})}, \qquad \text{Fisher scoring: } \theta^{(t+1)} = \theta^{(t)} + \frac{4}{n}\sum_{i=1}^{20}\frac{x_i - \theta^{(t)}}{1 + (x_i - \theta^{(t)})^2}.
$$

stats4 包的函数 `mle` 的第一个参数是计算负对数似然 $-l(\theta)$ 的函数，它调用通用优化器 `optim` 将其极小化：

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

这组数据的对数似然在 $\hat\theta = -0.19229$ 处取全局极大，在 $2.8175$ 处有一个局部极大，在离群值 $43.21$ 和 $56.75$ 附近还有其他驻点。从不同初值运行两种迭代（各 30 次）可以看出初值有多重要：

| $\theta^{(0)}$ | $-11$ | $-1$ | $0$ | $1.5$ | $4$ | $4.7$ | $7$ | $8$ | $38$ | $\bar x = 5.106$ |
|---|---|---|---|---|---|---|---|---|---|---|
| Newton–Raphson | 发散 | $-0.1923$ | $-0.1923$ | $1.7136$（极小） | $2.8175$ | $-0.1923$ | $41.04$（极小） | 发散 | $42.80$ | $54.88$（极小） |
| Fisher 得分 | $-0.2833$ | $-0.1923$ | $-0.1923$ | $-0.1902$ | $2.8177$ | $2.8177$ | $2.8179$ | $2.8182$ | $36.35$ | $2.8177$ |

牛顿法一旦收敛就很快，但可能走到局部极小值点或发散；这里 Fisher 得分法总是上坡，因为 $I(\theta) = n/2 > 0$，但它只线性收敛，30 步后有几次运行离驻点还差一点。对 Cauchy 数据，样本均值是很差的初值。

![左：Cauchy 对数似然，全局极大值在 -0.1923；从 1.5 出发的牛顿法收敛到局部极小值点 1.71，从 7 出发收敛到 41 附近的极小值点，而从 7 出发的 Fisher 得分法爬到局部极大值点 2.82。右：从 -1 出发的误差（对数坐标）；牛顿法五步内二阶收敛，Fisher 得分法线性收敛。](./plots/cauchy-newton-scoring.py)

#### 5.1.3.3. 迭代重加权最小二乘

对 $p$ 维参数，多元 Taylor 论证给出牛顿更新 $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - [\nabla^2 g(\boldsymbol{x}^{(t)})]^{-1}\nabla g(\boldsymbol{x}^{(t)})$ 和带 **Fisher 信息矩阵** $I(\boldsymbol{\theta})$ 的得分法 (5.2)。在把它们用于回归模型之前，先作比较。

- 很多情况下 $I(\boldsymbol{\theta})$ 更容易计算，且总是正（半）定的。这通常使算法更稳定：得分方向是上升方向。
- 收敛时，$J(\boldsymbol{\theta}^{(t)}) \approx J(\hat{\boldsymbol{\theta}}) \approx I(\hat{\boldsymbol{\theta}})$ 可用来评估 $\hat{\boldsymbol{\theta}}$ 的不确定性：由于 $\hat{\boldsymbol{\theta}} \overset{\cdot}{\sim} \mathcal{N}_d\bigl(\boldsymbol{\theta}, I(\boldsymbol{\theta})^{-1}\bigr)$ 且 $(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta})^{\mathsf T}I(\hat{\boldsymbol{\theta}})(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}) \overset{\cdot}{\sim} \chi^2_d$，可估计 $\operatorname{Cov}(\hat{\boldsymbol{\theta}}) \approx J(\boldsymbol{\theta}^{(t)})^{-1}$。
- 对指数族模型两者几乎等价：若 $(\theta_1, \dots, \theta_p)$ 是自然参数，则 $J(\boldsymbol{\theta}) = I(\boldsymbol{\theta})$，两种方法一致；否则得分法更简洁。
- 两者有相同的渐近性质，对具体问题哪个更容易都有可能。一般而言，两者都收敛时牛顿法更快，而 Fisher 得分法的收敛半径往往更大；Fisher 得分法开始时改进迅速，牛顿法在最后的精细化上更好。

现在考虑 **logistic 回归**。线性预测子 $\eta = \beta_0 + \beta_1x_1 + \cdots + \beta_{p-1}x_{p-1}$，不再假设 $Y \mid \boldsymbol{X} = \boldsymbol{x}_i \sim \mathcal{N}(\eta_i, \sigma^2)$，而假设 $Y \mid \boldsymbol{X} = \boldsymbol{x}_i \sim \mathrm{Ber}(p_i)$。**联系函数** $g$ 把均值 $\mu = \mathbb{E}(Y \mid \boldsymbol{X}) \in (0, 1)$ 映到 $\eta \in \mathbb{R}$：$\eta = g(\mu)$，$\mu = g^{-1}(\eta)$；这里

$$
g(p) = \operatorname{logit}(p) = \log\frac{p}{1 - p} = \eta, \qquad p = g^{-1}(\eta) = \frac{\mathrm{e}^\eta}{1 + \mathrm{e}^\eta}.
$$
一般地，**广义线性模型**对指数族中的响应假设 $g\bigl(\mathbb{E}(Y_i \mid \boldsymbol{x}_i)\bigr) = \boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}$。对 logistic 回归，$Y_i \mid \boldsymbol{x}_i \sim \mathrm{Ber}(p_i)$ 相互独立，$f(y \mid p) = \exp\{y\log\frac{p}{1 - p} + \log(1 - p)\}$ 的**自然参数**为 $\theta = \log\frac{p}{1 - p}$。在 logit 联系下自然参数是协变量的线性函数，$\theta_i = g(p_i) = \boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}$，且 $b(\theta_i) = -\log(1 - p_i) = \log(1 + \mathrm{e}^{\theta_i})$，$b'(\theta) = \frac{\mathrm{e}^\theta}{1 + \mathrm{e}^\theta} = p$。记 $\boldsymbol{y} = (y_1, \dots, y_n)^{\mathsf T}$，$\boldsymbol{p} = (p_1, \dots, p_n)^{\mathsf T}$，设计矩阵为 $X$，则

$$
l(\boldsymbol{\beta}) = \sum_{i=1}^n\bigl[y_i\theta_i - b(\theta_i)\bigr] = \boldsymbol{y}^{\mathsf T}X\boldsymbol{\beta} - \boldsymbol{b}(X\boldsymbol{\beta})^{\mathsf T}\boldsymbol{1},
$$
$$
\nabla l(\boldsymbol{\beta}) = X^{\mathsf T}(\boldsymbol{y} - \boldsymbol{p}), \qquad \nabla^2 l(\boldsymbol{\beta}) = -\left(\frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}\boldsymbol{\theta}}\frac{\mathrm{d}\boldsymbol{\theta}}{\mathrm{d}\boldsymbol{\beta}}\right)^{\mathsf T}X = -X^{\mathsf T}WX,
$$
其中 $W = \frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}\boldsymbol{\theta}}$ 是对角阵，对角元 $\frac{\mathrm{d}p_i}{\mathrm{d}\theta_i} = \frac{\mathrm{e}^{\theta_i}}{(1 + \mathrm{e}^{\theta_i})^2} = p_i(1 - p_i)$。

Hesse 矩阵与 $\boldsymbol{y}$ 无关，所以 $-\nabla^2 l(\boldsymbol{\beta}) = X^{\mathsf T}WX = \mathbb{E}[-\nabla^2 l(\boldsymbol{\beta})] = I(\boldsymbol{\beta})$，Fisher 得分法与牛顿法相同。对 GLM，只要联系函数使自然参数成为协变量的线性函数（典范联系，$\eta \equiv \theta$），这一点总成立。牛顿更新为

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \bigl(X^{\mathsf T}W^{(t)}X\bigr)^{-1}X^{\mathsf T}(\boldsymbol{y} - \boldsymbol{p}^{(t)}), \qquad W^{(t)} = \operatorname{diag}\bigl\{p_i^{(t)}(1 - p_i^{(t)})\bigr\},
$$
其中 $\boldsymbol{p}^{(t)} = \boldsymbol{p}(\boldsymbol{\beta}^{(t)})$。怎样用任何最小二乘软件计算它？回忆 $W^{1/2}\boldsymbol{Y} = W^{1/2}X\boldsymbol{\beta} + W^{1/2}\boldsymbol{\varepsilon}$ 的**加权最小二乘**给出 $\hat{\boldsymbol{\beta}} = (X^{\mathsf T}WX)^{-1}X^{\mathsf T}W\boldsymbol{Y}$（[3.3.12](/3.3.12)）。改写为

$$
\boldsymbol{\beta}^{(t+1)} = \bigl(X^{\mathsf T}W^{(t)}X\bigr)^{-1}\bigl(X^{\mathsf T}W^{(t)}X\boldsymbol{\beta}^{(t)} + X^{\mathsf T}(\boldsymbol{y} - \boldsymbol{p}^{(t)})\bigr) = \bigl(X^{\mathsf T}W^{(t)}X\bigr)^{-1}X^{\mathsf T}W^{(t)}\boldsymbol{z}^{(t)}, \tag{5.3}
$$
其中工作响应（调整因变量）为 $\boldsymbol{z}^{(t)} = X\boldsymbol{\beta}^{(t)} + (W^{(t)})^{-1}(\boldsymbol{y} - \boldsymbol{p}^{(t)})$。它是把联系函数作用于数据后的线性化：$z = g(y) \approx g(p) + (y - p)g'(p) = \theta + (y - p)\frac{\mathrm{d}\theta}{\mathrm{d}p}$，对 logit 联系 $\frac{\mathrm{d}\theta}{\mathrm{d}p} = \frac{1}{p(1 - p)}$。

**算法 5.1.2（迭代重加权最小二乘）** 迭代重加权最小二乘（IRLS）通过反复做加权最小二乘计算 GLM 的 MLE。设定 $\boldsymbol{\beta}^{(0)}$；对 logistic 回归（$\boldsymbol{\mu} = \boldsymbol{p}$），每次迭代为：

1. 固定 $\boldsymbol{\beta}^{(t)}$，计算 $p_i^{(t)} = g^{-1}(\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}^{(t)})$；
2. 计算权重 $W^{(t)} = \operatorname{diag}\{p_i^{(t)}(1 - p_i^{(t)})\}$；
3. 计算调整因变量 $z_i^{(t)} = \boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}^{(t)} + (y_i - p_i^{(t)})/W^{(t)}_{ii}$；
4. 以 $W^{(t)}$ 为权重把 $\boldsymbol{z}^{(t)}$ 对 $X$ 回归，得到 $\boldsymbol{\beta}^{(t+1)}$，在 R 中即 `lm(z ~ X - 1, weights = w)`。

重复直至收敛。

常用的初值是 $\boldsymbol{\mu}^{(0)} = \boldsymbol{y}$，即由 $g(\boldsymbol{y})$ 对 $X$ 回归得到 $\boldsymbol{\beta}^{(0)}$。这对 logistic 回归不适用，因为 $\operatorname{logit}(0)$ 与 $\operatorname{logit}(1)$ 为无穷；此时从 $\boldsymbol{\beta}^{(0)} = \boldsymbol{0}$（$p_i = 1/2$）出发，或像 `glm` 那样取 $\mu_i^{(0)} = (y_i + 1/2)/2$。

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

**注 5.1.1** 同样的推导适用于任何指数族响应和任何联系函数：均值 $\mu_i = g^{-1}(\eta_i)$、方差 $\operatorname{Var}(Y_i) = a(\phi)V(\mu_i)$ 的 GLM 的 Fisher 得分法，就是取

$$
w_i = \frac{1}{V(\mu_i)\,g'(\mu_i)^2}, \qquad z_i = \eta_i + (y_i - \mu_i)\,g'(\mu_i)
$$
的加权回归 (5.3)；散布 $a(\phi)$ 被约去。对数联系的 Poisson 回归中 $w_i = \mu_i$，$z_i = \eta_i + (y_i - \mu_i)/\mu_i$。对典范联系，IRLS 也是牛顿法；对其他联系，它是 Fisher 得分法。

### 5.1.4. 牛顿法的变种

#### 5.1.4.1. 牛顿法的缺点

速度不是唯一要考虑的因素。在慢速的划界方法（如二分法）能成功的地方，牛顿法可能发散：迭代点可能落在切线几乎水平的地方而被抛向远处，迭代也可能来回振荡。初值至关重要，例 5.1.3 的 Cauchy 对数似然就说明了这一点。基本算法（解 $\nabla^2 g(\boldsymbol{x}^{(t)})\boldsymbol{h}^{(t)} = -\nabla g(\boldsymbol{x}^{(t)})$）有以下问题：

- 需要导数，计算导数可能代价高昂甚至不可能；
- 每次迭代要解一个线性方程组，对大规模问题要求很高；
- 只有初值离解足够近时才收敛；
- Hesse 矩阵 $\nabla^2 g(\boldsymbol{x}^{(t)})$ 可能奇异，方程组无法求解；
- 不能保证上坡（或下坡）；
- 即使步长方向好，步长大小也很重要。

注意若 $A$ 是**正定矩阵**，则 $A^{-1}$ 存在且仍正定（其特征值是 $A$ 的特征值的倒数）。下文反复用到这一点。

#### 5.1.4.2. 下降方向与步长

考虑极小化。沿方向 $\boldsymbol{d}$，

$$
g(\boldsymbol{x}^{(t)} + \alpha\boldsymbol{d}) = g(\boldsymbol{x}^{(t)}) + \alpha\boldsymbol{d}^{\mathsf T}\nabla g(\boldsymbol{x}^{(t)}) + \frac12\alpha^2\boldsymbol{d}^{\mathsf T}\nabla^2 g(\boldsymbol{x}^{(t)})\boldsymbol{d} + o(\alpha^2\lVert\boldsymbol{d}\rVert_2^2).
$$
若 $g$ 是二次函数，牛顿步 $\alpha^{(t)}\boldsymbol{d}^{(t)} = -[\nabla^2 g(\boldsymbol{x}^{(t)})]^{-1}\nabla g(\boldsymbol{x}^{(t)})$ 恰是 $g$ 的极小值点。否则，把它代入二次部分得到预测的变化量

$$
\bigl(\alpha^{(t)}\boldsymbol{d}^{(t)}\bigr)^{\mathsf T}\nabla g + \frac12\bigl(\alpha^{(t)}\boldsymbol{d}^{(t)}\bigr)^{\mathsf T}\nabla^2 g\,\bigl(\alpha^{(t)}\boldsymbol{d}^{(t)}\bigr) = -\frac12\nabla g(\boldsymbol{x}^{(t)})^{\mathsf T}\bigl[\nabla^2 g(\boldsymbol{x}^{(t)})\bigr]^{-1}\nabla g(\boldsymbol{x}^{(t)}),
$$
Hesse 矩阵负定时它是增加量，正定时是减少量。

**定义 5.1.3（下降方向）** 在点 $\boldsymbol{x} \in \mathbb{R}^n$ 处，若存在 $\bar\alpha > 0$ 使得对所有 $\alpha \in (0, \bar\alpha)$ 有 $g(\boldsymbol{x} + \alpha\boldsymbol{d}) < g(\boldsymbol{x})$，则称方向 $\boldsymbol{d} \in \mathbb{R}^n$ 为**下降方向**。

**命题 5.1.2** 在 $\nabla g(\boldsymbol{x}) \ne \boldsymbol{0}$ 且 $\nabla^2 g(\boldsymbol{x}) \succ 0$ 的任意点 $\boldsymbol{x}$ 处，牛顿方向 $-[\nabla^2 g(\boldsymbol{x})]^{-1}\nabla g(\boldsymbol{x})$ 是下降方向。

**证明** 任何满足 $\boldsymbol{d}^{\mathsf T}\nabla g(\boldsymbol{x}) < 0$ 的 $\boldsymbol{d}$ 都是下降方向，因为 $g(\boldsymbol{x} + \alpha\boldsymbol{d}) = g(\boldsymbol{x}) + \alpha\boldsymbol{d}^{\mathsf T}\nabla g(\boldsymbol{x}) + o(\alpha)$。对牛顿方向，$\boldsymbol{d}^{\mathsf T}\nabla g(\boldsymbol{x}) = -\nabla g(\boldsymbol{x})^{\mathsf T}[\nabla^2 g(\boldsymbol{x})]^{-1}\nabla g(\boldsymbol{x}) < 0$，因为正定矩阵的逆正定。$\square$

所以牛顿法不能保证每次迭代都下降，但对严格**凸函数**，牛顿方向总是下降方向：只要步子足够小，就确实得到下降。这启发我们控制步长。

**定义 5.1.4（阻尼牛顿法）** 牛顿法结合回溯，即**阻尼牛顿法**，迭代

$$
\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\bigl[\nabla^2 g(\boldsymbol{x}^{(t)})\bigr]^{-1}\nabla g(\boldsymbol{x}^{(t)}),
$$
其中 $\alpha^{(t)}$ 由回溯确定：先试 $\alpha = 1$ 的一步；若它上坡，就缩小（例如减半）$\alpha$；继续减半，直到找到一个足够小的下坡步。

当计算和使用 Hesse 矩阵不切实际或代价太高时，用近似 $M^{(t)} \approx \nabla^2 g(\boldsymbol{x}^{(t)})$ 代替它，得到改进的牛顿法（偏转梯度法）

$$
\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\bigl(M^{(t)}\bigr)^{-1}\nabla g(\boldsymbol{x}^{(t)}).
$$
由命题 5.1.2 的证明，任何正定的 $M^{(t)}$ 都能保证在 $\alpha^{(t)}$ 足够小时下降。取 $M^{(t)} = I$ 即为梯度下降 $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\nabla g(\boldsymbol{x}^{(t)})$（5.2 节）。因此改进的牛顿法每步要做两个选择：步长，以及 Hesse 矩阵的近似。

#### 5.1.4.3. 离散牛顿法

一维弦截法的类比是用梯度的差分近似 Hesse 矩阵：

$$
M_{ij}^{(t)} = \frac{g_i'\bigl(\boldsymbol{x}^{(t)} + h_{ij}^{(t)}\boldsymbol{e}_j\bigr) - g_i'(\boldsymbol{x}^{(t)})}{h_{ij}^{(t)}},
$$
其中 $g_i'(\boldsymbol{x}) = \partial g(\boldsymbol{x})/\partial x_i$ 是 $\nabla g$ 的第 $i$ 个分量，$\boldsymbol{e}_j$ 是 $\mathbb{R}^p$ 的第 $j$ 个标准基向量，$h_{ij}^{(t)}$ 是常数。对所有 $(i, j)$ 和 $t$ 取 $h_{ij}^{(t)} = h$ 导致线性收敛，而对所有 $i$ 取 $h_{ij}^{(t)} = x_j^{(t)} - x_j^{(t-1)}$ 给出超线性收敛。若 $M^{(t)}$ 不对称，用 $\frac12\bigl(M^{(t)} + (M^{(t)})^{\mathsf T}\bigr)$。这种方法计算负担重：每次迭代需要额外 $p$ 次梯度计算。

#### 5.1.4.4. 拟牛顿法

**定义 5.1.5（割线条件与拟牛顿法）** 记 $\boldsymbol{z}^{(t)} = \boldsymbol{x}^{(t+1)} - \boldsymbol{x}^{(t)}$，$\boldsymbol{y}^{(t)} = \nabla g(\boldsymbol{x}^{(t+1)}) - \nabla g(\boldsymbol{x}^{(t)})$。若矩阵 $M^{(t+1)}$ 满足

$$
\nabla g(\boldsymbol{x}^{(t+1)}) - \nabla g(\boldsymbol{x}^{(t)}) = M^{(t+1)}\bigl(\boldsymbol{x}^{(t+1)} - \boldsymbol{x}^{(t)}\bigr), \quad\text{即}\quad \boldsymbol{y}^{(t)} = M^{(t+1)}\boldsymbol{z}^{(t)},
$$
则称它满足**割线条件**（拟牛顿条件）。**拟牛顿法**以计算量小、满足割线条件、并学习 $g$ 在最近一步方向上的曲率的方式，由 $M^{(t)}$ 生成 $M^{(t+1)}$。

迭代交替两步：用 $M^{(t)}$ 把 $\boldsymbol{x}^{(t)}$ 更新为 $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}(M^{(t)})^{-1}\nabla g(\boldsymbol{x}^{(t)})$，再学习曲率，把 $M^{(t)}$ 更新为 $M^{(t+1)}$，用于 $\boldsymbol{x}^{(t+2)} = \boldsymbol{x}^{(t+1)} - \alpha^{(t+1)}(M^{(t+1)})^{-1}\nabla g(\boldsymbol{x}^{(t+1)})$。

最简单的选择是秩一修正，即 Davidon 更新（Davidon's update），即对称秩一更新：

$$
M^{(t+1)} = M^{(t)} + \frac{\boldsymbol{v}^{(t)}(\boldsymbol{v}^{(t)})^{\mathsf T}}{(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}, \qquad \boldsymbol{v}^{(t)} = \boldsymbol{y}^{(t)} - M^{(t)}\boldsymbol{z}^{(t)}.
$$
它满足割线条件：$M^{(t+1)}\boldsymbol{z}^{(t)} = M^{(t)}\boldsymbol{z}^{(t)} + \boldsymbol{v}^{(t)} = \boldsymbol{y}^{(t)}$。通常配合回溯使用，并且必须监控分母 $(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}$：它接近零时跳过本次更新。若 $M^{(t)}$ 正定，$M^{(t+1)}$ 对称但不一定正定，因为 $(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}$ 可能为负。

最流行的更新是秩二修正 $M^{(t+1)} = M^{(t)} + a\,\boldsymbol{v}\boldsymbol{v}^{\mathsf T} + b\,\boldsymbol{u}\boldsymbol{u}^{\mathsf T}$，它使 $M^{(t+1)}$ 接近 $M^{(t)}$，同时满足割线条件并保持正定。取 $\boldsymbol{u} = \boldsymbol{y}^{(t)}$、$\boldsymbol{v} = M^{(t)}\boldsymbol{z}^{(t)}$，割线条件 $M^{(t)}\boldsymbol{z}^{(t)} + a\boldsymbol{v}(\boldsymbol{v}^{\mathsf T}\boldsymbol{z}^{(t)}) + b\,\boldsymbol{y}^{(t)}\bigl((\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}\bigr) = \boldsymbol{y}^{(t)}$ 在 $a = -1/\bigl((\boldsymbol{z}^{(t)})^{\mathsf T}M^{(t)}\boldsymbol{z}^{(t)}\bigr)$、$b = 1/\bigl((\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}\bigr)$ 时成立。

**定义 5.1.6（BFGS 更新）** **BFGS 更新**（Broyden、Fletcher、Goldfarb 与 Shanno，1970）为

$$
M^{(t+1)} = M^{(t)} - \frac{M^{(t)}\boldsymbol{z}^{(t)}\bigl(M^{(t)}\boldsymbol{z}^{(t)}\bigr)^{\mathsf T}}{(\boldsymbol{z}^{(t)})^{\mathsf T}M^{(t)}\boldsymbol{z}^{(t)}} + \frac{\boldsymbol{y}^{(t)}(\boldsymbol{y}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}. \tag{5.4}
$$

**定理 5.1.3（BFGS 保持正定性）** 设 $M^{(t)}$ 正定。则式 (5.4) 中的 $M^{(t+1)}$ 正定当且仅当曲率条件（Curvature Condition）$(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$ 成立。

**证明** 记 $M = M^{(t)}$，$\boldsymbol{z} = \boldsymbol{z}^{(t)}$，$\boldsymbol{y} = \boldsymbol{y}^{(t)}$。更新满足割线条件：$M^{(t+1)}\boldsymbol{z} = M\boldsymbol{z} - M\boldsymbol{z} + \boldsymbol{y} = \boldsymbol{y}$。必要性：若 $M^{(t+1)} \succ 0$，则 $\boldsymbol{y}^{\mathsf T}\boldsymbol{z} = \boldsymbol{z}^{\mathsf T}M^{(t+1)}\boldsymbol{z} > 0$。充分性：对 $\boldsymbol{x} \ne \boldsymbol{0}$，

$$
\boldsymbol{x}^{\mathsf T}M^{(t+1)}\boldsymbol{x} = \left(\boldsymbol{x}^{\mathsf T}M\boldsymbol{x} - \frac{(\boldsymbol{x}^{\mathsf T}M\boldsymbol{z})^2}{\boldsymbol{z}^{\mathsf T}M\boldsymbol{z}}\right) + \frac{(\boldsymbol{x}^{\mathsf T}\boldsymbol{y})^2}{\boldsymbol{y}^{\mathsf T}\boldsymbol{z}}.
$$
由内积 $\langle\boldsymbol{u}, \boldsymbol{v}\rangle_M = \boldsymbol{u}^{\mathsf T}M\boldsymbol{v}$ 的 Cauchy–Schwarz 不等式，即 $(\boldsymbol{x}^{\mathsf T}M\boldsymbol{z})^2 = \bigl((M^{1/2}\boldsymbol{x})^{\mathsf T}M^{1/2}\boldsymbol{z}\bigr)^2 \le \lVert M^{1/2}\boldsymbol{x}\rVert_2^2\lVert M^{1/2}\boldsymbol{z}\rVert_2^2$，第一个括号非负，且只在 $\boldsymbol{x} = c\boldsymbol{z}$ 时为零；第二项非负，而对 $\boldsymbol{x} = c\boldsymbol{z}$ 它等于 $c^2\boldsymbol{y}^{\mathsf T}\boldsymbol{z} > 0$。$\square$

要求曲率条件比要求 $(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$ 合理。当 $g$ 凸时，$(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} = \bigl(\nabla g(\boldsymbol{x}^{(t+1)}) - \nabla g(\boldsymbol{x}^{(t)})\bigr)^{\mathsf T}(\boldsymbol{x}^{(t+1)} - \boldsymbol{x}^{(t)}) \ge 0$，且约等于 $(\boldsymbol{z}^{(t)})^{\mathsf T}\nabla^2 g\,\boldsymbol{z}^{(t)}$；而 $(\boldsymbol{v}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} = (\boldsymbol{z}^{(t)})^{\mathsf T}\bigl(M^{(t+1)} - M^{(t)}\bigr)\boldsymbol{z}^{(t)} \approx 0$，符号不定。对强凸函数，曲率条件总成立。

**定义 5.1.7（强凸函数）** 对 $\alpha > 0$，若 $f(\boldsymbol{x}) - \frac{\alpha}{2}\lVert\boldsymbol{x}\rVert_2^2$ 在 $\operatorname{dom}(f)$ 上是凸的，则称 $f$ 是参数为 $\alpha$ 的**强凸**函数（$\alpha$-强凸）；对二阶可微的 $f$，这等价于对所有 $\boldsymbol{x}$ 有 $\nabla^2 f(\boldsymbol{x}) \succeq \alpha I$，即 $\nabla^2 f(\boldsymbol{x}) - \alpha I \succeq 0$。

**引理 5.1.1** 若 $f$ 可微且 $\alpha$-强凸，则对所有 $\boldsymbol{x}, \boldsymbol{y} \in \operatorname{dom}(f)$，

$$
f(\boldsymbol{y}) - f(\boldsymbol{x}) \ge \nabla f(\boldsymbol{x})^{\mathsf T}(\boldsymbol{y} - \boldsymbol{x}) + \frac{\alpha}{2}\lVert\boldsymbol{y} - \boldsymbol{x}\rVert_2^2.
$$
把它与交换 $\boldsymbol{x}, \boldsymbol{y}$ 后的不等式相加，得 $\bigl(\nabla f(\boldsymbol{y}) - \nabla f(\boldsymbol{x})\bigr)^{\mathsf T}(\boldsymbol{y} - \boldsymbol{x}) \ge \alpha\lVert\boldsymbol{y} - \boldsymbol{x}\rVert_2^2 > 0$（$\boldsymbol{y} \ne \boldsymbol{x}$），所以每一步都有 $(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$。若 $g$ 不是强凸的，曲率条件必须显式地强制，例如跳过更新，或用能保证它的线搜索。

**例 5.1.4（Himmelblau 函数的 BFGS）** 从 $(-4, 0)$ 出发极小化例 5.1.2 的函数，取 $M^{(0)} = I$，用减半回溯：

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

结果仍是 $\boldsymbol{x} = (3, 2)$，$g(\boldsymbol{x}) = 0$，$\nabla g(\boldsymbol{x}) = \boldsymbol{0}$。`[1]` 很重要：`t(z) %*% M %*% z` 是 $1\times1$ 矩阵，用它去除 $2\times2$ 矩阵会报错 "non-conformable arrays"。从 $(-2, -2)$ 出发，基本牛顿法到达极小值点 $(3, 2)$，而 BFGS 到达 $(-3.779310, -3.283186)$：从同一点出发的不同方法可能找到不同的局部最优。

![Himmelblau 函数的等高线（对数尺度），标出四个局部极小值点和局部极大值点。从 (-2, -2) 出发的牛顿法越过中央的山丘收敛到 (3, 2)；带回溯的 BFGS 从 (-2, -2) 下降到 (-3.779, -3.283)，从 (-4, 0) 到达 (3, 2)。](./plots/himmelblau-newton-bfgs.py)

R 函数 `optim` 默认做极小化。考虑

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

极小化 $f = -g$ 就是极大化 Himmelblau 函数 $g$，而 $g$ 无上界。BFGS（左）正确地沿 $f$ 走向 $-\infty$，却报告收敛代码 $0$；Nelder–Mead（右）停在 $g$ 唯一的局部极大值点 $(-0.2711, -0.9233)$，$g = 181.6165$。教训不在于一种方法"行"而另一种"不行"，而在于这个问题没有全局极大值，并且收敛代码 $0$ 并不保证得到了解。要用 `optim` 求极大，应极小化 $-g$ 或使用 `control = list(fnscale = -1)`。

上面的拟牛顿更新每次迭代仍要用 $M$ 解一个线性方程组（`solve(M)`），代价 $O(p^3)$；这正是该改进的一行。由于 BFGS 更新可写成 $M^{(t+1)} = A - \frac{M^{(t)}\boldsymbol{z}^{(t)}(M^{(t)}\boldsymbol{z}^{(t)})^{\mathsf T}}{(\boldsymbol{z}^{(t)})^{\mathsf T}M^{(t)}\boldsymbol{z}^{(t)}}$，其中 $A = M^{(t)} + \frac{\boldsymbol{y}^{(t)}(\boldsymbol{y}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}$，两次应用 **Sherman–Morrison 公式** $(A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T})^{-1} = A^{-1} - \frac{A^{-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1}}{1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}}$，就直接得到 $H = M^{-1}$ 的更新：

$$
H^{(t+1)} = \left(I - \frac{\boldsymbol{z}^{(t)}(\boldsymbol{y}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}\right)H^{(t)}\left(I - \frac{\boldsymbol{y}^{(t)}(\boldsymbol{z}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}\right) + \frac{\boldsymbol{z}^{(t)}(\boldsymbol{z}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}},
$$
每次迭代只需 $O(p^2)$；对严格凸的 $g$ 有 $(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$。

**定义 5.1.8（DFP 更新）** **DFP 更新**（Davidon–Fletcher–Powell，又称变尺度法）用两个对称秩一矩阵之和修正逆 Hesse 矩阵的近似：

$$
H^{(t+1)} = H^{(t)} - \frac{H^{(t)}\boldsymbol{y}^{(t)}\bigl(H^{(t)}\boldsymbol{y}^{(t)}\bigr)^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}H^{(t)}\boldsymbol{y}^{(t)}} + \frac{\boldsymbol{z}^{(t)}(\boldsymbol{z}^{(t)})^{\mathsf T}}{(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)}}. \tag{5.5}
$$

DFP 与 BFGS 互为对偶：式 (5.5) 就是式 (5.4) 中作 $M \leftrightarrow H$、$\boldsymbol{y} \leftrightarrow \boldsymbol{z}$ 的替换。割线条件 $\boldsymbol{y}^{(t)} = M^{(t+1)}\boldsymbol{z}^{(t)}$ 变为 $H^{(t+1)}\boldsymbol{y}^{(t)} = \boldsymbol{z}^{(t)}$，(5.5) 满足它：$H^{(t+1)}\boldsymbol{y}^{(t)} = H^{(t)}\boldsymbol{y}^{(t)} - H^{(t)}\boldsymbol{y}^{(t)} + \boldsymbol{z}^{(t)}$。由定理 5.1.3 的对偶形式，若 $H^{(t)}$ 正定且 $(\boldsymbol{y}^{(t)})^{\mathsf T}\boldsymbol{z}^{(t)} > 0$，则 $H^{(t+1)}$ 仍正定。DFP 是最早的拟牛顿法；实践中更偏爱 BFGS，它在非精确线搜索下更稳健。Davidon 的秩一更新不如两者流行，因为它可能失去正定性，分母也可能为零。

**算法 5.1.3（拟牛顿法）** 初始步：选一个正定矩阵 $H^{(0)}$（例如 $I$）和 $\boldsymbol{x}^*$ 的初始估计 $\boldsymbol{x}^{(0)}$；令 $t = 0$。迭代步：

1. 计算 $\nabla g(\boldsymbol{x}^{(t)})$ 和方向 $\boldsymbol{d}^{(t)} = -H^{(t)}\nabla g(\boldsymbol{x}^{(t)})$；
2. 计算 $\alpha^{(t)} = \arg\min_\alpha g(\boldsymbol{x}^{(t)} + \alpha\boldsymbol{d}^{(t)})$，或用回溯选取；
3. 令 $\boldsymbol{z}^{(t)} = \alpha^{(t)}\boldsymbol{d}^{(t)}$，$\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} + \boldsymbol{z}^{(t)}$。

更新步：计算 $\nabla g(\boldsymbol{x}^{(t+1)})$ 与 $\boldsymbol{y}^{(t)} = \nabla g(\boldsymbol{x}^{(t+1)}) - \nabla g(\boldsymbol{x}^{(t)})$，再用 DFP 或逆 BFGS 公式计算 $H^{(t+1)}$。把 $t$ 换成 $t + 1$，重复迭代步与更新步直至收敛。

### 5.1.5. 在非线性回归中的应用

#### 5.1.5.1. 置信域法

考虑 $\min_x (x^2 - 1)^2$。由于 $g'(0) = 0$，从 $0$ 出发的线搜索无法前进，尽管 $0$ 是局部极大值点。在 $0$ 处用二次函数 $m(s) = g(0) + g'(0)s + g''(0)s^2/2 = 1 - 2s^2$ 近似 $g$；为使近似可信，取 $\Delta > 0$ 并要求 $\lvert s\rvert \le \Delta$。两个解 $s = \pm\Delta$ 都能逃离这个驻点。这就是置信域的原理。

迭代优化算法要解的是容易得多的子问题。线搜索法的子问题容易，是因为它们是一维的。置信域法的子问题是 $n$ 维的，但基于更简单的目标函数，即一个线性或二次模型，它在一个简单区域（给定范数下给定半径的球）内被信任。在概念上，置信域方法用一个约束问题代替 $n$ 维无约束问题。这种替换是值得的，因为子问题不必解得很精确（近似解就够了），而且模型函数属于已经有高效专门算法的一类函数。

**定义 5.1.9（置信域法）** 由 $g(\boldsymbol{x}^{(k)} + \boldsymbol{s}) = g(\boldsymbol{x}^{(k)}) + \boldsymbol{s}^{\mathsf T}\nabla g(\boldsymbol{x}^{(k)}) + \frac12\boldsymbol{s}^{\mathsf T}H(\boldsymbol{x}^{(k)} + \tau\boldsymbol{s})\boldsymbol{s}$（某个 $\tau \in [0, 1]$），建立二次模型

$$
m^{(k)}(\boldsymbol{s}) = g(\boldsymbol{x}^{(k)}) + \boldsymbol{s}^{\mathsf T}\nabla g(\boldsymbol{x}^{(k)}) + \frac12\boldsymbol{s}^{\mathsf T}B^{(k)}\boldsymbol{s},
$$
使 $m^{(k)}(\boldsymbol{s}) - g(\boldsymbol{x}^{(k)} + \boldsymbol{s}) = O(\lVert\boldsymbol{s}\rVert^2)$；$B^{(k)}$ 可以取 Hesse 矩阵 $H(\boldsymbol{x}^{(k)})$。**置信域法**通过求解置信域子问题

$$
\min_{\boldsymbol{s}}\ m^{(k)}(\boldsymbol{s}) \quad\text{subject to}\quad \lVert\boldsymbol{s}\rVert \le \Delta^{(k)}
$$
选取步长；若模型承诺的下降被 $g(\boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)})$ 继承，就接受 $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)}$，否则令 $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)}$，并改进模型或缩小区域。

线搜索法先选下降方向 $\boldsymbol{d}^{(k)}$，再选步长 $\alpha^{(k)}$ 使 $g(\boldsymbol{x}^{(k)} + \alpha\boldsymbol{d}^{(k)})$ 下降；置信域法先选区域的大小，再同时确定步 $\boldsymbol{s}^{(k)}$ 的方向和长度。若 $B^{(k)} \succ 0$ 且无约束极小点 $\boldsymbol{s}^* = -(B^{(k)})^{-1}\nabla g(\boldsymbol{x}^{(k)})$ 满足 $\lVert\boldsymbol{s}^*\rVert \le \Delta^{(k)}$，则 $\boldsymbol{s}^{(k)} = \boldsymbol{s}^*$。因此取 $B^{(k)} = H(\boldsymbol{x}^{(k)})$ 时，只有当 Hesse 矩阵正定且牛顿步落在区域内，置信域步才是牛顿步；否则置信域步落在区域边界上，更短，方向也不同（介于牛顿方向和 $-\nabla g$ 之间）。特别地，Hesse 矩阵不定时子问题仍有解，置信域步可以利用负曲率方向，而牛顿法却会奔向鞍点或极大值点。

**算法 5.1.4（基本置信域算法）** 初始化：令 $k = 0$，$\Delta^{(0)} > 0$；凭经验选初始点 $\boldsymbol{x}^{(0)}$；固定 $\eta_v \in (0, 1)$（通常 $0.9$），$\eta_s \in (0, \eta_v)$（通常 $0.1$），$\gamma_i \ge 1$（通常 $2$），$\gamma_d \in (0, 1)$（通常 $0.5$）。重复直至收敛：

1. 建立近似 $g(\boldsymbol{x}^{(k)} + \boldsymbol{s})$ 的模型 $m^{(k)}(\boldsymbol{s})$；
2. 近似求解置信域子问题，找到满足 $m^{(k)}(\boldsymbol{s}^{(k)}) < g(\boldsymbol{x}^{(k)})$ 与 $\lVert\boldsymbol{s}^{(k)}\rVert \le \Delta^{(k)}$ 的 $\boldsymbol{s}^{(k)}$，并计算下降的质量，即实际下降与预测下降之比
   $$
   \rho^{(k)} = \frac{g(\boldsymbol{x}^{(k)}) - g(\boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)})}{m^{(k)}(\boldsymbol{0}) - m^{(k)}(\boldsymbol{s}^{(k)})};
   $$
3. 若 $\rho^{(k)} \ge \eta_v$（非常成功的一步），令 $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)}$，$\Delta^{(k+1)} = \gamma_i\Delta^{(k)}$；否则若 $\rho^{(k)} \ge \eta_s$（成功的一步），令 $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)} + \boldsymbol{s}^{(k)}$，$\Delta^{(k+1)} = \Delta^{(k)}$；否则（不成功的一步）令 $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{(k)}$，$\Delta^{(k+1)} = \gamma_d\Delta^{(k)}$；
4. $k$ 增加 $1$。

#### 5.1.5.2. 非线性回归与 Gauss–Newton 法

设我们观测了某城镇过去几年的气温。考虑到季节效应和全球变暖，假设第 $t$ 天的气温模型为 $T(t) = a\sin(\omega t + \phi) + bt$，任务是找到最拟合数据 $(t_i, T_i)$（$i = 1, \dots, n$）的参数 $a, \omega, \phi, b$，以预测未来的气温：

$$
\min_{a, \omega, \phi, b}\ \sum_{i=1}^n\bigl(T_i - a\sin(\omega t_i + \phi) - bt_i\bigr)^2.
$$
一般地，非线性回归（[3.3.6](/3.3.6)）考虑数据 $(\boldsymbol{x}_i, y_i)$ 与含未知 $\boldsymbol{\beta} \in \mathbb{R}^p$ 的曲线 $y = f(\boldsymbol{x}; \boldsymbol{\beta})$，

$$
y_i = f(\boldsymbol{x}_i; \boldsymbol{\beta}) + \varepsilon_i, \qquad r_i(\boldsymbol{\beta}) = y_i - f(\boldsymbol{x}_i; \boldsymbol{\beta}), \qquad S(\boldsymbol{\beta}) = \sum_{i=1}^n r_i(\boldsymbol{\beta})^2 = \lVert\boldsymbol{r}(\boldsymbol{\beta})\rVert^2,
$$
选取 $\boldsymbol{\beta}$ 极小化 $S$；当 $\varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$ 时，MLE 就是最小二乘估计，$\hat{\boldsymbol{\beta}}_{\mathrm{MLE}} = \hat{\boldsymbol{\beta}}_{\mathrm{OLS}} = \arg\min_{\boldsymbol{\beta}}S(\boldsymbol{\beta})$。极小值通常出现在梯度为零处，$\frac{\partial S}{\partial\beta_j} = 2\sum_i r_i\frac{\partial r_i}{\partial\beta_j} = 0$，$j = 1, \dots, p$，但这些方程一般没有闭式解，于是转向牛顿法、Nelder–Mead 法等。

本小节中 $J = J(\boldsymbol{\beta})$ 表示 $\boldsymbol{f}(\boldsymbol{\beta}) = \bigl(f(\boldsymbol{x}_1; \boldsymbol{\beta}), \dots, f(\boldsymbol{x}_n; \boldsymbol{\beta})\bigr)^{\mathsf T}$ 的 $n\times p$ Jacobi 矩阵，元素为 $\partial f(\boldsymbol{x}_i; \boldsymbol{\beta})/\partial\beta_j$，于是 $\nabla\boldsymbol{r} = -J$。则

$$
\nabla S(\boldsymbol{\beta}) = -2J(\boldsymbol{\beta})^{\mathsf T}\boldsymbol{r}(\boldsymbol{\beta}), \qquad \nabla^2 S(\boldsymbol{\beta}) = 2J(\boldsymbol{\beta})^{\mathsf T}J(\boldsymbol{\beta}) - 2\sum_{i=1}^n r_i(\boldsymbol{\beta})\nabla^2 f(\boldsymbol{x}_i; \boldsymbol{\beta}),
$$
牛顿法为

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \Bigl[J^{\mathsf T}J - \sum_{i=1}^n r_i\nabla^2 f(\boldsymbol{x}_i; \boldsymbol{\beta}^{(t)})\Bigr]^{-1}J^{\mathsf T}\boldsymbol{r}(\boldsymbol{\beta}^{(t)}).
$$
对正态误差下的 Fisher 得分法，记 $\tau = \sigma^{-2}$；略去常数，$l(\boldsymbol{\beta}, \tau) = \frac n2\log\tau - \frac\tau2 S(\boldsymbol{\beta})$，所以

$$
\nabla l(\boldsymbol{\beta}, \tau) = \begin{bmatrix}\tau J^{\mathsf T}\boldsymbol{r} \\ \frac{n}{2\tau} - \frac12S(\boldsymbol{\beta})\end{bmatrix}, \qquad \nabla^2 l(\boldsymbol{\beta}, \tau) = \begin{bmatrix}\tau\sum_i r_i\nabla^2 f_i - \tau J^{\mathsf T}J & J^{\mathsf T}\boldsymbol{r} \\ \boldsymbol{r}^{\mathsf T}J & -\frac n2\tau^{-2}\end{bmatrix},
$$
其中 $f_i = f(\boldsymbol{x}_i; \boldsymbol{\beta})$。由于 $\mathbb{E}[\boldsymbol{r}(\boldsymbol{\beta})] = \boldsymbol{0}$，$\boldsymbol{y}$ 的信息矩阵为

$$
I_n(\boldsymbol{\beta}, \tau) = \mathbb{E}[-\nabla^2 l(\boldsymbol{\beta}, \tau)] = \begin{bmatrix}\tau J^{\mathsf T}J & \boldsymbol{0} \\ \boldsymbol{0}^{\mathsf T} & \frac n2\tau^{-2}\end{bmatrix},
$$
$\boldsymbol{\beta}$ 的得分更新为 $\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + (J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r}$，在 $\boldsymbol{\beta}^{(t)}$ 处计算（因子 $\tau$ 约去）。若步子太大，就用回溯，$\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \alpha^{(t)}(J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r}$。

同样的更新不需要任何分布假设也能得到。牛顿法用 Taylor 级数近似 $S(\boldsymbol{\beta})$；Gauss–Newton 法着眼于 $f$，直接把它线性化：

$$
y_i \approx f(\boldsymbol{x}_i; \boldsymbol{\beta}^{(t)}) + \nabla f(\boldsymbol{x}_i; \boldsymbol{\beta}^{(t)})^{\mathsf T}(\boldsymbol{\beta} - \boldsymbol{\beta}^{(t)}) + \varepsilon_i, \quad\text{即}\quad \boldsymbol{r}^{(t)} \approx J^{(t)}(\boldsymbol{\beta} - \boldsymbol{\beta}^{(t)}) + \boldsymbol{\varepsilon},
$$
其中 $\boldsymbol{r}^{(t)} = \boldsymbol{r}(\boldsymbol{\beta}^{(t)})$，$J^{(t)} = J(\boldsymbol{\beta}^{(t)})$ 的行为 $\nabla f(\boldsymbol{x}_i; \boldsymbol{\beta}^{(t)})^{\mathsf T}$。这是残差对 Jacobi 矩阵的线性回归。

**定义 5.1.10（Gauss–Newton 法）** 对非线性最小二乘问题 $\min_{\boldsymbol{\beta}}\lVert\boldsymbol{y} - \boldsymbol{f}(\boldsymbol{\beta})\rVert^2$，**Gauss–Newton 法**迭代

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \bigl[(J^{(t)})^{\mathsf T}J^{(t)}\bigr]^{-1}(J^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)}, \tag{5.6}
$$
即新的猜测是 $\boldsymbol{\beta}^{(t)}$ 加上 $\boldsymbol{r}^{(t)}$ 对 $J^{(t)}$ 的无截距最小二乘回归系数，$\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \texttt{lm}(\boldsymbol{r}^{(t)} \sim J^{(t)} - 1)$。

因此可以从三个角度看 Gauss–Newton 法：它是去掉 Hesse 矩阵中麻烦的二阶项 $\sum_i r_i\nabla^2 f_i$ 的牛顿法；它是 Fisher 得分法，后者在正态假设下由 $\mathbb{E}[\boldsymbol{r}(\boldsymbol{\beta})] = \boldsymbol{0}$ 得到同一公式；它也是逐次极小化非线性最小二乘问题的线性最小二乘模型 $\min_{\boldsymbol{\beta}}\lVert\boldsymbol{r}(\boldsymbol{\beta}^{(t)}) - J(\boldsymbol{\beta}^{(t)})(\boldsymbol{\beta} - \boldsymbol{\beta}^{(t)})\rVert^2$。它不需要 Hesse 矩阵，在 $f$ 非线性不太严重时效果最好。

**命题 5.1.3** 若 $J(\boldsymbol{\beta}^{(t)})$ 列满秩，则在任何非驻点处 Gauss–Newton 步都是 $S$ 的下降方向。

**证明** 记 $\boldsymbol{d} = (J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r}$，它存在，因为 $J^{\mathsf T}J \succ 0$。则

$$
\boldsymbol{d}^{\mathsf T}\nabla S(\boldsymbol{\beta}^{(t)}) = -2\bigl[(J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r}\bigr]^{\mathsf T}J^{\mathsf T}\boldsymbol{r} = -2\boldsymbol{r}^{\mathsf T}J(J^{\mathsf T}J)^{-1}J^{\mathsf T}\boldsymbol{r} = -2\boldsymbol{r}^{\mathsf T}P_J\boldsymbol{r},
$$
其中 $P_J$ 是到 $J$ 的列空间的**正交投影矩阵**。由于 $\boldsymbol{r}^{\mathsf T}P_J\boldsymbol{r} = \lVert P_J\boldsymbol{r}\rVert^2 \ge 0$，且等号当且仅当 $J^{\mathsf T}\boldsymbol{r} = \boldsymbol{0}$，即 $\nabla S = \boldsymbol{0}$，所以在非驻点处方向导数为负。$\square$

与其他方法比较：

| | 牛顿法 | Gauss–Newton 法 |
|---|---|---|
| 导数 | 需要 $f$ 的二阶导数，即 $\nabla^2 S$ | 只需一阶导数 |
| 方向 | 不一定是下降方向（$\nabla^2 S$ 不一定正定） | $J$ 列满秩时是下降方向 |
| 速度 | 在局部极小值点附近快（二阶） | 若 $\sum_i r_i(\boldsymbol{\beta}^*)\nabla^2 f_i(\boldsymbol{\beta}^*)$ 很小，即 $f$ 在 $\boldsymbol{\beta}^*$ 附近近乎线性或残差小，则与牛顿法相近 |

与 Fisher 得分法不同，Gauss–Newton 法不需要误差的正态性假设。

**定理 5.1.4（Gauss–Newton 法的局部收敛）** 设 $M$ 是 $J$ 在极小值点 $\boldsymbol{\beta}^*$ 附近的局部 Lipschitz 常数，$J(\boldsymbol{\beta}^*)$ 列满秩，最小奇异值为 $\sigma_{\min}$，记 $\boldsymbol{\varepsilon}^{(t)} = \boldsymbol{\beta}^{(t)} - \boldsymbol{\beta}^*$。则当 $\boldsymbol{\beta}^{(t)}$ 接近 $\boldsymbol{\beta}^*$ 时近似有

$$
\lVert\boldsymbol{\varepsilon}^{(t+1)}\rVert \lesssim \frac{M\lVert\boldsymbol{r}(\boldsymbol{\beta}^*)\rVert}{\sigma_{\min}^2}\lVert\boldsymbol{\varepsilon}^{(t)}\rVert + O(\lVert\boldsymbol{\varepsilon}^{(t)}\rVert^2).
$$

因此当 $M\lVert\boldsymbol{r}(\boldsymbol{\beta}^*)\rVert < \sigma_{\min}^2$ 时局部线性收敛，零残差问题则二阶收敛；若 $\lVert\boldsymbol{r}(\boldsymbol{\beta}^*)\rVert$ 相对 $J(\boldsymbol{\beta}^*)$ 的最小奇异值很大，就没有任何保障。还可能遇到其他问题：$J^{\mathsf T}J$ 往往病态（它的**条件数**是 $J$ 的条件数的平方，所以最好用 $J$ 的 QR 分解计算这一步，[3.5.3](/3.5.3)）；远离 $\boldsymbol{\beta}^*$ 时，迭代映射可能不是压缩的。

**例 5.1.5（拟合种群模型）** 在严格控制食物供给的条件下，对各发育阶段的面粉甲虫计数了 154 天。种群增长的初等模型是**逻辑斯谛增长**，

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\left(1 - \frac NK\right),
$$
其中 $N$ 是种群规模，$t$ 是时间，$K$ 是环境的承载量，$r$ 是最大可能增长率（繁殖与死亡的净效应）。分离变量，$r\,\mathrm{d}t = \frac{K\,\mathrm{d}N}{N(K - N)} = \bigl(\frac1N - \frac{1}{N - K}\bigr)\mathrm{d}N$，时刻 $t$ 的种群规模为

$$
N_t = f(t) = \frac{KN_0}{N_0 + (K - N_0)\exp(-rt)}, \qquad N_0 = f(0).
$$
若 $N_0 < K$，则 $N_t$ 增加到 $K$ 而永不超过它。取 $N_0 = 2$，用 Gauss–Newton 法估计 $r$ 与 $K$，其中

$$
\frac{\partial N}{\partial r} = \frac{tKN_0(K - N_0)\exp(-rt)}{\bigl(N_0 + (K - N_0)\exp(-rt)\bigr)^2}, \qquad \frac{\partial N}{\partial K} = \frac{N_0^2\bigl(1 - \exp(-rt)\bigr)}{\bigl(N_0 + (K - N_0)\exp(-rt)\bigr)^2}.
$$
给定 $r$ 与 $K$ 的当前猜测：(1) 计算 $\nabla f(t_i)$ 构成 $J$；(2) 计算计数与当前预测之间的残差 $x_i^{(k)} = N_{t_i} - f(t_i; r^{(k)}, K^{(k)})$；(3) 把残差对 $J$ 回归，得到 $r$ 与 $K$ 的更新；(4) 迭代直到 $\lVert\nabla S\rVert$ 或 $\lVert\boldsymbol{x}^{\mathsf T}J\rVert$ 低于容差。

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

终止准则用梯度 $J^{\mathsf T}\boldsymbol{r}$ 而不用残差平方和，因为对不能精确拟合的模型，残差平方和不会趋于零。这里残差很大，迭代如定理 5.1.4 所预言的那样线性收敛。R 的 `nls` 默认使用 Gauss–Newton 算法。

#### 5.1.5.3. Levenberg–Marquardt–Fletcher 法

类似于线性最小二乘的**岭回归**（Tikhonov 正则化），K. Levenberg（1944）提出修改 Gauss–Newton 更新。

**定义 5.1.11（Levenberg–Marquardt 法）** **Levenberg–Marquardt 法**（阻尼最小二乘法）迭代

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \bigl[(J^{(t)})^{\mathsf T}J^{(t)} + \lambda^{(t)}I_p\bigr]^{-1}(J^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)}, \tag{5.7}
$$
其中 $\lambda^{(t)} > 0$ 是阻尼因子。

当 $\lambda \to 0^+$ 时这一步趋于 Gauss–Newton 步，收敛快但可能发散；当 $\lambda \to \infty$ 时它趋于 $\lambda^{-1}J^{\mathsf T}\boldsymbol{r} = -\frac{1}{2\lambda}\nabla S$，即很短的梯度下降步，收敛慢但更稳定。由于 $\lambda I_p$ 对所有参数一视同仁，参数（或预测变量）应当标准化。Levenberg 用固定的 $\lambda$。为了在快速收敛与数值稳定之间权衡，D. Marquardt（1963）让阻尼因子随迭代变化：收敛稳定时减小它，$\lambda^{(t+1)} \leftarrow \lambda^{(t)}/\nu$，以利用 Gauss–Newton 的快速收敛；出现发散时增大它，$\lambda^{(t+1)} \leftarrow \lambda^{(t)}\nu$，以恢复稳定。

这种方法是一种置信域方法。Gauss–Newton 步极小化 $S(\boldsymbol{\beta}^{(t)} + \boldsymbol{s})$ 的模型 $m^{(t)}(\boldsymbol{s}) = \boldsymbol{r}^{\mathsf T}\boldsymbol{r} - 2\boldsymbol{s}^{\mathsf T}J^{\mathsf T}\boldsymbol{r} + \boldsymbol{s}^{\mathsf T}J^{\mathsf T}J\boldsymbol{s}$（各量均在 $\boldsymbol{\beta}^{(t)}$ 处计算）；Marquardt 步 (5.7) 极小化 $\boldsymbol{s}^{\mathsf T}(J^{\mathsf T}J + \lambda^{(t)}I_p)\boldsymbol{s} - 2\boldsymbol{s}^{\mathsf T}J^{\mathsf T}\boldsymbol{r} + \boldsymbol{r}^{\mathsf T}\boldsymbol{r}$，它也是 Gauss–Newton 模型在约束 $\lVert\Delta\boldsymbol{\beta}^{(t)}\rVert \le \Delta^{(t)}$ 下的解，$\lambda^{(t)}$ 是 Lagrange 乘子；调整 $\lambda$ 就是调整置信域的半径。

若阻尼因子很大，$J^{\mathsf T}J$ 中的曲率信息几乎没有用上。R. Fletcher（1971）提出进一步的改进，

$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \bigl[J^{\mathsf T}J + \lambda\operatorname{diag}(J^{\mathsf T}J)\bigr]^{-1}J^{\mathsf T}\boldsymbol{r},
$$
其中 $\operatorname{diag}(J^{\mathsf T}J)$ 是由 $J^{\mathsf T}J$ 的对角元组成的对角阵。用曲率缩放梯度的各个分量，鼓励在梯度小的方向上移动得更多；这可以看作求解病态问题时的预条件步骤，并使方法对参数的缩放不变。这样得到 Levenberg–Marquardt–Fletcher（LMF）算法。

## 5.2. 梯度下降法

### 5.2.1. 一般形式

对一元函数 $f$，沿与导数符号相反的方向移动就能减小 $f(x)$：对 $f(x) = x^2/2$，$x > 0$ 时 $f'(x) > 0$，$f$ 递增，$x < 0$ 时 $f'(x) < 0$，$f$ 递减。用 $f'(x)$ 就能沿函数下坡。在多元情形，对一步 $\boldsymbol{h}^{(t)}$，$f(\boldsymbol{x}^{(t+1)}) - f(\boldsymbol{x}^{(t)}) \approx (\boldsymbol{h}^{(t)})^{\mathsf T}\nabla f(\boldsymbol{x}^{(t)})$：**梯度**是最速上升方向，当前点处的负梯度是最速下降方向。从 $\boldsymbol{x}^{(t)}$ 沿 $-\nabla f(\boldsymbol{x}^{(t)})$ 方向走，函数下降得最快（A. Cauchy，1847）。

**定义 5.2.1（梯度下降法）** **梯度下降法**迭代

$$
\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\nabla f(\boldsymbol{x}^{(t)}), \tag{5.8}
$$
步长 $\alpha^{(t)} > 0$；求极大时为 $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} + \alpha^{(t)}\nabla f(\boldsymbol{x}^{(t)})$（梯度上升）。

在每次迭代考虑展开

$$
f(\boldsymbol{y}) \approx f(\boldsymbol{x}) + \nabla f(\boldsymbol{x})^{\mathsf T}(\boldsymbol{y} - \boldsymbol{x}) + \frac12(\boldsymbol{y} - \boldsymbol{x})^{\mathsf T}\nabla^2 f(\boldsymbol{x})(\boldsymbol{y} - \boldsymbol{x}) \approx f(\boldsymbol{x}) + \nabla f(\boldsymbol{x})^{\mathsf T}(\boldsymbol{y} - \boldsymbol{x}) + \frac{1}{2\alpha}\lVert\boldsymbol{y} - \boldsymbol{x}\rVert_2^2,
$$
这个二次近似把 Hesse 矩阵 $\nabla^2 f(\boldsymbol{x})$ 换成了 $\frac1\alpha I$。选下一个点 $\boldsymbol{y} = \boldsymbol{x}^+$ 使其极小，$\boldsymbol{y} - \boldsymbol{x} = -\alpha\nabla f(\boldsymbol{x})$，恰好得到 $\boldsymbol{x}^+ = \boldsymbol{x} - \alpha\nabla f(\boldsymbol{x})$。这把三种方法统一了起来：Newton–Raphson 法、Fisher 得分法和梯度下降法都走到目标函数局部二次模型的最优点，区别只在模型的曲率矩阵：实际的 Hesse 矩阵（观测信息）、它的期望（Fisher 信息），或单位阵的倍数。

**算法 5.2.1（梯度下降）** 选初值 $\boldsymbol{x}^{(0)}$ 与容差 $\varepsilon$。对 $t = 0, 1, \dots$：令 $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\nabla f(\boldsymbol{x}^{(t)})$；若 $\lVert\boldsymbol{x}^{(t+1)} - \boldsymbol{x}^{(t)}\rVert \le \varepsilon$ 或 $\lVert\nabla f(\boldsymbol{x}^{(t)})\rVert \le \varepsilon$，停止。

步长规则有：固定步长，$\alpha^{(t)}$ 为常数；回溯线搜索；精确线搜索，即对 $\alpha$ 极小化 $h(\alpha) \triangleq f\bigl(\boldsymbol{x}^{(t)} - \alpha\nabla f(\boldsymbol{x}^{(t)})\bigr)$。

### 5.2.2. 三种线搜索方法

#### 5.2.2.1. 精确线搜索

**定义 5.2.2（精确线搜索）** **线搜索**沿给定方向选取步长；**精确线搜索**取 $\alpha^{(t)} = \arg\min_{\alpha \ge 0}f\bigl(\boldsymbol{x}^{(t)} - \alpha\nabla f(\boldsymbol{x}^{(t)})\bigr)$。

由于 $\alpha$ 沿直线极小化 $f$，由链式法则

$$
0 = \frac{\mathrm{d}}{\mathrm{d}\alpha}f(\boldsymbol{x}^{(t+1)}) = \nabla f(\boldsymbol{x}^{(t+1)})^{\mathsf T}\frac{\mathrm{d}}{\mathrm{d}\alpha}\boldsymbol{x}^{(t+1)} = -\nabla f(\boldsymbol{x}^{(t+1)})^{\mathsf T}\nabla f(\boldsymbol{x}^{(t)}):
$$
相邻梯度正交，路径以锯齿形走向极小值点。

对二次函数 $f(\boldsymbol{x}) = \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x} + c$（$A \succ 0$），$\nabla f(\boldsymbol{x}) = A\boldsymbol{x} - \boldsymbol{b}$，极小值点满足 $A\boldsymbol{x}^* = \boldsymbol{b}$。误差 $\boldsymbol{e}^{(t)} = \boldsymbol{x}^{(t)} - \boldsymbol{x}^*$ 表示离解有多远；残差 $\boldsymbol{r}^{(t)} = \boldsymbol{b} - A\boldsymbol{x}^{(t)} = -\nabla f(\boldsymbol{x}^{(t)})$ 表示离 $\boldsymbol{b}$ 有多远。注意 $\boldsymbol{r}^{(t)} = -A\boldsymbol{e}^{(t)}$（残差是变换到 $\boldsymbol{b}$ 所在空间的误差），更重要的是残差就是最速下降方向，$\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} + \alpha^{(t)}\boldsymbol{r}^{(t)}$。正交条件给出步长：

$$
0 = (\boldsymbol{r}^{(t+1)})^{\mathsf T}\boldsymbol{r}^{(t)} = \bigl(\boldsymbol{b} - A(\boldsymbol{x}^{(t)} + \alpha^{(t)}\boldsymbol{r}^{(t)})\bigr)^{\mathsf T}\boldsymbol{r}^{(t)} = (\boldsymbol{r}^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)} - \alpha^{(t)}(\boldsymbol{r}^{(t)})^{\mathsf T}A\boldsymbol{r}^{(t)} \quad\Longrightarrow\quad \alpha^{(t)} = \frac{(\boldsymbol{r}^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)}}{(\boldsymbol{r}^{(t)})^{\mathsf T}A\boldsymbol{r}^{(t)}}.
$$

#### 5.2.2.2. 回溯线搜索

沿直线精确极小化通常没有必要。考虑 $h(\alpha) = f(\boldsymbol{x} + \alpha\Delta\boldsymbol{x})$，$\Delta\boldsymbol{x} = -\nabla f(\boldsymbol{x})$。它在 $\alpha = 0$ 处的切线是 $y = f(\boldsymbol{x}) + \alpha\nabla f(\boldsymbol{x})^{\mathsf T}\Delta\boldsymbol{x}$，因为 $\frac{\mathrm{d}}{\mathrm{d}\alpha}f(\boldsymbol{x} + \alpha\Delta\boldsymbol{x}) = \nabla f(\boldsymbol{x} + \alpha\Delta\boldsymbol{x})^{\mathsf T}\Delta\boldsymbol{x}$。当 $h$ 位于这条切线的一条放平了的版本之下时，这一步就可以接受。

**定义 5.2.3（回溯线搜索）** 固定 $0 < \beta < 1$（通常在 $(0.1, 0.8)$ 内）与 $0 < c \le 1/2$。每次迭代从 $\alpha = 1$ 开始，更新 $\alpha \leftarrow \beta\alpha$，直到 **Armijo 条件**

$$
f\bigl(\boldsymbol{x}^{(k)} - \alpha\nabla f(\boldsymbol{x}^{(k)})\bigr) \le f(\boldsymbol{x}^{(k)}) - c\,\alpha\lVert\nabla f(\boldsymbol{x}^{(k)})\rVert_2^2
$$
成立；这就是**回溯线搜索**。右端是直线 $\tilde h(\alpha) = f(\boldsymbol{x}) + c\,\alpha\nabla f(\boldsymbol{x})^{\mathsf T}\Delta\boldsymbol{x}$，即斜率乘以因子 $c$ 后的切线。

这一规则自适应地选择步长，简单且在实践中往往效果很好。

#### 5.2.2.3. 固定步长

最简单的规则是对所有 $t$ 取 $\alpha^{(t)} = \alpha$。若 $\alpha$ 太大，算法可能发散；若 $\alpha$ 太小，可能很慢。对 $f(\boldsymbol{x}) = (10x_1^2 + x_2^2)/2$，$L = 10$ 是 Hesse 矩阵的最大特征值，步长 $\alpha > 2/L$ 发散，$\alpha = 1/L$ 大致合适。

![六种方法从 (2, 20) 出发求 f(x) = (10 x1^2 + x2^2)/2 的极小。上排：固定步长 0.35 发散，固定步长 0.01 走了 100 步仍离极小值点很远，固定步长 0.1 = 1/L 一步之后笔直向下。下排：β = 0.8 的回溯和精确线搜索都呈锯齿形；共轭梯度法两步到达极小值点。](./plots/gradient-descent-step-sizes.py)

**例 5.2.1** 用固定步长的最速上升法求 $f(x) = 6x - x^3$ 的极大：

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

步长为正时，迭代爬到局部极大值点 $x = \sqrt2$，$f = 4\sqrt2 = 5.656854$。步长为负时，它逆着梯度走，即做梯度下降，找到局部极小值点 $x = -\sqrt2$。两者都是驻点；步长的符号决定找到哪一种。（由于 $f$ 在两个方向上都无界，两者都不是全局最优。）

### 5.2.3. 收敛性

步长足够小时，梯度下降使 $f$ 下降。设 $f\colon \mathbb{R}^n \to \mathbb{R}$ 凸且可微，$\nabla f$ 满足常数为 $L > 0$ 的 **Lipschitz 条件**，

$$
\lVert\nabla f(\boldsymbol{x}) - \nabla f(\boldsymbol{y})\rVert_2 \le L\lVert\boldsymbol{x} - \boldsymbol{y}\rVert_2 \quad\text{对所有 }\boldsymbol{x}, \boldsymbol{y}.
$$
这是相当弱的假设，最小二乘和 logistic 回归都满足（深度神经网络局部满足）。对 $C^2$ 函数，它意味着对所有 $\boldsymbol{x}$ 有 $\nabla^2 f(\boldsymbol{x}) \preceq LI$：Hesse 矩阵的特征值以 $L$ 为上界。对最小二乘 $f(\boldsymbol{\beta}) = \frac12\lVert\boldsymbol{y} - X\boldsymbol{\beta}\rVert^2$，最小的这种 $L$ 是 $X^{\mathsf T}X$ 的最大特征值。

**定理 5.2.1（梯度下降的收敛性）** 在上述假设下，记 $\boldsymbol{x}^*$ 为极小值点：

1. 固定步长 $\alpha \le 1/L$ 的梯度下降满足 $f(\boldsymbol{x}^{(t)}) - f(\boldsymbol{x}^*) \le \dfrac{\lVert\boldsymbol{x}^{(0)} - \boldsymbol{x}^*\rVert_2^2}{2\alpha t}$；
2. 回溯线搜索（$c = 1/2$）的梯度下降满足 $f(\boldsymbol{x}^{(t)}) - f(\boldsymbol{x}^*) \le \dfrac{\lVert\boldsymbol{x}^{(0)} - \boldsymbol{x}^*\rVert_2^2}{2\alpha_{\min}t}$，其中 $\alpha_{\min} = \min\{1, \beta/L\}$；
3. 对 $f(\boldsymbol{x}) = \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x} + c$（$A \succ 0$），精确线搜索的梯度下降满足
$$
\frac{f(\boldsymbol{x}^{(t)}) - f(\boldsymbol{x}^*)}{f(\boldsymbol{x}^{(0)}) - f(\boldsymbol{x}^*)} = \frac{(\boldsymbol{e}^{(t)})^{\mathsf T}A\boldsymbol{e}^{(t)}}{(\boldsymbol{e}^{(0)})^{\mathsf T}A\boldsymbol{e}^{(0)}} \le \left(\frac{\kappa(A) - 1}{\kappa(A) + 1}\right)^{2t},
$$
其中 $\boldsymbol{e}^{(t)} = \boldsymbol{x}^{(t)} - \boldsymbol{x}^*$，$\kappa(A) = \lambda_{\max}/\lambda_{\min}$ 是 $A$ 的条件数。

**证明**（第 3 条的概要）由 $A\boldsymbol{x}^* = \boldsymbol{b}$ 得 $f(\boldsymbol{x}) - f(\boldsymbol{x}^*) = \frac12\boldsymbol{e}^{\mathsf T}A\boldsymbol{e}$，于是等式成立。由于 $A$ 对称，它有标准正交的特征向量 $\boldsymbol{v}_i$，对应**特征值** $\lambda_i$；记 $\boldsymbol{e}^{(t)} = \sum_i c_i\boldsymbol{v}_i$，则 $\boldsymbol{r}^{(t)} = -A\boldsymbol{e}^{(t)} = -\sum_i c_i\lambda_i\boldsymbol{v}_i$，且

$$
(\boldsymbol{e}^{(t)})^{\mathsf T}A\boldsymbol{e}^{(t)} = \sum_i c_i^2\lambda_i, \qquad (\boldsymbol{r}^{(t)})^{\mathsf T}\boldsymbol{r}^{(t)} = \sum_i c_i^2\lambda_i^2, \qquad (\boldsymbol{r}^{(t)})^{\mathsf T}A\boldsymbol{r}^{(t)} = \sum_i c_i^2\lambda_i^3.
$$
由 $\boldsymbol{e}^{(t+1)} = \boldsymbol{e}^{(t)} + \alpha^{(t)}\boldsymbol{r}^{(t)}$ 与精确步长 $\alpha^{(t)} = \frac{\boldsymbol{r}^{\mathsf T}\boldsymbol{r}}{\boldsymbol{r}^{\mathsf T}A\boldsymbol{r}}$，

$$
(\boldsymbol{e}^{(t+1)})^{\mathsf T}A\boldsymbol{e}^{(t+1)} = \boldsymbol{e}^{\mathsf T}A\boldsymbol{e} + 2\alpha\boldsymbol{r}^{\mathsf T}A\boldsymbol{e} + \alpha^2\boldsymbol{r}^{\mathsf T}A\boldsymbol{r} = \boldsymbol{e}^{\mathsf T}A\boldsymbol{e} - \frac{(\boldsymbol{r}^{\mathsf T}\boldsymbol{r})^2}{\boldsymbol{r}^{\mathsf T}A\boldsymbol{r}},
$$
所以比值 $\omega^2 \triangleq \frac{(\boldsymbol{e}^{(t+1)})^{\mathsf T}A\boldsymbol{e}^{(t+1)}}{(\boldsymbol{e}^{(t)})^{\mathsf T}A\boldsymbol{e}^{(t)}} = 1 - \frac{(\sum_i c_i^2\lambda_i^2)^2}{(\sum_i c_i^2\lambda_i)(\sum_i c_i^2\lambda_i^3)}$。在二维情形，取 $\lambda_1 = \kappa$、$\lambda_2 = 1$、$\mu = c_2/c_1$，它等于 $\omega^2 = 1 - \frac{(\kappa^2 + \mu^2)^2}{(\kappa + \mu^2)(\kappa^3 + \mu^2)}$；固定 $\kappa$，简单的微积分表明 $\omega^2$ 在 $\mu^2 = \kappa^2$ 时最大，此时

$$
\omega^2 = 1 - \frac{4\kappa^4}{\kappa(\kappa + 1)\cdot\kappa^2(\kappa + 1)} = \left(\frac{\kappa - 1}{\kappa + 1}\right)^2.
$$
在 $n$ 维情形，同一界由 Kantorovich 不等式得到。逐次迭代即得结论。$\square$

特征值很关键。若所有特征值相等，$\lambda_i \equiv \lambda$，则 $\boldsymbol{r}^{(t)} = -\lambda\boldsymbol{e}^{(t)}$，$\alpha^{(t)} = 1/\lambda$，$\boldsymbol{e}^{(t+1)} = \boldsymbol{e}^{(t)} + \frac1\lambda(-\lambda\boldsymbol{e}^{(t)}) = \boldsymbol{0}$：梯度下降第一次迭代就收敛。特征值相差越大，收敛越慢。

收敛阶是多少？第 1、2 条中的界像 $1/t$ 那样下降：相邻两个界之比 $\frac{t - 1}{t}$ 趋于 $1$，比任何线性速率都慢（次线性收敛）。在强凸条件 $\mu I \preceq \nabla^2 f \preceq LI$ 下收敛是线性的，因子取决于条件数 $L/\mu$，第 3 条对二次函数说明了这一点。

**定理 5.2.2（最速下降法的全局收敛性）** 设 $f\colon \mathbb{R}^n \to \mathbb{R}$ 在集合 $S = \{\boldsymbol{x} \in \mathbb{R}^n\colon f(\boldsymbol{x}) \le f(\boldsymbol{x}^{(0)})\}$ 上连续可微，且 $S$ 有界闭。则精确线搜索梯度下降产生的序列 $\{\boldsymbol{x}^{(t)}\}$ 的每个聚点 $\bar{\boldsymbol{x}}$ 都满足 $\nabla f(\bar{\boldsymbol{x}}) = \boldsymbol{0}$。

**证明** 由于 $f$ 递减，迭代点留在 $S$ 中。由**列紧性定理**，至少存在一个聚点；设 $\bar{\boldsymbol{x}}$ 是其中之一，取子列后不妨设 $\boldsymbol{x}^{(t)} \to \bar{\boldsymbol{x}}$。反设 $\nabla f(\bar{\boldsymbol{x}}) \ne \boldsymbol{0}$，令 $\bar{\boldsymbol{d}} = -\nabla f(\bar{\boldsymbol{x}})$。则存在 $\bar\alpha > 0$ 使 $\delta \triangleq f(\bar{\boldsymbol{x}}) - f(\bar{\boldsymbol{x}} + \bar\alpha\bar{\boldsymbol{d}}) > 0$。令 $\boldsymbol{d}^{(t)} = -\nabla f(\boldsymbol{x}^{(t)})$。由于 $\boldsymbol{d}^{(t)} \to \bar{\boldsymbol{d}}$，也有 $\boldsymbol{x}^{(t)} + \bar\alpha\boldsymbol{d}^{(t)} \to \bar{\boldsymbol{x}} + \bar\alpha\bar{\boldsymbol{d}}$，由连续性，当 $t$ 充分大时

$$
f(\boldsymbol{x}^{(t)} + \bar\alpha\boldsymbol{d}^{(t)}) \le f(\bar{\boldsymbol{x}} + \bar\alpha\bar{\boldsymbol{d}}) + \frac\delta2 = f(\bar{\boldsymbol{x}}) - \frac\delta2.
$$
然而，由于 $f(\boldsymbol{x}^{(t)})$ 递减地趋于 $f(\bar{\boldsymbol{x}})$，且 $\alpha^{(t)}$ 沿直线极小化 $f$，

$$
f(\bar{\boldsymbol{x}}) < f(\boldsymbol{x}^{(t)} + \alpha^{(t)}\boldsymbol{d}^{(t)}) \le f(\boldsymbol{x}^{(t)} + \bar\alpha\boldsymbol{d}^{(t)}) \le f(\bar{\boldsymbol{x}}) - \frac\delta2,
$$
矛盾。所以 $\nabla f(\bar{\boldsymbol{x}}) = \boldsymbol{0}$。$\square$

### 5.2.4. 优劣势

梯度法的优点：

- 每次迭代代价低，只需梯度而不需二阶导数；
- 对光滑、良态且强凸的目标函数可以非常快；
- 稳定：若极小值点存在，该方法保证能找到它们，尽管可能需要无穷多次迭代；许多方法在进展不足时会改用最速下降步。

缺点：

- 往往很慢（线性）：做线搜索可能很耗时，而固定的小步长可能导致收敛很差；若 Hesse 矩阵在 $\boldsymbol{x}^*$ 处的特征值相差几个数量级，可能需要极多次迭代；
- 不具有尺度不变性：改变 $\mathbb{R}^n$ 上的内积会改变梯度的概念。例如从 $x = 1/2$ 出发的 $f(x) = 4x^2$ 与从 $z = 1$ 出发的 $\tilde f(z) = z^2$ 在 $z = 2x$ 下描述同一个问题，但同样步长的梯度下降在两种参数化下产生不同的序列（每步的因子分别是 $1 - 8\alpha$ 和 $1 - 2\alpha$），而牛顿法对两者都一步求解；
- 不能处理不可微函数。

#### 5.2.4.1. 最速下降法

梯度下降是范数取 Euclid 范数时最速下降的特例。

**定义 5.2.4（最速下降方向）** 对范数 $\lVert\cdot\rVert$ 及其对偶范数 $\lVert\boldsymbol{z}\rVert_* = \sup_{\lVert\boldsymbol{x}\rVert \le 1}\boldsymbol{z}^{\mathsf T}\boldsymbol{x}$，规范化的最速下降方向为

$$
\Delta\boldsymbol{x}_{\mathrm{nsd}} = \arg\min_{\lVert\boldsymbol{v}\rVert \le 1}\nabla f(\boldsymbol{x})^{\mathsf T}\boldsymbol{v},
$$
即使 $f$ 的线性近似下降最多的单位范数步；它满足 $\nabla f(\boldsymbol{x})^{\mathsf T}\Delta\boldsymbol{x}_{\mathrm{nsd}} = -\lVert\nabla f(\boldsymbol{x})\rVert_*$。非规范化的最速下降方向为 $\Delta\boldsymbol{x}_{\mathrm{sd}} = \lVert\nabla f(\boldsymbol{x})\rVert_*\Delta\boldsymbol{x}_{\mathrm{nsd}} = \arg\min_{\boldsymbol{v}}\bigl(\nabla f(\boldsymbol{x})^{\mathsf T}\boldsymbol{v} + \frac12\lVert\boldsymbol{v}\rVert^2\bigr)$，**最速下降法**沿 $\Delta\boldsymbol{x}_{\mathrm{sd}}$ 移动。

事实上，对 $\boldsymbol{v} = k\Delta\boldsymbol{x}_{\mathrm{nsd}}$，目标为 $-k\lVert\nabla f(\boldsymbol{x})\rVert_* + \frac12k^2$，在 $k = \lVert\nabla f(\boldsymbol{x})\rVert_*$ 处取极小。对 $\ell_p$ 范数，由 Hölder 不等式 $\sum_i x_iy_i \le \lVert\boldsymbol{x}\rVert_p\lVert\boldsymbol{y}\rVert_q$，$\lVert\cdot\rVert_p$ 的对偶是 $\lVert\cdot\rVert_q$，$\frac1p + \frac1q = 1$：

- $p = 2$ 时，$\Delta\boldsymbol{x}_{\mathrm{nsd}} = -\nabla f(\boldsymbol{x})/\lVert\nabla f(\boldsymbol{x})\rVert_2$，$\Delta\boldsymbol{x}_{\mathrm{sd}} = -\nabla f(\boldsymbol{x})$：梯度下降；
- $p = 1$ 时，取 $i$ 使 $\lvert\partial f(\boldsymbol{x})/\partial x_i\rvert = \max_j\lvert\partial f(\boldsymbol{x})/\partial x_j\rvert = \lVert\nabla f(\boldsymbol{x})\rVert_\infty$；则 $\Delta\boldsymbol{x}_{\mathrm{nsd}} = -\operatorname{sgn}\bigl(\partial f(\boldsymbol{x})/\partial x_i\bigr)\boldsymbol{e}_i$，$\Delta\boldsymbol{x}_{\mathrm{sd}} = -\frac{\partial f(\boldsymbol{x})}{\partial x_i}\boldsymbol{e}_i$：沿偏导数最大的坐标走一步坐标下降（比较 [3.5.4](/3.5.4) 的坐标下降法）。

什么时候负梯度不是真正最陡的方向？当不同方向上的变化率相差很大时，这要从 Hesse 矩阵看出。对 $A \succ 0$ 定义能量范数（Energy Norm）$\lVert\boldsymbol{x}\rVert_A = (\boldsymbol{x}^{\mathsf T}A\boldsymbol{x})^{1/2}$。对二次近似 $f(\boldsymbol{x}) \approx f(\boldsymbol{x}^*) + \frac12(\boldsymbol{x} - \boldsymbol{x}^*)^{\mathsf T}A(\boldsymbol{x} - \boldsymbol{x}^*)$（$A = \nabla^2 f(\boldsymbol{x}^*)$），它是自然的范数，因为此时极小化 $f(\boldsymbol{x}^{(t)})$ 等价于极小化 $\lVert\boldsymbol{e}^{(t)}\rVert_A$。它的对偶范数是 $\lVert\cdot\rVert_{A^{-1}}$，因为 $\boldsymbol{x}^{\mathsf T}\boldsymbol{y} = (A^{1/2}\boldsymbol{x})^{\mathsf T}(A^{-1/2}\boldsymbol{y}) \le \lVert\boldsymbol{x}\rVert_A\lVert\boldsymbol{y}\rVert_{A^{-1}}$。因此

$$
\Delta\boldsymbol{x}_{\mathrm{nsd}} = \arg\min_{\lVert\boldsymbol{v}\rVert_A \le 1}\nabla f(\boldsymbol{x})^{\mathsf T}\boldsymbol{v} = -\frac{A^{-1}\nabla f(\boldsymbol{x})}{\lVert\nabla f(\boldsymbol{x})\rVert_{A^{-1}}}, \qquad \Delta\boldsymbol{x}_{\mathrm{sd}} = \lVert\nabla f(\boldsymbol{x})\rVert_{A^{-1}}\Delta\boldsymbol{x}_{\mathrm{nsd}} = -A^{-1}\nabla f(\boldsymbol{x}).
$$
取 $A = \nabla^2 f(\boldsymbol{x})$ 时这就是牛顿步：牛顿法是范数 $\lVert\cdot\rVert_{\nabla^2 f(\boldsymbol{x})}$ 下的最速下降法。

#### 5.2.4.2. 随机梯度下降

对最小二乘，$f(\boldsymbol{\beta}) = \lVert\boldsymbol{Y} - X\boldsymbol{\beta}\rVert^2 = \sum_{i=1}^n r_i^2$。若有 10,000 个数据点和 10 个特征，每个梯度需要每个 $r_i$ 对每个 $\beta_j$ 的导数，实际上每次迭代 $10{,}000 \times 10 = 100{,}000$ 次计算；常见的 1,000 次迭代就是 $10^8$ 次计算，对海量数据很慢。

**定义 5.2.5（随机梯度下降）** 对目标 $f(\boldsymbol{\beta}) = \sum_{i=1}^n f_i(\boldsymbol{\beta})$，**随机梯度下降**（SGD）每次迭代从整个数据集中随机选一个数据点 $i$，更新 $\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} - \alpha^{(t)}\nabla f_i(\boldsymbol{\beta}^{(t)})$。若每步改用一小部分随机点 $B$，$\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} - \alpha^{(t)}\frac{n}{\lvert B\rvert}\sum_{i \in B}\nabla f_i(\boldsymbol{\beta}^{(t)})$，则称为**小批量梯度下降**。

SGD 极大地减少了计算量，并且能方便地处理新加入的数据点，而不必从头开始。由于随机 $i$ 下的 $n\nabla f_i$ 是 $\nabla f$ 的无偏估计，迭代平均而言朝正确方向移动，但带有噪声；为保证收敛，步长必须递减，例如满足 $\sum_t\alpha^{(t)} = \infty$ 与 $\sum_t(\alpha^{(t)})^2 < \infty$。小批量在完整梯度下降的精度与 SGD 的速度之间取得平衡。

## 5.3. 共轭方向法

### 5.3.1. 共轭方向法

#### 5.3.1.1. 背景

最速下降法慢；牛顿法快，但需要 Hesse 矩阵的逆。共轭方向法介于两者之间：旨在加速最速下降法的收敛，同时避免牛顿法的高计算代价。它最初是为二次问题

$$
\min_{\boldsymbol{x} \in \mathbb{R}^n}\ \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x}, \qquad A \succ 0
$$
发展的，它等价于求解 $A\boldsymbol{x} = \boldsymbol{b}$。共轭方向法至多 $n$ 次迭代就能解这个问题；它可用于大到无法用直接法（如 Cholesky 分解）处理的方程组，是求解大型稀疏对称（或 Hermite）正定方程组的标准算法；它也能寻找非线性函数的极小值。

回忆这个 $f$ 的最速下降法：从 $\boldsymbol{x}^{(0)}$ 出发，走 $\boldsymbol{x}^{(t+1)} = \boldsymbol{x}^{(t)} - \alpha^{(t)}\nabla f(\boldsymbol{x}^{(t)})$，直到离 $\boldsymbol{x}^*$ 足够近；误差为 $\boldsymbol{e}^{(t)} = \boldsymbol{x}^{(t)} - \boldsymbol{x}^*$，残差为 $\boldsymbol{r}^{(t)} = \boldsymbol{b} - A\boldsymbol{x}^{(t)} = -A\boldsymbol{e}^{(t)} = -\nabla f(\boldsymbol{x}^{(t)})$。精确线搜索使 $\nabla f(\boldsymbol{x}^{(t+1)}) \perp \nabla f(\boldsymbol{x}^{(t)})$，但它常常沿与先前相同的方向走。改用一般的更新记号 $\boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k$，于是 $\boldsymbol{x}_{k+1} = \boldsymbol{x}_{k-1} + \alpha_{k-1}\boldsymbol{d}_{k-1} + \alpha_k\boldsymbol{d}_k = \cdots$。设我们选一组搜索方向，每个方向恰好走一步，步长恰到好处，使得 $n$ 步之后就完成。那么每一步也必须对之前所有方向都是最优的，即一阶最优条件

$$
0 = \frac{\mathrm{d}}{\mathrm{d}\alpha_i}f(\boldsymbol{x}_{k+1}) = \boldsymbol{d}_i^{\mathsf T}\nabla f(\boldsymbol{x}_{k+1}) = \boldsymbol{d}_i^{\mathsf T}A\boldsymbol{e}_{k+1}, \qquad i \le k
$$
必须成立：新的要求是 $\boldsymbol{e}_{k+1}$ 与各 $\boldsymbol{d}_i$ 关于 $A$ 正交。

#### 5.3.1.2. $A$-共轭

**定义 5.3.1（$A$-共轭方向）** 设 $A$ 是对称矩阵。若

$$
\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_j = 0 \qquad \text{对所有 } i \ne j,
$$
则称向量 $\boldsymbol{d}_1, \boldsymbol{d}_2, \dots, \boldsymbol{d}_k$ 是关于 $A$ 的**共轭方向**（$A$-共轭、$A$-正交，或关于 $A$ 正交）。

大多数应用中 $A$ 正定。若 $A = O$，任意两个向量都共轭；若 $A = I$，共轭就是通常的正交。一般地，$A$-共轭的向量经变换 $\boldsymbol{d} \mapsto A^{1/2}\boldsymbol{d}$ 后正交，这个变换把 $f$ 的椭圆等高线拉成圆。

#### 5.3.1.3. $A$-共轭的性质

**引理 5.3.1（线性无关）** 设 $A$ 正定。若非零向量 $\boldsymbol{d}_1, \dots, \boldsymbol{d}_k$ 是 $A$-共轭的，则它们线性无关。

**证明** 若比如 $\boldsymbol{d}_k = \alpha_1\boldsymbol{d}_1 + \cdots + \alpha_{k-1}\boldsymbol{d}_{k-1}$，则 $0 < \boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k = \boldsymbol{d}_k^{\mathsf T}A(\alpha_1\boldsymbol{d}_1 + \cdots + \alpha_{k-1}\boldsymbol{d}_{k-1}) = 0$，矛盾。$\square$

对 $A \succ 0$ 的二次问题，唯一极小值点 $\boldsymbol{x}^*$ 也是 $A\boldsymbol{x} = \boldsymbol{b}$ 的唯一解。设 $\boldsymbol{d}_0, \dots, \boldsymbol{d}_{n-1}$ 非零且 $A$-共轭。它们线性无关，所以 $\boldsymbol{x}^* = \alpha_0\boldsymbol{d}_0 + \cdots + \alpha_{n-1}\boldsymbol{d}_{n-1}$，左乘 $\boldsymbol{d}_i^{\mathsf T}A$ 得 $\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{x}^* = \alpha_i\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i$，故

$$
\alpha_i = \frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{x}^*}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i} = \frac{\boldsymbol{d}_i^{\mathsf T}\boldsymbol{b}}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}, \qquad \boldsymbol{x}^* = \sum_{i=0}^{n-1}\frac{\boldsymbol{d}_i^{\mathsf T}\boldsymbol{b}}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}\boldsymbol{d}_i.
$$
牛顿法需要求矩阵的逆；有了共轭方向，我们只需计算内积。这个展开可以看作 $n$ 步迭代过程的结果，第 $i$ 步加上 $\alpha_i\boldsymbol{d}_i$。另一个动机：记 $\boldsymbol{x} - \boldsymbol{x}_0 = \sum_{i=0}^{n-1}\alpha_i\boldsymbol{d}_i$，交叉项 $\alpha_i\alpha_j\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_j$ 消失，

$$
f(\boldsymbol{x}) = c + \sum_{i=0}^{n-1}\left[\frac12\alpha_i^2\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i + \alpha_i\boldsymbol{d}_i^{\mathsf T}(A\boldsymbol{x}_0 - \boldsymbol{b})\right]
$$
分解为 $n$ 个一维优化问题。

**定理 5.3.1（共轭方向定理）** 设 $\boldsymbol{d}_0, \dots, \boldsymbol{d}_{n-1}$ 是非零的 $A$-共轭向量，$A \succ 0$，$\boldsymbol{x}_0 \in \mathbb{R}^n$ 是任意初始点。按更新规则 $\boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k$，梯度 $\boldsymbol{g}_k \triangleq \nabla f(\boldsymbol{x}_k) = A\boldsymbol{x}_k - \boldsymbol{b}$ 以及

$$
\alpha_k = -\frac{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k} = \frac{\boldsymbol{d}_k^{\mathsf T}\boldsymbol{r}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k},
$$
$n$ 步后 $\boldsymbol{x}_n = \boldsymbol{x}^*$。

**证明** 由于 $\boldsymbol{d}_i$ 线性无关，对某些系数 $\alpha_i'$ 有 $\boldsymbol{x}^* - \boldsymbol{x}_0 = \alpha_0'\boldsymbol{d}_0 + \cdots + \alpha_{n-1}'\boldsymbol{d}_{n-1}$，而由更新规则 $\boldsymbol{x}_k = \boldsymbol{x}_0 + \alpha_0\boldsymbol{d}_0 + \cdots + \alpha_{k-1}\boldsymbol{d}_{k-1}$。所以只需证 $\alpha_k' = \alpha_k$。第一个展开左乘 $\boldsymbol{d}_k^{\mathsf T}A$ 得 $\alpha_k' = \frac{\boldsymbol{d}_k^{\mathsf T}A(\boldsymbol{x}^* - \boldsymbol{x}_0)}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k}$。由共轭性 $\boldsymbol{d}_k^{\mathsf T}A(\boldsymbol{x}_k - \boldsymbol{x}_0) = 0$，所以

$$
\boldsymbol{d}_k^{\mathsf T}A(\boldsymbol{x}^* - \boldsymbol{x}_0) = \boldsymbol{d}_k^{\mathsf T}A(\boldsymbol{x}^* - \boldsymbol{x}_k) = -\boldsymbol{d}_k^{\mathsf T}(A\boldsymbol{x}_k - \boldsymbol{b}) = -\boldsymbol{d}_k^{\mathsf T}\boldsymbol{g}_k,
$$
从而 $\alpha_k' = -\frac{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k} = \alpha_k$。$\square$

几何上，$\boldsymbol{e}_0 = \boldsymbol{x}_0 - \boldsymbol{x}^* = -\sum_{i=0}^{n-1}\alpha_i\boldsymbol{d}_i$，方法的每一步消去其中一个 $A$-正交分量。

**定理 5.3.2（扩展子空间定理）** 设 $\boldsymbol{d}_0, \dots, \boldsymbol{d}_{n-1}$ 是 $\mathbb{R}^n$ 中非零的 $A$-共轭向量，$\boldsymbol{x}_0 \in \mathbb{R}^n$ 任意，$\boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k$，$\alpha_k$ 如定理 5.3.1，$\mathcal{B}_k = \operatorname{span}\{\boldsymbol{d}_0, \dots, \boldsymbol{d}_{k-1}\} \subset \mathbb{R}^n$。则

$$
\boldsymbol{x}_k = \arg\min_{\boldsymbol{x} = \boldsymbol{x}_{k-1} + \alpha\boldsymbol{d}_{k-1},\ \alpha \in \mathbb{R}}\ \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x} = \arg\min_{\boldsymbol{x} \in \boldsymbol{x}_0 + \mathcal{B}_k}\ \frac12\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} - \boldsymbol{b}^{\mathsf T}\boldsymbol{x}.
$$

**证明** 由于 $\boldsymbol{x}_0 + \mathcal{B}_k$ 包含直线 $\boldsymbol{x}_{k-1} + \alpha\boldsymbol{d}_{k-1}$，只需证明 $\boldsymbol{x}_k$ 在 $\boldsymbol{x}_0 + \mathcal{B}_k$ 上极小化 $f$。由于 $f$ 严格凸，只需 $\boldsymbol{g}_k = \nabla f(\boldsymbol{x}_k) \perp \mathcal{B}_k$：此时对 $\boldsymbol{x}_0 + \mathcal{B}_k$ 中任意 $\boldsymbol{x} \ne \boldsymbol{x}_k$，

$$
f(\boldsymbol{x}) = f(\boldsymbol{x}_k) + \boldsymbol{g}_k^{\mathsf T}(\boldsymbol{x} - \boldsymbol{x}_k) + \frac12(\boldsymbol{x} - \boldsymbol{x}_k)^{\mathsf T}A(\boldsymbol{x} - \boldsymbol{x}_k) > f(\boldsymbol{x}_k) + \boldsymbol{g}_k^{\mathsf T}(\boldsymbol{x} - \boldsymbol{x}_k) = f(\boldsymbol{x}_k).
$$
用归纳法证明 $\boldsymbol{g}_k \perp \mathcal{B}_k$。$k = 0$ 时 $\mathcal{B}_0 = \{\boldsymbol{0}\}$。设 $\boldsymbol{g}_k \perp \mathcal{B}_k$。由于 $\boldsymbol{g}_{k+1} = A(\boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k) - \boldsymbol{b} = \boldsymbol{g}_k + \alpha_kA\boldsymbol{d}_k$，

$$
\boldsymbol{d}_k^{\mathsf T}\boldsymbol{g}_{k+1} = \boldsymbol{d}_k^{\mathsf T}\boldsymbol{g}_k - \frac{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k}\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k = 0, \qquad \boldsymbol{d}_i^{\mathsf T}\boldsymbol{g}_{k+1} = \boldsymbol{d}_i^{\mathsf T}\boldsymbol{g}_k + \alpha_k\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_k = 0 \quad (i < k),
$$
所以 $\boldsymbol{g}_{k+1} \perp \mathcal{B}_{k+1}$。$\square$

子空间 $\mathcal{B}_k$ 构成递增序列 $\mathcal{B}_{k+1} \supset \mathcal{B}_k$，且 $i < k$ 时 $\boldsymbol{g}_k \perp \boldsymbol{d}_i$（一阶最优条件 $\boldsymbol{d}_i^{\mathsf T}\nabla f(\boldsymbol{x}_{k+1}) = 0$，$i \le k$）。由于 $\boldsymbol{x}_k$ 在 $\boldsymbol{x}_0 + \mathcal{B}_k$ 上极小化 $f$，$\boldsymbol{x}_n$ 在 $\boldsymbol{x}_0 + \mathcal{B}_n = \mathbb{R}^n$ 上极小化 $f$。用能量范数表述，极小化 $f$ 就是极小化 $\lVert\boldsymbol{e}\rVert_A^2 = \sum_i\alpha_i^2\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i$，这是互相分离的各项之和；由于 $\boldsymbol{d}_k$ 在能量内积下与 $\mathcal{B}_k$ 正交，$\boldsymbol{x}_{k+1}$ 可以通过沿 $\boldsymbol{d}_k$ 极小化 $f$ 并把结果加到 $\boldsymbol{x}_k$ 上得到。

**定理 5.3.3（DFP 是共轭方向法）** 设 $f$ 是 Hesse 矩阵 $A$ 正定的二次函数，用精确线搜索运行 DFP 方法（采用更新 (5.5) 的算法 5.1.3）；记 $\boldsymbol{z}_i = \boldsymbol{x}_{i+1} - \boldsymbol{x}_i$ 为各步，$\boldsymbol{g}_i = \nabla f(\boldsymbol{x}_i)$。则对 $k \le n$，

1. 搜索向量共轭，$0 \le i < j < k$ 时 $\boldsymbol{z}_i^{\mathsf T}A\boldsymbol{z}_j = 0$；
2. $0 \le i < k$ 时 $H_kA\boldsymbol{z}_i = \boldsymbol{z}_i$：割线方程不仅沿最近的方向成立，而且沿所有之前的方向成立。

因此方法至多 $n$ 步终止，且 $H_n = A^{-1}$；第 $k$ 个方向位于 $\operatorname{span}\{H_0\boldsymbol{g}_0, \dots, H_0\boldsymbol{g}_{k-1}\}$ 中，且 $i \ne j$ 时 $\boldsymbol{g}_i^{\mathsf T}H_0\boldsymbol{g}_j = 0$。

**证明**（概要）这里 $\boldsymbol{y}_i = \boldsymbol{g}_{i+1} - \boldsymbol{g}_i = A\boldsymbol{z}_i$，$\boldsymbol{z}_i = -\alpha_iH_i\boldsymbol{g}_i$，精确线搜索给出 $\boldsymbol{z}_i^{\mathsf T}\boldsymbol{g}_{i+1} = 0$，割线方程给出 $\boldsymbol{z}_i = H_{i+1}\boldsymbol{y}_i = H_{i+1}A\boldsymbol{z}_i$。$k = 1$ 时结论成立：$H_1A\boldsymbol{z}_0 = \boldsymbol{z}_0$，且 $0 = \boldsymbol{z}_0^{\mathsf T}\boldsymbol{g}_1 = \boldsymbol{z}_0^{\mathsf T}AH_1\boldsymbol{g}_1 = -\boldsymbol{z}_0^{\mathsf T}A\boldsymbol{z}_1/\alpha_1$。归纳步中，$\boldsymbol{g}_k = \boldsymbol{g}_{i+1} + A(\boldsymbol{z}_{i+1} + \cdots + \boldsymbol{z}_{k-1})$，所以 $i < k$ 时 $\boldsymbol{z}_i^{\mathsf T}\boldsymbol{g}_k = \boldsymbol{z}_i^{\mathsf T}\boldsymbol{g}_{i+1} = 0$，进而 $0 = \boldsymbol{z}_i^{\mathsf T}AH_k\boldsymbol{g}_k = -\boldsymbol{z}_i^{\mathsf T}A\boldsymbol{z}_k/\alpha_k$；此外 $\boldsymbol{y}_k^{\mathsf T}H_kA\boldsymbol{z}_i = \boldsymbol{y}_k^{\mathsf T}\boldsymbol{z}_i = \boldsymbol{z}_k^{\mathsf T}A\boldsymbol{z}_i = 0$，所以 (5.5) 的两个修正项都把 $A\boldsymbol{z}_i$ 映为零，$H_{k+1}A\boldsymbol{z}_i = H_kA\boldsymbol{z}_i = \boldsymbol{z}_i$。最后，$n$ 个满足 $H_nA\boldsymbol{z}_i = \boldsymbol{z}_i$ 的线性无关向量迫使 $H_nA = I$。$\square$

#### 5.3.1.4. 用 Gram–Schmidt 构造共轭方向

**引理 5.3.2（Gram–Schmidt 共轭化）** 设 $\boldsymbol{v}_0, \boldsymbol{v}_1, \dots, \boldsymbol{v}_{n-1}$ 线性无关，$A \succ 0$，递归定义

$$
\boldsymbol{d}_k = \boldsymbol{v}_k - \sum_{i=0}^{k-1}\beta_{ki}\boldsymbol{d}_i, \qquad \beta_{ki} = \frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{v}_k}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}.
$$
则对所有 $j \ne k$ 有 $\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_k = 0$。

**证明** 对 $k$ 归纳；$k = 0$ 时无需证明。设对 $\{0, \dots, k - 1\}$ 中所有 $j \ne h$ 有 $\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_h = 0$。对 $j < k$，和式中只有 $i = j$ 一项留下：

$$
\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_k = \boldsymbol{d}_j^{\mathsf T}A\boldsymbol{v}_k - \sum_{i=0}^{k-1}\frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{v}_k}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_i = \boldsymbol{d}_j^{\mathsf T}A\boldsymbol{v}_k - \boldsymbol{d}_j^{\mathsf T}A\boldsymbol{v}_k = 0.
$$
$\boldsymbol{v}_i$ 的线性无关性保证没有 $\boldsymbol{d}_i$ 为零（每个 $\boldsymbol{d}_k$ 是 $\boldsymbol{v}_k$ 加上 $\boldsymbol{v}_0, \dots, \boldsymbol{v}_{k-1}$ 的组合），所以对所有 $i$ 有 $\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i > 0$。$\square$

这就是内积 $\langle\boldsymbol{u}, \boldsymbol{v}\rangle_A = \boldsymbol{u}^{\mathsf T}A\boldsymbol{v}$ 下的 **Gram–Schmidt 正交化**，从两个（或更多）线性无关向量出发。

#### 5.3.1.5. 共轭方向法与 Gauss 消元法

Gram–Schmidt 共轭化有一个缺点：它要求把之前所有的向量 $\boldsymbol{d}_i$（$i < k$）保存在内存中，所以当 $k \to n$ 时需要 $O(n^2)$ 内存（以及 $O(n^3)$ 次运算）。若 $\boldsymbol{v}_k = \boldsymbol{e}_k$ 取坐标轴单位向量，共轭方向法就是 **Gauss 消元法**。因此在共轭梯度法发现之前，共轭方向法很少使用。

考虑 $n = 2$，对称矩阵 $A = \begin{bmatrix}a_{11} & a_{12} \\ a_{21} & a_{22}\end{bmatrix}$（$a_{21} = a_{12}$），$\boldsymbol{x}_0 = \boldsymbol{0}$，$\boldsymbol{v}_0 = \boldsymbol{e}_1$，$\boldsymbol{v}_1 = \boldsymbol{e}_2$。Gram–Schmidt 共轭化给出

$$
\boldsymbol{d}_0 = \boldsymbol{e}_1, \qquad \boldsymbol{d}_1 = \boldsymbol{e}_2 - \frac{\boldsymbol{e}_1^{\mathsf T}A\boldsymbol{e}_2}{\boldsymbol{e}_1^{\mathsf T}A\boldsymbol{e}_1}\boldsymbol{e}_1 = \begin{bmatrix}l \\ 1\end{bmatrix}, \qquad l \triangleq -\frac{a_{12}}{a_{11}},
$$
且 $\boldsymbol{d}_1^{\mathsf T}\boldsymbol{b} = lb_1 + b_2$，$\boldsymbol{d}_1^{\mathsf T}A\boldsymbol{d}_1 = a_{22} + 2la_{12} + l^2a_{11} = la_{12} + a_{22}$，所以

$$
\boldsymbol{x}^* = \frac{\boldsymbol{d}_0^{\mathsf T}\boldsymbol{b}}{\boldsymbol{d}_0^{\mathsf T}A\boldsymbol{d}_0}\boldsymbol{d}_0 + \frac{\boldsymbol{d}_1^{\mathsf T}\boldsymbol{b}}{\boldsymbol{d}_1^{\mathsf T}A\boldsymbol{d}_1}\boldsymbol{d}_1 = \frac{b_1}{a_{11}}\begin{bmatrix}1 \\ 0\end{bmatrix} + \frac{lb_1 + b_2}{la_{12} + a_{22}}\begin{bmatrix}l \\ 1\end{bmatrix}.
$$
乘子 $l = -a_{21}/a_{11}$ 的 Gauss 消元把增广矩阵 $\begin{bmatrix}a_{11} & a_{12} & b_1 \\ a_{21} & a_{22} & b_2\end{bmatrix}$ 化为 $\begin{bmatrix}a_{11} & a_{12} & b_1 \\ 0 & a_{22} + la_{12} & b_2 + lb_1\end{bmatrix}$，回代得 $x_2 = \frac{lb_1 + b_2}{la_{12} + a_{22}}$，$x_1 = \frac{b_1 - a_{12}x_2}{a_{11}} = \frac{b_1}{a_{11}} + lx_2$：同一个解。一般地，第一步消元后的第二行为 $A_2^{(2)} = A_2^{(1)} - \frac{A_{2,1}^{(1)}}{A_{1,1}^{(1)}}A_1^{(1)}$，而 $A_i^{(1)} = \boldsymbol{e}_i^{\mathsf T}A$，$A_{i,j}^{(1)} = \boldsymbol{e}_i^{\mathsf T}A\boldsymbol{e}_j$，所以

$$
A_2^{(2)} = \left(\boldsymbol{e}_2 - \frac{\boldsymbol{e}_1^{\mathsf T}A\boldsymbol{e}_2}{\boldsymbol{e}_1^{\mathsf T}A\boldsymbol{e}_1}\boldsymbol{e}_1\right)^{\mathsf T}A = \boldsymbol{d}_1^{\mathsf T}A, \qquad A^{(2)} = \begin{bmatrix}\boldsymbol{d}_0^{\mathsf T} \\ \boldsymbol{d}_1^{\mathsf T}\end{bmatrix}A = L_1A, \qquad \boldsymbol{b}^{(2)} = L_1\boldsymbol{b}:
$$
消元后的矩阵由共轭 Gram–Schmidt 算法产生。比较正交方向法与沿坐标轴单位向量的共轭方向法可知，执行共轭方向法（包括共轭梯度法）相当于在一个拉伸（缩放）后的空间中执行正交方向法。

### 5.3.2. 共轭梯度法

#### 5.3.2.1. 二次问题

由扩展子空间定理，$\boldsymbol{g}_k \perp \mathcal{B}_k$，所以非零梯度 $\boldsymbol{g}_k$ 与之前的方向线性无关，可以产生新的搜索方向。在 Gram–Schmidt 共轭化中选 $\boldsymbol{v}_k = -\boldsymbol{g}_k$，结果只需 $O(n)$ 存储。

**引理 5.3.3（正交性）** 选 $\boldsymbol{d}_0 = -\nabla f(\boldsymbol{x}_0)$，对 $k = 1, \dots, n - 1$ 令

$$
\boldsymbol{d}_k = -\nabla f(\boldsymbol{x}_k) - \sum_{i=0}^{k-1}\beta_{ki}\boldsymbol{d}_i, \qquad \beta_{ki} = \frac{\boldsymbol{d}_i^{\mathsf T}A\bigl(-\nabla f(\boldsymbol{x}_k)\bigr)}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i},
$$
其中 $\boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k$，$\alpha_k$ 如定理 5.3.1。则 $j < k$ 时 $\nabla f(\boldsymbol{x}_j)^{\mathsf T}\nabla f(\boldsymbol{x}_k) = 0$ 且 $\boldsymbol{d}_j^{\mathsf T}\nabla f(\boldsymbol{x}_k) = 0$。

**证明** 注意对所有 $k$ 有 $\nabla f(\boldsymbol{x}_k) = A\boldsymbol{x}_k - \boldsymbol{b}$。对 $k$ 归纳证明对所有 $j < k$ 有 $\boldsymbol{d}_j^{\mathsf T}\nabla f(\boldsymbol{x}_k) = 0$。$k = 0$ 时显然。设它对 $k$ 成立。则对 $j < k$，

$$
\boldsymbol{d}_j^{\mathsf T}\nabla f(\boldsymbol{x}_{k+1}) = \boldsymbol{d}_j^{\mathsf T}\bigl(A(\boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k) - \boldsymbol{b}\bigr) = \boldsymbol{d}_j^{\mathsf T}\nabla f(\boldsymbol{x}_k) + \alpha_k\boldsymbol{d}_j^{\mathsf T}A\boldsymbol{d}_k = 0,
$$
因为 $\boldsymbol{d}_k$ 按构造与之前的方向 $A$-共轭（引理 5.3.2）；而 $\boldsymbol{d}_k^{\mathsf T}\nabla f(\boldsymbol{x}_{k+1}) = 0$ 是定义 $\boldsymbol{x}_{k+1}$ 的线搜索 $\min_\alpha f(\boldsymbol{x}_k + \alpha\boldsymbol{d}_k)$ 的一阶最优条件。其次，由 $\boldsymbol{d}_k$ 的定义，对所有 $k$ 有 $\operatorname{span}(\boldsymbol{d}_0, \dots, \boldsymbol{d}_k) = \operatorname{span}\bigl(\nabla f(\boldsymbol{x}_0), \dots, \nabla f(\boldsymbol{x}_k)\bigr)$。因此 $j < k$ 时存在 $c_0, \dots, c_j$ 使 $\nabla f(\boldsymbol{x}_j) = \sum_{i=0}^jc_i\boldsymbol{d}_i$，于是

$$
\nabla f(\boldsymbol{x}_j)^{\mathsf T}\nabla f(\boldsymbol{x}_k) = \sum_{i=0}^jc_i\boldsymbol{d}_i^{\mathsf T}\nabla f(\boldsymbol{x}_k) = 0. \qquad\square
$$

这里共轭意味着正交：搜索方向关于 $A$ 正交，梯度即残差 $\boldsymbol{r}_k = \boldsymbol{b} - A\boldsymbol{x}_k$ 两两正交。残差的正交性意味着对某个 $m \le n$，$\boldsymbol{x}_m$ 等于 $A\boldsymbol{x} = \boldsymbol{b}$ 的解：若对所有 $k = 0, 1, \dots, n - 1$ 都有 $\boldsymbol{x}_k \ne \boldsymbol{x}^*$，则非零的 $\boldsymbol{r}_0, \dots, \boldsymbol{r}_{n-1}$ 构成 $\mathbb{R}^n$ 的正交基，与它们全都正交的 $\boldsymbol{r}_n$ 只能是 $\boldsymbol{0}$，于是 $\boldsymbol{x}_n = \boldsymbol{x}^*$。

为什么选 $\boldsymbol{v}_k = \boldsymbol{r}_k$？残差在最速下降法中很好用，而性质 $\boldsymbol{r}_k \perp \mathcal{B}_k$ 保证非零的 $\boldsymbol{r}_k$ 总能产生一个新的、线性无关的搜索方向 $\boldsymbol{d}_k$。由于 $\boldsymbol{d}_k$ 由 $\boldsymbol{r}_k$ 构造，$\mathcal{B}_k = \operatorname{span}\{\boldsymbol{d}_0, \dots, \boldsymbol{d}_{k-1}\} = \operatorname{span}\{\boldsymbol{r}_0, \dots, \boldsymbol{r}_{k-1}\}$；又由于 $\boldsymbol{r}_k = \boldsymbol{r}_{k-1} - \alpha_{k-1}A\boldsymbol{d}_{k-1}$，$\mathcal{B}_{k+1} = \mathcal{B}_k + A\mathcal{B}_k$。因此

$$
\mathcal{B}_k = \operatorname{span}\{\boldsymbol{d}_0, A\boldsymbol{d}_0, \dots, A^{k-1}\boldsymbol{d}_0\} = \operatorname{span}\{\boldsymbol{r}_0, A\boldsymbol{r}_0, A^2\boldsymbol{r}_0, \dots, A^{k-1}\boldsymbol{r}_0\},
$$
若 $\boldsymbol{x}_0 = \boldsymbol{0}$，则 $\boldsymbol{d}_0 = \boldsymbol{r}_0 = \boldsymbol{b}$，$\mathcal{B}_k = \operatorname{span}\{\boldsymbol{b}, A\boldsymbol{b}, \dots, A^{k-1}\boldsymbol{b}\}$。

**定义 5.3.2（Krylov 子空间）** 对矩阵 $A$ 和向量 $\boldsymbol{v}$，通过把矩阵反复作用于向量而得到的子空间 $\mathcal{K}_k(A, \boldsymbol{v}) = \operatorname{span}\{\boldsymbol{v}, A\boldsymbol{v}, \dots, A^{k-1}\boldsymbol{v}\}$ 称为 **Krylov 子空间**。

这一结构减少了内存。由于 $\boldsymbol{r}_{k+1} \perp \mathcal{B}_{k+1} = \mathcal{B}_k + A\mathcal{B}_k$，向量 $\boldsymbol{r}_{k+1}$ 与 $\mathcal{B}_k$ $A$-正交，即与除 $\boldsymbol{d}_k$ 外所有之前的搜索方向 $A$-正交。Gram–Schmidt 共轭化变得简单：由 $\boldsymbol{r}_{k+1}$ 构造 $\boldsymbol{d}_{k+1}$，

$$
\boldsymbol{d}_{k+1} = \boldsymbol{r}_{k+1} - \sum_{i=0}^k\frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{r}_{k+1}}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}\boldsymbol{d}_i = \boldsymbol{r}_{k+1} - \frac{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{r}_{k+1}}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k}\boldsymbol{d}_k.
$$
利用 $A\boldsymbol{d}_k = (\boldsymbol{r}_k - \boldsymbol{r}_{k+1})/\alpha_k$ 以及 $\boldsymbol{r}_{k+1}^{\mathsf T}\boldsymbol{r}_k = 0$、$\boldsymbol{d}_k^{\mathsf T}\boldsymbol{r}_{k+1} = 0$，

$$
\frac{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{r}_{k+1}}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k} = \frac{(\boldsymbol{r}_k - \boldsymbol{r}_{k+1})^{\mathsf T}\boldsymbol{r}_{k+1}}{\boldsymbol{d}_k^{\mathsf T}(\boldsymbol{r}_k - \boldsymbol{r}_{k+1})} = -\frac{\boldsymbol{r}_{k+1}^{\mathsf T}\boldsymbol{r}_{k+1}}{\boldsymbol{d}_k^{\mathsf T}\boldsymbol{r}_k}.
$$
此外 $\boldsymbol{d}_k^{\mathsf T}\boldsymbol{r}_k = \boldsymbol{r}_k^{\mathsf T}\boldsymbol{r}_k$，因为 $\boldsymbol{d}_k = \boldsymbol{r}_k + (\boldsymbol{d}_{k-1}\text{ 的倍数})$ 且 $\boldsymbol{d}_{k-1}^{\mathsf T}\boldsymbol{r}_k = 0$；等价地，$\nabla f(\boldsymbol{x}_k)^{\mathsf T}\boldsymbol{d}_k = -\lVert\nabla f(\boldsymbol{x}_k)\rVert^2$。所以

$$
\boldsymbol{d}_{k+1} = \boldsymbol{r}_{k+1} + \frac{\boldsymbol{r}_{k+1}^{\mathsf T}\boldsymbol{r}_{k+1}}{\boldsymbol{r}_k^{\mathsf T}\boldsymbol{r}_k}\boldsymbol{d}_k, \quad\text{即}\quad \boldsymbol{d}_k = -\nabla f(\boldsymbol{x}_k) + \frac{\lVert\nabla f(\boldsymbol{x}_k)\rVert^2}{\lVert\nabla f(\boldsymbol{x}_{k-1})\rVert^2}\boldsymbol{d}_{k-1}. \tag{5.9}
$$
这就是共轭梯度法更新搜索方向的规则。

**算法 5.3.1（共轭梯度法）** 求解 $A\boldsymbol{x} = \boldsymbol{b}$（$A \succ 0$）的共轭梯度法（CG；M. Hestenes 与 E. Stiefel，1952）：选初值 $\boldsymbol{x}_0$，令 $\boldsymbol{d}_0 = \boldsymbol{r}_0 = \boldsymbol{b} - A\boldsymbol{x}_0$。对 $k = 0, 1, \dots, n - 1$：

$$
\alpha_k = \frac{\boldsymbol{r}_k^{\mathsf T}\boldsymbol{r}_k}{\boldsymbol{d}_k^{\mathsf T}A\boldsymbol{d}_k}, \quad \boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k, \quad \boldsymbol{r}_{k+1} = \boldsymbol{r}_k - \alpha_kA\boldsymbol{d}_k, \quad \boldsymbol{d}_{k+1} = \boldsymbol{r}_{k+1} + \frac{\boldsymbol{r}_{k+1}^{\mathsf T}\boldsymbol{r}_{k+1}}{\boldsymbol{r}_k^{\mathsf T}\boldsymbol{r}_k}\boldsymbol{d}_k,
$$
若 $\boldsymbol{r}_{k+1} = \boldsymbol{0}$ 则提前停止；返回 $\boldsymbol{x}^* = \boldsymbol{x}_n$。

计算 $\boldsymbol{d}_k$ 只需在内存中保存两个向量（$\boldsymbol{d}_{k-1}$ 与 $\boldsymbol{x}_k$，连同残差）和一个数（$\lVert\nabla f(\boldsymbol{x}_{k-1})\rVert^2$），计算过程中覆盖写入。方法至多 $n$ 次迭代终止；实践中 $\boldsymbol{x}_k$ 很快就非常接近 $\boldsymbol{x}^*$，其余的迭代只是精细调整。

理论上 CG 需要 $n$ 次迭代，每次需要 $\mathbb{R}^n$ 中的几个内积和一次矩阵–向量乘积 $A\boldsymbol{d}_k$。若 $A$ 稠密，乘积代价 $n^2$，总代价 $n^3$，与分解相当；收益来自稀疏的 $A$ 和提前停止。有舍入误差时，CG 作为有限步方法可能表现很差（甚至失败），但对某些 $A$（和 $\boldsymbol{b}$），它在 $\ll n$ 次迭代内给出很好的近似解。

**定理 5.3.4（CG 的收敛性）** 共轭梯度迭代收敛到 $\boldsymbol{x}^* = A^{-1}\boldsymbol{b}$，误差估计为

$$
\lVert\boldsymbol{e}_t\rVert_A \le 2\left(\frac{\sqrt{\kappa(A)} - 1}{\sqrt{\kappa(A)} + 1}\right)^t\lVert\boldsymbol{e}_0\rVert_A, \qquad \kappa(A) = \frac{\lambda_{\max}(A)}{\lambda_{\min}(A)}.
$$

对比精确线搜索的梯度下降，定理 5.2.1 给出 $\lVert\boldsymbol{e}_t\rVert_A \le \bigl(\frac{\kappa - 1}{\kappa + 1}\bigr)^t\lVert\boldsymbol{e}_0\rVert_A$：CG 把 $\kappa$ 换成了 $\sqrt\kappa$。这个界只用到了极端特征值；当 $A$ 的谱是聚集的而非分散的时候，实际收敛可以快得多。若 $A$ 只有 $m$ 个不同的特征值，在精确算术下 CG 在 $m$ 步后终止。5.2.2.3 节图的最后一幅显示 CG 两步解出一个二维二次问题，而精确线搜索呈锯齿形。

#### 5.3.2.2. 非二次问题

为极小化一般的 $f$，用 $A = \nabla^2 f(\boldsymbol{x}_k)$ 作二次近似：局部地 $\boldsymbol{g}_k = \nabla f = A\boldsymbol{x} - \boldsymbol{b}$，这与牛顿法相似，都是用二次函数近似 $f$（$\boldsymbol{b} = \nabla^2 f(\boldsymbol{x}_k)\boldsymbol{x}_k - \nabla f(\boldsymbol{x}_k)$ 的具体值并不重要）。用于非二次问题时，CG 方法通常不会在 $n$ 步内终止；$n$ 步后从当前点重新开始，再运行 $n$ 步，依此类推。

用局部 Hesse 矩阵计算 Gram–Schmidt 系数 $\beta_{ki} = \frac{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{v}_k}{\boldsymbol{d}_i^{\mathsf T}A\boldsymbol{d}_i}$，得到 Daniel（1967）的方法：

**算法 5.3.2（一般共轭梯度法）** 选 $\boldsymbol{x}_0$ 和容差 $\varepsilon$；令 $\boldsymbol{d}_0 = -\nabla f(\boldsymbol{x}_0)$。当 $\lVert\boldsymbol{d}_0\rVert > \varepsilon$ 时：对 $k = 0, 1, \dots, n - 1$，

$$
\alpha_k = -\frac{\nabla f(\boldsymbol{x}_k)^{\mathsf T}\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}\nabla^2 f(\boldsymbol{x}_k)\boldsymbol{d}_k}, \qquad \boldsymbol{x}_{k+1} = \boldsymbol{x}_k + \alpha_k\boldsymbol{d}_k,
$$
若 $k < n - 1$，令 $\beta_k = \frac{\nabla f(\boldsymbol{x}_{k+1})^{\mathsf T}\nabla^2 f(\boldsymbol{x}_k)\boldsymbol{d}_k}{\boldsymbol{d}_k^{\mathsf T}\nabla^2 f(\boldsymbol{x}_k)\boldsymbol{d}_k}$，$\boldsymbol{d}_{k+1} = -\nabla f(\boldsymbol{x}_{k+1}) + \beta_k\boldsymbol{d}_k$；然后以 $\boldsymbol{x}_0 = \boldsymbol{x}_n$、$\boldsymbol{d}_0 = -\nabla f(\boldsymbol{x}_0)$ 重新开始。

与牛顿法一样，它不需要线搜索，对二次问题有限步收敛。它的缺点是每步都要计算 Hesse 矩阵，并且一般不是全局收敛的。为避免 Hesse 矩阵，改用线搜索方法。

**定义 5.3.3（Fletcher–Reeves 方法与 Polak–Ribière 方法）** 在算法 5.3.2 中，用线搜索 $\alpha_k = \arg\min_\alpha f(\boldsymbol{x}_k + \alpha\boldsymbol{d}_k)$ 代替 $\alpha_k$，用只含梯度 $\boldsymbol{g}_k = \nabla f(\boldsymbol{x}_k)$ 的公式代替 $\beta_k$。**Fletcher–Reeves 方法**用

$$
\beta_k = \frac{\lVert\nabla f(\boldsymbol{x}_{k+1})\rVert^2}{\lVert\nabla f(\boldsymbol{x}_k)\rVert^2} = \frac{\boldsymbol{g}_{k+1}^{\mathsf T}\boldsymbol{g}_{k+1}}{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{g}_k},
$$
而 **Polak–Ribière 方法**用

$$
\beta_k = \frac{(\boldsymbol{g}_{k+1} - \boldsymbol{g}_k)^{\mathsf T}\boldsymbol{g}_{k+1}}{\boldsymbol{g}_k^{\mathsf T}\boldsymbol{g}_k}.
$$

在二次情形两者都与原始的 CG 相同，因为此时 $\boldsymbol{g}_{k+1}^{\mathsf T}\boldsymbol{g}_k = 0$。实验证据似乎更支持 Polak–Ribière 方法：当迭代停滞、$\boldsymbol{g}_{k+1} \approx \boldsymbol{g}_k$ 时，它的 $\beta_k$ 接近 $0$，下一个方向接近最速下降方向，相当于自动重启。

一般非二次问题的局部收敛是 $n$ 步二阶的，

$$
\lVert\boldsymbol{x}_{k+n} - \boldsymbol{x}^*\rVert \le c\lVert\boldsymbol{x}_k - \boldsymbol{x}^*\rVert^2, \qquad k = 0, n, 2n, 3n, \dots,
$$
因为一个完整的 $n$ 步循环解一个二次问题，类似于牛顿法的一步。线搜索方法的全局收敛性来自以下观察：每 $n$ 步走一次纯最速下降步，作为间隔步，其他步不增加目标函数。因此重启对全局收敛分析很重要，因为一般无法保证方法产生的方向 $\boldsymbol{d}_k$ 都是下降方向。

## 5.4. 三类方法的比较

与梯度下降相比，共轭梯度法实现起来只稍微复杂一点，却对二次问题有限步收敛；与牛顿法相比，它不需要求矩阵的逆。牛顿法利用曲率信息，比梯度下降走更直接的路线，代价是二阶导数和线性方程组的求解。

| 方法 | 每步代价（梯度之外） | 内存 | 收敛 | 典型用途 |
|---|---|---|---|---|
| 牛顿法 | $O(n^3)$（分解 Hesse 矩阵） | $O(n^2)$ | 二阶（局部） | 小规模、光滑问题 |
| 拟牛顿法（BFGS） | $O(n^2)$ | $O(n^2)$ | 超线性 | 中等规模 |
| 梯度下降 | $O(n)$ | $O(n)$ | 线性（常常很慢） | 大规模凸问题 |
| 共轭梯度 | 一次矩阵–向量乘积，稠密时 $O(n^2)$ | $O(n)$ | 二次问题至多 $n$ 步，速率依赖 $\sqrt\kappa$ | 大型稀疏正定方程组 |
| 随机梯度 | 每个小批量 $O(\lvert B\rvert n)$ | $O(n)$ | 次线性、有噪声 | 超大规模数据集 |

拟牛顿法要在内存中保存一个 $n\times n$ 矩阵，即 $H^{(t)}$（近似 Hesse 矩阵 $M^{(t)}$ 的逆）或 $L^{(t)}$（$M^{(t)}$ 的 Cholesky 因子），也就是 $O(n^2)$ 个数。最速下降法在任何时刻只占用 $O(n)$ 内存，保存 $\boldsymbol{x}_k$ 与 $\nabla f(\boldsymbol{x}_k)$ 并覆盖写入，因此能处理大得多的 $n$。共轭梯度法同样只需 $O(n)$ 内存，但收敛比最速下降快得多；当拟牛顿法的内存需求超出可用内存时就用它，它也用于求解正定线性方程组。

对线性方程组 $A\boldsymbol{x} = \boldsymbol{b}$，$A \in \mathbb{R}^{n\times n}$，有三类方法：

| | 稠密直接法（分解–求解） | 稀疏直接法（分解–求解） | 迭代法 |
|---|---|---|---|
| 运行时间取决于 | 只取决于规模；与数据、结构、稀疏性无关 | 规模与稀疏模式；（几乎）与数据无关 | 数据、规模、稀疏性、所需精度 |
| 适用于 | $n$ 至多几千 | $n$ 至多 $10^4$ 或 $10^5$（或更大） | $n = 10^6$ 或更大时唯一的选择 |
| 需要 | 无特殊要求 | 好的排序启发式 | 调参、预条件等 |

共轭梯度法既是直接法又是迭代法，而且不需要估计任何参数。Hestenes 与 Stiefel 于 1952 年把它作为直接法发表：至多 $n$ 次迭代求得精确解。大约 30 年后人们才真正认识到它的迭代性质：收敛分析表明 $\lVert\boldsymbol{x}_k - \boldsymbol{x}^*\rVert_A$ 通常很快变小，因此可以在 $k$ 远小于 $n$ 时停止迭代。正是这种快速收敛（速率由条件数的平方根控制），使 CG 成为求解大型稀疏线性方程组的首选方法。

## 小结

- Newton–Raphson 法：二阶收敛；需要梯度和 Hesse 矩阵；对初值敏感；Hesse 矩阵不定时可能发散。弦截法用差商代替二阶导数，以约 $1.618$ 的阶超线性收敛。
- Fisher 得分法用期望信息代替观测信息，期望信息正定；它更稳定，收敛半径更大。对典范指数族（典范联系）它与牛顿法一致，对 GLM 它就是迭代重加权最小二乘。
- 牛顿法的改进：用回溯线搜索控制步长；离散牛顿法（Hesse 矩阵的差分近似）；满足割线条件的拟牛顿更新，Davidon（秩一）、BFGS 与 DFP（秩二，互为对偶，曲率条件下保持正定），不需要 Hesse 矩阵，逆形式下也不需要解方程组。三种线搜索是精确、回溯和固定步长；置信域法先确定区域大小，再确定步。
- 非线性回归：Gauss–Newton 法用 Jacobi 矩阵近似 Hesse 矩阵，不需要二阶导数，在正态误差下与 Fisher 得分法一致，残差小时收敛快；Levenberg–Marquardt–Fletcher 法加入阻尼，在 Gauss–Newton 与梯度下降之间插值，对病态问题稳健。
- 梯度下降：每步便宜，线性（或次线性）收敛，锯齿现象，对条件数敏感，不具尺度不变性。牛顿法是 Hesse 范数下的最速下降。SGD 与小批量降低大数据上的计算量。
- 共轭方向：对 $A \succ 0$ 的二次函数，$A$-共轭方向至多 $n$ 步给出解；梯度与已探索的子空间正交（扩展子空间定理）；Gram–Schmidt 构造共轭方向，取单位向量时就是 Gauss 消元。共轭梯度由残差构造方向，只需 $O(n)$ 存储，收敛速率依赖 $\sqrt\kappa$，谱聚集时更快，并通过 Fletcher–Reeves 与 Polak–Ribière 方法推广到非二次问题。
