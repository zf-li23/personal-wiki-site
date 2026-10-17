---
title: 协方差、相关
---

期望与方差概括单个随机变量；本章引入概括两个随机变量之间关系的数字特征。在资产组合理论中，Markowitz（1990 年诺贝尔经济学奖）用组合的期望衡量收益、用组合的方差衡量风险，而组合的方差不仅取决于各资产的方差，还取决于资产之间的协方差；在脑科学中，两个脑区信号之间的"功能连接"常用相关系数度量。本章先定义协方差并给出它的性质，再把它标准化为相关系数，讨论不相关与独立的关系、相关系数的几何意义（夹角余弦）与最佳线性预测，最后把这些概念推广到随机向量，定义协方差矩阵。本章用到 [3.1.8](/3.1.8) 的期望与方差、[3.1.9](/3.1.9) 的条件期望；协方差矩阵是多元正态分布（[3.1.15](/3.1.15)）、线性回归（[3.3](/3.3)）与多元统计分析的基础。

## 10.1. 协方差

### 10.1.1. 定义

如何用一个数概括 $X$ 与 $Y$ 的协同变化？先平移去掉位置信息，考察 $X - \mathbb{E}X$ 与 $Y - \mathbb{E}Y$。以点 $(\mathbb{E}X, \mathbb{E}Y)$ 为原点把平面分成四个象限：若 $(X, Y)$ 多落在第一、三象限（两者同时偏大或同时偏小），乘积 $(X - \mathbb{E}X)(Y - \mathbb{E}Y)$ 多为正；若多落在第二、四象限，乘积多为负。对乘积求平均，就得到协方差。

**定义 10.1.1（协方差）** 设 $\mathbb{E}X$ 与 $\mathbb{E}Y$ 存在，当 $\mathbb{E}\lvert(X - \mathbb{E}X)(Y - \mathbb{E}Y)\rvert < \infty$ 时，称

$$
\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}X)(Y - \mathbb{E}Y)]
$$
为随机变量 $X, Y$ 的**协方差**。

协方差为正、为零、为负时，分别称 $X, Y$ 正相关、不相关、负相关。由 Cauchy–Schwarz 不等式，$X, Y$ 的方差有限时协方差存在。

**性质 10.1.1** 设所涉及的协方差存在，则

1. $\operatorname{Cov}(X, X) = \operatorname{Var}(X)$；
2. $\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)$；
3. $\operatorname{Cov}(X, Y) = \mathbb{E}(XY) - \mathbb{E}X\,\mathbb{E}Y$（常用计算公式）；
4. 若 $c$ 是常数，则 $\operatorname{Cov}(X, c) = 0$；
5. （双线性）$\operatorname{Cov}(cX, Y) = c\operatorname{Cov}(X, Y)$，$\operatorname{Cov}(X, Y + Z) = \operatorname{Cov}(X, Y) + \operatorname{Cov}(X, Z)$；
6. $\operatorname{Var}(X_1 + X_2) = \operatorname{Var}(X_1) + \operatorname{Var}(X_2) + 2\operatorname{Cov}(X_1, X_2)$。

这些性质都基于期望的线性性。以第 6 条为例，

$$
\operatorname{Var}(X_1 + X_2) = \mathbb{E}[(X_1 - \mathbb{E}X_1) + (X_2 - \mathbb{E}X_2)]^2 = \operatorname{Var}(X_1) + \operatorname{Var}(X_2) + 2\mathbb{E}[(X_1 - \mathbb{E}X_1)(X_2 - \mathbb{E}X_2)].
$$
一般地，由双线性，

$$
\operatorname{Var}\Big(\sum_{i=1}^n X_i\Big) = \sum_{i=1}^n\operatorname{Var}(X_i) + 2\sum_{1 \le i < j \le n}\operatorname{Cov}(X_i, X_j), \qquad \operatorname{Cov}\Big(\sum_i a_iX_i, \sum_j b_jY_j\Big) = \sum_{i,j}a_ib_j\operatorname{Cov}(X_i, Y_j).
$$
所以两两不相关的随机变量之和的方差等于方差之和（定理 8.3.1 的第 4 条只需要这一条件）。资产组合 $wX + (1 - w)Y$ 的风险 $w^2\operatorname{Var}(X) + (1 - w)^2\operatorname{Var}(Y) + 2w(1 - w)\operatorname{Cov}(X, Y)$ 随协方差减小而减小：组合负相关的资产可以分散风险。

