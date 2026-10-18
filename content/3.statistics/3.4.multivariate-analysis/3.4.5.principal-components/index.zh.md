---
title: 主成分分析
description: 总体与样本主成分即协方差矩阵或相关矩阵的特征向量；方差贡献与主成分和变量的相关系数；标准化；正态假设下的主成分；主成分个数的选择、碎石图、解释与诊断；主成分分析作为最佳低秩逼近；特征值与特征向量的大样本推断。
source_hash: 99585f97f86c
---

当 $p$ 个变量高度相关时，数据只占据 $\mathbb{R}^p$ 中的少数几个方向，描述中有大量冗余。主成分分析用少数几个互不相关、保留了原变量大部分变异的线性组合代替原变量。在数学上它就是协方差矩阵的**谱分解**（[2.1.7](/2.1.7)）：主成分是数据在特征向量正交基下按特征值排序的坐标，而这种选择的最优性就是 **Rayleigh 商**的极值性质。本章建立总体理论及其样本版本，并讨论保留几个主成分、如何解释它们等实际问题。下一章（[3.4.6](/3.4.6)）通过**奇异值分解**计算主成分，并把它推广到距离数据（多维标度）和非线性结构（核主成分分析）；因子分析（[3.4.8](/3.4.8)）在同样的协方差结构上建立统计模型。

## 5.1. 动机与基本思想

`decathlon2` 数据记录了 $27$ 名运动员在两次十项全能比赛中十个项目的成绩。怎样理解十个相关特征的结构？画出其中两个，例如铅球对铁饼，可以看到很强的正相关：点散布在一条直线附近。极端情形下所有点恰好落在一条直线上，那么沿这条直线的一个坐标就能完全描述它们。一般地，我们寻找数据方差最大的方向；投影到这个方向上损失的信息最少。在更高维中，我们保留少数几个散布最大的方向，例如在 $\mathbb{R}^3$ 中最贴合一团弯曲点云的平面。

选取这些方向相当于换一个坐标系。几何上，主成分分析（principal component analysis）旋转原来的坐标轴；代数上，它构造 $p$ 个随机变量的线性组合

$$
Y_j = \boldsymbol{a}_j^{\mathsf T}\boldsymbol{X} = a_{j1}X_1 + \cdots + a_{jp}X_p,
$$

使 $n \times p$ 的**数据矩阵** $X$（行为 $\boldsymbol{x}_1^{\mathsf T}, \dots, \boldsymbol{x}_n^{\mathsf T}$，每行一个观测）旋转成新坐标矩阵 $(y_{jk})$，其后面几列只带有很少的变异。主成分分析（简称 PCA）通过少数几个线性组合解释一组变量的方差–协方差结构，两个一般目标是数据降维和解释。它由 Karl Pearson 于 1901 年提出，Harold Hotelling 在 20 世纪 30 年代独立地发展并命名；如今几乎在每个领域都是最常用的统计方法之一。

![一个相关的二元样本及其主轴：第一主方向 e_1 沿常数距离椭圆的长轴（左）；在旋转后的坐标 (y_1, y_2) 中得分互不相关，大部分散布沿 y_1（右）](./plots/pca-axes.py)

## 5.2. 总体主成分

### 5.2.1. 定义

设随机向量 $\boldsymbol{X} = (X_1, \dots, X_p)^{\mathsf T}$ 的**协方差矩阵**为 $\Sigma$，特征值 $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_p \ge 0$。第一个成分应是使 $\operatorname{Var}(Y_1) = \boldsymbol{a}_1^{\mathsf T}\Sigma\boldsymbol{a}_1$ 最大的线性组合 $Y_1 = \boldsymbol{a}_1^{\mathsf T}\boldsymbol{X}$。由于把 $\boldsymbol{a}_1$ 换成 $c\boldsymbol{a}_1$ 会使方差乘以 $c^2$，问题只对单位长度的系数向量有意义，或等价地考虑比值 $\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}/\boldsymbol{a}^{\mathsf T}\boldsymbol{a}$。

**定义 5.2.1（主成分）** $\boldsymbol{X}$ 的第一**主成分**是在 $\boldsymbol{a}_1^{\mathsf T}\boldsymbol{a}_1 = 1$ 下使 $\operatorname{Var}(\boldsymbol{a}_1^{\mathsf T}\boldsymbol{X})$ 最大的线性组合 $Y_1 = \boldsymbol{a}_1^{\mathsf T}\boldsymbol{X}$。对 $i = 2, \dots, p$，第 $i$ 主成分是在 $\boldsymbol{a}_i^{\mathsf T}\boldsymbol{a}_i = 1$ 且对所有 $k < i$ 有 $\operatorname{Cov}(\boldsymbol{a}_i^{\mathsf T}\boldsymbol{X}, \boldsymbol{a}_k^{\mathsf T}\boldsymbol{X}) = \boldsymbol{a}_k^{\mathsf T}\Sigma\boldsymbol{a}_i = 0$ 的条件下使 $\operatorname{Var}(\boldsymbol{a}_i^{\mathsf T}\boldsymbol{X})$ 最大的线性组合 $Y_i = \boldsymbol{a}_i^{\mathsf T}\boldsymbol{X}$。

求解要用到对称矩阵特征值的极值刻画，即 [2.1.7](/2.1.7) 的 Rayleigh 商。

**引理 5.2.1（单位球面上二次型的最大化）** 设 $\Sigma$ 是 $p \times p$ 对称矩阵，特征值 $\lambda_1 \ge \cdots \ge \lambda_p$，对应的标准正交特征向量为 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$。则

