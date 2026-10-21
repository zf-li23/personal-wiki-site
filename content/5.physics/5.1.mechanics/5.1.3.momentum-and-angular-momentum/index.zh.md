---
title: 动量与角动量
description: 冲量与动量定理；质点系的动量定理与动量守恒定律；变质量系统与火箭方程；质心与质心运动定理，质心系；质点与质点系的角动量、力矩与角动量定理，角动量守恒定律与 Kepler 第二定律；质心系中的角动量定理。
---

**Newton 第二定律**（[5.1.2](/5.1.2)）是力与**加速度**之间的瞬时关系。很多问题中我们并不关心每一时刻的受力，而关心力在一段时间内积累的效果：力对时间的积累改变物体的动量，力矩对时间的积累改变物体的角动量。本章由 Newton 定律导出动量定理与角动量定理，并把它们推广到**质点**系。质点系的内力成对出现，在求和时相互抵消，于是得到两条守恒定律：不受外力的系统动量守恒，不受外力矩的系统角动量守恒。它们比 Newton 定律适用得更广，在相对论（[5.1.8](/5.1.8)）与量子物理（[5.5](/5.5)）中依然成立；按照 Noether 定理，它们分别对应空间的平移对称性与转动对称性（[5.1.4](/5.1.4)）。**质心**（[2.2.12](/2.2.12#def-12.5.1)）是本章的另一个核心概念：质点系的整体运动像一个位于质心、集中了全部质量的质点。下一章 [5.1.4](/5.1.4) 讨论力对空间的积累（功）与能量，[5.1.5](/5.1.5) 把本章的角动量定理用于刚体。

## 3.1. 冲量、动量与质点动量定理

### 3.1.1. 动量定理

**定义 3.1.1（冲量）** 力 $\boldsymbol{F}$ 在时间 $t_1$ 到 $t_2$ 内对时间的积分

$$
\boldsymbol{I} = \int_{t_1}^{t_2}\boldsymbol{F}\,\mathrm{d}t
$$
称为这段时间内力的**冲量**。

**定义 3.1.2（动量）** 质量为 $m$、**速度**为 $\boldsymbol{v}$ 的质点的**动量**为 $\boldsymbol{p} = m\boldsymbol{v}$，单位是 $\mathrm{kg\,m\,s^{-1}}$。

**定理 3.1.1（质点动量定理）** 质点所受合力的冲量等于质点动量的增量：

$$
\boldsymbol{F} = \frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}t}, \qquad \mathrm{d}\boldsymbol{I} = \boldsymbol{F}\,\mathrm{d}t = \mathrm{d}\boldsymbol{p}, \qquad
\boldsymbol{I} = \int_{t_1}^{t_2}\boldsymbol{F}\,\mathrm{d}t = \boldsymbol{p}_2 - \boldsymbol{p}_1.
$$
前两式是微分形式，最后一式是积分形式。

