---
title: 补救措施与单因子方差分析
description: 应对误差方差不等的加权最小二乘与广义最小二乘；应对多重共线性的岭回归、Lasso 与弹性网络；稳健回归与非参数回归；自助法；单因子方差分析的单元格均值模型与因子效应模型。
source_hash: f7db7ef5efca
---

本章分为两部分。第一部分补全 [3.3.6](/3.3.6) 开始介绍的补救措施：当 [3.3.5](/3.3.5) 与 [3.3.11](/3.3.11) 的诊断显示误差方差不等、**多重共线性**、强影响点或非线性关系时，可以改换估计方法而不改模型。加权最小二乘在**异方差性**下恢复有效性；岭回归及其同类方法以少许偏差换取方差的大幅下降；稳健回归与非参数回归放宽模型假设；自助法则用来评估抽样分布难以推导的估计量的精度。第二部分开始讨论只有一个分类解释变量的方差分析。它仍是线性模型，其**设计矩阵**由示性变量构成，因此回归的全部结论都适用；它也为 [3.8](/3.8) 的实验设计做准备。这些模型的推断见 [3.3.13](/3.3.13)，两个因子的情形见 [3.3.14](/3.3.14)。

## 12.1. 补救措施

前几章的诊断可以归纳为一张检查清单。用**正态 QQ 图**或直方图检查**残差**的正态性；把残差对拟合值、对每个预测变量以及（适当时）对时间或空间作图，观察是否有弯曲的趋势或变化的散布；考察偏回归图。然后找出在影响度量上取极端值的观测（学生化删除残差、**帽子矩阵**的对角元、DFFITS、**Cook 距离**与 DFBETAS），并考察每个预测变量的容忍度（或**方差膨胀因子**）：容忍度低的变量需要重新编码或进行变量选择。本节汇集针对这些问题的补救方法。

### 12.1.1. 误差方差不等：加权最小二乘

考虑模型 $Y_i=\beta_0+\beta_1X_{i,1}+\cdots+\beta_{p-1}X_{i,p-1}+\varepsilon_i$，其中 $\varepsilon_i\sim\mathcal{N}(0,\sigma_i^2)$ 相互独立。若对所有 $i$ 都有 $\sigma_i^2=\sigma^2$，最大化**似然函数** $L=f_1f_2\cdots f_n$ 就是普通最小二乘。若各方差不同但已知，$Y_i$ 的密度为

$$
f_i=\frac{1}{\sqrt{2\pi}\,\sigma_i}\exp\left[-\frac12\left(\frac{Y_i-\beta_0-\beta_1X_{i,1}-\cdots-\beta_{p-1}X_{i,p-1}}{\sigma_i}\right)^2\right],
$$
关于各 $\beta$ 最大化 $L$ 等价于最小化

$$
\sum_{i=1}^n\left(\frac{Y_i-\beta_0-\beta_1X_{i,1}-\cdots-\beta_{p-1}X_{i,p-1}}{\sigma_i}\right)^2.
$$
每个观测按其方差的倒数加权：精确的观测分量更重。

**注 12.1.1** 如果忽略异方差、照样使用 OLS 估计量 $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$，会怎样？记 $\operatorname{Cov}(\boldsymbol{Y})=\Sigma\ne\sigma^2I_n$。估计量仍然无偏，因为 $\mathbb{E}\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}X\boldsymbol{\beta}=\boldsymbol{\beta}$ 只用到 $\mathbb{E}\boldsymbol{\varepsilon}=\boldsymbol{0}$；但其协方差矩阵变为

$$
\operatorname{Cov}(\boldsymbol{b})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\Sigma X(X^{\mathsf T}X)^{-1},
$$
不再是 $\sigma^2(X^{\mathsf T}X)^{-1}$。于是通常的标准误是错的，而 **Gauss–Markov 定理**的证明需要 $\Sigma=\sigma^2I_n$，不再适用：$\boldsymbol{b}$ 无偏，但一般不是方差最小的（命题 12.1.1 给出最优线性无偏估计）。实际中，OLS 的预测区间的覆盖率会低于或高于名义水平，取决于新观测所处的位置。

**定义 12.1.1（White 估计量）** $\operatorname{Cov}(\boldsymbol{b})$ 的 **White 估计量**（又称异方差稳健估计量或三明治估计量）用残差平方构成的对角矩阵代替未知的 $\Sigma$：

$$
\widehat{\operatorname{Cov}}(\boldsymbol{b})=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\hat\Sigma X(X^{\mathsf T}X)^{-1},\qquad \hat\Sigma=\operatorname{diag}(e_1^2,\dots,e_n^2).
$$

White 估计量保留 OLS 系数，只修正其标准误；在形式未知的异方差下它是相合的。它对预测区间无能为力：$\operatorname{Var}(Y_h-\hat Y_h)=\boldsymbol{X}_h^{\mathsf T}\operatorname{Cov}(\boldsymbol{b})\boldsymbol{X}_h+\sigma_h^2$ 需要估计新观测 $\boldsymbol{X}_h$ 处的误差方差 $\sigma_h^2$，也就是需要一个描述方差如何随预测变量变化的模型。这正是加权最小二乘所提供的。

**定义 12.1.2（加权最小二乘）** 给定权重 $w_i>0$，**加权最小二乘**（WLS）估计量 $\boldsymbol{b}_{\mathrm{w}}$ 最小化加权残差平方和