$$
\max_{\boldsymbol{a} \ne \boldsymbol{0}} \frac{\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \lambda_1 \ (\text{在 } \boldsymbol{a} = \boldsymbol{e}_1 \text{ 处取到}), \qquad \min_{\boldsymbol{a} \ne \boldsymbol{0}} \frac{\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \lambda_p \ (\text{在 } \boldsymbol{a} = \boldsymbol{e}_p \text{ 处取到}),
$$

且对 $k = 1, \dots, p-1$，

$$
\max_{\boldsymbol{a} \perp \boldsymbol{e}_1, \dots, \boldsymbol{e}_k,\ \boldsymbol{a} \ne \boldsymbol{0}} \frac{\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \lambda_{k+1} \ (\text{在 } \boldsymbol{a} = \boldsymbol{e}_{k+1} \text{ 处取到}).
$$

**证明** 写 $\Sigma = P\Lambda P^{\mathsf T}$，$P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_p]$ 为正交矩阵，$\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_p)$，令 $\boldsymbol{b} = P^{\mathsf T}\boldsymbol{a}$。则 $\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}/\boldsymbol{a}^{\mathsf T}\boldsymbol{a} = \sum_i\lambda_i b_i^2/\sum_i b_i^2$ 是特征值的加权平均，介于 $\lambda_p$ 与 $\lambda_1$ 之间。约束 $\boldsymbol{a} \perp \boldsymbol{e}_1, \dots, \boldsymbol{e}_k$ 即 $b_1 = \cdots = b_k = 0$，此时平均值至多为 $\lambda_{k+1}$。$\square$

### 5.2.2. 求主成分

**定理 5.2.1** 设 $\Sigma$ 是 $\boldsymbol{X} = (X_1, \dots, X_p)^{\mathsf T}$ 的协方差矩阵，其特征值–特征向量对为 $(\lambda_1, \boldsymbol{e}_1), \dots, (\lambda_p, \boldsymbol{e}_p)$，$\lambda_1 \ge \cdots \ge \lambda_p \ge 0$，特征向量标准正交。则第 $i$ 主成分为

$$
Y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{X} = e_{i1}X_1 + e_{i2}X_2 + \cdots + e_{ip}X_p, \qquad i = 1, \dots, p,
$$

且

$$
\operatorname{Var}(Y_i) = \boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{e}_i = \lambda_i, \qquad \operatorname{Cov}(Y_i, Y_k) = \boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{e}_k = 0 \quad (i \ne k).
$$

若有相等的特征值，则对应的系数向量以及主成分不唯一。

**证明** 由引理 5.2.1，$\boldsymbol{e}_1$ 在单位向量中使方差最大。对 $Y_i$，约束 $\operatorname{Cov}(\boldsymbol{e}_k^{\mathsf T}\boldsymbol{X}, \boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{e}_k^{\mathsf T}\Sigma\boldsymbol{a} = \lambda_k\boldsymbol{e}_k^{\mathsf T}\boldsymbol{a} = 0$ 在 $\lambda_k > 0$ 时就是 $\boldsymbol{a} \perp \boldsymbol{e}_k$，再由引理 5.2.1，最大值为 $\lambda_i$，在 $\boldsymbol{e}_i$ 处取到。最后，$i \ne k$ 时 $\operatorname{Cov}(\boldsymbol{e}_i^{\mathsf T}\boldsymbol{X}, \boldsymbol{e}_k^{\mathsf T}\boldsymbol{X}) = \boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{e}_k = \lambda_k\boldsymbol{e}_i^{\mathsf T}\boldsymbol{e}_k = 0$。$\square$

写成矩阵形式，记 $P = [\boldsymbol{e}_1, \dots, \boldsymbol{e}_p]$，$\boldsymbol{Y} = (Y_1, \dots, Y_p)^{\mathsf T}$，则

$$
\boldsymbol{Y} = P^{\mathsf T}\boldsymbol{X}, \qquad \boldsymbol{X} = P\boldsymbol{Y}, \qquad \operatorname{Cov}(\boldsymbol{Y}) = P^{\mathsf T}\Sigma P = \Lambda.
$$

特征向量构成新的坐标系，主成分是 $\boldsymbol{X}$ 在其中的坐标。

**例 5.2.1** 设

$$
\Sigma = \begin{bmatrix} 1 & -2 & 0 \\ -2 & 5 & 0 \\ 0 & 0 & 2 \end{bmatrix}.
$$

特征值–特征向量对为 $\lambda_1 = 5.83$，$\boldsymbol{e}_1 = (0.383, -0.924, 0)^{\mathsf T}$；$\lambda_2 = 2.00$，$\boldsymbol{e}_2 = (0, 0, 1)^{\mathsf T}$；$\lambda_3 = 0.17$，$\boldsymbol{e}_3 = (0.924, 0.383, 0)^{\mathsf T}$。于是 $\Sigma = P\Lambda P^{\mathsf T}$，$P = [\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}_3]$，主成分为

$$
Y_1 = 0.383X_1 - 0.924X_2, \qquad Y_2 = X_3, \qquad Y_3 = 0.924X_1 + 0.383X_2.
$$

与其他变量不相关的 $X_3$ 本身就是一个主成分。

### 5.2.3. 主成分的解释

**定理 5.2.2** 在定理 5.2.1 的条件下，

$$
\sigma_{11} + \sigma_{22} + \cdots + \sigma_{pp} = \sum_{i=1}^p\operatorname{Var}(X_i) = \lambda_1 + \lambda_2 + \cdots + \lambda_p = \sum_{i=1}^p\operatorname{Var}(Y_i).
$$

