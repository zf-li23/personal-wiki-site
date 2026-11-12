---
title: 由因果图识别因果效应
description: 由干预定义的平均因果效应；重访 Simpson 悖论与调整公式，及其逆倾向加权形式和 Rubin 与 Pearl 记号的对照；后门路径、后门准则与后门调整定理（附证明）；前门准则（吸烟、焦油与肺癌）；受控直接效应、do 演算的三条规则、其完备性与识别算法。
source_hash: d23e3a0830c3
---

在 [3.9.11](/3.9.11) 中，因果 Bayes 网络是由干预下发生的事情定义的：每个机制 $\mathbb{P}(v_i \mid \mathrm{pa}_i)$ 保持不变，干预 $\operatorname{do}(X = x)$ 则移除 $X$ 的机制。有了这样的模型，$X$ 对 $Y$ 的平均因果效应就是干预分布的性质。但数据通常来自对系统的观察而不是对它的干预，而且使计算变得容易的那些变量往往没有被测量。本章要问：给定因果图，何时可以由所测变量的观察分布计算干预分布 $\mathbb{P}(y \mid \operatorname{do}(x))$，并给出公式。答案是一些图形判据：后门准则，它告诉我们应当对哪些协变量做调整，是 [3.9.2](/3.9.2) 与 [3.9.8](/3.9.8) 的**无混杂性**的图形对应；前门准则，它即使在处理与结果存在未测量的混杂因素时也能识别效应；以及 do 演算，它处理所有可识别的情形。[3.9.13](/3.9.13) 将转向寻找图本身的问题。

## 12.1. 平均因果效应

**定义 12.1.1（因果图中的平均因果效应）** 设 $G$ 是含有变量 $X$ 与 $Y$ 的因果 Bayes 网络。把 $X$ 由 $x_2$ 变为 $x_1$ 对 $Y$ 的平均因果效应为

$$
\mathrm{ACE} = \mathbb{E}[Y \mid \operatorname{do}(X = x_1)] - \mathbb{E}[Y \mid \operatorname{do}(X = x_2)]
= \sum_y y\,\mathbb{P}(Y = y \mid \operatorname{do}(X = x_1)) - \sum_y y\,\mathbb{P}(Y = y \mid \operatorname{do}(X = x_2)).
$$
对二值的 $X$ 与 $Y$，它就是 $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) - \mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0))$。

该定义设想对整个总体做两次假想的干预：让每个人都取 $X = x_1$，再让每个人都取 $X = x_2$，并比较平均结果。它就是 [3.9.1](/3.9.1) 中超总体意义下的**平均处理效应**（§12.2.3）。若能实施这些干预，如在随机化实验中，我们就能直接估计这两个干预分布。有了观察数据，我们只有 $\mathbb{P}(v)$，问题是 $\mathbb{P}(y \mid \operatorname{do}(x))$ 是否由 $\mathbb{P}(v)$ 与 $G$ 决定。当它对每个与 $G$ 相容的分布（在有关取值处为正）都被决定时，就说该效应可由 $G$ 识别；通过观察量表示它的公式就是识别公式，此时估计问题归结为估计公式中的观察量。

## 12.2. 重访 Simpson 悖论

### 12.2.1. 例子

**例 12.2.1（药物、康复与性别）** 在一项新药的研究中，$X = 1$ 表示服药，$Y = 1$ 表示康复，$Z = 1$ 表示男性。700 名患者的数据如下（**Simpson 悖论**的经典例证）：

| | 服药（$X = 1$） | 不服药（$X = 0$） |
|---|---|---|
| 男性（$Z = 1$） | 87 人中 81 人康复（93%） | 270 人中 234 人康复（87%） |
| 女性（$Z = 0$） | 263 人中 192 人康复（73%） | 80 人中 55 人康复（69%） |
| 合并 | 350 人中 273 人康复（78%） | 350 人中 289 人康复（83%） |

对男性药物更好，对女性药物也更好，但对合并的总体药物更差。医生应当依据哪个结论采取行动？假设我们知道性别既影响是否服药（女性更可能服药），也影响康复的机会（无论服药与否，女性康复的比例都较低），且药物不会改变人的性别：因果图为 $Z \to X$，$Z \to Y$，$X \to Y$。于是合并后的比较混合了药物的效应与性别的效应，因为服药组主要是女性。答案取决于因果故事，而不取决于表格：若数字相同，但 $Z$ 是血压之类的处理后变量，则合并后的比较才是正确的。

### 12.2.2. 调整公式

要计算 $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = x))$，考虑被操纵的模型 $\mathbb{P}_m(\cdot) = \mathbb{P}(\cdot \mid \operatorname{do}(X = x))$，它的图 $G_{\overline{X}}$ 失去了箭头 $Z \to X$。它的两个成分是未改变的机制，另有一个独立性可以从新图中读出：

1. $\mathbb{P}_m(Y = y \mid X = x, Z = z) = \mathbb{P}(Y = y \mid X = x, Z = z)$：$Y$ 的机制未被触动；
2. $\mathbb{P}_m(Z = z) = \mathbb{P}(Z = z)$：$Z$ 的机制未被触动；
3. 在 $G_{\overline{X}}$ 中，$Z$ 与 $X$ 被 d-分离，所以 $\mathbb{P}_m(Z = z \mid X = x) = \mathbb{P}_m(Z = z)$。

因此，在被操纵的模型中由全概率公式，

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}_m(y \mid x, z)\,\mathbb{P}_m(z \mid x) = \sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z).
\tag{12.1}
$$
这就是调整公式（adjustment formula）：先在 $Z$ 的每个水平内计算效应，再以总体权重 $\mathbb{P}(z)$ 而不是处理组或未处理组的权重 $\mathbb{P}(z \mid x)$ 对各水平取平均。由截断分解 (11.3) 一行就能得到同样的结果：$\mathbb{P}(y, z \mid \operatorname{do}(x)) = \mathbb{P}(z)\,\mathbb{P}(y \mid x, z)$。

