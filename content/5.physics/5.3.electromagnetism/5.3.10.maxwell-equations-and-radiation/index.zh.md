---
title: Maxwell 方程组和电磁辐射
description: 位移电流与电磁场的对称性；Maxwell 方程组的积分形式、微分形式与界面关系；电磁波方程、平面电磁波的性质、能量密度、Poynting 矢量与 Poynting 定理、动量与辐射压；振荡电偶极子的辐射；光是电磁波。
---

本章是电磁学的总结。前面九章分别建立了静**电场的高斯定理**与环路定理（[5.3.1](/5.3.1)、[5.3.2](/5.3.2)）、介质中的 $\boldsymbol{D}$ 与 $\boldsymbol{H}$（[5.3.4](/5.3.4)、[5.3.8](/5.3.8)）、磁场的通量与环路定理（[5.3.6](/5.3.6)）以及**电磁感应**定律（[5.3.9](/5.3.9)）。Maxwell 在 1865 年把它们推广到随时间变化的情形，补上关键的位移电流项，写成一组完整的方程。这组方程说明变化的电场与变化的磁场互相激发，可以脱离电荷与电流而以波的形式传播，其速度恰好等于光速。于是电、磁、光被统一在一个理论中。本章先回顾位移电流，写出 Maxwell 方程组的积分形式与微分形式（用到 [2.2.14](/2.2.14) 的**散度**、**旋度**、**Gauss 公式**与 **Stokes 公式**），然后由它导出**波动方程**（[2.5.3](/2.5.3)），讨论平面电磁波的性质、能量与动量，最后讨论振荡电偶极子怎样辐射电磁波。**机械波**的一般概念见 [5.1.7](/5.1.7)；本章的结论"光是电磁波"是波动光学（[5.4](/5.4)）的出发点。

## 10.1. 位移电流

[5.3.6](/5.3.6) 中已经看到，**恒定电流**的 **Ampère 环路定理**用于**电容器**充放电这类非恒定情形时会出现矛盾：以同一个回路为边界的两个曲面，一个被导线穿过，一个从电容器两极板之间穿过，算出的电流不同。Maxwell 的解决办法是引入**位移电流**：**电位移**通量的变化率 $I_{\mathrm{d}}=\frac{\mathrm{d}\Phi_D}{\mathrm{d}t}$，即位移电流密度

$$
\boldsymbol{J}_{\mathrm{d}}=\frac{\partial\boldsymbol{D}}{\partial t}=\varepsilon_0\frac{\partial\boldsymbol{E}}{\partial t}+\frac{\partial\boldsymbol{P}}{\partial t}.
$$
在电容器的例子中，导线中的传导电流 $I_0=\frac{\mathrm{d}q_0}{\mathrm{d}t}$，而由 $\boldsymbol{D}$ 的**高斯定理**，两极板间的位移电流 $\iint\frac{\partial\boldsymbol{D}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}=\frac{\mathrm{d}q_0}{\mathrm{d}t}$ 与它相等，传导电流与位移电流合起来的**全电流**处处连续。位移电流与传导电流一样激发磁场，但它的实质是变化的电场（第二项 $\partial\boldsymbol{P}/\partial t$ 对应介质中**束缚电荷**的微小移动），不伴随自由电荷的定向运动，不产生 Joule 热。位移电流存在于一切电场变化的地方，不限于电容器内部，同一点可以同时有传导电流与位移电流。

引入位移电流以后，电场与磁场的规律呈现出对称性。在没有传导电流的区域，

$$
\oint_L\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S},\qquad \oint_L\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\frac{\partial\boldsymbol{D}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}:
$$
变化的磁场激发**涡旋电场**，变化的电场激发涡旋磁场。两式相差一个负号，这是能量守恒的要求：若两式同号，磁场增强会产生使电场增强的感应，电场增强又产生使磁场增强的感应，能量将无中生有地增长。

## 10.2. Maxwell 方程组

### 10.2.1. 积分形式

设空间中既有自由电荷和传导电流，又有变化的电场和磁场，还有**电介质**和**磁介质**。把**静电场的环路定理**与**感生电场**的环路定理合并（总电场是两者之和），把 $\boldsymbol{D}$ 的高斯定理和**磁通连续定理**推广到变化的场，把 $\boldsymbol{H}$ 的环路定理补上位移电流，得到电磁场的基本方程。

**定理 10.2.1（Maxwell 方程组）** 对任意闭合曲面 $S$（所围体积为 $V$）和任意闭合回路 $L$（所围曲面为 $S$，法向与 $L$ 成右手螺旋关系），

