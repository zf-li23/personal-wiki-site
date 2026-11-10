---
title: 完全随机化实验：Neyman 重复抽样方法
description: Neyman 的完全随机化实验方法。均值差估计量及其对有限样本平均处理效应的无偏性；精确的随机化方差、证明及其用潜在结果相关系数的表示；保守的 Neyman 方差估计及其替代；大样本置信区间与弱原假设的检验，以蜂蜜数据为例；以及含两层随机性的超总体观点。
source_hash: 2ee2d464d9ac
---

[3.9.3](/3.9.3) 的 Fisher 方法回答的是一个狭窄的问题：处理对某个单元是否有效应？其尖锐原假设限制很强，拒绝它也不能说明效应有多大。Neyman（1923）在引入潜在结果的那篇论文中提出了另一个问题：处理的平均效应是多少，随机化实验能把它估计得多精确？他的答案是两组平均结果之差——仅就随机化而言，它是平均处理效应的无偏估计量——再配上方差公式、该方差的保守估计和大样本置信区间。本章先固定潜在结果，使随机性只来自完全随机化实验（CRE）的分配；最后把单元看作来自超总体的样本，从而引入第二层随机性。[3.9.5](/3.9.5) 的回归方法和 [3.9.7](/3.9.7) 的分层与配对设计都建立在本章的结果之上。

## 4.1. Fisher 方法与 Neyman 方法

| | Fisher | Neyman |
|---|---|---|
| 问题 | 是否存在单元层面的效应？ | 平均效应有多大？ |
| 假设或估计目标 | 尖锐原假设：对所有 $i$，$Y_i(1) = Y_i(0)$ | $\tau_{\mathrm{fs}} = \bar Y(1) - \bar Y(0)$（或 $\tau_{\mathrm{sp}}$） |
| 缺失的结果 | 在 $H_0$ 下精确插补 | 不插补，只用平均值 |
| 输出 | 精确 p 值 | 无偏点估计、方差、置信区间 |
| 随机性 | 分配 $\boldsymbol{W}$ | 分配；在超总体中还有单元的抽样 |
| 推断 | 有限样本下精确 | 近似，大样本下基于正态分布 |

本章中，$\mathbb{E}_W$ 与 $\operatorname{Var}_W$ 表示固定潜在结果时对随机分配取的矩，$\mathbb{E}_{\mathrm{sp}}$、$\operatorname{Var}_{\mathrm{sp}}$ 表示对抽样与分配两者取的矩（[3.9.1](/3.9.1)）。

## 4.2. 均值差估计量

### 4.2.1. 无偏性

估计目标是有限样本的**平均处理效应** $\tau_{\mathrm{fs}} = \frac{1}{N}\sum_{i=1}^{N}(Y_i(1) - Y_i(0))$。

**定义 4.2.1（均值差估计量）** 在有 $N_{\mathrm{t}}$ 个处理单元与 $N_{\mathrm{c}}$ 个对照单元的 CRE 中，**均值差估计量**（又称 Neyman 估计量）为

$$
\hat\tau^{\mathrm{dif}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}Y_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}Y_i^{\mathrm{obs}}.
$$

为把它作为随机分配的函数来研究，用固定的潜在结果与随机指示变量来表示。由于 $W_iY_i^{\mathrm{obs}} = W_iY_i(1)$ 且 $(1 - W_i)Y_i^{\mathrm{obs}} = (1 - W_i)Y_i(0)$，

$$
\hat\tau^{\mathrm{dif}} = \frac{1}{N}\sum_{i=1}^{N}\left(\frac{N}{N_{\mathrm{t}}}W_iY_i(1) - \frac{N}{N_{\mathrm{c}}}(1 - W_i)Y_i(0)\right).
$$

**定理 4.2.1（均值差的无偏性）** 在 CRE 中，$\mathbb{E}_W[\hat\tau^{\mathrm{dif}}] = \tau_{\mathrm{fs}}$。

**证明** 每个单元以概率 $N_{\mathrm{t}}/N$ 接受处理，故 $\mathbb{E}_W[W_i] = N_{\mathrm{t}}/N$，$\mathbb{E}_W[1 - W_i] = N_{\mathrm{c}}/N$。潜在结果是常数，由线性性

$$
\mathbb{E}_W\bigl[\hat\tau^{\mathrm{dif}}\bigr] = \frac{1}{N}\sum_{i=1}^{N}\left(\frac{N}{N_{\mathrm{t}}}\cdot\frac{N_{\mathrm{t}}}{N}Y_i(1) - \frac{N}{N_{\mathrm{c}}}\cdot\frac{N_{\mathrm{c}}}{N}Y_i(0)\right) = \frac{1}{N}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0)\bigr) = \tau_{\mathrm{fs}}. \qquad \square
$$

这一结果对潜在结果没有任何要求：不需要模型，不需要效应为常数，也不需要分布假定。正是随机化使处理组的平均值成为全部 $Y_i(1)$ 的平均值的无偏估计，使对照组的平均值成为全部 $Y_i(0)$ 的平均值的无偏估计。在这个意义上，$\hat\tau^{\mathrm{dif}}$ 是有限样本效应的**无偏估计**，这里的"无偏"指对同一批单元重复进行随机化：这就是重复抽样方法名称的由来。

