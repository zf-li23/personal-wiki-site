---
title: 理想液态混合物与理想稀溶液
---

[6.3.4](/6.3.4) 建立了多组分系统的语言：**偏摩尔量**、**化学势**与**逸度**，并给出了气体（理想与实际）的化学势表达式。本章把这套语言用到液相。液体的化学势无法直接测量，但液体与它的蒸气平衡时两相中每种物质的化学势相等，于是液相中的化学势可以借助气相表示，问题归结为溶液上方的蒸气分压如何随组成变化。稀溶液中有两条实验定律：溶剂服从 Raoult 定律，挥发性溶质服从 Henry 定律。以它们为基础定义两种理想化的溶液——理想液态混合物（5.1）与理想稀溶液（5.2），写出各组分化学势的表达式，并由此严格推出稀溶液的依数性（5.3）：蒸气压降低、凝固点降低、沸点升高与渗透压。这些结果是实际溶液的出发点：[6.3.6](/6.3.6) 用活度修正对理想行为的偏离，[6.3.7](/6.3.7) 由化学势导出溶液中的平衡常数，[6.3.9](/6.3.9) 由 Raoult 定律画出二组分相图；渗透压则是细胞与体液水分调节的物理基础。

本章用 A 表示溶剂、B 表示溶质（或混合物中任一组分），上标 $*$ 表示纯物质，上标 $^\circ$ 表示标准态（**标准压力** $p^\circ = 10^5\,\mathrm{Pa}$）。

## 5.1. Raoult 定律与理想液态混合物

### 5.1.1. Raoult 定律

纯液体的**饱和蒸气压** $p^*_{\mathrm{A}}$ 主要取决于温度。溶入另一种物质后，溶剂的蒸气分压下降。Raoult 在 1887 年总结了大量稀溶液的数据，得到 Raoult 定律（Raoult's law）：一定温度下，稀溶液中溶剂的蒸气分压等于同温度下纯溶剂的饱和蒸气压乘以溶液中溶剂的**摩尔分数**，

$$
p_{\mathrm{A}} = p^*_{\mathrm{A}}x_{\mathrm{A}}. \tag{5.1}
$$

说明：

1. 对任何溶液，$x_{\mathrm{A}} \to 1$ 时式 (5.1) 都严格成立；它是一条极限定律，溶液越稀越准确。
2. 计算 $x_{\mathrm{A}}$ 时，溶剂的摩尔质量取其气态分子的摩尔质量（例如水取 $18.015\,\mathrm{g\,mol^{-1}}$，即使液态水中有氢键缔合）。
3. 溶质可以挥发，也可以不挥发；但溶质若在溶液中解离或缔合，$x_{\mathrm{A}}$ 要按溶液中实际存在的粒子计算（电解质溶液见 [6.3.12](/6.3.12)）。
4. 严格地说，$p^*_{\mathrm{A}}$ 是与溶液同温、同压下纯溶剂的饱和蒸气压；外压对蒸气压的影响很小（[6.3.8](/6.3.8)），通常不必区分。

### 5.1.2. 理想液态混合物

实验发现，结构与性质相近的液体组成的混合物中，每个组分在全部浓度范围内都遵守或近似遵守 Raoult 定律：水–重水（同位素化合物）、d-樟脑–l-樟脑（光学异构体）、邻/间/对二甲苯（结构异构体）、苯–甲苯、甲醇–乙醇（相邻的同系物）。它们的共同点是 A–A、B–B、A–B 分子间的相互作用几乎相同，分子大小也相近：一个分子周围换成另一种分子，能量不变，只是排列的方式变多了。

**定义 5.1.1（理想液态混合物）** 任一组分在全部浓度范围内都遵守 Raoult 定律的液态混合物称为**理想液态混合物**（也称理想溶液）。

对二组分理想液态混合物，

$$
p_{\mathrm{A}} = p^*_{\mathrm{A}}x_{\mathrm{A}}, \qquad p_{\mathrm{B}} = p^*_{\mathrm{B}}x_{\mathrm{B}}, \qquad p = p_{\mathrm{A}} + p_{\mathrm{B}} = p^*_{\mathrm{A}} + (p^*_{\mathrm{B}} - p^*_{\mathrm{A}})x_{\mathrm{B}}.
$$
总压与液相组成成直线关系。设蒸气是**理想气体**，由 **Dalton 分压定律**，气相组成为

$$
y_{\mathrm{B}} = \frac{p_{\mathrm{B}}}{p} = \frac{p^*_{\mathrm{B}}x_{\mathrm{B}}}{p}, \qquad \frac{y_{\mathrm{B}}}{x_{\mathrm{B}}} = \frac{p^*_{\mathrm{B}}}{p}.
$$
若 $p^*_{\mathrm{B}} > p^*_{\mathrm{A}}$（B 易挥发），则 $p^*_{\mathrm{B}} > p$，$y_{\mathrm{B}} > x_{\mathrm{B}}$：易挥发组分在气相中的含量高于它在液相中的含量。这是蒸馏与**精馏**的依据（[6.3.9](/6.3.9)）。

![理想液态混合物的气液平衡（p*_A = 40 kPa，p*_B = 120 kPa）：左图为分压与总压随液相组成的直线；右图为液相线与气相线，竖直箭头是例 5.1.1 中蒸气的恒温压缩过程](./plots/ideal-pxy.py)

**例 5.1.1** 室温下液体 A 与 B 形成理想液态混合物，$p^*_{\mathrm{A}} = 40.0\,\mathrm{kPa}$，$p^*_{\mathrm{B}} = 120.0\,\mathrm{kPa}$。把 $y_{\mathrm{A}} = 0.40$ 的蒸气放入带活塞的气缸，恒温下缓慢压缩。求开始液化时的压力与第一滴液体的组成，以及全部液化时的压力与最后一个气泡的组成。

**解** 开始液化（露点）时气相组成仍为 $y_{\mathrm{A}} = 0.40$。由 $x_{\mathrm{A}} = py_{\mathrm{A}}/p^*_{\mathrm{A}}$、$x_{\mathrm{B}} = py_{\mathrm{B}}/p^*_{\mathrm{B}}$ 与 $x_{\mathrm{A}} + x_{\mathrm{B}} = 1$，

$$
\frac{1}{p} = \frac{y_{\mathrm{A}}}{p^*_{\mathrm{A}}} + \frac{y_{\mathrm{B}}}{p^*_{\mathrm{B}}} = \frac{0.40}{40.0} + \frac{0.60}{120.0} = 0.0150\,\mathrm{kPa^{-1}}, \qquad p = 66.7\,\mathrm{kPa},
$$
第一滴液体 $x_{\mathrm{A}} = 66.7 \times 0.40/40.0 = 0.667$。全部液化（泡点）时液相组成为 $x_{\mathrm{A}} = 0.40$，$p = 40.0 \times 0.40 + 120.0 \times 0.60 = 88.0\,\mathrm{kPa}$，最后一个气泡 $y_{\mathrm{A}} = 16.0/88.0 = 0.182$。反过来，把这一液体减压汽化时，第一个气泡的组成也是 $y_{\mathrm{A}} = 0.182$。压缩过程中两相的组成都在变：液相从 $x_{\mathrm{A}} = 0.667$ 变到 $0.40$，气相从 $0.40$ 变到 $0.182$，两相的相对数量由**杠杆规则**确定（[6.3.9](/6.3.9)）。

