---
title: 引言与矩阵基础
description: 多元数据与多元分析的目标；数据矩阵与随机向量样本；欧氏距离、马氏距离与二次型的期望；探索性作图；矩阵运算的几何意义、谱分解、平方根矩阵、奇异值分解、推广的 Cauchy–Schwarz 不等式与最大化引理；向量与矩阵微积分。
source_hash: dce136fbfd38
---

实际收集的数据几乎都在每个个体上记录多个变量，而这些变量通常彼此相关。多元统计分析把这些变量放在一起研究，而不是逐个分析。本章为课程打下两方面的基础。一是统计方面：多元数据如何组织与建模，两个观测之间的距离应如何考虑量纲差异与相关性（马氏距离），以及如何用图形探索数据。二是代数方面：课程中反复使用的矩阵工具及其几何意义。矩阵理论本身已在线性代数（[2.1](/2.1)）中建立，尤其是 [2.1.7](/2.1.7) 的谱分解与奇异值分解；这里汇总所需的结论，给出几何解释，并补充估计所需的不等式与矩阵微积分。样本的描述统计量与多元正态分布见 [3.4.2](/3.4.2)。

## 1.1. 多元数据与多元分析的目标

多元数据出现在各个学科中：一份病历、一份信用卡申请、一幅图像、一张购物小票，都用许多测量值描述一个对象。典型的问题有：

- 是否存在差异？例如处理前后大量基因表达水平的平均变化。
- 关键特征是什么？由性格测试各题得分，如何划分不同性格的人群，各群体又有什么特点。
- 关键关联是什么？全脑功能连接（数千对脑区之间的同步性得分）的哪些特征与青少年的哪些情绪、行为评分相关；招聘笔试测得的哪些能力与入职后的哪些业绩表现相关。
- 如何预测或推荐？"购买此商品的顾客也购买了……"。
- 作者是谁？由每一回中虚词的出现频数，研究《红楼梦》的作者是一位还是多位。
- 如何分类？由血液、影像等检测结果判断疾病类型；由客户的年龄、收入、受教育程度和还贷记录决定是否放贷。

从应用的角度，课程中的方法可分为以下几类；从模型 $f(\boldsymbol{x})$ 的角度，第一类关心均值向量 $\boldsymbol{\mu}$，其余大多关心协方差矩阵 $\Sigma$。

| 目标 | 方法 | 章节 |
|---|---|---|
| 均值的推断 | Hotelling $T^2$、均值向量的比较 | [3.4.3](/3.4.3)、[3.4.4](/3.4.4) |
| 降维（无监督） | 主成分、多维标度、因子分析、典型相关 | [3.4.5](/3.4.5)、[3.4.6](/3.4.6)、[3.4.8](/3.4.8)、[3.4.9](/3.4.9) |
| 预测与分类（有监督） | 多元回归、判别分析 | [3.4.7](/3.4.7)、[3.4.10](/3.4.10) |
| 聚类（无监督） | 系统聚类与划分方法 | [3.4.11](/3.4.11) |

凡涉及不确定性的问题都需要统计，而现实问题几乎都是如此。课程中贯穿着两组张力：科学与工程，即可解释性与预测精度；相应地，简单模型与复杂模型。本课程的经典方法偏向可解释的一侧，[3.4.12](/3.4.12) 讨论其扩展。

## 1.2. 多元数据的组织与建模

### 1.2.1. 数据矩阵

设在 $n$ 个对象（个体、试验单元）上各测量 $p$ 个变量，$x_{jk}$ 为第 $j$ 个对象的第 $k$ 个变量的取值。

**定义 1.2.1（数据矩阵）** 称 $n \times p$ 矩阵

$$
X = \begin{bmatrix} x_{11} & x_{12} & \cdots & x_{1p} \\ x_{21} & x_{22} & \cdots & x_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ x_{n1} & x_{n2} & \cdots & x_{np} \end{bmatrix} = \begin{bmatrix} \boldsymbol{x}_1^{\mathsf T} \\ \boldsymbol{x}_2^{\mathsf T} \\ \vdots \\ \boldsymbol{x}_n^{\mathsf T} \end{bmatrix}
$$
为**数据矩阵**。行对应对象，列对应变量；第 $j$ 行 $\boldsymbol{x}_j^{\mathsf T} = (x_{j1}, \dots, x_{jp})$ 是第 $j$ 个多元观测。

把数据写成矩阵，所有计算都可以用矩阵运算完成，也与数据的存储方式一致（例如以监测站为行、污染物为列的表格）。全课程采用以下约定：下标 $j = 1, \dots, n$ 遍历对象，$k$（或 $i$）$= 1, \dots, p$ 遍历变量。观测之前，矩阵元是随机变量 $X_{jk}$，各行是随机向量 $\boldsymbol{X}_j = (X_{j1}, \dots, X_{jp})^{\mathsf T}$；观测值记为 $x_{jk}$ 与 $\boldsymbol{x}_j$。两种情形下数据矩阵都记作 $X$，是随机的还是观测到的由上下文确定。于是观测数据是一个随机变量矩阵的一次实现，我们要问它的元素的联合分布是什么：各行来自什么总体分布，哪些假定合理，哪些未知参数刻画这一分布。

### 1.2.2. 随机样本

**定义 1.2.2（随机样本）** 称随机向量 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 为来自密度为 $f(\boldsymbol{x}) = f(x_1, \dots, x_p)$ 的 $p$ 维分布的**随机样本**，如果

1. $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 相互独立，且
2. 每个 $\boldsymbol{X}_j$ 都服从密度为 $f$ 的同一联合分布。

即数据矩阵的各行独立同分布。在此假定下，整个样本的联合密度为

$$
f(\boldsymbol{x}_1)f(\boldsymbol{x}_2)\cdots f(\boldsymbol{x}_n), \qquad f(\boldsymbol{x}_j) = f(x_{j1}, x_{j2}, \dots, x_{jp}),
$$
其中 $f$ 可以是参数形式，也可以是非参数的。独立性只假定在对象之间：同一对象上的 $p$ 个测量一般是相关的，对这种相关性建模正是本课程的主题。

概括 $f$ 的总体量是**随机向量** $\boldsymbol{X} = (X_1, \dots, X_p)^{\mathsf T}$ 的均值向量与**协方差矩阵**：

