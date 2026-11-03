---
title: 单因子实验：方差分析
description: 完全随机化的单因子实验及其方差分析；均值模型与效应模型、平方和的分解、期望均方、F 检验与方差分析表；分解的几何与 Cochran 定理；作为回归、一般线性检验与似然比检验的方差分析。
source_hash: 1b35f7fee62f
---

简单对比实验比较两个处理；多数实验要比较更多。当一个因子取 $a$ 个水平，其余条件保持不变或被随机化时，"各水平的平均响应有无差异？"这一自然的问题由**方差分析**来回答。当 $a=2$ 时，方差分析的 $F$ 检验恰好就是 [3.8.2](/3.8.2) 的合并**两样本 t 检验**（$F=t^2$），所以这个方法是它向多个组的推广。回归课程已经从建模的角度处理过单因素方差分析（[3.3.12](/3.3.12)、[3.3.13](/3.3.13)）；本章则从实验的角度展开：数据如何收集（完全随机化设计）、方差分析表的每一项是什么意思、为什么这样计算、自由度背后的几何，以及为什么方差分析的 $F$ 检验、一般线性检验与似然比检验是同一个检验。$F$ 检验显著之后的一步，即判断哪些水平有差异，是 [3.8.4](/3.8.4) 的主题；检查假设、规划样本量以及把水平视为随机的情形见 [3.8.5](/3.8.5)。

记号。因子有 $a$ 个水平，水平 $i$ 上有 $n_i$ 个观测（平衡实验中 $n_i=n$），共 $N=\sum_i n_i$ 个观测。点号代替被求和的下标，横线表示平均：$y_{i\cdot}=\sum_j y_{ij}$，$\bar y_{i\cdot}=y_{i\cdot}/n_i$，$y_{\cdot\cdot}=\sum_{i,j}y_{ij}$，$\bar y_{\cdot\cdot}=y_{\cdot\cdot}/N$。在模型与定理中，观测是随机变量，写作 $Y_{ij}$；在数据与算例中写作 $y_{ij}$（实验设计的许多文献对两者都用小写）。平方和与均方带直立下标，$\mathrm{SS}_{\mathrm{T}}$、$\mathrm{SS}_{\mathrm{Tr}}$、$\mathrm{SS}_{\mathrm{E}}$、$\mathrm{MS}_{\mathrm{Tr}}$、$\mathrm{MS}_{\mathrm{E}}$；它们对应于 [3.3.12](/3.3.12) 的 SSTO、SSTR、SSE、MSTR 与 MSE。

## 3.1. 单因子实验与完全随机化设计

一位工程师研究单片晶圆的等离子体刻蚀设备。刻蚀速率取决于施加于腔室的射频（RF）功率，她想知道所关心的四个功率设置 $160$、$180$、$200$ 与 $220\,\mathrm{W}$ 是否给出不同的平均刻蚀速率；她怀疑功率越高速率越高。每个设置刻蚀五片晶圆，$20$ 次试验按随机顺序进行。响应以 $\mathrm{\mathring{A}}/\mathrm{min}$ 记录（一埃为 $0.1\,\mathrm{nm}$）。

| RF 功率 / W | 观测值 | $y_{i\cdot}$ | $\bar y_{i\cdot}$ | $s_i$ |
|---|---|---|---|---|
| 160 | 575, 542, 530, 539, 570 | 2756 | 551.2 | 20.02 |
| 180 | 565, 593, 590, 579, 610 | 2937 | 587.4 | 16.74 |
| 200 | 600, 651, 610, 637, 629 | 3127 | 625.4 | 20.53 |
| 220 | 725, 700, 715, 685, 710 | 3535 | 707.0 | 15.25 |
| | | $y_{\cdot\cdot} = 12355$ | $\bar y_{\cdot\cdot} = 617.75$ | |

数据在 R 中录入为数据框，其解释变量是一个因子：

```r
y <- c(575, 542, 530, 539, 570,
       565, 593, 590, 579, 610,
       600, 651, 610, 637, 629,
       725, 700, 715, 685, 710)
X <- rep(c(160, 180, 200, 220), each = 5)
etch.rate <- data.frame(RF = as.factor(X), rate = y)
```

![刻蚀速率对 RF 功率的图：各片晶圆（点）、各水平的均值（菱形）与总均值（虚线），并附四组的箱线图。](./plots/etch-data.py)

这张图提出两个问题，它们组织了本章与下一章：(1) 四个功率水平的平均刻蚀速率是否相等？(2) 如果不等，哪些水平两两之间有差异？

在这个实验中，RF 功率是唯一的**因子**，它的四个设置是**因子水平**（处理），每片晶圆是一个实验单位，$20$ 次试验的顺序是随机选定的。这是最简单的实验设计。

**定义 3.1.1（完全随机化设计）** 在**完全随机化设计**（CRD）中，$N$ 个实验单位被完全随机地分配给 $a$ 个处理，处理 $i$ 得到 $n_i$ 个单位，使具有这些组大小的每一种分配的可能性相等；当试验按先后顺序进行时，试验顺序也是随机的。

随机化使各组可比：未知的变异来源（漂移的腔室、操作员的更换）分散在各处理上，而不是与处理混杂，并且使把误差视为独立成为合理。CRD 对随机化没有限制；在区组内随机化的设计见后面的章节。这里四个水平是仅有的关心的功率设置，结论是关于这四个水平的：因子是固定的。如果水平是从更大的水平总体中随机抽取的样本，则推断是关于那个总体的；这种随机效应模型是 [3.8.5](/3.8.5) 的主题。

这个实验是平衡的，$n_1=\cdots=n_a$。正如 [3.8.2](/3.8.2) 对两组所示，在总试验次数固定时，**平衡设计**使比较的功效最大，并使检验对方差不等不太敏感；对于多个组，它还使方差分析分解的各平方和正交、易于计算。尽管如此，下面的所有公式都对一般的 $n_i$ 写出。

## 3.2. 模型

### 3.2.1. 均值模型与效应模型

数据的模型有两种等价的写法。**单元格均值模型**（均值模型）是

$$
Y_{ij} = \mu_i + \varepsilon_{ij},\qquad \varepsilon_{ij} \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2),\qquad i = 1, \dots, a,\quad j = 1, \dots, n_i,
$$
其中 $\mu_i$ 是水平 $i$ 上的平均响应。**因子效应模型**（效应模型）把每个均值写成总均值加一个偏差，

$$
Y_{ij} = \mu + \tau_i + \varepsilon_{ij},\qquad \sum_{i=1}^a \tau_i = 0,
$$
其中 $\mu$ 是总均值，$\tau_i = \mu_i - \mu$ 是水平 $i$ 的**处理效应**，$\varepsilon_{ij}$ 是随机的实验误差。两个模型描述同样的分布；效应模型比均值多一个参数，约束消除了这种冗余（也可以用其他约束，见 [3.3.13](/3.3.13)）。在约束 $\sum_i\tau_i = 0$ 下，$\mu = \frac1a\sum_i\mu_i$；对非平衡数据，加权约束 $\sum_i n_i\tau_i = 0$ 往往更方便，此时 $\mu = \sum_i n_i\mu_i/N$。两个模型都假定观测独立、正态且方差相同，为 $\sigma^2$。

各处理均值相等的假设有两种等价的形式：

$$
H_0\colon \mu_1 = \mu_2 = \cdots = \mu_a \quad\text{对}\quad H_1\colon \mu_i \ne \mu_j \text{ 至少对一对 } (i, j),
$$

$$
H_0\colon \tau_1 = \tau_2 = \cdots = \tau_a = 0 \quad\text{对}\quad H_1\colon \tau_i \ne 0 \text{ 至少对一个 } i.
$$

