---
title: 观察性研究的分析：分块、加权与匹配估计量
description: 正则分配机制下观察性研究的分析阶段。彩票数据；线性结果模型下均值差的偏差及分块对它的削减；分块与块内回归相结合，估计平均效应与处理组平均效应及其方差；分块作为以粗化倾向评分加权；最低工资数据与不放回、放回、多重匹配的匹配估计量，及其偏差与偏差校正匹配；所有估计量共有的线性结构与条件方差；完整的设计与分析流程。
source_hash: e4c89c4289b1
---

在 [3.9.9](/3.9.9) 的设计阶段之后，我们得到一个样本（可能经过修剪），其中处理组与对照组的单位被安排在倾向评分相近的区组中，或协变量相近的匹配集中。分析阶段则利用结果变量来估计平均因果效应。本章所有估计量都建立在无混杂性之上，即**正则分配机制**（[3.9.8](/3.9.8)）的假设；它们的区别在于如何消除协变量上仍然存在的差异。本章的要旨是：设计与分析互为补充。分块或匹配消除了大部分不平衡，因此块内或匹配对内的回归调整只需修正很小的差异，不再强烈依赖函数形式。我们先在彩票数据上研究分块估计量（§10.1–10.2），再把分块与加权联系起来（§10.3），在最低工资数据上研究匹配估计量（§10.4），最后讨论所有这些估计量的方差（§10.5）与完整的工作流程（§10.6）。

与 [3.9.8](/3.9.8) 相同，这里的单位是来自超总体的随机样本；$\mu_w(x) = \mathbb{E}[Y_i(w) \mid X_i = x]$ 与 $\sigma_w^2(x) = \operatorname{Var}(Y_i(w) \mid X_i = x)$ 分别表示潜在结果的条件均值与条件方差，在无混杂性下 $\mu_w(x) = \mathbb{E}[Y_i^{\mathrm{obs}} \mid W_i = w, X_i = x]$。

## 10.1. 彩票数据

**例 10.1.1（彩票中奖者与劳动供给）** Imbens、Rubin 与 Sacerdote（2001）研究了非劳动收入对经济行为（包括劳动供给、消费与储蓄）的影响。他们调查了购买过马萨诸塞州彩票的人。处理组是"中奖者"，他们赢得了按年分期支付的大额奖金；对照组是"未中奖者"，他们同样买过彩票，但只赢得小额奖金。这里考察的结果变量是中奖后六年的年均劳动收入（单位为千美元），协变量包括购买的彩票张数、受教育程度、中奖时是否有工作，以及中奖前几年的收入。

在购买彩票的人当中，是否中奖是随机的，但分析样本并不是随机化实验：中奖者与未中奖者的调查应答率不同，两组在协变量上也有差异，例如购买的彩票张数既与中奖机会有关，也与收入有关。在给定协变量的无混杂性下，分析沿用 [3.9.9](/3.9.9) 的设计。倾向评分用 logistic 回归估计，变量按 [3.9.8](/3.9.8) 的三步法选择，496 个单位的样本被修剪到满足 $0.0891 \le \hat e(X_i) \le 0.9109$ 的单位：

| | $\hat e(X_i) < 0.0891$ | $0.0891 \le \hat e(X_i) \le 0.9109$ | $\hat e(X_i) > 0.9109$ | 合计 |
|---|---|---|---|---|
| 未中奖者 | 82 | 172 | 5 | 259 |
| 中奖者 | 4 | 151 | 82 | 237 |
| 合计 | 86 | 323 | 87 | 496 |

修剪阈值 $0.0891$ 由 [3.9.9](/3.9.9) 的方差最小化规则给出。余下的 323 个单位按算法 9.4.1 的递归分割划分为五个区组，分别含 80、40、41、81 和 81 个单位。

:::

## 10.2. 分块估计量

### 10.2.1. 均值差的偏差

为了看清分块的作用，暂且假设潜在结果的条件均值服从线性模型，且平均效应为常数：

$$
\mu_w(x) = \mathbb{E}\bigl[Y_i(w) \mid X_i = x\bigr] = \alpha + \tau_{\mathrm{sp}}w + x\boldsymbol{\beta}, \qquad w = 0, 1.
$$

**定理 10.2.1（均值差的偏差）** 在无混杂性与上述线性模型下，均值差估计量 $\hat\tau^{\mathrm{dif}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$ 的条件偏差为

$$
\mathbb{E}\bigl[\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr] = (\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta},
$$
其中 $\bar X_{\mathrm{t}}$ 与 $\bar X_{\mathrm{c}}$ 分别是处理组与对照组单位的协变量均值。

**证明** 写出

$$
\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} = \left(\frac{1}{N_{\mathrm{t}}}\sum_{i=1}^{N}W_iY_i(1) - \frac{1}{N}\sum_{i=1}^{N}Y_i(1)\right) - \left(\frac{1}{N_{\mathrm{c}}}\sum_{i=1}^{N}(1 - W_i)Y_i(0) - \frac{1}{N}\sum_{i=1}^{N}Y_i(0)\right).
$$
各单位相互独立，因此 $Y_i(w)$ 在给定 $(\boldsymbol{X}, \boldsymbol{W})$ 下的条件期望只依赖于 $(X_i, W_i)$，又由无混杂性，$\mathbb{E}[Y_i(w) \mid X_i, W_i] = \mathbb{E}[Y_i(w) \mid X_i] = \mu_w(X_i)$。对第一个括号，处理组单位贡献 $(\frac{1}{N_{\mathrm{t}}} - \frac{1}{N})\mu_1(X_i) = \frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}\mu_1(X_i)$，对照组单位贡献 $-\frac{1}{N}\mu_1(X_i)$，所以它的条件期望为

