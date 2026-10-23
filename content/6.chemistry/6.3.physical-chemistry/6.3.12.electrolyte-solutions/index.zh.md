---
title: 电解质溶液
description: 离子导体与 Faraday 电解定律；电迁移率、迁移数与 Hittorf 法；电导率、摩尔电导率与 Kohlrausch 定律；离子独立迁移定律与电导法的应用；电解质的化学势、平均活度因子与离子强度；由线性化 Poisson–Boltzmann 方程推出 Debye–Hückel 理论，以及 Debye–Hückel–Onsager 电导理论。
---

电化学研究化学能与电能的相互转化。它的历史几乎与电学本身一样长：Galvani（1791）在蛙腿上观察到"动物电"，Volta（1800）用锌、铜片和浸了盐水的纸板叠成第一个持续电源，Faraday（1833–1834）发现电解产物的量与电量成正比，Kohlrausch（1875–1879）测量了大量溶液的电导，Arrhenius（1884–1887）提出电离理论，Nernst（1889）把电池电动势与反应的 Gibbs 自由能联系起来，Tafel（1905）给出了过电势与电流的经验关系。一个电化学系统由电解质、两个电极和外电路组成，三者分别对应本章、[6.3.13](/6.3.13)（零电流下电极与溶液界面的平衡）和 [6.3.14](/6.3.14)（有电流时电极过程的动力学）。

本章研究电解质溶液本身。它有两类性质：输运性质——离子在电场中迁移（12.2）、溶液导电（12.3–12.5）；热力学性质——离子之间的静电作用使电解质溶液即使很稀也明显偏离理想（12.6），Debye–Hückel 理论从静电学与统计力学出发定量地解释了这种偏离（12.7）。前者是物理 [5.3.5](/5.3.5) 中**电导率**与 **Ohm 定律**在离子导体中的具体化，后者把 [6.3.6](/6.3.6) 的**活度**与**活度因子**推广到电解质。数学上，12.7 用到 [2.5.1](/2.5.1) 的 **Poisson 方程**、[5.2.1](/5.2.1) 的 **Boltzmann 分布**，以及在**球坐标**中求解二阶常微分方程（[2.4.9](/2.4.9)）。这些结果也是生物物理的基础：细胞内液与体液都是离子强度约 $0.15\,\mathrm{mol\,kg^{-1}}$ 的电解质溶液，蛋白质、核酸周围的离子氛与 Debye 屏蔽决定了生物大分子之间的静电相互作用。

## 12.1. 电化学系统与 Faraday 定律

### 12.1.1. 两类导体与电解质

**定义 12.1.1** 靠自由电子（或空穴）的定向运动导电的导体称为**电子导体**（第一类导体），如金属、石墨和某些金属氧化物；靠离子的定向运动导电的导体称为**离子导体**（第二类导体），如电解质溶液、熔融盐和固体电解质。

两类导体的导电性对温度的依赖相反：金属的电阻率随温度升高而增大（晶格振动加剧电子散射），电解质溶液的电导率随温度升高而增大（溶剂的黏度降低，离子运动加快，每升高 $1\,\mathrm{K}$ 约增大 2%）。电流从电子导体进入离子导体时，载流子必须在两者的界面上转换，这只能通过电极反应实现——这正是电化学的特点。

**定义 12.1.2** 溶解于溶剂（或熔融）后能全部或部分解离为离子的物质称为**电解质**。在溶液中（在通常浓度范围内）全部解离的称为**强电解质**，如 $\ce{HCl}$、$\ce{NaOH}$ 和大多数盐；只部分解离、溶液中解离平衡与未解离分子共存的称为**弱电解质**，如 $\ce{CH3COOH}$、$\ce{NH3(aq)}$。

强与弱不是物质的固有属性，也取决于溶剂：$\ce{HCl}$ 在水中是强电解质，在冰醋酸中是弱电解质。弱电解质的解离程度用**电离度**描述（[6.1.9](/6.1.9)）。电解质溶液与非电解质溶液在热力学上的根本区别在于离子之间的长程静电作用：$0.01\,\mathrm{mol\,kg^{-1}}$ 的蔗糖溶液几乎是理想的，同浓度的 $\ce{CaCl2}$ 溶液的平均活度因子只有 0.73（12.6）。

### 12.1.2. 电极的命名与导电机理

按 IUPAC 的规定，发生氧化反应的电极称为**阳极**，发生还原反应的电极称为**阴极**（[6.1.11](/6.1.11)）；另一套命名按电势高低，电势高的称为正极，电势低的称为负极。两套名称的对应关系在**原电池**与**电解池**中相反：原电池的负极是阳极，电解池的正极是阳极。本课程讨论电极反应时一律用阴、阳极，讨论电池的输出时用正、负极。

以 Pt 为阳极、Cu 为阴极电解 $\ce{CuCl2}$ 溶液为例：外电路中电子由电源负极流向 Cu 电极；在 Cu 电极上 $\ce{Cu^2+ + 2e- -> Cu}$；溶液中 $\ce{Cu^2+}$ 向阴极、$\ce{Cl-}$ 向阳极迁移；在 Pt 电极上 $\ce{2Cl- -> Cl2 + 2e-}$，电子经外电路回到电源正极。整个回路可以写成

$$
\text{电源}(-) \xrightarrow{\ \mathrm{e}^-\ } \ce{Cu} \xrightarrow{\ \text{还原}\ } \text{溶液（离子迁移）} \xrightarrow{\ \text{氧化}\ } \ce{Pt} \xrightarrow{\ \mathrm{e}^-\ } \text{电源}(+).
$$

于是电解质溶液的导电由三个串联的过程组成：溶液中离子的电迁移（物理过程）、两个电极上的电极反应（化学过程）、电子在电极与外电路中的运动（物理过程）。串联意味着三者的电流处处相等；几个电解池串联时，通过每个电极的电量也相等。这一点是下面 Faraday 定律和 Hittorf 法的出发点。

### 12.1.3. Faraday 电解定律

电极反应把电量与物质的量联系起来。设电极反应写成

$$
0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B} + z\,\mathrm{e}^-\ (\text{或} - z\,\mathrm{e}^-),
$$
即反应进度为 $1\,\mathrm{mol}$ 时有 $z\,\mathrm{mol}$ 电子通过电极。

**定理 12.1.1（Faraday 电解定律）** 通过电极的电量 $Q$ 与电极反应的**反应进度** $\xi$ 成正比：

$$
Q = zF\xi, \qquad n_{\mathrm{B}} = \lvert\nu_{\mathrm{B}}\rvert\,\frac{Q}{zF}, \qquad m_{\mathrm{B}} = \lvert\nu_{\mathrm{B}}\rvert\,\frac{M_{\mathrm{B}}Q}{zF},
$$
其中 $F$ 是 **Faraday 常量**，$Q = \int_0^t I\,\mathrm{d}t$（恒电流时 $Q = It$）。

[6.1.12](/6.1.12) 已经给出了这一定律的初等形式 $n_{\mathrm{B}} = Q/(zF)$；写成反应进度的形式后，它对任何计量方程都成立。Faraday 在 1833–1834 年的《电学实验研究》第 3、5、7 辑中逐步确立了这一定律，比电子的发现早六十多年；今天看来它只是电荷守恒加上"每个离子得失整数个电子"。$F = N_{\mathrm{A}}e = 96\,485.332\,12\,\mathrm{C\,mol^{-1}}$，其中 $e = 1.602\,176\,634\times10^{-19}\,\mathrm{C}$、$N_{\mathrm{A}} = 6.022\,140\,76\times10^{23}\,\mathrm{mol^{-1}}$，自 2019 年起三者都是精确值。

Faraday 定律没有温度、压力、浓度或电极材料的限制，对电解池和原电池都适用，也与电极反应是否可逆无关。实际电解中产物少于理论量，是因为有副反应或产物损失，而不是定律失效；两者之比就是**电流效率**。根据这一定律制成的测量电量的装置称为电量计（库仑计）：银电量计中阴极析出 $\ce{Ag}$，每析出 $1\,\mathrm{g}$ 对应 $96\,485/107.868 = 894.5\,\mathrm{C}$。

电解所需的能量则由热力学决定。例如氯碱工业中 $\ce{2NaCl + 2H2O -> 2NaOH + H2 + Cl2}$（水溶液中）的 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 422\,\mathrm{kJ\,mol^{-1}}$（298 K，$z = 2$），外界对系统做的电功 $W' = QU$（$U$ 是槽电压）必须不小于 $\xi\Delta_{\mathrm{r}}G_{\mathrm{m}}$（[6.3.13](/6.3.13)）；电量由 Faraday 定律给出，槽电压由热力学与电极动力学决定（[6.3.14](/6.3.14)），两者之积才是电能消耗。

### 12.1.4. 荷一个元电荷的基本单元

物质的量 $n = N/N_{\mathrm{A}}$ 与所选的基本单元有关：$18\,\mathrm{g}$ 水是 $n(\ce{H2O}) = 1\,\mathrm{mol}$，也是 $n(\tfrac12\ce{H2O}) = 2\,\mathrm{mol}$。讨论电解质溶液的导电时，习惯以荷一个元电荷的粒子为基本单元：

- 离子 $\ce{M^{z+}}$、$\ce{A^{z-}}$ 取 $\tfrac{1}{z_+}\ce{M^{z+}}$、$\tfrac{1}{\lvert z_-\rvert}\ce{A^{z-}}$，如 $\ce{H+}$、$\tfrac12\ce{Cu^2+}$、$\tfrac13\ce{Fe^3+}$、$\tfrac12\ce{SO4^2-}$；
- 参加电极反应的物质取得失一个电子的量，如电解 $\ce{CuCl2}$ 时的 $\tfrac12\ce{Cu}$、$\tfrac12\ce{Cl2}$；
- 电解质 $\ce{M_{\nu_+}A_{\nu_-}}$ 取 $\tfrac{1}{\nu_+z_+}\ce{M_{\nu_+}A_{\nu_-}}$，如 $\ce{KCl}$、$\tfrac12\ce{Na2SO4}$、$\tfrac13\ce{AlCl3}$。

这样，$1\,\mathrm{mol}$ 任何这种基本单元都对应 $1\,\mathrm{mol}$ 元电荷，即 $F$ 的电量；两个电极上反应的基本单元的物质的量相等；完全解离时 $n(\tfrac12\ce{Na2SO4}) = n(\ce{Na+}) = n(\tfrac12\ce{SO4^2-})$。这种单元在旧文献中称为"当量"。它的好处是公式中的 $z$ 都变成 1，代价是必须时刻注明单元：$\Lambda_{\mathrm{m}}(\ce{CuSO4}) = 2\Lambda_{\mathrm{m}}(\tfrac12\ce{CuSO4})$（12.3.2）。

## 12.2. 离子的电迁移

### 12.2.1. 溶液中传质的三种方式

溶液中物质 B 的输运有三种方式，可以用通量密度 $\boldsymbol{J}_{\mathrm{B}}$（单位时间通过单位面积的物质的量，$\mathrm{mol\,m^{-2}\,s^{-1}}$）分别表示：

