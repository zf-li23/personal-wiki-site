---
title: 可逆电池的电动势及其应用
description: 可逆电池与三类可逆电极；端电压、对消法与标准电池；由化学反应等温式推出 Nernst 方程，电动势与 ΔrG、K°、ΔrS、ΔrH 和可逆热；内电势、外电势与电化学势，电动势的组成与液接电势；电极电势与参比电极；浓差电池与由反应设计电池；用电动势法测平衡常数、活度因子、标准电极电势、迁移数与 pH；Fe–H₂O 电势–pH 图；膜电势、细胞静息电位与玻璃电极。
---

[6.3.12](/6.3.12) 研究了电解质溶液本身；本章研究电流趋于零时电池的平衡性质。这时电池中的化学反应以可逆的方式进行，测得的电动势直接给出反应的摩尔 Gibbs 自由能：$\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$。电动势可以测到 $10^{-5}\,\mathrm{V}$ 甚至更高的精度，于是电化学测量成为求 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$、$K^\circ$、$\Delta_{\mathrm{r}}S_{\mathrm{m}}$、$\Delta_{\mathrm{r}}H_{\mathrm{m}}$、平均活度因子与 pH 的精确方法。

[6.1.11](/6.1.11) 与 [6.1.12](/6.1.12) 已经介绍了原电池、电池符号、电极电势、Nernst 方程、浓差电池和电势–pH 图的基本用法，那里以浓度近似活度，对热力学基础只作了初步说明。本章把这些结论放到 [6.3.3](/6.3.3)（Gibbs 判据与 Gibbs–Helmholtz 方程）、[6.3.6](/6.3.6)（活度）与 [6.3.7](/6.3.7)（化学反应等温式）的严格基础上：用活度写出 Nernst 方程（13.3），用电化学势分析电动势由哪些界面电势差组成（13.4），并系统讨论电动势法的应用（13.7）与电势–pH 图（13.8）。最后一节讨论膜电势：细胞膜两侧的离子浓度差产生的电势是神经冲动与细胞能量转换的基础。有电流通过时电极偏离平衡，那是 [6.3.14](/6.3.14) 的内容。

## 13.1. 可逆电池与可逆电极

### 13.1.1. 化学能转变为电能的条件

同一个反应 $\ce{Zn + Cu^2+ -> Zn^2+ + Cu}$ 可以在烧杯中进行，也可以在电池中进行。两种途径的始态和终态相同，状态函数的变化（$\Delta_{\mathrm{r}}G$、$\Delta_{\mathrm{r}}H$、$\Delta_{\mathrm{r}}S$）相同，功和热却不同：

| | 热化学反应（烧杯中） | 电化学反应（电池中） |
|---|---|---|
| 反应物 | 直接接触，电子在碰撞中转移 | 在空间上分开，分别在两个电极上反应 |
| 电子的路径 | 极短，无规则 | 经外电路，定向运动 |
| 速率由谁决定 | 温度、浓度（活化能来自热运动） | 还取决于电极电势（[6.3.14](/6.3.14)） |
| 能量形式 | 全部以热放出，$W' = 0$，$Q_p = \Delta_{\mathrm{r}}H$ | 电功 + 热，$Q_p \ne \Delta_{\mathrm{r}}H$ |

只有氧化还原反应，或者包含氧化还原步骤的反应（如沉淀反应、中和反应，13.6.2）才能设计成电池，把电子转移的路径拉长到外电路中。

等温等压下，系统 Gibbs 自由能的变化不大于环境对系统所做的**非体积功**：$(\Delta_{\mathrm{r}}G)_{T,p} \le W'$，可逆时取等号（[6.3.3](/6.3.3)、[6.1.6](/6.1.6)）。电池对外做电功时 $W' < 0$。若反应进度为 $1\,\mathrm{mol}$ 时有 $z\,\mathrm{mol}$ 电子通过外电路，电量为 $zF$，在两极间电势差 $U$ 下环境对系统做的电功为 $W' = -zFU$。可逆放电时两极间的电势差就是电池的**电动势** $E_{\mathrm{cell}}$（物理 [5.3.5](/5.3.5) 的 $\mathcal{E}$），于是

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}\quad(\text{可逆}), \qquad -\Delta_{\mathrm{r}}G_{\mathrm{m}} > zFU\quad(\text{不可逆放电}). \tag{13.1}
$$
可逆时化学能 $-\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 全部转变为电功；不可逆时只有一部分转变为电功，其余以热的形式耗散。式 (13.1) 把反应的性质（$\Delta_{\mathrm{r}}G_{\mathrm{m}}$）与电池的性质（$E_{\mathrm{cell}}$）联系起来，是本章的基础；它只对可逆电池成立。

### 13.1.2. 可逆电池

**定义 13.1.1** 满足下面两个条件的电池称为**可逆电池**：

1. 物质可逆：电池放电时的电极反应与总反应，在外加反向电压充电时能完全逆向进行，系统能复原；电池中不存在两种不同电解质溶液的接界等不可逆过程。
2. 能量可逆：电池在电流趋于零的条件下充、放电，放电时对外做最大电功，充电时消耗最小电功，电流通过电池时没有 Joule 热等耗散，环境也能复原。

例如 $\ce{Zn} \mid \ce{ZnCl2}(\mathrm{aq}) \mid \ce{AgCl(s)} \mid \ce{Ag}$：放电时 $\ce{Zn + 2AgCl -> Zn^2+ + 2Cl- + 2Ag}$，充电时恰好逆向。而把 Zn 插入稀硫酸、Cu 也插入稀硫酸构成的 Volta 电池，放电时阴极析出 $\ce{H2}$，充电时阳极溶解的却是 Cu，充、放电的反应不同，不是可逆电池。

可逆电池是理想化的极限，它给出了化学能转变为电能的最高限度，也是测量热力学量的工具。严格地说，只有单液电池（两个电极共用一种电解质溶液）可能是可逆的；双液电池中两种溶液接界处的扩散是不可逆的（13.4.6），用盐桥把液接电势降到可以忽略后，近似当作可逆电池。

### 13.1.3. 电池符号与电池反应

**电池符号**的书写规则见 [6.1.11](/6.1.11)：负极（阳极）写在左，正极（阴极）写在右，按物质接触的顺序书写；$\mid$ 表示相界面，$\parallel$ 表示已消除液接电势的盐桥，$\vdots$（或 $\mid$ 的虚线）表示两种溶液的直接接界，同一相中的物质用逗号隔开；注明温度（未注明指 $298.15\,\mathrm{K}$）、各物质的相态以及溶液的浓度（活度）和气体的分压。

电池反应是电池放电时两个电极上以及整个电池中发生的总变化：左边电极发生氧化，右边电极发生还原，两者电子数相等后相加。写电池反应时注意：

1. 两个电极反应的电子数必须相同；$z$ 是所写的电池反应进行 $1\,\mathrm{mol}$ 时转移的电子数。
2. 不要随意把离子合并成电解质分子；同一种物质只有处于同一相、同一状态时才能在两边消去。
3. 反应式中不要出现电池符号中没有的物质（水溶液中的 $\ce{H2O}$ 除外）。

| 电池 | 电极反应 | 电池反应（$z$） |
|---|---|---|
| $\ce{Pt} \mid \ce{H2}(p) \mid \ce{HCl}(b) \mid \ce{AgCl(s)} \mid \ce{Ag}$ | 左 $\tfrac12\ce{H2 -> H+ + e-}$；右 $\ce{AgCl + e- -> Ag + Cl-}$ | $\tfrac12\ce{H2 + AgCl -> Ag + H+ + Cl-}$（1） |
| $\ce{Pt} \mid \ce{H2}(p_1) \mid \ce{KOH}(b) \mid \ce{O2}(p_2) \mid \ce{Pt}$ | 左 $\ce{2H2 + 4OH- -> 4H2O + 4e-}$；右 $\ce{O2 + 2H2O + 4e- -> 4OH-}$ | $\ce{2H2 + O2 -> 2H2O}$（4） |
| $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+}(a = 0.1) \parallel \ce{Fe^3+}(a = 0.2), \ce{Fe^2+}(a = 0.05) \mid \ce{Pt}$ | 左 $\tfrac12\ce{H2 -> H+ + e-}$；右 $\ce{Fe^3+ + e- -> Fe^2+}$ | $\tfrac12\ce{H2 + Fe^3+ -> H+ + Fe^2+}$（1） |
| $\ce{Pt} \mid \ce{O2}(p^\circ) \mid \ce{HCl}(b_1) \parallel \ce{HCl}(b_2) \mid \ce{O2}(p^\circ) \mid \ce{Pt}$ | 左 $\ce{H2O -> 2H+}(b_1) + \tfrac12\ce{O2 + 2e-}$；右 $\ce{2H+}(b_2) + \tfrac12\ce{O2 + 2e- -> H2O}$ | $\ce{2H+}(b_2) \to \ce{2H+}(b_1)$（2） |

### 13.1.4. 可逆电极的类型

**定义 13.1.2** 电极反应能可逆地进行、交换电流足够大（[6.3.14](/6.3.14)）因而电势稳定于 Nernst 方程所给值的电极称为**可逆电极**。按参加电极反应的物质所在的相，常把它们分为三类：

1. **第一类电极**：只有一个相界面，包括金属浸在含该金属离子的溶液中构成的金属电极（$\ce{Zn^2+} \mid \ce{Zn}$）、汞齐电极（$\ce{Na+} \mid \ce{Na(Hg)}$），以及气体被吸附在惰性金属（Pt）上、与溶液中相应的离子构成的气体电极（氢电极、氧电极、卤素电极）。
2. **第二类电极**：金属表面覆盖一层该金属的难溶盐（或难溶氧化物），浸在含该难溶盐的负离子（或 $\ce{H+}$、$\ce{OH-}$）的溶液中，参加电极反应的物质分处三个相，如 $\ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$、$\ce{Cl-} \mid \ce{Hg2Cl2(s)} \mid \ce{Hg}$、$\ce{OH-} \mid \ce{HgO(s)} \mid \ce{Hg}$。
3. **氧化还原电极**（第三类电极）：惰性金属插入含同一元素两种氧化态的溶液，参加电极反应的物质都在溶液中，金属只传导电子，如 $\ce{Fe^3+}, \ce{Fe^2+} \mid \ce{Pt}$、$\ce{Cr2O7^2-}, \ce{Cr^3+}, \ce{H+} \mid \ce{Pt}$、醌–氢醌电极。

| 电极 | 电极反应（还原形式） | 说明 |
|---|---|---|
| $\ce{Cu^2+} \mid \ce{Cu}$ | $\ce{Cu^2+ + 2e- <=> Cu}$ | 第一类 |
| $\ce{Na+} \mid \ce{Na(Hg)}(a)$ | $\ce{Na+ + e- + Hg <=> Na(Hg)}(a)$ | 第一类；Na 溶于汞中，活度小于 1，不与水剧烈反应，汞齐电解是制备活泼金属的方法之一 |
| $\ce{H+} \mid \ce{H2}(p) \mid \ce{Pt}$；$\ce{OH-} \mid \ce{H2}(p) \mid \ce{Pt}$ | $\ce{2H+ + 2e- <=> H2}$；$\ce{2H2O + 2e- <=> H2 + 2OH-}$ | 第一类；酸性与碱性中的电极反应不同，$E^\circ$ 不同（$0$ 与 $-0.8277\,\mathrm{V}$） |
| $\ce{OH-} \mid \ce{O2}(p) \mid \ce{Pt}$ | $\ce{O2 + 2H2O + 4e- <=> 4OH-}$ | 第一类；$E^\circ = 0.401\,\mathrm{V}$ |
| $\ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$ | $\ce{AgCl + e- <=> Ag + Cl-}$ | 第二类；$E^\circ = 0.22233\,\mathrm{V}$ |
| $\ce{H+} \mid \ce{Ag2O(s)} \mid \ce{Ag}$ | $\ce{Ag2O + 2H+ + 2e- <=> 2Ag + H2O}$ | 第二类（难溶氧化物） |
| $\ce{Sn^4+}, \ce{Sn^2+} \mid \ce{Pt}$ | $\ce{Sn^4+ + 2e- <=> Sn^2+}$ | 氧化还原电极 |

