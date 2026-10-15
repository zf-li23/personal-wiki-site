---
title: 期望、方差、相关不等式
---

## 8.1. 数学期望

### 8.1.1. 期望的定义

#### 8.1.1.1. 离散型随机变量
设 $X$ 有概率分布 $\mathbb{P}(X = x_j), j = 1, 2, \dots$，如果 $\sum_{j=1}^\infty |x_j| \mathbb{P}(X = x_j) < +\infty$，则：
$$
\mathbb{E}(X) = \sum_{j=1}^\infty x_j \mathbb{P}(X = x_j)
$$

#### 8.1.1.2. 连续型随机变量
设 $X$ 有概率密度 $f(x)$，如果 $\int_{-\infty}^{\infty} |x| f(x) \mathrm{d}x < +\infty$，则：
$$
\mathbb{E}(X) = \int_{-\infty}^{\infty} x f(x) \mathrm{d}x
$$

### 8.1.2. 常见分布的期望

- **两点分布** $B(1, p)$：$\mathbb{E}(X) = p$
- **二项分布** $B(n, p)$：$\mathbb{E}(X) = np$
- **泊松分布** $\mathcal{P}(\lambda)$：$\mathbb{E}(X) = \lambda$
- **几何分布** $G(p)$：$\mathbb{E}(X) = \frac{1}{p}$
- **均匀分布** $U(a, b)$：$\mathbb{E}(X) = \frac{a+b}{2}$
- **指数分布** $\varepsilon(\lambda)$：$\mathbb{E}(X) = \frac{1}{\lambda}$
- **Gamma分布** $\Gamma(\alpha, \beta)$：$\mathbb{E}(X) = \frac{\alpha}{\beta}$
- **正态分布** $N(\mu, \sigma^2)$：$\mathbb{E}(X) = \mu$

### 8.1.3. 期望的性质

**定理**：设 $E|X| < +\infty, E|Y| < +\infty$，$a, b, C$ 为实数，则：
1. $\mathbb{E}(C) = C$
2. $|\mathbb{E}X| \leq E|X|$
3. $\mathbb{E}(aX + bY) = aEX + bEY$（线性性）
4. 若 $X \leq Y$ a.s.，则 $\mathbb{E}X \leq \mathbb{E}Y$
5. 若 $X$ 和 $Y$ 独立，则 $\mathbb{E}(XY) = (\mathbb{E}X)(\mathbb{E}Y)$

## 8.2. 随机变量函数的数学期望

### 8.2.1. 基本定理
设 $X = (X_1, X_2, \dots, X_n)$ 是随机向量，$g(x)$ 是实函数，如果 $\int_{\mathbb{R}^n} |g(x)| \mathrm{d}F(x) < \infty$，则：
$$
\mathbb{E}(g(X)) = \int_{\mathbb{R}^n} g(x) \mathrm{d}F(x)
$$

### 8.2.2. 应用实例

**例 8.2.1**：$X \sim U(0, \pi/2)$，计算 $\mathbb{E}(\cos(X))$
$$
\mathbb{E}(\cos(X)) = \int_{0}^{\frac{\pi}{2}} \frac{2}{\pi} \cos(x) \mathrm{d}x = \frac{2}{\pi}
$$

**例 8.2.2**：$(X, Y)$ 在单位圆内均匀分布，计算 $\mathbb{E}(X)$
$$
\mathbb{E}(X) = \frac{1}{\pi} \int_{-1}^{1} \left( \int_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}} x \mathrm{d}x \right) \mathrm{d}y = 0
$$

## 8.3. 方差

### 8.3.1. 定义与性质

**定义**：设 $\mu = \mathbb{E}X$ 有限，则方差为：
$$
\operatorname{Var}(X) = \mathbb{E}(X - \mu)^2
$$

**等价计算公式**：
$$
\operatorname{Var}(X) = \mathbb{E}(X^2) - (\mathbb{E}X)^2
$$

**性质**：

1. $\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X)$
2. $\operatorname{Var}(X) = \mathbb{E}(X - \mu)^2 \leq \mathbb{E}(X - c)^2, \forall c \in \mathbb{R}$
3. $\operatorname{Var}(X) = 0 \iff X = \mu$ a.s.
4. 若 $X_1, \dots, X_n$ 相互独立，则 $var\left(\sum_{k=1}^n X_k\right) = \sum_{k=1}^n \operatorname{Var}(X_k)$

