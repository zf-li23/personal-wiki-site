---
title: 线性回归模型
description: 从多元的角度看经典线性回归模型：最小二乘及其作为正交投影的几何，Gauss–Markov 假定与正态假定下的性质、t 与 F 推断和预测区间，以及岭回归、主成分回归与 Lasso 等正则化方法。
source_hash: 1cbf4135a61b
---

统计与机器学习中的许多问题都在问：响应如何依赖于若干个协变量？例如明年的收入如何依赖于年龄、受教育程度和过去的收入，孩子的身高如何依赖于父母的身高。线性回归模型是最简单而又不平凡的回答。它自然地属于多元统计课程，因为它的一切都是矩阵代数：最小二乘拟合是到**设计矩阵**列空间上的**正交投影**，其分布由 [3.4.2](/3.4.2) 的**多元正态分布**得出，检验一组系数的统计量与 [3.4.3](/3.4.3) 中的 Hotelling $T^2$ 是同一类二次型。本章先建立模型与最小二乘估计，再在三层逐渐加强的假定（无假定、Gauss–Markov 模型、正态误差）下研究它的性质，最后讨论协变量很多的情形：岭回归、主成分回归（建立在 [3.4.5](/3.4.5) 的**主成分分析**之上）和 **Lasso** 以少量偏差换取方差的大幅减小。估计理论与 [3.2.3](/3.2.3) 有重叠，检验与 [3.2.5](/3.2.5) 有重叠；模型诊断、变量选择与一般线性模型在线性回归课程 [3.3](/3.3) 中展开。

## 7.1. 经典线性回归模型

### 7.1.1. 响应与协变量

数据由 $n$ 个个体组成，每个个体有一个响应和 $p$ 个协变量。响应变量（response）记为 $Y$；协变量（covariate，也称预测变量）记为 $X_1,\dots,X_p$，合成 $\boldsymbol{X}=(X_1,\dots,X_p)^{\mathsf T}$。对这样的数据可以提出两类问题：

- 描述：$Y$ 与 $\boldsymbol{X}$ 有怎样的关联（身高与体重、收入与教育和工作经验之间是什么关系）？
- 预测：给定新的协变量向量 $\boldsymbol{x}^*$，应当预期怎样的响应 $Y^*$？

我们假定 $n$ 个观测 $(\boldsymbol{x}_i,y_i)$ 独立同分布，$p$ 固定，并把协变量视为给定的（是否对其取条件对下文并不关键）。任何响应都可以分解为条件均值加误差：

$$
Y=\mathbb{E}(Y\mid\boldsymbol{X}=\boldsymbol{x})+\varepsilon=g(\boldsymbol{x})+\varepsilon,\qquad\mathbb{E}(\varepsilon\mid\boldsymbol{X}=\boldsymbol{x})=0,
$$

其中 $g$ 是回归函数；**条件期望**是在均方意义下由 $\boldsymbol{X}$ 预测 $Y$ 的**最佳预测**（[3.1.9](/3.1.9)）。线性模型把 $g$ 限制为线性函数，一个协变量时为 $g(x)=a+bx$。

线性模型是很好的起点，原因有几条：它简单但不平凡；基于优美的代数与几何可以得到显式公式，从而带来洞见；把协变量的非线性变换放进模型，它也能刻画非线性；它常常是非线性数据生成过程的良好近似；它虽然更简单，预测效果却未必比复杂的非线性模型差。

**例 7.1.1（一个协变量）** 要由年龄 $x$ 预测一个人明年的收入 $y$，数据为 $(x_i,y_i)$，$i=1,\dots,n$，取

$$
y_i=a+bx_i+\varepsilon_i,\quad i=1,\dots,n,\qquad\text{即}\qquad\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},\qquad\boldsymbol{Y}=\begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix},\quad X=\begin{bmatrix}1&x_1\\\vdots&\vdots\\1&x_n\end{bmatrix},\quad\boldsymbol{\beta}=\begin{bmatrix}a\\b\end{bmatrix}.
$$

**例 7.1.2（两个总体）** 若第 $i$ 人参加了职业培训则 $x_i=1$，否则 $x_i=0$，拟合同样的模型 $y_i=a+bx_i+\varepsilon_i$。由 $\mathbb{E}\varepsilon_i=0$，未培训者的平均收入为 $\mu_1=a$，培训者为 $\mu_2=a+b$，因此检验 $H_0\colon\mu_1=\mu_2$ 就是检验 $H_0\colon b=0$。把个体按组排列，设计矩阵的第一列全为 1，第二列是 $n_1$ 个 0 后接 $n_2$ 个 1；这个回归中 $b=0$ 的 $t$ 检验恰好就是 [3.2.5](/3.2.5) 的合并方差两样本 $t$ 检验。

**例 7.1.3（二次趋势）** 若收入随年龄先升后降，取 $y_i=a+bx_i+cx_i^2+\varepsilon_i$，它仍是 $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$，其中 $X$ 的行为 $(1,x_i,x_i^2)$，$\boldsymbol{\beta}=(a,b,c)^{\mathsf T}$。设计矩阵可以包含原始协变量的多项式或任何其他非线性变换：统计中的"线性"指对参数线性，而不是对协变量线性。

### 7.1.2. 最小二乘估计

哪条直线拟合得最好？Gauss 提出使竖直偏差的平方和最小。一个协变量时，普通最小二乘（OLS）估计为

$$
(\hat\alpha,\hat\beta)=\arg\min_{a,b}\frac1n\sum_{i=1}^n(y_i-a-bx_i)^2.
$$

令两个偏导数为零得

