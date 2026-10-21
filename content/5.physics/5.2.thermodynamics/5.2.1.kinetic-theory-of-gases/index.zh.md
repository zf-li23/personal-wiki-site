---
title: 温度与气体动理论
---

热学研究与温度有关的现象：宏观上，这些现象表现为物体的温度、压强、体积、相态的变化；微观上，它们来源于大量分子永不停息的无规则运动。研究热现象有两条互补的途径。热力学从少数几条宏观实验定律出发，用逻辑推理得到普遍而可靠的结论，不涉及物质的微观结构（[5.2.3](/5.2.3)、[5.2.4](/5.2.4)）；统计力学从分子的微观模型出发，用统计方法求出宏观量，能揭示热现象的本质，但结论受模型的限制。本章是统计方法的入门：先建立温度、平衡态等热学特有的概念，然后用 Newton 力学（[5.1](/5.1)）和概率论（[3.1](/3.1)）推出理想气体的压强、温度的微观意义、能量均分定理、Maxwell 速率分布与 Boltzmann 分布。下一章 [5.2.2](/5.2.2) 讨论偏离理想气体的真实气体与非平衡的输运过程；这里得到的 Boltzmann 分布还会在黑体辐射、激光与物理化学中反复出现。

## 1.1. 热力学系统、平衡态与温度

### 1.1.1. 热力学系统

**定义 1.1.1（热力学系统）** 由大量微观粒子（分子、原子等）组成、体积有限的宏观物体称为**热力学系统**，简称系统；系统以外、与系统相互作用的部分称为**外界**（环境）。按与外界的相互作用，系统分为：

- **孤立系统**：与外界既无能量交换，也无物质交换；
- **封闭系统**：与外界有能量交换，无物质交换；
- **绝热系统**：与外界只有做**功**形式的能量交换，没有热量交换；
- **开放系统**：与外界既有能量交换，又有物质交换。

宇宙这样体积无限的系统、只含少数粒子的系统都不是热力学系统：前者没有确定的边界与外界，后者谈不上统计规律。上述分类与物理化学（IUPAC）的用法一致。

### 1.1.2. 平衡态

**定义 1.1.2（平衡态）** 在外界条件不变的情况下，若系统内部没有宏观的粒子流与能量流，系统的宏观性质不随时间变化，则称系统处于**平衡态**。

与外界有相互作用的系统要保持平衡态，必须满足相应的平衡条件：

| 平衡条件 | 适用情形 | 平衡时的要求 |
|---|---|---|
| 力学平衡 | 系统与外界有力学作用（如活塞） | 内外压强相等 |
| 热平衡 | 系统与外界能交换热量（导热壁） | 内外温度相等 |
| 相平衡 | 系统中有不同的相共存 | 除力学平衡、热平衡外，各相之间没有净的物质转移 |
| 化学平衡 | 系统中有化学反应或不同组分的混合 | 没有净反应，各组分在空间上的分布不再改变 |

平衡态要与稳定态（steady state）区分：把一根金属杆的两端分别接到温度为 $T_1$、$T_2$（$T_1 \neq T_2$）的恒温热库上，经过足够长的时间，杆上各点的温度不再随时间变化，但杆中始终有热流，这是稳定态而不是平衡态；只有 $T_1 = T_2$ 时杆才处于平衡态。平衡态是一种动态平衡：宏观上静止，微观上分子仍在剧烈运动，宏观量只在平均值附近有微小的涨落。

### 1.1.3. 宏观量、微观量与物态方程

**定义 1.1.3** 表征系统整体性质、可以直接测量的物理量称为**宏观量**，如压强 $p$、体积 $V$、温度 $T$、质量、内能。宏观量分为两类：**广延量**与系统的大小成正比，把系统分成几部分时可以相加（$V$、质量、内能）；**强度量**与系统的大小无关，不能相加（$p$、$T$、密度）。描写单个微观粒子运动状态的物理量（分子的质量 $m$、**速度** $\boldsymbol{v}$、直径 $d$）称为**微观量**，一般只能间接测量。

统计力学的任务，就是把宏观量表示为微观量的统计平均值。

**定义 1.1.4（态参量）** 描写系统平衡态的一组相互独立的宏观量称为**态参量**（物态参量）；态参量之间的函数关系 $f(p, V, T) = 0$ 称为系统的**物态方程**。

对一定量的气体，一组态参量（如 $p, V$）唯一确定一个平衡态，物态方程再给出第三个量 $T$。

### 1.1.4. 热力学第零定律与温度

两个系统通过导热壁长时间接触后达到的共同平衡态称为热平衡。温度是热学特有的物理量，它的定义依赖下面的实验定律。

**定理 1.1.1（热力学第零定律）** 若系统 $A$ 与 $C$ 处于热平衡、$B$ 与 $C$ 处于热平衡，则 $A$ 与 $B$ 也处于热平衡（即使 $A$ 与 $B$ 没有接触）。

第零定律说明"处于热平衡"是一种等价关系（自反、对称由定义显然，第零定律给出传递性），因此所有系统按热平衡关系分成等价类，每个类可以用一个数标记。

**定义 1.1.5（温度）** 处于同一热平衡态的各系统共同具有的宏观性质称为**温度**：两个系统处于热平衡，当且仅当它们的温度相等。

第零定律也是温度计的原理：温度计 $C$ 先后与 $A$、$B$ 达到热平衡，示数相同就说明 $A$ 与 $B$ 温度相同。下一节将看到，温度在微观上是分子热运动剧烈程度的量度。

### 1.1.5. 温标

温度的数值表示方法称为温标。

1. 理想气体温标：一定量的气体在压强趋于零的极限下，$pV$ 只由温度决定。规定 $T \propto \lim_{p\to0} pV$，并取水的三相点为 $273.16\,\mathrm{K}$，得
   $$
   T = 273.16\,\mathrm{K} \times \lim_{p \to 0}\frac{pV}{(pV)_3},
   $$
   其中 $(pV)_3$ 是同一份气体在三相点的值。用低压 $^3\mathrm{He}$ 气体，这一温标可用到约 $0.5\,\mathrm{K}$。
