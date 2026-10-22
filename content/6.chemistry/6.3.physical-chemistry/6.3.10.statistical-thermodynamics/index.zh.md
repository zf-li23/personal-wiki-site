---
title: 统计热力学基础
description: 宏观态与微观态，定域子系、离域子系与独立子系；一种分布的微观状态数、Stirling 公式与最概然分布的主导地位；用 Lagrange 乘子法推导 Boltzmann 分布并确定 β = 1/(kT)；分子配分函数的概率意义、平均能量与能量涨落；系统配分函数与 U、S、A、G、H、p、C_V 的关系，能量零点的选择；热、功、熵与第三定律的统计意义。
---

前面九章的化学热力学从几条经验定律出发，只用 $T$、$p$、$V$、$U$、$S$ 这些宏观量讨论能量转换、方向与限度，完全不涉及物质由什么组成（[6.3.1](/6.3.1)）。这样得到的结论普遍可靠，代价是一切物性数据——热容、标准摩尔熵、平衡常数——都只能靠测量。统计热力学走相反的路：把宏观系统看作大量分子的集合，从分子的能级出发，用概率方法求出宏观性质的统计平均。它回答了热力学回答不了的问题：理想气体的 $U$ 为什么只与 $T$ 有关，双原子气体的 $C_{V,\mathrm{m}}$ 为什么在常温下是 $\frac{5}{2}R$，熵的微观意义是什么，以及怎样只用光谱数据算出标准摩尔熵和平衡常数。

