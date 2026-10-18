---
title: 单总体均值的推断
description: 正态样本的样本均值向量与样本协方差矩阵的抽样分布与 Wishart 分布；Hotelling T² 统计量、其 F 分布、均值向量的检验及其不变性；置信椭球；线性组合的单个区间、Bonferroni 区间与 T² 联合置信区间；T² 与似然比检验的关系。
source_hash: 0f4ff070b619
---

本章把正态总体均值的推断（[3.2.4](/3.2.4)、[3.2.5](/3.2.5)）推广到协方差矩阵未知时的均值向量。每个一维对象都有 $p$ 维的对应：样本方差变为样本协方差矩阵，其分布是 Wishart 分布（尺度化卡方分布的矩阵版本）；$t$ 统计量的平方变为 Hotelling $T^2$ 统计量，适当缩放后仍服从 $F$ 分布；置信区间变为置信椭球。但有一个想法在一维中没有对应：面对多个均值或它们的多个线性组合时，我们通常希望这些区间同时正确，本章比较 Bonferroni 区间与由置信椭球得到的 $T^2$ 区间。所用工具是多元正态分布的性质（[3.4.2](/3.4.2)）与最大化引理（[3.4.1](/3.4.1)）。两个及多个均值向量的比较与大样本推断见 [3.4.4](/3.4.4)。

## 3.1. 问题设定与抽样分布

### 3.1.1. 引例与模型

**例 3.1.1（职业评分）** O*NET 数据库按六项工作价值对职业评分：成就（Achievement，职业能让员工运用最强的能力，取得成果并获得成就感）、工作条件（Working Conditions，工作上的安全感和良好的工作环境）、认可（Recognition，晋升机会、领导潜力与声望）、人际关系（Relationships，在友好、非竞争的环境中为他人服务、与同事合作）、支持（Support，支持性的管理，让员工感到公司站在他们身后）与独立（Independence，独立工作并自主决策）。对建筑、工程及相关领域的 $n = 55$ 种职业（建筑师、景观设计师、制图师、测量师、航空航天工程师……），六项评分的样本均值为

| 成就 | 独立 | 认可 | 人际关系 | 支持 | 工作条件 |
|---|---|---|---|---|---|
| 5.118 | 5.021 | 4.717 | 3.668 | 4.592 | 5.101 |

自然的问题是：均值向量是否等于某个假设值？对整个均值向量有多大把握？对 $\frac{1}{2}\mu_{\text{成就}} + \frac{1}{2}\mu_{\text{独立}}$ 这样的综合值有多大把握？若同时关心几个这样的综合值又如何？

全章假定 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的随机样本，$\boldsymbol{\mu}$ 与 $\Sigma$ 都未知：各 $\boldsymbol{X}_j$ 相互独立，且每个 $\boldsymbol{X}_j \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$。点估计量为 $\bar{\boldsymbol{X}}$ 与 $S = \frac{1}{n-1}\sum_j(\boldsymbol{X}_j - \bar{\boldsymbol{X}})(\boldsymbol{X}_j - \bar{\boldsymbol{X}})^{\mathsf T}$，它们是无偏的（定理 2.2.1），除因子 $\frac{n-1}{n}$ 外就是极大似然估计（定理 2.5.1），并且是充分的（定理 2.5.2）。推断需要它们的联合分布。

两个概率工具是定理 2.4.7——对 $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 有 $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_p$——与关于独立正态向量线性组合 $\sum_jc_j\boldsymbol{X}_j$ 的定理 2.4.8。向量的线性组合可以像标量那样写，只是用单位矩阵块代替系数：$\bar{\boldsymbol{X}} = \frac{1}{n}\boldsymbol{X}_1 + \cdots + \frac{1}{n}\boldsymbol{X}_n = \frac{1}{n}[I_p, \dots, I_p](\boldsymbol{X}_1^{\mathsf T}, \dots, \boldsymbol{X}_n^{\mathsf T})^{\mathsf T}$，正如一维中 $\bar X = \frac{1}{n}(1, \dots, 1)(X_1, \dots, X_n)^{\mathsf T}$。例如 $p = 2$、$n = 2$ 时，$\begin{bmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{bmatrix}(X_{11}, X_{12}, X_{21}, X_{22})^{\mathsf T} = \boldsymbol{X}_1 + \boldsymbol{X}_2$。两个这样的组合 $\sum_jc_j\boldsymbol{X}_j$ 与 $\sum_jb_j\boldsymbol{X}_j$ 的协方差为 $\sum_jc_jb_j\Sigma$，当 $\sum_jb_jc_j = 0$ 时二者独立。

### 3.1.2. Wishart 分布

一维中，若 $z_1, \dots, z_m$ 独立同分布于 $\mathcal{N}(0, \sigma^2)$，则 $\sum_iz_i^2 \sim \sigma^2\chi^2_m$。多元的类比是用外积代替平方。

**定义 3.1.1（Wishart 分布）** 设 $\boldsymbol{Z}_1, \dots, \boldsymbol{Z}_m$ 独立同分布于 $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$。称 $p \times p$ 随机矩阵

$$
\sum_{j=1}^{m}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}
$$
的分布为自由度为 $m$、尺度矩阵为 $\Sigma$ 的 **Wishart 分布**，记作 $W_p(m, \Sigma)$。

