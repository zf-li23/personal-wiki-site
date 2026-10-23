---
title: 偏微分方程
---

在上一节中，我们讨论了常微分方程描述的种群动态，它们假设了空间是同质性的，仅关注时间变化，忽略了种群在空间中的分布与移动。然而，现实生态系统中的个体总是在空间中活动，种群密度不仅随时间变化，也随空间位置而改变，且空间为非均匀环境。为了刻画这种时空动态，我们需要引入偏微分方程（Partial Differential Equations，PDEs）。偏微分方程将时间导数和空间导数结合在一起，能够描述种群密度的演化过程，是空间生态学最重要的数学工具之一。楼元教授在综述《空间生态学中的一些反应扩散方程模型》中系统阐述了该领域的理论基础与应用，本章将结合该综述的内容，深入介绍反应-扩散模型及其数值方法。

## 5.1. 偏微分方程的基本理论

### 5.1.1. 从常微分方程到偏微分方程

常微分方程描述的是因变量（如种群密度）仅随时间的变化，忽略了空间维度。引入空间变量后，密度函数成为时间和空间的函数：$u(t,\boldsymbol{x})$，其中 $\boldsymbol{x}\in\Omega\subset\mathbb{R}^n$ 是空间坐标。一个典型的时空偏微分方程具有如下形式：

$$
F\left(t,\boldsymbol{x},u,\frac{\partial u}{\partial t},\frac{\partial u}{\partial x_1},\ldots,\frac{\partial^2 u}{\partial x_1^2},\ldots\right)=0.
$$

例如，在生态学中我们通常关注的 **反应-扩散方程（Reaction-Diffusion Equations）**，它由两项构成：
- **反应项** $f(u)$：描述局部种群动态（出生、死亡、种内与种间相互作用）；
- **扩散项** $D\nabla^2 u$：描述个体的随机移动，其中 $D>0$ 是扩散系数，$\nabla^2$ 是拉普拉斯算子，也写作 $\Delta$。

对于一维空间，方程写作
$$
\frac{\partial u}{\partial t}=D\frac{\partial^2 u}{\partial x^2}+f(u);
$$
对于二维空间，
$$
\frac{\partial u}{\partial t}=D\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right)+f(u)=D\nabla^2 u+f(u).
$$

### 5.1.2. 有限差分法基础

大多数反应-扩散方程无法求得解析解，必须借助数值方法。**有限差分法（Finite Difference Method）** 是最常用的离散化方法之一，其核心思想是用差商近似导数，将连续的偏微分方程转化为离散的代数方程组。

将空间区间 $[0,L]$ 划分为均匀网格，步长 $\Delta x$，网格点 $x_i=i\Delta x$（$i=0,1,\ldots,N$）。同样时间离散为 $t_n=n\Delta t$。记 $u_i^n\approx u(x_i,t_n)$。

一阶导数的差分近似：
- 向前差分：$\displaystyle \frac{\partial u}{\partial x}\approx\frac{u_{i+1}^n-u_i^n}{\Delta x}$，
- 向后差分：$\displaystyle \frac{\partial u}{\partial x}\approx\frac{u_i^n-u_{i-1}^n}{\Delta x}$，
- 中心差分：$\displaystyle \frac{\partial u}{\partial x}\approx\frac{u_{i+1}^n-u_{i-1}^n}{2\Delta x}$。

二阶导数的中心差分：
$$
\frac{\partial^2 u}{\partial x^2}\approx\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{(\Delta x)^2}.
$$

对于二维情况，若空间步长 $\Delta x=\Delta y=h$，则拉普拉斯算子的 **五点差分格式** 为
$$
\nabla^2 u_{i,j}\approx\frac{u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{i,j}}{h^2}.
$$

![有限差分时空网格与差分模板示意图](./plots/finite-difference-grid-and-stencils.py)

以一维反应-扩散方程 $\partial_t u = D\partial_{xx}u+f(u)$ 为例，常见的时间推进格式有：

* **显式欧拉格式**（Explicit Euler）：
  $$
  u_i^{n+1}=u_i^n+\Delta t\left(D\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{(\Delta x)^2}+f(u_i^n)\right).
  $$
  该格式简单易实现，但稳定性受 **CFL条件** 约束：$D\Delta t/(\Delta x)^2\leq 1/2$（一维）。若步长过大，数值解会发散。

* **隐式欧拉格式**（Implicit Euler）：
  $$
  u_i^{n+1}=u_i^n+\Delta t\left(D\frac{u_{i+1}^{n+1}-2u_i^{n+1}+u_{i-1}^{n+1}}{(\Delta x)^2}+f(u_i^{n+1})\right).
  $$
  隐式格式无条件稳定，但每步需解线性方程组（若 $f$ 非线性还需迭代），计算量较大。

* **Crank-Nicolson格式**：取显式与隐式的平均，时间精度为二阶：
  $$
  \begin{aligned}
  u_i^{n+1}=u_i^n+\frac{\Delta t}{2}&\left[D\frac{u_{i+1}^{n+1}-2u_i^{n+1}+u_{i-1}^{n+1}}{(\Delta x)^2}+D\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{(\Delta x)^2}\right.\\
  &\left.+f(u_i^{n+1})+f(u_i^n)\right].
  \end{aligned}
  $$
  Crank-Nicolson格式也是无条件稳定且精度较高，但同样需要求解方程组。

* **IMEX方法**（Implicit-Explicit）：对扩散项用隐式处理，对反应项用显式处理，可在保证稳定性的同时避免非线性迭代。

在有限区域 $\Omega$ 上求解PDE时，必须指定边界条件，常见类型有：

* **狄利克雷边界条件（Dirichlet）**：直接给定边界上的函数值，如 $u(0,t)=g_1(t)$。
* **诺伊曼边界条件（Neumann）**：给定边界上的外法向导数（即通量），如 $\dfrac{\partial u}{\partial\nu}=h(t)$。特别地，**零流边界** $\dfrac{\partial u}{\partial\nu}=0$ 表示边界封闭，个体不能进出。
* **周期边界条件**：适用于空间环状区域，要求 $u(0,t)=u(L,t)$ 且 $\dfrac{\partial u}{\partial x}(0,t)=\dfrac{\partial u}{\partial x}(L,t)$。

