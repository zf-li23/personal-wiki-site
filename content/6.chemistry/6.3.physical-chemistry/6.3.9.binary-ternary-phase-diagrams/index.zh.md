---
title: 二组分与三组分系统的相图
description: 二组分系统的相律分析；理想液态混合物的 p–x 与 T–x 图、物系点与相点、杠杆规则与精馏；非理想系统与恒沸物，Duhem–Margules 方程与 Konovalov 规则；部分互溶的液–液平衡、会溶温度与正规溶液的相分离，完全不互溶系统与水蒸气蒸馏；热分析与步冷曲线，简单低共熔系统与理想溶解度方程，水–盐系统，稳定与不稳定化合物，固溶体与区域熔炼；七类基本相图与复杂相图的读法，Fe–C 相图；三组分系统的等边三角形坐标与萃取。
---

上一章用相律与 Clapeyron 方程处理了单组分系统。本章转向二组分系统，这是相平衡在化工、冶金、材料与制药中用得最多的部分：蒸馏与精馏、萃取、结晶提纯、合金设计都以相图为依据。二组分系统的相图可以由前几章的溶液热力学算出来——理想系统用 **Raoult 定律**（[6.3.5](/6.3.5)），非理想系统用**活度因子**与**正规溶液**模型（[6.3.6](/6.3.6)），固–液平衡用与**凝固点降低**同一个公式——本章的图都是这样用 Python 计算出来的；但对真实的复杂系统，相图主要靠实验测定，这时要学会读图。本章依次讨论气–液、液–液、固–液三类平衡，然后总结读复杂相图的规律，最后简单介绍三组分系统的三角坐标与萃取。

## 9.1. 理想液态混合物的气–液平衡

### 9.1.1. 二组分系统的相律分析

二组分系统 $C = 2$，由**相律**（[6.3.8](/6.3.8)）$F = 4 - P$。$P = 1$ 时 $F = 3$，需要 $T$、$p$ 与一个组成变量三个坐标，完整的相图是立体图；$F = 0$ 时 $P = 4$，最多四相共存。为了用平面图表示，固定一个变量，用**条件自由度** $F^* = 3 - P$：

| 固定的变量 | 平面图 | 用途 |
|---|---|---|
| 温度 | $p$–$x$ 图（蒸气压–组成图） | 与 Raoult 定律直接对应，便于理论分析 |
| 压力 | $T$–$x$ 图（沸点–组成图、熔点–组成图） | 蒸馏、结晶在恒压下进行，用得最多 |
| 组成 | $p$–$T$ 图 | 用得最少 |

平面图上单相区 $F^* = 2$，两相区 $F^* = 1$，三相共存时 $F^* = 0$（一条水平线）。

### 9.1.2. p–x 图

设 A、B 形成**理想液态混合物**，蒸气为理想气体。由 Raoult 定律，温度一定时

$$
p_{\mathrm{A}} = p_{\mathrm{A}}^*x_{\mathrm{A}}, \qquad p_{\mathrm{B}} = p_{\mathrm{B}}^*x_{\mathrm{B}}, \qquad p = p_{\mathrm{A}} + p_{\mathrm{B}} = p_{\mathrm{A}}^* + (p_{\mathrm{B}}^* - p_{\mathrm{A}}^*)\,x_{\mathrm{B}},
\tag{9.1}
$$
其中 $x$ 表示液相组成，$p_{\mathrm{A}}^*$、$p_{\mathrm{B}}^*$ 是纯液体的**饱和蒸气压**。总压与液相组成成直线关系，这条直线称为液相线。与之平衡的气相组成 $y_{\mathrm{B}}$ 由 Dalton 分压定律给出：

$$
y_{\mathrm{B}} = \frac{p_{\mathrm{B}}}{p} = \frac{p_{\mathrm{B}}^*x_{\mathrm{B}}}{p}, \qquad \frac{y_{\mathrm{B}}}{y_{\mathrm{A}}} = \frac{p_{\mathrm{B}}^*}{p_{\mathrm{A}}^*}\cdot\frac{x_{\mathrm{B}}}{x_{\mathrm{A}}}.
$$
若 $p_{\mathrm{B}}^* > p_{\mathrm{A}}^*$（B 是易挥发组分），则 $y_{\mathrm{B}}/y_{\mathrm{A}} > x_{\mathrm{B}}/x_{\mathrm{A}}$，即 $y_{\mathrm{B}} > x_{\mathrm{B}}$：易挥发组分在气相中的含量大于它在液相中的含量，这是一切蒸馏分离的基础。由上式解出 $x$ 代入式 (9.1)，得总压与气相组成的关系

$$
\frac{1}{p} = \frac{y_{\mathrm{A}}}{p_{\mathrm{A}}^*} + \frac{y_{\mathrm{B}}}{p_{\mathrm{B}}^*},
$$
它是一条位于液相线下方的曲线，称为气相线。液相线以上为液相区，气相线以下为气相区，两线之间为气–液两相区。

### 9.1.3. T–x 图、物系点与相点

恒压下的 $T$–$x$ 图可以由实验测定（测不同组成的溶液的沸点与沸腾时气、液两相的组成），也可以由 $p$–$x$ 关系计算：对每个液相组成，求总压等于外压 $p$ 时的温度。苯–甲苯是接近理想的系统，下图用 Antoine 方程与 Raoult 定律算出了它的两种相图。$T$–$x$ 图中，易挥发组分沸点低，液相线（沸点线）在下、气相线（露点线）在上，两条线都是曲线；两相区之上为气相区、之下为液相区，与 $p$–$x$ 图上下颠倒。