### 5.1.3. 理想液态混合物中各组分的化学势

设混合物在温度 $T$、压力 $p$ 下与其蒸气平衡，蒸气可视为理想气体混合物。组分 B 在两相中的化学势相等（[6.3.4](/6.3.4)），

$$
\mu_{\mathrm{B}}(\mathrm{sln}) = \mu_{\mathrm{B}}(\mathrm{g}) = \mu^\circ_{\mathrm{B}}(\mathrm{g}, T) + RT\ln\frac{p_{\mathrm{B}}}{p^\circ} = \mu^\circ_{\mathrm{B}}(\mathrm{g}, T) + RT\ln\frac{p^*_{\mathrm{B}}}{p^\circ} + RT\ln x_{\mathrm{B}}.
$$
前两项之和是纯液体 B 与其蒸气平衡时的化学势，即纯液体 B 的化学势 $\mu^*_{\mathrm{B}}(\mathrm{l}, T, p)$。于是

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) = \mu^*_{\mathrm{B}}(\mathrm{l}, T, p) + RT\ln x_{\mathrm{B}}. \tag{5.2}
$$

推导中用到了蒸气的理想性，但式 (5.2) 本身只涉及液相。更好的做法是把它作为理想液态混合物的热力学定义：在某一温度、压力范围内各组分的化学势都满足式 (5.2) 的液态混合物。由式 (5.2) 出发，蒸气为理想气体时立即得到 Raoult 定律；蒸气不理想时，Raoult 定律中的分压换成**逸度**仍严格成立。

$\mu^*_{\mathrm{B}}(\mathrm{l}, T, p)$ 不是标准态的化学势。液体 B 的**标准态**规定为温度 $T$、压力 $p^\circ$ 下的纯液体，其化学势记作 $\mu^\circ_{\mathrm{B}}(\mathrm{l}, T)$，只是温度的函数。由 $(\partial\mu^*_{\mathrm{B}}/\partial p)_T = V^*_{\mathrm{m,B}}$，

$$
\mu^*_{\mathrm{B}}(\mathrm{l}, T, p) = \mu^\circ_{\mathrm{B}}(\mathrm{l}, T) + \int_{p^\circ}^{p}V^*_{\mathrm{m,B}}\,\mathrm{d}p,
$$
代入式 (5.2)：

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) = \mu^\circ_{\mathrm{B}}(\mathrm{l}, T) + RT\ln x_{\mathrm{B}} + \int_{p^\circ}^{p}V^*_{\mathrm{m,B}}\,\mathrm{d}p. \tag{5.3}
$$
三项分别只依赖于 $T$；$T$ 与组成；$T$ 与 $p$。凝聚相的摩尔体积很小，压力项通常可以忽略：水的 $V^*_{\mathrm{m}} = 18\,\mathrm{cm^3\,mol^{-1}}$，压力改变 $1\,\mathrm{MPa}$ 时压力项只有 $18\,\mathrm{J\,mol^{-1}}$，而 $298\,\mathrm{K}$ 时 $x_{\mathrm{B}} = 0.5$ 对应的 $RT\ln x_{\mathrm{B}} = -1.7\,\mathrm{kJ\,mol^{-1}}$。压力不大时，

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) \approx \mu^\circ_{\mathrm{B}}(\mathrm{l}, T) + RT\ln x_{\mathrm{B}}.
$$

式 (5.2) 与理想气体混合物中组分的化学势 $\mu_{\mathrm{B}} = \mu^*_{\mathrm{B}}(T, p) + RT\ln y_{\mathrm{B}}$（[6.3.4](/6.3.4)）形式完全相同，只是纯物质的化学势换成纯液体的。这一相似决定了两者的混合性质也相同。

### 5.1.4. 混合性质

在等温等压下把 $n_{\mathrm{A}}$ 的纯液体 A 与 $n_{\mathrm{B}}$ 的纯液体 B 混合成理想液态混合物，各广延性质的变化称为混合性质，记作 $\Delta_{\mathrm{mix}}V$、$\Delta_{\mathrm{mix}}H$、$\Delta_{\mathrm{mix}}S$、$\Delta_{\mathrm{mix}}G$。

**定义 5.1.2** 等温等压下由纯组分混合成混合物时 Gibbs 自由能的变化

$$
\Delta_{\mathrm{mix}}G = \sum_{\mathrm{B}}n_{\mathrm{B}}\mu_{\mathrm{B}} - \sum_{\mathrm{B}}n_{\mathrm{B}}\mu^*_{\mathrm{B}}
$$
称为**混合 Gibbs 自由能**；其余混合性质的定义类推。

**定理 5.1.1（理想液态混合物的混合性质）** 等温等压下由纯液体配制理想液态混合物时

$$
\Delta_{\mathrm{mix}}V = 0, \qquad \Delta_{\mathrm{mix}}H = 0, \qquad \Delta_{\mathrm{mix}}S = -R\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}, \qquad \Delta_{\mathrm{mix}}G = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}.
$$

**证明** 由偏摩尔量的加和公式，$\Delta_{\mathrm{mix}}V = \sum_{\mathrm{B}}n_{\mathrm{B}}(V_{\mathrm{B}} - V^*_{\mathrm{m,B}})$。对式 (5.2) 在恒定 $T$ 与组成下对 $p$ 求偏导，$RT\ln x_{\mathrm{B}}$ 与压力无关，所以 $V_{\mathrm{B}} = (\partial\mu_{\mathrm{B}}/\partial p)_{T,n} = (\partial\mu^*_{\mathrm{B}}/\partial p)_T = V^*_{\mathrm{m,B}}$，$\Delta_{\mathrm{mix}}V = 0$。

把式 (5.2) 两边除以 $T$ 再对 $T$ 求偏导，$R\ln x_{\mathrm{B}}$ 与温度无关；由 **Gibbs–Helmholtz 方程**的偏摩尔形式 $\left(\frac{\partial(\mu_{\mathrm{B}}/T)}{\partial T}\right)_{p,n} = -\frac{H_{\mathrm{B}}}{T^2}$（[6.3.3](/6.3.3)、[6.3.4](/6.3.4)）得 $H_{\mathrm{B}} = H^*_{\mathrm{m,B}}$，所以 $\Delta_{\mathrm{mix}}H = 0$。

$\Delta_{\mathrm{mix}}G = \sum_{\mathrm{B}}n_{\mathrm{B}}(\mu_{\mathrm{B}} - \mu^*_{\mathrm{B}}) = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}$；再由 $S_{\mathrm{B}} = -(\partial\mu_{\mathrm{B}}/\partial T)_{p,n} = S^*_{\mathrm{m,B}} - R\ln x_{\mathrm{B}}$ 得 $\Delta_{\mathrm{mix}}S$，它也等于 $(\Delta_{\mathrm{mix}}H - \Delta_{\mathrm{mix}}G)/T$。$\square$

