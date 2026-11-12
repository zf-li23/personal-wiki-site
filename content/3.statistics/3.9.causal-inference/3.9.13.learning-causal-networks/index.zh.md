---
title: 学习因果 Bayes 网络
description: 结构已知的 Bayes 网络的参数学习（似然的分解、条件概率表的极大似然估计与 Dirichlet 后验、bnlearn）；结构学习能够识别什么（Markov 等价类与 CPDAG）；搜索评分法（似然、AIC 与 BIC 得分、爬山法）；约束法（IC 与 PC 算法、Meek 规则、五变量的完整例子、条件独立性的 G 平方检验与 Fisher z 检验）；Gauss 图模型、有向图与无向图的表达能力，以及进阶与前沿的方法。
source_hash: 6a345d1509db
---

[3.9.12](/3.9.12) 的方法把因果图当作已知。当因果图来自成熟的科学知识时，例如流行病学研究中变量的时间顺序与生物学顺序已被充分理解，这样做是合理的。在许多其他问题中，例如数千个基因之间的调控关系或众多经济指标之间的依赖关系，图是未知的，必须从数据中学习。本章讨论学习 Bayes 网络的两个部分：结构已知时估计参数，这是标准的似然问题；以及估计结构本身，即结构学习（structure learning），它困难得多，也只能部分做到。在 [3.9.11](/3.9.11) 的假设（Markov 相容与忠实性）之下，观测分布至多只能确定图所在的 Markov 等价类，因此结构学习的输出一般是一个部分有向图。这些算法在 R 包 `bnlearn` 中实现，本章始终使用它（MATLAB 中的 Bayes Net Toolbox 提供类似的函数）。[7.9.11](/7.9.11) 把同样的思想用于基因调控网络。

## 13.1. 参数学习

### 13.1.1. 似然可以分解

设 DAG $G$ 已知，观测到 $M$ 个独立的案例 $\boldsymbol{x}^{(1)}, \dots, \boldsymbol{x}^{(M)}$，每个节点都被观测到；记数据为 $D$，节点 $X_i$ 的父节点为 $\pi_i$，其条件分布（CPD）$\mathbb{P}(x_i \mid \pi_i, \boldsymbol{\phi}_i)$ 的参数为 $\boldsymbol{\phi}_i$。与任何统计模型一样，有两种做法。

- *Bayes 方法*：把 $\boldsymbol{\phi}$ 看作随机的，计算其后验分布 $p(\boldsymbol{\phi} \mid D)$。
- *频率学派方法*：把 $\boldsymbol{\phi}$ 看作未知常数并加以估计，例如用**极大似然估计**或惩罚似然，$\boldsymbol{\phi}^* = \arg\max_{\boldsymbol{\phi}} \{\log \mathbb{P}(D \mid \boldsymbol{\phi}) - \lambda C(\boldsymbol{\phi})\}$，其中 $C$ 度量复杂度。

由分解式 (11.2)，对数似然为

$$
\ell(\boldsymbol{\phi}) = \sum_{m=1}^M \log \mathbb{P}(\boldsymbol{x}^{(m)} \mid \boldsymbol{\phi}) = \sum_{i=1}^n \underbrace{\sum_{m=1}^M \log \mathbb{P}\bigl(x_i^{(m)} \mid \pi_i^{(m)}, \boldsymbol{\phi}_i\bigr)}_{\ell_i(\boldsymbol{\phi}_i)}.
\tag{13.1}
$$
如果不同 CPD 的参数在变分意义下相互独立（全局参数独立性），对数似然就是若干项之和，每一项只涉及一个节点及其父节点，可以逐个节点地最大化：估计一个 Bayes 网络化为 $n$ 个相互独立的回归，每个回归把一个节点对其父节点做回归。若先验对各节点也分解，则后验同样如此。

### 13.1.2. 条件概率表

对离散变量，节点 $i$ 的 CPD 是一张表：设 $X_i$ 取值 $k = 1, \dots, r_i$，$j = 1, \dots, q_i$ 为其父节点各种取值组合的编号，并记 $\theta_{ijk} = \mathbb{P}(X_i = k \mid \pi_i = j)$，满足 $\sum_k \theta_{ijk} = 1$。充分统计量是各家庭构型（节点及其父节点的取值组合）的计数 $N_{ijk} = \#\{m : x_i^{(m)} = k, \pi_i^{(m)} = j\}$，而

$$
\ell(\boldsymbol{\theta}) = \sum_{i=1}^n \sum_{j=1}^{q_i} \sum_{k=1}^{r_i} N_{ijk} \log \theta_{ijk}.
$$

**定理 13.1.1（多项 CPD 的极大似然）** 数据完整时，条件概率表的极大似然估计就是观测到的条件频率表，

$$
\hat\theta_{ijk} = \frac{N_{ijk}}{N_{ij}}, \qquad N_{ij} = \sum_{k=1}^{r_i} N_{ijk}.
$$

**证明** 对数似然按 $(i, j)$ 分开，每一部分 $\sum_k N_{ijk}\log\theta_{ijk}$ 都是一个**多项分布**的对数似然。对约束 $\sum_k \theta_{ijk} = 1$ 引入 **Lagrange 乘子**，令 $\sum_k N_{ijk}\log\theta_{ijk} - \lambda(\sum_k \theta_{ijk} - 1)$ 的导数为零：$N_{ijk}/\theta_{ijk} = \lambda$，于是 $\theta_{ijk} = N_{ijk}/\lambda$，由约束得 $\lambda = N_{ij}$。该函数关于 $\boldsymbol{\theta}$ 是凹的，所以这就是最大值点。$\square$