微分形式就是 Newton 第二定律的原始形式（[5.1.2](/5.1.2#thm-2.1.2)）。积分形式的好处在于：碰撞、打击这类过程中，力在极短的时间内急剧变化，难以测量，但动量的变化容易测量。定义平均冲力

$$
\bar{\boldsymbol{F}} = \frac{1}{t_2 - t_1}\int_{t_1}^{t_2}\boldsymbol{F}\,\mathrm{d}t = \frac{\Delta\boldsymbol{p}}{\Delta t},
$$
同样的动量变化，作用时间越短，平均冲力越大。跳远落在沙坑里、包装中垫泡沫，都是延长作用时间以减小冲力。

**例 3.1.1** 质量 $m = 0.58\,\mathrm{kg}$ 的篮球从 $h = 2\,\mathrm{m}$ 高处自由下落，触地后以同样的**速率**反弹，触地时间 $\Delta t = 0.019\,\mathrm{s}$。求篮球对地面的平均冲力。

篮球触地时的速率 $v = \sqrt{2gh} = \sqrt{2\times9.80\times2}\,\mathrm{m\,s^{-1}} = 6.26\,\mathrm{m\,s^{-1}}$，触地前后动量的变化量大小为 $2mv$。忽略触地期间的重力（约 $5.7\,\mathrm{N}$），

$$
\bar F = \frac{2mv}{\Delta t} = \frac{2\times0.58\times6.26}{0.019}\,\mathrm{N} \approx 3.8\times10^2\,\mathrm{N},
$$
约为篮球重力的 67 倍。由 **Newton 第三定律**，篮球对地面的平均冲力与此等值反向。

**例 3.1.2** 一个重球的上下两面各系一根同样的细线，用上面的线把球吊起，用手向下拉下面的线。缓慢地加力时，上面的线先断：它的张力等于球的重力加上拉力，总比下面的线大。猛地一拉时，下面的线先断：作用时间极短，冲量很小，球几乎来不及运动，上面的线的伸长（因而张力）几乎不变，而下面的线的张力在这极短的时间内已经达到断裂强度。哪根线先断取决于拉力的大小与快慢，而不只取决于两者的乘积。

**例 3.1.3（逆风行舟）** 帆船能够斜着逆风航行。从上往下看，风吹到斜置的帆上后沿帆面偏转流走，风的动量改变了 $\Delta\boldsymbol{p}$；由动量定理，帆对风的作用力与 $\Delta\boldsymbol{p}$ 同向，于是风对帆的作用力与之反向，大致垂直于帆面。把这个力分解为沿船身的分量与垂直于船身的分量：前者推船前进，后者被水对船底龙骨的横向阻力平衡。只要帆的方位合适，沿船身的分量就指向前方，船可以与风向成一定角度逆风前进，再以"之"字形航线到达上风处。

### 3.1.2. 光压与光镊

光也有动量。频率为 $\nu$、波长为 $\lambda$ 的光子的动量为 $p = \dfrac{h\nu}{c} = \dfrac{h}{\lambda}$（[5.5](/5.5)），光被物体吸收、反射或折射时动量发生变化，物体就受到力的作用，这就是光压。日光的光压极小，但聚焦的激光能对微米、纳米尺度的颗粒施加可观的力。

激光束经透明的小颗粒（反射相对很弱）折射后传播方向改变，光的动量改变，颗粒受到反方向的力。对于强度中心高、四周低的聚焦光束，偏离焦点的颗粒所受的合力指向焦点，于是颗粒被"夹"在焦点附近，这就是光镊。用光镊可以捕获和移动细胞、细菌，或者拉伸 DNA 分子测量它的弹性。Ashkin 因发明光镊及其在生物系统中的应用获得 2018 年 Nobel 物理学奖；用激光冷却和捕获原子的工作获得了 1997 年 Nobel 物理学奖（朱棣文、Cohen-Tannoudji、Phillips）。

## 3.2. 质点系动量定理

由相互作用的若干个质点组成的系统称为质点系。系统外的物体对系统内质点的作用力称为外力，系统内质点之间的相互作用力称为内力。

设质点 $i$ 受外力 $\boldsymbol{F}_i$，受质点 $j$ 的内力 $\boldsymbol{f}_{ij}$，动量为 $\boldsymbol{p}_i$。对每个质点用动量定理：

$$
\Big(\boldsymbol{F}_i + \sum_{j\ne i}\boldsymbol{f}_{ij}\Big)\,\mathrm{d}t = \mathrm{d}\boldsymbol{p}_i.
$$
对所有质点求和。由 Newton 第三定律 $\boldsymbol{f}_{ij} = -\boldsymbol{f}_{ji}$，内力成对抵消，$\sum_i\sum_{j\ne i}\boldsymbol{f}_{ij} = \boldsymbol{0}$。记合外力 $\boldsymbol{F}_{\mathrm{ext}} = \sum_i\boldsymbol{F}_i$，系统的总动量 $\boldsymbol{P} = \sum_i\boldsymbol{p}_i$，得到：

**定理 3.2.1（质点系动量定理）** 质点系所受合外力的冲量等于系统总动量的增量：

$$
\boldsymbol{F}_{\mathrm{ext}} = \frac{\mathrm{d}\boldsymbol{P}}{\mathrm{d}t}, \qquad \int_{t_1}^{t_2}\boldsymbol{F}_{\mathrm{ext}}\,\mathrm{d}t = \boldsymbol{P}_2 - \boldsymbol{P}_1.
$$

系统的总动量只由外力的冲量决定，与内力无关。内力可以在系统内部转移动量，却不能改变总动量。所以用质点系动量定理处理问题，可以避开往往未知的内力。

## 3.3. 动量守恒定律

**定理 3.3.1（动量守恒定律）** 质点系所受合外力为零时，系统的总动量不随时间改变：

$$
\boldsymbol{F}_{\mathrm{ext}} = \boldsymbol{0} \quad\Longrightarrow\quad \boldsymbol{P} = \sum_i m_i\boldsymbol{v}_i = \text{常矢量}.
$$

几点说明：

1. 在 Newton 力学中，动量守恒定律是 Newton 第二、第三定律的推论。但它的适用范围比 Newton 定律更广：在相对论和量子物理中，在 Newton 第三定律不成立的电磁相互作用中（计入电磁场的动量），动量守恒定律依然成立。它是物理学最基本的定律之一，根源是空间的平移对称性（[5.1.4](/5.1.4)）。
2. 动量定理与动量守恒定律只适用于**惯性系**；动量在某一惯性系中守恒，则在其他一切惯性系中也守恒（各质点的速度都差一个相同的常矢量，总动量差一个常矢量）。
3. 合外力不为零，但它在某个方向上的分量为零时，总动量在该方向上的分量守恒。
4. 外力远小于内力、作用时间又极短时（如碰撞、爆炸），外力的冲量可以忽略，系统的动量近似守恒。
5. 用守恒定律解题时，要明确所选的系统、所研究的过程，并检查守恒的条件。

**例 3.3.1** 质量为 $M$ 的楔块放在光滑水平面上，其斜面的水平宽度为 $d$。质量为 $m$ 的小物块从斜面顶端由静止开始滑下，求它滑到底端时楔块在水平方向移动的距离。斜面是直的、凹的或凸的，结果是否相同？

取物块与楔块为系统。系统在水平方向不受外力，水平动量守恒，且初始为零。设任一时刻物块与楔块的水平速度分别为 $v_x$（向斜面底端的方向为正）与 $-V$，则 $mv_x - MV = 0$。对时间积分，物块与楔块的水平**位移**大小满足 $mX_m = MX_M$；物块相对楔块的水平位移为 $d$，$X_m + X_M = d$，所以

$$
X_M = \frac{m}{m + M}\,d.
$$
这个结果与斜面的形状无关，只要物块与楔块初始的相对位置相同即可。若斜面不光滑，摩擦力是系统的内力，水**平动**量仍然守恒，结果不变（只要物块能滑到底端）；若地面不光滑，系统受到水平外力，水平动量不守恒，结果改变。

## 3.4. 变质量系统与火箭飞行原理

低速情况下的变质量问题有两类：主体的质量因粘附而增加（滚雪球、雨滴在云中下落），或因抛射而减少（火箭）。研究方法都是把主体与它在 $\mathrm{d}t$ 内粘附或抛射的质量合起来作为系统，对这个质量不变的系统应用动量定理。下面以火箭为例。高速情况下的动量与能量见 [5.1.8](/5.1.8)，那里的质量始终是不变质量。

### 3.4.1. 自由空间中的火箭

火箭在远离天体的自由空间中飞行，不受外力。以地面（惯性系）为**参考系**，取时刻 $t$ 的箭体与箭内尚存的燃料为系统，质量为 $m$，速度为 $v$。设燃料燃烧后的气体相对箭体以恒定速率 $u$ 向后喷出。

- 时刻 $t$：系统的动量为 $mv$。
- 时刻 $t + \mathrm{d}t$：喷出的气体质量为 $-\mathrm{d}m > 0$（$\mathrm{d}m < 0$ 是箭体质量的增量），速度为 $v - u$；剩余部分质量为 $m + \mathrm{d}m$，速度为 $v + \mathrm{d}v$。

由动量守恒，

$$
mv = (m + \mathrm{d}m)(v + \mathrm{d}v) + (-\mathrm{d}m)(v - u).
$$
略去二阶小量 $\mathrm{d}m\,\mathrm{d}v$，得 $m\,\mathrm{d}v = -u\,\mathrm{d}m$，这是一个**变量分离方程**。从初始状态（质量 $m_{\mathrm{i}}$，速度 $v_{\mathrm{i}}$）积分到燃料耗尽（质量 $m_{\mathrm{f}}$，速度 $v_{\mathrm{f}}$）：

**公式 3.4.1（Tsiolkovsky 公式）**

$$
v_{\mathrm{f}} = v_{\mathrm{i}} + u\ln\frac{m_{\mathrm{i}}}{m_{\mathrm{f}}} = v_{\mathrm{i}} + u\ln N,
$$
其中 $N = m_{\mathrm{i}}/m_{\mathrm{f}}$ 称为火箭的质量比。

火箭获得的速度增量与燃料燃烧的快慢无关，只取决于喷气速率与质量比。提高末速度有两条途径：

1. 提高喷气速率 $u$：化学火箭中液氢液氧发动机最高，真空中约 $4.5\,\mathrm{km\,s^{-1}}$。
2. 增大质量比 $N$：速度增量只随 $N$ 对数增长，单级火箭一味增大 $N$ 并不合算，因为燃料箱、发动机等结构的质量无法抛掉。所以采用多级火箭，每一级燃料用完就把这一级的壳体抛掉。三级火箭的末速度为

$$
v = u_1\ln N_1 + u_2\ln N_2 + u_3\ln N_3,
$$
$N_k$ 是第 $k$ 级点火时与熄火时的质量之比。

### 3.4.2. 火箭的推力

以 $\mathrm{d}t$ 内喷出的气体（质量 $-\mathrm{d}m$）为研究对象。时刻 $t$ 它随箭体运动，动量为 $-\mathrm{d}m\cdot v$；时刻 $t + \mathrm{d}t$ 速度为 $v - u$，动量为 $-\mathrm{d}m\cdot(v - u)$。由动量定理，箭体对这部分气体的作用力满足

$$
F_{\text{rocket on gas}}\,\mathrm{d}t = -\mathrm{d}m\,(v - u) - (-\mathrm{d}m)\,v = u\,\mathrm{d}m,
$$
即箭体对气体的力向后。由 Newton 第三定律，气体对箭体的推力向前，大小为

$$
F = u\left\lvert\frac{\mathrm{d}m}{\mathrm{d}t}\right\rvert = uq_m,
$$
$q_m$ 是单位时间喷出的燃气质量。推力等于喷气速率与质量流量的乘积。

### 3.4.3. 重力场中的竖直发射

在地面附近竖直发射时，系统受外力 $-mg$（忽略 $g$ 的变化与空气阻力）。对 3.4.1 节的系统用动量定理，$\mathrm{d}(\text{动量}) = -mg\,\mathrm{d}t$，得 $m\,\mathrm{d}v = -u\,\mathrm{d}m - mg\,\mathrm{d}t$，积分得时刻 $t$ 火箭的速度

$$
v(t) = v_{\mathrm{i}} - gt + u\ln\frac{m_{\mathrm{i}}}{m(t)},
$$
$m(t)$ 是时刻 $t$ 箭体与尚存燃料的质量。火箭能够离开地面的条件是推力大于重力，$uq_m > m_{\mathrm{i}}g$；燃烧时间越长，重力造成的速度损失 $gt$ 越大，所以运载火箭都尽量快地燃烧。

## 3.5. 质心

### 3.5.1. 质心的定义

**定义 3.5.1（质心）** 质点系中质点 $i$ 的质量为 $m_i$、**位矢**为 $\boldsymbol{r}_i$，总质量 $m = \sum_im_i$。点 $C$ 的位矢

$$
\boldsymbol{r}_C = \frac{\sum_im_i\boldsymbol{r}_i}{m}
$$
称为质点系的**质心**。分量式为 $x_C = \dfrac{\sum_im_ix_i}{m}$，$y_C$、$z_C$ 同理。

质心的位置是各质点位置以质量为权重的平均值，它与原点的选取无关（原点移动时，$\boldsymbol{r}_C$ 与各 $\boldsymbol{r}_i$ 改变同一个矢量）。对质量连续分布的物体，求和换成积分：

$$
\boldsymbol{r}_C = \frac{1}{m}\int\boldsymbol{r}\,\mathrm{d}m, \qquad x_C = \frac1m\int x\,\mathrm{d}m, \ \dots
$$
这就是 [2.2.12](/2.2.12#def-12.5.1) 中用重积分定义的质心，$\mathrm{d}m = \rho\,\mathrm{d}V$（面分布、线分布时 $\mathrm{d}m = \sigma\,\mathrm{d}S$、$\lambda\,\mathrm{d}l$）。

几种常见的情形：

- 两个质点：质心在两者的连线上，到两者的距离 $r_1$、$r_2$ 满足 $m_1r_1 = m_2r_2$，离质量大的质点更近。
- 质量均匀分布、形状对称的物体（杆、圆盘、圆环、球），质心在几何中心。
- 线度不大的物体，各处的重力加速度相同，重力的合力作用在质心上，质心与重心重合。
- 质心不一定在物体上：圆环、弯成弧形的铁丝的质心都在物体之外。

**例 3.5.1** 半径为 $R$ 的均匀圆盘上挖去一个半径为 $r$ 的小圆盘，两者的圆心相距 $d$。求剩余部分的质心。

以大圆盘的圆心 $O$ 为原点，$x$ 轴指向小圆盘的圆心 $O'$。由对称性，质心在 $x$ 轴上。设面密度为 $\sigma$。挖去之后的圆盘与小圆盘合起来是完整的大圆盘，其质心在 $O$；把挖去的部分看作质量为负的圆盘叠加上去：

$$
x_C = \frac{\sigma\pi R^2\cdot0 - \sigma\pi r^2\cdot d}{\sigma\pi R^2 - \sigma\pi r^2} = -\frac{d}{(R/r)^2 - 1}.
$$
质心在 $O$ 的另一侧，偏离挖去的一边。

**例 3.5.2** 均匀铁丝弯成半径为 $R$ 的半圆形，求它的质心。

以圆心为原点、对称轴为 $y$ 轴。由对称性 $x_C = 0$。设线密度为 $\lambda$，取张角 $\mathrm{d}\theta$ 的一小段，$\mathrm{d}m = \lambda R\,\mathrm{d}\theta$，$y = R\sin\theta$，总质量 $m = \pi R\lambda$：

$$
y_C = \frac{1}{m}\int_0^\pi R\sin\theta\cdot\lambda R\,\mathrm{d}\theta = \frac{2R^2\lambda}{\pi R\lambda} = \frac{2R}{\pi}.
$$
质心不在铁丝上。

## 3.6. 质心运动定理

### 3.6.1. 质心运动定理

对质心的位矢求导，质心的速度为

$$
\boldsymbol{v}_C = \frac{\mathrm{d}\boldsymbol{r}_C}{\mathrm{d}t} = \frac{\sum_im_i\boldsymbol{v}_i}{m},
$$
是各质点速度的加权平均。于是质点系的总动量

$$
\boldsymbol{P} = \sum_im_i\boldsymbol{v}_i = m\boldsymbol{v}_C,
$$
等于把全部质量集中在质心、以质心速度运动的一个质点的动量。代入质点系动量定理（定理 3.2.1）：

**定理 3.6.1（质心运动定理）** 质点系的总质量与质心加速度的乘积等于质点系所受的合外力：

$$
\boldsymbol{F}_{\mathrm{ext}} = \frac{\mathrm{d}\boldsymbol{P}}{\mathrm{d}t} = m\frac{\mathrm{d}\boldsymbol{v}_C}{\mathrm{d}t} = m\boldsymbol{a}_C.
$$

质心的运动就像一个质点的运动，这个质点位于质心，集中了质点系的全部质量和所受的全部外力。通常所说的"物体的运动"，实际上就是物体质心的运动；把物体看作质点（[5.1.1](/5.1.1)），严格的含义也正在于此。内力不影响质心的运动：

- 在光滑水平面上旋转着滑动的扳手，各点的运动很复杂，质心却做匀速直线运动；
- 跳水运动员在空中翻转，质心仍沿抛物线运动；
- 焰火弹在空中爆炸，碎片四散，在碎片落地之前，整体的质心仍沿原来的抛物线运动。

**例 3.6.1** 直升机的每片旋翼长 $L = 5.97\,\mathrm{m}$，按宽度一定、厚度均匀的薄片计算。旋翼以 $400\,\mathrm{r/min}$ 的转速旋转时，旋翼根部所受的拉力是旋翼重力的多少倍？

旋翼的质心在距转轴 $L/2$ 处，以**角速度** $\omega = 400\times2\pi/60\,\mathrm{rad\,s^{-1}} = 41.9\,\mathrm{rad\,s^{-1}}$ 做匀速圆周运动，加速度 $a_C = \omega^2L/2$ 指向转轴。在水平方向上，旋翼只受根部的拉力（重力与气动力相比之下忽略），由质心运动定理，

$$
F = ma_C = m\omega^2\frac L2, \qquad \frac{F}{mg} = \frac{\omega^2L}{2g} = \frac{41.9^2\times5.97}{2\times9.8} \approx 5.3\times10^2.
$$
旋翼根部承受的拉力是旋翼重力的五百多倍。注意这里用的是地面惯性系中的质心运动定理，而不是在质心系中求解。

**例 3.6.2** 质量 $m_1 = 50\,\mathrm{kg}$ 的人站在质量 $m_2 = 200\,\mathrm{kg}$、长 $l = 4\,\mathrm{m}$ 的船的船头上，开始时人与船都静止。忽略水的阻力，求人走到船尾时船移动的距离。

人与船组成的系统在水平方向不受外力，质心的水平速度保持为零，质心的位置不变：

$$
\frac{m_1x_1 + m_2x_2}{m_1 + m_2} = \frac{m_1x'_1 + m_2x'_2}{m_1 + m_2} \quad\Longrightarrow\quad m_1(x_1 - x'_1) = m_2(x'_2 - x_2).
$$
设船向前（向船头方向）移动 $d$，则人相对地面向后移动 $l - d$，于是 $m_1(l - d) = m_2d$，

$$
d = \frac{m_1}{m_1 + m_2}\,l = \frac{50}{250}\times4\,\mathrm{m} = 0.8\,\mathrm{m}.
$$

### 3.6.2. 动量守恒与质心的运动

由 $\boldsymbol{P} = m\boldsymbol{v}_C$：合外力为零时，$\boldsymbol{a}_C = \boldsymbol{0}$，$\boldsymbol{v}_C$ 为常矢量；合外力在某方向的分量为零时，质心在该方向的分速度不变（例如 $\sum_iF_{ix} = 0 \Rightarrow v_{Cx}$ 为常量）。所以，质点系的动量守恒与质心做匀速直线运动（或静止）是等价的。例 3.3.1 与例 3.6.2 正是用两种说法处理同一类问题。

### 3.6.3. 质心系

**定义 3.6.1（质心系）** 以质心为原点、随质心平动的参考系称为**质心系**（质心参考系）。

质心有加速度时，质心系是平动**非惯性系**（[5.1.2](/5.1.2) 的 2.6.2 节）。质点系的复杂运动可以看成两部分的组合：

1. 整个质点系随质心的平动，由质心运动定理决定；
2. 各质点相对于质心的运动，要在质心系中考察。

**定理 3.6.2（质心系是零动量参考系）** 在质心系中，质点系的总动量为零：$\sum_im_i\boldsymbol{v}'_i = \boldsymbol{0}$，其中 $\boldsymbol{v}'_i = \boldsymbol{v}_i - \boldsymbol{v}_C$ 是质点 $i$ 相对质心系的速度。

**证明** $\sum_im_i\boldsymbol{v}'_i = \sum_im_i\boldsymbol{v}_i - \Big(\sum_im_i\Big)\boldsymbol{v}_C = m\boldsymbol{v}_C - m\boldsymbol{v}_C = \boldsymbol{0}$。同理 $\sum_im_i\boldsymbol{r}'_i = \boldsymbol{0}$，$\boldsymbol{r}'_i = \boldsymbol{r}_i - \boldsymbol{r}_C$。$\square$

因此质心系又称零动量参考系。两个质点组成的系统在质心系中，两者的动量总是等值反向的，这使碰撞问题在质心系中特别简单（[5.1.4](/5.1.4)）。

**例 3.6.3** 线密度为 $\lambda$ 的柔软长绳盘放在地面上，用手以力 $F$ 竖直向上提起其一端。设提起部分的长度为 $y$，求：（1）以恒定速率 $v$ 提起时的 $F$；（2）从静止开始以恒定加速度 $a$ 提起时的 $F$。

这个问题可以当作变质量问题，也可以用质心运动定理处理。取全绳（长 $l$）为系统，以地面为原点、竖直向上为 $y$ 轴。提起的部分质心在 $y/2$ 处，留在地面上的部分质心高度为零，所以全绳的质心坐标为

$$
y_C = \frac{\lambda y\cdot\frac y2 + 0}{\lambda l} = \frac{y^2}{2l}.
$$
全绳所受的外力有：拉力 $F$，重力 $\lambda lg$，地面对留在地面上部分的支持力 $\lambda(l - y)g$。由质心运动定理，

$$
\lambda l\,\ddot y_C = F + \lambda(l - y)g - \lambda lg = F - \lambda yg, \qquad \ddot y_C = \frac{\dot y^2 + y\ddot y}{l},
$$
所以 $F = \lambda yg + \lambda(\dot y^2 + y\ddot y)$。

（1）$\dot y = v$，$\ddot y = 0$：$F = \lambda yg + \lambda v^2$。除提起部分的重力外，还要额外的 $\lambda v^2$ 不断使静止的绳段获得速度 $v$。

（2）$\ddot y = a$，$\dot y^2 = 2ay$：$F = \lambda yg + 3\lambda ya$。

## 3.7. 质点的角动量

### 3.7.1. 角动量

质点绕某一点转动时，仅用动量不足以刻画转动的强弱：同样的动量，离转动中心越远，"转动的量"越大。

**定义 3.7.1（角动量）** 质点 $m$ 相对参考点 $O$ 的位矢为 $\boldsymbol{r}$，动量为 $\boldsymbol{p} = m\boldsymbol{v}$，它对 $O$ 的**角动量**为

$$
\boldsymbol{L} = \boldsymbol{r}\times\boldsymbol{p} = \boldsymbol{r}\times(m\boldsymbol{v}).
$$
大小 $L = rp\sin\alpha = rmv\sin\alpha$（$\alpha$ 为 $\boldsymbol{r}$ 与 $\boldsymbol{p}$ 的夹角），方向垂直于 $\boldsymbol{r}$ 与 $\boldsymbol{p}$ 所在的平面，按右手螺旋确定。单位是 $\mathrm{kg\,m^2\,s^{-1}}$。

参考点 $O$ 是所选参考系中的一个固定点。质点以速率 $v$ 做半径为 $R$ 的圆周运动时，对圆心的角动量大小为 $L = mvR$，方向垂直于圆面、保持不变。参考点不同，角动量一般也不同，所以说角动量必须指明参考点。以圆锥摆为例：摆长为 $l$，摆线与竖直方向成 $\alpha$ 角，摆球以速率 $v$ 在水平面内做圆周运动。

- 对悬点 $O$：$\boldsymbol{r}$ 沿摆线，长度为 $l$，与 $\boldsymbol{v}$ 垂直，$L_O = lmv$；方向垂直于摆线与速度，随摆球绕竖直轴转动而不断改变。
- 对圆周的中心 $O'$：$L_{O'} = mvl\sin\alpha$，方向竖直向上，保持不变。

### 3.7.2. 力矩与角动量定理

对角动量求导，利用向量积的求导法则（[2.2.11](/2.2.11#thm-11.3.1)）：

$$
\frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t} = \frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t}\times\boldsymbol{p} + \boldsymbol{r}\times\frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}t} = \boldsymbol{v}\times m\boldsymbol{v} + \boldsymbol{r}\times\boldsymbol{F} = \boldsymbol{r}\times\boldsymbol{F}.
$$

