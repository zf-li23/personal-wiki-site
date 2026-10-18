---
title: 多维标度与核主成分分析
description: 主成分分析的三种等价表述；用奇异值分解计算主成分及其与特征值分解在精度上的权衡；邻近矩阵与欧氏距离矩阵；经典多维标度（主坐标分析）及其刻画定理；核主成分分析与正定核；用于可视化的 t-SNE。
source_hash: 7afcc25fc728
---

上一章（[3.4.5](/3.4.5)）用 $p \times p$ 协方差矩阵的特征向量定义了主成分。本章从另外三个角度看主成分分析。理论上，逐个构造成分等价于整体地拟合最佳的 $r$ 维子空间。计算上，主成分由中心化数据矩阵的**奇异值分解**得到，这样不仅更精确，而且通过观测之间内积组成的 $n \times n$ 矩阵，引出两种推广。第一种是多维标度，在只知道观测之间距离时重建点的构形。第二种是核主成分分析，先把数据非线性地映射到高维特征空间再做主成分分析，却从不需要计算这个映射。最后介绍 t-SNE，一种借用观测间相似度思想的非线性可视化方法。这些工具将在聚类分析（[3.4.11](/3.4.11)）和统计计算（[3.5](/3.5)）中再次出现。

## 6.1. 再看主成分分析

### 6.1.1. 三种表述

[3.4.5](/3.4.5) 的主成分可以用三种等价的方式导出：

| | 逐个方向 | $r$ 维子空间：距离小 | $r$ 维子空间：散布大 |
|---|---|---|---|
| 动机 | 保留信息，即散布大 | 投影离数据近 | 投影散布开 |
| 模型 | $\boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ | 位置 $C$，方向 $U$，系数 $\boldsymbol{b}$ | 方向 $U$ |
| 目标函数 | $\max_{\boldsymbol{a}}\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \max_{\boldsymbol{a}}\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}$ | $\min_{U, C, \boldsymbol{b}}\mathbb{E}d^2 = \operatorname{tr}\Sigma - \max_U\operatorname{tr}(U^{\mathsf T}\Sigma U)$ | $\max_U\sum_{i=1}^p\operatorname{Var}(\tilde X_i) = \max_U\operatorname{tr}(U^{\mathsf T}\Sigma U)$ |
| 解 | $\boldsymbol{a}_i = \boldsymbol{e}_i$ | 对每个 $r$，$U = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_r]$ | 对每个 $r$，$U = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_r]$ |

这里 $U$ 的列标准正交，$\tilde{\boldsymbol{X}} = UU^{\mathsf T}(\boldsymbol{X} - \boldsymbol{\mu})$ 是投影（见 [3.4.5](/3.4.5) 第 5.6 节）。后两种表述说明前 $r$ 个成分作为整体也是最优的，而不只是逐个最优。

### 6.1.2. 数据矩阵与中心化矩阵

设 $X$ 是 $n \times p$ 的**数据矩阵**，行为 $\boldsymbol{x}_1^{\mathsf T}, \dots, \boldsymbol{x}_n^{\mathsf T}$。样本均值为 $\bar{\boldsymbol{x}} = \frac1nX^{\mathsf T}\boldsymbol{1}_n$；例如

$$
X = \begin{bmatrix} 4 & 1 \\ 5 & 2 \\ 3 & 5 \end{bmatrix}, \qquad \bar{\boldsymbol{x}} = \frac13\begin{bmatrix} 4 & 5 & 3 \\ 1 & 2 & 5 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 \\ 8/3 \end{bmatrix}.
$$

各行都等于 $\bar{\boldsymbol{x}}^{\mathsf T}$ 的矩阵是 $\boldsymbol{1}_n\bar{\boldsymbol{x}}^{\mathsf T} = \frac1n\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}X$，所以减去列均值（消除位置的影响）就是左乘**中心化矩阵** $H = I_n - \frac1n\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}$（[3.4.2](/3.4.2)）：

$$
\tilde X = HX = X - \boldsymbol{1}_n\bar{\boldsymbol{x}}^{\mathsf T}, \qquad \tilde x_{ij} = x_{ij} - \bar x_j.
$$

$H$ 对称且幂等（$H^2 = H$）：它是到 $\boldsymbol{1}_n$ 的正交补上的**正交投影矩阵**。因此

$$
(n-1)S = \tilde X^{\mathsf T}\tilde X = (HX)^{\mathsf T}(HX) = X^{\mathsf T}HX.
$$

### 6.1.3. 用奇异值分解计算主成分

