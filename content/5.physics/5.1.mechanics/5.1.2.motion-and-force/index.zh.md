---
title: 运动与力
description: Newton 运动定律与惯性系；2019 年 SI 的定义常数与量纲分析；常见的力与四种基本相互作用；Newton 定律的应用；平动与转动非惯性系中的惯性力、等效原理、潮汐、惯性离心力与 Coriolis 力。
---

上一章 [5.1.1](/5.1.1) 只描述运动，本章讨论运动变化的原因：动力学（dynamics）研究物体之间的相互作用（力）怎样决定物体的**加速度**。Newton 运动定律是经典力学的基础，后面几章的动量定理（[5.1.3](/5.1.3)）、动能定理与能量守恒（[5.1.4](/5.1.4)）、刚体的转动定律（[5.1.5](/5.1.5)）都是它的推论。本章先陈述三条定律与惯性系的概念，再介绍国际单位制与量纲、常见的力和四种基本相互作用，然后通过例题说明用 Newton 定律解题的一般步骤——列出的往往是一个**微分方程**（[2.2.15](/2.2.15)），可以解析求解，也可以用数值方法求解（[4.4.4](/4.4.4)）。最后讨论非惯性系：在加速或转动的**参考系**中引入惯性力，Newton 定律就仍然可以使用，由此可以解释失重、潮汐、重力随纬度的变化和 Coriolis 力的种种现象。

## 2.1. Newton 运动定律

**定理 2.1.1（Newton 第一定律）** 任何物体都保持静止或匀速直线运动的状态，直到其他物体的作用迫使它改变这种状态为止。

第一定律又称惯性定律。物体保持原有运动状态的性质称为惯性；第一定律定性地指出，力是改变物体运动状态的原因，而不是维持运动的原因。它同时规定了定律适用的参考系：

**定义 2.1.1（惯性系）** Newton 第一定律在其中成立的参考系称为**惯性系**。相对惯性系做匀速直线运动的参考系也是惯性系；相对惯性系加速运动的参考系称为**非惯性系**。

**定理 2.1.2（Newton 第二定律）** 物体所受的合外力等于它的动量对时间的变化率：

$$
\boldsymbol{F} = \frac{\mathrm{d}(m\boldsymbol{v})}{\mathrm{d}t}.
$$
质量 $m$ 不变时，$\boldsymbol{F} = m\boldsymbol{a}$。

式中的 $m\boldsymbol{v}$ 是物体的动量（[5.1.3](/5.1.3)）。

**定义 2.1.2（惯性质量）** 第二定律中的质量 $m$ 量度物体惯性的大小——同样的力作用下，质量越大，加速度越小——称为**惯性质量**。

**定理 2.1.3（Newton 第三定律）** 两个物体之间的作用力与反作用力大小相等、方向相反，作用在同一条直线上：

$$
\boldsymbol{F}_{12} = -\boldsymbol{F}_{21},
$$
其中 $\boldsymbol{F}_{12}$ 是物体 2 对物体 1 的作用力。

作用力与反作用力分别作用在两个物体上，不能互相抵消；它们同时出现，性质相同（同为引力、弹力或摩擦力）。

对 Newton 定律的几点说明：

1. Newton 定律只在惯性系中成立；在非惯性系中使用时要引入惯性力（2.6 节）。
2. 定律的对象是**质点**。一般物体可以看成质点的集合（质点系），对每个质点应用 Newton 定律再求和，就得到质点系与刚体的定律（[5.1.3](/5.1.3)、[5.1.5](/5.1.5)），所以 Newton 定律具有普遍意义。
3. 适用范围是宏观物体在弱引力场中的低速运动。**速率**接近光速时要用狭义相对论（[5.1.8](/5.1.8)），第二定律的形式 $\boldsymbol{F} = \mathrm{d}\boldsymbol{p}/\mathrm{d}t$ 保留，但动量不再是 $m\boldsymbol{v}$，$\boldsymbol{F} = m\boldsymbol{a}$ 也不再成立；微观粒子要用量子力学（[5.5](/5.5)）。
4. 第三定律对接触力严格成立；对通过场传递的相互作用（如运动电荷之间的电磁力），两个力可能不严格等值反向，这时守恒的是物体与场的总动量（[5.3](/5.3)）。

上述三条定律合称 Newton 运动定律（Newton's laws of motion）。

## 2.2. SI 单位与量纲

### 2.2.1. 国际单位制

物理量的数值依赖于所选的单位。国际单位制（SI）选定 7 个基本单位，其余单位由它们导出。自 2019 年 5 月 20 日起，SI 不再用实物基准（如保存在巴黎的国际千克原器）定义单位，而是把 7 个物理常数规定为精确值，所有单位都由这些定义常数导出：