**定义 3.7.2（力矩）** 力 $\boldsymbol{F}$ 作用在位矢为 $\boldsymbol{r}$（相对参考点 $O$）的质点上，它对 $O$ 的**力矩**为

$$
\boldsymbol{M} = \boldsymbol{r}\times\boldsymbol{F},
$$
大小 $M = rF\sin\alpha = r_0F$，其中 $r_0 = r\sin\alpha$ 是 $O$ 到力的作用线的距离，称为力臂。单位是 $\mathrm{N\,m}$。

**定理 3.7.1（质点角动量定理）** 质点所受的合力矩等于它的角动量对时间的变化率；对同一参考点，

$$
\boldsymbol{M} = \frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t}, \qquad \int_{t_1}^{t_2}\boldsymbol{M}\,\mathrm{d}t = \boldsymbol{L}_2 - \boldsymbol{L}_1.
$$

**定义 3.7.3（冲量矩）** 力矩对时间的积分 $\displaystyle\int_{t_1}^{t_2}\boldsymbol{M}\,\mathrm{d}t$ 称为**冲量矩**（角冲量），它是力矩对时间的积累作用。

角动量定理与动量定理形式相同：力 ↔ 力矩，动量 ↔ 角动量，冲量 ↔ 冲量矩。必须注意，力矩和角动量要对同一个参考点计算。

