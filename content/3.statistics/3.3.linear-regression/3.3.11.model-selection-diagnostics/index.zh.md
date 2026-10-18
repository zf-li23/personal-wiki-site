---
title: 模型选择与诊断
description: 模型的建立与核实，最优子集与逐步回归，R²、调整的 R²、Mallows Cp、AIC、BIC、PRESS 与预测 R² 等准则及留一公式，以及多元回归的诊断——附加变量图、学生化删除残差、杠杆值、DFFITS、Cook 距离、DFBETAS 与方差膨胀因子。
source_hash: 53f8854c1721
---

面对许多候选的解释变量，我们如何决定取舍？选定模型之后，又如何检查它？本章对多元回归回答这两个问题。前半部分讨论模型选择：建立与核实模型的总体策略，在变量子集上的搜索，以及比较模型的准则——从 $R^2$ 和调整的 $R^2$ 到 Mallows $C_p$、信息准则 AIC 与 BIC，以及 PRESS 统计量——它们都在欠拟合与过拟合之间求得平衡。后半部分把 [3.3.5](/3.3.5) 与 [3.3.6](/3.3.6) 的诊断推广到多个解释变量：用附加变量图判断每个变量的形式，用学生化删除残差判断离群的响应，用杠杆值判断解释变量的离群取值，用 DFFITS、Cook 距离和 DFBETAS 判断影响，用方差膨胀因子判断 [3.3.10](/3.3.10) 的多重共线性。前面用到的删除残差与 Cook 距离的公式，在这里由删去单个个体的一个恒等式统一推出。补救措施见 [3.3.12](/3.3.12)；**Lasso** 等收缩方法见 [3.2.3](/3.2.3) 与 [3.4.7](/3.4.7)。

## 11.1. 什么是模型选择

### 11.1.1. 模型的建立与核实

回归模型通常分四个阶段建立：

1. 收集与整理数据；
2. 借助探索性分析和专业知识精简解释变量；
3. 改进和选择模型，包括诊断以及可能加入的曲率项和交互项；
4. 核实模型。

核实（validation）评价模型的表现，并给出其泛化能力的无偏估计。用于拟合模型、估计参数的数据是训练数据；理想情况下，应当用另一组数据（测试数据或新数据）来检验拟合好的模型，例如它的预测能力。没有新数据时，**交叉验证**（[3.4.10](/3.4.10)）把数据分成训练与测试两部分：一次划分、留一法，或 $K$ 折交叉验证——把数据分成 $K$ 份（比如 $K=5$ 或 $10$），每一份轮流作为测试集，用其余 $K-1$ 份拟合的模型来预测它，再把 $K$ 个预测误差取平均。

**定义 11.1.1（过拟合与欠拟合）** 当模型对训练数据的拟合远好于它对新数据的预测，即众多参数迁就了这个样本特有的噪声时，称模型**过拟合**。当模型过于简单、未能抓住系统性的结构，例如遗漏了重要的解释变量，从而预测有偏时，称模型**欠拟合**。

由 [3.3.10](/3.3.10) 可得一条基本规则：候选解释变量的清单必须包含所有真正能预测响应的变量。否则选出的每个模型都是设定不足的，系数有偏，分析具有误导性。在这份清单之内，目标是一个合理而有用的模型，既不欠拟合，也不过拟合。

### 11.1.2. 常规方法

从现有解释变量中选出一个子集作为"最佳"模型，涉及两个决定：用多少个解释变量（子集大小），以及给定大小后用哪些。方法分为三类：

| 类别 | 思路 | 主要方法 |
|---|---|---|
| 子集选择 | 每个变量要么整个保留、要么整个删除，搜索最优子集 | 最优子集回归；向前、向后与逐步选择 |
| 正则化与收缩 | 惩罚系数的大小；系数收缩到 $0$ 时间接地完成选择 | **岭回归**（只收缩，适合多重共线性）；Lasso（把部分系数恰好压缩为 $0$） |
| 交叉验证 | 用留出数据上的预测误差评价候选模型（或调节参数 $\lambda$） | **留一交叉验证**（小样本）；$K$ 折交叉验证（$K=5$ 或 $10$） |

子集选择与收缩方法提出候选者；AIC、BIC、调整的 $R^2$ 等准则或交叉验证充当在其中做出选择的裁判。

**定义 11.1.2（最优子集回归与逐步回归）** 有 $P-1$ 个候选解释变量时，含截距的模型共有 $2^{P-1}$ 个（$P-1=10$ 时为 $1024$ 个）。**最优子集回归**拟合所有这些模型（或用无须全部拟合就能找出最佳者的算法），按某个准则比较，并报告每种大小下的若干个好模型。**逐步回归**则贪婪地搜索：**向前选择**从不含变量的模型出发，每一步加入使拟合改善最多的变量，只要它的 $t$ 检验或 $F$ 检验在预设水平 $\alpha_{\mathrm{enter}}$ 下显著；**向后剔除**从完全模型出发，只要最不显著的变量的 $p$ 值超过 $\alpha_{\mathrm{remove}}$ 就把它删去；向前逐步选择像向前选择一样加入变量，但每加入一个变量后都检查已在模型中的变量是否变得多余，若是就把它删去。

最优子集回归在候选变量不超过约 $30$ 到 $40$ 个时可行，并能给出若干个好模型供最后考虑；候选变量更多时，自动搜索最终只给出一个模型。逐步回归的结果不应被滥用或夸大：