$$
\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X} = \begin{bmatrix} \mathbb{E}X_1 \\ \vdots \\ \mathbb{E}X_p \end{bmatrix} = \begin{bmatrix} \mu_1 \\ \vdots \\ \mu_p \end{bmatrix}, \qquad \Sigma = \operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}] = \begin{bmatrix} \sigma_{11} & \cdots & \sigma_{1p} \\ \vdots & \ddots & \vdots \\ \sigma_{p1} & \cdots & \sigma_{pp} \end{bmatrix},
$$
其中 $\sigma_{ik} = \operatorname{Cov}(X_i, X_k) = \mathbb{E}[(X_i - \mu_i)(X_k - \mu_k)]$，$\sigma_{kk} = \operatorname{Var}(X_k)$（运算法则见 [3.1.15](/3.1.15)）。

**例 1.2.1** 每年产生的城市固体垃圾总重量记录如下。

| 年份 | 1960 | 1970 | 1980 | 1990 | 1995 | 2000 | 2003 |
|---|---|---|---|---|---|---|---|
| $x_1$（纸张） | 29.2 | 44.3 | 55.2 | 72.7 | 81.7 | 87.7 | 83.1 |
| $x_2$（塑料） | 0.4 | 2.9 | 6.8 | 17.1 | 18.9 | 24.7 | 26.7 |

这七行不应视为随机样本。它们是同一时间序列的相继年份，有明显的上升趋势，观测既不独立也不同分布。在使用下面的任何方法之前，都要先根据数据的收集方式检查随机抽样的假定是否合理。

### 1.2.3. 两种几何图像

数据矩阵有两种看法。

- 看作 $p$ 维空间中的 $n$ 个点：每一行 $\boldsymbol{x}_j$ 是 $\mathbb{R}^p$ 中的一个点；$p = 2$ 或 $3$ 时就是散点图，它显示点的位置与离散程度。
- 看作 $n$ 维空间中的 $p$ 个向量：每一列是 $\mathbb{R}^n$ 中的一个向量，存放一个变量的 $n$ 个测量值。这些向量的长度与夹角对应于方差与相关（[3.4.2](/3.4.2)）。

例如，对 $X = \begin{bmatrix} 4 & 1 \\ 5 & 2 \\ 3 & 5 \end{bmatrix}$（三家书店的销售额（单位 100 元）与图书种数），第一种图像是平面上的三个点 $\boldsymbol{x}_1 = (4, 1)^{\mathsf T}$、$\boldsymbol{x}_2 = (5, 2)^{\mathsf T}$、$\boldsymbol{x}_3 = (3, 5)^{\mathsf T}$。$\boldsymbol{x}_1$ 与 $\boldsymbol{x}_2$ 更相似，还是与 $\boldsymbol{x}_3$ 更相似？答案取决于如何度量距离，这正是下一节的主题。

## 1.3. 统计距离

### 1.3.1. 从欧氏距离到统计距离

许多应用要比较两个个体，因此需要两个多元观测 $P = (x_1, \dots, x_p)$ 与 $Q = (y_1, \dots, y_p)$ 之间的距离或相似度。欧氏距离

$$
d(P, Q) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + \cdots + (x_p - y_p)^2}
$$
对每个坐标一视同仁。当各变量的单位或尺度不同时，这并不合理：改变一个变量的单位（米改为厘米）就会改变哪些点相近。

若各变量独立（或至少不相关），自然的办法是把每个坐标标准化，$x_k - y_k \mapsto (x_k - y_k)/\sqrt{s_{kk}}$，其中 $s_{kk}$ 是第 $k$ 个变量的样本方差：

$$
d(P, Q) = \sqrt{\frac{(x_1 - y_1)^2}{s_{11}} + \frac{(x_2 - y_2)^2}{s_{22}} + \cdots + \frac{(x_p - y_p)^2}{s_{pp}}}.
$$
此时到原点距离为常数 $c$ 的点构成沿坐标轴、半轴为 $c\sqrt{s_{11}}$ 与 $c\sqrt{s_{22}}$ 的椭圆。沿离散程度小的方向远离中心的点，比沿离散程度大的方向同样远的点更反常。

若变量相关，例如 $x_2$ 倾向于随 $x_1$ 增大，则点云是一个轴倾斜的椭圆，沿坐标轴的椭圆不再能描述它：位于这样一个椭圆上的两点 $P$、$Q$ 的典型程度可能相差很大。办法是把坐标系旋转角度 $\theta$，使新轴 $\tilde x_1, \tilde x_2$ 沿点云的轴，

$$
\tilde x_1 = x_1\cos\theta + x_2\sin\theta, \qquad \tilde x_2 = -x_1\sin\theta + x_2\cos\theta,
$$
再在新坐标下（变量不相关）标准化：

$$
d(O, P) = \sqrt{\frac{\tilde x_1^2}{\tilde s_{11}} + \frac{\tilde x_2^2}{\tilde s_{22}}} = \sqrt{a_{11}x_1^2 + 2a_{12}x_1x_2 + a_{22}x_2^2},
$$
其中常数 $a_{11}, a_{12}, a_{22}$ 由 $\theta$、$\tilde s_{11}$、$\tilde s_{22}$ 决定。交叉项 $2a_{12}x_1x_2$ 处理了非零的相关性。在 $p$ 维中，

$$
d(P, Q) = \sqrt{\sum_{k=1}^{p} a_{kk}(x_k - y_k)^2 + 2\sum_{i < k} a_{ik}(x_i - y_i)(x_k - y_k)},
$$
即 $d^2(P, Q) = (\boldsymbol{x} - \boldsymbol{y})^{\mathsf T}A(\boldsymbol{x} - \boldsymbol{y})$ 是 $\boldsymbol{x} - \boldsymbol{y}$ 的一个**二次型**，$A = (a_{ik})$ 对称。1.6 节将说明正确的选择是 $A = \Sigma^{-1}$。

### 1.3.2. 马氏距离

**定义 1.3.1（马氏距离）** 观测 $\boldsymbol{x} = (x_1, \dots, x_p)^{\mathsf T}$ 到均值为 $\boldsymbol{\mu} = (\mu_1, \dots, \mu_p)^{\mathsf T}$、协方差矩阵为正定矩阵 $\Sigma$ 的总体（或一组观测）的**马氏距离**为

$$
d(\boldsymbol{x}, \boldsymbol{\mu}) = \|\boldsymbol{x} - \boldsymbol{\mu}\|_{\Sigma} = \sqrt{(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})}.
$$
作为来自同一分布（协方差矩阵为 $\Sigma$）的两个随机向量 $\boldsymbol{x}$、$\boldsymbol{y}$ 之间的相异度，

