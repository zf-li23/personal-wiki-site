---
title: 矩阵方法与多元线性回归
description: 矩阵形式的简单线性回归，用微积分和向列空间作正交投影两种方式推导最小二乘，估计的抽样分布；多元线性回归模型及其参数与特例，Gauss–Markov 定理，帽子矩阵与杠杆值，以及含整体 F 检验、R² 与调整 R² 的方差分析。
source_hash: 2503e4d86094
---

只有一个预测变量时，前几章的每个公式都能用求和写出来。预测变量多了，这样写就难以驾驭，自然的语言是向量和矩阵：数据构成响应向量和设计矩阵，最小二乘成为正交投影，所有平方和都成为二次型。本章先用这种语言重写简单线性回归（[3.3.2](/3.3.2)–[3.3.4](/3.3.4)），除了记号之外没有任何新东西；然后让设计矩阵有更多的列，这就是多元线性回归模型。我们用解析和几何两种方法推导最小二乘估计，给出其抽样分布、Gauss–Markov 定理、帽子矩阵的性质（它解释了 [3.3.5](/3.3.5) 与 [3.3.6](/3.3.6) 中用到的杠杆值与残差方差），以及整个模型的方差分析、$R^2$ 与调整 $R^2$。对单个系数和系数组的推断见 [3.3.8](/3.3.8) 与 [3.3.9](/3.3.9)。线性代数取自 [2.1](/2.1)，分布理论取自 [3.1.15](/3.1.15)；[3.4.7](/3.4.7) 从多元统计的角度讨论了同一模型。

## 7.1. 矩阵形式的简单线性回归

### 7.1.1. 工具：多元正态分布与二次型

先汇集本章用到的事实。对均值向量为 $\boldsymbol{\mu}$ 的随机向量 $\boldsymbol{Z}$，**协方差矩阵** $\operatorname{Cov}(\boldsymbol{Z}) = \mathbb{E}\big[(\boldsymbol{Z} - \boldsymbol{\mu})(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\big]$（[3.1.10](/3.1.10)）对分块的 $\boldsymbol{Z}$ 有分块 $\operatorname{Cov}(\boldsymbol{Z}_1)$、$\operatorname{Cov}(\boldsymbol{Z}_1, \boldsymbol{Z}_2)$ 等，并且对常数矩阵 $A$ 与常数向量 $\boldsymbol{c}$，

$$
\mathbb{E}(A\boldsymbol{Z} + \boldsymbol{c}) = A\boldsymbol{\mu} + \boldsymbol{c}, \qquad \operatorname{Cov}(A\boldsymbol{Z} + \boldsymbol{c}) = \mathbb{E}\big[A(\boldsymbol{Z} - \boldsymbol{\mu})(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}A^{\mathsf T}\big] = A\operatorname{Cov}(\boldsymbol{Z})A^{\mathsf T}.
$$

**定理 7.1.1（多元正态分布的性质）** 设 $n \times 1$ 随机向量 $\boldsymbol{Z}$ 服从**多元正态分布** $\mathcal{N}_n(\boldsymbol{\mu}, \Sigma)$（[3.1.15](/3.1.15)）。

1. (N1) 正态向量的线性变换仍是正态的：对任意常数 $d \times n$ 矩阵 $A$ 与 $\boldsymbol{c} \in \mathbb{R}^d$，$A\boldsymbol{Z} + \boldsymbol{c} \sim \mathcal{N}(A\boldsymbol{\mu} + \boldsymbol{c}, A\Sigma A^{\mathsf T})$。
2. (N2) 给定一阶矩和二阶矩，即均值向量和协方差矩阵，正态分布就确定了。
3. (N3) 若 $\boldsymbol{Z} = \begin{bmatrix}\boldsymbol{Z}_1\\\boldsymbol{Z}_2\end{bmatrix}$ 是正态的，且 $\boldsymbol{Z}_1$ 与 $\boldsymbol{Z}_2$ 不相关，$\operatorname{Cov}(\boldsymbol{Z}_1, \boldsymbol{Z}_2) = O$，则 $\boldsymbol{Z}_1$ 与 $\boldsymbol{Z}_2$ 独立；对 $k$ 个分块同样成立。
4. (N4) $\boldsymbol{W}_1 = A_1\boldsymbol{Z}$ 与 $\boldsymbol{W}_2 = A_2\boldsymbol{Z}$ 独立当且仅当 $A_1\Sigma A_2^{\mathsf T} = O$。若 $\Sigma = \sigma^2I_n$，条件为 $A_1A_2^{\mathsf T} = O$。
5. (N5) 若 $\boldsymbol{W}_i = A_i\boldsymbol{Z}$，$i = 1, \dots, k$，且对 $1 \le i < j \le k$ 有 $\operatorname{Cov}(\boldsymbol{W}_i, \boldsymbol{W}_j) = O$，则长度平方 $\boldsymbol{W}_1^{\mathsf T}\boldsymbol{W}_1, \dots, \boldsymbol{W}_k^{\mathsf T}\boldsymbol{W}_k$ 相互独立。
6. (N6) 若 $\Sigma$ 非奇异，则 $(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{Z} - \boldsymbol{\mu}) \sim \chi^2_n$。若 $\Sigma$ 奇异、秩为 $r < n$，$\Sigma^-$ 是 $\Sigma$ 的广义逆（满足 $\Sigma\Sigma^-\Sigma = \Sigma$ 的任一矩阵，不唯一），则 $(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\Sigma^-(\boldsymbol{Z} - \boldsymbol{\mu}) \sim \chi^2_r$。

(N1)–(N4) 在 [3.1.15](/3.1.15) 中已经证明（由 (N1)，堆叠向量 $(\boldsymbol{W}_1, \boldsymbol{W}_2) = \begin{bmatrix}A_1\\A_2\end{bmatrix}\boldsymbol{Z}$ 是正态的，其协方差的非对角块为 $A_1\Sigma A_2^{\mathsf T}$，于是 (N4) 由 (N3) 推出）；(N5) 由 (N3) 推出，因为独立向量的函数仍独立，这正是平方和之间相互独立的来源。对 (N6)，$\Sigma^{-1/2}(\boldsymbol{Z} - \boldsymbol{\mu}) \sim \mathcal{N}(\boldsymbol{0}, I_n)$ 是 $\boldsymbol{Z}$ 的标准化，二次型就是它的长度平方；奇异情形下 $\boldsymbol{Z} - \boldsymbol{\mu}$ 的可能取值只占据 $\mathbb{R}^n$ 的一个 $r$ 维子空间。

**引理 7.1.1** $n$ 阶方阵 $A$ 幂等（$A^2 = A$）当且仅当 $\operatorname{rank}(A) + \operatorname{rank}(I_n - A) = n$。

**证明** 任一 $\boldsymbol{x} \in \mathbb{R}^n$ 都有 $\boldsymbol{x} = A\boldsymbol{x} + (I_n - A)\boldsymbol{x}$，所以 $\mathbb{R}^n = \mathcal{R}(A) + \mathcal{R}(I_n - A)$，两个秩之和总不小于 $n$。若 $A^2 = A$，则 $A(I_n - A) = O$，于是 $\mathcal{R}(I_n - A) \subseteq \mathcal{N}(A)$；反之 $A\boldsymbol{x} = \boldsymbol{0}$ 蕴含 $\boldsymbol{x} = (I_n - A)\boldsymbol{x}$。因此 $\mathcal{R}(I_n - A) = \mathcal{N}(A)$，其维数为 $n - \operatorname{rank}(A)$。若两个秩之和为 $n$，则和 $\mathcal{R}(A) + \mathcal{R}(I_n - A)$ 是直和，$\mathcal{R}(A) \cap \mathcal{R}(I_n - A) = \{\boldsymbol{0}\}$；向量 $(A - A^2)\boldsymbol{x} = A(I_n - A)\boldsymbol{x} = (I_n - A)A\boldsymbol{x}$ 同时属于二者，所以对每个 $\boldsymbol{x}$ 都为 $\boldsymbol{0}$，即 $A^2 = A$。$\square$

**定理 7.1.2（二次型的期望）** 设随机向量 $\boldsymbol{Z}$ 的均值为 $\boldsymbol{\mu}$、协方差矩阵为 $\Sigma$，$A$ 是常数方阵，则

$$
\mathbb{E}(\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}) = \operatorname{tr}(A\Sigma) + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}.
$$

**证明**（迹技巧）在 $\boldsymbol{\mu}$ 处展开，线性项的期望为零；一个数等于它自身的迹，$\operatorname{tr}(\boldsymbol{u}^{\mathsf T}A\boldsymbol{u}) = \operatorname{tr}(A\boldsymbol{u}\boldsymbol{u}^{\mathsf T})$：