## 5.2. 扩散方程与反应-扩散方程

### 5.2.1. 纯扩散方程

纯扩散方程 $\partial_t u = D\partial_{xx}u$ 描述热量传导或物质扩散过程，其解析解可通过傅里叶级数或分离变量法得到。在生态学中，它对应于没有局部增长、仅个体随机移动的情形。

扩散现象基于 **菲克定律（Fick’s law）**：扩散通量与密度梯度成正比，且方向从高密度指向低密度。在一维情形，通量 $J$ 可表示为
$$
J=-D\frac{\partial u}{\partial x}.
$$
负号表示扩散方向与梯度方向相反。结合 **连续性方程** $\dfrac{\partial u}{\partial t}=-\dfrac{\partial J}{\partial x}$，得到纯粹扩散方程
$$
\frac{\partial u}{\partial t}=D\frac{\partial^2 u}{\partial x^2}.
$$
该方程描述了种群因随机运动而逐渐均匀分布的过程。

在数值方法下，对于显式格式，一维扩散方程的稳定性条件为
$$
D\frac{\Delta t}{(\Delta x)^2}\le\frac{1}{2}.
$$
二维情形（$\Delta x=\Delta y=h$）条件更严格：
$$
D\Delta t\left(\frac{1}{h^2}+\frac{1}{h^2}\right)=\frac{2D\Delta t}{h^2}\le\frac{1}{2}\quad\Longrightarrow\quad\frac{D\Delta t}{h^2}\le\frac{1}{4}.
$$
当反应项存在时，稳定性条件可能更复杂，通常需通过线性化分析（如von Neumann分析）确定。

![一维高斯扩散过程与二维显式格式的稳定性对比](./plots/diffusion-1d-and-2d-stability.py)

### 5.2.2. 生态学中的反应-扩散方程

回顾反应-扩散方程，对于一维空间，方程写作
$$
\frac{\partial u}{\partial t}=D\frac{\partial^2 u}{\partial x^2}+f(u);
$$
对于二维空间，
$$
\frac{\partial u}{\partial t}=D\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right)+f(u)=D\nabla^2 u+f(u).
$$

反应项 $f(u)$ 体现了种群的局部动力学，常见形式包括：

* **指数增长**：$f(u)=ru$，对应于无限资源下的无界增长。
* **逻辑斯谛增长**：$f(u)=ru(1-u/K)$，其中 $r$ 为内禀增长率，$K$ 为环境容纳量。
* **Allee效应**：$f(u)=ru(u-a)(1-u/K)$，$0<a<K$ 为Allee阈值，当密度低于 $a$ 时种群负增长。
* **捕食者-猎物相互作用**：需用两个耦合方程描述。

### 5.2.3. 反应-扩散方程的无量纲化

以带逻辑斯谛增长的反应-扩散方程为例进行无量纲化：
$$
\frac{\partial u}{\partial t}=ru\left(1-\frac{u}{K}\right)+D\frac{\partial^2 u}{\partial x^2}.
$$
引入无量纲变量：
$$
\bar{u}=\frac{u}{K},\quad \bar{x}=x\sqrt{\frac{r}{D}},\quad \bar{t}=rt,
$$
方程简化为
$$
\frac{\partial \bar{u}}{\partial \bar{t}}=\bar{u}(1-\bar{u})+\frac{\partial^2 \bar{u}}{\partial \bar{x}^2}.
$$
无量纲化减少了参数个数，突出了系统的本质特征。下文若无特别说明，尽可能采用无量纲形式。

## 5.3. Fisher-KPP 方程

### 5.3.1. 模型与行波解

Fisher-KPP 方程（Fisher-Kolmogorov-Petrovsky-Piscounov）是反应-扩散方程最经典的例子：
$$
\frac{\partial u}{\partial t}=ru(1-u)+D\frac{\partial^2 u}{\partial x^2}.
$$
它描述了具有逻辑斯谛增长的种群在一维空间中的传播。该方程存在 **行波解（traveling wave solution）**：
$$
u(x,t)=U(z),\quad z=x-ct,
$$
其中 $c$ 为波速。代入方程得到关于 $U$ 的常微分方程：
$$
-cU' = rU(1-U)+DU''.
$$

### 5.3.2. 最小波速与入侵速度

对于初始条件具有紧支集（局部化）的情形，行波最终以 **最小波速** 传播：
$$
c_{\min}=2\sqrt{rD}.
$$
这个最小波速正是种群在均匀环境中的 **入侵速度（invasion speed）**。数值模拟可以验证这一理论结果：初始时刻在局部区域放置种群，随后形成向前传播的波形，波速趋近于 $2\sqrt{rD}$。

![Fisher-KPP 方程的入侵前沿传播与波速](./plots/fisher-kpp-invasion-front.py)

## 5.4. 非均匀环境中的单种群动态

自然环境中资源分布往往是不均匀的，考虑如下单种群模型：

$$
\begin{cases}
\dfrac{\partial u}{\partial t}=d\Delta u+u(m(x)-u), & (x,t)\in\Omega\times(0,T),\\[6pt]
\dfrac{\partial u}{\partial\nu}=0, & (x,t)\in\partial\Omega\times(0,T),\\[6pt]
u(x,0)=u_0(x), & x\in\Omega,
\end{cases}
$$
其中 $m(x)$ 是空间依赖的生长率（反映资源质量），$\Omega$ 是有界区域，$\partial u/\partial\nu=0$ 表示封闭边界。

