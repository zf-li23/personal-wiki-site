---
title: 完全随机化实验：Fisher 精确 p 值
description: Fisher 对完全随机化实验的方法。蜂蜜实验；Fisher 尖锐原假设与全部缺失潜在结果的插补；检验统计量（均值差、分位数、t 统计量、规范化秩、基于模型的统计量与 Kolmogorov–Smirnov 统计量、组合统计量）；枚举得到的精确 p 值及其有效性、Monte Carlo 近似、有限总体中心极限定理与两样本 t 检验的联系；检验统计量中的协变量；由检验反演得到的 Fisher 区间。
source_hash: 503c92554082
---

从本章到 [3.9.7](/3.9.7)，我们研究随机化实验，即分配机制已知（因为是研究者选定的）的情形。最简单的情形是 [3.9.2](/3.9.2) 的完全随机化实验（CRE）：从 $N$ 个单元中随机抽取 $N_{\mathrm{t}}$ 个接受处理。本章与后三章发展 CRE 中推断的四种方法。

| 方法 | 问题 | 估计目标或假设 | 随机性的来源 | 章 |
|---|---|---|---|---|
| Fisher 精确 p 值 | 是否有任何效应？ | 尖锐原假设：对一切 $i$，$Y_i(1) = Y_i(0)$ | 仅分配 | [3.9.3](/3.9.3) |
| Neyman 重复抽样 | 平均效应有多大？ | $\tau_{\mathrm{fs}}$ 或 $\tau_{\mathrm{sp}}$ | 分配（以及抽样） | [3.9.4](/3.9.4) |
| 回归 | 调整协变量后的平均效应 | $\tau_{\mathrm{sp}}$ | 抽样与分配 | [3.9.5](/3.9.5) |
| 基于模型的插补 | 通过缺失结果的分布得到任意估计目标 | 任意 $\tau(\boldsymbol{Y}(0), \boldsymbol{Y}(1), \boldsymbol{X}, \boldsymbol{W})$ | 后验分布 | [3.9.6](/3.9.6) |

Fisher 的方法最古老，所需假设也最少。其想法是：在处理对任何单元都没有效应的假设下，所有潜在结果都已知，仅剩的随机性是分配，而它的分布由研究者控制。因此任一检验统计量在该假设下的分布可以精确算出，不需要任何关于结果的模型，也不需要大样本近似。这正是 Fisher 品茶女士（[3.8.1](/3.8.1)）背后的推理，它是一种**置换检验**（[3.6.1](/3.6.1)），其依据是实际进行的随机化，而不是关于数据的假设。

## 3.1. 蜂蜜实验与尖锐原假设

### 3.1.1. 数据

我们的贯穿示例是一项随机化试验，研究蜂蜜对上呼吸道感染儿童夜间咳嗽的治疗作用，取自 Paul 等人（2007）一项研究中的蜂蜜组与无治疗组。

| | |
|---|---|
| 单元 | $N = 72$ 名儿童 |
| 处理 | 睡前单次服用荞麦蜂蜜 |
| 对照 | 无主动处理 |
| 分配 | 完全随机化，$N_{\mathrm{t}} = 35$，$N_{\mathrm{c}} = 37$ |
| 结果 | 之后的咳嗽频率（cfa）与之后的咳嗽严重程度（csa） |
| 协变量 | 之前的咳嗽频率（cfp）与之前的咳嗽严重程度（csp） |

四个变量都按 0（“完全不频繁/不严重”）到 6（“极其频繁/严重”）的量表测量。协变量是在处理之前的那个晚上测得的。为了说明计算，我们用前六个单元，以咳嗽频率为结果。

| 单元 | $Y_i(0)$ | $Y_i(1)$ | $W_i$ | $X_i$（cfp） | $Y_i^{\mathrm{obs}}$（cfa） |
|---|---|---|---|---|---|
| 1 | ? | 3 | 1 | 4 | 3 |
| 2 | ? | 5 | 1 | 6 | 5 |
| 3 | ? | 0 | 1 | 4 | 0 |
| 4 | 4 | ? | 0 | 4 | 4 |
| 5 | 0 | ? | 0 | 1 | 0 |
| 6 | 1 | ? | 0 | 5 | 1 |

一半的潜在结果缺失，这就是 [3.9.1](/3.9.1) 的基本问题的具体形式。

### 3.1.2. Fisher 尖锐原假设

**定义 3.1.1（Fisher 尖锐原假设）** **Fisher 尖锐原假设**是处理对任何单元都没有效应的假设，

$$
H_0\colon\ Y_i(0) = Y_i(1) \quad \text{对一切 } i = 1, \dots, N.
$$
更一般地，若一个原假设与观测数据一起决定了所有缺失的潜在结果，则称它是尖锐的。

尖锐原假设远强于平均效应为零的假设 $\tau_{\mathrm{fs}} = 0$，后者允许一些单元的正效应与另一些单元的负效应相互抵消；后者有时称为 Neyman 弱原假设，是 [3.9.4](/3.9.4) 的主题。尖锐原假设之强使 Fisher 的方法成为可能：在 $H_0$ 下我们可以填补每一个缺失的潜在结果，$Y_i^{\mathrm{mis}} = Y_i^{\mathrm{obs}}$。

| 单元 | $Y_i(0)$ | $Y_i(1)$ | $W_i$ | $X_i$ | $Y_i^{\mathrm{obs}}$ |
|---|---|---|---|---|---|
| 1 | (3) | 3 | 1 | 4 | 3 |
| 2 | (5) | 5 | 1 | 6 | 5 |
| 3 | (0) | 0 | 1 | 4 | 0 |
| 4 | 4 | (4) | 0 | 4 | 4 |
| 5 | 0 | (0) | 0 | 1 | 0 |
| 6 | 1 | (1) | 0 | 5 | 1 |

