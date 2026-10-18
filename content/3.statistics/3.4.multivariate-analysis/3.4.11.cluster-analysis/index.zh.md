---
title: 聚类分析
description: 不同连接方式的层次聚类、k 均值及其变体、聚类数目的选择、用 EM 算法拟合的高斯混合模型，以及基于 BIC 的模型选择。
source_hash: e700ffd41cc2
---

判别分析（[3.4.10](/3.4.10)）从类别已知的观测中学习分类规则。聚类分析在没有标签的情况下提出同样的问题：只凭测量值，数据中是否存在自然的类？哪些观测属于同一类？它是无监督学习的基本工具。本章介绍三大类方法：层次聚类，从距离矩阵出发构建一棵嵌套类的树；划分方法，如 $k$ 均值，最小化某个类内准则；基于模型的聚类，用 EM 算法拟合**多元正态分布**的混合，并把聚类数目的选择变成模型选择问题。基于模型的聚类是上一章正态理论判别分析的无监督版本：模型相同，只是标签缺失了。全章都会用到观测之间的距离（[3.4.1](/3.4.1)）以及用于可视化的**多维标度**（[3.4.6](/3.4.6)）。

## 11.1. 引言

再看鸢尾花数据，假设品种标签丢失了：只凭四项测量能否发现这些类？或者考虑一项约 2000 名受试者的脑成像研究，全脑 47473 个体素中约有 12000 个被激活，分属 26 个解剖区域。这里有两个问题：26 个区域之间是什么关系？一个感兴趣的区域（如脑岛）能否分成功能不同的子区域？第一个问题是对变量（区域）分组，第二个是对单元（体素）分组；聚类分析两者都能处理。

类是一组对象，同一类中的对象彼此相似（或相关），与其他类中的对象不相似（或无关）。聚类分析（cluster analysis）也称聚类、数据分割，在网络中称社区发现；它根据对象的测量特征找出它们之间的相似性，并把相似的对象归为一类，使类内距离小、类间距离大。这里没有预先定义的类：聚类是无监督学习（unsupervised learning），即从观测中学习；判别分析则是有监督学习（supervised learning），即从带标签的样例中学习。

聚类分析有两种用途：

- 理解：作为独立工具，洞察数据的分布，例如把相关的文档归类以便浏览，或把功能相似的基因与蛋白质归类；
- 概括：作为后续分析的预处理步骤，把大数据集化简为少数几个有代表性的组。

主要方法有：

| 方法 | 思路 | 典型方法 |
|---|---|---|
| 层次方法 | 按某个准则构造数据的层次分解 | AGNES、DIANA、BIRCH、CHAMELEON |
| 划分方法 | 构造若干划分，再按某个准则评价 | $k$ 均值、$k$ 中心点、CLARANS |
| 基于模型的方法 | 为每一类假设一个模型，求最佳拟合 | 用 EM 拟合的高斯混合、SOM、COBWEB |

## 11.2. 层次聚类

### 11.2.1. 凝聚聚类与分裂聚类

层次聚类（hierarchical clustering）给出一组按树组织起来的嵌套类。这棵树用树状图（dendrogram）表示，它是记录合并或分裂次序的树形图：叶子是观测，两条分支相接处的高度是被合并的两类之间的距离。层次聚类主要有两种。

- 凝聚：从每个点自成一类开始，每一步合并最近的两类，直到只剩一类（或 $k$ 类）。
- 分裂：从包含全部点的一类开始，每一步分裂一类，直到每类只含一个点（或得到 $k$ 类）。

凝聚聚类远为常用，本节其余部分都讨论它。为了量化"接近"，它使用距离（或相异度）矩阵，需要做两个选择：点与点之间的距离，以及由点间距离定义的类与类之间的距离。

### 11.2.2. 点与点之间的距离

点间距离要与数据类型相适应：数值型数据用欧氏距离（或 Mahalanobis 距离）；关注剖面的形状而非水平时用 $1 - r$，$r$ 为相关系数；二元或分类数据用 Jaccard 距离或 Hamming 距离。对文本和其他稀疏高维数据，向量之间的夹角是一个自然的度量。

**定义 11.2.1（余弦相似度）** 两个非零向量 $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^p$ 的**余弦相似度**为

$$
\cos(\boldsymbol{a}, \boldsymbol{b}) = \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\|\boldsymbol{a}\|\,\|\boldsymbol{b}\|} \in [-1, 1],
$$
$1 - \cos(\boldsymbol{a}, \boldsymbol{b}) \in [0, 2]$ 是相应的相异度。

例如，一篇文档可以表示为词表中各词（加权）频率组成的向量；大部分分量为 $0$，余弦相似度比较的是用词的比例，而与文档长短无关。对中心化的向量，余弦相似度就是相关系数。

### 11.2.3. 类与类之间的距离

**定义 11.2.2（连接方式）** 设 $d(\boldsymbol{x}, \boldsymbol{y})$ 为点间距离，$A, B$ 是两个不相交的类，分别含 $\lvert A\rvert, \lvert B\rvert$ 个点，重心（均值向量）为 $\boldsymbol{m}_A, \boldsymbol{m}_B$。$A$ 与 $B$ 之间的距离由连接方式定义：

1. **单连接**（最小）：$d(A, B) = \min_{\boldsymbol{x}\in A, \boldsymbol{y}\in B} d(\boldsymbol{x}, \boldsymbol{y})$，即最近一对点的距离；
2. **全连接**（最大）：$d(A, B) = \max_{\boldsymbol{x}\in A, \boldsymbol{y}\in B} d(\boldsymbol{x}, \boldsymbol{y})$，即最远一对点的距离；
3. **平均连接**（组平均）：$d(A, B) = \frac{1}{\lvert A\rvert\lvert B\rvert}\sum_{\boldsymbol{x}\in A}\sum_{\boldsymbol{y}\in B} d(\boldsymbol{x}, \boldsymbol{y})$；
4. **重心连接**：$d(A, B) = \|\boldsymbol{m}_A - \boldsymbol{m}_B\|$，即两个重心之间的距离；
5. **Ward 法**：$d(A, B)$ 是合并 $A$ 与 $B$ 所引起的类内误差平方和的增量（见下文）。