**例 4.2.1** 对 [3.9.3](/3.9.3) 的蜂蜜实验，取 $N = 72$、$N_{\mathrm{t}} = 35$，以咳嗽频率为结果，$\hat\tau^{\mathrm{dif}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = -0.697$：在 $0$–$6$ 的量表上，服用蜂蜜的儿童平均咳嗽频率低约 $0.7$ 分。要判断这是否超出偶然，需要知道它的方差。

### 4.2.2. 从方差到置信区间

$\tau_{\mathrm{fs}}$ 的置信区间分三步构造：

1. 推导估计量在随机化下的抽样方差；
2. 构造该抽样方差的估计量；
3. 利用估计值及其估计方差，借助正态近似构造大样本置信区间。

4.3–4.5 节依次完成这些步骤。

## 4.3. 抽样方差

### 4.3.1. 方差定理

定义有限总体均值 $\bar Y(w) = \frac{1}{N}\sum_i Y_i(w)$ 与有限总体方差

$$
S_{\mathrm{c}}^2 = \frac{1}{N - 1}\sum_{i=1}^{N}\bigl(Y_i(0) - \bar Y(0)\bigr)^2, \qquad
S_{\mathrm{t}}^2 = \frac{1}{N - 1}\sum_{i=1}^{N}\bigl(Y_i(1) - \bar Y(1)\bigr)^2,
$$

$$
S_{\mathrm{tc}}^2 = \frac{1}{N - 1}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0) - \tau_{\mathrm{fs}}\bigr)^2.
$$
$S_{\mathrm{c}}^2$ 与 $S_{\mathrm{t}}^2$ 分别是全部 $N$ 个单元的对照与处理潜在结果的方差，$S_{\mathrm{tc}}^2$ 是单元层面处理效应的方差。三者都是固定的数，且都涉及缺失的潜在结果。方差公式的证明依赖于分配指示变量的联合分布。

**引理 4.3.1** 在 CRE 中，令 $D_i = W_i - N_{\mathrm{t}}/N$。则 $\sum_{i=1}^{N}D_i = 0$，$\mathbb{E}_W[D_i] = 0$，且

$$
\mathbb{E}_W\bigl[D_i^2\bigr] = \operatorname{Var}_W(W_i) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2}, \qquad
\mathbb{E}_W[D_iD_j] = \operatorname{Cov}_W(W_i, W_j) = -\frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2(N - 1)} \quad (i \ne j).
$$
因此，对任意均值为 $\bar a$ 的常数 $a_1, \dots, a_N$，

$$
\operatorname{Var}_W\left(\sum_{i=1}^{N}D_ia_i\right) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}\cdot\frac{1}{N - 1}\sum_{i=1}^{N}(a_i - \bar a)^2.
$$

**证明** 第一个等式成立是因为恰有 $N_{\mathrm{t}}$ 个 $W_i$ 等于 1。$W_i$ 服从成功概率为 $N_{\mathrm{t}}/N$ 的 Bernoulli 分布，故 $\operatorname{Var}_W(W_i) = \frac{N_{\mathrm{t}}}{N}\cdot\frac{N_{\mathrm{c}}}{N}$。对 $i \ne j$，两个单元同时接受处理的概率为 $\frac{N_{\mathrm{t}}(N_{\mathrm{t}} - 1)}{N(N - 1)}$，于是

$$
\operatorname{Cov}_W(W_i, W_j) = \frac{N_{\mathrm{t}}(N_{\mathrm{t}} - 1)}{N(N - 1)} - \frac{N_{\mathrm{t}}^2}{N^2} = \frac{N_{\mathrm{t}}\bigl[N(N_{\mathrm{t}} - 1) - N_{\mathrm{t}}(N - 1)\bigr]}{N^2(N - 1)} = -\frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2(N - 1)}.
$$
（另一种推法：$0 = \operatorname{Var}_W(\sum_i D_i) = N\operatorname{Var}_W(D_i) + N(N - 1)\operatorname{Cov}_W(D_i, D_j)$。）对最后一个公式，

$$
\operatorname{Var}_W\left(\sum_i D_ia_i\right) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2}\left[\sum_i a_i^2 - \frac{1}{N - 1}\sum_{i \ne j}a_ia_j\right]
= \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N^2}\cdot\frac{N\sum_i a_i^2 - \bigl(\sum_i a_i\bigr)^2}{N - 1},
$$
这里用到 $\sum_{i \ne j}a_ia_j = (\sum_i a_i)^2 - \sum_i a_i^2$ 以及 $N\sum_i a_i^2 - (\sum_i a_i)^2 = N\sum_i (a_i - \bar a)^2$。$\square$

最后一个公式就是不放回简单随机抽样中求和量的方差，只是写成了方便的形式；其中隐含的因子 $\frac{N_{\mathrm{c}}}{N}$ 就是有限总体修正。取 $a_i = Y_i(1)/N_{\mathrm{t}}$，得到 $\operatorname{Var}_W(\bar Y_{\mathrm{t}}^{\mathrm{obs}}) = \frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}S_{\mathrm{t}}^2 = \left(\frac{1}{N_{\mathrm{t}}} - \frac{1}{N}\right)S_{\mathrm{t}}^2$，因为 $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y(1) = \frac{1}{N_{\mathrm{t}}}\sum_i D_iY_i(1)$。

**定理 4.3.1（均值差的抽样方差）** 在 CRE 中，

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{S_{\mathrm{tc}}^2}{N}. \tag{4.1}
$$

**证明** 在 4.2.1 节的表示式中代入 $W_i = D_i + N_{\mathrm{t}}/N$ 与 $1 - W_i = N_{\mathrm{c}}/N - D_i$，

$$
\hat\tau^{\mathrm{dif}} = \frac{1}{N}\sum_i\bigl(Y_i(1) - Y_i(0)\bigr) + \sum_i D_i\left(\frac{Y_i(1)}{N_{\mathrm{t}}} + \frac{Y_i(0)}{N_{\mathrm{c}}}\right)
= \tau_{\mathrm{fs}} + \sum_{i=1}^{N}D_ia_i, \qquad a_i = \frac{Y_i(1)}{N_{\mathrm{t}}} + \frac{Y_i(0)}{N_{\mathrm{c}}}.
$$
由引理 4.3.1，$\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}S_a^2$，其中 $S_a^2$ 是 $a_i$ 的有限总体方差。设 $S_{01} = \frac{1}{N - 1}\sum_i (Y_i(1) - \bar Y(1))(Y_i(0) - \bar Y(0))$ 为两个潜在结果的有限总体协方差。则