2. 热力学温标（thermodynamic temperature scale）：不依赖任何测温物质及其测温属性的温标，由 Carnot 定理定义（[5.2.4](/5.2.4)），在理想气体温标适用的范围内与之一致。热力学温度 $T$ 的单位是开尔文（$\mathrm{K}$），是 SI 的基本单位之一。
3. 摄氏温标：$t/{}^\circ\mathrm{C} = T/\mathrm{K} - 273.15$。水的三相点约为 $0.01\,{}^\circ\mathrm{C}$，一个标准大气压下水的沸点约为 $100\,{}^\circ\mathrm{C}$。
4. 华氏温标（只在美国等地日常使用）：$t_{\mathrm{F}}/{}^\circ\mathrm{F} = \frac{9}{5}\,t/{}^\circ\mathrm{C} + 32$，例如 $100\,{}^\circ\mathrm{F} \approx 37.8\,{}^\circ\mathrm{C}$。

**注 1.1.1（2019 年的 SI）** 2019 年以前，开尔文定义为水三相点热力学温度的 $1/273.16$，三相点温度是精确的 $273.16\,\mathrm{K}$。自 2019 年 5 月起，开尔文改由固定 Boltzmann 常量的数值来定义：
$$
k_{\mathrm{B}} = 1.380\,649 \times 10^{-23}\,\mathrm{J\,K^{-1}}\quad(\text{exact}),
$$
即 $1\,\mathrm{K}$ 是使热运动能量 $k_{\mathrm{B}}T$ 改变 $1.380\,649 \times 10^{-23}\,\mathrm{J}$ 的温度变化。水的三相点从此成为测量值，仍约为 $273.16\,\mathrm{K}$（不确定度约 $0.1\,\mathrm{mK}$）。同时固定的还有 Avogadro 常量 $N_{\mathrm{A}} = 6.022\,140\,76 \times 10^{23}\,\mathrm{mol^{-1}}$，所以摩尔气体常量 $R = N_{\mathrm{A}}k_{\mathrm{B}} = 8.314\,462\,618\ldots\,\mathrm{J\,mol^{-1}\,K^{-1}}$ 也是精确值。

### 1.1.6. 理想气体物态方程

**定义 1.1.6（理想气体）** 在任何状态下都严格满足物态方程
$$
pV = nRT
$$
的气体称为**理想气体**，其中 $n$ 是物质的量。

各种实际气体在压强趋于零时都趋于理想气体。用分子数 $N = nN_{\mathrm{A}}$ 与分子数密度 $n_V = N/V$ 表示，物态方程又可写成
$$
pV = Nk_{\mathrm{B}}T, \qquad p = n_Vk_{\mathrm{B}}T.
\tag{1.1}
$$
这里的 Boltzmann 常量（Boltzmann constant）$k_{\mathrm{B}} = R/N_{\mathrm{A}}$ 是"每个分子的气体常量"，它把温度换算成单个分子的能量尺度：室温 $T = 300\,\mathrm{K}$ 时 $k_{\mathrm{B}}T \approx 4.14 \times 10^{-21}\,\mathrm{J} \approx 0.0259\,\mathrm{eV} \approx \frac{1}{40}\,\mathrm{eV}$。若气体的质量为 $m_{\mathrm{gas}}$、摩尔质量为 $M$，则 $n = m_{\mathrm{gas}}/M$。标准状况（$273.15\,\mathrm{K}$、$101.325\,\mathrm{kPa}$）下 $n_V \approx 2.69 \times 10^{25}\,\mathrm{m^{-3}}$（Loschmidt 常量）。

## 1.2. 理想气体的压强

### 1.2.1. 气体动理论的基本观点

气体动理论（分子运动论）的出发点是三条基本观点：宏观物体由大量分子、原子组成，分子之间有间隙；分子永不停息地做无规则运动，即热运动（thermal motion）；分子之间有相互作用力。

### 1.2.2. 理想气体的微观模型

力学假设（每个分子遵从的规律）：

1. 分子的线度远小于分子间的平均距离，分子可看作**质点**；
2. 除碰撞的瞬间外，分子之间、分子与器壁之间没有相互作用（忽略重力）；
3. 碰撞是完全弹性的；
4. 分子的运动遵从 Newton 力学。

统计假设（大量分子处于平衡态时）：

1. 无外场时，分子在容器中各处出现的概率相同，分子数密度处处相等：$n_V = \frac{\mathrm{d}N}{\mathrm{d}V} = \frac{N}{V}$；
2. 分子速度的方向在各方向上等概率（各向同性），因此
   $$
   \overline{v_x} = \overline{v_y} = \overline{v_z} = 0, \qquad \overline{v_x^2} = \overline{v_y^2} = \overline{v_z^2} = \frac{1}{3}\overline{v^2}.
   $$

统计规律有两个特点：一是稳定性，大量事件的平均结果是确定的；二是涨落（fluctuation），个别观测值在平均值附近起伏，统计对象越多，相对涨落越小（与 $1/\sqrt{N}$ 同阶）。**Galton 板**是一个直观的演示：单个小球落入哪一格是随机的，大量小球的分布却总接近同一条钟形曲线，这正是**二项分布**趋于**正态分布**的**中心极限定理**。

### 1.2.3. 压强公式

设容器中只有一种分子，分子质量为 $m$，总数为 $N$，体积为 $V$；把分子按速度分组，速度为 $\boldsymbol{v}_i$ 的分子数为 $N_i$，数密度为 $n_i = N_i/V$，$\sum_i n_i = n_V$。在器壁上取垂直于 $x$ 轴的面元 $\mathrm{d}A$（远大于分子的截面）。