$$
d(\boldsymbol{x}, \boldsymbol{y}) = \sqrt{(\boldsymbol{x} - \boldsymbol{y})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{y})}.
$$
其平方也称为广义平方点间距离。

这一距离由印度统计学家 P. C. Mahalanobis（1893–1972）于 1936 年提出，起因是根据多项测量判断头骨的相似程度。若把数据椭球的各轴重新缩放为单位方差，马氏距离就是变换后空间中的普通欧氏距离（1.6.4 节）。因此它无量纲、不受尺度影响，并考虑了数据的相关性。实际中用样本均值 $\bar{\boldsymbol{x}}$ 与样本协方差矩阵 $S$ 代替 $\boldsymbol{\mu}$ 与 $\Sigma$，得到 $(\boldsymbol{x} - \bar{\boldsymbol{x}})^{\mathsf T}S^{-1}(\boldsymbol{x} - \bar{\boldsymbol{x}})$。其应用包括异常值检测、判别（[3.4.10](/3.4.10)）与聚类（[3.4.11](/3.4.11)）。

欧氏距离（$A = I$）与马氏距离（$A = \Sigma^{-1}$）都是二次型 $Q(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$（$A$ 对称）的平方根。比较二者的第一种方式是计算它们的期望。

![左：相关样本，以及过点 P 的欧氏圆与马氏椭圆；Q 的欧氏距离比 P 小，马氏距离却大得多。右：白化（旋转到主轴并缩放为单位方差）之后，椭圆变为圆，马氏距离即欧氏距离。](./plots/mahalanobis-geometry.py)

### 1.3.3. 二次型的期望

**定理 1.3.1** 设随机向量 $\boldsymbol{Z}$ 的均值 $\boldsymbol{\mu}_Z$ 与协方差矩阵 $\Sigma_Z$ 有限，$A$ 为常数对称矩阵，则

$$
\mathbb{E}[\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}] = \operatorname{tr}(A\Sigma_Z) + \boldsymbol{\mu}_Z^{\mathsf T}A\boldsymbol{\mu}_Z.
$$

**证明** 标量等于自身的**迹**，迹是线性的（因而与期望可交换），且 $\operatorname{tr}(BC) = \operatorname{tr}(CB)$。再利用 $\mathbb{E}[\boldsymbol{Z}\boldsymbol{Z}^{\mathsf T}] = \Sigma_Z + \boldsymbol{\mu}_Z\boldsymbol{\mu}_Z^{\mathsf T}$，

$$
\begin{aligned}
\mathbb{E}[\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}] &= \mathbb{E}[\operatorname{tr}(\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z})] = \mathbb{E}[\operatorname{tr}(A\boldsymbol{Z}\boldsymbol{Z}^{\mathsf T})] = \operatorname{tr}(A\,\mathbb{E}[\boldsymbol{Z}\boldsymbol{Z}^{\mathsf T}]) \\
&= \operatorname{tr}(A\Sigma_Z) + \operatorname{tr}(A\boldsymbol{\mu}_Z\boldsymbol{\mu}_Z^{\mathsf T}) = \operatorname{tr}(A\Sigma_Z) + \boldsymbol{\mu}_Z^{\mathsf T}A\boldsymbol{\mu}_Z. \quad \square
\end{aligned}
$$

**推论 1.3.1（欧氏距离平方的期望）** 若 $p$ 维随机向量 $\boldsymbol{X}$ 的均值 $\boldsymbol{\mu}$ 与协方差矩阵 $\Sigma$ 有限，则

$$
\mathbb{E}\|\boldsymbol{X} - \boldsymbol{\mu}\|^2 = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}I(\boldsymbol{X} - \boldsymbol{\mu})] = \operatorname{tr}\Sigma = \sum_{k=1}^{p}\sigma_{kk}.
$$

在定理 1.3.1 中取 $\boldsymbol{Z} = \boldsymbol{X} - \boldsymbol{\mu}$（均值为 $\boldsymbol{0}$）、$A = I$ 即得。欧氏距离平方的期望是总方差，由方差最大的那些变量主导。

**推论 1.3.2（马氏距离平方的期望）** 在同样的假定下，若 $\Sigma$ 正定，则

$$
\mathbb{E}\|\boldsymbol{X} - \boldsymbol{\mu}\|_{\Sigma}^2 = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu})] = \operatorname{tr}(\Sigma^{-1}\Sigma) = p.
$$
若 $\boldsymbol{X}$ 与 $\boldsymbol{Y}$ 独立同分布，均值为 $\boldsymbol{\mu}$、协方差矩阵为 $\Sigma$，则 $\mathbb{E}\|\boldsymbol{X} - \boldsymbol{Y}\|_{\Sigma}^2 = 2p$。

**证明** 第一个结论是定理 1.3.1 取 $A = \Sigma^{-1}$。对第二个结论，$\boldsymbol{Z} = \boldsymbol{X} - \boldsymbol{Y}$ 的均值为 $\boldsymbol{0}$，其协方差矩阵的元素为

$$
\operatorname{Cov}(X_i - Y_i, X_k - Y_k) = \operatorname{Cov}(X_i, X_k) - \operatorname{Cov}(Y_i, X_k) - \operatorname{Cov}(X_i, Y_k) + \operatorname{Cov}(Y_i, Y_k) = 2\sigma_{ik},
$$
这是因为由独立性交叉协方差为零，由同分布 $\operatorname{Cov}(Y_i, Y_k) = \sigma_{ik}$。故 $\operatorname{Cov}(\boldsymbol{X} - \boldsymbol{Y}) = 2\Sigma$，$\mathbb{E}[\boldsymbol{Z}^{\mathsf T}\Sigma^{-1}\boldsymbol{Z}] = \operatorname{tr}(\Sigma^{-1} \cdot 2\Sigma) = 2p$。$\square$

证明中逐个元素的计算值得做一次；此后应当像一维情形那样直接写出 $\operatorname{Cov}(\boldsymbol{X} - \boldsymbol{Y}) = \operatorname{Cov}(\boldsymbol{X}) + \operatorname{Cov}(\boldsymbol{Y}) = 2\Sigma$。与欧氏距离不同，马氏距离平方的期望与各变量的尺度和相关性无关：$p$ 个标准化、去相关的方向各贡献 $1$。

## 1.4. 探索性数据分析

