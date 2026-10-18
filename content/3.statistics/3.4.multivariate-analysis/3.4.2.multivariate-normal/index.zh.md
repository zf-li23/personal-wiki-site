---
title: 描述统计与多元正态分布
description: 样本均值向量、样本协方差矩阵与样本相关矩阵的矩阵形式、几何意义与广义样本方差；无偏性与线性组合；多元正态密度、等密度椭球及由独立正态变量的构造；线性变换、边缘分布、独立性、条件分布与卡方性质；正态假定下的极大似然估计与充分性。
source_hash: 2a98e3344d81
---

本章在多元情形下建立样本与总体之间的联系。首先是数据矩阵的描述统计量（样本均值向量、样本协方差矩阵与样本相关矩阵），用矩阵形式写出并给出几何解释，同时引入刻画变异程度的单个数值——广义样本方差。不需要任何分布假定，这些统计量就是相应总体量的无偏估计。后半部分讨论多元正态分布，它是多元分析的基本构件与基准。其定义与基本性质已在概率论（[3.1.15](/3.1.15)）中推导；这里按本课程使用的形式重述，补充其密度的几何意义，并推导正态样本的极大似然估计与充分统计量。所用工具见 [3.4.1](/3.4.1)；这些估计量的抽样分布及其上的推断见 [3.4.3](/3.4.3)。

## 2.1. 描述统计量

### 2.1.1. 样本均值、方差、协方差与相关系数

设 $X = (x_{jk})$ 为 $n \times p$ 数据矩阵（定义 1.2.1），各行 $\boldsymbol{x}_j^{\mathsf T}$ 对应对象 $j = 1, \dots, n$，各列对应变量 $k = 1, \dots, p$。对每个变量，有**样本均值** $\bar x_k$（中心、位置）与**样本方差** $s_{kk} = s_k^2$（散布、离散程度）；对每对变量，**样本协方差** $s_{ik}$ 度量它们的线性关联：

$$
\bar x_k = \frac{1}{n}\sum_{j=1}^{n}x_{jk}, \qquad s_{ik} = \frac{1}{n-1}\sum_{j=1}^{n}(x_{ji} - \bar x_i)(x_{jk} - \bar x_k), \qquad i, k = 1, \dots, p.
$$
协方差依赖于变量的单位，除以标准差即可消去单位。

**定义 2.1.1（样本均值向量、样本协方差矩阵、样本相关矩阵）** 数据矩阵 $X$ 的**样本均值向量**、**样本协方差矩阵**与**样本相关矩阵**为

$$
\bar{\boldsymbol{x}} = \begin{bmatrix} \bar x_1 \\ \vdots \\ \bar x_p \end{bmatrix}, \qquad S = \begin{bmatrix} s_{11} & \cdots & s_{1p} \\ \vdots & \ddots & \vdots \\ s_{p1} & \cdots & s_{pp} \end{bmatrix} = \frac{1}{n-1}\sum_{j=1}^{n}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}, \qquad R = \begin{bmatrix} 1 & r_{12} & \cdots & r_{1p} \\ r_{21} & 1 & \cdots & r_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ r_{p1} & r_{p2} & \cdots & 1 \end{bmatrix},
$$
其中样本相关系数为

$$
r_{ik} = \frac{s_{ik}}{\sqrt{s_{ii}}\sqrt{s_{kk}}} = \frac{\sum_{j=1}^{n}(x_{ji} - \bar x_i)(x_{jk} - \bar x_k)}{\sqrt{\sum_{j=1}^{n}(x_{ji} - \bar x_i)^2}\sqrt{\sum_{j=1}^{n}(x_{jk} - \bar x_k)^2}}.
$$
以 $n$ 代替 $n - 1$ 作除数的矩阵记为 $S_n = \frac{n-1}{n}S$。

两种除数都常用：$S$ 是无偏的（定理 2.2.1），$S_n$ 是正态假定下的极大似然估计（定理 2.5.1）。矩阵 $S$、$S_n$、$R$ 都对称且非负定，因为 $\boldsymbol{a}^{\mathsf T}S\boldsymbol{a} = \frac{1}{n-1}\sum_j[\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})]^2 \ge 0$。

**注 2.1.1** 样本相关系数 $r_{ik}$ 是标准化变量的样本协方差，因此与单位和尺度无关。它满足 $\lvert r_{ik}\rvert \le 1$，只度量线性关联：$r = 0$ 表示没有线性关联，而不是没有关联。在线性变换 $y_{ji} = ax_{ji} + b$、$y_{jk} = cx_{jk} + d$ 下，相关系数变为 $\operatorname{sgn}(ac)\,r_{ik}$；$a$ 与 $c$ 同号时不变，异号时变号。

**例 2.1.1** 对数据矩阵 $X = \begin{bmatrix} 4 & 1 \\ 5 & 2 \\ 3 & 5 \end{bmatrix}$（$n = 3$，$p = 2$；三家书店的销售额与图书种数），

$$
\bar x_1 = \frac{4 + 5 + 3}{3} = 4, \qquad \bar x_2 = \frac{1 + 2 + 5}{3} = \frac{8}{3},
$$

$$
s_{11} = \frac{0^2 + 1^2 + (-1)^2}{2} = 1, \qquad s_{22} = \frac{(-\frac{5}{3})^2 + (-\frac{2}{3})^2 + (\frac{7}{3})^2}{2} = \frac{13}{3}, \qquad s_{12} = \frac{0 \cdot (-\frac{5}{3}) + 1 \cdot (-\frac{2}{3}) + (-1)\cdot\frac{7}{3}}{2} = -\frac{3}{2},
$$
故

$$
\bar{\boldsymbol{x}} = \begin{bmatrix} 4 \\ \frac{8}{3} \end{bmatrix}, \qquad S = \begin{bmatrix} 1 & -\frac{3}{2} \\ -\frac{3}{2} & \frac{13}{3} \end{bmatrix}, \qquad r_{12} = \frac{-3/2}{\sqrt{1}\sqrt{13/3}} \approx -0.72, \qquad R = \begin{bmatrix} 1 & -0.72 \\ -0.72 & 1 \end{bmatrix}.
$$
在这三个点的散点图中，$\bar{\boldsymbol{x}}$ 是重心，$s_{11}$ 与 $s_{22}$ 描述水平与竖直方向的散布，负相关说明点云从左上延伸到右下。

### 2.1.2. 矩阵形式

记 $\boldsymbol{1}_n$ 为 $n \times 1$ 全 1 向量，$\boldsymbol{y}_k = (x_{1k}, \dots, x_{nk})^{\mathsf T}$ 为 $X$ 的第 $k$ 列，则 $\bar x_k = \frac{1}{n}\boldsymbol{y}_k^{\mathsf T}\boldsymbol{1}_n$，叠起来得

$$
\bar{\boldsymbol{x}} = \frac{1}{n}\begin{bmatrix} x_{11} & \cdots & x_{n1} \\ \vdots & \ddots & \vdots \\ x_{1p} & \cdots & x_{np} \end{bmatrix}\begin{bmatrix} 1 \\ \vdots \\ 1 \end{bmatrix} = \frac{1}{n}X^{\mathsf T}\boldsymbol{1}_n.
$$
每一行都是 $\bar{\boldsymbol{x}}^{\mathsf T}$ 的 $n \times p$ 矩阵是 $\boldsymbol{1}_n\bar{\boldsymbol{x}}^{\mathsf T} = \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}X$，所以离差矩阵为

$$
B = X - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}X = \left(I_n - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}\right)X.
$$

**定义 2.1.2（中心化矩阵）** 称 $n \times n$ 矩阵 $H = I_n - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$ 为**中心化矩阵**。

$H$ 对称且幂等，$H^2 = I_n - \frac{2}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T} + \frac{1}{n^2}\boldsymbol{1}_n(\boldsymbol{1}_n^{\mathsf T}\boldsymbol{1}_n)\boldsymbol{1}_n^{\mathsf T} = H$；它是到 $\boldsymbol{1}_n$ 的正交补上的**正交投影矩阵**。由于 $(n-1)s_{ik}$ 是 $B$ 的第 $i$ 列与第 $k$ 列的内积，

$$
(n-1)S = nS_n = B^{\mathsf T}B = X^{\mathsf T}H^{\mathsf T}HX = X^{\mathsf T}HX = X^{\mathsf T}\left(I_n - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}\right)X.
$$
记 $D^{1/2} = \operatorname{diag}(\sqrt{s_{11}}, \dots, \sqrt{s_{pp}})$，则相关矩阵为