Ward 法用类内误差平方和度量合并的代价。对划分为 $C_1, \dots, C_K$、中心为 $\boldsymbol{m}_1, \dots, \boldsymbol{m}_K$ 的一组类，一个点的误差是它到所在类中心的距离，

$$
\mathrm{SSE} = \sum_{i=1}^K\sum_{\boldsymbol{x}\in C_i}\|\boldsymbol{x} - \boldsymbol{m}_i\|^2.
$$
Ward 法合并使 SSE 增加最少的一对类，也就是在所有类对之间比较 $\mathrm{SSE}_{A\cup B} - \mathrm{SSE}_A - \mathrm{SSE}_B$。简单的计算（把合并后关于新重心的总平方和分解为类内与类间两部分）给出

$$
\mathrm{SSE}_{A\cup B} - \mathrm{SSE}_A - \mathrm{SSE}_B = \frac{\lvert A\rvert\,\lvert B\rvert}{\lvert A\rvert + \lvert B\rvert}\|\boldsymbol{m}_A - \boldsymbol{m}_B\|^2,
$$
即按类大小加权的重心距离，它会抑制两个大类的合并。

### 11.2.4. 凝聚算法

**算法 11.2.1（凝聚层次聚类）** 给定 $n$ 个点、点间距离与连接方式：

1. 令每个数据点自成一类；
2. 计算 $n \times n$ 距离矩阵；
3. 重复：合并最近的两类，并计算新类到其他各类的距离，更新距离矩阵；
4. 直到只剩一类。

树状图按次序画出各次合并，每次合并画在其发生时的距离高度上。要得到 $k$ 类，用一条恰好穿过 $k$ 条竖直分支的水平线截断树状图，截线下方的子树就是各类。聚类数目不必事先确定：在不同高度截断即可得到任意个数的类。

**例 11.2.1** 用欧氏距离和重心连接对六个点 $(0,0)$、$(1,2)$、$(2,1)$、$(4,1)$、$(5.2,0)$、$(5,3)$ 聚类。

1. 最近的一对是 $(1,2)$ 与 $(2,1)$，距离 $\sqrt2 \approx 1.414$；合并为重心 $(1.5, 1.5)$ 的一类。
2. 接着 $(4,1)$ 与 $(5.2,0)$ 以距离 $\sqrt{2.44} \approx 1.562$ 合并，重心 $(4.6, 0.5)$。
3. 现在最近的是 $(0,0)$ 与重心 $(1.5,1.5)$，距离 $\approx 2.121$；新的三点类重心为 $(1, 1)$。
4. 然后 $(5,3)$ 以距离 $\approx 2.532$ 并入重心为 $(4.6, 0.5)$ 的类，新重心为 $(4.73, 1.33)$。
5. 最后两类以距离 $\lVert(1,1) - (4.73,1.33)\rVert \approx 3.748$ 合并；六个点的重心为 $(2.87, 1.17)$。

在高度 $2.53$ 与 $3.75$ 之间截断树状图，得到两类 $\{(0,0), (1,2), (2,1)\}$ 与 $\{(4,1), (5.2,0), (5,3)\}$。注意合并后的类的重心是两个重心的加权平均，而不是它们的中点。

![例中的六个点（左）与重心连接凝聚聚类的树状图（右）；虚线把树截为两类。](./plots/six-point-dendrogram.py)

### 11.2.5. 各种连接方式的比较

不同的连接方式产生形状不同的类。

| 连接方式 | 优点 | 缺点 |
|---|---|---|
| 单连接 | 能较自然地处理形状不规则（非椭圆）的类 | 对噪声和离群点敏感，会产生"链式效应"：通过中间点连成细长松散的类 |
| 全连接 | 对噪声和离群点不太敏感；类紧凑 | 偏向球形的类，可能违背"接近"（一个点离相邻类中某些点比离本类的点近得多），表现为打散大类 |
| 平均连接 | 介于单连接与全连接之间：像全连接一样得到球形类，对噪声又比单连接不敏感 | |
| Ward 法 | 当相异度取距离平方时与平均连接相似；是 $k$ 均值的层次版本，有时用于 $k$ 均值的初始化 | 偏向大小相近的球形类 |

**例 11.2.2** 对鸢尾花数据用欧氏距离（R 中为 `hclust(dist(iris[, -5]), method)`，再用 `cutree(res, k = 3)`），单连接能分出 setosa，但把除两个离群点外的全部 versicolor 与 virginica 链成一类，三个类的大小为 $50$、$98$ 和 $2$。全连接、平均连接和 Ward 法给出的树状图分支更均衡，也都分出了 setosa。平均连接和 Ward 法大体按品种划分其余的花，约有 $15$ 朵 virginica 被归入 versicolor；全连接则把 versicolor 打散成两部分，正是"打散大类"的缺点。

![鸢尾花数据（欧氏距离）在四种连接方式下的树状图。单连接表现出链式效应；其余三种都有清楚的 setosa 分支和另外两组。](./plots/iris-linkage-dendrograms.py)

**例 11.2.3** 在脑成像研究中，用 $1 - r$（$r$ 为两个区域在 1709 名受试者上激活程度的相关系数）和平均连接对 26 个脑区聚类。把树截为六类后，同时激活的区域归在一起，例如同一结构的左右两部分，以及壳核与苍白球。

### 11.2.6. 优点、局限与推广