$$
S_a^2 = \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}^2} + \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}^2} + \frac{2S_{01}}{N_{\mathrm{t}}N_{\mathrm{c}}},
\qquad
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{1}{N}\left(\frac{N_{\mathrm{c}}}{N_{\mathrm{t}}}S_{\mathrm{t}}^2 + \frac{N_{\mathrm{t}}}{N_{\mathrm{c}}}S_{\mathrm{c}}^2 + 2S_{01}\right).
$$
效应之差的方差为 $S_{\mathrm{tc}}^2 = S_{\mathrm{t}}^2 + S_{\mathrm{c}}^2 - 2S_{01}$，故 $2S_{01} = S_{\mathrm{t}}^2 + S_{\mathrm{c}}^2 - S_{\mathrm{tc}}^2$，从而

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{1}{N}\left[\left(\frac{N_{\mathrm{c}}}{N_{\mathrm{t}}} + 1\right)S_{\mathrm{t}}^2 + \left(\frac{N_{\mathrm{t}}}{N_{\mathrm{c}}} + 1\right)S_{\mathrm{c}}^2 - S_{\mathrm{tc}}^2\right] = \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} + \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} - \frac{S_{\mathrm{tc}}^2}{N}. \qquad \square
$$

前两项相当于把两个组均值看作来自两个总体的独立样本时得到的方差；第三项为负，反映了两组是从同一批 $N$ 个单元中不放回地抽出的，因而两个均值是负相关的。仅当各单元的效应全部相等时它才为零。

**推论 4.3.1** 若处理效应为常数，即对所有 $i$ 有 $Y_i(1) - Y_i(0) = \tau_{\mathrm{fs}}$，则 $S_{\mathrm{tc}}^2 = 0$，$S_{\mathrm{t}}^2 = S_{\mathrm{c}}^2 = S^2$，且

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} = S^2\left(\frac{1}{N_{\mathrm{c}}} + \frac{1}{N_{\mathrm{t}}}\right).
$$

在 [3.9.3](/3.9.3) 的尖锐原假设下，常数效应为零，这就是定理 3.3.2。

**例 4.3.1** 回到例 1.5.1 的四名患者，$Y(0) = (1, 6, 1, 8)$，$Y(1) = (7, 5, 5, 7)$，现用 $N_{\mathrm{t}} = 2$ 的 CRE 分配。六种可能的处理对及相应的估计值为

| 处理单元 | $\{1,2\}$ | $\{1,3\}$ | $\{1,4\}$ | $\{2,3\}$ | $\{2,4\}$ | $\{3,4\}$ |
|---|---|---|---|---|---|---|
| $\hat\tau^{\mathrm{dif}}$ | $1.5$ | $-1$ | $3.5$ | $0.5$ | $5$ | $2.5$ |

它们的平均值为 $2 = \tau_{\mathrm{fs}}$，与定理 4.2.1 一致；它们的方差（每种分配的概率为 $1/6$，故除数为 $6$）为 $3.833$。公式给出同样的结果：$S_{\mathrm{c}}^2 = 38/3 \approx 12.667$，$S_{\mathrm{t}}^2 = 4/3$，单元效应 $(6, -1, 4, -1)$ 的 $S_{\mathrm{tc}}^2 = 38/3$，而

$$
\frac{38/3}{2} + \frac{4/3}{2} - \frac{38/3}{4} = \frac{19}{3} + \frac{2}{3} - \frac{19}{6} = \frac{23}{6} \approx 3.833.
$$
若忽略第三项，方差会被高估 $S_{\mathrm{tc}}^2/N = 19/6$，几乎是真值的两倍。

### 4.3.2. 用潜在结果的相关系数表示

设 $\rho_{\mathrm{tc}} = S_{01}/(S_{\mathrm{t}}S_{\mathrm{c}})$ 为 $Y_i(1)$ 与 $Y_i(0)$ 的有限总体**相关系数**。

**定理 4.3.2** 在 CRE 中，

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = S_{\mathrm{c}}^2\cdot\frac{N_{\mathrm{t}}}{N\cdot N_{\mathrm{c}}} + S_{\mathrm{t}}^2\cdot\frac{N_{\mathrm{c}}}{N\cdot N_{\mathrm{t}}} + \rho_{\mathrm{tc}}\cdot S_{\mathrm{c}}\cdot S_{\mathrm{t}}\cdot\frac{2}{N}.
$$
给定 $S_{\mathrm{c}}$ 与 $S_{\mathrm{t}}$，方差在 $\rho_{\mathrm{tc}} = 1$ 时最大，在 $\rho_{\mathrm{tc}} = -1$ 时最小。

**证明** 在 (4.1) 中代入 $S_{\mathrm{tc}}^2 = S_{\mathrm{t}}^2 + S_{\mathrm{c}}^2 - 2\rho_{\mathrm{tc}}S_{\mathrm{t}}S_{\mathrm{c}}$，并利用 $\frac{1}{N_{\mathrm{c}}} - \frac{1}{N} = \frac{N_{\mathrm{t}}}{NN_{\mathrm{c}}}$、$\frac{1}{N_{\mathrm{t}}} - \frac{1}{N} = \frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}$。方差关于 $\rho_{\mathrm{tc}}$ 递增，而 $\rho_{\mathrm{tc}}$ 位于 $[-1, 1]$ 内。$\square$

取 $\rho_{\mathrm{tc}} = 1$，上界为

$$
\frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{(S_{\mathrm{t}} - S_{\mathrm{c}})^2}{N},
$$
它等于 (4.1) 中把 $S_{\mathrm{tc}}^2$ 换成其可能的最小值 $(S_{\mathrm{t}} - S_{\mathrm{c}})^2$。$\rho_{\mathrm{tc}} = 1$ 的情形包含常数效应，此时 $Y_i(1)$ 就是 $Y_i(0)$ 平移后的结果。符号的直观是：强正相关意味着 $Y_i(0)$ 高的单元 $Y_i(1)$ 也高；若处理组碰巧含有许多这样的单元，则处理组均值偏高而对照组均值偏低，两个误差使 $\hat\tau^{\mathrm{dif}}$ 朝同一方向偏离。

## 4.4. 估计抽样方差

