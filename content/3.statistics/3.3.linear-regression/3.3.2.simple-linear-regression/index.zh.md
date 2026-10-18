---
title: 简单线性回归
description: 一般误差与正态误差下的简单线性回归模型、模型假设（LINE）与参数的含义；最小二乘估计、拟合值与残差、作为误差方差估计的误差均方，以及极大似然估计，并以比萨斜塔数据在 R 中演示。
source_hash: 928b338b91ea
---

上一章以二元正态分布的回归函数 $\mathbb{E}(Y\mid X=x)$ 结束。然而在大多数应用中，$X$ 并不像 $Y$ 那样随机：它是试验者选定的剂量、年份或批量。本章建立**简单线性回归模型**：响应的均值是一个预测变量的线性函数，对这条直线的偏离是随机误差；并研究它的两种经典估计方法。**最小二乘法**只需要关于误差均值和方差的假设；**极大似然估计**需要误差的分布，而在正态误差下两者给出同一条直线。这个模型在 [3.2.3](/3.2.3) 中已简单出现过，这里完整地展开，其中的残差将在 [3.3.5](/3.3.5) 中用于模型检验。参数的推断见 [3.3.3](/3.3.3)，多个预测变量时的矩阵形式见 [3.3.7](/3.3.7)。

## 2.1. 简单线性回归模型

### 2.1.1. 数据与模型

我们观测 $n$ 对数据 $(X_1,Y_1),\dots,(X_n,Y_n)$；每一对 $(X_i,Y_i)$ 称为一个样本点（case），$X_i$ 是解释变量的第 $i$ 个观测值，$Y_i$ 是第 $i$ 个观测到的响应，$n$ 是**样本量**。确定性的（函数）关系 $Y=f(X)$ 会让所有点恰好落在一条曲线上；统计关系则允许观测值在曲线周围散布。

**定义 2.1.1（简单线性回归模型）** **简单线性回归模型**为

$$
Y_i=\beta_0+\beta_1X_i+\varepsilon_i,\qquad i=1,\dots,n,
$$
其中 $X_i$ 是已知常数，$\beta_0$（**截距**）与 $\beta_1$（**斜率**）是未知参数，**随机误差项** $\varepsilon_i$ 满足 $\mathbb{E}(\varepsilon_i)=0$，$\operatorname{Var}(\varepsilon_i)=\sigma^2$，且当 $i\ne j$ 时 $\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=0$。

模型称为"简单"，是因为只有一个预测变量；称为"线性"，是因为它关于参数 $\beta_0,\beta_1$ 是线性的（这里关于预测变量也是线性的）。误差项代表响应的内在随机性：不由 $X$ 决定的那一部分，无论它来自测量误差、遗漏的变量还是真正的随机性。参数 $\beta_0$、$\beta_1$ 和 $\sigma^2$ 是未知常数，是**统计推断**的对象；统计推断就是由数据推断参数性质的过程。

### 2.1.2. 正态误差模型

为了得到精确的检验和区间，我们加上一个分布假设。

**定义 2.1.2（正态误差回归模型）** **正态误差回归模型**是满足

$$
\varepsilon_1,\dots,\varepsilon_n\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)
$$
的简单线性回归模型。

不相关的正态误差是独立的（它们的联合分布是协方差矩阵为对角阵的多元正态分布），因此该模型等价于：$Y_1,\dots,Y_n$ 相互独立，且

$$
Y_i\sim\mathcal{N}(\beta_0+\beta_1X_i,\ \sigma^2),\qquad i=1,\dots,n.
$$
在 $X$ 的每个水平上，响应服从正态分布，其均值在直线 $\beta_0+\beta_1X$ 上，散布程度相同。

### 2.1.3. 模型假设与参数的含义

两个模型有下列共同特征。由于 $\mathbb{E}(\varepsilon_i)=0$，

$$
\mathbb{E}(Y_i)=\beta_0+\beta_1X_i+\mathbb{E}(\varepsilon_i)=\beta_0+\beta_1X_i,\qquad\operatorname{Var}(Y_i)=\operatorname{Var}(\varepsilon_i)=\sigma^2.
$$
$Y_i$ 的均值由 $X_i$ 的值决定；所有可能的均值都落在直线

