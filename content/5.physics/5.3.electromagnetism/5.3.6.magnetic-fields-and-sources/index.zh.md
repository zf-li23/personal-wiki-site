---
title: 磁场和它的源
description: 磁现象与电荷运动的联系，Lorentz 力与磁感应强度，磁感线、磁通量与磁通连续定理，Biot–Savart 定律及其应用（直导线、圆电流与磁偶极子、Helmholtz 线圈、螺线管、运动电荷），Ampère 环路定理及其应用，极矢量与轴矢量，位移电流与全电流 Ampère 环路定理。
---

前五章研究静止电荷的电场与**恒定电流**。本章转向电流的另一种效应：磁场。1820 年 Ørsted 发现电流使磁针偏转，此后不到半年，人们就认识到一切磁现象都来源于电荷的运动：磁场由运动的电荷（电流）产生，又只对运动的电荷施力。描述磁场的基本量是磁感应强度 $\boldsymbol{B}$，它由运动电荷所受的 Lorentz 力定义；电流产生磁场的规律是 Biot–Savart 定律。由它得到磁场的两条基本定理，与静电场的两条基本定理（[5.3.1](/5.3.1)、[5.3.2](/5.3.2)）恰好"互补"：

| | 静电场 $\boldsymbol{E}$ | 恒定磁场 $\boldsymbol{B}$ |
|---|---|---|
| 通量 | $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} = q_{\mathrm{enc}}/\varepsilon_0$，有源 | $\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = 0$，无源 |
| 环量 | $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0$，无旋 | $\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0I_{\mathrm{enc}}$，有旋 |

用场论的语言，静电场是**无旋场**，恒定磁场是**无源场**（[2.2.14](/2.2.14)）。最后一节说明 Ampère 环路定理只对恒定电流成立，Maxwell 引入位移电流把它推广到一般情形：变化的电场也产生磁场。这是 Maxwell 方程组（[5.3.10](/5.3.10)）的关键一步。下一章 [5.3.7](/5.3.7) 研究磁场对运动电荷与电流的作用。

## 6.1. 磁力与电荷的运动

### 6.1.1. 早期的磁现象

磁石吸铁的现象很早就为人所知，《管子》中已有"上有慈石者，其下有铜金"的记载，指南针更是古代中国的重要发明。基本的磁现象是：磁铁能吸引铁、钴、镍等物质；磁铁有 N、S 两极，同性相斥、异性相吸；把磁铁切开，每一块都仍有各自的 N 极和 S 极，从未得到单独的磁极。

人们也零星地观察到电与磁的联系：雷电使钢刀叉磁化（1731 年），莱顿瓶放电使缝衣针磁化（Franklin，1751 年）。但直到 19 世纪初，Coulomb、Ampère 等人仍认为电和磁是彼此无关的两类现象，电学与磁学是独立发展的。

### 6.1.2. Ørsted 实验

1820 年，丹麦物理学家 Ørsted 发现通电导线附近的磁针会偏转，揭示了电流的磁效应；在磁针与导线之间放入玻璃、金属、木头、水等，偏转并不减弱。这一发现开启了电磁学的新纪元。同年之内，Ampère 研究了圆电流对磁针的作用、两段平行直导线的相互作用，并发现载流螺线管与磁棒等效；Arago 发现钢片在电流作用下被磁化；Biot 与 Savart 测量了长直导线对磁针的作用。从 Ørsted 的发现到对磁现象较为系统的认识只用了半年时间。

实验表明，磁相互作用有以下几种：通电导线对磁针的作用，磁铁对通电导线的作用，通电导线之间的作用，磁铁对运动电子（如阴极射线）的作用。它们的共同点是至少一方涉及电荷的运动。

### 6.1.3. 磁荷说与分子电流假说

一种解释是仿照电荷引入"磁荷" $Q_{\mathrm{m}}$，假设磁荷之间也有平方反比的力，$\boldsymbol{F}_{21} = k\dfrac{Q_{\mathrm{m}1}Q_{\mathrm{m}2}}{r^2}\boldsymbol{e}_{r}$。1931 年 Dirac 从量子力学论证，如果存在磁单极子（magnetic monopole），即单独的磁荷，电荷就必然是量子化的。但至今没有发现磁单极子存在的确凿实验证据。凝聚态体系（如自旋冰）中有一些行为类似磁单极子的准粒子激发，它们不是基本粒子。

另一种解释是 Ampère 的分子电流假说：磁体的分子内部有环形的电流（分子电流），每个分子相当于一个小磁体。非磁性材料中分子电流的取向杂乱无章，它们的磁场互相抵消；磁性材料中分子电流的取向大致相同，两端就显示出磁极。分子电流说能自然地解释磁棒与载流螺线管的相似性，也能解释为什么切不出单独的磁极。按照这种观点，一切磁相互作用都归结为电流（运动电荷）之间的相互作用：电荷的运动是一切磁现象的起源。于是像静电学那样，只要找到电流产生磁场的规律和磁场对电流的作用规律，就能解决磁相互作用的问题。分子电流的微观本质（电子的轨道运动与自旋）要到量子力学中才能说明（[5.3.8](/5.3.8)、[5.5.4](/5.5.4)）。

## 6.2. 磁场与磁感应强度

### 6.2.1. 磁场

与电荷之间通过电场相互作用一样，电流之间的磁相互作用是通过磁场传递的：电流（运动电荷）在周围空间产生磁场，磁场对处于其中的其他电流（运动电荷）施加作用力。磁场与电场一样是物质存在的一种形态，具有能量与动量：它对磁场中的运动电荷有作用力，在磁场中移动载流导线时，磁场力对导线做功。运动电荷周围既有电场，也有磁场。

### 6.2.2. 磁感应强度

用运动电荷在磁场中的受力定义描述磁场的物理量。实验发现，电荷 $q$ 以速度 $\boldsymbol{v}$ 通过磁场中某点时：

- 所受的磁力总与 $\boldsymbol{v}$ 垂直，大小与 $q$、$v$ 成正比；
- 磁力的大小与 $\boldsymbol{v}$ 的方向有关：沿某一特定方向运动时磁力为零，与这一方向垂直时磁力最大。