括号中的值是在 $H_0$ 下插补的。其他尖锐原假设有常数可加效应 $Y_i(1) = Y_i(0) + C$（对一切 $i$）与常数可乘效应 $Y_i(1) = C \cdot Y_i(0)$（对一切 $i$），其中 $C$ 是指定的常数；在这两种假设下，$Y_i^{\mathrm{mis}}$ 同样由 $Y_i^{\mathrm{obs}}$ 与 $W_i$ 决定。Fisher 的方法适用于所有这些假设，3.5 节用它们构造区间。

### 3.1.3. 三个步骤

Fisher 精确 p 值通过三个步骤得到：

1. 设定一个尖锐原假设；
2. 选择检验统计量，即我们观测到的全部信息的已知实值函数 $T(\boldsymbol{W}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{X})$；
3. 衡量统计量的观测值有多极端：把它与枚举所有可能分配得到的 $H_0$ 下的精确分布作比较。

第一步刚刚讨论过。接下来两节讨论第二、三步。

## 3.2. 检验统计量

### 3.2.1. 基于位置差异的统计量

在尖锐原假设下，所有潜在结果都是固定的，所以**检验统计量** $T(\boldsymbol{W}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{X})$ 成为仅关于随机分配 $\boldsymbol{W}$ 的函数。任何统计量都给出有效的检验；选择只影响对所关心的备择假设的功效。最常见的选择是两组平均结果之差的绝对值，

$$
T^{\mathrm{dif}} = \bigl\lvert \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} \bigr\rvert = \left\lvert \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1} Y_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0} Y_i^{\mathrm{obs}} \right\rvert,
$$
它对常数可加效应 $H_1\colon Y_i(1) = Y_i(0) + C$ 有良好的功效。绝对值使检验成为双侧的；不取绝对值则为单侧。同一想法的变体有：

- 对数的平均之差 $T^{\log} = \bigl\lvert \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\ln Y_i^{\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}\ln Y_i^{\mathrm{obs}} \bigr\rvert$，用于正的结果，适合常数可乘效应 $Y_i(1) = C \cdot Y_i(0)$；
- 中位数或其他分位数之差 $T^{\mathrm{median}} = \lvert \operatorname{med}_{\mathrm{t}}(Y_i^{\mathrm{obs}}) - \operatorname{med}_{\mathrm{c}}(Y_i^{\mathrm{obs}}) \rvert$ 与 $T^{\mathrm{quant}} = \lvert q_{\delta,\mathrm{t}}(Y_i^{\mathrm{obs}}) - q_{\delta,\mathrm{c}}(Y_i^{\mathrm{obs}}) \rvert$，其中 $q_{\delta,\mathrm{t}}$ 是处理组的 $\delta$ 分位数，它们对异常值不敏感；
- $t$ 统计量
  $$
  T^{\text{t-stat}} = \left\lvert \frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}}} \right\rvert, \qquad
  s_{\mathrm{t}}^2 = \frac{1}{N_{\mathrm{t}} - 1}\sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2,
  $$
  其中 $s_{\mathrm{c}}^2$ 以同样方式定义，它考虑了两组方差不等。在 Fisher 的方法中使用时，它只是又一个统计量；并不需要它的 $t$ 分布。

### 3.2.2. 秩统计量

异常值与偏态分布会降低均值差的功效。把结果换成它们的秩，得到对两者都不敏感的统计量。秩是 [3.6.2](/3.6.2) 的主题；这里只需要一种以零为中心、并用平均秩处理结的版本。

**定义 3.2.1（规范化秩）** 单元 $i$ 在观测结果中的规范化秩为

$$
R_i = R_i\bigl(Y_1^{\mathrm{obs}}, \dots, Y_N^{\mathrm{obs}}\bigr) = \sum_{j=1}^{N}\boldsymbol{1}\bigl\{Y_j^{\mathrm{obs}} < Y_i^{\mathrm{obs}}\bigr\} + \frac{1}{2}\left(1 + \sum_{j=1}^{N}\boldsymbol{1}\bigl\{Y_j^{\mathrm{obs}} = Y_i^{\mathrm{obs}}\bigr\}\right) - \frac{N + 1}{2}.
$$
秩统计量是平均规范化秩之差的绝对值，

$$
T^{\operatorname{rank}} = \bigl\lvert \bar R_{\mathrm{t}} - \bar R_{\mathrm{c}} \bigr\rvert = \left\lvert \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1} R_i - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0} R_i \right\rvert.
$$

前两项给出通常的秩，结取其所占秩的平均，减去 $(N + 1)/2$ 使秩的和为零。由于秩是观测结果的函数，而观测结果在尖锐原假设下是固定的，$T^{\operatorname{rank}}$ 只是 $\boldsymbol{W}$ 的函数，其零分布的计算方式与 $T^{\mathrm{dif}}$ 相同。这个检验等价于 [3.2.6](/3.2.6) 的 **Wilcoxon 秩和检验**：在 $N_{\mathrm{t}}$ 固定时，处理组秩的和是 $\bar R_{\mathrm{t}} - \bar R_{\mathrm{c}}$ 的线性函数。在前六个蜂蜜单元中，观测结果 $(3, 5, 0, 4, 0, 1)$ 的秩为 $(4, 6, 1.5, 5, 1.5, 3)$，规范化秩为 $(0.5, 2.5, -2, 1.5, -2, -0.5)$，所以 $T^{\operatorname{rank}} = \lvert 1/3 - (-1/3) \rvert = 2/3$。

