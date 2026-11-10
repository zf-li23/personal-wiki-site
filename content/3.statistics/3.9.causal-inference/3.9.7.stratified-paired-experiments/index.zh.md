---
title: 分层随机化实验与配对随机化实验
description: 用前几章的四种方法推断分层随机化实验与配对随机化实验。包括使用层内统计量的 Fisher 检验，Neyman 分层估计量及其方差、相对完全随机化的精度增益，含层指示变量的回归与饱和交互模型，分层模型；对配对实验，讨论对内差、无需对内重复的保守方差估计量，以及以对为单位的协变量的回归。例子取自 Project STAR 与 Electric Company 实验。
source_hash: b979a0648f4a
---

完全随机化实验对所有单元一视同仁。但在实验之前，人们往往已经知道不同单元组之间的结果存在系统差异：各学校的平均测验成绩不同，不同年龄患者的预后不同。若在设计中按此形成分组，并在每组内分别随机分配处理，就排除了组间的偶然失衡，处理单元与对照单元的比较也就在相似的单元之间进行。这就是 [3.9.2](/3.9.2) 中的**分层随机化实验**（定义 2.4.7），它是因果推断中与**分区组**（[3.8.2](/3.8.2)）和**随机区组设计**（[3.8.6](/3.8.6)）相对应的设计。每层只有两个单元的极限情形是**配对随机化实验**（定义 2.4.8），对应 [3.8.2](/3.8.2) 的**配对设计**。本章把 [3.9.3](/3.9.3)–[3.9.6](/3.9.6) 中为 CRE 建立的四种方法移植到这两种设计上。大部分移植是直截了当的，值得讲的是不那么直截了当的地方。同样的结构在观察性研究中再次出现：由倾向评分划分的层扮演设计中的层的角色（[3.9.9](/3.9.9)、[3.9.10](/3.9.10)）。

## 7.1. 分层随机化实验

### 7.1.1. 设计与记号

$N$ 个单元按协变量划分为 $J$ 层，在每层内各做一次 CRE，层间相互独立。记 $G_i \in \{1, \dots, J\}$ 为单元 $i$ 所在的层，$B_i(j) = \boldsymbol{1}\{G_i = j\}$。第 $j$ 层有 $N(j)$ 个单元，其中 $N_{\mathrm{t}}(j)$ 个接受处理，$N_{\mathrm{c}}(j) = N(j) - N_{\mathrm{t}}(j)$ 个为对照；该层占样本的比例为 $q(j) = N(j)/N$，倾向评分为 $e(j) = N_{\mathrm{t}}(j)/N(j)$。分配机制为

$$
\mathbb{P}\bigl(\boldsymbol{W} \mid \boldsymbol{X}, \boldsymbol{Y}(0), \boldsymbol{Y}(1)\bigr) = \prod_{j=1}^{J}\binom{N(j)}{N_{\mathrm{t}}(j)}^{-1} \quad \text{for } \boldsymbol{W} \in \mathcal{W}^+ = \Bigl\{\boldsymbol{W} \in \mathcal{W} : \sum_{i: G_i = j}W_i = N_{\mathrm{t}}(j) \text{ for } j = 1, \dots, J\Bigr\},
$$
其余取值处概率为零。该设计也称随机区组实验。与 CRE 相比，其特点是各层的倾向评分可以不同，并且它固定的是每一层中接受处理的单元数，而不只是总数。

### 7.1.2. Project STAR

学生与教师成绩比实验（Student/Teacher Achievement Ratio experiment，Project STAR）于 1985–1986 年在 Tennessee 州进行，评估班级规模对测验成绩的影响，是教育领域最有影响的随机化实验之一。在这里使用的幼儿园数据中，单元是教师（即班级），而不是学生个人：同班学生会相互影响，以班级为单元分析可使 SUTVA 中的无干扰部分变得合理（[3.9.1](/3.9.1)）。处理是小班（13–17 名学生），对照是常规班（22–25 名学生），结果是班级的数学测验平均分。共 $N = 68$ 个班级，分布在 16 所学校，随机化在学校内进行，因此学校就是层：

| 学校数 | $N_{\mathrm{t}}(j)$ | $N_{\mathrm{c}}(j)$ | $e(j)$ | 每所学校的分配数 |
|---|---|---|---|---|
| 13 | 2 | 2 | 0.50 | $\binom{4}{2} = 6$ |
| 2 | 3 | 2 | 0.60 | $\binom{5}{3} = 10$ |
| 1 | 4 | 2 | 0.67 | $\binom{6}{4} = 15$ |

可能的分配向量共有 $6^{13} \times 10^2 \times 15 \approx 2 \times 10^{13}$ 个，远少于小班总数同为 $N_{\mathrm{t}} = 36$ 的 CRE 的 $\binom{68}{36} \approx 2.5 \times 10^{19}$ 个；分层排除了所有诸如把小班都集中在少数几所学校的分配。

### 7.1.3. 估计目标

第 $j$ 层内的效应与总体效应为

$$
\tau_{\mathrm{fs}}(j) = \frac{1}{N(j)}\sum_{i: G_i = j}\bigl(Y_i(1) - Y_i(0)\bigr), \qquad
\tau_{\mathrm{fs}} = \frac{1}{N}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0)\bigr) = \sum_{j=1}^{J}q(j)\,\tau_{\mathrm{fs}}(j).
$$
总体效应是各层效应按层比例加权的平均。若只有两层，例如女性（$f$）与男性（$m$），则 $\tau_{\mathrm{fs}} = q\,\tau_{\mathrm{fs}}(f) + (1 - q)\,\tau_{\mathrm{fs}}(m)$，其中 $q = N(f)/N$。其他加权方式定义其他估计目标，例如处理组效应 $\tau_{\mathrm{fs,t}}$，它以第 $j$ 层占处理单元的比例 $N_{\mathrm{t}}(j)/N_{\mathrm{t}}$ 为权。

### 7.1.4. 为何分层，以及难在何处

分层有三个理由：CRE 可能无法实施，例如处理必须在每所学校或每家医院内实施；当层能预测结果时，分层给出更精确的估计（定理 7.3.2）；并且，理解分层实验是理解观察性研究的关键，后者被当作倾向评分未知的分层实验来分析（[3.9.8](/3.9.8)）。原则上每一层都是一个 CRE，可用 [3.9.3](/3.9.3)–[3.9.6](/3.9.6) 的方法分析。实际中各层常常很小（STAR 中每所学校只有两个处理班与两个对照班），层内效应本身并不是关注的对象，问题在于如何把各层合起来对 $\tau_{\mathrm{fs}}$ 或 $\tau_{\mathrm{fs,t}}$ 作推断。

## 7.2. Fisher 精确 p 值