![Benzene–toluene computed from Raoult's law with Antoine vapor pressures. Left: p–x diagram at 90 °C; the liquid line is straight and lies above the vapor line, and the dashed lines are the partial pressures. Right: T–x diagram at 101.325 kPa; the boiling-point (bubble) line lies below the dew-point line. The tie line a–O–b at 95 °C joins the liquid and vapor compositions in equilibrium with the system point O (overall benzene mole fraction 0.5)](./plots/benzene-toluene.py)

**定义 9.1.1** 相图中表示系统总组成（与温度、压力）的点称为**物系点**，表示某一相的组成的点称为**相点**。单相区中物系点与相点重合；在两相区中，物系点落在连接两个相点的水平线上，这条连接平衡两相相点的线称为连结线（tie line）。

恒压下加热组成为 $X_{\mathrm{B}}$ 的液体，物系点沿竖直线上升。到达液相线时开始沸腾，这个温度称为该液体的泡点（bubble point）；继续升温，液相中易挥发组分 B 减少，液相点沿液相线向 A 一侧移动、沸点不断升高，气相点沿气相线移动；到达气相线时最后一滴液体蒸发完，这个温度对于组成为 $X_{\mathrm{B}}$ 的气体称为露点（dew point）。两相区中 $F^* = 1$：温度一定，两相的组成都随之确定，只有两相的数量随物系点变化。

### 9.1.4. 杠杆规则

**定理 9.1.1（杠杆规则）** 组成为 $X_{\mathrm{B}}$、总物质的量为 $n$ 的系统分成组成为 $x_{\mathrm{B}}$、$y_{\mathrm{B}}$ 的两相，两相的物质的量 $n_{\mathrm{l}}$、$n_{\mathrm{g}}$ 满足

$$
n_{\mathrm{l}}\,(X_{\mathrm{B}} - x_{\mathrm{B}}) = n_{\mathrm{g}}\,(y_{\mathrm{B}} - X_{\mathrm{B}}), \qquad \text{即} \qquad \frac{n_{\mathrm{l}}}{n_{\mathrm{g}}} = \frac{\overline{\mathrm{Ob}}}{\overline{\mathrm{aO}}},
$$
其中 O、a、b 分别是物系点与两个相点，$\overline{\mathrm{aO}}$、$\overline{\mathrm{Ob}}$ 是连结线上的线段长度。

**证明** B 的物质的量守恒：$nX_{\mathrm{B}} = n_{\mathrm{l}}x_{\mathrm{B}} + n_{\mathrm{g}}y_{\mathrm{B}}$；总物质的量守恒：$n = n_{\mathrm{l}} + n_{\mathrm{g}}$。把第二式乘以 $X_{\mathrm{B}}$ 减去第一式即得。$\square$

两相的数量与它们的相点到物系点的距离成反比，就像以物系点为支点的杠杆。杠杆规则只是质量守恒，所以适用于任何相图的任何两相区（液–液、固–液、三组分相图中的连结线）；横坐标用质量分数时，式中换成两相的质量。

**例 9.1.1** A、B 形成理想液态混合物，纯 A 与纯 B 的沸点分别为 $393\,\mathrm{K}$ 与 $358\,\mathrm{K}$；$p^\circ$ 下组成 $x_{\mathrm{B}} = 0.4$ 的溶液在 $373\,\mathrm{K}$ 沸腾，气相组成 $y_{\mathrm{B}} = 0.8$。在 $373\,\mathrm{K}$、$p^\circ$ 下把 $90\,\mathrm{mol}$ B 的蒸气缓慢通入 $10\,\mathrm{mol}$ 液态 A 中，说明系统状态的变化。

**解** 温度与压力都不变，物系点沿 $373\,\mathrm{K}$ 的水平线由 $X_{\mathrm{B}} = 0$ 向 $X_{\mathrm{B}} = 90/100 = 0.9$ 移动。

1. $0 < X_{\mathrm{B}} < 0.4$：$373\,\mathrm{K}$ 低于这些溶液的沸点，通入的 B 全部溶入液相（放出凝结热，由恒温器移走），系统只有液相。
2. $X_{\mathrm{B}} = 0.4$（共通入 $6.67\,\mathrm{mol}$ B）：液相到达泡点，开始产生组成 $y_{\mathrm{B}} = 0.8$ 的气相。
3. $0.4 < X_{\mathrm{B}} < 0.8$：气、液两相共存，组成分别固定为 0.8 与 0.4，数量由杠杆规则确定。例如 $X_{\mathrm{B}} = 0.6$（共 $25\,\mathrm{mol}$）时，$n_{\mathrm{l}}(0.6 - 0.4) = n_{\mathrm{g}}(0.8 - 0.6)$，两相各 $12.5\,\mathrm{mol}$。
4. $X_{\mathrm{B}} = 0.8$（共通入 $40\,\mathrm{mol}$ B）：液相消失；此后到 $X_{\mathrm{B}} = 0.9$ 都只有气相。最终得到 $100\,\mathrm{mol}$ 组成 $y_{\mathrm{B}} = 0.9$ 的混合蒸气。

### 9.1.5. 精馏

一次部分汽化得到的气相只比液相略富含易挥发组分。把气相部分冷凝、液相部分汽化反复进行多次，就能把两组分分开，这称为精馏（fractional distillation）。在 $T$–$x$ 图上，每一次"汽化–冷凝"相当于在两相区中画一条水平连结线再竖直移到相界：气相一步步趋向纯 B（塔顶），液相一步步趋向纯 A（塔釜）。

精馏塔把这一过程连续化：塔釜加热，蒸气沿塔上升；塔顶的冷凝液一部分回流，沿塔下降；在每一层塔板上，上升的蒸气与下降的液体接触并趋于平衡，相当于一次部分汽化与部分冷凝。达到一次气–液平衡的分离效果称为一块理论塔板；两组分挥发性越接近（$p_{\mathrm{B}}^*/p_{\mathrm{A}}^*$ 越接近 1），所需理论塔板数越多。石油炼制、液态空气分离制取 $\ce{O2}$ 与 $\ce{N2}$、同位素（如 $\ce{D2O}$）的富集都靠精馏。

## 9.2. 非理想液态混合物的气–液平衡

### 9.2.1. 偏差不大的系统

真实混合物对 Raoult 定律有正偏差（$p_{\mathrm{B}} > p_{\mathrm{B}}^*x_{\mathrm{B}}$，活度因子 $\gamma > 1$，A–B 之间的吸引比 A–A、B–B 弱，如 $\ce{CH3OH}$–$\ce{H2O}$、$\ce{CCl4}$–$\ce{C6H6}$）或负偏差（$\gamma < 1$，A–B 之间有氢键等较强的作用，如 $\ce{CHCl3}$–丙酮）。偏差不大时，总压仍在 $p_{\mathrm{A}}^*$ 与 $p_{\mathrm{B}}^*$ 之间，液相线只是略向上凸或向下凹，$T$–$x$ 图的形状与理想系统相似，同样可以用精馏分离。

### 9.2.2. 恒沸物

正偏差很大时，$p$–$x$ 图上的总压出现最高点，相应地 $T$–$x$ 图上出现最低点；负偏差很大时，$p$–$x$ 图上有最低点，$T$–$x$ 图上有最高点。在这样的极值点处，液相线与气相线相切。

**定义 9.2.1（恒沸物）** 在恒压的 $T$–$x$ 图中，气–液两相组成相同的极值点称为恒沸点（最低恒沸点或最高恒沸点），组成在恒沸点的液态混合物称为**恒沸物**。

恒沸物的特点：

1. 沸腾时气、液两相组成相同，$x_{\mathrm{B}} = y_{\mathrm{B}}$（定理 9.2.2 将证明这一点），所以它像纯物质一样在恒定温度下沸腾，馏出物的组成不变。
2. 它是混合物而不是化合物：改变压力，恒沸点的温度与组成都随之改变。由相律，恒压下两相共存 $F^* = 1$，恒沸条件 $x_{\mathrm{B}} = y_{\mathrm{B}}$ 再给出一个关系，于是 $F^* = 0$：一定压力下恒沸物的组成与沸点都是确定的。
3. 具有恒沸物的系统，用普通精馏不能同时得到两种纯组分。这类相图可以看作两张"偏差不大"的相图在恒沸点处拼接而成：对最低恒沸系统，塔顶得到恒沸物，塔釜得到原料所在那一侧的纯组分。

![T–x–y diagrams at 101.325 kPa computed from Raoult's law with activity coefficients. Left: ethanol + water (van Laar model), with a minimum-boiling azeotrope at x(ethanol) ≈ 0.92, 78.2 °C (measured: 0.894, 78.15 °C). Right: acetone + chloroform (one-parameter Margules model), with a maximum-boiling azeotrope at x(acetone) ≈ 0.38, 64.3 °C](./plots/azeotropes.py)

| 系统（$101.325\,\mathrm{kPa}$） | 类型 | 恒沸点 | 恒沸组成 |
|---|---|---|---|
| 乙醇–水 | 最低恒沸点 | $78.15\,{}^\circ\mathrm{C}$ | 乙醇的质量分数 95.6%（$x = 0.894$） |
| 丙酮–氯仿 | 最高恒沸点 | $64.5\,{}^\circ\mathrm{C}$ | $x(\text{丙酮}) \approx 0.38$ |
| $\ce{HCl}$–水 | 最高恒沸点 | $108.6\,{}^\circ\mathrm{C}$ | $\ce{HCl}$ 的质量分数 20.2% |
| $\ce{HNO3}$–水 | 最高恒沸点 | $120.5\,{}^\circ\mathrm{C}$ | $\ce{HNO3}$ 的质量分数 68% |

乙醇–水的恒沸组成随压力变化：$17.3\,\mathrm{kPa}$ 时乙醇的质量分数为 98.7%，$193.5\,\mathrm{kPa}$ 时为 95.25%；压力足够低时恒沸点消失。质量分数 50% 的乙醇溶液精馏，塔顶得到 95.6% 的恒沸乙醇，塔釜得到水。制取无水乙醇要打破恒沸：加入苯或环己烷作夹带剂进行恒沸精馏（生成新的三元最低恒沸物把水带出），利用恒沸组成随压力的变化进行变压精馏，或者用分子筛选择性地吸附水。恒沸盐酸的组成在一定压力下精确确定、不随蒸馏改变，曾被用作酸碱滴定的基准物质。

### 9.2.3. Duhem–Margules 方程与 Konovalov 规则

为什么极值点处气、液组成必然相同？答案来自 **Gibbs–Duhem 方程**（[6.3.4](/6.3.4)）对两组分蒸气压的约束。

**定理 9.2.1（Duhem–Margules 方程）** 在恒温下，与二组分液态混合物平衡的理想蒸气中（忽略总压变化对液相化学势的影响，即略去 $V_{\mathrm{m}}\,\mathrm{d}p$ 项），两组分的分压满足

$$
x_{\mathrm{A}}\,\mathrm{d}\ln p_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln p_{\mathrm{B}} = 0, \qquad \text{即} \qquad \left(\frac{\partial\ln p_{\mathrm{A}}}{\partial\ln x_{\mathrm{A}}}\right)_T = \left(\frac{\partial\ln p_{\mathrm{B}}}{\partial\ln x_{\mathrm{B}}}\right)_T.
\tag{9.2}
$$

**证明** 等温等压下液相的 Gibbs–Duhem 方程为 $x_{\mathrm{A}}\,\mathrm{d}\mu_{\mathrm{A}}(\mathrm{l}) + x_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}}(\mathrm{l}) = 0$。气–液平衡时 $\mu_{\mathrm{B}}(\mathrm{l}) = \mu_{\mathrm{B}}(\mathrm{g}) = \mu_{\mathrm{B}}^\circ(\mathrm{g}) + RT\ln(p_{\mathrm{B}}/p^\circ)$，所以 $\mathrm{d}\mu_{\mathrm{B}}(\mathrm{l}) = RT\,\mathrm{d}\ln p_{\mathrm{B}}$，A 同理，代入即得第一式；两边除以 $\mathrm{d}x_{\mathrm{A}} = -\mathrm{d}x_{\mathrm{B}}$ 并利用 $x\,\mathrm{d}\ln p/\mathrm{d}x = \mathrm{d}\ln p/\mathrm{d}\ln x$ 得第二式。严格地说，组成改变时与液相平衡的总压也在变，Gibbs–Duhem 方程中还应有 $V_{\mathrm{m}}\,\mathrm{d}p$ 项；液体的摩尔体积很小，这一项可以忽略。$\square$

