---
title: 双因子方差分析、诊断与补救
description: 两个因子的单元格均值模型与因子效应模型，主效应与交互效应，双因子方差分析表及其 F 检验，不平衡数据的最小二乘均值；方差分析模型的残差诊断与方差齐性检验；加权方差分析、Box–Cox 变换与 Kruskal–Wallis 检验。
source_hash: 4915fbee9945
---

作为本课程的最后一章，本章从两个方向推广 [3.3.12](/3.3.12) 与 [3.3.13](/3.3.13) 的方差分析。第一，处理可以同时按两个因子分类；这时除了"每个因子是否起作用"之外还出现了一个新问题：一个因子的效应是否依赖于另一个因子的水平。这就是在含乘积项的回归模型中已经见过的**交互效应**（[3.3.10](/3.3.10)）。双因子方差分析表用 $F$ 检验回答这些问题，数据不平衡时用最小二乘均值概括各因子。第二，我们把 [3.3.5](/3.3.5) 与 [3.3.11](/3.3.11) 的回归诊断以及 [3.3.6](/3.3.6) 与 [3.3.12](/3.3.12) 的补救措施移用到方差分析模型：残差图、方差齐性检验、加权方差分析、变换与秩检验。多个因子的设计是实验设计（[3.8](/3.8)）的内容；响应为向量时的多元推广是**多元方差分析**（[3.4.10](/3.4.10)）。

## 14.1. 双因子方差分析模型

### 14.1.1. 数据与假设

响应 $Y$ 是连续的，现在有两个分类解释变量（因子）：处理按两种方式分类，构成一张二维表。因子 $A$ 的水平为 $i=1,\dots,a$，因子 $B$ 的水平为 $j=1,\dots,b$；每个组合 $(i,j)$ 是一个单元格，$Y_{ijk}$ 是单元格 $(i,j)$ 中的第 $k$ 个观测。除非另有说明，我们假定所有单元格的样本量相等，$n_{ij}=n$（平衡设计），于是 $n_T=abn$。

| | $A=1$ | $\cdots$ | $A=a$ |
|---|---|---|---|
| $B=1$ | $Y_{111},\dots,Y_{11n}$ | $\cdots$ | $Y_{a11},\dots,Y_{a1n}$ |
| $\vdots$ | $\vdots$ | | $\vdots$ |
| $B=b$ | $Y_{1b1},\dots,Y_{1bn}$ | $\cdots$ | $Y_{ab1},\dots,Y_{abn}$ |

我们假定观测服从正态分布，其均值只可能依赖于因子 $A$ 与 $B$ 的水平，方差相同，并且相互独立。

**例 14.1.1** 一家面包店研究货架陈列对面包销量的影响。$Y$ 是售出的面包箱数；因子 $A$ 是陈列的高度，有 $a=3$ 个水平（底层、中层、顶层），因子 $B$ 是陈列的宽度，有 $b=2$ 个水平（常规、加宽）。$3\times2=6$ 个处理组合各在 $n=2$ 家商店中使用，所以 $n_T=12$。

| 宽度 \ 高度 | 1（底层） | 2（中层） | 3（顶层） |
|---|---|---|---|
| 1（常规） | 47, 43 | 62, 68 | 41, 39 |
| 2（加宽） | 46, 40 | 67, 71 | 42, 46 |

### 14.1.2. 单元格均值模型

**定义 14.1.1（双因子单元格均值模型）** **双因子单元格均值模型**为

$$
Y_{ijk}=\mu_{ij}+\varepsilon_{ijk},\qquad \varepsilon_{ijk}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
其中 $\mu_{ij}$ 是单元格 $(i,j)$ 中所有观测的理论均值；等价地，$Y_{ijk}\sim\mathcal{N}(\mu_{ij},\sigma^2)$ 相互独立。参数是 $ab$ 个单元格均值 $\mu_{ij}$ 与 $\sigma^2$。

这就是把 $ab$ 个单元格看作单个因子的各水平的单因子单元格均值模型，因此 [3.3.12](/3.3.12) 的结论直接适用。用单元格均值 $\bar Y_{ij\cdot}=\sum_kY_{ijk}/n$ 估计 $\mu_{ij}$，并把各单元格方差 $s_{ij}^2=\sum_k(Y_{ijk}-\bar Y_{ij\cdot})^2/(n-1)$ 按与自由度成比例的权重合并：

