---
title: 恒定电流
description: 电流与电流密度、电流连续性方程，恒定电流与恒定电场、Kirchhoff 第一定律，Ohm 定律的积分与微分形式、电阻的计算，电动势与温差电，全电路 Ohm 定律与 Kirchhoff 第二定律，恒定电流场与静电场的联合求解，Drude 模型与 Joule 定律，RC 电路的充电与放电。
---

前几章研究的是静止电荷的电场。电荷定向运动就形成电流；电流分布不随时间变化时称为恒定电流，这是从静电学走向电动力学的第一步。恒定电流的电荷分布不变，它产生的电场仍然满足静电场的两条基本定理，但与静电场不同，**导体**内部的**场强**不为零，场对电荷做功、把能量转化为热，维持它需要电源提供的非静电力。本章先用电流密度这个矢量场描述电流，由**电荷守恒**写出电流连续性方程；再讨论导体中电流与场强的关系（Ohm 定律）、电源的电动势与电路的两条定律（Kirchhoff 定律）；最后给出电流的一种经典微观图像，并讨论**电容器**的充放电这一最简单的非恒定过程。

本章用到前面课程的许多工具：电流是电流密度的**通量**，**连续性方程**的微分形式来自 **Gauss 公式**（[2.2.14](/2.2.14)），与流体的**连续性方程**（[5.1.4](/5.1.4)）和偏微分方程中的**守恒律**（[2.5.2](/2.5.2)）形式相同；Ohm 定律的微分形式与热传导的 **Fourier 定律**（[5.2.2](/5.2.2)）平行；复杂电路是一个**线性方程组**，它的独立方程数由图论中的**基本回路**决定（[1.4.3](/1.4.3)）；RC 电路的暂态是一阶**线性微分方程**（[2.2.15](/2.2.15#sec-15.3)）。下一章 [5.3.6](/5.3.6) 研究电流产生的磁场。

本章用 $\rho$ 表示电阻率、$\sigma$ 表示电导率；为避免混淆，电荷的体密度与面密度记为 $\rho_q$、$\sigma_q$。5.6 节（电流的经典微观图像）是选讲内容。

## 5.1. 电流和电流密度

电荷的定向运动形成电流。形成电流的带电粒子称为载流子：金属中是自由电子，电解液与电离气体中是正、负离子（以及电子），半导体中是电子与空穴（[5.5.6](/5.5.6)）。

**定义 5.1.1（电流）** 单位时间内通过导体某一横截面的电荷，

$$
I = \frac{\mathrm{d}q}{\mathrm{d}t},
$$
称为通过该截面的**电流**（电流强度）。电流的 SI 单位是安培（$\mathrm{A}$），它是七个基本单位之一；自 2019 年起，安培由固定**元电荷**的数值 $e = 1.602\,176\,634\times10^{-19}\,\mathrm{C}$（精确值）来定义（[5.3.7](/5.3.7)）。

电流只描述通过整个截面的总电荷，不能描述大块导体中各处电流的分布（如电阻法探矿中，大地里电流的分布）。为此引入矢量场：

### 5.1.1. 电流密度

**定义 5.1.2（电流密度）** 导体中某点的**电流密度** $\boldsymbol{J}$ 是一个矢量：大小等于单位时间内通过该点附近垂直于电荷运动方向的单位面积的电荷，即 $J = \dfrac{\mathrm{d}I}{\mathrm{d}S_\perp}$；方向为该点正载流子的运动方向（负载流子运动方向的反方向）。单位 $\mathrm{A\,m^{-2}}$。

设载流子的电荷为 $q$（代数量），数密度为 $n$，定向运动的速度为 $\boldsymbol{v}$。在 $\Delta t$ 内通过垂直于 $\boldsymbol{v}$ 的面元 $\Delta S$ 的载流子，位于以 $\Delta S$ 为底、长 $v\Delta t$ 的柱体内，所以

$$
\boldsymbol{J} = nq\boldsymbol{v} = \rho_q\boldsymbol{v} .
$$
有几种载流子时，$\boldsymbol{J} = \sum_in_iq_i\boldsymbol{v}_i$。

**定义 5.1.3（漂移速度）** 金属中自由电子作无规的热运动，同时在电场作用下有一个平均的定向速度 $\boldsymbol{v}_{\mathrm{d}}$（对全部自由电子的速度求平均），称为**漂移速度**，$\boldsymbol{J} = -ne\boldsymbol{v}_{\mathrm{d}}$。

无外场时 $\boldsymbol{v}_{\mathrm{d}} = \boldsymbol{0}$，没有电流。漂移速度很小：铜中 $n \approx 8.5\times10^{28}\,\mathrm{m^{-3}}$，截面 $1\,\mathrm{mm^2}$ 的铜线通过 $1\,\mathrm{A}$ 电流时，$v_{\mathrm{d}} = \dfrac{I}{neS} \approx 7\times10^{-5}\,\mathrm{m\,s^{-1}}$，即每秒不到 $0.1\,\mathrm{mm}$，远小于电子热运动的速率（$10^5$–$10^6\,\mathrm{m\,s^{-1}}$）。

通过任意曲面 $S$ 的电流等于电流密度对该曲面的**通量**：

$$
\mathrm{d}I = \boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S},\qquad I = \int_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} .
$$
像**电场线**一样，可以用电流线形象地描述电流分布：电流线上各点的切线方向是该点 $\boldsymbol{J}$ 的方向，垂直于 $\boldsymbol{J}$ 的单位面积上穿过的电流线条数等于 $J$。