$$
\frac{N_{\mathrm{c}}}{N}\left(\frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\mu_1(X_i) - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\mu_1(X_i)\right) = \frac{N_{\mathrm{c}}}{N}\Bigl[(\alpha + \tau_{\mathrm{sp}} + \bar X_{\mathrm{t}}\boldsymbol{\beta}) - (\alpha + \tau_{\mathrm{sp}} + \bar X_{\mathrm{c}}\boldsymbol{\beta})\Bigr] = \frac{N_{\mathrm{c}}}{N}(\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta}.
$$
同理，第二个括号的条件期望为 $\frac{N_{\mathrm{t}}}{N}(\bar X_{\mathrm{c}} - \bar X_{\mathrm{t}})\boldsymbol{\beta}$。两式相减，

$$
\mathbb{E}\bigl[\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr] = \frac{N_{\mathrm{c}}}{N}(\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta} - \frac{N_{\mathrm{t}}}{N}(\bar X_{\mathrm{c}} - \bar X_{\mathrm{t}})\boldsymbol{\beta} = (\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta}. \qquad \square
$$

偏差是协变量不平衡与协变量对结果影响的乘积，其结构与回归中的**遗漏变量偏差**（[3.3.10](/3.3.10)）相同。在完全随机化实验中 $\mathbb{E}[\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}}] = 0$，偏差平均为零；在观察性研究中它可能很大。该估计量忽略了设计阶段构造的区组结构，因此要付出代价。

### 10.2.2. 分块

基本的分块（子类化）估计量把每个区组当作完全随机化实验来分析，再以区组比例 $q(j) = N(j)/N$ 为权重对各区组的估计取平均，与 [3.9.7](/3.9.7) 的分层估计量完全一致：

$$
\hat\tau^{\mathrm{strat}} = \sum_{j=1}^{J}q(j)\,\hat\tau^{\mathrm{dif}}(j), \qquad \hat\tau^{\mathrm{dif}}(j) = \bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - \bar Y_{\mathrm{c}}^{\mathrm{obs}}(j).
$$
在每个区组内应用定理 10.2.1，得到：

**推论 10.2.1（分块估计量的偏差）** 在定理 10.2.1 的假设下，

$$
\mathbb{E}\bigl[\hat\tau^{\mathrm{dif}}(j) - \tau_{\mathrm{fs}}(j) \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr] = \bigl(\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j)\bigr)\boldsymbol{\beta}, \qquad \mathbb{E}\bigl[\hat\tau^{\mathrm{strat}} - \tau_{\mathrm{fs}} \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr] = \left(\sum_{j=1}^{J}q(j)\bigl(\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j)\bigr)\right)\boldsymbol{\beta},
$$
其中 $\tau_{\mathrm{fs}}(j)$ 是区组 $j$ 内的平均效应，$\tau_{\mathrm{fs}} = \sum_j q(j)\tau_{\mathrm{fs}}(j)$。

区组本来就是为平衡协变量而构造的，所以块内差 $\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j)$ 远小于总体差，偏差也随之减小。但偏差不会消失：区组有一定宽度，块内处理组单位的倾向评分仍然倾向于略高，协变量因而略有不同。

### 10.2.3. 分块与回归

块内剩余的不平衡很小，因此在每个区组内做回归即可消除它，而不必过多依赖线性形式。在区组 $j$ 中拟合局部线性模型

$$
Y_i^{\mathrm{obs}} = \alpha(j) + \tau(j)W_i + X_i\boldsymbol{\beta}(j) + \varepsilon_i,
$$
用该区组内的单位做最小二乘，

$$
\bigl(\hat\alpha(j), \hat\tau^{\mathrm{adj}}(j), \hat{\boldsymbol{\beta}}(j)\bigr) = \arg\min_{\alpha, \tau, \boldsymbol{\beta}}\sum_{i=1}^{N}B_i(j)\bigl(Y_i^{\mathrm{obs}} - \alpha - \tau W_i - X_i\boldsymbol{\beta}\bigr)^2,
$$
再合并各区组的估计：

$$
\hat\tau^{\mathrm{strat,adj}} = \sum_{j=1}^{J}q(j)\,\hat\tau^{\mathrm{adj}}(j), \qquad \hat\tau_{\mathrm{t}}^{\mathrm{strat,adj}} = \sum_{j=1}^{J}\frac{N_{\mathrm{t}}(j)}{N_{\mathrm{t}}}\,\hat\tau^{\mathrm{adj}}(j).
$$
第二个版本以各区组内处理组单位的比例为权重，估计的是另一个估计目标，即**处理组平均处理效应**。若线性模型在每个区组内成立，回归会完全消除偏差 $(\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j))\boldsymbol{\beta}$；若只是近似成立，误差就是设定误差与一个很小的不平衡之积，是二阶小量。这就是为什么回归在观察性研究的原始样本上不可靠（[3.9.8](/3.9.8)，§8.3.2），而在分块之后变得可靠。各区组的系数 $\boldsymbol{\beta}(j)$ 也可以不同，这允许协变量的效应随倾向评分而变化。

### 10.2.4. 方差

在区组 $j$ 内，均值差的方差用 [3.9.4](/3.9.4) 的 Neyman 公式 $\widehat{\operatorname{Var}}(j) = s_{\mathrm{c}}^2(j)/N_{\mathrm{c}}(j) + s_{\mathrm{t}}^2(j)/N_{\mathrm{t}}(j)$ 估计；回归估计 $\hat\tau^{\mathrm{adj}}(j)$ 的方差则用通常的（最好是异方差稳健的）最小二乘方差。各区组互不相交，估计在给定条件下相互独立，所以

$$
\widehat{\operatorname{Var}}\bigl(\hat\tau^{\mathrm{strat}}\bigr) = \sum_{j=1}^{J}q(j)^2\,\widehat{\operatorname{Var}}(j), \qquad \widehat{\operatorname{Var}}\bigl(\hat\tau_{\mathrm{t}}^{\mathrm{strat,adj}}\bigr) = \sum_{j=1}^{J}\left(\frac{N_{\mathrm{t}}(j)}{N_{\mathrm{t}}}\right)^2\widehat{\operatorname{Var}}\bigl(\hat\tau^{\mathrm{adj}}(j)\bigr),
$$
$\hat\tau^{\mathrm{strat,adj}}$ 的方差类似。这些公式把区组视为固定，并忽略了倾向评分的估计；§10.5 将更一般地讨论方差。

