---
title: 随机区组设计
description: 分区组原理与随机区组设计；可加的区组模型、最小二乘估计、期望均方与血管移植物例的方差分析；是否检验区组、残差分析与多重比较；相对于完全随机化设计的相对效率；随机区组；缺失值；有重复的广义完全区组设计、以区组与处理的交互效应作误差项，以及混合模型。
source_hash: b5f96921372f
---

在 [3.8.2](/3.8.2) 的实验设计三项基本原则中，随机化与重复在此前的每一章里都已发挥作用；本章讨论第三项原则，**分区组**。许多实验的材料并不均匀：不同批次的原料、试样、田块、日期、操作员。如果把实验单位完全随机地分配给各个处理，批次或日期之间的差异就会进入误差，掩盖处理效应。分区组在相似单位构成的组内比较处理，从而把这些差异从误差中扣除。最简单的分区组设计是随机区组设计，它在 [3.8.6](/3.8.6) 中作为**可加模型**的一个例子引入；这里把它完整地展开：模型与方差分析、是否应检验区组的问题、多重比较、它相对于完全随机化设计的效率、随机区组、缺失观测，以及推广到每个区组含有各处理多次重复的情形，这引出本课程中的第一个混合模型。下一章 [3.8.8](/3.8.8) 用拉丁方同时控制两个干扰因子。

记号沿用 [3.8.3](/3.8.3) 与 [3.8.6](/3.8.6)：$a$ 个处理以 $i$ 编号，$b$ 个区组以 $j$ 编号，共 $N=ab$ 个观测，圆点表示求和，横线表示平均，模型中写 $Y_{ij}$，数据中写 $y_{ij}$。所有分位数都是上分位数：$F_{\nu_1,\nu_2,\alpha}$ 是其上方概率为 $\alpha$ 的点。

## 7.1. 分区组原理

### 7.1.1. 干扰因子

回忆 [3.8.2](/3.8.2) 的定义 2.1.4，**干扰因子**是可能影响响应、但实验者并不感兴趣的因子。典型的例子有原料批次、操作员、试验设备、时间（班次、日期），以及单位本身不均匀时的实验单位。在模型 $y=\mu+\varepsilon$，$\varepsilon\sim\mathcal{N}(0,\sigma^2)$ 中，未被考虑的干扰因子的效应是 $\sigma^2$，即未被解释的变异的一部分；工业上的许多实验都涉及分区组以减小它，或者本应如此。不分区组是实验设计中最常见的缺陷之一。

分区组起源于农业田间试验。要比较若干作物品种（或肥料的若干水平），人们取一块土地，把它划分为小区，再把品种随机分配到小区上。然而小区数量一多，往往变得很不均匀：肥力、湿度与排水沿田块变化，在完全随机的分配下，某些品种会偶然落在较好的土壤上。补救的办法是把相邻、相似的小区组成**区组**，并在每个区组内比较所有品种。一般地，区组是一组同质的实验单位，通常对应于干扰因子的一个水平：一个批次、一天、一条地带。

### 7.1.2. 如何处理干扰变量

用哪种技术处理干扰变量，取决于两个问题：变异的来源是否已知，是否可以控制？

| 干扰变量 | 技术 | 做法 |
|---|---|---|
| 已知且可控 | 分区组 | 在该变量的每个水平内运行所有处理（区组也可以是几个变量的组合，如"机器与日期"） |
| 已知、可测量但不可控 | **协方差分析** | 对每个单位测量该变量（协变量），用回归除去它的效应 |
| 未知且不可控 | **随机化** | 该变量成为**潜伏变量**；随机分配使其效应平均地在各处理间平衡 |

这些原则合起来就是 [3.8.2](/3.8.2) 的规则：能分区组的就分区组，不能的就随机化。分区组并不取代随机化；在每个区组内，处理仍然是随机分配的。

## 7.2. 随机区组设计

### 7.2.1. 硬度测试例

我们想知道，四种压头在洛氏硬度计上给出的平均硬度读数是否不同。机器把压头压入金属试片，硬度由压痕的深度读出。完全随机化设计会把每种压头随机地分配给若干试片。但试片可能来自不同炉次的金属，硬度各不相同；这种变异会进入误差，模糊压头之间的比较。由于每个试片足够大，可以做四次测试，更好的设计是在每个试片上测试全部四种压头：每个试片是一个区组，在一个试片内，各压头的测试顺序是随机的。取 $b=4$ 个试片，一种可能的随机化是

| 试片 1 | 试片 2 | 试片 3 | 试片 4 |
|---|---|---|---|
| 压头 3 | 压头 3 | 压头 2 | 压头 1 |
| 压头 1 | 压头 4 | 压头 1 | 压头 4 |
| 压头 4 | 压头 2 | 压头 3 | 压头 2 |
| 压头 2 | 压头 1 | 压头 4 | 压头 3 |

该实验具有双向结构，即处理乘区组，其定义性的特征是每个区组恰好见到每个处理一次。区组之间的变异可以很大，但区组内部的变异应当相对较小，处理是在区组内部比较的。区组是对随机化的一种限制：一个区组内的所有试验是随机化的，跨区组则不是。每个区组含有基本实验的一次完整重复，所以区组大小等于处理数。

**定义 7.2.1（随机区组设计）** 在有 $a$ 个处理与 $b$ 个区组的**随机区组设计**（RCBD）中，每个区组由 $a$ 个实验单位构成，每个处理在每个区组中恰好施加于一个单位，处理在每个区组内被分别、独立地随机分配给单位。共有 $(a!)^b$ 种等可能的随机化。

用因果推断的术语，RCBD 是每层恰含每个处理一个单位的[分层随机化实验](/3.9.2#def-2.4.7)；[3.8.2](/3.8.2) 的**配对设计**就是 $a=2$ 的 RCBD（7.3.6 节）。

### 7.2.2. 模型

**定义 7.2.2（RCBD 的效应模型）** 随机区组设计的效应模型是

$$
Y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij},\qquad i=1,\dots,a,\quad j=1,\dots,b,\qquad \sum_{i=1}^a\tau_i=0,\quad \sum_{j=1}^b\beta_j=0,
$$
其中 $\mu$ 是总均值，$\tau_i$ 是第 $i$ 个处理的效应，$\beta_j$ 是第 $j$ 个区组的效应，误差 $\varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$。

这是 [3.8.6](/3.8.6) 定义 6.4.1 的可加模型，处理因子对应 $\tau_i$，区组因子对应 $\beta_j$；与所有方差分析模型一样，它是**一般线性模型**：对处理与区组的指示变量作线性回归。它关于处理与区组没有交互效应的假定是一个设计假定：处理效应在每个区组中都相同，误差项反映处理之间的差异随区组而变化的程度。处理均值为 $\mu_i=\mu+\tau_i$，感兴趣的假设是

$$
H_0\colon\tau_1=\tau_2=\cdots=\tau_a=0\qquad\text{versus}\qquad H_1\colon\tau_i\ne0\ \text{for at least one }i,
$$
等价于 $H_0\colon\mu_1=\cdots=\mu_a$。区组进入模型只是为了除去它们的变异。

### 7.2.3. 最小二乘估计

**命题 7.2.1** 在约束 $\sum_i\tau_i=\sum_j\beta_j=0$ 下，RCBD 模型的最小二乘估计是

$$
\hat\mu=\bar y_{\cdot\cdot},\qquad \hat\tau_i=\bar y_{i\cdot}-\bar y_{\cdot\cdot},\qquad \hat\beta_j=\bar y_{\cdot j}-\bar y_{\cdot\cdot},
$$
拟合值为 $\hat y_{ij}=\bar y_{i\cdot}+\bar y_{\cdot j}-\bar y_{\cdot\cdot}$，残差为 $e_{ij}=y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot}$。

**证明** 极小化 $L=\sum_{i,j}(y_{ij}-\mu-\tau_i-\beta_j)^2$。令对 $\mu$、$\tau_i$、$\beta_j$ 的导数为零，得正规方程

$$
ab\,\mu+b\sum_i\tau_i+a\sum_j\beta_j=y_{\cdot\cdot},\qquad b\mu+b\tau_i+\sum_j\beta_j=y_{i\cdot},\qquad a\mu+\sum_i\tau_i+a\beta_j=y_{\cdot j}.
$$
这 $1+a+b$ 个方程的秩为 $a+b-1$（处理方程之和与区组方程之和都等于第一个方程），所以需要两个约束。取 $\sum_i\tau_i=\sum_j\beta_j=0$，第一个方程给出 $\hat\mu=\bar y_{\cdot\cdot}$，第二个给出 $\hat\tau_i=\bar y_{i\cdot}-\hat\mu$，第三个给出 $\hat\beta_j=\bar y_{\cdot j}-\hat\mu$。因为 $L$ 是凸二次函数，这个解就是极小点。$\square$

每个区组恰含每个处理一次，所以处理与区组的指示变量列在中心化后正交：$\hat\tau_i$ 不依赖于区组，$\hat\beta_j$ 不依赖于处理。处理均值的对比 $\sum_ic_i\mu_i$（$\sum_ic_i=0$）由 $\sum_ic_i\bar y_{i\cdot}$ 估计，其中区组效应相互抵消，方差为 $\sigma^2\sum_ic_i^2/b$。特别地，$\operatorname{Var}(\bar Y_{i\cdot}-\bar Y_{k\cdot})=2\sigma^2/b$。

## 7.3. 方差分析

### 7.3.1. 总平方和的分解

把 $y_{ij}-\bar y_{\cdot\cdot}$ 写成 $(\bar y_{i\cdot}-\bar y_{\cdot\cdot})+(\bar y_{\cdot j}-\bar y_{\cdot\cdot})+(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})$，平方后求和，交叉项都消失（每一项都是行模式、列模式与双重中心化数组的乘积之和），得

