---
title: 单因子实验：诊断、功效、随机效应与回归方法
description: 单因素方差分析的残差诊断（正态概率图、标准化残差、Bartlett 与 Levene 检验、Welch 方差分析、杠杆值 1/n_i）；由非中心 F 分布与 power.anova.test 得到的功效与样本量；单因素随机效应模型及其协方差结构、期望均方、方差分量的方差分析估计与 REML 估计、组内相关系数、置信区间，以及 aov、lm 与 lmer 的 R 输出；固定效应与随机效应的选择；以及对定量因子的回归方法，包括失拟与多项式项。
source_hash: dae0755aabe4
---

[3.8.3](/3.8.3) 的单因素方差分析与 [3.8.4](/3.8.4) 的多重比较都建立在一个模型之上，本章围绕这个模型的四个问题完成对单因子实验的研究。第一，它的假定（独立、方差相同的正态误差）是否得到数据的支持，方差不同时可以怎么办？第二，需要多少次重复，才能使 $F$ 检验检出给定大小的差异；这是同一个模型在规划方面的问题。第三，当因子的水平不是仅有的感兴趣的水平，而是从大量水平的总体中随机抽出的样本时，会发生什么变化；这导向随机效应模型、它的方差分量与组内相关。第四，当因子是定量的时，能否利用其水平的数值，对它们作回归，而不是把水平当作无序的类别？

所需的许多工具已经出现在线性回归课程中：残差图与方差相等的检验（[3.3.5](/3.3.5)）、杠杆值与帽子矩阵（[3.3.7](/3.3.7)）、失拟检验（[3.3.5](/3.3.5)）、多项式回归（[3.3.10](/3.3.10)），以及加权方差分析、变换与 Kruskal–Wallis 检验（[3.3.14](/3.3.14)）。这里我们在设计实验的情境下使用这些工具，并补充其特有的内容。全章使用两个贯穿的例子：[3.8.3](/3.8.3) 的等离子体刻蚀实验（四个 RF 功率水平，每个水平五片晶圆），以及一个关于随机选取的织机上所织织物强度的新实验。

## 5.1. 检查模型假定

单因素模型 $Y_{ij}=\mu+\tau_i+\varepsilon_{ij}$ 假定误差 $\varepsilon_{ij}$ 独立同服从 $\mathcal{N}(0,\sigma^2)$。$F$ 检验、置信区间与多重比较的有效性都来自这一假定，所以必须加以检查。误差是观测不到的，但**残差**

$$
e_{ij}=y_{ij}-\hat y_{ij}=y_{ij}-\bar y_{i\cdot}
$$
估计了它们：在模型下，$e_{ij}$ 服从均值为 $0$、方差为 $\sigma^2(1-1/n_i)$ 的正态分布，所以看起来像正态噪声样本的残差支持模型，而系统的模式则揭示偏离。要问三个问题：误差是否正态，是否有相同的方差，是否独立？它们背后还有更一般的问题：这是不是正确的模型，是否有扭曲分析的离群值？

对刻蚀数据，残差为

| RF 功率 (W) | 残差（括号内为试验顺序） | $\bar y_{i\cdot}$ |
|---|---|---|
| 160 | $23.8\ (13)$, $-9.2\ (14)$, $-21.2\ (8)$, $-12.2\ (5)$, $18.8\ (4)$ | 551.2 |
| 180 | $-22.4\ (18)$, $5.6\ (9)$, $2.6\ (6)$, $-8.4\ (16)$, $22.6\ (17)$ | 587.4 |
| 200 | $-25.4\ (7)$, $25.6\ (19)$, $-15.4\ (10)$, $11.6\ (20)$, $3.6\ (1)$ | 625.4 |
| 220 | $18.0\ (2)$, $-7.0\ (3)$, $8.0\ (15)$, $-22.0\ (11)$, $3.0\ (12)$ | 707.0 |

其中括号里的数字记录了 20 次试验进行的顺序（设计是**完全随机化设计**，所以顺序是一个随机排列）。

### 5.1.1. 正态性、离群值与独立性

**定义 5.1.1（正态概率图）** 样本 $x_1,\dots,x_m$ 的**正态概率图**（正态 Q–Q 图）画出排序后的值 $x_{(1)}\le\cdots\le x_{(m)}$ 对标准正态分布相应分位数 $\Phi^{-1}\big((k-0.5)/m\big)$（$k=1,\dots,m$，或类似的作图位置）的点。如果样本来自正态分布，这些点靠近一条直线，其截距与斜率估计均值与标准差。

应用于残差时，该图检查误差的正态性。即使恰好正态，小样本也会围绕直线摆动，所以要找的是清楚的系统形状：S 形（轻尾或重尾）或弯曲（偏斜）。适度的偏离对固定效应的 $F$ 检验影响不大，它对非正态性是稳健的；重尾与离群值的影响更大。

离群值的粗略检查使用尺度化残差

$$
d_{ij}=\frac{e_{ij}}{\sqrt{\mathrm{MS}_{\mathrm{E}}}}.
$$
若误差服从 $\mathcal{N}(0,\sigma^2)$，则 $d_{ij}$ 近似服从 $\mathcal{N}(0,1)$，所以约 $95\%$ 的 $d_{ij}$ 应在 $\pm2$ 之内，几乎全部在 $\pm3$ 之内；$\lvert d_{ij}\rvert>3$ 的残差是潜在的**离群值**，应当加以调查（记录错误、有缺陷的试验，或真实但不寻常的响应）。实验设计与分析的教材把这些 $d_{ij}$ 称为标准化残差；它们与回归中内部的**标准化残差** $r_{ij}=e_{ij}/\sqrt{\mathrm{MS}_{\mathrm{E}}(1-h_{ij})}$ 仅相差因子 $\sqrt{1-1/n_i}$，因为杠杆值是 $h_{ij}=1/n_i$（下面的命题 5.1.1）。

对刻蚀数据，$\mathrm{MS}_{\mathrm{E}}=333.7$，$\sqrt{\mathrm{MS}_{\mathrm{E}}}=18.27$，最大的残差 $25.6$ 给出 $\max\lvert d_{ij}\rvert=1.40$：没有离群值。下图中的正态概率图接近一条直线。

独立性无法仅由残差检查，但残差对试验顺序（或对时间、操作员、位置以及其他任何可能起作用的变量）的图，揭示最常见的违反情形：相近时间进行的试验之间存在相关，或过程出现漂移。符号相同的残差成串、或出现趋势，表明存在相依。把试验顺序随机化是主要的保护措施：它不能消除漂移，但可以防止漂移与处理混杂，如 [3.8.2](/3.8.2) 所讨论的。对刻蚀数据，残差对试验顺序的图没有显示任何模式。

![刻蚀实验的残差诊断：残差对拟合值（四个水平均值）、尺度化残差的正态概率图、残差对试验顺序，以及按水平分组的尺度化残差，附界限正负 3](./plots/etch-diagnostics.py)

### 5.1.2. 方差齐性

**同方差性**的假定 $\sigma_1^2=\cdots=\sigma_a^2$ 首先用图来检查：在残差对拟合值（水平均值）的图中，各水平的垂直散布应大致相同。漏斗形，即散布随均值增大，是**异方差性**的典型标志。当响应有偏斜的分布、方差是均值的函数时（计数、失效时间、浓度），它常常出现；此时，用例如 Box–Cox 方法（[3.3.14](/3.3.14)）选取的稳定方差的变换，通常能同时消除这两个问题。

违反这一假定有多大影响？经验与模拟给出了清楚的图景。

- 在平衡的固定效应设计中，$F$ 检验只受到轻微的影响：它的实际显著性水平仍接近名义水平。这是**平衡设计**（[3.8.2](/3.8.2)）的主要优点之一。
- 在非平衡设计中，影响更严重，特别是当某个方差远大于其他方差时。如果较大的方差出现在较小的组中，检验变得过于宽松（错误拒绝太多）；如果出现在较大的组中，检验变得保守。
- 在随机效应模型（5.3 节）中，即使设计是平衡的，不等的误差方差也可能严重扰乱对方差分量的推断。

检验 $H_0\colon\sigma_1^2=\cdots=\sigma_a^2$ 对"至少一个方差不同"，有两个标准的形式检验；二者都已在 [3.3.5](/3.3.5) 中介绍过，这里用本章的记号给出它们的统计量。设 $S_i^2$ 是水平 $i$ 的样本方差，自由度为 $n_i-1$，$N=\sum_in_i$，而

$$
S_p^2=\frac{1}{N-a}\sum_{i=1}^a(n_i-1)S_i^2=\mathrm{MS}_{\mathrm{E}}
$$
是合并方差。

**Bartlett 检验**是对正态性下方差相等的**似然比检验**的一种修正，用来使 $\chi^2$ 分布的近似更好：

$$
T=\frac{(N-a)\ln S_p^2-\sum_{i=1}^a(n_i-1)\ln S_i^2}{c}\ \overset{H_0}{\approx}\ \chi^2_{a-1},\qquad c=1+\frac{1}{3(a-1)}\left(\sum_{i=1}^a\frac{1}{n_i-1}-\frac{1}{N-a}\right),
$$
当 $T>\chi^2_{a-1,\alpha}$ 时拒绝 $H_0$。分子比较的是 $S_i^2$ 的算术平均（权为 $w_i=(n_i-1)/(N-a)$）与它们的加权几何平均：令 $l=\prod_i(S_i^2)^{w_i}/\sum_iw_iS_i^2$，则分子是 $-(N-a)\ln l$，由 Jensen 不等式 $0<l\le1$，当且仅当所有 $S_i^2$ 相等时等号成立。所以样本方差分散时 $T$ 大。有两点要注意：该检验对非正态性非常敏感（即使方差相等，重尾也会使它膨胀），并且对小样本，$\chi^2$ 近似很差；通常的建议是 $\min_in_i\ge3$，且大多数 $n_i>5$。

