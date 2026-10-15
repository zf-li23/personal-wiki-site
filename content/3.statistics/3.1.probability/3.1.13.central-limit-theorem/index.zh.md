---
title: 中心极限定理
---

## 13.1. 基本概念

### 13.1.1. 问题背景
大数定律描述了样本均值的极限行为，但未涉及收敛速度和分布形态。中心极限定理揭示了独立随机变量和的标准化形式依分布收敛于标准正态分布。

### 13.1.2. 收敛模式

**定义 13.1.1（依分布收敛）**
设 $Y_n, Y$ 的分布函数分别为 $F_n(x), F(x)$。如果在 $F(x)$ 的连续点 $x$，有
$$
\lim_{n \to \infty} F_n(x) = F(x)
$$
则称 $Y_n$ 依分布收敛到 $Y$，记作 $Y_n \xrightarrow{d} Y$。

## 13.2. 基本定理

### 13.2.1. Lindeberg-Lévy 中心极限定理

**定理 13.2.1（中心极限定理）**
设 $\{X_n\}$ 是独立同分布的随机变量序列，其期望为 $\mu$，方差为 $0 < \sigma^2 < \infty$，记 $S_n = X_1 + \cdots + X_n$，则
$$
\frac{S_n - \mathbb{E}(S_n)}{\sqrt{\operatorname{Var}(S_n)}} \xrightarrow{d} \mathcal{N}(0,1)
$$

**等价形式**
样本均值 $M_n = \frac{1}{n} \sum_{i=1}^n X_i$ 满足：
$$
\frac{M_n - \mathbb{E}(M_n)}{\sqrt{\operatorname{Var}(M_n)}} \xrightarrow{d} \mathcal{N}(0,1)
$$

### 13.2.2. 近似分布
当 $n$ 充分大时：
$$
S_n \approx \mathcal{N}(n\mu, n\sigma^2), \quad M_n \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)
$$

## 13.3. 定理证明

### 13.3.1. 证明思路
令 $Y_k = \frac{X_k - \mu}{\sigma}$，则 $\{Y_k\}$ 独立同分布，$\mathbb{E}Y_k = 0$，$\operatorname{Var}(Y_k) = 1$。

考虑标准化和：
$$
\frac{1}{\sqrt{n}} \sum_{k=1}^n Y_k = \frac{S_n - n\mu}{\sigma\sqrt{n}}
$$

### 13.3.2. 特征函数方法
**定理 13.3.1（连续性定理）**
$X_n \xrightarrow{d} X$ 的充分必要条件是其特征函数满足：
$$
\lim_{n \to \infty} \phi_n(t) = \phi(t), \quad \forall t \in \mathbb{R}
$$

**证明过程**
$Y_1$ 的特征函数 $\phi(t)$ 满足：
$$
\phi(t) = 1 - \frac{t^2}{2} + o(t^2)
$$

标准化和的特征函数：
$$
\phi_n(t) = \left[\phi\left(\frac{t}{\sqrt{n}}\right)\right]^n = \left(1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right)\right)^n \to \mathrm{e}^{-t^2/2}
$$

## 13.4. 理论拓展

### 13.4.1. 非独立同分布情形

**定理 13.4.1（Lindeberg-Feller 中心极限定理）**
设 $\{X_n\}$ 是独立的随机变量序列，方差序列 $\{\sigma_k^2\}$ 满足：
$$
B_n^2 = \sum_{k=1}^n \sigma_k^2 \to \infty, \quad \frac{\sigma_n^2}{B_n^2} \to 0
$$

则中心极限定理成立的充分必要条件是 Lindeberg 条件：
$$
\lim_{n \to \infty} \frac{1}{B_n^2} \sum_{k=1}^n \mathbb{E}[(X_k - \mathbb{E}X_k)^2 \boldsymbol{1}_{\{|X_k - \mathbb{E}X_k| > \varepsilon B_n\}}] = 0
$$

### 13.4.2. 理论意义
- 大量"微小"独立随机因素的叠加近似服从正态分布
- 正态分布在自然界和工程中普遍存在

## 13.5. 细致讨论

### 13.5.1. 离散型随机变量的修正

**定理 13.5.1（de Moivre-Laplace 中心极限定理）**
设 $S_n \sim \mathrm{Bin}(n,p)$，当 $n$ 充分大时：
$$
\mathbb{P}(k \leq S_n \leq m) \approx \Phi\left(\frac{m + 0.5 - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right)
$$

**连续性修正**
- 区间概率：端点加减 0.5
- 单点概率：$\mathbb{P}(S_n = k) \approx \Phi\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right)$

### 13.5.2. 适用条件
- 要求方差有限：柯西分布等重尾分布不适用
- 近似精度依赖于原始分布的对称性和样本量
- 在均值附近近似效果更好

## 13.6. 应用场景

### 13.6.1. 样本量计算
确定满足精度要求的样本量：
$$
\mathbb{P}(|M_n - \mu| < \varepsilon) \approx 2\Phi\left(\frac{\varepsilon\sqrt{n}}{\sigma}\right) - 1
$$

### 13.6.2. 概率近似
复杂分布的概率计算：
$$
\mathbb{P}(S_n \leq c) \approx \Phi\left(\frac{c - n\mu}{\sigma\sqrt{n}}\right)
$$

### 13.6.3. 区间估计
置信区间的构造：
$$
M_n \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
$$

其中 $z_{\alpha/2}$ 是标准正态分布的上 $\alpha/2$ 分位数（$1 - \Phi(z_{\alpha/2}) = \alpha/2$），区间的近似置信水平为 $1-\alpha$。

## 小结

### 核心知识点
- 中心极限定理：独立同分布随机变量和的标准化形式依分布收敛于标准正态分布
- 依分布收敛的定义和特征函数判别法
- 离散型随机变量的连续性修正
- 定理的适用条件和近似精度

### 关键公式
- 中心极限定理：
$$
\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)
$$

- 样本均值近似：
$$
M_n \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)
$$

- 离散修正：
$$
\mathbb{P}(k \leq S_n \leq m) \approx \Phi\left(\frac{m + 0.5 - np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right)
$$

### 理论意义
中心极限定理解释了正态分布在自然界和统计学中的普遍性，为统计推断提供了理论基础，是大样本理论的基石。