$$
\underbrace{\sum_{i=1}^a\sum_{j=1}^b(y_{ij}-\bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{T}}}
=\underbrace{b\sum_{i=1}^a(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{Tr}}}
+\underbrace{a\sum_{j=1}^b(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{Blocks}}}
+\underbrace{\sum_{i=1}^a\sum_{j=1}^b(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2}_{\mathrm{SS}_{\mathrm{E}}},
$$
即 $\mathrm{SS}_{\mathrm{T}}=\sum_{i,j}(y_{ij}-\hat\mu)^2$，$\mathrm{SS}_{\mathrm{Tr}}=b\sum_i\hat\tau_i^2$，$\mathrm{SS}_{\mathrm{Blocks}}=a\sum_j\hat\beta_j^2$，$\mathrm{SS}_{\mathrm{E}}=\sum_{i,j}(y_{ij}-\hat\mu-\hat\tau_i-\hat\beta_j)^2$。自由度以同样的方式分解，

$$
ab-1=(a-1)+(b-1)+(a-1)(b-1).
$$
手算时用总和：

$$
\mathrm{SS}_{\mathrm{T}}=\sum_{i,j}y_{ij}^2-\frac{y_{\cdot\cdot}^2}{N},\qquad \mathrm{SS}_{\mathrm{Tr}}=\frac1b\sum_iy_{i\cdot}^2-\frac{y_{\cdot\cdot}^2}{N},\qquad \mathrm{SS}_{\mathrm{Blocks}}=\frac1a\sum_jy_{\cdot j}^2-\frac{y_{\cdot\cdot}^2}{N},
$$
误差平方和由相减得到，$\mathrm{SS}_{\mathrm{E}}=\mathrm{SS}_{\mathrm{T}}-\mathrm{SS}_{\mathrm{Tr}}-\mathrm{SS}_{\mathrm{Blocks}}$。

与 [3.8.3](/3.8.3) 对同样 $N$ 个观测所作的单因素方差分析相比，处理平方和不变，而单因素的误差平方和 $\mathrm{SS}_{\mathrm{Blocks}}+\mathrm{SS}_{\mathrm{E}}$（自由度 $a(b-1)$）被分成区组引起的部分（自由度 $b-1$）与残差。

### 7.3.2. 期望均方与 F 检验

**定理 7.3.1** 在处理效应与区组效应都固定的 RCBD 模型中，

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+\frac{b\sum_{i=1}^a\tau_i^2}{a-1},\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{Blocks}}]=\sigma^2+\frac{a\sum_{j=1}^b\beta_j^2}{b-1},\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2,
$$
其中 $\mathrm{MS}_{\mathrm{Tr}}=\mathrm{SS}_{\mathrm{Tr}}/(a-1)$，$\mathrm{MS}_{\mathrm{Blocks}}=\mathrm{SS}_{\mathrm{Blocks}}/(b-1)$，$\mathrm{MS}_{\mathrm{E}}=\mathrm{SS}_{\mathrm{E}}/[(a-1)(b-1)]$。而且 $\mathrm{SS}_{\mathrm{Tr}}$、$\mathrm{SS}_{\mathrm{Blocks}}$ 与 $\mathrm{SS}_{\mathrm{E}}$ 相互独立，$\mathrm{SS}_{\mathrm{E}}/\sigma^2\sim\chi^2_{(a-1)(b-1)}$，在 $H_0\colon\tau_1=\cdots=\tau_a=0$ 下 $\mathrm{SS}_{\mathrm{Tr}}/\sigma^2\sim\chi^2_{a-1}$，从而

$$
F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\ \overset{H_0}{\sim}\ F_{a-1,(a-1)(b-1)} .
$$

**证明** 代入模型，$\bar Y_{i\cdot}-\bar Y_{\cdot\cdot}=\tau_i+(\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot\cdot})$，因为区组效应在每个处理均值中都平均为 $\bar\beta=0$。$\bar\varepsilon_{i\cdot}$ 是独立的 $\mathcal{N}(0,\sigma^2/b)$，所以 $\mathbb{E}\sum_i(\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot\cdot})^2=(a-1)\sigma^2/b$，交叉项的期望为零，于是 $\mathbb{E}[\mathrm{SS}_{\mathrm{Tr}}]=b\sum_i\tau_i^2+(a-1)\sigma^2$。区组均方的处理方式相同。残差是 $Y_{ij}-\bar Y_{i\cdot}-\bar Y_{\cdot j}+\bar Y_{\cdot\cdot}=\varepsilon_{ij}-\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot j}+\bar\varepsilon_{\cdot\cdot}$，不含任何参数。在 $\mathbb{R}^{ab}$ 中，$\boldsymbol{\varepsilon}$ 的四个分量，即总均值、行效应、列效应与双重中心化的残差，是它在维数分别为 $1$、$a-1$、$b-1$ 与 $(a-1)(b-1)$ 的子空间上的正交投影。由 **Cochran 定理**（[3.8.3](/3.8.3)），各分量的平方长度除以 $\sigma^2$ 是自由度如上的独立 $\chi^2$ 变量（当效应不为零时，处理与区组分量是非中心的），这就给出全部结论。$\square$

在 $H_0$ 下，$\mathrm{MS}_{\mathrm{Tr}}$ 与 $\mathrm{MS}_{\mathrm{E}}$ 都估计 $\sigma^2$；在 $H_1$ 下处理均方更大。当 $F_0>F_{a-1,(a-1)(b-1),\alpha}$ 时拒绝 $H_0$。分析归结为方差分析表：

| 来源 | 平方和 | 自由度 | 均方 | $\mathbb{E}[\mathrm{MS}]$ | $F_0$ |
|---|---|---|---|---|---|
| 处理 | $\mathrm{SS}_{\mathrm{Tr}}$ | $a-1$ | $\mathrm{SS}_{\mathrm{Tr}}/(a-1)$ | $\sigma^2+\frac{b\sum\tau_i^2}{a-1}$ | $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}$ |
| 区组 | $\mathrm{SS}_{\mathrm{Blocks}}$ | $b-1$ | $\mathrm{SS}_{\mathrm{Blocks}}/(b-1)$ | $\sigma^2+\frac{a\sum\beta_j^2}{b-1}$ | |
| 误差 | $\mathrm{SS}_{\mathrm{E}}$ | $(a-1)(b-1)$ | $\mathrm{SS}_{\mathrm{E}}/[(a-1)(b-1)]$ | $\sigma^2$ | |
| 总计 | $\mathrm{SS}_{\mathrm{T}}$ | $N-1$ | | | |

### 7.3.3. 例：血管移植物实验

**例 7.3.1** 一家医疗器械制造商生产血管移植物（人造血管），做法是把聚四氟乙烯树脂与润滑剂混合后的坯料挤出成管。有些管子的外表面带有小而硬的凸起，称为毛刺（flick），这是产品被拒收的原因之一。产品工程师怀疑挤出压力会影响毛刺的出现，打算研究四种压力：$8500$、$8700$、$8900$ 与 $9100\,\mathrm{psi}$。树脂是分批生产的，批次之间可能有显著差异。响应是产率，即一次生产运行中不含毛刺的管子所占的百分比。每批树脂足够做四次生产运行，所以工程师在六个批次中的每一批上以随机顺序运行全部四种压力：这是 $a=4$ 个处理、$b=6$ 个区组的 RCBD。

| 压力（psi） | 批次 1 | 2 | 3 | 4 | 5 | 6 | $y_{i\cdot}$ | $\bar y_{i\cdot}$ |
|---|---|---|---|---|---|---|---|---|
| 8500 | 90.3 | 89.2 | 98.2 | 93.9 | 87.4 | 97.9 | 556.9 | 92.82 |
| 8700 | 92.5 | 89.5 | 90.6 | 94.7 | 87.0 | 95.8 | 550.1 | 91.68 |
| 8900 | 85.5 | 90.8 | 89.6 | 86.2 | 88.0 | 93.4 | 533.5 | 88.92 |
| 9100 | 82.5 | 89.5 | 85.6 | 87.4 | 78.9 | 90.7 | 514.6 | 85.77 |
| $y_{\cdot j}$ | 350.8 | 359.0 | 364.0 | 362.2 | 341.3 | 377.8 | $y_{\cdot\cdot}=2155.1$ | |

由 $\sum y_{ij}^2=193999.31$ 与 $y_{\cdot\cdot}^2/N=2155.1^2/24=193519.00$，

$$
\begin{aligned}
\mathrm{SS}_{\mathrm{T}}&=193999.31-193519.00=480.31,\\
\mathrm{SS}_{\mathrm{Tr}}&=\tfrac16(556.9^2+550.1^2+533.5^2+514.6^2)-193519.00=178.17,\\
\mathrm{SS}_{\mathrm{Blocks}}&=\tfrac14(350.8^2+359.0^2+\cdots+377.8^2)-193519.00=192.25,\\
\mathrm{SS}_{\mathrm{E}}&=480.31-178.17-192.25=109.89 .
\end{aligned}
$$
在 R 中，数据框有 `PSI`、`Block` 与 `Yield` 三列，前两列是因子，公式 `Yield ~ .` 把所有其他列作为可加项：

```r
graft <- data.frame(
  PSI   = factor(rep(c(8500, 8700, 8900, 9100), each = 6)),
  Block = factor(rep(1:6, times = 4)),
  Yield = c(90.3, 89.2, 98.2, 93.9, 87.4, 97.9,
            92.5, 89.5, 90.6, 94.7, 87.0, 95.8,
            85.5, 90.8, 89.6, 86.2, 88.0, 93.4,
            82.5, 89.5, 85.6, 87.4, 78.9, 90.7))
graft.aov <- aov(Yield ~ ., graft)
summary(graft.aov)
```

```text
            Df Sum Sq Mean Sq F value Pr(>F)   
PSI          3    178    59.4    8.11 0.0019 **
Block        5    192    38.5    5.25 0.0055 **
Residuals   15    110     7.3                  
```

各列就是方差分析表的各列：$\mathrm{MS}_{\mathrm{Tr}}=178.17/3=59.39$，$\mathrm{MS}_{\mathrm{Blocks}}=192.25/5=38.45$，$\mathrm{MS}_{\mathrm{E}}=109.89/15=7.33$，$F_0=59.39/7.33=8.11$。由于 $F_{3,15,0.05}=3.29<8.11$（$p=0.0019$），我们断定挤出压力影响平均产率。比值 $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}=5.25$ 表明树脂批次之间相差很大，所以分区组是值得的；7.3.4 节解释为什么这是一个描述性的说法而不是检验。

:::

![血管移植物数据。左：每个批次在四种压力下的产率，及各压力的均值；各批次的轮廓线上下平移，但随压力以相似的方式下降。右：按批次分组的产率，及各批次均值与总均值](./plots/graft-data.py)

该图说明了这种设计为什么有帮助。各批次的轮廓线高度相差很大，从批次 5 的均值 $85.3$ 到批次 6 的 $94.5$，但在每个批次内，产率都随压力增大而下降。在完全随机化设计中，这些批次差异会成为误差的一部分；在 RCBD 中，它们被 $\mathrm{SS}_{\mathrm{Blocks}}$ 除去（7.5 节）。

### 7.3.4. 应当检验区组吗？

区组因子按定义并不是感兴趣的。那么我们是否仍应检验 $H_0\colon\beta_1=\cdots=\beta_b=0$，例如为了断言树脂批次之间有显著差异？