**例 12.2.2** 在例 12.2.1 中，$\mathbb{P}(Z = 1) = 357/700 = 0.51$。用精确的组内比率，

$$
\begin{aligned}
\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) &= \tfrac{81}{87}(0.51) + \tfrac{192}{263}(0.49) \approx 0.4748 + 0.3577 = 0.833,\\
\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0)) &= \tfrac{234}{270}(0.51) + \tfrac{55}{80}(0.49) \approx 0.4420 + 0.3369 = 0.779,
\end{aligned}
$$
所以 $\mathrm{ACE} \approx 0.054$（用取整后的百分比 $0.93$、$0.73$、$0.87$、$0.69$ 则得 $0.832 - 0.782 = 0.050$）。在所述的因果故事下，服药使康复概率提高约五个百分点，与朴素比较的 $0.78 - 0.83 = -0.05$ 恰好相反。

:::

(12.1) 中的调整是对 $X$ 的父节点做的。这个论证在任何因果 Bayes 网络中都成立。

**定理 12.2.1（对直接原因的调整）** 设 $\mathrm{PA}_X$ 是因果 Bayes 网络中 $X$ 的父节点集，$Y$ 是不在 $\mathrm{PA}_X \cup \{X\}$ 中的变量。则

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_{\mathrm{pa}} \mathbb{P}(y \mid x, \mathrm{pa})\,\mathbb{P}(\mathrm{pa}),
$$
其中求和遍历 $\mathrm{PA}_X$ 的取值。

**证明** 由截断分解 (11.3)，对与 $x$ 一致的 $v$ 有 $\mathbb{P}(v \mid \operatorname{do}(x)) = \mathbb{P}(v)/\mathbb{P}(x \mid \mathrm{pa}_X)$，即 $\mathbb{P}(v \mid \operatorname{do}(x)) = \mathbb{P}(v \setminus \{x, \mathrm{pa}_X\} \mid x, \mathrm{pa}_X)\,\mathbb{P}(\mathrm{pa}_X)$。对除 $Y$ 与 $\mathrm{PA}_X$ 之外的所有变量求和，得 $\mathbb{P}(y, \mathrm{pa} \mid \operatorname{do}(x)) = \mathbb{P}(y \mid x, \mathrm{pa})\,\mathbb{P}(\mathrm{pa})$，再对 $\mathrm{pa}$ 求和即得结论。$\square$

### 12.2.3. 与潜在结果框架的联系

把 (12.1) 乘以并除以 $\mathbb{P}(x \mid z)$，得到等价的形式

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \frac{\mathbb{P}(x, y, z)}{\mathbb{P}(x \mid z)},
\tag{12.2}
$$
其中每个 $X = x$ 的观测都按它在给定 $Z$ 时实际接受的处理的概率的倒数加权。$\mathbb{P}(X = 1 \mid z)$ 就是**倾向评分**，(12.2) 的样本版本就是 [3.9.8](/3.9.8) 与 [3.9.10](/3.9.10) 的**逆概率加权**（Horvitz–Thompson）估计量：用 Rubin 的记号，$\mathbb{E}[Y \mid \operatorname{do}(X = 1)] = \mathbb{E}[W Y / e(X)]$。当 $Z$ 是高维的、倾向评分比结果更容易建模时，加权形式很有用。

两个框架对相同的角色使用不同的字母。

| 角色 | Rubin（3.9.1–3.9.10、3.9.14） | Pearl（3.9.11–3.9.13） |
|---|---|---|
| 处理 | $W$ | $X$ |
| 处理前协变量 | $X$ | $Z$ |
| 结果 | $Y^{\mathrm{obs}}$，潜在结果为 $Y(0)$、$Y(1)$ | $Y$；结构模型中为 $Y_x$ |
| 平均效应 | $\tau_{\mathrm{sp}} = \mathbb{E}[Y(1) - Y(0)]$ | $\mathbb{E}[Y \mid \operatorname{do}(X = 1)] - \mathbb{E}[Y \mid \operatorname{do}(X = 0)]$ |
| 无未测量的混杂 | $W \perp (Y(0), Y(1)) \mid X$ | $Z$ 满足后门准则 |
| 调整 | 分层，以 $e(X)$ 加权 | $\sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z)$ |

对二值的 $W$ 与 $Y$，$\mathbb{P}(Y = 1 \mid \operatorname{do}(W = 1)) - \mathbb{P}(Y = 1 \mid \operatorname{do}(W = 0)) = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)] = \tau_{\mathrm{sp}}$，因为 $Y(w)$ 是单位在 $\operatorname{do}(W = w)$ 下会有的结果。在例 12.2.1 中，调整公式就是以性别为层的分层估计量；等价地，也就是倾向评分为 $\mathbb{P}(X = 1 \mid Z = 1) = 87/357$ 与 $\mathbb{P}(X = 1 \mid Z = 0) = 263/343$ 的加权估计量。

## 12.3. 后门准则

### 12.3.1. 准则

对 $X$ 的父节点做调整（定理 12.2.1）是最自然的选择，但父节点可能没有被测量（比如医生开药的理由），或者数量很多。我们需要同样好的其他变量集。例 12.2.1 中可以看出，指导原则有三条：阻断 $X$ 与 $Y$ 之间所有虚假的路径，保持从 $X$ 到 $Y$ 的所有有向路径不受扰动，并且不产生新的虚假路径。

**定义 12.3.1（后门路径）** 从 $X$ 到 $Y$ 的**后门路径**是 $X$ 与 $Y$ 之间第一条边指向 $X$ 的路径，即形如 $X \leftarrow \cdots\, Y$ 的路径。

后门路径是关联在 $X$ 与 $Y$ 之间流动的非因果通道：它们从 $X$ 的原因出发，"从后门"到达 $X$。有向路径 $X \to \cdots \to Y$ 承载我们想测量的效应。其他从 $X$ 向前出发并经过对撞因子到达 $Y$ 的路径（$X \to M \leftarrow \cdots\, Y$）则不传递关联，除非我们对该对撞因子取条件。