**定义 6.2.1（磁感应强度）** 电荷沿其运动时不受磁力的方向，就是该点**磁感应强度** $\boldsymbol{B}$ 的方向（指向由下式确定）；电荷垂直于该方向运动时所受的最大磁力为 $F_{\max}$，$\boldsymbol{B}$ 的大小为

$$
B = \frac{F_{\max}}{qv} .
$$
磁感应强度的单位是特斯拉，$1\,\mathrm{T} = 1\,\mathrm{N\,A^{-1}\,m^{-1}}$。

把上述实验规律合写成一个式子：

**定义 6.2.2（Lorentz 力）** 电荷 $q$ 以速度 $\boldsymbol{v}$ 在磁感应强度为 $\boldsymbol{B}$ 的磁场中运动时所受的磁力

$$
\boldsymbol{F} = q\boldsymbol{v}\times\boldsymbol{B}
$$
称为 **Lorentz 力**（洛伦兹力）。同时有电场时，电荷所受的电磁力为 $\boldsymbol{F} = q(\boldsymbol{E} + \boldsymbol{v}\times\boldsymbol{B})$。

$\boldsymbol{v}\times\boldsymbol{B}$ 是**向量积**，所以 Lorentz 力总与速度垂直，对电荷不做功。文献中常见的 CGS 单位高斯与特斯拉的换算为 $1\,\mathrm{T} = 10^4\,\mathrm{Gs}$，本课程一律用 SI。几种典型的磁感应强度：

| 场合 | $B/\mathrm{T}$ |
|---|---|
| 地球表面的地磁场 | $(3$–$6)\times10^{-5}$ |
| 冰箱贴 | 约 $5\times10^{-3}$ |
| 医用磁共振成像 | $1.5$–$3$（研究用可达 $7$ 以上） |
| 实验室最强的稳恒磁场 | 约 $45$ |
| 中子星表面 | $10^{6}$–$10^{9}$，磁星可达 $10^{11}$ |

**性质 6.2.1（磁场叠加原理）** 几个场源同时存在时，场点的磁感应强度等于各个场源单独存在时在该点产生的磁感应强度的矢量和：$\boldsymbol{B} = \sum_i\boldsymbol{B}_i$，或 $\boldsymbol{B} = \int\mathrm{d}\boldsymbol{B}$。

### 6.2.3. 磁感线与磁通量

**定义 6.2.3（磁感线）** 在磁场中画一系列曲线，使曲线上每一点的切线方向都是该点 $\boldsymbol{B}$ 的方向，并使通过垂直于 $\boldsymbol{B}$ 的单位面积的曲线条数等于该处 $B$ 的大小，这些曲线称为**磁感线**（磁感应线）。

直线电流、圆电流、直螺线管、环形螺线管的磁感线表明：任何两条磁感线都不相交；磁感线与电流成右手螺旋关系；磁感线是围绕电流、无头无尾的闭合曲线（6.3 节画出了圆电流的磁感线）。

**定义 6.2.4（磁通量）** 磁感应强度对曲面 $S$ 的通量

$$
\Phi = \int_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}
$$
称为通过 $S$ 的**磁通量**，单位韦伯，$1\,\mathrm{Wb} = 1\,\mathrm{T\,m^2}$。它等于穿过 $S$ 的磁感线的条数。

### 6.2.4. 磁通连续定理

下一节的 Biot–Savart 定律表明，每个电流元的磁感线都是圆心在电流元轴线上的同心圆，是闭合曲线，所以一个电流元的磁场穿过任何闭合曲面的磁通量都为零。由叠加原理，对任意电流的磁场：

**定理 6.2.1（磁通连续定理）** 通过任意闭合曲面的磁通量恒等于零：

$$
\oint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = 0,\qquad \nabla\cdot\boldsymbol{B} = 0 .
$$
这也称为磁场的高斯定理。微分形式由 **Gauss 公式**得到。

磁场是**无源场**：它没有发出或吸收磁感线的"源"，这与目前没有发现磁单极子的事实一致。若将来发现磁单极子，右端要加上磁荷项。由 $\nabla\cdot\boldsymbol{B} = 0$，总可以把 $\boldsymbol{B}$ 写成另一个矢量场的**旋度**，$\boldsymbol{B} = \nabla\times\boldsymbol{A}$，$\boldsymbol{A}$ 称为矢势（6.3 节圆电流的磁感线图就是用矢势画出的）。

## 6.3. Biot–Savart 定律

把电流看成一段段电流元 $I\,\mathrm{d}\boldsymbol{l}$（$\mathrm{d}\boldsymbol{l}$ 沿电流方向），先求每个电流元产生的磁场，再由叠加原理求总的磁场。Biot、Savart 的实验经 Laplace 的数学分析，得到电流元的磁场：

**定理 6.3.1（Biot–Savart 定律）** 电流元 $I\,\mathrm{d}\boldsymbol{l}$ 在位矢为 $\boldsymbol{r}$（由电流元指向场点）处产生的磁感应强度为

$$
\mathrm{d}\boldsymbol{B} = \frac{\mu_0}{4\pi}\frac{I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{e}_r}{r^2},
$$
其中 $\boldsymbol{e}_r = \boldsymbol{r}/r$，$\mu_0$ 称为真空磁导率（vacuum permeability）。

电流元的磁感线在垂直于电流元的平面内，是圆心在电流元轴线上的一系列同心圆，绕向与电流方向成右手螺旋关系。$\mathrm{d}B$ 与 $r^2$ 成反比、与 $\sin\theta$（$\mathrm{d}\boldsymbol{l}$ 与 $\boldsymbol{r}$ 的夹角）成正比；沿电流元的延长线上 $\mathrm{d}\boldsymbol{B} = \boldsymbol{0}$。原则上，Biot–Savart 定律与叠加原理可以求出任意电流分布的磁场：

$$
\boldsymbol{B} = \frac{\mu_0}{4\pi}\int_L\frac{I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{e}_r}{r^2} .
$$