凝聚聚类不需要事先给定聚类数目，因为在适当高度截断树状图就能得到任意个数的类；树状图还直观地展示了对象之间的关系，例如生物学家用来表示物种进化关系的系统发生树。

它的局限有计算上的，也有统计上的。

- 距离矩阵需要 $O(n^2)$ 的空间，直接的算法需要 $O(n^3)$ 的时间：共 $n$ 步，每一步都要搜索并更新一个 $n^2$ 规模的矩阵。
- 合并一旦做出就不能撤销。
- 没有直接最小化任何目标函数。
- 视连接方式而定，它或对噪声和离群点敏感，或难以处理大小不同、形状非凸的类，或会打散大类。

**注 11.2.1** 立方阶的运行时间并不是本质的。单连接聚类等价于在以距离为权的完全图上构造最小生成树，用 Prim 算法只需 $O(n^2)$ 时间。对全连接、平均连接与 Ward 法，朴素算法有大量重复计算，用最近邻链算法也能达到 $O(n^2)$。

一些推广针对这些局限：BIRCH（1996）用 CF 树（聚类特征树）概括数据并增量地调整子类，运行时间为 $O(n)$；CHAMELEON（1999）用动态建模合并类，能处理形状复杂的类。

## 11.3. 划分聚类：k 均值

### 11.3.1. 算法

划分聚类（partitioning clustering）把数据分成互不重叠的子集（类），使每个对象恰好属于一个子集。最常用的划分方法是 $k$ 均值。

**算法 11.3.1（k 均值聚类）** 给定 $n$ 个点和聚类数目 $k$：

1. 选择 $k$ 个初始重心；
2. 重复：把每个点分到离它最近的重心所在的类，并把每一类的重心更新为该类各点的均值；
3. 直到分配不再改变。

使用 $k$ 均值需要给定聚类数目 $k$、点间距离（通常为欧氏距离，也用基于相关系数的距离）以及初始重心。初始化的常见做法有：随机选 $k$ 个数据点；对数据的一个样本做层次聚类，取各类均值；或随机选一个点，再依次选 $k-1$ 个点，每个都尽量远离已选的点（例如 leader 算法，要求每个新中心与已有中心的距离至少为 $d$）。结果可能强烈依赖于初值，所以实践中从许多随机初值出发运行 $k$ 均值，保留 SSE 最小的解。

### 11.3.2. 目标函数

设 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ 为数据，$\boldsymbol{\mu}_1, \dots, \boldsymbol{\mu}_k$ 为各类重心，$c_i \in \{1, \dots, k\}$ 为 $\boldsymbol{x}_i$ 所属的类。总 SSE

$$
J(c, \boldsymbol{\mu}) = \sum_{i=1}^n\|\boldsymbol{x}_i - \boldsymbol{\mu}_{c_i}\|^2
$$
就是 $k$ 均值所最小化的目标，算法 11.3.1 是对它的坐标下降：

1. 给定 $\boldsymbol{\mu}$ 优化 $c$：$c_i = \arg\min_j\|\boldsymbol{x}_i - \boldsymbol{\mu}_j\|^2$（分配步）；
2. 给定 $c$ 优化 $\boldsymbol{\mu}$：$\boldsymbol{\mu}_j = \arg\min_{\boldsymbol{\mu}}\sum_{i : c_i = j}\|\boldsymbol{x}_i - \boldsymbol{\mu}\|^2$，即第 $j$ 类各点的均值（更新步）。

**命题 11.3.1** 算法 11.3.1 的每一步都不增大 $J$，算法在有限次迭代后终止于一个用任一步单独都无法改进的划分。这是 $J$ 的局部极小，不保证是全局极小。

**证明** 分配步在 $\boldsymbol{\mu}$ 固定时对 $c$ 最小化 $J$；更新步在 $c$ 固定时对 $\boldsymbol{\mu}$ 最小化 $J$，因为 $\sum_{i\in C}\|\boldsymbol{x}_i - \boldsymbol{\mu}\|^2 = \sum_{i\in C}\|\boldsymbol{x}_i - \bar{\boldsymbol{x}}_C\|^2 + \lvert C\rvert\,\|\bar{\boldsymbol{x}}_C - \boldsymbol{\mu}\|^2$ 在类均值 $\bar{\boldsymbol{x}}_C$ 处最小。所以 $J$ 不增。划分只有有限多个，并且（以一致的方式处理平局时）$J$ 严格下降之后先前的划分不会再出现，因此有限次迭代后分配不再改变。$\square$

### 11.3.3. 选择 k

选择 $k$ 是一种权衡：类太少时许多点离重心很远；类太多时再增加类几乎不减小平均距离。单看 SSE 无法决定，因为它随 $k$ 增大而减小，每个点自成一类时为 $0$。常用的方法如下。

1. 肘部法则（elbow method）：画出最小 SSE 随 $k$ 变化的曲线；它在某个 $k$ 之前迅速下降，之后变化很小，取曲线的拐点作为 $k$。
2. 经验法则：$n$ 个点取 $k \approx \sqrt{n/2}$，例如 $n = 200$ 时 $k = 10$。
3. 轮廓系数（定义 11.3.1）：取使所有点的平均轮廓系数最大的 $k$。
4. 间隙统计量（gap statistic）（Tibshirani、Walther 与 Hastie，2001）：把 $\ln\mathrm{SSE}_k$ 与它在无聚类结构的参照分布下的期望比较，取间隙大的 $k$（R 中为 `cluster::clusGap`）。
5. 交叉验证：把数据分成 $m$ 份，用 $m-1$ 份得到聚类，用剩下的一份检验聚类的质量（例如留出的点相对于拟合重心的 SSE），对每个 $k$ 重复 $m$ 次，取总体质量最好的 $k$。

**定义 11.3.1（轮廓系数）** 对一个聚类结果和相异度 $d$，记 $C(i)$ 为点 $i$ 所在的类。令

