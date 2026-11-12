---
title: 完全随机化实验的回归方法
description: 以线性回归估计完全随机化实验中的平均处理效应。无协变量时，OLS 估计量就是均值差，其因果含义来自随机化，稳健标准误重现 Neyman 方差估计；有协变量时，即使模型有误，总体系数也等于超总体平均效应，估计量渐近正态，且在协变量能预测结果时更精确；交互项、效应异质性的检验，以及 LRC-CPPT 胆固醇数据。
source_hash: 658caf5c1f47
---

[3.9.4](/3.9.4) 中 Neyman 的分析只使用处理指示变量与结果。多数实验还会记录处理前变量，这些变量若能预测结果，就含有均值差所丢弃的信息。线性回归是利用它们最常用的方法：把观测结果对处理指示变量和协变量作回归，读出处理的系数。回归本身只描述关联，任何数据集都可以做回归。然而在**完全随机化实验**中，随机化赋予回归系数因果含义，而且不要求线性模型成立。本章把这一论断讲精确。全章中，单元是来自**超总体**的随机样本，所以估计目标是 $\tau_{\mathrm{sp}}$，期望 $\mathbb{E}_{\mathrm{sp}}$ 与方差 $\operatorname{Var}_{\mathrm{sp}}$ 同时对单元的抽样与分配取（[3.9.4](/3.9.4)）。回归的结果是大样本结果，不同于 Fisher 与 Neyman 的精确有限样本结果。最小二乘的矩阵形式与稳健方差估计取自 [3.3.7](/3.3.7) 与 [3.3.12](/3.3.12)；[3.9.7](/3.9.7) 的分层设计与 [3.9.10](/3.9.10) 的观察性研究沿用同样的回归论证。

## 5.1. 设定

### 5.1.1. 协变量能有帮助吗？

由定理 4.3.1，CRE 中**均值差估计量**的抽样方差为

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{S_{\mathrm{tc}}^2}{N},
$$
其中 $S_{\mathrm{c}}^2$ 与 $S_{\mathrm{t}}^2$ 是 $Y_i(0)$ 与 $Y_i(1)$ 的有限总体方差，$S_{\mathrm{tc}}^2$ 是单元效应的有限总体方差。起主导作用的项是潜在结果的方差。协变量只有解释了结果的一部分变异，才能降低它们。两种极端情形说明了可能的范围：

- 协变量与潜在结果独立：它不含关于潜在结果的信息，对它作调整只会增加噪声；
- 协变量与潜在结果强相关，因而也与 $Y_i^{\mathrm{obs}}$ 强相关：比较协变量取值相近的处理与对照单元，可以去掉结果的大部分变异，使效应估计得更精确。

对 CRE 的四种方法回答不同的问题：

| 方法 | 问题 | 章节 |
|---|---|---|
| Fisher 精确 p 值 | 是否存在非零的单元层面效应？ | [3.9.3](/3.9.3) |
| Neyman 重复抽样 | 如何估计平均效应，精度如何？ | [3.9.4](/3.9.4) |
| 回归 | 协变量如何改进平均效应的估计？ | 本章 |
| 基于模型的推断 | 潜在结果的参数模型有何帮助？ | [3.9.6](/3.9.6) |

### 5.1.2. 超总体与记号

$N$ 个单元的样本从无穷超总体中随机抽取，然后用 CRE 把其中 $N_{\mathrm{t}}$ 个分配到处理。因此被抽中单元的潜在结果是随机的，估计量的性质通过对总体重复抽样、再对分配重复来评价。协变量 $X_i$ 是 $1 \times K$ 行向量。下面用到的总体量为

$$
\begin{aligned}
&\tau_{\mathrm{sp}} = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1) - Y_i(0)\bigr], \qquad
\mu_{\mathrm{c}}(x) = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(0) \mid X_i = x\bigr], \qquad
\mu_{\mathrm{t}}(x) = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1) \mid X_i = x\bigr],\\
&\sigma_{\mathrm{c}}^2(x) = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(0) \mid X_i = x\bigr), \qquad
\sigma_{\mathrm{t}}^2(x) = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(1) \mid X_i = x\bigr), \qquad
\tau(x) = \mu_{\mathrm{t}}(x) - \mu_{\mathrm{c}}(x),\\
&\mu_{\mathrm{c}} = \mathbb{E}_{\mathrm{sp}}[\mu_{\mathrm{c}}(X_i)], \qquad
\sigma_{\mathrm{c}}^2 = \mathbb{E}_{\mathrm{sp}}\bigl[\sigma_{\mathrm{c}}^2(X_i)\bigr] + \operatorname{Var}_{\mathrm{sp}}\bigl(\mu_{\mathrm{c}}(X_i)\bigr) \quad (\text{t 的情形同理}),\\
&\mu_X = \mathbb{E}_{\mathrm{sp}}[X_i], \qquad
\Omega_X = \operatorname{Var}_{\mathrm{sp}}(X_i) = \mathbb{E}_{\mathrm{sp}}\bigl[(X_i - \mu_X)^{\mathsf T}(X_i - \mu_X)\bigr].
\end{aligned}
$$
$\sigma_{\mathrm{c}}^2$ 的分解就是全方差公式（[3.1.9](/3.1.9)）；其第二项是协变量能够解释的那部分结果方差。在大样本的陈述中，$p = \lim_{N \to \infty} N_{\mathrm{t}}/N \in (0, 1)$ 是处理单元所占的极限比例。在超总体中，CRE 使随机抽取的单元的处理指示变量与该单元的其余一切独立：$W_i \perp \bigl(Y_i(0), Y_i(1), X_i\bigr)$，$\mathbb{P}(W_i = 1) = N_{\mathrm{t}}/N$。下面只用到设计的这一性质。

### 5.1.3. LRC-CPPT 胆固醇数据

脂质研究诊所冠心病一级预防试验（LRC-CPPT）是一项随机双盲试验，研究降胆固醇药物考来烯胺（cholestyramine）对高胆固醇男性的作用。这里分析的子样本由 Efron 与 Feldman（1991）研究，含 $N = 337$ 名男性，其中 $N_{\mathrm{c}} = 172$ 人被分配到安慰剂，$N_{\mathrm{t}} = 165$ 人被分配到药物。安慰剂使两组之间只有药物本身不同：没有安慰剂，知道自己接受了处理这件事本身可能改变饮食、运动等同样影响胆固醇的行为，比较衡量的就是整套做法的效应，而不是药物的效应。

| 变量 | 时间 | 对照组均值（标准差） | 处理组均值（标准差） |
|---|---|---|---|
| `chol1`：胆固醇，第一次处理前测量 | 处理前 | 297.1 (23.1) | 297.0 (20.4) |
| `chol2`：胆固醇，第二次处理前测量 | 处理前 | 289.2 (24.1) | 287.4 (21.4) |
| `cholp`：处理前综合水平 | 处理前 | 291.2 (23.2) | 289.9 (20.4) |
| `cholf`：处理后胆固醇（结果） | 处理后 | 282.7 (24.9) | 256.5 (26.2) |
| `chold` $=$ `cholf` $-$ `cholp` | 处理后 | $-8.5$ (10.8) | $-33.4$ (21.3) |
| `comp`：服用处方剂量的百分比 | 处理后 | 74.5 (21.0) | 59.9 (24.4) |

