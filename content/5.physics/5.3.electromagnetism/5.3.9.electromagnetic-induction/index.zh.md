---
title: 电磁感应
description: Faraday 电磁感应定律与 Lenz 定律，磁链与感应电量；动生电动势与 Lorentz 力；感生电场、涡流、电子感应加速器与趋肤效应；互感、自感与 RL 电路；磁场能量与能量密度；超导电性与 Meissner 效应。
---

Oersted 发现电流产生磁场以后，人们自然地追问它的逆效应：磁场能否产生电流？Faraday 经过近十年的探索，于 1831 年发现了电磁感应：恒定的磁场不产生电流，变化的磁通才产生。电磁感应把电场和磁场真正联系在一起，是发电机、变压器、电感器与无线充电的原理。本章先给出 Faraday 定律与判断方向的 Lenz 定律，然后分析感应**电动势**的两种机理：**导体**在磁场中运动时，**非静电力**是 **Lorentz 力**（动生电动势，[5.3.7](/5.3.7)）；导体静止而磁场变化时，非静电力来自变化的磁场在空间激发的感生电场。后者是 Maxwell 方程组的第一条（[5.3.10](/5.3.10)）。接着讨论回路自身与回路之间的感应（自感与互感），由自感导出磁场的能量；RL 电路与 LC 电路分别对应一阶与二阶常系数线性微分方程（[2.4](/2.4)）。最后简介超导电性，§9.7 是选讲内容。

## 9.1. Faraday 电磁感应定律

### 9.1.1. 电磁感应现象

Faraday 的实验可以归纳为三类：条形磁铁插入或拔出线圈时，线圈中产生电流，磁铁相对线圈静止时没有电流；用通电线圈代替磁铁，两线圈有相对运动时，或者两线圈相对静止而改变其中一个的电流时，另一个线圈中有电流；把闭合回路放在恒定磁场中，导体棒沿导轨滑动时，回路中有电流。Faraday 把产生感应电流的情况归纳为五种：运动的磁铁、运动的**恒定电流**、变化的磁场、变化的电流、磁场中运动的导体。它们的共同点是：穿过闭合回路的**磁通量**发生了变化。

穿过闭合导体回路的磁通量发生变化时，不论这种变化是什么原因引起的，回路中都会产生电流，这一现象称为电磁感应（electromagnetic induction）。回路中的电流称为感应电流，驱动它的电动势称为感应电动势。感应电动势比感应电流更基本：回路断开时没有感应电流，但感应电动势照样存在；感应电流由感应电动势和回路的**电阻**决定，方向与感应电动势一致。

### 9.1.2. Faraday 电磁感应定律

**定理 9.1.1（Faraday 电磁感应定律）** 回路中感应电动势的大小与穿过回路的磁通量的变化率成正比：

$$
\mathcal{E}=-\frac{\mathrm{d}\Phi}{\mathrm{d}t}.
$$
其中电动势的正方向取回路 $L$ 的绕行方向，磁通量 $\Phi=\iint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}$ 中曲面 $S$ 的法向与 $L$ 的绕行方向成右手螺旋关系。

在 SI 中比例系数为 1：磁通量的单位韦伯 $\mathrm{Wb}=\mathrm{V\,s}$ 正是由此定义的。按上述约定，$\mathcal{E}>0$ 表示感应电动势沿 $L$ 的绕行方向，$\mathcal{E}<0$ 则相反。式中的负号表示感应电动势的方向，它的物理意义由 Lenz 定律给出。

### 9.1.3. Lenz 定律

**定理 9.1.2（Lenz 定律）** 闭合回路中感应电流的方向，总是使它所激发的磁场阻碍引起感应电流的磁通量的变化。

Lenz 定律（Lenz's law，1834 年）的更一般的说法是：感应电流的效果总是反抗引起感应电流的原因。磁铁靠近线圈时，线圈中的感应电流使线圈与磁铁相斥，阻碍它们靠近；磁铁离开时，感应电流使两者相吸，阻碍它们分离。它是能量守恒在电磁感应中的表现：如果感应电流的方向相反，磁铁一旦开始靠近就会被加速，感应电流和动能同时无限增大，构成**第一类永动机**。

**例 9.1.1（滑杆中的能量转化）** 长为 $l$ 的导体杆在匀强磁场 $B$ 中沿两条平行导轨以速度 $v$ 匀速滑动，杆与导轨垂直，磁场垂直于导轨平面，回路的电阻为 $R$。回路面积每秒增加 $lv$，感应电动势的大小为 $\mathcal{E}=Blv$，电流 $I=Blv/R$。杆受的 **Ampère 力**大小为 $F=IlB=B^2l^2v/R$，方向与速度相反（Lenz 定律）。要维持匀速运动，外力必须做功，功率

$$
Fv=\frac{B^2l^2v^2}{R}=I^2R,
$$
恰好等于回路中的 Joule 热功率：外力做的机械功经由电磁感应全部转化为电能，再变为热。

### 9.1.4. 磁链与感应电量

$N$ 匝线圈串联时，总电动势是各匝电动势之和：

$$
\mathcal{E}=-\sum_i\frac{\mathrm{d}\Phi_i}{\mathrm{d}t}=-\frac{\mathrm{d}\Psi}{\mathrm{d}t},\qquad \Psi=\sum_i\Phi_i,
$$
$\Psi$ 称为磁链（magnetic flux linkage），即穿过各匝的磁通之和。若穿过每一匝的磁通相同，$\Psi=N\Phi$。