### 10.2.5. 彩票数据的结果

**例 10.2.1（彩票数据的分块与回归）** 在五个区组内，均值差与带四个协变量（彩票张数、受教育程度、中奖时是否有工作、中奖前一年的收入）的回归估计分别为：

| 区组 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $N(j)$ | 80 | 40 | 41 | 81 | 81 |
| $\hat\tau^{\mathrm{dif}}(j)$（标准误） | $-10.82$ ($4.70$) | $2.07$ ($5.10$) | $-1.17$ ($4.97$) | $-9.43$ ($3.23$) | $-2.89$ ($3.59$) |
| $\hat\tau^{\mathrm{adj}}(j)$（标准误） | $-6.21$ ($4.01$) | $-6.51$ ($3.86$) | $-4.81$ ($3.87$) | $-5.88$ ($1.82$) | $-2.56$ ($2.39$) |

调整使各区组的估计发生很大变化，并且使它们更加一致。由此可见两点：协变量确实影响结果（中奖前一年收入的系数在每个区组都在 $0.6$ 到 $0.85$ 之间），而且区组内的协变量仍有足够的差异，使调整产生影响。对不同样本、区组数与协变量集合，总体估计为：

| 回归中的协变量 | 全样本，1 块 | 修剪后，1 块 | 修剪后，2 块 | 修剪后，5 块 |
|---|---|---|---|---|
| 无 | $-6.2$ ($1.4$) | $-6.6$ ($1.7$) | $-6.0$ ($1.9$) | $-5.7$ ($2.0$) |
| 四个协变量 | $-2.8$ ($0.9$) | $-4.0$ ($1.1$) | $-5.6$ ($1.2$) | $-5.1$ ($1.2$) |
| 全部协变量 | $-5.1$ ($1.0$) | $-5.3$ ($1.1$) | $-6.4$ ($1.1$) | $-5.7$ ($1.1$) |

在不分块的全样本上，估计值随回归中纳入的协变量不同而在 $-6.2$ 到 $-2.8$ 之间变动：结论由模型设定所左右。修剪并分成五块之后，三种设定给出 $-5.7$、$-5.1$ 与 $-5.7$。修剪与分块都大大降低了对回归设定的敏感性，三者结合（修剪、分块与回归）给出可信的估计：赢得大额奖金会使此后几年的年劳动收入减少约 $5000$ 到 $6000$ 美元。

:::

## 10.3. 加权估计量及其与分块的关系

[3.9.8](/3.9.8) 的 **Horvitz–Thompson 估计量**（定义 8.3.1）用单位实际接受的处理的概率的倒数对其加权：处理组单位为 $1/e(X_i)$，对照组单位为 $1/(1 - e(X_i))$。用真实的倾向评分时它是无偏的；用估计的倾向评分时，若倾向评分模型正确，**逆概率加权**是相合的。事实上，分块估计量就是一种伪装的加权估计量。

**定理 10.3.1（分块即加权）** 基本分块估计量可以写成

$$
\hat\tau^{\mathrm{strat}} = \frac{1}{N}\sum_{i=1}^{N}W_i\lambda_i^{\mathrm{strat}}Y_i^{\mathrm{obs}} - \frac{1}{N}\sum_{i=1}^{N}(1 - W_i)\lambda_i^{\mathrm{strat}}Y_i^{\mathrm{obs}}, \qquad \lambda_i^{\mathrm{strat}} = \begin{cases} \sum_{j}B_i(j)\,\dfrac{1}{1 - \tilde e(j)}, & W_i = 0, \\[2ex] \sum_{j}B_i(j)\,\dfrac{1}{\tilde e(j)}, & W_i = 1, \end{cases}
$$
其中 $\tilde e(j) = N_{\mathrm{t}}(j)/N(j)$ 是区组 $j$ 中处理组单位的比例。因此它就是把倾向评分换成逐块粗化的倾向评分 $\tilde e(j)$ 的加权估计量。

**证明** 在区组 $j$ 中，

$$
q(j)\,\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) = \frac{N(j)}{N}\cdot\frac{1}{N_{\mathrm{t}}(j)}\sum_{i:W_i = 1}B_i(j)Y_i^{\mathrm{obs}} = \frac{1}{N}\sum_{i=1}^{N}W_iB_i(j)\frac{N(j)}{N_{\mathrm{t}}(j)}Y_i^{\mathrm{obs}},
$$
类似地 $q(j)\bar Y_{\mathrm{c}}^{\mathrm{obs}}(j) = \frac{1}{N}\sum_i(1 - W_i)B_i(j)\frac{N(j)}{N_{\mathrm{c}}(j)}Y_i^{\mathrm{obs}}$。对 $j$ 求和，并利用 $N(j)/N_{\mathrm{t}}(j) = 1/\tilde e(j)$ 与 $N(j)/N_{\mathrm{c}}(j) = 1/(1 - \tilde e(j))$，即得公式。$\square$

分块不用每个单位自己的倾向评分估计值，而用它所在区组的平均分配比率。这解释了它的稳健性：一个 $\hat e(X_i) = 0.01$ 的处理组单位，若所在区组中有 10% 的单位接受处理，则其权重为 $10$，而不是 $100$。代价是块内的残余偏差，它可由 §10.2.3 的回归调整消除。

不同估计量的权重可以直接比较。在修剪后的彩票样本中（$N_{\mathrm{c}} = 172$，$N_{\mathrm{t}} = 151$），加权估计量的归一化权重在对照组中最大为 $9.68$，即单个单位的作用几乎是平均单位的十倍；在全样本中最大权重为 $41.7$，对照组权重的标准差为 $2.69$，这是协变量不平衡的表现，也是未修剪样本上的加权对倾向评分模型敏感的原因。在修剪后的样本中，分块加回归与匹配加回归的权重标准差约为 $1$（它们的权重甚至可以为负，因为回归在块内或匹配对内会略有外推）。

