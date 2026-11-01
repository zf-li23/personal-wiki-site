---
title: 磁共振：NMR 的自旋物理、结构与动态，以及 EPR
description: 生物大分子的磁共振：核自旋与 Zeeman 能级，Bloch 方程、弛豫与自旋回波，弛豫与分子运动，蛋白质与核酸的谱图、多维谱与归属，NOE、残余偶极耦合与顺磁约束下的结构测定，化学交换与动态，EPR、自旋标记与 DEER，动态核极化与 MRI。
source_hash: 24f4c7e9a3a8
---

核磁共振（NMR）是结构生物学三种高分辨率方法中唯一能在室温溶液中研究分子的方法，它记录的不是一幅图像，而是一组关于原子对的数字：哪些核之间有化学键相连，哪些在空间中相互靠近，键如何取向，分子的各个部分运动得多快，又多久访问一次其他构象。结构就由这些数字计算得出。代价是陡峭的学习曲线和分子大小的限制；回报则是能够直接观察柔性、瞬态、弱结合和无序蛋白质，而这些正是晶体学（[7.6.10](/7.6.10)）和**冷冻电镜**（[7.6.14](/7.6.14)）看得不清甚至看不到的。电子顺磁共振（EPR）把同样的物理用于未成对电子，借助自旋标记，可以在任意大小的分子中测量数纳米的距离。