一般不必。引入区组因子是为了减小由干扰因子引起的误差变异，而不是为了检验它的效应，无论区组是否有差异，对处理的分析都是有效的。把 $\mathrm{MS}_{\mathrm{Blocks}}$ 与 $\mathrm{MS}_{\mathrm{E}}$ 比较，有助于确认分区组是有效的，即区组解释了本来属于实验误差的变异。若这个比值很小，分区组白白损失了 $b-1$ 个误差自由度，设计实际上还不如 CRD 有效（7.5.2 节）；这对规划下一个实验是有用的。

无论怎样看待区组因子，关于区组都不可能得出更强的结论：

- 把它看作分类因子（批次、试片、高尔夫球手），其观测到的水平不是从某个确定总体中的随机样本，它们也不曾被随机分配给任何东西；区组之间的差异不能归因于任何特定的原因；
- 把它看作实验因子，处理与区组之间有不对称性：处理在区组内被随机化、并在每个区组中重复，而区组本身既没有被随机化，也没有重复，所以证明处理的 $F$ 检验合理的随机化论证不适用于区组。

因此，软件常常连同 $p$ 值一起输出的比值 $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}$，至多是分区组是否有用的一个近似指南，这在 [3.8.6](/3.8.6) 6.4.4 节的比较表中已经指出。对于随机区组，假设 $H_0\colon\sigma_\beta^2=0$ 是有意义的（7.6 节）。

### 7.3.5. 残差分析

模型适当性的检查对 RCBD 与对单因素设计（[3.8.5](/3.8.5)）同样重要。残差 $e_{ij}=y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot}$ 要对拟合值作图、画在**正态概率图**上，并对处理与区组作图；若已知运行顺序，对运行顺序作图可检查独立性假定。在 R 中基本的图是

```r
par(mfcol = c(2, 2))
plot(graft.aov)
par(mfcol = c(1, 1))
```

![血管移植物 RCBD 的残差诊断：残差对拟合值，标准化残差的正态概率图，以及按压力与按批次的残差](./plots/graft-residuals.py)

对于移植物数据，正态性与方差齐性的假定看起来是满足的：正态图接近直线，残差的散布在各拟合值处相近。按因子画的残差给出关于方差齐性与可能的离群值的额外信息；压力之间、批次之间的散布都没有明显差别。RCBD 的残差在每一行与每一列上的和都为零，所以每个区组内的 $a$ 个残差只有 $a-1$ 个自由度；$a=4$ 时，区组内几乎没有出现模式的余地。残差对拟合值图中的弯曲模式会提示处理与区组之间存在交互效应，这可以用 **Tukey 可加性检验**（[3.8.6](/3.8.6) 的定义 6.4.3）正式检验。

### 7.3.6. 特例：配对 t 检验

**命题 7.3.1** 对 $a=2$ 个处理，RCBD 的 $F$ 统计量等于**配对 t 检验**统计量的平方：令 $d_j=y_{1j}-y_{2j}$，$\bar d$ 与 $s_d$ 为它们的均值与标准差，则

$$
F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}=\left(\frac{\bar d}{s_d/\sqrt b}\right)^2=t_0^2,
$$
且 $F_{1,b-1,\alpha}=t_{b-1,\alpha/2}^2$，所以两个检验完全相同。

**证明** 当 $a=2$ 时，$\bar y_{1\cdot}-\bar y_{\cdot\cdot}=\bar d/2$，$\bar y_{2\cdot}-\bar y_{\cdot\cdot}=-\bar d/2$，所以 $\mathrm{SS}_{\mathrm{Tr}}=b\,\bar d^2/2$，自由度为 1。区组均值为 $\bar y_{\cdot j}=(y_{1j}+y_{2j})/2$，所以残差为 $e_{1j}=y_{1j}-\bar y_{\cdot j}-\bar d/2=(d_j-\bar d)/2$，$e_{2j}=-(d_j-\bar d)/2$。因此 $\mathrm{SS}_{\mathrm{E}}=\frac12\sum_j(d_j-\bar d)^2=\frac{(b-1)s_d^2}{2}$，自由度为 $b-1$，$\mathrm{MS}_{\mathrm{E}}=s_d^2/2$，$F_0=b\bar d^2/s_d^2=t_0^2$。$\square$

[3.8.2](/3.8.2) 中"配对还是不配对？"的讨论，因此对两个处理就是"RCBD 还是 CRD？"的讨论：配对就是大小为二的区组，配对的优点恰好就是 7.5 节所研究的分区组的效率增益。

## 7.4. 多重比较

当 $F$ 检验拒绝 $H_0$ 时，[3.8.4](/3.8.4) 的**多重比较**方法可用于处理均值，但有两处改变：每个处理的观测数是区组数 $b$，误差均方及其自由度是 RCBD 的，即自由度为 $(a-1)(b-1)$ 的 $\mathrm{MS}_{\mathrm{E}}$。比较处理 $i$ 与 $k$ 时，

$$
\mathrm{LSD}=t_{(a-1)(b-1),\alpha/2}\sqrt{\frac{2\mathrm{MS}_{\mathrm{E}}}{b}},\qquad \mathrm{HSD}=q_{a,(a-1)(b-1),\alpha}\sqrt{\frac{\mathrm{MS}_{\mathrm{E}}}{b}},
$$
Bonferroni 方法把未调整的 $t$ 检验 $p$ 值与 $\alpha/m$ 比较，$m=\binom a2$。要点在于使用分区组分析中较小的误差：这些比较继承了分区组所获得的精度。

对移植物实验，$\mathrm{MS}_{\mathrm{E}}=7.326$，自由度 $15$，$b=6$，所以差的标准误为 $\sqrt{2\times7.326/6}=1.563$，$\mathrm{LSD}=2.131\times1.563=3.33$，$\mathrm{HSD}=4.076\sqrt{7.326/6}=4.50$。Tukey 区间由

```r
TukeyHSD(graft.aov, "PSI") -> ci
plot(ci, las = 1, cex.axis = .75)
```

得到，它给出下面的差、$95\%$ 同时区间与调整后的 $p$ 值，同时列出用同一个 $\mathrm{MS}_{\mathrm{E}}$ 算出的未调整（LSD）与 Bonferroni 调整的 $p$ 值：

| 比较 | 差 | Tukey 区间 | Tukey $p$ | Bonferroni $p$ | LSD $p$ |
|---|---|---|---|---|---|
| 8700 − 8500 | $-1.13$ | $(-5.64,\ 3.37)$ | 0.885 | 1.000 | 0.479 |
| 8900 − 8500 | $-3.90$ | $(-8.40,\ 0.60)$ | 0.101 | 0.148 | 0.025 |
| 9100 − 8500 | $-7.05$ | $(-11.55,\ -2.55)$ | 0.002 | 0.002 | 0.0004 |
| 8900 − 8700 | $-2.77$ | $(-7.27,\ 1.74)$ | 0.325 | 0.582 | 0.097 |
| 9100 − 8700 | $-5.92$ | $(-10.42,\ -1.41)$ | 0.009 | 0.011 | 0.002 |
| 9100 − 8900 | $-3.15$ | $(-7.65,\ 1.35)$ | 0.226 | 0.373 | 0.062 |

Tukey 方法与 Bonferroni 校正都发现，$9100\,\mathrm{psi}$ 的产率低于 $8500$ 与 $8700\,\mathrm{psi}$；不对多重性作任何调整的 LSD 还判定 $8900$ 与 $8500$ 不同。从 Bonferroni 到 Tukey 再到 LSD，功效依次增大，对假阳性的保护依次减弱。由于 HSD 大于 LSD，Tukey 方法判为不同的任何一对，LSD 也判为不同，反之则不然。

关于软件有两点实际的说明。第一，R 中的 `pairwise.t.test(Yield, PSI)` 使用的是 `Yield` 对 `PSI` 作单因素分析的合并标准差，即忽略区组的、自由度为 $20$ 的误差均方 $15.11$。因此在不作调整时，它并不是 RCBD 的 LSD；用 `p.adjust.method = "bonferroni"` 时，例如对 $9100-8500$ 给出 $p=0.03$，而不是 $0.002$。正确的 LSD 使用分区组分析的 $\mathrm{MS}_{\mathrm{E}}$：

```r
MSE   <- summary(graft.aov)[[1]][3, 3]   # 7.33
df    <- summary(graft.aov)[[1]][3, 1]   # 15
means <- tapply(graft$Yield, graft$PSI, mean)
pairs <- combn(means, 2)
dpair <- pairs[1, ] - pairs[2, ]
t     <- dpair / sqrt(MSE * 2 / 6)
p     <- 2 * (1 - pt(abs(t), df = df))
rbind(combn(4, 2), p)
```

```text
     [,1]    [,2]    [,3]    [,4]    [,5]   [,6]
  1.00000 1.00000 1.00000 2.00000 2.00000 3.0000
  2.00000 3.00000 4.00000 3.00000 4.00000 4.0000
p 0.47946 0.02471 0.00041 0.09696 0.00179 0.0621
```

这里 `combn(4, 2)` 列出六对处理的指标。第二，软件包 `agricolae` 直接由拟合的模型执行 LSD，因而自动使用正确的误差项：

```r
library(agricolae)
LSD.test(graft.aov, trt = "PSI", group = FALSE, console = TRUE)
```

```text
Study: graft.aov ~ "PSI"

LSD t Test for Yield 

Mean Square Error:  7.32575 

PSI,  means and individual ( 95 %) CI

        Yield      std r      LCL      UCL  Min  Max
8500 92.81667 4.577081 6 90.46148 95.17185 87.4 98.2
8700 91.68333 3.304189 6 89.32815 94.03852 87.0 95.8
8900 88.91667 2.966760 6 86.56148 91.27185 85.5 93.4
9100 85.76667 4.445072 6 83.41148 88.12185 78.9 90.7

Alpha: 0.05 ; DF Error: 15
Critical Value of t: 2.13145 

Comparison between treatments means

            difference pvalue signif.        LCL       UCL
8500 - 8700   1.133333 0.4795         -2.1974047  4.464071
8500 - 8900   3.900000 0.0247       *  0.5692620  7.230738
8500 - 9100   7.050000 0.0004     ***  3.7192620 10.380738
8700 - 8900   2.766667 0.0970       . -0.5640714  6.097405
8700 - 9100   5.916667 0.0018      **  2.5859286  9.247405
8900 - 9100   3.150000 0.0621       . -0.1807380  6.480738
```

`std` 一列是每个压力下六个观测的普通标准差，其中包含批次变异；个体区间 `LCL`、`UCL` 使用 $\bar y_{i\cdot}\pm t_{15,0.025}\sqrt{\mathrm{MS}_{\mathrm{E}}/b}=\bar y_{i\cdot}\pm2.131\times1.105$。比较的区间是差 $\pm\mathrm{LSD}=\pm3.33$。

