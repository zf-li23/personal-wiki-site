## 5.1 概率分布函数

### 5.1.1 为什么需要分布函数？
- **目标**：完整刻画一个随机变量的信息。
- **已有工具局限性**：概率质量函数（PMF）和概率密度函数（PDF）仅适用于特定类型随机变量，而分布函数（CDF）适用于所有随机变量，提供统一描述。

### 5.1.2 分布函数的定义
对随机变量 $X$，其累积分布函数（CDF）定义为：
$$
F(x) = \mathbb{P}(X \leq x), \quad x \in \mathbb{R}
$$
其中 $\mathbb{P}$ 是概率测度。

### 5.1.3 CDF 与 PMF/PDF 的关系
- **离散型随机变量**：若 $X$ 有 PMF $p_k = \mathbb{P}(X = x_k)$，则 CDF 为：
  $$
  F(x) = \sum_{j: x_j \leq x} p_j
  $$
  CDF 是单调不减的阶梯函数，在 $x_j$ 处跳跃 $p_j$。

- **连续型随机变量**：若 $X$ 有 PDF $f(x)$，则 CDF 为：
  $$
  F(x) = \int_{-\infty}^{x} f(t) \, dt
  $$
  在 $f(x)$ 的连续点处，有 $f(x) = F'(x)$。

### 5.1.4 分布函数的性质
- **单调性**：$F(x)$ 单调非降。
- **极限行为**：
  $$
  \lim_{x \to -\infty} F(x) = 0, \quad \lim_{x \to \infty} F(x) = 1
  $$
- **连续性**：$F(x)$ 右连续。若 $\mathbb{P}(X = x) = 0$ 对所有 $x$ 成立，则 $F(x)$ 连续。

### 5.1.5 分布函数的功能
- **统一性**：适用于所有随机变量，便于研究离散与连续随机变量之间的关系（如几何分布与指数分布的近似）。
- **类型判断**：若 $F(x)$ 不连续，则 $X$ 非连续型；若 $F(x)$ 连续且导数存在，可通过导数得到 PDF。

### 5.1.6 例子
- **标准正态分布**：CDF 为 $\Phi(x) = \int_{-\infty}^{x} \varphi(t) \, dt$，其中 $\varphi(t) = \frac{1}{\sqrt{2\pi}} e^{-t^2/2}$。性质：$\Phi(-x) = 1 - \Phi(x)$。
- **一般正态分布**：若 $X \sim N(\mu, \sigma^2)$，则：
  $$
  \mathbb{P}(X \leq a) = \Phi\left( \frac{a - \mu}{\sigma} \right)
  $$
- **$3\sigma$ 原则**：
  $$
  \mathbb{P}(|X - \mu| \leq \sigma) \approx 68.27\%, \quad \mathbb{P}(|X - \mu| \leq 3\sigma) \approx 99.73\%
  $$

## 5.2 随机变量函数的分布

### 5.2.1 离散型随机变量的函数
- **方法**：对 $Y = g(X)$，直接计算 $Y$ 的 PMF。

### 5.2.2 连续型随机变量的函数

- **一般方法**：
  1. 求 $Y$ 的 CDF：$F_Y(y) = \mathbb{P}(Y \leq y)$。
  2. 求导得 PDF：$f_Y(y) = \frac{d}{dy} F_Y(y)$。

- **线性变换**：若 $Y = aX + b$，则：
  $$
  f_Y(y) = \frac{1}{|a|} f_X\left( \frac{y - b}{a} \right)
  $$
  例如，若 $X \sim N(\mu, \sigma^2)$，则 $Y = aX + b \sim N(a\mu + b, a^2\sigma^2)$。

- **严格单调函数**：若 $Y = g(X)$，$g$ 严格单调且可逆，则：
  $$
  f_Y(y) = f_X(h(y)) \left| h'(y) \right|
  $$
  其中 $h$ 是 $g$ 的逆函数。

- **一般非单调函数**：若 $Y = g(X)$，且对 $y \in D$，有 $n$ 个逆函数 $h_i(y)$，则：
  $$
  f_Y(y) = \sum_{i=1}^{n} f_X(h_i(y)) \left| h_i'(y) \right|
  $$

### 5.2.3 Gamma 分布
- **定义**：$X \sim \Gamma(\alpha, \lambda)$ 的 PDF 为：
  $$
  f(x) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}, \quad x \geq 0
  $$
  其中 $\Gamma(\alpha) = \int_{0}^{\infty} x^{\alpha-1} e^{-x} \, dx$。
- **性质**：
  - $\Gamma(n) = (n-1)!$ 对正整数 $n$。
  - $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$。
  - $\Gamma(1/2) = \sqrt{\pi}$。
- **特例**：
  - $\alpha = 1$：指数分布。
  - $\alpha$ 为正整数：Erlang 分布。

## 小结

### 核心知识点
- **分布函数（CDF）**：统一描述随机变量的工具，适用于所有类型。定义 $F(x) = \mathbb{P}(X \leq x)$，具有单调性、极限行为和右连续性。
- **CDF 与 PMF/PDF 的关系**：
  - 离散型：$F(x) = \sum_{j: x_j \leq x} p_j$。
  - 连续型：$F(x) = \int_{-\infty}^{x} f(t) \, dt$，$f(x) = F'(x)$。
- **随机变量函数的分布**：
  - 离散型：直接计算 PMF。
  - 连续型：通过 CDF 求导或使用变换公式（如线性变换、单调函数）。

### 应用技巧
- **变量变换**：利用 $Y = g(X)$ 的单调性简化计算，避免直接积分。
- **分布识别**：通过函数形式判断分布类型（如 $X^2$ 对于正态分布得到 Gamma 分布）。
- **归一化原则**：在推导 PDF 时，确保积分结果为 1。

### 关键公式总结
- CDF 定义：$F(x) = \mathbb{P}(X \leq x)$
- 离散型 CDF：$F(x) = \sum_{j: x_j \leq x} p_j$
- 连续型 CDF：$F(x) = \int_{-\infty}^{x} f(t) \, dt$
- 线性变换：$f_Y(y) = \frac{1}{|a|} f_X\left( \frac{y - b}{a} \right)$
- 单调变换：$f_Y(y) = f_X(h(y)) \left| h'(y) \right|$
- Gamma 分布 PDF：$f(x) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}$
