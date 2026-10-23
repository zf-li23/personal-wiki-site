---
title: 滴定分析与酸碱滴定
description: 滴定分析的方式、基准物质、滴定度与计算；活度与浓度常数；分布系数、质子条件与 pH 的精确式和近似判据；缓冲溶液的配制（含离子强度修正、Tris 与 Good 缓冲液）；指示剂与混合指示剂；多元酸碱与混合酸的滴定、双指示剂法；终点误差公式与滴定可行性判据；Kjeldahl 定氮法与氨基酸的滴定。
---

[6.1.9](/6.1.9) 已经讲了酸碱质子理论、弱酸弱碱与两性物质的 pH、缓冲溶液和最简单的滴定曲线（[9.6](/6.1.9#sec-9.6)）。本章把滴定分析作为一种定量方法系统化：先介绍滴定分析的方式与计算（2.1），再说明什么时候要用活度代替浓度（2.2），然后在 6.1.9 的基础上给出酸碱平衡的严格处理与近似判据（2.3）、生理与生化缓冲溶液（2.4）、指示剂的选择（2.5）、多元体系的滴定曲线（2.6），以及终点误差的定量公式与由它得出的滴定可行性判据（2.7），最后是 Kjeldahl 定氮法、氨基酸滴定等应用（2.8）。2.3 的分布系数与 2.7 的终点误差公式是后面三章的统一框架：配位滴定（[6.4.3](/6.4.3)）、沉淀滴定（[6.4.4](/6.4.4)）与氧化还原滴定（[6.4.5](/6.4.5)）只是把质子换成金属离子、沉淀剂或电子，把 pH 换成 pM 或电极电势。

## 2.1. 滴定分析概述

### 2.1.1. 基本概念与滴定方式

**滴定**是把**标准溶液**从滴定管滴加到被测溶液中，直到两者按化学计量关系反应完全，由标准溶液的浓度与体积计算被测物含量的方法（[6.1.9](/6.1.9#sec-9.6.1)）。两者恰好按计量关系反应完全的一点是**化学计量点**（sp），指示剂变色、停止滴定的一点是**滴定终点**（ep），两者不一致造成的误差是**滴定误差**（2.7）。

**定义 2.1.1** 滴定中从滴定管加入的、已知准确浓度的试剂溶液称为**滴定剂**。

按反应类型，滴定分析分为四类，本课程各用一章：

| 类别 | 反应 | 例 | 本课程 |
|---|---|---|---|
| 酸碱滴定 | 质子传递 | $\ce{H+ + OH- -> H2O}$ | 本章 |
| 配位滴定 | 生成配合物 | $\ce{Zn^2+ + Y^4- -> ZnY^2-}$（Y 为 EDTA） | [6.4.3](/6.4.3) |
| 沉淀滴定 | 生成沉淀 | $\ce{Ag+ + Cl- -> AgCl v}$ | [6.4.4](/6.4.4) |
| 氧化还原滴定 | 电子转移 | $\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}$ | [6.4.5](/6.4.5) |

用于滴定的反应必须按确定的计量关系定量完成（99.9% 以上）、速率足够快，并且有确定终点的简便方法。不满足这些条件时，可以改变滴定方式。

**定义 2.1.2** 用标准溶液直接滴定被测物的方式称为**直接滴定**；先加入一定量过量的标准溶液，待反应完全后再用另一种标准溶液滴定剩余量的方式称为**返滴定**；被测物不能直接与滴定剂按确定计量关系反应时，先使它与适当试剂反应、定量置换出另一种物质，再滴定该物质的方式称为**置换滴定**；被测物不与滴定剂反应时，通过其他化学反应把它定量转化为能被滴定的物质的方式称为**间接滴定**。

- 返滴定：$\ce{Al^3+}$ 与 EDTA 反应很慢，并且封闭指示剂，所以先加入过量 EDTA 标准溶液、加热使配位完全，再用 $\ce{Zn^2+}$ 标准溶液返滴定剩余的 EDTA（[6.4.3](/6.4.3#sec-3.6.2)）。固体试样（如 $\ce{CaCO3}$ 溶于过量 HCl）也常用返滴定。
- 置换滴定：$\ce{K2Cr2O7}$ 氧化 $\ce{S2O3^2-}$ 的产物不定（$\ce{S4O6^2-}$ 与 $\ce{SO4^2-}$ 的混合物），没有确定的计量关系；改为在酸性溶液中与过量 KI 反应，置换出定量的 $\ce{I2}$，再用 $\ce{Na2S2O3}$ 滴定（[6.4.5](/6.4.5#sec-5.5.3)）。
- 间接滴定：$\ce{Ca^2+}$ 没有氧化还原性质，先沉淀为 $\ce{CaC2O4}$，过滤洗净后溶于 $\ce{H2SO4}$，再用 $\ce{KMnO4}$ 滴定释放出的 $\ce{H2C2O4}$。

### 2.1.2. 基准物质与标准溶液

标准溶液的配制方法与**基准物质**的条件（组成与化学式相符、纯度 99.9% 以上、性质稳定、摩尔质量较大、参加反应时定量进行）见 [6.1.9](/6.1.9#sec-9.6.1)：基准物质可以直接称量配制标准溶液，其他试剂先粗配再**标定**。常用的基准物质：

| 滴定类型 | 基准物质 | 干燥条件 | 标定对象 |
|---|---|---|---|
| 酸碱 | 无水 $\ce{Na2CO3}$ | 270–300 °C | HCl |
| | 硼砂 $\ce{Na2B4O7*10H2O}$ | 保存于相对湿度 60% 的恒湿器（防风化） | HCl |
| | 邻苯二甲酸氢钾 $\ce{KHC8H4O4}$ | 105–110 °C | NaOH |
| | 草酸 $\ce{H2C2O4*2H2O}$ | 室温空气干燥 | NaOH、$\ce{KMnO4}$ |
| 配位 | Zn、$\ce{CaCO3}$ | Zn 用稀酸洗去氧化膜；$\ce{CaCO3}$ 110 °C | EDTA |
| 沉淀 | NaCl；$\ce{AgNO3}$ | NaCl 500–600 °C；$\ce{AgNO3}$ 避光保存 | $\ce{AgNO3}$；氯化物 |
| 氧化还原 | $\ce{K2Cr2O7}$ | 140–150 °C | $\ce{Na2S2O3}$、$\ce{Fe^2+}$ |
| | $\ce{Na2C2O4}$ | 105–110 °C | $\ce{KMnO4}$ |
| | $\ce{KIO3}$、$\ce{KBrO3}$ | 130 °C | $\ce{Na2S2O3}$ |

$\ce{As2O3}$ 曾是标定碘溶液的基准物质，因剧毒现已少用。$\ce{AgNO3}$ 纯度足够时可以直接配制：配制 $100.0\,\mathrm{mL}$ $0.1000\,\mathrm{mol\,L^{-1}}$ 溶液，准确称取 $0.1000\times0.1000\times169.87 = 1.6987\,\mathrm{g}$ 溶解定容即可。

标准溶液的浓度一般用物质的量浓度 $c_{\mathrm{B}} = n_{\mathrm{B}}/V$ 表示，必须指明基本单元（如 $c(\ce{KMnO4})$ 与 $c(\tfrac15\ce{KMnO4})$ 相差 5 倍；本站一律以化学式为基本单元）。工业上批量测定同一种组分时，用滴定度更方便。

**定义 2.1.3（滴定度）** 每毫升标准溶液 B 相当的被测物 A 的质量称为**滴定度**，记作 $T_{\mathrm{A/B}}$，单位 $\mathrm{g\,mL^{-1}}$。（这里的 $T$ 与热力学温度同字母，只在本节使用。）

设滴定反应为 $a\mathrm{A} + b\mathrm{B} \to$ 产物，计量点时 $n_{\mathrm{A}} : n_{\mathrm{B}} = a : b$。消耗体积 $V_{\mathrm{B}}$（mL）时 $m_{\mathrm{A}} = \frac ab c_{\mathrm{B}}V_{\mathrm{B}}M_{\mathrm{A}}\times10^{-3}$，所以

$$
T_{\mathrm{A/B}} = \frac{m_{\mathrm{A}}}{V_{\mathrm{B}}} = \frac ab\,c_{\mathrm{B}}M_{\mathrm{A}}\times10^{-3}, \qquad m_{\mathrm{A}} = T_{\mathrm{A/B}}V_{\mathrm{B}}, \tag{2.1}
$$
其中 $c_{\mathrm{B}}$ 以 $\mathrm{mol\,L^{-1}}$、$M_{\mathrm{A}}$ 以 $\mathrm{g\,mol^{-1}}$ 计。

### 2.1.3. 滴定分析的计算

计算的步骤是：写出有关的反应式，找出被测物与滴定剂的计量关系，再列式计算。试样质量为 $m_{\mathrm{s}}$ 时，被测物的质量分数为

$$
w_{\mathrm{A}} = \frac{\frac ab\,c_{\mathrm{B}}V_{\mathrm{B}}M_{\mathrm{A}}}{m_{\mathrm{s}}}. \tag{2.2}
$$
涉及几步反应时，由总的计量关系找出被测物与最终滴定剂之间的比例。

**例 2.1.1** 求 $0.1000\,\mathrm{mol\,L^{-1}}$ NaOH 标准溶液对 $\ce{H2C2O4}$ 的滴定度。

**解** $\ce{H2C2O4 + 2NaOH -> Na2C2O4 + 2H2O}$，$a/b = 1/2$，由式 (2.1)，$T_{\ce{H2C2O4}/\ce{NaOH}} = \frac12\times0.1000\times90.03\times10^{-3} = 4.502\times10^{-3}\,\mathrm{g\,mL^{-1}}$。$\square$

**例 2.1.2** $\ce{KMnO4}$ 标准溶液的浓度为 $0.02010\,\mathrm{mol\,L^{-1}}$，求 $T_{\ce{Fe}/\ce{KMnO4}}$ 与 $T_{\ce{Fe2O3}/\ce{KMnO4}}$。称取铁矿试样 $0.2718\,\mathrm{g}$，溶解后把 $\ce{Fe^3+}$ 还原为 $\ce{Fe^2+}$，用该溶液滴定，消耗 $26.30\,\mathrm{mL}$。求试样中 Fe 与 $\ce{Fe2O3}$ 的质量分数。

**解** $\ce{5Fe^2+ + MnO4- + 8H+ -> 5Fe^3+ + Mn^2+ + 4H2O}$，$n(\ce{Fe}) = 5n(\ce{KMnO4})$，$n(\ce{Fe2O3}) = \frac52 n(\ce{KMnO4})$。

$$
T_{\ce{Fe}/\ce{KMnO4}} = 5\times0.02010\times55.845\times10^{-3} = 5.612\times10^{-3}\,\mathrm{g\,mL^{-1}}, \qquad T_{\ce{Fe2O3}/\ce{KMnO4}} = \tfrac52\times0.02010\times159.69\times10^{-3} = 8.024\times10^{-3}\,\mathrm{g\,mL^{-1}},
$$
$w(\ce{Fe}) = 5.612\times10^{-3}\times26.30/0.2718 = 54.31\%$，$w(\ce{Fe2O3}) = 8.024\times10^{-3}\times26.30/0.2718 = 77.65\%$。$\square$

**例 2.1.3** 分析 $0.200\,\mathrm{g}$ 软锰矿时，加入 $50.00\,\mathrm{mL}$ $0.100\,\mathrm{mol\,L^{-1}}$ 硫酸亚铁铵溶液，把 $\ce{MnO2}$ 还原为 $\ce{Mn^2+}$；反应完全后，过量的 $\ce{Fe^2+}$ 用 $0.0200\,\mathrm{mol\,L^{-1}}$ $\ce{KMnO4}$ 返滴定，消耗 $15.0\,\mathrm{mL}$。以 $\ce{Mn3O4}$ 表示锰的含量，求其质量分数。

**解** 两个反应为 $\ce{MnO2 + 2Fe^2+ + 4H+ -> Mn^2+ + 2Fe^3+ + 2H2O}$ 与 $\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}$。加入 $\ce{Fe^2+}$ $5.00\,\mathrm{mmol}$，返滴定消耗 $5\times0.0200\times15.0 = 1.50\,\mathrm{mmol}$，与 $\ce{MnO2}$ 反应的为 $3.50\,\mathrm{mmol}$，即 Mn 为 $1.75\,\mathrm{mmol}$。以 $\ce{Mn3O4}$ 表示（3 个 Mn 对应 1 个 $\ce{Mn3O4}$）：

$$
w(\ce{Mn3O4}) = \frac{\frac13\times1.75\times10^{-3}\times228.81}{0.200} = 66.7\%.
$$
矿石与合金的分析结果常按约定的化合物形式报告，与该元素在试样中实际的存在形式无关。$\square$

**例 2.1.4** 以 $\ce{KBrO3}$ 为基准物质用置换滴定标定 $\ce{Na2S2O3}$ 溶液，写出计量关系。

**解** $\ce{BrO3- + 6I- + 6H+ -> 3I2 + Br- + 3H2O}$，$\ce{I2 + 2S2O3^2- -> 2I- + S4O6^2-}$。总的计量关系 $1\,\ce{BrO3-} \;\hat{=}\; 3\,\ce{I2} \;\hat{=}\; 6\,\ce{S2O3^2-}$，所以 $c(\ce{Na2S2O3}) = \dfrac{6m(\ce{KBrO3})}{M(\ce{KBrO3})V}$。KI 只是中间物，加入过量即可，不必准确计量。$\square$

## 2.2. 活度与平衡常数

### 2.2.1. 离子强度对平衡的影响

向 $\ce{Fe^3+ + SCN- <=> FeSCN^2+}$ 的平衡体系中加入 $\ce{KNO3}$，血红色变浅，$[\ce{FeSCN^2+}]/([\ce{Fe^3+}][\ce{SCN-}])$ 随 $\ce{KNO3}$ 浓度增大而减小；在 $\ce{CaSO4}$ 饱和溶液中加入 $0.05\,\mathrm{mol\,L^{-1}}$ $\ce{KNO3}$，溶解度明显增大。$\ce{K+}$ 与 $\ce{NO3-}$ 并不参加反应，它们通过离子氛的屏蔽作用降低了反应离子的有效浓度，即**活度**。这一效应的理论在 [6.3.12](/6.3.12#sec-12.7) 中已经给出，这里只写出分析中要用的结论。

离子 $i$ 的活度 $a_i = \gamma_ic_i/c^\circ$，**活度因子** $\gamma_i$ 由溶液的**离子强度** $I = \frac12\sum c_iz_i^2$（[6.3.12](/6.3.12#sec-12.6.4)）决定。$25\,^\circ\mathrm{C}$ 的稀水溶液（$I \lesssim 0.01$）中用 **Debye–Hückel 极限公式**，$I \lesssim 0.1$ 时用扩展式：

$$
\lg\gamma_i = -0.509\,z_i^2\sqrt I, \qquad \lg\gamma_i = -\frac{0.509\,z_i^2\sqrt I}{1 + B\mathring{a}\sqrt I}, \tag{2.3}
$$
$I$ 以 $\mathrm{mol\,L^{-1}}$ 的数值代入，$B = 3.29\,\mathrm{nm^{-1}}$（$25\,^\circ\mathrm{C}$ 的水），$\mathring{a}$ 是离子的有效尺寸参数（Kielland 的数据：$\ce{H+}$ 0.9 nm，$\ce{Li+}$、$\ce{Ca^2+}$、$\ce{Mg^2+}$ 0.6–0.8 nm，$\ce{Na+}$、$\ce{HCO3-}$、$\ce{H2PO4-}$ 0.4–0.45 nm，$\ce{K+}$、$\ce{Cl-}$、$\ce{NO3-}$ 0.3 nm，$\ce{SO4^2-}$、$\ce{HPO4^2-}$ 0.4 nm）。在不知道 $\mathring{a}$ 时，可取 $B\mathring{a} \approx 1$，或用 Davies 方程（[6.3.12](/6.3.12#sec-12.7.5)，适用到 $I \approx 0.5$）。

一些教材对式 (2.3) 中常数的解释有误：系数 $0.509 = A$ 正比于 $(\varepsilon_{\mathrm{r}}T)^{-3/2}$（$\varepsilon_{\mathrm{r}}$ 为溶剂的相对电容率），而不是"溶剂色散率与绝对温度 $-2/3$ 次方的乘积"；$\mathring{a} = 900\,\mathrm{pm}$ 只是 $\ce{H+}$ 的值，多数一价离子在 300–450 pm 之间。

活度因子的规律是：离子电荷越高，偏离理想越大（$z_i^2$）；同一离子强度下，同价离子的 $\gamma$ 相近；稀溶液中 $\gamma < 1$，浓的电解质溶液中 $\gamma$ 可以回升甚至大于 1（溶剂的活度降低、离子部分脱水）；中性分子的 $\gamma \approx 1$。

**例 2.2.1** 计算 $0.30\,\mathrm{mol\,L^{-1}}$ NaCl 与 $0.20\,\mathrm{mol\,L^{-1}}$ $\ce{Na2SO4}$ 混合溶液的离子强度。

**解** $c(\ce{Na+}) = 0.70$，$c(\ce{Cl-}) = 0.30$，$c(\ce{SO4^2-}) = 0.20$，$I = \frac12(0.70 + 0.30 + 0.20\times4) = 0.90\,\mathrm{mol\,L^{-1}}$。这样高的离子强度已超出式 (2.3) 的适用范围。$\square$

### 2.2.2. 活度常数与浓度常数

以弱酸 $\ce{HA <=> H+ + A-}$ 为例，平衡常数有三种写法：

$$
K_{\mathrm{a}}^\circ = \frac{a_{\ce{H+}}a_{\ce{A-}}}{a_{\ce{HA}}}, \qquad K_{\mathrm{a}}^{\mathrm{c}} = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]} = K_{\mathrm{a}}^\circ\,\frac{\gamma_{\ce{HA}}}{\gamma_{\ce{H+}}\gamma_{\ce{A-}}}, \qquad K_{\mathrm{a}}^{\mathrm{M}} = \frac{a_{\ce{H+}}[\ce{A-}]}{[\ce{HA}]} = K_{\mathrm{a}}^\circ\,\frac{\gamma_{\ce{HA}}}{\gamma_{\ce{A-}}}.
$$

**定义 2.2.1** 用各物种活度表示的平衡常数 $K^\circ$（即标准平衡常数，又称活度常数或热力学常数）只与温度有关；用平衡浓度表示的平衡常数 $K^{\mathrm{c}}$ 称为**浓度常数**，它还与离子强度有关；$\ce{H+}$ 用活度、其余物种用浓度表示的 $K^{\mathrm{M}}$ 称为**混合常数**。

手册中的 $K_{\mathrm{a}}$、$K_{\mathrm{sp}}$、$\beta_n$ 一般是 $I \to 0$ 的活度常数，或注明了离子强度（如 $I = 0.1$）的浓度常数。混合常数的意义在于 pH 计测得的是 $a_{\ce{H+}}$（[9.2.2](/6.1.9#sec-9.2.2)），而滴定计算中物质的量守恒要用浓度。只有温度与离子强度都一定时，浓度常数才是常数。

**例 2.2.2** (1) $0.500\,\mathrm{mol\,L^{-1}}$ 与 $0.010\,\mathrm{mol\,L^{-1}}$ HCl 溶液中 $\gamma_\pm$ 分别为 0.757 与 0.904，求两溶液的 pH。(2) 求 $25\,^\circ\mathrm{C}$、$I = 0.10$ 时乙酸的 $\mathrm{p}K_{\mathrm{a}}^{\mathrm{c}}$。

**解** (1) $\mathrm{pH} = -\lg(0.757\times0.500) = 0.42$，按浓度计算为 0.30；$\mathrm{pH} = -\lg(0.904\times0.010) = 2.04$，按浓度计算为 2.00。浓度越高，活度修正越大。(2) 用 Davies 方程，$I = 0.10$ 时一价离子 $\lg\gamma = -0.509\times\left(\frac{0.316}{1.316} - 0.030\right) = -0.107$，HAc 是中性分子，$\gamma \approx 1$，

$$
\mathrm{p}K_{\mathrm{a}}^{\mathrm{c}} = \mathrm{p}K_{\mathrm{a}}^\circ + \lg\gamma_{\ce{H+}} + \lg\gamma_{\ce{Ac-}} = 4.76 - 0.21 = 4.55.
$$
离子强度 0.1 使 $\mathrm{p}K_{\mathrm{a}}$ 减小约 0.2，对二价离子参与的平衡影响更大（$\lg\gamma$ 是一价离子的 4 倍）。$\square$

酸碱滴定的计算一般忽略活度：0.2 左右的 $\mathrm{p}K$ 差别只使计量点的 pH 移动零点几，对指示剂的选择与终点误差的估计影响很小。必须考虑活度的场合是：计算或配制 pH 有确定值的缓冲溶液（尤其 pH 标准缓冲溶液，2.4）、离子强度高的溶液、用离子选择性电极测定离子活度（[6.4.6](/6.4.6#sec-6.3)），以及由测得的 pH 求热力学常数。

## 2.3. 酸碱平衡的定量处理

### 2.3.1. 共轭酸碱对的解离常数

按**酸碱质子理论**，**共轭酸碱对**的解离常数满足 $K_{\mathrm{a}}K_{\mathrm{b}} = K_{\mathrm{w}}$（[式 (9.1)](/6.1.9#eq-9.1)）。对 $n$ 元酸 $\ce{H_nA}$，它的各级共轭碱按逆序配对：

$$
K_{\mathrm{a}i}\,K_{\mathrm{b}(n+1-i)} = K_{\mathrm{w}}, \qquad i = 1, \dots, n.
$$
如 $\ce{H3PO4}$ 的 $K_{\mathrm{a}1}$ 对应最弱的共轭碱 $\ce{H2PO4-}$ 的 $K_{\mathrm{b}3}$；$\ce{HPO4^2-}$ 作为碱（接受质子成为 $\ce{H2PO4-}$）的 $\mathrm{p}K_{\mathrm{b}2} = 14.00 - \mathrm{p}K_{\mathrm{a}2} = 14.00 - 7.21 = 6.79$。本章的常数取自 CRC Handbook（$25\,^\circ\mathrm{C}$，$I \to 0$），与 [6.1.9](/6.1.9#sec-9.3.1) 的表一致：$\ce{H3PO4}$ 2.16、7.21、12.32，$\ce{H2CO3}$ 6.35、10.33，HAc 4.76，$\ce{NH4+}$ 9.25，$\ce{H3BO3}$ 9.27，邻苯二甲酸 2.94、5.43。

### 2.3.2. 分析浓度、平衡浓度与分布系数

**定义 2.3.1** 溶液中溶质各种存在形式的浓度之和，即按配制时加入的量计算的浓度，称为**分析浓度**，记作 $c$；平衡时溶液中某一种存在形式（型体）的浓度称为**平衡浓度**，记作 $[\ ]$。

两者由**分布系数** $\delta$（[6.1.9](/6.1.9#sec-9.3.6)）联系：$[\text{型体}] = \delta\cdot c$。对 $n$ 元酸 $\ce{H_nA}$，记失去 $j$ 个质子的型体 $\ce{H}_{n-j}\mathrm{A}^{j-}$ 的分布系数为 $\delta_j$（$j = 0, 1, \dots, n$），由各级 $K_{\mathrm{a}i}$ 的表达式依次消元，

$$
\delta_j = \frac{[\ce{H+}]^{n-j}\prod_{i=1}^{j}K_{\mathrm{a}i}}{\sum_{k=0}^{n}[\ce{H+}]^{n-k}\prod_{i=1}^{k}K_{\mathrm{a}i}}, \tag{2.4}
$$
空积取 1。例如 $n = 3$ 时分母为 $[\ce{H+}]^3 + K_{\mathrm{a}1}[\ce{H+}]^2 + K_{\mathrm{a}1}K_{\mathrm{a}2}[\ce{H+}] + K_{\mathrm{a}1}K_{\mathrm{a}2}K_{\mathrm{a}3}$，分子依次是它的四项。（许多教材按型体所含的质子数给 $\delta$ 编号，$\delta_3$ 指 $\ce{H3PO4}$，与这里相反，阅读时要注意。）由式 (2.4) 可知：$\sum_j\delta_j = 1$；$\delta$ 只是 $[\ce{H+}]$ 与各 $K_{\mathrm{a}}$ 的函数，与分析浓度 $c$ 无关；相邻两型体的分布系数在 $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}i}$ 处相等。$\ce{H3PO4}$ 的三个 $\mathrm{p}K_{\mathrm{a}}$ 相差 5 个单位左右，各型体共存不明显：$\mathrm{pH} = 4.7$ 时 $\delta(\ce{H2PO4-}) = 0.994$，其余两种各约 0.003；$\mathrm{pH} = 9.8$ 时 $\delta(\ce{HPO4^2-}) = 0.994$。正因为如此，磷酸可以被分步滴定（2.6，图中下半部分正是这些分布系数随滴定的变化）。

### 2.3.3. 物料平衡、电荷平衡与质子条件

**物料平衡**、**电荷平衡**与**质子条件**的定义与 $\ce{NaHCO3}$ 的例子见 [6.1.9](/6.1.9#sec-9.4.3)。质子条件可以由物料平衡与电荷平衡相减得到，更直接的写法是参考水准法：

1. 选择溶液中大量存在并参加质子传递的起始物种（包括溶剂水）作为参考水准；
2. 找出所有比参考水准多质子的型体与少质子的型体；
3. 得质子的总量等于失质子的总量，每个型体的浓度乘以它与参考水准相差的质子数。

**例 2.3.1** 写出 $\ce{Na2CO3}$、$\ce{Na2HPO4}$、$\ce{NH4HCO3}$ 水溶液的质子条件。

**解** $\ce{Na2CO3}$：参考水准 $\ce{CO3^2-}$、$\ce{H2O}$；得质子的有 $\ce{HCO3-}$（1 个）、$\ce{H2CO3}$（2 个）、$\ce{H3O+}$，失质子的有 $\ce{OH-}$，质子条件为 $[\ce{H+}] + [\ce{HCO3-}] + 2[\ce{H2CO3}] = [\ce{OH-}]$。$\ce{Na2HPO4}$：参考水准 $\ce{HPO4^2-}$、$\ce{H2O}$，$[\ce{H+}] + [\ce{H2PO4-}] + 2[\ce{H3PO4}] = [\ce{PO4^3-}] + [\ce{OH-}]$。$\ce{NH4HCO3}$：参考水准 $\ce{NH4+}$、$\ce{HCO3-}$、$\ce{H2O}$，$[\ce{H+}] + [\ce{H2CO3}] = [\ce{NH3}] + [\ce{CO3^2-}] + [\ce{OH-}]$。不参加质子传递的 $\ce{Na+}$ 不出现在质子条件中。$\square$

### 2.3.4. pH 的精确式与近似判据

把各型体用 $[\ce{H+}]$ 与分布系数表示后代入质子条件，就得到关于 $[\ce{H+}]$ 的精确方程。以浓度为 $c$ 的一元弱酸为例，质子条件 $[\ce{H+}] = [\ce{A-}] + [\ce{OH-}]$ 给出

$$
[\ce{H+}] = \frac{K_{\mathrm{a}}c}{[\ce{H+}] + K_{\mathrm{a}}} + \frac{K_{\mathrm{w}}}{[\ce{H+}]}, \qquad [\ce{H+}]^3 + K_{\mathrm{a}}[\ce{H+}]^2 - (K_{\mathrm{a}}c + K_{\mathrm{w}})[\ce{H+}] - K_{\mathrm{a}}K_{\mathrm{w}} = 0. \tag{2.5}
$$
允许结果有 5% 的相对误差时，可以作两步近似：

1. 若 $K_{\mathrm{a}}c \ge 20K_{\mathrm{w}}$，水的解离可以忽略（略去的 $K_{\mathrm{w}}$ 项不超过保留项的 5%），式 (2.5) 化为 6.1.9 的一元二次方程 $[\ce{H+}]^2 + K_{\mathrm{a}}[\ce{H+}] - K_{\mathrm{a}}c = 0$；
2. 若 $c/K_{\mathrm{a}} \ge 105$，酸的解离很少，$[\ce{HA}] \approx c$，得 $[\ce{H+}] = \sqrt{K_{\mathrm{a}}c + K_{\mathrm{w}}}$；
3. 两个条件都满足时得最简式 $[\ce{H+}] = \sqrt{K_{\mathrm{a}}c}$。

判据中的 105 正是最简式的相对误差恰好为 5% 的 $c/K_{\mathrm{a}}$：[6.1.9](/6.1.9#sec-9.3.2) 证明了最简式的误差约为 $1/(2\sqrt{c/K_{\mathrm{a}}})$，严格解 $\sqrt r/\bigl(\tfrac12(\sqrt{1+4r} - 1)\bigr) - 1 = 0.05$ 得 $r = c/K_{\mathrm{a}} = 104.9$。6.1.9 采用更严格的 $c/K_{\mathrm{a}} \ge 400$（误差 2.5%），两者只是对允许误差的不同约定。

**例 2.3.2** 计算 $1.0\times10^{-4}\,\mathrm{mol\,L^{-1}}$ $\ce{H3BO3}$ 溶液的 pH（$\mathrm{p}K_{\mathrm{a}} = 9.27$）。

**解** $K_{\mathrm{a}}c = 10^{-13.27} = 5.4\times10^{-14} < 20K_{\mathrm{w}}$，水的解离不能忽略；$c/K_{\mathrm{a}} = 10^{5.27} \gg 105$，$[\ce{HA}] \approx c$。所以

$$
[\ce{H+}] = \sqrt{K_{\mathrm{a}}c + K_{\mathrm{w}}} = \sqrt{5.4\times10^{-14} + 1.0\times10^{-14}} = 2.5\times10^{-7}, \qquad \mathrm{pH} = 6.60.
$$
若误用最简式得 $\mathrm{pH} = 6.64$，$[\ce{H+}]$ 偏低约 8%。$\square$

两性物质 $\ce{NaHA}$（浓度 $c$）的质子条件 $[\ce{H+}] + [\ce{H2A}] = [\ce{A^2-}] + [\ce{OH-}]$ 给出精确式

$$
[\ce{H+}] = \sqrt{\frac{K_{\mathrm{a}1}\bigl(K_{\mathrm{a}2}[\ce{HA-}] + K_{\mathrm{w}}\bigr)}{K_{\mathrm{a}1} + [\ce{HA-}]}}. \tag{2.6}
$$
$\ce{HA-}$ 得失质子的倾向都较弱时 $[\ce{HA-}] \approx c$；若又有 $cK_{\mathrm{a}2} \ge 20K_{\mathrm{w}}$，得近似式 $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}c/(K_{\mathrm{a}1} + c)}$；再有 $c \ge 20K_{\mathrm{a}1}$，得最简式 $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}}$（[式 (9.4)](/6.1.9#eq-9.4)），pH 与浓度无关。

**例 2.3.3** 计算 $0.10\,\mathrm{mol\,L^{-1}}$ 邻苯二甲酸氢钾（KHP）溶液的 pH，并与 NIST 标准缓冲溶液（$0.05\,\mathrm{mol\,kg^{-1}}$ KHP，$25\,^\circ\mathrm{C}$ 时 pH 4.005）比较。

**解** $\mathrm{p}K_{\mathrm{a}1} = 2.94$，$\mathrm{p}K_{\mathrm{a}2} = 5.43$。$cK_{\mathrm{a}2} = 3.7\times10^{-7} \gg 20K_{\mathrm{w}}$，$c/K_{\mathrm{a}1} = 87 > 20$，用最简式，$\mathrm{pH} = \frac12(2.94 + 5.43) = 4.19$（精确式给出同一值）。

它比标准值高 0.18，原因是活度。在 KHP 溶液中 $I \approx c$。用活度常数严格处理：$K_{\mathrm{a}1}^\circ = \dfrac{a_{\ce{H+}}\gamma_1[\ce{HA-}]}{[\ce{H2A}]}$、$K_{\mathrm{a}2}^\circ = \dfrac{a_{\ce{H+}}\gamma_2[\ce{A^2-}]}{\gamma_1[\ce{HA-}]}$（$\gamma_1$、$\gamma_2$ 为一价、二价阴离子的活度因子），代入质子条件 $[\ce{H2A}] \approx [\ce{A^2-}]$ 得 $a_{\ce{H+}}^2 = K_{\mathrm{a}1}^\circ K_{\mathrm{a}2}^\circ/\gamma_2$，即

$$
\mathrm{pH} = \tfrac12(\mathrm{p}K_{\mathrm{a}1}^\circ + \mathrm{p}K_{\mathrm{a}2}^\circ) + \tfrac12\lg\gamma_2.
$$
$I = 0.05$ 时 Davies 方程给出 $\lg\gamma_2 = -0.34$，$\mathrm{pH} = 4.19 - 0.17 = 4.01$，与标准值相符。$\square$

**例 2.3.4** 室温下 $\ce{CO2}$ 饱和水溶液中 $c(\ce{H2CO3}) \approx 0.040\,\mathrm{mol\,L^{-1}}$（包括溶解的 $\ce{CO2}$），求 pH。

**解** $K_{\mathrm{a}1} \gg K_{\mathrm{a}2}$，按一元弱酸处理；$cK_{\mathrm{a}1} \gg 20K_{\mathrm{w}}$，$c/K_{\mathrm{a}1} = 9\times10^4 \gg 105$，$[\ce{H+}] = \sqrt{0.040\times10^{-6.35}}$，$\mathrm{pH} = 3.87$。这就是用 HCl 滴定碳酸盐到第二计量点时溶液的 pH（2.6）。$\square$

| 体系 | 质子条件 | 最简式 | 条件（误差 ≤ 5%） |
|---|---|---|---|
| 一元弱酸 HA | $[\ce{H+}] = [\ce{A-}] + [\ce{OH-}]$ | $[\ce{H+}] = \sqrt{K_{\mathrm{a}}c}$ | $K_{\mathrm{a}}c \ge 20K_{\mathrm{w}}$，$c/K_{\mathrm{a}} \ge 105$ |
| 多元弱酸 $\ce{H2A}$ | $[\ce{H+}] = [\ce{HA-}] + 2[\ce{A^2-}] + [\ce{OH-}]$ | 同上，用 $K_{\mathrm{a}1}$ | 另需 $K_{\mathrm{a}1} \gg K_{\mathrm{a}2}$（忽略二级解离） |
| 两性物质 $\ce{HA-}$ | $[\ce{H+}] + [\ce{H2A}] = [\ce{A^2-}] + [\ce{OH-}]$ | $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}}$ | $cK_{\mathrm{a}2} \ge 20K_{\mathrm{w}}$，$c \ge 20K_{\mathrm{a}1}$ |
| 缓冲溶液 HA–$\ce{A-}$ | 见 2.4 | $[\ce{H+}] = K_{\mathrm{a}}c_{\mathrm{a}}/c_{\mathrm{b}}$ | $c_{\mathrm{a}}, c_{\mathrm{b}} \gg [\ce{H+}], [\ce{OH-}]$ |
| 一元弱碱、多元弱碱 | 同上，把 $\ce{H+}$ 与 $\ce{OH-}$、$K_{\mathrm{a}}$ 与 $K_{\mathrm{b}}$ 互换 | | |

这些近似式的价值在于估算与理解：它们说明了 pH 由哪个平衡主导、随哪些量怎样变化。需要准确数值，或者体系复杂（几种酸碱共存、浓度很稀）时，今天的做法是直接由电荷平衡数值求根（[4.4.4](/4.4.4#sec-4.2.2)，6.1.9 的 [9.6.2](/6.1.9#sec-9.6.2) 已经示范）。把式 (2.4) 写成函数，一段程序就能处理任意的酸碱混合物：

```python
import numpy as np
from scipy.optimize import brentq

Kw = 1.0e-14


def fractions(h, Ka):
    """Distribution fractions of H_nA, H_(n-1)A, ..., A at [H+] = h."""
    terms = np.cumprod(np.concatenate(([1.0], np.asarray(Ka) / h)))
    return terms / terms.sum()


def pH(acids, cation=0.0, anion=0.0):
    """acids: list of (total concentration, [Ka1, Ka2, ...], charge of the fully protonated form);
    cation, anion: concentrations of spectator ions such as Na+ and Cl- (charge units)."""
    def balance(p):
        h = 10.0 ** -p
        q = h - Kw / h + cation - anion
        for c, Ka, z0 in acids:
            d = fractions(h, Ka)
            q += c * np.dot(z0 - np.arange(len(d)), d)
        return q
    return brentq(balance, -2.0, 16.0, xtol=1e-12)    # solve in pH: [H+] spans many decades


print(pH([(0.10, [10**-2.94, 10**-5.43], 0)], cation=0.10))                    # KHP: 4.19
print(pH([(0.05, [10**-6.35, 10**-10.33], 0), (0.05, [10**-9.25], +1)]))       # NH4HCO3: 7.78
```

## 2.4. 缓冲溶液

### 2.4.1. 缓冲溶液的 pH

**缓冲溶液**的作用原理、**Henderson–Hasselbalch 方程** $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} + \lg(c_{\mathrm{b}}/c_{\mathrm{a}})$ 与**缓冲容量**的推导（极大值 $0.576c$ 在 $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}}$ 处，有效范围 $\mathrm{p}K_{\mathrm{a}} \pm 1$）见 [6.1.9](/6.1.9#sec-9.5)。缓冲溶液的 pH 与共轭酸碱对的浓度比有关，与总体积无关，所以在一定范围内稀释时 pH 基本不变；缓冲容量却与总浓度成正比，稀释会降低缓冲能力。

Henderson–Hasselbalch 方程要求 $c_{\mathrm{a}}, c_{\mathrm{b}} \gg [\ce{H+}], [\ce{OH-}]$。不满足时（缓冲溶液很稀，或 $K_{\mathrm{a}}$ 较大），由物料平衡与电荷平衡得到的精确式为

$$
[\ce{H+}] = K_{\mathrm{a}}\,\frac{c_{\mathrm{a}} - [\ce{H+}] + [\ce{OH-}]}{c_{\mathrm{b}} + [\ce{H+}] - [\ce{OH-}]}, \tag{2.7}
$$
酸性缓冲溶液中可略去 $[\ce{OH-}]$，碱性缓冲溶液中可略去 $[\ce{H+}]$。除弱酸及其共轭碱外，浓度较大的两性物质（如邻苯二甲酸氢钾、硼砂）和高浓度的强酸、强碱也有缓冲作用，前者常用作 pH 标准缓冲溶液。

**例 2.4.1** 把 12.43 g Tris（三羟甲基氨基甲烷，$M = 121.14\,\mathrm{g\,mol^{-1}}$）与 4.67 g Tris 盐酸盐（$M = 157.60\,\mathrm{g\,mol^{-1}}$）溶于水配成 1 L，求 pH；再加入 $12.0\,\mathrm{mL}$ $1.00\,\mathrm{mol\,L^{-1}}$ HCl，pH 变为多少？（$25\,^\circ\mathrm{C}$，$\mathrm{p}K_{\mathrm{a}}(\ce{TrisH+}) = 8.07$）

**解** Tris $0.1026\,\mathrm{mol}$，$\ce{TrisH+}$ $0.0296\,\mathrm{mol}$，$\mathrm{pH} = 8.07 + \lg(0.1026/0.0296) = 8.61$。加入的 $0.0120\,\mathrm{mol}$ $\ce{H+}$ 把等量的 Tris 转化为 $\ce{TrisH+}$，两者变为 0.0906 与 0.0416 mol，$\mathrm{pH} = 8.07 + \lg(0.0906/0.0416) = 8.41$，只降低 0.20。同样的 HCl 加入 1 L 纯水，pH 为 1.93。$\square$

**例 2.4.2** 配制 100 mL pH 10.00、$\ce{NH4Cl}$ 浓度为 $0.200\,\mathrm{mol\,L^{-1}}$ 的缓冲溶液，需浓氨水（$14.8\,\mathrm{mol\,L^{-1}}$）与 $\ce{NH4Cl}$ 各多少？

**解** 由 $\mathrm{pH} = 9.25 + \lg([\ce{NH3}]/[\ce{NH4+}])$，$[\ce{NH3}]/[\ce{NH4+}] = 10^{0.75} = 5.62$，$[\ce{NH3}] = 1.12\,\mathrm{mol\,L^{-1}}$。需浓氨水 $1.12\times100/14.8 = 7.6\,\mathrm{mL}$，$\ce{NH4Cl}$ $0.0200\times53.49 = 1.07\,\mathrm{g}$。（离子强度 0.2 时实际 pH 要低一些，精确配制时用 pH 计调节。）$\square$

**例 2.4.3** 配制离子强度为 0.100、pH 7.45 的磷酸盐缓冲溶液 1 L，需 $\ce{NaH2PO4}$ 与 $\ce{Na2HPO4}$ 各多少克？

**解** 设 $[\ce{H2PO4-}] = x$，$[\ce{HPO4^2-}] = y$，则 $[\ce{Na+}] = x + 2y$，$I = \frac12\bigl[(x + 2y) + x + 4y\bigr] = x + 3y = 0.100$。pH 是 $\ce{H+}$ 的活度，所以

$$
\mathrm{pH} = \mathrm{p}K_{\mathrm{a}2}^\circ + \lg\frac{\gamma_2 y}{\gamma_1 x}.
$$
$I = 0.100$ 时 Davies 方程给出 $\lg\gamma_1 = -0.107$、$\lg\gamma_2 = -0.428$，$\lg(y/x) = 7.45 - 7.21 + 0.321 = 0.561$，$y/x = 3.64$。与 $x + 3y = 0.100$ 联立，$x = 8.39\,\mathrm{mmol\,L^{-1}}$，$y = 30.5\,\mathrm{mmol\,L^{-1}}$，需 $\ce{NaH2PO4}$ $8.39\times10^{-3}\times119.98 = 1.007\,\mathrm{g}$，$\ce{Na2HPO4}$ $30.5\times10^{-3}\times141.96 = 4.34\,\mathrm{g}$。若不作活度修正，按 $y/x = 10^{0.24} = 1.74$ 配制，实际的 pH 约为 7.13，相差 0.3：二价离子参与的平衡受离子强度的影响很大。$\square$

### 2.4.2. 常用缓冲溶液与 pH 标准缓冲溶液

选择缓冲体系的原则是 $\mathrm{p}K_{\mathrm{a}}$ 尽量接近所需的 pH，缓冲物质不与体系中的其他组分反应。常用的缓冲物质（$25\,^\circ\mathrm{C}$，CRC）：

| 缓冲物质 | $\mathrm{p}K_{\mathrm{a}}$ | 缓冲物质 | $\mathrm{p}K_{\mathrm{a}}$ |
|---|---|---|---|
| 氨基乙酸（甘氨酸） | 2.34，9.60 | 六次甲基四胺（共轭酸） | 5.15 |
| 一氯乙酸 | 2.87 | 碳酸 | 6.35，10.33 |
| 甲酸 | 3.75 | 磷酸 | 2.16，7.21，12.32 |
| 柠檬酸 | 3.13，4.76，6.40 | 三乙醇胺（共轭酸） | 7.76 |
| 丁二酸 | 4.21，5.64 | Tris（共轭酸） | 8.07 |
| 乙酸 | 4.76 | 硼酸 | 9.27 |
| | | 氨（$\ce{NH4+}$） | 9.25 |

校准 pH 计用的标准缓冲溶液的 pH 不是由 Henderson–Hasselbalch 方程计算的，而是由无液接电池测定、包含活度修正的约定值（IUPAC 2002，$25\,^\circ\mathrm{C}$）：

| 标准缓冲溶液 | pH |
|---|---|
| 饱和酒石酸氢钾（约 $0.034\,\mathrm{mol\,kg^{-1}}$） | 3.557 |
| 邻苯二甲酸氢钾，$0.05\,\mathrm{mol\,kg^{-1}}$ | 4.005 |
| $\ce{KH2PO4}$ 与 $\ce{Na2HPO4}$ 各 $0.025\,\mathrm{mol\,kg^{-1}}$ | 6.865 |
| 硼砂，$0.01\,\mathrm{mol\,kg^{-1}}$ | 9.180 |
| 饱和 $\ce{Ca(OH)2}$ | 12.454 |

### 2.4.3. 生理与生化缓冲溶液

血液的 pH 维持在 7.35–7.45，主要依靠开放的 $\ce{CO2}$–$\ce{HCO3-}$ 体系（$37\,^\circ\mathrm{C}$ 时表观 $\mathrm{p}K_{\mathrm{a}}' = 6.1$），其计算与生理调节见 [6.1.9](/6.1.9#sec-9.5.4) 的例题；此外血浆蛋白与血红蛋白中的组氨酸咪唑基、末端氨基与羧基也是有效的缓冲剂。pH 低于 7.35 称为酸中毒（如糖尿病酮症酸中毒、呼吸衰竭），高于 7.45 称为碱中毒。临床上测定血液的 pH 与 $\ce{CO2}$ 分压或总 $\ce{CO2}$（2.8），由 Henderson–Hasselbalch 方程判断酸碱失衡的类型。

生物化学实验用的缓冲溶液除 pH 外还要考虑离子强度、温度、与金属离子和生物分子的相互作用：

- 磷酸盐缓冲液：$\mathrm{p}K_{\mathrm{a}2} = 7.21$，最接近生理 pH，缓冲范围 6.2–8.2，温度系数很小。常用的磷酸盐缓冲生理盐水（PBS）含 $137\,\mathrm{mmol\,L^{-1}}$ NaCl、$2.7\,\mathrm{mmol\,L^{-1}}$ KCl、$10\,\mathrm{mmol\,L^{-1}}$ $\ce{Na2HPO4}$、$1.8\,\mathrm{mmol\,L^{-1}}$ $\ce{KH2PO4}$，pH 7.4，与体液等渗。缺点是与 $\ce{Ca^2+}$、$\ce{Mg^2+}$ 生成沉淀，并且抑制一些酶（激酶、磷酸酶）。由例 2.4.3，磷酸盐缓冲液的 pH 对离子强度很敏感，加盐或稀释都会改变 pH。
- Tris 缓冲液：$\mathrm{p}K_{\mathrm{a}} = 8.07$（$25\,^\circ\mathrm{C}$），缓冲范围约 7.1–9.1。它易溶、不吸湿、几乎不吸收 $\ce{CO2}$、不沉淀 $\ce{Ca^2+}$，不妨碍大多数酶。缺点有三：$\mathrm{p}K_{\mathrm{a}}$ 的温度系数很大（约 $-0.028\,\mathrm{K^{-1}}$），$25\,^\circ\mathrm{C}$ 配成 pH 8.0 的溶液在 $37\,^\circ\mathrm{C}$ 约为 7.7、在 $4\,^\circ\mathrm{C}$ 约为 8.6，所以应在使用温度下调节 pH；pH 7.5 以下缓冲容量迅速减小；它是伯胺，会与醛、活性酯（如蛋白质标记用的 NHS 酯）反应，并能与某些金属离子配位。

Tris 的这些缺点促使 Good 等（1966）系统地设计了一批两性离子缓冲剂。

**定义 2.4.1（Good 缓冲液）** 按以下要求设计、用于生物学研究的一类两性离子缓冲剂称为 **Good 缓冲液**：$\mathrm{p}K_{\mathrm{a}}$ 在 6–8 之间；水溶性好而不易透过生物膜；受浓度、离子强度与温度的影响小；与金属离子的配位作用弱；化学与酶学上稳定；在 230 nm 以上不吸收紫外–可见光；易于制备与纯化。

它们多是含磺酸基的胺（N-取代的牛磺酸或吗啉、哌嗪衍生物），在缓冲的 pH 下以两性离子存在（2.8.3）。结构式依次为 Tris（1）、MES（2）、MOPS（3）、HEPES（4）：

```smiles
NC(CO)(CO)CO 1
[O-]S(=O)(=O)CC[NH+]1CCOCC1 2
[O-]S(=O)(=O)CCC[NH+]1CCOCC1 3
OCCN1CC[NH+](CCS(=O)(=O)[O-])CC1 4
```

| 缓冲剂 | $\mathrm{p}K_{\mathrm{a}}$（$25\,^\circ\mathrm{C}$） | $\mathrm{d}\,\mathrm{p}K_{\mathrm{a}}/\mathrm{d}T$ / $\mathrm{K^{-1}}$ | 缓冲范围 |
|---|---|---|---|
| MES | 6.27 | $-0.011$ | 5.5–6.7 |
| PIPES | 7.14 | $-0.008$ | 6.1–7.5 |
| MOPS | 7.18 | $-0.011$ | 6.5–7.9 |
| HEPES | 7.56 | $-0.014$ | 6.8–8.2 |
| Tris | 8.07 | $-0.028$ | 7.1–9.1 |
| 磷酸盐（$\mathrm{p}K_{\mathrm{a}2}$） | 7.21 | $-0.003$ | 6.2–8.2 |

（$\mathrm{p}K_{\mathrm{a}}$ 为 $I \to 0$ 的热力学值，取自 NIST 的评述数据；文献中常见的 HEPES 7.5、MES 6.1 等是 $20\,^\circ\mathrm{C}$ 或一定离子强度下的值。）HEPES 用于细胞培养基，MOPS 用于 RNA 的变性凝胶电泳，MES 用于 pH 6 附近的蛋白质层析。Good 缓冲液也不是完全惰性的：哌嗪类缓冲剂（HEPES、PIPES）在光照下产生自由基，HEPES 会干扰 Folin–Lowry 法测蛋白质。

## 2.5. 酸碱指示剂

### 2.5.1. 变色原理与变色范围

**酸碱指示剂**是酸式与碱式颜色不同的有机弱酸或弱碱；溶液颜色取决于 $[\ce{In-}]/[\ce{HIn}] = K_{\mathrm{HIn}}/[\ce{H+}]$，理论**变色范围**为 $\mathrm{pH} = \mathrm{p}K_{\mathrm{HIn}} \pm 1$。酚酞（内酯式无色 ⇌ 醌式红色）与甲基橙（偶氮式黄色 ⇌ 醌式红色）的结构变化见 [6.1.9](/6.1.9#sec-9.2.3)。实际的变色范围由目测确定，往往偏离 $\mathrm{p}K_{\mathrm{HIn}} \pm 1$，原因是人眼对不同颜色的敏感程度不同：甲基橙的红色比黄色醒目，红色组分只要约为黄色的 2 倍就显红色，所以变色范围的酸端只比 $\mathrm{p}K_{\mathrm{HIn}}$ 低 0.3。

| 指示剂 | $\mathrm{p}K_{\mathrm{HIn}}$ | 变色范围 | 酸式色 → 碱式色 |
|---|---|---|---|
| 甲基橙 | 3.4 | 3.1–4.4 | 红 → 黄 |
| 溴酚蓝 | 4.1 | 3.0–4.6 | 黄 → 紫 |
| 溴甲酚绿 | 4.9 | 3.8–5.4 | 黄 → 蓝 |
| 甲基红 | 5.0 | 4.4–6.2 | 红 → 黄 |
| 溴百里酚蓝 | 7.1 | 6.0–7.6 | 黄 → 蓝 |
| 酚红 | 7.9 | 6.8–8.4 | 黄 → 红 |
| 酚酞 | 9.1 | 8.2–10.0 | 无色 → 红 |
| 百里酚酞 | 10.0 | 9.4–10.6 | 无色 → 蓝 |

（酚酞的变色范围在不同手册中写作 8.0–10.0、8.0–9.6 或 8.2–10.0，这里取 8.2–10.0。）变色范围越窄，终点越敏锐。

### 2.5.2. 混合指示剂

**定义 2.5.1（混合指示剂）** 由两种指示剂、或一种指示剂与一种不随 pH 变色的染料按一定比例混合而成，利用颜色互补使变色范围变窄、颜色变化更敏锐的指示剂称为**混合指示剂**。

最常用的是溴甲酚绿–甲基红：在 pH 5.1 以下两者的酸式色（黄与红）合成酒红色，pH 5.1 时两种颜色互补呈灰色，pH 稍高即变为绿色（溴甲酚绿的蓝与甲基红的黄），终点只有约 0.2 个 pH 单位宽，用于以 $\ce{Na2CO3}$ 标定 HCl 和 Kjeldahl 定氮的硼酸吸收液滴定（2.8）。甲基橙与靛蓝二磺酸钠（染料）的混合物也是这一类。把几种变色范围不同的指示剂混合，就是在整个 pH 范围内逐渐变色的通用指示剂与 pH 试纸。

### 2.5.3. 影响变色的因素

1. 指示剂的用量。双色指示剂（甲基橙、甲基红）的颜色只取决于 $[\ce{In-}]/[\ce{HIn}]$，与指示剂浓度无关，但用量太多时颜色深、变化不敏锐，指示剂本身也消耗滴定剂。单色指示剂（酚酞）只有碱式有色：设人眼能看出颜色所需的最低浓度为 $a$，在 $\mathrm{pH} < \mathrm{p}K_{\mathrm{HIn}}$ 的区域 $[\ce{In-}] = c_{\ce{HIn}}K_{\mathrm{HIn}}/([\ce{H+}] + K_{\mathrm{HIn}}) \approx c_{\ce{HIn}}K_{\mathrm{HIn}}/[\ce{H+}]$，于是开始显色的 pH 为

$$
\mathrm{pH}_{\text{变色}} = \mathrm{p}K_{\mathrm{HIn}} + \lg\frac{a}{c_{\ce{HIn}}},
$$
指示剂浓度增大 10 倍，变色点降低 1 个 pH 单位。50–100 mL 溶液中加 2–3 滴酚酞约在 pH 9 变色，加 15–20 滴约在 pH 8 变色。
2. 温度。温度改变 $K_{\mathrm{HIn}}$ 与 $K_{\mathrm{w}}$，变色范围随之移动，滴定一般在室温进行，需要加热（如煮沸除 $\ce{CO2}$）时要冷却后再滴定到终点。
3. 溶剂与离子强度。有机溶剂与大量中性盐改变 $\mathrm{p}K_{\mathrm{HIn}}$（2.2），以及溶液对光的吸收。
4. 滴定次序。颜色由浅到深的变化比由深到浅容易观察：用 NaOH 滴定酸时用酚酞（无色 → 红），用 HCl 滴定碱时用甲基橙（黄 → 橙）。

## 2.6. 酸碱滴定曲线与滴定的可行性

### 2.6.1. 一元酸碱的滴定

强碱滴定强酸与弱酸的**滴定曲线**、**滴定突跃**的计算与指示剂的选择见 [6.1.9](/6.1.9#sec-9.6.2)：$0.1000\,\mathrm{mol\,L^{-1}}$ NaOH 滴定同浓度 HCl 的突跃范围为 4.30–9.70，滴定 HAc 为 7.76–9.70，计量点 pH 8.73。选择指示剂的原则是：指示剂的变色范围全部或部分落在突跃范围之内，在此前提下变色点越接近计量点越好。这里补充几点规律。

- 强酸强碱：浓度每降低到 1/10，突跃范围两端各收缩 1 个 pH 单位，共缩小 2 个单位（$1.000\,\mathrm{mol\,L^{-1}}$：3.30–10.70；$0.01000\,\mathrm{mol\,L^{-1}}$：5.30–8.70）。浓度是影响突跃大小的唯一因素。
- 弱酸：计量点前是缓冲区，突跃的起点 $\mathrm{pH} \approx \mathrm{p}K_{\mathrm{a}} + 3$（剩余 0.1% 的酸），只取决于 $K_{\mathrm{a}}$；计量点后与滴定强酸相同，取决于浓度。所以 $K_{\mathrm{a}}$ 每减小到 1/10，或浓度每降低到 1/10，突跃都缩小约 1 个单位，突跃的大小由 $cK_{\mathrm{a}}$ 决定（下图）。只能用在碱性区变色的指示剂（酚酞、百里酚酞），甲基橙完全不能用。

![NaOH 滴定同浓度的一元弱酸。左：c = 0.1000 mol/L，pKa 不同；右：pKa = 7，浓度不同。灰带为计量点前后 ±0.1%](./plots/weak-acid-feasibility.py)

由图可见，$c_{\mathrm{sp}}K_{\mathrm{a}}$（$c_{\mathrm{sp}}$ 是计量点时弱酸的分析浓度）降到 $10^{-9}$ 左右时，突跃已经小到无法目测。2.7 将由终点误差公式得到准确滴定的判据：

$$
c_{\mathrm{sp}}K_{\mathrm{a}} \ge 10^{-8} \quad(\text{弱酸}), \qquad c_{\mathrm{sp}}K_{\mathrm{b}} \ge 10^{-8} \quad(\text{弱碱}). \tag{2.8}
$$
它的前提是：终点观测的不确定性为 $\pm0.2$ 个 pH 单位（人眼判断指示剂颜色的极限），允许的终点误差为 $\pm0.1\%$。$K_{\mathrm{a}}$ 太小的酸（如 $\ce{H3BO3}$、$\ce{NH4+}$）不能直接滴定，可以设法强化：$\ce{H3BO3}$ 与甘露醇、甘油等多元醇生成 $\mathrm{p}K_{\mathrm{a}}$ 约为 4–5 的配位酸后用 NaOH 滴定；$\ce{NH4+}$ 与甲醛反应释放出等物质的量的 $\ce{H+}$（甲醛法），或者在非水溶剂中滴定。

强酸滴定弱碱与此对称。用 $0.1000\,\mathrm{mol\,L^{-1}}$ HCl 滴定同浓度 $\ce{NH3}$，计量点为 $0.05000\,\mathrm{mol\,L^{-1}}$ $\ce{NH4Cl}$，$\mathrm{pH} = 5.28$，突跃范围 6.25–4.30，用甲基红（或溴甲酚绿–甲基红）作指示剂，甲基橙偏离计量点较远。

### 2.6.2. 多元酸的滴定

多元酸的滴定要回答两个问题：各级解离的 $\ce{H+}$ 能否被准确滴定，能否被分步滴定（第一级完全中和之后第二级才开始中和，滴定曲线上出现分开的突跃）。由 2.7 的推导，第 $i$ 级能被准确分步滴定的常用判据是

$$
c_{\mathrm{sp}}K_{\mathrm{a}i} \ge 10^{-9} \quad\text{且}\quad \frac{K_{\mathrm{a}i}}{K_{\mathrm{a}(i+1)}} \ge 10^4; \tag{2.9}
$$
其中比值条件对应 $\Delta\mathrm{pH} = \pm0.2$、终点误差 $\pm1\%$；$c_{\mathrm{sp}}K_{\mathrm{a}i} \ge 10^{-9}$ 对应 $\Delta\mathrm{pH} = \pm0.3$、误差 $\pm0.5\%$（只要求 $\pm1\%$ 时 $10^{-10}$ 已足够，取 $10^{-9}$ 留有余量）。允许误差为 $\pm0.5\%$ 时，比值要求约为 $10^5$。只要求测定总量时，按最弱的一级 $K_{\mathrm{a}n}$ 用式 (2.8) 判断。多元碱把 $K_{\mathrm{a}}$ 换成 $K_{\mathrm{b}}$。

**例 2.6.1** 用 $0.1000\,\mathrm{mol\,L^{-1}}$ NaOH 滴定 $20.00\,\mathrm{mL}$ $0.1000\,\mathrm{mol\,L^{-1}}$ $\ce{H3PO4}$，判断能否分步滴定，计算各计量点的 pH 并选择指示剂。

**解** $K_{\mathrm{a}1}/K_{\mathrm{a}2} = 10^{5.05}$，$K_{\mathrm{a}2}/K_{\mathrm{a}3} = 10^{5.11}$，都大于 $10^4$；第一计量点 $c_{\mathrm{sp}} = 0.050$，$c_{\mathrm{sp}}K_{\mathrm{a}1} \gg 10^{-9}$；第二计量点 $c_{\mathrm{sp}} = 0.033$，$c_{\mathrm{sp}}K_{\mathrm{a}2} = 2\times10^{-9} > 10^{-9}$；而 $c_{\mathrm{sp}}K_{\mathrm{a}3} \approx 1.6\times10^{-14}$，第三级不能直接滴定。所以可以分步滴定前两级，出现两个突跃。

第一计量点溶液为 $0.0500\,\mathrm{mol\,L^{-1}}$ $\ce{NaH2PO4}$。$c/K_{\mathrm{a}1} = 7.2$，不满足 $c \ge 20K_{\mathrm{a}1}$，要用式 (2.6) 的近似式 $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}c/(K_{\mathrm{a}1} + c)}$，得 $\mathrm{pH} = 4.71$（最简式给出 4.69）。可用甲基橙（滴到黄色）或溴甲酚绿–甲基橙混合指示剂。第二计量点溶液为 $0.0333\,\mathrm{mol\,L^{-1}}$ $\ce{Na2HPO4}$，$cK_{\mathrm{a}3} = 1.6\times10^{-14}$ 与 $K_{\mathrm{w}}$ 相当，水的解离不能忽略，由式 (2.6) 得 $[\ce{H+}] = \sqrt{K_{\mathrm{a}2}(K_{\mathrm{a}3}c + K_{\mathrm{w}})/c}$，$\mathrm{pH} = 9.66$（最简式给出的 9.77 偏高）。可用百里酚酞（无色 → 浅蓝）或酚酞–百里酚酞混合指示剂；单用酚酞终点偏早。计量点前后 $\pm1\%$ 的 pH 变化分别为 4.17–5.25 与 9.16–10.16，只有约 1 个单位，所以这两个突跃都只能达到约 $\pm0.5\%$ 的准确度。第三级的 $\ce{H+}$ 可以在加入 $\ce{CaCl2}$ 生成 $\ce{Ca3(PO4)2}$ 沉淀、释放出 $\ce{H+}$ 后再滴定。$\square$

![NaOH 滴定 H₃PO₄（各 0.1000 mol/L，CRC 常数，由电荷平衡数值计算）。上：滴定曲线与两个计量点；下：四种型体的分布系数随滴定的变化](./plots/phosphoric-acid-titration.py)

### 2.6.3. 多元碱的滴定与双指示剂法

用 HCl 滴定 $\ce{Na2CO3}$：$\ce{CO3^2-}$ 的 $K_{\mathrm{b}1} = K_{\mathrm{w}}/K_{\mathrm{a}2} = 10^{-3.67}$，$\ce{HCO3-}$ 的 $K_{\mathrm{b}2} = K_{\mathrm{w}}/K_{\mathrm{a}1} = 10^{-7.65}$，$K_{\mathrm{b}1}/K_{\mathrm{b}2} = 10^{3.98}$，略小于 $10^4$。第一计量点（$\ce{NaHCO3}$，pH 8.34）附近曲线很平缓，计量点前后 $\pm1\%$ 只有 0.4 个 pH 单位的变化（下图插图）。所以第一级不能被准确地分步滴定，用酚酞（滴到无色）或甲酚红–百里酚蓝混合指示剂（pH 8.3）只能达到约 $\pm1\%$ 的准确度。第二计量点是 $\ce{CO2}$ 的饱和溶液，pH 约 3.9，用甲基橙（黄 → 橙）作指示剂；由于溶液中积累的 $\ce{CO2}$ 使终点提前且不敏锐，更好的做法是用甲基红或溴甲酚绿–甲基红，滴到变色后煮沸除去 $\ce{CO2}$（溶液又回到碱式色），冷却后再滴定到终点。

![0.1000 mol/L HCl 滴定 20.00 mL 0.1000 mol/L Na₂CO₃（密闭体系）。插图为第一计量点前后 ±2% 的 pH，变化很平缓](./plots/carbonate-titration.py)

**定义 2.6.1（双指示剂法）** 在同一份试液中先用酚酞作指示剂滴定到第一终点（消耗体积 $V_1$），再加甲基橙继续滴定到第二终点（又消耗 $V_2$），由 $V_1$ 与 $V_2$ 的关系确定混合碱的组成并计算各组分含量的方法称为**双指示剂法**。

酚酞终点时 $\ce{OH-}$ 已中和、$\ce{CO3^2-}$ 转化为 $\ce{HCO3-}$；甲基橙终点时 $\ce{HCO3-}$ 转化为 $\ce{CO2}$。所以：

| $V_1$ 与 $V_2$ | 组成 | 各组分消耗的 HCl |
|---|---|---|
| $V_1 > V_2 > 0$ | NaOH + $\ce{Na2CO3}$ | NaOH：$V_1 - V_2$；$\ce{Na2CO3}$：$2V_2$ |
| $V_2 > V_1 > 0$ | $\ce{Na2CO3}$ + $\ce{NaHCO3}$ | $\ce{Na2CO3}$：$2V_1$；$\ce{NaHCO3}$：$V_2 - V_1$ |
| $V_1 = V_2$ | $\ce{Na2CO3}$ | $2V_1$ |
| $V_1 = 0$ | $\ce{NaHCO3}$ | $V_2$ |
| $V_2 = 0$ | NaOH | $V_1$ |

**例 2.6.2** 称取 $0.2000\,\mathrm{g}$ 烧碱试样，用 $0.1000\,\mathrm{mol\,L^{-1}}$ HCl 滴定，酚酞终点消耗 $24.00\,\mathrm{mL}$，再加甲基橙，又消耗 $12.00\,\mathrm{mL}$。求 NaOH 与 $\ce{Na2CO3}$ 的质量分数。

**解** $V_1 > V_2$，试样含 NaOH 与 $\ce{Na2CO3}$。$n(\ce{Na2CO3}) = cV_2 = 1.200\,\mathrm{mmol}$，$n(\ce{NaOH}) = c(V_1 - V_2) = 1.200\,\mathrm{mmol}$，

$$
w(\ce{Na2CO3}) = \frac{1.200\times10^{-3}\times105.99}{0.2000} = 63.59\%, \qquad w(\ce{NaOH}) = \frac{1.200\times10^{-3}\times40.00}{0.2000} = 24.00\%.
$$
双指示剂法简便，但第一终点不敏锐，误差可达 1% 左右。更准确的方法是氯化钡法：一份试液用甲基橙滴定总碱量；另一份加 $\ce{BaCl2}$ 沉淀 $\ce{CO3^2-}$ 后，用酚酞滴定剩余的 NaOH。$\square$

### 2.6.4. 混合酸的滴定

两种弱酸 HA 与 HB（$K_{\mathrm{HA}} > K_{\mathrm{HB}}$）混合时，在允许误差 $\pm1\%$ 时能分别滴定的条件与多元酸相似：$c_{\mathrm{HA}}K_{\mathrm{HA}} \ge 10^{-9}$，且 $c_{\mathrm{HA}}K_{\mathrm{HA}}/(c_{\mathrm{HB}}K_{\mathrm{HB}}) \ge 10^4$；若还有 $c_{\mathrm{HB}}K_{\mathrm{HB}} \ge 10^{-9}$，较弱的酸也能接着被滴定。比值条件中出现的是浓度与常数的乘积，因为两种酸彼此独立，竞争的强弱由 $cK$ 决定。强酸与弱酸混合时，若弱酸的 $K_{\mathrm{a}}$ 足够小（如 HCl 与 $\ce{NH4Cl}$、HCl 与 $\ce{H3BO3}$），可以单独滴定强酸；若弱酸较强（如 HCl 与 HAc），第一个突跃很小，只能滴定总量。

## 2.7. 终点误差

### 2.7.1. 终点误差公式

**滴定误差**（终点误差）用 $E_{\mathrm{t}}$ 表示：终点时滴定剂加入的量与计量关系所需的量之差，占被测物的量的百分数，正值表示滴定过量。它来自终点与计量点不一致，属于方法引起的**系统误差**。下面由质子条件推出它的计算式。

用浓度为 $c$ 的 NaOH 滴定 HCl，终点时溶液中 $c_{\mathrm{ep}}(\ce{NaOH})$ 与 $c_{\mathrm{ep}}(\ce{HCl})$ 分别是两者的分析浓度，电荷平衡 $[\ce{Na+}] + [\ce{H+}] = [\ce{Cl-}] + [\ce{OH-}]$ 给出

$$
E_{\mathrm{t}} = \frac{c_{\mathrm{ep}}(\ce{NaOH}) - c_{\mathrm{ep}}(\ce{HCl})}{c_{\mathrm{ep}}(\ce{HCl})} = \frac{[\ce{OH-}]_{\mathrm{ep}} - [\ce{H+}]_{\mathrm{ep}}}{c_{\mathrm{ep}}(\ce{HCl})}. \tag{2.10}
$$
滴定弱酸 HA 时，电荷平衡为 $[\ce{Na+}] + [\ce{H+}] = [\ce{A-}] + [\ce{OH-}]$，$[\ce{A-}] = c_{\mathrm{ep}}(\ce{HA}) - [\ce{HA}]$，计量点附近溶液呈碱性，$[\ce{H+}]$ 可以忽略：

$$
E_{\mathrm{t}} = \frac{[\ce{OH-}]_{\mathrm{ep}} - [\ce{HA}]_{\mathrm{ep}}}{c_{\mathrm{ep}}(\ce{HA})} = \frac{[\ce{OH-}]_{\mathrm{ep}}}{c_{\mathrm{ep}}(\ce{HA})} - \delta_{\ce{HA},\mathrm{ep}}. \tag{2.11}
$$
式 (2.10) 与 (2.11) 对任何终点都成立。终点靠近计量点时，把它们用终点与计量点的 pH 之差 $\Delta\mathrm{pH} = \mathrm{pH}_{\mathrm{ep}} - \mathrm{pH}_{\mathrm{sp}}$ 表示，得到更便于使用的形式。

**定理 2.7.1（终点误差公式）** 设终点靠近计量点，$c_{\mathrm{sp}}$ 是被测物在计量点时的分析浓度，$K_{\mathrm{t}}$ 是滴定反应的平衡常数。

1. 强碱滴定强酸（$K_{\mathrm{t}} = 1/K_{\mathrm{w}}$）：$E_{\mathrm{t}} = \dfrac{10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}}}{c_{\mathrm{sp}}\sqrt{K_{\mathrm{t}}}}$；
2. 强碱滴定一元弱酸（$\ce{HA + OH- -> A- + H2O}$，$K_{\mathrm{t}} = K_{\mathrm{a}}/K_{\mathrm{w}}$）：$E_{\mathrm{t}} = \dfrac{10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}}}{\sqrt{c_{\mathrm{sp}}K_{\mathrm{t}}}}$；
3. 二元酸 $\ce{H2A}$ 滴定到第一计量点（$c_{\mathrm{sp}}K_{\mathrm{a}2} \gg K_{\mathrm{w}}$，$c_{\mathrm{sp}} \gg K_{\mathrm{a}1}$）：$E_{\mathrm{t}} = (10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}})\sqrt{K_{\mathrm{a}2}/K_{\mathrm{a}1}}$。

