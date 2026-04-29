## 13b.1 收敛模式定义

### 13b.1.1 依分布收敛

**定义 13b.1.1（依分布收敛）**
设 $Y_n, Y$ 的分布函数分别为 $F_n(x), F(x)$。如果在 $F(x)$ 的连续点 $x$，有
$$
\lim_{n \to \infty} F_n(x) = F(x)
$$
则称 $Y_n$ 依分布收敛到 $Y$，记作 $Y_n \overset{d}{\to} Y$。

### 13b.1.2 几乎处处收敛

**定义 13b.1.2（几乎处处收敛）**
如果
$$
\mathbb{P}(\lim_{n \to \infty} X_n = X) = 1
$$
则称 $X_n$ 几乎处处收敛到 $X$，记作 $X_n \overset{a.s.}{\to} X$。

**等价表述**
对 $\forall \varepsilon > 0$：
$$
\left\{ \lim_{n \to \infty} X_n = X \right\} = \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} \{ |X_k - X| < \varepsilon \}
$$

### 13b.1.3 依概率收敛

**定义 13b.1.3（依概率收敛）**
如果对 $\forall \varepsilon > 0$，有
$$
\lim_{n \to \infty} \mathbb{P}(|X_n - X| \geq \varepsilon) = 0
$$
则称 $X_n$ 依概率收敛到 $X$，记作 $X_n \overset{p}{\to} X$。

**等价表述**
令 $A_n = \{ |X_n - X| < \varepsilon \}$，则：
$$
\lim_{n \to \infty} \mathbb{P}(A_n) = 1
$$

### 13b.1.4 收敛模式对比

| 收敛类型     | 记号                        | 定义                                         |
| ------------ | --------------------------- | -------------------------------------------- |
| 依分布收敛   | $X_n \overset{d}{\to} X$    | 在 $F(x)$ 连续点，$\lim F_n(x) = F(x)$       |
| 依概率收敛   | $X_n \overset{p}{\to} X$    | $\forall \varepsilon > 0$，$\lim \mathbb{P}( | X_n - X | \geq \varepsilon) = 0$ |
| 几乎处处收敛 | $X_n \overset{a.s.}{\to} X$ | $\mathbb{P}(\lim X_n = X) = 1$               |

## 13b.2 收敛性关系

### 13b.2.1 基本关系

**定理 13b.2.1（收敛性强弱关系）**
$$
X_n \overset{a.s.}{\to} X \Rightarrow X_n \overset{p}{\to} X \Rightarrow X_n \overset{d}{\to} X
$$

### 13b.2.2 几乎处处收敛推依概率收敛

**定理 13b.2.2**
如果 $X_n \overset{a.s.}{\to} X$，则 $X_n \overset{p}{\to} X$。

**证明思路**
利用集合关系：
$$
\left\{ \lim_{n \to \infty} X_n = X \right\} = \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} \{ |X_k - X| < \varepsilon \}
$$
通过概率的连续性可得结论。

### 13b.2.3 依概率收敛推依分布收敛

**定理 13b.2.3**
如果 $X_n \overset{p}{\to} X$，则 $X_n \overset{d}{\to} X$。

**证明思路**
通过构造不等式：
$$
F(x-\varepsilon) - \mathbb{P}(|X_n - X| > \varepsilon) \leq F_n(x) \leq F(x+\varepsilon) + \mathbb{P}(|X_n - X| > \varepsilon)
$$
令 $n \to \infty$ 和 $\varepsilon \to 0$ 可得结论。

### 13b.2.4 常数情形的等价性

**定理 13b.2.4**
若 $C$ 为常数，则：
$$
X_n \overset{d}{\to} C \Leftrightarrow X_n \overset{p}{\to} C
$$

## 13b.3 反例分析

### 13b.3.1 依分布收敛不蕴含依概率收敛