| 方式 | 推动力 | 通量密度 |
|---|---|---|
| 对流 | 溶液整体流动（搅拌、密度差） | $\boldsymbol{J} = c_{\mathrm{B}}\boldsymbol{v}$，$\boldsymbol{v}$ 是流速 |
| 扩散 | 浓度梯度（化学势梯度） | $\boldsymbol{J} = -D_{\mathrm{B}}\nabla c_{\mathrm{B}}$（**Fick 定律**，[5.2.2](/5.2.2)、[2.5.1](/2.5.1)） |
| 电迁移 | 电场 | $\boldsymbol{J} = \operatorname{sgn}(z_{\mathrm{B}})\,c_{\mathrm{B}}u_{\mathrm{B}}\boldsymbol{E}$ |

三项之和就是稀溶液中的 Nernst–Planck 方程。本章讨论电场驱动的电迁移；扩散在电极附近的作用（浓差极化）见 [6.3.14](/6.3.14)，在非平衡热力学中扩散与电迁移统一由电化学势的梯度驱动（[6.3.18](/6.3.18)）。

### 12.2.2. 电迁移率

**定义 12.2.1** 电场作用下溶液中离子的定向运动称为离子的**电迁移**。一定温度、压力和溶液组成下，离子 B 的迁移速度的大小 $v_{\mathrm{B}}$ 与电场强度 $E$ 成正比，比例系数

$$
u_{\mathrm{B}} = \frac{v_{\mathrm{B}}}{E}
$$
称为离子 B 的**电迁移率**（旧称淌度），单位 $\mathrm{m^2\,V^{-1}\,s^{-1}}$，即单位场强下离子的迁移速度。

$v_{\mathrm{B}}$ 就是离子的**漂移速度**。离子在溶液中受电场力 $\lvert z_{\mathrm{B}}\rvert eE$ 加速，同时受溶剂的黏性阻力；两者平衡后离子匀速运动。把离子近似为半径 $r$ 的刚性小球，阻力由 Stokes 公式 $6\pi\eta rv$ 给出（[5.1.2](/5.1.2)，$\eta$ 是溶剂的**黏度**），于是

$$
u_{\mathrm{B}} = \frac{\lvert z_{\mathrm{B}}\rvert e}{6\pi\eta r}. \tag{12.1}
$$
它说明电迁移率随电荷数增大而增大，随离子半径和溶剂黏度增大而减小；温度升高时 $\eta$ 下降，$u_{\mathrm{B}}$ 增大。

$u_{\mathrm{B}}$ 不是离子 B 的特性常数：它还与溶剂、温度和浓度有关，浓度越大，离子间的静电作用越使迁移变慢（12.7.6）。浓度趋于零时的极限值 $u^\infty_{\mathrm{B}}$ 称为极限电迁移率，此时离子间的作用消失，强、弱电解质也不再有区别；在给定溶剂与温度下，$u^\infty_{\mathrm{B}}$ 是离子 B 的特性参数，与共存的其他离子无关，可以查表。弱电解质与难溶盐溶液中离子浓度很低，可以近似取 $u_{\mathrm{B}} \approx u^\infty_{\mathrm{B}}$。

| 离子（$25\,^\circ\mathrm{C}$，水） | $\ce{H+}$ | $\ce{Li+}$ | $\ce{Na+}$ | $\ce{K+}$ | $\ce{Ag+}$ | $\ce{Ca^2+}$ | $\ce{OH-}$ | $\ce{Cl-}$ | $\ce{NO3-}$ | $\ce{CH3COO-}$ | $\ce{SO4^2-}$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $u^\infty/(10^{-8}\,\mathrm{m^2\,V^{-1}\,s^{-1}})$ | 36.24 | 4.01 | 5.19 | 7.62 | 6.42 | 6.16 | 20.5 | 7.91 | 7.40 | 4.24 | 8.29 |

（由 CRC Handbook 的极限离子摩尔电导率按 $u^\infty = \lambda^\infty/(\lvert z\rvert F)$ 换算，见 12.4.2。）在 $1\,\mathrm{V\,cm^{-1}}$ 的电场中，$\ce{K+}$ 每秒只移动约 $8\,\mu\mathrm{m}$，远小于分子热运动的速率；电迁移是叠加在无规热运动上的微小漂移。

**例 12.2.1** 由式 (12.1) 和 $\eta(\ce{H2O}, 25\,^\circ\mathrm{C}) = 0.890\,\mathrm{mPa\,s}$ 估算 $\ce{Li+}$、$\ce{Na+}$、$\ce{K+}$ 的有效半径，并与晶体中的离子半径（0.076、0.102、0.138 nm）比较。

**解** $r = e/(6\pi\eta u^\infty)$。对 $\ce{Na+}$，

$$
r = \frac{1.602\times10^{-19}\,\mathrm{C}}{6\pi \times 0.890\times10^{-3}\,\mathrm{Pa\,s}\times5.19\times10^{-8}\,\mathrm{m^2\,V^{-1}\,s^{-1}}} = 1.84\times10^{-10}\,\mathrm{m} = 0.184\,\mathrm{nm};
$$
同样得 $\ce{Li+}$ 0.238 nm、$\ce{K+}$ 0.125 nm。晶体半径越小，有效（"Stokes"）半径反而越大，顺序完全颠倒：小离子的电场强，结合的水分子多，在溶液中拖着一个较大的水合层运动。这一估计只有定性意义——Stokes 公式是为宏观小球推出的，用于与溶剂分子同样大小的离子时只能给出数量级。$\square$

### 12.2.3. 迁移数

电流在溶液中由正、负离子共同承担，各自承担的份额不同。

**定义 12.2.2** 溶液中离子 B 迁移所输送的电量 $Q_{\mathrm{B}}$ 占通过溶液的总电量 $Q$ 的分数

$$
t_{\mathrm{B}} = \frac{Q_{\mathrm{B}}}{Q} = \frac{I_{\mathrm{B}}}{I}
$$
称为离子 B 的**迁移数**。溶液中各种离子的迁移数之和为 1。

**定理 12.2.1** 只含一种电解质（解离为 $\ce{M^{z+}}$ 与 $\ce{A^{z-}}$）的溶液中，

$$
t_+ = \frac{u_+}{u_+ + u_-}, \qquad t_- = \frac{u_-}{u_+ + u_-}.
$$
一般地，溶液中含多种离子时 $t_{\mathrm{B}} = \lvert z_{\mathrm{B}}\rvert c_{\mathrm{B}}u_{\mathrm{B}}\big/\sum_i \lvert z_i\rvert c_i u_i$。

**证明** 设溶液处于截面积 $A$、相距 $l$ 的两平行电极之间，两极间电压为 $U$，场强 $E = U/l$。单位时间内穿过任一截面的正离子的物质的量为 $c_+v_+A$，每摩尔正离子带电 $z_+F$，所以正离子承担的电流 $I_+ = z_+Fc_+u_+EA$；同理 $I_- = \lvert z_-\rvert Fc_-u_-EA$（负离子反向运动，但输送的电流与正离子同向）。由电中性 $z_+c_+ = \lvert z_-\rvert c_-$，

$$
t_+ = \frac{I_+}{I_+ + I_-} = \frac{z_+c_+u_+}{z_+c_+u_+ + \lvert z_-\rvert c_-u_-} = \frac{u_+}{u_+ + u_-}.
$$
多种离子时不再能约去 $\lvert z_i\rvert c_i$，直接得到一般式。$\square$

迁移数与电迁移率一样依赖于浓度、温度与溶剂，还依赖于共存的离子，只能由实验测定（12.2.4、12.2.5，以及 [6.3.13](/6.3.13) 的电动势法）。它的大小直接决定了电解时两极附近浓度的变化，也决定了液接电势（[6.3.13](/6.3.13)）：$\ce{KCl}$ 的 $t_+ \approx t_- \approx 0.5$，所以被用作盐桥。

### 12.2.4. Hittorf 法

设想一个分成阳极区、中间区、阴极区的电解池，三区各含 $5\,\mathrm{mol}$ 基本单元的 1-1 价电解质，正离子的电迁移率是负离子的 3 倍，通入 $4\,\mathrm{mol}$ 元电荷的电量（$4F$），电极本身不溶解、不参加离子平衡（如在阳极只发生负离子的氧化，在阴极只发生正离子的还原）。通过任一截面的电量都是 $4F$，其中 $3F$ 由正离子向阴极迁移输送，$1F$ 由负离子向阳极迁移输送：

| | 阳极区 | 中间区 | 阴极区 |
|---|---|---|---|
| 电极反应 | 负离子氧化 $4\,\mathrm{mol}$ | — | 正离子还原 $4\,\mathrm{mol}$ |
| 迁入 | 负离子 $+1$ | 不变 | 正离子 $+3$ |
| 迁出 | 正离子 $-3$ | 不变 | 负离子 $-1$ |
| 电解质的变化 | $5 \to 2$（减少 3，等于迁出的正离子） | $5$ | $5 \to 4$（减少 1，等于迁出的负离子） |

由此看出：中间区浓度不变；对每种离子，迁移的量与电极反应的量不同；每个电极区中电解质减少的量等于由该区迁出的离子的量（物质守恒加电中性）。测出一个电极区电解质的变化量，就能求出迁移数。

**定义 12.2.3** 在迁移管中电解已知浓度的电解质溶液，通电后分析阴极区（或阳极区）溶液组成的变化，并由串联的电量计测出通过的电量，据此计算离子迁移数的方法称为 **Hittorf 法**。

对阴极区的离子 B（正离子，在阴极被还原），物料衡算为

$$
n_{\text{终}} = n_{\text{始}} + n_{\text{迁}} - n_{\text{电}}, \qquad t_{\mathrm{B}} = \frac{n_{\text{迁}}}{n_{\text{电}}},
$$
其中 $n_{\text{电}} = Q/F$ 以荷一个元电荷的基本单元计。对不参加电极反应的离子，去掉 $n_{\text{电}}$ 一项，迁出取负号。

**例 12.2.2** 在 Hittorf 迁移管中用 Cu 电极电解 $\ce{CuSO4}$ 溶液。通电一段时间后，串联的银电量计中析出 $0.0405\,\mathrm{g}$ Ag。阴极区溶液中的 $\ce{CuSO4}$ 通电前为 $1.1276\,\mathrm{g}$，通电后为 $1.1090\,\mathrm{g}$（同一质量的水）。求 $t(\ce{Cu^2+})$ 与 $t(\ce{SO4^2-})$。

**解** 以 $\tfrac12\ce{Cu^2+}$、$\tfrac12\ce{CuSO4}$ 为基本单元，$M(\tfrac12\ce{CuSO4}) = 79.80\,\mathrm{g\,mol^{-1}}$，

$$
n_{\text{电}} = \frac{0.0405}{107.87} = 3.754\times10^{-4}\,\mathrm{mol}, \quad n_{\text{始}} = \frac{1.1276}{79.80} = 1.4130\times10^{-2}\,\mathrm{mol}, \quad n_{\text{终}} = \frac{1.1090}{79.80} = 1.3897\times10^{-2}\,\mathrm{mol}.
$$
阴极上 $\tfrac12\ce{Cu^2+ + e- -> 1/2Cu}$ 使 $\ce{Cu^2+}$ 减少，迁移使它增加：$n_{\text{迁}} = n_{\text{终}} - n_{\text{始}} + n_{\text{电}} = (-2.33 + 3.754)\times10^{-4} = 1.42\times10^{-4}\,\mathrm{mol}$，所以