结果为 $Y = $ `cholf`，处理 $W$ 是被分配到药物，处理前的测量值是协变量 $X$。如随机化所保证的，它们在两组间是平衡的，并且对结果有很强的预测力：对照组中变化量 `chold` 的标准差不到 `cholf` 的一半。依从变量 `comp` 在分配之后测量，且两组不同；5.3.8 节解释为什么不能把它用作协变量。

## 5.2. 无协变量的回归

### 5.2.1. 估计量

考虑回归模型

$$
Y_i^{\mathrm{obs}} = \alpha + \tau W_i + \varepsilon_i,
$$
及最小二乘估计量 $(\hat\alpha^{\mathrm{ols}}, \hat\tau^{\mathrm{ols}}) = \arg\min_{\alpha, \tau}\sum_{i=1}^{N}\bigl(Y_i^{\mathrm{obs}} - \alpha - \tau W_i\bigr)^2$。

**定理 5.2.1** 最小二乘估计量为

$$
\hat\tau^{\mathrm{ols}} = \frac{\sum_{i=1}^{N}(W_i - \bar W)(Y_i^{\mathrm{obs}} - \bar Y^{\mathrm{obs}})}{\sum_{i=1}^{N}(W_i - \bar W)^2} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = \hat\tau^{\mathrm{dif}}, \qquad
\hat\alpha^{\mathrm{ols}} = \bar Y_{\mathrm{c}}^{\mathrm{obs}},
$$
其中 $\bar W = N_{\mathrm{t}}/N$。

**证明** 第一个等号是简单线性回归的斜率公式。因为 $W_i^2 = W_i$，分母为 $\sum_i W_i - N\bar W^2 = N_{\mathrm{t}} - N_{\mathrm{t}}^2/N = N_{\mathrm{t}}N_{\mathrm{c}}/N$。分子为 $\sum_i W_iY_i^{\mathrm{obs}} - N\bar W\bar Y^{\mathrm{obs}} = N_{\mathrm{t}}\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \frac{N_{\mathrm{t}}}{N}\bigl(N_{\mathrm{t}}\bar Y_{\mathrm{t}}^{\mathrm{obs}} + N_{\mathrm{c}}\bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)$。相除得 $\hat\tau^{\mathrm{ols}} = \hat\tau^{\mathrm{dif}}$，而 $\hat\alpha^{\mathrm{ols}} = \bar Y^{\mathrm{obs}} - \hat\tau^{\mathrm{ols}}\bar W = \bar Y_{\mathrm{c}}^{\mathrm{obs}}$。$\square$

只含一个二值回归变量的回归恰好重现 Neyman 估计量，因此在 CRE 中，$\hat\tau^{\mathrm{ols}}$ 对分配而言是 $\tau_{\mathrm{fs}}$ 的无偏估计，对抽样与分配而言是 $\tau_{\mathrm{sp}}$ 的无偏估计（定理 4.2.1 与 4.6.1）。

### 5.2.2. 因果解释

回归的系数与误差项可以直接用潜在结果来定义。设 $\mu_{\mathrm{c}} = \mathbb{E}_{\mathrm{sp}}[Y_i(0)]$，$\mu_{\mathrm{t}} = \mathbb{E}_{\mathrm{sp}}[Y_i(1)]$，并令

$$
\alpha = \mu_{\mathrm{c}}, \qquad \tau = \mu_{\mathrm{t}} - \mu_{\mathrm{c}} = \tau_{\mathrm{sp}}, \qquad
\varepsilon_i = \begin{cases} Y_i(0) - \mu_{\mathrm{c}}, & W_i = 0,\\ Y_i(1) - \mu_{\mathrm{t}}, & W_i = 1. \end{cases}
$$
于是对每个单元，$Y_i^{\mathrm{obs}} = \alpha + \tau W_i + \varepsilon_i$ 按构造成立：它是恒等式，不是模型。实质在于误差的性质。由于 CRE 中 $W_i$ 与 $(Y_i(0), Y_i(1))$ 独立，

$$
\mathbb{E}_{\mathrm{sp}}[\varepsilon_i \mid W_i = 1] = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1) - \mu_{\mathrm{t}} \bigm| W_i = 1\bigr] = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1)\bigr] - \mu_{\mathrm{t}} = 0,
$$
同理 $\mathbb{E}_{\mathrm{sp}}[\varepsilon_i \mid W_i = 0] = 0$。条件方差为

$$
\operatorname{Var}_{\mathrm{sp}}(\varepsilon_i \mid W_i) = \sigma_{\mathrm{t}}^2 W_i + \sigma_{\mathrm{c}}^2(1 - W_i).
$$
通常的回归条件 $\mathbb{E}[\varepsilon_i \mid W_i] = 0$，在观察性分析中是可能失效的假定，在这里却是随机化的推论。这就是从关联陈述到因果陈述的一步：$Y^{\mathrm{obs}}$ 对 $W$ 的总体回归系数在任何数据集中都等于 $\mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 1] - \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 0]$，只有凭借 CRE，它才等于 $\mathbb{E}_{\mathrm{sp}}[Y_i(1)] - \mathbb{E}_{\mathrm{sp}}[Y_i(0)] = \tau_{\mathrm{sp}}$。各单元是独立同分布的抽样，所以线性模型的标准正则条件成立，关于 $(\alpha, \tau)$ 的全部推断理论都适用，唯一需要注意的是两组的误差方差可以不同。

### 5.2.3. 推断

把单元堆叠起来，前 $N_{\mathrm{c}}$ 个是对照。用 [3.3.7](/3.3.7) 的矩阵记号，$\boldsymbol{Y}^{\mathrm{obs}} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$，$\boldsymbol{\beta} = (\alpha, \tau)^{\mathsf T}$，且

$$
X = \begin{bmatrix} \boldsymbol{1}_{N_{\mathrm{c}}} & \boldsymbol{0}_{N_{\mathrm{c}}} \\ \boldsymbol{1}_{N_{\mathrm{t}}} & \boldsymbol{1}_{N_{\mathrm{t}}} \end{bmatrix}, \qquad
\mathbb{E}_{\mathrm{sp}}[\boldsymbol{\varepsilon} \mid X] = \boldsymbol{0}, \qquad
\operatorname{Var}_{\mathrm{sp}}(\boldsymbol{\varepsilon} \mid X) = \Sigma = \operatorname{diag}\bigl(\sigma_{\mathrm{c}}^2\boldsymbol{1}_{N_{\mathrm{c}}}^{\mathsf T}, \sigma_{\mathrm{t}}^2\boldsymbol{1}_{N_{\mathrm{t}}}^{\mathsf T}\bigr).
$$
估计量为 $\hat{\boldsymbol{\beta}} = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}^{\mathrm{obs}} = \boldsymbol{\beta} + H\boldsymbol{\varepsilon}$，其中 $H = (X^{\mathsf T}X)^{-1}X^{\mathsf T}$ 的两行为 $\bigl(\boldsymbol{1}_{N_{\mathrm{c}}}^{\mathsf T}/N_{\mathrm{c}},\ \boldsymbol{0}^{\mathsf T}\bigr)$ 与 $\bigl(-\boldsymbol{1}_{N_{\mathrm{c}}}^{\mathsf T}/N_{\mathrm{c}},\ \boldsymbol{1}_{N_{\mathrm{t}}}^{\mathsf T}/N_{\mathrm{t}}\bigr)$。故 $\operatorname{Var}_{\mathrm{sp}}(\hat{\boldsymbol{\beta}} \mid X) = H\Sigma H^{\mathsf T}$，其 $(2,2)$ 元为