## 10.4. 匹配估计量

### 10.4.1. 最低工资数据

**例 10.4.1（新泽西州与宾夕法尼亚州的快餐业雇员数）** Card 与 Krueger（1994）利用新泽西州与邻近的宾夕法尼亚州东部（最低工资未变）的快餐店雇员数，研究了新泽西州 1992 年提高州最低工资的效应。单位是一家餐厅，处理组是新泽西州的餐厅，对照组是宾夕法尼亚州的餐厅；结果变量是涨薪后的雇员人数。协变量为涨薪前的雇员人数、起薪、首次加薪的平均等待时间，以及连锁品牌（汉堡王、肯德基、Roy Rogers 或温蒂汉堡）。Card 与 Krueger 比较的是两个州雇员数的变化，即双重差分设计；这里只用这组数据来说明匹配估计量，并假设给定协变量时分配是无混杂的。为了让机制清晰可见，取 20 家餐厅的小子样本，含两个协变量：连锁品牌 $X_{i1}$（0 表示汉堡王，1 表示肯德基）与初始雇员数 $X_{i2}$：

| 单位 | 州 | 品牌 | 初始雇员数 | 最终雇员数 | 单位 | 州 | 品牌 | 初始雇员数 | 最终雇员数 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | NJ | BK | 22.5 | 40.0 | 11 | PA | BK | 20.0 | 19.5 |
| 2 | NJ | KFC | 14.0 | 12.5 | 12 | PA | BK | 13.5 | 21.0 |
| 3 | NJ | BK | 37.5 | 20.0 | 13 | PA | BK | 19.0 | 11.0 |
| 4 | NJ | KFC | 9.0 | 3.5 | 14 | PA | BK | 12.0 | 17.0 |
| 5 | NJ | KFC | 8.0 | 5.5 | 15 | PA | BK | 32.5 | 22.5 |
| 6 | PA | BK | 10.5 | 15.0 | 16 | PA | BK | 16.0 | 20.0 |
| 7 | PA | KFC | 13.8 | 17.0 | 17 | PA | KFC | 11.0 | 14.0 |
| 8 | PA | KFC | 8.5 | 10.5 | 18 | PA | KFC | 4.5 | 6.5 |
| 9 | PA | BK | 25.5 | 18.5 | 19 | PA | BK | 12.5 | 31.5 |
| 10 | PA | BK | 17.0 | 12.5 | 20 | PA | BK | 8.0 | 8.0 |

前五个单位是处理组（$\mathbb{I}_{\mathrm{t}} = \{1, \dots, 5\}$），其余十五个是对照组（$\mathbb{I}_{\mathrm{c}} = \{6, \dots, 20\}$）。估计目标是处理组效应，即新泽西州各餐厅 $Y_i(1) - Y_i(0)$ 的平均。

:::

### 10.4.2. 不放回匹配

**定义 10.4.1（匹配估计量）** 对每个处理组单位 $i$，给定一个匹配的对照 $m_i^{\mathrm{c}}$（或 $M$ 个对照组成的集合 $\mathcal{M}_i^{\mathrm{c}}$），处理组平均效应的**匹配估计量**用匹配对象的结果来插补每个处理组单位缺失的对照结果：

$$
\hat\tau_{\mathrm{t}}^{\mathrm{match}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\hat\tau_i^{\mathrm{match}}, \qquad \hat\tau_i^{\mathrm{match}} = Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}} = Y_i(1) - Y_{m_i^{\mathrm{c}}}(0).
$$

在不放回的最近可用匹配中，处理组单位按固定的顺序依次取出，每个单位与尚未用过的对照中最近的一个匹配。结果取决于顺序与距离。在例 10.4.1 中，取距离 $d^2 = (x_1 - x_1')^2 + (x_2 - x_2')^2$ 和顺序 $1, \dots, 5$，匹配对象为单位 11、7、15、8 与 20，各单位的估计为 $20.5$、$-4.5$、$-2.5$、$-7$ 与 $-2.5$，$\hat\tau_{\mathrm{t}}^{\mathrm{match}} = 0.8$。下面两处改动说明了这种任意性：

- 取顺序 $1, 2, 3, 5, 4$ 时，单位 5 取走对照 8（另一家有 8.5 名雇员的肯德基餐厅），单位 4 得到对照 20，是一家汉堡王。平均值恰好仍为 $0.8$，但五对中有两对改变了。
- 取距离 $100(x_1 - x_1')^2 + (x_2 - x_2')^2$（实际上要求品牌精确匹配）时，单位 5 匹配的是对照 17（肯德基，11 名雇员）而不是 20（汉堡王，8 名雇员），估计值变为 $-0.4$。

距离的选择体现了对哪些协变量最重要的判断；[3.9.9](/3.9.9) 的 Mahalanobis 距离是默认选择，它把协变量标准化并考虑了它们的相关性。

### 10.4.3. 放回匹配与多重匹配

放回时，每个处理组单位都与它最近的对照匹配，$m_i^{\mathrm{c}} = \arg\min_{i' \in \mathbb{I}_{\mathrm{c}}}\lVert X_i - X_{i'}\rVert$，无论该对照是否已被用过。设 $L(i)$ 为单位 $i$ 被用作匹配对象的次数，则

$$
\hat\tau_{\mathrm{t}}^{\mathrm{repl}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}}\bigr) = \frac{1}{N_{\mathrm{t}}}\sum_{i=1}^{N}\Bigl(W_iY_i^{\mathrm{obs}} - (1 - W_i)L(i)Y_i^{\mathrm{obs}}\Bigr).
$$
顺序不再起作用，每个匹配都是当前最好的，所以偏差更小；但被多次使用的对照获得较大的权重 $L(i)$，使方差增大。在例 10.4.1 中，单位 4 与 5 都与对照 8 匹配，它被使用了两次，估计值为 $(20.5 - 4.5 - 2.5 - 7 - 5)/5 = 0.3$。