## 7.5. 与完全随机化设计的比较

### 7.5.1. 忽略区组

假设移植物数据被当作来自**完全随机化设计**来分析，忽略批次：

```text
          Df Sum Sq Mean Sq F value Pr(>F)  
PSI        3  178.2   59.39   3.931 0.0234 *
Residuals 20  302.1   15.11                 
```

处理平方和相同，都是 $178.2$，因为处理与区组正交：每个压力在每个批次中恰好运行一次，所以批次差异对所有压力均值的影响相同。但误差平方和现在包含了批次变异，$302.1=192.3+109.9$。误差自由度是 $20$ 而不是 $15$，误差均方却大了约一倍，是 $15.11$ 而不是 $7.33$，所以 $F$ 统计量从 $8.11$ 降到 $3.93$。这里的结果在 $5\%$ 水平上仍然显著，但只要效应稍小或批次变异稍大，压力效应就会检测不出来。Tukey 区间的比较说明了同一点：

![压力均值六个两两差的 Tukey 95% 同时区间，分别由 RCBD 误差均方与忽略批次的单因素误差均方算出；忽略区组使每个区间变宽约 50%](./plots/blocking-intervals.py)

### 7.5.2. 相对效率

CRD 与 RCBD 的区别在于随机化的方式：在 CRD 中全部 $ab$ 个单位都随机分配，在 RCBD 中处理在每个区组内随机化。RCBD 的模型是每个单元格只有一个观测的双向模型，当区组内的误差方差 $\sigma^2_{\mathrm{RCBD}}$ 小于全部单位之间的误差方差 $\sigma^2_{\mathrm{CRD}}$ 时，分区组就是值得的。两种设计的**相对效率**比较的就是这两个方差。

**定义 7.5.1（RCBD 的相对效率）** 随机区组设计相对于观测总数相同的完全随机化设计的**相对效率**是

$$
\mathrm{RE}=\frac{\sigma^2_{\mathrm{CRD}}}{\sigma^2_{\mathrm{RCBD}}} .
$$
由于处理比较的方差正比于 $\sigma^2/r$（每个处理有 $r$ 次重复），CRD 需要 RCBD 的 $\mathrm{RE}$ 倍的重复数，才能以同样的精度估计处理之间的差异。

粗略的估计使用同一数据两种分析的误差均方：

$$
\widehat{\mathrm{RE}}=\frac{\mathrm{MS}_{\mathrm{E}}^{\mathrm{CRD}}}{\mathrm{MS}_{\mathrm{E}}^{\mathrm{RCBD}}}=\frac{15.11}{7.33}=2.06 .
$$
因此 CRD 需要多约 $106\%$ 的观测，才能获得与 RCBD 相同的精度。

更细致的估计（Yates，Cochran 与 Cox）问的是：如果同样的单位不分区组而随机化，误差方差会是多少。此时误差会包含区组变异与区组内变异，但处理的自由度也会成为误差自由度；用 $\mathrm{MS}_{\mathrm{E}}$ 代替它们，

$$
\hat\sigma^2_{\mathrm{CRD}}=\frac{(b-1)\mathrm{MS}_{\mathrm{Blocks}}+b(a-1)\mathrm{MS}_{\mathrm{E}}}{ab-1}=\frac{5\times38.45+18\times7.326}{23}=14.09 .
$$
Fisher 针对两种设计误差自由度的不同，$f_{\mathrm{RCBD}}=(a-1)(b-1)$ 与 $f_{\mathrm{CRD}}=a(b-1)$，提出把比值乘以修正因子

$$
\frac{(f_{\mathrm{RCBD}}+1)(f_{\mathrm{CRD}}+3)}{(f_{\mathrm{RCBD}}+3)(f_{\mathrm{CRD}}+1)}=\frac{16\times23}{18\times21}=0.974,
$$
它反映了用较少自由度估计 $\sigma^2$ 所损失的信息。由此得到的估计是 $\widehat{\mathrm{RE}}=0.974\times14.09/7.326=1.87$：按批次分区组使所需的运行次数大致减半。（除去这个小的修正外）当且仅当 $\mathrm{MS}_{\mathrm{Blocks}}>\mathrm{MS}_{\mathrm{E}}$ 时，该估计大于 1，这正是"区组之间的变异超过区组内的变异时，分区组是有效的"的精确含义。当区组之间没有差异时，RCBD 损失 $b-1$ 个误差自由度，效率略低于 CRD。

于是，应当分区组而没有分区组的后果是清楚的：未被解释的误差更大，处理效应的检验功效更低。

### 7.5.3. 在 R 中随机化两种设计

软件包 `agricolae` 可以生成两种设计的随机化田间记录簿：

```r
library(agricolae)
trt <- levels(graft$PSI)
# Completely randomized design: 6 replicates of each of the 4 pressures
design  <- design.crd(trt, r = rep(6, 4), seed = 777)
book1   <- design$book
# Randomized complete block design: 6 blocks
design2 <- design.rcbd(trt, r = 6, seed = 999)
book2   <- design2$book
design2$sketch
```

```text
     [,1]   [,2]   [,3]   [,4]  
[1,] "8900" "8500" "8700" "9100"
[2,] "8700" "9100" "8900" "8500"
[3,] "9100" "8900" "8700" "8500"
[4,] "9100" "8500" "8700" "8900"
[5,] "9100" "8700" "8500" "8900"
[6,] "8500" "8700" "8900" "9100"
```

草图的每一行是一个区组，每个区组含有四种压力的一个随机排列。田间记录簿 `book2` 列出同一方案并附有小区编号（区组 1 中是 $101,\dots,104$，区组 2 中是 $201,\dots$），而 `book1` 把 CRD 的 $24$ 次运行列在一个随机序列中，其中同一压力可能连续出现若干次，同一压力的重复在各批次中任意分布。

## 7.6. 随机区组

实验的区组往往只是所有可能区组中的一个样本：六个树脂批次是工厂将来会生产的所有批次中的一个样本，关于压力的结论是要对未来的批次成立的。于是很自然地把区组效应当作随机的，如 [3.8.5](/3.8.5) 的**随机效应模型**。

**定义 7.6.1（随机区组的 RCBD）** 在随机区组的 RCBD 模型

$$
Y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij},\qquad \sum_{i=1}^a\tau_i=0,\qquad \beta_j\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma_\beta^2),\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
中，$\beta_j$ 与 $\varepsilon_{ij}$ 相互独立；处理是固定的，区组是随机的。

观测的矩为

$$
\mathbb{E}[Y_{ij}]=\mu+\tau_i,\qquad \operatorname{Var}(Y_{ij})=\sigma_\beta^2+\sigma^2,\qquad \operatorname{Cov}(Y_{ij},Y_{i'j})=\sigma_\beta^2\ (i\ne i'),\qquad \operatorname{Cov}(Y_{ij},Y_{i'j'})=0\ (j\ne j').
$$
同一区组内的观测是相关的，**组内相关系数**为 $\rho=\sigma_\beta^2/(\sigma_\beta^2+\sigma^2)$；不同区组的观测相互独立。方差 $\sigma_\beta^2$ 与 $\sigma^2$ 是**方差分量**。

**定理 7.6.1** 在随机区组的 RCBD 中，

$$
\mathbb{E}[\mathrm{MS}_{\mathrm{Tr}}]=\sigma^2+\frac{b\sum_{i=1}^a\tau_i^2}{a-1},\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{Blocks}}]=\sigma^2+a\sigma_\beta^2,\qquad \mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2 .
$$
检验无处理效应的统计量是 $F_0=\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}$，在 $H_0$ 下 $\sim F_{a-1,(a-1)(b-1)}$，与固定区组时完全相同；$H_0\colon\sigma_\beta^2=0$ 由 $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}$ 检验，在该假设下 $\sim F_{b-1,(a-1)(b-1)}$。

**证明** 处理均值 $\bar Y_{i\cdot}=\mu+\tau_i+\bar\beta+\bar\varepsilon_{i\cdot}$ 都含有同一个随机量 $\bar\beta$，它在 $\bar Y_{i\cdot}-\bar Y_{\cdot\cdot}=\tau_i+\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot\cdot}$ 中抵消；所以 $\mathrm{SS}_{\mathrm{Tr}}$ 与固定区组时是误差的同一个函数。残差 $\varepsilon_{ij}-\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot j}+\bar\varepsilon_{\cdot\cdot}$ 完全不涉及 $\beta_j$。区组均值为 $\bar Y_{\cdot j}=\mu+\beta_j+\bar\varepsilon_{\cdot j}$，是独立的 $\mathcal{N}(\mu,\sigma_\beta^2+\sigma^2/a)$，所以 $\mathrm{SS}_{\mathrm{Blocks}}/(\sigma^2+a\sigma_\beta^2)=a\sum_j(\bar Y_{\cdot j}-\bar Y_{\cdot\cdot})^2/(\sigma^2+a\sigma_\beta^2)\sim\chi^2_{b-1}$，如 [3.8.5](/3.8.5) 的定理 5.3.1。在给定 $\beta_j$ 的条件下，三个平方和相互独立，分布如定理 7.3.1；$\mathrm{SS}_{\mathrm{Tr}}$ 与 $\mathrm{SS}_{\mathrm{E}}$ 的条件分布不依赖于 $\beta_j$，由此得到无条件下的独立性与零分布。$\square$

因此，把区组当作随机的并不改变对处理效应的检验。区组方差分量的方差分析估计令 $\mathrm{MS}_{\mathrm{Blocks}}$ 等于其期望：

$$
\hat\sigma_\beta^2=\frac{\mathrm{MS}_{\mathrm{Blocks}}-\mathrm{MS}_{\mathrm{E}}}{a}=\frac{38.45-7.33}{4}=7.78
$$
对移植物实验，批次之间的方差与批次内运行之间的方差 $\hat\sigma^2=7.33$ 大致一样大，$\hat\rho\approx0.5$。同一模型也可用 `lme4` 软件包由**限制极大似然估计**拟合；`0 + PSI` 要求每个压力一个均值，而不是截距与对比：

```r
library(lme4)
summary(lmer(Yield ~ 0 + PSI + (1 | Block), data = graft))
```

```text
Linear mixed model fit by REML ['lmerMod']
Formula: Yield ~ 0 + PSI + (1 | Block)
   Data: graft

REML criterion at convergence: 112

Scaled residuals: 
     Min       1Q   Median       3Q      Max 
-1.32253 -0.64269  0.01068  0.54202  1.62882 

Random effects:
 Groups   Name        Variance Std.Dev.
 Block    (Intercept) 7.781    2.789   
 Residual             7.326    2.707   
Number of obs: 24, groups:  Block, 6

Fixed effects:
        Estimate Std. Error t value
PSI8500   92.817      1.587   58.49
PSI8700   91.683      1.587   57.78
PSI8900   88.917      1.587   56.04
PSI9100   85.767      1.587   54.05
```