$$
\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{ols}}\bigr) = \frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}}.
$$
$\hat{\boldsymbol{\beta}}$ 的每个分量都是组内独立同分布误差的平均，所以由**中心极限定理**渐近正态。两种方差估计对应关于 $\Sigma$ 的两种假定：

| 假定 | 方差估计 | 等于 | R |
|---|---|---|---|
| 同方差，$\sigma_{\mathrm{t}}^2 = \sigma_{\mathrm{c}}^2 = \sigma^2$ | $\hat\sigma^2\bigl(\frac{1}{N_{\mathrm{c}}} + \frac{1}{N_{\mathrm{t}}}\bigr)$，$\hat\sigma^2 = \frac{1}{N - 2}\sum_i \hat\varepsilon_i^2$ | [3.9.4](/3.9.4) 的 $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$ | `lm` |
| 异方差，允许 $\sigma_{\mathrm{t}}^2 \ne \sigma_{\mathrm{c}}^2$ | $\frac{\hat\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\hat\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}}$，$\hat\sigma_{\mathrm{t}}^2 = \frac{1}{N_{\mathrm{t}} - 1}\sum_{i: W_i = 1}\hat\varepsilon_i^2$ | $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$（定义 4.4.1） | `car::hccm` |

残差为：处理单元 $\hat\varepsilon_i = Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}$，对照单元 $Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$，所以 $\hat\sigma_{\mathrm{t}}^2 = s_{\mathrm{t}}^2$，$\hat\sigma_{\mathrm{c}}^2 = s_{\mathrm{c}}^2$。因此回归推断恰好重现 Neyman 的推断：常规的 OLS 标准误是在常数效应下有效的合并估计，而异方差稳健的标准误就是 Neyman 估计。

一般地，稳健估计量是 **White 估计量**（[定义 12.1.1](/3.3.12#def-12.1.1)），又称 Eicker–Huber–White 估计量或异方差一致协方差矩阵估计量，

$$
\widehat{\operatorname{Var}}\bigl(\hat{\boldsymbol{\beta}}\bigr) = (X^{\mathsf T}X)^{-1}X^{\mathsf T}\operatorname{diag}\bigl(\hat\varepsilon_1^2, \dots, \hat\varepsilon_N^2\bigr)X(X^{\mathsf T}X)^{-1},
$$
它是 $(X^{\mathsf T}X)^{-1}X^{\mathsf T}\Sigma X(X^{\mathsf T}X)^{-1}$ 的矩估计。它的有限样本修正略有不同：原始形式（HC0）给出 $\frac{N_{\mathrm{c}} - 1}{N_{\mathrm{c}}}\frac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{N_{\mathrm{t}} - 1}{N_{\mathrm{t}}}\frac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}}$；HC2 修正把 $\hat\varepsilon_i^2$ 除以 $1 - h_{ii}$（杠杆值 $h_{ii} = 1/N_{\mathrm{t}}$ 或 $1/N_{\mathrm{c}}$），恰好给出 $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$。`car::hccm` 的默认是 HC3，还要略大一些。

```r
library(car)
fit <- lm(cholf ~ W, data = lrc)              # tau-hat = difference in means
sqrt(vcov(fit)["W", "W"])                     # pooled: valid under a constant effect
sqrt(hccm(fit, type = "hc2")["W", "W"])       # robust: equals the Neyman standard error
```

### 5.2.4. 另外两种解释

*插补。* 因果推断的困难是数据缺失：每个单元都缺一个潜在结果。在无混杂性下，$\mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 0] = \mathbb{E}_{\mathrm{sp}}[Y_i(0)]$，$\mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 1] = \mathbb{E}_{\mathrm{sp}}[Y_i(1)]$，因此拟合的回归对处理单元以 $\hat Y_i(0) = \hat\alpha$、对对照单元以 $\hat Y_i(1) = \hat\alpha + \hat\tau$ 预测缺失的结果。估计的单元效应为：$W_i = 1$ 时 $\hat\tau_i = Y_i^{\mathrm{obs}} - \hat Y_i(0)$，$W_i = 0$ 时 $\hat\tau_i = \hat Y_i(1) - Y_i^{\mathrm{obs}}$，它们的平均值为

$$
\frac{1}{N}\sum_{i=1}^{N}\hat\tau_i = \frac{1}{N}\sum_{i=1}^{N}\Bigl\{W_i\bigl(Y_i^{\mathrm{obs}} - \hat Y_i(0)\bigr) + (1 - W_i)\bigl(\hat Y_i(1) - Y_i^{\mathrm{obs}}\bigr)\Bigr\} = \hat\tau^{\mathrm{ols}}.
$$
这种把回归看作一种特定插补规则的观点，在 [3.9.6](/3.9.6) 中发展成完整的方法。

*大样本极限。* 当 $N \to \infty$ 时，最小二乘估计量收敛到总体目标函数的极小点，

$$
(\alpha^*, \tau^*) = \arg\min_{\alpha, \tau}\mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \alpha - \tau W_i)^2\bigr],
$$
该问题的解为 $\tau^* = \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 1] - \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 0]$，在 CRE 中它等于 $\tau_{\mathrm{sp}}$。因此回归估计量是一个被设计赋予因果含义的总体量的**相合估计**。加入协变量后的同一论证是 5.3 节的核心。

### 5.2.5. 回归增加了什么，没有增加什么

回归方法为人熟悉，计算方便，重现了 Neyman 的结果，并且可以直接推广到协变量。另一面同样值得强调：回归可以在任何数据集上运行并总会返回一个系数；一般而言，这个系数描述的是关联。它的因果含义来自设计，而不是来自回归：在 CRE 中，是随机化使 $\mathbb{E}[\varepsilon_i \mid W_i] = 0$ 与 $\tau^* = \tau_{\mathrm{sp}}$ 成立。在观察性研究中，没有任何东西保证这一点，同样的回归可以有严重偏差（[3.9.8](/3.9.8)，[3.9.10](/3.9.10)）。

## 5.3. 含协变量的回归

### 5.3.1. 模型与总体对应量

把协变量加入回归：

