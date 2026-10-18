---
title: 预测与方差分析
description: 使用拟合好的简单线性回归：平均响应的置信区间、新观测及其均值的预测区间、整条回归直线的 Working–Hotelling 置信带；方差分析（平方和的分解、自由度、期望均方、F 检验、方差分析表）、一般线性检验，以及决定系数及其与相关系数的关系。
source_hash: a05884fc4888
---

典型的回归分析包括四个步骤：建立模型、估计模型、评价模型和使用模型。前面几章建立了简单线性回归模型（[3.3.2](/3.3.2)），并对其参数作了推断（[3.3.3](/3.3.3)）。本章讨论模型的使用与评价。前半部分回答通常向一条拟合直线提出的问题：给定 $X$ 的水平时平均响应是多少，新的观测会落在哪里，整条直线确定得有多好。估计均值与预测观测的区别、单个区间与联合置信带的区别，会在整门课程中反复出现。后半部分从**方差分析**的角度看拟合：响应的总变异被分成由回归解释的部分和留给误差的部分。由此得到 $F$ 检验；得到一般线性检验，它比较完全模型与简化模型，是多元回归中主要的检验工具（[3.3.9](/3.3.9)）；还得到决定系数 $R^2$。

## 4.1. 平均响应的估计

### 4.1.1. 估计量及其分布

在预测变量的某个水平 $X=X_h$ 上（在模型的适用范围内，但不必是某个观测到的 $X_i$），平均响应为

$$
\mathbb{E}(Y_h)=\mu_h=\beta_0+\beta_1X_h,
$$
这是由 $\beta_0$ 与 $\beta_1$ 导出的参数。我们用拟合值

$$
\hat Y_h=\hat\mu_h=b_0+b_1X_h
$$
估计它。

**定理 4.1.1** 在简单线性回归模型下，$\hat Y_h$ 是 $\mathbb{E}(Y_h)$ 的无偏估计，

$$
\sigma^2(\hat Y_h)=\operatorname{Var}(\hat Y_h)=\sigma^2\left[\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right],
$$
且在 $\beta_0+\beta_1X_h$ 的所有线性无偏估计量中方差最小。在正态误差下，$\hat Y_h\sim\mathcal{N}\big(\mathbb{E}(Y_h),\sigma^2(\hat Y_h)\big)$。

**证明** 由于 $b_0=\bar Y-b_1\bar X$，

$$
\hat Y_h=\bar Y+b_1(X_h-\bar X).
$$
由 $\mathbb{E}(\bar Y)=\beta_0+\beta_1\bar X$ 与 $\mathbb{E}(b_1)=\beta_1$ 得无偏性。由于 $\operatorname{Cov}(\bar Y,b_1)=0$（[3.3.2](/3.3.2)），$\operatorname{Var}(\hat Y_h)=\sigma^2/n+(X_h-\bar X)^2\sigma^2/S_{XX}$。最小方差性与 **Gauss–Markov 定理**（[3.3.3](/3.3.3)）的证明相同，约束为 $\sum_ic_i=1$ 与 $\sum_ic_iX_i=X_h$。在正态误差下，$\hat Y_h$ 是独立正态变量的线性组合。$\square$

把 $\sigma^2$ 换成 $\mathrm{MSE}$，得到估计方差与标准误，

$$
s^2(\hat Y_h)=\mathrm{MSE}\left[\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right],\qquad\frac{\hat Y_h-\mathbb{E}(Y_h)}{s(\hat Y_h)}\sim t_{n-2},
$$
理由与 [3.3.3](/3.3.3) 中关于 $b_1$ 的论证相同。由此可以得到 $\mathbb{E}(Y_h)$ 的检验和**置信区间**；$100(1-\alpha)\%$ 置信区间为

$$
\hat Y_h\pm t_{n-2,\alpha/2}\,s(\hat Y_h).
$$

标准误随 $X_h$ 与 $\bar X$ 的距离增大而增大：平均响应在数据中心估计得最精确。原因在于斜率的不确定性。估计直线总是经过 $(\bar X,\bar Y)$，就像以中点为支点的跷跷板，离 $\bar X$ 越远，斜率的变化影响越大。在 $X_h=0$ 处，公式化为 [3.3.3](/3.3.3) 中的 $s^2(b_0)=\mathrm{MSE}\,(1/n+\bar X^2/S_{XX})$。

### 4.1.2. 例：Toluca 公司

[3.3.3](/3.3.3) 例 3.6.1 中的 Toluca 公司分批生产一种制冷设备的替换零件，批量大小不一。为了确定最优批量，公司首先需要工时 $Y$ 与批量 $X$ 之间的关系。观测到的 $n=25$ 个批次批量在 $20$ 到 $120$ 个单位之间，$\bar X=70$，$S_{XX}=19800$。最小二乘拟合为

