---
title: 相律与单组分系统的相平衡
description: 相与相平衡条件；物种数、独立反应数、浓度限制条件与独立组分数；自由度数与 Gibbs 相律的推导、条件自由度与广义相律；Clapeyron 方程与 Clausius–Clapeyron 方程（含蒸发焓随温度的修正）、固–液平衡与外压对蒸气压的影响；一级相变、二级相变与 Ehrenfest 方程、λ 相变；水的相图、三相点与冰点、高压冰相、CO₂ 与超临界流体。
---

溶解、蒸馏、结晶、萃取、冶金，以及细胞膜的凝胶–液晶转变，都是多相系统趋于平衡的过程。上一章讨论化学平衡，本章与下一章讨论相平衡：同一套热力学原理——平衡时每种物质在它所在的各相中**化学势**相等（[6.3.4](/6.3.4)）——用于相之间的物质交换。本章先给出一切相平衡系统都遵守的计数规律 Gibbs 相律，它不涉及任何具体物质，却告诉我们一个系统最多能有几相共存、需要几个强度变量才能确定它的状态；然后用化学势相等的条件推出纯物质两相平衡线的方程（Clapeyron 方程），把 [6.1.1](/6.1.1#sec-1.2.2) 中的 Clausius–Clapeyron 方程放到严格的基础上，并说明它的近似与修正；再按化学势导数的连续性对相变分类，讨论物理 [5.3.8](/5.3.8) 与 [5.3.9](/5.3.9) 中出现过的铁磁转变与超导转变；最后读懂单组分系统的相图。[6.3.9](/6.3.9) 把相律和本章的方法用于二组分与三组分系统；表面与弯曲界面对相平衡的影响（Kelvin 方程）留到 [6.3.19](/6.3.19)。

## 8.1. 相与相平衡条件

### 8.1.1. 相与相数

**定义 8.1.1（相）** 系统中物理性质与化学性质完全均匀的部分称为一个**相**。系统中共存的相的数目称为相数，记作 $P$。只含一个相的系统称为均相系统，含两个以上相的称为多相系统。

相与相之间有明显的界面，越过界面时某些性质（密度、折射率、组成等）发生突变。判断相数要看物质在什么层次上混合：

- 气体：任意多种气体都能以分子层次混合，只有一个气相。
- 液体：按互溶程度可以是一相（水与乙醇）、两相（水与苯）甚至三相；牛奶、豆浆是乳状液与胶体分散系统，不是一相（[6.3.21](/6.3.21)）。
- 固体：除了固溶体（[6.1.4](/6.1.4)）以外，一种固体就是一个相。$\ce{CaCO3(s)}$ 与 $\ce{CaO(s)}$ 的粉末无论混得多么均匀仍是两相；铁的 $\alpha$、$\gamma$、$\delta$ 等晶型各是一相；一堆小冰块，或大块与粉末状的 $\ce{CaCO3(s)}$，只是一相——相的数目与这种物质分成几块无关。

### 8.1.2. 相平衡条件

多相系统达到热力学平衡，要同时满足热平衡（各相温度相等）、力平衡（界面为平面时各相压力相等）、相平衡与化学平衡。相平衡的条件由**化学势**给出：等温等压下若物质 B 在 $\alpha$、$\beta$ 两相中化学势不等，$\mathrm{d}n_{\mathrm{B}}$ 由 $\alpha$ 转入 $\beta$ 使系统的 Gibbs 自由能改变 $\mathrm{d}G = (\mu_{\mathrm{B}}^{\beta} - \mu_{\mathrm{B}}^{\alpha})\,\mathrm{d}n_{\mathrm{B}}$，物质自发地从化学势高的相流向化学势低的相，直到二者相等（[6.3.4](/6.3.4)）。

**定义 8.1.2** 多相系统中各相的组成与数量不随时间变化的状态称为**相平衡**。

**定理 8.1.1（相平衡条件）** 温度、压力均匀的多相系统处于相平衡的充要条件是：任一物质 B 在它所存在的所有相中化学势相等，

$$
\mu_{\mathrm{B}}^{\alpha} = \mu_{\mathrm{B}}^{\beta} = \cdots .
$$

条件只要求物质在它所存在的各相中化学势相等，并不要求每种物质在每一相中都存在。例如蔗糖水溶液与其蒸气平衡时，蔗糖不挥发，只有水满足 $\mu_{\mathrm{H_2O}}(\mathrm{sln}) = \mu_{\mathrm{H_2O}}(\mathrm{g})$。对一个只允许 $\ce{O2}$ 透过的**半透膜**，膜两侧只有 $\ce{O2}$ 的化学势相等，两侧的压力可以不同（§8.2.3）。

相平衡的一个重要特点是：它只取决于强度性质，与各相物质的多少无关。$25\,{}^\circ\mathrm{C}$ 时一杯水与一滴水上方的饱和蒸气压相同；溶液的沸点、凝固点、溶解度都是强度性质。因此，描述一个相平衡系统需要多少个强度变量，就是下一节的问题。

## 8.2. 相律

### 8.2.1. 物种数与独立组分数

描述系统的组成，先要数清其中有几种物质，但"几种物质"的答案取决于看问题的层次：纯水可以看作只含 $\ce{H2O}$，也可以看作含 $\ce{H2O}$、$\ce{H+}$、$\ce{OH-}$ 三种物质。需要一个与描述方式无关的量。

**定义 8.2.1（独立组分数）** 设系统中有 $s$ 种化学物质（物种数），物种之间有 $r$ 个独立的化学平衡（独立反应数：不能由其他反应式线性组合得到），另有 $r'$ 个浓度限制条件（同一相中几种物质的浓度之间固定不变的关系，各相中 $\sum_{\mathrm{B}} x_{\mathrm{B}} = 1$ 不计在内）。称

$$
C = s - r - r'
$$
为系统的**独立组分数**（简称组分数）。它是确定平衡系统中所有各相组成所需的最少物种数，也就是平衡系统中可以独立改变其数量的物种数。

浓度限制条件必须是同一相内的强度关系，它通常来自系统的制备方式（反应物按计量比投料、只由一种物质分解而来）或电中性条件。几个例子：

| 系统 | $s$ | $r$ | $r'$ | $C$ | 说明 |
|---|---|---|---|---|---|
| 纯水，只计 $\ce{H2O}$ | 1 | 0 | 0 | 1 | |
| 纯水，计 $\ce{H2O, H+, OH-}$ | 3 | 1 | 1 | 1 | 电中性：$x(\ce{H+}) = x(\ce{OH-})$ |
| $\ce{H2(g) + I2(g) <=> 2HI(g)}$，任意投料 | 3 | 1 | 0 | 2 | |
| 同上，$\ce{H2}$ 与 $\ce{I2}$ 等量投料或只由 $\ce{HI}$ 分解 | 3 | 1 | 1 | 1 | $p(\ce{H2}) = p(\ce{I2})$ |
| $\ce{C(s)}$、$\ce{O2}$、$\ce{CO}$、$\ce{CO2}$ | 4 | 2 | 0 | 2 | 三个燃烧反应中只有两个独立 |
| $\ce{NH4Cl(s)}$ 在真空容器中分解 | 3 | 1 | 1 | 1 | 气相中 $p(\ce{NH3}) = p(\ce{HCl})$ |
| 同上，容器中预先有任意量 $\ce{NH3}$ | 3 | 1 | 0 | 2 | |
| $\ce{CaCO3(s)}$ 在真空容器中分解 | 3 | 1 | 0 | 2 | $\ce{CaO}$ 与 $\ce{CO2}$ 不在同一相 |
| $\ce{HCN}$ 水溶液 | 5 | 2 | 1 | 2 | $\ce{H2O, H+, OH-, HCN, CN-}$；电中性 |

$\ce{CaCO3}$ 分解生成的 $\ce{CaO}$ 与 $\ce{CO2}$ 物质的量虽然相等，但它们分处固、气两相，"物质的量相等"不是任何一相的强度关系，不改变任何相的组成自由度，所以不算浓度限制条件。同理，**Nernst 分配定律**（[6.3.6](/6.3.6)）给出的两相浓度之比也不是浓度限制条件：它是相平衡条件 $\mu_{\mathrm{B}}^{\alpha} = \mu_{\mathrm{B}}^{\beta}$ 的推论，在推导相律时已经计入（§8.2.2），再算一次就重复了。

$C$ 与看问题的层次无关：多计一种物种，就同时多出一个反应或一个限制条件。上表中纯水的两种算法、$\ce{HCN}$ 溶液按分子（$\ce{H2O}$、$\ce{HCN}$，$C = 2$）与按离子的两种算法，结果都相同。

### 8.2.2. 自由度数与 Gibbs 相律

**定义 8.2.2（自由度数）** 在不改变系统相态（不使旧相消失、新相产生）的条件下，可以在一定范围内独立变动的强度变量的数目，称为系统的**自由度数**，记作 $F$。它等于描述系统所需的强度变量总数减去平衡时这些变量之间必须满足的独立关系式的数目。

**定理 8.2.1（相律）** 处于热平衡、力平衡、相平衡与化学平衡的系统，若只有温度与压力两个外部强度变量，则

$$
F = C - P + 2.
\tag{8.1}
$$

**证明** 先设 $s$ 种物质在 $P$ 个相中都存在。强度变量为温度 $T$、压力 $p$（热平衡与力平衡使各相的 $T$、$p$ 相同）与各相的组成；每相的组成用 $s$ 个摩尔分数描述，但它们之和为 1，独立的只有 $s - 1$ 个。因此强度变量共有

$$
2 + P(s - 1)
$$
个。平衡时它们之间的独立关系有：

1. 相平衡条件（定理 8.1.1）：每种物质在 $P$ 个相中的化学势相等，给出 $P - 1$ 个等式，$s$ 种物质共 $s(P - 1)$ 个。化学势是 $T$、$p$ 与该相组成的函数，所以这些都是强度变量之间的方程。
2. 化学平衡条件：每个独立反应有 $\sum_{\mathrm{B}} \nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$，共 $r$ 个。
3. 浓度限制条件 $r'$ 个。

于是

$$
F = 2 + P(s - 1) - s(P - 1) - r - r' = (s - r - r') - P + 2 = C - P + 2.
$$

