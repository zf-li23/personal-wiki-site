---
title: 因子分析
description: 正交因子模型及其协方差结构，不可识别性与尺度不变性，用主成分法和极大似然法估计载荷以及因子个数的检验，方差最大旋转，用加权最小二乘法和回归法计算因子得分，以及实际应用的策略。
source_hash: e9a1594adf24
---

因子分析（factor analysis）用少数几个不可观测的变量——因子——来解释许多观测变量之间的相关。它起源于心理测量：K. Pearson 与 C. Spearman 想知道，儿童各科成绩彼此正相关，能否用单一的"一般智力"来解释。模型有两个目的：约简（用远少于 $p(p+1)/2$ 个参数描述 $p\times p$ 协方差矩阵）与解释（用有含义的潜在因子解释协方差）。因子分析与 [3.4.5](/3.4.5) 的**主成分分析**密切相关，后者提供了它的一种估计方法；但两者有本质区别：主成分是观测变量的线性组合，而因子分析把观测变量建模为因子的线性组合加误差，并且模型只在相差一个旋转的意义下可识别。本章先介绍正交因子模型（8.1 节），再在总体水平用主成分法与极大似然法估计其参数（8.2 节），通过旋转使解易于解释（8.3 节），在个体水平估计每个个体的因子值（8.4 节），最后给出实际应用的策略（8.5 节）。本章用到 [2.1](/2.1) 的**谱分解**、**多元正态分布**及其条件分布（[3.4.2](/3.4.2)）、似然比检验（[3.2.5](/3.2.5)）和 [3.4.7](/3.4.7) 的最小二乘；[3.4.9](/3.4.9) 的典型相关分析是针对两组变量的类似方法。

## 8.1. 正交因子模型

### 8.1.1. 动机

**例 8.1.1（考试成绩）** 两名高中生六科总分都是 $511$，但学生 A 的数学、物理、化学为 $98,97,93$，历史、政治、语文为 $73,70,80$；学生 B 则分别为 $75,71,80$ 与 $95,94,96$。全体学生六科成绩的相关矩阵呈现两个块：三门理科之间的相关为 $0.35$–$0.44$，三门文科之间为 $0.46$–$0.61$，而跨块的相关只有 $0.16$–$0.32$。这提示存在两种潜在能力，"理科因子" $F_1$ 与"文科因子" $F_2$，例如对数学成绩 $X_1$ 与语文成绩 $X_2$ 有

$$
\begin{bmatrix}X_1\\X_2\end{bmatrix}-\begin{bmatrix}50\\60\end{bmatrix}=\begin{bmatrix}0.8&0.2\\0.1&0.9\end{bmatrix}\begin{bmatrix}F_1\\F_2\end{bmatrix}+\begin{bmatrix}\varepsilon_1\\\varepsilon_2\end{bmatrix},
$$
其中 $\varepsilon_1$、$\varepsilon_2$ 分别是数学与语文特有的部分。这样，学生 A 和 B 就由他们的 $(F_1,F_2)$ 而不是六个分数来刻画。

**例 8.1.2（Spearman，1904）** Spearman 观察到儿童在 $X_1$ = 古典文学、$X_2$ = 法语、$X_3$ = 英语三科成绩的相关矩阵

$$
R=\begin{bmatrix}1&0.83&0.78\\0.83&1&0.67\\0.78&0.67&1\end{bmatrix},
$$
并提出单因子模型 $X_i=l_iF+\varepsilon_i$，$i=1,2,3$：三科成绩背后有一个共同的公共因子 $F$。大五人格测验之类的问卷就是这一思想的现代后继。

### 8.1.2. 模型

**定义 8.1.1（正交因子模型）** 设可观测的 $p$ 维随机向量 $\boldsymbol{X}$ 的均值为 $\boldsymbol{\mu}$，协方差矩阵为 $\Sigma$。含 $m$ 个公共因子的**正交因子模型**假定

$$
\underset{(p\times1)}{\boldsymbol{X}-\boldsymbol{\mu}}=\underset{(p\times m)}{L}\ \underset{(m\times1)}{\boldsymbol{F}}+\underset{(p\times1)}{\boldsymbol{\varepsilon}},\qquad\text{即}\qquad X_i-\mu_i=l_{i1}F_1+l_{i2}F_2+\cdots+l_{im}F_m+\varepsilon_i,\quad i=1,\dots,p,
$$
其中 $\boldsymbol{F}$ 与 $\boldsymbol{\varepsilon}$ 是不可观测的随机向量，满足

$$
\mathbb{E}(\boldsymbol{F})=\boldsymbol{0},\quad\operatorname{Cov}(\boldsymbol{F})=\mathbb{E}(\boldsymbol{F}\boldsymbol{F}^{\mathsf T})=I_m,\qquad\mathbb{E}(\boldsymbol{\varepsilon})=\boldsymbol{0},\quad\operatorname{Cov}(\boldsymbol{\varepsilon})=\Psi=\operatorname{diag}(\psi_1,\dots,\psi_p),\qquad\operatorname{Cov}(\boldsymbol{\varepsilon},\boldsymbol{F})=\mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{F}^{\mathsf T})=O.
$$
$\boldsymbol{F}$ 的分量称为**公共因子**，$\boldsymbol{\varepsilon}$ 的分量称为**特殊因子**，$l_{ij}$ 称为第 $i$ 个变量在第 $j$ 个因子上的**因子载荷**，$L=(l_{ij})$ 为因子载荷矩阵。

"正交"指因子互不相关。每个特殊因子 $\varepsilon_i$ 只影响 $X_i$，特殊因子之间以及与公共因子都不相关，所以观测变量之间的一切相关都必须经由公共因子传递。模型对因子是线性的，未知参数为 $\boldsymbol{\mu}$、$L$ 与 $\Psi$。

### 8.1.3. 模型蕴含的协方差结构

由 $(\boldsymbol{X}-\boldsymbol{\mu})(\boldsymbol{X}-\boldsymbol{\mu})^{\mathsf T}=(L\boldsymbol{F}+\boldsymbol{\varepsilon})(L\boldsymbol{F}+\boldsymbol{\varepsilon})^{\mathsf T}=L\boldsymbol{F}\boldsymbol{F}^{\mathsf T}L^{\mathsf T}+\boldsymbol{\varepsilon}\boldsymbol{F}^{\mathsf T}L^{\mathsf T}+L\boldsymbol{F}\boldsymbol{\varepsilon}^{\mathsf T}+\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^{\mathsf T}$，取期望得

$$
\Sigma=\operatorname{Cov}(\boldsymbol{X})=L\,\mathbb{E}(\boldsymbol{F}\boldsymbol{F}^{\mathsf T})L^{\mathsf T}+\mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{F}^{\mathsf T})L^{\mathsf T}+L\,\mathbb{E}(\boldsymbol{F}\boldsymbol{\varepsilon}^{\mathsf T})+\mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^{\mathsf T})=LL^{\mathsf T}+\Psi,
$$
类似地 $\operatorname{Cov}(\boldsymbol{X},\boldsymbol{F})=\mathbb{E}(\boldsymbol{X}-\boldsymbol{\mu})\boldsymbol{F}^{\mathsf T}=\mathbb{E}(L\boldsymbol{F}+\boldsymbol{\varepsilon})\boldsymbol{F}^{\mathsf T}=L$。按分量写，记 $\boldsymbol{l}_i^{\mathsf T}$ 为 $L$ 的第 $i$ 行，

$$
\sigma_{ii}=\underbrace{l_{i1}^2+l_{i2}^2+\cdots+l_{im}^2}_{h_i^2}+\psi_i,\qquad\sigma_{ik}=\operatorname{Cov}(X_i,X_k)=\boldsymbol{l}_i^{\mathsf T}\boldsymbol{l}_k=l_{i1}l_{k1}+\cdots+l_{im}l_{km}\ (i\ne k),\qquad\operatorname{Cov}(X_i,F_j)=l_{ij}.
$$
于是 $X_i$ 的方差分解为共同度（communality）$h_i^2=\sum_jl_{ij}^2$，即公共因子解释的部分，与特殊方差（specific variance）$\psi_i$。协方差完全由载荷产生，载荷 $l_{ij}$ 就是 $X_i$ 与 $F_j$ 的协方差（$X_i$ 标准化时即相关系数）。