$$
Q_{\mathrm{w}}(\boldsymbol{\beta})=\sum_{i=1}^nw_i\,(Y_i-\boldsymbol{X}_i^{\mathsf T}\boldsymbol{\beta})^2=(\boldsymbol{Y}-X\boldsymbol{\beta})^{\mathsf T}W(\boldsymbol{Y}-X\boldsymbol{\beta}),\qquad W=\operatorname{diag}(w_1,\dots,w_n),
$$
其中 $\boldsymbol{X}_i^{\mathsf T}$ 是 $X$ 的第 $i$ 行。权重之和不必为 $1$。

**命题 12.1.1** 设 $\operatorname{Cov}(\boldsymbol{\varepsilon})=\Sigma=\operatorname{diag}(\sigma_1^2,\dots,\sigma_n^2)$，$\sigma_i^2$ 已知，取 $w_i=1/\sigma_i^2$，即 $W=\Sigma^{-1}$。则

$$
\boldsymbol{b}_{\mathrm{w}}=(X^{\mathsf T}WX)^{-1}X^{\mathsf T}W\boldsymbol{Y},\qquad \operatorname{Cov}(\boldsymbol{b}_{\mathrm{w}})=(X^{\mathsf T}WX)^{-1},
$$
并且 $\boldsymbol{b}_{\mathrm{w}}$ 是 $\boldsymbol{\beta}$ 的最优线性无偏估计。

**证明** 用 $W^{1/2}=\operatorname{diag}(1/\sigma_1,\dots,1/\sigma_n)$ 左乘模型：

$$
\underbrace{W^{1/2}\boldsymbol{Y}}_{\boldsymbol{Y}^*}=\underbrace{W^{1/2}X}_{X^*}\boldsymbol{\beta}+\underbrace{W^{1/2}\boldsymbol{\varepsilon}}_{\boldsymbol{\varepsilon}^*},\qquad \operatorname{Cov}(\boldsymbol{\varepsilon}^*)=W^{1/2}\Sigma W^{1/2}=I_n.
$$
变换后的模型满足 Gauss–Markov 假设（$\sigma^2=1$），且 $Q_{\mathrm{w}}(\boldsymbol{\beta})=\|\boldsymbol{Y}^*-X^*\boldsymbol{\beta}\|^2$。因此它的 OLS 估计量 $(X^{*\mathsf T}X^*)^{-1}X^{*\mathsf T}\boldsymbol{Y}^*=(X^{\mathsf T}WX)^{-1}X^{\mathsf T}W\boldsymbol{Y}$ 是最优线性无偏估计，协方差矩阵为 $(X^{*\mathsf T}X^*)^{-1}=(X^{\mathsf T}WX)^{-1}$。基于 $\boldsymbol{Y}$ 的线性估计也是 $\boldsymbol{Y}^*$ 的线性函数，故最优性可以移回原模型。$\square$

换言之，最优权重与方差成反比，$w_i=k/\sigma_i^2$，此时每个观测都有 $\operatorname{Var}(\sqrt{w_i}\,Y_i)=k$。计算 $\boldsymbol{b}_{\mathrm{w}}$ 很容易（`lm()` 的 `weights` 参数），实际的问题在于确定权重。分三种情形。

1. 方差已知：按命题 12.1.1 取 $w_i=1/\sigma_i^2$。
2. 只知道方差的相对大小：若比值 $\sigma_i^2/\sigma_j^2$ 已知，例如 $\sigma_i^2$ 与 $X_i$ 或 $X_i^2$ 成正比，就记 $\sigma_i^2=k/w_i$，其中 $w_i$ 已知、比例常数 $k$ 未知。此时 $\operatorname{Cov}(W^{1/2}\boldsymbol{Y})=kI_n$，估计量 $\boldsymbol{b}_{\mathrm{w}}$ 不变，$\operatorname{Cov}(\boldsymbol{b}_{\mathrm{w}})=k(X^{\mathsf T}WX)^{-1}$，$k$ 用变换后模型的误差均方估计：

$$
\hat k=\mathrm{MSE}_{\mathrm{w}}=\frac{\sum_i(Y_i^*-\hat Y_i^*)^2}{n-p}=\frac{\sum_iw_i(Y_i-\hat Y_i)^2}{n-p}=\frac{\sum_iw_ie_i^2}{n-p}.
$$
3. 方差完全未知：(a) 若有重复观测或近似重复观测（预测变量取值相同或相近的观测），在每组内用**样本方差** $s_i^2$ 估计方差，组内所有观测取 $w_i=1/s_i^2$。(b) 否则用两阶段估计：先作 OLS 拟合，再把残差绝对值 $\lvert e_i\rvert$ 对预测变量回归来建模标准差（或把残差平方 $e_i^2$ 对预测变量回归来建模方差）；拟合值 $\hat\sigma_i$（或 $\hat\sigma_i^2$）给出权重 $w_i=1/\hat\sigma_i^2$，再用它作 WLS。若系数变化较大，可以用 WLS 拟合的残差重复这两步，直到 $\boldsymbol{b}_{\mathrm{w}}$ 稳定；这是迭代重加权最小二乘（iteratively reweighted least squares）的一种形式。

在 (b) 中通常用残差绝对值而不用残差平方：它受离群观测的影响较小，而且它对预测变量的回归估计的是标准差，标准差对 $X$ 的依赖往往更接近线性。

**例 12.1.1** 一项研究调查了 54 名 20 至 60 岁的健康成年女性，$Y$ 是舒张压，$X$ 是年龄。散点图显示很强的线性关系、没有偏斜，但 $Y$ 的散布随年龄增大。