回忆：每个实 $m \times k$ 矩阵 $A$ 都有奇异值分解 $A = U\Gamma V^{\mathsf T}$，其中 $U$（$m \times m$）与 $V$（$k \times k$）为正交矩阵，$\Gamma$ 为 $m \times k$ 矩阵，对角元 $\gamma_1 \ge \gamma_2 \ge \cdots \ge \gamma_{\min(m,k)} \ge 0$，其余元素为零；正的 $\gamma_i$ 是 $A$ 的**奇异值**。于是

$$
AA^{\mathsf T} = U\Gamma\Gamma^{\mathsf T}U^{\mathsf T}, \qquad A^{\mathsf T}A = V\Gamma^{\mathsf T}\Gamma V^{\mathsf T},
$$

所以 $U$ 与 $V$ 的列分别是 $AA^{\mathsf T}$ 与 $A^{\mathsf T}A$ 的特征向量，共同的非零特征值为 $\gamma_i^2$。

把它用于中心化数据矩阵：

$$
S = \frac{1}{n-1}\tilde X^{\mathsf T}\tilde X, \qquad \tilde X = U\Gamma V^{\mathsf T} \ \Longrightarrow\ \tilde X^{\mathsf T}\tilde X = V(\Gamma^{\mathsf T}\Gamma)V^{\mathsf T}.
$$

右奇异向量就是 $S$ 的特征向量：$\hat P = V$，$\hat\lambda_i = \gamma_i^2/(n-1)$。全部主成分得分为

$$
Y = \tilde X\hat P = \tilde XV = U\Gamma V^{\mathsf T}V = U\Gamma,
$$

其 $(i, j)$ 元 $\hat y_{ij} = \hat{\boldsymbol{e}}_j^{\mathsf T}(\boldsymbol{x}_i - \bar{\boldsymbol{x}})$ 是第 $i$ 个单元的第 $j$ 主成分。$S$ 与 $\tilde X^{\mathsf T}\tilde X$ 的谱分解有相同的特征向量，特征值只差因子 $n - 1$。对 [3.4.5](/3.4.5) 的锦龟数据，$U\Gamma$ 的第一列与由 $S$ 的谱分解算出的第一主成分得分完全一致。

### 6.1.4. 奇异值分解与特征值分解的比较

谱分解常称为特征值分解（EVD）。奇异值分解可以通过 $A^{\mathsf T}A$ 的特征值分解来计算，但标准算法（LAPACK 中的算法，R 和 Matlab 都使用它，是 Golub 与 Van Loan 书中 Golub–Kahan 方法的改进）直接作用于 $A$。对主成分分析，两者之间有权衡：

- 速度：$n \gg p$ 时，构造 $p \times p$ 矩阵 $S$ 再做特征值分解代价很小；$n \ll p$ 时，对 $\tilde X$ 做瘦奇异值分解，或等价地处理 $n \times n$ 矩阵 $\tilde X\tilde X^{\mathsf T}$，代价更小，这正是核主成分分析的思路（第 6.3 节）；
- 精度：奇异值分解更好，因为构造 $\tilde X^{\mathsf T}\tilde X$ 会使条件数平方，在浮点运算中可能毁掉小的奇异值。

**例 6.1.1（Läuchli 矩阵）** 设

$$
L = \begin{bmatrix} 1 & 1 & 1 \\ \varepsilon & 0 & 0 \\ 0 & \varepsilon & 0 \\ 0 & 0 & \varepsilon \end{bmatrix}, \qquad L^{\mathsf T}L = \begin{bmatrix} 1 + \varepsilon^2 & 1 & 1 \\ 1 & 1 + \varepsilon^2 & 1 \\ 1 & 1 & 1 + \varepsilon^2 \end{bmatrix}.
$$

$L$ 的奇异值为 $\sqrt{3 + \varepsilon^2}, \varepsilon, \varepsilon$。$\varepsilon = 0.01$ 时，奇异值分解（$1.73208, 0.01, 0.01$）与 $L^{\mathsf T}L$ 的特征值分解（$3.0001, 0.0001, 0.0001$）都是准确的。$\varepsilon = 10^{-10}$ 时，奇异值分解仍给出 $1.7320508, 10^{-10}, 10^{-10}$；但在双精度下 $1 + \varepsilon^2$ 被舍入为 $1$，$L^{\mathsf T}L$ 算出来是秩一矩阵，特征值为 $3, 8.9 \times 10^{-16}, 0$：小奇异值丢失了。

## 6.2. 多维标度

### 6.2.1. 邻近矩阵

主成分分析从 $n \times p$ 数据矩阵出发，得到 $n \times k$ 的坐标矩阵。在多维标度（multidimensional scaling）中，观测到的只是 $n$ 个单元之间的 $n \times n$ 邻近矩阵 $D = (d_{ij})$；数据矩阵 $X$ 可能存在，也可能不存在。目标是用简单的几何模型或地图表示这些邻近度：在低维空间中找点 $\boldsymbol{z}_1, \dots, \boldsymbol{z}_n$，使它们之间的距离尽可能重现 $d_{ij}$。