$$
s^2=\frac{\sum_{i,j}(n_{ij}-1)s_{ij}^2}{\sum_{i,j}(n_{ij}-1)},\qquad\text{which for }n_{ij}=n\text{ is }s^2=\frac{1}{ab}\sum_{i,j}s_{ij}^2,
$$
即各单元格方差的平均。因子水平的边际均值（marginal mean）是对另一个因子求平均：$A$ 的水平 $i$ 为 $\bar Y_{i\cdot\cdot}$，$B$ 的水平 $j$ 为 $\bar Y_{\cdot j\cdot}$。

面包店数据的单元格均值与边际均值为

| 宽度 \ 高度 | 1 | 2 | 3 | 宽度均值 |
|---|---|---|---|---|
| 1 | 45 | 65 | 40 | 50 |
| 2 | 43 | 69 | 44 | 52 |
| 高度均值 | 44 | 67 | 42 | 51 |

各单元格标准差为 $2.83, 4.24, 4.24, 2.83, 1.41, 2.83$，所以 $s^2=(8+18+18+8+2+8)/6=10.33$，$s=3.215$。用六个单元格示性变量作回归来拟合单元格均值模型，结果相同：每个估计的标准误为 $s/\sqrt2=2.273$。

```r
a <- read.table("CH19TA07.txt")
names(a) <- c("sales", "height", "width", "store")
a$height <- factor(a$height); a$width <- factor(a$width)
a$cell <- factor(paste0("h", a$height, "w", a$width))
summary(lm(sales ~ 0 + cell, data = a))                  # cell means model
aggregate(sales ~ height * width, data = a, FUN = mean)  # cell means by hand
with(a, interaction.plot(x.factor = height, trace.factor = width,
                         response = sales, fun = mean))   # interaction plot
```

自然的问题是两个因子的主效应（main effects）。陈列高度（$A$）是否影响销量？如果是，就比较顶层与中层、顶层与底层、中层与底层。宽度（$B$）是否影响销量？如果是，就比较常规与加宽。但这些因子水平的比较有意义吗？这取决于高度对销量的效应是否依赖于宽度，以及宽度的效应是否依赖于高度。如果是，两个因子就存在交互作用，边际比较可能显著却没有意义：对另一个因子的水平求平均，会掩盖大小乃至符号都在变化的效应。

交互作用图（interaction plot）把单元格均值 $\bar Y_{ij\cdot}$ 对一个因子的水平作图，另一个因子的每个水平画一条线。没有交互作用时各线平行：$A$ 的效应在 $B$ 的每个水平上都相同，只差一个常数平移。不平行的线表示有交互作用；相交的线表示连一个因子效应的方向都依赖于另一个因子。面包店数据的两条线几乎平行：两种宽度下都是中层货架卖得最好。

![左：面包店单元格均值的交互作用图，销量对货架高度作图，每种宽度一条线。中、右：示意图，分别是没有交互作用（平行线）与相交的交互作用；后者中因子 A 的边际均值相等，尽管 A 在 B 的每个水平上都有很强的效应。](./plots/interaction-plots.py)

### 14.1.3. 因子效应模型

**定义 14.1.2（双因子因子效应模型）** 定义总均值与因子水平均值

$$
\mu_{\cdot\cdot}=\frac{1}{ab}\sum_{i,j}\mu_{ij},\qquad \mu_{i\cdot}=\frac1b\sum_j\mu_{ij},\qquad \mu_{\cdot j}=\frac1a\sum_i\mu_{ij}.
$$
$A$ 与 $B$ 的**主效应**为 $\alpha_i=\mu_{i\cdot}-\mu_{\cdot\cdot}$ 与 $\beta_j=\mu_{\cdot j}-\mu_{\cdot\cdot}$，**交互效应**为

$$
(\alpha\beta)_{ij}=\mu_{ij}-(\mu_{\cdot\cdot}+\alpha_i+\beta_j)=\mu_{ij}-\mu_{i\cdot}-\mu_{\cdot j}+\mu_{\cdot\cdot}.
$$
记 $\mu=\mu_{\cdot\cdot}$，**双因子因子效应模型**为

$$
Y_{ijk}=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}+\varepsilon_{ijk},\qquad \varepsilon_{ijk}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
约束为 $\alpha_\cdot=\sum_i\alpha_i=0$，$\beta_\cdot=\sum_j\beta_j=0$，对所有 $j$ 有 $(\alpha\beta)_{\cdot j}=\sum_i(\alpha\beta)_{ij}=0$，对所有 $i$ 有 $(\alpha\beta)_{i\cdot}=\sum_j(\alpha\beta)_{ij}=0$。