$$
\mathbb{E}(Y)=\beta_0+\beta_1X
$$
上，这就是总体回归直线（模型的回归函数），$Y_i$ 以恒定的方差围绕这条直线波动。误差的**正态分布**是第二个模型额外的特征。构成正态误差简单线性回归模型的四个条件可以用缩写 LINE 概括。

- 线性函数（L，Linear）：在预测变量的每个值上，响应的均值是预测变量的线性函数。
- 独立（I，Independent）：误差相互独立。
- 正态分布（N，Normal）：在预测变量的每个值上，误差服从正态分布。
- 方差相等（E，Equal variances）：在预测变量的每个值上，误差的方差都是 $\sigma^2$。

总体回归直线是一条固定而未知的直线；下面计算的估计回归直线 $\hat Y=b_0+b_1X$ 则是一条随样本而变的随机直线。

斜率 $\beta_1$ 是 $X$ 每增加一个单位时 $Y$ 的概率分布的均值的变化量。截距 $\beta_0$ 是 $X=0$ 处 $Y$ 的均值，只有当模型的适用范围包含 $X=0$ 时才有这种解释。例如数据中的批量只覆盖 $20$ 到 $120$ 个单位时，$\beta_0$ 只是直线延伸到远离数据处的高度，不应加以解释。

## 2.2. 最小二乘估计

### 2.2.1. 最小二乘准则

应当怎样估计给定水平 $X=x$ 处的响应？如果忽略 $X$（或 $X$ 对 $Y$ 没有影响），自然的估计是一个与所有响应都接近的数 $c$，而使 $\sum_{i=1}^n(Y_i-c)^2$ 最小的是 $c=\bar Y$。如果考虑 $X$，我们就改为选一条直线。对每个样本点，观测到的响应是 $Y_i=\beta_0+\beta_1X_i+\varepsilon_i$，候选直线给出的预测响应是 $b_0+b_1X_i$，两者之差为 $Y_i-b_0-b_1X_i$。最小二乘准则选取使所有样本点上差的平方和最小的直线，

$$
Q(b_0,b_1)=\sum_{i=1}^n(Y_i-b_0-b_1X_i)^2,\qquad(b_0,b_1)=\arg\min_{b_0,b_1}Q(b_0,b_1).
$$

记 $\bar X=\frac1n\sum_iX_i$，$\bar Y=\frac1n\sum_iY_i$，以及

$$
S_{XX}=\sum_{i=1}^n(X_i-\bar X)^2,\qquad S_{XY}=\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y).
$$

**定理 2.2.1** 若各 $X_i$ 不全相等（$S_{XX}>0$），则最小二乘估计为

$$
b_1=\hat\beta_1=\frac{S_{XY}}{S_{XX}}=\frac{\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y)}{\sum_{i=1}^n(X_i-\bar X)^2},\qquad b_0=\hat\beta_0=\bar Y-b_1\bar X.
$$

**证明** $Q$ 是 $(b_0,b_1)$ 的凸二次函数，其极小点就是**正规方程**

$$
\frac{\partial Q}{\partial b_0}=-2\sum_{i=1}^n(Y_i-b_0-b_1X_i)=0,\qquad\frac{\partial Q}{\partial b_1}=-2\sum_{i=1}^nX_i(Y_i-b_0-b_1X_i)=0
$$
的解。由第一式得 $b_0=\bar Y-b_1\bar X$。代入第二式得 $\sum_iX_i\big[(Y_i-\bar Y)-b_1(X_i-\bar X)\big]=0$；由于 $\sum_i\bar X(Y_i-\bar Y)=\sum_i\bar X(X_i-\bar X)=0$，这就是 $S_{XY}-b_1S_{XX}=0$。Hesse 矩阵 $2\begin{bmatrix}n&\sum X_i\\\sum X_i&\sum X_i^2\end{bmatrix}$ 的行列式为 $4nS_{XX}>0$，因此该解是唯一的极小点。$\square$