| 定义常数 | 精确值 | 主要定义的单位 |
|---|---|---|
| $^{133}\mathrm{Cs}$ 原子基态超精细跃迁频率 $\Delta\nu_{\mathrm{Cs}}$ | $9\,192\,631\,770\,\mathrm{Hz}$ | 秒 $\mathrm{s}$ |
| 真空中的光速 $c$ | $299\,792\,458\,\mathrm{m\,s^{-1}}$ | 米 $\mathrm{m}$ |
| Planck 常量 $h$ | $6.626\,070\,15\times10^{-34}\,\mathrm{J\,s}$ | 千克 $\mathrm{kg}$ |
| 元电荷 $e$ | $1.602\,176\,634\times10^{-19}\,\mathrm{C}$ | 安培 $\mathrm{A}$ |
| Boltzmann 常量 $k_{\mathrm{B}}$ | $1.380\,649\times10^{-23}\,\mathrm{J\,K^{-1}}$ | 开尔文 $\mathrm{K}$ |
| Avogadro 常量 $N_{\mathrm{A}}$ | $6.022\,140\,76\times10^{23}\,\mathrm{mol^{-1}}$ | 摩尔 $\mathrm{mol}$ |
| 频率为 $540\times10^{12}\,\mathrm{Hz}$ 的单色辐射的发光效能 $K_{\mathrm{cd}}$ | $683\,\mathrm{lm\,W^{-1}}$ | 坎德拉 $\mathrm{cd}$ |

力学的三个基本单位因此是：$1\,\mathrm{s}$ 等于 $^{133}\mathrm{Cs}$ 原子基态超精细跃迁辐射周期的 $9\,192\,631\,770$ 倍；$1\,\mathrm{m}$ 是光在真空中 $1/299\,792\,458\,\mathrm{s}$ 内走过的距离；千克由 $h$ 的数值（$\mathrm{J\,s} = \mathrm{kg\,m^2\,s^{-1}}$）连同秒和米的定义确定，实际上用 Kibble 秤等装置复现。热学与电磁学中用到的 $k_{\mathrm{B}}$、$e$、$N_{\mathrm{A}}$ 同样是精确值（[5.2.1](/5.2.1)、[5.3.1](/5.3.1)）。

### 2.2.2. 量纲

**定义 2.2.1（量纲）** 不考虑数字因数，把一个物理量 $Q$ 表示为基本量的幂的乘积，称为 $Q$ 的**量纲**，记作 $\dim Q$。力学中的基本量是长度、质量和时间，量纲记作 $\mathsf{L}$、$\mathsf{M}$、$\mathsf{T}$：

$$
\dim Q = \mathsf{L}^{\alpha}\,\mathsf{M}^{\beta}\,\mathsf{T}^{\gamma}.
$$
指数都为零的量称为量纲一的量（无量纲量），$\dim Q = 1$。

例如 $\dim v = \mathsf{L}\,\mathsf{T}^{-1}$，$\dim F = \mathsf{L}\,\mathsf{M}\,\mathsf{T}^{-2}$。SI 的 7 个基本量纲为 $\mathsf{L}, \mathsf{M}, \mathsf{T}, \mathsf{I}, \Theta, \mathsf{N}, \mathsf{J}$（长度、质量、时间、电流、热力学温度、物质的量、发光强度）。教材中常把量纲写成 $[Q]$，本站按 ISO 80000-1 写 $\dim Q$。

量纲的基本用途是检验方程：只有量纲相同的量才能相加减或用等号连接；指数函数、三角函数、对数的自变量必须是量纲一的量。由此还可以做量纲分析，在不解方程的情况下得到物理量之间关系的形式。

**例 2.2.1** 单摆的周期 $T$ 可能依赖于摆长 $l$、摆球质量 $m$ 与重力加速度 $g$。设 $T = C\,l^{a}m^{b}g^{c}$（$C$ 为量纲一的常数），比较量纲：$\mathsf{T} = \mathsf{L}^{a + c}\,\mathsf{M}^{b}\,\mathsf{T}^{-2c}$，得 $b = 0$，$c = -\frac12$，$a = \frac12$，即

$$
T = C\sqrt{\frac{l}{g}}.
$$
周期与质量无关。常数 $C = 2\pi$（小振幅时）要由动力学求出（[5.1.6](/5.1.6)）；量纲分析也不能判断周期是否依赖于量纲一的振幅角。

## 2.3. 常见的几种力

1. 重力：地面附近质量为 $m$ 的物体所受的重力为 $m\boldsymbol{g}$。严格地说，重力是地球引力与地球自转引起的惯性离心力的合力（例 2.6.4）。
2. 弹力：物体形变后企图恢复原状而对接触物体产生的力，包括正压力（支持力）$F_{\mathrm{N}}$、绳的张力 $F_{\mathrm{T}}$ 与弹簧的弹力。在弹性限度内，弹簧的弹力满足 Hooke 定律 $F = -k\,\Delta x$，$k$ 为劲度系数，$\Delta x$ 为伸长量。
3. 摩擦力：相互接触的物体之间阻碍相对运动或相对运动趋势的力。静摩擦力的大小由其他力和运动状态决定，最大值为 $\mu_{\mathrm{s}}F_{\mathrm{N}}$；滑动摩擦力 $F_{\mathrm{f}} = \mu_{\mathrm{k}}F_{\mathrm{N}}$，通常 $\mu_{\mathrm{k}} < \mu_{\mathrm{s}}$。
4. 流体阻力（拖曳力）：物体在流体中运动时受到的与**相对速度**反向的力。速率很低时阻力与速率成正比（半径为 $r$ 的小球在黏度为 $\eta$ 的流体中，Stokes 公式 $F = 6\pi\eta rv$）；速率较高时近似与速率的平方成正比，$F = \frac12 C\rho Av^2$，其中 $\rho$ 是流体密度，$A$ 是物体的迎风面积，$C$ 是量纲一的阻力系数。
5. 表面张力：液体表面层中相邻两部分之间的拉力，作用在表面内、垂直于分界线，大小与分界线长度 $l$ 成正比，$F = \gamma l$，$\gamma$ 为表面张力系数（单位 $\mathrm{N\,m^{-1}}$）。液膜有两个表面，拉力为 $2\gamma l$。