1. 一个速度为 $\boldsymbol{v}_i$（$v_{ix} > 0$）的分子与 $\mathrm{d}A$ **弹性碰撞**一次，**动量**的 $x$ 分量改变 $-2mv_{ix}$，由**动量定理**，它给器壁的**冲量**为 $2mv_{ix}$。
2. 在 $\mathrm{d}t$ 内能碰到 $\mathrm{d}A$ 的这类分子，位于以 $\mathrm{d}A$ 为底、斜高沿 $\boldsymbol{v}_i$、厚度为 $v_{ix}\,\mathrm{d}t$ 的柱体内，共 $n_iv_{ix}\,\mathrm{d}t\,\mathrm{d}A$ 个，它们给器壁的冲量为 $\mathrm{d}I_i = 2n_imv_{ix}^2\,\mathrm{d}t\,\mathrm{d}A$。
3. 对 $v_{ix} > 0$ 的各组求和；由各向同性，$v_{ix} > 0$ 与 $v_{ix} < 0$ 的分子各占一半，所以
   $$
   \mathrm{d}I = \sum_{v_{ix}>0} 2n_imv_{ix}^2\,\mathrm{d}t\,\mathrm{d}A = \sum_i n_imv_{ix}^2\,\mathrm{d}t\,\mathrm{d}A.
   $$
4. 压强是单位面积受到的平均力：
   $$
   p = \frac{\mathrm{d}I}{\mathrm{d}t\,\mathrm{d}A} = m\sum_i n_iv_{ix}^2 = n_Vm\overline{v_x^2} = \frac{1}{3}n_Vm\overline{v^2}.
   $$

**公式 1.2.1（理想气体压强公式）** 记分子的平均平动**动能**为 $\bar\varepsilon_{\mathrm{t}} = \frac{1}{2}m\overline{v^2}$，则
$$
p = \frac{1}{3}n_Vm\overline{v^2} = \frac{2}{3}n_V\bar\varepsilon_{\mathrm{t}}.
\tag{1.2}
$$

压强是大量分子碰撞器壁的平均效果，对单个分子谈"压强"没有意义。推导中分子之间的碰撞没有出现：平衡态下它们不改变速度分布，只使分布保持各向同性。

## 1.3. 温度的统计意义

比较压强公式 (1.2) 与物态方程 (1.1) 得到

**公式 1.3.1** 理想气体分子的平均平动动能只由温度决定：
$$
\bar\varepsilon_{\mathrm{t}} = \frac{1}{2}m\overline{v^2} = \frac{3}{2}k_{\mathrm{B}}T.
\tag{1.3}
$$

这就是温度的统计意义：热力学温度是大量分子热运动平均平动动能的量度。温度与压强一样是统计概念，只对大量分子有意义。由式 (1.3)，分子的方均根速率（root-mean-square speed）为
$$
v_{\mathrm{rms}} = \sqrt{\overline{v^2}} = \sqrt{\frac{3k_{\mathrm{B}}T}{m}} = \sqrt{\frac{3RT}{M}} \propto \sqrt{T}.
$$

**例 1.3.1（数量级）** $T = 273\,\mathrm{K}$ 时，$\bar\varepsilon_{\mathrm{t}} = \frac{3}{2}k_{\mathrm{B}}T \approx 5.65 \times 10^{-21}\,\mathrm{J} \approx 3.53 \times 10^{-2}\,\mathrm{eV}$，与分子种类无关；$\ce{H2}$ 的 $v_{\mathrm{rms}} \approx 1.84 \times 10^3\,\mathrm{m\,s^{-1}}$，$\ce{O2}$ 的 $v_{\mathrm{rms}} \approx 461\,\mathrm{m\,s^{-1}}$，与声速同一数量级。化学键能为几个 $\mathrm{eV}$，远大于室温下的 $k_{\mathrm{B}}T$，所以常温下的分子碰撞不足以打断化学键。

## 1.4. 能量均分定理

### 1.4.1. 分子的自由度

分子不总能看作质点：双原子分子还会转动和振动。决定分子空间位置所需的独立坐标数就是分子的**自由度**，记作 $i = t + r + s$，其中 $t$、$r$、$s$ 分别是平动、转动、振动自由度。

| 分子 | 例子 | $t$ | $r$ | $s$ | $i$ |
|---|---|---|---|---|---|
| 单原子 | $\ce{He}$、$\ce{Ne}$、$\ce{Ar}$ | 3 | 0 | 0 | 3 |
| 双原子 | $\ce{H2}$、$\ce{O2}$、$\ce{CO}$ | 3 | 2 | 1 | 6 |
| 线形多原子（$N$ 个原子） | $\ce{CO2}$ | 3 | 2 | $3N-5$ | $3N$ |
| 非线形多原子（$N$ 个原子） | $\ce{H2O}$、$\ce{NH3}$ | 3 | 3 | $3N-6$ | $3N$ |

双原子分子的质心坐标 $(x, y, z)$ 给出 3 个平动自由度，轴的方向 $(\theta, \phi)$ 给出 2 个转动自由度（绕轴本身的转动不计，原子可看作质点），两原子间距 $l$ 的变化给出 1 个振动自由度。$N$ 个原子共有 $3N$ 个坐标；非线形分子作为**刚体**的**定点转动**需要 3 个 **Euler 角**，余下 $3N - 6$ 个是振动；线形分子只有 2 个转动自由度，振动自由度为 $3N - 5$。

### 1.4.2. 能量均分定理

由式 (1.3) 与各向同性，$\frac{1}{2}m\overline{v_x^2} = \frac{1}{2}m\overline{v_y^2} = \frac{1}{2}m\overline{v_z^2} = \frac{1}{2}k_{\mathrm{B}}T$：每个平动自由度平均分得 $\frac{1}{2}k_{\mathrm{B}}T$ 的动能。分子间的频繁碰撞使能量在平动、转动、振动之间不断交换，平衡时没有哪个自由度占优势，于是有