因为设计是平衡的且 $\mathrm{MS}_{\mathrm{Blocks}}>\mathrm{MS}_{\mathrm{E}}$，REML 估计 $\hat\sigma_\beta^2=7.781$ 与 $\hat\sigma^2=7.326$ 和方差分析估计一致。固定效应的估计就是各压力的均值。它们的标准误 $1.587=\sqrt{(7.781+7.326)/6}$ 是 $\sqrt{\operatorname{Var}(\bar Y_{i\cdot})}=\sqrt{(\sigma_\beta^2+\sigma^2)/b}$，大于固定区组分析的 $\sqrt{7.326/6}=1.105$：对批次总体而言，$8500\,\mathrm{psi}$ 下的平均产率之所以不确定，也是因为只抽取了六个批次。压力均值之差中 $\bar\beta$ 抵消，在两个模型中有相同的标准误 $\sqrt{2\sigma^2/b}=1.563$，所以 7.4 节的比较不变。

随机区组的方差分析方法的优点是公式明确，机制一目了然。它的缺点是：$\hat\sigma_\beta^2$ 可能为负（只要 $\mathrm{MS}_{\mathrm{Blocks}}<\mathrm{MS}_{\mathrm{E}}$）；对于不平衡的设计与多个因子，方差分析的分解不唯一（依赖于因子的顺序），平方和不正交，精确的分布理论失效；以及随着因子的增加公式变得复杂。替代的办法是基于似然的估计，即极大似然或 REML，这就是 `lmer` 所做的。

## 7.7. 缺失值

### 7.7.1. 为什么缺失值是个问题

随机区组设计中偶尔会丢失一个观测：试样断裂、一次运行作废、一个小区被水淹。**缺失值**破坏了 RCBD 每个处理在每个区组中都出现的定义性特征。处理不再与区组正交，问题也不只是把 $b$ 换成每个处理的观测数 $n_i$：恒等式