任何数据分析的重要一步是探索性数据分析（Exploratory Data Analysis），包括数据的图形展示。图形可以提示合理的数据模型、检验模型假定是否成立、发现异常值，或提示使数据接近正态的变换。对每个变量，要看位置、离散程度、偏度、异常值与子群；对多个变量，还要看变量之间的关系。

### 1.4.1. 单个变量的展示

**定义 1.4.1（箱线图）** 设 $Q_1$、$Q_2$、$Q_3$ 分别为样本的下四分位数、中位数与上四分位数，$\mathrm{IQR} = Q_3 - Q_1$ 为四分位距。**箱线图**画一个从 $Q_1$ 到 $Q_3$ 的箱子，在中位数处画线（常常也标出均值），从箱子向两端画须线，直到正常范围 $[Q_1 - 1.5\,\mathrm{IQR},\ Q_3 + 1.5\,\mathrm{IQR}]$ 内最极端的观测；范围之外的观测单独画出，作为可能的异常值。

**例 1.4.1** 若样本中位数为 $8$，$Q_1 = 4$，$Q_3 = 10$，则 $\mathrm{IQR} = 6$，正常范围为 $[4 - 9,\ 10 + 9] = [-5, 19]$。上须线止于 $\min(19, \max_j x_j)$，下须线止于 $\max(-5, \min_j x_j)$。

并排的箱线图用于比较各组。对美国、日本与欧洲汽车的燃油效率，它一眼就显示出日本车更省油（美国车的箱子位于日本车的箱子之下，最费油的日本车也比约一半的美国车省油），并且有一辆非常省油的车（一款柴油大众车）是异常值。箱线图显示位置、离散程度、偏度与异常值，但不能显示多峰与子群。

直方图近似密度，因此也能显示多峰与子群。它不唯一：其外观取决于组距 $h$ 与起点。对标准差为 $\sigma$ 的正态数据，使渐近积分均方误差最小的组距为

$$
h_{\mathrm{opt}} = \left(\frac{24\sqrt{\pi}}{n}\right)^{1/3}\sigma \approx 3.49\,\sigma n^{-1/3}.
$$
分类变量则用条形图与饼图。

### 1.4.2. 多个变量的展示

对多个变量，既看每个变量的特征，也看变量之间的关系。

| 图形 | 显示什么 |
|---|---|
| 两个变量的散点图 | 子群、异常值、正或负的相依关系 |
| 散点图矩阵（所有变量两两配对，对角线上为直方图或密度） | 一次看到所有两两关系 |
| 三维散点图（可旋转） | 涉及三个变量的结构 |
| 相关热图 | 以颜色显示相关矩阵；调整变量顺序可以显出相关变量的分块 |
| 雷达图、星图 | 每个对象画成多边形或星形，各射线为（缩放后的）变量；比较对象或组的轮廓 |
| Chernoff 脸谱图 | 每个变量控制卡通脸的一个特征 |
| Andrews 曲线 | 每个对象画成一条曲线，见下 |
| 生长曲线 | 随时间的重复测量，每个对象一条曲线 |

观测 $\boldsymbol{x} = (x_1, \dots, x_p)^{\mathsf T}$ 的 Andrews 曲线是函数

$$
f_{\boldsymbol{x}}(t) = \frac{x_1}{\sqrt{2}} + x_2\sin t + x_3\cos t + x_4\sin 2t + x_5\cos 2t + \cdots, \qquad -\pi \le t \le \pi.
$$
由三角函数的正交性，两条曲线之间的 $L^2$ 距离与两个观测之间的欧氏距离成正比，因此相似的对象给出相似的曲线。

![模拟的含两组的四变量数据的散点图矩阵：对角线为各变量的直方图，非对角线为所有两两散点图。两组在每个单变量上都重叠，但在某些变量对上明显分开。](./plots/scatterplot-matrix.py)

在经典的瑞士旧版 1000 法郎钞票数据（真钞与伪钞各六项尺寸测量）中，两项测量的散点图区分真伪钞的效果远好于任何单项测量。这正是推动多元方法的典型情形。

## 1.5. 向量与矩阵的几何视角

下面回顾本课程的矩阵工具，重点是借助几何理解代数。

### 1.5.1. 长度、夹角与投影

对 $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$，**内积**为 $\boldsymbol{x}^{\mathsf T}\boldsymbol{y} = x_1y_1 + \cdots + x_ny_n$，长度为 $L_{\boldsymbol{x}} = \sqrt{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$，非零向量的夹角 $\theta$ 满足

$$
\cos\theta = \frac{\boldsymbol{x}^{\mathsf T}\boldsymbol{y}}{L_{\boldsymbol{x}}L_{\boldsymbol{y}}} = \frac{\boldsymbol{x}^{\mathsf T}\boldsymbol{y}}{\sqrt{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}\sqrt{\boldsymbol{y}^{\mathsf T}\boldsymbol{y}}}.
$$
$\boldsymbol{x}$ 在 $\boldsymbol{y} \ne \boldsymbol{0}$ 所张直线上的**正交投影**为

$$
\frac{\boldsymbol{x}^{\mathsf T}\boldsymbol{y}}{\boldsymbol{y}^{\mathsf T}\boldsymbol{y}}\,\boldsymbol{y} = \frac{\boldsymbol{x}^{\mathsf T}\boldsymbol{y}}{L_{\boldsymbol{y}}}\cdot\frac{\boldsymbol{y}}{L_{\boldsymbol{y}}},
$$
其有向长度为 $\boldsymbol{x}^{\mathsf T}\boldsymbol{y}/L_{\boldsymbol{y}} = L_{\boldsymbol{x}}\cos\theta$。例如 $(3, 2)^{\mathsf T}$ 在 $(4, 0)^{\mathsf T}$ 上的投影是 $(3, 0)^{\mathsf T}$。

### 1.5.2. 矩阵作为映射

$m \times k$ 矩阵 $A = [\boldsymbol{a}_1, \dots, \boldsymbol{a}_k]$ 把 $\boldsymbol{x} \in \mathbb{R}^k$ 映为 $A\boldsymbol{x} = x_1\boldsymbol{a}_1 + \cdots + x_k\boldsymbol{a}_k \in \mathbb{R}^m$，即其各列的线性组合。基本运算（转置、加法、数乘、乘法、迹、行列式、秩、逆、分块、特征值与特征向量）见 [2.1](/2.1)；回忆一般 $AB \ne BA$。经常出现的特殊矩阵有：**对称矩阵**（总体与样本的协方差矩阵都是对称的）；**对角矩阵** $\operatorname{diag}(d_1, \dots, d_p)$，它分别缩放各坐标轴；**单位矩阵** $I$，$IA = AI = A$。

### 1.5.3. 正交矩阵

若方阵 $P$ 的各行作为向量两两垂直且长度为 $1$，即 $PP^{\mathsf T} = I$，则称 $P$ 为**正交矩阵**。等价地 $P^{-1} = P^{\mathsf T}$，从而也有 $P^{\mathsf T}P = I$，各列也是标准正交的。我们常按列写出正交矩阵，$P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_p]$，$i \ne k$ 时 $\boldsymbol{e}_i^{\mathsf T}\boldsymbol{e}_k = 0$，$\boldsymbol{e}_i^{\mathsf T}\boldsymbol{e}_i = 1$。