$$
t(\ce{Cu^2+}) = \frac{1.42\times10^{-4}}{3.754\times10^{-4}} = 0.38, \qquad t(\ce{SO4^2-}) = 1 - 0.38 = 0.62. \qquad \square
$$

Hittorf 法的误差主要来自对流与扩散使电极区之间混合，以及溶剂化：离子迁移时带着水合水，测得的是以溶剂为参照的"表观"迁移数。

### 12.2.5. 界面移动法

**定义 12.2.4** 在竖直的细管中让两种有共同离子的电解质溶液形成清晰的界面（如下层 $\ce{CdCl2}$、上层 $\ce{HCl}$），通电后测量界面在一定时间内移动的距离，由此计算离子迁移数的方法称为**界面移动法**。

设上层溶液中待测离子 $\ce{H+}$ 的浓度为 $c$，通过电量 $Q$ 时界面扫过的体积为 $V$，则这段体积中的 $\ce{H+}$ 全部越过了某一固定截面，输送的电量为 $z_+cVF$，

$$
t_+ = \frac{z_+cVF}{Q}.
$$
界面保持清晰的条件是指示离子（$\ce{Cd^2+}$）的电迁移率小于待测离子：若指示离子落后，界面下方的电阻增大、场强增大，使它加速赶上；若超前，就进入场强较小的区域而减速。这种自动"锐化"使界面移动法比 Hittorf 法更精确，现代的迁移数数据多由它测得。

## 12.3. 电导、电导率与摩尔电导率

### 12.3.1. 电导与电导率

对金属导体习惯用电阻 $R$ 表示导电能力，对电解质溶液习惯用其倒数——**电导** $G = 1/R$（单位 S）。截面积 $A$、长 $l$ 的均匀导体，$G = \sigma A/l$，$\sigma$ 就是 [5.3.5](/5.3.5) 的**电导率**（单位 $\mathrm{S\,m^{-1}}$），它是**电阻率**的倒数，相当于边长 $1\,\mathrm{m}$ 的立方体溶液在相对两面之间的电导。化学文献常把电导率记作 $\kappa$，本站与物理一致写 $\sigma$。

电导率与电迁移率的关系由 12.2.3 的电流表达式得到：$I = \sum_{\mathrm{B}}\lvert z_{\mathrm{B}}\rvert Fc_{\mathrm{B}}u_{\mathrm{B}}EA$，与 $I = \sigma EA$（**Ohm 定律**的微分形式 $\boldsymbol{J} = \sigma\boldsymbol{E}$）比较，

$$
\sigma = F\sum_{\mathrm{B}}\lvert z_{\mathrm{B}}\rvert c_{\mathrm{B}}u_{\mathrm{B}}. \tag{12.2}
$$
这与金属中 $\sigma = ne\mu_{\mathrm{e}}$ 的结构完全相同：电导率 = 载流子浓度 × 电荷 × 迁移率，只是溶液中有两种以上载流子。因此电导率取决于离子的数目与迁移的快慢。强电解质的电导率随浓度先增大（离子数增多）后减小（离子间作用使 $u$ 减小，浓溶液中还有离子缔合），在某一浓度出现极大值（$\ce{H2SO4}$ 约在 30% 质量分数）；弱电解质的电导率很小，且随浓度变化不大，因为浓度增大时电离度下降。

| 导体 | $\sigma/(\mathrm{S\,m^{-1}})$（室温，数量级） |
|---|---|
| 纯水 | $5.5\times10^{-6}$（只来自水自身的解离） |
| 天然水、饮用水 | $10^{-3}$–$10^{-1}$ |
| 水溶液电解质（$0.01$–$1\,\mathrm{mol\,L^{-1}}$ 的盐、酸、碱） | $10^{-1}$–$10^{2}$；海水约 5 |
| 锂离子电池的有机电解液（$\ce{LiPF6}$ 的碳酸酯溶液） | 约 1 |
| 离子液体 | $10^{-2}$–$1$ |
| 聚合物电解质（如 PEO–锂盐，室温） | $10^{-5}$–$10^{-2}$ |
| 无机固体电解质（$\alpha$-$\ce{AgI}$、硫化物锂离子导体、高温下的 YSZ） | $10^{-2}$–$10^{2}$ |
| 熔融盐（如熔融 $\ce{KCl}$） | $10^{2}$ |
| 金属 | $10^{6}$–$10^{8}$ |

### 12.3.2. 摩尔电导率

电导率随浓度变化，不便比较不同电解质的导电本领。把它折算到 $1\,\mathrm{mol}$ 电解质上：

**定义 12.3.1** 电解质溶液的电导率与电解质的物质的量浓度之比

$$
\Lambda_{\mathrm{m}} = \frac{\sigma}{c}
$$
称为该电解质的**摩尔电导率**，单位 $\mathrm{S\,m^2\,mol^{-1}}$（$c$ 用 $\mathrm{mol\,m^{-3}}$）。它相当于把含 $1\,\mathrm{mol}$ 电解质的溶液放在相距 $1\,\mathrm{m}$ 的两个大平行板电极之间时的电导。

$\Lambda_{\mathrm{m}}$ 的数值与所选的基本单元有关，使用时必须注明：$\Lambda_{\mathrm{m}}(\ce{CuSO4}) = 2\Lambda_{\mathrm{m}}(\tfrac12\ce{CuSO4})$。比较不同价型的电解质时常取荷一个元电荷的单元（12.1.4）。表中数据常用 $\mathrm{S\,cm^2\,mol^{-1}}$，$1\,\mathrm{S\,cm^2\,mol^{-1}} = 10^{-4}\,\mathrm{S\,m^2\,mol^{-1}}$；换算时注意 $c$ 的单位，$c = 0.01\,\mathrm{mol\,L^{-1}} = 10\,\mathrm{mol\,m^{-3}}$。

由式 (12.2)，对解离度为 $\alpha$ 的电解质 $\ce{M_{\nu_+}A_{\nu_-}}$，$c_+ = \nu_+\alpha c$、$c_- = \nu_-\alpha c$，以 $\tfrac{1}{\nu_+z_+}\ce{M_{\nu_+}A_{\nu_-}}$ 为单元时 $\nu_+z_+ = 1$，

$$
\Lambda_{\mathrm{m}} = \alpha(u_+ + u_-)F. \tag{12.3}
$$
其中 $\alpha$ 反映离子的数目，$u_+ + u_-$ 反映离子迁移的快慢。强电解质 $\alpha = 1$，$\Lambda_{\mathrm{m}}$ 随浓度的变化完全来自 $u$；弱电解质的变化主要来自 $\alpha$。常见的说法"摩尔电导率就是溶液中含正、负离子各 $1\,\mathrm{mol}$ 时的电导"只对 1-1 价强电解质成立。

### 12.3.3. 电导的测量

电导用电导池测量：两片平行的铂电极之间充满待测溶液，用 Wheatstone 电桥或电导仪测其电阻。必须用交流电（通常约 $1\,\mathrm{kHz}$）：直流会在电极上引起电解和极化（[6.3.14](/6.3.14)），在两极间产生反电动势。铂片上镀铂黑可以增大真实表面积、降低电流密度，进一步减小极化。

**定义 12.3.2** 电导池两电极间的距离 $l$ 与电极面积 $A$ 之比 $K_{\mathrm{cell}} = l/A$ 称为**电导池常数**。由 $\sigma = K_{\mathrm{cell}}/R$，测出电阻即得电导率。

电极的有效面积与电场线的分布很难直接量出，所以 $K_{\mathrm{cell}}$ 用已知电导率的标准溶液标定，通常是 $\ce{KCl}$ 溶液（$25\,^\circ\mathrm{C}$ 时 $0.0100\,\mathrm{mol\,L^{-1}}$ $\ce{KCl}$ 的 $\sigma = 0.1413\,\mathrm{S\,m^{-1}}$）。现代电导率仪内置标定与温度补偿，直接读出 $\sigma$。

**例 12.3.1** $25\,^\circ\mathrm{C}$ 时某电导池充以 $0.0100\,\mathrm{mol\,L^{-1}}$ $\ce{KCl}$ 溶液，测得电阻 $484.0\,\Omega$；换成 $0.00500\,\mathrm{mol\,L^{-1}}$ 的 $\tfrac12\ce{K2SO4}$ 溶液（即 $0.00250\,\mathrm{mol\,L^{-1}}$ $\ce{K2SO4}$），电阻为 $1101\,\Omega$。求电导池常数和 $\Lambda_{\mathrm{m}}(\tfrac12\ce{K2SO4})$。

**解** $K_{\mathrm{cell}} = \sigma R = 0.1413 \times 484.0\,\mathrm{m^{-1}} = 68.39\,\mathrm{m^{-1}}$。待测溶液 $\sigma = 68.39/1101\,\mathrm{S\,m^{-1}} = 0.06212\,\mathrm{S\,m^{-1}}$，

$$
\Lambda_{\mathrm{m}}(\tfrac12\ce{K2SO4}) = \frac{0.06212\,\mathrm{S\,m^{-1}}}{5.00\,\mathrm{mol\,m^{-3}}} = 1.242\times10^{-2}\,\mathrm{S\,m^2\,mol^{-1}} = 124.2\,\mathrm{S\,cm^2\,mol^{-1}},
$$
而 $\Lambda_{\mathrm{m}}(\ce{K2SO4}) = 248.4\,\mathrm{S\,cm^2\,mol^{-1}}$。（无限稀时 $\lambda^\infty(\ce{K+}) + \lambda^\infty(\tfrac12\ce{SO4^2-}) = 153.5\,\mathrm{S\,cm^2\,mol^{-1}}$，有限浓度下的值较小，原因见 12.7.6。）$\square$

### 12.3.4. 摩尔电导率与浓度的关系

Kohlrausch 测量了大量电解质在不同浓度下的摩尔电导率，发现强电解质与弱电解质的行为截然不同（下图）。

**定理 12.3.1（Kohlrausch 平方根定律）** 强电解质的稀溶液（约 $c < 0.01\,\mathrm{mol\,L^{-1}}$）中，摩尔电导率与浓度的平方根成线性关系：

$$
\Lambda_{\mathrm{m}} = \Lambda^\infty_{\mathrm{m}} - \mathcal{A}\sqrt{c},
$$
其中 $\mathcal{A}$ 是与电解质、溶剂和温度有关的常数。

这原本是经验规律，其理论解释（包括 $\mathcal{A}$ 的数值）由 Debye–Hückel–Onsager 理论给出（12.7.6）：$\sqrt c$ 的出现正是离子氛的半径 $\lambda_{\mathrm{D}} \propto c^{-1/2}$ 的反映。