**定义 12.3.2（后门准则）** 若 DAG $G$ 中的变量集 $Z$ 满足以下条件，则称 $Z$ 相对于有序变量对 $(X, Y)$ 满足**后门准则**：

1. $Z$ 中没有 $X$ 的后代，且
2. $Z$ 阻断 $X$ 与 $Y$ 之间所有含指向 $X$ 的箭头的路径。

条件 2 消除虚假关联；条件 1 保持因果路径不受影响（对位于某条有向路径上的 $X$ 的后代，即中介变量，取条件会阻断一部分效应），并防止产生新的虚假关联（对 $X$ 与 $Y$ 的共同后代，或这样的对撞因子的后代取条件，会打开一条路径）。$X$ 的父节点总是满足该准则：它们不是 $X$ 的后代，并且每条后门路径都以 $X \leftarrow P$ 开始，其中 $P$ 是父节点，在该路径上是链节点或叉节点。

**定理 12.3.1（后门调整）** 若一组观测变量 $Z$ 相对于 $(X, Y)$ 满足后门准则，则 $X$ 对 $Y$ 的因果效应是可识别的，且

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z).
\tag{12.3}
$$

**证明** 先处理实践中最常出现的情形，即单个离散的混杂因素：图为 $Z \to X$，$Z \to Y$，$X \to Y$（可能还有不是 $X$ 或 $Y$ 的祖先的其他变量）。此时 $\mathbb{P}(x, y, z) = \mathbb{P}(z)\,\mathbb{P}(x \mid z)\,\mathbb{P}(y \mid x, z)$，由截断分解，干预去掉因子 $\mathbb{P}(x \mid z)$：

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(y, z \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z)\,\mathbb{P}(y \mid x, z).
$$

对一般情形，用 $X$ 的一个额外父节点 $F$ 来表示干预：$F = \text{idle}$ 时保留 $X$ 的机制，$F = x$ 时设定 $X = x$，于是 $\mathbb{P}(\cdot \mid \operatorname{do}(x)) = \mathbb{P}(\cdot \mid F = x)$，$\mathbb{P}(\cdot) = \mathbb{P}(\cdot \mid F = \text{idle})$。在增广的图中：

- $Z \perp F$。从 $F$ 出发的每条路径都以 $F \to X$ 开始。若它继续为 $X \to \cdots$，则它要么是从 $X$ 出发的有向路径，不可能终止于 $Z$（$Z$ 的成员都不是 $X$ 的后代），要么含有对撞因子；该对撞因子及其后代都是 $X$ 的后代，所以没有一个在（空的）条件集中。若它继续为 $X \leftarrow \cdots$，则 $X$ 是对撞因子，而我们没有对 $X$ 或其任何后代取条件。
- $Y \perp F \mid (X, Z)$。路径 $F \to X \to \cdots\, Y$ 被条件集中的链节点 $X$ 阻断。路径 $F \to X \leftarrow \cdots\, Y$ 接着是从 $X$ 到 $Y$ 的一条后门路径；条件 2 说明 $Z$ 在 $G$ 中阻断它，而且不难检查，把 $X$ 加入条件集不会把它重新打开：其上作为 $X$ 的祖先的对撞因子，会通过该对撞因子的父节点产生另一条从 $X$ 到 $Y$ 的后门路径，$Z$ 也必须阻断它。

因此

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(y \mid x, z, F = x)\,\mathbb{P}(z \mid F = x) = \sum_z \mathbb{P}(y \mid x, z, F = \text{idle})\,\mathbb{P}(z \mid F = \text{idle}),
$$
即 (12.3)。$\square$

后门准则是无混杂性的图形形式：若 $Z$ 满足它，则给定 $Z$ 时 $X \perp \{Y_x\}$，用 Rubin 的记号就是 $W \perp (Y(0), Y(1)) \mid Z$。DAG 使这个假设可以对照所述的因果故事来检验，而在 Rubin 的框架中它是被直接假定的。当 $Z = \varnothing$ 时，该准则说的是 $X$ 没有后门路径，如在 $X$ 没有父节点的随机化实验中；此时 $\mathbb{P}(y \mid \operatorname{do}(x)) = \mathbb{P}(y \mid x)$。

### 12.3.2. 例子

![四个因果图。(a) 未测量的 $Z$（虚线箭头）使 $X$ 与 $Y$ 混杂，但被测量的 $W$ 阻断了后门路径。(b) 每个调整集都必须含有对撞因子 $Z$，以及 $E$ 或 $A$。(c) 前门情形：$U$ 未被测量，$Z$ 中介全部效应。(d) $X$ 对 $Y$ 的直接效应要求把 $Z$ 固定。](./plots/adjustment_dags.py)

**例 12.3.1（对代理变量的调整）** 在图 (a) 中，$X$ 是一种新药，$Y$ 是康复，$W$ 是患者的体重，$Z$ 是未测量的社会经济地位，它既影响谁得到药物，也影响患者的体重，而体重影响康复。唯一的后门路径是 $X \leftarrow Z \to W \to Y$，被测量的 $W$ 阻断了它；$W$ 不是 $X$ 的后代。所以 $W$ 满足后门准则，且

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_w \mathbb{P}(y \mid x, w)\,\mathbb{P}(w).
$$
我们不需要测量混杂因素本身，只需测量一个截断它对结果的影响的变量。

**例 12.3.2（对对撞因子的调整）** 在图 (b) 中，从 $X$ 到 $Y$ 的后门路径有 $X \leftarrow Z \to Y$、$X \leftarrow Z \leftarrow A \to Y$、$X \leftarrow E \to Z \to Y$ 与 $X \leftarrow E \to Z \leftarrow A \to Y$。第一条要求调整集中含有 $Z$。但 $Z$ 是最后一条路径上的对撞因子，对 $Z$ 取条件会打开这条路径；于是必须再用 $E$ 或 $A$ 把它重新阻断。满足该准则的集合为 $\{E, Z\}$、$\{A, Z\}$ 与 $\{E, Z, A\}$；单独的 $\{Z\}$ 不满足。有时我们不得不对对撞因子做调整，这时还必须对别的变量也做调整。