正交矩阵保持长度与夹角，其作用是更换标准正交坐标系。若 $\boldsymbol{x}$ 是某点在原坐标系中的坐标，坐标轴逆时针旋转 $\theta$，则同一点在旋转后坐标系中的坐标为

$$
P\boldsymbol{x}, \qquad P = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix};
$$
例如 $\boldsymbol{x} = (\cos\phi, \sin\phi)^{\mathsf T}$ 变为 $P\boldsymbol{x} = (\cos(\phi - \theta), \sin(\phi - \theta))^{\mathsf T}$。一般地，$P$ 的各行是用旧坐标表示的新坐标轴，$P\boldsymbol{x}$ 的各分量是 $\boldsymbol{x}$ 在新轴上的投影。正交矩阵 $\begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}$（行列式为 $-1$）同样是坐标变换：新轴为 $(\cos\theta, \sin\theta)^{\mathsf T}$ 与 $(\sin\theta, -\cos\theta)^{\mathsf T}$，即旋转 $\theta$ 后再把第二个轴反向。

## 1.6. 谱分解与正定矩阵

### 1.6.1. 谱分解

$k \times k$ 对称矩阵 $A$ 有 $k$ 个实的特征值–特征向量对 $(\lambda_1, \boldsymbol{e}_1), \dots, (\lambda_k, \boldsymbol{e}_k)$，特征向量可以取为两两垂直的单位向量，于是 $\{\boldsymbol{e}_1, \dots, \boldsymbol{e}_k\}$ 是一组**标准正交基**，$P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_k]$ 是正交矩阵。除非有两个或更多特征值相等，特征向量是唯一的（相差符号）。

**定理 1.6.1（谱分解）** 设 $k \times k$ 对称矩阵 $A$ 的标准正交特征向量为 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_k$，特征值为 $\lambda_1, \dots, \lambda_k$，记 $P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_k]$，$\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_k)$，则

$$
A = P\Lambda P^{\mathsf T} = \sum_{i=1}^{k}\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T} = \lambda_1\boldsymbol{e}_1\boldsymbol{e}_1^{\mathsf T} + \lambda_2\boldsymbol{e}_2\boldsymbol{e}_2^{\mathsf T} + \cdots + \lambda_k\boldsymbol{e}_k\boldsymbol{e}_k^{\mathsf T}.
$$

这就是 [2.1.7](/2.1.7) 的**谱分解**。把 $k$ 个等式 $A\boldsymbol{e}_i = \lambda_i\boldsymbol{e}_i$ 并排写在一起即得矩阵形式：左边构成 $[A\boldsymbol{e}_1, \dots, A\boldsymbol{e}_k] = AP$，右边构成 $[\lambda_1\boldsymbol{e}_1, \dots, \lambda_k\boldsymbol{e}_k] = P\Lambda$，故 $AP = P\Lambda$，$A = P\Lambda P^{-1} = P\Lambda P^{\mathsf T}$。把 $P \cdot \Lambda P^{\mathsf T}$ 按"列乘行"展开，就得到秩一矩阵 $\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$ 之和。像这样在核对维数的前提下把向量和矩阵形式上当作标量来推演，是本课程希望培养的习惯。

### 1.6.2. 几何解释

映射 $\boldsymbol{x} \mapsto A\boldsymbol{x} = P\Lambda P^{\mathsf T}\boldsymbol{x}$（从右向左读）由三步复合而成：$P^{\mathsf T}$ 把 $\boldsymbol{x}$ 表示到特征向量坐标系中（旋转，可能带反射），$\Lambda$ 把第 $i$ 个新轴伸缩 $\lambda_i$ 倍（$\lambda_i < 0$ 时反向），$P$ 再回到原坐标。

**例 1.6.1** 对 $A = \begin{bmatrix} 1 & -5 \\ -5 & 1 \end{bmatrix}$，特征值为 $6$ 与 $-4$，单位特征向量为 $\frac{1}{\sqrt{2}}(1, -1)^{\mathsf T}$ 与 $\frac{1}{\sqrt{2}}(1, 1)^{\mathsf T}$，故

$$
A = P\Lambda P^{\mathsf T}, \qquad P^{\mathsf T} = \begin{bmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}, \qquad \Lambda = \begin{bmatrix} 6 & 0 \\ 0 & -4 \end{bmatrix}.
$$
作用于点云 $B$（$n \times 2$ 数据矩阵）时，三步依次可见：$B_2^{\mathsf T} = P^{\mathsf T}B^{\mathsf T}$ 把点云旋转 $45^\circ$，$B_3^{\mathsf T} = \Lambda B_2^{\mathsf T}$ 把第一个轴拉伸六倍、第二个轴拉伸四倍并反向，$B_4^{\mathsf T} = PB_3^{\mathsf T} = AB^{\mathsf T}$ 再转回。

### 1.6.3. 正定矩阵、逆矩阵与平方根矩阵

设 $A$ 为 $k \times k$ 对称矩阵。若对一切 $\boldsymbol{x}$ 有 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} \ge 0$，则称矩阵及其二次型为非负定的，即**半正定矩阵**；若对一切 $\boldsymbol{x} \ne \boldsymbol{0}$ 有 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} > 0$，则称为**正定矩阵**（[2.1.7](/2.1.7)）。正是这些矩阵定义了距离。由谱分解，记 $y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{x}$，

$$
\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} = \sum_{i=1}^{k}\lambda_i(\boldsymbol{e}_i^{\mathsf T}\boldsymbol{x})^2 = \sum_{i=1}^{k}\lambda_iy_i^2,
$$
所以 $A$ 正定当且仅当所有特征值为正，非负定当且仅当所有特征值非负。当所有 $\lambda_i \ge 0$ 时，$\boldsymbol{x}^{\mathsf T}A\boldsymbol{x} = \sum_i(\sqrt{\lambda_i}y_i)^2$ 是旋转并缩放后坐标中的欧氏长度平方。