这一分布以 John Wishart 命名，他于 1928 年导出了它。它是尺度化卡方分布的多元类比：$W_1(m, \sigma^2) = \sigma^2\chi^2_m$，$A \sim W_p(m, \Sigma)$ 的对角元服从 $\sigma_{kk}\chi^2_m$。其均值为 $\mathbb{E}A = m\Sigma$。当 $m \ge p$ 且 $\Sigma$ 正定时，$A$ 以概率一正定，并有密度，本课程不需要它；也有文献把同一分布记作 $W_m(\cdot \mid \Sigma)$。除了多元分析中的检验问题，它在 Bayes 统计中是精度矩阵的共轭先验。

**性质 3.1.1** 设 $A_1 \sim W_p(m_1, \Sigma)$ 与 $A_2 \sim W_p(m_2, \Sigma)$ 独立，$A \sim W_p(m, \Sigma)$，则

1. $A_1 + A_2 \sim W_p(m_1 + m_2, \Sigma)$；
2. 对任意 $q \times p$ 常数矩阵 $C$（特别是 $p \times p$ 可逆矩阵 $C$），$CAC^{\mathsf T} \sim W_q(m, C\Sigma C^{\mathsf T})$。

两条都由定义得到：第一条把两组 $\boldsymbol{Z}_j$ 合在一起；第二条注意 $CAC^{\mathsf T} = \sum_j(C\boldsymbol{Z}_j)(C\boldsymbol{Z}_j)^{\mathsf T}$，而 $C\boldsymbol{Z}_j$ 独立同分布于 $\mathcal{N}_q(\boldsymbol{0}, C\Sigma C^{\mathsf T})$。

### 3.1.3. 样本均值向量与样本协方差矩阵的联合分布

**定理 3.1.1** 设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的随机样本，则

1. $\bar{\boldsymbol{X}} \sim \mathcal{N}_p\left(\boldsymbol{\mu}, \frac{1}{n}\Sigma\right)$；
2. $(n-1)S \sim W_p(n-1, \Sigma)$；
3. $\bar{\boldsymbol{X}}$ 与 $S$ 独立。

**证明** 设 $Q = (q_{jl})$ 为 $n \times n$ Helmert 矩阵

$$
Q = \begin{bmatrix} \frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \cdots & \frac{1}{\sqrt{n}} \\ \frac{1}{\sqrt{2 \cdot 1}} & \frac{-1}{\sqrt{2 \cdot 1}} & 0 & \cdots & 0 \\ \frac{1}{\sqrt{3 \cdot 2}} & \frac{1}{\sqrt{3 \cdot 2}} & \frac{-2}{\sqrt{3 \cdot 2}} & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ \frac{1}{\sqrt{n(n-1)}} & \frac{1}{\sqrt{n(n-1)}} & \frac{1}{\sqrt{n(n-1)}} & \cdots & \frac{-(n-1)}{\sqrt{n(n-1)}} \end{bmatrix},
$$
它是正交矩阵，第一行为 $\boldsymbol{1}_n^{\mathsf T}/\sqrt{n}$；其余各行与第一行正交，所以元素之和为零。对 $l = 1, \dots, n$ 定义 $\boldsymbol{Z}_l = \sum_{j=1}^{n}q_{lj}(\boldsymbol{X}_j - \boldsymbol{\mu})$。由定理 2.4.8，各 $\boldsymbol{Z}_l$ 联合正态，$\operatorname{Cov}(\boldsymbol{Z}_l, \boldsymbol{Z}_{l'}) = \left(\sum_jq_{lj}q_{l'j}\right)\Sigma$；由于 $Q$ 的各行标准正交，$l = l'$ 时它为 $\Sigma$，否则为 $O$。因此 $\boldsymbol{Z}_1, \dots, \boldsymbol{Z}_n$ 独立同分布于 $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$。而 $\boldsymbol{Z}_1 = \sqrt{n}(\bar{\boldsymbol{X}} - \boldsymbol{\mu})$，这给出第 1 条；又因 $Q$ 正交，

$$
\sum_{l=1}^{n}\boldsymbol{Z}_l\boldsymbol{Z}_l^{\mathsf T} = \sum_{j=1}^{n}(\boldsymbol{X}_j - \boldsymbol{\mu})(\boldsymbol{X}_j - \boldsymbol{\mu})^{\mathsf T} = (n-1)S + n(\bar{\boldsymbol{X}} - \boldsymbol{\mu})(\bar{\boldsymbol{X}} - \boldsymbol{\mu})^{\mathsf T},
$$
所以 $(n-1)S = \sum_{l=2}^{n}\boldsymbol{Z}_l\boldsymbol{Z}_l^{\mathsf T} \sim W_p(n-1, \Sigma)$，即第 2 条。第 3 条成立，因为 $\bar{\boldsymbol{X}}$ 只依赖于 $\boldsymbol{Z}_1$，而 $S$ 只依赖于 $\boldsymbol{Z}_2, \dots, \boldsymbol{Z}_n$。$\square$

概括地说，存在独立同分布于 $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$ 的 $\boldsymbol{Z}_j$，使

$$
\bar{\boldsymbol{X}} = \boldsymbol{\mu} + \frac{1}{\sqrt{n}}\boldsymbol{Z}_1, \qquad (n-1)S = \sum_{j=2}^{n}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}. \tag{3.1}
$$
这是正态样本中 $\bar X$ 与 $S^2$ 独立（[3.2.2](/3.2.2)）的多元版本。

## 3.2. Hotelling T² 检验

### 3.2.1. 从 t 统计量到 T² 统计量

假设检验遵循固定的流程：提出原假设 $H_0$；选择**检验统计量** $T$；推导其零分布；对给定的**显著性水平** $\alpha$ 构造拒绝域，这一步在看到数据之前就可以完成；最后由数据算出统计量的观测值 $t$ 及其 **p 值**，决定是否拒绝 $H_0$。