这里 $b_1$ 是估计的斜率（$\beta_1$ 的估计量），$b_0$ 是估计的截距。分子分母同除以 $n-1$ 可得 $b_1=r\,s_Y/s_X$，其中 $r$ 是样本相关系数，$s_X,s_Y$ 是样本标准差：这正是 [3.3.1](/3.3.1) 中 Galton 调整后的斜率。

### 2.2.2. 拟合值与残差

**定义 2.2.1** 估计的回归函数为 $\hat Y=b_0+b_1X$。对第 $i$ 个样本点，**拟合值**为 $\hat Y_i=b_0+b_1X_i$，**残差**为

$$
e_i=Y_i-\hat Y_i=Y_i-(b_0+b_1X_i).
$$

残差不是误差项。由于 $Y_i=\beta_0+\beta_1X_i+\varepsilon_i$，

$$
e_i=(\beta_0-b_0)+(\beta_1-b_1)X_i+\varepsilon_i,
$$
因此只有当拟合直线接近真实直线时才有 $e_i\approx\varepsilon_i$：$\varepsilon_i$ 是 $Y_i$ 对未知的总体直线的竖直偏离，$e_i$ 是它对估计直线的偏离。模型恰当时，残差反映了误差项，这使残差在研究给定的回归模型是否适合手头数据时极为有用（[3.3.5](/3.3.5)）。

**命题 2.2.1** 最小二乘拟合具有以下性质。

1. $\sum_{i=1}^ne_i=0$，$\sum_{i=1}^nX_ie_i=0$。
2. $\sum_{i=1}^n\hat Y_ie_i=0$，$\sum_{i=1}^n\hat Y_i=\sum_{i=1}^nY_i$。
3. $\sum_{i=1}^ne_i^2=Q(b_0,b_1)$ 是 $Q$ 的最小值。
4. 估计回归直线经过点 $(\bar X,\bar Y)$。

**证明** 第 1 条就是代入 $(b_0,b_1)$ 后的两个正规方程。于是 $\sum_i\hat Y_ie_i=b_0\sum_ie_i+b_1\sum_iX_ie_i=0$，且 $\sum_i(Y_i-\hat Y_i)=\sum_ie_i=0$。第 3 条是 $(b_0,b_1)$ 的定义，第 4 条即 $b_0+b_1\bar X=\bar Y$。$\square$

特别地，$n$ 个残差不是自由的：它们满足两个线性约束。

### 2.2.3. 误差方差的估计

对来自一个总体的单个样本，$\sigma^2=\operatorname{Var}(Y)$ 用样本方差 $\sum_i(Y_i-\bar Y)^2/(n-1)$ 估计。在回归中这是错误的：各 $Y_i$ 来自不同的概率分布，其均值 $\beta_0+\beta_1X_i$ 依赖于水平 $X_i$，而 $\sum_i(Y_i-\bar Y)^2$ 还包含了这些均值的变化。每个偏差都必须围绕它自己的估计均值 $\hat Y_i$ 计算，这些偏差就是残差。由于 $e_i\approx\varepsilon_i$ 且 $\sigma^2=\operatorname{Var}(\varepsilon_i)=\mathbb{E}(\varepsilon_i^2)$，自然的初步想法是 $\frac1n\sum_ie_i^2$。但由命题 2.2.1，残差满足两个线性约束，只有 $n-2$ 个**自由度**，正确的除数是 $n-2$。

**定义 2.2.2** **误差平方和**与**误差均方**为

$$
\mathrm{SSE}=\sum_{i=1}^n(Y_i-\hat Y_i)^2=\sum_{i=1}^ne_i^2,\qquad\mathrm{MSE}=\frac{\mathrm{SSE}}{n-2}.
$$
$\sigma^2$ 的估计量为 $s^2=\hat\sigma^2=\mathrm{MSE}$，$s=\sqrt{\mathrm{MSE}}$（残差标准误）估计 $\sigma$。

**定理 2.2.2** 在简单线性回归模型下，$\mathbb{E}(\mathrm{SSE})=(n-2)\sigma^2$，因而 $\mathbb{E}(\mathrm{MSE})=\sigma^2$。

