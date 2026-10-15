---
title: 课程总结
---

## 16.1. 知识体系框架

### 16.1.1. 概率空间
- 样本空间 $\Omega$、事件域 $\mathcal{F}$、概率测度 $\mathbb{P}$
- 条件概率 $\mathbb{P}_A(\cdot) = \mathbb{P}(\cdot|A)$

### 16.1.2. 随机变量
- 离散型：分布列(PMF)、概率母函数(PGF)
- 连续型：概率密度函数(PDF)、矩母函数(MGF)
- 一般型：分布函数(CDF)、特征函数(CF)

### 16.1.3. 联合分布
- 边缘分布、条件分布、独立性
- 随机向量函数的分布、次序统计量

### 16.1.4. 数值特征
- 期望 $\mathbb{E}X$、方差 $\operatorname{Var}(X)$
- 协方差 $\operatorname{Cov}(X,Y)$、相关系数
- 条件期望 $\mathbb{E}(X|Y)$、条件方差 $\operatorname{Var}(X|Y)$

### 16.1.5. 极限理论
- 收敛性：依分布、依概率、几乎处处收敛
- 大数定律（强、弱）
- 中心极限定理

## 16.2. 重要分布总结

### 16.2.1. 离散型分布
- 两点分布 $\mathrm{Bin}(1,p)$
- 二项分布 $\mathrm{Bin}(n,p)$
- 几何分布 $\mathrm{Geo}(p)$
- 泊松分布 $\mathrm{Poi}(\lambda)$
- 负二项分布 $\mathrm{NB}(r,p)$
- 超几何分布

### 16.2.2. 连续型分布
- 均匀分布 $\mathrm{U}(a,b)$
- 指数分布 $\mathrm{Exp}(\lambda)$
- 正态分布 $\mathcal{N}(\mu,\sigma^2)$
- Gamma分布 $\Gamma(\alpha,\lambda)$
- 卡方分布 $\chi^2_n$
- t分布 $t_n$
- F分布 $F_{m,n}$

### 16.2.3. 多元分布
- 多项分布
- 多元正态分布 $\mathcal{N}(\boldsymbol{\mu},\Sigma)$

## 16.3. 核心定理与公式

### 16.3.1. 不等式
- Markov不等式：$\mathbb{P}(|X| \geq a) \leq \frac{\mathbb{E}|X|}{a}$
- Chebyshev不等式：$\mathbb{P}(|X-\mathbb{E}X| \geq \varepsilon) \leq \frac{\operatorname{Var}(X)}{\varepsilon^2}$
- Cauchy-Schwarz不等式：$|\mathbb{E}(XY)| \leq \sqrt{\mathbb{E}X^2 \cdot \mathbb{E}Y^2}$
- Jensen不等式：$g(\mathbb{E}X) \leq \mathbb{E}g(X)$（$g$凸函数）

### 16.3.2. 期望公式
- 重期望法则：$\mathbb{E}X = \mathbb{E}[\mathbb{E}(X|Y)]$
- 全方差公式：$\operatorname{Var}(X) = \operatorname{Var}[\mathbb{E}(X|Y)] + \mathbb{E}[\operatorname{Var}(X|Y)]$

### 16.3.3. 收敛性关系
- 几乎处处收敛 $\Rightarrow$ 依概率收敛 $\Rightarrow$ 依分布收敛
- 常数情形：依分布收敛 $\Leftrightarrow$ 依概率收敛

### 16.3.4. 极限定理
- 弱大数定律：$\frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{p} \mathbb{E}X_1$
- 强大数定律：$\frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{\text{a.s.}} \mathbb{E}X_1$
- 中心极限定理：$\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)$

## 16.4. 解题技巧与方法

### 16.4.1. 三套工具
1. **离散型随机变量**：PMF、CDF、特征函数
2. **连续型随机变量**：PDF、CDF、特征函数  
3. **一般随机变量**：CDF、特征函数

### 16.4.2. 常用方法
- 条件化方法
- 对称性分析
- 归一化技巧
- 指示随机变量
- 母函数方法
- 微元法、增补变量法

### 16.4.3. 独立随机变量和的分布
| $X_i$ 分布                 | $\sum X_i$ 分布                      |
| -------------------------- | ------------------------------------ |
| $\mathrm{Ber}(p)$          | $\mathrm{Bin}(n,p)$                  |
| $\mathrm{Bin}(m_i,p)$      | $\mathrm{Bin}(\sum m_i,p)$           |
| $\mathrm{Geo}(p)$          | 帕斯卡分布（参数 $n, p$），即 $n + \mathrm{NB}(n,p)$ |
| $\mathrm{Poi}(\lambda_i)$  | $\mathrm{Poi}(\sum \lambda_i)$       |
| $\mathcal{N}(\mu_i,\sigma_i^2)$ | $\mathcal{N}(\sum \mu_i,\sum \sigma_i^2)$ |
| $\mathrm{Exp}(\lambda)$    | $\Gamma(n,\lambda)$                  |
| $\chi^2_1$                 | $\chi^2_n$                           |

## 16.5. 课程启示
概率论建立了偶然现象与必然规律之间的桥梁，为统计学和数据分析提供了坚实的理论基础。通过本课程的学习，不仅掌握了概率论的基本理论和方法，更重要的是培养了严谨的数学思维和解决实际问题的能力。
