---
title: 化学平衡
---

[6.1.6](/6.1.6) 给出了反应方向的判据：恒温恒压、不做**非体积功**时，$\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$ 的反应可以自发进行。但大多数反应并不进行到底，而是停在反应物与产物共存的某一状态，此后宏观组成不再变化。这一状态有两种等价的刻画：从动力学看（[6.1.7](/6.1.7)），正反应与逆反应的速率相等；从热力学看，系统的 **Gibbs 自由能**随反应进度达到极小，$\Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$。本章先描述化学平衡与平衡常数（8.1、8.2），再由热力学推出化学反应等温式与 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$（8.3），把第 6 章的热力学数据与平衡组成联系起来，最后讨论浓度、压力、温度对平衡的影响（8.4）。本章的标准平衡常数与等温式是后面四大平衡（酸碱、配位、沉淀、氧化还原，[6.1.9](/6.1.9)–[6.1.12](/6.1.12)）的共同基础。化学势、活度系数与逸度、多相平衡与相律等严格处理见[物理化学](/6.3)。

## 8.1. 可逆反应与化学平衡

**定义 8.1.1** 在同一条件下既能向正方向进行、又能向逆方向进行的反应称为**可逆反应**，用 $\ce{<=>}$ 表示。

严格地说，几乎所有反应都是可逆的，差别只在于逆反应的倾向大小：

| 反应 | 情况 |
|---|---|
| $\ce{2KClO3 ->[MnO2] 2KCl + 3O2}$（加热） | 产物 $\ce{O2}$ 逸出，可以进行到底 |
| $\ce{Ag+ + Cl- -> AgCl(s)}$ | 逆反应（溶解）的倾向很弱，几乎进行到底 |
| $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}$ | 正逆反应都不完全 |
| $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$ | 正逆反应都不完全 |
| $\ce{N2O4(g) <=> 2NO2(g)}$ | 正逆反应都不完全 |

在 $373\,\mathrm{K}$ 的密闭容器中放入 $0.100\,\mathrm{mol\,L^{-1}}$ 的 $\ce{N2O4}$（无色），它分解为 $\ce{NO2}$（红棕色）：

| $t/\mathrm{s}$ | 0 | 20 | 40 | 60 | 80 | 100 |
|---|---|---|---|---|---|---|
| $c(\ce{N2O4})/(\mathrm{mol\,L^{-1}})$ | 0.100 | 0.070 | 0.050 | 0.040 | 0.040 | 0.040 |
| $c(\ce{NO2})/(\mathrm{mol\,L^{-1}})$ | 0 | 0.060 | 0.100 | 0.120 | 0.120 | 0.120 |

反应不能进行到底：每升最多只有 $0.060\,\mathrm{mol}$ 的 $\ce{N2O4}$ 分解。60 s 以后浓度不再变化，但反应并没有停止：正反应不断生成 $\ce{NO2}$，逆反应以同样的速率把它变回 $\ce{N2O4}$。

**定义 8.1.2（化学平衡）** 封闭系统中，在恒定的温度（与压力或体积）下，可逆反应的正反应速率与逆反应速率相等时系统所处的状态称为**化学平衡**。

