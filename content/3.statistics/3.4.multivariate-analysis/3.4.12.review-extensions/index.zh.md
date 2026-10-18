---
title: 课程总结与延伸
description: 全课的高密度回顾（各方法的目标、模型、求解与假设），以及延伸方法：错误发现率、对应分析、稀疏与 logistic 主成分分析、正则化判别分析、logistic 回归、k 近邻、网络模型与矩阵因子模型。
source_hash: c14beec1013a
---

本章先回顾整门课程：多元方法回答哪些问题，各方法的并列比较，以及它们共有的"建模—求解—评价"框架。然后介绍若干延伸方法，它们或者更好地解决旧问题，或者用新方法处理类似的问题，或者处理新类型的数据：同时检验大量假设时的错误发现率，列联表的对应分析，稀疏与 logistic 版本的主成分分析，正则化判别分析，用于分类的 logistic 回归与 $k$ 近邻，以及网络和矩阵值时间序列的模型。这些延伸只是对问题的介绍，而非完整的论述；其中若干内容将在后续课程中展开，如[统计计算](/3.5)、[非参数统计](/3.6)、[贝叶斯统计](/3.7)与[因果推断](/3.9)。

## 12.1. 课程回顾

### 12.1.1. 多元分析的全景

多元方法可以按其研究随机向量 $\boldsymbol{X}$ 的哪个方面来组织。

| 方面 | 问题 | 方法 |
|---|---|---|
| $\boldsymbol{X}$ 的位置 | 均值向量是否等于给定值？两个均值向量是否相等？ | 基于 **Hotelling T² 统计量** 的单样本与两样本检验（[3.4.3](/3.4.3)、[3.4.4](/3.4.4)） |
| $\boldsymbol{X}$ 的变异 | 变异的主要方向是什么？能否用少数变量或因子解释？ | **主成分分析**（[3.4.5](/3.4.5)）、**多维标度**（[3.4.6](/3.4.6)）、**因子分析**（[3.4.8](/3.4.8)） |
| $\boldsymbol{X}_1$ 与 $\boldsymbol{X}_2$ 的关系 | 两组变量如何关联？ | **典型相关分析**（[3.4.9](/3.4.9)） |
| $\boldsymbol{X}$ 与隐变量 $Y$ 的关系 | 是否存在未观测到的类？ | **聚类分析**：层次聚类、$k$ 均值、EM（[3.4.11](/3.4.11)） |
| $\boldsymbol{X}$ 与观测到的 $Y$ 的关系，$Y$ 连续 | $Y$ 如何依赖于 $\boldsymbol{X}$？ | 线性回归（[3.4.7](/3.4.7)） |
| $\boldsymbol{X}$ 与观测到的 $Y$ 的关系，$Y$ 离散 | 新观测属于哪一类？ | Fisher 判别；最小 ECM 规则，正态下的 LDA 与 QDA（[3.4.10](/3.4.10)） |

主成分、多维标度、因子分析、典型相关与聚类是无监督的（不使用响应变量）；回归与判别分析是有监督的。

### 12.1.2. 各方法一览

| 方法 | 目标 | 模型或目标函数（总体） | 求解 | 假设与说明 |
|---|---|---|---|---|
| Hotelling $T^2$（[3.4.3](/3.4.3)） | 检验 $H_0\colon\boldsymbol{\mu} = \boldsymbol{\mu}_0$；$\boldsymbol{\mu}$ 的置信域 | $T^2 = n(\bar{\boldsymbol{x}}-\boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}}-\boldsymbol{\mu}_0)$，$\frac{n-p}{(n-1)p}T^2 \sim F_{p,n-p}$ | 椭球置信域；联合 $T^2$ 区间或 Bonferroni 区间 | 正态总体；即似然比检验 |
| 两个均值向量（[3.4.4](/3.4.4)） | 检验 $\boldsymbol{\mu}_1 = \boldsymbol{\mu}_2$（成对样本或独立样本） | $T^2 = (\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}\bigl[(\tfrac1{n_1}+\tfrac1{n_2})S_{\mathrm{pooled}}\bigr]^{-1}(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)$ | $F$ 分布；大样本时 $\chi^2_p$ | 协方差相等，或协方差不等时用大样本 |
| PCA（[3.4.5](/3.4.5)） | 用少数互不相关的组合概括变异 | 在 $\boldsymbol{a}^{\mathsf T}\boldsymbol{a} = 1$ 且与前面各成分正交的约束下最大化 $\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X})$ | $\Sigma$（或相关矩阵）的特征向量；解析解 | 无分布假设；不具有量纲不变性 |
| MDS 与核 PCA（[3.4.6](/3.4.6)） | 由距离得到低维构型；非线性结构 | 保持给定的距离；在核函数定义的特征空间中做 PCA | 双中心化距离矩阵或核矩阵的特征分解 | 欧氏距离下的经典 MDS 就是 PCA |
| 线性回归（[3.4.7](/3.4.7)） | 预测连续响应 | $\boldsymbol{Y} = Z\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ | 最小二乘；共线性时用带惩罚的版本 | 正态误差下的推断 |
| 因子分析（[3.4.8](/3.4.8)） | 用 $m < p$ 个隐因子解释协方差 | $\boldsymbol{X} - \boldsymbol{\mu} = L\boldsymbol{F} + \boldsymbol{\varepsilon}$，$\Sigma = LL^{\mathsf T} + \Psi$ | 主成分法或极大似然估计；旋转；因子得分 | 载荷只在旋转意义下可识别；极大似然法假设正态 |
| CCA（[3.4.9](/3.4.9)） | 两组变量之间的关联 | $\max\operatorname{Corr}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_1, \boldsymbol{b}^{\mathsf T}\boldsymbol{X}_2)$ | $\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\Sigma_{11}^{-1/2}$ 的特征向量；解析解 | 相关系数的检验假设正态 |
| 判别分析（[3.4.10](/3.4.10)） | 分到已知的类 | Fisher：$\max\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}/\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}$；似然方法：最小化 ECM | $W^{-1}B$ 的特征向量；LDA、QDA | LDA 要求协方差相等；LDA 与 QDA 的最优性需要正态性 |
| 聚类分析（[3.4.11](/3.4.11)） | 发现未知的类 | 基于连接方式的合并；最小化 SSE；高斯混合似然 | 迭代：合并、$k$ 均值交替步、EM | 距离与 $k$ 的选择；局部最优 |