| | 估计值 | 标准误 | $t$ 值 | $\mathbb{P}(>\lvert t\rvert)$ |
|---|---|---|---|---|
| 截距 | $62.366$ | $26.177$ | $2.382$ | $0.0259$ |
| lotsize | $3.570$ | $0.347$ | $10.290$ | $4.45\times10^{-10}$ |

残差标准误 $s=48.82$，自由度 $23$：批量每增加一个单位，约需多 $3.57$ 个工时。所有观测批量以及新批量 $65$ 和 $100$ 处平均响应的置信区间可以用 `predict` 得到：

```r
toluca <- read.table("CH01TA01.txt", col.names = c("lotsize", "hours"))
reg <- lm(hours ~ lotsize, data = toluca)
predict(reg, newdata = data.frame(lotsize = c(65, 100)),
        interval = "confidence", level = 0.95)
```

或者直接由公式计算：

```r
n <- nrow(toluca); x <- toluca$lotsize; xnew <- 100; alpha <- 0.05
s2 <- sum(residuals(reg)^2) / (n - 2)                 # MSE
ssx <- sum((x - mean(x))^2)
muh <- coef(reg)[1] + coef(reg)[2] * xnew             # fitted mean response
wid <- qt(1 - alpha / 2, df = n - 2) * sqrt((1 / n + (xnew - mean(x))^2 / ssx) * s2)
c(muh - wid, muh + wid)
```

| $X_h$ | $\hat Y_h$ | $95\%$ 置信区间 | 宽度 |
|---|---|---|---|
| $80$ | $347.98$ | $(326.54,\ 369.42)$ | $43$ |
| $30$ | $169.47$ | $(134.37,\ 204.58)$ | $70$ |
| $65$ | $294.43$ | $(273.91,\ 314.95)$ | $41$ |
| $100$ | $419.39$ | $(389.86,\ 448.91)$ | $59$ |

宽度印证了上述规律：区间在 $\bar X=70$ 附近最窄，向数据两端变宽；$X_h=30$（离 $\bar X$ 的距离为 $40$）处的区间比 $X_h=100$（距离为 $30$）处的更宽。

## 4.2. 新观测的预测

### 4.2.1. 预测区间

现在要预测 $X=X_h$ 处一个新观测的值，

$$
Y_{h(\mathrm{new})}=\beta_0+\beta_1X_h+\varepsilon_{h(\mathrm{new})},
$$
其中新的误差与用于拟合的 $n$ 个观测独立。由于 $\mathbb{E}(\varepsilon_{h(\mathrm{new})})=0$，预测值与估计的均值相同，都是 $\hat Y_h=b_0+b_1X_h$；缺失的响应也是这样填补的（例如 [3.3.2](/3.3.2) 比萨数据中倾斜度缺失的那一年）。然而区间必须更宽，因为涉及两个变异来源：

1. $Y$ 的分布所在位置的变异，即 $\hat Y_h$ 作为均值估计的不确定性；
2. $Y$ 的概率分布内部的变异，即新的误差本身。

形式上，预测误差为

$$
Y_{h(\mathrm{new})}-\hat Y_h=\big[\mathbb{E}(Y_h)-\hat Y_h\big]+\varepsilon_{h(\mathrm{new})},
$$
其均值为 $0$；由于两项独立，

$$
\sigma^2(\mathrm{pred})=\operatorname{Var}\big(Y_{h(\mathrm{new})}-\hat Y_h\big)=\sigma^2+\sigma^2(\hat Y_h)=\sigma^2\left[1+\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right].
$$
在正态误差下预测误差服从 $\mathcal{N}\big(0,\sigma^2(\mathrm{pred})\big)$，记

$$
s^2(\mathrm{pred})=\mathrm{MSE}\left[1+\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right],\qquad\frac{Y_{h(\mathrm{new})}-\hat Y_h}{s(\mathrm{pred})}\sim t_{n-2}.
$$
因此 $\mathbb{P}\big(\lvert Y_{h(\mathrm{new})}-\hat Y_h\rvert<t_{n-2,\alpha/2}\,s(\mathrm{pred})\big)=1-\alpha$。

**定义 4.2.1** 以概率 $1-\alpha$ 包含新观测 $Y_{h(\mathrm{new})}$ 的随机区间

$$
\hat Y_h\pm t_{n-2,\alpha/2}\,s(\mathrm{pred})
$$
称为 $Y_{h(\mathrm{new})}$ 的 $100(1-\alpha)\%$ **预测区间**。

预测区间是一种针对随机量的置信区间：我们在 $Y$ 的分布中选一个大部分观测都会落入的范围，并断言下一个观测会落在其中。它是否有用，照例取决于它的宽度和使用者所需的精度。与平均响应的置信区间相比，有两点本质区别。

- 根号下多出的 $1$ 不随 $n\to\infty$ 而消失：样本增大时，置信区间收缩到点 $\mathbb{E}(Y_h)$，而预测区间趋于 $\mathbb{E}(Y_h)\pm z_{\alpha/2}\sigma$。
- 预测区间强烈依赖于误差项的正态性，因为它覆盖的是单个误差 $\varepsilon_{h(\mathrm{new})}$，其中没有任何平均。平均响应的置信区间涉及的是 $\hat Y_h$，它是所有 $Y_i$ 的线性组合，即使误差不服从正态分布，由**中心极限定理**，$n$ 大时它也近似服从正态分布。

