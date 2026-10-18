---
title: 判别分析
description: Fisher 线性判别、最小期望误判代价分类、正态总体下的 LDA 与 QDA、多总体的 Fisher 判别，以及分类规则的评价。
source_hash: b2d3104a4f93
---

前面几章描述一组变量的结构（[主成分](/3.4.5)、[因子分析](/3.4.8)）或两组变量之间的关系（[典型相关](/3.4.9)）。本章转向一个有监督的问题：观测带有已知的类别标签，我们要构造一个规则，把新的观测分到某一类。两种思路在正态假设下给出同一个答案：Fisher 寻找最能把各类分开的变量线性组合；似然方法利用各类的密度、先验概率和误判代价，使期望误判代价最小，这正是[统计决策理论](/3.2.7#sec-7.9)中某个**损失函数**下的**贝叶斯行动**。由此得到的规则——线性判别分析与二次判别分析——建立在**多元正态分布**（[3.4.2](/3.4.2)）和均值向量的比较（[3.4.4](/3.4.4)）之上。本章最后讨论如何估计分类规则的误判率，特别是交叉验证；[下一章](/3.4.11)选择聚类数目时还会用到它。

## 10.1. 引言

先看几个分类问题。

- 大学要制定录取规则。对往届学生，学校知道他们是否顺利毕业，以及他们的高中成绩和入学考试成绩；新的申请者只有成绩。
- 根据脑成像测量，判断受试者处于哪一种心理状态。
- 对 150 朵鸢尾花，记录了四项测量（萼片长与宽、花瓣长与宽）以及品种（setosa、versicolor、virginica）。Fisher 于 1936 年为区分这三个品种提出了他的方法；下文以鸢尾花数据作为贯穿始终的例子。

判别分析（discriminant analysis）研究分离与分类：根据类别已知的对象的测量值 $\boldsymbol{x}$，构造一个规则，把类别未知的新对象分到预先给定的某一类。训练数据是一个 $n \times (p+1)$ 的数组，最后一列是类别标签——分类变量而非连续变量：

$$
D = \begin{bmatrix} x_{11} & x_{12} & \cdots & x_{1p} & g_1 \\ x_{21} & x_{22} & \cdots & x_{2p} & g_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ x_{n1} & x_{n2} & \cdots & x_{np} & g_n \end{bmatrix}, \qquad \tilde D = \begin{bmatrix} x_{01} & \cdots & x_{0p} & ? \end{bmatrix},
$$

任务是填上新的一行 $\tilde D$ 的标签。在机器学习中，同样的问题称为模式识别或分类。

当类别无法直接观测时就需要分类：类别要到将来才揭晓（申请者能否毕业），观测类别会毁坏对象（灯泡的寿命），或者类别信息无法获得、代价高昂（需要手术才能确诊）。这是一个预测问题，但与[线性回归](/3.4.7)不同，响应是类别标签。我们研究两种方法：

1. Fisher 线性判别分析，一种几何方法；
2. 基于 **Bayes 公式**的似然分类。

## 10.2. 两总体的 Fisher 方法

Fisher 的想法是把多元观测 $\boldsymbol{x}$ 变换为一元观测 $y = \boldsymbol{a}^{\mathsf T}\boldsymbol{x}$，使来自总体 $\pi_1$ 与 $\pi_2$ 的 $y$ 值尽可能分开。唯一的假设是两个总体有相同的协方差矩阵 $\Sigma_1 = \Sigma_2$；不假设正态性。

设 $\boldsymbol{x}_{11}, \dots, \boldsymbol{x}_{1n_1}$ 是来自 $\pi_1$ 的样本，$\boldsymbol{x}_{21}, \dots, \boldsymbol{x}_{2n_2}$ 是来自 $\pi_2$ 的样本，样本均值为 $\bar{\boldsymbol{x}}_1, \bar{\boldsymbol{x}}_2$，样本协方差矩阵为 $S_1, S_2$。投影值为 $y_{ij} = \boldsymbol{a}^{\mathsf T}\boldsymbol{x}_{ij}$，其均值为 $\bar y_i = \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_i$。分离程度用投影均值之差相对于 $y$ 的合并标准差来度量：

$$
\text{分离度} = \frac{\lvert \bar y_1 - \bar y_2\rvert}{s_y}, \qquad s_y^2 = \frac{\sum_{j=1}^{n_1}(y_{1j}-\bar y_1)^2 + \sum_{j=1}^{n_2}(y_{2j}-\bar y_2)^2}{n_1+n_2-2}.
$$

把 $y_{ij} - \bar y_i = \boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_{ij} - \bar{\boldsymbol{x}}_i)$ 代入得

$$
s_y^2 = \frac{\sum_{j}\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_{1j}-\bar{\boldsymbol{x}}_1)(\boldsymbol{x}_{1j}-\bar{\boldsymbol{x}}_1)^{\mathsf T}\boldsymbol{a} + \sum_{j}\boldsymbol{a}^{\mathsf T}(\boldsymbol{x}_{2j}-\bar{\boldsymbol{x}}_2)(\boldsymbol{x}_{2j}-\bar{\boldsymbol{x}}_2)^{\mathsf T}\boldsymbol{a}}{n_1+n_2-2} = \boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a},
$$

其中 $S_{\mathrm{pooled}} = \frac{(n_1-1)S_1 + (n_2-1)S_2}{n_1+n_2-2}$ 是**合并样本协方差矩阵**，即 [3.4.4](/3.4.4) 比较两个均值向量时所用的公共协方差矩阵的估计。

**定理 10.2.1（Fisher 线性判别）** 记 $\boldsymbol{d} = \bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2$，设 $S_{\mathrm{pooled}}$ 正定。线性组合

$$
\hat y = \hat{\boldsymbol{a}}^{\mathsf T}\boldsymbol{x} = (\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}\boldsymbol{x}
$$
在所有非零系数向量 $\boldsymbol{a}$ 中使分离度的平方

$$
\frac{(\bar y_1 - \bar y_2)^2}{s_y^2} = \frac{(\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_1 - \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_2)^2}{\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a}} = \frac{(\boldsymbol{a}^{\mathsf T}\boldsymbol{d})^2}{\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a}}
$$
达到最大；最大值点在相差一个非零倍数的意义下唯一，最大值为 $D^2 = (\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)$。

**证明** 这就是取 $B = S_{\mathrm{pooled}}$ 的最大化引理（引理 4.3.1）。直接证明：对内积 $\langle \boldsymbol{u}, \boldsymbol{v}\rangle = \boldsymbol{u}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{v}$ 用 Cauchy–Schwarz 不等式，

$$
(\boldsymbol{a}^{\mathsf T}\boldsymbol{d})^2 = \bigl(\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}(S_{\mathrm{pooled}}^{-1}\boldsymbol{d})\bigr)^2 \le (\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a})(\boldsymbol{d}^{\mathsf T}S_{\mathrm{pooled}}^{-1}\boldsymbol{d}),
$$
等号成立当且仅当存在 $c \ne 0$ 使 $\boldsymbol{a} = c\,S_{\mathrm{pooled}}^{-1}\boldsymbol{d}$。两边除以 $\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a} > 0$ 即得上界 $D^2$，它在 $\hat{\boldsymbol{a}} = S_{\mathrm{pooled}}^{-1}\boldsymbol{d}$ 处取到。$\square$