```r
a1 <- read.table("CH11TA01.txt")
colnames(a1) <- c("age", "diast")
fit <- lm(diast ~ age, data = a1)            # OLS
a1$absr <- abs(fit$residuals)
fit2 <- lm(absr ~ age, data = a1)            # model the standard deviation
a1$shat <- predict(fit2)                     # estimated sigma_i
a1$wt <- 1 / a1$shat^2                       # weights w_i = 1 / sigma_i^2
fit3 <- lm(diast ~ age, weights = wt, data = a1)   # WLS
summary(fit3)
```

| | OLS | WLS |
|---|---|---|
| 截距（标准误） | $56.157\ (3.994)$ | $55.566\ (2.521)$ |
| 年龄的斜率（标准误） | $0.580\ (0.0970)$ | $0.596\ (0.0792)$ |
| 斜率的 $t$ 值 | $5.98$ | $7.53$ |
| 残差标准误（自由度 52） | $8.146$ | $1.213$ |
| $R^2$ | $0.408$ | $0.521$ |

两个估计量都无偏，估计值几乎不变，但年龄系数的标准误从 $0.097$ 降到 $0.079$。

![左：散布随 X 增大的模拟数据的 OLS 与 WLS 拟合直线。右：OLS 残差绝对值对 X 的散点图，以及用来估计各观测标准差的拟合直线。](./plots/weighted-least-squares.py)

**注 12.1.2** WLS 输出中有两个数不能按 OLS 的方式解读。残差标准误 $1.213$ 是 $\sqrt{\mathrm{MSE}_{\mathrm{w}}}$，是加权尺度上 $\sqrt{k}$ 的估计，而不是 $Y$ 的误差标准差的估计；它在这里较小只是权重恰好这样标定的结果（所有权重乘以 $c$，它就乘以 $\sqrt c$），因此并非 WLS 的优势。同样，$R^2$ 对加权最小二乘没有明确的含义。WLS 的好处是系数的标准误更小、预测区间正确。

WLS 处理对角的 $\Sigma$。当误差还彼此相关时（例如时间序列或聚类数据，见 [3.3.5](/3.3.5)），同样的思想使用完整的协方差矩阵。

**定义 12.1.3（广义最小二乘）** 在模型 $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ 中，设 $\mathbb{E}[\boldsymbol{\varepsilon}\mid X]=\boldsymbol{0}$，$\operatorname{Cov}(\boldsymbol{\varepsilon}\mid X)=\Omega$ 正定。**广义最小二乘**（GLS）估计量最小化残差向量的 Mahalanobis 长度的平方：

$$
\hat{\boldsymbol{\beta}}_{\mathrm{GLS}}=\arg\min_{\boldsymbol{\beta}}(\boldsymbol{Y}-X\boldsymbol{\beta})^{\mathsf T}\Omega^{-1}(\boldsymbol{Y}-X\boldsymbol{\beta})=(X^{\mathsf T}\Omega^{-1}X)^{-1}X^{\mathsf T}\Omega^{-1}\boldsymbol{Y}.
$$

GLS 就是对线性变换后的数据作 OLS：取 **Cholesky 分解** $\Omega=CC^{\mathsf T}$，模型 $C^{-1}\boldsymbol{Y}=C^{-1}X\boldsymbol{\beta}+C^{-1}\boldsymbol{\varepsilon}$ 满足 $\operatorname{Cov}(C^{-1}\boldsymbol{\varepsilon})=I_n$，于是命题 12.1.1 的证明表明 GLS 是最优线性无偏估计。WLS 是 $\Omega$ 为对角矩阵的特例。

### 12.1.2. 多重共线性：岭回归

当预测变量近似线性相关时（**多重共线性**，[3.3.10](/3.3.10)），$X^{\mathsf T}X$ 接近奇异，$(X^{\mathsf T}X)^{-1}$ 的元素很大，于是 OLS 系数的方差很大。一个自然的办法是改为对某个 $\lambda>0$ 求 $X^{\mathsf T}X+\lambda I$ 的逆。这就是不适定问题的 Tikhonov 正则化；在统计中它由 A. E. Hoerl（1962）提出，并由 Hoerl 与 Kennard（1970）发展为岭回归，在机器学习中称为权重衰减（weight decay）。估计量变得有偏，但稳定得多，而且在 $p\gg n$ 时同样适用。

**定义 12.1.4（岭回归）** 对 $\lambda>0$，**岭回归**估计量是惩罚残差平方和的最小值点：

$$
Q(\boldsymbol{\beta})=(\boldsymbol{Y}-X\boldsymbol{\beta})^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol{\beta})+\lambda\sum_j\beta_j^2,\qquad \boldsymbol{b}^{R}(\lambda)=(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}\boldsymbol{Y}.
$$
预测变量先标准化，截距不受惩罚。

闭式解来自 $\partial Q/\partial\boldsymbol{\beta}=-2X^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol{\beta})+2\lambda\boldsymbol{\beta}=\boldsymbol{0}$，即 $(X^{\mathsf T}X+\lambda I)\boldsymbol{\beta}=X^{\mathsf T}\boldsymbol{Y}$；对每个 $\lambda>0$，$X^{\mathsf T}X+\lambda I$ 都是**正定矩阵**。标准化是必要的：惩罚对所有系数一视同仁，所以它们必须处于同一尺度。

**命题 12.1.2** 设 $X^{\mathsf T}X$ 可逆，其**谱分解**为 $X^{\mathsf T}X=V\operatorname{diag}(d_1,\dots,d_p)V^{\mathsf T}$，$d_j>0$，$\boldsymbol{b}$ 为 OLS 估计量。则对 $\lambda>0$：