强酸滴定强碱或弱碱的情形，把式中的 $\Delta\mathrm{pH}$ 换成 $-\Delta\mathrm{pH}$、$K_{\mathrm{a}}$ 换成 $K_{\mathrm{b}}$。

**证明** (1) 计量点时 $[\ce{H+}]_{\mathrm{sp}} = [\ce{OH-}]_{\mathrm{sp}} = \sqrt{K_{\mathrm{w}}}$，所以 $[\ce{H+}]_{\mathrm{ep}} = \sqrt{K_{\mathrm{w}}}\,10^{-\Delta\mathrm{pH}}$，$[\ce{OH-}]_{\mathrm{ep}} = \sqrt{K_{\mathrm{w}}}\,10^{\Delta\mathrm{pH}}$；终点靠近计量点，$c_{\mathrm{ep}}(\ce{HCl}) \approx c_{\mathrm{sp}}$。代入式 (2.10)，并注意 $\sqrt{K_{\mathrm{w}}} = 1/\sqrt{K_{\mathrm{t}}}$。

(2) 计量点时溶液是 $c_{\mathrm{sp}}$ 的 $\ce{A-}$，$[\ce{OH-}]_{\mathrm{sp}} = \sqrt{K_{\mathrm{w}}c_{\mathrm{sp}}/K_{\mathrm{a}}}$；计量点附近 $[\ce{A-}] \approx c_{\mathrm{sp}}$，$[\ce{HA}] = [\ce{H+}]c_{\mathrm{sp}}/K_{\mathrm{a}}$，于是 $[\ce{HA}]_{\mathrm{sp}} = \dfrac{K_{\mathrm{w}}}{[\ce{OH-}]_{\mathrm{sp}}}\cdot\dfrac{c_{\mathrm{sp}}}{K_{\mathrm{a}}} = [\ce{OH-}]_{\mathrm{sp}}$（这正是计量点的质子条件）。终点时 $[\ce{OH-}]_{\mathrm{ep}} = [\ce{OH-}]_{\mathrm{sp}}10^{\Delta\mathrm{pH}}$，$[\ce{HA}]_{\mathrm{ep}} = [\ce{HA}]_{\mathrm{sp}}10^{-\Delta\mathrm{pH}} = [\ce{OH-}]_{\mathrm{sp}}10^{-\Delta\mathrm{pH}}$，代入式 (2.11)：