**Levene 检验**对非正态性是稳健的。它把每个观测换成它与所在水平中心的绝对偏差 $Z_{ij}=\lvert y_{ij}-\bar y_{i\cdot}\rvert$，并对 $Z_{ij}$ 作单因素方差分析：

$$
T=\frac{N-a}{a-1}\cdot\frac{\sum_{i=1}^an_i(\bar Z_{i\cdot}-\bar Z_{\cdot\cdot})^2}{\sum_{i=1}^a\sum_{j=1}^{n_i}(Z_{ij}-\bar Z_{i\cdot})^2}\ \overset{H_0}{\approx}\ F_{a-1,N-a},
$$
当 $T>F_{a-1,N-a,\alpha}$ 时拒绝 $H_0$。如果方差相等，平均绝对偏差大致相等，$T$ 就小。**Brown–Forsythe 检验**（修正的 Levene 检验）使用各水平的中位数，$Z_{ij}=\lvert y_{ij}-\tilde y_{i}\rvert$，这使它对偏斜分布更加稳健；它是 R 中 `car::leveneTest` 的默认形式。

对刻蚀数据，两个检验一致表明没有方差不等的证据（样本方差为 $400.7$、$280.3$、$421.3$、$232.5$）：

```r
bartlett.test(rate ~ RF, data = etch.rate)
library(car)
leveneTest(etch.rate.aov)
```

```text
	Bartlett test of homogeneity of variances

data:  rate by RF
Bartlett's K-squared = 0.43349, df = 3, p-value = 0.9332

Levene's Test for Homogeneity of Variance (center = median)
      Df F value Pr(>F)
group  3  0.1959 0.8977
      16
```

在 Bartlett 的输出中，`K-squared` 是统计量 $T$，`df` $=a-1=3$。Levene 的输出是 $Z_{ij}$ 的方差分析表：行 `group` 的自由度为 $a-1=3$，没有标签的第二行是残差，$N-a=16$，而 `center = median` 表明这是 Brown–Forsythe 的版本。

### 5.1.3. Welch 方差分析

当方差明显不同时，一种办法是对响应作变换，另一种是加权方差分析（[3.3.14](/3.3.14)）。第三种是修改检验本身，正如 **Welch t 检验**修改合并的两样本 $t$ 检验那样（[3.2.5](/3.2.5)、[3.8.2](/3.8.2)）：每个水平均值按其估计的精度加权，自由度用 **Satterthwaite 近似**来近似。

**定义 5.1.2（Welch 方差分析）** 设 $\bar y_{i\cdot}$ 与 $s_i^2$ 是水平 $i$ 上 $n_i$ 个观测的均值与方差，并令

$$
w_i=\frac{n_i}{s_i^2},\qquad w=\sum_{i=1}^aw_i,\qquad \bar y'=\frac{\sum_iw_i\bar y_{i\cdot}}{w},\qquad \Lambda=\sum_{i=1}^a\frac{(1-w_i/w)^2}{n_i-1}.
$$
**Welch 方差分析**不假定方差相等，用