Fisher 尖锐原假设 $H_0\colon Y_i(0) = Y_i(1)$（$i = 1, \dots, N$）与 CRE 中相同，在其下所有缺失的结果都已知。p 值的算法与 [3.9.3](/3.9.3) 完全一样，只是随机化分布取在分层设计的 $\mathcal{W}^+$ 上：分配在每一层内重新随机化。任何统计量都给出有效的检验；设计决定的是哪种统计量有检验功效。

| 统计量 | 定义 | 评价 |
|---|---|---|
| 仅用一层 | $T^{\mathrm{dif}}(j) = \lvert\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - \bar Y_{\mathrm{c}}^{\mathrm{obs}}(j)\rvert$ | 有效但浪费：只用了部分数据，可能漏掉其他层中对 $H_0$ 的违背 |
| 合并均值差 | $T^{\mathrm{dif}} = \lvert\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\rvert$ | 有效，但若 $e(j)$ 随层变化且各层结果水平不同，则它在 $H_0$ 下不以零为中心，损失功效 |
| 层内差的加权和 | $T^{\mathrm{dif}, \lambda} = \Bigl\lvert\sum_{j=1}^{J}\lambda(j)\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - \bar Y_{\mathrm{c}}^{\mathrm{obs}}(j)\bigr)\Bigr\rvert$，$\sum_j\lambda(j) = 1$ | 推荐；$\lambda(j) = q(j)$ 针对 $\tau_{\mathrm{fs}}$，$\lambda(j) \propto q(j)e(j)(1 - e(j))$ 按精度给各层加权 |
| 合并秩 | $T^{\operatorname{rank}} = \lvert\bar R_{\mathrm{t}} - \bar R_{\mathrm{c}}\rvert$，秩在整个样本中计算 | 同 CRE；各层结果水平相差很大时不理想 |
| 层内秩 | $T^{\mathrm{rank,stratum}} = \lvert\bar R_{\mathrm{t}}^{\mathrm{strat}} - \bar R_{\mathrm{c}}^{\mathrm{strat}}\rvert$ | 推荐；稳健，且不受层间水平差异的影响 |

要理解合并均值差为何不以零为中心，设有两层，$e(f) \ne e(m)$，原假设成立，但女性的结果较高。于是处理组中结果较高的那一层占的比例比对照组大，$\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$ 便系统地为正，尽管没有任何单元有效应。检验仍然有效，因为其随机化分布发生了同样的平移，但真实的效应更难与这种平移区分开。

单元 $i$ 的层内标准化秩只在其所在层的单元中对其结果排序，并如 [3.9.3](/3.9.3)（定义 3.2.1）那样中心化：

$$
R_i^{\mathrm{strat}} = \sum_{i': G_{i'} = G_i}\boldsymbol{1}\bigl\{Y_{i'}^{\mathrm{obs}} < Y_i^{\mathrm{obs}}\bigr\} + \frac{1}{2}\Bigl(1 + \sum_{i': G_{i'} = G_i}\boldsymbol{1}\bigl\{Y_{i'}^{\mathrm{obs}} = Y_i^{\mathrm{obs}}\bigr\}\Bigr) - \frac{N(G_i) + 1}{2},
$$
$\bar R_{\mathrm{t}}^{\mathrm{strat}}$、$\bar R_{\mathrm{c}}^{\mathrm{strat}}$ 是它在处理单元与对照单元上的平均。由于秩在层内计算，它们完全消去了层间的水平差异，这与 **Wilcoxon 符号秩检验**消去对效应的道理相同（[3.6.8](/3.6.8)）；这些分层秩检验属于 [3.6](/3.6) 的**秩统计量**家族。

对 Project STAR，p 值由分层随机化分布的模拟近似：

| 统计量 | 取值 | p 值 |
|---|---|---|
| $T^{\mathrm{dif}}$ | 0.224 | 0.034 |
| $T^{\mathrm{dif}, \lambda}$，$\lambda(j) = q(j)$ | 0.241 | 0.023 |
| $T^{\mathrm{rank,stratum}}$ | 0.48 | 0.15 |

基于均值的检验在 $5\%$ 水平上拒绝无效应的原假设，秩检验则不拒绝。差别的来源在于，均值所给的证据部分依赖于少数结果极端的班级，而秩会削弱这些班级的影响。两类统计量回答的问题略有不同，应在看到数据之前选定。

## 7.3. Neyman 方法

### 7.3.1. 分层估计量

每一层内的分配都是 CRE，所以 [3.9.4](/3.9.4) 的结果适用于层内均值差 $\hat\tau^{\mathrm{dif}}(j) = \bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - \bar Y_{\mathrm{c}}^{\mathrm{obs}}(j)$：它是 $\tau_{\mathrm{fs}}(j)$ 的无偏估计，方差为定理 4.3.1 在该层内的值。以定义 $\tau_{\mathrm{fs}}$ 的权重合并各层，就得到分层估计量。

**定理 7.3.1** 在分层随机化实验中，设每一层都有 $N_{\mathrm{t}}(j), N_{\mathrm{c}}(j) \ge 2$，令

$$
\hat\tau^{\mathrm{strat}} = \sum_{j=1}^{J}q(j)\,\hat\tau^{\mathrm{dif}}(j), \qquad
\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = \sum_{j=1}^{J}q(j)^2\left(\frac{s_{\mathrm{c}}^2(j)}{N_{\mathrm{c}}(j)} + \frac{s_{\mathrm{t}}^2(j)}{N_{\mathrm{t}}(j)}\right),
$$
其中 $s_{\mathrm{c}}^2(j)$ 与 $s_{\mathrm{t}}^2(j)$ 是第 $j$ 层对照单元与处理单元观测结果的样本方差。则

$$
\mathbb{E}_W\bigl[\hat\tau^{\mathrm{strat}}\bigr] = \tau_{\mathrm{fs}}, \qquad
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{strat}}\bigr) = \sum_{j=1}^{J}q(j)^2\left(\frac{S_{\mathrm{c}}^2(j)}{N_{\mathrm{c}}(j)} + \frac{S_{\mathrm{t}}^2(j)}{N_{\mathrm{t}}(j)} - \frac{S_{\mathrm{tc}}^2(j)}{N(j)}\right),
$$
其中有限总体方差 $S^2(j)$ 在第 $j$ 层内计算；并且 $\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] \ge \operatorname{Var}_W(\hat\tau^{\mathrm{strat}})$，若个体效应在每层内为常数则等号成立。

**证明** 由定理 4.2.1 在第 $j$ 层内的结论，$\mathbb{E}_W[\hat\tau^{\mathrm{dif}}(j)] = \tau_{\mathrm{fs}}(j)$，故由线性性 $\mathbb{E}_W[\hat\tau^{\mathrm{strat}}] = \sum_j q(j)\tau_{\mathrm{fs}}(j) = \tau_{\mathrm{fs}}$。不同层的分配相互独立，所以各 $\hat\tau^{\mathrm{dif}}(j)$ 相互独立，且