![两种方差都为 1 的资产按比例 w 组合时，组合的方差随 w 与相关系数 rho 的变化](./plots/portfolio-variance.py)

### 10.1.2. 例子

**例 10.1.1** 设 $(X_1, \dots, X_k) \sim \mathrm{Mult}(n, \boldsymbol{p})$，$\boldsymbol{p} = (p_1, \dots, p_k)^{\mathsf T}$，$\sum_{i=1}^k p_i = 1$，求 $\operatorname{Cov}(X_i, X_j)$。

**解** $i = j$ 时，由性质 6.2.1，$X_i \sim \mathrm{Bin}(n, p_i)$，$\operatorname{Cov}(X_i, X_i) = \operatorname{Var}(X_i) = np_i(1 - p_i)$。

$i \ne j$ 时，用示性函数分解：记 $I_t$、$J_t$ 分别为第 $t$ 次试验中 $A_i$、$A_j$ 发生的示性函数，则 $X_i = \sum_{t=1}^n I_t$，$X_j = \sum_{s=1}^n J_s$。不同次试验独立，$\operatorname{Cov}(I_t, J_s) = 0$（$t \ne s$）；同一次试验中 $A_i, A_j$ 互斥，$I_tJ_t = 0$，$\operatorname{Cov}(I_t, J_t) = 0 - p_ip_j$。由双线性，

$$
\operatorname{Cov}(X_i, X_j) = \sum_{t=1}^n\operatorname{Cov}(I_t, J_t) = -np_ip_j.
$$
协方差为负符合直观：$n$ 次试验的总数固定，一类结果多了，另一类就倾向于少。

**例 10.1.2** 独立地掷 $n$ 颗均匀的骰子，$X$、$Y$ 分别是 1 点、2 点出现的颗数。由例 10.1.1（$p_1 = p_2 = \frac{1}{6}$），$\operatorname{Var}(X) = \operatorname{Var}(Y) = \frac{5n}{36}$，$\operatorname{Cov}(X, Y) = -\frac{n}{36}$。直接计算时注意：同一颗骰子的两个示性函数 $X_k$ 与 $Y_k$ 不独立，$X_kY_k = 0$，$\operatorname{Cov}(X_k, Y_k) = -\frac{1}{36} \ne 0$；不同骰子的示性函数才独立。

**例 10.1.3（超几何分布的方差）** 例 8.2.5 中 $X = \sum_{k=1}^n X_k \sim \mathrm{H}(n, M, N)$，$X_k \sim \mathrm{Ber}(M/N)$。$j \ne k$ 时 $\mathbb{P}(X_j = X_k = 1) = \frac{M(M - 1)}{N(N - 1)}$，

$$
\operatorname{Cov}(X_j, X_k) = \frac{M(M - 1)}{N(N - 1)} - \frac{M^2}{N^2} = -\frac{M(N - M)}{N^2(N - 1)},
$$
所以

$$
\operatorname{Var}(X) = n\frac{M}{N}\Big(1 - \frac{M}{N}\Big) - n(n - 1)\frac{M(N - M)}{N^2(N - 1)} = n\frac{M}{N}\Big(1 - \frac{M}{N}\Big)\frac{N - n}{N - 1}.
$$
因子 $\frac{N - n}{N - 1}$ 是无放回抽样相对于有放回抽样（二项分布）的方差修正。

## 10.2. 相关系数

协方差依赖于量纲：若 $\operatorname{Var}(Z) = \operatorname{Var}(W) = 1$，$\operatorname{Cov}(Z, W) = 0.42$，则 $X = 10Z$、$Y = 10W$ 的协方差是 $42$，但 $X, Y$ 之间关系的紧密程度并没有变。为了得到可比较的度量，对 $X, Y$ 先标准化再求协方差：

$$
\operatorname{Cov}\Big(\frac{X - \mathbb{E}X}{\sqrt{\operatorname{Var}(X)}}, \frac{Y - \mathbb{E}Y}{\sqrt{\operatorname{Var}(Y)}}\Big) = \frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X)}\sqrt{\operatorname{Var}(Y)}}.
$$

**定义 10.2.1（相关系数）** 当 $0 < \operatorname{Var}(X)\operatorname{Var}(Y) < \infty$ 时，称

$$
\operatorname{Corr}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X)}\sqrt{\operatorname{Var}(Y)}}
$$
为 $X, Y$ 的**相关系数**（Pearson 相关系数），也记作 $\rho_{XY}$。