- 最终模型并不保证在任何特定意义下最优；
- 这个过程只给出一个模型，而往往存在若干个同样好的模型；
- 不借助研究者的知识，可能需要强制把重要的预测变量放进模型；
- 不应过度解读变量进入模型的先后顺序；
- 要做许多次 $t$ 检验，因此很可能纳入了一些不重要的预测变量，或排除了一些重要的预测变量。

能否改为拟合包含全部候选变量的完全模型，保留系数显著的变量？一般不能。$t$ 检验是"最后加入变量"检验，相关的变量可能每一个都不显著而合起来却重要（[3.3.9](/3.3.9) 的体脂数据），而且同时做了许多检验。

## 11.2. 选择准则

本节中，候选模型含 $p-1$ 个解释变量、$p$ 个参数（$1\le p\le P$），误差平方和为 $\mathrm{SSE}_p$，均方为 $\mathrm{MSE}_p=\mathrm{SSE}_p/(n-p)$；完全模型含全部 $P-1$ 个候选变量。

### 11.2.1. R² 与调整的 R²

[3.3.4](/3.3.4) 的**决定系数**及其调整形式为

$$
R_p^2=1-\frac{\mathrm{SSE}_p}{\mathrm{SSTO}},\qquad R_{a,p}^2=1-\frac{n-1}{n-p}\cdot\frac{\mathrm{SSE}_p}{\mathrm{SSTO}}=1-\frac{\mathrm{MSE}_p}{\mathrm{SSTO}/(n-1)}.
$$
完全模型总使 $R_p^2$ 最大（$\mathrm{SSE}_p$ 最小），所以 $R_p^2$ 无法决定模型大小；我们改为寻找它的增长开始放缓之处，这表明再加的变量不重要。调整的 $R_{a,p}^2$ 考虑了参数个数：可以选使 $R_{a,p}^2$ 最大、即使 $\mathrm{MSE}_p$ 最小的模型。

### 11.2.2. Mallows Cp

设 $\boldsymbol{\mu}=(\mu_1,\dots,\mu_n)^{\mathsf T}=\mathbb{E}(\boldsymbol{Y})$ 是各观测 $X$ 值处的真实平均响应。设计矩阵为 $X_p$、帽子矩阵为 $H_p$ 的候选模型给出 $\hat{\boldsymbol{Y}}_p=H_p\boldsymbol{Y}$，$\mathbb{E}(\hat{\boldsymbol{Y}}_p)=H_p\boldsymbol{\mu}$，$\operatorname{Cov}(\hat{\boldsymbol{Y}}_p)=\sigma^2H_p$。其总均方误差分解为偏差平方与方差：

$$
\sum_{i=1}^n\mathbb{E}(\hat Y_{i,p}-\mu_i)^2=\sum_{i=1}^n\big(\mathbb{E}(\hat Y_{i,p})-\mu_i\big)^2+\sum_{i=1}^n\operatorname{Var}(\hat Y_{i,p}).
$$
变量少则偏差大，变量多则方差大；最佳的模型复杂度使二者之和最小，这就是**偏差–方差权衡**。

**定理 11.2.1** 设 $\operatorname{Cov}(\boldsymbol{Y})=\sigma^2I_n$。候选模型的标准化总均方误差为

$$
\Gamma_p=\frac{1}{\sigma^2}\sum_{i=1}^n\mathbb{E}(\hat Y_{i,p}-\mu_i)^2=\frac{\mathbb{E}(\mathrm{SSE}_p)}{\sigma^2}-(n-2p),
$$
且 $\Gamma_p\ge p$，等号成立当且仅当模型无偏，即 $H_p\boldsymbol{\mu}=\boldsymbol{\mu}$。

**证明** 方差部分为 $\operatorname{tr}\operatorname{Cov}(\hat{\boldsymbol{Y}}_p)=\sigma^2\operatorname{tr}(H_p)=p\sigma^2$。偏差部分为 $\|H_p\boldsymbol{\mu}-\boldsymbol{\mu}\|^2=\boldsymbol{\mu}^{\mathsf T}(I_n-H_p)\boldsymbol{\mu}$。对任何均值为 $\boldsymbol{\mu}$、协方差为 $\Sigma$ 的随机向量，$\mathbb{E}(\boldsymbol{Y}^{\mathsf T}A\boldsymbol{Y})=\operatorname{tr}(A\Sigma)+\boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}$；取 $A=I_n-H_p$ 得 $\mathbb{E}(\mathrm{SSE}_p)=(n-p)\sigma^2+\boldsymbol{\mu}^{\mathsf T}(I_n-H_p)\boldsymbol{\mu}$。因此偏差部分为 $\mathbb{E}(\mathrm{SSE}_p)-(n-p)\sigma^2\ge0$，且 $\sigma^2\Gamma_p=p\sigma^2+\mathbb{E}(\mathrm{SSE}_p)-(n-p)\sigma^2$。$\square$

若完全模型包含全部重要变量，$\mathrm{MSE}_P$ 就是 $\sigma^2$ 的无偏估计；用估计代替未知量就得到一个准则。

**定义 11.2.1（Mallows Cp）** 候选模型的 **Mallows Cp** 为

$$
C_p=\hat\Gamma_p=\frac{\mathrm{SSE}_p}{\mathrm{MSE}_P}-(n-2p),
$$
其中 $\mathrm{MSE}_P$ 是完全模型的均方误差。