$$
R = D^{-1/2}SD^{-1/2}, \qquad S = D^{1/2}RD^{1/2}.
$$
左乘对角矩阵缩放各行，右乘缩放各列，故 $(D^{-1/2}SD^{-1/2})_{ik} = s_{ik}/(\sqrt{s_{ii}}\sqrt{s_{kk}})$。

对例 2.1.1，$\bar{\boldsymbol{x}} = \frac{1}{3}\begin{bmatrix} 4 & 5 & 3 \\ 1 & 2 & 5 \end{bmatrix}\boldsymbol{1}_3 = (4, \frac{8}{3})^{\mathsf T}$，$X^{\mathsf T}HX = \begin{bmatrix} 2 & -3 \\ -3 & \frac{26}{3} \end{bmatrix} = 2S$。

### 2.1.3. 样本的几何

除了看作 $\mathbb{R}^p$ 中的 $n$ 个点，数据矩阵还可以看作 $\mathbb{R}^n$ 中的 $p$ 个向量 $\boldsymbol{y}_1, \dots, \boldsymbol{y}_p$（[3.4.1](/3.4.1) 的 1.2.3 节）。$n$ 较大时无法画出 $n$ 维空间，但长度、夹角与体积仍有意义，描述统计量恰好就是这些量。

- 均值 = 在 $\boldsymbol{1}_n$ 上的投影。沿 $\boldsymbol{1}_n$ 的单位向量为 $\boldsymbol{1}_n/\sqrt{n}$，$\boldsymbol{y}_k$ 在其上的投影为 $\left(\boldsymbol{y}_k^{\mathsf T}\frac{\boldsymbol{1}_n}{\sqrt{n}}\right)\frac{\boldsymbol{1}_n}{\sqrt{n}} = \bar x_k\boldsymbol{1}_n$。
- 方差 = 离差向量长度的平方。离差向量 $\boldsymbol{d}_k = \boldsymbol{y}_k - \bar x_k\boldsymbol{1}_n$ 与 $\boldsymbol{1}_n$ 垂直，$L_{\boldsymbol{d}_k}^2 = \boldsymbol{d}_k^{\mathsf T}\boldsymbol{d}_k = \sum_j(x_{jk} - \bar x_k)^2 = (n-1)s_{kk}$。$\boldsymbol{y}_k$ 越靠近 $\boldsymbol{1}_n$ 所在直线，方差越小。
- 相关系数 = 夹角的余弦。$\boldsymbol{d}_i^{\mathsf T}\boldsymbol{d}_k = (n-1)s_{ik} = L_{\boldsymbol{d}_i}L_{\boldsymbol{d}_k}\cos\theta_{ik}$，故 $r_{ik} = \cos\theta_{ik}$。两个离差向量的夹角越小，相关系数越大。

**例 2.1.2** 对 $X = \begin{bmatrix} 4 & 1 \\ -1 & 3 \\ 3 & 5 \end{bmatrix}$，$\bar{\boldsymbol{x}} = (2, 3)^{\mathsf T}$，两列在 $\boldsymbol{1}_3$ 上的投影为 $2\boldsymbol{1}_3$ 与 $3\boldsymbol{1}_3$，离差向量为 $\boldsymbol{d}_1 = (2, -3, 1)^{\mathsf T}$、$\boldsymbol{d}_2 = (-2, 0, 2)^{\mathsf T}$。于是 $s_{11} = 14/2 = 7$，$s_{22} = 8/2 = 4$，$s_{12} = -2/2 = -1$，$r_{12} = \cos\theta_{12} = -2/\sqrt{14 \cdot 8} \approx -0.19$：两个离差向量几乎垂直。

### 2.1.4. 广义样本方差

如何用一个数概括 $p \times p$ 矩阵 $S$ 的信息？两种常用选择是总样本方差 $\operatorname{tr}S = s_{11} + \cdots + s_{pp}$ 与下面的量。

**定义 2.1.3（广义样本方差）** 称样本协方差矩阵的行列式 $\det S$ 为**广义样本方差**。

样本的两种图像都能说明它度量的是什么。

在 $\mathbb{R}^n$ 中 $p$ 个向量的图像下，当 $p = 2$ 时，离差向量 $\boldsymbol{d}_1, \boldsymbol{d}_2$ 张成的平行四边形面积为 $L_{\boldsymbol{d}_1}L_{\boldsymbol{d}_2}\sin\theta = L_{\boldsymbol{d}_1}L_{\boldsymbol{d}_2}\sqrt{1 - \cos^2\theta}$。由 $L_{\boldsymbol{d}_k} = \sqrt{(n-1)s_{kk}}$ 与 $\cos\theta = r_{12}$，

$$
\text{面积} = (n-1)\sqrt{s_{11}s_{22}(1 - r_{12}^2)}, \qquad \det S = \det\begin{bmatrix} s_{11} & \sqrt{s_{11}s_{22}}\,r_{12} \\ \sqrt{s_{11}s_{22}}\,r_{12} & s_{22} \end{bmatrix} = s_{11}s_{22}(1 - r_{12}^2),
$$
故 $\det S = (\text{面积})^2/(n-1)^2$。一般地 $\det S = (n-1)^{-p}(\text{体积})^2$，其中体积指 $\boldsymbol{d}_1, \dots, \boldsymbol{d}_p$ 张成的平行多面体的体积（等于 $\sqrt{\det(B^{\mathsf T}B)}$）。离差向量越长、越不共线，广义方差越大。

在 $\mathbb{R}^p$ 中 $n$ 个点的图像下，若 $\det S > 0$，实心椭球 $\{\boldsymbol{x}\colon (\boldsymbol{x} - \bar{\boldsymbol{x}})^{\mathsf T}S^{-1}(\boldsymbol{x} - \bar{\boldsymbol{x}}) \le c^2\}$（到 $\bar{\boldsymbol{x}}$ 的马氏距离不超过 $c$ 的点）的体积为

$$
\operatorname{vol}\{\boldsymbol{x}\colon (\boldsymbol{x} - \bar{\boldsymbol{x}})^{\mathsf T}S^{-1}(\boldsymbol{x} - \bar{\boldsymbol{x}}) \le c^2\} = k_p(\det S)^{1/2}c^p, \qquad k_p = \frac{2\pi^{p/2}}{p\,\Gamma(p/2)},
$$
因为其半轴为 $c\sqrt{\lambda_i}$，其中 $\lambda_1, \dots, \lambda_p$ 是 $S$ 的特征值，而 $\det S = \lambda_1\lambda_2\cdots\lambda_p$。因此 $\det S$ 度量数据点云主体所占的体积。

**定理 2.1.1** 对样本 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$，以下条件等价：

1. $\det S = 0$；
2. 存在 $\boldsymbol{a} \ne \boldsymbol{0}$ 使 $S\boldsymbol{a} = \boldsymbol{0}$（即 $\boldsymbol{a}$ 是 $S$ 的属于特征值 $0$ 的特征向量）；
3. 对一切 $j$，$\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}}) = 0$：以 $\boldsymbol{a}$ 为系数的中心化数据的线性组合为零，即离差向量 $\boldsymbol{d}_1, \dots, \boldsymbol{d}_p$ 线性相关；
4. 对一切 $j$，$\boldsymbol{a}^{\mathsf T}\boldsymbol{x}_j = c$，其中 $c = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}$：原始数据的这一线性组合是常数。

特别地，$n \le p$ 时总有 $\det S = 0$。

**证明** 由 $\det S = \lambda_1\cdots\lambda_p$ 得 (1)⇔(2)。(2)⇒(3)：$0 = \boldsymbol{a}^{\mathsf T}S\boldsymbol{a} = \frac{1}{n-1}\sum_j[\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})]^2$。(3)⇒(2)：$(n-1)S\boldsymbol{a} = \sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}\boldsymbol{a} = \boldsymbol{0}$。(3)⇔(4) 显然，而 (3) 就是 $B\boldsymbol{a} = a_1\boldsymbol{d}_1 + \cdots + a_p\boldsymbol{d}_p = \boldsymbol{0}$。最后 $\operatorname{rank}(S) = \operatorname{rank}(B) = \operatorname{rank}(HX) \le \operatorname{rank}(H) = n - 1$，所以 $n - 1 < p$ 时 $S$ 奇异。$\square$

