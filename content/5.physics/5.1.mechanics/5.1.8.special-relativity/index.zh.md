---
title: 狭义相对论基础
---

到 19 世纪末，Newton 力学、热学与分子动理论、波动光学和 Maxwell 电磁理论都取得了巨大成功：Newton 力学由天王星轨道的摄动预言了海王星，Maxwell 方程组预言了电磁波。1900 年 Kelvin 在演讲中说，物理学晴朗的天空中只飘着"两朵乌云"：以太漂移实验的零结果和黑体辐射的能量均分困难。前者引出了狭义相对论（1905），后者引出了量子论（[5.5.1](/5.5.1)）；连同揭示时空与引力关系的广义相对论（1916）和量子力学（1925），20 世纪初的这几次概念革命彻底改变了我们对时间、空间和物质的认识。

本章是力学的最后一章。前七章都建立在 Galilei 变换与绝对时空观之上（[5.1.1](/5.1.1) 的相对运动、[5.1.2](/5.1.2) 的**惯性系**）。本章从 Einstein 的两条基本原理出发，导出 **Lorentz 变换**，由它得到同时性的相对性、时间延缓、长度收缩和**速度**变换（**运动学**部分）；再要求**动量**守恒和能量守恒在所有惯性系中成立，得到相对论动量、能量与质能关系（**动力学**部分）。数学上，Lorentz 变换是保持 Minkowski 时空中不定二次型的线性变换，它们组成 **Lorentz 群**（[2.1.13](/2.1.13#ex-13.7.1)）。本章的结果在电磁学（[5.3](/5.3)，电磁场的变换）和量子物理（[5.5](/5.5)，光子、Compton 散射、物质波）中都要用到；上一章光的 **Doppler 效应**（[5.1.7](/5.1.7#sec-7.9.2)）的推导也放在这里（[8.5.7 节](#sec-8.5.7)）。

## 8.1. Newton 相对性原理与 Galilei 变换

### 8.1.1. 事件与时空坐标

**定义 8.1.1** 具有确定的发生时刻和发生地点的物理现象称为**事件**，事件发生的时刻和地点 $(x,y,z,t)$ 称为该事件在某**参考系**中的**时空坐标**。同一事件在两个惯性系中的时空坐标之间的变换关系称为时空变换。

例如"一个粒子在某时刻出现在某位置"就是一个事件。讨论时空的性质时，我们只关心事件的时空坐标，不关心事件的具体物理内容。不同形式的时空变换代表对时间和空间的不同测量方式，反映不同的时空观：

- 绝对时空观：时间与空间相互独立，是绝对的、与物质运动无关的"背景舞台"；时间间隔和空间间隔的测量与参考系无关。这与日常经验相符。
- 相对论时空观：时间与空间是统一的整体，与物质的运动密不可分；时空的度量与参考系有关。

### 8.1.2. Galilei 变换

**性质 8.1.1（Newton 相对性原理）** 一切力学规律在所有惯性系中具有相同的形式。

设惯性系 S′ 相对惯性系 S 以速度 $\boldsymbol{v}=v\boldsymbol{e}_x$ 运动，两系的坐标轴相互平行，$t=t'=0$ 时原点 $O$、$O'$ 重合（下文称为标准配置）。由时间间隔与空间间隔测量的绝对性，同一事件的时空坐标满足 Galilei 变换（Galilean transformation）

$$
x'=x-vt,\qquad y'=y,\qquad z'=z,\qquad t'=t.\tag{8.1}
$$
对时间求导得到 **Galilei 速度变换** $u_x'=u_x-v$，$u_y'=u_y$，$u_z'=u_z$（[5.1.1](/5.1.1)），再求导得 $\boldsymbol{a}'=\boldsymbol{a}$。力和质量与参考系无关，所以 **Newton 第二定律** $\boldsymbol{F}=m\boldsymbol{a}$ 在 Galilei 变换下形式不变：Galilei 变换与力学相对性原理一致，用力学实验无法判断一个惯性系是静止还是在作匀速直线运动。

### 8.1.3. 绝对时空观的困难

Newton 力学满足 Galilei 变换，Maxwell 电磁理论却不满足。

- 电磁理论给出真空中的光速 $c=1/\sqrt{\varepsilon_0\mu_0}$ 是常量，与光源和观察者的运动无关；按 Galilei 速度变换，光速应当随参考系变化。
- Maxwell 方程组在 Galilei 变换下形式改变。难道不同惯性系中的电磁规律不同？

历史上提出过一些折中的理论，目的仍是保留 Galilei 变换，但都被实验否定。

发射理论认为光速要叠加光源的速度。按此理论，双星中向着地球运动的星发出的光（速度 $c+v_1$）与背离地球运动的星发出的光（速度 $c-v_2$）到达地球的时间不同，双星的视运动应当出现明显的畸变，但从未观测到（de Sitter，1913）。1964 年 CERN 的实验中，速度为 $0.99975c$ 的 $\pi^0$ 介子衰变 $\pi^0\to2\gamma$ 发出的 $\gamma$ 光子，沿运动方向测得的速度与静止光源发出的光速在 $10^{-4}$ 的精度内一致。大量实验表明：光速与光源的运动无关。

以太理论认为光波在真空中的传播需要一种绝对静止的媒质"以太"，电磁规律只在相对以太静止的"绝对参考系"中成立，光速 $c$ 也只在这个参考系中各向相同。地球相对以太运动，在地球上就应观测到"以太风"。1887 年的 Michelson–Morley 实验用干涉仪比较两条相互垂直、长度都为 $l$ 的光路。设仪器以速度 $v$ 相对以太运动，按 Galilei 速度合成，沿运动方向往返一次的时间为 $t_\parallel=\frac{l}{c-v}+\frac{l}{c+v}=\frac{2l/c}{1-\beta^2}$，垂直方向为 $t_\perp=\frac{2l/c}{\sqrt{1-\beta^2}}$（$\beta=v/c$），两者相差 $\Delta t\approx\frac{l}{c}\beta^2$。把仪器转过 $90^\circ$，两路交换，干涉条纹应移动

$$
\Delta N=\frac{2c\Delta t}{\lambda}\approx\frac{2l\beta^2}{\lambda}.
$$
取地球公转速度 $v\approx3\times10^4\,\mathrm{m\,s^{-1}}$（$\beta\approx10^{-4}$），等效臂长 $l\approx11\,\mathrm{m}$，$\lambda\approx500\,\mathrm{nm}$，预期 $\Delta N\approx0.4$ 条；实际观测到的移动小于 $0.02$ 条，在不同季节、不同时刻重复也是如此。这个"零结果"否定了"以太风"的存在。

于是问题变得尖锐：Galilei 变换（绝对时空观）与物理规律在所有惯性系中的不变性，哪一个更基本？Einstein 选择了后者：Maxwell 方程组应当在所有惯性系中成立，光速在任何惯性系中都是各向同性的 $c$，Michelson–Morley 实验的零结果于是是自然的；需要修改的是时空变换。

## 8.2. Einstein 相对性原理与光速不变原理

Einstein 在 1905 年的论文《论动体的电动力学》中提出两条基本原理，它们是狭义相对论的出发点。

**性质 8.2.1（Einstein 相对性原理）** 所有惯性系都是平权的：物理规律（包括力学规律和电磁学规律）在所有惯性系中具有相同的形式。

**性质 8.2.2（光速不变原理）** 在任何惯性系中，真空中的光速都是 $c$，与惯性系的运动无关，也与光源或观察者的运动无关。

自 1983 年起，SI 把真空中的光速定义为精确值 $c=299\,792\,458\,\mathrm{m\,s^{-1}}$，米由光在 $1/299\,792\,458\,\mathrm{s}$ 内走过的距离定义，这就把光速不变原理写进了单位制。

用一个特定的事件来理解光速不变原理：在标准配置下，$O$ 与 $O'$ 重合的时刻（$t=t'=0$）从重合点发出一个闪光。在 S 系中，光速与光源的运动无关，闪光的**波前**是以 $O$ 为球心、半径为 $ct$ 的球面；在 S′ 系中，波前同样是以 $O'$ 为球心、半径为 $ct'$ 的球面：

$$
x^2+y^2+z^2=c^2t^2,\qquad x'^2+y'^2+z'^2=c^2t'^2.\tag{8.2}
$$
两个球心在 $t>0$ 时并不重合，同一个波前却在两个参考系中都是以本系原点为球心的球面。这只有在 $t'\ne t$ 时才可能：时间也必须随参考系变换。

## 8.3. 同时性的相对性

要比较不同地点发生的事件的时刻，必须先说明如何把放在不同地点的钟对准。

**定义 8.3.1（Einstein 对钟）** 在惯性系中，从静止的钟 A、B 连线的中点 M 发出光信号。由光速不变原理，信号同时到达 A、B，在到达时刻把两只钟拨到同一读数，两只钟就对准了（同步）。

在惯性系的每个位置都配置一只相对该系静止的钟，用这种方法把所有的钟对准；这些对准的钟与惯性坐标系一起构成该惯性系的测量系统。事件 $(x,y,z,t)$ 的时刻 $t$ 由放在事件发生地点 $(x,y,z)$ 处的本系的钟读出。

现在设想一列火车（S′ 系）相对站台（S 系）以速度 $v$ 向右运动，车厢中点 M 发出闪光。在火车上看，闪光同时到达车头与车尾。在站台上看，光速仍是 $c$，而车尾迎着光运动、车头背着光运动，光先到达车尾、后到达车头。所以：

**性质 8.3.1（同时性的相对性）** 在一个惯性系中不同地点同时发生的两个事件，在另一个相对它运动的惯性系中不一定同时发生。

同时性的相对性是光速不变原理的直接结果。由此，每个惯性系都认为自己的钟是对准的，而认为别的惯性系的钟没有对准；分属两个惯性系的两只钟只有在相遇时才能直接比较读数。定量地（[8.5.1 节](#sec-8.5.1)）：在 S 系看，S′ 系中沿运动方向配置的一排钟，越靠前的读数越小（越"晚"）。

## 8.4. Lorentz 变换

### 8.4.1. 推导

光速不变原理和 Einstein 相对性原理所蕴含的时空观，应由一个新的时空变换来表达。早在 1899–1904 年，Lorentz 为解释以太漂移实验的零结果就得到了这一变换，但他以以太存在为前提，并认为只有 $t$ 是真正的时间，$t'$ 只是辅助量（"地方时"）。Einstein 在 1905 年从全新的物理基础出发重新导出了它。

在标准配置下，求同一事件的坐标 $(x,y,z,t)$ 与 $(x',y',z',t')$ 之间的变换。

1. 变换必须是线性的：时空是均匀的，匀速直线运动在两个惯性系中都应是匀速直线运动，一个惯性系中的等间隔事件在另一个惯性系中也应等间隔。
2. 垂直于运动方向的长度测量与参考系无关：$y'=y$，$z'=z$。否则设想两根沿 $y$ 方向、静止长度相同的尺相对运动，它们在相遇时的比较结果将区分两个参考系，违背相对性原理。
3. $O'$（$x'=0$）在 S 系中的运动是 $x=vt$，所以 $x'$ 必须正比于 $x-vt$：$x'=\gamma(x-vt)$，$\gamma$ 待定。由相对性原理，S 在 S′ 中以 $-v$ 运动，两系地位对称（空间各向同性保证比例系数相同）：$x=\gamma(x'+vt')$。
4. 用光速不变确定 $\gamma$：取 $t=t'=0$ 时由原点沿 $x$ 方向发出的光信号，它在两系中分别满足 $x=ct$ 与 $x'=ct'$。代入上面两式，$ct'=\gamma(c-v)t$，$ct=\gamma(c+v)t'$，两式相乘消去 $tt'$，得 $c^2=\gamma^2(c^2-v^2)$。

**定义 8.4.1（Lorentz 因子）** 记 $\beta=v/c$，

$$
\gamma=\frac{1}{\sqrt{1-\beta^2}}=\frac{1}{\sqrt{1-v^2/c^2}}\ge1
$$
称为 **Lorentz 因子**。

最后从 $x=\gamma(x'+vt')$ 与 $x'=\gamma(x-vt)$ 中消去 $x'$，利用 $1-\gamma^2=-\gamma^2\beta^2$，解出 $t'=\gamma\big(t-\frac{v}{c^2}x\big)$。可以验证，由此得到的变换使式 (8.2) 中的两个波前方程等价。

### 8.4.2. Lorentz 变换及其性质

**定理 8.4.1（Lorentz 变换）** 在标准配置下，同一事件在惯性系 S 与 S′ 中的时空坐标满足

$$
x'=\gamma(x-vt),\quad y'=y,\quad z'=z,\quad t'=\gamma\Big(t-\frac{v}{c^2}x\Big);\tag{8.3}
$$
逆变换为把 $v$ 换成 $-v$：

$$
x=\gamma(x'+vt'),\quad y=y',\quad z=z',\quad t=\gamma\Big(t'+\frac{v}{c^2}x'\Big).
$$
两事件的空间间隔与时间间隔满足同样的关系：

$$
\Delta x'=\gamma(\Delta x-v\Delta t),\qquad \Delta t'=\gamma\Big(\Delta t-\frac{v}{c^2}\Delta x\Big).\tag{8.4}
$$

说明：

1. $v\ll c$ 时 $\gamma\approx1$，$\frac{v}{c^2}x\approx0$，Lorentz 变换过渡到 Galilei 变换 (8.1)。Newton 力学是相对论在低速下的极限。
2. $v\ge c$ 时 $\gamma$ 为虚数或无穷大，变换失去意义：真空中的光速 $c$ 是一切可作为参考系的物体的极限**速率**，两个物体的**相对速度**只能小于 $c$。
3. 时间与空间的测量是耦合的：$t'$ 依赖于 $x$，$x'$ 依赖于 $t$。用 $ct$ 代替 $t$，变换写成 $ct'=\gamma(ct-\beta x)$、$x'=\gamma(x-\beta ct)$，$ct$ 与 $x$ 的地位完全对称；它是 Minkowski 时空 $(ct,x,y,z)$ 中的一个"双曲转动"：令 $\beta=\tanh\phi$，则 $\gamma=\cosh\phi$，$\gamma\beta=\sinh\phi$。

**例 8.4.1（Einstein 火车）** 火车（S′ 系）以 $v=0.6c$ 相对地面（S 系）运动。车上的光信号发生器 M 与位于其后方的接收器 A 相距 $l=3\times10^6\,\mathrm{m}$。求地面上测得的光信号从 M 传到 A 所需的时间。

**解** 事件 1：M 发光；事件 2：光到达 A。在火车系中，$\Delta t'=l/c=0.01\,\mathrm{s}$，$\Delta x'=-l$。由逆变换，

$$
\Delta t=\gamma\Big(\Delta t'+\frac{v}{c^2}\Delta x'\Big)=\gamma\frac{l}{c}(1-\beta)=\sqrt{\frac{1-\beta}{1+\beta}}\,\frac lc=\frac12\times0.01\,\mathrm{s}=0.005\,\mathrm{s}.
$$
在地面上看，A 迎着光运动，光走的路程比 $l$ 短，所用时间也短。[8.5.3 节](#sec-8.5.3)将用长度收缩重新计算这个问题。

## 8.5. 相对论时空观

本节从 Lorentz 变换出发，讨论体现相对论时空观的几个重要结论。

![Minkowski 时空图（c = 1）。S′ 系以 v = 0.5c 运动：其时间轴 ct′ 与空间轴 x′ 向光锥（虚线）靠拢；平行于 x′ 轴的虚线是 S′ 系的同时线，在 S′ 中同时的事件 P₁、P₂ 在 S 中不同时](./plots/minkowski-diagram.py)

### 8.5.1. 同时性的相对性

设两事件 $P_1$、$P_2$ 在 S′ 系中同时（$\Delta t'=0$）发生于不同地点（$\Delta x'=x_2'-x_1'\ne0$）。由逆变换 (8.4)，

$$
\Delta t=t_2-t_1=\gamma\frac{v}{c^2}\Delta x'.
$$
$\Delta x'>0$ 时 $\Delta t>0$：在 S 系看，位于运动后方的事件 $P_1$ 先发生。$v\ll c$ 或 $\Delta x'=0$ 时 $\Delta t=0$：同一地点同时发生的事件，在任何惯性系中都同时发生。在 Minkowski 图上，S′ 系的同时线是平行于 $x'$ 轴的斜线，而不是 S 系的水平线。

### 8.5.2. 时间延缓

**定义 8.5.1（原时）** 在某惯性系中同一地点先后发生的两个事件的时间间隔，由该地的一只钟测得，称为这两个事件的**原时**（固有时），记为 $\tau$。在另一个惯性系中，这两个事件发生在不同地点，其时间间隔要由两只（对准的）钟测量。

设两事件在 S′ 系中同地（$\Delta x'=0$）发生，原时 $\tau=\Delta t'$。由逆变换 $\Delta t=\gamma(\Delta t'+\frac{v}{c^2}\Delta x')$，

$$
\Delta t=\gamma\tau=\frac{\tau}{\sqrt{1-v^2/c^2}}>\tau.\tag{8.5}
$$

**性质 8.5.1（时间延缓）** 在一个惯性系中观测，相对它运动的另一个惯性系中同一地点发生的两事件的时间间隔比原时长（原时最短）。这称为时间延缓（time dilation），也称时间膨胀。

任何过程都由一系列相继发生的事件构成，所以从一个惯性系观测，运动参考系中同一地点发生的任何过程（物理的、化学的和生命的）节奏都变慢，即"动钟变慢"：与 S 系中一系列静止的同步钟的"1 秒"相比，运动的钟的"1 秒"更长。注意：

- 动钟变慢不是钟的结构发生了变化，与钟一起运动的观测者感觉不到钟变慢。
- 时间延缓是相对的：S 系认为相对 S′ 静止的钟变慢，S′ 系也认为相对 S 静止的钟变慢。这并不矛盾，因为两种判断比较的是不同的事件对，需要的"同时"概念也不同。
- $v\ll c$ 时 $\Delta t\approx\tau$，回到绝对时间。

**例 8.5.1（$\pi$ 介子的寿命）** 带电 $\pi$ 介子衰变为 $\mu$ 子与中微子，$\pi^+\to\mu^++\nu_\mu$，静止时的平均寿命为 $\tau\approx2.6\times10^{-8}\,\mathrm{s}$。若一束 $\pi$ 介子以 $v=0.99c$ 运动，测得其平均飞行距离 $l\approx53\,\mathrm{m}$，则实验室中的平均寿命为 $\Delta t=l/v\approx1.8\times10^{-7}\,\mathrm{s}$，$\tau/\Delta t\approx0.15$；理论值 $\sqrt{1-\beta^2}=\sqrt{1-0.99^2}\approx0.14$，两者在实验误差内一致。若没有时间延缓，平均飞行距离只有 $v\tau\approx7.7\,\mathrm{m}$。宇宙线在高空产生的 $\mu$ 子能大量到达地面，也是时间延缓的结果。

### 8.5.3. 长度收缩

**定义 8.5.2（原长）** 在相对物体静止的惯性系中测得的物体长度称为**原长**（固有长度），记为 $l_0$。测原长需要测物体两端的坐标，与测量的先后无关。在物体运动的参考系中测长度，必须同时测量两端的坐标。

设尺沿 $x'$ 轴静止于 S′ 系，原长 $l_0=x_2'-x_1'$。在 S 系中同时（$\Delta t=0$）测得两端坐标 $x_1$、$x_2$，由 (8.4)，$\Delta x'=\gamma(\Delta x-v\Delta t)=\gamma\Delta x$，所以

$$
l=x_2-x_1=\frac{l_0}{\gamma}=l_0\sqrt{1-\frac{v^2}{c^2}}<l_0.\tag{8.6}
$$

**性质 8.5.2（长度收缩）** 在相对物体运动的惯性系中，沿运动方向测得的物体长度比原长短（原长最长）。这称为长度收缩（length contraction）。

长度收缩只发生在运动方向上，垂直于运动方向的长度不变。它与时间延缓一样，不是尺的结构发生了变化，也是相对的；与尺一起运动的观测者感受不到尺缩短。

**例 8.5.2** 用长度收缩重解例 8.4.1。在地面系中，车厢 AM 的长度收缩为 $l\sqrt{1-\beta^2}$。光从 M 发出后经时间 $\Delta t$ 到达 A，其间 A 向前移动了 $v\Delta t$，所以 $c\Delta t+v\Delta t=l\sqrt{1-\beta^2}$，

$$
\Delta t=\frac{l\sqrt{1-\beta^2}}{c+v}=\sqrt{\frac{1-\beta}{1+\beta}}\,\frac lc=0.005\,\mathrm{s},
$$
与例 8.4.1 相同。

**例 8.5.3（杆与门框）** 一根原长等于门框宽度 $l_0$ 的细杆贴着墙高速平移，经过墙上的门框（忽略门框厚度）。能否在某一时刻把杆整个"推进"门框里？以墙为参考系，杆的长度收缩为 $l_0\sqrt{1-\beta^2}<l_0$，杆有一段时间整个位于门框的两边之间，似乎可以。以杆为参考系，门框收缩而杆长为 $l_0$，杆似乎不可能整个处于门框之内。矛盾的根源在于同时性：墙系中"杆的前端还没到达门框远边"与"杆的后端已经越过门框近边"是同时的两个事件，在杆系中并不同时。在杆系中，杆的前端先越过门框远边，后端随后才越过近边，杆从未整个位于门框内。若在墙系中同时推动杆的各点，在杆系中各点并不同时受推，杆会弯曲，因此两种描述并不矛盾。

### 8.5.4. 因果关系的绝对性

Lorentz 变换会不会颠倒两个事件的先后？设事件 $P_1$、$P_2$ 在 S 系中的时间间隔与空间间隔为 $\Delta t=t_2-t_1$、$\Delta x=x_2-x_1$，记 $v_{\mathrm{s}}=\Delta x/\Delta t$。由 (8.4)，

$$
\Delta t'=\gamma\Delta t\Big(1-\frac{v}{c^2}v_{\mathrm{s}}\Big).
$$
若 $P_1$ 是 $P_2$ 的原因，$P_1$ 发出的影响（信号）要以速度 $v_{\mathrm{s}}$ 传到 $P_2$，而任何信号的速度都不超过 $c$，所以 $\lvert v_{\mathrm{s}}\rvert\le c$。又 $\lvert v\rvert<c$，故 $1-\frac{v v_{\mathrm{s}}}{c^2}>0$，$\Delta t'$ 与 $\Delta t$ 同号：

**性质 8.5.3（因果关系的绝对性）** 有因果联系的两个事件的先后顺序在所有惯性系中都相同。

若 $P_1$、$P_2$ 相互独立，$v_{\mathrm{s}}$ 可以大于 $c$，选取 $v>c^2/v_{\mathrm{s}}$ 的惯性系就能使它们的时序颠倒（时序的相对性），这并不违背因果律。反过来，如果存在超光速的信号，就可以在某个惯性系中让结果先于原因发生；因果律要求信号速度不超过 $c$。

### 8.5.5. 时空间隔的不变性

**定义 8.5.3（时空间隔）** 两事件 $P_1$、$P_2$ 的时空间隔 $\Delta s$ 定义为

$$
(\Delta s)^2=c^2(\Delta t)^2-\big[(\Delta x)^2+(\Delta y)^2+(\Delta z)^2\big]=c^2(\Delta t)^2-(\Delta l)^2,
$$
$\Delta t$、$\Delta l$ 是两事件在同一惯性系中的时间间隔与空间距离。

**定理 8.5.1（间隔不变性）** 时空间隔是 Lorentz 不变量：$(\Delta s')^2=(\Delta s)^2$。

**证明** 由 (8.4) 直接计算，$c^2(\Delta t')^2-(\Delta x')^2=\gamma^2\big[(c\Delta t-\beta\Delta x)^2-(\Delta x-\beta c\Delta t)^2\big]=\gamma^2(1-\beta^2)\big[c^2(\Delta t)^2-(\Delta x)^2\big]=c^2(\Delta t)^2-(\Delta x)^2$，而 $\Delta y'=\Delta y$，$\Delta z'=\Delta z$。$\square$

用线性代数的语言，$(\Delta s)^2$ 是 $\mathbb{R}^4$ 上的 Lorentz 型（符号差为 $(1,3)$ 的不定二次型），保持它的线性变换就是 Lorentz 变换（[2.1.13](/2.1.13#ex-13.7.1)，那里给出了同样的计算）。按间隔的符号，两事件的关系分为三类：

| 间隔 | 类型 | 物理意义 |
|---|---|---|
| $(\Delta s)^2>0$ | 类时 | 可以有因果联系；存在惯性系使两事件同地发生，时序在所有惯性系中相同 |
| $(\Delta s)^2=0$ | 类光 | 可以用光信号联系，$\Delta l=c\Delta t$ |
| $(\Delta s)^2<0$ | 类空 | 不能有因果联系；存在惯性系使两事件同时发生，时序可以颠倒 |

对同一地点发生的两事件，$\Delta l=0$，$\Delta s=c\tau$，所以原时 $\tau=\Delta s/c$ 也是 Lorentz 不变量：不同惯性系对"同一只钟走过的时间"的判断一致。时间延缓式 (8.5) 正是这一不变性的结果：$c^2\tau^2=c^2(\Delta t)^2-v^2(\Delta t)^2$。

**例 8.5.4** 在 S′ 系中同一地点发生的两事件的时间间隔为 $4\,\mathrm{s}$，在 S 系中的时间间隔为 $5\,\mathrm{s}$。求 S 系中两事件的空间距离。

**解** 由间隔不变性，$c^2(5\,\mathrm{s})^2-(\Delta l)^2=c^2(4\,\mathrm{s})^2$，所以 $\Delta l=c\times3\,\mathrm{s}\approx9.0\times10^8\,\mathrm{m}$。由此还可求出两系的相对速度 $v=\Delta l/\Delta t=0.6c$。

### 8.5.6. 孪生子问题

一对孪生子，哥哥乘飞船以高速往返于遥远的星球，弟弟留在地球。按时间延缓，弟弟认为哥哥的钟变慢，哥哥也认为弟弟的钟变慢；两人重逢时究竟谁年轻？这就是孪生子佯谬。

佯谬的解决在于两人的地位并不对称：地球（近似）始终是惯性系，飞船则要掉头，在掉头时有**加速度**，不是始终处于同一个惯性系。这个问题完全可以在狭义相对论中求解，不需要广义相对论：在地球惯性系中，旅行者的原时是沿其世界线累积的

$$
\tau=\int\sqrt{1-\frac{v(t)^2}{c^2}}\,\mathrm{d}t,
$$
它总小于地球上的时间 $\int\mathrm{d}t$，与加速过程的细节无关（加速阶段可以任意短）。例如飞船以 $0.8c$ 往返于相距 $4$ 光年的星球，地球上经过 $10$ 年，哥哥只经过 $10\times0.6=6$ 年：重逢时哥哥更年轻。这称为孪生子效应。从哥哥的角度看，掉头时他从一个惯性系换到另一个惯性系，他心目中"与此同时"的地球时刻发生了跳变，补上了差额。

这类效应已被实验直接验证。1971 年 Hafele 与 Keating 携带铯原子钟乘民航班机分别向东、向西环球飞行，与美国海军天文台的原子钟比较：向东飞行的钟慢了 $(59\pm10)\,\mathrm{ns}$（预言 $(40\pm23)\,\mathrm{ns}$），向西飞行的钟快了 $(273\pm7)\,\mathrm{ns}$（预言 $(275\pm21)\,\mathrm{ns}$），实验与理论一致。其中的预言同时包含运动引起的狭义相对论效应和高度引起的引力（广义相对论）效应。今天的 GPS 卫星时钟必须同时修正这两种效应才能正常定位。

### 8.5.7. 光的 Doppler 效应

[5.1.7](/5.1.7#sec-7.9.2) 给出了电磁波的 Doppler 公式，现在用时间延缓推导它。在接收器 R 的惯性系中，设光源 S 以速度 $v$ 运动，速度方向与由 S 指向 R 的方向成 $\theta$ 角，R 离 S 很远。光源在自身参考系中的周期 $T_0=1/\nu_{\mathrm{S}}$ 是原时（前后两个波峰在光源处同地发出），所以在 R 系中两次发射相隔 $\gamma T_0$。其间光源向 R 靠近了 $v\gamma T_0\cos\theta$，后一个波峰少走这段路程，到达 R 的时间间隔为

$$
T_{\mathrm{R}}=\gamma T_0-\frac{v\gamma T_0\cos\theta}{c}=\gamma T_0(1-\beta\cos\theta).
$$
所以

$$
\nu_{\mathrm{R}}=\frac{\nu_{\mathrm{S}}}{\gamma(1-\beta\cos\theta)}=\frac{\sqrt{1-\beta^2}}{1-\beta\cos\theta}\,\nu_{\mathrm{S}}.\tag{8.7}
$$
与**机械波**的公式 [5.1.7](/5.1.7#fml-7.9.1) 相比，分母中的 $1-\beta\cos\theta$ 是波源运动压缩**波长**的经典因子，分子中的 $\sqrt{1-\beta^2}$ 是光源的时间延缓。$\theta=0$ 与 $\theta=\pi$ 给出纵向 Doppler 效应 $\nu_{\mathrm{R}}=\sqrt{\frac{1\pm\beta}{1\mp\beta}}\nu_{\mathrm{S}}$；$\theta=\pi/2$ 时仍有 $\nu_{\mathrm{R}}=\nu_{\mathrm{S}}/\gamma$，这是纯粹的相对论效应（横向 Doppler 效应），1938 年 Ives 与 Stilwell 用高速氢离子束的光谱首次证实。纵向公式只依赖相对速度：在光源参考系中计算接收器向光源运动的情形，会得到同样的结果，这正是相对性原理的要求。注意式 (8.7) 中的 $\theta$ 是在接收器参考系中测量的；在光源参考系中测得的角度不同（光行差）。

## 8.6. 相对论速度变换

设同一**质点**在 S 系和 S′ 系中的速度分别为 $\boldsymbol{u}=(u_x,u_y,u_z)$ 与 $\boldsymbol{u}'$（本节用 $u$ 表示质点的速度，以区别于两个参考系的相对速度 $v$）。对 Lorentz 变换 (8.3) 取微分：

$$
\mathrm{d}x'=\gamma(\mathrm{d}x-v\,\mathrm{d}t),\qquad \mathrm{d}t'=\gamma\Big(\mathrm{d}t-\frac{v}{c^2}\mathrm{d}x\Big)=\gamma\,\mathrm{d}t\Big(1-\frac{vu_x}{c^2}\Big),\qquad \mathrm{d}y'=\mathrm{d}y,\qquad \mathrm{d}z'=\mathrm{d}z,
$$
两两相除即得：

**定理 8.6.1（相对论速度变换）**

$$
u_x'=\frac{u_x-v}{1-\dfrac{vu_x}{c^2}},\qquad u_y'=\frac{u_y}{\gamma\Big(1-\dfrac{vu_x}{c^2}\Big)},\qquad u_z'=\frac{u_z}{\gamma\Big(1-\dfrac{vu_x}{c^2}\Big)};\tag{8.8}
$$
逆变换为把带撇与不带撇的量互换、$v$ 换成 $-v$：$u_x=\frac{u_x'+v}{1+vu_x'/c^2}$，$u_y=\frac{u_y'}{\gamma(1+vu_x'/c^2)}$，$u_z=\frac{u_z'}{\gamma(1+vu_x'/c^2)}$。

说明：

1. $v\ll c$、$u\ll c$ 时过渡到 Galilei 速度变换 $\boldsymbol{u}'=\boldsymbol{u}-\boldsymbol{v}$。
2. 与**位移**不同，垂直于相对运动方向的速度分量也要变换，因为时间间隔变了。
3. 通过参考系变换不可能得到超光速（见下式）。

由 (8.8) 可以验证恒等式

$$
1-\frac{u'^2}{c^2}=\frac{\big(1-\frac{v^2}{c^2}\big)\big(1-\frac{u^2}{c^2}\big)}{\big(1-\frac{vu_x}{c^2}\big)^2},
$$
所以 $u<c$ 时 $u'<c$，$u=c$ 时 $u'=c$：光速在所有惯性系中相同，这正是光速不变原理。

**例 8.6.1** 飞船以 $0.80c$ 相对地面飞行，从飞船上沿飞行方向抛出一个物体，物体相对飞船的速度为 $0.90c$。求地面上测得的物体速度。

**解** 取地面为 S 系、飞船为 S′ 系，$v=0.80c$，$u_x'=0.90c$。由逆变换，

$$
u_x=\frac{0.90c+0.80c}{1+0.80\times0.90}=\frac{1.70}{1.72}c\approx0.99c,
$$
而不是按 Galilei 变换得到的 $1.70c$。

**例 8.6.2** 在 S′ 系中一束光沿 $y'$ 轴传播，S′ 系相对 S 系以 $0.8c$ 沿 $x$ 方向运动。求 S 系中的光速。

**解** $v=0.8c$，$u_x'=0$，$u_y'=c$，$u_z'=0$。由逆变换，$u_x=v=0.8c$，$u_y=\frac{c}{\gamma}=c\sqrt{1-0.64}=0.6c$，$u_z=0$，所以 $u=\sqrt{u_x^2+u_y^2}=c$。光速不变指的是在不同参考系中光的传播速率不变，而不是传播方向不变：在 S 系中光沿与 $x$ 轴成 $\arctan(0.6/0.8)\approx37^\circ$ 的方向传播（光行差）。

## 8.7. 相对论动量

从本节起，$\boldsymbol{v}$ 表示质点相对某惯性系的速度，$\gamma=1/\sqrt{1-v^2/c^2}$ 是质点的 Lorentz 因子。

相对论动力学是在保留动量、能量等基本守恒定律的基础上建立的。基本要求是：按相对性原理，基本规律（守恒定律、动力学方程）在 Lorentz 变换下形式不变；$v\ll c$ 时过渡到 Newton 力学。

Newton 力学的动量 $m\boldsymbol{v}$ 不能满足第一条：可以验证，若一次碰撞在 S 系中满足 $\sum m_i\boldsymbol{v}_i$ 守恒，用相对论速度变换 (8.8) 换到 S′ 系后一般就不再守恒。问题出在时间：$\mathrm{d}\boldsymbol{r}/\mathrm{d}t$ 中的 $\mathrm{d}t$ 依赖于参考系，而原时 $\mathrm{d}\tau=\mathrm{d}t/\gamma$ 是不变量（[8.5.5 节](#sec-8.5.5)）。用它代替 $\mathrm{d}t$，就得到：

**定义 8.7.1（相对论动量）** 质量为 $m$、速度为 $\boldsymbol{v}$ 的质点的**相对论动量**为

$$
\boldsymbol{p}=m\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}\tau}=\gamma m\boldsymbol{v}=\frac{m\boldsymbol{v}}{\sqrt{1-v^2/c^2}}.\tag{8.9}
$$
其中 $m$ 是质点的质量（不变质量），与参考系和运动速度无关。

实验（例如带电粒子在磁场中的偏转，[8.8 节](#sec-8.8)）证实，按 (8.9) 定义的动量在孤立系统中守恒，而且在所有惯性系中都守恒。$v\ll c$ 时 $\boldsymbol{p}\approx m\boldsymbol{v}$，回到 Newton 力学；$v\to c$ 时 $p\to\infty$，所以有质量的物体不能被加速到光速。

**例 8.7.1** 一个静止的粒子（质量 $M$）分裂为质量都为 $m$ 的两块 A、B，在粒子原来静止的参考系 S′ 中，两块分别以 $-v$、$+v$ 沿 $x$ 方向运动。在随 A 一起运动的参考系 S 中分析这一过程。

**解** S′ 系相对 S 系以 $v$ 运动。由速度变换，A 在 S 中静止，B 的速度为 $v_B=\frac{2v}{1+\beta^2}$，分裂前的粒子以 $v$ 运动。可以算出 $1-v_B^2/c^2=\big(\frac{1-\beta^2}{1+\beta^2}\big)^2$，即 $\gamma_B=\frac{1+\beta^2}{1-\beta^2}=2\gamma^2-1$。在 S 系中，动量守恒要求

$$
\gamma Mv=0+\gamma_Bmv_B=\frac{2mv}{1-\beta^2}=2\gamma^2mv,
$$
所以 $M=2\gamma m>2m$：分裂前粒子的质量大于分裂后两块质量之和，相对论中质量不是可加的。在 S′ 系中验证能量守恒（[8.9 节](#sec-8.9)）：$Mc^2=2\gamma mc^2$，同样成立。从动量守恒式还可以读出 $\gamma_B m$ 的作用：如果把 $m_B=\gamma_Bm$ 叫作 B 的"质量"，动量就仍可写成"质量乘速度"。

**注 8.7.1（相对论质量）** 许多较早的教材（包括本课程所用教材）把 $m(v)=\gamma m_0$ 称为"相对论质量"或"运动质量"，$m_0$ 称为"静止质量"，于是 $\boldsymbol{p}=m(v)\boldsymbol{v}$，$E=m(v)c^2$。这种写法在数值上与本章等价，但现代物理文献（包括粒子数据组）只使用不随速度变化的不变质量 $m$：$m(v)$ 只是总能量 $E/c^2$ 的另一个名字，它并不满足 $\boldsymbol{F}=m(v)\boldsymbol{a}$（[8.8 节](#sec-8.8)），也会让人误以为高速物体的"惯性"或引力质量"变大了"。本站一律用 $\boldsymbol{p}=\gamma m\boldsymbol{v}$、$E=\gamma mc^2$，$m$ 就是粒子的质量。

| 电子的总能量 $E/\mathrm{MeV}$ | $\gamma=E/(mc^2)$ | $v/c$ |
|---|---|---|
| $5$ | $9.78$ | $0.9948$ |
| $25$ | $48.9$ | $0.99979$ |
| $2.8\times10^3$ | $5.48\times10^3$ | $0.999\,999\,983$ |

（电子的静能 $mc^2=0.511\,\mathrm{MeV}$。能量增大到 560 倍，速度只从 $0.995c$ 增加到 $0.999\,999\,98c$。）

## 8.8. 相对论动力学方程

保留力的定义"力等于动量的变化率"：

$$
\boldsymbol{F}=\frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}t}=\frac{\mathrm{d}}{\mathrm{d}t}(\gamma m\boldsymbol{v})=\gamma m\boldsymbol{a}+m\frac{\mathrm{d}\gamma}{\mathrm{d}t}\boldsymbol{v}.\tag{8.10}
$$
由 $\frac{\mathrm{d}\gamma}{\mathrm{d}t}=\gamma^3\frac{v}{c^2}\frac{\mathrm{d}v}{\mathrm{d}t}=\gamma^3\frac{\boldsymbol{v}\cdot\boldsymbol{a}}{c^2}$，把加速度分解为切向分量 $a_{\mathrm{t}}=\mathrm{d}v/\mathrm{d}t$（沿 $\boldsymbol{v}$）与法向分量 $a_{\mathrm{n}}=v^2/\rho$（[5.1.1](/5.1.1) 的**自然坐标系**），得

$$
F_{\mathrm{t}}=\gamma ma_{\mathrm{t}}+m\gamma^3\frac{v^2}{c^2}a_{\mathrm{t}}=\gamma^3ma_{\mathrm{t}},\qquad F_{\mathrm{n}}=\gamma ma_{\mathrm{n}}.
$$

因此：

- 力与加速度一般不平行（$\boldsymbol{F}=m\boldsymbol{a}$ 不成立，用任何"质量"都不行）；
- 速度越大，加速越困难；
- 沿速度方向加速（比例系数 $\gamma^3m$）比改变速度方向（比例系数 $\gamma m$）更困难。

$v\ll c$ 时 $\gamma\approx1$，回到 $\boldsymbol{F}=m\boldsymbol{a}$。当 $\boldsymbol{F}\perp\boldsymbol{v}$ 时，速率不变，$\boldsymbol{F}=\gamma m\boldsymbol{a}$。例如电荷为 $-e$ 的电子在匀强磁场 $\boldsymbol{B}$ 中作垂直于磁场的圆周运动，Lorentz 力 $evB$ 提供向心力（[5.3.7](/5.3.7)）：

$$
evB=\gamma m\frac{v^2}{R},\qquad R=\frac{\gamma mv}{eB}=\frac{p}{eB}.
$$
测量轨道半径就可以测出动量。20 世纪初 Kaufmann、Bucherer 等人对高速电子在电磁场中偏转的测量，最早验证了动量的相对论表达式。

## 8.9. 相对论能量

### 8.9.1. 相对论动能

保留**动能定理**（[5.1.4](/5.1.4)）：合力所做的**功**等于**动能**的增量，$\mathrm{d}E_{\mathrm{k}}=\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}=\frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}t}\cdot\boldsymbol{v}\,\mathrm{d}t=\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{p}$。由 $\boldsymbol{p}=\gamma m\boldsymbol{v}$，

$$
\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{p}=m\big(\gamma v\,\mathrm{d}v+v^2\,\mathrm{d}\gamma\big)=m\big(\gamma+\gamma^3\beta^2\big)v\,\mathrm{d}v=m\gamma^3v\,\mathrm{d}v=mc^2\,\mathrm{d}\gamma,
$$
其中用到 $\mathrm{d}\gamma=\gamma^3v\,\mathrm{d}v/c^2$ 和 $\gamma(1+\gamma^2\beta^2)=\gamma^3$。从静止（$\gamma=1$）积分到速度 $v$：

**公式 8.9.1（相对论动能）**

$$
E_{\mathrm{k}}=(\gamma-1)mc^2=\frac{mc^2}{\sqrt{1-v^2/c^2}}-mc^2.\tag{8.11}
$$

$v\ll c$ 时，$\gamma=1+\frac12\beta^2+\frac38\beta^4+\cdots$，$E_{\mathrm{k}}\approx\frac12mv^2+\frac38\frac{mv^4}{c^2}$，首项就是 Newton 力学的动能。注意：$\boldsymbol{p}=\gamma m\boldsymbol{v}$ 是相对论动量，但 $\frac12\gamma mv^2$ 不是相对论动能。$v\to c$ 时 $E_{\mathrm{k}}\to\infty$，把有质量的物体加速到光速需要无穷大的能量。

![左：Lorentz 因子 γ 随 β = v/c 的变化；右：相对论动能 (γ - 1)mc² 与 Newton 动能 mv²/2 的比较，两者在 β ≲ 0.3 时几乎重合](./plots/lorentz-factor-energy.py)

### 8.9.2. 静能与质能关系

式 (8.11) 中的 $\gamma mc^2$ 与 $mc^2$ 各有物理意义。

**定义 8.9.1** $E_0=mc^2$ 称为质点的**静能**（静止能量），$E=\gamma mc^2=E_{\mathrm{k}}+mc^2$ 称为质点的总能量（相对论能量）。

物体静止时也具有能量 $E_0=mc^2$，它包括物体内部所有粒子的动能、相互作用**势能**（例如原子核的结合能）等。Einstein 提出的质能关系（mass–energy relation）

$$
E_0=mc^2,\qquad E=\gamma mc^2\tag{8.12}
$$
说明质量是物体所含静能的量度：系统的静能改变 $\Delta E_0$ 时，其质量相应地改变 $\Delta m=\Delta E_0/c^2$。在相对论中，能量守恒与动量守恒仍然成立，而 Newton 力学中独立的质量守恒定律被并入能量守恒：一个孤立系统的总能量 $\sum\gamma_im_ic^2$ 守恒，各粒子的质量之和则不一定守恒。

对由若干个粒子组成的孤立系统，反应前后总能量守恒，$\Delta E_{\mathrm{k}}+\Delta\big(\sum m_ic^2\big)=0$，所以

$$
\Delta E_{\mathrm{k}}=\Big(\sum m_{i,\mathrm{initial}}-\sum m_{i,\mathrm{final}}\Big)c^2=\Delta m\,c^2.
$$
反应前后粒子质量之和的减少量 $\Delta m$ 称为质量亏损（mass defect）；质量亏损对应的静能转化为反应产物的动能（释放能量）。

**例 8.9.1（D–T 聚变）** 热核反应 $\ce{^2_1H + ^3_1H -> ^4_2He + ^1_0n}$ 中，由原子质量（$m_{\mathrm{D}}=2.014\,10\,\mathrm{u}$，$m_{\mathrm{T}}=3.016\,05\,\mathrm{u}$，$m_{\mathrm{He}}=4.002\,60\,\mathrm{u}$，$m_{\mathrm{n}}=1.008\,66\,\mathrm{u}$）得质量亏损

$$
\Delta m=(m_{\mathrm{D}}+m_{\mathrm{T}})-(m_{\mathrm{He}}+m_{\mathrm{n}})=0.018\,88\,\mathrm{u}\approx3.136\times10^{-29}\,\mathrm{kg},
$$
释放能量 $\Delta E=\Delta m\,c^2\approx2.818\times10^{-12}\,\mathrm{J}\approx17.6\,\mathrm{MeV}$（$1\,\mathrm{u}\cdot c^2=931.494\,\mathrm{MeV}$）。每千克 D–T 燃料释放约 $3.4\times10^{14}\,\mathrm{J}$，约为 $1\,\mathrm{kg}$ 优质煤燃烧热（约 $2.9\times10^7\,\mathrm{J}$）的一千万倍。质能关系的提出开创了原子能时代。

**例 8.9.2** 两个质量都为 $m$ 的全同粒子以相同的速率 $v$ 相向运动，碰撞后结合成一个复合粒子。求复合粒子的速度与质量。

**解** 设复合粒子的质量为 $M$、速度为 $V$。动量守恒：$\gamma mv-\gamma mv=\gamma_VMV$，所以 $V=0$。能量守恒：$2\gamma mc^2=Mc^2$，所以

$$
M=2\gamma m=\frac{2m}{\sqrt{1-v^2/c^2}}>2m.
$$
碰撞损失的动能 $2(\gamma-1)mc^2$ 全部转化为复合粒子的静能，复合粒子的质量因此大于 $2m$。在 Newton 力学中，这部分动能"变成了热"；在相对论中，热运动的能量本来就计入物体的静能。

### 8.9.3. 能量–动量关系

由 $E=\gamma mc^2$ 与 $p=\gamma mv$，$E^2-p^2c^2=\gamma^2m^2c^4(1-\beta^2)=m^2c^4$，即

**公式 8.9.2（能量–动量关系）**

$$
E^2=p^2c^2+m^2c^4.\tag{8.13}
$$

$E$、$pc$、$mc^2$ 构成一个直角三角形的斜边与两条直角边。$E^2-p^2c^2=m^2c^4$ 与参考系无关（[8.10 节](#sec-8.10)），所以质量 $m$ 是 Lorentz 不变量。由 $E=E_{\mathrm{k}}+mc^2$ 还得到动能–动量关系

$$
E_{\mathrm{k}}^2+2E_{\mathrm{k}}mc^2=p^2c^2.
$$
$v\ll c$ 时 $E_{\mathrm{k}}\ll mc^2$，略去 $E_{\mathrm{k}}^2$，得 $E_{\mathrm{k}}\approx\frac{p^2}{2m}$，回到 Newton 力学的动能–动量关系；极端相对论情形 $E_{\mathrm{k}}\gg mc^2$ 时 $E\approx pc$。由 (8.13) 与 $E=\gamma mc^2$ 还有一个常用的关系 $\boldsymbol{v}=\frac{\boldsymbol{p}c^2}{E}$。

### 8.9.4. 光子

对质量为零的粒子，由 (8.13)，$E=pc$；由 $\boldsymbol{v}=\boldsymbol{p}c^2/E$，它的速率总是 $c$。反过来，以光速运动的粒子质量必须为零（否则 $\gamma\to\infty$，能量无穷大）。光子就是这样的粒子（[5.5.1](/5.5.1)）：按 Einstein 的光子理论，频率为 $\nu$ 的光子的能量与动量为

$$
E=h\nu,\qquad p=\frac{E}{c}=\frac{h\nu}{c}=\frac{h}{\lambda}.
$$
光子的质量为零，它的全部能量都是动能。较早的教材把 $h\nu/c^2$ 称为光子的"运动质量"，按现行写法这只是 $E/c^2$，不是光子的质量（注 8.7.1）。光子的动量在光压、Compton 散射中有直接的体现。

## 8.10. 动量–能量变换

由 $\boldsymbol{p}=\gamma m\boldsymbol{v}$、$E=\gamma mc^2$ 和速度变换 (8.8)，可以求出同一质点的动量与能量在 S 与 S′ 系之间的变换（$v$ 为两系的相对速度，$\gamma$ 为两系之间的 Lorentz 因子）：

**定理 8.10.1（动量–能量变换）**

$$
p_x'=\gamma\Big(p_x-\frac{v}{c^2}E\Big),\qquad p_y'=p_y,\qquad p_z'=p_z,\qquad E'=\gamma(E-vp_x).\tag{8.14}
$$

与 Lorentz 变换 (8.3) 对比，$p_x\leftrightarrow x$，$p_y\leftrightarrow y$，$p_z\leftrightarrow z$，$E/c^2\leftrightarrow t$：$(E/c,\boldsymbol{p})$ 与 $(ct,\boldsymbol{r})$ 按同样的方式变换。$(E/c,p_x,p_y,p_z)$ 称为四维动量（four-momentum），$(ct,x,y,z)$ 称为四维**位置矢量**；它们的"长度平方" $E^2/c^2-p^2=m^2c^2$、$c^2t^2-r^2$ 都在 **Lorentz 群**（[2.1.13](/2.1.13#ex-13.7.1)）的作用下保持不变。这说明在相对论中，能量与动量是同一个四维矢量的分量，正如时间与空间是同一个时空的坐标。

## 8.11. 力的变换

由 $\boldsymbol{F}=\mathrm{d}\boldsymbol{p}/\mathrm{d}t$、动量–能量变换 (8.14) 和 $\mathrm{d}E/\mathrm{d}t=\boldsymbol{F}\cdot\boldsymbol{u}$，可以求出质点所受的力在两个惯性系之间的变换。设质点在 S′ 系中的速度为 $\boldsymbol{u}'$，结果为

$$
F_x=\frac{F_x'+\dfrac{v}{c^2}\boldsymbol{F}'\cdot\boldsymbol{u}'}{1+\dfrac{vu_x'}{c^2}},\qquad F_y=\frac{F_y'}{\gamma\Big(1+\dfrac{vu_x'}{c^2}\Big)},\qquad F_z=\frac{F_z'}{\gamma\Big(1+\dfrac{vu_x'}{c^2}\Big)}.
$$
特别地，若质点在 S′ 系中瞬时静止（$\boldsymbol{u}'=\boldsymbol{0}$，它在 S 系中以 $v$ 运动），则