$$
\frac1n\sum_{i=1}^n(y_i-\hat\alpha-\hat\beta x_i)=0\ \Longrightarrow\ \bar y=\hat\alpha+\hat\beta\bar x,\qquad\frac1n\sum_{i=1}^nx_i(y_i-\hat\alpha-\hat\beta x_i)=0\ \Longrightarrow\ \overline{xy}=\hat\alpha\bar x+\hat\beta\,\overline{x^2},
$$

消去 $\hat\alpha$ 得 $\overline{xy}-\bar x\bar y=\hat\beta(\overline{x^2}-\bar x^2)$，即 $\hat\sigma_{xy}=\hat\beta\hat\sigma_x^2$。于是

$$
\hat\beta=\frac{\hat\sigma_{xy}}{\hat\sigma_x^2},\qquad\hat\alpha=\bar y-\hat\beta\bar x,
$$

其中 $\hat\sigma_{xy}=\frac1n\sum_i(x_i-\bar x)(y_i-\bar y)$，$\hat\sigma_x^2=\frac1n\sum_i(x_i-\bar x)^2$。

用样本**相关系数** $\hat\rho_{xy}=\hat\sigma_{xy}/(\hat\sigma_x\hat\sigma_y)$ 改写拟合直线，可以看出它的含义：

$$
\hat y_i-\bar y=\frac{\hat\sigma_{xy}}{\hat\sigma_x^2}(x_i-\bar x)=\frac{\hat\rho_{xy}\hat\sigma_x\hat\sigma_y}{\hat\sigma_x^2}(x_i-\bar x)\quad\Longrightarrow\quad\frac{\hat y_i-\bar y}{\hat\sigma_y}=\hat\rho_{xy}\,\frac{x_i-\bar x}{\hat\sigma_x}.
$$

在标准化单位下斜率就是相关系数；由于 $\lvert\hat\rho_{xy}\rvert\le1$，预测值比协变量更靠近均值，这就是 Galton 最初观察到的"向均值回归"。这正是 [3.1.10](/3.1.10) 中**最佳线性预测**的样本版本：斜率 $\rho\sqrt{\operatorname{Var}(Y)}/\sqrt{\operatorname{Var}(X)}$ 在 $b\in\mathbb{R}$ 上最小化 $\mathbb{E}[(Y-\mathbb{E}Y)-b(X-\mathbb{E}X)]^2$。因此回归反映的是相关，而不是因果。

多个协变量时，令第一个协变量为常数 $1$（截距项），仍用 $p$ 表示列的总数。数据为

$$
\boldsymbol{Y}=\begin{bmatrix}y_1\\y_2\\\vdots\\y_n\end{bmatrix},\qquad X=\begin{bmatrix}x_{11}&x_{12}&\cdots&x_{1p}\\x_{21}&x_{22}&\cdots&x_{2p}\\\vdots&\vdots&&\vdots\\x_{n1}&x_{n2}&\cdots&x_{np}\end{bmatrix}=\begin{bmatrix}\boldsymbol{x}_1^{\mathsf T}\\\boldsymbol{x}_2^{\mathsf T}\\\vdots\\\boldsymbol{x}_n^{\mathsf T}\end{bmatrix}=(X_1,\dots,X_p),
$$

即 $\boldsymbol{x}_i\in\mathbb{R}^p$ 是个体 $i$ 的协变量向量，$X_j\in\mathbb{R}^n$ 是第 $j$ 列。（[3.2.3](/3.2.3) 把截距单独计数，那里的 $p+1$ 对应这里的 $p$。）OLS 估计为

$$
\hat{\boldsymbol{\beta}}=\arg\min_{\boldsymbol{\beta}}\frac1n\sum_{i=1}^n(y_i-\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta})^2=\arg\min_{\boldsymbol{\beta}}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2.
$$

一阶条件为 $\sum_{i=1}^n\boldsymbol{x}_i(y_i-\boldsymbol{x}_i^{\mathsf T}\hat{\boldsymbol{\beta}})=\boldsymbol{0}$，即正规方程 $X^{\mathsf T}(\boldsymbol{Y}-X\hat{\boldsymbol{\beta}})=\boldsymbol{0}$；若 $X^{\mathsf T}X=\sum_i\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}$ 非奇异（等价地，$X$ 列满秩 $p$），则

$$
\hat{\boldsymbol{\beta}}=\Big(\sum_{i=1}^n\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}\Big)^{-1}\Big(\sum_{i=1}^n\boldsymbol{x}_iy_i\Big)=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$

当 $p=2$、$X=(\boldsymbol{1},\boldsymbol{x})$ 时，这就退化为上面 $(\hat\alpha,\hat\beta)$ 的公式。

### 7.1.3. 最小二乘的几何

把 $\boldsymbol{Y}$ 与各列 $X_1,\dots,X_p$ 看作 $\mathbb{R}^n$ 中的向量。向量 $X\boldsymbol{b}$（$\boldsymbol{b}\in\mathbb{R}^p$）构成列空间 $\mathcal{R}(X)=\{b_1X_1+\cdots+b_pX_p\colon b_j\in\mathbb{R}\}$，因此最小化 $\|\boldsymbol{Y}-X\boldsymbol{b}\|^2$ 就是在 $\mathcal{R}(X)$ 中找离 $\boldsymbol{Y}$ 最近的点：

$$
X\hat{\boldsymbol{\beta}}=\arg\min_{\boldsymbol{v}\in\mathcal{R}(X)}\|\boldsymbol{Y}-\boldsymbol{v}\|^2.
$$