广义方差为零说明某些变量是多余的（是其他变量的精确线性函数），在进一步计算（例如求 $S^{-1}$）之前应当删去。

**注 2.1.2** 一个数无法概括一个矩阵。三个协方差矩阵

$$
S = \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix}\ (r = 0.8), \qquad S = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}\ (r = 0), \qquad S = \begin{bmatrix} 5 & -4 \\ -4 & 5 \end{bmatrix}\ (r = -0.8)
$$
都有 $\det S = 9$，描述的点云形状与方向却很不相同。广义方差丢失了相关的方向以及各方向上的变异信息；$S$ 的特征值与特征向量保留了这些信息，这就引出了主成分分析（[3.4.5](/3.4.5)）。

![三组均值为 (2, 1) 的模拟样本，其协方差矩阵的相关系数分别为 0.8、0、-0.8，广义方差都是 det S = 9。椭圆是真实协方差下的 95% 等高线 (x - 均值)^T S^(-1) (x - 均值) = 5.99，面积相同；箭头是沿特征向量的半轴。](./plots/generalized-variance.py)

## 2.2. 样本统计量与总体参数

现在设数据矩阵的各行是**随机样本** $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$（定义 1.2.2），于是 $\bar{\boldsymbol{X}}$、$S$、$S_n$ 都是随机的。这些统计量与总体均值向量 $\boldsymbol{\mu}$、协方差矩阵 $\Sigma$ 有什么关系？下面的结果除二阶矩有限外，不需要对 $f(\boldsymbol{x})$ 的形式作任何假定。

**定理 2.2.1** 设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自均值向量为 $\boldsymbol{\mu}$、协方差矩阵为 $\Sigma$ 的联合分布的随机样本，则

$$
\mathbb{E}\bar{\boldsymbol{X}} = \boldsymbol{\mu}, \qquad \operatorname{Cov}(\bar{\boldsymbol{X}}) = \frac{1}{n}\Sigma, \qquad \mathbb{E}S_n = \frac{n-1}{n}\Sigma, \qquad \mathbb{E}S = \Sigma.
$$
因此 $\bar{\boldsymbol{X}}$ 与 $S$ 分别是 $\boldsymbol{\mu}$ 与 $\Sigma$ 的**无偏估计**，而 $S_n$ 是有偏的。

**证明** 由线性性，$\mathbb{E}\bar{\boldsymbol{X}} = \frac{1}{n}\sum_j\mathbb{E}\boldsymbol{X}_j = \boldsymbol{\mu}$。由独立性交叉协方差为零，故

$$
\operatorname{Cov}(\bar{\boldsymbol{X}}) = \mathbb{E}\left[\frac{1}{n}\sum_j(\boldsymbol{X}_j - \boldsymbol{\mu})\cdot\frac{1}{n}\sum_l(\boldsymbol{X}_l - \boldsymbol{\mu})^{\mathsf T}\right] = \frac{1}{n^2}\sum_{j=1}^{n}\mathbb{E}[(\boldsymbol{X}_j - \boldsymbol{\mu})(\boldsymbol{X}_j - \boldsymbol{\mu})^{\mathsf T}] = \frac{1}{n}\Sigma.
$$
对 $S_n$，展开 $\sum_j(\boldsymbol{X}_j - \bar{\boldsymbol{X}})(\boldsymbol{X}_j - \bar{\boldsymbol{X}})^{\mathsf T} = \sum_j\boldsymbol{X}_j\boldsymbol{X}_j^{\mathsf T} - n\bar{\boldsymbol{X}}\bar{\boldsymbol{X}}^{\mathsf T}$，并利用 $\mathbb{E}[\boldsymbol{X}_j\boldsymbol{X}_j^{\mathsf T}] = \Sigma + \boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf T}$ 与 $\mathbb{E}[\bar{\boldsymbol{X}}\bar{\boldsymbol{X}}^{\mathsf T}] = \frac{1}{n}\Sigma + \boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf T}$：

$$
\mathbb{E}\left[\sum_j(\boldsymbol{X}_j - \bar{\boldsymbol{X}})(\boldsymbol{X}_j - \bar{\boldsymbol{X}})^{\mathsf T}\right] = n(\Sigma + \boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf T}) - n\left(\frac{1}{n}\Sigma + \boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf T}\right) = (n-1)\Sigma.
$$
分别除以 $n$ 与 $n - 1$ 即得后两个结论。$\square$

