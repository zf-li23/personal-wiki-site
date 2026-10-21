---
title: 磁力
description: 带电粒子在磁场中的回旋、螺旋运动与磁约束，电场与磁场的相对性，Hall 效应与量子 Hall 效应，载流导线受的 Ampère 力与安培的定义，载流线圈的磁矩、磁力矩与势能。
---

上一章（[5.3.6](/5.3.6)）讨论磁场怎样由电流产生，本章讨论磁场怎样作用于运动电荷和电流。基本规律只有一条：速度为 $\boldsymbol{v}$ 的电荷 $q$ 受 **Lorentz 力** $q\boldsymbol{v}\times\boldsymbol{B}$。由它出发，本章依次讨论单个带电粒子的运动（回旋加速器、质谱仪、磁约束）、**导体**中大量载流子受力的两种宏观表现（Hall 效应和载流导线受的 Ampère 力）以及载流线圈受的力矩。中间插入一节，用狭义相对论（[5.1.8](/5.1.8)）说明磁力与电力是同一种相互作用在不同参考系中的表现。本章引入的磁矩是下一章（[5.3.8](/5.3.8)）理解物质磁性的出发点；力矩与能量的计算与**电偶极子**在电场中的情形（[5.3.2](/5.3.2)）完全平行。

## 7.1. 带电粒子在磁场中的运动

在磁场 $\boldsymbol{B}$ 中以速度 $\boldsymbol{v}$ 运动的**点电荷** $q$ 受力

$$
\boldsymbol{F}=q\boldsymbol{v}\times\boldsymbol{B}.
$$
磁力始终垂直于速度，所以它不做功，只改变速度的方向而不改变速率与动能。本节讨论均匀磁场（及缓变磁场）中只受磁力的粒子。

### 7.1.1. 回旋运动

设粒子以速度 $\boldsymbol{v}\perp\boldsymbol{B}$ 进入均匀磁场。磁力大小 $qvB$ 恒定、方向垂直于速度，提供圆周运动的向心力：$qvB=mv^2/R$，因此粒子在垂直于 $\boldsymbol{B}$ 的平面内做匀速圆周运动，

$$
R=\frac{mv}{qB}=\frac{p}{qB},\qquad T=\frac{2\pi R}{v}=\frac{2\pi m}{qB},\qquad \omega_{\mathrm{c}}=\frac{qB}{m}.
$$
$\omega_{\mathrm{c}}$ 称为回旋频率（cyclotron frequency）。它的要点是：周期与速率、半径无关，快的粒子走大圆，慢的粒子走小圆，转一圈的时间相同。从 $\boldsymbol{B}$ 的方向看去，正电荷沿顺时针方向回旋，负电荷沿逆时针方向回旋。