$$
a(i) = \frac{1}{\lvert C(i)\rvert - 1}\sum_{j\in C(i), j\ne i} d(i, j)
$$
为 $i$ 到本类其他点的平均相异度，

$$
b(i) = \min_{C \ne C(i)}\frac{1}{\lvert C\rvert}\sum_{j\in C} d(i, j)
$$
为 $i$ 到最近的其他类的平均相异度。点 $i$ 的**轮廓系数**为

$$
s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}} \in [-1, 1].
$$

接近 $1$ 表示该点离本类比离次近的类近得多；接近 $0$ 表示它位于两类之间；负值说明它可能被分错了类。

**例 11.3.1** 对鸢尾花数据，`kmeans(iris[, -5], 3)` 得到三类，但不同的随机初值可能给出不同的划分。为了可视化，用经典多维标度（`cmdscale`）把四维数据投影到二维，按类着色；与品种对照，setosa 自成一类，versicolor 与 virginica 部分混在一起。

**例 11.3.2** 在脑成像研究中，以平均连接层次聚类的各类均值为初始中心，用相关系数距离对脑岛的 650 个体素做 $k$ 均值聚类。类内 SSE 随聚类数目变化的曲线在 $k = 3$ 处出现肘部，三个子区域分别与不同的功能相关：抑制与反应时间、目标导向的认知、情绪（如看到厌恶的面孔）。

### 11.3.4. 优点、局限与推广

$k$ 均值很高效：$n$ 个对象、$k$ 类、$t$ 次迭代的计算量为 $O(tkn)$，通常 $k, t \ll n$。它的局限是：

1. 对离群点敏感，因为单个点就能把均值拉得很远；
2. 各类大小不同、密度不同或形状非凸时效果不好，因为它隐含地寻找散布相近的球形类；
3. 必须事先给定 $k$，结果依赖于初值。

一些变体针对其中的问题。

- $k$ 众数用众数代替各类的均值，因而能处理分类数据。
- $k$ 中心点用中心点代替重心：一类的中心点是与本类其他成员距离总和最小的观测。它用同样的交替算法计算，但中心总是某个观测，这在例如特征取 $0$ 或 $1$ 时很有用，也降低了对离群点的敏感性。PAM（Partitioning Around Medoids；Kaufman 与 Rousseeuw，1987）实现了这一方法；R 中的 `cluster::pam` 用欧氏距离而非其平方。CLARA（1990）对大数据集的样本应用 PAM，CLARANS（Ng 与 Han，1994）使用随机搜索。

## 11.4. 基于模型的聚类

### 11.4.1. 高斯混合模型

层次聚类、$k$ 均值等算法在很大程度上是启发式的，不以正式模型为基础，因而无法进行正式的推断。这不一定是缺点，因为聚类主要是探索性的；但基于模型的聚类提供了另一种选择。它假设观测来自两个或更多成分的混合，每个成分用一个密度函数和它在混合中的先验概率（权重）描述一类。原则上可以采用任何概率模型，通常取多元正态分布。

**定义 11.4.1（高斯混合模型）** 设 $Y \sim \mathrm{Mult}(1, \boldsymbol{\pi})$ 是以概率 $\pi_l$ 取值 $l \in \{1, \dots, k\}$ 的隐标签，$\sum_l\pi_l = 1$，且 $\boldsymbol{X} \mid Y = l \sim \mathcal{N}_p(\boldsymbol{\mu}_l, \Sigma_l)$。$\boldsymbol{X}$ 的分布，即密度为

$$
f(\boldsymbol{x}) = \sum_{l=1}^k\pi_l\,\phi(\boldsymbol{x}; \boldsymbol{\mu}_l, \Sigma_l)
$$
的分布（$\phi(\cdot\,; \boldsymbol{\mu}, \Sigma)$ 为 $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ 的密度），称为**高斯混合模型**（GMM）；$\pi_l$ 称为混合比例。

这就是 [3.4.10](/3.4.10) 中 QDA 的模型（若所有 $\Sigma_l$ 相等则是 LDA 的模型），先验为 $\pi_l$，各类密度为 $\phi(\cdot\,; \boldsymbol{\mu}_l, \Sigma_l)$；不同之处在于标签 $Y_i$ 丢失了，只观测到 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ 组成的 $n \times p$ 数据矩阵。目标是估计 $\boldsymbol{\pi}$ 与 $(\boldsymbol{\mu}_l, \Sigma_l)$（$1 \le l \le k$），再把每个观测分到后验概率最大的成分。由于每个观测得到的是属于各类的概率而不是单一标签，基于模型的聚类称为软聚类（soft clustering），层次聚类与 $k$ 均值则是硬聚类（hard clustering）。

$\boldsymbol{\theta} = (\boldsymbol{\pi}, \boldsymbol{\mu}_1, \dots, \boldsymbol{\mu}_k, \Sigma_1, \dots, \Sigma_k)$ 的**似然函数**为

$$
L(\boldsymbol{\theta}) = \prod_{i=1}^n\sum_{l=1}^k\pi_l\,\phi(\boldsymbol{x}_i; \boldsymbol{\mu}_l, \Sigma_l) = \text{常数}\cdot\prod_{i=1}^n\sum_{l=1}^k\pi_l\lvert\Sigma_l\rvert^{-1/2}\exp\left\{-\frac12(\boldsymbol{x}_i-\boldsymbol{\mu}_l)^{\mathsf T}\Sigma_l^{-1}(\boldsymbol{x}_i-\boldsymbol{\mu}_l)\right\},
$$
**对数似然函数**为

$$
\ell(\boldsymbol{\theta}) = \sum_{i=1}^n\ln f(\boldsymbol{x}_i; \boldsymbol{\theta}) = \sum_{i=1}^n\ln\sum_{l=1}^k f(\boldsymbol{x}_i \mid Y_i = l; \boldsymbol{\mu}_l, \Sigma_l)\,\mathbb{P}(Y_i = l; \boldsymbol{\pi}).
$$
对数里面的和把所有参数耦合在一起，难以直接求这些参数的**极大似然估计**。