**例 3.7.1（圆锥摆的角动量）** 对悬点 $O$：摆线的张力 $\boldsymbol{F}_{\mathrm{T}}$ 通过 $O$，力矩为零；重力的力矩大小为 $l\sin\alpha\cdot mg$，方向水平且不为零，所以 $\boldsymbol{L}_O$ 不断变化——与上面看到的 $\boldsymbol{L}_O$ 方向随摆球转动一致。对圆心 $O'$：张力与重力的力矩大小相等、方向相反，合力矩为零，所以 $\boldsymbol{L}_{O'}$ 的大小、方向都不变。而摆球所受的合力（指向圆心）不为零，动量不断改变。可见动量守恒与角动量守恒的条件不同。

### 3.7.3. 对定轴的力矩与角动量

刚体绕定轴转动（[5.1.5](/5.1.5)）时，只有沿转轴的分量起作用。取过参考点 $O$ 的 $z$ 轴，把 $\boldsymbol{r}$、$\boldsymbol{F}$ 分解为平行于 $z$ 轴的分量 $\boldsymbol{r}_\parallel$、$\boldsymbol{F}_\parallel$ 与垂直于 $z$ 轴的分量 $\boldsymbol{r}_\perp$、$\boldsymbol{F}_\perp$。由于 $\boldsymbol{r}_\parallel\times\boldsymbol{F}_\parallel = \boldsymbol{0}$，$\boldsymbol{r}_\parallel\times\boldsymbol{F}_\perp$ 与 $\boldsymbol{r}_\perp\times\boldsymbol{F}_\parallel$ 都垂直于 $z$ 轴，

