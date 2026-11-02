---
title: 网络的动力学模型：建立、求解与拟合
description: 生物网络动力学模型的方法：正向与逆向模型；从示意图到速率方程（质量作用、化学计量矩阵与守恒基团、准稳态及其适用条件、唯象速率律、示意图的歧义、Lotka–Volterra）；数值解（Euler 与 Runge–Kutta 方法、阶与稳定性、自适应步长、刚性）；稳态、线性稳定性、糖酵解振荡的 Bier 模型及其 Hopf 分岔；网络的灵敏度分析与代谢控制分析（控制系数矩阵、求和与连接定理、分支途径、组合响应定理）；参数估计（最小二乘与似然、进程曲线、梯度、局部极小与多起点）；可辨识性、Fisher 信息、轮廓似然、自助法、模型选择与验证，并附完整的 Python 流程。
source_hash: ebed1670e9bd
---

前面各章把网络当作图来处理：哪些分子相互作用，哪些基因调控哪些基因。图并不说明随时间会发生什么。要预测一条通路如何响应刺激，一个回路是否振荡，或者使某个酶的活性减半的药物会使通量改变多少，就必须给边赋予速率，网络也就成为一个**常微分方程**组。本章讲这类动力学模型的做法：如何由示意图写出方程（14.2），如何数值求解（14.3），如何求稳态以及参数变化时行为的改变（14.4），行为对各参数有多敏感（14.5），以及反问题，即如何由数据估计参数（14.6）、如何知道数据究竟确定了什么（14.7）。14.8 节把这些步骤在 Python 中串起来。