### 3.2.2. 作为回归的模型

把观测按水平排序。两个模型都是线性回归 $\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$，$\boldsymbol{\varepsilon} \sim \mathcal{N}_N(\boldsymbol{0}, \sigma^2 I_N)$；它们的区别在于**设计矩阵**。对均值模型，$\boldsymbol{\beta} = (\mu_1, \dots, \mu_a)^{\mathsf T}$，$X$ 由 $a$ 个示性列构成：

$$
X = \begin{bmatrix} \boldsymbol{1}_{n_1} & \boldsymbol{0} & \cdots & \boldsymbol{0} \\ \boldsymbol{0} & \boldsymbol{1}_{n_2} & \cdots & \boldsymbol{0} \\ \vdots & & \ddots & \vdots \\ \boldsymbol{0} & \boldsymbol{0} & \cdots & \boldsymbol{1}_{n_a} \end{bmatrix}.
$$
对带 $\sum_i\tau_i = 0$ 的效应模型，最后一个效应是 $\tau_a = -\tau_1 - \cdots - \tau_{a-1}$，所以 $\boldsymbol{\beta} = (\mu, \tau_1, \dots, \tau_{a-1})^{\mathsf T}$，$X$ 的第一列是 $\boldsymbol{1}_N$，水平 $a$ 的各行在每个 $\tau$ 列中都是 $-1$：

$$
X = \begin{bmatrix} \boldsymbol{1}_{n_1} & \boldsymbol{1}_{n_1} & \boldsymbol{0} & \cdots & \boldsymbol{0} \\ \boldsymbol{1}_{n_2} & \boldsymbol{0} & \boldsymbol{1}_{n_2} & \cdots & \boldsymbol{0} \\ \vdots & & & \ddots & \vdots \\ \boldsymbol{1}_{n_{a-1}} & \boldsymbol{0} & \boldsymbol{0} & \cdots & \boldsymbol{1}_{n_{a-1}} \\ \boldsymbol{1}_{n_a} & -\boldsymbol{1}_{n_a} & -\boldsymbol{1}_{n_a} & \cdots & -\boldsymbol{1}_{n_a} \end{bmatrix}.
$$

R 默认两者都不用。对因子，它使用处理对照：一个截距列加上水平 $2, \dots, a$ 的示性变量，对应于约束 $\tau_1 = 0$。此时截距是第一个水平的均值，每个系数是某个水平均值与第一水平均值之差。

```r
fit1 <- lm(rate ~ RF, data = etch.rate)
model.matrix(fit1)
```

```text
   (Intercept) RF180 RF200 RF220
1            1     0     0     0
...
5            1     0     0     0
6            1     1     0     0
...
11           1     0     1     0
...
16           1     0     0     1
...
20           1     0     0     1
```

公式 `rate ~ 0 + RF` 去掉截距，给出均值模型，系数 `RF160`、…、`RF220` 等于四个水平的均值。三种参数化有相同的列空间，因而有相同的拟合值、残差与方差分析表。

### 3.2.3. 估计

**命题 3.2.1** 在均值模型中，$\mu_1, \dots, \mu_a$ 的最小二乘估计量是 $\hat\mu_i = \bar Y_{i\cdot}$。在带 $\sum_i\tau_i = 0$ 且各 $n_i$ 相等的效应模型中，$\hat\mu = \bar Y_{\cdot\cdot}$，$\hat\tau_i = \bar Y_{i\cdot} - \bar Y_{\cdot\cdot}$。两种情形下，$Y_{ij}$ 的拟合值都是 $\bar Y_{i\cdot}$，残差是 $e_{ij} = Y_{ij} - \bar Y_{i\cdot}$。

**证明** 最小二乘准则按组分离：

$$
Q(\mu_1, \dots, \mu_a) = \sum_{i=1}^a\sum_{j=1}^{n_i}(Y_{ij} - \mu_i)^2 = \sum_{i=1}^a Q_i(\mu_i),\qquad Q_i(\mu_i) = \sum_{j=1}^{n_i}(Y_{ij} - \mu_i)^2.
$$
每个 $Q_i$ 只依赖于 $\mu_i$，而 $Q_i(\mu_i) = \sum_j(Y_{ij} - \bar Y_{i\cdot})^2 + n_i(\bar Y_{i\cdot} - \mu_i)^2$ 在 $\mu_i = \bar Y_{i\cdot}$ 处最小。效应模型是一种重新参数化，$\mu = \frac1a\sum_i\mu_i$，$\tau_i = \mu_i - \mu$，所以它的估计量是 $\hat\mu_i$ 的同样的函数；当各 $n_i$ 相等时，$\frac1a\sum_i\bar Y_{i\cdot} = \bar Y_{\cdot\cdot}$。$\square$

误差方差通过合并组内变异来估计，

$$
\hat\sigma^2 = \mathrm{MS}_{\mathrm{E}} = \frac{\sum_i\sum_j(Y_{ij} - \bar Y_{i\cdot})^2}{N - a} = \frac{\sum_i(n_i - 1)s_i^2}{N - a},
$$
即 $a$ 个组的**合并方差**；它是无偏的（定理 3.3.1）。由于 $\bar Y_{i\cdot} \sim \mathcal{N}(\mu_i, \sigma^2/n_i)$ 且与 $\mathrm{MS}_{\mathrm{E}}$ 独立，$(N - a)\mathrm{MS}_{\mathrm{E}}/\sigma^2 \sim \chi^2_{N-a}$，所以某个水平均值以及两个水平均值之差的 $100(1 - \alpha)\%$ **置信区间**分别为

$$
\bar y_{i\cdot} \pm t_{N-a,\alpha/2}\sqrt{\frac{\mathrm{MS}_{\mathrm{E}}}{n_i}},\qquad \bar y_{i\cdot} - \bar y_{j\cdot} \pm t_{N-a,\alpha/2}\sqrt{\mathrm{MS}_{\mathrm{E}}\Bigl(\frac{1}{n_i} + \frac{1}{n_j}\Bigr)}.
$$
方差估计用到了全部 $N$ 个观测，所以区间用 $N - a$ 个自由度，而不是单个组的 $n_i - 1$。对刻蚀数据，$\mathrm{MS}_{\mathrm{E}} = 333.7$（下面计算），$\sqrt{333.7/5} = 8.17$，$t_{16,0.025} = 2.120$，所以 $220\,\mathrm{W}$ 时均值的 95% 区间是 $707.0 \pm 17.3$，$\mu_4 - \mu_1$ 的区间是 $155.8 \pm 24.5$。这些是单个的区间；对多个比较同时成立的区间是 [3.8.4](/3.8.4) 的主题。

## 3.3. 平方和的分解与方差分析表

### 3.3.1. 分解

"方差分析"这一名称来自把响应的总变异分解为与模型各项对应的成分。总变异用**总平方和**度量

$$
\mathrm{SS}_{\mathrm{T}} = \sum_{i=1}^a\sum_{j=1}^{n_i}(y_{ij} - \bar y_{\cdot\cdot})^2.
$$
把 $y_{ij} - \bar y_{\cdot\cdot} = (y_{ij} - \bar y_{i\cdot}) + (\bar y_{i\cdot} - \bar y_{\cdot\cdot})$ 平方，交叉项 $2\sum_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})\sum_j(y_{ij} - \bar y_{i\cdot})$ 因内层和为零而消失。因此