除重力外，这些宏观的力都来源于原子、分子之间的电磁相互作用。固体的剪切与扭转形变产生的力见 [5.1.7](/5.1.7) 的弹性形变。

## 2.4. 四种基本相互作用

**定义 2.4.1（基本相互作用）** 迄今所知，自然界的一切相互作用都可以归结为四种**基本相互作用**：引力相互作用、电磁相互作用、弱相互作用和强相互作用。

| 相互作用 | 相对强度（数量级） | 力程 | 传递者 | 例子 |
|---|---|---|---|---|
| 强相互作用 | $1$ | $\sim10^{-15}\,\mathrm{m}$ | 胶子 | 把夸克束缚成质子、中子；核力是它的剩余作用 |
| 电磁相互作用 | $10^{-2}$ | 无限远 | 光子 | 原子与分子的结构，弹力、摩擦力等宏观力 |
| 弱相互作用 | $10^{-6}$ | $\sim10^{-18}\,\mathrm{m}$ | $\mathrm{W}^{\pm}$、$\mathrm{Z}^0$ 玻色子 | $\beta$ 衰变，太阳中的核聚变 |
| 引力相互作用 | $10^{-39}$ | 无限远 | （假想的引力子） | 重力，天体运动 |

相对强度依赖于比较的方式和粒子的能量，表中只是低能下的数量级。引力在四种相互作用中最弱，却支配着天体的运动，因为它只有吸引、没有屏蔽，而宏观物体的正负电荷几乎完全抵消。电磁相互作用与弱相互作用在高能下统一为电弱相互作用（Glashow、Weinberg、Salam）。在广义相对论中，引力被理解为时空弯曲的效应（2.6.3 节）。

## 2.5. Newton 定律应用举例

用 Newton 定律解题的一般步骤是：

1. 选对象：确定研究哪个物体，必要时把它从周围隔离出来（隔离体）；
2. 看运动：分析它的运动状态，写出加速度（[5.1.1](/5.1.1) 的**运动学**）；
3. 查受力：画出它所受的全部外力；
4. 列方程：在选定的坐标系中写出 Newton 第二定律的分量式，常常还要补充运动学关系或几何约束；
5. 验结果：检查量纲、特殊情形与变化趋势是否合理。

**例 2.5.1（肥皂泡内外的压强差）** 半径为 $R$ 的球形肥皂泡，肥皂液的表面张力系数为 $\gamma$，求泡内压强 $p_{\mathrm{in}}$ 比外部大气压 $p_0$ 大多少。

取右半个肥皂泡为研究对象，它在水平方向受三个力：泡外大气的压力 $F_{\mathrm{ext}}$（向左）、泡内气体的压力 $F_{\mathrm{in}}$（向右）、左半球通过分界圆对它的表面张力 $F_{\mathrm{surf}}$（向左）。由对称性，压力的竖直分量抵消。取球面上的面积元 $\mathrm{d}S = R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$（$\theta$ 从水平轴量起），其上压力的水平分量为 $p\cos\theta\,\mathrm{d}S$，积分得

$$
F_{\mathrm{ext}} = \int p_0\cos\theta\,\mathrm{d}S = p_0\,\pi R^2, \qquad F_{\mathrm{in}} = p_{\mathrm{in}}\,\pi R^2,
$$
即均匀压强对曲面的合力等于压强乘以曲面在垂直方向上的投影面积。肥皂膜有内外两个表面，$F_{\mathrm{surf}} = 2\gamma\cdot2\pi R$。平衡时 $F_{\mathrm{in}} = F_{\mathrm{ext}} + F_{\mathrm{surf}}$，所以

$$
p_{\mathrm{in}} - p_0 = \frac{4\gamma}{R}.
$$
液滴只有一个表面，内外压强差为 $2\gamma/R$（Laplace 公式）。泡越小，内部压强越大：两个大小不同的肥皂泡连通后，小泡会缩小，大泡会胀大。

**例 2.5.2（旋转水桶）** 圆桶绕竖直的对称轴以恒定**角速度** $\omega$ 转动，桶内的水相对桶静止。求水面的形状。

1. 选对象：水面上任一小块质量为 $m$ 的水，它到转轴的距离为 $r$。
2. 看运动：它做匀速圆周运动，加速度 $\omega^2 r$ 指向转轴。
3. 查受力：重力 $mg$；其余的水对它的压力 $F_{\mathrm{N}}$，垂直于水面。设水面的法线与竖直方向成 $\theta$ 角。
4. 列方程：

$$
F_{\mathrm{N}}\cos\theta - mg = 0, \qquad F_{\mathrm{N}}\sin\theta = m\omega^2 r,
$$
补充几何关系：水面的斜率 $\dfrac{\mathrm{d}z}{\mathrm{d}r} = \tan\theta$。三式联立得 $\dfrac{\mathrm{d}z}{\mathrm{d}r} = \dfrac{\omega^2}{g}r$，这是一个**变量分离方程**，积分得