该模型存在唯一正平衡解 $\theta(x)$，满足
$$
\begin{cases}
d\Delta\theta+\theta(m-\theta)=0,&x\in\Omega,\\[4pt]
\dfrac{\partial\theta}{\partial\nu}=0,&x\in\partial\Omega.
\end{cases}
$$
总生物量 $\int_\Omega\theta(x)\,\mathrm{d}x$ 如何依赖于扩散系数 $d$？一个很粗略的回答是：对所有 $d>0$，有 $\int_\Omega\theta > \int_\Omega m$，且
$$
\lim_{d\to0^+}\int_\Omega\theta = \lim_{d\to\infty}\int_\Omega\theta = \int_\Omega m.
$$
这意味着总生物量作为 $d$ 的函数是非单调的：在扩散极慢或极快时，总生物量等于总资源量；而在某个适中的扩散系数下，总生物量达到最大值（甚至可能出现多个局部最大值）。该结论表明，适度的扩散有助于种群更有效地利用空间异质性资源。

![非均匀环境中单种群总生物量随扩散系数的变化](./plots/single-species-biomass-vs-diffusion.py)

## 5.5. 空间中的竞争模型

### 5.5.1. 均匀环境中的Lotka-Volterra竞争模型

经典的两种群竞争模型在均匀环境下可写作
$$
\begin{cases}
\dfrac{\partial u}{\partial t}=d_1\Delta u+u(a_1-b_1u-c_1v),\\[6pt]
\dfrac{\partial v}{\partial t}=d_2\Delta v+v(a_2-b_2u-c_2v),
\end{cases}
$$
并附加适当的边界条件。当系数满足 **弱竞争条件**
$$
\frac{b_1}{b_2}>\frac{a_1}{a_2}>\frac{c_1}{c_2}
$$
时，均匀环境中两物种可稳定共存。

### 5.5.2. 非均匀环境中的竞争模型

考虑资源分布 $m(x)$ 相同的简化情形：
$$
\begin{cases}
u_t = d\Delta u + u(m - u - bv),\\[4pt]
v_t = D\Delta v + v(m - cu - v),\\[4pt]
\dfrac{\partial u}{\partial\nu}=\dfrac{\partial v}{\partial\nu}=0,
\end{cases}
$$
其中 $0<b,c<1$ 保证处处满足弱竞争条件。然而，由于扩散系数的差异，竞争结果可能变为排斥，定理指出：

设 $b,c\in(0,1)$，$u^*$ 是单物种平衡解。定义 $c^* = \inf_{d>0}\dfrac{\int_\Omega m}{\int_\Omega u^*}$。若 $c>c^*$，则存在一个非空区域 $\Sigma\subset\mathbb{R}_+\times\mathbb{R}_+$，使得对 $(d,D)\in\Sigma$，半平凡平衡态 $(u^*,0)$ 是稳定的（即物种 $v$ 灭绝）。

特别地，当竞争对称（$b=c=1$）时，有更简洁的结论：

若 $b=c=1$，则：
- 若 $d<D$，则 $(u^*,0)$ 稳定，$(0,v^*)$ 不稳定；
- 若 $d>D$，则 $(0,v^*)$ 稳定，$(u^*,0)$ 不稳定；
- 若 $d=D$，则存在连续统的共存平衡解。

该定理揭示了在对称竞争下，扩散较慢的物种具有竞争优势，这与非均匀环境中的资源利用策略有关。

![非均匀环境中竞争模型的稳定区域与竞争动力学](./plots/competition-stability-regions.py)

## 5.6. 图灵不稳定性与空间格局形成

### 5.6.1. 图灵机制

1952年，图灵提出：两种具有不同扩散速率的物质（形态发生素）通过反应-扩散相互作用，可以自发形成空间斑图。这一机制同样适用于生态学中的捕食者-猎物系统或竞争系统。

考虑一般两变量反应-扩散系统：
$$
\begin{aligned}
\frac{\partial u}{\partial t} &= f(u,v) + D_u\nabla^2 u,\\
\frac{\partial v}{\partial t} &= g(u,v) + D_v\nabla^2 v.
\end{aligned}
$$
设 $(u^*,v^*)$ 为无扩散时的稳定平衡点（即 $f(u^*,v^*)=g(u^*,v^*)=0$，且 Jacobian 矩阵的特征值均有负实部）。加入扩散后，线性稳定性分析表明，若 $D_v\neq D_u$，且满足一定条件（通常要求 $D_v>D_u$），则均匀稳态可能对某些空间扰动变得不稳定，从而产生空间斑图。这种现象称为 **图灵不稳定性**。

### 5.6.2. 经典模型：Schnakenberg 系统

Schnakenberg 模型（Schnakenberg 1979 年提出的三分子反应模型，与 Brusselator 同属简单的自催化模型）是产生图灵斑图的经典例子：
$$
\begin{aligned}
f(u,v) &= a - u + u^2 v,\\
g(u,v) &= b - u^2 v,
\end{aligned}
$$
其中 $a,b>0$。通过线性稳定性分析可导出图灵不稳定的参数区域。数值模拟显示，从均匀初值添加微小随机扰动后，系统会演化出点状、条纹状或迷宫状的空间斑图，其主导波长可通过傅里叶分析确定。

![Schnakenberg 模型图灵斑图的形成及其功率谱](./plots/schnakenberg-turing-pattern.py)

### 5.6.3. 捕食者-猎物模型中的图灵斑图

考虑具有逻辑斯谛增长的捕食者-猎物模型：
$$
\begin{aligned}
\frac{\partial N}{\partial t} &= rN\left(1-\frac{N}{K}\right)-aNP + D_N\nabla^2 N,\\
\frac{\partial P}{\partial t} &= caNP - mP + D_P\nabla^2 P,
\end{aligned}
$$
其中 $N$ 为猎物密度，$P$ 为捕食者密度。当捕食者扩散系数 $D_P$ 远大于猎物扩散系数 $D_N$ 时，系统可能产生图灵斑图，形成捕食者与猎物密度的空间异质性分布。

![捕食者-猎物系统中的图灵斑图及其傅里叶谱](./plots/predator-prey-turing-patterns.py)

## 5.7. 移流效应