$$
\underbrace{\sum_{i=1}^a\sum_{j=1}^{n_i}(y_{ij} - \bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{T}}} = \underbrace{\sum_{i=1}^a n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{Tr}}} + \underbrace{\sum_{i=1}^a\sum_{j=1}^{n_i}(y_{ij} - \bar y_{i\cdot})^2}_{\mathrm{SS}_{\mathrm{E}}}. \tag{3.1}
$$
**处理平方和** $\mathrm{SS}_{\mathrm{Tr}}$ 度量各水平均值之间的差异，即组间变异；误差平方和 $\mathrm{SS}_{\mathrm{E}}$ 度量观测值围绕其所在水平均值的变异，即组内变异。用回归的语言说，$\mathrm{SS}_{\mathrm{Tr}} = \sum_{i,j}(\hat\mu_i - \hat{\bar\mu})^2$ 是拟合均值的回归平方和，而 $\mathrm{SS}_{\mathrm{E}}$ 是剩下的部分。$\mathrm{SS}_{\mathrm{Tr}}$ 相对于 $\mathrm{SS}_{\mathrm{E}}$ 较大，表明各处理均值之间有差异。

自由度也同样分解：

$$
N - 1 = (a - 1) + (N - a).
$$
$\mathrm{SS}_{\mathrm{T}}$ 是 $N$ 个平方偏差之和，受一个线性约束（$\sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot}) = 0$）；$\mathrm{SS}_{\mathrm{Tr}}$ 涉及 $a$ 个水平均值，受一个约束（$\sum_i n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot}) = 0$）；$\mathrm{SS}_{\mathrm{E}}$ 合并了 $a$ 个组内的和，每个有 $n_i - 1$ 个自由度。3.4 节把这种计数说得更精确。

手算时，平方和由总和计算：

$$
\mathrm{SS}_{\mathrm{T}} = \sum_{i,j} y_{ij}^2 - \frac{y_{\cdot\cdot}^2}{N},\qquad \mathrm{SS}_{\mathrm{Tr}} = \sum_{i=1}^a \frac{y_{i\cdot}^2}{n_i} - \frac{y_{\cdot\cdot}^2}{N},\qquad \mathrm{SS}_{\mathrm{E}} = \mathrm{SS}_{\mathrm{T}} - \mathrm{SS}_{\mathrm{Tr}}.
$$

### 3.3.2. 期望均方

平方和不能直接比较，因为它们是不同项数的和。把每个平方和除以它的自由度，得到**均方**

$$
\mathrm{MS}_{\mathrm{Tr}} = \frac{\mathrm{SS}_{\mathrm{Tr}}}{a - 1},\qquad \mathrm{MS}_{\mathrm{E}} = \frac{\mathrm{SS}_{\mathrm{E}}}{N - a},
$$
它们的期望显示各自估计什么。

**定理 3.3.1（期望均方）** 在效应模型 $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$ 中，设 $\sum_i n_i\tau_i = 0$（平衡实验中即 $\sum_i\tau_i = 0$），则

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{E}}] = \sigma^2,\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}] = \sigma^2 + \frac{\sum_{i=1}^a n_i\tau_i^2}{a - 1},
$$
当 $n_i = n$ 时，后者为 $\sigma^2 + n\sum_i\tau_i^2/(a - 1)$。

**证明** 记 $\bar\varepsilon_{i\cdot} = \frac{1}{n_i}\sum_j\varepsilon_{ij}$，$\bar\varepsilon_{\cdot\cdot} = \frac1N\sum_{i,j}\varepsilon_{ij}$。则 $\bar Y_{i\cdot} = \mu + \tau_i + \bar\varepsilon_{i\cdot}$，且因 $\sum_i n_i\tau_i = 0$，$\bar Y_{\cdot\cdot} = \mu + \bar\varepsilon_{\cdot\cdot}$。对误差平方和，$Y_{ij} - \bar Y_{i\cdot} = \varepsilon_{ij} - \bar\varepsilon_{i\cdot}$，而 $\sum_j(\varepsilon_{ij} - \bar\varepsilon_{i\cdot})^2$ 是 $n_i$ 个独立 $\mathcal{N}(0, \sigma^2)$ 变量的样本方差的 $n_i - 1$ 倍，所以它的期望是 $(n_i - 1)\sigma^2$；对 $i$ 求和，$\mathbb{E}[\mathrm{SS}_{\mathrm{E}}] = (N - a)\sigma^2$。对处理平方和，

$$
\mathrm{SS}_{\mathrm{Tr}} = \sum_i n_i(\tau_i + \bar\varepsilon_{i\cdot} - \bar\varepsilon_{\cdot\cdot})^2 = \sum_i n_i\tau_i^2 + 2\sum_i n_i\tau_i(\bar\varepsilon_{i\cdot} - \bar\varepsilon_{\cdot\cdot}) + \sum_i n_i(\bar\varepsilon_{i\cdot} - \bar\varepsilon_{\cdot\cdot})^2.
$$
中间项的期望为零。在最后一项中，$\sum_i n_i(\bar\varepsilon_{i\cdot} - \bar\varepsilon_{\cdot\cdot})^2 = \sum_i n_i\bar\varepsilon_{i\cdot}^2 - N\bar\varepsilon_{\cdot\cdot}^2$，其期望为 $\sum_i n_i\cdot\sigma^2/n_i - N\cdot\sigma^2/N = (a - 1)\sigma^2$。因此 $\mathbb{E}[\mathrm{SS}_{\mathrm{Tr}}] = \sum_i n_i\tau_i^2 + (a - 1)\sigma^2$；除以 $a - 1$ 即得。$\square$

无论 $H_0$ 是否成立，$\mathrm{MS}_{\mathrm{E}}$ 都是 $\sigma^2$ 的无偏估计量。在 $H_0$ 下 $\mathrm{MS}_{\mathrm{Tr}}$ 对 $\sigma^2$ 也是无偏的，但在 $H_1$ 下，它的期望比 $\sigma^2$ 多一个非负的量，该量随处理效应的大小与样本量增大。因此两个均方的比较是对 $H_0$ 的检验，只有大的比值才是反对 $H_0$ 的证据。这些期望均方将在 [3.8.5](/3.8.5) 中与随机效应模型的相比较，那里同一个比值用来检验另一个假设。

### 3.3.3. F 检验与方差分析表

**定理 3.3.2（方差分析的 F 检验）** 在正态模型中，$\mathrm{SS}_{\mathrm{E}}/\sigma^2 \sim \chi^2_{N-a}$。若 $H_0\colon \tau_1 = \cdots = \tau_a = 0$ 成立，则还有 $\mathrm{SS}_{\mathrm{Tr}}/\sigma^2 \sim \chi^2_{a-1}$，且与 $\mathrm{SS}_{\mathrm{E}}$ 独立，并且

$$
F_0 = \frac{\mathrm{SS}_{\mathrm{Tr}}/(a - 1)}{\mathrm{SS}_{\mathrm{E}}/(N - a)} = \frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}} \sim F_{a-1,N-a}.
$$
水平为 $\alpha$ 的检验在 $F_0 > F_{a-1,N-a,\alpha}$ 时拒绝 $H_0$，其中 $F_{a-1,N-a,\alpha}$ 是 **F 分布**的上 $\alpha$ 分位数；**p 值**是 $\mathbb{P}(F_{a-1,N-a} > F_0)$。

这些分布陈述由 3.4 节的 Cochran 定理得出。尽管 $H_1$ 是"各均值不全相等"，该检验却是单侧的（上尾）：由定理 3.3.1，偏离 $H_0$ 的任何方向都使 $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]$ 增大而 $\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]$ 不变，所以它们使 $F_0$ 变大，决不会变小。（异常小的 $F_0$ 不是关于均值的证据；它可能表明模型有误，例如各次试验并不独立。）

计算汇总在**方差分析表**中：