化学平衡是**平衡态**（[5.2.1](/5.2.1#def-1.1.2)）在有化学反应的系统中的特例，它的特征是：

1. 前提：恒温、封闭系统、可逆反应；
2. 条件：正逆反应速率相等，是动态平衡；
3. 标志：各物种的浓度不再随时间变化，反应达到该条件下的最大限度；
4. 化学平衡是有条件的：外界条件改变时，正逆反应速率不再相等，原有平衡被破坏，在新的条件下建立新的平衡（8.4）。

从动力学看平衡常数的来源。设 $a\mathrm{A} + b\mathrm{B} \ce{<=>} g\mathrm{G} + h\mathrm{H}$ 的正逆反应都是**基元反应**，由**质量作用定律**（[6.1.7](/6.1.7)），平衡时

$$
k_+c_{\mathrm{A}}^ac_{\mathrm{B}}^b = k_-c_{\mathrm{G}}^gc_{\mathrm{H}}^h \quad\Longrightarrow\quad \frac{c_{\mathrm{G}}^gc_{\mathrm{H}}^h}{c_{\mathrm{A}}^ac_{\mathrm{B}}^b} = \frac{k_+}{k_-}.
$$
左边的浓度比值在给定温度下是常数，与初始浓度无关。对复杂反应，平衡时其中每一步基元反应的正逆速率都分别相等（**细致平衡**，这一原理在 Markov 链 Monte Carlo 中也是构造平稳分布的条件，[3.5.9](/3.5.9)），总的浓度比值等于各步 $k_+/k_-$ 的乘积，结论相同。热力学给出了不依赖于机理的证明（8.3）。

## 8.2. 平衡常数

### 8.2.1. 经验平衡常数

在 $373\,\mathrm{K}$ 下从不同的初始组成出发建立 $\ce{N2O4 <=> 2NO2}$ 的平衡：

| 实验 | 初始 $c(\ce{NO2})$ | 初始 $c(\ce{N2O4})$ | 平衡 $[\ce{NO2}]$ | 平衡 $[\ce{N2O4}]$ | $[\ce{NO2}]^2/[\ce{N2O4}]$ |
|---|---|---|---|---|---|
| 1 | 0.000 | 0.100 | 0.120 | 0.040 | 0.36 |
| 2 | 0.100 | 0.000 | 0.072 | 0.014 | 0.37 |
| 3 | 0.100 | 0.100 | 0.160 | 0.070 | 0.36 |

（浓度单位 $\mathrm{mol\,L^{-1}}$；本章用 $[\mathrm{B}]$ 表示平衡浓度，用 $c_{\mathrm{B}}$ 表示任意时刻的浓度。）无论从正向还是逆向开始，最终都达到平衡，且 $[\ce{NO2}]^2/[\ce{N2O4}]$ 相同；温度改变时这一比值随之改变。

**定义 8.2.1** 一定温度下可逆反应 $a\mathrm{A} + b\mathrm{B} \ce{<=>} g\mathrm{G} + h\mathrm{H}$ 达到平衡时，产物浓度以其系数为指数的幂的乘积与反应物浓度以其系数为指数的幂的乘积之比是常数，称为浓度**平衡常数**：

$$
K_c = \frac{[\mathrm{G}]^g[\mathrm{H}]^h}{[\mathrm{A}]^a[\mathrm{B}]^b}.
$$
对气相反应，也常用平衡分压表示，称为压力平衡常数 $K_p = \frac{p_{\mathrm{G}}^gp_{\mathrm{H}}^h}{p_{\mathrm{A}}^ap_{\mathrm{B}}^b}$。$K_c$、$K_p$ 由实验测定，统称经验平衡常数，只与温度有关，一般有单位：$K_c$ 的单位是 $(\mathrm{mol\,L^{-1}})^{\Delta\nu}$，$K_p$ 的单位是 $\mathrm{Pa}^{\Delta\nu}$（或 $\mathrm{bar}^{\Delta\nu}$）。

这里 $\Delta\nu = (g + h) - (a + b)$；对气相反应记 $\Delta\nu_{\mathrm{g}} = \sum_{\mathrm{B(g)}}\nu_{\mathrm{B}}$，即气态物种**化学计量数**之和。例如合成氨 $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$，$K_c = \frac{[\ce{NH3}]^2}{[\ce{N2}][\ce{H2}]^3}$，$K_p = \frac{p_{\ce{NH3}}^2}{p_{\ce{N2}}p_{\ce{H2}}^3}$，$\Delta\nu_{\mathrm{g}} = -2$。

$K_p$ 与 $K_c$ 的关系可由物态方程得到：对**理想气体**，$p_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{V}RT = c_{\mathrm{B}}RT$，代入 $K_p$ 得

$$
K_p = K_c(RT)^{\Delta\nu_{\mathrm{g}}}.
$$
$\Delta\nu_{\mathrm{g}} = 0$ 时 $K_p = K_c$。计算时 $R$ 的单位要与浓度、压力的单位配套：$c$ 用 $\mathrm{mol\,m^{-3}}$、$p$ 用 $\mathrm{Pa}$ 时取 $R = 8.314\,\mathrm{Pa\,m^3\,mol^{-1}\,K^{-1}}$；$c$ 用 $\mathrm{mol\,L^{-1}}$、$p$ 用 $\mathrm{kPa}$ 时数值相同，$R = 8.314\,\mathrm{kPa\,L\,mol^{-1}\,K^{-1}}$；$p$ 用 $\mathrm{bar}$ 时 $R = 0.08314\,\mathrm{bar\,L\,mol^{-1}\,K^{-1}}$。

### 8.2.2. 平衡常数表达式的书写规则

1. 平衡常数的表达式和数值与方程式的写法有关。$373\,\mathrm{K}$ 时：

| 方程式 | $K_c$ | 数值 |
|---|---|---|
| $\ce{N2O4 <=> 2NO2}$ | $K_{c,1} = \frac{[\ce{NO2}]^2}{[\ce{N2O4}]}$ | $0.36$ |
| $\ce{1/2N2O4 <=> NO2}$ | $K_{c,2} = \frac{[\ce{NO2}]}{[\ce{N2O4}]^{1/2}}$ | $0.60$ |
| $\ce{2NO2 <=> N2O4}$ | $K_{c,3} = \frac{[\ce{N2O4}]}{[\ce{NO2}]^2}$ | $2.78$ |

$K_{c,1} = K_{c,2}^2 = 1/K_{c,3}$：方程式乘以 $n$，平衡常数变为 $n$ 次方；正逆反应的平衡常数互为倒数。因此给出平衡常数时必须同时给出方程式。

2. 纯固体、纯液体以及稀溶液中大量存在的溶剂（水）不写入表达式，它们的影响已包含在平衡常数中（8.3.1 用**活度**说明原因）：

$$
\ce{CaCO3(s) <=> CaO(s) + CO2(g)}: \quad K_p = p_{\ce{CO2}};
$$

$$
\ce{CO2(g) + H2(g) <=> CO(g) + H2O(l)}: \quad K_p = \frac{p_{\ce{CO}}}{p_{\ce{CO2}}p_{\ce{H2}}}; \qquad \ce{CO2(g) + H2(g) <=> CO(g) + H2O(g)}: \quad K_p = \frac{p_{\ce{CO}}p_{\ce{H2O}}}{p_{\ce{CO2}}p_{\ce{H2}}};
$$

$$
\ce{Cr2O7^2- + H2O <=> 2CrO4^2- + 2H+}: \quad K_c = \frac{[\ce{CrO4^2-}]^2[\ce{H+}]^2}{[\ce{Cr2O7^2-}]}.
$$
同一物质是液态还是气态，表达式不同。在非水溶剂中，若水是反应物或产物，它的浓度不再近似不变，必须写入表达式，如乙醇与乙酸的酯化：$K_c = \frac{[\ce{CH3COOC2H5}][\ce{H2O}]}{[\ce{C2H5OH}][\ce{CH3COOH}]}$。

3. 几个反应相加得到总反应时，总反应的平衡常数等于各反应平衡常数的乘积（下面的定理）。

**定理 8.2.1（多重平衡规则）** 若反应 (3) = 反应 (1) + 反应 (2)，则同一温度下 $K_3 = K_1K_2$；若反应 (3) = 反应 (1) − 反应 (2)，则 $K_3 = K_1/K_2$。

**证明** 各反应在同一系统中同时达到平衡时，各物种的平衡浓度是唯一的。把 (1)、(2) 的平衡常数表达式相乘，在两式中分别作为产物与反应物出现的物种相消，得到的正是反应 (3) 的表达式。$\square$

例如 $\ce{2NO + O2 <=> 2NO2}$（$K_1 = \frac{[\ce{NO2}]^2}{[\ce{NO}]^2[\ce{O2}]}$）与 $\ce{2NO2 <=> N2O4}$（$K_2 = \frac{[\ce{N2O4}]}{[\ce{NO2}]^2}$）相加得 $\ce{2NO + O2 <=> N2O4}$，$K_3 = \frac{[\ce{N2O4}]}{[\ce{NO}]^2[\ce{O2}]} = K_1K_2$。利用这一规则，可以由已知反应的平衡常数求出难以直接测定的反应的平衡常数；它与 **Hess 定律**（[6.1.6](/6.1.6)）是同一件事的两种表现：反应相加时 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 相加，而 $K^\circ = \mathrm{e}^{-\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT}$（8.3.2），所以平衡常数相乘。

### 8.2.3. 标准平衡常数与反应商

经验平衡常数的单位随反应而变，给计算和比较带来不便，也无法直接与热力学量联系。把浓度和分压分别除以**标准态**的浓度 $c^\circ = 1\,\mathrm{mol\,L^{-1}}$ 与**标准压力** $p^\circ = 10^5\,\mathrm{Pa}$（[6.1.6](/6.1.6)），就得到量纲一的相对浓度与相对分压。

**定义 8.2.2（标准平衡常数）** 对反应 $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$，平衡时

$$
K^\circ = \prod_{\mathrm{B}}\left(\frac{[\mathrm{B}]}{c^\circ}\right)^{\nu_{\mathrm{B}}}\ (\text{溶液中的物种}) \times \prod_{\mathrm{B}}\left(\frac{p_{\mathrm{B}}}{p^\circ}\right)^{\nu_{\mathrm{B}}}\ (\text{气体}),
$$
纯固体、纯液体与溶剂不出现（相当于取 1），称为**标准平衡常数**。它的量纲为一，只与温度有关。

例如 $a\mathrm{A(aq)} + b\mathrm{B(aq)} \ce{<=>} g\mathrm{G(aq)} + h\mathrm{H(aq)}$ 的 $K^\circ = \frac{([\mathrm{G}]/c^\circ)^g([\mathrm{H}]/c^\circ)^h}{([\mathrm{A}]/c^\circ)^a([\mathrm{B}]/c^\circ)^b}$，$\ce{CaCO3(s) <=> CaO(s) + CO2(g)}$ 的 $K^\circ = p_{\ce{CO2}}/p^\circ$。由于 $c^\circ = 1\,\mathrm{mol\,L^{-1}}$，溶液反应的 $K^\circ$ 在数值上等于以 $\mathrm{mol\,L^{-1}}$ 为单位的 $K_c$。气相反应则不同：

$$
K^\circ = K_p(p^\circ)^{-\Delta\nu_{\mathrm{g}}} = K_c\left(\frac{c^\circ RT}{p^\circ}\right)^{\Delta\nu_{\mathrm{g}}}.
$$

**例 8.2.1** 求 $373\,\mathrm{K}$ 时 $\ce{N2O4(g) <=> 2NO2(g)}$ 的 $K^\circ$。

**解** $K_c = 0.36\,\mathrm{mol\,L^{-1}} = 360\,\mathrm{mol\,m^{-3}}$，$\Delta\nu_{\mathrm{g}} = 1$，

$$
K^\circ = \frac{K_cRT}{p^\circ} = \frac{360 \times 8.314 \times 373}{10^5} = 11.
$$
可见气相反应的 $K^\circ$ 与 $K_c$ 的数值可以相差很大，不能混用。

平衡常数只描述平衡状态。对任意时刻（不一定平衡）的系统，可以用同样的形式写出一个比值。

**定义 8.2.3（反应商）** 把标准平衡常数表达式中的平衡浓度、平衡分压换成任意时刻的浓度 $c_{\mathrm{B}}$ 与分压 $p_{\mathrm{B}}$，所得的量

$$
Q = \prod_{\mathrm{B}}\left(\frac{c_{\mathrm{B}}}{c^\circ}\right)^{\nu_{\mathrm{B}}}\prod_{\mathrm{B}}\left(\frac{p_{\mathrm{B}}}{p^\circ}\right)^{\nu_{\mathrm{B}}}
$$
称为**反应商**。平衡时 $Q = K^\circ$。

反应商判据：$Q < K^\circ$ 时产物相对不足，反应正向进行；$Q = K^\circ$ 时处于平衡；$Q > K^\circ$ 时反应逆向进行。这一判据在 8.3.2 由热力学严格证明。本站约定反应商记作 $Q$，与热量 $Q$ 同形，由上下文区分。

### 8.2.4. 平衡常数的意义

平衡常数首先可以用来判断反应进行的程度。平衡是可逆反应在给定条件下进行的最大限度，$K^\circ$ 的大小反映平衡时产物所占的比例。下面用 [6.1.6](/6.1.6) 的**标准摩尔生成 Gibbs 自由能**按 8.3.2 的式 (8.3) 计算 $298.15\,\mathrm{K}$ 的 $K^\circ$：

- $\ce{2Cl(g) <=> Cl2(g)}$，$K^\circ \approx 8 \times 10^{36}$。若 $p_{\ce{Cl2}} = p^\circ$，平衡时 $p_{\ce{Cl}}/p^\circ = (K^\circ)^{-1/2} \approx 4 \times 10^{-19}$：氯原子几乎全部结合成分子。
- $\ce{N2(g) + O2(g) <=> 2NO(g)}$，$K^\circ \approx 2 \times 10^{-31}$。若 $p_{\ce{N2}} = p_{\ce{O2}} = p^\circ$，平衡时 $p_{\ce{NO}}/p^\circ \approx 4.5 \times 10^{-16}$：常温下 $\ce{N2}$ 与 $\ce{O2}$ 几乎不化合，反过来 NO 在热力学上不稳定（它在大气中能长期存在是动力学的原因）。
- $\ce{N2O4(g) <=> 2NO2(g)}$，$K^\circ \approx 0.15$（$373\,\mathrm{K}$ 时为 11，例 8.2.1）：反应物与产物的量相差不悬殊，都不可忽略。

粗略地说，$K^\circ > 10^7$ 时正反应进行得相当完全，$K^\circ < 10^{-7}$ 时正反应几乎不进行，介于两者之间的是典型的可逆反应。这只是数量级的参考，实际的平衡组成还取决于方程式的写法、各物种的系数与初始组成。

平衡常数只说明反应可能进行的最大程度，不说明达到平衡需要多长时间。$\ce{2SO2(g) + O2(g) <=> 2SO3(g)}$ 在 $298.15\,\mathrm{K}$ 的 $K^\circ \approx 7.5 \times 10^{24}$（例 8.3.1），常温下却几乎不反应，工业上要用 $\ce{V2O5}$ 催化剂并加热到 $400$–$600\,^\circ\mathrm{C}$。反之，$K^\circ$ 很小的反应也可以通过改变条件（移去产物、改变温度）使之进行得较完全。

平衡常数还可以用来计算平衡组成。已知 $K^\circ$ 与初始组成，可以求平衡组成。衡量反应物转化程度的量是转化率。

**定义 8.2.4** 反应物已转化的量占其初始量的百分数称为**转化率**：

$$
\alpha = \frac{\text{反应物的初始量} - \text{反应物的平衡量}}{\text{反应物的初始量}} \times 100\%.
$$
平衡时的转化率是该条件下的最大转化率，称为平衡转化率。

**例 8.2.2** $1473\,\mathrm{K}$ 时 $\ce{CO2(g) + H2(g) <=> CO(g) + H2O(g)}$ 的 $K^\circ = 2.3$。(1) $\ce{CO2}$ 和 $\ce{H2}$ 的初始浓度均为 $0.010\,\mathrm{mol\,L^{-1}}$，求 $\ce{CO2}$ 的平衡转化率；(2) 若 $\ce{H2}$ 的初始浓度改为 $0.020\,\mathrm{mol\,L^{-1}}$，其他不变，转化率是多少？

**解** 该反应 $\Delta\nu_{\mathrm{g}} = 0$，各分压之比等于浓度之比，$K^\circ$ 可以直接用浓度计算。设 CO 的平衡浓度为 $x$（单位 $\mathrm{mol\,L^{-1}}$）。

| | $\ce{CO2}$ | $\ce{H2}$ | $\ce{CO}$ | $\ce{H2O}$ |
|---|---|---|---|---|
| 初始 | 0.010 | 0.010 | 0 | 0 |
| 平衡 | $0.010 - x$ | $0.010 - x$ | $x$ | $x$ |

(1) $K^\circ = \frac{[\ce{CO}][\ce{H2O}]}{[\ce{CO2}][\ce{H2}]} = \frac{x^2}{(0.010 - x)^2} = 2.3$，开方得 $\frac{x}{0.010 - x} = 1.517$，$x = 0.0060$。$[\ce{CO2}] = 0.0040\,\mathrm{mol\,L^{-1}}$，转化率 $60\%$。

(2) $\frac{x^2}{(0.010 - x)(0.020 - x)} = 2.3$，整理得 $1.3x^2 - 0.069x + 4.6 \times 10^{-4} = 0$，取 $0 < x < 0.010$ 的根 $x = 0.0078$。$[\ce{CO2}] = 0.0022\,\mathrm{mol\,L^{-1}}$，转化率 $78\%$。

平衡常数不变，增加一种反应物（$\ce{H2}$）的浓度，提高了另一种反应物（$\ce{CO2}$）的转化率：转化率与初始组成有关，平衡常数只与温度有关。工业上常让廉价的反应物过量，以提高贵重反应物的转化率（8.4.1）。

## 8.3. 标准平衡常数与 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$

### 8.3.1. 化学反应等温式

[6.1.6](/6.1.6) 的 Gibbs 判据用的是 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$，即反应在给定组成下进行时 Gibbs 自由能的变化率；表中查到的却是各物种处于标准态时的 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$。两者的关系就是本节的等温式。我们先对理想气体推导，再推广到溶液。

先看一种理想气体的 Gibbs 自由能怎样随压力变化。对只做体积功的封闭系统，由热力学基本关系 $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$（[5.2.4](/5.2.4#eq-4.2)）和 $G = H - TS = U + pV - TS$，

$$
\mathrm{d}G = \mathrm{d}U + p\,\mathrm{d}V + V\,\mathrm{d}p - T\,\mathrm{d}S - S\,\mathrm{d}T = V\,\mathrm{d}p - S\,\mathrm{d}T.
$$
恒温时 $\mathrm{d}G = V\,\mathrm{d}p$。对 $1\,\mathrm{mol}$ 理想气体，$V_{\mathrm{m}} = RT/p$，从 $p^\circ$ 积分到 $p$：

$$
G_{\mathrm{m}}(T, p) = G^\circ_{\mathrm{m}}(T) + RT\ln\frac{p}{p^\circ},
$$
其中 $G^\circ_{\mathrm{m}}(T)$ 是该气体在标准压力下的摩尔 Gibbs 自由能。压力越高，Gibbs 自由能越高：气体有向低压处膨胀的自发倾向。

再看理想气体混合物。理想气体分子之间没有相互作用，混合物中每种气体的行为就像它单独占据整个容器、压力等于其**分压** $p_{\mathrm{B}}$ 一样（**Dalton 分压定律**，[6.1.1](/6.1.1)）。因此组分 B 的摩尔 Gibbs 自由能为

$$
G_{\mathrm{B}} = G^\circ_{\mathrm{m,B}}(T) + RT\ln\frac{p_{\mathrm{B}}}{p^\circ}. \tag{8.1}
$$
（严格地说，混合物中组分的摩尔 Gibbs 自由能是偏摩尔量，即化学势 $\mu_{\mathrm{B}}$；式 (8.1) 对理想气体混合物成立，一般的证明见[物理化学](/6.3)。）

系统的 Gibbs 自由能为 $G = \sum_{\mathrm{B}}n_{\mathrm{B}}G_{\mathrm{B}}$。反应进度增加 $\mathrm{d}\xi$ 时 $\mathrm{d}n_{\mathrm{B}} = \nu_{\mathrm{B}}\,\mathrm{d}\xi$，在恒温恒压下

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \left(\frac{\partial G}{\partial\xi}\right)_{T,p} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}G_{\mathrm{B}}.
$$
（$G_{\mathrm{B}}$ 本身也随组成变化，但这些变化的加权和为零，即 Gibbs–Duhem 关系，见[物理化学](/6.3)。）$\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 是 $G$–$\xi$ 曲线的斜率，单位 $\mathrm{J\,mol^{-1}}$，"摩尔"指每摩尔反应进度。代入式 (8.1)：

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}G^\circ_{\mathrm{m,B}} + RT\sum_{\mathrm{B}}\nu_{\mathrm{B}}\ln\frac{p_{\mathrm{B}}}{p^\circ} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln\prod_{\mathrm{B}}\left(\frac{p_{\mathrm{B}}}{p^\circ}\right)^{\nu_{\mathrm{B}}}.
$$
最后一个乘积正是反应商 $Q$。