$$
\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{strat}}\bigr) = \sum_{j=1}^{J}q(j)^2\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}(j)\bigr),
$$
其中每一项由定理 4.3.1 在该层内给出。由定理 4.4.1 在每层内的结论，$\mathbb{E}_W[s_{\mathrm{c}}^2(j)] = S_{\mathrm{c}}^2(j)$，$\mathbb{E}_W[s_{\mathrm{t}}^2(j)] = S_{\mathrm{t}}^2(j)$，所以 $\mathbb{E}_W[\widehat{\operatorname{Var}}{}^{\mathrm{neyman}}] - \operatorname{Var}_W(\hat\tau^{\mathrm{strat}}) = \sum_j q(j)^2S_{\mathrm{tc}}^2(j)/N(j) \ge 0$，当且仅当每个 $S_{\mathrm{tc}}^2(j) = 0$ 时取等号。$\square$

在分层实验中，全体处理单元与全体对照单元的简单均值差一般是有偏的：它在处理组中以 $N_{\mathrm{t}}(j)/N_{\mathrm{t}}$ 给第 $j$ 层加权，在对照组中以 $N_{\mathrm{c}}(j)/N_{\mathrm{c}}$ 加权，而倾向评分不同时这两组权重不同。只有 $e(j)$ 在所有层相同时它才无偏，此时它与 $\hat\tau^{\mathrm{strat}}$ 一致。

**例 7.3.1** 对 Project STAR，分层分析给出 $\hat\tau^{\mathrm{strat}} = 0.241$，$\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = 0.092^2$，所以 $\tau_{\mathrm{fs}}$ 的 $95\%$ 区间为 $0.241 \pm 1.96 \times 0.092 = (0.061, 0.421)$。若把同样的数据错误地当作来自 CRE 来分析，则 $\hat\tau^{\mathrm{dif}} = 0.224$，标准误为 $0.141$，区间为 $(-0.053, 0.500)$，包含零。

这一比较说明两点。其一，CRE 的方差估计量在此无效，因为各层的处理概率不同（$0.5$、$0.6$、$0.67$），而 CRE 的公式忽略了设计；同理，$\hat\tau^{\mathrm{dif}}$ 也不是无偏的。其二，分层带来了精度的显著提高，因为各学校的平均结果不同：分层分析把校间变异从误差中去掉了。

:::

### 7.3.2. 分层实验与完全随机化实验的比较

精度增益可以在超总体中精确刻画。取两层 $f$ 与 $m$，它们在总体中的比例分别为 $q$ 与 $1 - q$，并设每层中接受处理的比例同为 $p$，于是分层实验与完全随机化实验处理的单元数相同。对 $w \in \{\mathrm{c}, \mathrm{t}\}$，以 $\mu_w(g)$ 与 $\sigma_w^2(g)$ 记第 $g$ 层中 $Y_i(w)$ 的均值与方差。

**定理 7.3.2** 在上述条件下，设 $N_{\mathrm{t}} = pN$，则

$$
N\Bigl(\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{dif}}\bigr)_{\mathrm{CRE}} - \operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{strat}}\bigr)_{\mathrm{SRE}}\Bigr) = q(1 - q)\left(\frac{\bigl(\mu_{\mathrm{c}}(f) - \mu_{\mathrm{c}}(m)\bigr)^2}{1 - p} + \frac{\bigl(\mu_{\mathrm{t}}(f) - \mu_{\mathrm{t}}(m)\bigr)^2}{p}\right) \ge 0.
$$

**证明** 在 CRE 中，由定理 4.6.1，$N\operatorname{Var}_{\mathrm{sp}}(\hat\tau^{\mathrm{dif}}) = \sigma_{\mathrm{c}}^2/(1 - p) + \sigma_{\mathrm{t}}^2/p$，其中 $\sigma_w^2$ 是 $Y_i(w)$ 的总体方差。由对各层的全方差公式，

$$
\sigma_w^2 = q\,\sigma_w^2(f) + (1 - q)\,\sigma_w^2(m) + q(1 - q)\bigl(\mu_w(f) - \mu_w(m)\bigr)^2.
$$
在 SRE 中，$\hat\tau^{\mathrm{strat}} = q\,\hat\tau^{\mathrm{dif}}(f) + (1 - q)\,\hat\tau^{\mathrm{dif}}(m)$，第 $g$ 层含 $qN$ 或 $(1 - q)N$ 个单元，其中比例 $p$ 接受处理。在每层内应用定理 4.6.1 并利用独立性，

$$
N\operatorname{Var}_{\mathrm{sp}}\bigl(\hat\tau^{\mathrm{strat}}\bigr) = q\left(\frac{\sigma_{\mathrm{c}}^2(f)}{1 - p} + \frac{\sigma_{\mathrm{t}}^2(f)}{p}\right) + (1 - q)\left(\frac{\sigma_{\mathrm{c}}^2(m)}{1 - p} + \frac{\sigma_{\mathrm{t}}^2(m)}{p}\right).
$$
两式相减，层内方差相互抵消，只剩下全方差中的层间项。$\square$

分层估计量的方差从不更大，并且当且仅当潜在结果的层均值不同时才严格更小：在这一设定下，按某个协变量分层从不吃亏。增益就是分层协变量所解释的方差，这与 [3.9.5](/3.9.5) 中回归调整所利用的是同一个量；分层是在设计阶段而不是分析阶段把它去掉。在小样本中有一点代价：定理 7.3.1 的方差估计量自由度较少，而只含一个处理单元或一个对照单元的层根本无法估计层内方差，这一问题要靠 7.6 节的配对设计来解决。

## 7.4. 回归方法

### 7.4.1. 层指示变量

一个自然的回归含处理指示变量，以及每一层各自的截距：

$$
Y_i^{\mathrm{obs}} = \tau W_i + \sum_{j=1}^{J}\beta(j)B_i(j) + \varepsilon_i,
$$
共有 $J + 1$ 个参数，最小二乘估计量为 $(\hat\tau^{\mathrm{ols}}, \hat{\boldsymbol{\beta}}^{\mathrm{ols}})$，其总体对应量为 $(\tau^*, \boldsymbol{\beta}^*) = \arg\min\mathbb{E}_{\mathrm{sp}}\bigl[(Y_i^{\mathrm{obs}} - \tau W_i - \sum_j\beta(j)B_i(j))^2\bigr]$。如果各层的效应相同，$\tau_{\mathrm{sp}}(j) = \tau$，则模型正确，$\tau^* = \tau$。没有这一假设时，该系数是各层效应的加权平均，但权重不是 $\tau_{\mathrm{sp}}$ 的权重。

**定理 7.4.1** 在从无限总体随机抽取的样本上做分层随机化实验，设层概率为 $q(j)$，倾向评分为 $e(j)$，则

$$
\tau^* = \tau_\omega = \frac{\sum_{j=1}^{J}\omega(j)\,\tau_{\mathrm{sp}}(j)}{\sum_{j=1}^{J}\omega(j)}, \qquad \omega(j) = q(j)\,e(j)\bigl(1 - e(j)\bigr),
$$
且 $\sqrt{N}(\hat\tau^{\mathrm{ols}} - \tau_\omega)$ 渐近服从均值为零的正态分布。