### 4.4.1. Neyman 方差估计

(4.1) 的每一项都涉及缺失的结果，但前两项可以由两组的样本方差无偏估计：

$$
s_{\mathrm{c}}^2 = \frac{1}{N_{\mathrm{c}} - 1}\sum_{i:W_i = 0}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2, \qquad
s_{\mathrm{t}}^2 = \frac{1}{N_{\mathrm{t}} - 1}\sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2.
$$

**定理 4.4.1** 在 $N_{\mathrm{t}}, N_{\mathrm{c}} \ge 2$ 的 CRE 中，$\mathbb{E}_W[s_{\mathrm{t}}^2] = S_{\mathrm{t}}^2$，$\mathbb{E}_W[s_{\mathrm{c}}^2] = S_{\mathrm{c}}^2$。

**证明** 对处理组，$(N_{\mathrm{t}} - 1)s_{\mathrm{t}}^2 = \sum_i W_iY_i(1)^2 - N_{\mathrm{t}}(\bar Y_{\mathrm{t}}^{\mathrm{obs}})^2$。利用 $\mathbb{E}_W[W_i] = N_{\mathrm{t}}/N$ 与 $\mathbb{E}_W[(\bar Y_{\mathrm{t}}^{\mathrm{obs}})^2] = \bar Y(1)^2 + \left(\frac{1}{N_{\mathrm{t}}} - \frac{1}{N}\right)S_{\mathrm{t}}^2$，

$$
(N_{\mathrm{t}} - 1)\,\mathbb{E}_W\bigl[s_{\mathrm{t}}^2\bigr] = \frac{N_{\mathrm{t}}}{N}\Bigl(\sum_i Y_i(1)^2 - N\bar Y(1)^2\Bigr) - \Bigl(1 - \frac{N_{\mathrm{t}}}{N}\Bigr)S_{\mathrm{t}}^2
= \left(\frac{N_{\mathrm{t}}(N - 1)}{N} - \frac{N - N_{\mathrm{t}}}{N}\right)S_{\mathrm{t}}^2 = (N_{\mathrm{t}} - 1)S_{\mathrm{t}}^2.
$$
对照组同理。$\square$

单元效应的方差 $S_{\mathrm{tc}}^2$ 完全无法估计：它取决于单元内 $Y_i(1)$ 与 $Y_i(0)$ 的配对，而没有任何单元同时给出两者。由于 $S_{\mathrm{tc}}^2 \ge 0$，舍去第三项偏向安全一侧。

**定义 4.4.1（Neyman 方差估计）** $\hat\tau^{\mathrm{dif}}$ 的抽样方差的 **Neyman 方差估计**为

$$
\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = \frac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}}.
$$

**定理 4.4.2** 在 CRE 中，

$$
\mathbb{E}_W\bigl[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}\bigr] = \operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) + \frac{S_{\mathrm{tc}}^2}{N} \ge \operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr),
$$
等号成立当且仅当处理效应为常数。因此 Neyman 方差估计一般是保守的，在常数效应下是无偏的。

**证明** 由定理 4.4.1，$\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] = S_{\mathrm{c}}^2/N_{\mathrm{c}} + S_{\mathrm{t}}^2/N_{\mathrm{t}}$，它比 (4.1) 大 $S_{\mathrm{tc}}^2/N$；这个差恰在所有 $Y_i(1) - Y_i(0)$ 相等时为零。$\square$

使用这一估计量还有第二个理由：把 $\hat\tau^{\mathrm{dif}}$ 视为超总体效应 $\tau_{\mathrm{sp}}$ 的估计量时，它是方差的无偏估计（4.6 节）。因此无论心中的估计目标是哪一个，$\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$ 不是无偏就是保守。

### 4.4.2. 两个替代估计

若效应为常数，则还有 $S_{\mathrm{t}}^2 = S_{\mathrm{c}}^2 = S^2$，两组方差可以合并：

$$
\widehat{\operatorname{Var}}{}^{\mathrm{const}} = s^2\left(\frac{1}{N_{\mathrm{c}}} + \frac{1}{N_{\mathrm{t}}}\right), \qquad
s^2 = \frac{(N_{\mathrm{c}} - 1)s_{\mathrm{c}}^2 + (N_{\mathrm{t}} - 1)s_{\mathrm{t}}^2}{N - 2} = \frac{1}{N - 2}\left(\sum_{i:W_i = 0}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2 + \sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2\right).
$$
这就是等方差两样本 $t$ 检验中的方差估计。在常数效应下，由定理 4.4.1 与推论 4.3.1，它是无偏的。没有这一假定时，它的偏差可正可负；当两组样本量不等且较大的一组方差较小时，它会严重低估方差（思考题 5）。

另一个极端是利用定理 4.3.2 的界，预先指定相关系数，并把总体量换成样本量：

$$
\widehat{\operatorname{Var}}{}^{\rho_{\mathrm{tc}}} = s_{\mathrm{c}}^2\cdot\frac{N_{\mathrm{t}}}{N\cdot N_{\mathrm{c}}} + s_{\mathrm{t}}^2\cdot\frac{N_{\mathrm{c}}}{N\cdot N_{\mathrm{t}}} + \rho_{\mathrm{tc}}\cdot s_{\mathrm{c}}\cdot s_{\mathrm{t}}\cdot\frac{2}{N}.
$$
取 $\rho_{\mathrm{tc}} = 1$ 得到比 Neyman 估计更紧的界，

$$
\widehat{\operatorname{Var}}{}^{\rho = 1} = \frac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{(s_{\mathrm{t}} - s_{\mathrm{c}})^2}{N},
$$
它在大样本下仍然是保守的，因为真实方差不会超过它在 $\rho_{\mathrm{tc}} = 1$ 处的值。（在小样本中只是近似如此，因为 $s_{\mathrm{t}}$、$s_{\mathrm{c}}$ 不是 $S_{\mathrm{t}}$、$S_{\mathrm{c}}$ 的无偏估计。）它只在两组方差不同时才优于 Neyman 估计。