$$
Y_i^{\mathrm{obs}} = \alpha + \tau W_i + X_i\boldsymbol{\beta} + \varepsilon_i, \qquad
(\hat\tau^{\mathrm{ols}}, \hat\alpha^{\mathrm{ols}}, \hat{\boldsymbol{\beta}}^{\mathrm{ols}}) = \arg\min_{\tau, \alpha, \boldsymbol{\beta}}\sum_{i=1}^{N}\bigl(Y_i^{\mathrm{obs}} - \alpha - \tau W_i - X_i\boldsymbol{\beta}\bigr)^2.
$$
用实验设计的语言，这就是**协方差分析**。与 5.2.2 节不同的是，线性模型现在可以是错的：$\mu_{\mathrm{c}}(x)$ 不必是线性的，效应 $\tau(x)$ 也不必是常数。我们不假定模型正确，而是把估计量的目标定义为总体目标函数的极小点，

$$
(\alpha^*, \tau^*, \boldsymbol{\beta}^*) = \arg\min_{\alpha, \tau, \boldsymbol{\beta}}\mathbb{E}_{\mathrm{sp}}\Bigl[\bigl(Y_i^{\mathrm{obs}} - \alpha - \tau W_i - X_i\boldsymbol{\beta}\bigr)^2\Bigr].
$$
在 $\Omega_X$ 正定且二阶矩有限的正则条件下，$(\hat\tau^{\mathrm{ols}}, \hat\alpha^{\mathrm{ols}}, \hat{\boldsymbol{\beta}}^{\mathrm{ols}}) \to (\tau^*, \alpha^*, \boldsymbol{\beta}^*)$ 依概率成立。问题在于 $\tau^*$ 是什么。

### 5.3.2. 总体系数就是平均效应

**定理 5.3.1** 在对超总体的随机样本进行的 CRE 中，无论真实的条件期望 $\mu_{\mathrm{c}}(x)$ 与 $\mu_{\mathrm{t}}(x)$ 如何，都有 $\tau^* = \tau_{\mathrm{sp}}$。

**证明** 通过把截距重新参数化为 $\tilde\alpha = \alpha + \mu_X\boldsymbol{\beta}$ 来中心化协变量。目标函数变为

$$
Q(\tilde\alpha, \tau, \boldsymbol{\beta}) = \mathbb{E}_{\mathrm{sp}}\Bigl[\bigl(Y_i^{\mathrm{obs}} - \tilde\alpha - \tau W_i - (X_i - \mu_X)\boldsymbol{\beta}\bigr)^2\Bigr],
$$
而使其极小的 $\tau$ 与之前相同，因为重新参数化不涉及 $\tau$。展开平方，

$$
\begin{aligned}
Q(\tilde\alpha, \tau, \boldsymbol{\beta}) &= \mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \tilde\alpha - \tau W_i)^2\bigr] + \mathbb{E}_{\mathrm{sp}}\bigl[\bigl((X_i - \mu_X)\boldsymbol{\beta}\bigr)^2\bigr]\\
&\quad - 2\,\mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \tilde\alpha - \tau W_i)(X_i - \mu_X)\boldsymbol{\beta}\bigr].
\end{aligned}
$$
在交叉项中，$\mathbb{E}_{\mathrm{sp}}[\tilde\alpha(X_i - \mu_X)\boldsymbol{\beta}] = 0$，因为 $X_i - \mu_X$ 的均值为零；而 $\mathbb{E}_{\mathrm{sp}}[\tau W_i(X_i - \mu_X)\boldsymbol{\beta}] = \tau\,\mathbb{E}_{\mathrm{sp}}[W_i]\,\mathbb{E}_{\mathrm{sp}}[X_i - \mu_X]\boldsymbol{\beta} = 0$，因为 CRE 使 $W_i$ 与 $X_i$ 独立。于是

$$
Q(\tilde\alpha, \tau, \boldsymbol{\beta}) = \underbrace{\mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \tilde\alpha - \tau W_i)^2\bigr]}_{\text{仅依赖 } (\tilde\alpha, \tau)} + \underbrace{\mathbb{E}_{\mathrm{sp}}\bigl[\bigl((X_i - \mu_X)\boldsymbol{\beta}\bigr)^2\bigr] - 2\,\mathbb{E}_{\mathrm{sp}}\bigl[Y_i^{\mathrm{obs}}(X_i - \mu_X)\boldsymbol{\beta}\bigr]}_{\text{仅依赖 } \boldsymbol{\beta}}.
$$
目标函数可以分离，所以使 $(\tilde\alpha, \tau)$ 极小的点就是仅第一项的极小点。该项是无协变量回归的目标函数，其极小点为 $\tau^* = \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 1] - \mathbb{E}_{\mathrm{sp}}[Y_i^{\mathrm{obs}} \mid W_i = 0]$（5.2.4 节）。由 $W_i$ 与潜在结果的独立性，它等于 $\mathbb{E}_{\mathrm{sp}}[Y_i(1)] - \mathbb{E}_{\mathrm{sp}}[Y_i(0)] = \tau_{\mathrm{sp}}$。$\square$

证明只用了设计的一个性质，即 $W_i \perp X_i$ 以及 $W_i \perp (Y_i(0), Y_i(1))$，没有用回归模型的任何性质。协变量改变了 $\boldsymbol{\beta}^*$ 与残差，从而改变精度，但不改变目标。在观察性研究中，$W_i$ 与 $X_i$ 通常相依，交叉项不再消失，$\tau^*$ 一般不是因果效应。

### 5.3.3. 渐近正态性

**定理 5.3.2** 设对从无穷超总体中随机抽取的样本进行 CRE，且 $N_{\mathrm{t}}/N \to p \in (0, 1)$。则 $\hat\tau^{\mathrm{ols}} \xrightarrow{p} \tau^* = \tau_{\mathrm{sp}}$，且

$$
\sqrt{N}\bigl(\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}}\bigr) \xrightarrow{d} \mathcal{N}\left(0,\ \frac{\mathbb{E}_{\mathrm{sp}}\bigl[(W_i - p)^2\bigl(Y_i^{\mathrm{obs}} - \alpha^* - \tau_{\mathrm{sp}}W_i - X_i\boldsymbol{\beta}^*\bigr)^2\bigr]}{p^2(1 - p)^2}\right).
$$
无论回归模型是否正确，该定理都成立。

**证明**（概要）由 **Frisch–Waugh–Lovell 定理**，$\hat\tau^{\mathrm{ols}}$ 是 $Y^{\mathrm{obs}}$ 对 $W_i$ 关于截距与 $X_i$ 回归后的残差 $\tilde W_i$ 作回归的斜率。因为 $W_i$ 与 $X_i$ 独立，总体残差为 $W_i - p$，样本残差与之相差 $O_p(N^{-1/2})$。记 $\varepsilon_i^* = Y_i^{\mathrm{obs}} - \alpha^* - \tau_{\mathrm{sp}}W_i - X_i\boldsymbol{\beta}^*$，由一阶条件得 $\mathbb{E}_{\mathrm{sp}}[\varepsilon_i^*] = \mathbb{E}_{\mathrm{sp}}[W_i\varepsilon_i^*] = 0$，$\mathbb{E}_{\mathrm{sp}}[X_i^{\mathsf T}\varepsilon_i^*] = \boldsymbol{0}$，于是