| 变异来源 | 平方和 | 自由度 | 均方 | $F_0$ | $p$ 值 |
|---|---|---|---|---|---|
| 处理之间 | $\mathrm{SS}_{\mathrm{Tr}} = \sum_i n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2$ | $a - 1$ | $\mathrm{MS}_{\mathrm{Tr}} = \dfrac{\mathrm{SS}_{\mathrm{Tr}}}{a - 1}$ | $\dfrac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}$ | $\mathbb{P}(F_{a-1,N-a} > F_0)$ |
| 误差（处理之内） | $\mathrm{SS}_{\mathrm{E}} = \sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2$ | $N - a$ | $\mathrm{MS}_{\mathrm{E}} = \dfrac{\mathrm{SS}_{\mathrm{E}}}{N - a}$ | | |
| 总计 | $\mathrm{SS}_{\mathrm{T}} = \sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2$ | $N - 1$ | | | |

每一列各有作用。平方和与自由度沿列可加（总计行是其余两行之和），均方则不可加。$\mathrm{MS}_{\mathrm{E}}$ 是 $\sigma^2$ 的估计，其平方根就是 `lm` 报告的残差标准误。$\mathrm{MS}_{\mathrm{Tr}}$ 估计 $\sigma^2$ 加上处理效应。$F_0$ 是两者之比，与 $F_{a-1,N-a}$ 分布比较。由于可加性，三个平方和中的任何两个，连同 $a$ 与 $N$，就决定整张表；有缺项的表就是这样补全的。

方差分析有一个简单的不变性。如果把每个观测换成 $y'_{ij} = c\,y_{ij} + d$，其中 $c > 0$，则各水平均值与总均值作同样的变换，所以 $\hat\tau'_i = c\,\hat\tau_i$，$\hat\sigma' = c\,\hat\sigma$，每个平方和乘以 $c^2$，而 $F_0$ 不变：分析不依赖于响应的位置与测量单位。特别地，手算前先减去一个方便的常数来编码数据，是无害的。

### 3.3.4. 例：等离子体刻蚀实验

由 3.1 节的总和，$\sum y_{ij}^2 = 7{,}704{,}511$，$y_{\cdot\cdot}^2/N = 12355^2/20 = 7{,}632{,}301.25$，所以

$$
\mathrm{SS}_{\mathrm{T}} = 72{,}209.75,\qquad \mathrm{SS}_{\mathrm{Tr}} = \frac{2756^2 + 2937^2 + 3127^2 + 3535^2}{5} - 7{,}632{,}301.25 = 66{,}870.55,
$$
并且 $\mathrm{SS}_{\mathrm{E}} = 72{,}209.75 - 66{,}870.55 = 5339.20$。在 R 中：

```r
etch.rate.aov <- aov(rate ~ RF, data = etch.rate)
summary(etch.rate.aov)
fit1 <- lm(rate ~ RF, data = etch.rate)
anova(fit1)               # the same table from the regression fit
```

```text
Analysis of Variance Table

Response: rate
          Df Sum Sq Mean Sq F value    Pr(>F)    
RF         3  66871 22290.2  66.797 2.883e-09 ***
Residuals 16   5339   333.7                      
```

逐行读这个输出：因子 `RF` 有 $a - 1 = 3$ 个自由度，$\mathrm{SS}_{\mathrm{Tr}} = 66871$，所以 $\mathrm{MS}_{\mathrm{Tr}} = 66871/3 = 22290.2$；残差行有 $N - a = 16$ 个自由度，$\mathrm{SS}_{\mathrm{E}} = 5339$，所以 $\mathrm{MS}_{\mathrm{E}} = 333.7$，$\hat\sigma = \sqrt{333.7} = 18.27\,\mathrm{\mathring{A}/min}$。比值 $F_0 = 22290.2/333.7 = 66.80$ 远超过 $F_{3,16,0.05} = 3.24$ 与 $F_{3,16,0.01} = 5.29$；$\mathbb{P}(F_{3,16} > 66.80) = 2.9\times10^{-9}$。总计行没有打印：$\mathrm{SS}_{\mathrm{T}} = 66871 + 5339 = 72210$，自由度 $19$。我们得出结论：RF 功率设置影响平均刻蚀速率。估计的效应是 $\hat\tau_i = \bar y_{i\cdot} - \bar y_{\cdot\cdot} = -66.55, -30.35, 7.65, 89.25$。

![F(3, 16) 的密度：5% 拒绝域在 3.24 的右侧，而观测到的 F0 = 66.8 远在密度图的范围之外。](./plots/f-reference.py)

### 3.3.5. 组间与组内：直观的看法

$F_0$ 与比值

$$
\frac{\sum_i n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2}{\sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2}
$$
成正比，所以因子效应的证据有两个成分。各水平均值围绕总均值的离散程度大，使效应更显著；观测值围绕其所在水平均值的散布大，使效应更不显著。因此，两个实验即使各组均值之间的差异相同，如果一个实验的组内观测紧密聚集，而另一个的组内观测分散很广，也可能得出相反的结论。

![两个模拟实验，水平均值相同（五个水平，各十个观测）。左：组内散布小，F0 大。右：同样的均值，组内标准差为六倍；均值的差异不再显著。](./plots/between-within.py)

样本量是第三个成分。并排的箱线图显示各个 $y_{ij}$ 的分布，但检验针对的是均值，显著性取决于 $\bar y_{i\cdot}$ 的抽样变异，其方差是 $\sigma^2/n_i$，而不取决于 $y_{ij}$ 本身的散布。$\mathrm{SS}_{\mathrm{Tr}}$ 中的权 $n_i$ 表达了这一点：两组箱线图完全相同的数据，当每个箱概括 $500$ 个观测时，所得 $F_0$ 比概括 $5$ 个观测时大得多。箱线图描述的是数据，而不是均值的精度，箱线图大量重叠的数据也可能与高度显著的 $F$ 检验相容。

分解 (3.1) 有一个概率上的对应。设 $X$ 是从实验中随机选取的一个观测所在的组标签，$Y$ 是它的响应。**全方差公式**（[3.1.9](/3.1.9)）

$$
\operatorname{Var}(Y) = \mathbb{E}\bigl[\operatorname{Var}(Y \mid X)\bigr] + \operatorname{Var}\bigl(\mathbb{E}[Y \mid X]\bigr)
$$
把响应的方差分解为组内方差的平均与组均值的方差。把 (3.1) 除以 $N$ 就得到经验版本：$\mathrm{SS}_{\mathrm{T}}/N$ 是全部观测的方差，$\mathrm{SS}_{\mathrm{E}}/N$ 是组内方差的加权平均，$\mathrm{SS}_{\mathrm{Tr}}/N$ 是组均值的加权方差。当第二项占优时，因子对 $Y$ 的预测就好，也就是说，知道组别能使条件均值 $\mathbb{E}[Y \mid X]$ 远离总均值，同时条件分布又很窄。

## 3.4. 几何与分布理论

### 3.4.1. 自由度

平方和的自由度有几种等价的理解方式：一是其中在计入约束之后可以自由变动的量的个数；二是相应的随机向量所在空间的维数；三是确定该向量所需的独立坐标的最少个数。引入这一概念的 Fisher 是通过多维几何得到它的。对样本 $x_1, \dots, x_n$，把观测值看作 $\mathbb{R}^n$ 中的点 $P = (x_1, \dots, x_n)$，令 $M = (\bar x, \dots, \bar x) = \bar x\,\boldsymbol{1}$。则 $M$ 是 $P$ 在过 $O$、方向为 $\boldsymbol{1}$ 的直线上的正交投影，并且

$$
\lvert PM\rvert^2 = (x_1 - \bar x)^2 + \cdots + (x_n - \bar x)^2 = (n - 1)s^2.
$$
对给定的 $\bar x$ 与 $s^2$，$P$ 位于以 $M$ 为中心、维数为 $n - 1$ 的球面上，该球面在与直线 $OM$ 垂直的超平面内：偏差向量 $P - M$ 在一个 $(n-1)$ 维空间内变化，所以 $s^2$ 有 $n - 1$ 个自由度。