回忆一维情形（[3.2.5](/3.2.5)）。对 $H_0\colon \mu = \mu_0$ 与 $H_1\colon \mu \ne \mu_0$，$x_1, \dots, x_n$ 独立同分布于 $\mathcal{N}(\mu, \sigma^2)$，在 $H_0$ 下 $\sqrt{n}(\bar x - \mu_0)/\sigma \sim \mathcal{N}(0, 1)$，$(n-1)s^2/\sigma^2 \sim \chi^2_{n-1}$，二者独立，估计的标准误为 $\widehat{\mathrm{se}}(\hat\mu) = s/\sqrt{n}$，故

$$
t = \frac{\bar x - \mu_0}{s/\sqrt{n}} \sim t_{n-1}, \qquad t^2 = \sqrt{n}(\bar x - \mu_0)(s^2)^{-1}\sqrt{n}(\bar x - \mu_0) \sim F_{1,n-1}.
$$
平方后的统计量具有"（正态随机变量）$\times$（尺度化 $\chi^2$ 随机变量 / 自由度）$^{-1}$ $\times$（正态随机变量）"的结构，可以直接推广。

**定义 3.2.1（Hotelling T² 统计量）** 对检验 $H_0\colon \boldsymbol{\mu} = \boldsymbol{\mu}_0$ 与 $H_1\colon \boldsymbol{\mu} \ne \boldsymbol{\mu}_0$，称统计量

$$
T^2 = \sqrt{n}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}\sqrt{n}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0) = n(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)
$$
为 **Hotelling T² 统计量**。

$T^2$ 是用 $S$ 度量的 $\bar{\boldsymbol{X}}$ 到 $\boldsymbol{\mu}_0$ 的马氏距离平方的 $n$ 倍。由式 (3.1)，在 $H_0$ 下它的结构为

$$
T^2 = (\text{多元正态随机向量})^{\mathsf T}\left(\frac{\text{Wishart 随机矩阵}}{\text{自由度}}\right)^{-1}(\text{多元正态随机向量}) = \boldsymbol{Z}_1^{\mathsf T}\left[\frac{1}{n-1}\sum_{j=2}^{n}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}\right]^{-1}\boldsymbol{Z}_1,
$$
即一个 $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$ 向量与一个独立的 $W_p(n-1, \Sigma)/(n-1)$ 矩阵的组合。$p = 1$ 时 $T^2 = t^2$。

### 3.2.2. T² 的分布

**定理 3.2.1** 设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu}_0, \Sigma)$ 的随机样本，$n > p$，则

$$
\frac{n-p}{p}\cdot\frac{T^2}{n-1} \sim F_{p,n-p}, \qquad \text{即} \qquad T^2 \sim \frac{p(n-1)}{n-p}F_{p,n-p}.
$$

**证明** 由式 (3.1)，$T^2/(n-1) = \boldsymbol{Z}_1^{\mathsf T}A^{-1}\boldsymbol{Z}_1$，其中 $A = \sum_{j=2}^{n}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}$，$\boldsymbol{Z}_1, \dots, \boldsymbol{Z}_n$ 独立同分布于 $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$。不妨设 $\Sigma = I_p$：把每个 $\boldsymbol{Z}_j$ 换成 $\Sigma^{-1/2}\boldsymbol{Z}_j$ 不改变 $\boldsymbol{Z}_1^{\mathsf T}A^{-1}\boldsymbol{Z}_1$。写

$$
\frac{T^2}{n-1} = \boldsymbol{Z}_1^{\mathsf T}A^{-1}\boldsymbol{Z}_1 = \frac{\boldsymbol{Z}_1^{\mathsf T}\boldsymbol{Z}_1}{1/(\boldsymbol{L}^{\mathsf T}A^{-1}\boldsymbol{L})}, \qquad \boldsymbol{L} = \frac{\boldsymbol{Z}_1}{\|\boldsymbol{Z}_1\|}.
$$
我们证明：(a) 分子服从 $\chi^2_p$；(b) 分母服从 $\chi^2_{n-p}$；(c) 二者独立。于是 $\frac{T^2}{n-1} = \frac{\chi^2_p}{\chi^2_{n-p}}$，由 **F 分布**的定义即 $\frac{n-p}{p}\cdot\frac{T^2}{n-1} \sim F_{p,n-p}$。(a) 是显然的。

(b)，特殊情形 $\boldsymbol{L} = \boldsymbol{e}_p = (0, \dots, 0, 1)^{\mathsf T}$。把以 $\boldsymbol{Z}_2^{\mathsf T}, \dots, \boldsymbol{Z}_n^{\mathsf T}$ 为行的 $(n-1) \times p$ 矩阵写成 $[B, \boldsymbol{y}]$，$B$ 为 $(n-1) \times (p-1)$，$\boldsymbol{y}$ 为 $(n-1) \times 1$。则

$$
A = \begin{bmatrix} B^{\mathsf T} \\ \boldsymbol{y}^{\mathsf T} \end{bmatrix}[B, \boldsymbol{y}] = \begin{bmatrix} B^{\mathsf T}B & B^{\mathsf T}\boldsymbol{y} \\ \boldsymbol{y}^{\mathsf T}B & \boldsymbol{y}^{\mathsf T}\boldsymbol{y} \end{bmatrix}.
$$
$\boldsymbol{e}_p^{\mathsf T}A^{-1}\boldsymbol{e}_p$ 是 $A^{-1}$ 的 $(p, p)$ 元，等于 $\det(B^{\mathsf T}B)/\det A$（代数余子式公式），而由分块矩阵的行列式公式（**Schur 补**），$\det A = \det(B^{\mathsf T}B)\cdot[\boldsymbol{y}^{\mathsf T}\boldsymbol{y} - \boldsymbol{y}^{\mathsf T}B(B^{\mathsf T}B)^{-1}B^{\mathsf T}\boldsymbol{y}]$。故