高速粒子的半径公式 $R=p/(qB)$ 仍然成立，只是 $p$ 要用**相对论动量** $p=\gamma mv$（[5.1.8](/5.1.8#sec-8.7)）；回旋频率则变为 $\omega=qB/(\gamma m)$，随能量增大而减小。高能物理中常用的实用公式是 $pc\,[\mathrm{GeV}]\approx0.3\,B\,[\mathrm{T}]\,R\,[\mathrm{m}]$（$q=e$），测量径迹的曲率半径就能求出粒子的动量。

### 7.1.2. 回旋加速器与质谱仪

回旋加速器（cyclotron）（Lawrence，1932 年）利用了回旋周期与速率无关这一点。两个中空的 D 形金属盒置于均匀磁场中，盒间的缝隙加上频率等于回旋频率的交变电压。粒子在盒内（无电场）做半圆运动，每次穿过缝隙时电压恰好反向，粒子每半圈被加速一次；速率增大后半径增大，但每半圈的时间不变，加速得以同步地持续下去。D 形盒的半径 $R$ 决定了最终的速率与动能：

$$
v_{\max}=\frac{qBR}{m},\qquad E_{\mathrm{k}}=\frac{q^2B^2R^2}{2m}.
$$

**例 7.1.1（回旋加速器的能量上限）** 取 $B=1\,\mathrm{T}$，$R=1\,\mathrm{m}$，对质子，$p=eBR$，$pc=e\,B\,R\,c\approx300\,\mathrm{MeV}$，由能量–动量关系（[5.1.8](/5.1.8#sec-8.9.3)）求得动能 $E_{\mathrm{k}}=\sqrt{(pc)^2+(m_{\mathrm{p}}c^2)^2}-m_{\mathrm{p}}c^2\approx47\,\mathrm{MeV}$（按非相对论公式为 $48\,\mathrm{MeV}$），$v\approx0.3c$。此时 $\gamma\approx1.05$，回旋频率已比低速时降低约 5%，粒子逐渐落后于加速电压的相位。因此固定频率的经典回旋加速器只能把质子加速到约 $20\,\mathrm{MeV}$；更高的能量需要随能量调低电压频率（同步回旋加速器）、让 $B$ 随半径增大（等时性回旋加速器），或者让粒子在固定半径的环形轨道上运动、同步地增大 $B$（同步加速器）。

质谱仪（mass spectrometer）用磁偏转区分质量。离子先通过电场 $\boldsymbol{E}$ 与磁场 $\boldsymbol{B}$ 互相垂直的速度选择器，只有电力与磁力平衡（$qE=qvB$）的离子沿直线通过，速率都是 $v=E/B$；进入另一个磁场 $B'$ 后做半圆运动，半径 $R=mv/(qB')\propto m/q$。电荷相同的同位素落在底片的不同位置，由此测定同位素的质量和丰度，或者分离同位素。

### 7.1.3. 螺旋运动与磁聚焦

若速度与均匀磁场的夹角为 $\theta$，把速度分解为平行于 $\boldsymbol{B}$ 的分量 $v_\parallel=v\cos\theta$ 和垂直分量 $v_\perp=v\sin\theta$。磁力只与 $v_\perp$ 有关，所以粒子在垂直平面内以半径 $R=mv_\perp/(qB)$、周期 $T=2\pi m/(qB)$ 回旋，同时沿磁场方向匀速运动，轨迹是一条螺旋线，螺距为

$$
h=v_\parallel T=\frac{2\pi mv\cos\theta}{qB}.
$$
从同一点发出、速率相同、与 $\boldsymbol{B}$ 的夹角 $\theta$ 都很小的一束粒子，$\cos\theta\approx1$，各粒子的螺距近似相同，虽然它们沿不同的螺旋线前进，但经过一个周期后又会聚到同一点。这就是磁聚焦（magnetic focusing），电子显微镜中的磁透镜即依据这一原理（用的是短线圈产生的非均匀磁场）。

### 7.1.4. 磁约束

粒子沿**磁感线**做螺旋运动，回旋半径 $R=mv_\perp/(qB)$ 随 $B$ 增大而减小：磁场很强（$1\,\mathrm{T}$ 量级）时，带电粒子被"拴"在一束很细的磁感线上，横向不能自由运动，这是横向约束。纵向约束靠的是非均匀磁场。在磁场由弱变强的区域，磁感线向轴线会聚，$\boldsymbol{B}$ 有指向轴线的径向分量，它与回旋速度的**叉积**给出指向弱场区的轴向力，使粒子的纵向运动减速，甚至反射回来。这样的强场区称为磁镜（magnetic mirror）；两端各有一个磁镜的位形称为磁瓶，可以把粒子约束在两镜之间来回运动。用这种方法约束高温等离子体，称为磁约束（magnetic confinement），它是受控热核聚变研究的基本思路之一（托卡马克用环形的磁场位形实现约束）。

**注 7.1.1（磁镜的反射条件）** 磁场沿粒子轨道缓慢变化（在一个回旋周期内变化很小）时，回旋运动的磁矩（把 [§7.5](#sec-7.5) 定义的磁矩用于回旋轨道）$\frac{mv_\perp^2}{2B}$ 近似守恒，称为绝热不变量；又因磁力不做功，$v_\perp^2+v_\parallel^2=v^2$ 不变。在磁场为 $B_0$ 处速度与磁场的夹角为 $\theta_0$ 的粒子，在 $B$ 较大处有 $\sin^2\theta=\sin^2\theta_0\cdot B/B_0$，当 $B=B_0/\sin^2\theta_0$ 时 $v_\parallel=0$，粒子在那里反射。若磁瓶中最强处的磁场为 $B_{\max}$，则 $\sin^2\theta_0<B_0/B_{\max}$ 的粒子（速度几乎沿磁感线的粒子）不能被反射而逃逸，所以磁镜总有一定的泄漏。

![左：均匀磁场中带电粒子的螺旋运动，螺距恒定；右：数值求解的粒子在磁瓶中的运动（灰线为磁感线，中心处的投掷角为 50°），粒子在两端磁场较强处被反射，回旋半径随磁场增强而减小](./plots/charged-particle-trajectories.py)

地球磁场是一个天然的磁瓶：磁场从赤道上空向两极逐渐增强，能够俘获来自宇宙线和太阳风的质子与电子，形成环绕地球的 van Allen 辐射带（1958 年由人造卫星发现，内带以高能质子为主，外带以高能电子为主）。在地磁两极附近，磁感线几乎垂直于地面，带电粒子可以沿磁感线沉降到高层大气，与氧原子、氮分子碰撞并激发它们发光，这就是极光（氧原子的绿光 $557.7\,\mathrm{nm}$ 最常见）。

## 7.2. 电场和磁场的相对性和统一性

同时存在电场和磁场时，运动电荷受的力是电场力与磁场力之和：

**公式 7.2.1（Lorentz 力公式）**

$$
\boldsymbol{F}=q\boldsymbol{E}+q\boldsymbol{v}\times\boldsymbol{B}.
$$

磁力依赖于电荷的速度，而速度依赖于参考系。在电荷瞬时静止的参考系中，磁力消失了——但物理结果（例如电荷是否撞上某处的屏）不能依赖于参考系的选择。这说明电场和磁场本身也必须随参考系变换。下面用一个简单的例子看出这一点。

**例 7.2.1（运动带电平面的电场与磁场）** 一个无限大均匀带电平面（$xz$ 平面）与它上方（$y>0$）的点电荷 $q$ 一起以速度 $u$ 沿 $x$ 方向运动。在随之运动的 S′ 系中，平面静止，设其面**电荷密度**为 $\sigma$，则只有静电场 $E'_y=\frac{\sigma}{2\varepsilon_0}$，$q$ 受力 $F'_y=qE'_y=\frac{q\sigma}{2\varepsilon_0}$。

在 S 系中，电荷量是相对论不变量（[5.3.1](/5.3.1)），而平面沿 $x$ 方向**长度收缩**，面电荷密度变为 $\gamma\sigma$（$\gamma$ 是 **Lorentz 因子**）；同时运动的电荷构成面电流，面**电流密度**为 $\gamma\sigma u$。因此 S 系中既有电场又有磁场（无限大面电流的磁场为 $\mu_0K/2$，[5.3.6](/5.3.6)）：

$$
E_y=\frac{\gamma\sigma}{2\varepsilon_0},\qquad B_z=\frac{\mu_0}{2}\gamma\sigma u=\frac{uE_y}{c^2},\qquad\text{即}\quad\boldsymbol{B}=\frac{\boldsymbol{u}\times\boldsymbol{E}}{c^2},
$$
其中用了 $\varepsilon_0\mu_0=1/c^2$。$q$ 在 S 系中受的力为

$$
F_y=q(E_y-uB_z)=\frac{q\gamma\sigma}{2\varepsilon_0}\Big(1-\frac{u^2}{c^2}\Big)=\frac{q\sigma}{2\varepsilon_0\gamma}=\frac{F'_y}{\gamma}.
$$
这正是相对论的力的变换（[5.1.8](/5.1.8#sec-8.11)）所要求的：在粒子静止系中测得的力，在粒子以速度 $u$ 运动的参考系中，沿运动方向的分量不变，垂直分量变为原来的 $1/\gamma$。反过来，如果 S 系中只考虑电场力 $qE_y$，就会得到 $\gamma F'_y$，与力的变换矛盾：磁场力恰好是保证**相对性原理**成立所必需的。

一般地，设 S′ 系相对 S 系以速度 $v$ 沿 $x$ 方向运动，由 **Lorentz 变换**和力的变换可以导出电磁场的变换：

$$
\begin{aligned}
E'_x&=E_x, & E'_y&=\gamma(E_y-vB_z), & E'_z&=\gamma(E_z+vB_y),\\
B'_x&=B_x, & B'_y&=\gamma\Big(B_y+\frac{v}{c^2}E_z\Big), & B'_z&=\gamma\Big(B_z-\frac{v}{c^2}E_y\Big).
\end{aligned}
$$
沿运动方向的分量不变，垂直分量互相混合。一个**惯性系**中的纯电场，在另一个惯性系中观测就同时有电场和磁场，反之亦然；电场和磁场是同一个电磁场的不同侧面，它们怎样划分取决于参考系。$\boldsymbol{E}\cdot\boldsymbol{B}$ 与 $E^2-c^2B^2$ 在变换下保持不变，所以若某个惯性系中只有电场（$\boldsymbol{B}=\boldsymbol{0}$），则在任何惯性系中都有 $E>cB$。

**注 7.2.1（为什么通常磁力比电力小得多）** 两个点电荷以相同的速度 $v$ 平行运动时，可以算出它们之间的磁力与电力之比为 $F_{\mathrm{m}}/F_{\mathrm{e}}=v^2/c^2$。导线中电子的漂移速率只有 $10^{-4}\,\mathrm{m/s}$ 量级，$v^2/c^2\sim10^{-25}$，然而载流导线之间的磁力却很容易观察。原因在于导线是电中性的：正负电荷的电力精确地相互抵消，剩下的只有这个"相对论修正"。从这个意义上说，磁现象是**电荷守恒**、电荷不变性与狭义相对论的必然结果（Purcell 的电磁学教材就是这样展开的）。

## 7.3. Hall 效应

### 7.3.1. Hall 效应与 Hall 电势差

1879 年 Hall 发现：把载流导体或半导体薄片放在与电流方向垂直的磁场中，在与电流和磁场都垂直的方向上，薄片两侧之间出现横向**电势差**。这一现象称为 Hall 效应（Hall effect），横向电势差称为 Hall 电势差 $U_{\mathrm{H}}$。

设薄片沿电流方向放置，宽 $h$（Hall 电势差测量的方向），厚 $b$（沿磁场方向），载流子的电荷量为 $q$、数密度为 $n$、**漂移速度**为 $\boldsymbol{v}$，则电流 $I=nqvhb$。载流子受磁力 $q\boldsymbol{v}\times\boldsymbol{B}$ 偏向一侧，使两侧积累异号电荷，产生横向电场 $E_{\mathrm{H}}$；当横向电力与磁力平衡，

$$
qE_{\mathrm{H}}=qvB,
$$
后续的载流子不再偏转，达到稳定。于是

$$
U_{\mathrm{H}}=E_{\mathrm{H}}h=vBh=\frac{1}{nq}\frac{IB}{b}=K_{\mathrm{H}}\frac{IB}{b},\qquad K_{\mathrm{H}}=\frac{1}{nq}.
$$
$K_{\mathrm{H}}$ 称为 Hall 系数（Hall coefficient）（国际文献多记为 $R_{\mathrm{H}}$），$U_{\mathrm{H}}/I=B/(nqb)$ 称为 Hall **电阻**。

Hall 效应有两个主要用途。第一，$U_{\mathrm{H}}$ 的正负由载流子电荷的正负决定（同样方向的电流，正载流子与负载流子向同一侧偏转，积累的电荷却异号），所以测量 $U_{\mathrm{H}}$ 的符号可以判断载流子的类型，测量 $K_{\mathrm{H}}$ 的大小可以求出载流子的数密度 $n$。这正是确认半导体中存在带正电的"空穴"的实验依据（[5.5.6](/5.5.6)）。第二，已知 $K_{\mathrm{H}}$ 时，由 $U_{\mathrm{H}}$ 可以测磁场（Hall 探头，也用于手机中的电子罗盘和无刷电机的位置传感器），或者由电流的磁场测大电流。

**例 7.3.1（金属与半导体的 Hall 电势差）** 铜的自由电子数密度 $n\approx8.5\times10^{28}\,\mathrm{m^{-3}}$。厚 $b=0.1\,\mathrm{mm}$ 的铜片通以 $I=10\,\mathrm{A}$，置于 $B=1\,\mathrm{T}$ 的磁场中，

$$
U_{\mathrm{H}}=\frac{IB}{neb}=\frac{10\times1}{8.5\times10^{28}\times1.6\times10^{-19}\times10^{-4}}\,\mathrm{V}\approx7\,\mu\mathrm{V}.
$$
掺杂半导体的载流子数密度可以低到 $10^{21}\,\mathrm{m^{-3}}$，同样厚度的薄片只需 $I=1\,\mathrm{mA}$、$B=0.1\,\mathrm{T}$ 就有约 $6\,\mathrm{mV}$ 的 Hall 电势差。所以 Hall 元件都用半导体制作。

### 7.3.2. 量子 Hall 效应

1980 年 von Klitzing 发现，在极低温（约 $1\,\mathrm{K}$）和强磁场（约 $10\,\mathrm{T}$）下，半导体界面上的二维电子气的 Hall 电阻不再与 $B$ 成正比，而是随 $B$ 的增大呈现一系列平台：

$$
R_{\mathrm{H}}=\frac{R_{\mathrm{K}}}{\nu},\qquad \nu=1,2,3,\dots,\qquad R_{\mathrm{K}}=\frac{h}{e^2}=25\,812.807\,45\ldots\,\Omega.
$$
这称为量子 Hall 效应（quantum Hall effect），$R_{\mathrm{K}}$ 称为 von Klitzing 常量（von Klitzing constant），von Klitzing 因此获 1985 年 Nobel 物理学奖。平台的值只由基本常量决定，与样品的材料、形状和杂质无关，不同实验室测得的平台值在 $10^{-10}$ 的相对精度内一致；其根源是二维电子在强磁场中形成的分立能级（Landau 能级）和波函数的拓扑性质。因此 1990 年起国际上用约定值 $R_{\mathrm{K\text{-}90}}=25\,812.807\,\Omega$ 复现电阻单位欧姆。2019 年 SI 把 $h$ 和 $e$ 定义为精确值以后，$R_{\mathrm{K}}=h/e^2$ 本身成为精确值，量子 Hall 电阻直接实现 SI 的欧姆。

1982 年 Tsui 与 Störmer 又在更纯净的样品中发现了 $\nu$ 为分数（如 $\frac13$、$\frac25$）的平台，即分数量子 Hall 效应；Laughlin 的理论表明它来自电子之间强关联形成的集体状态，其中的准粒子携带分数电荷（如 $e/3$，1997 年由电流噪声实验证实），三人获 1998 年 Nobel 物理学奖。2013 年薛其坤团队在磁性拓扑绝缘体薄膜中观测到无需外磁场的量子反常 Hall 效应。

## 7.4. 载流导线在磁场中受的磁力

### 7.4.1. Ampère 力

导线中的电流是载流子的定向运动，每个载流子都受 **Lorentz 力** $q\boldsymbol{v}\times\boldsymbol{B}$，这些力通过载流子与晶格的相互作用传给导线，宏观上表现为导线受力。设导线截面积为 $S$，载流子数密度为 $n$、电荷量为 $q$、漂移速度为 $\boldsymbol{v}$（与线元 $\mathrm{d}\boldsymbol{l}$ 同向）。长为 $\mathrm{d}l$ 的一段导线中有 $nS\,\mathrm{d}l$ 个载流子，它们受力之和为

$$
\mathrm{d}\boldsymbol{F}=nS\,\mathrm{d}l\,q\boldsymbol{v}\times\boldsymbol{B}=nqvS\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}=I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B},
$$
其中 $I=nqvS$。

**定理 7.4.1（Ampère 力公式）** 磁场对电流元 $I\,\mathrm{d}\boldsymbol{l}$ 的作用力为 $\mathrm{d}\boldsymbol{F}=I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}$，一段载流导线 $L$ 受的磁力为

$$
\boldsymbol{F}=\int_LI\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}.
$$