$$
\begin{aligned}
&\oiint_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}=\iiint_V\rho_0\,\mathrm{d}V, &&\text{(1)}\\
&\oint_L\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}, &&\text{(2)}\\
&\oiint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=0, &&\text{(3)}\\
&\oint_L\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\Big(\boldsymbol{J}_0+\frac{\partial\boldsymbol{D}}{\partial t}\Big)\cdot\mathrm{d}\boldsymbol{S}. &&\text{(4)}
\end{aligned}
$$
其中 $\rho_0$、$\boldsymbol{J}_0$ 是自由**电荷密度**与传导**电流密度**。

四个方程分别是：电场的高斯定理（电荷是电场的源），**Faraday 电磁感应定律**（变化的磁场激发电场），磁通连续定理（没有磁荷，**磁感线**闭合），以及全电流的 Ampère 环路定理（电流与变化的电场激发磁场）。方程组对电场和磁场不完全对称，是因为自然界中没有发现单独的磁荷及相应的"磁流"。

方程组还要配上描述介质性质的物质方程。对各向同性线性介质，

$$
\boldsymbol{D}=\varepsilon\boldsymbol{E},\qquad\boldsymbol{B}=\mu\boldsymbol{H},\qquad\boldsymbol{J}_0=\sigma\boldsymbol{E},
$$
以及电磁场对电荷的作用，即 [5.3.7](/5.3.7#sec-7.2) 的 **Lorentz 力**公式 $\boldsymbol{F}=q\boldsymbol{E}+q\boldsymbol{v}\times\boldsymbol{B}$。Maxwell 方程组、物质方程与 Lorentz 力公式构成经典电动力学的完整基础，在宏观领域已被大量实验证实。在微观领域，电磁场本身也要量子化，相应的理论是量子电动力学，它的预言（如电子 $g$ 因子与 2 的偏差，[5.3.8](/5.3.8)）与实验在 $10^{-12}$ 的精度内一致。

**例 10.2.1（由 Maxwell 方程组导出电荷守恒）** 取任意闭合曲面 $S$，用一条闭合曲线 $L$ 把它分成两部分 $S_1$、$S_2$。对 $S_1$ 和 $S_2$ 分别使用方程 (4)，若两者的法向都取 $S$ 的外法向，则它们的边界 $L$ 的绕向相反，两个环量之和为零，于是

$$
\oiint_S\Big(\boldsymbol{J}_0+\frac{\partial\boldsymbol{D}}{\partial t}\Big)\cdot\mathrm{d}\boldsymbol{S}=0\quad\Longrightarrow\quad\oiint_S\boldsymbol{J}_0\cdot\mathrm{d}\boldsymbol{S}=-\frac{\mathrm{d}}{\mathrm{d}t}\oiint_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}=-\frac{\mathrm{d}}{\mathrm{d}t}\iiint_V\rho_0\,\mathrm{d}V,
$$
最后一步用了方程 (1)。这正是**电荷守恒定律**的积分形式（[5.3.5](/5.3.5) 的**电流连续性方程**）：流出闭合曲面的电流等于曲面内电荷的减少率。没有位移电流项，方程 (4) 就与电荷守恒矛盾，这是 Maxwell 引入位移电流的理论依据。

### 10.2.2. 微分形式