若允许每个处理组单位有 $M$ 个匹配，$\mathcal{M}_i^{\mathrm{c}}$ 为最近的 $M$ 个对照组成的集合，则

$$
\hat\tau_{\mathrm{t}}^{\mathrm{match},M} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\left(Y_i(1) - \frac{1}{M}\sum_{j \in \mathcal{M}_i^{\mathrm{c}}}Y_j(0)\right).
$$
若匹配的对照互不相同，且在给定协变量时结果的方差为 $\sigma_{\mathrm{t}}^2$ 与 $\sigma_{\mathrm{c}}^2$，则条件方差为

$$
\operatorname{Var}\bigl(\hat\tau_{\mathrm{t}}^{\mathrm{match},M} \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr) = \frac{1}{N_{\mathrm{t}}}\left(\sigma_{\mathrm{t}}^2 + \frac{\sigma_{\mathrm{c}}^2}{M}\right).
$$
当 $\sigma_{\mathrm{c}}^2 = \sigma_{\mathrm{t}}^2 = \sigma^2$ 时，相对于单个匹配的方差缩减比例为

$$
\frac{\operatorname{Var}(\hat\tau_{\mathrm{t}}^{\mathrm{match},1}) - \operatorname{Var}(\hat\tau_{\mathrm{t}}^{\mathrm{match},M})}{\operatorname{Var}(\hat\tau_{\mathrm{t}}^{\mathrm{match},1})} = \frac{2\sigma^2 - \sigma^2(1 + 1/M)}{2\sigma^2} = \frac{M - 1}{2M},
$$
当 $M = 2$ 时为 25%，$M = 3$ 时为 33%，$M \to \infty$ 时趋于 50%：处理组结果自身的方差永远不能靠增加匹配数来减少。收益递减得很快，而额外的匹配质量更差、会增加偏差，所以通常取较小的 $M$（一到四）。

### 10.4.4. 匹配的偏差与偏差校正

除非匹配是精确的，匹配总会留下偏差。对匹配对象为 $m_i^{\mathrm{c}}$ 的处理组单位 $i$，记 $D_i = X_i - X_{m_i^{\mathrm{c}}}$ 为匹配差异（精确匹配时 $D_i = 0$）。则

$$
\mathbb{E}\bigl[\hat\tau_i^{\mathrm{match}} \bigm| W_i = 1, X_i, X_{m_i^{\mathrm{c}}}\bigr] = \mu_1(X_i) - \mu_0(X_{m_i^{\mathrm{c}}}) = \tau(X_i) + \bigl(\mu_0(X_i) - \mu_0(X_{m_i^{\mathrm{c}}})\bigr),
$$
其中 $\tau(x) = \mu_1(x) - \mu_0(x)$。单位层面的偏差为 $B_i = \mu_0(X_i) - \mu_0(X_{m_i^{\mathrm{c}}})$：精确匹配时为零，当 $D_i$ 很小且 $\mu_0$ 光滑时也很小。协变量个数多且为连续型时，差异随样本量增大而缩小得很慢（Abadie 与 Imbens 2006），大样本中偏差可能超过方差而占主导。补救办法是估计偏差并将其减去。

**定义 10.4.2（偏差校正匹配估计量）** 设 $\hat\mu_0$ 是对照回归函数的一个估计，插补 $\hat Y_i(0) = Y_{m_i^{\mathrm{c}}}(0) + \hat\mu_0(X_i) - \hat\mu_0(X_{m_i^{\mathrm{c}}})$。**偏差校正匹配估计量**为

$$
\hat\tau_{\mathrm{t}}^{\mathrm{adj}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\bigl(Y_i(1) - \hat Y_i(0)\bigr) = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\bigl(Y_i(1) - Y_{m_i^{\mathrm{c}}}(0) - \hat B_i\bigr).
$$

对线性模型，估计的偏差为 $\hat B_i = D_i\hat{\boldsymbol{\beta}}$，各估计量的区别在于如何得到 $\hat{\boldsymbol{\beta}}$：

1. 差分回归。假设 $\mu_0(x) = \alpha + x\boldsymbol{\beta}$ 且 $\mu_1(x) = \tau + \mu_0(x)$。则 $Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}} = \tau + D_i\boldsymbol{\beta} + \nu_i$，其中 $\nu_i = (Y_i(1) - \mu_1(X_i)) - (Y_{m_i^{\mathrm{c}}}(0) - \mu_0(X_{m_i^{\mathrm{c}}}))$ 在给定 $\boldsymbol{X}$ 与 $\boldsymbol{W}$ 时均值为零。在处理组单位上把匹配对之差对差异做回归，

   $$
   \hat{\boldsymbol{\beta}}_{\mathrm{d}} = \left(\sum_{i:W_i = 1}(D_i - \bar D)^{\mathsf T}(D_i - \bar D)\right)^{-1}\sum_{i:W_i = 1}(D_i - \bar D)^{\mathsf T}\bigl(Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}}\bigr),
   $$
   得到 $\hat\tau_{\mathrm{t}}^{\mathrm{adj,d}} = \hat\tau_{\mathrm{t}}^{\mathrm{match}} - \bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}}$，即回归的截距。
2. 对照回归。把已匹配的对照单位的结果对其协变量做回归来估计 $\boldsymbol{\beta}$。
3. 分别回归。在已匹配的对照样本与处理样本中分别回归来估计 $\mu_0$ 与 $\mu_1$，允许效应随协变量变化。

三种方法中的回归都是局部的：只使用匹配后的样本（其中协变量的分布相近），只修正很小的差异 $D_i$。与分块加回归一样，线性模型的设定误差现在只有二阶影响。