第二类电极的意义在于：它对负离子可逆，且电势稳定、易于制备，因此常用作参比电极（13.5.2）。气体电极必须注明气体的分压；溶液中的离子浓度不能太低（一般大于 $10^{-6}$–$10^{-8}\,\mathrm{mol\,L^{-1}}$），否则交换电流太小，电势不稳定。

## 13.2. 电动势的测定

### 13.2.1. 电动势与端电压

**定义 13.2.1** 电池放电时两极之间的电势差称为电池的**端电压**，记作 $U$。

设电池的电动势为 $E_{\mathrm{cell}}$、内阻为 $R_{\mathrm{i}}$，外电路电阻为 $R_{\mathrm{o}}$，由全电路 **Ohm 定律**（[5.3.5](/5.3.5)）$E_{\mathrm{cell}} = I(R_{\mathrm{o}} + R_{\mathrm{i}})$、$U = IR_{\mathrm{o}}$，

$$
\frac{U}{E_{\mathrm{cell}}} = \frac{R_{\mathrm{o}}}{R_{\mathrm{o}} + R_{\mathrm{i}}}.
$$
只有 $R_{\mathrm{o}} \to \infty$（$I \to 0$）时 $U \to E_{\mathrm{cell}}$。实际电池放电时，端电压还因电极极化而进一步降低（[6.3.14](/6.3.14)），所以普通电压表测得的是端电压而不是电动势。

### 13.2.2. 对消法

**定义 13.2.2** 用一个电压可调的工作电源产生与待测电池电动势大小相等、方向相反的电压，使通过待测电池的电流为零（检流计指零），由此测定电动势的方法称为**对消法**（补偿法）。

经典的电位差计中，工作电池 $E_{\mathrm{w}}$ 在均匀滑线电阻 $AB$ 上形成稳定的电势降。先接入电动势已知的标准电池 $E_{\mathrm{s}}$，调节滑点到 $H$ 使检流计指零；再换成待测电池 $E_x$，调节到 $C$ 使检流计指零，则 $E_x = E_{\mathrm{s}}\cdot\overline{AC}/\overline{AH}$。平衡时待测电池中没有电流，满足可逆电池的使用条件。今天的测量多用输入阻抗 $10^{12}\,\Omega$ 以上的数字电压表或电位计，流过电池的电流小于 $10^{-12}\,\mathrm{A}$，原理相同：零电流条件不变。

电动势本来是一个正的量。为了使式 (13.1) 对任意写法的电池都成立，规定 $E_{\mathrm{cell}} = E_{\text{右}} - E_{\text{左}}$（右边电极的电极电势减去左边电极的），于是：按电池符号所写的电池反应若自发进行，$\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$，$E_{\mathrm{cell}} > 0$；若 $E_{\mathrm{cell}} < 0$，说明实际的正负极与所写的相反，所写的反应逆向自发；$E_{\mathrm{cell}} = 0$ 表示反应处于平衡，电池没有做功的本领。例如 $\ce{Zn} \mid \ce{Zn^2+} \parallel \ce{Cu^2+} \mid \ce{Cu}$ 的 $E_{\mathrm{cell}} > 0$，而 $\ce{Cu} \mid \ce{Cu^2+} \parallel \ce{Zn^2+} \mid \ce{Zn}$ 的 $E_{\mathrm{cell}} < 0$。

### 13.2.3. 标准电池

**定义 13.2.3** 电动势已知、稳定且重现性好、温度系数很小、用来校准电位差计的电池称为**标准电池**。最常用的是 Weston 标准电池：

$$
\ce{Cd(Hg)}(w_{\ce{Cd}} = 0.125) \mid \ce{CdSO4 * 8/3H2O(s)} \mid \ce{CdSO4}(\text{饱和}) \mid \ce{Hg2SO4(s)} \mid \ce{Hg(l)}.
$$

负极 $\ce{Cd(Hg) -> Cd^2+ + 2e-}$，正极 $\ce{Hg2SO4 + 2e- -> 2Hg + SO4^2-}$，电池反应 $\ce{Cd(Hg) + Hg2SO4 + 8/3H2O -> CdSO4 * 8/3H2O + 2Hg}$。$20\,^\circ\mathrm{C}$ 时电动势约 $1.0186\,\mathrm{V}$，温度系数只有约 $-4\times10^{-5}\,\mathrm{V\,K^{-1}}$。

它稳定的原因可以从 [6.3.9](/6.3.9) 的相图理解：在室温下，Cd–Hg 系统中 Cd 的质量分数在约 0.05–0.14 之间时处于液态汞齐与固溶体的两相区，两相的组成由温度固定，与总组成无关，于是镉汞齐中 Cd 的活度为定值；溶液为 $\ce{CdSO4}$ 的饱和溶液，有固相 $\ce{CdSO4 * 8/3H2O}$ 共存，其活度也为定值。电池反应中各物质的活度都恒定，电动势就是恒定的。

Weston 电池（1893）作为电压的实物标准用了将近一个世纪。1990 年起，电压的计量基准改为 Josephson 效应：超导隧道结在频率 $f$ 的微波照射下出现量子化的电压台阶 $U = nf/K_{\mathrm{J}}$；自 2019 年 SI 改用固定常数定义以来，$K_{\mathrm{J}} = 2e/h$ 是精确值，伏特由频率和基本常数直接复现。Weston 电池已退出计量，只在部分教学和老式电位差计中使用。

## 13.3. 电池热力学

### 13.3.1. Nernst 方程

对任意电池反应 $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$，**化学反应等温式**（[6.3.7](/6.3.7)）给出 $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln\prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}}$。

**定义 13.3.1** 参加电池反应的各物质都处于各自的标准态时电池的电动势称为电池的**标准电动势**，记作 $E^\circ_{\mathrm{cell}}$。由式 (13.1)，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$，它只是温度的函数。

**定理 13.3.1（Nernst 方程）** 可逆电池的电动势与参加电池反应的各物质的活度之间有

$$
E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{zF}\ln\prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}}. \tag{13.2}
$$

**证明** 设想在一个很大的电池中进行 $1\,\mathrm{mol}$ 反应，各物质的活度不变，电池放出 $zF$ 的电量。把 $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$ 与 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$ 代入化学反应等温式，两边除以 $-zF$ 即得。$\square$