由 $\Delta_{\mathrm{mix}}V = 0$、$\Delta_{\mathrm{mix}}H = 0$ 还得 $\Delta_{\mathrm{mix}}U = \Delta_{\mathrm{mix}}H - p\Delta_{\mathrm{mix}}V = 0$，$\Delta_{\mathrm{mix}}A = \Delta_{\mathrm{mix}}G$。概括地说：配制理想液态混合物时无体积效应、无热效应，熵增加，Gibbs 自由能减少。这与理想气体的等温等压混合完全相同，$\Delta_{\mathrm{mix}}S$ 就是 [6.3.2](/6.3.2) 的**混合熵**。它的统计意义是：A、B 分子可以互换位置而能量不变，$N$ 个格位上排列 $N_{\mathrm{A}}$ 个 A 与 $N_{\mathrm{B}}$ 个 B 的方式有 $\binom{N}{N_{\mathrm{A}}}$ 种，由 **Boltzmann 熵公式**（[5.2.4](/5.2.4)）与 **Stirling 公式**即得 $\Delta_{\mathrm{mix}}S = -k_{\mathrm{B}}\sum N_{\mathrm{B}}\ln x_{\mathrm{B}}$（[6.3.10](/6.3.10)）。理想液态混合物的混合是纯粹由熵推动的。

![298.15 K 时理想液态混合物的摩尔混合函数：混合焓与混合体积为零，TΔmixS 与 ΔmixG 关于 x = 1/2 对称，等摩尔时 ΔmixG,m = −RT ln 2](./plots/ideal-mixing-functions.py)

**例 5.1.2** $298.15\,\mathrm{K}$、常压下由 $1\,\mathrm{mol}$ A 与 $1\,\mathrm{mol}$ B 形成理想液态混合物，求混合过程的 $\Delta V$、$\Delta H$、$\Delta U$、$\Delta S$、$\Delta G$。

**解** $\Delta_{\mathrm{mix}}V = \Delta_{\mathrm{mix}}H = \Delta_{\mathrm{mix}}U = 0$；$\Delta_{\mathrm{mix}}S = -R(\ln 0.5 + \ln 0.5) = 2R\ln 2 = 11.53\,\mathrm{J\,K^{-1}}$；$\Delta_{\mathrm{mix}}G = -T\Delta_{\mathrm{mix}}S = -3.44\,\mathrm{kJ}$。反过来，在等温等压下把这一混合物分离成纯 A 与纯 B，$\Delta V = \Delta H = \Delta U = 0$，$\Delta S < 0$，$\Delta G = \Delta A = +3.44\,\mathrm{kJ}$：分离至少需要 $3.44\,\mathrm{kJ}$ 的**非体积功**。

## 5.2. Henry 定律与理想稀溶液

### 5.2.1. Henry 定律

Henry 在 1803 年研究气体在水中的溶解，得到 Henry 定律（Henry's law）：一定温度下，稀溶液中挥发性溶质的平衡分压与它在溶液中的摩尔分数成正比，

$$
p_{\mathrm{B}} = k_{x,\mathrm{B}}x_{\mathrm{B}}. \tag{5.4}
$$
比例系数 $k_{x,\mathrm{B}}$ 称为 Henry 常数（Henry's law constant），单位为 Pa，与温度、压力以及溶质和溶剂的本性有关。它也是一条极限定律，$x_{\mathrm{B}} \to 0$ 时严格成立。

$k_{x,\mathrm{B}}$ 一般不等于纯 B 的饱和蒸气压 $p^*_{\mathrm{B}}$：$p^*_{\mathrm{B}}$ 反映 B 分子在纯 B 中的逸出倾向，$k_{x,\mathrm{B}}$ 反映 B 分子被溶剂分子包围时的逸出倾向。若溶剂对 B 的吸引弱于 B 分子之间的吸引，B 在稀溶液中更容易逸出，$k_{x,\mathrm{B}} > p^*_{\mathrm{B}}$；反之 $k_{x,\mathrm{B}} < p^*_{\mathrm{B}}$。理想液态混合物中两者相等，Henry 定律与 Raoult 定律重合。$k_{x,\mathrm{B}}$ 可以理解为把稀溶液中 Henry 定律的直线外推到 $x_{\mathrm{B}} = 1$ 时的"蒸气压"：这是一个假想的状态，但它在 5.2.3 中有用。

使用 Henry 定律时要注意：

1. 溶质在气相与溶液中的分子形态必须相同。强电解质（如 HCl 在水中）不适用；$\ce{SO2}$、$\ce{NH3}$、$\ce{CO2}$ 等在水中部分反应或解离的气体，$x_{\mathrm{B}}$ 只算以溶解分子形态存在的部分。
2. 压力不大时，几种气体同时溶解，可以对每种气体分别使用（各有自己的 Henry 常数），$p_{\mathrm{B}}$ 是该气体的分压。
3. 浓度也可以用**质量摩尔浓度** $b_{\mathrm{B}}$ 或**物质的量浓度** $c_{\mathrm{B}}$ 表示：

$$
p_{\mathrm{B}} = k_{b,\mathrm{B}}\frac{b_{\mathrm{B}}}{b^\circ} = k_{c,\mathrm{B}}\frac{c_{\mathrm{B}}}{c^\circ}, \qquad b^\circ = 1\,\mathrm{mol\,kg^{-1}}, \quad c^\circ = 1\,\mathrm{mol\,L^{-1}}.
$$
稀溶液中 $x_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{n_{\mathrm{A}} + n_{\mathrm{B}}} \to \frac{n_{\mathrm{B}}}{n_{\mathrm{A}}} = M_{\mathrm{A}}b_{\mathrm{B}}$，$c_{\mathrm{B}} \to \rho^*_{\mathrm{A}}b_{\mathrm{B}}$（$M_{\mathrm{A}}$、$\rho^*_{\mathrm{A}}$ 为溶剂的摩尔质量与密度），比较极限斜率得

$$
k_{b,\mathrm{B}} = k_{x,\mathrm{B}}M_{\mathrm{A}}b^\circ, \qquad k_{c,\mathrm{B}} = k_{x,\mathrm{B}}\frac{M_{\mathrm{A}}c^\circ}{\rho^*_{\mathrm{A}}}. \tag{5.5}
$$
三个常数数值不同、单位都是 Pa，换算是严格的（它们都是 $x_{\mathrm{B}} \to 0$ 处的极限斜率）。文献中也常用 Henry 定律的"溶解度形式" $c_{\mathrm{B}} = H^{cp}p_{\mathrm{B}}$，使用时要看清定义。

**例 5.2.1** $25\,^\circ\mathrm{C}$ 时 $\ce{O2}$ 分压为 $101.325\,\mathrm{kPa}$ 时在水中的平衡摩尔分数为 $2.29 \times 10^{-5}$（CRC Handbook），求 $k_{x}(\ce{O2})$ 与 $101.325\,\mathrm{kPa}$ 下空气饱和水中的溶解氧。

**解** $k_x = 101.325\,\mathrm{kPa}/(2.29 \times 10^{-5}) = 4.42 \times 10^9\,\mathrm{Pa}$。与水接触的空气被水蒸气饱和，干空气的分压为 $(101.325 - 3.17)\,\mathrm{kPa}$，其中 $p(\ce{O2}) = 0.2095 \times 98.16\,\mathrm{kPa} = 20.6\,\mathrm{kPa}$，$x(\ce{O2}) = 20.6 \times 10^3/(4.42 \times 10^9) = 4.65 \times 10^{-6}$，$b = x/M_{\mathrm{A}} = 2.58 \times 10^{-4}\,\mathrm{mol\,kg^{-1}}$，约 $8.2\,\mathrm{mg\,L^{-1}}$（实测 $8.3\,\mathrm{mg\,L^{-1}}$）。Henry 常数达到 GPa 量级，说明 $\ce{O2}$ 在水中极难溶：$k_x \gg p^*$ 正是溶剂与溶质相互作用弱的表现。血浆中直接溶解的 $\ce{O2}$ 同样服从 Henry 定律，数量很少；血液运输的氧绝大部分与血红蛋白结合，那是一个化学平衡，不服从 Henry 定律。