**定义 1.6.1（平方根矩阵）** 设 $A = P\Lambda P^{\mathsf T} = \sum_{i=1}^{k}\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$ 对称且非负定。称矩阵

$$
A^{1/2} = P\Lambda^{1/2}P^{\mathsf T} = \sum_{i=1}^{k}\sqrt{\lambda_i}\,\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}, \qquad \Lambda^{1/2} = \operatorname{diag}(\sqrt{\lambda_1}, \dots, \sqrt{\lambda_k}),
$$
为 $A$ 的**平方根矩阵**。

**性质 1.6.1** 设 $A$ 对称正定，$A = P\Lambda P^{\mathsf T}$，所有 $\lambda_i > 0$，则

1. $A^{-1} = P\Lambda^{-1}P^{\mathsf T} = \sum_{i=1}^{k}\frac{1}{\lambda_i}\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$；
2. $(A^{1/2})^{\mathsf T} = A^{1/2}$，$A^{1/2}A^{1/2} = A$；
3. $(A^{1/2})^{-1} = P\Lambda^{-1/2}P^{\mathsf T} = \sum_{i=1}^{k}\frac{1}{\sqrt{\lambda_i}}\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$，记作 $A^{-1/2}$；
4. $A^{1/2}A^{-1/2} = A^{-1/2}A^{1/2} = I$，$A^{-1/2}A^{-1/2} = A^{-1}$。

四条都由 $P^{\mathsf T}P = I$ 得到，例如 $A^{1/2}A^{1/2} = P\Lambda^{1/2}P^{\mathsf T}P\Lambda^{1/2}P^{\mathsf T} = P\Lambda P^{\mathsf T} = A$。同样的方式可以通过特征值定义对称矩阵的任意函数。

### 1.6.4. 马氏距离的几何解释

现在从 1.3.1 节的需求出发推导马氏距离：找新的坐标，使数据呈球形，从而欧氏距离变得合适。不妨设均值为 $\boldsymbol{0}$，并设 $\Sigma = P\Lambda P^{\mathsf T}$ 是 $\boldsymbol{X}$ 的协方差矩阵的谱分解。

我们要找 $\operatorname{Cov}(\boldsymbol{Y}) = I$ 的 $\boldsymbol{Y}$（数据分布在球面而非椭球面上），以及旋转 $\tilde P$ 与缩放 $\tilde\Lambda$（正的对角矩阵），使 $\boldsymbol{X} = \tilde P\tilde\Lambda\boldsymbol{Y}$。于是

$$
\Sigma = \operatorname{Cov}(\boldsymbol{X}) = \tilde P\tilde\Lambda\operatorname{Cov}(\boldsymbol{Y})\tilde\Lambda\tilde P^{\mathsf T} = \tilde P\tilde\Lambda^2\tilde P^{\mathsf T},
$$
由谱分解的唯一性可取 $\tilde P = P$，$\tilde\Lambda = \Lambda^{1/2}$：旋转由 $\Sigma$ 的特征向量给出，尺度由其特征值的平方根给出。新坐标下的欧氏长度平方为

$$
\boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} = \boldsymbol{X}^{\mathsf T}P\Lambda^{-1/2}\Lambda^{-1/2}P^{\mathsf T}\boldsymbol{X} = \boldsymbol{X}^{\mathsf T}P\Lambda^{-1}P^{\mathsf T}\boldsymbol{X} = \boldsymbol{X}^{\mathsf T}\Sigma^{-1}\boldsymbol{X},
$$
这正是马氏距离的平方。实际中用样本协方差矩阵 $S = \hat P\hat\Lambda\hat P^{\mathsf T}$ 估计 $\Sigma$，旋转由 $\hat P$ 给出，所用的距离为 $\boldsymbol{x}^{\mathsf T}S^{-1}\boldsymbol{x}$。

**注 1.6.1** 为什么旋转 $P^{\mathsf T}$ 能把倾斜的椭圆转成与坐标轴平行？椭圆倾斜意味着分量相关，$\sigma_{12} \ne 0$。旋转之后

$$
\operatorname{Cov}(P^{\mathsf T}\boldsymbol{X}) = P^{\mathsf T}\Sigma P = P^{\mathsf T}P\Lambda P^{\mathsf T}P = \Lambda
$$
是对角矩阵：新坐标互不相关，椭圆与新坐标轴平行。随后的缩放 $\Lambda^{-1/2}$ 使各轴方差为 $1$，椭圆变为圆。关键在于距离中所用的矩阵正是被度量的这批数据本身的协方差矩阵。

## 1.7. 奇异值分解与矩阵不等式

### 1.7.1. 奇异值分解

**定理 1.7.1（奇异值分解）** 设 $A$ 为 $m \times k$ 实矩阵，则存在 $m \times m$ 正交矩阵 $U$ 与 $k \times k$ 正交矩阵 $V$，使得

$$
A = U\Lambda V^{\mathsf T},
$$
其中 $\Lambda$ 为 $m \times k$ 矩阵，其 $(i, i)$ 元 $\lambda_i \ge 0$（$i = 1, \dots, \min(m, k)$），其余元素为零。正的 $\lambda_i$ 称为 $A$ 的**奇异值**。

这就是 [2.1.7](/2.1.7) 的**奇异值分解**。由它得 $AA^{\mathsf T} = U\Lambda\Lambda^{\mathsf T}U^{\mathsf T}$ 与 $A^{\mathsf T}A = V\Lambda^{\mathsf T}\Lambda V^{\mathsf T}$，这是两个对称矩阵的谱分解：$U$、$V$ 的列是它们的特征向量，奇异值的平方 $\lambda_i^2$ 是它们的非零特征值。几何上，一般矩阵对数据的作用为 $A\boldsymbol{x} = U(\Lambda(V^{\mathsf T}\boldsymbol{x}))$：换到 $V$ 给出的坐标，把各轴伸缩 $\lambda_i$ 倍（$m \ne k$ 时舍去或增加维数），再由 $U$ 旋转到目标空间。与谱分解不同，伸缩前后的坐标系不同。

### 1.7.2. 推广的 Cauchy–Schwarz 不等式

**Cauchy–Schwarz 不等式**说，对任意 $p \times 1$ 向量 $\boldsymbol{b}$、$\boldsymbol{d}$，