**定理 1.4.1（能量均分定理）** 在温度为 $T$ 的平衡态下，按经典统计，分子能量中每一个独立的平方项（动能 $\frac{1}{2}mv_x^2$、$\frac{1}{2}J\omega^2$，或简谐**势能** $\frac{1}{2}kx^2$）的平均值都等于 $\frac{1}{2}k_{\mathrm{B}}T$。

一个振动自由度既有振动动能又有振动势能，两个平方项共贡献 $k_{\mathrm{B}}T$。因此一个分子的平均能量为
$$
\bar\varepsilon = \bar\varepsilon_{\mathrm{t}} + \bar\varepsilon_{\mathrm{r}} + \bar\varepsilon_{\mathrm{v}} = \frac{1}{2}(t + r + 2s)\,k_{\mathrm{B}}T.
$$
定理的证明要用 Boltzmann 分布，见注 1.7.1。它适用于气体、液体与固体中的经典自由度，例如固体中每个原子有 3 个振动自由度，平均能量 $3k_{\mathrm{B}}T$，给出摩尔热容 $3R$（Dulong–Petit 定律）。

能量均分是经典理论的结论。量子力学中转动与振动的能量是分立的：当 $k_{\mathrm{B}}T$ 远小于相邻能级的间隔时，这个自由度几乎不能被激发，称为被"冻结"。振动能级间隔通常对应 $10^3\,\mathrm{K}$ 量级的温度（$\ce{H2}$ 约 $6000\,\mathrm{K}$，$\ce{Cl2}$ 约 $800\,\mathrm{K}$），所以常温下多数分子的振动被冻结，可看作刚性分子（$s = 0$），平均能量为 $\bar\varepsilon = \frac{t + r}{2}k_{\mathrm{B}}T$：单原子分子 $\frac{3}{2}k_{\mathrm{B}}T$，双原子与线形分子 $\frac{5}{2}k_{\mathrm{B}}T$，非线形多原子分子 $3k_{\mathrm{B}}T$。
温度更低时转动也会被冻结（$\ce{H2}$ 在几十开尔文以下）。热容随温度的这种台阶式变化是经典物理无法解释、而量子化能级能够解释的现象，见 [5.2.3](/5.2.3)。

### 1.4.3. 理想气体的内能

**定义 1.4.1（内能）** 系统中所有分子热运动的能量（平动、转动、振动的动能与分子内的振动势能）与分子之间相互作用势能的总和，称为系统的**内能**，记作 $U$。内能不包括系统整体的**机械能**（质心运动的动能、系统在外场中的势能）。

分子热运动的能量由温度决定，分子间的势能由分子间距、即体积决定，所以一般 $U = U(T, V)$。理想气体忽略分子间的相互作用，内能只是温度的函数：

**公式 1.4.1（理想气体的内能）** 物质的量为 $n$ 的理想气体，
$$
U = N\bar\varepsilon = \frac{t + r + 2s}{2}\,nRT.
\tag{1.4}
$$
对刚性分子 $U = \frac{i}{2}nRT$，$i = t + r$。

内能的零点可以任意选取，物理上有意义的是内能的变化。热力学中内能将由绝热功重新定义（[5.2.3](/5.2.3)），两种定义一致。

## 1.5. Maxwell 速率分布律

知道方均根速率还不足以描述气体：碰撞、泄流、化学反应的**速率**都依赖于有多少分子具有多大的速率。分子速率的统计分布用分布函数描述；由分布函数可以求出任何微观量的统计平均值，进而求出宏观量。

### 1.5.1. 速率分布函数

把速率分成小区间，第 $i$ 个区间 $[v_i, v_i + \Delta v_i)$ 中有 $N_i$ 个分子：这种分立的描写依赖于区间的划分，不便于表达统计规律。设速率在 $[v, v + \mathrm{d}v)$ 内的分子数为 $\mathrm{d}N_v$，它与总数 $N$ 和区间长度 $\mathrm{d}v$ 都成正比，比例系数依赖于 $v$。

**定义 1.5.1（速率分布函数）** 函数
$$
f(v) = \frac{\mathrm{d}N_v}{N\,\mathrm{d}v}
$$
称为分子的**速率分布函数**：$f(v)$ 是速率在 $v$ 附近单位速率区间内的分子数占总分子数的比例。它满足归一化条件
$$
\int_0^{\infty} f(v)\,\mathrm{d}v = 1.
$$

对单个分子而言，$f(v)$ 就是它的速率（一个随机变量）的**概率密度**：$f(v)\,\mathrm{d}v$ 是分子速率落在 $[v, v + \mathrm{d}v)$ 内的概率，曲线 $f(v)$ 下 $[v_1, v_2]$ 上的面积是速率在这个区间内的分子所占的比例。微观量 $\phi(v)$ 对全体分子的平均值就是它的**数学期望**：
$$
\overline{\phi(v)} = \frac{\int \phi(v)\,\mathrm{d}N_v}{N} = \int_0^{\infty}\phi(v)f(v)\,\mathrm{d}v.
$$
物理文献把 $f(v)$ 叫作"分布函数"，在概率论的术语中它是密度，而概率论的分布函数指累积分布函数 $\int_0^v f(u)\,\mathrm{d}u$。

### 1.5.2. Maxwell 速率分布

**定理 1.5.1（Maxwell 速率分布）** 分子质量为 $m$ 的理想气体在温度为 $T$ 的平衡态下（无外场），分子的速率分布函数为
$$
f(v) = 4\pi\left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{3/2} v^2\,\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}, \qquad v \ge 0.
\tag{1.5}
$$

它由速度分布推出，见 §1.5.4。分布由两个因子竞争决定：$v^2$ 来自速度空间中半径为 $v$ 的球壳的面积，速率越大，可取的速度方向"越多"；$\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}$ 抑制高能量的分子。所以 $f(v)$ 从零开始上升，经过一个峰后迅速衰减，并有一条长尾。