这是 [6.1.11 的定理 11.5.1](/6.1.11#thm-11.5.1) 的严格形式：那里的浓度比在这里换成了活度，溶液中的物种用 $a_{\mathrm{B}} = \gamma_{\mathrm{B}}b_{\mathrm{B}}/b^\circ$，气体用 $p_{\mathrm{B}}/p^\circ$（理想气体，严格地应是逸度），纯固体、纯液体的活度为 1，稀溶液中的溶剂水近似为 1。电解质溶液中单个离子的活度不可测，在式中它们总以电中性的组合出现，可以写成 $a_\pm$（例 13.3.1）。

### 13.3.2. 电动势与反应方程式的写法

电动势是电池的强度性质，与电池反应的计量方程怎样写无关；$\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 与 $K^\circ$ 则随写法变化。以 $\ce{Pt} \mid \ce{H2}(p_1) \mid \ce{OH-} \mid \ce{O2}(p_2) \mid \ce{Pt}$ 为例：

$$
\begin{aligned}
&(1)\ \ce{H2 + 1/2O2 -> H2O}, \quad z = 2, && E_1 = E^\circ_1 - \frac{RT}{2F}\ln\frac{a(\ce{H2O})}{(p_1/p^\circ)(p_2/p^\circ)^{1/2}};\\
&(2)\ \ce{2H2 + O2 -> 2H2O}, \quad z = 4, && E_2 = E^\circ_2 - \frac{RT}{4F}\ln\frac{a(\ce{H2O})^2}{(p_1/p^\circ)^2(p_2/p^\circ)}.
\end{aligned}
$$
$\Delta_{\mathrm{r}}G_{\mathrm{m}}(2) = 2\Delta_{\mathrm{r}}G_{\mathrm{m}}(1)$，$z_2 = 2z_1$，两者之比 $E = -\Delta_{\mathrm{r}}G_{\mathrm{m}}/(zF)$ 不变：$E_1 = E_2$，$E^\circ_1 = E^\circ_2 = 1.229\,\mathrm{V}$。

但同一个总反应，如果在不同的电池中进行、电子转移的方式不同，电动势就不同。$\ce{Cu^2+ + Cu -> 2Cu+}$ 可以设计成两个电池：

$$
(1)\ \ce{Cu} \mid \ce{Cu+} \parallel \ce{Cu+}, \ce{Cu^2+} \mid \ce{Pt}\ (z = 1), \qquad (2)\ \ce{Cu} \mid \ce{Cu^2+} \parallel \ce{Cu+}, \ce{Cu^2+} \mid \ce{Pt}\ (z = 2).
$$
电池 (1) 的电极反应是 $\ce{Cu -> Cu+ + e-}$ 与 $\ce{Cu^2+ + e- -> Cu+}$；电池 (2) 是 $\ce{Cu -> Cu^2+ + 2e-}$ 与 $\ce{2Cu^2+ + 2e- -> 2Cu+}$。两者的总反应相同，$\Delta_{\mathrm{r}}G_{\mathrm{m}}$、$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 相同，放出的电功相同，但 $z_2 = 2z_1$，所以 $E^\circ_1 = 2E^\circ_2$。由 [6.1.12](/6.1.12) 的铜的元素电势图，$E^\circ_1 = 0.153 - 0.521 = -0.368\,\mathrm{V}$，$E^\circ_2 = -0.184\,\mathrm{V}$，都是负的：$\ce{Cu+}$ 在水中歧化。（若直接用表值 $E^\circ(\ce{Cu^2+}/\ce{Cu}) = 0.342\,\mathrm{V}$ 算，$E^\circ_2 = 0.153 - 0.342 = -0.189\,\mathrm{V}$；5 mV 的差别来自三个表值各自独立的测定与修约，严格的热力学要求 $E^\circ(\ce{Cu^2+}/\ce{Cu}) = [E^\circ(\ce{Cu^2+}/\ce{Cu+}) + E^\circ(\ce{Cu+}/\ce{Cu})]/2$。）

**例 13.3.1** 求 $298.15\,\mathrm{K}$ 时电池 $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{HCl}(b = 0.100\,\mathrm{mol\,kg^{-1}}) \mid \ce{Cl2}(2p^\circ) \mid \ce{Pt}$ 的电动势。已知 $0.100\,\mathrm{mol\,kg^{-1}}$ $\ce{HCl}$ 的 $\gamma_\pm = 0.796$。

**解** 电池反应 $\ce{H2}(p^\circ) + \ce{Cl2}(2p^\circ) \to \ce{2H+ + 2Cl-}$，$z = 2$，$E^\circ_{\mathrm{cell}} = E^\circ(\ce{Cl2}/\ce{Cl-}) - 0 = 1.358\,\mathrm{V}$。$a(\ce{H+})a(\ce{Cl-}) = a_\pm^2 = (\gamma_\pm b/b^\circ)^2 = 0.0796^2$，

$$
E_{\mathrm{cell}} = 1.358\,\mathrm{V} - \frac{0.05916\,\mathrm{V}}{2}\lg\frac{0.0796^4}{1\times2} = 1.358 + 0.139 = 1.497\,\mathrm{V}.
$$
若把反应写成 $\tfrac12\ce{H2} + \tfrac12\ce{Cl2 -> HCl(aq)}$，$z = 1$，$E_{\mathrm{cell}} = 1.358 - 0.05916\lg[0.0796^2/2^{1/2}]$，结果相同。若忽略活度因子，得 $1.485\,\mathrm{V}$，误差 12 mV——在电化学中这已经是很大的误差。$\square$

### 13.3.3. 标准电动势与平衡常数

由 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ = -zFE^\circ_{\mathrm{cell}}$，

$$
\ln K^\circ = \frac{zFE^\circ_{\mathrm{cell}}}{RT}, \qquad \lg K^\circ = \frac{zE^\circ_{\mathrm{cell}}}{0.05916\,\mathrm{V}}\quad(298.15\,\mathrm{K}). \tag{13.3}
$$
$E^\circ_{\mathrm{cell}}$ 与方程式写法无关，而 $z$ 与 $K^\circ$ 随写法变化：上例 (1)、(2) 中 $K^\circ_2 = (K^\circ_1)^2$。$E^\circ_{\mathrm{cell}}$ 每增大 $0.1\,\mathrm{V}$（$z = 1$），$K^\circ$ 增大约 50 倍；$z = 2$、$E^\circ_{\mathrm{cell}} = 1.1\,\mathrm{V}$ 的 Daniell 电池对应 $K^\circ \approx 10^{37}$（[6.1.11](/6.1.11)）。电动势为零时电池反应达到平衡，这时 $\prod a_{\mathrm{B}}^{\nu_{\mathrm{B}}} = K^\circ$，Nernst 方程就是"距离平衡有多远"的电学度量：$E_{\mathrm{cell}} = (RT/zF)\ln(K^\circ/Q)$。

### 13.3.4. 电动势的温度系数与反应的熵变、焓变

由 $(\partial G/\partial T)_p = -S$（[6.3.3](/6.3.3)），对式 (13.1) 求导：

**定义 13.3.2** 恒压下电池电动势随温度的变化率 $(\partial E_{\mathrm{cell}}/\partial T)_p$ 称为**电动势的温度系数**。

**定理 13.3.2** 可逆电池反应的摩尔熵变、摩尔焓变与可逆热为

$$
\Delta_{\mathrm{r}}S_{\mathrm{m}} = zF\left(\frac{\partial E_{\mathrm{cell}}}{\partial T}\right)_p, \qquad \Delta_{\mathrm{r}}H_{\mathrm{m}} = -zFE_{\mathrm{cell}} + zFT\left(\frac{\partial E_{\mathrm{cell}}}{\partial T}\right)_p, \qquad Q_{\mathrm{r}} = T\Delta_{\mathrm{r}}S_{\mathrm{m}} = zFT\left(\frac{\partial E_{\mathrm{cell}}}{\partial T}\right)_p. \tag{13.4}
$$

**证明** $\Delta_{\mathrm{r}}S_{\mathrm{m}} = -(\partial\Delta_{\mathrm{r}}G_{\mathrm{m}}/\partial T)_p = zF(\partial E_{\mathrm{cell}}/\partial T)_p$；$\Delta_{\mathrm{r}}H_{\mathrm{m}} = \Delta_{\mathrm{r}}G_{\mathrm{m}} + T\Delta_{\mathrm{r}}S_{\mathrm{m}}$；可逆过程的热 $Q_{\mathrm{r}} = T\Delta S$。第二式也就是 **Gibbs–Helmholtz 方程**（[6.3.3](/6.3.3)）用于电池。$\square$

几点说明：

- 电池中有非体积功，可逆热 $Q_{\mathrm{r}} = T\Delta_{\mathrm{r}}S_{\mathrm{m}}$ 不等于 $\Delta_{\mathrm{r}}H_{\mathrm{m}}$。由第一定律，恒压下 $\Delta_{\mathrm{r}}H_{\mathrm{m}} = Q + W'$，可逆时 $W' = -zFE_{\mathrm{cell}}$：焓的减少一部分做电功，一部分放热（或者还从环境吸热来做电功）。
- $(\partial E/\partial T)_p > 0$ 的电池可逆工作时从环境吸热（$Q_{\mathrm{r}} > 0$），升温时电动势增大；$(\partial E/\partial T)_p < 0$ 的电池放热，升温时电动势减小。吸热电池做的电功大于 $-\Delta_{\mathrm{r}}H_{\mathrm{m}}$，"热–电转换效率" $W'/\Delta_{\mathrm{r}}H_{\mathrm{m}}$ 超过 100%，这并不违反第二定律：多出的能量来自环境的热，而系统的熵增加了。
- 不含气体电极的电池，$E$–$T$ 关系在不大的温度范围内近似为直线，温度系数可以测得很精确，因此电动势法求 $\Delta_{\mathrm{r}}H_{\mathrm{m}}$ 常比量热法更准确，而且能用于难以在量热计中直接进行的反应。

**例 13.3.2** $298.15\,\mathrm{K}$ 时电池 $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{KCl}(\mathrm{aq}) \mid \ce{Hg2Cl2(s)} \mid \ce{Hg(l)}$ 的电动势为 $0.0455\,\mathrm{V}$，温度系数为 $3.38\times10^{-4}\,\mathrm{V\,K^{-1}}$。求电池反应的 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$、$\Delta_{\mathrm{r}}S_{\mathrm{m}}$、$\Delta_{\mathrm{r}}H_{\mathrm{m}}$ 与可逆热，并与热力学表比较。

**解** 左 $\ce{Ag + Cl- -> AgCl + e-}$，右 $\tfrac12\ce{Hg2Cl2 + e- -> Hg + Cl-}$，电池反应 $\ce{Ag} + \tfrac12\ce{Hg2Cl2 -> AgCl + Hg}$，$z = 1$。反应中不出现溶液中的物种，各物质都是纯固体或纯液体，$E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}}$，与 $\ce{KCl}$ 的浓度无关（$E^\circ(\ce{Hg2Cl2}/\ce{Hg}) - E^\circ(\ce{AgCl}/\ce{Ag}) = 0.26808 - 0.22233 = 0.04575\,\mathrm{V}$）。

$$
\begin{aligned}
\Delta_{\mathrm{r}}G_{\mathrm{m}} &= -96\,485 \times 0.0455\,\mathrm{J\,mol^{-1}} = -4.39\,\mathrm{kJ\,mol^{-1}},\\
\Delta_{\mathrm{r}}S_{\mathrm{m}} &= 96\,485 \times 3.38\times10^{-4}\,\mathrm{J\,mol^{-1}\,K^{-1}} = 32.6\,\mathrm{J\,mol^{-1}\,K^{-1}},\\
\Delta_{\mathrm{r}}H_{\mathrm{m}} &= -4.39 + 298.15\times32.6\times10^{-3} = 5.33\,\mathrm{kJ\,mol^{-1}}, \qquad Q_{\mathrm{r}} = 9.72\,\mathrm{kJ\,mol^{-1}}.
\end{aligned}
$$
这是一个吸热反应，却能自发进行并对外做功：驱动力来自熵增。电池可逆工作时从环境吸热 $9.72\,\mathrm{kJ}$，其中 $5.33\,\mathrm{kJ}$ 用于增加系统的焓，$4.39\,\mathrm{kJ}$ 转变为电功。由 CRC 的 $\Delta_{\mathrm{f}}H^\circ$（$\ce{AgCl}$ $-127.0$，$\ce{Hg2Cl2}$ $-265.4\,\mathrm{kJ\,mol^{-1}}$）算得 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = 5.7\,\mathrm{kJ\,mol^{-1}}$，由 $S^\circ$ 算得 $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = 33.8\,\mathrm{J\,mol^{-1}\,K^{-1}}$，在数据的不确定度内一致。$\square$

### 13.3.5. 不可逆放电的热效应

同一个反应在不同条件下进行，$\Delta_{\mathrm{r}}H_{\mathrm{m}}$ 相同，热不同。等温等压下 $Q = \Delta_{\mathrm{r}}H_{\mathrm{m}} - W'$；电池以端电压 $U$ 放电时 $W' = -zFU$，

$$
Q = \Delta_{\mathrm{r}}H_{\mathrm{m}} + zFU, \qquad U = E_{\mathrm{cell}}:\ Q = Q_{\mathrm{r}};\qquad U = 0\ (\text{短路}):\ Q = \Delta_{\mathrm{r}}H_{\mathrm{m}}.
$$

**例 13.3.3** 电池 $\ce{Pb(Hg)}(x_{\ce{Pb}} = 0.0165) \mid \ce{Pb(NO3)2}(\mathrm{aq}) \mid \ce{Pb(Hg)}(x_{\ce{Pb}} = 0.000625)$ 中的汞齐可看作**理想稀溶液**。(1) 求 $25\,^\circ\mathrm{C}$ 时的电动势；在 $25\,^\circ\mathrm{C}$、$101.325\,\mathrm{kPa}$ 下放电 $2F$ 电量时，分别求 (2) 可逆放电、(3) 短路、(4) 端电压为 $0.8E_{\mathrm{cell}}$ 时电池吸收的热。

**解** (1) 左 $\ce{Pb}(x_1) \to \ce{Pb^2+ + 2e-}$，右 $\ce{Pb^2+ + 2e- ->}\ \ce{Pb}(x_2)$，电池反应 $\ce{Pb}(x_1) \to \ce{Pb}(x_2)$，是电极浓差电池，$E^\circ_{\mathrm{cell}} = 0$，

$$
E_{\mathrm{cell}} = -\frac{RT}{2F}\ln\frac{x_2}{x_1} = 0.012\,85\,\mathrm{V}\times\ln\frac{0.0165}{0.000625} = 0.0420\,\mathrm{V}.
$$
(2) 理想稀溶液中溶质的偏摩尔焓与浓度无关，$\Delta_{\mathrm{r}}H_{\mathrm{m}} = 0$；$\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}} = -8.11\,\mathrm{kJ\,mol^{-1}}$，$Q_{\mathrm{r}} = T\Delta_{\mathrm{r}}S_{\mathrm{m}} = \Delta_{\mathrm{r}}H_{\mathrm{m}} - \Delta_{\mathrm{r}}G_{\mathrm{m}} = 8.11\,\mathrm{kJ}$（吸热）。(3) 短路时 $W' = 0$，$Q = \Delta_{\mathrm{r}}H_{\mathrm{m}} = 0$。(4) $Q = 0 + 2\times96\,485\times0.8\times0.0420\,\mathrm{J} = 6.49\,\mathrm{kJ}$（吸热）。

这个电池的驱动力完全是熵：Pb 从浓汞齐"扩散"到稀汞齐。可逆时它把从环境吸收的热全部变成电功；短路时不做功也不吸热，熵增 $27.2\,\mathrm{J\,K^{-1}}$ 全部是不可逆的熵产生。（不少教材把这里的热写成 $\Delta U - (p\Delta V + W_{\mathrm{e}})$，并以系统对外做功为正；按本站系统得到为正的约定，数值相同。）$\square$