在例 2.1.1 中，总体为 $\boldsymbol{X} = (X_1, X_2)^{\mathsf T}$，$\boldsymbol{\mu} = (\mu_1, \mu_2)^{\mathsf T}$，$\Sigma = \begin{bmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{bmatrix}$；样本给出 $\boldsymbol{\mu}$ 的估计 $\bar{\boldsymbol{x}} = (4, \frac{8}{3})^{\mathsf T}$ 与 $\Sigma$ 的估计 $S$。样本矩阵的每个元素估计总体矩阵的相应元素。

变量的线性组合也是如此。对常数向量 $\boldsymbol{b}, \boldsymbol{c}$ 与 $q \times p$ 常数矩阵 $A$，总体层面的结果见 [3.1.15](/3.1.15)：

$$
\mathbb{E}(\boldsymbol{c}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{c}^{\mathsf T}\boldsymbol{\mu}, \quad \operatorname{Var}(\boldsymbol{c}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{c}^{\mathsf T}\Sigma\boldsymbol{c}, \quad \operatorname{Cov}(\boldsymbol{b}^{\mathsf T}\boldsymbol{X}, \boldsymbol{c}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{b}^{\mathsf T}\Sigma\boldsymbol{c}, \quad \mathbb{E}(A\boldsymbol{X}) = A\boldsymbol{\mu}, \quad \operatorname{Cov}(A\boldsymbol{X}) = A\Sigma A^{\mathsf T}.
$$
例如 $\operatorname{Cov}(\boldsymbol{b}^{\mathsf T}\boldsymbol{X}, \boldsymbol{c}^{\mathsf T}\boldsymbol{X}) = \mathbb{E}[\boldsymbol{b}^{\mathsf T}(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\boldsymbol{c}] = \boldsymbol{b}^{\mathsf T}\Sigma\boldsymbol{c}$，更一般地 $\operatorname{Cov}(B\boldsymbol{X}, C\boldsymbol{X}) = B\Sigma C^{\mathsf T}$；它们是 $\mathbb{E}(aX) = a\,\mathbb{E}X$ 与 $\operatorname{Var}(aX) = a^2\operatorname{Var}(X)$ 的矩阵版本。样本版本的形式完全相同。

**定理 2.2.2** 设 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ 的样本均值向量为 $\bar{\boldsymbol{x}}$，样本协方差矩阵为 $S$。两个线性组合的取值 $\boldsymbol{b}^{\mathsf T}\boldsymbol{x}_j$ 与 $\boldsymbol{c}^{\mathsf T}\boldsymbol{x}_j$（$j = 1, \dots, n$）的

$$
\text{样本均值为 } \boldsymbol{b}^{\mathsf T}\bar{\boldsymbol{x}},\ \boldsymbol{c}^{\mathsf T}\bar{\boldsymbol{x}}, \qquad \text{样本方差为 } \boldsymbol{b}^{\mathsf T}S\boldsymbol{b},\ \boldsymbol{c}^{\mathsf T}S\boldsymbol{c}, \qquad \text{样本协方差为 } \boldsymbol{b}^{\mathsf T}S\boldsymbol{c}.
$$
更一般地，$q$ 个线性组合 $A\boldsymbol{x}_j$ 的样本均值向量为 $A\bar{\boldsymbol{x}}$，样本协方差矩阵为 $ASA^{\mathsf T}$。

**证明** $A\boldsymbol{x}_j$ 的均值为 $\frac{1}{n}\sum_jA\boldsymbol{x}_j = A\bar{\boldsymbol{x}}$，样本协方差矩阵为 $\frac{1}{n-1}\sum_jA(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}A^{\mathsf T} = ASA^{\mathsf T}$。其余结论是 $A = \boldsymbol{c}^{\mathsf T}$ 与 $A = \begin{bmatrix} \boldsymbol{b}^{\mathsf T} \\ \boldsymbol{c}^{\mathsf T} \end{bmatrix}$ 的特例。$\square$

**例 2.2.1** 在例 2.1.1 中，线性组合 $c_1x_1 + c_2x_2$ 的取值为 $\boldsymbol{c}^{\mathsf T}(4, 1)^{\mathsf T}$、$\boldsymbol{c}^{\mathsf T}(5, 2)^{\mathsf T}$、$\boldsymbol{c}^{\mathsf T}(3, 5)^{\mathsf T}$，样本均值为 $4c_1 + \frac{8}{3}c_2$，样本方差为

$$
\boldsymbol{c}^{\mathsf T}S\boldsymbol{c} = \begin{bmatrix} c_1 & c_2 \end{bmatrix}\begin{bmatrix} 1 & -\frac{3}{2} \\ -\frac{3}{2} & \frac{13}{3} \end{bmatrix}\begin{bmatrix} c_1 \\ c_2 \end{bmatrix} = c_1^2 - 3c_1c_2 + \frac{13}{3}c_2^2.
$$
取 $\boldsymbol{c} = (1, 1)^{\mathsf T}$，取值为 $5, 7, 8$，均值为 $\frac{20}{3}$，方差为 $\frac{7}{3}$，与公式一致。

## 2.3. 多元正态分布

### 2.3.1. 为什么是多元正态分布

多元正态分布扮演四个角色。它是构造更复杂分布（Gauss 混合模型）的基本构件，也是检验新方法的基准。它提供了一个坐标系：其均值向量与协方差矩阵定义了"正常的"线性相依，异常、非线性等偏离都相对于它来度量。它是许多现代方法的数学核心：生成模型的隐空间、共轭 Bayes 分析、Gauss 过程。它还训练统计直觉：用向量思考，区分联合分布与边缘分布，通过条件化更新认识。

### 2.3.2. 密度与等高线

一维时 $X \sim \mathcal{N}(\mu, \sigma^2)$ 的密度为 $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left\{-\frac{(x - \mu)^2}{2\sigma^2}\right\}$，指数是到 $\mu$ 的标准化距离平方的负一半。把它换成**马氏距离**的平方，就得到多元密度。

**定义 2.3.1（多元正态分布）** 设 $\boldsymbol{\mu} \in \mathbb{R}^p$，$\Sigma$ 为 $p \times p$ 正定矩阵。若 $p$ 维随机向量 $\boldsymbol{X}$ 的密度为

$$
f(\boldsymbol{x}) = \frac{1}{(2\pi)^{p/2}(\det\Sigma)^{1/2}}\exp\left\{-\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\right\}, \qquad \boldsymbol{x} \in \mathbb{R}^p, \tag{2.1}
$$
则称 $\boldsymbol{X}$ 服从多元正态分布 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$。

在 [3.1.15](/3.1.15) 中，多元正态分布定义为 $\boldsymbol{\mu} + B\boldsymbol{\varepsilon}$，其中 $\boldsymbol{\varepsilon}$ 的分量独立且服从标准正态分布（[定义 15.2.1](/3.1.15#def-15.2.1)），式 (2.1) 是作为其密度推导出来的；两种定义等价，用线性组合的刻画（下面的定理 2.4.1）也等价。这一分布是连续的，完全由前两阶矩确定：$\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X}$，$\Sigma = \operatorname{Cov}(\boldsymbol{X})$。

**例 2.3.1（二元正态密度）** $p = 2$ 时有五个自由参数，两个描述位置，三个描述尺度：

$$
\boldsymbol{\mu} = \begin{bmatrix} \mu_1 \\ \mu_2 \end{bmatrix} = \begin{bmatrix} \mathbb{E}X_1 \\ \mathbb{E}X_2 \end{bmatrix}, \qquad \Sigma = \begin{bmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{bmatrix} = \begin{bmatrix} \sigma_{11} & \rho_{12}\sqrt{\sigma_{11}\sigma_{22}} \\ \rho_{12}\sqrt{\sigma_{11}\sigma_{22}} & \sigma_{22} \end{bmatrix},
$$
式 (2.1) 化为 [3.1.6](/3.1.6) 的**二元正态分布**。$\sigma_{11} = \sigma_{22}$、$\rho_{12} = 0$ 时密度曲面是旋转对称的钟形；$\rho_{12} = 0.75$ 时是沿对角线的山脊。$\rho_{12}$ 从 $0$ 增向 $1$ 时，等高线从圆变为沿直线 $x_2 = x_1$ 越来越扁的椭圆；$\rho_{12}$ 为负时则沿 $x_2 = -x_1$。

密度只通过距离平方 $(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})$ 依赖于 $\boldsymbol{x}$，所以其等高线就是到 $\boldsymbol{\mu}$ 的马氏距离为常数的集合。

**定理 2.3.1（等密度轮廓）** 设 $\Sigma$ 的特征值为 $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_p > 0$，单位特征向量为 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$，$\Sigma\boldsymbol{e}_i = \lambda_i\boldsymbol{e}_i$。$\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的等密度轮廓

$$
\{\boldsymbol{x}\colon (\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) = c^2\}
$$
是以 $\boldsymbol{\mu}$ 为中心、以 $\pm c\sqrt{\lambda_i}\,\boldsymbol{e}_i$（$i = 1, \dots, p$）为轴的椭球面。

**证明** $\Sigma^{-1} = \sum_i\lambda_i^{-1}\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$（性质 1.6.1），记 $y_i = \boldsymbol{e}_i^{\mathsf T}(\boldsymbol{x} - \boldsymbol{\mu})$ 为 $\boldsymbol{x} - \boldsymbol{\mu}$ 沿各特征向量的坐标，方程化为 $\sum_i y_i^2/\lambda_i = c^2$：沿 $\boldsymbol{e}_i$ 半轴为 $c\sqrt{\lambda_i}$ 的椭球面。$\square$

最长的轴沿 $\Sigma$ 最大特征值的特征向量，即方差最大的方向。下面的定理 2.4.7 给出这些椭球所含的概率。

![左：二元正态分布的 400 个样本点，以及含 50%、90%、99% 概率的等密度轮廓；箭头是 90% 椭圆的半轴 c sqrt(lambda_i) e_i。右：水平为 1 - alpha 的椭圆内样本点所占比例对 1 - alpha 作图，接近对角线，与定理 2.4.7 一致。](./plots/mvn-contours.py)

### 2.3.3. 由独立标准正态变量构造

**定理 2.3.2** 设 $Z_1, \dots, Z_p$ 独立同分布于 $\mathcal{N}(0, 1)$，$\boldsymbol{Z} = (Z_1, \dots, Z_p)^{\mathsf T}$，$\Sigma$ 为对称正定矩阵，$\boldsymbol{\mu} \in \mathbb{R}^p$，则

$$
\boldsymbol{X} = \boldsymbol{\mu} + \Sigma^{1/2}\boldsymbol{Z} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma).
$$

**证明** 由独立性，$\boldsymbol{Z}$ 的密度为 $f_{\boldsymbol{Z}}(\boldsymbol{z}) = \prod_jf_j(z_j) = (2\pi)^{-p/2}\exp(-\boldsymbol{z}^{\mathsf T}\boldsymbol{z}/2)$。变换 $\boldsymbol{x} = \boldsymbol{\mu} + \Sigma^{1/2}\boldsymbol{z}$ 可逆，$\boldsymbol{z} = \Sigma^{-1/2}(\boldsymbol{x} - \boldsymbol{\mu})$；由 $\partial\boldsymbol{z}/\partial\boldsymbol{x} = \Sigma^{-1/2}$，**Jacobi 行列式**的绝对值为 $\det\Sigma^{-1/2} = (\det\Sigma)^{-1/2}$。于是

$$
f(\boldsymbol{x}) = (\det\Sigma)^{-1/2}(2\pi)^{-p/2}\exp\left\{-\frac{1}{2}[\Sigma^{-1/2}(\boldsymbol{x} - \boldsymbol{\mu})]^{\mathsf T}[\Sigma^{-1/2}(\boldsymbol{x} - \boldsymbol{\mu})]\right\} = \frac{1}{(2\pi)^{p/2}(\det\Sigma)^{1/2}}\exp\left\{-\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\right\},
$$
这里用到 $\Sigma^{-1/2}\Sigma^{-1/2} = \Sigma^{-1}$。$\square$

一维情形即 $X = \mu + \sigma Z$。另一种证明用**特征函数**，见 [3.1.15](/3.1.15)。在根本的意义上，多元正态分布就是独立 Gauss 变量的仿射变换的分布；定理 2.3.2（或用 **Cholesky 分解** $\Sigma = LL^{\mathsf T}$ 代替 $\Sigma^{1/2}$ 的变体）正是模拟多元正态样本的方法。反过来，$\boldsymbol{Z} = \Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu})$ 把正态向量标准化，这是 [3.4.1](/3.4.1) 的 1.6.4 节中白化的概率版本：旋转到等高椭球的轴上，再把它们缩放为单位长度。

## 2.4. 多元正态分布的性质

下面的性质已在 [3.1.15](/3.1.15) 中证明，大多借助特征函数；这里按本课程全程使用的形式重述。其中两条是后续一切的关键工具：线性变换下的封闭性（定理 2.4.2）与独立等价于协方差为零（定理 2.4.4）。定理 2.4.1 可作为等价定义，也是判断多元正态性最快的方法；边缘分布与条件分布（定理 2.4.3 与 2.4.5）在其他课程中用得更多，在本课程中主要用来练习如何运用这两个关键工具；定理 2.4.7 与 2.4.8 是 [3.4.3](/3.4.3) 中推断的基础。

### 2.4.1. 线性组合与线性变换

**定理 2.4.1** 随机向量 $\boldsymbol{X}$ 服从 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$，当且仅当对每个 $\boldsymbol{a} \in \mathbb{R}^p$，$\boldsymbol{a}^{\mathsf T}\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a})$。

这就是[定理 15.3.3](/3.1.15#thm-15.3.3)：$Y = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ 在 $t$ 处的特征函数等于 $\boldsymbol{X}$ 在 $t\boldsymbol{a}$ 处的特征函数，所以所有 $\boldsymbol{a}$ 对应的一维特征函数确定了多元特征函数。例如

$$
\begin{bmatrix} X_1 \\ X_2 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 1 \\ -5 \end{bmatrix}, \begin{bmatrix} 4 & -2 \\ -2 & 9 \end{bmatrix}\right) \iff \text{对一切 } a_1, a_2, \ a_1X_1 + a_2X_2 \sim \mathcal{N}\left(a_1 - 5a_2,\ 4a_1^2 - 4a_1a_2 + 9a_2^2\right).
$$

**定理 2.4.2（线性变换）** 若 $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$，$A$ 为 $q \times p$ 常数矩阵（$q \le p$），且 $A\Sigma A^{\mathsf T}$ 可逆，则

$$
A\boldsymbol{X} = \begin{bmatrix} a_{11}X_1 + \cdots + a_{1p}X_p \\ \vdots \\ a_{q1}X_1 + \cdots + a_{qp}X_p \end{bmatrix} \sim \mathcal{N}_q(A\boldsymbol{\mu}, A\Sigma A^{\mathsf T}).
$$
对任意常数向量 $\boldsymbol{d}$，还有 $\boldsymbol{X} + \boldsymbol{d} \sim \mathcal{N}_p(\boldsymbol{\mu} + \boldsymbol{d}, \Sigma)$。

**证明** 对 $\boldsymbol{b} \in \mathbb{R}^q$，由定理 2.4.1，$\boldsymbol{b}^{\mathsf T}(A\boldsymbol{X}) = (A^{\mathsf T}\boldsymbol{b})^{\mathsf T}\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{b}^{\mathsf T}A\boldsymbol{\mu}, \boldsymbol{b}^{\mathsf T}A\Sigma A^{\mathsf T}\boldsymbol{b})$，再由定理 2.4.1 即得结论。第二个结论对 $\boldsymbol{b}^{\mathsf T}(\boldsymbol{X} + \boldsymbol{d})$ 作同样的论证。$\square$