对完全模型恰有 $C_P=P$。无偏的模型 $C_p\approx p$；在这样的模型中，我们偏好 $C_p$ 小的。$C_p\gg p$ 表明有明显偏差，即遗漏了重要的预测变量；$C_p\ll p$（由于抽样波动是可能的）可能提示过拟合。通常把 $C_p$ 对 $p$ 作图并画出直线 $C_p=p$，寻找位于直线附近或下方、$C_p$ 较小的模型。

![六个模拟候选预测变量（其中三个是重要的）的所有子集的 Mallows Cp 对参数个数 p 的图：遗漏重要预测变量的模型远在直线 Cp = p 上方，包含全部三个重要预测变量的模型位于直线附近，最小的 Cp 由真实的三变量模型取得](./plots/mallows-cp.py)

### 11.2.3. AIC 与 BIC

**赤池信息准则**和**贝叶斯信息准则**（也称 Schwarz 贝叶斯准则，SBC）已在 [3.4.11](/3.4.11) 中对一般的似然模型定义：$\mathrm{AIC}=-2\ln\hat L+2m$，$\mathrm{BIC}=-2\ln\hat L+m\ln n$，其中 $\hat L$ 是极大化的似然，$m$ 是参数个数。二者都取越小越好。

**命题 11.2.1** 对有 $p$ 个回归系数的正态线性模型，相差一个对所有候选模型都相同的常数，

$$
\mathrm{AIC}_p=n\ln\frac{\mathrm{SSE}_p}{n}+2p,\qquad\mathrm{BIC}_p=n\ln\frac{\mathrm{SSE}_p}{n}+p\ln n.
$$

**证明** $\sigma^2$ 的极大似然估计为 $\hat\sigma^2=\mathrm{SSE}_p/n$，故 $-2\ln\hat L=n\ln(2\pi)+n\ln\hat\sigma^2+\mathrm{SSE}_p/\hat\sigma^2=n\ln(2\pi)+n\ln(\mathrm{SSE}_p/n)+n$。$n\ln(2\pi)+n$ 这两项，以及每个模型都有的参数 $\sigma^2$ 的惩罚，都与模型无关。$\square$

第一项奖励拟合，第二项惩罚复杂度。由于 $n\ge8$ 时 $\ln n>2$，BIC 对增加参数的惩罚比 AIC 重，倾向于选出较小的模型。若 $\sigma^2$ 已知，$-2\ln\hat L=\mathrm{SSE}_p/\sigma^2+\text{常数}$，于是 AIC 与（用 $\sigma^2$ 代替 $\mathrm{MSE}_P$ 的）$C_p$ 只相差一个常数：对正态线性回归，这两个准则是等价的；$\sigma^2$ 需要估计时，二者也很接近。

### 11.2.4. PRESS 与预测 R²

以上准则都在拟合所用的数据上评价模型。PRESS 准则则用其他个体来预测每一个个体，这是留一交叉验证的一种形式。设 $\boldsymbol{b}_{(-i)}$ 是不用个体 $i$、由删去第 $i$ 行的设计矩阵 $X_{(-i)}$ 和响应 $\boldsymbol{Y}_{(-i)}$ 算出的最小二乘估计，$\hat Y_{i(-i)}=\boldsymbol{x}_i^{\mathsf T}\boldsymbol{b}_{(-i)}$ 是由此得到的 $Y_i$ 的预测。

**定义 11.2.2（PRESS 与预测 R²）** 模型的预测平方和（**PRESS**）为

$$
\mathrm{PRESS}_p=\sum_{i=1}^n\big(Y_i-\hat Y_{i(-i)}\big)^2,
$$
并称 $R_{\mathrm{pred}}^2=1-\mathrm{PRESS}_p/\mathrm{SSTO}$ 为**预测 R²**。偏好 $\mathrm{PRESS}_p$ 小（$R_{\mathrm{pred}}^2$ 大）的模型。

计算 PRESS 不需要重新拟合 $n$ 次。关键在于删去一个个体的效果，它由 **Sherman–Morrison 公式**给出：若 $A$ 与 $A+B$ 可逆且 $B$ 的秩为 $1$，则令 $g=\operatorname{tr}(BA^{-1})\ne-1$，有

$$
(A+B)^{-1}=A^{-1}-\frac{1}{1+g}A^{-1}BA^{-1}.
$$

**定理 11.2.2（留一公式）** 设 $h_{ii}=\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i<1$ 是帽子矩阵的第 $i$ 个对角元，$e_i=Y_i-\hat Y_i$ 是第 $i$ 个残差。则

$$
\boldsymbol{b}-\boldsymbol{b}_{(-i)}=\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_ie_i}{1-h_{ii}},\qquad Y_i-\hat Y_{i(-i)}=\frac{e_i}{1-h_{ii}}.
$$
因此 $\mathrm{PRESS}_p=\sum_{i=1}^n\big(e_i/(1-h_{ii})\big)^2$ 只需一次拟合就能算出。

**证明** 删去第 $i$ 行，得 $X_{(-i)}^{\mathsf T}X_{(-i)}=X^{\mathsf T}X-\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}$，$X_{(-i)}^{\mathsf T}\boldsymbol{Y}_{(-i)}=X^{\mathsf T}\boldsymbol{Y}-\boldsymbol{x}_iY_i$。对 $A=X^{\mathsf T}X$、$B=-\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}$、$g=-h_{ii}$ 应用 Sherman–Morrison 公式，得

$$
\big(X_{(-i)}^{\mathsf T}X_{(-i)}\big)^{-1}=(X^{\mathsf T}X)^{-1}+\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}}{1-h_{ii}}.
$$
乘以 $X^{\mathsf T}\boldsymbol{Y}-\boldsymbol{x}_iY_i$ 并利用 $\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}=\hat Y_i$，