$$
\frac{1}{\boldsymbol{e}_p^{\mathsf T}A^{-1}\boldsymbol{e}_p} = \boldsymbol{y}^{\mathsf T}[I_{n-1} - B(B^{\mathsf T}B)^{-1}B^{\mathsf T}]\boldsymbol{y} = \boldsymbol{y}^{\mathsf T}C\boldsymbol{y}.
$$
$C$ 对称且幂等，是到 $B$ 的列空间的正交补上的**正交投影矩阵**，秩为 $(n-1) - (p-1) = n - p$。所以存在正交矩阵 $\Gamma$ 使 $\Gamma C\Gamma^{\mathsf T} = \operatorname{diag}(I_{n-p}, O)$。向量 $\boldsymbol{y}$（$\boldsymbol{Z}_2, \dots, \boldsymbol{Z}_n$ 的最后一个坐标）服从 $\mathcal{N}_{n-1}(\boldsymbol{0}, I)$，且与 $B$ 独立；给定 $B$ 时，$\tilde{\boldsymbol{y}} = \Gamma\boldsymbol{y} \sim \mathcal{N}_{n-1}(\boldsymbol{0}, I)$，$\boldsymbol{y}^{\mathsf T}C\boldsymbol{y} = \tilde{\boldsymbol{y}}^{\mathsf T}\operatorname{diag}(I_{n-p}, O)\tilde{\boldsymbol{y}} = \sum_{i=1}^{n-p}\tilde y_i^2 \sim \chi^2_{n-p}$。这一条件分布与 $B$ 无关，因此 $1/(\boldsymbol{e}_p^{\mathsf T}A^{-1}\boldsymbol{e}_p) \sim \chi^2_{n-p}$。

(b)，一般情形。对固定的单位向量 $\boldsymbol{l}$，取最后一行为 $\boldsymbol{l}^{\mathsf T}$ 的正交矩阵 $\Gamma$，使 $\Gamma^{\mathsf T}\boldsymbol{e}_p = \boldsymbol{l}$。则 $\boldsymbol{l}^{\mathsf T}A^{-1}\boldsymbol{l} = \boldsymbol{e}_p^{\mathsf T}(\Gamma A\Gamma^{\mathsf T})^{-1}\boldsymbol{e}_p$，而 $\Gamma A\Gamma^{\mathsf T} = \sum_{j=2}^{n}\tilde{\boldsymbol{Z}}_j\tilde{\boldsymbol{Z}}_j^{\mathsf T}$，其中 $\tilde{\boldsymbol{Z}}_j = \Gamma\boldsymbol{Z}_j$ 仍独立同分布于 $\mathcal{N}_p(\boldsymbol{0}, I_p)$。由特殊情形，对每个固定的单位向量 $\boldsymbol{l}$，$1/(\boldsymbol{l}^{\mathsf T}A^{-1}\boldsymbol{l}) \sim \chi^2_{n-p}$。随机的 $\boldsymbol{L} = \boldsymbol{Z}_1/\|\boldsymbol{Z}_1\|$ 与 $A$ 独立，所以给定 $\boldsymbol{Z}_1$ 时 $1/(\boldsymbol{L}^{\mathsf T}A^{-1}\boldsymbol{L}) \sim \chi^2_{n-p}$。

(c) 这一给定 $\boldsymbol{Z}_1$ 的条件分布与 $\boldsymbol{Z}_1$ 无关。因此分母与 $\boldsymbol{Z}_1$ 独立，特别是与分子 $\boldsymbol{Z}_1^{\mathsf T}\boldsymbol{Z}_1$ 独立，其无条件分布为 $\chi^2_{n-p}$。$\square$

这个证明有三点值得注意。它先把所有随机量看作固定的来研究代数结构，然后才研究其随机性。它做了两次不失一般性的化简：$\Sigma = I_p$（每个 $\boldsymbol{Z}_j$ 乘以 $\Sigma^{-1/2}$）与 $\boldsymbol{L} = \boldsymbol{e}_p$（每个 $\boldsymbol{Z}_j$ 乘以一个正交矩阵），两者都不改变分母。它还拆解了分母的随机性来源（$\boldsymbol{L}$、$B$ 与 $\boldsymbol{y}$）：固定 $\boldsymbol{L}$ 与 $B$ 时，条件分布总是 $\chi^2_{n-p}$，与它们的取值无关，由此同时得到无条件分布与独立性。自由度 $n - p = (n-1) - (p-1)$ 是 Wishart 矩阵的自由度减去 $B$ 用掉的 $p - 1$ 维。

### 3.2.3. 检验

由定理 3.2.1，$H_0\colon \boldsymbol{\mu} = \boldsymbol{\mu}_0$ 对 $H_1\colon \boldsymbol{\mu} \ne \boldsymbol{\mu}_0$ 的水平 $\alpha$ 检验在