### 3.2.3. 基于模型的统计量与基于分布的统计量

统计量也可以由一个模型导出，该模型被认为在某个备择假设下近似潜在结果的分布。例如，若 $Y_i(0) \sim \mathcal{N}(\mu_{\mathrm{c}}, \sigma_{\mathrm{c}}^2)$ 且 $Y_i(1) \sim \mathcal{N}(\mu_{\mathrm{t}}, \sigma_{\mathrm{t}}^2)$，统计量可以取 $\mu_{\mathrm{t}} - \mu_{\mathrm{c}}$ 的极大似然估计，可能还要标准化；若 $\ln Y_i(0) \sim \mathcal{N}(\mu_{\mathrm{c}}, \sigma_{\mathrm{c}}^2)$ 且 $\ln Y_i(1) \sim \mathcal{N}(\mu_{\mathrm{t}}, \sigma_{\mathrm{t}}^2)$，则取对数正态模型下的相应估计。模型只用来选择统计量。即使模型是错的，检验仍然是精确的，因为零分布来自随机化；错误的模型只损失功效。

要检测两组结果分布之间的任何差异，而不仅是平移，可以用 Kolmogorov–Smirnov 统计量

$$
T^{\mathrm{ks}} = \sup_y \bigl\lvert \hat F_{\mathrm{t}}(y) - \hat F_{\mathrm{c}}(y) \bigr\rvert, \qquad
\hat F_{\mathrm{t}}(y) = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\boldsymbol{1}\bigl\{Y_i^{\mathrm{obs}} \le y\bigr\},
$$
其中 $\hat F_{\mathrm{c}}$ 以同样方式定义：它是经验分布函数之间的最大距离，如 [3.2.6](/3.2.6) 的两样本 **Kolmogorov–Smirnov 检验**。

### 3.2.4. 按功效选择统计量

由于每个统计量都给出有效的检验，选择应当由功效来决定：即在应用中合理的备择假设下，$H_0$ 为假时拒绝它的概率。一项模拟研究在水平 $\alpha = 0.1$ 下，在三个模型下比较均值差、中位数差与秩统计量：正态结果的可加效应、含异常值的可加效应、对数正态结果的可乘效应。

![Fisher 精确检验在水平 0.1 下的功效，比较均值差、中位数差与秩统计量，横轴为效应大小，分别在可加正态模型、含异常观测的可加模型与可乘对数正态模型下；模拟数据](./plots/fep_power.py)

结果呈现清晰的规律。

- 正态结果时，均值差是三者中最好的，但秩统计量几乎一样有功效；中位数明显更差。
- 有异常值时，均值差的功效大幅下降，而秩统计量与中位数统计量几乎不受影响。
- 偏态结果上的可乘效应时，秩统计量仍接近最好。

因此秩统计量是一个有吸引力的默认选择：它在所有情形下都有相对好的功效，并且对结果分布的形式稳健。其他统计量只在对它们有利的情形下表现良好，代价是在其他情形下功效相对较差。

### 3.2.5. 有多个分量的统计量

有时有几个感兴趣的备择假设（比如均值之差与方差之差），或每个单元有几个结果（蜂蜜实验中的咳嗽频率与严重程度）。分别用各自的统计量检验，再非正式地合并结论，会遇到多重检验问题：两个水平为 $\alpha$ 的检验，在 $H_0$ 下至少有一个拒绝的概率超过 $\alpha$。在 Fisher 的框架中，自然的解决办法是把各分量合并成单个统计量 $T^{\mathrm{comb}} = g(T^1, T^2)$，并以通常方式计算其精确零分布。两个结果的标准选择是 **Hotelling T² 统计量**形式的统计量，

$$
T^{\mathrm{Hotelling}} =
\begin{pmatrix} \bar Y_{\mathrm{t},1}^{\mathrm{obs}} - \bar Y_{\mathrm{c},1}^{\mathrm{obs}} \\ \bar Y_{\mathrm{t},2}^{\mathrm{obs}} - \bar Y_{\mathrm{c},2}^{\mathrm{obs}} \end{pmatrix}^{\mathsf T}
\left(\frac{\hat\Sigma_{\mathrm{c}}}{N_{\mathrm{c}}} + \frac{\hat\Sigma_{\mathrm{t}}}{N_{\mathrm{t}}}\right)^{-1}
\begin{pmatrix} \bar Y_{\mathrm{t},1}^{\mathrm{obs}} - \bar Y_{\mathrm{c},1}^{\mathrm{obs}} \\ \bar Y_{\mathrm{t},2}^{\mathrm{obs}} - \bar Y_{\mathrm{c},2}^{\mathrm{obs}} \end{pmatrix},
$$
其中 $\hat\Sigma_{\mathrm{t}}$ 与 $\hat\Sigma_{\mathrm{c}}$ 是两个结果在两组中的样本协方差矩阵。由于原假设是两个结果对任何单元都不受影响，单一的随机化分布涵盖两个分量，水平恰为 $\alpha$。

## 3.3. 计算 p 值

### 3.3.1. 精确 p 值

**定义 3.3.1（Fisher 精确 p 值）** 设 $T^{\mathrm{obs}} = T(\boldsymbol{W}^{\mathrm{obs}}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{X})$ 为统计量的观测值。在尖锐原假设下，令 $T(\boldsymbol{w})$ 表示分配 $\boldsymbol{w}$ 下统计量会取的值，由插补的潜在结果算出。**Fisher 精确 p 值**为