$$
(\boldsymbol{b}^{\mathsf T}\boldsymbol{d})^2 \le (\boldsymbol{b}^{\mathsf T}\boldsymbol{b})(\boldsymbol{d}^{\mathsf T}\boldsymbol{d}),
$$
等号成立当且仅当存在常数 $c$ 使 $\boldsymbol{b} = c\boldsymbol{d}$（或 $\boldsymbol{d} = c\boldsymbol{b}$）。

**引理 1.7.1（推广的 Cauchy–Schwarz 不等式）** 设 $\boldsymbol{b}$、$\boldsymbol{d}$ 为 $p \times 1$ 向量，$B$ 为 $p \times p$ 正定矩阵，则

$$
(\boldsymbol{b}^{\mathsf T}\boldsymbol{d})^2 \le (\boldsymbol{b}^{\mathsf T}B\boldsymbol{b})(\boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d}),
$$
等号成立当且仅当存在常数 $c$ 使 $\boldsymbol{b} = cB^{-1}\boldsymbol{d}$（或 $\boldsymbol{d} = \boldsymbol{0}$）。

**证明** 写 $\boldsymbol{b}^{\mathsf T}\boldsymbol{d} = \boldsymbol{b}^{\mathsf T}B^{1/2}B^{-1/2}\boldsymbol{d} = (B^{1/2}\boldsymbol{b})^{\mathsf T}(B^{-1/2}\boldsymbol{d})$，对向量 $B^{1/2}\boldsymbol{b}$ 与 $B^{-1/2}\boldsymbol{d}$ 用 Cauchy–Schwarz 不等式，它们的长度平方分别是 $\boldsymbol{b}^{\mathsf T}B\boldsymbol{b}$ 与 $\boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d}$。等号成立当且仅当 $B^{1/2}\boldsymbol{b} = cB^{-1/2}\boldsymbol{d}$，即 $\boldsymbol{b} = cB^{-1}\boldsymbol{d}$。$\square$

**引理 1.7.2（最大化引理）** 设 $B$ 为 $p \times p$ 正定矩阵，$\boldsymbol{d}$ 为给定的 $p \times 1$ 向量，则

$$
\max_{\boldsymbol{x} \ne \boldsymbol{0}}\frac{(\boldsymbol{x}^{\mathsf T}\boldsymbol{d})^2}{\boldsymbol{x}^{\mathsf T}B\boldsymbol{x}} = \boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d},
$$
最大值在 $\boldsymbol{x} = cB^{-1}\boldsymbol{d}$（任意常数 $c \ne 0$）处取到。

**证明** 由引理 1.7.1，$(\boldsymbol{x}^{\mathsf T}\boldsymbol{d})^2 \le (\boldsymbol{x}^{\mathsf T}B\boldsymbol{x})(\boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d})$；两边除以 $\boldsymbol{x}^{\mathsf T}B\boldsymbol{x} > 0$。上界恰在 $\boldsymbol{x} = cB^{-1}\boldsymbol{d}$ 时取到。$\square$

最大化引理是 [3.4.3](/3.4.3) 的联合置信区间与判别分析（[3.4.10](/3.4.10)）的代数核心。

**定理 1.7.2（二次型在单位球面上的最大化）** 设 $p \times p$ 正定矩阵 $B$ 的特征值为 $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_p > 0$，对应的单位特征向量为 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$，则

$$
\max_{\boldsymbol{x} \ne \boldsymbol{0}}\frac{\boldsymbol{x}^{\mathsf T}B\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}} = \lambda_1 \ (\text{在 } \boldsymbol{x} = \boldsymbol{e}_1 \text{ 处取到}), \qquad \min_{\boldsymbol{x} \ne \boldsymbol{0}}\frac{\boldsymbol{x}^{\mathsf T}B\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}} = \lambda_p \ (\text{在 } \boldsymbol{x} = \boldsymbol{e}_p \text{ 处取到}).
$$
此外，对 $k = 1, \dots, p - 1$，

$$
\max_{\boldsymbol{x} \perp \boldsymbol{e}_1, \dots, \boldsymbol{e}_k}\frac{\boldsymbol{x}^{\mathsf T}B\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}} = \lambda_{k+1} \quad (\text{在 } \boldsymbol{x} = \boldsymbol{e}_{k+1} \text{ 处取到}).
$$