最大分离度 $D^2$ 是两个样本均值之间的 **Mahalanobis 距离**的平方；两样本 **Hotelling T² 统计量** 统计量正是由它构成的，$T^2 = \frac{n_1 n_2}{n_1+n_2}D^2$（[3.4.4](/3.4.4)）。因此 Fisher 方向就是两样本检验看到差异最大的方向。从几何上看，$S_{\mathrm{pooled}}^{-1}$ 先把数据"白化"，使类内散布变成球形；在白化后的坐标中，最佳方向就是连接两个均值的直线。

对新观测 $\boldsymbol{x}_0$ 分类时，计算 $\hat y_0 = \hat{\boldsymbol{a}}^{\mathsf T}\boldsymbol{x}_0$，与投影均值的中点

$$
\hat m = \tfrac{1}{2}(\bar y_1 + \bar y_2) = \tfrac12(\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1 + \bar{\boldsymbol{x}}_2)
$$
比较：若 $\hat y_0 \ge \hat m$ 则判给 $\pi_1$，否则判给 $\pi_2$。这就是最初形式的线性判别分析；§10.4 将说明，对先验与代价都相等的两个正态总体，它也是最优规则。

## 10.3. 考虑代价与先验的分类

### 10.3.1. 模型

好的分类规则应当误判少，但还应考虑到不同的误判可能代价不同（把病人判为健康比反过来更糟），以及一个总体可能比另一个常见得多。例如，假设两个鸢尾花品种的商业价值不同，并且其中一个品种很稀少。

设 $f_1(\boldsymbol{x})$ 与 $f_2(\boldsymbol{x})$ 分别是 $p \times 1$ 随机向量 $\boldsymbol{X}$ 在总体 $\pi_1$、$\pi_2$ 中的概率密度，$\Omega$ 是样本空间，即所有可能观测 $\boldsymbol{x}$ 的集合。分类规则就是把 $\Omega$ 分成两个不相交的区域：$R_1$ 是判为 $\pi_1$ 的 $\boldsymbol{x}$ 的集合，$R_2 = \Omega \setminus R_1$ 是判为 $\pi_2$ 的集合。设 $p_1, p_2$ 是 $\pi_1, \pi_2$ 的先验概率，$p_1 + p_2 = 1$。误判代价构成代价矩阵：

| 真实总体 | 判为 $\pi_1$ | 判为 $\pi_2$ |
|---|---|---|
| $\pi_1$ | $0$ | $c(2\mid 1)$ |
| $\pi_2$ | $c(1\mid 2)$ | $0$ |

密度、先验与代价是给定的；区域 $R_1, R_2$ 是要求的。误判的条件概率为

$$
\mathbb{P}(2\mid 1) = \mathbb{P}(\boldsymbol{X}\in R_2 \mid \pi_1) = \int_{R_2} f_1(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}, \qquad \mathbb{P}(1\mid 2) = \mathbb{P}(\boldsymbol{X}\in R_1 \mid \pi_2) = \int_{R_1} f_2(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x},
$$
于是一个观测被误判为 $\pi_2$ 的概率是 $\mathbb{P}(\boldsymbol{X}\in R_2, \boldsymbol{X}\in\pi_1) = \mathbb{P}(2\mid 1)\,p_1$，被误判为 $\pi_1$ 的概率是 $\mathbb{P}(1\mid 2)\,p_2$。

### 10.3.2. 使期望误判代价最小

**定义 10.3.1（期望误判代价）** 对一个观测分类的代价是随机变量：当 $\boldsymbol{X}\in\pi_1$ 且 $\boldsymbol{X}\in R_2$ 时等于 $c(2\mid 1)$，当 $\boldsymbol{X}\in\pi_2$ 且 $\boldsymbol{X}\in R_1$ 时等于 $c(1\mid 2)$，其余情形为 $0$。它的期望

$$
\mathrm{ECM}(R_1) = c(2\mid 1)\,\mathbb{P}(2\mid 1)\,p_1 + c(1\mid 2)\,\mathbb{P}(1\mid 2)\,p_2
$$
称为**期望误判代价**。

**定理 10.3.1（最小 ECM 规则）** 使 ECM 最小的区域 $R_1$ 与 $R_2$ 为

$$
R_1 = \left\{\boldsymbol{x} : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} \ge \frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right\}, \qquad R_2 = \left\{\boldsymbol{x} : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} < \frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right\},
$$
即当（密度比）$\ge$（代价比）$\times$（先验比）时判为 $\pi_1$。

**证明** 由 $R_1 \cup R_2 = \Omega$ 与 $\int_\Omega f_1 = 1$，有 $\mathbb{P}(2\mid 1) = 1 - \int_{R_1} f_1(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$。于是

$$
\mathrm{ECM}(R_1) = c(2\mid 1)\,p_1 + \int_{R_1} h(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}, \qquad h(\boldsymbol{x}) = c(1\mid 2)\,p_2 f_2(\boldsymbol{x}) - c(2\mid 1)\,p_1 f_1(\boldsymbol{x}).
$$
第一项与规则无关；积分在 $R_1$ 恰好由被积函数非正的点组成，即 $R_1 = \{\boldsymbol{x} : h(\boldsymbol{x}) \le 0\}$ 时最小。把 $h(\boldsymbol{x}) \le 0$ 移项即得所述不等式。（$h(\boldsymbol{x}) = 0$ 的点可以任意归类。）$\square$

**推论 10.3.1** 最小期望代价区域的几种特殊情形：

1. 先验相等，$p_2/p_1 = 1$：$R_1 : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} \ge \frac{c(1\mid 2)}{c(2\mid 1)}$；
2. 误判代价相等，$c(1\mid 2)/c(2\mid 1) = 1$：$R_1 : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} \ge \frac{p_2}{p_1}$；
3. 先验相等且代价相等（更一般地，$\frac{p_2}{p_1} = \frac{c(2\mid 1)}{c(1\mid 2)}$）：$R_1 : \frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} \ge 1$。

各情形中 $R_2$ 都是 $R_1$ 的补集。起作用的只有代价之比和先验之比——这很方便，因为绝对代价很少知道，相对代价却常常知道。

### 10.3.3. 其他准则

**定义 10.3.2（总误判概率）** 不考虑代价，规则的**总误判概率**为

$$
\mathrm{TPM} = \mathbb{P}(\text{误判一个观测}) = \mathbb{P}(1\mid 2)\,p_2 + \mathbb{P}(2\mid 1)\,p_1 = p_2\int_{R_1} f_2(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} + p_1\int_{R_2} f_1(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}.
$$

TPM 就是 $c(1\mid 2) = c(2\mid 1) = 1$ 时的 ECM，所以使它最小的规则是推论 10.3.1 的情形 2。

**定义 10.3.3（贝叶斯分类器）** 由 **Bayes 公式**，观测 $\boldsymbol{x}_0$ 来自 $\pi_1$ 的后验概率为