$$
z = \frac{\omega^2}{2g}r^2 + z_0,
$$
水面是旋转抛物面，$z_0$ 是轴线上的水面高度。设不转动时水深为 $h$、桶的半径为 $R$，由水的体积不变 $\int_0^R z\cdot2\pi r\,\mathrm{d}r = \pi R^2h$ 得 $z_0 = h - \dfrac{\omega^2R^2}{4g}$。

5. 验结果：$\dim\dfrac{\omega^2r^2}{g} = \dfrac{\mathsf{T}^{-2}\mathsf{L}^2}{\mathsf{L}\,\mathsf{T}^{-2}} = \mathsf{L}$，与 $z$ 一致；$\omega = 0$ 时 $z = h$，水面水平；$\omega$ 越大，中心越低、边缘越高。

这个例子说明，除动力学方程外，常常还需要补充运动学方程或几何约束方程（这里是水面斜率与法线方向的关系）。

**例 2.5.3（收尾速率）** 质量为 $m$ 的物体从静止开始在空气中竖直下落。

若阻力与速率成正比，$F = bv$，取向下为正，$m\dfrac{\mathrm{d}v}{\mathrm{d}t} = mg - bv$。这是一阶**线性微分方程**（[2.2.15](/2.2.15)），满足 $v(0) = 0$ 的解为

$$
v(t) = v_{\mathrm{T}}\left(1 - \mathrm{e}^{-t/\tau}\right), \qquad v_{\mathrm{T}} = \frac{mg}{b}, \qquad \tau = \frac{m}{b} = \frac{v_{\mathrm{T}}}{g}.
$$
若阻力与速率的平方成正比，$F = \frac12C\rho Av^2$，方程 $m\dfrac{\mathrm{d}v}{\mathrm{d}t} = mg - \frac12C\rho Av^2$ 是**变量分离方程**，解为

$$
v(t) = v_{\mathrm{T}}\tanh\frac{gt}{v_{\mathrm{T}}}, \qquad v_{\mathrm{T}} = \sqrt{\frac{2mg}{C\rho A}}.
$$
两种情形下速率都单调增大并趋于极限值 $v_{\mathrm{T}}$，此时阻力与重力平衡，物体匀速下落。这个极限速率称为收尾速率（terminal velocity）。由 $v_{\mathrm{T}}$ 的表达式，同样形状的物体越大，收尾速率越大：$m \propto r^3$，$A \propto r^2$，所以 $v_{\mathrm{T}} \propto \sqrt{r}$。

抛体同时受重力与平方阻力时，两个分量的方程通过 $\lvert\boldsymbol{v}\rvert$ 耦合在一起，没有初等解，可以用 `scipy.integrate.solve_ivp` 数值求解（[4.4.4](/4.4.4) 的初值问题）。

![左：从静止下落的物体在线性阻力与平方阻力下的速率，横轴为 $gt/v_{\mathrm{T}}$，两者都趋于收尾速率。右：以 $50\,\mathrm{m\,s^{-1}}$、$45^\circ$ 抛出的物体在不同收尾速率（即不同的阻力大小）下的数值轨迹；阻力使射程变短，轨迹不再对称，下降段比上升段陡](./plots/air-resistance.py)

## 2.6. 非惯性系中的动力学问题

### 2.6.1. 惯性系的近似性

Newton 定律只在惯性系中成立。在相对地面加速的车厢里，光滑桌面上的小球不受水平力，却相对车厢向后加速：车厢参考系中 Newton 定律不成立。

自然界中并不存在严格的惯性系，常用的参考系都有加速度：

| 参考系 | 加速度的来源 | 加速度的量级 |
|---|---|---|
| 地面参考系 | 地球自转（赤道处） | $3.4\times10^{-2}\,\mathrm{m\,s^{-2}}$ |
| 地心参考系 | 地球绕太阳公转 | $6\times10^{-3}\,\mathrm{m\,s^{-2}}$ |
| 太阳参考系 | 太阳绕银河系中心运动 | $2\times10^{-10}\,\mathrm{m\,s^{-2}}$ |

所以，一个参考系能否当作惯性系取决于问题要求的精度。为了在加速的参考系中也能使用 Newton 定律，需要对它加以修正。

### 2.6.2. 平动非惯性系与惯性力

设 $S$ 是惯性系，$S'$ 相对 $S$ **平动**，加速度为 $\boldsymbol{a}_0$。质点在 $S$ 中满足 $\boldsymbol{F} = m\boldsymbol{a}$。由 Galilei 变换（[5.1.1](/5.1.1#thm-1.7.1)），质点在 $S'$ 中的加速度 $\boldsymbol{a}' = \boldsymbol{a} - \boldsymbol{a}_0$；力与质量不随参考系改变，所以 $\boldsymbol{F} \ne m\boldsymbol{a}'$。但

$$
\boldsymbol{F} = m\boldsymbol{a} = m\boldsymbol{a}' + m\boldsymbol{a}_0 \quad\Longrightarrow\quad \boldsymbol{F} - m\boldsymbol{a}_0 = m\boldsymbol{a}'.
$$