对溶液中的溶质与纯凝聚相，可以写出与式 (8.1) 形式相同的关系，相对分压换成另一个量纲一的量：

**定义 8.3.1** 物种 B 的摩尔 Gibbs 自由能（化学势）写成 $G_{\mathrm{B}} = G^\circ_{\mathrm{m,B}} + RT\ln a_{\mathrm{B}}$ 时，量纲一的量 $a_{\mathrm{B}}$ 称为 B 的**活度**（相对活度）。对理想气体 $a_{\mathrm{B}} = p_{\mathrm{B}}/p^\circ$；对理想稀溶液中的溶质 $a_{\mathrm{B}} \approx c_{\mathrm{B}}/c^\circ$；对纯固体、纯液体以及稀溶液中的溶剂 $a_{\mathrm{B}} \approx 1$。

活度就是"有效的相对浓度"。真实溶液中 $a_{\mathrm{B}} = \gamma_{\mathrm{B}}c_{\mathrm{B}}/c^\circ$，活度系数 $\gamma_{\mathrm{B}}$ 反映离子间相互作用等对理想行为的偏离，稀溶液中 $\gamma_{\mathrm{B}} \to 1$（[物理化学](/6.3)）；真实气体用逸度代替分压。纯固体与纯液体在标准压力附近的 Gibbs 自由能几乎不随压力变化，所以 $a = 1$：这就是 8.2.2 中它们不写入平衡常数的原因。本课程中一律按理想情形处理：气体用相对分压，溶质用相对浓度。