$$
\mathbb{P}(\pi_1 \mid \boldsymbol{x}_0) = \frac{p_1 f_1(\boldsymbol{x}_0)}{p_1 f_1(\boldsymbol{x}_0) + p_2 f_2(\boldsymbol{x}_0)}, \qquad \mathbb{P}(\pi_2 \mid \boldsymbol{x}_0) = \frac{p_2 f_2(\boldsymbol{x}_0)}{p_1 f_1(\boldsymbol{x}_0) + p_2 f_2(\boldsymbol{x}_0)}.
$$
所谓**贝叶斯分类器**，是在 $\mathbb{P}(\pi_1 \mid \boldsymbol{x}_0) > \mathbb{P}(\pi_2 \mid \boldsymbol{x}_0)$ 时把 $\boldsymbol{x}_0$ 判给 $\pi_1$、否则判给 $\pi_2$ 的规则。

由于 $\mathbb{P}(\pi_1\mid\boldsymbol{x}_0) > \mathbb{P}(\pi_2\mid\boldsymbol{x}_0)$ 等价于 $p_1f_1(\boldsymbol{x}_0) > p_2f_2(\boldsymbol{x}_0)$，贝叶斯分类器仍是代价相等时的最小 ECM 规则，三个准则一致。用[决策理论](/3.2.7#sec-7.9)的语言：行动是选择一个总体，未知状态是真实总体，最小 ECM 规则就是以代价矩阵为**损失函数**的**贝叶斯行动**；在 $0$–$1$ 损失下，它化为选择**后验分布**概率较大的总体。因此 ECM、TPM 与贝叶斯分类器是同一规则的三种视角；剩下的问题是给出密度。

## 10.4. 两个多元正态总体

现在设 $\pi_1 : \mathcal{N}_p(\boldsymbol{\mu}_1, \Sigma_1)$，$\pi_2 : \mathcal{N}_p(\boldsymbol{\mu}_2, \Sigma_2)$。与比较两个均值向量（[3.4.4](/3.4.4)）时一样，分 $\Sigma_1 = \Sigma_2$ 与 $\Sigma_1 \ne \Sigma_2$ 两种情形讨论。

### 10.4.1. 协方差矩阵相等：LDA

当 $\Sigma_1 = \Sigma_2 = \Sigma$ 时，密度为

$$
f_i(\boldsymbol{x}) = \frac{1}{(2\pi)^{p/2}\lvert\Sigma\rvert^{1/2}}\exp\left\{-\frac12(\boldsymbol{x}-\boldsymbol{\mu}_i)^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_i)\right\}, \qquad i = 1, 2.
$$

**定理 10.4.1** 对协方差矩阵同为 $\Sigma$ 的两个正态总体，使 ECM 最小的区域为

$$
R_1 : (\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}\boldsymbol{x} - \frac12(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1+\boldsymbol{\mu}_2) \ge \ln\left[\frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right],
$$
$R_2$ 是反向严格不等式成立的集合。

**证明** 在定理 10.3.1 中取对数，$R_1 = \{\boldsymbol{x} : \ln(f_1(\boldsymbol{x})/f_2(\boldsymbol{x})) \ge \ln[(c(1\mid 2)/c(2\mid 1))(p_2/p_1)]\}$。协方差矩阵相等，归一化常数相消，所以

$$
\begin{aligned}
\ln\frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} &= -\frac12(\boldsymbol{x}-\boldsymbol{\mu}_1)^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_1) + \frac12(\boldsymbol{x}-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_2) \\
&= -\frac12\bigl(-2\boldsymbol{\mu}_1^{\mathsf T}\Sigma^{-1}\boldsymbol{x} + \boldsymbol{\mu}_1^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_1\bigr) + \frac12\bigl(-2\boldsymbol{\mu}_2^{\mathsf T}\Sigma^{-1}\boldsymbol{x} + \boldsymbol{\mu}_2^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_2\bigr) \\
&= (\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}\boldsymbol{x} - \frac12(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1+\boldsymbol{\mu}_2).
\end{aligned}
$$
第二行中二次项 $\boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}$ 相消，并用到 $\boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_i = \boldsymbol{\mu}_i^{\mathsf T}\Sigma^{-1}\boldsymbol{x}$（标量等于其转置）。最后一行出于同样的理由用到 $\boldsymbol{\mu}_2^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_1 = \boldsymbol{\mu}_1^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_2$。$\square$

实际中 $\boldsymbol{\mu}_1, \boldsymbol{\mu}_2, \Sigma$ 未知，用两样本推断中的估计 $\bar{\boldsymbol{x}}_1, \bar{\boldsymbol{x}}_2$ 与 $S_{\mathrm{pooled}}$ 代替。

**定义 10.4.1（线性判别分析）** 对协方差矩阵相等的两个正态总体，估计的最小 ECM 规则是：若

$$
(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}\boldsymbol{x} - \frac12(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1+\bar{\boldsymbol{x}}_2) \ge \ln\left[\frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right]
$$
则把 $\boldsymbol{x}$ 判给 $\pi_1$，否则判给 $\pi_2$，其中 $S_{\mathrm{pooled}} = \frac{1}{n_1+n_2-2}\left[\sum_{j=1}^{n_1}(\boldsymbol{x}_{1j}-\bar{\boldsymbol{x}}_1)(\boldsymbol{x}_{1j}-\bar{\boldsymbol{x}}_1)^{\mathsf T} + \sum_{j=1}^{n_2}(\boldsymbol{x}_{2j}-\bar{\boldsymbol{x}}_2)(\boldsymbol{x}_{2j}-\bar{\boldsymbol{x}}_2)^{\mathsf T}\right]$。这一规则称为**线性判别分析**（LDA）：它的分界是一个超平面。

当 $\frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1} = 1$ 时右端为 $0$；记 $\hat y = (\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}S_{\mathrm{pooled}}^{-1}\boldsymbol{x} = \hat{\boldsymbol{a}}^{\mathsf T}\boldsymbol{x}$，$\bar y_i = \hat{\boldsymbol{a}}^{\mathsf T}\bar{\boldsymbol{x}}_i$，规则成为

$$
R_1 : \hat y \ge \tfrac12(\bar y_1 + \bar y_2), \qquad R_2 : \hat y < \tfrac12(\bar y_1 + \bar y_2),
$$
这恰好是 §10.2 的 Fisher 规则。Fisher 不借助正态性、通过最大化分离度得到它；似然方法则说明，在协方差相等的正态假设下（且先验与代价相等），同一规则使期望代价最小。先验或代价不等只是平移阈值。

**例 10.4.1** 对使用全部四项测量的鸢尾花数据，以样本比例为先验（这里相等，每个品种 $50$ 朵），LDA 对训练数据的分类结果如下（行为真实品种，列为预测品种）。

| | setosa | versicolor | virginica |
|---|---|---|---|
| setosa | $50$ | $0$ | $0$ |
| versicolor | $0$ | $48$ | $2$ |
| virginica | $0$ | $1$ | $49$ |

150 朵花中有 3 朵被误判，都在 versicolor 与 virginica 的重叠区域；setosa 被完全分开。（这里用的三类规则见 §10.5。）

### 10.4.2. 协方差矩阵不等：QDA