对方程 (2)、(4) 用 **Stokes 公式**，对 (1)、(3) 用 **Gauss 公式**（[2.2.14](/2.2.14#sec-14.2.1)、[2.2.14](/2.2.14#sec-14.3.1)），由于曲面与体积是任意的，被积函数必须相等：

**定理 10.2.2（Maxwell 方程组的微分形式）**

$$
\nabla\cdot\boldsymbol{D}=\rho_0,\qquad\nabla\times\boldsymbol{E}=-\frac{\partial\boldsymbol{B}}{\partial t},\qquad\nabla\cdot\boldsymbol{B}=0,\qquad\nabla\times\boldsymbol{H}=\boldsymbol{J}_0+\frac{\partial\boldsymbol{D}}{\partial t}.
$$

微分形式描述每一点的场与该点的源、该点场的变化率之间的关系，是一组一阶线性偏微分方程。对第四式取**散度**，由 $\nabla\cdot(\nabla\times\boldsymbol{H})=0$（[2.2.14](/2.2.14#sec-14.1.4)）和第一式，立即得到电流连续性方程 $\nabla\cdot\boldsymbol{J}_0+\partial\rho_0/\partial t=0$，这是例 10.2.1 的微分形式。

### 10.2.3. 界面关系

在两种介质的界面上，场可能不连续，微分形式不成立，要由积分形式导出界面关系（推导与 [5.3.4](/5.3.4)、[5.3.8](/5.3.8) 相同：跨越界面取扁圆柱面与扁矩形回路，令其厚度趋于零，$\partial\boldsymbol{B}/\partial t$、$\partial\boldsymbol{D}/\partial t$ 有限，它们的贡献随之趋于零）。设 $\boldsymbol{e}_{\mathrm{n}}$ 是由介质 2 指向介质 1 的单位法向矢量，$\sigma_0$、$\boldsymbol{K}_0$ 是界面上的自由电荷面密度与传导面电流密度：

$$
\boldsymbol{e}_{\mathrm{n}}\cdot(\boldsymbol{D}_1-\boldsymbol{D}_2)=\sigma_0,\qquad\boldsymbol{e}_{\mathrm{n}}\times(\boldsymbol{E}_1-\boldsymbol{E}_2)=\boldsymbol{0},\qquad\boldsymbol{e}_{\mathrm{n}}\cdot(\boldsymbol{B}_1-\boldsymbol{B}_2)=0,\qquad\boldsymbol{e}_{\mathrm{n}}\times(\boldsymbol{H}_1-\boldsymbol{H}_2)=\boldsymbol{K}_0.
$$
即 $D_{1n}-D_{2n}=\sigma_0$，$E_{1t}=E_{2t}$，$B_{1n}=B_{2n}$，$\boldsymbol{H}$ 的切向分量跃变 $\boldsymbol{K}_0$（$\boldsymbol{K}_0=\boldsymbol{0}$ 时连续）。微分方程组与界面关系一起构成完备的方程组：给定初始条件和边界条件，电磁场就被唯一确定。

## 10.3. 电磁波

### 10.3.1. 电磁波方程

考虑均匀、各向同性、线性的无限大介质中没有自由电荷和传导电流的区域（$\rho_0=0$，$\boldsymbol{J}_0=\boldsymbol{0}$）。由物质方程，Maxwell 方程组化为

$$
\nabla\times\boldsymbol{E}=-\mu\frac{\partial\boldsymbol{H}}{\partial t},\qquad\nabla\times\boldsymbol{H}=\varepsilon\frac{\partial\boldsymbol{E}}{\partial t},\qquad\nabla\cdot\boldsymbol{E}=0,\qquad\nabla\cdot\boldsymbol{H}=0,
$$
$\boldsymbol{E}$ 与 $\boldsymbol{H}$ 的地位完全对称。对第一式取**旋度**，利用矢量恒等式 $\nabla\times(\nabla\times\boldsymbol{A})=\nabla(\nabla\cdot\boldsymbol{A})-\Delta\boldsymbol{A}$（$\Delta$ 是 **Laplace 算子**，作用于各直角分量）和 $\nabla\cdot\boldsymbol{E}=0$，再代入第二式：

$$
-\Delta\boldsymbol{E}=-\mu\frac{\partial}{\partial t}(\nabla\times\boldsymbol{H})=-\varepsilon\mu\frac{\partial^2\boldsymbol{E}}{\partial t^2}.
$$
对 $\boldsymbol{H}$ 同理。

**定理 10.3.1（电磁波方程）** 在无源的均匀线性介质中，$\boldsymbol{E}$ 与 $\boldsymbol{H}$ 的每个直角分量都满足三维**波动方程**

$$
\Delta\boldsymbol{E}=\frac{1}{u^2}\frac{\partial^2\boldsymbol{E}}{\partial t^2},\qquad\Delta\boldsymbol{H}=\frac{1}{u^2}\frac{\partial^2\boldsymbol{H}}{\partial t^2},\qquad u=\frac{1}{\sqrt{\varepsilon\mu}}.
$$

所以电磁场可以以波的形式传播，这种波称为电磁波（electromagnetic wave），波速为 $u=1/\sqrt{\varepsilon\mu}$。真空中的波速

$$
c=\frac{1}{\sqrt{\varepsilon_0\mu_0}}=299\,792\,458\,\mathrm{m/s}
$$
（SI 中的定义值）。Maxwell 用当时由电学测量得到的 $\varepsilon_0\mu_0$ 算出的波速与 Fizeau 等人测得的光速相符，由此在 1865 年预言了电磁波，并断言光就是一种电磁波。1886–1888 年 Hertz 用实验产生并检测到电磁波（§10.4），证实了这一预言。

真空中的光速与介质中的波速之比称为介质的折射率（refractive index）。由波速公式，

$$
n=\frac cu=\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}\approx\sqrt{\varepsilon_{\mathrm{r}}}\qquad(\text{非铁磁质，}\mu_{\mathrm{r}}\approx1).
$$
光学中通常直接用 $n=c/u$ 作为折射率的定义（它也就是 [5.1.7](/5.1.7) **折射定律**中两种媒质波速之比的来源），而 $n=\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}$ 把这个光学常数与电学常数联系起来。式中的 $\varepsilon_{\mathrm{r}}$ 必须取对应频率下的值：水的静态**相对介电常量**约为 80，$\sqrt{80}\approx9$，而可见光的折射率只有 1.33，因为分子的**取向极化**跟不上光频的变化。$\varepsilon_{\mathrm{r}}$ 随频率变化，正是**色散**的来源。