磁场对电流的作用力称为 Ampère 力（Ampère force）。它是电动机、扬声器、电流计等的工作原理。两个较新的例子：电磁轨道炮让兆安量级的电流经两条平行导轨和导轨间的导电滑块（或滑块后方的等离子体）构成回路，导轨电流的磁场对滑块电流的 Ampère 力在毫秒内把弹丸加速到每秒数千米；磁流体推进让电流横向穿过导管中的海水，在垂直的磁场中受 Ampère 力，把海水沿导管喷出而推动船只（日本"大和一号"实验船，1992 年），没有螺旋桨与传动部件。

**例 7.4.1（均匀磁场中的弯曲导线）** 一段任意形状的导线 $ab$ 通有电流 $I$，置于均匀磁场 $\boldsymbol{B}$ 中。由于 $\boldsymbol{B}$ 是常矢量，

$$
\boldsymbol{F}=\int_a^bI\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}=I\Big(\int_a^b\mathrm{d}\boldsymbol{l}\Big)\times\boldsymbol{B}=I\,\overrightarrow{ab}\times\boldsymbol{B},
$$
大小为 $F=I\,\lvert ab\rvert\,B\sin\theta$（$\theta$ 是 $\overrightarrow{ab}$ 与 $\boldsymbol{B}$ 的夹角）：弯曲导线受的力与连接两端的直导线相同。若 $a$、$b$ 重合，$\boldsymbol{F}=\boldsymbol{0}$：均匀磁场中的闭合载流回路所受的磁力之和为零（但力矩一般不为零，见 [§7.5](#sec-7.5)）。

### 7.4.2. 平行电流之间的作用力与安培的定义

**例 7.4.2（平行载流直导线之间的力）** 真空中两根平行的无限长直导线相距 $d$，分别通有电流 $I_1$、$I_2$。$I_1$ 在导线 2 处的磁场为 $B_1=\frac{\mu_0I_1}{2\pi d}$（[5.3.6](/5.3.6)），方向垂直于两导线所在的平面，所以导线 2 每单位长度受力

$$
\frac{\mathrm{d}F_2}{\mathrm{d}l}=B_1I_2=\frac{\mu_0I_1I_2}{2\pi d},
$$
方向在两导线所在的平面内、垂直于导线。同理导线 1 每单位长度受力大小相同、方向相反。电流同向时两导线相吸，反向时相斥。

2019 年以前，SI 正是用这个结果定义电流单位安培（A）：真空中相距 $1\,\mathrm{m}$ 的两根无限长、截面可忽略的平行直导线通有相等的**恒定电流**，若每米长度上受力 $2\times10^{-7}\,\mathrm{N}$，则电流为 $1\,\mathrm{A}$。这个定义等价于规定 $\mu_0=4\pi\times10^{-7}\,\mathrm{N\,A^{-2}}$ 为精确值。

**注 7.4.1（2019 年的 SI）** 2019 年 5 月 20 日起，SI 改为通过规定**元电荷**的数值 $e=1.602\,176\,634\times10^{-19}\,\mathrm{C}$ 来定义安培：$1\,\mathrm{A}$ 就是每秒通过 $1/(1.602\,176\,634\times10^{-19})$ 个元电荷的电流。于是 $\mu_0$ 不再是定义值，而要由精细结构常数 $\alpha$ 的测量确定（$\mu_0=2\alpha h/(e^2c)$）：

$$
\mu_0=1.256\,637\,061\,27(20)\times10^{-6}\,\mathrm{N\,A^{-2}},
$$
它与 $4\pi\times10^{-7}\,\mathrm{N\,A^{-2}}$ 的相对差别在 $10^{-10}$ 量级，日常计算中仍取 $4\pi\times10^{-7}$。$\varepsilon_0=1/(\mu_0c^2)$ 也随之成为测量值（[5.3.1](/5.3.1)）。

## 7.5. 载流线圈在均匀磁场中的磁力矩

### 7.5.1. 磁矩与磁力矩

由例 7.4.1，均匀磁场中闭合线圈受的合力为零，但各边受力不共线，线圈受力矩。考虑边长为 $l_1$、$l_2$ 的矩形线圈，通有电流 $I$，可以绕平行于 $l_2$ 边的中心轴转动，磁场 $\boldsymbol{B}$ 垂直于转轴。两条 $l_1$ 边受的力大小相等、方向相反且共线，相互抵消；两条 $l_2$ 边垂直于 $\boldsymbol{B}$，受力大小都是 $F=Il_2B$、方向相反，构成力偶。设线圈平面的法线（与电流成右手螺旋关系）与 $\boldsymbol{B}$ 的夹角为 $\theta$，力偶的力臂为 $l_1\sin\theta$，力矩大小为

$$
M=Il_2B\cdot l_1\sin\theta=ISB\sin\theta,
$$
其中 $S=l_1l_2$ 是线圈的面积。力矩只通过乘积 $IS$ 与线圈有关，由此引入描述载流线圈磁性质的矢量。

**定义 7.5.1（磁矩）** 面积为 $S$、通有电流 $I$ 的平面线圈的**磁矩**为

$$
\boldsymbol{m}=IS\boldsymbol{e}_{\mathrm{n}},
$$
其中 $\boldsymbol{e}_{\mathrm{n}}$ 是线圈平面的单位法向矢量，方向与电流的绕向成右手螺旋关系（右手四指沿电流方向弯曲，拇指指向 $\boldsymbol{e}_{\mathrm{n}}$）。$N$ 匝线圈的磁矩为 $NIS\boldsymbol{e}_{\mathrm{n}}$。磁矩的 SI 单位是 $\mathrm{A\,m^2}$（也可写作 $\mathrm{J/T}$）。

磁矩也称磁偶极矩（magnetic dipole moment）：小线圈在远处产生的磁场与电偶极子的电场形式相同（[5.3.6](/5.3.6) 中圆电流轴线上的场），线圈就是一个**磁偶极子**。用磁矩表示，力矩为

**公式 7.5.1（载流线圈的磁力矩）**

$$
\boldsymbol{M}=\boldsymbol{m}\times\boldsymbol{B}.
$$

这个结果对任意形状的平面线圈都成立（任意线圈可以分割成许多小矩形线圈，相邻线圈的公共边上电流相反而抵消），与电偶极子在均匀电场中受的力矩 $\boldsymbol{M}=\boldsymbol{p}\times\boldsymbol{E}$ 形式完全相同。力矩使线圈转向磁矩与磁场同向的位置（$\theta=0$，稳定平衡），也就是使穿过线圈的**磁通量**（沿 $\boldsymbol{e}_{\mathrm{n}}$ 计算）增大的方向。

直流电动机的转子就是放在磁场中的载流线圈，换向器在线圈转过平衡位置时把电流反向，使力矩的方向保持不变，线圈持续转动。磁电式电流计中，线圈的磁力矩与游丝的弹性力矩平衡，偏转角与电流成正比。

### 7.5.2. 磁矩在均匀磁场中的势能

设磁矩为 $\boldsymbol{m}$ 的线圈在均匀磁场中由夹角 $\theta_1$ 转到 $\theta_2$，保持电流不变（不考虑维持电流的**电源**做的功），外力矩克服磁力矩做的功为

$$
A=\int_{\theta_1}^{\theta_2}mB\sin\theta\,\mathrm{d}\theta=mB(\cos\theta_1-\cos\theta_2).
$$
取磁矩与磁场垂直（$\theta=\pi/2$）时为势能零点，磁矩在均匀磁场中的势能为

$$
E_{\mathrm{p}}=-mB\cos\theta=-\boldsymbol{m}\cdot\boldsymbol{B},
$$
与电偶极子的**静电势能** $E_{\mathrm{p}}=-\boldsymbol{p}\cdot\boldsymbol{E}$ 相对应。$\theta=0$ 时势能最低，$\theta=\pi$ 时最高。在非均匀磁场中，磁矩除受力矩外还受力 $\boldsymbol{F}=\nabla(\boldsymbol{m}\cdot\boldsymbol{B})$（$\boldsymbol{m}$ 保持不变），与磁场同向的磁矩被拉向强场区。这是顺磁物质被磁铁吸引、Stern–Gerlach 实验中原子束分裂（[5.5.4](/5.5.4)）的原因；磁矩在磁场中不同取向的能量差 $2mB$ 则是核磁共振的基础（[5.3.8](/5.3.8)）。

**例 7.5.1（旋转带电圆盘的磁矩与磁力矩）** 半径为 $R$ 的塑料圆盘均匀带电，面电荷密度为 $\sigma$，绕通过圆心、垂直于盘面的轴以角速度 $\omega$ 转动，置于与转轴垂直的均匀磁场 $\boldsymbol{B}$ 中，求圆盘受的磁力矩。

**解** 把圆盘分成同心细圆环。半径 $r$、宽 $\mathrm{d}r$ 的圆环带电 $\mathrm{d}q=\sigma\cdot2\pi r\,\mathrm{d}r$，每转一周（时间 $2\pi/\omega$）这些电荷通过环上任一截面一次，等效电流与磁矩为

$$
\mathrm{d}I=\frac{\omega}{2\pi}\,\mathrm{d}q=\sigma\omega r\,\mathrm{d}r,\qquad \mathrm{d}m=\pi r^2\,\mathrm{d}I=\pi\sigma\omega r^3\,\mathrm{d}r.
$$
各圆环的磁矩方向相同（$\sigma>0$ 时沿 $\boldsymbol{\omega}$），积分得

$$
m=\int_0^R\pi\sigma\omega r^3\,\mathrm{d}r=\frac{\pi\sigma\omega R^4}{4}.
$$
$\boldsymbol{m}\perp\boldsymbol{B}$，磁力矩大小为 $M=mB=\frac14\pi\sigma\omega BR^4$，方向沿 $\boldsymbol{m}\times\boldsymbol{B}$，垂直于转轴和磁场。

**注 7.5.1（磁矩与角动量）** 设圆盘的质量为 $m_0$、总电荷 $Q=\sigma\pi R^2$，其**角动量**为 $L=\frac12m_0R^2\omega$，于是

$$
\frac{m}{L}=\frac{\pi\sigma\omega R^4/4}{m_0R^2\omega/2}=\frac{Q}{2m_0}.
$$
只要电荷与质量的分布成比例，任何转动的带电体都有 $\boldsymbol{m}=\frac{Q}{2m_0}\boldsymbol{L}$。下一章（[5.3.8](/5.3.8)）会看到，电子轨道运动的磁矩与**角动量**之比正是 $-e/(2m_{\mathrm{e}})$，而电子自旋的这个比值约大一倍，后者是经典图像无法解释的量子效应。由于磁矩与角动量成正比，磁场中的磁力矩 $\boldsymbol{m}\times\boldsymbol{B}$ 使角动量绕磁场**进动**，而不是直接把磁矩转到磁场方向，就像重力矩使陀螺**进动**一样（[5.1.5](/5.1.5#sec-5.7.2)）。

## 小结

- 运动电荷受 **Lorentz 力** $\boldsymbol{F}=q\boldsymbol{E}+q\boldsymbol{v}\times\boldsymbol{B}$；磁力不做功。均匀磁场中粒子做回旋或螺旋运动，$R=p/(qB)$，非相对论情形下 $T=2\pi m/(qB)$ 与速率无关。
- 电场与磁场随参考系变换，磁力是保证相对性原理成立的必然结果。
- Hall 电势差 $U_{\mathrm{H}}=IB/(nqb)$，其符号判断载流子类型；二维电子气的 Hall 电阻量子化为 $h/(\nu e^2)$。
- 电流元受 Ampère 力 $I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}$；平行电流同向相吸，单位长度受力 $\mu_0I_1I_2/(2\pi d)$。2019 年起安培由元电荷定义。
- 载流线圈的磁矩 $\boldsymbol{m}=IS\boldsymbol{e}_{\mathrm{n}}$，在均匀磁场中受力矩 $\boldsymbol{m}\times\boldsymbol{B}$，势能 $-\boldsymbol{m}\cdot\boldsymbol{B}$，与电偶极子一一对应。

## 思考题

1. 一束电子从静止经电压 $U$ 加速后垂直进入均匀磁场。电压加倍时，回旋半径和回旋周期怎样变化（非相对论情形）？
   提示：$v\propto\sqrt U$，半径 $R=mv/(eB)$ 变为 $\sqrt2$ 倍；周期 $2\pi m/(eB)$ 不变。
2. 能否用磁场使静止的带电粒子运动起来？能否用恒定磁场改变带电粒子的动能？
   提示：都不能。静止电荷不受磁力；恒定磁场的力垂直于速度，不做功。但变化的磁场会产生电场（[5.3.9](/5.3.9)），可以加速粒子，例如电子感应加速器。
3. 均匀磁场中的闭合载流线圈合力为零。在非均匀磁场中呢？
   提示：一般不为零，力为 $\nabla(\boldsymbol{m}\cdot\boldsymbol{B})$；磁矩与磁场同向的小线圈被吸向强场区，例如条形磁铁吸引通电的小线圈。
4. 测得某半导体样品的 Hall 电势差与用电子导电预期的符号相反，说明什么？
   提示：主要载流子带正电，是 p 型半导体，载流子是空穴（[5.5.6](/5.5.6)）。