$$
\boldsymbol{b}_{(-i)}=\boldsymbol{b}+\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i\hat Y_i}{1-h_{ii}}-(X^{\mathsf T}X)^{-1}\boldsymbol{x}_iY_i-\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_ih_{ii}Y_i}{1-h_{ii}}=\boldsymbol{b}+\frac{(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i}{1-h_{ii}}(\hat Y_i-Y_i).
$$
最后 $Y_i-\hat Y_{i(-i)}=\boldsymbol{x}_i^{\mathsf T}(\boldsymbol{b}-\boldsymbol{b}_{(-i)})+e_i=h_{ii}e_i/(1-h_{ii})+e_i=e_i/(1-h_{ii})$。$\square$

由于 $0<1-h_{ii}\le1$，每个留一误差的绝对值都不小于对应残差的绝对值，所以 $\mathrm{PRESS}_p\ge\mathrm{SSE}_p$。模型中噪声很大时，可能有 $\mathrm{PRESS}_p>\mathrm{SSTO}$，$R_{\mathrm{pred}}^2$ 为负；调整的 $R^2$ 在 $\mathrm{SSE}\approx\mathrm{SSTO}$ 时也可能为负。若 $R_{\mathrm{pred}}^2\ll R^2$，即使变量在统计上显著，模型也很可能过拟合了。例如，对 $12$ 个点拟合的一个三次多项式，$R^2=0.66$，$R_a^2=0.54$，每一项在 $0.05$ 水平下都显著，而 $R_{\mathrm{pred}}^2\approx0$：曲线紧贴少数几个极端点，一旦把它们留出，就预测得很差。

### 11.2.5. 实例：外科病房

**例 11.2.1（外科病房）** 对 $n=54$ 名接受肝脏手术的病人，响应是生存时间，候选解释变量包括凝血评分、预后指数、酶功能测试得分和肝功能测试得分（另外四个变量——年龄、性别和两个饮酒示性变量——这里暂不考虑）。生存时间严重右偏，取对数 lsurv 能缩短长长的右尾并稳定残差的方差，所以用它作响应。lsurv 与四项得分的相关系数为 $0.25$、$0.47$、$0.65$、$0.65$；得分之间最大的相关系数为 $0.50$（凝血与肝功能）。

饮酒有三个类别（不饮、适量、大量）。它通过两个示性变量 alcmod 和 alcheavy 进入模型，以"不饮"为基准。若用一个编码为 $-1,0,1$ 或 $1,2,3$ 的变量，会强行把三个类别放在等间距的位置上，并假定作用对编码是线性的；而示性变量允许各类别之间有任意的差异。

```r
library(leaps)
predictors <- a1[, c("blood", "prog", "enz", "liver")]
leapSet <- leaps(x = predictors, y = a1$lsurv, nbest = 3, method = "Cp")
leapSet$which[which.min(leapSet$Cp), ]           # TRUE TRUE TRUE FALSE
fit <- lm(lsurv ~ blood + prog + enz, data = a1)
extractAIC(fit)                                  # n log(SSE/n) + 2p
extractAIC(fit, k = log(nrow(a1)))               # BIC
regsubsets(x = predictors, y = a1$lsurv, nbest = 3)   # also forward/backward
```

每种大小下最好的三个模型为

| $p-1$ | 变量 | $R_p^2$ | $C_p$ | $\mathrm{AIC}_p$ | $\mathrm{BIC}_p$ |
|---|---|---|---|---|---|
| $1$ | enz | $0.428$ | $66.5$ | $-103.8$ | $-99.8$ |
| $1$ | liver | $0.422$ | $67.7$ | $-103.3$ | $-99.3$ |
| $1$ | prog | $0.221$ | $108.6$ | $-87.2$ | $-83.2$ |
| $2$ | prog、enz | $0.663$ | $20.5$ | $-130.5$ | $-124.5$ |
| $2$ | enz、liver | $0.600$ | $33.5$ | $-121.1$ | $-115.1$ |
| $2$ | blood、enz | $0.549$ | $43.9$ | $-114.7$ | $-108.7$ |
| $3$ | blood、prog、enz | $0.757$ | $3.4$ | $-146.2$ | $-138.2$ |
| $3$ | prog、enz、liver | $0.718$ | $11.4$ | $-138.0$ | $-130.1$ |
| $3$ | blood、enz、liver | $0.612$ | $32.9$ | $-120.8$ | $-112.9$ |
| $4$ | 全部四个 | $0.759$ | $5.0$ | $-144.6$ | $-134.6$ |

三个准则都选 blood、prog、enz：$C_p=3.4$ 接近 $p=4$，AIC 与 BIC 都最小；再加入 liver，$R^2$ 只从 $0.757$ 升到 $0.759$。（`regsubsets` 的 `plot()` 方法取 `scale = "Cp"` 时只是按 $C_p$ 排列模型，不管其值好坏。）当几个大小相同的模型给出近似相同的预测时，应由专业知识来决定；若以预测为主要目的，选哪个关系不大。不同的准则常常偏好不同的预测变量集合，所以最优子集回归最好用作筛选工具。

## 11.3. 多元回归的诊断

"当一切已知原因的作用都被精确地估计并扣除之后，剩下的事实总是以全新现象的面目出现。"（John Herschel）[3.3.8](/3.3.8) 的残差图仍是第一道检查；多元回归还需要一些工具，用来判断每个解释变量的形式、离群的响应和解释变量取值、强影响个体以及多重共线性。

**例 11.3.1（人寿保险）** 对 $n=18$ 名经理，$Y$ 是所买人寿保险的金额，$X_1$ 是平均年收入，$X_2$ 是风险厌恶得分。一阶模型给出 $\hat Y=-205.72+6.288X_1+4.738X_2$，$t$ 分别为 $30.8$ 与 $3.44$，$R^2=0.986$，$s=12.66$（自由度 $15$）。通常的残差图乍看没有明显问题；下面的工具会揭示更多。

### 11.3.1. 附加变量图

**定义 11.3.1（附加变量图）** $X_k$ 的**附加变量图**（偏回归图）是把 $Y$ 对其他解释变量回归的残差 $Y\mid X_{-k}$，对 $X_k$ 对其他解释变量回归的残差 $X_k\mid X_{-k}$ 所作的散点图。每个 $X_k$ 各有一幅（程序包 car 中的 `avPlots()`）。

由 [3.3.9](/3.3.9) 的 Frisch–Waugh–Lovell 定理，图中的最小二乘直线斜率为 $b_k$，残差与完全模型的残差相同，其 $R^2$ 是偏决定系数。所以这幅图显示 $Y$ 与 $X_k$ 在完全模型中边际关系的强弱，并能揭示非线性关系、方差不齐和离群值——这一切都是在对其他变量调整之后。残差对各 $X_k$ 的图也有用，但它没有针对其他变量对响应做调整。

![一组模拟人寿保险数据的附加变量图，其中收入的真实作用是二次的：收入的图在拟合直线周围呈现明显的弯曲，风险厌恶的图则是带有散布的线性趋势](./plots/added-variable-plots.py)

在例 11.3.1 中，收入的附加变量图呈曲线关系，残差对收入的图也是如此。加入 $X_1^2$ 项后，$\mathrm{SSE}$ 从 $2405.15$ 降到 $75.06$（$F^*=434.6$，自由度 $(1,14)$）：模型需要收入的曲率项。

### 11.3.2. 离群的响应：学生化删除残差

残差 $\boldsymbol{e}=(I_n-H)\boldsymbol{Y}$ 满足 $\operatorname{Cov}(\boldsymbol{e})=\sigma^2(I_n-H)$，故 $\operatorname{Var}(e_i)=\sigma^2(1-h_{ii})$：各残差的方差不等，$h_{ii}$ 大的个体残差方差小。

**定义 11.3.2（学生化残差与删除残差）** 内学生化的**学生化残差**为 $e_i^*=e_i/\sqrt{\mathrm{MSE}(1-h_{ii})}$。**删除残差**为 $d_i=Y_i-\hat Y_{i(-i)}$，即用不含个体 $i$ 的拟合预测 $Y_i$ 的误差；**学生化删除残差**（外学生化残差）为

$$
t_i=\frac{d_i}{s(d_i)}=\frac{e_i}{\sqrt{\mathrm{MSE}_{(-i)}(1-h_{ii})}},
$$
其中 $\mathrm{MSE}_{(-i)}$ 是不含个体 $i$ 的拟合的均方误差，$s^2(d_i)=\mathrm{MSE}_{(-i)}/(1-h_{ii})$。

由定理 11.2.2，$d_i=e_i/(1-h_{ii})$，所以 $\operatorname{Var}(d_i)=\sigma^2/(1-h_{ii})$，这给出 $t_i$ 的第二个表达式。等价地，$1/(1-h_{ii})=1+\boldsymbol{x}_i^{\mathsf T}\big(X_{(-i)}^{\mathsf T}X_{(-i)}\big)^{-1}\boldsymbol{x}_i$（在 $\big(X_{(-i)}^{\mathsf T}X_{(-i)}\big)^{-1}$ 的 Sherman–Morrison 表达式两边左乘、右乘 $\boldsymbol{x}_i$），所以 $t_i=\big(Y_i-\hat Y_{i(-i)}\big)\big/\sqrt{\mathrm{MSE}_{(-i)}\big(1+\boldsymbol{x}_i^{\mathsf T}(X_{(-i)}^{\mathsf T}X_{(-i)})^{-1}\boldsymbol{x}_i\big)}$ 就是用其余 $n-1$ 个个体预测 $\boldsymbol{x}_i$ 处一个新观测的标准化误差（[3.3.8](/3.3.8)）。

**定理 11.3.1** 在正态线性模型下，

$$
(n-p)\,\mathrm{MSE}=(n-p-1)\,\mathrm{MSE}_{(-i)}+\frac{e_i^2}{1-h_{ii}},
$$
所以 $t_i=e_i\Big(\dfrac{n-p-1}{\mathrm{SSE}(1-h_{ii})-e_i^2}\Big)^{1/2}$ 只需一次拟合就能算出，且 $t_i\sim t_{n-p-1}$。

**证明** 在模型中加入个体 $i$ 的示性向量 $\boldsymbol{u}_i$（$\mathbb{R}^n$ 的第 $i$ 个标准基向量），$\boldsymbol{Y}=X\boldsymbol{\beta}+\gamma\boldsymbol{u}_i+\boldsymbol{\varepsilon}$。这个均值漂移模型恰好拟合个体 $i$，所以它的误差平方和就是其余 $n-1$ 个个体的误差平方和 $(n-p-1)\mathrm{MSE}_{(-i)}$，且 $\hat\gamma=Y_i-\hat Y_{i(-i)}=d_i$。与 [3.3.9](/3.3.9) 中命题 9.2.1 的证明一样，令 $\tilde{\boldsymbol{u}}=(I_n-H)\boldsymbol{u}_i$，则 $\tilde{\boldsymbol{u}}^{\mathsf T}\tilde{\boldsymbol{u}}=1-h_{ii}$，$\tilde{\boldsymbol{u}}^{\mathsf T}\boldsymbol{Y}=e_i$，所以 $\boldsymbol{u}_i$ 的额外平方和为 $e_i^2/(1-h_{ii})$，这就是所述恒等式。此外，$t_i$ 恰好是均值漂移模型中 $\hat\gamma$ 的 $t$ 统计量，该模型有 $n-p-1$ 个误差自由度；若个体 $i$ 服从模型，则 $\gamma=0$，由 [3.3.8](/3.3.8) 的定理 8.2.2 得 $t_i\sim t_{n-p-1}$。$\square$

增加一个个体会使 $\mathrm{SSE}$ 增大，这与增加一个变量会使 $\mathrm{SSE}$ 减小不同。检验离群值时，若 $\lvert t_i\rvert>t_{n-p-1,\alpha/(2n)}$，就判定个体 $i$ 的 $Y$ 值离群。由于要检验全部 $n$ 个个体，这里用了 **Bonferroni 校正**。

在例 11.3.1 中，`rstudent()` 给出的最大值为 $t_7=2.75$（MASS 的 `stdres()` 给出 $e_7^*=2.29$）。Bonferroni 临界值为 $t_{14,0.05/36}=3.62$；car 的 `outlierTest()` 报告未调整的 $p$ 值 $0.016$ 和 Bonferroni $p$ 值 $0.28$：没有个体在 $Y$ 上显著离群。

离群值不一定是坏的观测。如果它们是正确的，反而可能是数据中信息最多的点：在指数增长的数据中，最后两个观测相对于直线看似离群，实际上却揭示了增长的真实形式。为保护某个理论而删去不合意的点，或者把不喜欢的回答定义为离群值，都是不良的做法。

### 11.3.3. 解释变量的离群取值：杠杆值

**定义 11.3.3（杠杆值）** 个体 $i$ 的**杠杆值**是**帽子矩阵**的对角元 $h_{ii}=\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i$；由于 $\hat Y_i=h_{i1}Y_1+\cdots+h_{ii}Y_i+\cdots+h_{in}Y_n$，它是 $Y_i$ 在其自身拟合值中的权重。

杠杆值满足 $0\le h_{ii}\le1$，$\sum_{i=1}^nh_{ii}=\operatorname{tr}(H)=\operatorname{rank}(H)=p$，所以平均值为 $\bar h=p/n$。模型含截距时，

$$
h_{ii}=\frac1n+(\tilde{\boldsymbol{x}}_i)^{\mathsf T}(\tilde X^{\mathsf T}\tilde X)^{-1}\tilde{\boldsymbol{x}}_i,
$$
其中 $\tilde X$ 是中心化的解释变量构成的矩阵，$\tilde{\boldsymbol{x}}_i^{\mathsf T}$ 是它的第 $i$ 行：$h_{ii}$ 以样本协方差矩阵为度量，衡量个体 $i$ 的 $X$ 值离其均值有多远。通常当 $h_{ii}>2p/n$ 时判定个体的 $X$ 值异常；杠杆值在 $0.2$ 到 $0.5$ 之间为中等，超过 $0.5$ 为高。同一个量 $\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h$ 在新点处还能检测隐蔽外推（[3.3.8](/3.3.8)）：若它远超出数据的杠杆值范围，则在 $\boldsymbol{x}_h$ 处的预测就是外推。

在例 11.3.1 中，$2p/n=6/18=0.33$；`hatvalues()` 给出 $h_{77}=0.62$，杠杆值高，$h_{66}=0.35$，刚刚超过界限。其余杠杆值都低于 $0.30$。

### 11.3.4. 强影响个体

若删去一个个体会使拟合的回归发生重大变化，就称它是有影响的。杠杆值小的 $Y$ 离群值，或与其他个体模式一致的高杠杆个体，不一定有影响；残差大且杠杆值高的个体通常有影响。三种度量分别量化对拟合的不同部分的影响。

**定义 11.3.4（DFFITS、Cook 距离、DFBETAS）** 对个体 $i$，

1. **DFFITS** 是有无个体 $i$ 时个体 $i$ 的拟合值之差的学生化形式，

$$
(\mathrm{DFFITS})_i=\frac{\hat Y_i-\hat Y_{i(-i)}}{\sqrt{\mathrm{MSE}_{(-i)}h_{ii}}};
$$
2. **Cook 距离**是全部 $n$ 个拟合值的总体变化，

$$
D_i=\frac{\big\|X(\boldsymbol{b}-\boldsymbol{b}_{(-i)})\big\|^2}{p\,\mathrm{MSE}}=\frac{\sum_{j=1}^n\big(\hat Y_j-\hat Y_{j(-i)}\big)^2}{p\,\mathrm{MSE}};
$$
3. **DFBETAS** 度量每个系数的变化，$(\mathrm{DFBETAS})_{k(-i)}=\dfrac{b_k-b_{k(-i)}}{\sqrt{\mathrm{MSE}_{(-i)}c_{kk}}}$，$k=0,1,\dots,p-1$，其中 $c_{kk}=[(X^{\mathsf T}X)^{-1}]_{kk}$，从而 $\operatorname{Var}(b_k)=\sigma^2c_{kk}$。

Cook 距离的名称来自 $\boldsymbol{\beta}$ 的置信域。由于 $(\boldsymbol{b}-\boldsymbol{\beta})^{\mathsf T}X^{\mathsf T}X(\boldsymbol{b}-\boldsymbol{\beta})/\sigma^2\sim\chi^2_p$，$100(1-\alpha)\%$ 置信椭球（[3.2.4](/3.2.4)）为 $\big\{\boldsymbol{\beta}\in\mathbb{R}^p\colon\|X(\boldsymbol{\beta}-\boldsymbol{b})\|^2/(p\,\mathrm{MSE})\le F_{p,n-p,\alpha}\big\}$，以 $\boldsymbol{b}$ 为中心，轴由 $X^{\mathsf T}X$ 的特征向量和特征值决定。Cook（1977）用 $\boldsymbol{b}$ 与 $\boldsymbol{b}_{(-i)}$ 之间同样的距离度量个体 $i$ 的影响。

**命题 11.3.1** 用残差、杠杆值和 $t_i$ 表示，

$$
(\mathrm{DFFITS})_i=t_i\sqrt{\frac{h_{ii}}{1-h_{ii}}},\qquad D_i=\frac{e_i^2}{p\,\mathrm{MSE}}\cdot\frac{h_{ii}}{(1-h_{ii})^2}=\frac{(e_i^*)^2}{p}\cdot\frac{h_{ii}}{1-h_{ii}}.
$$

**证明** 由定理 11.2.2，$\hat Y_i-\hat Y_{i(-i)}=\boldsymbol{x}_i^{\mathsf T}(\boldsymbol{b}-\boldsymbol{b}_{(-i)})=h_{ii}e_i/(1-h_{ii})$；除以 $\sqrt{\mathrm{MSE}_{(-i)}h_{ii}}$ 得 $\frac{e_i}{\sqrt{\mathrm{MSE}_{(-i)}(1-h_{ii})}}\sqrt{\frac{h_{ii}}{1-h_{ii}}}$。对 Cook 距离，$\|X(\boldsymbol{b}-\boldsymbol{b}_{(-i)})\|^2=\frac{e_i^2}{(1-h_{ii})^2}\boldsymbol{x}_i^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}X(X^{\mathsf T}X)^{-1}\boldsymbol{x}_i=\frac{e_i^2h_{ii}}{(1-h_{ii})^2}$。$\square$