### 4.2.2. 例：Toluca 公司的预测

在 R 中，`interval = "prediction"` 把置信区间换成预测区间；在上面的公式代码中，`(1 / n + ...)` 变为 `(1 + 1 / n + ...)`。

```r
predict(reg, newdata = data.frame(lotsize = c(65, 100)),
        interval = "prediction", level = 0.95)
```

| $X_h$ | $\hat Y_h$ | $95\%$ 预测区间 | 宽度 | 置信区间的宽度 |
|---|---|---|---|---|
| $80$ | $347.98$ | $(244.73,\ 451.23)$ | $206$ | $43$ |
| $30$ | $169.47$ | $(62.55,\ 276.40)$ | $214$ | $70$ |
| $65$ | $294.43$ | $(191.37,\ 397.49)$ | $206$ | $41$ |
| $100$ | $419.39$ | $(314.16,\ 524.61)$ | $210$ | $59$ |

预测区间约为置信区间的五倍宽，而且随 $X_h$ 的变化小得多，因为起主导作用的是误差方差 $\mathrm{MSE}=2384$。

### 4.2.3. 若干个新观测的均值

考虑清华学生的身高。"大二学生的平均身高是多少？"问的是平均响应；"随机挑一名大二学生，他的身高会是多少？"问的是单个新观测。"随机挑一个 $30$ 人的大二班级，他们的平均身高会是多少？"则介于这两个极端之间：它问的是同在 $X=X_h$ 处的 $m$ 个新观测的均值 $\bar Y_{h(\mathrm{new})}$。估计量仍是 $\hat Y_h$；由于 $m$ 个独立新误差的平均的方差为 $\sigma^2/m$，$100(1-\alpha)\%$ 预测区间变为

$$
\hat Y_h\pm t_{n-2,\alpha/2}\,s(\mathrm{predmean}),\qquad s^2(\mathrm{predmean})=\mathrm{MSE}\left[\frac1m+\frac1n+\frac{(X_h-\bar X)^2}{S_{XX}}\right].
$$
$m=1$ 时就是预测区间；$m\to\infty$ 时成为平均响应的置信区间。

## 4.3. 回归直线的置信带

对每个固定的 $x$，置信区间 $\big(l(x),u(x)\big)$ 满足 $\mathbb{P}\big[l(x)<\beta_0+\beta_1x<u(x)\big]=1-\alpha$。能否由此推出 $\mathbb{P}\big[l(x)<\beta_0+\beta_1x<u(x)\text{ 对所有 }x\text{ 成立}\big]=1-\alpha$？不能：所有区间同时覆盖的概率更小，逐点的区间并不构成真正的置信带。

**定义 4.3.1** 由样本算出的下函数 $L(x)$ 与上函数 $U(x)$ 若满足

$$
\mathbb{P}\big[L(x)<\beta_0+\beta_1x<U(x)\text{ 对所有 }x\in\mathbb{R}\text{ 成立}\big]=1-\alpha,
$$
则它们确定回归直线 $y=\beta_0+\beta_1x$ 的 $100(1-\alpha)\%$ **置信带** $\{(x,y)\colon L(x)<y<U(x),\ x\in\mathbb{R}\}$。

记 $\mu_x=\beta_0+\beta_1x$，$\hat Y_x=b_0+b_1x$。我们不再用某一个 $x$ 处 $(\hat Y_x-\mu_x)/s(\hat Y_x)$ 的抽样分布，而用它在所有 $x$ 上的最大值的分布。

**定理 4.3.1（Working–Hotelling 置信带）** 在正态误差回归模型下，记

$$
W^2=2F_{2,n-2,\alpha},
$$
则置信带 $\hat Y_x\pm W\,s(\hat Y_x)$，$x\in\mathbb{R}$，的联合置信水平恰为 $1-\alpha$：

$$
\mathbb{P}\big[\lvert\hat Y_x-\mu_x\rvert\le W\,s(\hat Y_x)\text{ 对所有 }x\text{ 成立}\big]=1-\alpha.
$$

**证明** 令 $\boldsymbol{\theta}=(b_0-\beta_0,\ b_1-\beta_1)^{\mathsf T}$，$\boldsymbol{a}_x=(1,x)^{\mathsf T}$，则 $\hat Y_x-\mu_x=\boldsymbol{a}_x^{\mathsf T}\boldsymbol{\theta}$。向量 $\boldsymbol{\theta}$ 服从均值为 $\boldsymbol{0}$、协方差矩阵为 $\sigma^2M^{-1}$ 的二元正态分布，其中 $M=\begin{bmatrix}n&\sum_iX_i\\\sum_iX_i&\sum_iX_i^2\end{bmatrix}$（可以验证 $\sigma^2\boldsymbol{a}_x^{\mathsf T}M^{-1}\boldsymbol{a}_x$ 就是定理 4.1.1 中的方差 $\sigma^2(\hat Y_x)$）。对 $M^{-1/2}\boldsymbol{a}$ 与 $M^{1/2}\boldsymbol{\theta}$ 用 Cauchy–Schwarz 不等式，