$$
\begin{aligned}
\mathbb{E}(\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}) &= \mathbb{E}\big[(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}A(\boldsymbol{Z} - \boldsymbol{\mu})\big] + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu} = \operatorname{tr}\big\{\mathbb{E}\big[A(\boldsymbol{Z} - \boldsymbol{\mu})(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\big]\big\} + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu} \\
&= \operatorname{tr}\big\{A\,\mathbb{E}\big[(\boldsymbol{Z} - \boldsymbol{\mu})(\boldsymbol{Z} - \boldsymbol{\mu})^{\mathsf T}\big]\big\} + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu} = \operatorname{tr}(A\Sigma) + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}. \qquad \square
\end{aligned}
$$
这个定理只需要一阶矩和二阶矩，不需要正态性。

**例 7.1.1（等相关变量）** 设 $X_1, \dots, X_n$ 的均值为 $0$、方差为 $1$、两两相关系数为 $\rho$，$Y = a_1X_1 + \cdots + a_nX_n = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$。则 $\mathbb{E}(Y) = \boldsymbol{a}^{\mathsf T}\mathbb{E}(\boldsymbol{X}) = 0$，$\operatorname{Var}(Y) = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}$，其中 $\Sigma = (1 - \rho)I_n + \rho\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$，$\boldsymbol{1}_n$ 是全 1 向量。$\rho$ 最小能是多少？协方差矩阵是半正定的，而 $\Sigma$ 的特征值为 $1 + (n - 1)\rho$（特征向量 $\boldsymbol{1}_n$）和 $1 - \rho$（在 $\boldsymbol{1}_n$ 的正交补上，重数 $n - 1$）。因此 $\rho \ge -1/(n - 1)$，且最小值 $\rho = -1/(n - 1)$ 可以取到，例如取 $X_i = \sqrt{n/(n - 1)}\,(U_i - \bar U)$，其中 $U_1, \dots, U_n$ 独立同分布、方差为 $1$；这时 $Y = \boldsymbol{1}_n^{\mathsf T}\boldsymbol{X}$ 的方差为 $0$。

### 7.1.2. 矩阵形式的模型

简单线性回归模型 $Y_i = \beta_0 + \beta_1X_i + \varepsilon_i$（误差独立、正态、均值 $0$、方差 $\sigma^2$）由 $n$ 个方程组成：

$$
Y_1 = \beta_0 + \beta_1X_1 + \varepsilon_1, \quad Y_2 = \beta_0 + \beta_1X_2 + \varepsilon_2, \quad \dots, \quad Y_n = \beta_0 + \beta_1X_n + \varepsilon_n,
$$
即

$$
\begin{bmatrix}Y_1\\Y_2\\\vdots\\Y_n\end{bmatrix} = \begin{bmatrix}\beta_0 + \beta_1X_1\\\beta_0 + \beta_1X_2\\\vdots\\\beta_0 + \beta_1X_n\end{bmatrix} + \begin{bmatrix}\varepsilon_1\\\varepsilon_2\\\vdots\\\varepsilon_n\end{bmatrix} = \begin{bmatrix}1 & X_1\\1 & X_2\\\vdots & \vdots\\1 & X_n\end{bmatrix}\begin{bmatrix}\beta_0\\\beta_1\end{bmatrix} + \begin{bmatrix}\varepsilon_1\\\varepsilon_2\\\vdots\\\varepsilon_n\end{bmatrix}.
$$
写成矩阵形式，

$$
\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon},
$$
其中响应向量 $\boldsymbol{Y} = (Y_1, \dots, Y_n)^{\mathsf T}$，$n \times 2$ 的**设计矩阵** $X$ 的各行为 $(1, X_i)$，参数（系数）向量 $\boldsymbol{\beta} = (\beta_0, \beta_1)^{\mathsf T}$，误差向量 $\boldsymbol{\varepsilon} = (\varepsilon_1, \dots, \varepsilon_n)^{\mathsf T}$。

由于误差独立且方差相同，其协方差矩阵为

$$
\operatorname{Cov}(\boldsymbol{\varepsilon}) = \operatorname{Cov}\begin{bmatrix}\varepsilon_1\\\vdots\\\varepsilon_n\end{bmatrix} = \sigma^2I_n:
$$
任意两个误差项的协方差为零，对角元都等于 $\sigma^2$。由于设计矩阵是固定的，$X\boldsymbol{\beta}$ 是常数向量，所以 $\boldsymbol{Y}$ 与 $\boldsymbol{\varepsilon}$ 有相同的协方差矩阵 $\operatorname{Cov}(\boldsymbol{Y}) = \sigma^2I_n$。分布模型为

$$
\boldsymbol{Y} \sim \mathcal{N}_n(X\boldsymbol{\beta}, \sigma^2I_n).
$$

### 7.1.3. 最小二乘：解析方法

最小二乘准则为

$$
Q(\boldsymbol{\beta}) = \|\boldsymbol{Y} - X\boldsymbol{\beta}\|^2 = (\boldsymbol{Y} - X\boldsymbol{\beta})^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{\beta}), \qquad \hat{\boldsymbol{\beta}} = \arg\min_{\boldsymbol{\beta} \in \mathbb{R}^2}Q(\boldsymbol{\beta}).
$$
它的梯度和 Hesse 矩阵为

$$
\frac{\partial Q}{\partial\boldsymbol{\beta}} = -2X^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{\beta}), \qquad \frac{\partial^2Q}{\partial\boldsymbol{\beta}\,\partial\boldsymbol{\beta}^{\mathsf T}} = 2X^{\mathsf T}X.
$$
令梯度为零，得**正规方程** $X^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{\beta}) = \boldsymbol{0}$，即 $X^{\mathsf T}X\boldsymbol{\beta} = X^{\mathsf T}\boldsymbol{Y}$。Hesse 矩阵半正定，且恰在 $\operatorname{rank}(X) = 2$（各 $X_i$ 不全相等）时正定。在这一条件下 $Q$ 的最小点存在且唯一：

$$
\boldsymbol{b} = \hat{\boldsymbol{\beta}} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$
具体地，

$$
X^{\mathsf T}X = \begin{bmatrix}n & \sum X_i\\\sum X_i & \sum X_i^2\end{bmatrix}, \qquad (X^{\mathsf T}X)^{-1} = \frac{1}{n\sum X_i^2 - (\sum X_i)^2}\begin{bmatrix}\sum X_i^2 & -\sum X_i\\-\sum X_i & n\end{bmatrix}, \qquad X^{\mathsf T}\boldsymbol{Y} = \begin{bmatrix}\sum Y_i\\\sum X_iY_i\end{bmatrix},
$$
乘出来就得到 [3.3.2](/3.3.2) 的 $b_1 = \sum(X_i - \bar X)(Y_i - \bar Y)/\sum(X_i - \bar X)^2$ 与 $b_0 = \bar Y - b_1\bar X$，因为 $n\sum X_i^2 - (\sum X_i)^2 = n\sum(X_i - \bar X)^2$。

拟合（预测）响应向量与残差向量为

$$
\hat{\boldsymbol{Y}} = X\boldsymbol{b} = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y} = H\boldsymbol{Y}, \qquad \boldsymbol{e} = \boldsymbol{Y} - \hat{\boldsymbol{Y}} = \boldsymbol{Y} - H\boldsymbol{Y} = (I_n - H)\boldsymbol{Y},
$$
其中 $H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$ 是 7.3 节的帽子矩阵（投影矩阵）。

### 7.1.4. 最小二乘：几何方法

按列写出设计矩阵，$X = [\boldsymbol{1}_n \mid \boldsymbol{x}]$，$\boldsymbol{x} = (X_1, \dots, X_n)^{\mathsf T}$。于是

$$
\hat{\boldsymbol{Y}} = X\boldsymbol{b} = b_0\boldsymbol{1}_n + b_1\boldsymbol{x}
$$
是 $X$ 各列的线性组合：它属于**列空间** $\mathcal{R}(X)$（也记作 $C(X)$ 或 $\operatorname{Im}X$），即 $X$ 的各列在 $\mathbb{R}^n$ 中张成的子空间。$n \times p$ 矩阵把 $\mathbb{R}^p$ 映到 $\mathbb{R}^n$，$\boldsymbol{\beta} \mapsto X\boldsymbol{\beta}$；有 $n = 3$ 个观测、$p = 2$ 列时，$X$ 把系数向量所在的平面 $\mathbb{R}^2$ 映成 $\mathbb{R}^3$ 中一个过原点的平面。