$$
\sum_{i,j}(y_{ij}-\bar y_{\cdot\cdot})^2=b\sum_i(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2+a\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2+\sum_{i,j}(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2
$$
不再成立，无论求和对哪些项进行。取 $a=2$ 个处理、$b=3$ 个区组、缺失 $y_{22}$ 的一个很小的例子可以说明：

| | 区组 1 | 区组 2 | 区组 3 | $\bar y_{i\cdot}$ |
|---|---|---|---|---|
| 处理 1 | 1 | 3 | 2 | 2 |
| 处理 2 | 2 | – | 2 | 2 |
| $\bar y_{\cdot j}$ | 1.5 | 3 | 2 | $\bar y_{\cdot\cdot}=2$ |

这里 $\mathrm{SS}_{\mathrm{T}}=1+1+0+0+0=2$，而公式给出 $\mathrm{SS}_{\mathrm{Tr}}=0$，$\mathrm{SS}_{\mathrm{Blocks}}=2[(1.5-2)^2+(3-2)^2+0]=2.5$，$\mathrm{SS}_{\mathrm{E}}=0.25+0+0+0.25+0=0.5$，它们之和是 $3\ne2$。区组 2 只有处理 1 的那个较高的观测，这样的模式使处理均值与区组均值相互依赖。

有两种补救办法。精确的分析把模型当作不平衡的双向模型，用最小二乘拟合不完全的数据。经典的近似分析先估计缺失值，再把补全的数据当作 RCBD 来分析。

### 7.7.2. 估计一个缺失值

**命题 7.7.1** 设观测 $y_{ij}$ 缺失，$y'_{i\cdot}$、$y'_{\cdot j}$ 与 $y'_{\cdot\cdot}$ 分别是不含它的处理 $i$ 的总和、区组 $j$ 的总和与全体观测的总和。使补全数据的误差平方和 $\mathrm{SS}_{\mathrm{E}}(x)$ 最小的值 $x$ 是

$$
x=\frac{a\,y'_{i\cdot}+b\,y'_{\cdot j}-y'_{\cdot\cdot}}{(a-1)(b-1)} .
$$
它是 RCBD 模型对 $ab-1$ 个可用观测作最小二乘拟合时单元格 $(i,j)$ 的拟合值，而 $\mathrm{SS}_{\mathrm{E}}(x)$ 等于该拟合的残差平方和。

**证明** 把 $x$ 放入单元格 $(i,j)$，$\mathrm{SS}_{\mathrm{E}}(x)=\min_{\mu,\tau,\beta}Q(x;\mu,\tau,\beta)$，其中 $Q$ 是全部 $ab$ 个单元格上的偏差平方和。同时对 $x$ 极小化，$\min_x\mathrm{SS}_{\mathrm{E}}(x)=\min_{\mu,\tau,\beta}\min_xQ$。对固定的参数，$Q$ 中唯一含 $x$ 的项是 $(x-\mu-\tau_i-\beta_j)^2$，取 $x=\mu+\tau_i+\beta_j$ 时它被极小化，并化为零；剩下的是 $ab-1$ 个可用单元格上的平方和。所以联合极小值在对不完全数据的最小二乘拟合处取得，$x$ 等于它的拟合值，最小的 $\mathrm{SS}_{\mathrm{E}}$ 就是该拟合的残差平方和。等价地，在补全数据的分析中，补入单元格的残差为零，即 $x=\bar y_{i\cdot}+\bar y_{\cdot j}-\bar y_{\cdot\cdot}$，其中的均值由补全的数据算出：

$$
x=\frac{y'_{i\cdot}+x}{b}+\frac{y'_{\cdot j}+x}{a}-\frac{y'_{\cdot\cdot}+x}{ab}.
$$
两边乘以 $ab$ 得 $abx=a(y'_{i\cdot}+x)+b(y'_{\cdot j}+x)-(y'_{\cdot\cdot}+x)$，即 $(ab-a-b+1)\,x=a\,y'_{i\cdot}+b\,y'_{\cdot j}-y'_{\cdot\cdot}$，而 $ab-a-b+1=(a-1)(b-1)$。$\square$

同一个公式也可以直接对 $\mathrm{SS}_{\mathrm{E}}(x)=\sum_{i,j}(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2$ 求导并解 $\mathrm{d}\,\mathrm{SS}_{\mathrm{E}}/\mathrm{d}x=0$ 得到，这是经典的推导。

**例 7.7.1** 设移植物实验中批次 4 里 $8700\,\mathrm{psi}$ 的观测 $y_{24}=94.7$ 丢失了。则 $y'_{2\cdot}=550.1-94.7=455.4$，$y'_{\cdot4}=362.2-94.7=267.5$，$y'_{\cdot\cdot}=2155.1-94.7=2060.4$，

$$
x=\frac{4\times455.4+6\times267.5-2060.4}{3\times5}=\frac{1366.2}{15}=91.08 .
$$
近似方法用可加模型的预测（"插补"）值代替缺失点，R 用 `predict` 计算它：

```r
vas <- graft
vas[10, 3] <- NA                         # row 10: PSI 8700, Block 4
p <- predict(aov(Yield ~ PSI + Block, vas), newdata = vas[10, ])   # 91.08
vas[10, 3] <- p                          # just replace it
summary(aov(Yield ~ PSI + Block, vas))
```

```text
          Df Sum Sq Mean Sq F value  Pr(>F)   
PSI        3  166.1   55.38   8.169 0.00185 **
Block      5  189.5   37.90   5.591 0.00419 **
Residuals 15  101.7    6.78                   
```

:::

这个表在使用之前需要两处修正。

1. 误差自由度必须对每个缺失观测减少一个：插补值对误差没有贡献，因为它的残差为零。误差自由度是 $14$，$\mathrm{MS}_{\mathrm{E}}=101.7/14=7.26$，而不是 $6.78$。
2. 补全数据的处理平方和有向上的偏差。对区组调整后的处理平方和的精确值要小

   $$
   \frac{\bigl[y'_{\cdot j}-(a-1)x\bigr]^2}{a(a-1)}=\frac{(267.5-3\times91.08)^2}{12}=2.75,
   $$
   即 $166.1-2.7=163.4$，精确的检验是 $F_0=(163.4/3)/7.26=7.50$（$p=0.0031$）。

偏差来自约化模型。调整后的处理平方和是只含区组的模型与完全模型的残差平方和之差。第二个由命题 7.7.1 就是 $\mathrm{SS}_{\mathrm{E}}(x)$。在第一个中，插补的 $x$ 不是最优值：在只含区组的模型下，最佳的值是区组 $j$ 中其余观测的均值 $y'_{\cdot j}/(a-1)$，当 $a$ 个观测中的一个偏离其余观测的均值时，这组观测的残差平方和增加 $\frac{a-1}{a}\bigl(x-y'_{\cdot j}/(a-1)\bigr)^2$。这个增加量就是上面给出的偏差，它被加到了处理平方和上。

与完整数据相比（$\mathrm{SS}_{\mathrm{E}}=110$，自由度 $15$），补全数据的误差平方和较小，为 $101.7$：插补值完全符合模型，而真实的观测有残差。这总是成立的，因为 $x$ 在缺失观测所有可能的取值中使 $\mathrm{SS}_{\mathrm{E}}$ 最小。

### 7.7.3. 多个缺失值与精确分析

有多个缺失值时，每一个都用命题 7.7.1 的公式估计，公式中代入其他缺失值的当前估计，迭代直至估计收敛；误差自由度减去缺失值的个数。这种拟合与插补的迭代是 **EM 算法**的早期实例，它收敛到对不完全数据的最小二乘拟合。

如今精确的最小二乘分析直接就能算出。R 丢弃含 `NA` 的行，拟合不平衡的可加模型；方差分析表此时列出**序贯平方和**，其中每一项只对它前面的项作调整，所以各项的顺序很重要：

```r
vas[10, 3] <- NA
summary(aov(Yield ~ PSI + Block, vas))
summary(aov(Yield ~ Block + PSI, vas))
```

```text
            Df Sum Sq Mean Sq F value  Pr(>F)   
PSI          3  164.0   54.67   7.525 0.00308 **
Block        5  189.5   37.90   5.218 0.00653 **
Residuals   14  101.7    7.26                   
1 observation deleted due to missingness

            Df Sum Sq Mean Sq F value  Pr(>F)   
Block        5  190.1   38.02   5.235 0.00645 **
PSI          3  163.4   54.47   7.498 0.00313 **
Residuals   14  101.7    7.26                   
1 observation deleted due to missingness
```

两种顺序下的残差行相同，且与修正后的近似分析一致：$\mathrm{SS}_{\mathrm{E}}=101.7$，自由度 $14$。在第一个表中，`PSI` 没有对区组作调整：它的平方和 $164.0$ 比较的是不完全数据的压力均值，其中 $8700\,\mathrm{psi}$ 的均值缺少批次 4。在第二个表中，`PSI` 排在 `Block` 之后，它的平方和 $163.4$ 度量的是除去批次效应之后的压力效应，这才是实验要回答的问题；它与例 7.7.1 修正后的值一致，$F_0=7.498$。因此在有缺失数据的区组设计中检验处理时，区组项必须先放入：`Yield ~ Block + PSI`。

## 7.8. 广义完全区组设计

### 7.8.1. 区组大于处理数

为什么区组的大小必须等于处理数？原因在于同质性：一组单位越大，越可能是不均匀的，而区组只有在其内部的单位相似时才有用。但当较大的区组并不增加区组内的变异时，就没有必要限制每个区组每个处理只有一个单位，每个处理可以在每个区组内重复。

**定义 7.8.1（广义完全区组设计）** 有 $a$ 个处理与 $b$ 个区组的**广义完全区组设计**（GCBD）的区组含有 $an$ 个实验单位，$n\ge2$；每个处理在每个区组中施加于 $n$ 个单位，处理在每个区组内随机化。它的模型是

$$
Y_{ijk}=\mu+\tau_i+\beta_j+\gamma_{ij}+\varepsilon_{ijk},\qquad i=1,\dots,a,\quad j=1,\dots,b,\quad k=1,\dots,n,
$$
其中 $\gamma_{ij}$ 是区组与处理的交互效应，$\varepsilon_{ijk}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$。

与 RCBD 不同，GCBD 在每个处理与区组的单元格内有重复，所以处理与区组之间的交互效应可以估计与检验，RCBD 的可加性假定也就不再需要。分析是 [3.8.6](/3.8.6) 那样的双因素方差分析，处理、区组、交互效应与误差的自由度分别是 $a-1$、$b-1$、$(a-1)(b-1)$ 与 $ab(n-1)$。

**例 7.8.1** 一本高尔夫杂志（2006）报道的一个实验，旨在向所有读者推荐击球座的高度，使开球的球飞得最远。处理因子是击球座的高度，有三个水平：

| 水平 | 击球座高度 |
|---|---|
| 1 | 整个球低于球杆击球面的顶沿 |
| 2 | 球的一半高出顶沿 |
| 3 | 球的底部与击球面的顶部齐平 |

响应是球被击出后飞行的距离。由于球手的开球能力差别很大，试验按球手分区组，每个球手击球的顺序是随机的。多击三个以上的球不会使球手疲劳、使其开球距离的变异增大，所以没有必要限制每个球手只击三次。九名球手各自在三种击球座高度下各击五个球，每人共 $15$ 个球，顺序随机：这是 $a=3$ 个处理、$b=9$ 个区组、$n=5$ 次重复，$N=135$ 次开球的 GCBD。

:::

### 7.8.2. 以区组与处理的交互效应作误差项

如果球手与击球座高度之间的交互效应显著，最优的击球座高度就可能因人而异。研究中的球手只是球手的一个样本，所以我们不能根据这些球手的偏好，向全体读者推荐一个最优的击球座高度。要把关于处理效应的结论推广到所有实验单位，平均的处理效应应当大于处理效应在区组之间的差异。因此，由区组与处理的交互效应度量的处理效应在区组之间的变异，是检验处理效应的正确标尺，也就是正确的误差项：

$$
\text{RCBD: } F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{E}}}\qquad\Longrightarrow\qquad \text{GCBD: } F_0=\frac{\mathrm{MS}_{\mathrm{Tr}}}{\mathrm{MS}_{\mathrm{Tr}\times\mathrm{B}}} .
$$
7.8.4 节说明，这正是混合模型的期望均方所要求的。在 RCBD 中二者重合：每个单元格只有一个观测时，可加模型的误差就是区组与处理的交互效应。

在 R 中，`aov` 的误差层给出这个检验。数据从一个文件读入，文件的第一行是球手的编号，第一列是击球座的高度：

```r
f <- file.choose()   # choose "golf.txt"
y <- scan(f)
y <- matrix(y, byrow = T, ncol = 10)
golf <- data.frame(cdistance = as.vector(y[-1, -1]),
                   teehgt = as.factor(rep(y[-1, 1], times = 9)),
                   id = as.factor(rep(y[1, -1], each = 15)))
# Test the significance of teehgt
mod1 <- aov(cdistance ~ teehgt + Error(id/teehgt), data = golf)
summary(mod1)
```

```text
Error: id
          Df Sum Sq Mean Sq F value Pr(>F)
Residuals  8 124741   15593               

Error: id:teehgt
          Df Sum Sq Mean Sq F value Pr(>F)  
teehgt     2   1724   862.0   5.854 0.0124 *
Residuals 16   2356   147.3                 
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Error: Within
           Df Sum Sq Mean Sq F value Pr(>F)
Residuals 108   7341   67.97               
```

项 `Error(id/teehgt)` 在单次开球之上声明了两个误差层：球手（`id`），以及球手内的击球座高度（`id:teehgt`）。每个变异来源用它自己所在层的残差来检验。在球手内部变化的击球座高度效应，用球手与击球座高度的交互均方检验：$F_0=862.0/147.3=5.854$，自由度为 $2$ 与 $16$，$p=0.0124$。`Within` 层含有一个球手在一种击球座高度下五次开球之间的变异，$\mathrm{MS}_{\mathrm{E}}=67.97$，自由度为 $9\times3\times4=108$。

一个等价而更简单的方法是对重复取平均。建立新的响应，即每个区组与处理的单元格的均值，对这些单元格均值拟合普通的 RCBD 模型：

```r
cellmeans <- tapply(golf$cdistance, list(golf$id, golf$teehgt), mean)
dim(cellmeans) <- NULL   # same as as.vector
teehgt <- factor(rep(1:3, each = 9))
id     <- factor(rep(1:9, 3))
mod2 <- aov(cellmeans ~ id + teehgt)
summary(mod2)
```

```text
          Df Sum Sq Mean Sq F value   Pr(>F)    
id         8  24948  3118.5 105.888 2.19e-12 ***
teehgt     2    345   172.4   5.854   0.0124 *  
Residuals 16    471    29.5                     
```

单元格均值为

| 球手 | 座高 1 | 座高 2 | 座高 3 |
|---|---|---|---|
| 1 | 143.18 | 141.64 | 147.40 |
| 2 | 173.18 | 176.14 | 188.04 |
| 3 | 141.64 | 147.40 | 143.18 |
| 4 | 176.10 | 178.04 | 175.72 |
| 5 | 204.68 | 213.20 | 226.26 |
| 6 | 137.10 | 148.56 | 146.70 |
| 7 | 171.18 | 166.46 | 173.14 |
| 8 | 168.88 | 187.38 | 176.06 |
| 9 | 227.18 | 241.72 | 242.04 |

这个 RCBD 的每个平方和，都等于 GCBD 相应的平方和除以 $n=5$（$24948=124741/5$，$345=1724/5$，$471=2356/5$），所以击球座高度的 $F$ 比与 $p$ 值与误差层分析的完全相同。对重复取平均不损失关于处理检验的任何信息，因为单元格内的变异不进入这个检验。

![高尔夫实验：每个球手在三种击球座高度下的平均开球距离。左：球手的水平相差极大；右：减去每个球手的均值后，轮廓线仍然不同，这就是球手与击球座高度的交互效应，击球座高度正是相对于它来检验的](./plots/golf-cell-means.py)

基于单元格均值模型（$\mathrm{MS}=29.5$，自由度 $16$）的各击球座高度的平均距离与 Tukey 比较是

```r
model.tables(mod2, type = "means")$tables$teehgt
TukeyHSD(mod2, "teehgt")
```

```text
teehgt
       1        2        3 
171.4578 177.8378 179.8378 

  Tukey multiple comparisons of means
    95% family-wise confidence level

Fit: aov(formula = cellmeans ~ id + teehgt)

$teehgt
    diff        lwr       upr     p adj
2-1 6.38 -0.2211713 12.981171 0.0589879
3-1 8.38  1.7788287 14.981171 0.0124851
3-2 2.00 -4.6011713  8.601171 0.7192035
```

高度 3 比高度 1 飞得显著更远，高度 2 比高度 1 处于好的边缘，高度 2 与 3 没有差别。给文章读者的建议是：击球时让球至少有一半高出球杆击球面的顶沿，以使开球距离最大。

### 7.8.3. 合并还是不合并

如果交互效应可以忽略，可加模型

$$
Y_{ijk}=\mu+\tau_i+\beta_j+\varepsilon_{ijk}
$$
给出的处理效应检验，比以交互均方为分母的检验更有功效。此时交互均方估计的是与误差均方相同的实验误差，把二者合并增加了误差自由度，从而提高了 $F$ 检验的功效。通常的"合并还是不合并"程序在这两种做法之间作出决定：

1. 用 $F=\mathrm{MS}_{\mathrm{Tr}\times\mathrm{B}}/\mathrm{MS}_{\mathrm{E}}$ 检验交互效应，显著性水平比通常的更高，一般取 $\alpha=0.25$，这样只有当存在交互效应的证据很弱时才合并。
2. 如果交互效应显著，就以交互均方作处理 $F$ 检验的分母。
3. 如果不显著，就拟合可加模型，用它的默认 $F$ 检验，使用合并的误差均方 $(\mathrm{SS}_{\mathrm{Tr}\times\mathrm{B}}+\mathrm{SS}_{\mathrm{E}})/[(a-1)(b-1)+ab(n-1)]$。

对高尔夫实验，完整的双因素方差分析给出

```r
mod3 <- aov(cdistance ~ id * teehgt, data = golf)
summary(mod3)
```

```text
           Df Sum Sq Mean Sq F value   Pr(>F)    
id          8 124741   15593 229.406  < 2e-16 ***
teehgt      2   1724     862  12.682 1.13e-05 ***
id:teehgt  16   2356     147   2.166   0.0102 *  
Residuals 108   7341      68                     
```

交互效应检验的 $p=0.0102<0.25$，所以不应拟合可加模型，对击球座高度也没有比使用交互项的检验更有功效的 $F$ 检验，$F_0=5.854$。该表 `teehgt` 一行的 $F=862/67.97=12.68$ 以单元格内误差为分母；只有当这些球手是仅有的感兴趣的球手（固定区组）、结论只限于他们时，它才是正确的检验，而这并不是这项研究的目的。

预备检验使最后的检验以它的结果为条件，所以总的显著性水平并不恰好是 $\alpha$；预备检验采用较高的水平 $0.25$，是为了使合并一个真实交互效应的风险保持得很小。

### 7.8.4. 混合模型

击球座高度可以看作固定效应，因为实验的目的是确定击球座高度是否引起开球距离的差别。球手，即区组因子，可以看作随机效应：我们对比较实验中用到的这些具体球手并无兴趣，他们是有代表性的球手的一个样本。于是球手与击球座高度的交互效应也应当看作随机的，因为随机效应与固定效应的交互效应按定义是随机效应。这样既含固定效应又含随机效应的模型就是**线性混合模型**（一般形式见 [7.7.17](/7.7.17)）。

**定义 7.8.2（双因子混合模型）** 在有一个**固定因子** $A$（$a$ 个水平）、一个**随机因子** $B$（$b$ 个水平）与 $n$ 次重复的双因子混合模型

$$
Y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\varepsilon_{ijk},\qquad \sum_{i=1}^a\tau_i=0,\qquad \beta_j\sim\mathcal{N}(0,\sigma_\beta^2),\quad (\tau\beta)_{ij}\sim\mathcal{N}(0,\sigma_{\tau\beta}^2),\quad \varepsilon_{ijk}\sim\mathcal{N}(0,\sigma^2),
$$
中，所有随机项相互独立（在模型的受限形式中，一个区组的交互效应被约束为对 $i$ 求和为零，见下）。此时 $\mathbb{E}[Y_{ijk}]=\mu+\tau_i$，$\operatorname{Var}(Y_{ijk})=\sigma_\beta^2+\sigma_{\tau\beta}^2+\sigma^2$。

对高尔夫实验，$a=3$，$b=9$，$n=5$，期望均方为

| 来源 | 自由度 | $\mathbb{E}[\mathrm{MS}]$ | 高尔夫 |
|---|---|---|---|
| $A$：击球座高度（$\tau_i$） | $a-1$ | $\sigma^2+n\sigma_{\tau\beta}^2+\dfrac{bn\sum_i\tau_i^2}{a-1}$ | $\sigma^2+5\sigma_{\tau\beta}^2+\dfrac{9\times5\sum_i\tau_i^2}{2}$，自由度 $2$ |
| $B$：球手（$\beta_j$） | $b-1$ | $\sigma^2+an\sigma_\beta^2$ | $\sigma^2+3\times5\,\sigma_\beta^2$，自由度 $8$ |
| $AB$：击球座高度 × 球手（$(\tau\beta)_{ij}$） | $(a-1)(b-1)$ | $\sigma^2+n\sigma_{\tau\beta}^2$ | $\sigma^2+5\sigma_{\tau\beta}^2$，自由度 $16$ |
| 误差（$\varepsilon_{ijk}$，重复） | $ab(n-1)$ | $\sigma^2$ | $\sigma^2$，自由度 $(5-1)\times3\times9=108$ |

构造 $F$ 检验的规则是：选择这样的均方作分母，它的期望在零假设成立时等于分子的期望。在 $H_0\colon\tau_1=\tau_2=\tau_3=0$ 下，$\mathrm{MS}_A$ 的期望化为 $\sigma^2+n\sigma_{\tau\beta}^2$，即 $\mathrm{MS}_{AB}$ 的期望，所以

$$
F_0=\frac{\mathrm{MS}_A}{\mathrm{MS}_{AB}}\ \overset{H_0}{\sim}\ F_{a-1,(a-1)(b-1)},
$$
这就是 7.8.2 节的检验。交互方差分量由 $\mathrm{MS}_{AB}/\mathrm{MS}_{\mathrm{E}}$ 检验，由 $\hat\sigma_{\tau\beta}^2=(\mathrm{MS}_{AB}-\mathrm{MS}_{\mathrm{E}})/n=(147.3-67.97)/5=15.9$ 估计；区组分量由 $\hat\sigma_\beta^2=(\mathrm{MS}_B-\mathrm{MS}_{\mathrm{E}})/(an)=(15593-67.97)/15=1035$ 估计。于是，球手的长期平均距离以约 $32$ 个距离单位的标准差变化，球手对击球座高度的特有反应以约 $4$ 的标准差变化，单次开球以约 $8$ 的标准差变化。

$B$ 的期望均方依赖于一种约定。上表是受限混合模型的，其中交互效应对每个区组 $j$ 满足 $\sum_i(\tau\beta)_{ij}=0$（且 $\operatorname{Var}((\tau\beta)_{ij})=\frac{a-1}{a}\sigma_{\tau\beta}^2$，使 $AB$ 一行如表所示）；假设 $H_0\colon\sigma_\beta^2=0$ 此时由 $F_0=\mathrm{MS}_B/\mathrm{MS}_{\mathrm{E}}$ 检验。在定义 7.8.2 的不受限混合模型（不加该约束）中，$\mathbb{E}[\mathrm{MS}_B]=\sigma^2+n\sigma_{\tau\beta}^2+an\sigma_\beta^2$，检验 $\sigma_\beta^2=0$ 用 $\mathrm{MS}_B/\mathrm{MS}_{AB}$。两个模型对固定效应给出相同的检验；它们的差别只在于区组方差分量的含义（在受限模型中，$\sigma_\beta^2$ 是对处理平均后的区组均值的方差；在不受限模型中，它不含交互效应的部分）。R 中的 `Error(id/teehgt)` 分析对应于不受限模型，而 `lmer(cdistance ~ teehgt + (1 | id) + (1 | id:teehgt))` 用 REML 拟合它。

对于 7.6 节随机区组的可加模型（$n=1$，没有交互项），$\mathbb{E}[\mathrm{MS}_{\mathrm{Blocks}}]=\sigma^2+a\sigma_\beta^2$，检验 $\sigma_\beta^2=0$ 用 $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}$（定理 7.6.1）。含有多个随机因子的混合模型、它们的 REML 估计与近似 $F$ 检验将在后面的章节中讨论。

## 小结 {#summary}

- 分区组除去由已知且可控的干扰因子引起的变异；已知但不可控的协变量用协方差分析处理，未知的用随机化处理（7.1.2 节）。能分区组的就分区组，不能的就随机化。
- RCBD（定义 7.2.1）让每个处理在每个区组中恰好运行一次，并在区组内随机化。模型 $Y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij}$（定义 7.2.2）按设计是可加的；估计为 $\hat\tau_i=\bar y_{i\cdot}-\bar y_{\cdot\cdot}$，$\hat\beta_j=\bar y_{\cdot j}-\bar y_{\cdot\cdot}$（命题 7.2.1）。
- RCBD 的方差分析（定理 7.3.1）：

  | 来源 | SS | 自由度 | $\mathbb{E}[\mathrm{MS}]$（固定区组） | $\mathbb{E}[\mathrm{MS}]$（随机区组） | $F_0$ |
  |---|---|---|---|---|---|
  | 处理 | $b\sum_i(\bar y_{i\cdot}-\bar y_{\cdot\cdot})^2$ | $a-1$ | $\sigma^2+\frac{b\sum\tau_i^2}{a-1}$ | $\sigma^2+\frac{b\sum\tau_i^2}{a-1}$ | $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{E}}$ |
  | 区组 | $a\sum_j(\bar y_{\cdot j}-\bar y_{\cdot\cdot})^2$ | $b-1$ | $\sigma^2+\frac{a\sum\beta_j^2}{b-1}$ | $\sigma^2+a\sigma_\beta^2$ | （不是严格的检验） |
  | 误差 | $\sum_{i,j}(y_{ij}-\bar y_{i\cdot}-\bar y_{\cdot j}+\bar y_{\cdot\cdot})^2$ | $(a-1)(b-1)$ | $\sigma^2$ | $\sigma^2$ | |
  | 总计 | $\sum_{i,j}(y_{ij}-\bar y_{\cdot\cdot})^2$ | $ab-1$ | | | |

- 区组的 $F$ 比只表明分区组是否有效（7.3.4 节）；仍然需要残差分析（7.3.5 节）。对 $a=2$，RCBD 就是配对设计，$F_0=t_0^2$（命题 7.3.1）。
- 多重比较使用自由度为 $(a-1)(b-1)$ 的 $\mathrm{MS}_{\mathrm{E}}$，每个均值有 $b$ 个观测：$\mathrm{LSD}=t_{(a-1)(b-1),\alpha/2}\sqrt{2\mathrm{MS}_{\mathrm{E}}/b}$，$\mathrm{HSD}=q_{a,(a-1)(b-1),\alpha}\sqrt{\mathrm{MS}_{\mathrm{E}}/b}$。单因素的 `pairwise.t.test` 忽略区组。
- CRD 与 RCBD：处理平方和相同，CRD 的误差吸收了区组平方和。相对效率（定义 7.5.1）$\approx\mathrm{MS}_{\mathrm{E}}^{\mathrm{CRD}}/\mathrm{MS}_{\mathrm{E}}^{\mathrm{RCBD}}$，更精确地用 $\hat\sigma^2_{\mathrm{CRD}}=[(b-1)\mathrm{MS}_{\mathrm{Blocks}}+b(a-1)\mathrm{MS}_{\mathrm{E}}]/(ab-1)$ 并作 Fisher 的自由度修正；移植物例：$2.06$ 与 $1.87$。
- 随机区组（定义 7.6.1，定理 7.6.1）：处理的 $F$ 检验相同；$\hat\sigma_\beta^2=(\mathrm{MS}_{\mathrm{Blocks}}-\mathrm{MS}_{\mathrm{E}})/a$；处理均值的标准误含 $\sigma_\beta^2$，均值之差的标准误不含。
- 一个缺失值：$x=\dfrac{a\,y'_{i\cdot}+b\,y'_{\cdot j}-y'_{\cdot\cdot}}{(a-1)(b-1)}$（命题 7.7.1）；每个缺失值减少一个误差自由度；补全数据的处理 SS 有向上的偏差 $[y'_{\cdot j}-(a-1)x]^2/[a(a-1)]$。精确分析：`Yield ~ Block + PSI`（区组在前）。
- GCBD（定义 7.8.1）：每个区组中每个处理有 $n$ 次重复；区组随机时处理的检验是 $\mathrm{MS}_{\mathrm{Tr}}/\mathrm{MS}_{\mathrm{Tr}\times\mathrm{B}}$（`Error(block/trt)`，或对单元格均值作 RCBD）；只有当交互效应在 $\alpha=0.25$ 的预备检验中不显著时，才把它合并入误差。
- 混合模型（定义 7.8.2），$A$ 固定，$B$ 随机：$\mathbb{E}[\mathrm{MS}_A]=\sigma^2+n\sigma_{\tau\beta}^2+bn\sum\tau_i^2/(a-1)$，$\mathbb{E}[\mathrm{MS}_{AB}]=\sigma^2+n\sigma_{\tau\beta}^2$，$\mathbb{E}[\mathrm{MS}_B]=\sigma^2+an\sigma_\beta^2$（受限）或 $\sigma^2+n\sigma_{\tau\beta}^2+an\sigma_\beta^2$（不受限）；$F$ 检验的分母是在 $H_0$ 下期望与分子相同的均方。

## 思考题

1. 在一项田间试验中，响应是作物产量，感兴趣的因子是品种；田块被划分成肥力不同的地带，每条地带又划分成与品种数相同的小区。哪种设计与分析是合适的：带简单线性回归的 CRD、带单因素方差分析的 CRD，还是考虑地带的设计？

   **答** 地带是区组（干扰因子）：在每条地带内把品种随机化，这就是 RCBD，用含品种与地带的双因素可加模型（无交互效应的双因素方差分析）分析。带单因素方差分析的 CRD 是有效的，但会把地带的差异留在误差中；简单线性回归不适用于定性因子。

2. 对血管移植物实验，分别把它描述为 CRD 与 RCBD（有几个因子，有无交互效应，运行如何随机化），并说明你会选择哪一个。

   **答** CRD：一个因子，即压力，有 $6$ 次重复；$24$ 次运行不论批次随机地分配给材料，批次差异成为误差的一部分。RCBD：一个处理因子与一个区组因子，即批次；每个批次以随机顺序接受全部四种压力，模型是双因子可加模型，假定压力与批次没有交互效应。由于已知批次会有变化，且每个批次够做四次运行，RCBD 更可取；数据也证实了这一点（$\widehat{\mathrm{RE}}\approx1.9$ 至 $2.1$）。

3. 干扰因子按定义是不感兴趣的。我们需要检验它的效应吗，例如批次之间是否有显著差异？

   **答** 一般不需要：区组因子在模型中是为了减小误差，无论如何处理的检验都是有效的。对区组作正式检验是不合理的，因为区组既没有被随机化，也没有重复。不过，把 $\mathrm{MS}_{\mathrm{Blocks}}$ 与 $\mathrm{MS}_{\mathrm{E}}$ 比较，作为分区组是否必要和有效的检查仍然有用，这对规划未来的实验有意义。

4. 在移植物实验的两两比较中，如果用 Fisher 的 LSD 而不是 Tukey 方法，结论可能怎样不同？

   **答** Tukey 方法拒绝的每一对，LSD 也拒绝，因为 HSD $4.50$ 大于 LSD $3.33$；但 Tukey 没有拒绝的一对，LSD 仍可能拒绝。$8900-8500$ 就是这样（差 $3.90$，介于 $3.33$ 与 $4.50$ 之间）。

5. `pairwise.t.test` 也使用合并标准差。`with(graft, pairwise.t.test(Yield, PSI, p.adjust.method = "none"))` 是 RCBD 的 Fisher LSD 吗？

   **答** 不是。它像单因素分析那样合并四个压力组的方差，所以它的误差均方是自由度为 $20$ 的 $15.11$，其中包含批次变异。RCBD 的 LSD 使用自由度为 $15$ 的 $\mathrm{MS}_{\mathrm{E}}=7.33$，如 7.4 节的代码，或对拟合的 RCBD 模型使用 `agricolae::LSD.test`。

6. 对于随机区组，哪个假设表达"分区组是不必要的"？在可加模型 $y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij}$ 中如何检验它：$H_0\colon\beta_1=\cdots=\beta_b=0$，还是 $H_0\colon\sigma_\beta^2=0$？

   **答** $H_0\colon\sigma_\beta^2=0$；对于随机区组，各个 $\beta_j$ 是随机变量，不是参数。由定理 7.6.1，$\mathbb{E}[\mathrm{MS}_{\mathrm{Blocks}}]=\sigma^2+a\sigma_\beta^2$，$\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]=\sigma^2$，所以检验统计量是 $F_0=\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}$，在 $H_0$ 下 $\sim F_{b-1,(a-1)(b-1)}$。对移植物数据 $F_0=5.25$，$p=0.0055$。