**例 13.3.4** 可逆电动势为 $1.07\,\mathrm{V}$ 的电池放在 $20\,^\circ\mathrm{C}$ 的大恒温槽中，短路放电 $1000\,\mathrm{C}$，电池中的反应与可逆放电 $1000\,\mathrm{C}$ 时相同。求电池与恒温槽的总熵变。

**解** 短路时 $W' = 0$，电池放热 $Q = \Delta H$，恒温槽得到 $-\Delta H$，$\Delta S_{\text{槽}} = -\Delta H/T$。电池的熵变 $\Delta S$ 与过程无关，

$$
\Delta S_{\text{总}} = \Delta S - \frac{\Delta H}{T} = -\frac{\Delta G}{T} = \frac{QE_{\mathrm{cell}}}{T} = \frac{1000\,\mathrm{C}\times1.07\,\mathrm{V}}{293.15\,\mathrm{K}} = 3.65\,\mathrm{J\,K^{-1}}.
$$
要分别求出电池与恒温槽的熵变，还需要温度系数（给出 $\Delta S$）或反应焓。$\square$

## 13.4. 相间电势与电化学势

### 13.4.1. 内电势、外电势与表面电势

电动势是在两个相同金属的端子之间测得的电势差。要理解它由哪些部分组成，需要讨论一个带电粒子从一相进入另一相时的能量变化。设想把一个试探点电荷从无穷远的真空移入相 $\alpha$ 的内部。

**定义 13.4.1** 把单位正电荷从无穷远处（真空中）移到相 $\alpha$ 表面外侧附近（约 $10^{-6}\,\mathrm{m}$，已离开表面上像电荷力的作用范围）所做的电功，称为相 $\alpha$ 的**外电势** $\psi^\alpha$（Volta 电势）；从表面外侧移入相内所做的电功，称为相 $\alpha$ 的**表面电势** $\chi^\alpha$；两者之和 $\varphi^\alpha = \psi^\alpha + \chi^\alpha$ 称为相 $\alpha$ 的**内电势**（Galvani 电势）。

外电势由相所带的净电荷决定，可以测量；表面电势来自表面的定向偶极层（金属表面的电子"溢出"、水表面的定向排列），与相所带的净电荷无关，不可测量；因此内电势也不可测。（这里的 $\chi$ 与电负性同形，只在本节使用。）

### 13.4.2. 电化学势

带电物种 B（电荷数 $z_{\mathrm{B}}$）进入相 $\alpha$ 时，除了与化学组成有关的能量变化外，还要做电功 $z_{\mathrm{B}}F\varphi^\alpha$（每摩尔）。这两部分在实验上不能分开。

**定义 13.4.2** 相 $\alpha$ 中带电物种 B 的**电化学势**为

$$
\tilde\mu^\alpha_{\mathrm{B}} = \mu^\alpha_{\mathrm{B}} + z_{\mathrm{B}}F\varphi^\alpha = \mu^\alpha_{\mathrm{B}} + z_{\mathrm{B}}F\psi^\alpha + z_{\mathrm{B}}F\chi^\alpha,
$$
其中 $\mu^\alpha_{\mathrm{B}}$ 是"化学"部分（相 $\alpha$ 不带净电荷、没有外电场时 B 的化学势）。对不带电的物种，$\tilde\mu_{\mathrm{B}} = \mu_{\mathrm{B}}$。

电化学势是 [6.3.4](/6.3.4) 的化学势在有电场时的推广：组成可变的带电系统的热力学基本方程是 $\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p + \sum_{\mathrm{B}}\tilde\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$。只有 $\tilde\mu_{\mathrm{B}}$ 有确定的物理意义；把它拆成 $\mu_{\mathrm{B}}$ 与 $z_{\mathrm{B}}F\varphi$ 两部分，对同一相中的单个离子来说没有可操作的意义，这正是单个离子的活度不可测的原因（[6.3.12](/6.3.12)）。

**定理 13.4.1（电化学势判据）** 等温等压下，带电物种 B 自发地从电化学势高的相向电化学势低的相转移；两相间对 B 达到平衡的条件是 $\tilde\mu^\alpha_{\mathrm{B}} = \tilde\mu^\beta_{\mathrm{B}}$。相界面上发生电化学反应 $0 = \sum\nu_{\mathrm{B}}\mathrm{B}$（包括电子）时，平衡条件是 $\sum_{\mathrm{B}}\nu_{\mathrm{B}}\tilde\mu_{\mathrm{B}} = 0$，自发方向是 $\sum\nu_{\mathrm{B}}\tilde\mu_{\mathrm{B}} < 0$ 的方向。

**证明** 与化学势判据（[6.3.4](/6.3.4)）相同：$\mathrm{d}n$ mol B 由 $\alpha$ 进入 $\beta$ 时 $\mathrm{d}G = (\tilde\mu^\beta_{\mathrm{B}} - \tilde\mu^\alpha_{\mathrm{B}})\,\mathrm{d}n$，自发过程要求 $\mathrm{d}G < 0$，平衡时 $\mathrm{d}G = 0$。反应的情形相同。$\square$

**定义 13.4.3** 两相内电势之差 $\Delta^\beta_\alpha\varphi = \varphi^\beta - \varphi^\alpha$ 称为两相间的 **Galvani 电势差**（内电势差）；外电势之差 $\Delta^\beta_\alpha\psi = \psi^\beta - \psi^\alpha$ 称为 **Volta 电势差**（外电势差，接触电势差）。

由定理 13.4.1，若离子 B 能在两相间自由穿越并达到平衡，则 $\mu^\alpha_{\mathrm{B}} + z_{\mathrm{B}}F\varphi^\alpha = \mu^\beta_{\mathrm{B}} + z_{\mathrm{B}}F\varphi^\beta$，

$$
\Delta^\beta_\alpha\varphi = -\frac{\mu^\beta_{\mathrm{B}} - \mu^\alpha_{\mathrm{B}}}{z_{\mathrm{B}}F}. \tag{13.5}
$$
两相间的内电势差是由离子在两相中的化学势差驱动形成的：离子从化学势高的一侧穿过界面，留下的反号电荷与它形成双电层，产生的电势差恰好阻止进一步的转移。一般地，只有组成相同的两相（同种金属、同一溶液）之间的 Galvani 电势差可以测量，因为这时 $\mu^\alpha_{\mathrm{B}} = \mu^\beta_{\mathrm{B}}$，电化学势之差就是电势差。

### 13.4.3. 电动势的组成

电池 $\ce{Cu}' \mid \ce{Zn} \mid \ce{Zn^2+}(\mathrm{aq}) \parallel \ce{Cu^2+}(\mathrm{aq}) \mid \ce{Cu}$ 中，两端都是铜（左端的 $\ce{Cu}'$ 是接到 Zn 上的铜导线），测得的电动势是两端铜的内电势差 $E_{\mathrm{cell}} = \varphi^{\ce{Cu}} - \varphi^{\ce{Cu}'}$，它是电路中各相界面 Galvani 电势差的代数和：

$$
E_{\mathrm{cell}} = \Delta^{\ce{Zn}}_{\ce{Cu}'}\varphi + \Delta^{\mathrm{S}}_{\ce{Zn}}\varphi + \Delta^{\mathrm{S'}}_{\mathrm{S}}\varphi + \Delta^{\ce{Cu}}_{\mathrm{S'}}\varphi,
$$
依次是金属接界、Zn/溶液界面、液接（盐桥使之约为零）与溶液/Cu 界面的电势差。单个界面的 Galvani 电势差都不可测，但它们的和可测，而且由热力学完全确定。

用电化学势可以直接证明这一点。零电流时每个界面都处于平衡。Zn 与 $\ce{Cu}'$ 之间电子平衡：$\tilde\mu_{\mathrm{e}}(\ce{Zn}) = \tilde\mu_{\mathrm{e}}(\ce{Cu}')$；两个电极界面上反应平衡：

$$
\mu_{\ce{Zn}} = \tilde\mu_{\ce{Zn^2+}}(\mathrm{S}) + 2\tilde\mu_{\mathrm{e}}(\ce{Cu}'), \qquad \tilde\mu_{\ce{Cu^2+}}(\mathrm{S'}) + 2\tilde\mu_{\mathrm{e}}(\ce{Cu}) = \mu_{\ce{Cu}}.
$$
两式相减，并设理想盐桥使 $\varphi^{\mathrm{S}} = \varphi^{\mathrm{S'}}$，溶液中离子的 $z_{\mathrm{B}}F\varphi$ 项消去：

$$
2[\tilde\mu_{\mathrm{e}}(\ce{Cu}) - \tilde\mu_{\mathrm{e}}(\ce{Cu}')] = \mu_{\ce{Cu}} + \mu_{\ce{Zn^2+}} - \mu_{\ce{Zn}} - \mu_{\ce{Cu^2+}} = \Delta_{\mathrm{r}}G_{\mathrm{m}}.
$$
两端是同种金属，电子的化学部分相同，$\tilde\mu_{\mathrm{e}}(\ce{Cu}) - \tilde\mu_{\mathrm{e}}(\ce{Cu}') = -F(\varphi^{\ce{Cu}} - \varphi^{\ce{Cu}'}) = -FE_{\mathrm{cell}}$，于是 $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -2FE_{\mathrm{cell}}$。这就从界面平衡的角度重新得到了式 (13.1)：电动势是两端子中电子的电化学势之差（即 Fermi 能级之差，[5.5.6](/5.5.6)）除以 $-F$。

### 13.4.4. 金属接界电势

两种金属接触时，电子从**逸出功**小的金属流向逸出功大的金属，直到两边电子的电化学势相等，界面上形成双电层，两金属之间出现 Volta 电势差（接触电势差），数值约等于两者逸出功之差除以 $e$，可达零点几伏。上面的证明说明，在电池两端用同一种金属的导线引出时，这类接界电势已经包含在热力学结果中，不需要单独考虑。

接触电势本身不能用电压表测出：在温度均匀的闭合回路中，各接界的电势差之和为零。热电偶的电动势来自温度梯度引起的 **Seebeck 效应**（[5.3.5](/5.3.5)）——两种金属中电子的输运对温度梯度的响应不同，而不是来自接触电势本身；两个接点处在不同温度时回路中才有净电动势，所以热电偶可以测温。

### 13.4.5. 电极与溶液的界面

电极与溶液接触时，界面两侧形成**双电层**（[6.1.11](/6.1.11)）：金属一侧是表面上的过剩电荷（厚度不到 0.1 nm），溶液一侧由紧贴电极的紧密层（约 0.3–0.5 nm，含吸附的离子和定向的水分子）和向溶液内部散开的扩散层组成。扩散层的厚度就是 Debye 长度 $\lambda_{\mathrm{D}}$（[6.3.12](/6.3.12)，$0.1\,\mathrm{mol\,kg^{-1}}$ 时约 1 nm）。紧密层中的电势差可达 1 V，场强达 $10^9$–$10^{10}\,\mathrm{V\,m^{-1}}$，比空气的击穿场强大三个数量级，这是电极能以极高的效率改变反应活化能的原因（[6.3.14](/6.3.14)）。双电层内的溶液不呈电中性；只有在零电荷电势下，电极表面不带过剩电荷。双电层的结构模型（Helmholtz、Gouy–Chapman、Stern）与胶体的稳定性密切相关，在 [6.3.21](/6.3.21) 系统讨论。

### 13.4.6. 液接电势

**液接电势**（[6.1.11](/6.1.11)）产生于两种组成或浓度不同的电解质溶液的接界处。以 $\ce{HCl}(b_1) \mid \ce{HCl}(b_2)$（$b_1 > b_2$）为例：$\ce{H+}$ 与 $\ce{Cl-}$ 都从浓的一侧向稀的一侧扩散，$\ce{H+}$ 快，稀的一侧先带正电；形成的电场使 $\ce{H+}$ 减速、$\ce{Cl-}$ 加速，很快达到两种离子以相同速率扩散的稳态，界面上的电势差稳定下来，记作 $E_{\mathrm{l}} = \varphi_{\text{右}} - \varphi_{\text{左}}$。这是一个不可逆的稳态，两种溶液长时间接触后浓度趋于一致，液接电势才消失。

液接电势可以在零电流的近似下计算。电池中有 $1\,\mathrm{mol}$ 正电荷自左向右通过界面时，界面上有 $t_+/z_+$ mol 正离子从左（1）迁到右（2），$t_-/\lvert z_-\rvert$ mol 负离子从右迁到左，过程的 Gibbs 自由能变化为

$$
\Delta G = \frac{t_+}{z_+}RT\ln\frac{a_+(2)}{a_+(1)} + \frac{t_-}{\lvert z_-\rvert}RT\ln\frac{a_-(1)}{a_-(2)}.
$$
同种电解质的两种浓度，近似取两侧单个离子的活度比都等于 $a_\pm(2)/a_\pm(1)$，再由 $\Delta G = -FE_{\mathrm{l}}$，

$$
E_{\mathrm{l}} = \left(\frac{t_+}{z_+} - \frac{t_-}{\lvert z_-\rvert}\right)\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}, \qquad \text{1-1 型：}\ E_{\mathrm{l}} = (t_+ - t_-)\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}. \tag{13.6}
$$
其中 $t_\pm$ 取界面附近（两种浓度的平均）的迁移数。正离子较快（$t_+ > t_-$）时，浓溶液在左边则 $E_{\mathrm{l}} > 0$，与上面的定性分析一致。

**例 13.4.1** 估算 $25\,^\circ\mathrm{C}$ 时 $\ce{HCl}(0.100\,\mathrm{mol\,kg^{-1}}) \mid \ce{HCl}(0.0100\,\mathrm{mol\,kg^{-1}})$ 与同浓度的 $\ce{KCl}$ 溶液接界的液接电势。$t(\ce{H+}) = 0.83$，$t(\ce{K+}) = 0.49$；两种电解质的 $\gamma_\pm$ 都近似取 [6.3.12](/6.3.12) 表中 $\ce{HCl}$ 的值。

**解** $a_\pm(1)/a_\pm(2) = (0.796\times0.100)/(0.905\times0.0100) = 8.80$，$\lg 8.80 = 0.944$。

$$
E_{\mathrm{l}}(\ce{HCl}) = (0.83 - 0.17)\times0.05916\,\mathrm{V}\times0.944 = 0.037\,\mathrm{V}, \qquad E_{\mathrm{l}}(\ce{KCl}) = (0.49 - 0.51)\times0.05916\times0.944\,\mathrm{V} \approx -1\,\mathrm{mV}.
$$
$\ce{HCl}$ 溶液之间的液接电势达到 37 mV，而 $\ce{KCl}$ 由于 $t_+ \approx t_-$，液接电势只有约 1 mV。$\square$

盐桥的作用正基于这一点：用饱和（约 $4.2\,\mathrm{mol\,L^{-1}}$）$\ce{KCl}$ 琼脂凝胶连接两种溶液，形成两个液接界面，界面上的迁移主要由大量的 $\ce{K+}$ 与 $\ce{Cl-}$ 承担，两者迁移数接近，每个界面的液接电势都很小，而且两者符号相反，总和一般在 1–2 mV 以下。对盐桥的要求是：正、负离子迁移数接近，浓度远高于被连接的溶液，不与溶液中的物质反应（含 $\ce{Ag+}$ 的溶液改用 $\ce{KNO3}$ 或 $\ce{NH4NO3}$ 盐桥）。

## 13.5. 电极电势

### 13.5.1. 氢标还原电极电势

单个电极的 Galvani 电势差不可测，所以电极电势只能定义为相对值：以**标准氢电极** $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+}(a = 1)$ 为左边的电极，待测电极为右边的电极组成电池，该电池的电动势就是待测电极的**电极电势** $E$（[6.1.11 的定义 11.4.4](/6.1.11#def-11.4.4)，这里活度代替了浓度）。按这一约定，待测电极上发生的是还原反应，所以电极电势是"还原电势"：$E$ 越高，电对的氧化型越容易被还原；任何温度下 $E^\circ(\ce{H+}/\ce{H2}) = 0$。

**定理 13.5.1** 电极反应 $\text{氧化型} + z\ce{e-} \to \text{还原型}$，即 $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B} - z\ce{e-}$（还原型的 $\nu_{\mathrm{B}} > 0$），的电极电势为