由式 (9.2) 可以得到三个结论：

1. $\left(\partial p_{\mathrm{A}}/\partial p_{\mathrm{B}}\right)_T = -x_{\mathrm{B}}p_{\mathrm{A}}/(x_{\mathrm{A}}p_{\mathrm{B}}) < 0$：一个组分的分压随组成增大时，另一个组分的分压必然减小。
2. 若在某一浓度范围内溶剂 A 服从 Raoult 定律，$p_{\mathrm{A}} = p_{\mathrm{A}}^*x_{\mathrm{A}}$，则左边为 1，$\mathrm{d}\ln p_{\mathrm{B}} = \mathrm{d}\ln x_{\mathrm{B}}$，积分得 $p_{\mathrm{B}} = k_{x,\mathrm{B}}x_{\mathrm{B}}$：在同一浓度范围内溶质必然服从 **Henry 定律**。这是 [6.3.5](/6.3.5) 中理想稀溶液的两条定律互相一致的热力学证明。
3. 由分压之间的这一约束，可以得到总压与两相组成的关系：

**定理 9.2.2（Konovalov 规则）** 恒温下，二组分系统的总蒸气压与气相组成满足

$$
\left(\frac{\partial\ln p}{\partial y_{\mathrm{A}}}\right)_T = \frac{y_{\mathrm{A}} - x_{\mathrm{A}}}{y_{\mathrm{A}}(1 - y_{\mathrm{A}})}.
\tag{9.3}
$$
由此：（1）第一规则：$p$–$x$ 图上总压的极大或极小点（恒压下即 $T$–$x$ 图上的极小或极大点）处，$y_{\mathrm{A}} = x_{\mathrm{A}}$，即两相组成相同；（2）第二规则：若在气相中增加 A 使总蒸气压升高（恒压下使沸点降低），则气相中 A 的含量大于液相中的，$y_{\mathrm{A}} > x_{\mathrm{A}}$；反之亦然。

**证明** 把 $p_{\mathrm{A}} = y_{\mathrm{A}}p$、$p_{\mathrm{B}} = y_{\mathrm{B}}p$ 代入式 (9.2)：

$$
(x_{\mathrm{A}} + x_{\mathrm{B}})\,\mathrm{d}\ln p + x_{\mathrm{A}}\frac{\mathrm{d}y_{\mathrm{A}}}{y_{\mathrm{A}}} + x_{\mathrm{B}}\frac{\mathrm{d}y_{\mathrm{B}}}{y_{\mathrm{B}}} = 0 .
$$
利用 $x_{\mathrm{A}} + x_{\mathrm{B}} = 1$、$\mathrm{d}y_{\mathrm{B}} = -\mathrm{d}y_{\mathrm{A}}$，

$$
\mathrm{d}\ln p = -\left(\frac{x_{\mathrm{A}}}{y_{\mathrm{A}}} - \frac{x_{\mathrm{B}}}{y_{\mathrm{B}}}\right)\mathrm{d}y_{\mathrm{A}} = \frac{x_{\mathrm{B}}y_{\mathrm{A}} - x_{\mathrm{A}}y_{\mathrm{B}}}{y_{\mathrm{A}}y_{\mathrm{B}}}\,\mathrm{d}y_{\mathrm{A}},
$$
而 $x_{\mathrm{B}}y_{\mathrm{A}} - x_{\mathrm{A}}y_{\mathrm{B}} = (1 - x_{\mathrm{A}})y_{\mathrm{A}} - x_{\mathrm{A}}(1 - y_{\mathrm{A}}) = y_{\mathrm{A}} - x_{\mathrm{A}}$，即得式 (9.3)。$0 < y_{\mathrm{A}} < 1$ 时分母为正，所以导数为零当且仅当 $y_{\mathrm{A}} = x_{\mathrm{A}}$，导数的符号与 $y_{\mathrm{A}} - x_{\mathrm{A}}$ 相同。$\square$