| 估计量 | 公式 | 无偏所需的假定 | 否则 |
|---|---|---|---|
| $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$ | $s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}$ | 常数效应（或估计目标为超总体效应） | 保守，偏差为 $S_{\mathrm{tc}}^2/N$ |
| $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$ | $s^2(1/N_{\mathrm{c}} + 1/N_{\mathrm{t}})$ | 常数效应 | 偏差方向不定 |
| $\widehat{\operatorname{Var}}{}^{\rho = 1}$ | $s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}} - (s_{\mathrm{t}} - s_{\mathrm{c}})^2/N$ | $\rho_{\mathrm{tc}} = 1$ | 大样本下保守 |

Neyman 估计是标准的选择：它简单，不要求效应为常数，而且对超总体估计目标而言，其保守性消失。

## 4.5. 置信区间与检验

### 4.5.1. 置信区间

由**有限总体中心极限定理**（定理 3.3.3，应用于两组均值构成的向量），$\hat\tau^{\mathrm{dif}}$ 的随机化分布在大样本下近似正态，均值为 $\tau_{\mathrm{fs}}$，方差为 (4.1)。把方差换成一个估计 $\widehat{\operatorname{Var}}$（例如 Neyman 估计），得到大样本**置信区间**

$$
\mathrm{CI}^{1 - \alpha}(\tau_{\mathrm{fs}}) = \left(\hat\tau^{\mathrm{dif}} - z_{\alpha/2}\sqrt{\widehat{\operatorname{Var}}},\ \hat\tau^{\mathrm{dif}} + z_{\alpha/2}\sqrt{\widehat{\operatorname{Var}}}\right),
$$
其中 $z_{\alpha/2}$ 是标准正态分布的上 $\alpha/2$ 分位数；$90\%$ 区间取 $z_{0.05} = 1.645$。由于 Neyman 估计平均而言高估方差，该区间在大样本下对 $\tau_{\mathrm{fs}}$ 的覆盖概率至少为 $1 - \alpha$；效应为常数时则恰好如此。Neyman 区间是有效的（达到名义覆盖率），并且在数据所允许的范围内是高效的，因为多出的宽度只来自不可识别的 $S_{\mathrm{tc}}^2$。

### 4.5.2. 弱原假设的检验

Neyman 的框架同样给出检验，但所检验的假设与 Fisher 的不同。要检验平均效应为零，

$$
H_0\colon\ \tau_{\mathrm{fs}} = \frac{1}{N}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0)\bigr) = 0 \quad \text{对} \quad H_a\colon\ \tau_{\mathrm{fs}} \ne 0,
$$
使用 $t$ 统计量

$$
t = \frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}}}
$$
及由正态近似得到的 p 值 $2(1 - \Phi(\lvert t\rvert))$。该检验对弱原假设有效——弱原假设允许单元效应各不相同，只要平均为零——并且是近似检验，在大样本下才成立。[3.9.3](/3.9.3) 的 Fisher 检验是精确的，但检验的是尖锐原假设；就统计量 $T^{\text{t-stat}}$ 而言，两种检验使用数据的同一个函数，但与不同的参照分布比较。

| | Neyman | Fisher |
|---|---|---|
| 原假设 | $\tau_{\mathrm{fs}} = 0$（弱） | 对所有 $i$，$Y_i(1) = Y_i(0)$（尖锐） |
| 统计量 | $t = \hat\tau^{\mathrm{dif}}/\sqrt{\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}}$ | 任意，如 $T^{\mathrm{dif}}$ |
| 参照分布 | 标准正态（大样本） | 精确的随机化分布 |
| 有效性 | 近似，允许效应异质 | 精确，但仅在尖锐原假设下 |

**例 4.5.1** 对蜂蜜数据（咳嗽频率），$\hat\tau^{\mathrm{dif}} = -0.697$，三种方差估计都约为 $0.139$：两组样本量相近（$35$ 与 $37$），样本方差也相近，所以合并几乎没有改变，修正项 $(s_{\mathrm{t}} - s_{\mathrm{c}})^2/N$ 可以忽略。标准误为 $\sqrt{0.139} \approx 0.373$，$90\%$ 置信区间为

$$
-0.697 \pm 1.645 \times 0.373 \approx [-1.31, -0.08].
$$
$t$ 统计量为 $-0.697/0.373 \approx -1.87$，双侧 p 值为 $0.062$。用 $T^{\mathrm{dif}}$ 的 Fisher 精确检验给出 $0.067$。两种方法吻合得很好，尽管它们检验的假设不同：在 $10\%$ 水平上两者都拒绝"无效应"，在 $5\%$ 水平上两者都不拒绝。

## 4.6. 超总体

### 4.6.1. 两层随机性

现在把 $N$ 个单元看作来自无穷超总体的简单随机样本（[3.9.2](/3.9.2)），并对它们用 CRE 分配处理。于是有两层随机性：从超总体中抽取单元，以及把处理随机分配给被抽中的单元。估计目标是超总体平均处理效应

$$
\tau_{\mathrm{sp}} = \mathbb{E}_{\mathrm{sp}}\bigl[Y_i(1) - Y_i(0)\bigr],
$$
相关的总体方差为

$$
\sigma_{\mathrm{c}}^2 = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(0)\bigr), \qquad
\sigma_{\mathrm{t}}^2 = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(1)\bigr), \qquad
\sigma_{\mathrm{tc}}^2 = \operatorname{Var}_{\mathrm{sp}}\bigl(Y_i(1) - Y_i(0)\bigr).
$$
有限样本效应 $\tau_{\mathrm{fs}}$ 现在是随机变量：它是 $N$ 个独立同分布的单元效应的平均，$\mathbb{E}_{\mathrm{sp}}[\tau_{\mathrm{fs}}] = \tau_{\mathrm{sp}}$，$\operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}}) = \sigma_{\mathrm{tc}}^2/N$。

### 4.6.2. 无偏性与方差

**定理 4.6.1** 设 $N$ 个单元是来自超总体的随机样本，处理由 CRE 分配。则