$n \times p$、秩为 $r$ 的矩阵 $A$ 的四个基本子空间（[2.1.3](/2.1.3)、[2.1.4](/2.1.4)）组织起这幅图景：

| 子空间 | 所在空间 | 维数 | 正交补 |
|---|---|---|---|
| 列空间 $\mathcal{R}(A)$ | $\mathbb{R}^n$ | $r$ | 左零空间 $\mathcal{N}(A^{\mathsf T})$，维数 $n - r$ |
| 行空间 $\mathcal{R}(A^{\mathsf T})$ | $\mathbb{R}^p$ | $r$ | 零空间 $\mathcal{N}(A)$，维数 $p - r$ |

$A$ 把 $\mathbb{R}^p$ 映满 $\mathcal{R}(A)$，$A^{\mathsf T}$ 把 $\mathbb{R}^n$ 映满 $\mathcal{R}(A^{\mathsf T})$；$\mathbb{R}^n$ 中每个向量都是 $\mathcal{R}(A)$ 中的一个向量与 $\mathcal{N}(A^{\mathsf T})$ 中一个与之正交的向量之和。

因此最小二乘问题可以改写为

$$
\min_{\boldsymbol{\beta} \in \mathbb{R}^2}\|\boldsymbol{Y} - X\boldsymbol{\beta}\|^2 = \min_{\boldsymbol{v} = X\boldsymbol{\beta}}\|\boldsymbol{Y} - \boldsymbol{v}\|^2 = \min_{\boldsymbol{v} \in \mathcal{R}(X)}\|\boldsymbol{Y} - \boldsymbol{v}\|^2,
$$
即在列空间中找离 $\boldsymbol{Y}$ 最近的点。由最佳逼近定理（[2.1.4](/2.1.4)），最小点是 $\boldsymbol{Y}$ 在 $\mathcal{R}(X)$ 上的**正交投影** $\hat{\boldsymbol{Y}} = P\boldsymbol{Y}$，$P$ 是到 $\mathcal{R}(X)$ 的**正交投影矩阵**；由勾股定理，$\mathcal{R}(X)$ 中其他任何 $\boldsymbol{v}$ 都离 $\boldsymbol{Y}$ 更远。残差与列空间正交，$\boldsymbol{e} \in \mathcal{N}(X^{\mathsf T})$：

$$
X^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{b}) = X^{\mathsf T}\boldsymbol{e} = \boldsymbol{0}, \qquad\text{即}\qquad \boldsymbol{1}_n^{\mathsf T}\boldsymbol{e} = 0, \quad \boldsymbol{x}^{\mathsf T}\boldsymbol{e} = 0.
$$
这又是正规方程，每列一个，由它们得到 $\boldsymbol{b} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ 与

$$
P\boldsymbol{Y} = X\boldsymbol{b} = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}, \qquad P = H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}.
$$
投影矩阵对称且幂等（$P^2 = P$），残差与拟合值正交，$\boldsymbol{e}^{\mathsf T}\hat{\boldsymbol{Y}} = 0$，而 $\boldsymbol{1}_n^{\mathsf T}\boldsymbol{e} = 0$ 说明残差之和为零。（$n = 3$ 时投影的示意图见 [3.4.7](/3.4.7)。）

### 7.1.5. 抽样分布

**定理 7.1.3** 在简单线性回归模型中，$\boldsymbol{b} \sim \mathcal{N}_2\big(\boldsymbol{\beta}, \sigma^2(X^{\mathsf T}X)^{-1}\big)$。$\boldsymbol{b}$ 的协方差矩阵的估计为

$$
s^2\{\boldsymbol{b}\} = s^2(X^{\mathsf T}X)^{-1}, \qquad s^2 = \frac{\boldsymbol{e}^{\mathsf T}\boldsymbol{e}}{n - 2} = \frac{\boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}}{n - 2}.
$$

**证明** $\boldsymbol{Y} \sim \mathcal{N}_n(X\boldsymbol{\beta}, \sigma^2I_n)$，$\boldsymbol{b} = D\boldsymbol{Y}$，$D = (X^{\mathsf T}X)^{-1}X^{\mathsf T}$。由 (N1)，$\boldsymbol{b}$ 是正态的，均值为 $DX\boldsymbol{\beta} = \boldsymbol{\beta}$，协方差为 $\sigma^2DD^{\mathsf T} = \sigma^2(X^{\mathsf T}X)^{-1}X^{\mathsf T}X(X^{\mathsf T}X)^{-1} = \sigma^2(X^{\mathsf T}X)^{-1}$。$\boldsymbol{e}^{\mathsf T}\boldsymbol{e} = \boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}$ 由 $(I_n - H)^{\mathsf T}(I_n - H) = I_n - H$ 推出。$\square$

利用上面算出的逆矩阵，$\sigma^2(X^{\mathsf T}X)^{-1}$ 的元素就是 [3.3.3](/3.3.3) 中熟悉的公式：

$$
\operatorname{Var}(b_0) = \sigma^2\left[\frac1n + \frac{\bar X^2}{\sum(X_i - \bar X)^2}\right], \qquad \operatorname{Var}(b_1) = \frac{\sigma^2}{\sum(X_i - \bar X)^2}, \qquad \operatorname{Cov}(b_0, b_1) = -\frac{\bar X\sigma^2}{\sum(X_i - \bar X)^2}.
$$

这一框架不加改动地延伸到多元回归：增加一个解释变量，就是在设计矩阵 $X$ 中增加一列。

## 7.2. 多元线性回归模型

### 7.2.1. 数据与记号

个体仍记为 $i = 1, \dots, n$；数据为

$$
\{(Y_i;\ X_{i1}, X_{i2}, \dots, X_{i,p-1})\}_{1 \le i \le n},
$$
其中 $Y_i$ 是第 $i$ 个个体的响应，$X_{i1}, \dots, X_{i,p-1}$ 是它的 $p - 1$ 个解释（预测）变量的值。在整门课程中，$p$ 表示包括截距在内的回归参数的个数，因此有 $p - 1$ 个预测变量，简单线性回归中 $p = 2$。（这与 [3.4.7](/3.4.7) 一致；[3.2.3](/3.2.3) 中的 $p$ 只计预测变量。）设计矩阵

$$
X = \begin{bmatrix}1 & X_{11} & X_{12} & \cdots & X_{1,p-1}\\1 & X_{21} & X_{22} & \cdots & X_{2,p-1}\\\vdots & \vdots & \vdots & & \vdots\\1 & X_{n1} & X_{n2} & \cdots & X_{n,p-1}\end{bmatrix} = \big[\boldsymbol{1}_n \mid \boldsymbol{x}_1 \mid \cdots \mid \boldsymbol{x}_{p-1}\big] = \begin{bmatrix}\boldsymbol{x}_{(1)}^{\mathsf T}\\\boldsymbol{x}_{(2)}^{\mathsf T}\\\vdots\\\boldsymbol{x}_{(n)}^{\mathsf T}\end{bmatrix}
$$
可以按列读，$\boldsymbol{x}_k = (X_{1k}, \dots, X_{nk})^{\mathsf T}$ 是第 $k$ 个预测变量的取值；也可以按行读，$\boldsymbol{x}_{(i)}^{\mathsf T} = (1, X_{i1}, \dots, X_{i,p-1})$ 是第 $i$ 个个体。

### 7.2.2. 模型及其参数

**定义 7.2.1（多元线性回归模型）** **多元线性回归模型**为

$$
Y_i = \beta_0 + \beta_1X_{i1} + \beta_2X_{i2} + \cdots + \beta_{p-1}X_{i,p-1} + \varepsilon_i, \qquad i = 1, \dots, n,
$$
其中 $\varepsilon_1, \dots, \varepsilon_n$ 是相互独立的正态随机误差，均值为 $0$，方差为 $\sigma^2$。记 $\boldsymbol{Y} = (Y_1, \dots, Y_n)^{\mathsf T}$、$n \times p$ 设计矩阵 $X$、$\boldsymbol{\beta} = (\beta_0, \beta_1, \dots, \beta_{p-1})^{\mathsf T}$ 与 $\boldsymbol{\varepsilon} = (\varepsilon_1, \dots, \varepsilon_n)^{\mathsf T}$，矩阵形式为

$$
\boldsymbol{Y}_{n\times1} = X_{n\times p}\boldsymbol{\beta}_{p\times1} + \boldsymbol{\varepsilon}_{n\times1}, \qquad \boldsymbol{\varepsilon} \sim \mathcal{N}_n(\boldsymbol{0}, \sigma^2I_n), \qquad \boldsymbol{Y} \sim \mathcal{N}_n(X\boldsymbol{\beta}, \sigma^2I_n).
$$