**证明** 由 **Frisch–Waugh–Lovell 定理**，$\tau^*$ 是 $Y^{\mathrm{obs}}$ 对 $W$ 在层指示变量上投影后的残差所作回归的总体系数。该投影为 $\sum_j e(j)B_i(j) = e(G_i)$，所以残差为 $W_i - e(G_i)$，且

$$
\tau^* = \frac{\mathbb{E}_{\mathrm{sp}}\bigl[(W_i - e(G_i))Y_i^{\mathrm{obs}}\bigr]}{\mathbb{E}_{\mathrm{sp}}\bigl[(W_i - e(G_i))^2\bigr]}.
$$
在 $G_i = j$ 的条件下，$W_i$ 服从 $\mathrm{Ber}(e(j))$ 且与潜在结果独立，所以 $\mathbb{E}[(W_i - e(j))^2 \mid G_i = j] = e(j)(1 - e(j))$，且

$$
\mathbb{E}\bigl[(W_i - e(j))Y_i^{\mathrm{obs}} \bigm| G_i = j\bigr] = e(j)(1 - e(j))\,\mathbb{E}[Y_i(1) \mid G_i = j] - (1 - e(j))e(j)\,\mathbb{E}[Y_i(0) \mid G_i = j] = e(j)(1 - e(j))\,\tau_{\mathrm{sp}}(j).
$$
以概率 $q(j)$ 对各层平均即得公式。渐近正态性的证明同定理 5.3.2。$\square$

权重偏向单元多、倾向评分接近 $1/2$ 的层，即效应估计得最精确的层。当倾向评分在所有层相同，或效应在所有层相同时，$\tau_\omega = \tau_{\mathrm{sp}}$；否则回归估计的是一个定义明确的因果量，但不是平均效应。

### 7.4.2. 饱和模型

要得到 $\tau_{\mathrm{sp}}$，需允许每一层有各自的效应，即含 $2J$ 个参数的**饱和模型**。在参数化

$$
Y_i^{\mathrm{obs}} = \tau W_i\frac{B_i(J)}{N(J)/N} + \sum_{j=1}^{J}\beta(j)B_i(j) + \sum_{j=1}^{J-1}\gamma(j)W_i\Bigl(B_i(j) - B_i(J)\frac{N(j)}{N(J)}\Bigr) + \varepsilon_i,
$$
之下，系数 $\tau$ 直接就是各层效应的加权平均。等价形式更便于阅读：(i) 对第 $j$ 层的单元 $i$，$Y_{i}^{\mathrm{obs}} = \beta_j + \tau_jW_i + \varepsilon_i$，其中 $\tau = N^{-1}\sum_j N(j)\tau_j$；或 (ii) $Y_{i}^{\mathrm{obs}} = \beta_j + \tau W_i + \gamma_jW_i + \varepsilon_i$，约束为 $\sum_j N(j)\gamma_j = 0$。

**定理 7.4.2** 在从无限总体随机抽取的样本上做分层随机化实验，饱和模型中系数 $\hat\tau^{\mathrm{ols,inter}}$ 的总体对应量为 $\tau^* = \tau_{\mathrm{sp}}$，且

$$
\sqrt{N}\bigl(\hat\tau^{\mathrm{ols,inter}} - \tau_{\mathrm{sp}}\bigr) \xrightarrow{d} \mathcal{N}\left(0,\ \sum_{j=1}^{J}q(j)^2\left(\frac{\sigma_{\mathrm{c}}^2(j)}{(1 - e(j))q(j)} + \frac{\sigma_{\mathrm{t}}^2(j)}{e(j)q(j)}\right)\right).
$$

在形式 (i) 中，每个 $\hat\tau_j$ 都是层内均值差，所以 $\hat\tau^{\mathrm{ols,inter}} = \sum_j q(j)\hat\tau^{\mathrm{dif}}(j) = \hat\tau^{\mathrm{strat}}$ 严格成立：饱和回归复现了 Neyman 分层估计量，其渐近方差就是定理 7.3.1 中方差的超总体版本。在 R 中，两个模型的拟合为

```r
fit_add <- lm(Y_obs ~ W + Strata)   # coefficient of W estimates tau_omega
fit_sat <- lm(Y_obs ~ W * Strata)   # coefficient of W is the effect in the reference stratum
```

在 R 的默认对比下，`fit_sat` 中 `W` 的系数是第一层的效应而不是平均效应；$\tau$ 须由各系数按 $\sum_j q(j)\hat\tau_j$ 计算（或者用上面的中心化参数化拟合模型），其标准误则由相应的线性组合得到。

对 Project STAR，可加模型给出 $\hat\tau^{\mathrm{ols}} = 0.238$（标准误 $0.103$），饱和模型给出 $\hat\tau^{\mathrm{ols,inter}} = 0.241$（标准误 $0.095$）。两个估计很接近，标准误也相近，这与效应在学校之间异质性有限相符：当各层效应相近时，$\tau_\omega$ 与 $\tau_{\mathrm{sp}}$ 相差很小。

## 7.5. 基于模型的分析

[3.9.6](/3.9.6) 的基于模型的方法移植时多了一个新的选择。三个输入是分层分配机制、各层内潜在结果的模型（例如 $Y_i(w) \mid G_i = j, \theta \sim \mathcal{N}(\mu_w(j), \sigma_w^2)$），以及层参数 $\theta_j = (\mu_{\mathrm{c}}(j), \mu_{\mathrm{t}}(j))$ 的先验。由定理 6.3.1，不依赖于结果的分配机制再次被消去。先验可以在各层之间独立，但当每层只有两个处理单元和两个对照单元时，每个 $\theta_j$ 都定得很差；也可以取分层先验

$$
\begin{pmatrix} \mu_{\mathrm{c}}(j) \\ \mu_{\mathrm{t}}(j) \end{pmatrix} \Bigm| \boldsymbol{\gamma}, \Sigma \overset{\text{iid}}{\sim} \mathcal{N}(\boldsymbol{\gamma}, \Sigma), \qquad j = 1, \dots, J,
$$
并给超参数 $(\boldsymbol{\gamma}, \Sigma)$ 一个先验。**分层模型**（[3.7.6](/3.7.6)）使每一层都能从其他层借力，把层均值朝公共均值部分合并，合并的程度由数据决定。它还带来新的估计目标：$\Sigma$ 的后验显示平均潜在结果与处理效应在层间变化多大，层效应 $\mu_{\mathrm{t}}(j) - \mu_{\mathrm{c}}(j)$ 的方差则直接度量效应的异质性。对 Project STAR，分层模型回答小班效应在学校之间相差多少，这是其他三种方法都没有直接处理的问题。

## 7.6. 配对随机化实验

### 7.6.1. 设计与记号