电阻为 $R$ 的回路中，感应电流为 $I=\mathcal{E}/R=-\frac1R\frac{\mathrm{d}\Psi}{\mathrm{d}t}$。在 $t_1$ 到 $t_2$ 时间内通过回路截面的电荷量为

$$
q=\int_{t_1}^{t_2}I\,\mathrm{d}t=-\frac1R\int_{\Psi_1}^{\Psi_2}\mathrm{d}\Psi=\frac{\Psi_1-\Psi_2}{R},
$$
只取决于磁链的变化，与变化的快慢无关。测出通过的电荷量就能求出磁链的变化，这是磁通计（冲击电流计）的原理，[5.3.8](/5.3.8) 中测量**铁磁质**的磁化曲线就用这种方法。

感应电动势的产生有两种情况：一是回路或其一部分在恒定磁场中运动，二是回路不动而磁场随时间变化（场源运动或电流变化）。前者产生的称为动生电动势，后者称为感生电动势。按照电动势的定义（[5.3.5](/5.3.5)），两者都必须有非静电力，下面两节分别找出它们。

## 9.2. 动生电动势

导体在恒定磁场中运动时产生的感应电动势称为动生电动势（motional electromotive force）。设回路 $L$ 以速度 $\boldsymbol{v}$ 运动（各部分速度可以不同），线元 $\mathrm{d}\boldsymbol{l}$ 在 $\mathrm{d}t$ 内扫过的矢量面元为 $(\boldsymbol{v}\,\mathrm{d}t)\times\mathrm{d}\boldsymbol{l}$。由于**磁通连续定理**，回路磁通的增量等于它扫过的侧面上的磁通：

$$
\mathrm{d}\Phi=\oint_L\boldsymbol{B}\cdot\big[(\boldsymbol{v}\,\mathrm{d}t)\times\mathrm{d}\boldsymbol{l}\big],\qquad \mathcal{E}_{\mathrm{mot}}=-\frac{\mathrm{d}\Phi}{\mathrm{d}t}=-\oint_L\boldsymbol{B}\cdot(\boldsymbol{v}\times\mathrm{d}\boldsymbol{l})=\oint_L(\boldsymbol{v}\times\boldsymbol{B})\cdot\mathrm{d}\boldsymbol{l},
$$
最后一步用了混合积的轮换性质。

**公式 9.2.1（动生电动势）** 导线 $ab$ 在恒定磁场中运动时产生的动生电动势为

$$
\mathcal{E}_{\mathrm{mot}}=\int_a^b(\boldsymbol{v}\times\boldsymbol{B})\cdot\mathrm{d}\boldsymbol{l}.
$$
积分为正时电动势由 $a$ 指向 $b$（$b$ 端**电势**高），为负时由 $b$ 指向 $a$。

公式本身给出了非静电力：导体中的载流子随导体以 $\boldsymbol{v}$ 运动，受 Lorentz 力 $q\boldsymbol{v}\times\boldsymbol{B}$，相当于一个非静电场 $\boldsymbol{E}_{\mathrm{K}}=\boldsymbol{v}\times\boldsymbol{B}$，电动势就是它沿导线的线积分。若 $\boldsymbol{B}$ 与 $\boldsymbol{v}$ 都是常矢量，$\mathcal{E}_{\mathrm{mot}}=(\boldsymbol{v}\times\boldsymbol{B})\cdot\overrightarrow{ab}$，与导线的形状无关。

**注 9.2.1（Lorentz 力不做功，为什么能产生电动势）** 设载流子除了随导线以 $\boldsymbol{v}$ 运动外，还以速度 $\boldsymbol{u}$ 沿导线运动（这就是电流）。它受的总 Lorentz 力为 $\boldsymbol{F}=q(\boldsymbol{v}+\boldsymbol{u})\times\boldsymbol{B}$，垂直于合速度 $\boldsymbol{v}+\boldsymbol{u}$，总功率为零：

$$
\boldsymbol{F}\cdot(\boldsymbol{v}+\boldsymbol{u})=0\quad\Longrightarrow\quad q(\boldsymbol{v}\times\boldsymbol{B})\cdot\boldsymbol{u}=-q(\boldsymbol{u}\times\boldsymbol{B})\cdot\boldsymbol{v}.
$$
左边是分力 $q\boldsymbol{v}\times\boldsymbol{B}$ 推动载流子沿导线运动的功率，即电动势对电流做功的功率；右边是另一个分力 $q\boldsymbol{u}\times\boldsymbol{B}$（宏观上就是导线受的 **Ampère 力**）做的负功，必须由外力克服。所以 Lorentz 力本身不做功，它只是把外力做的机械功转化为电能的"桥梁"，与例 9.1.1 的能量分析一致。

**例 9.2.1（转动金属杆中的电动势）** 长为 $L$ 的金属杆 $OA$ 在垂直于杆的匀强磁场 $\boldsymbol{B}$ 中绕 $O$ 端以角速度 $\boldsymbol{\omega}$ 转动，$\boldsymbol{\omega}$ 平行于 $\boldsymbol{B}$。求杆中的电动势。

**解** 距 $O$ 为 $l$ 处的速度 $v=\omega l$，$\boldsymbol{v}\times\boldsymbol{B}$ 沿杆由 $O$ 指向 $A$（$\boldsymbol{v}=\boldsymbol{\omega}\times\boldsymbol{l}$，$(\boldsymbol{\omega}\times\boldsymbol{l})\times\boldsymbol{B}=\omega B\,\boldsymbol{l}$），大小为 $\omega lB$。于是