$$
\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}} = \frac{\frac{1}{N}\sum_i (W_i - p)\varepsilon_i^*}{p(1 - p)} + o_p\bigl(N^{-1/2}\bigr).
$$
各求和项独立同分布，均值为零，方差为 $\mathbb{E}_{\mathrm{sp}}[(W_i - p)^2(\varepsilon_i^*)^2]$，由**中心极限定理**与 **Slutsky 定理**即得结论。$\square$

无协变量（$\boldsymbol{\beta}^* = \boldsymbol{0}$）时，处理单元的 $\varepsilon_i^* = Y_i(1) - \mu_{\mathrm{t}}$，对照单元的 $\varepsilon_i^* = Y_i(0) - \mu_{\mathrm{c}}$，渐近方差为

$$
\frac{p(1 - p)^2\sigma_{\mathrm{t}}^2 + (1 - p)p^2\sigma_{\mathrm{c}}^2}{p^2(1 - p)^2} = \frac{\sigma_{\mathrm{t}}^2}{p} + \frac{\sigma_{\mathrm{c}}^2}{1 - p},
$$
即定理 4.6.1 中 Neyman 方差 $\sigma_{\mathrm{c}}^2/N_{\mathrm{c}} + \sigma_{\mathrm{t}}^2/N_{\mathrm{t}}$ 的 $N$ 倍。含协变量时，残差 $\varepsilon_i^*$ 是由 $X_i$ 作最佳线性预测之后剩下的部分，协变量对结果的预测越好，它就越小。

### 5.3.4. 精度的提高：一个特例

**例 5.3.1** 设带公共斜率的线性模型是正确的，且结果的方差不依赖于处理或协变量：

$$
\mathbb{E}_{\mathrm{sp}}\bigl[Y_i^{\mathrm{obs}} \bigm| X_i = x, W_i = w\bigr] = \alpha_{\mathrm{c}} + \tau_{\mathrm{sp}}w + x\boldsymbol{\beta}, \qquad
\operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(w) \mid X_i = x\bigr) = \sigma_{Y \mid W, X}^2 \quad \text{对 } w = 0, 1 \text{ 与所有 } x.
$$
证明对 $X$ 调整使渐近方差缩小为原来的 $1 - R^2$ 倍，其中 $R^2$ 是（一个处理组内）结果方差中被 $X$ 解释的比例。

*无协变量。* 每个处理组内结果的方差相同，$\sigma_{Y \mid W}^2 = \operatorname{Var}_{\mathrm{sp}}(Y_i(w))$。同方差下的方差估计为

$$
\widehat{\operatorname{Var}}{}^{\mathrm{homosk}} = \frac{\hat\sigma_{Y \mid W}^2}{\sum_{i=1}^{N}(W_i - \bar W)^2} = \hat\sigma_{Y \mid W}^2\Bigl(\frac{1}{N_{\mathrm{c}}} + \frac{1}{N_{\mathrm{t}}}\Bigr), \qquad
\hat\sigma_{Y \mid W}^2 = \frac{1}{N - 2}\Bigl(\sum_{i: W_i = 0}(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}})^2 + \sum_{i: W_i = 1}(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}})^2\Bigr),
$$
且 $N \cdot \widehat{\operatorname{Var}}{}^{\mathrm{homosk}} \xrightarrow{p} \sigma_{Y \mid W}^2/\bigl(p(1 - p)\bigr)$。

*含协变量。* 模型正确，所以 $\boldsymbol{\beta}^* = \boldsymbol{\beta}$，且 $\varepsilon_i^*$ 在给定 $(W_i, X_i)$ 时的条件方差为 $\sigma_{Y \mid W, X}^2$。在定理 5.3.2 中，$\mathbb{E}_{\mathrm{sp}}[(W_i - p)^2(\varepsilon_i^*)^2] = \mathbb{E}_{\mathrm{sp}}[(W_i - p)^2]\,\sigma_{Y \mid W, X}^2 = p(1 - p)\sigma_{Y \mid W, X}^2$，所以 $\sqrt{N}(\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}})$ 的渐近方差为 $\sigma_{Y \mid W, X}^2/\bigl(p(1 - p)\bigr)$。

*比较。* 由于 $X_i \perp W_i$，在一个处理组内应用全方差公式得 $\sigma_{Y \mid W}^2 = \sigma_{Y \mid W, X}^2 + \boldsymbol{\beta}^{\mathsf T}\Omega_X\boldsymbol{\beta}$。因此

$$
\frac{\text{含 } X \text{ 的渐近方差}}{\text{不含 } X \text{ 的渐近方差}} = \frac{\sigma_{Y \mid W, X}^2}{\sigma_{Y \mid W}^2} = 1 - R^2, \qquad R^2 = \frac{\boldsymbol{\beta}^{\mathsf T}\Omega_X\boldsymbol{\beta}}{\sigma_{Y \mid W}^2}.
$$
$R^2 = 0.75$ 的协变量使标准误减半；这一收益相当于把样本量增为四倍。

:::

在这个特例中，调整从不会有害。一般情形下则可能有害：Freedman（2008）证明，当两组的斜率不同且设计不平衡（$p \ne 1/2$）时，定理 5.3.2 中估计量的渐近方差可能超过 $\hat\tau^{\mathrm{dif}}$ 的渐近方差，此时常规的（同方差）标准误还可能不相合。补救办法是加入交互项（5.4 节），并使用下一小节的稳健方差估计，它在两种情形下都有效。

### 5.3.5. 方差估计

在定理 5.3.2 中用样本平均代替总体期望，得到抽样方差的异方差稳健估计，

$$
\widehat{\operatorname{Var}}{}^{\mathrm{hetero}}_{\mathrm{sp}} = \frac{1}{N(N - 1 - K)} \cdot \frac{\sum_{i=1}^{N}(W_i - \bar W)^2\bigl(Y_i^{\mathrm{obs}} - \hat\alpha^{\mathrm{ols}} - \hat\tau^{\mathrm{ols}}W_i - X_i\hat{\boldsymbol{\beta}}^{\mathrm{ols}}\bigr)^2}{\bar W^2(1 - \bar W)^2},
$$
在同方差下则有更简单的

$$
\widehat{\operatorname{Var}}{}^{\mathrm{homo}}_{\mathrm{sp}} = \frac{1}{N(N - 1 - K)} \cdot \frac{\sum_{i=1}^{N}\bigl(Y_i^{\mathrm{obs}} - \hat\alpha^{\mathrm{ols}} - \hat\tau^{\mathrm{ols}}W_i - X_i\hat{\boldsymbol{\beta}}^{\mathrm{ols}}\bigr)^2}{\bar W(1 - \bar W)},
$$
其中 $K = \dim X_i$。第一个估计量除去自由度因子之外，就是该回归的 White 估计量的 $(\tau, \tau)$ 元；除非同方差模型有充分依据，应当使用它。

### 5.3.6. 插补解释

