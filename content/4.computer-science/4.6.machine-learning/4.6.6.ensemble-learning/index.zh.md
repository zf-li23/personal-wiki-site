---
title: 集成学习
description: 集成为什么有效（多样性与偏差—方差）；弱学习器；加权多数算法及其错误界；Stacking；Bagging、随机森林与袋外误差；Boosting、AdaBoost 及其训练误差界；梯度提升与 XGBoost、LightGBM、CatBoost。
---

"三个臭皮匠，顶个诸葛亮。"集成学习把多个学习器的预测结合起来，得到比其中任何一个都更准确、更稳定的预测。它是经典机器学习中最有效的技术之一：随机森林与梯度提升树至今仍是表格数据上的首选方法，在数据竞赛中长期占据榜首。本章先说明集成为什么有效，再依次介绍四类结合方式：对同一数据上不同算法加权投票的加权多数算法，用另一个学习器学习如何结合的 Stacking，在自助样本上训练同一算法的 Bagging 与随机森林，以及顺序地关注"难"样本的 Boosting、AdaBoost 与梯度提升。基学习器常用 [4.5.6](/4.5.6) 的**决策树**；Bagging 建立在**自助法**（[3.5.7](/3.5.7)）之上，集成降低误差的机理可以用**偏差–方差权衡**来理解；评价集成效果的统计方法见 [4.6.7](/4.6.7)。

## 6.1. 集成学习简介

### 6.1.1. 基本想法

**定义 6.1.1（集成学习）** **集成学习**训练若干个学习器 $h_1, \dots, h_T$（称为基学习器或个体学习器），对新实例 $x$ 让每个学习器分别预测，再由一个结合策略把 $h_1(x), \dots, h_T(x)$ 合成最终的预测 $H(x)$。

结合并不总是有益。设三个分类器 $h_1, h_2, h_3$ 对三个样本的预测如下（✓ 为正确，✗ 为错误），用多数投票结合：

| | (a) 积极影响 | | | (b) 没有影响 | | | (c) 负面影响 | | |
|---|---|---|---|---|---|---|---|---|---|
| | 样本 1 | 样本 2 | 样本 3 | 样本 1 | 样本 2 | 样本 3 | 样本 1 | 样本 2 | 样本 3 |
| $h_1$ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ |
| $h_2$ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ |
| $h_3$ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ |
| 集成 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |

情形 (a) 中每个分类器的准确率都是 $2/3$，集成后为 $1$；(b) 中三个分类器完全相同，集成没有带来任何新信息；(c) 中每个分类器的准确率只有 $1/3$，集成后为 $0$。因此个体学习器要"好而不同"：效果不能太差，并且彼此要有差异（多样性）。

**命题 6.1.1** 设 $T$（奇数）个二分类器的错误率都是 $\varepsilon < 1/2$，且它们的错误相互独立，则多数投票的错误率为

$$
\mathbb{P}(H(x) \ne y) = \sum_{k > T/2} \binom{T}{k}\varepsilon^k(1 - \varepsilon)^{T - k} \le \exp\!\Big(-2T\big(\tfrac12 - \varepsilon\big)^2\Big),
$$
随 $T \to \infty$ 指数地趋于 0。

**证明** 犯错的分类器个数 $K \sim \mathrm{Bin}(T, \varepsilon)$（**二项分布**），多数投票出错当且仅当 $K > T/2$，这给出等式。不等式是 Hoeffding 不等式 $\mathbb{P}(K/T - \varepsilon \ge s) \le \mathrm{e}^{-2Ts^2}$ 在 $s = 1/2 - \varepsilon$ 时的情形。$\square$

例如 $\varepsilon = 0.3$ 时，11 个独立分类器的多数投票错误率约为 $0.078$，21 个约为 $0.026$。现实中各学习器在同一数据上训练，错误高度相关，达不到这样的效果；集成方法的核心就是用各种方式制造多样性：不同的算法（加权多数、Stacking）、不同的训练样本（Bagging）、不同的特征（随机森林）、不同的样本权重（Boosting）。

### 6.1.2. 为什么集成有效

Dietterich（2000）从三个角度解释集成的效果。设 $\mathcal{H}$ 是学习算法的**假设空间**，$f$ 是真实的目标概念。

1. 统计上：训练样本很少而 $\mathcal{H}$ 很大时，存在多个在训练集上同样准确的假设，任选一个都可能在测试集上表现很差；把它们平均可以降低选错的风险。
2. 计算上：学习算法（**决策树**的贪心构造、神经网络的梯度下降）只能找到局部最优，在 $\mathcal{H}$ 中穷举搜索全局最优代价太大；从不同起点出发得到的多个局部最优结合起来，往往比其中任何一个更接近 $f$。
3. 表示上：$\mathcal{H}$ 可能根本不包含 $f$，但若干假设的加权组合可以扩大可表示的函数类，例如轴平行的决策树桩组合起来可以逼近斜的或弯曲的决策边界。