NMR 作为分析方法的原理（核自旋、共振条件、化学位移、耦合常数与 $n + 1$ 规则、谱仪、二维谱与 MRI）见 [6.4.12](/6.4.12)，有机自由基的 EPR 谱见 [6.5.7](/6.5.7#sec-7.4)，本章不再重复，而是沿着大分子所需的方向把物理推进一步。首先用经典图像描述自旋体系：磁化强度服从 Bloch 方程，由此解释脉冲、自由感应衰减、弛豫和回波（13.1–13.2）。接着通过关联函数与谱密度把弛豫和分子运动联系起来，说明为什么大分子的 NMR 变得困难，以及 TROSY 与氘代如何推迟这一极限（13.3）。用密度算符做量子描述，则可解释多维谱的脉冲序列，借此分辨并归属蛋白质的信号（13.4）。由 NOE、耦合、化学位移、残余偶极耦合和顺磁效应测得的距离、角度与取向，成为结构计算的约束条件（13.5）。弛豫、化学交换和氢交换则报告从皮秒到数月的各种运动（13.6）。随后是 EPR、定点自旋标记与 DEER（13.7），最后以同一套方程的医学应用磁共振成像（13.8）和各种方法的比较（13.9）收尾。驱动弛豫的**转动扩散**已在 [7.6.5](/7.6.5#sec-5.3.2) 讨论；化学交换背后的两态动力学见 [7.6.3](/7.6.3) 与 [7.6.4](/7.6.4)；受约束驱动的结构计算使用 [7.6.9](/7.6.9#alg-9.11.1) 的**模拟退火**；NMR 所测量的折叠与动力学是 [7.6.16](/7.6.16) 的主题。

## 13.1. 磁场中的核自旋

### 13.1.1. 简史

磁共振的历史是一连串物理实验，先发展为化学方法，继而成为生物学方法：

| 年份 | 事件 |
|---|---|
| 1922 | Stern 与 Gerlach：原子束中角动量的空间量子化（[5.5.4](/5.5.4#sec-4.2.2)）；1933 年 Stern 测得质子的磁矩 |
| 1938 | Rabi：分子束中用射频场实现核磁共振 |
| 1944 | Zavoisky：$\ce{CuCl2.2H2O}$ 中的电子顺磁共振 |
| 1946 | Bloch（水）与 Purcell（石蜡）：体相物质中的 NMR |
| 1948 | Bloembergen、Purcell 与 Pound：弛豫理论（BPP） |
| 1950 | Proctor 与 Yu：化学位移（$\ce{NH4NO3}$ 的两条 $^{14}\mathrm{N}$ 谱线）；Hahn：自旋回波 |
| 1951 | Gutowsky 与 McCall、Ramsey 与 Purcell：经键传递的标量耦合 |
| 1953–1955 | Overhauser：由电子到核的极化转移；Solomon：交叉弛豫方程 |
| 1966 | Ernst 与 Anderson：脉冲 Fourier 变换 NMR |
| 1971–1976 | Jeener 提出、Ernst 实现二维 NMR（COSY） |
| 1973 | Lauterbur 与 Mansfield：利用场梯度成像 |
| 1985 | Wüthrich 及其合作者：根据 NOE 距离约束得到第一个溶液中的蛋白质结构 |
| 1990 年代 | $^{13}\mathrm{C}/^{15}\mathrm{N}$ 标记、三共振谱、残余偶极耦合（1995–1997）、TROSY（1997） |
| 2000 年代 | 脉冲 EPR 距离测量（DEER）进入结构生物学；动态核极化；用弛豫色散和 CEST 研究不可见态 |

诺贝尔奖先后授予 Stern（1943）、Rabi（1944）、Bloch 与 Purcell（1952）、Ernst（1991）、Wüthrich（2002，化学奖）以及 Lauterbur 与 Mansfield（2003，生理学或医学奖）。

### 13.1.2. 核自旋与磁矩

原子核具有内禀角动量 $\boldsymbol{I}$，其大小为 $\hbar\sqrt{I(I + 1)}$，其中**核自旋量子数** $I$ 为整数或半整数，$z$ 分量为 $m\hbar$，$m = -I, \dots, I$（[6.4.12](/6.4.12#def-12.1.1)）。其磁矩与角动量平行或反平行，

$$
\boldsymbol{\mu} = \gamma\boldsymbol{I}, \tag{13.1}
$$
其中**旋磁比** $\gamma$ 是核的固有性质。$I$ 的取值规则来自核子的配对：质子数与中子数都是偶数时 $I = 0$（$^{12}\mathrm{C}$、$^{16}\mathrm{O}$、$^{32}\mathrm{S}$），这种核对 NMR 不可见；二者都是奇数时 $I$ 为非零整数（$^2\mathrm{H}$、$^{14}\mathrm{N}$）；质量数为奇数时 $I$ 为半整数。具体数值无法由此规则预言，需要查表。

| 核 | $I$ | $\gamma/(10^7\,\mathrm{rad\,s^{-1}\,T^{-1}})$ | $14.1\,\mathrm{T}$ 下的 $\lvert\nu_0\rvert$ / MHz | 天然丰度 / % | 在生物分子 NMR 中的用途 |
|---|---|---|---|---|---|
| $^1\mathrm{H}$ | 1/2 | 26.752 | 600.0 | 99.99 | 几乎所有实验中的检测核 |
| $^2\mathrm{H}$ | 1 | 4.107 | 92.1 | 0.012 | 氘代以减慢弛豫；溶剂锁场 |
| $^{13}\mathrm{C}$ | 1/2 | 6.728 | 150.9 | 1.07 | 均匀标记 |
| $^{14}\mathrm{N}$ | 1 | 1.934 | 43.4 | 99.63 | 四极矩，谱线宽；避免使用 |
| $^{15}\mathrm{N}$ | 1/2 | −2.713 | 60.8 | 0.37 | 均匀标记；主链酰胺 |
| $^{17}\mathrm{O}$ | 5/2 | −3.628 | 81.4 | 0.038 | 四极矩，很少使用 |
| $^{19}\mathrm{F}$ | 1/2 | 25.18 | 564.7 | 100 | 位点特异的探针（13.3.5） |
| $^{31}\mathrm{P}$ | 1/2 | 10.84 | 243.1 | 100 | 核酸主链、磷脂、代谢物 |

$I \ge 1$ 的核具有电四极矩，与电场梯度耦合而迅速弛豫，因此谱线很宽。生物分子 NMR 于是采用自旋为 1/2 的核；又因为 $^{12}\mathrm{C}$、$^{14}\mathrm{N}$ 和 $^{16}\mathrm{O}$ 都不能用，蛋白质和核酸要在以 $^{13}\mathrm{C}$-葡萄糖和 $^{15}\mathrm{NH_4Cl}$ 为唯一碳源和氮源的培养基中表达。$^{15}\mathrm{N}$ 的 $\gamma$ 为负（其磁矩与自旋反平行），使下文若干符号反转；质子的 $\gamma$ 在稳定核中最大（仅次于氚），所以只要可能就在 $^1\mathrm{H}$ 上检测。

### 13.1.3. Zeeman 能级与 Larmor 频率

在静磁场 $\boldsymbol{B}_0 = B_0\boldsymbol{e}_z$ 中，能量 $-\boldsymbol{\mu}\cdot\boldsymbol{B}_0$ 使 $2I + 1$ 个状态分裂（核 **Zeeman 效应**）：

$$
E_m = -\gamma\hbar B_0 m, \qquad \Delta E = E_{m-1} - E_m = \hbar\lvert\gamma\rvert B_0 . \tag{13.2}
$$

**定义 13.1.1（Larmor 频率）** 核在磁场 $B_0$ 中的 Larmor 频率为 $\omega_0 = -\gamma B_0$（角频率；$\nu_0 = \omega_0/2\pi$）。其大小等于跃迁 $\Delta m = \pm 1$ 中吸收或发射的光子频率，并且如定理 13.2.1 所示，也是磁矩绕磁场进动的角速度；其符号给出进动的方向。

对 $\gamma > 0$ 的自旋 1/2 核，状态 $m = +\frac12$（自旋向上，$\alpha$）能量较低。谱仪按质子频率命名：“600 MHz” 的磁体对应 $B_0 = 2\pi\times600\,\mathrm{MHz}/\gamma_{\mathrm{H}} = 14.1\,\mathrm{T}$，这一磁场由浸在液氦中的超导线圈产生，约为地磁场（$50\,\mu\mathrm{T}$）的 $3\times10^5$ 倍。在同一磁体中，$^{13}\mathrm{C}$ 的共振频率为 $150.9\,\mathrm{MHz}$，$^{15}\mathrm{N}$ 为 $60.8\,\mathrm{MHz}$。光子能量极小：$h\nu = 4.0\times10^{-25}\,\mathrm{J} = 2.5\,\mu\mathrm{eV}$，在室温下仅为 $10^{-4}\,k_{\mathrm{B}}T$（[7.6.6](/7.6.6)）。经典图像是磁矩在磁场中的 **Larmor 进动**（[5.3.8](/5.3.8#sec-8.2.5)）：能级之间的量子跃迁与矢量的经典进动这两种图像将在 13.2 中统一起来。

### 13.1.4. 极化、磁化强度与灵敏度

由于 $\Delta E \ll k_{\mathrm{B}}T$，**Boltzmann 分布**使两个能级的占据几乎相等：

$$
\frac{N_\alpha - N_\beta}{N_\alpha + N_\beta} = \tanh\frac{\hbar\gamma B_0}{2k_{\mathrm{B}}T} \approx \frac{\hbar\gamma B_0}{2k_{\mathrm{B}}T}. \tag{13.3}
$$

在 $14.1\,\mathrm{T}$、$298\,\mathrm{K}$ 下，质子的极化度为 $4.8\times10^{-5}$：每 $10^5$ 个质子中，沿磁场方向的比逆磁场方向的多 $2.4$ 个，只有这一多出的部分产生信号。把单位体积内 $N$ 个自旋的磁矩相加，就得到平衡**磁化强度**：

**公式 13.1.1（核磁化强度的 Curie 定律）**

$$
M_0 = \frac{N\gamma^2\hbar^2 I(I + 1)}{3k_{\mathrm{B}}T}B_0, \qquad M_0 = \frac{N\gamma^2\hbar^2B_0}{4k_{\mathrm{B}}T}\quad\left(I = \tfrac12\right). \tag{13.4}
$$
它正比于 $\gamma^2$（极化度 $\propto\gamma$，每个自旋的磁矩 $\propto\gamma$）以及 $B_0/T$。

接收线圈中感应的电压正比于 $\mathrm{d}M/\mathrm{d}t$，即正比于 $\omega_0M_0$，而噪声随频率增长较慢。仔细分析可得，激发一种核而检测另一种核的实验的信噪比为

$$
\frac{S}{N} \propto N\,\gamma_{\mathrm{exc}}\,\gamma_{\mathrm{det}}^{3/2}\,B_0^{3/2}\sqrt{n_{\mathrm{s}}}, \tag{13.5}
$$
其中 $n_{\mathrm{s}}$ 为扫描次数。由此有三点结论，决定着每个实验的设计。其一，在 $^1\mathrm{H}$ 上激发和检测，比直接检测 $^{15}\mathrm{N}$ 增益 $(\gamma_{\mathrm{H}}/\gamma_{\mathrm{N}})^{5/2} \approx 300$ 倍，因此要把极化由质子转移到杂核再转移回来（13.4.4）。其二，信号只随测量时间的平方根增长：信噪比加倍需要四倍的时间。其三，蛋白质样品必须浓缩：通常在 $0.3$–$0.5\,\mathrm{mL}$ 中达到 $0.1$–$1\,\mathrm{mM}$，即数毫克标记蛋白。低温探头（线圈与前置放大器冷却到约 $20\,\mathrm{K}$）可增益三至四倍；更高的磁场增益 $B_0^{3/2}$；而动态核极化（13.7.5）的超极化可以把极化度本身提高两个数量级。

## 13.2. Bloch 方程

### 13.2.1. 磁化强度的进动

宏观样品含有约 $10^{20}$ 个自旋，被操控与检测的是它们的总和，即磁化强度 $\boldsymbol{M}$。对于无相互作用的自旋，每个自旋的期望值服从磁矩在磁场中的经典方程，因为力矩 $\boldsymbol{\mu}\times\boldsymbol{B}$ 改变角动量：$\mathrm{d}\boldsymbol{I}/\mathrm{d}t = \boldsymbol{\mu}\times\boldsymbol{B}$。乘以 $\gamma$ 并对单位体积求和，得到：

**定理 13.2.1（磁化强度的进动）** 在磁场 $\boldsymbol{B}(t)$ 中且无弛豫时，

$$
\frac{\mathrm{d}\boldsymbol{M}}{\mathrm{d}t} = \gamma\,\boldsymbol{M}\times\boldsymbol{B}. \tag{13.6}
$$
在静磁场 $B_0\boldsymbol{e}_z$ 中，$M_z$ 为常数，横向分量转动：$M_x + \mathrm{i}M_y = (M_x + \mathrm{i}M_y)_0\,\mathrm{e}^{\mathrm{i}\omega_0t}$，$\omega_0 = -\gamma B_0$。磁化强度以 Larmor 频率绕磁场进动；若 $\gamma > 0$，从 $+z$ 方向看为顺时针。

**证明** 取 $\boldsymbol{B} = B_0\boldsymbol{e}_z$，式 (13.6) 给出 $\dot M_x = \gamma B_0M_y$，$\dot M_y = -\gamma B_0M_x$，$\dot M_z = 0$。令 $m = M_x + \mathrm{i}M_y$，则 $\dot m = \gamma B_0(M_y - \mathrm{i}M_x) = -\mathrm{i}\gamma B_0m$，其解为 $m(0)\mathrm{e}^{-\mathrm{i}\gamma B_0t} = m(0)\mathrm{e}^{\mathrm{i}\omega_0t}$。$\square$

量子与经典的描述是一致的：处于叠加态 $c_\alpha|\alpha\rangle + c_\beta|\beta\rangle$ 的自旋，其横向期望值以频率 $\Delta E/\hbar$ 转动，即式 (13.2) 中光子的频率。平衡时各自旋的相位随机，横向分量相互抵消，$\boldsymbol{M} = M_0\boldsymbol{e}_z$，没有可进动的分量。自旋并非字面意义上的“平行或反平行”于磁场；每个自旋都处在某个叠加态，式 (13.3) 的布居描述的是 $I_z$ 测量的统计结果。

### 13.2.2. 旋转坐标系与射频脉冲

为了把 $\boldsymbol{M}$ 从 $z$ 轴转开，射频线圈产生垂直于 $\boldsymbol{B}_0$ 的场 $2B_1\cos(\omega t)\boldsymbol{e}_x$，$B_1$ 约为 $B_0$ 的 $10^{-4}$。静态的横向场是无用的：它只在进动的矢量恰好指向某一方向时才使 $\boldsymbol{M}$ 倾斜，半个周期后又把它倾回去。线性振荡场是两个振幅为 $B_1$、绕 $z$ 轴向相反方向转动的分量之和；与自旋同向转动的那个起作用，另一个远离共振，可以忽略。在以射频频率绕 $z$ 轴转动的坐标系中，一切都变得简单。

**定义 13.2.1（旋转坐标系）** 旋转坐标系是绕 $\boldsymbol{B}_0$ 以发射机频率 $\omega$ 转动的坐标系 $(x', y', z)$。在其中，同向转动的射频分量是沿 $x'$ 的静态场 $B_1$，静磁场则减小为剩余的 $\Delta B = B_0 + \omega/\gamma$，于是 Larmor 频率为 $\omega_0$ 的自旋绕有效场进动：

$$
\gamma\boldsymbol{B}_{\mathrm{eff}} = (\gamma B_1, 0, -\Omega), \qquad \Omega = \omega_0 - \omega , \tag{13.7}
$$
其中 $\Omega$ 是自旋频率相对发射机的偏置。

共振时（$\Omega = 0$），有效场就是沿 $x'$ 的 $B_1$，$\boldsymbol{M}$ 在 $y'z$ 平面内以章动频率 $\omega_1 = \gamma B_1$ 转动。持续时间为 $t_{\mathrm{p}}$ 的脉冲使它转过翻转角 $\beta = \gamma B_1t_{\mathrm{p}}$；$90^\circ$ 脉冲（$\pi/2$）把全部 $M_0$ 放到横向平面内，$180^\circ$ 脉冲（$\pi$）使之反转。取 $\omega_1/2\pi = 25\,\mathrm{kHz}$，$90^\circ$ 脉冲持续 $10\,\mu\mathrm{s}$。偏离共振时，有效场偏离横向平面的角度为 $\arctan(\Omega/\omega_1)$，矢量到不了横向平面（下图 A 板）：脉冲只能均匀地激发偏置远小于 $\omega_1$ 的自旋，因此“硬”脉冲必须又短又强，而长的弱脉冲则选择性地激发窄带（用于溶剂抑制、CEST 和 MRI 的层面选择）。旋转坐标系还给出“共振”的经典含义：只有随自旋同步转动的场才能使它们转动，正如只有与秋千同相的推力才能使摆幅增大。同一论断的量子表述是：射频场在两个方向上等同地驱动 $\alpha \leftrightarrow \beta$ 跃迁。因此，长时间的弱辐照使布居相等并破坏磁化强度，这就是*饱和*，溶剂预饱和与饱和转移实验的基础。

### 13.2.3. 弛豫

式 (13.6) 保持 $\lvert\boldsymbol{M}\rvert$ 不变，但脉冲之后磁化强度会回到平衡。Bloch 加入了两个唯象的速率。

**定义 13.2.2（Bloch 方程）** Bloch 方程描述无相互作用自旋系综的磁化强度：

$$
\frac{\mathrm{d}\boldsymbol{M}}{\mathrm{d}t} = \gamma\,\boldsymbol{M}\times\boldsymbol{B} - \frac{M_x\boldsymbol{e}_x + M_y\boldsymbol{e}_y}{T_2} - \frac{M_z - M_0}{T_1}\boldsymbol{e}_z . \tag{13.8}
$$
时间常数 $T_1$ 支配 $M_z$ 向 $M_0$ 的恢复（**纵向弛豫**，[6.4.12](/6.4.12#sec-12.1.5)），$T_2$ 支配横向磁化强度的衰减（**横向弛豫**）；$R_1 = 1/T_1$ 与 $R_2 = 1/T_2$ 为弛豫速率。

$90^\circ$ 脉冲之后，在旋转坐标系中，解为

$$
M_{x'} + \mathrm{i}M_{y'} = \mathrm{i}M_0\,\mathrm{e}^{\mathrm{i}\Omega t}\mathrm{e}^{-t/T_2}, \qquad M_z = M_0\left(1 - \mathrm{e}^{-t/T_1}\right). \tag{13.9}
$$

两个过程的物理本质不同。纵向弛豫改变布居并与周围环境交换能量（历史上称“晶格”，故称自旋–晶格弛豫）。横向弛豫是自旋之间相位相干性的丧失：横向磁化强度是许多进动磁矩的矢量和，任何使它们相位发散的因素都会破坏它，而不一定改变能量。改变布居的跃迁同时也破坏相干，所以总有 $T_2 \le 2T_1$；对大分子则 $T_2 \ll T_1$。把 $T_2$ 称为“自旋–自旋弛豫”是历史遗留的说法，容易引起误解：自旋间的相互翻转只是退相位的原因之一，横向弛豫还包括局部场的一切缓慢涨落（13.3）。在样品中，不均匀的静磁场会增加可逆的退相位，观测到的衰减具有更快的常数 $T_2^*$，近似有 $1/T_2^* = 1/T_2 + \gamma\Delta B_0/2$；自旋回波可以把二者分开（13.2.5）。

![旋转坐标系中 Bloch 方程的数值解（约定 dM/dt = γM × B，γ > 0，故沿 x′ 的场使 M 由 z 转向 +y′）。A：在沿 x′ 的 90° 脉冲期间，共振自旋的磁化强度由 z 章动到横向平面（紫色）；偏离共振 Ω = 0.5 ω₁ 的自旋绕倾斜的有效场进动，到不了该平面（橙色）。脉冲之后，在有偏置并有弛豫的自由进动中，M 螺旋式地回到 z（虚线）。B：偏置为 5 Hz、T₂ = 0.1 s、T₁ = 0.3 s 时 90° 脉冲之后 M 的各分量：横向分量以 Ω 振荡并以 T₂ 衰减；M_z 以 T₁ 恢复](./plots/bloch.py)

### 13.2.4. 自由感应衰减与 Lorentz 线形

进动的横向磁化强度在线圈中感应出电压：**自由感应衰减**（FID，[6.4.12](/6.4.12#def-12.4.2)）。接收机把它与发射机频率混频，相当于电子学上进入旋转坐标系，并记录相差 $90^\circ$ 的两个通道（正交检测），其组合 $s(t) = M_{x'} + \mathrm{i}M_{y'}$ 可以区分正偏置与负偏置。对一条谱线，当 $t \ge 0$ 时 $s(t) = s_0\mathrm{e}^{\mathrm{i}\Omega t - R_2t}$，其 **Fourier 变换**为

$$
S(\omega) = \int_0^\infty s(t)\mathrm{e}^{-\mathrm{i}\omega t}\,\mathrm{d}t = s_0\frac{R_2 - \mathrm{i}(\omega - \Omega)}{R_2^2 + (\omega - \Omega)^2}. \tag{13.10}
$$

**公式 13.2.1（Lorentz 线形）** 式 (13.10) 的实部即吸收谱线，是一个 Lorentz 线形，其角频率半高全宽为 $2R_2$，即

$$
\Delta\nu_{1/2} = \frac{R_2}{\pi} = \frac{1}{\pi T_2}, \tag{13.11}
$$
其面积 $\pi s_0$ 与 $T_2$ 无关。虚部是色散线形，较宽，并在 $\Omega$ 处变号。

因此宽度加倍的谱线高度减半，线宽增加既损失信号也损失分辨率。归一化到单位面积的 Lorentz 线形是 **Cauchy 分布**（[3.1](/3.1)）的密度，具有重尾：相互重叠的谱线在远离中心处仍相互干扰。多条谱线的谱中，$s(t)$ 是这类项之和；它以间隔 $\Delta t$ 采样（由采样定理，谱宽为 $1/\Delta t$），采集时间为 $t_{\mathrm{acq}}$（数字分辨率为 $1/t_{\mathrm{acq}}$），再用**快速 Fourier 变换**（[4.4](/4.4)）变换。变换之前通常把 FID 乘以窗函数：指数窗以增宽为代价提高信噪比，正弦钟形窗以信噪比为代价提高分辨率。还必须校正谱的相位，使所有谱线都呈纯吸收形。

![自由感应衰减与谱。A：偏置为 50 与 120 Hz、T₂ 分别为 50 ms 与 20 ms 的两条谱线的正交检测 FID（实部与虚部通道）。B：其 Fourier 变换的实部（吸收）与虚部（色散）：线宽 1/(πT₂) 分别为 6.4 与 15.9 Hz、面积相等的 Lorentz 线形，所以较宽的谱线较低。C：600 MHz 下 8、25、50 与 100 kDa 折叠蛋白的 ¹H 谱酰胺区的模拟（每 110 Da 一个酰胺，位移在 8.2 ppm 附近随机取值；每 kDa 的 τc = 0.5 ns；线宽来自刚性分子中酰胺 ¹⁵N 与邻近两个质子的偶极弛豫）。线宽随分子增大而增大，谱线数目也随之增加，使大蛋白的一维谱无法分辨](./plots/fid.py)

### 13.2.5. 自旋回波

当样品各部分的磁场略有不同时，自旋以略有差异的频率进动并扇形散开，FID 的衰减比 $T_2$ 更快。Hahn（1950）发现这一衰减是可逆的。

**定义 13.2.3（自旋回波）** 自旋回波是在激发后时间 $\tau$ 施加 $180^\circ$ 脉冲所产生的横向磁化强度的重聚：每个自旋的相位 $\phi = \Omega\tau$ 变为 $\pi - \phi$（对于绕 $x'$ 的脉冲，横向矢量被反射穿过 $x'z$ 平面），再经过时间 $\tau$ 后，无论偏置多大，每个自旋都到达同一相位。在 $t = 2\tau$ 时磁化强度重聚，仅因不可逆弛豫而衰减 $\mathrm{e}^{-2\tau/T_2}$。

回波消除了在 $2\tau$ 内保持静态且线性地进入频率的一切相互作用：场的不均匀性、化学位移偏置，以及（对杂核对，当只对其中一个自旋施加脉冲时）标量耦合。它消除不了比 $\tau$ 更快的随机涨落，即真正的 $T_2$，也消除不了在回波两半之间改变自旋频率的较慢过程，特别是化学交换（13.6.2）。改变 $\tau$ 并记录回波幅度即可测得 $T_2$；以 $2\tau$ 为间隔的一串 $180^\circ$ 脉冲，即 Carr–Purcell–Meiboom–Gill（CPMG）序列，在一次实验中用许多回波测量它，并通过把重聚脉冲沿 $y'$ 施加来抑制脉冲误差的影响。CPMG 脉冲串也是弛豫色散的工具（13.6.4）。$T_1$ 用反转恢复法测量：$180^\circ$ 脉冲使 $M_z$ 反转，它按 $M_0(1 - 2\mathrm{e}^{-\tau/T_1})$ 恢复，经可变延迟 $\tau$ 之后用 $90^\circ$ 脉冲读出。

![Hahn 自旋回波的模拟，偏置取标准差为 6 Hz 的 Gaussian 分布，真实 T₂ 为 0.15 s。A：旋转坐标系中 15 个等色团的横向磁化强度，依次为 90°ₓ 脉冲刚结束时（全部沿 +y′）、τ 时（扇形散开）、180°ₓ 脉冲刚结束时（每个矢量被反射，最快的现在落在最后）和 2τ 时（沿 −y′ 重聚）。B：τ = 60 ms 时净横向磁化强度的模：FID 以 T₂* 衰减，2τ 处的回波把信号恢复到仅差因子 exp(−2τ/T₂)，其他 τ 的回波极大值（圆点）描出 exp(−t/T₂)](./plots/spin-echo.py)

![脉冲序列（示意图，未按比例；窄条为 90° 脉冲，宽条为 180° 脉冲）。A：测 T₁ 的反转恢复与测 T₂ 和弛豫色散的 CPMG 脉冲串，ν_CPMG = 1/(4τ)。B：¹H–¹⁵N HSQC：INEPT 把极化由 ¹H 转移到 ¹⁵N，¹⁵N 化学位移在 t₁ 期间演化，中间的一个 ¹H 180° 脉冲用于去除耦合，反向 INEPT 转回 ¹H，并在 ¹⁵N 去耦下于 t₂ 期间采集；各点 1–4 处的乘积算符状态写在上方（13.4.4）。C：四脉冲 DEER：在一个微波频率下的观测脉冲 π/2–π–π 产生重聚回波，第二个频率下的泵浦 π 脉冲在间隔内随时间 t 步进，使配偶自旋反转并以偶极频率调制回波（13.7.4）](./plots/pulse-sequences.py)

## 13.3. 弛豫与分子运动

### 13.3.1. 涨落的局部场

Bloch 方程把 $T_1$ 与 $T_2$ 当作已知量；弛豫理论则把它们计算出来，同时使弛豫成为探测运动的手段。分子中的原子核除了 $\boldsymbol{B}_0$ 之外，还感受到来自分子自身的微小局部场，这些场依赖于分子的取向：

- 邻近自旋的偶极场：对相距 $0.18\,\mathrm{nm}$ 的质子约为 $0.5\,\mathrm{mT}$，按 $(3\cos^2\theta - 1)/r^3$ 变化，$\theta$ 为核间矢量与 $\boldsymbol{B}_0$ 的夹角；
- 化学位移各向异性（CSA）：电子的屏蔽（[6.4.12](/6.4.12#sec-12.2.1)）是张量，所以位移依赖于分子的取向；对酰胺 $^{15}\mathrm{N}$，各向异性约为 $-170\,\mathrm{ppm}$，其唯一轴几乎沿 N–H 键，所产生的场随 $B_0$ 增大；
- 对四极核，是电四极耦合；对顺磁样品，是未成对电子的场（13.5.4）。

在溶液中分子不断翻滚，这些场平均为零：$3\cos^2\theta - 1$ 在球面上的平均值为零，这就是溶液谱显示尖锐的谱线、各向同性的位移而没有偶极裂分的原因。但这些场是涨落的，含有 Larmor 频率分量的涨落场与射频场一样驱动跃迁，而它的缓慢分量则使进动相位随机化。所以弛豫速率取决于涨落的功率有多少落在各个频率上。

### 13.3.2. 关联函数与谱密度

设 $\boldsymbol{u}(t)$ 为沿核间键的单位矢量。因为偶极与 CSA 相互作用都是二阶张量，相关的取向函数是 $P_2(x) = (3x^2 - 1)/2$，即**Legendre 多项式**中的第二个。

**定义 13.3.1（谱密度函数）** 键矢量的取向关联函数为 $C(t) = \langle P_2(\boldsymbol{u}(0)\cdot\boldsymbol{u}(t))\rangle$，对系综取平均，$C(0) = 1$。其余弦变换

$$
J(\omega) = \frac25\int_0^\infty C(t)\cos(\omega t)\,\mathrm{d}t , \tag{13.12}
$$
就是谱密度函数，即取向涨落在角频率 $\omega$ 处的功率（因子 $2/5$ 是球谐函数的归一化）。

对于各向同性**转动扩散**（系数为 $D_{\mathrm{r}}$）的刚性分子，$P_2$ 关联函数按 $\mathrm{e}^{-6D_{\mathrm{r}}t}$ 衰减（[7.6.5](/7.6.5#def-5.3.1)），因此令**转动相关时间** $\tau_{\mathrm{c}} = 1/(6D_{\mathrm{r}})$，则

$$
C(t) = \mathrm{e}^{-t/\tau_{\mathrm{c}}}, \qquad J(\omega) = \frac25\,\frac{\tau_{\mathrm{c}}}{1 + \omega^2\tau_{\mathrm{c}}^2}, \qquad \tau_{\mathrm{c}} = \frac{4\pi\eta r_{\mathrm{h}}^3}{3k_{\mathrm{B}}T}, \tag{13.13}
$$
最后一式是对**流体力学半径**为 $r_{\mathrm{h}}$ 的球体的 Stokes–Einstein–Debye 关系（即 **Stokes–Einstein 方程**的转动类比）。谱密度在 $\omega \approx 1/\tau_{\mathrm{c}}$ 以下是平的，$J(\omega) \approx \frac25\tau_{\mathrm{c}}$，此后按 $\omega^{-2}$ 下降。分子越慢，低频功率越多、高频功率越少；总量 $\int_0^\infty J\,\mathrm{d}\omega = \pi/5$ 是固定的。

**例 13.3.1（蛋白质的相关时间）** 对每克蛋白质含 $0.3\,\mathrm{g}$ 水合水的情形，式 (13.13) 在 $25\,{}^\circ\mathrm{C}$ 下给出每 kDa 约 $0.37\,\mathrm{ns}$；实测值更大，约为每 kDa $0.5$–$0.6\,\mathrm{ns}$，因为真实的蛋白质不是球形，水合层也更厚。**泛素**（$8.6\,\mathrm{kDa}$）在 $25\,{}^\circ\mathrm{C}$ 的水中 $\tau_{\mathrm{c}} \approx 4\,\mathrm{ns}$，$25\,\mathrm{kDa}$ 的蛋白质为 $12$–$15\,\mathrm{ns}$，$100\,\mathrm{kDa}$ 的蛋白质约为 $50\,\mathrm{ns}$。由于 $\tau_{\mathrm{c}} \propto \eta/T$，把样品从 25 冷却到 $5\,{}^\circ\mathrm{C}$ 使 $\tau_{\mathrm{c}}$ 几乎翻倍（水的黏度由 $0.89$ 升到 $1.52\,\mathrm{mPa\,s}$），而 $\mathrm{D_2O}$ 的黏度比 $\mathrm{H_2O}$ 高 25 %。

### 13.3.3. BPP 理论

含时微扰论把每个弛豫速率表示为谱密度在涨落场能够驱动的各跃迁频率处的取值之和。对于相距 $r$、以偶极相互作用耦合的两个全同自旋 1/2，Bloembergen、Purcell 与 Pound 得到：

**定理 13.3.1（BPP 弛豫速率）** 令 $K = \frac{\mu_0}{4\pi}\frac{\gamma^2\hbar}{r^3}$，$j(\omega) = \tau_{\mathrm{c}}/(1 + \omega^2\tau_{\mathrm{c}}^2)$，则

$$
\frac{1}{T_1} = \frac{3}{10}K^2\left[j(\omega_0) + 4j(2\omega_0)\right], \qquad \frac{1}{T_2} = \frac{3}{20}K^2\left[3j(0) + 5j(\omega_0) + 2j(2\omega_0)\right]. \tag{13.14}
$$

式 (13.14) 的结构解释了溶液中分子 NMR 的主要事实：

- $T_1$ 只依赖于 $\omega_0$ 与 $2\omega_0$ 处的谱密度，即能够交换能量的频率。作为 $\tau_{\mathrm{c}}$ 的函数，它在 $\omega_0\tau_{\mathrm{c}} = 0.616$ 处经过极小值，此时涨落在 Larmor 频率处最有效，运动变慢后 $T_1$ 又增大。
- $T_2$ 含有零频项 $j(0) = \tau_{\mathrm{c}}$，即只使相位随机化的缓慢涨落的“长期”贡献。运动变慢时它无限制地减小，这就是溶液 NMR 大小限制的来源。
- 在极端窄化极限 $\omega_0\tau_{\mathrm{c}} \ll 1$（小分子、水）下，$T_1 = T_2 = (\frac32K^2\tau_{\mathrm{c}})^{-1}$，均为数秒；大分子则有 $\omega_0\tau_{\mathrm{c}} \gg 1$（在 $600\,\mathrm{MHz}$ 下，$\tau_{\mathrm{c}} = 10\,\mathrm{ns}$ 时 $\omega_0\tau_{\mathrm{c}} = 38$），$T_1$ 变长而 $T_2$ 变短。

对相距 $0.18\,\mathrm{nm}$ 的质子对，$K/2\pi = 21\,\mathrm{kHz}$。取 $\tau_{\mathrm{c}} = 25\,\mathrm{ns}$（$50\,\mathrm{kDa}$ 的蛋白质），$1/T_2 \approx \frac{9}{20}K^2\tau_{\mathrm{c}} = 200\,\mathrm{s^{-1}}$，在计入其他邻居之前，谱线已宽达 $60\,\mathrm{Hz}$。在未氘代的蛋白质中，每个质子在 $0.3\,\mathrm{nm}$ 之内都有若干邻居，$^1\mathrm{H}$–$^1\mathrm{H}$ 耦合的稠密网络主导了质子的弛豫。

### 13.3.4. 主链酰胺 $^{15}\mathrm{N}$ 的弛豫

主链酰胺 $^{15}\mathrm{N}$ 是弛豫研究的主力，因为它的弛豫由几何关系相同的两种相互作用主导：与自身质子在固定距离 $r_{\mathrm{NH}} = 0.102\,\mathrm{nm}$ 处的偶极耦合，以及其自身的 CSA，二者的轴都接近键方向。两者都报告单个 N–H 矢量（每个残基一个）的重新取向，并可在分辨良好的 $^1\mathrm{H}$–$^{15}\mathrm{N}$ 相关谱中观测。

**公式 13.3.1（主链酰胺 $^{15}\mathrm{N}$ 的弛豫）** 令 $d = \frac{\mu_0\hbar\gamma_{\mathrm{H}}\gamma_{\mathrm{N}}}{4\pi r_{\mathrm{NH}}^3}$，$c = \omega_{\mathrm{N}}\Delta\sigma/\sqrt3$（$\Delta\sigma \approx -170\,\mathrm{ppm}$），$J(\omega)$ 如式 (13.12)，则

$$
\begin{aligned}
R_1 &= \frac{d^2}{4}\left[J(\omega_{\mathrm{H}} - \omega_{\mathrm{N}}) + 3J(\omega_{\mathrm{N}}) + 6J(\omega_{\mathrm{H}} + \omega_{\mathrm{N}})\right] + c^2J(\omega_{\mathrm{N}}),\\
R_2 &= \frac{d^2}{8}\left[4J(0) + J(\omega_{\mathrm{H}} - \omega_{\mathrm{N}}) + 3J(\omega_{\mathrm{N}}) + 6J(\omega_{\mathrm{H}}) + 6J(\omega_{\mathrm{H}} + \omega_{\mathrm{N}})\right] + \frac{c^2}{6}\left[4J(0) + 3J(\omega_{\mathrm{N}})\right] + R_{\mathrm{ex}},\\
\mathrm{NOE} &= 1 + \frac{\gamma_{\mathrm{H}}}{\gamma_{\mathrm{N}}}\,\frac{d^2}{4R_1}\left[6J(\omega_{\mathrm{H}} + \omega_{\mathrm{N}}) - J(\omega_{\mathrm{H}} - \omega_{\mathrm{N}})\right].
\end{aligned} \tag{13.15}
$$
这里 NOE 是稳态异核 Overhauser 增强，即质子饱和与否时 $^{15}\mathrm{N}$ 强度之比，$R_{\mathrm{ex}}$ 是化学交换的贡献（13.6.2）。

三个速率在频率 $0$、$\omega_{\mathrm{N}}$、$\omega_{\mathrm{H}}$ 与 $\omega_{\mathrm{H}} \pm \omega_{\mathrm{N}}$ 处对 $J(\omega)$ 取样，相当于对每个键的运动做粗略的谱分析。它们的灵敏度各不相同（下图）：$R_2$ 通过 $J(0)$ 随 $\tau_{\mathrm{c}}$ 线性增长，报告慢运动与交换；$R_1$ 在 $\tau_{\mathrm{c}} \approx 2\,\mathrm{ns}$ 附近达到峰值；NOE 对 $\omega_{\mathrm{H}}$ 附近的快运动敏感，当 $\tau_{\mathrm{c}} \gtrsim 5\,\mathrm{ns}$ 时趋近刚性极限值约 $0.8$，而对在亚纳秒时间尺度上运动的柔性末端和环区则变小甚至为负（因为 $\gamma_{\mathrm{N}} < 0$）。实际上，低 NOE 是无序最简单的标志。刚性残基的 $R_2/R_1$ 给出整个分子的 $\tau_{\mathrm{c}}$，进而报告寡聚状态（二聚体的翻滚约慢一倍），并由它在残基间的变化给出翻滚的各向异性。

**例 13.3.2（600 MHz 下的小蛋白）** 对泛素刚性部分的一个残基（$\tau_{\mathrm{c}} = 4.1\,\mathrm{ns}$），内部运动由 $S^2 = 0.85$ 与 $\tau_{\mathrm{e}} = 50\,\mathrm{ps}$ 描述（13.6.3），式 (13.15) 在 $14.1\,\mathrm{T}$ 下给出 $R_1 = 2.2\,\mathrm{s^{-1}}$，$R_2 = 6.1\,\mathrm{s^{-1}}$，$\mathrm{NOE} = 0.70$，与实测值接近。柔性 C 端尾部的一个残基，$S^2 = 0.3$，$\tau_{\mathrm{e}} = 0.5\,\mathrm{ns}$，则给出 $R_1 = 1.8\,\mathrm{s^{-1}}$，$R_2 = 3.2\,\mathrm{s^{-1}}$，$\mathrm{NOE} = -0.56$。

![弛豫速率随转动相关时间的变化（除非另有说明，均为刚性各向同性翻滚）。A：600 MHz 下相距 0.18 nm 的质子对的 BPP 理论；T₁ 在 ω₀τc = 0.62 处有极小值，T₂ 单调下降；在极端窄化区 T₁ = T₂。上方横轴给出每 kDa 0.5 ns 时球状蛋白的质量。B：主链酰胺在 600 MHz 与 1 GHz 下的 ¹⁵N R₁ 与 R₂。C：{¹H}–¹⁵N 异核 NOE。D：Lipari–Szabo 模型：三个序参量下的内部关联函数 C_I(t) = S² + (1 − S²)exp(−t/τe)（实线）与 τm = 5 ns 时的总关联函数 C(t) = C_I(t)exp(−t/τm)（虚线）](./plots/relaxation.py)

### 13.3.5. 大小限制及其突破

溶液 NMR 的大小限制有两个同时增长的原因。线宽通过 $J(0)$ 项与 $\tau_{\mathrm{c}}$ 成正比，从而与分子质量成正比；信号数目也与质量成正比，使重叠按平方增长。脉冲序列中的每一步转移还按 $\mathrm{e}^{-R_2t}$ 损失信号。因此常规的结构测定限于约 $25$–$30\,\mathrm{kDa}$，而主链归属在约 $50\,\mathrm{kDa}$ 以上就变得困难。有四种策略可以扩展这一范围。

1. 氘代。在 $\mathrm{D_2O}$ 中表达蛋白质，使与碳相连的质子被氘取代，氘的 $\gamma$ 小 6.5 倍，其偶极场对弛豫的贡献约小 40 倍。在 $\mathrm{H_2O}$ 中纯化之后，可交换的酰胺位点重新质子化，留下一个稀疏的 $^1\mathrm{H}^{\mathrm{N}}$ 自旋网络，$T_2$ 较长。
2. TROSY。在 $^1\mathrm{H}$–$^{15}\mathrm{N}$ 对中，偶极场与 $^{15}\mathrm{N}$ 的 CSA 场随同一分子运动涨落，二者相互干涉：对于因与质子耦合而分裂的 $^{15}\mathrm{N}$ 二重峰，其中一条线的两种场相加，另一条线的两种场部分抵消。

   **定义 13.3.2（TROSY）** TROSY（横向弛豫优化谱，transverse relaxation-optimized spectroscopy；Pervushin、Riek、Wider 与 Wüthrich，1997）是一类脉冲序列，它们在每个维度上选出标量耦合多重峰中偶极耦合与化学位移各向异性的弛豫相互抵消的那个成分，而不是通过去耦把各成分平均。在慢翻滚极限下，两个成分的横向速率近似为 $R_{\mathrm{DD}} + R_{\mathrm{CSA}} \pm 2\sqrt{R_{\mathrm{DD}}R_{\mathrm{CSA}}}\,P_2(\cos\beta)$，其中 $\beta \approx 17^\circ$ 为键与 CSA 轴之间的夹角。

   因为 $R_{\mathrm{CSA}} \propto B_0^2$ 而 $R_{\mathrm{DD}}$ 与场无关，当 $\sqrt{R_{\mathrm{CSA}}}P_2(\cos\beta) = \sqrt{R_{\mathrm{DD}}}$ 时抵消最彻底，对酰胺 $^{15}\mathrm{N}$ 约在 $1\,\mathrm{GHz}$ 附近。对于 $1\,\mathrm{GHz}$ 下 $\tau_{\mathrm{c}} = 50\,\mathrm{ns}$ 的情形，去耦后的 $^{15}\mathrm{N}$ 谱线仅由这两种相互作用就有 $R_2 \approx 104\,\mathrm{s^{-1}}$，而 TROSY 成分约为 $13\,\mathrm{s^{-1}}$（远处的质子还会使之增加，氘代可以减小这一部分）。结合氘代与 TROSY，可以记录 $100\,\mathrm{kDa}$ 以上蛋白质的主链谱。
3. 甲基 TROSY。在氘代的蛋白质中，把异亮氨酸、亮氨酸与缬氨酸的甲基选择性地标记为 $^{13}\mathrm{CH_3}$，则甲基内部类似的抵消使一半的甲基信号弛豫很慢。甲基在疏水核心与界面中数目众多，并绕其轴快速转动；用这一方法，Kay 及其合作者研究了接近 $1\,\mathrm{MDa}$ 的复合物（如 20S **蛋白酶体**）的动力学与**别构**。
4. $^{19}\mathrm{F}$ NMR。在单一位点引入氟（氟代氨基酸或半胱氨酸上的氟代标签），得到一条谱线，灵敏度为 $^1\mathrm{H}$ 的 $83\,\%$，化学位移对环境高度敏感，生物样品无背景信号，也无需归属；它用于膜蛋白和细胞中的大型组装体，代价是只得到单个位点的信息。

固体 NMR 以另一种方式回避这一问题：没有翻滚就没有 $\tau_{\mathrm{c}}$，各向异性相互作用改由**魔角旋转**（[6.4.12](/6.4.12#def-12.6.1)）平均，信号通过**交叉极化**转移。它是研究**淀粉样纤维**、脂双层中的膜蛋白和其他不溶性组装体的首选方法。

## 13.4. 生物分子的谱

### 13.4.1. 蛋白质与核酸的化学位移

**化学位移** $\delta = (\nu - \nu_{\mathrm{ref}})/\nu_{\mathrm{ref}}\times10^6$（[6.4.12](/6.4.12#def-12.2.2)）在水溶液的生物样品中以水溶性的 DSS（4,4-二甲基-4-硅杂戊烷-1-磺酸）的甲基信号为参考，而不用 TMS；$^{13}\mathrm{C}$ 与 $^{15}\mathrm{N}$ 的位移则通过其频率与 DSS 质子频率的固定比值间接参考。在质子频率为 $800\,\mathrm{MHz}$ 的谱仪上，$^1\mathrm{H}$ 的 $1\,\mathrm{ppm}$ 为 $800\,\mathrm{Hz}$，所以酰胺区中心（$\approx 8.2\,\mathrm{ppm}$）距 $4.77\,\mathrm{ppm}$（$25\,{}^\circ\mathrm{C}$）的水信号约 $2.8\,\mathrm{kHz}$。蛋白质中的典型范围：

| 质子 | $\delta/\mathrm{ppm}$ |
|---|---|
| 甲基（Ala、Val、Leu、Ile、Thr、Met） | $0$–$1.5$（核心中受环电流位移的甲基可低至 $-1$） |
| 其他脂肪族侧链 | $1.5$–$3.5$ |
| $\mathrm{H}^\alpha$ | $3.5$–$5.5$ |
| 芳环质子 | $6.5$–$7.8$ |
| 主链酰胺 $\mathrm{H}^{\mathrm{N}}$ | 折叠蛋白中 $6.5$–$10.5$；无序蛋白中 $7.8$–$8.6$ |
| Trp 吲哚 $\mathrm{H}^{\varepsilon1}$ | $\approx 10$ |
| 核酸：碱基配对的 G 与 U/T 的亚氨基质子 | $10$–$15$ |

位移是局部结构的报告者。在折叠蛋白中，氢键、邻近芳环的**环电流效应**和局部电场使酰胺信号分布在 $4\,\mathrm{ppm}$ 的范围内；在**内在无序蛋白**中，每个残基快速采样许多构象，其位移被平均到无规卷曲值附近，所有酰胺都挤在 $7.8$ 到 $8.6\,\mathrm{ppm}$ 之间。因此一维谱一眼就能看出蛋白质是否折叠。在核酸中，亚氨基质子只有在碱基对中形成氢键时才免于与水交换：$10\,\mathrm{ppm}$ 以上的信号数目即稳定碱基对的数目，其位移则可区分 Watson–Crick G·C 对（$12$–$13.5\,\mathrm{ppm}$）、A·U 对（$13$–$15\,\mathrm{ppm}$）与 G·U 摆动碱基对（$10$–$12\,\mathrm{ppm}$）。1970 年代，tRNA 与寡核苷酸双链的亚氨基谱给出了溶液中形成的是 Watson–Crick 配对而非 Hoogsteen 配对的第一个直接证据。

主链位移 $\mathrm{C}^\alpha$、$\mathrm{C}^\beta$、$\mathrm{C}'$ 与 $\mathrm{H}^\alpha$ 相对于无规卷曲值的偏差，即二级化学位移（secondary chemical shift），报告**二级结构**：螺旋中 $\mathrm{C}^\alpha$ 向低场（正）位移 $2$–$3\,\mathrm{ppm}$，链中则向高场位移，$\mathrm{C}^\beta$ 则相反。TALOS-N 等程序通过与已知结构蛋白质的数据库比较，由一个残基及其邻居的位移预测主链二面角 $\phi$、$\psi$，精度为 $10$–$15^\circ$；每次归属都免费给出的位移，因此就是结构的第一批约束。

### 13.4.2. 标量耦合与 Karplus 关系

经键的**自旋–自旋耦合**（[6.4.12](/6.4.12#def-12.3.1)）使谱线按**耦合常数** $J$ 裂分，与 $B_0$ 无关。在蛋白质中，单键耦合用于在成键的核之间转移磁化强度（13.4.4）；其大小决定脉冲序列的延迟：

| 耦合 | $^1J(\mathrm{N},\mathrm{H}^{\mathrm{N}})$ | $^1J(\mathrm{C}^\alpha,\mathrm{H}^\alpha)$ | $^1J(\mathrm{C}^\alpha,\mathrm{C}')$ | $^1J(\mathrm{N},\mathrm{C}')$ | $^1J(\mathrm{N},\mathrm{C}^\alpha)$ | $^2J(\mathrm{N},\mathrm{C}^\alpha_{i-1})$ |
|---|---|---|---|---|---|---|
| $\lvert J\rvert/\mathrm{Hz}$ | 92 | 140 | 55 | 15 | 7–11 | 4–9 |

（$^1J_{\mathrm{NH}}$ 为负，因为 $\gamma_{\mathrm{N}} < 0$。）三键耦合通过 **Karplus 关系**（[6.4.12](/6.4.12#def-12.3.2)）依赖于二面角。

**公式 13.4.1（主链的 Karplus 关系）** 酰胺质子与 $\alpha$ 质子之间的耦合依赖于主链角 $\phi$：

$$
{}^3J(\mathrm{H}^{\mathrm{N}}, \mathrm{H}^\alpha) = A\cos^2\theta + B\cos\theta + C, \qquad \theta = \phi - 60^\circ, \tag{13.16}
$$
其中 $A = 6.51\,\mathrm{Hz}$，$B = -1.76\,\mathrm{Hz}$，$C = 1.60\,\mathrm{Hz}$（Vuister 与 Bax，1993，由已知结构的蛋白质标定）；$\theta$ 是二面角 $\mathrm{H}^{\mathrm{N}}$–N–$\mathrm{C}^\alpha$–$\mathrm{H}^\alpha$。

在 $\alpha$ 螺旋中（$\phi \approx -57^\circ$）$^3J \approx 4\,\mathrm{Hz}$，在 $\beta$ 链中（$\phi \approx -120$ 到 $-140^\circ$）为 $8$–$10\,\mathrm{Hz}$；$6$–$8\,\mathrm{Hz}$ 的值表示对多种构象的平均。该关系是多值的（一个 $J$ 对应至多四个 $\phi$），需要结合**Ramachandran 图**中多数残基限于 $\phi < 0$ 这一点使用。其他 Karplus 关系由 $^3J(\mathrm{H}^\alpha,\mathrm{H}^\beta)$ 与 $^3J(\mathrm{N},\mathrm{H}^\beta)$ 给出 $\chi_1$，由 $^3J(\mathrm{H}1',\mathrm{H}2')$ 给出核酸的糖环折叠，由与 $^{31}\mathrm{P}$ 的耦合给出 RNA 的主链扭转角。

### 13.4.3. 量子描述：密度算符与乘积算符

只要耦合起作用，矢量模型就失效了：耦合自旋的磁化强度可以转化为没有经典类比的状态，如反相磁化强度和多量子相干，多维实验的全部信息都由它们携带。因此需要量子描述，它是 $2\times2$ 矩阵线性代数的一个优美应用。

单个自旋 1/2 的基态为 $|\alpha\rangle = (1, 0)^{\mathsf T}$ 与 $|\beta\rangle = (0, 1)^{\mathsf T}$，自旋算符（以 $\hbar$ 为单位）是 $\hat{I}_k = \frac12\sigma_k$，其中 $\sigma_k$ 为 Pauli 矩阵：

$$
\hat{I}_x = \frac12\begin{bmatrix}0 & 1\\ 1 & 0\end{bmatrix}, \quad \hat{I}_y = \frac12\begin{bmatrix}0 & -\mathrm{i}\\ \mathrm{i} & 0\end{bmatrix}, \quad \hat{I}_z = \frac12\begin{bmatrix}1 & 0\\ 0 & -1\end{bmatrix}, \tag{13.17}
$$
它们是本征值为 $\pm\frac12$ 的 **Hermite 矩阵**，并满足角动量的**换位子**关系 $[\hat{I}_x, \hat{I}_y] = \mathrm{i}\hat{I}_z$（循环置换）。样品不是处于一个态的一个自旋，而是处于不同态的自旋系综，需要用矩阵来描述。

**定义 13.4.1（密度算符）** 对于其中比例为 $p_k$ 的成员处于态 $|\psi_k\rangle$ 的系综，**密度算符**为 $\hat\rho = \sum_kp_k|\psi_k\rangle\langle\psi_k|$。可观测量 $\hat{Q}$ 的期望值为 $\langle\hat{Q}\rangle = \operatorname{tr}(\hat{Q}\hat\rho)$。它的对角元是基态的布居，非对角元即相干，只有当各成员的相位相关时才不为零；横向磁化强度就是 $|\alpha\rangle$ 与 $|\beta\rangle$ 之间的相干。

密度算符在 Schrödinger 方程下的演化为

$$
\frac{\mathrm{d}\hat\rho}{\mathrm{d}t} = -\mathrm{i}[\hat{H}, \hat\rho] \quad\Longrightarrow\quad \hat\rho(t) = \mathrm{e}^{-\mathrm{i}\hat{H}t}\,\hat\rho(0)\,\mathrm{e}^{\mathrm{i}\hat{H}t} \tag{13.18}
$$
其中 Hamilton 量 $\hat{H}$（以角频率为单位）在该时间间隔内为常数（Liouville–von Neumann 方程；解用到**矩阵指数**）。脉冲序列是一连串具有不同常数 Hamilton 量的时间间隔，最终的 $\hat\rho$ 由逐个间隔地应用式 (13.18) 的“夹心”得到。热平衡时 $\hat\rho = \mathrm{e}^{-\hat{H}/k_{\mathrm{B}}T}/Z \approx \frac12\hat{E} + \frac{\hbar\gamma B_0}{2k_{\mathrm{B}}T}\hat{I}_z$，其中 $\hat{E}$ 为单位算符；单位部分永不改变也不产生信号，所以实验从 $\hat\rho(0) \propto \hat{I}_z$ 开始。

对多个自旋，算符是张量积（$2\hat{I}_x\hat{S}_z$ 是 $4\times4$ 矩阵），16 个乘积 $\hat{E}/2$、$\hat{I}_k$、$\hat{S}_k$、$2\hat{I}_k\hat{S}_l$ 构成一对自旋的基。乘积算符（product-operator formalism）方法由 Sørensen、Ernst 及其合作者于 1983 年提出，它把 $\hat\rho$ 写在这个基中，并利用这样一个事实：每个相关的 Hamilton 量都在小的子空间内转动算符，如同矢量的转动。转动取正方向（NMR 教材的通常约定，对 $\gamma > 0$ 与定理 13.2.1 的方向相反，但只影响相位的符号）：

| Hamilton 量 | 时间 $t$ 内（或转角为 $\beta$ 的脉冲）的效果 |
|---|---|
| 绕 $x$ 的脉冲，$\omega_1\hat{I}_x$ | $\hat{I}_z \to \hat{I}_z\cos\beta - \hat{I}_y\sin\beta$；$\hat{I}_y \to \hat{I}_y\cos\beta + \hat{I}_z\sin\beta$ |
| 化学位移，$\Omega\hat{I}_z$ | $\hat{I}_x \to \hat{I}_x\cos\Omega t + \hat{I}_y\sin\Omega t$ |
| 标量耦合，$2\pi J\hat{I}_z\hat{S}_z$（弱耦合） | $\hat{I}_x \to \hat{I}_x\cos\pi Jt + 2\hat{I}_y\hat{S}_z\sin\pi Jt$；$\hat{I}_y \to \hat{I}_y\cos\pi Jt - 2\hat{I}_x\hat{S}_z\sin\pi Jt$ |

算符 $2\hat{I}_x\hat{S}_z$ 是反相磁化强度：其符号依赖于 $S$ 的状态的 $I$ 磁化强度，表现为一正一负两条线的二重峰。耦合使同相与反相磁化强度相互转换，对 $S$ 施加的脉冲则把 $2\hat{I}_z\hat{S}_z$ 型的序转化为另一自旋上的相干：磁化强度就是这样由一个核转移到另一个核的。

### 13.4.4. 二维谱与 HSQC

在**二维核磁共振**（[6.4.12](/6.4.12#def-12.5.2)）中，信号被记录为两个时间的函数：递增的演化期 $t_1$，其间磁化强度被一种核的频率标记；以及采集时间 $t_2$，其间在另一种核上检测。对两个时间做 Fourier 变换得到谱 $S(\omega_1, \omega_2)$，在每对发生了磁化强度转移的核的频率对处有一个交叉峰。

**例 13.4.1（用乘积算符分析 HSQC）** 在 $^1\mathrm{H}$–$^{15}\mathrm{N}$ 异核单量子相干（HSQC）实验中（13.2.5 的图，B 板），令 H 为酰胺质子，N 为其氮：

1. 对 H 施加 $90^\circ_x$ 脉冲：$\hat{H}_z \to -\hat{H}_y$。
2. INEPT（非灵敏核的极化转移增强）：延迟 $\tau = 1/(4J_{\mathrm{NH}}) = 2.7\,\mathrm{ms}$，对 H 与 N 同时施加 $180^\circ$ 脉冲，再延迟 $\tau$。$180^\circ$ 脉冲使 H 的化学位移重聚，而耦合演化 $2\tau = 1/(2J)$，$\sin(\pi J\cdot2\tau) = 1$：忽略符号，$-\hat{H}_y \to 2\hat{H}_x\hat{N}_z$。再对 H 施加 $90^\circ_y$、对 N 施加 $90^\circ_x$ 得到 $2\hat{H}_z\hat{N}_y$：相干此时以 $^{15}\mathrm{N}$ 的频率进动。
3. 演化 $t_1$，中间施加一个 H 的 $180^\circ$ 脉冲以使耦合重聚：$2\hat{H}_z\hat{N}_y \to 2\hat{H}_z\hat{N}_y\cos\Omega_{\mathrm{N}}t_1 - 2\hat{H}_z\hat{N}_x\sin\Omega_{\mathrm{N}}t_1$。
4. 反向 INEPT（同时施加 $90^\circ$ 脉冲并取相同的延迟）把余弦项转换回同相的质子磁化强度 $\hat{H}_x\cos\Omega_{\mathrm{N}}t_1$，在 $^{15}\mathrm{N}$ 去耦下于 $t_2$ 期间检测。正弦项在第二次扫描中通过改变相位选出，从而在 $t_1$ 中实现正交检测。

信号 $\cos(\Omega_{\mathrm{N}}t_1)\,\mathrm{e}^{\mathrm{i}\Omega_{\mathrm{H}}t_2}$ 对 $t_1$ 与 $t_2$ 变换后，每个 N–H 基团在 $(\Omega_{\mathrm{N}}, \Omega_{\mathrm{H}})$ 处给出一个峰：除脯氨酸外每个残基一个，另加 Asn 与 Gln 侧链的 $\mathrm{NH_2}$ 以及 Trp 的吲哚 NH。激发与检测都在质子上，相对直接观测 $^{15}\mathrm{N}$ 的增益就是 13.1.4 中的 300 倍。

$^1\mathrm{H}$–$^{15}\mathrm{N}$ HSQC 是蛋白质的“指纹”：对 $0.1\,\mathrm{mM}$ 的样品数分钟到一小时即可记录，其分散程度说明蛋白质是否折叠，峰的变化则报告结合、突变、pH、温度和构象变化。甲基区的 $^1\mathrm{H}$–$^{13}\mathrm{C}$ HSQC 对大蛋白起同样的作用。其他二维实验以不同的方式转移磁化强度：

| 实验 | 转移 | 交叉峰位于 | 用途 |
|---|---|---|---|
| COSY | $J$ 耦合，一步 | 相隔两或三个键的质子之间 | 小分子与肽的自旋体系 |
| TOCSY | $J$ 耦合，各向同性混合（自旋锁定） | 一个残基自旋体系的所有质子之间 | 识别残基类型 |
| NOESY | 经空间的交叉弛豫（NOE） | 相距小于约 $0.5\,\mathrm{nm}$ 的质子之间 | 序列归属、距离 |
| HSQC、HMQC | 单键异核 $J$ | 质子与其直接键合的 $^{15}\mathrm{N}$ 或 $^{13}\mathrm{C}$ 之间 | 指纹、滴定、弛豫 |

三维实验插入第二个递增的演化期与第二次转移；例如 NOESY-HSQC 把拥挤的 NOESY 谱沿接受 NOE 的质子所连的 $^{15}\mathrm{N}$ 或 $^{13}\mathrm{C}$ 频率展开。在两三个间接维度上对网格采样很慢，每张谱需要数天；非均匀采样只记录网格的一个随机子集，并用稀疏恢复的方法重建谱，使测量时间缩短数倍。

### 13.4.5. 共振归属

在任何解释之前，必须把每个信号归属到它的原子。对于肽和小的未标记蛋白质，Wüthrich 的策略只用质子谱。TOCSY（或 COSY）识别每个残基的自旋体系，其位移模式指示残基类型（Gly 有两个 $\mathrm{H}^\alpha$；Ala 有与 $\mathrm{H}^\alpha$ 耦合的甲基；Glu 与 Gln 只能由其较长侧链的 TOCSY 模式区分），而 NOESY 则利用 $\mathrm{H}^\alpha(i)$ 与 $\mathrm{H}^{\mathrm{N}}(i + 1)$ 之间的短距离把每个残基与序列中的邻居联系起来，无论构象如何 $d_{\alpha N}(i, i+1) \le 0.36\,\mathrm{nm}$。把自旋体系类型的链与已知序列匹配，即可确定归属。

**例 13.4.2（含 RGD 基序的七肽）** 序列 Arg–Gly–Asp 被**整联蛋白**识别，把 Asp 换成 Glu（RGE）则使结合消失。在对七肽 YGRGDSP 与 YGRGESP 的研究中，COSY 识别了七个残基的自旋体系，NOESY 通过 $d_{\alpha N}(i, i+1)$ 的连接把它们沿链排序，而相隔两个残基的残基之间的额外 NOE 模式表明，RGD 肽形成 II 型 $\beta$ 转角，RGE 肽则形成 I 型或 III 型转角：这一局部构象的差异与活性的丧失相关。

对于大于约 $10\,\mathrm{kDa}$ 的蛋白质，质子谱过于拥挤，归属要在 $^{13}\mathrm{C}/^{15}\mathrm{N}$ 标记的样品上使用三共振实验，通过 13.4.2 的单键耦合沿主链转移磁化强度。HNCACB（或 CBCANH）实验把残基 $i$ 的 $\mathrm{H}^{\mathrm{N}}$ 与 N 同残基 $i$（通过 $^1J_{\mathrm{NC}^\alpha}$）和残基 $i - 1$（通过 $^2J_{\mathrm{NC}^\alpha}$）两者的 $\mathrm{C}^\alpha$ 与 $\mathrm{C}^\beta$ 相关联；经羰基转移的 CBCA(CO)NH（或 HN(CO)CACB）实验则只显示残基 $i - 1$ 的。对每个酰胺，三维谱在其 $(\mathrm{H}^{\mathrm{N}}, \mathrm{N})$ 位置的“条带”显示两对 $\mathrm{C}^\alpha/\mathrm{C}^\beta$ 峰，把一个条带的“前一残基”对与另一个条带的“本残基”对匹配，就把各条带连接起来：这是一次序列行走。$\mathrm{C}^\alpha$ 与 $\mathrm{C}^\beta$ 的位移识别残基类型（Gly 没有 $\mathrm{C}^\beta$，$\mathrm{C}^\alpha \approx 45\,\mathrm{ppm}$；Ala 的 $\mathrm{C}^\beta \approx 19\,\mathrm{ppm}$；Ser 与 Thr 的 $\mathrm{C}^\beta$ 高于 $60\,\mathrm{ppm}$），这使行走锚定到序列上。灵敏度低时，改用更灵敏的 HNCA/HN(CO)CA 与 HNCO/HN(CA)CO 对。侧链随后用 HCCH-TOCSY 与 NOESY 类谱归属。核酸在经磷酸的主链上缺少强耦合的通路，仍主要通过 NOESY 归属，从碱基对的亚氨基质子开始。

### 13.4.6. 化学位移扰动与滴定

**定义 13.4.2（化学位移扰动）** 化学位移扰动（CSP）是加入结合配体后大分子化学位移的变化。在 $^1\mathrm{H}$–$^{15}\mathrm{N}$ HSQC 滴定中，它按残基以组合变化 $\Delta\delta = \sqrt{\Delta\delta_{\mathrm{H}}^2 + (\alpha\Delta\delta_{\mathrm{N}})^2}$ 概括，其中 $\alpha \approx 0.14$–$0.2$ 用来补偿 $^{15}\mathrm{N}$ 位移范围较大的因素。

把 $\Delta\delta$ 大的残基映射到结构上，就勾画出**结合部位**；对于**衔接蛋白** Crk 的 SH3 结构域与来自 Sos 的肽，这一图谱与后来在复合物晶体结构中看到的界面一致。用 [7.6.3](/7.6.3) 的结合等温线拟合峰的位移对配体浓度的依赖关系，得到解离常数，NMR 能很好地测量约 $1\,\mu\mathrm{M}$ 到 $10\,\mathrm{mM}$ 的范围，其中包括大多数其他方法测不到的**非共价相互作用**；峰如何移动取决于自由态与结合态之间的交换速率（13.6.2）。在基于片段的药物发现中，用 HSQC 谱或配体观测的实验（饱和转移差谱、WaterLOGSY）筛选弱结合小分子库。对 pH 的滴定同样如此：沿着质子化平衡跟踪组氨酸 $\mathrm{C}^{\varepsilon1}$–H 或 Asp 与 Glu 羧基 $^{13}\mathrm{C}$ 的位移，可以得到各个基团的 $\mathrm{p}K_{\mathrm{a}}$，这些值在折叠蛋白中常与其在肽中的值相差数个单位（[7.6.6](/7.6.6)）。CSP 显示的是何处发生了变化，这既可能是接触面本身，也可能是远离接触面的别构位点。

## 13.5. 结构测定

### 13.5.1. 核 Overhauser 效应

**核 Overhauser 效应**（NOE，[6.4.12](/6.4.12#def-12.5.1)）是通过交叉弛豫在自旋之间转移布居差的现象，交叉弛豫即两个自旋由涨落的偶极耦合驱动的相互翻转。对于两个质子 $I$ 与 $S$，纵向磁化强度服从 Solomon 方程

$$
\frac{\mathrm{d}I_z}{\mathrm{d}t} = -\rho_I(I_z - I_z^0) - \sigma(S_z - S_z^0), \qquad \frac{\mathrm{d}S_z}{\mathrm{d}t} = -\sigma(I_z - I_z^0) - \rho_S(S_z - S_z^0), \tag{13.19}
$$
其中 $\rho$ 为自弛豫速率，$\sigma$ 为交叉弛豫速率。

**公式 13.5.1（交叉弛豫速率）** 对于各向同性翻滚的分子中相距 $r$ 的两个质子，$K$ 与 $j(\omega)$ 同定理 13.3.1，则

$$
\sigma = \frac{K^2}{10}\left[6j(2\omega_0) - j(0)\right] \propto \frac{1}{r^6}\,f(\tau_{\mathrm{c}}), \qquad \rho = \frac{K^2}{10}\left[j(0) + 3j(\omega_0) + 6j(2\omega_0)\right]. \tag{13.20}
$$
$\sigma$ 在快翻滚时为正，慢翻滚时为负，并在 $\omega_0\tau_{\mathrm{c}} = \sqrt{5}/2 = 1.12$ 处变号。

两项对应两种翻转过程：频率 $2\omega_0$ 处的双量子跃迁 $\alpha\alpha \leftrightarrow \beta\beta$，以及零频处的零量子相互翻转 $\alpha\beta \leftrightarrow \beta\alpha$。小分子（$\omega_0\tau_{\mathrm{c}} \ll 1$）在稳态下显示最多 $50\,\%$ 的正 NOE；大分子则深处于慢运动区（在 $600\,\mathrm{MHz}$ 下，$25\,\mathrm{kDa}$ 的蛋白质 $\omega_0\tau_{\mathrm{c}} \approx 50$），$\sigma \approx -K^2\tau_{\mathrm{c}}/10$ 绝对值很大且为负；$1$–$2\,\mathrm{kDa}$、接近变号点的分子可能完全没有 NOE，需用旋转坐标系中的变体 ROESY 测量。

在 NOESY 实验中，$t_1$ 期间被 $I$ 的频率标记的横向磁化强度被转回 $z$ 轴，在混合时间 $\tau_{\mathrm{m}}$ 内发生交叉弛豫，然后在 $S$ 上读出。混合时间较短时，交叉峰强度线性增长，$a_{IS} \propto \sigma\tau_{\mathrm{m}} \propto r^{-6}$（初速率近似），通过与已知距离的一对核校准即可得到距离：

$$
r_{IS} = r_{\mathrm{ref}}\left(\frac{a_{\mathrm{ref}}}{a_{IS}}\right)^{1/6}. \tag{13.21}
$$
六次方根很宽容：强度有两倍的误差，距离只有 12 % 的误差。其另一面是，NOE 在约 $0.5$–$0.6\,\mathrm{nm}$ 之外就无法检测，所以 NMR 结构是由许多短程接触构建的。混合时间较长时，磁化强度继续传到第三个自旋，$I \to K \to S$：这种自旋扩散（spin diffusion）使远处的质子看起来很近，对大的、未氘代的分子最为严重；可以用较短的混合时间、氘代或完整的弛豫矩阵分析加以限制。由于核间矢量在涨落，平均值为 $\langle r^{-6}\rangle^{-1/6}$，由所访问的最短距离主导，而内部运动也调制 $\sigma$，NOE 距离的使用是保守的，按类别取作上界（例如强 $\le 0.27\,\mathrm{nm}$，中 $\le 0.33\,\mathrm{nm}$，弱 $\le 0.5\,\mathrm{nm}$），而不是精确值。

### 13.5.2. NOE 模式与其他局部约束

短的质子–质子距离的模式在任何计算之前就能识别二级结构（下图）：$\alpha$ 螺旋使 $\mathrm{H}^{\mathrm{N}}(i)$ 与 $\mathrm{H}^{\mathrm{N}}(i + 1)$ 靠近（$0.28\,\mathrm{nm}$），并使 $\mathrm{H}^\alpha(i)$ 靠近 $\mathrm{H}^{\mathrm{N}}(i + 3)$ 与 $\mathrm{H}^\beta(i + 3)$；$\beta$ 链的 $d_{\alpha N}(i, i + 1)$ 很短（$0.22\,\mathrm{nm}$），在反平行片层中，不形成氢键的跨链对的 $\mathrm{H}^\alpha$ 质子（$0.23\,\mathrm{nm}$）与形成氢键的对的酰胺质子（$0.33\,\mathrm{nm}$）彼此相对。序列上相距很远的残基之间的长程 NOE 决定折叠。与此同时还有：

- 来自 $^3J$ 耦合（公式 13.4.1）与主链化学位移（13.4.1）的二面角约束；
- 氢键约束，来自免于与溶剂交换的酰胺（13.6.5），或直接测得的跨氢键耦合；
- 以下两小节的约束，它们不是局部的。

![由标准键长键角构建的理想二级结构的主链坐标算出的、短于 0.5 nm（NOE 范围）的质子–质子距离（每个残基取酰胺、α 与一个 β 质子）。每个符号标出残基 i 与 j 之间已分类的最短距离，其大小与颜色表示距离：方块为 d_NN（Hᴺ–Hᴺ），圆为 d_αN（Hᵅ–Hᴺ），菱形为 d_αα（Hᵅ–Hᵅ）。A：α 螺旋（φ = −57°，ψ = −47°）：强的 d_NN(i, i+1) 与 d_αN(i, i+3)，较弱的 d_αN(i, i+2) 与 (i, i+4)。B：双链反平行 β 片层（φ = −139°，ψ = 135°），第二条链在一个未建模的转角之后编号为 9–15：很短的序列相邻 d_αN(i, i+1)，反对角线上是不形成氢键的对（1–15、3–13、5–11、7–9）的跨链 d_αα 与形成氢键的对（2–14、4–12、6–10）的 d_NN](./plots/noe-map.py)

### 13.5.3. 残余偶极耦合

两个成键核之间的直接偶极耦合非常大（对 N–H，最大为 $23\,\mathrm{kHz}$），携带着键的取向信息，但在各向同性溶液中它精确地平均为零。Tolman 与 Prestegard（1995）以及 Tjandra 与 Bax（1997）的技巧是使溶液产生极微弱的各向异性。

**定义 13.5.1（残余偶极耦合）** 当大分子相对磁场发生弱取向时，固定距离 $r$ 处两个核 $I$ 与 $S$ 之间的偶极耦合不再平均为零；剩余的平均值

$$
D_{IS} = -\frac{\mu_0\gamma_I\gamma_S\hbar}{8\pi^2r^3}\left\langle3\cos^2\theta - 1\right\rangle , \tag{13.22}
$$
以赫兹计，其中 $\theta$ 为核间矢量与 $\boldsymbol{B}_0$ 的夹角，括号表示对分子取向与内部运动的平均，称为残余偶极耦合（RDC）。它与标量耦合相加，所以在取向样品中测得的裂分为 $J + D$，$D$ 由其与各向同性样品的差得到。

对刚性分子，平均值通过整个分子的取向张量表示：在其主轴系中，对极角为 $(\theta, \phi)$ 的键，

$$
D(\theta, \phi) = D_{\mathrm{a}}\left[(3\cos^2\theta - 1) + \tfrac32R\sin^2\theta\cos2\phi\right], \tag{13.23}
$$
其中大小 $D_{\mathrm{a}}$ 与菱形度 $R$ 同主轴系的取向一起拟合。式 (13.22) 的前置因子对 N–H（$r = 0.102\,\mathrm{nm}$；因 $\gamma_{\mathrm{N}} < 0$ 而为正）为 $+11.5\,\mathrm{kHz}$，对 $\mathrm{C}^\alpha$–$\mathrm{H}^\alpha$（$0.109\,\mathrm{nm}$）为 $-23.4\,\mathrm{kHz}$。$10^{-3}$ 量级的取向度把它们缩小到 $\pm10$–$30\,\mathrm{Hz}$，既小到能保持谱图简单，又大到能以 $\pm1\,\mathrm{Hz}$ 的精度测量。取向由不与蛋白质结合的稀释液晶产生：DMPC 与 DHPC 的双层胶束、丝状 Pf1 噬菌体（$10$–$20\,\mathrm{mg\,mL^{-1}}$）、烷基–聚乙二醇/己醇相，或拉伸和压缩的聚丙烯酰胺凝胶；磁各向异性大的核酸也能自身发生弱取向。

RDC 报告的是键相对于整个分子共同坐标系的取向，而不是到邻居的距离：它是全局约束。因此它可以确定没有 NOE 接触的两个结构域之间的相对取向，检验晶体结构与溶液状态是否相符（拟合的品质因子 $Q$），把结构精修到超出 NOE 的精度，并且在多种介质中测量，或对有内部运动的残基测量，可以刻画比 $\tau_{\mathrm{c}}$ 慢、至毫秒的运动的幅度与方向。其弱点是简并：$3\cos^2\theta - 1$ 不能区分 $\theta$ 与 $180^\circ - \theta$，一组 RDC 在绕取向张量主轴转 $180^\circ$ 时不变。RDC 也不受自旋扩散的影响，这使它们对大蛋白很有价值，并且与**小角 X 射线散射**（[7.6.9](/7.6.9#sec-9.12)）结合，可以确定 RNA 的整体结构。

**注 13.5.1（符号）** 不带 $\gamma$ 而写成 $D \propto 1 - 3\cos^2\theta$ 的公式，假定两个旋磁比均为正，如 C–H：平行于取向主轴的 C–H 键于是 $D < 0$。对 N–H，乘积 $\gamma_{\mathrm{H}}\gamma_{\mathrm{N}}$ 为负，符号相反，沿轴的键 $D > 0$；单键标量耦合 $^1J_{\mathrm{NH}} \approx -92\,\mathrm{Hz}$ 也因同样的原因为负。许多论文报告的 $^1D_{\mathrm{NH}}$ 乘了 $-1$，或把所有耦合都归一化到 N–H 的情形；合并不同来源的 RDC 时必须核对所用的约定。

![几何约束。A：Karplus 关系 ³J(Hᴺ, Hᵅ) = 6.51 cos²θ − 1.76 cos θ + 1.60 Hz，θ = φ − 60°（Vuister 与 Bax）；α 螺旋（φ = −57°）约给出 4 Hz，β 片层（φ = −139°）约 9 Hz，多数残基位于阴影所示的 φ < 0 半区。B：N–H 键的残余偶极耦合随键与取向轴夹角 θ 的变化，D = Dₐ(3cos²θ − 1)，Dₐ = 10 Hz：沿轴为正，因为 γ_N < 0，在魔角 54.7° 处为零。C：NMR 与 EPR 约束的近似距离范围及其距离律，并以 FRET 作比较](./plots/restraints.py)

### 13.5.4. 顺磁约束

附着在分子上的顺磁中心把 NMR 的作用范围扩展到远超 $0.5\,\mathrm{nm}$，因为电子的磁矩是质子的 658 倍。

**定义 13.5.2（顺磁弛豫增强）** 顺磁弛豫增强（PRE）是未成对电子的涨落偶极场使核的弛豫速率增大的现象。对距质子 $r$ 处的电子自旋 $S$，横向增强为（Solomon–Bloembergen）

$$
\Gamma_2 = \frac{1}{15}\left(\frac{\mu_0}{4\pi}\right)^2\gamma_{\mathrm{H}}^2g^2\mu_{\mathrm{B}}^2S(S + 1)\,\frac{1}{r^6}\left[4\tau_{\mathrm{c}} + \frac{3\tau_{\mathrm{c}}}{1 + \omega_{\mathrm{H}}^2\tau_{\mathrm{c}}^2}\right], \tag{13.24}
$$
其中 $\tau_{\mathrm{c}}$ 是电子–核矢量的相关时间（包括电子弛豫）。

PRE 与 NOE 一样依赖于 $r^{-6}$，但前置因子约大 $4\times10^5$ 倍，所以硝酰基自旋标记，如 MTSL（甲硫基磺酸盐自旋标记，连接在通过突变在选定位点引入的半胱氨酸上），可使 $1.5$–$3\,\mathrm{nm}$ 范围内的信号变宽。测量方法是比较标记处于顺磁形式时的峰强度与用抗坏血酸还原为抗磁的羟胺之后的峰强度之比。由于 $r^{-6}$ 加权，使标记接近某个残基的少数构象即便只占百分之几的布居，也会主导 PRE；因此 PRE 是研究瞬态相遇复合物、**内在无序蛋白**的紧缩状态和分子间接触（标记在一个配体上，被观测的核在另一个上）的首选方法，而用可溶性顺磁试剂做的溶剂 PRE 则可绘出可及表面。

具有各向异性磁化率的镧系离子（结合在标签上的 Tb³⁺、Dy³⁺、Tm³⁺、Yb³⁺）则改为使附近核的信号发生位移。

**定义 13.5.3（赝接触位移）** 赝接触位移（PCS）是距离 $r$ 处顺磁中心的各向异性磁化率 $\Delta\chi$ 所引起的核化学位移的变化：

$$
\Delta\delta^{\mathrm{PCS}} = \frac{1}{12\pi r^3}\left[\Delta\chi_{\mathrm{ax}}(3\cos^2\theta - 1) + \tfrac32\Delta\chi_{\mathrm{rh}}\sin^2\theta\cos2\phi\right], \tag{13.25}
$$
其中 $(r, \theta, \phi)$ 是核在磁化率张量主轴系中的位置。它以顺磁样品与抗磁（La³⁺、Lu³⁺、Y³⁺）样品的位移之差测量。

PCS 只按 $r^{-3}$ 衰减，可达 $4$–$6\,\mathrm{nm}$，并同时给出距离与角度信息；同一张量还使分子在磁场中取向，从而产生 RDC。PCS 与 PRE 对结构域的对接和配体的定位特别有用。

### 13.5.5. 结构计算

NMR 结构的约束是成百上千个对距离与角度的界限，每个都不精确，结构就是同时满足它们和已知共价几何的构象集合。

**算法 13.5.1（受约束驱动的模拟退火）**

1. 用标准共价几何与简化的力场（键、键角、平面性、手性、纯排斥的 van der Waals 项）表示分子。
2. 定义目标函数 $E = E_{\operatorname{Cov}} + E_{\mathrm{rep}} + w_{\mathrm{NOE}}\sum\max(0, r_{ij} - u_{ij})^2 + w_\phi\sum\Delta\phi^2 + w_D\sum(D^{\mathrm{calc}} - D^{\mathrm{obs}})^2 + \cdots$，即对每个被违反的约束施加平底惩罚。
3. 从随机或伸展的构象出发，在高温下用软排斥进行**分子动力学**（在 Cartesian 坐标或扭转角坐标中），使链可以相互穿过，并缓慢冷却，同时提高约束与排斥的权重：**模拟退火**（[7.6.9](/7.6.9#alg-9.11.1)）。
4. 从 50–200 个起始构象重复；保留能量最低的 10–20 个，用更完整的、带显式或隐式溶剂的力场对它们精修。
5. 验证：约束违反情况、Ramachandran 统计、堆积，以及与未用于计算的数据（交叉验证的 RDC、化学位移）的吻合程度。

输出是结构的系综，其离散度（用坐标相对其平均值的均方根偏差（RMSD）度量）有两种含义，不借助进一步的数据无法分开：约束的缺乏（NOE 很少的环与末端）与真实的运动。良好结构中明确定义的区域，主链 RMSD 为 $0.03$–$0.06\,\mathrm{nm}$。程序有：CYANA（扭转角动力学，带自动 NOE 归属）、Xplor-NIH 与 CNS、ARIA；最终精修则在 Amber、CHARMM 或 GROMACS 的力场中进行。整个过程的瓶颈，即把数千个 NOESY 交叉峰归属到质子对，由迭代的软件完成，它利用每个初步结构消除歧义。仅用化学位移，结合 Rosetta 的**片段组装**（CS-Rosetta）以及少量 NOE 或 RDC，即可测定至多约 $40\,\mathrm{kDa}$ 的蛋白质结构；自 2021 年以来，预测结构（[7.6.15](/7.6.15)）日益被用作起始模型，由 NMR 数据加以确认、修正或精修，而 NMR 的贡献则在预测最薄弱之处，即动力学与替代状态。

## 13.6. 动态

### 13.6.1. 时间尺度

NMR 的独特优势在于，它能以原子分辨率测量跨越约十七个数量级时间的运动，每个窗口有各自的实验（下图）。自旋弛豫（13.3，13.6.3）报告比整体翻滚更快的运动，从皮秒到纳秒。RDC 对直到毫秒的一切运动取平均。化学交换通过线形、弛豫色散、CEST 和交换谱覆盖微秒到秒，即催化、别构、小结构域折叠和结合的时间尺度（13.6.2，13.6.4）。氢交换报告从毫秒到数月的开启事件（13.6.5），而实时 NMR 则直接追踪缓慢的折叠与反应。蛋白质是动态而非刚性的这一观念，在 1970 年代同时从两个方向兴起：第一个蛋白质（BPTI）的分子动力学模拟（真空中 9.2 ps；McCammon、Gelin 与 Karplus，1977），以及 NMR 对 BPTI 中埋藏芳香残基环翻转的观测，这种翻转要求核心发生瞬时的膨胀。

![生物分子运动的时间尺度（灰色，上部各行）及报告它们的磁共振方法（彩色，下部各行）；范围为近似值。DEER 测量冷冻样品中的距离分布，是系综的快照而非速率](./plots/timescales.py)

### 13.6.2. 化学交换

**定义 13.6.1（化学交换）** 在 NMR 中，化学交换是核通过构象变化、化学反应或结合，在具有不同共振频率的环境之间的相互转化。对于速率常数为 $k_{\mathrm{AB}}$、$k_{\mathrm{BA}}$ 的两位点 $\mathrm{A} \rightleftharpoons \mathrm{B}$，交换速率为 $k_{\mathrm{ex}} = k_{\mathrm{AB}} + k_{\mathrm{BA}}$，布居为 $p_{\mathrm{A}} = k_{\mathrm{BA}}/k_{\mathrm{ex}}$，$p_{\mathrm{B}} = k_{\mathrm{AB}}/k_{\mathrm{ex}}$。设 $\Delta\omega$ 为两个频率之差，则 $k_{\mathrm{ex}} \ll \lvert\Delta\omega\rvert$ 时交换为慢，$k_{\mathrm{ex}} \approx \lvert\Delta\omega\rvert$ 时为中等，$k_{\mathrm{ex}} \gg \lvert\Delta\omega\rvert$ 时为快。

McConnell（1958）把 Bloch 方程与一级动力学结合起来。

**公式 13.6.1（Bloch–McConnell 方程）** 两个位点的横向磁化强度 $m_{\mathrm{A}}$、$m_{\mathrm{B}}$（复数，$M_x + \mathrm{i}M_y$）满足

$$
\frac{\mathrm{d}}{\mathrm{d}t}\begin{bmatrix}m_{\mathrm{A}}\\ m_{\mathrm{B}}\end{bmatrix} = \begin{bmatrix}\mathrm{i}\Omega_{\mathrm{A}} - R_2 - k_{\mathrm{AB}} & k_{\mathrm{BA}}\\ k_{\mathrm{AB}} & \mathrm{i}\Omega_{\mathrm{B}} - R_2 - k_{\mathrm{BA}}\end{bmatrix}\begin{bmatrix}m_{\mathrm{A}}\\ m_{\mathrm{B}}\end{bmatrix} = L\begin{bmatrix}m_{\mathrm{A}}\\ m_{\mathrm{B}}\end{bmatrix}, \tag{13.26}
$$
因此 FID 为 $s(t) = \boldsymbol{1}^{\mathsf T}\mathrm{e}^{Lt}\boldsymbol{p}$，其中 $\boldsymbol{p} = (p_{\mathrm{A}}, p_{\mathrm{B}})^{\mathsf T}$，谱为 $\operatorname{Re}\boldsymbol{1}^{\mathsf T}(\mathrm{i}\omega I - L)^{-1}\boldsymbol{p}$。

$L$ 的本征值给出所观测谱线的位置与宽度，三种区域由此而来（下图）。慢交换时，在 $\Omega_{\mathrm{A}}$ 与 $\Omega_{\mathrm{B}}$ 处有两条强度分别为 $p_{\mathrm{A}}$ 与 $p_{\mathrm{B}}$ 的谱线，每条都因离开其位点的速率而增宽（$k_{\mathrm{AB}}$ 或 $k_{\mathrm{BA}}$ 加到 $R_2$ 上）。随着 $k_{\mathrm{ex}}$ 增大，谱线变宽、相互靠拢，布居相等时在聚并处合并，$k_{\mathrm{ex}} = \lvert\Delta\omega\rvert/\sqrt2 = \sqrt2\,\pi\lvert\Delta\nu\rvert$。快交换时，在布居加权平均 $p_{\mathrm{A}}\Omega_{\mathrm{A}} + p_{\mathrm{B}}\Omega_{\mathrm{B}}$ 处出现单条谱线，其宽度中的交换贡献为

$$
R_{\mathrm{ex}} = \frac{p_{\mathrm{A}}p_{\mathrm{B}}\Delta\omega^2}{k_{\mathrm{ex}}}, \tag{13.27}
$$
它随交换变快而减小：这是 13.3 的运动窄化的另一种形式。随温度变化的线形会经过这些区域，由此得到 $k_{\mathrm{ex}}$ 及其活化能；经典的例子是酰胺部分双键的旋转，或蛋白质核心中 Phe 与 Tyr 的环翻转。

**例 13.6.1（结合滴定与交换）** 对于蛋白质 P 与过量配体 L 的结合，$\mathrm{P} + \mathrm{L} \rightleftharpoons \mathrm{PL}$，赝一级速率为 $k_{\mathrm{AB}} = k_{\mathrm{on}}[\mathrm{L}]$ 与 $k_{\mathrm{BA}} = k_{\mathrm{off}}$，所以 $k_{\mathrm{ex}} = k_{\mathrm{on}}[\mathrm{L}] + k_{\mathrm{off}}$；在滴定的中点 $[\mathrm{L}] = K_{\mathrm{d}}$，$k_{\mathrm{ex}} = 2k_{\mathrm{off}} = 2k_{\mathrm{on}}K_{\mathrm{d}}$。结合速率接近扩散控制的范围（$k_{\mathrm{on}} \approx 10^7$–$10^8\,\mathrm{M^{-1}\,s^{-1}}$，[7.6.5](/7.6.5#sec-5.2.3)），所以区域基本上由亲和力决定。对位移为 $\Delta\nu = 100\,\mathrm{Hz}$（$\lvert\Delta\omega\rvert = 630\,\mathrm{s^{-1}}$）且 $k_{\mathrm{on}} = 10^8\,\mathrm{M^{-1}\,s^{-1}}$ 的峰：$K_{\mathrm{d}} = 100\,\mu\mathrm{M}$ 的配体给出 $k_{\mathrm{ex}} = 2\times10^4\,\mathrm{s^{-1}}$，为快交换，峰从自由位置平滑地移到结合位置；$K_{\mathrm{d}} = 1\,\mu\mathrm{M}$ 给出 $200\,\mathrm{s^{-1}}$，为慢交换，自由峰逐渐消失，而结合峰在原位增长；介于二者之间时，峰变宽，并可能在中点附近消失。因此弱结合者通过跟踪位移来滴定，紧结合者则通过跟踪强度来滴定。

**例 13.6.2（视为交换的催化）** 亲环蛋白催化脯氨酰肽键的顺反异构化，这是许多蛋白质折叠中的慢步骤（无催化时需数分钟）。模型底物琥珀酰-Ala-Ala-Pro-Phe-对硝基苯胺的顺式与反式给出分开的信号，它们相互转化得太慢，不影响谱图。加入催化量的亲环蛋白使互变加速到中等区域，信号变宽；加入阻断活性位点的抑制剂环孢素 A，则尖锐的谱线得以恢复。这类线形无需改变任何浓度，就能测量处于平衡的酶的周转。

![由 Bloch–McConnell 方程得到的两位点化学交换（本征 R₂ = 10 s⁻¹）。A：布居相等、Δν = 200 Hz 时，k_ex 增大时的谱：从慢交换（两条线），经聚并（k_ex = √2 πΔν = 888 s⁻¹），到快交换（平均位置处一条线）。B：结合态布居由 0 升到 1 的滴定在慢、中、快三种区域的表现：慢交换时一个峰消失而另一个增长，快交换时一个峰移动，中等交换时峰变宽到几乎无法检测。C：5 % 次要态、Δν = 150 Hz 的 CPMG 弛豫色散：当重聚脉冲频繁到足以跑赢交换时，有效 R₂ 由 R₂⁰ + R_ex 降向 R₂⁰；曲线的形状取决于 k_ex](./plots/exchange.py)

### 13.6.3. 无模型分析与序参量

$^{15}\mathrm{N}$ 的弛豫速率（公式 13.3.1）取决于每个 N–H 键的运动，这种运动由整个分子的翻滚及分子内的内部运动组成。若二者相互独立，且内部运动比翻滚快，则关联函数可以分解，$C(t) = C_{\mathrm{O}}(t)C_{\mathrm{I}}(t)$，各向同性翻滚时 $C_{\mathrm{O}} = \mathrm{e}^{-t/\tau_{\mathrm{m}}}$。内部关联函数会衰减，但不会衰减到零，因为连在折叠蛋白上的键不能到达所有取向；它最终趋于一个平台值。

**定义 13.6.2（广义序参量）** 键矢量的广义序参量 $S^2$ 是其内部关联函数的平台值，$S^2 = \lim_{t\to\infty}C_{\mathrm{I}}(t) = \frac{4\pi}{5}\sum_{m=-2}^{2}\lvert\langle Y_2^m(\boldsymbol{u})\rangle\rvert^2$，其中 $Y_2^m$ 为二阶**球面调和函数**，平均对内部运动取。其范围从 $1$（刚性固定在分子坐标系中的键）到 $0$（取向被内部运动完全随机化的键）。

**定义 13.6.3（无模型分析）** 无模型分析（Lipari 与 Szabo，1982）用内部关联函数 $C_{\mathrm{I}}(t) = S^2 + (1 - S^2)\mathrm{e}^{-t/\tau_{\mathrm{e}}}$ 解释弛豫速率，每个键用两个参数刻画：序参量 $S^2$（幅度）与有效内部相关时间 $\tau_{\mathrm{e}}$（快慢），而不假设运动的任何物理模型。谱密度成为

$$
J(\omega) = \frac25\left[\frac{S^2\tau_{\mathrm{m}}}{1 + \omega^2\tau_{\mathrm{m}}^2} + \frac{(1 - S^2)\tau}{1 + \omega^2\tau^2}\right], \qquad \frac1\tau = \frac{1}{\tau_{\mathrm{m}}} + \frac{1}{\tau_{\mathrm{e}}}. \tag{13.28}
$$

对 $n$ 个残基测得 $R_1$、$R_2$ 与 NOE（最好在两个磁场下），有 $3n$ 个数据对应 $2n + 1$ 个参数（每个残基的 $S^2$ 与 $\tau_{\mathrm{e}}$，加上 $\tau_{\mathrm{m}}$；各向异性翻滚时再多四个），通过**最小二乘法**拟合并做模型选择（必要时加入 $R_{\mathrm{ex}}$ 或第二个较慢的内部运动），得到沿序列的 $S^2$ 分布图。这些参数有简单的含义：对在半角为 $\theta_0$ 的圆锥内均匀摆动的键，$S^2 = [\frac12\cos\theta_0(1 + \cos\theta_0)]^2$，所以螺旋与片层中主链酰胺的典型值 $S^2 = 0.85$ 对应于 $\theta_0 \approx 19^\circ$，低于 $0.6$ 的值标志着柔性的环与末端。这一分析也可以反过来从分子动力学轨迹进行：把所有帧叠合到第一帧上消除翻滚，每个 N–H 矢量的 $P_2$ 关联函数直接给出 $C_{\mathrm{I}}(t)$，比较计算与实测的 $S^2$ 即可检验力场。

由于 $S^2$ 度量键取向分布的宽度，它与残基的**构象熵**相关。Wand、Kay 及其合作者对**钙调蛋白**和其他蛋白质测得的结合时侧链甲基序参量的变化表明，构象**熵**对结合自由能的贡献与量热法测得的相当（[7.6.8](/7.6.8)），并且配体可以通过改变涨落而不是平均结构来耦合远处的位点，这是别构的一种形式（[7.6.4](/7.6.4)）。当内部运动与整体运动不可分离时，这一分析失效，不应使用：对内在无序蛋白，宜采用谱密度映射（直接由速率估计 $J(0)$、$J(\omega_{\mathrm{N}})$ 与 $J(0.87\omega_{\mathrm{H}})$）或与模拟比较；对结构域在翻滚的时间尺度上重新取向的柔性多结构域蛋白也是如此。

### 13.6.4. 弛豫色散、CEST 与 ZZ 交换

处于平衡的蛋白质常有百分之几的时间处在较高能量的构象中：底物结合态、折叠中间体、别构转变路径上的某个状态。这些激发态在谱图中不可见，因为它们的峰很弱且变宽，但它们与基态的交换会在基态信号上留下痕迹。

**定义 13.6.4（弛豫色散）** 弛豫色散是有效横向弛豫速率对重聚速率的依赖关系：在 CPMG 实验中依赖于 $180^\circ$ 脉冲的间隔 $\tau_{\mathrm{cp}}$（表示为 $\nu_{\mathrm{CPMG}} = 1/(2\tau_{\mathrm{cp}})$），在 $R_{1\rho}$ 实验中依赖于连续自旋锁定场的强度。它源于微秒到毫秒时间尺度上的交换：如果脉冲在核于两个位点之间跳跃之前使磁化强度重聚，则跳跃造成的退相位被抑制。

在低 $\nu_{\mathrm{CPMG}}$ 下有效速率为 $R_2^0 + R_{\mathrm{ex}}$；在高 $\nu_{\mathrm{CPMG}}$ 下交换贡献被淬灭，$R_{2,\mathrm{eff}} \to R_2^0$。对快交换，曲线具有 Luz–Meiboom 形式

$$
R_{2,\mathrm{eff}}(\nu_{\mathrm{CPMG}}) = R_2^0 + \frac{p_{\mathrm{A}}p_{\mathrm{B}}\Delta\omega^2}{k_{\mathrm{ex}}}\left[1 - \frac{4\nu_{\mathrm{CPMG}}}{k_{\mathrm{ex}}}\tanh\frac{k_{\mathrm{ex}}}{4\nu_{\mathrm{CPMG}}}\right], \tag{13.29}
$$
而对一般的交换则由 Bloch–McConnell 方程精确计算（Carver–Richards 公式，或如 13.6.2 图的 C 板那样做数值传播）。在两个磁场下拟合许多残基的色散曲线，得到 $k_{\mathrm{ex}}$、激发态的布居 $p_{\mathrm{B}}$，以及每个核的 $\lvert\Delta\omega\rvert$，即不可见态相对基态的化学位移。由于化学位移编码了结构（13.4.1），激发态的位移已被用来测定它们的结构，例如折叠中间体以及碱基对错位的 RNA 次要构象。把弛豫色散用于**二氢叶酸还原酶**和亲环蛋白，表明即使没有配体，酶也以与周转相当的速率采样类似其催化循环下一状态的构象（Eisenmesser、Kern 及其合作者，2002–2005；Boehr、Wright 及其合作者，2006）。CPMG 覆盖约 $50$–$5000\,\mathrm{s^{-1}}$ 的 $k_{\mathrm{ex}}$，$R_{1\rho}$ 可达约 $10^5\,\mathrm{s^{-1}}$；CPMG 中丢失的 $\Delta\omega$ 的符号可通过比较两个磁场下的位移或由 $R_{1\rho}$ 得到。

对于较慢的交换（$k_{\mathrm{ex}} \approx 20$–$300\,\mathrm{s^{-1}}$），化学交换饱和转移（chemical exchange saturation transfer）简称 CEST，在一系列偏置下施加几百毫秒的弱射频场：当它恰好落在不可见态的频率上时，饱和通过交换传给基态，基态峰的强度下降，因此强度对偏置作图，在不可见峰的位置出现一个凹陷。对于更慢的交换（数百毫秒到数秒）且两个状态都可见的情形，ZZ 交换谱让纵向磁化强度在混合时间内交换，并在两个位置之间显示交叉峰，其增长给出速率。

### 13.6.5. 氢–氘交换

酰胺质子与水的质子交换，由 $\mathrm{OH^-}$ 催化（pH 3 以下则由 $\mathrm{H^+}$ 催化）。在无结构的肽中，本征速率 $k_{\mathrm{int}}$ 在 pH 7、$25\,{}^\circ\mathrm{C}$ 下约为 $1$–$10\,\mathrm{s^{-1}}$，在其最小值（约 pH $2.5$–$3$）之上每升高一个 pH 单位增大十倍，并以已被标定的方式依赖于相邻的侧链和温度（Bai、Englander 及其合作者，1993）。在折叠蛋白中，大多数酰胺形成氢键或被埋藏，只有当涨落打断氢键并使它们暴露时才发生交换。

**定义 13.6.5（氢–氘交换）** 氢–氘交换（HDX）是大分子的可交换氢，主要是主链酰胺氢，被 $\mathrm{D_2O}$ 中的氘取代（或反过来）。在 Linderstrøm-Lang 模型中，酰胺只能从开放态发生交换，

$$
\text{闭合态 (NH)} \underset{k_{\mathrm{cl}}}{\overset{k_{\mathrm{op}}}{\rightleftharpoons}} \text{开放态 (NH)} \overset{k_{\mathrm{int}}}{\longrightarrow} \text{开放态 (ND)}, \qquad k_{\mathrm{obs}} = \frac{k_{\mathrm{op}}k_{\mathrm{int}}}{k_{\mathrm{op}} + k_{\mathrm{cl}} + k_{\mathrm{int}}}. \tag{13.30}
$$

**定义 13.6.6（保护因子）** 酰胺的保护因子为 $P = k_{\mathrm{int}}/k_{\mathrm{obs}}$，即结构使其交换变慢的倍数。

两种极限使式 (13.30) 变得有用。当结构重新闭合远快于化学步骤，$k_{\mathrm{cl}} \gg k_{\mathrm{int}}$（天然条件下的通常情形，即 EX2 区），每次开启只给出很小的交换机会，$k_{\mathrm{obs}} = K_{\mathrm{op}}k_{\mathrm{int}}$，$K_{\mathrm{op}} = k_{\mathrm{op}}/k_{\mathrm{cl}} \ll 1$：保护因子度量的是开启的平衡常数，

$$
\Delta G_{\mathrm{op}} = -RT\ln K_{\mathrm{op}} = RT\ln P \qquad (\text{EX2}). \tag{13.31}
$$
当化学步骤快于重新闭合，$k_{\mathrm{int}} \gg k_{\mathrm{cl}}$（高 pH 或蛋白质失稳时，即 EX1 区），每次开启都导致交换，$k_{\mathrm{obs}} = k_{\mathrm{op}}$：即开启反应本身的速率。两种区域可由对 pH 的依赖性区分：EX2 中 $k_{\mathrm{obs}}$ 随 $k_{\mathrm{int}}$ 变化，每升高一个 pH 单位增大十倍；EX1 中则与 pH 无关。

这些自由能很大：$10^6$ 的保护因子在 $298\,\mathrm{K}$ 下对应 $34\,\mathrm{kJ\,mol^{-1}}$，稳定蛋白质中受保护最强的酰胺要经数周至数月才交换。对这些最慢的酰胺，$\Delta G_{\mathrm{op}}$ 等于由变性测得的整体去折叠自由能（[7.6.8](/7.6.8)）；其他酰胺则通过局部涨落或协同单元的亚整体去折叠而交换。Englander 及其合作者在逐渐增大的变性剂浓度下逐个残基测量 $\Delta G_{\mathrm{op}}$，由此提出折叠通过由协同单元，即折叠子（foldon），构成的部分去折叠形式进行的图景，最先是对**细胞色素** $c$（[7.6.16](/7.6.16)）。

在 NMR 中，HDX 的测量方法是把质子化的蛋白质溶于 $\mathrm{D_2O}$ 并随时间记录 HSQC 谱（变成 ND 的酰胺消失），或对更快的交换，通过来自水的磁化强度转移（CLEANEX 及相关的饱和转移方法），或在折叠期间做脉冲标记（淬灭流动），随后对复性的蛋白质做 NMR。在质谱（**氢氘交换质谱**，[6.4.15](/6.4.15)）中，蛋白质在 $\mathrm{D_2O}$ 中标记一定时间，通过把条件降到 pH 2.5 与 $0\,{}^\circ\mathrm{C}$（使交换减慢约 $10^4$ 倍）来淬灭交换，用胃蛋白酶消化蛋白质，并测量每个肽的质量增加。氢氘交换质谱的分辨率较低（5–20 个残基的肽），但没有大小限制，并且可以由同位素包络直接区分两种区域：EX2 使包络逐渐移动，EX1 则给出未交换与完全交换分子的双峰包络。它被广泛用于绘制大复合物与膜蛋白的**表位**、配体结合与构象变化图。

![Linderstrøm-Lang 模型中的氢–氘交换。A：对 k_op = 1 s⁻¹、k_cl = 10³ s⁻¹（ΔG_op = 17 kJ/mol）的位点，随 pH 升高使本征速率增大时的 k_obs：k_int ≪ k_cl 时为 EX2（k_obs = K_op k_int），k_int ≫ k_cl 时为 EX1（k_obs = k_op）。B：保护因子为 1 到 10⁶（k_int = 10 s⁻¹）时 D₂O 中剩余的酰胺 ¹H 的分数，及相应的开启自由能 RT ln P。C：含 12 个可交换酰胺的肽标记 1、10 与 100 s 后的模拟质谱：EX2 中每个酰胺独立交换，包络移动；EX1 中该片段在一次协同开启中交换，未交换与完全交换的布居共存](./plots/hdx.py)

## 13.7. 电子顺磁共振

### 13.7.1. 电子自旋共振

**电子顺磁共振**（[6.5.7](/6.5.7#def-7.4.1)）是未成对电子的磁共振，共振条件为 $h\nu = g\mu_{\mathrm{B}}B$，其中 $\mu_{\mathrm{B}}$ 是 **Bohr 磁子**，$g$ 值（自由电子为 $2.0023$）因自旋–轨道耦合而发生位移，起着化学位移的作用。由于电子的磁矩是质子的 658 倍，共振位于微波区：商品谱仪固定谐振腔的频率而扫描磁场。

| 波段 | L | S | X | Q | W |
|---|---|---|---|---|---|
| $\nu/\mathrm{GHz}$ | 1.5 | 3.0 | 9.5 | 34 | 95 |
| $g = 2.0023$ 的共振场 / mT | 54 | 107 | 339 | 1213 | 3390 |

X 波段是主力；Q 与 W 波段对 $g$ 各向异性的分辨更好，用于脉冲实验。谱图以场调制记录，呈现为吸收的一阶导数。$0.34\,\mathrm{T}$、$298\,\mathrm{K}$ 下电子的极化度为 $7.7\times10^{-4}$，是 $14.1\,\mathrm{T}$ 下质子的十六倍，而大得多的磁矩使 EPR 对微摩尔浓度的自旋就很灵敏。未成对电子通过**超精细耦合**（[6.5.7](/6.5.7#def-7.4.2)）与附近的磁性核相互作用，使谱线裂分为 $2nI + 1$ 个成分；弛豫时间是微秒而不是秒，所以脉冲 EPR 工作在纳秒时间尺度上，且通常在低温下进行。

生物样品含有天然的顺磁中心：电子传递链与酶中的铁硫簇、铜位点、黄素与醌的半醌以及酪氨酰自由基，自 1960 年代起即被 EPR 研究（呼吸链与光合链见 [7.1.23](/7.1.23) 和 [7.1.24](/7.1.24)）；还有**核糖核苷酸还原酶**的酪氨酰自由基，以及自由基与**活性氧**，后者通过**自旋捕获**（[6.5.7](/6.5.7)）检测。然而，大多数大分子是抗磁性的，EPR 在结构生物学中的普遍应用建立在连接顺磁标记的基础上。

### 13.7.2. 定点自旋标记

**定义 13.7.1（定点自旋标记）** 定点自旋标记（SDSL；Hubbell 及其合作者，自 1989 年起）是把稳定的顺磁基团，即自旋标记，共价连接到大分子的选定位点上，使 EPR 报告其局部环境、流动性以及与其他标记之间的距离。

好的自旋标记应当体积小、稳定、特异连接且扰动最小，并且具有对环境敏感的简单谱。标准的标记是硝酰基 MTSL，它与半胱氨酸的巯基反应：通过突变去除天然暴露于溶剂的半胱氨酸，再在“半胱氨酸扫描”中逐个位点地在每个感兴趣的位点引入半胱氨酸。所得的侧链称为 R1，具有五个键的柔性连接臂，使电子位于距主链 $0.6$–$0.8\,\mathrm{nm}$ 处，并给距离增加零点几纳米的不确定度。替代方案包括刚性标记（连在两个半胱氨酸上的双功能 RX 标记，或螺旋中 $i, i+4$ 位的双组氨酸基序螯合 Cu²⁺）、在细胞的还原性内部环境中稳定并很适合高场 EPR 的 Gd³⁺ 螯合物、室温下弛豫时间长的三苯甲基自由基，以及作为非天然氨基酸引入的标记，对 RNA 则是在化学合成时或通过修饰的核苷酸引入。

### 13.7.3. 硝酰基的谱与流动性

硝酰基的未成对电子主要位于 N–O 基团的 $\pi$ 轨道上，并与 $^{14}\mathrm{N}$ 核（$I = 1$）耦合，所以谱由三条线 $m_I = +1, 0, -1$ 组成，间隔为各向同性超精细耦合 $a \approx 1.5\,\mathrm{mT}$。$g$ 值与超精细耦合都是各向异性的（近似轴对称：沿 $\pi$ 轨道 $A_\parallel \approx 3.5\,\mathrm{mT}$，$A_\perp \approx 0.6\,\mathrm{mT}$；$g_\parallel \approx 2.0027$，$g_\perp \approx 2.0075$），各向异性被运动平均，与 NMR 中完全相同，但时间尺度由各向异性本身决定，$(A_\parallel - A_\perp)\gamma_{\mathrm{e}} \approx 5\times10^8\,\mathrm{s^{-1}}$，所以 X 波段的硝酰基谱对 $0.1$ 到约 $100\,\mathrm{ns}$ 的**转动相关时间**敏感：

- 当 $\tau_{\mathrm{c}} \lesssim 0.1\,\mathrm{ns}$（水中的自由标记）时，三条线都很窄且几乎相等；
- 当 $\tau_{\mathrm{c}}$ 约为 $0.5$–$2\,\mathrm{ns}$ 时，各线不等量地变宽，高场线最甚，因为线宽按 $A + Bm_I + Cm_I^2$ 依赖于 $m_I$，其中 $B$ 与 $C$ 正比于 $\tau_{\mathrm{c}}$（Kivelson 的运动窄化理论）；
- 对更慢的运动，谱的形状逐渐向取向随机的不动标记的刚性极限“粉末”谱变化，其外侧极值相距约 $2A_\parallel$；这一区域的模拟需要 Freed 的随机 Liouville 方程；饱和转移 EPR 把灵敏范围扩展到毫秒。

对连在蛋白质上的标记，有效 $\tau_{\mathrm{c}}$ 反映的是侧链相对主链的运动，而不是整个蛋白质的翻滚（必要时用蔗糖或 Ficoll 使之变慢）。因此，流动性可以区分位于环上（流动）、螺旋表面（中等）以及位于三级接触或埋藏位置（固定）的位点，沿半胱氨酸扫描的流动性周期则揭示螺旋（周期 3.6）与链（周期 2）。各位点对顺磁弛豫剂 $\mathrm{O_2}$（可溶于膜）与 $\mathrm{NiEDDA}$（水溶）的可及性由功率饱和测得，说明它面向脂质还是水：在高分辨率结构出现很久之前，SDSL 就绘出了**视紫红质**、钾通道 KcsA 以及转运蛋白等膜蛋白的拓扑与构象变化。

![硝酰基自旋标记的 X 波段（9.5 GHz）连续波 EPR。A：电子 Zeeman 能级因与 ¹⁴N（I = 1）的超精细耦合而分裂；三个允许的跃迁（Δm_S = ±1，Δm_I = 0）给出间隔为 a 的三条线。B：快运动区（τc = 0.1、0.5 与 1.5 ns，线宽取自轴对称 g 与 A 张量的运动窄化表达式；高场线增宽最多）与刚性极限（固定标记的粉末谱，外侧极值相距约 2A∥）的一阶导数谱。2–100 ns 的中间区域需要随机 Liouville 方程，未予计算](./plots/nitroxide.py)

### 13.7.4. 用 DEER 测距离

相距 $r$ 的两个电子自旋通过各自的偶极场相互作用。

**公式 13.7.1（电子–电子偶极耦合）** 对 $g \approx 2.0023$ 的两个自旋，其连线与 $\boldsymbol{B}_0$ 成角 $\theta$，在弱耦合极限下，

$$
\nu_{\mathrm{dd}}(r, \theta) = \frac{\mu_0g_{\mathrm{A}}g_{\mathrm{B}}\mu_{\mathrm{B}}^2}{4\pi h}\,\frac{1}{r^3}\,(3\cos^2\theta - 1) = \frac{52.04\,\mathrm{MHz\,nm^3}}{r^3}\,(3\cos^2\theta - 1). \tag{13.32}
$$

对 $r = 3\,\mathrm{nm}$，垂直频率为 $\nu_\perp = 52.04/27\,\mathrm{MHz} = 1.93\,\mathrm{MHz}$；在冷冻的、取向随机的样品中，$\theta$ 的分布产生 Pake 图样，其峰位于 $\pm\nu_\perp$，边缘位于 $\pm2\nu_\perp$。在约 $1.5$–$2\,\mathrm{nm}$ 以下，耦合使连续波谱明显变宽，可从线形中提取；在此以上，它隐藏在谱的非均匀宽度中，必须用脉冲实验把它分离出来。

**定义 13.7.2（双电子–电子共振）** 双电子–电子共振（DEER，亦称脉冲电子–电子双共振，PELDOR）利用对一组自旋（观测频率）的自旋回波序列测量电子自旋之间的偶极耦合，在此期间第二个频率下的泵浦脉冲在可变的时刻 $t$ 使配偶自旋反转；这一反转使被观测自旋处的局部场改变一个偶极场，并使重聚的回波随 $t$ 调制。在四脉冲版本（Pannier、Jeschke 及其合作者，2000）中，序列为 $\frac\pi2 - \tau_1 - \pi - (\tau_1 + t) - \pi_{\mathrm{pump}} - (\tau_2 - t) - \pi - \tau_2 - \text{回波}$，它给出从 $t = 0$ 开始、没有死时间的信号。

双标记分子样品的 DEER 信号为

$$
V(t) = \left[(1 - \lambda) + \lambda\int_0^\infty P(r)K(t, r)\,\mathrm{d}r\right]B(t), \qquad K(t, r) = \int_0^1\cos\left[(3x^2 - 1)\,2\pi\nu_\perp(r)t\right]\mathrm{d}x, \tag{13.33}
$$
其中 $P(r)$ 为距离分布，核 $K$ 对取向（$x = \cos\theta$）平均偶极振荡，$\lambda$ 为被泵浦脉冲反转的配偶自旋的比例（调制深度，硝酰基为 $0.3$–$0.5$），$B(t)$ 是来自其他分子中自旋的背景，$\exp[-(kt)^{d/3}]$，均匀溶液中 $d = 3$。由 $V(t)$ 恢复 $P(r)$ 是不适定的反问题，与小角 X 射线散射的**间接 Fourier 变换**（[7.6.9](/7.6.9#sec-9.10.4)）属于同一类：$V$ 中的小噪声会在 $P$ 中产生大的振荡，通过 Tikhonov 正则化使解稳定，即在 $P \ge 0$ 的条件下最小化 $\lVert KP - V\rVert^2 + \alpha^2\lVert LP\rVert^2$，其中 $L$ 为二阶导数算子，正则化参数 $\alpha$ 由 L 曲线或统计判据选取。程序有：DeerAnalysis、DeerLab，以及神经网络方法（DEERNet）。

可测量的范围约为 $1.8$–$6\,\mathrm{nm}$，下限由脉冲的带宽决定（高于约 $10\,\mathrm{MHz}$ 的偶极频率不被激发），上限由电子的相位记忆时间所允许的偶极演化时间决定：要确定平均距离 $r$，迹线需持续约 $2\,\mu\mathrm{s}\times(r/5\,\mathrm{nm})^3$，要确定分布的宽度则约需两倍之久。蛋白质与溶剂的氘代延长相位记忆时间，使范围扩展到 $8$–$10\,\mathrm{nm}$，有利时还可更远。样品在成玻璃的缓冲液（含甘油）中冷冻到 $50$–$80\,\mathrm{K}$，所以分布是冷冻温度下构象系综的快照；样品量为数十微升、$10$–$100\,\mu\mathrm{M}$，对分子大小没有上限。自旋标记之间的距离不是主链原子之间的距离：要用标记侧链的旋转异构体库（MMM、chiLife）把测得的分布转换为结构约束。

**例 13.7.1（GPCR 的偏向激动剂）** 对血管紧张素 II 1 型受体（一种 G 蛋白偶联受体）胞质侧的成对自旋标记，在不同效力的配体存在下测得的 DEER 距离分布表明，受体占据多种构象，其相对布居依赖于配体，而不是在单一的失活与单一的活化结构之间切换；使信号偏向 **G 蛋白**或偏向 β **抑制蛋白**的配体，稳定的构象集合不同（Wingler 及其合作者，2019）。这类距离分布揭示了单一结构无法显示的构象平衡。

**例 13.7.2（细胞内 EPR）** 用抗还原的硝酰基标记的 RNA 双链，显微注射到非洲爪蟾（*Xenopus laevis*）卵母细胞中，给出的 DEER 距离分布比在缓冲液中略短，接近在浓蛋白溶液中的测量值，与拥挤导致的适度紧缩一致（[7.6.23](/7.6.23)）（Collauto 及其合作者，2020）。能在细胞质还原环境中存活的 Gd³⁺ 与三苯甲基标记，使这类细胞内测量日益普遍。

![DEER：从距离分布到时间迹线再返回。A：3.0 nm（60 %）与 4.2 nm（40 %）两种构象的混合物，以及用二阶导数惩罚与非负约束的 Tikhonov 正则化恢复的分布。B：调制深度为 0.35、带均匀背景与噪声的模拟迹线 V(t)（灰色），扣除背景后的形状因子（紫色）及其拟合（橙色），以及单个 3.0 nm 自旋对的偶极振荡（错开显示）。C：3.0 nm 自旋对的 Pake 图样，即取向平均的偶极谱，峰位于 ν⊥ = 1.93 MHz，边缘位于 2ν⊥](./plots/deer.py)

### 13.7.5. 动态核极化

由于在同一磁场中电子的极化比质子强 658 倍，把电子的极化转移给核，可使 NMR 信号最多提高到这一倍数。这是 Overhauser 在 1953 年的预言，同年由 Carver 与 Slichter 在金属中验证。

**定义 13.7.3（动态核极化）** 动态核极化（DNP）是在电子共振附近用微波辐照，通过电子自旋与核自旋之间的超精细或偶极耦合，把电子自旋的大极化转移给核自旋，使核极化度最多提高到 $\gamma_{\mathrm{e}}/\gamma_{\mathrm{H}} \approx 658$ 的倍数。

在现代魔角旋转 DNP 中，掺有稳定双自由基的样品冷冻到约 $100\,\mathrm{K}$，由回旋管在电子频率下辐照（质子频率 $400$–$800\,\mathrm{MHz}$ 对应 $263$–$527\,\mathrm{GHz}$）；$20$–$200$ 的增强使得研究低浓度的蛋白质、膜中和细胞中的蛋白质成为可能。在溶解 DNP 中，在约 $1\,\mathrm{K}$ 下极化的样品被迅速溶解并注射；丙酮酸经超极化的 $^{13}\mathrm{C}$ 在极化弛豫之前一分钟内成像，显示出患者肿瘤中丙酮酸转化为乳酸的过程，这是代谢成像的一种应用（13.8）。

## 13.8. 磁共振成像

### 13.8.1. 空间编码

**磁共振成像**（[6.4.12](/6.4.12#def-12.6.3)）利用水（软组织中约 $80\,\mathrm{M}$）与脂肪中的质子。在均匀磁场中，所有水质子以同一频率共振；线性场梯度使频率依赖于位置，

$$
\omega(\boldsymbol{x}) = \gamma\left(B_0 + \boldsymbol{G}\cdot\boldsymbol{x}\right) \tag{13.34}
$$
（取其大小），所以在梯度 $G_x$ 下记录的谱就是质子密度在 $x$ 上的投影。Lauterbur 的首批图像（1973）由多个角度的投影重建物体，即计算机断层成像的方法。现代 MRI 把位置编码在相位与频率中，并通过 **Fourier 变换**重建。

**定理 13.8.1（k 空间）** 激发了密度为 $\rho(\boldsymbol{x})$ 的一个层面的自旋之后，在施加梯度 $\boldsymbol{G}(t)$ 期间记录的信号，在旋转坐标系中且忽略弛豫时为

$$
s(t) = \int\rho(\boldsymbol{x})\,\mathrm{e}^{-\mathrm{i}2\pi\boldsymbol{k}(t)\cdot\boldsymbol{x}}\,\mathrm{d}\boldsymbol{x}, \qquad \boldsymbol{k}(t) = \frac{\gamma}{2\pi}\int_0^t\boldsymbol{G}(t')\,\mathrm{d}t'. \tag{13.35}
$$
信号是图像的二维 Fourier 变换，在梯度波形于 k 空间中描出的轨迹 $\boldsymbol{k}(t)$ 上取值。

**证明** 位于 $\boldsymbol{x}$ 处的自旋相对于 $\gamma B_0$ 处的发射机积累的相位为 $\int_0^t\gamma\boldsymbol{G}(t')\cdot\boldsymbol{x}\,\mathrm{d}t' = 2\pi\boldsymbol{k}(t)\cdot\boldsymbol{x}$（进动的符号已吸收在约定中），线圈把所有自旋按其密度加权的贡献求和。$\square$

因此，成像序列在 k 空间中操控 $\boldsymbol{k}$。在标准的自旋翘曲序列中，层面由与梯度 $G_z$ 一起施加的成形射频脉冲选出：只有频率落在脉冲带宽 $\Delta f$ 内的自旋被激发，层厚为 $\Delta z = 2\pi\Delta f/(\gamma G_z)$（取 $\gamma/2\pi = 42.58\,\mathrm{MHz\,T^{-1}}$、$\Delta f = 1\,\mathrm{kHz}$、$G_z = 10\,\mathrm{mT\,m^{-1}}$，则 $\Delta z = 2.3\,\mathrm{mm}$）。短暂施加的相位编码梯度 $G_y$ 设定 $k_y$；然后在恒定的频率编码梯度 $G_x$ 下读出信号，它沿一条线扫描 $k_x$；对每个 $k_y$ 重复该序列，再做二维逆 FFT 即得图像。k 空间的采样决定图像：视野为 $1/\Delta k$，分辨率为 $1/(2k_{\max})$，所以对 k 空间的粗采样使图像折叠（混叠），而截去其外围部分则使图像模糊（下图）。回波平面成像在一次激发中约 $50\,\mathrm{ms}$ 内覆盖整个 k 空间；利用接收线圈阵列的并行成像与压缩感知则由欠采样的 k 空间重建图像，使扫描缩短数倍。

### 13.8.2. 对比度

软组织之间的质子密度差别不大，但 $T_1$ 与 $T_2$ 差别很大，因为组织中的水与结合在大分子上的水发生交换，其弛豫反映局部的组成。在重复时间为 TR、回波时间为 TE 的自旋回波序列中，

$$
S = \rho\left(1 - \mathrm{e}^{-\mathrm{TR}/T_1}\right)\mathrm{e}^{-\mathrm{TE}/T_2}. \tag{13.36}
$$
短 TR 与短 TE 给出 $T_1$ 加权像（$T_1$ 短的白质较亮，脑脊液较暗）；长 TR 与长 TE 给出 $T_2$ 加权像（液体较亮），其中水肿与许多病灶突出显现。造影剂是 Gd³⁺ 螯合物，它通过 13.5.4 的顺磁弛豫增强缩短附近水的 $T_1$，使灌注良好的组织和渗漏的血管变亮。其他对比度来自生理。在扩散加权成像中，一对强梯度脉冲使自旋退相位又重聚，在其间运动的分子使信号按 $S = S_0\mathrm{e}^{-bD}$ 衰减（Stejskal–Tanner 关系，$b = \gamma^2G^2\delta^2(\Delta - \delta/3)$，梯度脉冲长为 $\delta$、间隔为 $\Delta$）：这是对水的**扩散系数**（[7.6.5](/7.6.5)）的直接测量，其在数分钟内下降提示缺血性卒中，其方向依赖性则勾画出神经纤维束。在功能 MRI 中，脱氧血红蛋白是顺磁性的，神经活动之后血氧的局部升高使 $T_2^*$ 变长，并使信号升高约 1 %（血氧水平依赖，BOLD，对比度）。

临床扫描仪工作在 $1.5$ 与 $3\,\mathrm{T}$（质子频率 $64$ 与 $128\,\mathrm{MHz}$），研究用扫描仪在 $7\,\mathrm{T}$ 以上，梯度为 $40$–$80\,\mathrm{mT\,m^{-1}}$；没有电离辐射且软组织对比度好，使 MRI 成为脑、脊髓、关节和许多肿瘤的首选方法。同样的物理，在高得多的梯度下，给出磁共振显微术和 NMR 管中扩散的测量，后者用于确定蛋白质的流体力学半径（DOSY）。

![用 128 × 128 数值体模展示的 MRI 空间编码与对比度。A：体模，T₁ 加权（TR = 0.5 s，TE = 15 ms）。B：在线性梯度下，层面的谱是其在 x 上的投影。C：对数标度的 k 空间；记录的信号是图像的 Fourier 变换。D：只对 k 空间中央 32 × 32 个点做逆变换，得到模糊的图像。E：每隔一条相位编码线省略一条：视野减半，图像折叠。F：TR = 3 s 时白质、灰质与脑脊液的自旋回波信号随 TE 的变化（1.5 T 下的近似值）：长 TE 给出 T₂ 加权，其中脑脊液较亮](./plots/mri.py)

## 13.9. 结构方法中的磁共振

| | 溶液 NMR | 固体 NMR | EPR (DEER) | X 射线晶体学 | 冷冻电镜 |
|---|---|---|---|---|---|
| 样品 | $0.1$–$1\,\mathrm{mM}$，$0.3\,\mathrm{mL}$，同位素标记 | 数毫克固体、纤维或蛋白脂质体 | $10$–$100\,\mu\mathrm{M}$，$20\,\mu\mathrm{L}$，自旋标记 | 晶体 | $\sim1\,\mu\mathrm{M}$，$3\,\mu\mathrm{L}$，玻璃态冷冻 |
| 大小 | 最适 $< 30\,\mathrm{kDa}$；借助甲基 TROSY，动力学可达 $\sim1\,\mathrm{MDa}$ | 原则上无限制 | 无限制 | 能结晶则无限制 | 最适 $> 50\,\mathrm{kDa}$ |
| 信息 | 原子约束、系综、皮秒到数月的动态、弱结合 | 不溶性组装体的原子结构 | $1.8$–$10\,\mathrm{nm}$ 的距离分布 | 原子结构，一个主导状态 | 原子结构，多个状态 |
| 长处 | 柔性、无序、次要态、溶液条件 | 淀粉样物、双层中的膜蛋白 | 大蛋白与膜蛋白，细胞内 | 精度、配体 | 大型复合物、异质性 |

这些方法是互补而不是竞争的。现代的典型研究把来自晶体学、冷冻电镜或预测的结构，与 NMR 对其动态和次要态的测量、DEER 对其在膜中构象平衡的分布，以及溶液中对其整体形状的小角 X 射线散射（[7.6.9](/7.6.9#sec-9.14)）结合在一个整合模型（[7.6.15](/7.6.15)）中。磁共振的独特贡献是任何图像都无法给出的：布居与互变的速率、运动的幅度，以及没有单一结构的分子的结构系综。

## 小结

- 自旋与灵敏度。$\boldsymbol{\mu} = \gamma\boldsymbol{I}$；Zeeman 能级 $E_m = -\gamma\hbar B_0m$；Larmor 频率 $\omega_0 = -\gamma B_0$（定义 13.1.1；$^1\mathrm{H}$ 在 $14.1\,\mathrm{T}$ 下为 $600\,\mathrm{MHz}$）。极化度 $\hbar\gamma B_0/2k_{\mathrm{B}}T \approx 5\times10^{-5}$；Curie 磁化强度 $M_0 \propto N\gamma^2B_0/T$（公式 13.1.1）；$S/N \propto N\gamma_{\mathrm{exc}}\gamma_{\mathrm{det}}^{3/2}B_0^{3/2}\sqrt{n_{\mathrm{s}}}$，故在质子上激发与检测。自旋 1/2 的核（$^1\mathrm{H}$、$^{13}\mathrm{C}$、$^{15}\mathrm{N}$、$^{19}\mathrm{F}$、$^{31}\mathrm{P}$）通过同位素标记使用；$^{17}\mathrm{O}$ 的 $I = 5/2$。
- Bloch 方程（定理 13.2.1，定义 13.2.1–13.2.2）：绕 $\boldsymbol{B}$ 进动；在旋转坐标系中，绕 $B_1$ 转角为 $\beta = \gamma B_1t_{\mathrm{p}}$ 的脉冲；$T_1$ 对应布居的恢复，$T_2$ 对应相位相干的丧失，$T_2 \le 2T_1$。FID 与宽度为 $1/(\pi T_2)$、面积不变的 Lorentz 线（公式 13.2.1）。自旋回波（定义 13.2.3）使静态退相位重聚；CPMG 与反转恢复分别测量 $T_2$ 与 $T_1$。
- 弛豫与运动。谱密度 $J(\omega) = \frac25\tau_{\mathrm{c}}/(1 + \omega^2\tau_{\mathrm{c}}^2)$（定义 13.3.1），$\tau_{\mathrm{c}} \approx 0.5$–$0.6\,\mathrm{ns/kDa}$。BPP（定理 13.3.1）：$T_1$ 在 $\omega_0\tau_{\mathrm{c}} = 0.62$ 处有极小值，$T_2$ 通过 $J(0)$ 正比于 $1/\tau_{\mathrm{c}}$：这就是大小限制。$^{15}\mathrm{N}$ 的 $R_1$、$R_2$、NOE（公式 13.3.1）。氘代、TROSY（定义 13.3.2）、甲基 TROSY、$^{19}\mathrm{F}$、固体 NMR。
- 谱。位移范围、折叠与无序蛋白的分散度、碱基对的亚氨基质子、二级位移；Karplus 关系 $^3J(\mathrm{H}^{\mathrm{N}},\mathrm{H}^\alpha) = 6.51\cos^2\theta - 1.76\cos\theta + 1.60\,\mathrm{Hz}$（公式 13.4.1）。密度算符，$\mathrm{d}\hat\rho/\mathrm{d}t = -\mathrm{i}[\hat{H}, \hat\rho]$（定义 13.4.1），乘积算符；INEPT 的 HSQC（例 13.4.1）；COSY、TOCSY、NOESY，三共振归属；化学位移扰动（定义 13.4.2）。
- 约束与结构。NOE：交叉弛豫 $\sigma \propto r^{-6}[6j(2\omega_0) - j(0)]$，在 $\omega_0\tau_{\mathrm{c}} = 1.12$ 处变号，距离至 $0.5\,\mathrm{nm}$，自旋扩散（公式 13.5.1）。RDC $D = -\frac{\mu_0\gamma_I\gamma_S\hbar}{8\pi^2r^3}\langle3\cos^2\theta - 1\rangle$，全局取向，N–H 的符号相反（定义 13.5.1，注 13.5.1）。PRE（$r^{-6}$，至 $3\,\mathrm{nm}$）与 PCS（$r^{-3}$，至 $5\,\mathrm{nm}$）（定义 13.5.2–13.5.3）。**模拟退火**得到结构系综（算法 13.5.1）。
- 动态。化学交换与 Bloch–McConnell 方程（定义 13.6.1，公式 13.6.1）：慢、中、快；$R_{\mathrm{ex}} = p_{\mathrm{A}}p_{\mathrm{B}}\Delta\omega^2/k_{\mathrm{ex}}$；滴定中 $k_{\mathrm{ex}} = k_{\mathrm{on}}[\mathrm{L}] + k_{\mathrm{off}}$（例 13.6.1）。无模型 $S^2$、$\tau_{\mathrm{e}}$（定义 13.6.2–13.6.3）。针对不可见态的弛豫色散（定义 13.6.4）、CEST、ZZ 交换。HDX：$k_{\mathrm{obs}} = k_{\mathrm{op}}k_{\mathrm{int}}/(k_{\mathrm{op}} + k_{\mathrm{cl}} + k_{\mathrm{int}})$；EX2 时 $\Delta G_{\mathrm{op}} = RT\ln P$，EX1 时 $k_{\mathrm{obs}} = k_{\mathrm{op}}$（定义 13.6.5–13.6.6）。
- EPR。$h\nu = g\mu_{\mathrm{B}}B$，X 波段在 $0.34\,\mathrm{T}$ 下为 $9.5\,\mathrm{GHz}$；SDSL（定义 13.7.1）；由线形得到硝酰基的流动性；DEER 的 $\nu_\perp = 52.04\,\mathrm{MHz\,nm^3}/r^3$（公式 13.7.1），经正则化反演得到 $1.8$–$6$（至 $10$）nm 的距离分布（定义 13.7.2）；DNP（定义 13.7.3）。
- MRI。梯度编码位置，信号是 k 空间中图像的 Fourier 变换（定理 13.8.1）；对比度来自 $T_1$、$T_2$、Gd³⁺（PRE）、扩散与 BOLD。

## 思考题

1. 把一个蛋白质样品从 $600\,\mathrm{MHz}$ 谱仪换到 $1.2\,\mathrm{GHz}$ 仪器上。下列量各变为原来的多少倍：(a) 质子的极化度，(b) HSQC 预期的信噪比，(c) 相距 $0.05\,\mathrm{ppm}$ 的两个酰胺峰的赫兹间隔，(d) 它们的 $^3J(\mathrm{H}^{\mathrm{N}},\mathrm{H}^\alpha)$ 裂分？

   **答** (a) 极化度 $\propto B_0$：2 倍。(b) 式 (13.5)：$B_0^{3/2}$，即 $2^{3/2} = 2.8$ 倍（实际上略小，因为 $R_2$ 也会改变，探头也不同）；达到同样的信噪比只需 $1/8$ 的时间。(c) 以赫兹计的位移随 $B_0$ 标度：$0.05\,\mathrm{ppm}$ 在 $600\,\mathrm{MHz}$ 下为 $30\,\mathrm{Hz}$，在 $1.2\,\mathrm{GHz}$ 下为 $60\,\mathrm{Hz}$，所以只要线宽的增长慢于线性，峰就分辨得更好。(d) $J$ 耦合与磁场无关：不变。

2. 证明对由涨落场弛豫的自旋有 $T_2 \le 2T_1$（提示：考虑两个能级之间的跃迁对自旋相位的作用），并解释为什么蛋白质的 $T_1$ 与 $T_2$ 之差很大，而水的却很小。

   **答** 每个自旋是一个二能级体系；以速率 $W$（向上与向下）改变布居的过程，使 $M_z$ 以 $2W$ 弛豫，并以 $W$ 破坏横向分量的相干（每次跃迁使一个自旋的相位随机化），所以布居对 $R_2$ 的贡献为 $R_1/2$，而长期的（零频）退相位只能再增加它：$R_2 = R_1/2 + R_2'$，$R_2' \ge 0$，即 $T_2 \le 2T_1$。（对偶极对，式 (13.14) 在极端窄化时给出 $T_2 = T_1$，与此一致。）在式 (13.14) 中，$R_2$ 的额外项为 $\frac{9}{20}K^2j(0) \propto \tau_{\mathrm{c}}$，而 $R_1$ 依赖于 $j(\omega_0)$ 与 $j(2\omega_0)$。对水，$\tau_{\mathrm{c}} \approx 3\,\mathrm{ps}$，$\omega_0\tau_{\mathrm{c}} \approx 10^{-2}$，所有 $j$ 相等，$T_1 = T_2$；对 $\tau_{\mathrm{c}} = 10\,\mathrm{ns}$ 的蛋白质，$\omega_0\tau_{\mathrm{c}} \approx 40$，$j(\omega_0)$ 只有 $j(0)$ 的 $1/1600$，所以 $T_1$ 长而 $T_2$ 短。

3. 一个 $40\,\mathrm{kDa}$ 的蛋白质，在 $600\,\mathrm{MHz}$、$25\,{}^\circ\mathrm{C}$ 下的 $^1\mathrm{H}$–$^{15}\mathrm{N}$ HSQC 很差，峰宽且相互重叠。列出可能的原因，以及你会做哪些实验来区分它们并改进谱图。

   **答** 原因：(i) 单体慢翻滚（$\tau_{\mathrm{c}} \approx 20$–$24\,\mathrm{ns}$），或 (ii) 寡聚或聚集（用 SEC–**静态光散射**、DLS，或由 $R_2/R_1$ 得到的 $\tau_{\mathrm{c}}$ 检查；稀释，改变盐浓度或 pH）；(iii) 中等区域的化学交换，例如单体–二聚体平衡或构象交换（线宽的温度依赖性、弛豫色散；加入配体或稳定性突变可能使平衡移动）；(iv) 部分去折叠或异质性（$8.2\,\mathrm{ppm}$ 附近的窄簇表示无序；用 CD、DSC 检查）。改进方法：升高温度（使 $\tau_{\mathrm{c}}$ 变短），使蛋白质氘代并在可用的最高磁场下记录 TROSY 谱，采用甲基标记与甲基 TROSY，或研究分离的结构域；对非常大或不溶的体系，则转向 $^{19}\mathrm{F}$ NMR 或固体 NMR。

4. 对一个二自旋体系，用乘积算符从 $\hat{I}_z$ 出发追踪 INEPT 转移：对 $I$ 施加 $90^\circ_x$ 脉冲，延迟 $\tau$，对 $I$ 与 $S$ 施加 $180^\circ_x$ 脉冲，延迟 $\tau$，然后对 $I$ 施加 $90^\circ_y$、对 $S$ 施加 $90^\circ_x$。最终状态作为 $\tau$ 的函数是什么？为什么选 $\tau = 1/(4J)$？与直接激发 $S$ 相比，这一转移使 $S$（$^{15}\mathrm{N}$）的信号增大多少倍？

   **答** $90^\circ_x$：$\hat{I}_z \to -\hat{I}_y$。$\tau$–$180^\circ$–$\tau$ 单元使 $I$（以及 $S$）的位移重聚，而耦合因两个自旋都被反转而不受影响，演化 $2\tau$：$-\hat{I}_y \to -\hat{I}_y\cos(2\pi J\tau) + 2\hat{I}_x\hat{S}_z\sin(2\pi J\tau)$，符号由反转决定。对 $I$ 的 $90^\circ_y$ 使 $\hat{I}_x \to -\hat{I}_z$，对 $S$ 的 $90^\circ_x$ 使 $\hat{S}_z \to -\hat{S}_y$：反相项成为 $2\hat{I}_z\hat{S}_y\sin(2\pi J\tau)$，即 $S$ 的相干，当 $2\pi J\tau = \pi/2$ 时最大，对 $J = 92\,\mathrm{Hz}$ 即 $\tau = 1/(4J) = 2.7\,\mathrm{ms}$。其幅度携带 $I$ 的极化，所以 $S$ 的信号增大 $\gamma_I/\gamma_S = 9.9$ 倍（对 $^1\mathrm{H} \to {}^{15}\mathrm{N}$，取其大小）；回到 $^1\mathrm{H}$ 上检测使增益进一步放大（式 13.5）。

5. 蛋白质中的两个质子对，在同一张短混合时间的谱中给出强度之比为 1 : 0.2 的 NOESY 交叉峰。第一对是 $0.25\,\mathrm{nm}$ 的参照。估计第二个距离，并讨论为什么这类距离只用作上界。

   **答** 式 (13.21)：$r = 0.25 \times (1/0.2)^{1/6} = 0.25 \times 1.31 = 0.33\,\mathrm{nm}$。用作上界的原因是：(i) 有效距离是 $\langle r^{-6}\rangle^{-1/6}$，偏向最近的接近；(ii) 内部运动改变每一对的有效相关时间，所以强度不仅仅按 $r^{-6}$ 标度；(iii) 通过第三个质子的自旋扩散可使交叉峰增强；(iv) 强度因差异弛豫与部分饱和而减小。误差大多使一对质子看起来比实际近或远一个适度的因子，而六次方根压缩了这些误差，所以取 $\le 0.35$–$0.4\,\mathrm{nm}$ 一类的界限是安全的。

6. 若取向使沿主轴的键有 $\langle3\cos^2\theta - 1\rangle = 2\times10^{-3}$，计算 $\mathrm{C}^\alpha$–$\mathrm{H}^\alpha$ 键（$r = 0.109\,\mathrm{nm}$）的最大残余偶极耦合，并与单键标量耦合比较。为什么单个 RDC 不能确定键的取向，如何减小这种简并？

   **答** 式 (13.22)：$\mu_0\gamma_{\mathrm{H}}\gamma_{\mathrm{C}}\hbar/(8\pi^2r^3) = (1.2566\times10^{-6} \times 2.675\times10^8 \times 6.728\times10^7 \times 1.0546\times10^{-34})/(78.96 \times 1.295\times10^{-30}) = 23.3\,\mathrm{kHz}$，所以 $D = -23.3\,\mathrm{kHz} \times 2\times10^{-3} = -47\,\mathrm{Hz}$，约为 $^1J_{\mathrm{CH}} \approx 140\,\mathrm{Hz}$ 的三分之一。一个 RDC 只把键限制在绕主轴的一个方向锥上（及其镜像，即 $\theta$ 与 $180^\circ - \theta$）。减小简并的办法有：测量同一刚性单元中取向不同的许多键（这也决定张量）、测量多种键（$\mathrm{N}$–$\mathrm{H}$、$\mathrm{C}^\alpha$–$\mathrm{H}^\alpha$、$\mathrm{C}'$–$\mathrm{N}$），以及采用张量取向不同的第二种取向介质；除非与其他数据（NOE、PCS、小角 X 射线散射）结合，结构域取向的四重歧义仍然存在。

7. 自由蛋白质的一个峰在结合配体时 $^{15}\mathrm{N}$ 位移 $0.5\,\mathrm{ppm}$（$^{15}\mathrm{N}$ 为 $60\,\mathrm{MHz}$）。若 $k_{\mathrm{on}} = 10^8\,\mathrm{M^{-1}\,s^{-1}}$，对 $K_{\mathrm{d}} = 10\,\mu\mathrm{M}$，滴定中点处的交换处于什么区域？估计中点处交换对 $^{15}\mathrm{N}$ 线宽的贡献。

   **答** $\Delta\nu = 0.5 \times 60 = 30\,\mathrm{Hz}$，$\lvert\Delta\omega\rvert = 188\,\mathrm{s^{-1}}$。在中点，$k_{\mathrm{ex}} = 2k_{\mathrm{off}} = 2 \times 10^8 \times 10^{-5} = 2000\,\mathrm{s^{-1}} \approx 10\lvert\Delta\omega\rvert$：快交换，峰发生移动。式 (13.27)，$p_{\mathrm{A}} = p_{\mathrm{B}} = 0.5$：$R_{\mathrm{ex}} = 0.25 \times 188^2/2000 = 4.4\,\mathrm{s^{-1}}$，线宽增加 $1.4\,\mathrm{Hz}$，很小。对同一配体，在 $600\,\mathrm{MHz}$ 下位移 $0.5\,\mathrm{ppm}$ 的质子峰（$\lvert\Delta\omega\rvert = 1885\,\mathrm{s^{-1}}$）将处于中等交换而强烈变宽（由式 (13.27) 得 $R_{\mathrm{ex}} \approx 440\,\mathrm{s^{-1}}$，在此速率下这只是定性的）。

8. 在天然条件下，某酰胺在 pH 7（此时 $k_{\mathrm{int}} = 4\,\mathrm{s^{-1}}$）以 $k_{\mathrm{obs}} = 2\times10^{-6}\,\mathrm{s^{-1}}$ 交换；在 pH 8 时 $k_{\mathrm{obs}} = 2\times10^{-5}\,\mathrm{s^{-1}}$。适用哪种区域？计算 $298\,\mathrm{K}$ 下的保护因子与 $\Delta G_{\mathrm{op}}$，以及交换的半衰期。你将如何检验这个酰胺是否报告整体去折叠？

   **答** $k_{\mathrm{obs}}$ 随 pH 增大十倍，与 $k_{\mathrm{int}}$ 一样：EX2。$P = 4/(2\times10^{-6}) = 2\times10^6$；$\Delta G_{\mathrm{op}} = 8.314 \times 298 \times \ln(2\times10^6) = 36\,\mathrm{kJ\,mol^{-1}}$。半衰期 $\ln2/k_{\mathrm{obs}} = 3.5\times10^5\,\mathrm{s} = 4\,\mathrm{d}$。检验：把 $\Delta G_{\mathrm{op}}$ 与化学或热变性得到的去折叠 $\Delta G$（[7.6.8](/7.6.8)）比较，并在逐渐增大的变性剂浓度下测量 $\Delta G_{\mathrm{op}}$：若酰胺通过整体去折叠而交换，$\Delta G_{\mathrm{op}}$ 下降的斜率（$m$ 值）与整体 $\Delta G$ 相同；通过局部涨落交换的酰胺则斜率较小。若干酰胺共有同一斜率，就定义一个协同单元（折叠子）。

9. 在一个双自旋标记蛋白质的 DEER 实验中，偶极振荡的周期为 $0.95\,\mu\mathrm{s}$（取作 $1/\nu_\perp$）。估计自旋间的距离。迹线要持续多久才能确定分布的宽度？要测量 $8\,\mathrm{nm}$ 的距离需要改变什么？

   **答** $\nu_\perp = 1/0.95\,\mu\mathrm{s} = 1.05\,\mathrm{MHz}$；$r = (52.04/1.05)^{1/3}\,\mathrm{nm} = 3.7\,\mathrm{nm}$。平均距离需要约 $2\,\mu\mathrm{s}\times(3.7/5)^3 = 0.8\,\mu\mathrm{s}$，宽度约需其两倍，即 $1.6\,\mu\mathrm{s}$ 或更长。对 $8\,\mathrm{nm}$，$\nu_\perp = 0.10\,\mathrm{MHz}$，迹线须持续约 $8\,\mu\mathrm{s}$（确定宽度则 $16\,\mu\mathrm{s}$）：使蛋白质与溶剂（及甘油）氘代以延长相位记忆时间，在低温和适中浓度下工作以减小背景，并考虑在更高磁场下使用 Gd³⁺ 或三苯甲基标记。

10. （设计题）你想知道一个 30 kDa 的酶在没有底物时，是否会采样其复合物晶体结构中所见的闭合构象。提出一种 NMR 方法和一种 EPR 方法，说明各自测量什么及预期的特征。

    **答** NMR：对游离酶（最好氘代）在两个磁场下做 $^{15}\mathrm{N}$（或甲基 $^{13}\mathrm{C}$）的 CPMG 弛豫色散。如果游离酶在 μs–ms 时间尺度上与次要的闭合态交换，铰链与活性位点环中的残基会显示色散；整体拟合给出 $p_{\mathrm{B}}$、$k_{\mathrm{ex}}$ 与 $\lvert\Delta\omega\rvert$，检验的标准是 $\Delta\omega$ 是否与游离酶和酶–底物（或抑制剂）复合物之间的位移差相关。残余偶极耦合可检验结构域的平均取向，无模型 $S^2$ 则检验环的快速柔性。EPR：把自旋标记放在两个叶上、在开放与闭合晶体结构之间距离变化超过 $0.5\,\mathrm{nm}$ 的位置（用旋转异构体库预测），并在没有和有底物类似物时测量 DEER 分布。游离酶中的双峰分布，其次要成分位于闭合距离处并随配体增加，表明**构象选择**；单一距离在结合时发生移动，则表明**诱导契合**。对照：标记突变体的活性；冷冻可能使平衡移动，所以要与 NMR 的室温数据比较。