$$
M_z = (\boldsymbol{r}\times\boldsymbol{F})\cdot\boldsymbol{e}_z = (\boldsymbol{r}_\perp\times\boldsymbol{F}_\perp)\cdot\boldsymbol{e}_z = \pm F_\perp r_\perp\sin\alpha,
$$
$\alpha$ 是 $\boldsymbol{r}_\perp$ 与 $\boldsymbol{F}_\perp$ 的夹角，正负号由转向按右手螺旋确定。

**定义 3.7.4（对轴的力矩与角动量）** 力矩 $\boldsymbol{M}$ 与角动量 $\boldsymbol{L}$ 在过参考点的 $z$ 轴上的投影 $M_z = \boldsymbol{M}\cdot\boldsymbol{e}_z$、$L_z = \boldsymbol{L}\cdot\boldsymbol{e}_z = (\boldsymbol{r}_\perp\times\boldsymbol{p}_\perp)\cdot\boldsymbol{e}_z$ 分别称为力对 $z$ 轴的力矩与质点对 $z$ 轴的角动量。它们与参考点在轴上的位置无关。

$\boldsymbol{e}_z$ 是固定方向，对角动量定理两边取 $z$ 分量，得到质点对定轴的角动量定理

$$
M_z = \frac{\mathrm{d}L_z}{\mathrm{d}t}.
$$
平行于转轴的力和通过转轴的力，对该轴的力矩都为零。