$$
\mathcal{E}_{OA}=\int_0^L\omega Bl\,\mathrm{d}l=\frac12B\omega L^2,
$$
电动势由 $O$ 指向 $A$，正电荷向 $A$ 端积累，$A$ 端电势高。若 $\boldsymbol{\omega}$ 与 $\boldsymbol{B}$ 反向，则 $O$ 端电势高。把杆换成金属圆盘，在轴与盘边之间就得到恒定的电动势 $\frac12B\omega R^2$，这就是 Faraday 圆盘发电机（单极发电机）。

## 9.3. 感生电动势和感生电场

### 9.3.1. 感生电场

回路固定不动、磁场随时间变化时产生的感应电动势称为感生电动势（induced electromotive force）。按 Faraday 定律，

$$
\mathcal{E}_{\mathrm{ind}}=-\frac{\mathrm{d}\Phi}{\mathrm{d}t}=-\frac{\mathrm{d}}{\mathrm{d}t}\iint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}.
$$
导体静止，载流子不受 Lorentz 力；能驱动静止电荷的只能是电场，而它的环量不为零，不是静电场。实验还表明，感生电动势与回路的材料无关。Maxwell 由此提出：变化的磁场在其周围空间激发一种电场，不论那里有没有导体；导体回路只是显示了它的存在。这种电场称为感生电场（induced electric field），记为 $\boldsymbol{E}_{\mathrm{ind}}$。

**定理 9.3.1（感生电场的环路定理）** 感生电场沿任一闭合回路的环量等于穿过以该回路为边界的曲面的磁通量变化率的负值：

$$
\oint_L\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{l}=-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S},\qquad\text{微分形式}\quad\nabla\times\boldsymbol{E}_{\mathrm{ind}}=-\frac{\partial\boldsymbol{B}}{\partial t},
$$
曲面 $S$ 的法向与回路 $L$ 成右手螺旋关系。感生电场不是由电荷产生的，它对任一闭合曲面的通量为零：$\oiint_S\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{S}=0$。

微分形式由 **Stokes 公式**得到。感生电场的**电场线**是与**磁感线**相套连的闭合曲线，所以感生电场也称涡旋电场。它与静电场的对比：

| | 静电场 | 感生电场 |
|---|---|---|
| 场源 | 静止电荷 | 变化的磁场 |
| 通量 | $\oiint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=q/\varepsilon_0$，有源 | $\oiint\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{S}=0$，**无源场** |
| 环量 | $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=0$，**保守场** | $\oint\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{l}=-\frac{\mathrm{d}\Phi}{\mathrm{d}t}$，有旋、非保守 |
| 电场线 | 起于正电荷，止于负电荷 | 闭合曲线 |
| 电势 | 可以定义 | 不能定义 |
| 对电荷的作用 | $q\boldsymbol{E}$ | $q\boldsymbol{E}_{\mathrm{ind}}$ |

一般情况下空间同时有两种电场，总电场 $\boldsymbol{E}=\boldsymbol{E}_{\mathrm{s}}+\boldsymbol{E}_{\mathrm{ind}}$ 满足 $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=-\iint\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}$，这就是 Maxwell 方程组中的电磁感应定律。

**例 9.3.1（长直螺线管内外的感生电场）** 无限长直螺线管的半径为 $R$，单位长度 $n$ 匝，电流 $I=\alpha t$（$\alpha$ 为常量），求管内外的感生电场。

**解** 管内 $\boldsymbol{B}=\mu_0nI\boldsymbol{e}_z$，管外 $\boldsymbol{B}=\boldsymbol{0}$，所以 $\frac{\partial\boldsymbol{B}}{\partial t}=\mu_0n\alpha\boldsymbol{e}_z$（$r<R$），管外为零。先由对称性确定 $\boldsymbol{E}_{\mathrm{ind}}$ 的方向。由轴对称和沿轴的平移对称，$\boldsymbol{E}_{\mathrm{ind}}=E_r(r)\boldsymbol{e}_r+E_\varphi(r)\boldsymbol{e}_\varphi+E_z(r)\boldsymbol{e}_z$。任一垂直于轴线的平面都是系统的镜面（电流沿圆周，镜像后不变），$\boldsymbol{E}_{\mathrm{ind}}$ 是**极矢量**，在镜面上不能有垂直于镜面的分量，所以 $E_z=0$。取与螺线管同轴的封闭圆柱面，由 $\oiint\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{S}=0$ 得 $E_r\cdot2\pi rl=0$，所以 $E_r=0$。于是 $\boldsymbol{E}_{\mathrm{ind}}=E_\varphi(r)\boldsymbol{e}_\varphi$。

取半径为 $r$ 的同轴圆周为回路，沿 $\boldsymbol{e}_\varphi$ 绕行，左边为 $E_\varphi\cdot2\pi r$；右边

$$
-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}=\begin{cases}-\mu_0n\alpha\,\pi r^2,&r<R,\\-\mu_0n\alpha\,\pi R^2,&r>R,\end{cases}
\qquad\text{所以}\qquad
E_\varphi=\begin{cases}-\dfrac12\mu_0n\alpha\,r,&r<R,\\[2mm]-\dfrac{\mu_0n\alpha R^2}{2r},&r>R.\end{cases}
$$
负号表示感生电场的绕向与电流的绕向相反（Lenz 定律）。管内**场强**与 $r$ 成正比，管外与 $r$ 成反比：螺线管外虽然没有磁场，却有感生电场。用一般的 $\frac{\mathrm{d}B}{\mathrm{d}t}$ 表示，$E=\frac r2\frac{\mathrm{d}B}{\mathrm{d}t}$（$r<R$），$E=\frac{R^2}{2r}\frac{\mathrm{d}B}{\mathrm{d}t}$（$r>R$）。