**定理 10.4.2** 对两个正态总体 $\mathcal{N}_p(\boldsymbol{\mu}_1, \Sigma_1)$ 与 $\mathcal{N}_p(\boldsymbol{\mu}_2, \Sigma_2)$，$\Sigma_1 \ne \Sigma_2$，使 ECM 最小的区域为

$$
R_1 : -\frac12\boldsymbol{x}^{\mathsf T}(\Sigma_1^{-1} - \Sigma_2^{-1})\boldsymbol{x} + (\boldsymbol{\mu}_1^{\mathsf T}\Sigma_1^{-1} - \boldsymbol{\mu}_2^{\mathsf T}\Sigma_2^{-1})\boldsymbol{x} - k \ge \ln\left[\frac{c(1\mid 2)}{c(2\mid 1)}\cdot\frac{p_2}{p_1}\right],
$$
$R_2$ 是反向严格不等式成立的集合，其中

$$
k = \frac12\ln\frac{\lvert\Sigma_1\rvert}{\lvert\Sigma_2\rvert} + \frac12\bigl(\boldsymbol{\mu}_1^{\mathsf T}\Sigma_1^{-1}\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2^{\mathsf T}\Sigma_2^{-1}\boldsymbol{\mu}_2\bigr).
$$

**证明** 现在归一化常数为 $\ln(f_1/f_2)$ 贡献 $-\frac12\ln(\lvert\Sigma_1\rvert/\lvert\Sigma_2\rvert)$；与前面一样展开两个二次型，得 $\ln\frac{f_1(\boldsymbol{x})}{f_2(\boldsymbol{x})} = -\frac12\boldsymbol{x}^{\mathsf T}(\Sigma_1^{-1}-\Sigma_2^{-1})\boldsymbol{x} + (\boldsymbol{\mu}_1^{\mathsf T}\Sigma_1^{-1}-\boldsymbol{\mu}_2^{\mathsf T}\Sigma_2^{-1})\boldsymbol{x} - k$。再用定理 10.3.1。$\square$

**定义 10.4.2（二次判别分析）** 在定理 10.4.2 中用 $\bar{\boldsymbol{x}}_i$ 代替 $\boldsymbol{\mu}_i$、用 $S_i$ 代替 $\Sigma_i$，得到**二次判别分析**（QDA）规则；它的分界是二次曲面。

二次项恰在 $\Sigma_1 = \Sigma_2$ 时消失，此时 QDA 化为 LDA。QDA 为每一类分别估计协方差矩阵，每类 $p(p+1)/2$ 个参数，而不是总共 $p(p+1)/2$ 个，因此需要更大的样本。它也更依赖正态性：线性规则即使不正态也有 Fisher 的理由，二次规则则没有，非正态数据可能严重影响它。

**例 10.4.2** 对鸢尾花数据，QDA 误判的训练样本与 LDA 相同，都是那三朵，所以本例中两者的表观误判率相同；在 §10.6 的留一法评价下，QDA 比 LDA 多错一个。

![两个协方差矩阵不等的模拟正态总体。左：LDA 的分界是直线。右：QDA 的分界是适应不同散布的二次曲线。](./plots/lda-qda-boundaries.py)

## 10.5. 多总体的分类

本节把两种方法推广到 $g > 2$ 个总体。重点是 Fisher 判别的几何意义和规则的应用；推导与两总体情形类似。

### 10.5.1. 最小 ECM 规则

设 $f_i$ 是总体 $\pi_i$ 的密度，$p_i$ 是其先验概率，$R_i$ 是判为 $\pi_i$ 的区域，$c(k\mid i)$ 是把 $\pi_i$ 的对象判为 $\pi_k$ 的代价（$c(i\mid i) = 0$）。记 $\mathbb{P}(k\mid i) = \mathbb{P}(\boldsymbol{X}\in R_k \mid \pi_i) = \int_{R_k} f_i(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$，则 $\pi_i$ 中对象的条件期望代价为 $\mathrm{ECM}(i) = \sum_{k\ne i}\mathbb{P}(k\mid i)\,c(k\mid i)$，并且

$$
\mathrm{ECM} = \sum_{i=1}^g p_i\,\mathrm{ECM}(i) = \sum_{i=1}^g p_i\sum_{k\ne i}\mathbb{P}(k\mid i)\,c(k\mid i).
$$

**定理 10.5.1** 在所有划分 $R_1, \dots, R_g$ 中，使 ECM 最小的规则是把 $\boldsymbol{x}$ 判给使

$$
\sum_{i\ne k} p_i f_i(\boldsymbol{x})\,c(k\mid i)
$$
最小的总体 $\pi_k$。若所有误判代价相等，则当 $p_k f_k(\boldsymbol{x}) > p_i f_i(\boldsymbol{x})$ 对一切 $i \ne k$ 成立时判给 $\pi_k$，等价地，判给后验概率

$$
\mathbb{P}(\pi_k \mid \boldsymbol{x}) = \frac{p_k f_k(\boldsymbol{x})}{p_1 f_1(\boldsymbol{x}) + \cdots + p_g f_g(\boldsymbol{x})}
$$
最大的总体。

**证明** 交换求和次序，$\mathrm{ECM} = \sum_{k=1}^g\int_{R_k}\sum_{i\ne k}p_i f_i(\boldsymbol{x})\,c(k\mid i)\,\mathrm{d}\boldsymbol{x}$；当每个 $\boldsymbol{x}$ 都放入在该点被积函数最小的区域时，它最小。代价都等于 $c$ 时，被积函数为 $c\bigl(\sum_i p_i f_i(\boldsymbol{x}) - p_k f_k(\boldsymbol{x})\bigr)$，它在 $p_k f_k(\boldsymbol{x})$ 最大时最小。$\square$

对正态总体，最大化 $\ln(p_k f_k(\boldsymbol{x}))$ 给出二次判别得分 $-\frac12\ln\lvert\Sigma_k\rvert - \frac12(\boldsymbol{x}-\boldsymbol{\mu}_k)^{\mathsf T}\Sigma_k^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_k) + \ln p_k$；协方差矩阵同为 $\Sigma$ 时则是线性得分 $\boldsymbol{\mu}_k^{\mathsf T}\Sigma^{-1}\boldsymbol{x} - \frac12\boldsymbol{\mu}_k^{\mathsf T}\Sigma^{-1}\boldsymbol{\mu}_k + \ln p_k$。它们的样本版本就是 $g$ 类的 QDA 与 LDA。

### 10.5.2. 多类的 Fisher 判别

对 $g$ 类，Fisher 方法要回答三个问题：投影到几维？沿哪些方向投影？在投影空间中怎样给新单元分类？答案推广了**方差分析**中的变差分解。设 $\boldsymbol{x}_{lj}$（$j = 1, \dots, n_l$）是第 $l$ 类的样本，$\bar{\boldsymbol{x}}_l$ 为各类均值，$\bar{\boldsymbol{x}}$ 为总均值。对一个变量，总平方和分解为组间与组内两部分：