第二规则正是 §9.1.2 中"易挥发组分在气相中富集"的一般形式：它对任何非理想系统都成立，不需要 Raoult 定律。

## 9.3. 液–液平衡

### 9.3.1. 部分互溶与会溶温度

两种液体的正偏差足够大时，在一定组成范围内不能完全互溶。例如 $20\,{}^\circ\mathrm{C}$、$p^\circ$ 下向水中滴加异丁醇：异丁醇的质量分数小于 8.5% 时得到均匀的溶液；超过 8.5% 后分成两层，一层是异丁醇的水溶液（8.5%），另一层是水的异丁醇溶液（83.6%），继续加入异丁醇只改变两层的相对数量；超过 83.6% 后又成为一相。两层共存时 $C = 2$、$P = 2$，等温等压下 $F^* = 0$，两层的组成都是确定的。

**定义 9.3.1（共轭溶液）** 两种液体部分互溶时，平衡共存的两个组成不同的液层称为**共轭溶液**。升高（或降低）温度时，两个液层的组成逐渐接近，在某一温度下合为一相，这个温度称为**会溶温度**（临界溶解温度）。

恒压下的溶解度图（$T$–$x$ 图）中，两条溶解度曲线围成"帽形"的两相区，帽顶就是会溶点。会溶温度的高低反映两种液体相互溶解能力的强弱。实际系统大致分为以下几种类型：

| 类型 | 例子 | 会溶温度 |
|---|---|---|
| 有最高会溶温度：升温时互溶度增大 | 水–苯胺；水–苯酚；水–异丁醇 | 水–苯胺约 $167\,{}^\circ\mathrm{C}$，水–苯酚约 $66\,{}^\circ\mathrm{C}$ |
| 有最低会溶温度：降温时互溶度增大 | 水–三乙胺 | 约 $18.5\,{}^\circ\mathrm{C}$ |
| 同时有最高与最低会溶温度（封闭的环形两相区） | 水–烟碱 | 约 $61\,{}^\circ\mathrm{C}$ 与 $210\,{}^\circ\mathrm{C}$ |
| 在液态范围内没有会溶温度 | 水–乙醚 | — |

最低会溶温度通常出现在两种分子之间有氢键的系统：低温下 A–B 氢键使混合放热（$H^{\mathrm{E}} < 0$）、二者互溶；但氢键同时使分子的相对取向受到限制，混合熵小于理想值（$S^{\mathrm{E}} < 0$），升温时 $-TS^{\mathrm{E}}$ 项占优，又发生分相。

### 9.3.2. 正规溶液的相分离

部分互溶可以用 [6.3.6](/6.3.6) 的正规溶液模型定量理解。设**超额 Gibbs 自由能** $G^{\mathrm{E}}_{\mathrm{m}} = Wx_{\mathrm{A}}x_{\mathrm{B}}$（$W$ 与温度无关，$S^{\mathrm{E}} = 0$），则

$$
\frac{\Delta_{\mathrm{mix}}G_{\mathrm{m}}}{RT} = x\ln x + (1 - x)\ln(1 - x) + \frac{W}{RT}\,x(1 - x), \qquad x = x_{\mathrm{B}} .
$$
等温等压下系统处于 Gibbs 自由能最低的状态。若 $\Delta_{\mathrm{mix}}G_{\mathrm{m}}(x)$ 曲线有一段向上凸，均匀溶液分成两相可以降低 Gibbs 自由能：两相的组成由曲线的公切线的两个切点给出——公切线意味着两相中 $\mathrm{d}G/\mathrm{d}x$ 相同、截距相同，也就是 A 与 B 在两相中的**化学势**分别相等。

曲线的凸凹由二阶导数决定：

$$
\frac{1}{RT}\frac{\partial^2\Delta_{\mathrm{mix}}G_{\mathrm{m}}}{\partial x^2} = \frac{1}{x(1 - x)} - \frac{2W}{RT}.
$$
它在 $x = 1/2$ 处最小，所以 $W/RT > 2$ 时曲线中部出现向上凸的区域。会溶温度（这里是最高会溶温度）为

$$
T_{\mathrm{c}} = \frac{W}{2R}.
$$
对称模型的两相组成满足 $\ln\dfrac{x}{1 - x} = \dfrac{W}{RT}(2x - 1)$，即两相共存线。二阶导数为零的曲线 $T = 2Wx(1 - x)/R$ 称为旋节线（spinodal）：在共存线与旋节线之间，均匀溶液对小的涨落是稳定的，分相要通过成核进行（亚稳）；在旋节线以内，任意小的组成涨落都会自发长大（旋节分解）。

![Symmetric regular solution. Left: Gibbs energy of mixing against composition for W/RT = 0, 1.5, 2 and 2.8; for W/RT > 2 the curve has two minima and the common tangent gives the compositions of the two coexisting liquids. Right: coexistence curve and spinodal in reduced temperature T/Tc, with Tc = W/(2R) the upper critical solution temperature; a tie line l1–l2 is shown at T/Tc = 0.8](./plots/regular-solution-miscibility.py)

同样的热力学（推广到高分子的 Flory–Huggins 理论）用来理解细胞中蛋白质与 RNA 的液–液相分离：一些含有低复杂度序列的蛋白质在一定浓度与温度下从胞质中分出富含蛋白质的液滴，形成没有膜包围的细胞器（生物分子凝聚体），如核仁与应激颗粒（[7.3](/7.3)）。

### 9.3.3. 完全不互溶系统与水蒸气蒸馏

若两种液体的互溶度小到可以忽略，它们共存时各自的蒸气压与单独存在时相同，液面上的总蒸气压

$$
p = p_{\mathrm{A}}^* + p_{\mathrm{B}}^*
$$
与两种液体的相对数量无关，并且大于任一纯组分的蒸气压。因此混合物的沸点低于任一纯组分的沸点：只要两种液体都存在，系统就在 $p_{\mathrm{A}}^*(T) + p_{\mathrm{B}}^*(T) = p$ 的温度下沸腾。向不溶于水、沸点高或在沸点附近易分解的有机物中通入水蒸气，使它在低于 $100\,{}^\circ\mathrm{C}$ 时随水蒸气一起蒸出，这种方法称为水蒸气蒸馏（steam distillation），用于提取植物精油、纯化苯胺与硝基苯等。

馏出物中两组分的物质的量之比等于分压之比，$n_{\mathrm{B}}/n_{\mathrm{A}} = p_{\mathrm{B}}^*/p_{\mathrm{A}}^*$，所以质量比为

$$
\frac{m_{\mathrm{B}}}{m_{\mathrm{A}}} = \frac{p_{\mathrm{B}}^*M_{\mathrm{B}}}{p_{\mathrm{A}}^*M_{\mathrm{A}}}.
$$
有机物的蒸气压虽小，摩尔质量却比水大得多，所以每蒸出单位质量的水能带出相当多的有机物。