协变量调整后的估计量同样是插补估计量。对处理单元插补 $\hat Y_i(0) = \hat\alpha^{\mathrm{ols}} + X_i\hat{\boldsymbol{\beta}}^{\mathrm{ols}}$，对对照单元插补 $\hat Y_i(1) = \hat\alpha^{\mathrm{ols}} + \hat\tau^{\mathrm{ols}} + X_i\hat{\boldsymbol{\beta}}^{\mathrm{ols}}$。设残差为 $\hat\varepsilon_i$，则处理单元的估计单元效应为 $\hat\tau^{\mathrm{ols}} + \hat\varepsilon_i$，对照单元的为 $\hat\tau^{\mathrm{ols}} - \hat\varepsilon_i$，所以

$$
\frac{1}{N}\sum_{i=1}^{N}\hat\tau_i = \hat\tau^{\mathrm{ols}} + \frac{1}{N}\Bigl(\sum_{i: W_i = 1}\hat\varepsilon_i - \sum_{i: W_i = 0}\hat\varepsilon_i\Bigr) = \hat\tau^{\mathrm{ols}},
$$
因为截距与 $W$ 的正规方程使残差在每组内求和为零。在无混杂性下，回归是由单元的协变量预测每个缺失的潜在结果的工具；预测越好，估计越精确。

### 5.3.7. LRC-CPPT 的结果

| 协变量 | 估计 | （标准误） |
|---|---|---|
| 无 | $-26.22$ | $(3.93)$ |
| `cholp` | $-25.01$ | $(2.60)$ |
| `chol1`、`chol2` | $-25.02$ | $(2.59)$ |
| `chol1`、`chol2`，与 $W$ 交互 | $-25.04$ | $(2.56)$ |

被分配到药物对处理后胆固醇的效应是下降约 25 个单位。如随机化所保证的，加入协变量后点估计几乎不动，但标准误下降了三分之一：处理前的测量值解释了超过一半的结果方差（$1 - (2.60/3.93)^2 \approx 0.56$）。用两个单独的处理前测量值代替它们的综合量，或加入交互项，几乎没有变化。

### 5.3.8. 协变量是否越多越好？

即使在无混杂性下，答案也是否定的，理由有三。

- *处理后变量。* 定理 5.3.1 的论证要求 $X_i \perp W_i$，这只对在分配之前确定的变量成立。LRC-CPPT 的依从变量 `comp` 受处理影响（处理组服用的剂量比例较低，大概是副作用所致），所以它是分配的函数，对它调整会把估计目标改成不再是分配的因果效应的东西。由处理后行为所定义的子群中的效应，需要 [3.9.14](/3.9.14) 的方法。
- *有限样本偏差。* 含协变量的 $\hat\tau^{\mathrm{ols}}$ 是相合的，但与 $\hat\tau^{\mathrm{dif}}$ 不同，它不是严格无偏的；其偏差为 $1/N$ 阶，并随协变量个数相对于样本量的增加而增大。
- *精度。* 不能预测结果的协变量会损失一个自由度，并且在 5.3.4 节所述不平衡且异质的情形中还可能增大方差。

实践中，协变量应当少而精，在分配之前测得，根据预期的预测力选取，并在看到结果之前确定，使选择不能被调整得迎合结果。

## 5.4. 交互项与检验

### 5.4.1. 含交互的回归

允许两组的斜率不同，得到模型

$$
Y_i^{\mathrm{obs}} = \alpha + \tau W_i + X_i\boldsymbol{\beta} + W_i(X_i - \bar X)\boldsymbol{\gamma} + \varepsilon_i,
$$
其最小二乘估计量为 $(\hat\tau^{\mathrm{ols}}, \hat\alpha^{\mathrm{ols}}, \hat{\boldsymbol{\beta}}^{\mathrm{ols}}, \hat{\boldsymbol{\gamma}}^{\mathrm{ols}})$，总体对应量为 $(\tau^*, \alpha^*, \boldsymbol{\beta}^*, \boldsymbol{\gamma}^*)$，以 $\mu_X$ 代替 $\bar X$ 来定义。因为模型是完全交互的，它等价于在两组中分别回归，$\hat\mu_{\mathrm{c}}(x) = \hat\alpha_{\mathrm{c}} + x\hat{\boldsymbol{\beta}}_{\mathrm{c}}$，$\hat\mu_{\mathrm{t}}(x) = \hat\alpha_{\mathrm{t}} + x\hat{\boldsymbol{\beta}}_{\mathrm{t}}$，而把交互项在 $\bar X$ 处中心化，使 $W_i$ 的系数成为预测效应在整个样本上的平均，

$$
\hat\tau^{\mathrm{ols}} = \hat\mu_{\mathrm{t}}(\bar X) - \hat\mu_{\mathrm{c}}(\bar X) = \frac{1}{N}\sum_{i=1}^{N}\bigl(\hat\mu_{\mathrm{t}}(X_i) - \hat\mu_{\mathrm{c}}(X_i)\bigr).
$$
不作中心化时，$W_i$ 的系数是 $X_i = 0$ 处的预测效应，这通常不是我们关心的。这仍是一个插补估计量，只是对每个潜在结果各有一个预测模型。

**定理 5.4.1** 在对超总体的随机样本进行的 CRE 中，(i) $\tau^* = \tau_{\mathrm{sp}}$；(ii)

$$
\sqrt{N}\bigl(\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}}\bigr) \xrightarrow{d} \mathcal{N}\left(0,\ \frac{\mathbb{E}_{\mathrm{sp}}\bigl[(W_i - p)^2\bigl(Y_i^{\mathrm{obs}} - \alpha^* - \tau_{\mathrm{sp}}W_i - X_i\boldsymbol{\beta}^* - W_i(X_i - \mu_X)\boldsymbol{\gamma}^*\bigr)^2\bigr]}{p^2(1 - p)^2}\right).
$$
证明与定理 5.3.1、5.3.2 类似：两个总体线性预测在协变量均值处之差 $\mu_{\mathrm{t}}^{\mathrm{lin}}(\mu_X) - \mu_{\mathrm{c}}^{\mathrm{lin}}(\mu_X)$ 等于 $\mathbb{E}_{\mathrm{sp}}[Y_i(1)] - \mathbb{E}_{\mathrm{sp}}[Y_i(0)]$，因为每个带截距的总体回归在回归变量的均值处重现其结果的均值，而 $X_i$ 在两组中分布相同。

交互项的好处在于两组可以有不同的斜率。Lin（2013）证明，无论真实的回归函数如何，含交互的估计量在渐近意义上至少与 $\hat\tau^{\mathrm{dif}}$ 以及 5.3 节的估计量一样精确，并且稳健方差估计对它是相合的或保守的。斜率相同或 $p = 1/2$ 时，交互项没有渐近收益，但代价也很小。

![N = 100、含一个正态协变量（平均效应为 1）的模拟完全随机化实验。左：斜率相同且一半单元接受处理时，两个回归估计量的离散程度远小于均值差。右：对照组斜率为 -1、处理组斜率为 3 时，设计不平衡的情形下无交互的回归可能不如均值差精确，而含交互的回归在每个处理比例下都最精确。模拟数据](./plots/covariate_adjustment.py)

### 5.4.2. 效应异质性的检验