![左：磁场垂直纸面向里并均匀增强时的感生电场线，是与螺线管同心的圆（蓝色区域为螺线管截面）；右：感生电场的大小随到轴线距离的变化，管内正比于 $r$，管外反比于 $r$](./plots/solenoid-induced-field.py)

### 9.3.2. 涡流

大块导体处在变化的磁场中时，感生电场在导体内部驱动闭合的感应电流，称为涡流（eddy current）。大块导体的电阻很小，涡流可以很大。

- 热效应：在圆柱形导体中，若磁场沿轴线均匀变化，半径 $r$ 处的感生电场 $E\propto r$，单位体积的热功率 $\sigma E^2\propto r^2$，越靠外层发热越多，加上 §9.3.4 的趋肤效应，表面的加热更为集中，这正适合金属零件的表面淬火。高频感应炉用涡流在坩埚内熔炼金属，无需与炉料接触，便于在真空中冶炼。电磁炉用交变磁场在锅底产生涡流加热。
- 电**磁阻**尼：导体在磁场中运动时，涡流受的 Ampère 力阻碍运动（Lenz 定律），可用于电表指针的阻尼和列车的涡流制动。
- 减小涡流：变压器和电机的铁芯用彼此绝缘的硅钢片叠成，硅钢片平行于磁场方向，割断了垂直于磁场的涡流通路，又因硅钢的**电阻率**较大，涡流损耗大大减小。

### 9.3.3. 电子感应加速器

电子感应加速器（betatron）用感生电场加速电子。在电磁铁两极之间放一个环形真空室，电磁铁通以交变电流，变化的磁场一方面在环形轨道上产生感生电场加速电子，另一方面使电子在半径为 $R$ 的轨道上做圆周运动。保持轨道半径不变需要什么条件？电子的动量 $p$ 与轨道处的磁场 $B_R$ 满足 $p=eB_RR$（相对论情形也成立）。感生电场沿轨道的大小为 $E=\frac{1}{2\pi R}\frac{\mathrm{d}\Phi}{\mathrm{d}t}$，$\Phi=\pi R^2\bar B$，$\bar B$ 是轨道所围面积上的平均**磁感应强度**，于是

$$
\frac{\mathrm{d}p}{\mathrm{d}t}=eE=\frac{eR}{2}\frac{\mathrm{d}\bar B}{\mathrm{d}t}=eR\frac{\mathrm{d}B_R}{\mathrm{d}t}\qquad\Longrightarrow\qquad B_R=\frac12\bar B,
$$
即轨道处的磁场应为轨道内平均磁场的一半（"二比一条件"），靠极面的形状实现。电子只在交变磁场增强的四分之一周期中被加速，结束时被引出。第一台电子感应加速器由 Kerst 于 1940 年建成，能量为 $2.3\,\mathrm{MeV}$，此后的最大型号（1950 年）达到约 $300\,\mathrm{MeV}$。更高能量的电子加速器改用同步加速器：1947 年通用电气公司的 $70\,\mathrm{MeV}$ 电子同步加速器上首次观察到同步辐射（[5.3.10](/5.3.10)）。

### 9.3.4. 趋肤效应

直流电流在导线截面上均匀分布，高频交变电流却集中在导线的表面附近，越靠近表面**电流密度**越大，这称为趋肤效应（skin effect）。定性地看，交变电流在导线内产生交变磁场，后者产生的感生电场在导线中心附近与电流反向、在表面附近与电流同向，于是中心的电流被削弱、表面的电流被加强；频率越高，感生电场越强，效应越显著。

定量处理要用 Maxwell 方程组：在良导体中忽略**位移电流**，由 $\nabla\times\boldsymbol{H}=\sigma\boldsymbol{E}$ 与 $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$ 消去 $\boldsymbol{E}$，得到 $\Delta\boldsymbol{B}=\mu\sigma\,\partial\boldsymbol{B}/\partial t$，这是与热传导方程（[2.5.7](/2.5.7)）同型的扩散方程。对频率为 $\omega$ 的交变场，在平表面附近求解，电流密度的幅值随深度 $d$ 按指数衰减：

$$
J(d)=J_0\,\mathrm{e}^{-d/\delta},\qquad \delta=\sqrt{\frac{2}{\omega\mu\sigma}}=\frac{1}{\sqrt{\pi f\mu\sigma}},
$$
$\delta$ 称为趋肤深度。对铜（$\sigma=5.96\times10^7\,\mathrm{S/m}$），$50\,\mathrm{Hz}$ 时 $\delta\approx9.2\,\mathrm{mm}$，$1\,\mathrm{MHz}$ 时约 $66\,\mu\mathrm{m}$，$1\,\mathrm{GHz}$ 时约 $2\,\mu\mathrm{m}$。因此高频电路用多股绝缘细线绞合的导线或空心铜管，微波器件只需在表面镀银。

### 9.3.5. 动生与感生的相对性