若某种物质 B 不存在于某一相中，该相的组成变量少一个，B 的化学势等式也少一个，二者相消，结论不变。$\square$

相律只是变量计数，它不涉及任何物质的具体性质，因而对一切相平衡系统普遍成立；代价是它只告诉我们独立变量有几个，不告诉我们是哪几个，也不告诉我们相态如何随变量变化——那要靠热力学计算或实验测定，结果画成相图。由 $F \geq 0$ 得 $P \leq C + 2$：组分数为 $C$ 的系统最多 $C + 2$ 相共存。相数每多一个，自由度数就少一个；$P = 1$ 时 $F$ 最大，$F = 0$ 时 $P$ 最大。

相律由 Gibbs 在 1875–1878 年分两部分发表的长文《论多相物质的平衡》中给出。这篇三百多页的论文以抽象的数学形式写成，发表在不出名的康涅狄格科学院学报上，十多年后才经 Ostwald（1892 年德译本）与 Le Chatelier（1899 年法译本）的翻译而广为人知，此后成为冶金、地质与化工中分析多相系统的基本工具。

### 8.2.3. 条件自由度与广义相律

式 (8.1) 中的"2"代表温度与压力，并且假定各相的温度、压力分别相同。实际问题中常有两种修正。

**定义 8.2.3（条件自由度）** 人为指定某些强度变量后剩下的自由度数称为**条件自由度**，记作 $F^*$。恒压（或恒温）时 $F^* = C - P + 1$，等温等压时 $F^* = C - P$。

**定理 8.2.2（广义相律）** 若除组成以外，确定系统状态所需的外部强度变量共有 $n$ 个，则 $F = C - P + n$。

$n$ 要具体分析：电场、磁场、重力场的作用不可忽略时，$n$ 大于 2；用半透膜隔开的两部分压力可以不同时，每一部分的压力都是独立变量。凝聚系统的性质对压力不敏感，常把压力看作不变，这时 $n = 1$。

