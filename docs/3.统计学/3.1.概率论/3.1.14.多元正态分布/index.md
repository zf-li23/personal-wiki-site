## 14.1 随机向量的期望与协方差矩阵

### 14.1.1 随机向量的期望

设 $X = (X_1, ..., X_n)^T$ 是随机向量，如果对每个 $i$，$\mu_i = EX_i$ 存在，则定义：
$$
EX = (EX_1, ..., EX_n)^T = (\mu_1, ..., \mu_n)^T
$$

**期望性质**：
1. $E(a^TX) = a^TEX$
2. $(EY)^T = E(Y^T)$
3. $E(AY) = AEY$
4. $E(YB) = EY \cdot B$
5. $E(AYB) = AEY \cdot B$

### 14.1.2 协方差矩阵

**定义 14.1.1（协方差矩阵）**
如果随机向量 $X$ 的数学期望 $\mu = EX$ 存在，对每个分量 $X_i$ 的方差有限，则称：
$$
\Sigma = E[(X - \mu)(X - \mu)^T] = (\sigma_{ij})
$$
为 $X$ 的协方差矩阵，其中 $\sigma_{ij} = \text{cov}(X_i, X_j)$。

**性质**：
- $\Sigma$ 是对称矩阵
- $\Sigma$ 是非负定矩阵
- $\Sigma$ 退化的充要条件是存在不全为零的常数 $a_1, ..., a_n$ 使得：
  $$
  \sum_{i=1}^n a_i(X_i - EX_i) = 0 \quad \text{a.s.}
  $$

## 14.2 多元正态分布的定义

### 14.2.1 等价定义

**定义 14.2.1（多元正态分布）**
设 $\vec{\mu} = (\mu_1, \mu_2, ..., \mu_n)^T$ 是 $n$ 维常数列向量，$B$ 是 $n \times m$ 常数矩阵，$\varepsilon_1, \varepsilon_2, ..., \varepsilon_m$ 是相互独立且服从标准正态分布的随机变量。如果：
$$
\vec{X} = \vec{\mu} + B\vec{\varepsilon}
$$
其中 $\vec{\varepsilon} = (\varepsilon_1, \varepsilon_2, ..., \varepsilon_m)^T$，且矩阵 $BB^T$ 满秩，就称 $\vec{X}$ 服从 $n$ 维正态分布，记作 $\vec{X} \sim N(\vec{\mu}, BB^T)$。

### 14.2.2 密度函数

当 $\Sigma$ 正定时，$\vec{X} \sim N(\vec{\mu}, \Sigma)$ 有联合密度函数：
$$
f(\vec{x}) = \frac{1}{(\sqrt{2\pi})^{n}\sqrt{\det(\Sigma)}} \exp\left[ -\frac{1}{2}(\vec{x} - \vec{\mu})^{T}\Sigma^{-1}(\vec{x} - \vec{\mu}) \right]
$$

### 14.2.3 特征函数

$\vec{X} \sim N(\vec{\mu}, \Sigma)$ 的特征函数为：
$$
\phi_{\vec{X}}(\vec{t}) = E[\exp(i\vec{t}^T\vec{X})] = \exp\left[i\vec{t}^T\vec{\mu} - \frac{1}{2}\vec{t}^T\Sigma\vec{t}\right]
$$

## 14.3 多元正态分布的性质

### 14.3.1 线性变换

**定理 14.3.1**
如果 $\vec{X} \sim N(\vec{\mu}, \Sigma)$，则对任意常数矩阵 $A$ 和常向量 $\vec{b}$，只要 $\vec{b} + A\vec{X}$ 有意义，$A\Sigma A^T$ 满秩，则：
$$
\vec{Y} = \vec{b} + A\vec{X} \sim N\left( \vec{b} + A\vec{\mu}, A\Sigma A^T \right)
$$

### 14.3.2 判定法则

**定理 14.3.2（重要判定法则）**
$\vec{X} = (X_1, X_2, ..., X_n)^T \sim N(\vec{\mu}, \Sigma)$ 的充要条件是对任何 $\vec{a} = (a_1, a_2, ..., a_n)^T \in \mathbb{R}^n$：
$$
Y := \vec{a}^T \vec{X} \sim N(\vec{a}^T \vec{\mu}, \vec{a}^T \Sigma \vec{a})
$$

### 14.3.3 边缘分布

如果 $\vec{X}$ 服从多元正态分布，则 $\vec{X}$ 的任何分量 $(X_{j_1}, ..., X_{j_k})^T$ 也服从多元正态分布。

## 14.4 独立性判定

### 14.4.1 分块独立性

**定理 14.4.1**
设 $\vec{X} \sim N(\vec{\mu}, \Sigma)$，如果：
$$
\vec{X} = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}, \quad
\vec{\mu} = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \quad
\Sigma = \begin{pmatrix} \Sigma_{11} & 0 \\ 0 & \Sigma_{22} \end{pmatrix}
$$
且 $X_1, \mu_1$ 和方阵 $\Sigma_{11}$ 的行数相同，则 $X_1$ 和 $X_2$ 独立，而且：
$$
X_1 \sim N(\mu_1, \Sigma_{11}), \quad X_2 \sim N(\mu_2, \Sigma_{22})
$$