![Maxwell speed distribution: N2 at three temperatures (left) and different gases at 300 K (right)](./plots/maxwell-speed-distribution.py)

温度升高时，峰向右移且变低（曲线下面积恒为 1），速率大的分子比例增加，热运动更剧烈；温度一定时，分子质量越大，峰越靠左、越高。

### 1.5.3. 三种特征速率

**定义 1.5.2** 使 $f(v)$ 取极大值的速率 $v_{\mathrm{p}}$ 称为**最概然速率**；速率的平均值 $\bar v = \int_0^\infty vf(v)\,\mathrm{d}v$ 称为**平均速率**。

**公式 1.5.1** 由式 (1.5)，令 $f'(v_{\mathrm{p}}) = 0$，并用 **Gamma 函数**（或 **Gauss 积分**）计算各阶矩，得
$$
v_{\mathrm{p}} = \sqrt{\frac{2k_{\mathrm{B}}T}{m}} = \sqrt{\frac{2RT}{M}}, \qquad
\bar v = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi m}} = \sqrt{\frac{8RT}{\pi M}}, \qquad
v_{\mathrm{rms}} = \sqrt{\frac{3k_{\mathrm{B}}T}{m}} = \sqrt{\frac{3RT}{M}},
$$
$$
v_{\mathrm{p}} : \bar v : v_{\mathrm{rms}} = \sqrt{2} : \sqrt{8/\pi} : \sqrt{3} \approx 1.41 : 1.60 : 1.73,
$$
且峰值 $f(v_{\mathrm{p}}) = \sqrt{\frac{8m}{\pi k_{\mathrm{B}}T}}\,\mathrm{e}^{-1} \propto \sqrt{m/T}$。

由分布律算出的 $v_{\mathrm{rms}}$ 与 §1.3 中由压强公式得到的结果相同，这是理论自洽的一个检验。三种速率各有用途：讨论速率分布时用 $v_{\mathrm{p}}$，讨论碰撞与泄流时用 $\bar v$，讨论平均平动动能时用 $v_{\mathrm{rms}}$。

用约化速率 $u = v/v_{\mathrm{p}}$ 作变量，分布律化为与气体种类和温度无关的形式
$$
\frac{\mathrm{d}N_v}{N} = \varphi(u)\,\mathrm{d}u, \qquad \varphi(u) = \frac{4}{\sqrt{\pi}}\,u^2\mathrm{e}^{-u^2}.
$$

**例 1.5.1** 氧气在 $T = 300\,\mathrm{K}$ 时 $v_{\mathrm{p}} \approx 395\,\mathrm{m\,s^{-1}}$。求速率在 $790$–$800\,\mathrm{m\,s^{-1}}$ 之间的分子所占的比例。

解：$u = 790/395 = 2$，$\Delta u = 10/395$，区间很窄，
$$
\frac{\Delta N}{N} \approx \frac{4}{\sqrt{\pi}}\,u^2\mathrm{e}^{-u^2}\,\Delta u = \frac{4}{\sqrt{\pi}} \times 4\,\mathrm{e}^{-4} \times \frac{10}{395} \approx 4.2 \times 10^{-3}.
$$
（在区间上精确积分得 $4.0 \times 10^{-3}$，差别来自 $f$ 在区间内的变化。）速率为最概然速率两倍附近的分子仍有可观的比例，这条长尾决定了化学反应等"需要大能量"的过程的速率。

**例 1.5.2** 设某假想气体的速率分布函数为 $f(v) = av^2$（$0 \le v \le v_0$），$f(v) = 0$（$v > v_0$）。求：(1) $a$ 与 $v_0$ 的关系；(2) 平均速率；(3) 速率在 $0$–$v_0/2$ 之间的分子的平均速率。

解：(1) 由归一化 $\int_0^{v_0} av^2\,\mathrm{d}v = \frac{1}{3}av_0^3 = 1$，$a = 3/v_0^3$。(2) $\bar v = \int_0^{v_0} v \cdot av^2\,\mathrm{d}v = \frac{a}{4}v_0^4 = \frac{3}{4}v_0$。(3) 部分分子的平均速率要除以这部分分子所占的比例，而不是直接算 $\int_0^{v_0/2} vf(v)\,\mathrm{d}v$：
$$
\bar v' = \frac{\int_0^{v_0/2} vf(v)\,\mathrm{d}v}{\int_0^{v_0/2} f(v)\,\mathrm{d}v} = \frac{\frac{a}{4}(v_0/2)^4}{\frac{a}{3}(v_0/2)^3} = \frac{3}{8}v_0.
$$
这就是概率论中的**条件期望** $\mathbb{E}[v \mid v \le v_0/2]$。

### 1.5.4. Maxwell 速度分布

速率分布不区分方向。在以 $v_x, v_y, v_z$ 为坐标的速度空间中，设速度落在 $\boldsymbol{v}$ 附近体积元 $\mathrm{d}^3v = \mathrm{d}v_x\,\mathrm{d}v_y\,\mathrm{d}v_z$ 内的分子数为 $\mathrm{d}N_{\boldsymbol{v}}$，速度分布函数 $F(\boldsymbol{v}) = \frac{\mathrm{d}N_{\boldsymbol{v}}}{N\,\mathrm{d}^3v}$ 是速度矢量的联合概率密度。

**定理 1.5.2（Maxwell 速度分布）** 平衡态下理想气体分子的速度分布函数为
$$
F(\boldsymbol{v}) = \left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{3/2}\mathrm{e}^{-m(v_x^2 + v_y^2 + v_z^2)/(2k_{\mathrm{B}}T)} = g(v_x)\,g(v_y)\,g(v_z),
\qquad g(v_x) = \left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{1/2}\mathrm{e}^{-mv_x^2/(2k_{\mathrm{B}}T)}.
$$