物理中已经用 **Boltzmann 分布**（[5.2.1](/5.2.1#sec-1.7)）讨论过气体分子在外场中的分布，用**微观态**计数与 **Boltzmann 熵公式**（[5.2.4](/5.2.4#sec-4.7)）解释过第二定律的统计意义。本章把这些想法系统化：先学会数一种能量分布包含多少微观态（10.2），再用 Lagrange 乘子法求出微观态最多的分布，即能级形式的 Boltzmann 分布（10.3），由此引出统计热力学的核心量**配分函数**，并把全部热力学函数用它表示（10.4）。分子的平动、转动、振动等配分函数的具体计算，以及由它们求理想气体的热容、熵与平衡常数，在下一章 [6.3.11](/6.3.11)。本章用到的分子能级来自量子物理：势箱中的粒子与谐振子（[5.5.3](/5.5.3)），**简并**与全同粒子（[5.5.4](/5.5.4)），分子的转动与振动能级（[5.5.5](/5.5.5#sec-5.3)）；数学上用到排列组合与**多项分布**（[3.1.6](/3.1.6)）和条件极值（[2.2.11](/2.2.11#sec-11.6)）。

## 10.1. 基本概念

### 10.1.1. 宏观态与微观态

只由实验可测的宏观性质（$N$、$V$、$U$、$T$、$p$ 等）描述的系统状态是**宏观态**，例如 $\{N, V, U\}$ 给定的孤立系统，或 $\{N, V, T\}$ 给定的与热源接触的封闭系统。把系统中每个粒子的状态都说清楚时，系统所处的状态是**微观态**（[5.2.4 定义 4.7.1](/5.2.4#def-4.7.1)）。在量子力学中，粒子的能量只能取分立的能级 $\varepsilon_0 < \varepsilon_1 < \varepsilon_2 < \cdots$，指明每个粒子处于哪个量子态，就确定了一个微观态。

宏观上静止的平衡态，微观上瞬息万变：分子不停地碰撞，在能级之间跃迁，在同一能级的不同量子态之间转换。测得的宏观量是微观量对时间的平均。统计热力学的基本做法是用对微观态的平均代替时间平均，从而把"大量粒子的力学"变成"概率论"。

统计方法有几种分类方式：按描述单个粒子的方式分为经典统计与量子统计；按系统是否平衡分为平衡态统计与非平衡态统计；按处理方法分为把系统看作分子集合的分子统计（Boltzmann 的方法）与 Gibbs 的系综方法。量子统计按粒子的类型又分为 Bose–Einstein 统计与 Fermi–Dirac 统计（[5.5.4](/5.5.4#sec-4.3.3)）。本章讲 Boltzmann 统计：它是量子统计在粒子数远少于可占据的量子态数时的极限（10.2.3），适用于常温常压下的一切气体和许多其他系统。

### 10.1.2. 统计系统的分类

**定义 10.1.1** 粒子可以区分的系统称为**定域子系**（可别粒子系统）；粒子不可区分的系统称为**离域子系**（等同粒子系统）。

微观粒子都是**全同粒子**（[5.5.4 定义 4.3.1](/5.5.4#def-4.3.1)），原则上不能区分。但在晶体中，每个原子被束缚在自己的格点附近振动，可以用格点的位置给它"编号"：交换两个格点上的原子，系统的状态改变了。所以晶体是定域子系。气体和液体中的分子在整个容器中运动，无法编号，是离域子系。

**定义 10.1.2** 粒子之间的相互作用可以忽略，系统的能量等于各粒子能量之和 $U = \sum_{i} N_i\varepsilon_i$ 的系统称为**独立子系**（近独立粒子系统）；粒子间相互作用不能忽略，$U = \sum_{i} N_i\varepsilon_i + U_{\mathrm{p}}$（$U_{\mathrm{p}}$ 为粒子间的势能）的系统称为**相依子系**。

**理想气体**是独立的离域子系。实际气体、液体与真实晶体是相依子系；但晶体的晶格振动可以分解为 $3N$ 个相互独立的振动模式（Einstein 与 Debye 模型），在这个意义下可以当作独立的定域子系处理。本章与下一章只讨论（近）独立子系。

### 10.1.3. 能级与简并度

具有相同能量的粒子可以处在不同的量子态上。一个能级包含的量子态数称为该能级的**简并度**（统计权重），记作 $g_i$。

**例 10.1.1（三维平动子）** 质量为 $m$ 的粒子在边长为 $a$、体积 $V = a^3$ 的立方箱中运动。由一维势箱的能级（[5.5.3](/5.5.3#sec-3.2.2)，式 (3.6)）与三个方向的分离变量，

$$
\varepsilon_{\mathrm{t}} = \frac{h^2}{8mV^{2/3}}\left(n_x^2 + n_y^2 + n_z^2\right), \qquad n_x, n_y, n_z = 1, 2, 3, \dots
\tag{10.1}
$$
以 $\varepsilon^* = h^2/(8mV^{2/3})$ 为单位，最低的几个能级与简并度为：

| $n_x^2 + n_y^2 + n_z^2$ | 3 | 6 | 9 | 11 | 12 | 14 |
|---|---|---|---|---|---|---|
| $(n_x, n_y, n_z)$ | $(1,1,1)$ | $(1,1,2)$ 的排列 | $(1,2,2)$ 的排列 | $(1,1,3)$ 的排列 | $(2,2,2)$ | $(1,2,3)$ 的排列 |
| $g$ | 1 | 3 | 3 | 3 | 1 | 6 |

对宏观容器，能级间隔小得惊人：$\ce{N2}$ 分子（$m = 4.65\times10^{-26}\,\mathrm{kg}$）在 $a = 10\,\mathrm{cm}$ 的箱中，$\varepsilon^* \approx 1.2\times10^{-40}\,\mathrm{J}$，而 $298\,\mathrm{K}$ 时 $k_{\mathrm{B}}T = 4.1\times10^{-21}\,\mathrm{J}$，两者相差 $10^{19}$ 倍以上。能量不超过 $\varepsilon$ 的量子态数等于半径 $R = (\varepsilon/\varepsilon^*)^{1/2}$ 的球在第一卦限中的整点数，约为 $\frac{1}{8}\cdot\frac{4}{3}\pi R^3 = \frac{\pi}{6}(\varepsilon/\varepsilon^*)^{3/2}$；取 $\varepsilon \sim k_{\mathrm{B}}T$，这是 $10^{29}$ 量级的数。所以平动能级可以看作连续的，而能量在 $k_{\mathrm{B}}T$ 附近的量子态数远远多于分子数。

## 10.2. 微观状态数

### 10.2.1. 计数工具与 Stirling 公式

计数要用到两个组合公式。$N$ 个不同的物体分成 $k$ 堆、各堆依次有 $N_1, \dots, N_k$ 个（$\sum N_i = N$）的分法有

$$
\frac{N!}{N_1!\,N_2!\cdots N_k!}
$$
种，这就是**多项分布**的系数（[3.1.6 定义 6.2.3](/3.1.6#def-6.2.3)）；$N$ 个不同的物体放进 $g$ 个不同的盒子、每盒不限个数，有 $g^N$ 种放法。

微观状态数中的阶乘都是 $10^{23}$ 量级的数的阶乘，必须用渐近公式处理。

**定理 10.2.1（Stirling 公式）** $N \to \infty$ 时，

$$
N! \sim \sqrt{2\pi N}\left(\frac{N}{\mathrm{e}}\right)^N, \qquad \ln N! = N\ln N - N + \frac{1}{2}\ln(2\pi N) + O\!\left(\frac{1}{N}\right).
$$
统计热力学中 $N$ 极大，取它的粗略形式

$$
\ln N! \approx N\ln N - N.
\tag{10.2}
$$

**证明** 只证粗略形式。$\ln N! = \sum_{k=1}^{N}\ln k$，而 $\ln x$ 单调递增，所以

$$
\int_1^N \ln x\,\mathrm{d}x \le \sum_{k=1}^{N}\ln k \le \int_1^{N+1}\ln x\,\mathrm{d}x,
$$
即 $N\ln N - N + 1 \le \ln N! \le (N+1)\ln(N+1) - N$，两端与 $N\ln N - N$ 的差都是 $O(\ln N)$，相对于 $N\ln N$ 趋于零。精确形式中的 $\sqrt{2\pi N}$ 可以由中心极限定理得到（[3.1.13 例 13.4.3](/3.1.13#ex-13.4.3)）。$\square$

式 (10.2) 舍去的 $\frac{1}{2}\ln(2\pi N)$ 对 $N = 10^{23}$ 只有约 $27$，与 $N\ln N \approx 5\times10^{24}$ 相比完全可以忽略（下图）。在推导中还常用它的推论 $\frac{\mathrm{d}\ln N!}{\mathrm{d}N} \approx \ln N$。

![Stirling 公式计算 ln N! 的相对误差：粗略形式 N ln N − N 的相对误差约为 1/(2N)，加上 ½ ln(2πN) 一项后约为 1/(12N² ln N)](./plots/stirling-accuracy.py)

### 10.2.2. 定域子系的微观状态数

考虑 $N$、$V$、$U$ 给定的独立定域子系。$V$ 给定决定了能级 $\varepsilon_i$ 与简并度 $g_i$。在某一时刻，每个粒子处于某个能级上，各能级上的粒子数 $\{N_0, N_1, N_2, \dots\}$ 称为系统的一种能量分布（简称分布，记作 $D$）。每种分布都必须满足

$$
\sum_i N_i = N, \qquad \sum_i N_i\varepsilon_i = U.
\tag{10.3}
$$

实现一种分布 $D$ 的微观状态数 $t_D$ 分两步计算：先决定哪些粒子在哪个能级上，这是把 $N$ 个可区分的粒子分成大小为 $N_0, N_1, \dots$ 的堆，有 $N!/\prod_i N_i!$ 种分法；再让能级 $i$ 上的 $N_i$ 个粒子各自选择该能级的 $g_i$ 个量子态之一，有 $g_i^{N_i}$ 种。于是

$$
t_D = N!\prod_i\frac{g_i^{N_i}}{N_i!} \qquad (\text{定域子系}).
\tag{10.4}
$$
系统的总微观状态数是对一切满足式 (10.3) 的分布求和：

$$
\Omega = \sum_D t_D.
$$
$\Omega$ 就是宏观态 $(N, V, U)$ 的**热力学概率**（[5.2.4 定义 4.7.2](/5.2.4#def-4.7.2)）。

### 10.2.3. 离域子系的微观状态数

离域子系的粒子不可区分，"哪些粒子在能级 $i$ 上"不再有意义，只需数出 $N_i$ 个全同粒子在 $g_i$ 个量子态中的分配方式。这取决于粒子是玻色子还是费米子（[5.5.4](/5.5.4#sec-4.3.2)）：

- 玻色子：每个量子态的粒子数不限。$N_i$ 个相同的球放进 $g_i$ 个盒子，相当于 $N_i$ 个球与 $g_i - 1$ 块隔板排成一列，有 $\frac{(N_i + g_i - 1)!}{N_i!\,(g_i - 1)!}$ 种方式；
- 费米子：受 **Pauli 不相容原理**限制，每个量子态至多一个粒子，有 $\binom{g_i}{N_i} = \frac{g_i!}{N_i!\,(g_i - N_i)!}$ 种方式。

对这两种计数求最概然分布，分别得到 **Bose–Einstein 分布**与 **Fermi–Dirac 分布**。当每个能级的量子态数远多于其上的粒子数，$g_i \gg N_i$ 时，

$$
\frac{(N_i + g_i - 1)!}{(g_i - 1)!} = g_i(g_i + 1)\cdots(g_i + N_i - 1) \approx g_i^{N_i}, \qquad \frac{g_i!}{(g_i - N_i)!} = g_i(g_i - 1)\cdots(g_i - N_i + 1) \approx g_i^{N_i},
$$
两种统计给出同一个结果：

$$
t_D = \prod_i\frac{g_i^{N_i}}{N_i!} \qquad (\text{离域子系}，g_i \gg N_i).
\tag{10.5}
$$
它恰好是定域子系的式 (10.4) 除以 $N!$。"除以 $N!$"常被说成"等同粒子修正"，上面的推导说明了它的来历与适用条件：粒子不可区分，且几乎没有两个粒子处于同一量子态。由例 10.1.1，常温下气体的可占据量子态数比分子数多好几个数量级，条件很好地满足（定量检验见 [6.3.11](/6.3.11#sec-11.2)）；低温下的电子气、液氦、超冷原子气体不满足它，必须用量子统计。

### 10.2.4. 等概率原理与最概然分布

$\Omega$ 中各个微观态出现的机会是否相等？统计热力学的基本假设是**等概率原理**（[5.2.4 性质 4.7.1](/5.2.4#pty-4.7.1)）：$N$、$V$、$U$ 给定的孤立系统处于平衡态时，每个可能的微观态出现的概率都等于 $1/\Omega$。于是分布 $D$ 出现的概率是 $t_D/\Omega$。

**定义 10.2.1** 在约束 (10.3) 下微观状态数 $t_D$ 最大的分布称为**最概然分布**，记其微观状态数为 $t_{\max}$。

Boltzmann 进一步假定：$N$ 足够大时，平衡态就是最概然分布，可以用 $t_{\max}$ 代替 $\Omega$。这个"假定"其实可以证明。设满足约束的分布共有 $n_D$ 种，则

$$
t_{\max} \le \Omega = \sum_D t_D \le n_D\,t_{\max}, \qquad\text{即}\qquad \ln t_{\max} \le \ln\Omega \le \ln t_{\max} + \ln n_D.
$$
若实际被占据的能级有 $k$ 个，每个 $N_i$ 只能取 $0, 1, \dots, N$，所以 $n_D \le (N + 1)^k$，$\ln n_D \le k\ln(N + 1)$ 只随 $N$ 对数增长；而由 Stirling 公式，$\ln t_{\max}$ 与 $N$ 成正比。因此

$$
\ln\Omega = \ln t_{\max}\left[1 + O\!\left(\frac{\ln N}{N}\right)\right],
\tag{10.6}
$$
对 $N \sim 10^{23}$ 两者没有任何可测的差别。熵只依赖 $\ln\Omega$，所以计算熵时可以只用最概然分布：$S = k_{\mathrm{B}}\ln\Omega \approx k_{\mathrm{B}}\ln t_{\max}$。

更直观地看，把 $\ln t_D$ 在最概然分布 $N_i^*$ 附近展开到二阶（$\partial^2\ln t_D/\partial N_i^2 = -1/N_i$），

$$
t_D \approx t_{\max}\exp\left[-\sum_i\frac{(N_i - N_i^*)^2}{2N_i^*}\right]:
$$
各能级粒子数对最概然值的偏离近似服从方差为 $N_i^*$ 的**正态分布**，相对**涨落** $\Delta N_i/N_i^* \sim (N_i^*)^{-1/2}$。$N_i^* \sim 10^{20}$ 时，相对涨落只有 $10^{-10}$：几乎所有微观态都属于与最概然分布无法区分的那些分布。这正是**大数定律**在统计热力学中的体现。

下图用一个可以精确计数的小系统说明这一点：$N$ 个可区分粒子分布在能量为 $0$、$\varepsilon$、$2\varepsilon$ 的三个非简并能级上，总能量 $U = N\varepsilon/2$。一种分布由 $N_2$ 确定（$N_1 = U/\varepsilon - 2N_2$，$N_0 = N - N_1 - N_2$），$t_D$ 由式 (10.4) 精确算出。$N$ 增大时，$t_D/\Omega$ 迅速集中到 10.3 节的 Boltzmann 分布给出的位置，$\ln t_{\max}/\ln\Omega$ 趋于 1。

![N 个可区分粒子分布在三个等间距能级上（U = Nε/2）的精确计数。左：各分布所含微观态占总数的比例随 N₂/N 的分布，N 从 40 增大到 40000 时迅速集中到 Boltzmann 分布给出的 N₂/N = 0.116（虚线）；右：ln t_max / ln Ω 随 N 增大趋于 1](./plots/three-level-distributions.py)

## 10.3. Boltzmann 分布

### 10.3.1. 最概然分布的求法

求最概然分布就是在两个约束 (10.3) 下求 $t_D$ 的极大值，这是**条件极值**问题，用 **Lagrange 乘子法**（[2.2.11](/2.2.11#sec-11.6)）。

**定理 10.3.1（Boltzmann 分布）** 独立定域子系，以及满足 $g_i \gg N_i$ 的独立离域子系，在 $N$、$V$、$U$ 给定时的最概然分布为

$$
N_i^* = \frac{N}{q}\,g_i\,\mathrm{e}^{-\beta\varepsilon_i}, \qquad q = \sum_i g_i\,\mathrm{e}^{-\beta\varepsilon_i},
\tag{10.7}
$$
其中 $\beta$ 是由总能量 $U$ 决定的常数（10.3.2 节证明 $\beta = 1/(k_{\mathrm{B}}T)$）。

**证明** 对式 (10.4) 取对数，并对 $N!$ 与各 $N_i!$ 用 Stirling 公式：

$$
\ln t_D = \ln N! + \sum_i\left(N_i\ln g_i - \ln N_i!\right) \approx \ln N! + \sum_i\left(N_i\ln g_i - N_i\ln N_i + N_i\right).
$$
$\ln t_D$ 与 $t_D$ 同时取极大。作 Lagrange 函数

$$
L = \ln t_D - \alpha\left(\sum_i N_i - N\right) - \beta\left(\sum_i N_i\varepsilon_i - U\right),
$$
把各 $N_i$ 当作独立变量，令 $\partial L/\partial N_i = 0$：

$$
\ln g_i - \ln N_i - \alpha - \beta\varepsilon_i = 0, \qquad\text{即}\qquad N_i^* = g_i\,\mathrm{e}^{-\alpha}\,\mathrm{e}^{-\beta\varepsilon_i}.
$$
代入 $\sum_i N_i = N$ 得 $\mathrm{e}^{-\alpha} = N/\sum_i g_i\mathrm{e}^{-\beta\varepsilon_i} = N/q$，即式 (10.7)；$\beta$ 由第二个约束 $\sum_i N_i^*\varepsilon_i = U$ 确定。又 $\partial^2\ln t_D/\partial N_i\partial N_j = -\delta_{ij}/N_i < 0$，$\ln t_D$ 是严格凹函数，所以驻点是唯一的极大值点。对离域子系，式 (10.5) 的对数只比定域子系少了常数 $\ln N!$，推导与结果完全相同。$\square$

**注 10.3.1** 推导中对每个 $N_i$ 都用了 Stirling 公式，这要求每个能级上的粒子数都很大。对气体，单个平动能级上的分子数并不大（$g_i \gg N_i$ 正说明平均每个量子态远不到一个分子）。严格的做法是把能量相近的大量能级合并成"能级组"，组内的量子态数与粒子数都是大数，对能级组重复上面的推导，结果不变；或者改用 Gibbs 的正则系综（10.4.2 节），根本不需要最概然分布。

### 10.3.2. β 的确定

$\beta$ 的物理意义由熵确定。对定域子系，把最概然分布 (10.7) 代入 $\ln t_{\max} = N\ln N + \sum_i N_i^*\ln(g_i/N_i^*)$（Stirling 公式），注意 $\ln(g_i/N_i^*) = \ln(q/N) + \beta\varepsilon_i$：

$$
\ln t_{\max} = N\ln N + N\ln\frac{q}{N} + \beta U = N\ln q + \beta U.
$$
由 $S = k_{\mathrm{B}}\ln\Omega \approx k_{\mathrm{B}}\ln t_{\max}$，

$$
S = k_{\mathrm{B}}\left[N\ln q(\beta) + \beta U\right].
$$
$N$、$V$ 不变时能级 $\varepsilon_i$ 不变，$S$ 只通过 $U$ 和 $\beta(U)$ 变化：

$$
\mathrm{d}S = k_{\mathrm{B}}\left[N\frac{\mathrm{d}\ln q}{\mathrm{d}\beta}\,\mathrm{d}\beta + U\,\mathrm{d}\beta + \beta\,\mathrm{d}U\right].
$$
而 $N\frac{\mathrm{d}\ln q}{\mathrm{d}\beta} = -\frac{N}{q}\sum_i g_i\varepsilon_i\mathrm{e}^{-\beta\varepsilon_i} = -\sum_i N_i^*\varepsilon_i = -U$，前两项相消，于是 $\left(\frac{\partial S}{\partial U}\right)_{N,V} = k_{\mathrm{B}}\beta$。另一方面，由**热力学基本方程** $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$（[6.3.3 定理 3.2.1](/6.3.3#thm-3.2.1)），$\left(\frac{\partial S}{\partial U}\right)_V = \frac{1}{T}$。比较两式，

$$
\beta = \frac{1}{k_{\mathrm{B}}T}.
\tag{10.8}
$$
离域子系的 $\ln t_{\max}$ 只多一个与 $U$ 无关的项（10.4.1 节），结论相同。

有的教材把 Lagrange 乘子项写作 $+\beta(\sum_i N_i\varepsilon_i - U)$，得到 $N_i \propto g_i\mathrm{e}^{\beta\varepsilon_i}$ 与 $\beta = -1/(k_{\mathrm{B}}T)$；本站采用现行教材的通行写法 $\beta = 1/(k_{\mathrm{B}}T) > 0$。这样确定的 $T$ 就是热力学温度：$\beta$ 是 Lagrange 乘子，而能够交换能量的两个系统达到平衡时 $\beta$ 必须相等，正对应于热平衡时温度相等（**热力学第零定律**）。

代回式 (10.7)，就得到能级形式的 **Boltzmann 分布**：

$$
\frac{N_i^*}{N} = \frac{g_i\,\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)}}{q}, \qquad \frac{N_i^*}{N_j^*} = \frac{g_i}{g_j}\,\mathrm{e}^{-(\varepsilon_i - \varepsilon_j)/(k_{\mathrm{B}}T)}.
\tag{10.9}
$$
**Boltzmann 因子** $\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)}$ 说明能量比 $k_{\mathrm{B}}T$ 高得多的能级几乎不被占据，简并度 $g_i$ 则给出能级所含状态数的权重。物理中的定理 1.7.1（[5.2.1](/5.2.1#thm-1.7.1)）是它在经典连续能量下的形式：以重力场中高度 $h$ 处的分子为例，$\varepsilon = mgh$，即得恒温气压公式 $p = p_0\mathrm{e}^{-mgh/(k_{\mathrm{B}}T)}$。

### 10.3.3. 分子配分函数及其概率意义

**定义 10.3.1** 单个分子所有能级的 Boltzmann 因子按简并度加权之和

$$
q = \sum_i g_i\,\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)} = \sum_{s}\mathrm{e}^{-\varepsilon_s/(k_{\mathrm{B}}T)}
\tag{10.10}
$$
称为**分子配分函数**。第一个和对能级求和，第二个和对分子的全部量子态 $s$ 求和，两者相等。

- $q$ 是量纲一的量，由分子的能级算出。它依赖于 $T$，并通过能级（例如平动能级 (10.1)）依赖于 $V$，与 $N$ 无关：$q = q(T, V)$。
- $q$ 是"热可及的量子态数"：取基态能量为零，$T \to 0$ 时 $q \to g_0$，只有基态被占据；$T$ 升高，越来越多的激发态进入 $k_{\mathrm{B}}T$ 的范围，$q$ 增大；$T \to \infty$ 时 $q$ 趋于全部量子态数。
- $q$ 的名称来自式 (10.9)：它是把 $N$ 个分子"分配"到各能级时的归一化因子。

用概率论的语言，随机取一个分子，它处于能级 $i$ 的概率是 $P_i = g_i\mathrm{e}^{-\beta\varepsilon_i}/q$，$q$ 是这个概率分布的归一化常数。分子能量的期望与方差都可以由 $\ln q$ 对 $\beta$ 求导得到：

$$
\langle\varepsilon\rangle = \sum_i P_i\varepsilon_i = -\frac{\partial\ln q}{\partial\beta} = k_{\mathrm{B}}T^2\,\frac{\partial\ln q}{\partial T}, \qquad \sigma_\varepsilon^2 = \langle\varepsilon^2\rangle - \langle\varepsilon\rangle^2 = \frac{\partial^2\ln q}{\partial\beta^2} = k_{\mathrm{B}}T^2\,\frac{\partial\langle\varepsilon\rangle}{\partial T},
\tag{10.11}
$$
导数都在 $V$ 不变时求。第二式说明能量涨落与热容成正比：热容大的系统，能量涨落也大。$N$ 个独立分子的总能量 $U = N\langle\varepsilon\rangle$，方差为 $N\sigma_\varepsilon^2$，相对涨落 $\propto N^{-1/2}$，与 10.2.4 节的结论一致。

**例 10.3.1（二能级系统）** 设分子只有两个能级：基态能量 $0$、简并度 $g_0$，激发态能量 $\varepsilon$、简并度 $g_1$。则 $q = g_0 + g_1\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}$，激发态的分数与每个分子的平均能量为

$$
\frac{N_1}{N} = \frac{g_1\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}}{g_0 + g_1\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}}, \qquad \langle\varepsilon\rangle = \varepsilon\,\frac{N_1}{N}.
$$
$T \to \infty$ 时 $N_1/N \to g_1/(g_0 + g_1)$，但永远不会超过它：热平衡不能造成粒子数反转（激光需要非平衡的泵浦，[5.5.5](/5.5.5#sec-5.2.3)）。由式 (10.11)，热容 $C_V = N\,\mathrm{d}\langle\varepsilon\rangle/\mathrm{d}T = Nk_{\mathrm{B}}(\varepsilon/k_{\mathrm{B}}T)^2\,P_0P_1$。它在 $k_{\mathrm{B}}T \approx 0.42\,\varepsilon$（$g_0 = g_1$ 时）出现一个峰：温度太低，激发不了；温度太高，两能级已接近饱和，再吸热也改变不了布居。这种热容峰称为 Schottky 反常（Schottky anomaly），在顺磁盐的低温热容中观测到（[5.3.8](/5.3.8)）。

![二能级系统（g₁/g₀ = 1 与 3）：左为激发态分子的分数，点线是高温极限 g₁/(g₀ + g₁)；右为每个分子的热容，即 Schottky 反常](./plots/two-level-system.py)

二能级的 Boltzmann 分布用途很广。核磁共振中，$400\,\mathrm{MHz}$ 的质子自旋能级差 $h\nu$ 只有 $k_{\mathrm{B}}T$（$298\,\mathrm{K}$）的 $6.4\times10^{-5}$，上下能级的布居差只有约 $3\times10^{-5}$，这是 NMR 灵敏度低的根本原因。生物物理中，离子通道的开与关、蛋白质的折叠态与去折叠态常用二态模型描述：开放概率 $P_{\mathrm{open}} = 1/[1 + \mathrm{e}^{\Delta G/(k_{\mathrm{B}}T)}]$，$\Delta G$ 是开放态与关闭态的 Gibbs 自由能之差（这里用自由能而不是能量，是因为每个"态"本身包含大量微观态）。

## 10.4. 配分函数与热力学函数

### 10.4.1. 熵

由 $S = k_{\mathrm{B}}\ln t_{\max}$ 与 10.3.2 节的计算，定域子系的熵为

$$
S = Nk_{\mathrm{B}}\ln q + \frac{U}{T} \qquad (\text{定域子系}).
\tag{10.12}
$$
离域子系的 $t_D$ 用式 (10.5)：$\ln t_{\max} = \sum_i\left[N_i^*\ln(g_i/N_i^*) + N_i^*\right] = N\ln(q/N) + \beta U + N$，再由 Stirling 公式 $N\ln N - N = \ln N!$，

$$
S = k_{\mathrm{B}}\ln\frac{q^N}{N!} + \frac{U}{T} \qquad (\text{离域子系}).
\tag{10.13}
$$
两者相差 $k_{\mathrm{B}}\ln N!$。

### 10.4.2. 系统配分函数

由 $A = U - TS$，定域子系 $A = -Nk_{\mathrm{B}}T\ln q = -k_{\mathrm{B}}T\ln q^N$，离域子系 $A = -k_{\mathrm{B}}T\ln(q^N/N!)$。两种情形可以统一写成 $A = -k_{\mathrm{B}}T\ln Z$，$Z$ 有更一般的意义。

**定义 10.4.1** 设 $N$、$V$ 给定的系统的微观态为 $s$，能量为 $E_s$。称

$$
Z = \sum_s \mathrm{e}^{-E_s/(k_{\mathrm{B}}T)}
$$
为系统的**配分函数**（正则配分函数）。

Gibbs 的正则系综理论证明：与温度为 $T$ 的热源接触的系统处于微观态 $s$ 的概率为 $\mathrm{e}^{-E_s/(k_{\mathrm{B}}T)}/Z$（这正是 [5.2.1 定理 1.7.1](/5.2.1#thm-1.7.1) 末句所说的"一个微观状态的概率"），并且 $A = -k_{\mathrm{B}}T\ln Z$ 对任意系统成立，包括相依子系。对独立子系，系统配分函数可以用分子配分函数表示：

**定理 10.4.1** 对 $N$ 个独立粒子组成的系统，

$$
Z = q^N \quad (\text{定域子系}), \qquad Z = \frac{q^N}{N!} \quad (\text{离域子系}，g_i \gg N_i).
\tag{10.14}
$$

**证明** 独立子系的微观态由各粒子的量子态 $(s_1, s_2, \dots, s_N)$ 确定，$E_s = \varepsilon_{s_1} + \cdots + \varepsilon_{s_N}$。粒子可区分时，各 $s_k$ 独立地取遍单粒子量子态，指数函数把和变成积，

$$
Z = \sum_{s_1}\cdots\sum_{s_N}\mathrm{e}^{-\beta(\varepsilon_{s_1} + \cdots + \varepsilon_{s_N})} = \left(\sum_{s}\mathrm{e}^{-\beta\varepsilon_s}\right)^N = q^N.
$$
粒子不可区分时，$N$ 个粒子占据 $N$ 个互不相同的量子态的同一种安排在上式中被数了 $N!$ 次（粒子编号的全部排列）。当 $g_i \gg N_i$ 时，两个粒子处于同一量子态的项所占比例可以忽略，所以 $Z = q^N/N!$。$\square$

**注 10.4.1** 符号 $Z$ 在 [6.3.1](/6.3.1) 与 [6.3.4](/6.3.4) 中表示**压缩因子**，本章与下一章表示系统配分函数，两者不同时出现。物理 [5.2.1](/5.2.1#sec-1.7.2) 中把单粒子状态的 Boltzmann 因子之和也写作 $Z$；在化学中习惯用 $q$ 表示分子配分函数，用 $Z$（或 $Q$）表示系统配分函数，本站用 $q$ 与 $Z$（$Q$ 已用于热量与反应商）。

有了 $A(T, V, N) = -k_{\mathrm{B}}T\ln Z$，其余热力学函数都可以由 $\mathrm{d}A = -S\,\mathrm{d}T - p\,\mathrm{d}V$（[6.3.3 定理 3.2.1](/6.3.3#thm-3.2.1)）求出，因为 $A$ 以 $T$、$V$ 为自然变量时是**特性函数**（[6.3.3 定义 3.2.1](/6.3.3#def-3.2.1)）：

| 函数 | 用 $Z$ 表示 | 定域子系（$Z = q^N$） | 离域子系（$Z = q^N/N!$） |
|---|---|---|---|
| $A$ | $-k_{\mathrm{B}}T\ln Z$ | $-Nk_{\mathrm{B}}T\ln q$ | $-k_{\mathrm{B}}T\ln\dfrac{q^N}{N!}$ |
| $S$ | $k_{\mathrm{B}}\ln Z + k_{\mathrm{B}}T\left(\dfrac{\partial\ln Z}{\partial T}\right)_V$ | $Nk_{\mathrm{B}}\ln q + \dfrac{U}{T}$ | $k_{\mathrm{B}}\ln\dfrac{q^N}{N!} + \dfrac{U}{T}$ |
| $U$ | $k_{\mathrm{B}}T^2\left(\dfrac{\partial\ln Z}{\partial T}\right)_V$ | $Nk_{\mathrm{B}}T^2\left(\dfrac{\partial\ln q}{\partial T}\right)_V$ | 同左 |
| $p$ | $k_{\mathrm{B}}T\left(\dfrac{\partial\ln Z}{\partial V}\right)_T$ | $Nk_{\mathrm{B}}T\left(\dfrac{\partial\ln q}{\partial V}\right)_T$ | 同左 |
| $H = U + pV$ | — | $Nk_{\mathrm{B}}T^2\left(\dfrac{\partial\ln q}{\partial T}\right)_V + Nk_{\mathrm{B}}TV\left(\dfrac{\partial\ln q}{\partial V}\right)_T$ | 同左 |
| $G = A + pV$ | — | $-Nk_{\mathrm{B}}T\ln q + Nk_{\mathrm{B}}TV\left(\dfrac{\partial\ln q}{\partial V}\right)_T$ | $-k_{\mathrm{B}}T\ln\dfrac{q^N}{N!} + Nk_{\mathrm{B}}TV\left(\dfrac{\partial\ln q}{\partial V}\right)_T$ |
| $C_V$ | $\left(\dfrac{\partial U}{\partial T}\right)_V$ | $\dfrac{\partial}{\partial T}\left[Nk_{\mathrm{B}}T^2\left(\dfrac{\partial\ln q}{\partial T}\right)_V\right]_V$ | 同左 |

（表中的偏导数都在 $N$ 不变时求。）$U$、$H$、$p$、$C_V$ 只含 $\ln q$ 的导数，定域与离域子系的表达式相同；$S$、$A$、$G$ 含 $\ln q$ 本身，离域子系多出 $-k_{\mathrm{B}}\ln N!$ 一类的常数项。$U$ 的表达式与式 (10.11) 的 $U = N\langle\varepsilon\rangle$ 一致。

**例 10.4.1（理想气体的状态方程）** 分子的能级中只有平动能级与体积有关，由式 (10.1)，平动配分函数与 $V$ 成正比（[6.3.11](/6.3.11#sec-11.2)），内部运动的配分函数与 $V$ 无关，所以任何理想气体的 $q = V f(T)$。于是

$$
p = Nk_{\mathrm{B}}T\left(\frac{\partial\ln q}{\partial V}\right)_T = \frac{Nk_{\mathrm{B}}T}{V}, \qquad pV = Nk_{\mathrm{B}}T = nRT,
$$
与分子的内部结构无关。同理 $U = Nk_{\mathrm{B}}T^2(\partial\ln q/\partial T)_V$ 中的 $V$ 因子在求导时消失，$U$ 只是 $T$ 的函数：这就是 Joule 实验结论（[6.3.1](/6.3.1)）的微观解释。由 $pV = Nk_{\mathrm{B}}T$ 与 Stirling 公式，理想气体的 Gibbs 自由能

$$
G = A + pV = -k_{\mathrm{B}}T\left(N\ln q - N\ln N + N\right) + Nk_{\mathrm{B}}T = -Nk_{\mathrm{B}}T\ln\frac{q}{N},
\tag{10.15}
$$
每个分子的 Gibbs 自由能（即**化学势**）$\mu = -k_{\mathrm{B}}T\ln(q/N)$。由它求平衡常数见 [6.3.11](/6.3.11#sec-11.7)。

### 10.4.3. 能量零点的选择

能量只有相对的意义。配分函数可以从分子基态的能量 $\varepsilon_0$ 算起，也可以从别的零点算起。记以基态为零点的配分函数为 $q^{(0)} = \sum_i g_i\mathrm{e}^{-(\varepsilon_i - \varepsilon_0)/(k_{\mathrm{B}}T)}$，则

$$
q = \mathrm{e}^{-\varepsilon_0/(k_{\mathrm{B}}T)}\,q^{(0)}, \qquad \ln q = \ln q^{(0)} - \frac{\varepsilon_0}{k_{\mathrm{B}}T}.
$$
代入上表：$\ln q$ 的 $T$ 导数多出 $\varepsilon_0/(k_{\mathrm{B}}T^2)$，$V$ 导数不变。所以（记 $U_0 = N\varepsilon_0$，即系统在 $0\,\mathrm{K}$ 的能量）

$$
U = U^{(0)} + U_0, \quad H = H^{(0)} + U_0, \quad A = A^{(0)} + U_0, \quad G = G^{(0)} + U_0, \qquad S = S^{(0)}, \quad p = p^{(0)}, \quad C_V = C_V^{(0)}.
$$
$S$ 中的两项 $Nk_{\mathrm{B}}\ln q$ 与 $U/T$ 的变化 $\mp N\varepsilon_0/T$ 恰好相消。$N_i^*/N$ 也与零点无关（分子分母同乘一个因子）。

对不涉及化学变化的过程，初末态的 $U_0$ 相同，零点的选择不影响 $\Delta U$、$\Delta H$、$\Delta A$、$\Delta G$。化学反应中各物种的分子不同，必须把所有物种的能量放在共同的零点上，此时 $U_0$ 的差（反应在 $0\,\mathrm{K}$ 的能量变化）是平衡常数中的关键一项（[6.3.11](/6.3.11#sec-11.7)）。下一章计算各运动的配分函数时，一律以该运动的基态为零点，需要时再显式加上 $U_0$。

## 10.5. 热力学定律的统计意义

### 10.5.1. 热与功

独立子系的内能 $U = \sum_i N_i\varepsilon_i$，其全微分

$$
\mathrm{d}U = \sum_i\varepsilon_i\,\mathrm{d}N_i + \sum_i N_i\,\mathrm{d}\varepsilon_i
\tag{10.16}
$$
有两部分：能级不变、粒子在能级间重新分布引起的能量变化，与粒子分布不变、能级本身移动引起的能量变化。对封闭系统的**可逆过程**，它们分别就是热与功：

- 能级只随外参量（这里是体积）变化，$\sum_i N_i\,\mathrm{d}\varepsilon_i = \left(\sum_i N_i\frac{\partial\varepsilon_i}{\partial V}\right)\mathrm{d}V = -p\,\mathrm{d}V = \delta W_{\mathrm{r}}$，其中 $p = -\sum_i N_i\,\partial\varepsilon_i/\partial V$。（容易验证它与表中的 $p = Nk_{\mathrm{B}}T(\partial\ln q/\partial V)_T$ 相同。）
- 由 $S = k_{\mathrm{B}}\ln t_{\max}$ 与 $\partial\ln t_D/\partial N_i = \ln(g_i/N_i) = \alpha + \beta\varepsilon_i$（10.3.1 节），在 $\sum_i\mathrm{d}N_i = 0$ 时 $\mathrm{d}S = k_{\mathrm{B}}\sum_i(\alpha + \beta\varepsilon_i)\,\mathrm{d}N_i = \frac{1}{T}\sum_i\varepsilon_i\,\mathrm{d}N_i$，所以 $\sum_i\varepsilon_i\,\mathrm{d}N_i = T\,\mathrm{d}S = \delta Q_{\mathrm{r}}$。

于是式 (10.16) 就是**热力学第一定律** $\mathrm{d}U = \delta Q + \delta W$ 的微观形式：热是能级不变时粒子在能级间重新分配所传递的能量，功是分布不变时能级移动所传递的能量。

**例 10.5.1（绝热可逆膨胀）** 单原子理想气体绝热可逆地改变体积：$\delta Q_{\mathrm{r}} = 0$，各能级上的分子数不变，平动能级 (10.1) 按 $V^{-2/3}$ 整体移动。分布要始终保持 Boltzmann 形式 $N_i/N \propto g_i\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)}$，而 $N_i$ 不变、$\varepsilon_i \propto V^{-2/3}$，只有 $\varepsilon_i/(k_{\mathrm{B}}T)$ 保持不变才行，所以 $T \propto V^{-2/3}$，即 $TV^{2/3} = $ 常数。这正是 $\gamma = 5/3$ 的**绝热过程**方程 $TV^{\gamma - 1} = $ 常数（[6.3.1](/6.3.1)），这里没有用到热容的数值。

### 10.5.2. 熵、自发过程与第三定律

**Boltzmann 熵公式** $S = k_{\mathrm{B}}\ln\Omega$ 说明熵是系统微观状态数的量度。孤立系统中的自发过程，微观上是一个限制条件（隔板、反应的能垒、相界面）被撤除、系统可以到达的微观态集合扩大的过程：撤除限制后，原来的微观态仍然可以到达，又增加了新的微观态，所以 $\Omega_2 \ge \Omega_1$，$\Delta S \ge 0$。系统在扩大了的微观态集合中"漫游"，几乎总是处在属于最概然分布的那些微观态中，宏观上表现为趋于新的平衡态，这就是**熵增加原理**的统计意义。例如理想气体向真空膨胀，$q \propto V$，由式 (10.13)，$\Delta S = Nk_{\mathrm{B}}\ln(V_2/V_1)$，与 [5.2.4 例 4.8.1](/5.2.4#ex-4.8.1) 的计数结果相同。

$T \to 0$ 时，Boltzmann 因子使所有粒子都落到基态。若基态的简并度为 $g_0$，对定域子系，只有一种分布 $N_0 = N$，式 (10.4) 给出 $\Omega = g_0^N$，$S(0\,\mathrm{K}) = Nk_{\mathrm{B}}\ln g_0$。**完美晶体**中每个粒子的基态唯一，$g_0 = 1$，$S(0\,\mathrm{K}) = 0$，这就是**热力学第三定律**（[6.3.2 定理 2.4.2](/6.3.2#thm-2.4.2)）的统计解释。如果晶体中分子的取向在凝固时被"冻结"在无序状态，$0\,\mathrm{K}$ 时系统的微观态数仍大于 1，便有**残余熵**（[6.3.11](/6.3.11#sec-11.6.3)）。

### 10.5.3. 讨论：晶体与气体的熵

由式 (10.4) 与 (10.5)，同样的 $q$ 下 $\Omega_{\text{定域}}/\Omega_{\text{离域}} = N!$，定域子系的熵比离域子系大 $k_{\mathrm{B}}\ln N!$。另一方面，同一物质的晶体的熵总是比它的蒸气小得多（$S_{\mathrm{m}}(\mathrm{s}) < S_{\mathrm{m}}(\mathrm{l}) < S_{\mathrm{m}}(\mathrm{g})$）。这并不矛盾：比较是在"同样的 $q$"下作的，而晶体与气体的 $q$ 完全不同。

- 晶体是相依子系，原子间的作用把每个原子束缚在格点附近，作为定域子系处理时，每个原子只有 3 个振动模式，振动配分函数的量级为 $1$–$10$。
- 气体中分子在整个容器中自由运动，平动配分函数极大：$298\,\mathrm{K}$、$p^\circ$ 下 $\ce{N2}$ 的 $q_{\mathrm{t}}/N_{\mathrm{A}} \approx 6\times10^6$（[6.3.11](/6.3.11#sec-11.2)），还有转动的贡献。
- 液体介于两者之间：分子可以在较大范围内移动与转动，可及的能级多于晶体。

$N!$ 这个因子来自粒子不可区分，只是把气体巨大的 $q^N$ 修正为 $(q/N)^N\mathrm{e}^N$；能级越密、可及的量子态越多（$q$ 越大），熵越大，这才是决定性的因素。

## 小结

| 量 | 定域子系 | 离域子系（$g_i \gg N_i$） |
|---|---|---|
| 一种分布的微观状态数 $t_D$ | $N!\prod_i g_i^{N_i}/N_i!$ | $\prod_i g_i^{N_i}/N_i!$ |
| 最概然分布 | $N_i^*/N = g_i\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)}/q$ | 同左 |
| 系统配分函数 $Z$ | $q^N$ | $q^N/N!$ |
| $S$ | $Nk_{\mathrm{B}}\ln q + U/T$ | $k_{\mathrm{B}}\ln(q^N/N!) + U/T$ |
| $A$ | $-Nk_{\mathrm{B}}T\ln q$ | $-k_{\mathrm{B}}T\ln(q^N/N!)$ |
| $U$、$p$、$H$、$C_V$ | 由 $\ln q$ 的导数给出，两种系统相同 | |

- 统计热力学的基本假设是等概率原理；$N$ 很大时 $\ln\Omega = \ln t_{\max}$ 的相对误差为 $O(\ln N/N)$，因此可以只用最概然分布。
- Boltzmann 分布由 Lagrange 乘子法求出，乘子 $\beta = 1/(k_{\mathrm{B}}T)$ 由 $(\partial S/\partial U)_V = 1/T$ 确定。
- 配分函数是宏观性质与分子性质之间的桥梁：分子能级 → $q$ → $Z$ → $A = -k_{\mathrm{B}}T\ln Z$ → 全部热力学函数。
- 改变能量零点只使 $U$、$H$、$A$、$G$ 平移 $U_0$，不改变 $S$、$p$、$C_V$。

## 思考题

1. 下列说法哪些是 Boltzmann 统计的特点？(A) 讨论的是 $N$、$V$、$U$ 给定的系统；(B) 系统的能量满足 $\sum_i N_i\varepsilon_i = U$；(C) 每个量子态中的粒子数受 Pauli 不相容原理限制；(D) 一切可能的微观态出现的概率相等。
   答：A、B、D。C 是 Fermi–Dirac 统计的特点；Boltzmann 统计是 $g_i \gg N_i$ 的极限，Pauli 原理的限制在其中不起作用。
2. 用 $q$ 与用 $q^{(0)}$ 分别计算下列函数，哪些结果不同：$U$、$H$、$S$、$A$、$G$、$p$、$C_V$？
   答：$U$、$H$、$A$、$G$ 相差 $U_0 = N\varepsilon_0$；$S$、$p$、$C_V$ 相同。
3. 根据熵的统计意义，判断下列过程的熵变符号：(1) 水蒸气凝结成水；(2) $\ce{CaCO3}$ 受热分解；(3) 乙烯聚合成聚乙烯；(4) 气体吸附在催化剂表面；(5) 磷脂膜由凝胶态转变为流动的液晶态。
   答：(1) 分子失去在整个容器中的平动，$\Delta S < 0$；(2) 生成气体，分子数与平动自由度增加，$\Delta S > 0$；(3) 分子数减少，$\Delta S < 0$；(4) 分子被限制在表面上，平动减少，$\Delta S < 0$；(5) 脂质分子的烃链由有序变为无序，分子在膜平面内的移动与链段的转动增加，$\Delta S > 0$（这一相变是吸热的，由熵驱动）。
4. 为什么说"根据统计热力学可以算出 $N$、$V$、$U$ 给定的系统的熵的绝对值"并不完全准确？
   答：$S = k_{\mathrm{B}}\ln\Omega$ 原则上给出熵的绝对值，但实际计算总要略去一些在所讨论的温度范围内"冻结"、在化学与物理过程中不变的自由度，最典型的是核自旋（[6.3.11](/6.3.11#sec-11.5)）。所以通常所说的统计熵也是一种约定的熵：它与以 $0\,\mathrm{K}$ 完美晶体为零点的量热熵采用同样的约定，两者可以直接比较，差别就是残余熵。