### 11.4.2. 思路：一维两类

考虑来自 $k = 2$ 个正态分布混合的观测 $x_1, \dots, x_n$，均值与方差未知，把两个成分记为 $A$（$Y = 1$）与 $B$（$Y = 2$）。

如果知道每个观测属于哪一类，估计就很简单。设 $n = 10$，前五个观测属于 $A$。用示性变量 $\boldsymbol{1}_{\{Y_i = 1\}}$（$i \le 5$ 时为 $1$，$i > 5$ 时为 $0$），

$$
\hat\pi_1 = \frac{n_1}{n} = \frac{5}{10}, \qquad \hat\mu_1 = \frac{\sum_i\boldsymbol{1}_{\{Y_i=1\}}x_i}{\sum_i\boldsymbol{1}_{\{Y_i=1\}}} = \frac{x_1 + \cdots + x_5}{5}, \qquad \hat\sigma_1^2 = \frac{\sum_i\boldsymbol{1}_{\{Y_i=1\}}(x_i - \hat\mu_1)^2}{\sum_i\boldsymbol{1}_{\{Y_i=1\}}},
$$
$B$ 类同理。

如果不知道类别，但知道两个正态分布的参数，就可以由 **Bayes 公式**算出每个点属于 $A$ 或 $B$ 的可能性：

$$
\gamma_{i1} = \mathbb{P}(Y = 1 \mid X = x_i) = \frac{\pi_1 f_1(x_i)}{\pi_1 f_1(x_i) + \pi_2 f_2(x_i)}, \qquad f_1(x_i) = \frac{1}{\sqrt{2\pi\sigma_1^2}}\exp\left\{-\frac{(x_i-\mu_1)^2}{2\sigma_1^2}\right\},
$$
$\gamma_{i2} = 1 - \gamma_{i1}$。设 $Y = 1$ 的这些后验概率为 $0.9, 0.8, 0.7, 0.6, 0.6, 0.3, 0.2, 0.2, 0.2, 0.1$。用它们代替未知的示性变量，得到加权估计：

$$
\hat\pi_1 = \frac{\sum_i\gamma_{i1}}{n} = \frac{4.6}{10}, \qquad \hat\mu_1 = \frac{0.9x_1 + 0.8x_2 + \cdots + 0.1x_{10}}{4.6}, \qquad \hat\sigma_1^2 = \frac{0.9(x_1-\hat\mu_1)^2 + \cdots + 0.1(x_{10}-\hat\mu_1)^2}{4.6}.
$$

两步互相提供输入：参数（类的特征，总体层面）给出隶属概率，隶属概率（点的特征，样本层面）给出参数。交替迭代两者，就是 EM 算法。

### 11.4.3. 高斯混合的 EM 算法

一般地，对 $p$ 维的 $k$ 类，把隶属概率排成 $n \times k$ 矩阵 $\Gamma = [\gamma_{il}]$，$\gamma_{il} = \mathbb{P}(Y_i = l \mid \boldsymbol{X}_i = \boldsymbol{x}_i)$。

**算法 11.4.1（高斯混合的 EM 算法）** 初始化 $\hat{\boldsymbol{\pi}}^{(0)}$、$\hat{\boldsymbol{\mu}}_l^{(0)}$、$\hat\Sigma_l^{(0)}$。对 $t = 0, 1, 2, \dots$ 直到收敛：

1. （期望步）对 $i = 1, \dots, n$，$l = 1, \dots, k$，
   $$
   \hat\gamma_{il}^{(t+1)} = \mathbb{P}\bigl(Y_i = l \mid \boldsymbol{X}_i = \boldsymbol{x}_i; \hat{\boldsymbol{\pi}}^{(t)}, \hat{\boldsymbol{\mu}}^{(t)}, \hat\Sigma^{(t)}\bigr) = \frac{\hat\pi_l^{(t)}\phi(\boldsymbol{x}_i; \hat{\boldsymbol{\mu}}_l^{(t)}, \hat\Sigma_l^{(t)})}{\sum_{j=1}^k\hat\pi_j^{(t)}\phi(\boldsymbol{x}_i; \hat{\boldsymbol{\mu}}_j^{(t)}, \hat\Sigma_j^{(t)})};
   $$
2. （最大化步）对 $l = 1, \dots, k$，
   $$
   \hat\pi_l^{(t+1)} = \frac{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}}{n}, \qquad \hat{\boldsymbol{\mu}}_l^{(t+1)} = \frac{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}\boldsymbol{x}_i}{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}}, \qquad \hat\Sigma_l^{(t+1)} = \frac{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}(\boldsymbol{x}_i - \hat{\boldsymbol{\mu}}_l^{(t+1)})(\boldsymbol{x}_i - \hat{\boldsymbol{\mu}}_l^{(t+1)})^{\mathsf T}}{\sum_{i=1}^n\hat\gamma_{il}^{(t+1)}},
   $$
   即以 $\hat\gamma_{il}^{(t+1)}$ 为权的加权比例、加权平均与加权协方差矩阵。

把这些更新与标签已观测的判别分析中的估计比较：