$$
\frac{(\boldsymbol{a}^{\mathsf T}\boldsymbol{\theta})^2}{\boldsymbol{a}^{\mathsf T}M^{-1}\boldsymbol{a}}\le\boldsymbol{\theta}^{\mathsf T}M\boldsymbol{\theta}\quad\text{对所有 }\boldsymbol{a}\ne\boldsymbol{0},
$$
当 $\boldsymbol{a}$ 与 $M\boldsymbol{\theta}$ 成比例时取等号。左边在 $\boldsymbol{a}$ 伸缩时不变，而向量 $\boldsymbol{a}_x$（$x\in\mathbb{R}$）的方向是除 $(0,1)^{\mathsf T}$ 之外的所有方向，后者是 $x\to\pm\infty$ 时的极限；因此

$$
\sup_{x\in\mathbb{R}}\frac{(\hat Y_x-\mu_x)^2}{\sigma^2(\hat Y_x)}=\frac{\boldsymbol{\theta}^{\mathsf T}M\boldsymbol{\theta}}{\sigma^2}\sim\chi^2_2.
$$
这个变量与 $\mathrm{SSE}/\sigma^2\sim\chi^2_{n-2}$ 独立（[3.3.3](/3.3.3)），所以 $\sup_x(\hat Y_x-\mu_x)^2/s^2(\hat Y_x)=\boldsymbol{\theta}^{\mathsf T}M\boldsymbol{\theta}/\mathrm{MSE}\sim2F_{2,n-2}$，而置信带覆盖整条直线当且仅当这个上确界不超过 $W^2$。$\square$

联合陈述更强，因此 $W>t_{n-2,\alpha/2}$：置信带比单个置信区间宽。它用的 $F_{2,n-2,\alpha}$ 与 [3.3.3](/3.3.3) 中 $(\beta_0,\beta_1)$ 的椭圆置信域相同；事实上，置信带正是系数落在该椭圆内的所有直线所构成的集合。

**例 4.3.1** 对 Toluca 数据，单个 $95\%$ 区间用 $t_{23,0.025}=2.069$，$95\%$ 置信带用 $W=\sqrt{2F_{2,23,0.05}}=2.616$。在 $X_h=100$ 处，置信带为