### 14.4.2 分量独立性

**定理 14.4.2**
如果 $\vec{X} \sim N(\vec{\mu}, \Sigma)$，则 $(X_1, X_2, ..., X_n)$ 相互独立的充要条件是：
$$
\Sigma = \text{diag}(\sigma_1^2, \sigma_2^2, ..., \sigma_n^2)
$$

## 14.5 条件分布

**定理 14.5.1（条件分布）**
设 $\vec{X} \sim N(\vec{\mu}, \Sigma)$，$\det(\Sigma) > 0$ 和分块矩阵：
$$
\vec{X} = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}, \quad
\vec{\mu} = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \quad
\Sigma = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix}
$$
其中 $X_1, \mu_1$ 和方阵 $\Sigma_{11}$ 的行数相同，则在条件 $X_1 = X_1^*$ 下，$X_2$ 服从多元正态分布：
$$
N(\mu_2 + \Sigma_{21}\Sigma_{11}^{-1}(X_1^* - \mu_1), \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1} \Sigma_{12})
$$

## 14.6 重要应用

### 14.6.1 卡方分布

设 $\vec{X} = (X_1, X_2, ..., X_n)^T \sim N(\vec{\mu}, \Sigma)$，且 $\Sigma$ 正定，则：
$$
(\vec{X} - \vec{\mu})^T \Sigma^{-1}(\vec{X} - \vec{\mu}) \sim \chi^2(n)
$$

### 14.6.2 线性组合的独立性

设 $\begin{pmatrix} X \\ Y \end{pmatrix} \sim N\left( \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \Sigma \right)$，且二维矩阵 $\Sigma = \begin{pmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{pmatrix}$ 正定，则 $X + Y$ 与 $X - Y$ 独立的充分必要条件是 $\sigma_{11} = \sigma_{22}$。

### 14.6.3 统计推断应用

设 $X_1, ..., X_n$ 相互独立，同服从 $N(\mu, \sigma^2)$ 分布，记：
- $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ 为样本均值
- $S_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ 为样本方差

则有：
1. $\bar{X}$ 与 $S_n^2$ 独立
2. $\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$
3. $\frac{(n-1)S_n^2}{\sigma^2} \sim \chi_{n-1}^2$

## 14.7 随机向量的极限定理

### 14.7.1 大数定律

设 $\vec{X}_1, \ldots, \vec{X}_n, \ldots$ 独立同分布，则：
$$
\frac{\vec{X}_1 + \cdots + \vec{X}_n}{n} \overset{a.s./p}{\longrightarrow} E\vec{X}_1
$$

### 14.7.2 中心极限定理

设 $\vec{X}_1, \ldots, \vec{X}_n, \ldots$ 独立同分布，$E\vec{X}_1 = \vec{\mu}$，$var(\vec{X}_1) = \Sigma$，则：
$$
\frac{\vec{S}_n - n\vec{\mu}}{\sqrt{n}} \overset{d}{\to} N(0, \Sigma)
$$
其中 $\vec{S}_n = \vec{X}_1 + \cdots + \vec{X}_n$。

**标准化形式**：
$$
\Sigma^{-1/2} \cdot \frac{\vec{S}_n - n\vec{\mu}}{\sqrt{n}} \overset{d}{\to} N(0, I)
$$

## 小结

### 核心知识点
- 多元正态分布的三种等价定义：线性变换定义、密度函数定义、特征函数定义
- 多元正态分布的线性变换性质
- 多元正态分布的判定法则：任意线性组合服从正态分布
- 多元正态分布的独立性判定：协方差矩阵分块对角或对角
- 多元正态分布的条件分布公式
- 随机向量的极限定理：大数定律和中心极限定理

### 关键公式
- 密度函数：
  $$
  f(\vec{x}) = \frac{1}{(\sqrt{2\pi})^{n}\sqrt{\det(\Sigma)}} \exp\left[ -\frac{1}{2}(\vec{x} - \vec{\mu})^{T}\Sigma^{-1}(\vec{x} - \vec{\mu}) \right]
  $$

- 特征函数：
  $$
  \phi_{\vec{X}}(\vec{t}) = \exp\left[i\vec{t}^T\vec{\mu} - \frac{1}{2}\vec{t}^T\Sigma\vec{t}\right]
  $$

- 条件分布：
  $$
  X_2|X_1 = X_1^* \sim N(\mu_2 + \Sigma_{21}\Sigma_{11}^{-1}(X_1^* - \mu_1), \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1} \Sigma_{12})
  $$

### 理论意义
多元正态分布是多元统计分析的理论基础，具有良好的解析性质和几何解释，在大数据分析和机器学习中有广泛应用。