**例 8.2.1** 一个容器被只允许 $\ce{O2}$ 透过的半透膜分成两部分：左边是 $\ce{Ag(s)}$、$\ce{Ag2O(s)}$ 与 $\ce{O2(g)}$，右边是 $\ce{O2}$ 与 $\ce{CCl4}$ 的混合气体。求系统的自由度数，以及 $298\,\mathrm{K}$ 时的条件自由度。

解：物种 $\ce{Ag, Ag2O, O2, CCl4}$，$s = 4$；左边有反应 $\ce{2Ag(s) + 1/2 O2(g) <=> Ag2O(s)}$，$r = 1$；$r' = 0$。故 $C = 3$。相有 $\ce{Ag(s)}$、$\ce{Ag2O(s)}$、左边气相、右边气相，$P = 4$。两边压力可以不同，外部强度变量是 $T$、$p_{\text{左}}$、$p_{\text{右}}$，$n = 3$。于是 $F = 3 - 4 + 3 = 2$；指定温度后 $F^* = 1$。

物理意义：温度一定时，左边的 $\ce{O2}$ 压力由 $\ce{Ag2O}$ 的分解平衡确定（它就是 $\ce{Ag2O}$ 的**分解压**，[6.3.7](/6.3.7)）；膜两边 $\ce{O2}$ 的化学势相等，右边 $\ce{O2}$ 的分压也随之确定，但右边还可以加入任意多的 $\ce{CCl4}$，总压（或 $\ce{O2}$ 的摩尔分数）可以独立变化，所以只剩一个自由度。若误用 $n = 2$，会得到 $F^* = 3 - 4 + 1 = 0$ 的错误结论。

### 8.2.4. 相律的应用

**例 8.2.2** 单组分的均相封闭系统：$F = 1 - 1 + 2 = 2$，温度与压力可以独立变化，摩尔体积等其他强度性质由它们确定（物态方程）。

**例 8.2.3** 纯液体在一定外压下的沸点有定值，溶液的沸点则没有：纯液体沸腾时 $C = 1$、$P = 2$，恒压下 $F^* = 1 - 2 + 1 = 0$；二组分溶液沸腾时 $C = 2$、$P = 2$，$F^* = 1$，沸点随组成变化，而且在沸腾过程中随液相组成的改变而升高（[6.3.9](/6.3.9)）。

**例 8.2.4** $p^\circ$ 下 $\ce{NaCl}$ 的饱和水溶液与 $\ce{NaCl(s)}$ 平衡共存：$C = 2$，$P = 2$，$F^* = 2 - 2 + 1 = 1$，所以溶解度是温度的单值函数，可以画成一条溶解度曲线。

**例 8.2.5** $\ce{Na2CO3}$ 与水可以生成 $\ce{Na2CO3.H2O}$、$\ce{Na2CO3.7H2O}$ 与 $\ce{Na2CO3.10H2O}$ 三种水合物。$p^\circ$ 下与 $\ce{Na2CO3}$ 水溶液平衡共存的水合物最多有几种？

解：物种为 $\ce{H2O}$、$\ce{Na2CO3}$ 与三种水合物，$s = 5$；每种水合物有一个生成反应，$r = 3$；$C = 5 - 3 = 2$，与水合物有几种无关。恒压下 $F^* = 2 - P + 1 = 3 - P \geq 0$，$P \leq 3$。溶液占一相，所以最多有两种水合物与溶液共存。

## 8.3. 纯物质的两相平衡

纯物质两相平衡时 $C = 1$、$P = 2$，$F = 1$：温度与压力只有一个可以独立变化，平衡压力是温度的函数 $p = p(T)$，在 $p$–$T$ 图上是一条曲线。它的方程由相平衡条件直接导出。

### 8.3.1. Clapeyron 方程

纯物质的化学势就是摩尔 Gibbs 自由能，$\mu^* = G_{\mathrm{m}}$，由**热力学基本方程**（[6.3.3](/6.3.3)），

$$
\mathrm{d}\mu^* = -S_{\mathrm{m}}\,\mathrm{d}T + V_{\mathrm{m}}\,\mathrm{d}p .
$$

两相平衡线的斜率由 Clapeyron 方程（Clapeyron equation）给出，它是 1834 年 Clapeyron 在推广 Carnot 的工作时得到的，后来 Clausius 用热力学第二定律给出了严格推导。

**定理 8.3.1（Clapeyron 方程）** 纯物质的 $\alpha$、$\beta$ 两相平衡共存时，平衡压力随温度的变化率为

$$
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta_{\mathrm{trs}}S_{\mathrm{m}}}{\Delta_{\mathrm{trs}}V_{\mathrm{m}}} = \frac{\Delta_{\mathrm{trs}}H_{\mathrm{m}}}{T\,\Delta_{\mathrm{trs}}V_{\mathrm{m}}},
\tag{8.2}
$$
其中 $\Delta_{\mathrm{trs}}H_{\mathrm{m}} = H_{\mathrm{m}}^{\beta} - H_{\mathrm{m}}^{\alpha}$、$\Delta_{\mathrm{trs}}V_{\mathrm{m}} = V_{\mathrm{m}}^{\beta} - V_{\mathrm{m}}^{\alpha}$ 是同一相变（$\alpha \to \beta$）在温度 $T$ 与平衡压力下的摩尔焓变与摩尔体积变化。

**证明** 在 $(T, p)$ 处两相平衡，$\mu^{\alpha}(T, p) = \mu^{\beta}(T, p)$。沿平衡线移到相邻的平衡点 $(T + \mathrm{d}T, p + \mathrm{d}p)$，两相仍然平衡，所以 $\mathrm{d}\mu^{\alpha} = \mathrm{d}\mu^{\beta}$：

$$
-S_{\mathrm{m}}^{\alpha}\,\mathrm{d}T + V_{\mathrm{m}}^{\alpha}\,\mathrm{d}p = -S_{\mathrm{m}}^{\beta}\,\mathrm{d}T + V_{\mathrm{m}}^{\beta}\,\mathrm{d}p ,
$$
即 $\Delta_{\mathrm{trs}}V_{\mathrm{m}}\,\mathrm{d}p = \Delta_{\mathrm{trs}}S_{\mathrm{m}}\,\mathrm{d}T$。平衡相变是等温等压下的**可逆过程**，$\Delta_{\mathrm{trs}}S_{\mathrm{m}} = \Delta_{\mathrm{trs}}H_{\mathrm{m}}/T$，代入即得。$\square$