$$
E_{\mathrm{t}} = \frac{[\ce{OH-}]_{\mathrm{sp}}}{c_{\mathrm{sp}}}\bigl(10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}}\bigr) = \sqrt{\frac{K_{\mathrm{w}}}{K_{\mathrm{a}}c_{\mathrm{sp}}}}\bigl(10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}}\bigr).
$$

(3) 第一计量点前后，终点误差等于多中和的 $\ce{HA-}$ 与未中和的 $\ce{H2A}$ 之差：$E_{\mathrm{t}} = ([\ce{A^2-}]_{\mathrm{ep}} - [\ce{H2A}]_{\mathrm{ep}})/c_{\mathrm{sp}}$（$\ce{H+}$、$\ce{OH-}$ 相对很小）。$[\ce{HA-}] \approx c_{\mathrm{sp}}$，$[\ce{A^2-}] = K_{\mathrm{a}2}c_{\mathrm{sp}}/[\ce{H+}]$，$[\ce{H2A}] = [\ce{H+}]c_{\mathrm{sp}}/K_{\mathrm{a}1}$，计量点 $[\ce{H+}]_{\mathrm{sp}} = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}}$，代入即得。$\square$

这些公式是 Ringbom（1958）系统化的。注意强酸与弱酸的分母不同：弱酸是 $\sqrt{c_{\mathrm{sp}}K_{\mathrm{t}}}$，强酸是 $c_{\mathrm{sp}}\sqrt{K_{\mathrm{t}}}$，因为强酸的计量点 pH 与浓度无关。配位滴定把 $\Delta\mathrm{pH}$ 换成 $\Delta\mathrm{pM}'$、$K_{\mathrm{t}}$ 换成条件稳定常数，得到同样形式的公式（公式 3.3.1）；氧化还原滴定的对应公式见公式 5.3.1。