$$
p = \mathbb{P}_W\bigl(T(\boldsymbol{W}) \ge T^{\mathrm{obs}}\bigr) = \sum_{\boldsymbol{w} \in \mathcal{W}^+} \mathbb{P}(\boldsymbol{W} = \boldsymbol{w}) \, \boldsymbol{1}\bigl\{T(\boldsymbol{w}) \ge T^{\mathrm{obs}}\bigr\},
$$
在 CRE 中，它是 $\binom{N}{N_{\mathrm{t}}}$ 个可能分配中给出不小于观测值的统计量值的分配所占的比例。

p 值回答的问题是：如果原假设成立，统计量的观测值有多不寻常？$T(\boldsymbol{W})$ 在随机分配上的分布是统计量的精确零分布。它唯一的随机性来源是分配向量，所以对任何样本量结果都是精确的：既不涉及关于结果的模型，也不涉及渐近近似。

**例 3.3.1** 对六个蜂蜜单元，$\boldsymbol{W}^{\mathrm{obs}} = (1, 1, 1, 0, 0, 0)$，$T^{\mathrm{dif}, \mathrm{obs}} = \lvert (3 + 5 + 0)/3 - (4 + 0 + 1)/3 \rvert = \lvert 8/3 - 5/3 \rvert = 1$。在尖锐原假设下，结果 $(3, 5, 0, 4, 0, 1)$ 是固定的，三个处理单元的 $\binom{6}{3} = 20$ 个分配中每个的概率为 $1/20$。枚举它们得到 $T^{\mathrm{dif}}$ 的零分布：

| $T^{\mathrm{dif}}$ | $1/3$ | $1$ | $5/3$ | $7/3$ | $11/3$ |
|---|---|---|---|---|---|
| 分配个数 | 4 | 6 | 6 | 2 | 2 |

二十个分配中有十六个给出 $T^{\mathrm{dif}} \ge 1$，所以 $p = 16/20 = 0.80$。秩统计量的 $T^{\operatorname{rank}, \mathrm{obs}} = 2/3$，其零分布为

| $T^{\operatorname{rank}}$ | $0$ | $2/3$ | $1$ | $4/3$ | $5/3$ | $7/3$ | $3$ |
|---|---|---|---|---|---|---|---|
| 分配个数 | 4 | 4 | 2 | 4 | 2 | 2 | 2 |

同样 $p = 16/20 = 0.80$。没有证据反对无效应的假设。

![六个蜂蜜单元的 20 个分配上均值差绝对值的精确零分布，标出观测值 1；以及 72 个单元的模拟实验中均值差的随机化分布，及其由有限总体中心极限定理给出的正态近似](./plots/fep_null_distribution.py)

:::

这个结果与直觉相符吗？单元 2 接受了处理，之前的咳嗽频率最高，之后仍咳得很多；单元 4 是对照，之前的频率高，结果也高；处理单元与对照单元在之前的咳嗽上的差异，与在结果上的差异一样大。更根本的是，六个单元提供不了多少证据。每个分配与它的补（处理与对照互换）给出 $\lvert\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\rvert$ 的同一个值，所以统计量的每个值至少出现两次，最小可能的 p 值为 $2/20 = 0.10$：当 $N = 6$、$N_{\mathrm{t}} = 3$ 时，无论结果如何都不可能在 $5\%$ 水平上拒绝。没有功效的检验不能指望检测出效应，大的 p 值也不是没有效应的证据。

精确 p 值名副其实，因为无论统计量与样本量如何，它都精确地控制水平。

**定理 3.3.1（Fisher 精确检验的有效性）** 在尖锐原假设下，对每个 $\alpha \in [0, 1]$，

$$
\mathbb{P}_W(p \le \alpha) \le \alpha,
$$
当 $\alpha$ 是 $p$ 可能取的值之一时等号成立。

**证明** 在 $H_0$ 下，$\mathcal{W}^+$ 上的函数 $\boldsymbol{w} \mapsto T(\boldsymbol{w})$ 是固定的，观测到的统计量是 $T(\boldsymbol{W})$，其中 $\boldsymbol{W}$ 取自分配机制。令 $G(t) = \mathbb{P}_W(T(\boldsymbol{W}) \ge t)$，它是非增函数，所以 $p = G(T(\boldsymbol{W}))$。令 $t^* = \min\{t \in T(\mathcal{W}^+) : G(t) \le \alpha\}$，即尾概率至多为 $\alpha$ 的统计量的最小可取值（若不存在，则 $\mathbb{P}_W(p \le \alpha) = 0$）。由于 $G$ 非增，$p \le \alpha$ 当且仅当 $T(\boldsymbol{W}) \ge t^*$，因此 $\mathbb{P}_W(p \le \alpha) = G(t^*) \le \alpha$。若 $\alpha$ 是 $p$ 的一个可取值，则 $G(t^*) = \alpha$。$\square$

### 3.3.2. 模拟近似

精确枚举很快变得不可行：对完整的蜂蜜数据有 $\binom{72}{35} \approx 4.3 \times 10^{20}$ 个分配。通过模拟可以得到高精度的近似。从分配机制中独立抽取 $K$ 个分配向量 $\boldsymbol{W}^1, \dots, \boldsymbol{W}^K$，对每个计算统计量，并用下式估计 p 值

$$
\hat p = \frac{1}{K}\sum_{k=1}^{K}\boldsymbol{1}\bigl\{T(\boldsymbol{W}^k) \ge T^{\mathrm{obs}}\bigr\}.
$$
这些示性变量是成功概率为 $p$（真实 p 值）的独立 Bernoulli 变量，所以 $\hat p$ 无偏，标准误为