这就是线性代数中的**最小二乘**问题（[2.1](/2.1)），答案是 $\boldsymbol{Y}$ 在 $\mathcal{R}(X)$ 上的**正交投影**：残差 $\boldsymbol{Y}-X\hat{\boldsymbol{\beta}}$ 与每一列都正交，这正是正规方程所说的。

![n = 3、两个协变量时最小二乘的几何：拟合向量 X b_hat 是 Y 在 X_1 与 X_2 张成的平面上的正交投影，残差与该平面垂直，任何其他 X b 离 Y 都更远](./plots/ols-geometry.py)

**定义 7.1.1** 称 $\hat{\boldsymbol{Y}}=X\hat{\boldsymbol{\beta}}$ 为**拟合值**向量，$\hat{\boldsymbol{\varepsilon}}=\boldsymbol{Y}-\hat{\boldsymbol{Y}}$ 为**残差**向量。由于

$$
\hat{\boldsymbol{Y}}=X\hat{\boldsymbol{\beta}}=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}=H\boldsymbol{Y},\qquad H=X(X^{\mathsf T}X)^{-1}X^{\mathsf T},
$$
称 $n\times n$ 矩阵 $H$ 为**帽子矩阵**（它给 $\boldsymbol{Y}$ "戴上帽子"）。

$H$ 对称且幂等，$H=H^{\mathsf T}$、$H^2=H$，所以它是到 $\mathcal{R}(X)$ 上的**正交投影矩阵**，且 $\operatorname{tr}(H)=\operatorname{tr}\big((X^{\mathsf T}X)^{-1}X^{\mathsf T}X\big)=p=\operatorname{rank}(H)$；$I_n-H$ 是到正交补上的投影，秩为 $n-p$。按分量写，$\hat y_i=\sum_{j=1}^nh_{ij}y_j$：每个拟合值都是全部响应的加权平均，对角元 $h_{ii}$（个体 $i$ 的杠杆值）衡量 $y_i$ 对自身拟合值的影响。

**命题 7.1.1（性质 I）** 不需要任何概率假定，$\hat{\boldsymbol{Y}}\perp\hat{\boldsymbol{\varepsilon}}$，即 $\hat{\boldsymbol{Y}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}=0$；从而 $\|\boldsymbol{Y}\|^2=\|\hat{\boldsymbol{Y}}\|^2+\|\hat{\boldsymbol{\varepsilon}}\|^2$。

**证明** $\hat{\boldsymbol{Y}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}=\boldsymbol{Y}^{\mathsf T}H(I_n-H)\boldsymbol{Y}=\boldsymbol{Y}^{\mathsf T}(H-H^2)\boldsymbol{Y}=0$。$\square$

这是 OLS 纯粹的几何性质；下一节加入概率。

## 7.2. 最小二乘估计的性质

### 7.2.1. Gauss–Markov 模型

**定义 7.2.1（Gauss–Markov 模型）** **Gauss–Markov 模型**是

$$
\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},\qquad\mathbb{E}(\boldsymbol{\varepsilon})=\boldsymbol{0},\qquad\operatorname{Cov}(\boldsymbol{\varepsilon})=\sigma^2I_n,
$$
其中设计矩阵 $X$ 固定且各列线性无关。等价地，$y_i=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}+\varepsilon_i$，$\mathbb{E}\varepsilon_i=0$，$\operatorname{Var}(\varepsilon_i)=\sigma^2$，$i\ne j$ 时 $\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$。未知参数为 $(\boldsymbol{\beta},\sigma^2)$。

这里只规定了误差的前两阶矩，但这已足以求出 $\boldsymbol{Y}$ 的任何线性函数的均值与协方差。

**定理 7.2.1** 在 Gauss–Markov 模型下，

$$
\mathbb{E}(\hat{\boldsymbol{\beta}})=\boldsymbol{\beta},\qquad\operatorname{Cov}(\hat{\boldsymbol{\beta}})=\sigma^2(X^{\mathsf T}X)^{-1},
$$
而拟合值与残差满足

$$
\mathbb{E}\begin{bmatrix}\hat{\boldsymbol{Y}}\\\hat{\boldsymbol{\varepsilon}}\end{bmatrix}=\begin{bmatrix}X\boldsymbol{\beta}\\\boldsymbol{0}\end{bmatrix},\qquad\operatorname{Cov}\begin{bmatrix}\hat{\boldsymbol{Y}}\\\hat{\boldsymbol{\varepsilon}}\end{bmatrix}=\sigma^2\begin{bmatrix}H&O\\O&I_n-H\end{bmatrix}.
$$

**证明** 由 $\mathbb{E}(\boldsymbol{Y})=X\boldsymbol{\beta}$ 与 $\operatorname{Cov}(\boldsymbol{Y})=\sigma^2I_n$，

$$
\mathbb{E}(\hat{\boldsymbol{\beta}})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\mathbb{E}(\boldsymbol{Y})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}X\boldsymbol{\beta}=\boldsymbol{\beta},
$$

$$
\operatorname{Cov}(\hat{\boldsymbol{\beta}})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\operatorname{Cov}(\boldsymbol{Y})X(X^{\mathsf T}X)^{-1}=\sigma^2(X^{\mathsf T}X)^{-1}X^{\mathsf T}X(X^{\mathsf T}X)^{-1}=\sigma^2(X^{\mathsf T}X)^{-1}.
$$

第二个结论的关键在于两个向量都是 $\boldsymbol{Y}$ 的线性函数：

$$
\begin{bmatrix}\hat{\boldsymbol{Y}}\\\hat{\boldsymbol{\varepsilon}}\end{bmatrix}=\begin{bmatrix}H\boldsymbol{Y}\\(I_n-H)\boldsymbol{Y}\end{bmatrix}=\begin{bmatrix}H\\I_n-H\end{bmatrix}\boldsymbol{Y}.
$$