$$
\mathbb{E}_{\mathrm{sp}}\bigl[\hat\tau^{\mathrm{dif}}\bigr] = \tau_{\mathrm{sp}}, \qquad
\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}},
$$
且 Neyman 方差估计是该方差的无偏估计：$\mathbb{E}_{\mathrm{sp}}[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] = \operatorname{Var}_{\mathrm{sp}}(\hat\tau^{\mathrm{dif}})$。

**证明** 对样本取条件，即对这 $N$ 个单元的潜在结果取条件。给定样本时，分配是 CRE，因此定理 4.2.1、4.3.1 与 4.4.1 在条件意义下成立。由**全期望公式**，

$$
\mathbb{E}_{\mathrm{sp}}\bigl[\hat\tau^{\mathrm{dif}}\bigr] = \mathbb{E}_{\mathrm{sp}}\Bigl[\mathbb{E}_W\bigl[\hat\tau^{\mathrm{dif}} \bigm| \boldsymbol{Y}(0), \boldsymbol{Y}(1)\bigr]\Bigr] = \mathbb{E}_{\mathrm{sp}}[\tau_{\mathrm{fs}}] = \tau_{\mathrm{sp}}.
$$
由**全方差公式**（[3.1.9](/3.1.9#thm-9.4.1)），

$$
\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \mathbb{E}_{\mathrm{sp}}\Bigl[\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}} \bigm| \boldsymbol{Y}(0), \boldsymbol{Y}(1)\bigr)\Bigr] + \operatorname{Var}_{\mathrm{sp}}\Bigl(\mathbb{E}_W\bigl[\hat\tau^{\mathrm{dif}} \bigm| \boldsymbol{Y}(0), \boldsymbol{Y}(1)\bigr]\Bigr)
= \mathbb{E}_{\mathrm{sp}}\left[\frac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{S_{\mathrm{tc}}^2}{N}\right] + \operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}}).
$$
有限总体方差 $S_{\mathrm{c}}^2$、$S_{\mathrm{t}}^2$、$S_{\mathrm{tc}}^2$ 是 $N$ 个独立同分布样本的样本方差（除数为 $N - 1$），所以它们的期望分别是 $\sigma_{\mathrm{c}}^2$、$\sigma_{\mathrm{t}}^2$、$\sigma_{\mathrm{tc}}^2$。再由 $\operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}}) = \sigma_{\mathrm{tc}}^2/N$，

$$
\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{\sigma_{\mathrm{tc}}^2}{N} + \frac{\sigma_{\mathrm{tc}}^2}{N} = \frac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}}.
$$
最后，$\mathbb{E}_{\mathrm{sp}}[s_{\mathrm{t}}^2] = \mathbb{E}_{\mathrm{sp}}[\mathbb{E}_W[s_{\mathrm{t}}^2 \mid \boldsymbol{Y}(1)]] = \mathbb{E}_{\mathrm{sp}}[S_{\mathrm{t}}^2] = \sigma_{\mathrm{t}}^2$，对照组同理，所以 $\mathbb{E}_{\mathrm{sp}}[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] = \sigma_{\mathrm{c}}^2/N_{\mathrm{c}} + \sigma_{\mathrm{t}}^2/N_{\mathrm{t}}$。$\square$

等价地，估计量与 $\tau_{\mathrm{sp}}$ 的偏差分解为两个不相关的部分，

$$
\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{sp}} = \bigl(\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}}\bigr) + \bigl(\tau_{\mathrm{fs}} - \tau_{\mathrm{sp}}\bigr);
$$
交叉项的期望为零，因为第一部分在给定样本时条件均值为零。第一部分是分配造成的误差，其方差平均为 $\sigma_{\mathrm{c}}^2/N_{\mathrm{c}} + \sigma_{\mathrm{t}}^2/N_{\mathrm{t}} - \sigma_{\mathrm{tc}}^2/N$；第二部分是抽样造成的误差，方差为 $\sigma_{\mathrm{tc}}^2/N$。

### 4.6.3. 解释

定理 4.6.1 解开了保守方差估计之谜。Neyman 估计高估有限样本方差的量 $S_{\mathrm{tc}}^2/N$，平均而言恰好等于有限样本效应围绕超总体效应的方差 $\sigma_{\mathrm{tc}}^2/N$。若目标是 $\tau_{\mathrm{sp}}$，该估计量是无偏的；若目标是 $\tau_{\mathrm{fs}}$，手头的单元是固定的，没有抽样变异，同一估计量就是保守的。估计实验中这 $N$ 个单元的效应，比估计它们所来自的总体的效应更容易，两者之差正是效应的异质性：效应为常数时，$\tau_{\mathrm{fs}} = \tau_{\mathrm{sp}}$，两个方差重合。实践中两种估计目标使用同一个区间 $\hat\tau^{\mathrm{dif}} \pm z_{\alpha/2}\sqrt{\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}}$；它对 $\tau_{\mathrm{sp}}$ 近似精确，对 $\tau_{\mathrm{fs}}$ 则是保守的。

![对一个固定的、含 100 个单元的模拟有限总体：均值差的随机化分布，以及由真实方差和 Neyman 方差估计的期望所对应的正态密度；随单元效应异质性增大，真实抽样方差与 Neyman 估计和 rho = 1 估计的期望；以及名义 95% 的 Neyman 区间对有限样本效应的覆盖率](./plots/neyman_variance.py)

该图说明有限样本的结果。效应为常数（异质性为零）时，Neyman 估计是无偏的，区间达到名义覆盖率。随着单元效应越来越异质，真实方差比 Neyman 估计的期望低 $S_{\mathrm{tc}}^2/N$，而区间对 $\tau_{\mathrm{fs}}$ 的覆盖率升至 $95\%$ 以上。当两个潜在结果分布的离散程度不同时，$\rho = 1$ 估计去掉了一部分多余的宽度。