此外，找到很多"大体正确"的经验法则很容易，找到一个高准确率的规则很难；集成正是把前者变成后者。从**偏差–方差权衡**的角度看，平均主要降低方差：

**命题 6.1.2** 设 $T$ 个预测 $Z_1, \dots, Z_T$ 的方差都是 $\sigma^2$，两两的相关系数都是 $\rho$，则

$$
\operatorname{Var}\Big(\frac1T\sum_{t=1}^T Z_t\Big) = \rho\sigma^2 + \frac{1 - \rho}{T}\sigma^2 .
$$

**证明** $\operatorname{Var}\big(\sum_t Z_t\big) = \sum_t \operatorname{Var}(Z_t) + \sum_{s \ne t}\operatorname{Cov}(Z_s, Z_t) = T\sigma^2 + T(T-1)\rho\sigma^2$，除以 $T^2$ 即得。$\square$

$T$ 增大时第二项消失，方差的下限是 $\rho\sigma^2$：要继续降低方差，就要降低个体学习器之间的相关性。平均不改变偏差，所以 Bagging 与随机森林适合低偏差、高方差的学习器（充分生长的决策树）；Boosting 则通过顺序地修正前面的错误来降低偏差，适合高偏差、低方差的简单学习器（决策树桩）。

### 6.1.3. 弱学习器与强学习器

**定义 6.1.2（弱学习器与强学习器）** 对二分类问题，若一个学习算法对任意的数据分布都能以高概率输出错误率不超过 $1/2 - \gamma$（某个固定的 $\gamma > 0$）的假设，即只比随机猜测略好，则称它为**弱学习器**；若对任意 $\varepsilon > 0$ 都能以高概率输出错误率不超过 $\varepsilon$ 的假设，则称它为**强学习器**。

Kearns 与 Valiant（1988）提出问题：弱可学习是否等价于强可学习，即能否把弱学习器"提升"为强学习器？Schapire（1990）给出了肯定的回答，构造了第一个多项式时间的 Boosting 算法；Freund（1990）改进了它；Freund 与 Schapire（1995）提出的 AdaBoost 不需要事先知道 $\gamma$，在实际中的优势很大，此后的研究进一步发展了理论和算法。

### 6.1.4. 结合策略

| 策略 | 做法 | 适用 |
|---|---|---|
| 简单平均 | $H(x) = \frac1T\sum_t h_t(x)$ | 回归、概率输出 |
| 加权平均 | $H(x) = \sum_t w_t h_t(x)$，$w_t \ge 0$，$\sum_t w_t = 1$ | 个体性能差异大时 |
| 多数投票 | 得票最多的类别 | 分类 |
| 加权投票 | 按权重 $w_t$ 计票 | 分类 |
| 软投票 | 平均各学习器给出的类别概率，取最大者 | 能输出概率的分类器 |
| 学习结合 | 用另一个学习器学习怎样结合 | Stacking |

下面各节的方法分别对应不同的权重来源：加权多数算法在线地调整权重，Stacking 学习结合方式，Bagging 等权投票，Boosting 按每轮的错误率确定权重。

## 6.2. 加权多数算法

加权多数算法（Littlestone 与 Warmuth，1994）结合一个算法池 $A = \{a_1, \dots, a_n\}$ 中的 $n$ 个预测算法，它们可以是任意的学习器，甚至是固定的规则。主算法为每个 $a_i$ 维护权重 $w_i$，按权重投票，并在出错时惩罚投错票的算法。

**算法 6.2.1（加权多数算法）** 设每个 $a_i$ 对输入 $x$ 输出 $\{0, 1\}$，惩罚系数 $\beta \in [0, 1)$。

1. 对一切 $i$，令 $w_i \leftarrow 1$。
2. 对每个训练样例 $\langle x, c(x)\rangle$：
   - 计算 $q_0 = \sum_{i : a_i(x) = 0} w_i$，$q_1 = \sum_{i : a_i(x) = 1} w_i$；若 $q_0 > q_1$ 则预测 $c'(x) = 0$，否则预测 $c'(x) = 1$（$q_0 = q_1$ 时任取）；
   - 若 $c'(x) \ne c(x)$，则对每个 $a_i(x) \ne c(x)$ 的算法令 $w_i \leftarrow \beta w_i$。

$\beta = 0$ 时，犯错的算法被直接淘汰，这就是 Halving 算法：若池中有一个永不出错的算法，每次主算法出错至少淘汰一半的权重，所以至多出错 $\log_2 n$ 次。另一种常见的版本无论主算法是否出错，都惩罚每个出错的 $a_i$；下面的错误界对两种版本都成立。算法容易推广到多类输出（对每个类别累计权重）。