| | 硬：观测到的 $Y$（QDA） | 软：猜测的 $Y$（聚类） |
|---|---|---|
| 比例 | $\hat\pi_l = \frac1n\sum_i\boldsymbol{1}_{\{Y_i=l\}}$ | $\hat\pi_l = \frac1n\sum_i\hat\gamma_{il}$ |
| 均值 | $\hat{\boldsymbol{\mu}}_l = \frac{\sum_i\boldsymbol{1}_{\{Y_i=l\}}\boldsymbol{x}_i}{\sum_i\boldsymbol{1}_{\{Y_i=l\}}}$ | $\hat{\boldsymbol{\mu}}_l = \frac{\sum_i\hat\gamma_{il}\boldsymbol{x}_i}{\sum_i\hat\gamma_{il}}$ |
| 协方差 | $\hat\Sigma_l = \frac{\sum_i\boldsymbol{1}_{\{Y_i=l\}}(\boldsymbol{x}_i-\hat{\boldsymbol{\mu}}_l)(\boldsymbol{x}_i-\hat{\boldsymbol{\mu}}_l)^{\mathsf T}}{\sum_i\boldsymbol{1}_{\{Y_i=l\}}}$ | $\hat\Sigma_l = \frac{\sum_i\hat\gamma_{il}(\boldsymbol{x}_i-\hat{\boldsymbol{\mu}}_l)(\boldsymbol{x}_i-\hat{\boldsymbol{\mu}}_l)^{\mathsf T}}{\sum_i\hat\gamma_{il}}$ |

$\Gamma$ 中的量并不真是参数：它们是未观测的随机标签 $Y_i$ 的估计。如果观测到了 $Y$，$\Gamma$ 的每一行除一个 $1$ 外全为零，$\pi_l, \boldsymbol{\mu}_l, \Sigma_l$ 的估计就恰好是 QDA 中的估计。EM 只是用一个猜测代替未观测的 $Y$。在所有成分的协方差矩阵都是 $\sigma^2 I$ 且 $\sigma \to 0$ 的极限下，后验概率变成 $0$ 或 $1$（每个点分给最近的均值），EM 退化为 $k$ 均值。

### 11.4.4. 一般的 EM 算法

算法 11.4.1 是 EM 算法（EM algorithm）的特例。EM 即期望—最大化（expectation–maximization），是含缺失数据时求极大似然估计的一般方法。原始目标是最大化

$$
\ell(\boldsymbol{\theta}) = \sum_{i=1}^n\ln\sum_{l=1}^k f(\boldsymbol{x}_i \mid Y_i = l; \boldsymbol{\theta})\,\mathbb{P}(Y_i = l; \boldsymbol{\theta}).
$$
借助缺失的示性变量 $\delta_{il} = \boldsymbol{1}_{\{Y_i = l\}}$ 改写：若它们被观测到，完全数据对数似然为

$$
\ell(\boldsymbol{\delta}, \boldsymbol{\theta}) = \sum_{i=1}^n\ln\prod_{l=1}^k\bigl[\pi_l f_l(\boldsymbol{x}_i; \boldsymbol{\mu}_l, \Sigma_l)\bigr]^{\delta_{il}} = \sum_{i=1}^n\sum_{l=1}^k\delta_{il}\bigl[\ln\pi_l + \ln f_l(\boldsymbol{x}_i; \boldsymbol{\mu}_l, \Sigma_l)\bigr],
$$
它分解为简单的项。由于 $\boldsymbol{\delta}$ 未知，EM 交替进行两步，记当前值为 $\boldsymbol{\theta}^{(t)} = (\boldsymbol{\pi}^{(t)}, \boldsymbol{\mu}^{(t)}, \Sigma^{(t)})$：

1. E 步：计算 $\mathbb{E}[\boldsymbol{\delta} \mid \boldsymbol{\theta}^{(t)}, \boldsymbol{X}]$，得到 $\gamma^{(t+1)}$，从而
   $$
   B(\boldsymbol{\theta}; \boldsymbol{\theta}^{(t)}) = \mathbb{E}_{\boldsymbol{\delta}\mid\boldsymbol{\theta}^{(t)}, \boldsymbol{X}}\bigl[\ell(\boldsymbol{\delta}, \boldsymbol{\theta})\bigr] = \sum_{i=1}^n\sum_{l=1}^k\gamma_{il}^{(t+1)}\bigl[\ln\pi_l + \ln f_l(\boldsymbol{x}_i; \boldsymbol{\mu}_l, \Sigma_l)\bigr];
   $$
2. M 步：$\boldsymbol{\theta}^{(t+1)} = \arg\max_{\boldsymbol{\theta}} B(\boldsymbol{\theta}; \boldsymbol{\theta}^{(t)})$。

对高斯混合，最大化 $B$ 恰好给出算法 11.4.1 的加权估计。为什么最大化 $B$ 能使 $\ell$ 增大？$B$ 有三个性质：它的最大值点容易求；在相差一个常数的意义下它是 $\ell$ 的下界；这个下界在当前值处是紧的。

**定理 11.4.1（EM 的上升性）** 对一切 $\boldsymbol{\theta}$，$\ell(\boldsymbol{\theta}) \ge \tilde B(\boldsymbol{\theta}, \boldsymbol{\theta}^{(t)})$，其中

$$
\tilde B(\boldsymbol{\theta}, \boldsymbol{\theta}^{(t)}) = \ell(\boldsymbol{\theta}^{(t)}) + \sum_{l=1}^k\mathbb{P}(Y = l \mid \boldsymbol{x}, \boldsymbol{\theta}^{(t)})\ln\frac{f(\boldsymbol{x} \mid Y = l, \boldsymbol{\theta})\,\mathbb{P}(Y = l \mid \boldsymbol{\theta})}{\mathbb{P}(Y = l \mid \boldsymbol{x}, \boldsymbol{\theta}^{(t)})\,f(\boldsymbol{x} \mid \boldsymbol{\theta}^{(t)})}
$$
（这里写的是 $n = 1$ 的情形；$n > 1$ 时在对数之外对 $i$ 求和），等号在 $\boldsymbol{\theta} = \boldsymbol{\theta}^{(t)}$ 处成立。此外 $\tilde B(\boldsymbol{\theta}, \boldsymbol{\theta}^{(t)}) - B(\boldsymbol{\theta}; \boldsymbol{\theta}^{(t)})$ 与 $\boldsymbol{\theta}$ 无关，所以 M 步也最大化 $\tilde B$，从而 $\ell(\boldsymbol{\theta}^{(t+1)}) \ge \ell(\boldsymbol{\theta}^{(t)})$。