**例 2.4.1** 取上面的 $\boldsymbol{X}$，令 $\boldsymbol{Y} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\boldsymbol{X}$，则

$$
\boldsymbol{Y} \sim \mathcal{N}\left(\begin{bmatrix} 1 \\ 0 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ -5 \end{bmatrix},\ \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 4 & -2 \\ -2 & 9 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}^{\mathsf T}\right) = \mathcal{N}\left(\begin{bmatrix} 2 \\ -4 \end{bmatrix}, \begin{bmatrix} 4 & 2 \\ 2 & 9 \end{bmatrix}\right).
$$

### 2.4.2. 边缘分布与独立性

把 $\boldsymbol{X}$、其均值向量与协方差矩阵相应地分块为

$$
\boldsymbol{X} = \begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix}, \qquad \boldsymbol{\mu} = \begin{bmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{bmatrix}, \qquad \Sigma = \begin{bmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{bmatrix}, \tag{2.2}
$$
其中 $\boldsymbol{X}_1$、$\boldsymbol{\mu}_1$ 为 $q \times 1$，$\boldsymbol{X}_2$、$\boldsymbol{\mu}_2$ 为 $(p - q) \times 1$，$\Sigma_{11}$ 为 $q \times q$。这里 $\Sigma_{11} = \operatorname{Cov}(\boldsymbol{X}_1)$，$\Sigma_{22} = \operatorname{Cov}(\boldsymbol{X}_2)$，$\Sigma_{12} = \operatorname{Cov}(\boldsymbol{X}_1, \boldsymbol{X}_2) = \Sigma_{21}^{\mathsf T}$ 是 $\boldsymbol{X}_1$ 各分量与 $\boldsymbol{X}_2$ 各分量之间协方差构成的 $q \times (p - q)$ 矩阵。（若不熟悉分块记号，可以先把下面每个论证中的 $\boldsymbol{X}_1$、$\boldsymbol{X}_2$ 都读作标量，此时 $\Sigma = \begin{bmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{bmatrix}$。）

**定理 2.4.3（边缘分布）** $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的任意一组分量都服从正态分布：在分块 (2.2) 下，$\boldsymbol{X}_1 \sim \mathcal{N}_q(\boldsymbol{\mu}_1, \Sigma_{11})$。

这是定理 2.4.2 取 $A = [I_q, O]$。例如

$$
\begin{bmatrix} X_1 \\ X_2 \\ X_3 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 2 \\ 7 \\ 3 \end{bmatrix}, \begin{bmatrix} 4 & -1 & 2 \\ -1 & 9 & -3 \\ 2 & -3 & 8 \end{bmatrix}\right) \implies X_1 \sim \mathcal{N}(2, 4), \quad \begin{bmatrix} X_2 \\ X_3 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 7 \\ 3 \end{bmatrix}, \begin{bmatrix} 9 & -3 \\ -3 & 8 \end{bmatrix}\right).
$$
反之不成立：边缘正态并不意味着联合正态。

**定理 2.4.4（独立性与零协方差）**

1. 若 $\boldsymbol{X}_1$（$q_1 \times 1$）与 $\boldsymbol{X}_2$（$q_2 \times 1$）独立，则 $\operatorname{Cov}(\boldsymbol{X}_1, \boldsymbol{X}_2) = O$，即 $q_1 \times q_2$ 零矩阵。
2. 若 $\begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix} \sim \mathcal{N}_{q_1+q_2}\left(\begin{bmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{bmatrix}, \begin{bmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{bmatrix}\right)$，则 $\boldsymbol{X}_1$ 与 $\boldsymbol{X}_2$ 独立当且仅当 $\Sigma_{12} = O$。
3. 若 $\boldsymbol{X}_1 \sim \mathcal{N}_{q_1}(\boldsymbol{\mu}_1, \Sigma_{11})$ 与 $\boldsymbol{X}_2 \sim \mathcal{N}_{q_2}(\boldsymbol{\mu}_2, \Sigma_{22})$ 独立，则

$$
\begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix} \sim \mathcal{N}_{q_1+q_2}\left(\begin{bmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{bmatrix}, \begin{bmatrix} \Sigma_{11} & O \\ O & \Sigma_{22} \end{bmatrix}\right).
$$

第 1 条对任意分布成立；第 2 条即[定理 15.4.1](/3.1.15#thm-15.4.1)（$\Sigma_{12} = O$ 时特征函数可分解）；第 3 条成立是因为独立向量的联合特征函数是两个正态特征函数之积。例如

$$
\begin{bmatrix} X_1 \\ X_2 \\ X_3 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 2 \\ 7 \\ 3 \end{bmatrix}, \begin{bmatrix} 4 & 0 & 0 \\ 0 & 9 & -3 \\ 0 & -3 & 8 \end{bmatrix}\right) \iff X_1 \sim \mathcal{N}(2, 4),\ \begin{bmatrix} X_2 \\ X_3 \end{bmatrix} \sim \mathcal{N}\left(\begin{bmatrix} 7 \\ 3 \end{bmatrix}, \begin{bmatrix} 9 & -3 \\ -3 & 8 \end{bmatrix}\right),\ X_1 \text{ 与 } (X_2, X_3) \text{ 独立}.
$$

**注 2.4.1** 第 2 条中联合正态是必不可少的。若 $\boldsymbol{X}_1$ 与 $\boldsymbol{X}_2$ 独立且各自正态，则叠起来的向量正态（第 3 条）。若二者不独立，叠起来的向量可能正态，也可能不正态。反例：设 $X_1 \sim \mathcal{N}(0, 1)$，$S$ 与 $X_1$ 独立，$\mathbb{P}(S = 1) = \mathbb{P}(S = -1) = \frac{1}{2}$，$X_2 = SX_1$。则 $X_2 \sim \mathcal{N}(0, 1)$ 且 $\operatorname{Cov}(X_1, X_2) = 0$，但 $X_1$ 与 $X_2$ 不独立（[注 15.3.1](/3.1.15#rem-15.3.1)）。由定理 2.4.1 立即可知 $(X_1, X_2)^{\mathsf T}$ 不是二元正态的：线性组合 $X_1 + X_2$ 以概率 $\frac{1}{2}$ 等于 $0$（否则等于 $2X_1$），这不是正态分布。所以"协方差为零等价于独立"只在联合正态下成立。

### 2.4.3. 条件分布

**定理 2.4.5（条件分布）** 设 $\boldsymbol{X} = \begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix} \sim \mathcal{N}_{q_1+q_2}(\boldsymbol{\mu}, \Sigma)$ 按 (2.2) 分块，$\det\Sigma_{22} > 0$，则在 $\boldsymbol{X}_2 = \boldsymbol{x}_2$ 的条件下，$\boldsymbol{X}_1$ 服从正态分布，且

$$
\text{均值} = \boldsymbol{\mu}_1 + \Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{x}_2 - \boldsymbol{\mu}_2), \qquad \text{协方差} = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}.
$$