:::

由此得到两点教训。第一，对"所有处理前变量"做调整并不自动安全：在箭头为 $E \to X$、$E \to M$、$A \to M$、$A \to Y$ 与 $X \to Y$ 的图中（所谓 M 偏倚），空集就满足该准则，而只对处理前变量 $M$ 做调整会产生**对撞偏倚**。第二，当有多个集合满足该准则时，它们都给出同样的 $\mathbb{P}(y \mid \operatorname{do}(x))$。因此我们可以选择测量成本最低或给出最精确估计的集合；并且如果两个不同的调整集都被观测到，等式 $\sum_{z_1} \mathbb{P}(y \mid x, z_1)\,\mathbb{P}(z_1) = \sum_{z_2} \mathbb{P}(y \mid x, z_2)\,\mathbb{P}(z_2)$ 就是因果图的一个可检验的推论，很像 d-分离所蕴含的独立性。在图 (b) 中，对 $\{E, Z\}$ 与对 $\{A, Z\}$ 做调整必须给出相同的答案。

## 12.4. 前门准则

### 12.4.1. 吸烟、焦油与肺癌

当 $X$ 与 $Y$ 的混杂因素未被测量，且没有其他变量阻断后门路径时，后门准则失效。这正是 20 世纪 50、60 年代关于吸烟与肺癌的争论中的情形：R. A. Fisher 认为，某种基因型可能同时引起对尼古丁的渴求与癌症，而任何观察性研究都无法排除这一点。然而假设吸烟（$X$）只通过沉积在肺中的焦油（$Z$）影响癌症（$Y$），未测量的基因型 $U$ 不直接影响焦油，且混杂只作用于 $X$ 与 $Y$（图 (c)）。那么，连续两次应用后门准则就能识别该效应。

- *$X$ 对 $Z$ 的效应。* 从 $X$ 到 $Z$ 唯一的后门路径是 $X \leftarrow U \to Y \leftarrow Z$，它被对撞因子 $Y$ 阻断。因此 $\mathbb{P}(z \mid \operatorname{do}(x)) = \mathbb{P}(z \mid x)$。
- *$Z$ 对 $Y$ 的效应。* 后门路径 $Z \leftarrow X \leftarrow U \to Y$ 被不是 $Z$ 的后代的 $X$ 阻断。因此 $\mathbb{P}(y \mid \operatorname{do}(z)) = \sum_{x'} \mathbb{P}(y \mid x', z)\,\mathbb{P}(x')$。
- *链式组合。* 由于 $X$ 只通过 $Z$ 影响 $Y$，$\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z \mid \operatorname{do}(x))\,\mathbb{P}(y \mid \operatorname{do}(z))$。

### 12.4.2. 准则与公式

**定义 12.4.1（前门准则）** 若变量集 $Z$ 满足以下条件，则称 $Z$ 相对于有序变量对 $(X, Y)$ 满足**前门准则**：

1. $Z$ 截断从 $X$ 到 $Y$ 的所有有向路径；
2. 从 $X$ 到 $Z$ 没有未被阻断的后门路径；并且
3. 从 $Z$ 到 $Y$ 的所有后门路径都被 $X$ 阻断。

**定理 12.4.1（前门调整）** 若 $Z$ 相对于 $(X, Y)$ 满足前门准则，且 $\mathbb{P}(x, z) > 0$，则 $X$ 对 $Y$ 的因果效应是可识别的，且

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z \mid x) \sum_{x'} \mathbb{P}(y \mid x', z)\,\mathbb{P}(x').
\tag{12.4}
$$

**证明** 对图 (c) 证明：$U \to X$，$U \to Y$，$X \to Z$，$Z \to Y$，$U$ 未被观测。四个变量的联合分布分解为 $\mathbb{P}(u)\,\mathbb{P}(x \mid u)\,\mathbb{P}(z \mid x)\,\mathbb{P}(y \mid z, u)$，由截断分解得

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z \mid x) \sum_u \mathbb{P}(y \mid z, u)\,\mathbb{P}(u).
$$
还需要通过观测量来表示内层的和。写 $\mathbb{P}(u) = \sum_{x'} \mathbb{P}(u \mid x')\,\mathbb{P}(x')$。该图蕴含 $Y \perp X \mid (Z, U)$（从 $X$ 到 $Y$ 的两条路径分别经过 $Z$ 或叉节点 $U$）与 $U \perp Z \mid X$（路径 $U \to X \to Z$ 与 $U \to Y \leftarrow Z$ 分别被链节点 $X$ 与对撞因子 $Y$ 阻断）。因此 $\mathbb{P}(y \mid z, u) = \mathbb{P}(y \mid x', z, u)$，$\mathbb{P}(u \mid x') = \mathbb{P}(u \mid x', z)$，从而