Clapeyron 方程是严格的，没有任何近似；它适用于纯物质的任意两相平衡（气–液、气–固、液–固、两种晶型之间），条件是相变有焓变与体积变化。$\Delta_{\mathrm{trs}}H_{\mathrm{m}}$ 与 $\Delta_{\mathrm{trs}}V_{\mathrm{m}}$ 必须对应同一个相变方向；对 $\Delta_{\mathrm{trs}}H_{\mathrm{m}} = 0$、$\Delta_{\mathrm{trs}}V_{\mathrm{m}} = 0$ 的二级相变，式 (8.2) 成为 $0/0$ 型，要改用 Ehrenfest 方程（§8.4.2）。

**相变焓**总是由低温相到高温相为正（熔化、蒸发、升华都吸热），所以平衡线的斜率的正负由 $\Delta_{\mathrm{trs}}V_{\mathrm{m}}$ 决定：高温相体积较大时斜率为正（绝大多数物质的熔化线），较小时为负（水、Bi、Ga、Si 的熔化线）。

### 8.3.2. 气–液与气–固平衡

对蒸发与升华，作两个近似：凝聚相的摩尔体积比气体小得多，$\Delta V_{\mathrm{m}} \approx V_{\mathrm{m}}(\mathrm{g})$；蒸气是理想气体，$V_{\mathrm{m}}(\mathrm{g}) = RT/p$。代入式 (8.2) 即得 **Clausius–Clapeyron 方程**（[6.1.1](/6.1.1#sec-1.2.2) 的[定理 1.2.2](/6.1.1#thm-1.2.2)）：

$$
\frac{\mathrm{d}\ln(p/p^\circ)}{\mathrm{d}T} = \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{RT^2}.
\tag{8.3}
$$

对数里要除以一个压力单位（这里用 $p^\circ$，不影响导数）。两个近似的误差在正常沸点附近都只有百分之几：$100\,{}^\circ\mathrm{C}$ 时液态水的摩尔体积约为蒸气的 $1/1600$，水蒸气的压缩因子约 $0.985$；越接近**临界点**，两个近似越差，到临界点时 $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ 与 $\Delta V_{\mathrm{m}}$ 同时趋于零。

$\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ 可看作常数时，积分得

$$
\ln\frac{p_2}{p_1} = -\frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right),
\tag{8.4}
$$
$\ln p$ 对 $1/T$ 是直线，这是由蒸气压测定**摩尔蒸发焓**的依据（[6.1.1](/6.1.1) 中有作图与回归的例子）。温度范围较宽时必须考虑蒸发焓随温度的变化。由 **Kirchhoff 定律**（[6.3.1](/6.3.1)），在 $\Delta C_{p,\mathrm{m}} = C_{p,\mathrm{m}}(\mathrm{g}) - C_{p,\mathrm{m}}(\mathrm{l})$ 可看作常数的范围内

$$
\Delta_{\mathrm{vap}}H_{\mathrm{m}}(T) = \Delta H_0 + \Delta C_{p,\mathrm{m}}T, \qquad \Delta H_0 = \Delta_{\mathrm{vap}}H_{\mathrm{m}}(T_1) - \Delta C_{p,\mathrm{m}}T_1 ,
$$
代入式 (8.3) 积分：

$$
\ln\frac{p_2}{p_1} = -\frac{\Delta H_0}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) + \frac{\Delta C_{p,\mathrm{m}}}{R}\ln\frac{T_2}{T_1}.
\tag{8.5}
$$
一般地，$\ln p = A - B/T + C\ln T$ 形式的经验式就来自这一积分；蒸气压的精密数据常用 Antoine 方程 $\lg p = A - B/(T + C)$ 拟合。

**例 8.3.1** 水的正常沸点为 $373.12\,\mathrm{K}$，该温度下 $\Delta_{\mathrm{vap}}H_{\mathrm{m}} = 40.65\,\mathrm{kJ\,mol^{-1}}$。估算 $30\,{}^\circ\mathrm{C}$ 时水的饱和蒸气压（实测 $4.247\,\mathrm{kPa}$）。

解：（1）把 $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ 看作常数，由式 (8.4)，

$$
\ln\frac{p_2}{101.325\,\mathrm{kPa}} = -\frac{40650}{8.314}\left(\frac{1}{303.15} - \frac{1}{373.12}\right) = -3.025, \qquad p_2 = 4.92\,\mathrm{kPa},
$$
偏高 16%。原因是低温下蒸发焓更大（$30\,{}^\circ\mathrm{C}$ 时实际为 $43.8\,\mathrm{kJ\,mol^{-1}}$），由沸点向低温外推时用偏小的蒸发焓，蒸气压就降得不够。

（2）取 $C_{p,\mathrm{m}}(\mathrm{H_2O, g}) = 33.6$、$C_{p,\mathrm{m}}(\mathrm{H_2O, l}) = 75.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$，$\Delta C_{p,\mathrm{m}} = -41.7\,\mathrm{J\,mol^{-1}\,K^{-1}}$，由式 (8.5) 得 $p_2 = 4.38\,\mathrm{kPa}$，误差降到 3%。剩下的误差主要来自水蒸气的非理想性与 $\Delta C_{p,\mathrm{m}}$ 随温度的变化。