**定理 8.3.1（化学反应等温式）** 恒温恒压下，反应 $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$ 的摩尔 Gibbs 自由能变为

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q, \qquad Q = \prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}}. \tag{8.2}
$$

在理想情形下 $Q$ 就是定义 8.2.3 的反应商。$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 只与温度有关，可以由热力学数据计算；$RT\ln Q$ 反映了实际组成的影响。由等温式可以求出任意组成下的 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$，从而判断反应方向。

### 8.3.2. 标准平衡常数与标准摩尔反应 Gibbs 自由能

平衡时 $G$ 取极小，$\Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$，$Q = K^\circ$。由式 (8.2)：

**公式 8.3.1** 

$$
\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ, \qquad K^\circ = \exp\left(-\frac{\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}}{RT}\right). \tag{8.3}
$$

这一结果说明：$Q$ 在平衡时的值只由 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}(T)$ 决定，与初始组成无关，这正是 8.2 中由实验总结出的平衡常数。它从热力学上证明了平衡常数的存在，并且不依赖于反应机理。把式 (8.3) 代回式 (8.2)：

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = RT\ln\frac{Q}{K^\circ}.
$$
于是 $Q < K^\circ \iff \Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$（正向自发），$Q = K^\circ \iff \Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$（平衡），$Q > K^\circ \iff \Delta_{\mathrm{r}}G_{\mathrm{m}} > 0$（逆向自发）：反应商判据与 Gibbs 判据是同一个判据。