**例 8.1.3** 协方差矩阵

$$
\Sigma=\begin{bmatrix}19&30&2&12\\30&57&5&23\\2&5&38&47\\12&23&47&68\end{bmatrix}=\begin{bmatrix}4&1\\7&2\\-1&6\\1&8\end{bmatrix}\begin{bmatrix}4&7&-1&1\\1&2&6&8\end{bmatrix}+\begin{bmatrix}2&0&0&0\\0&4&0&0\\0&0&1&0\\0&0&0&3\end{bmatrix}
$$
具有 $m=2$ 时 $LL^{\mathsf T}+\Psi$ 的形式。对第一个变量，$\sigma_{11}=19=h_1^2+\psi_1$，共同度 $h_1^2=l_{11}^2+l_{12}^2=4^2+1^2=17$，特殊方差 $\psi_1=2$。

这里有一个有用的几何图像。对方差有限的中心化随机变量，$\langle U,W\rangle=\mathbb{E}(UW)$ 是内积，其中 $U$ 的长度是它的标准差，$U$ 与 $W$ 夹角的余弦是它们的相关系数。在这个空间里，$F_1,\dots,F_m$ 构成标准正交组，$X_i-\mu_i=\tilde X_i+\varepsilon_i$，其中 $\tilde X_i=l_{i1}F_1+\cdots+l_{im}F_m$ 位于因子张成的子空间内，$\varepsilon_i$ 与该子空间以及其他每个 $\varepsilon_k$ 都正交。载荷 $l_{ij}=\langle X_i,F_j\rangle$ 是 $\tilde X_i$ 在因子基下的坐标，$h_i^2=\|\tilde X_i\|^2$，$\psi_i=\|\varepsilon_i\|^2$。

### 8.1.4. 约简、不可识别性与尺度不变性

约简。协方差矩阵有 $p(p+1)/2$ 个自由参数，而 $LL^{\mathsf T}+\Psi$ 有 $pm+p$ 个。$p=12$、$m=2$ 时为 $36$ 个而不是 $78$ 个。只有当 $m$ 远小于 $p$ 时模型才有用，而它有一个实质性的局限：并非每个协方差矩阵都能在 $m\ll p$ 时分解为 $LL^{\mathsf T}+\Psi$。即使分解在数学上存在，在统计上也可能毫无意义。若例 8.1.3 中的 $\sigma_{11}$ 是 $15$ 而不是 $19$（仍是合法的协方差矩阵），同样的 $L$ 就迫使 $\psi_1=15-17=-2<0$。对相关矩阵

$$
R=\begin{bmatrix}1&0.9&0.7\\0.9&1&0.4\\0.7&0.4&1\end{bmatrix}
$$
与 $m=1$，方程 $l_1l_2=0.9$、$l_1l_3=0.7$、$l_2l_3=0.4$ 给出 $l_1^2=0.9\cdot0.7/0.4=1.575$，于是 $\operatorname{Corr}(X_1,F)=l_1=1.255>1$，$\psi_1=1-1.575=-0.575<0$。特殊方差为负（或为零）的解称为 Heywood 情形（Heywood case），得名于 H. B. Heywood（1931）。

不可识别性。设 $T$ 是任意 $m\times m$ **正交矩阵**，则

$$
\boldsymbol{X}-\boldsymbol{\mu}=L\boldsymbol{F}+\boldsymbol{\varepsilon}=LTT^{\mathsf T}\boldsymbol{F}+\boldsymbol{\varepsilon}=L^*\boldsymbol{F}^*+\boldsymbol{\varepsilon},\qquad L^*=LT,\quad\boldsymbol{F}^*=T^{\mathsf T}\boldsymbol{F},
$$
且 $\boldsymbol{F}^*$ 满足模型假定：$\mathbb{E}\boldsymbol{F}^*=\boldsymbol{0}$，$\operatorname{Cov}(\boldsymbol{F}^*)=T^{\mathsf T}T=I_m$，$\operatorname{Cov}(\boldsymbol{\varepsilon},\boldsymbol{F}^*)=O$。又 $L^*L^{*\mathsf T}=LL^{\mathsf T}$，所以 $\Sigma$ 无法区分 $L$ 与 $LT$：载荷只在相差一个正交变换的意义下确定。这一自由度（从上面的参数计数中扣除 $m(m-1)/2$ 个）有两种用法：旋转因子使之易于解释（8.3 节），以及施加一个便于计算的约束，使极大似然估计有确定的解（8.2.2 节）。

尺度不变性。设 $C=\operatorname{diag}(c_1,\dots,c_p)$，$c_i\ne0$，$\boldsymbol{Y}=C\boldsymbol{X}$（更换单位）。则

$$
\boldsymbol{Y}=C\boldsymbol{\mu}+CL\boldsymbol{F}+C\boldsymbol{\varepsilon}=\boldsymbol{\mu}_C+L_C\boldsymbol{F}+\boldsymbol{\varepsilon}_C,
$$
由于 $C$ 是对角的，$\operatorname{Cov}(\boldsymbol{\varepsilon}_C)=C\Psi C$ 仍为对角矩阵。因此 $\boldsymbol{Y}$ 服从具有同样因子的 $m$ 因子模型：因子分析不受变量尺度变换的影响。特别地，对标准化变量 $\boldsymbol{Z}=V^{-1/2}(\boldsymbol{X}-\boldsymbol{\mu})$，$V=\operatorname{diag}(\sigma_{11},\dots,\sigma_{pp})$，

$$
\boldsymbol{Z}=L_z\boldsymbol{F}+\boldsymbol{\varepsilon}_z,\qquad L_z=V^{-1/2}L,\qquad\Psi_z=V^{-1/2}\Psi V^{-1/2},\qquad\rho=L_zL_z^{\mathsf T}+\Psi_z,
$$
其中 $\rho$ 是 $\boldsymbol{X}$ 的相关矩阵。主成分没有这样的不变性（[3.4.5](/3.4.5)）。

### 8.1.5. 总体水平与个体水平

设 $\boldsymbol{x}_1,\dots,\boldsymbol{x}_n$ 是来自 $p$ 维总体的 $n$ 个独立观测，$\boldsymbol{\mu}$ 与 $\Sigma$ 未知，数据由**样本协方差矩阵** $S$ 或**样本相关矩阵** $R$ 概括。因子分析在两个不同的水平上有两个目标。

- 总体水平：给定 $m$，求 $\hat L$ 与 $\hat\Psi$ 使 $S\approx\hat L\hat L^{\mathsf T}+\hat\Psi$（8.2 节），并在适当旋转之后通过载荷赋予因子含义（8.3 节）。这些参数描述的是所有个体共有的规律。
- 个体水平：给定 $\hat L$ 与 $\hat\Psi$，估计每个个体的因子值，即因子得分（8.4 节）。

例如，观测了 $n=100$ 名学生 $p=6$ 门课的成绩并取 $m=2$，则 $6\times2$ 矩阵 $L$ 与 $6\times6$ 对角矩阵 $\Psi$ 说明，有一个共同的"理科因子"和一个共同的"文科因子"影响所有成绩，且对每名学生影响的强度（载荷）都相同；如果模型正确，换一批学生也应呈现同样的规律。但每名学生有各自的因子值，例如擅长文科的学生为 $(0.3,1.5)$，擅长理科的学生为 $(1.2,0.4)$。

## 8.2. 载荷的估计

### 8.2.1. 主成分法

由谱分解，$\Sigma=\sum_{i=1}^p\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$，特征值 $\lambda_1\ge\cdots\ge\lambda_p\ge0$，$\boldsymbol{e}_i$ 为标准正交的特征向量，即