$$
T^2 = n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0) > \frac{p(n-1)}{n-p}F_{p,n-p,\alpha} \tag{3.2}
$$
时拒绝 $H_0$，其中 $F_{p,n-p,\alpha}$ 是 $F_{p,n-p}$ 的上 $\alpha$ 分位数；右边是临界值，下文记作 $T^2_\alpha$。这一统计量及其分布以 Harold Hotelling（1895–1973）命名，他在 1931 年把它作为 Student $t$ 的推广提出。

**例 3.2.1** 在例 3.1.1 中（$n = 55$，$p = 6$，$\alpha = 0.05$），临界值为 $\frac{6 \cdot 54}{49}F_{6,49,0.05} = 15.145$。

- 对 $H_{01}\colon \boldsymbol{\mu} = (5.0, 5.0, 4.7, 3.6, 4.6, 5.0)^{\mathsf T}$，$T^2 = 9.053 < 15.145$：不拒绝 $H_{01}$。
- 对 $H_{02}\colon \boldsymbol{\mu} = (5.0, 5.0, 4.8, 3.6, 4.6, 5.0)^{\mathsf T}$，$T^2 = 20.840 > 15.145$：拒绝 $H_{02}$。

两个假设只在"认可"分量上相差 $0.1$（其样本均值为 $4.717$）。前者与数据相容，后者不相容，尽管两者的每个分量与样本均值的差都在约 $0.12$ 以内；偏差是否算大取决于各分量的方差与相关性，$T^2$ 通过 $S^{-1}$ 把它们考虑在内。

**性质 3.2.1（不变性）** $T^2$ 在测量单位的改变下不变，更一般地在非奇异仿射变换下不变：若 $\boldsymbol{y}_j = C\boldsymbol{x}_j + \boldsymbol{d}$，$C$ 为 $p \times p$ 可逆矩阵，假设相应地变为 $\boldsymbol{\mu}_{Y,0} = C\boldsymbol{\mu}_0 + \boldsymbol{d}$，则由 $\boldsymbol{y}_j$ 算出的 $T^2$ 等于由 $\boldsymbol{x}_j$ 算出的 $T^2$。

**证明** 由定理 2.2.2，$\bar{\boldsymbol{y}} = C\bar{\boldsymbol{x}} + \boldsymbol{d}$，$S_Y = CSC^{\mathsf T}$。于是

$$
\begin{aligned}
T^2_Y &= n(\bar{\boldsymbol{y}} - \boldsymbol{\mu}_{Y,0})^{\mathsf T}S_Y^{-1}(\bar{\boldsymbol{y}} - \boldsymbol{\mu}_{Y,0}) = n[C(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)]^{\mathsf T}(CSC^{\mathsf T})^{-1}C(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0) \\
&= n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}C^{\mathsf T}(C^{\mathsf T})^{-1}S^{-1}C^{-1}C(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0) = n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0). \quad \square
\end{aligned}
$$

## 3.3. 置信域

一维中，$z_1, \dots, z_n$ 独立同分布于 $\mathcal{N}(\psi, \sigma_\psi^2)$，枢轴量 $\left(\frac{\bar z - \psi}{s/\sqrt{n}}\right)^2 \sim F_{1,n-1}$ 给出置信区间

$$
I(\boldsymbol{z}) = \bar z \pm t_{n-1,\alpha/2}\frac{s}{\sqrt{n}} = \{\psi\colon n(\bar z - \psi)(s^2)^{-1}(\bar z - \psi) \le c^2\}, \qquad c^2 = t_{n-1,\alpha/2}^2 = F_{1,n-1,\alpha},
$$
其覆盖概率为 $\mathbb{P}_\psi(I(\boldsymbol{z}) \ni \psi) = \mathbb{P}(\lvert t_{n-1}\rvert \le t_{n-1,\alpha/2}) = 1 - \alpha$。所用统计量与检验相同；区别在于检验固定 $\mu_0$、考察数据，而区间固定数据、收集所有不会被拒绝的参数值。同样的反转对均值向量也成立。

**定理 3.3.1（均值向量的置信域）** 设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的随机样本，$n > p$。集合

$$
R(X) = \{\boldsymbol{\mu}\colon n(\bar{\boldsymbol{X}} - \boldsymbol{\mu})^{\mathsf T}S^{-1}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}) \le c^2\}, \qquad c^2 = T^2_\alpha = \frac{p(n-1)}{n-p}F_{p,n-p,\alpha},
$$
是 $\boldsymbol{\mu}$ 的 $100(1 - \alpha)\%$ **置信域**：$\mathbb{P}_{\boldsymbol{\mu}}(R(X) \ni \boldsymbol{\mu}) = 1 - \alpha$。

覆盖概率就是定理 3.2.1 中把 $\boldsymbol{\mu}_0$ 换成真实的 $\boldsymbol{\mu}$。这个区域恰由检验 (3.2) 不拒绝的那些 $\boldsymbol{\mu}_0$ 组成。要判断给定的 $\boldsymbol{\mu}_0$ 是否在其中，只需对 $\boldsymbol{\mu}_0$ 计算 $T^2$ 并与 $c^2$ 比较。

几何上，$R(X)$ 是以 $\bar{\boldsymbol{x}}$ 为中心的实心椭球。若 $S$ 的特征值为 $\lambda_1 \ge \cdots \ge \lambda_p > 0$、特征向量为 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$，则由定理 2.3.1（把 $\Sigma$ 换成 $S/n$），其轴为