### 12.1.3. 共同的框架

本课程的大多数方法都沿同一条从总体到样本的路径展开。

- 建模，在总体层面。假设检验从 $H_0$ 出发，其逻辑是"若 $H_0$ 成立，则统计量的行为已知；若统计量不是这样表现，就拒绝 $H_0$"。PCA、CCA 与判别分析从一个要最大化的目标出发，通过特征分解得到解析解；聚类也从一个目标出发，但其求解需要迭代计算。
- 模型或解的性质：成分、因子或判别函数的含义，它们在哪些变换下不变，彼此之间的关系（例如 [3.4.10](/3.4.10#sec-10.5.2) 中 LDA 与 CCA 的关系，经典 MDS 与 PCA 的关系）。
- 应用，在样本层面：估计总体量，并解读每一幅图和每一张表。
- 评价，包括调节参数的选择与模型选择。指标与方法的着眼点不同（更好的解释，或更小的误差），类型也不同：AIC、BIC 等参数化准则，或**交叉验证**等非参数方法。

贯穿始终需要三种能力——代数（几乎每种方法背后的特征分解与奇异值分解）、几何（投影、椭球、距离）与数值计算；以及三类任务——识别问题并建模、求解、解读结果。

因子分析是按这种方式复习一种方法的好模板。

| 步骤 | 内容 |
|---|---|
| 动机 | 降维（$m < p$）与解释 |
| 模型 | $\boldsymbol{X} = \boldsymbol{\mu} + L\boldsymbol{F} + \boldsymbol{\varepsilon}$，其中 $\mathbb{E}\boldsymbol{F} = \boldsymbol{0}$，$\operatorname{Cov}(\boldsymbol{F}) = I$，$\operatorname{Cov}(\boldsymbol{\varepsilon}) = \Psi$ 为对角阵，$\boldsymbol{F}$ 与 $\boldsymbol{\varepsilon}$ 不相关，由此 $\Sigma = LL^{\mathsf T} + \Psi$ |
| 标准化模型 | $V^{-1/2}(\boldsymbol{X}-\boldsymbol{\mu}) = L_z\boldsymbol{F} + \boldsymbol{\varepsilon}_z$，$\rho = L_zL_z^{\mathsf T} + \Psi_z$，$L_z = V^{-1/2}L$：模型具有量纲不变性 |
| 目标 | 总体层面：$L$ 与 $\Psi$（只对某些 $\Sigma$ 存在，且 $L$ 只在旋转意义下唯一）；个体层面：因子得分 $\boldsymbol{F}$ |
| 主成分解 | $\hat L = [\sqrt{\hat\lambda_1}\hat{\boldsymbol{e}}_1, \dots, \sqrt{\hat\lambda_m}\hat{\boldsymbol{e}}_m]$；计算方便（$m$ 增大时前面各列不变），与 PCA 类似；但忽略了模型的结构（例如 $\Psi$ 为对角阵） |
| 极大似然解 | 在可识别性约束 $L^{\mathsf T}\Psi^{-1}L$ 为对角阵下最大化正态似然；对 $S$ 与 $R$ 等价；可以对因子个数作似然比检验；但需要额外的多元正态假设 |

### 12.1.4. 实施一项多元分析

一个数据分析项目通常按如下步骤进行。

1. 从数据和引发研究的问题出发；在选择方法之前先探索数据（EDA）。
2. 规划分析：预处理（EDA、尺度变换、数据变换、离群点），再组合使用方法，例如先 PCA 再 LDA，先 PCA 再聚类，或先做因子分析再对因子得分聚类。
3. 解读每一幅图和每一张表，得出结论，讨论局限。

这样一个项目的摘要应当说清三件事：数据、问题与结论。

## 12.2. 多重检验与错误发现率

### 12.2.1. 族错误率

除了检验关于均值向量的一个假设 $H_0\colon\boldsymbol{\mu}_1 = \boldsymbol{\mu}_2$，我们也许想逐个坐标检验 $H_{0j}\colon\mu_{1j} = \mu_{2j}$（$j = 1, \dots, m$），以找出哪些变量有差异。在 $m$ 适中时，基于 Hotelling $T^2$ 的联合区间可以做到这一点，但当变量个数超过样本量时，本课程的经典检验都会失效。下面的方法在这种情形下同样适用，而且只要检验多于一个假设，多重检验问题就会出现。

设 $p_j$ 是 $H_{0j}$ 的 **p 值**；水平为 $\alpha$ 的检验在 $p_j < \alpha$ 时拒绝 $H_{0j}$，所以每个检验犯**第一类错误**的概率为 $\alpha$。做 $m$ 个检验时，至少犯一次第一类错误的概率大于 $\alpha$。

**定义 12.2.1（族错误率）** 多重检验程序的**族错误率**（FWER）是在 $m$ 个检验中至少犯一次第一类错误的概率。

**Bonferroni 校正**以水平 $\alpha/m$ 检验每个假设。由并集的概率上界，若 $I_0$ 是为真的原假设的集合，

$$
\mathbb{P}\Bigl(\bigcup_{j\in I_0}\{p_j < \alpha/m\}\Bigr) \le \sum_{j\in I_0}\mathbb{P}(p_j < \alpha/m) \le m\cdot\frac{\alpha}{m} = \alpha,
$$
因此无论各检验之间如何相依，FWER 都被控制在 $\alpha$ 水平。

**例 12.2.1** 在一项前列腺癌基因表达研究中（Efron，*Large-Scale Inference*，2010），对 $n_1 = 52$ 名前列腺癌患者和 $n_2 = 50$ 名健康对照测量了 $m = 6033$ 个基因的表达水平，科学问题是哪些基因的表达存在差异。对每个基因计算两样本 $t$ 统计量，并变换为 $z$ 值 $z_j = \Phi^{-1}(F_{t,100}(t_j))$，它在 $H_{0j}$ 下服从标准正态分布。在 $0.05$ 水平的 Bonferroni 阈值下，$6033$ 个基因中只有 $2$ 个被判为显著，尽管 $z$ 值直方图的尾部明显比零分布重：控制 FWER 只能得到很少的发现。

### 12.2.2. 错误发现率

控制 FWER 是保守的。犯几次第一类错误未必很糟，只要它们在全部拒绝中只占很小的比例。把 $m$ 个检验分类如下。

| | $H_0$ 为真 | $H_0$ 为假 | 合计 |
|---|---|---|---|
| 判为显著 | $V$ | $S$ | $R$ |
| 判为不显著 | $U$ | $T$ | $m - R$ |
| 合计 | $m_0$ | $m - m_0$ | $m$ |

只有 $m$ 与 $R$ 是可观测的。用这些记号，$\mathrm{FWER} = \mathbb{P}(V \ge 1)$。

**定义 12.2.2（错误发现率）** 错误发现比例为 $Q = V/\max(R, 1)$（错误拒绝在全部拒绝中所占的比例，无拒绝时取 $0$），它的期望

$$
\mathrm{FDR} = \mathbb{E}[Q] = \mathbb{E}\left[\frac{V}{\max(R, 1)}\right]
$$
称为**错误发现率**（Benjamini 与 Hochberg，1995）。

FDR 与 FWER 有两个基本关系。

1. 若所有原假设都为真（$m_0 = m$），则 $V = R$，于是 $Q = \boldsymbol{1}_{\{V\ge1\}}$，$\mathrm{FDR} = \mathbb{P}(V \ge 1) = \mathrm{FWER}$。
2. 一般地 $Q \le \boldsymbol{1}_{\{V\ge1\}}$，所以 $\mathrm{FDR} \le \mathrm{FWER}$，任何控制 FWER 的程序也控制 FDR。只控制 FDR 的程序要求较宽，因而可能有更高的功效。当 $m - m_0$ 较大时，$S$ 往往较大，$\mathbb{E}[Q]$ 与 $\mathbb{P}(V \ge 1)$ 的差别也大。

因此在 $\alpha$ 水平控制 FDR 比在 $\alpha$ 水平控制 FWER 保守程度低：它容许若干次第一类错误，只要这些错误在"发现"（被拒绝的原假设）中所占的比例不太高。

### 12.2.3. Benjamini–Hochberg 方法

**算法 12.2.1（Benjamini–Hochberg 方法）** 设 $p_{(1)} \le p_{(2)} \le \cdots \le p_{(m)}$ 为排序后的 p 值，$H_{(i)}$ 为相应的假设，取定 $\alpha \in (0, 1)$。

1. 令 $k = \max\{i : p_{(i)} \le \frac{i}{m}\alpha\}$（若不存在这样的 $i$，则 $k = 0$）。
2. 拒绝 $H_{(1)}, \dots, H_{(k)}$。

阈值 $\frac{i}{m}\alpha$ 从 Bonferroni 阈值 $\alpha/m$ 线性增大到 $\alpha$。这是一个逐步向上（step-up）的程序：它从最大的 p 值向下搜索，拒绝直到最后一次穿越为止的全部假设，即使其中某些较小的 p 值高于各自的阈值。

**定理 12.2.1** 若检验统计量相互独立，且为真的原假设的 p 值服从 $(0, 1)$ 上的均匀分布，则 Benjamini–Hochberg 方法满足

$$
\mathrm{FDR} = \frac{m_0}{m}\alpha \le \alpha.
$$
在一种正相依条件下，界 $\mathrm{FDR} \le \alpha$ 仍然成立（Benjamini 与 Yekutieli，2001）。

**证明** 记 $\alpha_k = \frac{k}{m}\alpha$。对为真的原假设 $H_i$ 与 $k = 1, \dots, m$，令 $C_k^{(i)}$ 为由其余 $m-1$ 个 p 值决定的事件："若 $H_i$ 被拒绝，则总共恰好拒绝 $k$ 个假设"。对每个 $i$，这些事件互不相交且必有一个发生，所以 $\sum_k\mathbb{P}(C_k^{(i)}) = 1$。对逐步向上程序，$\{H_i \text{ 被拒绝且 } R = k\} = \{p_i \le \alpha_k\}\cap C_k^{(i)}$。因此对 $m_0$ 个为真的原假设求和并利用独立性，

$$
\begin{aligned}
\mathbb{E}[Q] &= \sum_{i\in I_0}\sum_{k=1}^m\frac1k\,\mathbb{P}\bigl(p_i \le \alpha_k,\ C_k^{(i)}\bigr) = \sum_{i\in I_0}\sum_{k=1}^m\frac1k\,\mathbb{P}(p_i \le \alpha_k)\,\mathbb{P}\bigl(C_k^{(i)}\bigr) \\
&= \sum_{i\in I_0}\sum_{k=1}^m\frac1k\cdot\frac{k}{m}\alpha\,\mathbb{P}\bigl(C_k^{(i)}\bigr) = \frac{\alpha}{m}\sum_{i\in I_0}\sum_{k=1}^m\mathbb{P}\bigl(C_k^{(i)}\bigr) = \frac{m_0}{m}\alpha. \qquad \square
\end{aligned}
$$

**例 12.2.2** 对前列腺数据，在 $0.05$ 水平下 Benjamini–Hochberg 方法得到的发现比 Bonferroni 多得多：$21$ 个基因而不是 $2$ 个。平均而言，这些发现中错误的至多占 $5\%$。

![模拟数据上的 Benjamini–Hochberg 方法：1000 个检验，其中 100 个有真实效应。排序后的 p 值对其秩作图，并画出 BH 直线 i alpha/m 与 Bonferroni 阈值 alpha/m（对数刻度）；BH 拒绝直到最后一个低于其直线的 p 值为止的全部假设。](./plots/bh-procedure.py)

较新的工作在许多方向上推广了 FDR 控制，例如基于 e 值的方法（Wang 与 Ramdas，2022）。

## 12.3. 对应分析

### 12.3.1. 列联表的卡方统计量

对应分析处理一种新类型的数据：二维计数**列联表**。例如，五个物种在三个样地的多度为

$$
F = [f_{ij}] = \begin{bmatrix} 45 & 10 & 15 & 0 & 10 \\ 25 & 8 & 10 & 0 & 3 \\ 7 & 15 & 20 & 14 & 12 \end{bmatrix}, \qquad \text{行和 } f_{i+} = 80, 46, 68, \quad \text{列和 } f_{+j} = 77, 33, 45, 14, 25, \quad f_{++} = 194,
$$
各行为样地 1–3，各列为物种 1–5。样地与物种之间是否有关联？Pearson 卡方**独立性检验**回答了这个问题。记 $r$、$c$ 为行数与列数，定义对应矩阵（correspondence matrix）$P = [p_{ij}]$，$p_{ij} = f_{ij}/f_{++}$，行质量 $p_{i+} = f_{i+}/f_{++}$，列质量 $p_{+j} = f_{+j}/f_{++}$。则

$$
\chi^2 = \sum_{i=1}^r\sum_{j=1}^c\frac{\bigl(f_{ij} - f_{++}\frac{f_{i+}}{f_{++}}\frac{f_{+j}}{f_{++}}\bigr)^2}{f_{++}\frac{f_{i+}}{f_{++}}\frac{f_{+j}}{f_{++}}} = f_{++}\sum_{i=1}^r\sum_{j=1}^c\frac{(p_{ij} - p_{i+}p_{+j})^2}{p_{i+}p_{+j}},
$$
在独立性下它近似服从自由度为 $(r-1)(c-1)$ 的**卡方分布**。本例中 $\chi^2 = 55.25$，自由度 $8$，p 值约为 $4\times10^{-9}$：样地与物种显然有关联。对应分析展示这种关联是怎样的。

### 12.3.2. 计算

把表格变换为标准化残差，其平方就是各格对卡方统计量的贡献：

$$
\bar q_{ij} = \frac{p_{ij} - p_{i+}p_{+j}}{\sqrt{p_{i+}p_{+j}}}, \qquad \bar Q = [\bar q_{ij}] = D_r^{-1/2}(P - \boldsymbol{r}\boldsymbol{c}^{\mathsf T})D_c^{-1/2},
$$
其中 $D_r = \operatorname{diag}(p_{1+}, \dots, p_{r+})$，$D_c = \operatorname{diag}(p_{+1}, \dots, p_{+c})$，$\boldsymbol{r}, \boldsymbol{c}$ 是行质量与列质量组成的向量。本例中

$$
\bar Q = \begin{bmatrix} 0.169 & -0.070 & -0.059 & -0.173 & -0.007 \\ 0.113 & 0.004 & -0.015 & -0.131 & -0.086 \\ -0.276 & 0.072 & 0.076 & 0.295 & 0.079 \end{bmatrix},
$$
并且 $\chi^2 = f_{++}\sum_{i,j}\bar q_{ij}^2 = f_{++}\|\bar Q\|_{\mathrm{F}}^2$。矩阵 $P - \boldsymbol{r}\boldsymbol{c}^{\mathsf T}$ 是从表中随机抽取一个观测时其行示性向量与列示性向量之间的协方差矩阵 $\Sigma_{12}$，所以 $\bar Q = D_r^{-1/2}\Sigma_{12}D_c^{-1/2}$ 很像典型相关分析中研究的矩阵。为提取其中的关系，作**奇异值分解**

$$
\bar Q = U\Lambda V^{\mathsf T}, \qquad U \in \mathbb{R}^{r\times k}, \quad \Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_k), \quad V \in \mathbb{R}^{c\times k},
$$
非零奇异值有 $k \le \min(r, c) - 1$ 个。总惯量 $\chi^2/f_{++} = \sum_l\lambda_l^2$ 在各轴之间分配；本例中 $\lambda_1 = 0.527$，$\lambda_2 = 0.083$，第一轴承载了 $97.6\%$ 的惯量。