波动方程的一般理论见 [2.5.3](/2.5.3)：三维情形的 Kirchhoff 公式说明，信号以速度 $u$ 传播且保持锐利的前沿（强形式的 **Huygens 原理**只在奇数维空间成立）。

### 10.3.2. 平面电磁波

波动方程最简单的解是沿 $x$ 方向传播的平面**简谐波**。电磁波是**横波**：对平面波 $\boldsymbol{E}=\boldsymbol{E}(x,t)$，$\nabla\cdot\boldsymbol{E}=\partial E_x/\partial x=0$，而 $\nabla\times\boldsymbol{H}=\varepsilon\partial\boldsymbol{E}/\partial t$ 的 $x$ 分量给出 $\partial E_x/\partial t=0$，所以沿传播方向没有交变分量；$\boldsymbol{H}$ 同理。取 $\boldsymbol{E}$ 沿 $y$ 方向，

$$
E_y=E_0\cos\omega\Big(t-\frac xu\Big),
$$
由 $\nabla\times\boldsymbol{E}=-\mu\partial\boldsymbol{H}/\partial t$ 的 $z$ 分量，$\frac{\partial E_y}{\partial x}=-\mu\frac{\partial H_z}{\partial t}$，积分得

$$
H_z=\sqrt{\frac\varepsilon\mu}\,E_0\cos\omega\Big(t-\frac xu\Big),
$$
而 $H_x=H_y=0$。

**性质 10.3.1（平面电磁波的性质）**

1. **横波**：$\boldsymbol{E}\perp\boldsymbol{u}$，$\boldsymbol{H}\perp\boldsymbol{u}$，且 $\boldsymbol{E}\perp\boldsymbol{H}$；$\boldsymbol{E}\times\boldsymbol{H}$ 沿传播方向，三者构成右手系。
2. $\boldsymbol{E}$ 与 $\boldsymbol{H}$ 同相位，振幅之比固定：$\sqrt\varepsilon\,E=\sqrt\mu\,H$，即 $E=uB$，真空中 $E=cB$。
3. 波速 $u=1/\sqrt{\varepsilon\mu}$，与频率无关（在 $\varepsilon$、$\mu$ 与频率无关时）。

$\boldsymbol{E}$ 保持在一个固定平面内振动的电磁波称为线偏振波；$\boldsymbol{E}$ 的方向随时间旋转的情形见 [5.4.3](/5.4.3)。

![沿 $x$ 方向传播的线偏振平面电磁波在某一时刻的波形：$\boldsymbol{E}$ 沿 $y$ 方向、$\boldsymbol{B}$ 沿 $z$ 方向振动，两者同相位，$\boldsymbol{E}\times\boldsymbol{B}$ 指向传播方向（为便于观察，$B$ 的振幅画成与 $E$ 相同）](./plots/plane-wave.py)

按波长（或频率）排列的电磁波构成电磁波谱。各波段的物理本质相同，只是波长不同，产生与探测的方法、与物质的相互作用随之不同（边界是约定的、近似的）：

| 波段 | 波长范围 | 主要来源与用途 |
|---|---|---|
| 无线电波 | $>1\,\mathrm{m}$ | 电路中的振荡电流；广播、通信 |
| 微波 | $1\,\mathrm{mm}$–$1\,\mathrm{m}$ | 雷达、移动通信、微波炉、宇宙微波背景辐射 |
| 红外线 | $760\,\mathrm{nm}$–$1\,\mathrm{mm}$ | 分子的振动与转动、热辐射；红外成像与光谱 |
| 可见光 | 约 $380$–$760\,\mathrm{nm}$ | 原子与分子中外层电子的跃迁 |
| 紫外线 | $10$–$380\,\mathrm{nm}$ | 原子的激发；消毒、光刻 |
| X 射线 | $0.01$–$10\,\mathrm{nm}$ | 内层电子跃迁、高速电子的轫致辐射（[5.5.5](/5.5.5)）；晶体衍射（[5.4.2](/5.4.2)）、医学成像 |
| $\gamma$ 射线 | $<0.01\,\mathrm{nm}$ | 原子核的跃迁、粒子湮灭 |