1. （约束形式）$\boldsymbol{b}^R(\lambda)$ 是在约束 $\sum_j\beta_j^2\le c$ 下最小化 $(\boldsymbol{Y}-X\boldsymbol{\beta})^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol{\beta})$ 的解，其中 $c=\|\boldsymbol{b}^R(\lambda)\|^2$。
2. （收缩）$\boldsymbol{b}^R(\lambda)=(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}X\,\boldsymbol{b}$，因此在坐标 $V^{\mathsf T}\boldsymbol\beta$ 下，$\boldsymbol{b}$ 的每个分量乘以 $d_j/(d_j+\lambda)<1$；特别地，$\|\boldsymbol{b}^R(\lambda)\|$ 随 $\lambda$ 递减，且 $\lambda\to\infty$ 时趋于 $0$。
3. （偏差与方差）一般地 $\mathbb{E}\boldsymbol{b}^R(\lambda)=(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}X\boldsymbol{\beta}\ne\boldsymbol{\beta}$，并且

$$
\operatorname{Cov}(\boldsymbol{b}^R(\lambda))=\sigma^2(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}X(X^{\mathsf T}X+\lambda I)^{-1}=\sigma^2V\operatorname{diag}\Big(\frac{d_j}{(d_j+\lambda)^2}\Big)V^{\mathsf T},
$$
它小于 $\operatorname{Cov}(\boldsymbol{b})=\sigma^2V\operatorname{diag}(1/d_j)V^{\mathsf T}$，即两者之差正定。

**证明** 1. 若 $\sum_j\beta_j^2\le c$，由 $Q(\boldsymbol\beta)\ge Q(\boldsymbol{b}^R)$ 得 $\|\boldsymbol{Y}-X\boldsymbol\beta\|^2\ge\|\boldsymbol{Y}-X\boldsymbol{b}^R\|^2+\lambda(c-\|\boldsymbol\beta\|^2)\ge\|\boldsymbol{Y}-X\boldsymbol{b}^R\|^2$。这就是 Lagrange 乘子法的论证：$\lambda$ 是约束的乘子。2. 代入 $X^{\mathsf T}\boldsymbol{Y}=X^{\mathsf T}X\boldsymbol{b}$ 并对角化。3. 对 2 取期望与协方差；差的特征值为 $\sigma^2\big[1/d_j-d_j/(d_j+\lambda)^2\big]=\sigma^2\lambda(2d_j+\lambda)/[d_j(d_j+\lambda)^2]>0$。$\square$

因此随着 $\lambda$ 增大，系数向量的长度与方差都在收缩，而 $d_j$ 小的方向——数据在这些方向上信息很少、OLS 最不稳定——收缩得最多。代价是随 $\lambda$ 增大的偏差。Hoerl 与 Kennard 证明，总存在某个 $\lambda>0$，使总的**均方误差** $\mathbb{E}\|\boldsymbol{b}^R(\lambda)-\boldsymbol{\beta}\|^2$ 小于 OLS 的均方误差：这是一种**偏差–方差权衡**。实际中 $\lambda$ 用**交叉验证**（或广义交叉验证）选取，或者观察岭迹（ridge trace）——系数随 $\lambda$ 变化的曲线——取系数趋于稳定的最小 $\lambda$。

![左：模拟的共线预测变量下三个标准化系数的岭迹。右：岭估计量的偏差平方、方差及二者之和（均方误差）随 lambda 的变化；虚线是 OLS 的均方误差。](./plots/ridge-trace-bias-variance.py)

**例 12.1.2** 对 [3.3.9](/3.3.9) 与 [3.3.10](/3.3.10) 中三个预测变量高度相关的体脂数据，程序包 `MASS` 中的 `lm.ridge` 先把预测变量标准化，再计算岭回归的路径。

```r
library(MASS)
fits <- lm.ridge(fat ~ skinfold + thigh + midarm,
                 lambda = seq(0, 0.1, 0.001), data = b1)
plot(fits)                                 # ridge trace
whichIsBest <- which.min(fits$GCV)         # generalized cross-validation
coef(fits)[whichIsBest, ]
```

| $\lambda$ | 截距 | skinfold | thigh | midarm |
|---|---|---|---|---|
| $0$（OLS） | $117.08$ | $4.334$ | $-2.857$ | $-2.186$ |
| $0.019$ | $43.84$ | $2.117$ | $-0.960$ | $-1.018$ |

由广义交叉验证选出的系数小得多，量级也更合理；估计效率最低的系数收缩得最快。

为什么要惩罚系数的大小？大系数意味着把很大的权重放在某个特征上。对一组固定的点拟合次数越来越高的多项式时，残差平方和不断减小，系数却急剧膨胀、正负交替：拟合刻画的是仅属于这批训练数据的复杂关系，这就是**过拟合**。限制 $\sum_j\beta_j^2$ 可以排除这样的拟合。