由 $HX=X$，均值为 $(HX\boldsymbol{\beta},(I_n-H)X\boldsymbol{\beta})=(X\boldsymbol{\beta},\boldsymbol{0})$；协方差为 $\sigma^2\begin{bmatrix}H\\I_n-H\end{bmatrix}\begin{bmatrix}H&I_n-H\end{bmatrix}$，其各块为 $H^2=H$、$H(I_n-H)=O$、$(I_n-H)^2=I_n-H$。$\square$

于是在 Gauss–Markov 模型下，几何上的正交 $\hat{\boldsymbol{Y}}\perp\hat{\boldsymbol{\varepsilon}}$ 变成了 $\operatorname{Cov}(\hat{\boldsymbol{Y}},\hat{\boldsymbol{\varepsilon}})=O$。

为估计 $\sigma^2$，记 $\hat y_i=\boldsymbol{x}_i^{\mathsf T}\hat{\boldsymbol{\beta}}$，$\hat\varepsilon_i=y_i-\hat y_i$；残差 $\hat\varepsilon_i$ 是数据点到拟合直线的竖直距离，$\sigma$ 是 $y$ 围绕总体回归直线的散布程度。自然的选择是 $\tilde\sigma^2=\operatorname{RSS}/n$，其中残差平方和（residual sum of squares）为

$$
\operatorname{RSS}=\sum_{i=1}^n\hat\varepsilon_i^2=\hat{\boldsymbol{\varepsilon}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}.
$$
但由定理 7.2.1，$\mathbb{E}\hat\varepsilon_i=0$，$\operatorname{Var}(\hat\varepsilon_i)=\sigma^2(1-h_{ii})$，所以

$$
\mathbb{E}(\operatorname{RSS})=\sigma^2\sum_{i=1}^n(1-h_{ii})=\sigma^2\big(n-\operatorname{tr}(H)\big)=\sigma^2(n-p).
$$
因此我们使用

$$
\hat\sigma^2=\frac{\operatorname{RSS}}{n-p}=\frac{1}{n-p}\sum_{i=1}^n\hat\varepsilon_i^2,
$$
它是 $\sigma^2$ 的**无偏估计**：拟合 $p$ 个系数用掉了 $p$ 个自由度。

Gauss–Markov 模型还给出 OLS 的一个最优性。对对称矩阵，若 $A-B$ 半正定则记 $A\succeq B$；$\operatorname{Cov}(\tilde{\boldsymbol{\beta}})\succeq\operatorname{Cov}(\hat{\boldsymbol{\beta}})$ 意味着对每个 $\boldsymbol{c}\in\mathbb{R}^p$ 都有 $\operatorname{Var}(\boldsymbol{c}^{\mathsf T}\tilde{\boldsymbol{\beta}})\ge\operatorname{Var}(\boldsymbol{c}^{\mathsf T}\hat{\boldsymbol{\beta}})$。

**定理 7.2.2（Gauss–Markov 定理）** 在 Gauss–Markov 模型下，OLS 估计 $\hat{\boldsymbol{\beta}}$ 是 $\boldsymbol{\beta}$ 的最优线性无偏估计（BLUE）：对满足下列条件的任何估计 $\tilde{\boldsymbol{\beta}}$，都有 $\operatorname{Cov}(\tilde{\boldsymbol{\beta}})\succeq\operatorname{Cov}(\hat{\boldsymbol{\beta}})$：

1. 对某个不依赖于 $\boldsymbol{Y}$ 的 $A\in\mathbb{R}^{p\times n}$，$\tilde{\boldsymbol{\beta}}=A\boldsymbol{Y}$；
2. 对每个 $\boldsymbol{\beta}$，$\mathbb{E}(\tilde{\boldsymbol{\beta}})=\boldsymbol{\beta}$。

**证明** 条件 2 意味着对一切 $\boldsymbol{\beta}$ 有 $AX\boldsymbol{\beta}=\boldsymbol{\beta}$，即 $AX=I_p$。记 $A=(X^{\mathsf T}X)^{-1}X^{\mathsf T}+D$，则 $DX=O$，且

$$
\operatorname{Cov}(\tilde{\boldsymbol{\beta}})=\sigma^2AA^{\mathsf T}=\sigma^2(X^{\mathsf T}X)^{-1}+\sigma^2DD^{\mathsf T}\succeq\sigma^2(X^{\mathsf T}X)^{-1}=\operatorname{Cov}(\hat{\boldsymbol{\beta}}),
$$
因为交叉项 $(X^{\mathsf T}X)^{-1}X^{\mathsf T}D^{\mathsf T}$ 为零。$\square$

### 7.2.2. 正态线性模型

为了得到精确的置信区间与检验，我们加强对误差的假定。

**定义 7.2.2（正态线性模型）** **正态线性模型**是

$$
\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon},\qquad\boldsymbol{\varepsilon}\sim\mathcal{N}_n(\boldsymbol{0},\sigma^2I_n),
$$
其中设计矩阵 $X$ 固定且列满秩；等价地，$y_i=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{\beta}+\varepsilon_i$，$\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$，$i=1,\dots,n$。

由于它蕴含了误差不相关且方差相同，正态线性模型是 Gauss–Markov 模型的特例，7.2.1 节的结论全部成立。回忆 $\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$，$\hat{\boldsymbol{Y}}=X\hat{\boldsymbol{\beta}}$，$\hat{\boldsymbol{\varepsilon}}=\boldsymbol{Y}-\hat{\boldsymbol{Y}}$，$\hat\sigma^2=\hat{\boldsymbol{\varepsilon}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}/(n-p)$。