$$
E = E^\circ - \frac{RT}{zF}\ln\prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}} = E^\circ + \frac{RT}{zF}\ln\frac{a_{\text{氧化型}}}{a_{\text{还原型}}}. \tag{13.7}
$$

**证明** 电池 $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+}(a = 1) \parallel \text{待测电极}$ 的反应为 $\text{氧化型} + \tfrac z2\ce{H2} \to \text{还原型} + z\ce{H+}$，其中 $a(\ce{H+}) = 1$、$p(\ce{H2}) = p^\circ$，代入式 (13.2) 即得。$\square$

例如 $\ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$：$E = E^\circ(\ce{AgCl}/\ce{Ag}) - \frac{RT}{F}\ln a(\ce{Cl-})$。电池的标准电动势 $E^\circ_{\mathrm{cell}} = E^\circ_{\text{右}} - E^\circ_{\text{左}}$，$E^\circ$ 只是温度的函数，$298.15\,\mathrm{K}$ 的值见 [6.1.11](/6.1.11) 的表。

标准氢电极要求 $\ce{H+}$ 的活度恰为 1，例如 $1.184\,\mathrm{mol\,kg^{-1}}$ 的 $\ce{HCl}$（$\gamma_\pm \approx 0.845$）；它的缺点是制备和使用要求很严格（纯 $\ce{H2}$、铂黑易中毒），电势不够稳定，所以日常测量用参比电极。

### 13.5.2. 参比电极

常用的**参比电极**都是第二类电极，电势只取决于 $\ce{Cl-}$ 的活度：

| 参比电极（$25\,^\circ\mathrm{C}$） | $E$ / V（vs SHE） |
|---|---|
| **甘汞电极** $\ce{Hg} \mid \ce{Hg2Cl2(s)} \mid \ce{KCl}(0.1\,\mathrm{mol\,L^{-1}})$ | 0.3337 |
| 甘汞电极，$\ce{KCl}(1\,\mathrm{mol\,L^{-1}})$ | 0.2801 |
| 饱和甘汞电极（SCE） | 0.2412 |
| $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{KCl}$（饱和） | 0.197 |
| $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{Cl-}(a = 1)$ | 0.22233 |

（$E^\circ(\ce{Hg2Cl2}/\ce{Hg}) = 0.26808\,\mathrm{V}$。）饱和甘汞电极制备简单、电势稳定可靠，曾是实验室中用得最多的参比电极；含汞，现在多被 $\ce{Ag}/\ce{AgCl}$ 电极取代。生物与医学中的微电极几乎都用 $\ce{Ag}/\ce{AgCl}$。

### 13.5.3. 由电极电势计算电动势

计算电动势有三种等价的方法：由 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$（$E = -\Delta_{\mathrm{r}}G_{\mathrm{m}}/zF$）；由电池反应的 Nernst 方程 (13.2)；由两个电极电势 $E_{\mathrm{cell}} = E_{\text{右}} - E_{\text{左}}$，每个电极电势都按还原反应用式 (13.7) 计算。最后一种方法的依据是 Gibbs 自由能的加和：电池反应 = 右电极的还原反应 − 左电极的还原反应，$\Delta_{\mathrm{r}}G_{\mathrm{m}} = (-zFE_{\text{右}}) - (-zFE_{\text{左}})$。

**例 13.5.1** 用两种方法写出 $\ce{Zn} \mid \ce{Zn^2+}(a_1) \parallel \ce{Cu^2+}(a_2) \mid \ce{Cu}$ 的电动势。

**解** 方法一：$E_{\mathrm{cell}} = \left[E^\circ(\ce{Cu^2+}/\ce{Cu}) + \frac{RT}{2F}\ln a_2\right] - \left[E^\circ(\ce{Zn^2+}/\ce{Zn}) + \frac{RT}{2F}\ln a_1\right]$。方法二：电池反应 $\ce{Zn + Cu^2+ -> Zn^2+ + Cu}$，$E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{2F}\ln\frac{a_1}{a_2}$，$E^\circ_{\mathrm{cell}} = 0.342 - (-0.762) = 1.104\,\mathrm{V}$。两式相同。$\square$

相互关联的电对，其标准电极电势不能直接加减，而要按 $\Delta_{\mathrm{r}}G^\circ = -zFE^\circ$ 加减（[6.1.12 的定理 12.2.1](/6.1.12#thm-12.2.1)）：$E^\circ$ 是强度量，$zE^\circ$ 才可以相加。

## 13.6. 电池的分类与设计

### 13.6.1. 化学电池与浓差电池

| 类型 | 电池反应 | 例 | 电动势 |
|---|---|---|---|
| 无液接的化学电池（单液电池） | 化学变化 | $\ce{Zn} \mid \ce{ZnCl2}(b) \mid \ce{AgCl(s)} \mid \ce{Ag}$ | $E^\circ - \frac{RT}{2F}\ln a(\ce{ZnCl2})$，$a(\ce{ZnCl2}) = a_\pm^3$ |
| 有液接的化学电池 | 化学变化 | $\ce{Zn} \mid \ce{ZnSO4} \vdots \ce{CuSO4} \mid \ce{Cu}$ | 计算值 + 液接电势；常用盐桥消除 |
| 电极浓差电池 | 电极物质由一种浓度（分压）转移到另一种 | $\ce{Pt} \mid \ce{H2}(p_1) \mid \ce{HCl} \mid \ce{H2}(p_2) \mid \ce{Pt}$；汞齐浓差电池（例 13.3.3） | $E^\circ = 0$，$E = \frac{RT}{2F}\ln\frac{p_1}{p_2}$ |
| 电解质浓差电池（无迁移） | 电解质由一种浓度转移到另一种 | 两个单液电池背靠背：$\ce{Ag} \mid \ce{AgCl} \mid \ce{HCl}(b_1) \mid \ce{H2} \mid \ce{Pt} \mid \ce{H2} \mid \ce{HCl}(b_2) \mid \ce{AgCl} \mid \ce{Ag}$ | $\frac{2RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}$ |
| 电解质浓差电池（有迁移） | 同上，经液接迁移 | $\ce{Ag} \mid \ce{AgCl} \mid \ce{HCl}(b_1) \vdots \ce{HCl}(b_2) \mid \ce{AgCl} \mid \ce{Ag}$ | $2t_+\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}$（13.7.5） |