$$
419.39\pm2.616\times14.27=(382.05,\ 456.72),
$$
比单个区间 $(389.86,\ 448.91)$ 宽。`predict` 只会算 $t$ 区间，要用它得到置信带，需找出满足 $t_{n-2,\alpha'/2}=W$ 的水平 $1-\alpha'$：

```r
W <- sqrt(2 * qf(0.95, df1 = 2, df2 = n - 2))   # 2.6162
adjalpha <- 2 * (1 - pt(W, df = n - 2))         # 0.0154
predict(reg, newdata = data.frame(lotsize = 100),
        interval = "confidence", level = 1 - adjalpha)
```

| $n$ | $\alpha$ | 自由度 | $t_{23,0.025}$（单个区间） | $W$（置信带） | 调整后的 $\alpha'$ |
|---|---|---|---|---|---|
| $25$ | $0.05$ | $(2,23)$ | $2.0687$ | $2.6162$ | $0.0154$ |

所以置信带在每一点上都是水平为 $98.46\%$ 的单个区间。

![Toluca 数据与拟合直线、平均响应的 95% 逐点置信区间、更宽的 95% Working–Hotelling 置信带，以及宽得多的 95% 预测区间；它们都在平均批量 70 处最窄](./plots/toluca-intervals.py)

置信带的用途在于：

- 评价模型的可靠性：它显示拟合直线的不确定范围，窄带意味着精度高，宽带意味着不确定性大；
- 一次给出若干个平均响应的区间估计，并保证联合水平，例如用于风险评估和决策；
- 评价拟合：若回归函数设定严重错误，穿过数据的光滑曲线（如 `lowess`）会越出置信带；而单个观测本来就不应指望落在带内，因为置信带针对的是均值，观测的散布由预测区间描述。

至此遇到的四类陈述为：

| 问题 | 区间 | 标准误 |
|---|---|---|
| 某一水平 $X_h$ 处的平均响应 $\mathbb{E}(Y_h)$ | 置信区间，$t_{n-2,\alpha/2}$ | $s(\hat Y_h)$ |
| $X_h$ 处的一个新观测 $Y_{h(\mathrm{new})}$ | 预测区间，$t_{n-2,\alpha/2}$ | $s(\mathrm{pred})$ |
| $X_h$ 处 $m$ 个新观测的均值 | 预测区间，$t_{n-2,\alpha/2}$ | $s(\mathrm{predmean})$ |
| 若干个或所有水平上的回归直线 | 置信带，$W=\sqrt{2F_{2,n-2,\alpha}}$ | $s(\hat Y_x)$ |

例如，"可支配收入为 $23\,500$ 美元的家庭平均在外出就餐上花多少钱？"要的是平均响应的置信区间；"空调设定为 $31\,^\circ\mathrm{C}$ 时，明天这个房间的温度是多少？"要的是预测区间；同时关于一整段条件下的平均响应的问题，则要用置信带。

## 4.4. 方差分析

### 4.4.1. 总平方和的分解

响应的总变异用总平方和度量；若所有观测相等，它为 $0$，否则为正。方差分析把它分解开，按来源对变异进行量化和分类。每个对均值的偏差都分成两部分：

$$
Y_i-\bar Y=(Y_i-\hat Y_i)+(\hat Y_i-\bar Y),
$$
即观测围绕拟合直线的偏差，以及拟合值围绕均值的偏差。

![Toluca 数据中两个批次的偏差分解：(a) 对均值的总偏差 Y_i - Y_bar，(b) 围绕拟合直线的偏差 Y_i - Y_hat_i，(c) 拟合值对均值的偏差 Y_hat_i - Y_bar](./plots/anova-decomposition.py)

**定义 4.4.1** **总平方和**与**回归平方和**为

$$
\mathrm{SSTO}=\sum_{i=1}^n(Y_i-\bar Y)^2,\qquad\mathrm{SSR}=\sum_{i=1}^n(\hat Y_i-\bar Y)^2;
$$
与 [3.3.2](/3.3.2) 的 $\mathrm{SSE}=\sum_i(Y_i-\hat Y_i)^2$ 一起，SSR 是由模型引起（由回归直线解释）的变异，SSE 是由误差项引起的变异。

**定理 4.4.1** $\mathrm{SSTO}=\mathrm{SSR}+\mathrm{SSE}$，且 $\mathrm{SSR}=b_1^2\sum_i(X_i-\bar X)^2$。

**证明** 把 $Y_i-\bar Y$ 的分解平方后求和，

$$
\sum_i(Y_i-\bar Y)^2=\sum_i(Y_i-\hat Y_i)^2+2\sum_i(Y_i-\hat Y_i)(\hat Y_i-\bar Y)+\sum_i(\hat Y_i-\bar Y)^2,
$$
由于 $\sum_ie_i=\sum_iX_ie_i=0$（[3.3.2](/3.3.2)），交叉项为 $\sum_ie_i(b_0+b_1X_i)-\bar Y\sum_ie_i=0$。由于 $\hat Y_i-\bar Y=b_1(X_i-\bar X)$，$\mathrm{SSR}=b_1^2S_{XX}$。$\square$

总平方和也常记为 SST，有些软件的输出就这样写。

### 4.4.2. 自由度与均方

自由度也以同样的方式分解，$n-1=1+(n-2)$：

- $\mathrm{SSTO}$ 的自由度为 $\mathrm{df}_{\mathrm{T}}=n-1$：$n$ 个偏差 $Y_i-\bar Y$ 之和为 $0$；
- $\mathrm{SSR}$ 的自由度为 $\mathrm{df}_{\mathrm{R}}=1$，因为 $\mathrm{SSR}=b_1^2S_{XX}$ 只通过一个量 $b_1$ 依赖于数据；
- $\mathrm{SSE}$ 的自由度为 $\mathrm{df}_{\mathrm{E}}=n-2$，扣除了估计的截距和斜率。

**定义 4.4.2** 平方和除以其自由度称为**均方**。回归均方与误差均方为

$$
\mathrm{MSR}=\frac{\mathrm{SSR}}{\mathrm{df}_{\mathrm{R}}}=\mathrm{SSR},\qquad\mathrm{MSE}=\frac{\mathrm{SSE}}{\mathrm{df}_{\mathrm{E}}}=\frac{\mathrm{SSE}}{n-2}.
$$

$\mathrm{MSE}=s^2$ 是 [3.3.2](/3.3.2) 中得到的 $\sigma^2=\operatorname{Var}(Y\mid X)=\operatorname{Var}(\varepsilon)$ 的估计量，而 $\mathrm{SSTO}/(n-1)$ 是各 $Y_i$ 的样本方差，它忽略了 $X$。由于 $\hat Y_i=b_0+b_1X_i$ 比 $\bar Y$ 更好地估计 $\mathbb{E}(Y_i)$，我们预期 SSE 小于 SSTO，由定理 4.4.1 确实如此：$\mathrm{SSE}=\mathrm{SSTO}-\mathrm{SSR}\le\mathrm{SSTO}$。

### 4.4.3. 期望均方

在得到观测之前，MSR 与 MSE 是随机变量。

**定理 4.4.2** 在简单线性回归模型下，

$$
\mathbb{E}(\mathrm{MSE})=\sigma^2,\qquad\mathbb{E}(\mathrm{MSR})=\sigma^2+\beta_1^2\sum_{i=1}^n(X_i-\bar X)^2.
$$

**证明** 第一式是 [3.3.2](/3.3.2) 的定理 2.2.2。对第二式，$\mathbb{E}(\mathrm{MSR})=S_{XX}\,\mathbb{E}(b_1^2)=S_{XX}\big[\operatorname{Var}(b_1)+\beta_1^2\big]=S_{XX}\big(\sigma^2/S_{XX}+\beta_1^2\big)$。$\square$

当 $H_0\colon\beta_1=0$ 为真时，$\mathbb{E}(\mathrm{MSR})=\mathbb{E}(\mathrm{MSE})=\sigma^2$，两者都是 $\sigma^2$ 的无偏估计。当 $H_1\colon\beta_1\ne0$ 成立时，$\mathbb{E}(\mathrm{MSR})>\mathbb{E}(\mathrm{MSE})$，MSR 倾向于比 MSE 大。因此比较两个均方就是检验 $\beta_1=0$。

### 4.4.4. F 检验

检验统计量为

$$
F^*=\frac{\mathrm{MSR}}{\mathrm{MSE}}.
$$
在正态误差模型与 $H_0\colon\beta_1=0$ 下，$\mathrm{SSR}/\sigma^2=\big(b_1/\sigma(b_1)\big)^2\sim\chi^2_1$ 与 $\mathrm{SSE}/\sigma^2\sim\chi^2_{n-2}$ 独立（[3.3.3](/3.3.3)），所以

$$
F^*=\frac{\chi^2_{\mathrm{df}_{\mathrm{R}}}/\mathrm{df}_{\mathrm{R}}}{\chi^2_{\mathrm{df}_{\mathrm{E}}}/\mathrm{df}_{\mathrm{E}}}\sim F_{\mathrm{df}_{\mathrm{R}},\mathrm{df}_{\mathrm{E}}}=F_{1,n-2}.
$$
$F^*$ 的大值支持 $H_1$，所以水平 $\alpha$ 的检验在 $F^*>F_{1,n-2,\alpha}$ 时拒绝 $H_0$；用 $p$ 值法等价地说，对 $F\sim F_{1,n-2}$，若 $\mathbb{P}(F>F^*)<\alpha$ 则拒绝。

**注 4.4.1** 有两个事实把 $F$ 检验与已知的结果联系起来。

1. 在 $H_1\colon\beta_1\ne0$ 下，$F^*$ 服从自由度为 $(1,n-2)$、非中心参数为 $\beta_1^2S_{XX}/\sigma^2$ 的非中心 $F$ 分布，可以像 [3.3.3](/3.3.3) 那样由它计算 $\operatorname{Power}(\beta_1)=\mathbb{P}(F^*>F_{1,n-2,\alpha})$。
2. [3.3.3](/3.3.3) 的 **t 检验**用 $T=b_1/s(b_1)$，而

$$
T^2=\frac{b_1^2}{\mathrm{MSE}/S_{XX}}=\frac{b_1^2S_{XX}}{\mathrm{MSE}}=\frac{\mathrm{MSR}}{\mathrm{MSE}}=F^*.
$$
又因为 $F_{1,n-2,\alpha}=t_{n-2,\alpha/2}^2$，在简单线性回归中双侧 $t$ 检验与 $F$ 检验等价，给出相同的 $p$ 值。关键在于 $\mathrm{df}_{\mathrm{R}}=1$；有多个预测变量时，$F$ 检验一次检验多个系数，没有对应的 $t$ 检验。

### 4.4.5. 方差分析表

计算整理成方差分析表（ANOVA table）：

| 来源 | 自由度 | 平方和 | 均方 | $F$ 值 | $\mathbb{P}(>F)$ |
|---|---|---|---|---|---|
| 回归 | $1$ | $\mathrm{SSR}=\sum_i(\hat Y_i-\bar Y)^2$ | $\mathrm{MSR}=\mathrm{SSR}/1$ | $\mathrm{MSR}/\mathrm{MSE}$ | $p$ 值 |
| 误差 | $n-2$ | $\mathrm{SSE}=\sum_i(Y_i-\hat Y_i)^2$ | $\mathrm{MSE}=\mathrm{SSE}/(n-2)$ | | |
| 总计 | $n-1$ | $\mathrm{SSTO}=\sum_i(Y_i-\bar Y)^2$ | | | |

在 R 中，`anova(lm(...))` 打印前两行，误差一行标为 `Residuals`。

**例 4.4.1** 对比萨数据（$n=13$），`anova(lm(lean ~ year, data = pisa))` 给出

| | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
|---|---|---|---|---|---|
| year | $1$ | $15804.5$ | $15804.5$ | $904.12$ | $6.5\times10^{-12}$ |
| Residuals | $11$ | $192.3$ | $17.5$ | | |

这里 $F^*=15804.5/17.48=904.1=30.069^2=T^2$，$\sqrt{17.48}=4.181$ 就是 `summary` 中的残差标准误。对 Toluca 数据（$n=25$），表中 $\mathrm{SSR}=252378$，自由度 $1$，$\mathrm{SSE}=54825$，自由度 $23$，于是 $\mathrm{MSE}=2384$，$F^*=105.88=10.290^2$，$p=4.45\times10^{-10}$，与 $t$ 检验一致。

## 4.5. 一般线性检验

方差分析还可以从另一个可以推广的角度看。检验 $H_0\colon\beta_1=0$ 对 $H_1\colon\beta_1\ne0$ 就是比较两个模型：

$$
Y_i=\beta_0+\beta_1X_i+\varepsilon_i\quad\text{（完全模型）},\qquad Y_i=\beta_0+\varepsilon_i\quad\text{（简化模型，}H_0\text{ 为真）}.
$$
额外平方和原理通过两个模型的误差平方和来比较它们：简化模型的拟合不可能更好，从完全模型换成简化模型时误差平方和的增加量，衡量了被去掉的项的贡献。

**定义 4.5.1** 给定一个**完全模型**与一个**简化模型**，后者是 $H_0$ 所规定的完全模型的特例；记 $\mathrm{SSE}(F)$（自由度 $\mathrm{df}(F)$）与 $\mathrm{SSE}(R)$（自由度 $\mathrm{df}(R)$）为它们的误差平方和。$H_0$ 的**一般线性检验**使用统计量

$$
F^*=\frac{\big[\mathrm{SSE}(R)-\mathrm{SSE}(F)\big]/\big(\mathrm{df}(R)-\mathrm{df}(F)\big)}{\mathrm{SSE}(F)/\mathrm{df}(F)},
$$
并在 $F^*$ 较大时拒绝 $H_0$。

在正态误差模型下，若 $H_0$ 成立（两个模型没有差别），$F^*\sim F_{\mathrm{df}(R)-\mathrm{df}(F),\,\mathrm{df}(F)}$；临界值法与 $p$ 值法都可以使用。一般情形的分布理论在 [3.3.9](/3.3.9) 中用矩阵方法证明。

对简单线性回归，完全模型的 $\mathrm{SSE}(F)=\mathrm{SSE}$，$\mathrm{df}(F)=n-2$。在简化模型中 $\beta_0$ 的最小二乘估计为 $\bar Y$，所以 $\mathrm{SSE}(R)=\sum_i(Y_i-\bar Y)^2=\mathrm{SSTO}$，$\mathrm{df}(R)=n-1$。因此

$$
F^*=\frac{(\mathrm{SSTO}-\mathrm{SSE})/\big((n-1)-(n-2)\big)}{\mathrm{SSE}/(n-2)}=\frac{\mathrm{SSR}}{\mathrm{MSE}}=\frac{\mathrm{MSR}}{\mathrm{MSE}},
$$
恰为方差分析的 $F$ 检验。这里一般线性检验没有带来新东西，但它适用于任意一对嵌套的线性模型，是多元回归中检验一组系数的标准方法。

## 4.6. 相关系数与决定系数

通常的（Pearson）样本**相关系数**

$$
r=\frac{\sum_i(X_i-\bar X)(Y_i-\bar Y)}{\sqrt{\sum_i(X_i-\bar X)^2\sum_i(Y_i-\bar Y)^2}}=\frac{S_{XY}}{\sqrt{S_{XX}\,\mathrm{SSTO}}}
$$
是介于 $-1$ 与 $1$ 之间的数，度量两个变量之间线性关系的强弱。方差分析给出了第二种度量。

**定义 4.6.1** **决定系数**是总变异中由模型（由预测变量）解释的比例：

$$
R^2=\frac{\mathrm{SSR}}{\mathrm{SSTO}}=1-\frac{\mathrm{SSE}}{\mathrm{SSTO}}.
$$

由定理 4.4.1，$0\le R^2\le1$；所有点都在拟合直线上时 $R^2=1$，$b_1=0$ 时 $R^2=0$。

**命题 4.6.1** 在简单线性回归中，$R^2=r^2$，且 $b_1=r\sqrt{\mathrm{SSTO}/S_{XX}}$。

**证明** $b_1=S_{XY}/S_{XX}=r\sqrt{S_{XX}\mathrm{SSTO}}/S_{XX}=r\sqrt{\mathrm{SSTO}/S_{XX}}$，因此 $\mathrm{SSR}=b_1^2S_{XX}=r^2\,\mathrm{SSTO}$。$\square$

所以 $r=\pm\sqrt{R^2}$，符号与 $b_1$ 相同。对比萨数据，$R^2=15804.5/(15804.5+192.3)=0.988$，$r=0.994$；对 Toluca 数据，$R^2=252378/(252378+54825)=0.8215$，$r=0.906$。R 把 $R^2$ 报告为 `Multiple R-squared`；旁边的调整 $R^2$ 对预测变量的个数加以惩罚，在多元回归中讨论（[3.3.8](/3.3.8)）。

$R^2$ 和 $r$ 都只度量线性关联，而且很容易被误读。

- 即使存在完美的非线性关系（关于 $\bar X$ 对称的抛物线上的点），它们也可以为 $0$。
- $R^2$ 高并不意味着线性模型恰当（弯曲的关系也可能有很高的 $R^2$），也不意味着预测足够精确：预测区间取决于 $\mathrm{MSE}$，而不是 $R^2$。
- $R^2$ 低而斜率显著，说明无论 $p$ 值多小，$X$ 都只解释了 $Y$ 的很少一部分变异；反过来，穿过一团 $R^2$ 接近 $0$ 的点云的回归直线几乎什么也没有描述，无论肉眼想在其中看出什么图案。
- $R^2$ 依赖于样本中 $X_i$ 的分散程度：同一个模型，$X_i$ 越分散，$R^2$ 越大。

最后证明 [3.3.3](/3.3.3) 中用到的零相关检验的公式。

**定理 4.6.1** 设 $(X_i,Y_i)$，$i=1,\dots,n$，是来自相关系数为 $\rho$ 的二元正态分布的随机样本。在 $H_0\colon\rho=0$ 下，

$$
t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}\sim t_{n-2}.
$$