$$
\sqrt{\frac{p(1 - p)}{K}} \le \frac{1}{2\sqrt{K}},
$$
因为 $p(1 - p) \le 1/4$。抽取 $K = 10{,}000$ 次时标准误至多为 $0.005$，$K = 10^6$ 时至多为 $0.0005$，与单元个数无关。对蜂蜜数据与秩统计量，估计的 p 值为：

| 抽取次数 $K$ | 100 | 1,000 | 10,000 | 100,000 | 1,000,000 |
|---|---|---|---|---|---|
| $\hat p$ | 0.010 | 0.044 | 0.044 | 0.042 | 0.043 |
| 估计的标准误 | 0.010 | 0.006 | 0.002 | 0.001 | 0.000 |

抽取一百万次时 $p \approx 0.043$：数据提供了蜂蜜至少对一些儿童的咳嗽频率有影响的中等强度证据。

### 3.3.3. 大样本近似

对均值差，零分布有简单的大样本近似。在 $H_0$ 下，记 $y_i = Y_i(0) = Y_i(1)$，$\bar y = \frac{1}{N}\sum_i y_i$，$S^2 = \frac{1}{N - 1}\sum_{i=1}^{N}(y_i - \bar y)^2$，它们都是固定的。

**定理 3.3.2** 在 CRE 中，在 Fisher 尖锐原假设下，

$$
\mathbb{E}_W\bigl[\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr] = 0, \qquad
\operatorname{Var}_W\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr) = \frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}}\,S^2.
$$

**证明** 在 $H_0$ 下，处理组是从固定值 $y_1, \dots, y_N$ 中不放回抽取的大小为 $N_{\mathrm{t}}$ 的简单随机样本，$\bar Y_{\mathrm{t}}^{\mathrm{obs}}$ 是它的均值。由抽样理论，$\mathbb{E}_W[\bar Y_{\mathrm{t}}^{\mathrm{obs}}] = \bar y$，$\operatorname{Var}_W(\bar Y_{\mathrm{t}}^{\mathrm{obs}}) = (1/N_{\mathrm{t}} - 1/N)S^2 = \frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}S^2$（这也可由引理 4.3.1 得到）。由于 $N_{\mathrm{t}}\bar Y_{\mathrm{t}}^{\mathrm{obs}} + N_{\mathrm{c}}\bar Y_{\mathrm{c}}^{\mathrm{obs}} = N\bar y$，

$$
\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \frac{N\bar y - N_{\mathrm{t}}\bar Y_{\mathrm{t}}^{\mathrm{obs}}}{N_{\mathrm{c}}} = \frac{N}{N_{\mathrm{c}}}\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar y\bigr).
$$
因此期望为零，方差为 $\frac{N^2}{N_{\mathrm{c}}^2}\cdot\frac{N_{\mathrm{c}}}{NN_{\mathrm{t}}}S^2 = \frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}}S^2$。$\square$

[3.1.13](/3.1.13) 的**中心极限定理**针对独立观测，而 CRE 的处理组结果是不放回地取自有限总体的，彼此相依。适用的版本归功于 Hájek（1960）。

**定理 3.3.3（有限总体中心极限定理）** 设 $\bar y_n$ 是从有限总体 $y_1, \dots, y_N$（均值为 $\bar y$，方差为 $S^2 = \frac{1}{N - 1}\sum_i (y_i - \bar y)^2$）中不放回抽取的大小为 $n$ 的简单随机样本的均值，并考虑 $N \to \infty$ 的一列这样的总体。若

$$
\frac{1}{\min(n, N - n)} \cdot \frac{\max_{1 \le i \le N}(y_i - \bar y)^2}{S^2} \to 0,
$$
则

$$
\frac{\bar y_n - \bar y}{\sqrt{(1/n - 1/N)S^2}} \xrightarrow{d} \mathcal{N}(0, 1).
$$

这个条件说的是，样本与它的补集都增大，并且没有单个取值主导方差；例如当 $n/N$ 保持远离 $0$ 与 $1$、结果有界时（如蜂蜜数据）条件成立。把它应用于处理组并与定理 3.3.2 结合，在 $H_0$ 下得到

$$
\frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{\frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}}S^2}} \xrightarrow{d} \mathcal{N}(0, 1), \qquad N \to \infty.
$$
由于 $S^2$ 在 $H_0$ 下固定，这个标准化统计量是 $T^{\mathrm{dif}}$ 的单调函数，给出同一个精确检验；正态分布在大样本下近似它的零分布，如例 3.3.1 的图的右半部分所示。

这解释了为什么在大型随机化实验中，Fisher 检验与经典的两样本 $t$ 检验给出相近的答案，尽管 $t$ 检验假定结果服从正态分布。方差相等的两样本 $t$ 检验使用

$$
\frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{\frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}(N - 2)}\Bigl[\sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2 + \sum_{i:W_i = 0}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2\Bigr]}} \sim t_{N-2}
$$
（在正态性下）。把它与 $H_0$ 下总平方和的分解比较，

$$
(N - 1)S^2 = \sum_{i:W_i = 1}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{t}}^{\mathrm{obs}}\bigr)^2 + \sum_{i:W_i = 0}\bigl(Y_i^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2 + \frac{N_{\mathrm{t}}N_{\mathrm{c}}}{N}\bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr)^2.
$$
最后一项是一阶量，而组内平方和是 $N$ 阶的，所以 $N$ 大时，$t$ 统计量中的合并方差估计接近 $S^2$，$t$ 检验的 p 值（在 R 中由 `t.test` 与 `var.equal = TRUE` 计算）接近由有限总体中心极限定理得到的 p 值。同样，在 $H_0$ 下，