**证明** 写 $Y_i-\bar Y=\beta_1(X_i-\bar X)+(\varepsilon_i-\bar\varepsilon)$。由命题 2.2.1，

$$
\mathrm{SSE}=\sum_i\big[(Y_i-\bar Y)-b_1(X_i-\bar X)\big]^2=\sum_i(Y_i-\bar Y)^2-b_1^2S_{XX}.
$$
而 $\mathbb{E}\sum_i(Y_i-\bar Y)^2=\beta_1^2S_{XX}+\mathbb{E}\sum_i(\varepsilon_i-\bar\varepsilon)^2=\beta_1^2S_{XX}+(n-1)\sigma^2$，由下面的定理 2.2.3，$\mathbb{E}(b_1^2)=\operatorname{Var}(b_1)+\beta_1^2=\sigma^2/S_{XX}+\beta_1^2$。因此 $\mathbb{E}(\mathrm{SSE})=(n-1)\sigma^2-\sigma^2=(n-2)\sigma^2$。$\square$

### 2.2.4. 最小二乘估计量的性质

估计量关于响应是线性的。由于 $\sum_i(X_i-\bar X)=0$，

$$
b_1=\sum_{i=1}^nk_iY_i,\qquad k_i=\frac{X_i-\bar X}{S_{XX}},\qquad\sum_ik_i=0,\quad\sum_ik_iX_i=1,\quad\sum_ik_i^2=\frac1{S_{XX}},
$$
且 $b_0=\bar Y-b_1\bar X=\sum_i\big(\frac1n-\bar Xk_i\big)Y_i$。

**定理 2.2.3** 在简单线性回归模型下，

$$
\mathbb{E}(b_1)=\beta_1,\quad\operatorname{Var}(b_1)=\frac{\sigma^2}{S_{XX}},\qquad\mathbb{E}(b_0)=\beta_0,\quad\operatorname{Var}(b_0)=\sigma^2\left(\frac1n+\frac{\bar X^2}{S_{XX}}\right),\qquad\operatorname{Cov}(\bar Y,b_1)=0.
$$

**证明** $\mathbb{E}(b_1)=\sum_ik_i(\beta_0+\beta_1X_i)=\beta_0\sum_ik_i+\beta_1\sum_ik_iX_i=\beta_1$；由于各 $Y_i$ 不相关且方差为 $\sigma^2$，$\operatorname{Var}(b_1)=\sigma^2\sum_ik_i^2=\sigma^2/S_{XX}$。其次 $\operatorname{Cov}(\bar Y,b_1)=\sum_i\frac1nk_i\sigma^2=0$，所以 $\mathbb{E}(b_0)=\beta_0+\beta_1\bar X-\beta_1\bar X=\beta_0$，$\operatorname{Var}(b_0)=\operatorname{Var}(\bar Y)+\bar X^2\operatorname{Var}(b_1)=\sigma^2/n+\bar X^2\sigma^2/S_{XX}$。$\square$

于是 $b_0$、$b_1$ 和 $s^2$ 都是**无偏估计**。它们还是最优的：在所有关于 $Y_1,\dots,Y_n$ 线性的无偏估计量中，$b_0$ 与 $b_1$ 的方差最小（**Gauss–Markov 定理**，[3.3.3](/3.3.3)）；在正态误差下，$s^2$ 是 $\sigma^2$ 的最小方差无偏估计（[3.2.3](/3.2.3)）。

### 2.2.5. 例：比萨斜塔

比萨钟楼于 1173 年动工，到 1178 年建第二层时已开始下沉。1272 年恢复施工；为了弥补倾斜，工程师把上面几层的一侧建得更高。第七层于 1319 年完工，钟室于 1372 年加建。倾斜持续加剧并一直受到监测；斜塔于 1990 年关闭，通过从较高一侧的下方取土进行的加固工程于 2008 年完成。下面的监测数据给出了年份 $X=75,\dots,87$（即 1975–1987 年）的倾斜度 $Y$（超出 $2.9$ 米的部分，单位为十分之一毫米）。

| 年份 $X$ | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 倾斜度 $Y$ | 642 | 644 | 656 | 667 | 673 | 688 | 696 | 698 | 713 | 717 | 725 | 742 | 757 |