**注** 2019 年 SI 修订以前，安培由平行导线间的力定义，$\mu_0 = 4\pi\times10^{-7}\,\mathrm{N\,A^{-2}}$ 是精确值。修订后改为固定**元电荷** $e$，$\mu_0$ 成为由实验测定的量，$\mu_0 = 1.256\,637\,061\,27(20)\times10^{-6}\,\mathrm{N\,A^{-2}}$，与 $4\pi\times10^{-7}$ 只在第十位有效数字上有差别，计算中仍可取 $4\pi\times10^{-7}\,\mathrm{N\,A^{-2}}$。$\varepsilon_0\mu_0 = 1/c^2$ 仍然精确成立。

### 6.3.1. Ampère 定律与 Newton 第三定律

把 Biot–Savart 定律与 Lorentz 力（对电流元，$\mathrm{d}\boldsymbol{F} = I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}$，[5.3.7](/5.3.7)）结合，得到两个孤立电流元之间的作用力（Ampère 定律）：

$$
\mathrm{d}\boldsymbol{F}_{12} = I_2\,\mathrm{d}\boldsymbol{l}_2\times\Big(\frac{\mu_0}{4\pi}\frac{I_1\,\mathrm{d}\boldsymbol{l}_1\times\boldsymbol{e}_{12}}{r_{12}^2}\Big),
$$
其中 $\mathrm{d}\boldsymbol{F}_{12}$ 是电流元 1 对电流元 2 的力，$\boldsymbol{e}_{12}$ 由 1 指向 2。Ampère 定律与 Biot–Savart 定律的地位相同。

一般 $\mathrm{d}\boldsymbol{F}_{12} \ne -\mathrm{d}\boldsymbol{F}_{21}$。例如两个电流元互相垂直、$I_1\,\mathrm{d}\boldsymbol{l}_1$ 沿两者连线时，$\mathrm{d}\boldsymbol{B}_1$ 在电流元 2 处为零，$\mathrm{d}\boldsymbol{F}_{12} = \boldsymbol{0}$，而 $\mathrm{d}\boldsymbol{F}_{21} \ne \boldsymbol{0}$：两个电流元之间的力不满足 **Newton 第三定律**。这与**动量守恒定律**并不矛盾。电荷、电流之间的相互作用是通过电磁场传递的，不是超距作用，电磁场本身也有动量（[5.3.10](/5.3.10)）；可以证明，场源的动量加上场的动量是守恒的。所以**动量守恒定律**更普遍，**Newton 第三定律**只是它在力学范围内的表现形式（[5.1.3](/5.1.3)）。对两个闭合的恒定电流回路，相互作用力仍满足 Newton 第三定律。

Biot–Savart 定律与 Ampère 定律是实验的总结，但不能用实验直接验证，因为不存在孤立的恒定电流元（恒定电流必须闭合，[5.3.5](/5.3.5)）。能直接验证的只是它们对闭合回路积分的结果。

### 6.3.2. 应用举例

**例 6.3.1（载流直导线的磁场）** 求载流直导线段 $A_1A_2$（电流 $I$）在距导线 $r_0$ 的点 $P$ 产生的磁感应强度。

**解** 各电流元在 $P$ 点产生的 $\mathrm{d}\boldsymbol{B}$ 方向相同（垂直于导线与 $P$ 所在的平面，与电流成右手螺旋），只需把大小相加。设电流元 $I\,\mathrm{d}l$ 到 $P$ 的连线与电流方向的夹角为 $\theta$，以 $P$ 在导线上的垂足 $O$ 为原点，$l = -r_0\cot\theta$，$\mathrm{d}l = \dfrac{r_0\,\mathrm{d}\theta}{\sin^2\theta}$，$r = \dfrac{r_0}{\sin\theta}$，

$$
B = \int\frac{\mu_0}{4\pi}\frac{I\,\mathrm{d}l\sin\theta}{r^2} = \frac{\mu_0I}{4\pi r_0}\int_{\theta_1}^{\theta_2}\sin\theta\,\mathrm{d}\theta = \frac{\mu_0I}{4\pi r_0}(\cos\theta_1 - \cos\theta_2),
$$
其中 $\theta_1$、$\theta_2$ 是导线起点 $A_1$ 与终点 $A_2$ 处的 $\theta$。无限长直导线 $\theta_1 = 0$，$\theta_2 = \pi$；半无限长直导线、$P$ 在端点的垂线上时 $\theta_1 = \pi/2$，$\theta_2 = \pi$：

$$
B_\infty = \frac{\mu_0I}{2\pi r_0},\qquad B_{\text{semi}} = \frac{\mu_0I}{4\pi r_0} .
$$

**例 6.3.2（圆电流轴线上的磁场）** 半径为 $R$ 的圆电流 $I$，求其轴线上距圆心 $x$ 处的磁感应强度。

**解** 圆环上每个电流元 $I\,\mathrm{d}l$ 都与它到场点的连线垂直，$\mathrm{d}B = \dfrac{\mu_0I\,\mathrm{d}l}{4\pi r^2}$，$r^2 = R^2 + x^2$。由轴对称性，$\mathrm{d}\boldsymbol{B}$ 垂直于轴线的分量互相抵消，只剩沿轴线的分量 $\mathrm{d}B_\parallel = \mathrm{d}B\cdot\dfrac Rr$：

$$
B = \oint\frac{\mu_0I}{4\pi r^2}\frac Rr\,\mathrm{d}l = \frac{\mu_0IR}{4\pi r^3}\cdot2\pi R = \frac{\mu_0IR^2}{2(R^2 + x^2)^{3/2}},
$$
方向沿轴线，与电流成右手螺旋关系。圆心处 $B = \dfrac{\mu_0I}{2R}$。

远处（$x \gg R$）$B \approx \dfrac{\mu_0IR^2}{2x^3}$，与**电偶极子**轴线上的**场强** $E = \dfrac{p}{2\pi\varepsilon_0x^3}$ 形式相同。引入矢量 $\boldsymbol{m} = IS\boldsymbol{e}_{\mathrm{n}}$（$S = \pi R^2$ 是圆电流所围的面积，$\boldsymbol{e}_{\mathrm{n}}$ 是与电流成右手螺旋的单位法向矢量），它称为线圈的磁矩，可写成 $\boldsymbol{B} = \dfrac{\mu_0\boldsymbol{m}}{2\pi x^3}$。