**例 12.1.3** 设软件只能计算 OLS，即 $(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$。为了得到岭估计量，在数据中添加 $p$ 个伪观测：

$$
X^*=\begin{bmatrix}X\\ \sqrt\lambda\,I_p\end{bmatrix},\qquad \boldsymbol{Y}^*=\begin{bmatrix}\boldsymbol{Y}\\ \boldsymbol{0}_p\end{bmatrix}.
$$
则 $(\boldsymbol{Y}^*-X^*\boldsymbol\beta)^{\mathsf T}(\boldsymbol{Y}^*-X^*\boldsymbol\beta)=(\boldsymbol{Y}-X\boldsymbol\beta)^{\mathsf T}(\boldsymbol{Y}-X\boldsymbol\beta)+\lambda\boldsymbol\beta^{\mathsf T}\boldsymbol\beta$，且 $X^*$ 列满**秩**，所以对 $(X^*,\boldsymbol{Y}^*)$ 作 OLS 有意义，结果为 $(X^{*\mathsf T}X^*)^{-1}X^{*\mathsf T}\boldsymbol{Y}^*=(X^{\mathsf T}X+\lambda I_p)^{-1}X^{\mathsf T}\boldsymbol{Y}$。

### 12.1.3. Lasso 与弹性网络

岭回归收缩所有系数，但不把任何系数压缩到零，因此不能选择变量。把平方惩罚换成绝对值惩罚就改变了这一点。

**定义 12.1.5（Lasso）** 设 $Z$ 为标准化后的预测变量矩阵。**Lasso**（least absolute shrinkage and selection operator，R. Tibshirani，1996）最小化

$$
(\boldsymbol{Y}-Z\boldsymbol{\beta})^{\mathsf T}(\boldsymbol{Y}-Z\boldsymbol{\beta})+\lambda\sum_j\lvert\beta_j\rvert,\qquad\lambda>0;
$$
把惩罚换成 $\lambda\sum_j\beta_j^2$ 就是岭回归。

写成约束形式，Lasso 在菱形 $\sum_j\lvert\beta_j\rvert\le c$ 而不是球 $\sum_j\beta_j^2\le c$ 上最小化残差平方和。残差平方和的椭圆等值线通常先碰到菱形的顶点，而顶点处有些坐标恰为零，所以 Lasso 同时进行收缩与变量选择。它没有闭式解，解的路径用坐标下降法或 LARS 算法计算。

![OLS 估计周围残差平方和的椭圆等值线，以及岭回归（圆盘）与 Lasso（菱形）的约束区域；Lasso 的解落在顶点上，其中一个系数恰为零。](./plots/ridge-lasso-geometry.py)

**定义 12.1.6（弹性网络）** **弹性网络**（H. Zou 与 T. Hastie，2005）同时使用两种惩罚：

$$
\hat{\boldsymbol{\beta}}=\arg\min_{\boldsymbol{\beta}}\Big\{\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\lambda_1\|\boldsymbol{\beta}\|_1+\lambda_2\|\boldsymbol{\beta}\|_2^2\Big\},\qquad\lambda_1,\lambda_2\ge0.
$$

弹性网络同时处理**多重共线性**（通过 $\ell_2$ 部分，它使相关的预测变量成组地保留或剔除）与变量选择（通过 $\ell_1$ 部分）。两个调节参数在一组组合上用交叉验证选取。程序包 `glmnet` 用总强度 $\lambda$ 与混合参数 $\alpha\in[0,1]$ 表示惩罚，最小化

$$
\frac{1}{2n}\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2+\lambda\Big[\alpha\|\boldsymbol{\beta}\|_1+\frac{1-\alpha}{2}\|\boldsymbol{\beta}\|_2^2\Big],
$$
于是 $\alpha=1$ 是 Lasso，$\alpha=0$ 是岭回归，$\alpha\in(0,1)$ 是弹性网络。

```r
library(glmnet)
# x: matrix of predictors, y: response; glmnet standardizes x by default
fit <- glmnet(x, y, alpha = 1)             # Lasso path over a grid of lambda
cvfit <- cv.glmnet(x, y, alpha = 0.5)      # elastic net, lambda chosen by 10-fold CV
coef(cvfit, s = "lambda.min")
```

**注 12.1.3** 这些惩罚有贝叶斯解释（[3.2.7](/3.2.7)）。误差正态时，OLS 就是极大似然估计：$\hat{\boldsymbol\beta}_{\mathrm{OLS}}=\arg\min_{\boldsymbol\beta}\|\boldsymbol{Y}-X\boldsymbol\beta\|^2$ 使给定 $(\boldsymbol\beta,\sigma^2)$ 时 $\boldsymbol{Y}$ 的密度最大。频率学派把 $\boldsymbol\beta$ 看作未知常数，点估计是一个优化问题；贝叶斯学派把 $\boldsymbol\beta$ 看作服从**先验分布** $\pi(\boldsymbol\beta)$ 的随机变量，**后验分布**为 $\pi(\boldsymbol\beta\mid\boldsymbol{Y})\propto f(\boldsymbol{Y}\mid\boldsymbol\beta)\,\pi(\boldsymbol\beta)$。**最大后验估计**是后验分布的众数：

$$
\hat{\boldsymbol\beta}_{\mathrm{MAP}}=\arg\max_{\boldsymbol\beta}\pi(\boldsymbol\beta\mid\boldsymbol{Y})=\arg\min_{\boldsymbol\beta}\Big\{\frac{1}{2\sigma^2}\|\boldsymbol{Y}-X\boldsymbol\beta\|^2-\log\pi(\boldsymbol\beta)\Big\}.
$$
若各 $\beta_j$ 独立服从 $\mathcal{N}(0,\tau^2)$，则 $-\log\pi(\boldsymbol\beta)=\|\boldsymbol\beta\|^2/(2\tau^2)+\text{const}$，MAP 估计就是 $\lambda=\sigma^2/\tau^2$ 的岭估计；若它们独立服从密度为 $\frac{1}{2s}\mathrm{e}^{-\lvert\beta\rvert/s}$ 的 Laplace（双指数）分布，MAP 估计就是 $\lambda=2\sigma^2/s$ 的 Lasso。

### 12.1.4. 强影响点：稳健回归

最小二乘对离群观测非常敏感，因为残差平方赋予它们很大的影响。稳健回归（robust regression）的基本思想是采用对离群观测不敏感的拟合方法。可以不最小化残差平方和，而最小化

- 残差绝对值之和 $\sum_i\lvert Y_i-\boldsymbol{X}_i^{\mathsf T}\boldsymbol\beta\rvert$：最小绝对偏差（least absolute deviations），简记 LAD，又称最小绝对残差 LAR，即中位数回归；
- 残差平方的中位数：最小中位数平方（least median of squares），简记 LMS，它能容忍将近一半的观测是离群值。

第三种方法是迭代重加权最小二乘，简记 IRLS：作加权回归，权重由上一次拟合的残差计算，使标准化残差大的观测得到小的权重（例如 Huber 权或双平方权），反复进行直到系数收敛。稳健性的代价是大量计算；稳健拟合应当与最小二乘拟合相互对照，而不能代替对离群观测本身的研究。

### 12.1.5. 非线性：非参数回归与回归树

当没有简单的参数形式能拟合回归函数时，非参数回归（nonparametric regression）直接估计 $\mathbb{E}[Y\mid X=x]$；它有多种版本，理论也很有意思（[3.6](/3.6)），所有版本都有一个平衡偏差与方差的光滑参数或惩罚参数。

- 局部多项式回归在每个 $x$ 的移动邻域内用加权最小二乘拟合低次多项式。R 中 `lowess`（局部加权散点光滑）处理简单回归，`loess`（局部回归）处理一般情形；前几章残差图上添加的光滑曲线就是这一类。
- 光滑样条在所有光滑函数 $f$ 中最小化 $\sum_i(Y_i-f(X_i))^2+\lambda\int f''(x)^2\,\mathrm{d}x$；R 中 `smooth.spline` 处理简单回归。
- 回归树（regression tree）是机器学习中的标准方法：按单个预测变量反复把数据划分到各个结点，从而把预测变量空间划分成若干矩形；每个矩形中的预测值是其中响应的均值。

### 12.1.6. 评估估计量：自助法

对于复杂的估计量（由数据选取 $\lambda$ 后的岭系数、稳健拟合、系数之比），抽样分布难以推导。自助法（bootstrap）由 B. Efron 于 1979 年提出，它用重抽样来近似抽样分布：从数据中有放回地抽样，对每个重抽样样本重新拟合模型，用所得的感兴趣量的分布估计其精度。从观测中重抽样，相当于用**经验分布函数**（[3.1.7](/3.1.7)）代替未知的分布。回归模型的自助法有两种。

**算法 12.1.1（观测重抽样）** 1. 从原样本中有放回地抽取 $n$ 个观测 $(\boldsymbol{X}_i,Y_i)$，得到一个自助样本。2. 对它作 OLS，得到 $\hat{\boldsymbol\beta}^*_b$。3. 对 $b=1,\dots,B$ 重复，按通常方式用这些 $\hat{\boldsymbol\beta}^*_b$ 构造系数的自助标准误与置信区间（例如 $\hat\beta^*_{b,j}$ 的样本标准差，或其 $\alpha/2$ 与 $1-\alpha/2$ 分位数）。

**算法 12.1.2（残差重抽样）** 1. 对原样本作 OLS，得到拟合值 $\hat Y_i$ 与残差 $e_i$。2. 从 $e_1,\dots,e_n$ 中有放回地抽取 $e_{b1}^{*},\dots,e_{bn}^{*}$，令 $Y^*_{bi}=\hat Y_i+e_{bi}^{*}$。3. 把 $Y^*_{bi}$ 对固定的 $\boldsymbol{X}_i$ 回归，得到 $\hat{\boldsymbol\beta}^*_b$。4. 对 $b=1,\dots,B$ 重复，其余同算法 12.1.1。

**注 12.1.4** 哪种做法更合理取决于具体情形。残差重抽样保持设计固定，并假定误差可交换，因此适用于预测变量由设计固定、模型（包括方差齐性）恰当的情形；观测很少时它也是自然的选择。观测重抽样把 $(\boldsymbol{X}_i,Y_i)$ 看作来自某个联合分布的随机样本；它在异方差和回归函数设定错误时仍然有效，代价是设计随重抽样而变化。两者在统计计算（[3.5](/3.5)）中会进一步展开。

## 12.2. 单因子方差分析

### 12.2.1. 基本概念

在**方差分析**（ANOVA）中，响应变量 $Y$ 与回归中一样是连续的，但解释变量是分类的（定性的或离散的）。

**定义 12.2.1（因子）** 分类的解释变量称为**因子**，它的 $r$ 个可能取值称为**因子水平**。水平也常称为组或处理；在单因子研究中，每个水平对应一个响应总体。

记 $Y_{ij}$ 为因子第 $i$ 个水平下的第 $j$ 个观测，$i=1,\dots,r$，$j=1,\dots,n_i$；各样本量 $n_i$ 不必相等，$n_T=\sum_in_i$ 为观测总数。方差分析关注不同因子水平下的平均响应，分析通常分两步：

1. 判断各因子水平的均值是否全都相同；
2. 若不同，考察它们如何不同，以及这些差异意味着什么。

$r=2$ 时第 1 步就是合并方差的两样本 **t 检验**（[3.2.5](/3.2.5)）；单因子方差分析把它推广到 $r$ 组。

方差分析就是回归。区别在于模型关注的东西：回归模型关心一个或多个定量预测变量与响应之间的统计关系 $\mathbb{E}Y=f(X)$，而方差分析不考虑 $X$ 各水平之间的数量差异（各水平甚至可能根本没有自然的顺序），也不考虑它们与 $\mathbb{E}Y$ 的统计关系，只比较均值。用示性变量对各水平编码，就把方差分析模型变成线性回归模型，我们正是这样拟合它的。

### 12.2.2. 单元格均值模型

方差分析模型假定：

1. 响应的均值可以依赖于因子的水平；
2. 每个因子水平下的响应是来自相应概率分布的随机样本，并且与其他水平下的响应独立；
3. 这些分布都是正态分布；
4. 它们的方差都相同。

**定义 12.2.2（单元格均值模型）** "单元格"指因子的一个水平。**单元格均值模型**为

$$
Y_{ij}=\mu_i+\varepsilon_{ij},\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),\qquad i=1,\dots,r,\quad j=1,\dots,n_i,
$$
其中 $\mu_i$ 是水平 $i$ 下所有观测的理论均值（期望）。等价地说，$Y_{ij}\sim\mathcal{N}(\mu_i,\sigma^2)$ 相互独立。