**证明** $\sum_i\sigma_{ii} = \operatorname{tr}(\Sigma) = \operatorname{tr}(P\Lambda P^{\mathsf T}) = \operatorname{tr}(\Lambda P^{\mathsf T}P) = \operatorname{tr}(\Lambda)$。$\square$

这个共同的值称为总体总方差（total population variance），旋转只是把它在各成分之间重新分配，并不改变它。因此

$$
\text{第 } k \text{ 主成分的方差贡献率} = \frac{\lambda_k}{\lambda_1 + \lambda_2 + \cdots + \lambda_p}.
$$

如果 $p$ 较大时前一、两、三个成分就解释了总方差的 $80\%$–$90\%$，它们就可以代替原来的 $p$ 个变量而几乎不损失信息。例 5.2.1 中总方差为 $1 + 5 + 2 = 8$，第一主成分解释 $5.83/8 = 73\%$，前两个主成分解释 $(5.83 + 2)/8 = 98\%$。

系数向量 $\boldsymbol{e}_i = (e_{i1}, \dots, e_{ip})^{\mathsf T}$ 描述成分的整体：$e_{ik}$ 衡量在其他变量存在的情况下第 $k$ 个变量对第 $i$ 个成分的重要性。单个变量本身的重要性则用相关系数衡量。

**定理 5.2.3** 若 $Y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{X}$ 是由 $\Sigma$ 得到的主成分，则主成分与变量之间的相关系数为

$$
\rho_{Y_i, X_k} = \frac{e_{ik}\sqrt{\lambda_i}}{\sqrt{\sigma_{kk}}}, \qquad i, k = 1, \dots, p,
$$

且对每个 $k$ 有 $\sum_{i=1}^p\rho_{Y_i, X_k}^2 = 1$。

**证明** 设 $\boldsymbol{c}_k$ 为第 $k$ 个坐标向量，则 $X_k = \boldsymbol{c}_k^{\mathsf T}\boldsymbol{X}$。于是 $\operatorname{Cov}(Y_i, X_k) = \boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{c}_k = \lambda_i\boldsymbol{e}_i^{\mathsf T}\boldsymbol{c}_k = \lambda_i e_{ik}$，除以 $\sqrt{\operatorname{Var}(Y_i)\operatorname{Var}(X_k)} = \sqrt{\lambda_i\sigma_{kk}}$ 即得公式。由于 $\Sigma = \sum_i\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$，取 $(k,k)$ 元得 $\sum_i\lambda_ie_{ik}^2 = \sigma_{kk}$，这就是第二个结论。$\square$

所以 $\rho_{Y_i, X_k}^2$ 是 $X_k$ 的方差中由它与 $Y_i$ 的相关所解释的比例。几何上，若把所有变量缩放到单位长度，$\rho_{Y_i, X_k}$ 就是 $X_k$ 与 $Y_i$ 轴夹角的余弦，$\sum_i\rho_{Y_i, X_k}^2 = 1$ 就是旋转后坐标中的勾股定理。

**例 5.2.2** 在例 5.2.1 中，

$$
\rho_{Y_1, X_1} = \frac{0.383\sqrt{5.83}}{\sqrt1} = 0.925, \qquad \rho_{Y_1, X_2} = \frac{-0.924\sqrt{5.83}}{\sqrt5} = -0.998.
$$

$Y_1$ 中 $X_2$ 的系数绝对值约为 $X_1$ 的 $2.4$ 倍，但两个变量与 $Y_1$ 的相关几乎同样强；系数与相关系数回答的是不同的问题。

### 5.2.4. 标准化变量的主成分

如果某个变量的量纲远大于其他变量，例如十项全能中以秒计的 1500 米成绩与 100 米成绩，或满分相差悬殊的作业、小测验和考试成绩，会发生什么？第一主成分将被方差最大的变量主导。

**例 5.2.3** 对

$$
\Sigma = \begin{bmatrix} 1 & 4 \\ 4 & 100 \end{bmatrix},
$$

特征值为 $100.16$ 和 $0.84$，$\boldsymbol{e}_1 = (0.040, 0.999)^{\mathsf T}$：解释了总方差 $99.2\%$ 的第一主成分几乎就是第二个变量本身，原因仅仅是它的方差大得多。

补救办法是标准化：令 $Z_k = (X_k - \mu_k)/\sqrt{\sigma_{kk}}$，$k = 1, \dots, p$，写成矩阵形式即

$$
\boldsymbol{Z} = (V^{1/2})^{-1}(\boldsymbol{X} - \boldsymbol{\mu}), \qquad V^{1/2} = \operatorname{diag}(\sqrt{\sigma_{11}}, \dots, \sqrt{\sigma_{pp}}).
$$

于是 $\operatorname{Cov}(\boldsymbol{Z}) = (V^{1/2})^{-1}\Sigma(V^{1/2})^{-1} = \rho$，即 $\boldsymbol{X}$ 的总体相关矩阵，其元素为 $\rho_{ik} = \sigma_{ik}/\sqrt{\sigma_{ii}\sigma_{kk}}$。

**定理 5.2.4** 标准化变量 $\boldsymbol{Z} = (Z_1, \dots, Z_p)^{\mathsf T}$（$\operatorname{Cov}(\boldsymbol{Z}) = \rho$）的第 $i$ 主成分为