## 3.8. 角动量守恒定律

**定理 3.8.1（角动量守恒定律）** 质点所受的合力矩为零时，质点的角动量保持不变：

$$
\boldsymbol{M} = \boldsymbol{0} \quad\Longrightarrow\quad \boldsymbol{L} = \text{常矢量}.
$$
若只是合力矩对某轴的分量为零，$M_z = 0$，则质点对该轴的角动量守恒，$L_z$ 为常量。

$\boldsymbol{M} = \boldsymbol{r}\times\boldsymbol{F} = \boldsymbol{0}$ 有两种情形：合力为零，或者合力始终通过参考点 $O$。后一种情形中力的作用线始终通过一个固定点，这种力称为有心力（[5.1.4](/5.1.4)），如行星所受太阳的引力、电子所受原子核的 Coulomb 力。质点在有心力作用下，对力心的角动量守恒。角动量守恒定律与动量守恒定律一样，是物理学的基本定律之一。

**例 3.8.1（Kepler 第二定律）** 行星所受的太阳引力始终指向太阳，对太阳的角动量 $\boldsymbol{L} = \boldsymbol{r}\times m\boldsymbol{v}$ 守恒。由此得到两个结论：

1. $\boldsymbol{L}$ 的方向不变，$\boldsymbol{r}$ 与 $\boldsymbol{v}$ 始终在垂直于 $\boldsymbol{L}$ 的同一个平面内，行星的轨道是平面曲线。
2. $\boldsymbol{L}$ 的大小不变。$\mathrm{d}t$ 内行星的位矢扫过的面积是以 $\boldsymbol{r}$ 与 $\boldsymbol{v}\,\mathrm{d}t$ 为两边的三角形，$\mathrm{d}S = \frac12\lvert\boldsymbol{r}\times\boldsymbol{v}\,\mathrm{d}t\rvert$，所以单位时间扫过的面积（掠面速度）

$$
\frac{\mathrm{d}S}{\mathrm{d}t} = \frac12rv\sin\alpha = \frac{L}{2m}
$$
为常量：行星与太阳的连线在相等的时间内扫过相等的面积。这就是 Kepler 第二定律（Kepler's second law）。用极坐标写，$\dfrac{\mathrm{d}S}{\mathrm{d}t} = \frac12r^2\dot\theta$，与 [5.1.1](/5.1.1) 的 1.6 节中加速度横向分量 $a_\theta = \dfrac1r\dfrac{\mathrm{d}}{\mathrm{d}t}(r^2\dot\theta) = 0$ 是同一件事。

这个结论只用到力是有心力，与力随距离的变化规律无关；轨道为椭圆（Kepler 第一定律）才依赖于引力与距离的平方成反比（[5.1.4](/5.1.4)）。

![用 solve_ivp 数值求解平方反比有心力下的轨道（偏心率 0.6）。左：相等时间间隔内位矢扫过的扇形面积相等，近日点附近的扇形短而宽，远日点附近的长而窄。右：速率随时间大幅变化，掠面速度保持不变](./plots/kepler-equal-areas.py)

**例 3.8.2（星系的盘状结构）** 许多星系与原行星云呈扁平的盘状。定性的解释是：设一团缓慢旋转的物质在自身引力作用下收缩，取旋转轴为 $z$ 轴。其中质量为 $m$ 的一部分开始时到轴的距离为 $r_0$、绕轴的速率为 $v_0$。引力指向中心，对 $z$ 轴的力矩近似为零，$L_z = mv_0r_0$ 守恒，所以它收缩到距离 $r$ 时速率 $v = \dfrac{v_0r_0}{r} \propto r^{-1}$，维持圆周运动所需的向心力

$$
F_{\mathrm{c}} = \frac{mv^2}{r} \propto r^{-3},
$$
而引力近似 $\propto r^{-2}$。$r$ 减小时所需的向心力增长得比引力快，径向的收缩到 $F_{\mathrm{c}}$ 与引力相等时就停止了；沿 $z$ 方向则没有这种限制，物质可以在引力作用下继续收缩。结果形成绕 $z$ 轴旋转的扁平圆盘。实际上，物质还必须通过气体的碰撞把沿 $z$ 方向运动的能量耗散掉，才能沉降到盘面上。星系的尺度常用秒差距表示，$1\,\mathrm{pc} = 3.086\times10^{16}\,\mathrm{m}$。

## 3.9. 质点系的角动量

**定义 3.9.1（质点系的角动量）** 质点系对参考点 $O$ 的角动量是各质点对 $O$ 的角动量的矢量和，$\boldsymbol{L} = \sum_i\boldsymbol{r}_i\times\boldsymbol{p}_i$。

对每个质点用角动量定理再求和：

$$
\frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t} = \sum_i\boldsymbol{r}_i\times\Big(\boldsymbol{F}_i + \sum_{j\ne i}\boldsymbol{f}_{ij}\Big) = \boldsymbol{M}_{\mathrm{ext}} + \boldsymbol{M}_{\mathrm{int}}.
$$
内力矩按对配对：$\boldsymbol{r}_i\times\boldsymbol{f}_{ij} + \boldsymbol{r}_j\times\boldsymbol{f}_{ji} = (\boldsymbol{r}_i - \boldsymbol{r}_j)\times\boldsymbol{f}_{ij}$。当内力沿两质点的连线时（引力、静电力、轻杆与绳的力都如此），$\boldsymbol{f}_{ij} \parallel \boldsymbol{r}_i - \boldsymbol{r}_j$，这一项为零，所以 $\boldsymbol{M}_{\mathrm{int}} = \boldsymbol{0}$。

**定理 3.9.1（质点系角动量定理）** 质点系所受的合外力矩等于系统角动量对时间的变化率：