除随机扩散外，许多生物还能沿环境梯度进行定向运动，即 **移流（advection）**。Belgacem 和 Cosner 提出的包含移流的模型：

### 5.7.1. 单种群移流模型

$$
\begin{cases}
u_t = \nabla\cdot[d\nabla u - \alpha u\nabla m] + u(m - u), & (x,t)\in\Omega\times(0,\infty),\\[6pt]
\dfrac{\partial u}{\partial\nu} - \alpha u\dfrac{\partial m}{\partial\nu}=0, & (x,t)\in\partial\Omega\times(0,\infty),\\[6pt]
u(x,0)=u_0(x), & x\in\Omega,
\end{cases}
$$
其中 $\alpha$ 是移流系数，描述物种沿资源梯度 $\nabla m$ 的定向运动。边界条件意味着移流通量与扩散通量在边界上平衡。

### 5.7.2. 包含移流的竞争模型

Cantrell 等人进一步研究了两种群的竞争，其中一种具有移流能力：
$$
\begin{cases}
u_t = \nabla\cdot[d\nabla u - \alpha u\nabla m] + u(m - u - v),\\[4pt]
v_t = D\Delta v + v(m - u - v),\\[4pt]
d\dfrac{\partial u}{\partial\nu} - \alpha u\dfrac{\partial m}{\partial\nu}=0,\quad \dfrac{\partial v}{\partial\nu}=0,
\end{cases}
$$
移流物种 $u$ 沿资源梯度运动，而非移流物种 $v$ 仅作随机扩散。一个重要结论是：

当移流系数 $\alpha$ 充分大时，两个半平凡平衡态 $(u^*,0)$ 和 $(0,v^*)$ 都不稳定，系统至少存在一个稳定的正平衡解，即两物种可以共存。

这揭示了一个反直觉的现象：过强的定向运动反而会削弱物种的竞争优势，促使共存。数值实验可验证：小 $\alpha$ 时移流物种占优；随着 $\alpha$ 增大，系统由竞争排除转变为共存。

![移流系数对竞争结果与共存区域的影响](./plots/advection-competition-coexistence.py)

## 小结

- 反应-扩散方程 $\partial_t u = D\nabla^2 u + f(u)$ 由描述局部种群动态的反应项与描述随机移动的扩散项组成（5.1.1）；扩散项来自 Fick 定律 $J = -D\,\partial u/\partial x$ 与连续性方程（5.2.1）。常见反应项有指数增长、逻辑斯谛增长与 Allee 效应（5.2.2），无量纲化可以减少参数个数（5.2.3）。
- 有限差分法用差商代替导数（5.1.2）：

  | 格式 | 稳定性 | 代价 |
  |---|---|---|
  | 显式欧拉 | 受 CFL 条件约束，一维 $D\Delta t/(\Delta x)^2 \le 1/2$ | 简单 |
  | 隐式欧拉 | 无条件稳定 | 每步解线性方程组 |
  | Crank–Nicolson | 无条件稳定，时间二阶精度 | 每步解方程组 |
  | IMEX | 扩散隐式、反应显式 | 兼顾稳定与效率 |

  边界条件有 Dirichlet、Neumann（零流）与周期三类。
- Fisher-KPP 方程 $u_t = ru(1-u) + Du_{xx}$ 有行波解 $u = U(x - ct)$；局部化初值的入侵前沿以最小波速 $c_{\min} = 2\sqrt{rD}$ 传播（5.3）。
- 非均匀环境 $m(x)$ 中，单种群的总生物量对扩散系数 $d$ 非单调：$d \to 0^+$ 与 $d \to \infty$ 时都趋于总资源量 $\int_\Omega m$，适中的扩散下更大（5.4）。
- 空间竞争（5.5）：均匀环境中弱竞争条件保证共存；非均匀环境中扩散的差异可以使结果变为排斥，对称竞争（$b = c = 1$）时扩散较慢的物种获胜。
- 图灵不稳定性：无扩散时稳定的平衡点，在两种成分扩散速率不同（通常要求 $D_v > D_u$）时可能对某些空间扰动失稳，形成斑图；Schnakenberg 模型与捕食者扩散远快于猎物的捕食者-猎物模型都能产生图灵斑图（5.6）。
- 移流（沿资源梯度的定向运动）：移流系数 $\alpha$ 充分大时两个半平凡平衡态都不稳定，两物种共存，即过强的定向运动反而削弱竞争优势（5.7）。

## 思考题