### 5.1.2. 电流连续性方程

电荷既不能产生也不能消灭。对任一闭合曲面 $S$，单位时间内净流出 $S$ 的电荷等于 $S$ 内电荷的减少：

**定理 5.1.1（电流连续性方程）**

$$
\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = -\frac{\mathrm{d}q_{\mathrm{enc}}}{\mathrm{d}t},\qquad
\nabla\cdot\boldsymbol{J} + \frac{\partial\rho_q}{\partial t} = 0 .
$$

微分形式由 **Gauss 公式**得到。电流连续性方程是**电荷守恒定律**的数学表述，它给出了电流分布与电荷分布之间的普遍关系：

- $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} > 0$：有电流线从面内发出，面内电荷减少；
- $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} < 0$：有电流线终止于面内，面内电荷增加；
- $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = 0$：电流线连续地穿过，面内电荷不变。

电流线只能起止于电荷随时间变化的地方。

## 5.2. 恒定电流和恒定电场

**定义 5.2.1（恒定电流）** 电流密度 $\boldsymbol{J}$ 的分布不随时间变化的电流称为**恒定电流**（稳恒电流）。

$\boldsymbol{J}$ 不随时间变化时，电荷分布也不随时间变化：电荷从某处流走的同时，必有等量的电荷流过来补充。否则电荷的积累会改变电场，从而改变电流。由连续性方程，恒定电流满足

**定理 5.2.1（恒定条件）**

$$
\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = 0,\qquad \nabla\cdot\boldsymbol{J} = 0 .
$$
恒定电流的电流线是闭合曲线，$\boldsymbol{J}$ 是**无源场**。一段无分支的恒定电路中，各横截面的电流相等。

**定义 5.2.2（恒定电场）** 恒定电流的电荷分布不随时间变化，它产生的电场也不随时间变化，称为**恒定电场**。

恒定电场与静电场的相同之处：它由不随时间变化的电荷分布产生，所以满足**高斯定理**与环路定理

$$
\oint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} = \frac{q_{\mathrm{enc}}}{\varepsilon_0},\qquad \oint_L\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0,
$$
**电势**与**电势差**的概念仍然适用，习惯上也把恒定电场称为静电场。不同之处：

| | 静电场 | 恒定电场 |
|---|---|---|
| 场源 | 静止的电荷 | 运动的电荷，但分布不随时间变化 |
| 导体内部 | 静电平衡，场强为零 | 场强不为零，驱动电流 |
| 能量 | 维持静电场不需要能量转换 | 电场对运动电荷做功，总是伴随能量的转换 |

把恒定条件用于电路中的一个节点（三条或更多支路的汇合点），就得到：

**定理 5.2.2（Kirchhoff 第一定律）** 在恒定电路的任一节点处，流出节点的电流的代数和为零：

$$
\sum_iI_i = 0,
$$
规定流出节点的电流为正，流入为负。即流入节点的电流之和等于流出的电流之和（节点电流方程）。

## 5.3. Ohm 定律和电阻

1826 年，Ohm通过实验发现：通过一段导体的电流与导体两端的电压成正比。

### 5.3.1. 积分形式

**定理 5.3.1（Ohm 定律）** 一段导体两端的电压 $U = \varphi_a - \varphi_b$ 与通过它的电流 $I$ 成正比：

$$
U = IR,
$$
沿电流方向经过一个电阻，电势降低 $IR$。

**定义 5.3.1（电阻与电导）** Ohm 定律中的比例系数 $R = U/I$ 称为这段导体的**电阻**，单位欧姆（$\Omega = \mathrm{V\,A^{-1}}$）；电阻的倒数 $G = 1/R$ 称为**电导**，单位西门子（$\mathrm{S} = \Omega^{-1}$）。

**定义 5.3.2（电阻率与电导率）** 长 $L$、横截面积 $S$ 的均匀导体的电阻为

$$
R = \rho\frac{L}{S},
$$
$\rho$ 称为材料的**电阻率**，单位 $\Omega\,\mathrm{m}$；其倒数 $\sigma = 1/\rho$ 称为**电导率**，单位 $\mathrm{S\,m^{-1}}$。

| 材料（$20^\circ\mathrm{C}$） | $\rho/(\Omega\,\mathrm{m})$ | 材料 | $\rho/(\Omega\,\mathrm{m})$ |
|---|---|---|---|
| 银 | $1.6\times10^{-8}$ | 镍铬合金 | $1.1\times10^{-6}$ |
| 铜 | $1.7\times10^{-8}$ | 海水 | 约 $0.2$ |
| 铝 | $2.7\times10^{-8}$ | 纯硅 | 约 $2\times10^3$ |
| 铁 | $9.7\times10^{-8}$ | 玻璃 | $10^{10}$–$10^{14}$ |

导体、半导体与绝缘体的电阻率相差二十多个数量级，其原因要用能带论解释（[5.5.6](/5.5.6)）。金属的电阻率在常温附近随温度近似线性增大，$\rho \approx \rho_0(1 + \alpha t)$，铜的 $\alpha \approx 4\times10^{-3}\,\mathrm{K^{-1}}$；半导体的电阻率随温度升高而迅速减小。

### 5.3.2. 微分形式