若对每张表的每一行取 **Dirichlet 分布** $\mathrm{Dir}(\alpha_{ij1}, \dots, \alpha_{ijr_i})$ 作先验，各行之间独立，则由 [3.7.3](/3.7.3) 的 Dirichlet–多项分布共轭性，后验为 $\mathrm{Dir}(\alpha_{ij1} + N_{ij1}, \dots, \alpha_{ijr_i} + N_{ijr_i})$，后验均值为 $(N_{ijk} + \alpha_{ijk})/(N_{ij} + \alpha_{ij})$，其中 $\alpha_{ij} = \sum_k \alpha_{ijk}$。先验计数平滑了观测很少的行的估计，这很重要，因为父节点取值组合的个数 $q_i$ 随父节点数指数增长。

**例 13.1.1（`bnlearn` 中的洒水器网络）** 结构通过列出各条弧来设定，`bn.fit` 由数据框 `data`（五个变量均为因子）估计各张表。DAG 必须是完全有向的；实际中它常常来自一个结构学习步骤。

```r
library(bnlearn)
dag <- empty.graph(nodes = c("Season", "Sprinkler", "Rain", "Wet", "Slippery"))
arc.set <- matrix(c("Season", "Sprinkler",
                    "Season", "Rain",
                    "Sprinkler", "Wet",
                    "Rain", "Wet",
                    "Wet", "Slippery"),
                  byrow = TRUE, ncol = 2,
                  dimnames = list(NULL, c("from", "to")))
arcs(dag) <- arc.set
plot(dag)
fitted <- bn.fit(dag, data, method = "mle")
fitted$Wet   # the table P(Wet | Sprinkler, Rain)
```

`method = "bayes"` 把极大似然估计换成取定想象样本量的均匀 Dirichlet 先验下的后验均值。

:::

## 13.2. 结构学习能够识别什么

学习结构是在 DAG 上做模型选择，它比参数学习困难，原因有二。其一，空间巨大：$n$ 个带标号节点上的 DAG 个数在 $n = 1, \dots, 5$ 时依次为 $1, 3, 25, 543, 29281$，并且超指数增长；寻找得分最高的 DAG 是 **NP 难**的（Chickering 1996）。其二，目标只能部分识别。由定理 11.3.2，两个 DAG Markov 等价当且仅当它们有相同的骨架和相同的 v-结构；$X \to Y \to Z$、$X \leftarrow Y \leftarrow Z$ 与 $X \leftarrow Y \to Z$ 编码相同的独立性，无法用观测数据区分。相反，v-结构 $X \to Y \leftarrow Z$ 有独一无二的统计特征（$X \perp Z$，但给定 $Y$ 时不独立），因此部分箭头的方向可以从被动观测中推断出来。

**定义 13.2.1（部分有向无环图）** **部分有向无环图**（PDAG）是既有有向边又有无向边、且没有有向圈的图。一个 Markov 等价类的**完备部分有向无环图**（CPDAG，也称本质图）具有该类共同的骨架；若类中所有 DAG 都含有 $a \to b$，则它有有向边 $a \to b$（强制边）；若类中有的 DAG 含有 $a \to b$、有的含有 $b \to a$，则它有无向边 $a - b$。

把 CPDAG 的无向边定向，只要不产生新的 v-结构，也不产生有向圈，得到的每个 DAG 都属于该类。因此在 Markov 相容与忠实性之下，CPDAG 是观测数据所能揭示的全部。要区分等价类中的成员，需要干预或实验（设定 $Y$ 并观察 $X$ 是否改变，可以区分 $X \to Y$ 与 $Y \to X$），或者需要背景知识，例如时间顺序。算法有三大类。

| 类别 | 思路 | 例 |
|---|---|---|
| 搜索评分法 | 定义模型好坏的得分，搜索使它最大的图 | 爬山法 |
| 约束法 | 检验条件独立性，构造与检验结果一致的图 | IC、PC |
| 混合法 | 先用检验限制搜索空间，再搜索评分 | MMHC（Tsamardinos 等 2006） |

## 13.3. 搜索评分法

### 13.3.1. 得分

**定义 13.3.1（搜索评分法）** 结构学习的**搜索评分法**定义一个评分函数 $S(G; D)$，度量 DAG $G$ 对数据 $D$ 的拟合程度，并用搜索算法寻找（局部）得分最大的图。

Bayes 版本把图看作随机的，计算 $\mathbb{P}(G \mid D) \propto \mathbb{P}(D \mid G)\,\mathbb{P}(G)$，其中边缘似然 $\mathbb{P}(D \mid G) = \int \mathbb{P}(D \mid \boldsymbol{\phi}, G)\,p(\boldsymbol{\phi} \mid G)\,\mathrm{d}\boldsymbol{\phi}$ 对 Dirichlet 先验有闭式（BDe 得分）。频率学派版本最大化惩罚似然，