主效应 $\alpha_i$ 是对 $A$ 的水平 $i$ 所作的总均值调整，$\beta_j$ 是对 $B$ 的水平 $j$ 所作的调整。交互作用 $(\alpha\beta)_{ij}$ 是完全可加模型 $\mu+\alpha_i+\beta_j$ 未能解释的部分：它是同时考虑 $i$ 与 $j$ 的附加调整，无法由前面的调整解释。没有交互作用当且仅当所有 $(\alpha\beta)_{ij}=0$，即 $\mu_{ij}-\mu_{i'j}$ 不依赖于 $j$（交互作用图中的平行线）。

交互效应的约束共 $a+b$ 个方程，其中 $a+b-1$ 个线性无关（各行方程之和等于各列方程之和）。因此参数共有 $1+(a-1)+(b-1)+(a-1)(b-1)=ab$ 个自由分量，与单元格均值的个数相同；模型有 $ab-1$ 个自由度：$A$ 占 $a-1$，$B$ 占 $b-1$，交互作用占 $(a-1)(b-1)$。

**命题 14.1.1** 在平衡设计中，和为零约束下的最小二乘估计量为

$$
\hat\mu=\bar Y_{\cdot\cdot\cdot},\qquad \hat\alpha_i=\bar Y_{i\cdot\cdot}-\bar Y_{\cdot\cdot\cdot},\qquad \hat\beta_j=\bar Y_{\cdot j\cdot}-\bar Y_{\cdot\cdot\cdot},\qquad \widehat{(\alpha\beta)}_{ij}=\bar Y_{ij\cdot}-\bar Y_{i\cdot\cdot}-\bar Y_{\cdot j\cdot}+\bar Y_{\cdot\cdot\cdot},
$$
其中 $\bar Y_{\cdot\cdot\cdot}=\sum_{i,j,k}Y_{ijk}/(abn)$，并且 $\hat\mu_{i\cdot}=\bar Y_{i\cdot\cdot}$，$\hat\mu_{\cdot j}=\bar Y_{\cdot j\cdot}$。

**证明** 单元格均值的最小二乘估计量为 $\hat\mu_{ij}=\bar Y_{ij\cdot}$（定理 12.2.1），而定义 14.1.2 的参数都是单元格均值的线性函数；$n_{ij}=n$ 时，把各 $\bar Y_{ij\cdot}$ 对 $j$、对 $i$ 或对两者求平均，分别得到 $\bar Y_{i\cdot\cdot}$、$\bar Y_{\cdot j\cdot}$ 与 $\bar Y_{\cdot\cdot\cdot}$。$\square$

对面包店数据，$\hat\mu=51$，$\hat\alpha=(-7,16,-9)$，$\hat\beta=(-1,1)$；交互效应的估计在底层为 $\pm2$，在其余两层为 $\pm1$，例如 $\widehat{(\alpha\beta)}_{11}=45-44-50+51=2$。

R 使用不同的约束。调用 `lm(sales ~ height * width)` 以每个因子的第一个水平为基线，即 $\alpha_1=0$，$\beta_1=0$，对所有 $j$ 有 $(\alpha\beta)_{1j}=0$，对所有 $i$ 有 $(\alpha\beta)_{i1}=0$；自由参数的个数相同。

| 常用约束 | 自由度 | R 使用的约束 | 自由度 |
|---|---|---|---|
| $\sum_i\alpha_i=0$ | $a-1$ | $\alpha_1=0$ | $a-1$ |
| $\sum_j\beta_j=0$ | $b-1$ | $\beta_1=0$ | $b-1$ |
| 对所有 $j$ 有 $\sum_i(\alpha\beta)_{ij}=0$，对所有 $i$ 有 $\sum_j(\alpha\beta)_{ij}=0$ | $(a-1)(b-1)$ | 对所有 $j$ 有 $(\alpha\beta)_{1j}=0$，对所有 $i$ 有 $(\alpha\beta)_{i1}=0$ | $ab-(a+b-1)=(a-1)(b-1)$ |

对面包店数据，R 给出截距 $45$（单元格 $(1,1)$），$\hat\alpha_2=20$，$\hat\alpha_3=-5$，$\hat\beta_2=-2$，$\widehat{(\alpha\beta)}_{22}=\widehat{(\alpha\beta)}_{32}=6$，主效应系数的标准误为 $3.215$，交互作用系数的为 $4.546$；例如 $\hat\mu_{22}=45+20-2+6=69$。这些系数的单个 $t$ 检验是在把各单元格与基线比较，很少是我们关心的问题；在方差分析中我们关心的是水平之间的差异，而不是模型的预测能力，这些差异由方差分析表来检验。

## 14.2. 双因子方差分析表

总平方和分解为四部分，每一部分都是估计效应的平方对所有观测求和：

$$
\begin{aligned}
\mathrm{SSA}&=\sum_{i,j,k}\hat\alpha_i^2=bn\sum_i(\bar Y_{i\cdot\cdot}-\bar Y_{\cdot\cdot\cdot})^2, & \mathrm{SSB}&=\sum_{i,j,k}\hat\beta_j^2=an\sum_j(\bar Y_{\cdot j\cdot}-\bar Y_{\cdot\cdot\cdot})^2,\\
\mathrm{SSAB}&=\sum_{i,j,k}\widehat{(\alpha\beta)}_{ij}^2=n\sum_{i,j}\widehat{(\alpha\beta)}_{ij}^2, & \mathrm{SSE}&=\sum_{i,j,k}(Y_{ijk}-\bar Y_{ij\cdot})^2,
\end{aligned}
$$
在平衡设计中 $\mathrm{SSTO}=\sum_{i,j,k}(Y_{ijk}-\bar Y_{\cdot\cdot\cdot})^2=\mathrm{SSA}+\mathrm{SSB}+\mathrm{SSAB}+\mathrm{SSE}$，因为在约束下四个分量的交叉乘积之和为零。

| 来源 | 自由度 | 平方和 | 均方 | $F$ |
|---|---|---|---|---|
| $A$ | $a-1$ | $\mathrm{SSA}$ | $\mathrm{MSA}=\mathrm{SSA}/(a-1)$ | $\mathrm{MSA}/\mathrm{MSE}$ |
| $B$ | $b-1$ | $\mathrm{SSB}$ | $\mathrm{MSB}=\mathrm{SSB}/(b-1)$ | $\mathrm{MSB}/\mathrm{MSE}$ |
| $AB$ | $(a-1)(b-1)$ | $\mathrm{SSAB}$ | $\mathrm{MSAB}=\mathrm{SSAB}/[(a-1)(b-1)]$ | $\mathrm{MSAB}/\mathrm{MSE}$ |
| 误差 | $ab(n-1)$ | $\mathrm{SSE}$ | $\mathrm{MSE}=\mathrm{SSE}/[ab(n-1)]$ | |
| 总计 | $abn-1$ | $\mathrm{SSTO}$ | | |

**定理 14.2.1（期望均方）** 在平衡的双因子因子效应模型中，

$$
\begin{aligned}
\mathbb{E}[\mathrm{MSE}]&=\sigma^2, & \mathbb{E}[\mathrm{MSA}]&=\sigma^2+\frac{bn}{a-1}\sum_i\alpha_i^2,\\
\mathbb{E}[\mathrm{MSB}]&=\sigma^2+\frac{an}{b-1}\sum_j\beta_j^2, & \mathbb{E}[\mathrm{MSAB}]&=\sigma^2+\frac{n}{(a-1)(b-1)}\sum_{i,j}(\alpha\beta)_{ij}^2.
\end{aligned}
$$
此外 $\mathrm{SSE}/\sigma^2\sim\chi^2_{ab(n-1)}$，四个平方和相互独立；相应的效应为零时，$\mathrm{SSA}/\sigma^2$、$\mathrm{SSB}/\sigma^2$、$\mathrm{SSAB}/\sigma^2$ 分别服从自由度为 $a-1$、$b-1$、$(a-1)(b-1)$ 的 $\chi^2$ 分布。

证明与单因子情形（定理 12.2.2）相同，利用的是：四个分量是 $\boldsymbol{Y}$ 在两两正交的子空间上的正交投影。每个均方在其效应为零时期望为 $\sigma^2$，否则更大，由此得到三个 $F$ 检验：

| 假设 | 统计量 | 零分布 |
|---|---|---|
| $H_{0A}\colon\alpha_i=0$ 对所有 $i$；$H_{1A}\colon$ 至少有一个 $\alpha_i\ne0$ | $F_A=\mathrm{MSA}/\mathrm{MSE}$ | $F_{a-1,\,ab(n-1)}$ |
| $H_{0B}\colon\beta_j=0$ 对所有 $j$；$H_{1B}\colon$ 至少有一个 $\beta_j\ne0$ | $F_B=\mathrm{MSB}/\mathrm{MSE}$ | $F_{b-1,\,ab(n-1)}$ |
| $H_{0AB}\colon(\alpha\beta)_{ij}=0$ 对所有 $(i,j)$；$H_{1AB}\colon$ 至少有一个 $(\alpha\beta)_{ij}\ne0$ | $F_{AB}=\mathrm{MSAB}/\mathrm{MSE}$ | $F_{(a-1)(b-1),\,ab(n-1)}$ |

$p$ 值由这些 $F$ 分布计算，$p$ 值不超过 $0.05$ 时认为所检验的效应统计显著。应先考察交互作用：若交互作用显著，主效应的解释就要格外小心，分析应转向单元格均值（例如在 $B$ 的每个水平上分别比较 $A$ 的各水平）。

**例 14.2.1** 对面包店数据：

```r
fit <- lm(sales ~ height * width, data = a)
anova(fit)
```

| 来源 | 自由度 | 平方和 | 均方 | $F$ | $p$ |
|---|---|---|---|---|---|
| 高度 | 2 | 1544 | 772 | 74.71 | $5.8\times10^{-5}$ |
| 宽度 | 1 | 12 | 12 | 1.16 | 0.323 |
| 高度 × 宽度 | 2 | 24 | 12 | 1.16 | 0.375 |
| 误差 | 6 | 62 | 10.33 | | |
| 总计 | 11 | 1642 | | | |

设计中有 $6$ 个单元格，所以模型有 $6-1=5$ 个自由度（$\mathrm{SSA}+\mathrm{SSB}+\mathrm{SSAB}=1580$，整个模型的 $F=30.58$）。交互作用不显著：陈列高度的效应在常规与加宽两种陈列下相近。陈列高度影响面包销量，而宽度没有明显的效应。

接下来需要解释高度的效应，它有底层、中层、顶层三个水平。可以把数据重新作为高度的单因子方差分析，用 [3.3.13](/3.3.13) 的方法；更好的做法是在双因子模型中比较各高度，从而把宽度保留在误差结构中。注意误差自由度依赖于模型：只有高度时为 $n_T-a=9$，两个因子且无交互作用时为 $n_T-a-b+1=8$，有交互作用时为 $n_T-ab=6$。在可加模型中用 Tukey 方法：

```r
mod <- aov(sales ~ height + width, data = a)
TukeyHSD(mod, "height")
```

得到差 $\hat\mu_{2\cdot}-\hat\mu_{1\cdot}=23$，95% 族区间 $[16.4,\ 29.6]$；$\hat\mu_{3\cdot}-\hat\mu_{1\cdot}=-2$，区间 $[-8.6,\ 4.6]$；$\hat\mu_{3\cdot}-\hat\mu_{2\cdot}=-25$，区间 $[-31.6,\ -18.4]$：中层货架比底层或顶层多卖约 23 到 25 箱，而底层与顶层没有差别。

## 14.3. 最小二乘均值

在平衡设计中，$A$ 的某个水平的边际均值是对 $B$ 各水平的等权平均。在不平衡设计中，原始边际均值 $\bar Y_{i\cdot\cdot}$ 按样本量对各单元格加权，因此 $A$ 的两个水平之间的差异可能反映的是 $B$ 各水平混合比例的不同，而不是 $A$ 的效应。

**定义 14.3.1（最小二乘均值）** 一个因子各水平的**最小二乘均值**（LS 均值）是拟合模型在一个平衡的参考网格上的预测值的平均：对 $A$ 的水平 $i$，

$$
\hat\mu_{i\cdot}^{\mathrm{LS}}=\frac1b\sum_{j=1}^b\hat\mu_{ij},
$$
其中 $\hat\mu_{ij}$ 是拟合模型对单元格 $(i,j)$ 预测的均值（若有协变量，则把它们取在参考值上，例如其均值）。

最小二乘均值也称估计边际均值、预测（总体）边际、预测均值或基于模型的均值。数据不平衡或有协变量时用它来比较各组的响应；SAS 中用 `LSMEANS`、Stata 中用 `margins`、R 中用程序包 `emmeans` 计算。在平衡设计中它等于算术边际均值。

**例 14.3.1** 对平衡的面包店数据，单因子模型 `lm(sales ~ 0 + height)` 与可加模型 `lm(sales ~ height + width)` 给出相同的高度均值 $44$、$67$、$42$，只有标准误与自由度不同（自由度 $9$ 时为 $1.65$，自由度 $8$ 时为 $1.64$）。现在删去第一个观测（单元格 $(1,1)$ 中的 47）。底层的原始均值变为 $(43+46+40)/3=43$，单因子模型给出 $43$。可加模型的系数为 $41$（截距）、$24.5$（高度 2）、$-0.5$（高度 3）与 $3$（宽度 2），所以它预测的单元格均值为

| 宽度 \ 高度 | 1 | 2 | 3 |
|---|---|---|---|
| 1 | 41 | 65.5 | 40.5 |
| 2 | 44 | 68.5 | 43.5 |

最小二乘均值为 $(41+44)/2=42.5$、$67$ 与 $42$。原始均值 $43$ 中，底层剩下的三个观测有两个来自销量较高的加宽陈列；最小二乘均值 $42.5$ 消除了这种不平衡。"预测均值"这个名称就来自这一构造：一个水平的最小二乘均值是模型在另一个因子各水平上的预测值的平均。

```r
library(emmeans)
fit3 <- lm(sales ~ height + width, data = a[-1, ])
emmeans(fit3, ~ height)                                        # LS-means 42.5, 67, 42
emmeans(aov(sales ~ height + width, data = a[-1, ]),
        pairwise ~ height, adjust = "tukey")                   # Tukey comparisons of LS-means
```

在含交互作用的模型中，`emmeans` 对拟合的单元格均值 $\bar Y_{ij\cdot}$ 求平均（这里底层为 $43$ 与 $43$），并警告由于该因子涉及交互作用，结果可能有误导性：交互作用真实存在时，对 $B$ 各水平的平均可能不描述任何实际的条件。

## 14.4. 方差分析模型的诊断

### 14.4.1. 残差图

回归的诊断方法经过一些修改后可以用于方差分析。在单因子模型中，预测值是单元格均值 $\hat Y_{ij}=\bar Y_{i\cdot}$，残差是观测与其单元格均值之差 $e_{ij}=Y_{ij}-\bar Y_{i\cdot}$。我们要寻找离群值、依赖于水平的方差以及非正态的误差：

- 把响应 $Y$ 对因子水平作图；
- 当观测的顺序可得且有意义时，用残差的序列图检查独立性；
- 用残差的**正态 QQ 图**检查正态性；
- 把残差对拟合值（单元格均值）或因子水平作图，检查方差齐性；
- 尽可能利用额外的信息，例如测量的时间或地点。

**例 14.4.1** 比较四个品牌的防锈剂，$r=4$，每个品牌 $n=10$ 个单位；响应度量防锈剂的效果。响应对品牌的散点图显示均值看起来不同、散布相近。方差分析给出 $\mathrm{SSTR}=15953$（自由度 $3$）与 $\mathrm{SSE}=221$（自由度 $36$），$F=866.1$，$p<2\times10^{-16}$。

```r
a1 <- read.table("CH17TA02.txt")
colnames(a1) <- c("eff", "brand", "unit")
a1$brand <- as.factor(a1$brand)
plot(eff ~ brand, data = a1)                # responses against the factor
fit1 <- aov(eff ~ brand, data = a1)
summary(fit1)
par(mfrow = c(2, 2)); plot(fit1); par(mfrow = c(1, 1))   # residual plots
```

对假设的偏离按回归中的方式判断：

- 非正态性：用正态概率图。若方差不等，普通残差的图常常会错误地显示非正态，因此应先作变换（第 14.5 节）再重新检查。正态性是最不重要的假设：几乎所有方差分析方法对正态性的轻微偏离都是稳健的。
- 非独立性：若数据按时间顺序获得，把残差对时间作图。出现规律就表示不独立：正的序列相关（相邻残差倾向于同号）或负的序列相关（相邻残差倾向于异号）。非独立性通常对推断有严重影响，使之失效。
- 极端值：与前面一样，用学生化残差或学生化删除残差判别离群值（[3.3.11](/3.3.11)）。在单因子模型中，$Y_{ij}$ 的**杠杆值**，即**帽子矩阵**的对角元，等于 $1/n_i$，因为拟合值 $\bar Y_{i\cdot}$ 给本水平的每个观测权重 $1/n_i$。单元格大小相等时，所有杠杆值相等，没有哪个点的杠杆比别的点大。

### 14.4.2. 方差齐性检验

形式检验可以补充图形。正态性检验有 **Shapiro–Wilk 检验**、**Anderson–Darling 检验**与 **Kolmogorov–Smirnov 检验**。对方差齐性（**同方差性**），

$$
H_0\colon\sigma_1^2=\sigma_2^2=\cdots=\sigma_r^2\qquad\text{versus}\qquad H_1\colon\text{not all }\sigma_i^2\text{ are equal},
$$
有几种检验可用；这很重要，因为方差分析的结果可能对方差齐性假设敏感，而其中一些检验本身又对正态性假设敏感。**Bartlett 检验**本质上是正态假设下 $H_0$ 的**似然比检验**，对非正态性非常敏感；修正的 **Levene 检验**（即 [3.3.5](/3.3.5) 的 **Brown–Forsythe 检验**）对与各水平中位数的绝对离差 $\lvert Y_{ij}-\tilde Y_i\rvert$ 作单因子方差分析，是稳健的；Hartley 检验最为简单。

**定义 14.4.1（Hartley 检验）** 设 $r$ 个水平的样本量相等，$n_i=n$，误差正态。方差齐性的 **Hartley 检验**使用

$$
H^*=\frac{\max_is_i^2}{\min_is_i^2},
$$
在 $H_0$ 下它服从 Hartley 制表的分布 $H(r,n-1)$；$H^*$ 大时拒绝 $H_0$。

作为粗略的经验法则，最大标准差与最小标准差之比超过 $2$，即 $H^*>4$，就值得关注。

**例 14.4.2** 比较五种焊剂，每种 $n=8$ 个焊点；响应是拉力强度，即拉断焊点所需的力（磅）。散点图让人怀疑散布是否相同。

```r
library(car)
leveneTest(a1$strength, a1$type)            # modified Levene (center = median)
```

修正的 Levene 检验给出 $F=2.936$，自由度 $4$ 与 $35$，$p=0.034$，因此拒绝方差相等的假设。各类型的样本方差为 $1.531$、$1.570$、$6.183$、$0.667$、$0.592$，所以 $H^*=6.183/0.592=10.44$，远大于 $4$，也超过 $5\%$ 临界值 $H_{0.95}(5,7)\approx9.7$。

实验设计的经验对这些结论有所限定。只要样本量相等，方差分析的 $F$ 检验受方差不等的影响很小；单元格大小相等时，Scheffé 多重比较方法对方差不等也相当稳健；其他两两比较方法则可能受到方差不等的严重影响。使用相等的样本量可以把这些影响降到最低，这正是平衡设计重要的原因之一。

## 14.5. 补救措施

方差分析模型的补救措施与回归类似：

- 删除离群值，但先要问删除是否重要、是否正当；
- 使用权重（加权最小二乘）；
- 变换响应；
- 使用非参数方法。

### 14.5.1. 加权方差分析

对焊剂数据，方差齐性假设被拒绝，又没有明显的离群值，所以考虑加权方差分析。在加权回归（[3.3.12](/3.3.12)）中，我们为标准差如何依赖于解释变量建模，并使用与估计方差成反比的权重。有了因子，事情更简单：计算每个水平的**样本方差** $s_i^2$，以其倒数 $w_{ij}=1/s_i^2$ 作为权重。

```r
library(plyr)
a2 <- ddply(a1, ~type, summarise, freq = length(strength),
            mean = mean(strength), s2 = var(strength))
a2$wt <- 1 / a2$s2
a3 <- merge(a1, a2, by = "type")
weightedfit <- lm(strength ~ type, data = a3, weights = wt)
anova(weightedfit)
```

加权方差分析给出处理平方和 $324.21$（自由度 $4$）与残差平方和 $35.00$（自由度 $35$），所以 $F=81.05$，$p<2.2\times10^{-16}$。残差均方恰为 $1$：在水平 $i$ 内所有权重都等于 $1/s_i^2$，所以加权拟合值仍是各水平均值，加权误差平方和为 $\sum_i(n_i-1)s_i^2/s_i^2=n_T-r$。因此 $F$ 统计量就是加权处理均方本身，是一种让每个水平按其精度计入的水平均值比较。

### 14.5.2. 变换

**例 14.5.1** 一项研究记录了三个地点的计算机故障间隔时间，每个地点五个间隔：

| 地点 | 故障间隔时间 |
|---|---|
| 1 | 4.41, 100.65, 14.45, 47.13, 85.21 |
| 2 | 8.24, 81.16, 7.35, 12.29, 1.61 |
| 3 | 106.19, 33.83, 78.88, 342.81, 44.33 |

散点图显示分布严重右偏（$342.81$ 是离群值，还是分布本身偏斜？），而且散布随均值增大：样本方差分别为 $1789$、$1103$ 与 $16167$。**Box–Cox 变换**（[3.4.4](/3.4.4)、[3.3.6](/3.3.6)）选取使变换后响应的单因子模型轮廓似然最大的幂 $\lambda$。

```r
library(MASS)
a3 <- read.table("CH18TA05.txt")
colnames(a3) <- c("time", "location", "interval")
bc <- boxcox(time ~ as.factor(location), data = a3, lambda = seq(-2, 2, by = 0.2))
lambda <- bc$x[which.max(bc$y)]             # about 0.10
a3$logtime <- log(a3$time)                  # lambda = 0 is within the confidence interval
```

最大值在 $\hat\lambda\approx0.10$ 处，近似 95% 置信区间约为 $[-0.2,\ 0.4]$，包含 $0$，所以可以直接取对数。变换后各方差为 $1.74$、$1.97$ 与 $0.82$：散布稳定得多，可以对 $\log Y$ 作方差分析。

![左：各地点的计算机故障间隔时间。中：Box-Cox 轮廓对数似然及 lambda 的近似 95% 置信区间。右：各地点取对数后的时间。](./plots/box-cox-failures.py)

### 14.5.3. 非参数检验

非参数方法不依赖于误差项的分布；通常唯一的要求是分布连续。对单因子方差分析，假设是所研究的 $r$ 个总体具有连续分布，且只在位置上不同。

**定义 14.5.1（Kruskal–Wallis 检验）** 把全部 $n_T$ 个观测合在一起从 $1$ 到 $n_T$ 排秩，记 $\bar R_{i\cdot}$ 为水平 $i$ 中观测的平均秩。**Kruskal–Wallis 检验**在

$$
H=\frac{12}{n_T(n_T+1)}\sum_{i=1}^rn_i\Big(\bar R_{i\cdot}-\frac{n_T+1}{2}\Big)^2
$$
较大时拒绝"$r$ 个分布全都相同"的假设；其零分布近似为 $\chi^2_{r-1}$（小样本有精确表）。

$H$ 是由秩算出的处理平方和除以秩的方差 $n_T(n_T+1)/12$；$r=2$ 时它等价于双侧的 **Wilcoxon 秩和检验**（[3.2.6](/3.2.6)）。由于只用到秩，检验对离群值和偏斜不敏感，并且在响应的任何单调递增变换下不变。

```r
kruskal.test(eff ~ brand, data = a1)        # rust inhibitor data
```

对防锈剂数据，Kruskal–Wallis 统计量为 $33.70$，自由度 $3$，$p=2.3\times10^{-7}$，证实了 $F$ 检验发现的品牌之间的巨大差异。

## 小结 {#summary}

- 双因子单元格均值模型 $Y_{ijk}=\mu_{ij}+\varepsilon_{ijk}$ 是以 $ab$ 个单元格为水平的单因子模型；因子效应模型 $\mu_{ij}=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}$ 把单元格均值分解为主效应与交互效应，由和为零约束识别（R 改用基线约束）。
- 双因子方差分析表把 $\mathrm{SSTO}=\mathrm{SSA}+\mathrm{SSB}+\mathrm{SSAB}+\mathrm{SSE}$ 分解，自由度分别为 $a-1$、$b-1$、$(a-1)(b-1)$ 与 $ab(n-1)$；每个效应都与 $\mathrm{MSE}$ 比较来检验。解释主效应之前先考察交互作用（及交互作用图）。
- 最小二乘均值是模型预测的单元格均值对另一个因子各水平的平均；在不平衡设计中它与原始边际均值不同。
- 方差分析的诊断使用相对单元格均值的残差；正态性最不重要，独立性最重要。方差齐性用 Bartlett 检验、修正的 Levene 检验与 Hartley 检验检查；平衡设计使 $F$ 检验对方差不等稳健。
- 补救措施有权重 $w=1/s_i^2$ 的加权方差分析、由 Box–Cox 选取的变换，以及基于秩的 Kruskal–Wallis 检验。