**例 10.4.2（最低工资数据的结果）** 对完整数据集，放回匹配给出最低工资上调对雇员数（每家餐厅的雇员人数）影响的如下估计：

| 估计目标 | 方法 | $M$ | 距离 | 估计值 |
|---|---|---|---|---|
| 新泽西州 | 回归，无协变量 | | | $-0.22$ |
| 新泽西州 | 回归，带协变量 | | | $1.35$ |
| 新泽西州 | 匹配 | 1 | Mahalanobis | $0.89$ |
| 新泽西州 | 匹配 | 4 | Mahalanobis | $1.01$ |
| 新泽西州 | 匹配 | 1 | 欧氏 | $0.93$ |
| 新泽西州 | 匹配 | 1 | 品牌精确匹配，其余用 Mahalanobis | $0.92$ |
| 宾夕法尼亚州 | 匹配 | 1 | Mahalanobis | $0.63$ |
| 全体 | 匹配 | 1 | Mahalanobis | $0.84$ |
| 新泽西州 | 偏差校正（差分回归） | 1 | Mahalanobis | $0.51$ |

匹配估计对实施细节的小改动是稳健的：匹配个数、距离以及对品牌的精确匹配对估计值影响很小。这里 Mahalanobis 距离与欧氏距离给出相近的结果，因为协变量几乎不相关。没有一个估计表明最低工资上调减少了这些餐厅的雇员数；这与 Card 和 Krueger 的结论一致，尽管他们的分析基于随时间的变化而非匹配。

:::

## 10.5. 估计量的方差

本章与前几章的所有估计量都是观测结果的加权平均，

$$
\hat\tau = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\lambda_iY_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\lambda_iY_i^{\mathrm{obs}}, \qquad \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\lambda_i = \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\lambda_i = 1,
$$
权重 $\lambda_i = \lambda(W_i, X_i, \boldsymbol{W}_{(-i)}, \boldsymbol{X}_{(-i)})$ 依赖于处理与协变量，但不依赖于结果：

| 估计量 | 权重 $\lambda_i$ |
|---|---|
| 均值差 | $1$ |
| 加权 | 处理组为 $\frac{N_{\mathrm{t}}}{e(X_i)}\Big/\sum_{j:W_j = 1}\frac{1}{e(X_j)}$，对照组为 $\frac{N_{\mathrm{c}}}{1 - e(X_i)}\Big/\sum_{j:W_j = 0}\frac{1}{1 - e(X_j)}$ |
| 子类化 | 处理组为 $\sum_jB_i(j)\frac{N(j)/N}{N_{\mathrm{t}}(j)/N_{\mathrm{t}}}$，对照组为 $\sum_jB_i(j)\frac{N(j)/N}{N_{\mathrm{c}}(j)/N_{\mathrm{c}}}$ |
| 匹配（对全体单位的效应） | 由每个单位被用作匹配对象的次数决定 |
| 回归 | $X_i$ 的线性函数，可能为负 |

记 $\mu_i = \mu_{W_i}(X_i)$，$\sigma_i^2 = \sigma_{W_i}^2(X_i)$。在给定 $(\boldsymbol{X}, \boldsymbol{W})$ 下各结果相互独立，所以

$$
\hat\tau = \left(\frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\lambda_i\mu_i - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\lambda_i\mu_i\right) + \left(\frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\lambda_i(Y_i^{\mathrm{obs}} - \mu_i) - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\lambda_i(Y_i^{\mathrm{obs}} - \mu_i)\right)
$$
且

$$
\operatorname{Var}\bigl(\hat\tau \bigm| \boldsymbol{X}, \boldsymbol{W}\bigr) = \frac{1}{N_{\mathrm{t}}^2}\sum_{i:W_i = 1}\lambda_i^2\sigma_i^2 + \frac{1}{N_{\mathrm{c}}^2}\sum_{i:W_i = 0}\lambda_i^2\sigma_i^2.
$$
第一个括号是估计量的条件均值，它与估计目标之差就是偏差；第二个括号具有上面的方差。该公式解释了 §10.3 中权重比较的意义：方差随 $\sum\lambda_i^2$ 增大，所以少数几个很大的权重就会使方差膨胀。要估计方差，需要 $\sigma_i^2$。一个简单而一般的办法是在同一处理组内匹配：对单位 $i$，找到处理相同、协变量最接近的单位 $j(i)$，取 $\hat\sigma_i^2 = \frac{1}{2}(Y_i^{\mathrm{obs}} - Y_{j(i)}^{\mathrm{obs}})^2$；当 $X_i \approx X_j$ 时 $\mathbb{E}[(Y_i - Y_{j})^2] \approx 2\sigma^2_{W_i}(X_i)$，所以它近似无偏。代入得到 $\widehat{\operatorname{Var}}(\hat\tau \mid \boldsymbol{X}, \boldsymbol{W})$，即给定协变量时的方差，适用于样本平均效应；超总体方差还要加上条件平均效应 $\tau(X_i)$ 的方差。朴素的**自助法**对匹配个数固定的匹配估计量并不成立（Abadie 与 Imbens 2008），因为重抽样改变了匹配结构，其改变方式无法模拟抽样分布；基于匹配的方差估计量避开了这个问题。

## 10.6. 完整的工作流程

关于正则分配机制的三章合起来构成一个完整的工作流程：

| 阶段 | 步骤 | 工具 | 章节 |
|---|---|---|---|
| 设计 | 估计倾向评分 | logistic 回归，三步协变量选择 | [3.9.8](/3.9.8) |
| 设计 | 评估平衡 | 标准化差，标准差的对数比，Mahalanobis 距离，线性化倾向评分，重叠 | [3.9.9](/3.9.9) |
| 设计 | 改善平衡 | 修剪（必要时）；按倾向评分分块，或按 Mahalanobis 距离或倾向评分距离匹配 | [3.9.9](/3.9.9) |
| 分析 | 估计效应 | 加权；分块并在块内回归；匹配加回归（偏差校正） | 本章 |
| 分析 | 推断 | 线性估计量的方差，置信区间与检验 | 本章 |