**定义 2.6.1（惯性力）** 在加速度为 $\boldsymbol{a}_0$ 的平动非惯性系中，对质量为 $m$ 的质点引入

$$
\boldsymbol{F}_{\mathrm{in}} = -m\boldsymbol{a}_0,
$$
称为平移**惯性力**。于是在该参考系中 $\boldsymbol{F} + \boldsymbol{F}_{\mathrm{in}} = m\boldsymbol{a}'$，Newton 第二定律形式上成立。

惯性力是由于参考系本身的加速运动而引入的附加力，本质上是物体惯性的表现。它不是物体之间的相互作用，找不到施力物体，也没有反作用力，但在非惯性系中有真实的效果：急刹车时乘客前倾，在惯性力的语言中就是受到向前的惯性力。

### 2.6.3. 等效原理

平移惯性力 $-m\boldsymbol{a}_0$ 与质量成正比，这一点与重力完全相同。在远离天体、以加速度 $\boldsymbol{a}_0 = -\boldsymbol{g}$ 加速的飞船中，一切物体都"受到"惯性力 $m\boldsymbol{g}$，与在地面上静止的飞船中受到重力 $m\boldsymbol{g}$ 无法区分；反过来，在引力场中自由下落的飞船里，引力与惯性力抵消，一切物体都处于失重状态，与在远离天体的惯性系中无法区分。

这种不可区分性的前提是惯性质量（第二定律中的 $m$）等于引力质量（万有引力定律中的 $m$）。从 Eötvös 的扭秤实验到 2017–2022 年的 MICROSCOPE 卫星实验，两者之比与 1 的相对偏差被限制在 $10^{-15}$ 的量级以下。Einstein 把它提升为一条原理：在足够小的时空区域内，均匀引力场与匀加速参考系的物理效应完全等价。这称为等效原理（equivalence principle），它是广义相对论的出发点。

**例 2.6.1** 车厢以加速度 $\boldsymbol{a}_0$ 水平加速，车厢中挂一个摆长为 $l$ 的单摆。在车厢参考系中，摆球受重力 $m\boldsymbol{g}$、绳的张力与惯性力 $-m\boldsymbol{a}_0$。重力与惯性力的合力相当于一个"等效重力" $m\boldsymbol{g}_{\mathrm{eff}} = m(\boldsymbol{g} - \boldsymbol{a}_0)$，大小 $mg_{\mathrm{eff}} = m\sqrt{g^2 + a_0^2}$。所以摆的平衡位置向后偏离竖直方向

$$
\theta = \arctan\frac{a_0}{g},
$$
小振幅振动的周期由 $2\pi\sqrt{l/g}$ 变为

$$
T = 2\pi\sqrt{\frac{l}{\sqrt{g^2 + a_0^2}}}.
$$

**例 2.6.2（失重）** 一个质量为 $M$ 的箱子竖直自由下落，箱内用长为 $l$ 的轻绳挂一个质量为 $m$ 的小球（$M \gg m$，小球不影响箱子的运动）。箱子自由下落时，在箱子参考系中小球受到的惯性力 $-m\boldsymbol{g}$ 与重力抵消，只受绳的张力。若释放时小球相对箱子有垂直于绳的**速度** $v$，它将以绳的悬点为圆心做速率为 $v$ 的匀速圆周运动，张力 $mv^2/l$ 提供向心力；若相对箱子静止，它就一直静止。在地面上看，小球的运动是这个匀速圆周运动与箱子的自由落体的叠加。

**例 2.6.3** 质量为 $M$、倾角为 $\theta$ 的楔块放在光滑水平面上，质量为 $m$ 的物块沿楔块的光滑斜面下滑。求楔块的加速度。

设物块对楔块的压力为 $F'_{\mathrm{N}}$，它垂直于斜面，其水平分量推动楔块：

$$
Ma_M = F'_{\mathrm{N}}\sin\theta.
$$
在楔块参考系中分析物块：它受重力 $mg$、斜面的支持力 $F_{\mathrm{N}} = F'_{\mathrm{N}}$ 与惯性力 $ma_M$（水平，背离楔块的运动方向）。物块沿斜面运动，在斜面法向上没有加速度：

$$
F_{\mathrm{N}} + ma_M\sin\theta - mg\cos\theta = 0.
$$
两式联立解得

$$
a_M = \frac{g\sin\theta\cos\theta}{M/m + \sin^2\theta}.
$$
检验：$M \to \infty$ 时 $a_M \to 0$，楔块不动；$\theta \to 0$ 或 $\theta \to \pi/2$ 时 $a_M \to 0$，也都合理。在楔块参考系中处理，避免了直接写出物块在地面参考系中复杂的加速度。

### 2.6.4. 潮汐

海水每天两次涨落。为什么向着月球和背着月球的两侧同时涨潮？为什么月球的作用比质量大得多的太阳还大？

以地心为原点、随地心平动的参考系（地心参考系）在月球的引力作用下有加速度 $\boldsymbol{a}_0$，它等于月球在地心处产生的引力加速度。在这个参考系中，地球上质量为 $m$ 的海水除受地球引力外，还受月球的引力与惯性力 $-m\boldsymbol{a}_0$。月球的引力随距离减小，在地球上各处的大小和方向不同，而惯性力处处相同：