配对随机化实验是含 $J = N/2$ 层、每层两个单元且其中一个接受处理的分层实验：$N(j) = 2$，$N_{\mathrm{t}}(j) = N_{\mathrm{c}}(j) = 1$。每个单元的分配概率为 $1/2$，可能的分配向量共 $2^{N/2}$ 个。当预期对内潜在结果的变异远小于对间变异时就选用这种设计；在大总体中，往往能找到协变量非常相近的单元对。

第 $j$ 对的两个单元记为 $A$ 与 $B$，潜在结果为 $Y_{j,A}(0), Y_{j,A}(1), Y_{j,B}(0), Y_{j,B}(1)$，协变量为 $X_{j,A}, X_{j,B}$，处理指示变量为 $W_{j,A}$ 与 $W_{j,B} = 1 - W_{j,A}$。第 $j$ 对中观测到的差（处理减对照）为

$$
\hat\tau^{\mathrm{pair}}(j) = W_{j,A}\bigl(Y_{j,A}^{\mathrm{obs}} - Y_{j,B}^{\mathrm{obs}}\bigr) + (1 - W_{j,A})\bigl(Y_{j,B}^{\mathrm{obs}} - Y_{j,A}^{\mathrm{obs}}\bigr),
$$
估计目标是各对与总体的平均效应

$$
\tau^{\mathrm{pair}}(j) = \frac{1}{2}\Bigl[\bigl(Y_{j,A}(1) - Y_{j,A}(0)\bigr) + \bigl(Y_{j,B}(1) - Y_{j,B}(0)\bigr)\Bigr], \qquad
\tau_{\mathrm{fs}} = \frac{1}{J}\sum_{j=1}^{J}\tau^{\mathrm{pair}}(j).
$$
由于每一对恰好贡献一个处理单元与一个对照单元，处理子样本与对照子样本就和配对所能做到的一样相似。

### 7.6.2. Electric Company 实验

1970 年前后，《芝麻街》的制作方儿童电视工作坊（Children's Television Workshop）评估了旨在教授阅读的教育电视节目《The Electric Company》（Ball and Bogatz 1972）。各班级在学校内依阅读成绩配对，每对中随机选一个班观看该节目。单元是班级，协变量 $X$ 是班级的前测阅读平均分，结果 $Y$ 是后测分数。Ohio 州 Youngstown 的八对数据如下：

| 对 | $W_{j,A}$ | $Y_{j,A}^{\mathrm{obs}}$ | $X_{j,A}$ | $W_{j,B}$ | $Y_{j,B}^{\mathrm{obs}}$ | $X_{j,B}$ | $\hat\tau^{\mathrm{pair}}(j)$ | $\Delta_{X,j}$ |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 54.6 | 12.9 | 1 | 60.6 | 12.0 | 6.0 | $-0.9$ |
| 2 | 0 | 56.5 | 15.1 | 1 | 55.5 | 13.9 | $-1.0$ | $-1.2$ |
| 3 | 0 | 75.2 | 16.8 | 1 | 84.8 | 17.2 | 9.6 | 0.4 |
| 4 | 0 | 75.6 | 15.8 | 1 | 101.9 | 18.9 | 26.3 | 3.1 |
| 5 | 0 | 55.3 | 13.9 | 1 | 70.6 | 15.3 | 15.3 | 1.4 |
| 6 | 0 | 59.3 | 14.5 | 1 | 78.4 | 16.6 | 19.1 | 2.1 |
| 7 | 0 | 87.0 | 17.0 | 1 | 84.2 | 16.0 | $-2.8$ | $-1.0$ |
| 8 | 0 | 73.7 | 15.8 | 1 | 108.6 | 20.1 | 34.9 | 4.3 |

这里单元的标记使得单元 $B$ 是接受处理的一方，$\Delta_{X,j}$ 是前测分数之差（处理减对照）。

### 7.6.3. Fisher 精确 p 值

尖锐原假设与随机化都与 SRE 相同：在 $H_0$ 下，对每一对独立地翻转哪个单元接受处理，即可得到随机化分布，这会改变 $\hat\tau^{\mathrm{pair}}(j)$ 的符号。7.2 节的统计量与 SRE 中的表现一致，只有一个例外：层内统计量 $T^{\mathrm{dif}}(j)$ 毫无用处，因为一对只给出一个差，其随机化分布只有两个点。自然的统计量是 $T = \lvert\frac{1}{J}\sum_j\hat\tau^{\mathrm{pair}}(j)\rvert$，它等于 $\lambda(j) = 1/J$ 时的加权统计量 $T^{\mathrm{dif}, \lambda}$。其精确分布是带独立随机符号的 $\pm\hat\tau^{\mathrm{pair}}(j)$ 之和的分布；把差换成它们的秩，就得到 **Wilcoxon 符号秩检验**（[3.6.8](/3.6.8)），其经典的对称性论证在这里被设计的随机化所取代。

### 7.6.4. Neyman 方法

均值差是各对之差的平均，$\hat\tau^{\mathrm{dif}} = \frac{1}{J}\sum_j\hat\tau^{\mathrm{pair}}(j)$，由定理 7.3.1（或直接由每个 $\hat\tau^{\mathrm{pair}}(j)$ 以概率 $1/2$ 取其两个可能值）可知它是无偏的。问题在于方差。在一对之内，$\hat\tau^{\mathrm{pair}}(j)$ 的方差涉及 $Y_{j,A}(0)$、$Y_{j,A}(1)$、$Y_{j,B}(0)$ 与 $Y_{j,B}(1)$，其中只有两个能被观测到，而一个处理单元和一个对照单元无法给出对内样本方差。定理 7.3.1 中逐层的估计量没有定义。解决办法是改用对间的变异。

**定理 7.6.1** 设有 $J$ 对单元，每对中随机指派一个单元接受处理、另一个作对照。则

1. $\mathbb{E}_W\bigl[\hat\tau^{\mathrm{dif}}\bigr] = \tau_{\mathrm{fs}}$；
2. $\displaystyle\operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) = \frac{1}{N^2}\sum_{j=1}^{J}\Bigl(Y_{j,A}(0) + Y_{j,A}(1) - Y_{j,B}(0) - Y_{j,B}(1)\Bigr)^2$；
3. 估计量 $\displaystyle\widehat{\operatorname{Var}}{}^{\mathrm{pair}} = \frac{1}{J(J - 1)}\sum_{j=1}^{J}\bigl(\hat\tau^{\mathrm{pair}}(j) - \hat\tau^{\mathrm{dif}}\bigr)^2$ 满足

$$
\mathbb{E}_W\bigl[\widehat{\operatorname{Var}}{}^{\mathrm{pair}}\bigr] = \operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr) + \frac{1}{J(J - 1)}\sum_{j=1}^{J}\bigl(\tau^{\mathrm{pair}}(j) - \tau_{\mathrm{fs}}\bigr)^2 \ge \operatorname{Var}_W\bigl(\hat\tau^{\mathrm{dif}}\bigr).
$$

