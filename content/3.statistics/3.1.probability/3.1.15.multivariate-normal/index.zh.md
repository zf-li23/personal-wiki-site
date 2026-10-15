---
title: 多元正态分布
---

## 15.1. 随机向量的期望与协方差矩阵

### 15.1.1. 随机向量的期望

设 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ 是随机向量，如果对每个 $i$，$\mu_i = \mathbb{E}X_i$ 存在，则定义：
$$
\mathbb{E}\boldsymbol{X} = (\mathbb{E}X_1, \dots, \mathbb{E}X_n)^{\mathsf T} = (\mu_1, \dots, \mu_n)^{\mathsf T}
$$

**期望性质**：
1. $\mathbb{E}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{a}^{\mathsf T}\mathbb{E}\boldsymbol{X}$
2. $(\mathbb{E}Y)^{\mathsf T} = \mathbb{E}(Y^{\mathsf T})$
3. $\mathbb{E}(AY) = A\,\mathbb{E}Y$
4. $\mathbb{E}(YB) = \mathbb{E}Y \cdot B$
5. $\mathbb{E}(AYB) = A\,\mathbb{E}Y \cdot B$

### 15.1.2. 协方差矩阵

**定义 15.1.1（协方差矩阵）**
如果随机向量 $\boldsymbol{X}$ 的数学期望 $\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X}$ 存在，对每个分量 $X_i$ 的方差有限，则称：
$$
\Sigma = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}] = (\sigma_{ij})
$$
为 $\boldsymbol{X}$ 的协方差矩阵，其中 $\sigma_{ij} = \operatorname{Cov}(X_i, X_j)$。

**性质**：
- $\Sigma$ 是对称矩阵
- $\Sigma$ 是非负定矩阵
- $\Sigma$ 退化的充要条件是存在不全为零的常数 $a_1, \dots, a_n$ 使得：
  $$
  \sum_{i=1}^n a_i(X_i - \mathbb{E}X_i) = 0 \quad \text{a.s.}
  $$

## 15.2. 多元正态分布的定义

### 15.2.1. 等价定义

**定义 15.2.1（多元正态分布）**
设 $\boldsymbol{\mu} = (\mu_1, \mu_2, \dots, \mu_n)^{\mathsf T}$ 是 $n$ 维常数列向量，$B$ 是 $n \times m$ 常数矩阵，$\varepsilon_1, \varepsilon_2, \dots, \varepsilon_m$ 是相互独立且服从标准正态分布的随机变量。如果：
$$
\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}
$$
其中 $\boldsymbol{\varepsilon} = (\varepsilon_1, \varepsilon_2, \dots, \varepsilon_m)^{\mathsf T}$，且矩阵 $BB^{\mathsf T}$ 满秩，就称 $\boldsymbol{X}$ 服从 $n$ 维正态分布，记作 $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, BB^{\mathsf T})$。

### 15.2.2. 密度函数

当 $\Sigma$ 正定时，$\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ 有联合密度函数：
$$
f(\boldsymbol{x}) = \frac{1}{(\sqrt{2\pi})^{n}\sqrt{\det(\Sigma)}} \exp\left[ -\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) \right]
$$

### 15.2.3. 特征函数

$\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ 的特征函数为：
$$
\phi_{\boldsymbol{X}}(\boldsymbol{t}) = \mathbb{E}[\exp(\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{X})] = \exp\left[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}\Sigma\boldsymbol{t}\right]
$$

## 15.3. 多元正态分布的性质

### 15.3.1. 线性变换

**定理 15.3.1**
如果 $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，则对任意常数矩阵 $A$ 和常向量 $\boldsymbol{b}$，只要 $\boldsymbol{b} + A\boldsymbol{X}$ 有意义，$A\Sigma A^{\mathsf T}$ 满秩，则：
$$
\boldsymbol{Y} = \boldsymbol{b} + A\boldsymbol{X} \sim \mathcal{N}\left( \boldsymbol{b} + A\boldsymbol{\mu}, A\Sigma A^{\mathsf T} \right)
$$

### 15.3.2. 判定法则

**定理 15.3.2（重要判定法则）**
$\boldsymbol{X} = (X_1, X_2, \dots, X_n)^{\mathsf T} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ 的充要条件是对任何 $\boldsymbol{a} = (a_1, a_2, \dots, a_n)^{\mathsf T} \in \mathbb{R}^n$：
$$
Y := \boldsymbol{a}^{\mathsf T} \boldsymbol{X} \sim \mathcal{N}(\boldsymbol{a}^{\mathsf T} \boldsymbol{\mu}, \boldsymbol{a}^{\mathsf T} \Sigma \boldsymbol{a})
$$

### 15.3.3. 边缘分布

如果 $\boldsymbol{X}$ 服从多元正态分布，则 $\boldsymbol{X}$ 的任何分量 $(X_{j_1}, \dots, X_{j_k})^{\mathsf T}$ 也服从多元正态分布。

## 15.4. 独立性判定