$$
\boldsymbol{M}_{\mathrm{ext}} = \sum_i\boldsymbol{r}_i\times\boldsymbol{F}_i = \frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t},
$$
其中所有的 $\boldsymbol{L}_i$ 与 $\boldsymbol{M}_i$ 都对同一个参考点计算。

**定理 3.9.2（质点系的角动量守恒）** 质点系所受的合外力矩为零时，系统的总角动量守恒；合外力矩在某一方向的分量为零时，总角动量在该方向的分量守恒。

质点系的动量守恒与角动量守恒是相互独立的：前者要求合外力为零，后者要求合外力矩为零。一对大小相等、方向相反、不共线的力（力偶）合力为零而力矩不为零；有心力对力心的力矩为零而合力不为零。所以两者可以各自成立。

**例 3.9.1** 长为 $l$ 的轻杆上端用光滑轴固定在 $O$ 点，下端固结一个质量为 $m_1$ 的小球。质量为 $m_2$ 的小球以水平速度 $v_0$ 打在杆的中点并与杆粘在一起。求碰撞后杆的角速度 $\omega$。

取 $m_1$（连同杆）与 $m_2$ 为系统。碰撞中重力与轴的作用力都通过 $O$（碰撞时杆竖直），对 $O$ 的力矩为零，系统对 $O$ 的角动量守恒：

$$
\frac l2\,m_2v_0 = l\cdot m_1\omega l + \frac l2\cdot m_2\omega\frac l2 \quad\Longrightarrow\quad \omega = \frac{2m_2}{4m_1 + m_2}\,\frac{v_0}{l}.
$$
碰撞过程中系统的水平动量并不守恒：碰后的动量 $m_1\omega l + m_2\omega\frac l2 = \dfrac{2m_1 + m_2}{4m_1 + m_2}\,m_2v_0 < m_2v_0$，轴在碰撞中对杆施加了向后的冲量。

**例 3.9.2** 光滑水平面上，质量为 $m_1$、$m_2$ 的两个小球用长为 $l$ 的轻杆连接，静止放置。质量为 $m_3$ 的小球以速度 $v_0$ 垂直于杆射向杆的中点 $O$，发生弹性碰撞。求碰撞刚结束时三个小球的速度，以及 $m_1$、$m_2$ 系统的质心速度。

取三个小球与杆为系统，水平面内不受外力。碰撞刚结束时 $m_1$、$m_2$ 的速度 $v_1$、$v_2$ 都沿 $v_0$ 的方向，设 $m_3$ 以速率 $v_3$ 反弹（$v_3 < 0$ 表示继续向前）。

- 弹性碰撞，动能守恒：$\frac12m_3v_0^2 = \frac12m_1v_1^2 + \frac12m_2v_2^2 + \frac12m_3v_3^2$；
- 沿 $v_0$ 方向动量守恒：$m_3v_0 = m_1v_1 + m_2v_2 - m_3v_3$；
- 对与 $O$ 重合的固定点角动量守恒（取垂直纸面向外为正），碰前碰后 $m_3$ 的速度都通过 $O$：$0 = -m_1v_1\frac l2 + m_2v_2\frac l2$，即 $m_1v_1 = m_2v_2$。

也可以对与质心 $C$ 重合的固定点写角动量守恒，结果相同。联立解得，记 $D = 4m_1m_2 + (m_1 + m_2)m_3$，

$$
v_1 = \frac{4m_2m_3}{D}v_0, \qquad v_2 = \frac{4m_1m_3}{D}v_0, \qquad v_3 = \frac{4m_1m_2 - (m_1 + m_2)m_3}{D}v_0,
$$

$$
v_C = \frac{m_1v_1 + m_2v_2}{m_1 + m_2} = \frac{8m_1m_2m_3}{(m_1 + m_2)D}v_0.
$$
若 $m_1 \ne m_2$，则 $v_1 \ne v_2$，碰后杆既随质心平动又绕质心转动，角速度为 $\omega = \dfrac{\lvert v_1 - v_2\rvert}{l} = \dfrac{4m_3\lvert m_2 - m_1\rvert}{Dl}v_0$。

动量与角动量的对比：

| | 动量 | 角动量 |
|---|---|---|
| 定义 | $\boldsymbol{P} = \sum_im_i\boldsymbol{v}_i$，矢量 | $\boldsymbol{L} = \sum_i\boldsymbol{r}_i\times\boldsymbol{p}_i$，矢量 |
| 参考点 | 无需指定 | 必须指定 |
| 变化的原因 | 合外力，与内力无关 | 合外力矩，与内力矩无关 |
| 守恒条件 | $\sum_i\boldsymbol{F}_i = \boldsymbol{0}$ | $\sum_i\boldsymbol{r}_i\times\boldsymbol{F}_i = \boldsymbol{0}$ |
| 与质心的关系 | $\boldsymbol{P} = m\boldsymbol{v}_C$ | $\boldsymbol{L} = \boldsymbol{r}_C\times m\boldsymbol{v}_C + \boldsymbol{L}'$（3.10 节） |
| 质心系中 | 总动量为零 | 对质心的角动量定理成立（3.10 节） |

## 3.10. 质心系中的角动量定理

### 3.10.1. 质心系中的角动量

设 $O$ 是惯性系 $S$ 中的固定点，$\boldsymbol{r}_i$、$\boldsymbol{r}_C$ 是质点 $i$ 与质心相对 $O$ 的位矢，$\boldsymbol{r}'_i = \boldsymbol{r}_i - \boldsymbol{r}_C$、$\boldsymbol{v}'_i = \boldsymbol{v}_i - \boldsymbol{v}_C$ 是质点 $i$ 相对质心的位矢与速度。考虑三个角动量：

- 在 $S$ 系中，质点系对 $O$ 的角动量 $\boldsymbol{L} = \sum_i\boldsymbol{r}_i\times m_i\boldsymbol{v}_i$；
- 在 $S$ 系中，把全部质量集中在质心时对 $O$ 的角动量 $\boldsymbol{L}_C = \boldsymbol{r}_C\times m\boldsymbol{v}_C = \boldsymbol{r}_C\times\boldsymbol{P}$；
- 在质心系中，质点系对质心的角动量 $\boldsymbol{L}' = \sum_i\boldsymbol{r}'_i\times m_i\boldsymbol{v}'_i$。

**定理 3.10.1** $\boldsymbol{L} = \boldsymbol{L}_C + \boldsymbol{L}'$：质点系对固定点的角动量，等于质心的角动量（轨道角动量）与质点系对质心的角动量（自旋角动量）之和。