### 10.3.3. 电磁波的能量与 Poynting 矢量

电磁场的能量密度是**电场能量密度**与磁场能量密度（[5.3.4](/5.3.4)、[5.3.9](/5.3.9)）之和：

$$
w=w_{\mathrm{e}}+w_{\mathrm{m}}=\frac12\boldsymbol{E}\cdot\boldsymbol{D}+\frac12\boldsymbol{B}\cdot\boldsymbol{H}=\frac12\varepsilon E^2+\frac12\mu H^2.
$$
对平面电磁波，$\sqrt\varepsilon E=\sqrt\mu H$，所以 $w_{\mathrm{e}}=w_{\mathrm{m}}$，电场与磁场各占一半能量，$w=\varepsilon E^2=\sqrt{\varepsilon\mu}\,EH$。电磁波传播时，能量也随之传播。与机械波一样（[5.1.7](/5.1.7#sec-7.5.2)），单位时间内通过垂直于传播方向的单位面积的能量称为**能流密度**，其大小为 $wu=\varepsilon E^2/\sqrt{\varepsilon\mu}=EH$，方向沿传播方向，即 $\boldsymbol{E}\times\boldsymbol{H}$ 的方向。

**定义 10.3.1（Poynting 矢量）** 电磁场的能流密度矢量

$$
\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}
$$
称为 **Poynting 矢量**，单位 $\mathrm{W/m^2}$。

$\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}$ 不只对平面波成立，而是普遍的能量守恒关系的一部分：

**定理 10.3.2（Poynting 定理）** 在线性介质中，对任一闭合曲面 $S$ 所围的体积 $V$，

$$
-\frac{\mathrm{d}}{\mathrm{d}t}\iiint_Vw\,\mathrm{d}V=\oiint_S\boldsymbol{S}\cdot\mathrm{d}\boldsymbol{S}+\iiint_V\boldsymbol{J}_0\cdot\boldsymbol{E}\,\mathrm{d}V.
$$
体积内电磁能的减少率，等于通过边界流出的能量与电磁场对体积内电荷做功的功率（对**电阻**性**导体**即 Joule 热功率）之和。

**证明** 由矢量恒等式 $\nabla\cdot(\boldsymbol{E}\times\boldsymbol{H})=\boldsymbol{H}\cdot(\nabla\times\boldsymbol{E})-\boldsymbol{E}\cdot(\nabla\times\boldsymbol{H})$ 和 Maxwell 方程组的微分形式，

$$
\nabla\cdot\boldsymbol{S}=-\boldsymbol{H}\cdot\frac{\partial\boldsymbol{B}}{\partial t}-\boldsymbol{E}\cdot\frac{\partial\boldsymbol{D}}{\partial t}-\boldsymbol{E}\cdot\boldsymbol{J}_0=-\frac{\partial w}{\partial t}-\boldsymbol{J}_0\cdot\boldsymbol{E},
$$
其中用了线性介质中 $\boldsymbol{H}\cdot\partial_t\boldsymbol{B}=\partial_t(\frac12\boldsymbol{B}\cdot\boldsymbol{H})$、$\boldsymbol{E}\cdot\partial_t\boldsymbol{D}=\partial_t(\frac12\boldsymbol{E}\cdot\boldsymbol{D})$。在 $V$ 上积分并用 Gauss 公式即得。$\square$

对平面简谐波，**能流密度**在一个周期内的平均值就是**波的强度**：

$$
I=\overline S=\frac12E_0H_0=\frac12\sqrt{\frac\varepsilon\mu}\,E_0^2,\qquad\text{真空中}\quad I=\frac12c\varepsilon_0E_0^2.
$$
强度与电场振幅的平方成正比。例如地球轨道处的太阳辐照度约为 $1361\,\mathrm{W/m^2}$，相应的电场振幅 $E_0=\sqrt{2I/(c\varepsilon_0)}\approx1.0\,\mathrm{kV/m}$，磁场振幅 $B_0=E_0/c\approx3.4\,\mu\mathrm{T}$，比地磁场（约 $50\,\mu\mathrm{T}$）还小。