**注 8.3.1** 判断反应方向的是 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$，不是 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$。$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} < 0$ 只说明 $K^\circ > 1$，或者说各物种都处于标准态（$Q = 1$）时反应正向自发；在实际组成下，只要 $Q > K^\circ$，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} < 0$ 的反应也会逆向进行。不过 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 的绝对值很大时，$K^\circ$ 极大或极小，一般的组成变化不足以改变方向：$298\,\mathrm{K}$ 时 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -40\,\mathrm{kJ\,mol^{-1}}$ 对应 $K^\circ \approx 10^7$，因此常用 $|\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}| > 40\,\mathrm{kJ\,mol^{-1}}$ 粗略判断反应基本完全或基本不进行。

$G$ 为什么在 $0 < \xi < 1$ 之间有极小，而不是在纯反应物或纯产物处？以 $\ce{N2O4 <=> 2NO2}$ 为例，若反应物与产物各自保持纯态、不混合，$G$ 随 $\xi$ 线性变化，系统会一直走到 $G$ 较低的一端。实际上两者混合：式 (8.1) 中的 $RT\ln(p_{\mathrm{B}}/p^\circ)$ 在 $\xi \to 0$ 与 $\xi \to 1$ 处趋于 $-\infty$ 的斜率，来自混合**熵**；它使 $G$–$\xi$ 曲线在两端都向下弯，极小值落在中间。所以化学平衡总是反应物与产物共存，只是 $K^\circ$ 很大或很小时，极小点非常靠近一端。