**证明** 记 $q_l = \mathbb{P}(Y = l \mid \boldsymbol{x}, \boldsymbol{\theta}^{(t)})$，它是 $l$ 上的一个概率分布。则

$$
\begin{aligned}
\ell(\boldsymbol{\theta}) - \ell(\boldsymbol{\theta}^{(t)}) &= \ln\left(\sum_{l=1}^k q_l\,\frac{f(\boldsymbol{x} \mid Y = l, \boldsymbol{\theta})\,\mathbb{P}(Y = l \mid \boldsymbol{\theta})}{q_l}\right) - \ln f(\boldsymbol{x} \mid \boldsymbol{\theta}^{(t)}) \\
&\ge \sum_{l=1}^k q_l\ln\frac{f(\boldsymbol{x} \mid Y = l, \boldsymbol{\theta})\,\mathbb{P}(Y = l \mid \boldsymbol{\theta})}{q_l} - \ln f(\boldsymbol{x} \mid \boldsymbol{\theta}^{(t)}) = \tilde B(\boldsymbol{\theta}, \boldsymbol{\theta}^{(t)}) - \ell(\boldsymbol{\theta}^{(t)}),
\end{aligned}
$$
这里对凹函数 $\ln$ 用了 **Jensen 不等式**，并利用 $\sum_l q_l = 1$ 把 $\ln f(\boldsymbol{x}\mid\boldsymbol{\theta}^{(t)})$ 移入求和号内。在 $\boldsymbol{\theta} = \boldsymbol{\theta}^{(t)}$ 处，由 Bayes 公式，对数中的比值对每个 $l$ 都等于 $1$，所以 $\tilde B(\boldsymbol{\theta}^{(t)}, \boldsymbol{\theta}^{(t)}) = \ell(\boldsymbol{\theta}^{(t)})$。$\tilde B$ 中依赖于 $\boldsymbol{\theta}$ 的部分是 $\sum_l q_l\ln\bigl(f(\boldsymbol{x}\mid Y=l,\boldsymbol{\theta})\,\mathbb{P}(Y=l\mid\boldsymbol{\theta})\bigr) = B(\boldsymbol{\theta}; \boldsymbol{\theta}^{(t)})$。因此 $\ell(\boldsymbol{\theta}^{(t+1)}) \ge \tilde B(\boldsymbol{\theta}^{(t+1)}, \boldsymbol{\theta}^{(t)}) \ge \tilde B(\boldsymbol{\theta}^{(t)}, \boldsymbol{\theta}^{(t)}) = \ell(\boldsymbol{\theta}^{(t)})$。$\square$

EM 算法是 minorization–maximization（MM）原则的特例：最大化一个在当前点与目标函数相切的简单下界。它在统计学中应用广泛，尤其适用于存在某些隐藏数据、而一旦知道它们问题就变得简单的情形。由定理 11.4.1，似然从不下降，所以在似然有界时算法收敛，但只收敛到局部极大（或驻点）；实践中从多个初值或从一个好的初始聚类出发。

### 11.4.5. 模型选择与实现

基于模型的聚类在 R 中由程序包 mclust 的函数 `Mclust` 实现（Scrucca 等，2016）：用层次聚类初始化，用 EM 算法优化，用 BIC 选择聚类数目。既然聚类现在是统计模型，选择聚类数目（以及协方差矩阵的形式）就成了模型选择问题，任何模型选择准则，如 AIC、BIC 或似然比，都可以使用。

**定义 11.4.2（信息准则）** 设 $L$ 是含 $m$ 个自由参数的模型拟合 $n$ 个观测所得的最大似然值。**贝叶斯信息准则**与**赤池信息准则**为

$$
\mathrm{BIC} = -2\ln L + m\ln n, \qquad \mathrm{AIC} = -2\ln L + 2m.
$$
在候选模型中，准则值较小者更优。

两个准则都用参数个数惩罚拟合程度 $-2\ln L$；当 $\ln n > 2$ 时 BIC 的惩罚更重，因而选择更小的模型。注意有些教材和 mclust 用相反的符号 $2\ln L - m\ln n$，此时 BIC 越大越好。

**注 11.4.1（为什么 AIC 着眼于预测）** 设数据 $\boldsymbol{y}$ 来自 $f(\cdot \mid \theta_0)$，$\hat\theta$ 是由 $\boldsymbol{y}$ 得到的极大似然估计。AIC 关心的是拟合模型 $f(\cdot \mid \hat\theta)$ 对来自同一分布的新数据 $\boldsymbol{y}^{\mathrm{new}}$ 的预测能力，即 $\ln f(\boldsymbol{y}^{\mathrm{new}} \mid \hat\theta)$ 的期望。直观地看：对新数据，真模型比拟合模型预测得好，$\ln f(\boldsymbol{y}^{\mathrm{new}}\mid\hat\theta) < \ln f(\boldsymbol{y}^{\mathrm{new}}\mid\theta_0)$；平均而言，真模型对 $\boldsymbol{y}^{\mathrm{new}}$ 和 $\boldsymbol{y}$ 拟合得一样好；对用于拟合的数据，拟合模型胜过真模型，$\ln f(\boldsymbol{y}\mid\theta_0) < \ln f(\boldsymbol{y}\mid\hat\theta)$，这就是过拟合。因此可观测的 $\ln f(\boldsymbol{y}\mid\hat\theta) = \ln L$ 高估了预测质量 $\ln f(\boldsymbol{y}^{\mathrm{new}}\mid\hat\theta)$，修正量 $\mathbb{E}[\ln f(\boldsymbol{y}\mid\hat\theta) - \ln f(\boldsymbol{y}^{\mathrm{new}}\mid\hat\theta)]$ 渐近地等于参数个数 $m$，乘以 $-2$ 即得 AIC。BIC 则近似对数**边际似然**的 $-2$ 倍，即贝叶斯模型比较所用的量（[3.2.7](/3.2.7)）。