在大块导体中沿电流线取一小柱体，长 $\mathrm{d}l$，截面 $\mathrm{d}S$，两端电势差 $\mathrm{d}U = -\mathrm{d}\varphi$，电阻 $\mathrm{d}R = \rho\,\mathrm{d}l/\mathrm{d}S$。由 $\mathrm{d}U = \mathrm{d}I\,\mathrm{d}R$，

$$
J = \frac{\mathrm{d}I}{\mathrm{d}S} = \frac1\rho\Big(-\frac{\mathrm{d}\varphi}{\mathrm{d}l}\Big) = \sigma E .
$$
在各向同性导体中 $\boldsymbol{J}$ 与 $\boldsymbol{E}$ 同向，于是得到：

**定理 5.3.2（Ohm 定律的微分形式）**

$$
\boldsymbol{J} = \sigma\boldsymbol{E} .
$$

微分形式是局域的关系，比积分形式适用得更广：它对非均匀导体成立，对变化不太快的非恒定电流也成立。它与热传导的 **Fourier 定律** $\boldsymbol{q} = -\kappa\nabla T$、扩散的 Fick 定律在形式上完全相同：电流沿电势降低的方向流动，热量沿温度降低的方向流动。

Ohm 定律不是普遍规律。电离气体、半导体器件（如二极管）的伏安特性曲线是非线性的；很强的电场下，即使金属，$\boldsymbol{J}$ 与 $\boldsymbol{E}$ 也偏离线性关系。"理想导体"指 $\sigma \to \infty$ 的极限，它与超导体不同：超导体除零电阻外还有完全抗磁性（[5.3.9](/5.3.9)）。

### 5.3.3. 电阻的计算

导体截面或电流方向不均匀时，把导体分成沿电流方向串联的薄层，$R = \int\rho\,\dfrac{\mathrm{d}l}{S(l)}$。

**例 5.3.1（电缆的漏电阻）** 同轴电缆的芯线半径 $R_1$，外层导体内半径 $R_2$，长 $l$，其间的绝缘层电阻率为 $\rho$。求径向的漏电阻；若芯线与外层间的电压为 $U$，求漏电流。

**解** 电流沿径向流动。半径 $r$ 到 $r + \mathrm{d}r$ 的圆柱薄层，长 $\mathrm{d}r$，截面积 $2\pi rl$，

$$
R = \int_{R_1}^{R_2}\rho\frac{\mathrm{d}r}{2\pi rl} = \frac{\rho}{2\pi l}\ln\frac{R_2}{R_1},\qquad
I = \frac UR = \frac{2\pi lU}{\rho\ln(R_2/R_1)} .
$$
电缆越长，漏电阻越小。

## 5.4. 电动势

### 5.4.1. 非静电力与电源

恒定电流的电路必须闭合。若电路不闭合，电荷就会在断开处积累，破坏恒定条件。但仅靠静电场不能维持闭合回路中的恒定电流：静电场是**保守场**，$\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0$，正电荷沿回路运动一周，静电场做的总功为零，而电流通过电阻时不断把能量转化为热。所以回路中必须有一段，载流子在那里受到与静电力方向相反的力，从低电势处被推回高电势处。

**定义 5.4.1（非静电力与电源）** 能使正电荷逆着静电场从低电势处移到高电势处的力称为**非静电力** $\boldsymbol{F}_{\mathrm{ne}}$；提供非静电力的装置称为**电源**。

非静电力有多种来源：化学电池中是化学作用，发电机中是电磁感应（[5.3.9](/5.3.9)），温差电偶中是热扩散，光电池中是光与半导体的相互作用。电源并不产生电荷，它只是电荷的"搬运工"：把其他形式的能量转化为电能。

### 5.4.2. 电动势

仿照**电场强度**，定义非静电场强 $\boldsymbol{E}_{\mathrm{ne}} = \boldsymbol{F}_{\mathrm{ne}}/q$。

**定义 5.4.2（电动势）** 电源内把单位正电荷从负极移到正极时非静电力所做的功

$$
\mathcal{E} = \int_{-}^{+}\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l} = \frac{A_{\mathrm{ne}}}{q}
$$
（积分沿电源内部进行）称为电源的**电动势**，单位伏特。规定电源内由负极指向正极的方向为电动势的方向。若 $\boldsymbol{E}_{\mathrm{ne}}$ 分布在整个回路 $L$ 上（如感生电动势，[5.3.9](/5.3.9)），回路的电动势为

$$
\mathcal{E} = \oint_L\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l} .
$$

注意区分电压与电动势。电压由静电场决定，$U_{12} = \int_1^2\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}$ 与路径无关；沿回路 $L$ 由点 1 到点 2 的电动势 $\mathcal{E}_{12} = \int_{1(L)}^{2}\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l}$ 与路径有关。电动势是非静电力引起的"电势升高"，反映电源把其他形式的能量转化为电能的本领。

### 5.4.3. 温差电现象

**定义 5.4.3（Seebeck 效应）** 两种不同的金属（如铜与铁）连接成闭合回路，若两个接头的温度不同，回路中就产生电动势和电流，这种现象称为**Seebeck 效应**（Seebeck 效应，1821 年发现），这样的电动势称为温差电动势。

温差电动势有两个来源：同一种金属中，温度**梯度**使自由电子从热端向冷端扩散，形成 Thomson 电动势；两种金属的接头处，自由电子浓度不同而互相扩散，形成与温度有关的接触电动势，即 Peltier 电动势。