邻近矩阵（相似度矩阵、相异度矩阵或距离矩阵）的来源，要么是直接的，来自让受试者评价成对刺激相似程度的实验；要么是间接的，由原始剖面数据计算的相关系数、协方差或距离。例如在一项经典研究中，两名受试者用从 $0$（"相同"）到 $100$（"不同"）的视觉模拟量表评价了十种可乐两两之间的差异；所得矩阵对称、类似距离，但不一定满足三角不等式。相反，美国十个城市之间的航空距离是对称的、度量的（满足三角不等式），并且接近欧氏距离。

**定义 6.2.1（邻近矩阵）** $n \times n$ 矩阵 $D = (d_{ij})$ 称为**邻近矩阵**，如果

1. $D = D^{\mathsf T}$，且
2. 对所有 $i, j = 1, \dots, n$，$d_{ij} \ge 0$，$d_{ii} = 0$。

方法分两类。度量多维标度（metric multidimensional scaling）把 $d_{ij}$ 当作距离，其基本形式即本节的经典多维标度。非度量多维标度（nonmetric multidimensional scaling）只用邻近度的大小顺序，例如 Shepard–Kruskal 算法，适合可乐数据这样的主观判断。

### 6.2.2. 欧氏距离矩阵

经典多维标度假设 $D$ 由某个未观测的 $n \times p$ 数据矩阵 $X$ 计算的欧氏距离组成。

**定义 6.2.2（欧氏距离矩阵）** $n \times n$ 矩阵 $D = (d_{ij})$ 称为**欧氏距离矩阵**，如果存在正整数 $p$ 与 $n$ 个点 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n \in \mathbb{R}^p$，使

$$
d_{ij}^2 = (\boldsymbol{x}_i - \boldsymbol{x}_j)^{\mathsf T}(\boldsymbol{x}_i - \boldsymbol{x}_j), \qquad i, j = 1, \dots, n.
$$

给定 $D$，构形并不唯一：若 $\boldsymbol{z}_i = Q\boldsymbol{x}_i + \boldsymbol{a}$，$Q$ 为**正交矩阵**，$\boldsymbol{a}$ 为常数向量，则距离不变。邻近矩阵觉察不到平移、旋转和反射，所以 $X$ 至多在这些变换下被恢复。因此应当恢复的是在这些变换下不变的对象。在主成分分析中我们用的是 $p \times p$ 矩阵 $(HX)^{\mathsf T}(HX)$，它衡量变量之间的相似性；要衡量单元之间的相似性，就用 $n \times n$ 矩阵

$$
B = (HX)(HX)^{\mathsf T}, \qquad b_{ij} = (\boldsymbol{x}_i - \bar{\boldsymbol{x}})^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}}).
$$

$B$ 在平移、旋转和反射下不变。若对所有单元 $\boldsymbol{y}_i = Q\boldsymbol{x}_i + \boldsymbol{a}$，则 $Y = XQ^{\mathsf T} + \boldsymbol{1}_n\boldsymbol{a}^{\mathsf T}$；由于 $H\boldsymbol{1}_n = \boldsymbol{0}$，$HY = HXQ^{\mathsf T}$，从而

$$
(HY)(HY)^{\mathsf T} = HXQ^{\mathsf T}QX^{\mathsf T}H = (HX)(HX)^{\mathsf T}.
$$

### 6.2.3. 经典多维标度

记 $\tilde x_{ik} = x_{ik} - \bar x_k$，于是对每个 $k$ 有 $\sum_{i=1}^n\tilde x_{ik} = 0$。已知量与未知量之间的联系是

$$
d_{ij}^2 = \sum_{k=1}^p(\tilde x_{ik} - \tilde x_{jk})^2 = \sum_k\tilde x_{ik}^2 + \sum_k\tilde x_{jk}^2 - 2\sum_k\tilde x_{ik}\tilde x_{jk} = b_{ii} + b_{jj} - 2b_{ij}.
$$

任务分两步：由 $D$ 求出 $B$，再分解 $B$。

第一步（$D \to B$）。中心化约束给出行和为零：对每个 $i$，$\sum_{j=1}^n b_{ij} = \sum_{k=1}^p\tilde x_{ik}\sum_{j=1}^n\tilde x_{jk} = 0$；由对称性，列和也为零。令 $T = \operatorname{tr}B = \sum_i b_{ii}$。对联系公式求和，