**定理 7.2.3** 在正态线性模型下，

$$
\begin{bmatrix}\hat{\boldsymbol{\beta}}\\\hat{\boldsymbol{\varepsilon}}\end{bmatrix}\sim\mathcal{N}_{p+n}\left(\begin{bmatrix}\boldsymbol{\beta}\\\boldsymbol{0}\end{bmatrix},\ \sigma^2\begin{bmatrix}(X^{\mathsf T}X)^{-1}&O\\O&I_n-H\end{bmatrix}\right),\qquad\frac{\hat\sigma^2}{\sigma^2}\sim\frac{\chi^2_{n-p}}{n-p},
$$
因此 $\hat{\boldsymbol{\beta}}\perp\!\!\!\perp\hat{\boldsymbol{\varepsilon}}$，$\hat{\boldsymbol{\beta}}\perp\!\!\!\perp\hat\sigma^2$。同样，$(\hat{\boldsymbol{Y}},\hat{\boldsymbol{\varepsilon}})$ 服从联合正态分布，其矩如定理 7.2.1 所示，从而 $\hat{\boldsymbol{Y}}\perp\!\!\!\perp\hat{\boldsymbol{\varepsilon}}$。

**证明** 向量 $(\hat{\boldsymbol{\beta}},\hat{\boldsymbol{\varepsilon}})$ 等于 $\begin{bmatrix}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\\I_n-H\end{bmatrix}\boldsymbol{Y}$，是正态向量 $\boldsymbol{Y}$ 的线性变换，所以服从（退化的）多元正态分布。其均值为 $(\boldsymbol{\beta},\boldsymbol{0})$；由于 $X^{\mathsf T}H=X^{\mathsf T}$，非对角协方差块为 $\sigma^2(X^{\mathsf T}X)^{-1}X^{\mathsf T}(I_n-H)=O$。对联合正态向量，协方差为零即独立，所以 $\hat{\boldsymbol{\beta}}$ 与 $\hat{\boldsymbol{\varepsilon}}$ 及其任何函数独立，特别是与 $\hat\sigma^2$ 独立。最后 $\hat{\boldsymbol{\varepsilon}}=(I_n-H)\boldsymbol{\varepsilon}$，故 $\hat{\boldsymbol{\varepsilon}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}=\boldsymbol{\varepsilon}^{\mathsf T}(I_n-H)\boldsymbol{\varepsilon}$；把投影写成 $I_n-H=QQ^{\mathsf T}$，其中 $Q\in\mathbb{R}^{n\times(n-p)}$ 的列标准正交，则 $Q^{\mathsf T}\boldsymbol{\varepsilon}/\sigma\sim\mathcal{N}_{n-p}(\boldsymbol{0},I_{n-p})$，于是 $\hat{\boldsymbol{\varepsilon}}^{\mathsf T}\hat{\boldsymbol{\varepsilon}}/\sigma^2=\|Q^{\mathsf T}\boldsymbol{\varepsilon}/\sigma\|^2\sim\chi^2_{n-p}$。关于 $\hat{\boldsymbol{Y}}=X\hat{\boldsymbol{\beta}}$ 的结论同理可得。$\square$

这个定理是线性模型中一切精确推断的来源。三种典型应用是：单个线性组合、多个线性组合与预测。

**推论 7.2.1** 在正态线性模型下，对每个 $\boldsymbol{c}\in\mathbb{R}^p$，

$$
\boldsymbol{c}^{\mathsf T}\hat{\boldsymbol{\beta}}\sim\mathcal{N}\big(\boldsymbol{c}^{\mathsf T}\boldsymbol{\beta},\ \sigma^2\boldsymbol{c}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{c}\big),\qquad T_{\boldsymbol{c}}=\frac{\boldsymbol{c}^{\mathsf T}\hat{\boldsymbol{\beta}}-\boldsymbol{c}^{\mathsf T}\boldsymbol{\beta}}{\sqrt{\hat\sigma^2\boldsymbol{c}^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{c}}}\sim t_{n-p}.
$$

取 $\boldsymbol{c}$ 为第 $j$ 个标准基向量，就得到单个系数 $\beta_j$ 通常的 $t$ 检验与置信区间（[3.2.5](/3.2.5)）。

**推论 7.2.2** 设 $C$ 是秩为 $l$ 的 $l\times p$ 矩阵，行为 $\boldsymbol{c}_1^{\mathsf T},\dots,\boldsymbol{c}_l^{\mathsf T}$，从而 $C\boldsymbol{\beta}=(\boldsymbol{c}_1^{\mathsf T}\boldsymbol{\beta},\dots,\boldsymbol{c}_l^{\mathsf T}\boldsymbol{\beta})^{\mathsf T}$。在正态线性模型下，$C\hat{\boldsymbol{\beta}}-C\boldsymbol{\beta}\sim\mathcal{N}_l\big(\boldsymbol{0},\sigma^2C(X^{\mathsf T}X)^{-1}C^{\mathsf T}\big)$，且

$$
F_C=\frac{(C\hat{\boldsymbol{\beta}}-C\boldsymbol{\beta})^{\mathsf T}\{C(X^{\mathsf T}X)^{-1}C^{\mathsf T}\}^{-1}(C\hat{\boldsymbol{\beta}}-C\boldsymbol{\beta})}{l\,\hat\sigma^2}\sim F_{l,n-p}.
$$