**例 9.3.1** 溴苯的正常沸点为 $156\,{}^\circ\mathrm{C}$。用 Antoine 方程计算可知，$101.325\,\mathrm{kPa}$ 下水–溴苯混合物在 $95.3\,{}^\circ\mathrm{C}$ 沸腾，此时 $p^*(\ce{H2O}) = 85.4\,\mathrm{kPa}$，$p^*(\ce{C6H5Br}) = 15.9\,\mathrm{kPa}$。馏出物中

$$
\frac{m(\ce{C6H5Br})}{m(\ce{H2O})} = \frac{15.9 \times 157.0}{85.4 \times 18.02} = 1.62,
$$
蒸出 $1\,\mathrm{kg}$ 水可以带出 $1.6\,\mathrm{kg}$ 溴苯。二者密度相差很大，馏出液很容易分层分离。

## 9.4. 固–液平衡

液态完全互溶的二组分系统冷却时会析出固体。固–液平衡对压力不敏感，通常只画 $p^\circ$ 下的 $T$–$x$ 图，$F^* = 3 - P$，最多三相共存。按固态的互溶情况，基本类型有：简单低共熔系统、生成稳定化合物或不稳定化合物的系统、生成固溶体的系统。

### 9.4.1. 热分析与步冷曲线

金属系统的相图用热分析法测定：把已知组成的样品加热熔化，然后在恒压下缓慢均匀地冷却，记录温度随时间的变化。

**定义 9.4.1（步冷曲线）** 恒压下样品缓慢冷却时的温度–时间曲线称为**步冷曲线**。

没有相变时样品按 Newton 冷却规律平滑降温；有固体析出时放出的凝固热抵消一部分散热，曲线斜率变小（出现转折点）；若三相共存（$F^* = 0$），温度保持不变直到一相消失，曲线出现水平段。由一系列组成的步冷曲线上转折点与水平段的温度，就能画出相图。水–盐系统在常温附近用溶解度法测定：配制不同浓度的溶液，测饱和溶解度与凝固点。现代方法还有**差示扫描量热法**（[6.3.1](/6.3.1)）与高温 X 射线衍射。

### 9.4.2. 简单低共熔系统

液态完全互溶、固态完全不互溶、两组分之间不生成化合物的系统，相图最简单。以 Bi–Cd 为例：液相区之下有两条凝固点曲线（液相线），分别表示与纯 Bi(s)、纯 Cd(s) 平衡的液相组成，它们随另一组分的加入而降低（**凝固点降低**），交于一点 E；过 E 的水平线是 Bi(s)、Cd(s) 与组成为 E 的液相的三相平衡线。

**定义 9.4.2（低共熔点）** 简单低共熔系统中两条凝固点曲线的交点 E 称为**低共熔点**（共晶点），在这一温度下两种固体与组成一定的液相三相共存；液相冷却到 E 时两种固体按 E 的组成同时析出，得到的两种细小晶体的混合物称为**低共熔混合物**（共晶体）。

低共熔点处 $C = 2$、$P = 3$，$F^* = 0$：温度与液相组成都是定值。低共熔混合物熔点最低，但它是两相的机械混合物，不是化合物：在显微镜下可以看到两种晶体交替排列的细密组织。

液相线可以由热力学计算。

**定理 9.4.1（理想溶解度方程）** 纯固体 B 与理想液态混合物平衡时，液相中 B 的摩尔分数满足

$$
\ln x_{\mathrm{B}} = -\frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,B}}}{R}\left(\frac{1}{T} - \frac{1}{T_{\mathrm{f,B}}^*}\right),
\tag{9.4}
$$
其中 $T_{\mathrm{f,B}}^*$ 与 $\Delta_{\mathrm{fus}}H_{\mathrm{m,B}}$ 是纯 B 的熔点与摩尔熔化焓（看作与温度无关）。

**证明** 平衡时 $\mu_{\mathrm{B}}^*(\mathrm{s}) = \mu_{\mathrm{B}}(\mathrm{l}) = \mu_{\mathrm{B}}^*(\mathrm{l}) + RT\ln x_{\mathrm{B}}$，所以 $\ln x_{\mathrm{B}} = -\Delta_{\mathrm{fus}}G_{\mathrm{m,B}}/(RT)$。由 **Gibbs–Helmholtz 方程**（[6.3.3](/6.3.3)），$\partial(\Delta_{\mathrm{fus}}G_{\mathrm{m}}/T)/\partial T = -\Delta_{\mathrm{fus}}H_{\mathrm{m}}/T^2$，由 $T_{\mathrm{f,B}}^*$（此处 $\Delta_{\mathrm{fus}}G_{\mathrm{m}} = 0$）积分到 $T$ 即得。$\square$

式 (9.4) 把 B 看作溶剂就是 [6.3.5](/6.3.5) 中凝固点降低公式的未作稀溶液近似的形式；把 B 看作溶质，它就是固体在理想溶液中的溶解度：只与溶质的熔点与熔化焓有关，与溶剂的性质无关，熔点越高、熔化焓越大的固体越难溶。对两条液相线分别用式 (9.4)，二者的交点满足 $x_{\mathrm{A}}(T) + x_{\mathrm{B}}(T) = 1$，用 `scipy.optimize.brentq`（[4.4.4](/4.4.4)）即可求出低共熔点。

**例 9.4.1** Bi：$T_{\mathrm{f}}^* = 544.55\,\mathrm{K}$，$\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 11.30\,\mathrm{kJ\,mol^{-1}}$；Cd：$T_{\mathrm{f}}^* = 594.22\,\mathrm{K}$，$\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 6.21\,\mathrm{kJ\,mol^{-1}}$。按理想溶解度方程算得低共熔点 $408\,\mathrm{K}$，$x(\mathrm{Cd}) = 0.565$（Cd 的质量分数 41%）。实测低共熔点约 $419\,\mathrm{K}$（$146\,{}^\circ\mathrm{C}$），Cd 的质量分数约 40%：组成符合得很好，温度低了约 $10\,\mathrm{K}$，说明液态 Bi–Cd 对理想溶液有正偏差。

![Bi–Cd simple eutectic system. Left: liquidus curves computed from the ideal solubility equation; they meet at the eutectic point E (408 K in the ideal model, about 419 K measured), and the horizontal line through E is the three-phase line Bi(s) + Cd(s) + liquid E. Right: simulated cooling curves for pure Bi, x(Cd) = 0.20, the eutectic composition, 0.80 and pure Cd: pure metals and the eutectic show only a plateau, the other mixtures show a break at the liquidus followed by the eutectic plateau](./plots/bi-cd-eutectic.py)

由步冷曲线读相图（右图）：纯 Bi 与纯 Cd 冷却到熔点时出现水平段（$C = 1$、$P = 2$，$F^* = 0$）；$x(\mathrm{Cd}) = 0.20$ 的样品在液相线温度开始析出 Bi(s)（$F^* = 1$，转折），液相组成沿液相线移向 E，到达低共熔温度时再析出 Cd(s)，三相共存出现水平段，水平段的长度与低共熔混合物的数量成正比；恰为低共熔组成的样品没有转折，只有一个水平段，看起来像纯物质。

### 9.4.3. 水–盐系统