**例 10.3.1（导线消耗的能量从哪里来）** 一段长为 $L$、半径为 $r$、**电导率**为 $\sigma$ 的圆柱形导体通有恒定电流 $I$，求通过其侧面流入的电磁能流。

**解** 导体中的电场沿轴线，$E=J/\sigma=\frac{I}{\sigma\pi r^2}$；切向电场在界面上连续，所以导体表面外侧也有同样的轴向电场。表面处的磁场由 Ampère 环路定理得 $H=\frac{I}{2\pi r}$，沿圆周方向。$\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}$ 沿半径指向轴线，大小 $S=EH=\frac{I^2}{2\sigma\pi^2r^3}$。通过侧面流入的总功率为

$$
2\pi rL\cdot S=\frac{I^2L}{\sigma\pi r^2}=I^2R,\qquad R=\frac{L}{\sigma\pi r^2},
$$
恰好等于导体中的 Joule 热功率。能量不是在导线内部顺着电流"流"过去的，而是由场从导线外的空间输入。一般的输电线路也是这样：导线表面的电场除切向分量 $E_t$ 外还有由导线所带电荷产生的法向分量 $E_n$，$\boldsymbol{E}_n\times\boldsymbol{H}$ 平行于导线，在两根导线之间的空间中把能量由**电源**送到负载；$\boldsymbol{E}_t\times\boldsymbol{H}$ 沿半径向内，补偿导线的 Joule 热损耗。导线的作用是引导能量的流动。

### 10.3.4. 电磁波的动量与辐射压

电磁波不仅携带能量，也携带动量。由**质能关系**和光子的能量–动量关系 $p=E/c$（[5.1.8](/5.1.8#sec-8.9.4)），真空中能量密度为 $w$ 的电磁波的动量密度大小为 $w/c=S/c^2$，方向沿传播方向：

$$
\boldsymbol{g}=\frac{\boldsymbol{S}}{c^2}=\frac{\boldsymbol{E}\times\boldsymbol{H}}{c^2}.
$$
这也可以由 Maxwell 方程组与 Lorentz 力直接导出（电场使物体中的电荷振动，磁场对振动电荷的 Lorentz 力沿传播方向）。电磁波照射到物体上时，动量的转移表现为压强，称为辐射压（radiation pressure），对光也称光压。真空中强度为 $I$ 的电磁波垂直入射到物体表面，单位时间内单位面积上入射的动量为 $gc=I/c$。若完全吸收，压强为 $p_{\mathrm{r}}=I/c$；若完**全反射**，动量的变化加倍，$p_{\mathrm{r}}=2I/c$。

辐射压通常很小：地球轨道处的太阳光对全吸收表面的压强约为 $1361/(3\times10^8)\,\mathrm{Pa}\approx4.5\,\mu\mathrm{Pa}$；即使把一个 $100\,\mathrm{W}$ 灯泡的功率全部当作光，$1\,\mathrm{m}$ 外的强度也只有 $100/(4\pi)\approx8\,\mathrm{W/m^2}$，光压约 $3\times10^{-8}\,\mathrm{Pa}$。1899–1901 年 Lebedev 以及 Nichols 与 Hull 用真空中悬挂的轻小镜片的扭秤，首次测出了光压。

辐射压的效应：彗星的尘埃彗尾由太阳光的辐射压推开，总是背离太阳伸展（离子彗尾则主要由太阳风推动，更加笔直）；在大质量恒星的内部，辐射压与气体压强一起抵抗引力，它限制了恒星光度的上限（Eddington 极限），而像太阳这样的恒星主要靠气体压强支撑；太阳帆利用光压推进（日本的 IKAROS，2010 年）；激光的辐射压可以俘获和操纵微粒（光镊，Ashkin，2018 年 Nobel 物理学奖），也用于原子的激光冷却。

## 10.4. 电磁辐射

### 10.4.1. 电磁波的产生与 Hertz 实验

要产生电磁波，需要变化的电流与电荷。[5.3.9](/5.3.9) 中的 LC 回路以角频率 $\omega_0=1/\sqrt{LC}$ 振荡，但电场集中在电容器中、磁场集中在线圈中，向外辐射的能量很少。要有效地辐射，一是提高频率（辐射功率与 $\omega^4$ 成正比，见下），即减小 $L$ 与 $C$；二是使电路开放，让电场和磁场分布到周围空间中。把电容器的两极板拉开、把线圈拉直，LC 回路就逐步变为一根直导线，电流在其中往复振荡，两端的电荷交替地变号，这就是振荡电偶极子，也就是最简单的天线。

1886–1888 年，Hertz 用感应线圈激励两根带金属球的直导线（其间有小火花隙）作为振荡偶极子，在几米外用一个带火花隙的金属环检测：发射端产生火花时，接收环的间隙中也跳过微弱的火花。他测出了电磁波的驻波与波长，由已知的振荡频率算出波速等于光速，并证明电磁波与光一样能反射、折射、偏振，从而证实了 Maxwell 的理论。

### 10.4.2. 振荡电偶极子的辐射

设位于原点的电偶极子的**电偶极矩**沿 $z$ 轴作**简谐振动**，$\boldsymbol{p}=p_0\cos\omega t\,\boldsymbol{e}_z$，偶极子的长度 $l$ 远小于波长 $\lambda=2\pi c/\omega$。由 Maxwell 方程组可以解出它在周围空间产生的场（推导要用推迟势，超出本课程范围）。在 $r\gg\lambda$ 的辐射区，用球坐标 $(r,\theta,\varphi)$，$\theta$ 是场点方向与 $z$ 轴的夹角，场为

$$
\boldsymbol{E}=\frac{\ddot p(t-r/c)\sin\theta}{4\pi\varepsilon_0c^2r}\,\boldsymbol{e}_\theta,\qquad\boldsymbol{H}=\sqrt{\frac{\varepsilon_0}{\mu_0}}\,E_\theta\,\boldsymbol{e}_\varphi,\qquad\ddot p(t)=-\omega^2p_0\cos\omega t.
$$
这些表达式表明：

- 辐射场在 $t$ 时刻的值由偶极子在 $t-r/c$ 时刻的状态决定，扰动以光速向外传播。
- $\boldsymbol{E}$、$\boldsymbol{H}$ 与径向 $\boldsymbol{e}_r$ 两两垂直，同相位，$\sqrt{\varepsilon_0}E=\sqrt{\mu_0}H$：在远处的小范围内，辐射场就是沿 $\boldsymbol{e}_r$ 传播的平面电磁波（实际上是球面波）。
- **场强**与 $1/r$ 成正比，而不是像静电偶极子的场那样与 $1/r^3$ 成正比，所以辐射可以传到很远；场强与偶极矩的二阶导数成正比，只有加速运动的电荷才辐射。

相应的 Poynting 矢量为

$$
\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}=\frac{\ddot p^2\sin^2\theta}{16\pi^2\varepsilon_0c^3r^2}\,\boldsymbol{e}_r,
$$
它与 $1/r^2$ 成正比，通过任一同心球面的功率相同，能量确实被辐射出去了。辐射关于偶极子的轴旋转对称：在垂直于轴的方向（$\theta=90^\circ$）最强，沿轴线方向为零。对整个球面积分（$\int_0^\pi\sin^3\theta\,\mathrm{d}\theta=\frac43$），辐射功率为