**定义 6.3.1（磁偶极子）** 线度远小于场点到它的距离的载流线圈称为**磁偶极子**，它的磁性由磁矩 $\boldsymbol{m} = IS\boldsymbol{e}_{\mathrm{n}}$ 完全描述（[5.3.7](/5.3.7)）。在远处，它的磁场与电偶极子的电场形式相同：

$$
\boldsymbol{B} = \frac{\mu_0}{4\pi}\Big(\frac{3(\boldsymbol{m}\cdot\boldsymbol{r})\boldsymbol{r}}{r^5} - \frac{\boldsymbol{m}}{r^3}\Big),\qquad
\boldsymbol{E} = \frac{1}{4\pi\varepsilon_0}\Big(\frac{3(\boldsymbol{p}\cdot\boldsymbol{r})\boldsymbol{r}}{r^5} - \frac{\boldsymbol{p}}{r^3}\Big) .
$$

在线圈附近两者则完全不同：电偶极子的**电场线**从正电荷出发、终止于负电荷，而圆电流的磁感线穿过线圈闭合。下图用椭圆积分精确算出圆电流的磁感线；远处它与电偶极子的电场线形状相同。

![圆电流（半径 $a$）在过轴线的平面内的磁感线：磁感线穿过线圈、无头无尾，远处趋于磁偶极子的场；左右两个符号表示电流垂直于纸面流出与流入](./plots/current-loop-field-lines.py)

**例 6.3.3（Helmholtz 线圈）** 两个半径为 $R$、各 $N$ 匝的同轴圆线圈，通以同向电流 $I$，两线圈间距等于半径 $R$。求每个线圈中心处与两线圈中点处的磁感应强度。

**解** 两线圈在轴线上的磁场方向相同。由例 6.3.2，一个线圈中心处的磁场是它自己的 $\frac{\mu_0NI}{2R}$ 加上另一个线圈在距离 $R$ 处的场：

$$
B_0 = \frac{\mu_0NI}{2R} + \frac{\mu_0NIR^2}{2(R^2 + R^2)^{3/2}} = \frac{\mu_0NI}{2R}\Big(1 + \frac{1}{2\sqrt2}\Big) \approx 0.677\frac{\mu_0NI}{R} .
$$
中点 $P$ 到两线圈的距离都是 $R/2$：

$$
B_P = 2\cdot\frac{\mu_0NIR^2}{2\big(R^2 + (R/2)^2\big)^{3/2}} = \frac{8\mu_0NI}{5\sqrt5R} \approx 0.716\frac{\mu_0NI}{R} .
$$

**定义 6.3.2（Helmholtz 线圈）** 间距等于半径的一对相同的同轴载流线圈称为 **Helmholtz 线圈**。

间距取 $d = R$ 是为了使中点附近的磁场最均匀：由对称性，$B(x)$ 在中点处的一阶导数为零；计算表明，$d = R$ 时二阶导数也为零（三阶导数由对称性为零），所以 $B(x) = B_P + O(x^4)$。实验室常用它产生不太强的均匀磁场，如抵消地磁场、测量电子的荷质比。

**例 6.3.4（载流直螺线管轴线上的磁场）** 螺线管半径为 $R$，长为 $L$，单位长度上绕 $n$ 匝，通电流 $I$。求轴线上的磁场分布。

**解** 把螺线管看成许多圆电流。轴线上点 $P$ 附近，距 $P$ 为 $l$ 处长 $\mathrm{d}l$ 的一段相当于电流 $nI\,\mathrm{d}l$ 的圆电流，由例 6.3.2，它在 $P$ 点的磁场为

$$
\mathrm{d}B = \frac{\mu_0nIR^2\,\mathrm{d}l}{2(R^2 + l^2)^{3/2}} .
$$
设该段到 $P$ 的连线与轴线的夹角为 $\beta$，$l = R\cot\beta$，$\mathrm{d}l = -\dfrac{R\,\mathrm{d}\beta}{\sin^2\beta}$，$R^2 + l^2 = \dfrac{R^2}{\sin^2\beta}$，于是 $\mathrm{d}B = -\dfrac{\mu_0nI}{2}\sin\beta\,\mathrm{d}\beta$。各段在 $P$ 点的磁场方向相同，

$$
B = -\frac{\mu_0nI}{2}\int_{\beta_1}^{\beta_2}\sin\beta\,\mathrm{d}\beta = \frac{\mu_0nI}{2}(\cos\beta_2 - \cos\beta_1),
$$
其中 $\beta_1$、$\beta_2$ 是 $P$ 到螺线管两端的连线与轴线的夹角（$\beta_1 > \beta_2$）。无限长螺线管 $\beta_1 = \pi$，$\beta_2 = 0$，$B = \mu_0nI$；半无限长螺线管端面中心处 $B = \frac12\mu_0nI$。

长 $L = 10R$ 的螺线管，中心处 $B \approx 0.98\mu_0nI$，端面中心约为 $0.50\mu_0nI$，管外距端面 $2R$ 处已降到约 $0.05\mu_0nI$。管内的磁场在中心附近相当均匀，并从中心向两端单调减小。

![左：不同长度的螺线管轴线上的磁场；右：两个同轴线圈的轴线上的磁场，间距等于半径（Helmholtz 线圈）时中点附近最平坦](./plots/solenoid-helmholtz-axis.py)

**例 6.3.5（匀速运动点电荷的磁场）** 求电荷 $q$ 以速度 $\boldsymbol{v}$（$v \ll c$）运动时产生的磁场。

**解** 设电流元的截面积为 $S$，载流子数密度为 $n$，每个载流子带电 $q$，**漂移速度**为 $\boldsymbol{v}$，则 $I = nqSv$，且 $I\,\mathrm{d}\boldsymbol{l} = nqS\,\mathrm{d}l\,\boldsymbol{v}$。电流元内共有 $nS\,\mathrm{d}l$ 个载流子，所以每个载流子产生的磁场为