浓差电池（[6.1.11 的定义 11.5.1](/6.1.11#def-11.5.1)）的 $E^\circ_{\mathrm{cell}} = 0$，驱动力完全是物质从高活度向低活度的转移，即混合熵。例如 $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{HCl}(\mathrm{aq}) \mid \ce{H2}(0.1p^\circ) \mid \ce{Pt}$ 的电池反应 $\ce{H2}(p^\circ) \to \ce{H2}(0.1p^\circ)$，$E_{\mathrm{cell}} = \frac{RT}{2F}\ln10 = 0.0296\,\mathrm{V}$。电解质浓差电池若不用盐桥，测得的电动势比按电极反应计算的值多出液接电势：前面计算电动势的方法只适用于可逆电池。

### 13.6.2. 由反应设计电池

把一个给定的反应设计成电池的步骤：(1) 找出反应中被氧化与被还原的物种（没有价态变化的反应，在两边加上同一种物质，构造出氧化与还原两个半反应）；(2) 氧化的一对作左边电极，还原的一对作右边电极；(3) 写出电池符号，再由电池写出电池反应，检查是否与原反应一致。

| 反应 | 电池 |
|---|---|
| $\ce{H2 + Cl2 -> 2HCl(aq)}$ | $\ce{Pt} \mid \ce{H2} \mid \ce{HCl}(\mathrm{aq}) \mid \ce{Cl2} \mid \ce{Pt}$ |
| $\ce{Zn + 2Cu^2+ -> Zn^2+ + 2Cu+}$ | $\ce{Zn} \mid \ce{Zn^2+} \parallel \ce{Cu^2+}, \ce{Cu+} \mid \ce{Pt}$ |
| $\ce{AgCl(s) + I- -> AgI(s) + Cl-}$（两边加 Ag：$\ce{Ag + I- -> AgI + e-}$，$\ce{AgCl + e- -> Ag + Cl-}$） | $\ce{Ag} \mid \ce{AgI(s)} \mid \ce{I-} \parallel \ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$ |
| $\ce{Ag+ + Cl- -> AgCl(s)}$ | $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{Cl-} \parallel \ce{Ag+} \mid \ce{Ag}$ |
| $\ce{H2O -> H+ + OH-}$（两边加 $\tfrac12\ce{H2}$） | $\ce{Pt} \mid \ce{H2}(p) \mid \ce{H+} \parallel \ce{OH-} \mid \ce{H2}(p) \mid \ce{Pt}$ |
| $\ce{HgO(s) -> Hg(l) + 1/2O2}$ | $\ce{Pt} \mid \ce{O2}(p) \mid \ce{NaOH}(\mathrm{aq}) \mid \ce{HgO(s)} \mid \ce{Hg}$ 的逆向 |

最后一行可以用来测 $\ce{HgO}$ 的分解压：电池 $\ce{Pt} \mid \ce{O2} \mid \ce{NaOH}(\mathrm{aq}) \mid \ce{HgO(s)} \mid \ce{Hg}$ 的两个电极都对 $\ce{OH-}$ 可逆（$\ce{O2 + 2H2O + 4e- -> 4OH-}$，$\ce{HgO + H2O + 2e- -> Hg + 2OH-}$），电池反应 $\ce{Hg + 1/2O2 -> HgO}$ 中不出现溶液的物种，$E$ 与碱的浓度无关；在 $\ce{H2SO4}$ 中 $\ce{HgO}$ 会溶解，在纯水中导电性太差，都不合适。

## 13.7. 电动势法的应用

**定义 13.7.1** 设计适当的可逆电池，精确测量其电动势，由此求得热力学量、平衡常数、活度因子、pH 等的方法称为**电动势法**（电势法）。

电动势法的优点是精度高，可以测得非常小或非常大的平衡常数；局限是只适用于能设计成可逆电池的反应。一般程序是：设计电池，制备电池并测量 $E_{\mathrm{cell}}$，由 $E_{\mathrm{cell}}$ 计算待求的量。

### 13.7.1. 平衡常数

由式 (13.3)，测得或查得 $E^\circ_{\mathrm{cell}}$ 即得 $K^\circ$。

**例 13.7.1** 由标准电极电势求 $25\,^\circ\mathrm{C}$ 时水的离子积与 $\ce{AgCl}$ 的溶度积。

**解** (1) 电池 $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+} \parallel \ce{OH-} \mid \ce{H2}(p^\circ) \mid \ce{Pt}$，右 $\ce{H2O + e- -> 1/2H2 + OH-}$，左 $\tfrac12\ce{H2 -> H+ + e-}$，电池反应 $\ce{H2O -> H+ + OH-}$，$z = 1$，$E^\circ_{\mathrm{cell}} = E^\circ(\ce{H2O}/\ce{H2}, \ce{OH-}) - 0 = -0.8277\,\mathrm{V}$，

$$
K_{\mathrm{w}} = \exp\frac{FE^\circ_{\mathrm{cell}}}{RT} = \exp\left(-\frac{0.8277}{0.025\,693}\right) = \exp(-32.22) = 1.02\times10^{-14}.
$$
(2) 电池 $\ce{Ag} \mid \ce{Ag+} \parallel \ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$，电池反应 $\ce{AgCl -> Ag+ + Cl-}$，$E^\circ_{\mathrm{cell}} = 0.22233 - 0.7996 = -0.5773\,\mathrm{V}$，$K_{\mathrm{sp}} = \exp(-0.5773/0.025\,693) = 1.75\times10^{-10}$，与 [6.1.10](/6.1.10) 的 $1.8\times10^{-10}$ 一致。注意设计的电池中只能出现 $\ce{AgCl}$ 的溶解平衡，在 $\ce{Ag} \mid \ce{AgCl} \mid \ce{HCl} \mid \ce{Cl2} \mid \ce{Pt}$ 之类的电池中，电池反应是 $\ce{AgCl}$ 的生成，得到的是 $\Delta_{\mathrm{f}}G^\circ(\ce{AgCl})$。$\square$

### 13.7.2. 反应的熵变与焓变

由定理 13.3.2，在几个温度下测量 $E_{\mathrm{cell}}$，求出温度系数，即得 $\Delta_{\mathrm{r}}S_{\mathrm{m}}$ 与 $\Delta_{\mathrm{r}}H_{\mathrm{m}}$（例 13.3.2）。与量热法相比，电动势法测的是平衡性质，不受反应速率的限制，精度常更高；同一组数据还给出 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$，三者自洽。

### 13.7.3. 平均活度因子

在电池反应只涉及一种电解质的单液电池中，电动势直接给出该电解质的平均活度。最经典的是 Harned 电池

$$
\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{HCl}(b) \mid \ce{AgCl(s)} \mid \ce{Ag},
$$
电池反应 $\tfrac12\ce{H2 + AgCl -> Ag + H+ + Cl-}$，$z = 1$，

$$
E_{\mathrm{cell}} = E^\circ(\ce{AgCl}/\ce{Ag}) - \frac{RT}{F}\ln[a(\ce{H+})a(\ce{Cl-})] = E^\circ(\ce{AgCl}/\ce{Ag}) - \frac{2RT}{F}\ln\frac{\gamma_\pm b}{b^\circ}. \tag{13.8}
$$
已知 $E^\circ$ 时，测出 $E_{\mathrm{cell}}$ 就得到 $\gamma_\pm$。同理，$\ce{Cu} \mid \ce{CuCl2}(b) \mid \text{甘汞电极}$ 的电池反应是 $\ce{Cu + Hg2Cl2 -> Cu^2+ + 2Cl- + 2Hg}$，$E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{2F}\ln[4\gamma_\pm^3(b/b^\circ)^3]$，由此求 $\ce{CuCl2}$ 的 $\gamma_\pm$。

**例 13.7.2** $25\,^\circ\mathrm{C}$ 时 Harned 电池中 $b = 0.0100\,\mathrm{mol\,kg^{-1}}$，测得 $E_{\mathrm{cell}} = 0.4640\,\mathrm{V}$，求 $\gamma_\pm$。

**解** 由式 (13.8)，$\lg(\gamma_\pm b/b^\circ) = (0.22233 - 0.4640)/(2\times0.05916) = -2.0425$，$\gamma_\pm b/b^\circ = 9.07\times10^{-3}$，$\gamma_\pm = 0.907$（表值 0.905）。$\square$

### 13.7.4. 标准电极电势的测定

$E^\circ$ 不能直接测量：标准态的离子溶液是假想态。办法是测量一系列稀溶液的电动势，外推到无限稀。把式 (13.8) 改写成

$$
E' \equiv E_{\mathrm{cell}} + \frac{2RT}{F}\ln\frac{b}{b^\circ} = E^\circ - \frac{2RT}{F}\ln\gamma_\pm.
$$
左边全部可测，$b \to 0$ 时 $\gamma_\pm \to 1$，$E' \to E^\circ$。但 $E'$ 对 $b$ 作图时，曲线在 $b \to 0$ 处斜率无穷大，无法准确外推。由 Debye–Hückel 极限公式（[6.3.12 的定理 12.7.1](/6.3.12#thm-12.7.1)），稀溶液中 $\ln\gamma_\pm = -A\ln10\sqrt{b/b^\circ}$，于是

$$
E' = E^\circ + \frac{2RT\ln10}{F}A\sqrt{b/b^\circ} = E^\circ + 0.0602\,\mathrm{V}\times\sqrt{b/b^\circ},
$$
$E'$ 对 $\sqrt b$ 是直线，斜率由理论给出，外推的准确度高——这就是习惯上对 $\sqrt b$ 作图的原因。实际处理中用扩展的 Debye–Hückel 式加一个线性项作最小二乘拟合，Harned 与 Ehlers（1932–1933）由此得到 $E^\circ(\ce{AgCl}/\ce{Ag}) = 0.2224\,\mathrm{V}$，与现行 CRC 值 $0.22233\,\mathrm{V}$（13.1.4 与 13.5.2 节的表）相差不到 $0.1\,\mathrm{mV}$。所有离子的标准热力学函数最终都依赖这样的外推。

![用 Harned 电池 Pt | H₂ | HCl(b) | AgCl | Ag 测定 E°(AgCl/Ag)（25 °C，由 CRC 的 HCl 平均活度因子反算的电动势）。左：电动势随 HCl 稀释而升高；右：E' = E + (2RT/F)ln(b/b°) 对 √b 作图，稀溶液中趋于 Debye–Hückel 极限斜率（虚线），扩展式的最小二乘拟合外推到 b → 0 得 0.2223 V](./plots/harned-extrapolation.py)

### 13.7.5. 迁移数的测定

比较同一对浓度下有迁移与无迁移的电解质浓差电池。无迁移的电池（13.6.1 表中第四行）的总变化是 $1\,\mathrm{mol}$ $\ce{HCl}$ 从 $b_1$ 转移到 $b_2$，$E_{\text{无}} = \frac{2RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}$。有迁移的电池 $\ce{Ag} \mid \ce{AgCl} \mid \ce{HCl}(b_1) \vdots \ce{HCl}(b_2) \mid \ce{AgCl} \mid \ce{Ag}$ 中，两个电极对 $\ce{Cl-}$ 可逆，电极反应使 $1\,\mathrm{mol}$ $\ce{Cl-}$ 从左到右"转移"，贡献 $\frac{RT}{F}\ln\frac{a_-(1)}{a_-(2)}$；加上式 (13.6) 的液接电势，

$$
E_{\text{有}} = \frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}\left[1 + (t_+ - t_-)\right] = 2t_+\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}, \qquad t_+ = \frac{E_{\text{有}}}{E_{\text{无}}}.
$$
物理意义：电流通过液接时，只有 $t_+$ 的电量由 $\ce{H+}$ 携带向右，净结果是 $t_+$ mol $\ce{HCl}$ 由左转移到右。这是测迁移数的第三种方法（另两种见 [6.3.12](/6.3.12)）。

### 13.7.6. pH 的测定

**定义 13.7.2** 电极电势随溶液中某种离子的活度按 Nernst 方程变化、用来测定该离子活度的电极称为**指示电极**。测量时它与参比电极组成电池。