**定理 6.2.1（加权多数算法的错误界）** 设算法池中最好的算法在样例序列上犯了 $m$ 次错误，则加权多数算法犯错的次数 $M$ 满足

$$
M \le \frac{\log_2 n + m\log_2(1/\beta)}{\log_2\big(2/(1 + \beta)\big)} .
$$

**证明** 记总权重 $W = \sum_i w_i$，初始 $W = n$。主算法每犯一次错，投错票的算法的权重之和至少为 $W/2$，它们都乘以 $\beta$，所以新的总权重至多为

$$
\frac W2 + \beta\cdot\frac W2 = \frac{1 + \beta}{2}\,W .
$$
主算法不犯错时 $W$ 不增加。于是犯 $M$ 次错之后 $W \le n\big(\frac{1+\beta}2\big)^M$。另一方面，最好的算法至多被惩罚 $m$ 次，权重至少为 $\beta^m$，而它不超过 $W$：

$$
\beta^m \le n\Big(\frac{1 + \beta}{2}\Big)^M .
$$
取以 2 为底的对数并整理即得。$\square$

取 $\beta = 1/2$ 时 $M \le 2.41\,(m + \log_2 n)$：主算法的错误次数至多是最好的算法的常数倍，再加上与池的大小成对数关系的一项。这里对样例序列没有任何概率假设，序列甚至可以由对手构造，所以它是在线学习中"与最好的专家竞争"的典型结果；它的连续版本（Hedge，乘性权重更新）在在线学习、博弈论和优化中有广泛应用。

## 6.3. Stacking

加权多数用固定的规则结合各算法；Stacking（堆叠，Wolpert，1992）把结合本身也当作一个学习问题。

**算法 6.3.1（Stacking）** 给定数据 $\{(x_i, y_i)\}_{i=1}^n$、$K$ 个基学习器 $M_1, \dots, M_K$（可以相同也可以不同）和一个次级学习器（元学习器，meta-learner）。

1. 用 $k$ 折**交叉验证**为每个样本生成基学习器的预测：对每一折，用其余各折训练 $M_1, \dots, M_K$，再对这一折中的 $x_i$ 预测，得到 $z_i = (\hat y_{i1}, \dots, \hat y_{iK})$；
2. 在新数据 $\{(z_i, y_i)\}$ 上训练次级学习器；
3. 用全部数据重新训练 $M_1, \dots, M_K$。预测时先由基学习器得到 $z = (\hat y_1, \dots, \hat y_K)$，再以次级学习器的输出作为最终预测。

第 1 步不能直接用在 $x_i$ 上训练过的基学习器来生成 $z_i$：那样得到的预测过于乐观，次级学习器会偏向最过拟合的基学习器。用交叉验证得到的"折外"预测（out-of-fold prediction）可以避免这种过拟合。次级学习器通常取简单的模型，如 **logistic 回归**或非负权重的线性回归（Breiman，1996）；基学习器的输出用类别概率比用类别标签效果更好。Stacking 可以结合任何方法，基学习器差异越大（如树模型、线性模型与 **k 近邻**），收益往往越大。

## 6.4. Bagging 与随机森林

### 6.4.1. 自助采样

如果只有一个学习算法，怎样得到多个不同的学习器？在不同的数据上训练就会得到不同的模型。朴素的做法是把训练集分成互不相交的子集，各训练一个模型，但每个子集太小，模型的效果不好。Bagging（Bootstrap AGGregatING，Breiman，1996）改用**自助法**（Efron，1979）产生训练集：从含 $m$ 个样本的训练集 $D$ 中均匀随机地有放回抽取 $m$ 次，得到**自助样本** $D_t$。

**命题 6.4.1** 一个给定的样本不出现在自助样本中的概率为 $(1 - 1/m)^m \to \mathrm{e}^{-1} \approx 0.368$（$m \to \infty$）。因此每个自助样本平均包含约 $63.2\%$ 的不同样本。

$m = 100$ 时这个概率已是 $0.366$。自助样本彼此有较大差异，又与原训练集同样大小，所以在它们上训练的学习器既各不相同，又各自不太差。

### 6.4.2. Bagging

**定义 6.4.1（Bagging）** **Bagging** 对 $t = 1, \dots, T$ 从训练集 $S$ 中自助采样得到 $D_t$，在 $D_t$ 上训练学习器 $H_t$；分类时对 $H_1(x), \dots, H_T(x)$ 等权多数投票，回归时取平均。