气体的溶解度随压力与温度变化。由 Henry 定律，恒温下气体的溶解度与其分压成正比。潜水员下潜 $30\,\mathrm{m}$ 时呼吸的空气压力约为 $0.4\,\mathrm{MPa}$，血液与组织中溶解的 $\ce{N2}$ 约为海面的 4 倍；上升过快时外压骤降，溶解的 $\ce{N2}$ 来不及经肺排出，在血管与组织中析出气泡，这就是减压病，所以必须缓慢上浮（或分段停留）。

温度的影响由化学势导出。溶质 B 在气相与溶液中平衡，$\mu^\circ_{\mathrm{B}}(\mathrm{g}, T) + RT\ln(p_{\mathrm{B}}/p^\circ) = \mu_{\mathrm{B}}(\mathrm{sln})$；按 5.2.3 把溶液中溶质的化学势写成 $\mu^*_{x,\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}$，代入 $p_{\mathrm{B}} = k_{x,\mathrm{B}}x_{\mathrm{B}}$ 得

$$
\ln\frac{k_{x,\mathrm{B}}}{p^\circ} = \frac{\mu^*_{x,\mathrm{B}}(T, p) - \mu^\circ_{\mathrm{B}}(\mathrm{g}, T)}{RT}.
$$
对 $T$ 求导并用 Gibbs–Helmholtz 方程，

$$
\frac{\mathrm{d}\ln k_{x,\mathrm{B}}}{\mathrm{d}T} = -\frac{H^{\infty}_{\mathrm{B}} - H^\circ_{\mathrm{m,B}}(\mathrm{g})}{RT^2} = -\frac{\Delta_{\mathrm{sol}}H^{\infty}_{\mathrm{m}}}{RT^2},
$$
其中 $H^{\infty}_{\mathrm{B}}$ 是 B 在无限稀溶液中的偏摩尔焓，$\Delta_{\mathrm{sol}}H^{\infty}_{\mathrm{m}}$ 是 $1\,\mathrm{mol}$ 气体溶入大量溶剂时的焓变。气体溶解通常放热（$\Delta_{\mathrm{sol}}H^{\infty}_{\mathrm{m}} < 0$），$k_{x,\mathrm{B}}$ 随温度升高而增大，一定分压下的溶解度 $x_{\mathrm{B}} = p_{\mathrm{B}}/k_{x,\mathrm{B}}$ 随温度升高而减小：温暖的水体溶解氧更少。固体在理想溶液中的溶解度则随温度升高而增大：饱和时 $\mu^*_{\mathrm{B}}(\mathrm{s}) = \mu^*_{\mathrm{B}}(\mathrm{l}) + RT\ln x_{\mathrm{B}}$，同样的推导给出 $\frac{\mathrm{d}\ln x_{\mathrm{B}}}{\mathrm{d}T} = \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,B}}}{RT^2} > 0$，这正是 5.3.2 凝固点降低公式中溶剂与溶质角色互换的形式，它给出低共熔相图的液相线（[6.3.9](/6.3.9)）。

### 5.2.2. 理想稀溶液

**定义 5.2.1（理想稀溶液）** 在一定的浓度范围内，溶剂服从 Raoult 定律、溶质服从 Henry 定律的溶液称为**理想稀溶液**。

这是一个极限模型：任何非电解质溶液在 $x_{\mathrm{B}} \to 0$ 时都趋于理想稀溶液，但"浓度很小"并不保证理想，电解质溶液在很稀时就明显偏离（[6.3.12](/6.3.12)）。两条定律并不独立：只要溶质在某一浓度范围内服从 Henry 定律，溶剂在同一范围内必定服从 Raoult 定律。

**证明** 等温等压下，由 **Gibbs–Duhem 方程**，$x_{\mathrm{A}}\,\mathrm{d}\mu_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}} = 0$。溶质服从 Henry 定律即 $\mu_{\mathrm{B}} = \text{常数} + RT\ln x_{\mathrm{B}}$（5.2.3），$\mathrm{d}\mu_{\mathrm{B}} = RT\,\mathrm{d}x_{\mathrm{B}}/x_{\mathrm{B}}$，于是

$$
\mathrm{d}\mu_{\mathrm{A}} = -\frac{x_{\mathrm{B}}}{x_{\mathrm{A}}}RT\frac{\mathrm{d}x_{\mathrm{B}}}{x_{\mathrm{B}}} = RT\frac{\mathrm{d}x_{\mathrm{A}}}{x_{\mathrm{A}}}.
$$
从 $x_{\mathrm{A}} = 1$（纯溶剂，$\mu_{\mathrm{A}} = \mu^*_{\mathrm{A}}$）积分，得 $\mu_{\mathrm{A}} = \mu^*_{\mathrm{A}} + RT\ln x_{\mathrm{A}}$，即 Raoult 定律。$\square$

溶剂的化学势与理想液态混合物中的组分相同：

$$
\mu_{\mathrm{A}}(\mathrm{sln}, T, p) = \mu^*_{\mathrm{A}}(\mathrm{l}, T, p) + RT\ln x_{\mathrm{A}} = \mu^\circ_{\mathrm{A}}(\mathrm{l}, T) + RT\ln x_{\mathrm{A}} + \int_{p^\circ}^{p}V^*_{\mathrm{m,A}}\,\mathrm{d}p, \tag{5.6}
$$
标准态是 $T$、$p^\circ$ 下的纯溶剂，是真实存在的状态。

### 5.2.3. 溶质的化学势与三种标准态

由溶质 B 的气液平衡与 Henry 定律 (5.4)，

$$
\mu_{\mathrm{B}}(\mathrm{sln}) = \mu^\circ_{\mathrm{B}}(\mathrm{g}, T) + RT\ln\frac{k_{x,\mathrm{B}}}{p^\circ} + RT\ln x_{\mathrm{B}} \equiv \mu^*_{x,\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}. \tag{5.7}
$$
$\mu^*_{x,\mathrm{B}}(T, p)$ 是 $x_{\mathrm{B}} = 1$ 而仍服从 Henry 定律的"纯 B"的化学势，它的蒸气压是 $k_{x,\mathrm{B}}$。这是假想态：真实的纯 B 蒸气压是 $p^*_{\mathrm{B}}$，化学势是 $\mu^*_{\mathrm{B}}$，两者相差 $RT\ln(k_{x,\mathrm{B}}/p^*_{\mathrm{B}})$。假想态的意义在于它保留了无限稀溶液中 B 的性质：每个 B 分子周围都是溶剂分子。因此它的摩尔体积与摩尔焓分别是 B 在无限稀溶液中的偏摩尔体积 $V^{\infty}_{\mathrm{B}}$ 与偏摩尔焓 $H^{\infty}_{\mathrm{B}}$，而不是纯 B 的 $V^*_{\mathrm{m,B}}$、$H^*_{\mathrm{m,B}}$。