![Left: vapor pressure of water from 0 to 100 °C on a logarithmic scale, comparing the IAPWS reference curve with Clausius–Clapeyron integrated from the normal boiling point with a constant enthalpy of vaporization and with a temperature-dependent one (Kirchhoff's law). Right: relative errors of the two approximations; the constant-enthalpy form overestimates the pressure by up to 37 % at 0 °C, the Kirchhoff-corrected form by less than 5 %](./plots/clausius-clapeyron-accuracy.py)

许多正常液体（非极性、分子不缔合）在正常沸点的摩尔蒸发熵相近，**Trouton 规则**（[6.1.1](/6.1.1)）给出 $\Delta_{\mathrm{vap}}H_{\mathrm{m}}/T_{\mathrm{b}} \approx 85$–$88\,\mathrm{J\,mol^{-1}\,K^{-1}}$，缺少数据时可以用来估计蒸发焓。它的含义是：在同样的蒸气密度（$1\,\mathrm{atm}$）下，由液体变为气体时分子获得的"位置自由"大致相同；水与醇的氢键使液体更有序，蒸发熵偏大。

把式 (8.3) 中的蒸发焓换成升华焓，就得到固体的蒸气压方程。在**三相点**，冰的升华曲线与水的蒸发曲线压力相同，斜率之比为

$$
\frac{(\mathrm{d}p/\mathrm{d}T)_{\mathrm{sub}}}{(\mathrm{d}p/\mathrm{d}T)_{\mathrm{vap}}} = \frac{\Delta_{\mathrm{sub}}H_{\mathrm{m}}}{\Delta_{\mathrm{vap}}H_{\mathrm{m}}} = \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m}} + \Delta_{\mathrm{vap}}H_{\mathrm{m}}}{\Delta_{\mathrm{vap}}H_{\mathrm{m}}} = \frac{6.01 + 45.05}{45.05} = 1.13,
$$
升华曲线更陡；在线性的 $p$–$T$ 坐标中，两条曲线都向上弯（$\mathrm{d}p/\mathrm{d}T = p\,\Delta H_{\mathrm{m}}/(RT^2)$ 随 $p$ 的增大而增大）。

### 8.3.3. 固–液平衡

熔化时 $\Delta_{\mathrm{fus}}V_{\mathrm{m}}$ 很小，式 (8.2) 给出很大的斜率，熔化曲线几乎是竖直的。若 $\Delta_{\mathrm{fus}}H_{\mathrm{m}}$、$\Delta_{\mathrm{fus}}V_{\mathrm{m}}$ 可看作常数，分离变量积分得

$$
\ln\frac{T_2}{T_1} = \frac{\Delta_{\mathrm{fus}}V_{\mathrm{m}}}{\Delta_{\mathrm{fus}}H_{\mathrm{m}}}(p_2 - p_1),
$$
压力变化不大时近似为 $\Delta T \approx T\,\Delta_{\mathrm{fus}}V_{\mathrm{m}}\,\Delta p/\Delta_{\mathrm{fus}}H_{\mathrm{m}}$。

**例 8.3.2** $0\,{}^\circ\mathrm{C}$ 时冰与水的密度分别为 $0.9167$ 与 $0.99984\,\mathrm{g\,cm^{-3}}$，$\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 6.01\,\mathrm{kJ\,mol^{-1}}$。求冰的熔点随压力的变化率。

解：$\Delta_{\mathrm{fus}}V_{\mathrm{m}} = M(1/\rho_{\mathrm{l}} - 1/\rho_{\mathrm{s}}) = 18.015 \times (1.0002 - 1.0909)\,\mathrm{cm^3\,mol^{-1}} = -1.634\,\mathrm{cm^3\,mol^{-1}}$，

$$
\frac{\mathrm{d}T}{\mathrm{d}p} = \frac{T\,\Delta_{\mathrm{fus}}V_{\mathrm{m}}}{\Delta_{\mathrm{fus}}H_{\mathrm{m}}} = \frac{273.15 \times (-1.634 \times 10^{-6})}{6010}\,\mathrm{K\,Pa^{-1}} = -7.43 \times 10^{-8}\,\mathrm{K\,Pa^{-1}},
$$
即每增加 $1\,\mathrm{MPa}$（约 10 atm），熔点降低约 $0.074\,\mathrm{K}$；反过来，要使熔点降低 $1\,\mathrm{K}$ 需要约 $13.5\,\mathrm{MPa}$。

"冰刀的高压使冰熔化、形成水膜"是流传很广的滑冰解释，但按例 8.3.2 的数字它不成立：体重约 $700\,\mathrm{N}$ 的人站在接触面积约 $1\,\mathrm{cm^2}$ 的冰刀上，压强约 $7\,\mathrm{MPa}$，熔点只降低约 $0.5\,\mathrm{K}$，解释不了 $-20\,{}^\circ\mathrm{C}$ 时冰面仍然很滑。现在认为起主要作用的是冰表面本身：表面上的水分子比体相中少一半氢键，在熔点以下很宽的温度范围内就有一层活动性很强的表面层（表面预熔），滑动时摩擦生热又会加强这一效应。表面层的结构（是否可以称为液膜、厚度多少）仍在研究中，2018–2021 年 Bonn 等人的摩擦与光谱实验表明，润滑来自高度活动的表面分子，而不是加压熔化产生的宏观水膜。

### 8.3.4. 外压对蒸气压的影响

液体上方除自身的蒸气外还有不溶于液体的惰性气体（例如空气）时，液体受到的总压 $p_{\mathrm{e}}$ 大于它的蒸气分压 $p_{\mathrm{v}}$。这时系统含液体与惰性气体两个组分，$C = 2$、$P = 2$，$F = 2$：温度与液体所受的总压都可以独立改变，蒸气压是二者的函数 $p_{\mathrm{v}}(T, p_{\mathrm{e}})$。温度的影响由 Clausius–Clapeyron 方程描述，外压的影响如下。

**定理 8.3.2** 恒温下，液体的饱和蒸气压随液体所受压力的变化满足

$$
\left(\frac{\partial p_{\mathrm{v}}}{\partial p_{\mathrm{e}}}\right)_T = \frac{V_{\mathrm{m}}(\mathrm{l})}{V_{\mathrm{m}}(\mathrm{g})};
$$
蒸气为理想气体、液体不可压缩时，

$$
\ln\frac{p_{\mathrm{v}}}{p_{\mathrm{v}}^*} = \frac{V_{\mathrm{m}}(\mathrm{l})\,(p_{\mathrm{e}} - p_{\mathrm{v}}^*)}{RT},
\tag{8.6}
$$
其中 $p_{\mathrm{v}}^*$ 是液体只受自身蒸气压时的饱和蒸气压。