$$
\sum_u \mathbb{P}(y \mid z, u)\,\mathbb{P}(u) = \sum_{x'} \mathbb{P}(x') \sum_u \mathbb{P}(y \mid x', z, u)\,\mathbb{P}(u \mid x', z) = \sum_{x'} \mathbb{P}(x')\,\mathbb{P}(y \mid x', z).
$$
代入即得 (12.4)。在一般的 DAG 中，定义 12.4.1 的三个条件给出同样的两个独立性（以后门路径上的变量代替 $U$），同样的计算适用；它也可以由 §12.5 的 do 演算的规则导出。$\square$

该公式有清楚的解读：$\mathbb{P}(z \mid x)$ 是吸烟对焦油的效应，内层的和是焦油对癌症的效应，并以总体权重 $\mathbb{P}(x')$ 对吸烟做了调整；在那里对 $X$ 做调整消除了基因型造成的混杂，因为基因型只通过吸烟到达焦油。

**例 12.4.1（假想的数据）** 假设一项研究涉及 800 000 人，吸烟者占一半，给出如下的组大小与癌症比率。

| 组 | $\mathbb{P}(x, z)$（占总体的百分比） | $\mathbb{P}(Y = 1 \mid x, z)$（患癌的百分比） |
|---|---|---|
| $X = 0$，$Z = 0$：不吸烟，无焦油 | 47.5 | 10 |
| $X = 1$，$Z = 0$：吸烟，无焦油 | 2.5 | 90 |
| $X = 0$，$Z = 1$：不吸烟，有焦油 | 2.5 | 5 |
| $X = 1$，$Z = 1$：吸烟，有焦油 | 47.5 | 85 |

于是 $\mathbb{P}(X = 1) = 0.5$，$\mathbb{P}(Z = 1 \mid X = 1) = 0.95$，$\mathbb{P}(Z = 1 \mid X = 0) = 0.05$。内层的和对 $z = 0$ 为 $0.10(0.5) + 0.90(0.5) = 0.50$，对 $z = 1$ 为 $0.05(0.5) + 0.85(0.5) = 0.45$，且

$$
\begin{aligned}
\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) &= 0.05(0.50) + 0.95(0.45) = 0.4525,\\
\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0)) &= 0.95(0.50) + 0.05(0.45) = 0.4975.
\end{aligned}
$$
虽然吸烟者的癌症比不吸烟者多得多（$0.8525$ 对 $0.0975$），但在前门模型下，吸烟会使癌症比率降低 $4.5$ 个百分点，因为在每个吸烟组内，焦油都与较少的癌症相关联。这些数字是为了说明公式可以反转朴素的比较而编造的，与真实的吸烟无关。该例也说明这些假设有多强：吸烟只通过焦油起作用、焦油与癌症没有未测量的共同原因，都是关于生物学而不是关于数据的断言。

:::

## 12.5. do 演算

### 12.5.1. 超越后门与前门

**定义 12.5.1（受控直接效应）** 在中介变量 $Z$ 固定为 $z$ 时，把 $X$ 由 $x'$ 变为 $x$ 对 $Y$ 的**受控直接效应**为