$$
Y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{Z} = \boldsymbol{e}_i^{\mathsf T}(V^{1/2})^{-1}(\boldsymbol{X} - \boldsymbol{\mu}), \qquad i = 1, \dots, p,
$$

其中 $(\lambda_i, \boldsymbol{e}_i)$ 现在是 $\rho$ 的特征值–特征向量对。并且

$$
\sum_{i=1}^p\operatorname{Var}(Y_i) = \sum_{i=1}^p\operatorname{Var}(Z_i) = p, \qquad \rho_{Y_i, Z_k} = e_{ik}\sqrt{\lambda_i}, \quad i, k = 1, \dots, p.
$$

这是把定理 5.2.1–5.2.3 用于方差全为 $1$ 的 $\boldsymbol{Z}$；第 $k$ 主成分占标准化总方差的比例为 $\lambda_k/p$。由 $\Sigma$ 和由 $\rho$ 得到的主成分一般不同，也不是彼此的简单函数：标准化是一个实质性的选择，适用于变量量纲不可比的情形。

**例 5.2.4** 在例 5.2.3 中，相关矩阵为 $\rho = \begin{bmatrix} 1 & 0.4 \\ 0.4 & 1 \end{bmatrix}$，特征值为 $1.4$ 和 $0.6$，$\boldsymbol{e}_1 = (0.707, 0.707)^{\mathsf T}$，$\boldsymbol{e}_2 = (-0.707, 0.707)^{\mathsf T}$。现在两个变量的方差都是 $1$，第一主成分对它们赋予相同的权重，解释了标准化总方差的 $1.4/2 = 70\%$。

### 5.2.5. 正态假设下的主成分

现在设 $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$，$\Sigma$ 正定。由此还有两个结论。

1. 主成分得分是独立的正态变量：$\boldsymbol{Y} = P^{\mathsf T}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \mathcal{N}_p(\boldsymbol{0}, \Lambda)$，所以 $Y_1, \dots, Y_p$ 相互独立，$Y_i \sim \mathcal{N}(0, \lambda_i)$。
2. $\boldsymbol{X}$ 的密度在椭球 $(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) = c^2$ 上为常数。由于 $\Sigma^{-1} = \sum_i\lambda_i^{-1}\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$，在坐标 $y_i = \boldsymbol{e}_i^{\mathsf T}(\boldsymbol{x} - \boldsymbol{\mu})$ 下椭球为

   $$
   \frac{y_1^2}{\lambda_1} + \frac{y_2^2}{\lambda_2} + \cdots + \frac{y_p^2}{\lambda_p} = c^2,
   $$

   其轴沿 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_p$，半轴长为 $c\sqrt{\lambda_1}, \dots, c\sqrt{\lambda_p}$。主成分就是等密度椭球的轴，第一主成分是最长的轴。

## 5.3. 样本主成分

### 5.3.1. 定义与性质

设 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ 是来自均值为 $\boldsymbol{\mu}$、协方差矩阵为 $\Sigma$ 的 $p$ 维总体的 $n$ 个独立观测，样本均值为 $\bar{\boldsymbol{x}}$，**样本协方差矩阵**为 $S$，**样本相关矩阵**为 $R$（[3.4.2](/3.4.2)）。我们寻找能解释样本中大部分变异且彼此不相关的测量变量的线性组合。做法是用经验分布代替总体分布：把 $\Sigma$ 换成 $S$，$\rho$ 换成 $R$，然后照前面的步骤进行。

**定义 5.3.1（样本主成分）** 设 $S$ 的特征值–特征向量对为 $(\hat\lambda_1, \hat{\boldsymbol{e}}_1), \dots, (\hat\lambda_p, \hat{\boldsymbol{e}}_p)$，$\hat\lambda_1 \ge \cdots \ge \hat\lambda_p \ge 0$，$\hat{\boldsymbol{e}}_i$ 标准正交。第 $i$ 个**样本主成分**为

$$
\hat y_i = \hat{\boldsymbol{e}}_i^{\mathsf T}\boldsymbol{x} = \hat e_{i1}x_1 + \hat e_{i2}x_2 + \cdots + \hat e_{ip}x_p, \qquad i = 1, \dots, p,
$$

它在第 $j$ 个观测处的值 $\hat y_{ji} = \hat{\boldsymbol{e}}_i^{\mathsf T}\boldsymbol{x}_j$ 称为该观测的第 $i$ 主成分得分。通常先把观测中心化，$\hat y_{ji} = \hat{\boldsymbol{e}}_i^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})$，这只改变得分的位置。

**定理 5.3.1** 样本主成分满足

| 量 | 值 |
|---|---|
| $\hat y_k$ 的样本方差 | $\hat\lambda_k$，$k = 1, \dots, p$ |
| $\hat y_i, \hat y_k$ 的样本协方差 | $0$，$i \ne k$ |
| 样本总方差 | $\sum_{i=1}^p s_{ii} = \hat\lambda_1 + \hat\lambda_2 + \cdots + \hat\lambda_p$ |
| $\hat y_i$ 与 $x_k$ 的样本相关系数 | $r_{\hat y_i, x_k} = \dfrac{\hat e_{ik}\sqrt{\hat\lambda_i}}{\sqrt{s_{kk}}}$ |

**证明** 对第一行，