用概率论的语言：三个速度分量相互独立，各自服从**正态分布** $\mathcal{N}(0, k_{\mathrm{B}}T/m)$。Maxwell（1860）的原始论证正是：若分布各向同性（$F$ 只依赖 $v^2$），且三个分量相互独立（$F$ 是三个同一函数之积），则函数方程 $g(v_x)g(v_y)g(v_z) = \Phi(v_x^2 + v_y^2 + v_z^2)$ 的可积解只有 Gauss 函数；常数由 $\overline{v_x^2} = k_{\mathrm{B}}T/m$ 确定。更一般的推导由 Boltzmann 分布给出（§1.7.3）。

由速度分布到速率分布：速率在 $[v, v + \mathrm{d}v)$ 而方向任意的分子，其速度矢量的端点位于速度空间中半径为 $v$、厚度为 $\mathrm{d}v$ 的球壳内，球壳体积为 $4\pi v^2\,\mathrm{d}v$，$F$ 在其上为常数，于是
$$
f(v)\,\mathrm{d}v = F(\boldsymbol{v})\cdot 4\pi v^2\,\mathrm{d}v,
$$
这就是式 (1.5)。换一种说法：$mv^2/(k_{\mathrm{B}}T)$ 是三个独立标准正态变量的平方和，服从**卡方分布** $\chi^2_3$；二维气体（如吸附在表面上的分子）的速率则服从 **Rayleigh 分布**。分子平动动能 $\varepsilon = \frac{1}{2}mv^2$ 的概率密度为 $\frac{2}{\sqrt{\pi}}(k_{\mathrm{B}}T)^{-3/2}\varepsilon^{1/2}\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}$，即 $\Gamma(\frac{3}{2}, 1/(k_{\mathrm{B}}T))$ 分布，其均值 $\frac{3}{2}k_{\mathrm{B}}T$ 与式 (1.3) 一致。

## 1.6. Maxwell 速率分布的实验验证

### 1.6.1. Miller–Kusch 实验

1955 年 Miller 与 Kusch 用分子束精确检验了 Maxwell 分布。炉中的钾（或铊）蒸气经小孔逸出，形成分子束，射向一个以**角速度** $\omega$ 旋转的长圆柱。圆柱长 $L$，表面刻有螺旋形细槽，槽的入口与出口错开角度 $\phi$。分子在槽中飞行时间 $L/v$ 内圆柱恰好转过 $\phi$，才能穿过细槽到达检测器，所以选出的速率为
$$
v = \frac{\omega L}{\phi}, \qquad \Delta v = \frac{\omega L}{\phi^2}\,\Delta\phi = \frac{v}{\phi}\,\Delta\phi,
$$
其中 $\Delta\phi$ 是细槽宽度对应的角度。改变 $\omega$，测量检测器上的强度，就得到分子束的速率分布。

注意检测器上的分布不是 $f(v)$ 本身：

1. 从小孔逸出的分子数正比于 $vf(v)$（速率大的分子更频繁地撞到小孔，见下面的碰壁数），所以束中速率分布 $\propto v^3\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}$；
2. 选择器透过的速率带宽 $\Delta v \propto v$，又多出一个因子 $v$。

所以检测到的强度 $\propto v^4\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}$。实验数据与这个预言在百分之几以内吻合，是 Maxwell 分布最直接的验证。

![Speed distributions in the gas, in an effusive beam and at the detector of a Miller–Kusch selector, in reduced speed](./plots/miller-kusch.py)

### 1.6.2. 分子碰壁数

**定义 1.6.1** 单位时间内碰撞单位面积器壁的分子数称为**碰壁数** $\Gamma$。

取垂直于 $x$ 轴的面元 $\mathrm{d}A$。速度在 $\boldsymbol{v}$ 附近 $\mathrm{d}^3v$ 内、$v_x > 0$ 的分子，在 $\mathrm{d}t$ 内能碰到 $\mathrm{d}A$ 的，位于体积为 $v_x\,\mathrm{d}t\,\mathrm{d}A$ 的斜柱内，共 $n_Vv_x\,\mathrm{d}t\,\mathrm{d}A\,F(\boldsymbol{v})\,\mathrm{d}^3v$ 个。对 $v_y, v_z$ 积分（各得 1），对 $v_x > 0$ 积分：

**公式 1.6.1**
$$
\Gamma = n_V\int_0^{\infty} v_x\,g(v_x)\,\mathrm{d}v_x = n_V\sqrt{\frac{k_{\mathrm{B}}T}{2\pi m}} = \frac{1}{4}n_V\bar v.
$$

**例 1.6.1（泄流）** 容积为 $V$ 的容器内装有温度恒为 $T$ 的气体，初始压强为 $p_0$，器壁上有面积为 $\Delta A$ 的小孔通向真空（或压强远小于 $p_0$ 的外界）。小孔远小于分子的平均自由程（[5.2.2](/5.2.2)），分子逐个从孔中"泄出"而不形成宏观气流。求压强降为 $p_0/2$ 所需的时间。

解：设 $t$ 时刻容器内有 $N$ 个分子，则 $\mathrm{d}N = -\Gamma\,\Delta A\,\mathrm{d}t = -\frac{\bar v\,\Delta A}{4V}N\,\mathrm{d}t$。$T$ 不变时 $p = Nk_{\mathrm{B}}T/V \propto N$，所以
$$
\frac{\mathrm{d}p}{\mathrm{d}t} = -\frac{\bar v\,\Delta A}{4V}\,p, \qquad p(t) = p_0\,\mathrm{e}^{-t/\tau},\quad \tau = \frac{4V}{\bar v\,\Delta A},
$$
这是一阶**线性微分方程**的指数衰减解。压强减半的时间 $\Delta t = \tau\ln 2$。对氧气，$T = 300\,\mathrm{K}$ 时 $\bar v \approx 445\,\mathrm{m\,s^{-1}}$；取 $V = 1\,\mathrm{L}$、$\Delta A = 0.1\,\mathrm{mm^2}$，得 $\Delta t \approx 62\,\mathrm{s}$。