**定义 12.3.3** 电解质的摩尔电导率在浓度趋于零时的极限值 $\Lambda^\infty_{\mathrm{m}} = \lim_{c\to0}\Lambda_{\mathrm{m}}$ 称为该电解质的**极限摩尔电导率**（无限稀释摩尔电导率）。

$\Lambda^\infty_{\mathrm{m}}$ 是离子之间没有相互作用时 $1\,\mathrm{mol}$ 电解质的导电本领，在给定溶剂与温度下是电解质的特性参数。对强电解质，把稀溶液的数据对 $\sqrt c$ 作图，用**最小二乘法**拟合直线（[3.3](/3.3)）外推到 $c = 0$ 即得 $\Lambda^\infty_{\mathrm{m}}$。弱电解质不行：它的 $\Lambda_{\mathrm{m}}$ 在稀溶液中随 $c$ 的减小急剧上升（电离度趋于 1），在可以准确测量的浓度范围内远未达到极限，外推毫无根据。弱电解质的 $\Lambda^\infty_{\mathrm{m}}$ 要借助离子独立迁移定律求出（12.4）。

![25 °C 水溶液的摩尔电导率。左：HCl、KCl、NaCl 的实验值（CRC）除以外推的极限值后对 √c 作图，c ≤ 0.01 mol/L 的点用最小二乘直线外推（实线），虚线是 Onsager 理论的极限斜率；右：乙酸的摩尔电导率（按 Ostwald 稀释定律计算）在稀溶液中陡升，远离 390.6 S cm² mol⁻¹ 的极限值，无法外推](./plots/molar-conductivity.py)

## 12.4. 离子独立迁移定律

### 12.4.1. 离子的摩尔电导率与独立迁移

Kohlrausch 比较了有共同离子的电解质的极限摩尔电导率，发现它们的差值与共同离子无关：

| 电解质对 | $\Lambda^\infty_{\mathrm{m}}/(\mathrm{S\,cm^2\,mol^{-1}})$ | 差值 | 电解质对 | $\Lambda^\infty_{\mathrm{m}}/(\mathrm{S\,cm^2\,mol^{-1}})$ | 差值 |
|---|---|---|---|---|---|
| $\ce{KCl}$ / $\ce{LiCl}$ | 149.8 / 115.0 | 34.8 | $\ce{HCl}$ / $\ce{HNO3}$ | 426.0 / 421.1 | 4.9 |
| $\ce{KNO3}$ / $\ce{LiNO3}$ | 144.9 / 110.1 | 34.8 | $\ce{KCl}$ / $\ce{KNO3}$ | 149.8 / 144.9 | 4.9 |
| $\ce{KClO4}$ / $\ce{LiClO4}$ | 140.8 / 106.0 | 34.8 | $\ce{LiCl}$ / $\ce{LiNO3}$ | 115.0 / 110.1 | 4.9 |

无论负离子是什么，$\ce{K+}$ 与 $\ce{Li+}$ 的差值总是 34.8；无论正离子是什么，$\ce{Cl-}$ 与 $\ce{NO3-}$ 的差值总是 4.9。这说明无限稀溶液中每种离子对导电的贡献是独立的。

**定义 12.4.1** 电解质溶液中离子 B 对电导率的贡献 $\sigma_{\mathrm{B}} = \lvert z_{\mathrm{B}}\rvert Fc_{\mathrm{B}}u_{\mathrm{B}}$ 与其浓度之比

$$
\lambda_{\mathrm{B}} = \frac{\sigma_{\mathrm{B}}}{c_{\mathrm{B}}} = \lvert z_{\mathrm{B}}\rvert Fu_{\mathrm{B}}
$$
称为离子 B 的**离子摩尔电导率**；无限稀时的值 $\lambda^\infty_{\mathrm{B}}$ 称为极限离子摩尔电导率。以荷一个元电荷的单元表示时，$\lambda(\tfrac{1}{\lvert z\rvert}\mathrm{B}) = Fu_{\mathrm{B}}$。

由 $\sigma = \sum\sigma_{\mathrm{B}}$ 立即得到摩尔电导率的加和性：完全解离的 $\ce{M_{\nu_+}A_{\nu_-}}$ 有 $\Lambda_{\mathrm{m}} = \nu_+\lambda_+ + \nu_-\lambda_-$。这在任何浓度下都成立，只是有限浓度下 $\lambda_{\mathrm{B}}$ 依赖于溶液中的其他离子；无限稀时这种依赖消失。

**定理 12.4.1（离子独立迁移定律）** 在给定溶剂和温度下，无限稀溶液中各种离子独立迁移，互不影响，每种离子的极限摩尔电导率 $\lambda^\infty_{\mathrm{B}}$ 是定值，与共存的其他离子无关；电解质 $\ce{M_{\nu_+}A_{\nu_-}}$ 的极限摩尔电导率为

$$
\Lambda^\infty_{\mathrm{m}} = \nu_+\lambda^\infty_+ + \nu_-\lambda^\infty_-.
$$

离子的贡献可以用迁移数分开。对强电解质，由定理 12.2.1，

$$
t_+ = \frac{u_+}{u_+ + u_-} = \frac{\nu_+\lambda_+}{\Lambda_{\mathrm{m}}}, \qquad \lambda_+ = \frac{t_+\Lambda_{\mathrm{m}}}{\nu_+}, \quad \lambda_- = \frac{t_-\Lambda_{\mathrm{m}}}{\nu_-}.
$$
所以测出一种电解质的 $\Lambda^\infty_{\mathrm{m}}$ 与极限迁移数，就得到两种离子的 $\lambda^\infty$；再由独立迁移定律推及其他电解质。

### 12.4.2. 极限离子摩尔电导率

| 正离子 | $\lambda^\infty/(\mathrm{S\,cm^2\,mol^{-1}})$ | 负离子 | $\lambda^\infty/(\mathrm{S\,cm^2\,mol^{-1}})$ |
|---|---|---|---|
| $\ce{H+}$ | 349.65 | $\ce{OH-}$ | 198.0 |
| $\ce{Li+}$ | 38.66 | $\ce{Cl-}$ | 76.31 |
| $\ce{Na+}$ | 50.08 | $\ce{Br-}$ | 78.1 |
| $\ce{K+}$ | 73.48 | $\ce{I-}$ | 76.8 |
| $\ce{NH4+}$ | 73.5 | $\ce{NO3-}$ | 71.42 |
| $\ce{Ag+}$ | 61.9 | $\ce{CH3COO-}$ | 40.9 |
| $\tfrac12\ce{Mg^2+}$ | 53.0 | $\ce{HCO3-}$ | 44.5 |
| $\tfrac12\ce{Ca^2+}$ | 59.47 | $\tfrac12\ce{SO4^2-}$ | 80.0 |
| $\tfrac12\ce{Cu^2+}$ | 53.6 | $\tfrac12\ce{CO3^2-}$ | 69.3 |

（$25\,^\circ\mathrm{C}$ 水溶液，CRC Handbook。）

**例 12.4.1** 求 $25\,^\circ\mathrm{C}$ 时乙酸的 $\Lambda^\infty_{\mathrm{m}}$。

**解** 直接查表：$\Lambda^\infty_{\mathrm{m}}(\ce{CH3COOH}) = \lambda^\infty(\ce{H+}) + \lambda^\infty(\ce{CH3COO-}) = 349.65 + 40.9 = 390.6\,\mathrm{S\,cm^2\,mol^{-1}}$。若只有电解质的数据，可以用三个强电解质组合，它们的 $\Lambda^\infty_{\mathrm{m}}$ 都能由外推得到：

$$
\Lambda^\infty_{\mathrm{m}}(\ce{CH3COOH}) = \Lambda^\infty_{\mathrm{m}}(\ce{HCl}) + \Lambda^\infty_{\mathrm{m}}(\ce{CH3COONa}) - \Lambda^\infty_{\mathrm{m}}(\ce{NaCl}) = 426.0 + 91.0 - 126.4 = 390.6\,\mathrm{S\,cm^2\,mol^{-1}}. \qquad \square
$$

### 12.4.3. 质子与氢氧根的异常迁移

表中 $\ce{H+}$ 与 $\ce{OH-}$ 的 $\lambda^\infty$ 是其他离子的 3–7 倍。按式 (12.1) 反算，$\ce{H+}$ 的有效半径只有 0.026 nm，比氢原子还小，说明它不是作为一个整体在水中漂移。目前公认的是 Grotthuss 机理（1806 年提出，现代形式由分子动力学模拟确立）：水合质子 $\ce{H3O+}$ 把一个质子沿**氢键**交给相邻的水分子，后者再把另一个质子交给下一个，正电荷沿氢键网络"接力"传递，而每个原子只移动了很短的距离；$\ce{OH-}$ 是反方向的空位接力。限速步骤是氢键网络的重排（约 1 ps）。同样的机理使质子在冰中、在蛋白质的质子通道（如 ATP 合酶、细菌视紫红质）和燃料电池的质子交换膜中都能快速传导。

### 12.4.4. Walden 规则

由式 (12.1)，极限电迁移率与溶剂黏度成反比；若离子的有效半径不随溶剂改变，则 $\lambda^\infty\eta$ 与溶剂无关。

**性质 12.4.1（Walden 规则）** 同一电解质在不同溶剂中的极限摩尔电导率与溶剂黏度之积近似为常数：$\Lambda^\infty_{\mathrm{m}}\eta \approx$ 常数。

Walden 规则对体积大、溶剂化弱的离子（如四烷基铵离子）符合得较好，对小离子偏差大，因为它们的溶剂化程度随溶剂而变；对 $\ce{H+}$、$\ce{OH-}$ 在水中则完全不适用（Grotthuss 机理与黏度无关）。同一溶剂中温度改变时，$\lambda^\infty\eta$ 也近似不变，这解释了电导率约 2% 每开尔文的温度系数：水的黏度每开尔文下降约 2%。离子液体研究中常用"Walden 图"（$\lg\Lambda_{\mathrm{m}}$ 对 $\lg\eta^{-1}$）判断离子液体中离子解离的程度。

### 12.4.5. 各种导电量的关系

| 层次 | 量 | 是否为本性（可查表） |
|---|---|---|
| 电解质溶液 | 电导 $G$、电导率 $\sigma$ | 否（依赖浓度与电导池） |
| 电解质 | 摩尔电导率 $\Lambda_{\mathrm{m}} = \sigma/c$ | 否（依赖浓度） |
| | 极限摩尔电导率 $\Lambda^\infty_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\lambda^\infty_{\mathrm{B}}$ | 是 |
| 离子 | 电迁移率 $u_{\mathrm{B}}$、离子摩尔电导率 $\lambda_{\mathrm{B}} = \lvert z_{\mathrm{B}}\rvert Fu_{\mathrm{B}}$、迁移数 $t_{\mathrm{B}}$ | 否（依赖浓度与共存离子） |
| | 极限电迁移率 $u^\infty_{\mathrm{B}}$、极限离子摩尔电导率 $\lambda^\infty_{\mathrm{B}}$ | 是 |
| | 极限迁移数 $t^\infty_{\mathrm{B}}$ | 否（还依赖于电解质中的另一种离子） |

## 12.5. 电导法的应用

### 12.5.1. 弱电解质的电离度与电离常数