这一方法有一个局限，它决定了后续章节的内容：它不使用协变量。当处理前变量能预测结果时，它们可以大幅降低方差，正如 [3.9.3](/3.9.3) 中增益得分统计量对 Fisher 检验所做的那样。把协变量纳入估计是 [3.9.5](/3.9.5)（回归）与 [3.9.7](/3.9.7)（分层）的主题。

## 小结

| | 有限样本 | 超总体 |
|---|---|---|
| 估计目标 | $\tau_{\mathrm{fs}} = \bar Y(1) - \bar Y(0)$ | $\tau_{\mathrm{sp}} = \mathbb{E}_{\mathrm{sp}}[Y_i(1) - Y_i(0)]$ |
| 随机性 | 分配 | 抽样与分配 |
| 估计量 | $\hat\tau^{\mathrm{dif}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$，无偏（定理 4.2.1） | 同左，无偏（定理 4.6.1） |
| 方差 | $\dfrac{S_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \dfrac{S_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \dfrac{S_{\mathrm{tc}}^2}{N}$（定理 4.3.1） | $\dfrac{\sigma_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \dfrac{\sigma_{\mathrm{t}}^2}{N_{\mathrm{t}}}$（定理 4.6.1） |
| 方差估计量 | $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = \dfrac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \dfrac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}}$，保守，偏差为 $S_{\mathrm{tc}}^2/N$（定理 4.4.2） | 同左，无偏 |
| 区间 | $\hat\tau^{\mathrm{dif}} \pm z_{\alpha/2}\sqrt{\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}}$，覆盖率 $\ge 1 - \alpha$ | 同左，覆盖率 $\approx 1 - \alpha$ |

- 方差定理的证明用到 $D_i = W_i - N_{\mathrm{t}}/N$，其中 $\operatorname{Var}_W(W_i) = N_{\mathrm{t}}N_{\mathrm{c}}/N^2$，$\operatorname{Cov}_W(W_i, W_j) = -N_{\mathrm{t}}N_{\mathrm{c}}/(N^2(N - 1))$（引理 4.3.1）。
- 以潜在结果的相关系数 $\rho_{\mathrm{tc}}$ 表示，方差关于 $\rho_{\mathrm{tc}}$ 递增（定理 4.3.2）；$\rho_{\mathrm{tc}} = 1$ 给出可识别的最紧上界及估计量 $\widehat{\operatorname{Var}}{}^{\rho = 1}$；在常数效应下，合并估计 $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$ 是无偏的。
- Neyman 检验针对弱原假设 $\tau_{\mathrm{fs}} = 0$，是近似的；Fisher 检验针对尖锐原假设，是精确的。蜂蜜数据：$\hat\tau = -0.697$，方差约 $0.139$，$90\%$ 区间 $[-1.31, -0.08]$，p 值为 $0.062$（Neyman）与 $0.067$（Fisher）。

## 思考题

1. 三个单元有 $Y(0) = (0, 2, 4)$，$Y(1) = (1, 2, 6)$，随机选其中一个接受处理（$N_{\mathrm{t}} = 1$）。列出 $\hat\tau^{\mathrm{dif}}$ 的三个可能取值，并验证定理 4.2.1 与 4.3.1。

   **答** 处理单元 1：$1 - (2 + 4)/2 = -2$；单元 2：$2 - (0 + 4)/2 = 0$；单元 3：$6 - (0 + 2)/2 = 5$。平均值为 $1 = \tau_{\mathrm{fs}}$，因为各单元效应为 $(1, 0, 2)$。三种分配下的方差为 $\frac{1}{3}[(-3)^2 + (-1)^2 + 4^2] = 26/3$。由公式：$S_{\mathrm{c}}^2 = 4$，$S_{\mathrm{t}}^2 = \frac{1}{2}[(1 - 3)^2 + (2 - 3)^2 + (6 - 3)^2] = 7$，$S_{\mathrm{tc}}^2 = 1$，而 $4/2 + 7/1 - 1/3 = 26/3$。
2. 证明 $\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) \ge \frac{(S_{\mathrm{c}}\sqrt{N_{\mathrm{t}}/N_{\mathrm{c}}} - S_{\mathrm{t}}\sqrt{N_{\mathrm{c}}/N_{\mathrm{t}}})^2}{N}$，即 $\rho_{\mathrm{tc}} = -1$ 处的值。这个下界何时为零？这意味着什么？

   **答** 在 $\rho_{\mathrm{tc}} = -1$ 处，定理 4.3.2 给出 $\frac{1}{N}\bigl[S_{\mathrm{c}}^2\frac{N_{\mathrm{t}}}{N_{\mathrm{c}}} + S_{\mathrm{t}}^2\frac{N_{\mathrm{c}}}{N_{\mathrm{t}}} - 2S_{\mathrm{c}}S_{\mathrm{t}}\bigr] = \frac{1}{N}\bigl(S_{\mathrm{c}}\sqrt{N_{\mathrm{t}}/N_{\mathrm{c}}} - S_{\mathrm{t}}\sqrt{N_{\mathrm{c}}/N_{\mathrm{t}}}\bigr)^2$，而方差关于 $\rho_{\mathrm{tc}}$ 递增。当 $S_{\mathrm{c}}N_{\mathrm{t}} = S_{\mathrm{t}}N_{\mathrm{c}}$ 且潜在结果完全负相关时它为零；此时 $a_i = Y_i(1)/N_{\mathrm{t}} + Y_i(0)/N_{\mathrm{c}}$ 为常数，因此每种分配都恰好给出 $\hat\tau^{\mathrm{dif}} = \tau_{\mathrm{fs}}$。