$$
P=\frac{\ddot p^2}{6\pi\varepsilon_0c^3},\qquad\overline P=\frac{p_0^2\omega^4}{12\pi\varepsilon_0c^3}.
$$

![左：振荡电偶极子（中心的短线）在某一时刻的电场线。近处的电场线连接偶极子的两端，与静电偶极子相似；电场线随振荡断开、形成闭合的环，脱离偶极子以光速向外传播；右：辐射强度的角分布 $\sin^2\theta$，$\theta$ 从偶极子的轴（图中竖直方向）量起](./plots/dipole-radiation.py)

**注 10.4.1（加速电荷的辐射）** 单个**点电荷** $q$ 以加速度 $a$（$v\ll c$）运动时，$\ddot p=qa$，辐射功率为

$$
P=\frac{q^2a^2}{6\pi\varepsilon_0c^3}\qquad(\text{Larmor 公式}).
$$
这一结果有许多重要推论。平均辐射功率与 $\omega^4$ 成正比，这是天空呈蓝色的原因：大气分子在太阳光的电场中做**受迫振动**而向四面散射，短波长的蓝光散射得最强（Rayleigh 散射，[5.4.3](/5.4.3)）。高速电子在原子核附近急剧减速时发出连续的 X 射线（轫致辐射，[5.5.5](/5.5.5)）；在环形加速器中做圆周运动的高能电子沿切线方向发出极强的同步辐射，现已成为研究物质结构的重要光源。按经典理论，绕核旋转的电子有**向心加速度**，会不断辐射而在约 $10^{-11}\,\mathrm{s}$ 内落入原子核，这与原子的稳定性矛盾，是经典物理在原子尺度上失效的标志之一（[5.5.4](/5.5.4)）。