**证明** 给定 $X_1,\dots,X_n$ 时，正态误差回归模型成立，且 $\beta_1=\rho\sigma_Y/\sigma_X$，所以 $H_0\colon\rho=0$ 就是 $H_0\colon\beta_1=0$，在其下 $T=b_1/s(b_1)\sim t_{n-2}$。而

$$
T=\frac{b_1\sqrt{S_{XX}}}{\sqrt{\mathrm{SSE}/(n-2)}}=\frac{b_1\sqrt{S_{XX}}\sqrt{n-2}}{\sqrt{\mathrm{SSTO}-\mathrm{SSR}}}=\frac{r\sqrt{\mathrm{SSTO}}\sqrt{n-2}}{\sqrt{\mathrm{SSTO}(1-r^2)}}=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}},
$$
这里用到 $b_1\sqrt{S_{XX}}=r\sqrt{\mathrm{SSTO}}$ 与 $\mathrm{SSR}=r^2\mathrm{SSTO}$（命题 4.6.1）。条件分布 $t_{n-2}$ 不依赖于各 $X_i$，因而也是无条件分布。$\square$

对简单线性回归中的 $H_0\colon\beta_1=0$，我们现在有四个等价的检验，它们给出相同的 $p$ 值：

1. 单个参数的 $t$ 检验，$T=b_1/s(b_1)$；
2. 总体相关系数的 $t$ 检验，$H_0\colon\rho=0$（对二元正态数据）；
3. 整体的方差分析 $F$ 检验，$F^*=\mathrm{MSR}/\mathrm{MSE}=T^2$；
4. 一般线性检验，这里与方差分析的 $F$ 检验一致；有多个预测变量时，它成为 [3.3.9](/3.3.9) 的偏 $F$ 检验。