参数是截距 $\beta_0$、各解释变量的回归系数 $\beta_1, \dots, \beta_{p-1}$ 以及误差方差 $\sigma^2$。注意术语从"斜率"换成了"回归系数"。

**定义 7.2.2（偏回归系数）** 在多元线性回归模型中，$\beta_k$（$1 \le k \le p - 1$）是其他预测变量 $X_1, \dots, X_{k-1}, X_{k+1}, \dots, X_{p-1}$ 保持不变时，$X_k$ 每增加一个单位平均响应 $\mathbb{E}(Y)$ 的变化。因此各 $\beta_k$ 也称为**偏回归系数**：它们反映其他预测变量都在模型中且保持不变时，一个预测变量的偏效应。

偏回归系数一般不同于 $Y$ 只对 $X_k$ 作简单回归的斜率，后者还吸收了与 $X_k$ 相关的预测变量的效应；预测变量加入或移出模型时，偏回归系数也会改变。它的解释还要求所考虑的预测变量取值组合位于模型的适用范围之内，即数据共同覆盖的预测变量取值区域：预测变量相关时，固定一个而改变另一个可能会走出这个区域。

### 7.2.3. 特例

模型关于参数是线性的，预测变量可以是原始变量的函数。几种重要的模型都是它的特例。

- $p - 1$ 阶多项式模型$Y_i = \beta_0 + \beta_1X_i + \beta_2X_i^2 + \cdots + \beta_{p-1}X_i^{p-1} + \varepsilon_i$ 以一个变量的各次幂为预测变量。
- 解释变量之间的交互作用可以用它们的乘积（交叉项）表示并放进模型。
- 有些解释变量可以是指示变量。虚拟变量（dummy variable）是取值 $0$ 与 $1$（或其他不同数值）、用来编码定性变量各类别的预测变量。

这些模型在 [3.3.10](/3.3.10) 中展开；下面一个例子说明单个线性模型能表达多少内容。

**例 7.2.1（儿童身高）** 响应是身高 $Y$，两个解释变量是以月计的年龄 $X_1$ 和性别 $X_2$，后者是虚拟变量，女孩 $X_2 = 0$，男孩 $X_2 = 1$。考虑

$$
Y_i = \beta_0 + \beta_1X_{i1} + \beta_2X_{i2} + \beta_3X_{i1}X_{i2} + \varepsilon_i.
$$
若第 $i$ 个儿童是女孩（$X_{i2} = 0$），$Y_i = \beta_0 + \beta_1X_{i1} + \varepsilon_i$；若是男孩（$X_{i2} = 1$），$Y_i = (\beta_0 + \beta_2) + (\beta_1 + \beta_3)X_{i1} + \varepsilon_i$。一个模型表示了女孩和男孩各自的 $Y$ 对 $X_1$ 的两条不同的回归直线：$\beta_2$ 是截距之差，交互项的系数 $\beta_3$ 是斜率之差。

![Simulated heights of 40 girls and 40 boys against age in months, with the two regression lines given by a single model with a gender dummy variable and an age-by-gender interaction](./plots/dummy-interaction.py)

## 7.3. 估计

### 7.3.1. 最小二乘

解析方法与 7.1 节相同：在 $\boldsymbol{\beta} \in \mathbb{R}^p$ 上最小化 $Q(\boldsymbol{\beta}) = \|\boldsymbol{Y} - X\boldsymbol{\beta}\|^2$，得到正规方程 $X^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{\beta}) = \boldsymbol{0}$，Hesse 矩阵为 $2X^{\mathsf T}X$。在 $\operatorname{rank}(X) = p$（$X$ 的各列线性无关）的条件下，最小点存在且唯一，

$$
\boldsymbol{b} = \hat{\boldsymbol{\beta}} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$
几何上，$\hat{\boldsymbol{Y}} = X\boldsymbol{b} = b_0\boldsymbol{1}_n + b_1\boldsymbol{x}_1 + \cdots + b_{p-1}\boldsymbol{x}_{p-1}$ 是 $\boldsymbol{Y}$ 在 $p$ 维列空间 $\mathcal{R}(X) \subseteq \mathbb{R}^n$ 上的正交投影，残差 $\boldsymbol{e}$ 与每一列都正交。

**定义 7.3.1（帽子矩阵）** $n \times n$ 矩阵

$$
H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}
$$
称为**帽子矩阵**（也称投影矩阵或影响矩阵），因为它把响应映为拟合值，$\hat{\boldsymbol{Y}} = X\boldsymbol{b} = H\boldsymbol{Y}$；残差为 $\boldsymbol{e} = \boldsymbol{Y} - \hat{\boldsymbol{Y}} = (I_n - H)\boldsymbol{Y}$。

可以直接验证 $H$ 对称且幂等，$H^{\mathsf T} = H = H^2$，并且 $HX = X$，$(I_n - H)X = O$；所以 $H$ 是到 $\mathcal{R}(X)$ 的正交投影矩阵，$I_n - H$ 是到其正交补的正交投影矩阵。于是残差与拟合值正交，$\boldsymbol{e}^{\mathsf T}\hat{\boldsymbol{Y}} = \boldsymbol{Y}^{\mathsf T}(I_n - H)H\boldsymbol{Y} = 0$，残差的自由度为 $\mathrm{df}_E = \operatorname{rank}(I_n - H) = n - p$（7.3.3 节）。

误差平方和、其自由度与均方误差为

$$
\mathrm{SSE} = \boldsymbol{e}^{\mathsf T}\boldsymbol{e} = (\boldsymbol{Y} - X\boldsymbol{b})^{\mathsf T}(\boldsymbol{Y} - X\boldsymbol{b}) = \boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}, \qquad \mathrm{df}_E = n - p, \qquad \mathrm{MSE} = \frac{\mathrm{SSE}}{\mathrm{df}_E} = \frac{\boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}}{n - p},
$$
$\sigma^2$ 与 $\sigma$ 的估计量为 $s^2 = \mathrm{MSE}$ 与 $s = \sqrt{\mathrm{MSE}}$。

**定理 7.3.1（抽样分布）** 在 $\operatorname{rank}(X) = p$ 的多元线性回归模型中：

1. $\boldsymbol{b} \sim \mathcal{N}_p\big(\boldsymbol{\beta}, \sigma^2(X^{\mathsf T}X)^{-1}\big)$：$\boldsymbol{b}$ 无偏，$\mathbb{E}(\boldsymbol{b}) = \boldsymbol{\beta}$，协方差矩阵 $\operatorname{Cov}(\boldsymbol{b}) = \sigma^2(X^{\mathsf T}X)^{-1}$ 的估计为 $s^2\{\boldsymbol{b}\} = \mathrm{MSE}\,(X^{\mathsf T}X)^{-1}$；
2. $\boldsymbol{e} \sim \mathcal{N}_n\big(\boldsymbol{0}, \sigma^2(I_n - H)\big)$，且 $\boldsymbol{e}$ 与 $\boldsymbol{b}$ 独立；
3. $\mathrm{SSE}/\sigma^2 \sim \chi^2_{n-p}$，且与 $\boldsymbol{b}$ 独立；特别地 $\mathbb{E}(\mathrm{MSE}) = \sigma^2$。

**证明** (1) 的证明与定理 7.1.3 完全相同。对 (2)，由于 $(I_n - H)X = O$，$\boldsymbol{e} = (I_n - H)\boldsymbol{Y} = (I_n - H)\boldsymbol{\varepsilon}$，由 (N1) 它是正态的，均值为 $\boldsymbol{0}$，协方差为 $\sigma^2(I_n - H)(I_n - H)^{\mathsf T} = \sigma^2(I_n - H)$。对 $\boldsymbol{b} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$，条件 (N4) 成立：由 $X^{\mathsf T}H = X^{\mathsf T}$ 得 $(X^{\mathsf T}X)^{-1}X^{\mathsf T}(I_n - H) = O$。对 (3)，把秩为 $n - p$ 的对称幂等矩阵写成 $I_n - H = QQ^{\mathsf T}$，$Q \in \mathbb{R}^{n\times(n-p)}$ 的列标准正交。则 $Q^{\mathsf T}\boldsymbol{\varepsilon}/\sigma \sim \mathcal{N}_{n-p}(\boldsymbol{0}, I_{n-p})$，$\mathrm{SSE}/\sigma^2 = \boldsymbol{\varepsilon}^{\mathsf T}(I_n - H)\boldsymbol{\varepsilon}/\sigma^2 = \|Q^{\mathsf T}\boldsymbol{\varepsilon}/\sigma\|^2 \sim \chi^2_{n-p}$；它是 $\boldsymbol{e}$ 的函数，所以与 $\boldsymbol{b}$ 独立。$\square$