各个 $H_t$ 可以并行训练。Breiman 在多个数据集上把训练集的 $10\%$ 留作测试集，比较单棵决策树与 50 棵自助决策树多数投票的测试错误率，重复 100 次取平均，Bagging 使错误率显著下降；同样的实验换成 k 近邻分类器则几乎没有改进。原因在于学习器的稳定性："如果扰动训练集会使得到的预测器有很大变化，Bagging 就能提高准确率"（Breiman，1996）。决策树、神经网络、回归中的子集选择是不稳定的，训练集的微小差异就会产生大不相同的假设；k 近邻、线性回归是稳定的，各自助样本上的模型几乎一样，平均也就没有作用。这与命题 6.1.2 一致：Bagging 降低方差，对本身方差小的学习器帮助不大。

一般来说 $T$ 越大越好，但收益递减：Breiman 的分类实验中，自助样本超过 25 个之后改进就很小，再增加主要是增加计算量；与 Boosting 不同，增大 $T$ 不会使 Bagging 过拟合。

### 6.4.3. 袋外误差

每个样本大约不出现在 $36.8\%$ 的自助样本中，这些"袋外"（out-of-bag）的学习器没有见过它，可以用来无偏地评估它。

**定义 6.4.2（袋外误差）** 对每个训练样本 $x_i$，只用训练集中不含 $x_i$ 的那些学习器 $\{H_t : x_i \notin D_t\}$ 投票，得到袋外预测 $H^{\mathrm{oob}}(x_i)$。**袋外误差**是袋外预测在全部训练样本上的错误率

$$
\mathrm{err}_{\mathrm{oob}} = \frac1m\sum_{i=1}^m \boldsymbol{1}\{H^{\mathrm{oob}}(x_i) \ne y_i\} .
$$

袋外误差是 Bagging 训练时免费得到的泛化误差估计，作用类似于交叉验证，不需要另外留出验证集；$T$ 足够大时，它与留出法或交叉验证的估计相当接近，差异在估计本身的抽样误差范围内（[4.6.7](/4.6.7)）。它也常用来选择超参数，如随机森林每次分裂考虑的特征数。

### 6.4.4. 随机森林

随机森林（Breiman，2001）是以**决策树**为基学习器的 Bagging，再加上特征的随机性，进一步降低树与树之间的相关系数 $\rho$。

**算法 6.4.1（随机森林）** 设训练集有 $n$ 个样本、$p$ 个特征，参数为树的棵数 $T$ 和每次分裂考虑的特征数 $k$。

1. 对 $t = 1, \dots, T$：从训练集中自助采样 $n$ 个样本；在其上生长一棵决策树，树的每个结点都先从 $p$ 个特征中随机选出 $k$ 个，只在这 $k$ 个特征中寻找最优的分裂；树充分生长，不剪枝。
2. 分类时对 $T$ 棵树多数投票（回归时取平均）。

课件中的表述是"对每棵树随机选取 $p$ 个特征中的 $k$ 个来建树"，那是随机子空间方法（Ho，1998）；Breiman 的随机森林在每个结点重新选择特征，树之间的差异更大。常用的默认值是分类时 $k = \lfloor\sqrt p\rfloor$，回归时 $k = \lfloor p/3\rfloor$；$k = p$ 时退化为普通的 Bagging。$k$ 越小，单棵树越弱，但树之间越不相关。

随机森林的优点：

- 能学到特征之间的交互作用；特征的随机性缓解了过拟合；
- 每次分裂只考虑部分特征，便于处理高维数据；
- 训练可以并行，对**超参数**不敏感，几乎不需要调参；
- 通过自助采样的方式（如对少数类过采样）可以在一定程度上平衡不平衡数据集的误差；
- 能给出特征重要性：一是每个特征在所有分裂中带来的不纯度下降之和（MDI，偏向取值多的特征），二是置换重要性，即把袋外样本中某个特征的取值随机打乱后袋外误差的增加量。

缺点是噪声很大时仍会过拟合，且由几百棵树组成的模型失去了单棵决策树的可解释性。极端随机树（Extra-Trees，Geurts 等，2006）在随机选出的特征上再随机选择分裂阈值，进一步增加多样性并加快训练。

## 6.5. Boosting 与 AdaBoost

### 6.5.1. 基本想法

Bagging 的各个学习器独立地训练，彼此互不了解。Boosting 让学习器顺序地"从失败中学习"：

**定义 6.5.1（Boosting）** **Boosting** 给每个训练样本一个权重，进行 $T$ 轮迭代：每一轮在带权的样本上训练一个弱学习器 $C_t$，然后增大被 $C_t$ 分错的样本的权重、减小分对的样本的权重，使下一轮更关注"难"样本；最后把 $C_1, \dots, C_T$ 加权结合。