$$
\pm\sqrt{\lambda_i}\,\frac{c}{\sqrt{n}}\,\boldsymbol{e}_i = \pm\sqrt{\lambda_i}\sqrt{\frac{p(n-1)}{n(n-p)}F_{p,n-p,\alpha}}\,\boldsymbol{e}_i, \qquad i = 1, \dots, p.
$$
椭球在数据变异最大的方向上最长，并以 $1/\sqrt{n}$ 的速度收缩。$p = 2$ 时可以画出来：对例 3.1.1 中的"成就"与"认可"两项评分（$n = 55$），其样本相关性很强，$95\%$ 置信椭圆是一个围绕 $(5.12, 4.72)$、沿对角线倾斜的细长椭圆，与数据的散布相比很小。$p \ge 4$ 时无法直观展示椭球，于是改为报告区间。

## 3.4. 联合置信区间

### 3.4.1. 单个线性组合的区间

$\frac{1}{2}\mu_1 + \frac{1}{2}\mu_2 = (\frac{1}{2}, \frac{1}{2}, 0, 0, 0, 0)\boldsymbol{\mu}$ 这样的综合值是线性组合 $\psi = \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$。对固定的 $\boldsymbol{a}$，$z_j = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}_j$ 独立同分布于 $\mathcal{N}(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a})$（定理 2.4.1），样本均值为 $\bar z = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}}$，样本方差为 $s_z^2 = \boldsymbol{a}^{\mathsf T}S\boldsymbol{a}$（定理 2.2.2）。对它们使用一维 $t$ 区间：$\hat\psi = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}}$，$\widehat{\mathrm{se}}(\hat\psi) = s_z/\sqrt{n}$，$\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ 的 $100(1 - \beta)\%$ 置信区间为

$$
I_{\boldsymbol{a}} = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}} \pm t_{n-1,\beta/2}\sqrt{\frac{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}}{n}}. \tag{3.3}
$$
取 $\boldsymbol{a} = \boldsymbol{e}_k$ 就是分量均值 $\mu_k$ 的通常区间。对两变量的子数据集（成就、认可），$n = 55$、$\beta = 0.05$ 时乘数为 $t_{54,0.025} = 2.005$。

### 3.4.2. 联合覆盖与 Bonferroni 区间

每个区间 (3.3) 以概率 $1 - \beta$ 正确：$\mathbb{P}(I_{\boldsymbol{a}_k} \ni \boldsymbol{a}_k^{\mathsf T}\boldsymbol{\mu}) = 1 - \beta$。同时报告 $m$ 个这样的区间时，它们全部正确的概率更小，而如果要同时依据所有区间下结论，起作用的正是这个概率。

**定义 3.4.1（联合置信区间）** 若关于 $\psi_k = \boldsymbol{a}_k^{\mathsf T}\boldsymbol{\mu}$（$k = 1, \dots, m$）的区间 $I_1, \dots, I_m$ 满足

$$
\mathbb{P}(\text{对一切 } k = 1, \dots, m, \ I_k \ni \psi_k) \ge 1 - \alpha,
$$
则称它们为置信水平 $1 - \alpha$ 的**联合置信区间**。与之相对，单个置信区间只对每个 $k$ 分别满足 $\mathbb{P}(I_k \ni \psi_k) \ge 1 - \alpha$。

联合覆盖是一种需求，而不是一种方法；本课程介绍两种常用的实现方式。设 $C_k$ 为 $I_{\boldsymbol{a}_k}$ 覆盖 $\psi_k$ 的事件，每个区间的水平为 $1 - \beta$。由 Bonferroni 不等式，

$$
\mathbb{P}(\text{某个 } C_k \text{ 不成立}) \le \sum_{k=1}^{m}\mathbb{P}(C_k \text{ 不成立}) = m\beta, \qquad \text{故} \qquad \mathbb{P}(\text{所有 } C_k \text{ 成立}) \ge 1 - m\beta.
$$
取 $\beta = \alpha/m$（[3.2.4](/3.2.4) 的 **Bonferroni 校正**），得到 Bonferroni 区间

$$
\boldsymbol{a}_k^{\mathsf T}\bar{\boldsymbol{X}} \pm t_{n-1,\alpha/(2m)}\sqrt{\frac{\boldsymbol{a}_k^{\mathsf T}S\boldsymbol{a}_k}{n}}, \qquad k = 1, \dots, m, \tag{3.4}
$$
无论区间之间如何相依，其联合水平都至少为 $1 - \alpha$。它们是保守的。Bonferroni 方法让每个线性组合平等地分担错误率：$m = 5$、$\alpha = 0.05$ 时，每个区间都按 $99\%$ 的水平计算，而不是有的取 $98.5\%$、有的取 $99.5\%$（不均等的分配也是有效的，但必须事先确定）。

### 3.4.3. T² 区间

能否用同一个乘数 $c$，使区间 $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}} \pm c\sqrt{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}/n}$ 对一切 $\boldsymbol{a} \ne \boldsymbol{0}$ 同时覆盖 $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$？对 $\boldsymbol{a}$ 的区间覆盖当且仅当 $t_{\boldsymbol{a}}^2 \le c^2$，其中

$$
t_{\boldsymbol{a}}^2 = \frac{n[\boldsymbol{a}^{\mathsf T}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})]^2}{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}},
$$
所以它们全部覆盖当且仅当 $\max_{\boldsymbol{a}}t_{\boldsymbol{a}}^2 \le c^2$。由最大化引理（引理 1.7.2，取 $B = S$、$\boldsymbol{d} = \bar{\boldsymbol{x}} - \boldsymbol{\mu}$），