$$
F_0^*=\frac{\frac{1}{a-1}\sum_{i=1}^aw_i(\bar y_{i\cdot}-\bar y')^2}{1+\frac{2(a-2)}{a^2-1}\Lambda}\ \overset{H_0}{\approx}\ F_{a-1,\,\nu},\qquad \nu=\frac{a^2-1}{3\Lambda}
$$
检验 $H_0\colon\mu_1=\cdots=\mu_a$，当 $F_0^*>F_{a-1,\nu,\alpha}$ 时拒绝 $H_0$。

权 $w_i=n_i/s_i^2$ 是 $\bar y_{i\cdot}$ 的估计方差的倒数，所以精确的均值更重要，而 $\bar y'$ 是相应的加权总均值。分子是加权的处理均方；分母修正了估计的权的变异，而分母自由度 $\nu$ 不是整数，通常远小于 $N-a$。当 $a=2$ 时，统计量化为 Welch $t$ 统计量的平方，并有相同的 Welch–Satterthwaite 自由度。Welch 方差分析仍假定误差正态且独立；它在方差不等、样本量不等或较小时最有用，而这正是普通 $F$ 检验最不可靠的情形。

```r
oneway.test(rate ~ RF, data = etch.rate, var.equal = FALSE)
```

```text
	One-way analysis of means (not assuming equal variances)

data:  rate and RF
F = 68.719, num df = 3.0000, denom df = 8.8278, p-value = 1.913e-06
```

结论与普通 $F$ 检验一致（自由度为 3 与 16 的 $F_0=66.80$）：刻蚀数据的方差相近，所以权几乎不改变统计量，但不假定方差相等的代价体现在分母自由度上，是 $8.83$ 而不是 $16$。

既然 Welch 方差分析无论如何都保护了均值的检验，为什么还要检验方差是否不等？有几个理由。方差不等本身常常就是一个发现：改变过程变异性的处理，可能比改变其均值的处理更重要，这一点在 [3.8.2](/3.8.2) 中已就两个样本说过。方差不恒定也是一种症状：它可能表明响应是偏斜的、应当变换，也可能表明遗漏了某个因子，或存在离群值。而且稳健的检验只涵盖均值的整体检验；[3.8.4](/3.8.4) 的多重比较、5.3 节的方差分量估计以及 [3.8.6](/3.8.6) 的多因子分析，都没有同样简单的 Welch 版本，而是依赖共同方差的假定。

### 5.1.4. R 中的诊断图与杠杆值

在 R 中，对拟合的 `aov` 对象作 `plot`，画出四张诊断图：

```r
opar <- par(mfrow = c(2, 2), cex = .8)
plot(etch.rate.aov)
par(opar)
```

它们是残差对拟合值、标准化残差的正态 Q–Q 图、尺度–位置图（$\sqrt{\lvert r_{ij}\rvert}$ 对拟合值，用于发现散布的趋势），以及第四张图，对回归模型它显示标准化残差对**杠杆值**。对单因素模型，R 把最后一张换成残差对因子水平的图，并标注"Constant Leverage"。原因是下面的事实。

**命题 5.1.1** 在用最小二乘拟合的单因素模型中，观测 $y_{ij}$ 的杠杆值，即**帽子矩阵** $H$ 的对角元，是 $h_{ij}=1/n_i$。

**证明** 把观测按水平排序，使用均值模型 $\boldsymbol{Y}=X\boldsymbol{\mu}+\boldsymbol{\varepsilon}$，它的**设计矩阵** $X$ 对每个水平有一列水平的示性变量；效应模型有相同的列空间，因而有相同的 $H$。于是 $X^{\mathsf T}X=\operatorname{diag}(n_1,\dots,n_a)$，

$$
H=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}=\begin{bmatrix}\frac{1}{n_1}\boldsymbol{1}_{n_1}\boldsymbol{1}_{n_1}^{\mathsf T}&&\\&\ddots&\\&&\frac{1}{n_a}\boldsymbol{1}_{n_a}\boldsymbol{1}_{n_a}^{\mathsf T}\end{bmatrix},
$$
这是分块对角矩阵，第 $i$ 块对水平 $i$ 的观测取平均；确实，$H\boldsymbol{y}$ 把每个 $y_{ij}$ 换成 $\bar y_{i\cdot}$。它的对角元是 $1/n_i$。$\square$

因此在平衡设计中，所有观测有相同的杠杆值 $1/n$，残差对杠杆值的图退化为一条竖直的带。这标志着方差分析与回归在诊断上的真实差别。在对连续预测变量的回归中，各观测的杠杆值差别很大，预测变量空间中远离的一个点就能决定拟合，所以杠杆值与影响度量是核心。在单因素方差分析中，没有哪个设计点比另一个更偏远，一个水平的拟合值就是它自己的观测值的均值，离群值只能扭曲它自己所在水平的均值与合并方差。因此诊断的精力集中在每个组的方差、响应的正态性与离群值，以及独立性；而当设计非平衡时，观测少的水平有较大的杠杆值。

## 5.2. 功效与样本量

在实验进行之前，应该决定需要多少次重复。太少，处理之间的真实差异可能被漏掉；太多，则浪费资源。对单因素 $F$ 检验，问题是：给定显著性水平 $\alpha$、误差标准差 $\sigma$ 以及我们希望检出的一种处理均值的配置，每个水平取多大的 $n$，才使检验有规定的**功效** $1-\beta$？回答它需要 $H_0$ 为假时 $F_0$ 的分布。

### 5.2.1. 非中心 F 分布

**定义 5.2.1（非中心卡方分布）** 设 $X_1,\dots,X_\nu$ 独立，$X_k\sim\mathcal{N}(\delta_k,1)$。$\sum_{k=1}^\nu X_k^2$ 的分布只依赖于 $\nu$ 与 $\lambda=\sum_k\delta_k^2$；它称为自由度为 $\nu$、非中心参数为 $\lambda$ 的**非中心卡方分布** $\chi^2_\nu(\lambda)$。它的均值是 $\nu+\lambda$，而 $\chi^2_\nu(0)$ 就是通常的**卡方分布**。

**定义 5.2.2（非中心 F 分布）** 若 $U\sim\chi^2_{\nu_1}(\lambda)$ 与 $V\sim\chi^2_{\nu_2}$ 独立，则 $(U/\nu_1)/(V/\nu_2)$ 的分布是**非中心 F 分布** $F_{\nu_1,\nu_2}(\lambda)$；当 $\lambda=0$ 时，它是中心 **F 分布**。

它们是用于 $t$ 检验功效的**非中心 t 分布**（[3.3.3](/3.3.3)、[3.8.2](/3.8.2)）的类似物。**非中心参数** $\lambda$ 越大，分布越向右移动，统计量超过固定临界值的可能性就越大。

**定理 5.2.1** 在每个水平有 $n$ 个观测的平衡单因素固定效应模型中，

$$
\frac{\mathrm{SS}_{\mathrm{Tr}}}{\sigma^2}\sim\chi^2_{a-1}(\lambda),\qquad \frac{\mathrm{SS}_{\mathrm{E}}}{\sigma^2}\sim\chi^2_{N-a},\qquad F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\sim F_{a-1,N-a}(\lambda),\qquad \lambda=\frac{n\sum_{i=1}^a\tau_i^2}{\sigma^2},
$$
其中 $\mathrm{SS}_{\mathrm{Tr}}$ 与 $\mathrm{SS}_{\mathrm{E}}$ 独立。在 $H_0$ 下（$\lambda=0$），这些分布是中心的。

**证明** 向量 $\sqrt n(\bar Y_{1\cdot},\dots,\bar Y_{a\cdot})/\sigma$ 服从 $\mathcal{N}_a(\sqrt n\boldsymbol{\mu}/\sigma,I_a)$，而 $\mathrm{SS}_{\mathrm{Tr}}/\sigma^2=\lVert P\sqrt n\bar{\boldsymbol{Y}}/\sigma\rVert^2$，其中 $P=I_a-\frac1a\boldsymbol{1}\boldsymbol{1}^{\mathsf T}$ 是秩为 $a-1$ 的投影。旋转到 $P$ 的值域的标准正交基，得到 $a-1$ 个独立的单位方差正态变量的平方和，其均值平方之和为 $\lVert P\sqrt n\boldsymbol{\mu}\rVert^2/\sigma^2=n\sum_i(\mu_i-\bar\mu)^2/\sigma^2=n\sum_i\tau_i^2/\sigma^2$。$\mathrm{SS}_{\mathrm{E}}$ 的分布与独立性同 $H_0$ 下相同（[3.8.3](/3.8.3)），因为 $\mathrm{SS}_{\mathrm{E}}$ 不涉及各均值。$\square$

因此水平为 $\alpha$ 的检验的功效是

$$
1-\beta=\mathbb{P}\big(F_{a-1,N-a}(\lambda)>F_{a-1,N-a,\alpha}\big),
$$
它是 $\lambda$ 的增函数，而 $\lambda$ 又随 $n$ 与 $\sum_i\tau_i^2/\sigma^2$（以误差方差为单位度量的真实均值的散布）线性增长。要确定样本量，就增大 $n$，直到该概率达到 $1-\beta$。在有计算机之前，功效是从 OC 图上读出的：每条 **OC 曲线**（[3.8.2](/3.8.2)）对给定的分子与分母自由度，画出 $\beta$ 对参数

$$
\Phi=\sqrt{\frac{n\sum_{i=1}^a\tau_i^2}{a\sigma^2}}=\sqrt{\lambda/a}
$$
的曲线；由于 $\Phi$ 本身含有 $n$，这些图要迭代使用。今天直接计算这个概率（R 中是 `pf(q, df1, df2, ncp, lower.tail = FALSE)`）。

### 5.2.2. 刻蚀实验的样本量

设实验者想检出配置 $\mu_1=575$、$\mu_2=600$、$\mu_3=650$、$\mu_4=675$ Å/min，$\sigma=25$ Å/min，水平 $\alpha=0.01$，功效 $0.90$。效应为 $\tau_i=\mu_i-625=-50,-25,25,50$，所以 $\sum\tau_i^2=6250$，$\lambda=6250n/625=10n$。

```r
true.means <- c(575, 600, 650, 675); sd <- 25
power.anova.test(groups = 4, between.var = var(true.means),
                 within.var = sd^2, sig.level = .01, power = .90)
```

```text
     Balanced one-way analysis of variance power calculation 

         groups = 4
              n = 3.520243
    between.var = 2083.333
     within.var = 625
      sig.level = 0.01
          power = 0.9

NOTE: n is number in each group
```

参数 `between.var` 是均值的样本方差，$\sum_i(\mu_i-\bar\mu)^2/(a-1)=6250/3=2083.33$，除数是 $a-1$ 而不是 $a$；R 内部用 $\lambda=(a-1)\,n\cdot\text{between.var}/\text{within.var}$，这与 $\lambda=n\sum\tau_i^2/\sigma^2$ 相同。如果给出除数为 $a$ 的方差，就会低估效应。解 $n=3.52$ 不是整数，必须向上取整：每个水平取 $n=4$ 片晶圆时功效为 $0.962$（取 $n=3$ 则只有 $0.753$）。

实验者常常无法给定全部均值，只能给出值得检出的最大与最小均值之间的最小差 $\Delta=\max_i\mu_i-\min_i\mu_i$。功效只通过 $\sum\tau_i^2$ 依赖于均值，对极差为 $\Delta$ 的每种配置的保证，由最不利的配置得到。

**命题 5.2.1** 在所有满足 $\max_i\mu_i-\min_i\mu_i=\Delta$ 的均值 $\mu_1,\dots,\mu_a$ 中，

$$
\min\sum_{i=1}^a\tau_i^2=\min\sum_{i=1}^a(\mu_i-\bar\mu)^2=\frac{\Delta^2}{2},
$$
当一个均值为 $\bar\mu+\Delta/2$、一个为 $\bar\mu-\Delta/2$、其余都等于 $\bar\mu$ 时取到。

**证明** 设 $u=\max_i\mu_i$，$v=\min_i\mu_i$。去掉其他项，$\sum_i(\mu_i-\bar\mu)^2\ge(u-\bar\mu)^2+(v-\bar\mu)^2$。对任何实数 $c$，$(u-c)^2+(v-c)^2=\frac{(u-v)^2}{2}+2\big(c-\frac{u+v}{2}\big)^2\ge\frac{\Delta^2}{2}$。当其余均值等于 $\bar\mu$ 且 $\bar\mu=(u+v)/2$ 时，两步都取等号，这是自洽的：均值 $\bar\mu\pm\Delta/2$ 与 $a-2$ 个 $\bar\mu$ 的平均确实是 $\bar\mu$。$\square$

所以按 $\sum\tau_i^2=\Delta^2/2$ 计算的样本量，保证只要真实均值的极差至少为 $\Delta$，功效就至少是 $1-\beta$。对 $\Delta=75$ 的刻蚀问题，$\sum\tau_i^2=2812.5$（Minitab 报告的"SS Means"），$\lambda=4.5n$。当 $\alpha=0.01$、$\sigma=25$ 时，$n=5$ 的功效是 $0.805$，$n=6$ 的是 $0.915$，所以每个水平需要六片晶圆：比上面求得的四片更多，因为最不利的配置使均值散布得更少。

![左：F 检验的功效对每个水平的重复数的曲线，针对指定的均值与极差为 75 的最不利配置，alpha 取 0.05 与 0.01。右：n = 4 时自由度为 3 与 12 的中心与非中心 F 密度，附 alpha 为 0.01 的临界值；阴影面积是功效](./plots/anova-power.py)

## 5.3. 单因素随机效应模型

### 5.3.1. 固定因子与随机因子

到目前为止，因子的 $a$ 个水平是有意选定的，并且是仅有的感兴趣的水平：四个具体的 RF 功率设置。结论针对这些水平及其均值。

**定义 5.3.1（固定效应模型）** 单因素**固定效应模型**是

$$
Y_{ij}=\mu+\tau_i+\varepsilon_{ij},\qquad i=1,\dots,a,\quad j=1,\dots,n_i,\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
其中 $\mu$ 与处理效应 $\tau_1,\dots,\tau_a$ 是未知的常数，受 $\sum_i\tau_i=0$ 之类的约束。无处理效应的假设是 $H_0\colon\tau_1=\cdots=\tau_a=0$，推断只适用于这 $a$ 个水平。

现在考虑一种不同的情形。一家纺织公司在大量织机上织一种织物，织机应当是同质的，使织物的强度均匀。过程工程师怀疑，除了同一织机上样品强度的通常变异之外，织机之间可能还有显著的变异。为了研究这一点，她随机选了四台织机，在每台织机的织物上各作四次强度测定：

| 织机 | 观测值 | $y_{i\cdot}$ | $\bar y_{i\cdot}$ |
|---|---|---|---|
| 1 | 98, 97, 99, 96 | 390 | 97.50 |
| 2 | 91, 90, 93, 92 | 366 | 91.50 |
| 3 | 96, 95, 97, 95 | 383 | 95.75 |
| 4 | 95, 96, 99, 98 | 388 | 97.00 |
| | | $y_{\cdot\cdot}=1527$ | $\bar y_{\cdot\cdot}=95.44$ |

这四台织机本身并不令人感兴趣；它们代表工厂里织机的全体，问题是该总体中的织机变异有多大。

**定义 5.3.2（固定因子与随机因子）** 如果因子的水平是有意选定的，且结论只涉及这些水平，则它是**固定因子**。如果它在实验中的水平是从更大的可能水平的总体中随机抽取的样本，且结论要推广到该总体，则它是**随机因子**。

**定义 5.3.3（随机效应模型）** 单因素**随机效应模型**是

$$
Y_{ij}=\mu+\tau_i+\varepsilon_{ij},\qquad i=1,\dots,a,\quad j=1,\dots,n,
$$
其中 $\mu$ 是常数（总均值），$\tau_i\sim\mathcal{N}(0,\sigma_\tau^2)$ 是第 $i$ 个水平的随机效应，$\varepsilon_{ij}\sim\mathcal{N}(0,\sigma^2)$ 是实验误差，所有 $\tau_i$ 与 $\varepsilon_{ij}$ 相互独立。方差 $\sigma_\tau^2$ 与 $\sigma^2$ 分别称为处理间与处理内的**方差分量**。

这个模型看起来与固定效应模型一样，方差分析表的算术也相同；不同的是 $\tau_i$ 的含义。这里 $\tau_i$ 是随机变量，而不是参数：参数是 $\mu$、$\sigma_\tau^2$ 与 $\sigma^2$，无论抽取多少个水平都只是三个数。没有约束 $\sum_i\tau_i=0$，因为四个随机效应的样本之和不为零。由于 $\operatorname{Var}(Y_{ij})=\sigma_\tau^2+\sigma^2$，观测的总方差分解为由水平引起的部分与由误差引起的部分，所以这种分析也称为方差分量分析。

**定义 5.3.4（组内相关系数）** 在随机效应模型中，**组内相关系数**为

$$
\rho_I=\frac{\sigma_\tau^2}{\sigma_\tau^2+\sigma^2},
$$
即观测的方差中由水平之间的变异引起的比例。它等于同一水平上两个观测之间的相关系数（5.3.2 节）。

组内相关系数接近 $1$，意味着同一水平上的观测几乎相同，各水平差别很大；接近 $0$，则与水平内的噪声相比，水平几乎无关紧要。在织机的例子中，$\rho_I$ 度量使织机一致可以消除织物强度变异的多大一部分。

### 5.3.2. 观测的协方差结构

在固定效应模型中，观测独立，协方差矩阵为 $\sigma^2I_N$。在随机效应模型中它们并不独立。对同一水平 $i$ 上的两个观测，$j\ne j'$，

$$
\operatorname{Cov}(Y_{ij},Y_{ij'})=\operatorname{Cov}(\tau_i+\varepsilon_{ij},\tau_i+\varepsilon_{ij'})=\operatorname{Var}(\tau_i)=\sigma_\tau^2,
$$
而不同水平上的观测没有共同的随机项，是不相关的。因此

$$
\operatorname{Var}(Y_{ij})=\sigma_\tau^2+\sigma^2,\qquad \operatorname{Corr}(Y_{ij},Y_{ij'})=\frac{\sigma_\tau^2}{\sigma_\tau^2+\sigma^2}=\rho_I\quad(j\ne j'),\qquad \operatorname{Cov}(Y_{ij},Y_{i'j'})=0\quad(i\ne i').
$$
把观测按水平逐个叠起来，$\boldsymbol{Y}$ 服从**多元正态分布** $\mathcal{N}_N(\mu\boldsymbol{1}_N,\Sigma)$，协方差矩阵为分块对角矩阵

$$
\Sigma=\begin{bmatrix}\Sigma_0&&\\&\ddots&\\&&\Sigma_0\end{bmatrix}=I_a\otimes\Sigma_0,\qquad \Sigma_0=\sigma^2I_n+\sigma_\tau^2\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T}=\begin{bmatrix}\sigma_\tau^2+\sigma^2&\sigma_\tau^2&\cdots&\sigma_\tau^2\\ \sigma_\tau^2&\sigma_\tau^2+\sigma^2&\cdots&\sigma_\tau^2\\ \vdots&&\ddots&\vdots\\ \sigma_\tau^2&\sigma_\tau^2&\cdots&\sigma_\tau^2+\sigma^2\end{bmatrix}.
$$
每个块的对角线上方差相等，对角线之外协方差相等（复合对称）。所以随机效应模型中的观测不是独立的：它们在一个水平内可交换，在不同水平之间独立。只有在特殊情形 $\sigma_\tau^2=0$ 下才有独立性。同样的结构在对同一被试的重复测量以及整群抽样中再次出现。

### 5.3.3. $\sigma_\tau^2=0$ 的检验

在固定效应模型中，我们检验各个特定的处理均值是否相等。对于随机因子，感兴趣的是水平的总体，自然的假设是

$$
H_0\colon\sigma_\tau^2=0\qquad\text{对}\qquad H_1\colon\sigma_\tau^2>0.
$$
若 $\sigma_\tau^2=0$，则所有随机效应以概率一为 $0$，水平之间没有变异。方差分析恒等式 $\mathrm{SS}_{\mathrm{T}}=\mathrm{SS}_{\mathrm{Tr}}+\mathrm{SS}_{\mathrm{E}}$ 纯粹是代数的，仍然成立；改变的是期望均方。

**定理 5.3.1（随机效应模型中的期望均方）** 在平衡的单因素随机效应模型中，

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+n\sigma_\tau^2,\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2.
$$
此外 $\mathrm{SS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{N-a}$，$\mathrm{SS}_{\mathrm{Tr}}/(\sigma^2+n\sigma_\tau^2)\sim\chi^2_{a-1}$，且二者独立。

**证明** 在水平 $i$ 内，$Y_{ij}-\bar Y_{i\cdot}=\varepsilon_{ij}-\bar\varepsilon_{i\cdot}$ 不含 $\tau_i$，所以 $\mathrm{SS}_{\mathrm{E}}$ 是与固定效应模型中相同的误差函数，$\mathrm{SS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{N-a}$。对处理平方和，记 $U_i=\bar Y_{i\cdot}=\mu+\tau_i+\bar\varepsilon_{i\cdot}$。各 $U_i$ 独立同服从 $\mathcal{N}(\mu,\sigma_\tau^2+\sigma^2/n)$，并且

$$
\mathrm{SS}_{\mathrm{Tr}}=n\sum_{i=1}^a(\bar Y_{i\cdot}-\bar Y_{\cdot\cdot})^2=n\sum_{i=1}^a(U_i-\bar U)^2 .
$$
由正态样本的样本方差理论，$\sum_i(U_i-\bar U)^2/(\sigma_\tau^2+\sigma^2/n)\sim\chi^2_{a-1}$；乘以 $n$ 即得关于 $\mathrm{SS}_{\mathrm{Tr}}/(\sigma^2+n\sigma_\tau^2)$ 的结论，特别地 $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=n(\sigma_\tau^2+\sigma^2/n)=\sigma^2+n\sigma_\tau^2$。最后，$\mathrm{SS}_{\mathrm{Tr}}$ 是水平均值 $\bar\varepsilon_{i\cdot}$ 与 $\tau_i$ 的函数，$\mathrm{SS}_{\mathrm{E}}$ 是偏差 $\varepsilon_{ij}-\bar\varepsilon_{i\cdot}$ 的函数，后者与 $\bar\varepsilon_{i\cdot}$（正态样本）及 $\tau_i$ 独立。$\square$

人们很容易想从 [3.8.3](/3.8.3) 的固定效应结果 $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+n\sum_i\tau_i^2/(a-1)$ 出发，先对 $\tau_i$ 取条件再取期望来得到定理 5.3.1，$\mathbb{E}\big[n\sum_i\tau_i^2/(a-1)\big]=na\sigma_\tau^2/(a-1)$。这给出错误的系数 $na/(a-1)$，而不是 $n$。毛病在于固定效应的公式用了约束 $\sum_i\tau_i=0$，而随机效应并不满足它。对 $\tau_i$ 取条件，正确地给出

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}\mid\tau_1,\dots,\tau_a]=\sigma^2+\frac{n}{a-1}\sum_{i=1}^a(\tau_i-\bar\tau)^2,
$$
由于 $\mathbb{E}\sum_i(\tau_i-\bar\tau)^2=(a-1)\sigma_\tau^2$，沿着**全方差公式**的路线，或者直接用迭代期望，就得到 $\sigma^2+n\sigma_\tau^2$。

在 $H_0$ 下两个均方都估计 $\sigma^2$；在 $H_1$ 下，处理均方更大。所以检验统计量与固定效应模型中相同，

$$
F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\ \overset{H_0}{\sim}\ F_{a-1,N-a},
$$
当 $F_0>F_{a-1,N-a,\alpha}$ 时拒绝 $H_0$。区别在于备择假设：由定理 5.3.1，一般地

$$
F_0\sim\frac{\sigma^2+n\sigma_\tau^2}{\sigma^2}\,F_{a-1,N-a},
$$
它是中心 $F$ 变量的倍数，而不是非中心 $F$。因此随机效应检验的功效是 $\mathbb{P}\big(F_{a-1,N-a}>F_{a-1,N-a,\alpha}/(1+n\sigma_\tau^2/\sigma^2)\big)$，由中心 $F$ 分布算出。

对于水平 $i$ 有 $n_i$ 个观测的非平衡设计，仍然有 $\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2$，而 $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+n_0\sigma_\tau^2$，其中 $n_0=\big(N-\sum_in_i^2/N\big)/(a-1)$，当所有 $n_i=n$ 时它等于 $n$；但此时 $\mathrm{SS}_{\mathrm{Tr}}$ 不再是缩放的 $\chi^2$ 变量，本节的精确结果只近似成立。

### 5.3.4. 估计方差分量

最简单的估计令观测到的均方等于其期望并求解：

$$
\hat\sigma^2=\mathrm{MS}_{\mathrm{E}},\qquad \hat\sigma_\tau^2=\frac{\mathrm{MS}_{\mathrm{Tr}}-\mathrm{MS}_{\mathrm{E}}}{n}.
$$
这就是方差分析法。这些估计量是无偏的，除矩之外不需要任何分布假定，在平衡设计中，它们是正态性下方差最小的无偏二次估计量。组内相关系数用 $\hat\rho_I=\hat\sigma_\tau^2/(\hat\sigma_\tau^2+\hat\sigma^2)$ 估计。

这个方法有一个弱点：只要 $\mathrm{MS}_{\mathrm{Tr}}<\mathrm{MS}_{\mathrm{E}}$，即 $F_0<1$，$\hat\sigma_\tau^2$ 就是负的；当 $\sigma_\tau^2$ 很小时，这有不小的概率发生（在 $H_0$ 下概率为 $\mathbb{P}(F_{a-1,N-a}<1)$，常在一半左右）。方差不可能为负。通常的对策有：

- 取 $\hat\sigma_\tau^2=0$，接受一个有偏的估计量；$F_0<1$ 与 $H_0\colon\sigma_\tau^2=0$ 是相容的；
- 采用尊重参数空间的估计方法，例如限制极大似然（5.3.5 节），它给出非负的估计；
- 把绝对值较大的负估计看作反对模型的证据：误差在水平内可能以模型没有描述的方式相关（例如测量过程引起的负相关），或者各水平的方差可能不同。

### 5.3.5. 例：R 中的纤维强度数据

织机数据的方差分析：

```r
summary(aov(Obs ~ Loom, data = LoomData))
```

```text
            Df Sum Sq Mean Sq F value   Pr(>F)    
Loom         3  89.19  29.729   15.68 0.000188 ***
Residuals   12  22.75   1.896                     
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

每一项含义照旧：$\mathrm{SS}_{\mathrm{Tr}}=4\sum_i(\bar y_{i\cdot}-95.4375)^2=89.19$，自由度 $a-1=3$，$\mathrm{SS}_{\mathrm{E}}=22.75$，自由度 $N-a=12$，均方 $29.729$ 与 $1.896$，$F_0=29.729/1.896=15.68$，$p$ 值 $\mathbb{P}(F_{3,12}>15.68)=0.000188$。解释变了：我们拒绝 $H_0\colon\sigma_\tau^2=0$，并得出结论：工厂里的织机（不只是这四台）在强度上有显著差异。方差分量为

$$
\hat\sigma^2=1.896,\qquad \hat\sigma_\tau^2=\frac{29.729-1.896}{4}=6.958,\qquad \hat\sigma_y^2=\hat\sigma_\tau^2+\hat\sigma^2=8.854,\qquad \hat\rho_I=\frac{6.958}{8.854}=0.786 .
$$
织物强度方差的约 $79\%$ 可归因于织机之间的差异：过程工程师应当寻找织机间变异的原因（调试、维护、操作员培训），因为减小它会使织物均匀得多。

同样的数据可以拟合为以织机为因子的回归：

```r
summary(lm(Obs ~ Loom, data = LoomData))
```

```text
Call:
lm(formula = Obs ~ Loom, data = LoomData)

Residuals:
    Min      1Q  Median      3Q     Max 
-2.0000 -0.8125 -0.1250  1.0625  2.0000 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  97.5000     0.6884 141.623  < 2e-16 ***
Loom2        -6.0000     0.9736  -6.163 4.85e-05 ***
Loom3        -1.7500     0.9736  -1.797   0.0975 .  
Loom4        -0.5000     0.9736  -0.514   0.6169    

Residual standard error: 1.377 on 12 degrees of freedom
Multiple R-squared:  0.7968,	Adjusted R-squared:  0.746 
F-statistic: 15.68 on 3 and 12 DF,  p-value: 0.0001878
```

这是 R 默认的处理对照编码（[3.8.3](/3.8.3)）下的固定效应分析：截距 $97.5$ 是织机 1，即基线的均值，系数 `Loom2`、`Loom3`、`Loom4` 是差 $\bar y_{i\cdot}-\bar y_{1\cdot}$，即 $91.5-97.5=-6$、$-1.75$ 与 $-0.5$。标准误对水平均值是 $\sqrt{\mathrm{MS}_{\mathrm{E}}/n}=\sqrt{1.896/4}=0.6884$，对两个均值之差是 $\sqrt{2\,\mathrm{MS}_{\mathrm{E}}/n}=0.9736$。残差标准误是 $\sqrt{\mathrm{MS}_{\mathrm{E}}}=1.377$，自由度 12，$R^2=\mathrm{SS}_{\mathrm{Tr}}/\mathrm{SS}_{\mathrm{T}}=89.19/111.94=0.797$，而自由度为 3 与 12 的整体 $F$ 统计量 $15.68$ 就是方差分析的 $F_0$。这些数字描述的是这四台特定的织机；对随机因子，个别的系数没有长久的意义，但 $F$ 检验是一样的。

随机效应模型用 `lme4` 包的函数 `lmer` 拟合，其中 `(1 | Loom)` 声明对分组因子 `Loom` 的每个水平有一个随机截距：

```r
library(lme4)
summary(lmer(Obs ~ (1 | Loom), data = LoomData))
```

```text
Linear mixed model fit by REML ['lmerMod']
Formula: Obs ~ 1 + (1 | Loom)
   Data: LoomData

REML criterion at convergence: 63.2

Scaled residuals: 
     Min       1Q   Median       3Q      Max 
-1.38018 -0.57260 -0.04342  0.82574  1.52491 

Random effects:
 Groups   Name        Variance Std.Dev.
 Loom     (Intercept) 6.958    2.638   
 Residual             1.896    1.377   
Number of obs: 16, groups:  Loom, 4

Fixed effects:
            Estimate Std. Error t value
(Intercept)   95.438      1.363   70.01
```

`lmer` 不使用方差分析法；它最大化限制似然。

**定义 5.3.5（限制极大似然）** 对线性模型 $\boldsymbol{Y}\sim\mathcal{N}_N(X\boldsymbol{\beta},\Sigma(\boldsymbol{\theta}))$，其协方差矩阵依赖于方差参数 $\boldsymbol{\theta}$，且 $X$ 的秩为 $p$，$\boldsymbol{\theta}$ 的**限制极大似然**（REML）估计最大化 $N-p$ 个线性无关的误差对照 $K^{\mathsf T}\boldsymbol{Y}$（$K^{\mathsf T}X=O$）的似然，其分布不涉及 $\boldsymbol{\beta}$。差一个常数，这个限制对数似然的 $-2$ 倍是

$$
\ln\det\Sigma+\ln\det(X^{\mathsf T}\Sigma^{-1}X)+(\boldsymbol{y}-X\hat{\boldsymbol{\beta}})^{\mathsf T}\Sigma^{-1}(\boldsymbol{y}-X\hat{\boldsymbol{\beta}}),\qquad \hat{\boldsymbol{\beta}}=(X^{\mathsf T}\Sigma^{-1}X)^{-1}X^{\mathsf T}\Sigma^{-1}\boldsymbol{y}.
$$

方差分量的普通**极大似然估计**向下有偏，因为它忽略了估计固定效应所用掉的自由度；最简单的情形是正态方差的估计量 $\frac1N\sum(y_i-\bar y)^2$，它的 REML 对应物是无偏的 $\frac{1}{N-1}\sum(y_i-\bar y)^2$。REML 通过使用对照消除了这种偏差。在平衡的单因素设计中，只要方差分析的估计非负，REML 估计就与之重合；当 $\mathrm{MS}_{\mathrm{Tr}}<\mathrm{MS}_{\mathrm{E}}$ 时，REML 取 $\hat\sigma_\tau^2=0$。对非平衡数据，两种方法不同，REML 是标准的选择。

输出的读法如下。

- `REML criterion at convergence: 63.2` 是最大化的限制对数似然的 $-2$ 倍（包括常数 $(N-p)\ln 2\pi$）；它用来比较有相同固定效应的模型。
- `Scaled residuals` 是残差 $y_{ij}-\hat\mu-\tilde\tau_i$ 除以 $\hat\sigma$，其中 $\tilde\tau_i=\frac{n\hat\sigma_\tau^2}{n\hat\sigma_\tau^2+\hat\sigma^2}(\bar y_{i\cdot}-\bar y_{\cdot\cdot})$ 是随机效应的预测值。这些预测值把织机均值的偏差按因子 $27.83/29.73=0.936$ 向总均值收缩，所以这些残差与固定效应的残差 $y_{ij}-\bar y_{i\cdot}$ 略有不同。
- `Random effects` 列出两个方差分量及其平方根：织机截距的 $\hat\sigma_\tau^2=6.958$（$\hat\sigma_\tau=2.638$）与残差的 $\hat\sigma^2=1.896$（$\hat\sigma=1.377$），它们与方差分析的估计相同，因为设计是平衡的且 $\hat\sigma_\tau^2>0$。`Number of obs: 16, groups: Loom, 4` 给出 $N$ 与 $a$。
- `Fixed effects`：唯一的固定参数是 $\mu$，由总均值 $95.4375$ 估计（舍入为 $95.438$）；可以由 `lm` 的系数验算为 $97.5+(-6-1.75-0.5)/4=95.4375$。不打印 $p$ 值，因为在一般的混合模型中，$t$ 值的零分布并不恰好是 $t$ 分布。

截距的标准误 $1.363$ 由 5.3.2 节的协方差结构算出。对全部观测取平均，

$$
\operatorname{Var}(\bar Y_{\cdot\cdot})=\operatorname{Var}\Big(\mu+\bar\tau+\bar\varepsilon_{\cdot\cdot}\Big)=\frac{\sigma_\tau^2}{a}+\frac{\sigma^2}{an}=\frac{\sigma^2+n\sigma_\tau^2}{N},
$$
它的估计是 $\hat\sigma_\tau^2/a+\hat\sigma^2/(an)=\mathrm{MS}_{\mathrm{Tr}}/N$：

```r
sqrt(6.958/4 + 1.896/16)    # 1.363; equivalently sqrt(29.729/16)
```

这是 `lm` 的截距的标准误 $0.6884$ 的两倍，这个比较显示了两个模型的本质区别。在固定效应模型中，唯一的不确定性是测量误差，16 个观测把它平均掉了。在随机效应模型中，目标是工厂里所有织机的平均强度，而只抽样了四台织机：无论在每台织机上测量多少次，织机间的方差 $\sigma_\tau^2$ 都只在 $a=4$ 个水平上平均。增加每台织机上的重复只减小第二项；要精确地估计 $\mu$，必须抽样更多的织机。

![四台随机选取的织机上的纤维强度：观测值、各织机的均值、总均值及其正负估计的织机间标准差的带，以及各织机均值周围正负估计的织机内标准差](./plots/loom-random-effects.py)

### 5.3.6. 方差分量的置信区间

定理 5.3.1 的分布结果给出置信区间。

误差方差有精确的区间：由于 $(N-a)\mathrm{MS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{N-a}$，

$$
\frac{(N-a)\mathrm{MS}_{\mathrm{E}}}{\chi^2_{N-a,\alpha/2}}\le\sigma^2\le\frac{(N-a)\mathrm{MS}_{\mathrm{E}}}{\chi^2_{N-a,1-\alpha/2}} .
$$
对织机，$\chi^2_{12,0.025}=23.34$ 与 $\chi^2_{12,0.975}=4.404$ 给出 $0.975\le\sigma^2\le5.166$。

对 $\sigma_\tau^2$ 没有精确的区间，因为 $\hat\sigma_\tau^2$ 是两个独立的缩放 $\chi^2$ 变量之差，

$$
\hat\sigma_\tau^2=\frac{\mathrm{MS}_{\mathrm{Tr}}-\mathrm{MS}_{\mathrm{E}}}{n}\sim\frac{\sigma^2+n\sigma_\tau^2}{n(a-1)}\chi^2_{a-1}-\frac{\sigma^2}{n(N-a)}\chi^2_{N-a},
$$
其分布依赖于未知的分量之比。**Satterthwaite 近似**（[3.8.2](/3.8.2)）把它当作缩放的 $\chi^2$ 变量，$r\hat\sigma_\tau^2/\sigma_\tau^2\overset{\cdot}{\sim}\chi^2_r$，自由度用矩方法匹配：

$$
r=\frac{(\mathrm{MS}_{\mathrm{Tr}}-\mathrm{MS}_{\mathrm{E}})^2}{\mathrm{MS}_{\mathrm{Tr}}^2/(a-1)+\mathrm{MS}_{\mathrm{E}}^2/(N-a)},\qquad \frac{r\hat\sigma_\tau^2}{\chi^2_{r,\alpha/2}}\le\sigma_\tau^2\le\frac{r\hat\sigma_\tau^2}{\chi^2_{r,1-\alpha/2}} .
$$
对织机，$r=2.63$，近似的 95% 区间是 $2.12\le\sigma_\tau^2\le130$：只有四台织机时，织机间方差被确定得很差，尽管它的存在已被 $F$ 检验清楚地确立。当 $r$ 较小时，这种近似很粗糙；REML 的轮廓似然区间（对 `lmer` 拟合用 `confint`）或 Bayes 区间（[3.7.6](/3.7.6)）是可选的替代。

分量之比则有精确的区间。由定理 5.3.1，

$$
\frac{\mathrm{MS}_{\mathrm{Tr}}/(\sigma^2+n\sigma_\tau^2)}{\mathrm{MS}_{\mathrm{E}}/\sigma^2}\sim F_{a-1,N-a},
$$
所以以概率 $1-\alpha$，

$$
F_{a-1,N-a,1-\alpha/2}\le\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\cdot\frac{\sigma^2}{\sigma^2+n\sigma_\tau^2}\le F_{a-1,N-a,\alpha/2}.
$$
对 $\sigma_\tau^2/\sigma^2$ 求解，得区间 $[L,U]$，

$$
L=\frac1n\left(\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\cdot\frac{1}{F_{a-1,N-a,\alpha/2}}-1\right),\qquad U=\frac1n\left(\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\cdot\frac{1}{F_{a-1,N-a,1-\alpha/2}}-1\right),
$$
其中较低的分位数可以算作 $F_{a-1,N-a,1-\alpha/2}=1/F_{N-a,a-1,\alpha/2}$。由于 $\rho_I=\frac{\sigma_\tau^2/\sigma^2}{1+\sigma_\tau^2/\sigma^2}$ 是该比值的增函数，

$$
\frac{L}{1+L}\le\frac{\sigma_\tau^2}{\sigma_\tau^2+\sigma^2}\le\frac{U}{1+U}
$$
是组内相关系数的精确 $1-\alpha$ 区间（负的 $L$ 换成 $0$）。对织机，$F_0=15.68$，$F_{3,12,0.025}=4.474$，$F_{3,12,0.975}=0.0698$，所以 $L=0.626$，$U=55.95$，$0.385\le\rho_I\le0.982$。即使在下限，方差的三分之一以上也来自织机。

### 5.3.7. 固定还是随机？

一个因子应当处理成固定的还是随机的，与变量本身关系不大，而与研究问题关系很大。固定效应是其对响应的效应本身就是研究对象的因子：我们想要的是关于这些特定水平如何影响 $Y$ 的结论。随机效应通常是我们需要考虑、但其个别水平并不令人感兴趣的分组因子（织机、批次、实验室、被试、田地）；数据中的水平是一个样本，结果要推广到抽取它们的水平总体，这要求样本有代表性。

**例 5.3.1** 实验室检测某种疾病的准确度如何，各实验室的准确度是否有差异？在 3 个实验室检测不同的人；因子是实验室（$i=1,2,3$），实验单位是接受检测的人，$y_{ij}$ 是实验室 $i$ 对人 $j$ 的检测准确度评分。如果我们只关心这 3 个实验室（例如为了决定医院应与其中哪个签约），实验室是固定效应。如果这 3 个实验室是所有此类实验室的随机样本，而我们关心一般的实验室（准确度在实验室之间变化多大？），则它是随机效应。

| | 固定效应模型 | 随机效应模型 |
|---|---|---|
| 水平 | 有意选定；仅有的感兴趣的水平 | 取自水平总体的随机样本 |
| $\tau_i$ | 未知常数 | 随机变量，$\tau_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma_\tau^2)$，与误差独立 |
| 参数 | $\mu,\tau_1,\dots,\tau_a,\sigma^2$（$a+1$ 个自由参数） | $\mu,\sigma_\tau^2,\sigma^2$（3 个，与 $a$ 无关） |
| 约束 | $\sum_i\tau_i=0$（或基线） | 无 |
| $\mathbb{E}[Y_{ij}]$，$\operatorname{Var}(Y_{ij})$ | $\mu+\tau_i$，$\sigma^2$ | $\mu$，$\sigma_\tau^2+\sigma^2$ |
| $\operatorname{Cov}(\boldsymbol{Y})$ | $\sigma^2I_N$：观测独立 | $I_a\otimes(\sigma^2I_n+\sigma_\tau^2\boldsymbol{1}_n\boldsymbol{1}_n^{\mathsf T})$：水平内相关 |
| $H_0$ | $\tau_1=\cdots=\tau_a=0$ | $\sigma_\tau^2=0$ |
| $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]$ | $\sigma^2+n\sum_i\tau_i^2/(a-1)$ | $\sigma^2+n\sigma_\tau^2$ |
| $H_1$ 下的 $F_0$ | 非中心 $F_{a-1,N-a}(\lambda)$ | $(1+n\sigma_\tau^2/\sigma^2)\,F_{a-1,N-a}$ |
| 估计目标 | 处理均值、对照、多重比较 | 方差分量、$\rho_I$、总体均值 $\mu$ |
| 结论的范围 | 这 $a$ 个水平 | 整个水平总体 |

:::

随机效应模型是**分层模型**（[3.7.6](/3.7.6)）的频率学派对应：在分层模型中，组效应被赋予一个共同的先验分布，其参数被估计或赋予超先验，而组效应的后验均值向总均值收缩，正如 `lmer` 的随机效应预测值 $\tilde\tau_i$ 那样。既有固定因子又有随机因子的模型，即混合模型，将在后面关于分区组与多因子设计的章节中出现。

## 5.4. 定量因子的回归方法

### 5.4.1. 定量因子与定性因子

**定义 5.4.1（定量因子与定性因子）** 如果因子的水平是某个区间尺度的数值变量的值，例如温度、压力或 RF 功率，使水平之间的差与距离有意义，则它是**定量因子**。如果因子的水平是没有数值尺度的类别，例如材料类型、操作员或供应商，则它是**定性因子**（分类因子）。

固定效应模型把所有因子都当作定性的：效应 $\tau_1,\dots,\tau_a$ 是互不相关的参数，把水平的标签重新排列并不改变分析。对定量因子，这就忽略了信息。以水平为 $160$、$180$、$200$、$220$ W 的刻蚀实验为例，自然的目标是描述刻蚀速率如何依赖于功率，预测未试验设置下的速率，并找出最佳设置；这些需要一个关于功率 $x$ 的回归模型。这类回归模型是经验的而不是机理的：它们在实验区域内近似一个未知的光滑关系，不应远远外推到该区域之外。

作为回归，带约束 $\sum\tau_i=0$ 的刻蚀实验的固定效应模型是 $\boldsymbol{y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$，$\boldsymbol{\beta}=(\mu,\tau_1,\tau_2,\tau_3)^{\mathsf T}$，$\tau_4=-\tau_1-\tau_2-\tau_3$；$X$ 对四个水平的行是

$$
\begin{bmatrix}1&1&0&0\\1&0&1&0\\1&0&0&1\\1&-1&-1&-1\end{bmatrix}\otimes\boldsymbol{1}_n
$$
（每行对 $n=5$ 片晶圆重复）。另一个选择是简单线性回归模型

$$
y_{ij}=\beta_0+\beta_1x_i+\varepsilon_{ij},\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
设计矩阵的行为 $(1,x_i)$，用最小二乘 $\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{y}$ 拟合，$\hat\sigma^2=\boldsymbol{e}^{\mathsf T}\boldsymbol{e}/(N-p)$，$p=2$，并用通常的 $H_0\colon\beta_j=0$ 的 $t$ 检验与 $H_0\colon\beta_1=0$ 的 $F$ 检验。

对预测变量中心化，既简化计算，也简化解释。令 $z_i=(x_i-\bar x)/\Delta$，其中 $\bar x=190$ 是中心，$\Delta=10$ W 是间距的一半，则各水平变为 $z=-3,-1,1,3$，设计矩阵的列 $\boldsymbol{1}$ 与 $\boldsymbol{z}$ 正交，因为 $\sum_iz_i=0$。于是 $X^{\mathsf T}X$ 是对角的，截距与斜率的估计不相关，截距估计设计中心处的平均响应，增加或去掉一项也不改变其他估计。正交性是设计的性质：对等间距的水平与相等的重复，总可以通过这样的线性变换得到它。

### 5.4.2. 两个模型的比较

```r
x <- as.numeric(as.character(Etch$Power))   # as.numeric(Etch$Power) would give 1, 2, 3, 4
summary(lm(Rate ~ x, data = Etch))          # regression model
summary(lm(Rate ~ Power, data = Etch))      # fixed-effects model
```

```text
Coefficients (regression model):
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 137.6200    41.2108   3.339  0.00365 ** 
x             2.5270     0.2154  11.731 7.26e-10 ***
Residual standard error: 21.54 on 18 degrees of freedom
Multiple R-squared:  0.8843,	Adjusted R-squared:  0.8779 
F-statistic: 137.6 on 1 and 18 DF,  p-value: 7.263e-10

Coefficients (fixed-effects model):
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  551.200      8.169  67.471  < 2e-16 ***
Power180      36.200     11.553   3.133  0.00642 ** 
Power200      74.200     11.553   6.422 8.44e-06 ***
Power220     155.800     11.553  13.485 3.73e-10 ***
Residual standard error: 18.27 on 16 degrees of freedom
Multiple R-squared:  0.9261,	Adjusted R-squared:  0.9122 
F-statistic:  66.8 on 3 and 16 DF,  p-value: 2.883e-09
```

拟合的直线表明，功率每增加一瓦，刻蚀速率约增加 $2.53$ Å/min，截距 $137.6$ 是外推到零功率处的速率，没有物理意义。固定效应模型报告 160 W 水平的均值 $551.2$ 以及其他水平均值与它的差。

| | 回归模型 $y_{ij}=\beta_0+\beta_1x_i+\varepsilon_{ij}$ | 固定效应模型 $y_{ij}=\mu+\tau_i+\varepsilon_{ij}$ |
|---|---|---|
| 自由参数 | 3：$\beta_0,\beta_1,\sigma^2$ | $a+1$：$\mu,\tau_1,\dots,\tau_{a-1},\sigma^2$ |
| 误差自由度 | $N-2=18$ | $N-a=16$ |
| SSE（刻蚀） | $8352.5$ | $5339.2$ |
| 残差标准误 | $21.54$ | $18.27$ |
| $R^2$ | $0.884$ | $0.926$ |
| 是否需要重复 | 不需要：两个不同的水平就足以拟合直线 | 需要：$\sigma^2$ 由各水平内的重复估计 |
| 在其他 $x$ 处的预测 | 能（在范围内内插） | 不能：只有试验过的水平 |
| 对形状的假定 | 关于 $x$ 线性；对这一假定敏感 | 无 |

回归模型的参数更少，留给估计 $\sigma^2$ 的自由度更多，不需要重复，并且能在各水平之间预测。它的局限是线性的假定。它的 SSE 必然至少与固定效应模型的一样大，因为回归模型嵌套在其中：直线 $\beta_0+\beta_1x_i$ 是水平均值 $\mu+\tau_i$ 的一种特殊选择，而固定效应模型自由地拟合每个水平的均值。较大的 SSE 是否要紧，恰是 [3.3.5](/3.3.5) 的失拟问题。

回归模型的误差偏差分解为纯误差偏差与失拟偏差，

$$
y_{ij}-\hat y_{ij}=(y_{ij}-\bar y_{i\cdot})+(\bar y_{i\cdot}-\hat y_{ij}),
$$
求平方和（交叉乘积项为零），得

$$
\mathrm{SSE}=\mathrm{SSPE}+\mathrm{SSLF},\qquad N-2=(N-a)+(a-2),
$$
其中**纯误差平方和** $\mathrm{SSPE}=\sum_{i,j}(y_{ij}-\bar y_{i\cdot})^2$ 就是固定效应模型的 SSE，**失拟平方和** $\mathrm{SSLF}=\sum_in_i(\bar y_{i\cdot}-\hat y_i)^2$ 度量各水平均值偏离直线的程度。$H_0$："平均响应关于 $x$ 是线性的"的检验是

$$
F_0=\frac{\mathrm{SSLF}/(a-2)}{\mathrm{SSPE}/(N-a)}\ \overset{H_0}{\sim}\ F_{a-2,N-a},
$$
这就是回归模型（简化模型）对固定效应模型（完全模型）的**一般线性检验**。对刻蚀数据，$\mathrm{SSLF}=8352.5-5339.2=3013.3$，自由度 $2$，$F_0=1506.6/333.7=4.51$，$p=0.028$：在 5% 水平下，直线是不够的。在 R 中，`anova(lm(Rate ~ x), lm(Rate ~ Power))` 执行这个检验。

### 5.4.3. 二次与多项式模型

失拟提示存在曲率，而水平均值对功率的图也证实，速率在高功率处增长得更快。**多项式回归**（[3.3.10](/3.3.10)）加上一个二次项，

$$
y_{ij}=\beta_0+\beta_1x_i+\beta_2x_i^2+\varepsilon_{ij},
$$
其中 $\beta_1$ 描述因子的线性效应，$\beta_2$ 描述二次效应。

```r
modf <- lm(Rate ~ x + I(x^2), data = Etch)   # or: x2 <- x^2; lm(Rate ~ x + x2)
summary(modf)
```

```text
Coefficients:
              Estimate  Std. Error t value Pr(>|t|)   
(Intercept) 1147.77000   368.52081   3.115  0.00631 **
x             -8.25550     3.91993  -2.106  0.05037 . 
I(x^2)         0.02838     0.01030   2.754  0.01356 * 

Residual standard error: 18.43 on 17 degrees of freedom
Multiple R-squared:   0.92,	Adjusted R-squared:  0.9106 
F-statistic: 97.76 on 2 and 17 DF,  p-value: 4.74e-10
```

二次项显著（$p=0.014$），$R^2$ 升到 $0.920$，残差标准误 $18.43$ 接近固定效应模型的 $18.27$。二次模型的失拟检验，$F_0=(5776.0-5339.2)/333.7=1.31$，自由度 1 与 16（$p=0.27$），没有发现进一步的偏离：均值用三个参数时，二次模型对四个水平均值的拟合几乎与四参数的固定效应模型一样好，并且它能内插。

线性项的 $p$ 值 $0.050$ 处于临界，应不应该把它从二次模型中去掉？不应该，而且 $p$ 值也不是正确的准则。在未中心化的模型中，$\beta_1$ 是抛物线在 $x=0$ 处的斜率，远在实验范围之外，它的 $t$ 检验问的是零功率处的切线是否水平，这个问题毫无兴趣。它的值与显著性随 $x$ 的原点而变，而拟合曲线不变。含二次项的模型应当保留低阶项（[3.3.10](/3.3.10)的层次原则）：没有它，曲线就被迫在 $x=0$ 处有顶点。在中心化的参数化下，线性系数高度显著。

中心化还使二次模型正交。令 $z=(x-190)/10$，则列 $\boldsymbol{1}$、$\boldsymbol{z}$ 与 $\boldsymbol{z}^2-5$（平方用其均值 $5$ 中心化）由于设计对称而两两正交，拟合变为

$$
\hat y=617.75+25.27\,z+2.84\,(z^2-5),
$$
其中 $617.75$ 是总均值，线性系数与直线拟合的 $2.527\times10$ 相同。对 $a$ 个等间距的水平，这种构造继续到次数至多为 $a-1$ 的正交多项式，它们把处理平方和分解为单自由度的对照。对刻蚀数据，用正交多项式**对照** $(-3,-1,1,3)$、$(1,-1,-1,1)$ 与 $(-1,3,-3,1)$，线性、二次与三次成分分别为 $63857.3$、$2576.5$ 与 $436.8$，加起来是 $\mathrm{SS}_{\mathrm{Tr}}=66870.6$；二次与三次成分合起来构成直线的 $\mathrm{SSLF}=3013.3$。$a=4$ 个水平的三次模型精确内插四个均值，又回到固定效应模型。

![刻蚀速率对 RF 功率的图：观测值、固定效应模型估计的水平均值，以及拟合的线性与二次回归曲线](./plots/etch-regression.py)

## 小结 {#summary}

检查单因素模型的假定：

| 假定 | 图形检查 | 形式工具 | 备注 |
|---|---|---|---|
| 正态性 | 残差的正态概率图 | | $F$ 检验对适度的偏离稳健 |
| 无离群值 | 尺度化残差 $d_{ij}=e_{ij}/\sqrt{\mathrm{MS}_{\mathrm{E}}}$ | $\lvert d_{ij}\rvert>3$ | 杠杆值为 $1/n_i$（命题 5.1.1） |
| 独立性 | 残差对试验顺序或时间 | | 由随机化保护 |
| 方差相等 | 残差对拟合值 | Bartlett（对非正态性敏感）、Levene / Brown–Forsythe（稳健） | 若被违反：变换、加权，或 Welch 方差分析（定义 5.1.2） |

功效与样本量：$F_0\sim F_{a-1,N-a}(\lambda)$，$\lambda=n\sum\tau_i^2/\sigma^2$（定理 5.2.1）；`power.anova.test` 用 `between.var` $=\sum\tau_i^2/(a-1)$；若只给定极差 $\Delta$，则用 $\sum\tau_i^2=\Delta^2/2$（命题 5.2.1）；$n$ 向上取整。

固定效应与随机效应，同一张方差分析表：

| 来源 | df | MS | $\mathbb{E}[\mathrm{MS}]$，固定 | $\mathbb{E}[\mathrm{MS}]$，随机 |
|---|---|---|---|---|
| 处理 | $a-1$ | $\mathrm{MS}_{\mathrm{Tr}}$ | $\sigma^2+\dfrac{n\sum_i\tau_i^2}{a-1}$ | $\sigma^2+n\sigma_\tau^2$ |
| 误差 | $N-a$ | $\mathrm{MS}_{\mathrm{E}}$ | $\sigma^2$ | $\sigma^2$ |
| 总计 | $N-1$ | | | |

- 随机效应：$H_0\colon\sigma_\tau^2=0$，同样的 $F_0=\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}$；$\hat\sigma^2=\mathrm{MS}_{\mathrm{E}}$，$\hat\sigma_\tau^2=(\mathrm{MS}_{\mathrm{Tr}}-\mathrm{MS}_{\mathrm{E}})/n$（在 $0$ 处截断或用 REML），$\hat\rho_I=\hat\sigma_\tau^2/(\hat\sigma_\tau^2+\hat\sigma^2)$。
- 同一水平内的观测相关，相关系数为 $\rho_I$（复合对称）；$\operatorname{Var}(\bar Y_{\cdot\cdot})=\sigma_\tau^2/a+\sigma^2/(an)$，估计为 $\mathrm{MS}_{\mathrm{Tr}}/N$。
- 区间：$\sigma^2$（$\chi^2_{N-a}$）与 $\sigma_\tau^2/\sigma^2$ 及 $\rho_I$（$F_{a-1,N-a}$）有精确区间；$\sigma_\tau^2$ 只有近似（Satterthwaite）区间。
- 选择取决于研究问题：关于这些水平的结论（固定）或关于水平总体的结论（随机）。

对定量因子，回归模型（$3$ 个自由参数、$N-2$ 个误差自由度、可内插、不需要重复）嵌套在固定效应模型（$a+1$ 个参数、SSE 较小）中；$\mathrm{SSE}=\mathrm{SSPE}+\mathrm{SSLF}$ 给出自由度为 $a-2$ 与 $N-a$ 的失拟检验；添加多项式项时要保留低阶项，最好用中心化或正交的形式。

## 思考题

1. 一个单因素随机效应方差分析给出下表：处理，df $3$，SS $80$；误差，df $24$，SS $120$；总计，df $27$，SS $200$。补全均方，并估计 $\sigma^2$、$\sigma_\tau^2$ 与组内相关系数。在 $\alpha=0.05$ 下，$\sigma_\tau^2$ 是否显著为正？

   **答** $a=4$，$N=28$，所以 $n=7$。$\mathrm{MS}_{\mathrm{Tr}}=80/3=26.67$，$\mathrm{MS}_{\mathrm{E}}=120/24=5$（而 $\mathrm{SS}_{\mathrm{T}}/27=7.41$ 是全部观测的样本方差，这里不用）。于是 $\hat\sigma^2=5$，$\hat\sigma_\tau^2=(26.67-5)/7=3.10$，$\hat\rho_I=3.10/8.10=0.38$。$F_0=26.67/5=5.33$ 超过 $F_{3,24,0.05}=3.01$（$p\approx0.006$），所以拒绝 $H_0\colon\sigma_\tau^2=0$。

2. 在随机效应模型中，证明观测不是独立的，并计算 $\operatorname{Var}(\bar Y_{i\cdot})$ 与 $\operatorname{Var}(\bar Y_{\cdot j})$，其中 $\bar Y_{\cdot j}=\frac1a\sum_iY_{ij}$ 是把第 $j$ 个观测在各水平上取平均。

   **答** 对 $j\ne j'$，$\operatorname{Cov}(Y_{ij},Y_{ij'})=\sigma_\tau^2$，除非 $\sigma_\tau^2=0$，它不为零；由于观测联合正态，只有当 $\sigma_\tau^2=0$ 时它们才独立。$\bar Y_{i\cdot}=\mu+\tau_i+\bar\varepsilon_{i\cdot}$ 的方差是 $\sigma_\tau^2+\sigma^2/n$：水平效应在一个水平内没有被平均掉。$\bar Y_{\cdot j}=\mu+\bar\tau+\frac1a\sum_i\varepsilon_{ij}$ 的方差是 $(\sigma_\tau^2+\sigma^2)/a$，因为它对 $a$ 个独立的水平取平均。

3. 对每种情形，判断因子应是固定的还是随机的。(a) 一家制药公司比较其三个候选的药物配方。(b) 从某供应商的产品中抽取五批原料，评估批次间的变异。(c) 一位农学家在一个农场的田地里比较四种特定的肥料。

   **答** (a) 固定：三个配方是仅有的感兴趣的，目标是比较它们。(b) 随机：各批是样本，目标是批次总体的方差分量。(c) 肥料是固定的。如果田地也是因子（作为区组，被抽样来代表该地区），则田地是随机的；答案取决于问题，而不取决于变量。

4. 在织机的例子中，为什么随机效应的截距标准误是 $1.363$，而 `lm` 的截距是 $0.688$？什么最能有效地减小前者？

   **答** `lm` 的截距估计织机 1 的均值，其唯一的不确定性是测量误差：$\sqrt{\hat\sigma^2/4}=0.688$。`lmer` 的截距估计全部织机的平均强度 $\mu$，而 $\operatorname{Var}(\bar Y_{\cdot\cdot})=\sigma_\tau^2/a+\sigma^2/(an)$ 含有被抽样织机之间的变异：$\sqrt{6.958/4+1.896/16}=\sqrt{\mathrm{MS}_{\mathrm{Tr}}/N}=1.363$。增大 $n$ 只减小第二项（总的 $1.858$ 中的 $0.118$）；由于第一项占优，抽样更多的织机（增大 $a$）有效得多。

5. 计划一个平衡的单因素固定效应实验，$a=5$ 个水平，$\sigma=4$，$\alpha=0.05$，目标功效为 $0.90$。实验者想检出最大与最小均值相差 $\Delta=8$ 的任何配置。应该给 `power.anova.test` 的 `between.var` 取什么值？为什么这保证了所有这类配置的功效？

   **答** 最不利的配置有 $\sum\tau_i^2=\Delta^2/2=32$（命题 5.2.1），所以 `between.var` $=32/(a-1)=8$，`within.var` $=16$。功效是 $\lambda=n\sum\tau_i^2/\sigma^2$ 的增函数，而每个极差至少为 $\Delta$ 的配置都有 $\sum\tau_i^2\ge\Delta^2/2$，所以它的功效至少是对最不利配置算出的功效。（得到的 $n$ 约为 $8.7$，向上取整为每个水平 $9$ 个；取 $n=8$ 时功效为 $0.866$。）

6. 对刻蚀数据，数一数线性回归模型与固定效应模型的自由参数，并解释哪个的 SSE 更小。然后仅用两个 R 输出，完成线性模型的失拟检验。

   **答** 回归模型有 3 个自由参数（$\beta_0,\beta_1,\sigma^2$），固定效应模型有 $a+1=5$ 个（$\mu,\tau_1,\tau_2,\tau_3,\sigma^2$）。固定效应模型的 SSE 更小，因为回归模型是它的特例（水平均值落在一条直线上）。由输出，$\mathrm{SSE}_{\mathrm{reg}}=18\times21.54^2=8352$，$\mathrm{SSPE}=16\times18.27^2=5339$，所以 $\mathrm{SSLF}=3013$，自由度 $18-16=2$，$F_0=(3013/2)/(5339/16)=4.51>F_{2,16,0.05}=3.63$（$p=0.028$）：直线有显著的失拟。

7. 证明当 $a=2$ 个水平时，Welch 方差分析统计量等于 Welch $t$ 统计量的平方，且 $\nu$ 等于 Welch–Satterthwaite 自由度。

   **答** 记 $v_i=s_i^2/n_i=1/w_i$，$\bar y'=(w_1\bar y_1+w_2\bar y_2)/(w_1+w_2)$，分子为 $w_1(\bar y_1-\bar y')^2+w_2(\bar y_2-\bar y')^2=\frac{w_1w_2}{w_1+w_2}(\bar y_1-\bar y_2)^2=\frac{(\bar y_1-\bar y_2)^2}{v_1+v_2}=t^2$。当 $a=2$ 时分母中的修正因子是 $1+0=1$，所以 $F_0^*=t^2$。又 $1-w_1/w=v_1/(v_1+v_2)$，$1-w_2/w=v_2/(v_1+v_2)$，所以 $\Lambda=\frac{v_1^2/(n_1-1)+v_2^2/(n_2-1)}{(v_1+v_2)^2}$，$\nu=3/(3\Lambda)=\frac{(v_1+v_2)^2}{v_1^2/(n_1-1)+v_2^2/(n_2-1)}$，这就是 Welch–Satterthwaite 公式。
