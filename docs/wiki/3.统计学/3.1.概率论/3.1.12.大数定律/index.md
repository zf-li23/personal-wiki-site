## 12.1 基本概念

### 12.1.1 问题背景
样本均值估计总体均值的可靠性问题：

$$
M_n = \frac{1}{n} \sum_{i=1}^n X_i \quad \text{vs} \quad EX_1
$$

其中 $\{X_n\}$ 是独立同分布的随机变量序列。

## 12.2 基本定理

### 12.2.1 弱大数定律

**定理 12.2.1（弱大数定律）**
设 $\{X_n\}$ 是独立同分布的随机变量序列，且 $var(X_1) < \infty$，则对任意 $\varepsilon > 0$：

$$
\lim_{n \to \infty} \mathbb{P}\left( \left| \frac{1}{n} \sum_{i=1}^n X_i - EX_1 \right| \geq \varepsilon \right) = 0
$$

记作：

$$
\frac{1}{n} \sum_{k=1}^n X_k \overset{p}{\to} EX_1
$$

### 12.2.2 证明方法
基于切比雪夫不等式：

$$
\mathbb{P}(|X - EX| \geq \varepsilon) \leq \frac{var(X)}{\varepsilon^2}
$$

## 12.3 理论深化

### 12.3.1 条件的放宽

**定理 12.3.1（辛钦大数定律）**
设 $\{X_n\}$ 是独立同分布序列，且 $E|X_1| < \infty$，则：
$$
\frac{1}{n} \sum_{k=1}^n X_k \overset{p}{\rightarrow} EX_1
$$

**定理 12.3.2（弱大数定律一般形式）**
设 $\{X_n\}$ 是独立同分布序列，则存在 $\{a_n\}$ 使得：

$$
\frac{1}{n} \sum_{k=1}^n X_k - a_n \overset{p}{\rightarrow} 0
$$

的充要条件是 $n\mathbb{P}(|X_1|\geq n)\to 0$。

### 12.3.2 强大数定律

**定理 12.3.3（强大数定律）**
设 $\{X_n\}$ 是独立同分布序列：

1. 若 $E|X_1| < \infty$，则：

$$
\frac{1}{n}\sum_{k=1}^n X_k \overset{a.s.}{\rightarrow} EX_1
$$

2. 若 $\frac{1}{n}\sum_{k=1}^n X_k \overset{a.s.}{\rightarrow} C$，则 $E|X_1| < \infty$ 且 $C = EX_1$

### 12.3.3 收敛模式

**定义 12.3.1（依概率收敛）**
$Y_n \overset{p}{\to} Y$ 如果对 $\forall \varepsilon > 0$：

$$
\lim_{n \to \infty} \mathbb{P}(|Y_n - Y| \geq \varepsilon) = 0
$$

**定义 12.3.2（几乎处处收敛）**
$Y_n \overset{a.s.}{\to} Y$ 如果：

$$
\mathbb{P} \left( \lim_{n \to \infty} Y_n = Y \right) = 1
$$

### 12.3.4 强、弱大数定律的对比

| 特性     | 弱大数定律                           | 强大数定律                         |
| -------- | ------------------------------------ | ---------------------------------- |
| 收敛类型 | 依概率收敛 $\overset{p}{\to}$        | 几乎处处收敛 $\overset{a.s.}{\to}$ |
| 条件     | $n\mathbb{P}(                        | X_1                                | \geq n) \to 0$ | $E | X_1 | < \infty$ |
| 直观理解 | 样本均值接近总体均值的可能性越来越大 | 样本均值几乎一定渐近接近总体均值   |

## 12.4 经典应用

### 12.4.1 频率与概率
对于伯努利试验 $X_n \sim B(1, p)$：

$$
\frac{1}{n} \sum_{k=1}^n X_k \overset{p}{\to} p
$$

### 12.4.2 经验分布
经验分布函数：

$$
F_n(x) = \frac{1}{n} \sum_{j=1}^n I_{\{X_j \leq x\}} \overset{a.s.}{\to} F(x)
$$

### 12.4.3 蒙特卡洛方法
用随机模拟计算积分：

$$
\int_a^b f(x) dx \approx c(b-a) \cdot \frac{1}{n} \sum_{j=1}^n I_j
$$

## 小结

### 核心知识点
- 弱大数定律：样本均值依概率收敛到总体均值
- 强大数定律：样本均值几乎处处收敛到总体均值  
- 收敛模式：依概率收敛与几乎处处收敛的定义与关系
- 条件放宽：从方差有限到一阶矩存在的推广

### 关键公式
- 弱大数定律：

$$
\frac{1}{n} \sum_{k=1}^n X_k \overset{p}{\to} EX_1
$$

- 强大数定律：

$$
\frac{1}{n} \sum_{k=1}^n X_k \overset{a.s.}{\to} EX_1
$$

- 切比雪夫不等式：

$$
\mathbb{P}(|X - EX| \geq \varepsilon) \leq \frac{var(X)}{\varepsilon^2}
$$

### 理论意义
大数定律建立了偶然性与必然性之间的桥梁，揭示了大量随机现象平均结果的稳定性，为统计推断提供了理论基础。