![弱酸滴定的终点误差 |Et| 随 ΔpH 的变化（终点误差公式），不同 c_sp K_t；虚线为 |Et| = 0.1%，点线为目测的极限 ΔpH = ±0.2](./plots/ringbom-error.py)

### 2.7.2. 由终点误差公式得到的判据

取 $\Delta\mathrm{pH} = \pm0.2$，$10^{0.2} - 10^{-0.2} = 0.954$。

- 弱酸：$\lvert E_{\mathrm{t}}\rvert \le 0.1\%$ 要求 $\sqrt{c_{\mathrm{sp}}K_{\mathrm{t}}} \ge 954$，即 $c_{\mathrm{sp}}K_{\mathrm{t}} \ge 9.1\times10^5$，$c_{\mathrm{sp}}K_{\mathrm{a}} \ge 9.1\times10^{-9} \approx 10^{-8}$，这就是式 (2.8)。允许 $\pm1\%$ 时降为 $10^{-10}$；上图中 $c_{\mathrm{sp}}K_{\mathrm{t}} = 10^6$ 的曲线在 $\Delta\mathrm{pH} = \pm0.2$ 处恰好约为 0.1%。
- 强酸：$c_{\mathrm{sp}}\sqrt{K_{\mathrm{t}}} \ge 954$，$c_{\mathrm{sp}} \ge 9.5\times10^{-5}\,\mathrm{mol\,L^{-1}}$，即强酸强碱的浓度不应低于约 $10^{-4}\,\mathrm{mol\,L^{-1}}$。
- 多元酸的分步滴定：$\lvert E_{\mathrm{t}}\rvert \le 1\%$ 要求 $0.954\sqrt{K_{\mathrm{a}2}/K_{\mathrm{a}1}} \le 0.01$，$K_{\mathrm{a}1}/K_{\mathrm{a}2} \ge 9.1\times10^3 \approx 10^4$，这就是式 (2.9)；要求 $\pm0.5\%$ 时，取 $\Delta\mathrm{pH} = \pm0.3$ 得 $K_{\mathrm{a}1}/K_{\mathrm{a}2} \ge 8.9\times10^4 \approx 10^5$。