### 7.3.2. Gauss–Markov 定理

定理 7.3.1 给出了 $\boldsymbol{b}$ 的协方差矩阵；它在什么意义下是最优的？回答只需要关于一阶矩和二阶矩的假设。Gauss–Markov 条件是：

1. 线性：模型关于参数是线性的，$\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$。
2. 随机性：数据是从总体中随机抽取的，因而不同个体的误差不相关。
3. 无完全共线性：各回归变量之间不完全相关，$\operatorname{rank}(X) = p$。
4. 外生性：回归变量与误差项不相关，$\mathbb{E}(\boldsymbol{\varepsilon} \mid X) = \boldsymbol{0}$。
5. 同方差性：无论回归变量取什么值，误差的方差都恒定。

条件 2、4、5 合起来就是 $\mathbb{E}(\boldsymbol{\varepsilon}) = \boldsymbol{0}$ 与 $\operatorname{Cov}(\boldsymbol{\varepsilon}) = \sigma^2I_n$（给定 $X$）。不需要正态性。

**定理 7.3.2（Gauss–Markov 定理）** 在 Gauss–Markov 条件下，普通最小二乘估计量 $\boldsymbol{b}$ 是 $\boldsymbol{\beta}$ 的最佳线性无偏估计（BLUE）：对每个形如 $\tilde{\boldsymbol{\beta}} = A\boldsymbol{Y}$（$A$ 为 $p \times n$ 常数矩阵）且对所有 $\boldsymbol{\beta}$ 都无偏的估计量，矩阵 $\operatorname{Cov}(\tilde{\boldsymbol{\beta}}) - \operatorname{Cov}(\boldsymbol{b})$ 半正定。特别地，对每个 $\boldsymbol{c} \in \mathbb{R}^p$ 有 $\operatorname{Var}(\boldsymbol{c}^{\mathsf T}\tilde{\boldsymbol{\beta}}) \ge \operatorname{Var}(\boldsymbol{c}^{\mathsf T}\boldsymbol{b})$，每个 $\tilde\beta_k$ 的方差都不小于 $\operatorname{Var}(b_k)$。

**证明** 记 $A = (X^{\mathsf T}X)^{-1}X^{\mathsf T} + D$，于是 $\tilde{\boldsymbol{\beta}} = D\boldsymbol{Y} + \boldsymbol{b}$。对所有 $\boldsymbol{\beta}$ 无偏意味着

$$
\mathbb{E}(\tilde{\boldsymbol{\beta}}) = \mathbb{E}(D\boldsymbol{Y} + \boldsymbol{b}) = DX\boldsymbol{\beta} + \boldsymbol{\beta} = \boldsymbol{\beta} \quad\text{对所有 }\boldsymbol{\beta}, \qquad\text{从而}\qquad DX = O.
$$
于是