$$
\frac{\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}}{\sqrt{s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}}} \xrightarrow{d} \mathcal{N}(0, 1),
$$
所以方差不等的 **Welch t 检验**（`var.equal = FALSE`）也近似有效。R 函数 `wilcox.test` 与 `ks.test` 对秩统计量与 Kolmogorov–Smirnov 统计量计算精确或渐近的 p 值。对六个蜂蜜单元：

```r
y_obs <- c(3, 5, 0, 4, 0, 1)
w <- c(1, 1, 1, 0, 0, 0)
yt <- y_obs[w == 1]; yc <- y_obs[w == 0]

t.test(yt, yc, var.equal = TRUE)     # pooled two-sample t-test
t.test(yt, yc, var.equal = FALSE)    # Welch t-test
wilcox.test(yt, yc)                  # rank-sum test (normal approximation with ties)
ks.test(yt, yc)                      # two-sample Kolmogorov-Smirnov test

# Fisher's exact p-value by enumerating all 20 assignments
assignments <- combn(6, 3)
t_dif <- apply(assignments, 2, function(tr) abs(mean(y_obs[tr]) - mean(y_obs[-tr])))
t_obs <- abs(mean(yt) - mean(yc))
mean(t_dif >= t_obs - 1e-12)         # 0.8
```

只有六个单元时，渐近近似很差，只有枚举才给出精确答案 $0.80$；结果中有重复取值时，`wilcox.test` 退回到正态近似，而 Fisher 的方法通过规范化秩处理结，不需要任何改变。

## 3.4. 使用协变量

协变量不改变 Fisher 方法的有效性，但可以大幅提高它的功效，因为它们使统计量能够去掉结果中与处理无关的一部分变异。使用处理前协变量 $X_i$ 有三种常见方式。

- 增益得分。定义新的潜在结果 $Y_i'(w) = Y_i(w) - X_i$（$w = 0, 1$），观测值为 $Y_i'^{,\mathrm{obs}} = Y_i^{\mathrm{obs}} - X_i$。由于 $X_i$ 不受处理影响，$Y$ 的尖锐原假设等价于 $Y'$ 的尖锐原假设，我们可以用
  $$
  T^{\mathrm{gain}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}Y_i'^{,\mathrm{obs}} - \frac{1}{N_{\mathrm{c}}}\sum_{i:W_i = 0}Y_i'^{,\mathrm{obs}} = \bigl(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}\bigr) - \bigl(\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}}\bigr).
  $$
  修正项 $\bar X_{\mathrm{t}} - \bar X_{\mathrm{c}}$ 对随机化取平均为零，但在给定的分配中并不为零；减去它就去掉了结果差中由协变量的偶然失衡造成的部分。若 $X_i$ 与结果高度相关，$T^{\mathrm{gain}}$ 的方差就远小于普通均值差的方差。
- 比例变化，$Y_i'(w) = (Y_i(w) - X_i)/X_i$，用于正的协变量与比率尺度上的结果。
- 回归系数。用最小二乘把 $Y_i^{\mathrm{obs}}$ 对截距、$W_i$ 与 $X_i$ 回归，并以 $W_i$ 的估计系数作为统计量 $T^{\mathrm{reg\text{-}coef}}$。

最后一种选择引出几个问题。若回归模型是错的怎么办？检验仍然有效，因为零分布是通过对每个分配重新计算系数、由随机化算出的；模型只是定义了数据的一个函数。它更有效吗？通常是，如果协变量对结果有很好的预测力。系数的因果含义是什么？在 Fisher 的方法中不需要任何含义：系数只是一个统计量。把它解释为平均效应的估计，是 [3.9.5](/3.9.5) 的主题。

对完整的蜂蜜数据，用 $10^6$ 个模拟的分配，各统计量给出下面的取值与 p 值。取值带符号（处理减对照）；p 值是双侧的，$p = \mathbb{P}_W(\lvert T\rvert \ge \lvert T^{\mathrm{obs}}\rvert)$，$T^{\operatorname{rank}}$ 是平均秩之差。

| 统计量 | 取值 | p 值 |
|---|---|---|
| $T^{\mathrm{dif}}$ | $-0.697$ | 0.067 |
| $T^{\mathrm{quant}}$，$\delta = 0.25$ | $-1.000$ | 0.440 |
| $T^{\mathrm{quant}}$，$\delta = 0.50$ | $-1.000$ | 0.637 |
| $T^{\mathrm{quant}}$，$\delta = 0.75$ | $-1.000$ | 0.576 |
| $T^{\text{t-stat}}$ | $-1.869$ | 0.065 |
| $T^{\operatorname{rank}}$ | $-9.785$ | 0.043 |
| $T^{\mathrm{ks}}$ | $0.304$ | 0.021 |
| $T^{\mathrm{gain}}$ | $-0.967$ | 0.006 |
| $T^{\mathrm{reg\text{-}coef}}$ | $-0.911$ | 0.008 |

忽略协变量的统计量给出的 p 值在约 $0.02$ 到 $0.6$ 之间；分位数统计量功效很低，因为结果只取七个值，使分位数跳跃式变化。使用之前咳嗽频率的两个统计量给出低于 $0.01$ 的 p 值。这反映了之前与之后咳嗽频率之间的强相关：一旦考虑了儿童的基线差异，蜂蜜的效应就清楚得多。

## 3.5. Fisher 区间

Fisher 的方法检验假设，不估计效应。然而通过反演一族检验，仍可得到效应的区间。考虑常数可加效应的尖锐原假设，