最重要的要素是：以倾向评分衡量平衡，以分块和匹配改善平衡，再以块内或匹配集内的回归调整消除残余的差异。下图在带有非线性结果模型的模拟数据上比较了这些估计量。

![300 次模拟观察性研究（$N = 1000$，两个协变量，非线性的对照结果，恒定效应为 2）中各估计量的抽样分布：均值差、线性回归、用 logistic 倾向评分的归一化逆概率加权、按倾向评分五分位数分五块（含与不含块内回归）、处理组平均效应的放回最近邻匹配，以及偏差校正匹配。模拟数据](./plots/estimator_comparison.py)

均值差偏离很远。线性回归与单纯分块仍有偏差：前者因为线性模型错误，后者因为五个区组仍留有残余不平衡。加权几乎无偏，但方差最大。块内回归的分块几乎无偏，且最精确：每个回归只需修正很小的不平衡，所以设定误差几乎无关紧要。匹配因匹配不精确而有较小的偏差，偏差校正使其减小。

## 小结

- 均值差的偏差（定理 10.2.1）：在无混杂性与 $\mu_w(x) = \alpha + \tau w + x\boldsymbol{\beta}$ 下，$\mathbb{E}[\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} \mid \boldsymbol{X}, \boldsymbol{W}] = (\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta}$；分块之后缩小为 $\sum_jq(j)(\bar X_{\mathrm{t}}(j) - \bar X_{\mathrm{c}}(j))\boldsymbol{\beta}$（推论 10.2.1）。
- 分块加回归：$\hat\tau^{\mathrm{strat,adj}} = \sum_jq(j)\hat\tau^{\mathrm{adj}}(j)$（平均效应）或 $\sum_j\frac{N_{\mathrm{t}}(j)}{N_{\mathrm{t}}}\hat\tau^{\mathrm{adj}}(j)$（处理组效应）；方差为 $\sum_jq(j)^2\widehat{\operatorname{Var}}(j)$。彩票数据表明，修剪与分块使估计对回归设定不敏感。
- 分块就是以粗化评分 $\tilde e(j) = N_{\mathrm{t}}(j)/N(j)$ 加权（定理 10.3.1），因此比用 $\hat e(X_i)$ 加权更稳定。
- **匹配估计量**（处理组效应）：

  | 变体 | 偏差 | 方差 | 说明 |
  |---|---|---|---|
  | 不放回 | 较大，依赖顺序 | 较小 | 结果依赖于匹配顺序 |
  | 放回 | 较小 | 较大（权重 $L(i)$） | 与顺序无关 |
  | $M$ 个匹配 | 较大 | 至多减少 $(M - 1)/(2M)$，不超过 50% | $\sigma_{\mathrm{c}} = \sigma_{\mathrm{t}}$ |
  | 偏差校正 | 消除 $\hat B_i = D_i\hat{\boldsymbol{\beta}}$ | 大致不变 | 在匹配样本上做局部回归 |

- 所有估计量对 $Y^{\mathrm{obs}}$ 都是线性的：$\hat\tau = \frac{1}{N_{\mathrm{t}}}\sum_{W_i = 1}\lambda_iY_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{W_i = 0}\lambda_iY_i^{\mathrm{obs}}$，条件方差为 $\sum\lambda_i^2\sigma_i^2/N_w^2$；$\sigma_i^2$ 用处理组内的匹配来估计。

## 思考题

1. 对 $N = 3$、单位 1 与 2 为处理组、单位 3 为对照的情形证明定理 10.2.1，写出每一项。

   **答** $\hat\tau^{\mathrm{dif}} - \tau_{\mathrm{fs}} = \frac{1}{2}(Y_1(1) + Y_2(1)) - Y_3(0) - \frac{1}{3}\sum_{i}(Y_i(1) - Y_i(0))$。取条件期望并代入 $\mu_w(x) = \alpha + \tau w + x\boldsymbol{\beta}$：$Y(1)$ 的各项给出 $\frac{1}{6}(\mu_1(X_1) + \mu_1(X_2)) - \frac{1}{3}\mu_1(X_3) = \frac{1}{3}(\bar X_{\mathrm{t}} - X_3)\boldsymbol{\beta}$，$Y(0)$ 的各项给出 $-\frac{2}{3}\mu_0(X_3) + \frac{1}{3}(\mu_0(X_1) + \mu_0(X_2)) = \frac{2}{3}(\bar X_{\mathrm{t}} - X_3)\boldsymbol{\beta}$，常数 $\alpha$、$\tau$ 在每一组中都抵消。二者之和为 $(\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}})\boldsymbol{\beta}$，其中 $\bar X_{\mathrm{c}} = X_3$；权重 $N_{\mathrm{c}}/N = 1/3$ 与 $N_{\mathrm{t}}/N = 2/3$ 正是证明中的权重。
2. 证明：若定理 10.2.1 的线性模型成立，并对整个样本做回归，则回归估计量是条件无偏的。那么为什么不推荐在原始样本上做回归？

   **答** 在系数 $\boldsymbol{\beta}$ 共同的模型下，$Y_i^{\mathrm{obs}} = \alpha + \tau_{\mathrm{sp}}W_i + X_i\boldsymbol{\beta} + \varepsilon_i$，且 $\mathbb{E}[\varepsilon_i \mid \boldsymbol{X}, \boldsymbol{W}] = 0$，所以最小二乘对 $\tau_{\mathrm{sp}}$ 是条件无偏的。问题在于模型只是一种近似：当 $\bar X_{\mathrm{t}}$ 与 $\bar X_{\mathrm{c}}$ 相差很大时，估计依赖于模型在其中一组没有数据的区域的形式，微小的设定误差（一个二次项、一个交互项）就会产生很大的偏差，彩票数据就是例证（全样本上的估计从 $-6.2$ 变到 $-2.8$）。