**pH** 的定义 $\mathrm{pH} = -\lg a(\ce{H+})$ 涉及单个离子的活度，不能由热力学严格测定。实际使用的是 IUPAC 的操作定义：用 $\ce{H+}$ 指示电极与参比电极组成电池，先后测量待测溶液 X 与 pH 已知的标准缓冲溶液 S，

$$
\mathrm{pH(X)} = \mathrm{pH(S)} - \frac{E_{\mathrm{X}} - E_{\mathrm{S}}}{RT\ln10/F},
$$
其中 $E$ 是"指示电极 − 参比电极"的电动势。标准缓冲溶液的 pH 由无液接的 Harned 型电池测定，并按约定（Bates–Guggenheim 约定）用 Debye–Hückel 公式估计单个 $\ce{Cl-}$ 的活度因子；$25\,^\circ\mathrm{C}$ 时 $0.05\,\mathrm{mol\,kg^{-1}}$ 邻苯二甲酸氢钾为 4.005，等摩尔磷酸盐（各 $0.025\,\mathrm{mol\,kg^{-1}}$）为 6.865，$0.01\,\mathrm{mol\,kg^{-1}}$ 硼砂为 9.180。

指示电极最早用氢电极：$\ce{Pt} \mid \ce{H2}(p^\circ) \mid \text{待测溶液} \parallel \text{饱和甘汞电极}$，$E_{\mathrm{cell}} = 0.2412\,\mathrm{V} + 0.05916\,\mathrm{V}\times\mathrm{pH}$（$25\,^\circ\mathrm{C}$，忽略液接电势）。氢电极准确，但需要纯氢气，铂易中毒，不能用于含氧化剂的溶液。今天几乎全部用玻璃电极（13.9.3）。

## 13.8. 电势–pH 图

### 13.8.1. 线的三种类型

**电势–pH 图**（Pourbaix 图，[6.1.12 的定义 12.3.1](/6.1.12#def-12.3.1)）把一个元素在水中的各种物种之间的平衡画在 $E$–pH 平面上，每条线是一个平衡在给定温度与给定的其他物种活度下的位置，每个区域是某一物种的稳定区。M. Pourbaix 在 1940–1960 年代为几乎所有元素画出了这种图，它是腐蚀、湿法冶金和地球化学的基本工具。线按所涉及的反应分为三类：

| 反应 | 线 | 例 |
|---|---|---|
| 氧化还原反应，无 $\ce{H+}$（$\ce{OH-}$）参加 | 水平线，$E$ 与 pH 无关 | $\ce{Fe^3+ + e- <=> Fe^2+}$ |
| 非氧化还原反应，有 $\ce{H+}$ 参加 | 垂直线，pH 一定（与 $E$ 无关） | $\ce{Fe2O3 + 6H+ <=> 2Fe^3+ + 3H2O}$ |
| 氧化还原反应，有 $\ce{H+}$ 参加 | 斜线，斜率 $-0.05916\,m/z\,\mathrm{V}$ | $\ce{Fe2O3 + 6H+ + 2e- <=> 2Fe^2+ + 3H2O}$ |

对 $\text{氧化型} + m\ce{H+} + z\ce{e-} \to \text{还原型}$，$E = E^\circ - \frac{0.05916\,\mathrm{V}}{z}\lg\frac{a_{\text{还原型}}}{a_{\text{氧化型}}} - \frac{0.05916\,\mathrm{V}\cdot m}{z}\mathrm{pH}$。除垂直线外，线上方是氧化型的稳定区，下方是还原型的稳定区；垂直线左侧是溶解的（酸性）形态，右侧是沉淀（碱性）形态。水的稳定区（$p = p^\circ$ 时的 a 线 $E = -0.0592\,\mathrm{pH}$ 与 b 线 $E = 1.229 - 0.0592\,\mathrm{pH}$，[6.1.12](/6.1.12)）是最基本的一张图，其他电势–pH 图都把这两条线画上。

### 13.8.2. Fe–H₂O 系统

取 $298.15\,\mathrm{K}$，溶液中铁物种的活度为 $10^{-6}$（腐蚀科学中习惯以此作为"不溶"的界限），考虑 Fe、$\ce{Fe^2+}$、$\ce{Fe^3+}$、赤铁矿 $\ce{Fe2O3}$ 与磁铁矿 $\ce{Fe3O4}$。数据：$E^\circ(\ce{Fe^2+}/\ce{Fe}) = -0.447\,\mathrm{V}$、$E^\circ(\ce{Fe^3+}/\ce{Fe^2+}) = 0.771\,\mathrm{V}$（CRC 标准电极电势表，与 [6.1.11](/6.1.11) 相同），由它们换算得 $\Delta_{\mathrm{f}}G^\circ(\ce{Fe^2+}) = -86.3$、$\Delta_{\mathrm{f}}G^\circ(\ce{Fe^3+}) = -11.9\,\mathrm{kJ\,mol^{-1}}$；$\Delta_{\mathrm{f}}G^\circ(\ce{Fe2O3}) = -742.2$、$\Delta_{\mathrm{f}}G^\circ(\ce{Fe3O4}) = -1015.4$、$\Delta_{\mathrm{f}}G^\circ(\ce{H2O, l}) = -237.1\,\mathrm{kJ\,mol^{-1}}$（CRC 热力学表）。

$$
\begin{aligned}
&\text{c}\quad \ce{Fe2O3 + 6H+ <=> 2Fe^3+ + 3H2O}, && \Delta_{\mathrm{r}}G^\circ = 7.2\,\mathrm{kJ\,mol^{-1}},\ \lg K^\circ = -1.26,\ \mathrm{pH} = \tfrac16(\lg K^\circ - 2\lg a) = 1.79;\\
&\text{d}\quad \ce{Fe^3+ + e- <=> Fe^2+}, && E = 0.771\,\mathrm{V};\\
&\text{e}\quad \ce{Fe^2+ + 2e- <=> Fe}, && E = -0.447 + 0.02958\lg10^{-6} = -0.624\,\mathrm{V};\\
&\text{f}\quad \ce{Fe2O3 + 6H+ + 2e- <=> 2Fe^2+ + 3H2O}, && E^\circ = 0.734\,\mathrm{V},\ E = 1.089 - 0.1775\,\mathrm{pH};\\
&\text{g}\quad \ce{Fe3O4 + 8H+ + 2e- <=> 3Fe^2+ + 4H2O}, && E^\circ = 0.994\,\mathrm{V},\ E = 1.526 - 0.2366\,\mathrm{pH};\\
&\text{h}\quad \ce{3Fe2O3 + 2H+ + 2e- <=> 2Fe3O4 + H2O}, && E = 0.214 - 0.0592\,\mathrm{pH};\\
&\text{i}\quad \ce{Fe3O4 + 8H+ + 8e- <=> 3Fe + 4H2O}, && E = -0.087 - 0.0592\,\mathrm{pH}.
\end{aligned}
$$
线 d、f 与 c 交于 pH 1.79；f、g、h 交于 pH 7.40；e、g、i 交于 pH 9.09。因为所有的线都由同一组 Gibbs 自由能算出，交点自动一致（例如 f 在 pH 1.79 处恰好等于 0.771 V）。

不少教材中的数值（c 线 pH 1.76，f 线 $1.083 - 0.1773\,\mathrm{pH}$，e 线 $-0.618\,\mathrm{V}$）来自旧的 $E^\circ(\ce{Fe^2+}/\ce{Fe}) = -0.440\,\mathrm{V}$ 等数据，与现行 CRC 值不符，这里全部按现行值计算；简化的图只考虑 $\ce{Fe2O3}$，加上 $\ce{Fe3O4}$ 后，中性到碱性区出现一个磁铁矿的窄带。另需说明，CRC 热力学表的 $\Delta_{\mathrm{f}}G^\circ(\ce{Fe^2+}) = -78.9\,\mathrm{kJ\,mol^{-1}}$ 对应 $E^\circ = -0.41\,\mathrm{V}$，与 $E^\circ$ 表的 $-0.447\,\mathrm{V}$ 不一致（这是铁的热力学数据中一个著名的分歧）；这里统一以 $E^\circ$ 表为准，图的结构不受影响，e 线约移动 40 mV。在 pH 13 以上还应考虑 $\ce{HFeO2-}$ 等可溶的羟基配离子，图中从略。

![298.15 K 时 Fe–H₂O 系统的电势–pH 图（溶液中铁物种活度 10⁻⁶，由 CRC 的 E° 与 ΔfG° 计算）：Fe 的稳定区是免蚀区，Fe²⁺ 与 Fe³⁺ 的稳定区是腐蚀区，Fe₂O₃ 与 Fe₃O₄ 的稳定区是钝化区；虚线 a、b 是水的稳定区边界](./plots/fe-pourbaix.py)

### 13.8.3. 电势–pH 图的应用与局限

电势–pH 图是电化学的平衡图，作用与相图相同：一张图同时给出各物种在一定条件下的相对稳定性，由此判断它们相互转化的可能性。规律是：两条线中，上方线的氧化型与下方线的还原型不能稳定共存，必然发生反应 $(\text{氧化型})_{\text{上}} + (\text{还原型})_{\text{下}} \to (\text{氧化型})_{\text{下}} + (\text{还原型})_{\text{上}}$，因为上方电对的电极电势较高。

对铁，图把 $E$–pH 平面分成三类区域：

- 免蚀区（Fe 稳定）：铁不会腐蚀。Fe 的稳定区整个在 a 线下方，说明铁在任何 pH 的水中都不是热力学稳定的，会被 $\ce{H+}$ 或水氧化。
- 腐蚀区（$\ce{Fe^2+}$、$\ce{Fe^3+}$ 稳定）：铁溶解。在酸性溶液中，Fe 与 $\ce{H+}$/$\ce{H2}$（a 线）组合，析氢腐蚀；在中性含氧水中，b 线远在 Fe 的稳定区之上，$\ce{O2}$ 把 Fe 氧化为 $\ce{Fe^2+}$，继而氧化为 $\ce{Fe2O3}$（铁锈的主要成分是水合氧化物 $\ce{FeO(OH)}$，图中以 $\ce{Fe2O3}$ 代表）。
- 钝化区（$\ce{Fe2O3}$、$\ce{Fe3O4}$ 稳定）：表面生成致密的氧化物膜时，金属被保护（**钝化**）。

由此可以读出三种电化学保护的思路：把电势降到免蚀区（阴极保护与牺牲阳极保护）、把电势升到钝化区（阳极保护）、调节 pH 使系统进入钝化区（如在锅炉水中加碱），见 [6.3.14](/6.3.14)。

电势–pH 图的局限：它只给出热力学上的可能性，不给出速率；钝化区中的氧化物膜是否真能保护金属取决于膜的结构（$\ce{Fe2O3}$ 膜疏松多孔，保护性不好；铬的氧化物膜致密，所以不锈钢耐蚀）；图中的线依赖于所设的离子活度、温度和所考虑的物种，有配体（$\ce{Cl-}$、$\ce{NH3}$）时图会显著改变。

## 13.9. 膜电势与离子选择性电极

### 13.9.1. 膜平衡与膜电势

许多膜对离子有选择透过性：细胞膜在静息时主要允许 $\ce{K+}$ 通过，某些玻璃膜只对 $\ce{H+}$ 有响应。设一张只允许离子 B 透过的膜把两种溶液隔开，B 在左边的活度较高，它就向右透过，使右边带正电（若 B 是正离子）、左边带负电，膜两侧形成双电层；产生的电场阻止 B 进一步透过，最终宏观上透过停止。

**定义 13.9.1** 选择透过性膜两侧的溶液中，能透过膜的离子在两侧的电化学势相等、宏观上不再净透过的状态称为**膜平衡**；膜平衡时膜两侧溶液的内电势差 $E_{\mathrm{m}} = \varphi_{\text{右}} - \varphi_{\text{左}}$ 称为**膜电势**。

由定理 13.4.1，膜平衡时 $\mu_{\mathrm{B},\text{左}} + z_{\mathrm{B}}F\varphi_{\text{左}} = \mu_{\mathrm{B},\text{右}} + z_{\mathrm{B}}F\varphi_{\text{右}}$，

$$
E_{\mathrm{m}} = \varphi_{\text{右}} - \varphi_{\text{左}} = \frac{\mu_{\mathrm{B},\text{左}} - \mu_{\mathrm{B},\text{右}}}{z_{\mathrm{B}}F} = \frac{RT}{z_{\mathrm{B}}F}\ln\frac{a_{\mathrm{B},\text{左}}}{a_{\mathrm{B},\text{右}}}. \tag{13.9}
$$
它与浓差电池的电动势形式相同（[6.1.11](/6.1.11)），但没有电极反应，只有离子的选择性透过：膜本身起了"选择性电极"的作用。透过膜的离子的量极少——建立 $100\,\mathrm{mV}$ 的膜电势只需要膜两侧约 $10^{-6}$ 的离子发生转移（膜的比电容约 $1\,\mu\mathrm{F\,cm^{-2}}$），所以溶液的组成与电中性几乎不受影响。

### 13.9.2. 细胞的静息电位

细胞内外的离子浓度相差很大（哺乳动物神经元的典型值：$\ce{K+}$ 内 140、外 5 $\mathrm{mmol\,L^{-1}}$；$\ce{Na+}$ 内 12、外 145 $\mathrm{mmol\,L^{-1}}$），这一梯度由消耗 ATP 的 Na⁺/K⁺ 泵维持。生物学中把膜电势定义为细胞内相对于细胞外的电势，$E_{\mathrm{m}} = \varphi_{\text{内}} - \varphi_{\text{外}}$。若膜只允许 $\ce{K+}$ 透过，由式 (13.9)（左 = 外，右 = 内），$37\,^\circ\mathrm{C}$ 时 $RT/F = 26.7\,\mathrm{mV}$，

$$
E_{\ce{K}} = 26.7\,\mathrm{mV}\times\ln\frac{5}{140} = -89\,\mathrm{mV}, \qquad E_{\ce{Na}} = 26.7\,\mathrm{mV}\times\ln\frac{145}{12} = +67\,\mathrm{mV}.
$$
这两个值称为离子的平衡电位（Nernst 电位）。实测的静息电位约 $-70\,\mathrm{mV}$，接近 $E_{\ce{K}}$ 而偏向 $E_{\ce{Na}}$，因为静息的膜对 $\ce{K+}$ 的通透性远大于对 $\ce{Na+}$ 的，但不是零；多种离子同时透过时膜电位是一个稳态而非平衡态，由 Goldman–Hodgkin–Katz 方程描述，见[神经生物学](/7.16)与[生物物理学](/7.5)。动作电位中 $\ce{Na+}$ 通道开放，膜电位迅速趋向 $E_{\ce{Na}}$；线粒体内膜的质子梯度（约 $-150$ 到 $-180\,\mathrm{mV}$ 的膜电位加 pH 差）则驱动 ATP 的合成，它的热力学正是本节的电化学势。若膜两侧还有不能透过膜的大分子离子（蛋白质），则形成 Donnan 平衡，见 [6.3.21](/6.3.21)。

### 13.9.3. 玻璃电极与离子选择性电极

**定义 13.9.2** 电势只对溶液中某一种离子的活度有 Nernst 响应、用于测定该离子活度的指示电极称为**离子选择性电极**，其敏感元件通常是一张选择性膜。以对 $\ce{H+}$ 有选择性响应的特种玻璃薄膜为敏感膜的离子选择性电极称为**玻璃电极**。

玻璃电极是一个薄壁玻璃泡，内装 $\ce{HCl}$ 溶液（活度一定）和一根 $\ce{Ag}/\ce{AgCl}$ 内参比电极：$\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{HCl}(\text{内}) \mid \text{玻璃膜} \mid \text{待测溶液}$。玻璃膜表面吸水形成水化凝胶层，其中的 $\ce{Na+}$ 与溶液中的 $\ce{H+}$ 交换；膜两侧表面的 $\ce{H+}$ 交换平衡相当于一张只对 $\ce{H+}$ 有响应的膜。电极的电势是内参比电极的电势加上膜电势：

$$
E_{\mathrm{g}} = E(\ce{AgCl}/\ce{Ag}) - \frac{RT}{F}\ln a(\ce{Cl-}, \text{内}) + \frac{RT}{F}\ln\frac{a(\ce{H+}, \text{外})}{a(\ce{H+}, \text{内})} = E^\circ_{\mathrm{g}} - \frac{RT\ln10}{F}\mathrm{pH},
$$
其中 $E^\circ_{\mathrm{g}}$ 包括内参比电极、内溶液和玻璃膜的不对称电势等，对给定的电极只是温度的函数，但各电极不同且随时间漂移。所以玻璃电极与参比电极组成电池（$E_{\mathrm{cell}} = E_{\text{参比}} - E_{\mathrm{g}} = E_{\text{参比}} - E^\circ_{\mathrm{g}} + 0.05916\,\mathrm{V}\times\mathrm{pH}$，$25\,^\circ\mathrm{C}$）后，必须用两种标准缓冲溶液标定，再按 13.7.6 的操作定义读出 pH。这就是 pH 计（酸度计）。玻璃膜电阻很大（$10^8\,\Omega$ 量级），所以 pH 计必须有很高的输入阻抗。玻璃电极不受氧化剂、还原剂和胶体的干扰，但在 pH > 12 时对 $\ce{Na+}$ 也有响应（碱误差），在强酸中也有偏差（酸误差）。

改变敏感膜的材料就得到其他离子选择性电极：$\ce{LaF3}$ 单晶膜（$\ce{F-}$）、$\ce{Ag2S}$ 膜（$\ce{Ag+}$、$\ce{S^2-}$）、含缬氨霉素的 PVC 膜（$\ce{K+}$，缬氨霉素是能选择性结合 $\ce{K+}$ 的天然离子载体）。离子选择性电极的电位分析与血液中电解质的临床检测见[分析化学](/6.4)。

## 小结

| 主题 | 要点 |
|---|---|
| 可逆电池 | 物质可逆 + 能量可逆（$I \to 0$）；$\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$；三类可逆电极 |
| 测量 | $U = E_{\mathrm{cell}}R_{\mathrm{o}}/(R_{\mathrm{o}} + R_{\mathrm{i}})$；对消法（零电流）；Weston 标准电池已被 Josephson 电压基准取代 |
| Nernst 方程 | $E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{zF}\ln\prod a_{\mathrm{B}}^{\nu_{\mathrm{B}}}$；$E$ 与方程式写法无关，$\Delta_{\mathrm{r}}G$、$K^\circ$、$z$ 有关；$\ln K^\circ = zFE^\circ_{\mathrm{cell}}/RT$ |
| 温度系数 | $\Delta_{\mathrm{r}}S_{\mathrm{m}} = zF(\partial E/\partial T)_p$，$\Delta_{\mathrm{r}}H_{\mathrm{m}} = -zFE + zFT(\partial E/\partial T)_p$，$Q_{\mathrm{r}} = T\Delta_{\mathrm{r}}S_{\mathrm{m}} \ne \Delta_{\mathrm{r}}H_{\mathrm{m}}$；以端电压 $U$ 放电时 $Q = \Delta_{\mathrm{r}}H_{\mathrm{m}} + zFU$ |
| 电化学势 | $\tilde\mu_{\mathrm{B}} = \mu_{\mathrm{B}} + z_{\mathrm{B}}F\varphi$；平衡 $\tilde\mu^\alpha = \tilde\mu^\beta$；电动势 = 各界面 Galvani 电势差之和 = 两端电子电化学势之差除以 $-F$ |
| 液接电势 | $E_{\mathrm{l}} = (t_+ - t_-)\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}$（1-1 型）；$\ce{KCl}$ 盐桥 |
| 电极电势 | 以 SHE 为左极的电池的电动势；$E = E^\circ + \frac{RT}{zF}\ln\frac{a_{\text{氧化型}}}{a_{\text{还原型}}}$；$E_{\mathrm{cell}} = E_{\text{右}} - E_{\text{左}}$；参比电极 SCE 0.2412 V、Ag/AgCl（饱和 KCl）0.197 V |
| 电动势法 | $K_{\mathrm{w}}$、$K_{\mathrm{sp}}$；$\Delta_{\mathrm{r}}S$、$\Delta_{\mathrm{r}}H$；$\gamma_\pm$（Harned 电池）；$E^\circ$ 对 $\sqrt b$ 外推；$t_+ = E_{\text{有}}/E_{\text{无}}$；pH 的操作定义 |
| 电势–pH 图 | 水平、垂直、斜线；Fe：$\ce{Fe2O3}/\ce{Fe^3+}$ 在 pH 1.79，$\ce{Fe^2+}/\ce{Fe}$ 在 $-0.624\,\mathrm{V}$（$a = 10^{-6}$）；免蚀、腐蚀、钝化区 |
| 膜电势 | $E_{\mathrm{m}} = \frac{RT}{z_{\mathrm{B}}F}\ln\frac{a_{\text{左}}}{a_{\text{右}}}$；$E_{\ce{K}} \approx -89\,\mathrm{mV}$；玻璃电极 $E_{\mathrm{g}} = E^\circ_{\mathrm{g}} - 0.05916\,\mathrm{V}\times\mathrm{pH}$ |