**证明** 分子乘以 $l/\sigma^2$ 是正态向量 $\boldsymbol{Z}\sim\mathcal{N}_l(\boldsymbol{0},\Sigma_Z)$ 的二次型 $\boldsymbol{Z}^{\mathsf T}\Sigma_Z^{-1}\boldsymbol{Z}$，故服从 $\chi^2_l$；它是 $\hat{\boldsymbol{\beta}}$ 的函数，因而与 $(n-p)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p}$ 独立。两个卡方变量各除以自由度后的比服从 $F_{l,n-p}$。$\square$

例如取 $C=\begin{bmatrix}\boldsymbol{0}&I_{p-1}\end{bmatrix}$，则 $C\boldsymbol{\beta}=(\beta_2,\dots,\beta_p)^{\mathsf T}$，在 $C\boldsymbol{\beta}=\boldsymbol{0}$ 下的 $F_C$ 检验截距以外是否有任何协变量起作用。这个统计量与 [3.4.3](/3.4.3) 中 Hotelling $T^2$ 的结构相同：都是在协方差矩阵之逆所定义的度量下的平方距离。

在新的协变量向量 $\boldsymbol{x}^*$ 处做预测，有两个目标。平均响应 $\boldsymbol{x}^{*\mathsf T}\boldsymbol{\beta}$ 的估计为 $\hat y^*=\boldsymbol{x}^{*\mathsf T}\hat{\boldsymbol{\beta}}$，由推论 7.2.1 取 $\boldsymbol{c}=\boldsymbol{x}^*$，得置信区间

$$
\hat y^*\pm t_{n-p,\alpha/2}\,\hat\sigma\sqrt{\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*}.
$$
新的响应 $y^*=\boldsymbol{x}^{*\mathsf T}\boldsymbol{\beta}+\varepsilon^*$（$\varepsilon^*\sim\mathcal{N}(0,\sigma^2)$ 与数据独立）满足 $y^*-\hat y^*\sim\mathcal{N}\big(0,\sigma^2(1+\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*)\big)$，由此得到预测区间（prediction interval）

$$
\hat y^*\pm t_{n-p,\alpha/2}\,\hat\sigma\sqrt{1+\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*}.
$$
多出的 $1$ 来自新观测本身的噪声；当 $n\to\infty$ 时它不会消失，而置信区间会收缩为一点。

### 7.2.3. 例子

**例 7.2.1（Galton 身高数据）** Galton 的家庭数据记录了 $934$ 个成年子女的身高（单位：英寸）以及父母中间身高（父母身高的平均）。把子女身高对父母中间身高作回归，得

| | 估计值 | 标准误 | $t$ 值 | $p$ 值 |
|---|---|---|---|---|
| 截距 | $22.64$ | $4.27$ | $5.31$ | $1.4\times10^{-7}$ |
| 父母中间身高 | $0.637$ | $0.0616$ | $10.35$ | $8.1\times10^{-24}$ |

斜率显著为正但小于 $1$：高个父母的子女也高，但平均而言不如父母那样极端，这就是 7.1.2 节的向均值回归。父母中间身高为 $60$ 英寸时拟合值为 $60.88$，平均身高的 $95\%$ 置信区间为 $[59.74,62.01]$。预测区间比置信区间宽得多，而且两者都随 $\boldsymbol{x}^*$ 远离数据中心而变宽，因为 $\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*$ 增大。

**例 7.2.2（职业培训）** 在 Lalonde 数据（$n=445$）中，把一项职业培训实验参与者 1978 年的收入 re78 对处理指示变量和十个处理前协变量（年龄、受教育年数、黑人、西班牙裔、已婚、无学位的指示变量、1974 与 1975 年收入以及这两年零收入的指示变量）作回归，于是 $p=12$，$n-p=433$。处理效应的系数为 $1671$（标准误 $641$，$t=2.61$，$p=0.0095$），是显著的正效应，而没有一个协变量在 $0.05$ 水平下单独显著。它们联合起来显著吗？对选出十个协变量系数的 $10\times12$ 矩阵 $C$ 用推论 7.2.2，得 $F_C=1.857$，自由度 $(10,433)$，$p=0.049$：在 $0.05$ 水平下只是勉强显著。单个 $t$ 检验与联合 $F$ 检验回答的是不同的问题，二者不能互相替代。

### 7.2.4. 各层假定的比较

| 假定 | 关键性质 |
|---|---|
| 无 | $\hat{\boldsymbol{Y}}\perp\hat{\boldsymbol{\varepsilon}}$（OLS 的几何性质） |
| Gauss–Markov 模型：$\mathbb{E}\varepsilon_i=0$，$\operatorname{Var}(\varepsilon_i)=\sigma^2$，$\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$（$i\ne j$） | $\operatorname{Cov}(\hat{\boldsymbol{Y}},\hat{\boldsymbol{\varepsilon}})=O$；$\hat{\boldsymbol{\beta}}$ 无偏且为 BLUE；$\hat\sigma^2$ 无偏 |
| 正态线性模型：$\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$ | $\hat{\boldsymbol{Y}}$ 与 $\hat{\boldsymbol{\varepsilon}}$ 独立（概率性质）；精确的 $t$ 与 $F$ 推断 |

正态性虽然是很强的假定，由它导出的方法却对多种偏离是稳健的：由**中心极限定理**，在 Gauss–Markov 模型下 $n$ 很大时 $\hat{\boldsymbol{\beta}}$ 近似正态，$t$ 与 $F$ 方法仍近似成立。

## 7.3. 过拟合、正则化与模型选择

### 7.3.1. 协变量很多的情形