$$
\mathrm{CDE}(z) = \mathbb{P}(Y = y \mid \operatorname{do}(X = x), \operatorname{do}(Z = z)) - \mathbb{P}(Y = y \mid \operatorname{do}(X = x'), \operatorname{do}(Z = z)),
$$
或相应的期望之差。

**例 12.5.1（性别与招聘）** 雇主是否存在性别歧视？在图 (d) 中，性别 $X$ 直接影响招聘结果 $Y$，也通过资质 $Z$ 影响它，而申请人的家庭收入 $I$ 同时影响资质与招聘结果。性别的总效应包含通过资质的正当途径；歧视是直接效应，即资质相同的申请人之间性别的效应。对 $Z$ 取条件得不到它：$Z$ 是 $X \to Z \leftarrow I \to Y$ 上的对撞因子，所以比较资质相同的男性与女性会通过收入打开一条虚假路径。后门准则与前门准则都不适用于对 $X$ 与 $Z$ 的联合干预；需要一个一般的工具。

:::

### 12.5.2. 三条规则

对 DAG $G$ 与节点集 $X$，令 $G_{\overline{X}}$ 为删去所有指向 $X$ 中节点的箭头所得的图，$G_{\underline{X}}$ 为删去所有从 $X$ 中节点发出的箭头所得的图；$G_{\overline{X}\underline{Z}}$ 则两种箭头都删去。记 $\hat x$ 为 $\operatorname{do}(X = x)$。

**定理 12.5.1（do 演算）** 设 $G$ 是因果图，$X$、$Y$、$Z$、$W$ 是互不相交的变量集。对每个与 $G$ 相容的分布：

1. *观测的插入或删除：* 若 $(Y \perp Z \mid X, W)_{G_{\overline{X}}}$，则 $\mathbb{P}(y \mid \hat x, z, w) = \mathbb{P}(y \mid \hat x, w)$。
2. *行动与观测的交换：* 若 $(Y \perp Z \mid X, W)_{G_{\overline{X}\underline{Z}}}$，则 $\mathbb{P}(y \mid \hat x, \hat z, w) = \mathbb{P}(y \mid \hat x, z, w)$。
3. *行动的插入或删除：* 若 $(Y \perp Z \mid X, W)_{G_{\overline{X}\,\overline{Z(W)}}}$，则 $\mathbb{P}(y \mid \hat x, \hat z, w) = \mathbb{P}(y \mid \hat x, w)$，其中 $Z(W)$ 是 $Z$ 中在 $G_{\overline{X}}$ 里不是任何 $W$ 中节点的祖先的那些节点。

这些规则归功于 Pearl（1995），由截断分解与对被操纵的图应用定理 11.3.1 得出。每条规则都有简单的含义。

- 规则 1 是对 $X$ 干预之后的世界中的 d-分离：一旦指向 $X$ 的箭头被切断，给定 $X$ 与 $W$ 时与 $Y$ d-分离的观测 $Z$ 就可以忽略。
- 规则 2 说明何时观测 $Z = z$ 与设定它一样好：当 $X$ 与 $W$ 阻断从 $Z$ 到 $Y$ 的所有后门路径时，这些路径正是 $G_{\overline{X}\underline{Z}}$ 中 $Z$ 与 $Y$ 之间留下的路径。它是规则形式的后门准则。
- 规则 3 说明何时一个行动没有效应：当切断指向 $Z$ 的箭头之后，从 $Z$ 到 $Y$ 没有有向路径留下（对作为被观测的 $W$ 节点的祖先的 $Z$ 节点要做修正，即 $Z(W)$，因为对它们的后代取条件会重新引入它们的影响）。

当一系列规则的应用连同普通的概率演算把一个干预量变换为不含帽子的表达式时，该干预量就被识别了。

**例 12.5.2（性别与招聘，续）** 在图 (d) 中，

$$
\begin{aligned}
\mathbb{P}(y \mid \hat x, \hat z)
&= \mathbb{P}(y \mid x, \hat z) && \text{规则 2：} (Y \perp X \mid Z)_{G_{\overline{Z}\underline{X}}}\\
&= \sum_i \mathbb{P}(y \mid x, \hat z, i)\,\mathbb{P}(i \mid x, \hat z) && \text{全概率公式}\\
&= \sum_i \mathbb{P}(y \mid x, z, i)\,\mathbb{P}(i \mid x, \hat z) && \text{规则 2：} (Y \perp Z \mid X, I)_{G_{\underline{Z}}}\\
&= \sum_i \mathbb{P}(y \mid x, z, i)\,\mathbb{P}(i \mid x) && \text{规则 3：} (I \perp Z \mid X)_{G_{\overline{Z}}}\\
&= \sum_i \mathbb{P}(y \mid x, z, i)\,\mathbb{P}(i) && \text{规则 1：} (I \perp X)_G.
\end{aligned}
$$
每个条件都可以在图上检验。在 $G_{\overline{Z}\underline{X}}$ 中，$X$ 发出的两条箭头与箭头 $I \to Z$ 都被删去，所以 $X$ 是孤立的。在 $G_{\underline{Z}}$ 中，从 $Z$ 到 $Y$ 的路径为 $Z \leftarrow X \to Y$ 与 $Z \leftarrow I \to Y$，分别被 $X$ 与 $I$ 阻断。在 $G_{\overline{Z}}$ 中（这里 $Z(W) = Z$，因为 $Z$ 不是 $X$ 的祖先），$I$ 与 $Z$ 之间唯一的路径是 $I \to Y \leftarrow Z$，被未取条件的对撞因子 $Y$ 阻断。在 $G$ 中，从 $I$ 到 $X$ 的路径都经过一个对撞因子（$Z$ 或 $Y$），所以由图得 $I \perp X$。因此

$$
\mathrm{CDE}(z) = \sum_i \bigl[\mathbb{P}(y \mid x, z, i) - \mathbb{P}(y \mid x', z, i)\bigr]\mathbb{P}(i)：
$$
比较资质相同、家庭收入相同的男性与女性，再对收入取平均。收入必须被测量；只有资质是不够的。

:::

### 12.5.3. 完备性与进一步的应用

这三条规则是完备的：若干预分布 $\mathbb{P}(y \mid \operatorname{do}(x))$ 可由带有潜变量的因果图识别，则它可以通过有限的规则应用序列化为观察表达式；若不存在这样的序列，则该效应不可识别（Shpitser 与 Pearl 2006；Huang 与 Valtorta 2006）。寻找这个序列并不靠反复试探。Tian 与 Pearl（2002）用所谓的 c-分量（由潜在混杂连接起来的变量集）给出了可识别效应的图形刻画，Shpitser 与 Pearl（2006）以及 Huang 与 Valtorta（2006）把它发展为 ID 算法，它对任何因果图与任何干预分布判断其是否可识别，若可识别则返回公式；do 演算的完备性就是通过这个算法证明的。在最简单的不可识别情形，即 $X \to Y$ 且 $X$ 与 $Y$ 有未观测的共同原因而别无其他时，算法报告失败，这是应当的：例 11.4.2 已给出观察分布相同而效应不同的模型。

除了单个效应，同样的机制还可以处理其他问题：中介分析，把效应分解为直接与间接的部分（[3.9.15](/3.9.15)）；可迁移性，即在一个总体中估计的效应能否搬到因果图以已知方式不同的另一个总体；以及多项实验与观察研究的结合（数据融合、元综合）。软件实现了这些准则：在 R 中，包 `pcalg` 有寻找调整集的函数 `backdoor`，包 `causaleffect` 实现了 ID 算法。

## 小结

- 平均因果效应由干预定义，$\mathbb{E}[Y \mid \operatorname{do}(x_1)] - \mathbb{E}[Y \mid \operatorname{do}(x_2)]$（定义 12.1.1）；若能用观察分布与图把它表示出来，它就是可识别的。
- 调整：对满足后门准则的集合 $Z$（不含 $X$ 的后代；阻断所有指向 $X$ 的路径；定义 12.3.2），

  $$
  \mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z) = \sum_z \frac{\mathbb{P}(x, y, z)}{\mathbb{P}(x \mid z)}
  $$
  （定理 12.2.1、12.3.1；式 (12.2)）。第一种形式是分层，第二种是以倾向评分做逆概率加权；后门准则是无混杂性的图形形式。Simpson 悖论由因果图而不是由数据来化解（例 12.2.1、12.2.2）。
- 协变量的选择：为阻断后门路径而调整，决不对 $X$ 的后代调整；对撞因子可能必须与一个把被打开的路径重新阻断的变量一起调整（例 12.3.2）；所有有效的集合给出同样的答案。
- 前门：若 $Z$ 截断从 $X$ 到 $Y$ 的所有有向路径，从 $X$ 到它没有未被阻断的后门路径，且 $X$ 阻断它到 $Y$ 的后门路径（定义 12.4.1），则即使 $X$ 与 $Y$ 存在未测量的混杂因素，$\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z \mid x)\sum_{x'}\mathbb{P}(y \mid x', z)\,\mathbb{P}(x')$（定理 12.4.1）。
- do 演算：三条规则（插入或删除观测；交换行动与观测；插入或删除行动），用被切断的图中的 d-分离来检验（定理 12.5.1）。它们可以识别例如受控直接效应 $\sum_i[\mathbb{P}(y \mid x, z, i) - \mathbb{P}(y \mid x', z, i)]\mathbb{P}(i)$（例 12.5.2），并且是完备的；ID 算法判定可识别性并系统地给出公式。

| 工具 | 图形条件 | 公式 |
|---|---|---|
| 对父节点调整 | 总是有效 | $\sum_{\mathrm{pa}} \mathbb{P}(y \mid x, \mathrm{pa})\,\mathbb{P}(\mathrm{pa})$ |
| 后门 | $Z$ 是 $X$ 的非后代，阻断所有后门路径 | $\sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z)$ |
| 前门 | $Z$ 中介全部效应，$X$–$Z$ 无混杂，$X$ 阻断 $Z$–$Y$ | $\sum_z \mathbb{P}(z \mid x)\sum_{x'}\mathbb{P}(y \mid x', z)\,\mathbb{P}(x')$ |
| do 演算 | 三条规则 | 任何可识别的效应 |

## 思考题

1. 在图 $Z \to X$，$Z \to Y$，$X \to Y$ 中，变量均为二值，一项 200 名患者的研究给出如下计数。

   | | $Z = 0$，$X = 0$ | $Z = 0$，$X = 1$ | $Z = 1$，$X = 0$ | $Z = 1$，$X = 1$ |
   |---|---|---|---|---|
   | $Y = 1$ | 30 | 15 | 5 | 40 |
   | $Y = 0$ | 50 | 5 | 15 | 40 |

   计算朴素的差 $\mathbb{P}(Y = 1 \mid X = 1) - \mathbb{P}(Y = 1 \mid X = 0)$ 与平均因果效应。

   **答** 朴素的：$\mathbb{P}(Y = 1 \mid X = 1) = (15 + 40)/100 = 0.55$，$\mathbb{P}(Y = 1 \mid X = 0) = (30 + 5)/100 = 0.35$，差为 $0.20$。取 $\mathbb{P}(Z = 1) = 100/200 = 0.5$，层内比率为 $0.75$、$0.375$（$Z = 0$）与 $0.5$、$0.25$（$Z = 1$）：$\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) = 0.5(0.75) + 0.5(0.5) = 0.625$，$\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0)) = 0.5(0.375) + 0.5(0.25) = 0.3125$，所以 $\mathrm{ACE} = 0.3125$。朴素的比较低估了效应，因为 $Z = 1$ 使接受处理更可能而使康复更不可能。
2. 一部分比例为 $r$ 的患者有某综合征（$Z = 1$）。没有该综合征的患者以概率 $q_1$ 服药（$X = 1$），有该综合征的以概率 $q_2$ 服药。死亡（$Y = 1$）的概率为 $p_1$（$Z = 0$，$X = 0$）、$p_2$（$Z = 0$，$X = 1$）、$p_3$（$Z = 1$，$X = 0$）、$p_4$（$Z = 1$，$X = 1$）。因果图为 $Z \to X$，$Z \to Y$，$X \to Y$。求 $\mathbb{P}(Y = 1 \mid X = 1) - \mathbb{P}(Y = 1 \mid X = 0)$ 与平均因果效应，并叙述和证明所用的准则。

   **答** $\mathbb{P}(x, y, z) = \mathbb{P}(z)\,\mathbb{P}(x \mid z)\,\mathbb{P}(y \mid x, z)$，例如 $\mathbb{P}(X = 1, Y = 1, Z = 1) = r q_2 p_4$。于是
   $$
   \mathbb{P}(Y = 1 \mid X = 1) = \frac{(1 - r) q_1 p_2 + r q_2 p_4}{(1 - r) q_1 + r q_2}, \qquad
   \mathbb{P}(Y = 1 \mid X = 0) = \frac{(1 - r)(1 - q_1) p_1 + r(1 - q_2) p_3}{(1 - r)(1 - q_1) + r(1 - q_2)}.
   $$
   $Z$ 是 $X$ 的父节点，所以满足后门准则，$\mathrm{ACE} = [(1 - r)p_2 + r p_4] - [(1 - r)p_1 + r p_3]$。该准则及其对这个图的证明就是定理 12.3.1 证明的第一部分：截断分解去掉因子 $\mathbb{P}(x \mid z)$，得 $\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z)\,\mathbb{P}(y \mid x, z)$。
3. 在图 (b) 中，列出从 $X$ 到 $Y$ 的所有后门路径，并验证 $\{E\}$、$\{A\}$ 与 $\{Z\}$ 不满足后门准则，而 $\{A, Z\}$ 满足。

   **答** 这些路径为 $X \leftarrow Z \to Y$、$X \leftarrow Z \leftarrow A \to Y$、$X \leftarrow E \to Z \to Y$ 与 $X \leftarrow E \to Z \leftarrow A \to Y$。$\{E\}$ 与 $\{A\}$ 使 $X \leftarrow Z \to Y$ 保持开放。$\{Z\}$ 阻断前三条（$Z$ 是叉节点或链节点），但打开第四条（其上 $Z$ 是对撞因子）。$\{A, Z\}$ 通过 $Z$ 阻断前三条，通过叉节点 $A$ 阻断第四条；二者都不是 $X$ 的后代。
4. 对前门图，设数据为：$\mathbb{P}(X = 1) = 0.5$；在 $X = 0$ 中，60% 有 $Z = 0$，癌症比率为 $0.2$，40% 有 $Z = 1$，比率为 $0.5$；在 $X = 1$ 中，20% 有 $Z = 0$，比率为 $0.3$，80% 有 $Z = 1$，比率为 $0.6$。用前门公式计算 ACE，并与朴素的差比较。

   **答** 内层的和：$z = 0$：$0.5(0.2) + 0.5(0.3) = 0.25$；$z = 1$：$0.5(0.5) + 0.5(0.6) = 0.55$。于是 $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) = 0.2(0.25) + 0.8(0.55) = 0.49$，$\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0)) = 0.6(0.25) + 0.4(0.55) = 0.37$，所以 $\mathrm{ACE} = 0.12$。朴素地，$\mathbb{P}(Y = 1 \mid X = 1) = 0.2(0.3) + 0.8(0.6) = 0.54$，$\mathbb{P}(Y = 1 \mid X = 0) = 0.6(0.2) + 0.4(0.5) = 0.32$，差为 $0.22$；观察到的关联有一部分是由未测量的混杂因素造成的。