$$
\frac{1}{n-1}\sum_{j=1}^n(\hat y_{jk} - \bar{\hat y}_k)^2 = \frac{1}{n-1}\sum_{j=1}^n\big[\hat{\boldsymbol{e}}_k^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}})\big]^2 = \hat{\boldsymbol{e}}_k^{\mathsf T}\Big[\frac{1}{n-1}\sum_{j=1}^n(\boldsymbol{x}_j - \bar{\boldsymbol{x}})(\boldsymbol{x}_j - \bar{\boldsymbol{x}})^{\mathsf T}\Big]\hat{\boldsymbol{e}}_k = \hat{\boldsymbol{e}}_k^{\mathsf T}S\hat{\boldsymbol{e}}_k = \hat\lambda_k.
$$

其余各行把总体情形证明中的 $\Sigma$ 换成 $S$ 即得。$\square$

这些是样本方差和样本相关系数，是观测数据的描述统计量；它们估计总体量 $\lambda_k$ 和 $\rho_{Y_i, X_k}$，但并不就是它们。

用数据矩阵来写，可以看清正交矩阵是左乘还是右乘。对一个观测，得分为 $\hat{\boldsymbol{y}}_j = \hat P^{\mathsf T}\boldsymbol{x}_j$，是 $p \times 1$ 向量，其中 $\hat P = [\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_p]$。数据矩阵 $X$ 把观测按行 $\boldsymbol{x}_j^{\mathsf T}$ 排列，所以得分矩阵为

$$
Y = X\hat P \quad (n \times p), \qquad Y \text{ 的第 } j \text{ 行} = \hat{\boldsymbol{y}}_j^{\mathsf T} = \boldsymbol{x}_j^{\mathsf T}\hat P.
$$

样本主成分是坐标，特征向量构成坐标系。

### 5.3.2. 样本相关矩阵的主成分

若把观测标准化，$z_{jk} = (x_{jk} - \bar x_k)/\sqrt{s_{kk}}$，则 $\boldsymbol{z}_1, \dots, \boldsymbol{z}_n$ 的样本协方差矩阵就是 $R$。此时 $(\hat\lambda_i, \hat{\boldsymbol{e}}_i)$ 为 $R$ 的特征对，第 $i$ 个样本主成分为

$$
\hat y_i = \hat{\boldsymbol{e}}_i^{\mathsf T}\boldsymbol{z} = \hat e_{i1}z_1 + \hat e_{i2}z_2 + \cdots + \hat e_{ip}z_p, \qquad i = 1, \dots, p.
$$

它的样本方差为 $\hat\lambda_i$，两个不同成分的样本协方差为 $0$，标准化样本总方差为 $\operatorname{tr}(R) = p = \hat\lambda_1 + \cdots + \hat\lambda_p$，且 $r_{\hat y_i, z_k} = \hat e_{ik}\sqrt{\hat\lambda_i}$。

### 5.3.3. 几何解释

对二元样本，以 $\bar{\boldsymbol{x}}$ 为中心的等 **Mahalanobis 距离**椭圆 $(\boldsymbol{x} - \bar{\boldsymbol{x}})^{\mathsf T}S^{-1}(\boldsymbol{x} - \bar{\boldsymbol{x}}) = c^2$ 的轴沿 $\hat{\boldsymbol{e}}_1$ 和 $\hat{\boldsymbol{e}}_2$；样本主成分就是沿这些轴的坐标。当 $\hat\lambda_1 > \hat\lambda_2$ 时椭圆狭长，主方向确定。当 $\hat\lambda_1 \approx \hat\lambda_2$ 时椭圆近似为圆，各方向的散布差不多，数据并不能确定主方向：这时主成分分析无法降维，算出的方向基本是任意的。

### 5.3.4. 降维与重构

保留 $k < p$ 个成分，就是保留 $Y = \tilde X\hat P$ 的前 $k$ 列（$\tilde X$ 为中心化的数据矩阵），其余置零：

$$
Y = [\hat{\boldsymbol{y}}_{(1)}, \dots, \hat{\boldsymbol{y}}_{(k)}, \hat{\boldsymbol{y}}_{(k+1)}, \dots, \hat{\boldsymbol{y}}_{(p)}] \ \longrightarrow\ \tilde Y = [\hat{\boldsymbol{y}}_{(1)}, \dots, \hat{\boldsymbol{y}}_{(k)}, \boldsymbol{0}, \dots, \boldsymbol{0}],
$$

其中 $\hat{\boldsymbol{y}}_{(i)}$ 是第 $i$ 个成分的得分列。旋转回去得到 $\tilde X$ 的近似 $\hat X = \tilde Y\hat P^{\mathsf T}$，仍是 $n \times p$ 的：每个观测被替换为它在 $\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_k$ 张成的子空间上的投影（再加回均值 $\bar{\boldsymbol{x}}$ 即可）。对平面上坐标为 $(2, 1)$、得分为 $(2.5, 0.3)$ 的一个点，保留一个成分就把得分换成 $(2.5, 0)$，旋转回去得到该点到第一轴的垂足。

为什么这样能节省存储？由于 $\tilde Y$ 的后 $p - k$ 列为零，只需存储它的前 $k$ 列（$nk$ 个数）和 $\hat P$ 的前 $k$ 列（$kp$ 个数），而不是 $X$ 的 $np$ 个元素。对一幅 $1440 \times 1080$ 的图像（把一个颜色通道看作 $p = 1080$ 个变量的 $n = 1440$ 个观测），取 $k = 100$，比例为

$$
\frac{nk + kp}{np} = \frac{1440 \cdot 100 + 100 \cdot 1080}{1440 \cdot 1080} \approx 16\%.
$$

对一张照片，每个颜色通道的第一主成分就解释了 $85\%$ 以上的方差，$20$ 个成分解释 $95\%$ 以上；$5$ 或 $10$ 个成分得到模糊、块状的图像，而 $100$ 或 $200$ 个成分在视觉上已接近原图。