1. **单种群引理数值验证**：取一维区域 $\Omega=[0,1]$，设资源函数 $m(x)=2+\sin(2\pi x)$，用有限差分法求解平衡态方程，计算总生物量 $\int_0^1\theta(x)\,\mathrm{d}x$ 随扩散系数 $d$ 的变化曲线。

   **答** 用有限体积法离散 $[0, 1]$（$N = 400$ 个单元，两端零通量），平衡态方程 $d\theta'' + \theta(m - \theta) = 0$ 化为非线性方程组，用 Newton 法求解；$d$ 从 $10^{-3}$ 到 $10^2$ 取对数等距的 101 个值，每个 $d$ 以上一个 $d$ 的解为初值（延拓）：

   ```python
   import numpy as np
   from scipy.sparse import diags
   from scipy.sparse.linalg import spsolve

   N = 400
   h = 1.0 / N
   x = (np.arange(N) + 0.5) * h                # cell centres
   m = 2 + np.sin(2 * np.pi * x)
   # Neumann Laplacian (finite volume, zero flux at both ends)
   main = -2 * np.ones(N); main[0] = main[-1] = -1
   Lap = diags([np.ones(N - 1), main, np.ones(N - 1)], [-1, 0, 1]) / h**2

   def steady_state(d, theta0, tol=1e-12):
       """Newton's method for d*theta'' + theta*(m - theta) = 0."""
       th = theta0.copy()
       for _ in range(100):
           F = d * (Lap @ th) + th * (m - th)
           J = d * Lap + diags(m - 2 * th)
           step = spsolve(J.tocsc(), -F)
           th += step
           if np.max(np.abs(step)) < tol:
               return th
       raise RuntimeError('Newton did not converge')

   ds = np.logspace(-3, 2, 101)
   biomass = []
   th = m.copy()
   for d in ds:                                # continuation from small to large d
       th = steady_state(d, th)
       biomass.append(th.sum() * h)
   biomass = np.array(biomass)
   k = biomass.argmax()
   print(f"int m = {m.sum() * h:.4f}")
   print(f"max biomass {biomass[k]:.4f} at d = {ds[k]:.4f}")
   for d in [1e-3, 1e-2, 0.1, 1, 10, 100]:
       i = np.argmin(np.abs(ds - d))
       print(f"d = {ds[i]:g}: biomass = {biomass[i]:.5f}")
   ```

   结果（$\int_0^1 m = 2$）：

   | $d$ | $10^{-3}$ | $10^{-2}$ | $0.1$ | $1$ | $10$ | $100$ |
   |---|---|---|---|---|---|---|
   | $\int_0^1\theta$ | 2.0050 | 2.0243 | 2.0490 | 2.0265 | 2.0037 | 2.0004 |

   总生物量对所有 $d$ 都大于 $\int_0^1 m$，在 $d \approx 0.16$ 处达到最大值 $2.0505$（比总资源量多约 $2.5\%$），$d \to 0^+$ 与 $d \to \infty$ 时都回到 $2$，与 5.4 的结论一致；把网格加密到 $N = 800$，结果不变（四位有效数字）。直观上，$d$ 很小时 $\theta \approx m$，各处只用本地资源；$d$ 很大时 $\theta$ 几乎是常数，等于 $m$ 的平均值；适中的扩散把个体从资源丰富处输送到贫乏处，而贫乏处的人均增长率 $m - \theta$ 又因密度低而较高，所以总量超过 $\int m$。$d$ 很大时 $\int\theta - \int m$ 大约按 $1/d$ 衰减（$d = 10$ 与 $d = 100$ 相差约 10 倍）。

2. **竞争模型的模拟**：在对称竞争 $b=c=1$ 下，取不同的 $(d,D)$，从随机初始条件出发，试验证扩散较慢的物种获胜的结论。

   **答** 取与第 1 题相同的 $m(x) = 2 + \sin(2\pi x)$、$\Omega = [0, 1]$、零通量边界。时间推进用 IMEX 格式：扩散项隐式（每步解一个三对角方程组，系数矩阵预先做 LU 分解），反应项显式，$\Delta t = 0.05$；初值在每个网格上取 $\mathrm{U}(0.5, 1.5)$ 的独立随机数：

   ```python
   import numpy as np
   from scipy.sparse import diags, identity
   from scipy.sparse.linalg import splu

   N = 200
   h = 1.0 / N
   x = (np.arange(N) + 0.5) * h
   m = 2 + np.sin(2 * np.pi * x)
   main = -2 * np.ones(N); main[0] = main[-1] = -1
   Lap = diags([np.ones(N - 1), main, np.ones(N - 1)], [-1, 0, 1]) / h**2

   def compete(d, D, T=3000.0, dt=0.05, seed=0):
       """IMEX Euler: implicit diffusion, explicit reaction; b = c = 1."""
       rng = np.random.default_rng(seed)
       u = rng.uniform(0.5, 1.5, N)
       v = rng.uniform(0.5, 1.5, N)
       Au = splu((identity(N) - dt * d * Lap).tocsc())
       Av = splu((identity(N) - dt * D * Lap).tocsc())
       for _ in range(int(T / dt)):
           r = m - u - v
           u, v = Au.solve(u + dt * u * r), Av.solve(v + dt * v * r)
       return u.sum() * h, v.sum() * h

   for d, D in [(0.01, 0.1), (0.1, 0.01), (0.1, 1.0), (1.0, 0.1), (0.05, 0.07)]:
       for seed in (0, 1):
           U, V = compete(d, D, seed=seed)
           print(f"d = {d}, D = {D}, seed {seed}: int u = {U:.4f}, int v = {V:.4f}")
   ```

   积分到 $t = 3000$ 的结果（两个随机种子结果相同）：

   | $(d, D)$ | $\int u$ | $\int v$ | 获胜者 |
   |---|---|---|---|
   | $(0.01, 0.1)$ | 2.0243 | 0 | $u$（扩散慢） |
   | $(0.1, 0.01)$ | 0 | 2.0243 | $v$（扩散慢） |
   | $(0.1, 1)$ | 2.0490 | 0 | $u$ |
   | $(1, 0.1)$ | 0 | 2.0490 | $v$ |
   | $(0.05, 0.07)$ | 2.0426 | 0 | $u$ |

   每一组都是扩散较慢的物种获胜，与初值无关；交换 $d$ 与 $D$，结局随之交换。获胜者的总量正好是它单独存在时的 $\int\theta$（与第 1 题的 $d = 0.01$、$d = 0.1$ 的数值相同），说明系统收敛到半平凡平衡态 $(u^*, 0)$ 或 $(0, v^*)$。排斥的速度取决于两个扩散系数的差距：败者的总量降到 $10^{-3}$ 以下所需的时间，$(0.1, 1)$ 约为 $160$，$(0.01, 0.1)$ 约为 $315$，$(0.05, 0.07)$ 约为 $650$；$d = D$ 时（定理的第三种情形）不发生排斥，任何初值都停在一族共存平衡解 $u + v = \theta$ 中的某一个上。

   直观上，扩散慢的物种分布更贴近 $m(x)$，在资源丰富处密度高；扩散快的物种把较多个体"浪费"在资源贫乏处。在对方的单种平衡下，扩散慢的物种处处面对 $m - \theta$ 的分布，它的入侵率为正，而扩散快的物种的入侵率为负（Dockery 等 1998 年的结果）。