$$
G^* = \arg\max_G \bigl\{\log \mathbb{P}(D \mid \hat{\boldsymbol{\phi}}_G, G) - \lambda\,C(G)\bigr\},
$$
其中 $C(G)$ 是自由参数的个数。单独的极大化对数似然（$\lambda = 0$）是很差的得分：添加一条弧绝不会使它减小，因为含这条弧的模型包含不含它的模型，所以它总是偏向近乎完全的图。**赤池信息准则**与**贝叶斯信息准则**（在 [3.4.11](/3.4.11) 中定义，并在 [3.7.8](/3.7.8) 中比较）的惩罚项

$$
\mathrm{AIC} = -2\log \mathbb{P}(D \mid \hat{\boldsymbol{\phi}}) + 2k, \qquad \mathrm{BIC} = -2\log \mathbb{P}(D \mid \hat{\boldsymbol{\phi}}) + k\log M,
$$
修正了这一点（$k$ 是自由参数的个数，$M$ 是样本量；越小越好，`bnlearn` 报告的是 $-\mathrm{BIC}/2$，所以越大越好）。两者回答的问题不同：BIC 在忽略低阶项的意义下近似 $-2\log \mathbb{P}(D \mid G)$，先验正是在这里被舍去的，并且当候选图中有一个是真图时，用它选择真图是相合的；AIC 与交叉验证类似，目标是预测最好的模型，倾向于保留多余的弧。两者都是可分解的，即如 (13.1) 那样是每个节点及其父节点各项之和，所以图的局部改动只改变一两项；两者也都是得分等价的，对 Markov 等价的 DAG 给出相同的值。

### 13.3.2. 爬山法

搜索通常是贪心的。**爬山法**（[4.5.2](/4.5.2)）从一个初始图（通常是空图）出发，只要结果仍无圈，就反复施行使得分提高最多的单步操作（添加、删除或反转一条弧），直到没有操作能再提高得分。由于得分是可分解的，评估每个候选操作只需重新计算一两个局部项。

```r
res <- hc(data, score = "loglik")   # log-likelihood: tends to a dense graph
res <- hc(data, score = "bic")      # also "aic"
plot(res)
data2 <- data[, c(2, 1, 3, 4, 5)]   # permute the columns
plot(hc(data2, score = "bic"))
```

爬山法返回的是单个 DAG 而不是等价类，其弧在类内的方向是任意的，取决于同样好的操作被尝试的先后。因此置换数据的列可能改变输出；在洒水器网络的样本上，甚至可能使搜索停在带有伪弧、并在季节节点处出现错误 v-结构的局部最优。基于约束的 `pc.stable`（13.4 节）无论列的顺序如何，都返回同一个 CPDAG。随机重启与禁忌表（`bnlearn` 中的 `tabu`）可以降低陷入较差局部最优的风险。

| | 搜索评分法 |
|---|---|
| 优点 | 容易纳入先验知识（先验 $\mathbb{P}(G)$、必须或禁止的弧）；直接返回等价类中的一个完全有向 DAG；每次比较都用到全部数据 |
| 缺点 | 通常停在局部最优；变量数多、搜索空间大时计算代价高 |

## 13.4. 约束法

### 13.4.1. 从独立性到图

**定义 13.4.1（约束法）** 结构学习的**约束法**在数据中检验条件独立性 $X_i \perp X_j \mid S$，并构造与检验结果一致的图（一个等价类）。

它有两个部分：条件独立性检验把数据与概率联系起来，算法把概率与图联系起来，前提是所有条件独立性都被检验正确地揭示出来。在 Markov 相容与忠实性之下，$I(G) = I(\mathbb{P})$，算法依据两个事实：两个节点相邻当且仅当没有任何集合能 d-分离它们；若 $a$、$b$ 不相邻但有公共邻点 $c$，则 $a \to c \leftarrow b$ 是 v-结构当且仅当 $c$ 不在任何（等价地，不在已找到的）分离 $a$ 与 $b$ 的集合中。

**算法 13.4.1（IC 算法）** **IC 算法**（inductive causation；Verma 与 Pearl 1990）的输入是 $n$ 个变量的一个分布，或由数据估计出的条件独立性。

1. *骨架。* 对每一对 $(a, b)$，寻找集合 $S_{ab}$ 使 $a \perp b \mid S_{ab}$。当且仅当找不到这样的集合时，连接 $a - b$。
2. *v-结构。* 对每一对有公共邻点 $c$ 的不相邻节点 $a$、$b$，若 $c \notin S_{ab}$，则定向 $a \to c \leftarrow b$。
3. *传播。* 反复应用 Meek 规则，在不产生新 v-结构和有向圈的前提下，尽可能多地为其余无向边定向。

输出是真 DAG 所在等价类的 CPDAG。第 1 步对 $n(n - 1)/2$ 对节点中的每一对，可能要检查其余变量的全部 $2^{n-2}$ 个子集，所以最坏情形的复杂度为 $O(n^2 2^{n-2})$。

**定义 13.4.2（Meek 规则）** 在含有全部 v-结构的 PDAG 中，**Meek 规则**按如下方式为无向边 $b - c$ 定向：