$$
\boldsymbol{B} = \frac{\mathrm{d}\boldsymbol{B}}{nS\,\mathrm{d}l} = \frac{\mu_0}{4\pi}\frac{q\boldsymbol{v}\times\boldsymbol{e}_r}{r^2} .
$$
与**点电荷**的电场 $\boldsymbol{E} = \dfrac{q}{4\pi\varepsilon_0r^2}\boldsymbol{e}_r$ 比较，并利用 $\varepsilon_0\mu_0 = 1/c^2$，

$$
\boldsymbol{B} = \frac{1}{c^2}\boldsymbol{v}\times\boldsymbol{E} .
$$
这个关系对匀速运动的点电荷在任何速度下都精确成立（$\boldsymbol{E}$ 要用相对论的结果）。它表明磁场与电场是同一电磁场在不同参考系中的不同表现：在电荷静止的参考系中只有电场，在电荷运动的参考系中同时有电场与磁场（[5.1.8](/5.1.8)、[5.3.7](/5.3.7)）。磁场与电场之比 $B/E \sim v/c^2$，所以运动电荷之间的磁力与电力之比 $\sim v^2/c^2$，低速时很小；导线中的磁力之所以显著，是因为导线整体是电中性的，电力互相抵消。

**例 6.3.6（叠加法求磁场）** 均匀铜环上任意两点 $A$、$B$ 用两根沿半径方向的长直导线引到很远的**电源**上，电流 $I$ 由 $A$ 流入、由 $B$ 流出。求环心 $O$ 处的磁感应强度。

**解** 电流系统由五段组成：两根直导线、远处连接电源的导线、铜环被 $A$、$B$ 分成的两段弧（长 $L_1$、$L_2$，电流 $I_1$、$I_2$）。$O$ 在两根直导线的延长线上，它们在 $O$ 点不产生磁场；远处导线的磁场可以忽略。两段弧在 $O$ 点的磁场方向相反，大小为

$$
B_1 = \int_0^{L_1}\frac{\mu_0I_1\,\mathrm{d}l}{4\pi R^2} = \frac{\mu_0I_1L_1}{4\pi R^2},\qquad B_2 = \frac{\mu_0I_2L_2}{4\pi R^2} .
$$
两段弧并联，电压相同，$I_1R_1 = I_2R_2$；铜环均匀，**电阻**与长度成正比，$R_1/R_2 = L_1/L_2$，所以 $I_1L_1 = I_2L_2$，$B = B_1 - B_2 = 0$。

## 6.4. Ampère 环路定理

### 6.4.1. 定理的表述

**定理 6.4.1（Ampère 环路定理）** 在恒定电流的磁场中，磁感应强度沿任意闭合路径 $L$ 的线积分（**环量**），等于 $L$ 所包围（与 $L$ 套连）的电流的代数和的 $\mu_0$ 倍：

$$
\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0\sum_iI_{i,\mathrm{enc}} .
$$
任意规定 $L$ 的绕行方向，与绕行方向成右手螺旋关系的电流取正，反之取负。

注意：$\boldsymbol{B}$ 是空间中所有电流共同产生的，但环路积分只与 $L$ 所套连的电流有关；不与 $L$ 套连的电流对环量没有贡献，但对 $L$ 上各点的 $\boldsymbol{B}$ 有贡献。环路积分为零，并不表示回路上各点 $\boldsymbol{B} = \boldsymbol{0}$，也不表示回路内没有电流穿过（可能是正负电流相消）。

### 6.4.2. 定理的证明

先对无限长直线电流 $I$ 证明，再推广。

1. 在垂直于电流的平面内、以电流为圆心的圆形回路：$B = \dfrac{\mu_0I}{2\pi r}$，方向沿回路的切向，$\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \dfrac{\mu_0I}{2\pi r}\cdot2\pi r = \mu_0I$。
2. 在垂直于电流的平面内、包围电流的任意回路：$\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = B\,r\,\mathrm{d}\phi$，$\mathrm{d}\phi$ 是 $\mathrm{d}\boldsymbol{l}$ 对电流所张的角，$\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \oint\dfrac{\mu_0I}{2\pi r}r\,\mathrm{d}\phi = \dfrac{\mu_0I}{2\pi}\cdot2\pi = \mu_0I$。
3. 不包围电流的平面回路：从电流所在处引两条切线，把回路分成 $L_1$、$L_2$ 两段，它们对电流所张的角大小相等、符号相反，$\oint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \dfrac{\mu_0I}{2\pi}\big[\phi + (-\phi)\big] = 0$。
4. 非平面的闭合路径：把每个线元分解为平行于垂直平面的分量 $\mathrm{d}\boldsymbol{l}_\parallel$ 与沿电流方向的分量 $\mathrm{d}\boldsymbol{l}_\perp$。$\boldsymbol{B}$ 垂直于电流，$\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l}_\perp = 0$，只剩回路在垂直平面上的投影，化为 2、3 的情形。
5. 多根载流导线：由叠加原理，环量等于各电流单独贡献之和。

任意形状的闭合恒定电流可以看成许多电流元组成的回路，用 Biot–Savart 定律可以对一般情形证明这个定理，这里从略。

### 6.4.3. 微分形式与适用条件

设 $S$ 是以 $L$ 为边界的任意曲面，$L$ 所包围的电流 $I_{\mathrm{enc}} = \int_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S}$。由 **Stokes 公式**，$\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \int_S(\nabla\times\boldsymbol{B})\cdot\mathrm{d}\boldsymbol{S}$，对任意 $S$ 成立，所以

$$
\nabla\times\boldsymbol{B} = \mu_0\boldsymbol{J} .
$$

- **旋度**不为零，环量不为零：恒定磁场是非保守场（涡旋场），一般不能像静电场那样定义标量势。在没有电流的单连通区域中 $\nabla\times\boldsymbol{B} = \boldsymbol{0}$，才可以在该区域内定义磁标势。
- 定理只对恒定电流成立：电流必须闭合或伸展到无穷远。对 $\nabla\times\boldsymbol{B} = \mu_0\boldsymbol{J}$ 两边取**散度**，左边恒为零，所以要求 $\nabla\cdot\boldsymbol{J} = 0$，这正是恒定条件（[5.3.5](/5.3.5)）。非恒定的情形见 6.6 节。