### 1.6.3. 扩散法分离同位素

两种同位素分子的混合气体通过多孔膜泄流时，碰壁数 $\Gamma \propto n_V\bar v \propto n_V/\sqrt{m}$，轻的分子透过得多。设两种分子的数密度为 $n_1, n_2$，质量 $m_1 < m_2$，一次泄流后丰度比的提高倍数（单级分离系数）为
$$
\alpha = \frac{(n_1/n_2)_{\mathrm{after}}}{(n_1/n_2)_{\mathrm{before}}} = \frac{\bar v_1}{\bar v_2} = \sqrt{\frac{m_2}{m_1}}.
$$

**例 1.6.2（铀浓缩）** 天然铀中 $^{235}\mathrm{U}$ 的丰度为 $0.71\%$，核电站燃料要求约 $3\%$。用 $\ce{UF6}$ 气体泄流（氟只有一种稳定同位素 $^{19}\mathrm{F}$，两种分子的质量差只来自铀），
$$
\alpha = \sqrt{\frac{238 + 6 \times 19}{235 + 6 \times 19}} = \sqrt{\frac{352}{349}} \approx 1.0043.
$$
丰度比要从 $0.71/99.29 = 7.15 \times 10^{-3}$ 提高到 $3/97 = 3.09 \times 10^{-2}$，即提高 $4.33$ 倍，所需级数 $N_{\mathrm{s}}$ 满足 $\alpha^{N_{\mathrm{s}}} = 4.33$，
$$
N_{\mathrm{s}} = \frac{\ln 4.33}{\ln 1.0043} \approx 3.4 \times 10^2.
$$
要达到武器级（约 $90\%$）则需约 $1.7 \times 10^3$ 级。这是理想的估计，实际的单级分离系数更接近 1，所需级数更多。气体扩散厂耗电巨大，现已全部关闭；现行的铀浓缩以气体离心法为主，其原理见例 1.7.1。

## 1.7. Boltzmann 分布

### 1.7.1. 重力场中分子数密度的分布

热运动使分子趋于均匀分布，重力使分子落向底部，两者竞争，平衡时形成一定的分布。设大气温度 $T$ 处处相同，分子质量为 $m$。取高度 $z$ 到 $z + \mathrm{d}z$、底面积为 $S$ 的薄层气体，力学平衡要求 $(p + \mathrm{d}p)S + mgn_VS\,\mathrm{d}z = pS$，即 $\mathrm{d}p = -mgn_V\,\mathrm{d}z$。由 $p = n_Vk_{\mathrm{B}}T$，
$$
\frac{\mathrm{d}n_V}{n_V} = -\frac{mg}{k_{\mathrm{B}}T}\,\mathrm{d}z.
$$

**公式 1.7.1（恒温气压公式）** 设 $z = 0$ 处的数密度与压强为 $n_0$、$p_0$，则
$$
n_V(z) = n_0\,\mathrm{e}^{-mgz/(k_{\mathrm{B}}T)}, \qquad p(z) = p_0\,\mathrm{e}^{-mgz/(k_{\mathrm{B}}T)} = p_0\,\mathrm{e}^{-Mgz/(RT)}.
$$

特征高度 $H = RT/(Mg)$ 对空气（$M \approx 29\,\mathrm{g\,mol^{-1}}$、$T \approx 288\,\mathrm{K}$）约为 $8.4\,\mathrm{km}$：每升高 $8.4\,\mathrm{km}$，气压降为 $1/\mathrm{e}$。由此可以从气压估计高度（高度计的原理）；实际大气温度随高度变化，公式只是近似。

### 1.7.2. Boltzmann 分布律

重力势能 $mgz$ 出现在指数上不是偶然的。设分子处于任意保守外场中，势能为 $\varepsilon_{\mathrm{p}}(\boldsymbol{r})$，则有

**定理 1.7.1（Boltzmann 分布）** 在温度为 $T$ 的平衡态下，位于 $\boldsymbol{r}$ 附近体积元 $\mathrm{d}^3r = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ 内的分子数为
$$
\mathrm{d}N_{\boldsymbol{r}} = n_0\,\mathrm{e}^{-\varepsilon_{\mathrm{p}}(\boldsymbol{r})/(k_{\mathrm{B}}T)}\,\mathrm{d}^3r,
$$
其中 $n_0$ 是 $\varepsilon_{\mathrm{p}} = 0$ 处的分子数密度。更一般地，平衡态下系统处于能量为 $\varepsilon$ 的一个微观状态的概率正比于 $\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}$。

因子 $\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}$ 称为 Boltzmann 因子（Boltzmann factor）。它说明能量越高的状态越难被占据，而"高"与"低"的标尺是 $k_{\mathrm{B}}T$：$\varepsilon \ll k_{\mathrm{B}}T$ 的状态几乎与基态一样容易占据，$\varepsilon \gg k_{\mathrm{B}}T$ 的状态几乎是空的。把各状态的 Boltzmann 因子求和得到配分函数 $Z = \sum_s \mathrm{e}^{-\varepsilon_s/(k_{\mathrm{B}}T)}$，所有热力学量都可以由它求出；用 Monte Carlo 方法从 Boltzmann 分布中抽样正是 Metropolis 算法最初的用途（[3.5.9](/3.5.9)）。