### 10.4.3. 光是电磁波

Maxwell 理论的一个最重要的推论是：光是波长在约 $380$–$760\,\mathrm{nm}$ 之间的电磁波。由此，波动光学中的许多量都有了电磁学的意义：

- 光速 $c=1/\sqrt{\varepsilon_0\mu_0}$，介质的折射率 $n=\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}$。
- 光波中对人眼、感光乳剂和光电探测器起作用的主要是电场（磁场对电荷的作用力比电场力小 $v/c$ 倍），所以光波中的 $\boldsymbol{E}$ 称为光矢量，光的振动方向指 $\boldsymbol{E}$ 的方向。
- 光的强度是平均能流密度，与光矢量振幅的平方成正比，$I\propto E_0^2$。在波动光学中只需比较相对强度，常直接写成 $I=E_0^2$。
- 光是横波，因此有偏振现象（[5.4.3](/5.4.3)）。

两列光波在空间相遇时，由于 Maxwell 方程组是线性的，合成的光矢量是各光矢量之和（**叠加原理**），而强度是合振幅的平方，这就是光的**干涉**（[5.4.1](/5.4.1)）与**衍射**（[5.4.2](/5.4.2)）的基础。另一方面，在光电效应和黑体辐射中，光又表现出粒子性，经典的电磁理论无法解释，这引出了光的量子理论（[5.5.1](/5.5.1)）。

## 小结

| 方程 | 积分形式 | 微分形式 | 物理意义 |
|---|---|---|---|
| (1) | $\oiint\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}=q_0$ | $\nabla\cdot\boldsymbol{D}=\rho_0$ | 电荷激发电场 |
| (2) | $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=-\iint\partial_t\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}$ | $\nabla\times\boldsymbol{E}=-\partial_t\boldsymbol{B}$ | 变化的磁场激发电场 |
| (3) | $\oiint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=0$ | $\nabla\cdot\boldsymbol{B}=0$ | 没有磁荷 |
| (4) | $\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=I_0+\iint\partial_t\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}$ | $\nabla\times\boldsymbol{H}=\boldsymbol{J}_0+\partial_t\boldsymbol{D}$ | 电流和变化的电场激发磁场 |

- 无源区中 $\boldsymbol{E}$、$\boldsymbol{H}$ 满足波动方程，波速 $u=1/\sqrt{\varepsilon\mu}$，真空中为 $c$。平面电磁波是横波，$\boldsymbol{E}$、$\boldsymbol{H}$ 同相，$\boldsymbol{E}\times\boldsymbol{H}$ 沿传播方向，$E=uB$。
- 能量密度 $w=\frac12(\boldsymbol{E}\cdot\boldsymbol{D}+\boldsymbol{B}\cdot\boldsymbol{H})$，Poynting 矢量 $\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}$，强度 $I=\frac12\sqrt{\varepsilon/\mu}\,E_0^2$；动量密度 $\boldsymbol{S}/c^2$，辐射压 $I/c$（吸收）或 $2I/c$（反射）。
- 加速运动的电荷辐射电磁波；振荡电偶极子的辐射场与 $1/r$ 成正比，强度按 $\sin^2\theta$ 分布，总功率与 $\omega^4$ 成正比。

## 思考题

1. 平行板电容器充电时，两极板之间的位移电流与导线中的传导电流相等。极板间的磁场与导线周围的磁场有什么不同？
   提示：由全电流环路定理，对圆形极板，板间的磁场沿圆周方向，在半径 $r$（小于极板半径 $R$）处与 $r$ 成正比，在 $r>R$ 处与导线周围的磁场相同，都是 $\frac{\mu_0I}{2\pi r}$。
2. 电容器充电时，能量是怎样进入电容器的？
   提示：板间的电场沿轴向增大，边缘处的磁场沿圆周方向，Poynting 矢量从侧面沿半径指向电容器内部，流入的功率等于电场能量的增加率。
3. 为什么无线电广播的天线高高竖起，而收音机里的磁性天线（绕在磁棒上的线圈）却很小？
   提示：发射天线要有效地辐射，尺度要与波长可比；接收天线只需感应电磁波的磁场，磁棒的高**磁导率**集中了磁通，提高了感应**电动势**。
4. 为什么静止的电荷与匀速运动的电荷都不辐射电磁波？
   提示：辐射场与加速度成正比。匀速运动的电荷换到它的静止参考系中只有静电场，不会有向外流出的能流。