![298.15 K、总压 p° 下由 1 mol N₂O₄ 出发时系统的 Gibbs 自由能随反应进度的变化：虚线是不混合时的直线，实线因混合而向下弯曲，极小点就是平衡，两侧的斜率即 ΔrGm 的正负](./plots/gibbs-extent.py)

图中由 1 mol $\ce{N2O4}$ 出发，总压保持 $p^\circ$，平衡条件 $K^\circ = \frac{(p_{\ce{NO2}}/p^\circ)^2}{p_{\ce{N2O4}}/p^\circ} = \frac{4\xi^2}{1 - \xi^2}$。$298.15\,\mathrm{K}$ 时 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 4.73\,\mathrm{kJ\,mol^{-1}}$，$K^\circ = 0.148$，解得 $\xi_{\mathrm{eq}} = \sqrt{K^\circ/(4 + K^\circ)} = 0.189\,\mathrm{mol}$，即约 $19\%$ 的 $\ce{N2O4}$ 分解：$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} > 0$ 的反应也会进行一定程度。

**例 8.3.1** 求 $298.15\,\mathrm{K}$ 时 $\ce{2SO2(g) + O2(g) <=> 2SO3(g)}$ 的 $K^\circ$。已知 $\Delta_{\mathrm{f}}G^\circ(\ce{SO2}, \mathrm{g}) = -300.1\,\mathrm{kJ\,mol^{-1}}$，$\Delta_{\mathrm{f}}G^\circ(\ce{SO3}, \mathrm{g}) = -371.1\,\mathrm{kJ\,mol^{-1}}$。

**解** $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 2 \times (-371.1) - 2 \times (-300.1) - 0 = -142.0\,\mathrm{kJ\,mol^{-1}}$（单质 $\ce{O2}$ 的 $\Delta_{\mathrm{f}}G^\circ = 0$）。由式 (8.3)，

$$
\ln K^\circ = \frac{142.0 \times 10^3}{8.314 \times 298.15} = 57.28, \qquad K^\circ = 7.5 \times 10^{24}.
$$

## 8.4. 化学平衡的移动

条件改变使原来的平衡被破坏、系统在新条件下建立新平衡的过程称为平衡的移动。由 $\Delta_{\mathrm{r}}G_{\mathrm{m}} = RT\ln(Q/K^\circ)$，破坏平衡的途径只有两种：

- 改变 $Q$ 而 $K^\circ$ 不变：改变浓度、压力或体积；
- 改变 $K^\circ$：改变温度（$\ln K^\circ = -\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT$）。

无论哪种，判断移动方向只需比较新的 $Q$ 与 $K^\circ$。

### 8.4.1. 浓度

温度、体积不变时，增大反应物浓度或减小产物浓度，$Q < K^\circ$，平衡向正方向移动，直到 $Q$ 重新等于 $K^\circ$；反之平衡逆向移动。工业上的应用：

- $\ce{2SO2 + O2 <=> 2SO3}$：按方程式 $\ce{SO2}$ 与 $\ce{O2}$ 的物质的量之比为 $1 : 0.5$，实际采用约 $1 : 1.6$（空气过量），以提高 $\ce{SO2}$ 的转化率；
- $\ce{CO + H2O <=> H2 + CO2}$（水煤气变换）：使水蒸气过量，提高 CO 的转化率；
- $\ce{Fe3O4(s) + 4H2(g) <=> 3Fe(s) + 4H2O(g)}$：不断移去水蒸气，使 $\ce{Fe3O4}$ 还原完全。

### 8.4.2. 压力

压力对只有液体、固体参加的反应影响很小。对有气体参加的反应，考虑恒温下把体积压缩为原来的 $1/x$，各分压都变为原来的 $x$ 倍，反应商变为

$$
Q' = x^{\Delta\nu_{\mathrm{g}}}K^\circ.
$$

1. $\Delta\nu_{\mathrm{g}} \ne 0$：例如合成氨 $\Delta\nu_{\mathrm{g}} = -2$，加压一倍（$x = 2$）时 $Q' = \frac{1}{4}K^\circ < K^\circ$，平衡正向移动；减压一半（$x = \frac{1}{2}$）时 $Q' = 4K^\circ$，平衡逆向移动。增大压力，平衡向气体分子数减少的方向移动；减小压力，向气体分子数增加的方向移动。
2. $\Delta\nu_{\mathrm{g}} = 0$：例如 $\ce{CO(g) + H2O(g) <=> H2(g) + CO2(g)}$，$Q' = K^\circ$，改变总压对平衡没有影响。

向已达平衡的合成氨系统中充入不参加反应的气体（如 Ar），结果取决于条件：