弱电解质溶液中离子浓度很低，离子间作用很弱，可取 $u_{\mathrm{B}} \approx u^\infty_{\mathrm{B}}$。由式 (12.3)，$\Lambda_{\mathrm{m}} = \alpha(u_+^\infty + u_-^\infty)F$，而 $\Lambda^\infty_{\mathrm{m}} = (u_+^\infty + u_-^\infty)F$，于是

$$
\alpha = \frac{\Lambda_{\mathrm{m}}}{\Lambda^\infty_{\mathrm{m}}}.
$$
对 1-1 价弱电解质 $\ce{HA <=> H+ + A-}$，代入 **稀释定律**（[6.1.9](/6.1.9)），

$$
K_c = \frac{c\alpha^2}{c^\circ(1-\alpha)} = \frac{c\,\Lambda_{\mathrm{m}}^2}{c^\circ\Lambda^\infty_{\mathrm{m}}(\Lambda^\infty_{\mathrm{m}} - \Lambda_{\mathrm{m}})}.
$$
这就是 Arrhenius 提出电离理论的实验基础。

**例 12.5.1** $25\,^\circ\mathrm{C}$ 时 $0.0100\,\mathrm{mol\,L^{-1}}$ 乙酸溶液的电导率为 $1.63\times10^{-2}\,\mathrm{S\,m^{-1}}$（已扣除水的贡献）。求电离度与电离常数。

**解** $\Lambda_{\mathrm{m}} = 1.63\times10^{-2}/10.0 = 1.63\times10^{-3}\,\mathrm{S\,m^2\,mol^{-1}} = 16.3\,\mathrm{S\,cm^2\,mol^{-1}}$，$\alpha = 16.3/390.6 = 0.0417$，

$$
K_c = \frac{0.0100 \times 0.0417^2}{1 - 0.0417} = 1.82\times10^{-5}.
$$
严格地说，这是以浓度表示的平衡常数。溶液的**离子强度**为 $c\alpha \approx 4.2\times10^{-4}\,\mathrm{mol\,L^{-1}}$，由 Debye–Hückel 极限公式（定理 12.7.1）$\lg\gamma_\pm = -0.509\sqrt{4.2\times10^{-4}} = -0.0104$，热力学电离常数 $K_{\mathrm{a}} = K_c\gamma_\pm^2 = 1.82\times10^{-5}\times0.953 = 1.73\times10^{-5}$，与 [6.1.9](/6.1.9) 所用的 $1.75\times10^{-5}$ 相差约 1%。（剩余的差别主要因为有限浓度下离子的 $\lambda$ 略小于 $\lambda^\infty$。）$\square$

### 12.5.2. 难溶盐的溶解度与溶度积

难溶盐的饱和溶液很稀，可取 $\Lambda_{\mathrm{m}} \approx \Lambda^\infty_{\mathrm{m}}$；溶液的电导率要扣除水本身的贡献（此时两者的数量级相近）：

$$
c = \frac{\sigma(\text{溶液}) - \sigma(\ce{H2O})}{\Lambda^\infty_{\mathrm{m}}}.
$$
由溶解度 $c$ 即可求**溶度积**（[6.1.10](/6.1.10)）。

**例 12.5.2** $25\,^\circ\mathrm{C}$ 时 $\ce{AgCl}$ 饱和溶液的电导率为 $1.90\times10^{-4}\,\mathrm{S\,m^{-1}}$，所用水的电导率为 $0.05\times10^{-4}\,\mathrm{S\,m^{-1}}$。求 $K_{\mathrm{sp}}(\ce{AgCl})$。

**解** $\Lambda^\infty_{\mathrm{m}}(\ce{AgCl}) = 61.9 + 76.31 = 138.2\,\mathrm{S\,cm^2\,mol^{-1}} = 1.382\times10^{-2}\,\mathrm{S\,m^2\,mol^{-1}}$，

$$
c = \frac{(1.90 - 0.05)\times10^{-4}}{1.382\times10^{-2}}\,\mathrm{mol\,m^{-3}} = 1.34\times10^{-2}\,\mathrm{mol\,m^{-3}} = 1.34\times10^{-5}\,\mathrm{mol\,L^{-1}},
$$
$K_{\mathrm{sp}} = (c/c^\circ)^2 = 1.79\times10^{-10}$，与 [6.1.10](/6.1.10) 的 $1.8\times10^{-10}$ 一致。$\square$

### 12.5.3. 水的纯度与溶液浓度

纯水的电导率由 $\ce{H2O <=> H+ + OH-}$ 的**离子积**决定：$\sigma = [\lambda^\infty(\ce{H+}) + \lambda^\infty(\ce{OH-})]\sqrt{K_{\mathrm{w}}}\,c^\circ = 547.7\times10^{-4}\,\mathrm{S\,m^2\,mol^{-1}}\times1.0\times10^{-4}\,\mathrm{mol\,m^{-3}} = 5.5\times10^{-6}\,\mathrm{S\,m^{-1}}$（电阻率 $18.2\,\mathrm{M\Omega\,cm}$）。实验室的超纯水以达到这一理论值为指标；普通蒸馏水因溶入 $\ce{CO2}$，电导率约 $10^{-4}\,\mathrm{S\,m^{-1}}$。

电导率与浓度在一定范围内有单值关系，因此可用于在线监测：海水的盐度在海洋学中就是由电导率定义的（实用盐度标度）；把大气中的 $\ce{SO2}$ 吸收在 $\ce{H2O2}$ 溶液中氧化为 $\ce{H2SO4}$（$\ce{SO2 + H2O2 -> H2SO4}$，在溶液中即 $\ce{SO3^2- + H2O2 -> SO4^2- + H2O}$），由电导率的增加求出 $\ce{SO2}$ 的量。

### 12.5.4. 电导滴定

**定义 12.5.1** 以溶液电导（率）随滴定剂体积的变化确定滴定终点的方法称为**电导滴定**。滴定反应使溶液中导电能力不同的离子相互替换，电导–体积曲线由斜率不同的几段直线组成，转折点就是终点。

用 $\ce{NaOH}$ 滴定 $\ce{HCl}$ 时，终点前 $\ce{H+}$（$\lambda^\infty = 349.65$）被 $\ce{Na+}$（50.08）替换，电导直线下降；终点后过量的 $\ce{OH-}$（198.0）使电导直线上升。滴定乙酸时，起始电导很小；加入 $\ce{NaOH}$ 后生成的 $\ce{CH3COONa}$ 完全解离，电导逐渐上升（最初的一小段因同离子效应抑制乙酸解离而略有下降）；终点后上升变陡。电导滴定不需要指示剂，适用于有色或浑浊的溶液，以及很稀或很弱的酸碱（这时 pH 滴定曲线的突跃不明显）。为使各段是直线，滴定剂的浓度应比待测溶液大 10 倍以上，或者按 $(V_0 + V)/V_0$ 校正稀释效应。

![25 °C 时用 0.100 mol/L NaOH 滴定 100 mL 0.0100 mol/L 的 HCl 与乙酸的电导滴定曲线（由极限离子摩尔电导率与平衡组成计算，已按 (V₀+V)/V₀ 校正稀释），两条曲线都在 10 mL 处转折](./plots/conductometric-titration.py)

## 12.6. 强电解质的平均活度与活度因子

### 12.6.1. 电解质的化学势

按 [6.3.6](/6.3.6) 的一般方法，溶液中电解质 B 的**化学势**写成 $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}} + RT\ln a_{\mathrm{B}}$（$p^\circ$ 下，以质量摩尔浓度标度的 Henry 定律为参考），$a_{\mathrm{B}}$ 称为电解质的整体活度。但强电解质 $\ce{M_{\nu_+}A_{\nu_-}}$ 在溶液中并不以分子存在，真实的物种是离子：

$$
\mu_+ = \mu^\circ_+ + RT\ln a_+, \quad a_+ = \gamma_+\frac{b_+}{b^\circ}; \qquad \mu_- = \mu^\circ_- + RT\ln a_-, \quad a_- = \gamma_-\frac{b_-}{b^\circ},
$$
其中 $b_+ = \nu_+b$、$b_- = \nu_-b$ 是离子的**质量摩尔浓度**，$b^\circ = 1\,\mathrm{mol\,kg^{-1}}$，标准态是 $b = b^\circ$ 且仍服从 Henry 定律的假想态。

两种描述的关系由 Gibbs 自由能得到。设溶液由 $n$ mol $\ce{M_{\nu_+}A_{\nu_-}}$ 与 $n_{\mathrm{A}}$ mol 水组成，则 $G = n\mu_{\mathrm{B}} + n_{\mathrm{A}}\mu_{\mathrm{A}}$，也可以写成 $G = \nu_+n\mu_+ + \nu_-n\mu_- + n_{\mathrm{A}}\mu_{\mathrm{A}}$（偏摩尔量的加和公式，[6.3.4](/6.3.4)）。两式对任意 $n$ 成立，所以

$$
\mu_{\mathrm{B}} = \nu_+\mu_+ + \nu_-\mu_-. \tag{12.4}
$$
$1\,\mathrm{mol}$ 电解质与 $\nu_+$ mol 正离子加 $\nu_-$ mol 负离子对系统 Gibbs 自由能的贡献相同。取 $\mu^\circ_{\mathrm{B}} = \nu_+\mu^\circ_+ + \nu_-\mu^\circ_-$，代入得 $a_{\mathrm{B}} = a_+^{\nu_+}a_-^{\nu_-}$。

问题在于单个离子的化学势与活度不可测：溶液必须保持电中性，不能只加入正离子而不加入负离子（单个离子的化学势总伴随着把电荷移入相内的静电功，[6.3.13](/6.3.13)）。可测的只是 $\mu_{\mathrm{B}}$ 这种电中性组合。

### 12.6.2. 平均活度、平均活度因子与平均质量摩尔浓度

**定义 12.6.1** 对强电解质 $\ce{M_{\nu_+}A_{\nu_-}}$，令 $\nu = \nu_+ + \nu_-$，称离子活度、活度因子与质量摩尔浓度的几何平均

$$
a_\pm = \left(a_+^{\nu_+}a_-^{\nu_-}\right)^{1/\nu}, \qquad \gamma_\pm = \left(\gamma_+^{\nu_+}\gamma_-^{\nu_-}\right)^{1/\nu}, \qquad b_\pm = \left(b_+^{\nu_+}b_-^{\nu_-}\right)^{1/\nu} = \left(\nu_+^{\nu_+}\nu_-^{\nu_-}\right)^{1/\nu}b
$$
分别为离子的**平均活度**、**平均活度因子**和**平均质量摩尔浓度**。它们满足

$$
a_\pm = \gamma_\pm\frac{b_\pm}{b^\circ}, \qquad a_{\mathrm{B}} = a_+^{\nu_+}a_-^{\nu_-} = a_\pm^\nu.
$$

平均活度保持了活度"校正浓度"的本意，而 $\gamma_\pm$ 是电中性组合，可以由实验测定：蒸气压与凝固点降低等依数性测出溶剂活度，再由 **Gibbs–Duhem 方程**积分得到 $\gamma_\pm$（[6.3.6](/6.3.6)），或者由电池电动势直接测定（[6.3.13](/6.3.13)）。需要单个离子的活度时，通常近似取 $\gamma_+ \approx \gamma_- \approx \gamma_\pm$。