$$
\underbrace{\sum_{l=1}^g\sum_{j=1}^{n_l}(x_{lj}-\bar x)^2}_{\text{总（修正）平方和}} = \underbrace{\sum_{l=1}^g n_l(\bar x_l-\bar x)^2}_{\text{组间平方和}} + \underbrace{\sum_{l=1}^g\sum_{j=1}^{n_l}(x_{lj}-\bar x_l)^2}_{\text{组内平方和}},
$$
对向量，同样的恒等式对平方和与交叉乘积矩阵成立：

$$
\sum_{l=1}^g\sum_{j=1}^{n_l}(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}})(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}})^{\mathsf T} = B + W, \qquad B = \sum_{l=1}^g n_l(\bar{\boldsymbol{x}}_l-\bar{\boldsymbol{x}})(\bar{\boldsymbol{x}}_l-\bar{\boldsymbol{x}})^{\mathsf T}, \quad W = \sum_{l=1}^g\sum_{j=1}^{n_l}(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}}_l)(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}}_l)^{\mathsf T}.
$$

假设协方差矩阵相同，$\Sigma_1 = \cdots = \Sigma_g = \Sigma$，考虑 $Y = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$。则在每个总体中 $\mathbb{E}[Y \mid \pi_i] = \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}_i$，$\operatorname{Var}(Y) = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}$。$Y$ 的样本均值在各类中为 $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_i$，总体上为 $\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}$；投影后数据的组间平方和为 $\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}$，组内平方和为 $\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}$。Fisher 准则是比值

$$
\frac{\sum_{i=1}^g n_i(\boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}}_i - \boldsymbol{a}^{\mathsf T}\bar{\boldsymbol{x}})^2}{\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}} = \frac{\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}},
$$
即投影后各类中心的散布相对于类内散布的大小。它是一个广义 **Rayleigh 商**，其最大化是一个广义特征值问题。

**定理 10.5.2（Fisher 判别）** 设 $W$ 正定，$\hat\lambda_1 \ge \cdots \ge \hat\lambda_s > 0$ 是 $W^{-1}B$ 的 $s \le \min(g-1, p)$ 个非零**特征值**，$\hat{\boldsymbol{e}}_1, \dots, \hat{\boldsymbol{e}}_s$ 是相应的**特征向量**，标准化使 $\hat{\boldsymbol{e}}_k^{\mathsf T}S_{\mathrm{pooled}}\hat{\boldsymbol{e}}_k = 1$，其中 $S_{\mathrm{pooled}} = W/(n_1+\cdots+n_g-g)$ 是 $\Sigma$ 的估计。则使 $\frac{\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}}{\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}}$ 最大的系数向量是 $\hat{\boldsymbol{a}}_1 = \hat{\boldsymbol{e}}_1$，最大值为 $\hat\lambda_1$；对 $k = 2, \dots, s$，$\hat{\boldsymbol{a}}_k = \hat{\boldsymbol{e}}_k$ 在约束 $\hat{\boldsymbol{a}}_k^{\mathsf T}S_{\mathrm{pooled}}\hat{\boldsymbol{a}}_i = 0$（$i < k$）下使该比值最大，最大值为 $\hat\lambda_k$。线性组合 $\hat y_k = \hat{\boldsymbol{a}}_k^{\mathsf T}\boldsymbol{x}$ 称为第 $k$ 样本判别函数，$k \le s$。

**证明** 写 $W = W^{1/2}W^{1/2}$，令 $\boldsymbol{b} = W^{1/2}\boldsymbol{a}$：比值化为 $\frac{\boldsymbol{b}^{\mathsf T}W^{-1/2}BW^{-1/2}\boldsymbol{b}}{\boldsymbol{b}^{\mathsf T}\boldsymbol{b}}$，即对称半正定矩阵 $W^{-1/2}BW^{-1/2}$ 的 Rayleigh 商。它在正交约束下的逐次最大值是其特征值，在其特征向量 $\boldsymbol{b}_k$ 处取到（[2.1.7](/2.1.7)）。$W^{-1/2}BW^{-1/2}$ 与 $W^{-1}B$ 有相同的特征值，$\boldsymbol{a}_k = W^{-1/2}\boldsymbol{b}_k$ 是 $W^{-1}B$ 的特征向量；正交性 $\boldsymbol{b}_i^{\mathsf T}\boldsymbol{b}_k = 0$ 化为 $\boldsymbol{a}_i^{\mathsf T}W\boldsymbol{a}_k = 0$，即 $\boldsymbol{a}_i^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a}_k = 0$。最后，$B$ 是 $g$ 个秩一矩阵之和，其向量 $\bar{\boldsymbol{x}}_l - \bar{\boldsymbol{x}}$ 满足 $\sum_l n_l(\bar{\boldsymbol{x}}_l - \bar{\boldsymbol{x}}) = \boldsymbol{0}$，所以 $\operatorname{rank}(B) \le \min(g-1, p)$。$\square$

在合并度量下，各判别函数互不相关且方差为 1：$i = k \le s$ 时 $\hat{\boldsymbol{a}}_i^{\mathsf T}S_{\mathrm{pooled}}\hat{\boldsymbol{a}}_k = 1$，否则为 $0$。两类时 $B$ 的秩为 1，$\hat{\boldsymbol{a}}_1 \propto S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2)$，回到定理 10.2.1。

分类时，记 $Y_k = \boldsymbol{a}_k^{\mathsf T}\boldsymbol{X}$ 为第 $k$ 判别函数，$\boldsymbol{Y} = (Y_1, \dots, Y_r)^{\mathsf T}$ 为前 $r \le s$ 个判别函数组成的向量；它在总体 $\pi_i$ 中的均值为 $\boldsymbol{\mu}_{iY} = (\boldsymbol{a}_1^{\mathsf T}\boldsymbol{\mu}_i, \dots, \boldsymbol{a}_r^{\mathsf T}\boldsymbol{\mu}_i)^{\mathsf T}$，由标准化，其协方差矩阵为单位阵。Fisher 规则把 $\boldsymbol{y}$ 判给投影均值在欧氏距离下最近的类：

$$
\text{若 } (\boldsymbol{y}-\boldsymbol{\mu}_{kY})^{\mathsf T}(\boldsymbol{y}-\boldsymbol{\mu}_{kY}) = \sum_{j=1}^r(y_j - \mu_{kY_j})^2 \le \sum_{j=1}^r(y_j - \mu_{iY_j})^2 \text{ 对一切 } i \ne k \text{ 成立，则判给 } \pi_k,
$$
实际计算时代入样本量 $\hat{\boldsymbol{a}}_j$ 与 $\bar{\boldsymbol{x}}_i$。在判别坐标中各类散布是球形的，所以那里的欧氏距离就是原空间中的 Mahalanobis 距离；用全部 $s$ 个判别函数时，该规则与定理 10.5.1 中先验相等的线性规则一致。投影的价值在于：通常 $r = 1$ 或 $2$ 个判别函数就承载了几乎全部的分离信息，并且可以画出来。

**注 10.5.1** 求方向并不需要协方差矩阵相等：最大化 $\boldsymbol{a}^{\mathsf T}B\boldsymbol{a}/\boldsymbol{a}^{\mathsf T}W\boldsymbol{a}$ 只是寻找使各类中心相对于类内散布最分散的投影。分类这一步才需要这个假设：若协方差矩阵不同，投影后各类没有共同的球形散布，用到投影均值的欧氏距离来分类就不再合理。