## 小结

- $X_h$ 处的平均响应：$\hat Y_h=b_0+b_1X_h$，$s^2(\hat Y_h)=\mathrm{MSE}\,[1/n+(X_h-\bar X)^2/S_{XX}]$，置信区间 $\hat Y_h\pm t_{n-2,\alpha/2}s(\hat Y_h)$；在 $\bar X$ 处最精确。
- $X_h$ 处的新观测：预测区间 $\hat Y_h\pm t_{n-2,\alpha/2}s(\mathrm{pred})$，$s^2(\mathrm{pred})=\mathrm{MSE}+s^2(\hat Y_h)$；它不随 $n\to\infty$ 收缩为一点，并依赖于正态误差。对 $m$ 个新观测的均值，把 $1$ 换成 $1/m$。
- 整条直线：Working–Hotelling 置信带 $\hat Y_x\pm W s(\hat Y_x)$，$W^2=2F_{2,n-2,\alpha}$，联合水平恰为 $1-\alpha$，比逐点区间宽。
- 方差分析：$\mathrm{SSTO}=\mathrm{SSR}+\mathrm{SSE}$，自由度 $n-1=1+(n-2)$；$\mathbb{E}(\mathrm{MSE})=\sigma^2$，$\mathbb{E}(\mathrm{MSR})=\sigma^2+\beta_1^2S_{XX}$；在 $H_0\colon\beta_1=0$ 下 $F^*=\mathrm{MSR}/\mathrm{MSE}\sim F_{1,n-2}$，且 $F^*=T^2$。
- 一般线性检验：比较简化模型与完全模型的 $\mathrm{SSE}(R)$ 与 $\mathrm{SSE}(F)$；在简单回归中它就是方差分析的 $F$ 检验。
- $R^2=\mathrm{SSR}/\mathrm{SSTO}=r^2$ 度量线性拟合所解释的变异比例，仅此而已。