模型的参数是 $\mu_1,\dots,\mu_r$ 与 $\sigma^2$。问题"解释变量是否有助于解释 $Y$？"变成"各 $\mu_i$ 是否不同？"，即

$$
H_0\colon\mu_1=\mu_2=\cdots=\mu_r\ (=\mu,\text{ a constant})\qquad\text{versus}\qquad H_1\colon\text{not all }\mu_i\text{ are equal}.
$$

**定理 12.2.1** 记 $\bar Y_{i\cdot}=\sum_{j=1}^{n_i}Y_{ij}/n_i$ 为水平 $i$ 的样本均值，$s_i^2=\sum_{j=1}^{n_i}(Y_{ij}-\bar Y_{i\cdot})^2/(n_i-1)$ 为样本方差。在单元格均值模型中，$\mu_i$ 的最小二乘（也是极大似然）估计量为 $\hat\mu_i=\bar Y_{i\cdot}$，$\sigma^2$ 的无偏合并估计量为

$$
s^2=\frac{\sum_i(n_i-1)s_i^2}{\sum_i(n_i-1)}=\frac{\sum_i(n_i-1)s_i^2}{n_T-r}=\mathrm{MSE}.
$$

**证明** 平方和 $\sum_i\sum_j(Y_{ij}-\mu_i)^2$ 分解为 $r$ 个和，第 $i$ 个只含 $\mu_i$，由样本均值使之最小。每个 $s_i^2$ 都是 $\sigma^2$ 的无偏估计，所以它们的任何加权平均也是；取权重 $n_i-1$ 就得到 $s^2=\sum_i\sum_j(Y_{ij}-\bar Y_{i\cdot})^2/(n_T-r)$，即拟合回归的误差均方。$\square$