**例 10.5.1** 对鸢尾花数据，$g = 3$，$p = 4$，所以有 $s = 2$ 个判别函数，判别得分图展示了线性规则所能利用的全部分离信息。仅第一判别函数就把 setosa 与另两个品种分开，并承载了 $99\%$ 以上的组间变差（$\hat\lambda_1/(\hat\lambda_1+\hat\lambda_2)$）。对一朵新花，计算它的两个判别得分，找出最近的投影类均值即可分类。

![鸢尾花数据在前两个样本判别函数上的投影（左）与在前两个主成分上的投影（右）。判别函数最大化组间散布相对于组内散布之比，主成分则不使用标签、最大化总方差；叉号标出各类均值。](./plots/iris-discriminant-projection.py)

**注 10.5.2（LDA 与典型相关）** 设 $\boldsymbol{X}$ 为测量值，第二组变量取类别示性变量 $Z_l = \boldsymbol{1}_{\{\text{第 } l \text{ 类}\}}$；由于示性变量之和为 1，只需其中 $g-1$ 个。这时 $\boldsymbol{X}$ 在**典型相关分析**（[3.4.9](/3.4.9)）中的第一典型系数向量与 Fisher 第一判别函数成比例，尽管两种方法的出发点不同。事实上，CCA 求的是 $\Sigma_{11}^{-1}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ 的特征向量。对示性变量，$\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ 的样本版本与 $B$ 成比例（$\boldsymbol{X}$ 中由类均值解释的变差），$\Sigma_{11}$ 的样本版本与 $B + W$ 成比例；在总体层面，这就是**全方差公式** $\operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[\operatorname{Cov}(\boldsymbol{X}\mid G)] + \operatorname{Cov}(\mathbb{E}[\boldsymbol{X}\mid G])$。若 $(B+W)^{-1}B\boldsymbol{a} = \rho^2\boldsymbol{a}$，则 $(1-\rho^2)B\boldsymbol{a} = \rho^2 W\boldsymbol{a}$，故

$$
W^{-1}B\boldsymbol{a} = \frac{\rho^2}{1-\rho^2}\boldsymbol{a}:
$$
两者特征向量相同，特征值满足 $\hat\lambda = \rho^2/(1-\rho^2)$，其中 $\rho$ 是典型相关系数。这一恒等式无论协方差矩阵是否相等都成立。

### 10.5.3. 与 MANOVA 的关系

分解 $B + W$ 正是多元方差分析（multivariate analysis of variance）即 MANOVA 所用的分解，后者检验 $g$ 个均值向量是否相等。单因素模型为

$$
\boldsymbol{X}_{lj} = \boldsymbol{\mu} + \boldsymbol{\tau}_l + \boldsymbol{e}_{lj}, \qquad j = 1, \dots, n_l, \ l = 1, \dots, g, \qquad \sum_{l=1}^g n_l\boldsymbol{\tau}_l = \boldsymbol{0},
$$
其中 $\boldsymbol{\mu}$ 是总均值，$\boldsymbol{\tau}_l$ 是处理效应（约束条件使其可识别），误差 $\boldsymbol{e}_{lj} \sim \mathcal{N}_p(\boldsymbol{0}, \Sigma)$ 相互独立。原假设为 $H_0 : \boldsymbol{\tau}_1 = \cdots = \boldsymbol{\tau}_g = \boldsymbol{0}$。每个观测分解为

$$
\boldsymbol{x}_{lj} = \underbrace{\bar{\boldsymbol{x}}}_{\text{总样本均值}} + \underbrace{(\bar{\boldsymbol{x}}_l - \bar{\boldsymbol{x}})}_{\text{处理效应的估计}} + \underbrace{(\boldsymbol{x}_{lj} - \bar{\boldsymbol{x}}_l)}_{\text{残差}},
$$
一元方差分析表中的平方和变成矩阵：

| 变差来源 | 平方和与交叉乘积矩阵 | 自由度 |
|---|---|---|
| 处理 | $B = \sum_{l} n_l(\bar{\boldsymbol{x}}_l-\bar{\boldsymbol{x}})(\bar{\boldsymbol{x}}_l-\bar{\boldsymbol{x}})^{\mathsf T}$ | $g-1$ |
| 残差（误差） | $W = \sum_{l}\sum_{j}(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}}_l)(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}}_l)^{\mathsf T}$ | $\sum_l n_l - g$ |
| 总计（对均值修正） | $B + W = \sum_{l}\sum_{j}(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}})(\boldsymbol{x}_{lj}-\bar{\boldsymbol{x}})^{\mathsf T}$ | $\sum_l n_l - 1$ |

MANOVA 的检验统计量都是 $W^{-1}B$ 的特征值 $\hat\lambda_k$ 的函数，例如 Wilks $\Lambda$ 统计量 $\lvert W\rvert/\lvert B+W\rvert = \prod_k(1+\hat\lambda_k)^{-1}$。MANOVA 问各类是否不同；Fisher 判别则指出它们在哪些方向上差别最大。

## 10.6. 分类函数的评价

两个严重重叠的总体能以很高的准确率分开吗？任何规则都不可能超越重叠所允许的程度。所以在评判一个方法之前，我们想知道可达到的界；我们还需要从数据估计任一方法的误判率。度量分两类：

- 密度 $f_1, f_2$ 已知时：总误判概率（基于总体），以及由样本构造的规则的实际误判率；
- 分布未知时（一般情形）：表观误判率与交叉验证误判率。

### 10.6.1. 最优误判率

**定义 10.6.1（最优误判率与实际误判率）** **最优误判率**是 TPM 的最小值，由 §10.3 的最小 TPM 规则达到。由样本构造的规则 $\hat R_1, \hat R_2$ 的**实际误判率**是它在真实密度下的 TPM：

$$
\mathrm{AER} = p_1\int_{\hat R_2} f_1(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} + p_2\int_{\hat R_1} f_2(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}.
$$

**命题 10.6.1** 设 $\pi_i = \mathcal{N}_p(\boldsymbol{\mu}_i, \Sigma)$，$i = 1, 2$，$p_1 = p_2$，记 $\Delta^2 = (\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)$ 为两总体间 Mahalanobis 距离的平方。则最优误判率为

$$
\min \mathrm{TPM} = \Phi\left(-\frac{\Delta}{2}\right),
$$
其中 $\Phi$ 是标准正态分布函数。

**证明** 先验与代价相等时，最优规则（定理 10.4.1）只通过 $Y = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ 依赖于 $\boldsymbol{x}$，其中 $\boldsymbol{a} = \Sigma^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)$：若 $Y \ge m = \frac12(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^{\mathsf T}\Sigma^{-1}(\boldsymbol{\mu}_1+\boldsymbol{\mu}_2)$ 则判给 $\pi_1$。在 $\pi_i$ 下，$Y$ 服从正态分布，均值 $\mu_{iY} = \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}_i$，方差 $\sigma_Y^2 = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} = \Delta^2$，并且 $m - \mu_{1Y} = -\frac12\Delta^2$，$m - \mu_{2Y} = \frac12\Delta^2$。因此