**证明** 当 $\boldsymbol{X}_1$ 与 $\boldsymbol{X}_2$ 不独立时，我们设法从 $\boldsymbol{X}_1$ 中去掉与 $\boldsymbol{X}_2$ 有关的部分，使 $\boldsymbol{X}_1 - g(\boldsymbol{X}_2)$ 与 $\boldsymbol{X}_2$ 独立。对正态向量，相依关系只能是线性的，所以只需考虑 $g(\boldsymbol{X}_2) = A\boldsymbol{X}_2$。令 $\boldsymbol{Z} = \boldsymbol{X}_1 - \boldsymbol{\mu}_1 - A(\boldsymbol{X}_2 - \boldsymbol{\mu}_2)$。向量

$$
\begin{bmatrix} \boldsymbol{Z} \\ \boldsymbol{X}_2 - \boldsymbol{\mu}_2 \end{bmatrix} = \begin{bmatrix} I & -A \\ O & I \end{bmatrix}\begin{bmatrix} \boldsymbol{X}_1 - \boldsymbol{\mu}_1 \\ \boldsymbol{X}_2 - \boldsymbol{\mu}_2 \end{bmatrix}
$$
是正态向量的线性变换，因而是正态的（定理 2.4.2）。由定理 2.4.4，$\boldsymbol{Z}$ 与 $\boldsymbol{X}_2$ 独立当且仅当

$$
\operatorname{Cov}(\boldsymbol{Z}, \boldsymbol{X}_2) = \Sigma_{12} - A\Sigma_{22} = O, \qquad \text{即 } A = \Sigma_{12}\Sigma_{22}^{-1}.
$$
取这个 $A$，$\boldsymbol{Z}$ 的均值为 $\boldsymbol{0}$，协方差矩阵为

$$
\operatorname{Cov}(\boldsymbol{Z}) = \Sigma_{11} - A\Sigma_{21} - \Sigma_{12}A^{\mathsf T} + A\Sigma_{22}A^{\mathsf T} = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}.
$$
在 $\boldsymbol{X}_2 = \boldsymbol{x}_2$ 的条件下，$\boldsymbol{X}_1 = \boldsymbol{\mu}_1 + \Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{x}_2 - \boldsymbol{\mu}_2) + \boldsymbol{Z}$，而 $\boldsymbol{Z}$ 与 $\boldsymbol{X}_2$ 独立，所以条件分布就是 $\boldsymbol{Z}$ 的分布平移所述均值。$\square$

**例 2.4.2** 对定理 2.4.3 中的三维例子，求 $X_2 = 1$、$X_3 = 0$ 条件下 $X_1$ 的分布。这里 $\Sigma_{12} = (-1, 2)$，$\Sigma_{22} = \begin{bmatrix} 9 & -3 \\ -3 & 8 \end{bmatrix}$，$\Sigma_{22}^{-1} = \frac{1}{63}\begin{bmatrix} 8 & 3 \\ 3 & 9 \end{bmatrix}$，故 $\Sigma_{12}\Sigma_{22}^{-1} = \frac{1}{63}(-2, 15)$，

$$
\text{均值} = 2 + \frac{1}{63}(-2, 15)\begin{bmatrix} 1 - 7 \\ 0 - 3 \end{bmatrix} = 2 - \frac{33}{63} = \frac{31}{21}, \qquad \text{方差} = 4 - \frac{1}{63}(-2, 15)\begin{bmatrix} -1 \\ 2 \end{bmatrix} = 4 - \frac{32}{63} = \frac{220}{63}.
$$
于是 $X_1 \mid X_2 = 1, X_3 = 0 \sim \mathcal{N}\left(\frac{31}{21}, \frac{220}{63}\right)$；条件方差小于边缘方差 $4$。

**注 2.4.2** 条件协方差 $\Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ 即 $\Sigma_{22}$ 的 **Schur 补**，它与取值 $\boldsymbol{x}_2$ 无关，而条件均值是 $\boldsymbol{x}_2$ 的线性函数。由于**条件期望**是均方意义下的最佳预测（[3.1.9](/3.1.9)），在正态下最佳预测等于最佳线性预测；这就是与线性回归（[3.3](/3.3)、[3.4.7](/3.4.7)）的联系。Schur 补也出现在 $\Sigma$ 的逆中：由分块求逆公式（[2.1.2](/2.1.2)），

$$
\begin{bmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{bmatrix}^{-1} = \begin{bmatrix} (\Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21})^{-1} & * \\ * & * \end{bmatrix},
$$
所以精度矩阵 $\Sigma^{-1}$ 的左上块是条件协方差矩阵的逆。特别地，若 $\boldsymbol{X}_1 = (X_i, X_k)^{\mathsf T}$，$\boldsymbol{X}_2$ 由其余分量组成，则 $(\Sigma^{-1})_{ik} = 0$ 当且仅当给定其余分量时 $X_i$ 与 $X_k$ 条件独立。这是 Gauss 图模型的基础。

**定理 2.4.6** 设 $\boldsymbol{X}_1 \mid \boldsymbol{X}_2 = \boldsymbol{x}_2 \sim \mathcal{N}(A\boldsymbol{x}_2, \Omega)$，其中 $A$ 为常数矩阵，$\Omega$ 为常数正定矩阵，且 $\boldsymbol{X}_2 \sim \mathcal{N}(\boldsymbol{\mu}_2, \Sigma_{22})$。则 $\begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix}$ 服从多元正态分布，且

$$
\boldsymbol{X}_1 \sim \mathcal{N}(A\boldsymbol{\mu}_2, \Omega + A\Sigma_{22}A^{\mathsf T}).
$$