这些公式表明，影响是大残差与高杠杆值的结合。常用的准则为：

| 度量 | 度量的对象 | 判定为强影响的条件 |
|---|---|---|
| $(\mathrm{DFFITS})_i$ | 自身拟合值的变化 | $\lvert\mathrm{DFFITS}\rvert>1$（中小数据），$>2\sqrt{p/n}$（大数据） |
| $D_i$ | 全部拟合值的变化 | $D_i>4/n$；或看百分位 $\nu=\mathbb{P}(F_{p,n-p}<D_i)$：$\nu<20\%$ 影响很小，$\nu\ge50\%$ 影响显著 |
| $(\mathrm{DFBETAS})_{k(-i)}$ | 每个系数的变化 | $\lvert\mathrm{DFBETAS}\rvert>1$（中小数据），$>2/\sqrt{n}$（大数据） |

![一组模拟数据的影响诊断，其中一个个体的 X 值极端且残差大：散点图显示删去这个个体后拟合直线明显改变，Cook 距离的序号图把它单独挑了出来，远高于界限 4/n](./plots/influence-diagnostics.py)

```r
round(hatvalues(lmfit1), 4)          # leverages h_ii
round(rstudent(lmfit1), 4)           # studentized deleted residuals t_i
round(cooks.distance(lmfit1), 4)     # Cook's distances D_i
dfbetas(lmfit1)                      # DFBETAS for every case and coefficient
plot(lmfit1, which = 4)              # index plot of Cook's distances
plot(lmfit1, which = 5)              # residuals against leverage with Cook contours
```