**证明** 对内之差在 $A$ 接受处理时取值 $d_j^{A} = Y_{j,A}(1) - Y_{j,B}(0)$，在 $B$ 接受处理时取值 $d_j^{B} = Y_{j,B}(1) - Y_{j,A}(0)$，各以概率 $1/2$。其均值为 $\frac{1}{2}(d_j^A + d_j^B) = \tau^{\mathrm{pair}}(j)$，对各对平均即得 (1)。其方差为 $\frac{1}{4}(d_j^A - d_j^B)^2 = \frac{1}{4}\bigl(Y_{j,A}(1) + Y_{j,A}(0) - Y_{j,B}(1) - Y_{j,B}(0)\bigr)^2$。各对的分配相互独立，所以 $\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) = \frac{1}{J^2}\sum_j\operatorname{Var}_W(\hat\tau^{\mathrm{pair}}(j))$，由 $4J^2 = N^2$ 即得 (2)。对 (3)，各 $\hat\tau^{\mathrm{pair}}(j)$ 相互独立，均值为 $\tau^{\mathrm{pair}}(j)$，方差为 $v_j$。对独立但不同分布的变量作标准计算，得

$$
\mathbb{E}_W\Bigl[\sum_{j=1}^{J}\bigl(\hat\tau^{\mathrm{pair}}(j) - \hat\tau^{\mathrm{dif}}\bigr)^2\Bigr] = \Bigl(1 - \frac{1}{J}\Bigr)\sum_{j=1}^{J}v_j + \sum_{j=1}^{J}\bigl(\tau^{\mathrm{pair}}(j) - \tau_{\mathrm{fs}}\bigr)^2.
$$
除以 $J(J - 1)$ 并利用 $\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}) = \frac{1}{J^2}\sum_j v_j$，即得 (3)。$\square$

若平均效应在每一对中相同，即对所有 $j$ 有 $\tau^{\mathrm{pair}}(j) = \tau_{\mathrm{fs}}$，则该估计量是无偏的；这在配对设计中有时额外作出的两条假定下尤其成立：(A1) 效应在对内为常数，$Y_{j,A}(1) - Y_{j,A}(0) = Y_{j,B}(1) - Y_{j,B}(0)$；(A2) 效应在对间为常数，且各对的对内方差相等。仅有对内为常数并不需要。若效应在对间是异质的，则 $\widehat{\operatorname{Var}}{}^{\mathrm{pair}}$ 向上有偏，相应的置信区间是保守的但仍然有效，这与 CRE 中的 Neyman 估计量完全一样。

**例 7.6.1** 对 Youngstown 的各对数据，$\hat\tau^{\mathrm{dif}} = \frac{1}{8}\sum_j\hat\tau^{\mathrm{pair}}(j) = 107.4/8 = 13.4$，且

$$
\widehat{\operatorname{Var}}{}^{\mathrm{pair}} = \frac{1}{8 \cdot 7}\sum_{j=1}^{8}\bigl(\hat\tau^{\mathrm{pair}}(j) - 13.4\bigr)^2 = 4.6^2,
$$
所以 $95\%$ 区间为 $13.4 \pm 1.96 \times 4.6 = (4.3, 22.5)$。若同样的分配来自对 16 个班级的 CRE，估计值不变，仍是 $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = 13.4$，但 Neyman 方差要用两组的样本标准差 $s_{\mathrm{c}} = 12.2$ 与 $s_{\mathrm{t}} = 18.5$：$\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = 12.2^2/8 + 18.5^2/8 = 7.8^2$，区间为 $(-2.0, 28.8)$。配对消去了班级之间平均阅读水平的巨大差异，而这些差异在 CRE 分析中留在误差里，标准误因此下降了四成。

:::

### 7.6.5. 回归方法

[3.9.5](/3.9.5) 中对个体单元的回归遇到与 Neyman 方差同样的困难：对 $J = N/2$ 对设置层指示变量后，饱和模型的参数个数与观测个数一样多。解决办法仍然沿用 Neyman 的思路：均值差本身就是一个回归估计量，即对各对之差关于常数作回归所得的截距，而对内之差是分析的基本结果。然后可以加入以对为单位的协变量：

| 模型 | $\hat\tau^{\mathrm{pair}}(j)$ 对下列项的回归 | 协变量 |
|---|---|---|
| $M_1$ | $\tau + \varepsilon_j$ | 无；$\hat\tau^{\mathrm{ols}} = \frac{2}{N}\sum_j\hat\tau^{\mathrm{pair}}(j) = \hat\tau^{\mathrm{dif}}$ |
| $M_2$ | $\tau + \beta\Delta_{X,j} + \varepsilon_j$ | 对内差 $\Delta_{X,j} = W_{j,A}(X_{j,A} - X_{j,B}) + (1 - W_{j,A})(X_{j,B} - X_{j,A})$ |
| $M_3$ | $\tau + \gamma(\bar X_j - \bar X) + \varepsilon_j$ | 对均值 $\bar X_j = (X_{j,A} + X_{j,B})/2$ |
| $M_4$ | $\tau + \beta\Delta_{X,j} + \gamma(\bar X_j - \bar X) + \varepsilon_j$ | 两者都有 |

对内差 $\Delta_{X,j}$ 调整一对中处理单元与对照单元之间的偶然失衡；对均值 $\bar X_j$ 允许效应随该对的水平而变，并经中心化，使 $\tau$ 仍为平均效应。

**定理 7.6.2** 设配对随机化实验在从对的超总体中随机抽取的一些对上进行，$(\tau^*, \beta^*, \gamma^*)$ 为模型 $M_4$ 中最小二乘系数的总体对应量（以 $\mu_X$ 代替 $\bar X$）。则 $\tau^* = \tau_{\mathrm{sp}}$，且 $\sqrt{J}(\hat\tau^{\mathrm{ols}} - \tau_{\mathrm{sp}})$ 渐近服从均值为零的正态分布。

证明与定理 5.3.1 和 7.4.1 的思路相同。对内的随机化使 $\Delta_{X,j}$ 的符号为正或为负的可能性相等，且与该对的潜在结果和 $\bar X_j$ 独立，故 $\mathbb{E}[\Delta_{X,j}] = 0$，$\mathbb{E}[\Delta_{X,j}(\bar X_j - \mu_X)] = 0$；目标函数像在 CRE 中那样分离，截距等于 $\hat\tau^{\mathrm{pair}}(j)$ 的总体均值，即 $\tau_{\mathrm{sp}}$。

对 Youngstown 的各对数据，普通最小二乘给出（括号内为常规标准误）：

| 模型 | $\hat\tau$ | $\Delta_{X,j}$ 的系数 | $\bar X_j - \bar X$ 的系数 |
|---|---|---|---|
| $M_1$ | 13.4 (4.6) | | |
| $M_2$ | 7.0 (1.0) | 6.3 (0.5) | |
| $M_3$ | 13.4 (4.2) | | 3.9 (2.5) |
| $M_4$ | 6.3 (0.9) | 6.9 (0.5) | $-1.1$ (0.5) |