由定义，$\operatorname{Corr}(aX + b, cY + d) = \operatorname{sgn}(ac)\operatorname{Corr}(X, Y)$（$ac \ne 0$）：相关系数不受平移与正的伸缩影响，因此具有可比性。上面的例子中 $\operatorname{Corr}(X, Y) = \operatorname{Corr}(Z, W) = 0.42$。

**例 10.2.1** 设 $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$，则 $\operatorname{Corr}(X, Y) = \rho$。

**解** 由于相关系数不受平移与伸缩影响，不妨设 $(X, Y) \sim \mathcal{N}(0, 0, 1, 1, \rho)$，此时 $\mathbb{E}X = \mathbb{E}Y = 0$，$\operatorname{Var}(X) = \operatorname{Var}(Y) = 1$。由例 6.5.2，$\mathbb{E}(X \mid Y) = \rho Y$，于是由重期望公式与定理 9.3.2 的性质 3，

$$
\operatorname{Cov}(X, Y) = \mathbb{E}(XY) = \mathbb{E}[Y\,\mathbb{E}(X \mid Y)] = \rho\,\mathbb{E}Y^2 = \rho,
$$
故 $\operatorname{Corr}(X, Y) = \rho$。（也可以直接计算积分 $\int\!\!\int xy f(x, y)\,\mathrm{d}x\,\mathrm{d}y$。）这解释了二元正态分布的第五个参数为什么记作 $\rho$。

**定理 10.2.1** 设 $\operatorname{Corr}(X, Y)$ 是 $X, Y$ 的相关系数，则

1. $\lvert\operatorname{Corr}(X, Y)\rvert \le 1$；
2. $\lvert\operatorname{Corr}(X, Y)\rvert = 1$ 当且仅当存在常数 $a, b, c$（$a, b$ 不全为零），使得 $aX + bY = c$ a.s.，此时称 $X, Y$ 线性相关。

**证明** 记 $\tilde X = X - \mathbb{E}X$，$\tilde Y = Y - \mathbb{E}Y$。由 Cauchy–Schwarz 不等式（定理 8.5.2），

$$
\lvert\operatorname{Cov}(X, Y)\rvert = \lvert\mathbb{E}(\tilde X\tilde Y)\rvert \le \sqrt{\mathbb{E}\tilde X^2\,\mathbb{E}\tilde Y^2} = \sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)},
$$
即 1。等号成立当且仅当存在不全为零的 $a, b$ 使 $a\tilde X + b\tilde Y = 0$ a.s.，即 $aX + bY = a\mathbb{E}X + b\mathbb{E}Y =: c$ a.s. $\square$

$\operatorname{Corr}(X, Y) = 1$ 时 $Y$ 是 $X$ 的增函数 $Y = \alpha + \beta X$（$\beta > 0$），$= -1$ 时 $\beta < 0$。$\lvert\operatorname{Corr}\rvert$ 越接近 1，散点越集中在一条直线附近。

![不同相关系数下的散点图；最后两幅中 X, Y 有明确的非线性关系，相关系数却近似为 0](./plots/correlation-scatter.py)

## 10.3. 不相关与独立

**定理 10.3.1** 设 $X, Y$ 相互独立且方差有限，则 $X, Y$ 不相关，即 $\operatorname{Cov}(X, Y) = 0$。

**证明** 由独立性与定理 8.2.2 的第 5 条，$\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}X)(Y - \mathbb{E}Y)] = \mathbb{E}(X - \mathbb{E}X)\cdot\mathbb{E}(Y - \mathbb{E}Y) = 0$。 $\square$

反之不成立：不相关不一定独立。

**例 10.3.1** 设 $(X, Y)$ 在单位圆 $D = \{x^2 + y^2 \le 1\}$ 内均匀分布，则 $X, Y$ 不相关，也不独立。

**解** 由例 8.2.3，$\mathbb{E}X = \mathbb{E}Y = 0$。被积函数 $xy$ 关于 $x$ 是奇函数，

$$
\operatorname{Cov}(X, Y) = \int_{\mathbb{R}^2} xy\cdot\frac{1}{\pi}\boldsymbol{1}_D(x, y)\,\mathrm{d}x\,\mathrm{d}y = \frac{1}{\pi}\int_{-1}^1 y\Big(\int_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}} x\,\mathrm{d}x\Big)\mathrm{d}y = 0.
$$
但由注 6.3.1，$X, Y$ 不独立：例如 $\mathbb{P}(X > 0.8, Y > 0.8) = 0 \ne \mathbb{P}(X > 0.8)\mathbb{P}(Y > 0.8)$。