$$
\mathbb{P}(2\mid 1) = \mathbb{P}(Y < m \mid \pi_1) = \mathbb{P}\left(\frac{Y-\mu_{1Y}}{\sigma_Y} < \frac{-\Delta^2/2}{\Delta}\right) = \Phi\left(-\frac{\Delta}{2}\right),
$$
同理 $\mathbb{P}(1\mid 2) = \Phi(-\Delta/2)$。所以 $\min\mathrm{TPM} = \frac12\mathbb{P}(2\mid 1) + \frac12\mathbb{P}(1\mid 2) = \Phi(-\Delta/2)$。$\square$

例如 $\Delta^2 = 2.56$ 时 $\Delta = 1.6$，最小 TPM 为 $\Phi(-0.8) = 0.2119$：即使最优规则也会把约 $21\%$ 的个体判错。误判率只通过 $\Delta$ 依赖于总体，所以均值之间的 Mahalanobis 距离大是容易分类的条件。

![左：判别得分 Y 的两个正态密度，均值相距 Delta 的平方，方差同为 Delta 的平方；中点两侧的阴影尾部是两个误判概率。右：最优误判率 Phi(-Delta/2) 随 Delta 的变化。](./plots/optimum-error-rate.py)

### 10.6.2. 表观误判率

通常总体未知，我们需要一个不依赖模型的指标。思路是用比例估计概率：把样本分类规则用于训练数据，把结果列成表：

| | 预测为 $\pi_1$ | 预测为 $\pi_2$ | 合计 |
|---|---|---|---|
| 实际为 $\pi_1$ | $n_{1C}$ | $n_{1M} = n_1 - n_{1C}$ | $n_1$ |
| 实际为 $\pi_2$ | $n_{2M} = n_2 - n_{2C}$ | $n_{2C}$ | $n_2$ |

其中 $n_{iC}$ 是 $\pi_i$ 中被正确分类的个数，$n_{iM}$ 是被误判的个数。

**定义 10.6.2（表观误判率）** 上表称为规则的**混淆矩阵**。**表观误判率**（APER）是训练样本中被样本分类函数误判的观测所占的比例：

$$
\mathrm{APER} = \frac{n_{1M} + n_{2M}}{n_1 + n_2}.
$$

APER 直观、易算。遗憾的是它往往低估 AER，因为同一份数据用了两次：一次用来构造规则，一次用来评价规则。规则会迁就特定的样本，包括其中的噪声，所以在这份样本上的表现好于在新数据上的表现。设想两个正态总体和靠近分界的六个训练点：由它们构造的规则也许能把六个点全部分对，$\mathrm{APER} = 0$，而它在真实密度下的误判概率 AER 却是估计分界两侧错误一边的两块尾部面积之和。由于真实密度未知，AER 无法计算；能算的只有 APER，而它是乐观的。这就是**过拟合**（回归中已经遇到过，见 [3.4.7](/3.4.7)），它是统计学习的普遍问题，不限于判别分析。

### 10.6.3. 交叉验证

克服过拟合的办法是不把数据用两次：留出一个（或一组）观测，用其余数据构造规则，再在留出的观测上评价。让留出的部分轮遍全部数据，就得到误判率的近似无偏估计，代价是计算量更大。

**定义 10.6.3（交叉验证）** **交叉验证**把数据分成训练集（用于构造规则）与验证集（用于评价规则），并重复划分，使每个观测都恰好被用于验证一次。

1. **留一交叉验证**（LOOCV）：对每个样本点 $\boldsymbol{x}_i$，用除 $\boldsymbol{x}_i$ 外的全部数据构造规则，并用它对 $\boldsymbol{x}_i$ 分类；被误判的点所占比例就是误判率的估计。
2. $K$ 折交叉验证：把样本分成大小几乎相等的 $K$ 份；对每一份，用其余 $K-1$ 份构造规则，在这一份上评价；对 $K$ 个误判率取平均。

交叉验证是一种通用方法：凡是由数据拟合、用损失来评价的方法都可以用它。选择聚类数目（[3.4.11](/3.4.11)）和 $k$ 近邻分类中的近邻个数（[3.4.12](/3.4.12)）时还会用到它。

**例 10.6.1** 对鸢尾花数据的 LDA，APER 为 $3/150 = 0.02$，留一法误判率也是 $3/150 = 0.02$，混淆矩阵相同：三朵被误判的花仍被误判，没有新的错误。两个估计相同只是这个分离良好的例子中的巧合；通常交叉验证误判率大于 APER。参数更多的 QDA 的 APER 同样是 $0.02$，但留一法误判率为 $4/150 \approx 0.027$。

### 10.6.4. 其他评价指标

对两类问题，把一类称为阳性、另一类称为阴性；混淆矩阵于是给出真阳性（TP）、假阴性（FN）、假阳性（FP）与真阴性（TN）的个数。

**定义 10.6.4（准确率、精确率、召回率、特异度）** 对两类分类规则，

$$
\text{准确率} = \frac{\mathrm{TP}+\mathrm{TN}}{\mathrm{TP}+\mathrm{TN}+\mathrm{FP}+\mathrm{FN}}, \quad \text{精确率} = \frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}}, \quad \text{召回率} = \frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}}, \quad \text{特异度} = \frac{\mathrm{TN}}{\mathrm{TN}+\mathrm{FP}}.
$$
其中**准确率**等于 $1 - \mathrm{APER}$；**精确率**是被判为阳性者中真阳性所占的比例；**召回率**（又称**灵敏度**）是阳性中被检出的比例；**特异度**是阴性中被正确判为阴性的比例。

多数规则都有一个阈值（在定理 10.4.1 中是代价比与先验比之积的对数）。改变阈值就在灵敏度与特异度之间权衡；以真阳性率（灵敏度）对假阳性率（$1 -$ 特异度）作图，遍历所有阈值，得到 ROC 曲线（receiver operating characteristic curve）。随机猜测的规则落在对角线上；越好的规则越向左上角弯曲。曲线下面积（area under the curve）即 AUC，用一个介于 $0.5$（随机）与 $1$（完全分开）之间的数概括它。ROC 曲线是为两类设计的；阳性很少时更常用精确率—召回率曲线；ROC 曲线也有推广到多类的版本。

## 10.7. 讨论

### 10.7.1. 量纲的变化

变量的量纲相差悬殊时，是否应当标准化？对 LDA 不必：其结果在非奇异线性变换下不变，意义如下。若 $\boldsymbol{x}^* = A\boldsymbol{x} + \boldsymbol{b}$，$A$ 非奇异，则 $\bar{\boldsymbol{x}}_i^* = A\bar{\boldsymbol{x}}_i + \boldsymbol{b}$，$S_{\mathrm{pooled}}^* = AS_{\mathrm{pooled}}A^{\mathsf T}$，于是

