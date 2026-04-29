## 10.1 协方差定义及性质

### 10.1.1 协方差的定义

设 $X$ 和 $Y$ 是两个随机变量，且 $EX$ 和 $EY$ 存在。当 $E[(X - EX)(Y - EY)] < \infty$ 时，称
$$
\text{cov}(X, Y) = E[(X - EX)(Y - EY)]
$$
为 $X$ 与 $Y$ 的协方差。

### 10.1.2 协方差的性质

1. $\text{cov}(X, X) = var(X)$
2. $\text{cov}(X, Y) = \text{cov}(Y, X)$
3. $\text{cov}(X, Y) = E(XY) - (EX)(EY)$ （常用计算公式）
4. 若 $c$ 是常数，则 $\text{cov}(X, c) = 0$
5. 双线性：
   - $\text{cov}(cX, Y) = c \cdot \text{cov}(X, Y)$
   - $\text{cov}(X, Y+Z) = \text{cov}(X, Y) + \text{cov}(X, Z)$
6. $var(X_1 + X_2) = var(X_1) + var(X_2) + 2\text{cov}(X_1, X_2)$

### 10.1.3 例子：多项分布的协方差

设 $(X_1, \dots, X_k) \sim \text{Multinomial}(n, \vec{p})$，其中 $\vec{p} = (p_1, \dots, p_k)$，且 $\sum_{i=1}^k p_i = 1$。

- 当 $i = j$ 时，$\text{cov}(X_i, X_j) = var(X_i) = n p_i (1-p_i)$
- 当 $i \neq j$ 时，$\text{cov}(X_i, X_j) = -n p_i p_j$

## 10.2 相关系数定义

### 10.2.1 相关系数的定义

当 $0 < var(X) \cdot var(Y) < \infty$ 时，定义 $X$ 与 $Y$ 的相关系数为
$$
\text{corr}(X, Y) = \frac{\text{cov}(X, Y)}{\sqrt{var(X)} \sqrt{var(Y)}}
$$

### 10.2.2 例子：二元正态分布

设 $(X, Y) \sim N(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$，则 $\text{corr}(X, Y) = \rho$。

### 10.2.3 相关系数的性质

- 相关系数是标准化的协方差，取值范围为 $[-1, 1]$
- 具有可比性，不受变量缩放的影响

## 10.3 对协方差与相关系数的深入理解

### 10.3.1 不相关与独立

- 若 $X$ 与 $Y$ 独立，则 $\text{cov}(X, Y) = 0$，即 $X$ 与 $Y$ 不相关
- 反之，不相关不一定独立
- 特例：对于二元正态分布，不相关与独立等价

### 10.3.2 相关系数的几何解释

将中心化的随机变量 $\hat{X} = X - EX$ 和 $\hat{Y} = Y - EY$ 视为向量，内积定义为 $E(\hat{X}\hat{Y})$，则
$$
\text{corr}(X, Y) = \frac{\langle \hat{X}, \hat{Y} \rangle}{\|\hat{X}\| \cdot \|\hat{Y}\|} = \cos \varphi
$$
其中 $\varphi$ 是 $\hat{X}$ 与 $\hat{Y}$ 的夹角。

### 10.3.3 相关系数与线性关系

- $|\text{corr}(X, Y)| = 1$ 当且仅当 $X$ 与 $Y$ 几乎处处有线性关系，即存在常数 $a, b, c$ 使得 $aX + bY = c$ 几乎处处成立

### 10.3.4 相关与因果

- 相关关系不意味着因果关系
- 相关关系可以帮助发现潜在的因果关系，但需要进一步验证

## 10.4 随机向量的协方差矩阵

### 10.4.1 随机向量的期望

设 $X = (X_1, \dots, X_n)$，若每个 $X_i$ 的期望存在，则
$$
EX = (EX_1, \dots, EX_n)
$$

### 10.4.2 协方差矩阵的定义

设 $X = (X_1, \dots, X_n)$ 为随机向量，期望向量 $\mu = EX$，则协方差矩阵为
$$
\Sigma = E[(X - \mu)'(X - \mu)] = (\sigma_{ij})_{n \times n}
$$
其中 $\sigma_{ij} = \text{cov}(X_i, X_j)$。

### 10.4.3 协方差矩阵的性质

- $\Sigma$ 是对称非负定矩阵
- $\Sigma$ 退化的充要条件是存在非零向量 $\mathbf{a} = (a_1, \dots, a_n)$ 使得
  $$
  \sum_{i=1}^n a_i (X_i - EX_i) = 0 \quad \text{a.s.}
  $$

## 小结

### 核心知识点

- 协方差和相关系数的定义、性质与计算
- 理解不相关与独立的关系，特别是二元正态分布中的等价性
- 相关系数的几何解释和线性关系判断
- 随机向量的期望和协方差矩阵的定义及性质

### 关键公式

- 协方差：$\text{cov}(X, Y) = E[(X - EX)(Y - EY)] = E(XY) - (EX)(EY)$
- 相关系数：$\text{corr}(X, Y) = \frac{\text{cov}(X, Y)}{\sqrt{var(X)} \sqrt{var(Y)}}$
- 方差公式：$var(X_1 + X_2) = var(X_1) + var(X_2) + 2\text{cov}(X_1, X_2)$
- 协方差矩阵：$\Sigma = E[(X - \mu)'(X - \mu)]$

### 应用技巧

- 利用对称性和示性函数简化计算
- 通过二维情形帮助理解高维概念
- 注意相关关系与因果关系的区别