$$
\sum_{i=1}^n d_{ij}^2 = T + nb_{jj}, \qquad \sum_{j=1}^n d_{ij}^2 = T + nb_{ii}, \qquad \sum_{i=1}^n\sum_{j=1}^n d_{ij}^2 = 2nT.
$$

记平均值 $d_{i\cdot}^2 = \frac1n\sum_j d_{ij}^2$，$d_{\cdot j}^2 = \frac1n\sum_i d_{ij}^2$，$d_{\cdot\cdot}^2 = \frac{1}{n^2}\sum_i\sum_j d_{ij}^2$，解出 $b_{ij}$ 得

$$
b_{ij} = -\frac12\big(d_{ij}^2 - d_{i\cdot}^2 - d_{\cdot j}^2 + d_{\cdot\cdot}^2\big), \qquad\text{即}\qquad B = HAH, \quad A = (a_{ij}), \ a_{ij} = -\frac12d_{ij}^2.
$$

第二步（$B \to$ 坐标）。设 $\operatorname{rank}(B) = p$，写出谱分解 $B = P_1\Lambda_1P_1^{\mathsf T}$，$P_1 = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_p]$（$n \times p$），$\Lambda_1 = \operatorname{diag}(\lambda_1, \dots, \lambda_p)$，$\lambda_1 \ge \cdots \ge \lambda_p > 0$。则 $Z = P_1\Lambda_1^{1/2}$ 满足 $ZZ^{\mathsf T} = B$，其各行精确地重现了距离。降维时保留最大的 $k$ 个特征值：

**算法 6.2.1（经典多维标度）** 给定邻近矩阵 $D$ 和目标维数 $k$：

1. 构造 $A = (-\frac12d_{ij}^2)$ 与 $B = HAH$；
2. 计算 $B$ 的特征值 $\lambda_1 \ge \lambda_2 \ge \cdots$ 与标准正交特征向量 $\boldsymbol{e}_1, \boldsymbol{e}_2, \dots$；
3. 输出 $n \times k$ 构形 $\tilde Z = P_k\Lambda_k^{1/2}$，其中 $P_k = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_k]$，$\Lambda_k = \operatorname{diag}(\lambda_1, \dots, \lambda_k)$；第 $i$ 行给出单元 $i$ 的坐标。

维数 $k$ 的选择与主成分分析相同，例如根据比例 $\sum_{i \le k}\lambda_i/\sum_i\lvert\lambda_i\rvert$（或只对正特征值求和）或 $B$ 的特征值碎石图。

这种方法称为经典多维标度（classical multidimensional scaling），简记 CMDS；Gower（1966）称之为主坐标分析（principal coordinates analysis），简记 PCoA，因为它与主成分分析有如下联系。若 $D$ 由 $X$ 各行之间的欧氏距离组成，则 $B = \tilde X\tilde X^{\mathsf T}$；由 $\tilde X = U\Gamma V^{\mathsf T}$，

$$
B = \tilde X\tilde X^{\mathsf T} = U(\Gamma\Gamma^{\mathsf T})U^{\mathsf T}.
$$

所以 $B$ 的特征向量是 $\tilde X$ 的左奇异向量，特征值为 $\gamma_i^2$，$P_k\Lambda_k^{1/2}$ 由 $U\Gamma = \tilde X\hat P$ 的前 $k$ 列组成：经典多维标度的构形恰好就是前 $k$ 个主成分得分组成的矩阵（各列至多相差符号）。主成分分析从变量之间相似性的 $p \times p$ 矩阵到达 $U\Gamma$，经典多维标度则从单元之间相似性的 $n \times n$ 矩阵到达它。若记 $W = \tilde X^{\mathsf T}$ 为把单元当作"变量"的 $p \times n$ 矩阵，则 $B = W^{\mathsf T}W$ 就是相应的叉积矩阵。

**注 6.2.1** $B$ 的每行、每列之和都为零，而样本协方差矩阵 $S$ 一般不是这样。原因在于 $B$ 是由去掉列均值的数据矩阵定义的，相当于对 $p \times n$ 矩阵 $\tilde X^{\mathsf T}$ 先去掉行均值再做叉积；而计算变量的样本协方差矩阵时并不去掉各变量之间的均值。

### 6.2.4. 邻近矩阵何时是欧氏的

**定理 6.2.1** 设 $D = (d_{ij})$ 是 $n \times n$ 邻近矩阵，$A = (-\frac12d_{ij}^2)$，$B = HAH$。则 $D$ 是欧氏距离矩阵当且仅当 $B$ 半正定。此时 $D$ 是 $\mathbb{R}^p$ 中某个构形的距离矩阵，$p = \operatorname{rank}(B)$。

**证明**（$\Rightarrow$）若 $D$ 是点 $\boldsymbol{x}_i$ 的欧氏距离矩阵，第一步的推导表明 $B = (HX)(HX)^{\mathsf T}$，它是半正定的。