可以限制各成分的协方差矩阵以减少参数个数。把每个协方差矩阵作**谱分解** $\Sigma_l = \lambda_l D_l A_l D_l^{\mathsf T}$，其中标量 $\lambda_l$ 决定第 $l$ 类的体积，$\det A_l = 1$ 的对角阵 $A_l$ 决定形状，正交阵 $D_l$ 决定方向。mclust 用三个字母依次标记体积、形状与方向的参数化，每个字母为 E（各类相等）、V（可变）或 I（单位：球形，或方向沿坐标轴）。例如：

- EEE：$k$ 个类的体积、形状与方向都相同（公共的 $\Sigma$，如 LDA）；
- VEI：体积可变，形状相同，方向沿坐标轴；
- VVV：体积、形状与方向都可变（不加限制的 $\Sigma_l$，如 QDA）。

对球形，方向无关紧要，所以球形模型是 EII 与 VII。程序包在一系列 $k$ 上用 BIC 比较这些模型。

**例 11.4.1** 对鸢尾花数据，`Mclust(iris[, -5], 3)` 拟合三成分混合，按 BIC 选出模型 VEV（体积可变，形状相同，方向可变）。它的三个类与品种的吻合程度远好于 $k$ 均值：versicolor 与 virginica 细长、倾斜的类被各自的协方差矩阵刻画出来。与 $k$ 均值一样，结果可能依赖于初值。

![三类模拟数据，其中两类是细长的带状。左：偏好紧凑球形类的 k 均值横切了带状类。中：用 EM 拟合、协方差矩阵不加限制的高斯混合找回了三组；椭圆表示拟合的成分。右：高斯混合的 BIC（越小越好）随成分个数的变化，在 k = 3 处最小。](./plots/kmeans-vs-gmm.py)

高斯混合与 EM 算法有许多成功的应用，例如配电系统负荷的统计建模，以及视频中的自适应背景减除。理论上，有限高斯混合在 $L^1$ 度量下在全体密度中稠密（Li 与 Barron，1999），所以成分足够多时可以逼近任何分布。推广包括贝叶斯高斯混合与无限高斯混合（Rasmussen，1999）、分裂—合并 EM（Ueda 等，2000）、竞争 EM（Zhang 等，2004），以及其他分布的有限混合（McLachlan 等，2019）。

## 11.5. 讨论

一次聚类分析包含一系列选择。

1. 预处理：变换数据（标准化、取对数、主成分等），检查离群点。与 LDA 不同（[3.4.10](/3.4.10#sec-10.7.1)），聚类依赖于变量的量纲，因此常常需要**标准化**。
2. 点间距离，视数据类型而定：数值型数据用欧氏距离或基于相关系数的距离；文本与分类数据用 Jaccard、Hamming 或编辑距离。
3. 层次聚类中类间距离的选择。各有优点与局限：单连接能处理非椭圆形状，但对噪声与离群点敏感；全连接对噪声与离群点更稳健，但倾向于打散大类。
4. $k$ 均值中的初始重心。随机选择可能出问题：若有 $10$ 个大小相同的真实类，随机选 $10$ 个点，恰好每类选中一个的概率只有 $10!/10^{10} \approx 0.00036$。

为什么要评价结果？为了比较聚类算法、两组聚类或两个类，以及选择聚类数目。数值度量有三类。

- 外部指标（有监督）：用某种聚类质量度量，把聚类结果与先验的或专家给定的知识（如已知标签）比较，例如基于熵的指标、成对计数指标或相关指标。
- 内部指标（无监督）：不借助外部信息评价聚类的好坏，例如 SSE、伪 $F$ 统计量或伪 $T^2$ 统计量。
- 相对指标：直接比较不同的聚类，通常是同一算法在不同参数设定下得到的聚类；常用某个外部或内部指标（如 SSE 或熵）来完成。

## 小结 {#summary}

| | 层次（凝聚） | $k$ 均值 | 基于模型（GMM） |
|---|---|---|---|
| 类型 | 硬 | 硬 | 软 |
| 设定 | 点间距离与类间距离 | $k$、初始重心、点间距离 | $k$；$Y \sim \mathrm{Mult}(1, \boldsymbol{\pi})$，$\boldsymbol{X}\mid Y = l \sim \mathcal{N}_p(\boldsymbol{\mu}_l, \Sigma_l)$ |
| 方法 | 反复合并最近的类；树状图 | 交替分配与更新以最小化 $J(c, \boldsymbol{\mu})$ | 用 EM 交替更新 $\gamma$ 与 $(\boldsymbol{\pi}, \boldsymbol{\mu}, \Sigma)$ 以最大化 $\ell(\boldsymbol{\pi}, \boldsymbol{\mu}, \Sigma)$ |
| 收敛 | 确定性的，$n-1$ 次合并 | $J$ 的局部极小 | $\ell$ 的局部极大；似然从不下降 |
| 优点 | 无需指定 $k$；展示对象间的关系 | 快速，$O(tkn)$ | 有正式模型；协方差结构灵活；用 BIC 选 $k$ |
| 缺点 | $O(n^2)$ 内存，慢；合并不能撤销 | 对离群点和初值敏感；偏向球形类；需要 $k$ | 参数多；局部极大；依赖模型 |

聚类分析按相似性对对象分组，既可用于理解数据，也可用于概括数据；距离、方法与聚类数目的选择，以及结果的评价，是每一次应用中都要面对的实际问题。