用 $b_{\mathrm{B}}$ 或 $c_{\mathrm{B}}$ 表示 Henry 定律，同样得到

$$
\mu_{\mathrm{B}}(\mathrm{sln}) = \mu^*_{b,\mathrm{B}}(T, p) + RT\ln\frac{b_{\mathrm{B}}}{b^\circ} = \mu^*_{c,\mathrm{B}}(T, p) + RT\ln\frac{c_{\mathrm{B}}}{c^\circ},
$$
参考态分别是 $b_{\mathrm{B}} = b^\circ$ 与 $c_{\mathrm{B}} = c^\circ$ 时仍服从 Henry 定律的假想溶液。规定压力为 $p^\circ$ 时，这些参考态就是溶质的三种**标准态**，其化学势记作 $\mu^\circ_{x,\mathrm{B}}(T)$、$\mu^\circ_{b,\mathrm{B}}(T)$、$\mu^\circ_{c,\mathrm{B}}(T)$，例如

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) = \mu^\circ_{b,\mathrm{B}}(T) + RT\ln\frac{b_{\mathrm{B}}}{b^\circ} + \int_{p^\circ}^{p}V^{\infty}_{\mathrm{B}}\,\mathrm{d}p. \tag{5.8}
$$

| 浓度标度 | 化学势 | 标准态（$T$，$p^\circ$） | 是否真实 |
|---|---|---|---|
| 溶剂 $x_{\mathrm{A}}$ | $\mu^\circ_{\mathrm{A}}(\mathrm{l}, T) + RT\ln x_{\mathrm{A}}$ | 纯溶剂 A | 真实 |
| 溶质 $x_{\mathrm{B}}$ | $\mu^\circ_{x,\mathrm{B}}(T) + RT\ln x_{\mathrm{B}}$ | $x_{\mathrm{B}} = 1$ 且服从 Henry 定律的 B | 假想 |
| 溶质 $b_{\mathrm{B}}$ | $\mu^\circ_{b,\mathrm{B}}(T) + RT\ln(b_{\mathrm{B}}/b^\circ)$ | $b_{\mathrm{B}} = 1\,\mathrm{mol\,kg^{-1}}$ 且服从 Henry 定律 | 假想 |
| 溶质 $c_{\mathrm{B}}$ | $\mu^\circ_{c,\mathrm{B}}(T) + RT\ln(c_{\mathrm{B}}/c^\circ)$ | $c_{\mathrm{B}} = 1\,\mathrm{mol\,L^{-1}}$ 且服从 Henry 定律 | 假想 |

（表中略去了压力项。）对给定状态的溶液，溶质的化学势只有一个值，三种写法只是把它分成"标准化学势 + 浓度项"的方式不同。由稀溶液中 $x_{\mathrm{B}} \to M_{\mathrm{A}}b_{\mathrm{B}}$，比较三种写法得

$$
\mu^\circ_{b,\mathrm{B}} = \mu^\circ_{x,\mathrm{B}} + RT\ln(M_{\mathrm{A}}b^\circ), \qquad \mu^\circ_{c,\mathrm{B}} = \mu^\circ_{x,\mathrm{B}} + RT\ln\frac{M_{\mathrm{A}}c^\circ}{\rho^*_{\mathrm{A}}},
$$
与式 (5.5) 一致。水溶液中 $M_{\mathrm{A}}b^\circ = 0.018015$，$298.15\,\mathrm{K}$ 时 $RT\ln(M_{\mathrm{A}}b^\circ) = -9.96\,\mathrm{kJ\,mol^{-1}}$：标准态不同，标准化学势可以相差近 $10\,\mathrm{kJ\,mol^{-1}}$，所以溶液中的热力学数据（如 [6.1.6](/6.1.6) 表中水合物种的 $\Delta_{\mathrm{f}}G^\circ$）必须注明所用的标准态，通常是 $b^\circ$。

溶质与溶剂的表达式有三点不同：标准态（溶剂是真实的纯液体，溶质是假想态）；压力项的被积函数（$V^*_{\mathrm{m,A}}$ 与 $V^{\infty}_{\mathrm{B}}$）；溶质有多种等价的表达形式。

## 5.3. 稀溶液的依数性

一定温度和压力下，稀溶液的某些性质只取决于溶质粒子的数目，而与溶质的本性无关，称为依数性（colligative properties）：蒸气压降低、凝固点降低、沸点升高与渗透压。它们的共同根源是溶剂的化学势因溶质而降低：$\mu_{\mathrm{A}} - \mu^*_{\mathrm{A}} = RT\ln x_{\mathrm{A}} < 0$，降低的量只取决于 $x_{\mathrm{A}}$，并且它来自混合熵，与溶质分子的能量无关。

在恒压下画出溶剂化学势随温度的变化（斜率 $(\partial\mu/\partial T)_p = -S_{\mathrm{m}}$，气 > 液 > 固），液相线下移 $RT\ln x_{\mathrm{A}}$ 后与固相线、气相线的交点分别向低温、高温移动，凝固点降低、沸点升高便一目了然。前提是溶质不进入固相与气相：溶质不挥发，凝固时只析出纯溶剂。

![恒压下溶剂化学势随温度变化的示意图：溶质使液相线下移 RT ln x_A（图中夸大），与固相线的交点移到较低温度（凝固点降低），与气相线的交点移到较高温度（沸点升高）](./plots/colligative-mu-t.py)

### 5.3.1. 蒸气压降低

溶质不挥发时，溶液的蒸气压就是溶剂的分压。由 Raoult 定律，

$$
\Delta p = p^*_{\mathrm{A}} - p_{\mathrm{A}} = p^*_{\mathrm{A}}(1 - x_{\mathrm{A}}) = p^*_{\mathrm{A}}x_{\mathrm{B}},
$$
蒸气压降低（vapor-pressure lowering）的相对值 $\Delta p/p^*_{\mathrm{A}}$ 等于溶质的摩尔分数。溶质挥发时，溶剂的分压仍按 Raoult 定律降低，但总蒸气压可能升高。

### 5.3.2. 凝固点降低

凝固点是一定压力下固、液两相平衡共存的温度。若溶液冷却时析出的是纯固态溶剂 A（不形成**固溶体**），则溶液的凝固点 $T_{\mathrm{f}}$ 低于纯溶剂的 $T^*_{\mathrm{f}}$，即凝固点降低（freezing-point depression）。

**定理 5.3.1** 理想液态混合物或理想稀溶液在凝固点时只析出纯固态溶剂 A，且溶剂的摩尔熔化焓 $\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}$ 在 $T_{\mathrm{f}}$ 与 $T^*_{\mathrm{f}}$ 之间不随温度变化，则

$$
\ln x_{\mathrm{A}} = -\frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}}{R}\left(\frac{1}{T_{\mathrm{f}}} - \frac{1}{T^*_{\mathrm{f}}}\right). \tag{5.9}
$$
溶液很稀（$x_{\mathrm{B}} \ll 1$）时，