（$\Leftarrow$）设 $B$ 半正定，秩为 $p$，正特征值为 $\lambda_1 \ge \cdots \ge \lambda_p > 0$，标准正交特征向量为 $\tilde{\boldsymbol{e}}_1, \dots, \tilde{\boldsymbol{e}}_p$；令 $\tilde P = [\tilde{\boldsymbol{e}}_1, \dots, \tilde{\boldsymbol{e}}_p]$（$n \times p$），$\tilde\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_p)$，于是 $B = \tilde P\tilde\Lambda\tilde P^{\mathsf T}$。令 $\tilde X = \tilde P\tilde\Lambda^{1/2}$，其行为 $\tilde{\boldsymbol{x}}_i^{\mathsf T}$。则 $B = \tilde X\tilde X^{\mathsf T}$，$b_{ij} = \tilde{\boldsymbol{x}}_i^{\mathsf T}\tilde{\boldsymbol{x}}_j$，且

$$
(\tilde{\boldsymbol{x}}_i - \tilde{\boldsymbol{x}}_j)^{\mathsf T}(\tilde{\boldsymbol{x}}_i - \tilde{\boldsymbol{x}}_j) = b_{ii} + b_{jj} - 2b_{ij}. \tag{6.1}
$$

另一方面，$B = HAH$ 意味着 $b_{ij} = a_{ij} - \bar a_{i\cdot} - \bar a_{\cdot j} + \bar a_{\cdot\cdot}$，其中 $\bar a_{i\cdot}, \bar a_{\cdot j}, \bar a_{\cdot\cdot}$ 是 $A$ 的行均值、列均值与总均值。由于 $d_{ii} = 0$，$d_{ij} = d_{ji}$，有 $a_{ii} = 0$ 且 $\bar a_{i\cdot} = \bar a_{\cdot i}$。代入式 (6.1)，所有均值相互抵消，

$$
(\tilde{\boldsymbol{x}}_i - \tilde{\boldsymbol{x}}_j)^{\mathsf T}(\tilde{\boldsymbol{x}}_i - \tilde{\boldsymbol{x}}_j) = a_{ii} + a_{jj} - 2a_{ij} = -2a_{ij} = d_{ij}^2.
$$

所以 $D$ 是 $\tilde{\boldsymbol{x}}_1, \dots, \tilde{\boldsymbol{x}}_n \in \mathbb{R}^p$ 的欧氏距离矩阵。$\square$

若 $B$ 有负特征值，$D$ 就不是欧氏的；此时经典多维标度只使用正的部分，负特征值的大小衡量了与欧氏构形的偏离程度。

### 6.2.5. 实现与例子

R 中 `cmdscale()`（`stats` 包）实现经典多维标度，并可返回 $B$ 的特征值，便于选择 $k$；`isoMDS()`（`MASS` 包）实现非度量多维标度，它依据邻近度的顺序而不是数值。软件的结果可能与上面的理论不同，因为名为"MDS"的函数可能实现的是不要求 $D$ 为距离矩阵的非度量方法。

**例 6.2.1** 中国东部八个城市之间的公路距离（单位：km）为

| | 北京 | 天津 | 济南 | 青岛 | 郑州 | 上海 | 杭州 | 南京 |
|---|---|---|---|---|---|---|---|---|
| 北京 | 0 | | | | | | | |
| 天津 | 118 | 0 | | | | | | |
| 济南 | 439 | 363 | 0 | | | | | |
| 青岛 | 668 | 571 | 362 | 0 | | | | |
| 郑州 | 714 | 729 | 443 | 772 | 0 | | | |
| 上海 | 1259 | 1145 | 886 | 776 | 984 | 0 | | |
| 杭州 | 1328 | 1191 | 872 | 828 | 962 | 203 | 0 | |
| 南京 | 1065 | 936 | 626 | 617 | 710 | 322 | 305 | 0 |

$B$ 的特征值（单位 $10^3\,\mathrm{km}^2$）为 $1756, 337, 79, 38, 13, 0, -14, -33$。公路距离并不严格是欧氏的，所以有两个负特征值，但它们很小，前两个特征值占 $\sum_i\lvert\lambda_i\rvert$ 的 $92\%$。二维的经典多维标度构形在相差一个正交变换的意义下重现了地理位置：经过适当的旋转使北方朝上后，北京和天津在北，上海、杭州和南京在东南，郑州在西，青岛在东，济南居中，与地图大致相同。

![八个城市公路距离的经典多维标度：B 的特征值（左；有两个略小于零）与二维构形（右），已旋转使布局与地图的方向一致](./plots/cmds-cities.py)