- 恒温恒容：总压增大，但各反应气体的物质的量与体积都不变，分压不变，$Q = K^\circ$，平衡不移动。所以"充入惰性气体使总压变为原来的 2 倍"并不会使合成氨的平衡移动。
- 恒温恒压：体积增大，各反应气体的分压按同一比例减小，相当于对反应系统减压，平衡向气体分子数增加的方向（合成氨中为逆向）移动。合成氨原料气中积累的 Ar、$\ce{CH4}$ 要定期放空，就是这个原因。

决定平衡的是参加反应的各气体的分压，而不是总压。

### 8.4.3. 温度

温度改变时，$K^\circ$ 本身改变。由 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$ 与 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$，

$$
\ln K^\circ = -\frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT} + \frac{\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}}{R}. \tag{8.4}
$$

**定理 8.4.1（van 't Hoff 方程）** 标准平衡常数随温度的变化率为

$$
\frac{\mathrm{d}\ln K^\circ}{\mathrm{d}T} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT^2}.
$$
若温度范围不大，$\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ 可视为常数，则

$$
\ln\frac{K^\circ_2}{K^\circ_1} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right). \tag{8.5}
$$

**证明** 在 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$、$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 不随温度变化的近似下（即忽略反应前后热容之差 $\Delta_{\mathrm{r}}C_p$），对式 (8.4) 求导即得微分式；在 $T_1$、$T_2$ 两个温度写出式 (8.4) 相减，$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 消去，得式 (8.5)。微分式本身不需要这一近似，它是 Gibbs–Helmholtz 方程 $\left(\frac{\partial(G/T)}{\partial T}\right)_p = -\frac{H}{T^2}$ 的直接推论（[物理化学](/6.3)）。$\square$

van 't Hoff 方程与 Arrhenius 方程（[6.1.7](/6.1.7#def-7.3.5)）形式相同，这不是巧合：对基元反应 $K = k_+/k_-$，两边取对数对 $T$ 求导，$\frac{\mathrm{d}\ln K}{\mathrm{d}T} = \frac{E_{\mathrm{a}} - E_{\mathrm{a}}'}{RT^2}$，与势能图上 $\Delta_{\mathrm{r}}H_{\mathrm{m}} \approx E_{\mathrm{a}} - E_{\mathrm{a}}'$ 一致。

由式 (8.4)，$\ln K^\circ$ 对 $1/T$ 作图（van 't Hoff 作图）是一条直线，斜率为 $-\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}/R$，截距为 $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}/R$：测定不同温度的平衡常数，就能得到反应的标准焓变与熵变，这是不用量热计测定 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ 的方法。

- 放热反应（$\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} < 0$）：升高温度，$K^\circ$ 减小，平衡逆向移动；降低温度，平衡正向移动。
- 吸热反应（$\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} > 0$）：升高温度，$K^\circ$ 增大，平衡正向移动。

总之，升高温度使平衡向吸热方向移动，降低温度使平衡向放热方向移动。与浓度、压力不同，温度改变的是平衡常数本身。

**例 8.4.1** 合成氨 $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$。由 $\Delta_{\mathrm{f}}H^\circ(\ce{NH3}, \mathrm{g}) = -45.9\,\mathrm{kJ\,mol^{-1}}$ 与标准摩尔熵 $S^\circ_{\mathrm{m}}(\ce{NH3}) = 192.8$、$S^\circ_{\mathrm{m}}(\ce{N2}) = 191.6$、$S^\circ_{\mathrm{m}}(\ce{H2}) = 130.7\,\mathrm{J\,mol^{-1}\,K^{-1}}$，估算 $473\,\mathrm{K}$ 与 $573\,\mathrm{K}$ 的 $K^\circ$。

**解** $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = 2 \times (-45.9) = -91.8\,\mathrm{kJ\,mol^{-1}}$，$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = 2 \times 192.8 - 191.6 - 3 \times 130.7 = -198.1\,\mathrm{J\,mol^{-1}\,K^{-1}}$。忽略它们随温度的变化，由式 (8.4)：

$$
473\,\mathrm{K}: \quad \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -91.8 + 473 \times 0.1981 = 1.9\,\mathrm{kJ\,mol^{-1}}, \qquad K^\circ_1 = \mathrm{e}^{-1900/(8.314 \times 473)} = 0.62.
$$
再由式 (8.5)，

$$
\ln\frac{K^\circ_2}{0.62} = \frac{-91.8 \times 10^3}{8.314}\left(\frac{1}{473} - \frac{1}{573}\right) = -4.07, \qquad K^\circ_2 = 1.0 \times 10^{-2}.
$$
升高 100 K，$K^\circ$ 减小为约 $1/60$：降低温度有利于氨的生成（$298\,\mathrm{K}$ 时 $K^\circ \approx 5 \times 10^5$）。

但低温下反应太慢。工业上的 Haber–Bosch 法采用 $400$–$500\,^\circ\mathrm{C}$、$10$–$30\,\mathrm{MPa}$ 与铁催化剂：较高的温度保证速率，高压弥补高温造成的平衡产率下降，未反应的气体分离氨后循环使用。这是热力学与动力学折中的典型例子。