- 在向月的一侧，月球引力大于地心处的值，合力背离地心指向月球；
- 在背月的一侧，月球引力小于地心处的值，合力指向背离月球的方向，同样背离地心；
- 在与月地连线垂直的两侧，两者的合力指向地心。

这个由引力分布不均匀产生的剩余力称为引潮力。它使海面在月地连线的两端隆起、在两侧下陷，地球自转一周，某一地点就经历两次高潮、两次低潮。在连线方向上，距地心 $R$ 处的引潮加速度约为 $\dfrac{2GM_{\mathrm{M}}R}{r^3}$（$M_{\mathrm{M}}$ 为月球质量，$r$ 为月地距离），与 $r^3$ 成反比，而不是像引力那样与 $r^2$ 成反比。按平衡潮理论（假定海水有足够的时间达到平衡），高潮与低潮的高度差为

$$
\Delta h = \frac32\,\frac{M}{M_{\mathrm{E}}}\left(\frac{R_{\mathrm{E}}}{r}\right)^3R_{\mathrm{E}},
$$
其中 $M$、$r$ 是天体的质量和它到地心的距离，$M_{\mathrm{E}}$、$R_{\mathrm{E}}$ 是地球的质量和半径。代入数据，月球引起的 $\Delta h_{\mathrm{M}} \approx 0.54\,\mathrm{m}$，太阳引起的 $\Delta h_{\mathrm{S}} \approx 0.25\,\mathrm{m}$：太阳的质量是月球的 $2.7\times10^7$ 倍，但距离是月球的约 390 倍，三次方之后月球的作用约为太阳的 2.2 倍。

两者的效果按相对方位叠加。新月和满月时（农历初一、十五前后），太阳、地球、月球几乎在一条直线上，两者的隆起方向一致，形成大潮；上弦、下弦时两者的隆起方向相互垂直，部分抵消，形成小潮。实际的潮差还受海岸与海底地形的强烈影响：钱塘江口的涌潮、加拿大芬迪湾的潮差（可达约 $16\,\mathrm{m}$）都远大于平衡潮的估计，这是海湾形状对潮波的放大作用。潮汐应力对少数已处于临界状态的断层的触发作用有研究报道，但它不能用来预报地震。

### 2.6.5. 匀速转动参考系中的惯性离心力

设 $S'$ 系相对惯性系 $S$ 以恒定角速度 $\boldsymbol{\omega}$ 绕固定轴转动。先考虑在 $S'$ 中静止的质点，它到转轴的距离为 $r$。在 $S$ 中它做匀速圆周运动，所受合力 $\boldsymbol{f}$ 提供**向心加速度**：$\boldsymbol{f} = -m\omega^2\boldsymbol{r}_\perp$，$\boldsymbol{r}_\perp$ 是从转轴垂直指向质点的矢量。在 $S'$ 中质点静止，$\boldsymbol{a}' = \boldsymbol{0}$，但 $\boldsymbol{f} \ne \boldsymbol{0}$。

**定义 2.6.2（惯性离心力）** 在以角速度 $\boldsymbol{\omega}$ 匀速转动的参考系中，对质量为 $m$ 的质点引入

$$
\boldsymbol{F}_{\mathrm{cf}} = m\omega^2\boldsymbol{r}_\perp = -m\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}),
$$
称为**惯性离心力**，其中 $\boldsymbol{r}$ 是质点相对转轴上一点的**位矢**。

于是 $\boldsymbol{f} + \boldsymbol{F}_{\mathrm{cf}} = \boldsymbol{0} = m\boldsymbol{a}'$：在 $S'$ 中看，质点所受的真实的力与惯性离心力平衡，所以静止。惯性离心力不是向心力的反作用力：向心力的反作用力作用在施力物体上，而惯性离心力作用在质点本身。

**例 2.6.4（重力加速度与纬度）** 以随地球自转的地面为参考系，地面上的物体除受地球引力 $\boldsymbol{F}_{\mathrm{g}}$ 外，还受惯性离心力 $m\omega^2R\cos\varphi$，方向垂直于地轴向外（$R$ 为地球半径，$\varphi$ 为纬度，$\omega$ 为地球自转角速度）。我们称为重力的，是两者的合力。把地球看作均匀球体，引力加速度 $g_0 = \dfrac{GM_{\mathrm{E}}}{R^2} \approx 9.83\,\mathrm{m\,s^{-2}}$，而 $a_0 = R\omega^2 \approx 0.034\,\mathrm{m\,s^{-2}} \ll g_0$。离心加速度在指向地心方向上的分量为 $a_0\cos^2\varphi$，精确到 $a_0/g_0$ 的一阶，

$$
g \approx g_0\left(1 - \frac{a_0}{g_0}\cos^2\varphi\right) = g_0 - a_0\cos^2\varphi.
$$
赤道上 $g$ 最小，两极最大。重力的方向（铅垂线）也稍稍偏离地心方向，在纬度 $45^\circ$ 处偏离最大，约 $0.1^\circ$。实测的赤道与两极的差值（约 $9.780$ 与 $9.832\,\mathrm{m\,s^{-2}}$，相差 $0.052\,\mathrm{m\,s^{-2}}$）比 $a_0$ 大，其余部分来自地球的扁率：赤道处离地心更远。