### 6.5.2. AdaBoost

AdaBoost（Adaptive Boosting，Freund 与 Schapire，1995）是最著名的 Boosting 算法。下面用 $y \in \{-1, +1\}$ 表示二分类的标签。

**算法 6.5.1（AdaBoost）** 输入训练集 $\{(x_i, y_i)\}_{i=1}^N$、弱学习算法和轮数 $T$。

1. 初始化样本权重 $D_1(i) = 1/N$。
2. 对 $t = 1, \dots, T$：
   - 在权重 $D_t$ 下训练弱学习器，得到 $h_t\colon \mathcal{X} \to \{-1, +1\}$；
   - 计算加权错误率 $\varepsilon_t = \sum_{i : h_t(x_i) \ne y_i} D_t(i)$，即所有分错的样本的权重之和；
   - 令 $\alpha_t = \frac12\ln\frac{1 - \varepsilon_t}{\varepsilon_t}$；
   - 更新权重：分对的样本乘以 $\mathrm{e}^{-\alpha_t}$，分错的乘以 $\mathrm{e}^{\alpha_t}$，即 $D_{t+1}(i) = D_t(i)\exp(-\alpha_t y_i h_t(x_i))/Z_t$，其中 $Z_t$ 是使 $\sum_i D_{t+1}(i) = 1$ 的归一化因子。
3. 输出 $H(x) = \operatorname{sgn}\big(F(x)\big)$，$F(x) = \sum_{t=1}^T \alpha_t h_t(x)$。

$\varepsilon_t < 1/2$ 时 $\alpha_t > 0$，错误率越小，$h_t$ 的投票权重越大。权重更新后，$h_t$ 在新权重下的加权错误率恰好是 $1/2$（分错的样本的权重之和从 $\varepsilon_t$ 变成 $\varepsilon_t \mathrm{e}^{\alpha_t}/Z_t = 1/2$），下一轮的弱学习器因此必须学到 $h_t$ 没有学到的东西。

课件中还有 AdaBoost.M1 的写法：若 $\varepsilon_t > 0.5$ 则停止；令 $\beta_t = \varepsilon_t/(1 - \varepsilon_t)$，分对的样本权重乘以 $\beta_t$，分错的不变，再归一化；最终投票权重为 $\log(1/\beta_t)$。由于 $\beta_t = \mathrm{e}^{-2\alpha_t}$，归一化后的权重与算法 6.5.1 完全相同，投票权重 $\log(1/\beta_t) = 2\alpha_t$ 也只差一个常数倍，所以两者是同一个算法。AdaBoost.M1 直接用于多类问题，但要求每个弱学习器的错误率低于 $1/2$，这对多类问题是很强的要求；SAMME（Zhu 等，2009）把权重改为 $\alpha_t = \ln\frac{1 - \varepsilon_t}{\varepsilon_t} + \ln(K - 1)$，只要求弱学习器好于 $K$ 类的随机猜测 $1 - 1/K$，是 scikit-learn 中 `AdaBoostClassifier` 的算法。

**例 6.5.1** Freund 与 Schapire 的教程中有一个平面上 10 个点的例子，弱学习器是水平或竖直的直线（决策树桩）。三轮的加权错误率和投票权重约为 $\varepsilon_1 = 0.30$，$\alpha_1 = 0.42$；$\varepsilon_2 = 0.21$，$\alpha_2 = 0.65$；$\varepsilon_3 = 0.14$，$\alpha_3 = 0.92$。最终分类器 $H = \operatorname{sgn}(0.42h_1 + 0.65h_2 + 0.92h_3)$ 把 10 个点全部分对，而任何一条直线都做不到。

### 6.5.3. 训练误差界

**定理 6.5.1（AdaBoost 的训练误差界）** 记 $\gamma_t = 1/2 - \varepsilon_t$。AdaBoost 输出的 $H$ 的训练错误率满足

$$
\frac1N\sum_{i=1}^N \boldsymbol{1}\{H(x_i) \ne y_i\} \le \prod_{t=1}^T Z_t = \prod_{t=1}^T 2\sqrt{\varepsilon_t(1 - \varepsilon_t)} = \prod_{t=1}^T\sqrt{1 - 4\gamma_t^2} \le \exp\Big(-2\sum_{t=1}^T\gamma_t^2\Big).
$$
特别地，若每一轮都有 $\gamma_t \ge \gamma > 0$，则训练错误率不超过 $\mathrm{e}^{-2T\gamma^2}$，随 $T$ 指数地下降。

**证明** 把权重更新式展开 $T$ 次：