$$
H_0(C)\colon\ Y_i(1) = Y_i(0) + C \quad \text{对 } i = 1, \dots, N.
$$
在 $H_0(C)$ 下，缺失的结果为：处理单元的 $Y_i(0) = Y_i^{\mathrm{obs}} - C$，对照单元的 $Y_i(1) = Y_i^{\mathrm{obs}} + C$，合适的统计量是 $\lvert \bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} - C \rvert$（或由调整后的结果 $Y_i^{\mathrm{obs}} - CW_i$ 算出的秩统计量，它们是 $H_0(C)$ 下的对照潜在结果）。在 $C$ 的网格上对每个 $C$ 计算精确 p 值，在水平 $\alpha$ 下未被拒绝的 $C$ 的取值集合，就是常数效应的 $1 - \alpha$ Fisher 区间。

**定义 3.5.1（Fisher 区间）** 水平 $1 - \alpha$ 的 **Fisher 区间**是这样的常数 $C$ 的集合：Fisher 对尖锐原假设 $H_0(C)$ 的精确检验在水平 $\alpha$ 下不拒绝。

由定理 3.3.1，若效应确实是常数且等于 $C_0$，则对 $H_0(C_0)$ 的检验以至多 $\alpha$ 的概率拒绝，所以区间以至少 $1 - \alpha$ 的概率包含 $C_0$。对以咳嗽频率为结果的蜂蜜数据，基于 $T^{\mathrm{dif}}$ 的 p 值在约 $C = -1.44$ 与 $C = 0.06$ 处等于 $0.05$，给出 $95\%$ Fisher 区间 $[-1.44, 0.06]$；在 $C = 0$ 处 p 值为 $0.067$，与 3.4 节的检验一致。秩统计量给出端点约为 $-2$ 与 $0$ 的区间；它的 p 值关于 $C$ 是分段常数，因为对整数结果，$Y_i^{\mathrm{obs}} - CW_i$ 的秩只在孤立的 $C$ 值处变化。Fisher 区间的解释依赖于常数效应的假设；当效应随单元而异时，平均效应更适合用 [3.9.4](/3.9.4) 中 Neyman 的方法研究。

## 小结

- Fisher 的方法检验尖锐原假设，典型的是对任何单元都无效应：对一切 $i$，$H_0\colon Y_i(0) = Y_i(1)$（定义 3.1.1）。在它之下所有缺失的潜在结果都已知，唯一的随机性是分配。
- 三个步骤：尖锐原假设；检验统计量 $T(\boldsymbol{W}, \boldsymbol{Y}^{\mathrm{obs}}, \boldsymbol{X})$；通过枚举得到的精确 p 值 $p = \mathbb{P}_W(T(\boldsymbol{W}) \ge T^{\mathrm{obs}})$（定义 3.3.1）。对任何统计量与任何样本量，检验都是精确的（定理 3.3.1）。
- 统计量：观测数据的任何函数都有效；按功效选择。

  | 统计量 | 擅长对付 |
  |---|---|
  | $T^{\mathrm{dif}}$、$T^{\text{t-stat}}$ | 可加平移，大致正态的结果 |
  | $T^{\log}$ | 可乘效应 |
  | $T^{\mathrm{median}}$、$T^{\mathrm{quant}}$ | 含异常值的平移 |
  | $T^{\operatorname{rank}}$（规范化秩，定义 3.2.1） | 平移，稳健的默认选择 |
  | $T^{\mathrm{ks}}$ | 分布的任何差异 |
  | $T^{\mathrm{gain}}$、$T^{\mathrm{reg\text{-}coef}}$ | 平移，利用有预测力的协变量 |
  | $T^{\mathrm{comb}}$、Hotelling | 多个结果或备择假设 |
- 计算：$N$ 小时枚举（六个蜂蜜单元：$p = 16/20 = 0.80$）；否则取 $K$ 次随机抽取，标准误至多为 $1/(2\sqrt K)$。在 $H_0$ 下，$\operatorname{Var}_W(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}) = \frac{N}{N_{\mathrm{t}}N_{\mathrm{c}}}S^2$（定理 3.3.2），有限总体中心极限定理（定理 3.3.3）使 Fisher 检验在大样本下接近两样本 $t$ 检验。
- 协变量提高功效而不影响有效性（蜂蜜：不用协变量 $p = 0.067$，用增益得分 $0.006$）。Fisher 区间反演常数效应 $H_0(C)$ 的检验（定义 3.5.1）。
- 局限：尖锐原假设限制很强，拒绝它并不估计效应的大小；这些由 Neyman 的方法解决。

## 思考题

1. 四个单元以 $N_{\mathrm{t}} = 2$ 完全随机化；观测结果 $Y^{\mathrm{obs}} = (7, 9, 2, 4)$，$\boldsymbol{W}^{\mathrm{obs}} = (1, 1, 0, 0)$。计算单侧统计量 $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$ 的精确零分布与单侧 p 值。这一设计所能给出的最小 p 值是多少？

   **答** 共有 $\binom{4}{2} = 6$ 个分配。处理对为 $\{1,2\}, \{1,3\}, \{1,4\}, \{2,3\}, \{2,4\}, \{3,4\}$ 时，处理组均值为 $8, 4.5, 5.5, 5.5, 6.5, 3$，对照组均值为 $3, 6.5, 5.5, 5.5, 4.5, 8$，所以差为 $5, -2, 0, 0, 2, -5$。观测值为 $5$，是最大的，$p = 1/6 \approx 0.17$。这是最小可能的单侧 p 值，所以任何数据都不能在 $10\%$ 水平上显著。