## 6.5. 利用 Ampère 环路定理求磁场

对于有一定对称性的电流分布，用 Ampère 环路定理求磁场比用 Biot–Savart 定律简便。步骤是：分析电流分布的对称性，确定磁场的对称性（磁场的方向与大小在哪些变换下不变）；选取合适的回路，使回路上 $\boldsymbol{B}$ 的大小不变、方向与回路相切或垂直，从而把 $B$ 从积分号中提出来。

### 6.5.1. 极矢量与轴矢量

分析磁场的对称性时要注意，$\boldsymbol{B}$ 与 $\boldsymbol{E}$ 在镜像反射下的变换方式不同。

**定义 6.5.1（极矢量与轴矢量）** 在镜像反射（如对 $xy$ 平面的反射 $z \to -z$）下，与镜面平行的分量不变、与镜面垂直的分量反向的矢量，称为**极矢量**，如 $\mathrm{d}\boldsymbol{r}$、$\boldsymbol{v}$、$\boldsymbol{a}$、$\boldsymbol{p}$、$\boldsymbol{F}$、$\boldsymbol{E}$；与镜面平行的分量反向、与镜面垂直的分量不变的矢量，称为**轴矢量**（赝矢量），如角速度 $\boldsymbol{\omega}$、**角动量** $\boldsymbol{L}$、**力矩** $\boldsymbol{M}$、$\boldsymbol{B}$。

两个极矢量的**向量积**是轴矢量（如 $\boldsymbol{L} = \boldsymbol{r}\times\boldsymbol{p}$），轴矢量与极矢量的**向量积**是极矢量（如 $\boldsymbol{F} = q\boldsymbol{v}\times\boldsymbol{B}$）。定义向量积要用右手定则，镜像反射把右手变成左手，这就是轴矢量多一个负号的原因。由 Biot–Savart 定律，$\mathrm{d}\boldsymbol{B} \propto \mathrm{d}\boldsymbol{l}\times\boldsymbol{e}_r$，$\boldsymbol{B}$ 是轴矢量。

例如，无限长直线电流对任一包含导线的平面镜像对称。若 $\boldsymbol{B}$ 有平行于该平面的分量（径向分量或轴向分量），镜像后这些分量反向，而电流分布不变，矛盾，所以 $\boldsymbol{B}$ 只能垂直于包含导线的平面，即沿圆周的切向。

### 6.5.2. 应用举例

**例 6.5.1（无限长圆柱电流的磁场）** 电流 $I$ 沿半径为 $R$ 的无限长圆柱**导体**均匀流过，求导体内外的磁场。

**解** 由镜像对称性，$\boldsymbol{B}$ 沿以轴线为中心的圆周的切向；由轴对称性与平移对称性，$B$ 只与到轴线的距离 $r$ 有关。取半径为 $r$ 的同轴圆形回路：

$$
\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = 2\pi rB = \mu_0I_{\mathrm{enc}},\qquad
B = \begin{cases}\dfrac{\mu_0Ir}{2\pi R^2}, & r < R,\\[2ex] \dfrac{\mu_0I}{2\pi r}, & r > R .\end{cases}
$$
导体外的磁场与电流集中在轴线上时相同，与例 6.3.1 一致。

**例 6.5.2（无限长直螺线管的磁场）** 无限长密绕直螺线管单位长度上 $n$ 匝，通电流 $I$。求管内外的磁场。

**解** 密绕螺线管可以看成许多圆电流的排列（忽略螺距）。在柱坐标中写 $\boldsymbol{B} = B_r\boldsymbol{e}_r + B_\phi\boldsymbol{e}_\phi + B_z\boldsymbol{e}_z$，由无限长与轴对称，各分量只与 $r$ 有关。

- 以轴线为轴作半径 $r$、长 $l$ 的闭合圆柱面，两底面的通量抵消，由磁通连续定理，$2\pi rl\,B_r = 0$，所以 $B_r = 0$。
- 以轴线为中心作半径 $r$ 的圆形回路，它不套连电流（忽略螺距时，电流只沿圆周方向），由 Ampère 环路定理 $2\pi rB_\phi = 0$，$B_\phi = 0$。
- 所以 $\boldsymbol{B} = B_z(r)\boldsymbol{e}_z$。在管内作一边在轴线上、一边在半径 $r$ 处的矩形回路（与轴平行的边长 $l$），它不套连电流：$[B_z(0) - B_z(r)]l = 0$，管内是均匀场。在管外作类似的矩形回路，管外的场也均匀，又在无穷远处为零，所以管外 $B = 0$。
- 最后作一边在管内、一边在管外的矩形回路，套连电流 $nlI$：$B_{\mathrm{in}}l = \mu_0nlI$。

$$
\boldsymbol{B}_{\mathrm{in}} = \mu_0nI\boldsymbol{e}_z,\qquad \boldsymbol{B}_{\mathrm{out}} = \boldsymbol{0},
$$
$\boldsymbol{e}_z$ 与电流的流向成右手螺旋关系。这与例 6.3.4 中 $L \to \infty$ 的结果一致。截面不是圆形的密绕长直螺线管，结论相同。

**例 6.5.3（螺绕环的磁场）** 环形螺线管（螺绕环）共 $N$ 匝，通电流 $I$。求环内外的磁场。

**解** 由对称性，磁感线是与环共轴的圆。取半径为 $r$ 的同轴圆形回路：在环内，回路套连电流 $NI$，$2\pi rB = \mu_0NI$；在环外（$r$ 小于内半径或大于外半径），回路套连的电流代数和为零，$B = 0$。

$$
B_{\mathrm{in}} = \frac{\mu_0NI}{2\pi r} .
$$
环的截面很小时，$n = N/(2\pi r)$ 近似为常数，$B \approx \mu_0nI$，与无限长螺线管相同。

**例 6.5.4（无限大平面电流的磁场）** 无限大导体薄板中有均匀分布的电流，垂直于电流方向单位长度上的电流为 $K$（面**电流密度**，单位 $\mathrm{A\,m^{-1}}$）。求板外的磁场。