**定义 12.3.1（对应分析）** **对应分析**（CA）用低维图（CA 双标图）中的点表示列联表的行与列，点的位置显示关联，所用坐标为

| | 尺度 1 | 尺度 2 |
|---|---|---|
| 行（样地） | $F = D_r^{-1/2}U\Lambda$ | $B = D_r^{-1/2}U$ |
| 列（物种） | $A = D_c^{-1/2}V$ | $G = D_c^{-1/2}V\Lambda$ |

数据必须非负，且是频数一类的量。

把每一行看作剖面 $(p_{i1}/p_{i+}, \dots, p_{ic}/p_{i+})$，两行之间自然的距离是卡方距离（chi-square distance）

$$
D^2(i, i') = \sum_{j=1}^c\frac{1}{p_{+j}}\left(\frac{p_{ij}}{p_{i+}} - \frac{p_{i'j}}{p_{i'+}}\right)^2,
$$
即每一列按其质量的倒数加权后的剖面间欧氏距离，使稀有物种不被常见物种淹没。CA 保持卡方距离：在尺度 1 中，行点 $F$ 之间的欧氏距离（用全部 $k$ 个轴）等于行剖面之间的卡方距离；在尺度 2 中，列点 $G$ 也是如此。

- 主要关心样地之间的关系时用尺度 1。物种的位置使每个样地靠近在那里多度高的物种。本例中，物种 1 离样地 1、2 比离样地 3 近，因为它在样地 1、2 的多度更高。
- 主要关心物种之间的关系时用尺度 2。样地按物种多度分布在物种周围：物种 5 在样地 1、3 比在样地 2 多，物种 1 在样地 1、2 比在样地 3 多，而只在样地 3 出现的物种 4 与样地 3 重合。

![样地—物种表的 CA 双标图。左（尺度 1）：样地之间为卡方距离，物种按其贡献定位。右（尺度 2）：物种之间为卡方距离，样地按物种多度定位。](./plots/ca-biplots.py)

**注 12.3.1（CA 与 CCA）** CA 可以写成一个典型相关问题。设 $\boldsymbol{X}$ 为从表中随机抽取的一个观测的行示性向量，$\boldsymbol{Y}$ 为其列示性向量，CA 求解

$$
\max_{\|\boldsymbol{a}\| = \|\boldsymbol{b}\| = 1}\operatorname{Corr}\bigl(\boldsymbol{a}^{\mathsf T}D_r^{-1/2}\boldsymbol{X}, \boldsymbol{b}^{\mathsf T}D_c^{-1/2}\boldsymbol{Y}\bigr) = \max_{\|\boldsymbol{a}\| = \|\boldsymbol{b}\| = 1}\boldsymbol{a}^{\mathsf T}D_r^{-1/2}\Sigma_{12}D_c^{-1/2}\boldsymbol{b},
$$
它与 CCA 的 $\max_{\|\boldsymbol{a}\| = \|\boldsymbol{b}\| = 1}\boldsymbol{a}^{\mathsf T}\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1/2}\boldsymbol{b}$ 完全平行；这里 $D_r$ 与 $D_c$ 扮演 $\Sigma_{11}$ 与 $\Sigma_{22}$ 的角色（它们是示性向量的协方差矩阵，只差一个去掉平凡解的秩一项）。$\bar Q$ 的奇异值就是行类别与列类别之间的典型相关系数。在 R 中，例如程序包 vegan 提供了 CA。

## 12.4. 主成分分析的推广

### 12.4.1. 稀疏主成分分析

设 $X$ 是列均值已减去的 $n \times p$ 数据矩阵。PCA 可以写成两种等价形式：

$$
\max_{\boldsymbol{a}}\boldsymbol{a}^{\mathsf T}X^{\mathsf T}X\boldsymbol{a} \ \text{ 使得 } \boldsymbol{a}^{\mathsf T}\boldsymbol{a} = 1, \qquad \text{或} \qquad \min_{Y, A}\|X - YA^{\mathsf T}\|_{\mathrm{F}}^2 \ \text{ 使得 } A^{\mathsf T}A = I_r,
$$
其中 $A$ 是 $p \times r$ 载荷矩阵，$Y = XA$ 是 $n \times r$ 得分矩阵。每个主成分通常涉及全部 $p$ 个变量，$p$ 很大时难以解释。稀疏主成分分析（sparse PCA）的思想与 **Lasso** 类似：加上 $\ell_1$ 惩罚，

$$
\min_{Y, A}\|X - YA^{\mathsf T}\|_{\mathrm{F}}^2 + \gamma\sum_{i=1}^n\|\boldsymbol{y}_i\|_1 + \lambda\sum_{j=1}^p\|\boldsymbol{a}_j\|_1,
$$
其中 $\boldsymbol{y}_i$ 是 $Y$ 的行，$\boldsymbol{a}_j$ 是 $A$ 的行。对 $A$ 的惩罚使每个成分的含义只依赖于少数原始变量；对 $Y$ 的惩罚使每个观测的投影只依赖于少数成分。$\ell_1$ 惩罚产生精确的零，$\ell_2$ 惩罚只是使系数整体变小。人们提出了不同的表述，例如 Zou、Hastie 与 Tibshirani（2006）用弹性网回归的表述，d'Aspremont 等（2007）用半定松弛；在后者的一个基因表达例子中，涉及 500 个基因的主导成分被一个只涉及 14 个基因的稀疏成分所取代。

### 12.4.2. 其他数据类型的 PCA

对二元数据 $x_{ij} \in \{-1, 1\}$，平方误差不是自然的损失。logistic 主成分分析（logistic PCA）用 logistic 损失代替它：

$$
\min_{Y, A}\sum_{i=1}^n\sum_{j=1}^p\ln\Bigl(1 + \exp\Bigl\{-x_{ij}\sum_{k=1}^r y_{ik}A_{jk}\Bigr\}\Bigr),
$$
于是 $\sum_k y_{ik}A_{jk}$ 是 $x_{ij}$ 的自然参数（对数优势）。一般的原则是：普通 PCA 是正态模型下的低秩拟合，自然指数族 $p(x; \theta) = p_0(x)\exp\{\theta x - G(\theta)\}$ 的其他成员导出其他数据类型的 PCA，平方误差换成相应的 Bregman 散度——凸函数 $G$ 与其线性近似之间的差距。计数数据的 Poisson PCA 和有序数据的版本（Rennie 与 Srebro，2005）遵循同样的模式；分类主成分分析则先用线性、多项式或样条函数变换各个类别，再做 PCA。

## 12.5. 判别分析的推广

### 12.5.1. 正则化判别分析

LDA 使用一个合并协方差矩阵，QDA 对每一类各用一个。正则化判别分析（regularized discriminant analysis）即 RDA，是两者的折中：它把每个 $\hat\Sigma_k$ 向合并协方差矩阵 $\hat\Sigma$ 收缩，

$$
\hat\Sigma_k(\alpha) = \alpha\hat\Sigma_k + (1-\alpha)\hat\Sigma, \qquad \alpha \in [0, 1],
$$
并在二次判别函数中用 $\hat\Sigma_k(\alpha)$ 代替 $\hat\Sigma_k$。调节参数 $\alpha$ 决定协方差是分别估计（$\alpha = 1$，QDA）还是合并（$\alpha = 0$，LDA）。此外，$\hat\Sigma$ 本身还可以向数量协方差矩阵收缩，$\hat\Sigma(\gamma) = \gamma\hat\Sigma + (1-\gamma)\hat\sigma^2 I$，$\gamma = 1$ 给出合并协方差，$\gamma = 0$ 给出数量协方差。用 $\hat\Sigma_k(\alpha, \gamma)$ 代替 $\hat\Sigma_k$ 就得到一个双参数族，$\alpha$ 与 $\gamma$ 由交叉验证选择。作为一种正则化技术，RDA 在有许多可能相关的特征、样本协方差矩阵不稳定或奇异时特别有用；简单形式 $S_{\mathrm{pooled}} + \lambda I_p$ 已在 [3.4.10](/3.4.10#sec-10.7.3) 中提到。

### 12.5.2. Logistic 回归

[3.4.10](/3.4.10#sec-10.3.3) 的贝叶斯分类器比较后验概率

$$
\mathbb{P}(\pi_1 \mid \boldsymbol{x}) = \frac{p_1f_1(\boldsymbol{x})}{p_1f_1(\boldsymbol{x}) + p_2f_2(\boldsymbol{x})}, \qquad \mathbb{P}(\pi_2 \mid \boldsymbol{x}) = \frac{p_2f_2(\boldsymbol{x})}{p_1f_1(\boldsymbol{x}) + p_2f_2(\boldsymbol{x})}.
$$
LDA 通过对密度 $f_i$ 建模得到它们，logistic 回归则直接对后验概率建模。

**定义 12.5.1（Logistic 回归）** 对 $K$ 类，**logistic 回归**模型设定：对 $k = 1, \dots, K-1$，

$$
\ln\frac{\mathbb{P}(\pi_k \mid \boldsymbol{x})}{\mathbb{P}(\pi_K \mid \boldsymbol{x})} = \beta_{0k} + \boldsymbol{\beta}_k^{\mathsf T}\boldsymbol{x},
$$
等价地

$$
\mathbb{P}(\pi_k \mid \boldsymbol{x}) = \frac{\exp(\beta_{0k} + \boldsymbol{\beta}_k^{\mathsf T}\boldsymbol{x})}{1 + \sum_{l=1}^{K-1}\exp(\beta_{0l} + \boldsymbol{\beta}_l^{\mathsf T}\boldsymbol{x})}, \quad k < K, \qquad \mathbb{P}(\pi_K \mid \boldsymbol{x}) = \frac{1}{1 + \sum_{l=1}^{K-1}\exp(\beta_{0l} + \boldsymbol{\beta}_l^{\mathsf T}\boldsymbol{x})}.
$$
参数通过最大化给定 $\boldsymbol{x}_i$ 时标签的条件似然来估计，新观测分到拟合概率最大的类。$K = 2$ 时模型为 $\ln\frac{p}{1-p} = \beta_0 + \boldsymbol{\beta}^{\mathsf T}\boldsymbol{x}$，$p = \mathbb{P}(\pi_1\mid\boldsymbol{x})$。

两种方法关系密切。在 LDA 模型下，由定理 10.4.1 的证明，

$$
\ln\frac{\mathbb{P}(\pi_1 \mid \boldsymbol{x})}{\mathbb{P}(\pi_2 \mid \boldsymbol{x})} = \ln\frac{p_1}{p_2} + (\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}\boldsymbol{x} - \frac12(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1+\boldsymbol{\mu}_2),
$$
它是 $\boldsymbol{x}$ 的线性函数：后验对数优势恰好具有 logistic 形式。差别在于估计方式。LDA 估计 $(\boldsymbol{x}, \text{类别})$ 的联合分布，在正态模型成立时更有效；logistic 回归对 $\boldsymbol{x}$ 的分布不作假设，因而更稳健，其系数作为对数优势比也有清楚的解释。对鸢尾花数据，logistic 回归可以分开两个品种，多类模型可以分开全部三个品种，误判率与 LDA 相近。logistic 回归是广义线性模型与分类数据分析课程的内容。

### 12.5.3. k 近邻

**算法 12.5.1（k 近邻）** 给定带标签的数据 $(\boldsymbol{x}_i, y_i)$、点间距离（例如欧氏距离）与近邻个数 $k$（例如 $k = 5$）：对新单元 $\boldsymbol{x}$ 分类时，找出离 $\boldsymbol{x}$ 最近的 $k$ 个训练点，把 $\boldsymbol{x}$ 分到其中出现最多的类。

$k$ 近邻（KNN）分类器的思想是"物以类聚，人以群分"。由于它依赖距离，应先把变量标准化。$k$ 控制规则的灵活程度：$k = 1$ 给出非常不规则、紧跟每个训练点的分界；$k$ 很大（如 $k = 30$）时分界光滑，但可能漏掉真实的结构。$k$ 按预测准确度用交叉验证选择：对一个范围内的每个 $k$，计算交叉验证的预测误差（例如在训练集上做 $10$ 折交叉验证），选验证误差最小的 $k$（在一个鸢尾花数据的例子中为 $k = 6$），最后在一个独立的测试集上对选定的规则评价一次，以估计其误差。

KNN 是非参数方法：不需要分布假设，实现简单，$k$ 适中时个别离群的训练点对它影响不大。它的缺点是计算与存储代价高（要保存全部训练数据，每次预测都要搜索），预测误差对各类样本量的不平衡敏感，不能给出数据的结构描述，在高维中表现差——高维中所有点彼此都很远。

各分类器相比如何？在一个 $p = 2$ 个预测变量、$g = 2$ 类的模拟中，有六种情形（协方差矩阵相等的正态总体，分无相关与有相关两种；线性分界的 $t$ 分布数据；相关系数不等的正态总体；含二次项 $X_1^2, X_2^2, X_1X_2$ 的 logistic 模型；更复杂的非线性分界），真实分界为线性时 LDA 与 logistic 回归的测试误判率最小，分界为二次时 QDA 最好，分界高度非线性时用交叉验证选 $k$ 的 KNN 最好。没有哪种方法在所有情形下都最好；选择应与分界的形状和数据量相匹配。

## 12.6. 网络分析

传统的多元数据记录个体实体的属性（特征、协变量）。网络数据是关系型的：记录实体之间的关系。例如社交媒体（结点是用户，边是好友或关注关系）、生物学（基因与蛋白质，边是调控关系）、神经科学（脑区及其连接）和交通（机场与直飞航线）。关系可以直接观测——这是网络分析的对象——也可以由结点特征推断；这里只介绍在观测到的关系中发现结构的问题。

$n$ 个实体（结点）及其观测到的关系（边）构成的网络用 $n \times n$ **邻接矩阵** $A$ 表示：若有从 $i$ 到 $j$ 的边则 $A_{ij} = 1$，否则为 $0$。无向网络（$i$ 与 $j$ 是朋友）满足 $A = A^{\mathsf T}$；有向网络（$i$ 给 $j$ 发了邮件）则不一定。更一般地，边可以带权或带符号；贝叶斯网络与概率图模型以另一种方式使用图，即编码条件独立性。

二元的 $A_{ij}$ 可以用 $\mathbb{P}(A_{ij} = 1) = P_{ij}$ 的 Bernoulli 分布建模，$n \times n$ 矩阵 $P = \mathbb{E}A = [P_{ij}]$ 包含全部信息。通常假设给定 $P$ 时各边独立，这并不总是现实的，但大大简化了分析。问题是由一个观测到的 $A$ 估计 $P$。不加假设这是不可能的，因为每个 $P_{ij}$ 的样本量只有 1，所以必须假设某种结构：

- 社区：$P$ 有分块结构；
- 低秩：$P$ 是低秩矩阵（比社区更一般）；
- 光滑图元（graphon）：在结点的某个置换下，$P$ 在其 $n \times n$ 网格上光滑变化；
- 隐变量模型：边的概率是结点的隐特征和/或观测特征的函数。

**定义 12.6.1（随机块模型）** 对有 $K$ 个社区的无向网络，**随机块模型**（SBM；Holland、Laskey 与 Leinhardt，1983）假设每个结点 $i$ 独立地以概率 $\boldsymbol{\pi} = (\pi_1, \dots, \pi_K)$ 被赋予社区标签 $c_i \in \{1, \dots, K\}$，给定标签时各边是独立的 Bernoulli 变量，

$$
\mathbb{P}(A_{ij} = 1) = B_{c_ic_j},
$$
其中 $B$ 是 $K \times K$ 的对称连接概率矩阵。

这是对结点的基于模型的聚类，结构与 [3.4.11](/3.4.11) 的高斯混合相同，只是把正态观测换成了 Bernoulli 边。写成矩阵形式：令 $\boldsymbol{z}_i$ 为长度 $K$ 的向量，$Z_{ik} = \boldsymbol{1}_{\{c_i = k\}}$，把它们作为行排成 $n \times K$ 矩阵 $Z$。则

$$
\mathbb{E}A = P = ZBZ^{\mathsf T}
$$
（对角线以外），这是一个秩至多为 $K$ 的分块常数矩阵。例如两个社区时，$P$ 有两个由社区内连接概率构成的对角块，以及两个由社区间连接概率构成的非对角块。

社区发现（community detection）是由 $A$ 恢复 $Z$ 并估计 $B$ 的问题。若知道标签，按社区给结点排序就能在 $A$ 中看到分块；但标签未知，观测到的 $A$ 看不出任何模式。人们发展了许多拟合 SBM 的方法，例如变分推断、伪似然、谱方法（对 $A$ 的前几个特征向量聚类）和置信传播；它们属于统计学习与机器学习。一个应用是统计学家的引用网络（Ji 与 Jin，2016），其社区对应于研究领域。

怎样选择社区个数 $K$？模型很多（SBM 有许多推广），带调节参数的拟合方法也很多。交叉验证仍是自然的答案，但网络的训练—测试划分并不显然，因为一个结点的边依赖于其他所有结点。网络交叉验证（Chen 与 Lei，2018）随机选取 $n_1$ 个结点，把邻接矩阵分成块 $A_{11}, A_{12}, A_{22}$；在 $(A_{11}, A_{12})$ 上拟合模型——对标准方法稍作修改就仍能恢复分块——再在 $A_{22}$ 上检验。它是为分块模型设计的。

## 12.7. 矩阵时间序列的因子模型

时间序列是以离散时间 $t$ 为指标的随机变量序列 $X_1, X_2, \dots, X_t, \dots$。传统的时间序列分析处理一元、多元和面板观测，使用线性模型（ARMA）、非线性模型（门限、机制转换、GARCH）和非参数模型（函数系数、可加、单指标）。在大数据时代，许多新类型的数据在时间上被观测并带有时间相依性：交通网络与社交网络、文本、图像。这些就是现代时间序列。

矩阵时间序列是按时间观测的矩阵形式的观测序列 $Y_t$，例如一组国家的一组经济指标、一组公司的一组财务特征，或一组国家之间的进出口额，每季度记录一次。把 $Y_t$ 拉直成向量再用 [3.4.8](/3.4.8) 的因子模型，会忽略行与列的结构。

**定义 12.7.1（矩阵因子模型）** $m \times n$ 矩阵时间序列的**矩阵因子模型**为

$$
Y_t = \Lambda F_t\Gamma^{\mathsf T} + U_t,
$$
其中 $F_t$ 是 $r_1 \times r_2$ 的隐因子矩阵，$\Lambda$（$m \times r_1$）与 $\Gamma$（$n \times r_2$）分别是行载荷矩阵与列载荷矩阵，$U_t$ 是噪声。按元素写，

$$
y_{t,ij} = \sum_{l=1}^{r_1}\sum_{k=1}^{r_2}\lambda_{il}f_{t,lk}\gamma_{jk} + u_{t,ij}.
$$

模型通过 $\Lambda$ 刻画行之间的结构关系，通过 $\Gamma$ 刻画列之间的结构关系，参数远少于对拉直数据的因子模型。Wang、Liu 与 Chen（2019）研究了它的可识别性、通过行与列交叉自协方差矩阵平方的特征分析进行估计、$m, n, T \to \infty$ 时的渐近性质以及实证应用；Chen、Tsay 与 Chen（2020）研究了带约束的矩阵因子模型。把它用于进出口数据，行因子与列因子识别出贸易枢纽；比较 1983–1987 与 2001–2005 两个时期，可以看出枢纽如何变化。

## 12.8. 进一步的方向

本章的延伸分为四类：同一问题的更好解法（以 FDR 代替 FWER，正则化 LDA），类似问题的新方法（稀疏 PCA 与核 PCA），新类型的数据（对应分析、logistic PCA、矩阵因子模型、网络），以及从不同视角看同一问题（KNN 与 logistic 回归，即机器学习对分类的视角）。它们也指出了多元分析继续发展的方向。

| 方向 | 展开的地方 | 本课程中的例子 |
|---|---|---|
| 参数 → 非参数 | [非参数统计](/3.6) | FDR、KNN |
| 线性 → 非线性 | 统计学习 | 核 PCA、稀疏 PCA、SVM |
| 独立观测 → 时间序列 | 时间序列分析 | 矩阵因子模型 |
| 连续 → 离散数据 | logistic 回归、分类数据分析 | 对应分析、logistic PCA、logistic 回归 |
| 相关 → 因果 | [因果推断](/3.9) | 网络分析 |
| 先验与后验推断 | [贝叶斯统计](/3.7) | 贝叶斯分类器、贝叶斯高斯混合 |
| 算法 | [统计计算](/3.5) | EM 算法、SVD、迭代式聚类 |
