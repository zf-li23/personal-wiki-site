---
title: Schrödinger 方程
description: Schrödinger 方程及其线性性，量子力学的基本假设与哈密顿量，定态与能量本征方程；无限深方势阱的能级、零点能与驻波；阶跃势与有限宽势垒，隧道效应、穿透系数、α 衰变与扫描隧道显微镜；一维量子谐振子的等间距能级、Hermite 多项式与概率分布。
---

前两章（[5.5.1](/5.5.1)、[5.5.2](/5.5.2)）说明了光和实物粒子都具有**波粒二象性**，粒子的状态用**波函数**描述，$\lvert\Psi\rvert^2$ 是发现粒子的概率密度。但那里还缺一条动力学规律：给定粒子所处的力场，波函数怎样随时间变化？本章的 Schrödinger 方程回答了这个问题，它在量子力学中的地位相当于 **Newton 第二定律**在经典力学中的地位。势能不随时间变化时，用**分离变量法**（[2.5.4](/2.5.4)）把它化为一个**特征值**问题，能量量子化就表现为这个方程只在一些分立的能量下有合乎物理要求的解，这与弦振动只有一系列固有频率（[2.5.4](/2.5.4#sec-4.1.3)）在数学上是同一回事。随后用三个一维模型说明量子力学的基本特点：无限深方势阱（能量量子化与零点能）、势垒（隧道效应）和谐振子（等间距能级）。下一章（[5.5.4](/5.5.4)）用同样的方法处理三维的氢原子；谐振子是分子振动光谱（[5.5.5](/5.5.5)）和固体中晶格振动的基础，势阱模型在 [5.5.6](/5.5.6) 中推广为金属中的自由电子气。

## 3.1. Schrödinger 方程

### 3.1.1. 方程的建立

1926 年初，Schrödinger 在苏黎世的一次讨论会上介绍了 de Broglie 的**物质波**假说，Debye 评论说：有波就应该有**波动方程**。几周之后，Schrödinger 给出了这个方程。它不能从更基本的原理推导出来，下面的推理只是一种启发：沿 $x$ 方向运动、动量为 $p$、能量为 $E$ 的自由粒子对应平面波

$$
\Psi(x,t)=A\,\mathrm{e}^{\mathrm{i}(px-Et)/\hbar}.
$$
它满足 $\mathrm{i}\hbar\,\partial_t\Psi=E\Psi$ 和 $-\mathrm{i}\hbar\,\partial_x\Psi=p\Psi$，即 $-\hbar^2\partial_x^2\Psi=p^2\Psi$。非相对论的自由粒子有 $E=p^2/(2m)$，所以

$$
\mathrm{i}\hbar\frac{\partial\Psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2}.
$$
在势场 $U$ 中，能量是 $E=p^2/(2m)+U$，把右边加上 $U\Psi$ 就得到一般的方程。由此可以看出一条对应规则：经典的能量、动量对应于作用在波函数上的微分运算 $E\to\mathrm{i}\hbar\,\partial_t$、$\boldsymbol{p}\to-\mathrm{i}\hbar\nabla$。

**定理 3.1.1（Schrödinger 方程）** 质量为 $m$ 的粒子在势场 $U(\boldsymbol{r},t)$ 中运动时，它的波函数满足

$$
\mathrm{i}\hbar\frac{\partial\Psi(\boldsymbol{r},t)}{\partial t}=\Big[-\frac{\hbar^2}{2m}\nabla^2+U(\boldsymbol{r},t)\Big]\Psi(\boldsymbol{r},t),
\tag{3.1}
$$
其中 $\nabla^2=\Delta=\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}$ 是 **Laplace 算子**。一维情形为 $\mathrm{i}\hbar\,\partial_t\Psi(x,t)=-\frac{\hbar^2}{2m}\partial_x^2\Psi+U(x,t)\Psi$。

**注 3.1.1** 方程 (3.1) 是量子力学的基本假设，它的正确性只能由实验检验，正如 Newton 定律不能由更基本的经典原理导出。它有以下几个特点：

- 它是线性齐次方程：若 $\Psi_1,\Psi_2$ 是解，则 $c_1\Psi_1+c_2\Psi_2$（$c_1,c_2$ 为任意复数）也是解。这正是**态叠加原理**所要求的（[5.5.2](/5.5.2)）。
- 方程中含有虚数单位 $\mathrm{i}$，解一般是复函数。$\Psi$ 本身不可观测，可观测的是概率密度 $\lvert\Psi\rvert^2=\Psi^*\Psi$。
- 它对时间是一阶的，而经典的**波动方程**（[2.5.3](/2.5.3)）对时间是二阶的。因此只要给定初始时刻的 $\Psi(\boldsymbol{r},0)$，以后的波函数就完全确定：量子力学中被决定的是**概率幅**的演化，而不是单次测量的结果。
- 它是非相对论的方程（用了 $E=p^2/(2m)$），不包含粒子的产生与湮灭；高速粒子要用相对论量子力学（Dirac 方程）处理，电子的自旋（[5.5.4](/5.5.4)）在那里自然出现。