对 1-1 价电解质 $b_\pm = b$；对 $\ce{CaCl2}$（$\nu_+ = 1$，$\nu_- = 2$）$b_\pm = 4^{1/3}b = 1.587b$；对 $\ce{Na2SO4}$ 也是 $1.587b$；对 $\ce{LaCl3}$ $b_\pm = 27^{1/4}b = 2.280b$。

**例 12.6.1** $25\,^\circ\mathrm{C}$ 时 $0.0100\,\mathrm{mol\,kg^{-1}}$ $\ce{CaCl2}$ 溶液的 $\gamma_\pm = 0.732$。求 $b_\pm$、$a_\pm$、$a(\ce{CaCl2})$ 以及近似的 $a_+$、$a_-$。

**解** $b_+ = 0.0100$、$b_- = 0.0200\,\mathrm{mol\,kg^{-1}}$，$b_\pm = (0.0100 \times 0.0200^2)^{1/3} = 0.01587\,\mathrm{mol\,kg^{-1}}$；

$$
a_\pm = 0.732 \times 0.01587 = 0.01162, \qquad a(\ce{CaCl2}) = a_\pm^3 = 1.57\times10^{-6};
$$
取 $\gamma_+ \approx \gamma_- \approx \gamma_\pm$，$a_+ \approx 0.00732$，$a_- \approx 0.01464$。检验：$a_+a_-^2 = 1.57\times10^{-6}$。$\square$

### 12.6.3. 平均活度因子的数据与规律

| $b/(\mathrm{mol\,kg^{-1}})$ | $\ce{HCl}$ | $\ce{NaCl}$ | $\ce{CaCl2}$ | $\ce{Na2SO4}$ | $\ce{CuSO4}$ |
|---|---|---|---|---|---|
| 0.001 | 0.965 | 0.965 | 0.888 | 0.886 | 0.74 |
| 0.01 | 0.905 | 0.903 | 0.732 | 0.714 | 0.44 |
| 0.1 | 0.796 | 0.778 | 0.518 | 0.445 | 0.150 |
| 0.5 | 0.757 | 0.681 | 0.448 | 0.267 | 0.062 |
| 1.0 | 0.809 | 0.657 | 0.500 | 0.204 | 0.042 |

（$25\,^\circ\mathrm{C}$ 水溶液，CRC Handbook，Robinson–Stokes 汇编值。）从表中可以读出：

1. 同一电解质，浓度越小，$\gamma_\pm$ 越接近 1；$b \to 0$ 时 $\gamma_\pm \to 1$。即使在 $0.001\,\mathrm{mol\,kg^{-1}}$，$\ce{CuSO4}$ 的 $\gamma_\pm$ 仍只有 0.74：电解质溶液在非电解质看来"非常稀"的浓度下就已明显偏离理想。
2. 稀溶液中，同价型电解质的 $\gamma_\pm$ 几乎相等（$\ce{HCl}$ 与 $\ce{NaCl}$，$\ce{CaCl2}$ 与 $\ce{Na2SO4}$）；价数乘积 $\lvert z_+z_-\rvert$ 越大，偏离越大。
3. 浓溶液中 $\gamma_\pm$ 经过极小后回升，甚至大于 1（$\ce{HCl}$ 在约 $2\,\mathrm{mol\,kg^{-1}}$ 以上），规律因电解质而异：水被离子的水合层大量占据，"自由"溶剂减少，使有效浓度增大。

规律 1、2 说明，在稀溶液中 $\gamma_\pm$ 偏离 1 的原因是离子之间的静电作用：浓度越小，离子间距越大，作用越弱；电荷越多，作用越强。它决定于溶液中所有离子的浓度与电荷，于是引出离子强度。

### 12.6.4. 离子强度

**定义 12.6.2** 溶液中所有离子的质量摩尔浓度与其电荷数平方的乘积之和的一半

$$
I_b = \frac12\sum_{\mathrm{B}}b_{\mathrm{B}}z_{\mathrm{B}}^2
$$
称为溶液的**离子强度**（Lewis 与 Randall，1921）。若用物质的量浓度计算，记作 $I_c = \frac12\sum c_{\mathrm{B}}z_{\mathrm{B}}^2$；稀水溶液中 $I_c/(\mathrm{mol\,L^{-1}}) \approx 0.997\,I_b/(\mathrm{mol\,kg^{-1}})$。

求和遍及溶液中实际存在的每种离子（不论来自哪种电解质），用离子的实际浓度。Lewis 与 Randall 由经验发现：稀溶液中，电解质的 $\gamma_\pm$ 只由离子强度决定，与其他离子的种类无关。12.7 的理论证明了这一点，并给出了 $z^2$ 的来源：离子氛的屏蔽强度正比于 $\sum c_{\mathrm{B}}z_{\mathrm{B}}^2$。

**例 12.6.2** 求下列溶液的离子强度：(1) $0.10\,\mathrm{mol\,kg^{-1}}$ $\ce{NaCl}$ 与 $0.20\,\mathrm{mol\,kg^{-1}}$ $\ce{CaCl2}$ 的混合溶液；(2) $b$ $\ce{CuSO4}$；(3) 电离度为 0.013 的 $0.10\,\mathrm{mol\,kg^{-1}}$ 乙酸溶液。

**解** (1) $b(\ce{Na+}) = 0.10$，$b(\ce{Ca^2+}) = 0.20$，$b(\ce{Cl-}) = 0.10 + 2\times0.20 = 0.50$，$I_b = \frac12(0.10 + 4\times0.20 + 0.50) = 0.70\,\mathrm{mol\,kg^{-1}}$。(2) $I_b = \frac12(4b + 4b) = 4b$；一般地，1-1、2-1（或 1-2）、2-2、3-1 型的 $I_b$ 分别是 $b$、$3b$、$4b$、$6b$。(3) 只有已解离的部分计入：$b(\ce{H+}) = b(\ce{CH3COO-}) = 0.0013$，$I_b = 0.0013\,\mathrm{mol\,kg^{-1}}$。$\square$

[6.1.10](/6.1.10) 的**盐效应**在这里得到定量的解释：在难溶盐的饱和溶液中加入无关的强电解质，离子强度增大，$\gamma_\pm$ 减小；溶度积 $K_{\mathrm{sp}} = \gamma_\pm^2(b_+/b^\circ)(b_-/b^\circ)$ 不变，所以溶解度增大。蛋白质的"盐溶"也是同一效应；高离子强度下蛋白质又会"盐析"，那是水的活度降低和疏水作用增强的结果，超出了稀溶液理论。

## 12.7. 强电解质溶液理论

### 12.7.1. Debye–Hückel 模型

1923 年 Debye 与 Hückel 提出了第一个定量的强电解质溶液理论。它的出发点是：稀溶液中电解质溶液的非理想性完全来自离子之间的静电作用。

**定义 12.7.1** 基于以下假设计算强电解质稀溶液中离子活度因子的理论称为 **Debye–Hückel 理论**（离子互吸理论）：

1. 强电解质完全解离；离子是带电荷 $z_ie$ 的点电荷（或刚性小球），离子之间只有 Coulomb 作用；
2. 溶剂是电容率为 $\varepsilon = \varepsilon_0\varepsilon_{\mathrm{r}}$ 的连续介质，$\varepsilon_{\mathrm{r}}$ 取纯溶剂的值；
3. 任选一个离子作为中心离子，其他离子在它的电场中的分布服从 Boltzmann 分布，电荷密度与电势之间服从 Poisson 方程；
4. 离子的静电势能远小于热运动能，$\lvert z_ie\psi\rvert \ll k_{\mathrm{B}}T$。

在这些假设下，中心离子周围异号离子出现的概率比同号离子大，时间平均的结果是一个球对称、总电荷与中心离子等量异号的电荷云，称为离子氛（ionic atmosphere）。

离子氛不是固定的离子壳层：每个离子都是别的离子的离子氛的一员，离子氛中的离子不断交换，它只是统计平均意义上的电荷分布。中心离子与离子氛的吸引使中心离子的能量降低，化学势低于理想溶液中的值，因而 $\gamma < 1$。下面把这一图像定量化。

### 12.7.2. 线性化 Poisson–Boltzmann 方程

设中心离子 $j$ 带电荷 $z_je$，周围的平均电势为 $\psi(\boldsymbol{r})$。离子 $i$ 在电势 $\psi$ 处的势能为 $z_ie\psi$，按 Boltzmann 分布，它在该处的数密度为 $n_i = n_i^0\exp(-z_ie\psi/k_{\mathrm{B}}T)$，$n_i^0$ 是溶液本体中（$\psi = 0$ 处）的数密度。电荷密度 $\rho = \sum_i z_ien_i$，**电势**满足 Poisson 方程 $\Delta\psi = -\rho/\varepsilon$（[5.3.2](/5.3.2#sec-2.4.2)、[5.3.4](/5.3.4)），于是

$$
\Delta\psi = -\frac{1}{\varepsilon}\sum_i z_ien_i^0\exp\left(-\frac{z_ie\psi}{k_{\mathrm{B}}T}\right). \tag{12.5}
$$

**定义 12.7.2** 电解质溶液中平均电势 $\psi$ 满足的非线性偏微分方程 (12.5) 称为 **Poisson–Boltzmann 方程**。

它把静电学（Poisson 方程）与统计力学（Boltzmann 分布）组合起来，是"平均场"近似：用平均电势代替其他离子的瞬时位置。式 (12.5) 一般没有解析解。按假设 4，把指数展开到一阶：

$$
\Delta\psi = -\frac{e}{\varepsilon}\sum_i z_in_i^0 + \frac{e^2}{\varepsilon k_{\mathrm{B}}T}\sum_i z_i^2n_i^0\,\psi.
$$
由溶液本体的电中性 $\sum_i z_in_i^0 = 0$，第一项消失，得到线性化的 Poisson–Boltzmann 方程

$$
\Delta\psi = \kappa^2\psi, \qquad \kappa^2 = \frac{e^2}{\varepsilon k_{\mathrm{B}}T}\sum_i n_i^0z_i^2 = \frac{2F^2I_c}{\varepsilon RT}, \tag{12.6}
$$
最后一步用了 $n_i^0 = N_{\mathrm{A}}c_i$、$e^2N_{\mathrm{A}}^2 = F^2$、$k_{\mathrm{B}}N_{\mathrm{A}} = R$，$I_c$ 以 $\mathrm{mol\,m^{-3}}$ 计。离子强度正是在这里出现的：屏蔽只取决于 $\sum c_iz_i^2$。

**定义 12.7.3** 式 (12.6) 中的 $\kappa$ 的倒数

$$
\lambda_{\mathrm{D}} = \frac{1}{\kappa} = \sqrt{\frac{\varepsilon RT}{2F^2I_c}}
$$
称为 **Debye 长度**（Debye 屏蔽长度），它是离子氛的特征厚度。

代入 $25\,^\circ\mathrm{C}$ 水的 $\varepsilon_{\mathrm{r}} = 78.4$，并用 $I_c \approx 997\,\mathrm{kg\,m^{-3}}\times I_b$，得

$$
\lambda_{\mathrm{D}} = \frac{0.304\,\mathrm{nm}}{\sqrt{I_b/b^\circ}}, \qquad \kappa = B\sqrt{I_b/b^\circ}, \quad B = 3.29\,\mathrm{nm^{-1}}. \tag{12.7}
$$
$I_b = 0.001$、$0.01$、$0.1\,\mathrm{mol\,kg^{-1}}$ 时 $\lambda_{\mathrm{D}}$ 分别为 9.6、3.0、0.96 nm；生理盐水（约 $0.15\,\mathrm{mol\,kg^{-1}}$）中约 0.8 nm，所以细胞内的静电作用在 1 nm 以外就被大大屏蔽，蛋白质之间的静电相互作用是短程的。同一屏蔽也出现在等离子体和半导体中，在胶体的双电层理论中 $\lambda_{\mathrm{D}}$ 就是扩散层的厚度（[6.3.21](/6.3.21)）。

### 12.7.3. 离子氛的电势与电荷分布

中心离子周围的电势是球对称的，$\psi = \psi(r)$。在球坐标中 **Laplace 算子**作用于径向函数（[2.5.5](/2.5.5)）为

$$
\Delta\psi = \frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}\psi}{\mathrm{d}r}\right) = \frac1r\frac{\mathrm{d}^2(r\psi)}{\mathrm{d}r^2}.
$$
令 $w = r\psi$，式 (12.6) 化为常系数线性方程 $w'' = \kappa^2w$，通解 $w = A\mathrm{e}^{-\kappa r} + A'\mathrm{e}^{\kappa r}$（[2.4.9](/2.4.9)）。$r \to \infty$ 时电势有界，所以 $A' = 0$：