把无用的协变量放进模型会降低估计的精度。协变量总数相对样本量很小时，这无关紧要；但在许多现代应用中并非如此，例如 DNA 测序可以对几百个受试者产生数以百万计的协变量。这时上面的理论就失效了。当 $X$ 的各列高度相关（多重共线性）时，$X^{\mathsf T}X$ 接近奇异，$\operatorname{Cov}(\hat{\boldsymbol{\beta}})=\sigma^2(X^{\mathsf T}X)^{-1}$ 巨大；当 $p>n$ 时，$X^{\mathsf T}X$ 奇异，OLS 估计甚至不唯一。参数很多的模型可以把训练数据拟合得很好，对新数据却预测得很差，这称为过拟合（overfitting）。

可用的补救办法包括方差膨胀因子等诊断指标；RSS、$R^2$ 与调整 $R^2$、信息准则（AIC、BIC）和交叉验证等模型选择准则；以及前向、后向选择等变量选择程序。这些在 [3.3](/3.3) 中展开。这里讨论三种直接修改估计量本身的方法。它们大多最小化带惩罚的目标函数

$$
Q(\boldsymbol{\beta})=\frac{1}{2n}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\sum_{j=1}^pp_\lambda(\lvert\beta_j\rvert),
$$
其中 $p_\lambda(\cdot)$ 是惩罚函数（penalty function），$\lambda\ge0$ 是控制惩罚强度的调节参数（tuning parameter），通常用交叉验证选取。本节始终假定 $X$ 的各列已中心化（均值为零）且 $\boldsymbol{Y}$ 已中心化，于是截距由 $\bar y$ 估计，不受惩罚。

### 7.3.2. 岭回归

**定义 7.3.1（岭回归）** 对 $\lambda>0$，**岭回归**估计为

$$
\hat{\boldsymbol{\beta}}^{\mathrm{Ridge}}(\lambda)=\arg\min_{\boldsymbol{\beta}}\big\{\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\lambda\|\boldsymbol{\beta}\|^2\big\}=(X^{\mathsf T}X+\lambda I_p)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$

令梯度 $-2X^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol{\beta})+2\lambda\boldsymbol{\beta}$ 为零即得闭式解。由于 $X^{\mathsf T}X$ 是**半正定矩阵**，对每个 $\lambda>0$，$X^{\mathsf T}X+\lambda I_p$ 正定从而可逆，即使 $p>n$ 也是如此。

惩罚起了什么作用？取**奇异值分解** $X=UDV^{\mathsf T}$（[2.1](/2.1)），$\boldsymbol{u}_j$ 为 $U$ 的列，奇异值 $d_1\ge\cdots\ge d_p\ge0$。则

$$
X\hat{\boldsymbol{\beta}}^{\mathrm{OLS}}=\sum_{j=1}^p\boldsymbol{u}_j\,\boldsymbol{u}_j^{\mathsf T}\boldsymbol{Y},\qquad X\hat{\boldsymbol{\beta}}^{\mathrm{Ridge}}(\lambda)=UD(D^2+\lambda I_p)^{-1}DU^{\mathsf T}\boldsymbol{Y}=\sum_{j=1}^p\boldsymbol{u}_j\,\frac{d_j^2}{d_j^2+\lambda}\,\boldsymbol{u}_j^{\mathsf T}\boldsymbol{Y}
$$
（第一式在 $X$ 列满秩时成立）。由于 $X$ 的各列已中心化，$X\boldsymbol{v}_j=d_j\boldsymbol{u}_j$ 是协变量的第 $j$ 个样本主成分，$d_j^2/n$ 是它的方差。OLS 以权重 $1$ 把 $\boldsymbol{Y}$ 投影到所有主成分方向上；岭回归则把第 $j$ 个方向上的坐标乘以收缩因子 $d_j^2/(d_j^2+\lambda)$，因此方差小的方向——数据在这些方向上信息很少、OLS 最不稳定——收缩得最多。代价是偏差，$\mathbb{E}\hat{\boldsymbol{\beta}}^{\mathrm{Ridge}}=(X^{\mathsf T}X+\lambda I_p)^{-1}X^{\mathsf T}X\boldsymbol{\beta}\ne\boldsymbol{\beta}$；收获是更小的方差，对合适的 $\lambda$，其**均方误差**比 OLS 小，这是**偏差–方差权衡**的一个实例。

### 7.3.3. 主成分回归

**定义 7.3.2（主成分回归）** **主成分回归**（PCR）先求协变量的主成分（$XV$ 的各列，[3.4.5](/3.4.5)），从中选出若干个，再用 OLS 把 $\boldsymbol{Y}$ 对所选主成分而不是原始协变量作回归。

由于各主成分互不相关，对它们的回归是解耦的；沿用上面的记号，保留主成分集合 $J$ 的 PCR 拟合值为 $\sum_{j\in J}\boldsymbol{u}_j\boldsymbol{u}_j^{\mathsf T}\boldsymbol{Y}$，即收缩因子只取 $1$ 或 $0$，而岭回归是平滑地收缩。通常的做法是保留前 $k$ 个主成分，相当于丢弃方差小的方向。这未必是最好的选择：方差最大的主成分未必对 $Y$ 最有信息，响应可能主要依赖于一个方差很小的主成分（I. Jolliffe，1982）。应当选择对 $Y$ 预测能力最强的主成分，例如按它们与 $Y$ 的相关或用交叉验证来选，而不是按方差大小来选。

### 7.3.4. Lasso

岭回归预测效果好，但它的许多很小却非零的系数难以解释。R. Tibshirani（1996）提出了 **Lasso**（least absolute shrinkage and selection operator），以期同时完成参数估计与重要变量的选择这一宏大目标：

