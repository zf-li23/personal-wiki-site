---
title: 古典方程与适定问题
source_hash: bbec310b149b
---

**偏微分方程**把多元未知函数与它的偏导数联系起来。物理、化学与生物中几乎所有的连续介质模型都取这种形式：弦的位移、杆中的温度、化学物质的浓度、区域中的电势。本章介绍这门学科的基本术语，以及本课程其余部分研究的三个古典二阶方程：波动方程、热方程与 Laplace 方程。我们从守恒律推导出每个方程，说明怎样的初始条件与边界条件构成合理的问题，并给出 Hadamard 的适定问题概念。最后把二阶线性方程分为双曲型、抛物型与椭圆型。这种分类不只是归档：每一类都有自己的定性性态（有限传播速度、光滑化、平衡）和自己的方法，后面各章逐一展开：一阶方程见 [2.5.2](/2.5.2)，波动方程见 [2.5.3](/2.5.3)，分离变量法见 [2.5.4](/2.5.4) 与 [2.5.5](/2.5.5)，积分变换见 [2.5.6](/2.5.6)，热方程见 [2.5.7](/2.5.7)，Laplace 方程见 [2.5.8](/2.5.8)。所用的工具来自微积分（**Gauss 公式**，[2.2.14](/2.2.14#thm-14.2.1)；**Fourier 级数**，[2.2.9](/2.2.9)）与常微分方程（特征线，[2.4.14](/2.4.14)；Sturm–Liouville 问题，[2.4.12](/2.4.12)）。

## 1.1. 基本概念

### 1.1.1. 阶、解与线性

记 $u_x=\frac{\partial u}{\partial x}$，$u_{xy}=\frac{\partial^2u}{\partial y\,\partial x}$，等等；时间变量为 $t$，$\Omega\subset\mathbb{R}^n$ 表示以 $\partial\Omega$ 为边界的区域。

**定义 1.1.1（阶与古典解）** 未知函数 $u(x_1,\dots,x_n)$ 的偏微分方程是一个关系式

$$
F\big(x,u,Du,D^2u,\dots,D^mu\big)=0,\qquad x\in\Omega,\tag{1.1}
$$
其中 $D^ku$ 表示 $u$ 的全部 $k$ 阶偏导数，且 $D^mu$ 确实出现。数 $m$ 称为方程的**阶**。在 $\Omega$ 的每一点都满足式 (1.1) 的函数 $u\in C^m(\Omega)$ 称为**古典解**。

以后会遇到可微性不足、不能逐点满足方程的解（[2.5.2](/2.5.2) 的激波，[2.5.3](/2.5.3) 的"拨弦"）；目前"解"都指古典解。

**定义 1.1.2（线性方程与非线性方程）** 把式 (1.1) 中不含 $u$ 的项都移到右端，写成 $\mathcal{L}u=f$。

1. 若对一切函数 $u,v$ 与常数 $\alpha,\beta$ 有 $\mathcal{L}(\alpha u+\beta v)=\alpha\mathcal{L}u+\beta\mathcal{L}v$，则称方程是**线性**的；$f\equiv0$ 时称为**齐次**的，否则称为非齐次的。
2. 若方程关于最高阶 $m$ 阶导数是线性的，其系数只依赖于 $x$，而低阶项可以非线性地依赖于 $u$ 及其低于 $m$ 阶的导数，则称为**半线性方程**。
3. 若方程关于 $m$ 阶导数是线性的，其系数可以依赖于 $x$ 以及 $u$ 的低于 $m$ 阶的导数，则称为**拟线性方程**。
4. 其余情形称为**完全非线性方程**。

每一类都包含前一类。下表列出本课程及其应用中出现的方程（$c,k,D>0$ 为常数）。

| 方程 | 名称 | 阶 | 类型 |
|---|---|---|---|
| $u_t+cu_x=0$ | 输运方程 | 1 | 线性，齐次 |
| $u_t+uu_x=0$ | 无粘 Burgers 方程 | 1 | 拟线性 |
| $u_x^2+u_y^2=1$ | 程函方程 | 1 | 完全非线性 |
| $u_{tt}=c^2\Delta u$ | 波动方程 | 2 | 线性，齐次 |
| $u_t=k\Delta u+f(x,t)$ | 有源热方程 | 2 | 线性，非齐次 |
| $\Delta u=0$，$\Delta u=f$ | Laplace 方程与 Poisson 方程 | 2 | 线性 |
| $u_t=D\Delta u+u(1-u)$ | Fisher–KPP 方程 | 2 | 半线性 |
| $\operatorname{div}\Big(\dfrac{\nabla u}{\sqrt{1+\lvert\nabla u\rvert^2}}\Big)=0$ | 极小曲面方程 | 2 | 拟线性 |
| $u_t+6uu_x+u_{xxx}=0$ | Korteweg–de Vries 方程 | 3 | 半线性 |

Fisher–KPP 方程是最简单的**反应扩散方程**；这类方程描述种群扩张与化学斑图（[7.4](/7.4)）。

### 1.1.2. 叠加原理

线性齐次方程的解集是向量空间：这就是**叠加原理**，本课程中几乎所有求解线性方程的方法都以它为基础。

**定理 1.1.1（叠加原理）** 设 $\mathcal{L}$ 是 $m$ 阶线性微分算子。

1. 若 $u_1,\dots,u_N$ 是 $\mathcal{L}u=0$ 的解，则每个线性组合 $\sum_{j=1}^Nc_ju_j$ 也是；若 $u_p$ 是 $\mathcal{L}u=f$ 的解，则 $\mathcal{L}u=f$ 的每个解都具有 $u_p+v$ 的形式，其中 $\mathcal{L}v=0$。
2. 若 $u_1,u_2,\dots$ 是 $\mathcal{L}u=0$ 的解，级数 $u=\sum_{j=1}^\infty c_ju_j$ 收敛，且所有不超过 $m$ 阶的导数构成的级数在 $\Omega$ 的紧子集上**一致收敛**，则 $u$ 也是 $\mathcal{L}u=0$ 的解。

**证明** 第 1 条即线性性。第 2 条中，求导后级数的一致收敛性允许逐项求导（[2.2.9](/2.2.9#thm-9.1.6)），所以 $\mathcal{L}u=\sum c_j\mathcal{L}u_j=0$。$\square$

分离变量法需要的正是第 2 条（[2.5.4](/2.5.4)）：那里的解是简单解的无穷级数，必须验证收敛性条件。没有这一条件结论可能不成立，因为光滑函数的级数可能收敛到不可微的函数。

常微分方程的通解含有任意常数，偏微分方程的通解则含有任意函数。例如 $u_{xy}=0$ 说明 $u_x$ 与 $y$ 无关，所以 $u_x=f(x)$，对 $x$ 积分得

$$
u(x,y)=F(x)+G(y),
$$
其中 $F,G$ 是任意 $C^1$ 函数。因此线性齐次偏微分方程的解空间是无穷维的，要确定一个解，需要在整条曲线或整个曲面上给出条件，而不是在一点上。

## 1.2. 古典方程的推导

三个古典方程都表达一个平衡律：对一小段弦用 Newton 第二定律，对物体的一小块用能量守恒。做法总是相同的：对任意小区域写出平衡关系，把边界项化为体积分，再利用区域的任意性得到逐点成立的方程。

### 1.2.1. 弦振动

考虑沿 $x$ 轴张紧、在一个平面内振动的完全柔软的弹性弦，设 $u(x,t)$ 是它的横向位移。假设运动是纯横向的，斜率很小（$\lvert u_x\rvert\ll1$），弦的线密度 $\rho$ 为常数，张力沿切线方向。设 $\theta$ 是切线与 $x$ 轴的夹角，则在略去 $u_x^2$ 阶的项后，$\sin\theta\approx\tan\theta=u_x$，$\cos\theta\approx1$。

取 $[x,x+\Delta x]$ 上的一段弦。由于没有水平运动，两端张力的水平分量 $T\cos\theta$ 相互平衡，所以在一阶近似下两端的张力 $T$ 相同，与 $x$ 无关；微小振动不会使弦明显伸长，所以 $T$ 也与时间无关。竖直分量为 $T\sin\theta\approx Tu_x$，于是设单位长度上的外力密度为 $F(x,t)$，由 Newton 第二定律，

$$
\rho\,\Delta x\,u_{tt}(\bar x,t)=T\big[u_x(x+\Delta x,t)-u_x(x,t)\big]+F(\hat x,t)\,\Delta x,
$$
其中 $\bar x,\hat x$ 是区间中的某两点。除以 $\Delta x$ 并令 $\Delta x\to0$，

$$
u_{tt}=c^2u_{xx}+f(x,t),\qquad c=\sqrt{T/\rho},\quad f=F/\rho.\tag{1.2}
$$
常数 $c$ 具有速度的量纲；[2.5.3](/2.5.3) 将说明它就是扰动沿弦传播的速度。对张紧的薄膜作同样的论证，得到 $u_{tt}=c^2(u_{xx}+u_{yy})$；声学方程（气体中的微小压力扰动）与电磁学方程（真空中场的每个分量）给出三维的形式。

**定义 1.2.1（波动方程）** 方程

$$
u_{tt}=c^2\Delta u,\qquad x\in\mathbb{R}^n,\ t\in\mathbb{R},\tag{1.3}
$$
称为**波动方程**，其中 $\Delta=\partial_{x_1}^2+\cdots+\partial_{x_n}^2$ 是关于空间变量的 **Laplace 算子**，$c>0$；右端有 $f(x,t)$ 时称为非齐次波动方程。

### 1.2.2. 热传导与扩散

设 $u(x,t)$ 是物体在点 $x\in\mathbb{R}^3$ 处的温度，物体的密度 $\rho$、比热 $c_{\mathrm{p}}$ 与热导率 $\kappa$ 都是常数。需要两条物理定律。

1. 区域 $V$ 中的热能为 $\iiint_Vc_{\mathrm{p}}\rho u\,\mathrm{d}V$。
2. Fourier 定律（Fourier's law）：热量从高温处流向低温处，流速与温度梯度成正比；热流密度向量为 $\boldsymbol{q}=-\kappa\nabla u$。

设 $V$ 是以分段光滑曲面 $\partial V$ 为边界的任意区域，$\boldsymbol{n}$ 是外单位法向量，$F(x,t)$ 是内部热源在单位体积内的产热率。能量守恒说的是：$V$ 中热量的变化率等于经 $\partial V$ 流入的热流量加上内部产生的热量：

$$
\frac{\mathrm{d}}{\mathrm{d}t}\iiint_Vc_{\mathrm{p}}\rho u\,\mathrm{d}V=-\iint_{\partial V}\boldsymbol{q}\cdot\boldsymbol{n}\,\mathrm{d}S+\iiint_VF\,\mathrm{d}V.
$$
由 Gauss 公式，通量项等于 $\iiint_V\nabla\cdot(\kappa\nabla u)\,\mathrm{d}V$，再在积分号下求导，

$$
\iiint_V\big(c_{\mathrm{p}}\rho u_t-\kappa\Delta u-F\big)\,\mathrm{d}V=0.
$$
被积函数连续，且它在每个区域 $V$ 上的积分都为零，所以它恒为零（若它在某点为正，则在该点附近的小球上为正）。因此

$$
u_t=k\Delta u+f,\qquad k=\frac{\kappa}{c_{\mathrm{p}}\rho},\quad f=\frac{F}{c_{\mathrm{p}}\rho}.\tag{1.4}
$$
常数 $k$ 称为热扩散率。完全相同的推导适用于在介质中扩散的物质的浓度 $u$：用 Fick 定律（Fick's law）$\boldsymbol{q}=-D\nabla u$ 代替 Fourier 定律，$D$ 是扩散系数。若热导率随空间变化，推导给出的则是 $c_{\mathrm{p}}\rho u_t=\nabla\cdot(\kappa(x)\nabla u)+F$。

**定义 1.2.2（热方程）** 方程

$$
u_t=k\Delta u,\qquad k>0,\tag{1.5}
$$
称为**热方程**（也称扩散方程）；右端有 $f(x,t)$ 时称为非齐次热方程。

波动方程关于时间是二阶的，热方程是一阶的。这一差别有深刻的后果：波动方程在时间上可逆（若 $u(x,t)$ 是解，则 $u(x,-t)$ 也是），而热方程描述的是不可逆过程，它抹平不规则性，只能沿时间正向求解（§1.4）。

### 1.2.3. 稳态：Laplace 方程与 Poisson 方程

若热源与边界温度都与时间无关，温度趋于 $u_t=0$ 的稳态，由式 (1.4)，稳态满足 $k\Delta u+f=0$。同样的方程也出现在不随时间变化的载荷下薄膜的稳定形状、静电势（$\Delta\varphi=-\rho_{\mathrm{e}}/\varepsilon_0$，$\rho_{\mathrm{e}}$ 为电荷密度）、引力势，以及不可压缩无旋流动的速度势中（速度 $\boldsymbol{v}=\nabla\varphi$ 满足 $\nabla\cdot\boldsymbol{v}=0$，所以 $\Delta\varphi=0$）。

**定义 1.2.3（Laplace 方程与 Poisson 方程）** 方程

$$
\Delta u=0\tag{1.6}
$$
称为 **Laplace 方程**，它的 $C^2$ 解就是**调和函数**（[2.2.14](/2.2.14#sec-14.5.2)）。非齐次方程 $\Delta u=f$ 称为 **Poisson 方程**。

物理学家常把 Poisson 方程写成 $-\Delta u=f$，使正的源产生正的解；符号只是约定。在二元情形，调和函数恰好是解析函数的实部，这把这个方程与复分析联系起来（[2.3](/2.3)，[2.5.8](/2.5.8)）。

三个方程放在一起看：波动方程描述振动与传播，热方程描述向平衡的弛豫，Laplace 方程描述平衡本身。

## 1.3. 初始条件与边界条件

### 1.3.1. 初始条件

单独一个偏微分方程有无穷多个解；附加条件从中选出描述特定物理情形的那一个。在初始时刻 $t=0$ 给出的条件称为初始条件。热方程关于 $t$ 是一阶的，需要一个初始条件，即初始温度

$$
u(x,0)=\varphi(x).
$$
波动方程关于 $t$ 是二阶的，与质点的 Newton 方程一样，需要初始位移与初始速度：

$$
u(x,0)=\varphi(x),\qquad u_t(x,0)=\psi(x).
$$
Laplace 方程描述不随时间演化的状态，没有初始条件。

### 1.3.2. 边界条件

若物体占据有界区域 $\Omega$，还需要在边界 $\partial\Omega$ 上给出条件。设 $\boldsymbol{n}$ 是外单位法向量，$\frac{\partial u}{\partial\boldsymbol{n}}=\nabla u\cdot\boldsymbol{n}$ 是法向导数。

**定义 1.3.1（边界条件）** 设 $g$ 是 $\partial\Omega$ 上的已知函数（对发展方程，$g$ 还依赖于 $t$）。

1. $\partial\Omega$ 上的 $u=g$ 称为 **Dirichlet 边界条件**（第一类边界条件）；
2. $\partial\Omega$ 上的 $\dfrac{\partial u}{\partial\boldsymbol{n}}=g$ 称为 **Neumann 边界条件**（第二类边界条件）；
3. $\partial\Omega$ 上的 $\dfrac{\partial u}{\partial\boldsymbol{n}}+\alpha u=g$（$\alpha>0$ 是函数）称为 **Robin 边界条件**（第三类边界条件）。

$g\equiv0$ 时称边界条件是齐次的。

它们是 [2.4.12](/2.4.12#sec-12.4.1) 中常微分方程边界条件的多维形式。它们的物理意义如下：

| 条件 | 热传导 | 弦振动（$x=l$ 为端点） |
|---|---|---|
| Dirichlet | 边界温度给定（恒温热浴） | 端点按给定方式运动；$u(l,t)=0$ 为固定端 |
| Neumann | 热流 $-\kappa\frac{\partial u}{\partial\boldsymbol{n}}$ 给定；$g=0$ 为绝热边界 | 端点在竖直导轨上自由滑动：$u_x(l,t)=0$（无竖直方向的力） |
| Robin | Newton 冷却定律：$-\kappa\frac{\partial u}{\partial\boldsymbol{n}}=H(u-u_{\mathrm{env}})$，与温度为 $u_{\mathrm{env}}$ 的外界交换热量 | 端点系在劲度系数为 $K$ 的弹簧上：$Tu_x(l,t)=-Ku(l,t)$ |

Robin 条件中 $\alpha>0$ 是符合物理的符号：物体比外界热时热量流出。混合条件（$\partial\Omega$ 的不同部分上给出不同类型的条件）也很常见。对无界区域上的问题，改为在无穷远处给出增长或衰减条件，例如 $u$ 有界。

### 1.3.3. 定解问题的类型

方程连同它的初始条件与边界条件，称为该方程的定解问题。定解问题分为三类：

- **初值问题**（Cauchy 问题）：方程在全空间上，只有初始条件；
- **边值问题**：方程在 $\Omega$ 内，只有边界条件（Laplace 方程的典型情形）；边界条件是 Dirichlet 条件时称为 Dirichlet 问题，是 Neumann 条件时称为 Neumann 问题；
- 初边值问题，两种条件都有。

**定义 1.3.2（初边值问题）** 发展方程在 $\Omega\times(0,T)$ 上、在 $t=0$ 时给出初始条件、在 $\partial\Omega\times(0,T)$ 上给出边界条件的定解问题，称为**初边值问题**（混合问题）。

例如，长为 $l$、左端保持温度 $0$、右端绝热的杆中的热传导，是初边值问题

$$
\begin{cases}u_t=ku_{xx},&0<x<l,\ t>0,\\u(0,t)=0,\quad u_x(l,t)=0,&t>0,\\u(x,0)=\varphi(x),&0\le x\le l.\end{cases}\tag{1.7}
$$
这类问题的古典解要求在区域内部关于 $x$ 是 $C^2$ 的、关于 $t$ 是 $C^1$ 的，并且连续到边界（在给出 Neumann 或 Robin 条件的边界上，$u_x$ 也连续到边界），使条件有意义。在角点 $(0,0)$ 与 $(l,0)$ 处的连续性对数据提出了相容性条件：在 (1.7) 中需要 $\varphi(0)=0$。数据不相容时（把一根初始温热的杆浸入冰水中），解在角点处不连续；[2.5.4](/2.5.4) 的公式仍然有意义，解在 $t>0$ 时是古典解。

## 1.4. 适定性

偏微分方程的定解问题来自模型，模型中的数据是测量得到的，因而只是近似已知。所以一个有用的问题应当有解、只有一个解，而且数据稍有变化时解变化不大。

**定义 1.4.1（适定问题）** 若偏微分方程的定解问题满足

1. （存在性）对每一组容许的数据都有解；
2. （唯一性）解是唯一的；
3. （稳定性）解连续依赖于数据：数据（用适当的范数度量）的微小变化只引起解的微小变化，

则称它是（Hadamard 意义下）**适定**的。不适定的问题称为不适定问题。

条件 3 是常微分方程中**连续依赖性**（[2.4.7](/2.4.7)）的类比。范数是定义的一部分：例如对波动方程，用最大值或能量来度量数据与解。本课程中的古典问题都是适定的：波动方程的初值问题（[2.5.3](/2.5.3)），热方程的初值问题与初边值问题（[2.5.7](/2.5.7)），以及 Laplace 方程的 Dirichlet 问题（[2.5.8](/2.5.8)）。这个定义的要点在于，适定性取决于条件的类型是否与方程的类型相匹配，下面的经典例子说明了这一点。

**例 1.4.1（Hadamard 的例子）** 考虑上半平面 $y>0$ 中 Laplace 方程的初值问题：

$$
u_{xx}+u_{yy}=0,\qquad u(x,0)=0,\qquad u_y(x,0)=\frac{\sin nx}{n},
$$
其中 $n$ 是正整数。直接验证可知它的解（由 Holmgren 唯一性定理，解是唯一的）为

$$
u_n(x,y)=\frac{1}{n^2}\sinh ny\,\sin nx.
$$
$n\to\infty$ 时数据一致地趋于 $0$：$\sup_x\lvert u_y(x,0)\rvert=\frac1n\to0$。零数据对应的解是 $u\equiv0$。但对每个固定的 $y>0$，

$$
\sup_x\lvert u_n(x,y)\rvert=\frac{\sinh ny}{n^2}\to+\infty.
$$
任意小的数据在任何正的高度上都产生任意大的解：问题不稳定，因而不适定。

![Hadamard 的例子：Cauchy 数据 sin(nx)/n 收缩到零（左），而解在高度 y = 0.5, 1, 2 处的振幅 sinh(ny)/n² 随 n 指数增长（右）](./plots/hadamard-example.py)

同样的初始数据对波动方程 $u_{yy}=u_{xx}$（以 $y$ 为时间）则完全合理：解是 $\frac1{n^2}\sin ny\sin nx$，始终很小。Laplace 方程描述平衡，平衡由闭曲线上的边值决定，而不是由一条直线上的"位置与速度"决定。同一现象的第二个例子是逆时间方向求解的热方程。

**例 1.4.2（逆向热方程）** 在 $0<x<\pi$ 上，取 $u(0,t)=u(\pi,t)=0$，函数 $u_n=\mathrm{e}^{-n^2t}\sin nx$ 满足 $u_t=u_{xx}$。设要由时刻 $T>0$ 的温度反推初始温度。终值数据 $u(x,T)=\varepsilon\sin nx$ 对应初始状态 $u(x,0)=\varepsilon\mathrm{e}^{n^2T}\sin nx$：终值数据中大小为 $\varepsilon$ 的变化使初始状态改变 $\varepsilon\mathrm{e}^{n^2T}$，它关于 $n$ 无界。热传导以指数速度抹去细节（高频分量）的信息，所以由现在重建过去是不稳定的。

不适定问题并非没有意义：图像去模糊、计算机断层成像等反问题都属于这一类。它们需要关于解的额外先验信息（正则化），这是一个专门的课题。

## 1.5. 二阶线性方程的分类

### 1.5.1. 两个自变量

两个自变量的二阶线性方程的一般形式是

$$
Au_{xx}+2Bu_{xy}+Cu_{yy}+Du_x+Eu_y+Fu=G,\tag{1.8}
$$
其中系数是 $(x,y)$ 的函数，$A,B,C$ 不同时为零。二阶项（主部）决定方程的性质。它们对应于矩阵为 $M=\begin{bmatrix}A&B\\B&C\end{bmatrix}$ 的**二次型** $A\xi^2+2B\xi\eta+C\eta^2$，正如二次曲线 $Ax^2+2Bxy+Cy^2=1$ 按 $B^2-AC$ 的符号分为双曲线、抛物线与椭圆。

**定义 1.5.1（双曲型、抛物型与椭圆型方程）** 在点 $(x_0,y_0)$ 处，若

1. $B^2-AC>0$，则称式 (1.8) 为**双曲型方程**；
2. $B^2-AC=0$，则称为**抛物型方程**；
3. $B^2-AC<0$，则称为**椭圆型方程**。

若方程在区域的每一点都属于某一类型，则称它在该区域内属于这一类型。

把波动方程写成 $u_{tt}-c^2u_{xx}=0$（变量为 $(t,x)$，$A=1$，$B=0$，$C=-c^2$），得 $B^2-AC=c^2>0$：双曲型。热方程 $ku_{xx}-u_t=0$ 有 $A=k$，$B=C=0$：抛物型。Laplace 方程 $u_{xx}+u_{yy}=0$ 有 $B^2-AC=-1$：椭圆型。类型可以随点变化：跨声速气体动力学中的 Tricomi 方程 $yu_{xx}+u_{yy}=0$ 有 $B^2-AC=-y$，所以在 $y>0$ 时是椭圆型的（亚声速流），在 $y<0$ 时是双曲型的（超声速流），在直线 $y=0$ 上是抛物型的。

类型是方程本身的性质，与坐标无关。设

$$
\xi=\xi(x,y),\qquad\eta=\eta(x,y)
$$
是 **Jacobi 行列式** $J=\xi_x\eta_y-\xi_y\eta_x$ 不为零的 $C^2$ 变量替换，记 $u(x,y)=w(\xi,\eta)$。由**链式法则**，$u_x=w_\xi\xi_x+w_\eta\eta_x$，且

$$
u_{xx}=w_{\xi\xi}\xi_x^2+2w_{\xi\eta}\xi_x\eta_x+w_{\eta\eta}\eta_x^2+w_\xi\xi_{xx}+w_\eta\eta_{xx},
$$
$u_{xy}$ 与 $u_{yy}$ 类似。代入式 (1.8) 得到同一形式的方程

$$
\bar Aw_{\xi\xi}+2\bar Bw_{\xi\eta}+\bar Cw_{\eta\eta}+(\text{含 }w_\xi,w_\eta,w\text{ 的项})=G,
$$
其中

$$
\begin{aligned}
\bar A&=A\xi_x^2+2B\xi_x\xi_y+C\xi_y^2,\\
\bar B&=A\xi_x\eta_x+B(\xi_x\eta_y+\xi_y\eta_x)+C\xi_y\eta_y,\\
\bar C&=A\eta_x^2+2B\eta_x\eta_y+C\eta_y^2.
\end{aligned}\tag{1.9}
$$

**定理 1.5.1** 在 Jacobi 行列式 $J\ne0$ 的变量替换下，新系数 (1.9) 满足

$$
\bar B^2-\bar A\bar C=J^2\,(B^2-AC).
$$
特别地，式 (1.8) 在一点处的类型与坐标的选取无关。

**证明** 设 $P=\begin{bmatrix}\xi_x&\xi_y\\\eta_x&\eta_y\end{bmatrix}$ 是变量替换的 **Jacobi 矩阵**。把乘积展开即可验证，式 (1.9) 恰好说明

$$
\begin{bmatrix}\bar A&\bar B\\\bar B&\bar C\end{bmatrix}=P\begin{bmatrix}A&B\\B&C\end{bmatrix}P^{\mathsf T}.
$$
取行列式，$\bar A\bar C-\bar B^2=(\det P)^2(AC-B^2)=J^2(AC-B^2)$。$\square$

### 1.5.2. 特征线与标准形

分类的想法是选取新坐标，使主部尽可能简单，就像把二次型化为主轴形式。由式 (1.9)，$\bar A$ 为零恰好当 $\xi$ 满足一阶方程

$$
A\xi_x^2+2B\xi_x\xi_y+C\xi_y^2=0.\tag{1.10}
$$
若 $\xi_y\ne0$，等值线 $\xi(x,y)=\text{常数}$ 的斜率为 $\frac{\mathrm{d}y}{\mathrm{d}x}=-\frac{\xi_x}{\xi_y}$；把 $\xi_x=-\xi_y\frac{\mathrm{d}y}{\mathrm{d}x}$ 代入式 (1.10) 并除以 $\xi_y^2$，可知式 (1.10) 等价于等值线所满足的一个常微分方程。

**定义 1.5.2（特征方程与特征线）** 常微分方程

$$
A\Big(\frac{\mathrm{d}y}{\mathrm{d}x}\Big)^2-2B\frac{\mathrm{d}y}{\mathrm{d}x}+C=0,\qquad\text{即}\qquad A\,(\mathrm{d}y)^2-2B\,\mathrm{d}x\,\mathrm{d}y+C\,(\mathrm{d}x)^2=0,\tag{1.11}
$$
称为式 (1.8) 的**特征方程**，它的积分曲线称为式 (1.8) 的**特征线**。

$A\ne0$ 时，式 (1.11) 分解为

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{B\pm\sqrt{B^2-AC}}{A},
$$
所以双曲型方程有两族实特征线，抛物型方程有一族，椭圆型方程没有（根是复数）。特征线是这样的曲线：沿着它，方程不能由曲线上 $u$ 及其一阶导数的值确定 $u$ 的全部二阶导数；[2.5.3](/2.5.3) 将说明，对波动方程，特征线就是信号传播的路径。对 Tricomi 方程，式 (1.11) 成为 $y(\mathrm{d}y)^2+(\mathrm{d}x)^2=0$，它只在 $y<0$ 时有实解：此时 $\frac{\mathrm{d}x}{\mathrm{d}y}=\pm\sqrt{-y}$，特征线是曲线 $x\pm\frac23(-y)^{3/2}=\text{常数}$。

![Tricomi 方程 y u_xx + u_yy = 0 的类型区域与特征线：y > 0 时为椭圆型；y < 0 时为双曲型，两族特征线 x ± (2/3)(-y)^(3/2) = const 在抛物型直线 y = 0 上形成尖点](./plots/tricomi-characteristics.py)

**定理 1.5.2（标准形）** 设式 (1.8) 的系数充分光滑（椭圆型情形要求解析），且方程在一点的某个邻域内类型不变。则在该点附近存在坐标 $(\xi,\eta)$，使方程化为下列标准形（canonical form）之一，其中省略号表示不超过一阶的项：

1. 双曲型：$w_{\xi\eta}+\cdots=0$，或等价地（令 $\alpha=\xi+\eta$，$\beta=\xi-\eta$）$w_{\alpha\alpha}-w_{\beta\beta}+\cdots=0$；
2. 抛物型：$w_{\eta\eta}+\cdots=0$；
3. 椭圆型：$w_{\xi\xi}+w_{\eta\eta}+\cdots=0$。

**证明**（双曲型情形）设 $\varphi_1(x,y)=C_1$ 与 $\varphi_2(x,y)=C_2$ 分别是式 (1.11) 两个因式的通积分，$\nabla\varphi_1,\nabla\varphi_2\ne\boldsymbol{0}$。$\varphi_1$ 与 $\varphi_2$ 都满足式 (1.10)，且由于两族特征线的斜率不同，它们是独立的。取 $\xi=\varphi_1$，$\eta=\varphi_2$，则 $J\ne0$，且由式 (1.9) 得 $\bar A=\bar C=0$；由定理 1.5.1，$\bar B^2=J^2(B^2-AC)>0$，所以可以除以 $2\bar B$。

（抛物型情形）只有一族特征线 $\varphi(x,y)=C$；取 $\xi=\varphi$，$\eta$ 为任一使 $J\ne0$ 的函数。则 $\bar A=0$，由定理 1.5.1 得 $\bar B^2=\bar A\bar C=0$，所以 $\bar B=0$；由于主部不能恒为零，$\bar C\ne0$，除以 $\bar C$ 即可。

（椭圆型情形）特征方程给出式 (1.10) 的一个复解 $\varphi=\alpha+\mathrm{i}\beta$（这里用到了解析性）。把 $A\varphi_x^2+2B\varphi_x\varphi_y+C\varphi_y^2=0$ 的实部与虚部分开，对坐标 $\xi=\alpha$、$\eta=\beta$ 恰好得到 $\bar A=\bar C$ 与 $\bar B=0$。$\square$

常系数时特征线是直线，标准形可以手工求出，如下面的例子所示；化为标准形往往是求通解的第一步。

**例 1.5.1** 求 $u_{xx}+2u_{xy}-3u_{yy}=0$ 的通解。

**解** 这里 $A=1$，$B=1$，$C=-3$，$B^2-AC=4>0$：双曲型。特征方程 $(y')^2-2y'-3=0$ 给出 $y'=3$ 与 $y'=-1$，所以特征线是直线 $y-3x=C_1$ 与 $y+x=C_2$。取 $\xi=y-3x$，$\eta=y+x$，由式 (1.9) 得 $\bar A=\bar C=0$，$\bar B=1\cdot(-3)\cdot1+1\cdot(-3\cdot1+1\cdot1)+(-3)\cdot1\cdot1=-8$，所以方程化为 $-16w_{\xi\eta}=0$，即 $w_{\xi\eta}=0$。与 §1.1.2 一样，$w=F(\xi)+G(\eta)$，于是

$$
u(x,y)=F(y-3x)+G(y+x),
$$
其中 $F,G$ 是任意 $C^2$ 函数。

**例 1.5.2** 求 $u_{xx}+2u_{xy}+u_{yy}=0$ 的通解。

**解** $A=B=C=1$，$B^2-AC=0$：抛物型。特征方程 $(y'-1)^2=0$ 只有一族特征线 $y-x=C$。取 $\xi=y-x$，$\eta=x$。则 $\bar A=0$，$\bar B=0$，$\bar C=1$，方程化为 $w_{\eta\eta}=0$，从而 $w=F(\xi)+\eta\,G(\xi)$，

$$
u(x,y)=F(y-x)+x\,G(y-x).
$$
（事实上，方程就是 $(\partial_x+\partial_y)^2u=0$。）

**例 1.5.3** 把 $u_{xx}+2u_{xy}+5u_{yy}=0$ 化为标准形。

**解** $B^2-AC=1-5=-4<0$：椭圆型。特征方程 $(y')^2-2y'+5=0$ 有复根 $y'=1\pm2\mathrm{i}$，复特征线为 $y-x\mp2\mathrm{i}x=C$。取实部与虚部 $\xi=y-x$，$\eta=2x$。则 $P=\begin{bmatrix}-1&1\\2&0\end{bmatrix}$，且

$$
P\begin{bmatrix}1&1\\1&5\end{bmatrix}P^{\mathsf T}=\begin{bmatrix}4&0\\0&4\end{bmatrix},
$$
所以方程化为 $w_{\xi\xi}+w_{\eta\eta}=0$：在坐标 $(\xi,\eta)$ 下它就是 Laplace 方程。

### 1.5.3. 多个自变量

$n$ 个自变量的二阶线性方程是

$$
\sum_{i,j=1}^na_{ij}(x)u_{x_ix_j}+\sum_{i=1}^nb_i(x)u_{x_i}+c(x)u=f(x),\qquad a_{ij}=a_{ji}.\tag{1.12}
$$
在每一点，对称矩阵 $(a_{ij})$ 有 $n$ 个实**特征值**。若在某点所有特征值都不为零且同号，则称式 (1.12) 在该点是椭圆型的；若所有特征值都不为零，且恰有一个与其余的异号，则称为双曲型的；若恰有一个特征值为零，其余同号，则称为抛物型的。（$n\ge4$ 时可能出现其他符号组合，例如两正两负，但应用中很少遇到。）在变量替换 $y=y(x)$ 下，矩阵按定理 1.5.1 的方式变换：$(a_{ij})\mapsto P(a_{ij})P^{\mathsf T}$，$P$ 为 Jacobi 矩阵；由 **Sylvester 惯性定律**，正、负、零特征值的个数不变，所以类型同样与坐标无关。

$a_{ij}$ 为常数时，正交变量替换使矩阵对角化（主轴），再对每个变量作伸缩，主部化为 $\pm u_{y_1y_1}\pm\cdots\pm u_{y_ny_n}$。与 $n=2$ 不同，$n\ge3$ 的变系数方程一般不能在整个邻域内化为标准形；保留下来的只是逐点的分类。

在变量 $(x_1,\dots,x_n,t)$ 下，波动方程 $u_{tt}-c^2\Delta u=0$ 的矩阵是 $\operatorname{diag}(-c^2,\dots,-c^2,1)$：双曲型。热方程的矩阵是 $\operatorname{diag}(k,\dots,k,0)$：抛物型。Laplace 方程的矩阵是单位矩阵：椭圆型。下表总结三类方程的典型特征，后面各章将逐一证明。

| 类型 | 典型方程 | 典型问题 | 特征性态 |
|---|---|---|---|
| 双曲型 | 波动方程 $u_{tt}=c^2\Delta u$ | 初值问题或初边值问题（两个初始条件） | 有限传播速度，奇性沿特征线传播，能量守恒，时间可逆 |
| 抛物型 | 热方程 $u_t=k\Delta u$ | 初值问题或初边值问题（一个初始条件） | 无穷传播速度，瞬时光滑化，极值原理，不可逆 |
| 椭圆型 | Laplace 方程 $\Delta u=0$ | 边值问题 | 平衡；解光滑，由边值决定；平均值性质与极值原理 |

## 小结

- 偏微分方程按阶与非线性程度（线性、半线性、拟线性、完全非线性）分类。线性齐次方程的解可以叠加；无穷叠加需要求导后的级数一致收敛。
- 波动方程（弦的 Newton 定律，$c^2=T/\rho$）、热方程（能量守恒与 Fourier 定律，$k=\kappa/(c_{\mathrm{p}}\rho)$）以及 Laplace 方程与 Poisson 方程（稳态）是三个古典方程。
- 定解问题由方程连同初始条件（热方程一个，波动方程两个）与边界条件（Dirichlet、Neumann、Robin）组成。若解存在、唯一且连续依赖于数据，则问题是适定的。Laplace 方程的 Cauchy 问题（Hadamard 的例子）与逆向热方程是不适定的。
- 二阶方程 $Au_{xx}+2Bu_{xy}+Cu_{yy}+\cdots=0$ 按 $B^2-AC>0$、$=0$ 或 $<0$ 分为双曲型、抛物型或椭圆型；类型在变量替换下不变。特征方程 $A(\mathrm{d}y)^2-2B\,\mathrm{d}x\,\mathrm{d}y+C(\mathrm{d}x)^2=0$ 给出把方程化为标准形的坐标。