$$
\begin{aligned}
\operatorname{Cov}(\tilde{\boldsymbol{\beta}}) &= \operatorname{Cov}\big(D\boldsymbol{\varepsilon} + (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{\varepsilon}\big) = \sigma^2\big\{D + (X^{\mathsf T}X)^{-1}X^{\mathsf T}\big\}\big\{D + (X^{\mathsf T}X)^{-1}X^{\mathsf T}\big\}^{\mathsf T} \\
&= \sigma^2\big\{DD^{\mathsf T} + (X^{\mathsf T}X)^{-1} + DX(X^{\mathsf T}X)^{-1} + (X^{\mathsf T}X)^{-1}X^{\mathsf T}D^{\mathsf T}\big\} = \sigma^2\big\{DD^{\mathsf T} + (X^{\mathsf T}X)^{-1}\big\},
\end{aligned}
$$
因为由 $DX = O$，两个交叉项为零。由于 $DD^{\mathsf T}$ 半正定，$\operatorname{Cov}(\tilde{\boldsymbol{\beta}}) \succeq \sigma^2(X^{\mathsf T}X)^{-1} = \operatorname{Cov}(\boldsymbol{b})$。$\square$

这就是 [3.2.3](/3.2.3) 的 **Gauss–Markov 定理**，只是记号不同。它解释了 [3.3.5](/3.3.5) 的说法：在异方差下（条件 5 不成立），最小二乘仍然无偏，但不再是最佳的。它也有局限。"最佳"只是相对于线性无偏估计而言，而比较估计量的自然准则是**均方误差** $\mathbb{E}\big[(\tilde\beta - \beta)^2\big] = \operatorname{Var}(\tilde\beta) + (\text{偏差})^2$，即**偏差–方差权衡**（[3.2.3](/3.2.3)）。方差小得多的有偏估计在实践中可能更可取，这是**岭回归**（[3.4.7](/3.4.7)）背后的想法；方差比 OLS 大的无偏估计则永远不会更好。

![Sampling densities of three rival estimators of beta: a biased estimator with small variance, the OLS estimator (unbiased with the smallest variance among linear unbiased estimators) and an unbiased estimator with larger variance; the legend gives their mean squared errors](./plots/rival-estimators.py)

### 7.3.3. 帽子矩阵与杠杆值

帽子矩阵 $H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$，即投影矩阵或影响矩阵，把响应向量映为拟合值向量，$\hat{\boldsymbol{Y}} = H\boldsymbol{Y}$。它的元素描述每个响应值对每个拟合值的影响，

$$
\hat Y_i = \sum_{j=1}^n h_{ij}Y_j, \qquad h_{ij} = \frac{\partial\hat Y_i}{\partial Y_j} = \boldsymbol{x}_{(i)}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_{(j)},
$$
其对角元 $h_{ii} = \partial\hat Y_i/\partial Y_i = \boldsymbol{x}_{(i)}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_{(i)}$ 就是 [3.3.6](/3.3.6) 的**杠杆值**：每个响应值对同一观测的拟合值的影响。

**命题 7.3.1** $0 \le h_{ii} \le 1$，且 $\sum_{i=1}^n h_{ii} = \operatorname{tr}(H) = p$。若模型含截距，则 $h_{ii} \ge 1/n$。

**证明** 由于 $H$ 对称幂等，$h_{ii} = (H^2)_{ii} = \sum_jh_{ij}^2 = h_{ii}^2 + \sum_{j\ne i}h_{ij}^2 \ge 0$，再由 $h_{ii} \ge h_{ii}^2$ 得 $h_{ii} \le 1$。由迹的循环性质，$\operatorname{tr}(H) = \operatorname{tr}\big((X^{\mathsf T}X)^{-1}X^{\mathsf T}X\big) = \operatorname{tr}(I_p) = p$。若 $\boldsymbol{1}_n \in \mathcal{R}(X)$，则 $H\boldsymbol{1}_n = \boldsymbol{1}_n$，于是 $H - \frac1nJ$（$J = \boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$）仍对称幂等，因而半正定，其对角元 $h_{ii} - 1/n$ 非负。$\square$

平均杠杆值为 $p/n$。对简单线性回归，由 $\boldsymbol{x}_{(i)}^{\mathsf T} = (1, X_i)$ 和 7.1.3 节的逆矩阵，

$$
h_{ii} = \frac{\sum_jX_j^2 + nX_i^2 - 2X_i\sum_jX_j}{n\sum_jX_j^2 - (\sum_jX_j)^2} = \frac{\big(\sum_jX_j^2 - n\bar X^2\big) + n(X_i - \bar X)^2}{n\big(\sum_jX_j^2 - n\bar X^2\big)} = \frac1n + \frac{(X_i - \bar X)^2}{\sum_{j=1}^n(X_j - \bar X)^2},
$$
与命题 6.1.1 一致。为什么杠杆值是一种距离？一般地，它按样本的形状（密度）度量 $\boldsymbol{x}_{(i)}$ 与预测变量取值中心之间的距离：预测变量散点图同一条等高线上的点有相同的杠杆值。

**命题 7.3.2（杠杆值与马氏距离）** 设模型含截距，记 $\boldsymbol{x}_{(i)}^{\mathsf T} = (1, \boldsymbol{z}_i^{\mathsf T})$，$\boldsymbol{z}_i \in \mathbb{R}^{p-1}$ 为个体 $i$ 的预测变量值，$\bar{\boldsymbol{z}}$ 与 $S$ 为 $\boldsymbol{z}_1, \dots, \boldsymbol{z}_n$ 的样本均值向量与样本协方差矩阵。则

$$
h_{ii} = \frac1n + \frac{D^2(\boldsymbol{z}_i, \bar{\boldsymbol{z}})}{n - 1}, \qquad\text{即}\qquad D^2(\boldsymbol{z}_i, \bar{\boldsymbol{z}}) = (n - 1)\Big(h_{ii} - \frac1n\Big),
$$
其中 $D^2(\boldsymbol{z}, \bar{\boldsymbol{z}}) = (\boldsymbol{z} - \bar{\boldsymbol{z}})^{\mathsf T}S^{-1}(\boldsymbol{z} - \bar{\boldsymbol{z}})$ 是平方**马氏距离**（[3.4.1](/3.4.1)）。

**证明** 记 $Z_c$ 为以 $(\boldsymbol{z}_i - \bar{\boldsymbol{z}})^{\mathsf T}$ 为行的 $n \times (p - 1)$ 矩阵。减去列 $\boldsymbol{1}_n$ 的倍数不改变列空间，所以 $\mathcal{R}(X) = \mathcal{R}([\boldsymbol{1}_n \mid Z_c])$，且两块正交，$\boldsymbol{1}_n^{\mathsf T}Z_c = \boldsymbol{0}^{\mathsf T}$。到两个正交子空间之和的投影等于到各自的投影之和，所以

$$
H = \frac1nJ + Z_c(Z_c^{\mathsf T}Z_c)^{-1}Z_c^{\mathsf T}, \qquad h_{ii} = \frac1n + (\boldsymbol{z}_i - \bar{\boldsymbol{z}})^{\mathsf T}(Z_c^{\mathsf T}Z_c)^{-1}(\boldsymbol{z}_i - \bar{\boldsymbol{z}}),
$$
而 $Z_c^{\mathsf T}Z_c = (n - 1)S$。$\square$

因此有多个预测变量时，一个个体可以在每个预测变量单独看来都不极端的情况下具有高杠杆值：起作用的是按预测变量协方差度量的距离，打破相关模式的个体离中心很远。

![Leverage contours for a regression on two correlated predictors: the curves of constant h_ii are ellipses following the shape of the scatter, and a point that is not extreme in either predictor separately but lies against the correlation has the largest leverage](./plots/leverage-contours.py)

平方和的自由度是其二次型矩阵的秩：$\boldsymbol{Y}^{\mathsf T}A\boldsymbol{Y}$ 的自由度为 $\operatorname{rank}(A)$。幂等矩阵 $A$ 的特征值只能是 $0$ 或 $1$，所以 $\operatorname{rank}(A) = \operatorname{tr}(A) = \sum\lambda_i$。$H$ 幂等，$I_n - H$ 也幂等，$(I_n - H)^2 = I_n - H$，由引理 7.1.1 或直接计算，

$$
\mathrm{df}(\mathrm{SSE}) = \operatorname{rank}(I_n - H) = \operatorname{tr}(I_n - H) = n - \operatorname{tr}(H) = n - p.
$$

**命题 7.3.3（残差的协方差矩阵）** $I_n - H$ 的特征值为 $1$ 或 $0$，且

$$
\operatorname{Cov}(\boldsymbol{e}) = \operatorname{Cov}\big((I_n - H)\boldsymbol{Y}\big) = (I_n - H)\,\sigma^2I_n\,(I_n - H)^{\mathsf T} = \sigma^2(I_n - H), \qquad\text{从而}\qquad \operatorname{Var}(e_i) = \sigma^2(1 - h_{ii}), \quad \operatorname{Cov}(e_i, e_j) = -\sigma^2h_{ij}\ (i \ne j).
$$

随机误差 $\boldsymbol{\varepsilon}$ 不是残差 $\boldsymbol{e}$！即使误差满足方差相等的假设，残差的方差也不相等：个体的杠杆值越大，其残差的方差越小。在简单线性回归中，$X_i$ 位于取值范围两端的个体 $h_{ii}$ 最大，拟合直线在那里最贴近数据，它们的残差方差最小；中间的残差变异最大。这正是 [3.3.6](/3.3.6) 引入标准化残差和学生化残差的原因。

残差之间的这种相依性会影响把 $e_1, \dots, e_n$ 当作 iid 样本的正态性检验吗？含截距时 $\sum_ie_i = 0$，所以

$$
0 = \operatorname{Var}\Big(\sum_{i=1}^ne_i\Big) = \sum_{i=1}^n\operatorname{Var}(e_i) + \sum_{i\ne j}\operatorname{Cov}(e_i, e_j) = \sigma^2\big(n - \operatorname{tr}(H)\big) + n(n - 1)\,\overline{\operatorname{Cov}(e_i, e_j)},
$$
其中横线表示对 $i$ 以及对 $i \ne j$ 的数对取平均。因此

$$
\overline{\operatorname{Var}(e_i)} = \sigma^2\Big(1 - \frac pn\Big), \qquad \overline{\operatorname{Cov}(e_i, e_j)} = -\frac{\sigma^2(1 - p/n)}{n - 1}, \qquad \overline{\operatorname{Corr}(e_i, e_j)} \approx -\frac{1}{n - 1} \approx 0.
$$
只要 $p/n$ 很小，这在实践中影响不大。一个常用于残差的检验，特别是在计量经济学中，是 Jarque–Bera 检验（Jarque–Bera test），它是一种 Lagrange 乘子（得分）检验，使用残差的样本偏度 $S$ 与样本峰度 $K = m_4/m_2^2$：

$$
\mathrm{JB} = \frac n6\left(S^2 + \frac14(K - 3)^2\right) \overset{\cdot}{\sim} \chi^2_2
$$
（正态性下，$n$ 很大时）。对小样本或相依数据，其 $\chi^2$ 近似很差，要用自助法版本。

## 7.4. 方差分析

### 7.4.1. 平方和与自由度

变异来源与 [3.3.4](/3.3.4) 相同：回归（SAS 中称为模型）、误差（R 中称为残差）与总计，平方和与自由度像以前一样相加。记 $\boldsymbol{1}_n$ 为全 1 向量，

$$
\mathrm{SSR} = \sum_{i=1}^n(\hat Y_i - \bar Y)^2 = (\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n), \qquad \mathrm{SSE} = \sum_{i=1}^n(Y_i - \hat Y_i)^2 = (\boldsymbol{Y} - \hat{\boldsymbol{Y}})^{\mathsf T}(\boldsymbol{Y} - \hat{\boldsymbol{Y}}),
$$

$$
\mathrm{SSTO} = \sum_{i=1}^n(Y_i - \bar Y)^2 = (\boldsymbol{Y} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\boldsymbol{Y} - \bar Y\boldsymbol{1}_n).
$$
（有的教材和软件把 $\mathrm{SSR}$ 写作 SSM，$\mathrm{SSTO}$ 写作 SST，$\mathrm{SSE}$ 写作 RSS。）

**命题 7.4.1** 记 $J = \boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$ 为 $n \times n$ 全 1 矩阵。若模型含截距，则

$$
\mathrm{SSTO} = \boldsymbol{Y}^{\mathsf T}\Big(I_n - \frac1nJ\Big)\boldsymbol{Y}, \qquad \mathrm{SSR} = \boldsymbol{Y}^{\mathsf T}\Big(H - \frac1nJ\Big)\boldsymbol{Y}, \qquad \mathrm{SSE} = \boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y},
$$
三个矩阵都对称幂等，秩分别为 $n - 1$、$p - 1$ 与 $n - p$，并且

$$
\mathrm{SSTO} = \mathrm{SSR} + \mathrm{SSE}, \qquad \mathrm{df}_T = n - 1 = \mathrm{df}_R + \mathrm{df}_E = (p - 1) + (n - p).
$$

**证明** 由于 $\bar Y = \frac1n\boldsymbol{1}_n^{\mathsf T}\boldsymbol{Y} = \frac1n\boldsymbol{Y}^{\mathsf T}\boldsymbol{1}_n$，

$$
\mathrm{SSTO} = \boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} - 2\bar Y\boldsymbol{Y}^{\mathsf T}\boldsymbol{1}_n + \boldsymbol{1}_n^{\mathsf T}\boldsymbol{1}_n\bar Y^2 = \boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} - \frac2n\boldsymbol{Y}^{\mathsf T}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}\boldsymbol{Y} + \frac1n\boldsymbol{Y}^{\mathsf T}\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}\boldsymbol{Y} = \boldsymbol{Y}^{\mathsf T}\Big(I_n - \frac1nJ\Big)\boldsymbol{Y}.
$$
$\frac1nJ$ 是秩为 $1$ 的幂等矩阵（到 $\operatorname{span}(\boldsymbol{1}_n)$ 的投影），所以 $I_n - \frac1nJ$ 是秩为 $n - 1$ 的幂等矩阵。其次，$\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n = (H - \frac1nJ)\boldsymbol{Y}$，又由于 $\boldsymbol{1}_n \in \mathcal{R}(X)$ 有 $HJ = JH = J$，所以 $(H - \frac1nJ)^2 = H - \frac1nJ$，秩为 $\operatorname{tr}(H) - \operatorname{tr}(\frac1nJ) = p - 1$。最后，