3. 一个修剪后的样本有两个区组。区组 1：60 个对照，20 个处理，$\hat\tau^{\mathrm{dif}}(1) = 1.0$，方差估计为 $0.10$；区组 2：20 个对照，40 个处理，$\hat\tau^{\mathrm{dif}}(2) = 2.5$，方差估计为 $0.12$。计算 $\hat\tau^{\mathrm{strat}}$、处理组效应的估计及它们的标准误。

   **答** $q = (80/140, 60/140) = (0.571, 0.429)$：$\hat\tau^{\mathrm{strat}} = 0.571 + 1.071 = 1.64$，方差 $0.571^2 \times 0.10 + 0.429^2 \times 0.12 = 0.0327 + 0.0221 = 0.0547$，标准误 $0.234$。处理组权重 $(20/60, 40/60)$：$\hat\tau_{\mathrm{t}} = 0.333 + 1.667 = 2.0$，方差 $0.111 \times 0.10 + 0.444 \times 0.12 = 0.0644$，标准误 $0.254$。处理组效应更大，是因为处理组集中在效应较大的区组。
4. 利用定理 10.3.1，计算思考题 3 中区组 1 的一个处理组单位与一个对照组单位的权重，并与该区组内个体倾向评分估计值介于 $0.05$ 与 $0.45$ 之间时的 Horvitz–Thompson 权重比较。

   **答** $\tilde e(1) = 20/80 = 0.25$，所以处理组单位的权重为 $1/0.25 = 4$，对照组单位为 $1/0.75 = 1.33$。用个体评分时，处理组单位的权重 $1/\hat e$ 在 $2.2$ 到 $20$ 之间，对照组单位的权重 $1/(1 - \hat e)$ 在 $1.05$ 到 $1.8$ 之间。分块以区组平均值取代了极端的权重 $20$，用较小的块内偏差换取了小得多的方差。
5. 在例 10.4.1 中验证放回匹配的估计值 $0.3$，并计算各对照的权重 $L(i)$。

   **答** （欧氏距离下）最近的对照为：单位 1（BK，22.5）对应 11（BK，20.0）；单位 2（KFC，14.0）对应 7（KFC，13.8）；单位 3（BK，37.5）对应 15（BK，32.5）；单位 4（KFC，9.0）与 5（KFC，8.0）都对应 8（KFC，8.5）。各差为 $40 - 19.5 = 20.5$、$12.5 - 17 = -4.5$、$20 - 22.5 = -2.5$、$3.5 - 10.5 = -7$、$5.5 - 10.5 = -5$，均值为 $1.5/5 = 0.3$。$L(8) = 2$，$L(7) = L(11) = L(15) = 1$，其余对照的 $L(i) = 0$。
6. 推导方差缩减比例 $(M - 1)/(2M)$，并说明它为什么不能超过 50%。在什么情况下"匹配的对照互不相同"的假设不成立？此时会怎样？

   **答** 对照互不相同时，$M$ 个对照结果的平均在给定条件下方差为 $\sigma^2/M$，所以 $\operatorname{Var}(\hat\tau_{\mathrm{t}}^{\mathrm{match},M}) = (\sigma^2 + \sigma^2/M)/N_{\mathrm{t}}$，相对于 $2\sigma^2/N_{\mathrm{t}}$ 的缩减为 $(1 - 1/M)/2$。无论 $M$ 多大，处理组结果都贡献 $\sigma^2/N_{\mathrm{t}}$，即单个匹配时方差的一半，所以缩减不到 50%。放回匹配时，同一个对照常被多个处理组单位使用（$L(i)$ 大），对照项相关，方差比该公式更大，由一般公式 $\sum\lambda_i^2\sigma_i^2/N_{\mathrm{c}}^2$（其中 $\lambda_i \propto L(i)$）给出。
7. 证明差分回归的偏差校正给出 $\hat\tau_{\mathrm{t}}^{\mathrm{adj,d}} = \hat\tau_{\mathrm{t}}^{\mathrm{match}} - \bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}}$，并解释该校正项的含义。

   **答** 在处理组上把 $\Delta Y_i = Y_i^{\mathrm{obs}} - Y_{m_i^{\mathrm{c}}}^{\mathrm{obs}}$ 对 $(1, D_i)$ 回归，斜率为 $\hat{\boldsymbol{\beta}}_{\mathrm{d}}$，截距为 $\overline{\Delta Y} - \bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}} = \hat\tau_{\mathrm{t}}^{\mathrm{match}} - \bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}}$。对 $\Delta Y_i - D_i\hat{\boldsymbol{\beta}}_{\mathrm{d}}$ 取平均得到同样的值。截距是差异为零（即精确匹配）时匹配对之差的预测值；$\bar D\hat{\boldsymbol{\beta}}_{\mathrm{d}}$ 估计的是系统性差异造成的平均偏差 $\frac{1}{N_{\mathrm{t}}}\sum B_i$。
8. 解释为什么方差估计 $\hat\sigma_i^2 = \frac{1}{2}(Y_i^{\mathrm{obs}} - Y_{j(i)}^{\mathrm{obs}})^2$ 使用同一处理组内的匹配，如果改用另一组中的匹配会出什么问题。

   **答** 在同一组内，$Y_i$ 与 $Y_{j(i)}$ 独立，均值几乎相同，都是 $\mu_{W_i}(X_i)$，方差为 $\sigma_{W_i}^2$，所以 $\mathbb{E}[(Y_i - Y_{j(i)})^2] \approx 2\sigma_{W_i}^2(X_i)$。另一组中的匹配对象的均值是 $\mu_{1 - W_i}(X_i)$，于是平方差中还含有单位层面效应的平方 $\tau(X_i)^2$ 与另一个潜在结果的方差；这样的估计会因处理效应而向上偏，不能估计 $\sigma_{W_i}^2$。