### 2.6.6. Coriolis 力

质点相对转动参考系运动时，仅有惯性离心力还不够。先看一个特例：转盘以恒定角速度 $\omega$ 逆时针转动，盘上有一个以转轴为圆心、半径为 $r$ 的光滑圆形凹槽，质点在槽内以相对速率 $v'$ 沿转动方向做匀速圆周运动。在惯性系 $S$ 中，质点的速率为 $v' + \omega r$，槽壁对它的指向圆心的力为

$$
F = m\frac{(v' + \omega r)^2}{r} = m\frac{v'^2}{r} + 2mv'\omega + m\omega^2r.
$$
在转动系 $S'$ 中，质点做速率为 $v'$ 的匀速圆周运动，向心加速度为 $a' = v'^2/r$。所以 $F - 2mv'\omega - m\omega^2r = ma'$：在 $S'$ 中，除惯性离心力 $m\omega^2r$ 外，还有一个背离圆心、大小为 $2mv'\omega$ 的惯性力。

一般地，在转动参考系中观察到的矢量变化率与惯性系中的不同。设 $\boldsymbol{A}$ 是任一矢量，在 $S'$ 中把它按 $S'$ 的坐标轴分解，$S'$ 中的观察者只看到分量的变化 $\left(\dfrac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t}\right)_{S'}$；在 $S$ 中，$S'$ 的坐标轴本身以角速度 $\boldsymbol{\omega}$ 转动，单位矢量的变化率为 $\boldsymbol{\omega}\times\boldsymbol{e}'_i$（[5.1.1](/5.1.1) 的 1.5.2 节），所以

$$
\left(\frac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t}\right)_S = \left(\frac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t}\right)_{S'} + \boldsymbol{\omega}\times\boldsymbol{A}.
$$

**定理 2.6.1（转动参考系中的加速度变换）** 设 $S'$ 相对惯性系 $S$ 以恒定角速度 $\boldsymbol{\omega}$ 绕过原点的固定轴转动，质点在 $S'$ 中的位矢、速度、加速度分别为 $\boldsymbol{r}$、$\boldsymbol{v}'$、$\boldsymbol{a}'$，则它在 $S$ 中的速度与加速度为

$$
\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{r}, \qquad
\boldsymbol{a} = \boldsymbol{a}' + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}) + 2\boldsymbol{\omega}\times\boldsymbol{v}'.
$$

**证明** 对 $\boldsymbol{A} = \boldsymbol{r}$ 应用上面的关系，得 $\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{r}$。再对 $\boldsymbol{A} = \boldsymbol{v}$ 应用一次，$\boldsymbol{\omega}$ 为常矢量：

$$
\boldsymbol{a} = \left(\frac{\mathrm{d}}{\mathrm{d}t}\right)_{S'}(\boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{r}) + \boldsymbol{\omega}\times(\boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{r})
= \boldsymbol{a}' + \boldsymbol{\omega}\times\boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{v}' + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}). \quad\square
$$

三项的名称是：$\boldsymbol{a}$ 为绝对加速度，$\boldsymbol{a}'$ 为相对加速度，$\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r})$ 为牵连加速度（$S'$ 中与质点重合的点的向心加速度），$2\boldsymbol{\omega}\times\boldsymbol{v}'$ 称为 Coriolis 加速度（Coriolis acceleration）。它只在质点相对转动参考系运动时出现，正是 [5.1.1](/5.1.1) 中预告的、平动参考系之间的变换所没有的一项。把定理乘以 $m$ 并移项，就得到转动参考系中的动力学方程：

**定义 2.6.3（Coriolis 力）** 质量为 $m$ 的质点以速度 $\boldsymbol{v}'$ 相对以角速度 $\boldsymbol{\omega}$ 匀速转动的参考系运动时，在该参考系中引入的惯性力

$$
\boldsymbol{F}_{\mathrm{C}} = 2m\boldsymbol{v}'\times\boldsymbol{\omega} = -2m\boldsymbol{\omega}\times\boldsymbol{v}'
$$
称为 **Coriolis 力**。在转动参考系中，

$$
\boldsymbol{F} + m\omega^2\boldsymbol{r}_\perp + 2m\boldsymbol{v}'\times\boldsymbol{\omega} = m\boldsymbol{a}'.
$$

Coriolis 力垂直于相对速度，所以它只改变运动的方向、不做功。在前面的凹槽特例中，$\boldsymbol{v}'$ 沿转动方向，$2m\boldsymbol{v}'\times\boldsymbol{\omega}$ 背离圆心，大小 $2mv'\omega$，与直接计算的结果一致。

![光滑转盘上滑动的小物块。左：在惯性系中它沿直线运动；右：在逆时针转动的转盘上看，轨迹向右弯曲，这是惯性离心力与 Coriolis 力共同作用的结果](./plots/coriolis-deflection.py)

地球是一个转动参考系，$\omega = 7.29\times10^{-5}\,\mathrm{rad\,s^{-1}}$。Coriolis 力虽小，在大尺度或长时间的运动中效果显著：