所需的数学来自前面的课程，这里不再重复：解的存在唯一性与稳定性见 [2.4](/2.4)（特别是 [2.4.11](/2.4.11)），初值问题的数值方法见 [4.4.4](/4.4.4#sec-4.3)，非线性最小二乘见 [3.5.5](/3.5.5#sec-5.1.5) 与 [7.7.11](/7.7.11)，自助法见 [3.5.7](/3.5.7)。使用这些工具的生物学模型，即双稳态开关、抑制振荡子和 Goodwin 振荡器（[7.6.33](/7.6.33)）、随机动力学（[7.6.32](/7.6.32)）、通量平衡分析（[7.6.34](/7.6.34#sec-34.4)）和稳健性（[7.6.40](/7.6.40)），在用到时给出链接。后续各章把这些工具用于网络模体（[7.9.15](/7.9.15)）、信号转导中的反馈与振荡（[7.9.16](/7.9.16)）以及噪声与稳健性（[7.9.17](/7.9.17)）。

## 14.1. 正向模型与逆向模型

动力学模型可以朝两个方向使用（[7.9.1](/7.9.1#sec-1.5.3)）。**正向模型**由系统的结构和参数计算其行为；**逆向模型**由观测到的行为估计参数，或在不同结构之间做选择。两者用途不同，弱点也不同。

| | 正向模型 | 逆向模型 |
|---|---|---|
| 问题 | 若参数、输入或结构改变，会发生什么？ | 哪些参数（或哪个模型）能解释数据？ |
| 复杂度 | 在知识允许的范围内尽量详细；参数常取自文献 | 简单到数据能够确定为止 |
| 用途 | 总结知识、预测难以做的实验、在计算机上检验假设、设计实验 | 定量测定速率常数、亲和力和反馈强度；比较健康与疾病状态 |
| 主要风险 | 假设与文献值彼此不相容（"垃圾进，垃圾出"） | 数据无法确定的参数；局部最优；过拟合 |

两者在正向–逆向研究中结合：用已知参数和真实的噪声由正向模型生成合成数据，再用逆向模型拟合；已知参数能否被恢复，就能在做任何实验之前显示一项计划中的实验能确定哪些参数、精度如何。本章的若干图就是这样的研究。一般的原则是，模型必须得到验证：用结果已知的极限情形下的行为，以及它没有见过的实验；而它失败的地方是有信息的：它们显示了尚未理解的东西。

动力学模型是几种描述层次之一（[7.6.33](/7.6.33#sec-33.1.2)）。**布尔网络**不需要速率常数，可以扩展到数百个基因（[7.6.34](/7.6.34#sec-34.2.3)）；浓度的常微分方程给出时间尺度、阈值和分岔，是本章的主题；**化学主方程**及其 **Gillespie 算法**模拟描述小拷贝数的涨落（[7.6.32](/7.6.32#sec-32.5)）；偏微分方程加入空间（[2.5](/2.5)）；基于约束的模型如**通量平衡分析**不用动力学就描述基因组规模代谢网络的稳态（[7.6.34](/7.6.34#sec-34.4)）。模型用系统生物学标记语言（SBML）交换，这是一种记录物种、反应、速率律、参数和初始条件的 XML 格式，用系统生物学图形符号（SBGN）绘图，并存放在 BioModels 中，这是一个经过整理的已发表模型库，可以下载并模拟。

## 14.2. 从示意图到方程

### 14.2.1. 质量作用与化学计量矩阵

基元反应是经过单一过渡态进行的反应，其速率与反应物浓度之积成正比（**质量作用定律**，[7.6.3](/7.6.3#sec-3.2)）。一级反应 $A \to B$ 的速率为 $k_1[A]$，$k_1$ 的单位为 $\mathrm{s^{-1}}$；二级反应 $A + B \to C$ 的速率为 $k_2[A][B]$，$k_2$ 的单位为 $\mathrm{M^{-1}\,s^{-1}}$：不同级数的速率常数单位不同，这是检查每个方程的有用手段。

**定义 14.2.1（反应网络的动力学模型）** 设网络有 $m$ 个物种，浓度为 $\boldsymbol{x} = (x_1, \dots, x_m)$，有 $r$ 个反应，速率为 $\boldsymbol{v}(\boldsymbol{x}, \boldsymbol{p})$，依赖于参数 $\boldsymbol{p}$。设**化学计量矩阵** $N$ 为 $m \times r$ 矩阵，元素 $N_{ij}$ 是反应 $j$ 净产生的物种 $i$ 的分子数，则网络的*动力学模型*是方程组
$$
\frac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = N\boldsymbol{v}(\boldsymbol{x}, \boldsymbol{p}), \qquad \boldsymbol{x}(0) = \boldsymbol{x}_0. \tag{14.1}
$$

网络的结构在 $N$ 中，动力学在 $\boldsymbol{v}$ 中。通量平衡分析只用 $N$ 和稳态条件 $N\boldsymbol{v} = \boldsymbol{0}$；动力学模型则两者都需要。

**例 14.2.1** 对酶催化 $E + S \rightleftharpoons C \to E + P$，物种为 $(E, S, C, P)$，反应为 $v_1 = k_1[E][S]$（结合）、$v_2 = k_{-1}[C]$（解离）和 $v_3 = k_2[C]$（催化），
$$
N = \begin{bmatrix} -1 & 1 & 1 \\ -1 & 1 & 0 \\ 1 & -1 & -1 \\ 0 & 0 & 1 \end{bmatrix}, \qquad
\frac{\mathrm{d}[C]}{\mathrm{d}t} = k_1[E][S] - (k_{-1} + k_2)[C],
$$
其他三个物种类似：四个方程，由反应式机械地写出。

### 14.2.2. 守恒律

并非所有方程都是独立的。在例 14.2.1 中，$\mathrm{d}([E] + [C])/\mathrm{d}t = 0$：酶既不生成也不消失，只是在游离态与结合态之间转换。这类关系只需由 $N$ 就能找到。

**定理 14.2.1（守恒基团）** 若行向量 $\boldsymbol{\ell}$ 满足 $\boldsymbol{\ell}N = \boldsymbol{0}$，则无论速率律如何，$\boldsymbol{\ell}\boldsymbol{x}(t)$ 沿式 (14.1) 的每个解都是常数。若 $N$ 的秩为 $\rho$，则有 $m - \rho$ 个线性无关的这类关系，系统可以约化为 $\rho$ 个独立变量。

**证明** $\mathrm{d}(\boldsymbol{\ell}\boldsymbol{x})/\mathrm{d}t = \boldsymbol{\ell}N\boldsymbol{v} = 0$。秩为 $\rho$ 的 $m \times r$ 矩阵的左零空间维数为 $m - \rho$。取它的一组基 $L$，则 $L\boldsymbol{x} = L\boldsymbol{x}_0$ 给出 $m - \rho$ 个线性方程，可把 $m - \rho$ 个浓度用其余浓度表示。$\square$

**定义 14.2.2（守恒基团）** 满足 $\boldsymbol{\ell}N = \boldsymbol{0}$ 且系数非负的线性组合 $\boldsymbol{\ell}\boldsymbol{x}$ 是一个**守恒基团**：一个在物种之间转移、但在网络中从不生成或消失的化学基团（一种酶、一个磷酸基团、$\mathrm{NAD^+/NADH}$ 之类的辅酶、腺嘌呤核苷酸）。

**例 14.2.2** 例 14.2.1 的矩阵 $N$ 的秩为 $2$，所以有两条守恒律：$\boldsymbol{\ell}_1 = (1, 0, 1, 0)$，总酶量 $E_{\mathrm{T}} = [E] + [C]$；以及 $\boldsymbol{\ell}_2 = (0, 1, 1, 1)$，各种形式的总底物 $S_0 = [S] + [C] + [P]$。只剩下 $[S]$ 与 $[C]$ 的两个方程：
$$
\frac{\mathrm{d}[S]}{\mathrm{d}t} = -k_1(E_{\mathrm{T}} - [C])[S] + k_{-1}[C], \qquad \frac{\mathrm{d}[C]}{\mathrm{d}t} = k_1(E_{\mathrm{T}} - [C])[S] - (k_{-1} + k_2)[C]. \tag{14.2}
$$

守恒律在数值上和概念上同样重要：若保留全部 $m$ 个方程，系统的 Jacobi 矩阵是奇异的（14.4），并且在守恒总量被固定之前稳态不是唯一的。

### 14.2.3. 时间尺度分离与准稳态

式 (14.2) 仍含有一个快过程（结合）和一个慢过程（底物的转化）。如果复合物对底物的调整比底物的变化快得多，就可以在第二个方程中令 $\mathrm{d}[C]/\mathrm{d}t \approx 0$（**准稳态近似**），解出 $[C]$，得到 **Michaelis–Menten 方程** $\mathrm{d}[S]/\mathrm{d}t = -V_{\max}[S]/(K_{\mathrm{M}} + [S])$，其中 $V_{\max} = k_2E_{\mathrm{T}}$，$K_{\mathrm{M}} = (k_{-1} + k_2)/k_1$；推导及其假设见 [7.1.9](/7.1.9)。建模时的问题是这一约化何时有效。

**公式 14.2.1（准稳态的有效性）** 对从 $[S] = S_0$、$[C] = 0$ 出发的酶反应机制，标准准稳态近似在以下条件下是准确的（Segel 与 Slemrod，1989）
$$
\frac{E_{\mathrm{T}}}{S_0 + K_{\mathrm{M}}} \ll 1 .
$$
它来自比较复合物趋近其准稳态水平的时间 $t_C = 1/[k_1(S_0 + K_{\mathrm{M}})]$ 与底物发生明显变化的时间 $t_S = (S_0 + K_{\mathrm{M}})/(k_2E_{\mathrm{T}})$，并要求初始瞬态期间消耗的底物很少。

教科书上常用的条件 $E_{\mathrm{T}} \ll S_0$ 是充分的但不是必要的：底物浓度低时，只要 $E_{\mathrm{T}} \ll K_{\mathrm{M}}$，该近似也成立。当两者都不成立时，更好的约化是全准稳态近似（Borghans、de Boer 与 Segel，1996）：写出总底物 $\hat S = [S] + [C]$ 的方程 $\mathrm{d}\hat S/\mathrm{d}t = -k_2[C]$，并取 $[C]$ 为 $[C]^2 - (E_{\mathrm{T}} + K_{\mathrm{M}} + \hat S)[C] + E_{\mathrm{T}}\hat S = 0$ 的准稳态根，
$$
[C] = \tfrac12\Bigl(E_{\mathrm{T}} + K_{\mathrm{M}} + \hat S - \sqrt{(E_{\mathrm{T}} + K_{\mathrm{M}} + \hat S)^2 - 4E_{\mathrm{T}}\hat S}\Bigr),
$$
在酶与底物浓度相当时它仍然准确，许多信号蛋白就是如此，它们的底物是浓度相近的其他蛋白质。

![Michaelis–Menten 速率律何时可以代替质量作用机制（k₁ = 1，k₋₁ = 9，k₂ = 1，故 K_M = 10；S₀ = 50；模型单位）。A：E_T = 0.1 时，E_T/(S₀ + K_M) = 0.0017；复合物（虚线，右轴）在约 0.1 个时间单位内达到其准稳态水平，此后完整模型（实线）与 Michaelis–Menten 方程（点）的产物曲线重合（对数时间轴）。B：E_T = 20（比值 0.33）时，标准近似（点线）超前于完整模型，因为有三分之一的底物被束缚在复合物中；全准稳态近似（虚线）与完整模型吻合](./plots/qssa.py)

**例 14.2.3** 图中，$E_{\mathrm{T}} = 0.1$ 时，完整模型与 Michaelis–Menten 方程的产物曲线之间的最大差为 $S_0$ 的 $0.06\,\%$，半转化时间为 $319.5$ 和 $319.3$。$E_{\mathrm{T}} = 20$ 时，差达到 $S_0$ 的 $11.7\,\%$，半转化时间为 $1.83$（完整模型）和 $1.60$（标准近似）；全近似给出 $1.82$，最大误差为 $0.5\,\%$。

### 14.2.4. 较大网络的速率律

在单个酶之上的层次，模型使用唯象速率律，其参数概括了若干基元步骤：修饰酶用 Michaelis–Menten 项，协同结合与转录调控用 **Hill 方程**（[7.6.4](/7.6.4)、[7.6.33](/7.6.33#sec-33.1.2)），共价修饰循环则用两者的组合，当两个转换酶都饱和时，出现**零级超敏**（[7.1.9](/7.1.9#sec-9.6.1)）。

**例 14.2.4** 一个一般的三组分抑制性网络（Mogilner、Wollman 与 Marshall，2006，是土壤细菌中一个振荡回路的简化形式）有蛋白质 $A$、$B$、$C$，各有未修饰和磷酸化两种形式：$C$ 催化 $A$ 的磷酸化，$A$ 催化 $B$ 的去磷酸化，$B$ 催化 $C$ 的去磷酸化。每个转换都取 Michaelis–Menten 速率律，则 $A$ 及其磷酸化形式 $A_{\mathrm{p}}$ 的方程为
$$
\frac{\mathrm{d}[A]}{\mathrm{d}t} = \frac{k_{\mathrm{p}1}[A_{\mathrm{p}}]}{[A_{\mathrm{p}}] + K_{\mathrm{p}1}} - \frac{k_{\mathrm{k}1}[A][C]}{[A] + K_{\mathrm{k}1}}, \qquad \frac{\mathrm{d}[A_{\mathrm{p}}]}{\mathrm{d}t} = -\frac{\mathrm{d}[A]}{\mathrm{d}t},
$$
守恒律 $[A] + [A_{\mathrm{p}}] = A_{\mathrm{T}}$ 消去 $[A_{\mathrm{p}}]$。对 $B$ 和 $C$ 同样处理，剩下三个形如
$$
\frac{\mathrm{d}[A]}{\mathrm{d}t} = \frac{k_{\mathrm{p}1}(A_{\mathrm{T}} - [A])}{A_{\mathrm{T}} - [A] + K_{\mathrm{p}1}} - \frac{k_{\mathrm{k}1}[A][C]}{[A] + K_{\mathrm{k}1}},
$$
的方程，这是一个三级的负反馈环，与**抑制振荡子**（[7.6.33](/7.6.33#sec-33.5.3)）一样，对某些参数值振荡，对另一些则趋于稳态。

这个例子显示了一般的程序：列出包括每种修饰形式在内的物种，列出转换并给每个转换指定速率律，加上守恒律，检查单位。它也显示了主要的障碍：示意图常常有歧义。信号转导示意图中的箭头"MEK → ERK"代表 MEK 对 ERK 的两次磷酸化、磷酸酶的两次去磷酸化，MEK 自身也是如此；方程可以对详细的机制写出，而不能对这个箭头写出。有些示意图根本无法转换，因为它们省略了受体与效应之间的机制，或跳过了中间的激酶。因此写方程是对示意图的检验：每个箭头都必须说明是转换、催化还是调节，这正是 SBGN 过程图所要求的区分。

### 14.2.5. 最简单的振荡网络

Lotka–Volterra 系统是具有持续振荡的最简单网络：猎物 $x$ 增长并被捕食，捕食者 $y$ 因捕食而增长并死亡，
$$
\dot x = x(\alpha - \beta y), \qquad \dot y = y(-\gamma + \delta x). \tag{14.3}
$$
从网络的角度看，它是由质量作用项构成的两节点负反馈环：$x$ 激活 $y$，$y$ 抑制 $x$。它的正解是围绕平衡点 $(\gamma/\delta, \alpha/\beta)$ 的闭轨道，因为 $\Phi(x, y) = \delta x - \gamma\ln x + \beta y - \alpha\ln y$ 是一个**首次积分**（[例 14.1.2](/2.4.14#ex-14.1.2)）。有两点使它区别于生物振荡器。振幅不是由系统选定的，而是由初始条件固定，任何扰动都会使它转到另一条轨道。并且结构是脆弱的：加入猎物的自限项（$-\varepsilon x^2$）就把闭轨道变成趋向稳定平衡点的螺旋。稳健的生物振荡器是**极限环**（14.4）；式 (14.3) 在生态学中的应用见 [7.19](/7.19)，其首次积分使它成为检验数值方法的好例子（14.3）。

## 14.3. 数值解

很少有动力学模型能求出解析解。数值方法在离散时刻 $t_n = t_0 + nh$ 上计算**初值问题** $\dot{\boldsymbol{x}} = \boldsymbol{f}(t, \boldsymbol{x})$、$\boldsymbol{x}(t_0) = \boldsymbol{x}_0$ 的解。

### 14.3.1. Euler 方法

**算法 14.3.1（Euler 方法）** 给定 $\boldsymbol{x}_0$ 和步长 $h$，对 $n = 0, 1, 2, \dots$ 令
$$
\boldsymbol{x}_{n+1} = \boldsymbol{x}_n + h\,\boldsymbol{f}(t_n, \boldsymbol{x}_n). \tag{14.4}
$$

Euler 方法沿解在当前点的切线前进一步：它就是 [2.4.4](/2.4.4) 的 **Euler 折线**作为算法的应用。对一个模型，它写成循环：定义常数、步长和初始状态，每一步计算 $\mathrm{d}\boldsymbol{x}/\mathrm{d}t$ 并更新 $\boldsymbol{x}$。

**例 14.3.1** 对 $\dot x = a - bx$，$a = 20$，$b = 2$，$x(0) = 5$，$h = 0.05$，前几步为 $\dot x(0) = 20 - 10 = 10$，$x_1 = 5 + 0.05 \times 10 = 5.5$；$\dot x = 20 - 11 = 9$，$x_2 = 5.5 + 0.05 \times 9 = 5.95$。精确解为 $x(t) = a/b - (a/b - c)\mathrm{e}^{-bt}$，$c = x(0)$，所以 $x(1) = 10 - 5\mathrm{e}^{-2} = 9.3233$；二十步 Euler 给出 $9.3921$，误差为 $0.069$。$h = 0.025$ 时误差为 $0.034$：步长减半，误差也减半。

方法的两个性质决定它的用途。

**定理 14.3.1（Euler 方法的收敛性）** 设 $\boldsymbol{f}$ 连续可微，关于 $\boldsymbol{x}$ 满足常数为 $L$ 的 Lipschitz 条件，且解在 $[t_0, T]$ 上有界的二阶导数 $\lVert\ddot{\boldsymbol{x}}\rVert \le M$。则 Euler 近似满足
$$
\lVert\boldsymbol{x}_n - \boldsymbol{x}(t_n)\rVert \le \frac{hM}{2L}\bigl(\mathrm{e}^{L(t_n - t_0)} - 1\bigr),
$$
所以整体误差为 $O(h)$：该方法为 $1$ 阶。

**证明** 由 Taylor 定理，从真解出发的一步的局部误差至多为 $Mh^2/2$。记 $e_n = \lVert\boldsymbol{x}_n - \boldsymbol{x}(t_n)\rVert$。用式 (14.4) 减去 $\boldsymbol{x}(t_{n+1}) = \boldsymbol{x}(t_n) + h\boldsymbol{f}(t_n, \boldsymbol{x}(t_n)) + \boldsymbol{\tau}_n$，并利用 Lipschitz 界，得 $e_{n+1} \le (1 + hL)e_n + Mh^2/2$，$e_0 = 0$。归纳得 $e_n \le \frac{Mh^2}{2}\sum_{k<n}(1 + hL)^k = \frac{Mh}{2L}\bigl((1 + hL)^n - 1\bigr) \le \frac{Mh}{2L}(\mathrm{e}^{nhL} - 1)$。$\square$

第二个性质是稳定性。对衰减的检验方程 $\dot x = -\lambda x$（$\lambda > 0$），Euler 方法给出 $x_{n+1} = (1 - h\lambda)x_n$，只有当 $\lvert 1 - h\lambda\rvert < 1$，即 $h < 2/\lambda$ 时才衰减。步长更大时，数值解以增长的振幅振荡，取到 $10^{78}$ 之类的值，本应非负的浓度变为负值。在例 14.3.1 中，$\lambda = b = 2$，界限为 $h = 1$（图的 B 部分）：$h = 0.9$ 时迭代在 $10$ 附近振荡并缓慢收敛，$h = 1.1$ 时发散。

### 14.3.2. Runge–Kutta 方法与自适应步长

更好的方法每步多次计算 $\boldsymbol{f}$，并组合这些斜率，使低阶误差项相互抵消。

**算法 14.3.2（经典 Runge–Kutta 方法）** 对 $n = 0, 1, 2, \dots$ 计算
$$
\boldsymbol{k}_1 = \boldsymbol{f}(t_n, \boldsymbol{x}_n), \quad \boldsymbol{k}_2 = \boldsymbol{f}\bigl(t_n + \tfrac h2, \boldsymbol{x}_n + \tfrac h2\boldsymbol{k}_1\bigr), \quad \boldsymbol{k}_3 = \boldsymbol{f}\bigl(t_n + \tfrac h2, \boldsymbol{x}_n + \tfrac h2\boldsymbol{k}_2\bigr), \quad \boldsymbol{k}_4 = \boldsymbol{f}(t_n + h, \boldsymbol{x}_n + h\boldsymbol{k}_3),
$$
$$
\boldsymbol{x}_{n+1} = \boldsymbol{x}_n + \tfrac h6(\boldsymbol{k}_1 + 2\boldsymbol{k}_2 + 2\boldsymbol{k}_3 + \boldsymbol{k}_4).
$$

算法 14.3.2 的 **Runge–Kutta 方法**为 $4$ 阶：整体误差为 $O(h^4)$，所以步长减半使误差减小为十六分之一，代价是每步四次计算 $\boldsymbol{f}$。Heun 方法 $\boldsymbol{x}_{n+1} = \boldsymbol{x}_n + \tfrac h2[\boldsymbol{f}(t_n, \boldsymbol{x}_n) + \boldsymbol{f}(t_{n+1}, \boldsymbol{x}_n + h\boldsymbol{f}(t_n, \boldsymbol{x}_n))]$ 是该族中的二阶方法。

![常微分方程的数值解。A：Euler 方法、Heun 方法和经典四阶 Runge–Kutta 方法对 dx/dt = a − bx（a = 20，b = 2，x(0) = 5）在 t = 1 处的误差随步长 h 的变化，对数坐标轴；斜率即阶数 1、2 和 4。B：三种步长的 Euler 解；hb > 2 时迭代发散，尽管真解弛豫到 a/b = 10。C：Lotka–Volterra 系统 x′ = x(1 − 0.1y)，y′ = y(−1.5 + 0.075x)，自 (10, 5) 出发，历时 50 个时间单位：精确轨道是闭的，h = 0.01 的 Euler 解向外螺旋，h = 0.1 的 Runge–Kutta 解留在轨道上](./plots/ode_methods.py)

**例 14.3.2** 对例 14.3.1 的方程，Runge–Kutta 在 $t = 1$ 处的误差，$h = 0.05$ 时为 $1.2 \times 10^{-6}$，$h = 0.025$ 时为 $7.3 \times 10^{-8}$，比值为 $16.7$。对 C 图的 Lotka–Volterra 系统（$\alpha = 1$，$\beta = 0.1$，$\gamma = 1.5$，$\delta = 0.075$），首次积分 $\Phi$ 应保持其初值 $-3.813$。经过 $50$ 个时间单位（约九个周期，周期为 $5.48$）后，Euler 方法在 $h = 0.01$（$5000$ 步）时使它增加了 $0.51$，在 $h = 0.001$ 时增加了 $0.036$；Runge–Kutta 方法在 $h = 0.1$（$500$ 步，$2000$ 次计算）时只改变了 $4 \times 10^{-6}$。不保持首次积分的方法会把保守系统变成耗散的或爆炸的系统，这种定性的错误可能被误认为生物学。

固定步长在解光滑处浪费计算，在解变化快处又嫌太大。现代的求解器自适应地选择步长。一对共享计算的 $p$ 阶与 $p + 1$ 阶嵌入 Runge–Kutta 公式（Dormand 与 Prince，$4$ 阶与 $5$ 阶，即 `solve_ivp` 默认的 `RK45`）给出 $\boldsymbol{x}_{n+1}$ 的两个估计；它们之差估计局部误差，如果逐分量的误差小于 $\mathrm{atol} + \mathrm{rtol}\,\lvert x\rvert$ 就接受该步，否则拒绝，并相应地放大或缩小下一步。在 Lotka–Volterra 的例子中，$\mathrm{rtol} = 10^{-3}$ 的 `RK45` 需要 $566$ 次计算，使 $\Phi$ 改变 $0.011$；$\mathrm{rtol} = 10^{-6}$ 时需要 $1676$ 次计算，改变 $2 \times 10^{-6}$。容差是模型设定的一部分：$\mathrm{atol}$ 必须比最小的重要浓度小得多，否则低浓度的物种算出来就没有准确的数字。求解器及其选项见 [4.4.4](/4.4.4#sec-4.3.2)。

### 14.3.3. 刚性

生化网络把快过程与慢过程结合在一起：结合在毫秒内，转录在分钟内，生长在小时内。当一个系统的衰减模式比所跟踪的解快得多时，显式方法的步长受最快模式的限制，$h < 2/\lambda_{\max}$，哪怕该模式早已消失。这样的系统是刚性的（**刚性**，[4.4.4](/4.4.4#sec-4.3.3)）。最大与最小衰减率之比，即 Jacobi 矩阵的特征值之比（14.4），度量它的大小。

**例 14.3.3** 酶系统 (14.2) 取 $k_1 = 1$，$k_{-1} = 9$，$k_2 = 1$，$E_{\mathrm{T}} = 0.1$，$S_0 = 50$，在初始瞬态之后，Jacobi 矩阵的特征值为 $-60.0$（复合物的弛豫）和 $-2.8 \times 10^{-4}$（底物的转化），比值为 $2 \times 10^5$。积分到 $t = 1500$（几乎转化了全部底物），取 $\mathrm{rtol} = 10^{-6}$：显式 `RK45` 需要 $65\,630$ 次计算 $\boldsymbol{f}$；隐式的 `BDF`（后向微分公式）$518$ 次，`Radau`（隐式 Runge–Kutta）$1084$ 次，在显式与隐式方法之间自动切换的 `LSODA` 为 $463$ 次。

隐式方法，如后向 Euler 方法 $\boldsymbol{x}_{n+1} = \boldsymbol{x}_n + h\boldsymbol{f}(t_{n+1}, \boldsymbol{x}_{n+1})$，每步要解一个方程（用带 Jacobi 矩阵的 Newton 法），对衰减模式对所有步长都是稳定的：对 $\dot x = -\lambda x$，后向 Euler 迭代 $x_{n+1} = x_n/(1 + h\lambda)$ 对每个 $h > 0$ 都衰减。它们每步的代价较高，步数则由精度而不是稳定性决定。网络模型的实用规则是：先试显式求解器；如果慢或需要很小的步长，就换用 `LSODA` 或 `BDF`，并在能写出 Jacobi 矩阵时提供它。

## 14.4. 稳态、稳定性与分岔

### 14.4.1. 线性化

式 (14.1) 的稳态 $\boldsymbol{x}^*$ 满足 $N\boldsymbol{v}(\boldsymbol{x}^*, \boldsymbol{p}) = \boldsymbol{0}$（消去守恒基团之后）。若没有实部为零的特征值，其稳定性由 $\boldsymbol{x}^*$ 处的 **Jacobi 矩阵** $J = \partial\boldsymbol{f}/\partial\boldsymbol{x}$ 决定：若 $J$ 的所有**特征值**实部为负，稳态渐近稳定；若有一个实部为正，则不稳定（[2.4.11](/2.4.11#sec-11.3)）。对平面系统，特征值由 $\tau = \operatorname{tr}J$ 与 $\Delta = \det J$ 决定：$\Delta < 0$ 为鞍点；$\Delta > 0$ 且 $\tau < 0$ 为稳定结点或焦点；$\Delta > 0$ 且 $\tau > 0$ 为不稳定的；复特征值（$\tau^2 < 4\Delta$）给出螺旋（[2.4.11](/2.4.11#sec-11.5.2)）。**相平面**中，一个导数为零的**零倾线**及其之间的**方向场**（[7.6.33](/7.6.33#sec-33.3.1)）显示动力学的其余部分：零倾线把平面分成两个导数符号都固定的区域，轨线只在穿过零倾线时才改变方向。

### 14.4.2. 糖酵解振荡的 Bier 模型

悬浮的酵母细胞经饥饿后给予葡萄糖，会表现出 NADH 及其他糖酵解中间产物的振荡，周期约一分钟（**糖酵解振荡**，[7.1.18](/7.1.18)、[6.3.18](/6.3.18#sec-18.3.3)）。振荡的来源是磷酸果糖激酶，它消耗 ATP，却被其产物激活，所以下游产生的 ATP 加速了它自身的消耗：一个自催化环。已有许多模型；最简单的之一只保留两个变量（Bier、Bakker 与 Westerhoff，2000）。

**定义 14.4.1（Bier 模型）** 设 $G$ 是细胞内的葡萄糖浓度，$T$ 是 ATP 浓度，葡萄糖以恒定速率 $V_{\mathrm{in}}$ 进入，在消耗 ATP 的一步中被磷酸化，其速率与两者成正比（$k_1GT$），在下游糖酵解中以该速率的两倍净产生 ATP，而 ATP 被 ATP 酶按 Michaelis–Menten 动力学消耗：
$$
\frac{\mathrm{d}G}{\mathrm{d}t} = V_{\mathrm{in}} - k_1GT, \qquad \frac{\mathrm{d}T}{\mathrm{d}t} = 2k_1GT - \frac{k_{\mathrm{p}}T}{T + K_{\mathrm{m}}}. \tag{14.5}
$$

**例 14.4.1** 零倾线为 $G = V_{\mathrm{in}}/(k_1T)$（$\dot G = 0$）和 $G = k_{\mathrm{p}}/[2k_1(T + K_{\mathrm{m}})]$（$\dot T = 0$，$T > 0$）。令两者相等，得唯一的稳态
$$
T^* = \frac{2V_{\mathrm{in}}K_{\mathrm{m}}}{k_{\mathrm{p}} - 2V_{\mathrm{in}}}, \qquad G^* = \frac{V_{\mathrm{in}}}{k_1T^*},
$$
它在 $k_{\mathrm{p}} > 2V_{\mathrm{in}}$ 时存在（ATP 酶能消耗由葡萄糖供给所产生的 ATP）。取 $V_{\mathrm{in}} = 0.36$，$k_1 = 0.02$，$k_{\mathrm{p}} = 6$（模型单位），$K_{\mathrm{m}} = 13$：$T^* = 9.36/5.28 = 1.773$，$G^* = 10.15$。利用稳态处 $2k_1G^* = k_{\mathrm{p}}/(T^* + K_{\mathrm{m}})$，Jacobi 矩阵为
$$
J = \begin{bmatrix} -k_1T^* & -k_1G^* \\ 2k_1T^* & \dfrac{k_{\mathrm{p}}T^*}{(T^* + K_{\mathrm{m}})^2} \end{bmatrix}, \qquad
\operatorname{tr}J = \frac{k_{\mathrm{p}}T^*}{(T^* + K_{\mathrm{m}})^2} - k_1T^*, \qquad \det J = \frac{k_1k_{\mathrm{p}}K_{\mathrm{m}}T^*}{(T^* + K_{\mathrm{m}})^2} > 0 .
$$
对 $K_{\mathrm{m}} = 13$，$\operatorname{tr}J = 0.0133 > 0$，$\det J = 0.0127$：特征值 $0.0066 \pm 0.1124\,\mathrm{i}$ 使稳态成为不稳定焦点。对 $K_{\mathrm{m}} = 20$（$T^* = 2.727$，$G^* = 6.60$），$\operatorname{tr}J = -0.0229$，特征值 $-0.0114 \pm 0.1120\,\mathrm{i}$ 使它成为稳定焦点。

对角线上的正元素 $\partial\dot T/\partial T > 0$ 就是自催化：更多的 ATP 加速了产生更多 ATP 的那一步。当它超过葡萄糖消耗的阻尼 $k_1T^*$ 时，稳态就失稳。由于稳态是唯一的，并且轨线停留在有界区域内，由 Poincaré–Bendixson 定理，不稳定焦点被一个稳定的**极限环**所包围（[2.4.11](/2.4.11#sec-11.6.2)）。

![酵母糖酵解振荡的 Bier 模型，式 (14.5)（V_in = 0.36，k₁ = 0.02，k_p = 6；模型单位）。A：K_m = 13 的相平面，含两条零倾线、方向场和一条从稳态（空心圆）附近出发的轨线：稳态是不稳定焦点，轨线向外盘旋到一个稳定的极限环上。B：K_m = 20 时，从远处出发的轨线螺旋地趋于稳定焦点（实心圆）。C：分岔图，吸引子上 G 的最小值和最大值随 K_m 的变化；振荡在 K_m = 15.24 处的超临界 Hopf 分岔产生，该处 Jacobi 矩阵的迹为零；其左侧的虚线是不稳定的稳态](./plots/bier_phase.py)

### 14.4.3. Hopf 分岔与分岔图

当参数越过临界值时定性行为的改变是一个**分岔**。在 Bier 模型中，对所有 $K_{\mathrm{m}}$，$\det J$ 都为正（无论 $K_{\mathrm{m}}$ 为何值它都等于 $0.0127$，因为 $T^*$ 与 $K_{\mathrm{m}}$ 成正比），而 $\operatorname{tr}J$ 变号：一对复特征值穿过虚轴，这就是 **Hopf 分岔**的特征（[2.4.11](/2.4.11#sec-11.6.4)、[7.6.33](/7.6.33#sec-33.5.2)）。

**例 14.4.2** 令 $\operatorname{tr}J = 0$，得 $(T^* + K_{\mathrm{m}})^2 = k_{\mathrm{p}}/k_1 = 300$。由 $T^* = 0.1364K_{\mathrm{m}}$，临界值为 $K_{\mathrm{m}} = \sqrt{300}/1.1364 = 15.24$，该处特征值为 $\pm 0.1126\,\mathrm{i}$，所以振荡产生时的周期为 $2\pi/0.1126 = 55.8$。模拟显示这是超临界分岔：当 $K_{\mathrm{m}}$ 降到 $15.24$ 以下时，环的振幅从零连续增长，$G$ 中大致为 $4.6\sqrt{15.24 - K_{\mathrm{m}}}$（$K_{\mathrm{m}} = 15.2$ 时为 $0.94$，$15.0$ 时为 $2.26$），从稳态附近或远处出发的轨线都到达同一个环。在 $K_{\mathrm{m}} = 13$ 时，环的周期为 $68.5$，$G$ 在 $3.07$ 与 $17.6$ 之间振荡，$T$ 在 $0.05$ 与 $12.4$ 之间振荡：远离 Hopf 点时，振荡是一种大振幅的、非正弦的弛豫振荡，周期变长。

如 C 图那样的暴力分岔图，对许多参数值模拟模型，并在瞬态消失之后记录变量的极值。在分岔附近瞬态衰减缓慢（$K_{\mathrm{m}} = 15.3$ 时特征值的实部只有 $-1.3 \times 10^{-4}$，衰减时间为数千个时间单位），长度有限的模拟会把临界点放错位置：在短时间运行之后只记录最后 $500$ 个时间单位的扫描，把它放在 $16$ 附近，而不是 $15.24$。解析条件或数值延拓可以避免这一点。延拓方法随参数变化沿稳态的一个分支前进：由分支的切线预测下一个点并用 Newton 法校正（伪弧长延拓，它还能绕过分支折回的折点），沿分支监测 $J$ 的特征值以发现鞍结点与 Hopf 点，然后追踪 Hopf 点产生的周期轨道；AUTO、MatCont 和 XPPAUT 实现了这些方法。开关和滞后背后的**鞍结分岔**见 [7.6.33](/7.6.33#sec-33.2.2)，这类图在细胞命运开关和细胞周期中的生物学应用见 [7.9.16](/7.9.16)。

## 14.5. 灵敏度与控制

### 14.5.1. 灵敏度系数

模型的行为在多大程度上依赖于每个参数？这个问题有三方面的意义：稳健性（依赖于精细调节参数的功能是脆弱的，[7.6.40](/7.6.40)）、实验设计（观测对其不敏感的参数无法估计，14.7）和干预（药物通过改变某个参数起作用）。

**定义 14.5.1（灵敏度系数）** 对模型输出 $y$（某时刻的浓度、稳态水平、周期）和参数 $p$，*灵敏度系数*是 $\partial y/\partial p$，标度化的灵敏度系数是**对数灵敏度** $S^y_p = \partial\ln y/\partial\ln p$（[定义 40.1.2](/7.6.40#def-40.1.2)），即参数每发生单位相对变化时输出的相对变化。

**公式 14.5.1（灵敏度方程）** 设 $\boldsymbol{x}(t; \boldsymbol{p})$ 解 $\dot{\boldsymbol{x}} = \boldsymbol{f}(\boldsymbol{x}, \boldsymbol{p})$，$S(t) = \partial\boldsymbol{x}/\partial\boldsymbol{p}$ 是对 $q$ 个参数的灵敏度的 $m \times q$ 矩阵。则
$$
\dot S = J(t)S + \frac{\partial\boldsymbol{f}}{\partial\boldsymbol{p}}, \qquad S(0) = \frac{\partial\boldsymbol{x}_0}{\partial\boldsymbol{p}}, \tag{14.6}
$$
其中 $J(t) = \partial\boldsymbol{f}/\partial\boldsymbol{x}$ 沿解取值；在稳定稳态处（$\dot S = 0$），
$$
\frac{\partial\boldsymbol{x}^*}{\partial\boldsymbol{p}} = -J^{-1}\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{p}}. \tag{14.7}
$$

**证明** 把 $\dot{\boldsymbol{x}} = \boldsymbol{f}(\boldsymbol{x}, \boldsymbol{p})$ 对 $\boldsymbol{p}$ 求导并交换求导次序（由解对参数的可微依赖性保证，[2.4.7](/2.4.7)）。式 (14.7) 是把**隐函数定理**应用于 $\boldsymbol{f}(\boldsymbol{x}^*, \boldsymbol{p}) = \boldsymbol{0}$；$J$ 可逆，因为稳定稳态的特征值都不为零。$\square$

灵敏度方程与模型一起求解，计算量大致乘以 $q + 1$；它们比有限差分更准确，有限差分需要的步长既要小到足以逼近导数，又要大到超过求解器的误差。

**例 14.5.1** 对基因的诱导，$\dot x = \beta - \alpha x$，$x(0) = 0$，解为 $x = (\beta/\alpha)(1 - \mathrm{e}^{-\alpha t})$（[例 1.5.1](/7.9.1#ex-1.5.1)），灵敏度为
$$
\frac{\partial x}{\partial\beta} = \frac{1 - \mathrm{e}^{-\alpha t}}{\alpha}, \qquad \frac{\partial x}{\partial\alpha} = -\frac{\beta}{\alpha^2}\bigl(1 - \mathrm{e}^{-\alpha t}\bigr) + \frac{\beta}{\alpha}t\,\mathrm{e}^{-\alpha t}.
$$
在稳态时 $S^x_\beta = 1$，$S^x_\alpha = -1$。在早期，$\partial x/\partial\beta \approx t$，$\partial x/\partial\alpha \approx -\beta t^2/2$：对降解速率的灵敏度是 $t$ 的二阶量，所以早期测量能确定 $\beta$ 而不能确定 $\alpha$。

局部灵敏度描述的是一组参数周围的小变化。当参数有数量级的不确定性时，全局方法对参数空间采样，例如在对数坐标的 Latin 超立方上，并把输出的方差分解为各参数及其相互作用的贡献（Sobol 指数）；体节极性网络的参数稳健性研究（[7.6.40](/7.6.40#sec-40.2.3)）就是这类全局分析。

### 14.5.2. 网络的控制系数

**代谢控制分析**（[7.1.17](/7.1.17#sec-17.4)）是稳态对酶活性的灵敏度分析，通过两类系数来表达：**通量控制系数** $C^J_i = \partial\ln J/\partial\ln e_i$，是系统的性质；以及**弹性系数** $\varepsilon^{v_i}_{S}$，是单个速率律的局部性质。对线性途径，求和定理与连接定理由弹性系数确定控制系数。式 (14.7) 把这一点推广到任意网络。

**定理 14.5.1（网络的控制系数）** 设 $\dot{\boldsymbol{s}} = N\boldsymbol{v}(\boldsymbol{s}, \boldsymbol{e})$ 有一个稳定稳态，代谢物浓度为 $\boldsymbol{s}$，通量 $\boldsymbol{J} = \boldsymbol{v}$，每个速率 $v_i$ 与其酶的活性 $e_i$ 成正比，$N$ 行满秩（已消去守恒基团）。设 $\varepsilon$ 为标度化弹性 $\varepsilon_{ij} = \partial\ln v_i/\partial\ln s_j$ 的 $r \times m$ 矩阵，$D = \operatorname{diag}(\boldsymbol{J})$。则浓度控制系数（concentration control coefficient）$C^S_{ji} = \partial\ln s_j/\partial\ln e_i$ 与通量控制系数 $C^J_{ki} = \partial\ln J_k/\partial\ln e_i$ 的矩阵为
$$
C^S = -(ND\varepsilon)^{-1}ND, \qquad C^J = I + \varepsilon C^S, \tag{14.8}
$$
并且满足求和定理 $C^J\boldsymbol{1} = \boldsymbol{1}$、$C^S\boldsymbol{1} = \boldsymbol{0}$ 与连接定理 $C^J\varepsilon = O$、$C^S\varepsilon = -I$。

**证明** 在稳态处 $N\boldsymbol{v}(\boldsymbol{s}(\boldsymbol{e}), \boldsymbol{e}) = \boldsymbol{0}$。对 $\ln e_i$ 求导，取 $\partial\boldsymbol{v}/\partial\ln e_i = v_i\boldsymbol{u}_i$（$\boldsymbol{u}_i$ 为第 $i$ 个单位向量）和 $\partial\boldsymbol{v}/\partial\ln\boldsymbol{s} = D\varepsilon$，得 $ND\varepsilon\,C^S + ND = O$，从而得到第一个公式（$ND\varepsilon$ 在差一个对角因子的意义下是对数坐标中的 Jacobi 矩阵，在稳定稳态处可逆）。通量既直接依赖于 $e_i$，又通过 $\boldsymbol{s}$ 依赖于它：$\partial\ln\boldsymbol{J}/\partial\ln e_i = \boldsymbol{u}_i + \varepsilon\,\partial\ln\boldsymbol{s}/\partial\ln e_i$，这就是第二个公式。求和：$ND\boldsymbol{1} = N\boldsymbol{J} = \boldsymbol{0}$，所以 $C^S\boldsymbol{1} = \boldsymbol{0}$，$C^J\boldsymbol{1} = \boldsymbol{1}$。连接：$C^S\varepsilon = -(ND\varepsilon)^{-1}ND\varepsilon = -I$，$C^J\varepsilon = \varepsilon + \varepsilon C^S\varepsilon = O$。$\square$

对线性途径，这些化为定理 [17.4.1](/7.1.17#thm-17.4.1) 与 [17.4.2](/7.1.17#thm-17.4.2)。浓度定理说明，把所有酶都增大同一倍数不改变任何浓度；代谢物通过其周围酶的弹性系数对自身的控制是稳态化的（$-1$）。在分支网络中会出现新的效应。

![分支途径的代谢控制分析。A：酶 1 把固定的来源 X₀ 转化为 S₁，并受其产物抑制；S₁ 由酶 2 和酶 3 经 S₂ 转化为 P，或被酶 4 分流为 Q（不可逆的 Michaelis–Menten 速率律；V₁ = 10，K₁ = 0.5，K_i = 1，V₂ = 4，K₂ = 1，V₃ = 10，K₃ = 1，V₄ = 6，K₄ = 2，X₀ = 1）。B：由式 (14.8) 得到的通量控制系数；每一行之和为一；酶 4 对流向 P 的通量有负控制，酶 2 对流向 Q 的通量有负控制；酶 3 没有控制，因为 S₂ 不作用于其他步骤。C：酶 4 的量在其参考值的 0.25 到 4 倍之间变化时，稳态通量 J_P 与 J_Q 相对于参考状态的变化（对数坐标轴）；参考点处的斜率就是酶 4 的控制系数](./plots/branched_mca.py)

**例 14.5.2** 对图中的分支途径，稳态为 $s_1 = 0.845$，$s_2 = 0.224$，流入分支点的通量为 $J_1 = 3.61$，$J_P = 1.83$，$J_Q = 1.78$。弹性系数为 $\varepsilon^{v_1}_{S_1} = -0.46$（产物抑制）、$\varepsilon^{v_2}_{S_1} = 0.54$、$\varepsilon^{v_4}_{S_1} = 0.70$ 和 $\varepsilon^{v_3}_{S_2} = 0.82$。式 (14.8) 给出 B 图的控制系数（行为通量，列为酶 1 至 4）：

| | $e_1$ | $e_2$ | $e_3$ | $e_4$ | 和 |
|---|---|---|---|---|---|
| $J_1$（供给） | 0.58 | 0.22 | 0 | 0.21 | 1 |
| $J_P$ | 0.50 | 0.75 | 0 | −0.25 | 1 |
| $J_Q$ | 0.65 | −0.33 | 0 | 0.68 | 1 |

它们与有限差分导数在四位小数上一致。增加酶 4 会降低 $s_1$，从而降低流向 $P$ 的通量；把它减半，$J_P$ 升高 $15\,\%$，$J_Q$ 降低 $40\,\%$。酶 3 对任何通量都没有控制，因为它的底物 $S_2$ 不影响其他速率；它只控制 $s_2$（$C^{S_2}_3 = -1.22$）。在代谢工程中，负的元素是机会：要增加流向某个产物的通量，除了加快生成它的步骤，也可以减慢竞争的分支。

**定理 14.5.2（组合响应定理）** 设外部效应物 $X$（抑制剂、激活剂、激素）只直接作用于速率 $v_i$，其弹性系数为 $\varepsilon^{v_i}_X = \partial\ln v_i/\partial\ln X$。则任何通量或浓度 $Y$ 对 $X$ 的响应系数 $R^Y_X = \mathrm{d}\ln Y/\mathrm{d}\ln X$ 为
$$
R^Y_X = C^Y_i\,\varepsilon^{v_i}_X .
$$
若 $X$ 作用于若干步骤，则 $R^Y_X = \sum_iC^Y_i\varepsilon^{v_i}_X$。

**证明** 在代谢物浓度固定时，$\ln X$ 改变 $\delta$ 使 $\ln v_i$ 改变 $\varepsilon^{v_i}_X\delta$，这与 $\ln e_i$ 改变 $\varepsilon^{v_i}_X\delta$ 完全一样，因为 $v_i$ 与 $e_i$ 成正比。稳态只对 $v_i$ 的变化作出响应，无论其原因为何，所以 $\mathrm{d}\ln Y = C^Y_i\varepsilon^{v_i}_X\delta$。若干效应在一阶上相加。$\square$

**例 14.5.3** 设酶 4 的竞争性抑制剂的作用为 $v_4 \propto 1/(1 + I/K_I)$，$K_I = 0.5$；在 $I = 0.25$ 时其弹性系数为 $\varepsilon^{v_4}_I = -I/(K_I + I) = -1/3$。在被抑制的稳态处重新计算控制系数，得 $C^{J_P}_4 = -0.19$ 和 $C^{J_Q}_4 = 0.75$，所以该定理预测 $R^{J_P}_I = 0.0625$ 和 $R^{J_Q}_I = -0.25$；对稳态通量取有限差分给出相同的值。该定理把药物的效应分成药物的性质（它对靶标的抑制有多强）与网络的性质（靶标对输出的控制有多大）：对控制很小的酶，强效抑制剂对通量的影响也很小（[7.1.17](/7.1.17#sec-17.4.4)）。

## 14.6. 参数估计

### 14.6.1. 优度函数

反问题有六个步骤：选择模型（经验的趋势函数，或者更好的、参数有意义的机制模型）；定义度量模型与数据之间不一致程度的优度函数；对参数最小化它；检查拟合优度与残差；问是否存在好得多的拟合（更低的极小值，或更好的模型）；以及确定参数被了解得多精确。前四步在这里处理，后两步在 14.6.4 与 14.7。

**公式 14.6.1（$\chi^2$ 优度函数）** 设观测值 $y_k$ 对应于时间或条件 $t_k$（$k = 1, \dots, n$），模型预测 $\hat y_k(\boldsymbol{\theta})$（对动力学模型，它是参数为 $\boldsymbol{\theta}$ 的式 (14.1) 的解的可观测函数），误差独立且服从标准差为 $\sigma_k$ 的正态分布。负对数似然在相差一个常数的意义下等于 $\tfrac12\chi^2(\boldsymbol{\theta})$，其中
$$
\chi^2(\boldsymbol{\theta}) = \sum_{k=1}^n\frac{\bigl(y_k - \hat y_k(\boldsymbol{\theta})\bigr)^2}{\sigma_k^2},
$$
所以 $\boldsymbol{\theta}$ 的**极大似然估计**就是权重为 $1/\sigma_k^2$ 的加权**最小二乘法**（[定理 11.1.1](/7.7.11#thm-11.1.1)）；各 $\sigma_k$ 相等时就是普通最小二乘。在极小值处，若模型正确且 $\sigma_k$ 无误，$\chi^2$ 近似服从自由度为 $n - q$ 的**卡方分布**，由此可检验拟合优度（[7.7.11](/7.7.11#sec-11.2.2)）。

其他的误差模型给出其他的优度函数：乘性误差在浓度和荧光中常见，给出对数的最小二乘；计数给出 Poisson 似然；离群值要求稳健的损失函数。高 $R^2$ 并不能证明拟合良好：系统地偏离数据的模型也可以有 $R^2 > 0.99$。残差对时间或条件作图，应当围绕零散布而无趋势；同号残差成串说明缺少一个机制（例 14.7.5）。

拟合动力学模型与普通的**非线性回归**有两点不同。每次计算 $\hat y(\boldsymbol{\theta})$ 都需要数值求解一个初值问题，其误差必须比测量误差小，且求解器对优化器尝试的参数值不能失败（刚性随参数变化）。而速率常数为正且跨越多个数量级，所以参数最好以对数 $\boldsymbol{\theta} = \ln\boldsymbol{p}$ 来估计，这保证了正性，也使相对精度可以比较。

### 14.6.2. 线性化与进程曲线

在计算机出现之前，非线性模型要线性化：Michaelis–Menten 方程在双倒数的 **Lineweaver–Burk 作图**中变成线性，$1/v = (K_{\mathrm{M}}/V_{\max})(1/[S]) + 1/V_{\max}$。线性化扭曲了误差结构（小的、有噪声的速率的倒数有极大的误差），给出有偏而低效的估计；在原尺度上的非线性最小二乘才是首选方法（[7.7.11](/7.7.11#sec-11.4.2) 在 Puromycin 数据上显示了这一点）。动力学模型还提供了更进一步的做法：不用初速率（每个初速率只用到反应的开头），而是拟合整个时间过程。

**公式 14.6.2（积分形式的 Michaelis–Menten 方程）** 方程 $\mathrm{d}[S]/\mathrm{d}t = -V_{\max}[S]/(K_{\mathrm{M}} + [S])$ 在 $[S](0) = S_0$ 下的解满足 $K_{\mathrm{M}}\ln(S_0/[S]) + S_0 - [S] = V_{\max}t$，并有显式形式
$$
[S](t) = K_{\mathrm{M}}\,W\!\left(\frac{S_0}{K_{\mathrm{M}}}\exp\frac{S_0 - V_{\max}t}{K_{\mathrm{M}}}\right),
$$
其中 $W$ 是 Lambert 函数，即 $w \mapsto w\mathrm{e}^w$ 的反函数（`scipy.special.lambertw`）。

**证明** 分离变量，$(K_{\mathrm{M}}/[S] + 1)\,\mathrm{d}[S] = -V_{\max}\,\mathrm{d}t$，从 $0$ 到 $t$ 积分得隐式形式。记 $w = [S]/K_{\mathrm{M}}$，它变为 $w\mathrm{e}^w = (S_0/K_{\mathrm{M}})\mathrm{e}^{(S_0 - V_{\max}t)/K_{\mathrm{M}}}$，由 $W$ 求逆。$\square$

一条从饱和底物浓度一直到远低于 $K_{\mathrm{M}}$ 的进程曲线，在一次实验中就包含了完整的速率律，即 $v$ 对 $[S]$ 的关系。它能否确定参数取决于设计，下一节会说明。

### 14.6.3. 计算拟合

最小化使用 Gauss–Newton 的思想：把残差 $\boldsymbol{r}(\boldsymbol{\theta}) = (y_k - \hat y_k(\boldsymbol{\theta}))/\sigma_k$ 在当前估计处线性化，$\boldsymbol{r}(\boldsymbol{\theta} + \boldsymbol{\delta}) \approx \boldsymbol{r} - J_{\boldsymbol{r}}\boldsymbol{\delta}$，对 $\boldsymbol{\delta}$ 解线性最小二乘问题；**Levenberg–Marquardt 法**加入阻尼项 $\lambda\operatorname{diag}(J_{\boldsymbol{r}}^{\mathsf T}J_{\boldsymbol{r}})$，使线性化较差时的步长变成短的梯度步（[3.5.5](/3.5.5#sec-5.1.5)、[算法 11.4.1](/7.7.11#alg-11.4.1)）。对动力学模型，残差的 Jacobi 矩阵就是输出灵敏度的矩阵：$J_{\boldsymbol{r}}$ 的元素是 $(\partial\hat y_k/\partial\theta_j)/\sigma_k$，可由灵敏度方程 (14.6) 得到。计算它们有三种方法，参数多时效率依次提高：

| 方法 | 每个梯度的代价 | 精度 | 用途 |
|---|---|---|---|
| 有限差分 | $q + 1$ 次求解 | 受求解器容差限制 | 小模型、快速检查 |
| 前向灵敏度，式 (14.6) | 一个含 $m(q + 1)$ 个方程的扩展系统 | 与求解器一样准确 | 数十个参数时的默认方法 |
| 伴随方法 | 一次前向和一次后向的 $m$ 个方程的求解 | 与求解器一样准确 | 许多参数、标量目标（基于梯度的优化器） |

通过求解器的自动微分，如 Julia 和 JAX 生态中那样，可以不必手工推导方程而计算两种形式。

### 14.6.4. 局部极小与多起点

非线性最小二乘问题可能有多个局部极小，迭代方法收敛到它所在的盆地的极小。含振荡、时间延迟或多模式的模型的误差曲面常常崎岖不平，找到的极小依赖于初值。

![拟合振荡时的局部极小（模拟：对 y = 2 + sin(2πt + 0.5) 在四个周期内的 41 次测量加上标准差为 0.2 的 Gaussian 噪声；模型 y = c + a sin ωt + b cos ωt 对 c、a、b 是线性的，对角频率 ω 是非线性的）。A：数据、最佳拟合（ω = 6.29），以及 Levenberg–Marquardt 从初值 ω = 4 出发到达的拟合，它是一个没有抓住振荡的局部极小。B：对每个 ω 对 c、a、b 最小化后的残差平方和：一个靠近 2π 的深极小和六个浅极小。下方：从 0.5 到 15 之间均匀抽取的 200 个 ω 初值到达的频率：每次运行都终止于自己盆地的极小（13 个向 ω = 0 漂移，10 个超过 15），19.5 % 到达最佳极小](./plots/multistart.py)

**例 14.6.1** 图中最佳拟合的残差平方和为 $1.04$（噪声的期望值为 $41 \times 0.04 = 1.64$，再减去拟合的参数），$\omega = 4.00$ 附近的局部极小为 $19.8$，接近常数模型的值 $20$：它拟合了一个缓慢的弱波动，几乎什么也没有解释。从随机初始频率出发的 $200$ 次 Levenberg–Marquardt 运行中，有 $39$ 次（$19.5\,\%$）找到最佳极小。

有两种标准的补救办法。多起点：从分布在合理区域内的许多起点（对速率常数取对数尺度上的均匀分布，或 Latin 超立方）运行局部优化器，保留最好的结果；如果从不同起点反复找到最好的值，它大概就是全局极小；如果最好的几个极小的 $\chi^2$ 几乎相等而参数不同，则说明数据无法区分它们。全局优化器（差分进化、散射搜索、**模拟退火**）更系统地探索空间，通常之后再做局部精修；对已发表的信号转导和代谢网络模型的基准测试发现，用带灵敏度的基于梯度的局部优化器做多起点（Raue 及其同事，2013）以及全局搜索与局部精修的混合（Villaverde 及其同事，2019）是最有效的策略。若模型对某些参数是线性的，如这里的 $c$、$a$、$b$，则可对其余参数的每个取值用线性最小二乘消去它们，剩下低维的搜索（B 图中的轮廓）。参数的界限保证物理意义，但估计值落在界限上是模型或数据不足的警告，而不是结果。

## 14.7. 不确定性、可辨识性与模型选择

### 14.7.1. 可辨识性

拟合给出数字；问题是其中哪些是数据所确定的。

**定义 14.7.1（可辨识性）** 模型的参数 $\theta_j$ 对于给定的实验是*结构可辨识*的，如果对来自该实验的无噪声数据，观测唯一地确定其值（全局的，或在邻域内局部的）；否则不同的参数值会产生相同的观测。结构可辨识的参数对于给定的数据集是*实际可辨识*的，如果在通常的水平上其**置信区间**是有限的。第一种意义上的**可辨识性**是模型和实验设计的性质，第二种还取决于数据的数量和质量。

**例 14.7.1** 基因在 $t = 0$ 时被诱导，$\dot x = ku - \gamma x$，$u = 1$，$x(0) = 0$，用荧光 $y = sx$ 测量，标度 $s$ 未知。则 $y(t) = (sk/\gamma)(1 - \mathrm{e}^{-\gamma t})$：数据确定 $\gamma$ 和乘积 $sk$，但不能分别确定 $s$ 和 $k$。任何乘积相同的 $(s, k)$ 拟合得一样好。补救办法或者是通过校准固定标度，或者把模型重新参数化为可辨识的组合。

**例 14.7.2** 受产物竞争性抑制的酶遵循 $\mathrm{d}[S]/\mathrm{d}t = -V_{\max}[S]/\bigl(K_{\mathrm{M}}(1 + [P]/K_{\mathrm{p}}) + [S]\bigr)$。在一条进程曲线中 $[P] = S_0 - [S]$，所以分母为 $a + b[S]$，其中 $a = K_{\mathrm{M}}(1 + S_0/K_{\mathrm{p}})$，$b = 1 - K_{\mathrm{M}}/K_{\mathrm{p}}$，该曲线恰好是一条表观常数为 $K' = a/b$ 和 $V' = V_{\max}/b$ 的 Michaelis–Menten 进程曲线。三个参数通过两个组合进入：由一条进程曲线，产物抑制在结构上无法与更大的 $K_{\mathrm{M}}$ 区分。取 $K_{\mathrm{M}} = 10$，$V_{\max} = 1$，$K_{\mathrm{p}} = 20$，$S_0 = 50$，则 $K' = 70$，$V' = 2$；带噪声（$\sigma = 0.5$，$15$ 个点）的模拟曲线用普通 Michaelis–Menten 拟合得 $K' = 94$，$V' = 2.47$，用产物抑制模型拟合得到的 $\chi^2$ 与之在八位数字上相同；残差 Jacobi 矩阵的第三个奇异值为 $7 \times 10^{-7}$，而前两个为 $147$ 和 $13.7$。从几个不同的 $S_0$ 出发的进程曲线中，$[P]$ 与 $[S]$ 独立变化，使三个参数都可辨识（例 14.7.5）。

结构可辨识性可以用符号方法检验，即微分代数或输出的 Taylor 级数展开（SIAN 或 StructuralIdentifiability.jl 等工具），也可以用数值方法检验，即在随机参数值处取灵敏度矩阵的秩：奇异值为零，如例 14.7.2，揭示了一个不改变输出的参数组合。

### 14.7.2. Fisher 信息及其谱

在最优点附近，优度函数近似是二次的，$\chi^2(\hat{\boldsymbol{\theta}} + \boldsymbol{\delta}) \approx \chi^2(\hat{\boldsymbol{\theta}}) + \boldsymbol{\delta}^{\mathsf T}F\boldsymbol{\delta}$，其中 $F = J_{\boldsymbol{r}}^{\mathsf T}J_{\boldsymbol{r}}$ 是该实验在 Gaussian 误差下的 **Fisher 信息矩阵**。它的逆近似估计量的协方差（**Cramér–Rao 不等式**，[3.2.3](/3.2.3#sec-3.4.5)），Wald 区间为 $\hat\theta_j \pm 1.96\sqrt{(F^{-1})_{jj}}$。$F$ 的特征向量是数据独立确定的参数组合，特征值度量确定得多好；极端特征值之比（$F$ 的**条件数**）达到许多个数量级，意味着有些组合几乎没有被确定。生化网络的模型的特征值通常均匀地分布在许多个十倍程上，这种性质称为松散性（sloppiness，[7.6.40](/7.6.40#sec-40.1.3)）：少数刚性的组合被数据固定，而大多数没有。

![由酶进程曲线辨识 K_M 与 V_max（模拟：K_M = 10，V_max = 1；对产物的 15 次测量，Gaussian 误差的标准差为 S₀ 的 2 %；模型：公式 14.6.2）。低设计：S₀ = 2（0.2 K_M），时间 2 至 60；高设计：S₀ = 50（5 K_M），时间 6 至 90。A：数据与拟合曲线。B：K_M 的轮廓似然及 95 % 阈值 3.84；低设计的轮廓对所有大的 K_M 都低于阈值，所以 K_M 没有置信上限，而高设计给出闭区间。C：每种设计 300 个参数自助数据集的估计值（对数坐标轴）；对低设计，它们沿直线 V_max/K_M = 0.1（虚线）散布，这是数据所确定的组合；星号：真值](./plots/progress_curve.py)

**例 14.7.3** 图中两种设计都用对数参数拟合。对低设计（$S_0 = 0.2K_{\mathrm{M}}$），估计值为 $K_{\mathrm{M}} = 15.1$，$V_{\max} = 1.47$，$\ln\hat K_{\mathrm{M}}$ 与 $\ln\hat V_{\max}$ 的相关系数为 $0.9998$，$F$ 的特征值为 $0.30$ 和 $3211$，条件数为 $1.1 \times 10^4$；$K_{\mathrm{M}}$ 的 Wald 区间为 $1.1$ 至 $205$。对高设计（$S_0 = 5K_{\mathrm{M}}$）：$K_{\mathrm{M}} = 13.3$，$V_{\max} = 1.07$，相关系数 $0.983$，特征值 $20$ 和 $6555$（条件数 $328$），Wald 区间 $8.8$ 至 $20.1$。在低底物浓度时，速率为 $v \approx (V_{\max}/K_{\mathrm{M}})[S]$，一级衰减只确定比值：小特征值的特征向量沿 $\ln V_{\max} - \ln K_{\mathrm{M}} = \text{常数}$ 的方向，而比值本身确定得很好（自助区间 $0.088$ 至 $0.116$，真值 $0.1$）。

### 14.7.3. 轮廓似然

二次近似恰恰在最需要的地方失效：对确定得不好的参数，似然远非二次，Wald 区间可能错得离谱（它们按构造在对数尺度上是对称的）。**轮廓似然**（[3.5.4](/3.5.4#sec-4.1.3)）避免了这种近似：把一个参数固定在网格上的每个值，重新优化所有其他参数，并记录最好的 $\chi^2$。

**公式 14.7.1（轮廓似然置信区间）** 记 $\chi^2_{\mathrm{PL}}(\theta_j) = \min_{\boldsymbol{\theta}_{-j}}\chi^2(\theta_j, \boldsymbol{\theta}_{-j})$，则集合
$$
\bigl\{\theta_j : \chi^2_{\mathrm{PL}}(\theta_j) - \chi^2(\hat{\boldsymbol{\theta}}) \le \chi^2_{1, 0.05}\bigr\}, \qquad \chi^2_{1, 0.05} = 3.84,
$$
由**似然比检验**统计量的渐近分布，是 $\theta_j$ 的近似 $95\,\%$ 置信区间。如果一个参数的轮廓在一侧或两侧不超过阈值，它就是实际不可辨识的；如果轮廓是平的，则是结构不可辨识的。

**例 14.7.4（续）** 在图的 B 部分，高设计的 $K_{\mathrm{M}}$ 轮廓在 $8.9$ 和 $19.8$ 处穿过 $3.84$，是围绕真值 $10$ 的闭区间，与 Wald 区间相近。对低设计，它在左侧 $3.6$ 处穿过，但当 $K_{\mathrm{M}} \to \infty$ 时只升到 $0.55$：不存在上限，因为 $K_{\mathrm{M}} \gg S_0$ 时每条进程曲线都是同样的指数衰减。Wald 区间 $1.1$ 至 $205$ 在两侧都歪曲了事实。参数自助法（C 图）与轮廓一致：低设计的 $K_{\mathrm{M}}$ 估计中有 $26\,\%$ 超过 $100$，有的高出许多个数量级。

轮廓还有第二个用途：沿着一个不可辨识参数的轮廓跟踪其他参数，显示它们之间的函数关系（这里是 $V_{\max}/K_{\mathrm{M}}$ 为常数），这提示了重新参数化或能打破它的实验。预测的轮廓，对模型输出而不是参数用同样方式计算，显示即使参数没有确定，预测是否被确定：在松散模型中，依赖于刚性组合的预测往往是精确的。

### 14.7.4. Monte Carlo 与自助法

真实参数未知，数据只是实验的一次实现，其他实现会给出其他估计。区间应当描述的就是这些估计的分布。

- *Monte Carlo（参数自助法）。* 假定拟合参数接近真值且误差模型正确；在与真实数据相同的时间点上，用拟合模型和估计的噪声模拟许多合成数据集；逐个拟合；估计值围绕拟合值的离散度，估计原估计围绕真值的离散度（**参数自助法**，[3.5.7](/3.5.7#sec-7.4)）。若 $\sigma$ 未知，则用单位权重的 $\chi^2$ 除以 $n - q$ 来估计。
- *非参数自助法。* 若误差分布未知，就对数据本身重抽样。对时间点有放回地重抽样是经典的做法；对时间过程，相邻的点不可交换，对残差重抽样（把重抽样的残差加到拟合曲线上）或对整个重复实验重抽样更符合设计。

两者每个重复都要做一次完整的拟合，并且都继承了多起点的问题：每个重复都必须仔细拟合，否则离散度反映的是优化器的失败。

### 14.7.5. 模型选择

参数更多的模型至少拟合得一样好；问题是它是否拟合得显著更好。对用于同一数据的嵌套模型，额外平方和 **F 检验**（[公式 11.6.1](/7.7.11#fml-11.6.1)）比较
$$
F = \frac{(\chi^2_{\mathrm{simple}} - \chi^2_{\mathrm{complex}})/(q_{\mathrm{complex}} - q_{\mathrm{simple}})}{\chi^2_{\mathrm{complex}}/(n - q_{\mathrm{complex}})}
$$
与 $F$ 分布；当 $\sigma$ 已知时，把似然比统计量 $\chi^2_{\mathrm{simple}} - \chi^2_{\mathrm{complex}}$ 与自由度为 $q_{\mathrm{complex}} - q_{\mathrm{simple}}$ 的 $\chi^2$ 比较。均方误差 $\chi^2/(n - q)$ 也有帮助：若它增大而 $\chi^2$ 减小，说明额外的参数并不值得。对非嵌套模型，**赤池信息准则** $\mathrm{AIC} = n\ln(\mathrm{RSS}/n) + 2q$（$\sigma$ 为估计值时）或**贝叶斯信息准则**在拟合与复杂度之间权衡（[7.7.11](/7.7.11#sec-11.8)）。

**例 14.7.5** 由例 14.7.2 的产物抑制模型模拟三条 $S_0 = 10$、$25$ 和 $50$ 的进程曲线（每条 $15$ 个点，$\sigma = 0.5$），并用两个模型拟合。Michaelis–Menten（$K_{\mathrm{M}} = 17.5$，$V_{\max} = 0.96$）给出 $\chi^2 = 259.3$；产物抑制模型（$K_{\mathrm{M}} = 10.2$，$V_{\max} = 1.03$，$K_{\mathrm{p}} = 17.3$）在 $42$ 个自由度上给出 $\chi^2 = 33.6$，拟合是适当的。$F = 282$，自由度 $1$ 与 $42$，$p = 3 \times 10^{-20}$；Michaelis–Menten 的 AIC 为 $20.4$，产物抑制为 $-69.5$。Michaelis–Menten 拟合的残差不需任何检验就显示了缺失的机制：对 $S_0 = 50$，前七个点为负，后七个点为正。

### 14.7.6. 验证

拟合良好的模型是一个假设；当它能预测没有用于拟合的东西时才变得有用。

1. 物理意义：速率常数为正，亲和力和浓度在合理范围内，参数没有卡在界限上。
2. 独立测量：把拟合值与直接测量的值（纯化酶的 $K_{\mathrm{M}}$、追踪实验的降解速率）或事先已知的极限行为比较。
3. 扰动：用实验改变一个参数（过表达一个酶、加入抑制剂、改变输入），检查模型无论是否重新拟合都能预测新的数据，且改变的是正确的参数。
4. 群体之间的对比：疾病状态的模型应当把差异放在认为病变所在的参数上（哮喘中较高的气道阻力、糖尿病中较低的胰岛素敏感性）。
5. 按条件的交叉验证：用一些条件（输入、剂量、突变体）拟合并预测其他条件；检验机制的是对被留出条件的预测，而不是对同一实验中被留出时间点的预测（**交叉验证**，[7.7.21](/7.7.21)）。

## 14.8. 用 Python 完成一次拟合

下面的代码完成例 14.7.2 与例 14.7.5 的分析：用 `solve_ivp` 模拟模型，在对数参数下做带界限的多起点信赖域拟合（从较差的起点出发的无界 Levenberg–Marquardt 可能漂移到荒谬的速率常数，那里每次求解都变得很慢），Fisher 信息与 Wald 区间，$K_{\mathrm{p}}$ 的轮廓似然，以及参数自助法。

```python
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
from scipy import stats

# Model: Michaelis-Menten enzyme with competitive product inhibition, three progress curves
S0s = [10.0, 25.0, 50.0]
t_obs = np.linspace(6, 90, 15)
sigma = 0.5                                     # known measurement error (same units as P)

def rhs(t, s, KM, Vmax, Kp, S0):
    S = s[0]
    return [-Vmax * S / (KM * (1 + (S0 - S) / Kp) + S)]

def predict(logp, S0, t=t_obs):
    KM, Vmax, Kp = np.exp(logp)                 # log parameters keep rates positive
    sol = solve_ivp(rhs, (0, t[-1]), [S0], t_eval=t, args=(KM, Vmax, Kp, S0),
                    method="LSODA", rtol=1e-6, atol=1e-9)
    return S0 - sol.y[0]                        # product P(t)

def residuals(logp, data):
    return np.concatenate([(predict(logp, S0) - y) / sigma for S0, y in zip(S0s, data)])

rng = np.random.default_rng(1)
true = np.log([10.0, 1.0, 20.0])
data = [predict(true, S0) + rng.normal(0, sigma, t_obs.size) for S0 in S0s]

# 1. multistart trust-region fits within bounds (rate constants between 1e-3 and 1e3)
lo, hi = np.log(1e-3), np.log(1e3)
starts = rng.uniform(np.log(0.1), np.log(100), size=(10, 3))
fits = [least_squares(residuals, x0, args=(data,), bounds=(lo, hi)) for x0 in starts]
best = min(fits, key=lambda f: f.cost)
chi2 = 2 * best.cost
print("estimates", np.exp(best.x), "chi2", chi2, "dof", 3 * t_obs.size - 3)

# 2. Fisher information and Wald intervals (on the log scale)
J = best.jac                                    # sensitivities of the scaled residuals
cov = np.linalg.inv(J.T @ J)
print("FIM eigenvalues", np.linalg.eigvalsh(J.T @ J))
se = np.sqrt(np.diag(cov))
print("Wald 95% CI", np.exp(best.x - 1.96 * se), np.exp(best.x + 1.96 * se))

# 3. profile likelihood of Kp
def profile(logKp):
    f = least_squares(lambda q: residuals([q[0], q[1], logKp], data), best.x[:2], method="lm")
    return 2 * f.cost - chi2
grid = best.x[2] + np.linspace(-1.5, 1.5, 31)
prof = np.array([profile(g) for g in grid])
inside = np.exp(grid[prof <= stats.chi2.ppf(0.95, 1)])
print("profile 95% CI for Kp", inside.min(), inside.max())

# 4. parametric bootstrap
boot = []
for b in range(100):
    yb = [predict(best.x, S0) + rng.normal(0, sigma, t_obs.size) for S0 in S0s]
    boot.append(least_squares(residuals, best.x, args=(yb,), method="lm").x)
print("bootstrap 95% CI", np.exp(np.percentile(boot, [2.5, 97.5], axis=0)))
```

按所示运行，得到 $K_{\mathrm{M}} = 10.16$，$V_{\max} = 1.030$，$K_{\mathrm{p}} = 17.35$，在 $42$ 个自由度上 $\chi^2 = 33.6$；Fisher 信息的特征值为 $35$、$261$ 和 $26\,421$（条件数 $755$：三个参数都被确定，但程度不同）；Wald 区间为 $K_{\mathrm{M}}$：$8.3$ 至 $12.5$，$V_{\max}$：$0.97$ 至 $1.09$，$K_{\mathrm{p}}$：$13.1$ 至 $23.0$；$K_{\mathrm{p}}$ 的轮廓似然区间为 $14.2$ 至 $21.2$（在 $\ln K_{\mathrm{p}}$ 步长为 $0.1$ 的网格上）；参数自助区间为 $8.2$ 至 $12.3$、$0.98$ 至 $1.10$ 和 $13.5$ 至 $22.2$。真值 $10$、$1$ 和 $20$ 都落在所有这些区间内。用三条不同 $S_0$ 的曲线，在单条曲线中混淆的参数（例 14.7.2）被分开了，三种区间几乎一致，因为似然接近二次；对松散的参数则不会如此（例 14.7.4）。

## 小结

| 步骤 | 关键对象 | 公式或规则 | 陷阱 | 节 |
|---|---|---|---|---|
| 写出模型 | 化学计量矩阵、速率律 | $\dot{\boldsymbol{x}} = N\boldsymbol{v}(\boldsymbol{x}, \boldsymbol{p})$，式 (14.1) | 有歧义的示意图；单位错误 | 14.2.1, 14.2.4 |
| 约化它 | 守恒基团、准稳态 | $\boldsymbol{\ell}N = \boldsymbol{0}$（定理 14.2.1）；$E_{\mathrm{T}}/(S_0 + K_{\mathrm{M}}) \ll 1$（公式 14.2.1） | 酶与底物浓度相当时标准 QSSA 失效 | 14.2.2, 14.2.3 |
| 求解它 | Euler、Runge–Kutta、隐式方法 | 阶数 1 与 4（定理 14.3.1）；Euler 在 $h < 2/\lambda$ 时稳定 | 首次积分漂移；刚性 | 14.3 |
| 分析它 | Jacobi 矩阵、零倾线、分岔 | 迹与行列式；$\operatorname{tr}J = 0$ 处 Hopf（例 14.4.2） | 分岔附近的瞬态 | 14.4 |
| 问什么重要 | 灵敏度、控制系数 | 式 (14.6)、(14.7)；$C^S = -(ND\varepsilon)^{-1}ND$，$C^J = I + \varepsilon C^S$（定理 14.5.1）；$R^Y_X = C^Y_i\varepsilon^{v_i}_X$（定理 14.5.2） | 局部与全局灵敏度 | 14.5 |
| 拟合它 | $\chi^2$、似然 | 公式 14.6.1；带灵敏度的 Levenberg–Marquardt | 局部极小（多起点）；线性化 | 14.6 |
| 能信任它吗？ | 可辨识性、Fisher 信息、轮廓、自助法 | 定义 14.7.1；公式 14.7.1 | 松散参数的 Wald 区间 | 14.7.1–14.7.4 |
| 选择并检验它 | F 检验、AIC；验证 | 例 14.7.5 | 拟合不等于验证 | 14.7.5, 14.7.6 |

- 机制明确时写速率方程是机械的；守恒律来自 $N$ 的左零空间，准稳态约化需要时间尺度分离，且必须检验（公式 14.2.1，例 14.2.3）。
- Euler 方法为 $1$ 阶并有稳定性限制；带自适应步长的 Runge–Kutta 方法是默认选择，刚性网络用隐式方法（例 14.3.3：$65\,630$ 对 $463$ 次计算）。
- Bier 模型（定义 14.4.1）通过 $K_{\mathrm{m}} = 15.24$ 处的超临界 Hopf 分岔而振荡（例 14.4.2）。
- 在网络中，控制是分担的，并且在不同分支之间可以为负（例 14.5.2）；药物的效应是它的弹性系数乘以其靶标的控制系数（定理 14.5.2）。
- 拟合确定的是参数的组合；单个参数是否被确定取决于设计（例 14.7.1–14.7.4），可靠的检验是轮廓似然，而不是曲率。

## 思考题

1. 写出可逆磷酸化循环 $X \to X_{\mathrm{p}}$（激酶，速率 $v_1$）与 $X_{\mathrm{p}} \to X$（磷酸酶，速率 $v_2$）的化学计量矩阵，以及激酶形成复合物 $K + X \rightleftharpoons KX \to K + X_{\mathrm{p}}$ 的扩展机制的化学计量矩阵。求两种情形下的守恒律。

   **答** 物种为 $(X, X_{\mathrm{p}})$ 的循环：$N = \begin{bmatrix} -1 & 1 \\ 1 & -1\end{bmatrix}$，秩为 $1$，一条守恒律 $(1, 1)$：$[X] + [X_{\mathrm{p}}] = X_{\mathrm{T}}$。物种为 $(K, X, KX, X_{\mathrm{p}})$、反应为结合、解离、催化、去磷酸化的扩展机制：$N = \begin{bmatrix} -1 & 1 & 1 & 0 \\ -1 & 1 & 0 & 1 \\ 1 & -1 & -1 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix}$，秩为 $2$（第三行是第一行的相反数，第二行与第四行之和是第三行的相反数）。两条守恒律：$(1, 0, 1, 0)$，总激酶量 $[K] + [KX]$；以及 $(0, 1, 1, 1)$，总底物 $[X] + [KX] + [X_{\mathrm{p}}]$。剩下两个独立变量。

2. 对 $\dot x = -\lambda x$，证明经典 Runge–Kutta 方法每步把 $x$ 乘以 $R(z) = 1 + z + z^2/2 + z^3/6 + z^4/24$，其中 $z = -h\lambda$，并求 $\lambda = 60$（例 14.3.3 的快特征值）时最大的稳定步长。要到达 $t = 1500$ 需要多少步？

   **答** 代入 $f = -\lambda x$：$k_1 = zx/h$，$k_2 = z(1 + z/2)x/h$，$k_3 = z(1 + z/2 + z^2/4)x/h$，$k_4 = z(1 + z + z^2/2 + z^3/4)x/h$，$x_{n+1} = x_n[1 + \tfrac16(z + 2z(1 + z/2) + 2z(1 + z/2 + z^2/4) + z(1 + z + z^2/2 + z^3/4))] = R(z)x_n$，即 $\mathrm{e}^z$ 的 Taylor 多项式。在负实轴上 $R(z)$ 保持为正，并且恰在 $-2.785 < z < 0$ 时 $\lvert R(z)\rvert < 1$（$R(-2.785) = 1$）。所以 $h < 2.785/60 = 0.046$，$1500/0.046 \approx 32\,000$ 步，约 $130\,000$ 次计算，与 `RK45`（其稳定域相近）的数量级一致，尽管仅就精度而言，瞬态之后允许数十个时间单位的步长。

3. 在 Bier 模型（式 14.5）中，取 $V_{\mathrm{in}} = 0.36$，$k_1 = 0.02$，$k_{\mathrm{p}} = 6$，若把葡萄糖供给提高到 $V_{\mathrm{in}} = 0.5$，Hopf 分岔的临界 $K_{\mathrm{m}}$ 如何变化？解释之。

   **答** 对 $V_{\mathrm{in}} = 0.5$，$T^* = 2V_{\mathrm{in}}K_{\mathrm{m}}/(k_{\mathrm{p}} - 2V_{\mathrm{in}}) = K_{\mathrm{m}}/5$，所以 $T^* + K_{\mathrm{m}} = 1.2K_{\mathrm{m}}$。条件 $(T^* + K_{\mathrm{m}})^2 = k_{\mathrm{p}}/k_1 = 300$ 给出 $K_{\mathrm{m}} = 17.32/1.2 = 14.43$，比 $15.24$ 低。振荡要求 $K_{\mathrm{m}} < 14.43$：供给更高时，稳态的 ATP 水平相对于 $K_{\mathrm{m}}$ 更高，ATP 酶更饱和，自催化项 $k_{\mathrm{p}}T^*/(T^* + K_{\mathrm{m}})^2$ 必须克服更大的阻尼 $k_1T^*$；需要更小的 $K_{\mathrm{m}}$。行列式仍为正，所以分岔仍是 Hopf 型。

4. 证明：对两步途径 $X_0 \to S \to P$，定理 14.5.1 给出 $C^J_1 = \varepsilon_2/(\varepsilon_2 - \varepsilon_1)$ 与 $C^J_2 = -\varepsilon_1/(\varepsilon_2 - \varepsilon_1)$，其中 $\varepsilon_i = \varepsilon^{v_i}_S$，以及 $C^S_1 = -C^S_2 = 1/(\varepsilon_2 - \varepsilon_1)$。

   **答** $N = \begin{bmatrix} 1 & -1\end{bmatrix}$，$D = J\,I$（两个通量都等于 $J$），$\varepsilon = (\varepsilon_1, \varepsilon_2)^{\mathsf T}$。于是 $ND\varepsilon = J(\varepsilon_1 - \varepsilon_2)$，$ND = J\begin{bmatrix} 1 & -1\end{bmatrix}$，所以 $C^S = -\begin{bmatrix} 1 & -1\end{bmatrix}/(\varepsilon_1 - \varepsilon_2) = \begin{bmatrix} 1 & -1\end{bmatrix}/(\varepsilon_2 - \varepsilon_1)$。$C^J = I + \varepsilon C^S$：$C^J_{11} = 1 + \varepsilon_1/(\varepsilon_2 - \varepsilon_1) = \varepsilon_2/(\varepsilon_2 - \varepsilon_1)$，$C^J_{12} = -\varepsilon_1/(\varepsilon_2 - \varepsilon_1)$；第二行相同，因为两个通量相等。这就是 7.1.17 的[式 (17.5)](/7.1.17#eq-17.5)。增加酶 1 使 $S$ 升高（$C^S_1 > 0$，因为 $\varepsilon_2 > 0 \ge \varepsilon_1$），增加酶 2 使它降低，两者同倍数变化则 $S$ 不变。

5. 一种药物对例 14.5.2 的酶 4 做非竞争性抑制，$v_4 \propto 1/(1 + I/K_I)$。利用参考状态的控制系数（$C^{J_P}_4 = -0.25$，$C^{J_Q}_4 = 0.68$），估计小剂量 $I = 0.05K_I$ 时 $J_P$ 与 $J_Q$ 的相对变化。为什么大剂量时估计变得不准确？

   **答** $\varepsilon^{v_4}_I = -I/(K_I + I) = -0.05/1.05 = -0.048$。该剂量使 $v_4$ 减小为原来的 $1/1.05$，即代谢物固定时 $\ln v_4$ 改变 $-\ln 1.05 = -0.049$。由定理 14.5.2，通量改变 $C^{J}_4 \times (-0.049)$：$\ln J_P$ 改变 $+0.012$，$\ln J_Q$ 改变 $-0.033$，即 $J_P$ 升高约 $1.2\,\%$，$J_Q$ 降低约 $3.3\,\%$。响应系数是导数；剂量大时控制系数本身随状态变化（$I = 0.25$ 时，$C^{J_P}_4 = -0.19$，$C^{J_Q}_4 = 0.75$，例 14.5.3），所以必须通过求解新的稳态，或对响应系数沿剂量积分来计算响应。

6. 在基因诱导模型 $\dot x = \beta - \alpha x$，$x(0) = 0$ 中，在时刻 $t_k$ 以恒定误差 $\sigma$ 测量，计算由时刻 $t$ 的单次测量得到的 $(\beta, \alpha)$ 的 Fisher 信息矩阵，并证明一个时间点无法辨识两个参数，而两个时间点可以（当 $\alpha t$ 不小时）。

   **答** 用例 14.5.1 的灵敏度，$\boldsymbol{g}(t) = (\partial x/\partial\beta, \partial x/\partial\alpha)$，一次测量给出 $F = \boldsymbol{g}\boldsymbol{g}^{\mathsf T}/\sigma^2$，是秩一矩阵：一个参数组合被确定，另一个没有（一个数不能固定两个参数）。两个时间给出 $F = (\boldsymbol{g}_1\boldsymbol{g}_1^{\mathsf T} + \boldsymbol{g}_2\boldsymbol{g}_2^{\mathsf T})/\sigma^2$，若 $\boldsymbol{g}_1$ 与 $\boldsymbol{g}_2$ 不平行则秩为二。比值 $(\partial x/\partial\alpha)/(\partial x/\partial\beta) = -\beta/\alpha + \beta t\mathrm{e}^{-\alpha t}/(1 - \mathrm{e}^{-\alpha t})$ 随 $t$ 变化（从小 $t$ 时的 $\approx -\beta t/2$ 到大 $t$ 时的 $-\beta/\alpha$），所以两个不同的时间给出独立的向量；但如果两个时间都很早，向量几乎平行（$\boldsymbol{g} \approx (t, -\beta t^2/2)$ 只在较小的第二个分量上不同），$F$ 病态，$\alpha$ 实际不可辨识，如[例 1.5.1](/7.9.1#ex-1.5.1)。一次测量在上升期，一次在平台期，是有效的设计。

7. 解释为什么在例 14.7.4 的低设计中，$K_{\mathrm{M}}$ 的轮廓似然当 $K_{\mathrm{M}} \to \infty$ 时趋于有限极限（比极小值高 $0.55$）而不是上升。怎样的实验能以最少的额外工作使 $K_{\mathrm{M}}$ 可辨识？

   **答** 对 $K_{\mathrm{M}} \gg S_0$，速率律在极限下恰为 $v = (V_{\max}/K_{\mathrm{M}})[S]$，所以进程曲线族收敛到指数衰减 $[S] = S_0\mathrm{e}^{-kt}$，$k = V_{\max}/K_{\mathrm{M}}$；对每个 $K_{\mathrm{M}}$ 重新优化 $V_{\max}$ 使 $k$ 保持其最佳值，$\chi^2$ 趋于最佳一级拟合的值，它只比最佳 Michaelis–Menten 拟合稍差（$0.55$），差异在噪声之内。数据无法排除一级动力学。要使 $K_{\mathrm{M}}$ 可辨识，需要底物浓度达到或高于 $K_{\mathrm{M}}$，在那里显示出饱和：再增加一条 $S_0$ 为 $K_{\mathrm{M}}$ 数倍的进程曲线就够了（如给出 $8.9$ 至 $19.8$ 的高设计）。

8. 在例 14.7.5 中，假设给定的 $\sigma = 0.5$ 正确，计算两个模型的均方误差 $\chi^2/(n - q)$ 并解释。然后解释为什么对单条进程曲线（例 14.7.2）无法做 F 检验。

   **答** Michaelis–Menten：$259.3/43 = 6.03$；产物抑制：$33.6/42 = 0.80$。权重正确时，好模型的（加权）均方误差接近 $1$：简单模型的 $6$ 表明拟合不足（它在 $43$ 个自由度上的 $\chi^2 = 259$ 对应 $p < 10^{-30}$），复杂模型与噪声一致。对单条曲线，两个模型给出相同的 $\chi^2$（八位数字），因为产物抑制与更大的 $K_{\mathrm{M}}$ 在结构上不可区分；$F = 0$，检验没有功效。F 检验只能比较对所做实验作出不同预测的模型；设计必须先于检验。

9. （设计题）你想由刺激后八个时间点上双磷酸化 MAPK 的 Western blot，估计三激酶级联（MAPKKK、MAPKK、MAPK，每个都有激酶和磷酸酶步骤）的速率常数。概述建模流程、你预期的可辨识性问题，并提出额外的测量。

   **答** (i) 模型：写出详细的机制（每一级的单磷酸化与双磷酸化、磷酸酶、每个激酶总量守恒），用 Michaelis–Menten 或质量作用速率律，并加一个刺激输入；约 $15$ 到 $25$ 个参数。(ii) 观测模型：Western blot 测量相对量，每张膜有未知的标度，并有乘性误差，所以加入标度因子并拟合对数；这已经使绝对浓度和某些速率常数在结构上不可辨识（例 14.7.1）。(iii) 用带灵敏度的多起点 Levenberg–Marquardt 在对数参数下拟合；检查最佳极小被反复找到。(iv) 可辨识性：一个输出的八个点无法确定二十个参数；预期 Fisher 谱松散，大多数速率常数的轮廓是平的；计算轮廓以确定哪些组合被确定（激活与失活的时间尺度、总增益）。(v) 额外的测量：上游激酶的磷酸化（每一层都变得可观测）、几个刺激剂量（暴露饱和与超敏）、抑制剂扰动与磷酸酶抑制（分开正向与逆向速率）、激酶总量的绝对定量（用靶向质谱，[7.9.9](/7.9.9)）以消除标度问题，以及更密的早期时间点。(vi) 在留出的条件（新的剂量或抑制剂）上验证，并以轮廓似然区间而不是单个参数值报告预测。

10. 一位同事拟合了一条时间过程，报告 $R^2 = 0.995$。列出在接受拟合参数之前你会要求的三项检查。

    **答** (i) 残差：对时间作图；同号残差成串意味着即使 $R^2$ 很高也有系统失配，并且用已知测量误差计算的 $\chi^2$ 应与 $n - q$ 个自由度一致。(ii) 可辨识性与不确定性：每个参数的轮廓似然（或仔细重新拟合的自助法）；高 $R^2$ 并不说明参数是否被确定，Wald 标准误可能有误导性。(iii) 全局最优性：从广泛分布的初值做多起点，说明报告的极小是找到的最佳值，以及是否存在 $\chi^2$ 相近而参数不同的其他极小。此外：参数不在界限上且在物理上合理；与更简单模型的比较（F 检验或 AIC）；以及对一个独立条件的预测。