2. 证明在 $N_{\mathrm{t}} = N_{\mathrm{c}}$ 的 CRE 中，双侧统计量 $T^{\mathrm{dif}}$ 的每个取值至少出现两次，从而 $p \ge 2/\binom{N}{N/2}$。

   **答** 令 $\bar{\boldsymbol{w}} = \boldsymbol{1} - \boldsymbol{w}$ 为互补的分配；它也有 $N/2$ 个处理单元，所以属于 $\mathcal{W}^+$，且不同于 $\boldsymbol{w}$。在 $H_0$ 下它把两组互换，所以均值差变号，$T^{\mathrm{dif}}(\bar{\boldsymbol{w}}) = T^{\mathrm{dif}}(\boldsymbol{w})$。因此至少有两个分配，即观测到的分配及其补，满足 $T(\boldsymbol{w}) \ge T^{\mathrm{obs}}$，于是 $p \ge 2/\binom{N}{N/2}$。
3. 需要多少次随机抽取 $K$，才能保证模拟 p 值的 Monte Carlo 标准误至多为 $0.001$？若真实 p 值约为 $0.04$，要达到这一精度实际需要抽取多少次？

   **答** 由 $1/(2\sqrt K) \le 0.001$ 得 $K \ge 250{,}000$。若 $p \approx 0.04$，当 $K \ge 38{,}400$ 时标准误 $\sqrt{0.04 \times 0.96/K} \le 0.001$。
4. 在六个单元的蜂蜜例子中，用 $X = (4, 6, 4, 4, 1, 5)$ 计算观测分配下的 $T^{\mathrm{gain}}$。尽管 $X$ 不是潜在结果，为什么增益得分检验仍然有效？

   **答** 增益 $Y_i^{\mathrm{obs}} - X_i$ 为 $(-1, -1, -4, 0, -1, -4)$；处理组均值为 $-2$，对照组均值为 $-5/3$，所以 $T^{\mathrm{gain}} = -1/3$。因为 $X_i$ 是协变量，不受处理影响，尖锐原假设 $Y_i(1) = Y_i(0)$ 蕴含 $Y_i(1) - X_i = Y_i(0) - X_i$；在 $H_0$ 下增益是固定的，其随机化分布的计算与原结果完全相同。
5. 解释 Fisher 精确检验中的随机性与两个独立样本的置换检验中的随机性有何不同。在什么假设下两种计算是相同的？

   **答** 在 Fisher 检验中，单元及其潜在结果是固定的，随机性是分配，因为实验者做了随机化，所以它的分布已知；参照分布由设计提供依据。在两样本的置换检验中，随机性来自抽样，置换分布的依据是这样的假设：在原假设下观测是可交换的（例如独立同分布于同一分布）。两种计算是一致的：都对把合并的观测分成大小为 $N_{\mathrm{t}}$ 与 $N_{\mathrm{c}}$ 的两组的所有方式重新计算统计量；不同的是计算的依据，以及结论所指的对象。
6. 证明在 $H_0$ 下，标准化统计量 $(\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}})/\sqrt{NS^2/(N_{\mathrm{t}}N_{\mathrm{c}})}$ 与 $T^{\mathrm{dif}}$ 给出同一个精确 p 值，而 Welch 统计量 $T^{\text{t-stat}}$ 一般不然。

   **答** 在 $H_0$ 下，$S^2$ 由全部 $N$ 个结果算出，它们不依赖于分配，所以标准化统计量就是 $T^{\mathrm{dif}}$ 除以对每个 $\boldsymbol{w}$ 都相同的常数；分配的次序、从而 p 值不变。Welch 分母 $\sqrt{s_{\mathrm{c}}^2/N_{\mathrm{c}} + s_{\mathrm{t}}^2/N_{\mathrm{t}}}$ 依赖于结果如何在两组之间划分，所以随分配而变，并可能改变分配的次序；它定义的是另一个检验。
7. 描述如何为正结果的常数可乘效应 $Y_i(1) = C \cdot Y_i(0)$ 计算 $90\%$ Fisher 区间。

   **答** 对网格上的每个 $C > 0$，插补处理单元的 $Y_i(0) = Y_i^{\mathrm{obs}}/C$ 与对照单元的 $Y_i(1) = C\,Y_i^{\mathrm{obs}}$，于是调整后的结果 $Y_i^{\mathrm{obs}}/C^{W_i}$ 是 $H_0(C)$ 下固定的对照结果。用调整后结果的对数均值之差这样的统计量 $\lvert \overline{\ln Y}_{\mathrm{t}} - \overline{\ln Y}_{\mathrm{c}} - \ln C \rvert$，计算其精确（或模拟）p 值，保留所有满足 $p > 0.10$ 的 $C$。等价地，对 $\ln Y_i^{\mathrm{obs}}$ 应用可加的过程，再把端点取指数。
8. 蜂蜜数据给出 $T^{\mathrm{dif}}$ 的 $p = 0.067$ 与 $T^{\mathrm{gain}}$ 的 $p = 0.006$。一位同事建议报告给出较小 p 值的统计量。这样做有什么问题？有效地同时使用两者的办法是什么？

   **答** 看到 p 值之后才选统计量，会使报告的 p 值成为两个 p 值的最小值，它在 $H_0$ 下小于 $\alpha$ 的概率大于 $\alpha$；检验不再精确。统计量必须在看结果之前选定（可以利用协变量与设计）。要同时使用两者，应事先定义单个组合统计量，例如把 $T = \min(p^{\mathrm{dif}}, p^{\mathrm{gain}})$ 当作统计量（越小越极端），并对每个分配重新计算两个 p 值来得到其精确零分布；或者作 Bonferroni 校正。