$$
(\boldsymbol{Y} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\boldsymbol{Y} - \bar Y\boldsymbol{1}_n) = (\boldsymbol{Y} - \hat{\boldsymbol{Y}} + \hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\boldsymbol{Y} - \hat{\boldsymbol{Y}} + \hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n) = (\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n)^{\mathsf T}(\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n) + (\boldsymbol{Y} - \hat{\boldsymbol{Y}})^{\mathsf T}(\boldsymbol{Y} - \hat{\boldsymbol{Y}}),
$$
因为由 $\boldsymbol{e}^{\mathsf T}\hat{\boldsymbol{Y}} = 0$ 与 $\boldsymbol{e}^{\mathsf T}\boldsymbol{1}_n = 0$，交叉项 $\boldsymbol{e}^{\mathsf T}(\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n) = 0$。$\square$

均方为 $\mathrm{MSTO} = \mathrm{SSTO}/\mathrm{df}_T$、$\mathrm{MSR} = \mathrm{SSR}/\mathrm{df}_R$ 与 $\mathrm{MSE} = \mathrm{SSE}/\mathrm{df}_E$。

| 来源 | 平方和 | 自由度 | 均方 | $F$ |
|---|---|---|---|---|
| 回归 | $\mathrm{SSR} = \sum(\hat Y_i - \bar Y)^2$ | $p - 1$ | $\mathrm{MSR} = \mathrm{SSR}/(p - 1)$ | $\mathrm{MSR}/\mathrm{MSE}$ |
| 误差 | $\mathrm{SSE} = \sum(Y_i - \hat Y_i)^2$ | $n - p$ | $\mathrm{MSE} = \mathrm{SSE}/(n - p)$ | |
| 总计 | $\mathrm{SSTO} = \sum(Y_i - \bar Y)^2$ | $n - 1$ | $\mathrm{MSTO} = \mathrm{SSTO}/(n - 1)$ | |

### 7.4.2. 期望均方与 F 检验

**命题 7.4.2（期望均方）** 在多元线性回归模型中，

$$
\mathbb{E}(\mathrm{MSE}) = \sigma^2, \qquad \mathbb{E}(\mathrm{MSR}) = \sigma^2 + \frac{1}{p - 1}(X\boldsymbol{\beta})^{\mathsf T}\Big(I_n - \frac1nJ\Big)X\boldsymbol{\beta}.
$$
在良好设计 $\operatorname{rank}(X) = p$ 之下，二次型 $(X\boldsymbol{\beta})^{\mathsf T}(I_n - \frac1nJ)X\boldsymbol{\beta}$ 为 $0$ 当且仅当 $\beta_1 = \beta_2 = \cdots = \beta_{p-1} = 0$，至少有一个 $\beta_k \ne 0$ 时为正。

**证明** 由于 $(I_n - H)X = O$，$\mathrm{MSE} = \boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}/(n - p) = \boldsymbol{\varepsilon}^{\mathsf T}(I_n - H)\boldsymbol{\varepsilon}/(n - p)$，由定理 7.1.2

$$
\mathbb{E}(\mathrm{MSE}) = \frac{\mathbb{E}\big(\boldsymbol{\varepsilon}^{\mathsf T}(I_n - H)\boldsymbol{\varepsilon}\big)}{n - p} = \frac{\operatorname{tr}\big[(I_n - H)(\sigma^2I_n)\big]}{n - p} = \sigma^2.
$$
对 $\mathrm{SSR} = \boldsymbol{Y}^{\mathsf T}(H - \frac1nJ)\boldsymbol{Y}$，$\boldsymbol{Y} \sim \mathcal{N}(X\boldsymbol{\beta}, \sigma^2I_n)$，定理 7.1.2 给出

$$
\mathbb{E}\Big[\boldsymbol{Y}^{\mathsf T}\Big(H - \frac1nJ\Big)\boldsymbol{Y}\Big] = (X\boldsymbol{\beta})^{\mathsf T}\Big(H - \frac1nJ\Big)(X\boldsymbol{\beta}) + \sigma^2\operatorname{tr}\Big(H - \frac1nJ\Big),
$$
其中 $\operatorname{tr}(H - \frac1nJ) = \operatorname{rank}(H) - \operatorname{rank}(\frac1nJ) = p - 1$，并且由 $HX = X$，

$$
(X\boldsymbol{\beta})^{\mathsf T}\Big(H - \frac1nJ\Big)(X\boldsymbol{\beta}) = \boldsymbol{\beta}^{\mathsf T}\Big(X^{\mathsf T}HX - \frac1nX^{\mathsf T}JX\Big)\boldsymbol{\beta} = \boldsymbol{\beta}^{\mathsf T}\Big(X^{\mathsf T}X - \frac1nX^{\mathsf T}JX\Big)\boldsymbol{\beta} = (X\boldsymbol{\beta})^{\mathsf T}\Big(I_n - \frac1nJ\Big)X\boldsymbol{\beta}.
$$
除以 $p - 1$ 即得 $\mathbb{E}(\mathrm{MSR})$。$I_n - \frac1nJ$ 幂等，因而半正定，这个二次型等于 $\|(I_n - \frac1nJ)X\boldsymbol{\beta}\|^2$，它为零恰当 $X\boldsymbol{\beta}$ 是 $\boldsymbol{1}_n$ 的倍数；由于 $X$ 的各列线性无关，这恰在 $\beta_1 = \cdots = \beta_{p-1} = 0$ 时发生。$\square$

所以没有预测变量起作用时，$\mathrm{MSR}$ 与 $\mathrm{MSE}$ 估计同一个 $\sigma^2$，否则 $\mathrm{MSR}$ 倾向于更大：它们的比值是自然的检验统计量。

**定理 7.4.1（方差分析 F 检验）** 对假设

$$
H_0\colon \beta_1 = \beta_2 = \cdots = \beta_{p-1} = 0 \qquad\text{vs}\qquad H_1\colon \text{至少有一个 } k \in \{1, 2, \dots, p - 1\} \text{ 使 } \beta_k \ne 0,
$$
检验统计量 $F^* = \mathrm{MSR}/\mathrm{MSE}$ 在 $H_0$ 下的抽样分布为 $F^* \sim F_{p-1,n-p}$。在水平 $\alpha$ 下，若计算值 $F_0$ 超过 $F_{p-1,n-p,\alpha}$，或者等价地 $p$ 值 $\mathbb{P}(F^* > F_0 \mid H_0)$ 小于 $\alpha$，则拒绝 $H_0$。

**证明** 在 $H_0$ 下 $X\boldsymbol{\beta} = \beta_0\boldsymbol{1}_n$，而 $(H - \frac1nJ)\boldsymbol{1}_n = \boldsymbol{0}$，所以 $\mathrm{SSR} = \boldsymbol{\varepsilon}^{\mathsf T}(H - \frac1nJ)\boldsymbol{\varepsilon}$；同时 $\mathrm{SSE} = \boldsymbol{\varepsilon}^{\mathsf T}(I_n - H)\boldsymbol{\varepsilon}$。两个矩阵都对称幂等，秩分别为 $p - 1$ 与 $n - p$，所以与定理 7.3.1 的证明一样，$\mathrm{SSR}/\sigma^2 \sim \chi^2_{p-1}$，$\mathrm{SSE}/\sigma^2 \sim \chi^2_{n-p}$。此外 $\mathrm{SSR} = \|\boldsymbol{W}_1\|^2$、$\mathrm{SSE} = \|\boldsymbol{W}_2\|^2$，其中 $\boldsymbol{W}_1 = (H - \frac1nJ)\boldsymbol{\varepsilon}$，$\boldsymbol{W}_2 = (I_n - H)\boldsymbol{\varepsilon}$，并且由 $H(I_n - H) = O$ 与 $J(I_n - H) = J - JH = O$ 得 $(H - \frac1nJ)(I_n - H) = O$；由 (N4) 与 (N5)，两个平方和独立。两个独立卡方变量各除以自由度后之比服从 $F_{p-1,n-p}$ 分布。$\square$