$$
\Delta T_{\mathrm{f}} = T^*_{\mathrm{f}} - T_{\mathrm{f}} = K_{\mathrm{f}}b_{\mathrm{B}}, \qquad K_{\mathrm{f}} = \frac{R(T^*_{\mathrm{f}})^2M_{\mathrm{A}}}{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}}. \tag{5.10}
$$

**证明** 凝固点下固液平衡，$\mu_{\mathrm{A}}(\mathrm{sln}, T, p, x_{\mathrm{A}}) = \mu^*_{\mathrm{A}}(\mathrm{s}, T, p)$。代入式 (5.6)：

$$
\ln x_{\mathrm{A}} = \frac{\mu^*_{\mathrm{A}}(\mathrm{s}) - \mu^*_{\mathrm{A}}(\mathrm{l})}{RT} = -\frac{\Delta_{\mathrm{fus}}G_{\mathrm{m,A}}(T)}{RT},
$$
其中 $\Delta_{\mathrm{fus}}G_{\mathrm{m,A}}(T)$ 是纯 A 在温度 $T$ 下熔化的摩尔 Gibbs 自由能变化。这一等式在每个凝固点都成立，即它确定了凝固点 $T$ 与组成 $x_{\mathrm{A}}$ 的函数关系。恒压下对 $T$ 求导，由 Gibbs–Helmholtz 方程 $\frac{\mathrm{d}(\Delta G/T)}{\mathrm{d}T} = -\frac{\Delta H}{T^2}$，

$$
\frac{\mathrm{d}\ln x_{\mathrm{A}}}{\mathrm{d}T} = \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}}{RT^2}.
$$
从纯溶剂（$x_{\mathrm{A}} = 1$，$T = T^*_{\mathrm{f}}$）积分到溶液（$x_{\mathrm{A}}$，$T_{\mathrm{f}}$），熔化焓为常数时即得式 (5.9)。

稀溶液中 $\ln x_{\mathrm{A}} = \ln(1 - x_{\mathrm{B}}) = -x_{\mathrm{B}} - \frac{x_{\mathrm{B}}^2}{2} - \cdots \approx -x_{\mathrm{B}}$，又 $\frac{1}{T_{\mathrm{f}}} - \frac{1}{T^*_{\mathrm{f}}} = \frac{\Delta T_{\mathrm{f}}}{T_{\mathrm{f}}T^*_{\mathrm{f}}} \approx \frac{\Delta T_{\mathrm{f}}}{(T^*_{\mathrm{f}})^2}$，于是 $x_{\mathrm{B}} = \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}\Delta T_{\mathrm{f}}}{R(T^*_{\mathrm{f}})^2}$；再由 $x_{\mathrm{B}} \approx n_{\mathrm{B}}/n_{\mathrm{A}} = M_{\mathrm{A}}b_{\mathrm{B}}$ 得式 (5.10)。$\square$

$K_{\mathrm{f}}$ 称为凝固点降低常数（cryoscopic constant），只与溶剂有关。水：$T^*_{\mathrm{f}} = 273.15\,\mathrm{K}$，$\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 6.01\,\mathrm{kJ\,mol^{-1}}$，$K_{\mathrm{f}} = 1.86\,\mathrm{K\,kg\,mol^{-1}}$；苯：$T^*_{\mathrm{f}} = 278.7\,\mathrm{K}$，$\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 9.87\,\mathrm{kJ\,mol^{-1}}$，$K_{\mathrm{f}} = 5.11\,\mathrm{K\,kg\,mol^{-1}}$。熔化焓小、熔点高、摩尔质量大的溶剂（如樟脑，$K_{\mathrm{f}} \approx 40\,\mathrm{K\,kg\,mol^{-1}}$）凝固点降低更显著。

式 (5.10) 的两个近似（对数展开与 $T_{\mathrm{f}} \approx T^*_{\mathrm{f}}$）在 $b_{\mathrm{B}} = 1\,\mathrm{mol\,kg^{-1}}$ 时合计约 1.5%（线性律给出 $1.86\,\mathrm{K}$，积分式给出 $1.83\,\mathrm{K}$）；更浓时还要考虑熔化焓随温度的变化（$\Delta_{\mathrm{fus}}C_p = C_{p,\mathrm{m}}(\mathrm{l}) - C_{p,\mathrm{m}}(\mathrm{s})$，**Kirchhoff 定律**，[6.3.1](/6.3.1)）以及溶液本身的非理想性（[6.3.6](/6.3.6)）。

![水的凝固点降低（溶液按理想处理）：线性律 K_f b 与积分式（熔化焓为常数）、以及计入 ΔfusCp 的积分式的比较；4 mol/kg 时三者分别为 7.4、7.0、7.2 K](./plots/freezing-point-depression.py)

应用：

1. 测定摩尔质量：由 $\Delta T_{\mathrm{f}}$ 与溶质质量求 $b_{\mathrm{B}}$，进而求 $M_{\mathrm{B}}$（葡萄糖、氨基酸、肾上腺素等）。若溶质在溶液中缔合或解离，测得的是"表观摩尔质量"，可以由此研究缔合与解离。
2. 测定溶液中所有溶质粒子的总浓度：人的血清凝固点约 $-0.56\,^\circ\mathrm{C}$，$b = 0.56/1.86 = 0.30\,\mathrm{mol\,kg^{-1}}$，临床上称为渗透质量摩尔浓度（约 $300\,\mathrm{mOsm\,kg^{-1}}$），所有离子与分子都计入。海水的冰点约 $-1.9\,^\circ\mathrm{C}$，对应约 $1.0\,\mathrm{mol\,kg^{-1}}$ 的溶质粒子。
3. 检验纯度：杂质使熔点降低、熔程变宽，这是有机化学中用熔点鉴定纯度的依据。
4. 防冻：汽车防冻液（乙二醇水溶液）、道路撒盐。耐寒植物在低温下把淀粉转化为可溶性糖，提高细胞液浓度，既降低凝固点又减少胞内结冰，经霜的白菜因此更甜。某些极地鱼类的抗冻蛋白则不是依数性效应：它们吸附在冰晶表面阻止冰的生长，浓度很低时就能使冰点下降约 $1\,\mathrm{K}$，远超依数性的预期。

### 5.3.3. 沸点升高

沸点是液体的蒸气压等于外压时的温度。溶质不挥发时溶液的蒸气压低于纯溶剂，要升到更高的温度才能达到外压：沸点升高（boiling-point elevation）。

**定理 5.3.2** 溶质不挥发的理想稀溶液，在溶剂的**摩尔蒸发焓** $\Delta_{\mathrm{vap}}H_{\mathrm{m,A}}$ 为常数时

$$
\ln x_{\mathrm{A}} = \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m,A}}}{R}\left(\frac{1}{T_{\mathrm{b}}} - \frac{1}{T^*_{\mathrm{b}}}\right), \qquad \Delta T_{\mathrm{b}} = T_{\mathrm{b}} - T^*_{\mathrm{b}} = K_{\mathrm{b}}b_{\mathrm{B}}, \quad K_{\mathrm{b}} = \frac{R(T^*_{\mathrm{b}})^2M_{\mathrm{A}}}{\Delta_{\mathrm{vap}}H_{\mathrm{m,A}}}. \tag{5.11}
$$

**证明** 沸点下溶剂在溶液与纯蒸气之间平衡（蒸气中没有溶质），$\mu_{\mathrm{A}}(\mathrm{sln}, T, p) = \mu^*_{\mathrm{A}}(\mathrm{g}, T, p)$，