从代数上看，方差分析中的每个平方和是一个**二次型** $Q = \boldsymbol{Y}^{\mathsf T}A\boldsymbol{Y}$，其中 $A$ 对称，它的自由度是 $\operatorname{rank}(A)$。在方差分析中，每个这样的 $A$ 都是**正交投影矩阵**，而对投影矩阵，$\operatorname{rank}(A) = \operatorname{tr}(A)$。用于光滑器与带惩罚的拟合的一个更一般的定义，适用于方差为 $\sigma^2$ 的观测的任何线性拟合 $\hat{\boldsymbol{Y}} = C\boldsymbol{Y}$：

$$
\mathrm{df} = \frac{1}{\sigma^2}\sum_{i=1}^N\operatorname{Cov}(\hat Y_i, Y_i) = \operatorname{tr}(C),
$$
当 $C$ 是投影时，它化为秩。

### 3.4.2. 空间的分解

设 $\boldsymbol{y} \in \mathbb{R}^N$ 是全部观测构成的向量。在均值模型中，$\mathbb{E}[\boldsymbol{Y}] = X\boldsymbol{\beta}$ 位于示性矩阵 $X$ 的列空间 $\Omega$ 中，这是在每个组内为常数的向量构成的空间；$\dim\Omega = a$。在 $H_0$ 下，均值向量是 $\mu\boldsymbol{1}$，位于 $\omega = \operatorname{span}\{\boldsymbol{1}\}$ 中，$\dim\omega = 1$。设 $P_\Omega$ 与 $P_\omega$ 是向这两个空间的正交投影（[2.1.4](/2.1.4)）。则 $P_\Omega\boldsymbol{y} = \hat{\boldsymbol{y}}$ 是拟合值向量（每个分量换成它的组均值），$P_\omega\boldsymbol{y} = \bar y_{\cdot\cdot}\boldsymbol{1}$。空间分解为三个互相正交的子空间，

$$
\mathbb{R}^N = \omega \oplus (\Omega \ominus \omega) \oplus \Omega^{\perp},\qquad N = 1 + (a - 1) + (N - a),
$$
其中 $\Omega \ominus \omega$ 是 $\omega$ 在 $\Omega$ 中的正交补（在各组内为常数、且分量之和为零的向量），$\Omega^{\perp}$ 是残差空间。相应地，

$$
\boldsymbol{y} - \bar y_{\cdot\cdot}\boldsymbol{1} = (\hat{\boldsymbol{y}} - \bar y_{\cdot\cdot}\boldsymbol{1}) + (\boldsymbol{y} - \hat{\boldsymbol{y}}),\qquad \hat{\boldsymbol{y}} - \bar y_{\cdot\cdot}\boldsymbol{1} = (P_\Omega - P_\omega)\boldsymbol{y} \in \Omega \ominus \omega,\quad \boldsymbol{y} - \hat{\boldsymbol{y}} = (I - P_\Omega)\boldsymbol{y} \in \Omega^{\perp}.
$$
这两部分正交，勾股定理就是方差分析恒等式 (3.1)：

$$
\mathrm{SS}_{\mathrm{T}} = \lVert\boldsymbol{y} - \bar y_{\cdot\cdot}\boldsymbol{1}\rVert^2,\qquad \mathrm{SS}_{\mathrm{Tr}} = \lVert(P_\Omega - P_\omega)\boldsymbol{y}\rVert^2,\qquad \mathrm{SS}_{\mathrm{E}} = \lVert(I - P_\Omega)\boldsymbol{y}\rVert^2.
$$
投影矩阵 $P_\Omega - P_\omega$ 与 $I - P_\Omega$ 的秩（与迹）分别是 $a - 1$ 与 $N - a$：自由度就是向量所在子空间的维数。

![单因素方差分析的几何：观测向量 y，它在模型空间 Omega 上的投影 y-hat，以及两者在全 1 向量张成的直线 omega 上的投影。三条直角边的长度平方分别是 SS_T、SS_Tr 与 SS_E。](./plots/anova-geometry.py)

### 3.4.3. Cochran 定理

为什么 $\mathrm{SS}_{\mathrm{Tr}}$ 与 $\mathrm{SS}_{\mathrm{E}}$ 是独立的 $\chi^2$ 变量？若 $Z_1, \dots, Z_k$ 独立同服从 $\mathcal{N}(0, 1)$，则 $\sum_iZ_i^2 \sim \chi^2_k$。问题是：把 $\sum_iZ_i^2$ 分解为若干二次型，何时给出独立的 $\chi^2$ 部分。

**定理 3.4.1（Cochran 定理）** 设 $Z_1, \dots, Z_k$ 独立同服从 $\mathcal{N}(0, 1)$，$\boldsymbol{Z} = (Z_1, \dots, Z_k)^{\mathsf T}$，且

$$
\sum_{i=1}^k Z_i^2 = Q_1 + Q_2 + \cdots + Q_s,\qquad Q_j = \boldsymbol{Z}^{\mathsf T}A_j\boldsymbol{Z},
$$
其中 $s \le k$，每个 $A_j$ 对称且 $\operatorname{rank}(A_j) = k_j$。则 $Q_1, \dots, Q_s$ 是自由度分别为 $k_1, \dots, k_s$ 的独立 $\chi^2$ 随机变量，当且仅当

$$
k = k_1 + k_2 + \cdots + k_s.
$$

**证明**（概要）若各 $Q_j$ 是独立的 $\chi^2_{k_j}$，比较均值得 $k = \sum_j k_j$。反之，设 $\sum_jA_j = I_k$ 且 $\sum_j\operatorname{rank}(A_j) = k$。则各 $A_j$ 的列空间合起来张成 $\mathbb{R}^k$，维数之和为 $k$，所以 $\mathbb{R}^k$ 是它们的直和。对 $A_l$ 的列空间中的任何 $\boldsymbol{x}$，$\boldsymbol{x} = I\boldsymbol{x} = \sum_jA_j\boldsymbol{x}$，由直和分解的唯一性，必有 $A_l\boldsymbol{x} = \boldsymbol{x}$，且对 $j \ne l$，$A_j\boldsymbol{x} = \boldsymbol{0}$。因此每个 $A_j$ 幂等，且对 $j \ne l$ 有 $A_jA_l = O$：各 $A_j$ 是向互相正交的子空间的正交投影。选取适配于这些子空间的标准正交基，$Q_j$ 就是 $\boldsymbol{Z}$ 的某个正交变换的 $k_j$ 个坐标的平方和，这些坐标独立同服从 $\mathcal{N}(0, 1)$；所以各 $Q_j$ 是独立的 $\chi^2_{k_j}$。这个论证的幂等情形就是 [3.3.8](/3.3.8) 中关于二次型的引理。$\square$

**推论 3.4.1** 在 $H_0\colon \mu_1 = \cdots = \mu_a = \mu$ 下，变量 $Z_{ij} = (Y_{ij} - \mu)/\sigma$ 独立同服从 $\mathcal{N}(0, 1)$，并且

$$
\sum_{i,j}Z_{ij}^2 = \frac{N(\bar Y_{\cdot\cdot} - \mu)^2}{\sigma^2} + \frac{\mathrm{SS}_{\mathrm{Tr}}}{\sigma^2} + \frac{\mathrm{SS}_{\mathrm{E}}}{\sigma^2}
$$
是分解为秩为 $1$、$a - 1$、$N - a$ 的二次型，这三个秩之和为 $N$。因此 $\mathrm{SS}_{\mathrm{Tr}}/\sigma^2 \sim \chi^2_{a-1}$ 与 $\mathrm{SS}_{\mathrm{E}}/\sigma^2 \sim \chi^2_{N-a}$ 独立，这就证明了定理 3.3.2。（没有 $H_0$ 时，对 $(Y_{ij} - \mu_i)/\sigma$ 作同样的论证表明，总有 $\mathrm{SS}_{\mathrm{E}}/\sigma^2 \sim \chi^2_{N-a}$。）