$$
\Sigma=\begin{bmatrix}\sqrt{\lambda_1}\boldsymbol{e}_1&\sqrt{\lambda_2}\boldsymbol{e}_2&\cdots&\sqrt{\lambda_p}\boldsymbol{e}_p\end{bmatrix}\begin{bmatrix}\sqrt{\lambda_1}\boldsymbol{e}_1^{\mathsf T}\\\vdots\\\sqrt{\lambda_p}\boldsymbol{e}_p^{\mathsf T}\end{bmatrix}=L_0L_0^{\mathsf T}+O.
$$
这是精确的分解，但毫无用处：公共因子与变量一样多，也没有特殊方差。当后 $p-m$ 个特征值很小时，略去它们的贡献，$\Sigma\approx\sum_{i=1}^m\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}=LL^{\mathsf T}$，$L$ 为 $p\times m$ 矩阵，并令剩余部分的对角元为特殊方差。

**定义 8.2.1（主成分法）** 设 $(\hat\lambda_1,\hat{\boldsymbol{e}}_1),\dots,(\hat\lambda_p,\hat{\boldsymbol{e}}_p)$ 是 $S$（或 $R$）的特征对，$\hat\lambda_1\ge\cdots\ge\hat\lambda_p$。**主成分法**用

$$
\tilde L=\begin{bmatrix}\sqrt{\hat\lambda_1}\,\hat{\boldsymbol{e}}_1&\sqrt{\hat\lambda_2}\,\hat{\boldsymbol{e}}_2&\cdots&\sqrt{\hat\lambda_m}\,\hat{\boldsymbol{e}}_m\end{bmatrix},\qquad\tilde\Psi=\operatorname{diag}\big(S-\tilde L\tilde L^{\mathsf T}\big),\quad\text{即}\quad\tilde\psi_i=s_{ii}-\sum_{j=1}^m\tilde l_{ij}^2
$$
估计载荷与特殊方差，用 $\tilde h_i^2=\tilde l_{i1}^2+\cdots+\tilde l_{im}^2$ 估计共同度。

按构造，$S$ 的对角元被精确再现，但残差矩阵 $S-(\tilde L\tilde L^{\mathsf T}+\tilde\Psi)$ 的非对角元一般不为零。$\tilde L$ 的各列与 $m$ 无关：增加因子个数只是添加新的列，原有各列不变。

**例 8.2.1** 把例 8.1.3 的矩阵当作样本协方差矩阵 $S$。其特征值为 $116.27$、$61.42$、$2.52$、$1.80$，主成分解为（列的符号可任取，数值已四舍五入）

| $m$ | $\tilde L$（每行一个变量） | $\operatorname{diag}(\tilde\Psi)$ |
|---|---|---|
| $1$ | $(-2.5),(-4.8),(-5.1),(-7.8)$ | $12.6,\ 34.4,\ 12.2,\ 6.5$ |
| $2$ | $(-2.5,3.3),(-4.8,5.8),(-5.1,-3.3),(-7.8,-2.4)$ | $1.9,\ 0.6,\ 1.1,\ 0.7$ |
| $3$ | 再添第三列 $(1.3,-0.8,-0.3,0.2)$ | $0.1,\ 0.0,\ 1.0,\ 0.6$ |

$m=2$ 时非对角残差的绝对值至多为 $1.05$，$S\approx\tilde L\tilde L^{\mathsf T}+\tilde\Psi$ 很好地再现了 $S$；$m=1$ 时残差可达 $19$。注意，估计出的 $\tilde L$、$\tilde\Psi$ 与例 8.1.3 中构造 $S$ 所用的 $L$、$\Psi$ 不同，尽管两者都能很好地再现 $S$：载荷不唯一，而且主成分法往往把过多的方差归于公共因子。

因子个数取多少？与 PCA 一样，残差矩阵衡量近似的好坏。

**命题 8.2.1** 对主成分解，

$$
\sum_{i,k}\Big[S-\big(\tilde L\tilde L^{\mathsf T}+\tilde\Psi\big)\Big]_{ik}^2\le\hat\lambda_{m+1}^2+\cdots+\hat\lambda_p^2.
$$

**证明** $S-\tilde L\tilde L^{\mathsf T}=\sum_{i>m}\hat\lambda_i\hat{\boldsymbol{e}}_i\hat{\boldsymbol{e}}_i^{\mathsf T}$ 的 **Frobenius 范数**平方为 $\sum_{i>m}\hat\lambda_i^2$。减去 $\tilde\Psi$ 只是把对角元置为零而不改变非对角元，平方和只会减小。$\square$

因此被略去的特征值平方和小，就意味着近似误差的平方和小（例 8.2.1 中 $m=2$ 时：$3.9\le\hat\lambda_3^2+\hat\lambda_4^2=9.6$）。另一个角度是解释的方差。样本总方差为 $\operatorname{tr}(S)=s_{11}+\cdots+s_{pp}$，第 $j$ 个公共因子的贡献为 $\tilde l_{1j}^2+\cdots+\tilde l_{pj}^2=\hat\lambda_j\|\hat{\boldsymbol{e}}_j\|^2=\hat\lambda_j$，所以 $m$ 个公共因子解释的总方差比例为

$$
\frac{\hat\lambda_1+\cdots+\hat\lambda_m}{\operatorname{tr}(S)}\qquad\Big(\text{对 }R\text{ 为 }\frac{\hat\lambda_1+\cdots+\hat\lambda_m}{p}\Big).
$$
例 8.2.1 中 $m=2$ 时为 $(116.27+61.42)/182=0.976$。因此选择主成分个数的规则（累计比例、碎石图、$R$ 的特征值大于 $1$）都可以沿用。

**例 8.2.2（消费者偏好）** 在一项消费者偏好研究中，一组顾客从五个方面对一种新食品打分。样本相关矩阵为

$$
R=\begin{bmatrix}1&0.02&0.96&0.42&0.01\\0.02&1&0.13&0.71&0.85\\0.96&0.13&1&0.50&0.11\\0.42&0.71&0.50&1&0.79\\0.01&0.85&0.11&0.79&1\end{bmatrix},
$$
变量依次为（口味、物有所值、风味、适合作零食、提供大量能量）。$R$ 只有两个特征值 $2.85$ 与 $1.81$ 大于 $1$，二者合计解释了标准化总方差的 $93.2\%$，因此取 $m=2$。主成分解为

| 变量 | $\tilde l_{i1}$ | $\tilde l_{i2}$ | $\tilde h_i^2$ | $\tilde\psi_i$ |
|---|---|---|---|---|
| 口味 | $0.56$ | $0.82$ | $0.98$ | $0.02$ |
| 物有所值 | $0.78$ | $-0.53$ | $0.88$ | $0.12$ |
| 风味 | $0.65$ | $0.75$ | $0.98$ | $0.02$ |
| 适合作零食 | $0.94$ | $-0.10$ | $0.89$ | $0.11$ |
| 提供大量能量 | $0.80$ | $-0.54$ | $0.93$ | $0.07$ |
| 特征值 | $2.85$ | $1.81$ | | |
| 累计比例 | $0.571$ | $0.932$ | | |

共同度都很高，两个因子很好地解释了五项评分；但因子的含义还不清楚，8.3 节将回到这个例子。

### 8.2.2. 极大似然法

主成分法不需要分布假定。若公共因子与特殊因子服从联合正态分布，就可以用极大似然估计参数。

设 $\boldsymbol{F}\sim\mathcal{N}_m(\boldsymbol{0},I_m)$，$\boldsymbol{\varepsilon}\sim\mathcal{N}_p(\boldsymbol{0},\Psi)$，二者独立。则 $\boldsymbol{X}\sim\mathcal{N}_p(\boldsymbol{\mu},\Sigma)$，$\Sigma=LL^{\mathsf T}+\Psi$，样本的似然函数为