$$
\ln x_{\mathrm{A}} = \frac{\mu^*_{\mathrm{A}}(\mathrm{g}) - \mu^*_{\mathrm{A}}(\mathrm{l})}{RT} = \frac{\Delta_{\mathrm{vap}}G_{\mathrm{m,A}}(T)}{RT}.
$$
由 Gibbs–Helmholtz 方程，$\frac{\mathrm{d}\ln x_{\mathrm{A}}}{\mathrm{d}T} = -\frac{\Delta_{\mathrm{vap}}H_{\mathrm{m,A}}}{RT^2}$，从 $x_{\mathrm{A}} = 1$、$T = T^*_{\mathrm{b}}$ 积分得第一式。稀溶液近似与 5.3.2 相同：$-\ln x_{\mathrm{A}} \approx x_{\mathrm{B}} \approx M_{\mathrm{A}}b_{\mathrm{B}}$，$T_{\mathrm{b}}T^*_{\mathrm{b}} \approx (T^*_{\mathrm{b}})^2$。$\square$

这与 **Clausius–Clapeyron 方程**（[6.1.1](/6.1.1)）是同一个结果的两种看法：Raoult 定律把蒸气压曲线整体下移 $\Delta p = p^*_{\mathrm{A}}x_{\mathrm{B}}$，蒸气压曲线的斜率 $\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}p}{RT^2}$ 把这一压力差换算成温度差 $\Delta T_{\mathrm{b}} = \Delta p/(\mathrm{d}p/\mathrm{d}T)$，结果相同。

$K_{\mathrm{b}}$ 称为沸点升高常数（ebullioscopic constant）。水在 $101.325\,\mathrm{kPa}$ 下 $T^*_{\mathrm{b}} = 373.12\,\mathrm{K}$，$\Delta_{\mathrm{vap}}H_{\mathrm{m}} = 40.65\,\mathrm{kJ\,mol^{-1}}$，$K_{\mathrm{b}} = 0.513\,\mathrm{K\,kg\,mol^{-1}}$，只有 $K_{\mathrm{f}}$ 的约四分之一（蒸发焓大），所以沸点升高法不如凝固点降低法灵敏。注意"稀溶液的沸点一定比纯溶剂高"的说法只对不挥发的溶质成立；乙醇的水溶液沸点就低于水。

### 5.3.4. 渗透压

只允许溶剂分子通过、不允许溶质分子通过的膜称为半透膜（semipermeable membrane）。用半透膜把纯溶剂与溶液隔开，溶剂会自发地透过膜进入溶液一侧，使溶液液面升高，这就是渗透。原因是同温同压下 $\mu^*_{\mathrm{A}}(T, p) > \mu_{\mathrm{A}}(\mathrm{sln}, T, p)$。在溶液一侧施加额外的压力 $\varPi$ 可以阻止渗透：压力升高使溶液中溶剂的化学势增大（$(\partial\mu_{\mathrm{A}}/\partial p)_T = V_{\mathrm{A}} > 0$），当它与纯溶剂的化学势相等时达到渗透平衡。

**定义 5.3.1** 用半透膜隔开的纯溶剂与溶液达到渗透平衡时，溶液一侧必须比纯溶剂一侧多承受的压力 $\varPi$ 称为该溶液的**渗透压**：

$$
\mu^*_{\mathrm{A}}(\mathrm{l}, T, p) = \mu_{\mathrm{A}}(\mathrm{sln}, T, p + \varPi, x_{\mathrm{A}}).
$$

按这一定义，渗透压是溶液本身的性质，任何溶液都有，只是没有半透膜就表现不出来。

**定理 5.3.3** 对理想液态混合物或理想稀溶液，若溶剂不可压缩，则

$$
\varPi V^*_{\mathrm{m,A}} = -RT\ln x_{\mathrm{A}}; \tag{5.12}
$$
对理想稀溶液（$x_{\mathrm{B}} \ll 1$）近似为 van 't Hoff 渗透压公式

$$
\varPi = c_{\mathrm{B}}RT. \tag{5.13}
$$

**证明** 由式 (5.6)，$\mu_{\mathrm{A}}(\mathrm{sln}, T, p + \varPi) = \mu^*_{\mathrm{A}}(\mathrm{l}, T, p + \varPi) + RT\ln x_{\mathrm{A}}$，而 $\mu^*_{\mathrm{A}}(\mathrm{l}, T, p + \varPi) - \mu^*_{\mathrm{A}}(\mathrm{l}, T, p) = \int_p^{p+\varPi}V^*_{\mathrm{m,A}}\,\mathrm{d}p = \varPi V^*_{\mathrm{m,A}}$。代入渗透平衡条件即得式 (5.12)。稀溶液中 $-\ln x_{\mathrm{A}} \approx x_{\mathrm{B}} \approx n_{\mathrm{B}}/n_{\mathrm{A}}$，又 $n_{\mathrm{A}}V^*_{\mathrm{m,A}} \approx V$（溶液体积），所以 $\varPi \approx n_{\mathrm{B}}RT/V = c_{\mathrm{B}}RT$。$\square$

式 (5.13) 由 van 't Hoff 在 1886 年提出，形式与理想气体的物态方程相同，但溶质分子并没有像气体分子那样"撞击"半透膜：渗透压来自溶剂化学势的降低，即混合熵。式中 $c_{\mathrm{B}}$ 的单位是 $\mathrm{mol\,m^{-3}}$。对电解质，$c_{\mathrm{B}}$ 要换成所有溶质粒子的总浓度。

**例 5.3.1** 求 $25\,^\circ\mathrm{C}$ 时 $b_{\mathrm{B}} = 0.001\,\mathrm{mol\,kg^{-1}}$ 的非电解质水溶液的四种依数性。已知 $p^*(\ce{H2O}) = 3.17\,\mathrm{kPa}$。

**解** $x_{\mathrm{B}} \approx M_{\mathrm{A}}b_{\mathrm{B}} = 1.80 \times 10^{-5}$，$\Delta p = p^*_{\mathrm{A}}x_{\mathrm{B}} = 0.057\,\mathrm{Pa}$；$\Delta T_{\mathrm{f}} = 1.86 \times 10^{-3}\,\mathrm{K}$；$\Delta T_{\mathrm{b}} = 5.1 \times 10^{-4}\,\mathrm{K}$；$c_{\mathrm{B}} \approx \rho^*_{\mathrm{A}}b_{\mathrm{B}} = 0.997\,\mathrm{mol\,m^{-3}}$，$\varPi = 0.997 \times 8.314 \times 298.15 = 2.47\,\mathrm{kPa}$，相当于约 $25\,\mathrm{cm}$ 水柱。四种依数性中渗透压最显著，因此渗透压法适合测定大分子的摩尔质量：$1\,\mathrm{g\,L^{-1}}$、摩尔质量 $10^5\,\mathrm{g\,mol^{-1}}$ 的蛋白质溶液，$\varPi \approx 25\,\mathrm{Pa}$ 仍可精确测定，而凝固点只降低 $2 \times 10^{-5}\,\mathrm{K}$。大分子溶液偏离理想较早，实际按 $\varPi/c = RT(1/M + A_2c + \cdots)$ 作图外推到 $c \to 0$（[6.3.21](/6.3.21)），测得的是数均摩尔质量。