**例 1.7.1（旋转容器与离心分离）** 装有气体的圆筒以角速度 $\omega$ 绕竖直轴匀速转动。在随圆筒转动的**参考系**中，分子受**惯性离心力** $m\omega^2r$，相应的势能为 $\varepsilon_{\mathrm{p}}(r) = -\int_0^r m\omega^2r'\,\mathrm{d}r' = -\frac{1}{2}m\omega^2r^2$（取轴上为零）。由 Boltzmann 分布，
$$
n_V(r) = n_0\,\mathrm{e}^{m\omega^2r^2/(2k_{\mathrm{B}}T)},
$$
分子向筒壁聚集。两种同位素分子在半径 $r$ 与轴上的丰度比之比为 $\mathrm{e}^{(m_2 - m_1)\omega^2r^2/(2k_{\mathrm{B}}T)}$，只依赖质量差 $m_2 - m_1$，而泄流法的分离系数依赖质量比的平方根。对 $\ce{UF6}$，筒壁线速度 $\omega r$ 达到每秒数百米时，单级分离系数可达 1.1 以上，远大于泄流法的 1.0043，这就是气体离心法取代扩散法的原因。

### 1.7.3. Maxwell–Boltzmann 分布

同时考虑位置与速度：位于 $\boldsymbol{r}$ 附近 $\mathrm{d}^3r$ 内、速度在 $\boldsymbol{v}$ 附近 $\mathrm{d}^3v$ 内的分子数为
$$
\mathrm{d}N = n_0\left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{3/2}\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}\,\mathrm{d}^3r\,\mathrm{d}^3v, \qquad \varepsilon = \frac{1}{2}mv^2 + \varepsilon_{\mathrm{p}}(\boldsymbol{r}),
$$
称为 Maxwell–Boltzmann 分布。它是 Boltzmann 分布对分子总能量（动能加势能）的应用：对 $\boldsymbol{r}$ 积分就回到 Maxwell 速度分布，对 $\boldsymbol{v}$ 积分就回到定理 1.7.1。分子的位置分布与速度分布相互独立，所以重力场中各高度的气体温度相同、速度分布相同，只是数密度不同。

**注 1.7.1（能量均分定理的证明）** 设分子能量中有一项 $a\xi^2$（$\xi$ 是某个速度分量、角速度或振动坐标，$a > 0$），且它与其余各项相加。按 Boltzmann 分布，$\xi$ 的概率密度正比于 $\mathrm{e}^{-a\xi^2/(k_{\mathrm{B}}T)}$，即**正态分布** $\mathcal{N}(0, k_{\mathrm{B}}T/(2a))$，于是
$$
\overline{a\xi^2} = a \cdot \frac{k_{\mathrm{B}}T}{2a} = \frac{1}{2}k_{\mathrm{B}}T,
$$
与 $a$ 无关。这就是**能量均分定理**。它依赖于两点：能量是 $\xi$ 的二次函数，且 $\xi$ 可以连续取值。后一点在量子力学中不成立，于是有了自由度的"冻结"。

**例 1.7.2（原子能级的布居）** 氢原子的基态能量 $E_1 = -13.6\,\mathrm{eV}$，第一激发态 $E_2 = E_1/4 = -3.4\,\mathrm{eV}$，$\Delta E = 10.2\,\mathrm{eV}$。室温 $T = 300\,\mathrm{K}$ 下 $k_{\mathrm{B}}T \approx 0.0259\,\mathrm{eV}$，两能级上原子数之比（每个状态）为
$$
\frac{N_2}{N_1} = \mathrm{e}^{-\Delta E/(k_{\mathrm{B}}T)} \approx \mathrm{e}^{-394} \approx 10^{-171}.
$$
第一激发态有 4 个轨道状态而基态只有 1 个（不计自旋），能级的总布居还要乘以简并度之比 4，结论不变：室温下处于激发态的原子微乎其微，几乎全部处于基态。要使激发态的原子数多于基态（粒子数反转，激光的条件），必须用外界的能量把系统推离平衡态。

## 思考题

1. 温度一定时，分子质量 $m_2 > m_1$ 的两种气体的 Maxwell 速率分布曲线有什么不同？
   提示：$v_{\mathrm{p}} \propto 1/\sqrt{m}$，峰左移；$f(v_{\mathrm{p}}) \propto \sqrt{m}$，峰变高；曲线下的面积都是 1。
2. 室温下空气中 $\ce{N2}$ 与 $\ce{O2}$ 分子的平均平动动能哪个大？方均根速率呢？
   提示：平均平动动能只由温度决定，两者相同；$v_{\mathrm{rms}} \propto 1/\sqrt{M}$，$\ce{N2}$ 的稍大。

## 小结

| 内容 | 结论 |
|---|---|
| 物态方程 | $pV = nRT$，$p = n_Vk_{\mathrm{B}}T$，$R = N_{\mathrm{A}}k_{\mathrm{B}}$ |
| 压强公式 | $p = \frac{1}{3}n_Vm\overline{v^2} = \frac{2}{3}n_V\bar\varepsilon_{\mathrm{t}}$ |
| 温度的统计意义 | $\bar\varepsilon_{\mathrm{t}} = \frac{3}{2}k_{\mathrm{B}}T$ |
| 能量均分 | 每个平方项 $\frac{1}{2}k_{\mathrm{B}}T$；$\bar\varepsilon = \frac{1}{2}(t + r + 2s)k_{\mathrm{B}}T$；理想气体 $U = \frac{t + r + 2s}{2}nRT$ |
| Maxwell 速率分布 | $f(v) = 4\pi\left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{3/2}v^2\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}$；速度分量独立且服从 $\mathcal{N}(0, k_{\mathrm{B}}T/m)$ |
| 特征速率 | $v_{\mathrm{p}} = \sqrt{2k_{\mathrm{B}}T/m}$，$\bar v = \sqrt{8k_{\mathrm{B}}T/(\pi m)}$，$v_{\mathrm{rms}} = \sqrt{3k_{\mathrm{B}}T/m}$ |
| 碰壁数 | $\Gamma = \frac{1}{4}n_V\bar v$ |
| Boltzmann 分布 | $\mathrm{d}N_{\boldsymbol{r}} = n_0\mathrm{e}^{-\varepsilon_{\mathrm{p}}/(k_{\mathrm{B}}T)}\mathrm{d}^3r$；恒温气压公式 $p = p_0\mathrm{e}^{-Mgz/(RT)}$ |
