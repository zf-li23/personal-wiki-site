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
c_{\text{min}}=2\sqrt{rD}.
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

设 $b,c\in(0,1)$，$u^*$ 是单物种平衡解。定义 $c^* = \inf_{d>0}\dfrac{\int_\Omega m}{\int_\Omega u^*}$。若 $c>c^*$，则存在一个非空区域 $\Sigma\subset\mathbb{R}^+\times\mathbb{R}^+$，使得对 $(d,D)\in\Sigma$，半平凡平衡态 $(u^*,0)$ 是稳定的（即物种 $v$ 灭绝）。

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

Schnakenberg 模型（Brusselator 的简化版）是产生图灵斑图的经典例子：
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

## 思考题

1. **单种群引理数值验证**：取一维区域 $\Omega=[0,1]$，设资源函数 $m(x)=2+\sin(2\pi x)$，用有限差分法求解平衡态方程，计算总生物量 $\int_0^1\theta(x)\,\mathrm{d}x$ 随扩散系数 $d$ 的变化曲线。

2. **竞争模型的模拟**：在对称竞争 $b=c=1$ 下，取不同的 $(d,D)$，从随机初始条件出发，试验证扩散较慢的物种获胜的结论。

3. **图灵斑图参数分析**：针对 Schnakenberg 模型，通过线性稳定性分析推导图灵不稳定的参数条件，并用数值模拟验证不同参数下斑图类型（点状、条纹状）的转变。

4. **移流系数的影响**：在移流模型中固定 $d=D=1$，逐渐增大 $\alpha$，观察竞争结果从 $u$ 占优到共存的变化。

5. **无量纲化练习**：将带有 Allee 效应的反应-扩散方程 $\partial_t u = D\partial_{xx}u + ru(u-a)(1-u/K)$ 无量纲化，并讨论无量纲参数的生态学含义。