## 思考题

1. 可逆电池的电动势能否用普通电压表测量？

   **答** 不能。电压表需要有限电流，测得的是端电压；须用对消法或高输入阻抗的电位计。

2. 电池的电动势与电池反应的计量系数有关吗？$z$ 影响 $E$ 吗？

   **答** 无关；$z$ 与 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 同比例变化，比值 $E$ 不变。但同一总反应若经不同的电极反应进行，$z$ 不同，$E$ 也不同，13.3.2。

3. 为测 $\ce{AgCl}$ 的溶度积，应设计什么电池？

   **答** $\ce{Ag} \mid \ce{AgNO3}(\mathrm{aq}) \parallel \ce{HCl}(\mathrm{aq}) \mid \ce{AgCl(s)} \mid \ce{Ag}$，电池反应 $\ce{Ag+ + Cl- -> AgCl}$ 的逆反应即溶解平衡，例 13.7.1。

4. 电池反应的标准平衡常数有哪些求法？

   **答** 热力学：由 $\Delta_{\mathrm{f}}G^\circ$ 或 $\Delta_{\mathrm{r}}H^\circ$、$\Delta_{\mathrm{r}}S^\circ$；电化学：由 $E^\circ_{\mathrm{cell}}$；统计力学：由配分函数，[6.3.11](/6.3.11)；动力学：由正、逆反应速率常数之比，[6.3.15](/6.3.15)。

5. 为什么 $E'$ 对 $\sqrt b$ 而不是对 $b$ 外推？

   **答** 由 Debye–Hückel 极限公式，稀溶液中 $\ln\gamma_\pm \propto \sqrt b$，$E'$ 对 $\sqrt b$ 是斜率已知的直线。

6. 一个吸热的电池反应能否自发进行并对外做功？

   **答** 能，只要 $\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$；做功的能量部分来自环境的热，例 13.3.2。