在例 11.3.1 中，个体 7 的 $D_7=2.89$，位于 $F_{3,15}$ 的第 $93$ 百分位，远高于其他所有个体（其次是 $0.35$ 和 $0.20$）；它的 DFFITS 为 $2.75\sqrt{0.62/0.38}=3.53$，对收入和风险厌恶的 DFBETAS 分别为 $2.66$ 和 $-2.68$。个体 7 是强影响点，尽管按 Bonferroni 检验它不是离群值。

识别出离群和强影响的个体之后怎么办？应当查明它们*为什么*离群或有影响。根据查明的情况，可以采取的措施包括：改正数据中的错误；删去这些个体或降低其权重（稳健回归，[3.3.12](/3.3.12)）；变换数据；考虑另一个模型（这里是加入收入的曲率项）；重新设计试验或抽样调查，收集更多数据。

### 11.3.5. 多重共线性：方差膨胀因子

[3.3.10](/3.3.10) 的两两相关系数可能漏掉涉及多个变量的多重共线性。一个直接的度量是每个解释变量能被其他变量解释的程度。

**定义 11.3.5（方差膨胀因子）** 设 $R_k^2$ 是 $X_k$ 对其他 $p-2$ 个解释变量回归的决定系数。$X_k$ 的**方差膨胀因子**为 $(\mathrm{VIF})_k=(1-R_k^2)^{-1}$，其**容许度**为 $\mathrm{TOL}_k=1-R_k^2=1/(\mathrm{VIF})_k$。