把两种金属的一个接头置于待测温度 $T_1$、另一个接头置于已知的恒定温度 $T_2$，测量回路的温差电动势（一般约每 $100^\circ\mathrm{C}$ 几毫伏）就能确定 $T_1$，这就是温差电偶（热电偶）。它热容小、灵敏度高（可达 $10^{-3}\,^\circ\mathrm{C}$），能逐点测量很小范围内的温度变化，测温范围宽（约 $-200^\circ\mathrm{C}$ 到 $2000^\circ\mathrm{C}$），便于自动控制。扫描热显微镜把钨与镍在探针尖处接成热电偶，探针与表面距离不同时针尖的散热不同、温度不同，由此得到表面的形貌像。

## 5.5. 有电动势的电路

### 5.5.1. 恒定电路的特点

**性质 5.5.1** 恒定电流流过的均匀导体内部没有净电荷，净电荷只分布在导体的表面和不均匀处（电极、导线表面、不同导体的交界面、弯折处等）。

**证明** 对均匀导体，$\sigma$ 为常数。由恒定条件与 Ohm 定律，$\nabla\cdot\boldsymbol{J} = \sigma\nabla\cdot\boldsymbol{E} = 0$，再由**高斯定理**的微分形式，$\rho_q = \varepsilon_0\nabla\cdot\boldsymbol{E} = 0$。$\square$

外电路的导线内部，电流线与电场线方向一致，并且必然与导线表面平行：否则电流会流到表面上，表面电荷不断堆积，破坏恒定性。导线弯折时，正是导线表面的电荷分布产生了使载流子"拐弯"的电场。

在电源内部，载流子同时受静电力与非静电力的作用，Ohm 定律推广为

$$
\boldsymbol{J} = \sigma(\boldsymbol{E} + \boldsymbol{E}_{\mathrm{ne}}) .
$$

### 5.5.2. 全电路 Ohm 定律

把 $\boldsymbol{J}/\sigma = \boldsymbol{E} + \boldsymbol{E}_{\mathrm{ne}}$ 沿电源内部从负极积分到正极。电源的内阻为 $r$，电流 $I$ 的正方向规定为电源内由负极指向正极：

$$
\int_-^+\frac{\boldsymbol{J}}{\sigma}\cdot\mathrm{d}\boldsymbol{l} = Ir,\qquad
\int_-^+\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = \varphi_- - \varphi_+ = -U,\qquad
\int_-^+\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l} = \mathcal{E},
$$
其中 $U = \varphi_+ - \varphi_-$ 是电源的端电压。于是 $Ir = -U + \mathcal{E}$，即 $U = \mathcal{E} - Ir$。外电路电阻为 $R$ 时 $U = IR$，得到：

**定理 5.5.1（全电路 Ohm 定律）**

$$
I = \frac{\mathcal{E}}{R + r} .
$$

### 5.5.3. Kirchhoff 第二定律

复杂电路由许多支路组成，每条支路上可能有电阻和电源。

**定理 5.5.2（一段含源电路的 Ohm 定律）** 一段由 $a$ 到 $b$ 的含源电路上，第 $i$ 个元件的电流为 $I_i$、电阻为 $R_i$、电源电动势为 $\mathcal{E}_i$、内阻为 $r_i$，规定 $I_i$ 与 $\mathcal{E}_i$ 以由 $a$ 指向 $b$ 为正，则

$$
U_{ab} = \varphi_a - \varphi_b = \sum_i\big[I_i(R_i + r_i) - \mathcal{E}_i\big] .
$$

沿电流方向经过电阻，电势降低 $IR$；沿电动势方向经过电源，电势升高 $\mathcal{E}$。令 $b = a$，就得到：

**定理 5.5.3（Kirchhoff 第二定律）** 沿复杂电路中任一闭合回路绕行一周，

$$
\sum_i\mathcal{E}_i = \sum_iI_i(R_i + r_i),
$$
其中与绕行方向一致的 $I_i$、$\mathcal{E}_i$ 取正，相反的取负（回路电压方程）。

第一定律来自电荷守恒（恒定条件），第二定律来自**静电场的环路定理**（能量守恒）。对有 $n$ 个节点、$b$ 条支路的连通电路，独立的节点方程有 $n - 1$ 个，独立的回路方程有 $b - n + 1$ 个，恰好对应电路图的一棵**生成树**之外的 $b - n + 1$ 条边所确定的**基本回路**（[1.4.3](/1.4.3)）。两者合起来是关于 $b$ 个支路电流的 $b$ 元**线性方程组**，有唯一解。Kirchhoff 1847 年研究这类方程的解时，用电路图的生成树表示各支路电流，由此得到了图论中的**矩阵树定理**。

**例 5.5.1（无限梯形网络）** 由相同电阻 $R$ 组成的无限梯形网络：每一级是一个串联电阻（上边）和一个并联电阻（横档）。电动势 $\mathcal{E}$ 的理想电源接在网络的输入端。求：（1）网络的等效电阻 $R_x$；（2）第 $n$ 级串联电阻与第 $n$ 个横档上的电流。

**解**（1）去掉第一级后，剩下的网络仍是同样的无限网络，等效电阻仍为 $R_x$。所以第一级的横档与 $R_x$ 并联，再与第一个串联电阻串联：