**例 5.3.2** 人的血液在 $37\,^\circ\mathrm{C}$ 时渗透压为 $776\,\mathrm{kPa}$。把 NaCl 水溶液视为理想稀溶液、NaCl 完全解离，求与血液等渗的 NaCl 溶液的质量摩尔浓度。

**解** 溶质粒子总浓度 $c = \varPi/RT = 776 \times 10^3/(8.314 \times 310.15) = 301\,\mathrm{mol\,m^{-3}}$，每个 NaCl 给出两个离子，$c(\ce{NaCl}) = 150\,\mathrm{mol\,m^{-3}}$，$b(\ce{NaCl}) \approx c/\rho^*_{\mathrm{A}} = 0.150\,\mathrm{mol\,kg^{-1}}$，即每千克水含 $8.8\,\mathrm{g}$ NaCl。医用生理盐水是 $0.9\%$（质量分数，约 $9\,\mathrm{g}$ NaCl 每升溶液）：实际的 NaCl 溶液不是理想的，离子之间的相互作用使有效粒子数约为理想值的 0.93（渗透系数，[6.3.12](/6.3.12)），所以浓度要略高于理想估计。与 5.3.2 的血清冰点比较：$0.30\,\mathrm{mol\,kg^{-1}}$ 的粒子在 $37\,^\circ\mathrm{C}$ 产生约 $770\,\mathrm{kPa}$ 的渗透压，两种测定一致。

渗透压在生物中的作用：

- 细胞膜对水通透、对许多溶质不通透，近似为半透膜。红细胞放入纯水会吸水胀破（溶血），放入浓盐水会失水皱缩，所以静脉输液要用等渗溶液（$0.9\%$ NaCl 或 $5\%$ 葡萄糖）。
- 血浆中的蛋白质（主要是白蛋白）不能透过毛细血管壁，产生约 $3.3\,\mathrm{kPa}$（$25\,\mathrm{mmHg}$）的胶体渗透压，它与毛细血管中的静水压共同决定组织液的生成与回流。血浆蛋白过少时组织液回流减少，引起水肿。
- 植物细胞的膨压、气孔的开闭都靠渗透调节；高大树木的水分上升则主要由叶片蒸腾在木质部中形成的负压（张力）驱动，根部的渗透压（根压）只有约 $0.1$–$0.2\,\mathrm{MPa}$，不足以把水送上百米高的树冠。

在溶液一侧施加大于 $\varPi$ 的压力，溶剂就从溶液流向纯溶剂一侧，称为反渗透（reverse osmosis）。它用于海水淡化、溶液浓缩与废水处理。海水（盐度约 $35\,\mathrm{g\,kg^{-1}}$）的渗透压约 $2.7\,\mathrm{MPa}$，从海水中取出 $1\,\mathrm{m^3}$ 淡水的最小功约为 $\varPi V \approx 2.7\,\mathrm{MJ} = 0.75\,\mathrm{kWh}$（回收率趋于零时），现代反渗透装置约耗 $3\,\mathrm{kWh\,m^{-3}}$。反过来，河水与海水之间的渗透压差也可以用来发电（压力延迟渗透），每立方米淡水的理论可得能量同样约为 $0.75\,\mathrm{kWh}$。

## 小结

| 内容 | 要点 |
|---|---|
| Raoult 定律 | $p_{\mathrm{A}} = p^*_{\mathrm{A}}x_{\mathrm{A}}$，溶剂，$x_{\mathrm{A}} \to 1$ 的极限定律 |
| Henry 定律 | $p_{\mathrm{B}} = k_{x,\mathrm{B}}x_{\mathrm{B}} = k_{b,\mathrm{B}}b_{\mathrm{B}}/b^\circ = k_{c,\mathrm{B}}c_{\mathrm{B}}/c^\circ$，挥发性溶质，同一分子形态；$k_{x,\mathrm{B}} \ne p^*_{\mathrm{B}}$ |
| 理想液态混合物 | 各组分全浓度范围服从 Raoult 定律；$\mu_{\mathrm{B}} = \mu^*_{\mathrm{B}}(\mathrm{l}, T, p) + RT\ln x_{\mathrm{B}}$；$\Delta_{\mathrm{mix}}V = \Delta_{\mathrm{mix}}H = 0$，$\Delta_{\mathrm{mix}}S = -R\sum n_{\mathrm{B}}\ln x_{\mathrm{B}}$，$\Delta_{\mathrm{mix}}G = RT\sum n_{\mathrm{B}}\ln x_{\mathrm{B}}$ |
| 理想稀溶液 | 溶剂服从 Raoult 定律、溶质服从 Henry 定律（两者由 Gibbs–Duhem 方程相互蕴含） |
| 溶质的标准态 | $x_{\mathrm{B}} = 1$、$b^\circ$、$c^\circ$ 三种假想态，化学势相同、标准化学势不同；压力项用 $V^{\infty}_{\mathrm{B}}$ |
| 依数性 | 来自 $\mu_{\mathrm{A}} - \mu^*_{\mathrm{A}} = RT\ln x_{\mathrm{A}}$；$\Delta p = p^*_{\mathrm{A}}x_{\mathrm{B}}$，$\Delta T_{\mathrm{f}} = K_{\mathrm{f}}b_{\mathrm{B}}$，$\Delta T_{\mathrm{b}} = K_{\mathrm{b}}b_{\mathrm{B}}$，$\varPi = c_{\mathrm{B}}RT$；严格式 $\ln x_{\mathrm{A}} = -\frac{\Delta_{\mathrm{fus}}H}{R}(\frac{1}{T_{\mathrm{f}}} - \frac{1}{T^*_{\mathrm{f}}})$，$\varPi V^*_{\mathrm{m,A}} = -RT\ln x_{\mathrm{A}}$ |
| 适用条件 | 凝固点降低：只析出纯溶剂；沸点升高与蒸气压降低：溶质不挥发；渗透压：半透膜只让溶剂通过；电解质按粒子总数计 |

## 思考题

1. 两种液体能以任意比例混合，它们一定形成理想液态混合物吗？二组分理想液态混合物的总蒸气压一定大于任一纯组分的饱和蒸气压吗？

   **答** 都不一定。水与乙醇能任意混合，却明显偏离 Raoult 定律（[6.3.6](/6.3.6)）；反过来，理想液态混合物的 $\Delta_{\mathrm{mix}}G < 0$ 在全部组成都成立，所以它们一定能任意混合。理想液态混合物的总压介于两个纯组分的蒸气压之间。

2. 恒温抽空的玻璃罩中放一杯纯水和一杯糖水，足够长时间后会怎样？

   **答** 纯水的蒸气压高于糖水中水的分压，水不断从纯水杯蒸发、在糖水杯凝结，直到纯水杯蒸干（或糖水稀释到与纯水的蒸气压相等，这对不挥发溶质是不可能的）。

3. 理想稀溶液的四种依数性中，哪些对挥发性溶质也成立？

   **答** 凝固点降低（只要析出纯固态溶剂）与渗透压（只要半透膜不让溶质通过）只依赖于溶液中溶剂的化学势，对挥发性溶质同样成立；蒸气压降低与沸点升高的公式要求溶质不挥发。