**定理 11.3.2** 在 [3.3.9](/3.3.9) 的标准化回归模型中，$\operatorname{Var}(b_k^*)=\sigma^{*2}(\mathrm{VIF})_k$，其中 $\sigma^{*2}$ 是该模型的误差方差；在原模型中，

$$
\operatorname{Var}(b_k)=\frac{\sigma^2}{\sum_i(X_{ik}-\bar X_k)^2}\cdot(\mathrm{VIF})_k.
$$

**证明** $\operatorname{Cov}(\boldsymbol{b}^*)=\sigma^{*2}r_{XX}^{-1}$，所以要求 $[r_{XX}^{-1}]_{kk}$；取 $k=1$，把 $r_{XX}$ 分块为 $\begin{bmatrix}1&\boldsymbol{r}_{1,-1}^{\mathsf T}\\\boldsymbol{r}_{1,-1}&r_{-1,-1}\end{bmatrix}$，其中 $r_{-1,-1}$ 是 $X_2,\dots,X_{p-1}$ 的相关矩阵，$\boldsymbol{r}_{1,-1}$ 是它们与 $X_1$ 的相关系数。由利用 **Schur 补**的分块求逆公式，

$$
[r_{XX}^{-1}]_{11}=\big(1-\boldsymbol{r}_{1,-1}^{\mathsf T}r_{-1,-1}^{-1}\boldsymbol{r}_{1,-1}\big)^{-1}.
$$
在 $X_1^*$ 对 $X_2^*,\dots,X_{p-1}^*$ 的标准化回归中，系数为 $\boldsymbol{\beta}_{1,-1}=r_{-1,-1}^{-1}\boldsymbol{r}_{1,-1}$，总平方和为 $1$，回归平方和为 $\boldsymbol{\beta}_{1,-1}^{\mathsf T}r_{-1,-1}\boldsymbol{\beta}_{1,-1}=\boldsymbol{r}_{1,-1}^{\mathsf T}r_{-1,-1}^{-1}\boldsymbol{r}_{1,-1}$，因此它就是 $R_1^2$。于是 $[r_{XX}^{-1}]_{11}=(1-R_1^2)^{-1}$。由 $b_k=(s_Y/s_k)b_k^*$ 与 $\sigma^{*2}=\sigma^2/\big((n-1)s_Y^2\big)$ 即得第二个公式。$\square$