3. **图灵斑图参数分析**：针对 Schnakenberg 模型，通过线性稳定性分析推导图灵不稳定的参数条件，并用数值模拟验证不同参数下斑图类型（点状、条纹状）的转变。

   **答** 线性稳定性分析。均匀稳态为 $u^* = a + b$，$v^* = b/(a + b)^2$，雅可比矩阵的元素为

   $$
   f_u = \frac{b - a}{a + b}, \quad f_v = (a + b)^2, \quad g_u = -\frac{2b}{a + b}, \quad g_v = -(a + b)^2, \qquad \det J = (a + b)^2 > 0 .
   $$
   扰动 $\propto \mathrm{e}^{\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{x} + \lambda t}$ 的增长率是 $J - k^2\operatorname{diag}(D_u, D_v)$ 的特征值；行列式 $h(k^2) = D_uD_vk^4 - (D_vf_u + D_ug_v)k^2 + \det J$ 对某个 $k$ 为负时失稳。于是图灵不稳定的条件是

   1. 无扩散时稳定：$f_u + g_v < 0$，即 $b - a < (a + b)^3$；
   2. $D_vf_u + D_ug_v > 0$，即 $D_v(b - a) > D_u(a + b)^3$，特别要求 $b > a$（$u$ 是自催化的激活子，$f_u > 0$，$v$ 是被消耗的底物，$g_v < 0$），并且 $D_v > D_u$；
   3. $h$ 的极小值为负：$(D_vf_u + D_ug_v)^2 > 4D_uD_v\det J$。

   记 $\delta = D_v/D_u$，条件 3 的等号给出临界扩散比 $\delta_{\mathrm{c}} = \bigl[(a + b)(1 + \sqrt{1 + f_u})/f_u\bigr]^2$，$\delta > \delta_{\mathrm{c}}$ 时失稳；阈值处的临界波数 $k_{\mathrm{c}}^2 = \sqrt{\det J/(D_uD_v)} = (a + b)/\sqrt{D_uD_v}$，斑图的波长约为 $2\pi/k_{\mathrm{c}}$。正文取 $a = 0.1$、$b = 0.9$，$f_u = 0.8$，$\delta_{\mathrm{c}} = 8.57$；正文的 $D_u = 0.1$、$D_v = 1$ 给出 $\delta = 10 > \delta_{\mathrm{c}}$，$k_{\mathrm{c}} = 1.78$，波长 $3.53$，边长 $20$ 的区域中约有 $5.7$ 个波长。作为对照，$a = 0.1$、$b = 2$、$\delta = 30$ 时 $\delta_{\mathrm{c}} = 30.5$，在阈值以下，数值模拟中扰动衰减，解保持均匀（$u$ 的变化范围小于 $10^{-5}$）。

   数值模拟。取 $D_u = 1$，在边长为 8 个临界波长的周期正方形上用半隐式谱方法（扩散项在 Fourier 空间隐式处理，反应项显式），$128 \times 128$ 网格，$\Delta t = 0.05$，从均匀态加 $10^{-2}$ 的随机扰动出发积分到 $t = 4000$。按 $u > \bar u$ 的连通区域个数与面积分数区分斑图：点状斑图是许多小块，面积约三分之一；条纹是少数贯通的带，面积约一半。

   ```python
   import numpy as np
   from scipy import ndimage

   def turing_info(a, b, Du, Dv):
       """Linear stability of the homogeneous state; returns (Turing unstable?, k_c, critical Dv/Du)."""
       fu, fv, gu, gv = (b - a) / (a + b), (a + b)**2, -2 * b / (a + b), -(a + b)**2
       det = fu * gv - fv * gu
       unstable = (fu + gv < 0) and (Dv * fu + Du * gv > 2 * np.sqrt(Du * Dv * det))
       kc = (det / (Du * Dv)) ** 0.25
       dc = ((a + b) * (1 + np.sqrt(1 + fu)) / fu) ** 2 if fu > 0 else np.inf
       return unstable, kc, dc

   def simulate(a, b, Du, Dv, n=128, waves=8, T=2000.0, dt=0.05, seed=0):
       """Semi-implicit spectral scheme on a periodic square holding about `waves` wavelengths."""
       _, kc, _ = turing_info(a, b, Du, Dv)
       L = waves * 2 * np.pi / kc
       k = 2 * np.pi * np.fft.fftfreq(n, L / n)
       K2 = k[:, None]**2 + k[None, :]**2
       rng = np.random.default_rng(seed)
       u = a + b + 0.01 * rng.standard_normal((n, n))
       v = b / (a + b)**2 + 0.01 * rng.standard_normal((n, n))
       Eu, Ev = 1 / (1 + dt * Du * K2), 1 / (1 + dt * Dv * K2)
       for _ in range(int(T / dt)):
           f = a - u + u * u * v
           g = b - u * u * v
           u = np.real(np.fft.ifft2(Eu * np.fft.fft2(u + dt * f)))
           v = np.real(np.fft.ifft2(Ev * np.fft.fft2(v + dt * g)))
       return u

   def classify(u):
       """Spots: many small blobs of high u; stripes: few long bands covering half of the domain."""
       mask = u > u.mean()
       _, n_regions = ndimage.label(mask, structure=np.ones((3, 3)))
       return n_regions, mask.mean()

   a, b, Du = 0.1, 0.9, 1.0
   for Dv in [9.0, 10.0, 12.0, 15.0, 30.0]:
       unstable, kc, dc = turing_info(a, b, Du, Dv)
       u = simulate(a, b, Du, Dv, T=4000.0)
       print(f"Dv/Du = {Dv}: Turing = {unstable}, k_c = {kc:.3f}, d_c = {dc:.3f}, "
             f"regions = {classify(u)[0]}, area fraction = {classify(u)[1]:.2f}")
   ```

   | $\delta = D_v/D_u$ | $\delta/\delta_{\mathrm{c}}$ | 连通区域数 | 面积分数 | 斑图 |
   |---|---|---|---|---|
   | 9 | 1.05 | 10 | 0.50 | 条纹 |
   | 10 | 1.17 | 14 | 0.49 | 条纹（局部有断裂） |
   | 12 | 1.40 | 81 | 0.39 | 六角排列的点 |
   | 15 | 1.75 | 85 | 0.38 | 六角排列的点 |
   | 30 | 3.50 | 100 | 0.33 | 点（更尖锐、更稀疏的高 $u$ 斑点） |

   另取 $b = 1.6$、$\delta = 30$（$\delta/\delta_{\mathrm{c}} = 1.44$）也得到点状斑图。所以在这组参数下，刚越过阈值时出现条纹，离阈值较远（$\delta/\delta_{\mathrm{c}}$ 在 $1.2$ 与 $1.4$ 之间）时转变为点状。线性分析只决定哪些波数失稳以及波长；点与条纹的选择由非线性项决定：弱非线性分析中，振幅方程的二次项有利于六角形（点），三次项有利于条纹，两者的相对大小随参数变化。斑图的具体排布（缺陷、条纹的走向）还与初始扰动有关。