### 15.4.1. 分块独立性

**定理 15.4.1**
设 $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，如果：
$$
\boldsymbol{X} = \begin{pmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{pmatrix}, \quad
\boldsymbol{\mu} = \begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix}, \quad
\Sigma = \begin{pmatrix} \Sigma_{11} & 0 \\ 0 & \Sigma_{22} \end{pmatrix}
$$
且 $\boldsymbol{X}_1, \boldsymbol{\mu}_1$ 和方阵 $\Sigma_{11}$ 的行数相同，则 $\boldsymbol{X}_1$ 和 $\boldsymbol{X}_2$ 独立，而且：
$$
\boldsymbol{X}_1 \sim \mathcal{N}(\boldsymbol{\mu}_1, \Sigma_{11}), \quad \boldsymbol{X}_2 \sim \mathcal{N}(\boldsymbol{\mu}_2, \Sigma_{22})
$$

### 15.4.2. 分量独立性

**定理 15.4.2**
如果 $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，则 $(X_1, X_2, \dots, X_n)$ 相互独立的充要条件是：
$$
\Sigma = \operatorname{diag}(\sigma_1^2, \sigma_2^2, \dots, \sigma_n^2)
$$

## 15.5. 条件分布

**定理 15.5.1（条件分布）**
设 $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，$\det(\Sigma) > 0$ 和分块矩阵：
$$
\boldsymbol{X} = \begin{pmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{pmatrix}, \quad
\boldsymbol{\mu} = \begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix}, \quad
\Sigma = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix}
$$
其中 $\boldsymbol{X}_1, \boldsymbol{\mu}_1$ 和方阵 $\Sigma_{11}$ 的行数相同，则在条件 $\boldsymbol{X}_1 = \boldsymbol{x}_1$ 下，$\boldsymbol{X}_2$ 服从多元正态分布：
$$
\mathcal{N}(\boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1), \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1} \Sigma_{12})
$$

## 15.6. 重要应用

### 15.6.1. 卡方分布

设 $\boldsymbol{X} = (X_1, X_2, \dots, X_n)^{\mathsf T} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，且 $\Sigma$ 正定，则：
$$
(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T} \Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_n
$$

### 15.6.2. 线性组合的独立性

设 $\begin{pmatrix} X \\ Y \end{pmatrix} \sim \mathcal{N}\left( \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \Sigma \right)$，且二维矩阵 $\Sigma = \begin{pmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{pmatrix}$ 正定，则 $X + Y$ 与 $X - Y$ 独立的充分必要条件是 $\sigma_{11} = \sigma_{22}$。

### 15.6.3. 统计推断应用

设 $X_1, \dots, X_n$ 相互独立，同服从 $\mathcal{N}(\mu, \sigma^2)$ 分布，记：
- $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ 为样本均值
- $S_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ 为样本方差

则有：
1. $\bar{X}$ 与 $S_n^2$ 独立
2. $\bar{X} \sim \mathcal{N}(\mu, \frac{\sigma^2}{n})$
3. $\frac{(n-1)S_n^2}{\sigma^2} \sim \chi_{n-1}^2$

## 15.7. 随机向量的极限定理

### 15.7.1. 大数定律

设 $\boldsymbol{X}_1, \ldots, \boldsymbol{X}_n, \ldots$ 独立同分布，则：
$$
\frac{\boldsymbol{X}_1 + \cdots + \boldsymbol{X}_n}{n} \xrightarrow{\text{a.s.}/p} \mathbb{E}\boldsymbol{X}_1
$$

### 15.7.2. 中心极限定理

设 $\boldsymbol{X}_1, \ldots, \boldsymbol{X}_n, \ldots$ 独立同分布，$\mathbb{E}\boldsymbol{X}_1 = \boldsymbol{\mu}$，$\operatorname{Var}(\boldsymbol{X}_1) = \Sigma$，则：
$$
\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(\boldsymbol{0}, \Sigma)
$$
其中 $\boldsymbol{S}_n = \boldsymbol{X}_1 + \cdots + \boldsymbol{X}_n$。

**标准化形式**：
$$
\Sigma^{-1/2} \cdot \frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(\boldsymbol{0}, I)
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
  f(\boldsymbol{x}) = \frac{1}{(\sqrt{2\pi})^{n}\sqrt{\det(\Sigma)}} \exp\left[ -\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) \right]
  $$

- 特征函数：
  $$
  \phi_{\boldsymbol{X}}(\boldsymbol{t}) = \exp\left[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}\Sigma\boldsymbol{t}\right]
  $$

- 条件分布：
  $$
  \boldsymbol{X}_2 \mid \boldsymbol{X}_1 = \boldsymbol{x}_1 \sim \mathcal{N}(\boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1), \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1} \Sigma_{12})
  $$

### 理论意义
多元正态分布是多元统计分析的理论基础，具有良好的解析性质和几何解释，在大数据分析和机器学习中有广泛应用。