这些秩就是 3.4.2 节中三个投影的秩，所以这个定理是正交分解的概率形式：正交的子空间承载各向同性正态向量的独立部分。这一事实是后面各章所有平衡设计中精确 $F$ 检验的基础。

## 3.5. 方差分析、回归、一般线性检验与似然比检验

### 3.5.1. 方差分析就是回归

3.2.2 节把两个方差分析模型都写成对示性变量的线性回归，所以方差分析就是回归，上面的方差分析表就是 [3.3.4](/3.3.4) 的回归方差分析表。区别在于模型所关注的东西。回归模型描述定量预测变量与响应之间的统计关系 $\mathbb{E}Y = f(X)$；方差分析不使用各水平的数值，甚至不使用它们的顺序，而是为每个水平单独估计一个均值。RF 功率 $160, \dots, 220\,\mathrm{W}$ 是数，对功率作一个斜率的回归用 $2$ 个均值参数，方差分析用 $4$ 个；回归可以在各设置之间内插，但如果关系不是线性的，它就会出错。当因子是定量的时，两种方法可以结合并比较，这将在 [3.8.5](/3.8.5) 中进行。

### 3.5.2. 作为一般线性检验的方差分析 F 检验

**一般线性检验**（[3.3.4](/3.3.4)）通过误差平方和，比较**完全模型**与施加 $H_0$ 得到的**简化模型**：

$$
F_0 = \frac{\bigl[\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F)\bigr]/(\mathrm{df}_R - \mathrm{df}_F)}{\mathrm{SS}_{\mathrm{E}}(F)/\mathrm{df}_F} \sim F_{\mathrm{df}_R - \mathrm{df}_F,\,\mathrm{df}_F}\quad\text{在 } H_0 \text{ 下}.
$$
这个检验最好看作是两个线性模型的比较：完全模型多出的结构使误差平方和减少的幅度，是否超出偶然所能解释的程度？例如在有四个预测变量的多元回归中，$H_0\colon \beta_1 = \beta_3 = 0$ 把完全模型 $y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \beta_3x_3 + \beta_4x_4 + \varepsilon$ 简化为 $y = \beta_0 + \beta_2x_2 + \beta_4x_4 + \varepsilon$；在 R 中这个比较是

```r
redmodel  <- lm(y ~ x2 + x4, data = gas)
fullmodel <- lm(y ~ x1 + x2 + x3 + x4, data = gas)
anova(redmodel, fullmodel)
```

```text
Analysis of Variance Table

Model 1: y ~ x2 + x4
Model 2: y ~ x1 + x2 + x3 + x4
  Res.Df    RSS Df Sum of Sq      F Pr(>F)
1     29 238.39                           
2     27 201.23  2    37.159 2.4929 0.1015
```

这里 $\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F) = 238.39 - 201.23 = 37.16$，自由度 $29 - 27 = 2$，$F_0 = (37.16/2)/(201.23/27) = 2.49$，$p = 0.10$：$x_1$ 与 $x_3$ 可以去掉。

对单因子实验，完全模型是 $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$，$H_0\colon \tau_1 = \cdots = \tau_a = 0$ 给出简化模型 $Y_{ij} = \mu + \varepsilon_{ij}$，它表示所有观测来自同一个组；简化模型只是陈述该假设的另一种方式。完全模型的误差平方和是 $\mathrm{SS}_{\mathrm{E}}(F) = \sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2 = \mathrm{SS}_{\mathrm{E}}$，自由度为 $N - a$；简化模型对每个观测都拟合 $\bar y_{\cdot\cdot}$，所以 $\mathrm{SS}_{\mathrm{E}}(R) = \sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2 = \mathrm{SS}_{\mathrm{T}}$，自由度为 $N - 1$。因此

$$
F_0 = \frac{(\mathrm{SS}_{\mathrm{T}} - \mathrm{SS}_{\mathrm{E}})/(a - 1)}{\mathrm{SS}_{\mathrm{E}}/(N - a)} = \frac{\mathrm{SS}_{\mathrm{Tr}}/(a - 1)}{\mathrm{SS}_{\mathrm{E}}/(N - a)},
$$
恰好就是方差分析的 $F$ 检验。从几何上看，$\mathrm{SS}_{\mathrm{E}}(R) = \lVert\boldsymbol{y} - P_\omega\boldsymbol{y}\rVert^2$，$\mathrm{SS}_{\mathrm{E}}(F) = \lVert\boldsymbol{y} - P_\Omega\boldsymbol{y}\rVert^2$，它们的差是 3.4.2 节的图中位于 $\Omega \ominus \omega$ 内那条边的长度平方。

在 R 中，同一个假设可以用 `car` 包的 `linearHypothesis` 写成对任一种参数化的系数的线性约束。在均值模型中，假设 $\mu_1 = \mu_2 = \mu_3 = \mu_4$ 由三个线性无关的约束构成：

```r
fit <- lm(rate ~ 0 + RF, data = etch.rate)          # means model
library(car)
linearHypothesis(fit, c("RF160-RF180", "RF180-RF200", "RF200-RF220"))
# or with an explicit restriction matrix
conmat <- matrix(0, nrow = 3, ncol = 4)
conmat[, 1] <- 1; conmat[1, 2] <- conmat[2, 3] <- conmat[3, 4] <- -1
linearHypothesis(fit, conmat)
```

```text
> conmat
     [,1] [,2] [,3] [,4]
[1,]    1   -1    0    0
[2,]    1    0   -1    0
[3,]    1    0    0   -1

Linear hypothesis test

Hypothesis:
RF160 - RF180 = 0
RF160 - RF200 = 0
RF160 - RF220 = 0

Model 1: restricted model
Model 2: rate ~ 0 + RF

  Res.Df   RSS Df Sum of Sq      F    Pr(>F)    
1     19 72210                                  
2     16  5339  3     66871 66.797 2.883e-09 ***
```

受限模型的 $\mathrm{RSS} = \mathrm{SS}_{\mathrm{T}} = 72210$，自由度 $19$，均值模型的 $\mathrm{SS}_{\mathrm{E}} = 5339$，自由度 $16$，差 $66871$，自由度 $3$，就是 $\mathrm{SS}_{\mathrm{Tr}}$：结果与 3.3.4 节的 `anova(fit1)` 一致。采用 R 的默认编码（`fit1 <- lm(rate ~ RF)`，系数为 `(Intercept)`、`RF180`、`RF200`、`RF220`）时，同一个假设就是与第一个水平的三个差都为零：

```r
linearHypothesis(fit1, c("RF180 = 0", "RF200 = 0", "RF220 = 0"))
# or
conmat <- matrix(0, nrow = 3, ncol = 4)
conmat[1, 2] <- conmat[2, 3] <- conmat[3, 4] <- 1
linearHypothesis(fit1, conmat)
```

只要定义的是同一个简化模型，写出哪些约束并不重要。一般线性检验也是理论得以推广的方式：对于两个因子、区组或协变量，方差分析表中的每个 $F$ 检验都是一个模型与一个子模型的比较（[3.3.9](/3.3.9)）。

### 3.5.3. 一般线性模型

本章的模型、[3.8.2](/3.8.2) 的对比实验以及回归课程的模型，都是同一个模型的实例。