$$
\max_{\boldsymbol{a} \ne \boldsymbol{0}}t_{\boldsymbol{a}}^2 = n\max_{\boldsymbol{a} \ne \boldsymbol{0}}\frac{[\boldsymbol{a}^{\mathsf T}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})]^2}{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}} = n(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}) = T^2,
$$
在 $\boldsymbol{a} \propto S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})$ 处取到。因此所有区间都覆盖的事件，恰好就是定理 3.3.1 的置信域覆盖 $\boldsymbol{\mu}$ 的事件 $T^2 \le c^2$。

**定理 3.4.1（T² 联合置信区间）** 设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的随机样本，$n > p$，则

$$
\mathbb{P}\left(\text{对一切 } \boldsymbol{a}, \ \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}} - c\sqrt{\frac{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}}{n}} \le \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu} \le \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{X}} + c\sqrt{\frac{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}}{n}}\right) = 1 - \alpha, \qquad c^2 = \frac{p(n-1)}{n-p}F_{p,n-p,\alpha}. \tag{3.5}
$$

取 $\boldsymbol{a} = \boldsymbol{e}_1, \dots, \boldsymbol{e}_p$，分量均值的 $T^2$ 区间为 $\bar x_k \pm c\sqrt{s_{kk}/n}$。几何上，$\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ 的 $T^2$ 区间是置信椭球在方向 $\boldsymbol{a}$ 上的投影：同样由最大化引理，$\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ 在 $R(X)$ 上的最大值与最小值为 $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}} \pm c\sqrt{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}/n}$。在平面上，$\mu_1$ 与 $\mu_2$ 的 $T^2$ 区间就是置信椭圆在两个坐标轴上的影子，这并非巧合。

**注 3.4.1** 无论在推导中还是在结论中，向量 $\boldsymbol{a}$ 都不必是单位向量。$\boldsymbol{a}$ 伸缩时比值 $t_{\boldsymbol{a}}^2$ 不变，而由置信域一次求出的乘数 $c$ 为所有 $\boldsymbol{a}$ 的区间所共用；对具体的 $\boldsymbol{a}$ 不必重复求最大值的过程。另一方面，给定 $\boldsymbol{a}$ 的区间保留 $\boldsymbol{a}$ 的尺度：$100\,\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ 的区间是 $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ 的区间的 $100$ 倍，这理所当然。

**注 3.4.2** 三种区间（单个 $t$ 区间、Bonferroni 区间、$T^2$ 区间）都是关于一维量 $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ 的一维区间；只有置信域是 $p$ 维集合。把 $\mu_1$ 与 $\mu_2$ 的区间画成矩形，只是为了比较它们彼此之间以及与置信椭圆的大小关系。三种区间形式相同，都是 $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}} \pm c\sqrt{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}/n}$，只差在乘数 $c$。

![模拟的类似"成就"与"认可"评分的数据（n = 55）：均值向量的 95% 置信椭圆，以及以矩形表示的两个分量均值的单个 t 区间、Bonferroni 区间（m = 2）与 T^2 区间。T^2 矩形就是椭圆在坐标轴上的影子。](./plots/t2-confidence-ellipse.py)

### 3.4.4. 区间的比较

| 区间 | 乘数 $c$ | 覆盖 |
|---|---|---|
| 单个 $t$ 区间 | $t_{n-1,\alpha/2}$ | 每个区间各自为 $1 - \alpha$ |
| Bonferroni 区间 | $t_{n-1,\alpha/(2m)}$ | 对 $m$ 个事先指定的组合至少为 $1 - \alpha$ |
| $T^2$ 区间 | $\sqrt{\frac{p(n-1)}{n-p}F_{p,n-p,\alpha}}$ | 对一切组合恰为 $1 - \alpha$，包括看到数据后才选定的组合 |

对两变量的例子（$n = 55$，$p = 2$，$\alpha = 0.05$），乘数为 $2.005$（单个）、$2.306$（Bonferroni，$m = 2$）、$2.670$（Bonferroni，$m = 5$）与 $2.542$（$T^2$）。只有 Bonferroni 乘数依赖于线性组合的个数 $m$：对 $p$ 个分量均值（$m = p$），Bonferroni 区间比 $T^2$ 区间短，但随着 $m$ 增大它们会变长，而 $T^2$ 区间对任意多个组合都有效，即使是由数据提示的组合。两种乘数都随维数 $p$ 增长；$T^2$ 乘数增长得快得多，因为它要保护无穷多个组合。

![n = 200 时三种 95% 区间的乘数 c 随维数 p 的变化：单个 t 区间（常数）、m = p 个组合的 Bonferroni 区间与 T^2 区间。](./plots/critical-values.py)

实践中：只对单个事先关心的量用单个区间；对少数事先确定的组合（典型的是 $p$ 个分量均值）用 Bonferroni 区间；考察许多组合或在看到数据后才选定组合时用 $T^2$ 区间。

## 3.5. Hotelling T² 与似然比检验

$T^2$ 检验是类比 $t$ 检验构造出来的。它也是 $H_0\colon \boldsymbol{\mu} = \boldsymbol{\mu}_0$ 的**似然比检验**（[3.2.5](/3.2.5)），这说明它是自然的选择。

**定理 3.5.1** 设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的随机样本，$n > p$，记

$$
\hat\Sigma = \frac{1}{n}\sum_{j=1}^{n}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}, \qquad \hat\Sigma_0 = \frac{1}{n}\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu}_0)(\boldsymbol{x}_j - \boldsymbol{\mu}_0)^{\mathsf T}.
$$
$H_0\colon \boldsymbol{\mu} = \boldsymbol{\mu}_0$ 对 $H_1\colon \boldsymbol{\mu} \ne \boldsymbol{\mu}_0$ 的似然比为