可见终点误差由三个因素决定：反应的完全程度（$K_{\mathrm{t}}$）、浓度（$c_{\mathrm{sp}}$）与终点检测的精度（$\Delta\mathrm{pH}$）。改用电位滴定（[6.4.6](/6.4.6#sec-6.4.5)）可以把 $\Delta\mathrm{pH}$ 减小到 0.02 左右，相应的判据放宽两个数量级。

**例 2.7.1** 用 $0.10\,\mathrm{mol\,L^{-1}}$ NaOH 滴定 $10\,\mathrm{mL}$ $0.10\,\mathrm{mol\,L^{-1}}$ HCl，终点 pH 为 5.0（如用甲基红滴到橙色），求终点误差。

**解** $c_{\mathrm{ep}}(\ce{HCl}) \approx c_{\mathrm{sp}} = 0.050\,\mathrm{mol\,L^{-1}}$，由式 (2.10)，

$$
E_{\mathrm{t}} = \frac{10^{-9.0} - 10^{-5.0}}{0.050} = -0.02\%.
$$
由定理 2.7.1 (1)，$\Delta\mathrm{pH} = -2.0$，$E_{\mathrm{t}} = (10^{-2} - 10^{2})/(0.050\times10^7) = -0.02\%$，结果相同。$\square$

**例 2.7.2** 用 $0.1000\,\mathrm{mol\,L^{-1}}$ NaOH 滴定同浓度 HAc，分别以酚酞（终点 pH 9.0）和甲基橙（终点 pH 4.0）为指示剂，求终点误差。

**解** $c_{\mathrm{sp}} = 0.0500$，$\mathrm{pH}_{\mathrm{sp}} = 8.73$，$c_{\mathrm{sp}}K_{\mathrm{t}} = 0.0500\times1.75\times10^{-5}/10^{-14} = 8.75\times10^7$。酚酞：$\Delta\mathrm{pH} = 0.27$，

$$
E_{\mathrm{t}} = \frac{10^{0.27} - 10^{-0.27}}{\sqrt{8.75\times10^7}} = +0.014\%.
$$
甲基橙：终点离计量点太远，定理 2.7.1 的前提（$[\ce{A-}] \approx c_{\mathrm{sp}}$）不再成立，要用式 (2.11) 直接计算：$E_{\mathrm{t}} \approx -\delta_{\ce{HAc}} = -\dfrac{10^{-4.0}}{10^{-4.0} + 1.75\times10^{-5}} = -85\%$，即只中和了 15%。这说明了为什么滴定弱酸不能用在酸性区变色的指示剂。$\square$

## 2.8. 酸碱滴定的应用

### 2.8.1. 酸碱标准溶液的配制与标定

HCl 与 NaOH 都不能直接配制标准溶液，常用浓度为 $0.1\,\mathrm{mol\,L^{-1}}$，先粗配，再标定。

- HCl：用无水 $\ce{Na2CO3}$ 标定，$\ce{Na2CO3 + 2HCl -> 2NaCl + CO2 + H2O}$，计量点 pH 约 3.9，用甲基橙或溴甲酚绿–甲基红（近终点时煮沸除 $\ce{CO2}$）。$\ce{Na2CO3}$ 易得纯品，但易吸湿，要在 270–300 °C 干燥后密封保存，且摩尔质量小（105.99），称量误差较大。或用硼砂标定，$\ce{Na2B4O7 + 2HCl + 5H2O -> 4H3BO3 + 2NaCl}$，计量点为 $\ce{H3BO3}$ 溶液，pH 约 5.1，用甲基红；硼砂摩尔质量大（381.37），不吸湿，但空气相对湿度低于 39% 时会风化失去结晶水，应保存在相对湿度 60% 的恒湿器中（装有 NaCl 与蔗糖饱和溶液的干燥器）。
- NaOH：NaOH 易吸湿并吸收 $\ce{CO2}$。先配成约 50% 的浓溶液，$\ce{Na2CO3}$ 在其中溶解度很小而沉降，取上清液用煮沸除去 $\ce{CO2}$ 的水稀释。用邻苯二甲酸氢钾标定（摩尔质量 204.22，纯净、不吸湿、易保存，1:1 反应），计量点为邻苯二甲酸根溶液，pH 约 9.1，用酚酞；也可用草酸 $\ce{H2C2O4*2H2O}$。

NaOH 溶液吸收的 $\ce{CO2}$ 是否引起误差，取决于终点的 pH：吸收 $\ce{CO2}$ 生成的 $\ce{CO3^2-}$ 若在甲基橙终点（pH 约 4）被滴定，它消耗 2 个 $\ce{H+}$，与原来的 2 个 $\ce{OH-}$ 相当，没有误差；若在酚酞终点（pH 约 9），$\ce{CO3^2-}$ 只转化为 $\ce{HCO3-}$，消耗 1 个 $\ce{H+}$，有效浓度偏低。所以标定与使用 NaOH 溶液时应当用同一种指示剂，并尽量避免吸收 $\ce{CO2}$。

**例 2.8.1** 纯 $\ce{CaCO3}$ $0.5000\,\mathrm{g}$ 溶于 $50.00\,\mathrm{mL}$ HCl 溶液中，过量的酸用 NaOH 溶液返滴定，消耗 $6.20\,\mathrm{mL}$；已知 $1\,\mathrm{mL}$ NaOH 溶液相当于 $1.010\,\mathrm{mL}$ HCl 溶液。求两种溶液的浓度。

**解** 剩余的 HCl 相当于 $6.20\times1.010 = 6.26\,\mathrm{mL}$，与 $\ce{CaCO3}$ 反应的 HCl 为 $50.00 - 6.26 = 43.74\,\mathrm{mL}$。$\ce{CaCO3 + 2HCl -> CaCl2 + CO2 + H2O}$，$n(\ce{HCl}) = 2n(\ce{CaCO3}) = 2\times0.5000/100.09 = 9.991\,\mathrm{mmol}$，

$$
c(\ce{HCl}) = \frac{9.991}{43.74} = 0.2284\,\mathrm{mol\,L^{-1}}, \qquad c(\ce{NaOH}) = 1.010\times0.2284 = 0.2307\,\mathrm{mol\,L^{-1}}.
$$
$\square$

### 2.8.2. Kjeldahl 定氮法

蛋白质含氮量相当恒定（约 16%），测定氮就能估算蛋白质含量，这是食品、饲料与生物样品分析中最常用的方法之一。

**定义 2.8.1（Kjeldahl 定氮法）** 用浓硫酸在催化剂存在下消解有机试样，把其中的含氮化合物转化为 $\ce{NH4+}$，加碱蒸馏出 $\ce{NH3}$，用酸吸收后以酸碱滴定测定氮含量的方法称为 **Kjeldahl 定氮法**（Kjeldahl，1883）。

1. 消解：试样与浓 $\ce{H2SO4}$ 共热，加入 $\ce{K2SO4}$ 提高沸点（到约 380 °C），加入 $\ce{CuSO4}$ 作催化剂（过去用 Hg 或 Se，因毒性已淘汰），有机物被氧化为 $\ce{CO2}$ 与 $\ce{H2O}$，氨基与酰胺氮转化为 $\ce{NH4HSO4}$。
2. 蒸馏：消解液冷却稀释后加过量浓 NaOH，$\ce{NH4+ + OH- -> NH3 ^ + H2O}$，用水蒸气把 $\ce{NH3}$ 蒸出。
3. 吸收与滴定：现行做法是用 2%–4% 的 $\ce{H3BO3}$ 溶液吸收，$\ce{NH3 + H3BO3 -> NH4+ + H2BO3-}$，再用 HCl 标准溶液滴定生成的 $\ce{H2BO3-}$（以溴甲酚绿–甲基红为指示剂，终点 pH 约 5）。$\ce{H3BO3}$ 是极弱的酸，不干扰滴定，也不必准确计量。经典做法是用过量的 HCl 或 $\ce{H2SO4}$ 标准溶液吸收，再用 NaOH 返滴定剩余的酸（甲基红为指示剂），需要两种标准溶液。
4. 同时做空白试验，扣除试剂中的氮。

氮的质量分数 $w(\ce{N}) = \dfrac{c(\ce{HCl})(V - V_{\text{空白}})M(\ce{N})}{m_{\mathrm{s}}}$，蛋白质含量 $= F\cdot w(\ce{N})$，换算因子 $F$ 一般取 6.25（$= 100/16$），乳制品取 6.38，小麦取 5.70。

**例 2.8.2** 称取乳粉 $0.5000\,\mathrm{g}$ 按 Kjeldahl 法处理，用硼酸吸收，以 $0.1000\,\mathrm{mol\,L^{-1}}$ HCl 滴定消耗 $14.20\,\mathrm{mL}$，空白消耗 $0.10\,\mathrm{mL}$。求蛋白质含量。

**解** $w(\ce{N}) = \dfrac{0.1000\times(14.20 - 0.10)\times10^{-3}\times14.007}{0.5000} = 3.950\%$，蛋白质含量 $= 6.38\times3.950\% = 25.2\%$。$\square$

Kjeldahl 法测的是总有机氮与铵态氮，不能区分蛋白质氮与其他含氮物质（硝态氮与杂环氮需要额外的还原处理）。2008 年奶粉中添加三聚氰胺（$\ce{C3H6N6}$，含氮 66.6%）冒充蛋白质的事件，正是利用了这一局限；此后乳制品检测增加了针对三聚氰胺的液相色谱–质谱法（[6.4.15](/6.4.15#sec-15.5.1)）。现代实验室也常用燃烧法（Dumas 法）测定总氮：试样在氧气中高温燃烧，含氮物质转化为 $\ce{N2}$ 后用热导检测器测定（[6.4.13](/6.4.13#sec-13.6.4)），几分钟完成一个样品，不用浓硫酸。

### 2.8.3. 氨基酸的滴定与等电点

氨基酸同时含有酸性的羧基与碱性的氨基。

**定义 2.8.2（两性离子）** 分子内同时带有正电荷与负电荷基团、净电荷为零的离子称为**两性离子**（偶极离子）。

在水溶液与晶体中，氨基酸主要以两性离子 $\ce{H3N^+CHRCOO^-}$ 存在，而不是中性分子 $\ce{H2NCHRCOOH}$：羧基（$\mathrm{p}K_{\mathrm{a}}$ 约 2）的酸性远强于铵基（$\mathrm{p}K_{\mathrm{a}}$ 约 9–10），质子从羧基转移到氨基上。这解释了氨基酸熔点高、易溶于水而难溶于有机溶剂。以甘氨酸为例，它在强酸中以阳离子（1）存在，在中性附近以两性离子（2）存在，在强碱中以阴离子（3）存在：

```smiles
[NH3+]CC(=O)O 1
[NH3+]CC(=O)[O-] 2
NCC(=O)[O-] 3
```

把阳离子 $\ce{H2A+}$ 看作二元酸，$\mathrm{p}K_{\mathrm{a}1} = 2.34$（羧基）、$\mathrm{p}K_{\mathrm{a}2} = 9.60$（铵基），两性离子 $\ce{HA}$ 就是 2.3.4 的两性物质。

**定义 2.8.3（等电点）** 氨基酸或蛋白质分子的平均净电荷为零时溶液的 pH 称为**等电点**，记作 pI。

在等电点 $[\ce{H2A+}] = [\ce{A-}]$，由 $K_{\mathrm{a}1}K_{\mathrm{a}2} = [\ce{H+}]^2[\ce{A-}]/[\ce{H2A+}]$ 得

$$
\mathrm{pI} = \tfrac12(\mathrm{p}K_{\mathrm{a}1} + \mathrm{p}K_{\mathrm{a}2}),
$$
甘氨酸的 $\mathrm{pI} = 5.97$。它与两性物质的最简式 $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}}$ 相同：纯甘氨酸水溶液的 pH 就近似等于它的等电点。侧链可以解离的氨基酸，pI 取两性离子两侧的两个 $\mathrm{p}K_{\mathrm{a}}$ 的平均值：天冬氨酸（$\mathrm{p}K_{\mathrm{a}}$ 1.99、3.90、9.90）的 $\mathrm{pI} = \frac12(1.99 + 3.90) = 2.95$，赖氨酸（2.16、9.06、10.54）的 $\mathrm{pI} = \frac12(9.06 + 10.54) = 9.80$。蛋白质的等电点由所有可解离侧链共同决定；在等电点时蛋白质的溶解度最小，在电场中不移动，这是等电点沉淀与等电聚焦电泳（[6.4.14](/6.4.14)）的基础。