又如 $X \sim \mathcal{N}(0, 1)$，$Y = X^2$：$\operatorname{Cov}(X, Y) = \mathbb{E}X^3 = 0$，而 $Y$ 完全由 $X$ 决定。Pearson 相关系数只度量线性关联；非线性关联需要用其他工具度量，如 Spearman 秩相关系数、互信息等。

正态分布是一个重要的例外。

**例 10.3.2** 设 $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$，则 $X, Y$ 独立当且仅当 $X, Y$ 不相关。这是因为由例 10.2.1，不相关即 $\rho = 0$，而由定理 6.4.1，$\rho = 0$ 当且仅当独立。注意前提是 $(X, Y)$ 服从二元正态分布，仅仅 $X$、$Y$ 各自服从正态分布是不够的。

**例 10.3.3** 设 $(X, Y)$ 服从二元正态分布，且 $\mathbb{E}(X \mid Y) = \mu$ 是常数，则 $X, Y$ 独立。

**证明** 由重期望公式，$\mathbb{E}X = \mathbb{E}[\mathbb{E}(X \mid Y)] = \mu$。由定理 9.3.2 的性质 3，

$$
\mathbb{E}[(X - \mu)Y] = \mathbb{E}\big[Y\,\mathbb{E}(X - \mu \mid Y)\big] = \mathbb{E}[Y(\mu - \mu)] = 0,
$$
所以 $\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mu)Y] - \mathbb{E}(X - \mu)\,\mathbb{E}Y = 0$，$X, Y$ 不相关，再由例 10.3.2 得独立。 $\square$

证明的前半部分对任何方差有限的 $(X, Y)$ 都成立：$\mathbb{E}(X \mid Y)$ 为常数蕴含不相关。但一般分布下这不蕴含独立：例 10.3.1 中由对称性 $\mathbb{E}(X \mid Y) = 0$，$X, Y$ 却不独立。三个条件的强弱关系是

$$
X, Y \text{ 独立} \ \Longrightarrow\ \mathbb{E}(X \mid Y) = \mathbb{E}X \ \Longrightarrow\ X, Y \text{ 不相关},
$$
反方向一般都不成立，在二元正态分布下三者等价。

## 10.4. 相关系数的几何意义与最佳线性预测

### 10.4.1. 夹角余弦

把中心化的随机变量 $\tilde X = X - \mathbb{E}X$、$\tilde Y = Y - \mathbb{E}Y$ 看作向量，以 $\langle\tilde X, \tilde Y\rangle = \mathbb{E}(\tilde X\tilde Y)$ 为**内积**，则长度 $\|\tilde X\| = \sqrt{\mathbb{E}\tilde X^2}$ 就是标准差，而

$$
\operatorname{Corr}(X, Y) = \frac{\langle\tilde X, \tilde Y\rangle}{\|\tilde X\|\,\|\tilde Y\|} = \cos\varphi,
$$
其中 $\varphi$ 是 $\tilde X$ 与 $\tilde Y$ 的夹角。于是 $\lvert\operatorname{Corr}\rvert \le 1$ 就是 $\lvert\cos\varphi\rvert \le 1$，$\lvert\operatorname{Corr}\rvert = 1$ 就是两个向量共线，不相关就是正交。

### 10.4.2. 最佳线性预测

[3.1.8](/3.1.8) 与 [3.1.9](/3.1.9) 分别给出了均方误差意义下的最佳常数预测 $\mathbb{E}Y$ 与最佳预测 $\mathbb{E}(Y \mid X)$。如果只允许用 $X$ 的线性函数预测 $Y$，最佳的系数由协方差与相关系数决定。

**定理 10.4.1（最佳线性预测）** 设 $X, Y$ 的方差有限且 $\operatorname{Var}(X) > 0$，则 $\mathbb{E}[Y - (a + bX)]^2$ 在

$$
b^* = \frac{\operatorname{Cov}(X, Y)}{\operatorname{Var}(X)} = \rho_{XY}\frac{\sigma_Y}{\sigma_X}, \qquad a^* = \mathbb{E}Y - b^*\mathbb{E}X
$$
处取最小值，最小值为 $\operatorname{Var}(Y)(1 - \rho_{XY}^2)$。称 $\hat Y = a^* + b^*X = \mathbb{E}Y + \rho_{XY}\frac{\sigma_Y}{\sigma_X}(X - \mathbb{E}X)$ 为用 $X$ 预测 $Y$ 的最佳线性预测。