$$
F_x=F_x',\qquad F_y=\frac{F_y'}{\gamma},\qquad F_z=\frac{F_z'}{\gamma}:
$$
沿运动方向的分力不变，垂直方向的分力变为 $1/\gamma$。这一结果在电磁学中要用到：静止电荷在其静止系中只受电场力，换到运动参考系中，力的变换要求出现与速度有关的磁场力，由此可以从 Coulomb 定律与相对论导出电场与磁场的变换（[5.3](/5.3)）。

## 小结

| 主题 | 要点 |
|---|---|
| 基本原理 | Einstein 相对性原理；光速不变原理 |
| Lorentz 变换 | $x'=\gamma(x-vt)$，$t'=\gamma(t-vx/c^2)$，$\gamma=1/\sqrt{1-v^2/c^2}$；$v\ll c$ 时回到 Galilei 变换 |
| 同时性 | 在 S′ 中异地同时的事件，在 S 中 $\Delta t=\gamma v\Delta x'/c^2$，后方的先发生 |
| 时间延缓 | $\Delta t=\gamma\tau$，原时最短 |
| 长度收缩 | $l=l_0/\gamma$，原长最长，只在运动方向 |
| 间隔 | $(\Delta s)^2=c^2(\Delta t)^2-(\Delta l)^2$ 不变；因果关系的时序不变 |
| 速度变换 | $u_x'=\frac{u_x-v}{1-vu_x/c^2}$，$u_y'=\frac{u_y}{\gamma(1-vu_x/c^2)}$；不可能超光速 |
| 动量与力 | $\boldsymbol{p}=\gamma m\boldsymbol{v}$，$\boldsymbol{F}=\mathrm{d}\boldsymbol{p}/\mathrm{d}t$；$F_{\mathrm{t}}=\gamma^3ma_{\mathrm{t}}$，$F_{\mathrm{n}}=\gamma ma_{\mathrm{n}}$ |
| 能量 | $E=\gamma mc^2$，$E_0=mc^2$，$E_{\mathrm{k}}=(\gamma-1)mc^2$，$E^2=p^2c^2+m^2c^4$；光子 $E=pc=h\nu$ |
| 四维动量 | $(E/c,\boldsymbol{p})$ 与 $(ct,\boldsymbol{r})$ 同样变换 |

## 思考题

1. 时间延缓说"动钟变慢"，S 与 S′ 都认为对方的钟慢。这是否自相矛盾？

   **答** 两种判断比较的是不同的事件对；每个参考系用的是自己的一排对准的钟，而对方认为这排钟没有对准（[8.3 节](#sec-8.3)）。

2. 一个粒子的质量能否通过对它加速而改变？"运动的物体质量增大"这种说法错在哪里？

   **答** 质量 $m$ 是 Lorentz 不变量（$E^2-p^2c^2=m^2c^4$），增大的是能量 $\gamma mc^2$ 和动量（注 8.7.1）。

3. 一个盒子里的气体被加热后，盒子的质量是否变化？

   **答** 变化，$\Delta m=\Delta E_0/c^2$，但对日常的热量而言 $\Delta m$ 小到无法测量（$1\,\mathrm{J}$ 对应 $1.1\times10^{-17}\,\mathrm{kg}$）。

4. 探照灯的光斑在远处的云层上扫过的速度可以超过 $c$，这是否违背相对论？

   **答** 光斑上不同位置被照亮是没有因果联系的不同事件，不传递信号和能量，不受 $c$ 的限制。