水–盐系统的相图形状与简单低共熔系统相同，左侧凝固点曲线是盐水溶液的冰点线，右侧是盐的溶解度曲线（盐的熔点很高，曲线受水的沸点限制而不能延伸到盐的熔点）。例如 $\ce{(NH4)2SO4}$–$\ce{H2O}$ 的低共熔点为 $254.9\,\mathrm{K}$（$-18.3\,{}^\circ\mathrm{C}$），盐的质量分数为 39.8%。相图有两个用途：

- 配制冷冻剂：冰与盐混合时只要两种固体都在，系统就趋向低共熔点，所以冰盐浴能稳定地维持低共熔温度。
- 设计结晶工艺：把不饱和溶液冷却到溶解度曲线以下析出纯盐，而不要冷却到低共熔点以下（否则冰与盐同时析出）；浓度低于低共熔组成的溶液冷却时先析出冰，要先蒸发浓缩。

冬季道路除冰同样基于水–盐相图。$\ce{NaCl}$–$\ce{H2O}$ 实际上生成不稳定水合物 $\ce{NaCl.2H2O}$（$0.1\,{}^\circ\mathrm{C}$ 以上分解，§9.4.5），低共熔点为 $-21.2\,{}^\circ\mathrm{C}$（$\ce{NaCl}$ 的质量分数 23.3%，固相为冰与 $\ce{NaCl.2H2O}$）；$\ce{CaCl2}$–$\ce{H2O}$ 的低共熔点低至约 $-50\,{}^\circ\mathrm{C}$。撒盐后，只要气温高于低共熔点，冰与盐接触就会溶化成盐水，直到盐水稀释到该温度的冰点线；实际中溶化速度还取决于动力学，$\ce{NaCl}$ 在低于约 $-10\,{}^\circ\mathrm{C}$ 时效果已经很差。氯盐会腐蚀车辆与钢筋、危害路旁植物与土壤，所以有醋酸钙镁、醋酸钾等替代的融雪剂，以及在沥青中掺入缓释融雪材料的"融雪型"路面。

### 9.4.4. 生成稳定化合物的系统

两种固体可以生成一种或几种化合物。若化合物升温到熔化之前一直不分解，熔化时液相与固相组成相同，就称为稳定化合物。

**定义 9.4.3（相合熔点）** 化合物熔化时生成与其组成相同的液相，这一熔点称为**相合熔点**，这样的化合物称为具有相合熔点的化合物（稳定化合物）。

相图中稳定化合物 C 是一条竖直线，液相线在 C 的组成处出现最高点（相合熔点 D）。整张相图可以看作 A–C 与 C–B 两张简单低共熔相图并排拼成，有两个低共熔点。若液态中化合物部分解离，最高点是圆滑的；解离越少，最高点越尖。苯酚–苯胺（生成 1∶1 化合物）、$\ce{CuCl}$–$\ce{FeCl3}$ 属于这一类；$\ce{H2O}$–$\ce{H2SO4}$ 生成 $\ce{H2SO4.H2O}$、$\ce{H2SO4.2H2O}$、$\ce{H2SO4.4H2O}$ 三种稳定水合物，相图由四张简单低共熔图拼成。

![Schematic solid–liquid phase diagrams built from ideal-solubility liquidus curves. (a) A compound C = AB with a congruent melting point D: the diagram is two simple eutectic diagrams side by side. (b) A compound with an incongruent melting point: C decomposes at the peritectic temperature D into solid A and liquid M; E is the eutectic. (c) Complete solid solubility, computed for Cu–Ni as ideal solid and liquid solutions (a lens between liquidus and solidus). (d) Partial solid solubility with a eutectic: two terminal solid solutions α and β separated by solvus lines](./plots/solid-liquid-types.py)

浓硫酸在冬季的运输说明读图的用处：质量分数 98% 的硫酸位于 $\ce{H2SO4}$ 的液相线上，凝固点在 $0\,{}^\circ\mathrm{C}$ 以上，冬天会在管道中冻结；质量分数约 93% 的硫酸接近 $\ce{H2SO4}$ 与 $\ce{H2SO4.H2O}$ 之间的低共熔点，凝固点低于 $-25\,{}^\circ\mathrm{C}$，所以冬季输送的硫酸通常调到 93% 左右。

**例 9.4.2** 在生成稳定化合物 C 的系统中，同一温度下分处化合物两侧液相线上的两个溶液 M、N 都与 C(s) 平衡。把它们倒在一起，会不会形成共轭溶液？

**解** 不会。共轭溶液要求 $\mu_{\mathrm{A}}(\mathrm{M}) = \mu_{\mathrm{A}}(\mathrm{N})$ 且 $\mu_{\mathrm{B}}(\mathrm{M}) = \mu_{\mathrm{B}}(\mathrm{N})$，而 M、N 只满足 $\mu_{\mathrm{A}}(\mathrm{M}) + \mu_{\mathrm{B}}(\mathrm{M}) = \mu_{\mathrm{C}} = \mu_{\mathrm{A}}(\mathrm{N}) + \mu_{\mathrm{B}}(\mathrm{N})$（都与 C 处于化学平衡）。M、N 并不互相平衡。混合后物系点落在 M、N 之间，即该温度下的 $\mathrm{l} + \mathrm{C(s)}$ 两相区，结果是析出固体 C，剩下一个液相。

### 9.4.5. 生成不稳定化合物的系统

若化合物在熔化之前就分解成一种固体与一种组成不同的液相，就称为不稳定化合物。例如 $\ce{CaF2}$–$\ce{CaCl2}$ 系统生成 $\ce{CaF2.CaCl2}$，加热到约 $737\,{}^\circ\mathrm{C}$ 时分解：

$$
\ce{CaF2.CaCl2(s) -> CaF2(s) + melt}\;(x(\ce{CaCl2}) = 0.6).
$$

**定义 9.4.4（不相合熔点）** 化合物分解为一种固体与一种组成不同的液相的温度称为**不相合熔点**（转熔温度），这样的化合物称为不稳定化合物；这一分解反应及其逆反应（固体 A 与液相 M 反应生成化合物 C）称为**转熔反应**（包晶反应）。

不相合熔点处 $\ce{A(s)}$、$\ce{C(s)}$ 与液相 M 三相共存，$F^* = 0$，在相图上是一条水平线 D–M，但液相点 M 在这条线的一端，而不像低共熔点那样在中间。可以把它理解为化合物的"隐藏的"相合熔点被 A 的液相线盖住了：A 的熔点很高，它的液相线在化合物熔化之前就与化合物的液相线相交。

用相图可以设计化合物 C 的制备：若熔体组成在 M 与 E 之间，冷却时首先析出的就是 C，到 E 之前得到的固体都是纯 C。若熔体组成在 M 左侧，冷却时先析出 A(s)，到转熔温度时 A(s) 与熔液反应生成 C，但生成的 C 包在 A 晶体的外面，阻碍了熔液与 A 继续接触，转熔反应不能进行到底（包晶现象），得到的是外包 C、内核为 A 的固体。所以有固相参加时，相图给出的平衡状态未必能在有限时间内达到。

### 9.4.6. 固溶体