**证明** 令 $\boldsymbol{E} = \boldsymbol{X}_1 - A\boldsymbol{X}_2$。给定 $\boldsymbol{X}_2 = \boldsymbol{x}_2$ 时 $\boldsymbol{E} \sim \mathcal{N}(\boldsymbol{0}, \Omega)$，这个分布与 $\boldsymbol{x}_2$ 无关；所以 $\boldsymbol{E}$ 与 $\boldsymbol{X}_2$ 独立且 $\boldsymbol{E} \sim \mathcal{N}(\boldsymbol{0}, \Omega)$。由定理 2.4.4 第 3 条，$(\boldsymbol{E}^{\mathsf T}, \boldsymbol{X}_2^{\mathsf T})^{\mathsf T}$ 正态，由定理 2.4.2，$\begin{bmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{bmatrix} = \begin{bmatrix} I & A \\ O & I \end{bmatrix}\begin{bmatrix} \boldsymbol{E} \\ \boldsymbol{X}_2 \end{bmatrix}$ 正态，其中 $\boldsymbol{X}_1 = \boldsymbol{E} + A\boldsymbol{X}_2$ 的均值为 $A\boldsymbol{\mu}_2$，协方差为 $\Omega + A\Sigma_{22}A^{\mathsf T}$。$\square$

这种分层模型（正态观测的均值本身也服从正态分布）是正态先验下 Bayes 统计的基本计算。

### 2.4.4. 卡方性质与正态向量的线性组合

**定理 2.4.7** 设 $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$，$\Sigma$ 正定，则

1. $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_p$，即自由度为 $p$ 的**卡方分布**；
2. 分布 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 赋予实心椭球 $\{\boldsymbol{x}\colon (\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) \le \chi^2_{p,\alpha}\}$ 的概率为 $1 - \alpha$，其中 $\chi^2_{p,\alpha}$ 是 $\chi^2_p$ 的上 $\alpha$ 分位数。

**证明** 由定理 2.4.2，$\boldsymbol{Z} = \Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \mathcal{N}_p(\boldsymbol{0}, I_p)$，由定理 2.4.4，$Z_1, \dots, Z_p$ 独立同分布于 $\mathcal{N}(0, 1)$，故

$$
(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) = [\Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu})]^{\mathsf T}[\Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu})] = \boldsymbol{Z}^{\mathsf T}\boldsymbol{Z} = Z_1^2 + \cdots + Z_p^2 \sim \chi^2_p.
$$
第 2 条由第 1 条得到。$\square$

因此正态向量到其均值的马氏距离平方服从 $\chi^2_p$，其均值为 $p$，与推论 1.3.2 一致。$p = 2$ 时 $\chi^2_2$ 就是均值为 $2$ 的指数分布，$\chi^2_{2,0.05} \approx 5.99$。用估计代替 $\boldsymbol{\mu}$ 与 $\Sigma$，得到椭圆 $\{\boldsymbol{x}\colon (\boldsymbol{x} - \hat{\boldsymbol{\mu}})^{\mathsf T}\hat\Sigma^{-1}(\boldsymbol{x} - \hat{\boldsymbol{\mu}}) \le \chi^2_{2,\alpha}\}$；若数据是正态的，它应当包含约 $100(1 - \alpha)\%$ 的观测，这是检查正态性的一种简单图示方法。

**定理 2.4.8（独立正态向量的线性组合）** 设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 相互独立，$\boldsymbol{X}_j \sim \mathcal{N}_p(\boldsymbol{\mu}_j, \Sigma)$（协方差矩阵都是 $\Sigma$），则

1. $\boldsymbol{V}_1 = c_1\boldsymbol{X}_1 + c_2\boldsymbol{X}_2 + \cdots + c_n\boldsymbol{X}_n \sim \mathcal{N}_p\left(\sum_{j=1}^{n}c_j\boldsymbol{\mu}_j,\ \left(\sum_{j=1}^{n}c_j^2\right)\Sigma\right)$；
2. $\boldsymbol{V}_1$ 与 $\boldsymbol{V}_2 = b_1\boldsymbol{X}_1 + \cdots + b_n\boldsymbol{X}_n$ 联合服从多元正态分布，协方差矩阵为

$$
\begin{bmatrix} \left(\sum_{j}c_j^2\right)\Sigma & (\boldsymbol{b}^{\mathsf T}\boldsymbol{c})\Sigma \\ (\boldsymbol{b}^{\mathsf T}\boldsymbol{c})\Sigma & \left(\sum_{j}b_j^2\right)\Sigma \end{bmatrix};
$$
3. 因此，若 $\boldsymbol{b}^{\mathsf T}\boldsymbol{c} = \sum_{j=1}^{n}b_jc_j = 0$，则 $\boldsymbol{V}_1$ 与 $\boldsymbol{V}_2$ 独立。

**证明** 由定理 2.4.4 第 3 条，叠起来的 $np$ 维向量 $\tilde{\boldsymbol{X}} = (\boldsymbol{X}_1^{\mathsf T}, \dots, \boldsymbol{X}_n^{\mathsf T})^{\mathsf T}$ 是正态的，协方差为分块对角的 $\operatorname{diag}(\Sigma, \dots, \Sigma)$。$\boldsymbol{V}_1 = [c_1I_p, \dots, c_nI_p]\tilde{\boldsymbol{X}}$，$\boldsymbol{V}_2$ 类似，所以 $(\boldsymbol{V}_1^{\mathsf T}, \boldsymbol{V}_2^{\mathsf T})^{\mathsf T}$ 是 $\tilde{\boldsymbol{X}}$ 的线性变换，由定理 2.4.2 是正态的（当 $\boldsymbol{b}$ 与 $\boldsymbol{c}$ 线性相关时协方差矩阵奇异，此时结论理解为协方差奇异的正态分布）。由双线性与独立性得协方差：

$$
\operatorname{Cov}(\boldsymbol{V}_1, \boldsymbol{V}_2) = \operatorname{Cov}\left(\sum_jc_j\boldsymbol{X}_j, \sum_lb_l\boldsymbol{X}_l\right) = \sum_jc_jb_j\operatorname{Cov}(\boldsymbol{X}_j) = (\boldsymbol{b}^{\mathsf T}\boldsymbol{c})\Sigma.
$$
第 3 条由定理 2.4.4 得到。$\square$

例如正态样本的样本均值 $\bar{\boldsymbol{X}} = \frac{1}{n}\boldsymbol{X}_1 + \cdots + \frac{1}{n}\boldsymbol{X}_n$ 服从 $\mathcal{N}_p(\boldsymbol{\mu}, \frac{1}{n}\Sigma)$，而任何满足 $\sum_jb_j = 0$ 的组合 $\sum_jb_j\boldsymbol{X}_j$ 都与它独立。这是 [3.4.3](/3.4.3) 中 $(\bar{\boldsymbol{X}}, S)$ 的抽样分布的关键。

## 2.5. 正态假定下的估计

### 2.5.1. 极大似然估计

设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的随机样本：各 $\boldsymbol{X}_j$ 相互独立，且每个 $\boldsymbol{X}_j \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$。对观测值 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$，把联合密度看作 $(\boldsymbol{\mu}, \Sigma)$ 的函数，就是**似然函数**

$$
L(\boldsymbol{\mu}, \Sigma) = \prod_{j=1}^{n}\frac{1}{(2\pi)^{p/2}(\det\Sigma)^{1/2}}\mathrm{e}^{-(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu})/2} = \frac{1}{(2\pi)^{np/2}(\det\Sigma)^{n/2}}\exp\left\{-\frac{1}{2}\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu})\right\},
$$
其**对数似然函数**为

$$
\ell(\boldsymbol{\mu}, \Sigma) = -\frac{np}{2}\log(2\pi) - \frac{n}{2}\log\det\Sigma - \frac{1}{2}\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu}).
$$

**定理 2.5.1（极大似然估计）** 设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的随机样本，$n > p$，则

$$
\hat{\boldsymbol{\mu}} = \bar{\boldsymbol{X}}, \qquad \hat\Sigma = \frac{1}{n}\sum_{j=1}^{n}(\boldsymbol{X}_j - \bar{\boldsymbol{X}})(\boldsymbol{X}_j - \bar{\boldsymbol{X}})^{\mathsf T} = \frac{n-1}{n}S
$$
分别是 $\boldsymbol{\mu}$ 与 $\Sigma$ 的极大似然估计量。它们的观测值 $\bar{\boldsymbol{x}}$ 与 $\frac{1}{n}\sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}$ 称为极大似然估计值。

**证明** 沿用一维的思路：令 $\ell$ 的导数为零，用 [3.4.1](/3.4.1) 的 1.8 节（分母布局）。对 $\boldsymbol{\mu}$，写 $(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu}) = \boldsymbol{z}^{\mathsf T}\Sigma^{-1}\boldsymbol{z}$，$\boldsymbol{z} = \boldsymbol{\mu} - \boldsymbol{x}_j$。由链式法则与性质 1.8.1，$\frac{\partial}{\partial\boldsymbol{\mu}}\boldsymbol{z}^{\mathsf T}\Sigma^{-1}\boldsymbol{z} = \frac{\partial\boldsymbol{z}}{\partial\boldsymbol{\mu}}\cdot 2\Sigma^{-1}\boldsymbol{z} = 2\Sigma^{-1}(\boldsymbol{\mu} - \boldsymbol{x}_j)$，故