1. 若 $a \to b - c$ 且 $a$、$c$ 不相邻，则定向 $b \to c$（否则 $a \to b \leftarrow c$ 会成为新的 v-结构）；
2. 若 $b \to a \to c$ 且 $b - c$，则定向 $b \to c$（否则 $b \to a \to c \to b$ 是有向圈）；
3. 若 $b - a_1 \to c$、$b - a_2 \to c$，$a_1$、$a_2$ 不相邻，且 $b - c$，则定向 $b \to c$。

Meek（1995）证明，反复应用规则 1–3 直到没有规则可用，恰好得到 CPDAG：规则是可靠的（它们定向的每条边都是强制边），也是完备的（每条强制边都被定向）。只有当背景知识迫使出现更多定向时，才需要第四条规则。

**算法 13.4.2（PC 算法）** **PC 算法**（Spirtes 与 Glymour 1991）是在第 1 步中以更经济的方式搜索分离集的 IC 算法。从完全无向图出发。对 $\ell = 0, 1, 2, \dots$：对每一对仍然相邻的 $a - b$，检验 $a \perp b \mid S$，其中 $S$ 取遍 $a$ 的当前邻点（不含 $b$）以及 $b$ 的当前邻点中大小为 $\ell$ 的所有子集；若某次检验接受独立性，就删去该边并记录 $S_{ab} = S$。当没有节点除被检验的节点外还有多于 $\ell$ 个邻点时停止。然后如 IC 算法的第 2、3 步那样定向。

先检验小的条件集，并且只在当前邻点中取，其理由是：若 $a$ 与 $b$ 被某个集合 d-分离，则它们被 $a$ 的父节点的某个子集或 $b$ 的父节点的某个子集 d-分离，而这些父节点始终是邻点。当真图的最大度有界时，检验次数是 $n$ 的多项式，这使 PC 在稀疏图中可以处理数百个变量。小的条件集还意味着检验更可靠。与顺序无关的变体 PC-stable（Colombo 与 Maathuis 2014）在每一层 $\ell$ 开始时固定邻点集，使输出不依赖变量的顺序。

### 13.4.2. 一个完整的例子

**例 13.4.1（五个变量上的 PC）** 设数据来自带箭头 $X_1 \to X_2$、$X_1 \to X_3$、$X_2 \to X_4$、$X_3 \to X_4$、$X_3 \to X_5$、$X_4 \to X_5$ 的 DAG，样本足够大，能准确揭示所有条件独立性。

![五个变量上的 PC 算法：真 DAG、第 1 步找到的骨架、第 2 步找到的 v-结构（红色）以及应用 Meek 规则后的 CPDAG（蓝色的弧在第 3 步定向）。](./plots/pc_steps.py)

*第 1 步：骨架。* 对 $10$ 对节点中的每一对，先检验边缘独立性，再检验给定大小递增的集合时的条件独立性，在第一个分离该对的集合处停止（对 $X_1$ 与 $X_2$，要检验 $\{X_3, X_4, X_5\}$ 的至多 $8$ 个子集）。结果如下：

| 节点对 | 结果 | $S_{ab}$ |
|---|---|---|
| $X_1, X_2$；$X_1, X_3$；$X_2, X_4$；$X_3, X_4$；$X_3, X_5$；$X_4, X_5$ | 给定任何集合都相依 | 相邻 |
| $X_2, X_3$ | $X_2 \perp X_3 \mid X_1$ | $\{X_1\}$ |
| $X_1, X_4$ | $X_1 \perp X_4 \mid \{X_2, X_3\}$ | $\{X_2, X_3\}$ |
| $X_1, X_5$ | $X_1 \perp X_5 \mid \{X_3, X_4\}$ | $\{X_3, X_4\}$ |
| $X_2, X_5$ | $X_2 \perp X_5 \mid \{X_3, X_4\}$ | $\{X_3, X_4\}$ |

$\{X_1, X_4\}$ 不能分离 $X_2, X_5$：对对撞因子 $X_4$ 取条件会打开 $X_2 \to X_4 \leftarrow X_3 \to X_5$，而只有 $X_3$ 能阻断它。当多个集合都能分离一对节点时，如 $\{X_3, X_4\}$ 与 $\{X_2, X_3\}$ 都分离 $X_1$ 与 $X_5$，算法保留最先找到的那个，不必找出全部。骨架有真 DAG 的六条边。

*第 2 步：v-结构。* 有公共邻点的不相邻节点对为：$X_2, X_3$（公共邻点 $X_1$ 与 $X_4$）、$X_1, X_4$（公共邻点 $X_2$、$X_3$）、$X_1, X_5$（公共邻点 $X_3$）和 $X_2, X_5$（公共邻点 $X_4$）。只有 $X_4 \notin S_{23} = \{X_1\}$ 给出 v-结构：$X_2 \to X_4 \leftarrow X_3$。其余公共邻点都属于相应的分离集（$X_1 \in S_{23}$；$X_2, X_3 \in S_{14}$；$X_3 \in S_{15}$；$X_4 \in S_{25}$）。

*第 3 步：Meek 规则。* 规则 1 用于 $X_2 \to X_4 - X_5$（$X_2$ 与 $X_5$ 不相邻），定向 $X_4 \to X_5$（不产生新的 v-结构）。规则 2 用于 $X_3 \to X_4 \to X_5$ 与 $X_3 - X_5$，定向 $X_3 \to X_5$（不产生有向圈）。没有规则适用于 $X_1 - X_2$ 与 $X_1 - X_3$：只要避免 v-结构 $X_2 \to X_1 \leftarrow X_3$，两种定向都是可能的。