这个比值就是 **Rayleigh 商**，该定理即线性代数的[定理 7.2.1](/2.1.7#thm-7.2.1)（对任意对称矩阵 $B$ 成立）。在坐标 $\boldsymbol{y} = P^{\mathsf T}\boldsymbol{x}$ 下，商为 $\sum_i\lambda_iy_i^2/\sum_iy_i^2$，是特征值的加权平均。定理 1.7.2 是主成分分析（[3.4.5](/3.4.5)）的基础：在单位向量中，使 $\boldsymbol{x}^{\mathsf T}\boldsymbol{X}$ 方差最大的方向是 $\boldsymbol{e}_1$。

## 1.8. 向量与矩阵微积分

多元模型的极大似然估计需要对向量和矩阵求导。通用的布局有两种，相差一个转置。

**定义 1.8.1（分子布局与分母布局）** 设 $\boldsymbol{y} = (y_1, \dots, y_q)^{\mathsf T}$ 是 $\boldsymbol{x} = (x_1, \dots, x_p)^{\mathsf T}$ 的函数。在**分子布局**中，$\frac{\partial\boldsymbol{y}}{\partial\boldsymbol{x}}$ 是 $(i, k)$ 元为 $\frac{\partial y_i}{\partial x_k}$ 的 $q \times p$ 矩阵，按 $\boldsymbol{y}$ 与 $\boldsymbol{x}^{\mathsf T}$ 排列；在**分母布局**中，它是 $(k, i)$ 元为 $\frac{\partial y_i}{\partial x_k}$ 的 $p \times q$ 矩阵，按 $\boldsymbol{y}^{\mathsf T}$ 与 $\boldsymbol{x}$ 排列。对 $p \times p$ 矩阵 $A$ 的标量函数 $f$，分母布局给出 $p \times p$ 矩阵 $\frac{\partial f}{\partial A} = \left(\frac{\partial f}{\partial a_{ik}}\right)$。

在分母布局下，标量对列向量的导数是列向量（**梯度**）。$\boldsymbol{y}$ 的分子布局导数就是 $f\colon \mathbb{R}^p \to \mathbb{R}^q$ 的 **Jacobi 矩阵** $J_f(\boldsymbol{x})$，即全导数的矩阵（$q \times p$），链式法则为

$$
J_{f \circ g}(\boldsymbol{x}) = J_f(g(\boldsymbol{x}))\,J_g(\boldsymbol{x}) \quad (\text{分子布局}), \qquad H_{f \circ g}(\boldsymbol{x}) = H_g(\boldsymbol{x})\,H_f(g(\boldsymbol{x})) \quad (\text{分母布局}),
$$
其中 $H = J^{\mathsf T}$ 表示分母布局的导数。转置使因子的次序颠倒。

**例 1.8.1** 设 $\boldsymbol{y} = A\boldsymbol{x}$，$A = \begin{bmatrix} 1 & 3 \\ 0 & 2 \\ 0 & 1 \end{bmatrix}$，即 $y_1 = x_1 + 3x_2$，$y_2 = 2x_2$，$y_3 = x_2$。分子布局下 $\frac{\partial\boldsymbol{y}}{\partial\boldsymbol{x}} = \begin{bmatrix} 1 & 3 \\ 0 & 2 \\ 0 & 1 \end{bmatrix} = A$；分母布局下 $\frac{\partial\boldsymbol{y}}{\partial\boldsymbol{x}} = \begin{bmatrix} 1 & 0 & 0 \\ 3 & 2 & 1 \end{bmatrix} = A^{\mathsf T}$。

除非另有说明，我们采用分母布局。

**性质 1.8.1** 设 $\boldsymbol{x}$ 为向量，$A$ 为尺寸相容的常数矩阵。在分母布局下，

$$
\frac{\partial A\boldsymbol{x}}{\partial\boldsymbol{x}} = A^{\mathsf T}, \qquad \frac{\partial\boldsymbol{x}^{\mathsf T}A}{\partial\boldsymbol{x}} = A, \qquad \frac{\partial\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}{\partial\boldsymbol{x}} = 2\boldsymbol{x}, \qquad \frac{\partial\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\partial\boldsymbol{x}} = A\boldsymbol{x} + A^{\mathsf T}\boldsymbol{x}.
$$
特别地，$A$ 对称时 $\frac{\partial\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\partial\boldsymbol{x}} = 2A\boldsymbol{x}$。

**例 1.8.2** 设 $A$ 对称正定。以 $g(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$ 为内层函数、$\log$ 为外层函数，用链式法则（分母布局）得

$$
\frac{\partial}{\partial\boldsymbol{x}}\log(\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}) = \frac{\partial(\boldsymbol{x}^{\mathsf T}A\boldsymbol{x})}{\partial\boldsymbol{x}}\cdot\frac{1}{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}} = \frac{2A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}, \qquad \boldsymbol{x} \ne \boldsymbol{0}.
$$

**性质 1.8.2（行列式与迹的导数）** 设 $A$ 为 $p \times p$ 对称正定矩阵，$B$ 为 $p \times p$ 常数矩阵。在分母布局下，

$$
\frac{\partial\det A}{\partial A} = (\det A)A^{-1}, \qquad \frac{\partial\log\det A}{\partial A} = A^{-1}, \qquad \frac{\partial\operatorname{tr}(AB)}{\partial A} = B^{\mathsf T},
$$

$$
\frac{\partial\operatorname{tr}(A^{-1}B)}{\partial A} = -A^{-1}B^{\mathsf T}A^{-1}, \qquad \frac{\partial\operatorname{tr}(B^{\mathsf T}A^{-1}B)}{\partial A} = -A^{-1}BB^{\mathsf T}A^{-1}.
$$

**注 1.8.1** 这些公式把 $A$ 的 $p^2$ 个元素都当作自由变量；对一般（非对称）的 $A$，第一个公式为 $(\det A)(A^{-1})^{\mathsf T}$，$A$ 对称时它等于 $(\det A)A^{-1}$。若把对称性 $a_{ik} = a_{ki}$ 作为约束，导数的非对角元会相差一个因子，但方程"导数 $= O$"的解不变，而极大似然估计只需要这一点（[3.4.2](/3.4.2)）。矩阵微积分是工具而非课程目标：它使多元极大似然的计算可以沿用熟悉的一维思路，也是练习矩阵运算的好载体，但后续章节很少用到。

## 小结

- 多元数据：$n \times p$ 数据矩阵 $X$，行为对象、列为变量；在随机抽样下，各行 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 独立同分布，均值向量为 $\boldsymbol{\mu}$、协方差矩阵为 $\Sigma$，而同一行中的变量相关。两种图像：$\mathbb{R}^p$ 中的 $n$ 个点，或 $\mathbb{R}^n$ 中的 $p$ 个向量。
- 欧氏距离忽略单位与相关性；马氏距离 $\sqrt{(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})}$ 是旋转到 $\Sigma$ 的特征向量并缩放为单位方差后的欧氏距离。$\mathbb{E}[\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}] = \operatorname{tr}(A\Sigma_Z) + \boldsymbol{\mu}_Z^{\mathsf T}A\boldsymbol{\mu}_Z$；欧氏距离平方的期望为 $\operatorname{tr}\Sigma$，马氏距离平方的期望为 $p$。
- 探索性作图：单变量用箱线图与直方图；多变量用散点图、散点图矩阵、热图、星图、脸谱图与曲线。
- 矩阵工具：正交矩阵更换坐标；$A = P\Lambda P^{\mathsf T} = \sum\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$（旋转、伸缩、转回）；$A^{\pm 1/2} = P\Lambda^{\pm 1/2}P^{\mathsf T}$；任意矩阵 $A = U\Lambda V^{\mathsf T}$。
- 不等式：$(\boldsymbol{b}^{\mathsf T}\boldsymbol{d})^2 \le (\boldsymbol{b}^{\mathsf T}B\boldsymbol{b})(\boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d})$；$\max_{\boldsymbol{x}}(\boldsymbol{x}^{\mathsf T}\boldsymbol{d})^2/\boldsymbol{x}^{\mathsf T}B\boldsymbol{x} = \boldsymbol{d}^{\mathsf T}B^{-1}\boldsymbol{d}$；Rayleigh 商取值于 $[\lambda_p, \lambda_1]$。
- 分母布局下的矩阵微积分：$\partial\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}/\partial\boldsymbol{x} = (A + A^{\mathsf T})\boldsymbol{x}$，$\partial\log\det A/\partial A = A^{-1}$，$\partial\operatorname{tr}(A^{-1}B)/\partial A = -A^{-1}B^{\mathsf T}A^{-1}$。