$$
D_{T+1}(i) = D_1(i)\prod_{t=1}^T\frac{\exp(-\alpha_t y_i h_t(x_i))}{Z_t} = \frac{\exp(-y_i F(x_i))}{N\prod_t Z_t} .
$$
若 $H(x_i) \ne y_i$，则 $y_i F(x_i) \le 0$，$\exp(-y_i F(x_i)) \ge 1$；否则 $\exp(-y_iF(x_i)) > 0$。因此 $\boldsymbol{1}\{H(x_i) \ne y_i\} \le \exp(-y_i F(x_i))$，对 $i$ 平均并用上式，

$$
\frac1N\sum_i\boldsymbol{1}\{H(x_i) \ne y_i\} \le \frac1N\sum_i\exp(-y_iF(x_i)) = \sum_i D_{T+1}(i)\prod_t Z_t = \prod_t Z_t .
$$
再计算 $Z_t$：分对的样本贡献 $\mathrm{e}^{-\alpha_t}$ 倍的权重，分错的贡献 $\mathrm{e}^{\alpha_t}$ 倍，

$$
Z_t = (1 - \varepsilon_t)\mathrm{e}^{-\alpha_t} + \varepsilon_t\mathrm{e}^{\alpha_t} .
$$
代入 $\mathrm{e}^{\alpha_t} = \sqrt{(1 - \varepsilon_t)/\varepsilon_t}$ 得 $Z_t = 2\sqrt{\varepsilon_t(1 - \varepsilon_t)} = \sqrt{(1 - 2\gamma_t)(1 + 2\gamma_t)} = \sqrt{1 - 4\gamma_t^2}$。最后由 $1 + x \le \mathrm{e}^x$ 得 $\sqrt{1 - 4\gamma_t^2} \le \sqrt{\mathrm{e}^{-4\gamma_t^2}} = \mathrm{e}^{-2\gamma_t^2}$。$\square$

证明还说明了 $\alpha_t$ 的来历：$Z_t$ 作为 $\alpha_t$ 的函数是凸的，令导数 $-(1 - \varepsilon_t)\mathrm{e}^{-\alpha_t} + \varepsilon_t\mathrm{e}^{\alpha_t} = 0$ 恰好得到 $\alpha_t = \frac12\ln\frac{1 - \varepsilon_t}{\varepsilon_t}$。所以 AdaBoost 每一轮都在贪心地最小化训练误差的上界 $\prod_t Z_t$。由定理 6.5.1，当 $T > \ln N/(2\gamma^2)$ 时训练错误率小于 $1/N$，即为 0：只要每一轮的弱学习器都比随机猜测略好，AdaBoost 就能把训练集完全分对。这正面回答了弱学习器能否提升为强学习器的问题。

![AdaBoost 用决策树桩学习圆形的概念。左：200 轮后的决策区域（虚线是真实边界），由轴平行的线段拼成；右：训练误差的上界、训练误差与测试误差随轮数的变化（横轴为对数刻度），训练误差降为 0 之后测试误差仍保持在低位](./plots/adaboost-error.py)

### 6.5.4. 指数损失与间隔

Friedman、Hastie 与 Tibshirani（2000）指出，AdaBoost 是在用前向分步的方式拟合加性模型 $F(x) = \sum_t\alpha_t h_t(x)$，所最小化的是指数损失

$$
L(y, F(x)) = \exp(-yF(x)) .
$$
第 $t$ 步固定 $F_{t-1}$，求 $\sum_i\exp\big(-y_i(F_{t-1}(x_i) + \alpha h(x_i))\big) = \sum_i w_i\exp(-\alpha y_i h(x_i))$ 的最小值，其中 $w_i = \exp(-y_iF_{t-1}(x_i)) \propto D_t(i)$：对 $h$ 最小化就是在权重 $D_t$ 下最小化加权错误率，对 $\alpha$ 最小化就得到上面的 $\alpha_t$。指数损失的总体最小值点是 $F^*(x) = \frac12\ln\frac{\mathbb{P}(y = 1 \mid x)}{\mathbb{P}(y = -1 \mid x)}$，所以 $F$ 还可以换算成类别概率。这一观点把 Boosting 与统计中的加性模型、**损失函数**联系起来，并导出了下一节的梯度提升。

实验中常看到训练误差降为 0 之后，继续增加轮数测试误差仍在下降。Schapire 等（1998）用间隔解释这一现象：样本的间隔 $y_iF(x_i)/\sum_t\alpha_t \in [-1, 1]$ 衡量分类的把握，继续迭代会增大训练样本的间隔，而泛化误差的上界随间隔增大而减小。