### 8.3.2. 常见分布的方差

- **两点分布** $B(1, p)$：$\operatorname{Var}(X) = p(1-p)$
- **二项分布** $B(n, p)$：$\operatorname{Var}(X) = np(1-p)$
- **泊松分布** $\mathcal{P}(\lambda)$：$\operatorname{Var}(X) = \lambda$
- **几何分布** $G(p)$：$\operatorname{Var}(X) = \frac{1-p}{p^2}$
- **均匀分布** $U(a, b)$：$\operatorname{Var}(X) = \frac{(b-a)^2}{12}$
- **指数分布** $\varepsilon(\lambda)$：$\operatorname{Var}(X) = \frac{1}{\lambda^2}$
- **正态分布** $N(\mu, \sigma^2)$：$\operatorname{Var}(X) = \sigma^2$
- **Gamma分布** $\Gamma(\alpha, \beta)$：$\operatorname{Var}(X) = \frac{\alpha}{\beta^2}$

### 8.3.3. 标准化

**定义**：设 $\operatorname{Var}(X) < \infty$，令：
$$
Y = \frac{X - \mathbb{E}X}{\sqrt{var(X)}}
$$
则 $\mathbb{E}Y = 0, \operatorname{Var}(Y) = 1$，称 $Y$ 是 $X$ 的标准化。

## 8.4. 高阶矩

### 8.4.1. 定义
设 $X$ 是随机变量，$m$ 是正整数：
- **m阶原点矩**：$\mathbb{E}(X^m)$
- **m阶中心矩**：$\mathbb{E}(X - \mathbb{E}X)^m$

### 8.4.2. 重要高阶矩
- **偏度**（Skewness）：$\frac{E(X-\mathbb{E}X)^3}{[\mathbb{E}(X-\mathbb{E}X)^2]^{3/2}}$
- **峰度**（Kurtosis）：$\frac{E(X-\mathbb{E}X)^4}{[\mathbb{E}(X-\mathbb{E}X)^2]^2} - 3$

## 8.5. 相关不等式

### 8.5.1. Markov不等式
对随机变量 $X$ 和 $\varepsilon > 0$，有：
$$
\mathbb{P}(|X| \geq \varepsilon) \leq \frac{E |X|^{\alpha}}{\varepsilon^{\alpha}}, \\quad \alpha > 0
$$

### 8.5.2. Chebyshev不等式
$$
\mathbb{P}(|X - \mathbb{E}X| \geq \varepsilon) \leq \frac{var(X)}{\varepsilon^2}
$$

### 8.5.3. Cauchy-Schwarz不等式
设 $\mathbb{E}X^2 < \infty$ 和 $\mathbb{E}Y^2 < \infty$，则：
$$
|\mathbb{E}(XY)| \leq \sqrt{EX^2\mathbb{E}Y^2}
$$
等号成立当且仅当存在不全为零的常数 $a, b$ 使得 $aX + bY = 0$ a.s.

### 8.5.4. Jensen不等式
设 $\psi$ 是凸函数，且 $X$ 和 $\psi(X)$ 都有有限的期望，则：
$$
\psi(\mathbb{E}X) \leq \mathbb{E}(\psi(X))
$$
对于严格凸函数，等号成立当且仅当 $X = \mathbb{E}X$ a.s.

## 小结

### 核心知识点
- **数学期望**：随机变量的加权平均值，反映分布的中心位置
- **方差**：衡量随机变量与其期望的偏离程度
- **高阶矩**：描述分布形态特征（偏度、峰度）
- **不等式**：提供概率界限和关系约束

### 关键公式
- 期望：$\mathbb{E}(X) = \sum x_j \mathbb{P}(X=x_j)$ 或 $\int x f(x) \mathrm{d}x$
- 方差：$\operatorname{Var}(X) = \mathbb{E}(X^2) - (\mathbb{E}X)^2$
- Markov不等式：$\mathbb{P}(|X| \geq \varepsilon) \leq \frac{E |X|^{\alpha}}{\varepsilon^{\alpha}}$
- Chebyshev不等式：$\mathbb{P}(|X-\mathbb{E}X| \geq \varepsilon) \leq \frac{var(X)}{\varepsilon^2}$

### 应用技巧
- **线性性质**：简化复杂随机变量期望的计算
- **示性函数**：建立概率与期望的连接
- **对称性**：利用分布对称性简化计算
- **标准化**：使不同量纲的随机变量具有可比性