![合成氨：左为 ln K° 对 1/T 的 van 't Hoff 作图，放热反应的直线斜率为正；右为 N₂ 与 H₂ 按 1 : 3 投料时平衡氨摩尔分数随温度与总压的变化（理想气体、忽略 ΔrCp 的估算）](./plots/ammonia-equilibrium.py)

右图由例 8.4.1 的 $K^\circ(T)$ 数值求解平衡组成得到：设 $1\,\mathrm{mol}$ $\ce{N2}$ 与 $3\,\mathrm{mol}$ $\ce{H2}$ 中有 $\xi$ mol $\ce{N2}$ 反应，总量为 $4 - 2\xi$，代入 $K^\circ = \frac{x_{\ce{NH3}}^2}{x_{\ce{N2}}x_{\ce{H2}}^3}\left(\frac{p}{p^\circ}\right)^{-2}$，用数值求根（如 `scipy.optimize.brentq`，[4.4.4](/4.4.4#sec-4.2.2)）解出 $\xi$。高压下真实气体的偏离与 $\Delta_{\mathrm{r}}C_p$ 使实际数值与图中略有差别，但趋势相同。

### 8.4.4. Le Chatelier 原理

以上结论可以概括为 Le Chatelier 原理（Le Chatelier's principle）：如果改变平衡系统的条件之一（浓度、压力或温度），平衡就向减弱这一改变的方向移动。具体地说：增加反应物浓度，平衡向消耗反应物的方向移动；增大压力，平衡向气体分子数减少的方向移动；升高温度，平衡向吸热方向移动。（中文教材也称平衡移动原理；旧译名"里查德里原理"已不用。）

Le Chatelier 原理是一条定性的经验规则，条件复杂时可能给出错误的预言；可靠的判据始终是比较 $Q$ 与 $K^\circ$。

**例 8.4.2** 恒温恒压下，向已达平衡的合成氨系统中再加入少量 $\ce{N2}$，平衡一定向生成 $\ce{NH3}$ 的方向移动吗？

**解** 恒压下各物种的分压为 $p_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{n}p$（$n$ 为总物质的量），

$$
Q = \frac{(p_{\ce{NH3}}/p^\circ)^2}{(p_{\ce{N2}}/p^\circ)(p_{\ce{H2}}/p^\circ)^3} = \frac{n_{\ce{NH3}}^2\,n^2}{n_{\ce{N2}}\,n_{\ce{H2}}^3}\left(\frac{p^\circ}{p}\right)^2.
$$
加入 $\mathrm{d}n_{\ce{N2}}$ 时 $n$ 也增大 $\mathrm{d}n_{\ce{N2}}$，

$$
\frac{\partial\ln Q}{\partial n_{\ce{N2}}} = \frac{2}{n} - \frac{1}{n_{\ce{N2}}},
$$
当 $x_{\ce{N2}} = n_{\ce{N2}}/n > \frac{1}{2}$ 时它为正：加入 $\ce{N2}$ 使 $Q > K^\circ$，平衡反而向分解氨的方向移动。原因是加入 $\ce{N2}$ 虽然增大了 $\ce{N2}$ 的分压，却同时稀释了 $\ce{H2}$ 与 $\ce{NH3}$，而 $\ce{H2}$ 在 $Q$ 中是三次方。只有在 $x_{\ce{N2}} < \frac{1}{2}$（包括按 1 : 3 投料的通常情形）时，加入 $\ce{N2}$ 才使平衡正向移动。恒容下加入 $\ce{N2}$ 不改变其他分压，平衡总是正向移动。

催化剂同等程度地加快正逆反应（[6.1.7](/6.1.7)），不改变 $K^\circ$，因而不使平衡移动，只缩短达到平衡的时间。

## 思考题

1. 已知 $298\,\mathrm{K}$ 时 $\ce{2NO2(g) <=> N2O4(g)}$ 的 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -4.73\,\mathrm{kJ\,mol^{-1}}$。把 $p_{\ce{NO2}} = p_{\ce{N2O4}} = 50\,\mathrm{kPa}$ 的混合气体放入容器，反应向哪个方向进行？
   答：$K^\circ = \mathrm{e}^{4730/(8.314 \times 298)} = 6.7$，$Q = \frac{0.5}{0.5^2} = 2 < K^\circ$，向生成 $\ce{N2O4}$ 的方向进行。
2. 为什么说"$K^\circ$ 越大，反应越快"是错误的？
   答：$K^\circ$ 由 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 决定，是热力学量；速率由活化能决定，是动力学量。$\ce{2SO2 + O2}$ 的 $K^\circ \approx 10^{25}$，常温下却几乎不反应。
3. 对吸热反应，升高温度既加快正反应也加快逆反应，为什么平衡仍向正方向移动？
   答：由 $K = k_+/k_-$ 与 $E_{\mathrm{a}} - E_{\mathrm{a}}' = \Delta_{\mathrm{r}}H_{\mathrm{m}} > 0$，正反应活化能较大，$k_+$ 随温度增大得更快（[6.1.7](/6.1.7)），所以 $K$ 增大。

## 小结

| 内容 | 要点 |
|---|---|
| 化学平衡 | 正逆反应速率相等的动态平衡；$G$ 对 $\xi$ 取极小，$\Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$ |
| 平衡常数 | $K_c$、$K_p$ 有单位，$K_p = K_c(RT)^{\Delta\nu_{\mathrm{g}}}$；$K^\circ$ 用相对浓度、相对分压，量纲一，$K^\circ = K_c(c^\circ RT/p^\circ)^{\Delta\nu_{\mathrm{g}}}$ |
| 书写规则 | 与方程式写法有关；纯固体、纯液体、稀溶液的溶剂不写入；反应相加，平衡常数相乘 |
| 反应商 | $Q < K^\circ$ 正向，$Q = K^\circ$ 平衡，$Q > K^\circ$ 逆向 |
| 等温式 | $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q = RT\ln(Q/K^\circ)$；$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$ |
| 浓度与压力 | 改变 $Q$ 不改变 $K^\circ$；加压向气体分子数减少的方向移动；恒容充入惰性气体不移动，恒压充入相当于减压 |
| 温度 | 改变 $K^\circ$：$\frac{\mathrm{d}\ln K^\circ}{\mathrm{d}T} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT^2}$，升温向吸热方向移动 |
| Le Chatelier 原理 | 平衡向减弱外界改变的方向移动；定性规则，以 $Q$ 与 $K^\circ$ 的比较为准；催化剂不影响平衡 |