含交互的模型还可以检验效应如何随协变量变化。设 $\widehat{\operatorname{Var}}(\hat\tau^{\mathrm{ols}}, \hat{\boldsymbol{\gamma}}^{\mathrm{ols}})$ 是 $(\hat\tau^{\mathrm{ols}}, \hat{\boldsymbol{\gamma}}^{\mathrm{ols}})$ 协方差矩阵的稳健估计，其分块为 $\widehat{\operatorname{Var}}_\tau$、$\widehat{\operatorname{Var}}_\gamma$ 与 $\widehat{\operatorname{Cov}}_{\tau, \gamma}$。有两个原假设值得关注：

| 原假设 | 统计量 | $H_0$ 下的极限 |
|---|---|---|
| 常数效应：$H_0'\colon \tau(x) = \tau_{\mathrm{sp}}$ 对所有 $x$ | $Q_{\mathrm{const}} = (\hat{\boldsymbol{\gamma}}^{\mathrm{ols}})^{\mathsf T}\widehat{\operatorname{Var}}_\gamma^{-1}\hat{\boldsymbol{\gamma}}^{\mathrm{ols}}$ | $\chi^2_K$ |
| 零效应：$H_0\colon \tau(x) = 0$ 对所有 $x$ | $Q_{\mathrm{zero}} = \begin{pmatrix}\hat\tau^{\mathrm{ols}}\\ \hat{\boldsymbol{\gamma}}^{\mathrm{ols}}\end{pmatrix}^{\mathsf T}\widehat{\operatorname{Var}}(\hat\tau^{\mathrm{ols}}, \hat{\boldsymbol{\gamma}}^{\mathrm{ols}})^{-1}\begin{pmatrix}\hat\tau^{\mathrm{ols}}\\ \hat{\boldsymbol{\gamma}}^{\mathrm{ols}}\end{pmatrix}$ | $\chi^2_{K+1}$ |

**定理 5.4.2** 在对大总体的随机样本进行的 CRE 中，若对某个常数 $\tau$ 与所有单元有 $Y_i(1) - Y_i(0) = \tau$，则 $\boldsymbol{\gamma}^* = \boldsymbol{0}$，且 $Q_{\mathrm{const}} \xrightarrow{d} \chi^2_K$；若对所有单元 $Y_i(1) - Y_i(0) = 0$，则 $\tau^* = 0$，$\boldsymbol{\gamma}^* = \boldsymbol{0}$，且 $Q_{\mathrm{zero}} \xrightarrow{d} \chi^2_{K+1}$。

两者都是多个参数的 **Wald 检验**，其结论针对线性投影：$\boldsymbol{\gamma}^* = \boldsymbol{0}$ 并不排除与 $X$ 的线性函数不相关的异质性。零效应假设是尖锐原假设，所以也可以把 $Q_{\mathrm{zero}}$ 作为 Fisher 检验的统计量作精确检验（[3.9.3](/3.9.3)）。

对以 `chol1` 与 `chol2` 为协变量（$K = 2$）的 LRC-CPPT 数据：

| 假设 | 方法 | p 值 |
|---|---|---|
| 零效应 | $\chi^2_3$ 近似 | $< 0.001$ |
| 零效应 | Fisher 精确 p 值 | $< 0.001$ |
| 常数效应 | $\chi^2_2$ 近似 | $0.029$ |

药物降低胆固醇的证据极为充分。有一些证据表明效应随处理前水平而变（$p = 0.029$），但这种变化相对于平均效应很小，考虑它之后，平均效应的估计值不变。

## 小结

| 回归 | 目标 | 关键性质 | 方差（渐近地，乘以 $N$） |
|---|---|---|---|
| $Y^{\mathrm{obs}} \sim 1 + W$ | $\tau_{\mathrm{sp}}$ | $\hat\tau^{\mathrm{ols}} = \hat\tau^{\mathrm{dif}}$（定理 5.2.1）；由随机化得 $\mathbb{E}[\varepsilon \mid W] = 0$ | $\sigma_{\mathrm{t}}^2/p + \sigma_{\mathrm{c}}^2/(1 - p)$ |
| $Y^{\mathrm{obs}} \sim 1 + W + X$ | $\tau^* = \tau_{\mathrm{sp}}$（定理 5.3.1） | 即使模型有误也相合且渐近正态（定理 5.3.2） | $\mathbb{E}[(W - p)^2\varepsilon^{*2}]/(p(1 - p))^2$ |
| $Y^{\mathrm{obs}} \sim 1 + W + X + W(X - \bar X)$ | $\tau^* = \tau_{\mathrm{sp}}$（定理 5.4.1） | 斜率分开；渐近地从不更差 | 形式相同，用含交互的残差 |

- 回归系数的因果含义来自设计：CRE 中 $W_i \perp (Y_i(0), Y_i(1), X_i)$。观察性研究中的同一回归估计的是关联。
- 无协变量时，常规标准误是 $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$，稳健（HC2）标准误是 $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$；回归推断与 Neyman 的推断一致。
- 协变量通过解释结果方差而有帮助：在正确的同方差模型下，方差乘以 $1 - R^2$（例 5.3.1）。无交互项时，斜率不同且 $p \ne 1/2$ 的情形下调整可能有害；有交互项时（渐近地）不会。
- 这里的每个回归估计量都是插补估计量：即 $Y_i^{\mathrm{obs}} - \hat Y_i(0)$ 与 $\hat Y_i(1) - Y_i^{\mathrm{obs}}$ 的平均。
- 只用处理前的协变量，个数要少，在看到结果之前选定；报告稳健标准误。
- LRC-CPPT：不含处理前胆固醇为 $-26.2$（3.9），含它为 $-25.0$（2.6）。

## 思考题