5. 对图 (c)，从 $\mathbb{P}(y \mid \hat x) = \sum_z \mathbb{P}(y \mid \hat x, z)\,\mathbb{P}(z \mid \hat x)$ 出发，用 do 演算推导前门公式。

   **答** (i) 由规则 2，$\mathbb{P}(z \mid \hat x) = \mathbb{P}(z \mid x)$，因为 $(Z \perp X)_{G_{\underline{X}}}$（剩下的路径 $X \leftarrow U \to Y \leftarrow Z$ 含有对撞因子 $Y$）。(ii) 由规则 2，$\mathbb{P}(y \mid \hat x, z) = \mathbb{P}(y \mid \hat x, \hat z)$，因为 $(Y \perp Z \mid X)_{G_{\overline{X}\underline{Z}}}$。(iii) 由规则 3，$\mathbb{P}(y \mid \hat x, \hat z) = \mathbb{P}(y \mid \hat z)$，因为在 $G_{\overline{Z}\,\overline{X}}$ 中箭头 $U \to X$ 与 $X \to Z$ 被删去，$X$ 是孤立的，$(Y \perp X \mid Z)$ 成立。(iv) $\mathbb{P}(y \mid \hat z) = \sum_{x'} \mathbb{P}(y \mid x', \hat z)\,\mathbb{P}(x' \mid \hat z) = \sum_{x'} \mathbb{P}(y \mid x', z)\,\mathbb{P}(x')$，用到规则 2（$(Y \perp Z \mid X)_{G_{\underline{Z}}}$）与规则 3（$(X \perp Z)_{G_{\overline{Z}}}$）。合起来得 (12.4)。