![0.1000 mol/L NaOH 滴定 20.00 mL 0.1000 mol/L 甘氨酸盐酸盐。上：滴定曲线，第一计量点即等电点；下：阳离子、两性离子与阴离子的分布系数](./plots/glycine-titration.py)

用 NaOH 滴定甘氨酸盐酸盐时，第一计量点的溶液就是两性离子，pH 等于 pI，突跃明显；第二级（铵基）$c_{\mathrm{sp}}K_{\mathrm{a}2} \approx 10^{-11}$，不能直接滴定。从图中还能看出两段缓冲区分别以 $\mathrm{p}K_{\mathrm{a}1}$ 与 $\mathrm{p}K_{\mathrm{a}2}$ 为中心：氨基酸本身是缓冲剂（表中的甘氨酸缓冲液，pH 2.2–3.6 与 8.6–10.6）。要测定氨基的量，可以用甲醛法（Sørensen 甲醛滴定）：甲醛与氨基反应，使铵基释放出 $\ce{H+}$，就能用 NaOH 以酚酞为指示剂滴定，过去用来跟踪蛋白质水解的进程；或者在冰醋酸中用 $\ce{HClO4}$ 作非水滴定，这是药典测定氨基酸含量的方法。

血液中总 $\ce{CO2}$（$\ce{HCO3-}$、溶解的 $\ce{CO2}$ 与 $\ce{H2CO3}$ 之和）的测定也是酸碱反应的应用：加酸使 $\ce{HCO3-}$ 全部转化为 $\ce{CO2}$，测定释放出的气体体积或压力；或者加入过量的 HCl 标准溶液，赶尽 $\ce{CO2}$ 后用 NaOH 返滴定剩余的酸。结合测得的 pH 与 Henderson–Hasselbalch 方程，就能算出 $[\ce{HCO3-}]$ 与 $\ce{CO2}$ 分压。