4. **移流系数的影响**：在移流模型中固定 $d=D=1$，逐渐增大 $\alpha$，观察竞争结果从 $u$ 占优到共存的变化。

   **答** 仍取 $\Omega = [0, 1]$、$m(x) = 2 + \sin(2\pi x)$。移流项 $\nabla\cdot(d\nabla u - \alpha u\nabla m)$ 在 $\alpha$ 大时以对流为主，中心差分会产生振荡，所以用 Scharfetter–Gummel 通量（指数拟合的迎风格式），它对任意 Péclet 数稳定，并且在零通量边界下精确守恒。除了直接模拟，更干净的判据是两个半平凡平衡态的入侵率：$v$ 能否入侵 $(u^*, 0)$ 由算子 $D\Delta + (m - u^*)$ 的主特征值 $\lambda_v$ 的符号决定，$u$ 能否入侵 $(0, v^*)$ 由算子 $\varphi \mapsto \nabla\cdot(d\nabla\varphi - \alpha\varphi\nabla m) + (m - v^*)\varphi$ 的主特征值 $\lambda_u$ 决定。

   ```python
   import numpy as np
   from scipy.sparse import diags, identity
   from scipy.sparse.linalg import spsolve, splu
   from scipy.optimize import brentq

   N = 400
   h = 1.0 / N
   x = (np.arange(N) + 0.5) * h
   m = 2 + np.sin(2 * np.pi * x)

   def bern(z):
       """Bernoulli function z / (e^z - 1), safe near z = 0."""
       out = np.ones_like(z)
       nz = np.abs(z) > 1e-8
       out[nz] = z[nz] / np.expm1(z[nz])
       return out

   def transport(d, alpha):
       """div(d grad u - alpha u grad m) with Scharfetter-Gummel fluxes and zero flux at both ends."""
       P = alpha * np.diff(m) / d              # cell Peclet numbers at the interfaces
       bp, bm = bern(-P), bern(P)              # flux J_{i+1/2} = d/h * (bp*u_i - bm*u_{i+1})
       main = np.zeros(N)
       main[:-1] -= bp
       main[1:] -= bm
       return diags([bp, main, bm], [-1, 0, 1]) * d / h**2

   def single(d, alpha):
       """Single-species steady state by Newton's method."""
       A = transport(d, alpha)
       u = m.copy()
       for _ in range(200):
           F = A @ u + u * (m - u)
           step = spsolve((A + diags(m - 2 * u)).tocsc(), -F)
           u = np.maximum(u + step, 1e-12)
           if np.abs(step).max() < 1e-11:
               return u
       raise RuntimeError('Newton did not converge')

   def principal(A, q):
       """Principal eigenvalue (largest real part) of A + diag(q): the invasion rate of a rare species."""
       return np.linalg.eigvals((A + diags(q)).toarray()).real.max()

   def simulate(d, D, alpha, T=3000.0, dt=0.05):
       """IMEX time stepping of the competition model from u = v = 1."""
       Su = splu((identity(N) - dt * transport(d, alpha)).tocsc())
       Sv = splu((identity(N) - dt * transport(D, 0.0)).tocsc())
       u, v = np.ones(N), np.ones(N)
       for _ in range(int(T / dt)):
           r = m - u - v
           u, v = Su.solve(u + dt * u * r), Sv.solve(v + dt * v * r)
       return u.sum() * h, v.sum() * h

   d = D = 1.0
   vstar = single(D, 0.0)
   for alpha in [0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]:
       ustar = single(d, alpha)
       lam_v = principal(transport(D, 0.0), m - ustar)     # can v invade (u*, 0)?
       lam_u = principal(transport(d, alpha), m - vstar)   # can u invade (0, v*)?
       print(f"alpha = {alpha:5}: lambda_v = {lam_v:+.4f}, lambda_u = {lam_u:+.4f}")

   alpha_c = brentq(lambda al: principal(transport(D, 0.0), m - single(d, al)), 0.5, 1.0)
   print(f"alpha_c = {alpha_c:.3f}")
   for alpha in [0.25, 2.0, 8.0]:
       print(alpha, simulate(d, D, alpha))
   ```

   $d = D = 1$ 时的结果：

   | $\alpha$ | $\lambda_v$（$v$ 入侵 $u^*$） | $\lambda_u$（$u$ 入侵 $v^*$） | 结局 |
   |---|---|---|---|
   | 0 | 0 | 0 | 中性：两物种相同 |
   | 0.25 | $-0.053$ | $+0.107$ | $u$ 获胜 |
   | 0.5 | $-0.003$ | $+0.208$ | $u$ 获胜 |
   | 1 | $+0.262$ | $+0.380$ | 共存 |
   | 2 | $+0.752$ | $+0.591$ | 共存 |
   | 4 | $+1.136$ | $+0.735$ | 共存 |
   | 8 | $+1.329$ | $+0.801$ | 共存 |
   | 16 | $+1.545$ | $+0.832$ | 共存 |

   $\lambda_v$ 在 $\alpha_{\mathrm{c}} \approx 0.508$ 处由负变正（网格加密到 $N = 800$ 时不变），所以 $0 < \alpha < \alpha_{\mathrm{c}}$ 时 $(u^*, 0)$ 稳定、$(0, v^*)$ 不稳定，移流物种 $u$ 获胜；$\alpha > \alpha_{\mathrm{c}}$ 时两个半平凡平衡态都不稳定，两物种共存，与 5.7.2 的结论一致。直接模拟（从 $u = v = 1$ 积分到 $t = 3000$）给出：$\alpha = 0.25$ 时 $\int u = 2.059$、$\int v \to 0$；$\alpha = 2$ 时 $\int u = 0.583$、$\int v = 1.419$；$\alpha = 8$ 时 $\int u = 0.226$、$\int v = 1.786$。

   解释：$\alpha = 0$ 时两物种完全相同；小的 $\alpha$ 让 $u$ 稍微向资源丰富处聚集，它比单纯扩散更好地匹配 $m(x)$，于是占优（$u^*$ 的峰值随 $\alpha$ 从 $2.16$ 升到 $\alpha = 0.5$ 时的 $3.11$，峰的位置移到 $m$ 的极大点 $x = \frac14$）。$\alpha$ 继续增大，$u$ 过度集中在 $m$ 的极大点附近，其他地方的资源无法利用，$v$ 就能在那里入侵：共存时 $u$ 的总量随 $\alpha$ 减小，$v$ 占了大部分资源。这就是"过强的定向运动反而削弱竞争优势"的含义。