3. 由定理 4.3.2 推导 $\widehat{\operatorname{Var}}{}^{\rho = 1}$，并证明它不大于 $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$。

   **答** 取 $\rho_{\mathrm{tc}} = 1$ 并把 $S$ 换成 $s$：$s_{\mathrm{c}}^2\frac{N_{\mathrm{t}}}{NN_{\mathrm{c}}} + s_{\mathrm{t}}^2\frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}} + \frac{2s_{\mathrm{c}}s_{\mathrm{t}}}{N} = s_{\mathrm{c}}^2\bigl(\frac{1}{N_{\mathrm{c}}} - \frac{1}{N}\bigr) + s_{\mathrm{t}}^2\bigl(\frac{1}{N_{\mathrm{t}}} - \frac{1}{N}\bigr) + \frac{2s_{\mathrm{c}}s_{\mathrm{t}}}{N} = \frac{s_{\mathrm{c}}^2}{N_{\mathrm{c}}} + \frac{s_{\mathrm{t}}^2}{N_{\mathrm{t}}} - \frac{(s_{\mathrm{t}} - s_{\mathrm{c}})^2}{N}$。减去的项非负，所以 $\widehat{\operatorname{Var}}{}^{\rho = 1} \le \widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$，当 $s_{\mathrm{t}} = s_{\mathrm{c}}$ 时取等号。
4. 证明在 CRE 中两个组均值的协方差为 $\operatorname{Cov}_W(\bar Y_{\mathrm{t}}^{\mathrm{obs}}, \bar Y_{\mathrm{c}}^{\mathrm{obs}}) = -S_{01}/N$，其中 $S_{01}$ 是 $Y_i(1)$ 与 $Y_i(0)$ 的有限总体协方差，并据此给出定理 4.3.1 的第二个证明。

   **答** $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y(1) = \frac{1}{N_{\mathrm{t}}}\sum_i D_iY_i(1)$，$\bar Y_{\mathrm{c}}^{\mathrm{obs}} - \bar Y(0) = -\frac{1}{N_{\mathrm{c}}}\sum_i D_iY_i(0)$。由引理 4.3.1 的双线性形式，$\operatorname{Cov}_W(\sum_i D_ia_i, \sum_i D_ib_i) = \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}S_{ab}$，所以协方差为 $-\frac{1}{N_{\mathrm{t}}N_{\mathrm{c}}}\cdot\frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}S_{01} = -S_{01}/N$。于是 $\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) = (\frac{1}{N_{\mathrm{t}}} - \frac{1}{N})S_{\mathrm{t}}^2 + (\frac{1}{N_{\mathrm{c}}} - \frac{1}{N})S_{\mathrm{c}}^2 + \frac{2S_{01}}{N}$，代入 $2S_{01} = S_{\mathrm{t}}^2 + S_{\mathrm{c}}^2 - S_{\mathrm{tc}}^2$ 即得 (4.1)。
5. 某 CRE 中 $N = 100$，$N_{\mathrm{t}} = 10$，$S_{\mathrm{t}}^2 = 4$，$S_{\mathrm{c}}^2 = 1$。计算真实方差的一个上界，以及 $\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}$ 与 $\widehat{\operatorname{Var}}{}^{\mathrm{const}}$ 的期望。你得出什么结论？

   **答** $S_{\mathrm{tc}}^2 \ge (S_{\mathrm{t}} - S_{\mathrm{c}})^2 = 1$，所以方差至多为 $1/90 + 4/10 - 1/100 \approx 0.401$。$\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] = 1/90 + 4/10 \approx 0.411$，略显保守。$\mathbb{E}_W[s^2] = (89 \times 1 + 9 \times 4)/98 \approx 1.276$，所以 $\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{const}}] \approx 1.276\,(1/90 + 1/10) \approx 0.142$，约为真实方差的三分之一。当较小的一组方差较大时，合并估计（即等方差 $t$ 检验所用的估计）严重反保守；基于它的区间会窄得多。
6. 在均衡的 CRE（$N_{\mathrm{t}} = N_{\mathrm{c}} = N/2$）中，若 $\sigma_{\mathrm{c}} = \sigma_{\mathrm{t}} = 1$，要使 $95\%$ Neyman 区间的半宽不超过 $0.2$，至少需要多少个单元？

   **答** 超总体方差为 $2/(N/2) \cdot 1 = 4/N$，所以半宽为 $1.96 \times 2/\sqrt N \le 0.2$，得 $\sqrt N \ge 19.6$，即 $N \ge 385$；两组样本量取偶数，故 $N = 386$。
7. 在超总体设定下，计算 $\operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}})$，并解释为什么 $\operatorname{Var}_{\mathrm{sp}}(\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}})$ 恰好比 $\operatorname{Var}_{\mathrm{sp}}(\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{sp}})$ 小这个量。

   **答** $\tau_{\mathrm{fs}}$ 是 $N$ 个方差为 $\sigma_{\mathrm{tc}}^2$ 的独立同分布单元效应的均值，所以 $\operatorname{Var}_{\mathrm{sp}}(\tau_{\mathrm{fs}}) = \sigma_{\mathrm{tc}}^2/N$。把 $\hat\tau - \tau_{\mathrm{sp}}$ 写成 $(\hat\tau - \tau_{\mathrm{fs}}) + (\tau_{\mathrm{fs}} - \tau_{\mathrm{sp}})$，两项不相关，因为 $\mathbb{E}_W[\hat\tau - \tau_{\mathrm{fs}} \mid \text{样本}] = 0$，而第二项是样本的函数。因此方差相加，差为 $\sigma_{\mathrm{tc}}^2/N$。
8. 解释为什么 Neyman 对 $\tau_{\mathrm{fs}} = 0$ 的检验可以拒绝，而 Fisher 对尖锐原假设的精确检验却不拒绝，并说明为什么相反的情形也可能发生。

   **答** 两种检验用相近的统计量与不同的参照分布比较，两者只是近似可比。Neyman 检验使用正态近似，在小样本或结果偏斜时可能过于乐观，因此可能在精确随机化分布不拒绝时拒绝。反过来，Fisher 检验若采用均值差以外的统计量（例如秩或增益得分），可能对真实成立的备择假设更有功效，从而拒绝尖锐原假设，而均值差并不显著；符号相反的效应还会使尖锐原假设不成立而 $\tau_{\mathrm{fs}} \approx 0$，$T^{\mathrm{ks}}$ 这类分布型统计量能够检出这种情形，而 Neyman 检验按其设计无法检出。
