---
title: 振动
description: 简谐振动的定义、判据、特征量与旋转矢量表示，稳定平衡附近的微振动，简谐振动的合成（拍、Lissajous 图形、耦合振子的简正模式），谐振分析与频谱，阻尼振动与品质因数，受迫振动与共振。
---

物理量在某一数值附近往复变化的过程称为振动。振动不限于机械运动：交流电路中的电流、电磁波中的电场、分子中原子的位置都在振动，它们满足同样形式的方程。按受力情况，振动可分为无阻尼自由振动、阻尼自由振动与受迫振动；其中最简单、最基本的是无阻尼自由振动中的简谐振动，它是本章的重点：一方面，许多实际的小幅振动都可以看作简谐振动；另一方面，任何复杂的振动都可以分解为简谐振动的叠加。

数学上，本章的方程都是二阶常系数**线性微分方程**，其解法已在 [2.2.16](/2.2.16#sec-16.5) 的"振动问题"一节与 [2.4.9](/2.4.9) 中讲过，这里不再重复推导，而着重物理图像：用**复数**与旋转矢量表示振动、用能量判断振动的性质、用频率响应理解共振。耦合振动的简正模式是线性代数中**特征值**问题的直接应用，谐振分析就是 **Fourier 级数**。上一章的**势能曲线**（[5.1.4](/5.1.4)）告诉我们稳定平衡附近为什么会振动；下一章 [5.1.7](/5.1.7) 研究振动在空间中的传播，即波动。

## 6.1. 简谐振动

### 6.1.1. 简谐振动的定义

**定义 6.1.1（简谐振动）** 物理量 $x$ 随时间按余弦（或正弦）规律变化的过程

$$
x=A\cos(\omega t+\varphi_0)
$$
称为**简谐振动**，其中 $A>0$ 为**振幅**，$\omega$ 为**角频率**，$\omega t+\varphi_0$ 为**相位**，$\varphi_0$ 为**初相**。

$x$ 可以是**位移**、角度，也可以是电流、电场强度、温度等。简谐振动是理想化的模型，它是研究复杂振动的基础。

### 6.1.2. 简谐振动的判据

对机械振动，下面三条中任何一条成立，即可判定为简谐振动：

1. 受力特征：**质点**所受的合力与相对平衡位置的位移成正比、方向相反，
   $$
   F=-kx,
   $$
   这样的力称为线性回复力（弹性力或准弹性力），$k$ 为劲度系数（刚度系数）。
2. 运动方程：
   $$
   \frac{\mathrm{d}^2x}{\mathrm{d}t^2}+\omega^2x=0,
   $$
   其通解正是 $x=A\cos(\omega t+\varphi_0)$。
3. 能量特征：回复力是**保守力**，以平衡位置为**势能**零点，$E_{\mathrm{p}}=\frac12kx^2$，系统的**机械能**守恒，
   $$
   E=\frac12mv^2+\frac12kx^2=\frac12kA^2=\text{const}.
   $$
   **动能**与势能不断相互转化，在一个周期内的平均值相等：$\bar E_{\mathrm{k}}=\bar E_{\mathrm{p}}=\frac14kA^2$。

由 1 与 **Newton 第二定律** 得 2（$\omega^2=k/m$）；对 3 求导，$mv\dot v+kxv=0$，即 $m\ddot x+kx=0$，也得到 2。

### 6.1.3. 简谐振动的特征量

1. 角频率 $\omega=\sqrt{k/m}$，只由系统本身决定，也称固有角频率。频率 $\nu=\dfrac{\omega}{2\pi}$，周期 $T=\dfrac1\nu=\dfrac{2\pi}{\omega}$，单位分别为 $\mathrm{rad\,s^{-1}}$、$\mathrm{Hz}$、$\mathrm{s}$。
2. 振幅 $A$ 由初始条件 $x_0$、$v_0$ 与系统本身决定：
   $$
   A=\sqrt{x_0^2+\frac{v_0^2}{\omega^2}}=\sqrt{\frac{2E}{k}} .
   $$
3. 初相 $\varphi_0$ 也由初始条件与系统本身决定：由 $x_0=A\cos\varphi_0$、$v_0=-A\omega\sin\varphi_0$，
   $$
   \tan\varphi_0=-\frac{v_0}{\omega x_0},
   $$
   再由 $x_0$、$v_0$ 的正负确定 $\varphi_0$ 所在的象限（一般取 $(-\pi,\pi]$ 内的值）。

### 6.1.4. 简谐振动的表示法

给定振幅 $A$、角频率 $\omega$ 与初相 $\varphi_0$，就确定了一个简谐振动。

用振动函数表示，位移、**速度**、**加速度**为

$$
x=A\cos(\omega t+\varphi_0),\quad
v=\frac{\mathrm{d}x}{\mathrm{d}t}=\omega A\cos\Big(\omega t+\varphi_0+\frac\pi2\Big),\quad
a=\frac{\mathrm{d}^2x}{\mathrm{d}t^2}=\omega^2A\cos(\omega t+\varphi_0+\pi),
$$
速度的相位比位移超前 $\pi/2$，加速度与位移反相，$a=-\omega^2x$。

以 $t$ 为横坐标、$x$ 为纵坐标画出的振动曲线是一条余弦曲线，周期 $T$，在 $t=0$ 处的值为 $A\cos\varphi_0$。

更直观的是旋转矢量表示法：在 $x$ 轴所在平面内，以原点为起点作长为 $A$ 的矢量 $\boldsymbol{A}$，令它以**角速度** $\omega$ 逆时针匀速旋转，$t=0$ 时与 $x$ 轴的夹角为 $\varphi_0$。矢量端点在 $x$ 轴上的投影就是 $x=A\cos(\omega t+\varphi_0)$，端点画出的圆称为参考圆。这个旋转矢量（phasor）就是复数 $\tilde x=A\mathrm{e}^{\mathrm{i}(\omega t+\varphi_0)}$ 在复平面上的图像，$x=\operatorname{Re}\tilde x$：由 [Euler 公式](/2.1.9)，振幅与初相合成一个复振幅 $A\mathrm{e}^{\mathrm{i}\varphi_0}$（**复数的极形式**），求导就是乘以 $\mathrm{i}\omega$，即旋转矢量逆时针转过 $\pi/2$ 并伸长 $\omega$ 倍。用旋转矢量确定初相、研究振动的合成都很方便。

**例 6.1.1** 已知 $x_0=A/2$，求 $v_0<0$ 与 $v_0>0$ 两种情况下的初相。

**解** $\cos\varphi_0=\frac12$，$\varphi_0=\pm\frac\pi3$。在参考圆上，$t=0$ 时旋转矢量端点的投影在 $A/2$ 处；端点在上半圆时投影向左移动，$v_0<0$，所以 $v_0<0$ 时 $\varphi_0=\frac\pi3$，$v_0>0$ 时 $\varphi_0=-\frac\pi3$。

**例 6.1.2** U 形管内液体的质量为 $m$、密度为 $\rho$，管的截面积为 $S$。开始时使两边液面有一定高度差，忽略管壁与液体间的摩擦，判断液柱振动的性质。

**解** 方法一（受力）：设一侧液面相对平衡位置升高 $y$，另一侧降低 $y$，两侧液面高度差 $2y$ 的液柱的重力就是回复力，
$$
F=-2\rho gSy=-ky,\qquad k=2\rho gS=\text{const},
$$
所以是简谐振动，$\omega=\sqrt{k/m}=\sqrt{2\rho gS/m}$。

方法二（能量）：相对平衡位置，相当于把高 $y$、质量 $\rho Sy$ 的一段液柱从一侧移到另一侧并升高 $y$，势能 $E_{\mathrm{p}}=\rho gSy\cdot y=\frac12ky^2$，$k=2\rho gS$；无损耗，机械能守恒，所以是简谐振动，角频率同上。若液柱总长为 $l$，$m=\rho Sl$，则 $\omega=\sqrt{2g/l}$，与液体的密度和管的粗细无关。

### 6.1.5. 稳定平衡位置附近的微振动

**例 6.1.3** 证明稳定平衡位置附近的微振动是简谐振动。

**证明** 设一维保守系统的稳定平衡位置为 $x=0$，则 $E_{\mathrm{p}}'(0)=0$，$E_{\mathrm{p}}''(0)>0$。把势能在 $x=0$ 附近展开为 **Taylor 级数**，对微振动只保留到 $x^2$ 项，并取 $E_{\mathrm{p}}(0)=0$：

$$
E_{\mathrm{p}}(x)\approx\frac12E_{\mathrm{p}}''(0)\,x^2=\frac12kx^2,\qquad k=E_{\mathrm{p}}''(0)>0,
$$
于是 $f=-\dfrac{\mathrm{d}E_{\mathrm{p}}}{\mathrm{d}x}=-kx$，是线性回复力。$\square$

这就是在**平衡点**处把方程线性化（[2.4.11](/2.4.11)）。原子与分子的振动（[例 4.6.2](/5.1.4#ex-4.6.2) 的势能曲线在极小点附近近似为抛物线）、固体中的晶格振动都是这样的微振动。

**注 6.1.1（单摆的大角度振动）** 单摆的方程 $\ddot\theta+\frac gl\sin\theta=0$ 是非线性的，只有在 $\sin\theta\approx\theta$ 时才是简谐振动，周期 $T_0=2\pi\sqrt{l/g}$。以振幅 $\theta_0$ 摆动时，由能量守恒可以求出精确的周期

$$
T=4\sqrt{\frac lg}\,K\Big(\sin\frac{\theta_0}{2}\Big)\approx T_0\Big(1+\frac{\theta_0^2}{16}\Big),
$$
其中 $K(k)=\int_0^{\pi/2}\frac{\mathrm{d}\phi}{\sqrt{1-k^2\sin^2\phi}}$ 是第一类完全椭圆积分。$\theta_0=10^\circ$ 时 $T/T_0=1.0019$，$30^\circ$ 时 $1.0174$，$90^\circ$ 时 $1.1803$：摆角不大时周期几乎与振幅无关（等时性），振幅大了周期变长。这个结果也可以用 [4.4.4](/4.4.4#sec-4.3.2) 中的 `solve_ivp` 数值求解方程验证：

```python
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipk

theta0 = np.radians(90)


def crossing(t, y):  # pendulum passes theta = 0 after a quarter period
    return y[0]


crossing.terminal, crossing.direction = True, -1
sol = solve_ivp(lambda t, y: [y[1], -np.sin(y[0])], (0, 50), [theta0, 0],
                events=crossing, rtol=1e-10, atol=1e-12)  # g / l = 1
print(4 * sol.t_events[0][0] / (2 * np.pi))          # T / T0 from the ODE
print(2 / np.pi * ellipk(np.sin(theta0 / 2) ** 2))  # SciPy uses the parameter k^2
```

```text
1.18034059902613
1.1803405990160962
```

## 6.2. 简谐振动的合成

### 6.2.1. 同方向、同频率的简谐振动的合成

设 $x_1=A_1\cos(\omega t+\varphi_1)$，$x_2=A_2\cos(\omega t+\varphi_2)$。两个旋转矢量以相同的角速度旋转，夹角不变，它们的矢量和也以 $\omega$ 旋转，所以合振动 $x=x_1+x_2=A\cos(\omega t+\varphi)$ 仍是同频率的简谐振动，由平行四边形法则（或复振幅相加 $A\mathrm{e}^{\mathrm{i}\varphi}=A_1\mathrm{e}^{\mathrm{i}\varphi_1}+A_2\mathrm{e}^{\mathrm{i}\varphi_2}$），

$$
A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos(\varphi_2-\varphi_1)},\qquad
\tan\varphi=\frac{A_1\sin\varphi_1+A_2\sin\varphi_2}{A_1\cos\varphi_1+A_2\cos\varphi_2}.
$$
重要的特例：

- 同相，$\varphi_2-\varphi_1=2k\pi$（$k\in\mathbb{Z}$）：$A=A_1+A_2$，合振幅最大；
- 反相，$\varphi_2-\varphi_1=(2k+1)\pi$：$A=\lvert A_1-A_2\rvert$，合振幅最小。

再看 $n$ 个等幅、初相依次相差 $\delta$ 的简谐振动的合成。设 $x_j=a\cos\big(\omega t+(j-1)\delta\big)$，$j=1,\dots,n$。复振幅之和是等比数列

$$
a\sum_{j=0}^{n-1}\mathrm{e}^{\mathrm{i}j\delta}=a\frac{\mathrm{e}^{\mathrm{i}n\delta}-1}{\mathrm{e}^{\mathrm{i}\delta}-1}=a\frac{\sin(n\delta/2)}{\sin(\delta/2)}\mathrm{e}^{\mathrm{i}(n-1)\delta/2},
$$
所以合振动 $x=A\cos(\omega t+\varphi)$，

$$
A=a\frac{\sin(n\delta/2)}{\sin(\delta/2)},\qquad \varphi=\frac{n-1}{2}\delta .
$$
几何上，$n$ 个旋转矢量首尾相接构成正多边形的一部分。

- $\delta=2k\pi$（$k\in\mathbb{Z}$）：各分振动同相，$A=na$，最大；
- $\delta=2k\pi/n$，$k$ 不是 $n$ 的整数倍：$A=0$，分振幅矢量构成封闭的多边形。例如 $n=4$ 时，$\delta=\pm\frac\pi2,\pm\pi,\pm\frac{3\pi}2,\dots$ 都使合振幅为零。

这个结果是光栅衍射（[5.4.2](/5.4.2)）中多缝干涉强度分布的基础。

### 6.2.2. 同方向、不同频率的简谐振动的合成与拍

为简单起见，设两个振动振幅相同、初相相同：$x_1=A\cos(\omega_1t+\varphi_0)$，$x_2=A\cos(\omega_2t+\varphi_0)$。由和差化积，

$$
x=x_1+x_2=2A\cos\Big(\frac{\omega_2-\omega_1}{2}t\Big)\cos\Big(\frac{\omega_2+\omega_1}{2}t+\varphi_0\Big),
$$
合振动不再是简谐振动。若 $\omega_1$、$\omega_2$ 都较大而差值很小，第一个因子变化缓慢、第二个因子变化很快，合振动可以看作角频率为 $\frac{\omega_1+\omega_2}{2}$、振幅 $\big\lvert2A\cos\frac{\omega_2-\omega_1}{2}t\big\rvert$ 缓慢变化的振动：合振动时强时弱，这种现象称为拍（beat）。

用旋转矢量看，两个旋转矢量的夹角以 $\lvert\omega_1-\omega_2\rvert$ 的角速度缓慢变化：同向重合时 $A_{\max}=A_1+A_2$，反向重合时 $A_{\min}=\lvert A_1-A_2\rvert$。合振幅变化的频率称为拍频，

$$
\nu_{\mathrm{beat}}=\lvert\nu_1-\nu_2\rvert .
$$
两个频率相近的音叉同时发声，就能听到响度周期性起伏的拍音。拍可以用来测量频率（如调音时使拍音消失），也可以由两个高频振动得到低频的振动。

![Beats: two oscillations of equal amplitude with nearby frequencies nu1 = 10 Hz and nu2 = 11 Hz (top) and their sum (bottom), whose amplitude 2A|cos((omega2 - omega1) t / 2)| (dashed envelope) varies with the beat frequency |nu1 - nu2| = 1 Hz](./plots/beats.py)

**例 6.2.1（耦合摆与简正模式）** 两个相同的单摆（质量 $m$、摆长 $l$，$\omega_0^2=g/l$）用一根劲度系数为 $k$ 的轻弹簧相连，小振动时两摆的水平位移 $x_1$、$x_2$ 满足

$$
\ddot x_1=-\omega_0^2x_1-\kappa(x_1-x_2),\qquad \ddot x_2=-\omega_0^2x_2-\kappa(x_2-x_1),\qquad \kappa=\frac km,
$$
即 $\ddot{\boldsymbol{x}}=-K\boldsymbol{x}$，$K=\begin{bmatrix}\omega_0^2+\kappa&-\kappa\\-\kappa&\omega_0^2+\kappa\end{bmatrix}$。$K$ 是实**对称矩阵**，它的**特征值**与特征向量为

$$
\omega_1^2=\omega_0^2,\ \ \boldsymbol{u}_1=\begin{bmatrix}1\\1\end{bmatrix};\qquad
\omega_2^2=\omega_0^2+2\kappa,\ \ \boldsymbol{u}_2=\begin{bmatrix}1\\-1\end{bmatrix}.
$$
在特征向量组成的坐标 $q_1=\frac12(x_1+x_2)$、$q_2=\frac12(x_1-x_2)$ 下方程解耦为两个独立的简谐振动：两摆同相摆动时弹簧不伸缩，频率为 $\omega_1$；两摆反相摆动时弹簧伸缩，频率为 $\omega_2$。这两种每个部分以同一频率振动的方式称为简正模式，一般的运动是它们的叠加。若开始时只拉开第一个摆（$x_1=A$，$x_2=0$，均静止），则

$$
x_1=A\cos\frac{\omega_2-\omega_1}{2}t\,\cos\frac{\omega_2+\omega_1}{2}t,\qquad
x_2=A\sin\frac{\omega_2-\omega_1}{2}t\,\sin\frac{\omega_2+\omega_1}{2}t .
$$
弱耦合（$\kappa\ll\omega_0^2$）时两摆各自出现拍，能量在两摆之间往复传递，每隔 $\pi/(\omega_2-\omega_1)$ 完全转移一次：演示中的"共振耦合摆"就是这个现象。$n$ 个耦合振子有 $n$ 个简正模式，连续介质（弦、空气柱）的简正模式就是驻波（[5.1.7](/5.1.7)）。

### 6.2.3. 互相垂直、同频率的简谐振动的合成

质点同时参与 $x=A_x\cos(\omega t+\varphi_x)$ 与 $y=A_y\cos(\omega t+\varphi_y)$ 两个振动。消去 $t$ 得轨迹方程

$$
\frac{x^2}{A_x^2}+\frac{y^2}{A_y^2}-\frac{2xy}{A_xA_y}\cos(\varphi_y-\varphi_x)=\sin^2(\varphi_y-\varphi_x).
$$
记 $\Delta\varphi=\varphi_y-\varphi_x$：

- $\Delta\varphi=0$ 或 $\pi$：轨迹是过原点的直线段，合振动是直线振动；
- $\Delta\varphi=\pm\frac\pi2$：轨迹是以坐标轴为主轴的正椭圆，$A_x=A_y$ 时为圆；
- 一般情况下轨迹是斜椭圆。

旋转方向由 $\Delta\varphi$ 决定（取 $\Delta\varphi\in(-\pi,\pi]$）：$0<\Delta\varphi<\pi$ 时 $y$ 的相位超前，质点沿顺时针方向运动（右旋）；$-\pi<\Delta\varphi<0$ 时 $x$ 的相位超前，沿逆时针方向运动（左旋）。例如 $\Delta\varphi=\frac\pi2$，$x=A\cos\omega t$，$y=-A\sin\omega t$，在 $t=0$ 时位于 $(A,0)$、向 $-y$ 方向运动，是顺时针。反过来，任一圆周运动或椭圆运动都可以分解为两个互相垂直的同频率简谐振动；这正是光的偏振（[5.4.3](/5.4.3)）中线偏振、圆偏振与椭圆偏振的描述方式。

### 6.2.4. 互相垂直、不同频率的简谐振动的合成

若两个频率之比为简单的整数比，$\omega_x:\omega_y=m:n$，合成轨迹是稳定的闭合曲线，称为 Lissajous 图形（Lissajous figure）。在一个完整的图形周期内，$x$ 达到最大值的次数与 $y$ 达到最大值的次数之比等于频率之比：设图形与直线 $x=A_x$ 有 $N_x$ 个切点，与直线 $y=A_y$ 有 $N_y$ 个切点，则

$$
\frac{\omega_x}{\omega_y}=\frac{N_x}{N_y}.
$$
用示波器观察已知频率与未知频率合成的 Lissajous 图形，可以测定未知频率。图形的形状还与初相差有关。

若频率之比为无理数，轨迹不闭合，经过足够长的时间后几乎布满整个矩形 $\lvert x\rvert\le A_x$，$\lvert y\rvert\le A_y$。

两个频率接近、本来独立的振动之间若存在弱的物理耦合，频率比可能被"拉"到附近的简单整数比并保持锁定，称为锁频（frequency locking），也称同步。Huygens 在 1665 年发现挂在同一横梁上的两个摆钟会逐渐同步；生物钟被昼夜节律"牵引"到 24 小时，也是锁频的例子。

![Lissajous figures x = cos(m t), y = cos(n t + phi) for frequency ratios 1:1, 1:2 and 2:3 (rows) and phase differences 0, pi/4 and pi/2 (columns)](./plots/lissajous.py)

| 振动方向 | 频率相同 | 频率不同 |
|---|---|---|
| 相同 | 矢量合成：频率不变，振幅与相位改变 | 频率相近时出现拍 |
| 互相垂直 | 直线、圆或椭圆 | 整数比时为 Lissajous 图形；无理数比时轨迹不闭合 |

## 6.3. 谐振分析

简谐振动可以合成复杂的振动；反过来，复杂的振动也可以分解为一系列简谐振动的叠加，这称为谐振分析（Fourier 分析）。周期为 $T$ 的振动 $x(t)$（满足 Dirichlet 条件，[定理 9.3.1](/2.2.9#thm-9.3.1)）可以展开为 **Fourier 级数**

$$
x(t)=\frac{a_0}{2}+\sum_{k=1}^{\infty}A_k\cos(k\omega t+\varphi_k),\qquad \omega=\frac{2\pi}{T}.
$$

- $k=1$ 的分量称为基频（基音），频率 $\nu=1/T$ 等于原振动的频率，决定音调；
- $k=2,3,\dots$ 的分量称为二次、三次……谐频（泛音），各次谐频的相对强弱决定音色。

以 $k\omega$ 为横坐标、$A_k$ 为纵坐标作图得到振动的频谱。周期振动的频谱是分立谱。例如对称方波（一个周期内一半时间为 $+1$、一半时间为 $-1$）只含奇次谐频，

$$
x(t)=\frac4\pi\Big(\cos\omega t-\frac13\cos3\omega t+\frac15\cos5\omega t-\cdots\Big),
$$
$A_{2n}=0$；取前几项的部分和就能逼近方波，在间断点附近始终有约 $9\%$ 的过冲（**Gibbs 现象**）。

![Fourier synthesis of a square wave: partial sums with the first one, two, three and twenty odd harmonics (left) and its discrete amplitude spectrum A_k = 4/(pi k) for odd k (right)](./plots/square-wave-fourier.py)

非周期的振动（如一次敲击的声音）可以看作周期趋于无穷，频谱变为连续谱，由 **Fourier 变换**（[2.5.6](/2.5.6)）给出。实际测得的离散信号用**快速 Fourier 变换**计算频谱（[4.4.4](/4.4.4#sec-4.7)）。称赞歌唱家"声音洪亮、音域宽广、音色甜美"，分别对应振幅（声强）大、基频的变化范围宽、谐频成分悦耳。

## 6.4. 阻尼振动

实际的振动系统总要克服阻力做**功**，能量逐渐减少，振幅逐渐衰减，这种振动称为阻尼振动（damped oscillation）。速度不大时介质阻力与速度成正比，$f=-\gamma\dot x$，方程为

$$
m\frac{\mathrm{d}^2x}{\mathrm{d}t^2}=-kx-\gamma\frac{\mathrm{d}x}{\mathrm{d}t},
$$
即

$$
\ddot x+2\beta\dot x+\omega_0^2x=0,\qquad \omega_0=\sqrt{\frac km},\quad \beta=\frac{\gamma}{2m},
$$
$\omega_0$ 是固有角频率，$\beta$ 称为阻尼系数。这就是 [2.2.16](/2.2.16#sec-16.5.1) 中的方程 $x''+2kx'+\omega^2x=0$（那里的 $k$、$\omega$ 对应这里的 $\beta$、$\omega_0$），三种情形的解与图像见该节：

1. 欠阻尼（$\beta<\omega_0$）：
   $$
   x=A_0\mathrm{e}^{-\beta t}\cos(\omega_{\mathrm{d}}t+\varphi_0),\qquad \omega_{\mathrm{d}}=\sqrt{\omega_0^2-\beta^2},
   $$
   $\mathrm{e}^{-\beta t}$ 是衰减因子。这是振幅按指数衰减的准周期运动，周期 $T_{\mathrm{d}}=2\pi/\omega_{\mathrm{d}}$ 比系统的固有周期长：阻力使质点每次回到平衡位置都更慢一些。
2. 过阻尼（$\beta>\omega_0$）：非周期运动，质点缓慢地回到平衡位置。
3. 临界阻尼（$\beta=\omega_0$）：刚好不再振动，在非周期运动中回到平衡位置所需的时间最短。电表指针、天平、汽车减振器都设计在临界阻尼附近，使指针或车身迅速停稳而不来回摆动。

弱阻尼（$\beta\ll\omega_0$）时，振幅 $A=A_0\mathrm{e}^{-\beta t}$，能量 $E\propto A^2$，

$$
E=E_0\mathrm{e}^{-2\beta t}.
$$
能量减少到初始值的 $1/\mathrm{e}$ 所用的时间 $\tau=\dfrac1{2\beta}$ 称为鸣响时间。在 $\tau$ 内振动的次数越多，振动的"质量"越好。

**定义 6.4.1（品质因数）** 弱阻尼振动的**品质因数**为

$$
Q=2\pi\frac{\tau}{T}=\omega_0\tau=\frac{\omega_0}{2\beta},
$$
其中 $T$、$\omega_0$ 取系统的固有周期与固有角频率。等价地，$Q$ 等于 $2\pi$ 乘以系统储存的能量与每个周期损失的能量之比。

$Q$ 是**量纲**一的量。典型数值：无线电 $LC$ 振荡回路 $Q\sim10^2$，音叉、钢琴弦 $Q\sim10^3$，石英晶体振子 $Q\sim10^5$，激光器的光学谐振腔可达 $10^7$ 以上。

## 6.5. 受迫振动

### 6.5.1. 振动方程与稳态解

系统在周期性外力（驱动力）$F_0\cos\omega t$ 作用下的振动称为受迫振动（forced oscillation）。方程为

$$
m\frac{\mathrm{d}^2x}{\mathrm{d}t^2}=-kx-\gamma\frac{\mathrm{d}x}{\mathrm{d}t}+F_0\cos\omega t,\qquad \ddot x+2\beta\dot x+\omega_0^2x=\frac{F_0}{m}\cos\omega t .
$$
其通解是齐次方程的通解（阻尼振动）与一个特解之和（[2.2.16](/2.2.16#sec-16.5.2)）。阻尼振动部分随时间衰减，是暂态解；经过足够长时间后只剩下稳态解

$$
x=A\cos(\omega t+\varphi_0),\qquad
A=\frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+4\beta^2\omega^2}},\qquad
\tan\varphi_0=-\frac{2\beta\omega}{\omega_0^2-\omega^2},\quad -\pi<\varphi_0<0 .
$$
用复数求特解最简单：设 $\tilde x=\tilde A\mathrm{e}^{\mathrm{i}\omega t}$ 满足 $\ddot{\tilde x}+2\beta\dot{\tilde x}+\omega_0^2\tilde x=\frac{F_0}m\mathrm{e}^{\mathrm{i}\omega t}$，则 $\tilde A=\dfrac{F_0/m}{\omega_0^2-\omega^2+2\mathrm{i}\beta\omega}$，$A=\lvert\tilde A\rvert$，$\varphi_0=\arg\tilde A$。

稳态解在形式上与简谐振动相似，但不是一回事：

- 系统振动的频率等于驱动力的频率 $\omega$，而不是固有频率 $\omega_0$；
- $A$ 与 $\varphi_0$ 是 $F_0/m$、$\omega$、$\omega_0$、$\beta$ 的函数，与初始状态 $x_0$、$v_0$ 无关；
- $\varphi_0$ 是位移落后于驱动力的相位：$\omega\ll\omega_0$ 时 $\varphi_0\approx0$，位移与驱动力同相；$\omega=\omega_0$ 时 $\varphi_0=-\frac\pi2$；$\omega\gg\omega_0$ 时 $\varphi_0\to-\pi$，位移与驱动力反相。

### 6.5.2. 共振

驱动力的频率接近系统的固有频率时，受迫振动的振幅急剧增大，这一现象称为**共振**。

- 位移共振：$A(\omega)$ 在 $\omega_{\mathrm{r}}=\sqrt{\omega_0^2-2\beta^2}$ 处（$\beta<\omega_0/\sqrt2$ 时）取最大值 $A_{\mathrm{r}}=\dfrac{F_0}{2m\beta\sqrt{\omega_0^2-\beta^2}}$。阻尼越小，共振峰越高越尖，$\omega_{\mathrm{r}}$ 越接近 $\omega_0$。
- 速度共振：速度振幅 $v_{\mathrm{m}}=\omega A=\dfrac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2/\omega^2+4\beta^2}}$ 恰在 $\omega=\omega_0$ 处取最大值 $\dfrac{F_0}{2m\beta}$，与阻尼大小无关。

在 $\omega=\omega_0$ 处 $\varphi_0=-\frac\pi2$，

$$
v=\frac{\mathrm{d}x}{\mathrm{d}t}=\omega A\cos\Big(\omega t+\varphi_0+\frac\pi2\Big)=\omega A\cos\omega t,
$$
速度与驱动力同相，驱动力始终做正功，系统最大限度地从外界吸收能量。一般地，驱动力的平均**功率** $\bar P=\frac12F_0v_{\mathrm{m}}\cos(\varphi_0+\frac\pi2)$ 在 $\omega_0$ 处最大；弱阻尼时 $\bar P$ 降到峰值一半的两个频率之差（共振峰的宽度）为 $\Delta\omega=2\beta$，所以

$$
Q=\frac{\omega_0}{\Delta\omega},
$$
品质因数越高，共振峰越窄，系统对频率的选择性越好。弱阻尼时 $\omega_{\mathrm{r}}\approx\omega_0$，两种共振几乎在同一频率发生，峰值振幅 $A_{\mathrm{r}}\approx Q\cdot\dfrac{F_0}{k}$，是同样大小的静力所产生位移的 $Q$ 倍。

![Steady-state response of a driven damped oscillator for quality factors Q = 0.5, 1, 2, 5 and 10: amplitude A k / F0 (left) and phase phi0 of the displacement relative to the driving force (right) versus omega / omega0; all phase curves pass through -pi/2 at omega = omega0](./plots/forced-response.py)

共振的利用与防止都很重要。收音机靠 $LC$ 回路的电共振选台（$RLC$ 串联电路的方程与受迫振动方程形式相同，见 [5.3.9](/5.3.9)）；核磁共振、乐器的共鸣箱也是共振。另一方面，机器、建筑与桥梁要避免其固有频率与经常出现的驱动频率接近。中国古代早有对共振的认识：据《天中记》记载，蜀人有一个铜盘早晚自鸣，张华解释说它与宫中的钟声相谐，只要改变铜盘的厚薄就能消除。用与酒杯固有频率相同的声音持续激励，可以把酒杯振碎。

1940 年美国 Tacoma 海峡大桥在大风中剧烈扭转振动后断塌，常被当作共振的例子，但这是不准确的：当时风速大致稳定，并没有与桥的固有频率相同的周期性驱动力。桥的扭转振动使周围气流对桥面施加的力与振动同步，相当于负阻尼，振幅自激地增长，这是气动弹性颤振（自激振动），与受迫共振的机理不同。

**例 6.5.1（原子力显微镜）** 原子力显微镜（AFM）的探针装在一根微悬臂的末端，在动态模式下用压电元件以接近悬臂固有频率的频率驱动它振动。探针接近样品表面时，原子间作用力的梯度相当于改变了悬臂的等效劲度系数，使其共振频率移动，在固定驱动频率下振幅与相位随之变化；用激光（光束偏转或干涉）测出这一变化，经反馈控制探针高度，扫描后就得到表面的形貌。悬臂的 $Q$ 越高，共振曲线越陡，测量越灵敏。

## 小结

| 振动 | 方程 | 解与特征 |
|---|---|---|
| 简谐振动 | $\ddot x+\omega_0^2x=0$ | $x=A\cos(\omega_0t+\varphi_0)$；$\omega_0$ 由系统决定，$A$、$\varphi_0$ 由初始条件决定；$E=\frac12kA^2$ |
| 阻尼振动 | $\ddot x+2\beta\dot x+\omega_0^2x=0$ | 欠阻尼 $A_0\mathrm{e}^{-\beta t}\cos(\omega_{\mathrm{d}}t+\varphi_0)$，临界阻尼、过阻尼；$Q=\omega_0/(2\beta)$ |
| 受迫振动 | $\ddot x+2\beta\dot x+\omega_0^2x=\frac{F_0}m\cos\omega t$ | 稳态 $A\cos(\omega t+\varphi_0)$，频率为驱动频率，$A$、$\varphi_0$ 与初始条件无关；$\omega\approx\omega_0$ 时共振 |

简谐振动的合成：同方向同频率用旋转矢量相加；同方向不同频率出现拍，拍频 $\lvert\nu_1-\nu_2\rvert$；互相垂直的振动合成为直线、椭圆或 Lissajous 图形。任意周期振动可以分解为基频与谐频的叠加（Fourier 级数）。

## 思考题

1. 为什么阻尼振动的周期比无阻尼时长？

   **答** $\omega_{\mathrm{d}}=\sqrt{\omega_0^2-\beta^2}<\omega_0$；物理上，阻力总是减慢质点的运动。

2. 弹簧振子竖直悬挂时，重力会改变振动的周期吗？

   **答** 不会。以新的平衡位置（弹簧已伸长 $mg/k$）为原点，回复力仍为 $-kx$，$\omega=\sqrt{k/m}$ 不变，只是平衡位置下移。

3. 受迫振动达到稳态后，驱动力在一个周期内做的功到哪里去了？

   **答** 全部被阻力消耗（转化为热），系统的平均机械能保持不变。
