---
title: 补救措施与若干专题
description: 更多的残差诊断（R 的四幅诊断图，杠杆值、离群值与强影响点，标准化残差与学生化删除残差，Cook 距离，失拟 F 检验），针对非线性、异方差与非正态误差的补救措施（非线性回归与加权回归、广义线性模型、方差稳定化变换与 Box–Cox 变换），过原点的回归、反向预测、两条回归直线以及 R² 的局限。
source_hash: 24de832cbae1
---

[3.3.5](/3.3.5) 列出了简单线性回归可能出现的问题以及如何发现它们。本章完成诊断并转向补救。第一部分细化残差分析：从 R 自带的诊断图出发，区分离群值、高杠杆点和强影响点，引入按各自标准差缩放的残差和 Cook 距离；在相同的 $X$ 值处有重复观测时，[3.3.4](/3.3.4) 的**一般线性检验**成为失拟的正式检验。第二部分讨论补救措施：非线性回归、加权、广义线性模型，以及最重要的变换，并用 Box–Cox 方法选择变换。最后一部分汇集简单回归的几个专题：过原点的回归、反向预测、两条回归直线与相关系数的关系，以及 $R^2$ 的局限。[3.3.7](/3.3.7) 的矩阵方法将把这些推广到多个预测变量。

## 6.1. 残差的进一步诊断

### 6.1.1. 再谈残差图

**残差**是模型拟合数据之后响应变量剩下的部分，它揭示数据中拟合模型未能解释的模式。我们考察残差，以发现对模型假设的严重或明显违反：

- 非线性关系；
- 方差不恒定；
- 误差非正态；
- 相依性；

以及离群值的存在和分布强烈偏斜。推荐的步骤是：

1. 画 $Y$ 对 $X$ 的图：关系是线性的吗？用 `scatter.smooth` 添加一条光滑曲线。
2. 若直线合理，拟合模型并得到残差。
3. 考察残差的分布。
4. 画残差对时间（运行）顺序、对 $X$ 或任何其他潜在解释变量、以及对拟合值 $\hat Y = b_0 + b_1 X$ 的图。
5. 在所有图中寻找非随机的模式和离群值（异常观测）。

### 6.1.2. R 自带的诊断图

拟合之后对 `lm` 对象使用 `plot`，会给出四幅诊断图；各图中旁边标了序号的点是该图中最极端的个体。

1. 残差对拟合值（Residuals vs Fitted）显示残差是否有非线性模式。残差在一条水平线两侧均匀散布、没有明显模式时是好的；光滑曲线弯曲则提示非线性。
2. 正态 QQ 图（Normal Q–Q）是标准化残差（6.1.3 节）的**正态 QQ 图**。点很好地落在虚线上时是好的。
3. 尺度–位置图（Scale–Location，又称散布–位置图）画出标准化残差绝对值的平方根 $\sqrt{\lvert r_i\rvert}$ 对拟合值的图，检查方差相等的假设（**同方差性**）。光滑曲线水平、点均匀（随机）散布时是好的；光滑曲线上升表示方差随均值增大。这里用标准化残差，是因为即使误差同方差，原始残差的方差 $\sigma^2(1 - h_{ii})$ 也不相等。
4. 残差对杠杆值（Residuals vs Leverage）帮助发现强影响个体。这里模式无关紧要；我们留意右上角或右下角、位于 Cook 距离虚线等值线以外的离群点。

```r
reg <- lm(hours ~ lotsize, data = toluca)
par(mfrow = c(2, 2))   # four plots in one window
plot(reg)
par(mfrow = c(1, 1))
```

对 Toluca 数据（[3.3.5](/3.3.5)），四幅图都没有显示严重问题；这些图给出经验界限，最常被标出的个体是第 21 个观测（批量 $30$、工时 $273$），值得再看一眼，但它不是强影响点。图 2–4 中的量下面给出定义；对多元回归它们将在 [3.3.11](/3.3.11) 中再次讨论。

### 6.1.3. 杠杆值、离群值与影响

在简单线性回归中，每个拟合值都是各响应值的线性组合。由于 $\hat Y_i = \bar Y + b_1(X_i - \bar X)$ 且 $b_1 = \sum_j (X_j - \bar X)Y_j / \sum_k (X_k - \bar X)^2$，

$$
\hat Y_i = \sum_{j=1}^n h_{ij}Y_j, \qquad h_{ij} = \frac1n + \frac{(X_i - \bar X)(X_j - \bar X)}{\sum_{k=1}^n (X_k - \bar X)^2}.
$$
$n \times n$ 矩阵 $H = [h_{ij}]$ 满足 $\hat{\boldsymbol{Y}} = H\boldsymbol{Y}$，它就是 [3.3.7](/3.3.7) 的**帽子矩阵**。

**定义 6.1.1（杠杆值）** 第 $i$ 个观测的**杠杆值**是

$$
h_{ii} = \frac{\partial \hat Y_i}{\partial Y_i},
$$
即帽子矩阵的第 $i$ 个对角元。它也称为该观测的自敏感度或自影响。

**命题 6.1.1** 在简单线性回归中，

$$
h_{ii} = \frac1n + \frac{(X_i - \bar X)^2}{\sum_{j=1}^n (X_j - \bar X)^2}.
$$

**证明** 由于 $b_0 = \bar Y - b_1\bar X$，

$$
\begin{aligned}
h_{ii} = \frac{\partial \hat Y_i}{\partial Y_i} &= \frac{\partial}{\partial Y_i}(b_0 + b_1X_i) = \frac{\partial}{\partial Y_i}\big[\bar Y + b_1(X_i - \bar X)\big] \\
&= \frac1n + \frac{\partial}{\partial Y_i}\left[(X_i - \bar X)\frac{\sum_{j=1}^n (X_j - \bar X)Y_j}{\sum_{j=1}^n (X_j - \bar X)^2}\right] = \frac1n + \frac{(X_i - \bar X)^2}{\sum_{j=1}^n (X_j - \bar X)^2}. \qquad \square
\end{aligned}
$$