若拒绝 $H_0$，则有证据表明线性模型中的一个或多个解释变量对预测（解释）响应可能有用。若不拒绝 $H_0$，则没有证据表明任何解释变量能通过线性模型帮助建模、预测或解释响应。整体检验并不说明哪些预测变量起作用；那是 [3.3.8](/3.3.8) 与 [3.3.9](/3.3.9) 中 $t$ 检验与偏 $F$ 检验的任务。$p = 2$ 时它就是 [3.3.4](/3.3.4) 中 $H_0\colon \beta_1 = 0$ 的 $F$ 检验。

### 7.4.3. R² 与调整 R²

**定义 7.4.1（多重决定系数）** **多重决定系数**为

$$
R^2 = \frac{\mathrm{SSR}}{\mathrm{SSTO}} = \frac{\sum(\hat Y_i - \bar Y)^2}{\sum(Y_i - \bar Y)^2} = 1 - \frac{\mathrm{SSE}}{\mathrm{SSTO}}.
$$
它给出响应的变异中能被模型，即被模型中全部解释变量解释的比例；$1 - R^2$ 是未被解释的比例。

**命题 7.4.3** 若模型含截距：

1. $R^2 = r^2$，其中 $r$ 是响应 $Y_i$ 与拟合值 $\hat Y_i$ 的样本相关系数；$R = \sqrt{R^2} = r$ 是样本**复相关系数**。
2. $F^* = \dfrac{R^2}{1 - R^2}\cdot\dfrac{n - p}{p - 1}$。
3. 增加一个解释变量永远不会使 $\mathrm{SSE}$ 增大，也不会使 $R^2$ 减小。

**证明** (1) 由于 $\sum e_i = 0$，各 $\hat Y_i$ 的均值为 $\bar Y$。与命题 7.4.1 的证明一样，$\sum(Y_i - \bar Y)(\hat Y_i - \bar Y) = (\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n + \boldsymbol{e})^{\mathsf T}(\hat{\boldsymbol{Y}} - \bar Y\boldsymbol{1}_n) = \mathrm{SSR}$，所以

$$
r = \frac{\sum(Y_i - \bar Y)(\hat Y_i - \bar Y)}{\sqrt{\sum(Y_i - \bar Y)^2}\sqrt{\sum(\hat Y_i - \bar Y)^2}} = \frac{\mathrm{SSR}}{\sqrt{\mathrm{SSTO}\cdot\mathrm{SSR}}} = \sqrt{\frac{\sum(\hat Y_i - \bar Y)^2}{\sum(Y_i - \bar Y)^2}}.
$$
(2) $F^* = \dfrac{\mathrm{SSR}/(p - 1)}{\mathrm{SSE}/(n - p)}$；分子分母同除以 $\mathrm{SSTO}$。(3) 增加一列 $\boldsymbol{z}$ 时列空间只会扩大，$\mathcal{R}(X_{\mathrm{old}}) \subseteq \mathcal{R}(X_{\mathrm{new}})$，而 $\mathrm{SSE}$ 是 $\boldsymbol{Y}$ 到列空间的距离平方，子空间扩大时它不会增加；$\mathrm{SSTO}$ 不变。$\square$

更确切地说，若 $\boldsymbol{z}$ 不是原有各列的线性组合，记 $\tilde{\boldsymbol{z}} = (I_n - H_{\mathrm{old}})\boldsymbol{z} \ne \boldsymbol{0}$ 为它与 $\mathcal{R}(X_{\mathrm{old}})$ 正交的部分。则 $\mathcal{R}(X_{\mathrm{new}})$ 是 $\mathcal{R}(X_{\mathrm{old}})$ 与 $\operatorname{span}(\tilde{\boldsymbol{z}})$ 的正交和，新残差等于旧残差减去它在 $\tilde{\boldsymbol{z}}$ 上的投影，并且

$$
\mathrm{SSE}_{\mathrm{new}} = \mathrm{SSE}_{\mathrm{old}} - \frac{(\tilde{\boldsymbol{z}}^{\mathsf T}\boldsymbol{e}_{\mathrm{old}})^2}{\tilde{\boldsymbol{z}}^{\mathsf T}\tilde{\boldsymbol{z}}}.
$$
所以除非新变量在扣除旧变量的影响之后恰好与旧残差不相关，$\mathrm{SSE}$ 都严格减小。实际上它几乎总会减小，即使新变量是纯粹的噪声。因此不能只用 $R^2$ 在预测变量个数不同的模型之间作选择。

**定义 7.4.2（调整的决定系数）** **调整的决定系数**为

$$
R_a^2 = 1 - \frac{\mathrm{MSE}}{\mathrm{MSTO}} = 1 - \frac{n - 1}{n - p}\cdot\frac{\mathrm{SSE}}{\mathrm{SSTO}},
$$
它把 $1 - R^2$ 中的平方和换成均方，以 $\hat\sigma^2 = \mathrm{MSE} = \mathrm{SSE}/(n - p)$ 作为误差方差的估计。

增加解释变量时，$R^2$ 总是增大（或不变），而 $R_a^2$ 可能减小：$\mathrm{SSE}$ 的减少必须超过失去一个自由度的代价。总有 $R_a^2 \le R^2$，且 $R_a^2$ 可以为负。基于这一想法的模型选择准则在 [3.3.11](/3.3.11) 中讨论。[3.3.6](/3.3.6) 列出的 $R^2$ 的局限同样适用于 $R_a^2$。

## 小结

| 量 | 矩阵形式 | 分布或性质 |
|---|---|---|
| 模型 | $\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$，$X$ 为 $n \times p$，秩为 $p$ | $\boldsymbol{Y} \sim \mathcal{N}_n(X\boldsymbol{\beta}, \sigma^2I_n)$ |
| 估计 | $\boldsymbol{b} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ | $\mathcal{N}_p\big(\boldsymbol{\beta}, \sigma^2(X^{\mathsf T}X)^{-1}\big)$；BLUE |
| 拟合值、残差 | $\hat{\boldsymbol{Y}} = H\boldsymbol{Y}$，$\boldsymbol{e} = (I_n - H)\boldsymbol{Y}$，$H = X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$ | $\boldsymbol{e}^{\mathsf T}\hat{\boldsymbol{Y}} = 0$；$\operatorname{Cov}(\boldsymbol{e}) = \sigma^2(I_n - H)$ |
| 杠杆值 | $h_{ii} = \boldsymbol{x}_{(i)}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_{(i)}$ | $\frac1n \le h_{ii} \le 1$，$\sum h_{ii} = p$，$h_{ii} = \frac1n + \frac{D^2}{n - 1}$ |
| $\mathrm{SSE}$、$\mathrm{SSR}$、$\mathrm{SSTO}$ | $\boldsymbol{Y}^{\mathsf T}(I_n - H)\boldsymbol{Y}$、$\boldsymbol{Y}^{\mathsf T}(H - \frac1nJ)\boldsymbol{Y}$、$\boldsymbol{Y}^{\mathsf T}(I_n - \frac1nJ)\boldsymbol{Y}$ | 自由度 $n - p$、$p - 1$、$n - 1$ |
| 整体 $F$ 检验 | $F^* = \mathrm{MSR}/\mathrm{MSE}$ | 在 $H_0\colon \beta_1 = \cdots = \beta_{p-1} = 0$ 下为 $F_{p-1,n-p}$ |
| $R^2$、$R_a^2$ | $1 - \mathrm{SSE}/\mathrm{SSTO}$、$1 - \mathrm{MSE}/\mathrm{MSTO}$ | $R^2 = r^2(\boldsymbol{Y}, \hat{\boldsymbol{Y}})$；$R_a^2$ 惩罚多余的预测变量 |

- 最小二乘有两种推导：令 $\|\boldsymbol{Y} - X\boldsymbol{\beta}\|^2$ 的梯度为零，以及把 $\boldsymbol{Y}$ 正交投影到列空间 $\mathcal{R}(X)$ 上；两者都给出正规方程 $X^{\mathsf T}\boldsymbol{e} = \boldsymbol{0}$。
- 每个分布结果都来自多元正态分布的几条事实（线性变换、协方差为零即独立、投影矩阵的二次型服从卡方分布）以及 $\mathbb{E}(\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}) = \operatorname{tr}(A\Sigma) + \boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}$。
- Gauss–Markov 定理只需要 $\mathbb{E}(\boldsymbol{\varepsilon}) = \boldsymbol{0}$、$\operatorname{Cov}(\boldsymbol{\varepsilon}) = \sigma^2I_n$ 与满秩；它只把 OLS 与线性无偏估计相比。
- 偏回归系数度量其他预测变量保持不变时一个预测变量的效应；多项式项、交互项和虚拟变量使模型仍关于参数线性。
