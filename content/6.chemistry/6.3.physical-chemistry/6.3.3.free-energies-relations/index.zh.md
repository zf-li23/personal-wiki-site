---
title: 自由能与热力学基本关系
---

**熵增加原理**给出了一切宏观过程方向与限度的最终判据，但用它判断一个化学过程，必须同时计算系统与环境的熵变，还要把系统与环境合起来看成孤立系统。化学中最常见的条件是等温等容或等温等压，本章从 **Clausius 不等式**出发，构造两个只用系统自身性质就能作判据的状态函数：Helmholtz 自由能 $A$ 与 **Gibbs 自由能** $G$（3.1），并给出它们与最大功、最大非体积功的关系。第二部分建立热力学的数学结构：四个热力学基本方程与特性函数（3.2），对应系数关系与 Maxwell 关系（3.3），由它们推出不依赖于具体物质的普遍关系，例如热力学状态方程与 $C_p - C_V$ 的一般式（3.4）。最后系统地讨论各类过程 $\Delta G$、$\Delta A$ 的计算（3.5）和 $G$ 随温度变化的 Gibbs–Helmholtz 方程（3.6）。Gibbs 自由能与 Gibbs 判据在 [6.1.6](/6.1.6#sec-6.4.7) 已经引入，这里补全推导与适用条件；第一、二定律与熵见 [5.2.3](/5.2.3)、[5.2.4](/5.2.4) 和 [6.3.2](/6.3.2)；所用的偏导数、全微分与隐函数的运算见 [2.2.10](/2.2.10)。本章的关系式是后面各章的工具：组成可变时加上化学势一项（[6.3.4](/6.3.4)），Gibbs–Helmholtz 方程用于平衡常数随温度的变化（[6.3.7](/6.3.7)）与电动势的温度系数（[6.3.13](/6.3.13)），Clapeyron 方程（[6.3.8](/6.3.8)）则是 Maxwell 关系在两相共存时的形式。

## 3.1. Helmholtz 自由能与 Gibbs 自由能判据

### 3.1.1. 熵判据的局限

封闭系统任意过程的 **Clausius 不等式**是

$$
\mathrm{d}S \ge \frac{\delta Q}{T_{\mathrm{sur}}},
$$
其中 $T_{\mathrm{sur}}$ 是与系统交换热量的环境（热源）的温度，等号对可逆过程成立。直接用它判断方向有三点不便：要计算实际过程的热温商 $\delta Q/T_{\mathrm{sur}}$；熵增加原理只适用于绝热或孤立系统，一般过程要把环境并进来构成大孤立系统，再计算环境熵变 $\Delta S_{\mathrm{sur}} = -Q/T_{\mathrm{sur}}$；而对于电解水这类需要外界做电功才能进行的过程，大孤立系统的熵仍然增加，熵判据只说明"在电功的推动下可以发生"，并不直接回答"不做电功能否自发进行"。实际关心的是两种条件：等温等容的封闭系统与等温等压的封闭系统。在这两种条件下，环境的作用完全由温度和压力确定，可以把 Clausius 不等式改写成只含系统状态函数的形式。

### 3.1.2. Helmholtz 自由能

设封闭系统只与一个温度恒为 $T_{\mathrm{sur}}$ 的热源交换热量，过程的始态与末态温度都等于 $T_{\mathrm{sur}}$（过程中间系统的温度可以不同，例如在恒温槽中进行的燃烧）。这样的过程称为等温过程。积分 Clausius 不等式得 $Q \le T_{\mathrm{sur}}\Delta S$，代入第一定律 $\Delta U = Q + W$（$W$ 是环境对系统做的总功）：

$$
W \ge \Delta U - T_{\mathrm{sur}}\Delta S = \Delta U - \Delta(TS),
$$
最后一步用到 $T_1 = T_2 = T_{\mathrm{sur}}$。右端是一个状态函数的改变量。

**定义 3.1.1（Helmholtz 自由能）** 状态函数

$$
A = U - TS
$$
称为系统的 **Helmholtz 自由能**（IUPAC 称 Helmholtz 能），单位 J。

$A$ 是广延量。它本身没有直接的物理意义，但其改变量在等温条件下有明确的意义：

**定理 3.1.1（最大功）** 封闭系统的等温过程满足

$$
-W \le -\Delta A, \tag{3.1}
$$
等号对可逆过程成立。即系统在等温过程中对外所能做的功（包括体积功与非体积功）最多等于其 Helmholtz 自由能的减少，只有等温可逆过程才能达到。

这就是"等温可逆过程做功最多"的依据：两个过程始末态相同时 $\Delta A$ 相同，可逆过程的 $-W_{\mathrm{r}} = -\Delta A$，不可逆过程的 $-W_{\mathrm{ir}} < -\Delta A$。有的教材称 $A$ 为"功函数"，本站不用这一名称，以免与金属的逸出功混淆。

把总功分成体积功与**非体积功**，$W = -\int p_{\mathrm{ex}}\,\mathrm{d}V + W'$。若系统体积不变，体积功为零，式 (3.1) 成为 $W' \ge \Delta A$，再令 $W' = 0$：

**定理 3.1.2（Helmholtz 自由能判据）** 封闭系统在等温、等容、不做非体积功的条件下，

$$
\Delta A \le 0 \qquad (< 0 \text{ 自发},\ = 0 \text{ 平衡}).
$$
即在这些条件下系统的 Helmholtz 自由能只能减少，平衡时达到极小。

### 3.1.3. Gibbs 自由能

再设过程等温，且外压恒定、等于系统始末态的压力：$p_{\mathrm{ex}} = p_1 = p_2 = p$。体积功为 $-p\Delta V = -\Delta(pV)$，式 (3.1) 成为 $-\Delta(pV) + W' \ge \Delta A$，即

$$
W' \ge \Delta(A + pV) = \Delta(U + pV - TS) = \Delta(H - TS).
$$

**定义 3.1.2（Gibbs 自由能）** 状态函数

$$
G = H - TS = A + pV
$$
称为系统的 **Gibbs 自由能**。

**定理 3.1.3（最大非体积功）** 封闭系统的等温等压过程满足

$$
-W' \le -\Delta G, \tag{3.2}
$$
等号对可逆过程成立。即系统在等温等压过程中对外所能做的非体积功（电功、表面功等）最多等于其 Gibbs 自由能的减少。

**定理 3.1.4（Gibbs 自由能判据）** 封闭系统在等温、等压、不做非体积功的条件下，

$$
\Delta G \le 0 \qquad (< 0 \text{ 自发},\ = 0 \text{ 平衡}),
$$
系统总是向 Gibbs 自由能减小的方向变化，平衡时 $G$ 极小。

式 (3.2) 说明 $-\Delta G$ 是"可以转化为有用功的那部分能量"的上限，而不是系统所含的某种"化学能"：$-\Delta G = -\Delta H + T\Delta S$，其中 $-T\Delta S$ 一项是可逆过程中必须与热源交换的热。例如 $298.15\,\mathrm{K}$ 时 $\ce{H2(g) + 1/2O2(g) -> H2O(l)}$ 的 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -237.1\,\mathrm{kJ\,mol^{-1}}$，$\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = -285.8\,\mathrm{kJ\,mol^{-1}}$，燃料电池每摩尔反应最多输出 $237.1\,\mathrm{kJ}$ 电功，其余 $48.7\,\mathrm{kJ}$ 即使可逆进行也要以热的形式放给环境。反过来，**电解**水的 $\Delta G > 0$，它在等温等压下不能自发进行，必须由外界做至少 $\Delta G$ 的电功（$W' \ge \Delta G$）；这与"$\ce{H2}$ 与 $\ce{O2}$ 化合是自发过程"并不矛盾，两者是同一个反应的正逆两个方向。

**注 3.1.1** Clausius 不等式对任何过程都成立，包括电解：电解水时 $\Delta S \ge Q/T_{\mathrm{sur}}$ 同样满足，因为电功使大孤立系统（包括电源）的熵增加。"自发"指不需要外界做非体积功就能进行，Helmholtz 与 Gibbs 判据中的 $W' = 0$ 正是这一含义的数学表达。

### 3.1.4. 三个判据的比较

| 函数 | 系统 | 条件 | 判据（$<$ 不可逆，$=$ 可逆） |
|---|---|---|---|
| $S$ | 封闭系统 | 任意过程 | $\Delta S \ge \int \delta Q/T_{\mathrm{sur}}$ |
| $S$ | 孤立或绝热系统 | 任意过程 | $\Delta S \ge 0$ |
| $S$ | 系统 + 环境 | 任意过程 | $\Delta S + \Delta S_{\mathrm{sur}} \ge 0$ |
| $A$ | 封闭系统 | 等温 | $\Delta A \le W$ |
| $A$ | 封闭系统 | 等温、等容、$W' = 0$ | $\Delta A \le 0$ |
| $G$ | 封闭系统 | 等温、等压 | $\Delta G \le W'$ |
| $G$ | 封闭系统 | 等温、等压、$W' = 0$ | $\Delta G \le 0$ |

熵判据是根本，另外两个由它导出；化学中最常用的是 Gibbs 判据。使用时要注意条件的真正含义："等温"指系统只与一个恒温热源接触、始末态温度等于热源温度，"等压"指外压恒定且等于始末态压力。不满足这些条件时，即使算出 $\Delta G < 0$ 也不能断定过程自发（例 3.5.1、例 3.5.4）。

## 3.2. 热力学基本方程

### 3.2.1. 四个基本方程

考虑组成不变（或内部处于化学与相平衡）、不做非体积功的封闭系统中两个相邻的**平衡态**。沿连接它们的可逆途径，$\delta Q_{\mathrm{r}} = T\,\mathrm{d}S$，$\delta W_{\mathrm{r}} = -p\,\mathrm{d}V$，第一定律给出 $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$（[5.2.4 公式 4.5.1](/5.2.4#eq-4.2)）。对 $H = U + pV$、$A = U - TS$、$G = H - TS$ 取微分并代入，得到另外三个式子。

**定理 3.2.1（热力学基本方程）** 组成不变、只做体积功的封闭系统中，相邻两个平衡态的状态函数之间满足

$$
\begin{aligned}
\mathrm{d}U &= T\,\mathrm{d}S - p\,\mathrm{d}V, \\
\mathrm{d}H &= T\,\mathrm{d}S + V\,\mathrm{d}p, \\
\mathrm{d}A &= -S\,\mathrm{d}T - p\,\mathrm{d}V, \\
\mathrm{d}G &= -S\,\mathrm{d}T + V\,\mathrm{d}p.
\end{aligned}
\tag{3.3}
$$

**证明** 第一式见上。$\mathrm{d}H = \mathrm{d}U + p\,\mathrm{d}V + V\,\mathrm{d}p = T\,\mathrm{d}S + V\,\mathrm{d}p$；$\mathrm{d}A = \mathrm{d}U - T\,\mathrm{d}S - S\,\mathrm{d}T = -S\,\mathrm{d}T - p\,\mathrm{d}V$；$\mathrm{d}G = \mathrm{d}H - T\,\mathrm{d}S - S\,\mathrm{d}T = -S\,\mathrm{d}T + V\,\mathrm{d}p$。$\square$

基本方程的适用条件常被说得含糊，应当分清两件事：

1. 式 (3.3) 是状态函数之间的恒等关系。组成一定的均相封闭系统只有两个独立变量（双变量系统），$U$ 可以看成 $S$、$V$ 的函数，式 (3.3) 就是它的**全微分**。因此它对连接两个平衡态的任何过程都成立，与过程是否可逆无关：始末态相同的不可逆过程，可以用一条可逆途径代替来计算状态函数的改变。
2. 只有在可逆过程中才能把各项解释为热与功：$T\,\mathrm{d}S = \delta Q$，$-p\,\mathrm{d}V = \delta W$。不可逆过程中 $T\,\mathrm{d}S > \delta Q$（例如理想气体向真空膨胀，$\delta Q = 0$ 而 $T\,\mathrm{d}S = p\,\mathrm{d}V > 0$）。

"组成不变"这一条件不能省去。系统内发生化学反应或相变时，$U$ 还依赖于各物质的量，要加上 $\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ 一项（[6.3.4](/6.3.4)）。只有当反应或相变在平衡条件下进行（如正常沸点下的可逆蒸发），这一项为零，式 (3.3) 才照样成立；常说的"化学变化必须可逆才能用"指的正是这一点。由此也能解释一个常见的疑问：等温等压下 $\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p = 0$，似乎系统不能做非体积功，这与 $-\Delta G = -W'_{\max}$ 矛盾。实际上，能够对外做非体积功的等温等压过程（电池放电）必然伴随组成的变化，此时 $\mathrm{d}G = \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}} \neq 0$，式 (3.3) 的第四式不再适用。

可逆过程中 $\delta Q_{\mathrm{r}} = T\,\mathrm{d}S$，所以 $T$–$S$ 图上过程曲线下的面积就是可逆过程吸收的热，可逆循环所围的面积就是一个循环的净热与净功的绝对值（[5.2.4](/5.2.4#sec-4.9)）。

### 3.2.2. 自然变量与特性函数

式 (3.3) 中每个函数的微分都由另外两个变量的微分表示：$U$ 对应 $(S, V)$，$H$ 对应 $(S, p)$，$A$ 对应 $(T, V)$，$G$ 对应 $(T, p)$。这些变量称为相应函数的自然变量（natural variables）。

**定义 3.2.1（特性函数）** 若一个热力学函数用它的自然变量表示后，可以只通过求偏导与代数运算得到均相系统的全部热力学性质，则称它为**特性函数**。$U(S, V)$、$H(S, p)$、$A(T, V)$、$G(T, p)$ 都是特性函数。

以 $G(T, p)$ 为例，由式 (3.3)：

$$
S = -\left(\frac{\partial G}{\partial T}\right)_p, \quad V = \left(\frac{\partial G}{\partial p}\right)_T, \quad H = G - T\left(\frac{\partial G}{\partial T}\right)_p, \quad A = G - p\left(\frac{\partial G}{\partial p}\right)_T, \quad C_p = -T\left(\frac{\partial^2 G}{\partial T^2}\right)_p.
$$
例如知道 $n$ mol **理想气体**的 $G = n[\mu^\circ(T) + RT\ln(p/p^\circ)]$，就由 $V = (\partial G/\partial p)_T$ 得到物态方程 $pV = nRT$。同一个函数换用非自然变量就失去这一性质：$U(T, V)$ 不是特性函数，因为由 $(\partial U/\partial T)_V = C_V$ 只能得到热容，要得到 $S$ 还需对 $C_V/T$ 积分并引入积分常数，而 $p$ 根本无法由 $U(T, V)$ 求出。

### 3.2.3. Legendre 变换

由 $U(S, V)$ 得到 $A(T, V)$、$H(S, p)$、$G(T, p)$ 的运算有统一的数学形式。

**定义 3.2.2（Legendre 变换）** 设 $f(x)$ 是可微的严格凸函数，斜率 $\xi = f'(x)$ 随 $x$ 单调增加，因而 $x$ 可以反解为 $\xi$ 的函数。称

$$
g(\xi) = f(x) - \xi x \qquad (\xi = f'(x))
$$
为 $f$ 的 **Legendre 变换**。它满足 $\mathrm{d}g = -x\,\mathrm{d}\xi$，即 $g'(\xi) = -x$。多元函数对其中一个变量作 Legendre 变换时，其余变量保持为参数。

几何上，凸曲线 $y = f(x)$ 可以由它的全部切线确定（曲线是切线族的包络），而每条切线由斜率 $\xi$ 与纵截距 $f(x) - \xi x$ 确定。所以 $g(\xi)$ 与 $f(x)$ 包含同样的信息，只是换了自变量：用斜率代替原来的变量，而不像直接代入 $x = x(\xi)$ 那样丢掉信息。数学中常用的凸共轭 $f^*(\xi) = \sup_x[\xi x - f(x)]$ 与这里只差一个符号。

热力学中，$(\partial U/\partial S)_V = T$，所以 $A = U - TS$ 是 $U$ 对 $S$ 的 Legendre 变换，用 $T$ 代替 $S$；$(\partial U/\partial V)_S = -p$，所以 $H = U + pV$ 用 $p$ 代替 $V$；$G = U - TS + pV$ 同时变换两个变量。$U$ 对 $S$ 是凸函数（$(\partial^2 U/\partial S^2)_V = T/C_V > 0$），这保证了变换可逆。

![一摩尔单原子理想气体在固定体积下的 $U(S)$ 是凸函数（左）。斜率为 $T$ 的切线在 $S = 0$ 处的截距就是 $A = U - TS$；把所有切线的截距作为 $T$ 的函数，得到 $A(T)$（右），其斜率为 $-S$。$U$ 与 $A$ 的零点任意。](./plots/legendre-transform.py)

| 函数 | 定义 | 自然变量 | 基本方程 | 用途 |
|---|---|---|---|---|
| $U$ | — | $S, V$ | $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ | 孤立系统；统计热力学 |
| $H$ | $U + pV$ | $S, p$ | $\mathrm{d}H = T\,\mathrm{d}S + V\,\mathrm{d}p$ | 等压热效应 $Q_p = \Delta H$ |
| $A$ | $U - TS$ | $T, V$ | $\mathrm{d}A = -S\,\mathrm{d}T - p\,\mathrm{d}V$ | 等温等容判据；$A = -k_{\mathrm{B}}T\ln Z$（[6.3.10](/6.3.10)） |
| $G$ | $H - TS$ | $T, p$ | $\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p$ | 等温等压判据；化学平衡与相平衡 |

实验中容易控制的是 $T$ 与 $p$，而不是 $S$ 与 $V$，这就是化学热力学以 $G$ 为中心的原因。

## 3.3. 对应系数关系与 Maxwell 关系

### 3.3.1. 对应系数关系

把 $U$ 看成 $S$、$V$ 的函数，$\mathrm{d}U = (\partial U/\partial S)_V\,\mathrm{d}S + (\partial U/\partial V)_S\,\mathrm{d}V$，与式 (3.3) 逐项比较系数，得到对应系数关系：

**公式 3.3.1（对应系数关系）**

$$
\begin{aligned}
\left(\frac{\partial U}{\partial S}\right)_V &= \left(\frac{\partial H}{\partial S}\right)_p = T, &
\left(\frac{\partial U}{\partial V}\right)_S &= \left(\frac{\partial A}{\partial V}\right)_T = -p, \\
\left(\frac{\partial H}{\partial p}\right)_S &= \left(\frac{\partial G}{\partial p}\right)_T = V, &
\left(\frac{\partial A}{\partial T}\right)_V &= \left(\frac{\partial G}{\partial T}\right)_p = -S.
\end{aligned}
$$

第一式可以看作热力学温度的定义：$T$ 是体积不变时内能随熵的变化率。这些关系对任意平衡态成立，常用于证明题与分析问题。

### 3.3.2. Maxwell 关系

**定理 3.3.1（Maxwell 关系）** 组成不变的封闭系统中，

$$
\begin{aligned}
\left(\frac{\partial T}{\partial V}\right)_S &= -\left(\frac{\partial p}{\partial S}\right)_V, &
\left(\frac{\partial T}{\partial p}\right)_S &= \left(\frac{\partial V}{\partial S}\right)_p, \\
\left(\frac{\partial S}{\partial V}\right)_T &= \left(\frac{\partial p}{\partial T}\right)_V, &
\left(\frac{\partial S}{\partial p}\right)_T &= -\left(\frac{\partial V}{\partial T}\right)_p.
\end{aligned}
\tag{3.4}
$$

**证明** 以第三式为例。$A(T, V)$ 有连续的二阶偏导数，由对应系数关系 $(\partial A/\partial T)_V = -S$、$(\partial A/\partial V)_T = -p$，而混合偏导数与求导次序无关（[2.2.10 定理 10.4.1](/2.2.10#thm-10.4.1)），

$$
-\left(\frac{\partial S}{\partial V}\right)_T = \frac{\partial^2 A}{\partial V\,\partial T} = \frac{\partial^2 A}{\partial T\,\partial V} = -\left(\frac{\partial p}{\partial T}\right)_V.
$$
其余三式分别由 $U$、$H$、$G$ 得到。$\square$

换一种说法：$M\,\mathrm{d}x + N\,\mathrm{d}y$ 是某个函数的全微分，当且仅当 $(\partial M/\partial y)_x = (\partial N/\partial x)_y$（**全微分方程**的判别条件，[2.2.15 定理 15.4.1](/2.2.15#thm-15.4.1)）。$\delta Q_{\mathrm{r}}$ 不满足这个条件，乘上**积分因子** $1/T$ 之后的 $\mathrm{d}S$ 才满足；Maxwell 关系就是 $\mathrm{d}U$、$\mathrm{d}H$、$\mathrm{d}A$、$\mathrm{d}G$ 都是全微分这一事实的直接表达。

记忆方法：每个式子的两边，分子与下标合起来恰是两对共轭变量 $(T, S)$、$(p, V)$，且 $T$ 与 $S$、$p$ 与 $V$ 分处对角；偏导数的两个自变量（分母与下标）是 $S$ 与 $V$ 或 $T$ 与 $p$ 时带负号，即由 $U(S, V)$ 与 $G(T, p)$ 得到的两式。Maxwell 关系的用处在于以易测量代替难测量：后两式把熵随体积、压力的变化化为 $p$–$V$–$T$ 数据，熵本身不能直接测量。

### 3.3.3. 偏导数的运算工具

热力学证明大多只用到下面几个工具：基本方程与定义式；对恒等式两端求导，或把微分式在某些变量不变时除以另一个量的微分；比较系数；以及下面三个关系。设 $x$、$y$、$z$ 之间有一个函数关系 $F(x, y, z) = 0$，且各偏导数不为零（由**隐函数定理**，[2.2.10](/2.2.10#sec-10.8.1)），则

$$
\left(\frac{\partial x}{\partial y}\right)_z = \frac{1}{(\partial y/\partial x)_z}, \qquad
\left(\frac{\partial x}{\partial y}\right)_z\left(\frac{\partial y}{\partial z}\right)_x\left(\frac{\partial z}{\partial x}\right)_y = -1,
\tag{3.5}
$$
后者称为循环关系。证明：$x$、$y$、$z$ 中任两个可作自变量，$\mathrm{d}x = (\partial x/\partial y)_z\,\mathrm{d}y + (\partial x/\partial z)_y\,\mathrm{d}z$；取 $\mathrm{d}x = 0$ 得 $(\partial z/\partial y)_x = -(\partial x/\partial y)_z/(\partial x/\partial z)_y$，再用倒数关系整理即得。[2.2.10](/2.2.10#sec-10.4.1) 中已用 $pV = RT$ 验证过三个偏导数之积为 $-1$。另一个常用的关系是换下标（链关系）：若 $z = z(x, y)$，而 $y$ 又随 $x$ 沿 $u$ 不变的途径变化，则

$$
\left(\frac{\partial z}{\partial x}\right)_u = \left(\frac{\partial z}{\partial x}\right)_y + \left(\frac{\partial z}{\partial y}\right)_x\left(\frac{\partial y}{\partial x}\right)_u.
\tag{3.6}
$$

最常用的可测量是下面两个系数。

**定义 3.3.1** 称

$$
\alpha_V = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_p, \qquad \kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_T
$$
分别为物质的**等压热膨胀系数**与**等温压缩系数**，单位 $\mathrm{K^{-1}}$ 与 $\mathrm{Pa^{-1}}$。

由循环关系，$(\partial p/\partial T)_V = -(\partial V/\partial T)_p/(\partial V/\partial p)_T = \alpha_V/\kappa_T$。理想气体 $\alpha_V = 1/T$，$\kappa_T = 1/p$。$25\,^\circ\mathrm{C}$ 的液态水 $\alpha_V = 2.57 \times 10^{-4}\,\mathrm{K^{-1}}$，$\kappa_T = 4.52 \times 10^{-10}\,\mathrm{Pa^{-1}}$，所以要使水在加热 $1\,\mathrm{K}$ 时体积不变，需要加压 $\alpha_V/\kappa_T \approx 0.57\,\mathrm{MPa}$：这就是密闭的满液容器受热时容易胀裂的原因。

## 3.4. 基本关系的应用

### 3.4.1. 热力学状态方程

**定理 3.4.1（热力学状态方程）** 对任意物质，

$$
\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial p}{\partial T}\right)_V - p, \qquad
\left(\frac{\partial H}{\partial p}\right)_T = V - T\left(\frac{\partial V}{\partial T}\right)_p.
\tag{3.7}
$$

**证明** 在 $T$ 不变时用 $\mathrm{d}V$ 除 $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$，得 $(\partial U/\partial V)_T = T(\partial S/\partial V)_T - p$，再用 Maxwell 关系 $(\partial S/\partial V)_T = (\partial p/\partial T)_V$。第二式由 $\mathrm{d}H = T\,\mathrm{d}S + V\,\mathrm{d}p$ 与 $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ 同样得到。$\square$

式 (3.7) 把内能、焓随体积与压力的变化完全归结为物态方程 $p(T, V)$，这是第二定律对物态方程的约束。几个推论：

- **理想气体**：$(\partial p/\partial T)_V = nR/V$，故 $(\partial U/\partial V)_T = nRT/V - p = 0$，同理 $(\partial H/\partial p)_T = 0$。在 [5.2.3](/5.2.3#sec-3.3.4) 中"理想气体的内能只是温度的函数"是 Joule 实验的经验结论，这里它由物态方程 $pV = nRT$（$T$ 为热力学温度）与第二定律推出。
- van der Waals 气体：由 $p = nRT/(V - nb) - an^2/V^2$ 得 $(\partial U/\partial V)_T = an^2/V^2$，即 **van der Waals 方程**中的 $a$ 项就是**内压**（[6.3.1](/6.3.1)）。又 $(\partial C_V/\partial V)_T = T(\partial^2 p/\partial T^2)_V = 0$，所以 vdW 气体的 $C_V$ 也只是温度的函数，等温膨胀时 $\Delta U = -an^2(1/V_2 - 1/V_1)$。
- 一般地，$U = U(T, V)$、$H = H(T, p)$ 时
  $$
  \mathrm{d}U = C_V\,\mathrm{d}T + \left[T\left(\frac{\partial p}{\partial T}\right)_V - p\right]\mathrm{d}V, \qquad \mathrm{d}H = C_p\,\mathrm{d}T + \left[V - T\left(\frac{\partial V}{\partial T}\right)_p\right]\mathrm{d}p,
  $$
  有物态方程就能算出实际气体任意状态变化的 $\Delta U$、$\Delta H$；没有物态方程时，可由实验测量的 $(\partial U/\partial V)_T$、$(\partial H/\partial p)_T$ 反过来检验物态方程。
- **Joule–Thomson 系数**：$\mu_{\mathrm{JT}} = (\partial T/\partial p)_H = -(\partial H/\partial p)_T/C_p$（循环关系），代入式 (3.7) 得 $\mu_{\mathrm{JT}} = V(T\alpha_V - 1)/C_p$。理想气体 $T\alpha_V = 1$，节流后温度不变；$T\alpha_V > 1$ 时节流降温（[6.3.1](/6.3.1)）。

### 3.4.2. $C_p$ 与 $C_V$ 的关系

**定理 3.4.2** 对任意物质，

$$
C_p - C_V = T\left(\frac{\partial p}{\partial T}\right)_V\left(\frac{\partial V}{\partial T}\right)_p = \frac{TV\alpha_V^2}{\kappa_T}.
\tag{3.8}
$$

**证明** 由 $H = U + pV$ 与链关系 (3.6)（以 $U(T, V)$ 沿 $p$ 不变的途径求导），

$$
C_p - C_V = \left(\frac{\partial U}{\partial T}\right)_p + p\left(\frac{\partial V}{\partial T}\right)_p - \left(\frac{\partial U}{\partial T}\right)_V = \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\left(\frac{\partial V}{\partial T}\right)_p.
$$
代入式 (3.7) 得第一个等号，再用 $(\partial p/\partial T)_V = \alpha_V/\kappa_T$、$(\partial V/\partial T)_p = V\alpha_V$ 得第二个等号。$\square$

式 (3.8) 中右端第一个因子 $(\partial U/\partial V)_T + p$ 是等压升温时系统体积膨胀所需的额外能量：一部分克服分子间吸引（内压），一部分对外做功。由式 (3.8)：

1. 平衡态的稳定性要求 $\kappa_T > 0$，而 $T$、$V$、$\alpha_V^2$ 都非负，所以总有 $C_p \ge C_V$。
2. $\alpha_V = 0$ 时 $C_p = C_V$，例如液态水在 $3.98\,^\circ\mathrm{C}$（密度最大处）。
3. $T \to 0$ 时 $C_p - C_V \to 0$。
4. 理想气体 $C_p - C_V = nR$，即 Mayer 公式（[5.2.3](/5.2.3#sec-3.4.3)）。

凝聚相的 $\alpha_V$ 小，$C_p$ 与 $C_V$ 相差很少。$25\,^\circ\mathrm{C}$ 的液态水 $V_{\mathrm{m}} = 18.07\,\mathrm{cm^3\,mol^{-1}}$，代入上面的 $\alpha_V$、$\kappa_T$ 得 $C_{p,\mathrm{m}} - C_{V,\mathrm{m}} = 0.79\,\mathrm{J\,mol^{-1}\,K^{-1}}$，只占 $C_{p,\mathrm{m}} = 75.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$ 的 1%。凝聚相的 $C_V$ 很难直接测量（加热时要维持体积不变需要极大的压力），实验测的是 $C_p$，理论（如晶格振动的 Debye 模型）给出的是 $C_V$，式 (3.8) 正是两者之间的换算。

![液态水（1 bar）的等压热膨胀系数（左，在 3.98 °C 变号）与 $C_{p,\mathrm{m}} - C_{V,\mathrm{m}}$（右），由 Kell 的密度与压缩系数拟合式计算。](./plots/water-cp-cv.py)

### 3.4.3. 绝热可逆膨胀时压力必然降低

**例 3.4.1** 已知平衡态的稳定性条件 $(\partial p/\partial V)_T < 0$、$C_V > 0$。证明任何物质绝热可逆膨胀后压力降低，即 $(\partial p/\partial V)_S < 0$。

**解** 绝热可逆过程是**等熵过程**。由循环关系与链关系，

$$
\left(\frac{\partial p}{\partial V}\right)_S = -\frac{(\partial S/\partial V)_p}{(\partial S/\partial p)_V}
= -\frac{(\partial S/\partial T)_p(\partial T/\partial V)_p}{(\partial S/\partial T)_V(\partial T/\partial p)_V}
= \frac{C_p/T}{C_V/T}\cdot\left[-\frac{(\partial p/\partial T)_V}{(\partial V/\partial T)_p}\right]
= \frac{C_p}{C_V}\left(\frac{\partial p}{\partial V}\right)_T,
$$
其中用到 $(\partial S/\partial T)_p = C_p/T$、$(\partial S/\partial T)_V = C_V/T$ 与循环关系 $-(\partial p/\partial T)_V/(\partial V/\partial T)_p = (\partial p/\partial V)_T$。因为 $C_p \ge C_V > 0$、$(\partial p/\partial V)_T < 0$，所以 $(\partial p/\partial V)_S < 0$。$\square$

结果说明，绝热压缩系数 $\kappa_S = -\frac{1}{V}(\partial V/\partial p)_S$ 与等温压缩系数之比为 $\kappa_T/\kappa_S = C_p/C_V$。对理想气体 $C_p/C_V$ 就是**比热容比** $\gamma$，绝热线比等温线陡 $\gamma$ 倍（[5.2.3](/5.2.3#sec-3.5.1)）；这里的结论对任何物质都成立。

### 3.4.4. 温度与压力对热力学函数的影响

由基本方程、热容的定义、Maxwell 关系与式 (3.7)，各状态函数随 $T$、$p$ 的变化为：

| $X$ | $(\partial X/\partial T)_p$ | $(\partial X/\partial p)_T$ |
|---|---|---|
| $U$ | $C_p - pV\alpha_V$ | $pV\kappa_T - TV\alpha_V$ |
| $H$ | $C_p$ | $V(1 - T\alpha_V)$ |
| $S$ | $C_p/T$ | $-V\alpha_V$ |
| $A$ | $-S - pV\alpha_V$ | $pV\kappa_T$ |
| $G$ | $-S$ | $V$ |

温度对所有函数的影响都显著，不能忽略。压力的影响因相态而异：气体的 $V$ 大，$S$、$A$、$G$ 随压力变化显著（理想气体的 $U$、$H$ 与压力无关）；液体和固体的 $V$、$\alpha_V$、$\kappa_T$ 都很小，压力变化不大时 $\Delta U$、$\Delta H$、$\Delta S$、$\Delta A$、$\Delta G$ 都可以近似为零。例如 $298\,\mathrm{K}$ 下压力从 $1\,\mathrm{bar}$ 增至 $100\,\mathrm{bar}$，$1\,\mathrm{mol}$ 液态水的 $\Delta G = V_{\mathrm{m}}\Delta p \approx 0.18\,\mathrm{kJ}$，而 $1\,\mathrm{mol}$ 理想气体的 $\Delta G = RT\ln 100 = 11.4\,\mathrm{kJ}$。

## 3.5. ΔG 与 ΔA 的计算

### 3.5.1. 基本方法

$\Delta G$、$\Delta A$ 是状态函数的改变量，只取决于始末态。计算的出发点有四个：

1. 定义式：封闭系统的任意等温过程 $\Delta G = \Delta H - T\Delta S$，$\Delta A = \Delta U - T\Delta S$。
2. 基本方程：组成不变的简单 $pVT$ 变化，$\Delta G = \int(-S\,\mathrm{d}T + V\,\mathrm{d}p)$，$\Delta A = \int(-S\,\mathrm{d}T - p\,\mathrm{d}V)$。
3. 与功的关系：等温可逆过程 $\Delta A = W$；等温等容可逆过程 $\Delta A = W'$；等温等压可逆过程 $\Delta G = W'$。
4. Gibbs–Helmholtz 方程（3.6）：由一个温度下的 $\Delta G$ 求另一个温度下的 $\Delta G$。

一个问题往往可以同时套用几个公式；实际过程无公式可用时，就设计始末态相同、由可逆步骤组成的途径。

### 3.5.2. 理想气体的等温过程

理想气体等温时 $\Delta U = \Delta H = 0$，由 $\mathrm{d}G = V\,\mathrm{d}p$：

$$
\Delta G = \Delta A = nRT\ln\frac{p_2}{p_1} = nRT\ln\frac{V_1}{V_2} = -T\Delta S.
$$
最后一个等号只对等温过程成立：变温时理想气体的 $\Delta H \ne 0$，$\Delta G \ne -T\Delta S$。

**例 3.5.1** $300.2\,\mathrm{K}$ 时 $1\,\mathrm{mol}$ 理想气体从 $10p^\circ$ 分别经 (1) 等温可逆膨胀、(2) 向真空膨胀到 $p^\circ$。求两个过程的 $Q$、$W$、$\Delta U$、$\Delta H$、$\Delta S$、$\Delta A$、$\Delta G$。

**解** (1) $\Delta U = \Delta H = 0$；$Q = -W = nRT\ln(p_1/p_2) = 8.314 \times 300.2 \times \ln 10\,\mathrm{J} = 5747\,\mathrm{J}$；$\Delta S = nR\ln(p_1/p_2) = 19.14\,\mathrm{J\,K^{-1}}$；$\Delta G = \Delta A = -T\Delta S = -5747\,\mathrm{J}$，且 $\Delta A = W$（等温可逆）。

(2) $W = 0$，$Q = \Delta U = 0$；其余状态函数的改变与 (1) 相同。

过程 (2) 中 $\Delta G < 0$，但不能据此用 Gibbs 判据说它自发：压力从 $10p^\circ$ 变到 $p^\circ$，不满足等压条件。应当用孤立系统的熵判据：$\Delta S_{\mathrm{sur}} = -Q/T = 0$，$\Delta S + \Delta S_{\mathrm{sur}} = 19.14\,\mathrm{J\,K^{-1}} > 0$，过程不可逆且自发。

### 3.5.3. 变温过程与 $pVT$ 同时变化

等压变温时 $\Delta G = -\int_{T_1}^{T_2}S\,\mathrm{d}T$，被积函数是熵本身而不是熵变，必须知道 $S$ 的绝对值（由**热力学第三定律**和**标准摩尔熵**得到）：

$$
S(T) = S(T_0) + \int_{T_0}^{T}\frac{C_p}{T}\,\mathrm{d}T.
$$
也就是说，变温过程的 $\Delta G$ 不仅取决于热容，还取决于熵的零点；这与等温过程不同，后者只用到熵变。因此计算等温的相变或反应时，一般不要设计变温步骤来直接求 $\Delta G$（例 3.5.3 解法 1 中 $\Delta G$ 由 $\Delta H$ 与 $\Delta S$ 合成，而不是逐步相加）。

**例 3.5.2** 已知 $S^\circ_{\mathrm{m}}(\mathrm{He}, 298.2\,\mathrm{K}) = 126.06\,\mathrm{J\,mol^{-1}\,K^{-1}}$。求 $1\,\mathrm{mol}$ He 从 $298.2\,\mathrm{K}$、$10p^\circ$ 绝热可逆膨胀到 $p^\circ$ 的 $\Delta G$（He 视为理想气体，$C_{p,\mathrm{m}} = \frac52 R$）。

**解** 由绝热可逆方程 $T^\gamma p^{1-\gamma} = $ 常数（$\gamma = 5/3$），

$$
T_2 = T_1\left(\frac{p_2}{p_1}\right)^{(\gamma-1)/\gamma} = 298.2 \times 10^{-0.4}\,\mathrm{K} = 118.7\,\mathrm{K}.
$$
过程等熵，$S$ 保持为始态的熵：$S = S^\circ_{\mathrm{m}} + R\ln(p^\circ/10p^\circ) = (126.06 - 19.14)\,\mathrm{J\,K^{-1}} = 106.92\,\mathrm{J\,K^{-1}}$。于是 $\Delta(TS) = S\,\Delta T$，

$$
\Delta G = \Delta H - S\,\Delta T = \left[\tfrac52 \times 8.314 \times (-179.5) - 106.92 \times (-179.5)\right]\mathrm{J} = (-3731 + 19193)\,\mathrm{J} = 15.46\,\mathrm{kJ}.
$$
也可以由基本方程计算：$\Delta G = \int(-S\,\mathrm{d}T + V\,\mathrm{d}p) = -S\Delta T + \int V\,\mathrm{d}p$，而等熵过程中 $\int V\,\mathrm{d}p = \Delta H$，结果相同。$\square$

这里 $\Delta G > 0$ 同样不表示过程不能发生：它既不等温也不等压。

### 3.5.4. 相变

在正常相变点进行的可逆相变是等温等压、$W' = 0$ 的可逆过程，$\Delta G = 0$，$\Delta A = W = -p\Delta V$（蒸发时 $\approx -nRT$）。不在相平衡条件下的相变是不可逆的，要设计途径。

**例 3.5.3** 求 $298.15\,\mathrm{K}$、$p^\circ$ 下 $1\,\mathrm{mol}$ $\ce{H2O(l)}$ 完全汽化为同温同压的 $\ce{H2O(g)}$ 的 $\Delta G$。已知 $C_{p,\mathrm{m}}(\mathrm{l}) = 75\,\mathrm{J\,mol^{-1}\,K^{-1}}$，$C_{p,\mathrm{m}}(\mathrm{g}) = 33\,\mathrm{J\,mol^{-1}\,K^{-1}}$，$298.15\,\mathrm{K}$ 时水的**饱和蒸气压**为 $3160\,\mathrm{Pa}$，$\Delta_{\mathrm{vap}}H_{\mathrm{m}}(373.15\,\mathrm{K}) = 40.65\,\mathrm{kJ\,mol^{-1}}$（为简化，把 $373.15\,\mathrm{K}$、$p^\circ$ 当作两相平衡点）。

解法 1（分别求 $\Delta H$ 与 $\Delta S$）：设计途径，液态水等压升温到 $373.15\,\mathrm{K}$，可逆汽化，水蒸气等压降温回 $298.15\,\mathrm{K}$。

$$
\begin{aligned}
\Delta H &= [75 \times 75 + 40650 + 33 \times (-75)]\,\mathrm{J} = 43.80\,\mathrm{kJ}, \\
\Delta S &= \left[75\ln\frac{373.15}{298.15} + \frac{40650}{373.15} + 33\ln\frac{298.15}{373.15}\right]\mathrm{J\,K^{-1}} = 118.36\,\mathrm{J\,K^{-1}}, \\
\Delta G &= \Delta H - T\Delta S = (43800 - 298.15 \times 118.36)\,\mathrm{J} = 8.51\,\mathrm{kJ}.
\end{aligned}
$$
焓不利而熵有利，焓占主导，$\Delta G > 0$：$298.15\,\mathrm{K}$ 时 $p^\circ$ 下的水不会自发汽化成 $p^\circ$ 的水蒸气。

解法 2（等温变压）：设计途径，液态水从 $p^\circ$ 降压到饱和蒸气压 $3160\,\mathrm{Pa}$，在该压力下可逆汽化（$\Delta G = 0$），水蒸气再等温压缩到 $p^\circ$。液体的 $\Delta G$ 随压力的变化可以忽略（3.4.4），水蒸气视为理想气体：

$$
\Delta G \approx \int_{3160\,\mathrm{Pa}}^{p^\circ}V_{\mathrm{m}}(\mathrm{g})\,\mathrm{d}p = RT\ln\frac{p^\circ}{3160\,\mathrm{Pa}} = 8.314 \times 298.15 \times \ln\frac{10^5}{3160}\,\mathrm{J} = 8.56\,\mathrm{kJ}.
$$

解法 3（Gibbs–Helmholtz 方程）：见例 3.6.1，结果与解法 1 完全相同。$\square$

两种结果相差 $0.05\,\mathrm{kJ}$，来源不同：解法 1 与解法 3 假定两相的热容在 $298$–$373\,\mathrm{K}$ 为常数，并且把 $1\,\mathrm{bar}$ 当作 $373.15\,\mathrm{K}$ 的平衡压力（实际 $1\,\mathrm{bar}$ 下的沸点是 $372.76\,\mathrm{K}$）；解法 2 只用到实测的蒸气压和"蒸气是理想气体"的近似，数据更直接。由 CRC 手册的标准生成 Gibbs 自由能，$\Delta_{\mathrm{f}}G^\circ(\ce{H2O}, \mathrm{g}) - \Delta_{\mathrm{f}}G^\circ(\ce{H2O}, \mathrm{l}) = (-228.6) - (-237.1) = 8.5\,\mathrm{kJ\,mol^{-1}}$，与两种解法都一致。解法 2 也说明，题中"$298.15\,\mathrm{K}$ 时的蒸气压"不是多余的条件。

**例 3.5.4** $1\,\mathrm{mol}$ 液态苯在 $343.3\,\mathrm{K}$ 下向真空容器蒸发，末态为 $343.3\,\mathrm{K}$、$101.325\,\mathrm{kPa}$ 的苯蒸气，不做非体积功。已知苯的正常沸点 $353.3\,\mathrm{K}$，此时 $\Delta_{\mathrm{vap}}H_{\mathrm{m}} = 30.85\,\mathrm{kJ\,mol^{-1}}$，$C_{p,\mathrm{m}}(\mathrm{l}) = 135.10\,\mathrm{J\,mol^{-1}\,K^{-1}}$，$C_{p,\mathrm{m}}(\mathrm{g}) = 81.76\,\mathrm{J\,mol^{-1}\,K^{-1}}$。求 $Q$、$W$、$\Delta U$、$\Delta H$、$\Delta S$、$\Delta A$、$\Delta G$，并判断过程的方向。

**解** 状态函数沿途径"液体升温到 $353.3\,\mathrm{K}$ → 可逆蒸发 → 蒸气降温到 $343.3\,\mathrm{K}$"（均在 $101.325\,\mathrm{kPa}$）计算：

$$
\begin{aligned}
\Delta H &= [30850 + (135.10 - 81.76) \times 10]\,\mathrm{J} = 31.38\,\mathrm{kJ}, \\
\Delta S &= \left[(135.10 - 81.76)\ln\frac{353.3}{343.3} + \frac{30850}{353.3}\right]\mathrm{J\,K^{-1}} = 88.85\,\mathrm{J\,K^{-1}}, \\
\Delta G &= \Delta H - T\Delta S = (31383 - 343.3 \times 88.85)\,\mathrm{J} = 0.88\,\mathrm{kJ}.
\end{aligned}
$$
忽略液体体积、蒸气视为理想气体，$\Delta U = \Delta H - \Delta(pV) \approx \Delta H - nRT = 28.53\,\mathrm{kJ}$，$\Delta A = \Delta U - T\Delta S = -1.97\,\mathrm{kJ}$。实际过程向真空蒸发，$W = 0$，$Q = \Delta U = 28.53\,\mathrm{kJ}$。

判断方向：过程不等压，$\Delta G > 0$ 不能用来判断。环境熵变 $\Delta S_{\mathrm{sur}} = -Q/T = -83.10\,\mathrm{J\,K^{-1}}$，总熵变 $\Delta S + \Delta S_{\mathrm{sur}} = 5.75\,\mathrm{J\,K^{-1}} > 0$，过程自发。另一种看法：把苯与真空容器合起来作系统，过程等温、总体积不变、$W' = 0$，Helmholtz 判据 $\Delta A < 0$ 给出同样的结论。$\square$

$\Delta G = 0.88\,\mathrm{kJ} > 0$ 也有意义：末态的蒸气在 $343.3\,\mathrm{K}$ 下压力高于苯的饱和蒸气压。由 $\Delta G = RT\ln(p/p^*)$ 估计 $343.3\,\mathrm{K}$ 时苯的蒸气压 $p^* \approx 101.3\,\mathrm{kPa} \times \mathrm{e}^{-0.31} \approx 74\,\mathrm{kPa}$，末态是过饱和蒸气。

### 3.5.5. 混合过程

不同理想气体在等温等压下混合，$\Delta_{\mathrm{mix}}H = 0$，由**混合熵** $\Delta_{\mathrm{mix}}S = -R\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}$（[6.3.2](/6.3.2)）得

$$
\Delta_{\mathrm{mix}}G = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}} < 0.
$$
这一结果只适用于不同理想气体的等温等压混合；其他混合过程（如两种气体始态压力不同）先分别求各气体的 $\Delta G_{\mathrm{B}}$，再相加。混合物中各组分的 Gibbs 自由能由化学势描述，用它推导上式见 [6.3.4](/6.3.4)。

### 3.5.6. 化学反应

标准态下的等温反应 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}(T) = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(T) - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(T)$，$298.15\,\mathrm{K}$ 的 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$、$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 由手册中的**标准摩尔生成焓**与**标准摩尔熵**求得，或直接由**标准摩尔生成 Gibbs 自由能**求得（[6.1.6](/6.1.6#sec-6.4.8)）。其他温度下的值由 **Kirchhoff 定律**（[6.3.1](/6.3.1)）校正 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$、$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$，或用 Gibbs–Helmholtz 方程（3.6）。非标准态下的 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 与平衡常数见 [6.3.7](/6.3.7)。

### 3.5.7. 凝聚相的压力效应

凝聚相的 $\Delta G$ 随压力变化虽小，压力足够高时却能改变相的稳定性。由 $(\partial\Delta G/\partial p)_T = \Delta V$：

**例 3.5.5** $298.15\,\mathrm{K}$、$p^\circ$ 下 $\ce{C(石墨) -> C(金刚石)}$ 的 $\Delta_{\mathrm{trs}}G^\circ_{\mathrm{m}} = 2.900\,\mathrm{kJ\,mol^{-1}}$（CRC，与 [6.1.14](/6.1.14) 一致），金刚石与石墨的密度分别为 $3513\,\mathrm{kg\,m^{-3}}$ 与 $2260\,\mathrm{kg\,m^{-3}}$。$298.15\,\mathrm{K}$ 下至少要加多大压力，石墨才可能转变为金刚石？

**解** $\Delta V_{\mathrm{m}} = M(1/\rho_{\text{金刚石}} - 1/\rho_{\text{石墨}}) = 12.011 \times 10^{-3} \times (1/3513 - 1/2260)\,\mathrm{m^3\,mol^{-1}} = -1.896 \times 10^{-6}\,\mathrm{m^3\,mol^{-1}}$。设 $\Delta V_{\mathrm{m}}$ 不随压力变化，

$$
\Delta_{\mathrm{trs}}G_{\mathrm{m}}(p) = \Delta_{\mathrm{trs}}G^\circ_{\mathrm{m}} + \Delta V_{\mathrm{m}}(p - p^\circ) = 0 \;\Longrightarrow\; p = p^\circ - \frac{\Delta_{\mathrm{trs}}G^\circ_{\mathrm{m}}}{\Delta V_{\mathrm{m}}} = 1.53 \times 10^9\,\mathrm{Pa}.
$$
即室温下约 $1.5\,\mathrm{GPa}$ 以上金刚石才比石墨稳定。$\square$

再由 $(\partial\Delta G/\partial T)_p = -\Delta S$（$\Delta_{\mathrm{trs}}S^\circ_{\mathrm{m}} = 2.38 - 5.74 = -3.36\,\mathrm{J\,mol^{-1}\,K^{-1}}$），升温使平衡压力升高，相界的斜率 $\mathrm{d}p/\mathrm{d}T = \Delta S/\Delta V \approx 1.8\,\mathrm{MPa\,K^{-1}}$（这就是 [6.3.8](/6.3.8) 的 Clapeyron 方程）。高温下 $\Delta S$、$\Delta V$ 本身随温度变化，实验测得的相界（Berman–Simon 线）更陡。热力学只说明高压有利于金刚石；石墨在常温下转变的活化能极高，实际合成要在 $5$–$6\,\mathrm{GPa}$、$1600$–$2100\,\mathrm{K}$ 下借助熔融金属（Fe、Ni、Co）作溶剂与催化剂。低压化学气相沉积（CVD）生长的金刚石处于亚稳状态，靠的是表面反应的动力学选择，而不是改变了热力学平衡。

![石墨–金刚石转变：298.15 K 时 $\Delta_{\mathrm{trs}}G_{\mathrm{m}}$ 随压力的变化（左，设 $\Delta V$ 为常数）；两相平衡线（右）：本节的常数 $\Delta S$、$\Delta V$ 近似与实验的 Berman–Simon 线，以及工业高温高压合成的大致范围。](./plots/graphite-diamond.py)

## 3.6. Gibbs–Helmholtz 方程

化学反应的 $\Delta_{\mathrm{r}}G$ 常常只知道一个温度下的值，要求其他温度下的值。

**定理 3.6.1（Gibbs–Helmholtz 方程）** 对组成不变的封闭系统的任一平衡态，

$$
\left[\frac{\partial(G/T)}{\partial T}\right]_p = -\frac{H}{T^2}, \qquad \left[\frac{\partial(A/T)}{\partial T}\right]_V = -\frac{U}{T^2}.
\tag{3.9}
$$
对始末态温度相同、压力相同的过程（相变、化学反应），

$$
\left[\frac{\partial(\Delta G/T)}{\partial T}\right]_p = -\frac{\Delta H}{T^2}.
\tag{3.10}
$$

**证明** 由商的求导法则与 $(\partial G/\partial T)_p = -S$，

$$
\left[\frac{\partial(G/T)}{\partial T}\right]_p = \frac{T(\partial G/\partial T)_p - G}{T^2} = \frac{-TS - G}{T^2} = -\frac{H}{T^2}.
$$
$A/T$ 的情形相同，用 $(\partial A/\partial T)_V = -S$ 与 $A + TS = U$。对过程，始态与末态分别满足式 (3.9)，两式相减即得式 (3.10)。$\square$

式 (3.10) 也可写成 $[\partial(\Delta G/T)/\partial(1/T)]_p = \Delta H$：$\Delta G/T$ 对 $1/T$ 作图，斜率就是 $\Delta H$。$\Delta G/T$ 这个组合有直接的意义：等温等压、$W' = 0$ 时 $-\Delta G/T = \Delta S + \Delta S_{\mathrm{sur}}$ 是大孤立系统的总熵变（[6.1.6](/6.1.6#sec-6.4.7)），因此式 (3.10) 描述的是总熵变随温度的变化。

注意区分 $(\partial G/\partial T)_p = -S$ 与式 (3.9)：前者是 $G$ 本身的温度系数，要用到熵的绝对值；后者是 $G/T$ 的温度系数，只用到焓，而焓（或 $\Delta H$）可以由量热测定。这就是由一个温度下的 $\Delta G$ 推算另一温度下的 $\Delta G$ 时要用式 (3.10) 的原因。在等压下积分：

$$
\frac{\Delta G(T_2)}{T_2} = \frac{\Delta G(T_1)}{T_1} - \int_{T_1}^{T_2}\frac{\Delta H(T)}{T^2}\,\mathrm{d}T.
\tag{3.11}
$$
若 $\Delta H$ 与温度无关，$\Delta G(T_2)/T_2 = \Delta G(T_1)/T_1 + \Delta H(1/T_2 - 1/T_1)$；若 $\Delta C_p$ 为常数，由 Kirchhoff 定律 $\Delta H(T) = \Delta H(T_1) + \Delta C_p(T - T_1)$，代入积分得

$$
\frac{\Delta G(T_2)}{T_2} = \frac{\Delta G(T_1)}{T_1} + \Delta H(T_1)\left(\frac{1}{T_2} - \frac{1}{T_1}\right) - \Delta C_p\left(\ln\frac{T_2}{T_1} + \frac{T_1}{T_2} - 1\right).
$$

**例 3.6.1** 用 Gibbs–Helmholtz 方程求例 3.5.3 中 $298.15\,\mathrm{K}$ 水汽化的 $\Delta G$。

**解** 取 $T_1 = 373.15\,\mathrm{K}$（两相平衡，$\Delta G(T_1) = 0$），$T_2 = 298.15\,\mathrm{K}$，$\Delta H(T_1) = 40650\,\mathrm{J}$，$\Delta C_p = (33 - 75)\,\mathrm{J\,K^{-1}} = -42\,\mathrm{J\,K^{-1}}$。代入上式：

$$
\frac{\Delta G(T_2)}{T_2} = 40650 \times \left(\frac{1}{298.15} - \frac{1}{373.15}\right) + 42 \times \left(\ln\frac{298.15}{373.15} + \frac{373.15}{298.15} - 1\right) = (27.40 + 1.14)\,\mathrm{J\,K^{-1}},
$$
$\Delta G(T_2) = 298.15 \times 28.54\,\mathrm{J} = 8.51\,\mathrm{kJ}$，与解法 1 相同（两者用了同样的数据与近似）。$\square$

Gibbs–Helmholtz 方程用于 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$，就是平衡常数随温度变化的 van 't Hoff 方程（[6.3.7](/6.3.7)）；用于 $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$，就由电动势及其温度系数求反应焓（[6.3.13](/6.3.13)）。

## 小结

| 内容 | 关系式 | 条件 |
|---|---|---|
| 最大功 | $-W \le -\Delta A$ | 封闭系统，等温 |
| 最大非体积功 | $-W' \le -\Delta G$ | 封闭系统，等温等压 |
| 判据 | $\Delta A \le 0$；$\Delta G \le 0$ | 另加等容或等压，且 $W' = 0$ |
| 基本方程 | $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ 等四式 | 组成不变的封闭系统，$W' = 0$，相邻平衡态之间（与可逆与否无关） |
| Maxwell 关系 | $(\partial S/\partial V)_T = (\partial p/\partial T)_V$，$(\partial S/\partial p)_T = -(\partial V/\partial T)_p$ 等 | 同上 |
| 热力学状态方程 | $(\partial U/\partial V)_T = T(\partial p/\partial T)_V - p$ | 任意物质 |
| 热容之差 | $C_p - C_V = TV\alpha_V^2/\kappa_T$ | 任意物质 |
| Gibbs–Helmholtz 方程 | $[\partial(\Delta G/T)/\partial T]_p = -\Delta H/T^2$ | 始末态 $T$、$p$ 相同 |

- 判据的条件是"始末态的温度（压力）等于环境的温度（压力）"，不满足时 $\Delta G$ 的符号不能判断方向，回到孤立系统的熵判据。
- $U$、$H$、$A$、$G$ 是彼此的 Legendre 变换，各自在自然变量下是特性函数；化学以 $G(T, p)$ 为中心，因为 $T$、$p$ 最容易控制。
- 等温过程的 $\Delta G = \Delta H - T\Delta S$；变温时 $\Delta G$ 依赖熵的绝对值，换温度用 Gibbs–Helmholtz 方程。