$$
\hat{\boldsymbol{a}}^* = (S_{\mathrm{pooled}}^*)^{-1}(\bar{\boldsymbol{x}}_1^* - \bar{\boldsymbol{x}}_2^*) = A^{-\mathsf T}\hat{\boldsymbol{a}}, \qquad \hat{\boldsymbol{a}}^{*\mathsf T}\boldsymbol{x}^* = \hat{\boldsymbol{a}}^{\mathsf T}\boldsymbol{x} + \hat{\boldsymbol{a}}^{\mathsf T}A^{-1}\boldsymbol{b}.
$$
系数变了，但判别得分只差一个常数，而阈值也平移同样的常数，分离度 $D^2$ 不变。因此每个观测的分类都不变。标准化变量（对角的 $A$）只是对系数作伸缩，使它们更便于比较；对鸢尾花数据，标准化后的分类图就是原来的图换了坐标刻度。QDA 有同样的不变性。

### 10.7.2. 局限与变换

LDA 只能给出线性分界。排成同心圆环的两类，在原坐标 $(x_1, x_2)$ 下不能被任何线性规则分开，但经过变换 $(x_1, x_2) \mapsto (x_1^2, x_2^2)$ 后就能被一条直线分开。更一般地，五维空间 $(X_1, X_2, X_1X_2, X_1^2, X_2^2)$ 中的线性分界就是原平面上的二次分界。用这种方式扩大特征空间——显式地，或像**核主成分分析**（[3.4.6](/3.4.6)）那样通过核函数隐式地——可以把线性方法变成灵活的非线性方法。

### 10.7.3. 其他分类方法

从应用的角度，下列方法推广或取代 LDA。

- 正则化 LDA，用于 $S_{\mathrm{pooled}}$ 不满秩（例如 $p > n$）的情形：用 $S_{\mathrm{pooled}} + \lambda I_p$（$\lambda > 0$）代替 $S_{\mathrm{pooled}}$，于是 $R_1 : (\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}(S_{\mathrm{pooled}}+\lambda I_p)^{-1}\boldsymbol{x} \ge \frac12(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)^{\mathsf T}(S_{\mathrm{pooled}}+\lambda I_p)^{-1}(\bar{\boldsymbol{x}}_1+\bar{\boldsymbol{x}}_2)$；更一般的形式见 [3.4.12](/3.4.12)。
- 核 Fisher 判别分析，用于线性判别不合适的情形：在由核函数定义的特征空间中使用 Fisher 准则。
- 混合判别分析：每一类用正态混合分布而不是单个正态分布来描述（比较 [3.4.11](/3.4.11) 中的高斯混合）。
- Logistic 回归与 probit 回归，直接对后验概率建模，$\ln\frac{p}{1-p} = \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$ 或 $\Phi^{-1}(p) = \boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}$，其中 $p = \mathbb{P}(\pi_1\mid\boldsymbol{x})$。它们不要求正态性，但在正态模型成立时效率不如 LDA（[3.4.12](/3.4.12)）。
- 支持向量机、$k$ 近邻与决策树等统计学习方法。

其中两种值得细看。支持向量机（support vector machine）即 SVM，使用数据 $(\boldsymbol{x}_i, y_i)$，$i = 1, \dots, n$，标签 $y_i \in \{-1, 1\}$，以及线性函数 $f(\boldsymbol{x}) = \boldsymbol{\beta}^{\mathsf T}\boldsymbol{x} + \beta_0$。超平面 $\{\boldsymbol{x} : f(\boldsymbol{x}) = 0\}$ 的法向量为 $\boldsymbol{\beta}$，可以标准化为 $\|\boldsymbol{\beta}\| = 1$；规则按 $\operatorname{sgn}(f(\boldsymbol{x}))$ 分类；若两类可分，就能找到 $f$ 使 $y_i f(\boldsymbol{x}_i) > 0$ 对一切 $i$ 成立。在所有分离超平面中，SVM 选择间隔 $M$ 最大的一个：

$$
\max_{\boldsymbol{\beta}, \beta_0, \|\boldsymbol{\beta}\| = 1} M \quad \text{使得 } y_i(\boldsymbol{\beta}^{\mathsf T}\boldsymbol{x}_i + \beta_0) \ge M, \ i = 1, \dots, n,
$$
它等价于在 $y_i(\boldsymbol{\beta}^{\mathsf T}\boldsymbol{x}_i + \beta_0) \ge 1$ 的约束下求 $\min_{\boldsymbol{\beta}, \beta_0}\|\boldsymbol{\beta}\|$（令 $M = 1/\|\boldsymbol{\beta}\|$）。解只依赖于间隔边界上的点，即支持向量；远在本类内部的点不影响分界——这与 LDA 不同，LDA 通过均值与协方差用到所有点。两类重叠时，引入松弛变量 $\varepsilon_i$，允许一些点落在错误的一侧：

$$
\max_{\boldsymbol{\beta}, \beta_0, \|\boldsymbol{\beta}\| = 1} M \quad \text{使得 } y_i(\boldsymbol{\beta}^{\mathsf T}\boldsymbol{x}_i + \beta_0) \ge M(1 - \varepsilon_i), \quad \varepsilon_i \ge 0, \quad \sum_i\varepsilon_i \le C.
$$

决策树每次按一个变量递归地分割数据，每次分割都使所得结点中类别比例的不纯度函数最小，直到满足停止规则；然后对树剪枝。常用的不纯度函数有两个：熵，其最小化对应于结点标签的多项似然最大化；Gini 指数 $\sum_k \hat p_k(1-\hat p_k)$，它是按结点比例 $\hat p_k$ 随机给点贴标签的规则的期望误判率。

## 小结 {#summary}

| | 假设 | 规则 | 分界 |
|---|---|---|---|
| Fisher 判别（投影） | $\Sigma_1 = \Sigma_2$；不需正态性 | 最大化 $(\boldsymbol{a}^{\mathsf T}\boldsymbol{d})^2/\boldsymbol{a}^{\mathsf T}S_{\mathrm{pooled}}\boldsymbol{a}$，得 $\hat{\boldsymbol{a}} \propto S_{\mathrm{pooled}}^{-1}(\bar{\boldsymbol{x}}_1-\bar{\boldsymbol{x}}_2)$ | 线性 |
| 最小 ECM / 贝叶斯分类器 | 密度、先验、代价已知 | $f_1/f_2 \ge (c(1\mid 2)/c(2\mid 1))(p_2/p_1)$ | 任意 |
| LDA | 正态，$\Sigma_1 = \Sigma_2$ | 用 $\bar{\boldsymbol{x}}_i$、$S_{\mathrm{pooled}}$ 的最小 ECM；代价与先验平衡时即 Fisher 规则 | 线性 |
| QDA | 正态，$\Sigma_1 \ne \Sigma_2$ | 用 $\bar{\boldsymbol{x}}_i$、$S_i$ 的最小 ECM | 二次 |
| $g$ 类（Fisher） | 分类时需公共 $\Sigma$ | $W^{-1}B$ 的特征向量；最近的投影均值 | 线性 |

规则用 APER 或 ROC 曲线结合交叉验证来评价——交叉验证纠正了在自身训练数据上评价规则的乐观偏差；最小 TPM 给出可达到的准确率的界。在 R 中，LDA 与 QDA 分别是程序包 MASS 中的函数 `lda` 与 `qda`（新数据用 `predict`；选项 `CV = TRUE` 给出留一法预测）。