两种组分在固态相互溶解成为单一的固相，就是**固溶体**（[6.1.4](/6.1.4)）。按结构分两类：取代型固溶体中两种粒子大小接近（原子半径相差一般不超过 15%，Hume-Rothery 规则），在晶格中互相取代，如 Cu–Ni、Au–Ag；间隙型固溶体中溶质粒子小得多（与溶剂原子半径之比小于约 0.59），填入溶剂晶格的空隙，如 C 溶于 Fe、Ni。一般纯金属强度与硬度较低、塑性很好，形成固溶体后强度与硬度显著提高（固溶强化）：青铜（Sn 溶于 Cu）、黄铜（Zn 溶于 Cu）、银币（Cu 溶于 Ag）都是固溶体型的**合金**。

液态与固态都完全互溶时，相图的形状与理想或非理想的气–液相图相同：一条液相线与一条固相线围成"透镜"形两相区（Cu–Ni、Au–Ag），或者出现最低恒熔点（Au–Cu）。若液相与固溶体都是理想溶液，对每个组分写出 $\mu_i^*(\mathrm{s}) + RT\ln x_i^{\mathrm{s}} = \mu_i^*(\mathrm{l}) + RT\ln x_i^{\mathrm{l}}$，得

$$
\frac{x_i^{\mathrm{l}}}{x_i^{\mathrm{s}}} = \exp\left[-\frac{\Delta_{\mathrm{fus}}H_{\mathrm{m},i}}{R}\left(\frac{1}{T} - \frac{1}{T_{\mathrm{f},i}^*}\right)\right], \qquad i = \mathrm{A}, \mathrm{B},
$$
再加上 $\sum_i x_i^{\mathrm{l}} = \sum_i x_i^{\mathrm{s}} = 1$，即可解出每个温度下的两相组成（上图 (c)）。

冷却时最先析出的固溶体富含高熔点组分，随温度降低，平衡固相的组成沿固相线变化。但原子在固体中扩散很慢，已经析出的晶体来不及调整组成，结果晶体内部组成不均匀，先析出的芯部富含高熔点组分；由于固液界面不稳定，晶体常呈树枝状生长，这称为枝晶偏析（coring）。把合金加热到接近熔点的温度保持一段时间，使组成扩散均匀，就是退火；把高温的固体急速冷却、使高温结构在低温下保留下来，就是淬火。

液态完全互溶、固态部分互溶时，两侧各有一个固溶体单相区（$\alpha$：B 溶于 A，$\beta$：A 溶于 B），中间是类似液–液部分互溶的帽形两相区（$\alpha + \beta$）。这类相图有两种：

- 低共熔型（两组分熔点相差不大，如 Ag–Cu）：三相线上 $\mathrm{l(E)} \rightleftharpoons \alpha + \beta$（上图 (d)），Ag–Cu 的低共熔点为 $779\,{}^\circ\mathrm{C}$。
- 转熔型（两组分熔点相差很大，如 Hg–Cd）：三相线上 $\alpha \rightleftharpoons \mathrm{l} + \beta$ 或 $\mathrm{l} + \alpha \rightleftharpoons \beta$，三相线对应的温度是转熔温度。

Weston **标准电池**（[6.3.13](/6.3.13)）的负极用 Cd 的质量分数为 5%–14% 的镉汞齐，正是利用了 Hg–Cd 相图：在室温下，这一组成范围落在液态汞齐与固溶体共存的两相区中，等温等压下 $F^* = 0$，两相的组成都是确定的，镉的活度从而电极电势也就确定，与汞齐的总组成无关；汞齐中的镉在使用中略有消耗，电势也不变。

### 9.4.7. 区域熔炼

固溶体相图还提供了制备超纯材料的方法。设杂质 B 使主体 A 的熔点降低，在 A 一侧，与液相平衡的固相中杂质的含量比液相低：$k = x_{\mathrm{B}}^{\mathrm{s}}/x_{\mathrm{B}}^{\mathrm{l}} < 1$（分凝系数）。用一个窄的加热环使棒状材料局部熔化，并让熔化区沿棒缓慢移动：熔化区前端不断熔入原料，后端不断重新凝固，凝固出的固体比熔体纯，杂质随熔化区被扫向棒的一端。这种方法称为区域熔炼（zone refining），原理与精馏类似：重复多次相当于多块理论塔板。1952 年 Pfann 用它把锗提纯到杂质含量 $10^{-10}$ 量级，推动了半导体工业的起步；现在用于制备纯度在 99.999999%（"8 个 9"）以上的金属与半导体材料，以及有机化合物的提纯。

## 9.5. 读复杂相图

### 9.5.1. 七类基本相图

按高温相与低温相的互溶情况，二组分 $T$–$x$ 相图可以归纳为七类基本形状。

| 编号 | 高温相与低温相的互溶情况 | 例子 |
|---|---|---|
| ① | 都完全互溶，低温相理想或接近理想 | 理想液态混合物的气–液图；完全互溶固溶体（Cu–Ni） |
| ② | 都完全互溶，低温相偏差很大 | 恒沸物（乙醇–水）；有最低恒熔点的固溶体（Au–Cu） |
| ③ | 低温下部分互溶，只看帽形区 | 部分互溶的双液系（水–苯胺）或双固系 |
| ④ | 高温相完全互溶，低温相完全不互溶 | 简单低共熔系统（Bi–Cd）；完全不互溶双液系的气–液图（苯–水） |
| ⑤ | 生成稳定化合物 | 苯酚–苯胺，$\ce{H2O}$–$\ce{H2SO4}$ |
| ⑥ | 生成不稳定化合物 | $\ce{CaF2}$–$\ce{CaCl2}$ |
| ⑦ | 高温相完全互溶，低温相部分互溶 | 部分互溶固溶体（Ag–Cu、Hg–Cd）；部分互溶液体的气–液图 |

这些基本相图之间可以连续演变：⑦中互溶度减小到零就是④，增大到完全互溶就是②；⑤中组分 A 的熔点逐渐升高时，化合物的相合熔点会被 A 的液相线盖住而变为不相合熔点（⑤→⑥）；②的固溶体在低温下再发生分相，就是②与③的组合，得到⑦。

### 9.5.2. 相图的结构规律

复杂相图（如 Mg–Sn、$\ce{MgO}$–$\ce{SiO2}$）都由基本相图拼接而成。读图时利用以下规律：

1. 竖直线代表纯物质或化合物（化合物的组成固定）。
2. 水平线代表三相线（$F^* = 0$）：线上的三个相点一般是两个端点与线和另一条曲线的交点，三个相就是在这条线上下相邻的相区中出现的相。
3. 曲线都是两相平衡线，曲线上的点是相点。
4. 两相区中共存的两相，由该区左右相邻的两个单相区（或竖直线代表的纯物质）确定，满足杠杆规则。
5. 竖直方向上相邻的两个相区，相数一般相差 1（越过一条相界线只有一个相出现或消失）。

读图的步骤：先找出所有单相区（液相区、固溶体区、纯物质与化合物的竖直线），再由规律 4 确定每个两相区由哪两相组成，最后找三相线上的三个相点。用图时，沿物系点的竖直线从上往下走，就能说出冷却过程中每一步析出什么、步冷曲线是什么形状。

### 9.5.3. Fe–C 相图