$$
\begin{aligned}
L(\boldsymbol{\mu},\Sigma)&=(2\pi)^{-\frac{np}{2}}\lvert\Sigma\rvert^{-\frac n2}\exp\Big\{-\frac12\operatorname{tr}\Big[\Sigma^{-1}\Big(\sum_{j=1}^n(\boldsymbol{x}_j-\bar{\boldsymbol{x}})(\boldsymbol{x}_j-\bar{\boldsymbol{x}})^{\mathsf T}+n(\bar{\boldsymbol{x}}-\boldsymbol{\mu})(\bar{\boldsymbol{x}}-\boldsymbol{\mu})^{\mathsf T}\Big)\Big]\Big\}\\
&=(2\pi)^{-\frac{(n-1)p}{2}}\lvert\Sigma\rvert^{-\frac{n-1}{2}}\exp\Big\{-\frac12\operatorname{tr}\Big[\Sigma^{-1}\sum_{j=1}^n(\boldsymbol{x}_j-\bar{\boldsymbol{x}})(\boldsymbol{x}_j-\bar{\boldsymbol{x}})^{\mathsf T}\Big]\Big\}\times(2\pi)^{-\frac p2}\lvert\Sigma\rvert^{-\frac12}\exp\Big\{-\frac n2(\bar{\boldsymbol{x}}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\bar{\boldsymbol{x}}-\boldsymbol{\mu})\Big\}.
\end{aligned}
$$
它只通过 $\Sigma=LL^{\mathsf T}+\Psi$ 依赖于 $L$ 与 $\Psi$，所以由不可识别性，使之最大的 $L$ 不唯一。为此施加一个便于计算的唯一性条件

$$
L^{\mathsf T}\Psi^{-1}L=\Delta,\qquad\Delta\text{ 为对角矩阵}.
$$

这个条件总能满足，并且从每一类等价的载荷中挑出一个代表。若 $L_1=L_2P$，$P$ 正交，则称 $L_1$ 与 $L_2$ 等价；等价的载荷给出相同的 $\Sigma$，似然无法区分它们。对任意 $L_1$，对称矩阵 $B=L_1^{\mathsf T}\Psi^{-1}L_1$ 有谱分解 $B=P\Delta P^{\mathsf T}$，而 $L_0=L_1P$ 与 $L_1$ 等价且 $L_0^{\mathsf T}\Psi^{-1}L_0=P^{\mathsf T}BP=\Delta$ 为对角矩阵。当 $\Delta$ 的对角元互不相同时，$L_0$ 在相差各列符号的意义下唯一。最大化需用数值方法完成（迭代算法，或 [3.5](/3.5) 中的 EM 算法）。

**定理 8.2.1** 设 $\boldsymbol{X}_1,\dots,\boldsymbol{X}_n$ 是来自 $\mathcal{N}_p(\boldsymbol{\mu},\Sigma)$ 的随机样本，其中 $\Sigma=LL^{\mathsf T}+\Psi$ 是 $m$ 因子模型的协方差矩阵；设 $\hat L$、$\hat\Psi$ 与 $\hat{\boldsymbol{\mu}}=\bar{\boldsymbol{x}}$ 是在 $\hat L^{\mathsf T}\hat\Psi^{-1}\hat L$ 为对角矩阵的约束下的极大似然估计。则共同度的极大似然估计为

$$
\hat h_i^2=\hat l_{i1}^2+\hat l_{i2}^2+\cdots+\hat l_{im}^2,\qquad i=1,\dots,p,
$$
第 $j$ 个因子所占样本总方差的比例为

$$
\frac{\hat l_{1j}^2+\hat l_{2j}^2+\cdots+\hat l_{pj}^2}{s_{11}+s_{22}+\cdots+s_{pp}}.
$$

第一个结论由极大似然估计的不变性（[3.2.3](/3.2.3)）得出；第二个随之成为定义。由同样的不变性和模型的尺度不变性，标准化变量的估计可以直接由原始变量的估计得到：

$$
\hat L_z=\hat V^{-1/2}\hat L,\qquad\hat\Psi_z=\hat V^{-1/2}\hat\Psi\hat V^{-1/2},\qquad\hat V=\operatorname{diag}(\hat\sigma_{11},\dots,\hat\sigma_{pp}),
$$
所以对 $S$ 和对 $R$ 做极大似然因子分析是等价的。对 $R$，第 $j$ 个因子所占比例为 $(\hat l_{1j}^2+\cdots+\hat l_{pj}^2)/p$，其中为标准化载荷。

**例 8.2.3（股票价格）** 记录了五只股票（JPMorgan、Citibank、Wells Fargo、Royal Dutch Shell、ExxonMobil）连续 $n=103$ 周的周收益率。对样本相关矩阵拟合两因子模型，得

| 变量 | ML $\hat l_{i1}$ | ML $\hat l_{i2}$ | ML $\hat\psi_i$ | PC $\tilde l_{i1}$ | PC $\tilde l_{i2}$ | PC $\tilde\psi_i$ |
|---|---|---|---|---|---|---|
| JPMorgan | $0.115$ | $0.755$ | $0.42$ | $0.732$ | $-0.437$ | $0.27$ |
| Citibank | $0.322$ | $0.788$ | $0.27$ | $0.831$ | $-0.280$ | $0.23$ |
| Wells Fargo | $0.182$ | $0.652$ | $0.54$ | $0.726$ | $-0.374$ | $0.33$ |
| Royal Dutch Shell | $1.000$ | $-0.000$ | $0.00$ | $0.605$ | $0.694$ | $0.15$ |
| ExxonMobil | $0.683$ | $-0.032$ | $0.53$ | $0.563$ | $0.719$ | $0.17$ |
| 累计比例 | $0.323$ | $0.647$ | | $0.487$ | $0.769$ | |

主成分解有一个一般的"市场因子" $F_1$（所有股票的载荷大致相当），以及一个石油股与银行股的对比 $F_2$（"行业因子"）。极大似然解则给出一个石油因子和一个银行因子；它对 Shell 的估计 $\hat\psi_4=0.00$ 落在边界上，是一个 Heywood 情形。$\tilde L$ 的各列正交（它们是缩放后的特征向量），$\hat L$ 的各列则不一定；主成分法给出的特殊方差更小、解释的方差比例更大，因为它本来就是为最大化解释的方差而设计的。（R 的 `factanal` 给出的极大似然值略有不同，例如 JPMorgan 的载荷为 $0.121$、$0.754$，特殊方差为 $0.417,0.275,0.542,0.005,0.530$。）

### 8.2.3. 公共因子个数的大样本检验

在正态性下，可以检验 $m$ 个因子是否足够：

$$
H_0\colon\underset{(p\times p)}{\Sigma}=\underset{(p\times m)}{L}\ \underset{(m\times p)}{L^{\mathsf T}}+\underset{(p\times p)}{\Psi}\ \ \text{（且 }L^{\mathsf T}\Psi^{-1}L=\Delta\text{ 为对角矩阵）}\qquad\text{vs.}\qquad H_1\colon\Sigma\text{ 为任何其他正定矩阵}.
$$
在 $H_1$ 下，极大似然估计为 $\hat{\boldsymbol{\mu}}=\bar{\boldsymbol{x}}$、$\hat\Sigma=S_n=\frac{n-1}{n}S$，最大似然值正比于 $\lvert S_n\rvert^{-n/2}\mathrm{e}^{-np/2}$；在 $H_0$ 下为 $\bar{\boldsymbol{x}}$ 与 $\hat\Sigma=\hat L\hat L^{\mathsf T}+\hat\Psi$，最大似然值正比于 $\lvert\hat L\hat L^{\mathsf T}+\hat\Psi\rvert^{-n/2}\exp\big\{-\frac n2\operatorname{tr}\big[(\hat L\hat L^{\mathsf T}+\hat\Psi)^{-1}S_n\big]\big\}$。**似然比检验**的统计量为

$$
-2\ln\Lambda=-2\ln\frac{H_0\text{ 下的最大似然值}}{\text{最大似然值}}=n\ln\frac{\lvert\hat L\hat L^{\mathsf T}+\hat\Psi\rvert}{\lvert S_n\rvert}+n\Big[\operatorname{tr}\big((\hat L\hat L^{\mathsf T}+\hat\Psi)^{-1}S_n\big)-p\Big],
$$
在极大似然估计处迹项为零。由 **Wilks 定理**，$n$ 很大时它近似服从 $\chi^2_{\nu-\nu_0}$，自由度是自由参数个数之差：

- $H_1$ 下：$\nu=p(p+1)/2$；
- $H_0$ 下：$L$ 与 $\Psi$ 共 $p(m+1)$ 个参数，减去约束施加的 $m(m-1)/2$ 个方程（对称的 $m\times m$ 矩阵 $L^{\mathsf T}\Psi^{-1}L$ 的每个非对角元都必须为零），故 $\nu_0=p(m+1)-m(m-1)/2$；