![一幅 120 x 160 的合成灰度图像由前 k 个主成分（k = 1, 5, 20）重构的结果与原图的比较，以及累计方差贡献率](./plots/image-reconstruction.py)

## 5.4. 实际问题

### 5.4.1. 保留几个主成分

没有确定的规则，常用的辅助手段有：

- 碎石图（scree plot），即 $\hat\lambda_i$ 对 $i$ 的图（也称肘部图）：寻找拐点，其后剩下的特征值都较小且大致相等，保留拐点之前的成分；
- 样本总方差的累计贡献率 $(\hat\lambda_1 + \cdots + \hat\lambda_k)/(\hat\lambda_1 + \cdots + \hat\lambda_p)$，与 $80\%$ 或 $90\%$ 之类的目标比较；
- 对基于相关矩阵 $R$ 的主成分分析，以 $1$ 为界（Kaiser 准则）：保留 $\hat\lambda_i > 1$ 的成分，即解释的方差多于单个标准化变量的成分。

保留的成分是否可解释、分析的目的是什么，与这些规则同样重要。

![一个模拟样本（n = 200，p = 8，由两个潜在因子生成）的样本相关矩阵特征值碎石图（左）和累计方差贡献率（右）：第二个特征值之后的拐点提示保留两个成分](./plots/scree-plot.py)

**例 5.4.1** Jolicoeur 与 Mosimann 测量了 $24$ 只雌性和 $24$ 只雄性锦龟背甲（龟壳）的长、宽、高。雄龟的数据右偏，所以先取对数。对对数测量值的协方差矩阵做主成分分析（R 中的 `prcomp`，它以 `sdev` 返回特征值的平方根），各成分的标准差为 $0.1527, 0.0245, 0.0190$，所以第一主成分解释了总方差的 $96.05\%$，显然一个成分就几乎刻画了全部变异。它的系数向量为 $(0.683, 0.510, 0.523)^{\mathsf T}$，所以非常粗略地有

$$
\hat y_1 \approx 0.5\big[\log(\text{长}) + \log(\text{宽}) + \log(\text{高})\big] = 0.5\log(\text{体积}),
$$

第一主成分衡量的是龟壳体积的对数，即它的整体大小。

### 5.4.2. 软件

R 中 `princomp()` 使用协方差（或相关）矩阵的谱分解，`prcomp()` 使用中心化数据矩阵的奇异值分解（[3.4.6](/3.4.6)）。简化的调用形式为 `prcomp(x, scale = FALSE)` 与 `princomp(x, cor = FALSE, scores = TRUE)`；`scale = TRUE` 或 `cor = TRUE` 先将变量标准化，即分析相关矩阵。输出与上文各量的对应关系如下。

| `prcomp()` | `princomp()` | 含义 |
|---|---|---|
| `sdev` | `sdev` | 各成分的标准差 $\sqrt{\hat\lambda_j}$ |
| `rotation` | `loadings` | 以特征向量 $\hat{\boldsymbol{e}}_j$ 为列的矩阵 |
| `center` | `center` | 被减去的变量均值 |
| `scale` | `scale` | 对每个变量所用的缩放 |
| `x` | `scores` | 得分向量 $\hat{\boldsymbol{y}}_{(j)} = (\hat y_{1j}, \dots, \hat y_{nj})^{\mathsf T}$ |

### 5.4.3. 检查正态性与发现离群值

主成分 $\hat y_1, \hat y_2, \dots, \hat y_k$ 的图有两种诊断用途。

- 前几个成分是方差大的线性组合；在多元正态下它们是正态的，所以它们的 QQ 图和两两散点图可以检查正态性假设（[3.4.4](/3.4.4)）。
- 最后几个成分的方差小；在这些成分上取值大的观测违背了其余数据所满足的近似线性关系，因此它们有助于发现在任何原变量上都不突出的可疑观测。

在锦龟数据中，$\hat y_1$ 对 $\hat y_2$ 的散点图和 $\hat y_2$ 的 QQ 图都单独标出了同一只龟，它在第二主成分上的得分远大于其他个体。

### 5.4.4. 主成分的解释

解释一个成分的实际意义（而不是它作为方差最大方向的理论意义）分三步。

1. 根据系数的大小决定保留哪些原变量来解释。对 $\hat y_1 = -0.7x_1 + 0.5x_2 - 0.1x_3$，保留 $x_1$ 和 $x_2$；取舍的界限（例如 $0.4$）有一定主观性。
2. 根据系数的符号决定该成分是保留变量的综合（符号相同）还是对比（符号相反）。
3. 结合变量的含义作最终解读。若 $x_1$ 是语文成绩、$x_2$ 是数学成绩，则 $\hat y_1 = -0.7x_1 + 0.5x_2 - 0.1x_3$ 表示数学与语文成绩的差异：接近 $0$ 表示不偏科，大于 $0$ 表示偏理科，小于 $0$ 表示偏文科。而成分 $0.7x_1 + 0.5x_2 - 0.1x_3$ 则衡量两科的综合学习能力。

## 5.5. 讨论

### 5.5.1. 主成分分析何时有用

主成分分析通常是数据分析的中间步骤，例如在回归或分类之前降维。有两种情形值得注意。

- 特征值 $\hat\lambda_i \approx 0$ 表明变量之间存在（近似的）线性相关，对应的 $\hat{\boldsymbol{e}}_i$ 描述了这种关系。
- 相等或近似相等的特征值使对应的成分不确定，如第 5.3.3 节所述；若所有特征值都接近，变量近乎不相关，主成分分析用处不大。