$$
R_x = R + \frac{RR_x}{R + R_x}\quad\Longrightarrow\quad R_x^2 - RR_x - R^2 = 0,\qquad R_x = \frac{1 + \sqrt5}{2}R .
$$
（2）设第 $i$ 级串联电阻上的电流为 $I_i$，它在第 $i$ 个横档与后面的网络 $R_x$ 之间按电阻的反比分配：

$$
I_{i+1} = \frac{R}{R + R_x}I_i,\qquad I_i' = \frac{R_x}{R + R_x}I_i .
$$
记 $\phi = \frac{1 + \sqrt5}{2}$（黄金比，$\phi^2 = \phi + 1$），则 $\frac{R}{R + R_x} = \frac{1}{1 + \phi} = \phi^{-2}$，$\frac{R_x}{R + R_x} = \phi^{-1}$，$I_1 = \frac{\mathcal{E}}{R_x} = \frac{\mathcal{E}}{\phi R}$，所以

$$
I_n = \phi^{-(2n-1)}\frac{\mathcal{E}}{R},\qquad I_n' = \phi^{-2n}\frac{\mathcal{E}}{R} .
$$
电流沿网络按几何级数衰减，每一级衰减为 $\phi^{-2} \approx 0.38$ 倍。

**例 5.5.2（无限方格网络）** 无限大的正方形网格，每条边的电阻都是 $r$。求相邻两个节点 $A$、$B$ 之间的等效电阻。

**解** 用**叠加原理**。先设电流 $I$ 从 $A$ 流入、从无穷远流出：由对称性，从 $A$ 出发的四条边各分得 $I/4$，边 $AB$ 上的电流为 $I/4$（由 $A$ 到 $B$）。再设电流 $I$ 从无穷远流入、从 $B$ 流出：边 $AB$ 上的电流也是 $I/4$（由 $A$ 到 $B$）。两者叠加就是电流 $I$ 从 $A$ 流入、从 $B$ 流出，且无穷远处没有净电流；此时边 $AB$ 上的电流为 $I/2$，$U_{AB} = \frac I2r$，所以

$$
R_{AB} = \frac r2 .
$$
这里叠加之所以成立，是因为电路方程是线性的。

**例 5.5.3（用 Kirchhoff 定律解电路）** 两个节点 $a$（上）与 $b$（下）之间并联三条支路：左支路是电源 $\mathcal{E}_1 = 10\,\mathrm{V}$（内阻 $r_1 = 1\,\Omega$）与电阻 $R_1 = 1\,\Omega$；中间支路是电源 $\mathcal{E}_3 = 12\,\mathrm{V}$（$r_3 = 1\,\Omega$）与 $R_3 = 3\,\Omega$；右支路是电源 $\mathcal{E}_2 = 16\,\mathrm{V}$（$r_2 = 1\,\Omega$）与 $R_2 = 1\,\Omega$。三个电源的正极都朝向 $a$。求三条支路的电流。

**解** 规定三条支路的电流 $I_1$、$I_2$、$I_3$ 都以支路中由 $b$ 流向 $a$ 为正。由一段含源电路的 Ohm 定律，

$$
\varphi_a - \varphi_b = \mathcal{E}_1 - I_1(R_1 + r_1) = \mathcal{E}_2 - I_2(R_2 + r_2) = \mathcal{E}_3 - I_3(R_3 + r_3),
$$
由节点 $a$ 的电流方程，$I_1 + I_2 + I_3 = 0$。记 $U = \varphi_a - \varphi_b$，代入数值，

$$
\frac{10 - U}{2} + \frac{16 - U}{2} + \frac{12 - U}{4} = 0\quad\Longrightarrow\quad U = 12.8\,\mathrm{V},
$$
于是 $I_1 = -1.4\,\mathrm{A}$，$I_2 = 1.6\,\mathrm{A}$，$I_3 = -0.2\,\mathrm{A}$：电流从右支路流向 $a$，再经左支路与中间支路流回 $b$，电动势 $16\,\mathrm{V}$ 的电源在给另外两个电源"充电"。

这种以节点电势为未知量的方法称为节点电势法。较大的网络直接写成矩阵形式，用数值线性代数求解（[4.4.3](/4.4.3)）：

```python
import numpy as np

# unknowns: I1, I2, I3 (from b to a in each branch) and U = phi_a - phi_b
A = np.array([
    [1.0, 1.0, 1.0, 0.0],   # node a: I1 + I2 + I3 = 0
    [2.0, 0.0, 0.0, 1.0],   # E1 = I1 (R1 + r1) + U
    [0.0, 2.0, 0.0, 1.0],   # E2 = I2 (R2 + r2) + U
    [0.0, 0.0, 4.0, 1.0],   # E3 = I3 (R3 + r3) + U
])
b = np.array([0.0, 10.0, 16.0, 12.0])
print(np.linalg.solve(A, b))  # [-1.4  1.6 -0.2 12.8]
```

### 5.5.4. 恒定电流场与静电场的联合求解

导**电介质**中有恒定电流时，总伴随着电场。确定电流分布与电场分布的基本方程是

$$
\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = 0,\qquad \oint_L\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0,\qquad \boldsymbol{J} = \sigma\boldsymbol{E} .
$$
三个方程是闭合的，可以完全确定导电介质中的恒定电流场与电场。像 [5.3.4](/5.3.4) 中那样作小扁柱面与小矩形回路，由前两式得到两种导电介质交界面上的界面关系：

**定理 5.5.4（恒定电流场的界面关系）**

$$
J_{1\mathrm{n}} = J_{2\mathrm{n}},\qquad E_{1\mathrm{t}} = E_{2\mathrm{t}} .
$$