### 3.1.2. 量子力学的基本假设与哈密顿量

**性质 3.1.1（量子力学的基本假设）** 非相对论量子力学建立在以下假设之上：

1. 微观体系的状态由一个归一化的波函数 $\Psi(\boldsymbol{r},t)$ 完全描述，$\lvert\Psi\rvert^2$ 是在 $\boldsymbol{r}$ 处发现粒子的概率密度；
2. 波函数随时间的变化服从 Schrödinger 方程 (3.1)；
3. 每个力学量（可观测量）由一个线性 Hermite 算符表示，例如位置 $\hat x=x$、动量 $\hat{\boldsymbol{p}}=-\mathrm{i}\hbar\nabla$；
4. 测量力学量 $A$ 的可能结果只能是其算符 $\hat A$ 的**本征值**，得到各本征值的概率由波函数按**本征函数**展开的系数决定（[5.5.4](/5.5.4#sec-4.5.1)）。

Hermite 算符就是内积空间中的 **Hermite 变换**（[2.1.13](/2.1.13)）：对平方可积函数的内积 $\langle f,g\rangle=\int f^*g\,\mathrm{d}V$，它满足 $\langle f,\hat Ag\rangle=\langle\hat Af,g\rangle$。由线性代数的结论，它的**本征值**都是实数，属于不同本征值的**本征函数**相互正交，这正是测量结果必须是实数的数学保证。

**定义 3.1.1（哈密顿量）** 算符

$$
\hat H=\frac{\hat{\boldsymbol{p}}^2}{2m}+U(\boldsymbol{r},t)=-\frac{\hbar^2}{2m}\nabla^2+U(\boldsymbol{r},t)
$$
称为粒子的**哈密顿量**（哈密顿算符）；$U$ 不显含时间时，它就是能量算符。用哈密顿量，Schrödinger 方程写成

$$
\mathrm{i}\hbar\frac{\partial\Psi}{\partial t}=\hat H\Psi.
\tag{3.2}
$$

哈密顿量是经典力学中 Hamilton 函数（用动量和坐标表示的能量）的算符化，不要与矢量分析中的 **Hamilton 算子** $\nabla$（[2.2](/2.2)）混淆。在经典力学中，改变质点运动状态的原因是力；在量子力学中，决定波函数演化的是哈密顿量。外界对粒子的一切作用，包括不能用"力"表达的微观相互作用，都概括在势函数 $U$ 中。以下只讨论 $U$ 不随时间变化的情形。

### 3.1.3. 定态与能量本征方程

设 $U=U(\boldsymbol{r})$ 不显含 $t$。用**分离变量法**，令 $\Psi(\boldsymbol{r},t)=\psi(\boldsymbol{r})T(t)$，代入 (3.2) 并除以 $\psi T$：

$$
\mathrm{i}\hbar\frac{1}{T}\frac{\mathrm{d}T}{\mathrm{d}t}=\frac{1}{\psi}\hat H\psi.
$$
左边只与 $t$ 有关，右边只与 $\boldsymbol{r}$ 有关，所以两边等于同一常数，记作 $E$（它有能量的量纲）。于是得到两个方程：$\mathrm{i}\hbar\,\mathrm{d}T/\mathrm{d}t=ET$，解为 $T=C\mathrm{e}^{-\mathrm{i}Et/\hbar}$（振动因子）；以及

**定义 3.1.2（定态 Schrödinger 方程）** 方程

$$
\hat H\psi=-\frac{\hbar^2}{2m}\nabla^2\psi+U(\boldsymbol{r})\psi=E\psi
\tag{3.3}
$$
称为**定态 Schrödinger 方程**，也称**能量本征方程**。使它有满足物理条件的解的常数 $E$ 称为能量本征值，相应的解 $\psi_E$ 称为能量本征函数。一维情形常写成

$$
\psi''(x)+\frac{2m}{\hbar^2}\big[E-U(x)\big]\psi(x)=0.
\tag{3.4}
$$

在数学上，对任何 $E$ 方程 (3.3) 都有解；但在物理上，波函数必须满足标准条件：单值、有限（平方可积）、连续，在 $U$ 有限的地方导数也连续。只有某些特定的 $E$ 能使解满足这些条件，这与 **Sturm–Liouville 问题**（[2.4.12](/2.4.12#sec-12.5)）中的边界条件选出一列特征值完全相同。

**定义 3.1.3（定态）** 能量取确定值 $E$ 的状态

$$
\Psi_E(\boldsymbol{r},t)=\psi_E(\boldsymbol{r})\,\mathrm{e}^{-\mathrm{i}Et/\hbar}
$$
称为**定态**。定态的概率密度 $\lvert\Psi_E\rvert^2=\lvert\psi_E\rvert^2$ 不随时间变化，这正是"定态"一词的含义。

能量本征值可能是分立的（如束缚在势阱中的粒子），也可能是连续的（如自由粒子）。设本征值是分立的 $E_1,E_2,\dots$，相应的本征函数为 $\psi_1,\psi_2,\dots$。由线性，Schrödinger 方程的一般解是各定态的叠加

$$
\Psi(\boldsymbol{r},t)=\sum_n C_n\,\psi_n(\boldsymbol{r})\,\mathrm{e}^{-\mathrm{i}E_nt/\hbar},
\tag{3.5}
$$
复常数 $C_n$ 由初始波函数按本征函数的展开 $\Psi(\boldsymbol{r},0)=\sum_n C_n\psi_n$ 确定（**特征函数展开**，[2.5.4](/2.5.4#sec-4.4.1)）。叠加态的能量不确定，概率密度一般随时间变化。所以求解能量本征方程是量子力学中最基本的计算。下面用一维方程 (3.4) 讨论两类问题：

- 本征值问题：给定 $U(x)$，求束缚粒子的能量本征值 $E_n$ 和本征函数 $\psi_n$（§3.2、§3.4）；
- 散射问题：给定入射粒子的能量 $E$，求它穿过势垒的概率（§3.3）。

## 3.2. 无限深方势阱中的粒子

### 3.2.1. 模型与求解

金属中的自由电子可以在金属内部自由运动，却很难逸出表面：表面附近有一个高度约为几个电子伏特的势能台阶。把台阶理想化为无限高，就得到最简单的束缚模型。

**定义 3.2.1（无限深方势阱）** 势能

$$
U(x)=\begin{cases}0, & \lvert x\rvert<a/2,\\ \infty, & \lvert x\rvert\ge a/2\end{cases}
$$
称为宽度为 $a$ 的**无限深方势阱**。

阱外 $U=\infty$，粒子不可能出现，$\psi=0$。阱内 $U=0$，方程 (3.4) 成为 $\psi''+k^2\psi=0$，$k=\sqrt{2mE}/\hbar$（$E\le0$ 时只有零解，见下文），通解为 $\psi=A\sin(kx+\delta)$。波函数在阱壁连续，所以 $\psi(\pm a/2)=0$：

$$
\sin\Big(\frac{ka}{2}+\delta\Big)=0,\qquad \sin\Big(-\frac{ka}{2}+\delta\Big)=0.
$$
两式给出 $ka/2+\delta=l_1\pi$，$-ka/2+\delta=l_2\pi$，相加得 $\delta=l\pi/2$（$l$ 为整数）。不计不影响 $\lvert\psi\rvert^2$ 的正负号，只有两种情形：$\delta=0$ 时 $\psi=A\sin kx$ 是奇函数，由 $\sin(ka/2)=0$ 得 $ka=n\pi$，$n=2,4,6,\dots$；$\delta=\pi/2$ 时 $\psi=A\cos kx$ 是偶函数，由 $\cos(ka/2)=0$ 得 $ka=n\pi$，$n=1,3,5,\dots$。$n=0$ 给出 $\psi\equiv0$，不是物理状态。合并起来，$ka=n\pi$，$n=1,2,3,\dots$。

### 3.2.2. 能量本征值与零点能

由 $k^2=2mE/\hbar^2$ 和 $k=n\pi/a$ 得

$$
E_n=\frac{\pi^2\hbar^2}{2ma^2}\,n^2,\qquad n=1,2,3,\dots
\tag{3.6}
$$

束缚在势阱中的粒子，能量只能取一系列分立值，这就是能量量子化；每个能量值对应一个能级，$n$ 称为量子数。处于势阱、谐振子或原子中而不能跑到无穷远处的状态称为束缚态（bound state），束缚态的能量总是分立的。

最低能量 $E_1=\pi^2\hbar^2/(2ma^2)>0$ 称为零点能（zero-point energy）：粒子不可能静止在阱底。这是量子力学特有的结果，可以由**不确定关系**理解：粒子被限制在宽度 $a$ 内，$\Delta x\sim a$，于是动量不可能确定为零，$\Delta p_x\gtrsim\hbar/a$，动能至少是 $\hbar^2/(ma^2)$ 的量级，与 $E_1$ 一致。也正因为如此，$E=0$ 的解不存在。

相邻能级的间隔为

$$
\Delta E_n=E_{n+1}-E_n=\frac{\pi^2\hbar^2}{2ma^2}(2n+1),\qquad \frac{\Delta E_n}{E_n}=\frac{2n+1}{n^2}\approx\frac{2}{n}\quad(n\gg1).
$$
能级越高，间隔越大，但相对间隔越小。势阱越宽、粒子越重，能级越密。

**例 3.2.1（微观与宏观的势阱）** (1) 电子在 $a=1\,\mathrm{nm}$ 的势阱中，$E_1=\frac{h^2}{8m_{\mathrm{e}}a^2}\approx6.0\times10^{-20}\,\mathrm{J}\approx0.38\,\mathrm{eV}$，与原子中的能量同一量级，量子化十分显著。(2) 质量 $1\,\mathrm{g}$ 的小球在 $a=1\,\mathrm{cm}$ 的盒子中，$E_1\approx5.5\times10^{-61}\,\mathrm{J}$；它若以 $1\,\mathrm{mm/s}$ 运动，动能 $5\times10^{-10}\,\mathrm{J}$ 对应 $n\approx3\times10^{25}$，相对能级间隔 $2/n\sim10^{-25}$，能量完全可以看成连续的。

### 3.2.3. 驻波与本征函数

由 de Broglie 关系，第 $n$ 个能级的粒子的动量大小为 $p_n=\sqrt{2mE_n}=n\pi\hbar/a$，波长 $\lambda_n=h/p_n=2a/n$，即阱宽恰好是半波长的整数倍。这与两端固定的弦上的**驻波**完全相同（[5.1.7](/5.1.7)）：阱壁是**波节**，每个能量本征态对应一个特定波长的驻波。反过来也可以说，势阱中的能量量子化是 **de Broglie 波**形成稳定驻波的必然结果。

由**归一化条件** $\int_{-a/2}^{a/2}\lvert\psi_n\rvert^2\,\mathrm{d}x=A^2\cdot\frac a2=1$ 得 $A=\sqrt{2/a}$，所以

$$
\psi_n(x)=\begin{cases}\sqrt{\dfrac2a}\cos\dfrac{n\pi x}{a}, & n=1,3,5,\dots,\\[2ex] \sqrt{\dfrac2a}\sin\dfrac{n\pi x}{a}, & n=2,4,6,\dots,\end{cases}\qquad \lvert x\rvert<\frac a2,
\tag{3.7}
$$
阱外 $\psi_n=0$。相应的定态是 $\Psi_n=\psi_n\mathrm{e}^{-\mathrm{i}E_nt/\hbar}$，概率密度 $\lvert\psi_n\rvert^2$ 不随时间变化。本征函数有以下性质：

- 奇偶性：势能关于 $x=0$ 对称，本征函数或为偶函数（$n$ 奇），或为奇函数（$n$ 偶），基态是偶函数。
- 节点数：$\psi_n$ 在阱内有 $n-1$ 个零点，能量越高，零点越多（Sturm 振动定理，[2.4.12](/2.4.12#sec-12.5.2)）。
- 正交归一：$\int\psi_m\psi_n\,\mathrm{d}x=\delta_{mn}$，并且 $\{\psi_n\}$ 是完备的：这就是 $[-a/2,a/2]$ 上的 Fourier 正弦–余弦级数。

![无限深方势阱。左：前四个本征函数 ψ_n，分别画在能级 E_n = n²E_1 的高度上，第 n 个有 n - 1 个节点，阱壁是波节；右：n = 1、2、20 的概率密度与经典粒子的均匀分布（虚线）](./plots/infinite-well.py)

量子的概率分布与经典的截然不同：经典粒子在阱内以恒定速率来回运动，在各处停留的时间相同，概率密度是均匀的 $1/a$；而基态粒子最可能出现在阱中央，$n=2$ 的粒子在中央出现的概率为零。$n$ 很大时，$\lvert\psi_n\rvert^2$ 的振荡越来越密，在任何有限宽度的区间上的平均值趋于 $1/a$，与经典结果一致。

**定义 3.2.2** 在大量子数极限下，量子体系的行为趋于经典物理的结果，这称为**对应原理**（Bohr 对应原理）。

对应原理是 Bohr 在建立旧量子论时提出的指导原则（[5.5.4](/5.5.4)），它要求新理论在经典物理已被检验的范围内重现经典的结果，正如狭义相对论在 $v\ll c$ 时回到 Newton 力学。

## 3.3. 势垒穿透

### 3.3.1. 阶跃势垒

金属与半导体的接触处、原子核的表面附近，势能都会隆起形成势垒（potential barrier）。最简单的势垒是阶跃势：

$$
U(x)=\begin{cases}0, & x<0\ \text{(I)},\\ U_0, & x>0\ \text{(II)}.\end{cases}
$$
设能量为 $E<U_0$ 的粒子从左方入射。经典粒子到达 $x=0$ 后只能被完**全反射**，因为在区域 II 中动能 $E-U_0<0$。量子粒子是波，情况不同。令

$$
k=\frac{\sqrt{2mE}}{\hbar},\qquad \kappa=\frac{\sqrt{2m(U_0-E)}}{\hbar},
$$
方程 (3.4) 在两个区域中分别成为 $\psi''+k^2\psi=0$ 与 $\psi''-\kappa^2\psi=0$，通解为

$$
\psi_{\mathrm{I}}=A\mathrm{e}^{\mathrm{i}kx}+B\mathrm{e}^{-\mathrm{i}kx},\qquad \psi_{\mathrm{II}}=C\mathrm{e}^{-\kappa x}+D\mathrm{e}^{\kappa x}.
$$
$\psi_{\mathrm{I}}$ 是入射波与反射波的叠加（波动型解）；$x\to+\infty$ 时 $\psi$ 必须有限，所以 $D=0$，$\psi_{\mathrm{II}}=C\mathrm{e}^{-\kappa x}$ 是指数衰减型解。由 $\psi$ 与 $\psi'$ 在 $x=0$ 处连续，$A+B=C$，$\mathrm{i}k(A-B)=-\kappa C$，解得

$$
\frac BA=\frac{k-\mathrm{i}\kappa}{k+\mathrm{i}\kappa},\qquad \frac CA=\frac{2k}{k+\mathrm{i}\kappa}.
$$
$\lvert B/A\rvert=1$：粒子最终全部被反射，这一点与经典相同；但 $C\ne0$，粒子在势垒内出现的概率密度

$$
\lvert\psi_{\mathrm{II}}(x)\rvert^2=\lvert C\rvert^2\mathrm{e}^{-2\kappa x}
$$
不为零，在透入深度 $1/(2\kappa)$ 的范围内按指数衰减。势垒越高（$U_0-E$ 越大），衰减越快。对 $U_0-E=5\,\mathrm{eV}$ 的电子，$\kappa\approx1.15\times10^{10}\,\mathrm{m^{-1}}$，透入深度不到 $0.05\,\mathrm{nm}$。金属中的电子正是这样稍稍"渗出"表面，在表面外形成一层很薄的电子气。

### 3.3.2. 有限宽势垒与隧道效应

若势垒只有有限宽度 $a$：$0<x<a$ 时 $U=U_0$，其余各处 $U=0$，则衰减的波到达势垒右边界时振幅仍不为零，可以在区域 III 中以平面波 $F\mathrm{e}^{\mathrm{i}kx}$ 继续前进。能量低于势垒高度的粒子有一定概率穿过势垒，这称为隧道效应（tunnel effect），也称势垒穿透。

**定义 3.3.1（穿透系数）** 透射波与入射波的概率流之比 $T=\lvert F/A\rvert^2$（两侧势能相同，速度相同）称为势垒的**穿透系数**，即入射粒子穿过势垒的概率。

在 $x=0$ 和 $x=a$ 处分别要求 $\psi,\psi'$ 连续，得到关于 $B,C,D,F$ 的线性方程组，解为

$$
T=\Big[1+\frac{U_0^2\sinh^2(\kappa a)}{4E(U_0-E)}\Big]^{-1}.
\tag{3.8}
$$
当 $\kappa a\gg1$ 时 $\sinh\kappa a\approx\frac12\mathrm{e}^{\kappa a}$，于是

$$
T\approx\frac{16E(U_0-E)}{U_0^2}\,\mathrm{e}^{-2\kappa a}\sim\mathrm{e}^{-2\kappa a}=\exp\Big[-\frac{2a}{\hbar}\sqrt{2m(U_0-E)}\Big].
\tag{3.9}
$$
前面的系数是 1 的量级，穿透系数主要由指数决定：对势垒宽度 $a$、粒子质量 $m$ 和"欠缺的能量" $U_0-E$ 都非常敏感。对形状不规则的势垒，可以把它分成许多窄条，近似地有 $T\approx\exp\big[-\frac2\hbar\int\sqrt{2m(U(x)-E)}\,\mathrm{d}x\big]$，积分遍及 $U>E$ 的区域（WKB 近似）。

![矩形势垒。左：E = U_0/2、κa = 1.8 时散射态的概率密度：入射波与反射波干涉形成振荡，势垒内按指数衰减，透射区为常数；右：电子的穿透系数随势垒宽度的变化（对数坐标），实线为精确式 (3.8)，虚线为 e^{-2κa}](./plots/tunneling.py)

**例 3.3.1（电子的穿透系数）** 设 $U_0-E=5\,\mathrm{eV}$，$\kappa\approx1.15\times10^{10}\,\mathrm{m^{-1}}$。$a=0.1\,\mathrm{nm}$ 时 $\mathrm{e}^{-2\kappa a}\approx0.10$；$a=0.5\,\mathrm{nm}$ 时约 $10^{-5}$；$a=1\,\mathrm{nm}$ 时约 $10^{-10}$。可见势垒只要有几个纳米宽，电子的隧穿就几乎可以忽略；对宏观物体（$m$ 大、$a$ 大），$T$ 实际上严格为零，量子的结论过渡到经典的结论。

**注 3.3.1** 粒子穿过势垒与能量守恒并不矛盾。"粒子在势垒内动能为负"这种说法假定了粒子同时具有确定的位置和动量，而这正是**不确定关系**所否定的：在势垒内找到粒子，意味着位置不确定度 $\Delta x\lesssim a$，动量与能量就相应地不确定。用 $\Delta E\approx p\Delta p/m$ 所作的估算只是定性的图像，可靠的结论是式 (3.8)。

### 3.3.3. 隧道效应的应用

隧道效应最早的应用是解释原子核的 α 衰变。核内的 α 粒子受短程的核力束缚，核外受长程的 Coulomb 斥力（**Coulomb 定律**），两者合成的势垒在核表面附近高达约 $30\,\mathrm{MeV}$。例如 $\ce{^{238}U -> ^{234}Th + ^{4}He}$ 放出的 α 粒子能量只有 $4.27\,\mathrm{MeV}$，经典上无法逸出。1928 年 Gamow 与 Condon、Gurney 分别用隧道效应解释了 α 衰变：α 粒子在核内来回碰撞势垒约 $10^{21}$ 次每秒，每次以极小的概率 $T$ 穿出。由于 $T$ 对 $E$ 呈指数依赖，α 粒子能量相差不到一倍，半衰期却可以从不到微秒跨到 $10^{10}$ 年以上（$\ce{^{238}U}$ 为 $4.5\times10^9$ 年），这正是实验总结出的 Geiger–Nuttall 定律，理论与实验相符。

隧道二极管（江崎玲於奈，1957）、金属的场致发射、闪存中电荷穿过薄氧化层的写入与擦除，都利用了电子的隧穿。

扫描隧道显微镜（Scanning Tunneling Microscope），简称 STM，由 Binnig 与 Rohrer 于 1981 年发明，两人因此与发明电子显微镜的 Ruska 分享了 1986 年的诺贝尔物理学奖。导电探针的针尖与样品表面相距 $d\sim1\,\mathrm{nm}$，两者之间的真空是势垒；加上偏压 $U$ 后，电子隧穿形成隧道电流

$$
i\propto U\,\mathrm{e}^{-A\sqrt{\phi}\,d},\qquad A=\frac{2\sqrt{2m_{\mathrm{e}}}}{\hbar}\approx10.25\,\mathrm{nm^{-1}\,eV^{-1/2}},
$$
其中 $\phi$ 是表面的平均势垒高度（**功函数**量级，约 $4\,\mathrm{eV}$）。此时 $d$ 改变 $0.1\,\mathrm{nm}$，电流就改变约一个数量级。用压电陶瓷驱动针尖在表面上扫描，并用反馈电路保持电流恒定，针尖的起伏就描绘出表面的原子级形貌（横向分辨率约 $0.1\,\mathrm{nm}$）。STM 实际测量的是表面附近电子的 $\lvert\psi\rvert^2$ 分布，它还可以用针尖逐个搬运吸附在表面上的原子（如 $\ce{Ni}$ 表面上的 $\ce{Xe}$ 原子），在表面物理、材料科学、化学与生物学中应用很广。

## 3.4. 一维谐振子

### 3.4.1. 定态 Schrödinger 方程

任何势能在稳定平衡位置附近都可以近似为抛物线（**势能曲线**的极小值附近展开到二阶），所以谐振子是物理学中最重要的模型之一：分子中原子的振动、晶体中的晶格振动、电磁场的每个模式，都是谐振子。经典谐振子的能量可以连续取值，但用这种模型无法解释**黑体**辐射（[5.5.1](/5.5.1)）和低温下固体的比热，谐振子的能量必须量子化。

取平衡位置为原点和势能零点，质量为 $m$、劲度系数为 $k$ 的谐振子势能为 $U=\frac12kx^2=\frac12m\omega^2x^2$，$\omega=\sqrt{k/m}$ 是经典**简谐振动**的角频率（[5.1.6](/5.1.6)）。这样的量子体系称为量子谐振子（quantum harmonic oscillator）。定态 Schrödinger 方程为

$$
-\frac{\hbar^2}{2m}\psi''+\frac12m\omega^2x^2\psi=E\psi.
$$
引入无量纲的坐标与能量

$$
\xi=\alpha x,\quad \alpha=\sqrt{\frac{m\omega}{\hbar}},\qquad \lambda=\frac{2E}{\hbar\omega},
$$
方程化为 $\psi''(\xi)+(\lambda-\xi^2)\psi=0$。$\lvert\xi\rvert$ 很大时 $\psi\approx\mathrm{e}^{\pm\xi^2/2}$，有限性要求取 $\mathrm{e}^{-\xi^2/2}$。令 $\psi=H(\xi)\mathrm{e}^{-\xi^2/2}$，得到 Hermite 方程

$$
H''-2\xi H'+(\lambda-1)H=0.
$$
用**幂级数**解法（[2.4.10](/2.4.10)），$H=\sum c_j\xi^j$ 的系数满足 $c_{j+2}=\frac{2j+1-\lambda}{(j+1)(j+2)}c_j$。若级数不终止，$H$ 在 $\lvert\xi\rvert\to\infty$ 时像 $\mathrm{e}^{\xi^2}$ 一样增长，$\psi$ 不能归一化；所以级数必须在某一项终止，即 $\lambda=2n+1$，$n=0,1,2,\dots$。终止的级数是 $n$ 次多项式，取适当的常数因子，就是 Hermite 多项式（Hermite polynomials）

$$
H_0=1,\quad H_1=2\xi,\quad H_2=4\xi^2-2,\quad H_3=8\xi^3-12\xi,\quad\dots,\qquad H_n(\xi)=(-1)^n\mathrm{e}^{\xi^2}\frac{\mathrm{d}^n}{\mathrm{d}\xi^n}\mathrm{e}^{-\xi^2}.
$$

### 3.4.2. 能量量子化

由 $\lambda=2E/(\hbar\omega)=2n+1$ 得

$$
E_n=\Big(n+\frac12\Big)\hbar\omega=\Big(n+\frac12\Big)h\nu,\qquad n=0,1,2,\dots
\tag{3.10}
$$

- 能级等间距，间隔为 $\hbar\omega$，只由经典振动频率决定。这正是 Planck 为解释黑体辐射所假设的"**能量子**" $h\nu$（[5.5.1](/5.5.1)），量子力学还给出了 Planck 没有的零点能。
- 零点能 $E_0=\frac12\hbar\omega$ 符合**不确定关系**。在基态 $\langle x\rangle=\langle p\rangle=0$，所以 $E=\frac{(\Delta p)^2}{2m}+\frac12m\omega^2(\Delta x)^2$；由 $\Delta x\,\Delta p\ge\hbar/2$ 与均值不等式，$E\ge2\sqrt{\frac{(\Delta p)^2}{2m}\cdot\frac{m\omega^2(\Delta x)^2}{2}}=\omega\,\Delta x\,\Delta p\ge\frac12\hbar\omega$，基态恰好取等号。
- 分子振动：双原子分子的振动量子 $\hbar\omega$ 通常在 $0.1$–$0.5\,\mathrm{eV}$（如 $\ce{H2}$ 约 $0.52\,\mathrm{eV}$，$\ce{CO}$ 约 $0.27\,\mathrm{eV}$），远大于室温下的 $k_{\mathrm{B}}T\approx0.026\,\mathrm{eV}$。分子几乎都处于振动基态，振动**自由度**对热容没有贡献，可以把分子看作刚性的。这就是经典的**能量均分定理**在常温下给出错误的双原子气体热容的原因（[5.2.1](/5.2.1)）。
- 宏观极限：质量 $0.1\,\mathrm{kg}$、劲度系数 $10\,\mathrm{N/m}$ 的弹簧振子（$\omega=10\,\mathrm{s^{-1}}$）以 $1\,\mathrm{cm}$ 的振幅振动，能量 $5\times10^{-4}\,\mathrm{J}$ 对应 $n\approx5\times10^{29}$，能量量子化完全观察不到，符合对应原理。

### 3.4.3. 波函数与概率密度

归一化的本征函数为

$$
\psi_n(x)=\Big(\frac{\alpha}{2^nn!\sqrt\pi}\Big)^{1/2}H_n(\alpha x)\,\mathrm{e}^{-\alpha^2x^2/2},
\tag{3.11}
$$
例如 $\psi_0=\big(\frac{\alpha}{\sqrt\pi}\big)^{1/2}\mathrm{e}^{-\alpha^2x^2/2}$，$\psi_1=\big(\frac{\alpha}{2\sqrt\pi}\big)^{1/2}2\alpha x\,\mathrm{e}^{-\alpha^2x^2/2}$。与方势阱一样，$\psi_n$ 的奇偶性与 $n$ 相同，有 $n$ 个节点，并且构成正交归一的完备函数系。

![一维谐振子。左：前五个本征函数画在能级 E_n = (n + 1/2)ħω 的高度上，灰线是势能 U = mω²x²/2，点线标出经典的运动范围；右：n = 11 的概率密度与经典谐振子的概率密度（虚线），竖线为经典转折点](./plots/harmonic-oscillator.py)

量子数小时，概率分布与经典谐振子完全不同。基态的概率密度

$$
\lvert\psi_0(x)\rvert^2=\frac{\alpha}{\sqrt\pi}\mathrm{e}^{-\alpha^2x^2}
$$
是均值为 0、方差为 $\frac{1}{2\alpha^2}=\frac{\hbar}{2m\omega}$ 的**正态分布**（[3.1](/3.1)），在 $x=0$ 处最大；而经典振子在平衡位置速度最大、停留时间最短，在那里出现的概率最小，在转折点 $\pm A$ 附近速度为零、出现的概率最大，概率密度为 $\frac{1}{\pi\sqrt{A^2-x^2}}$。

另一个差别是，量子谐振子在经典禁区 $\lvert x\rvert>A_n$（$U>E$，$A_n=\sqrt{2n+1}/\alpha$）中也有概率，这是隧道效应的又一表现：基态粒子在禁区中的概率为 $\operatorname{erfc}(1)\approx0.16$。量子数增大时，$\lvert\psi_n\rvert^2$ 的振荡越来越密，平均起来趋于经典分布（上图右，$n=11$），这又是对应原理的体现。

### 3.4.4. 数值求解

能解析求解的势场很少。对一般的一维势 $U(x)$，可以把 $x$ 离散成步长为 $h$ 的网格，用中心差分 $\psi''(x_j)\approx(\psi_{j+1}-2\psi_j+\psi_{j-1})/h^2$ 代替二阶导数，定态 Schrödinger 方程就变成实对称三对角矩阵的特征值问题，用 SciPy 的对称特征值求解器即可（[4.4.3](/4.4.3#sec-3.2.3)、[4.4.4](/4.4.4)）。下面以谐振子检验这一方法（取 $\hbar=m=\omega=1$，精确值为 $n+\frac12$）：

```python
import numpy as np
from scipy.linalg import eigh_tridiagonal

# Units: hbar = m = omega = 1, so E_n should equal n + 1/2.
L, N = 10.0, 2000                       # grid on [-L, L], Phi = 0 at both ends
x, h = np.linspace(-L, L, N + 2, retstep=True)
x = x[1:-1]                              # interior points
diag = 1 / h**2 + 0.5 * x**2             # -1/2 Phi'' by central differences, plus U(x)
off = np.full(N - 1, -0.5 / h**2)
E, Phi = eigh_tridiagonal(diag, off, select="i", select_range=(0, 4))
print(np.round(E, 6))
```

```text
[0.499997 1.499984 2.499959 3.499922 4.499872]
```

误差约为 $10^{-5}$，随 $h^2$ 减小。区间端点 $\psi=0$ 的条件相当于在 $\pm L$ 处放了无限高的墙；只要 $L$ 远大于经典运动范围，它对低能级几乎没有影响。把 `0.5 * x**2` 换成其他势函数，同样的程序就能求出任意一维势阱的能级。

## 小结

| 模型 | 能级 | 主要结论 |
|---|---|---|
| 无限深方势阱（宽 $a$） | $E_n=\dfrac{\pi^2\hbar^2}{2ma^2}n^2$，$n=1,2,\dots$ | 能量量子化，零点能，驻波，$n\to\infty$ 时趋于经典 |
| 势垒（高 $U_0$，宽 $a$） | 连续 | 隧道效应，$T\sim\mathrm{e}^{-2\kappa a}$，$\kappa=\sqrt{2m(U_0-E)}/\hbar$ |
| 谐振子（角频率 $\omega$） | $E_n=(n+\frac12)\hbar\omega$，$n=0,1,2,\dots$ | 等间距能级，零点能 $\frac12\hbar\omega$，基态为正态分布 |

- Schrödinger 方程 $\mathrm{i}\hbar\,\partial_t\Psi=\hat H\Psi$ 是线性的一阶方程；势能不含时间时分离变量，得到能量本征方程 $\hat H\psi=E\psi$ 与定态 $\psi\,\mathrm{e}^{-\mathrm{i}Et/\hbar}$，一般解是定态的叠加。
- 束缚态的能量量子化来自波函数的标准条件（单值、有限、连续），在数学上就是边值问题只有分立的特征值。

## 思考题

1. Schrödinger 方程是严格推导出来的吗？
   提示：不是。§3.1.1 的推理只说明它与自由粒子的平面波相容；它是基本假设，由实验检验。
2. Schrödinger 方程怎样保证波函数服从叠加原理？
   提示：方程对 $\Psi$ 是线性齐次的，解的线性组合仍是解。
3. 在无限深方势阱和谐振子中，粒子处于基态时，除边界外概率密度为零的点有几处？第 $n$ 个激发态呢？
   提示：基态没有节点；方势阱的 $\psi_n$ 有 $n-1$ 个节点，谐振子的 $\psi_n$ 有 $n$ 个节点（谐振子从 $n=0$ 编号），即第 $k$ 个激发态都有 $k$ 个节点。
4. 宽度为 $2a$ 的无限深阱，右半部分的阱底抬高了 $U_0$（$E>U_0$）。粒子在左右两侧的波长哪个大？波函数的振幅哪个大？
   提示：右侧动能 $E-U_0$ 较小，动量小，波长较大；粒子在右侧运动较慢，停留时间较长，振幅也较大。
5. 比较经典和量子的一维谐振子。
   提示：能量连续与等间距分立；最低能量为零与零点能 $\frac12\hbar\omega$；概率分布在两端最大与基态在中央最大；粒子不能进入与可以进入 $U>E$ 的区域。