对内的前测分数之差是一个强预测变量：处理班恰好平均比其搭档的前测分数高 $1.0$ 分（$\bar\Delta_X = 8.2/8$），斜率在 $6$ 以上，这一偶然失衡解释了未调整估计值的大约一半。调整后，估计值降到约 $7$，标准误降为原来的四分之一。只有八对时，这些数值并不牢靠，定理 7.6.2 的大样本依据也很薄弱；但定性的结论是稳健的：配对消去了对间变异，而对 $\Delta_{X,j}$ 的回归则消去了剩余的对内失衡。相比之下，对均值的贡献很小。

### 7.6.6. 基于模型的分析

配对实验基于模型的分析就是带分层先验的 SRE 分析，而这里分层先验几乎是不可避免的：每一对只提供两个观测，不经合并就无法估计各对的参数。一个典型的模型写作

$$
Y_{j,u}(0) = \mu_j + \beta X_{j,u} + \varepsilon_{j,u}(0), \qquad Y_{j,u}(1) = \mu_j + \gamma + \beta X_{j,u} + \varepsilon_{j,u}(1), \qquad \mu_j \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma_\mu^2),
$$
其中单元 $u \in \{A, B\}$，误差服从正态分布，方差分别为 $\sigma_{\mathrm{c}}^2$ 与 $\sigma_{\mathrm{t}}^2$，从而 $\tau_{\mathrm{sp}} = \gamma$。对 $\theta = (\mu, \beta, \gamma, \log\sigma_\mu, \log\sigma_{\mathrm{c}}, \log\sigma_{\mathrm{t}})$ 取弱先验，后验用**随机游走 Metropolis 算法**抽样探索；给定 $\theta$，对效应 $\mu_j$ 从其条件后验抽取，插补缺失的结果，并对每个抽样如算法 6.6.1 那样计算 $\tau_{\mathrm{fs}}$。对 Electric Company 的数据，结果与对前测对内差作回归的结果相近，部分原因是模型使用了同样的对协变量的线性依赖。

![一个含 80 个单元的模拟总体的估计平均效应的随机化分布，其潜在结果强烈依赖于一个协变量（左图），分别在完全随机化、按协变量四分位数分为四层的分层，以及相邻单元配对之下；右图为潜在结果与层的边界。模拟数据](./plots/sre_vs_cre.py)

此图显示了按有预测力的协变量分区组的增益。三种估计量都是无偏的；分层设计使标准差降低了近一半，而配对作为最细的分层，使之进一步降低。

## 小结

| | CRE | SRE | PRE |
|---|---|---|---|
| 随机化 | $N$ 个单元中的 $N_{\mathrm{t}}$ 个 | 每层内做 CRE | 每对两个单元中的一个 |
| Fisher | 任意统计量 | 层内均值差或秩 | 对内差的符号翻转；符号秩 |
| Neyman 估计量 | $\hat\tau^{\mathrm{dif}}$ | $\hat\tau^{\mathrm{strat}} = \sum_j q(j)\hat\tau^{\mathrm{dif}}(j)$ | $\hat\tau^{\mathrm{pair}}(j)$ 的均值 |
| 方差估计量 | $s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}$ | $\sum_j q(j)^2\bigl(s_{\mathrm{c}}^2(j)/N_{\mathrm{c}}(j) + s_{\mathrm{t}}^2(j)/N_{\mathrm{t}}(j)\bigr)$ | $\frac{1}{J(J - 1)}\sum_j(\hat\tau^{\mathrm{pair}}(j) - \hat\tau)^2$ |
| 回归 | $Y \sim W + X$ | $Y \sim W + $ 层 估计 $\tau_\omega$；饱和模型给出 $\tau_{\mathrm{sp}}$ | 对内差对 $\Delta_X$、$\bar X_j$ 回归 |
| 基于模型 | 独立同分布单元 | 层间独立先验或分层先验 | 对间分层先验 |

- 当处理比例或潜在结果在层间系统地变化时，应在设计中分层；四种方法都可直接移植。
- Neyman 分层估计量无偏，方差为 $\sum_j q(j)^2\operatorname{Var}_W(\hat\tau^{\mathrm{dif}}(j))$（定理 7.3.1）；在超总体中它的精度从不低于 CRE 估计量，增益为层间方差（定理 7.3.2）。
- 当倾向评分不同时，把 SRE 当作 CRE 分析是错误的：估计量有偏，方差估计无效（Project STAR：$0.224 \pm 0.141$ 对 $0.241 \pm 0.092$）。
- 含层哑变量的回归以 $q(j)e(j)(1 - e(j))$ 给各层效应加权（定理 7.4.1）；饱和模型恢复 $\tau_{\mathrm{sp}}$（定理 7.4.2）。
- 在 PRE 中，对内差是基本的量：方差估计量使用对间变异，除非各对的效应为常数，否则是保守的（定理 7.6.1）；回归以对内差作为结果变量（定理 7.6.2）。
- Electric Company：配对分析为 $13.4$（标准误 $4.6$），按 CRE 分析为 $7.8$。

## 思考题

1. 某 SRE 有两层。第 1 层有 $N(1) = 4$ 个单元，$N_{\mathrm{t}}(1) = 2$；第 2 层有 $N(2) = 6$ 个单元，$N_{\mathrm{t}}(2) = 2$。可能的分配向量有多少个？$N_{\mathrm{t}} = 4$ 的 CRE 会允许多少个？$q(j)$ 与 $e(j)$ 各是多少？

   **答** $\binom{4}{2}\binom{6}{2} = 6 \times 15 = 90$，而 CRE 为 $\binom{10}{4} = 210$。$q(1) = 0.4$，$q(2) = 0.6$；$e(1) = 0.5$，$e(2) = 1/3$。

2. 在思考题 1 的 SRE 中，观测结果为：第 1 层，处理组 $10, 12$，对照组 $6, 8$；第 2 层，处理组 $5, 7$，对照组 $2, 3, 4, 3$。计算 $\hat\tau^{\mathrm{strat}}$、其 Neyman 方差估计，以及朴素均值差。两个估计为什么不同？

   **答** 第 1 层：$\hat\tau^{\mathrm{dif}}(1) = 11 - 7 = 4$，$s_{\mathrm{t}}^2(1) = 2$，$s_{\mathrm{c}}^2(1) = 2$。第 2 层：$\hat\tau^{\mathrm{dif}}(2) = 6 - 3 = 3$，$s_{\mathrm{t}}^2(2) = 2$，$s_{\mathrm{c}}^2(2) = 2/3$。于是 $\hat\tau^{\mathrm{strat}} = 0.4 \cdot 4 + 0.6 \cdot 3 = 3.4$，$\widehat{\operatorname{Var}}{}^{\mathrm{neyman}} = 0.16(2/2 + 2/2) + 0.36\bigl((2/3)/4 + 2/2\bigr) = 0.32 + 0.42 = 0.74$，标准误 $0.86$。朴素估计为 $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = 34/4 - 26/6 = 8.5 - 4.33 = 4.17$。第 1 层结果较高且倾向评分较高，因而在处理组中占比偏大（占处理单元的 $50\%$，占对照单元的 $33\%$）；朴素估计把效应与层间水平差异混在了一起。