由此可知：

- 导电介质中的恒定电流场与电场完全由导电特性（电导率 $\sigma$）决定，与介质的极化性质（**电容率** $\varepsilon$）无关。
- 由 $\boldsymbol{E}$ 的高斯定理可以求出总电荷（自由电荷加**极化电荷**）的分布，它也只与 $\sigma$ 有关。
- 由 $\boldsymbol{D} = \varepsilon\boldsymbol{E}$ 与 $\boldsymbol{D}$ 的高斯定理可以求出自由电荷的分布；自由电荷与极化电荷各占多少，与 $\varepsilon$ 有关。

**例 5.5.4（两层导电介质）** 平行板电容器内填充两层导电介质，厚度、电容率与电导率分别为 $(d_1, \varepsilon_1, \sigma_1)$ 与 $(d_2, \varepsilon_2, \sigma_2)$，介质 1 与高电势的极板相接，两极板间的电压为 $U$。求：（1）两层介质中的电流密度与场强；（2）两层介质的分界面上的总电荷面密度 $\sigma_q$ 与自由电荷面密度 $\sigma_{q,0}$。

**解**（1）由对称性，电流与场强都垂直于极板，由界面关系 $J_1 = J_2 = J$。于是 $E_1 = J/\sigma_1$，$E_2 = J/\sigma_2$，又 $U = E_1d_1 + E_2d_2$，解得

$$
J = \frac{\sigma_1\sigma_2}{\sigma_1d_2 + \sigma_2d_1}U,\qquad
E_1 = \frac{\sigma_2U}{\sigma_1d_2 + \sigma_2d_1},\qquad
E_2 = \frac{\sigma_1U}{\sigma_1d_2 + \sigma_2d_1} .
$$
$\sigma_1 \ne \sigma_2$ 时场强在界面上不连续，界面上有电荷积累。

（2）在界面上作小扁柱面，法向由介质 1 指向介质 2（即沿电流方向），分别用 $\boldsymbol{E}$ 与 $\boldsymbol{D}$ 的高斯定理：

$$
\sigma_q = \varepsilon_0(E_2 - E_1) = \frac{\varepsilon_0(\sigma_1 - \sigma_2)U}{\sigma_1d_2 + \sigma_2d_1},\qquad
\sigma_{q,0} = \varepsilon_2E_2 - \varepsilon_1E_1 = \frac{(\varepsilon_2\sigma_1 - \varepsilon_1\sigma_2)U}{\sigma_1d_2 + \sigma_2d_1} .
$$
即使 $\sigma_1 = \sigma_2$（总电荷为零），只要 $\varepsilon_1 \ne \varepsilon_2$，界面上仍有自由电荷，它与极化电荷恰好抵消。

**例 5.5.5（球形接地电极）** 半径为 $a$ 的金属球作为接地电极埋在电导率为 $\sigma$ 的大地中，埋深 $h \gg a$。求接地电阻。

**解** 设接地电流为 $I$。$h \gg a$ 时可以忽略地面的影响，电流沿径向均匀流出，

$$
\boldsymbol{J} = \frac{I}{4\pi r^2}\boldsymbol{e}_r,\qquad \boldsymbol{E} = \frac{\boldsymbol{J}}{\sigma} = \frac{I}{4\pi\sigma r^2}\boldsymbol{e}_r .
$$
电极相对无穷远处的电压与接地电阻为

$$
U = \varphi_a - \varphi_\infty = \int_a^\infty\frac{I\,\mathrm{d}r}{4\pi\sigma r^2} = \frac{I}{4\pi\sigma a},\qquad R = \frac UI = \frac{1}{4\pi\sigma a} \propto \frac{1}{\sigma a} .
$$
大地的电导率约为 $10^{-3}$–$10^{-1}\,\mathrm{S\,m^{-1}}$，取 $\sigma = 10^{-2}\,\mathrm{S\,m^{-1}}$、$a = 0.5\,\mathrm{m}$，得 $R \approx 16\,\Omega$。实际的接地电阻一般在 $1$–$10\,\Omega$ 的量级（电力系统通常要求不超过 $4\,\Omega$ 或 $10\,\Omega$），所以要用多根接地极并联、降阻剂等方法减小它。

怎样减小接地电阻？距球心 $r$ 处的电势为

$$
\varphi(r) = \int_r^\infty\frac{I\,\mathrm{d}r'}{4\pi\sigma r'^2} = \frac{I}{4\pi\sigma r} = U\frac ar,
$$
$r = 10a$ 处 $\varphi = 0.1U$，即 $90\%$ 的电势降落发生在 $r < 10a$ 的范围内。所以改善接地极附近土壤的导电性，是减小整个接地电阻的关键。同样由于电势在接地点附近变化剧烈，大电流入地时（如雷击、高压线落地），人在附近两脚之间会有危险的"跨步电压"。

![球形接地电极周围的电势 $\varphi(r) = \varphi_a a/r$：$90\%$ 的电势降落发生在 $r < 10a$ 的范围内](./plots/grounding-electrode.py)

## 5.6. 电流的一种经典微观图像

Ohm 定律的微分形式说电流密度（由电子的速度决定）与场强（决定电子的加速度）成正比。为什么不是速度越来越大？Drude 在 1900 年提出的 Drude 模型（Drude model）给出了经典的解释：电子在电场中加速，但不断与晶格中的离子"碰撞"，每次碰撞后速度的方向变得完全无规，电场赋予的定向速度随之丧失。