6. 在两个时间点给予处理：第一次就诊时的 $X$，第二次的 $U$。两次就诊之间测量一个危险因素 $Z$；$Z$ 受 $X$ 与未测量的健康状况 $H$ 的影响，$H$ 也影响结果 $Y$；第二次处理 $U$ 依据 $Z$ 选择；$X$、$Z$、$U$ 都影响 $Y$。$X$ 是随机化的。$\mathbb{P}(y \mid \operatorname{do}(x), \operatorname{do}(u))$ 可识别吗？为什么按通常方式对 $Z$ 做调整会失败？

   **答** 箭头为 $X \to Z$、$H \to Z$、$H \to Y$、$Z \to U$，以及 $X, Z, U \to Y$。它是可识别的：
   $$
   \mathbb{P}(y \mid \hat x, \hat u) = \sum_z \mathbb{P}(y \mid x, z, u)\,\mathbb{P}(z \mid x),
   $$
   这就是 Robins（1986）的 g 公式。推导：$\mathbb{P}(y \mid \hat x, \hat u) = \sum_z \mathbb{P}(y \mid \hat x, \hat u, z)\,\mathbb{P}(z \mid \hat x, \hat u)$；由规则 3（$U$ 不是 $Z$ 的祖先），$\mathbb{P}(z \mid \hat x, \hat u) = \mathbb{P}(z \mid \hat x)$，再由规则 2（$X$ 没有父节点），它等于 $\mathbb{P}(z \mid x)$；由规则 2（在 $G_{\overline{X}\underline{U}}$ 中，从 $U$ 到 $Y$ 的路径都以 $Z$ 为链节点或叉节点经过），$\mathbb{P}(y \mid \hat x, \hat u, z) = \mathbb{P}(y \mid \hat x, u, z)$，再由规则 2（在 $G_{\underline{X}}$ 中 $X$ 是孤立的），它等于 $\mathbb{P}(y \mid x, u, z)$。朴素的公式 $\sum_z \mathbb{P}(y \mid x, z, u)\,\mathbb{P}(z)$ 是错的：$Z$ 是 $X$ 的后代（位于路径 $X \to Z \to Y$ 上），又是 $X \to Z \leftarrow H \to Y$ 上的对撞因子，所以必须以 $\mathbb{P}(z \mid x)$（它在第一次处理下的分布）加权，而不能固定在它的边缘分布上。
7. 用本章的语言解释，为什么在随机化实验中不应对处理之后测量的变量做调整。

   **答** 处理后变量 $M$ 是 $X$ 的后代，所以违反后门准则的条件 1。若 $M$ 位于有向路径 $X \to M \to Y$ 上，对它做调整会阻断我们想要的一部分效应（我们估计的是类似直接效应的东西，而且若 $M$ 与 $Y$ 有共同原因，连这个也是错的）。若 $M$ 是 $X$ 与 $Y$ 的某个原因的共同结果，$X \to M \leftarrow V \to Y$，对它取条件会打开一条虚假路径。在随机化实验中 $X$ 根本没有后门路径，所以空集已经满足该准则，$\mathbb{P}(y \mid \operatorname{do}(x)) = \mathbb{P}(y \mid x)$。
8. 在图 $X \to Y$ 中，有未观测的 $U$ 使得 $U \to X$ 且 $U \to Y$，用例子说明 $\mathbb{P}(y \mid \operatorname{do}(x))$ 不由 $\mathbb{P}(x, y)$ 决定。

   **答** 取二值变量。模型 A：没有 $U$，$X \sim \mathrm{Ber}(1/2)$，$Y = X$。模型 B：$U \sim \mathrm{Ber}(1/2)$，$X = U$，$Y = U$（$X$ 没有效应）。两者都给出 $\mathbb{P}(X = Y = 0) = \mathbb{P}(X = Y = 1) = 1/2$，但 $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1))$ 在模型 A 中为 $1$，在模型 B 中为 $1/2$。两个模型都与该图相容，所以该效应不可识别。