与合并方差 $t$ 检验一样，各 $s_i^2$ 按与自由度 $n_i-1$ 成比例的权重合并；除非所有 $n_i$ 相等，否则不能简单平均。

记 $\bar Y_{\cdot\cdot}=\sum_i\sum_jY_{ij}/n_T$ 为总样本均值；所有 $n_i=n$ 时 $\bar Y_{\cdot\cdot}=\sum_i\bar Y_{i\cdot}/r$。总变差与回归中一样分解（[3.3.4](/3.3.4)）：

$$
\underbrace{\sum_{i,j}(Y_{ij}-\bar Y_{\cdot\cdot})^2}_{\mathrm{SSTO}}=\underbrace{\sum_in_i(\bar Y_{i\cdot}-\bar Y_{\cdot\cdot})^2}_{\mathrm{SSTR}}+\underbrace{\sum_{i,j}(Y_{ij}-\bar Y_{i\cdot})^2}_{\mathrm{SSE}},
$$
因为交叉项 $2\sum_i(\bar Y_{i\cdot}-\bar Y_{\cdot\cdot})\sum_j(Y_{ij}-\bar Y_{i\cdot})$ 为零。$\mathrm{SSTR}$ 是处理平方和（treatment sum of squares），即回归表述中的回归平方和或模型平方和 $\mathrm{SSR}$，是各水平均值围绕总均值的变差；$\mathrm{SSE}$ 是误差（残差）平方和，即水平内部的变差。

| 来源 | 自由度 | 平方和 | 均方 |
|---|---|---|---|
| 处理（模型） | $r-1$ | $\mathrm{SSTR}=\sum_in_i(\bar Y_{i\cdot}-\bar Y_{\cdot\cdot})^2$ | $\mathrm{MSTR}=\mathrm{SSTR}/(r-1)$ |
| 误差 | $n_T-r$ | $\mathrm{SSE}=\sum_{i,j}(Y_{ij}-\bar Y_{i\cdot})^2$ | $\mathrm{MSE}=\mathrm{SSE}/(n_T-r)$ |
| 总计 | $n_T-1$ | $\mathrm{SSTO}=\sum_{i,j}(Y_{ij}-\bar Y_{\cdot\cdot})^2$ | |

**定理 12.2.2（期望均方）** 在单元格均值模型中，