**证明** 平衡时 $\mu(\mathrm{l}, T, p_{\mathrm{e}}) = \mu(\mathrm{g}, T, p_{\mathrm{v}})$。恒温下改变外压，两边的变化相等：$V_{\mathrm{m}}(\mathrm{l})\,\mathrm{d}p_{\mathrm{e}} = V_{\mathrm{m}}(\mathrm{g})\,\mathrm{d}p_{\mathrm{v}}$，即得第一式。代入 $V_{\mathrm{m}}(\mathrm{g}) = RT/p_{\mathrm{v}}$ 得 $\mathrm{d}\ln p_{\mathrm{v}} = V_{\mathrm{m}}(\mathrm{l})\,\mathrm{d}p_{\mathrm{e}}/(RT)$，由 $p_{\mathrm{e}} = p_{\mathrm{v}}^*$ 积分到 $p_{\mathrm{e}}$ 即得式 (8.6)。$\square$

外压增大，蒸气压增大，但影响很小：因为 $V_{\mathrm{m}}(\mathrm{l}) \ll V_{\mathrm{m}}(\mathrm{g})$。$25\,{}^\circ\mathrm{C}$ 时水的外压增加 $1\,\mathrm{bar}$，蒸气压只增大 $0.07\%$；外压增加 $10\,\mathrm{MPa}$ 时增大约 $7.6\%$。所以通常把有空气存在时液体的蒸气压当作纯液体的饱和蒸气压。式 (8.6) 的形式以后会两次出现：溶液的**渗透压**是在溶液一侧加压、使溶剂的化学势回升到纯溶剂的值（[6.3.5](/6.3.5)）；小液滴的附加压力使其蒸气压高于平面液体，这就是 **Kelvin 方程**（[6.3.19](/6.3.19)）。

## 8.4. 相变的分类

### 8.4.1. 一级相变

两相平衡时化学势相等，但化学势对 $T$、$p$ 的偏导数不一定相等。按 Ehrenfest（1933）的分类，看化学势的哪一阶导数在相变点不连续。

**定义 8.4.1（一级相变）** 在相变点化学势连续、而它的一阶偏导数

$$
\left(\frac{\partial\mu}{\partial T}\right)_p = -S_{\mathrm{m}}, \qquad \left(\frac{\partial\mu}{\partial p}\right)_T = V_{\mathrm{m}}
$$
发生突变的相变称为**一级相变**。一级相变有相变焓 $\Delta_{\mathrm{trs}}H_{\mathrm{m}} = T\,\Delta_{\mathrm{trs}}S_{\mathrm{m}} \neq 0$ 与体积变化 $\Delta_{\mathrm{trs}}V_{\mathrm{m}} \neq 0$，两相平衡线服从 Clapeyron 方程。

熔化、蒸发、升华与多数晶型转变都是一级相变。一级相变点两侧，两相的 $\mu$–$T$ 曲线以不同斜率相交：低于相变温度时一相的化学势较低、较稳定，高于相变温度时另一相较稳定，曲线越过交点后的延长部分对应**过冷**液体或过热液体等亚稳状态。在相变点，热容出现 $\delta$ 函数形式的峰（吸收潜热而温度不变），**差示扫描量热法**（[6.3.1](/6.3.1)）测到的就是这样的峰。

### 8.4.2. 二级相变与 Ehrenfest 方程

**定义 8.4.2（二级相变）** 在相变点化学势及其一阶偏导数都连续（$\Delta_{\mathrm{trs}}S_{\mathrm{m}} = 0$、$\Delta_{\mathrm{trs}}V_{\mathrm{m}} = 0$，没有相变焓），而二阶偏导数

$$
\left(\frac{\partial^2\mu}{\partial T^2}\right)_p = -\frac{C_{p,\mathrm{m}}}{T}, \qquad \left(\frac{\partial^2\mu}{\partial p^2}\right)_T = -V_{\mathrm{m}}\kappa_T, \qquad \frac{\partial^2\mu}{\partial T\,\partial p} = V_{\mathrm{m}}\alpha_V
$$
发生有限突变的相变称为**二级相变**。依此类推，第 $n$ 阶导数首先不连续的称为 $n$ 级相变。

这里 $\alpha_V$ 是**等压热膨胀系数**，$\kappa_T$ 是**等温压缩系数**（[6.3.3](/6.3.3)）。二级相变的平衡线方程不能用 Clapeyron 方程，而要从 $S_{\mathrm{m}}$、$V_{\mathrm{m}}$ 在相变线上连续这一条件出发。

**定理 8.4.1（Ehrenfest 方程）** 沿二级相变线，

$$
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta C_{p,\mathrm{m}}}{TV_{\mathrm{m}}\,\Delta\alpha_V}, \qquad \frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta\alpha_V}{\Delta\kappa_T},
$$
其中 $\Delta$ 表示两相之差。

**证明** 把 $S_{\mathrm{m}}$ 看作 $T$、$p$ 的函数，由 **Maxwell 关系** $(\partial S_{\mathrm{m}}/\partial p)_T = -(\partial V_{\mathrm{m}}/\partial T)_p = -V_{\mathrm{m}}\alpha_V$，

$$
\mathrm{d}S_{\mathrm{m}} = \frac{C_{p,\mathrm{m}}}{T}\,\mathrm{d}T - V_{\mathrm{m}}\alpha_V\,\mathrm{d}p .
$$
沿相变线 $S_{\mathrm{m}}^{\alpha} = S_{\mathrm{m}}^{\beta}$ 始终成立，所以 $\mathrm{d}S_{\mathrm{m}}^{\alpha} = \mathrm{d}S_{\mathrm{m}}^{\beta}$；两相的 $V_{\mathrm{m}}$ 在相变点相同，于是 $\Delta C_{p,\mathrm{m}}\,\mathrm{d}T/T = V_{\mathrm{m}}\,\Delta\alpha_V\,\mathrm{d}p$，即第一式。同样由 $\mathrm{d}V_{\mathrm{m}} = V_{\mathrm{m}}\alpha_V\,\mathrm{d}T - V_{\mathrm{m}}\kappa_T\,\mathrm{d}p$ 与 $\mathrm{d}V_{\mathrm{m}}^{\alpha} = \mathrm{d}V_{\mathrm{m}}^{\beta}$ 得第二式。$\square$

两式也可以看作对 Clapeyron 方程 $\mathrm{d}p/\mathrm{d}T = \Delta S_{\mathrm{m}}/\Delta V_{\mathrm{m}}$ 的 $0/0$ 型用 L'Hôpital 法则的结果：分子与分母同时对 $T$ 求导得第一式，同时对 $p$ 求导得第二式。