AdaBoost 实用上的优点是：快，简单，容易实现；除了轮数 $T$ 几乎没有参数要调；不需要关于弱学习器的先验知识，可以与任何学习器结合（神经网络、C4.5 决策树等）；只要求弱学习器比随机猜测好一些，这改变了设计学习算法的思路。它的效果依赖于数据和弱学习器：弱学习器太复杂会过拟合；太弱则 $\alpha_t$ 很快趋于 0，导致欠拟合，或者间隔太小而过拟合。指数损失对分错的样本惩罚极重，标签噪声多时噪声样本的权重会越来越大，所以 AdaBoost 对噪声比较敏感。

### 6.5.5. 重新加权与重新采样

有些学习方法无法使用样本权重，很多常用工具包也不支持带权的训练集。这时可以重新采样代替重新加权：按 $D_t$ 给出的概率对训练集做有放回抽样，在抽得的样本上训练 $h_t$。一般来说重新加权效果更好，重新采样更容易实现。

## 6.6. 梯度提升

### 6.6.1. 函数空间中的梯度下降

AdaBoost 是对指数损失的前向分步拟合。Friedman（2001）把这一思想推广到任意可微的损失 $L(y, F)$：把 $F$ 在训练样本上的取值 $(F(x_1), \dots, F(x_N))$ 看作变量，沿损失的负梯度方向一步步改进，每一步用一棵回归树拟合负梯度，这就是函数空间中的**梯度下降法**。

**算法 6.6.1（梯度提升）** 输入训练集、可微损失 $L$、轮数 $M$、学习率 $\nu \in (0, 1]$。

1. 初始化为最优常数 $F_0(x) = \arg\min_c\sum_i L(y_i, c)$。
2. 对 $m = 1, \dots, M$：
   - 计算伪残差 $r_{im} = -\left.\dfrac{\partial L(y_i, F)}{\partial F}\right|_{F = F_{m-1}(x_i)}$；
   - 用一棵回归树拟合 $\{(x_i, r_{im})\}$，得到叶结点区域 $R_{1m}, \dots, R_{Jm}$；
   - 对每个叶结点求最优的取值 $c_{jm} = \arg\min_c\sum_{x_i \in R_{jm}} L(y_i, F_{m-1}(x_i) + c)$；
   - 更新 $F_m(x) = F_{m-1}(x) + \nu\sum_{j=1}^J c_{jm}\boldsymbol{1}\{x \in R_{jm}\}$。
3. 输出 $F_M$。

平方损失 $L = \frac12(y - F)^2$ 的伪残差就是普通的残差 $y_i - F_{m-1}(x_i)$，每一棵树拟合前面的树没有解释的部分。二分类用对数损失（logistic 损失）时伪残差是 $y_i - p_i$，$p_i$ 是当前模型给出的正类概率。学习率 $\nu$（收缩，常取 $0.01$ 到 $0.1$）越小，需要的树越多，泛化通常越好；每轮只用一部分随机样本拟合（随机梯度提升，Friedman，2002）既加快训练又起正则化作用。与 Bagging 不同，梯度提升的轮数过多会过拟合，通常用验证集上的早停来确定 $M$。

### 6.6.2. XGBoost、LightGBM 与 CatBoost

梯度提升决策树（GBDT）的三个主流实现在算法上各有改进，都支持并行与 GPU 训练，是目前表格数据上最常用的模型。

- XGBoost（Chen 与 Guestrin，2016）对损失做二阶 Taylor 展开，并在目标中加入树复杂度的正则项 $\Omega(f) = \gamma J + \frac12\lambda\sum_{j=1}^J w_j^2$（$J$ 是叶结点数，$w_j$ 是叶结点的取值）。记叶结点 $j$ 中样本的一阶、二阶导数之和为 $G_j$、$H_j$，则最优取值为 $w_j^* = -G_j/(H_j + \lambda)$，把一个结点分成左右两部分的增益为

  $$
  \frac12\left[\frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda}\right] - \gamma ,
  $$
  增益为负就不分裂。它还能自动学习缺失值应该走哪个分支。
- LightGBM（Ke 等，2017）把特征值分箱成直方图来寻找分裂点，按叶结点（选增益最大的叶结点分裂）而不是按层生长，并用基于梯度的单边采样（GOSS，保留梯度大的样本、对梯度小的样本抽样）和互斥特征捆绑（EFB）减少计算，在大数据上很快。scikit-learn 的 `HistGradientBoostingClassifier` 采用了类似的直方图算法。
- CatBoost（Prokhorenkova 等，2018）用有序提升（ordered boosting）避免用同一样本既计算梯度又拟合所造成的预测偏移，并原生支持类别型特征（有序的目标统计量编码），默认参数下就有很好的效果。

在中小规模的表格数据上，经过调参的梯度提升树通常仍优于深度神经网络（Grinsztajn 等，2022）；近年预训练的表格基础模型（如 TabPFN，Hollmann 等，2025）在小数据集上已能与之竞争。