3. 证明：若各层的倾向评分相同，$e(j) = N_{\mathrm{t}}/N$，则 $\hat\tau^{\mathrm{strat}} = \hat\tau^{\mathrm{dif}}$。由此能否推出 CRE 的方差估计量是合适的？

   **答** 由 $N_{\mathrm{t}}(j) = eN(j)$，处理组均值为 $\bar Y_{\mathrm{t}}^{\mathrm{obs}} = \sum_j\frac{N_{\mathrm{t}}(j)}{N_{\mathrm{t}}}\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) = \sum_j q(j)\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j)$，对照组同理，所以两个估计量一致。方差估计量则不能推出：CRE 的估计量把结果的层间变异也计入了 $s_{\mathrm{c}}^2$ 与 $s_{\mathrm{t}}^2$，而分层设计已经去除了这部分变异，所以它是保守的，往往相当保守；应当使用定理 7.3.1 的分层估计量。

4. 对 $J = 2$ 直接计算最小二乘估计量以证明定理 7.4.1，并证明若 $e(1) = e(2)$ 则 $\tau_\omega = \tau_{\mathrm{sp}}$。

   **答** 有两层时，由 Frisch–Waugh–Lovell 定理，$\hat\tau^{\mathrm{ols}} = \sum_i(W_i - e(G_i))Y_i^{\mathrm{obs}}/\sum_i(W_i - e(G_i))^2$，其中 $e(j)$ 为样本中的处理比例。在第 $j$ 层，$\sum_{G_i = j}(W_i - e(j))^2 = N(j)e(j)(1 - e(j))$，且 $\sum_{G_i = j}(W_i - e(j))Y_i^{\mathrm{obs}} = N_{\mathrm{t}}(j)(1 - e(j))\bar Y_{\mathrm{t}}^{\mathrm{obs}}(j) - N_{\mathrm{c}}(j)e(j)\bar Y_{\mathrm{c}}^{\mathrm{obs}}(j) = N(j)e(j)(1 - e(j))\hat\tau^{\mathrm{dif}}(j)$。因此 $\hat\tau^{\mathrm{ols}} = \sum_j\omega(j)\hat\tau^{\mathrm{dif}}(j)/\sum_j\omega(j)$，其中 $\omega(j) = q(j)e(j)(1 - e(j))$，其极限为 $\tau_\omega$。若 $e(1) = e(2)$，则 $\omega(j) \propto q(j)$，$\tau_\omega = \sum_j q(j)\tau_{\mathrm{sp}}(j) = \tau_{\mathrm{sp}}$。

5. 利用定理 7.3.2，量化在平衡实验（$p = 1/2$，$q = 1/2$）中按性别分层所得的精度增益：设两性的结果均值相差一个层内标准差（两个潜在结果都如此），且各层内方差都是 $\sigma^2$。

   **答** 层内项：$N\operatorname{Var}(\hat\tau^{\mathrm{strat}}) = \sigma^2/(1/2) + \sigma^2/(1/2) = 4\sigma^2$。增益为 $q(1 - q)(\sigma^2/(1/2) + \sigma^2/(1/2)) = \frac{1}{4} \cdot 4\sigma^2 = \sigma^2$，所以 CRE 的 $N\operatorname{Var} = 5\sigma^2$。分层使方差降低 $20\%$（标准误降低约 $11\%$），相当于样本量大 $25\%$ 的 CRE。

6. 在 PRE 中，证明若处理效应在对间为常数，则即使它在对内变化，$\widehat{\operatorname{Var}}{}^{\mathrm{pair}}$ 也是无偏的。构造一个两对的例子，使该估计量向上有偏。

   **答** 由定理 7.6.1(3)，偏差为 $\frac{1}{J(J - 1)}\sum_j(\tau^{\mathrm{pair}}(j) - \tau_{\mathrm{fs}})^2$，当所有对平均 $\tau^{\mathrm{pair}}(j)$ 相等时它为零，无论各单元的效应如何。例：第 1 对中两个单元都有 $Y(0) = Y(1) = 0$，第 2 对中两个单元都有 $Y(0) = 0$、$Y(1) = 4$。于是在每种分配下 $\hat\tau^{\mathrm{pair}}(1) = 0$，$\hat\tau^{\mathrm{pair}}(2) = 4$，真实方差为 $0$，但 $\widehat{\operatorname{Var}}{}^{\mathrm{pair}} = \frac{1}{2}\bigl((0 - 2)^2 + (4 - 2)^2\bigr) = 4$ 恒成立。全部取值都是偏差，正如定理所言：这里 $\tau^{\mathrm{pair}}(1) = 0$，$\tau^{\mathrm{pair}}(2) = 4$，$\tau_{\mathrm{fs}} = 2$。

7. 对 Electric Company 的数据，用统计量 $T = \lvert\frac{1}{J}\sum_j\hat\tau^{\mathrm{pair}}(j)\rvert$ 做尖锐原假设的 Fisher 检验。有多少种符号模式给出不小于观测值 $13.4$ 的取值？

   **答** 在 $H_0$ 下，每个差以概率 $1/2$ 保持或翻转符号，共 $2^8 = 256$ 个等可能的 $\sum_j\pm\lvert\hat\tau^{\mathrm{pair}}(j)\rvert$ 值。观测的和为 $107.4$；各差的绝对值为 $6.0, 1.0, 9.6, 26.3, 15.3, 19.1, 2.8, 34.9$，总和为 $115.0$。仅当被翻转的差之和至多为 $(115.0 - 107.4)/2 = 3.8$ 时，符号模式才给出 $\lvert\text{和}\rvert \ge 107.4$，即什么都不翻转、$\{1.0\}$、$\{2.8\}$ 或 $\{1.0, 2.8\}$；再加上四个镜像模式，共 $8$ 种。精确 p 值为 $8/256 = 0.031$。

8. 什么情形下不宜分层？请结合定理 7.3.2 与设计的实际要求讨论。

   **答** 在定理 7.3.2 的超总体设定下，分层从不损失精度，所以理由是实际的：分层变量必须在分配之前就测得；若层数很多且很小，只含一个处理单元或对照单元的层使层内方差无法估计（定理 7.6.1 的配对问题），并损失自由度；若该变量与结果无关，则增益为零，而设计与分析反而更复杂。协变量很多时，也许更好的做法是只按少数几个强预测变量分层，其余的用回归调整（[3.9.5](/3.9.5)），或使用再随机化（[3.9.15](/3.9.15)）。