钢铁的热处理以 Fe–C 相图为依据，它由几种基本相图组合而成。通常画的是 Fe–$\ce{Fe3C}$（渗碳体）亚稳相图（$\ce{Fe3C}$ 在热力学上不如石墨稳定，但分解极慢），横坐标是 C 的质量分数，右端到渗碳体的组成 6.69%。单相区有液相、$\delta$ 铁素体（体心立方）、奥氏体 $\gamma$（面心立方）、铁素体 $\alpha$（体心立方），它们都是 C 在 Fe 中的间隙固溶体，以及化合物 $\ce{Fe3C}$。特征点的现行数值：

| 特征点 | 温度 | C 的质量分数 | 反应 |
|---|---|---|---|
| 包晶点 | $1495\,{}^\circ\mathrm{C}$ | 0.17% | $\delta + \mathrm{l} \to \gamma$ |
| 共晶点（低共熔点） | $1148\,{}^\circ\mathrm{C}$ | 4.30% | $\mathrm{l} \to \gamma + \ce{Fe3C}$（莱氏体） |
| 奥氏体的最大溶碳量 | $1148\,{}^\circ\mathrm{C}$ | 2.11% | 钢（$< 2.11\%$）与铸铁（$> 2.11\%$）的分界 |
| 共析点 | $727\,{}^\circ\mathrm{C}$ | 0.77% | $\gamma \to \alpha + \ce{Fe3C}$（珠光体） |
| 铁素体的最大溶碳量 | $727\,{}^\circ\mathrm{C}$ | 0.0218% | |

共析反应与共晶反应形式相同，只是三相中没有液相：一个固相分解为两个固相，在固态的扩散下进行，得到两相交替的片层组织。$770\,{}^\circ\mathrm{C}$ 处还有铁素体的磁性转变，即铁的 **Curie 温度**（[5.3.8](/5.3.8#sec-8.5.4)），它是一个连续相变（[6.3.8](/6.3.8)），在相图上不形成新的相区。

## 9.6. 三组分系统

### 9.6.1. 等边三角形坐标

三组分系统 $C = 3$，$F = 5 - P$：最多五相共存，单相时 $F = 4$。恒温或恒压时 $F^* = 4 - P$，相图要用三棱柱的立体图（底面表示组成、高表示温度或压力）；等温等压时 $F^* = 3 - P$，单相区有两个组成变量，可以画成平面图。

三组分的组成常用等边三角形表示（Gibbs 三角形）：三个顶点代表纯 A、B、C，三条边代表三个二组分系统，三角形内的点代表三组分系统。取三角形的高为 1，由 Viviani 定理，三角形内任一点到三边的距离之和等于 1，所以可以用点到 BC、CA、AB 三边的距离分别表示 $x_{\mathrm{A}}$、$x_{\mathrm{B}}$、$x_{\mathrm{C}}$（或质量分数）。实际读数时，过该点作三边的平行线，与各边的交点给出三个组分的含量。三角坐标有以下性质：

1. 平行于某一边的直线上，对角顶点所代表的组分含量相同。
2. 过某一顶点的直线上，另外两个组分的含量之比相同；向系统中加入（或除去）纯组分，物系点沿该组分的顶点与原物系点的连线移动。
3. 两个系统混合，新的物系点在两点的连线上，位置由杠杆规则确定；三个系统混合，新物系点在三点构成的三角形的重心（以物质的量为权）。

![Equilateral triangular coordinates. Left: reading the composition of point O (x_A = 0.2, x_B = 0.3, x_C = 0.5) with lines parallel to the three sides. Right: a partially miscible three-liquid system A + C with solute B, computed from a ternary regular-solution model; the binodal curve encloses the two-liquid region, the tie lines slope upward to the right because B prefers the C-rich phase, and they shrink to the plait point](./plots/ternary-extraction.py)

### 9.6.2. 部分互溶的三液系与萃取

最常用的三组分相图是一对部分互溶的液体 A、C（如水与氯仿）加上一种能与二者都完全互溶的溶质 B（如乙酸）。在 A–C 边上，两液体只在中间的组成范围内分层；加入 B 后两层的互溶度逐渐增大，两相区在三角形中缩成一个由溶解度曲线（双结线）围成的区域。两相区中每一个物系点都分成由一条连结线两端给出的两个共轭液层，两层的数量由杠杆规则确定；连结线越往上越短，最后缩成一点，称为褶点（plait point），在这一点两个液层的组成相同，相当于二组分系统的会溶点。两相区中 $P = 2$，等温等压下 $F^* = 1$：只要一个液层中 B 的含量给定，两层的组成就都确定了——这就是 **Nernst 分配定律**（[6.3.6](/6.3.6)）的相律表述；连结线不平行于 AC 边，表明溶质在两层中的浓度不同，倾斜的方向指向 B 更富集的一层，斜率反映**分配系数**的大小。

**萃取**（[6.3.6](/6.3.6)）就是利用这类相图：向含 B 的 A 溶液（原料）中加入萃取剂 C，物系点沿原料点与 C 顶点的连线移入两相区，分成富含 C 的萃取相与富含 A 的萃余相；把萃取相中的 C 蒸出回收，就得到浓缩的 B。由相图可以确定萃取剂的用量（物系点必须进入两相区）、每一级萃取后两相的组成与数量，以及多级萃取所需的级数。这类计算在 [6.3.6](/6.3.6) 的分配定律中已经给出稀溶液的结果；三角相图适用于溶质浓度较大、两溶剂互溶度不可忽略的情况。二盐–水系统（利用盐的溶解度随温度与第二种盐的变化分离两种盐）也用三角相图分析，这里不再展开。

## 小结

| 内容 | 要点 |
|---|---|
| 相律 | 二组分 $F = 4 - P$，恒压或恒温 $F^* = 3 - P$；三组分等温等压 $F^* = 3 - P$ |
| 理想气–液平衡 | $p = p_{\mathrm{A}}^* + (p_{\mathrm{B}}^* - p_{\mathrm{A}}^*)x_{\mathrm{B}}$；易挥发组分在气相中富集 |
| 杠杆规则 | $n_{\mathrm{l}}(X_{\mathrm{B}} - x_{\mathrm{B}}) = n_{\mathrm{g}}(y_{\mathrm{B}} - X_{\mathrm{B}})$，质量守恒，适用于任何两相区 |
| 非理想气–液平衡 | 偏差很大时出现最低或最高恒沸点，恒沸物 $x = y$，不能用普通精馏完全分离 |
| Duhem–Margules 与 Konovalov | $x_{\mathrm{A}}\,\mathrm{d}\ln p_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln p_{\mathrm{B}} = 0$；极值点 $x = y$；增加某组分使总压升高时，该组分在气相中富集 |
| 液–液平衡 | 共轭溶液、会溶温度；正规溶液 $T_{\mathrm{c}} = W/(2R)$；不互溶系统 $p = p_{\mathrm{A}}^* + p_{\mathrm{B}}^*$，水蒸气蒸馏 |
| 固–液平衡 | 步冷曲线；低共熔点（三相，$F^* = 0$）；理想溶解度方程；相合与不相合熔点；固溶体、枝晶偏析、区域熔炼 |
| 读图规律 | 竖线是纯物质或化合物，水平线是三相线，曲线是两相线，相邻区相数差 1 |
| 三组分 | Gibbs 三角形；双结线、连结线、褶点；萃取 |