**例 13b.3.1**
设 $\{X_n\}$ 独立同分布 $\sim N(0,1)$，则 $X_n \overset{d}{\to} X_1$，但：
$$
\mathbb{P}(|X_n - X_1| > 1) = \mathbb{P}\left( |X_1| > \frac{1}{\sqrt{2}} \right) > 0
$$
不满足依概率收敛。

### 13b.3.2 依概率收敛不蕴含几乎处处收敛

**例 13b.3.2**
设 $\{X_n\}$ 独立，且：
$$
\mathbb{P}(X_n = 0) = 1 - n^{-1}, \quad \mathbb{P}(X_n = 1) = n^{-1}
$$
则 $X_n \overset{p}{\to} 0$，但由 Borel-Cantelli 引理，$X_n$ 不几乎处处收敛到 $0$。

## 13b.4 常用定理

### 13b.4.1 连续映射定理

**定理 13b.4.1（连续映射定理）**
设 $g$ 连续，则：
1. $X_n \overset{a.s.}{\to} X \Rightarrow g(X_n) \overset{a.s.}{\to} g(X)$
2. $X_n \overset{p}{\to} X \Rightarrow g(X_n) \overset{p}{\to} g(X)$  
3. $X_n \overset{d}{\to} X \Rightarrow g(X_n) \overset{d}{\to} g(X)$

### 13b.4.2 Slutsky 定理

**定理 13b.4.2（Slutsky 定理）**
假设 $X_n \overset{d}{\to} X$，$Y_n \overset{p}{\to} c$（常数），则：
1. $X_n + Y_n \overset{d}{\to} X + c$
2. $X_n Y_n \overset{d}{\to} cX$
3. $X_n / Y_n \overset{d}{\to} X / c$（$c \neq 0$）

### 13b.4.3 Delta 方法

**定理 13b.4.3（Delta 方法）**
假设 $\sqrt{n}(X_n - a) \overset{d}{\to} N(0, V)$，$g$ 连续可导，则：
$$
\sqrt{n}(g(X_n) - g(a)) \overset{d}{\to} N(0, (g'(a))^2 V)
$$

### 13b.4.4 连续性定理

**定理 13b.4.4（连续性定理）**
$X_n \overset{d}{\to} X$ 的充分必要条件是：
$$
\lim_{n \to \infty} \phi_n(t) = \phi(t), \quad \forall t \in \mathbb{R}
$$
其中 $\phi_n(t), \phi(t)$ 分别为 $X_n, X$ 的特征函数。

### 13b.4.5 Cramér-Wold 方法

**定理 13b.4.5（Cramér-Wold）**
$X_n \overset{d}{\to} X$ 的充分必要条件是对任意常数向量 $a$，有：
$$
a^T X_n \overset{d}{\to} a^T X
$$

## 13b.5 定理应用

### 13b.5.1 分布收敛证明
- $t$ 分布收敛到正态分布
- 二项分布收敛到泊松分布
- 辛钦大数定律的证明

### 13b.5.2 统计推断
- Delta 方法在渐近方差计算中的应用
- Slutsky 定理在构造统计量中的应用

## 小结

### 核心知识点
- 三种主要收敛模式的定义和直观理解
- 收敛性之间的强弱关系：几乎处处收敛 $\Rightarrow$ 依概率收敛 $\Rightarrow$ 依分布收敛
- 常数情形下依分布收敛与依概率收敛的等价性

### 关键定理
- 连续映射定理：保持各种收敛性
- Slutsky 定理：混合收敛模式下的运算
- 连续性定理：用特征函数判断依分布收敛
- Delta 方法：函数变换后的渐近分布

### 重要技巧
- 用反例理解不同收敛性的本质差异
- 特征函数在证明依分布收敛中的应用
- Cramér-Wold 方法将高维问题化为一维问题

### 理论意义
收敛性理论为概率论的极限定理提供了严格的数学基础，是大样本理论和统计推断的重要工具，建立了随机现象与确定性规律之间的联系。