设单位体积中有 $n$ 个自由电子。第 $i$ 个电子上次碰撞后的速度为 $\boldsymbol{v}_{0i}$，经过时间 $t_i$ 后速度为

$$
\boldsymbol{v}_i = \boldsymbol{v}_{0i} - \frac{e}{m_{\mathrm{e}}}\boldsymbol{E}t_i .
$$
电流密度是对所有电子求和：

$$
\boldsymbol{J} = -e\sum_{i=1}^n\boldsymbol{v}_i = -e\sum_{i=1}^n\boldsymbol{v}_{0i} + \frac{e^2}{m_{\mathrm{e}}}\boldsymbol{E}\sum_{i=1}^nt_i .
$$
碰撞后速度的方向无规，第一项为零；第二项中 $\frac1n\sum t_i = \tau$ 是电子自上次碰撞以来经过的平均时间。若碰撞是随机发生的，自由飞行时间服从**指数分布**，由它的**无记忆性**，这个平均值等于两次碰撞之间的平均自由飞行时间，即**弛豫时间**。于是 $\boldsymbol{J} = \dfrac{ne^2\tau}{m_{\mathrm{e}}}\boldsymbol{E}$，得到：

**公式 5.6.1（Drude 电导率）**

$$
\sigma = \frac{ne^2\tau}{m_{\mathrm{e}}} .
$$

对铜，$\sigma \approx 6.0\times10^7\,\mathrm{S\,m^{-1}}$，$n \approx 8.5\times10^{28}\,\mathrm{m^{-3}}$，得 $\tau \approx 2.5\times10^{-14}\,\mathrm{s}$。电子的速度乘以 $\tau$ 就是**平均自由程**（[5.2.2](/5.2.2#sec-2.3)）。

不同散射机制的碰撞频率相加，这称为 Matthiessen 规则（Matthiessen's rule）：$\dfrac1\tau = \dfrac1{\tau_{\mathrm{imp}}} + \dfrac1{\tau_{\mathrm{ph}}} + \dfrac1{\tau_{\mathrm{ee}}}$，分别来自杂质与缺陷、晶格振动（声子）和电子之间的散射，所以 $\rho = \rho_{\mathrm{imp}} + \rho_{\mathrm{ph}}(T) + \cdots$。晶格振动随温度增强，金属的电阻随温度升高而增大；低温下只剩与温度无关的杂质散射，电阻率趋于常数（剩余电阻率）。

**注** 经典模型在一定范围内与实验近似符合，但有根本困难：若用经典的热运动速率 $\propto\sqrt T$ 计算**平均自由程**，得到的电阻率 $\propto\sqrt T$，而实验是 $\propto T$；求出的平均自由程也比离子间距大得多，与"电子与离子碰撞"的图像矛盾。正确的解释要用量子理论：导电电子以 Fermi 速度运动，周期晶格本身不散射电子，散射来自晶格振动与杂质（[5.5.6](/5.5.6)）。

### 5.6.1. Joule 定律

电场对电子做的功在碰撞中转化为晶格的热运动能量，即**内能**。在上述模型中，电子在两次碰撞之间获得的定向速度为 $\frac{eE}{m_{\mathrm{e}}}t$，相应的动能 $\frac{e^2E^2}{2m_{\mathrm{e}}}t^2$ 在下一次碰撞中交给晶格。自由飞行时间 $t$ 服从参数为 $1/\tau$ 的指数分布，$\langle t^2\rangle = 2\tau^2$；单位时间内每个电子碰撞 $1/\tau$ 次。所以单位时间、单位体积内转化的内能为

$$
p = n\cdot\frac1\tau\cdot\frac{e^2E^2}{2m_{\mathrm{e}}}\cdot2\tau^2 = \frac{ne^2\tau}{m_{\mathrm{e}}}E^2 = \sigma E^2 .
$$

**定理 5.6.1（Joule 定律）** 导体中单位体积的热功率为

$$
p = \boldsymbol{J}\cdot\boldsymbol{E} = \sigma E^2,
$$
长 $l$、截面 $S$ 的导体通过电流 $I$ 时，发热的**功率** $P = plS = \dfrac{(JS)^2}{\sigma S}l = I^2R$。

$p = \boldsymbol{J}\cdot\boldsymbol{E}$ 是电场对电流做功的普遍表达式，与微观模型无关；积分形式 $P = UI = I^2R = U^2/R$。

## 5.7. 电容器的充电与放电

电阻 $R$ 与**电容** $C$ 串联，经开关接到电动势为 $\mathcal{E}$ 的电源上（内阻并入 $R$）。开关接通电源时电容器充电；开关把 $R$、$C$ 直接连成回路时电容器放电。

设电容器极板电荷为 $q$，回路电流 $i = \mathrm{d}q/\mathrm{d}t$。由 Kirchhoff 第二定律，充电时

$$
R\frac{\mathrm{d}q}{\mathrm{d}t} + \frac qC = \mathcal{E},
$$
放电时右端为零。这是常系数的一阶**线性微分方程**（[2.2.15](/2.2.15#sec-15.3)，[2.4.3](/2.4.3#sec-3.2)）。令 $q' = q - C\mathcal{E}$，充电方程化为齐次方程 $\dfrac{\mathrm{d}q'}{\mathrm{d}t} = -\dfrac{q'}{RC}$，其解按指数规律衰减。

**定义 5.7.1（时间常量）** $\tau = RC$ 具有时间的量纲，称为 RC 电路的**时间常量**。

**公式 5.7.1（RC 电路的充放电）** 充电（$q|_{t=0} = 0$）与放电（$q|_{t=0} = Q_0$）时，

$$
q = C\mathcal{E}\big(1 - \mathrm{e}^{-t/\tau}\big),\quad i = \frac{\mathcal{E}}{R}\mathrm{e}^{-t/\tau};\qquad\qquad
q = Q_0\mathrm{e}^{-t/\tau},\quad i = -\frac{Q_0}{RC}\mathrm{e}^{-t/\tau} .
$$

经过一个时间常量，充电达到终值的 $1 - \mathrm{e}^{-1} \approx 63\%$，放电剩下初值的 $\mathrm{e}^{-1} \approx 37\%$；经过 $5\tau$，过程基本结束（相差不到 $1\%$）。电容器两端的电压 $u_C = q/C$ 是连续的，不能突变，而电流可以突变。

![RC 电路充电与放电时电容器电压与电流随时间的变化，空心圆点是对微分方程数值积分的结果](./plots/rc-charge-discharge.py)

充电过程中的能量：电源做功 $\int_0^\infty\mathcal{E}i\,\mathrm{d}t = C\mathcal{E}^2$，电容器储存 $\frac12C\mathcal{E}^2$（[5.3.4](/5.3.4) 公式 4.5.1），电阻上发热 $\int_0^\infty i^2R\,\mathrm{d}t = \frac12C\mathcal{E}^2$。无论 $R$ 多大或多小，电源所做的功总有一半变成热。

**注** 充放电是非恒定过程（暂态过程），其中的电场是非恒定电场。只要电路的尺寸 $l$ 远小于电磁场在过程的特征时间内传播的距离，即 $l \ll c\tau$（对交流电，$l \ll c/\nu$，即远小于电磁波的波长），各处的电流在同一时刻近似相等，这样的电场称为似稳电场，Kirchhoff 定律仍然适用。这个条件称为似稳条件。例如 $50\,\mathrm{Hz}$ 交流电的波长为 $6000\,\mathrm{km}$，一般电路都满足似稳条件。

## 小结

| 规律 | 积分形式 | 微分形式 |
|---|---|---|
| 电流 | $I = \int_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S}$ | $\boldsymbol{J} = nq\boldsymbol{v}$ |
| 电流连续性方程 | $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = -\dfrac{\mathrm{d}q_{\mathrm{enc}}}{\mathrm{d}t}$ | $\nabla\cdot\boldsymbol{J} + \partial_t\rho_q = 0$ |
| 恒定条件、Kirchhoff 第一定律 | $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = 0$，$\sum I_i = 0$ | $\nabla\cdot\boldsymbol{J} = 0$ |
| Ohm 定律 | $U = IR$，$R = \rho L/S$ | $\boldsymbol{J} = \sigma\boldsymbol{E}$；电源内 $\boldsymbol{J} = \sigma(\boldsymbol{E} + \boldsymbol{E}_{\mathrm{ne}})$ |
| 电动势、Kirchhoff 第二定律 | $\mathcal{E} = \int_-^+\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l}$，$\sum\mathcal{E}_i = \sum I_i(R_i + r_i)$ | |
| Joule 定律 | $P = I^2R$ | $p = \boldsymbol{J}\cdot\boldsymbol{E} = \sigma E^2$ |
| Drude 模型 | | $\sigma = ne^2\tau/m_{\mathrm{e}}$ |
| RC 电路 | $\tau = RC$，$q = C\mathcal{E}(1 - \mathrm{e}^{-t/\tau})$ | |