$$
\frac{\partial\ell}{\partial\boldsymbol{\mu}} = -\Sigma^{-1}\sum_{j=1}^{n}(\boldsymbol{\mu} - \boldsymbol{x}_j) = \boldsymbol{0} \iff \hat{\boldsymbol{\mu}} = \frac{1}{n}\sum_{j=1}^{n}\boldsymbol{x}_j = \bar{\boldsymbol{x}},
$$
无论 $\Sigma$ 为何。对 $\Sigma$，把每个二次型写成迹，$(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu}) = \operatorname{tr}(\Sigma^{-1}B_j)$，$B_j = (\boldsymbol{x}_j - \boldsymbol{\mu})(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}$，并应用性质 1.8.2：

$$
\frac{\partial\ell}{\partial\Sigma} = -\frac{n}{2}\Sigma^{-1} + \frac{1}{2}\Sigma^{-1}\left(\sum_{j=1}^{n}B_j\right)\Sigma^{-1} = O \iff n\Sigma = \sum_{j=1}^{n}B_j.
$$
代入 $\hat{\boldsymbol{\mu}} = \bar{\boldsymbol{x}}$ 得 $\hat\Sigma = \frac{1}{n}\sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}$，$n > p$ 时它以概率一正定。这个驻点是全局最大值点，例如可由不等式 $\operatorname{tr}(\Sigma^{-1}B) + n\log\det\Sigma \ge np + n\log\det(B/n)$（$B$ 正定，等号仅在 $\Sigma = B/n$ 时成立）得到，取 $B = \sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}$。$\square$

代入估计值，$\sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}\hat\Sigma^{-1}(\boldsymbol{x}_j - \bar{\boldsymbol{x}}) = \operatorname{tr}(\hat\Sigma^{-1} \cdot n\hat\Sigma) = np$，所以似然函数的最大值为

$$
L(\hat{\boldsymbol{\mu}}, \hat\Sigma) = \frac{1}{(2\pi)^{np/2}}\mathrm{e}^{-np/2}\frac{1}{(\det\hat\Sigma)^{n/2}} \propto (\text{广义样本方差})^{-n/2}.
$$
这个值在 [3.4.3](/3.4.3) 的似然比检验中再次出现。由极大似然估计的不变性，函数 $h(\boldsymbol{\mu}, \Sigma)$ 的极大似然估计是 $h(\hat{\boldsymbol{\mu}}, \hat\Sigma)$：例如 $\boldsymbol{\mu}^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}$ 的极大似然估计是 $\hat{\boldsymbol{\mu}}^{\mathsf T}\hat\Sigma^{-1}\hat{\boldsymbol{\mu}}$，$\sqrt{\sigma_{kk}}$ 的极大似然估计是 $\sqrt{\hat\sigma_{kk}}$，其中 $\hat\sigma_{kk} = \frac{1}{n}\sum_j(x_{jk} - \bar x_k)^2$。

极大似然估计 $\hat\Sigma = S_n$ 是有偏的，$S$ 是它的无偏修正（定理 2.2.1）；$n$ 较大时二者差别可以忽略。

### 2.5.2. 充分统计量

**定理 2.5.2** 设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的随机样本，则 $(\bar{\boldsymbol{X}}, S)$ 是 $(\boldsymbol{\mu}, \Sigma)$ 的**充分统计量**。

**证明** 与定理 2.5.1 的证明一样，把似然的指数写成迹，并在 $\bar{\boldsymbol{x}}$ 处分解：

$$
\begin{aligned}
\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}_j - \boldsymbol{\mu}) &= \operatorname{tr}\left(\Sigma^{-1}\sum_{j=1}^{n}(\boldsymbol{x}_j - \boldsymbol{\mu})(\boldsymbol{x}_j - \boldsymbol{\mu})^{\mathsf T}\right) \\
&= \operatorname{tr}\left(\Sigma^{-1}\left[\sum_{j=1}^{n}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T} + n(\bar{\boldsymbol{x}} - \boldsymbol{\mu})(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}\right]\right) \\
&= (n-1)\operatorname{tr}(\Sigma^{-1}S) + n(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu}),
\end{aligned}
$$
其中交叉项因 $\sum_j(\boldsymbol{x}_j - \bar{\boldsymbol{x}}) = \boldsymbol{0}$ 而消失。于是

$$
L(\boldsymbol{\mu}, \Sigma) = \frac{1}{(2\pi)^{np/2}(\det\Sigma)^{n/2}}\exp\left\{-\frac{n-1}{2}\operatorname{tr}(\Sigma^{-1}S) - \frac{n}{2}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\bar{\boldsymbol{x}} - \boldsymbol{\mu})\right\}
$$
只通过 $\bar{\boldsymbol{x}}$ 与 $S$ 依赖于数据，由**因子分解定理**即得充分性。$\square$

因此对正态总体，无论样本量多大，样本中关于参数的全部信息都由 $\bar{\boldsymbol{X}}$ 与 $S$ 承载：数据矩阵可以压缩为 $p + p(p+1)/2$ 个数。对非正态总体这不成立，$\bar{\boldsymbol{X}}$ 与 $S$ 可能遗漏重要信息；所以凡是基于这些统计量的分析，都要检查正态性假定。充分统计量的抽样分布是 [3.4.3](/3.4.3) 的主题。

## 小结

- 矩阵形式的描述统计量：$\bar{\boldsymbol{x}} = \frac{1}{n}X^{\mathsf T}\boldsymbol{1}_n$，$(n-1)S = X^{\mathsf T}HX$，其中中心化矩阵 $H = I_n - \frac{1}{n}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$，$R = D^{-1/2}SD^{-1/2}$。几何上（各列看作 $\mathbb{R}^n$ 中的向量）：均值 = 在 $\boldsymbol{1}_n$ 上的投影，方差 $\propto$ 离差向量长度的平方，相关系数 = 夹角的余弦。
- 广义样本方差 $\det S = \lambda_1\cdots\lambda_p = (n-1)^{-p}(\text{体积})^2$；它为零当且仅当变量的某个线性组合是常数（$n \le p$ 时总是如此），且它不反映方向。
- 不需要分布假定：$\mathbb{E}\bar{\boldsymbol{X}} = \boldsymbol{\mu}$，$\operatorname{Cov}(\bar{\boldsymbol{X}}) = \Sigma/n$，$\mathbb{E}S = \Sigma$；线性组合 $A\boldsymbol{x}_j$ 的样本均值为 $A\bar{\boldsymbol{x}}$、样本协方差为 $ASA^{\mathsf T}$，与 $A\boldsymbol{\mu}$、$A\Sigma A^{\mathsf T}$ 对应。
- $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$：密度的指数中是马氏距离的平方；等高线是以 $\boldsymbol{\mu}$ 为中心、轴为 $\pm c\sqrt{\lambda_i}\boldsymbol{e}_i$ 的椭球；$\boldsymbol{\mu} + \Sigma^{1/2}\boldsymbol{Z}$，$\boldsymbol{Z}$ 的分量独立且服从标准正态分布。
- 性质：对一切 $\boldsymbol{a}$，$\boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ 正态（等价定义）；$A\boldsymbol{X} \sim \mathcal{N}(A\boldsymbol{\mu}, A\Sigma A^{\mathsf T})$；边缘分布正态；联合正态下独立 $\iff \Sigma_{12} = O$；$\boldsymbol{X}_1 \mid \boldsymbol{x}_2 \sim \mathcal{N}(\boldsymbol{\mu}_1 + \Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{x}_2 - \boldsymbol{\mu}_2), \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21})$；$(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_p$；$\boldsymbol{b}^{\mathsf T}\boldsymbol{c} = 0$ 时 $\sum c_j\boldsymbol{X}_j$ 与 $\sum b_j\boldsymbol{X}_j$ 独立。
- 正态假定下：极大似然估计为 $\bar{\boldsymbol{X}}$ 与 $\frac{n-1}{n}S$，似然的最大值与 $(\det\hat\Sigma)^{-n/2}$ 成正比，$(\bar{\boldsymbol{X}}, S)$ 是充分统计量。