实践中主成分分析通过奇异值分解实现，见 [3.4.6](/3.4.6)。

### 5.5.2. 特殊结构的协方差矩阵

**例 5.5.1** 若 $\Sigma = \operatorname{diag}(\sigma_{11}, \sigma_{22}, \dots, \sigma_{pp})$，则 $(\sigma_{ii}, \boldsymbol{c}_i)$ 就是特征对，$\boldsymbol{c}_i$ 为第 $i$ 个坐标向量：变量本来就不相关，主成分就是变量本身（按方差排序），主成分分析得不到任何新东西。

**例 5.5.2** 对等相关矩阵

$$
\Sigma = \sigma^2\begin{bmatrix} 1 & \rho & \cdots & \rho \\ \rho & 1 & \cdots & \rho \\ \vdots & \vdots & \ddots & \vdots \\ \rho & \rho & \cdots & 1 \end{bmatrix} = \sigma^2\big[(1 - \rho)I_p + \rho\boldsymbol{1}\boldsymbol{1}^{\mathsf T}\big], \qquad \rho > 0,
$$

最大特征值为 $\lambda_1 = \sigma^2[1 + (p-1)\rho]$，$\boldsymbol{e}_1 = \frac{1}{\sqrt p}(1, 1, \dots, 1)^{\mathsf T}$；其余特征值为 $\lambda_2 = \cdots = \lambda_p = \sigma^2(1 - \rho)$，特征向量可取为

$$
\boldsymbol{e}_k = \frac{1}{\sqrt{(k-1)k}}\big(\underbrace{1, \dots, 1}_{k-1}, -(k-1), 0, \dots, 0\big)^{\mathsf T}, \qquad k = 2, \dots, p.
$$

事实上 $\Sigma\boldsymbol{1} = \sigma^2(1 - \rho + p\rho)\boldsymbol{1}$，而每个 $\boldsymbol{v} \perp \boldsymbol{1}$ 满足 $\Sigma\boldsymbol{v} = \sigma^2(1 - \rho)\boldsymbol{v}$。第一主成分正比于变量之和（或平均），解释总方差的比例为 $\lambda_1/(p\sigma^2) = \rho + (1 - \rho)/p$；其他成分不唯一。一组正相关的考试成绩因此有一个"综合能力"的第一主成分。

### 5.5.3. 局限

- 主成分分析只用到协方差矩阵（二阶矩），忽略了更高阶的结构。
- 它只能刻画线性结构；弯曲或成簇的数据可能需要非线性方法（[3.4.6](/3.4.6)）。
- 许多变量的线性组合可能难以解释。
- 它对离群值和变量的量纲敏感。

## 5.6. 主成分分析作为最佳低维逼近

第 5.2 节的推导逐个构造成分，每次使方差最大。一个等价的观点把 $r$ 维逼近作为整体来看。用前 $r$ 个主成分逼近数据，就是把数据投影到过 $\bar{\boldsymbol{x}}$、由 $\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_r$ 张成的 $r$ 维平面上；在所有 $r$ 维平面中，它使观测到平面的距离平方和 $\sum_{j=1}^n d_j^2$ 最小，在所有过 $\bar{\boldsymbol{x}}$ 的平面中，它使投影后观测的散布最大。

**定理 5.6.1** 设 $A = [\boldsymbol{a}_1, \dots, \boldsymbol{a}_n]^{\mathsf T}$ 是任意 $n \times p$ 矩阵，$\operatorname{rank}(A) \le r < \min(p, n)$，用来逼近均值校正后的数据矩阵 $[\boldsymbol{x}_1 - \bar{\boldsymbol{x}}, \dots, \boldsymbol{x}_n - \bar{\boldsymbol{x}}]^{\mathsf T}$，误差用 $np$ 个误差的平方和 $\sum_{j=1}^n(\boldsymbol{x}_j - \bar{\boldsymbol{x}} - \boldsymbol{a}_j)^{\mathsf T}(\boldsymbol{x}_j - \bar{\boldsymbol{x}} - \boldsymbol{a}_j)$ 衡量。令 $\hat E_r = [\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_r]$。则误差在 $\hat A = [\hat{\boldsymbol{y}}_{(1)}, \dots, \hat{\boldsymbol{y}}_{(r)}]\hat E_r^{\mathsf T}$ 处最小，即把每个中心化观测投影到 $\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_r$ 张成的子空间上，最小误差为

$$
(n-1)(\hat\lambda_{r+1} + \cdots + \hat\lambda_p).
$$

这就是中心化数据矩阵的 **Eckart–Young 定理**。总体版本说明了原因：对均值为 $\boldsymbol{\mu}$、协方差为 $\Sigma$ 的随机向量 $\boldsymbol{X}$，用某个 $r$ 维平面上的点 $C + U\boldsymbol{b}$ 逼近 $\boldsymbol{X}$，其中位置为 $C$，方向矩阵 $U = [\boldsymbol{u}_1, \dots, \boldsymbol{u}_r]$ 列标准正交，系数为 $\boldsymbol{b}$，使 $\mathbb{E}(\boldsymbol{X} - C - U\boldsymbol{b})^{\mathsf T}(\boldsymbol{X} - C - U\boldsymbol{b})$ 最小。按 $\boldsymbol{b}$、$C$、$U$ 的顺序优化：