7. RCBD 中的一个缺失值用命题 7.7.1 的最小二乘估计代替，然后分析补全的数据。与真实（未知）观测给出的误差平方和相比，补全数据的误差平方和一般是更小、更大，还是两者皆有可能？

   **答** 更小（至多相等）。插补值 $x$ 在可以放入该单元格的所有值中使 $\mathrm{SS}_{\mathrm{E}}$ 最小，而真实的观测是这些值之一；只有当真实观测恰好等于它的拟合值时才取等号。对移植物数据：$101.7$ 对 $110$。

8. 有一个缺失观测时，应当用 `summary(aov(Yield ~ PSI + Block, vas))` 还是 `summary(aov(Yield ~ Block + PSI, vas))` 来检验处理？

   **答** 用第二个。一项的序贯平方和只对它前面的项作调整，而处理的比较必须对区组作调整，因为区组在各处理之间不再平衡。两者的残差行相同。

9. 对 $\mathrm{SS}_{\mathrm{E}}(x)$ 求导，验证命题 7.7.1 的缺失值公式。

   **答** 把补全数据的残差写成 $x$ 的线性函数。单元格 $(k,l)$ 的残差为 $e_{kl}(x)=y_{kl}-\bar y_{k\cdot}-\bar y_{\cdot l}+\bar y_{\cdot\cdot}$，$x$ 以权 $1/b$ 进入 $\bar y_{i\cdot}$，以权 $1/a$ 进入 $\bar y_{\cdot j}$，以权 $1/(ab)$ 进入 $\bar y_{\cdot\cdot}$。由于可加模型的残差是数据在交互效应空间 $\mathcal{L}$ 上的投影，$\mathrm{SS}_{\mathrm{E}}(x)=\|P_{\mathcal{L}}(\boldsymbol{y}_0+x\boldsymbol{u})\|^2$，其中 $\boldsymbol{y}_0$ 在单元格 $(i,j)$ 处取 $0$，$\boldsymbol{u}$ 是该单元格的指示向量。于是 $\frac{\mathrm{d}}{\mathrm{d}x}\mathrm{SS}_{\mathrm{E}}=2\langle P_{\mathcal{L}}(\boldsymbol{y}_0+x\boldsymbol{u}),\boldsymbol{u}\rangle=2e_{ij}(x)$，因为 $P_{\mathcal{L}}$ 对称且幂等。令它为零得 $e_{ij}(x)=0$，即 $x=\bar y_{i\cdot}+\bar y_{\cdot j}-\bar y_{\cdot\cdot}$（均值由补全的数据算出），整理后就是命题证明中的 $x=(a\,y'_{i\cdot}+b\,y'_{\cdot j}-y'_{\cdot\cdot})/[(a-1)(b-1)]$。二阶导数 $2\|P_{\mathcal{L}}\boldsymbol{u}\|^2=2(a-1)(b-1)/(ab)>0$ 确认这是极小。

10. 在高尔夫实验中（$9$ 名球手，每人在 $3$ 种击球座高度下各击 $5$ 个球，顺序随机），指出模型 $y_{ijk}=\mu+\tau_i+\beta_j+\gamma_{ij}+\varepsilon_{ijk}$ 中的 $a$、$b$ 与 $n$，并解释为什么检验击球座高度的分母是交互均方而不是误差均方。

    **答** $a=3$ 种击球座高度，$b=9$ 名球手，$n=5$ 次开球（每名球手每种击球座高度）。球手是建议所针对的球手的一个随机样本，所以球手与击球座高度的交互效应是随机的，且 $\mathbb{E}[\mathrm{MS}_A]=\sigma^2+n\sigma_{\tau\beta}^2+bn\sum\tau_i^2/(a-1)$。在 $H_0$ 下它等于 $\mathbb{E}[\mathrm{MS}_{AB}]$，而不是 $\mathbb{E}[\mathrm{MS}_{\mathrm{E}}]$；除以 $\mathrm{MS}_{\mathrm{E}}$ 会忽略击球座高度效应在球手之间的变异，夸大证据（$F=12.68$ 而不是 $5.85$）。

11. 用四个试片作区组，在硬度计上比较四种压头（7.2.1 节）。设编码后的读数为

    | 压头 | 试片 1 | 试片 2 | 试片 3 | 试片 4 |
    |---|---|---|---|---|
    | 1 | 9.3 | 9.4 | 9.6 | 10.0 |
    | 2 | 9.4 | 9.3 | 9.8 | 9.9 |
    | 3 | 9.2 | 9.4 | 9.5 | 9.7 |
    | 4 | 9.7 | 9.6 | 10.0 | 10.2 |

    建立方差分析表，在 $\alpha=0.05$ 下检验压头之间是否有差异，并与忽略试片的分析比较。

    **答** 压头总和 $38.3$、$38.4$、$37.8$、$39.5$；试片总和 $37.6$、$37.7$、$38.9$、$39.8$；$y_{\cdot\cdot}=154.0$，$N=16$。$\mathrm{SS}_{\mathrm{T}}=1.290$，$\mathrm{SS}_{\mathrm{Tr}}=0.385$，$\mathrm{SS}_{\mathrm{Blocks}}=0.825$，$\mathrm{SS}_{\mathrm{E}}=0.080$，自由度 $9$，$\mathrm{MS}_{\mathrm{E}}=0.00889$。$F_0=(0.385/3)/0.00889=14.44>F_{3,9,0.05}=3.86$（$p=0.0009$）：压头有差异。忽略试片时，误差为 $(0.825+0.080)/12=0.0754$，自由度 $12$，$F_0=1.70$（$p=0.22$）：压头效应将完全检测不出来。这里 $\mathrm{MS}_{\mathrm{Blocks}}/\mathrm{MS}_{\mathrm{E}}=30.9$，精细的相对效率约为 $6.7$。

12. $a=2$ 的 RCBD 是配对设计。对思考题 11 中的前两种压头，计算配对 $t$ 统计量与 RCBD 的 $F$ 统计量，并验证命题 7.3.1。

    **答** 压头 1 减压头 2 的差为 $-0.1$、$0.1$、$-0.2$、$0.1$，$\bar d=-0.025$，$s_d=0.15$，所以 $t_0=-0.025/(0.15/2)=-0.333$，$t_0^2=0.111$。含这两种压头的 RCBD 有 $\mathrm{SS}_{\mathrm{Tr}}=4\times0.025^2/2=0.00125$，$\mathrm{SS}_{\mathrm{E}}=3\times0.15^2/2=0.03375$，自由度 $3$，所以 $F_0=0.00125/0.01125=0.111=t_0^2$。