$$
\hat{\boldsymbol{\beta}}^{\mathrm{Lasso}}(\lambda)=\arg\min_{\boldsymbol{\beta}}\Big\{\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\lambda\sum_{j=1}^p\lvert\beta_j\rvert\Big\}.
$$
目标函数是凸的但不可微，没有闭式解；可用坐标下降或 LARS 等算法计算（其理论概述见 [3.2.3](/3.2.3)）。

为比较两种惩罚，先把它们都改写为约束问题。由 Lagrange 对偶，对每个 $\lambda\ge0$ 存在 $t\ge0$，使 Lasso 等价于

$$
\min_{\boldsymbol{\beta}}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2\quad\text{subject to}\quad\sum_{j=1}^p\lvert\beta_j\rvert\le t,
$$
而岭回归是约束为 $\sum_j\beta_j^2\le t$ 的同一问题。其次，目标函数的等高线是以 OLS 估计为中心的椭圆：由于 $X^{\mathsf T}(\boldsymbol{Y}-X\hat{\boldsymbol{\beta}})=\boldsymbol{0}$，下式中交叉项为零，

$$
\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2=(\boldsymbol{Y}-X\hat{\boldsymbol{\beta}})^{\mathsf T}(\boldsymbol{Y}-X\hat{\boldsymbol{\beta}})+(\boldsymbol{\beta}-\hat{\boldsymbol{\beta}})^{\mathsf T}X^{\mathsf T}X(\boldsymbol{\beta}-\hat{\boldsymbol{\beta}}),
$$
这正是 7.1.3 节的勾股分解。约束问题的解就是最小的椭圆 $(\boldsymbol{b}-\hat{\boldsymbol{\beta}})^{\mathsf T}X^{\mathsf T}X(\boldsymbol{b}-\hat{\boldsymbol{\beta}})=c$ 首次碰到约束区域的点。$\ell_1$ 球是菱形（高维时为正轴体），顶点位于坐标轴上，椭圆通常在顶点处与之相切，此时一些系数恰好为零；$\ell_2$ 球是圆的，切点一般各坐标都不为零。

![二维情形的 Lasso 与岭回归：以 OLS 估计为中心的残差平方和椭圆等高线首先碰到 l1 菱形的顶点，得到 b_2 = 0 的稀疏 Lasso 解；碰到 l2 圆盘时切点的两个坐标都不为零](./plots/ridge-lasso-geometry.py)

## 7.4. 模型检验

模型检验是回归分析的重要组成部分，其工具（残差图、杠杆值与影响度量、对假定的检验）属于 [3.3](/3.3)。一个经典的例子说明它为何不可省略。

**例 7.4.1（Anscombe 四重奏）** F. Anscombe（1973）构造了四组各 $11$ 个点的数据，它们的最小二乘拟合几乎完全相同：四组的拟合直线都是 $\hat y=3.00+0.500x$，$R^2\approx0.67$、残差标准误和 $t$ 统计量也都相同。但散点图揭示了根本的差异：第一组像是带噪声的线性关系，第二组是一条光滑曲线，第三组中一个离群点让本来完全落在直线上的数据倾斜，第四组中一个高杠杆点独自决定了斜率。只有模型合适时，回归的数值汇总才有意义，而画出数据是第一道检查。

![Anscombe 四重奏：四组数据的最小二乘直线 y = 3 + 0.5 x 与 R^2 几乎相同，散点图却完全不同](./plots/anscombe-quartet.py)

## 小结

模型 $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$（"线性"指对参数线性）的 OLS 估计 $\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ 使 $\hat{\boldsymbol{Y}}=H\boldsymbol{Y}$ 成为 $\boldsymbol{Y}$ 在 $\mathcal{R}(X)$ 上的正交投影；一个协变量时，标准化后的斜率就是相关系数。它的性质取决于假定：

| | 仅几何 | Gauss–Markov 模型 | 正态线性模型 |
|---|---|---|---|
| $\hat{\boldsymbol{Y}}$ 与 $\hat{\boldsymbol{\varepsilon}}$ | 正交 | 不相关 | 独立 |
| $\hat{\boldsymbol{\beta}}$ | 满足正规方程 | 无偏，$\operatorname{Cov}=\sigma^2(X^{\mathsf T}X)^{-1}$，BLUE | $\mathcal{N}_p(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1})$ |
| $\hat\sigma^2=\operatorname{RSS}/(n-p)$ | — | 无偏 | $\sigma^2\chi^2_{n-p}/(n-p)$，与 $\hat{\boldsymbol{\beta}}$ 独立 |

- 推断与预测：单个线性组合用 $T_{\boldsymbol{c}}\sim t_{n-p}$，多个线性组合用 $F_C\sim F_{l,n-p}$；平均响应的置信区间用 $\boldsymbol{x}^{*\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}^*$，预测区间在根号内再加 $1$。
- 协变量很多时：岭回归沿主成分方向按 $d_j^2/(d_j^2+\lambda)$ 收缩；主成分回归整个保留或丢弃主成分（应按与 $Y$ 的相关而不是方差来选）；Lasso 的 $\ell_1$ 惩罚使一些系数恰为零，从而选择变量。
- 模型检验：完全不同的数据可以给出相同的回归输出（Anscombe 四重奏）；务必先看数据。
- 联系：投影与谱的工具来自 [2.1](/2.1) 与 [3.4.1](/3.4.1)，分布理论来自 [3.4.2](/3.4.2)；$F$ 统计量与 Hotelling $T^2$（[3.4.3](/3.4.3)）相对应；[3.4.8](/3.4.8) 的因子得分和 [3.4.9](/3.4.9) 的复相关系数都沿用了本章最小二乘的思想。