**解** 由对称性，板两侧的磁场大小相等、方向相反，都平行于板面且垂直于电流。作一个跨过板面的矩形回路，两条长 $l$ 的边平行于板面、分居两侧，套连电流 $Kl$：

$$
2Bl = \mu_0Kl,\qquad B = \frac{\mu_0K}{2},
$$
与到板的距离无关，是均匀场。这与无限大均匀带电平面的电场 $E = \sigma/(2\varepsilon_0)$ 相对应。

## 6.6. 与变化电场相联系的磁场

### 6.6.1. Ampère 环路定理的困难

Ampère 环路定理中的 $I_{\mathrm{enc}}$ 是穿过以 $L$ 为边界的曲面 $S$ 的电流。对恒定电流，$\nabla\cdot\boldsymbol{J} = 0$，穿过以同一 $L$ 为边界的任意两个曲面的电流相等，$I_{\mathrm{enc}}$ 有确定的意义。电流不恒定时就会出现矛盾。

考虑给**电容器**充电的电路。以导线外的一个圆形回路 $L$ 为边界，取两个曲面：平面 $S_1$ 与导线相交，曲面 $S_2$ 从电容器两极板之间穿过，不与导线相交。对 $S_1$，$\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0I$；对 $S_2$，没有传导电流穿过，$\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = 0$。同一个环量得到两个不同的结果。

### 6.6.2. 位移电流

1861–1862 年，Maxwell 注意到电容器充电时，极板上的电荷在变化，极板之间的电场也在变化。由**电流连续性方程**与 $\boldsymbol{D}$ 的**高斯定理**（[5.3.4](/5.3.4) 定理 4.3.1），对任意闭合曲面 $S$，

$$
\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = -\frac{\mathrm{d}q_{\mathrm{enc}}}{\mathrm{d}t},\qquad
\frac{\mathrm{d}q_{\mathrm{enc}}}{\mathrm{d}t} = \frac{\mathrm{d}}{\mathrm{d}t}\oint_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S} = \oint_S\frac{\partial\boldsymbol{D}}{\partial t}\cdot\mathrm{d}\boldsymbol{S},
$$
所以

$$
\oint_S\Big(\boldsymbol{J} + \frac{\partial\boldsymbol{D}}{\partial t}\Big)\cdot\mathrm{d}\boldsymbol{S} = 0 .
$$
在非恒定情形下，传导电流 $\boldsymbol{J}$ 不连续，但 $\boldsymbol{J} + \partial\boldsymbol{D}/\partial t$ 总是连续的：$S_1$ 与 $S_2$ 合成一个闭合曲面，穿过 $S_1$ 与 $S_2$ 的 $\boldsymbol{J} + \partial\boldsymbol{D}/\partial t$ 的通量相等。

**定义 6.6.1（位移电流）** 电位移通量 $\Phi_D = \int_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}$ 对时间的变化率

$$
I_{\mathrm{d}} = \frac{\mathrm{d}\Phi_D}{\mathrm{d}t} = \int_S\frac{\partial\boldsymbol{D}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}
$$
称为通过 $S$ 的**位移电流**，$\boldsymbol{J}_{\mathrm{d}} = \partial\boldsymbol{D}/\partial t$ 称为位移电流密度。传导电流与位移电流之和 $I = I_{\mathrm{c}} + I_{\mathrm{d}}$ 称为**全电流**。

真空中 $\boldsymbol{J}_{\mathrm{d}} = \varepsilon_0\partial\boldsymbol{E}/\partial t$，它不是电荷的运动，而是变化的电场；介质中 $\partial\boldsymbol{D}/\partial t = \varepsilon_0\partial\boldsymbol{E}/\partial t + \partial\boldsymbol{P}/\partial t$，后一项是**极化电荷**的运动（极化电流）。全电流总是连续的。Maxwell 假设：位移电流与传导电流一样激发磁场，其实质是变化的电场激发磁场。于是 Ampère 环路定理推广为：

**定理 6.6.1（全电流 Ampère 环路定理）**

$$
\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0(I_{\mathrm{c}} + I_{\mathrm{d}}) = \mu_0\int_S\Big(\boldsymbol{J} + \frac{\partial\boldsymbol{D}}{\partial t}\Big)\cdot\mathrm{d}\boldsymbol{S},\qquad
\nabla\times\boldsymbol{B} = \mu_0\Big(\boldsymbol{J} + \frac{\partial\boldsymbol{D}}{\partial t}\Big),
$$
其中 $\boldsymbol{J}$ 是自由电荷的传导电流密度，$\boldsymbol{B}$ 的源还包括介质的磁化电流（[5.3.8](/5.3.8)）。

对微分形式取散度，左边为零，右边 $\nabla\cdot\boldsymbol{J} + \partial(\nabla\cdot\boldsymbol{D})/\partial t = \nabla\cdot\boldsymbol{J} + \partial\rho_0/\partial t = 0$ 正是电流连续性方程：引入位移电流后，Ampère 环路定理与**电荷守恒**相容了。位移电流的假设由电磁波的存在（Hertz，1888 年）得到证实（[5.3.10](/5.3.10)）。

**例 6.6.1（导体中的位移电流）** 截面积为 $S$ 的导体中通以简谐电流 $I = I_0\cos\omega t$，电流在截面上均匀分布。求位移电流与传导电流的振幅之比。

**解** 由 **Ohm 定律**，导体中 $E = \rho J = \rho I/S$（$\rho$ 是**电阻率**），