$$
\psi(r) = \frac{A\,\mathrm{e}^{-\kappa r}}{r}.
$$
对点电荷模型，$r \to 0$ 时离子氛的影响可忽略，$\psi$ 必须趋于中心离子自身的 Coulomb 势 $z_je/(4\pi\varepsilon r)$，于是 $A = z_je/(4\pi\varepsilon)$，

$$
\psi(r) = \frac{z_je}{4\pi\varepsilon}\frac{\mathrm{e}^{-\kappa r}}{r}. \tag{12.8}
$$
这就是屏蔽 Coulomb 势（在核物理中称为 Yukawa 势）：在 $r \ll \lambda_{\mathrm{D}}$ 处与裸电荷的势相同，在 $r \gg \lambda_{\mathrm{D}}$ 处指数衰减，中心离子的电场被离子氛"屏蔽"掉了。

离子氛的电荷密度由 Poisson 方程反求：$\rho(r) = -\varepsilon\Delta\psi = -\varepsilon\kappa^2\psi = -\dfrac{z_je\kappa^2}{4\pi}\dfrac{\mathrm{e}^{-\kappa r}}{r}$。半径 $r$ 到 $r + \mathrm{d}r$ 的球壳中的电荷为 $4\pi r^2\rho\,\mathrm{d}r = -z_je\kappa^2r\mathrm{e}^{-\kappa r}\,\mathrm{d}r$，对 $r$ 从 0 积分到 $\infty$ 恰好是 $-z_je$：离子氛的总电荷与中心离子等量异号。壳层电荷在 $r = 1/\kappa = \lambda_{\mathrm{D}}$ 处最大，这就是把 $\lambda_{\mathrm{D}}$ 称为离子氛厚度的原因。

把式 (12.8) 拆成中心离子自身的势和离子氛产生的势：

$$
\psi(r) = \frac{z_je}{4\pi\varepsilon r} + \psi_{\text{氛}}(r), \qquad \psi_{\text{氛}}(r) = \frac{z_je}{4\pi\varepsilon}\frac{\mathrm{e}^{-\kappa r} - 1}{r} \xrightarrow{r\to0} -\frac{z_je\kappa}{4\pi\varepsilon}. \tag{12.9}
$$
离子氛在中心离子处产生的电势，等于把电荷 $-z_je$ 均匀分布在半径 $\lambda_{\mathrm{D}}$ 的球面上所产生的电势。

![25 °C 水中一价离子的 Debye–Hückel 离子氛（点电荷模型）。左：中心正离子周围的屏蔽电势与裸 Coulomb 势的比较；右：每个球壳中离子氛电荷的径向分布，曲线下面积为 1，峰值在 r = λ_D 处（虚线）](./plots/ionic-atmosphere.py)

### 12.7.4. Debye–Hückel 极限公式

**定理 12.7.1（Debye–Hückel 极限公式）** 在 Debye–Hückel 模型的点电荷近似下，离子 $j$ 的活度因子与强电解质的平均活度因子为

$$
\ln\gamma_j = -\frac{z_j^2e^2\kappa}{8\pi\varepsilon k_{\mathrm{B}}T}, \qquad \lg\gamma_\pm = -A\lvert z_+z_-\rvert\sqrt{I_b/b^\circ},
$$
其中 $A = \dfrac{e^2B}{8\pi\varepsilon k_{\mathrm{B}}T\ln10}$；$25\,^\circ\mathrm{C}$ 的水溶液中 $A = 0.509$。

**证明** 理想溶液与实际溶液的差别只在于离子之间的静电作用，所以离子 $j$ 的化学势中的非理想部分 $k_{\mathrm{B}}T\ln\gamma_j$（每个离子）等于在离子氛存在下把该离子从不带电"充电"到 $z_je$ 所做的静电功中、由离子氛贡献的部分（自身的 Coulomb 自能在理想溶液中同样存在，相互抵消）。设想离子带电 $q$（$0 \le q \le z_je$）而溶液中其他离子保持不变，由式 (12.9)，离子氛在它所在处的电势为 $-q\kappa/(4\pi\varepsilon)$，把电荷 $\mathrm{d}q$ 移到该处需做功 $\psi_{\text{氛}}\,\mathrm{d}q$，

$$
k_{\mathrm{B}}T\ln\gamma_j = \int_0^{z_je}\left(-\frac{q\kappa}{4\pi\varepsilon}\right)\mathrm{d}q = -\frac{z_j^2e^2\kappa}{8\pi\varepsilon}.
$$
（若改为让所有离子同时按同一比例充电，$\kappa$ 也随之变化，积分结果相同，这是 Güntelberg 的处理。）这就是第一式。由定义 12.6.1，

$$
\ln\gamma_\pm = \frac{\nu_+\ln\gamma_+ + \nu_-\ln\gamma_-}{\nu} = -\frac{e^2\kappa}{8\pi\varepsilon k_{\mathrm{B}}T}\cdot\frac{\nu_+z_+^2 + \nu_-z_-^2}{\nu_+ + \nu_-}.
$$
由电中性 $\nu_+z_+ = -\nu_-z_-$，$\nu_+z_+^2 + \nu_-z_-^2 = \nu_+z_+(z_+ - z_-) = \lvert z_+z_-\rvert(\nu_+ + \nu_-)$（例如 $\ce{CaCl2}$：$4 + 2 = 2\times3$），所以 $\ln\gamma_\pm = -\lvert z_+z_-\rvert e^2\kappa/(8\pi\varepsilon k_{\mathrm{B}}T)$。代入 $\kappa = B\sqrt{I_b/b^\circ}$ 并换成常用对数即得第二式。数值：$e^2/(4\pi\varepsilon k_{\mathrm{B}}T)$ 是 Bjerrum 长度，$25\,^\circ\mathrm{C}$ 水中为 $0.715\,\mathrm{nm}$，所以 $A = 0.715\times3.29/(2\ln10) = 0.51$；用更精确的 $\varepsilon_{\mathrm{r}}$ 得通用值 $0.509$。$\square$

极限公式的内容是：

- $\ln\gamma_\pm$ 与 $\sqrt{I_b}$ 成正比，斜率由价型 $\lvert z_+z_-\rvert$ 和溶剂决定，与离子的个性无关——这正是 12.6.3 的规律 1、2 与 Lewis–Randall 的离子强度规则；
- 平方根依赖来自 $\kappa \propto \sqrt{I}$，即离子氛的半径随浓度的平方根缩小；它在 $b = 0$ 处斜率无穷大，说明静电作用是长程的，任何有限浓度的电解质都不是理想溶液；
- $A \propto (\varepsilon_{\mathrm{r}}T)^{-3/2}$：溶剂的电容率越小，偏离越大。乙醇（$\varepsilon_{\mathrm{r}} \approx 25$）中 $A$ 约为水中的 5.6 倍。

适用范围约为 $I_b \lesssim 0.01\,\mathrm{mol\,kg^{-1}}$（2-2 型更窄）。它也适用于弱电解质与难溶盐溶液中的离子（例 12.5.1），只要离子强度按溶液中实际的离子浓度计算。也常写成 $\ln\gamma_\pm = -1.172\lvert z_+z_-\rvert\sqrt{I_b/b^\circ}$，$1.172 = 0.509\ln10$，两者等价；常数必须与所用的对数相配。

### 12.7.5. 扩展的 Debye–Hückel 公式与适用范围

点电荷近似在离子间距接近离子大小时失效。设离子是直径（最近接近距离）为 $a$ 的刚性小球：$r < a$ 处没有其他离子，电势为 $\dfrac{z_je}{4\pi\varepsilon r} + C$；$r \ge a$ 处仍是 $A\mathrm{e}^{-\kappa r}/r$。在 $r = a$ 处令电势与电场连续，解得 $C = -\dfrac{z_je\kappa}{4\pi\varepsilon(1 + \kappa a)}$，即离子氛的电势比点电荷模型小一个因子 $1 + \kappa a$。重复充电过程得

$$
\lg\gamma_\pm = -\frac{A\lvert z_+z_-\rvert\sqrt{I_b/b^\circ}}{1 + Ba\sqrt{I_b/b^\circ}}. \tag{12.10}
$$
$a \approx 0.3\,\mathrm{nm}$ 时 $Ba \approx 1$，于是常用 $\lg\gamma_\pm = -A\lvert z_+z_-\rvert\sqrt{I}/(1 + \sqrt{I})$（$I = I_b/b^\circ$），适用于 $I \lesssim 0.1$。再加一个经验的线性项就是 Davies 方程

$$
\lg\gamma_\pm = -A\lvert z_+z_-\rvert\left(\frac{\sqrt{I}}{1 + \sqrt{I}} - 0.30\,I\right), \tag{12.11}
$$
它不含可调参数，在 $I \lesssim 0.1$–$0.5$ 内对多数电解质的误差在百分之几以内，广泛用于天然水和生理溶液的化学平衡计算。线性项表示的是近距离的短程作用（离子水合、离子对的形成），它使 $\gamma_\pm$ 在浓溶液中回升。更浓的溶液需要 Pitzer 方程等含离子特定参数的模型，或者用分子模拟。