5. **无量纲化练习**：将带有 Allee 效应的反应-扩散方程 $\partial_t u = D\partial_{xx}u + ru(u-a)(1-u/K)$ 无量纲化，并讨论无量纲参数的生态学含义。

   **答** 先确定量纲：$u$ 是密度，$t$ 是时间，$x$ 是长度，$D$ 的量纲为长度$^2$/时间；$u(u - a)(1 - u/K)$ 的量纲是密度$^2$，所以这里的 $r$ 的量纲为 1/（时间 $\times$ 密度）。令

   $$
   \bar u = \frac{u}{K}, \qquad \bar t = rKt, \qquad \bar x = x\sqrt{\frac{rK}{D}}, \qquad \bar a = \frac{a}{K},
   $$
   代入 $\partial_t u = K\,rK\,\partial_{\bar t}\bar u$、$D\partial_{xx}u = K\,rK\,\partial_{\bar x\bar x}\bar u$、$ru(u - a)(1 - u/K) = rK^2\,\bar u(\bar u - \bar a)(1 - \bar u)$，两边除以 $rK^2$，得到

   $$
   \frac{\partial \bar u}{\partial \bar t} = \frac{\partial^2 \bar u}{\partial \bar x^2} + \bar u(\bar u - \bar a)(1 - \bar u), \qquad 0 < \bar a < 1 .
   $$
   四个参数 $D, r, a, K$ 只剩下一个 $\bar a$。各尺度的生态学含义：

   - $\bar a = a/K$：Allee 阈值占环境容纳量的比例，度量种群在低密度时"难以起步"的程度（如配偶难找、群体防御失效）；
   - $1/(rK)$：时间尺度，$rK$ 是密度接近 $K$ 时人均增长率的量级（密度 $u$ 时人均增长率 $r(u - a)(1 - u/K)$ 的尺度）；
   - $\sqrt{D/(rK)}$：长度尺度，即个体在一个增长时间内随机扩散的距离。

   无量纲化后立刻可以讨论入侵：这是双稳的方程（$\bar u = 0$ 与 $\bar u = 1$ 都稳定，$\bar u = \bar a$ 不稳定），连接 $1$ 与 $0$ 的行波有唯一的速度 $c = (1 - 2\bar a)/\sqrt2$。$\bar a < \frac12$ 时种群向外扩张，$\bar a > \frac12$ 时前沿后退（种群退缩），$\bar a = \frac12$ 时前沿静止；回到原变量，速度为 $c\sqrt{DrK}$。与 Fisher-KPP 方程（5.3）不同，这个速度不由前沿最前端的低密度部分决定，低密度个体负增长，所以入侵需要足够大的初始种群。数值验证（从阶跃初值出发，测量 $\bar u = \frac12$ 处的位置随时间的变化）：

   ```python
   import numpy as np
   from scipy.sparse import diags, identity
   from scipy.sparse.linalg import splu

   def front_speed(A, Lx=400.0, N=4000, T=150.0, dt=0.02):
       """Speed of the front of u_t = u_xx + u(u - A)(1 - u) started from a step."""
       h = Lx / N
       x = (np.arange(N) + 0.5) * h
       main = -2 * np.ones(N); main[0] = main[-1] = -1
       Lap = diags([np.ones(N - 1), main, np.ones(N - 1)], [-1, 0, 1]) / h**2
       S = splu((identity(N) - dt * Lap).tocsc())
       u = (x < Lx / 2).astype(float)
       pos = []
       for n in range(int(T / dt)):
           u = S.solve(u + dt * u * (u - A) * (1 - u))
           if (n + 1) % int(10 / dt) == 0:
               pos.append(x[np.argmin(np.abs(u - 0.5))])
       t = 10 * np.arange(1, len(pos) + 1)
       return np.polyfit(t[len(t) // 2:], pos[len(t) // 2:], 1)[0]

   for A in [0.1, 0.25, 0.4, 0.5, 0.6]:
       print(f"a/K = {A}: simulated c = {front_speed(A):+.4f}, theory (1 - 2a/K)/sqrt(2) = {(1 - 2 * A) / np.sqrt(2):+.4f}")
   ```

   | $\bar a$ | 0.1 | 0.25 | 0.4 | 0.5 | 0.6 |
   |---|---|---|---|---|---|
   | 模拟的 $c$ | 0.5648 | 0.3527 | 0.1418 | 0.0000 | $-0.1418$ |
   | $(1 - 2\bar a)/\sqrt2$ | 0.5657 | 0.3536 | 0.1414 | 0 | $-0.1414$ |