$$
\Lambda = \frac{\max_{\Sigma}L(\boldsymbol{\mu}_0, \Sigma)}{\max_{\boldsymbol{\mu}, \Sigma}L(\boldsymbol{\mu}, \Sigma)} = \left(\frac{\det\hat\Sigma}{\det\hat\Sigma_0}\right)^{n/2} = \left(1 + \frac{T^2}{n-1}\right)^{-n/2}.
$$
因此在 $\Lambda$ 小时拒绝的似然比检验，等价于在 $T^2$ 大时拒绝的 $T^2$ 检验。

**证明** 分母为 $(2\pi)^{-np/2}\mathrm{e}^{-np/2}(\det\hat\Sigma)^{-n/2}$（定理 2.5.1 及 [3.4.2](/3.4.2) 中似然最大值的计算）。固定 $\boldsymbol{\mu} = \boldsymbol{\mu}_0$，与定理 2.5.1 的证明同样的论证表明 $L(\boldsymbol{\mu}_0, \Sigma)$ 在 $\Sigma = \hat\Sigma_0$ 处取最大值 $(2\pi)^{-np/2}\mathrm{e}^{-np/2}(\det\hat\Sigma_0)^{-n/2}$。这给出第一个表达式。

对第二个表达式，考虑 $(p + 1) \times (p + 1)$ 分块矩阵

$$
A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} = \begin{bmatrix} n\hat\Sigma & \sqrt{n}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0) \\ \sqrt{n}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T} & -1 \end{bmatrix},
$$
用 $\det A = \det A_{22}\det(A_{11} - A_{12}A_{22}^{-1}A_{21}) = \det A_{11}\det(A_{22} - A_{21}A_{11}^{-1}A_{12})$ 两种方式计算其行列式。第一种给出

$$
\det A = (-1)\det\left(n\hat\Sigma + n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}\right) = (-1)\det(n\hat\Sigma_0),
$$
因为 $\sum_j(\boldsymbol{x}_j - \boldsymbol{\mu}_0)(\boldsymbol{x}_j - \boldsymbol{\mu}_0)^{\mathsf T} = \sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T} + n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}$。第二种利用 $n\hat\Sigma = (n-1)S$，给出

$$
\det A = \det(n\hat\Sigma)\left(-1 - n(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)^{\mathsf T}[(n-1)S]^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}_0)\right) = (-1)\det(n\hat\Sigma)\left(1 + \frac{T^2}{n-1}\right).
$$
比较两式得 $\det\hat\Sigma_0 = \det\hat\Sigma\,(1 + T^2/(n-1))$。$\square$

一维中这一恒等式就是熟悉的分解 $\sum_j(x_j - \mu_0)^2 = \sum_j(x_j - \bar x)^2 + n(\bar x - \mu_0)^2$，它给出 $\hat\sigma_0^2/\hat\sigma^2 = 1 + t^2/(n-1)$。定理 3.5.1 还给出一个不必求 $S^{-1}$ 的 $T^2$ 计算公式：

$$
T^2 = \frac{(n-1)\det\hat\Sigma_0}{\det\hat\Sigma} - (n-1) = (n-1)\frac{\det\left(\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu}_0)(\boldsymbol{x}_j - \boldsymbol{\mu}_0)^{\mathsf T}\right)}{\det\left(\sum_{j=1}^{n}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}\right)} - (n-1).
$$
似然比方法可以推广到看不出 $T^2$ 类比的假设；$n$ 较大时，在 $H_0$ 下 $-2\log\Lambda = n\log(1 + T^2/(n-1))$ 近似服从 $\chi^2_p$（[3.4.4](/3.4.4)）。

## 小结

- 正态样本：$\bar{\boldsymbol{X}} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma/n)$，$(n-1)S \sim W_p(n-1, \Sigma)$，二者独立；Wishart 分布 $W_p(m, \Sigma)$ 是 $\sum_{j=1}^{m}\boldsymbol{Z}_j\boldsymbol{Z}_j^{\mathsf T}$（$\boldsymbol{Z}_j$ 独立同分布于 $\mathcal{N}_p(\boldsymbol{0}, \Sigma)$）的分布，是 $\sigma^2\chi^2_m$ 的类比。
- Hotelling $T^2 = n(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)^{\mathsf T}S^{-1}(\bar{\boldsymbol{X}} - \boldsymbol{\mu}_0)$ 推广了 $t^2$；在 $H_0$ 下 $\frac{n-p}{p(n-1)}T^2 \sim F_{p,n-p}$；当 $T^2 > \frac{p(n-1)}{n-p}F_{p,n-p,\alpha}$ 时拒绝。$T^2$ 在非奇异仿射变换下不变，并与似然比检验等价，$\Lambda = (1 + T^2/(n-1))^{-n/2}$。
- 置信域：椭球 $\{\boldsymbol{\mu}\colon n(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}S^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}) \le c^2\}$，轴为 $\pm\sqrt{\lambda_i}\,c\,\boldsymbol{e}_i/\sqrt{n}$。
- $\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$ 的区间形如 $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}} \pm c\sqrt{\boldsymbol{a}^{\mathsf T}S\boldsymbol{a}/n}$：$c = t_{n-1,\alpha/2}$（单个）、$t_{n-1,\alpha/(2m)}$（Bonferroni，$m$ 个组合）、$\sqrt{p(n-1)F_{p,n-p,\alpha}/(n-p)}$（$T^2$，一切组合，即置信椭球的投影）。联合覆盖是本章的新想法。