所以 $(\mathrm{VIF})_k$ 恰好是与正交设计（[3.3.10](/3.3.10) 的命题 10.1.1）相比，共线性使 $b_k$ 的方差膨胀的倍数。记 $\overline{\mathrm{VIF}}=\sum_{k=1}^{p-1}(\mathrm{VIF})_k/(p-1)$；当最大的 $\mathrm{VIF}$ 超过 $10$，或平均 $\mathrm{VIF}$ 显著大于 $1$ 时，认为多重共线性过强。在例 11.3.1 中，car 的 `vif()` 给出收入和风险厌恶的值都是 $1.07$：没有问题。对体脂数据，VIF 为 $709$（皮褶）、$564$（大腿）和 $105$（上臂），证实了 [3.3.10](/3.3.10) 中严重的多重共线性（上臂对另外两个变量回归的 $R^2=0.990$）。

## 小结

| 准则 | 公式 | 选择 |
|---|---|---|
| $R_p^2$ | $1-\mathrm{SSE}_p/\mathrm{SSTO}$ | 增长趋于平缓处 |
| $R_{a,p}^2$ | $1-\frac{n-1}{n-p}\cdot\frac{\mathrm{SSE}_p}{\mathrm{SSTO}}$ | 最大（$\mathrm{MSE}_p$ 最小） |
| Mallows $C_p$ | $\mathrm{SSE}_p/\mathrm{MSE}_P-(n-2p)$ | 小，且 $C_p\approx p$ |
| $\mathrm{AIC}_p$、$\mathrm{BIC}_p$ | $n\ln(\mathrm{SSE}_p/n)+2p$，$+p\ln n$ | 最小 |
| $\mathrm{PRESS}_p$、$R_{\mathrm{pred}}^2$ | $\sum_i\big(e_i/(1-h_{ii})\big)^2$，$1-\mathrm{PRESS}_p/\mathrm{SSTO}$ | PRESS 最小；警惕 $R_{\mathrm{pred}}^2\ll R^2$ |

| 问题 | 诊断工具 | 经验准则 |
|---|---|---|
| $X_k$ 的形式 | 附加变量图 | 弯曲、散布不均、离群值 |
| $Y$ 离群 | $t_i=e_i/\sqrt{\mathrm{MSE}_{(-i)}(1-h_{ii})}\sim t_{n-p-1}$ | $\lvert t_i\rvert>t_{n-p-1,\alpha/(2n)}$ |
| $X$ 离群 | $h_{ii}$ | $h_{ii}>2p/n$；$>0.5$ 为高 |
| 影响 | DFFITS、Cook 距离 $D_i$、DFBETAS | $>1$（或 $2\sqrt{p/n}$）、$>4/n$、$>1$（或 $2/\sqrt n$） |
| 多重共线性 | $(\mathrm{VIF})_k=(1-R_k^2)^{-1}$ | 最大值 $>10$ |

- 建立模型：纳入全部重要的候选变量，用最优子集或逐步搜索选择，用准则或交叉验证评判，在新数据或留出数据上核实；既要避免欠拟合（偏差），也要避免过拟合（方差）。
- 一个恒等式驱动了全部留一诊断：$\boldsymbol{b}-\boldsymbol{b}_{(-i)}=(X^{\mathsf T}X)^{-1}\boldsymbol{x}_ie_i/(1-h_{ii})$，$Y_i-\hat Y_{i(-i)}=e_i/(1-h_{ii})$。