## 小结

| 问题 | 结论 |
|---|---|
| 浓度常数与活度常数 | $K^{\mathrm{c}}$ 随离子强度变化；配制缓冲溶液、使用标准缓冲溶液与离子选择性电极时要作活度修正 |
| pH 的计算 | 由质子条件（或电荷平衡）列精确式；误差 5% 内的近似判据 $K_{\mathrm{a}}c \ge 20K_{\mathrm{w}}$、$c/K_{\mathrm{a}} \ge 105$；复杂体系数值求根 |
| 缓冲溶液的选择 | $\mathrm{p}K_{\mathrm{a}}$ 接近所需 pH；生化实验还要看温度系数、离子强度、金属配位与反应性 |
| 指示剂的选择 | 变色范围落在突跃范围内，变色点尽量接近计量点 |
| 一元弱酸（碱）能否准确滴定 | $c_{\mathrm{sp}}K_{\mathrm{a}} \ge 10^{-8}$（$\Delta\mathrm{pH} = \pm0.2$，$\lvert E_{\mathrm{t}}\rvert \le 0.1\%$） |
| 多元酸能否分步滴定 | $c_{\mathrm{sp}}K_{\mathrm{a}i} \ge 10^{-9}$ 且 $K_{\mathrm{a}i}/K_{\mathrm{a}(i+1)} \ge 10^4$（$\pm1\%$） |
| 终点误差 | 式 (2.10)、(2.11) 普遍适用；终点近于计量点时用终点误差公式（定理 2.7.1） |