**定义 3.5.1（一般线性模型）** **一般线性模型**是

$$
\boldsymbol{Y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon},\qquad \boldsymbol{\varepsilon} \sim \mathcal{N}_N(\boldsymbol{0}, \sigma^2 I_N),
$$
其中 $X$ 是已知的 $N \times p$ 矩阵，其列可以是定量预测变量、因子水平的示性变量或两者兼有，$\boldsymbol{\beta}$ 是未知的参数向量。

单样本 $z$ 检验与 $t$ 检验（$X = \boldsymbol{1}$）、两样本 $t$ 检验（两个示性列）、单因素与多因素方差分析、线性回归以及协方差分析都是它的特例，它们对线性假设的检验都是一般线性检验。不要把这个名称与**广义线性模型**（[3.3.6](/3.3.6)）混淆，后者允许非正态的响应（二项、Poisson）以及均值与线性预测量之间的联系函数。

### 3.5.4. 与似然比检验的等价性

正态一般线性模型中线性假设的 $F$ 检验，总是与**似然比检验**（[3.2.5](/3.2.5)）等价。先考虑简单线性回归 $Y_i = \beta_0 + \beta_1x_i + \varepsilon_i$ 中的 $H_0\colon \beta_1 = 0$。完全模型中的极大似然估计是 $\hat{\boldsymbol\theta} = (b_0, b_1, s^2)$，其中 $s^2 = \sum_i(y_i - b_0 - b_1x_i)^2/n$，简化模型中是 $\hat{\boldsymbol\theta}_0 = (\bar y, 0, s_Y^2)$，其中 $s_Y^2 = \sum_i(y_i - \bar y)^2/n$。在方差的极大似然估计处取值的正态似然是 $(2\pi\hat\sigma^2)^{-n/2}\mathrm{e}^{-n/2}$，所以

$$
\Lambda = \frac{L(\hat{\boldsymbol\theta}_0)}{L(\hat{\boldsymbol\theta})} = \Bigl(\frac{s^2}{s_Y^2}\Bigr)^{n/2},\qquad -2\log\Lambda = n\log\frac{s_Y^2}{s^2}.
$$
由于 $s_Y^2/s^2 = \mathrm{SST}/\mathrm{SSE} = 1 + \mathrm{SSR}/\mathrm{SSE} = 1 + F/(n - 2)$，

$$
-2\log\Lambda = n\log\Bigl(1 + \frac{F}{n - 2}\Bigr),
$$
这是 $F$ 的严格增函数。**Wilks 定理**给出 $-2\log\Lambda \to \chi^2_1$（依分布），但 $F$ 的精确分布使这一近似成为不必要：$-2\log\Lambda$ 大时拒绝与 $F$ 大时拒绝是一回事，而 $F$ 分布给出精确的临界值。

同样的计算适用于单因素方差分析。$\sigma^2$ 的极大似然估计在完全模型中是 $\mathrm{SS}_{\mathrm{E}}/N$，在简化模型 $Y_{ij} = \mu + \varepsilon_{ij}$ 中是 $\mathrm{SS}_{\mathrm{T}}/N$，所以

$$
-2\log\Lambda = N\log\frac{\mathrm{SS}_{\mathrm{T}}}{\mathrm{SS}_{\mathrm{E}}} = N\log\Bigl(1 + \frac{a - 1}{N - a}F_0\Bigr),
$$
同样是 $F_0$ 的单调函数。对刻蚀数据，$-2\log\Lambda = 20\log(72209.75/5339.2) = 52.1$。似然比检验、一般线性检验与方差分析的 $F$ 检验，是同一个步骤的三种推导。

## 小结

完全随机化设计（定义 3.1.1）的单因子方差分析，模型为 $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$，$\varepsilon_{ij} \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$：

| 来源 | SS | df | MS | $\mathbb{E}[\mathrm{MS}]$ | $F_0$ |
|---|---|---|---|---|---|
| 处理 | $\sum_i n_i(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2 = \sum_i\frac{y_{i\cdot}^2}{n_i} - \frac{y_{\cdot\cdot}^2}{N}$ | $a - 1$ | $\mathrm{SS}_{\mathrm{Tr}}/(a - 1)$ | $\sigma^2 + \frac{\sum_i n_i\tau_i^2}{a - 1}$ | $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}} \overset{H_0}{\sim} F_{a-1,N-a}$ |
| 误差 | $\sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2 = \mathrm{SS}_{\mathrm{T}} - \mathrm{SS}_{\mathrm{Tr}}$ | $N - a$ | $\mathrm{SS}_{\mathrm{E}}/(N - a)$ | $\sigma^2$ | |
| 总计 | $\sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2 = \sum_{i,j}y_{ij}^2 - \frac{y_{\cdot\cdot}^2}{N}$ | $N - 1$ | | | |

- 估计（命题 3.2.1）：$\hat\mu_i = \bar y_{i\cdot}$，$\hat\tau_i = \bar y_{i\cdot} - \bar y_{\cdot\cdot}$（平衡时），$\hat\sigma^2 = \mathrm{MS}_{\mathrm{E}}$；区间使用 $t_{N-a,\alpha/2}$ 与 $\mathrm{MS}_{\mathrm{E}}$。
- 期望均方（定理 3.3.1）解释了上侧 $F$ 检验（定理 3.3.2）；$F_0$ 随各水平均值的离散程度与 $n_i$ 增大，随组内散布减小。
- 几何：$\mathbb{R}^N = \omega \oplus (\Omega \ominus \omega) \oplus \Omega^{\perp}$，维数为 $1$、$a - 1$、$N - a$；平方和是投影的长度平方，自由度是维数，Cochran 定理（定理 3.4.1）把正交性转化为 $\chi^2$ 各部分的独立性。
- 一个检验，四种名称：

| 视角 | 完全模型 / 统计量 | 简化模型 | 等价关系 |
|---|---|---|---|
| 方差分析 | $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}$ | — | 定义 |
| 回归 | 对 $a - 1$ 个示性变量回归的整体 $F$ | 仅含截距 | 同一张表 |
| 一般线性检验 | $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$，$\mathrm{SS}_{\mathrm{E}}(F) = \mathrm{SS}_{\mathrm{E}}$ | $Y_{ij} = \mu + \varepsilon_{ij}$，$\mathrm{SS}_{\mathrm{E}}(R) = \mathrm{SS}_{\mathrm{T}}$ | $\mathrm{SS}_{\mathrm{E}}(R) - \mathrm{SS}_{\mathrm{E}}(F) = \mathrm{SS}_{\mathrm{Tr}}$ |
| 似然比检验 | $-2\log\Lambda = N\log(\mathrm{SS}_{\mathrm{T}}/\mathrm{SS}_{\mathrm{E}})$ | | 是 $F_0$ 的单调函数 |

- 方差分析是一般线性模型（定义 3.5.1）的特例；与对定量因子的回归不同，它忽略各水平的数值。

## 思考题

1. 补全下面平衡单因子实验的方差分析表，并给出 $p$ 值的范围。

   | 来源 | SS | df | MS | $F_0$ |
   |---|---|---|---|---|
   | 因子 | ? | ? | 14.0 | ? |
   | 误差 | 30.0 | ? | ? | |
   | 总计 | 72.0 | 23 | | |

   **答** $\mathrm{SS}_{\mathrm{Tr}} = 72.0 - 30.0 = 42.0$，所以 $a - 1 = 42.0/14.0 = 3$，$a = 4$，$N - a = 23 - 3 = 20$（因此 $n = 6$）。于是 $\mathrm{MS}_{\mathrm{E}} = 30.0/20 = 1.5$，$F_0 = 14.0/1.5 = 9.33$。由于 $F_{3,20,0.01} = 4.94$，$F_{3,20,0.001} = 8.10$，所以 $p < 0.001$（精确值 $p = 4.6\times10^{-4}$）。