## 6.7. Bagging 与 Boosting 的比较

| | Bagging | Boosting |
|---|---|---|
| 训练集 | 随机有放回抽样，各轮训练集相互独立 | 依赖于前一轮的学习结果，各轮不独立 |
| 结合 | 等权投票或平均 | 按错误率加权，权重呈指数变化 |
| 计算 | 可以并行 | 只能顺序进行 |
| 主要降低 | 方差 | 偏差（也降低方差） |
| 适合的基学习器 | 不稳定、低偏差（深决策树） | 弱、高偏差（决策树桩、浅树） |
| 轮数过多 | 不会过拟合 | 可能过拟合，需要早停 |
| 噪声数据 | 受影响较小 | 性能可能明显下降 |

实际中 Bagging 几乎总是有帮助；平均而言 Boosting 比 Bagging 更好一些，但也更常出现损害性能的情况。对稳定的模型 Bagging 效果不明显，Boosting 可能仍然有效。

## 6.8. 实践

下面用 scikit-learn 比较单棵**决策树**与几种集成方法（5 折交叉验证的准确率），并比较随机森林的袋外估计与留出测试集上的准确率：

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import (AdaBoostClassifier, BaggingClassifier, HistGradientBoostingClassifier,
                              RandomForestClassifier, StackingClassifier)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

X, y = make_classification(n_samples=2000, n_features=20, n_informative=8,
                           n_redundant=4, flip_y=0.05, random_state=0)
models = {
    "decision tree": DecisionTreeClassifier(random_state=0),
    "bagging (trees)": BaggingClassifier(DecisionTreeClassifier(), n_estimators=200, random_state=0),
    "random forest": RandomForestClassifier(n_estimators=200, random_state=0),
    "AdaBoost (stumps)": AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                                            n_estimators=200, random_state=0),
    "gradient boosting": HistGradientBoostingClassifier(random_state=0),
    "stacking": StackingClassifier(
        estimators=[("rf", RandomForestClassifier(n_estimators=200, random_state=0)),
                    ("knn", KNeighborsClassifier(n_neighbors=15))],
        final_estimator=LogisticRegression(), cv=5),
}
for name, model in models.items():
    acc = cross_val_score(model, X, y, cv=5)
    print(f"{name:18s} accuracy = {acc.mean():.3f} +- {acc.std():.3f}")

# out-of-bag estimate versus a held-out test set
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
rf = RandomForestClassifier(n_estimators=300, oob_score=True, random_state=0).fit(Xtr, ytr)
print(f"random forest: OOB accuracy {rf.oob_score_:.3f}, test accuracy {rf.score(Xte, yte):.3f}")
```

```text
decision tree      accuracy = 0.815 +- 0.011
bagging (trees)    accuracy = 0.895 +- 0.011
random forest      accuracy = 0.900 +- 0.014
AdaBoost (stumps)  accuracy = 0.882 +- 0.008
gradient boosting  accuracy = 0.907 +- 0.013
stacking           accuracy = 0.900 +- 0.012
random forest: OOB accuracy 0.892, test accuracy 0.917
```

单棵决策树的准确率约为 $0.82$，各种集成方法都提高到 $0.88$ 到 $0.91$，梯度提升最高。随机森林的袋外准确率与 600 个测试样本上的准确率相差 $0.025$，在测试集准确率的抽样误差（标准差约 $\sqrt{0.9 \times 0.1/600} \approx 0.012$）的两倍左右。这里的差异是否足以说明一种方法优于另一种，要用 [4.6.7](/4.6.7) 的检验方法来判断。

## 小结

| 方法 | 多样性来源 | 结合方式 | 要点 |
|---|---|---|---|
| 加权多数 | 不同的算法 | 加权投票，出错时乘以 $\beta$ | 错误数 $\le 2.41(m + \log_2 n)$（$\beta = 1/2$） |
| Stacking | 不同的算法 | 次级学习器 | 用折外预测训练次级学习器 |
| Bagging | 自助样本 | 等权投票或平均 | 降低方差；袋外误差 |
| 随机森林 | 自助样本 + 每个结点的随机特征 | 等权投票或平均 | 降低树间相关性；特征重要性 |
| AdaBoost | 样本权重 | $\alpha_t = \frac12\ln\frac{1-\varepsilon_t}{\varepsilon_t}$ 加权 | 训练误差 $\le \exp(-2\sum_t\gamma_t^2)$；指数损失 |
| 梯度提升 | 拟合负梯度 | 加性模型，学习率 $\nu$ | 任意可微损失；XGBoost、LightGBM、CatBoost |

集成的效果来自个体学习器"好而不同"：Bagging 类方法并行地平均掉方差，Boosting 类方法顺序地修正偏差。