动生与感生的区分与参考系有关。磁铁不动、线圈运动时，在磁铁的参考系中，线圈里的电荷受 Lorentz 力 $q\boldsymbol{v}\times\boldsymbol{B}$，是动生电动势；在线圈的参考系中，电荷静止，磁铁运动使空间的磁场变化，电荷受感生电场的力，是感生电动势。两种描述给出相同的电动势，这正是电场与磁场随参考系变换（[5.3.7](/5.3.7#sec-7.2)）的结果。Einstein 1905 年的狭义相对论论文《论动体的电动力学》就以这个例子开篇：Maxwell 理论对两种情形的解释不对称，而可观测的现象只取决于相对运动。

## 9.4. 互感

### 9.4.1. 互感系数

两个相邻的线圈 1、2，线圈 1 中的电流 $i_1$ 产生的磁场穿过线圈 2，在线圈 2 中形成磁链 $\Psi_{21}$。按 **Biot–Savart 定律**，磁场与电流成正比，所以 $\Psi_{21}$ 与 $i_1$ 成正比：

$$
\Psi_{21}=M_{21}i_1,\qquad \Psi_{12}=M_{12}i_2.
$$
可以证明（§9.6），$M_{12}=M_{21}=M$，称为两线圈的互感系数，简称互感（mutual inductance）。它由两线圈的大小、形状、匝数、相对位置和周围的介质决定，只要线圈附近没有铁磁质，它与电流无关。互感的 SI 单位是亨利，$1\,\mathrm{H}=1\,\mathrm{Wb/A}$。

当 $i_1$ 变化时，线圈 2 中产生互感电动势，反之亦然：

$$
\mathcal{E}_{21}=-M\frac{\mathrm{d}i_1}{\mathrm{d}t},\qquad \mathcal{E}_{12}=-M\frac{\mathrm{d}i_2}{\mathrm{d}t},
$$
这里约定每个线圈中电动势的正方向与另一线圈中电流的正方向都按右手螺旋关系确定磁通的正方向。

计算 $M$ 时，可以任选方便的一边：设 $i_1$ 求 $\Psi_{21}$，或设 $i_2$ 求 $\Psi_{12}$，两者结果相同。

**例 9.4.1（同轴长直螺线管的互感）** 长为 $l$、截面积为 $S$ 的长直螺线管 1 上，紧密地套绕另一个同长的线圈 2，单位长度的匝数分别为 $n_1$、$n_2$。设线圈 1 通电流 $i_1$，管内 $B_1=\mu_0n_1i_1$，穿过线圈 2 每匝的磁通为 $B_1S$，$\Psi_{21}=n_2l\cdot\mu_0n_1i_1S$，所以

$$
M=\mu_0n_1n_2lS=\mu_0n_1n_2V.
$$
而两个线圈各自的自感（§9.5）为 $L_1=\mu_0n_1^2V$、$L_2=\mu_0n_2^2V$，所以 $M=\sqrt{L_1L_2}$。一般地 $M=k\sqrt{L_1L_2}$，$0\le k\le1$ 称为耦合系数，$k=1$ 表示一个线圈的磁通全部穿过另一个线圈（无漏磁）。

变压器、互感器和无线充电都利用互感：理想变压器中两线圈绕在同一个闭合铁芯上，每匝的磁通相同，两边的电压之比等于匝数之比。

## 9.5. 自感

### 9.5.1. 自感系数

回路中的电流变化时，它自身产生的磁场穿过自身的磁链也随之变化，回路中产生感应电动势，这称为自感，相应的电动势称为自感电动势。若线圈的形状、尺寸不变，附近没有铁磁质，磁链与电流成正比：

$$
\Psi=Li,\qquad \mathcal{E}_L=-L\frac{\mathrm{d}i}{\mathrm{d}t},
$$
$L$ 称为回路的自感系数，简称自感或电感（self-inductance），单位也是亨利。这里磁链的正方向与电流的正方向成右手螺旋关系，保证 $L>0$；$\mathcal{E}_L$ 的正方向取电流的正方向。负号表示自感电动势总是阻碍回路自身电流的变化。

**例 9.5.1（长直螺线管的自感）** 长 $l$、截面积 $S$、单位长度 $n$ 匝的长直螺线管，充满**磁导率**为 $\mu$ 的线性介质。$B=\mu ni$，$\Psi=nl\cdot BS=\mu n^2lSi$，所以

$$
L=\mu n^2V,\qquad V=lS.
$$
自感与管的体积和匝数密度的平方成正比；插入铁芯可以使自感增大上千倍。

### 9.5.2. RL 电路

由于 $\mathcal{E}_L=-L\,\mathrm{d}i/\mathrm{d}t$，若电流突变，自感电动势将为无穷大，所以电感中的电流不能突变（对比：**电容器**两端的电压不能突变）。对交流电，频率越高，电流变化越快，自感电动势越大，所以电感"通直流、阻交流"，电容器则"通交流、隔直流"。

**例 9.5.2（RL 电路的暂态过程）** 电动势为 $\mathcal{E}$ 的**电源**（内阻不计）、电阻 $R$ 与自感 $L$ 串联，$t=0$ 时接通开关。由 **Kirchhoff 第二定律**，

$$
\mathcal{E}-L\frac{\mathrm{d}i}{\mathrm{d}t}=Ri.
$$
这是常系数一阶**线性微分方程**（[2.4.3](/2.4.3#sec-3.2)），初始条件 $i(0)=0$，解为

$$
i=\frac{\mathcal{E}}{R}\big(1-\mathrm{e}^{-t/\tau}\big),\qquad\tau=\frac LR.
$$
电流从零逐渐增大到稳定值 $\mathcal{E}/R$，$\tau$ 称为 RL 电路的**时间常量**：经过 $\tau$，电流达到稳定值的 $1-\mathrm{e}^{-1}\approx63\%$，经过 $5\tau$ 达到 99% 以上。电流稳定后，若在撤去电源的同时把 $L$ 与 $R$ 接成回路，由 $L\frac{\mathrm{d}i}{\mathrm{d}t}+Ri=0$，电流按 $i=\frac{\mathcal{E}}{R}\mathrm{e}^{-t/\tau}$ 衰减，并不立即消失。

![左：RL 电路接通电源后电流的增长与撤去电源后电流的衰减，时间以 $\tau=L/R$ 为单位；右：串联 RLC 电路中电容器初始带电 $q_0$ 时电荷的变化，三条曲线分别对应欠阻尼、临界阻尼与过阻尼](./plots/rl-rlc-circuits.py)

一个常见的演示：灯泡 $D_1$ 与电感线圈 $L$（直流电阻很小）并联后接到电源上，稳定时线圈中的电流 $I_L$ 大于灯泡中的电流 $I_R$。断开电源的瞬间，线圈中的电流不能突变，只能经由灯泡形成回路，灯泡中的电流由 $I_R$ 突然增大为 $I_L$ 再逐渐衰减，所以灯泡先闪亮一下再熄灭。闪亮的能量来自线圈中储存的磁场能量（§9.6）。

**注 9.5.1（LC 振荡电路）** 把充电到 $q_0$ 的电容器 $C$ 与电感 $L$ 接成回路，由 $L\frac{\mathrm{d}i}{\mathrm{d}t}+\frac qC=0$ 和 $i=\frac{\mathrm{d}q}{\mathrm{d}t}$，

$$
\frac{\mathrm{d}^2q}{\mathrm{d}t^2}+\frac{1}{LC}q=0,
$$
与弹簧振子的方程完全相同：电荷做**简谐振动**，**角频率** $\omega_0=1/\sqrt{LC}$，电场能量与磁场能量周期性地相互转换，对应于振子的势能与动能（[5.1.6](/5.1.6)）。回路中串联电阻 $R$ 时，方程变为 $L\ddot q+R\dot q+q/C=0$，这是常系数二阶线性方程（[2.4.9](/2.4.9#sec-9.4)），$R$ 起阻尼的作用：$R<2\sqrt{L/C}$ 时为**阻尼振动**，$R=2\sqrt{L/C}$ 时为临界阻尼，$R>2\sqrt{L/C}$ 时为过阻尼；**品质因数** $Q=\frac1R\sqrt{L/C}$。加上交变电源就是**受迫振动**，串联谐振正是收音机选台的原理。LC 回路是产生电磁振荡的基本电路，把它"打开"就成为发射电磁波的天线（[5.3.10](/5.3.10)）。

## 9.6. 磁场的能量

### 9.6.1. 自感磁能

在上面的演示中，断开电源后灯泡仍能闪亮，说明通电的线圈中储存着能量。接通电源后电流由 $0$ 增大到 $I$ 的过程中，电源要克服自感电动势做功，在 $\mathrm{d}t$ 内做功 $-\mathcal{E}_Li\,\mathrm{d}t=Li\,\mathrm{d}i$，总功为

$$
W_{\mathrm{m}}=\int_0^ILi\,\mathrm{d}i=\frac12LI^2.
$$
这部分功转化为线圈的磁能，电流消失时又通过自感电动势全部释放出来。它与电容器的电能 $\frac12CU^2$ 相对应。

### 9.6.2. 磁场能量密度

对长直螺线管，$B=\mu nI$，$L=\mu n^2V$，所以

$$
W_{\mathrm{m}}=\frac12\mu n^2VI^2=\frac{B^2}{2\mu}V.
$$
磁场均匀地分布在体积 $V$ 内，能量也应均匀地分布在磁场所在的空间中。这启发我们把能量看作储存在磁场之中。

**公式 9.6.1（磁场能量密度）** 在线性**磁介质**（非铁磁质）中，磁场的能量密度为

$$
w_{\mathrm{m}}=\frac{B^2}{2\mu}=\frac12BH=\frac12\boldsymbol{B}\cdot\boldsymbol{H},
$$
体积 $V$ 内的磁场能量为 $W_{\mathrm{m}}=\iiint_V\frac12\boldsymbol{B}\cdot\boldsymbol{H}\,\mathrm{d}V$。

这一结果对一般的线性介质和非均匀磁场都成立，与**电场能量密度** $\frac12\boldsymbol{E}\cdot\boldsymbol{D}$（[5.3.4](/5.3.4)）相对应。对铁磁质，把 $H$ 由 $0$ 增大时外界对单位体积做的功为 $\int H\,\mathrm{d}B$，它与过程有关，这就是 [5.3.8](/5.3.8) 中的磁滞损耗。从能量的角度看，电感中电流不能突变，是因为磁场能量不能突变，否则功率为无穷大。反过来，任何电流系统都有确定的磁场能量，也可以由能量计算自感：

$$
L=\frac{2W_{\mathrm{m}}}{I^2}.
$$

**例 9.6.1（同轴电缆的自感）** 同轴电缆由半径为 $R_1$ 的实心圆柱导体与半径为 $R_2$ 的薄圆筒组成，电流 $I$ 均匀地沿内导体流去、沿外筒流回，介质与导体的 $\mu_{\mathrm{r}}=1$。求单位长度的自感。

**解** 由 **Ampère 环路定理**，内导体中（$r<R_1$）$H=\frac{Ir}{2\pi R_1^2}$，两导体之间 $H=\frac{I}{2\pi r}$，外筒以外 $H=0$。单位长度的磁场能量为

$$
\frac{W_{\mathrm{m}}}{l}=\int_0^{R_1}\frac{\mu_0}{2}\Big(\frac{Ir}{2\pi R_1^2}\Big)^2 2\pi r\,\mathrm{d}r+\int_{R_1}^{R_2}\frac{\mu_0}{2}\Big(\frac{I}{2\pi r}\Big)^2 2\pi r\,\mathrm{d}r=\frac{\mu_0I^2}{16\pi}+\frac{\mu_0I^2}{4\pi}\ln\frac{R_2}{R_1},
$$
所以单位长度的自感为

$$
\frac Ll=\frac{\mu_0}{8\pi}+\frac{\mu_0}{2\pi}\ln\frac{R_2}{R_1}.
$$
第一项来自内导体内部的磁场。高频时电流集中在内导体表面（趋肤效应），这一项消失。

### 9.6.3. 互感磁能

两个线圈分别通有电流 $I_1$、$I_2$ 时，磁场的总能量为

$$
W_{\mathrm{m}}=\frac12L_1I_1^2+\frac12L_2I_2^2+MI_1I_2.
$$
推导：先使线圈 1 的电流由 $0$ 增大到 $I_1$（线圈 2 无电流），电源做功 $\frac12L_1I_1^2$；再保持 $I_1$ 不变，使线圈 2 的电流由 $0$ 增大到 $I_2$，线圈 2 的电源做功 $\frac12L_2I_2^2$，同时线圈 2 的电流变化在线圈 1 中产生互感电动势，线圈 1 的电源为维持 $I_1$ 不变要克服它做功 $\int I_1M_{12}\,\mathrm{d}i_2=M_{12}I_1I_2$。若改变两个线圈通电的顺序，同理得到交叉项 $M_{21}I_1I_2$。磁场的终态相同，能量与过程无关，所以 $M_{12}=M_{21}$，这就是 §9.4 中互感对称性的证明。交叉项 $MI_1I_2$ 称为互感磁能，可正可负；由 $W_{\mathrm{m}}\ge0$ 对一切 $I_1,I_2$ 成立，还可得到 $M^2\le L_1L_2$，即 $k\le1$。

## 9.7. 超导简介

### 9.7.1. 超导电性的发现

1908 年，Kamerlingh Onnes 在 Leiden 首次实现了氦的液化，获得 $4.2\,\mathrm{K}$ 的低温。1911 年他发现，汞冷却到约 $4.2\,\mathrm{K}$ 时电阻突然消失。物质在低温下电阻完全消失的现象称为超导电性（superconductivity），处于这种状态的导体称为超导体，电阻消失的温度称为超导**临界温度** $T_{\mathrm{c}}$。Onnes 因低温物理的研究获 1913 年 Nobel 物理学奖。

### 9.7.2. 超导体的两个基本性质

- 零电阻：超导体中 $R=0$，有电流时两端电压为零，体内总有 $\boldsymbol{E}=\boldsymbol{0}$。在超导环中激发的电流可以持续流动而不衰减（持续电流），实验观测数年未见减小，由此推断其电阻率比铜的室温电阻率（约 $1.7\times10^{-8}\,\Omega\,\mathrm{m}$）小 15 个数量级以上。
- 完全抗磁性：1933 年 Meissner 与 Ochsenfeld 发现，超导体处在超导态时，体内的磁感应强度总是零，原来在体内的磁场在转变为超导态时被排出，这称为 Meissner 效应（Meissner effect）。排斥磁场的是超导体表面薄层（约 $0.1\,\mu\mathrm{m}$ 量级，称为穿透深度）中的超导电流，它在体内产生的磁场与外磁场恰好抵消。相当于 $\chi_{\mathrm{m}}=-1$ 的理想**抗磁体**，超导体可以稳定地悬浮在磁体上方。

这两个性质是相互独立的，实验上判定一种材料是否为超导体，两者缺一不可。只有零电阻的导体称为理想导体：由 $\boldsymbol{E}=\boldsymbol{0}$ 和 $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$，理想导体内的磁场不能改变，但可以不为零，它的状态与历史有关（先降温后加磁场，体内无磁场；先加磁场后降温，磁场被"冻结"在体内）。超导体则不论先后顺序，体内都没有磁场，所以超导态是一个由温度与磁场唯一确定的热力学状态。

### 9.7.3. 临界参量

超导态只在一定条件下存在：

1. 临界温度 $T_{\mathrm{c}}$：$T<T_{\mathrm{c}}$ 时电阻为零。
2. 临界磁场 $B_{\mathrm{c}}$：外磁场超过 $B_{\mathrm{c}}$ 时超导态被破坏。经验上 $B_{\mathrm{c}}(T)\approx B_{\mathrm{c}}(0)\big[1-(T/T_{\mathrm{c}})^2\big]$。
3. 临界电流密度 $J_{\mathrm{c}}$：电流的磁场也会破坏超导，超导体中的电流密度不能超过 $J_{\mathrm{c}}$，它也随温度升高而减小。实用超导薄膜的 $J_{\mathrm{c}}$ 可达 $10^{10}\,\mathrm{A/m^2}$。

上面描述的是第一类超导体（多数纯金属）。第二类超导体（多数合金与化合物）在两个临界磁场之间处于混合态：磁场以量子化的磁通线（每根携带磁通量子 $h/(2e)$）穿入体内，其余部分仍是超导的，所以能在很强的磁场中保持零电阻。医院磁共振成像仪和大型强子对撞机的超导磁体用的都是第二类超导体（铌钛、铌三锡合金）。

### 9.7.4. 发展简史与现状

| 年份 | 事件 |
|---|---|
| 1911 | Onnes 发现汞的超导电性（1913 年 Nobel 奖） |
| 1933 | Meissner 效应 |
| 1957 | Bardeen、Cooper、Schrieffer 的微观理论（BCS 理论）：电子通过与晶格振动的相互作用结成 Cooper 对（1972 年 Nobel 奖） |
| 1962 | Josephson 预言超导隧道效应（Josephson 效应），1973 年与 Esaki、Giaever 共获 Nobel 奖 |
| 1986 | Bednorz 与 Müller 发现铜氧化物高温超导体（约 $35\,\mathrm{K}$，1987 年 Nobel 奖） |
| 1987 | 钇钡铜氧（$T_{\mathrm{c}}\approx92\,\mathrm{K}$，朱经武、吴茂昆，及赵忠贤等独立发现），首次高于液氮温度 $77\,\mathrm{K}$ |
| 1993–1994 | 汞系铜氧化物，常压 $T_{\mathrm{c}}\approx133$–$138\,\mathrm{K}$，加压下约 $164\,\mathrm{K}$，保持至今的常压纪录 |
| 2001、2008 | 二硼化镁（$39\,\mathrm{K}$）、铁基超导体（细野秀雄等；块材最高约 $55\,\mathrm{K}$） |
| 2003 | Abrikosov、Ginzburg、Leggett 因超导与超流理论获 Nobel 奖 |
| 2015–2019 | 高压下的氢化物：硫化氢约 $203\,\mathrm{K}$（约 $150\,\mathrm{GPa}$），十氢化镧约 $250\,\mathrm{K}$（约 $170\,\mathrm{GPa}$） |
| 2023 | 镍氧化物 $\ce{La3Ni2O7}$ 在约 $14\,\mathrm{GPa}$ 下约 $80\,\mathrm{K}$ |

常压下的室温超导至今尚未实现，几次宣称发现室温超导的报道都未能被重复。铜氧化物等高温超导体的机理也仍是凝聚态物理中悬而未决的问题。超导的应用包括强磁体（磁共振成像、加速器、核聚变装置）、超导磁悬浮列车、超导输电与限流器，以及基于 Josephson 效应的超导量子**干涉**器件（SQUID，可测 $10^{-15}\,\mathrm{T}$ 量级的磁场）和超导量子比特。

## 小结

- Faraday 定律 $\mathcal{E}=-\mathrm{d}\Psi/\mathrm{d}t$；Lenz 定律确定方向，是能量守恒的要求。
- 动生电动势 $\int(\boldsymbol{v}\times\boldsymbol{B})\cdot\mathrm{d}\boldsymbol{l}$，非静电力是 Lorentz 力；感生电动势来自感生电场，$\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$，感生电场是无源的涡旋场。两者的区分与参考系有关。
- 互感 $\Psi_{21}=Mi_1$，$M_{12}=M_{21}$；自感 $\Psi=Li$，长直螺线管 $L=\mu n^2V$。RL 电路的**时间常量** $L/R$，LC 电路的角频率 $1/\sqrt{LC}$。
- 磁能 $\frac12LI^2$，能量密度 $\frac12\boldsymbol{B}\cdot\boldsymbol{H}$；两线圈的总磁能 $\frac12L_1I_1^2+\frac12L_2I_2^2+MI_1I_2$。
- 超导体：零电阻与完全抗磁性（Meissner 效应），受临界温度、临界磁场与临界电流密度限制。

## 思考题

1. 电磁炉的工作原理是什么？为什么普通的铝锅不适合用在电磁炉上？
   提示：线圈中的高频交变电流在锅底产生涡流发热。铁是铁磁质，趋肤深度小，涡流集中在很薄的表层，等效电阻大，加热效率高；铝的电阻率小又不是铁磁质，趋肤深度大，等效电阻小，同样的感应电流下发热少（部分新型电磁炉用更高的频率加热铝锅）。
2. 变压器的铁芯为什么做成片状，并涂上绝缘漆相互隔开？铁片应怎样放置？
   提示：减小涡流损耗。铁片平行于磁场方向放置，涡流的通路（垂直于磁场的平面内的闭合回路）被绝缘层割断。
3. 尺寸相同的铁环和铝环中通过的磁通量的变化率相同，两环中的感应电动势、感应电流和感生电场是否相同？
   提示：感生电场由磁场的变化决定，与环的材料无关，所以感应电动势相同；电阻不同，感应电流不同（忽略感应电流自身的磁场时）。
4. 三个小线圈的中心在一条直线上，彼此相距很近，怎样放置才能使它们两两之间的互感为零？
   提示：使三个线圈的轴线互相垂直，其中一个线圈的轴线沿三个中心的连线。小线圈可看作**磁偶极子**，轴线沿连线的线圈在另两个线圈处的磁场平行于连线，不穿过它们；另两个线圈轴线都垂直于连线，各自在对方处的磁场与自身轴线平行、与对方轴线垂直。
5. 理想导体与超导体在磁场中降温时有什么不同？
   提示：见 §9.7.2。先加磁场后降温，理想导体把磁场冻结在体内，超导体把磁场排出。