**证明** 记 $\tilde X, \tilde Y$ 如上，$c = a + b\mathbb{E}X - \mathbb{E}Y$，则 $Y - (a + bX) = (\tilde Y - b\tilde X) - c$，由定理 8.2.4，

$$
\mathbb{E}[Y - (a + bX)]^2 = \mathbb{E}(\tilde Y - b\tilde X)^2 + c^2 = \operatorname{Var}(Y) - 2b\operatorname{Cov}(X, Y) + b^2\operatorname{Var}(X) + c^2.
$$
对 $b$ 配方，最小值在 $b = b^*$、$c = 0$ 处取得，最小值为 $\operatorname{Var}(Y) - \frac{\operatorname{Cov}(X, Y)^2}{\operatorname{Var}(X)} = \operatorname{Var}(Y)(1 - \rho_{XY}^2)$。 $\square$

几何上，$b^*\tilde X$ 是 $\tilde Y$ 在 $\tilde X$ 方向上的投影，残差 $\tilde Y - b^*\tilde X$ 与 $\tilde X$ 正交。$\rho_{XY}^2$ 是线性预测所能解释的方差比例：$\rho = 0$ 时线性预测完全无用，$\lvert\rho\rvert = 1$ 时预测没有误差。三种预测的比较如下：

| 预测的类型 | 最佳预测 | 解读 |
|---|---|---|
| 常数 $c$ | $\mathbb{E}Y = \operatorname*{argmin}_c\mathbb{E}(Y - c)^2$ | 质心 |
| 线性函数 $a + bX$ | $\mathbb{E}Y + \rho_{XY}\frac{\sigma_Y}{\sigma_X}(X - \mathbb{E}X)$ | 投影到 $\{1, X\}$ 张成的空间 |
| 任意函数 $g(X)$ | $\mathbb{E}(Y \mid X) = \operatorname*{argmin}_g\mathbb{E}[Y - g(X)]^2$ | 投影到 $X$ 的函数空间 |

由例 9.3.7，二元正态分布下后两者一致；一般分布下，最佳线性预测的均方误差不小于 $\mathbb{E}(Y \mid X)$ 的均方误差。这是统计中线性回归的总体版本。

### 10.4.3. 相关与因果

相关不意味着因果。公鸡打鸣与日出高度相关，但公鸡不打鸣，太阳照常升起；两个脑区的信号相关，可能是第三个脑区同时影响二者，而不是一方影响另一方。相关系数是两个变量协同变化的总结，解读时要注意它的边界：它只反映线性关联，也不说明作用的方向。另一方面，相关结构在一定的模型假设下可以帮助我们发现因果关系，例如在多元正态分布的假设下，由协方差矩阵推断变量之间的有向依赖关系（基因调控网络的学习即是一例）。系统的理论属于因果推断（[3.7](/3.7)）。

## 10.5. 随机向量的期望与协方差矩阵

### 10.5.1. 随机向量与随机矩阵的期望

下面把向量写成列向量。设 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ 是随机向量，如果每个 $\mu_i = \mathbb{E}X_i$ 都存在，就称 $\boldsymbol{X}$ 的数学期望存在，并定义

$$
\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X} = (\mathbb{E}X_1, \dots, \mathbb{E}X_n)^{\mathsf T}.
$$
类似地，元素为随机变量的矩阵 $Y = (Y_{ij})_{m \times n}$（随机矩阵）的期望定义为逐个元素取期望：$\mathbb{E}Y = (\mathbb{E}Y_{ij})_{m \times n}$。

由期望的线性性容易证明：对常数向量 $\boldsymbol{a} \in \mathbb{R}^n$，常数矩阵 $A_{k \times m}$、$B_{n \times j}$，

$$
\mathbb{E}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{a}^{\mathsf T}\mathbb{E}\boldsymbol{X}, \qquad \mathbb{E}(Y^{\mathsf T}) = (\mathbb{E}Y)^{\mathsf T}, \qquad \mathbb{E}(AYB) = A(\mathbb{E}Y)B.
$$

### 10.5.2. 协方差矩阵

**定义 10.5.1（协方差矩阵）** 设随机向量 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ 的每个分量的方差有限，$\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X}$，称

$$
\Sigma = \operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}] = (\sigma_{ij})_{n \times n}, \qquad \sigma_{ij} = \operatorname{Cov}(X_i, X_j)
$$
为 $\boldsymbol{X}$ 的**协方差矩阵**。