1. 仅用 5.2.2 节的回归表示，证明在 CRE 中无协变量回归的估计量 $\hat\tau^{\mathrm{ols}}$ 对 $\tau_{\mathrm{sp}}$ 无偏。

   **答** 由定理 5.2.1，$\hat\tau^{\mathrm{ols}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$。代入 $Y_i^{\mathrm{obs}} = \alpha + \tau W_i + \varepsilon_i$：$\bar Y_{\mathrm{t}}^{\mathrm{obs}} = \alpha + \tau + \bar\varepsilon_{\mathrm{t}}$，$\bar Y_{\mathrm{c}}^{\mathrm{obs}} = \alpha + \bar\varepsilon_{\mathrm{c}}$，所以 $\hat\tau^{\mathrm{ols}} = \tau + \bar\varepsilon_{\mathrm{t}} - \bar\varepsilon_{\mathrm{c}}$。给定 $\boldsymbol{W}$，每个 $\varepsilon_i$ 的均值为零，因为 $\mathbb{E}_{\mathrm{sp}}[\varepsilon_i \mid W_i] = 0$，且各单元独立同分布并与分配独立。故 $\mathbb{E}_{\mathrm{sp}}[\hat\tau^{\mathrm{ols}} \mid \boldsymbol{W}] = \tau = \tau_{\mathrm{sp}}$，对 $\boldsymbol{W}$ 取平均即得无偏性。

2. 在 $N = 6$、$N_{\mathrm{t}} = 3$ 的 CRE 中，观测结果为 $3, 5, 7$（处理）与 $2, 2, 5$（对照）。计算 $\hat\tau^{\mathrm{ols}}$、常规 OLS 标准误，以及 HC0 与 HC2 稳健标准误。哪一个等于 Neyman 标准误？

   **答** $\bar Y_{\mathrm{t}}^{\mathrm{obs}} = 5$，$\bar Y_{\mathrm{c}}^{\mathrm{obs}} = 3$，所以 $\hat\tau^{\mathrm{ols}} = 2$。残差平方和为 $4 + 0 + 4 = 8$（处理）与 $1 + 1 + 4 = 6$（对照），所以 $s_{\mathrm{t}}^2 = 4$，$s_{\mathrm{c}}^2 = 3$。常规：$\hat\sigma^2 = 14/4 = 3.5$，方差 $3.5(1/3 + 1/3) = 2.333$，标准误 $1.53$。HC0：$8/9 + 6/9 = 1.556$，标准误 $1.25$。HC2：$s_{\mathrm{t}}^2/3 + s_{\mathrm{c}}^2/3 = 4/3 + 1 = 2.333$，标准误 $1.53$。HC2 等于 Neyman 估计 $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$。这里它还与常规估计一致，因为 $N_{\mathrm{t}} = N_{\mathrm{c}}$：两组样本量相等时，合并估计与 Neyman 估计相同。

3. 定理 5.3.1 的证明究竟在哪里用到了随机化？举一个观察性研究的例子，其中即使每个潜在结果对 $X$ 的真实回归都是线性的，仍有 $\tau^* \ne \tau_{\mathrm{sp}}$。

   **答** 用到两次：使交叉项消失（$\mathbb{E}[W_i(X_i - \mu_X)] = 0$ 需要 $W_i \perp X_i$），以及把 $Y^{\mathrm{obs}}$ 仅对 $W$ 回归的系数与 $\tau_{\mathrm{sp}}$ 等同起来（$W_i \perp (Y_i(0), Y_i(1))$）。例：$X_i \sim \mathcal{N}(0, 1)$，$Y_i(0) = X_i$，$Y_i(1) = 3X_i$，两个回归都是线性的，$\tau_{\mathrm{sp}} = \mathbb{E}[2X_i] = 0$，而 $X_i$ 大的单元接受处理，$W_i = \boldsymbol{1}\{X_i > 1\}$。回归 $Y^{\mathrm{obs}} \sim 1 + W + X$ 强制公共斜率；由于处理单元的 $X_i$ 都很大，而那里 $Y_i(1) - Y_i(0) = 2X_i$ 很大，$W$ 的系数吸收了这一差异：数值计算得 $\tau^* \approx 2.85$，远离 $\tau_{\mathrm{sp}} = 0$。它大致度量的是处理组中的效应，而不是总体平均效应，而且即便如此也只是借助一条设定有误的直线外推得到的。观察性研究因此需要 [3.9.8](/3.9.8)–[3.9.10](/3.9.10) 的设计工具。

4. （协变量的收益）在例 5.3.1 中，设处理前胆固醇解释了处理后胆固醇组内方差的 $60\%$。对它调整使标准误降低多少？未调整的分析需要多少单元才能达到同样的精度？

   **答** 方差乘以 $1 - R^2 = 0.4$，所以标准误乘以 $\sqrt{0.4} \approx 0.63$，降低 $37\%$。方差与 $N$ 成反比，所以未调整的分析需要 $N/0.4 = 2.5N$ 个单元。

5. 证明 5.4.1 节在 $\bar X$ 处中心化的含交互估计量满足 $\hat\tau^{\mathrm{ols}} = (\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}) - (\bar X_{\mathrm{t}} - \bar X)\hat{\boldsymbol{\beta}}_{\mathrm{t}} + (\bar X_{\mathrm{c}} - \bar X)\hat{\boldsymbol{\beta}}_{\mathrm{c}}$，并解释修正项的含义。

   **答** 在分组回归中，拟合直线通过各组的均值：$\hat\alpha_{\mathrm{t}} + \bar X_{\mathrm{t}}\hat{\boldsymbol{\beta}}_{\mathrm{t}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}}$，所以 $\hat\mu_{\mathrm{t}}(\bar X) = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - (\bar X_{\mathrm{t}} - \bar X)\hat{\boldsymbol{\beta}}_{\mathrm{t}}$，对照组同理。相减即得公式。每个组均值沿该组自己的回归直线，从该组自己的协变量均值移到总均值。在 CRE 中 $\bar X_{\mathrm{t}} - \bar X$ 与 $\bar X_{\mathrm{c}} - \bar X$ 都很小，为 $N^{-1/2}$ 阶，修正项去掉了 $\hat\tau^{\mathrm{dif}}$ 中由协变量偶然失衡造成的部分。

6. （表决）若分配是无混杂的，加入更多协变量是否总是更好？分别给出正反两方的论据，并作出结论。

   **答** 赞成：在无混杂性下，每增加一个处理前协变量，目标 $\tau^* = \tau_{\mathrm{sp}}$ 都不变（定理 5.3.1），并且可能解释更多的结果方差。反对：在分配之后测得的变量（如依从情况）不在定理的适用范围内，并且会改变估计目标；相对于 $N$ 协变量过多时，有限样本偏差与自由度的损失增大；无交互项时，若斜率不同且设计不平衡，协变量甚至会增大渐近方差。结论：并不总是如此；应使用少量事先根据预测力选定的处理前协变量，最好带交互项并使用稳健标准误。

7. 在 LRC-CPPT 数据中，加入 `cholp` 后标准误由 $3.93$ 降到 $2.60$。估计 `cholp` 所解释的结果方差的比例，并解释为什么随机化使两个估计量对同一个量都相合，而点估计却由 $-26.22$ 变到 $-25.01$。

   **答** 约为 $1 - (2.60/3.93)^2 = 1 - 0.438 \approx 0.56$。$1.2$ 的变化来自偶然的失衡：处理组的 `cholp` 均值比对照组低 $1.3$（$289.9$ 对 $291.2$），斜率约为 1，调整后的估计去掉了均值差中归因于这一失衡的部分。这一变化远在一个标准误之内，这正是随机化实验应有的情形。

8. 为什么 5.4.2 节的零效应检验既可以作 $\chi^2$ 检验又可以作 Fisher 精确检验，而常数效应的检验只能是近似的？

   **答** 在零效应假设下，对所有单元 $Y_i(1) = Y_i(0)$ 是尖锐原假设：所有缺失的潜在结果都已知，任何统计量（包括 $Q_{\mathrm{zero}}$）的随机化分布都可以精确计算（[3.9.3](/3.9.3)）。常数效应假设没有指定 $\tau$ 的值，所以缺失的结果只在相差讨厌参数 $\tau$ 的意义下已知；检验只能依赖大样本的 $\chi^2_K$ 近似（或依赖对 $\tau$ 取最大或代入的更精细的构造）。