- 北半球水平运动的物体受到指向运动方向右侧的 Coriolis 力，南半球指向左侧。
- 赤道附近的信风：从副热带流向赤道的气流在北半球偏右成为东北信风，在南半球偏左成为东南信风。
- 热带气旋：气流向低压中心汇聚时向右偏转，所以北半球的台风逆时针旋转，南半球的气旋顺时针旋转。浴缸排水的旋转方向则主要由初始扰动和容器形状决定，Coriolis 力的影响微不足道。
- 落体偏东：竖直下落的物体受到向东的 Coriolis 力（例 2.6.5）。
- 北半球河流右岸冲刷较重、双轨铁路右侧的钢轨磨损较多，也常被归于 Coriolis 力，但这些效应很小，往往被其他因素掩盖。

**例 2.6.5（落体偏东）** 在纬度 $\varphi$ 处，物体从高 $h$ 处由静止自由下落，忽略空气阻力。取当地坐标：$x$ 轴向东，$y$ 轴向北，$z$ 轴竖直向上，则 $\boldsymbol{\omega} = \omega(\cos\varphi\,\boldsymbol{e}_y + \sin\varphi\,\boldsymbol{e}_z)$。Coriolis 力远小于重力，作为一级近似，取 $\boldsymbol{v}' \approx -gt\,\boldsymbol{e}_z$，

$$
-2\boldsymbol{\omega}\times\boldsymbol{v}' = 2\omega gt\cos\varphi\,(\boldsymbol{e}_y\times\boldsymbol{e}_z) = 2\omega gt\cos\varphi\,\boldsymbol{e}_x,
$$
即 Coriolis 加速度向东。积分两次得落地时的偏东距离

$$
x = \frac13\omega gt^3\cos\varphi = \frac13\omega\cos\varphi\sqrt{\frac{8h^3}{g}}.
$$
$h = 100\,\mathrm{m}$、$\varphi = 40^\circ$ 时 $x \approx 1.7\,\mathrm{cm}$。在惯性系中看，这是因为高处的物体随地球自转的线速度比地面大，落下时就"跑"到了地面上起点的东边。

**例 2.6.6（Foucault 摆）** 1851 年，Foucault 在巴黎用长 $67\,\mathrm{m}$ 的单摆演示了地球的自转：摆动平面相对地面缓慢地顺时针转动（北半球，从上往下看）。在惯性系中，摆动平面的方向保持不变（只受重力与张力，都在摆动平面内），是地面在它下面转动。在纬度 $\varphi$ 处，地球自转角速度沿当地竖直方向的分量为 $\omega\sin\varphi$，所以摆动平面转动一周的时间为

$$
T = \frac{T_0}{\sin\varphi},
$$
$T_0 \approx 23.93\,\mathrm{h}$ 是地球相对恒星自转一周的时间（恒星日）。巴黎（$\varphi \approx 48.9^\circ$）$T \approx 31.8\,\mathrm{h}$，北京（$\varphi \approx 39.9^\circ$）$T \approx 37.3\,\mathrm{h}$，两极 $T = T_0$，赤道上摆动平面不转。在地面参考系中，这是摆球所受的 Coriolis 力水平分量使摆动平面偏转的结果。

## 小结

| 内容 | 要点 |
|---|---|
| Newton 运动定律 | 第一定律给出惯性与力的概念、定义惯性系；第二定律 $\boldsymbol{F} = \dfrac{\mathrm{d}(m\boldsymbol{v})}{\mathrm{d}t}$；第三定律 $\boldsymbol{F}_{12} = -\boldsymbol{F}_{21}$ |
| 单位与量纲 | 2019 年 SI 由 7 个定义常数确定；$\dim F = \mathsf{L}\,\mathsf{M}\,\mathsf{T}^{-2}$，方程两边量纲必须一致 |
| 解题步骤 | 选对象、看运动、查受力、列方程、验结果 |
| 平动非惯性系 | 惯性力 $\boldsymbol{F}_{\mathrm{in}} = -m\boldsymbol{a}_0$；等效原理 |
| 转动参考系 | 惯性离心力 $m\omega^2\boldsymbol{r}_\perp$，Coriolis 力 $2m\boldsymbol{v}'\times\boldsymbol{\omega}$；$\boldsymbol{a} = \boldsymbol{a}' + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}) + 2\boldsymbol{\omega}\times\boldsymbol{v}'$ |

## 思考题

1. 用水平力 $F$ 把物体压在粗糙的竖直墙面上并保持静止。$F$ 逐渐增大时，物体所受的静摩擦力怎样变化？
   提示：不变，始终等于物体的重力。静摩擦力由平衡条件决定，$F$ 增大的只是最大静摩擦力 $\mu_{\mathrm{s}}F$。
2. 一根有质量的弹簧上端用绳挂起，处于平衡。弹簧各段的伸长是否相同？把绳剪断的瞬间，弹簧怎样运动？
   提示：越靠上的一段要承受下面越多的重量，伸长越大。剪断的瞬间，弹簧各处的形变来不及改变，下端所受的弹力仍与重力平衡而保持静止，上端则受向下的弹力与重力，加速度大于 $g$；弹簧从上端开始收缩，而整个弹簧质心的加速度始终是 $g$（[5.1.3](/5.1.3) 的质心运动定理）。
3. 太阳和月球引起的潮汐哪个更大？
   提示：月球。引潮力与天体质量成正比、与距离的三次方成反比（2.6.4 节）。