$$
\nu-\nu_0=\frac12p(p+1)-p(m+1)+\frac12m(m-1)=\frac12\big[(p-m)^2-p-m\big].
$$
检验要求 $\nu-\nu_0>0$，这限制了可检验的因子个数。Bartlett 修正把 $n$ 换成 $n-1-(2p+4m+5)/6$，改善卡方近似，标准软件都采用它。

**例 8.2.4（股票价格，续）** $p=5$ 时，检验 $m=2$ 的自由度为 $\frac12[(5-2)^2-7]=1$；R 的 `factanal` 给出 $\chi^2=1.97$，$p$ 值 $0.16$，所以两个因子足够。$m=1$ 时自由度为 $\frac12[16-6]=5$，$\chi^2=62.22$，$p$ 值 $4.2\times10^{-12}$：一个因子显然不够。

### 8.2.4. 两种方法的比较

| | 主成分法 | 极大似然法 |
|---|---|---|
| 假定 | 模型之外无额外假定 | $\boldsymbol{F}$ 与 $\boldsymbol{\varepsilon}$ 联合正态 |
| 唯一性 | $\tilde L$ 各列正交（来自特征向量） | $L^{\mathsf T}\Psi^{-1}L$ 为对角矩阵 |
| 计算 | 显式；不同 $m$ 的解嵌套 | 迭代优化 |
| 协方差还是相关 | 对 $S$ 和对 $R$ 结果不同 | 对 $S$ 和对 $R$ 的结果可以互相换算 |
| 选择 $m$ | 同 PCA（比例、$R$ 的特征值大于 $1$） | 似然比检验 |
| 缺点 | $\tilde\Psi$ 只是剩余部分；非对角拟合未经优化 | 依赖正态性；可能出现 Heywood 情形 |

实际中两种方法都要计算并加以比较（8.5 节）。

## 8.3. 因子旋转

### 8.3.1. 为什么要旋转

任何 $\hat L^*=\hat LT$（$T$ 正交）都是同样好的估计。PCA 不能旋转，因为那里的主成分由逐次最大化方差定义，方向已被固定；而因子分析只确定了因子张成的空间。旋转改变了什么？

- 不变的：估计的协方差矩阵 $\hat L^*\hat L^{*\mathsf T}+\hat\Psi=\hat L\hat L^{\mathsf T}+\hat\Psi$、残差矩阵、特殊方差 $\hat\psi_i$ 与共同度 $\hat h_i^2$（$\hat L$ 各行的长度不变），从而 $m$ 个因子解释的总方差比例也不变。
- 改变的：各个载荷、归于每个因子的方差比例，以及因子的解释。

旋转的目的在于解释。理想情况下，每个变量只在一个因子上有高载荷，在其他因子上的载荷小或适中。在例 8.2.2 中，若载荷模式为

| | 口味 | 物有所值 | 风味 | 零食 | 能量 |
|---|---|---|---|---|---|
| $F_1^*$ | $1$ | $0$ | $1$ | $0$ | $0$ |
| $F_2^*$ | $0$ | $1$ | $0$ | $1$ | $1$ |

就会得到清晰的"口味"因子与"营养"因子，而未旋转的载荷把二者混在一起。

### 8.3.2. 方差最大准则

**定义 8.3.1（方差最大旋转）** 设 $\hat l_{ij}^*$ 为旋转后的载荷，$\tilde l_{ij}^*=\hat l_{ij}^*/\hat h_i$ 为按共同度平方根缩放后的载荷。**方差最大旋转**在所有正交矩阵 $T$ 中选取使

$$
V=\frac1p\sum_{j=1}^m\Big[\sum_{i=1}^p\big(\tilde l_{ij}^*\big)^4-\frac1p\Big(\sum_{i=1}^p\big(\tilde l_{ij}^*\big)^2\Big)^2\Big]
$$
最大的一个，再把旋转后的缩放载荷乘回 $\hat h_i$。

这个准则背后有三个想法。载荷的重要性取决于大小而不是符号，所以准则使用平方 $(\tilde l_{ij}^*)^2$。按 $\hat h_i$ 缩放使共同度小的变量与共同度大的变量有相同的权重。最后，$V$ 正比于 $\sum_{j=1}^m$（第 $j$ 列缩放载荷平方的方差），因此最大化 $V$ 就是让每个因子上载荷的平方尽量分散，把它们推向 $0$ 或 $\pm1$。最大化必须限制在正交矩阵 $T$ 中进行；在任意矩阵中最大化是没有意义的。二维时 $T$ 是转角为 $\phi$ 的旋转（可能再加一个反射），可以直接对 $V(\phi)$ 求最大。

**例 8.3.1（消费者偏好，续）** 对例 8.2.2 的主成分载荷做方差最大旋转，相当于把因子轴转过约 $33^\circ$：

| 变量 | $\tilde l_{i1}^*$ | $\tilde l_{i2}^*$ | $\tilde h_i^2$ |
|---|---|---|---|
| 口味 | $0.02$ | $0.99$ | $0.98$ |
| 物有所值 | $0.94$ | $-0.01$ | $0.88$ |
| 风味 | $0.13$ | $0.98$ | $0.98$ |
| 适合作零食 | $0.84$ | $0.43$ | $0.89$ |
| 提供大量能量 | $0.97$ | $-0.02$ | $0.93$ |
| 累计比例 | $0.507$ | $0.932$ | |

现在物有所值、零食与能量在 $F_1^*$ 上有高载荷，是营养因子；口味与风味在 $F_2^*$ 上，是口味因子。共同度和累计比例 $0.932$ 不变，只是它在两个因子之间的分配由 $(0.571,0.361)$ 变为 $(0.507,0.425)$。

![消费者偏好数据的方差最大旋转：五个变量按其在两个因子上的载荷画出，左图为未旋转的因子轴，右图为方差最大旋转后的轴，它们贴近两簇变量](./plots/varimax-rotation.py)

### 8.3.3. 其他旋转

正交旋转保持因子不相关（在正态性下即独立）。方差最大旋转对每个因子最大化其平方载荷在各变量间的方差，目标是使因子易于解释；四次方最大（quartimax）旋转对每个变量最大化其平方载荷在各因子间的方差，目标是使变量易于解释，往往产生一个一般因子。

斜交旋转允许因子相关；直观上，因子轴之间的夹角不必是直角。例子有 oblimin（最小化不同因子平方载荷之间的协方差）、promax（从正交的方差最大解出发，使小载荷更接近零）以及目标旋转（逼近事先选定的"简单结构"）。斜交解用两个矩阵报告：模式矩阵（pattern matrix）给出通常的载荷，用于解释因子；结构矩阵（structure matrix）给出变量与因子之间的相关。对正交因子两者相同。

用哪一种？选择通常并不关键。正交（方差最大）旋转后的解释很简单，因为因子不相关，标准化变量的载荷就是相关系数。斜交（promax）的构型看起来可能更简单，但因子之间的相关可能难以与解释相协调。

## 8.4. 因子得分

### 8.4.1. 目的与设定

因子得分，即每个个体 $j$ 的公共因子估计值 $\hat{\boldsymbol{f}}_j$，可用于诊断（离群点、检查假定）、作为后续分析的输入（例如用少数因子代替许多变量做回归），或本身作为指标（能力或某种人格特质的度量）。

估计因子得分不是通常意义下的估计：每个个体有 $m+p$ 个未观测量 $(\boldsymbol{f},\boldsymbol{\varepsilon})$，却只有 $p$ 个观测。通常的启发式做法是把 $L$、$\Psi$ 与 $\boldsymbol{\mu}$ 视为已知（用估计值代替），对观测为 $\boldsymbol{x}$ 的单个个体估计其因子向量。对 $\boldsymbol{F}$ 的两种看法导致两种方法。

