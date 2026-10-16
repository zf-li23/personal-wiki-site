---
title: 柱坐标与球坐标中的分离变量
source_hash: 808168f319a1
---

鼓、管道、圆柱形的杆、行星和原子都不是矩形；圆盘、圆柱或球上提出的问题，应当在与其边界相适应的坐标系中求解。在这样的坐标系中，**分离变量法**与区间上完全一样（[2.5.4](/2.5.4)），只是分离出的常微分方程不再是 $X''+\lambda X=0$：在极坐标和柱坐标中，径向方程是 **Bessel 方程**；在球坐标中，角向方程是 **Legendre 方程**。于是特征函数是 Bessel 函数与 Legendre 多项式，而不是正弦和余弦；解按 Fourier–Bessel 级数与 Legendre 级数展开，而不是按 Fourier 级数展开。这些特殊函数及其正交性已在 [2.4.10](/2.4.10) 中准备好，Sturm–Liouville 理论（[2.4.12](/2.4.12)）则说明了这些展开为什么存在。本章把这些内容组合起来。下一章讨论无界区域，那里级数让位于积分变换。

## 5.1. 曲线坐标中的 Laplace 算子

### 5.1.1. 极坐标、柱坐标与球坐标

正交曲线坐标中的 **Laplace 算子**已在 [2.2.14](/2.2.14#sec-14.6) 中算出。本课程把**柱坐标**记为 $(r,\theta,z)$，把**球坐标**记为 $(r,\theta,\varphi)$，其中 $r$ 是到原点的距离，$\theta\in[0,\pi]$ 是从 $z$ 轴正向量起的极角，$\varphi\in[0,2\pi)$ 是方位角：

$$
x=r\sin\theta\cos\varphi,\qquad y=r\sin\theta\sin\varphi,\qquad z=r\cos\theta.
$$
这是物理学和大多数偏微分方程教材的约定，与 [2.4.10](/2.4.10) 中的记号 $P_n(\cos\theta)\mathrm{e}^{\mathrm{i}m\varphi}$ 一致；注意字母 $\theta$ 与 $\varphi$ 的角色与 [2.2.12](/2.2.12) 中相反。Laplace 算子为

$$
\begin{aligned}
\text{极坐标：}\quad&\Delta u=u_{rr}+\frac1ru_r+\frac1{r^2}u_{\theta\theta},\\
\text{柱坐标：}\quad&\Delta u=u_{rr}+\frac1ru_r+\frac1{r^2}u_{\theta\theta}+u_{zz},\\
\text{球坐标：}\quad&\Delta u=\frac1{r^2}\big(r^2u_r\big)_r+\frac1{r^2\sin\theta}\big(\sin\theta\,u_\theta\big)_\theta+\frac1{r^2\sin^2\theta}u_{\varphi\varphi}.
\end{aligned}\tag{5.1}
$$
球坐标 Laplace 算子的角向部分 $\Delta_SY=\frac1{\sin\theta}(\sin\theta\,Y_\theta)_\theta+\frac1{\sin^2\theta}Y_{\varphi\varphi}$ 是单位球面上的 Laplace 算子，于是 $\Delta u=\frac1{r^2}(r^2u_r)_r+\frac1{r^2}\Delta_Su$。

坐标奇点（$r=0$，以及球坐标中的 $\theta=0,\pi$）不是物理区域的边界。分离出的方程在这些点处有奇点，我们不给边界条件，而是要求解在那里有界。正是这个"自然"条件选出了 $J_m$ 而不是 $Y_m$，选出了 $P_n$ 而不是 $Q_n$。

### 5.1.2. Helmholtz 方程

在区域 $\Omega$ 上对**波动方程** $u_{tt}=c^2\Delta u$ 或**热方程** $u_t=k\Delta u$ 分离时间与空间变量，令 $u=T(t)v(x)$，得 $T''/(c^2T)=\Delta v/v=-\lambda$ 或 $T'/(k T)=\Delta v/v=-\lambda$。两种情形下空间因子满足同一个方程。

**定义 5.1.1（Helmholtz 方程）** 方程

$$
\Delta v+\lambda v=0\quad\text{在 }\Omega\text{ 内}\tag{5.2}
$$
称为 **Helmholtz 方程**。它与 $\partial\Omega$ 上的齐次边界条件一起构成算子 $-\Delta$ 的**特征值问题**：使 (5.2) 有满足边界条件的非平凡解的数 $\lambda$ 称为特征值，相应的解称为**特征函数**。

这时波动方程的时间因子是 $\cos(c\sqrt\lambda\,t)$、$\sin(c\sqrt\lambda\,t)$，热方程的时间因子是 $\mathrm{e}^{-k\lambda t}$，所以特征值决定了固有频率与衰减速率。它们的基本性质可以像一维 **Sturm–Liouville 问题**那样，由 **Green 第一公式**得到。

**定理 5.1.1** 设 $\Omega\subset\mathbb{R}^n$（$n=2,3$）是边界分段光滑的有界区域，考虑 $\Omega$ 内的 $-\Delta v=\lambda v$，附加 **Dirichlet 边界条件** $v=0$（在 $\partial\Omega$ 上），$v\in C^2(\Omega)\cap C^1(\bar\Omega)$（允许取复值）。

1. 每个特征值都是正实数，且
$$
\lambda=\frac{\displaystyle\int_\Omega\lvert\nabla v\rvert^2\,\mathrm{d}V}{\displaystyle\int_\Omega\lvert v\rvert^2\,\mathrm{d}V}.
$$
2. 属于不同特征值的特征函数正交：$\int_\Omega v\bar w\,\mathrm{d}V=0$。

对 **Neumann 边界条件** $\frac{\partial v}{\partial\boldsymbol{n}}=0$，结论同样成立，只是 $\lambda=0$ 是特征值，对应的特征函数是常数。

**证明** 由线性性，Green 第一公式对复值函数也成立。把它应用于 $\bar v$ 与 $v$，得

$$
\int_\Omega\bar v\,\Delta v\,\mathrm{d}V=\oint_{\partial\Omega}\bar v\frac{\partial v}{\partial\boldsymbol{n}}\,\mathrm{d}S-\int_\Omega\lvert\nabla v\rvert^2\,\mathrm{d}V=-\int_\Omega\lvert\nabla v\rvert^2\,\mathrm{d}V,
$$
因为在 $\partial\Omega$ 上 $v=0$。代入 $\Delta v=-\lambda v$ 即得商的公式，所以 $\lambda$ 是实数且 $\lambda\ge0$。若 $\lambda=0$，则 $\nabla v\equiv\boldsymbol{0}$，$v$ 在 $\Omega$ 的每个连通分支上为常数，再由边界条件知 $v\equiv0$，这对特征函数是不可能的。因此 $\lambda>0$。

对第 2 条，设 $-\Delta v=\lambda v$，$-\Delta w=\mu w$，$\lambda\ne\mu$；由第 1 条，$\mu$ 是实数。两次应用 Green 第一公式并相减，

$$
(\lambda-\mu)\int_\Omega v\bar w\,\mathrm{d}V=\int_\Omega\big(v\Delta\bar w-\bar w\Delta v\big)\,\mathrm{d}V=\oint_{\partial\Omega}\Big(v\frac{\partial\bar w}{\partial\boldsymbol{n}}-\bar w\frac{\partial v}{\partial\boldsymbol{n}}\Big)\mathrm{d}S=0.
$$
对 Neumann 条件，边界项由同样的理由为零。$\square$

与正则 Sturm–Liouville 问题一样，还可以证明更多的结论（这里不加证明地叙述）：对连通区域，Dirichlet 特征值构成序列 $0<\lambda_1<\lambda_2\le\lambda_3\le\cdots\to+\infty$（按重数重复列出），第一特征函数不变号，且特征函数构成完备正交系，因此 $\Omega$ 上每个合理的函数都有**特征函数展开**。特征值编码了几何信息：由 Weyl 定律，平面区域上 $\lambda_j\sim4\pi j/\lvert\Omega\rvert$，所以从鼓的高次泛音可以"听出"它的面积。一般说来，特征值无法用闭合形式算出；对圆盘和球则可以，因为 Helmholtz 方程能够分离变量。

## 5.2. 圆膜的振动

### 5.2.1. 分离变量

半径为 $a$ 的膜沿边缘固定，其位移 $u(r,\theta,t)$ 满足

$$
\begin{cases}
u_{tt}=c^2\Big(u_{rr}+\dfrac1ru_r+\dfrac1{r^2}u_{\theta\theta}\Big),&0\le r<a,\ t>0,\\[2mm]
u(a,\theta,t)=0,\\
u(r,\theta,0)=f(r,\theta),\quad u_t(r,\theta,0)=g(r,\theta).
\end{cases}\tag{5.3}
$$
按 §5.1.2，先求解 Helmholtz 方程 $v_{rr}+\frac1rv_r+\frac1{r^2}v_{\theta\theta}+\lambda v=0$，$v(a,\theta)=0$；由定理 5.1.1，$\lambda>0$。令 $v=R(r)\Theta(\theta)$ 并乘以 $r^2/(R\Theta)$，

$$
\frac{r^2R''+rR'+\lambda r^2R}{R}=-\frac{\Theta''}{\Theta}=\mu.
$$

1. 角向方程 $\Theta''+\mu\Theta=0$ 附加周期条件 $\Theta(\theta+2\pi)=\Theta(\theta)$，因为 $\theta$ 与 $\theta+2\pi$ 表示同一个点。由 [2.4.12](/2.4.12#sec-12.4.1) 表中的周期情形，$\mu=m^2$，$m=0,1,2,\dots$，$\Theta=A\cos m\theta+B\sin m\theta$。
2. 径向方程 $r^2R''+rR'+(\lambda r^2-m^2)R=0$。令 $s=\sqrt\lambda\,r$，它就是 $m$ 阶 Bessel 方程，通解为 $R=CJ_m(\sqrt\lambda\,r)+DY_m(\sqrt\lambda\,r)$。**第二类 Bessel 函数** $Y_m$ 在 $r=0$ 处无界，所以 $D=0$。
3. 边界条件 $R(a)=J_m(\sqrt\lambda\,a)=0$，所以 $\sqrt\lambda\,a$ 是 $J_m$ 的某个正零点 $j_{m,k}$：
$$
\lambda_{mk}=\Big(\frac{j_{m,k}}{a}\Big)^2,\qquad v_{mk}=J_m\Big(\frac{j_{m,k}r}{a}\Big)\cos m\theta,\ J_m\Big(\frac{j_{m,k}r}{a}\Big)\sin m\theta,\qquad k=1,2,\dots
$$

因此圆盘的 Dirichlet 特征值是 Bessel 函数零点的平方除以 $a^2$；$m\ge1$ 时每个特征值有两个线性无关的特征函数（图样旋转一个角度）。每个乘积

$$
u_{mk}=J_m\Big(\frac{j_{m,k}r}{a}\Big)\big(A\cos m\theta+B\sin m\theta\big)\cos(\omega_{mk}t-\delta),\qquad\omega_{mk}=\frac{c\,j_{m,k}}{a},
$$
都是一个驻波，即鼓的一个简正模态。它的节线（$u_{mk}\equiv0$ 的地方）由 $m$ 条直径和 $k-1$ 个圆 $r=a\,j_{m,i}/j_{m,k}$（$i<k$）组成。

![圆膜的六个简正模态及其节线；标题给出频率比 omega_mk / omega_01 = j_mk / j_01](./plots/membrane-modes.py)

相对于基频 $\omega_{01}$ 的频率为

| 模态 $(m,k)$ | $(0,1)$ | $(1,1)$ | $(2,1)$ | $(0,2)$ | $(3,1)$ | $(1,2)$ | $(2,2)$ | $(0,3)$ |
|---|---|---|---|---|---|---|---|---|
| $j_{m,k}$ | $2.4048$ | $3.8317$ | $5.1356$ | $5.5201$ | $6.3802$ | $7.0156$ | $8.4172$ | $8.6537$ |
| $\omega_{mk}/\omega_{01}$ | $1$ | $1.593$ | $2.136$ | $2.295$ | $2.653$ | $2.917$ | $3.500$ | $3.598$ |

弦的泛音是基频的整数倍 $n\omega_1$，人耳把它们听成一个具有确定音色的单一音高。鼓的泛音不是整数倍，间隔也不规则，所以鼓声听起来是打击声，而没有确定的音高。定音鼓通过膜下的空气负载来调音，使模态 $(1,1),(2,1),(3,1)$ 的频率接近 $2:3:4$。

![弦的固有频率（基频的整数倍）与圆膜的固有频率（Bessel 零点之比 j_mk / j_01），按角向指标 m 着色](./plots/drum-spectrum.py)

### 5.2.2. Fourier–Bessel 级数

为满足初始条件，由**叠加原理**把所有模态叠加起来，并把 $f$ 与 $g$ 按特征函数展开。对径向因子，这就是下面的展开，其正交关系已在[定理 10.4.2](/2.4.10#thm-10.4.2) 中证明。

**定义 5.2.1（Fourier–Bessel 级数）** 设 $\nu\ge0$，$j_{\nu,k}$ 是 $J_\nu$ 的正零点，$f$ 在 $[0,a]$ 上关于权 $r$ 可积。级数

$$
f(r)\sim\sum_{k=1}^\infty c_kJ_\nu\Big(\frac{j_{\nu,k}r}{a}\Big),\qquad c_k=\frac{2}{a^2J_{\nu+1}(j_{\nu,k})^2}\int_0^arf(r)J_\nu\Big(\frac{j_{\nu,k}r}{a}\Big)\mathrm{d}r\tag{5.4}
$$
称为 $f$ 的（$\nu$ 阶）**Fourier–Bessel 级数**。

系数公式就是通常的"坐标等于内积除以范数的平方"：在定理 10.4.2 中作代换 $x=r/a$，得 $\int_0^arJ_\nu(j_{\nu,k}r/a)^2\,\mathrm{d}r=\frac{a^2}2J_{\nu+1}(j_{\nu,k})^2$。对分段光滑的 $f$，与 **Fourier 级数**一样，级数在 $0<r<a$ 处收敛于 $\frac12\big(f(r^+)+f(r^-)\big)$（不加证明）。在 $r=a$ 处每一项都为零，所以除非 $f(a)=0$，级数在 $a$ 附近的收敛是不一致的。

把初始数据按双重系 $J_m(j_{m,k}r/a)\cos m\theta$、$J_m(j_{m,k}r/a)\sin m\theta$ 展开（关于 $\theta$ 的 Fourier 级数，其系数再关于 $r$ 展开为 Fourier–Bessel 级数），问题 (5.3) 的解为

$$
u=\sum_{m=0}^\infty\sum_{k=1}^\infty J_m\Big(\frac{j_{m,k}r}{a}\Big)\Big[\big(A_{mk}\cos m\theta+B_{mk}\sin m\theta\big)\cos\omega_{mk}t+\big(C_{mk}\cos m\theta+D_{mk}\sin m\theta\big)\sin\omega_{mk}t\Big],
$$
其中，例如，

$$
A_{mk}=\frac{\displaystyle\int_0^{2\pi}\!\!\int_0^af(r,\theta)J_m\Big(\frac{j_{m,k}r}{a}\Big)\cos m\theta\,r\,\mathrm{d}r\,\mathrm{d}\theta}{\varepsilon_m\pi\cdot\frac{a^2}{2}J_{m+1}(j_{m,k})^2},\qquad\varepsilon_0=2,\ \varepsilon_m=1\ (m\ge1),
$$
$C_{mk}$ 由 $g$ 同样得到，只是多一个因子 $1/\omega_{mk}$。

**例 5.2.1** 设 $a=c=1$，膜从抛物面 $f=1-r^2$ 的形状由静止释放。求膜的运动。

**解** 数据与 $\theta$ 无关，所以只出现 $m=0$；$g=0$ 给出 $C_{0k}=0$。记 $j_k=j_{0,k}$。利用递推关系中的 $(xJ_1)'=xJ_0$ 与 $(x^2J_2)'=x^2J_1$，

$$
\int_0^1rJ_0(j_kr)\,\mathrm{d}r=\frac{J_1(j_k)}{j_k},\qquad\int_0^1r(1-r^2)J_0(j_kr)\,\mathrm{d}r=\frac{2J_2(j_k)}{j_k^2}=\frac{4J_1(j_k)}{j_k^3},
$$
其中第二个积分由一次分部积分得到（$1-r^2$ 在 $r=1$ 处为零），最后一步用到 $J_2(j_k)=\frac{2}{j_k}J_1(j_k)-J_0(j_k)$ 及 $J_0(j_k)=0$。于是 $c_k=\frac{2}{J_1(j_k)^2}\cdot\frac{4J_1(j_k)}{j_k^3}$，

$$
u(r,t)=\sum_{k=1}^\infty\frac{8}{j_k^3J_1(j_k)}J_0(j_kr)\cos(j_kt).
$$
数值上各系数为 $1.108$、$-0.140$、$0.045,\dots$：运动几乎是纯粹的基本模态，因为初始形状已经很像 $J_0(j_1r)$。

## 5.3. 圆柱中的问题

### 5.3.1. 无限长圆柱的冷却

半径为 $a$ 的无限长圆柱，初始温度为 $f(r)$，表面保持温度 $0$。温度只依赖于 $r$ 和 $t$：

$$
u_t=k\Big(u_{rr}+\frac1ru_r\Big),\quad0\le r<a,\qquad u(a,t)=0,\qquad u(r,0)=f(r).
$$
这是 §5.2 中 $m=0$ 的情形，时间因子为 $\mathrm{e}^{-k\lambda t}$：

$$
u(r,t)=\sum_{n=1}^\infty c_n\,\mathrm{e}^{-k j_{0,n}^2t/a^2}J_0\Big(\frac{j_{0,n}r}{a}\Big),\qquad c_n\text{ 由 (5.4) 取 }\nu=0\text{ 给出}.
$$
对均匀的初始温度 $f\equiv u_0$，例 5.2.1 的第一个积分给出 $c_n=\frac{2u_0}{j_{0,n}J_1(j_{0,n})}$。所有项都衰减，$t$ 很大时第一项占主导：$u\approx1.602\,u_0\,\mathrm{e}^{-k j_{0,1}^2t/a^2}J_0(j_{0,1}r/a)$。时间常数 $a^2/(k j_{0,1}^2)$ 与初始温度无关；比较"半径"同为 $a$ 的三种基本形状，可以看出几何的影响：

| 物体 | 第一 Dirichlet 特征值 | 时间常数 $1/(k\lambda_1)$ |
|---|---|---|
| 平板 $\lvert x\rvert<a$ | $(\pi/2a)^2\approx2.47/a^2$ | $0.405\,a^2/k$ |
| 无限长圆柱 $r<a$ | $j_{0,1}^2/a^2\approx5.78/a^2$ | $0.173\,a^2/k$ |
| 球 $r<a$ | $\pi^2/a^2\approx9.87/a^2$ | $0.101\,a^2/k$ |

单位体积的表面积越大，物体冷却得越快。（球的数值来自 §5.4.3 的径向特征函数 $\frac{\sin(\pi r/a)}{r}$。）

### 5.3.2. 有限圆柱中的稳态

考虑圆柱 $0\le r<a$，$0<z<h$，侧面和底面保持温度 $0$，顶面保持轴对称的温度 $f(r)$。稳态温度满足 **Laplace 方程**

$$
u_{rr}+\frac1ru_r+u_{zz}=0,\qquad u(a,z)=0,\quad u(r,0)=0,\quad u(r,h)=f(r).
$$
齐次条件在侧面上，所以特征值问题关于 $r$：$u=R(r)Z(z)$ 给出 $(rR')'+\lambda rR=0$，$R(a)=0$，$R$ 有界，从而 $R=J_0(j_{0,k}r/a)$，$\lambda=(j_{0,k}/a)^2$。再由 $Z''-\lambda Z=0$ 与 $Z(0)=0$ 得 $Z=\sinh(j_{0,k}z/a)$，顶面的条件确定系数：

$$
u(r,z)=\sum_{k=1}^\infty c_k\frac{\sinh(j_{0,k}z/a)}{\sinh(j_{0,k}h/a)}J_0\Big(\frac{j_{0,k}r}{a}\Big),\qquad c_k\text{ 为 }f\text{ 的 Fourier–Bessel 系数}.
$$

若改为顶面和底面保持 $0$、侧面 $u(a,z)=g(z)$，则特征值问题关于 $z$：$Z=\sin\frac{n\pi z}{h}$，径向方程变为 $R''+\frac1rR'-\big(\frac{n\pi}h\big)^2R=0$，即变形 Bessel 方程，其有界解为 $I_0\big(\frac{n\pi r}{h}\big)$（[2.4.10](/2.4.10#sec-10.4.4)）。于是

$$
u(r,z)=\sum_{n=1}^\infty b_n\frac{I_0(n\pi r/h)}{I_0(n\pi a/h)}\sin\frac{n\pi z}{h},\qquad b_n=\frac2h\int_0^hg(z)\sin\frac{n\pi z}{h}\,\mathrm{d}z.
$$
一般规则与矩形上相同：带齐次边界条件的方向提供振荡的特征函数，另一个方向则用不振荡的函数（$\sinh$、$I_0$）来拟合其余的边界数据。

## 5.4. 球中的问题

### 5.4.1. 轴对称解与 Legendre 多项式

在球 $r<a$ 中求解 Laplace 方程的 Dirichlet 问题，边界值与 $\varphi$ 无关：

$$
\Delta u=0\ \ (r<a),\qquad u(a,\theta)=f(\theta),\quad0\le\theta\le\pi.
$$
此时解与 $\varphi$ 无关。在 (5.1) 中令 $u=R(r)\Theta(\theta)$ 并乘以 $r^2/(R\Theta)$，

$$
\frac{(r^2R')'}{R}=-\frac{(\sin\theta\,\Theta')'}{\sin\theta\,\Theta}=\mu.
$$
令 $x=\cos\theta$，则 $\frac{\mathrm{d}}{\mathrm{d}\theta}=-\sin\theta\frac{\mathrm{d}}{\mathrm{d}x}$，角向方程变为

$$
\big((1-x^2)\Theta_x\big)_x+\mu\Theta=0,\qquad-1<x<1,
$$
即 $\mu=\nu(\nu+1)$ 的 Legendre 方程。两极 $\theta=0,\pi$ 是球的内点，所以 $\Theta$ 在 $x=\pm1$ 处必须有界；由 [2.4.10](/2.4.10#sec-10.2.3)，这恰好在 $\mu=n(n+1)$（$n=0,1,2,\dots$）时发生，此时 $\Theta=P_n(\cos\theta)$。径向方程 $r^2R''+2rR'-n(n+1)R=0$ 是 Euler 方程（[2.4.9](/2.4.9)），解为 $r^n$ 与 $r^{-(n+1)}$；球心处的有界性选出 $r^n$。所以

$$
u(r,\theta)=\sum_{n=0}^\infty A_n\Big(\frac ra\Big)^nP_n(\cos\theta),\qquad A_n=\frac{2n+1}{2}\int_0^\pi f(\theta)P_n(\cos\theta)\sin\theta\,\mathrm{d}\theta,\tag{5.5}
$$
其中 $A_n$ 是 $f$ 关于变量 $x=\cos\theta$ 的 Legendre 级数的系数（因子 $\sin\theta\,\mathrm{d}\theta=-\mathrm{d}x$ 来自变量代换）。对外问题（$r>a$，$r\to\infty$ 时 $u\to0$），改为保留 $r^{-(n+1)}$，得 $u=\sum A_n(a/r)^{n+1}P_n(\cos\theta)$。

**例 5.4.1** 在 $r<a$ 内求解 $\Delta u=0$，$u(a,\theta)=\cos^2\theta$。

**解** 无需积分：由 $P_2(x)=\frac{3x^2-1}2$ 得 $x^2=\frac13P_0(x)+\frac23P_2(x)$。由 (5.5)，

$$
u=\frac13+\frac23\Big(\frac ra\Big)^2P_2(\cos\theta)=\frac13+\frac{3z^2-r^2}{3a^2}.
$$
在直角坐标中 $u=\frac13+\frac{2z^2-x^2-y^2}{3a^2}$，可以直接验证 $\Delta u=\frac{4-2-2}{3a^2}=0$。球心处的值为 $\frac13$，即 $\cos^2\theta$ 在球面上的平均值，正如调和函数的平均值性质（[2.5.8](/2.5.8)）所预言的。

**例 5.4.2（匀强电场中的导体球）** 把接地的导体球 $r=a$ 放入沿 $z$ 轴方向、强度为 $E_0$ 的匀强电场中。电势满足：$r>a$ 时 $\Delta u=0$，在 $r=a$ 上 $u=0$，$r$ 很大时 $u\approx-E_0z=-E_0r\cos\theta$。求 $u$。

**解** 边界数据只含 $P_1(\cos\theta)=\cos\theta$，所以试探 $u=\big(Ar+Br^{-2}\big)\cos\theta$，它是 $n=1$ 时两个径向解的组合。无穷远处的条件给出 $A=-E_0$，$u(a,\theta)=0$ 给出 $B=E_0a^3$：

$$
u=-E_0\Big(r-\frac{a^3}{r^2}\Big)\cos\theta.
$$
项 $E_0a^3\cos\theta/r^2$ 是偶极子的电势，即球面上感应电荷产生的场。球面上的电场强度为 $-u_r(a,\theta)=3E_0\cos\theta$：在两极处是外加电场的三倍。

### 5.4.2. 球面调和函数

没有轴对称性时，分离 $u=R(r)Y(\theta,\varphi)$，得 $(r^2R')'=\mu R$ 与 $\Delta_SY+\mu Y=0$，再令 $Y=\Theta(\theta)\Phi(\varphi)$。与圆盘一样，关于 $\varphi$ 的周期性给出 $\Phi=\mathrm{e}^{\mathrm{i}m\varphi}$，$m\in\mathbb{Z}$；而 $\Theta$ 在 $x=\cos\theta$ 下满足连带 Legendre 方程

$$
(1-x^2)\Theta''-2x\Theta'+\Big(\mu-\frac{m^2}{1-x^2}\Big)\Theta=0.
$$
它有在 $x=\pm1$ 处有界的解，当且仅当 $\mu=n(n+1)$ 且 $n\ge\lvert m\rvert$（不加证明），此时解是下面的 $P_n^{\lvert m\rvert}(x)$ 的常数倍。

**定义 5.4.1（球面调和函数）** 对整数 $0\le m\le n$，函数

$$
P_n^m(x)=(1-x^2)^{m/2}\frac{\mathrm{d}^m}{\mathrm{d}x^m}P_n(x)
$$
称为**连带 Legendre 函数**。对整数 $n\ge0$ 与 $\lvert m\rvert\le n$，单位球面上的函数

$$
Y_n^m(\theta,\varphi)=P_n^{\lvert m\rvert}(\cos\theta)\,\mathrm{e}^{\mathrm{i}m\varphi}
$$
称为 $n$ 次**球面调和函数**（常乘以归一化常数，这里略去）。

**定理 5.4.1** 球面调和函数有以下性质（不加证明）。

1. $\Delta_SY_n^m=-n(n+1)Y_n^m$：$n$ 次球面调和函数是 $-\Delta_S$ 属于特征值 $n(n+1)$ 的特征函数，该特征值的重数为 $2n+1$；
2. 它们在球面上关于面积元 $\mathrm{d}S=\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$ 正交，且系 $\{Y_n^m\}$ 完备，所以球面上每个平方可积函数都有 Laplace 级数 $f=\sum_{n,m}a_{nm}Y_n^m$；
3. $r^nY_n^m(\theta,\varphi)$ 是 $x,y,z$ 的 $n$ 次齐次调和多项式，而这种多项式在球面上的限制恰好就是 $n$ 次球面调和函数。

例如 $n=1$ 时：$rP_1(\cos\theta)=z$，$rP_1^1(\cos\theta)\mathrm{e}^{\pm\mathrm{i}\varphi}=r\sin\theta\,\mathrm{e}^{\pm\mathrm{i}\varphi}=x\pm\mathrm{i}y$，这是三个 1 次调和多项式。球中的一般 Dirichlet 问题的解为 $u=\sum_{n,m}a_{nm}(r/a)^nY_n^m$，其中 $a_{nm}$ 是边界值的 Laplace 级数系数。

![n = 0, …, 3 的球面调和函数的实部 P_n^m(cos theta) cos(m phi)：其零点集由 m 个过两极的大圆和 n - m 条纬线组成](./plots/spherical-harmonics.py)

凡是具有球对称性的问题都会出现球面调和函数：电势的多极展开、地球的引力场、宇宙微波背景辐射的角分布，以及原子轨道的角向部分。在氢原子中，对中心势场中的 Schrödinger 方程分离变量，恰好得到特征值问题 $\Delta_SY=-\ell(\ell+1)Y$；记作 s、p、d、f 的轨道对应于 $\ell=0,1,2,3$，而 $m$ 的 $2\ell+1$ 个取值说明了每个能级的简并度。

### 5.4.3. Helmholtz 方程的径向方程

对球中的波动方程或热方程，Helmholtz 方程 $\Delta v+\lambda v=0$ 分离为 $Y_n^m$ 与径向方程

$$
r^2R''+2rR'+\big(\lambda r^2-n(n+1)\big)R=0.
$$
代换 $R=r^{-1/2}S$ 把它化为关于 $S$ 的 $n+\frac12$ 阶 Bessel 方程，所以有界解是球 Bessel 函数 $j_n(\sqrt\lambda\,r)$，其中 $j_n(x)=\sqrt{\frac{\pi}{2x}}J_{n+1/2}(x)$。由[定理 10.4.1](/2.4.10#thm-10.4.1)，$J_{1/2}$ 是初等函数，$j_0(x)=\frac{\sin x}{x}$。因此对径向对称的问题（$n=0$），特征函数可以显式写出：球的 Dirichlet 特征函数为 $\frac{\sin(k\pi r/a)}{r}$，$\lambda=(k\pi/a)^2$，这给出了 §5.3.1 表格的最后一行。

## 小结

| 区域 | 分离出的方程 | 特征函数 | 特征值条件 |
|---|---|---|---|
| 圆盘 $r<a$（Helmholtz 方程） | $\Theta''+m^2\Theta=0$；关于 $\sqrt\lambda\,r$ 的 $m$ 阶 Bessel 方程 | $J_m(j_{m,k}r/a)\cos m\theta$，$J_m(j_{m,k}r/a)\sin m\theta$ | $\sqrt\lambda\,a=j_{m,k}$ |
| 圆柱，侧面齐次 | 关于 $r$ 的 Bessel 方程；$Z''=\lambda Z$ | $J_0(j_{0,k}r/a)$，乘以关于 $z$ 的 $\sinh$ 或 $\cosh$ | $J_0(\sqrt\lambda\,a)=0$ |
| 圆柱，顶面与底面齐次 | $Z''+\lambda Z=0$；关于 $r$ 的变形 Bessel 方程 | $\sin(n\pi z/h)$，乘以 $I_0(n\pi r/h)$ | $\lambda=(n\pi/h)^2$ |
| 球，Laplace 方程 | 关于 $r$ 的 Euler 方程；关于 $\cos\theta$ 的连带 Legendre 方程；$\Phi''+m^2\Phi=0$ | $r^nY_n^m(\theta,\varphi)$ | $\mu=n(n+1)$，两极处有界 |
| 球，Helmholtz 方程 | 关于 $r$ 的球 Bessel 方程 | $j_n(\sqrt\lambda\,r)Y_n^m$ | $j_n(\sqrt\lambda\,a)=0$ |

所有情形的方法都相同：在与边界相适应的坐标系中写出 $\Delta$，分离变量，对角度变量施加周期性、在坐标奇点处要求有界，在具有齐次条件的方向上求解特征值问题，再把其余数据按所得的正交系（Fourier、Fourier–Bessel、Legendre 或 Laplace 级数）展开。