### 8.4.3. 连续相变

符合 Ehrenfest 意义的二级相变的典型例子是零磁场下金属的**超导电性**转变（[5.3.9](/5.3.9#sec-9.7)）：在临界温度处电阻消失，熵连续，热容有一个有限的跃变，与 BCS 理论的预言一致。

但更多的这类相变并不符合 Ehrenfest 的图像。液氦（$^4\mathrm{He}$）在 $2.17\,\mathrm{K}$ 由普通液体 He I 转变为超流体 He II，没有相变焓，热容曲线却在转变点两侧对数发散，形状像希腊字母 $\lambda$，称为 λ 相变；铁磁质在 **Curie 温度**（[5.3.8](/5.3.8#sec-8.5.4)）失去自发磁化、合金（如 $\beta$ 黄铜 CuZn）的有序–无序转变、某些**液晶**的相变（如近晶 A 相–向列相）也属于这一类。热容发散时"二阶导数有限突变"的说法不再适用，所以现代文献不再使用 Ehrenfest 的高级分类，而只分为一级相变与连续相变（广义的**二级相变**）：前者有潜热、两相共存；后者没有潜热，一个描述有序程度的量（序参量，如自发磁化强度、超流组分的比例）在转变点连续地降为零，转变点附近的涨落很大，各种性质按幂律变化（临界现象）。气–液临界点就是一个连续相变点：到临界点时蒸发焓与 $\Delta V_{\mathrm{m}}$ 同时趋于零。临界现象的统一理论（Landau 理论与重整化群）属于统计物理。

![Schematic molar Gibbs energy (chemical potential), molar entropy and heat capacity against temperature at constant pressure for a first-order transition (kinked μ, entropy jump equal to the enthalpy of transition divided by T, delta-function peak in Cp), an Ehrenfest second-order transition (continuous μ and S, finite jump in Cp) and a lambda transition (Cp diverges on both sides)](./plots/transition-order.py)

生物膜中的磷脂双分子层在升温时由排列整齐的凝胶相转变为烃链无序的液晶相（主相变，二棕榈酰磷脂酰胆碱 DPPC 约 $41\,{}^\circ\mathrm{C}$），这是一个较弱的一级相变，用差示扫描量热法测到的尖锐吸热峰说明转变是高度协同的；细胞通过调节脂肪酸链的长度与不饱和度，使膜在生理温度下保持流动性（[7.6](/7.6)）。

## 8.5. 单组分系统的相图

单组分系统 $C = 1$，$F = 3 - P$：$P$ 最小为 1，所以 $F \leq 2$，用 $p$、$T$ 两个变量就能完整地画出相平衡关系，**相图**是一张平面图；$F \geq 0$ 给出 $P \leq 3$，单组分系统最多三相共存。

| 相数 | 自由度数 | 在 $p$–$T$ 图上 |
|---|---|---|
| $P = 1$ | $F = 2$ | 面（单相区） |
| $P = 2$ | $F = 1$ | 线（两相平衡线，方程是 Clapeyron 方程） |
| $P = 3$ | $F = 0$ | 点（三相点） |

### 8.5.1. 水的相图

中压、低压范围内水的相图由三条线把平面分成冰、液态水、水蒸气三个单相区：

- 蒸发曲线（液–气平衡线）：水的**饱和蒸气压**曲线，由三相点向上延伸，终止于临界点 $647.096\,\mathrm{K}$、$22.064\,\mathrm{MPa}$（IAPWS-95）。在临界点处液、气的差别消失，曲线不能再延长。
- 升华曲线（固–气平衡线）：冰的饱和蒸气压曲线，在三相点附近比蒸发曲线陡（§8.3.2）。
- 熔化曲线（固–液平衡线）：斜率为负、几乎竖直（例 8.3.2），压力升高时冰的熔点降低。冰 Ih 的熔点最低降到 $251.165\,\mathrm{K}$（$208.6\,\mathrm{MPa}$），此后与冰 III 相遇。
- 蒸发曲线越过三相点向低温的延长线是过冷水的饱和蒸气压曲线。它高于同温下冰的升华曲线：同一温度下过冷水的蒸气压比冰高，化学势也比冰高，所以过冷水是亚稳的，一旦有晶核就会结冰。

![Phase diagram of water on a logarithmic pressure axis computed from the IAPWS correlations: sublimation, vaporization (ending at the critical point 647.096 K, 22.064 MPa) and melting curves; the melting curve of ordinary ice Ih is almost vertical with a negative slope, and at high pressure the melting curves of ices III, V, VI and VII follow (boundaries between the solid phases are omitted). The dashed line is the vapor pressure of supercooled water](./plots/water-phase-diagram.py)

相图的用途是：给定条件，读出系统处于哪一相；条件改变时，预测相态的变化。例如在 $p^\circ$ 下由 $-10\,{}^\circ\mathrm{C}$ 等压加热，物系点沿水平线依次越过熔化线（$0\,{}^\circ\mathrm{C}$，冰与水两相共存，$F^* = 0$，温度不变直到冰全部熔化）与蒸发线（$99.61\,{}^\circ\mathrm{C}$，水与水蒸气共存）。在低于三相点的压力下加热冰，物系点只越过升华线，冰不经熔化直接变成水蒸气，所以冰升华的必要条件是压力低于三相点压力 $611.657\,\mathrm{Pa}$。冷冻干燥正是利用这一点：把含水的样品冷冻后在低于三相点的压力下使冰升华，样品不经过液态，蛋白质、疫苗、细菌菌种与食品的结构与活性得以保存。

### 8.5.2. 三相点与冰点

水的三相点是冰、水、水蒸气三相共存的唯一状态，$C = 1$、$P = 3$、$F = 0$：$273.16\,\mathrm{K}$、$611.657\,\mathrm{Pa}$。它是纯水本身的性质，不随外界条件改变，因此从 1954 年起被用来定义热力学温标（规定为 $273.16\,\mathrm{K}$ 整）。1938 年 Beattie、黄子卿与 Benedict 的精密测定（三相点比冰点高 $0.00981\,{}^\circ\mathrm{C}$）是这一选择的依据之一。2019 年 SI 修订以后，kelvin 由固定的 **Boltzmann 常量** $k_{\mathrm{B}}$ 定义（[5.2.1](/5.2.1)），三相点温度成为测量值，在现有精度内仍是 $273.16\,\mathrm{K}$。

冰点是在 $101.325\,\mathrm{kPa}$ 的空气中、被空气饱和的水与冰平衡共存的温度，$273.15\,\mathrm{K}$，比三相点低约 $0.0098\,\mathrm{K}$。这时系统含有水与空气两个组分，$C = 2$、$P = 3$（冰、溶有空气的水、湿空气），$F = 1$，指定压力后 $F^* = 0$：冰点随压力而变。二者之差由两个原因造成：

1. 压力由 $611.657\,\mathrm{Pa}$ 增大到 $101.325\,\mathrm{kPa}$，按例 8.3.2 熔点降低 $7.43 \times 10^{-8}\,\mathrm{K\,Pa^{-1}} \times 1.007 \times 10^{5}\,\mathrm{Pa} = 0.0075\,\mathrm{K}$；
2. 水中溶有空气（$0\,{}^\circ\mathrm{C}$ 时约 $1.3\,\mathrm{mmol\,kg^{-1}}$），按稀溶液的**凝固点降低**（[6.3.5](/6.3.5)），熔点再降低约 $1.86 \times 0.0013\,\mathrm{K} = 0.0024\,\mathrm{K}$。

### 8.5.3. 高压下的冰

压力高于约 $200\,\mathrm{MPa}$ 时，普通的六方冰 Ih 不再稳定，氢键网络被压成更致密的结构。至今已确认的冰的晶相约有 20 种（冰 Ih、Ic 与冰 II 至冰 XIX 等），其中与液态水接触、出现在熔化曲线上的有冰 Ih、III、V、VI、VII。高压冰相的熔化曲线斜率为正（它们的密度都比液态水大）：冰 VI 在约 $1\,\mathrm{GPa}$ 时于室温熔化，冰 VII 在 $10\,\mathrm{GPa}$ 时要到约 $600\,\mathrm{K}$ 才熔化，所以"热冰"是存在的。木卫三、土卫六等冰卫星的深处与一些系外行星的内部被认为存在这些高压冰相。

### 8.5.4. CO₂ 与超临界流体

$\ce{CO2}$ 的相图（[6.1.1](/6.1.1) 中有图）与水的形状相似，但熔化曲线斜率为正，而且三相点压力 $518\,\mathrm{kPa}$ 高于大气压：常压下干冰在 $194.7\,\mathrm{K}$ 直接升华，液态 $\ce{CO2}$ 只能在加压下存在（钢瓶中的 $\ce{CO2}$ 室温下是液体）。$\ce{CO2}$ 的临界点为 $304.13\,\mathrm{K}$、$7.377\,\mathrm{MPa}$。

在临界温度以上无论加多大的压力气体都不能液化，温度、压力都高于临界值的状态是**超临界流体**（[6.1.1](/6.1.1)）。超临界流体的密度接近液体，溶解能力强；黏度接近气体，扩散系数约为液体的 10 倍，传质快；在临界点附近（等温压缩系数很大），压力或温度的微小变化就能使密度与溶解能力大幅改变，因而可以通过调压来"开关"溶解能力。主要应用：

- 超临界 $\ce{CO2}$ 萃取：$\ce{CO2}$ 的临界温度接近室温，无毒、不燃、不残留。从咖啡豆中脱除咖啡因（约 $70$–$90\,{}^\circ\mathrm{C}$、$16$–$20\,\mathrm{MPa}$，咖啡因含量由约 3% 降到 0.02% 左右），从啤酒花、植物中提取香料与药物成分，降压后溶质自动析出。
- 超临界水氧化：超临界水（$400$–$600\,{}^\circ\mathrm{C}$、$25$–$40\,\mathrm{MPa}$）的介电常数很小，能与有机物和氧气完全互溶，有机废物在一分钟左右被氧化成 $\ce{CO2}$ 与水，去除率高于 99.99%，反应放热可以自持；与焚烧相比温度低得多，不产生二噁英与氮氧化物。
- 超临界流体色谱、超临界干燥（制备气凝胶，避免液体蒸发时表面张力压垮多孔结构）与超临界条件下的聚合反应。

## 小结

| 内容 | 要点 |
|---|---|
| 相平衡条件 | 每种物质在它所存在的各相中化学势相等 |
| 组分数 | $C = s - r - r'$；浓度限制条件必须是同一相内的关系，分配定律与不同相物质的量相等都不算 |
| 相律 | $F = C - P + 2$；恒压或恒温时 $F^* = C - P + 1$；广义 $F = C - P + n$；$P_{\max} = C + 2$ |
| Clapeyron 方程 | $\mathrm{d}p/\mathrm{d}T = \Delta_{\mathrm{trs}}H_{\mathrm{m}}/(T\,\Delta_{\mathrm{trs}}V_{\mathrm{m}})$，严格，适用于纯物质的任意一级相变 |
| Clausius–Clapeyron 方程 | 忽略凝聚相体积、蒸气理想：$\mathrm{d}\ln p/\mathrm{d}T = \Delta_{\mathrm{vap}}H_{\mathrm{m}}/(RT^2)$；宽温度范围用 Kirchhoff 定律修正 |
| 外压与蒸气压 | $\ln(p_{\mathrm{v}}/p_{\mathrm{v}}^*) = V_{\mathrm{m}}(\mathrm{l})(p_{\mathrm{e}} - p_{\mathrm{v}}^*)/(RT)$，影响很小 |
| 相变分类 | 一级：$S$、$V$ 突变，有潜热；二级：$C_p$、$\alpha_V$、$\kappa_T$ 有限跃变，Ehrenfest 方程；现代分为一级与连续相变 |
| 水的相图 | 三相点 $273.16\,\mathrm{K}$、$611.657\,\mathrm{Pa}$；冰点 $273.15\,\mathrm{K}$；临界点 $647.096\,\mathrm{K}$、$22.064\,\mathrm{MPa}$；熔化线斜率为负 |