**注 6.2.2** 即使有数据矩阵 $X$，多维标度也可能有用。可以计算一个更能反映所关心信息的邻近矩阵，例如由观测之间的样本相关系数得到。若这个 $D$ 是欧氏距离矩阵，就可以把它看作由某个数据矩阵 $\tilde X$ 计算而来，$\tilde X$ 的单元数相同（变量数不必相同）；我们不需要 $\tilde X$ 本身，因为经典多维标度直接给出它的低维表示。

### 6.2.6. 相关方法：潜在语义索引

在文本的"词袋"模型中，$C$ 篇文档在含 $W$ 个词的词典上的情况用 $C \times W$ 的词频矩阵 $n_w^{(c)}$ 概括。潜在语义索引（latent semantic indexing）由 Deerwester 等（1990）提出，简记 LSI，它对这个矩阵做奇异值分解，保留前几个奇异向量，它们张成"词–文档"空间中捕捉了文档集大部分变异的低维子空间。之后在这个潜在空间中比较文档和词，对大型文档集也能实现可观的压缩。

## 6.3. 核主成分分析

### 6.3.1. 非线性推广

主成分分析是线性投影，常用作预处理步骤，例如在分类之前保留最重要的线性特征。但线性不可分的数据经过非线性变换后可能变得可分。平面上分别排成圆盘和外环的两类点不能用直线分开，但经过映射

$$
\phi\big((x_1, x_2)^{\mathsf T}\big) = (x_1^2, x_2^2, \sqrt2x_1x_2)^{\mathsf T}
$$

之后，它们可以用 $\mathbb{R}^3$ 中的平面分开，因为 $x_1^2 + x_2^2$ 对内层一类小、对外层一类大。等价地说，可以先增加特征，再用线性方法。

设观测为 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n \in \mathbb{R}^{p_0}$，把它们映射到维数 $p > p_0$ 的特征空间，

$$
\phi\colon \mathbb{R}^{p_0} \to \mathbb{R}^p, \qquad \boldsymbol{x} \mapsto \tilde{\boldsymbol{x}} = \phi(\boldsymbol{x}),
$$

通常 $p \gg n$（高维问题）。对新特征做主成分分析需要 $p \times p$ 矩阵 $\tilde S_n = \frac1n(H\Phi)^{\mathsf T}(H\Phi)$ 的特征值分解，其中 $\Phi = [\phi(\boldsymbol{x}_1), \dots, \phi(\boldsymbol{x}_n)]^{\mathsf T}$ 为 $n \times p$ 矩阵。当 $p$ 很大甚至无穷时，这是做不到的。办法来自主成分分析与多维标度的经验：改用单元之间内积组成的 $n \times n$ 矩阵。

### 6.3.2. 核技巧

先设 $\Phi$ 已经中心化。我们不分解 $\tilde S_n = \frac1n\Phi^{\mathsf T}\Phi$，而分解

$$
B = \Phi\Phi^{\mathsf T}, \qquad b_{ij} = \langle\phi(\boldsymbol{x}_i), \phi(\boldsymbol{x}_j)\rangle,
$$

即特征向量的经典多维标度中的矩阵 $B$。它的元素是单元之间的相似度，于是给它一个新名字。

**定义 6.3.1（正定核）** 函数 $K\colon \mathbb{R}^{p_0} \times \mathbb{R}^{p_0} \to \mathbb{R}$ 称为**正定核**，如果它是对称的，$K(\boldsymbol{x}, \boldsymbol{y}) = K(\boldsymbol{y}, \boldsymbol{x})$，并且对任意 $n$ 和任意 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$，核矩阵 $K = [K(\boldsymbol{x}_i, \boldsymbol{x}_j)]_{n \times n}$ 都是半正定的。

特征的内积 $K(\boldsymbol{x}_i, \boldsymbol{x}_j) = \langle\phi(\boldsymbol{x}_i), \phi(\boldsymbol{x}_j)\rangle$ 都是正定核；反过来，每个正定核都是到某个（可能无穷维的）Hilbert 空间的特征映射的内积（Mercer 定理，或再生核 Hilbert 空间的 Moore–Aronszajn 构造）。因此核刻画了两个观测之间的相似度。主成分分析与多维标度之间的联系表明，我们从不需要显式地写出 $\phi$——有时它甚至写不出来，例如特征空间是无穷维的时候。我们只需指定 $K$。对 $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{p_0}$，常用的选择有：