- 估计总体参数 $L$、$\Psi$ 时，要寻找的是许多个体共有的规律，每个个体的因子随抽样而变，所以 $\boldsymbol{F}$ 是随机的。
- 对一个固定的个体（某一名学生），其因子（能力）是固定而未知的常数，要由该个体观测到的 $\boldsymbol{x}$ 来估计，而 $\boldsymbol{x}$ 已不再随机。这种看法导致加权最小二乘法；保持 $\boldsymbol{F}$ 为随机的并由 $\boldsymbol{X}$ 预测它，则导致回归法。

### 8.4.2. 加权最小二乘法

对固定的个体，模型 $\boldsymbol{x}-\boldsymbol{\mu}=L\boldsymbol{f}+\boldsymbol{\varepsilon}$ 是一个线性回归，"设计矩阵"为 $L$，"系数"为 $\boldsymbol{f}$，有 $p$ 个"观测"。普通最小二乘（[3.4.7](/3.4.7)）最小化 $\sum_{i=1}^p\varepsilon_i^2=(\boldsymbol{x}-\boldsymbol{\mu}-L\boldsymbol{f})^{\mathsf T}(\boldsymbol{x}-\boldsymbol{\mu}-L\boldsymbol{f})$，得 $\hat{\boldsymbol{f}}=(L^{\mathsf T}L)^{-1}L^{\mathsf T}(\boldsymbol{x}-\boldsymbol{\mu})$。但误差的方差 $\operatorname{Var}(\varepsilon_i)=\psi_i$ 各不相同，Gauss–Markov 条件不成立。用 $\Psi^{-1/2}$ 重新标度，

$$
\Psi^{-1/2}(\boldsymbol{x}-\boldsymbol{\mu})=\Psi^{-1/2}L\boldsymbol{f}+\Psi^{-1/2}\boldsymbol{\varepsilon},\qquad\operatorname{Cov}(\Psi^{-1/2}\boldsymbol{\varepsilon})=\Psi^{-1/2}\Psi\Psi^{-1/2}=I_p,
$$
条件就恢复了；对重新标度后的模型做 OLS，就是最小化 $\sum_{i=1}^p\varepsilon_i^2/\psi_i=(\boldsymbol{x}-\boldsymbol{\mu}-L\boldsymbol{f})^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu}-L\boldsymbol{f})$。

**定义 8.4.1（Bartlett 因子得分）** 观测为 $\boldsymbol{x}_j$ 的个体的**加权最小二乘因子得分**（**Bartlett 因子得分**，M. S. Bartlett，1937）为

$$
\hat{\boldsymbol{f}}_j=(\hat L^{\mathsf T}\hat\Psi^{-1}\hat L)^{-1}\hat L^{\mathsf T}\hat\Psi^{-1}(\boldsymbol{x}_j-\bar{\boldsymbol{x}}),
$$
它由 $\boldsymbol{f}=(L^{\mathsf T}\Psi^{-1}L)^{-1}L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ 把 $\hat L$、$\hat\Psi$ 与 $\hat{\boldsymbol{\mu}}=\bar{\boldsymbol{x}}$ 当作真值代入得到。

用极大似然估计时，$\hat L^{\mathsf T}\hat\Psi^{-1}\hat L=\hat\Delta$ 是对角矩阵，求逆很简单。若 $L$、$\Psi$ 是标准化变量的参数 $L_z=V^{-1/2}L$、$\Psi_z=V^{-1/2}\Psi V^{-1/2}$，则 $L_z^{\mathsf T}\Psi_z^{-1}L_z=L^{\mathsf T}\Psi^{-1}L$，$L_z^{\mathsf T}\Psi_z^{-1}\boldsymbol{z}=L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$，于是

$$
\hat{\boldsymbol{f}}_z=(L_z^{\mathsf T}\Psi_z^{-1}L_z)^{-1}L_z^{\mathsf T}\Psi_z^{-1}\boldsymbol{z}=\hat{\boldsymbol{f}}:
$$
Bartlett 得分与分析用的是 $S$ 还是 $R$ 无关，这与模型的尺度不变性一致——前提是 $L$ 与 $\Psi$ 的估计相应地变换（极大似然估计正是如此）。

若用主成分法估计 $L$ 与 $\Psi$，通常用 OLS，因为特殊方差并未建模。对 $\tilde L=[\sqrt{\hat\lambda_1}\hat{\boldsymbol{e}}_1,\dots,\sqrt{\hat\lambda_m}\hat{\boldsymbol{e}}_m]$，$\tilde L^{\mathsf T}\tilde L=\operatorname{diag}(\hat\lambda_1,\dots,\hat\lambda_m)$ 是对角矩阵，$\tilde L^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}})$ 的分量为 $\sqrt{\hat\lambda_j}\,\hat{\boldsymbol{e}}_j^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}})$，所以

$$
\hat f_j=\frac{1}{\sqrt{\hat\lambda_j}}\,\hat{\boldsymbol{e}}_j^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}})=\frac{\hat y_j}{\sqrt{\hat\lambda_j}},\qquad j=1,\dots,m,
$$
其中 $\hat y_j$ 是 [3.4.5](/3.4.5) 的第 $j$ 个主成分得分：因子得分就是标准化的主成分得分。从几何上看，用主成分法时，公共因子张成的空间正是 PCA 降维所得的子空间（$m=2$ 时是同一个平面）。因子是该子空间中方差为 1 的坐标，$F_j=Y_j/\sqrt{\lambda_j}$，$Y_j=\boldsymbol{e}_j^{\mathsf T}(\boldsymbol{X}-\boldsymbol{\mu})$，于是 $L\boldsymbol{F}=\sum_{j\le m}\boldsymbol{e}_jY_j$；而特殊因子 $\boldsymbol{\varepsilon}=\sum_{j>m}\boldsymbol{e}_jY_j$ 由其余的主成分构成。

### 8.4.3. 回归法

现在把 $\boldsymbol{F}$ 视为随机的。在正态因子模型下，

$$
\begin{bmatrix}\boldsymbol{X}-\boldsymbol{\mu}\\\boldsymbol{F}\end{bmatrix}=\begin{bmatrix}L\\I_m\end{bmatrix}\boldsymbol{F}+\begin{bmatrix}\boldsymbol{\varepsilon}\\\boldsymbol{0}\end{bmatrix}\sim\mathcal{N}_{p+m}\left(\boldsymbol{0},\begin{bmatrix}LL^{\mathsf T}+\Psi&L\\L^{\mathsf T}&I_m\end{bmatrix}\right).
$$
由多元正态向量的**条件分布**公式（[3.4.2](/3.4.2)），$\boldsymbol{F}\mid\boldsymbol{X}=\boldsymbol{x}$ 服从正态分布，

$$
\mathbb{E}(\boldsymbol{F}\mid\boldsymbol{x})=L^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu})=L^{\mathsf T}(LL^{\mathsf T}+\Psi)^{-1}(\boldsymbol{x}-\boldsymbol{\mu}),\qquad\operatorname{Cov}(\boldsymbol{F}\mid\boldsymbol{x})=I_m-L^{\mathsf T}(LL^{\mathsf T}+\Psi)^{-1}L.
$$

**定义 8.4.2（回归因子得分）** 观测为 $\boldsymbol{x}_j$ 的个体的**回归因子得分**（**Thomson 因子得分**，G. H. Thomson，1951）为

$$
\hat{\boldsymbol{f}}_j=\hat L^{\mathsf T}\hat\Sigma^{-1}(\boldsymbol{x}_j-\bar{\boldsymbol{x}})=\hat L^{\mathsf T}(\hat L\hat L^{\mathsf T}+\hat\Psi)^{-1}(\boldsymbol{x}_j-\bar{\boldsymbol{x}}).
$$

这个名称来自不需要正态性的第二种推导。把因子对观测作回归，$\boldsymbol{F}=B(\boldsymbol{X}-\boldsymbol{\mu})+\boldsymbol{\eta}$，$\mathbb{E}\boldsymbol{\eta}=\boldsymbol{0}$，$\operatorname{Cov}(\boldsymbol{X}-\boldsymbol{\mu},\boldsymbol{\eta})=O$，即取由 $\boldsymbol{X}$ 预测 $\boldsymbol{F}$ 的**最佳线性预测**。由于 $\boldsymbol{F}$ 不可观测，无法直接拟合 $B$，但载荷是已知的协方差：

