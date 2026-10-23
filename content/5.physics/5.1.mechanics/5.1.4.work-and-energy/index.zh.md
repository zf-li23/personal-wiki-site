---
title: 功和能
description: 功与动能定理、一对力的功、保守力与势能、由势能求力与势能曲线、功能原理与机械能守恒、有心力场与有效势能、守恒律与对称性、碰撞、König 定理与两体问题、理想流体的连续性方程与 Bernoulli 方程。
---

[上一章](/5.1.3)讨论力对时间的积累：**冲量**改变**动量**，**冲量矩**改变**角动量**。本章讨论力对空间的积累：力沿路径的积分是功，功改变动能；做功与路径无关的力可以用一个标量函数（势能）代替，于是得到机械能守恒定律，它和动量守恒、角动量守恒一起构成力学的三条守恒律。数学上，功是**第二型曲线积分**，保守力就是**保守场**，势能是**势函数**（差一个负号），由势能求力就是求**梯度**，这些都在 [2.2.14](/2.2.14) 中讲过；本章着重它们的物理含义：每个量属于**质点**还是系统，是否依赖**参考系**。有心力问题利用能量与角动量两个守恒量把运动方程降为一阶，是**首次积分**方法（[2.4.14](/2.4.14)）的典型应用。最后两节把功能关系用于流体，得到 Bernoulli 方程。下一章 [5.1.5](/5.1.5) 把这些规律用于刚体；热学中的热力学第一定律（[5.2.3](/5.2.3)）是能量守恒定律在热现象中的推广。

## 4.1. 功

**定义 4.1.1（功）** 质点在力 $\boldsymbol{F}$ 作用下沿路径 $L$ 由 $A$ 运动到 $B$，力对质点所做的**功**是力与质点元**位移**的标积沿路径的积分：

$$
W_{AB}=\int_{L}\mathrm{d}W=\int_{A}^{B}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}=\int_{A}^{B}F\cos\theta\,\lvert\mathrm{d}\boldsymbol{r}\rvert,
$$
其中 $\theta$ 是 $\boldsymbol{F}$ 与 $\mathrm{d}\boldsymbol{r}$ 的夹角。功的 SI 单位是焦耳，$1\,\mathrm{J}=1\,\mathrm{N\,m}$。

功是一个**第二型曲线积分**，有三点要注意：

- 功是过程量，不是状态量：一般与路径有关，不能说"质点在某处具有多少功"。
- 功是标量，有正负之分：$0\le\theta<\pi/2$ 时力做正功，$\theta=\pi/2$ 时不做功，$\pi/2<\theta\le\pi$ 时做负功（常说"克服该力做功"）。
- 功依赖于参考系：同一个力在不同参考系中对应的位移不同。例如站在匀速上行电梯里的人，电梯对人的支持力在地面系中做正功，在电梯系中不做功。

单位时间内所做的功称为功率（power），$P=\dfrac{\mathrm{d}W}{\mathrm{d}t}=\boldsymbol{F}\cdot\boldsymbol{v}$，单位 $\mathrm{W}=\mathrm{J\,s^{-1}}$。

## 4.2. 动能定理

**定理 4.2.1（动能定理）** 在**惯性系**中，合力对质点所做的功等于质点动能的增量：

$$
W_{AB}=E_{\mathrm{k}}(B)-E_{\mathrm{k}}(A)=\Delta E_{\mathrm{k}},\qquad E_{\mathrm{k}}=\frac12mv^2 .
$$

**证明** 由 **Newton 第二定律**，$\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}=m\dfrac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t}\cdot\boldsymbol{v}\,\mathrm{d}t=m\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{v}=\mathrm{d}\Big(\dfrac12mv^2\Big)$，沿路径积分即得。$\square$

$E_{\mathrm{k}}=\frac12mv^2$ 称为质点的动能（kinetic energy），它是状态量。动能与功都依赖于参考系，但在任何一个**惯性系**中定理都成立；在**非惯性系**中，要把**惯性力**的功也算进去。

**定理 4.2.2（质点系的动能定理）** 对质点系中的每个质点用定理 4.2.1 再求和，

$$
W_{\mathrm{ext}}+W_{\mathrm{int}}=\sum_i\Delta E_{\mathrm{k}i},
$$
其中 $W_{\mathrm{ext}}$、$W_{\mathrm{int}}$ 分别是外力与内力所做功的总和。

**注 4.2.1** 内力总是成对出现，内力的矢量和为零，所以内力不改变系统的总动量；但内力功的总和一般不为零，因为一对内力的作用点位移不一定相同。炸弹爆炸、冰面上两人互推后分开，都是内力做正功使系统动能增加的例子。

## 4.3. 一对力的功

两个质点之间的一对力是分别作用在两个质点上、大小相等、方向相反的力 $\boldsymbol{f}_1=-\boldsymbol{f}_2$（作用力与反作用力是最常见的一对力）。设质点 $m_1$、$m_2$ 的元位移分别为 $\mathrm{d}\boldsymbol{r}_1$、$\mathrm{d}\boldsymbol{r}_2$，这对力的元功之和为

$$
\mathrm{d}W_{\mathrm{pair}}=\boldsymbol{f}_1\cdot\mathrm{d}\boldsymbol{r}_1+\boldsymbol{f}_2\cdot\mathrm{d}\boldsymbol{r}_2=\boldsymbol{f}_2\cdot(\mathrm{d}\boldsymbol{r}_2-\mathrm{d}\boldsymbol{r}_1)=\boldsymbol{f}_2\cdot\mathrm{d}\boldsymbol{r}_{21},
$$
其中 $\boldsymbol{r}_{21}=\boldsymbol{r}_2-\boldsymbol{r}_1$ 是 $m_2$ 相对 $m_1$ 的**位矢**。从初位形 $A$（$m_1$ 在 $A_1$、$m_2$ 在 $A_2$）到末位形 $B$（$m_1$ 在 $B_1$、$m_2$ 在 $B_2$），