- 多项式核（polynomial kernel）$K(\boldsymbol{x}, \boldsymbol{y}) = (a\boldsymbol{x}^{\mathsf T}\boldsymbol{y} + c)^d$，$d \in \mathbb{N}_+$，$a > 0$，$c \ge 0$；在平面上取 $a = 1$、$c = 0$、$d = 2$，它恰好是上面特征 $(x_1^2, x_2^2, \sqrt2x_1x_2)$ 的内积；
- Gauss 核（Gaussian kernel），或称径向基函数（RBF）核，$K(\boldsymbol{x}, \boldsymbol{y}) = \exp\big(-\|\boldsymbol{x} - \boldsymbol{y}\|^2/(2\sigma^2)\big)$，其特征空间是无穷维的；
- sigmoid 核 $K(\boldsymbol{x}, \boldsymbol{y}) = \tanh(a\boldsymbol{x}^{\mathsf T}\boldsymbol{y} + r)$，实践中常用，但并非对所有参数值都半正定，所以一般不是正定核。

### 6.3.3. 算法

**算法 6.3.1（核主成分分析）** 给定观测 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$、正定核 $K$ 和维数 $k$：

1. 计算核矩阵 $K = [K(\boldsymbol{x}_i, \boldsymbol{x}_j)]_{n \times n}$；
2. 中心化：$\tilde K = HKH$；
3. 求 $\tilde K$ 最大的 $k$ 个特征值 $\lambda_1 \ge \cdots \ge \lambda_k > 0$ 及标准正交特征向量 $\boldsymbol{\alpha}_1, \dots, \boldsymbol{\alpha}_k$；
4. 输出核主成分得分组成的 $n \times k$ 矩阵 $[\sqrt{\lambda_1}\boldsymbol{\alpha}_1, \dots, \sqrt{\lambda_k}\boldsymbol{\alpha}_k]$。

这些得分就是对中心化特征向量 $\phi(\boldsymbol{x}_i) - \bar\phi$ 做普通主成分分析的得分，第 $j$ 个成分在特征空间中的方差为 $\lambda_j/n$。新点 $\boldsymbol{x}$ 通过同样中心化的核值 $K(\boldsymbol{x}, \boldsymbol{x}_i)$ 投影为 $\lambda_j^{-1/2}\boldsymbol{\alpha}_j^{\mathsf T}\tilde{\boldsymbol{k}}(\boldsymbol{x})$。R 中由 `kernlab::kpca()` 实现。

核主成分分析（kernel principal component analysis）是特征空间中的线性主成分分析，在原空间中则是非线性的。下面三个常见问题有助于理解这一构造。

**注 6.3.1** 核主成分分析也是做主成分分析，为什么是非线性的？数据先被映射到高维特征空间，再在那里做主成分分析。后一步确实是线性的，但映射 $\phi$ 可以是非线性的，所以得到的成分是原变量的非线性函数。

**注 6.3.2** $B$ 与 $D$ 都表示单元之间的相似性，但方向相反。$D$ 是距离：$d_{ij}$ 越大，单元越不相似。$B$ 仿照协方差矩阵定义：$b_{ij}$ 越接近 $0$，关联越弱。联系公式 $d_{ij}^2 = b_{ii} + b_{jj} - 2b_{ij}$ 体现了这种反向关系。

**注 6.3.3** 为什么算法在谱分解之前要把核矩阵中心化为 $HKH$？我们想要的是中心化特征的矩阵 $B$，它的行和与列和都为零：若 $\Phi$ 是未中心化的特征矩阵，则 $B = (H\Phi)(H\Phi)^{\mathsf T} = H\Phi\Phi^{\mathsf T}H$。核矩阵 $K$ 对应的是未中心化的 $\Phi\Phi^{\mathsf T}$，其行和、列和一般不为零，所以 $HKH$ 恰好就是我们需要的 $B$。

![平面上的两个同心圆环（左）：线性主成分分析只是旋转数据，第一主成分不能分开两个圆环（中）；而 Gauss 核的核主成分分析沿其第一主成分把它们分开（右）](./plots/kernel-pca-rings.py)

## 6.4. t-SNE

### 6.4.1. 投影与流形学习

当结构位于高维空间中一个弯曲的低维曲面（流形）上时，主成分分析这样的线性投影可能无法展示它：把"瑞士卷"投影到平面上，各层会叠在一起，而把它展开才能显示真正的二维结构。试图展开数据的方法称为流形学习。在把高维数据可视化到二维或三维的方法中，最流行的是 t 分布随机邻域嵌入（t-distributed stochastic neighbor embedding），简记 t-SNE（van der Maaten 与 Hinton，2008）。例如对 MNIST 手写数字，前两个主成分中各数字类别严重重叠，而 t-SNE 把大部分类别分成了不同的簇。

基本思想是：在低维空间中放置这些点，使高维空间中的邻域（簇）得以保持。t-SNE 从随机构形出发，每次把点移动一点；每个点受到原空间中与它相似的点的吸引，并受到其他点的排斥。