**证明** 代入 $\boldsymbol{r}_i = \boldsymbol{r}'_i + \boldsymbol{r}_C$、$\boldsymbol{v}_i = \boldsymbol{v}'_i + \boldsymbol{v}_C$ 展开：

$$
\boldsymbol{L} = \sum_im_i\boldsymbol{r}'_i\times\boldsymbol{v}'_i + \Big(\sum_im_i\boldsymbol{r}'_i\Big)\times\boldsymbol{v}_C + \boldsymbol{r}_C\times\sum_im_i\boldsymbol{v}'_i + m\,\boldsymbol{r}_C\times\boldsymbol{v}_C.
$$
由定理 3.6.2，$\sum_im_i\boldsymbol{r}'_i = \boldsymbol{0}$，$\sum_im_i\boldsymbol{v}'_i = \boldsymbol{0}$，中间两项为零。$\square$

由同样的理由，$\boldsymbol{L}' = \sum_i\boldsymbol{r}'_i\times m_i\boldsymbol{v}_i$：计算对质心的角动量时，用相对质心的速度还是相对 $S$ 系的速度，结果相同。

### 3.10.2. 对质心的角动量定理

对 $\boldsymbol{L}' = \boldsymbol{L} - \boldsymbol{r}_C\times\boldsymbol{P}$ 求导，用定理 3.9.1 与质点系动量定理，并注意 $\dot{\boldsymbol{r}}_C\times\boldsymbol{P} = \boldsymbol{v}_C\times m\boldsymbol{v}_C = \boldsymbol{0}$：

$$
\frac{\mathrm{d}\boldsymbol{L}'}{\mathrm{d}t} = \sum_i\boldsymbol{r}_i\times\boldsymbol{F}_i - \boldsymbol{r}_C\times\sum_i\boldsymbol{F}_i = \sum_i(\boldsymbol{r}_i - \boldsymbol{r}_C)\times\boldsymbol{F}_i = \sum_i\boldsymbol{r}'_i\times\boldsymbol{F}_i.
$$

**定理 3.10.2（对质心的角动量定理）** 在质心系中，质点系所受的外力对质心的合力矩等于质点系对质心的角动量的变化率：

$$
\boldsymbol{M}'_{\mathrm{ext}} = \sum_i\boldsymbol{r}'_i\times\boldsymbol{F}_i = \frac{\mathrm{d}\boldsymbol{L}'}{\mathrm{d}t}.
$$
无论质心系是否为惯性系，这一定理都成立。

这一点并不显然：质心有加速度 $\boldsymbol{a}_C$ 时，质心系是平动非惯性系，各质点都受**惯性力** $-m_i\boldsymbol{a}_C$。但这些惯性力对质心的合力矩为

$$
\boldsymbol{M}_{\mathrm{in}} = \sum_i\boldsymbol{r}'_i\times(-m_i\boldsymbol{a}_C) = -\Big(\sum_im_i\boldsymbol{r}'_i\Big)\times\boldsymbol{a}_C = \boldsymbol{0},
$$
与均匀重力场中各质点所受重力对质心的合力矩为零是同一个道理：惯性力 $-m_i\boldsymbol{a}_C$ 与质量成正比、方向处处相同，相当于一个作用在质心上的均匀"重力"。

于是质点系的运动可以完整地分成两部分处理：质心的运动由质心运动定理（定理 3.6.1）决定，绕质心的转动由对质心的角动量定理决定，两者都只涉及外力。这正是 [5.1.5](/5.1.5) 处理刚体平面运动（如滚动）的方法。

## 小结

| 内容 | 要点 |
|---|---|
| 动量定理 | 质点 $\boldsymbol{F} = \mathrm{d}\boldsymbol{p}/\mathrm{d}t$；质点系 $\boldsymbol{F}_{\mathrm{ext}} = \mathrm{d}\boldsymbol{P}/\mathrm{d}t$，内力不改变总动量 |
| 动量守恒 | $\boldsymbol{F}_{\mathrm{ext}} = \boldsymbol{0} \Rightarrow \boldsymbol{P}$ 守恒；可按分量守恒；碰撞中近似守恒 |
| 火箭 | $v_{\mathrm{f}} = v_{\mathrm{i}} + u\ln(m_{\mathrm{i}}/m_{\mathrm{f}})$；推力 $uq_m$ |
| 质心 | $\boldsymbol{r}_C = \sum m_i\boldsymbol{r}_i/m$；$\boldsymbol{P} = m\boldsymbol{v}_C$；$\boldsymbol{F}_{\mathrm{ext}} = m\boldsymbol{a}_C$；质心系是零动量参考系 |
| 角动量定理 | $\boldsymbol{L} = \boldsymbol{r}\times\boldsymbol{p}$，$\boldsymbol{M} = \boldsymbol{r}\times\boldsymbol{F}$，$\boldsymbol{M}_{\mathrm{ext}} = \mathrm{d}\boldsymbol{L}/\mathrm{d}t$，对同一参考点 |
| 角动量守恒 | $\boldsymbol{M}_{\mathrm{ext}} = \boldsymbol{0} \Rightarrow \boldsymbol{L}$ 守恒；有心力；Kepler 第二定律 |
| 质心系 | $\boldsymbol{L} = \boldsymbol{r}_C\times\boldsymbol{P} + \boldsymbol{L}'$；$\boldsymbol{M}'_{\mathrm{ext}} = \mathrm{d}\boldsymbol{L}'/\mathrm{d}t$ 对非惯性的质心系也成立 |

## 思考题

1. 一个小球放在桌面上的一张纸上，迅速把纸向右抽出，小球向哪边移动？
   提示：向右。纸对小球的摩擦力向右，由质心运动定理，小球的质心相对桌面向右加速，尽管它相对纸向左滑动（并且开始向后滚动）。
2. 质心可能在物体之外吗？
   提示：可能，如圆环、半圆形铁丝（例 3.5.2）。
3. 把质点系在某一瞬间看成一个整体，各质点所受的重力对质心的合力矩等于什么？由此说明惯性力对质心的力矩为什么为零。
   提示：均匀重力场中为零，因为 $\sum_i\boldsymbol{r}'_i\times m_i\boldsymbol{g} = \big(\sum_im_i\boldsymbol{r}'_i\big)\times\boldsymbol{g} = \boldsymbol{0}$；惯性力 $-m_i\boldsymbol{a}_C$ 具有完全相同的结构（3.10.2 节）。