杠杆值度量一个观测的预测变量值离其他观测的预测变量值有多远；它只依赖于 $X$ 的值，与响应无关。（把任何"与多数个体的趋势不合"的个体都叫作高杠杆个体是常见的错误；那描述的是离群值。）它的主要性质是：

- $h_{ii} \in [0, 1]$，这里还有 $h_{ii} \ge 1/n$，且 $\sum_i h_{ii} = 2$，即回归参数的个数（命题 7.3.1）。
- $h_{ii}$ 越小，$Y_i$ 对自身拟合值的影响越小。若 $h_{ii} = 1$，则 $\hat Y_i = Y_i$：直线必须恰好经过该点。
- $h_{ii}$ 度量 $X_i$ 到中心 $\bar X$ 的距离。有多个预测变量时，它是发现离群 $X$ 值的工具，这样的 $X$ 值可能有强影响，而此时不必有哪个单独的预测变量看起来极端（[3.3.7](/3.3.7)）。

**定义 6.1.2（离群值、高杠杆点与强影响点）** 区分两类极端值。**离群值**是响应 $Y_i$ 不服从其余数据总体趋势的观测：它的偏离大，即残差大。若一个观测的预测变量值 $X_i$ 极端，即 $h_{ii}$ 大，则称它为**高杠杆点**；这样的点稍有变化就可能改变拟合。若一个观测过度地影响回归分析的某一部分，即去掉它会显著改变估计的系数或拟合值，则称它为**强影响点**。

这三个概念是不同的。位于其余点趋势上的高杠杆点是无害的；杠杆值低的离群值主要使直线平移并放大 $s$（例 5.3.4）；杠杆值高的离群值通常是强影响点（例 5.3.5）。

**例 6.1.1** 下图每个面板中，九个点沿一条直线分布，再加入第十个点（三角形）。面板 A 中三角形的 $X = 20$，远离其他点，但位于趋势线上：杠杆值高，不是离群值，影响很小。面板 B 中它的 $X$ 普通，但响应远在直线下方：是杠杆值低的离群值，只使直线略有移动。面板 C 中它在 $X$ 方向上远离其他点，又远离趋势：它把直线拉向自己，是强影响点。