$$
\mathbb{E}[\mathrm{MSE}]=\sigma^2,\qquad \mathbb{E}[\mathrm{MSTR}]=\sigma^2+\frac{\sum_in_i(\mu_i-\mu_\cdot)^2}{r-1},\qquad \mu_\cdot=\frac{\sum_in_i\mu_i}{n_T}.
$$

**证明** 第一式即定理 12.2.1。对第二式，$\bar Y_{i\cdot}-\bar Y_{\cdot\cdot}$ 的均值为 $\mu_i-\mu_\cdot$，且 $\mathbb{E}[\mathrm{SSTR}]=\sum_in_i(\mu_i-\mu_\cdot)^2+\mathbb{E}\big[\sum_in_i(\bar\varepsilon_{i\cdot}-\bar\varepsilon_{\cdot\cdot})^2\big]$。最后的期望等于 $\sum_in_i\mathbb{E}\bar\varepsilon_{i\cdot}^2-n_T\mathbb{E}\bar\varepsilon_{\cdot\cdot}^2=\sum_in_i\frac{\sigma^2}{n_i}-n_T\frac{\sigma^2}{n_T}=(r-1)\sigma^2$。$\square$

因此恰在各水平均值不同时 $\mathbb{E}[\mathrm{MSTR}]>\mathbb{E}[\mathrm{MSE}]$，这提示我们比较两个均方。在更复杂的模型中，期望均方告诉我们每个 **F 检验**该用哪个比值。

**定理 12.2.3（方差分析 F 检验）** 在 $H_0\colon\mu_1=\cdots=\mu_r$ 下，

$$
F^*=\frac{\mathrm{MSTR}}{\mathrm{MSE}}\sim F_{r-1,\,n_T-r}.
$$
水平 $\alpha$ 的检验在 $F^*>F_{r-1,n_T-r,\alpha}$ 时拒绝 $H_0$；通常报告 **p 值** $\mathbb{P}(F_{r-1,n_T-r}>F^*)$。

**证明** 这就是下面回归表述中的整体 $F$ 检验：总有 $\mathrm{SSE}/\sigma^2\sim\chi^2_{n_T-r}$；在 $H_0$ 下 $\mathrm{SSTR}/\sigma^2\sim\chi^2_{r-1}$，且与 $\mathrm{SSE}$ 独立，因为各 $\bar Y_{i\cdot}$ 与各 $s_i^2$ 独立（[3.2.2](/3.2.2)）。$\square$

用回归拟合单元格均值模型时，每个水平用一个示性变量：观测来自第 $i$ 组时，第 $i$ 个解释变量取 $1$，否则取 $0$。于是设计矩阵每行只有一个 $1$，位于其所在组的列：

$$
X=\begin{bmatrix}1&0&\cdots&0\\0&1&\cdots&0\\\vdots&&\ddots&\vdots\\0&0&\cdots&1\end{bmatrix}\ \begin{matrix}\text{group }1\\\text{group }2\\\vdots\\\text{group }r\end{matrix},\qquad \boldsymbol\beta=(\mu_1,\dots,\mu_r)^{\mathsf T},
$$
没有截距列：$r$ 个示性变量之和已经是全 1 列。设计矩阵及相应的估计在 [3.3.13](/3.3.13) 中具体推导。

### 12.2.3. 因子效应模型

**定义 12.2.3（因子效应模型）** **因子效应模型**是单元格均值模型的重新参数化

$$
Y_{ij}=\mu+\tau_i+\varepsilon_{ij},\qquad \varepsilon_{ij}\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),
$$
其中 $\mu$ 是所有观测共有的常数，按研究目的定义；$\tau_i=\mu_i-\mu$ 称为第 $i$ 个**因子水平效应**或**处理效应**，对每个因子水平是一个常数。

两个模型描述的是同一族分布，$\mu_i=\mu+\tau_i$；但因子效应形式更便于看待更复杂的模型（[3.3.14](/3.3.14) 中的两个因子及其交互作用），零假设也更容易表述："没有因子效应"就是 $\tau_1=\cdots=\tau_r=0$。由于参数比均值多一个，因子效应模型需要对 $\tau_i$ 加一个约束；这一点以及 $\mu$ 的选取是下一章的内容。

## 小结 {#summary}

- 误差方差不等时，OLS 仍然无偏，但失去有效性，标准误也是错的。White 估计量修正标准误；取 $w_i\propto1/\sigma_i^2$ 的加权最小二乘是最优线性无偏估计，实际中权重由重复观测估计，或把残差绝对值对预测变量回归来估计。广义最小二乘把这一方法推广到相关的误差。
- 岭回归 $(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}\boldsymbol{Y}$ 以偏差为代价收缩系数及其方差；Lasso 还能把系数压缩为零，弹性网络结合了两者。它们分别是正态先验与 Laplace 先验下的 MAP 估计。
- 稳健回归（LAD、LMS、IRLS）限制离群观测的影响；非参数回归与回归树放宽回归函数的形式；自助法通过对观测或残差重抽样来估计精度。
- 单因子方差分析在单元格均值模型 $Y_{ij}=\mu_i+\varepsilon_{ij}$ 或因子效应模型 $Y_{ij}=\mu+\tau_i+\varepsilon_{ij}$ 中比较 $r$ 个因子水平的均值；$\hat\mu_i=\bar Y_{i\cdot}$，$\mathrm{SSTO}=\mathrm{SSTR}+\mathrm{SSE}$，$H_0\colon\mu_1=\cdots=\mu_r$ 用 $F^*=\mathrm{MSTR}/\mathrm{MSE}\sim F_{r-1,n_T-r}$ 检验。