散点图加上作为非参数参考的局部加权平滑曲线（`lowess`）显示出几乎完全线性的增长。用 `lm` 拟合直线：

```r
towerpisa <- read.table("pisa.txt", header = TRUE)   # columns: year, lean
plot(lean ~ year, data = towerpisa, xlab = "Year", ylab = "Lean", las = 1)
lines(lowess(towerpisa$year, towerpisa$lean), col = 2)   # locally weighted smoother
bc <- lm(lean ~ year, data = towerpisa)
summary(bc)
abline(bc, col = 3, lty = 2)
```

输出包括：

| | 估计值 | 标准误 | $t$ 值 | $\mathbb{P}(>\lvert t\rvert)$ |
|---|---|---|---|---|
| 截距 | $-61.1209$ | $25.1298$ | $-2.432$ | $0.0333$ |
| year | $9.3187$ | $0.3099$ | $30.069$ | $6.5\times10^{-12}$ |

残差标准误为 $4.181$，自由度 $11$，$R^2=0.988$，$F=904.1$，自由度为 $1$ 和 $11$。估计回归直线为

$$
\hat Y=-61.12+9.3187X:
$$
倾斜度每年增加约 $9.3$ 个十分之一毫米，接近 $1$ 毫米。截距是 1900 年的倾斜度，远在数据范围之外，没有物理意义。$n=13$ 个样本点，误差自由度为 $13-2=11$，

$$
\mathrm{SSE}=\sum_ie_i^2=192.29,\qquad\mathrm{MSE}=\frac{192.29}{11}=17.48,\qquad s=\sqrt{17.48}=4.181,
$$
这正是 R 报告的残差标准误（`sum(bc$residuals^2)` 给出 SSE）。1982 年的拟合值为 $\hat Y_{82}=b_0+82\,b_1=703.0$，残差为 $e_{82}=698-703.0=-5.0$。

![比萨数据与最小二乘直线 Y_hat = -61.12 + 9.32 X；竖直线段是残差，其平方和为 SSE = 192.3，1982 年的残差为 e = -5.0](./plots/pisa-least-squares.py)

残差不仅告诉我们误差的情况，还告诉我们模型对数据拟合得如何。残差图（residual plot）以残差对预测变量（或对拟合值）作图；模型恰当时，它呈现为围绕 $0$ 的一条没有结构的水平带。残差的**正态 QQ 图**（[3.2.6](/3.2.6)）以排序后的残差对标准正态分位数 $\Phi^{-1}\big((i-0.5)/n\big)$ 作图，用于检查正态性假设。两者都是 [3.3.5](/3.3.5) 中诊断的基本工具。

```r
plot(towerpisa$year, residuals(bc), las = 1, xlab = "Year", ylab = "Residual")
abline(h = 0)
qqnorm(residuals(bc), datax = TRUE)
qqline(residuals(bc), datax = TRUE)
```

![左图：比萨拟合的残差对年份的残差图，是围绕零的一条带，没有明显趋势；右图：残差的正态 QQ 图，各点接近一条直线](./plots/pisa-residual-diagnostics.py)

残差的取值从 $-5.97$ 到 $7.40$，没有明显的模式。有两点需要注意。第一，这些观测是同一座塔的连续年份，数据构成一个时间序列，误差的独立性不能想当然，必须加以检验（[3.3.5](/3.3.5)）。第二，在观测年份之外很远处预测倾斜度（数据文件中还有年份 $116$，即 2016 年，其倾斜度缺失，被 `lm` 删去）是模型无法支持的外推，更何况加固工程改变了过程本身。

## 2.3. 极大似然估计

**似然函数**衡量在观测数据下参数的各个取值有多"可能"；给定统计模型，样本中关于参数的全部证据都包含在似然函数中。在正态误差下，$Y_i$ 的密度为

$$
f(Y_i\mid\beta_0,\beta_1,\sigma^2)=\frac1{\sqrt{2\pi\sigma^2}}\exp\left\{-\frac{(Y_i-\beta_0-\beta_1X_i)^2}{2\sigma^2}\right\},
$$
由独立性，似然函数是乘积