![Three regressions with one added observation (triangle), fitted with all data (solid) and without the triangle (dashed): A, a high-leverage point on the trend; B, an outlier with low leverage; C, a high-leverage outlier that changes the slope; the titles give its leverage h, studentized deleted residual t and Cook's distance D](./plots/leverage-influence.py)

面板 C 也说明了为什么原始残差不是识别离群值的好依据：强影响点把直线拉向自己，它自身的残差小于它的偏离。在一个著名的小数据集中（八个城市的酒馆数量与死亡人数）也是如此：有一个城市的酒馆数是其他城市的五倍，它远离通过其余七个点的直线，原始残差却不大，而它的学生化残差极大。办法是用每个残差自己的标准差来缩放它，并把 $Y_i$ 与一个不使用 $Y_i$ 的拟合作比较。

**定义 6.1.3（标准化残差与学生化残差）** 由于 $\operatorname{Var}(e_i) = \sigma^2(1 - h_{ii})$（[7.3.3 节](/3.3.7#sec-7.3.3)），$e_i$ 的标准差的估计为 $s\{e_i\} = \sqrt{\mathrm{MSE}(1 - h_{ii})}$。

1. 半学生化残差（semistudentized residual）为 $e_i^* = e_i / \sqrt{\mathrm{MSE}}$。
2. **标准化残差**（内学生化残差）为 $r_i = \dfrac{e_i}{s\{e_i\}} = \dfrac{e_i}{\sqrt{\mathrm{MSE}(1 - h_{ii})}}$。在模型成立时，它们几乎都应落在 $-2$ 与 $2$ 之间。
3. **删除残差**为 $d_i = Y_i - \hat Y_{i(i)}$，其中 $\hat Y_{i(i)}$ 是删去第 $i$ 个观测后拟合的模型对第 $i$ 个观测的预测响应。
4. **学生化删除残差**（外学生化残差）是标准化的删除残差，

   $$
   t_i = \frac{d_i}{s\{d_i\}} = \frac{e_i}{\sqrt{\mathrm{MSE}_{(i)}(1 - h_{ii})}},
   $$
   其中 $\mathrm{MSE}_{(i)}$ 是不含第 $i$ 个观测的拟合的均方误差。

在 R 中，`rstandard` 返回 $r_i$，`rstudent` 返回 $t_i$（R 称之为学生化残差）。学生化删除残差是识别离群值更好的准则：在误差正态的模型下 $t_i \sim t_{n-p-1}$，其中 $p$ 是回归参数的个数（这里 $p = 2$），所以每个 $t_i$ 都可以与 $t$ 分位数比较（同时筛查全部 $n$ 个个体时用 Bonferroni 调整）。计算它们不需要重新拟合 $n$ 次：如下面所证，$d_i = e_i / (1 - h_{ii})$，且 $(n - p - 1)\mathrm{MSE}_{(i)} = \mathrm{SSE} - e_i^2/(1 - h_{ii})$，所以

$$
t_i = e_i\sqrt{\frac{n - p - 1}{\mathrm{SSE}(1 - h_{ii}) - e_i^2}}.
$$

**定义 6.1.4（Cook 距离）** 第 $i$ 个观测的 **Cook 距离**度量它对全部 $n$ 个拟合值的影响：

$$
D_i = \frac{\sum_{j=1}^n \big(\hat Y_j - \hat Y_{j(i)}\big)^2}{p\,\mathrm{MSE}},
$$
其中 $\hat Y_{j(i)}$ 是去掉第 $i$ 个个体后得到的第 $j$ 个个体的拟合值，$p$ 是回归参数的个数，$\mathrm{MSE} = s^2 = \boldsymbol{e}^{\mathsf T}\boldsymbol{e}/(n - p)$。

**命题 6.1.2** 设 $X$ 是列满秩的 $n \times p$ 设计矩阵，则

$$
D_i = \frac{e_i^2}{p\,\mathrm{MSE}}\left[\frac{h_{ii}}{(1 - h_{ii})^2}\right], \qquad d_i = \frac{e_i}{1 - h_{ii}}.
$$

**证明** 记 $A = X^{\mathsf T}X$，$\boldsymbol{x}_{(i)}^{\mathsf T}$ 为 $X$ 的第 $i$ 行，于是 $h_{ii} = \boldsymbol{x}_{(i)}^{\mathsf T}A^{-1}\boldsymbol{x}_{(i)}$；记 $\boldsymbol{b}_{(i)}$ 为不含个体 $i$ 的估计。删去该个体使 $A$ 变为 $A - \boldsymbol{x}_{(i)}\boldsymbol{x}_{(i)}^{\mathsf T}$，$X^{\mathsf T}\boldsymbol{Y}$ 变为 $X^{\mathsf T}\boldsymbol{Y} - \boldsymbol{x}_{(i)}Y_i$。由 Sherman–Morrison 公式 $(A - \boldsymbol{x}\boldsymbol{x}^{\mathsf T})^{-1} = A^{-1} + A^{-1}\boldsymbol{x}\boldsymbol{x}^{\mathsf T}A^{-1}/(1 - \boldsymbol{x}^{\mathsf T}A^{-1}\boldsymbol{x})$，并注意 $\boldsymbol{x}_{(i)}^{\mathsf T}\boldsymbol{b} = \hat Y_i$，

$$
\boldsymbol{b}_{(i)} = \boldsymbol{b} - A^{-1}\boldsymbol{x}_{(i)}Y_i + A^{-1}\boldsymbol{x}_{(i)}\frac{\hat Y_i - h_{ii}Y_i}{1 - h_{ii}} = \boldsymbol{b} - A^{-1}\boldsymbol{x}_{(i)}\frac{e_i}{1 - h_{ii}}.
$$
因此 $d_i = Y_i - \boldsymbol{x}_{(i)}^{\mathsf T}\boldsymbol{b}_{(i)} = e_i + h_{ii}e_i/(1 - h_{ii}) = e_i/(1 - h_{ii})$，并且

$$
\sum_{j=1}^n\big(\hat Y_j - \hat Y_{j(i)}\big)^2 = \big\|X(\boldsymbol{b} - \boldsymbol{b}_{(i)})\big\|^2 = \frac{e_i^2}{(1 - h_{ii})^2}\,\boldsymbol{x}_{(i)}^{\mathsf T}A^{-1}X^{\mathsf T}XA^{-1}\boldsymbol{x}_{(i)} = \frac{e_i^2h_{ii}}{(1 - h_{ii})^2}.
$$
除以 $p\,\mathrm{MSE}$ 即得 $D_i$。$\square$

可见 Cook 距离结合了残差的大小和杠杆值：两者都相当大时观测才有强影响。$D_i$ 通常与 $F_{p,n-p}$ 分布比较；经验上，$D_i > 0.5$ 的个体值得注意，$D_i > 1$ 的个体很可能是强影响点。这就是 R 的残差–杠杆值图中的虚线等值线；位于其外、在右上角或右下角的点就是强影响点。

回顾这些新概念：标准化残差用 $e_i$ 自身的标准差缩放它，学生化删除残差还进一步使用不含个体 $i$ 的拟合；杠杆值 $h_{ii} = \partial\hat Y_i/\partial Y_i \in [0, 1]$ 度量 $X_i$ 到预测变量取值中心的距离；Cook 距离 $D_i$ 度量第 $i$ 个个体对全部拟合值的影响。

### 6.1.4. 失拟 F 检验

残差图提示非线性；而要正式检验线性模型是否合适（一种拟合优度检验），需要一个前提：重复观测，即在相同 $X$ 值处的多次观测。有了重复观测，误差平方和就可以分成纯误差部分（重复观测内部的变异）和失拟部分，两个假设

$$
H_0\colon \text{线性回归模型不存在失拟} \quad\text{vs}\quad H_1\colon \text{存在失拟}
$$
可以通过比较两个模型的一般线性检验来比较。

设预测变量有 $c$ 个不同的水平 $X_1, \dots, X_c$，在水平 $X_i$ 处有 $n_i$ 个观测 $Y_{i1}, \dots, Y_{in_i}$，$\sum_{i=1}^c n_i = n$。在 $H_0\colon \beta_1 = 0$ 的一般线性检验（[3.3.4](/3.3.4)）中，全模型是 $Y_i = \beta_0 + \beta_1X_i + \varepsilon_i$，简化模型是 $Y_i = \beta_0 + \varepsilon_i$。对 $H_0\colon \mu_i = \beta_0 + \beta_1X_i$ 与 $H_1\colon \mu_i \ne \beta_0 + \beta_1X_i$ 的失拟检验，全模型允许每个水平有任意的均值，线性模型则是简化模型：

$$
\text{全模型：} Y_{ij} = \mu_i + \varepsilon_{ij}, \qquad \text{简化模型：} Y_{ij} = \beta_0 + \beta_1X_i + \varepsilon_{ij}, \qquad i = 1, \dots, c,\ j = 1, \dots, n_i.
$$
全模型的最小二乘拟合是水平均值 $\bar Y_i$，每个观测与回归直线的误差偏差分解为

$$
Y_{ij} - \hat Y_{ij} = (Y_{ij} - \bar Y_i) + (\bar Y_i - \hat Y_{ij}).
$$
例如，若第三个水平上的观测 $Y_{31} = 160$，水平均值 $\bar Y_3 = 155$，拟合值 $\hat Y_{31} = 112$，则误差偏差 $48$ 等于纯误差偏差 $5$ 加失拟偏差 $43$。

**定义 6.1.5（纯误差平方和与失拟平方和）** **纯误差平方和**与**失拟平方和**为

$$
\mathrm{SSPE} = \sum_{i=1}^c\sum_{j=1}^{n_i}(Y_{ij} - \bar Y_i)^2, \qquad \mathrm{SSLF} = \sum_{i=1}^c\sum_{j=1}^{n_i}(\bar Y_i - \hat Y_{ij})^2 = \sum_{i=1}^c n_i\big(\bar Y_i - (b_0 + b_1X_i)\big)^2.
$$

**命题 6.1.3** $\mathrm{SSE} = \mathrm{SSPE} + \mathrm{SSLF}$，自由度 $n - 2 = (n - c) + (c - 2)$。

**证明** 把分解式平方后求和，交叉项为零，因为 $\bar Y_i - \hat Y_{ij}$ 不依赖于 $j$（同一水平 $i$ 上所有重复观测的拟合值 $\hat Y_{ij} = b_0 + b_1X_i$ 相同）：

$$
\sum_{i,j}(Y_{ij} - \bar Y_i)(\bar Y_i - \hat Y_{ij}) = \sum_i(\bar Y_i - \hat Y_{ij})\sum_j(Y_{ij} - \bar Y_i) = 0. \qquad \square
$$

| 变异来源 | 平方和 | 自由度 | 均方 |
|---|---|---|---|
| 回归 | $\mathrm{SSR} = \sum\sum(\hat Y_{ij} - \bar Y)^2$ | $1$ | $\mathrm{MSR} = \mathrm{SSR}/1$ |
| 误差 | $\mathrm{SSE} = \sum\sum(Y_{ij} - \hat Y_{ij})^2$ | $n - 2$ | $\mathrm{MSE} = \mathrm{SSE}/(n - 2)$ |
| $\quad$ 失拟 | $\mathrm{SSLF} = \sum\sum(\bar Y_i - \hat Y_{ij})^2$ | $c - 2$ | $\mathrm{MSLF} = \mathrm{SSLF}/(c - 2)$ |
| $\quad$ 纯误差 | $\mathrm{SSPE} = \sum\sum(Y_{ij} - \bar Y_i)^2$ | $n - c$ | $\mathrm{MSPE} = \mathrm{SSPE}/(n - c)$ |
| 总计 | $\mathrm{SSTO} = \sum\sum(Y_{ij} - \bar Y)^2$ | $n - 1$ | |

简化（线性）模型的误差平方和是 $\mathrm{SSE}$，全模型的是 $\mathrm{SSPE}$，二者之差是 $\mathrm{SSLF}$。期望均方为

$$
\mathbb{E}(\mathrm{MSPE}) = \sigma^2, \qquad \mathbb{E}(\mathrm{MSLF}) = \sigma^2 + \frac{\sum_{i=1}^c n_i\big(\mu_i - (\beta_0 + \beta_1X_i)\big)^2}{c - 2},
$$
所以无论线性模型是否成立，$\mathrm{MSPE}$ 都估计 $\sigma^2$；而 $\mathrm{MSLF}$ 只在线性模型成立时估计 $\sigma^2$，否则偏大。这就是需要重复观测的原因：它们给出一个不依赖于回归函数形式的 $\sigma^2$ 估计。

**定理 6.1.1（失拟 F 检验）** 在正态误差模型下，若水平数 $c > 2$ 且 $n > c$，则

$$
F^* = \frac{(\mathrm{SSE} - \mathrm{SSPE})/\big((n - 2) - (n - c)\big)}{\mathrm{SSPE}/(n - c)} = \frac{\mathrm{MSLF}}{\mathrm{MSPE}} \overset{H_0}{\sim} F_{c-2,n-c},
$$
当 $F^* > F_{c-2,n-c,\alpha}$ 时在水平 $\alpha$ 下拒绝 $H_0$（不存在失拟）。

这正是全模型对简化模型的一般线性检验统计量。这个检验只给出反对线性的证据：若拒绝原假设，我们断定线性回归函数不合适，但检验并不告诉我们什么样的（非线性）回归函数才合适。

**例 6.1.2（Toluca 数据）** $n = 25$ 次生产有 $c = 11$ 个不同的批量。在 R 中，把批量当作因子、不带截距即可拟合全模型，再用 `anova` 比较两个模型：

```r
reg  <- lm(hours ~ lotsize, data = toluca)                   # reduced model
Full <- lm(hours ~ 0 + as.factor(lotsize), data = toluca)    # full model: one mean per level
anova(reg, Full)
```

| 模型 | 残差自由度 | 残差平方和 | 自由度 | 平方和 | $F$ | $p$ 值 |
|---|---|---|---|---|---|---|
| hours ~ lotsize | $23$ | $54825$ | | | | |
| hours ~ 0 + as.factor(lotsize) | $14$ | $37581$ | $9$ | $17245$ | $0.7138$ | $0.6893$ |

这里 $\mathrm{SSE} = 54825$，$\mathrm{SSPE} = 37581$，$\mathrm{SSLF} = 17245$，于是 $F^* = (17245/9)/(37581/14) = 0.714$，$p = 0.689$：没有失拟的证据，线性回归函数对这些数据是合适的。

## 6.2. 补救措施

### 6.2.1. 非线性关系

许多非线性关系可以用线性模型来建模："线性"指的是参数，而不是预测变量。

$$
Y = \beta_0 + \beta_1\log X + \varepsilon \quad\text{（对数线性）}, \qquad Y = \beta_0 + \beta_1X + \beta_2X^2 + \varepsilon \quad\text{（二次）}
$$
都是线性回归模型，后者有两个解释变量 $X$ 与 $X^2$，这就引出多元线性回归（[3.3.7](/3.3.7)、[3.3.10](/3.3.10)）。有时非线性方程可以变换成线性方程：模型

$$
Y = \beta_0\exp(\beta_1X + \varepsilon)
$$
取对数后成为线性模型 $\log Y = \log\beta_0 + \beta_1X + \varepsilon$。注意这个模型中误差是以乘法形式进入的；正因为变换使误差变成加法形式，它才是合适的。

**例 6.2.1（Michaelis–Menten 模型）** 在酶动力学中，反应速度 $V$ 依赖于底物浓度 $C$：$V = \theta_1C/(\theta_2 + C)$，其中 $\theta_1$ 是最大速度，$\theta_2$ 描述随浓度增加反应接近最大速度的快慢。取倒数，得到以 $1/C$ 为解释变量的线性模型：

$$
\frac1V = \frac1{\theta_1} + \frac{\theta_2}{\theta_1}\cdot\frac1C = \beta_0 + \beta_1\frac1C.
$$
这个变换能否给出好的拟合，要像检查其他任何模型一样检查：倒数也变换了误差，低浓度处的小速度变成变异很大的大 $1/V$ 值，而 $C$ 最小（$1/C$ 最大）的观测杠杆值很高。

很多时候这样的变换并不存在。如果不想改变对误差的假设，可以改做非线性回归（nonlinear regression）分析：平均响应以非线性方式随 $X$ 变化，观测围绕这些均值的偏离与线性回归中相同，即 $Y_i = f(X_i; \boldsymbol{\theta}) + \varepsilon_i$，$f$ 关于参数 $\boldsymbol{\theta}$ 非线性。这时最小二乘估计没有闭式解，需要迭代计算（R 的 `nls`，即非线性最小二乘）。

### 6.2.2. 方差不恒定

有时需要对误差方差的变化方式建模。它可能与 $X$ 有函数关系，换言之随均值变化。这时用加权分析：加权最小二乘使 $\sum_i w_i(Y_i - b_0 - b_1X_i)^2$ 最小，权重 $w_i$ 与 $1/\sigma_i^2$ 成正比，使误差方差大的观测所占分量较小（R：`lm` 的参数 `weights`）。加权最小二乘在 [3.3.12](/3.3.12) 中展开。另一种办法是对 $Y$ 作变换以稳定方差（6.2.4 节）。

**例 6.2.2** 例 5.3.2 中误差标准差为 $10X$，所以权重 $w_i = 1/X_i^2$ 是合适的。对同一设计的模拟表明，普通最小二乘与加权最小二乘都无偏，但加权估计精确得多：截距估计的标准差从约 $75$ 降到约 $9$，斜率估计的标准差减半。

![Histograms of the OLS and WLS estimates of the intercept and slope over 4000 simulated data sets from Y = 30 + 100 X + 10 X eps, X = 1, ..., 100: both are centered at the true values 30 and 100, but the WLS estimates with weights 1/X^2 are much less variable](./plots/wls-vs-ols.py)

### 6.2.3. 非正态误差

对 $Y$ 作变换往往使我们仍能使用线性回归。否则就要用允许误差项服从其他分布的方法。广义线性模型（generalized linear model）让 $Y$ 服从**指数族**（[3.2.2](/3.2.2)）中的分布，例如

- 二项分布（是/否数据或百分比数据），
- Poisson 分布（计数数据），
- Gamma 分布（包括指数分布），
- 逆 Gauss（Wald）分布，
- 负二项分布与多项分布，

并把均值建模为 $\mathbb{E}(Y) = g(\beta_0 + \beta_1X_1 + \cdots)$，其中 $g$ 是一个单调的、通常非线性的变换；它的逆 $g^{-1}$ 把均值映到线性预测子，称为联系函数（link function）。**logistic 回归**（[3.4.12](/3.4.12)）是取 logit 联系函数的二项分布情形。在 R 中这类模型用 `glm` 拟合。

### 6.2.4. 变换

响应变量的大值往往比小值变异更大。变换通常用于：

- 稳定方差，以达到方差相等；
- 改善正态性：方差大时容易出现离群值，正态性因此常被违反，变换可以把离群值"收回来"；
- 简化模型。

有时一个变换能同时解决其中几个问题。

**定义 6.2.1（方差稳定化变换）** 设 $\mathbb{E}(Y) = \mu$，$\operatorname{Var}(Y) = h(\mu)$，即方差随均值变化。使 $\operatorname{Var}\big(f(Y)\big)$ 近似为常数的变换 $f$ 称为**方差稳定化变换**。

由 **Delta 方法**（[3.1.14](/3.1.14)），$f(Y) \approx f(\mu) + f'(\mu)(Y - \mu)$，所以

$$
\operatorname{Var}\big(f(Y)\big) \approx \big(f'(\mu)\big)^2h(\mu).
$$
要求 $\big(f'(\mu)\big)^2h(\mu)$ 为常数，得 $f'(\mu) = c/\sqrt{h(\mu)}$，即

$$
f(\mu) = \int\frac{c\,\mathrm{d}\mu}{\sqrt{h(\mu)}}.
$$
例如，若 $h(\mu) = \mu^2$（变异系数恒定），则 $f(\mu) = \log\mu$；若 $h(\mu) = \mu^{2\nu}$ 且 $\nu \ne 1$，则 $f(\mu) = c\mu^{1-\nu}$，特别地对 Poisson 型方差 $h(\mu) = \mu$ 有 $f(\mu) = \sqrt\mu$。

幂变换推广了这些例子。对严格为正的响应，**Box–Cox 变换**（[3.4.4](/3.4.4)）为 $Y^* = Y^\lambda$，或重新标度为 $Y^* = (Y^\lambda - 1)/\lambda$；后一种形式在 $\lambda \to 0$ 时的极限是自然对数。它针对非正态性和方差不恒定（方差稳定化）进行调整，$\lambda$ 选取为使数据拟合最好的值。若方差在低端小、在高端大，残差图呈扇形，可考虑下列变换族：

| $\lambda$ | $Y^*$ | 名称 |
|---|---|---|
| $1$ | $Y$ | 不变换 |
| $0.5$ | $Y^{1/2}$ | 平方根 |
| $0$ | $\log Y$ | （自然）对数 |
| $-0.5$ | $Y^{-1/2}$ | 平方根的倒数 |
| $-1$ | $Y^{-1} = 1/Y$ | 倒数 |

表中越往下的变换越强：它们对大值的压缩比对小值更多。平方根已经压缩了较大的值，使较小的值更分散；对数压缩大值更为激进。因此适当选择变换可以使右偏分布变得更对称。

在回归中，把 $\lambda$ 作为参数放进非线性模型

$$
\frac{Y_i^\lambda - 1}{\lambda} = \beta_0 + \beta_1X_i + \varepsilon_i, \qquad \varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2),
$$
用极大似然法估计它。记 $K_2 = \big(\prod_{i=1}^n Y_i\big)^{1/n}$ 为响应的几何平均，定义标准化的变换响应

$$
h(Y_i, \lambda) = \begin{cases} K_1(Y_i^\lambda - 1), & \lambda \ne 0,\\ K_2\log Y_i, & \lambda = 0,\end{cases} \qquad K_1 = \frac{1}{\lambda K_2^{\lambda-1}},
$$
并记 $\mathrm{SSE}(\lambda)$ 为 $h(Y_i, \lambda)$ 对 $X_i$ 作最小二乘回归的误差平方和。

**定理 6.2.1（Box–Cox 方法）** $\lambda$ 的极大似然估计使 $\mathrm{SSE}(\lambda)$ 最小，$\lambda$ 的剖面对数似然为

$$
\ell(\lambda) = \max_{\beta_0,\beta_1,\sigma^2}\log L(\lambda, \beta_0, \beta_1, \sigma^2) = -\frac n2\log\frac{\mathrm{SSE}(\lambda)}{n} + \text{常数}.
$$

**证明** 变换后的响应相互独立且服从 $\mathcal{N}(\beta_0 + \beta_1X_i, \sigma^2)$，所以 $Y_1, \dots, Y_n$ 的密度含有变换的 Jacobi 行列式：

$$
L(\lambda, \boldsymbol{\beta}, \sigma^2) = \frac{1}{(2\pi)^{n/2}\sigma^n}\exp\left\{-\frac{\sum_{i=1}^n\big((Y_i^\lambda - 1)/\lambda - \beta_0 - \beta_1X_i\big)^2}{2\sigma^2}\right\}J(\lambda; \boldsymbol{Y}), \qquad J(\lambda; \boldsymbol{Y}) = \prod_{i=1}^n\left\lvert\frac{\mathrm{d}}{\mathrm{d}Y_i}\frac{Y_i^\lambda - 1}{\lambda}\right\rvert = \prod_{i=1}^nY_i^{\lambda-1}
$$
（$\lambda = 0$ 时该因子为 $\prod 1/Y_i$，公式相同）。由于 $J(\lambda; \boldsymbol{Y}) = K_2^{n(\lambda-1)}$，

$$
\log L = -\frac n2\log(2\pi\sigma^2) - \frac{\sum_i\big((Y_i^\lambda - 1)/\lambda - \beta_0 - \beta_1X_i\big)^2}{2\sigma^2} + n(\lambda - 1)\log K_2 = -\frac n2\log(2\pi\tilde\sigma^2) - \frac{\sum_i\big(h(Y_i, \lambda) - \tilde\beta_0 - \tilde\beta_1X_i\big)^2}{2\tilde\sigma^2},
$$
其中 $\tilde\sigma^2 = \sigma^2/K_2^{2(\lambda-1)}$，$\tilde\beta_k = \beta_k/K_2^{\lambda-1}$，对固定的 $\lambda$ 这是一一对应的重新参数化。对固定的 $\lambda$，这正是 $h(Y_i, \lambda)$ 对 $X_i$ 回归的正态对数似然，在最小二乘估计和 $\tilde\sigma^2 = \mathrm{SSE}(\lambda)/n$ 处取最大值 $-\frac n2\log\big(2\pi\,\mathrm{SSE}(\lambda)/n\big) - \frac n2$。因此对 $\lambda$ 求最大等价于使 $\mathrm{SSE}(\lambda)$ 最小。$\square$

用几何平均标准化使不同 $\lambda$ 下的误差平方和可以比较；否则 $\mathrm{SSE}$ 会随变换后响应的单位而变。实际中在 $\lambda$ 的一组格点上计算 $\mathrm{SSE}(\lambda)$，取最小点 $\hat\lambda$（极大似然估计）。由 **Wilks 定理**（[3.2.5](/3.2.5)），$-2\log\big(L(\lambda)/L(\hat\lambda)\big) \overset{\cdot}{\sim} \chi^2_1$，由此得到近似的 $1 - \alpha$ 置信区间

$$
(\lambda_l, \lambda_u) = \left\{\lambda\colon \ell(\lambda) \ge \ell(\hat\lambda) - \frac12\chi^2_{1,\alpha}\right\}.
$$
这个区间之所以重要，是因为 $\lambda$ 是工具而不是目的：目的是得到一个结构简单、误差性质良好的回归模型。区间内的任何值都与数据相容，所以通常取一个靠近 $\hat\lambda$ 的方便、易于解释的值（如 $0$、$\pm 0.5$ 或 $\pm 1$），而不是 $\hat\lambda$ 本身，然后对选定的变换估计 $\boldsymbol{\beta}$ 和 $\sigma^2$。

**例 6.2.3（血浆水平）** 在一项对 $25$ 名 $0$ 到 $4$ 岁健康儿童（每个年龄五名）的研究中，某种多胺的血浆水平 $Y$ 随年龄 $X$ 下降，其变异在 $0$ 岁时大、随年龄变小；$Y$ 的直方图右偏。未变换的回归 $\mathrm{SSE} = 77.98$，自由度 $23$，它也就是 $\mathrm{SSE}(1)$，因为 $h(Y_i, 1) = Y_i - 1$。Box–Cox 方法给出

| $\lambda$ | $-1.0$ | $-0.9$ | $-0.8$ | $-0.7$ | $-0.6$ | $-0.5$ | $-0.4$ | $-0.3$ | $-0.2$ | $-0.1$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $\mathrm{SSE}(\lambda)$ | $33.91$ | $32.70$ | $31.76$ | $31.09$ | $30.69$ | $30.56$ | $30.72$ | $31.18$ | $31.95$ | $33.06$ |

所以 $\hat\lambda = -0.5$，$95\%$ 置信区间约为 $(-1.1, 0.1)$。根据剖面对数似然图，平方根的倒数或对数都是合理的选择。两种变换之后，各年龄的散布大致相同，变换后响应的直方图大致对称；关系仍是单调的（$Y^{-1/2}$ 递增，$\log Y$ 递减）且接近线性。

```r
library(MASS)
boxcox(plasma ~ age, data = a1, lambda = seq(-1.5, 0.5, length = 10))  # profile log-likelihood
# the same by hand: SSE(lambda) of the standardized transformed response
n <- nrow(a1)
k2 <- exp(mean(log(a1$plasma)))           # geometric mean
lambda <- seq(-1, 1, by = 0.1)
sse <- sapply(lambda, function(l) {
  h <- if (l == 0) k2 * log(a1$plasma) else (a1$plasma^l - 1) / (l * k2^(l - 1))
  deviance(lm(h ~ a1$age))                # error sum of squares
})
lambda[which.min(sse)]
a1$tplasma <- a1$plasma^(-0.5)            # apply the chosen transformation
```

![Box-Cox procedure on simulated data with five observations at each of five predictor values: the spread of Y shrinks as X grows, Y^(-1/2) has nearly constant spread, and the profile log-likelihood of lambda is maximized near -0.5 with a 95% confidence interval that excludes both 1 and 0](./plots/box-cox-profile.py)

误差方差恒定而关系弯曲时，改为变换 $X$，这不改变误差分布；误差方差也随 $X$ 变化时，变换 $Y$，必要时再结合对 $X$ 的变换。典型模式如下：

| 散点图的形态 | 变换 |
|---|---|
| 散布恒定；递增、上凸 | $X' = \log_{10}X$ 或 $X' = \sqrt X$ |
| 散布恒定；递增、下凸 | $X' = X^2$ 或 $X' = \exp(X)$ |
| 散布恒定；递减、下凸 | $X' = 1/X$ 或 $X' = \exp(-X)$ |
| 散布随均值增大 | $Y' = \sqrt Y$、$Y' = \log_{10}Y$ 或 $Y' = 1/Y$ |

## 6.3. 补充专题

### 6.3.1. 过原点的回归

**定义 6.3.1（过原点的回归）** 模型 $Y_i = \beta_1X_i + \varepsilon_i$，即假定 $\beta_0 = 0$ 的简单线性回归模型，称为**过原点的回归**。它的最小二乘估计为

$$
b_1 = \frac{\sum_{i=1}^n X_iY_i}{\sum_{i=1}^n X_i^2},
$$
且 $\mathrm{MSE} = \sum_i e_i^2/(n - 1)$。在 R 中用 `lm(Y ~ 0 + X)` 拟合。

即使理论上直线应当过原点，拟合这个模型一般也不是好主意。模型很容易设定错误，数据中的偶然变异可能被误当作结构；强迫直线经过 $(0, 0)$ 可能迫使模型在没有数据的区域以某种方式表现。通常的统计量也失去了它们的性质：

- 残差之和不再为零，$\sum_i e_i \ne 0$，因为缺少关于截距的正规方程；
- 分解 $\sum(Y_i - \bar Y)^2 = \sum(Y_i - \hat Y_i)^2 + \sum(\hat Y_i - \bar Y)^2$ 不再成立，因为交叉项 $2\sum(Y_i - \hat Y_i)(\hat Y_i - \bar Y)$ 不再为零，所以 $\mathrm{SSTO} \ne \mathrm{SSE} + \mathrm{SSR}$，自由度也不再满足 $n - 1 = (n - 2) + 1$；
- 这时软件计算的 $R^2$ 基于未中心化的平方和 $\sum Y_i^2 = \sum\hat Y_i^2 + \sum e_i^2$（自由度 $n = (n - 1) + 1$），不能与带截距模型的 $R^2$ 比较；
- $b_1$ 与 $\bar Y$ 相关，$\operatorname{Cov}(b_1, \bar Y) = \sigma^2\sum_iX_i/(n\sum_iX_i^2) \ne 0$，而在带截距的模型中 $\operatorname{Cov}(b_1, \bar Y) = 0$。

更稳妥的做法是拟合带截距的模型，再检验 $\beta_0 = 0$。

### 6.3.2. 反向预测

模型相同，$Y_i = \beta_0 + \beta_1X_i + \varepsilon_i$，拟合的回归函数为 $\hat Y = b_0 + b_1X$。现在不是在给定的 $X_h$ 处预测新的 $Y_h$，而是观测到一个新响应 $Y_{h(\mathrm{new})}$，要估计产生它的 $X_h$。

**定义 6.3.2（反向预测）** **反向预测**（校准）通过对 $X$ 解拟合方程，估计新观测 $Y_{h(\mathrm{new})}$ 对应的预测变量值 $X_h$：

$$
\hat X_h = \frac{Y_{h(\mathrm{new})} - b_0}{b_1}, \qquad b_1 \ne 0.
$$

近似的 $1 - \alpha$ 置信区间为 $\hat X_h \pm t_{n-2,\alpha/2}\,s\{\mathrm{pred}X\}$，其中

$$
s^2\{\mathrm{pred}X\} = \frac{\mathrm{MSE}}{b_1^2}\left[1 + \frac1n + \frac{(\hat X_h - \bar X)^2}{\sum_{i=1}^n(X_i - \bar X)^2}\right];
$$
当 $t_{n-2,\alpha/2}^2\,\mathrm{MSE}/\big(b_1^2\sum(X_i - \bar X)^2\big)$ 较小（比如小于 $0.1$），即斜率估计得很精确时，这一近似是适当的。典型的技术应用是新仪器的验证，以及用一组标准值评估"未知"样品。例如，把测得的半乳糖浓度 $Y$ 对已知的实际浓度 $X$ 校准，拟合直线为 $\hat Y = -0.100 + 1.017X$，则一个新的测量值由 $\hat X_h = (Y_{h(\mathrm{new})} + 0.100)/1.017$ 换算成估计的实际浓度。

反向预测与 $X$ 对 $Y$ 的回归不同。$Y$ 对 $X$ 的回归使点到直线的竖直距离最小，$X$ 对 $Y$ 的回归使水平距离最小，除非所有点恰好在一条直线上，这两条直线是不同的。

### 6.3.3. 两条回归直线

设

$$
r = \frac{\sum(X_i - \bar X)(Y_i - \bar Y)}{\sqrt{\sum(X_i - \bar X)^2}\sqrt{\sum(Y_i - \bar Y)^2}}
$$
为样本**相关系数**，$s_X$、$s_Y$ 为样本标准差。$Y$ 对 $X$ 的回归与 $X$ 对 $Y$ 的回归

$$
Y = b_0 + b_1X, \qquad X = a_0 + a_1Y, \qquad b_1 = r\frac{s_Y}{s_X}, \qquad a_1 = r\frac{s_X}{s_Y}
$$
都经过 $(\bar X, \bar Y)$，且 $a_1b_1 = r^2$。画在同一个 $(X, Y)$ 平面上，第二条直线是 $Y = -a_0/a_1 + X/a_1$。由于 $0 \le a_1b_1 \le 1$，有 $\lvert b_1\rvert \le 1/\lvert a_1\rvert$（$r \ne 0$ 时）：$Y$ 对 $X$ 的回归总是较平缓的那条，两条直线都系统地偏离数据的主轴，偏向被预测变量的均值。

**命题 6.3.1** 设 $\theta$ 是两条回归直线的夹角，$r \ne 0$，则

$$
\tan\theta = \frac{1/a_1 - b_1}{1 + b_1/a_1} = \frac{1 - a_1b_1}{a_1 + b_1} = \frac{1 - r^2}{r\left(\dfrac{s_X}{s_Y} + \dfrac{s_Y}{s_X}\right)}.
$$
特别地，若 $s_X = s_Y$ 且 $r > 0$，则 $\tan\theta = (1 - r^2)/(2r)$，等价地

$$
r = \frac{1 - \sin\theta}{\cos\theta} = \tan\Big(\frac\pi4 - \frac\theta2\Big).
$$

**证明** 第一个式子是斜率为 $1/a_1$ 与 $b_1$ 的两条直线的夹角公式；分子分母同乘 $a_1$ 得第二个式子，再由 $a_1 + b_1 = r(s_X/s_Y + s_Y/s_X)$ 与 $a_1b_1 = r^2$ 得第三个式子。当 $s_X = s_Y$ 时，对 $r > 0$ 解 $r^2 + 2r\tan\theta - 1 = 0$ 得 $r = \sec\theta - \tan\theta = (1 - \sin\theta)/\cos\theta$。$\square$

这就是 $r$ 的几何意义：两条回归直线的夹角越小，$\lvert r\rvert$ 越大。若 $s_X = s_Y$ 且 $r = 1$，两条直线重合为直线 $Y - \bar Y = X - \bar X$；若 $r = -1$，重合为斜率为 $-1$ 的直线；若 $r = 0$，两条直线垂直，分别是水平线 $Y = \bar Y$ 与竖直线 $X = \bar X$。

### 6.3.4. R² 的局限

回顾**决定系数**（[3.3.4](/3.3.4)）

$$
R^2 = \frac{\mathrm{SSR}}{\mathrm{SSTO}} = \frac{b_1^2\sum(X_i - \bar X)^2}{\sum(Y_i - \bar Y)^2}
$$
（R 中为 `summary(fit)$r.squared`）。它常被误读；一定要画出数据，因为截然不同的数据集可以有相同的拟合和相同的 $R^2$（Anscombe 四重奏，[3.4.7 的例 7.4.1](/3.4.7#ex-7.4.1)）。特别地：

- $R^2$ 不度量拟合优度。$\sigma^2$ 很大时，即使模型完全正确，$R^2$ 也可能很小；遗漏了明显的非线性项时，它仍可能很高（例 5.3.1，$R^2 = 0.87$）；而且 $R^2$ 随 $\sum(X_i - \bar X)^2$ 增大，只要改变 $X$ 的取值范围，它就可以取 $0$ 到 $1$ 之间的任何值。
- $R^2$ 不说明预测能力；$\mathrm{MSE}$ 是更好的预测误差度量。
- $R^2$ 不能用来比较响应经过变换的模型，因为总平方和随 $Y$ 的尺度而变；模型假设满足得更好时，$R^2$ 反而很可能下降。
- $R^2$ 不度量一个变量对另一个变量的解释：把 $X$ 对 $Y$ 回归，得到完全相同的 $R^2 = r^2$。

[3.3.7](/3.3.7) 的调整 $R^2$ 对这些问题都无能为力。

## 小结

| 量 | 公式 | 用途 |
|---|---|---|
| 杠杆值 | $h_{ii} = \partial\hat Y_i/\partial Y_i = \frac1n + \frac{(X_i - \bar X)^2}{\sum(X_j - \bar X)^2}$ | 离群的 $X$ 值 |
| 标准化残差 | $r_i = e_i/\sqrt{\mathrm{MSE}(1 - h_{ii})}$ | QQ 图与尺度–位置图 |
| 学生化删除残差 | $t_i = e_i/\sqrt{\mathrm{MSE}_{(i)}(1 - h_{ii})} \sim t_{n-p-1}$ | 离群的 $Y$ 值 |
| Cook 距离 | $D_i = \frac{e_i^2}{p\,\mathrm{MSE}}\frac{h_{ii}}{(1 - h_{ii})^2}$ | 对全部拟合值的影响 |
| 失拟检验 | $F^* = \mathrm{MSLF}/\mathrm{MSPE} \sim F_{c-2,n-c}$ | 线性性，需要重复观测 |

- 离群值的残差大，高杠杆点的预测变量值极端；强影响点被去掉时拟合会改变，高杠杆的离群值通常是强影响点。
- 补救措施：非线性关系用变换 $X$、增加项或非线性回归处理；方差不恒定用加权最小二乘或 $Y$ 的方差稳定化变换处理；非正态误差用变换或广义线性模型处理。
- 方差稳定化变换满足 $f'(\mu) \propto 1/\sqrt{h(\mu)}$。Box–Cox 方法通过使几何平均标准化响应的 $\mathrm{SSE}(\lambda)$ 最小来选择 $\lambda$；与 $\hat\lambda$ 本身相比，更宜取 Wilks 置信区间内一个方便的 $\lambda$。
- 过原点的回归破坏 $\sum e_i = 0$ 和方差分析分解；反向预测是对 $X$ 解拟合直线；两条回归直线满足 $a_1b_1 = r^2$，其夹角度量 $r$；$R^2$ 不是拟合、预测或解释的度量。