$$
l_{ij}=\operatorname{Cov}(X_i-\mu_i,F_j)=b_{j1}\sigma_{i1}+\cdots+b_{jp}\sigma_{ip},\qquad\text{即}\qquad L=\Sigma B^{\mathsf T},
$$
所以 $B^{\mathsf T}=\Sigma^{-1}L$，$\hat{\boldsymbol{F}}=L^{\mathsf T}\Sigma^{-1}(\boldsymbol{X}-\boldsymbol{\mu})$。

实际中常用 $S$ 代替 $\hat L\hat L^{\mathsf T}+\hat\Psi$，这样在因子个数选错时得分更稳定：$\hat{\boldsymbol{f}}_j=\hat L^{\mathsf T}S^{-1}(\boldsymbol{x}_j-\bar{\boldsymbol{x}})$，对标准化数据为 $\hat{\boldsymbol{f}}_j=\hat L_z^{\mathsf T}R^{-1}\boldsymbol{z}_j$。用主成分载荷时，这一近似同样给出标准化的主成分得分：记 $S=P\Lambda P^{\mathsf T}$，$\tilde L=P_m\Lambda_m^{1/2}$（$P$ 的前 $m$ 列与前 $m$ 个特征值），

$$
\hat{\boldsymbol{f}}=\tilde L^{\mathsf T}S^{-1}(\boldsymbol{x}-\bar{\boldsymbol{x}})=\Lambda_m^{1/2}P_m^{\mathsf T}P\Lambda^{-1}P^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}})=\Lambda_m^{-1/2}P_m^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}}).
$$

### 8.4.4. 两种方法的比较

记 $\Delta=L^{\mathsf T}\Psi^{-1}L$，$\hat{\boldsymbol{f}}_{\mathrm{WLS}}=\Delta^{-1}L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$，$\hat{\boldsymbol{f}}_{\mathrm{R}}=L^{\mathsf T}(LL^{\mathsf T}+\Psi)^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$。关键的代数工具是

$$
L^{\mathsf T}(LL^{\mathsf T}+\Psi)^{-1}=(I_m+L^{\mathsf T}\Psi^{-1}L)^{-1}L^{\mathsf T}\Psi^{-1},
$$
它可由 **Woodbury 公式**得到，也可直接由 $(I_m+L^{\mathsf T}\Psi^{-1}L)L^{\mathsf T}=L^{\mathsf T}\Psi^{-1}(LL^{\mathsf T}+\Psi)$ 验证。

**命题 8.4.1** 两种得分满足

$$
\hat{\boldsymbol{f}}_{\mathrm{R}}=(I_m+\Delta)^{-1}\Delta\,\hat{\boldsymbol{f}}_{\mathrm{WLS}},\qquad\hat{\boldsymbol{f}}_{\mathrm{WLS}}=(I_m+\Delta^{-1})\,\hat{\boldsymbol{f}}_{\mathrm{R}}.
$$
并且：

1. （无偏性）$\mathbb{E}(\hat{\boldsymbol{f}}_{\mathrm{WLS}}\mid\boldsymbol{F})=\boldsymbol{F}$，而 $\mathbb{E}(\hat{\boldsymbol{f}}_{\mathrm{R}}\mid\boldsymbol{F})=(I_m+\Delta^{-1})^{-1}\boldsymbol{F}$，所以回归得分向 $\boldsymbol{0}$ 有偏。
2. （均方误差）$\mathbb{E}(\hat{\boldsymbol{f}}_{\mathrm{WLS}}-\boldsymbol{F})(\hat{\boldsymbol{f}}_{\mathrm{WLS}}-\boldsymbol{F})^{\mathsf T}=\Delta^{-1}$，$\mathbb{E}(\hat{\boldsymbol{f}}_{\mathrm{R}}-\boldsymbol{F})(\hat{\boldsymbol{f}}_{\mathrm{R}}-\boldsymbol{F})^{\mathsf T}=(I_m+\Delta)^{-1}$，后者更小。
3. （旋转）若 $L^*=LT$，$T$ 正交，则两种得分都与因子一样变换：$\hat{\boldsymbol{f}}^*=T^{\mathsf T}\hat{\boldsymbol{f}}$。

**证明** 由 $L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})=\Delta\hat{\boldsymbol{f}}_{\mathrm{WLS}}$ 与上述恒等式即得两者的关系。代入 $\boldsymbol{x}-\boldsymbol{\mu}=L\boldsymbol{F}+\boldsymbol{\varepsilon}$，

$$
\hat{\boldsymbol{f}}_{\mathrm{WLS}}=\boldsymbol{F}+\Delta^{-1}L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon},\qquad\hat{\boldsymbol{f}}_{\mathrm{R}}=(I_m+\Delta)^{-1}\Delta\boldsymbol{F}+(I_m+\Delta)^{-1}L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon}.
$$
取条件期望，并注意 $(I_m+\Delta)^{-1}\Delta=(I_m+\Delta^{-1})^{-1}$，即得 1。对 2，$\operatorname{Cov}(L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon})=L^{\mathsf T}\Psi^{-1}\Psi\Psi^{-1}L=\Delta$，所以 WLS 误差的协方差为 $\Delta^{-1}\Delta\Delta^{-1}=\Delta^{-1}$。回归误差为 $\hat{\boldsymbol{f}}_{\mathrm{R}}-\boldsymbol{F}=-(I_m+\Delta)^{-1}\boldsymbol{F}+(I_m+\Delta)^{-1}L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon}$，其中 $\boldsymbol{F}$ 与 $\boldsymbol{\varepsilon}$ 不相关且 $\operatorname{Cov}(\boldsymbol{F})=I_m$，故其二阶矩为 $(I_m+\Delta)^{-1}(I_m+\Delta)(I_m+\Delta)^{-1}=(I_m+\Delta)^{-1}$；又因特征值满足 $1/\delta\ge1/(1+\delta)$，$\Delta^{-1}\succeq(I_m+\Delta)^{-1}$。对 3，$(T^{\mathsf T}\Delta T)^{-1}T^{\mathsf T}L^{\mathsf T}\Psi^{-1}=T^{\mathsf T}\Delta^{-1}L^{\mathsf T}\Psi^{-1}$，$T^{\mathsf T}L^{\mathsf T}(LTT^{\mathsf T}L^{\mathsf T}+\Psi)^{-1}=T^{\mathsf T}L^{\mathsf T}\Sigma^{-1}$。$\square$

当 $\Delta$ 为对角矩阵时（极大似然的约束），这一关系按分量成立，$\hat f_{\mathrm{R},j}=\frac{\delta_j}{1+\delta_j}\hat f_{\mathrm{WLS},j}$：回归得分是把 Bartlett 得分向 $0$ 收缩的结果，$\delta_j$ 小（即数据对该因子确定得不好）的因子收缩得最厉害。这是一种**偏差–方差权衡**：Bartlett 得分无偏而均方误差较大，回归得分有偏而均方误差较小。

![模拟的两因子模型：Bartlett（加权最小二乘）得分散布在 45 度线周围，回归得分向零收缩但均方误差更小](./plots/factor-score-shrinkage.py)

这一比较可以自然地解释为对重新标度的模型 $\Psi^{-1/2}(\boldsymbol{x}-\boldsymbol{\mu})=\Psi^{-1/2}L\boldsymbol{f}+\Psi^{-1/2}\boldsymbol{\varepsilon}$ 做岭回归（[3.4.7](/3.4.7)）。

**命题 8.4.2** 对 $\lambda\ge0$，令 $\hat{\boldsymbol{f}}(\lambda)=(\Delta+\lambda I_m)^{-1}L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$，即重新标度的模型中 $\boldsymbol{f}$ 的岭估计，于是 $\hat{\boldsymbol{f}}(0)=\hat{\boldsymbol{f}}_{\mathrm{WLS}}$，$\hat{\boldsymbol{f}}(1)=\hat{\boldsymbol{f}}_{\mathrm{R}}$。则