$$
L(\beta_0,\beta_1,\sigma^2)=\prod_{i=1}^nf(Y_i\mid\beta_0,\beta_1,\sigma^2)=(2\pi\sigma^2)^{-n/2}\exp\left\{-\frac{1}{2\sigma^2}\sum_{i=1}^n(Y_i-\beta_0-\beta_1X_i)^2\right\}.
$$

**定理 2.3.1** 在正态误差回归模型下，极大似然估计量为

$$
\hat\beta_0=b_0,\qquad\hat\beta_1=b_1,\qquad\hat\sigma^2=\frac{1}{n}\sum_{i=1}^n(Y_i-\hat Y_i)^2=\frac{\mathrm{SSE}}{n}=\frac{n-2}{n}\,\mathrm{MSE}.
$$

**证明** 最大化 $L$ 等价于最小化

$$
-\log L=\frac n2\log(2\pi\sigma^2)+\frac{Q(\beta_0,\beta_1)}{2\sigma^2}.
$$
对每个固定的 $\sigma^2$，它关于 $(\beta_0,\beta_1)$ 的最小化就是最小化 $Q$，即取最小二乘估计。在 $(b_0,b_1)$ 处令关于 $\sigma^2$ 的导数为零，$\frac{n}{2\sigma^2}-\frac{\mathrm{SSE}}{2\sigma^4}=0$，得 $\hat\sigma^2=\mathrm{SSE}/n$。$\square$

两种方法的假设不同，一般而言结果也不同。

| | 最小二乘 | 极大似然 |
|---|---|---|
| 假设 | 误差的均值与方差（定义 2.1.1） | 误差的完整分布（定义 2.1.2） |
| $\beta_0,\beta_1$ | $b_0,b_1$ | $b_0,b_1$（正态误差下） |
| $\sigma^2$ | $\mathrm{MSE}=\mathrm{SSE}/(n-2)$，无偏 | $\mathrm{SSE}/n$，偏小 |

极大似然估计依赖于分布假设，最小二乘估计则不依赖；一般而言 MLE 与 LSE 不同，这里两者对回归系数一致，只是因为正态对数似然是平方和的减函数。对其他误差分布（例如 Laplace 分布），极大似然会导出其他准则（例如最小绝对偏差）。包括矩估计在内的同样比较见 [3.2.3](/3.2.3)。

## 小结

- 简单线性回归模型：$Y_i=\beta_0+\beta_1X_i+\varepsilon_i$，$\mathbb{E}(\varepsilon_i)=0$，$\operatorname{Var}(\varepsilon_i)=\sigma^2$，误差不相关；正态误差模型再加上 $\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$，即 $Y_i\sim\mathcal{N}(\beta_0+\beta_1X_i,\sigma^2)$ 相互独立。假设：LINE（均值线性、独立、正态、方差相等）。
- $\beta_1$ 是 $X$ 每增加一个单位时平均响应的变化；只有当 $X=0$ 在模型适用范围内时，$\beta_0$ 才可解释。
- 最小二乘：$b_1=S_{XY}/S_{XX}$，$b_0=\bar Y-b_1\bar X$；残差 $e_i=Y_i-\hat Y_i$ 满足 $\sum e_i=0$、$\sum X_ie_i=0$，拟合直线经过 $(\bar X,\bar Y)$。
- 误差方差：$s^2=\mathrm{MSE}=\mathrm{SSE}/(n-2)$ 无偏；$n-2$ 反映了两个被估计的参数。
- $b_0,b_1$ 关于 $Y$ 线性且无偏，$\operatorname{Var}(b_1)=\sigma^2/S_{XX}$，$\operatorname{Var}(b_0)=\sigma^2(1/n+\bar X^2/S_{XX})$。
- 正态误差下的极大似然给出同样的 $b_0,b_1$，以及 $\hat\sigma^2=\mathrm{SSE}/n$。
- 在 R 中：`lm(y ~ x)`、`summary()`、`residuals()`；残差图和残差的正态 QQ 图是对模型的最初检查。
