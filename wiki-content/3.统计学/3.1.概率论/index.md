对应课程：40160713 初等概率论

涵盖 10420803 概率论与数理统计的概率论部分内容，后续可以详细补充此部分。

## 知识体系框架

### 概率空间
- 样本空间 $\Omega$、事件域 $\mathcal{F}$、概率测度 $\mathbb{P}$
- 条件概率 $\mathbb{P}_A(\cdot) = \mathbb{P}(\cdot|A)$

### 随机变量
- 离散型：分布列(PMF)、概率母函数(PGF)
- 连续型：概率密度函数(PDF)、矩母函数(MGF)
- 一般型：分布函数(CDF)、特征函数(CF)

### 联合分布
- 边缘分布、条件分布、独立性
- 随机向量函数的分布、次序统计量

### 数值特征
- 期望 $EX$、方差 $var(X)$
- 协方差 $\text{cov}(X,Y)$、相关系数
- 条件期望 $E(X|Y)$、条件方差 $var(X|Y)$

### 极限理论
- 收敛性：依分布、依概率、几乎处处收敛
- 大数定律（强、弱）
- 中心极限定理

## 重要分布总结

### 离散型分布
- 两点分布 $B(1,p)$
- 二项分布 $B(n,p)$
- 几何分布 $Geom(p)$
- 泊松分布 $\mathcal{P}(\lambda)$
- 负二项分布 $NB(r,p)$
- 超几何分布

### 连续型分布
- 均匀分布 $U(a,b)$
- 指数分布 $\mathcal{E}(\lambda)$
- 正态分布 $N(\mu,\sigma^2)$
- Gamma分布 $\Gamma(\alpha,\lambda)$
- 卡方分布 $\chi^2(n)$
- t分布 $t(n)$
- F分布 $F(m,n)$

### 多元分布
- 多项分布
- 多元正态分布 $N(\vec{\mu},\Sigma)$

## 核心定理与公式

### 不等式
- Markov不等式：$\mathbb{P}(|X| \geq a) \leq \frac{E|X|}{a}$
- Chebyshev不等式：$\mathbb{P}(|X-EX| \geq \varepsilon) \leq \frac{var(X)}{\varepsilon^2}$
- Cauchy-Schwarz不等式：$|E(XY)| \leq \sqrt{EX^2 \cdot EY^2}$
- Jensen不等式：$g(EX) \leq Eg(X)$（$g$凸函数）

### 期望公式
- 重期望法则：$EX = E[E(X|Y)]$
- 全方差公式：$var(X) = var[E(X|Y)] + E[var(X|Y)]$

### 收敛性关系
- 几乎处处收敛 $\Rightarrow$ 依概率收敛 $\Rightarrow$ 依分布收敛
- 常数情形：依分布收敛 $\Leftrightarrow$ 依概率收敛

### 极限定理
- 弱大数定律：$\frac{1}{n}\sum_{i=1}^n X_i \overset{p}{\to} EX_1$
- 强大数定律：$\frac{1}{n}\sum_{i=1}^n X_i \overset{a.s.}{\to} EX_1$
- 中心极限定理：$\frac{S_n - n\mu}{\sigma\sqrt{n}} \overset{d}{\to} N(0,1)$

## 解题技巧与方法

### 三套工具
1. **离散型随机变量**：PMF、CDF、特征函数
2. **连续型随机变量**：PDF、CDF、特征函数  
3. **一般随机变量**：CDF、特征函数

### 常用方法
- 条件化方法
- 对称性分析
- 归一化技巧
- 指示随机变量
- 母函数方法
- 微元法、增补变量法

### 独立随机变量和的分布
| $X_i$ 分布                 | $\sum X_i$ 分布                      |
| -------------------------- | ------------------------------------ |
| $Bernoulli(p)$             | $Binomial(n,p)$                      |
| $Binomial(m_i,p)$          | $Binomial(\sum m_i,p)$               |
| $Geometric(p)$             | $NBin(n,p)$                          |
| $Poisson(\lambda_i)$       | $Poisson(\sum \lambda_i)$            |
| $Normal(\mu_i,\sigma_i^2)$ | $Normal(\sum \mu_i,\sum \sigma_i^2)$ |
| $Exponential(\lambda)$     | $Gamma(n,\lambda)$                   |
| $\chi^2_1$                 | $\chi^2_n$                           |

## 课程启示
概率论建立了偶然现象与必然规律之间的桥梁，为统计学和数据分析提供了坚实的理论基础。通过本课程的学习，不仅掌握了概率论的基本理论和方法，更重要的是培养了严谨的数学思维和解决实际问题的能力。