$$
\mathbb{E}\big(\hat{\boldsymbol{f}}(\lambda)-\boldsymbol{F}\big)\big(\hat{\boldsymbol{f}}(\lambda)-\boldsymbol{F}\big)^{\mathsf T}=(\lambda I_m+\Delta)^{-1}+(\lambda^2-\lambda)(\lambda I_m+\Delta)^{-2},
$$
其迹在 $\lambda=1$ 处最小：回归得分就是取最优调节参数的岭估计。

**证明** 与上面一样，$\hat{\boldsymbol{f}}(\lambda)-\boldsymbol{F}=-\lambda(\Delta+\lambda I_m)^{-1}\boldsymbol{F}+(\Delta+\lambda I_m)^{-1}L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon}$，其二阶矩为 $(\Delta+\lambda I_m)^{-1}(\lambda^2I_m+\Delta)(\Delta+\lambda I_m)^{-1}$；把 $\lambda^2I_m+\Delta$ 写成 $(\Delta+\lambda I_m)+(\lambda^2-\lambda)I_m$ 即得公式。在 $\Delta$ 的特征基下迹为 $\sum_j(\delta_j+\lambda^2)/(\delta_j+\lambda)^2$，而 $\frac{\mathrm{d}}{\mathrm{d}\lambda}\frac{\delta+\lambda^2}{(\delta+\lambda)^2}=\frac{2\delta(\lambda-1)}{(\delta+\lambda)^3}$ 在 $\lambda<1$ 时为负、在 $\lambda>1$ 时为正。$\square$

旋转与因子得分是两个独立的步骤：旋转作用于总体水平的 $L$，因子得分则在选定的 $L$（旋转与否均可）下对每个个体计算；由命题 8.4.1，先旋转再计算得分，得到的就是旋转后的得分。用哪种方法估计 $L$ 与 $\Psi$ 是另一个选择，各有优势：

- 用主成分估计时，OLS 与（近似的）回归法给出相同的结果，即标准化主成分得分，计算方便；但数据是否标准化会改变结果。
- 用极大似然估计时，WLS 与回归法得分彼此不同，但都不受标准化的影响，与模型理论上的尺度不变性一致；计算则不那么方便。

要画因子得分图，先估计总体水平的 $L$ 与 $\Psi$，再计算每个个体的 $m$ 维得分；对 $n=100$ 名学生、$m=2$，得到 $100\times2$ 的得分矩阵，以其两列画散点图，就是第一因子对第二因子的得分图。

**例 8.4.1（股票价格，续）** 用方差最大旋转后的极大似然载荷（JPMorgan $0.763$，第二个载荷小于 $0.1$；Citibank $0.819$、$0.232$；Wells Fargo $0.668$、$0.108$；Shell $0.113$、$0.991$；ExxonMobil $0.108$、$0.677$，于是 $F_1^*$ 是银行因子，$F_2^*$ 是石油因子），第一周的 Bartlett 得分为 $(0.251,-1.854)$，而 OLS 给出 $(0.176,-1.305)$：在极大似然下，OLS 与 WLS 可能相差很大。用方差最大旋转后的主成分载荷，OLS（等于近似回归得分）给出 $(0.065,-1.016)$，WLS 给出 $(0.056,-1.045)$：在主成分法下两者差别很小。

## 8.5. 因子分析的实际应用

### 8.5.1. 一种策略

应用时有两条指导原则：可解释性（用 R. Johnson 与 D. Wichern 的话说："如果研究者在仔细审视因子分析的结果时能喊出'哇，我理解这些因子了'，这项应用就算成功"）以及结果在不同方法与子样本之间的一致性。主要步骤为：

1. 收集与整理数据；
2. 选择因子个数；
3. 提取初始因子；
4. 旋转得到最终解；
5. 模型诊断与改进；
6. 计算因子得分以供进一步分析。

更具体地说：对大数据集，把它分成两半，分别做分析；对给定的数据和固定的 $m$，(1) 做主成分因子分析，(2) 做极大似然因子分析，(3) 比较两个解，检查因子并在因子得分图中寻找离群点；对其他 $m$ 值重复；最后检查一致性与可解释性。

**例 8.5.1（鸡骨数据）** 对 $n=276$ 只鸡测量了六项骨骼尺寸：头骨长与头骨宽（头部）、股骨长与胫骨长（腿部）、肱骨长与尺骨长（翅膀）。取 $m=3$ 并做方差最大旋转，两种方法都得到一个在四项腿骨和翅骨上载荷很高的主导因子（主成分法为 $0.89$–$0.92$，极大似然法为 $0.83$–$0.94$）。其余因子则不同：主成分法给出一个头骨宽因子和一个头骨长因子，这两个变量的特殊方差接近零；极大似然法给出一个头部因子和一个较弱的翅膀因子；累计比例分别为 $0.950$ 与 $0.823$。前两个因子得分的散点图揭示了几只离群的鸡；两种方法所得得分相互对照的图表明，第一因子吻合得很好，第三因子却不然，因此第三因子并不是数据的稳定特征。

### 8.5.2. 推广

分类变量。因子分析依赖于相关矩阵：只要能得到可解释的相关矩阵，分析就能进行。对二分类或有序题目，Pearson 相关往往低估关联，此时改用假设存在潜在正态变量的四分相关（二分类）或多分相关（有序）。

探索性与验证性分析。本章的分析是探索性因子分析（exploratory factor analysis）：它概括数据、描述相关结构并产生假设。验证性因子分析（confirmatory factor analysis）则检验一个事先指定的、受到严格约束的结构：因子个数由分析者确定，哪些因子影响哪些观测变量是指定的（其余载荷设为零），还可以检验相关的测量误差，或单因子模型对多因子模型。它是结构方程模型的特例。

## 小结

- 模型：$\boldsymbol{X}-\boldsymbol{\mu}=L\boldsymbol{F}+\boldsymbol{\varepsilon}$，因子不相关且方差为 1，$\Psi$ 为对角矩阵；从而 $\Sigma=LL^{\mathsf T}+\Psi$，$\sigma_{ii}=h_i^2+\psi_i$，$\operatorname{Cov}(\boldsymbol{X},\boldsymbol{F})=L$。模型把 $p(p+1)/2$ 个参数约简为 $pm+p-m(m-1)/2$ 个，只在相差旋转 $L\mapsto LT$ 的意义下可识别，对变量的尺度变换不变；它可能失效（Heywood 情形）。
- 总体水平：主成分法（$\tilde L$ 来自 $S$ 或 $R$ 的特征对；显式、对 $m$ 嵌套，残差受被略去特征值平方和控制）与极大似然法（正态性，约束 $L^{\mathsf T}\Psi^{-1}L$ 为对角矩阵，对 $S$ 与 $R$ 等价，用自由度为 $\frac12[(p-m)^2-p-m]$ 的似然比检验选因子个数）。
- 旋转：只为解释；共同度、特殊方差与拟合都不变；方差最大旋转使每列缩放载荷的平方尽量分散。
- 个体水平：在给定的 $\hat L$、$\hat\Psi$ 下对每个个体计算因子得分（见下表）；用主成分载荷时，OLS 与近似回归法都给出标准化主成分得分 $\hat y_j/\sqrt{\hat\lambda_j}$。
- 因子分析与 PCA：PCA 用观测变量表示主成分，在相差符号的意义下唯一；因子分析用因子表示观测变量，只在相差旋转的意义下唯一；用主成分法时两者张成同一子空间。

| | 加权最小二乘（Bartlett） | 回归（Thomson） |
|---|---|---|
| 公式 | $(L^{\mathsf T}\Psi^{-1}L)^{-1}L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ | $L^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ |
| 对 $\boldsymbol{F}$ 的看法 | 固定参数 | 随机向量 |
| 无偏 | 是 | 否（向 $\boldsymbol{0}$ 收缩） |
| 均方误差 | $\Delta^{-1}$（较大） | $(I_m+\Delta)^{-1}$（较小） |
| 旋转 $L^*=LT$ 下 | $\hat{\boldsymbol{f}}^*=T^{\mathsf T}\hat{\boldsymbol{f}}$ | $\hat{\boldsymbol{f}}^*=T^{\mathsf T}\hat{\boldsymbol{f}}$ |