结果是 CPDAG：$X_1 - X_2$、$X_1 - X_3$ 无向，其余四条边的方向与真 DAG 相同。该等价类含三个 DAG（$X_1$ 为源点；$X_2 \to X_1 \to X_3$；$X_3 \to X_1 \to X_2$）。要判断类似季节的变量 $X_1$ 是 $X_2$ 的原因还是结果，需要对 $X_1$ 或 $X_2$ 做干预，或者需要背景知识。

:::

### 13.4.3. 条件独立性检验

$X \perp Y \mid S$ 的独立性检验检验 $H_0\colon \mathbb{P}(x, y \mid s) = \mathbb{P}(x \mid s)\,\mathbb{P}(y \mid s)$。一般的选择是 [3.2.5](/3.2.5) 的**似然比检验**：在 $H_0$ 下，统计量 $G^2 = 2\log\Lambda$ 渐近服从 $\chi^2$ 分布，自由度等于备择模型与原假设模型的维数之差。

**定理 13.4.1（离散数据的检验）** 设 $X_i$、$X_j$ 与向量 $\boldsymbol{X}_k$ 都是离散的，$\#(X)$ 为 $X$ 的类别数，$N_{abc}$ 为 $N$ 个案例中 $X_i = a$、$X_j = b$、$\boldsymbol{X}_k = c$ 的个数（边缘计数记为 $N_{ac}$、$N_{bc}$、$N_c$）。在 $H_0\colon X_i \perp X_j \mid \boldsymbol{X}_k$ 之下，