![25 °C 水溶液的平均活度因子（CRC 数据点）与 Debye–Hückel 理论的比较：虚点线为极限公式，虚线为扩展式（Ba = 1），实线为 Davies 方程。左图是稀溶液区，三种价型的数据都趋于各自的极限斜率；右图延伸到浓溶液，扩展式与 Davies 方程的适用范围依次扩大，但都不能描述 2-2 型电解质在浓溶液中的行为](./plots/activity-coefficients.py)

**例 12.7.1** 分别用极限公式、扩展式与 Davies 方程估算 $25\,^\circ\mathrm{C}$ 时 $0.0100\,\mathrm{mol\,kg^{-1}}$ $\ce{CaCl2}$ 的 $\gamma_\pm$，并与实验值 0.732 比较。

**解** $I = 3\times0.0100 = 0.0300$，$\sqrt I = 0.1732$，$A\lvert z_+z_-\rvert = 1.018$。

$$
\begin{aligned}
\text{极限公式：}&\ \lg\gamma_\pm = -1.018\times0.1732 = -0.1763, && \gamma_\pm = 0.666;\\
\text{扩展式：}&\ \lg\gamma_\pm = -0.1763/1.1732 = -0.1503, && \gamma_\pm = 0.707;\\
\text{Davies：}&\ \lg\gamma_\pm = -1.018\times(0.1476 - 0.0090) = -0.1411, && \gamma_\pm = 0.723.
\end{aligned}
$$
对 2-1 型电解质，$I = 0.03$ 已超出极限公式的适用范围，误差约 9%；Davies 方程误差约 1%。$\square$

**例 12.7.2** 对 $0.1\,\mathrm{mol\,kg^{-1}}$ $\ce{NaCl}$ 与 $0.2\,\mathrm{mol\,kg^{-1}}$ $\ce{CaCl2}$ 的混合溶液，用极限公式求 $\gamma_\pm(\ce{NaCl})$，得 $\lg\gamma_\pm = -0.509\sqrt{0.70} = -0.426$，$\gamma_\pm = 0.375$。这一计算的问题是什么？

**解** 由例 12.6.2，$I_b = 0.70\,\mathrm{mol\,kg^{-1}}$，比极限公式的适用范围大约两个数量级，结果没有意义。用 Davies 方程估计，$\lg\gamma_\pm = -0.509\times(0.8367/1.8367 - 0.21) = -0.125$，$\gamma_\pm \approx 0.75$；即使这个值也只是粗略的估计（$I$ 已超出 Davies 方程的可靠范围），可靠的数值要用实验数据或 Pitzer 模型。按极限公式，$\gamma_\pm$ 随 $\sqrt I$ 无限下降，而实际上 1-1 型电解质的 $\gamma_\pm$ 在 $I \approx 0.5$–$1$ 附近已经达到极小（12.6.3 的表）。$\square$

### 12.7.6. Debye–Hückel–Onsager 电导理论

离子氛不但降低离子的化学势，也减慢离子的迁移，这就是强电解质 $\Lambda_{\mathrm{m}}$ 随浓度下降的原因。

**定义 12.7.4** 电场中离子迁移时，离子氛对中心离子运动的两种阻滞作用：中心离子运动时，前方要建立新的离子氛、后方的旧离子氛要消散，这需要一定的时间（弛豫时间约 $10^{-10}$–$10^{-8}\,\mathrm{s}$，与 $\varepsilon/\sigma$ 同量级），于是离子氛变得不对称，后方的异号电荷较多，把中心离子向后拉，称为**弛豫效应**；离子氛中的异号离子在电场中带着溶剂化的溶剂向相反方向运动，中心离子相当于逆流而行，所受的黏性阻力增大，称为**电泳效应**。

两种效应都正比于离子氛的"强度" $\kappa \propto \sqrt c$，这就解释了 Kohlrausch 平方根定律。Onsager（1927）在 Debye–Hückel 模型基础上算出了比例系数。

**定理 12.7.2（Debye–Hückel–Onsager 电导理论）** 1-1 价强电解质的稀溶液中，

$$
\Lambda_{\mathrm{m}} = \Lambda^\infty_{\mathrm{m}} - \left(a + b\Lambda^\infty_{\mathrm{m}}\right)\sqrt{c},\qquad a = \frac{eF^2}{3\pi\eta}\sqrt{\frac{2}{\varepsilon RT}},\qquad b = \frac{2q}{1 + \sqrt q}\cdot\frac{eF^2}{24\pi\varepsilon RT}\sqrt{\frac{2}{\varepsilon RT}},
$$
其中 $c$ 以 $\mathrm{mol\,m^{-3}}$ 计，$\eta$ 是溶剂的黏度，$q = 1/2$（对称电解质），$2q/(1 + \sqrt q) = 0.586$。第一项来自电泳效应，第二项来自弛豫效应。$25\,^\circ\mathrm{C}$ 的水溶液中

$$
\frac{\Lambda_{\mathrm{m}}}{\mathrm{S\,cm^2\,mol^{-1}}} = \frac{\Lambda^\infty_{\mathrm{m}}}{\mathrm{S\,cm^2\,mol^{-1}}} - \left(60.20 + 0.2289\,\frac{\Lambda^\infty_{\mathrm{m}}}{\mathrm{S\,cm^2\,mol^{-1}}}\right)\sqrt{\frac{c}{\mathrm{mol\,L^{-1}}}}.
$$

（不少教材按 Gauss 制写出这两个系数，并用 $D$ 表示介电常数；这里给出 SI 形式。）这是 Kohlrausch 经验系数 $\mathcal{A}$ 的理论值，无可调参数。对 $\ce{KCl}$，$\mathcal{A} = 60.20 + 0.2289\times149.8 = 94.5$；预言 $c = 0.001\,\mathrm{mol\,L^{-1}}$ 时 $\Lambda_{\mathrm{m}} = 149.8 - 94.5\times0.0316 = 146.8$，实验值 146.9。正如 12.3.4 图中的虚线所示，理论斜率在 $c \lesssim 0.001\,\mathrm{mol\,L^{-1}}$ 内与实验一致，浓度增大后实验点偏离到直线上方：这时离子的有限大小（因子 $1 + \kappa a$）已不可忽略。

两个效应都依赖于离子氛来得及建立。在高频交流电场（频率高于弛豫时间的倒数，约 $10^8\,\mathrm{Hz}$ 以上）中离子氛来不及形成不对称结构，弛豫效应消失，电导率升高（Debye–Falkenhagen 效应）；在很强的电场（约 $10^7\,\mathrm{V\,m^{-1}}$）中离子运动太快，离子氛来不及建立，电导率也升高（Wien 效应）。这两个效应直接证实了离子氛的存在。

## 小结

| 主题 | 要点 |
|---|---|
| 导电机理 | 离子电迁移 + 电极反应 + 外电路，三者串联、电流相等；阳极氧化、阴极还原 |
| Faraday 电解定律 | $Q = zF\xi$；$F = N_{\mathrm{A}}e = 96\,485.332\,12\,\mathrm{C\,mol^{-1}}$（精确）；以荷一个元电荷的粒子为基本单元 |
| 电迁移率与迁移数 | $u = v/E$，Stokes 估计 $u = \lvert z\rvert e/(6\pi\eta r)$；$t_+ = u_+/(u_+ + u_-)$；Hittorf 法、界面移动法 |
| 电导率与摩尔电导率 | $\sigma = F\sum\lvert z_{\mathrm{B}}\rvert c_{\mathrm{B}}u_{\mathrm{B}}$；$\Lambda_{\mathrm{m}} = \sigma/c = \alpha(u_+ + u_-)F$；电导池常数 $l/A$ 用 $\ce{KCl}$ 标定 |
| Kohlrausch 定律 | 强电解质 $\Lambda_{\mathrm{m}} = \Lambda^\infty_{\mathrm{m}} - \mathcal{A}\sqrt c$；$\Lambda^\infty_{\mathrm{m}} = \nu_+\lambda^\infty_+ + \nu_-\lambda^\infty_-$（离子独立迁移）；$\lambda_{\mathrm{B}} = \lvert z_{\mathrm{B}}\rvert Fu_{\mathrm{B}} = t_{\mathrm{B}}\Lambda_{\mathrm{m}}/\nu_{\mathrm{B}}$ |
| 电导法 | 弱电解质 $\alpha = \Lambda_{\mathrm{m}}/\Lambda^\infty_{\mathrm{m}}$；难溶盐 $c = [\sigma - \sigma(\ce{H2O})]/\Lambda^\infty_{\mathrm{m}}$；电导滴定 |
| 平均活度 | $\mu_{\mathrm{B}} = \nu_+\mu_+ + \nu_-\mu_-$；$a_{\mathrm{B}} = a_\pm^\nu$，$a_\pm = \gamma_\pm b_\pm/b^\circ$，几何平均 |
| 离子强度 | $I_b = \frac12\sum b_{\mathrm{B}}z_{\mathrm{B}}^2$ |
| Debye–Hückel 理论 | 线性化 PB 方程 $\Delta\psi = \kappa^2\psi$；$\lambda_{\mathrm{D}} = 0.304\,\mathrm{nm}/\sqrt{I_b/b^\circ}$（$25\,^\circ\mathrm{C}$ 水）；$\lg\gamma_\pm = -0.509\lvert z_+z_-\rvert\sqrt{I}$（$I \lesssim 0.01$），扩展式除以 $1 + \sqrt I$，Davies 方程再加 $0.30I$ |
| 电导理论 | 弛豫效应 + 电泳效应；1-1 型水溶液 $\Lambda_{\mathrm{m}} = \Lambda^\infty_{\mathrm{m}} - (60.20 + 0.2289\Lambda^\infty_{\mathrm{m}})\sqrt c$ |

## 思考题

1. 判断：电解质溶液中离子的电迁移率是离子本身的性质。

   **答** 错。电迁移率与浓度、共存离子有关；只有极限电迁移率在给定溶剂与温度下才是离子的特性参数。

2. 为什么测电导用交流电，而测电动势要求电流趋于零？

   **答** 前者要避免电极反应与极化；后者要保持电极处于平衡，[6.3.13](/6.3.13)。

3. 在弱电解质溶液中 $\Lambda_{\mathrm{m}} = \sigma/c$ 与 $\sigma/(c\alpha)$ 各代表什么？

   **答** 前者是按电解质总浓度计算的摩尔电导率；后者按实际离子浓度计算，近似等于 $\Lambda^\infty_{\mathrm{m}}$。

4. 用 Hittorf 法测得的 $\ce{HCl}$ 中 $t(\ce{H+}) \approx 0.82$，这与表中的 $\lambda^\infty$ 是否一致？

   **答** $349.65/(349.65 + 76.31) = 0.821$，一致。

5. 什么样的电解质溶液可以称为"理想的"？在难溶盐与弱电解质溶液中是否需要考虑 $\gamma_\pm$？

   **答** 只有无限稀时才是理想的；计算热力学平衡常数时仍应按实际离子强度用 Debye–Hückel 公式校正，例 12.5.1。

6. 为什么离子强度的定义中电荷数是平方？

   **答** 屏蔽来自 Boltzmann 因子的线性展开：每种离子贡献 $z_i \times z_i$——一个 $z_i$ 来自它的电荷，另一个来自它对电势的响应。