2. 三种药物各给 $n = 7$ 名患者服用，得分越高越好。样本均值为 $5.54$、$5.03$ 与 $5.93$，合并的组内方差为 $\mathrm{MS}_{\mathrm{E}} = 0.25$。构造方差分析表，并在 $\alpha = 0.05$ 下检验各均值是否相等。

   **答** $N = 21$，$\bar y_{\cdot\cdot} = (5.54 + 5.03 + 5.93)/3 = 5.50$。$\mathrm{SS}_{\mathrm{Tr}} = 7\bigl(0.04^2 + 0.47^2 + 0.43^2\bigr) = 7 \times 0.4074 = 2.852$，自由度 $2$，$\mathrm{MS}_{\mathrm{Tr}} = 1.426$；$\mathrm{SS}_{\mathrm{E}} = 18 \times 0.25 = 4.50$，自由度 $18$；$\mathrm{SS}_{\mathrm{T}} = 7.352$，自由度 $20$。$F_0 = 1.426/0.25 = 5.70 > F_{2,18,0.05} = 3.55$，$p = 0.012$：平均得分有差异。注意，这张表可以仅由汇总统计量构造：均值给出 $\mathrm{SS}_{\mathrm{Tr}}$，$\mathrm{MS}_{\mathrm{E}}$ 给出 $\mathrm{SS}_{\mathrm{E}}$。

3. 证明当 $a = 2$ 时，方差分析统计量等于合并两样本 $t$ 统计量的平方，$F_0 = t_0^2$，并且这两个检验是同一个检验。

   **答** 当 $a = 2$ 时，$\bar y_{\cdot\cdot} = (n_1\bar y_{1\cdot} + n_2\bar y_{2\cdot})/N$，所以 $\bar y_{1\cdot} - \bar y_{\cdot\cdot} = \frac{n_2}{N}(\bar y_{1\cdot} - \bar y_{2\cdot})$，$\bar y_{2\cdot} - \bar y_{\cdot\cdot} = -\frac{n_1}{N}(\bar y_{1\cdot} - \bar y_{2\cdot})$。因此
   $$
   \mathrm{SS}_{\mathrm{Tr}} = \frac{n_1n_2^2 + n_2n_1^2}{N^2}(\bar y_{1\cdot} - \bar y_{2\cdot})^2 = \frac{(\bar y_{1\cdot} - \bar y_{2\cdot})^2}{1/n_1 + 1/n_2}.
   $$
   $\mathrm{MS}_{\mathrm{E}} = \mathrm{SS}_{\mathrm{E}}/(N - 2) = s_p^2$，所以 $F_0 = \mathrm{SS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}} = (\bar y_{1\cdot} - \bar y_{2\cdot})^2/\bigl(s_p^2(1/n_1 + 1/n_2)\bigr) = t_0^2$。由于 $t_{N-2}^2 \sim F_{1,N-2}$ 且 $F_{1,N-2,\alpha} = t_{N-2,\alpha/2}^2$，当 $F_0 > F_{1,N-2,\alpha}$ 时拒绝与当 $\lvert t_0\rvert > t_{N-2,\alpha/2}$ 时拒绝是一回事。

4. 在单因子实验的一般线性检验中，量 $\sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2$、$\sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2$ 与 $\sum_i n(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2$ 中，哪个是完全模型的误差平方和，哪个是简化模型的？

   **答** 完全模型 $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$ 拟合 $\bar y_{i\cdot}$，所以它的误差平方和是 $\sum_{i,j}(y_{ij} - \bar y_{i\cdot})^2 = \mathrm{SS}_{\mathrm{E}}$。简化模型 $Y_{ij} = \mu + \varepsilon_{ij}$ 拟合 $\bar y_{\cdot\cdot}$，所以它的误差平方和是 $\sum_{i,j}(y_{ij} - \bar y_{\cdot\cdot})^2 = \mathrm{SS}_{\mathrm{T}}$。第三个量 $\mathrm{SS}_{\mathrm{Tr}}$ 是两者之差，即因子所带来的误差减少量。

5. 两个实验各比较五个水平，样本量相同，水平均值的离散程度也相同。在实验 A 中，每个水平内的观测紧密聚集；在实验 B 中，它们变化很大。哪个实验中因子效应更显著？如果两个实验的均值相同、组内散布也相同，但实验 C 每个水平有 $3$ 个观测，实验 D 有 $300$ 个，又如何？

   **答** 实验 A：$\mathrm{SS}_{\mathrm{Tr}}$ 相同时，较小的 $\mathrm{SS}_{\mathrm{E}}$ 给出较大的 $F_0$。实验 D：$\mathrm{SS}_{\mathrm{Tr}} = \sum_i n(\bar y_{i\cdot} - \bar y_{\cdot\cdot})^2$ 大 $100$ 倍，$\mathrm{MS}_{\mathrm{E}}$ 估计同样的 $\sigma^2$，所以 $F_0$ 大约大 $100$ 倍，误差自由度也更大。显著性取决于水平均值的方差 $\sigma^2/n$，而不取决于箱线图中看到的观测值的散布。

6. 通过只用水平均值 $\bar Y_{i\cdot}$ 表示 $\mathrm{SS}_{\mathrm{Tr}}$，证明在平衡实验中 $\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}] = \sigma^2 + n\sum_i\tau_i^2/(a - 1)$。

   **答** $\bar Y_{i\cdot} \sim \mathcal{N}(\mu + \tau_i, \sigma^2/n)$ 相互独立，且 $\mathrm{SS}_{\mathrm{Tr}} = n\sum_i(\bar Y_{i\cdot} - \bar{\bar Y})^2$，其中 $\bar{\bar Y} = \frac1a\sum_i\bar Y_{i\cdot} = \bar Y_{\cdot\cdot}$。对均值为 $\theta_i$、方差同为 $v$ 的独立 $W_i$，$\mathbb{E}\sum_i(W_i - \bar W)^2 = \sum_i(\theta_i - \bar\theta)^2 + (a - 1)v$。取 $W_i = \bar Y_{i\cdot}$，则 $\theta_i - \bar\theta = \tau_i$（因为 $\sum_i\tau_i = 0$），$v = \sigma^2/n$，所以 $\mathbb{E}[\mathrm{SS}_{\mathrm{Tr}}] = n\sum_i\tau_i^2 + (a - 1)\sigma^2$。

7. 证明单因素方差分析的 $-2\log\Lambda$ 是 $N\log\bigl(1 + \frac{a-1}{N-a}F_0\bigr)$，并对刻蚀数据比较基于 Wilks 定理的似然比检验与 $F$ 检验。

   **答** $\mathrm{SS}_{\mathrm{T}}/\mathrm{SS}_{\mathrm{E}} = 1 + \mathrm{SS}_{\mathrm{Tr}}/\mathrm{SS}_{\mathrm{E}} = 1 + \frac{(a-1)\mathrm{MS}_{\mathrm{Tr}}}{(N-a)\mathrm{MS}_{\mathrm{E}}}$，而 $-2\log\Lambda = N\log(\mathrm{SS}_{\mathrm{T}}/\mathrm{SS}_{\mathrm{E}})$（3.5.4 节）。对刻蚀数据，$-2\log\Lambda = 20\log(1 + \frac{3}{16}\times 66.80) = 52.1$，与 $\chi^2_3$ 比较，$p \approx 3\times10^{-11}$，小于 $F$ 检验的精确值 $p = 2.9\times10^{-9}$。两者都拒绝；对 $N = 20$ 而言，渐近的 $\chi^2$ 校准过于宽松，这就是要采用精确 $F$ 分布的原因。