1. 平面给定时，最近的点是正交投影，$\hat{\boldsymbol{b}} = U^{\mathsf T}(\boldsymbol{X} - C)$，残差为 $(I - UU^{\mathsf T})(\boldsymbol{X} - C)$；
2. 方向给定时，最佳位置是均值，$\hat C = \boldsymbol{\mu}$（均值是均方意义下离分布最近的点）；
3. 目标函数变为 $\mathbb{E}\|(I - UU^{\mathsf T})(\boldsymbol{X} - \boldsymbol{\mu})\|^2 = \operatorname{tr}\Sigma - \operatorname{tr}(U^{\mathsf T}\Sigma U)$，于是要使 $\operatorname{tr}(U^{\mathsf T}\Sigma U)$ 最大。

"散布最大"的提法给出同一个问题：

$$
\max_U\operatorname{tr}\operatorname{Cov}\big(UU^{\mathsf T}(\boldsymbol{X} - \boldsymbol{\mu})\big) = \max_U\operatorname{tr}(UU^{\mathsf T}\Sigma UU^{\mathsf T}) = \max_U\operatorname{tr}(U^{\mathsf T}\Sigma UU^{\mathsf T}U) = \max_U\operatorname{tr}(U^{\mathsf T}\Sigma U) = \sum_{i=1}^r\boldsymbol{e}_i^{\mathsf T}\Sigma\boldsymbol{e}_i = \sum_{i=1}^r\lambda_i,
$$

最大值在 $\hat{\boldsymbol{u}}_i = \boldsymbol{e}_i$ 处取到（Ky Fan 极大原理，即引理 5.2.1 的 $r$ 维推广）。因此，对每个 $r$，逐个构造与整体构造得到相同的成分。

## 5.7. 大样本推断

样本特征值和特征向量是随机的，它们的波动有多大？设 $\boldsymbol{X}_1, \dots, \boldsymbol{X}_n$ 是来自多元正态总体的随机样本，$\Sigma$ 的特征值互不相同且为正，$\lambda_1 > \lambda_2 > \cdots > \lambda_p > 0$。记 $\boldsymbol{\lambda} = (\lambda_1, \dots, \lambda_p)^{\mathsf T}$，$\hat{\boldsymbol{\lambda}}$ 为样本特征值组成的向量，$\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_p)$。$n$ 很大时有下面的结果（Anderson 与 Girshick）。

**定理 5.7.1** 在上述条件下：

1. $\sqrt{n}(\hat{\boldsymbol{\lambda}} - \boldsymbol{\lambda})$ 近似服从 $\mathcal{N}_p(\boldsymbol{0}, 2\Lambda^2)$；特别地，各 $\hat\lambda_i$ 近似独立，$\hat\lambda_i \overset{\cdot}{\sim} \mathcal{N}(\lambda_i, 2\lambda_i^2/n)$；
2. 令 $E_i = \lambda_i\sum_{k \ne i}\frac{\lambda_k}{(\lambda_k - \lambda_i)^2}\boldsymbol{e}_k\boldsymbol{e}_k^{\mathsf T}$，则 $\sqrt{n}(\hat{\boldsymbol{e}}_i - \boldsymbol{e}_i)$ 近似服从 $\mathcal{N}_p(\boldsymbol{0}, E_i)$；
3. 每个 $\hat\lambda_i$ 与对应的 $\hat{\boldsymbol{e}}_i$ 的元素近似独立。

由第 1 条，$\mathbb{P}(\lvert\hat\lambda_i - \lambda_i\rvert \le z_{\alpha/2}\lambda_i\sqrt{2/n}) \approx 1 - \alpha$，由此得到大样本 $100(1-\alpha)\%$ 置信区间

$$
\frac{\hat\lambda_i}{1 + z_{\alpha/2}\sqrt{2/n}} \le \lambda_i \le \frac{\hat\lambda_i}{1 - z_{\alpha/2}\sqrt{2/n}}.
$$

第 2 条表明：$\hat{\boldsymbol{e}}_i$ 在 $\boldsymbol{e}_i$ 周围近似正态分布，其各元素相关，且波动在很大程度上取决于特征值之间的间隔：若 $\lambda_i$ 与另一个特征值接近，$E_i$ 就很大，方向 $\hat{\boldsymbol{e}}_i$ 难以确定，这就是第 5.3.3 节那段话的定量形式。

## 小结

- $\boldsymbol{X}$ 的主成分为 $Y_i = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{X}$，其中 $(\lambda_i, \boldsymbol{e}_i)$ 是 $\Sigma$ 按递减顺序排列的特征对；它们互不相关，$\operatorname{Var}(Y_i) = \lambda_i$，$\sum_i\lambda_i = \operatorname{tr}\Sigma$ 为总方差，所以 $\lambda_k/\sum_i\lambda_i$ 是第 $k$ 个成分的贡献率。
- 系数 $e_{ik}$ 描述成分的整体，相关系数 $\rho_{Y_i, X_k} = e_{ik}\sqrt{\lambda_i}/\sqrt{\sigma_{kk}}$ 分别描述每个变量。
- 主成分分析不具有尺度不变性；变量量纲不可比时使用相关矩阵，其成分与 $\Sigma$ 的成分不同。
- 正态假设下各成分相互独立，是等密度椭球的轴。
- 样本主成分把 $\Sigma, \rho$ 换成 $S, R$；成分个数由碎石图、累计贡献率或 $R$ 的特征值大于 $1$ 来选择；前几个成分用于检查正态性，最后几个用于发现离群值。
- 保留 $r$ 个成分给出中心化数据的最佳秩 $r$ 逼近，误差为 $(n-1)\sum_{i > r}\hat\lambda_i$。