$$
G^2 = 2\sum_{a, b, c} N_{abc}\log\frac{N_{abc}N_c}{N_{ac}N_{bc}} \xrightarrow{d} \chi^2_{\mathrm{df}}, \qquad \mathrm{df} = (\#(X_i) - 1)(\#(X_j) - 1)\prod_{X \in \boldsymbol{X}_k}\#(X),
$$
当 $N \to \infty$ 时。

该统计量等于 $X_i$ 与 $X_j$ 在给定 $\boldsymbol{X}_k$ 时的经验条件**互信息**的 $2N$ 倍，`bnlearn` 因此把这个检验称为 `"mi"`。自由度随每个条件变量成倍增加，所以检验需要每个格子有许多观测；样本小时，大的条件集意味着功效低，边于是被错误地删除。（实际中自由度常常要减去空格的个数。）

**定理 13.4.2（Gauss 数据的检验）** 若变量服从联合正态分布，则 $X_i \perp X_j \mid \boldsymbol{X}_k$ 等价于**偏相关系数** $\rho_{ij \cdot k}$ 为零。设 $\hat\rho_{ij \cdot k}$ 为由 $N$ 个观测算出的样本偏相关系数，则

$$
\sqrt{N - \lvert k\rvert - 3}\;\cdot\;\frac12\log\frac{1 + \hat\rho_{ij \cdot k}}{1 - \hat\rho_{ij \cdot k}} \xrightarrow{d} \mathcal{N}(0, 1) \quad\text{在 } H_0 \text{ 下},
$$
所以其平方趋于 $\chi^2_1$；$\lvert k\rvert$ 是条件变量的个数。

这个变换就是偏相关系数的 **Fisher z 变换**。样本偏相关系数由 $(X_i, X_j, \boldsymbol{X}_k)$ 的样本相关矩阵的逆 $P$ 算出，$\hat\rho_{ij \cdot k} = -P_{ij}/\sqrt{P_{ii}P_{jj}}$（13.5.1 节）。

```r
res <- pc.stable(data, test = "mi")   # PC-stable with mutual information (G-squared) tests
plot(res)                             # the PDAG: undirected edges have no arrowheads
res2 <- pc.stable(data[, c(2, 1, 3, 4, 5)], test = "mi")   # same CPDAG
```

在洒水器数据上，`pc.stable` 恢复出骨架、v-结构 Sprinkler $\to$ Wet $\leftarrow$ Rain 和强制弧 Wet $\to$ Slippery，并让 Season $-$ Sprinkler 与 Season $-$ Rain 保持无向，恰好是真网络的 CPDAG。要得到因果 DAG，需要借助背景知识为无向边定向（季节不是由洒水器引起的），例如使用 `set.arc`。

![用带 Fisher z 检验（水平 0.05）的 PC 算法恢复结构，数据由线性 Gauss 结构模型模拟，其 DAG 为例 13.4.1 的 DAG。左：200 次重复中骨架与整个 CPDAG 被准确恢复的比例。右：骨架中错误边的平均个数。模拟数据。](./plots/pc_simulation.py)

模拟显示，即使只有五个变量，也需要相当多的数据。错误来自两类检验错误：样本小时，较弱的相依性检测不出来，真边被删除；在每种样本量下，真的独立性都有约 $0.05$ 的概率被拒绝，从而保留一条伪边。定向错误源于骨架错误，因为一个错误的分离集就会改变 v-结构，而 Meek 规则又把错误传播到其他边。在所选的模型中，从 $X_1$ 到 $X_4$ 的两条路径的效应符号相反、几乎抵消，所以分布接近不忠实，恢复很慢；若路径恰好抵消，则无论样本量多大都会失败。

| | 约束法 |
|---|---|
| 优点 | 在稀疏图中可扩展到许多变量；每个决定都基于可解释的检验；返回等价类，这是观测数据给出的诚实输出 |
| 缺点 | 难以做出可靠的检验，尤其是样本小时（假阳性与假阴性）；一次错误的检验可能使输出出现多处错误，所以方法对噪声不够稳健；依赖忠实性 |

## 13.5. 讨论与其他方法

### 13.5.1. Gauss 图模型

**定义 13.5.1（Gauss 图模型）** 设 $\boldsymbol{X} = (X_1, \dots, X_p)$ 服从多元正态分布，协方差矩阵 $\Sigma$ 正定。矩阵 $\Omega = \Sigma^{-1}$ 称为**精度矩阵**（浓度矩阵）。$\boldsymbol{X}$ 的 **Gauss 图模型**是 $\{1, \dots, p\}$ 上的无向图，其中边 $i - j$ 存在当且仅当 $\Omega_{ij} \neq 0$。

**定理 13.5.1** 设 $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$，$i \neq j$。则 $X_i \perp X_j \mid \boldsymbol{X}_{-\{i,j\}}$ 当且仅当 $\Omega_{ij} = 0$。更精确地，$X_i$ 与 $X_j$ 在给定所有其他变量时的偏相关系数为 $-\Omega_{ij}/\sqrt{\Omega_{ii}\Omega_{jj}}$。

**证明** 由**多元正态分布**的条件分布（[3.1.15](/3.1.15)），给定其余变量时 $(X_i, X_j)$ 的条件协方差矩阵是 $\Omega$ 中行列指标为 $i, j$ 的 $2 \times 2$ 子矩阵的逆（Schur 补恒等式）。$\begin{bmatrix}\Omega_{ii} & \Omega_{ij}\\ \Omega_{ij} & \Omega_{jj}\end{bmatrix}$ 的逆，其非对角元为 $-\Omega_{ij}/(\Omega_{ii}\Omega_{jj} - \Omega_{ij}^2)$，对角元为 $\Omega_{jj}/(\cdot)$、$\Omega_{ii}/(\cdot)$，所以条件相关系数为 $-\Omega_{ij}/\sqrt{\Omega_{ii}\Omega_{jj}}$，而对正态变量，条件相关系数为零就是条件独立。$\square$

精度矩阵的零元编码的是给定所有其他变量时的独立性，这与边缘独立性不同。在链 $X_1 \to X_2 \to X_3$ 中，精度矩阵是三对角的（$\Omega_{13} = 0$），尽管 $X_1$ 与 $X_3$ 相关。在对撞结构 $X_1 \to X_3 \leftarrow X_2$ 中，$X_1 \perp X_2$ 边缘成立，但 $\Omega_{12} \neq 0$，因为给定 $X_3$ 时它们相依。对由 DAG 生成且与之忠实的分布，Gauss 图模型是该 DAG 的道德图：把每个共同子节点的父节点两两连接，再去掉方向。当变量多于观测时，$\Omega$ 用**图 lasso**（[7.9.11](/7.9.11)）的惩罚似然估计。

### 13.5.2. 表达能力

有向图与无向图不能总是在不损失独立性的前提下相互转换。四个变量上没有哪个 DAG 恰好表示独立性 $X \perp Y \mid \{W, Z\}$ 与 $W \perp Z \mid \{X, Y\}$，即无向四圈 $X - W - Y - Z - X$ 的独立性：把这个圈定向为没有有向圈的任何方式都含有对撞因子，破坏两条陈述之一。反过来，没有哪个无向图恰好表示 v-结构 $X \to Z \leftarrow Y$ 的独立性，即 $X \perp Y$ 但 $X \not\perp Y \mid Z$：无向图要么经 $Z$ 把 $X$ 与 $Y$ 连起来，使它们边缘相依，要么根本不连。这种不对称正是因果发现使用 DAG 与 v-结构的原因。

### 13.5.3. 进阶方法

混合法把两类方法结合起来。最大最小爬山法（MMHC；Tsamardinos、Brown 与 Aliferis 2006）先用条件独立性检验为每个变量找出候选父节点与子节点的集合，再在这些候选之间的弧上做受限的爬山；它在 `bnlearn` 中为 `mmhc`。

分解与局部学习把大问题化为小问题。Xie 与 Geng（2008）的递归方法利用无向独立图，把学习大 DAG 的问题分解为学习两个较小的图的问题，递归地学习各小问题的局部骨架并加以合并，然后再定向；这是一种分治方法，同样的条件独立性检验在更小的条件集上进行。当只关心单个目标变量 $T$ 的原因时，没有必要学习整个网络。PCD-by-PCD 算法（Zhou、Wang、Yin 与 Geng 2010）先找出 $T$ 的父节点、子节点与后代的集合 $\mathrm{PCD}(T)$，再找这些变量的 PCD 集，如此向外扩展；当两个变量各在对方的 PCD 集中时，建立边 $x - z$，在已探索节点中发现的 v-结构为边做局部定向，一旦 $T$ 处的所有边都已定向，搜索就停止。还可以设计操纵部分变量的实验，用尽可能少的干预为 CPDAG 余下的无向边定向（He 与 Geng 2008）。

当前的研究课题包括时间序列的因果图（动态 Bayes 网络）、非 Gauss 连续数据的条件独立性检验（核方法）、重抽样下所学结构的稳定性、潜变量（FCI 算法返回部分祖先图而不是 CPDAG），以及把先验知识或领域知识纳入约束法。由观测数据与干预数据混合学习，可以识别出比等价类更多的信息。

评价算法时，把学得的结构与真结构比较，可以在模拟中进行，也可以在基准网络上进行，例如 ALARM（重症监护的监测网络，37 个节点、46 条弧；Beinlich 等 1989），比较的指标是多出与缺失的边数，以及结构 Hamming 距离（structural Hamming distance），简称 SHD：把学得的 CPDAG 变成真 CPDAG 所需的边插入、删除与反转（或改变定向）的次数。在例 13.4.1 中，若某个 CPDAG 除了多出一条边 $X_2 - X_3$ 之外都正确，则其 SHD 为 $1$。

## 小结

- 已知 DAG 的参数学习：对数似然分解为每个家庭一项（式 (13.1)）；对离散 CPD，极大似然估计就是条件频率 $N_{ijk}/N_{ij}$（定理 13.1.1），Dirichlet 先验给出共轭后验。R 中用 `empty.graph`、`arcs<-`、`bn.fit`。
- 可识别性：数据至多确定 Markov 等价类（相同的骨架与 v-结构），用 CPDAG 表示（定义 13.2.1）；为其余的边定向需要干预或背景知识。
- 结构学习：

  | | 搜索评分法 | 约束法 |
  |---|---|---|
  | 输入 | 得分：对数似然（过拟合）、AIC、BIC、Bayes 边缘似然 | 条件独立性检验：$G^2$ / 互信息、Fisher $z$ |
  | 算法 | 对弧的添加、删除与反转做爬山 | IC / PC：骨架、v-结构、Meek 规则 |
  | 输出 | 一个 DAG（局部最优） | CPDAG |
  | 弱点 | 局部最优、代价 | 检验错误会传播；依赖忠实性 |

- PC 三步（算法 13.4.2、例 13.4.1）：当某个集合 $S$ 使 $a$、$b$ 独立时删去 $a - b$，按大小递增、在当前邻点中检验集合；对有公共邻点 $c \notin S_{ab}$ 的不相邻节点 $a, b$，定向 $a \to c \leftarrow b$；再对更多的边定向，使其不产生新的 v-结构和有向圈（定义 13.4.2）。至少需要 $\binom{n}{2}$ 次检验（每对节点一次）；IC 可能需要 $O(n^2 2^{n-2})$ 次。
- Gauss 图模型：$\Omega_{ij} = 0$ 当且仅当 $X_i \perp X_j$ 给定其他所有变量（定理 13.5.1）；无向图是 DAG 的道德图。有向图与无向图的表达能力不同。
- 其他方法：MMHC、递归分解、局部的 PCD-by-PCD 学习、干预设计；在 ALARM 等基准上用 SHD 评价。

## 思考题

1. 你用约束法学习五个变量 $X, Y, Z, R, W$ 上的 DAG 的结构。至少必须做多少次条件独立性检验？

   **答** $\binom{5}{2} = 10$ 对节点每一对至少要检验一次，先用空的条件集，所以至少需要 $10$ 次检验。只有当每个边缘检验都已接受独立性（空图）时才取到最小值。否则还要继续检验：边缘相依的不相邻节点对要一直检验到找到分离集，相邻的节点对要一直检验到所有候选条件集用完。
2. 对 $X, Y, Z, R, W$ 的数据做检验，得到：$X \perp Y$；$X \perp R \mid Z$；$X \perp W \mid Z$；$Y \perp R \mid Z$；$Y \perp W \mid Z$；其余各对都没有条件独立性。逐步学习结构。哪些边仍然无向？如何为它们定向？

   **答** 骨架：未被分离的节点对为 $X - Z$、$Y - Z$、$Z - R$、$Z - W$、$R - W$。分离集：$S_{XY} = \varnothing$，$S_{XR} = S_{XW} = S_{YR} = S_{YW} = \{Z\}$。v-结构：$X$ 与 $Y$ 不相邻，公共邻点 $Z \notin S_{XY}$，所以 $X \to Z \leftarrow Y$；其他不相邻的节点对以 $Z$ 为公共邻点，且 $Z$ 在它们的分离集中，所以没有更多的 v-结构。Meek 规则 1：$X \to Z - R$ 且 $X$、$R$ 不相邻，得 $Z \to R$；同理 $Z \to W$。边 $R - W$ 保持无向：$Z \to R \to W$ 与 $Z \to W \to R$ 都无圈，且不产生新的 v-结构（因为 $Z$ 与 $R$、$W$ 都相邻）。可以用设定 $R$ 的实验为它定向（若 $W$ 的分布改变，则 $R \to W$），或者用测量的时间顺序等背景知识。
3. 由完整数据推导 $\mathbb{P}(\text{Wet} \mid \text{Sprinkler}, \text{Rain})$ 的极大似然估计，以及对每种父节点取值组合取独立的 $\mathrm{Dir}(1, 1)$ 先验时的后验均值。

   **答** 由定理 13.1.1，$\hat{\mathbb{P}}(\text{Wet} = k \mid s, r) = N_{s r k}/N_{s r}$，即在洒水器状态为 $s$、降雨状态为 $r$ 的案例中路面湿的比例。对四行中的每一行取 $\mathrm{Dir}(1, 1) = \mathrm{Beta}(1, 1)$ 先验，后验为 $\mathrm{Beta}(1 + N_{sr,\text{wet}}, 1 + N_{sr,\text{dry}})$，后验均值为 $(N_{sr,\text{wet}} + 1)/(N_{sr} + 2)$，即 Laplace 估计，即使对从未观测到的取值组合，它也严格介于 $0$ 与 $1$ 之间。
4. 为什么以 $\log \mathbb{P}(D \mid \hat{\boldsymbol{\phi}}_G, G)$ 为得分的爬山法倾向于返回近乎完全的图？AIC 与 BIC 如何改变这一点？两者中哪个是相合的？

   **答** 添加一条弧 $a \to b$ 会扩大 $b$ 的 CPD 族（原模型是 $b$ 不依赖 $a$ 的特例），所以极大化的似然不会减小；数据有限时它几乎总是略有增大，因此每个无圈的添加都会被接受。AIC 对每个多余参数减去 $2$，BIC 减去 $\log M$（在 $-2\log$ 的尺度上），所以只有当一条弧使拟合的改善超过它的代价时才会被添加。BIC 的惩罚随 $M$ 增大，它以趋于 1 的概率选中真正的等价类；AIC 的惩罚固定，即使渐近地也以正的概率保留伪弧。
5. 对两个二值变量 $X_i$、$X_j$ 和由两个各有三个类别的变量构成的条件集，$G^2$ 检验的自由度是多少？这对小样本意味着什么？

   **答** $\mathrm{df} = (2 - 1)(2 - 1)\cdot 3 \cdot 3 = 9$。数据被分成 $9$ 层，每层是一张 $2 \times 2$ 表；若只有 $100$ 个观测，这些表很稀疏，$\chi^2$ 近似很差，功效也低。功效低意味着检测不出相依性，于是真边被删除；这是 PC 先检验小条件集的原因之一。
6. 给出 DAG $A \to B$、$B \to C$、$A \to C$、$C \to D$ 的 CPDAG，以及 DAG $A \to C$、$B \to C$、$C \to D$ 的 CPDAG。每个等价类各含多少个 DAG？

   **答** 第一个 DAG 没有 v-结构（$A$、$B$、$C$ 构成三角形，$D$ 只有一个父节点 $C$），所以它的 CPDAG 是完全无向的：$A - B$、$B - C$、$A - C$、$C - D$。它的成员是没有 v-结构的无圈定向。若 $C \to D$，三角形的 $3! = 6$ 种无圈定向都可以。若 $D \to C$，则 $C$ 不能再有其他父节点（$A$ 与 $B$ 不与 $D$ 相邻），所以 $C \to A$ 且 $C \to B$，$A - B$ 可以取两个方向：再有 $2$ 个。该类共有 $8$ 个 DAG。第二个 DAG 有 v-结构 $A \to C \leftarrow B$，于是 Meek 规则 1 定向 $C \to D$，所以其 CPDAG 就是这个 DAG 本身，该类只有一个成员。
7. 设 $X_1 \to X_2 \to X_3$，$X_1 \sim \mathcal{N}(0, 1)$，$X_2 = X_1 + \varepsilon_2$，$X_3 = X_2 + \varepsilon_3$，$\varepsilon_2, \varepsilon_3 \sim \mathcal{N}(0, 1)$ 相互独立。计算 $\Sigma$ 与 $\Omega = \Sigma^{-1}$，并读出 Gauss 图模型。

   **答** $\operatorname{Var}(X_1) = 1$，$\operatorname{Var}(X_2) = 2$，$\operatorname{Var}(X_3) = 3$，$\operatorname{Cov}(X_1, X_2) = \operatorname{Cov}(X_1, X_3) = 1$，$\operatorname{Cov}(X_2, X_3) = 2$，所以 $\Sigma = \begin{bmatrix}1 & 1 & 1\\ 1 & 2 & 2\\ 1 & 2 & 3\end{bmatrix}$，$\Omega = \begin{bmatrix}2 & -1 & 0\\ -1 & 2 & -1\\ 0 & -1 & 1\end{bmatrix}$（验算：$\Sigma\Omega = I_3$）。图模型是无向链 $X_1 - X_2 - X_3$：$\Omega_{13} = 0$ 表示 $X_1 \perp X_3 \mid X_2$，尽管 $\operatorname{Corr}(X_1, X_3) = 1/\sqrt 3 \neq 0$。
8. 为例 13.4.1 学得的某个 CPDAG，所有边都正确，只是缺少 $X_3 \to X_5$，并且 $X_1 - X_2$ 被定向为 $X_1 \to X_2$。它与真 CPDAG 的结构 Hamming 距离是多少？

   **答** 要撤销一次删除（插入 $X_3 \to X_5$），并改变一次定向（把 $X_1 \to X_2$ 改回 $X_1 - X_2$），所以 SHD 为 $2$。注意，缺失的边在实践中还会改变其他定向：没有 $X_3 - X_5$，规则 2 就不再适用，PC 的输出会在更多的地方不同。