### 6.4.2. 方法

1. 原空间中的相似度。对点 $\boldsymbol{x}_i$，度量它到其他每个点的距离，并在以 $\boldsymbol{x}_i$ 为中心的正态密度下取值；归一化使相似度之和为 $1$，得到

   $$
   p_{j\mid i} = \frac{\exp\big(-\|\boldsymbol{x}_i - \boldsymbol{x}_j\|^2/(2\sigma_i^2)\big)}{\sum_{k \ne i}\exp\big(-\|\boldsymbol{x}_i - \boldsymbol{x}_k\|^2/(2\sigma_i^2)\big)}.
   $$

   远处的点相似度很小，近处的点相似度大。宽度 $\sigma_i$ 随 $\boldsymbol{x}_i$ 周围数据的密度而定，通过用户选择的困惑度（perplexity）设定，它大致是有效的邻居个数；归一化使稠密区域和稀疏区域中的点可以比较。然后对两个方向取平均，$p_{ij} = \frac{p_{j\mid i} + p_{i\mid j}}{2n}$。
2. 低维空间中的相似度。对低维点 $\boldsymbol{y}_1, \dots, \boldsymbol{y}_n$，用同样的方法计算相似度，但改用自由度为 $1$ 的 Student $t$ 分布（方法因此得名）：

   $$
   q_{ij} = \frac{(1 + \|\boldsymbol{y}_i - \boldsymbol{y}_j\|^2)^{-1}}{\sum_{k \ne l}(1 + \|\boldsymbol{y}_k - \boldsymbol{y}_l\|^2)^{-1}}.
   $$

   $t$ 分布的重尾允许中等不相似的点在低维图中相距较远，缓解了用正态核时点的"拥挤"，使簇分离得更清楚。
3. 匹配。用梯度下降移动各点 $\boldsymbol{y}_i$，使矩阵 $(q_{ij})$ 越来越像 $(p_{ij})$，即最小化 Kullback–Leibler 散度（Kullback–Leibler divergence）

   $$
   \mathrm{KL}(P\,\|\,Q) = \sum_{i \ne j}p_{ij}\log\frac{p_{ij}}{q_{ij}}.
   $$

简言之，t-SNE 把欧氏距离转换为表示相似度的概率，在高维空间中构造对象两两之间的一个概率分布，在低维空间中构造另一个，并使两者尽可能接近。

**注 6.4.1** t-SNE 只是借用了单元之间相似度的思想：它在两个空间中都刻画相似度（高维空间中是固定的，低维空间中是待求的），通过匹配它们找到合适的低维展示。它并不使用多维标度中的邻近矩阵 $D$、矩阵 $B$ 或主成分得分。

![1797 幅手写数字图像（8 x 8 像素，p = 64）按前两个主成分（左）和 t-SNE（右）展示，按数字着色：t-SNE 把大部分数字类别分成了不同的簇](./plots/pca-vs-tsne.py)

### 6.4.3. 优点与局限

t-SNE 专为把高维数据在低维中可视化而设计，实现广泛（例如 R 包 `tsne`）。它的局限是：

- 没有显式的映射，不能直接用于新数据；
- 倾向于保持局部结构；图中簇之间的距离和簇的大小没有意义，本质上高维的数据无法很好地表示在二维或三维中；
- 速度慢；原始维数很高时，通常先做主成分分析，再做 t-SNE。

目标相近的较新方法有 UMAP（Uniform Manifold Approximation and Projection，McInnes 等，2018；R 包 `umap`），它更快，并能保留更多的全局结构。

## 小结

- 主成分分析可以逐个方向地表述，也可以对整个子空间表述（距离最小或散布最大），三者给出相同的成分。它通过中心化数据矩阵的奇异值分解 $\tilde X = U\Gamma V^{\mathsf T}$ 计算：特征向量为 $V$，得分为 $U\Gamma$；奇异值分解比 $\tilde X^{\mathsf T}\tilde X$ 的特征值分解更精确。
- 多维标度用低维构形表示 $n \times n$ 邻近矩阵 $D$。经典多维标度构造 $B = HAH$（$a_{ij} = -\frac12d_{ij}^2$），取 $P_k\Lambda_k^{1/2}$；$D$ 是欧氏的当且仅当 $B$ 半正定；对欧氏距离，经典多维标度重现主成分得分（主坐标分析）。
- 核主成分分析用正定核代替数据的内积，把核矩阵中心化为 $HKH$ 再分解：这是在从不显式计算的特征空间中的主成分分析，对原变量是非线性的。
- t-SNE 通过最小化 Kullback–Leibler 散度，匹配原空间（正态核）与低维图（$t$ 核）中的邻域概率；它是可视化工具，而不是通用的投影方法。