协方差矩阵是对称矩阵，对角元是各分量的方差。如果 $\det\Sigma = 0$，称 $\Sigma$ 是退化的。例如二元正态分布 $\mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$ 的协方差矩阵正是 §6.4 中的 $\Sigma$，均值向量是 $\boldsymbol{\mu}$：二元正态密度完全由均值向量与协方差矩阵决定。

**定理 10.5.1** 设 $\Sigma$ 是 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ 的协方差矩阵，则

1. $\Sigma$ 是**半正定矩阵**；
2. $\Sigma$ 退化的充分必要条件是存在不全为零的常数 $a_1, \dots, a_n$，使得 $\sum_{i=1}^n a_i(X_i - \mathbb{E}X_i) = 0$ a.s.

**证明** 对任意 $\boldsymbol{a} = (a_1, \dots, a_n)^{\mathsf T} \in \mathbb{R}^n$，

$$
\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} = \sum_{i=1}^n\sum_{j=1}^n a_ia_j\,\mathbb{E}[(X_i - \mathbb{E}X_i)(X_j - \mathbb{E}X_j)] = \mathbb{E}\Big[\sum_{i=1}^n a_i(X_i - \mathbb{E}X_i)\Big]^2 = \operatorname{Var}\Big(\sum_{i=1}^n a_iX_i\Big) \ge 0,
$$
所以 $\Sigma$ 半正定。半正定矩阵退化当且仅当存在非零向量 $\boldsymbol{a}$ 使 $\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} = 0$，即 $\operatorname{Var}\big(\sum_i a_iX_i\big) = 0$，由定理 8.3.1 的第 3 条，这等价于 $\sum_i a_i(X_i - \mathbb{E}X_i) = 0$ a.s. $\square$

所以协方差矩阵退化，意味着随机向量几乎必然落在一个低维的超平面上，某个分量可以由其他分量线性表示。证明中的等式也给出了线性变换下协方差矩阵的变换规律：对常数矩阵 $A_{k \times n}$ 与常数向量 $\boldsymbol{b}$，

$$
\operatorname{Cov}(A\boldsymbol{X} + \boldsymbol{b}) = \mathbb{E}[A(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}A^{\mathsf T}] = A\Sigma A^{\mathsf T}.
$$
这一公式在多元正态分布（[3.1.15](/3.1.15)）中反复使用。

**例 10.5.1** 设 $\boldsymbol{X} = (X_1, \dots, X_k)^{\mathsf T} \sim \mathrm{Mult}(n, \boldsymbol{p})$。由例 10.1.1，

$$
\Sigma = n\big(\operatorname{diag}(p_1, \dots, p_k) - \boldsymbol{p}\boldsymbol{p}^{\mathsf T}\big).
$$
由于 $X_1 + \cdots + X_k = n$ 是常数，取 $\boldsymbol{a} = \boldsymbol{1}$ 得 $\sum_i(X_i - \mathbb{E}X_i) = 0$，由定理 10.5.1，$\Sigma$ 退化。直接验证：$\Sigma\boldsymbol{1} = n(\boldsymbol{p} - \boldsymbol{p}(\boldsymbol{p}^{\mathsf T}\boldsymbol{1})) = \boldsymbol{0}$。

## 小结

- 协方差 $\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}X)(Y - \mathbb{E}Y)] = \mathbb{E}(XY) - \mathbb{E}X\,\mathbb{E}Y$，双线性、对称；$\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X, Y)$。
- 相关系数 $\operatorname{Corr}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sigma_X\sigma_Y} \in [-1, 1]$，不受平移与伸缩影响；$\lvert\operatorname{Corr}\rvert = 1$ 当且仅当几乎必然线性相关；几何上是中心化变量的夹角余弦。
- 独立 $\Rightarrow$ $\mathbb{E}(X \mid Y)$ 为常数 $\Rightarrow$ 不相关，反之一般不成立；二元正态分布下三者等价。
- 最佳线性预测 $\mathbb{E}Y + \rho\frac{\sigma_Y}{\sigma_X}(X - \mathbb{E}X)$，均方误差 $\sigma_Y^2(1 - \rho^2)$。
- 协方差矩阵 $\Sigma = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}]$ 对称半正定，$\operatorname{Cov}(A\boldsymbol{X} + \boldsymbol{b}) = A\Sigma A^{\mathsf T}$；退化当且仅当分量之间几乎必然有线性关系。
- 技巧：用示性函数把计数写成和，再用双线性计算协方差（多项分布、超几何分布）；利用对称性；高维不清楚时，先用二维情形帮助理解。