$$
W_{\mathrm{pair}}=\int_A^B\boldsymbol{f}_2\cdot\mathrm{d}\boldsymbol{r}_{21}=\int_A^B\boldsymbol{f}_1\cdot\mathrm{d}\boldsymbol{r}_{12}.
$$

**性质 4.3.1** 一对力的功只取决于两质点的相对位移，因此：

1. 一对力的功与参考系的选取无关；
2. 两质点之间无相对位移，或相对位移总与这对力垂直时，一对力的功为零；
3. 一对滑动摩擦力的功恒为负：滑动摩擦力总与相对滑动方向相反，$W_{\mathrm{pair}}=-\int f\,\mathrm{d}s_{\mathrm{rel}}<0$（$s_{\mathrm{rel}}$ 为相对滑动的路程）。摩擦生热就是这对力做负功的结果，产生的热量 $-W_{\mathrm{pair}}$ 与参考系无关。

**例 4.3.1** 物块 $m$ 沿光滑斜面体 $M$ 下滑，斜面体放在光滑水平面上。在地面系中，$m$ 的**速度** $\boldsymbol{v}_m$ 并不沿斜面，所以斜面对物块的支持力 $\boldsymbol{N}$ 与 $\boldsymbol{v}_m$ 不垂直，$W_N\ne0$；同样物块对斜面的压力 $\boldsymbol{N}'$ 与斜面的速度 $\boldsymbol{v}_M$ 不垂直，$W_{N'}\ne0$。但 $m$ 相对 $M$ 的位移沿斜面，与 $\boldsymbol{N}$ 垂直，所以这一对力的功 $W_N+W_{N'}=0$。

## 4.4. 保守力

**定义 4.4.1（保守力）** 若一对力所做的功与两质点相对移动的路径无关，只取决于两质点的始末相对位置，则称这对力为**保守力**。等价地，沿任意闭合路径 $L$（相对位形回到原状），

$$
\oint_L\boldsymbol{f}\cdot\mathrm{d}\boldsymbol{r}=0 .
$$

两种说法等价，这正是 [定理 14.4.1](/2.2.14#thm-14.4.1) 中"保守场"与"闭路积分为零"的等价；力场 $\boldsymbol{f}(\boldsymbol{r})$ 是保守力当且仅当它是**保守场**。

### 4.4.1. 常见的保守力

1. 万有引力。质点 $m$ 在质点 $M$ 的引力 $\boldsymbol{f}=-\dfrac{GMm}{r^2}\boldsymbol{e}_r$ 作用下从 $A$ 到 $B$。由于 $\boldsymbol{e}_r\cdot\mathrm{d}\boldsymbol{r}=\mathrm{d}r$（位移沿径向的分量就是 $r$ 的增量），
   $$
   W=\int_A^B\Big(-\frac{GMm}{r^2}\Big)\boldsymbol{e}_r\cdot\mathrm{d}\boldsymbol{r}=\int_{r_A}^{r_B}\Big(-\frac{GMm}{r^2}\Big)\mathrm{d}r=\frac{GMm}{r_B}-\frac{GMm}{r_A},
   $$
   只与始末距离有关。同样的计算说明：任何只依赖于距离的有心力 $\boldsymbol{f}=f(r)\boldsymbol{e}_r$ 都是保守力，因为 $\boldsymbol{f}\cdot\mathrm{d}\boldsymbol{r}=f(r)\,\mathrm{d}r$ 是全微分。
2. 弹簧的弹力（一维）：$\boldsymbol{f}=-k(x-x_0)\boldsymbol{e}_x$，$x-x_0$ 是弹簧的伸长量，$k$ 是劲度系数。
3. 重力：$\boldsymbol{F}=m\boldsymbol{g}$（地面附近的均匀引力场）。

### 4.4.2. 非保守力

做功与路径有关的力称为非保守力。

- 摩擦力。一对滑动摩擦力的功恒为负，把机械能转化为热，这种力称为耗散力（dissipative force）。静摩擦力对单个物体做的功可正、可负、可零（如传送带带动货物），但一对静摩擦力之间没有相对滑动，它们的功之和为零，所以静摩擦力不是耗散力。
- 爆炸力等：作为内力做正功，把化学能等转化为机械能。

## 4.5. 势能

### 4.5.1. 势能的定义

保守力做功与路径无关，因此可以引入一个只依赖于系统位形的标量函数，用它的变化代替保守力的功。

**定义 4.5.1（势能）** 系统由位形 $A$ 变到位形 $B$ 的过程中，保守内力所做的功等于系统**势能**的减少：

$$
E_{\mathrm{p}}(A)-E_{\mathrm{p}}(B)=-\Delta E_{\mathrm{p}}=W_{\mathrm{c,int}}=\int_A^B\boldsymbol{f}_{\mathrm{c}}\cdot\mathrm{d}\boldsymbol{r} .
$$
选定某个位形 $O$ 为势能零点，$E_{\mathrm{p}}(O)=0$，则 $E_{\mathrm{p}}(A)=\int_A^O\boldsymbol{f}_{\mathrm{c}}\cdot\mathrm{d}\boldsymbol{r}$。

与 [2.2.14](/2.2.14) 中的**势函数** $\varphi$（$\nabla\varphi=\boldsymbol{f}$）相比，势能 $E_{\mathrm{p}}=-\varphi+C$ 差一个负号：物理上习惯让"力做正功"对应"势能减少"。

- 势能属于相互作用的整个系统，不属于单个质点；"物体的重力势能"是"物体与地球组成的系统的势能"的简称。
- 势能只由保守力的一对力的功定义，而一对力的功与参考系无关（性质 4.3.1），所以势能与参考系的选择无关；势能零点的选择也与参考系无关。
- 势能只确定到一个常数，有物理意义的是势能差。

### 4.5.2. 几种势能

| 系统 | 势能 | 常用的零点 |
|---|---|---|
| 两质点间的万有引力 | $E_{\mathrm{p}}(r)=-\dfrac{GMm}{r}$ | $E_{\mathrm{p}}(\infty)=0$ |
| 地面附近的重力 | $E_{\mathrm{p}}(h)=mgh$ | $E_{\mathrm{p}}(0)=0$（$h$ 为高度） |
| 弹簧 | $E_{\mathrm{p}}(x)=\dfrac12k(x-x_0)^2$ | $E_{\mathrm{p}}(x_0)=0$（自然长度） |

## 4.6. 由势能求保守力

### 4.6.1. 由势能函数求保守力

由定义 4.5.1，沿任意元位移 $\mathrm{d}\boldsymbol{l}$ 有 $\boldsymbol{f}_{\mathrm{c}}\cdot\mathrm{d}\boldsymbol{l}=-\mathrm{d}E_{\mathrm{p}}$。设 $\boldsymbol{f}_{\mathrm{c}}$ 与方向 $\boldsymbol{l}$ 的夹角为 $\theta$，则 $f_{\mathrm{c}}\cos\theta\,\mathrm{d}l=-\mathrm{d}E_{\mathrm{p}}$，即

$$
f_{\mathrm{c},l}=-\frac{\partial E_{\mathrm{p}}}{\partial l}:
$$
保守力沿某一方向的分量等于势能沿该方向的**方向导数**的负值。分别取 $x$、$y$、$z$ 方向，

$$
\boldsymbol{f}_{\mathrm{c}}=-\Big(\frac{\partial E_{\mathrm{p}}}{\partial x}\boldsymbol{e}_x+\frac{\partial E_{\mathrm{p}}}{\partial y}\boldsymbol{e}_y+\frac{\partial E_{\mathrm{p}}}{\partial z}\boldsymbol{e}_z\Big)=-\operatorname{grad}E_{\mathrm{p}}=-\nabla E_{\mathrm{p}},\tag{4.1}
$$
其中 $\nabla$ 是 **Hamilton 算子**。由于**梯度**指向函数增长最快的方向，保守力指向势能下降最快的方向，大小等于势能在该方向上的变化率。

**例 4.6.1** 弹簧的弹性势能 $E_{\mathrm{p}}=\frac12k(x-x_0)^2$ 给出 $\boldsymbol{f}=-\dfrac{\partial E_{\mathrm{p}}}{\partial x}\boldsymbol{e}_x=-k(x-x_0)\boldsymbol{e}_x$；引力势能 $E_{\mathrm{p}}=-GMm/r$ 给出 $\boldsymbol{f}=-\dfrac{\mathrm{d}E_{\mathrm{p}}}{\mathrm{d}r}\boldsymbol{e}_r=-\dfrac{GMm}{r^2}\boldsymbol{e}_r$。

### 4.6.2. 势能曲线

一维情形下式 (4.1) 化为 $f=-\dfrac{\mathrm{d}E_{\mathrm{p}}}{\mathrm{d}x}$：保守力指向势能下降的方向，大小等于势能曲线的斜率。势能随位形变化的图线称为势能曲线（potential energy curve），它直观地反映系统的平衡与稳定性。

- 势能曲线的局部极小点是稳定平衡位置：质点稍偏离时受到指向平衡位置的力，在其附近作小振动（[5.1.6](/5.1.6) 将证明这种小振动是简谐振动）。
- 局部极大点是不稳定平衡位置：质点稍偏离就受到背离平衡位置的力而远离。
- 势能为常数的一段是随遇平衡；局部极小但不是全局最小的位置称为亚稳平衡。
- 机械能守恒时 $E_{\mathrm{k}}=E-E_{\mathrm{p}}(x)\ge0$，所以质点只能在 $E_{\mathrm{p}}(x)\le E$ 的区域内运动，$E_{\mathrm{p}}(x)=E$ 的点是转折点。被势能较高的区域（势垒）包围的低势能区域称为势阱；质点在势阱 $A$ 中的动能超过势垒高度 $\Delta E_1$ 时，才能越过势垒进入相邻的势阱 $B$。

这些判断就是 [2.4.11](/2.4.11) 中**平衡点**稳定性理论的力学版本：方程 $m\ddot x=-E_{\mathrm{p}}'(x)$ 的平衡点是 $E_{\mathrm{p}}'=0$ 的点；若 $E_{\mathrm{p}}$ 在 $x_0$ 有严格局部极小，机械能 $E(x,\dot x)-E_{\mathrm{p}}(x_0)$ 正定且沿轨线不变，正是一个 **Lyapunov 函数**，由 [定理 11.4.1](/2.4.11#thm-11.4.1) 得到稳定性（Lagrange–Dirichlet 定理）。

**例 4.6.2（双原子分子的势能曲线）** 两原子之间的势能 $E_{\mathrm{p}}(r)$ 在核间距 $r=r_0$ 处取极小值。$r=r_0$ 时 $f=0$，是平衡位置；$r>r_0$ 时 $f=-\mathrm{d}E_{\mathrm{p}}/\mathrm{d}r<0$，表现为引力；$r<r_0$ 时 $f>0$，表现为斥力。常用的模型是 Lennard-Jones 势

$$
E_{\mathrm{p}}(r)=4\varepsilon\Big[\Big(\frac{\sigma}{r}\Big)^{12}-\Big(\frac{\sigma}{r}\Big)^{6}\Big],
$$
它在 $r_0=2^{1/6}\sigma$ 处取极小值 $-\varepsilon$，$\varepsilon$ 是势阱深度。分子在 $r_0$ 附近的小振动就是分子振动；实际双原子分子中电子的贡献要用量子力学计算，Lennard-Jones 势更适合描述惰性气体原子之间的作用（[5.2.2](/5.2.2) 讨论分子力与真实气体）。

![Lennard-Jones potential energy E_p(r) and the corresponding force f(r) = -dE_p/dr in reduced units; the minimum at r0 = 2^(1/6) sigma is the equilibrium separation, the force is repulsive for r < r0 and attractive for r > r0](./plots/lennard-jones.py)

## 4.7. 功能原理和机械能守恒定律

### 4.7.1. 功能原理

把质点系的内力分为保守内力与非保守内力，$W_{\mathrm{int}}=W_{\mathrm{c,int}}+W_{\mathrm{nc,int}}$，并用定义 4.5.1 把 $W_{\mathrm{c,int}}$ 写成势能的减少，定理 4.2.2 就变为

$$
W_{\mathrm{ext}}+W_{\mathrm{nc,int}}=\big[E_{\mathrm{k}}(B)+E_{\mathrm{p}}(B)\big]-\big[E_{\mathrm{k}}(A)+E_{\mathrm{p}}(A)\big].
$$

**定理 4.7.1（功能原理）** 定义系统的机械能（mechanical energy）$E=E_{\mathrm{k}}+E_{\mathrm{p}}$，则在惯性系中，外力的功与非保守内力的功之和等于系统机械能的增量：

$$
W_{\mathrm{ext}}+W_{\mathrm{nc,int}}=E(B)-E(A),\qquad \mathrm{d}W_{\mathrm{ext}}+\mathrm{d}W_{\mathrm{nc,int}}=\mathrm{d}E .
$$

动能定理与功能原理是同一规律的两种写法：前者把保守内力的功算作功，后者把它算进势能，二者不能重复计入。

### 4.7.2. 机械能守恒定律

**定理 4.7.2（机械能守恒定律）** 若 $\mathrm{d}W_{\mathrm{ext}}=0$ 且 $\mathrm{d}W_{\mathrm{nc,int}}=0$，即只有保守内力做功，则系统的机械能保持不变，$E=$ 常量。

孤立的保守系统的机械能守恒。此时 $\Delta E_{\mathrm{k}}=-\Delta E_{\mathrm{p}}=W_{\mathrm{c,int}}$：保守内力做正功时势能转化为动能，做负功时动能转化为势能，势能与动能的相互转化通过保守内力做功来实现和度量。由于外力的功依赖于参考系，机械能是否守恒也与惯性系的选择有关：一个系统在某个惯性系中机械能守恒，在另一个惯性系中外力可能做功。

### 4.7.3. 普遍的能量守恒定律

考虑各种物理现象，计入热、电磁、化学、核等各种形式的能量，有

**定理 4.7.3（能量守恒定律）** 一个孤立系统无论经历何种变化，系统所有形式的能量的总和保持不变。

机械能守恒定律是能量守恒定律在机械运动范围内的体现：耗散力做功时减少的机械能并没有消失，而是转化成了内能等其他形式的能量。热力学第一定律（[5.2.3](/5.2.3)）是它在热现象中的定量表述。

### 4.7.4. 守恒定律联合应用举例

**例 4.7.1** 质量为 $M$ 的斜面体放在光滑水平面上，斜面光滑。质量为 $m$ 的滑块以水平初速度 $v$ 从斜面底端冲上斜面（底端与水平面平滑连接，滑块不脱离斜面），求滑块上升的最大高度 $h_{\max}$。

**解** 取 $m$、$M$ 与地球为系统：外力（地面支持力）不做功，没有非保守内力做功，机械能守恒。$h=h_{\max}$ 时滑块相对斜面静止，二者有相同的水平速度 $V$。取地面为重力势能零点，

$$
\frac12mv^2=\frac12(m+M)V^2+mgh_{\max}.
$$
对 $m+M$，水平方向不受外力，由**动量守恒定律**，水平动量守恒：$mv=(m+M)V$。两式联立得

$$
h_{\max}=\frac{M}{M+m}\cdot\frac{v^2}{2g}.
$$
检验结果的合理性：**量纲**正确；$m/M\to0$ 时斜面不动，$mgh_{\max}=\frac12mv^2$，与预期一致。

### 4.7.5. 质点在有心力场中的运动

方向始终沿着（或背离）一个固定中心的力称为有心力（central force），其中只依赖于距离的 $\boldsymbol{F}=f(r)\boldsymbol{e}_r$（$\boldsymbol{e}_r$ 是以力心为原点的径向单位矢量）称为有心力场，万有引力与 Coulomb 力都是如此。由 4.4.1 节，有心力场是保守力场，势能为 $E_{\mathrm{p}}(r)=\int_r^{r_0}f(r)\,\mathrm{d}r+E_{\mathrm{p}}(r_0)$。

有心力对力心的**力矩**为零，质点在有心力场中运动有两个守恒量：

- 由**角动量守恒定律**，$\boldsymbol{L}=\boldsymbol{r}\times m\boldsymbol{v}$ 为常矢量，所以运动在过力心、垂直于 $\boldsymbol{L}$ 的平面内（[5.1.3](/5.1.3)）；
- 机械能守恒，$E$ 为常量。

在运动平面内取**极坐标** $(r,\theta)$，$\boldsymbol{r}=r\boldsymbol{e}_r$，$\boldsymbol{v}=\dot r\boldsymbol{e}_r+r\dot\theta\boldsymbol{e}_\theta$。由 $\boldsymbol{L}=r\boldsymbol{e}_r\times m(\dot r\boldsymbol{e}_r+r\dot\theta\boldsymbol{e}_\theta)=mr^2\dot\theta\,(\boldsymbol{e}_r\times\boldsymbol{e}_\theta)$ 与机械能守恒，

$$
mr^2\dot\theta=L,\qquad \frac12m\big(\dot r^2+r^2\dot\theta^2\big)+E_{\mathrm{p}}(r)=E .
$$
消去 $\dot\theta$ 得到只含 $r$ 的方程

$$
\frac12m\dot r^2+\frac{L^2}{2mr^2}+E_{\mathrm{p}}(r)=E.\tag{4.2}
$$
这两个一阶方程可以代替 Newton 方程（两个二阶方程）：利用守恒量把方程降了一阶，这正是**首次积分**的作用。常数 $L$ 与 $E$ 由初始条件 $\boldsymbol{r}_0$、$\boldsymbol{v}_0$ 决定，$L=\lvert\boldsymbol{r}_0\times m\boldsymbol{v}_0\rvert$，$E=\frac12mv_0^2+E_{\mathrm{p}}(r_0)$；初始条件与势能函数的形式一起决定轨道的特征：是否封闭、形状、大小与取向。

式 (4.2) 中 $\frac12m\dot r^2$ 是径向动能，$\dfrac{L^2}{2mr^2}$ 是横向运动的动能，它随 $r$ 减小而增大，效果相当于一个斥力的势能，称为离心势能。称

$$
E_{\mathrm{eff}}(r)=\frac{L^2}{2mr^2}+E_{\mathrm{p}}(r)
$$
为有效势能（effective potential），则沿径向，质点就像一维质点在保守势场 $E_{\mathrm{eff}}(r)$ 中运动，径向动能与有效势能相互转化，可以用 4.6.2 节的势能曲线分析。

对万有引力，$E_{\mathrm{eff}}(r)=\dfrac{L^2}{2mr^2}-\dfrac{GMm}{r}$。近日点与远日点处 $\dot r=0$，有效势能等于总机械能，$r$ 满足

$$
r^2+\frac{GMm}{E}r-\frac{L^2}{2mE}=0 .
$$

- $E=E_{\mathrm{eff,min}}$：只有 $r=r_0$ 一个解，圆轨道；
- $E_{\mathrm{eff,min}}<E<0$：两个正根 $r_{\min}\le r\le r_{\max}$，椭圆轨道，是束缚态；
- $E=0$：只有一个正根，抛物线轨道，质点刚好逃逸，到无穷远处动能为零；
- $E>0$：一个正根，双曲线轨道，质点不受束缚，到无穷远处仍有动能。

有效势能只说明 $r$ 的变化范围；轨道恰好是圆锥曲线（封闭的椭圆）是平方反比力的特殊性质，可以从式 (4.2) 与 $mr^2\dot\theta=L$ 消去 $t$ 积分得到。

![Left: effective potential E_eff(r) = L^2/(2 m r^2) - G M m / r for fixed angular momentum, with energy levels of a circular orbit, an ellipse (r_min to r_max), the parabolic case E = 0 and a hyperbola; right: orbits launched from the same point with velocity perpendicular to the radius and increasing speed (circle, ellipse, parabola, hyperbola)](./plots/effective-potential.py)

势能函数确定后，改变初始条件就能改变轨道。例如飞船绕地球作**速率**为 $v_0$ 的匀速圆周运动，在极短时间内沿径向向外（或向内）喷气，获得一个指向（或背离）地心的小速度 $\alpha v_0$。喷气瞬间位矢不变，切向速度不变，所以角动量 $L$ 不变，而机械能增加 $\frac12m\alpha^2v_0^2$：新轨道是过喷气点的椭圆，两种喷气方向得到的椭圆关于喷气点的径向对称，一个的近地点在喷气点之前，一个在之后。

![A ship on a circular orbit receives a small radial velocity kick alpha v0 (alpha = 0.3) at the marked point; the dashed and dotted ellipses are the new orbits for an inward and an outward kick, both with the same angular momentum as the circle](./plots/orbit-kick.py)

实际航天任务正是这样设计的。1978 年发射的 ISEE-3 探测器原本停在日地 L1 点附近的晕轨道上，1982–1983 年经过一系列点火与五次飞掠月球（借月球引力变轨）离开地月系统，更名为 ICE，1985 年穿过 Giacobini–Zinner 彗星的彗尾（第一个穿过彗尾的航天器），1986 年在远距离上观测了哈雷彗星，2014 年回到地球附近。

## 4.8. 守恒定律的意义

动量、角动量、能量三条守恒律都比 Newton 定律更普遍：它们在 Newton 力学失效的领域（高速运动、微观粒子）仍然成立。它们的根源是时空的对称性：

| 守恒律 | 对应的对称性 |
|---|---|
| 动量守恒 | 空间平移对称性（空间均匀） |
| 角动量守恒 | 空间转动对称性（空间各向同性） |
| 能量守恒 | 时间平移对称性（时间均匀） |

这一对应称为 Noether 定理（Noether's theorem）：物理规律的每一种连续对称性都对应一个守恒量（E. Noether，1918 年）。其严格表述要用分析力学，即由作用量的变分得到运动方程（**Euler–Lagrange 方程**，[2.4.13](/2.4.13)），若 Lagrange 函数在某个连续变换下不变，就有一个对应的首次积分。

## 4.9. 碰撞

碰撞是两个或多个物体在极短时间内发生强烈相互作用的过程。处理碰撞问题时，只关心运动状态在碰撞前后的变化，忽略过程的细节；碰撞时间极短、内力极大，通常可以忽略外力（如重力、摩擦力）的冲量，系统动量守恒。

**定义 4.9.1** 碰撞前后系统的总动能不变的碰撞称为**弹性碰撞**；碰撞中有动能损失的称为**非弹性碰撞**；碰撞后两物体以相同速度运动的称为**完全非弹性碰撞**，它的动能损失最大。

**例 4.9.1（一维弹性碰撞）** 质量 $m_1$、$m_2$ 的两球沿同一直线运动，碰前速度 $v_{10}$、$v_{20}$，碰后速度 $v_1$、$v_2$（取同一正方向的分量）。动量守恒与动能守恒

$$
m_1v_{10}+m_2v_{20}=m_1v_1+m_2v_2,\qquad \frac12m_1v_{10}^2+\frac12m_2v_{20}^2=\frac12m_1v_1^2+\frac12m_2v_2^2 .
$$
把两式分别写成 $m_1(v_{10}-v_1)=m_2(v_2-v_{20})$ 与 $m_1(v_{10}^2-v_1^2)=m_2(v_2^2-v_{20}^2)$ 相除，得 $v_{10}+v_1=v_{20}+v_2$，即 $v_2-v_1=v_{10}-v_{20}$：弹性碰撞前后**相对速度**大小不变、方向相反。解得

$$
v_1=\frac{m_1-m_2}{m_1+m_2}v_{10}+\frac{2m_2}{m_1+m_2}v_{20},\qquad
v_2=\frac{m_2-m_1}{m_1+m_2}v_{20}+\frac{2m_1}{m_1+m_2}v_{10}.
$$

- $m_1=m_2$：$v_1=v_{20}$，$v_2=v_{10}$，两球交换速度。
- $m_2\gg m_1$ 且 $v_{20}=0$：$v_1\approx-v_{10}$，$v_2\approx0$，小球以原速率弹回。

一般的一维碰撞常用恢复系数 $e=\dfrac{v_2-v_1}{v_{10}-v_{20}}$ 描述：弹性碰撞 $e=1$，完全非弹性碰撞 $e=0$，非弹性碰撞 $0<e<1$。完全非弹性碰撞中损失的动能见 4.10.3 节。

## 4.10. 质心系中的功能关系

### 4.10.1. König 定理

设质点系总质量 $m=\sum_im_i$，质心速度 $\boldsymbol{v}_C$。在**质心系** $S'$ 中各质点速度为 $\boldsymbol{v}_i'$，$\sum_im_i\boldsymbol{v}_i'=\boldsymbol{0}$；在惯性系 $S$ 中 $\boldsymbol{v}_i=\boldsymbol{v}_i'+\boldsymbol{v}_C$。

**定理 4.10.1（König 定理）** 质点系在惯性系中的动能等于它在质心系中的动能加上质心的动能：

$$
E_{\mathrm{k}}=E_{\mathrm{k}}'+E_{\mathrm{k}C},\qquad E_{\mathrm{k}}'=\sum_i\frac12m_iv_i'^2,\quad E_{\mathrm{k}C}=\frac12mv_C^2 .
$$

**证明**

$$
E_{\mathrm{k}}=\sum_i\frac12m_i(\boldsymbol{v}_i'+\boldsymbol{v}_C)\cdot(\boldsymbol{v}_i'+\boldsymbol{v}_C)=\sum_i\frac12m_iv_i'^2+\Big(\sum_im_i\boldsymbol{v}_i'\Big)\cdot\boldsymbol{v}_C+\frac12\Big(\sum_im_i\Big)v_C^2,
$$
中间一项为零。$\square$

### 4.10.2. 质心系中的功能原理

**定理 4.10.2** 在质心系中，功能原理与机械能守恒定律仍然成立，而且形式与惯性系中相同，无论质心系是否为惯性系：

$$
\mathrm{d}W_{\mathrm{ext}}'+\mathrm{d}W_{\mathrm{nc,int}}'=\mathrm{d}E',\qquad W_{\mathrm{ext}}'+W_{\mathrm{nc,int}}'=\Delta E' .
$$

**证明** 质心系是惯性系时显然成立。若质心系有**加速度** $\boldsymbol{a}_C$，还要计入平动**惯性力** $-m_i\boldsymbol{a}_C$ 的功：

$$
\mathrm{d}W_{\mathrm{in}}'=\sum_i(-m_i\boldsymbol{a}_C)\cdot\mathrm{d}\boldsymbol{r}_i'=-\boldsymbol{a}_C\cdot\Big(\sum_im_i\boldsymbol{v}_i'\Big)\mathrm{d}t=-\boldsymbol{a}_C\cdot m\boldsymbol{v}_C'\,\mathrm{d}t=0,
$$
因为质心在质心系中静止，$\boldsymbol{v}_C'=\boldsymbol{0}$。$\square$

于是：若 $\mathrm{d}W_{\mathrm{ext}}'=0$ 且 $\mathrm{d}W_{\mathrm{nc,int}}'=0$，则质心系中机械能 $E'$ 守恒。

### 4.10.3. 两质点系统在质心系中的动能

对两个质点，$\boldsymbol{v}_C=\dfrac{m_1\boldsymbol{v}_1+m_2\boldsymbol{v}_2}{m_1+m_2}$，由 König 定理

$$
E_{\mathrm{k}}'=E_{\mathrm{k}}-E_{\mathrm{k}C}=\frac12m_1v_1^2+\frac12m_2v_2^2-\frac{(m_1\boldsymbol{v}_1+m_2\boldsymbol{v}_2)^2}{2(m_1+m_2)}=\frac12\frac{m_1m_2}{m_1+m_2}\lvert\boldsymbol{v}_2-\boldsymbol{v}_1\rvert^2 .
$$

**定义 4.10.1（约化质量）** 两质点的**约化质量**为 $\mu=\dfrac{m_1m_2}{m_1+m_2}$。

记**相对速度** $\boldsymbol{v}_{\mathrm{r}}=\boldsymbol{v}_2-\boldsymbol{v}_1$，则两质点系统在质心系中的动能为 $E_{\mathrm{k}}'=\frac12\mu v_{\mathrm{r}}^2$。在完全非弹性碰撞中，碰后两物体相对静止，而质心动能 $E_{\mathrm{k}C}$ 由于动量守恒不变，所以损失的动能恰为 $\frac12\mu v_{\mathrm{r}}^2$，即碰前在质心系中的全部动能。

## 4.11. 两体问题

两个物体只在相互作用下运动的问题称为两体问题（two-body problem），如 $\alpha$ 粒子被原子核散射、行星绕太阳运动、双星。它可以化为单体问题。

设两质点之间的作用力是有心力，$\boldsymbol{r}=\boldsymbol{r}_1-\boldsymbol{r}_2$ 为 $m_1$ 相对 $m_2$ 的位矢。在惯性系中

$$
m_1\ddot{\boldsymbol{r}}_1=f(r)\boldsymbol{e}_r,\qquad m_2\ddot{\boldsymbol{r}}_2=-f(r)\boldsymbol{e}_r .
$$
以 $m_2$ 乘第一式、$m_1$ 乘第二式后相减，得 $m_1m_2(\ddot{\boldsymbol{r}}_1-\ddot{\boldsymbol{r}}_2)=(m_1+m_2)f(r)\boldsymbol{e}_r$，即

$$
\mu\ddot{\boldsymbol{r}}=f(r)\boldsymbol{e}_r .
$$

$m_1$ 相对 $m_2$ 的运动，等效于一个质量为 $\mu$ 的质点在 $m_2$ 的平动参考系（以 $m_2$ 为原点）中受同样的力作用的运动。这个参考系不是惯性系，但把 $m_1$ 换成 $\mu$ 后 Newton 第二定律仍然适用，有关动量、角动量与能量的定理也都适用：用 $\mu$ 代替 $m_1$ 恰好计入了作用在 $m_1$ 上的惯性力 $-m_1\ddot{\boldsymbol{r}}_2$。原来的问题由此分解为质心的匀速运动与相对运动两部分。$m_2\gg m_1$ 时 $\mu\approx m_1$，回到力心固定的情形（4.7.5 节）。

**例 4.11.1** 一个质子以速率 $v_0$ 从远处正对着另一个静止的质子运动，求二者的最近距离 $r_{\min}$。

**解** 以静止的质子为原点，约化质量 $\mu=m_{\mathrm{p}}/2$，两者间是 Coulomb 斥力，势能 $\dfrac{e^2}{4\pi\varepsilon_0r}$（[5.3.1](/5.3.1)）。正碰时角动量为零，最近处相对速度为零，能量守恒给出

$$
\frac12\mu v_0^2=\frac{e^2}{4\pi\varepsilon_0r_{\min}},\qquad r_{\min}=\frac{e^2}{\pi\varepsilon_0m_{\mathrm{p}}v_0^2} .
$$
这与质心系中的能量守恒方程一致：最近时两质子都相对质心静止，质心动能不变，可转化为势能的只有质心系中的动能 $\frac12\mu v_0^2$。

**例 4.11.2** 光滑水平面上，两小球 $m_1$、$m_2$ 用长为 $l$ 的轻绳相连。开始时绳拉直，两球的速度 $v_1$、$v_2$ 同向且与绳垂直，求此时绳的张力 $T$。

**解** 在 $m_2$ 的平动参考系中，$m_1$ 以相对速率 $\lvert v_1-v_2\rvert$ 绕 $m_2$ 作半径为 $l$ 的圆周运动，用约化质量写 Newton 第二定律：

$$
T=\mu\frac{(v_1-v_2)^2}{l}=\frac{m_1m_2}{m_1+m_2}\cdot\frac{(v_1-v_2)^2}{l}.
$$

## 4.12. 流体的稳定流动

流体是可以流动的特殊质点系。作为最简单的模型，不可压缩、没有黏性（各部分之间没有内摩擦，可以自由地相对流动）的流体称为理想流体（ideal fluid）。

**定义 4.12.1** 流体中各点的流速不随时间变化的流动称为**稳定流动**（定常流动）。稳定流动中，处处与流速相切的曲线称为**流线**，由流线围成的细管称为**流管**；流体不会穿过流管的侧壁。

**定理 4.12.1（连续性方程）** 理想流体作稳定流动时，同一流管中任意两个横截面 $S_1$、$S_2$ 处的流速满足

$$
S_1v_1=S_2v_2 .
$$

**证明** 在 $\Delta t$ 内流过 $S_1$ 的流体体积 $S_1v_1\Delta t$，必等于流过 $S_2$ 的体积 $S_2v_2\Delta t$（流体不可压缩，流管侧面无流体穿过，两截面之间的流体体积不变）。$\square$

对可压缩流体，质量守恒给出 $\rho_1S_1v_1=\rho_2S_2v_2$。连续性方程是质量守恒的一种形式；它的微分形式 $\dfrac{\partial\rho}{\partial t}+\nabla\cdot(\rho\boldsymbol{v})=0$ 就是 [2.5.2](/2.5.2) 中的**守恒律**，由 **Gauss 公式**从积分形式得到。

## 4.13. Bernoulli 方程

用功能原理研究稳定流动中压强、流速与高度的关系。取流管中位于截面 $S_1$、$S_2$ 之间的一段理想流体，经过 $\Delta t$ 移到 $S_1'$、$S_2'$ 之间。由于流动稳定，$S_1'$ 与 $S_2$ 之间那部分流体的状态不变，总效果是质量 $\Delta m=\rho S_1v_1\Delta t=\rho S_2v_2\Delta t$ 的流体从截面 1 处（高度 $h_1$、流速 $v_1$、压强 $p_1$）移到了截面 2 处。理想流体无黏性，没有非保守内力做功；外力中，两端的压力做功 $p_1S_1v_1\Delta t-p_2S_2v_2\Delta t=(p_1-p_2)\Delta m/\rho$，侧壁压力与流动方向垂直不做功。取流体与地球为系统，功能原理给出

$$
\frac{(p_1-p_2)\Delta m}{\rho}=\Delta m\Big[\Big(\frac12v_2^2+gh_2\Big)-\Big(\frac12v_1^2+gh_1\Big)\Big].
$$

**定理 4.13.1（Bernoulli 方程）** 理想流体作稳定流动时，沿同一条流线

$$
p+\frac12\rho v^2+\rho gh=\text{const}.
$$

Bernoulli 方程是理想流体的机械能守恒定律：$\frac12\rho v^2$ 与 $\rho gh$ 是单位体积流体的动能与重力势能，$p$ 是单位体积流体通过压力做功所能传递的能量。

**例 4.13.1（小孔流速）** 敞口的水桶静止放置，水深 $h$，底部水龙头打开后求出口处的流速。水面与出口都和大气接触，压强为 $p_0$；水桶截面远大于出口截面，由连续性方程，水面下降的速度近似为零。沿从水面到出口的流线，

$$
p_0+\rho gh=p_0+\frac12\rho v^2,\qquad v=\sqrt{2gh},
$$
与质点从高度 $h$ 自由落下的速率相同（Torricelli 定律）。

**例 4.13.2（流速大处压强小）** 水平放置的流管中 $h$ 处处相同，$p_1+\frac12\rho v_1^2=p_2+\frac12\rho v_2^2$。由连续性方程，截面小处流速大，因而压强小。Venturi 流量计就是根据两截面的压强差测量流量的。

下面几个现象常用"流速大处压强小"作定性说明：

- 机翼的升力：机翼使上方气流加速、下方气流减速，上方压强小于下方。这个说明本身没错，但通俗解释中"上下两股空气必须同时到达后缘、所以上方更快"的说法是错误的；升力的完整解释要考虑机翼对气流的偏转（环量）。
- 两船并排航行时容易相互靠近：两船之间的水相对船流速较大、压强较小，两船都受到指向对方的合力。
- 旋转的足球（"香蕉球"）弧线飞行：球的旋转使两侧空气相对球的流速不同，流速大的一侧压强小，球偏向这一侧（Magnus 效应）。旋转带动空气要靠黏性，所以这只是半定量的说明。

## 小结

| 概念或规律 | 内容 | 对象 | 与参考系的关系 |
|---|---|---|---|
| 功 | $W=\int\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}$ | 力与质点 | 依赖 |
| 一对力的功 | $W=\int\boldsymbol{f}_2\cdot\mathrm{d}\boldsymbol{r}_{21}$ | 两质点 | 无关 |
| 动能定理 | $W_{\mathrm{ext}}+W_{\mathrm{int}}=\Delta E_{\mathrm{k}}$ | 质点、质点系 | 在惯性系中成立 |
| 势能 | $-\Delta E_{\mathrm{p}}=W_{\mathrm{c,int}}$，$\boldsymbol{f}_{\mathrm{c}}=-\nabla E_{\mathrm{p}}$ | 系统 | 无关 |
| 功能原理 | $W_{\mathrm{ext}}+W_{\mathrm{nc,int}}=\Delta E$ | 系统 | 在惯性系与质心系中成立 |
| 机械能守恒 | 只有保守内力做功时 $E$ 不变 | 系统 | 是否守恒与惯性系的选择有关 |
| König 定理 | $E_{\mathrm{k}}=E_{\mathrm{k}}'+\frac12mv_C^2$ | 质点系 | 联系惯性系与质心系 |
| Bernoulli 方程 | $p+\frac12\rho v^2+\rho gh=\text{const}$ | 理想流体的稳定流动 | 流体静止的参考系 |

## 思考题

1. 功的计算是否依赖参考系？势能呢？

   **答** 功依赖参考系；势能由一对保守力的功定义，与参考系无关。

2. 机械能守恒是否与惯性系的选择有关？

   **答** 有关。例如物体在匀速运动的车厢里沿光滑斜面下滑，在车厢系中斜面支持力不做功，机械能守恒；在地面系中支持力做功，系统（物体加地球）的机械能不守恒，除非把车厢也纳入系统。

3. 摩擦生热是否与参考系有关？

   **答** 无关，它等于一对滑动摩擦力做功的负值。

4. 例 4.7.1 中，滑块上滑的过程里地面受到的压力如何变化？

   **答** 滑块有竖直向下的加速度分量（减速上升），系统的竖直方向动量在减小，所以地面支持力小于 $(m+M)g$。