$$
I_{\mathrm{d}} = \varepsilon_0\varepsilon_{\mathrm{r}}\frac{\mathrm{d}E}{\mathrm{d}t}S = \varepsilon_0\varepsilon_{\mathrm{r}}\rho\frac{\mathrm{d}I}{\mathrm{d}t} = \varepsilon_0\varepsilon_{\mathrm{r}}\rho\omega I_0\cos\Big(\omega t + \frac\pi2\Big),\qquad
\frac{I_{\mathrm{d},0}}{I_0} = \varepsilon_0\varepsilon_{\mathrm{r}}\rho\omega .
$$
对良导体，$\rho \sim 10^{-8}\,\Omega\,\mathrm{m}$，取 $\varepsilon_{\mathrm{r}} \approx 1$，比值约为 $9\times10^{-12}\times10^{-8}\times2\pi\nu \approx 6\times10^{-19}\nu/\mathrm{Hz}$：即使在 $\nu = 10^9\,\mathrm{Hz}$ 的微波频段也只有 $10^{-9}$ 量级，良导体中的位移电流完全可以忽略。对海水（$\rho \approx 0.2\,\Omega\,\mathrm{m}$，$\varepsilon_{\mathrm{r}} \approx 80$），两者在 $\nu \sim 10^9\,\mathrm{Hz}$ 时相当。在绝缘体与真空中则只有位移电流。

**例 6.6.2（平行板电容器充电时的磁场）** 极板半径为 $R$ 的圆形平行板电容器（板间为真空），以传导电流 $I_{\mathrm{c}}$ 充电。求极板之间距轴线 $r$ 处的磁场（忽略边缘效应）。

**解** 板间的场强 $E = \dfrac{q}{\varepsilon_0\pi R^2}$，$\dfrac{\mathrm{d}E}{\mathrm{d}t} = \dfrac{I_{\mathrm{c}}}{\varepsilon_0\pi R^2}$，位移电流在板间均匀分布，总量等于 $I_{\mathrm{c}}$。由轴对称，磁感线是与轴线同心的圆。取半径为 $r$ 的同轴圆形回路：

$$
2\pi rB = \mu_0\varepsilon_0\frac{\mathrm{d}}{\mathrm{d}t}\int_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} =
\begin{cases}\mu_0I_{\mathrm{c}}\dfrac{r^2}{R^2}, & r < R,\\[2ex] \mu_0I_{\mathrm{c}}, & r > R,\end{cases}
\qquad
B = \begin{cases}\dfrac{\mu_0I_{\mathrm{c}}r}{2\pi R^2}, & r < R,\\[2ex] \dfrac{\mu_0I_{\mathrm{c}}}{2\pi r}, & r > R .\end{cases}
$$
板间的磁场与电流 $I_{\mathrm{c}}$ 均匀流过半径为 $R$ 的圆柱导体时（例 6.5.1）完全相同：位移电流在产生磁场这一点上与传导电流等效。

## 小结

| 规律 | 积分形式 | 微分形式 |
|---|---|---|
| Lorentz 力 | $\boldsymbol{F} = q\boldsymbol{v}\times\boldsymbol{B}$ | |
| Biot–Savart 定律 | $\mathrm{d}\boldsymbol{B} = \dfrac{\mu_0}{4\pi}\dfrac{I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{e}_r}{r^2}$ | |
| 磁通连续定理 | $\oint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = 0$ | $\nabla\cdot\boldsymbol{B} = 0$ |
| Ampère 环路定理（恒定电流） | $\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0I_{\mathrm{enc}}$ | $\nabla\times\boldsymbol{B} = \mu_0\boldsymbol{J}$ |
| 全电流 Ampère 环路定理 | $\oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l} = \mu_0(I_{\mathrm{c}} + I_{\mathrm{d}})$ | $\nabla\times\boldsymbol{B} = \mu_0(\boldsymbol{J} + \partial_t\boldsymbol{D})$ |

| 电流分布 | 磁感应强度 |
|---|---|
| 直导线段 | $\dfrac{\mu_0I}{4\pi r_0}(\cos\theta_1 - \cos\theta_2)$；无限长 $\dfrac{\mu_0I}{2\pi r_0}$ |
| 圆电流轴线 | $\dfrac{\mu_0IR^2}{2(R^2 + x^2)^{3/2}}$；圆心 $\dfrac{\mu_0I}{2R}$ |
| 螺线管轴线 | $\dfrac{\mu_0nI}{2}(\cos\beta_2 - \cos\beta_1)$；无限长管内 $\mu_0nI$，管外 $0$ |
| 螺绕环 | 环内 $\dfrac{\mu_0NI}{2\pi r}$，环外 $0$ |
| 无限大平面电流 | $\dfrac{\mu_0K}{2}$ |
| 运动点电荷 | $\dfrac{\mu_0}{4\pi}\dfrac{q\boldsymbol{v}\times\boldsymbol{e}_r}{r^2} = \dfrac{\boldsymbol{v}\times\boldsymbol{E}}{c^2}$ |

## 思考题

1. 作一个只包围磁铁棒一个磁极的闭合曲面，通过它的磁通量是多少？
   提示：零。磁感线是闭合曲线，在磁铁内部由 S 极指向 N 极，穿出曲面的磁感线与穿入的一样多；这正是磁通连续定理，也说明不存在孤立的磁极。
2. 在没有电流的空间中，若磁感线是平行直线，磁场是否一定均匀？
   提示：是。设磁感线沿 $z$ 方向，由 $\nabla\cdot\boldsymbol{B} = 0$ 得 $\partial B_z/\partial z = 0$，即 $B$ 沿磁感线不变；由 $\nabla\times\boldsymbol{B} = \boldsymbol{0}$ 得 $\partial B_z/\partial x = \partial B_z/\partial y = 0$，即 $B$ 在垂直方向也不变（也可以用一个矩形回路的环量说明）。
3. 磁极间的磁场能否在磁极边缘处突然降为零？
   提示：不能。作一个矩形回路，一条边在磁极间平行于磁场，另一条边在外面磁场为零处，回路不套连电流，但环量不为零，与 Ampère 环路定理矛盾。边缘必有逐渐减弱的边缘场，与平行板电容器的边缘场类似（[5.3.4](/5.3.4)）。
4. 为什么 Ampère 环路定理对非恒定电流不成立？
   提示：非恒定时 $\nabla\cdot\boldsymbol{J} \ne 0$，穿过以同一回路为边界的不同曲面的传导电流不同，"回路所包围的电流"没有确定的意义；数学上，$\nabla\times\boldsymbol{B} = \mu_0\boldsymbol{J}$ 两边取散度会得到 $\nabla\cdot\boldsymbol{J} = 0$，与电荷守恒矛盾。加上位移电流后矛盾消除。