## 思考题

1. 是什么力驱动载流子在导线中运动？导线弯折时，载流子是怎样"拐弯"的？
   提示：驱动载流子的是电场，它由电源两极和导线表面的电荷共同产生。接通电路的瞬间，电荷在导线表面（特别是弯折处）积累，直到导线内的电场处处沿着导线；这些表面电荷产生的电场使载流子拐弯，手对导线的形状只起"约束"作用。
2. 导体中电子的漂移速度只有 $0.01$–$0.1\,\mathrm{mm\,s^{-1}}$，为什么按下开关后灯泡立即就亮，即使导线很长？
   提示：建立电流所需要的是导线中的电场，它以接近光速的速度沿导线建立起来（表面电荷的重新分布），各处的电子几乎同时开始漂移；并不需要电子从开关处移动到灯泡处。
3. 由 Ohm 定律，导线中的电子一定逆着电场线运动，而真空中的电子却不一定，为什么？
   提示：导线中的电子不断碰撞，没有"记忆"，平均速度由当时当地的场强决定（$\boldsymbol{v}_{\mathrm{d}} \propto -\boldsymbol{E}$）；真空中的电子不碰撞，加速度由场强决定，速度还与初速度和过去的受力有关，就像抛体运动的速度不一定沿重力方向。
4. 恒定电场也满足环路定理，电子绕电路一周，恒定电场做功为零。电能是怎样转化为其他形式的能量的？
   提示：在外电路中，恒定电场对电子做正功，电子又通过碰撞把能量交给晶格（Joule 热）；在电源内部，电子逆着静电力运动，静电场做负功，这部分能量由非静电力提供。恒定电场只起传递能量的作用，能量的来源是电源中的非静电力。
